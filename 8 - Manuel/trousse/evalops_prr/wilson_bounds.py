# SPDX-License-Identifier: MIT
"""Dimensionnement statistique Wilson 95 % < p (>= 3/p essais, EXIG-EVA-03)."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
import math

# FACT-WILSON-3P (faits-empiriques.json): a 0 echec, n = ceil(3/p) = 300
# pour p = 0.01 donne une borne unilaterale a 95 % de 0.8938 % < 1 %
# (contre 1.2643 % en intervalle bilateral z = 1.959964).
Z_95_ONE_SIDED: float = 1.6448536269514722
Z_95_TWO_SIDED: float = 1.959963984540054


@dataclass(frozen=True, slots=True)
class WilsonVerdict:
    """Verdict statistique de porte EvalOps selon EXIG-EVA-03."""

    successes: int
    n_independent: int
    target_max_failure_p: float
    wilson_failure_upper_95: float
    min_required_trials: int
    passes_gate: bool
    reason: str


def _bad_wilson_seq(
    outs: Sequence[bool], scns: Sequence[str], p_tgt: float
) -> bool:
    return (
        not (0.0 < p_tgt <= 1.0)
        or not outs
        or len(outs) != len(scns)
        or any(type(x) is not bool for x in outs)
        or any(not isinstance(s, str) or not s.strip() for s in scns)
    )


# CA-G0-SYNC-BEGIN:G0-EX-CH04-01
def wilson_failure_upper_bound(
    failures: int, n: int, z: float = Z_95_ONE_SIDED
) -> float:
    """Borne superieure de Wilson a 95 % du taux d'echec f/n."""
    if (type(failures) is not int or type(n) is not int or n <= 0
            or failures < 0 or failures > n
            or not math.isfinite(z) or z <= 0):
        raise ValueError("Parametres Wilson invalides")
    p_hat, z2 = failures / n, z * z
    rad = z * math.sqrt((p_hat * (1.0 - p_hat)) / n + z2 / (4.0 * n * n))
    return min(1.0, (p_hat + z2 / (2.0 * n) + rad) / (1.0 + z2 / n))

def evaluate_wilson_gate(
    independent_outcomes: Sequence[bool],
    scenario_ids: Sequence[str], target_max_failure_p: float,
) -> WilsonVerdict:
    """Exige scenarios distincts, n >= ceil(3/p) et Wilson 95 % < p."""
    outs, p_tgt = independent_outcomes, target_max_failure_p
    if _bad_wilson_seq(outs, scenario_ids, p_tgt):
        raise ValueError("Parametres Wilson ou listes invalides")
    if len(set(scenario_ids)) != len(outs):
        raise ValueError("Repetitions non independantes interdites")
    n, succ = len(outs), sum(1 for x in outs if x)
    ub = wilson_failure_upper_bound(n - succ, n, z=Z_95_ONE_SIDED)
    min_req = math.ceil(3.0 / p_tgt)
    ok = (n >= min_req) and (ub < p_tgt)
    why = "PASS" if ok else f"n={n}<{min_req} ou ub={ub:.6f}"
    return WilsonVerdict(succ, n, p_tgt, ub, min_req, ok, why)
# CA-G0-SYNC-END:G0-EX-CH04-01
