#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Tests unitaires et d'intégration pour la barrière G0 du Compendium (execute_g0.py)."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import venv
from pathlib import Path

from jsonschema import Draft202012Validator
import pytest

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import compute_excerpt_sha256, compute_lf_sha256_bytes  # noqa: E402
import execute_g0  # noqa: E402
from verifie_specs import extract_ssot_schemas_from_arch  # noqa: E402

_COMPENDIUM_BOOK_DIR = _TOOLS_DIR.parent
_REPO_ROOT = _COMPENDIUM_BOOK_DIR.parent.parent
_TOME8_DIR = _REPO_ROOT / "Tomes" / "Tome 8 - Ingénierie exécutable et homologation vérifiable"
_REAL_TROUSSE = _TOME8_DIR / "trousse"
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
    arch_text = (_TOME8_DIR / "specs" / "architecture-trousse-g0.md").read_text(encoding="utf-8")
    schemas, errs = extract_ssot_schemas_from_arch(arch_text)
    assert errs == []
    return schemas["RapportsG0Output"]


@pytest.fixture(scope="module")
def base_clean_venv(tmp_path_factory: pytest.TempPathFactory) -> Path:
    venv_dir = tmp_path_factory.mktemp("g0_clean_venv_cmp")
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
                "properties": {"action": {"type": "string"}, "ok": {"type": "boolean"}},
            },
            indent=2,
        )
        + "\n",
    )
    _write_lf(trousse / "harness_proto" / "__init__.py", "# SPDX-License-Identifier: MIT\n")
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
        "allow if {\n    input.safe == true\n}\n"
        "# CA-G0-SYNC-END:G0-EX-CH03-01\n",
    )
    _write_lf(
        trousse / "policies_opa" / "rule_of_two_test.rego",
        "# SPDX-License-Identifier: MIT\n"
        "package agentique.rule_of_two_test\n"
        "import rego.v1\n"
        "import data.agentique.rule_of_two\n\n"
        "test_allow_safe if {\n    rule_of_two.allow with input as {\"safe\": true}\n}\n\n"
        "test_deny_unsafe if {\n    not rule_of_two.allow with input as {\"safe\": false}\n}\n",
    )

    vec_files = []
    for suite in ("rfc8785", "nist_acvp", "a2a_tck", "owasp_src055"):
        rel = f"{suite}/vec.json"
        content = json.dumps({"suite": suite, "ok": True}) + "\n"
        vec_path = trousse / "vectors" / rel
        _write_lf(vec_path, content)
        raw = vec_path.read_bytes()
        vec_files.append({
            "suite": suite,
            "relative_path": rel,
            "sha256": compute_lf_sha256_bytes(raw),
            "byte_length": len(raw),
        })
    _write_lf(
        trousse / "vectors" / "vectors-manifest.json",
        json.dumps({"schema_version": "1.0", "freeze_date": "2026-12-02", "file_count": len(vec_files), "files": vec_files}, indent=2) + "\n",
    )
    return trousse


def test_g0_uses_compendium_manifest_unit_mapping(
    tmp_path: Path,
    base_clean_venv: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    book = tmp_path / "ouvrage"
    (book / "specs").mkdir(parents=True)
    _write_lf(
        book / "specs" / "manifest.json",
        json.dumps({
            "synced_excerpts_catalog": [
                {"id": "G0-EX-CH01-02", "unit": "ch04", "source_path": "harness_proto/pipeline.py", "max_lines": 32, "is_full_file": False},
                {"id": "G0-EX-CH03-01", "unit": "ch20", "source_path": "policies_opa/rule_of_two.rego", "max_lines": 28, "is_full_file": False},
            ]
        }, indent=2) + "\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report, book_dir=book, verify_sync_manifest=True)
    assert rc == 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    assert report["synced_excerpts"]["G0-EX-CH01-02"]["unit"] == "ch04"
    assert report["synced_excerpts"]["G0-EX-CH03-01"]["unit"] == "ch20"


def test_g0_fails_on_synced_excerpt_over_40_lines(
    tmp_path: Path,
    base_clean_venv: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    body = "\n".join(f"x_{i} = {i}" for i in range(41))
    _write_lf(
        trousse / "harness_proto" / "pipeline.py",
        "# SPDX-License-Identifier: MIT\n"
        "# CA-G0-SYNC-BEGIN:G0-EX-CH01-02\n"
        f"{body}\n"
        "# CA-G0-SYNC-END:G0-EX-CH01-02\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    assert "G0-EX-CH01-02" not in report["synced_excerpts"]


def test_g0_fails_on_tampered_vector_and_missing_default_deny(
    tmp_path: Path,
    base_clean_venv: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert _REAL_OPA is not None
    monkeypatch.setenv("OPA_BIN", str(_REAL_OPA))
    trousse = _build_valid_trousse(tmp_path, base_clean_venv)
    _write_lf(trousse / "vectors" / "rfc8785" / "vec.json", '{"tampered": true}\n')
    _write_lf(
        trousse / "policies_opa" / "rule_of_two.rego",
        "# SPDX-License-Identifier: MIT\npackage agentique.rule_of_two\nimport rego.v1\nallow if { input.safe == true }\n",
    )
    out_report = tmp_path / "aq" / "rapports-g0.json"
    rc = execute_g0.run_g0(trousse, out_report)
    assert rc != 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    assert report["third_party_vectors"]["rfc8785"]["passed"] is False
    assert report["opa_check"]["missing_default_deny"] == ["policies_opa/rule_of_two.rego"]


def test_g0_runner_seals_14_excerpts_on_real_trousse(tmp_path: Path) -> None:
    out_report = tmp_path / "rapports-g0.json"
    rc = execute_g0.run_g0(_REAL_TROUSSE, out_report, book_dir=_COMPENDIUM_BOOK_DIR, verify_sync_manifest=True)
    assert rc == 0
    report = json.loads(out_report.read_text(encoding="utf-8"))
    assert report["pytest_check"]["passed"] == 83
    assert report["opa_check"]["coverage_pct"] == 100.0
    assert report["opa_check"]["tests_passed"] == 45
    assert len(report["synced_excerpts"]) == 14
    assert all(1 <= v["line_count"] <= 40 for v in report["synced_excerpts"].values())
    assert report["synced_excerpts"]["G0-EX-CH01-01"]["unit"] == "ch04"
    assert report["synced_excerpts"]["G0-EX-CH03-03"]["unit"] == "ch15"
    assert report["synced_excerpts"]["G0-EX-CH04-01"]["unit"] == "ch35"
    assert report["synced_excerpts"]["G0-EX-CH04-03"]["unit"] == "ch34"
