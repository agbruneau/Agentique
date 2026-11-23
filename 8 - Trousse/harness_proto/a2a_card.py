# SPDX-License-Identifier: MIT
"""Validation AgentCard A2A v1.0.1 par JWS ES256 sur JCS et epinglage jku."""

from __future__ import annotations

import base64
import copy
from dataclasses import dataclass
import json
from typing import Any

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature,
)
from jsonschema import Draft202012Validator

from harness_proto.jcs import JcsError, canonicalize_jcs, jcs_sha256_hex

_BANNED_OAUTH_FLOWS = frozenset({"password", "implicit"})
_V101_TOP_KEYS = frozenset(
    {
        "name", "description", "supportedInterfaces", "provider", "version",
        "capabilities", "securitySchemes", "securityRequirements",
        "defaultInputModes", "defaultOutputModes", "skills", "signatures",
    }
)


@dataclass(frozen=True, slots=True)
class AgentCardVerdict:
    """Verdict immuable de validation d'une AgentCard A2A."""

    valid: bool
    card_etag: str
    signer_kid: str
    errors: tuple[str, ...]


class AgentCardAdapter:
    """Adaptateur versionne pour projections A2A v1.1.0-rc vers v1.0.1."""

    def __init__(self, protocol_version: str = "1.0") -> None:
        self.protocol_version = protocol_version

    def adapt(self, card: dict[str, Any]) -> dict[str, Any]:
        """Normalise une carte vers le contrat v1.0.1 valide en G0."""
        adapted = copy.deepcopy(card)
        if self.protocol_version.startswith("1.1"):
            adapted = {
                k: v for k, v in adapted.items() if k in _V101_TOP_KEYS
            }
            ifaces = adapted.get("supportedInterfaces")
            if isinstance(ifaces, list):
                for iface in ifaces:
                    if isinstance(iface, dict) and str(
                        iface.get("protocolVersion", "")
                    ).startswith("1.1"):
                        iface["protocolVersion"] = "1.0"
        return adapted


def _b64u_decode(data: str) -> bytes:
    pad = "=" * ((4 - len(data) % 4) % 4)
    return base64.urlsafe_b64decode(data + pad)


def _check_card_structure_and_policies(
    card: dict[str, Any],
    approved_extensions: set[str],
    schema: dict[str, Any],
) -> list[str]:
    errs: list[str] = []
    if not isinstance(card, dict):
        return ["AgentCard doit etre un objet JSON"]
    for s_err in Draft202012Validator(schema).iter_errors(card):
        errs.append(s_err.message)
    schemes = card.get("securitySchemes")
    if isinstance(schemes, dict):
        for scheme_name, scheme_obj in schemes.items():
            if not isinstance(scheme_obj, dict):
                continue
            oauth = scheme_obj.get("oauth2SecurityScheme")
            flows = oauth.get("flows") if isinstance(oauth, dict) else None
            if isinstance(flows, dict):
                for bad in _BANNED_OAUTH_FLOWS.intersection(flows.keys()):
                    errs.append(f"Flux OAuth interdit ({scheme_name}): {bad}")
    caps = card.get("capabilities")
    exts = caps.get("extensions") if isinstance(caps, dict) else None
    if isinstance(exts, list):
        for ext in exts:
            if isinstance(ext, dict):
                uri = ext.get("uri")
                if uri not in approved_extensions:
                    errs.append(f"Extension non approuvee : {uri}")
    return errs


def _verify_es256_jwk(
    jwks: dict[str, Any], kid: str, signing_input: bytes, sig_b64: str
) -> str | None:
    keys = jwks.get("keys") if isinstance(jwks, dict) else None
    if not isinstance(keys, list):
        return "JWKS invalide"
    jwk = next(
        (k for k in keys if isinstance(k, dict) and k.get("kid") == kid), None
    )
    if (
        jwk is None
        or jwk.get("kty") != "EC"
        or jwk.get("crv") != "P-256"
        or jwk.get("alg") not in (None, "ES256")
        or jwk.get("use") not in (None, "sig")
        or not isinstance(jwk.get("x"), str)
        or not isinstance(jwk.get("y"), str)
    ):
        return f"Cle P-256 introuvable pour kid={kid!r}"
    try:
        x_int = int.from_bytes(_b64u_decode(jwk["x"]), "big")
        y_int = int.from_bytes(_b64u_decode(jwk["y"]), "big")
        raw_sig = _b64u_decode(sig_b64)
        if len(raw_sig) != 64:
            return "Longueur signature ES256 invalide"
        r_val = int.from_bytes(raw_sig[:32], "big")
        s_val = int.from_bytes(raw_sig[32:], "big")
        pub = ec.EllipticCurvePublicNumbers(
            x_int, y_int, ec.SECP256R1()
        ).public_key()
        pub.verify(
            encode_dss_signature(r_val, s_val),
            signing_input,
            ec.ECDSA(hashes.SHA256()),
        )
    except (InvalidSignature, KeyError, TypeError, ValueError) as exc:
        return f"Echec verification JWS ES256 : {exc}"
    return None


def _parse_jws_sig(card: dict[str, Any]) -> tuple[str, dict[str, Any], str]:
    sigs = card.get("signatures")
    if not isinstance(sigs, list) or not sigs or not isinstance(sigs[0], dict):
        raise ValueError("Liste signatures JWS invalide")
    sig_obj = sigs[0]
    prot_b64 = sig_obj.get("protected")
    sig_b64 = sig_obj.get("signature")
    if not isinstance(prot_b64, str) or not isinstance(sig_b64, str):
        raise ValueError("Objet signature JWS invalide")
    hdr = json.loads(_b64u_decode(prot_b64).decode("utf-8"))
    if not isinstance(hdr, dict):
        raise ValueError("En-tete protege JWS non-objet")
    return prot_b64, hdr, sig_b64


# CA-G0-SYNC-BEGIN:G0-EX-CH01-04
def validate_agent_card(
    card: dict[str, Any], jwks: dict[str, Any], pinned_jku: str,
    approved_extensions: set[str], schema: dict[str, Any],
) -> AgentCardVerdict:
    """Valide schema A2A, epinglage jku/kid, JWS ES256 sur JCS."""
    errs = _check_card_structure_and_policies(
        card, approved_extensions, schema
    )
    if errs:
        return AgentCardVerdict(False, "", "", tuple(errs))
    base = {k: v for k, v in card.items() if k != "signatures"}
    try:
        pay_bytes = canonicalize_jcs(base)
        etag = jcs_sha256_hex(base)
        prot_b64, hdr, sig_b64 = _parse_jws_sig(card)
    except (JcsError, ValueError, UnicodeDecodeError) as exc:
        return AgentCardVerdict(False, "", "", (str(exc),))
    raw_kid = hdr.get("kid")
    kid = raw_kid if isinstance(raw_kid, str) else ""
    if hdr.get("alg") != "ES256" or hdr.get("jku") != pinned_jku or not kid:
        return AgentCardVerdict(False, etag, kid, ("jku/alg/kid invalide",))
    b64_pay = base64.urlsafe_b64encode(pay_bytes).rstrip(b"=").decode()
    err = _verify_es256_jwk(
        jwks, kid, f"{prot_b64}.{b64_pay}".encode(), sig_b64
    )
    return AgentCardVerdict(err is None, etag, kid, (err,) if err else ())
# CA-G0-SYNC-END:G0-EX-CH01-04
