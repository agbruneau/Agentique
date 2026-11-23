# SPDX-License-Identifier: MIT
"""Mappage OTel v1.41.0 <-> genai_dev (85 attr.) et caviardage PII FR/EN."""

from __future__ import annotations

from collections.abc import Mapping
import hashlib
import hmac
import re
from typing import Any, Literal

GENAI_DEV_85_ATTRS: tuple[str, ...] = (
    "gen_ai.agent.description",
    "gen_ai.agent.id",
    "gen_ai.agent.name",
    "gen_ai.agent.version",
    "gen_ai.conversation.compacted",
    "gen_ai.conversation.id",
    "gen_ai.data_source.id",
    "gen_ai.embeddings.dimension.count",
    "gen_ai.evaluation.explanation",
    "gen_ai.evaluation.name",
    "gen_ai.evaluation.score.label",
    "gen_ai.evaluation.score.value",
    "gen_ai.input.messages",
    "gen_ai.input.messages_ref",
    "gen_ai.main_agent.description",
    "gen_ai.main_agent.id",
    "gen_ai.main_agent.name",
    "gen_ai.memory.query.text",
    "gen_ai.memory.record.count",
    "gen_ai.memory.record.id",
    "gen_ai.memory.records",
    "gen_ai.memory.store.id",
    "gen_ai.operation.name",
    "gen_ai.output.messages",
    "gen_ai.output.messages_ref",
    "gen_ai.output.type",
    "gen_ai.prompt.name",
    "gen_ai.prompt.variable",
    "gen_ai.prompt.version",
    "gen_ai.provider.name",
    "gen_ai.request.choice.count",
    "gen_ai.request.encoding_formats",
    "gen_ai.request.frequency_penalty",
    "gen_ai.request.max_tokens",
    "gen_ai.request.model",
    "gen_ai.request.presence_penalty",
    "gen_ai.request.previous_response.id",
    "gen_ai.request.reasoning.level",
    "gen_ai.request.seed",
    "gen_ai.request.stop_sequences",
    "gen_ai.request.stream",
    "gen_ai.request.stream_cursor",
    "gen_ai.request.temperature",
    "gen_ai.request.top_k",
    "gen_ai.request.top_p",
    "gen_ai.response.finish_reasons",
    "gen_ai.response.id",
    "gen_ai.response.model",
    "gen_ai.response.status",
    "gen_ai.response.time_to_first_chunk",
    "gen_ai.retrieval.documents",
    "gen_ai.retrieval.query.text",
    "gen_ai.retrieval.top_k",
    "gen_ai.skill.description",
    "gen_ai.skill.name",
    "gen_ai.skill.resource.name",
    "gen_ai.skill.source.uri",
    "gen_ai.system_instructions",
    "gen_ai.system_instructions_ref",
    "gen_ai.token.modality",
    "gen_ai.tool.call.arguments",
    "gen_ai.tool.call.id",
    "gen_ai.tool.call.result",
    "gen_ai.tool.definitions",
    "gen_ai.tool.definitions_ref",
    "gen_ai.tool.description",
    "gen_ai.tool.name",
    "gen_ai.tool.type",
    "gen_ai.transfer.mode",
    "gen_ai.transfer.target.name",
    "gen_ai.usage.audio.cache_read.input_tokens",
    "gen_ai.usage.audio.input_tokens",
    "gen_ai.usage.audio.output_tokens",
    "gen_ai.usage.cache_read.input_tokens",
    "gen_ai.usage.cache_write.input_tokens",
    "gen_ai.usage.image.cache_read.input_tokens",
    "gen_ai.usage.image.input_tokens",
    "gen_ai.usage.image.output_tokens",
    "gen_ai.usage.input_tokens",
    "gen_ai.usage.output_tokens",
    "gen_ai.usage.reasoning.output_tokens",
    "gen_ai.usage.text.cache_read.input_tokens",
    "gen_ai.usage.text.input_tokens",
    "gen_ai.usage.text.output_tokens",
    "gen_ai.workflow.name",
)

FORBIDDEN_RAW_CONTENT_ATTRS: frozenset[str] = frozenset(
    {
        "gen_ai.input.messages",
        "gen_ai.output.messages",
        "gen_ai.system_instructions",
        "gen_ai.tool.call.arguments",
        "gen_ai.tool.call.result",
        "gen_ai.memory.records",
        "gen_ai.memory.query.text",
        "gen_ai.retrieval.documents",
        "gen_ai.retrieval.query.text",
    }
)

REQUIRED_MANDATE_JOIN_ATTRS: frozenset[str] = frozenset(
    {
        "ca.entreprise.task_id",
        "ca.entreprise.autonomy_level",
        "ca.entreprise.approval.jti",
        "ca.entreprise.cost_center",
    }
)

OTEL_V141_TO_GENAI_DEV_MAP: dict[str, str] = {
    "gen_ai.usage.cache_creation.input_tokens": (
        "gen_ai.usage.cache_write.input_tokens"
    ),
    "gen_ai.client.token.usage": (
        "gen_ai.client.inference.usage.input_tokens"
    ),
    "gen_ai.system": "gen_ai.provider.name",
    "gen_ai.token.type": "gen_ai.token.modality",
    "gen_ai.usage.prompt_tokens": "gen_ai.usage.input_tokens",
    "gen_ai.usage.completion_tokens": "gen_ai.usage.output_tokens",
}

_GENAI_DEV_TO_V141_MAP: dict[str, str] = {
    v: k for k, v in OTEL_V141_TO_GENAI_DEV_MAP.items()
}

