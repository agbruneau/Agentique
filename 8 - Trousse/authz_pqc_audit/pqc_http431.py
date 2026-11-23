# SPDX-License-Identifier: MIT
"""Banc exact HTTP 431 O(sauts) vs Transaction Tokens O(1) sous ML-DSA."""

from __future__ import annotations

import base64
from dataclasses import dataclass
from enum import StrEnum
from functools import lru_cache
import json
from typing import Any, Literal

import cbor2
from dilithium_py.ml_dsa import ML_DSA_65, ML_DSA_87

from harness_proto.jcs import jcs_sha256_hex


class PqcProfile(StrEnum):
    """Profils de transport cryptographique de delegation PQC."""

    JWT_EMBEDDED_JWK = "JWT_EMBEDDED_JWK"
    JWT_X5C_CHAIN = "JWT_X5C_CHAIN"
    JWT_KID_REF = "JWT_KID_REF"
    CBOR_COSE_CWT = "CBOR_COSE_CWT"
    TRANSACTION_TOKEN_JWT = "TRANSACTION_TOKEN_JWT"
    TRANSACTION_TOKEN_CBOR = "TRANSACTION_TOKEN_CBOR"


ML_DSA_SPECS: dict[str, dict[str, int]] = {
    "ML-DSA-65": {"sig_bytes": 3309, "pk_bytes": 1952},
    "ML-DSA-87": {"sig_bytes": 4627, "pk_bytes": 2592},
}

_SEED = b"trousse-vol8-pqc-http431-seed-v1"


@dataclass(frozen=True, slots=True)
class Http431Measurement:
    """Mesure exacte en octets d'un en-tete HTTP sous ML-DSA."""

    alg: str
    profile: PqcProfile
    hops: int
    header_bytes: int
    header_limit_bytes: int
    exceeds_limit: bool
    http_status: int


