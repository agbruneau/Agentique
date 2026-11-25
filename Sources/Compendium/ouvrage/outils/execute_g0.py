#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Orchestre les 7 vérifications bloquantes de la barrière G0 sur Tome 8/trousse/ pour le Compendium."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform as py_platform
import re
import shutil
import subprocess
import sys
import tempfile

from jsonschema import Draft202012Validator, ValidationError

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from _communs import DEFAULT_FREEZE_DATE, compute_excerpt_sha256, compute_lf_sha256_bytes, normalize_lf_text  # noqa: E402
from verifie_specs import adapt_ssot_schemas_for_compendium, extract_ssot_schemas_from_arch  # noqa: E402

_SPDX_HEADER_RE = re.compile(r"^#\s*SPDX-License-Identifier:\s*MIT\s*$")
_DEFAULT_DENY_RE = re.compile(
    r'^\s*default\s+(?:allow\s*:?=\s*false|decision\s*:?=\s*"deny")\b',
    re.MULTILINE,
)
_SYNC_BEGIN_RE = re.compile(r"^\s*#\s*CA-G0-SYNC-BEGIN:([A-Za-z0-9_-]+)\s*$")
_SYNC_END_RE = re.compile(r"^\s*#\s*CA-G0-SYNC-END:([A-Za-z0-9_-]+)\s*$")
_CH_UNIT_RE = re.compile(r"-CH0([1-4])-", re.IGNORECASE)
_REQ_PIN_RE = re.compile(r"^([A-Za-z0-9][A-Za-z0-9._-]*(?:\[[A-Za-z0-9._,-]+\])?)==([^\s;\\]+)$")
_HASH_SHA256_RE = re.compile(r"--hash=sha256:([0-9a-fA-F]{64})\b")
_SPDX_TOKEN_RE = re.compile(r"\(|\)|\bAND\b|\bOR\b|\bWITH\b|[A-Za-z0-9.\-+]+")
_SHA256_HEX_RE = re.compile(r"^[0-9a-f]{64}$")

_DEFAULT_SPDX_ALLOWED = [
    "MIT",
    "Apache-2.0",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "ISC",
    "PSF-2.0",
    "MPL-2.0",
    "CC0-1.0",
]
_DEFAULT_SPDX_FORBIDDEN = ["GPL", "AGPL", "LGPL", "SSPL", "Proprietary"]
_REQUIRED_VECTOR_SUITES = ("rfc8785", "nist_acvp", "a2a_tck", "owasp_src055")
_EXCLUDED_TROUSSE_DIRS = {
    ".venv",
    ".tools",
    "vectors",
    "__pycache__",
    ".pytest_cache",
    ".git",
    "build",
    "dist",
}

_NARRATIVE_UNIT_IDS = frozenset({"00-liminaire", *(f"ch{i:02d}" for i in range(1, 37))})

_PACKAGE_PROBE_CODE = r"""
import importlib.metadata as md
import json

out = []
for dist in md.distributions():
    meta = dist.metadata
    name = (meta.get("Name") or getattr(dist, "name", "") or "unknown").strip()
    version = str(getattr(dist, "version", "") or meta.get("Version") or "")
    license_expr = (meta.get("License-Expression") or "").strip()
    license_field = (meta.get("License") or "").strip()
    classifiers = [c.strip() for c in meta.get_all("Classifier", []) if str(c).startswith("License ::")]
    bsd_texts = []
    if not license_expr and any("BSD License" in c for c in classifiers):
        from pathlib import Path as _P
        for rel in (dist.files or []):
            s = rel.as_posix()
            base = s.rsplit("/", 1)[-1].upper()
            if "LICENSES/" in s.upper() or base.startswith("LICENSE") or base.startswith("COPYING"):
                try:
                    txt = _P(dist.locate_file(rel)).read_text(encoding="utf-8")
                except Exception:
                    txt = None
                if txt:
                    bsd_texts.append(txt[:4000])
    out.append({
        "name": name,
        "version": version,
        "license_expr": license_expr,
        "license": license_field,
        "classifiers": classifiers,
        "bsd_texts": bsd_texts,
    })
print(json.dumps(out, ensure_ascii=False))
"""

_PYTEST_RUNNER_CODE = r"""
import json
import sys
import pytest


class _G0Collector:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.skipped = 0
        self.modules = {}

    def pytest_runtest_logreport(self, report) -> None:
        mod = report.nodeid.split("::")[0].replace("\\", "/")
        if report.when == "call":
            if report.passed:
                self.passed += 1
                self.modules[mod] = self.modules.get(mod, 0) + 1
            elif report.failed:
                self.failed += 1
            elif report.skipped:
                self.skipped += 1
        elif report.when in ("setup", "teardown") and report.failed:
            self.failed += 1
        elif report.when == "setup" and report.skipped:
            self.skipped += 1


collector = _G0Collector()
code = int(pytest.main(["--tb=short", "-p", "no:cacheprovider"], plugins=[collector]))
payload = {
    "exit_code": code,
    "passed": collector.passed,
    "failed": collector.failed,
    "skipped": collector.skipped,
    "modules": collector.modules,
}
print("__G0_PYTEST_JSON__:" + json.dumps(payload, ensure_ascii=False), flush=True)
raise SystemExit(0)
"""


def _read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _is_excluded_path(path: Path, root: Path) -> bool:
    rel_parts = path.relative_to(root).parts[:-1]
    return any(part in _EXCLUDED_TROUSSE_DIRS or part.endswith(".egg-info") for part in rel_parts)


def _iter_trousse_code_files(trousse_dir: Path, include_tests: bool = True) -> list[Path]:
    files: list[Path] = []
    for ext in ("*.py", "*.rego"):
        for candidate in sorted(trousse_dir.rglob(ext)):
            if not candidate.is_file() or _is_excluded_path(candidate, trousse_dir):
                continue
            rel_parts = candidate.relative_to(trousse_dir).parts
            if not include_tests and ("tests" in rel_parts or candidate.name.endswith("_test.rego")):
                continue
            files.append(candidate)
    return sorted(set(files))


def _resolve_python_bin(trousse_dir: Path) -> tuple[Path, str, list[str]]:
    errors: list[str] = []
    candidates = (
        [trousse_dir / ".venv" / "Scripts" / "python.exe", trousse_dir / ".venv" / "bin" / "python"]
        if os.name == "nt"
        else [trousse_dir / ".venv" / "bin" / "python", trousse_dir / ".venv" / "Scripts" / "python.exe"]
    )
    py_bin = next((c for c in candidates if c.is_file()), Path(sys.executable))

    proc = subprocess.run(
        [
            str(py_bin),
            "-B",
            "-c",
            "import sys, platform; print(platform.python_version()); raise SystemExit(0 if sys.version_info >= (3, 12) else 2)",
        ],
        capture_output=True,
        text=True,
        shell=False,
        timeout=30,
    )
    py_ver = (proc.stdout or "").strip().splitlines()[-1] if (proc.stdout or "").strip() else "unknown"
    if proc.returncode != 0:
        errors.append(f"[G0-PLATFORM] Python >= 3.12 requis pour {py_bin} (detecte: {py_ver}, rc={proc.returncode})")
    return py_bin, py_ver, errors


