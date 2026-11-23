# SPDX-License-Identifier: MIT
"""Module 1 : harnais deterministe 80/20, JCS RFC 8785, MCP et A2A."""

from __future__ import annotations

from harness_proto.a2a_card import (
    AgentCardAdapter,
    AgentCardVerdict,
    validate_agent_card,
)
from harness_proto.jcs import JcsError, canonicalize_jcs, jcs_sha256_hex
from harness_proto.mcp_pinning import (
    DeprecatedTransportError,
    HeaderMismatchError,
    McpCatalogEntry,
    McpSyncResult,
    McpTransportAdapter,
    StreamableHttpAdapter,
    compute_tool_definition_digest,
    validate_mcp_headers,
    verify_tools_list_against_catalog,
)
from harness_proto.pipeline import (
    DeterministicHarness,
    HarnessConfig,
    HarnessOutcome,
    StepStatus,
    validate_strict_schema,
)

__all__ = [
    "AgentCardAdapter",
    "AgentCardVerdict",
    "DeprecatedTransportError",
    "DeterministicHarness",
    "HarnessConfig",
    "HarnessOutcome",
    "HeaderMismatchError",
    "JcsError",
    "McpCatalogEntry",
    "McpSyncResult",
    "McpTransportAdapter",
    "StepStatus",
    "StreamableHttpAdapter",
    "canonicalize_jcs",
    "compute_tool_definition_digest",
    "jcs_sha256_hex",
    "validate_agent_card",
    "validate_mcp_headers",
    "validate_strict_schema",
    "verify_tools_list_against_catalog",
]
