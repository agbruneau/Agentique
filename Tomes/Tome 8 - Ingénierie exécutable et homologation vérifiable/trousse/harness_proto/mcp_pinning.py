# SPDX-License-Identifier: MIT
"""Mediation protocolaire MCP 2026-07-28, epinglage JCS et Streamable HTTP."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
import copy
from dataclasses import dataclass, field
import re
from typing import Any, Literal, Protocol

from harness_proto.jcs import jcs_sha256_hex

_MCP_REV = "2026-07-28"
_PROTO_META_KEY = "io.modelcontextprotocol/protocolVersion"
_IDENT_PART_RE = re.compile(
    r"[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|[^a-zA-Z]|$)|[0-9]+"
)
_SENSITIVE_HEADER_TOKENS = frozenset(
    {
        "token", "secret", "password", "passwd", "auth", "authorization",
        "bearer", "nas", "sin", "ssn", "ramq", "iban", "card", "carte",
        "pii", "cookie", "jwt", "apikey", "credential", "credentials",
        "private",
    }
)


class HeaderMismatchError(Exception):
    """Erreur levee sur divergence entre en-tetes MCP et corps JSON-RPC."""

    def __init__(
        self,
        detail: str,
        http_status: int = 400,
        jsonrpc_code: int = -32020,
    ) -> None:
        super().__init__(detail)
        self.detail = detail
        self.http_status = http_status
        self.jsonrpc_code = jsonrpc_code


class DeprecatedTransportError(ValueError):
    """Refus explicite du transport deprecie HTTP+SSE (SEP-2596)."""


@dataclass(frozen=True, slots=True)
class McpCatalogEntry:
    """Entree de gouvernance au catalogue d'entreprise pour un outil MCP."""

    ref: str
    server_id: str
    tool_name: str
    contract_version: str
    definition_digest: str
    mcp_revision: str = "2026-07-28"
    tier: Literal["P0", "P1", "P2", "P3"] = "P0"
    allowed_header_projections: frozenset[str] = field(
        default_factory=frozenset
    )
    volatile_meta_keys: frozenset[str] = field(default_factory=frozenset)
    allowed_meta_keys: frozenset[str] = field(default_factory=frozenset)


@dataclass(frozen=True, slots=True)
class McpSyncResult:
    """Resultat de verification tools/list contre le catalogue epingle."""

    active_tools: dict[str, dict[str, Any]]
    suspended_tools: tuple[str, ...]
    server_suspended: bool
    drift_reasons: dict[str, str]


def _has_sensitive_token(prop_name: str, hdr: str) -> bool:
    tokens = {
        tok.lower()
        for part in (prop_name, hdr)
        for tok in _IDENT_PART_RE.findall(part)
    }
    return bool(tokens & _SENSITIVE_HEADER_TOKENS)


def _check_input_schema_headers(
    schema_node: Any,
    entry: McpCatalogEntry | None,
    proj_map: dict[str, str] | None = None,
) -> None:
    if isinstance(schema_node, list):
        for item in schema_node:
            _check_input_schema_headers(item, entry, proj_map)
        return
    if not isinstance(schema_node, dict):
        return
    props = schema_node.get("properties")
    if isinstance(props, dict):
        allowed = (
            {h.lower() for h in entry.allowed_header_projections}
            if entry is not None
            else None
        )
        for prop_name, prop_def in props.items():
            if not isinstance(prop_def, dict):
                continue
            if "x-mcp-header" in prop_def:
                hdr = prop_def.get("x-mcp-header")
                if not isinstance(hdr, str) or not hdr.strip():
                    raise ValueError(
                        f"x-mcp-header invalide sur {prop_name}"
                    )
                if _has_sensitive_token(prop_name, hdr):
                    raise ValueError(
                        f"x-mcp-header interdit sur secret/PII ({prop_name})"
                    )
                if allowed is not None and hdr.lower() not in allowed:
                    raise ValueError(
                        f"Projection x-mcp-header non autorisee : {hdr}"
                    )
                if proj_map is not None:
                    proj_map[hdr.lower()] = prop_name
            _check_input_schema_headers(prop_def, entry, proj_map)
    for k, val in schema_node.items():
        if k != "properties" and isinstance(val, (dict, list)):
            _check_input_schema_headers(val, entry, proj_map)


