# SPDX-License-Identifier: MIT
"""Arithmetique financiere exacte Decimal (rejet strict IEEE-754 float)."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_EVEN, Decimal, InvalidOperation

ALLOWED_CURRENCIES: frozenset[str] = frozenset({"CAD", "USD", "EUR"})


@dataclass(frozen=True, slots=True)
class MoneyAmount:
    """Montant financier entier exact en centimes."""

    cents: int
    currency: str = "CAD"


def from_decimal_str(
    raw: str | Decimal | int, currency: str = "CAD"
) -> MoneyAmount:
    """Rejette float par TypeError et convertit (ROUND_HALF_EVEN)."""
    if isinstance(raw, float):
        raise TypeError("IEEE-754 float interdit pour les montants financiers")
    if isinstance(raw, bool):
        raise TypeError("bool interdit pour les montants financiers")
    if currency not in ALLOWED_CURRENCIES:
        raise ValueError(f"Devise non autorisee : {currency!r}")
    try:
        dec = raw if isinstance(raw, Decimal) else Decimal(str(raw))
    except InvalidOperation as exc:
        raise ValueError(f"Montant decimal invalide : {raw!r}") from exc
    if not dec.is_finite():
        raise ValueError(f"Montant non fini interdit : {raw!r}")
    cents = int(
        (dec * Decimal("100")).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)
    )
    return MoneyAmount(cents=cents, currency=currency)