def _load_tools_lock_expected(trousse_dir: Path) -> tuple[str | None, str | None, Path | None, list[str]]:
    lock_path = trousse_dir / "tools-lock.json"
    if not lock_path.is_file():
        return None, None, None, []
    try:
        lock_data = _read_json(lock_path)
    except (OSError, json.JSONDecodeError) as exc:
        return None, None, None, [f"[G0-OPA] tools-lock.json invalide : {exc}"]
    if not isinstance(lock_data, dict):
        return None, None, None, ["[G0-OPA] tools-lock.json doit contenir un objet JSON"]

    plat_key = "windows_amd64" if os.name == "nt" else "linux_amd64"
    plat_block = (lock_data.get("platforms") or {}).get(plat_key)
    expected_sha = None
    expected_ver = lock_data.get("version")
    rel_path = None
    if isinstance(plat_block, dict):
        expected_sha = plat_block.get("sha256")
        expected_ver = plat_block.get("version") or expected_ver
        rel_path = plat_block.get("relative_path")
    if not expected_sha:
        expected_sha = lock_data.get("sha256")
    if not rel_path:
        rel_path = lock_data.get("relative_path")

    pinned_path = (trousse_dir / rel_path) if isinstance(rel_path, str) and rel_path else None
    return (
        str(expected_sha).lower() if expected_sha else None,
        str(expected_ver) if expected_ver else None,
        pinned_path,
        [],
    )


def _resolve_opa_bin(trousse_dir: Path) -> tuple[Path | None, str, str, list[str]]:
    expected_sha, expected_ver, lock_rel_path, errors = _load_tools_lock_expected(trousse_dir)
    if errors:
        return None, "invalid-lock", "0" * 64, errors

    default_local = trousse_dir / ".tools" / ("opa.exe" if os.name == "nt" else "opa")
    local_candidates = [p for p in (lock_rel_path, default_local) if p is not None]
    local_opa = next((p for p in local_candidates if p.is_file()), None)

    opa_env = os.environ.get("OPA_BIN", "").strip()
    from_local_tools = False
    if opa_env:
        opa_bin = Path(opa_env)
        if not opa_bin.is_file():
            return None, "missing", "0" * 64, [f"[G0-OPA] OPA_BIN introuvable : {opa_bin}"]
        if local_opa is not None and opa_bin.resolve() == local_opa.resolve():
            from_local_tools = True
    elif local_opa is not None:
        opa_bin = local_opa
        from_local_tools = True
    else:
        which_opa = shutil.which("opa")
        if not which_opa:
            return None, "missing", "0" * 64, ["[G0-OPA] Binaire opa introuvable (OPA_BIN, .tools/opa, PATH)"]
        opa_bin = Path(which_opa)

    actual_sha = hashlib.sha256(opa_bin.read_bytes()).hexdigest()
    if from_local_tools:
        if not expected_sha or not _SHA256_HEX_RE.fullmatch(expected_sha):
            return opa_bin, "unverified", actual_sha, ["[G0-OPA] tools-lock.json manquant ou sans SHA-256 valide pour .tools/opa"]
        if actual_sha != expected_sha:
            return (
                opa_bin,
                "hash-mismatch",
                actual_sha,
                [f"[G0-OPA] SHA-256 divergent pour {opa_bin} : attendu {expected_sha}, calcule {actual_sha}"],
            )

    try:
        proc = subprocess.run([str(opa_bin), "version"], capture_output=True, text=True, shell=False, timeout=20)
    except OSError as exc:
        return opa_bin, "exec-error", actual_sha, [f"[G0-OPA] Execution impossible pour {opa_bin} : {exc}"]

    if proc.returncode != 0:
        return opa_bin, "error", actual_sha, [f"[G0-OPA] 'opa version' a echoue (rc={proc.returncode}) : {proc.stderr.strip()}"]

    opa_version = "unknown"
    for line in (proc.stdout or "").splitlines():
        if line.lower().startswith("version:"):
            opa_version = line.split(":", 1)[1].strip()
            break
    if opa_version == "unknown" and (proc.stdout or "").strip():
        opa_version = proc.stdout.strip().splitlines()[0].strip()

    if from_local_tools and expected_ver and opa_version != expected_ver:
        errors.append(f"[G0-OPA] Version opa divergente : attendu {expected_ver}, detecte {opa_version}")

    return opa_bin, opa_version, actual_sha, errors


def _check_lockfile(trousse_dir: Path) -> tuple[dict, list[str]]:
    req_path = trousse_dir / "requirements.lock"
    errors: list[str] = []
    if not req_path.is_file():
        errors.append(f"[G0-LOCK] Fichier manquant : {req_path}")
        return {"path": "requirements.lock", "sha256": "0" * 64, "all_hashes_pinned": False, "passed": False}, errors

    raw_bytes = req_path.read_bytes()
    sha256 = compute_lf_sha256_bytes(raw_bytes)
    try:
        text = normalize_lf_text(raw_bytes.decode("utf-8"))
    except UnicodeDecodeError as exc:
        errors.append(f"[G0-LOCK] Encodage UTF-8 invalide dans requirements.lock : {exc}")
        return {"path": "requirements.lock", "sha256": sha256, "all_hashes_pinned": False, "passed": False}, errors

    logical_lines: list[str] = []
    buf = ""
    for line in text.split("\n"):
        stripped = line.strip()
        if not buf and (not stripped or stripped.startswith("#")):
            continue
        if stripped.endswith("\\"):
            buf += " " + stripped[:-1].strip()
            continue
        buf += " " + stripped
        logical_lines.append(buf.strip())
        buf = ""
    if buf.strip():
        logical_lines.append(buf.strip())

    pinned_count = 0
    for idx, entry in enumerate(logical_lines, start=1):
        if entry.startswith(("-r ", "--", "#")):
            continue
        if re.match(r"^(?:-e\s|\S+\s*@\s*\S+)", entry):
            errors.append(f"[G0-LOCK] Reference directe/VCS interdite dans requirements.lock (#{idx}) : {entry[:80]}")
            continue
        spec_part = re.split(r"\s+--|\s*;", entry, maxsplit=1)[0].strip()
        if not _REQ_PIN_RE.fullmatch(spec_part):
            errors.append(f"[G0-LOCK] Version non epinglee par '==' dans requirements.lock (#{idx}) : {spec_part}")
            continue
        hashes = _HASH_SHA256_RE.findall(entry)
        if not hashes:
            errors.append(f"[G0-LOCK] Empreinte --hash=sha256:... manquante pour {spec_part}")
            continue
        pinned_count += 1

    if pinned_count == 0 and not errors:
        errors.append("[G0-LOCK] Aucun paquet epingle dans requirements.lock")

    ok = len(errors) == 0 and pinned_count >= 1
    return {"path": "requirements.lock", "sha256": sha256, "all_hashes_pinned": ok, "passed": ok}, errors


