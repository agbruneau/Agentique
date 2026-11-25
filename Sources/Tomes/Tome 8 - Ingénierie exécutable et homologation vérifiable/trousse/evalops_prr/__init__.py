# SPDX-License-Identifier: MIT
"""Module 4 : banc EvalOps hermetique, Wilson 3/p, metamorphique et PRR."""

from __future__ import annotations

from evalops_prr.metamorphic import (
    MetamorphicCheck,
    MetamorphicRelation,
    TrajectoryResult,
    verify_metamorphic_pair,
)
from evalops_prr.mock_mcp_harness import (
    MockMcpServer,
    TrajectoryVerdict,
    compute_pass_k,
    evaluate_trajectory,
)
from evalops_prr.prr_validators import (
    BLOCKING_PRR_IDS,
    REQUIRED_5_SBB_SLOTS,
    REQUIRED_BLUEPRINT_IDS,
    PrrReport,
    validate_adr_2027_b001,
    validate_blueprints_and_c40,
    validate_prr_24_blocking,
)
from evalops_prr.wilson_bounds import (
    Z_95_ONE_SIDED,
    Z_95_TWO_SIDED,
    WilsonVerdict,
    evaluate_wilson_gate,
    wilson_failure_upper_bound,
)

__all__ = [
    "BLOCKING_PRR_IDS",
    "MetamorphicCheck",
    "MetamorphicRelation",
    "MockMcpServer",
    "PrrReport",
    "REQUIRED_5_SBB_SLOTS",
    "REQUIRED_BLUEPRINT_IDS",
    "TrajectoryResult",
    "TrajectoryVerdict",
    "WilsonVerdict",
    "Z_95_ONE_SIDED",
    "Z_95_TWO_SIDED",
    "compute_pass_k",
    "evaluate_trajectory",
    "evaluate_wilson_gate",
    "validate_adr_2027_b001",
    "validate_blueprints_and_c40",
    "validate_prr_24_blocking",
    "verify_metamorphic_pair",
    "wilson_failure_upper_bound",
]
