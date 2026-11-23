# SPDX-License-Identifier: MIT
"""Canonisation deterministe RFC 8785 (JSON Canonicalization Scheme)."""

from __future__ import annotations

import hashlib
import math
from typing import Any

_MAX_SAFE_INT = (1 << 53) - 1


class JcsError(ValueError):
    """Erreur levee sur NaN, Infinity, entier hors IEEE-754 ou cle non-str."""


def _format_ecmascript_float(num: float) -> str:
    if math.isnan(num) or math.isinf(num):
        raise JcsError(f"Nombre IEEE-754 non fini interdit : {num!r}")
    if num == 0.0:
        return "0"
    neg = num < 0.0
    if neg:
        num = -num
    rep = repr(num)
    if "e" in rep:
        mant, exp_s = rep.split("e")
        exp = int(exp_s)
    else:
        mant, exp = rep, 0
    if "." in mant:
        int_p, frac_p = mant.split(".")
        digits = int_p + frac_p
        n = len(int_p) + exp
    else:
        digits = mant
        n = len(mant) + exp
    stripped = digits.lstrip("0")
    n -= len(digits) - len(stripped)
    digits = stripped.rstrip("0")
    k = len(digits)
    if k <= n <= 21:
        res = digits + ("0" * (n - k))
    elif 0 < n <= 21:
        res = f"{digits[:n]}.{digits[n:]}"
    elif -6 < n <= 0:
        res = f"0.{'0' * (-n)}{digits}"
    elif k == 1:
        sign = "+" if n - 1 >= 0 else "-"
        res = f"{digits}e{sign}{abs(n - 1)}"
    else:
        sign = "+" if n - 1 >= 0 else "-"
        res = f"{digits[0]}.{digits[1:]}e{sign}{abs(n - 1)}"
    return f"-{res}" if neg else res


def _escape_jcs_string(text: str) -> str:
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise JcsError(f"Chaine UTF-8 invalide : {exc}") from exc
    parts = ['"']
    for ch in text:
        code = ord(ch)
        if ch == '"':
            parts.append('\\"')
        elif ch == "\\":
            parts.append("\\\\")
        elif code == 0x08:
            parts.append("\\b")
        elif code == 0x0C:
            parts.append("\\f")
        elif code == 0x0A:
            parts.append("\\n")
        elif code == 0x0D:
            parts.append("\\r")
        elif code == 0x09:
            parts.append("\\t")
        elif code < 0x20:
            parts.append(f"\\u{code:04x}")
        else:
            parts.append(ch)
    parts.append('"')
    return "".join(parts)


def _serialize_jcs(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        if value < -_MAX_SAFE_INT or value > _MAX_SAFE_INT:
            raise JcsError(f"Entier hors plage IEEE-754 : {value}")
        return str(value)
    if isinstance(value, float):
        return _format_ecmascript_float(value)
    if isinstance(value, str):
        return _escape_jcs_string(value)
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(_serialize_jcs(item) for item in value) + "]"
    if isinstance(value, dict):
        keyed: list[tuple[bytes, str, Any]] = []
        for k, v in value.items():
            if not isinstance(k, str):
                raise JcsError(f"Cle d'objet non-str interdite : {k!r}")
            try:
                sort_key = k.encode("utf-16-be")
            except UnicodeEncodeError as exc:
                raise JcsError(f"Cle UTF-16 invalide : {exc}") from exc
            keyed.append((sort_key, k, v))
        keyed.sort(key=lambda item: item[0])
        entries = [
            f"{_escape_jcs_string(k)}:{_serialize_jcs(v)}"
            for _, k, v in keyed
        ]
        return "{" + ",".join(entries) + "}"
    raise JcsError(f"Type JSON non supporte par JCS : {type(value).__name__}")


def canonicalize_jcs(value: Any) -> bytes:
    """Serialise value en JSON canonique UTF-8 selon RFC 8785."""
    return _serialize_jcs(value).encode("utf-8")


def jcs_sha256_hex(value: Any) -> str:
    """Retourne le condensat SHA-256 hex minuscules de canonicalize_jcs."""
    return hashlib.sha256(canonicalize_jcs(value)).hexdigest()
