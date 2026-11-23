# SPDX-License-Identifier: MIT
"""Interface securisee OPA CLI (shell=False, default-deny, couverture)."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from typing import Any

_DEFAULT_DENY_RE = re.compile(
    r'^\s*default\s+(?:allow\s*:?=\s*false|decision\s*:?=\s*"deny")\b'
)


class OpaStaticCheckError(ValueError):
    """Erreur levee si un .rego omet default allow := false."""


@dataclass(frozen=True, slots=True)
class OpaCoverageReport:
    """Resultat structure de 'opa test --coverage --format=json'."""

    coverage_pct: float
    tests_passed: int
    tests_failed: int
    not_covered_lines: int
    passed: bool


def verify_rego_default_deny(rego_path: Path) -> None:
    """Impose default allow := false (ou decision := 'deny') en tete."""
    try:
        text = rego_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise OpaStaticCheckError(
            f"Lecture impossible {rego_path} : {exc}"
        ) from exc
    seen_package = False
    for raw_line in text.splitlines():
        code_line = raw_line.split("#", 1)[0].strip()
        if not code_line:
            continue
        if re.match(r"^package\b", code_line):
            seen_package = True
            continue
        if re.match(r"^import\b", code_line):
            continue
        if _DEFAULT_DENY_RE.match(code_line):
            if not seen_package:
                raise OpaStaticCheckError(
                    f"default deny avant package dans {rego_path}"
                )
            return
        if re.match(r"^default\b", code_line):
            continue
        raise OpaStaticCheckError(
            f"default allow := false absent avant regle dans {rego_path}"
        )
    raise OpaStaticCheckError(
        f"default allow := false manquant dans {rego_path}"
    )


def _resolve_opa_executable(policies_dir: Path, opa_bin: Path | None) -> Path:
    if opa_bin is not None:
        if opa_bin.is_file():
            return opa_bin
        raise FileNotFoundError(f"Binaire CLI 'opa' introuvable : {opa_bin}")
    env_bin = os.environ.get("OPA_BIN", "").strip()
    if env_bin:
        env_path = Path(env_bin)
        if env_path.is_file():
            return env_path
        raise FileNotFoundError(f"OPA_BIN introuvable : {env_path}")
    exe_name = "opa.exe" if os.name == "nt" else "opa"
    for candidate in (
        policies_dir.parent / ".tools" / exe_name,
        Path(__file__).resolve().parent.parent / ".tools" / exe_name,
    ):
        if candidate.is_file():
            return candidate
    found = shutil.which("opa")
    if found:
        return Path(found)
    raise FileNotFoundError("Binaire CLI 'opa' introuvable")


class OpaPolicyEngine:
    """Evaluateur deterministe hors modele adosse au binaire OPA CLI."""

    def __init__(
        self, policies_dir: Path, opa_bin: Path | None = None
    ) -> None:
        self.policies_dir = policies_dir
        self.opa_bin = _resolve_opa_executable(policies_dir, opa_bin)

    def _verify_all_policies(self) -> None:
        for rego in sorted(self.policies_dir.glob("*.rego")):
            if not rego.name.endswith("_test.rego"):
                verify_rego_default_deny(rego)

    def evaluate(self, query: str, input_data: dict[str, Any]) -> bool:
        """Execute opa eval --fail --format=json (echec ferme si indefini)."""
        try:
            self._verify_all_policies()
            payload = json.dumps(input_data, ensure_ascii=False)
            proc = subprocess.run(
                [
                    str(self.opa_bin),
                    "eval",
                    "-d",
                    str(self.policies_dir),
                    "-I",
                    "--fail",
                    "--format=json",
                    query,
                ],
                input=payload,
                capture_output=True,
                text=True,
                shell=False,
                timeout=30,
            )
            if proc.returncode != 0:
                return False
            parsed = json.loads(proc.stdout or "{}")
            val = parsed["result"][0]["expressions"][0]["value"]
            return val is True
        except Exception:
            return False

    def run_coverage(self) -> OpaCoverageReport:
        """Execute opa test --coverage --format=json (100 % exige)."""
        self._verify_all_policies()
        res_tests = subprocess.run(
            [
                str(self.opa_bin),
                "test",
                str(self.policies_dir),
                "--format=json",
            ],
            capture_output=True,
            text=True,
            shell=False,
            timeout=60,
        )
        entries = json.loads(res_tests.stdout or "[]")
        passed = 0
        failed = 0
        if isinstance(entries, list):
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                if entry.get("fail") or entry.get("skip"):
                    failed += 1
                else:
                    passed += 1
        if res_tests.returncode != 0 and failed == 0:
            failed = 1

        res_cov = subprocess.run(
            [
                str(self.opa_bin),
                "test",
                str(self.policies_dir),
                "--coverage",
                "--format=json",
            ],
            capture_output=True,
            text=True,
            shell=False,
            timeout=60,
        )
        cov = json.loads(res_cov.stdout or "{}")
        cov_pct = float(cov.get("coverage", 0.0))
        not_cov = int(cov.get("not_covered_lines", 0))
        ok = (
            res_tests.returncode == 0
            and res_cov.returncode == 0
            and failed == 0
            and passed > 0
            and cov_pct == 100.0
            and not_cov == 0
        )
        return OpaCoverageReport(
            coverage_pct=cov_pct,
            tests_passed=passed,
            tests_failed=failed,
            not_covered_lines=not_cov,
            passed=ok,
        )
