# SPDX-License-Identifier: MIT
"""Propagation de contamination CaMeL / Can CaMeLs Talk? (EXIG-SEC-06)."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class TaintLevel(StrEnum):
    """Niveaux de contamination d'une source ou sortie d'outil."""

    TRUSTED = "TRUSTED"
    UNTRUSTED_EXTERNAL = "UNTRUSTED_EXTERNAL"
    PII_RESTRICTED = "PII_RESTRICTED"


@dataclass
class SessionTaintTracker:
    """Etat de contamination de session isole par locataire."""

    consumed_untrusted: bool = False
    tainted_sources: list[str] = field(default_factory=list)
    provenance_hops: list[str] = field(default_factory=list)
    tenant_id: str = "default"


def record_tool_output(
    tracker: SessionTaintTracker, source_id: str, taint: TaintLevel
) -> SessionTaintTracker:
    """Enregistre une sortie d'outil et marque consumed_untrusted si requis."""
    if not isinstance(source_id, str) or not source_id.strip():
        raise ValueError("source_id non vide requis")
    level = TaintLevel(taint)
    sources = list(tracker.tainted_sources)
    consumed = tracker.consumed_untrusted
    if level in (TaintLevel.UNTRUSTED_EXTERNAL, TaintLevel.PII_RESTRICTED):
        consumed = True
        if source_id not in sources:
            sources.append(source_id)
    return SessionTaintTracker(
        consumed_untrusted=consumed,
        tainted_sources=sources,
        provenance_hops=list(tracker.provenance_hops),
        tenant_id=tracker.tenant_id,
    )


def delegate_taint_envelope(
    parent: SessionTaintTracker, child_agent_id: str
) -> SessionTaintTracker:
    """Propage obligatoirement consumed_untrusted a tout agent aval."""
    if not isinstance(child_agent_id, str) or not child_agent_id.strip():
        raise ValueError("child_agent_id non vide requis")
    return SessionTaintTracker(
        consumed_untrusted=parent.consumed_untrusted,
        tainted_sources=list(parent.tainted_sources),
        provenance_hops=[*parent.provenance_hops, child_agent_id],
        tenant_id=parent.tenant_id,
    )
