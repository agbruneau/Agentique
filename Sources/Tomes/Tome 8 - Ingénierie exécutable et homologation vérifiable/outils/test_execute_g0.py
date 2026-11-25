#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Tests unitaires et d'integration pour la barriere G0 (execute_g0.py)."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import venv

from jsonschema import Draft202012Validator
import pytest

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import compute_excerpt_sha256, compute_lf_sha256_bytes
import execute_g0
from verifie_specs import extract_ssot_schemas_from_arch

_MANUEL_DIR = _TOOLS_DIR.parent
_REPO_ROOT = _MANUEL_DIR.parents[2]
_REAL_TROUSSE = _MANUEL_DIR / "trousse"
_REAL_OPA = next(
    (
        p
        for p in (
            _REAL_TROUSSE / ".tools" / "opa.exe",
            _REAL_TROUSSE / ".tools" / "opa",
            Path(shutil.which("opa")) if shutil.which("opa") else None,
        )
        if p is not None and p.is_file()
    ),
    None,
)


def _find_site_packages(venv_dir: Path) -> Path:
    return next(venv_dir.glob("**/site-packages"))


def _write_lf(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.replace("\r\n", "\n").encode("utf-8"))


@pytest.fixture(scope="module")
def rapports_g0_schema() -> dict:
    arch_text = (_MANUEL_DIR / "specs" / "architecture-trousse-g0.md").read_text(encoding="utf-8")
    schemas, errs = extract_ssot_schemas_from_arch(arch_text)
    assert errs == []
    return schemas["RapportsG0Output"]


@pytest.fixture(scope="module")
def base_clean_venv(tmp_path_factory: pytest.TempPathFactory) -> Path:
    venv_dir = tmp_path_factory.mktemp("g0_clean_venv")
    venv.EnvBuilder(with_pip=False).create(venv_dir)
    sp = _find_site_packages(venv_dir)
    real_sp_candidates = list((_REAL_TROUSSE / ".venv").glob("**/site-packages")) if (_REAL_TROUSSE / ".venv").is_dir() else []
    if real_sp_candidates:
        _write_lf(sp / "trousse_deps.pth", str(real_sp_candidates[0]) + "\n")
    return venv_dir