def _eval_spdx_expression(expr: str, allowed_set: set[str], forbidden: list[str]) -> bool:
    raw_upper = expr.upper()
    if any(sub.upper() in raw_upper for sub in forbidden):
        return False
    tokens = _SPDX_TOKEN_RE.findall(expr)
    if not tokens:
        return False

    pos = 0

    def parse_or() -> bool:
        nonlocal pos
        val = parse_and()
        while pos < len(tokens) and tokens[pos] == "OR":
            pos += 1
            rhs = parse_and()
            val = val or rhs
        return val

    def parse_and() -> bool:
        nonlocal pos
        val = parse_atom()
        while pos < len(tokens) and tokens[pos] == "AND":
            pos += 1
            rhs = parse_atom()
            val = val and rhs
        return val

    def parse_atom() -> bool:
        nonlocal pos
        if pos >= len(tokens):
            return False
        tok = tokens[pos]
        if tok == "(":
            pos += 1
            val = parse_or()
            if pos < len(tokens) and tokens[pos] == ")":
                pos += 1
            return val
        pos += 1
        if pos < len(tokens) and tokens[pos] == "WITH":
            pos += 2
        return tok in allowed_set

    try:
        res = parse_or()
    except Exception:
        return False
    return res and pos == len(tokens)


def _classify_package_license(pkg: dict, allowed: list[str], forbidden: list[str]) -> tuple[bool, str]:
    allowed_set = set(allowed)
    name = f"{pkg.get('name', '?')}=={pkg.get('version', '?')}"
    expr = str(pkg.get("license_expr") or "").strip()
    lic = str(pkg.get("license") or "").strip()
    classifiers = [str(c) for c in pkg.get("classifiers") or []]
    combined_meta = " | ".join([expr, lic, *classifiers]).upper()

    for bad in sorted(forbidden, key=lambda item: (-len(item), item)):
        if bad.upper() in combined_meta:
            return False, f"Licence interdite ({bad}) detectee pour {name}"

    if expr and expr.upper() != "NONE":
        if _eval_spdx_expression(expr, allowed_set, forbidden):
            return True, ""
        return False, f"License-Expression non autorisee pour {name} : {expr!r}"

    direct_map = {
        "MIT": "MIT",
        "MIT LICENSE": "MIT",
        "APACHE 2.0": "Apache-2.0",
        "APACHE-2.0": "Apache-2.0",
        "APACHE SOFTWARE LICENSE": "Apache-2.0",
        "BSD-3-CLAUSE": "BSD-3-Clause",
        "BSD-2-CLAUSE": "BSD-2-Clause",
        "ISC": "ISC",
        "PSF-2.0": "PSF-2.0",
        "MPL-2.0": "MPL-2.0",
        "CC0-1.0": "CC0-1.0",
    }
    if lic.upper() in direct_map and direct_map[lic.upper()] in allowed_set:
        return True, ""

    classifier_map = {
        "License :: OSI Approved :: MIT License": "MIT",
        "License :: OSI Approved :: Apache Software License": "Apache-2.0",
        "License :: OSI Approved :: ISC License (ISCL)": "ISC",
        "License :: OSI Approved :: Python Software Foundation License": "PSF-2.0",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)": "MPL-2.0",
    }
    for clf in classifiers:
        mapped = classifier_map.get(clf)
        if mapped and mapped in allowed_set:
            return True, ""

    if any("License :: OSI Approved :: BSD License" == clf for clf in classifiers):
        for txt in pkg.get("bsd_texts") or []:
            up = txt.upper()
            if any(bad.upper() in up for bad in forbidden):
                return False, f"Texte de licence interdit dans {name}"
            if "ALL ADVERTISING MATERIALS MENTIONING FEATURES" in up:
                return False, f"BSD 4-clause non autorisee dans {name}"
            if "REDISTRIBUTION AND USE" in up and "NEITHER THE NAME" in up and "BSD-3-Clause" in allowed_set:
                return True, ""
            if "REDISTRIBUTION AND USE" in up and "BSD-2-Clause" in allowed_set:
                return True, ""

    return False, f"Licence non verifiee/non autorisee pour {name} (License={lic!r}, Classifiers={classifiers!r})"


def _check_spdx(
    trousse_dir: Path,
    book_dir: Path | None,
    py_bin: Path,
    env: dict[str, str],
) -> tuple[dict, list[str]]:
    violations: list[str] = []
    allow_path = trousse_dir / "spdx-allowlist.json"
    allowed = list(_DEFAULT_SPDX_ALLOWED)
    forbidden = list(_DEFAULT_SPDX_FORBIDDEN)
    if allow_path.is_file():
        try:
            allow_data = _read_json(allow_path)
            if isinstance(allow_data, dict):
                allowed = [str(x) for x in allow_data.get("allowed", allowed)]
                forbidden = [str(x) for x in allow_data.get("forbidden_substrings", forbidden)]
        except (OSError, json.JSONDecodeError) as exc:
            violations.append(f"[G0-SPDX] spdx-allowlist.json invalide : {exc}")
    else:
        violations.append(f"[G0-SPDX] spdx-allowlist.json manquant : {allow_path}")

    code_files = _iter_trousse_code_files(trousse_dir, include_tests=True)
    if book_dir is not None and (book_dir / "outils").is_dir():
        for py_file in sorted((book_dir / "outils").rglob("*.py")):
            if py_file.is_file() and "__pycache__" not in py_file.parts and ".pytest_cache" not in py_file.parts:
                code_files.append(py_file)

    for src in code_files:
        try:
            head_lines = src.read_text(encoding="utf-8").splitlines()[:10]
        except (OSError, UnicodeDecodeError) as exc:
            violations.append(f"[G0-SPDX] Lecture impossible {src} : {exc}")
            continue
        if not any(_SPDX_HEADER_RE.match(ln.strip()) for ln in head_lines):
            violations.append(f"[G0-SPDX] En-tete '# SPDX-License-Identifier: MIT' manquant : {src}")

    if not code_files:
        violations.append("[G0-SPDX] Aucun fichier .py ou .rego trouve pour verification SPDX")

    checked_packages = 0
    proc = subprocess.run(
        [str(py_bin), "-B", "-c", _PACKAGE_PROBE_CODE],
        capture_output=True,
        text=True,
        shell=False,
        timeout=30,
        env=env,
    )
    if proc.returncode != 0:
        violations.append(f"[G0-SPDX] Inspection importlib.metadata echouee : {proc.stderr.strip()}")
    else:
        try:
            pkgs = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            violations.append(f"[G0-SPDX] Sortie JSON invalide de la sonde paquets : {exc}")
            pkgs = []
        checked_packages = len(pkgs)
        if checked_packages == 0:
            violations.append("[G0-SPDX] Aucun paquet Python inspecte dans l'environnement cible")
        for pkg in pkgs:
            ok_pkg, reason = _classify_package_license(pkg, allowed, forbidden)
            if not ok_pkg:
                violations.append(f"[G0-SPDX] {reason}")

    result = {
        "license_target": "MIT",
        "checked_files": len(code_files),
        "checked_packages": checked_packages,
        "violations": violations,
        "passed": len(violations) == 0,
    }
    return result, list(violations)


