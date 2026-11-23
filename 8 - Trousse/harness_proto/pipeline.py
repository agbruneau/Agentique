# SPDX-License-Identifier: MIT
"""Harnais deterministe 80/20 a 8 etapes et porte AMBIGU_ESCALADE."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import json
from pathlib import Path
from typing import Any, Callable

from jsonschema import Draft202012Validator, SchemaError

from harness_proto.jcs import jcs_sha256_hex

_INPUT_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": False,
    "required": ["reference_dossier", "texte"],
    "properties": {
        "reference_dossier": {"type": "string", "minLength": 1},
        "texte": {"type": "string", "minLength": 1},
    },
}


class StepStatus(StrEnum):
    """Statuts terminaux ou intermediaires du harnais deterministe."""

    OK = "OK"
    AMBIGU_ESCALADE = "AMBIGU_ESCALADE"
    DONNEES_INSUFFISANTES = "DONNEES_INSUFFISANTES"
    VALIDATION_FAILED = "VALIDATION_FAILED"
    ESCALADED = "ESCALADED"


@dataclass(frozen=True, slots=True)
class HarnessConfig:
    """Configuration immuable du harnais 80/20."""

    schema_path: Path
    max_repair_retries: int = 2
    max_payload_bytes: int = 65536
    allowed_grounding_ids: frozenset[str] = frozenset()


@dataclass(frozen=True, slots=True)
class HarnessOutcome:
    """Resultat scelle d'une execution de DeterministicHarness.run."""

    status: StepStatus
    validated_payload: dict[str, Any] | None
    escalade_reason: str | None
    repair_attempts: int
    step_trace: tuple[str, ...]
    output_sha256: str


def _walk_strict_rules(node: Any, ptr: str, errs: list[str]) -> None:
    if isinstance(node, list):
        for idx, item in enumerate(node):
            _walk_strict_rules(item, f"{ptr}[{idx}]", errs)
        return
    if not isinstance(node, dict):
        return
    ref = node.get("$ref")
    if isinstance(ref, str) and ref.strip().lower().startswith(
        ("http://", "https://")
    ):
        errs.append(f"{ptr}: $ref reseau interdit ({ref})")
    if node.get("additionalProperties") is True:
        errs.append(f"{ptr}: additionalProperties=true interdit")
    t_val = node.get("type")
    is_obj = t_val == "object" or (
        isinstance(t_val, list) and "object" in t_val
    )
    props = node.get("properties")
    if (is_obj or isinstance(props, dict)) and (
        node.get("additionalProperties") is not False
    ):
        errs.append(f"{ptr}: additionalProperties=false requis")
    if isinstance(props, dict):
        req = node.get("required")
        req_set = set(req) if isinstance(req, list) else set()
        missing = sorted(k for k in props if k not in req_set)
        if missing:
            errs.append(f"{ptr}: champs absents de required {missing}")
        for name, sub in props.items():
            _walk_strict_rules(sub, f"{ptr}.properties.{name}", errs)
    for key, val in node.items():
        if key != "properties" and isinstance(val, (dict, list)):
            _walk_strict_rules(val, f"{ptr}.{key}", errs)


def validate_strict_schema(
    schema: dict[str, Any], instance: dict[str, Any]
) -> list[str]:
    """Valide schema Draft 2020-12 strict: true puis l'instance."""
    errs: list[str] = []
    if not isinstance(schema, dict):
        return ["Schema doit etre un objet JSON"]
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        return [f"Meta-schema Draft 2020-12 invalide : {exc.message}"]
    for banned in ("allOf", "if", "then", "else"):
        if banned in schema:
            errs.append(f"Mot-cle racine interdit : {banned}")
    _walk_strict_rules(schema, "$", errs)
    if errs:
        return errs
    validator = Draft202012Validator(schema)
    for err in sorted(
        validator.iter_errors(instance),
        key=lambda e: tuple(str(p) for p in e.path),
    ):
        errs.append(err.message)
    return errs


