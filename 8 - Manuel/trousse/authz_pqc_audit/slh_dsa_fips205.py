# SPDX-License-Identifier: MIT
"""Implementation Python pur MIT de FIPS 205 SLH-DSA-SHA2-128s/128f."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
from typing import Literal

_WOTS_HASH = 0
_WOTS_PK = 1
_TREE = 2
_FORS_TREE = 3
_FORS_ROOTS = 4
_WOTS_PRF = 5
_FORS_PRF = 6


@dataclass(frozen=True, slots=True)
class _SlhParams:
    n: int
    h: int
    d: int
    hp: int
    a: int
    k: int
    m: int
    len_wots: int = 35
    sig_bytes: int = 0


_SHA2_128S = _SlhParams(
    n=16, h=63, d=7, hp=9, a=12, k=14, m=30,
    sig_bytes=(1 + 14 * (1 + 12) + 63 + 7 * 35) * 16,
)
_SHA2_128F = _SlhParams(
    n=16, h=66, d=22, hp=3, a=6, k=33, m=34,
    sig_bytes=(1 + 33 * (1 + 6) + 66 + 22 * 35) * 16,
)


def _adrs_compress(adrs: bytearray) -> bytes:
    return bytes(adrs[3:4] + adrs[8:16] + adrs[19:20] + adrs[20:32])


def _set_layer(adrs: bytearray, layer: int) -> None:
    adrs[0:4] = layer.to_bytes(4, "big")


def _set_tree(adrs: bytearray, tree: int) -> None:
    adrs[4:16] = tree.to_bytes(12, "big")


def _set_type_clear(adrs: bytearray, y: int) -> None:
    adrs[16:20] = y.to_bytes(4, "big")
    adrs[20:32] = b"\x00" * 12


def _set_kp(adrs: bytearray, kp: int) -> None:
    adrs[20:24] = kp.to_bytes(4, "big")


def _get_kp(adrs: bytearray) -> int:
    return int.from_bytes(adrs[20:24], "big")


def _set_chain(adrs: bytearray, ch: int) -> None:
    adrs[24:28] = ch.to_bytes(4, "big")


def _set_hash(adrs: bytearray, h_val: int) -> None:
    adrs[28:32] = h_val.to_bytes(4, "big")


def _set_height(adrs: bytearray, ht: int) -> None:
    adrs[24:28] = ht.to_bytes(4, "big")


def _set_index(adrs: bytearray, idx: int) -> None:
    adrs[28:32] = idx.to_bytes(4, "big")


def _mgf1_sha256(seed: bytes, out_len: int) -> bytes:
    out = bytearray()
    counter = 0
    while len(out) < out_len:
        out.extend(
            hashlib.sha256(seed + counter.to_bytes(4, "big")).digest()
        )
        counter += 1
    return bytes(out[:out_len])


class _Sha2Ctx:
    __slots__ = ("pk_seed", "_base")

    def __init__(self, pk_seed: bytes) -> None:
        self.pk_seed = pk_seed
        self._base = hashlib.sha256(pk_seed + b"\x00" * 48)

    def t_hash(self, adrs: bytearray, data: bytes) -> bytes:
        h = self._base.copy()
        h.update(_adrs_compress(adrs))
        h.update(data)
        return h.digest()[:16]

    def prf_msg(self, sk_prf: bytes, opt_rand: bytes, msg: bytes) -> bytes:
        return hmac.new(sk_prf, opt_rand + msg, hashlib.sha256).digest()[:16]

    def h_msg(
        self, r: bytes, pk_root: bytes, msg: bytes, m_len: int
    ) -> bytes:
        inner = hashlib.sha256(r + self.pk_seed + pk_root + msg).digest()
        return _mgf1_sha256(r + self.pk_seed + inner, m_len)


def _base_2b(x: bytes, b: int, out_len: int) -> list[int]:
    in_idx = 0
    bits = 0
    total = 0
    mask = (1 << b) - 1
    out: list[int] = []
    for _ in range(out_len):
        while bits < b:
            total = (total << 8) + x[in_idx]
            in_idx += 1
            bits += 8
        bits -= b
        out.append((total >> bits) & mask)
    return out


def _chain(
    ctx: _Sha2Ctx, x: bytes, start: int, steps: int, adrs: bytearray
) -> bytes:
    tmp = x
    for j in range(start, start + steps):
        _set_hash(adrs, j)
        tmp = ctx.t_hash(adrs, tmp)
    return tmp


def _wots_msg_nibbles(msg: bytes) -> list[int]:
    nibbles = _base_2b(msg, 4, 32)
    csum = sum(15 - d for d in nibbles) << 4
    nibbles.extend(_base_2b(csum.to_bytes(2, "big"), 4, 3))
    return nibbles


def _wots_pk_gen(
    ctx: _Sha2Ctx, sk_seed: bytes, adrs: bytearray
) -> bytes:
    kp = _get_kp(adrs)
    sk_adrs = bytearray(adrs)
    _set_type_clear(sk_adrs, _WOTS_PRF)
    _set_kp(sk_adrs, kp)
    parts: list[bytes] = []
    for i in range(35):
        _set_chain(sk_adrs, i)
        sk_i = ctx.t_hash(sk_adrs, sk_seed)
        _set_chain(adrs, i)
        parts.append(_chain(ctx, sk_i, 0, 15, adrs))
    pk_adrs = bytearray(adrs)
    _set_type_clear(pk_adrs, _WOTS_PK)
    _set_kp(pk_adrs, kp)
    return ctx.t_hash(pk_adrs, b"".join(parts))


def _wots_sign(
    ctx: _Sha2Ctx, msg: bytes, sk_seed: bytes, adrs: bytearray
) -> bytes:
    nibbles = _wots_msg_nibbles(msg)
    kp = _get_kp(adrs)
    sk_adrs = bytearray(adrs)
    _set_type_clear(sk_adrs, _WOTS_PRF)
    _set_kp(sk_adrs, kp)
    sig_parts: list[bytes] = []
    for i in range(35):
        _set_chain(sk_adrs, i)
        sk_i = ctx.t_hash(sk_adrs, sk_seed)
        _set_chain(adrs, i)
        sig_parts.append(_chain(ctx, sk_i, 0, nibbles[i], adrs))
    return b"".join(sig_parts)


def _wots_pk_from_sig(
    ctx: _Sha2Ctx, sig: bytes, msg: bytes, adrs: bytearray
) -> bytes:
    nibbles = _wots_msg_nibbles(msg)
    kp = _get_kp(adrs)
    parts: list[bytes] = []
    for i in range(35):
        _set_chain(adrs, i)
        s_i = sig[i * 16 : (i + 1) * 16]
        parts.append(_chain(ctx, s_i, nibbles[i], 15 - nibbles[i], adrs))
    pk_adrs = bytearray(adrs)
    _set_type_clear(pk_adrs, _WOTS_PK)
    _set_kp(pk_adrs, kp)
    return ctx.t_hash(pk_adrs, b"".join(parts))


def _build_xmss_tree(
    ctx: _Sha2Ctx, sk_seed: bytes, hp: int, base_adrs: bytearray
) -> list[list[bytes]]:
    leaves: list[bytes] = []
    leaf_adrs = bytearray(base_adrs)
    count = 1 << hp
    for i in range(count):
        _set_type_clear(leaf_adrs, _WOTS_HASH)
        _set_kp(leaf_adrs, i)
        leaves.append(_wots_pk_gen(ctx, sk_seed, leaf_adrs))
    levels: list[list[bytes]] = [leaves]
    tree_adrs = bytearray(base_adrs)
    _set_type_clear(tree_adrs, _TREE)
    for z in range(1, hp + 1):
        prev = levels[-1]
        _set_height(tree_adrs, z)
        nxt: list[bytes] = []
        for i in range(len(prev) // 2):
            _set_index(tree_adrs, i)
            nxt.append(ctx.t_hash(tree_adrs, prev[2 * i] + prev[2 * i + 1]))
        levels.append(nxt)
    return levels


def _xmss_sign_and_root(
    ctx: _Sha2Ctx,
    msg: bytes,
    sk_seed: bytes,
    idx: int,
    hp: int,
    adrs: bytearray,
) -> tuple[bytes, bytes]:
    levels = _build_xmss_tree(ctx, sk_seed, hp, adrs)
    sig_adrs = bytearray(adrs)
    _set_type_clear(sig_adrs, _WOTS_HASH)
    _set_kp(sig_adrs, idx)
    wots_sig = _wots_sign(ctx, msg, sk_seed, sig_adrs)
    auth = b"".join(levels[k][(idx >> k) ^ 1] for k in range(hp))
    return wots_sig + auth, levels[hp][0]


def _xmss_pk_from_sig(
    ctx: _Sha2Ctx,
    idx: int,
    sig_xmss: bytes,
    msg: bytes,
    hp: int,
    adrs: bytearray,
) -> bytes:
    wots_len = 35 * 16
    wots_sig = sig_xmss[:wots_len]
    auth = sig_xmss[wots_len:]
    w_adrs = bytearray(adrs)
    _set_type_clear(w_adrs, _WOTS_HASH)
    _set_kp(w_adrs, idx)
    node = _wots_pk_from_sig(ctx, wots_sig, msg, w_adrs)
    t_adrs = bytearray(adrs)
    _set_type_clear(t_adrs, _TREE)
    cur_idx = idx
    for k in range(hp):
        _set_height(t_adrs, k + 1)
        auth_k = auth[k * 16 : (k + 1) * 16]
        if (cur_idx & 1) == 0:
            cur_idx >>= 1
            _set_index(t_adrs, cur_idx)
            node = ctx.t_hash(t_adrs, node + auth_k)
        else:
            cur_idx >>= 1
            _set_index(t_adrs, cur_idx)
            node = ctx.t_hash(t_adrs, auth_k + node)
    return node


def _fors_sk_gen(
    ctx: _Sha2Ctx, sk_seed: bytes, adrs: bytearray, idx: int
) -> bytes:
    sk_adrs = bytearray(adrs)
    _set_type_clear(sk_adrs, _FORS_PRF)
    _set_kp(sk_adrs, _get_kp(adrs))
    _set_index(sk_adrs, idx)
    return ctx.t_hash(sk_adrs, sk_seed)


def _fors_sign_and_pk(
    ctx: _Sha2Ctx,
    md: bytes,
    sk_seed: bytes,
    p: _SlhParams,
    adrs: bytearray,
) -> tuple[bytes, bytes]:
    indices = _base_2b(md, p.a, p.k)
    sig_parts: list[bytes] = []
    roots: list[bytes] = []
    tree_size = 1 << p.a
    for i, idx_i in enumerate(indices):
        offset = i * tree_size
        sig_parts.append(_fors_sk_gen(ctx, sk_seed, adrs, offset + idx_i))
        leaves: list[bytes] = []
        node_adrs = bytearray(adrs)
        _set_height(node_adrs, 0)
        for j in range(tree_size):
            sk_j = _fors_sk_gen(ctx, sk_seed, adrs, offset + j)
            _set_index(node_adrs, offset + j)
            leaves.append(ctx.t_hash(node_adrs, sk_j))
        levels = [leaves]
        for z in range(1, p.a + 1):
            prev = levels[-1]
            _set_height(node_adrs, z)
            nxt: list[bytes] = []
            base_idx = offset >> z
            for j in range(len(prev) // 2):
                _set_index(node_adrs, base_idx + j)
                nxt.append(ctx.t_hash(node_adrs, prev[2 * j] + prev[2 * j + 1]))
            levels.append(nxt)
        for z in range(p.a):
            sig_parts.append(levels[z][(idx_i >> z) ^ 1])
        roots.append(levels[p.a][0])
    pk_adrs = bytearray(adrs)
    _set_type_clear(pk_adrs, _FORS_ROOTS)
    _set_kp(pk_adrs, _get_kp(adrs))
    return b"".join(sig_parts), ctx.t_hash(pk_adrs, b"".join(roots))


def _fors_pk_from_sig(
    ctx: _Sha2Ctx,
    sig_fors: bytes,
    md: bytes,
    p: _SlhParams,
    adrs: bytearray,
) -> bytes:
    indices = _base_2b(md, p.a, p.k)
    tree_size = 1 << p.a
    step = (1 + p.a) * 16
    roots: list[bytes] = []
    work_adrs = bytearray(adrs)
    for i, idx_i in enumerate(indices):
        chunk = sig_fors[i * step : (i + 1) * step]
        sk_i = chunk[:16]
        auth = chunk[16:]
        _set_height(work_adrs, 0)
        _set_index(work_adrs, i * tree_size + idx_i)
        node = ctx.t_hash(work_adrs, sk_i)
        tree_idx = i * tree_size + idx_i
        for z in range(p.a):
            _set_height(work_adrs, z + 1)
            auth_z = auth[z * 16 : (z + 1) * 16]
            if ((idx_i >> z) & 1) == 0:
                tree_idx >>= 1
                _set_index(work_adrs, tree_idx)
                node = ctx.t_hash(work_adrs, node + auth_z)
            else:
                tree_idx >>= 1
                _set_index(work_adrs, tree_idx)
                node = ctx.t_hash(work_adrs, auth_z + node)
        roots.append(node)
    pk_adrs = bytearray(adrs)
    _set_type_clear(pk_adrs, _FORS_ROOTS)
    _set_kp(pk_adrs, _get_kp(adrs))
    return ctx.t_hash(pk_adrs, b"".join(roots))


_PREHASH_SPECS: dict[str, tuple[str, str, int | None]] = {
    "SHA2-256": ("0609608648016503040201", "sha256", None),
    "SHA2-384": ("0609608648016503040202", "sha384", None),
    "SHA2-512": ("0609608648016503040203", "sha512", None),
    "SHA2-224": ("0609608648016503040204", "sha224", None),
    "SHA2-512/224": ("0609608648016503040205", "sha512_224", None),
    "SHA2-512/256": ("0609608648016503040206", "sha512_256", None),
    "SHA3-224": ("0609608648016503040207", "sha3_224", None),
    "SHA3-256": ("0609608648016503040208", "sha3_256", None),
    "SHA3-384": ("0609608648016503040209", "sha3_384", None),
    "SHA3-512": ("060960864801650304020a", "sha3_512", None),
    "SHAKE-128": ("060960864801650304020b", "shake_128", 32),
    "SHAKE-256": ("060960864801650304020c", "shake_256", 64),
}


def _encode_m_prime(
    msg: bytes,
    ctx_bytes: bytes,
    interface: Literal["external", "internal"],
    hash_alg: str | None,
) -> bytes:
    if interface == "internal":
        if hash_alg is not None:
            raise ValueError("preHash incompatible avec interface='internal'")
        return msg
    if interface != "external":
        raise ValueError(f"Interface FIPS 205 invalide : {interface!r}")
    if len(ctx_bytes) > 255:
        raise ValueError("Contexte FIPS 205 <= 255 octets")
    if hash_alg is None:
        return b"\x00" + bytes([len(ctx_bytes)]) + ctx_bytes + msg
    spec = _PREHASH_SPECS.get(hash_alg)
    if spec is None:
        raise ValueError(f"Algorithme preHash FIPS 205 inconnu : {hash_alg!r}")
    oid_hex, h_name, xof_len = spec
    h_obj = hashlib.new(h_name, msg)
    ph_m = h_obj.digest(xof_len) if xof_len is not None else h_obj.digest()
    return (
        b"\x01"
        + bytes([len(ctx_bytes)])
        + ctx_bytes
        + bytes.fromhex(oid_hex)
        + ph_m
    )


def _keygen_internal(
    p: _SlhParams, sk_seed: bytes, sk_prf: bytes, pk_seed: bytes
) -> tuple[bytes, bytes]:
    if len(sk_seed) != p.n or len(sk_prf) != p.n or len(pk_seed) != p.n:
        raise ValueError(f"Graines SLH-DSA invalides ({p.n} octets requis)")
    ctx = _Sha2Ctx(pk_seed)
    adrs = bytearray(32)
    _set_layer(adrs, p.d - 1)
    levels = _build_xmss_tree(ctx, sk_seed, p.hp, adrs)
    pk_root = levels[p.hp][0]
    pk = pk_seed + pk_root
    sk = sk_seed + sk_prf + pk
    return pk, sk


def _split_digest(
    digest: bytes, p: _SlhParams
) -> tuple[bytes, int, int]:
    ka_bytes = (p.k * p.a + 7) // 8
    ht_bits = p.h - p.hp
    ht_bytes = (ht_bits + 7) // 8
    leaf_bytes = (p.hp + 7) // 8
    md = digest[:ka_bytes]
    idx_tree = int.from_bytes(
        digest[ka_bytes : ka_bytes + ht_bytes], "big"
    ) & ((1 << ht_bits) - 1)
    idx_leaf = int.from_bytes(
        digest[ka_bytes + ht_bytes : ka_bytes + ht_bytes + leaf_bytes], "big"
    ) & ((1 << p.hp) - 1)
    return md, idx_tree, idx_leaf


def _sign_impl(
    p: _SlhParams,
    sk: bytes,
    msg: bytes,
    addr_rnd: bytes | None,
    ctx_bytes: bytes,
    interface: Literal["external", "internal"],
    hash_alg: str | None = None,
) -> bytes:
    if len(sk) != 64:
        raise ValueError("Cle privee SLH-DSA-128 invalide (64 octets requis)")
    if addr_rnd is not None and len(addr_rnd) != p.n:
        raise ValueError(f"addr_rnd SLH-DSA invalide ({p.n} octets requis)")
    m_prime = _encode_m_prime(msg, ctx_bytes, interface, hash_alg)
    sk_seed, sk_prf, pk_seed, pk_root = (
        sk[:16], sk[16:32], sk[32:48], sk[48:64]
    )
    ctx = _Sha2Ctx(pk_seed)
    opt_rand = pk_seed if addr_rnd is None else addr_rnd
    r = ctx.prf_msg(sk_prf, opt_rand, m_prime)
    digest = ctx.h_msg(r, pk_root, m_prime, p.m)
    md, idx_tree, idx_leaf = _split_digest(digest, p)

    fors_adrs = bytearray(32)
    _set_tree(fors_adrs, idx_tree)
    _set_type_clear(fors_adrs, _FORS_TREE)
    _set_kp(fors_adrs, idx_leaf)
    sig_fors, pk_fors = _fors_sign_and_pk(ctx, md, sk_seed, p, fors_adrs)

    ht_parts: list[bytes] = []
    cur_msg = pk_fors
    cur_tree, cur_leaf = idx_tree, idx_leaf
    leaf_mask = (1 << p.hp) - 1
    for layer in range(p.d):
        ht_adrs = bytearray(32)
        _set_layer(ht_adrs, layer)
        _set_tree(ht_adrs, cur_tree)
        sig_l, cur_msg = _xmss_sign_and_root(
            ctx, cur_msg, sk_seed, cur_leaf, p.hp, ht_adrs
        )
        ht_parts.append(sig_l)
        cur_leaf = cur_tree & leaf_mask
        cur_tree >>= p.hp
    return r + sig_fors + b"".join(ht_parts)


def _verify_impl(
    p: _SlhParams,
    pk: bytes,
    msg: bytes,
    sig: bytes,
    ctx_bytes: bytes,
    interface: Literal["external", "internal"],
    hash_alg: str | None = None,
) -> bool:
    if len(pk) != 32 or len(sig) != p.sig_bytes:
        return False
    try:
        m_prime = _encode_m_prime(msg, ctx_bytes, interface, hash_alg)
    except ValueError:
        return False
    pk_seed, pk_root = pk[:16], pk[16:32]
    ctx = _Sha2Ctx(pk_seed)
    r = sig[:16]
    fors_len = p.k * (1 + p.a) * 16
    sig_fors = sig[16 : 16 + fors_len]
    sig_ht = sig[16 + fors_len :]
    digest = ctx.h_msg(r, pk_root, m_prime, p.m)
    md, idx_tree, idx_leaf = _split_digest(digest, p)

    fors_adrs = bytearray(32)
    _set_tree(fors_adrs, idx_tree)
    _set_type_clear(fors_adrs, _FORS_TREE)
    _set_kp(fors_adrs, idx_leaf)
    cur_msg = _fors_pk_from_sig(ctx, sig_fors, md, p, fors_adrs)

    xmss_len = (35 + p.hp) * 16
    cur_tree, cur_leaf = idx_tree, idx_leaf
    leaf_mask = (1 << p.hp) - 1
    for layer in range(p.d):
        ht_adrs = bytearray(32)
        _set_layer(ht_adrs, layer)
        _set_tree(ht_adrs, cur_tree)
        sig_l = sig_ht[layer * xmss_len : (layer + 1) * xmss_len]
        cur_msg = _xmss_pk_from_sig(
            ctx, cur_leaf, sig_l, cur_msg, p.hp, ht_adrs
        )
        cur_leaf = cur_tree & leaf_mask
        cur_tree >>= p.hp
    return cur_msg == pk_root


def keygen_slh_dsa_sha2_128s(
    sk_seed: bytes, sk_prf: bytes, pk_seed: bytes
) -> tuple[bytes, bytes]:
    """Derive (pk, sk) SLH-DSA-SHA2-128s depuis les graines FIPS 205."""
    return _keygen_internal(_SHA2_128S, sk_seed, sk_prf, pk_seed)


def keygen_slh_dsa_sha2_128f(
    sk_seed: bytes, sk_prf: bytes, pk_seed: bytes
) -> tuple[bytes, bytes]:
    """Derive (pk, sk) SLH-DSA-SHA2-128f depuis les graines FIPS 205."""
    return _keygen_internal(_SHA2_128F, sk_seed, sk_prf, pk_seed)


def sign_slh_dsa_sha2_128s(
    sk: bytes,
    msg: bytes,
    addr_rnd: bytes | None = None,
    ctx: bytes = b"",
    interface: Literal["external", "internal"] = "external",
    hash_alg: str | None = None,
) -> bytes:
    """Signe msg avec SLH-DSA-SHA2-128s (pure ou preHash, det. ou hedged)."""
    return _sign_impl(_SHA2_128S, sk, msg, addr_rnd, ctx, interface, hash_alg)


def sign_slh_dsa_sha2_128f(
    sk: bytes,
    msg: bytes,
    addr_rnd: bytes | None = None,
    ctx: bytes = b"",
    interface: Literal["external", "internal"] = "external",
    hash_alg: str | None = None,
) -> bytes:
    """Signe msg avec SLH-DSA-SHA2-128f (pure ou preHash, det. ou hedged)."""
    return _sign_impl(_SHA2_128F, sk, msg, addr_rnd, ctx, interface, hash_alg)


def verify_slh_dsa_sha2_128s(
    pk: bytes,
    msg: bytes,
    sig: bytes,
    ctx: bytes = b"",
    interface: Literal["external", "internal"] = "external",
    hash_alg: str | None = None,
) -> bool:
    """Verifie une signature FIPS 205 SLH-DSA-SHA2-128s."""
    return _verify_impl(_SHA2_128S, pk, msg, sig, ctx, interface, hash_alg)


def verify_slh_dsa_sha2_128f(
    pk: bytes,
    msg: bytes,
    sig: bytes,
    ctx: bytes = b"",
    interface: Literal["external", "internal"] = "external",
    hash_alg: str | None = None,
) -> bool:
    """Verifie une signature FIPS 205 SLH-DSA-SHA2-128f."""
    return _verify_impl(_SHA2_128F, pk, msg, sig, ctx, interface, hash_alg)
