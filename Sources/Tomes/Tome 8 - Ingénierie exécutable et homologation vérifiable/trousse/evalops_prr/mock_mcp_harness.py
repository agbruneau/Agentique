# SPDX-License-Identifier: MIT
"""Banc EvalOps hermetique : serveur Mock MCP deterministe et pass^k."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
import copy
from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Literal


@dataclass(frozen=True, slots=True)
class TrajectoryVerdict:
    """Resultat d'evaluation deterministe d'une trajectoire d'outils."""

    passed: bool
    observed_tools: tuple[str, ...]
    total_cost_cad: Decimal
    errors: tuple[str, ...]


class MockMcpServer:
    """Doublure deterministe hors reseau pour tools/list et tools/call."""

    def __init__(
        self,
        tools: list[dict[str, Any]],
        scripted_responses: Mapping[
            str,
            list[dict[str, Any]] | Callable[[dict[str, Any]], dict[str, Any]],
        ]
        | None = None,
        seed: int = 20261202,
    ) -> None:
        self._tools = sorted(
            copy.deepcopy(tools), key=lambda t: str(t.get("name", ""))
        )
        self._tool_names = {str(t.get("name", "")) for t in self._tools}
        self._scripted = dict(scripted_responses or {})
        self._call_counts: dict[str, int] = {}
        self.seed = seed
        self._trajectory: list[dict[str, Any]] = []

    def tools_list(self) -> list[dict[str, Any]]:
        """Retourne les definitions MCP du serveur simule."""
        return copy.deepcopy(self._tools)

    def tools_call(
        self,
        tool_name: str,
        arguments: dict[str, Any],
        cost_cad: Decimal = Decimal("0.00"),
    ) -> dict[str, Any]:
        """Simule un appel d'outil et enregistre (tool, args, result, cost)."""
        if tool_name not in self._tool_names:
            raise ValueError(f"Outil MCP inconnu : {tool_name}")
        if isinstance(cost_cad, float):
            raise TypeError("IEEE-754 float interdit pour cost_cad")
        idx = self._call_counts.get(tool_name, 0)
        self._call_counts[tool_name] = idx + 1
        handler = self._scripted.get(tool_name)
        if callable(handler):
            result = copy.deepcopy(handler(copy.deepcopy(arguments)))
        elif isinstance(handler, list) and handler:
            result = copy.deepcopy(handler[idx % len(handler)])
        else:
            result = {"status": "ok"}
        self._trajectory.append(
            {
                "tool_name": tool_name,
                "arguments": copy.deepcopy(arguments),
                "result": copy.deepcopy(result),
                "cost_cad": Decimal(str(cost_cad)),
            }
        )
        return result

    @property
    def trajectory(self) -> list[dict[str, Any]]:
        """Retourne la trajectoire enregistree."""
        return copy.deepcopy(self._trajectory)


def compute_pass_k(
    trial_outcomes: Sequence[bool],
    k: int,
    *,
    metric_mode: Literal["pass_pow_k", "pass_at_k"] = "pass_pow_k",
) -> float:
    """Calcule la constance pass^k (rejette pass@k par ValueError)."""
    if metric_mode != "pass_pow_k":
        raise ValueError(
            "Metrique pass@k interdite comme porte bloquante; exigez pass^k"
        )
    if type(k) is not int or k < 3:
        raise ValueError(f"k doit etre un entier >= 3 pour pass^k (recu k={k})")
    if not trial_outcomes:
        raise ValueError("trial_outcomes ne doit pas etre vide")
    if not all(isinstance(ok, bool) for ok in trial_outcomes):
        raise TypeError("trial_outcomes doit contenir uniquement des bool")
    success_rate = sum(1 for ok in trial_outcomes if ok) / len(trial_outcomes)
    return float(success_rate**k)


def evaluate_trajectory(
    expected_tools: list[str],
    observed_calls: list[dict[str, Any]],
    max_cost_cad: Decimal,
) -> TrajectoryVerdict:
    """Verifie ordre des outils, ancrage des arguments et plafond CAD."""
    if isinstance(max_cost_cad, (float, bool)) or not max_cost_cad.is_finite():
        raise TypeError("max_cost_cad doit etre un Decimal fini")
    observed_tools = tuple(
        str(call.get("tool_name", "")) for call in observed_calls
    )
    total_cost = Decimal("0.00")
    for call in observed_calls:
        raw_cost = call.get("cost_cad", "0")
        if isinstance(raw_cost, (float, bool)):
            raise TypeError("IEEE-754 float/bool interdit pour cost_cad")
        cost = Decimal(str(raw_cost))
        if not cost.is_finite() or cost < 0:
            raise ValueError(f"Cout invalide dans trajectoire : {raw_cost!r}")
        total_cost += cost
    errors: list[str] = []
    if list(observed_tools) != expected_tools:
        errors.append(
            f"Trajectoire divergente : {list(observed_tools)} "
            f"!= {expected_tools}"
        )
    if total_cost > max_cost_cad:
        errors.append(
            f"Plafond budgetaire depasse : {total_cost} > {max_cost_cad}"
        )
    return TrajectoryVerdict(
        passed=len(errors) == 0,
        observed_tools=observed_tools,
        total_cost_cad=total_cost,
        errors=tuple(errors),
    )