def _walk_schema_strict(node: object, pointer: str, violations: list[str]) -> None:
    if isinstance(node, list):
        for idx, item in enumerate(node):
            _walk_schema_strict(item, f"{pointer}[{idx}]", violations)
        return
    if not isinstance(node, dict):
        return

    ref_val = node.get("$ref")
    if isinstance(ref_val, str) and re.match(r"^https?://", ref_val.strip(), re.IGNORECASE):
        violations.append(f"{pointer}: $ref reseau HTTP/HTTPS interdit ({ref_val})")

    if node.get("additionalProperties") is True:
        violations.append(f"{pointer}: additionalProperties=true interdit")

    is_object = node.get("type") == "object" or (
        isinstance(node.get("type"), list) and "object" in node["type"]
    )
    if is_object and "additionalProperties" not in node and "unevaluatedProperties" not in node:
        violations.append(f"{pointer}: objet sans additionalProperties=false")

    props = node.get("properties")
    if isinstance(props, dict):
        if node.get("additionalProperties") is not False:
            violations.append(f"{pointer}: objet avec 'properties' sans additionalProperties=false")
        req = node.get("required")
        req_set = set(req) if isinstance(req, list) else set()
        missing_req = sorted(k for k in props.keys() if k not in req_set)
        if missing_req:
            violations.append(f"{pointer}: proprietes absentes de required : {missing_req}")
        for prop_name, sub_schema in props.items():
            _walk_schema_strict(sub_schema, f"{pointer}.properties.{prop_name}", violations)

    for key, val in node.items():
        if key == "properties":
            continue
        if isinstance(val, (dict, list)):
            _walk_schema_strict(val, f"{pointer}.{key}", violations)


def _validate_inherited_registries(book_dir: Path, violations: list[str]) -> int:
    """Valide conditionnellement les registres herites s'ils existent sur disque."""
    checked = 0

    for fname, list_key, label in (
        ("ancres-chronologiques.json", "anchors", "ancres"),
        ("faits-empiriques.json", "facts", "faits"),
    ):
        fpath = book_dir / "registre" / fname
        if not fpath.is_file():
            continue
        checked += 1
        try:
            data = _read_json(fpath)
        except (OSError, json.JSONDecodeError) as exc:
            violations.append(f"[G0-SCHEMA] JSON invalide dans {fname} : {exc}")
            continue
        if not isinstance(data, dict):
            violations.append(f"[G0-SCHEMA] {fname} doit contenir un objet JSON")
            continue
        if data.get("freeze_date") != DEFAULT_FREEZE_DATE:
            violations.append(
                f"[G0-SCHEMA] freeze_date invalide dans {fname} : {data.get('freeze_date')!r} (attendu {DEFAULT_FREEZE_DATE!r})"
            )
        entries = data.get(list_key)
        if not isinstance(entries, list) or not entries:
            violations.append(f"[G0-SCHEMA] {fname} doit contenir une liste '{list_key}' non vide")
            continue
        for idx, entry in enumerate(entries):
            if not isinstance(entry, dict) or entry.get("statut_preuve") != "l_plus":
                eid = entry.get("id", entry.get("key", f"#{idx}")) if isinstance(entry, dict) else f"#{idx}"
                violations.append(f"[G0-SCHEMA] Entree '{eid}' ({label}) sans statut_preuve='l_plus' dans {fname}")

    gloss_path = book_dir / "registre" / "glossaire-termes.json"
    if gloss_path.is_file():
        checked += 1
        try:
            gloss = _read_json(gloss_path)
        except (OSError, json.JSONDecodeError) as exc:
            violations.append(f"[G0-SCHEMA] JSON invalide dans glossaire-termes.json : {exc}")
            gloss = None
        if gloss is not None and not isinstance(gloss, dict):
            violations.append("[G0-SCHEMA] glossaire-termes.json doit contenir un objet JSON")
        elif isinstance(gloss, dict):
            if gloss.get("freeze_date") != DEFAULT_FREEZE_DATE:
                violations.append(
                    f"[G0-SCHEMA] freeze_date invalide dans glossaire-termes.json : {gloss.get('freeze_date')!r}"
                )
            terms = gloss.get("terms")
            if not isinstance(terms, list) or len(terms) < 12:
                violations.append(
                    f"[G0-SCHEMA] glossaire-termes.json doit contenir >= 12 termes valides (trouve {len(terms) if isinstance(terms, list) else 0})"
                )
            else:
                seen_fr: set[str] = set()
                for idx, term in enumerate(terms):
                    if not isinstance(term, dict):
                        violations.append(f"[G0-SCHEMA] Terme #{idx} non-objet dans glossaire-termes.json")
                        continue
                    fr_val = str(term.get("fr", "")).strip()
                    en_val = str(term.get("en", "")).strip()
                    def_val = str(term.get("definition", "")).strip()
                    owner = term.get("chapitre_proprietaire")
                    if not fr_val or not en_val or not def_val:
                        violations.append(f"[G0-SCHEMA] Terme #{idx} incomplet dans glossaire-termes.json")
                    if owner not in _NARRATIVE_UNIT_IDS:
                        violations.append(
                            f"[G0-SCHEMA] Terme '{fr_val or idx}' avec chapitre_proprietaire invalide : {owner!r}"
                        )
                    low_fr = fr_val.lower()
                    if low_fr and low_fr in seen_fr:
                        violations.append(f"[G0-SCHEMA] Terme duplique dans glossaire-termes.json : {fr_val}")
                    if low_fr:
                        seen_fr.add(low_fr)

    statut_f_path = book_dir / "recherche" / "registre-statut-f.json"
    if statut_f_path.is_file():
        checked += 1
        try:
            sf = _read_json(statut_f_path)
        except (OSError, json.JSONDecodeError) as exc:
            violations.append(f"[G0-SCHEMA] JSON invalide dans registre-statut-f.json : {exc}")
            sf = None
        if sf is not None and not isinstance(sf, dict):
            violations.append("[G0-SCHEMA] registre-statut-f.json doit contenir un objet JSON")
        elif isinstance(sf, dict):
            if sf.get("freeze_date") != DEFAULT_FREEZE_DATE:
                violations.append(
                    f"[G0-SCHEMA] freeze_date invalide dans registre-statut-f.json : {sf.get('freeze_date')!r}"
                )
            entries_f = sf.get("blocked", sf.get("sources"))
            if not isinstance(entries_f, list):
                violations.append("[G0-SCHEMA] registre-statut-f.json doit contenir une liste 'blocked' ou 'sources'")
            else:
                for idx, item in enumerate(entries_f):
                    if not isinstance(item, dict):
                        violations.append(f"[G0-SCHEMA] Entree statut F #{idx} non-objet")
                        continue
                    if item.get("status") != "F":
                        violations.append(
                            f"[G0-SCHEMA] Entree statut F #{idx} ({item.get('url')}) avec status={item.get('status')!r} != 'F'"
                        )
                    if item.get("included_in_evidence") is not False:
                        violations.append(
                            f"[G0-SCHEMA] Entree statut F #{idx} ({item.get('url')}) avec included_in_evidence={item.get('included_in_evidence')!r}"
                        )

    return checked


