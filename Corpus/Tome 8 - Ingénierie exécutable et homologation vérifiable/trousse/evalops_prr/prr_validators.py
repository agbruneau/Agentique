# SPDX-License-Identifier: MIT
"""Validateurs mecaniques : 24 [BLOQUANT] PRR, 2027-B001, 5 SBB et C01-C40."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from jsonschema import Draft202012Validator
import yaml

BLOCKING_PRR_IDS: tuple[str, ...] = (
    "S-01",
    "S-03",
    "S-06",
    "S-08",
    "S-09",
    "S-11",
    "S-14",
    "S-15",
    "R-01",
    "R-03",
    "R-06",
    "R-07",
    "R-14",
    "O-02",
    "O-09",
    "G-01",
    "G-03",
    "G-05",
    "G-06",
    "G-07",
    "G-10",
    "G-15",
    "F-04",
    "F-14",
)

REQUIRED_5_SBB_SLOTS: tuple[str, ...] = (
    "secrets_vault",
    "guardrails_engine",
    "signed_human_approval_service",
    "immutable_audit_ledger",
    "finops_budget_quota_controller",
)

REQUIRED_BLUEPRINT_IDS: tuple[str, ...] = (
    "bp1_assistant_interne",
    "bp2_rag_entreprise_acl",
    "bp3_orchestration_multi_agents_b2b",
)

_REQUIRED_C40: frozenset[str] = frozenset(
    f"C{idx:02d}" for idx in range(1, 41)
)


@dataclass(frozen=True, slots=True)
class PrrReport:
    """Rapport de verification des 24 portes bloquantes PRR."""

    passed: bool
    present_count: int
    missing_ids: tuple[str, ...]
    failed_ids: tuple[str, ...]
    errors: tuple[str, ...]


def validate_adr_2027_b001(
    adr_yaml_or_dict: str | dict[str, Any], schema: dict[str, Any]
) -> list[str]:
    """Valide une fiche ADR 2027-B001 YAML ou dict contre schema strict."""
    if isinstance(adr_yaml_or_dict, str):
        try:
            data = yaml.safe_load(adr_yaml_or_dict)
        except yaml.YAMLError as exc:
            return [f"YAML ADR invalide : {exc}"]
    else:
        data = adr_yaml_or_dict
    if not isinstance(data, dict):
        return ["ADR 2027-B001 doit etre un objet YAML/dict"]
    validator = Draft202012Validator(schema)
    return [
        err.message
        for err in sorted(
            validator.iter_errors(data),
            key=lambda e: tuple(str(p) for p in e.path),
        )
    ]


def validate_prr_24_blocking(
    evidence: dict[str, Any], schema: dict[str, Any]
) -> PrrReport:
    """Verifie presence, statut PASS et SHA-256 pour les 24 PRR bloquants."""
    schema_errs = [
        err.message
        for err in sorted(
            Draft202012Validator(schema).iter_errors(evidence),
            key=lambda e: tuple(str(p) for p in e.path),
        )
    ]
    gates_raw = (
        evidence.get("gates") if isinstance(evidence, dict) else None
    )
    seen: dict[str, dict[str, Any]] = {}
    if isinstance(gates_raw, list):
        for gate in gates_raw:
            if isinstance(gate, dict) and isinstance(gate.get("prr_id"), str):
                pid = gate["prr_id"]
                if pid in seen:
                    schema_errs.append(f"PRR duplique : {pid}")
                seen[pid] = gate
    missing = tuple(pid for pid in BLOCKING_PRR_IDS if pid not in seen)
    failed = tuple(
        pid
        for pid in BLOCKING_PRR_IDS
        if pid in seen and seen[pid].get("status") != "PASS"
    )
    present_count = len(BLOCKING_PRR_IDS) - len(missing)
    passed = not schema_errs and not missing and not failed
    return PrrReport(
        passed=passed,
        present_count=present_count,
        missing_ids=missing,
        failed_ids=failed,
        errors=tuple(schema_errs),
    )


def validate_blueprints_and_c40(blueprints: list[dict[str, Any]]) -> list[str]:
    """Verifie que les 3 blueprints renseignent les 5 SBB et C01-C40."""
    errs: list[str] = []
    if not isinstance(blueprints, list):
        return ["blueprints doit etre une liste"]
    by_id: dict[str, dict[str, Any]] = {}
    for bp in blueprints:
        if not isinstance(bp, dict) or not isinstance(
            bp.get("blueprint_id"), str
        ):
            errs.append(f"Blueprint invalide : {bp!r}")
            continue
        bp_id = bp["blueprint_id"]
        if bp_id in by_id:
            errs.append(f"Blueprint duplique : {bp_id}")
        by_id[bp_id] = bp
    for req_bp in REQUIRED_BLUEPRINT_IDS:
        if req_bp not in by_id:
            errs.append(f"Blueprint obligatoire absent : {req_bp}")
            continue
        bp = by_id[req_bp]
        sbb = bp.get("sbb_slots")
        if not isinstance(sbb, dict):
            errs.append(f"{req_bp}: sbb_slots manquant")
        else:
            for slot in REQUIRED_5_SBB_SLOTS:
                val = sbb.get(slot)
                if not isinstance(val, str) or not val.strip():
                    errs.append(f"{req_bp}: SBB manquant '{slot}'")
        cov = bp.get("criteria_covered")
        if not isinstance(cov, list):
            errs.append(f"{req_bp}: criteria_covered manquant")
        else:
            missing_c = sorted(_REQUIRED_C40 - {str(c) for c in cov})
            if missing_c:
                errs.append(f"{req_bp}: criteres manquants {missing_c}")
    return errs
