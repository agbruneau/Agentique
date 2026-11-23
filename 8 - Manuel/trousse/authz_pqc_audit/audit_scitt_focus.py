# SPDX-License-Identifier: MIT
"""Chaine probatoire JCS (C.8), arbre Merkle SCITT (RFC 9943) et FOCUS."""

from __future__ import annotations

import copy
from dataclasses import dataclass
from decimal import Decimal
import hashlib
from typing import Any

from authz_pqc_audit.slh_dsa_fips205 import sign_slh_dsa_sha2_128s
from harness_proto.jcs import JcsError, jcs_sha256_hex

_GENESIS_PREV = "sha256:" + ("0" * 64)


@dataclass(frozen=True, slots=True)
class ChainVerdict:
    """Verdict d'integrite d'une chaine d'audit C.8."""

    valid: bool
    record_count: int
    broken_sequence: int | None
    reason: str | None


@dataclass(frozen=True, slots=True)
class ScittTree:
    """Arbre de Merkle SCITT RFC 9943."""

    root_hash: bytes
    leaves: tuple[bytes, ...]
    levels: tuple[tuple[bytes, ...], ...]


@dataclass(frozen=True, slots=True)
class FocusCpoSummary:
    """Agregation FinOps FOCUS v1.4, CPO Decimal exact et carbone CAP-046."""

    total_effective_cost_cad: Decimal
    compliant_outcomes: int
    cpo_cad: Decimal
    total_carbon_gco2e: Decimal
    total_energy_kwh: Decimal
    focus_records: tuple[dict[str, Any], ...]


