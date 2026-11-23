# SPDX-License-Identifier: MIT
"""Automate de revocation SSF/CAEP et brouillon agent-revocation-01."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Literal


class AgentAuthState(StrEnum):
    """Etats deterministes d'autorisation d'une identite NHI."""

    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    REVOKED = "REVOKED"


@dataclass(frozen=True, slots=True)
class CaepRevocationEvent:
    """Evenement de suspension, rehabilitation ou revocation SOC/CAEP."""

    event_id: str
    spec_source: Literal[
        "SSF_CAEP_FINAL",
        "IETF_INDIVIDUAL_DRAFT_AGENT_REVOCATION_01",
    ]
    subject_spiffe: str
    jti: str | None
    issued_at: int
    reason: str
    action: Literal["SUSPEND", "REINSTATE", "REVOKE"] = "REVOKE"


class RevocationStateMachine:
    """Automate deterministe ACTIVE <-> SUSPENDED -> REVOKED (terminal)."""

    def __init__(self) -> None:
        self._states: dict[str, AgentAuthState] = {}
        self._revoked_jtis: set[str] = set()
        self._events: list[CaepRevocationEvent] = []

    def get_state(self, subject_spiffe: str) -> AgentAuthState:
        """Retourne l'etat courant d'un sujet SPIFFE."""
        return self._states.get(subject_spiffe, AgentAuthState.ACTIVE)

    def apply_event(self, event: CaepRevocationEvent) -> AgentAuthState:
        """Applique une transition (REVOKED est strictement terminal)."""
        self._events.append(event)
        current = self.get_state(event.subject_spiffe)
        if current == AgentAuthState.REVOKED:
            return AgentAuthState.REVOKED
        if event.action == "REVOKE":
            self._states[event.subject_spiffe] = AgentAuthState.REVOKED
            if event.jti:
                self._revoked_jtis.add(event.jti)
        elif event.action == "SUSPEND":
            self._states[event.subject_spiffe] = AgentAuthState.SUSPENDED
        elif event.action == "REINSTATE":
            self._states[event.subject_spiffe] = AgentAuthState.ACTIVE
        return self.get_state(event.subject_spiffe)

    def assert_active(
        self, subject_spiffe: str, jti: str, now_ts: int
    ) -> bool:
        """Retourne True uniquement si le sujet et le jti sont actifs."""
        _ = now_ts
        if not subject_spiffe or not jti:
            return False
        if self.get_state(subject_spiffe) != AgentAuthState.ACTIVE:
            return False
        return jti not in self._revoked_jtis