def _check_grounding(
    cand: dict[str, Any],
    raw_input: dict[str, Any],
    grounding_records: dict[str, Any],
    allowed_ids: frozenset[str],
) -> list[str]:
    errs: list[str] = []
    ref = cand.get("reference_dossier")
    if allowed_ids and ref not in allowed_ids:
        errs.append(f"reference_dossier hors perimetre : {ref}")
    if ref not in grounding_records:
        errs.append(f"reference_dossier absent des pieces : {ref}")
    elif ref != raw_input.get("reference_dossier"):
        errs.append("reference_dossier discordant avec l'entree")
    else:
        rec = grounding_records[ref]
        max_c = rec.get("max_montant_cents") if isinstance(rec, dict) else None
        amt = cand.get("montant_reclame_cents")
        if amt is not None and max_c is not None and amt > max_c:
            errs.append(f"montant {amt} > plafond piece {max_c}")
    statut = cand.get("statut_analyse")
    if statut in ("AMBIGU_ESCALADE", "DONNEES_INSUFFISANTES"):
        if not cand.get("motif_escalade"):
            errs.append("motif_escalade requis pour escalade")
    elif statut == "EXTRAIT" and cand.get("montant_reclame_cents") is None:
        errs.append("montant_reclame_cents requis pour EXTRAIT")
    return errs


def _seal_outcome(
    status: StepStatus,
    payload: dict[str, Any] | None,
    reason: str | None,
    retries: int,
    trace: list[str],
) -> HarnessOutcome:
    digest = jcs_sha256_hex(
        {"status": str(status), "payload": payload, "trace": trace}
    )
    return HarnessOutcome(
        status=status,
        validated_payload=payload,
        escalade_reason=reason,
        repair_attempts=retries,
        step_trace=tuple(trace),
        output_sha256=digest,
    )


class DeterministicHarness:
    """Orchestre les 8 etapes deterministes hors invite."""

    def __init__(
        self, config: HarnessConfig,
        model_adapter: Callable[[dict[str, Any], list[str]], dict[str, Any]],
    ) -> None:
        self._config = config
        self._model_adapter = model_adapter

    def _check_input(self, raw_input: dict[str, Any]) -> HarnessOutcome | None:
        try:
            raw = json.dumps(
                raw_input, ensure_ascii=False, allow_nan=False
            ).encode("utf-8")
        except (TypeError, ValueError, UnicodeEncodeError):
            return _seal_outcome(
                StepStatus.VALIDATION_FAILED, None, "utf8_invalide",
                0, ["1_size_utf8_fail"],
            )
        if len(raw) > self._config.max_payload_bytes:
            return _seal_outcome(
                StepStatus.VALIDATION_FAILED, None, "payload_trop_volumineux",
                0, ["1_size_utf8_fail"],
            )
        if validate_strict_schema(_INPUT_SCHEMA, raw_input):
            return _seal_outcome(
                StepStatus.VALIDATION_FAILED, None, "entree_invalide",
                0, ["1_size_utf8", "2_input_schema_fail"],
            )
        return None

# CA-G0-SYNC-BEGIN:G0-EX-CH01-02
    def run(
        self, raw_input: dict[str, Any], grounding_records: dict[str, Any]
    ) -> HarnessOutcome:
        """Execute les 8 etapes deterministes 80/20 hors invite."""
        if (bad := self._check_input(raw_input)) is not None:
            return bad
        schema = json.loads(self._config.schema_path.read_text("utf-8"))
        ctx = {"input": raw_input, "refs": sorted(grounding_records)}
        trace = ["1_size_utf8", "2_input", "3_ctx", "4_model"]
        retries, errs, cand = 0, [], self._model_adapter(ctx, [])
        while True:
            errs = validate_strict_schema(schema, cand) or _check_grounding(
                cand, raw_input, grounding_records,
                self._config.allowed_grounding_ids,
            )
            if not errs or retries >= self._config.max_repair_retries:
                break
            retries += 1
            cand = self._model_adapter(ctx, errs)
        trace.extend(["5_schema", "6_grounding", "7_repair", "8_seal"])
        if errs:
            return _seal_outcome(
                StepStatus.ESCALADED, None, "; ".join(errs), retries, trace
            )
        raw_st = cand["statut_analyse"]
        st = StepStatus.OK if raw_st == "EXTRAIT" else StepStatus(raw_st)
        return _seal_outcome(
            st, cand, cand.get("motif_escalade"), retries, trace
        )
# CA-G0-SYNC-END:G0-EX-CH01-02