class AuditChainLedger:
    """Journal d'audit immuable chaine par JCS SHA-256 (C.8)."""

    def __init__(self, flux: str = "passerelle-agents-03") -> None:
        self.flux = flux
        self._records: list[dict[str, Any]] = []

    def append_record(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Ajoute sequence, flux, precedent_sha256 dans enregistrement et
        retourne {empreinte, enregistrement, signature} conforme a C.8."""
        seq = len(self._records) + 1
        prev = (
            self._records[-1]["empreinte"] if self._records else _GENESIS_PREV
        )
        enreg = copy.deepcopy(payload)
        enreg["flux"] = self.flux
        enreg["sequence"] = seq
        enreg["precedent_sha256"] = prev
        empreinte = "sha256:" + jcs_sha256_hex(enreg)
        sig = {
            "alg": "JCS-SHA256",
            "kid": f"{self.flux}-audit-v1",
            "valeur": empreinte.split(":", 1)[1],
        }
        record = {
            "empreinte": empreinte,
            "enregistrement": enreg,
            "signature": sig,
        }
        self._records.append(record)
        return copy.deepcopy(record)

    def verify_chain(self, records: list[dict[str, Any]]) -> ChainVerdict:
        """Verifie le chainage integral et les condensats JCS."""
        expected_prev = _GENESIS_PREV
        expected_flux: str | None = None
        for idx, rec in enumerate(records, start=1):
            if not isinstance(rec, dict):
                return ChainVerdict(
                    False, len(records), idx, "Enregistrement non-dict"
                )
            enreg = rec.get("enregistrement")
            if not isinstance(enreg, dict):
                return ChainVerdict(
                    False, len(records), idx, "Champ enregistrement manquant"
                )
            flux = enreg.get("flux")
            if not isinstance(flux, str) or not flux:
                return ChainVerdict(
                    False, len(records), idx, "Champ flux invalide"
                )
            if expected_flux is None:
                expected_flux = flux
            elif flux != expected_flux:
                return ChainVerdict(
                    False, len(records), idx, "Flux inconsistant"
                )
            if enreg.get("sequence") != idx:
                return ChainVerdict(
                    False, len(records), idx, "Sequence discontinue"
                )
            if enreg.get("precedent_sha256") != expected_prev:
                return ChainVerdict(
                    False, len(records), idx, "Rupture precedent_sha256"
                )
            try:
                hex_dig = jcs_sha256_hex(enreg)
            except JcsError as exc:
                return ChainVerdict(
                    False, len(records), idx, f"JCS invalide : {exc}"
                )
            computed = "sha256:" + hex_dig
            if rec.get("empreinte") != computed:
                return ChainVerdict(
                    False, len(records), idx, "Empreinte JCS SHA-256 invalide"
                )
            sig = rec.get("signature")
            if not isinstance(sig, dict) or (
                sig.get("alg") == "JCS-SHA256" and sig.get("valeur") != hex_dig
            ):
                return ChainVerdict(
                    False, len(records), idx, "Signature C.8 invalide"
                )
            expected_prev = rec["empreinte"]
        return ChainVerdict(True, len(records), None, None)


def _hash_leaf(leaf: bytes) -> bytes:
    return hashlib.sha256(b"\x00" + leaf).digest()


def _hash_node(left: bytes, right: bytes) -> bytes:
    return hashlib.sha256(b"\x01" + left + right).digest()


def _largest_pow2_lt(n: int) -> int:
    k = 1
    while (k << 1) < n:
        k <<= 1
    return k


def _mth(hashed_leaves: tuple[bytes, ...]) -> bytes:
    n = len(hashed_leaves)
    if n == 1:
        return hashed_leaves[0]
    k = _largest_pow2_lt(n)
    return _hash_node(_mth(hashed_leaves[:k]), _mth(hashed_leaves[k:]))


def _audit_path(m: int, hashed_leaves: tuple[bytes, ...]) -> list[bytes]:
    n = len(hashed_leaves)
    if n <= 1:
        return []
    k = _largest_pow2_lt(n)
    if m < k:
        return _audit_path(m, hashed_leaves[:k]) + [_mth(hashed_leaves[k:])]
    return _audit_path(m - k, hashed_leaves[k:]) + [_mth(hashed_leaves[:k])]


def build_scitt_merkle_tree(leaf_hashes: list[bytes]) -> ScittTree:
    """Construit un arbre Merkle conforme SCITT RFC 9943."""
    if not leaf_hashes:
        raise ValueError("leaf_hashes ne doit pas etre vide")
    hashed = tuple(_hash_leaf(lf) for lf in leaf_hashes)
    root = _mth(hashed)
    levels: list[tuple[bytes, ...]] = [hashed]
    cur = list(hashed)
    while len(cur) > 1:
        nxt = [
            _hash_node(cur[i], cur[i + 1]) if i + 1 < len(cur) else cur[i]
            for i in range(0, len(cur), 2)
        ]
        levels.append(tuple(nxt))
        cur = nxt
    return ScittTree(
        root_hash=root, leaves=tuple(leaf_hashes), levels=tuple(levels)
    )


def generate_inclusion_proof(tree: ScittTree, index: int) -> list[bytes]:
    """Genere le chemin d'inclusion Merkle pour la feuille index."""
    n = len(tree.leaves)
    if index < 0 or index >= n:
        raise IndexError(f"Index feuille hors bornes : {index}")
    hashed = tree.levels[0]
    return _audit_path(index, hashed)


def verify_inclusion_proof(
    leaf_hash: bytes,
    proof: list[bytes],
    root_hash: bytes,
    index: int,
    total: int,
) -> bool:
    """Verifie une preuve d'inclusion SCITT RFC 9943."""
    if total < 1 or index < 0 or index >= total:
        return False
    node = _hash_leaf(leaf_hash)
    if total == 1:
        return len(proof) == 0 and node == root_hash
    fn = index
    sn = total - 1
    for p_hash in proof:
        if sn == 0:
            return False
        if (fn & 1) == 1 or fn == sn:
            node = _hash_node(p_hash, node)
            if (fn & 1) == 0:
                while (fn & 1) == 0 and fn != 0:
                    fn >>= 1
                    sn >>= 1
        else:
            node = _hash_node(node, p_hash)
        fn >>= 1
        sn >>= 1
    return sn == 0 and node == root_hash


def seal_merkle_root(
    root_hash: bytes, sk_slh_dsa: bytes
) -> dict[str, Any]:
    """Scelle root_hash par SLH-DSA-SHA2-128s et retourne
    {'alg': 'SLH-DSA-SHA2-128s', 'root_hash_hex': ..., 'signature': bytes}."""
    sig = sign_slh_dsa_sha2_128s(
        sk_slh_dsa, root_hash, addr_rnd=None, interface="external"
    )
    return {
        "alg": "SLH-DSA-SHA2-128s",
        "root_hash_hex": root_hash.hex(),
        "signature": sig,
    }


def _to_decimal(val: Any, field_name: str) -> Decimal:
    if isinstance(val, (float, bool)):
        raise TypeError(f"IEEE-754 float/bool interdit pour {field_name}")
    dec = Decimal(str(val))
    if not dec.is_finite() or dec < 0:
        raise ValueError(f"Montant Decimal invalide pour {field_name}: {val!r}")
    return dec


def compute_cpo_and_focus(
    records: list[dict[str, Any]], compliant_outcomes: int
) -> FocusCpoSummary:
    """Calcule en Decimal exact le CPO et les champs FOCUS v1.4 CAP-046."""
    if isinstance(compliant_outcomes, bool) or not isinstance(
        compliant_outcomes, int
    ) or compliant_outcomes <= 0:
        raise ValueError("compliant_outcomes doit etre un entier >= 1")
    total_eff = Decimal("0")
    total_carbon = Decimal("0")
    total_energy = Decimal("0")
    out_records: list[dict[str, Any]] = []
    for rec in records:
        eff = _to_decimal(rec["EffectiveCost"], "EffectiveCost")
        _to_decimal(rec["BilledCost"], "BilledCost")
        carb = _to_decimal(rec.get("x_carbon_gco2e", "0"), "x_carbon_gco2e")
        nrg = _to_decimal(rec.get("x_energy_kwh", "0"), "x_energy_kwh")
        total_eff += eff
        total_carbon += carb
        total_energy += nrg
        out_records.append(copy.deepcopy(rec))
    cpo = total_eff / Decimal(compliant_outcomes)
    return FocusCpoSummary(
        total_effective_cost_cad=total_eff,
        compliant_outcomes=compliant_outcomes,
        cpo_cad=cpo,
        total_carbon_gco2e=total_carbon,
        total_energy_kwh=total_energy,
        focus_records=tuple(out_records),
    )