DEFAULT_ALLOWED_ATTRS: frozenset[str] = (
    frozenset(GENAI_DEV_85_ATTRS) - FORBIDDEN_RAW_CONTENT_ATTRS
) | REQUIRED_MANDATE_JOIN_ATTRS | frozenset(
    {"mcp.method.name", "gen_ai.client.inference.usage.input_tokens"}
)

_PII_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "BEARER_JWT",
        re.compile(
            r"\bbearer\s+[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*[A-Za-z0-9_-]",
            re.IGNORECASE,
        ),
    ),
    ("IBAN", re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b")),
    ("PAYMENT_CARD", re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b")),
    (
        "EMAIL",
        re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    ),
    ("RAMQ", re.compile(r"\b[A-Z]{4}\s?\d{4}\s?\d{4}\b")),
    (
        "PHONE",
        re.compile(
            r"(?<!\d)(?:\+\d{1,3}[-\s.](?:\(\d{1,4}\)|\d{1,3})"
            r"(?:[-\s.]\d{2,4}){2,4}"
            r"|(?:\(\d{3}\)|\d{3})[-\s.]\d{3}[-\s.]\d{4}"
            r"|0\d(?:[-\s.]\d{2}){4})(?!\d)"
        ),
    ),
    ("NAS_SIN", re.compile(r"\b\d{3}[-\s]?\d{3}[-\s]?\d{3}\b")),
)

_JOIN_KEYS = REQUIRED_MANDATE_JOIN_ATTRS
_RAW_BAN = FORBIDDEN_RAW_CONTENT_ATTRS
_APPROVER_KEYS = ("approver", "approbateur")


class OtelGenAiMapper:
    """Adaptateur versionne pour fenetre de transition OTel GenAI."""

    def __init__(
        self,
        mapping: Mapping[str, str] | None = None,
        allowlist: frozenset[str] = DEFAULT_ALLOWED_ATTRS,
    ) -> None:
        self.mapping = dict(mapping or OTEL_V141_TO_GENAI_DEV_MAP)
        self.allowlist = allowlist

    def map_attributes(
        self,
        raw_attrs: Mapping[str, Any],
        target_dialect: Literal["v1.41.0", "genai_dev"] = "genai_dev",
    ) -> dict[str, Any]:
        """Convertit les attributs en appliquant l'allowlist fermee."""
        return _map_with_table(
            raw_attrs, target_dialect, self.allowlist, self.mapping
        )


def _map_with_table(
    raw_attrs: Mapping[str, Any],
    target_dialect: Literal["v1.41.0", "genai_dev"],
    allowlist: frozenset[str],
    fwd_map: Mapping[str, str],
) -> dict[str, Any]:
    if target_dialect not in ("v1.41.0", "genai_dev"):
        raise ValueError(f"Dialecte OTel invalide : {target_dialect!r}")
    for key in raw_attrs:
        if key.startswith(("enterprise.", "otel.")):
            raise ValueError(f"Prefixe interdit EXIG-OBS-06 : {key}")
    missing = [
        req for req in _JOIN_KEYS if not str(raw_attrs.get(req) or "").strip()
    ]
    if missing:
        raise ValueError(f"Cles de jointure lacune 21 absentes : {missing}")
    rev_map = {v: k for k, v in fwd_map.items()}
    out: dict[str, Any] = {}
    for key, val in raw_attrs.items():
        if key in _RAW_BAN or any(t in key.lower() for t in _APPROVER_KEYS):
            continue
        canon_k = fwd_map.get(key, key)
        mapped_k = canon_k if target_dialect == "genai_dev" else rev_map.get(
            key, key
        )
        if (
            (mapped_k in allowlist or canon_k in allowlist)
            and canon_k not in _RAW_BAN
            and mapped_k not in _RAW_BAN
        ):
            out[mapped_k] = val
    return out


# CA-G0-SYNC-BEGIN:G0-EX-CH02-04
def map_span_attributes(
    raw_attrs: Mapping[str, Any],
    target_dialect: Literal["v1.41.0", "genai_dev"] = "genai_dev",
    allowlist: frozenset[str] = DEFAULT_ALLOWED_ATTRS,
) -> dict[str, Any]:
    """Applique liste fermee, purge brut (OBS-07) et jointure mandat."""
    if any(k.startswith(("enterprise.", "otel.")) for k in raw_attrs):
        raise ValueError("Prefixe interdit EXIG-OBS-06")
    if any(not str(raw_attrs.get(r) or "").strip() for r in _JOIN_KEYS):
        raise ValueError("Cles de jointure trace <-> mandat manquantes")
    out, fwd, rev = {}, OTEL_V141_TO_GENAI_DEV_MAP, _GENAI_DEV_TO_V141_MAP
    for k, val in raw_attrs.items():
        if k in _RAW_BAN or any(t in k.lower() for t in _APPROVER_KEYS):
            continue
        ck = fwd.get(k, k)
        mk = ck if target_dialect == "genai_dev" else rev.get(k, k)
        if (mk in allowlist or ck in allowlist) and ck not in _RAW_BAN:
            out[mk] = val
    return out

def redact_pii_bilingual(text: str, hmac_key: bytes) -> tuple[str, list[str]]:
    """Caviarde PII FR/EN par jeton HMAC-SHA256 tronque."""
    redacted, cats = text, []
    for cat, pattern in _PII_PATTERNS:
        def _repl(m: re.Match[str], c: str = cat) -> str:
            if c not in cats:
                cats.append(c)
            dig = hmac.new(hmac_key, m.group(0).encode(), hashlib.sha256)
            return f"[{c}:{dig.hexdigest()[:12]}]"
        redacted = pattern.sub(_repl, redacted)
    return redacted, cats
# CA-G0-SYNC-END:G0-EX-CH02-04
