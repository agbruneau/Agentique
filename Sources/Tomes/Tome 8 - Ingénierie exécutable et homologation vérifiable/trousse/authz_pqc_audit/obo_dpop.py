# SPDX-License-Identifier: MIT
"""Delegation OAuth 2.0 OBO (RFC 8693/8707) et liaison DPoP (RFC 9449)."""

from __future__ import annotations

import base64
from dataclasses import dataclass
import hashlib
from typing import Any


@dataclass(frozen=True, slots=True)
class OboValidationResult:
    """Resultat borne de validation d'une delegation OBO + DPoP."""

    accepted: bool
    principal_sub: str
    actor_chain: tuple[str, ...]
    hop_count: int
    rejection_code: str | None


def _check_dpop_binding(
    claims: dict[str, Any],
    dpop_proof: dict[str, Any] | None,
    http_method: str,
    http_uri: str,
    access_token: str | None,
    used_dpop_jtis: set[str] | None,
) -> str | None:
    cnf = claims.get("cnf")
    if not isinstance(cnf, dict):
        return "MISSING_CNF_BINDING"
    jkt = cnf.get("jkt")
    x5t = cnf.get("x5t#S256")
    bound = jkt if isinstance(jkt, str) and jkt else (
        x5t if isinstance(x5t, str) and x5t else None
    )
    if bound is None:
        return "MISSING_CNF_BINDING"
    if not isinstance(dpop_proof, dict):
        return "MISSING_DPOP_PROOF"
    if dpop_proof.get("typ") != "dpop+jwt":
        return "INVALID_DPOP_TYP"
    if dpop_proof.get("htm") != http_method:
        return "DPOP_HTM_MISMATCH"
    if dpop_proof.get("htu") != http_uri:
        return "DPOP_HTU_MISMATCH"
    proof_bind = (
        dpop_proof.get("jwk_thumbprint")
        if isinstance(jkt, str) and jkt
        else (dpop_proof.get("x5t#S256") or dpop_proof.get("jwk_thumbprint"))
    )
    if proof_bind != bound:
        return "DPOP_CNF_MISMATCH"
    if access_token is not None:
        digest = hashlib.sha256(access_token.encode("ascii")).digest()
        exp_ath = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
        if dpop_proof.get("ath") != exp_ath:
            return "DPOP_ATH_MISMATCH"
    jti = dpop_proof.get("jti")
    if not isinstance(jti, str) or not jti:
        return "MISSING_DPOP_JTI"
    if used_dpop_jtis is not None and jti in used_dpop_jtis:
        return "DPOP_JTI_REPLAY"
    return None


def extract_act_chain(claims: dict[str, Any]) -> tuple[str, ...]:
    """Deroule iterativement la chaine imbriquee 'act' (RFC 8693)."""
    if not isinstance(claims, dict):
        return ()
    chain, cur, seen = [], claims.get("act"), set()
    while isinstance(cur, dict) and id(cur) not in seen and len(chain) < 64:
        seen.add(id(cur))
        sub = cur.get("sub")
        if not isinstance(sub, str) or not sub:
            break
        chain.append(sub)
        cur = cur.get("act")
    return tuple(chain)


# CA-G0-SYNC-BEGIN:G0-EX-CH02-01
def validate_obo_delegation(
    token_claims: dict[str, Any], expected_audience: str,
    parent_exp: int | None, dpop_proof: dict[str, Any] | None,
    http_method: str, http_uri: str, now_ts: int, max_hops: int = 2,
    access_token: str | None = None, used_dpop_jtis: set[str] | None = None,
) -> OboValidationResult:
    """Valide OBO <= max_hops, aud, parent_exp et liaison DPoP + cnf."""
    raw = token_claims.get("sub") if isinstance(token_claims, dict) else ""
    sub = raw if isinstance(raw, str) else ""
    chain = extract_act_chain(token_claims)
    hops, exp = len(chain), token_claims.get("exp") if sub else None
    if not sub or hops == 0:
        err = "MISSING_NHI_ACTOR"
    elif token_claims.get("aud") != expected_audience:
        err = "TOKEN_PASSTHROUGH_AUD_MISMATCH"
    elif hops > max_hops:
        err = "MAX_HOPS_EXCEEDED"
    elif isinstance(exp, bool) or not isinstance(exp, int) or exp <= now_ts:
        err = "TOKEN_EXPIRED"
    elif parent_exp is not None and exp > parent_exp:
        err = "EXP_EXTENSION_FORBIDDEN"
    else:
        err = _check_dpop_binding(
            token_claims, dpop_proof, http_method, http_uri, access_token,
            used_dpop_jtis)
    if err is not None:
        return OboValidationResult(False, sub, chain, hops, err)
    if used_dpop_jtis is not None and dpop_proof is not None:
        used_dpop_jtis.add(str(dpop_proof["jti"]))
    return OboValidationResult(True, sub, chain, hops, None)
# CA-G0-SYNC-END:G0-EX-CH02-01
