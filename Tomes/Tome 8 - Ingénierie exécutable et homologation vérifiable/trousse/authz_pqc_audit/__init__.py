# SPDX-License-Identifier: MIT
"""Module 2 : identite NHI, OBO/DPoP, CAEP, CIBA, PQC ML-DSA, OTel, SCITT."""

from __future__ import annotations

from authz_pqc_audit.audit_scitt_focus import (
    AuditChainLedger,
    ChainVerdict,
    FocusCpoSummary,
    ScittTree,
    build_scitt_merkle_tree,
    compute_cpo_and_focus,
    generate_inclusion_proof,
    seal_merkle_root,
    verify_inclusion_proof,
)
from authz_pqc_audit.ciba_approval import (
    ApprovalVerdict,
    IJsonError,
    compute_action_hash_h,
    validate_ijson_strict,
    verify_ciba_approval_tokens,
)
from authz_pqc_audit.obo_dpop import (
    OboValidationResult,
    extract_act_chain,
    validate_obo_delegation,
)
from authz_pqc_audit.otel_pii_mapper import (
    DEFAULT_ALLOWED_ATTRS,
    FORBIDDEN_RAW_CONTENT_ATTRS,
    GENAI_DEV_85_ATTRS,
    OTEL_V141_TO_GENAI_DEV_MAP,
    REQUIRED_MANDATE_JOIN_ATTRS,
    OtelGenAiMapper,
    map_span_attributes,
    redact_pii_bilingual,
)
from authz_pqc_audit.pqc_http431 import (
    ML_DSA_SPECS,
    Http431Measurement,
    PqcProfile,
    build_signed_delegation_frame,
    evaluate_http_431,
)
from authz_pqc_audit.revocation_fsm import (
    AgentAuthState,
    CaepRevocationEvent,
    RevocationStateMachine,
)
from authz_pqc_audit.slh_dsa_fips205 import (
    keygen_slh_dsa_sha2_128f,
    keygen_slh_dsa_sha2_128s,
    sign_slh_dsa_sha2_128f,
    sign_slh_dsa_sha2_128s,
    verify_slh_dsa_sha2_128f,
    verify_slh_dsa_sha2_128s,
)

__all__ = [
    "AgentAuthState",
    "ApprovalVerdict",
    "AuditChainLedger",
    "CaepRevocationEvent",
    "ChainVerdict",
    "DEFAULT_ALLOWED_ATTRS",
    "FORBIDDEN_RAW_CONTENT_ATTRS",
    "FocusCpoSummary",
    "GENAI_DEV_85_ATTRS",
    "Http431Measurement",
    "IJsonError",
    "ML_DSA_SPECS",
    "OTEL_V141_TO_GENAI_DEV_MAP",
    "OboValidationResult",
    "OtelGenAiMapper",
    "PqcProfile",
    "REQUIRED_MANDATE_JOIN_ATTRS",
    "RevocationStateMachine",
    "ScittTree",
    "build_scitt_merkle_tree",
    "build_signed_delegation_frame",
    "compute_action_hash_h",
    "compute_cpo_and_focus",
    "evaluate_http_431",
    "extract_act_chain",
    "generate_inclusion_proof",
    "keygen_slh_dsa_sha2_128f",
    "keygen_slh_dsa_sha2_128s",
    "map_span_attributes",
    "redact_pii_bilingual",
    "seal_merkle_root",
    "sign_slh_dsa_sha2_128f",
    "sign_slh_dsa_sha2_128s",
    "validate_ijson_strict",
    "validate_obo_delegation",
    "verify_ciba_approval_tokens",
    "verify_inclusion_proof",
    "verify_slh_dsa_sha2_128f",
    "verify_slh_dsa_sha2_128s",
]