def _resolve_arch_spec_path(trousse_dir: Path, book_dir: Path | None) -> Path | None:
    candidates: list[Path] = []
    if book_dir is not None:
        candidates.append(book_dir / "specs" / "architecture-trousse-g0.md")
    candidates.append(trousse_dir.parent / "specs" / "architecture-trousse-g0.md")
    repo_arch = _TOOLS_DIR.parents[3] / "Sources" / "Tomes" / "Tome 8 - Ingénierie exécutable et homologation vérifiable" / "specs" / "architecture-trousse-g0.md"
    candidates.append(repo_arch)
    return next((c for c in candidates if c.is_file()), None)


def _check_schemas(trousse_dir: Path, book_dir: Path | None) -> tuple[dict, dict[str, dict], list[str]]:
    violations: list[str] = []
    schemas_dir = trousse_dir / "schemas"
    schema_files = sorted(schemas_dir.glob("*.schema.json")) if schemas_dir.is_dir() else []
    if not schema_files:
        violations.append(f"[G0-SCHEMA] Aucun fichier *.schema.json dans {schemas_dir}")

    for sf in schema_files:
        label = sf.name
        try:
            schema = _read_json(sf)
        except (OSError, json.JSONDecodeError) as exc:
            violations.append(f"[G0-SCHEMA] JSON invalide dans {label} : {exc}")
            continue
        if not isinstance(schema, dict):
            violations.append(f"[G0-SCHEMA] {label} doit contenir un objet JSON")
            continue
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            violations.append(f"[G0-SCHEMA] $schema Draft 2020-12 attendu dans {label} : {schema.get('$schema')!r}")
        if schema.get("x-license") != "MIT":
            violations.append(f"[G0-SCHEMA] x-license='MIT' manquant dans {label}")
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:
            violations.append(f"[G0-SCHEMA] Meta-schema Draft 2020-12 invalide dans {label} : {exc}")
            continue
        for banned_root in ("allOf", "if", "then", "else"):
            if banned_root in schema:
                violations.append(f"[G0-SCHEMA] Mot-cle racine '{banned_root}' interdit dans {label}")
        _walk_schema_strict(schema, label, violations)

    schemas_checked = len(schema_files)
    ssot_schemas: dict[str, dict] = {}

    if book_dir is not None:
        arch_path = _resolve_arch_spec_path(trousse_dir, book_dir)
        has_any_book_data = (
            (book_dir / "registre").is_dir()
            or (book_dir / "recherche" / "registre-statut-f.json").is_file()
        )
        if arch_path is not None:
            raw_schemas, extract_errs = extract_ssot_schemas_from_arch(arch_path.read_text(encoding="utf-8"))
            ssot_schemas = adapt_ssot_schemas_for_compendium(raw_schemas)
            violations.extend(f"[G0-SCHEMA] {err}" for err in extract_errs)
            if "RapportsG0Output" not in ssot_schemas:
                violations.append("[G0-SCHEMA] Schema SSOT 'RapportsG0Output' introuvable dans architecture-trousse-g0.md")
        elif has_any_book_data:
            violations.append("[G0-SCHEMA] Spec SSOT architecture-trousse-g0.md manquante pour valider registre/ et recherche/")

        if (book_dir / "registre").is_dir():
            mapping = (
                ("specifications-lplus.json", "SpecificationsLPlusRegistry"),
                ("matrice-exig-prr-c40.json", "MatriceExigPrrC40Registry"),
                ("concordance-taxonomies.json", "ConcordanceTaxonomiesRegistry"),
            )
            for reg_file, schema_name in mapping:
                reg_path = book_dir / "registre" / reg_file
                if not reg_path.is_file() or schema_name not in ssot_schemas:
                    continue
                schemas_checked += 1
                try:
                    reg_data = _read_json(reg_path)
                    Draft202012Validator(ssot_schemas[schema_name]).validate(reg_data)
                except (OSError, json.JSONDecodeError, ValidationError) as exc:
                    violations.append(f"[G0-SCHEMA] Registre {reg_file} non conforme a {schema_name} : {exc}")

        schemas_checked += _validate_inherited_registries(book_dir, violations)

    return {
        "schemas_checked": schemas_checked,
        "strict_violations": violations,
        "passed": len(violations) == 0 and len(schema_files) >= 1,
    }, ssot_schemas, list(violations)


def _minimal_parent_dirs(files: list[Path]) -> list[Path]:
    dirs = sorted({f.parent.resolve() for f in files}, key=lambda p: len(p.parts))
    roots: list[Path] = []
    for d in dirs:
        if not any(d == r or d.is_relative_to(r) for r in roots):
            roots.append(d)
    return roots


def _strip_rego_comments(text: str) -> str:
    return "\n".join(ln for ln in text.splitlines() if not ln.lstrip().startswith("#"))


def _has_header_default_deny(text: str) -> bool:
    """Exige default allow := false (ou default decision := 'deny') apres package/import, avant toute regle."""
    seen_package = False
    for raw_line in _strip_rego_comments(text).splitlines():
        stripped = raw_line.strip()
        if not stripped:
            continue
        if re.match(r"^package\b", stripped):
            seen_package = True
            continue
        if re.match(r"^import\b", stripped):
            continue
        if _DEFAULT_DENY_RE.match(stripped):
            return seen_package
        if re.match(r"^default\b", stripped):
            continue
        return False
    return False