def _b64u(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


@lru_cache(maxsize=4)
def _default_keypair(alg: str) -> tuple[bytes, bytes]:
    cls = ML_DSA_65 if alg == "ML-DSA-65" else ML_DSA_87
    return cls.key_derive(_SEED)


def _ml_dsa_sign(alg: str, sk: bytes, msg: bytes) -> bytes:
    cls = ML_DSA_65 if alg == "ML-DSA-65" else ML_DSA_87
    return cls.sign(sk, msg, deterministic=True)


def _hop_claims(claims: dict[str, Any], hops: int) -> dict[str, Any]:
    act: dict[str, Any] = {"sub": f"spiffe://ent.ca/agent-hop-{hops}"}
    for idx in range(hops - 1, 0, -1):
        act = {"sub": f"spiffe://ent.ca/agent-hop-{idx}", "act": act}
    return {
        "iss": "https://idp.ent.ca",
        "aud": "https://mcp.ent.ca",
        "iat": 1793084712,
        "exp": 1793085600,
        "jti": "3b7e90a1-6c52-4d8e-9a17-c4e05b2f8d66",
        **claims,
        "act": act,
    }


def _build_tx_token_payload(claims: dict[str, Any], hops: int) -> bytes:
    tctx_hash = jcs_sha256_hex({"claims": claims, "hops": hops})
    fixed_payload = {
        "iss": "https://tts.ent.ca",
        "aud": "https://mcp.ent.ca",
        "sub": str(claims.get("sub", "alice")),
        "txn": "txn-00000000-0000-4000-8000-000000000001",
        "tctx": tctx_hash,
        "iat": 1793084712,
        "exp": 1793085012,
    }
    return json.dumps(fixed_payload, separators=(",", ":")).encode("utf-8")


def _build_frame_bytes(
    alg: str,
    profile: PqcProfile,
    hops: int,
    claims: dict[str, Any],
    pk: bytes,
    sk: bytes,
) -> bytes:
    if profile == PqcProfile.TRANSACTION_TOKEN_CBOR:
        prot = cbor2.dumps({1: -49, 4: b"tts-ml-dsa"})
        pay = _build_tx_token_payload(claims, hops)
        sig = _ml_dsa_sign(alg, sk, prot + pay)
        return cbor2.dumps([prot, {}, pay, sig])
    if profile == PqcProfile.TRANSACTION_TOKEN_JWT:
        hdr = _b64u(json.dumps({"alg": alg, "typ": "txn+jwt"}).encode())
        pay = _b64u(_build_tx_token_payload(claims, hops))
        sig = _b64u(_ml_dsa_sign(alg, sk, f"{hdr}.{pay}".encode("ascii")))
        return f"{hdr}.{pay}.{sig}".encode("ascii")
    if profile == PqcProfile.CBOR_COSE_CWT:
        hop_frames = []
        for idx in range(1, hops + 1):
            prot = cbor2.dumps({1: -49, 4: f"hop-{idx}".encode()})
            pay = cbor2.dumps(_hop_claims(claims, idx))
            sig = _ml_dsa_sign(alg, sk, prot + pay)
            hop_frames.append([prot, {}, pay, sig])
        obj = hop_frames[0] if hops == 1 else hop_frames
        return cbor2.dumps(obj)
    tokens: list[bytes] = []
    for idx in range(1, hops + 1):
        hdr_obj: dict[str, Any] = {"alg": alg, "typ": "JWT"}
        if profile == PqcProfile.JWT_EMBEDDED_JWK:
            hdr_obj["jwk"] = {"kty": "AKP", "alg": alg, "pub": _b64u(pk)}
        elif profile == PqcProfile.JWT_X5C_CHAIN:
            cert_sig = _ml_dsa_sign(alg, sk, pk)
            cert_der = pk + cert_sig + b"\x30\x82\x00\x20"
            hdr_obj["x5c"] = [base64.b64encode(cert_der).decode("ascii")]
        else:
            hdr_obj["kid"] = f"ml-dsa-hop-{idx}"
        hdr_b = _b64u(json.dumps(hdr_obj, separators=(",", ":")).encode())
        pay_b = _b64u(
            json.dumps(_hop_claims(claims, idx), separators=(",", ":")).encode()
        )
        sig_b = _b64u(_ml_dsa_sign(alg, sk, f"{hdr_b}.{pay_b}".encode()))
        tokens.append(f"{hdr_b}.{pay_b}.{sig_b}".encode("ascii"))
    return b"~".join(tokens)


_CBOR_PROFILES = frozenset(
    {PqcProfile.CBOR_COSE_CWT, PqcProfile.TRANSACTION_TOKEN_CBOR}
)
_TX_PFX, _AUTH_PFX = b"Txn-Token: ", b"Authorization: Bearer "


# CA-G0-SYNC-BEGIN:G0-EX-CH02-03
def build_signed_delegation_frame(
    alg: Literal["ML-DSA-65", "ML-DSA-87"], profile: PqcProfile, hops: int,
    claims: dict[str, Any], keypair: tuple[bytes, bytes] | None = None,
) -> bytes:
    """Construit et signe la trame JWT (RFC 9964) ou CBOR-COSE."""
    prof = PqcProfile(profile)
    if (alg not in ML_DSA_SPECS or type(hops) is not int or hops < 1
            or not isinstance(claims, dict)):
        raise ValueError(f"Parametres PQC invalides : {alg}, hops={hops}")
    pk, sk = keypair if keypair is not None else _default_keypair(alg)
    return _build_frame_bytes(alg, prof, hops, claims, pk, sk)

def evaluate_http_431(
    alg: Literal["ML-DSA-65", "ML-DSA-87"], profile: PqcProfile,
    hops: int, header_limit_bytes: int = 8192,
) -> Http431Measurement:
    """Mesure Authorization / Txn-Token et detecte HTTP 431."""
    prof = PqcProfile(profile)
    frame = build_signed_delegation_frame(
        alg, prof, hops, {"sub": "alice", "scope": "finance:read"}
    )
    wire = _b64u(frame).encode("ascii") if prof in _CBOR_PROFILES else frame
    pfx = _TX_PFX if "TRANSACTION_TOKEN" in prof.value else _AUTH_PFX
    total = len(pfx) + len(wire)
    exceeds = total > header_limit_bytes
    return Http431Measurement(
        alg, prof, hops, total, header_limit_bytes,
        exceeds, 431 if exceeds else 200,
    )
# CA-G0-SYNC-END:G0-EX-CH02-03