def _normalize_headers(headers: Mapping[str, str]) -> dict[str, str]:
    hdr: dict[str, str] = {}
    for k, v in headers.items():
        lk = k.lower()
        if lk in hdr and hdr[lk] != v:
            raise HeaderMismatchError(f"En-tete duplique divergent : {k}")
        hdr[lk] = v
    return hdr


def _purge_and_validate(
    headers: Mapping[str, str],
    body: dict[str, Any],
    entry: McpCatalogEntry | None,
) -> dict[str, Any]:
    params = body.get("params") if isinstance(body.get("params"), dict) else {}
    proj_map: dict[str, str] = {}
    _check_input_schema_headers(params.get("inputSchema"), entry, proj_map)
    _check_input_schema_headers(body.get("inputSchema"), entry, proj_map)
    args = params.get("arguments")
    arg_map = args if isinstance(args, dict) else {}
    arg_vals = {str(v) for v in arg_map.values()}
    allowed_proj = (
        {p.lower() for p in entry.allowed_header_projections}
        if entry is not None
        else None
    )
    for hk, hv in headers.items():
        if hk.lower().startswith("mcp-param-"):
            proj = hk[len("mcp-param-") :]
            if allowed_proj is not None and proj.lower() not in allowed_proj:
                raise HeaderMismatchError(f"Projection non permise : {hk}")
            mapped_prop = proj_map.get(proj.lower())
            if mapped_prop is not None:
                if (
                    mapped_prop not in arg_map
                    or str(arg_map[mapped_prop]) != hv
                ):
                    raise HeaderMismatchError(
                        f"Divergence {hk} vs {mapped_prop}"
                    )
                continue
            norm_k = proj.lower().replace("-", "_")
            if norm_k in arg_map and str(arg_map[norm_k]) != hv:
                raise HeaderMismatchError(f"Divergence {hk} vs argument")
            if norm_k not in arg_map and hv not in arg_vals:
                raise HeaderMismatchError(f"Divergence valeur {hk}")
    cleaned = copy.deepcopy(body)
    c_params = cleaned.get("params")
    if isinstance(c_params, dict) and isinstance(c_params.get("_meta"), dict):
        keep = {_PROTO_META_KEY}
        if entry is not None:
            keep |= set(entry.allowed_meta_keys)
        c_params["_meta"] = {
            mk: mv for mk, mv in c_params["_meta"].items() if mk in keep
        }
    return cleaned


def compute_tool_definition_digest(
    tool_def: dict[str, Any], volatile_meta_keys: Iterable[str] = ()
) -> str:
    """Calcule 'sha256:' + JCS SHA-256 apres purge des cles volatiles."""
    vol = set(volatile_meta_keys)
    clean = {k: v for k, v in tool_def.items() if k not in vol}
    return "sha256:" + jcs_sha256_hex(clean)


def _tool_name(tool: Any) -> str:
    return str(tool.get("name", "")) if isinstance(tool, dict) else ""


def _tool_sync_error(
    tool: Any, ent: McpCatalogEntry | None,
    server_id: str, seen: set[str],
) -> str:
    if not isinstance(tool, dict):
        return "collision_ou_hors_catalogue"
    name = tool.get("name")
    if (not isinstance(name, str) or not name or name in seen
            or ent is None or ent.server_id != server_id):
        return "collision_ou_hors_catalogue"
    dig = compute_tool_definition_digest(tool, ent.volatile_meta_keys)
    return "derive_jcs_sha256" if dig != ent.definition_digest else ""


def _extract_mcp_fields(
    body: Any,
) -> tuple[dict[str, Any], dict[str, Any], Any, Any]:
    if not isinstance(body, dict):
        raise HeaderMismatchError("Corps JSON-RPC invalide (-32020)")
    p = body.get("params")
    m = p.get("_meta") if isinstance(p, dict) else None
    if not isinstance(p, dict) or not isinstance(m, dict):
        raise HeaderMismatchError("params/_meta MCP invalide (-32020)")
    return p, m, body.get("method"), p.get("name")