def _check_opa(trousse_dir: Path, opa_bin: Path | None, pre_errors: list[str]) -> tuple[dict, list[str]]:
    errors = list(pre_errors)
    rego_files = [p for p in _iter_trousse_code_files(trousse_dir, include_tests=True) if p.suffix == ".rego"]
    policy_files = [p for p in rego_files if not p.name.endswith("_test.rego")]
    test_files = [p for p in rego_files if p.name.endswith("_test.rego")]

    missing_default_deny: list[str] = []
    for pf in policy_files:
        try:
            raw_rego = pf.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"[G0-OPA] Lecture impossible {pf} : {exc}")
            continue
        if not _has_header_default_deny(raw_rego):
            missing_default_deny.append(pf.relative_to(trousse_dir).as_posix())

    if missing_default_deny:
        errors.append(f"[G0-OPA] default allow := false manquant dans : {missing_default_deny}")
    if not policy_files:
        errors.append("[G0-OPA] Aucun fichier politique .rego trouve")
    if not test_files:
        errors.append("[G0-OPA] Aucun fichier *_test.rego trouve")

    coverage_pct = 0.0
    tests_passed = 0
    tests_failed = 0

    if opa_bin is not None and not pre_errors and policy_files and test_files:
        target_args = [str(d) for d in _minimal_parent_dirs(rego_files)]
        res_tests = subprocess.run(
            [str(opa_bin), "test", *target_args, "--format=json"],
            capture_output=True,
            text=True,
            shell=False,
            timeout=60,
        )
        try:
            entries = json.loads(res_tests.stdout or "[]")
        except json.JSONDecodeError as exc:
            entries = []
            errors.append(f"[G0-OPA] Sortie JSON invalide de 'opa test --format=json' : {exc}")

        if isinstance(entries, list):
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                if entry.get("fail") or entry.get("skip"):
                    tests_failed += 1
                else:
                    tests_passed += 1
        if res_tests.returncode != 0:
            tests_failed = max(tests_failed, 1)
            errors.append(f"[G0-OPA] 'opa test' a retourne rc={res_tests.returncode}")
        if tests_passed == 0:
            errors.append("[G0-OPA] Aucun test OPA passe")
        if tests_failed > 0:
            errors.append(f"[G0-OPA] {tests_failed} test(s) OPA en echec ou ignores")

        res_cov = subprocess.run(
            [str(opa_bin), "test", *target_args, "--coverage", "--format=json"],
            capture_output=True,
            text=True,
            shell=False,
            timeout=60,
        )
        try:
            cov_data = json.loads(res_cov.stdout or "{}")
        except json.JSONDecodeError as exc:
            cov_data = {}
            errors.append(f"[G0-OPA] Sortie JSON invalide de 'opa test --coverage' : {exc}")

        if isinstance(cov_data, dict):
            coverage_pct = float(cov_data.get("coverage", 0.0))
            not_covered = int(cov_data.get("not_covered_lines", 0))
            if res_cov.returncode != 0 or coverage_pct != 100.0 or not_covered != 0:
                errors.append(
                    f"[G0-OPA] Couverture Rego insuffisante : {coverage_pct}% (non couverts={not_covered}, rc={res_cov.returncode})"
                )

    opa_obj = {
        "files_checked": len(policy_files),
        "missing_default_deny": missing_default_deny,
        "coverage_pct": round(coverage_pct, 4),
        "tests_passed": tests_passed,
        "tests_failed": tests_failed,
    }
    return opa_obj, errors