def _build_valid_trousse(tmp_path: Path, base_venv: Path) -> Path:
    trousse = tmp_path / "trousse"
    trousse.mkdir(parents=True, exist_ok=True)
    shutil.copytree(base_venv, trousse / ".venv")

    _write_lf(
        trousse / "pyproject.toml",
        '[project]\nname = "trousse-test"\nversion = "1.0.0"\nrequires-python = ">=3.12"\nlicense = "MIT"\n'
        '[tool.pytest.ini_options]\ntestpaths = ["tests"]\npythonpath = ["."]\n',
    )
    _write_lf(
        trousse / "requirements.lock",
        "jsonschema==4.26.0 \\\n    --hash=sha256:" + ("a" * 64) + "\n"
        "pytest==9.2.0 --hash=sha256:" + ("b" * 64) + "\n",
    )
    _write_lf(
        trousse / "spdx-allowlist.json",
        json.dumps(
            {
                "allowed": ["MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "PSF-2.0", "MPL-2.0", "CC0-1.0"],
                "forbidden_substrings": ["GPL", "AGPL", "LGPL", "SSPL", "Proprietary"],
            },
            indent=2,
        )
        + "\n",
    )

    _write_lf(
        trousse / "schemas" / "sample.schema.json",
        json.dumps(
            {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "x-license": "MIT",
                "title": "SampleAction",
                "type": "object",
                "additionalProperties": False,
                "required": ["action", "ok"],
                "properties": {
                    "action": {"type": "string"},
                    "ok": {"type": "boolean"},
                },
            },
            indent=2,
        )
        + "\n",
    )

    _write_lf(
        trousse / "harness_proto" / "__init__.py",
        "# SPDX-License-Identifier: MIT\n",
    )
    _write_lf(
        trousse / "harness_proto" / "pipeline.py",
        "# SPDX-License-Identifier: MIT\n"
        "# CA-G0-SYNC-BEGIN:G0-EX-CH01-02\n"
        "def run_step(x: int) -> int:\n"
        "    return x + 1\n"
        "# CA-G0-SYNC-END:G0-EX-CH01-02\n",
    )
    _write_lf(
        trousse / "tests" / "test_pipeline.py",
        "# SPDX-License-Identifier: MIT\n"
        "from harness_proto.pipeline import run_step\n\n"
        "def test_run_step_ok() -> None:\n"
        "    assert run_step(1) == 2\n",
    )

    _write_lf(
        trousse / "policies_opa" / "rule_of_two.rego",
        "# SPDX-License-Identifier: MIT\n"
        "package agentique.rule_of_two\n"
        "import rego.v1\n\n"
        "default allow := false\n\n"
        "# CA-G0-SYNC-BEGIN:G0-EX-CH03-01\n"
        "allow if {\n"
        "    input.safe == true\n"
        "}\n"
        "# CA-G0-SYNC-END:G0-EX-CH03-01\n",
    )
    _write_lf(
        trousse / "policies_opa" / "rule_of_two_test.rego",
        "# SPDX-License-Identifier: MIT\n"
        "package agentique.rule_of_two_test\n"
        "import rego.v1\n"
        "import data.agentique.rule_of_two\n\n"
        "test_allow_safe if {\n"
        "    rule_of_two.allow with input as {\"safe\": true}\n"
        "}\n\n"
        "test_deny_unsafe if {\n"
        "    not rule_of_two.allow with input as {\"safe\": false}\n"
        "}\n",
    )

    vec_files = []
    for suite in ("rfc8785", "nist_acvp", "a2a_tck", "owasp_src055"):
        rel = f"{suite}/vec.json"
        content = json.dumps({"suite": suite, "ok": True}) + "\n"
        vec_path = trousse / "vectors" / rel
        _write_lf(vec_path, content)
        raw = vec_path.read_bytes()
        vec_files.append(
            {
                "suite": suite,
                "relative_path": rel,
                "sha256": compute_lf_sha256_bytes(raw),
                "byte_length": len(raw),
            }
        )
    _write_lf(
        trousse / "vectors" / "vectors-manifest.json",
        json.dumps(
            {
                "schema_version": "1.0",
                "freeze_date": "2026-12-02",
                "file_count": len(vec_files),
                "files": vec_files,
            },
            indent=2,
        )
        + "\n",
    )
    return trousse


def test_run_g0_nominal_pass_and_schema_valid(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None, "Binaire opa requis pour le test nominal G0"
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    out_report = tmp_path / "aq" / "rapports-g0.json"

    rc = execute_g0.run_g0(trousse, out_report)
    assert rc == 0
    assert out_report.is_file()

    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["overall_status"] == "PASS"
    assert report["exit_code"] == 0
    assert report["spdx_check"]["passed"] is True
    assert report["lockfile_check"]["passed"] is True
    assert report["schema_validation"]["passed"] is True
    assert report["opa_check"]["coverage_pct"] == 100.0
    assert report["opa_check"]["tests_failed"] == 0
    assert report["pytest_check"]["passed"] == 1
    assert report["pytest_check"]["failed"] == 0
    assert report["pytest_check"]["skipped"] == 0
    assert "G0-EX-CH01-02" in report["synced_excerpts"]
    ex = report["synced_excerpts"]["G0-EX-CH01-02"]
    assert ex["sha256"] == compute_excerpt_sha256(["def run_step(x: int) -> int:", "    return x + 1"])


def test_g0_fails_on_missing_default_deny_rego(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    _write_lf(
        trousse / "policies_opa" / "rule_of_two.rego",
        "# SPDX-License-Identifier: MIT\n"
        "package agentique.rule_of_two\n"
        "import rego.v1\n"
        "allow if { input.safe == true }\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["overall_status"] == "FAIL"
    assert report["opa_check"]["missing_default_deny"] == ["policies_opa/rule_of_two.rego"]


def test_g0_fails_on_rego_coverage_below_100(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    _write_lf(
        trousse / "policies_opa" / "rule_of_two.rego",
        "# SPDX-License-Identifier: MIT\n"
        "package agentique.rule_of_two\n"
        "import rego.v1\n"
        "default allow := false\n"
        "allow if { input.safe == true }\n"
        "uncovered_rule if { input.never_tested == 42 }\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["opa_check"]["coverage_pct"] < 100.0


def test_g0_fails_on_lgpl_package_in_venv(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    sp = _find_site_packages(trousse / ".venv")
    _write_lf(
        sp / "bad_copyleft-1.0.dist-info" / "METADATA",
        "Metadata-Version: 2.4\nName: bad-copyleft\nVersion: 1.0\nLicense-Expression: LGPL-3.0-or-later\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["spdx_check"]["passed"] is False
    assert any("LGPL" in v for v in report["spdx_check"]["violations"])


def test_g0_fails_on_missing_spdx_header(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    _write_lf(trousse / "harness_proto" / "__init__.py", "# pas de spdx\n")
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["spdx_check"]["passed"] is False


def test_g0_fails_on_unpinned_requirements_lock(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    _write_lf(trousse / "requirements.lock", "jsonschema>=4.26.0\n")
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["lockfile_check"]["passed"] is False


def test_g0_fails_on_nonstrict_schema(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    _write_lf(
        trousse / "schemas" / "sample.schema.json",
        json.dumps(
            {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "x-license": "MIT",
                "type": "object",
                "additionalProperties": True,
                "properties": {"x": {"$ref": "https://example.com/remote.json"}},
            }
        )
        + "\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["schema_validation"]["passed"] is False
    assert len(report["schema_validation"]["strict_violations"]) >= 2


def test_g0_fails_on_tampered_vector(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    _write_lf(trousse / "vectors" / "rfc8785" / "vec.json", '{"tampered": true}\n')
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["third_party_vectors"]["rfc8785"]["passed"] is False


def test_g0_fails_on_tools_lock_opa_sha256_mismatch(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("OPA_BIN", raising=False)
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    opa_name = "opa.exe" if os.name == "nt" else "opa"
    tools_dir = trousse / ".tools"
    tools_dir.mkdir(parents=True, exist_ok=True)
    (tools_dir / opa_name).write_bytes(b"corrupted-opa-binary")
    _write_lf(
        trousse / "tools-lock.json",
        json.dumps(
            {
                "tool": "opa",
                "version": "1.22.4",
                "sha256": "f" * 64,
                "relative_path": f".tools/{opa_name}",
            }
        )
        + "\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["platform"]["opa_version"] == "hash-mismatch"


def test_g0_passes_with_verified_dot_tools_opa(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.delenv("OPA_BIN", raising=False)
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    opa_name = "opa.exe" if os.name == "nt" else "opa"
    dst_opa = trousse / ".tools" / opa_name
    dst_opa.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.link(_REAL_OPA, dst_opa)
    except OSError:
        shutil.copy2(_REAL_OPA, dst_opa)
    real_sha = hashlib.sha256(dst_opa.read_bytes()).hexdigest()
    real_lock_path = _REAL_TROUSSE / "tools-lock.json"
    expected_ver = json.loads(real_lock_path.read_text(encoding="utf-8"))["version"] if real_lock_path.is_file() else "1.22.4"
    _write_lf(
        trousse / "tools-lock.json",
        json.dumps(
            {
                "tool": "opa",
                "version": expected_ver,
                "sha256": real_sha,
                "relative_path": f".tools/{opa_name}",
            }
        )
        + "\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc == 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["platform"]["opa_sha256"] == real_sha


def test_g0_fails_on_pytest_failure_and_skip(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    _write_lf(
        trousse / "tests" / "test_pipeline.py",
        "# SPDX-License-Identifier: MIT\n"
        "import pytest\n"
        "def test_ok() -> None:\n    assert True\n"
        "def test_skip() -> None:\n    pytest.skip('interdit a G0')\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["pytest_check"]["skipped"] == 1


def test_g0_fails_on_synced_excerpt_over_40_lines(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    body = "\n".join(f"x_{i} = {i}" for i in range(41))
    _write_lf(
        trousse / "harness_proto" / "pipeline.py",
        "# SPDX-License-Identifier: MIT\n"
        "def run_step(x: int) -> int:\n    return x + 1\n"
        "# CA-G0-SYNC-BEGIN:G0-EX-CH01-02\n"
        f"{body}\n"
        "# CA-G0-SYNC-END:G0-EX-CH01-02\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert "G0-EX-CH01-02" not in report["synced_excerpts"]


def test_g0_verify_sync_manifest_and_book_registre(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    book = tmp_path / "book"
    (book / "specs").mkdir(parents=True, exist_ok=True)
    shutil.copy2(_MANUEL_DIR / "specs" / "architecture-trousse-g0.md", book / "specs" / "architecture-trousse-g0.md")
    _write_lf(
        book / "outils" / "tool_ok.py",
        "# SPDX-License-Identifier: MIT\nVALUE = 1\n",
    )
    _write_lf(
        book / "specs" / "manifest.json",
        json.dumps(
            {
                "synced_excerpts_catalog": [
                    {
                        "id": "G0-EX-CH01-02",
                        "unit": "ch01",
                        "source_path": "harness_proto/pipeline.py",
                        "max_lines": 32,
                        "is_full_file": False,
                    },
                    {
                        "id": "G0-EX-CH03-01",
                        "unit": "ch03",
                        "source_path": "policies_opa/rule_of_two.rego",
                        "max_lines": 28,
                        "is_full_file": False,
                    },
                ]
            },
            indent=2,
        )
        + "\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc_ok = execute_g0.main(
        [
            "--book-dir",
            str(book),
            "--trousse-dir",
            str(trousse),
            "--output",
            str(out_report),
            "--verify-sync-manifest",
        ]
    )
    assert rc_ok == 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert set(report["synced_excerpts"].keys()) == {"G0-EX-CH01-02", "G0-EX-CH03-01"}

    # Un registre SSOT malforme sous book/registre doit faire echouer G0
    _write_lf(book / "registre" / "specifications-lplus.json", json.dumps({"invalide": True}) + "\n")
    rc_bad = execute_g0.run_g0(trousse, out_report, book_dir=book, verify_sync_manifest=True)
    assert rc_bad != 0


def test_g0_rejects_default_deny_placed_after_rule(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    _write_lf(
        trousse / "policies_opa" / "rule_of_two.rego",
        "# SPDX-License-Identifier: MIT\n"
        "package agentique.rule_of_two\n"
        "import rego.v1\n\n"
        "allow if {\n"
        "    input.safe == true\n"
        "}\n\n"
        "default allow := false\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    assert report["opa_check"]["missing_default_deny"] == ["policies_opa/rule_of_two.rego"]


def test_g0_validates_inherited_registries_and_self_validates_report(
    tmp_path: Path,
    base_clean_venv: Path,
    rapports_g0_schema: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    book = tmp_path / "book"
    (book / "specs").mkdir(parents=True, exist_ok=True)
    shutil.copy2(_MANUEL_DIR / "specs" / "architecture-trousse-g0.md", book / "specs" / "architecture-trousse-g0.md")
    _write_lf(book / "outils" / "tool_ok.py", "# SPDX-License-Identifier: MIT\nVALUE = 1\n")
    _write_lf(
        book / "specs" / "manifest.json",
        json.dumps(
            {
                "synced_excerpts_catalog": [
                    {
                        "id": "G0-EX-CH01-02",
                        "unit": "ch01",
                        "source_path": "harness_proto/pipeline.py",
                        "max_lines": 32,
                        "is_full_file": False,
                    },
                    {
                        "id": "G0-EX-CH03-01",
                        "unit": "ch03",
                        "source_path": "policies_opa/rule_of_two.rego",
                        "max_lines": 28,
                        "is_full_file": False,
                    },
                ]
            },
            indent=2,
        )
        + "\n",
    )

    # Peupler les 4 registres herites valides
    _write_lf(
        book / "registre" / "ancres-chronologiques.json",
        json.dumps(
            {
                "freeze_date": "2026-12-02",
                "anchors": [{"key": "ANC-1", "statut_preuve": "l_plus", "source_l_plus_id": "SRC-001"}],
            }
        )
        + "\n",
    )
    _write_lf(
        book / "registre" / "faits-empiriques.json",
        json.dumps(
            {
                "freeze_date": "2026-12-02",
                "facts": [{"id": "FACT-1", "statut_preuve": "l_plus", "source_l_plus_id": "SRC-001"}],
            }
        )
        + "\n",
    )
    _write_lf(
        book / "registre" / "glossaire-termes.json",
        json.dumps(
            {
                "freeze_date": "2026-12-02",
                "terms": [
                    {
                        "fr": f"Terme {i}",
                        "en": f"Term {i}",
                        "definition": f"Definition {i}.",
                        "chapitre_proprietaire": "ch01",
                    }
                    for i in range(12)
                ],
            }
        )
        + "\n",
    )
    _write_lf(
        book / "recherche" / "registre-statut-f.json",
        json.dumps(
            {
                "freeze_date": "2026-12-02",
                "blocked": [{"url": "https://example.invalid/blocked", "status": "F", "included_in_evidence": False}],
            }
        )
        + "\n",
    )

    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc_ok = execute_g0.run_g0(trousse, out_report, book_dir=book, verify_sync_manifest=True)
    assert rc_ok == 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    Draft202012Validator(rapports_g0_schema).validate(report)
    # 1 schema.json + 4 registres herites + 1 RapportsG0Output = 6
    assert report["schema_validation"]["schemas_checked"] == 6

    # Violation 1 : ancre sans statut_preuve == l_plus
    _write_lf(
        book / "registre" / "ancres-chronologiques.json",
        json.dumps({"freeze_date": "2026-12-02", "anchors": [{"key": "ANC-1", "statut_preuve": "a_reancrer"}]}) + "\n",
    )
    assert execute_g0.run_g0(trousse, out_report, book_dir=book) != 0
    assert json.loads(out_report.read_text(encoding="utf-8"))["schema_validation"]["passed"] is False

    # Restaurer ancre, casser registre-statut-f.json (included_in_evidence=True)
    _write_lf(
        book / "registre" / "ancres-chronologiques.json",
        json.dumps({"freeze_date": "2026-12-02", "anchors": [{"key": "ANC-1", "statut_preuve": "l_plus"}]}) + "\n",
    )
    _write_lf(
        book / "recherche" / "registre-statut-f.json",
        json.dumps(
            {
                "freeze_date": "2026-12-02",
                "blocked": [{"url": "https://example.invalid/blocked", "status": "F", "included_in_evidence": True}],
            }
        )
        + "\n",
    )
    assert execute_g0.run_g0(trousse, out_report, book_dir=book) != 0

    # Restaurer statut F, casser glossaire (< 12 termes)
    _write_lf(
        book / "recherche" / "registre-statut-f.json",
        json.dumps(
            {
                "freeze_date": "2026-12-02",
                "blocked": [{"url": "https://example.invalid/blocked", "status": "F", "included_in_evidence": False}],
            }
        )
        + "\n",
    )
    _write_lf(
        book / "registre" / "glossaire-termes.json",
        json.dumps({"freeze_date": "2026-12-02", "terms": []}) + "\n",
    )
    assert execute_g0.run_g0(trousse, out_report, book_dir=book) != 0

    # Restaurer glossaire, casser faits-empiriques.json (statut_preuve != l_plus)
    _write_lf(
        book / "registre" / "glossaire-termes.json",
        json.dumps(
            {
                "freeze_date": "2026-12-02",
                "terms": [
                    {
                        "fr": f"Terme {i}",
                        "en": f"Term {i}",
                        "definition": f"Definition {i}.",
                        "chapitre_proprietaire": "ch01",
                    }
                    for i in range(12)
                ],
            }
        )
        + "\n",
    )
    _write_lf(
        book / "registre" / "faits-empiriques.json",
        json.dumps({"freeze_date": "2026-12-02", "facts": [{"id": "FACT-1", "statut_preuve": "a_reancrer"}]}) + "\n",
    )
    assert execute_g0.run_g0(trousse, out_report, book_dir=book) != 0

    # Restaurer faits et verifier que l'auto-validation RapportsG0Output bloque si le schema du rapport echoue
    _write_lf(
        book / "registre" / "faits-empiriques.json",
        json.dumps({"freeze_date": "2026-12-02", "facts": [{"id": "FACT-1", "statut_preuve": "l_plus"}]}) + "\n",
    )
    strict_rapports = json.loads(json.dumps(rapports_g0_schema))
    strict_rapports["required"] = list(strict_rapports["required"]) + ["champ_force_absent"]
    monkeypatch.setattr(
        execute_g0,
        "extract_ssot_schemas_from_arch",
        lambda _txt: ({"RapportsG0Output": strict_rapports}, []),
    )
    assert execute_g0.run_g0(trousse, out_report, book_dir=book, verify_sync_manifest=True) != 0
    bad_self = json.loads(out_report.read_text(encoding="utf-8"))
    assert bad_self["schema_validation"]["passed"] is False
    assert any("RapportsG0Output" in v for v in bad_self["schema_validation"]["strict_violations"])
