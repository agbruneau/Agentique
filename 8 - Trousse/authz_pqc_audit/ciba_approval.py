# SPDX-License-Identifier: MIT
"""Approbation humaine hors bande CIBA, I-JSON RFC 7493 et contrat C.6."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from harness_proto.jcs import jcs_sha256_hex

_MAX_IJSON_INT = (1 << 53) - 1


class IJsonError(ValueError):
    """Erreur levee sur violation I-JSON RFC 7493 (flottant, NaN, etc.)."""


@dataclass(frozen=True, slots=True)
class ApprovalVerdict:
    """Verdict verifie des jetons d'approbation humaine C.6."""

    approved: bool
    approver_subs: tuple[str, ...]
    action_sha256: str
    rejection_reason: str | None


def validate_ijson_strict(payload: Any) -> None:
    """Valide I-JSON RFC 7493 : pas de float/NaN/Inf ni surrogates isoles."""
    if payload is None or isinstance(payload, bool):
        return
    if isinstance(payload, int):
        if payload < -_MAX_IJSON_INT or payload > _MAX_IJSON_INT:
            raise IJsonError(f"Entier hors plage I-JSON : {payload}")
        return
    if isinstance(payload, float):
        raise IJsonError(f"Flottant interdit en I-JSON C.6 : {payload!r}")
    if isinstance(payload, str):
        try:
            payload.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise IJsonError(f"Surrogate UTF-8 isole : {exc}") from exc
        return
    if isinstance(payload, list):
        for item in payload:
            validate_ijson_strict(item)
        return
    if isinstance(payload, dict):
        for k, v in payload.items():
            if not isinstance(k, str):
                raise IJsonError(f"Cle non-str I-JSON : {k!r}")
            validate_ijson_strict(k)
            validate_ijson_strict(v)
        return
    raise IJsonError(f"Type non I-JSON : {type(payload).__name__}")


def _validate_single_ciba_token(
    tok: dict[str, Any],
    expected_h: str,
    expected_task_id: str,
    expected_agent_id: str,
    principal_sub: str,
    now_ts: int,
    seen_subs: set[str],
    seen_jtis: set[str],
    consumed_jtis: set[str] | None,
) -> tuple[str | None, str | None]:
    hdr = tok.get("header") if isinstance(tok, dict) else None
    clm = tok.get("claims") if isinstance(tok, dict) else None
    if not isinstance(hdr, dict) or not isinstance(clm, dict):
        return None, "Structure de jeton C.6 invalide"
    if hdr.get("typ") != "approbation+jwt":
        return None, "Type de jeton invalide (approbation+jwt requis)"
    try:
        validate_ijson_strict(clm)
    except IJsonError as exc:
        return None, str(exc)
    if not isinstance(expected_h, str) or len(expected_h) != 64:
        return None, "expected_h invalide"
    if clm.get("action_sha256") != expected_h:
        return None, "Discordance action_sha256 (h)"
    if clm.get("task_id") != expected_task_id:
        return None, "Discordance task_id"
    if clm.get("agent_id") != expected_agent_id:
        return None, "Discordance agent_id"
    exp = clm.get("exp")
    if isinstance(exp, bool) or not isinstance(exp, int) or exp <= now_ts:
        return None, "Jeton d'approbation expire"
    sub = clm.get("sub")
    if not isinstance(sub, str) or not sub or sub == principal_sub:
        return None, "Auto-approbation ou sub manquant"
    if sub in seen_subs:
        return None, "Approbateur duplique"
    jti = clm.get("jti")
    if not isinstance(jti, str) or not jti or jti in seen_jtis:
        return None, "jti manquant ou duplique"
    if consumed_jtis is not None and jti in consumed_jtis:
        return None, "Reutilisation jti interdite"
    seen_subs.add(sub)
    seen_jtis.add(jti)
    return sub, None


# CA-G0-SYNC-BEGIN:G0-EX-CH02-02
def compute_action_hash_h(
    outil: str, version: str, definition_digest: str,
    agent_id: str, task_id: str, arguments: dict[str, Any],
) -> str:
    """Valide I-JSON puis calcule h = SHA-256(JCS(action)) selon C.6."""
    obj = {
        "outil": outil, "version": version,
        "definition_digest": definition_digest,
        "agent_id": agent_id, "task_id": task_id, "arguments": arguments,
    }
    validate_ijson_strict(obj)
    return jcs_sha256_hex(obj)
# CA-G0-SYNC-END:G0-EX-CH02-02


def verify_ciba_approval_tokens(
    tokens: list[dict[str, Any]], expected_h: str, expected_task_id: str,
    expected_agent_id: str, principal_sub: str, required_approvers: int,
    now_ts: int, consumed_jtis: set[str] | None = None,
) -> ApprovalVerdict:
    """Verifie typ=approbation+jwt, h, approbateurs distincts et jti."""
    subs, jtis, approvers = set(), set(), []
    for tok in tokens:
        sub, err = _validate_single_ciba_token(
            tok, expected_h, expected_task_id, expected_agent_id,
            principal_sub, now_ts, subs, jtis, consumed_jtis,
        )
        if err is not None:
            return ApprovalVerdict(False, (), expected_h, err)
        approvers.append(str(sub))
    if (
        isinstance(required_approvers, bool)
        or not isinstance(required_approvers, int)
        or required_approvers < 1
        or len(approvers) < required_approvers
    ):
        return ApprovalVerdict(False, (), expected_h, "Quorum insuffisant")
    if consumed_jtis is not None:
        consumed_jtis.update(jtis)
    return ApprovalVerdict(True, tuple(approvers), expected_h, None)