def _check_vectors(trousse_dir: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    suites: dict[str, dict] = {
        s: {"passed": True, "file_count": 0, "verified_count": 0, "violations": []}
        for s in _REQUIRED_VECTOR_SUITES
    }
    vectors_dir = trousse_dir / "vectors"
    manifest_path = vectors_dir / "vectors-manifest.json"
    if not manifest_path.is_file():
        msg = f"[G0-VECTORS] Manifeste manquant : {manifest_path}"
        for s in _REQUIRED_VECTOR_SUITES:
            suites[s]["passed"] = False
            suites[s]["violations"].append(msg)
        return suites, [msg]

    try:
        manifest = _read_json(manifest_path)
    except (OSError, json.JSONDecodeError) as exc:
        msg = f"[G0-VECTORS] JSON invalide dans vectors-manifest.json : {exc}"
        for s in _REQUIRED_VECTOR_SUITES:
            suites[s]["passed"] = False
            suites[s]["violations"].append(msg)
        return suites, [msg]

    files_list = manifest.get("files") if isinstance(manifest, dict) else None
    if not isinstance(files_list, list) or not files_list:
        msg = "[G0-VECTORS] Champ 'files' vide ou invalide dans vectors-manifest.json"
        for s in _REQUIRED_VECTOR_SUITES:
            suites[s]["passed"] = False
            suites[s]["violations"].append(msg)
        return suites, [msg]

    if "file_count" in manifest and int(manifest["file_count"]) != len(files_list):
        errors.append(f"[G0-VECTORS] file_count={manifest['file_count']} != len(files)={len(files_list)}")

    vectors_root = vectors_dir.resolve()
    for item in files_list:
        if not isinstance(item, dict):
            errors.append("[G0-VECTORS] Entree de vecteur non-objet")
            continue
        suite = str(item.get("suite", ""))
        rel = str(item.get("relative_path", ""))
        expected_sha = str(item.get("sha256", "")).lower()
        expected_len = item.get("byte_length")
        if suite not in suites:
            errors.append(f"[G0-VECTORS] Suite inconnue '{suite}' pour {rel}")
            continue

        entry = suites[suite]
        entry["file_count"] += 1
        target = (vectors_dir / rel).resolve()
        if not rel or not target.is_relative_to(vectors_root) or not target.is_file():
            entry["violations"].append(f"Fichier introuvable ou hors vectors/ : {rel}")
            continue

        raw = target.read_bytes()
        lf_bytes = raw.replace(b"\r\n", b"\n")
        actual_sha = hashlib.sha256(lf_bytes).hexdigest()
        len_ok = expected_len is None or len(raw) == int(expected_len) or len(lf_bytes) == int(expected_len)
        if actual_sha != expected_sha or not len_ok:
            entry["violations"].append(
                f"Integrite invalide pour {rel} (sha={actual_sha[:12]} vs {expected_sha[:12]}, len={len(lf_bytes)} vs {expected_len})"
            )
            continue
        entry["verified_count"] += 1

    for suite_name, entry in suites.items():
        if entry["file_count"] == 0:
            entry["violations"].append(f"Aucun vecteur recense pour la suite {suite_name}")
        if entry["violations"] or entry["verified_count"] != entry["file_count"]:
            entry["passed"] = False
            errors.extend(f"[G0-VECTORS:{suite_name}] {v}" for v in entry["violations"])

    return suites, errors


def _check_pytest(trousse_dir: Path, py_bin: Path, env: dict[str, str]) -> tuple[dict, list[str]]:
    errors: list[str] = []
    if not (trousse_dir / "tests").is_dir():
        errors.append(f"[G0-PYTEST] Repertoire tests/ manquant dans {trousse_dir}")
        return {"passed": 0, "failed": 1, "skipped": 0, "modules": {}}, errors

    sub_env = dict(env)
    existing_pp = sub_env.get("PYTHONPATH", "")
    sub_env["PYTHONPATH"] = f"{trousse_dir}{os.pathsep}{existing_pp}" if existing_pp else str(trousse_dir)
    sub_env["PYTHONDONTWRITEBYTECODE"] = "1"

    proc = subprocess.run(
        [str(py_bin), "-B", "-c", _PYTEST_RUNNER_CODE],
        cwd=str(trousse_dir),
        capture_output=True,
        text=True,
        shell=False,
        timeout=120,
        env=sub_env,
    )
    payload: dict | None = None
    for line in reversed((proc.stdout or "").splitlines()):
        if line.startswith("__G0_PYTEST_JSON__:"):
            try:
                payload = json.loads(line.split(":", 1)[1])
            except json.JSONDecodeError:
                payload = None
            break

    if payload is None:
        errors.append(f"[G0-PYTEST] Echec d'execution pytest (rc={proc.returncode}) : {(proc.stderr or proc.stdout).strip()[-400:]}")
        return {"passed": 0, "failed": 1, "skipped": 0, "modules": {}}, errors

    p_exit = int(payload.get("exit_code", 1))
    passed = int(payload.get("passed", 0))
    failed = int(payload.get("failed", 0))
    skipped = int(payload.get("skipped", 0))
    modules = {str(k): int(v) for k, v in (payload.get("modules") or {}).items()}

    if p_exit != 0:
        errors.append(f"[G0-PYTEST] pytest a retourne le code {p_exit}")
    if passed < 1:
        errors.append("[G0-PYTEST] Aucun test pytest reussi")
    if failed > 0:
        errors.append(f"[G0-PYTEST] {failed} test(s) pytest en echec")
    if skipped > 0:
        errors.append(f"[G0-PYTEST] {skipped} test(s) pytest ignores (skip interdit a G0)")

    return {"passed": passed, "failed": failed, "skipped": skipped, "modules": modules}, errors


def _scan_marker_blocks(trousse_dir: Path) -> tuple[dict[str, dict], list[str]]:
    blocks: dict[str, dict] = {}
    errors: list[str] = []
    for src in _iter_trousse_code_files(trousse_dir, include_tests=False):
        rel = src.relative_to(trousse_dir).as_posix()
        try:
            raw_text = normalize_lf_text(src.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"[G0-SYNC] Lecture impossible {rel} : {exc}")
            continue
        lines = raw_text.split("\n")
        if lines and lines[-1] == "":
            lines = lines[:-1]

        open_id: str | None = None
        open_idx = -1
        for idx, line in enumerate(lines):
            m_begin = _SYNC_BEGIN_RE.match(line)
            if m_begin:
                if open_id is not None:
                    errors.append(f"[G0-SYNC] Balise BEGIN imbriquee ({m_begin.group(1)}) dans {rel}:{idx + 1}")
                open_id = m_begin.group(1)
                open_idx = idx
                continue
            m_end = _SYNC_END_RE.match(line)
            if m_end:
                end_id = m_end.group(1)
                if open_id is None:
                    errors.append(f"[G0-SYNC] Balise END orpheline ({end_id}) dans {rel}:{idx + 1}")
                elif end_id != open_id:
                    errors.append(f"[G0-SYNC] Balise END '{end_id}' != BEGIN '{open_id}' dans {rel}:{idx + 1}")
                elif open_id in blocks:
                    errors.append(f"[G0-SYNC] Identifiant d'extrait duplique : {open_id}")
                else:
                    slice_lines = lines[open_idx + 1 : idx]
                    blocks[open_id] = {
                        "source_path": rel,
                        "start_ln": open_idx + 2,
                        "end_ln": idx,
                        "lines": slice_lines,
                    }
                open_id = None
                open_idx = -1
        if open_id is not None:
            errors.append(f"[G0-SYNC] Balise BEGIN non fermee ({open_id}) dans {rel}")
    return blocks, errors


def _infer_unit_from_anchor(anchor_id: str) -> str:
    match = _CH_UNIT_RE.search(anchor_id)
    return f"ch0{match.group(1)}" if match else "ch01"


def _check_synced_excerpts(
    trousse_dir: Path,
    book_dir: Path | None,
    verify_sync_manifest: bool,
) -> tuple[dict[str, dict], list[str]]:
    blocks, errors = _scan_marker_blocks(trousse_dir)
    synced: dict[str, dict] = {}
    manifest_path = (book_dir / "specs" / "manifest.json") if book_dir is not None else None
    trousse_owner_label = "Tome 8 - Ingénierie exécutable et homologation vérifiable"

    if manifest_path is not None and manifest_path.is_file():
        manifest = _read_json(manifest_path)
        catalog = manifest.get("synced_excerpts_catalog", []) if isinstance(manifest, dict) else []
        expected_ids: set[str] = set()
        for item in catalog:
            aid = str(item["id"])
            expected_ids.add(aid)
            unit = str(item["unit"])
            rel = str(item["source_path"])
            for pref in (
                f"Sources/Tomes/{trousse_owner_label}/trousse/",
                "Sources/Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/",
                f"Tomes/{trousse_owner_label}/trousse/",
                "Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/",
                f"Corpus/{trousse_owner_label}/trousse/",
                f"{trousse_owner_label}/trousse/",
                "8 - Manuel/trousse/",
                "trousse/",
            ):
                if rel.startswith(pref):
                    rel = rel[len(pref) :]
                    break
            max_lines = min(40, int(item.get("max_lines", 40)))
            is_full = bool(item.get("is_full_file", False))
            target = trousse_dir / rel
            if not target.is_file():
                errors.append(f"[G0-SYNC] Fichier source absent pour {aid} : {rel}")
                continue
            if is_full:
                norm_lines = normalize_lf_text(target.read_text(encoding="utf-8")).split("\n")
                if norm_lines and norm_lines[-1] == "":
                    norm_lines = norm_lines[:-1]
                start_ln, end_ln, slice_lines = 1, len(norm_lines), norm_lines
            else:
                blk = blocks.get(aid)
                if blk is None:
                    errors.append(f"[G0-SYNC] Marqueurs # CA-G0-SYNC-BEGIN/END:{aid} absents de {rel}")
                    continue
                if blk["source_path"] != rel:
                    errors.append(f"[G0-SYNC] Ancre {aid} trouvee dans {blk['source_path']} au lieu de {rel}")
                    continue
                start_ln, end_ln, slice_lines = blk["start_ln"], blk["end_ln"], blk["lines"]

            if not slice_lines or len(slice_lines) > max_lines:
                errors.append(
                    f"[G0-SYNC] Extrait {aid} invalide ({len(slice_lines)} lignes, max={max_lines})"
                )
                continue

            synced[aid] = {
                "unit": unit,
                "source_path": f"{trousse_owner_label}/trousse/{rel}",
                "lines": f"{start_ln}-{end_ln}",
                "line_count": len(slice_lines),
                "sha256": compute_excerpt_sha256(slice_lines),
            }

        extra_ids = sorted(set(blocks.keys()) - expected_ids)
        if extra_ids:
            errors.append(f"[G0-SYNC] Marqueurs non references dans manifest.json : {extra_ids}")
    else:
        if verify_sync_manifest:
            errors.append(f"[G0-SYNC] manifest.json introuvable pour --verify-sync-manifest : {manifest_path}")
        for aid, blk in sorted(blocks.items()):
            slice_lines = blk["lines"]
            if not slice_lines or len(slice_lines) > 40:
                errors.append(f"[G0-SYNC] Extrait {aid} hors bornes 1..40 lignes ({len(slice_lines)})")
                continue
            synced[aid] = {
                "unit": _infer_unit_from_anchor(aid),
                "source_path": f"{trousse_owner_label}/trousse/{blk['source_path']}",
                "lines": f"{blk['start_ln']}-{blk['end_ln']}",
                "line_count": len(slice_lines),
                "sha256": compute_excerpt_sha256(slice_lines),
            }

    return synced, errors


def _write_json_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.replace(tmp_path, path)
    except Exception:
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)
        raise