# CA-G0-SYNC-BEGIN:G0-EX-CH01-03
def verify_tools_list_against_catalog(
    tools: list[dict[str, Any]], catalog: Mapping[str, McpCatalogEntry],
    server_id: str, max_drift_before_suspend: int = 1,
) -> McpSyncResult:
    """Trie tools/list, detecte rug pull et prefixe server_id.tool."""
    active, suspended, reasons, seen = {}, [], {}, set()
    for tool in sorted(tools, key=_tool_name):
        name = _tool_name(tool)
        err = _tool_sync_error(tool, catalog.get(name), server_id, seen)
        seen.add(name)
        if err:
            active.pop(f"{server_id}.{name}", None)
            suspended.append(name)
            reasons[name] = err
        else:
            active[f"{server_id}.{name}"] = copy.deepcopy(tool)
    susp = len(suspended) >= max_drift_before_suspend
    act = {} if susp else active
    return McpSyncResult(act, tuple(suspended), susp, reasons)

def validate_mcp_headers(
    headers: Mapping[str, str], jsonrpc_body: dict[str, Any],
    catalog_entry: McpCatalogEntry | None = None,
) -> dict[str, Any]:
    """Verifie concordance MCP headers/body (-32020) et _meta."""
    hdr = _normalize_headers(headers)
    p, m, meth, mn = _extract_mcp_fields(jsonrpc_body)
    pv, mm = hdr.get("mcp-protocol-version"), hdr.get("mcp-method")
    if (not pv or pv != m.get(_PROTO_META_KEY) or not mm or mm != meth
            or (("name" in p or "mcp-name" in hdr) and (
                not isinstance(mn, str) or not mn
                or hdr.get("mcp-name") != mn))):
        raise HeaderMismatchError("En-tetes MCP divergents (-32020)")
    return _purge_and_validate(hdr, jsonrpc_body, catalog_entry)
# CA-G0-SYNC-END:G0-EX-CH01-03


class McpTransportAdapter(Protocol):
    """Interface d'isolation contre les derives MCP post-gel (SEP-3398)."""

    expected_revision: str

    def send_jsonrpc(
        self, method: str, params: dict[str, Any], headers: dict[str, str]
    ) -> dict[str, Any]:
        """Envoie un appel JSON-RPC conforme a expected_revision."""
        ...

    def capabilities(self) -> dict[str, Any]:
        """Retourne les capacites declarees du transport."""
        ...


class StreamableHttpAdapter:
    """Adaptateur MCP 2026-07-28 Streamable HTTP (refus strict HTTP+SSE)."""

    def __init__(
        self,
        endpoint: str,
        expected_revision: str = "2026-07-28",
        transport_mode: str = "streamable_http",
    ) -> None:
        self.endpoint = endpoint
        self.expected_revision = expected_revision
        self.transport_mode = transport_mode

    def send_jsonrpc(
        self, method: str, params: dict[str, Any], headers: dict[str, str]
    ) -> dict[str, Any]:
        """Valide le mode de transport et achemine un message JSON-RPC."""
        if self.transport_mode.lower() != "streamable_http":
            raise DeprecatedTransportError(
                f"Transport deprecie refuse (SEP-2596) : {self.transport_mode}"
            )
        hdr = {k.lower(): v for k, v in headers.items()}
        proto = hdr.get("mcp-protocol-version")
        if proto is not None and proto != self.expected_revision:
            raise HeaderMismatchError("MCP-Protocol-Version incompatible")
        return {
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "endpoint": self.endpoint,
                "method": method,
                "revision": self.expected_revision,
                "params": copy.deepcopy(params),
            },
        }

    def capabilities(self) -> dict[str, Any]:
        """Retourne les capacites Streamable HTTP 2026-07-28."""
        return {
            "transport": self.transport_mode,
            "revision": self.expected_revision,
            "streamable_http": self.transport_mode == "streamable_http",
            "http_sse_supported": False,
        }