def run_g0(
    trousse_dir: Path,
    out_report: Path,
    book_dir: Path | None = None,
    *,
    verify_sync_manifest: bool = False,
) -> int:
    """Execute les 7 etapes bloquantes G0 sur trousse_dir et ecrit out_report atomiquement."""
    trousse_root = trousse_dir.resolve()
    book_root = book_dir.resolve() if book_dir is not None else None
    env = dict(os.environ)

    all_errors: list[str] = []
    if not trousse_root.is_dir():
        all_errors.append(f"[G0] Repertoire trousse introuvable : {trousse_root}")

    py_bin, py_ver, py_errs = _resolve_python_bin(trousse_root)
    all_errors.extend(py_errs)

    opa_bin, opa_ver, opa_sha, opa_res_errs = _resolve_opa_bin(trousse_root)

    lock_res, lock_errs = _check_lockfile(trousse_root)
    all_errors.extend(lock_errs)

    spdx_res, spdx_errs = _check_spdx(trousse_root, book_root, py_bin, env)
    all_errors.extend(spdx_errs)

    schema_res, ssot_schemas, schema_errs = _check_schemas(trousse_root, book_root)
    all_errors.extend(schema_errs)

    opa_res, opa_errs = _check_opa(trousse_root, opa_bin, opa_res_errs)
    all_errors.extend(opa_errs)

    vec_res, vec_errs = _check_vectors(trousse_root)
    all_errors.extend(vec_errs)

    pytest_res, pytest_errs = _check_pytest(trousse_root, py_bin, env)
    all_errors.extend(pytest_errs)

    synced_res, sync_errs = _check_synced_excerpts(trousse_root, book_root, verify_sync_manifest)
    all_errors.extend(sync_errs)

    passed = len(all_errors) == 0
    exit_code = 0 if passed else 1

    report = {
        "schema_version": "1.0.0",
        "executed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "freeze_date": DEFAULT_FREEZE_DATE,
        "platform": {
            "os": f"{py_platform.system().lower()}-{py_platform.machine().lower()}",
            "python_version": py_ver,
            "opa_version": opa_ver,
            "opa_sha256": opa_sha if _SHA256_HEX_RE.fullmatch(opa_sha) else "0" * 64,
        },
        "overall_status": "PASS" if passed else "FAIL",
        "exit_code": exit_code,
        "spdx_check": spdx_res,
        "lockfile_check": lock_res,
        "schema_validation": schema_res,
        "opa_check": opa_res,
        "pytest_check": pytest_res,
        "third_party_vectors": vec_res,
        "synced_excerpts": synced_res,
    }

    if "RapportsG0Output" in ssot_schemas:
        schema_res["schemas_checked"] += 1
        try:
            Draft202012Validator(ssot_schemas["RapportsG0Output"]).validate(report)
        except ValidationError as exc:
            msg = f"[G0-SCHEMA] Rapport de sortie non conforme a RapportsG0Output : {exc.message}"
            all_errors.append(msg)
            schema_res["strict_violations"].append(msg)
            schema_res["passed"] = False
            report["overall_status"] = "FAIL"
            report["exit_code"] = 1
            exit_code = 1

    _write_json_atomic(out_report, report)
    if all_errors:
        for err in all_errors:
            print(err, file=sys.stderr)
    return exit_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Exécute les 7 étapes bloquantes G0 sur Tome 8/trousse/ pour le Compendium.")
    default_book = Path(__file__).resolve().parent.parent
    default_trousse = default_book.parents[2] / "Sources" / "Tomes" / "Tome 8 - Ingénierie exécutable et homologation vérifiable" / "trousse"
    parser.add_argument("--book-dir", type=Path, default=default_book, help="Racine Sources/Compendium/ouvrage")
    parser.add_argument("--trousse-dir", type=Path, default=None, help="Répertoire trousse exécutable")
    parser.add_argument("--output", type=Path, default=None, help="Chemin du rapport JSON G0 (défaut : <book-dir>/aq/rapports-g0.json)")
    parser.add_argument("--verify-sync-manifest", action="store_true", help="Exige manifest.json et vérifie les 14 extraits CA-G0-SYNC")
    args = parser.parse_args(argv)
    book_dir = args.book_dir.resolve()
    if args.trousse_dir is not None:
        trousse_dir = args.trousse_dir.resolve()
    elif (book_dir / "trousse").is_dir():
        trousse_dir = (book_dir / "trousse").resolve()
    else:
        trousse_dir = default_trousse.resolve()
    out_report = (args.output if args.output is not None else book_dir / "aq" / "rapports-g0.json").resolve()
    return run_g0(trousse_dir, out_report, book_dir=book_dir, verify_sync_manifest=args.verify_sync_manifest)


if __name__ == "__main__":
    raise SystemExit(main())
