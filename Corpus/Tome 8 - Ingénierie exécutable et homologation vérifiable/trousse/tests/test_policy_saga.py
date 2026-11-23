# SPDX-License-Identifier: MIT
"""Suite pytest TDD pour Module 3 : OPA/Rego, CaMeL, sandbox, Decimal."""

from __future__ import annotations

import copy
from decimal import Decimal
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
import pytest

from policy_saga.decimal_money import from_decimal_str
from policy_saga.opa_runner import (
    OpaPolicyEngine,
    OpaStaticCheckError,
    verify_rego_default_deny,
)
from policy_saga.saga_orchestrator import (
    IdempotencyConflictError,
    SagaOrchestrator,
)
from policy_saga.sandbox_manifest import (
    IANA_SPECIAL_CIDRS,
    IMDS_IPV4,
    validate_sandbox_manifest,
)
from policy_saga.taint_camel import (
    SessionTaintTracker,
    TaintLevel,
    delegate_taint_envelope,
    record_tool_output,
)

ROOT_DIR = Path(__file__).resolve().parent.parent
POLICIES_DIR = ROOT_DIR / "policies_opa"
SCHEMAS_DIR = ROOT_DIR / "schemas"
OPA_BIN = ROOT_DIR / ".tools" / (
    "opa.exe" if Path("C:/").exists() else "opa"
)


def _load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMAS_DIR / name).read_text(encoding="utf-8"))


def _opa_engine() -> OpaPolicyEngine:
    opa_path = OPA_BIN if OPA_BIN.is_file() else None
    return OpaPolicyEngine(POLICIES_DIR, opa_bin=opa_path)


def _valid_opa_input(**overrides: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "tool": {
            "name": "creer_bon_commande",
            "tier": "P2",
            "exfiltration_capable": False,
            "egress_destination": "erp.ent.ca",
        },
        "session": {
            "consumed_untrusted": False,
            "tainted_sources": [],
            "provenance_hops": ["spiffe://ent.ca/agent-orch"],
        },
        "human_approval": {
            "verified": False,
            "action_sha256": None,
            "approver_sub": None,
        },
        "computed_action_sha256": (
            "92be40835a73023d117ebb4965da82df"
            "a05e2e6d647d0919d53461289bbc6e81"
        ),
        "principal_sub": "alice",
        "egress_allowlist": ["erp.ent.ca", "catalogue.ent.ca"],
        "control_flow_source": "TRUSTED_PLAN",
        "args_derived_from_untrusted": False,
        "sensitive_args_grounded_against_sor": False,
        "a2a_delegation": {
            "enabled": False,
            "propagated_consumed_untrusted": False,
        },
    }
    for key, val in overrides.items():
        base[key] = val
    return base


def _valid_sandbox_manifest() -> dict[str, Any]:
    return {
        "sandbox_id": "sbx-policy-01",
        "network": {
            "mode": "none",
            "allowlist": [],
            "imds_blocked": True,
            "special_iana_blocked": True,
            "blocked_cidrs": list(IANA_SPECIAL_CIDRS),
        },
        "env_secrets": [],
        "read_only_root": True,
        "allow_shell": False,
        "timeouts": {"tool_s": 30, "loop_s": 1200, "lifetime_s": 3600},
    }


def test_opa_default_deny_before_mutative_tool() -> None:
    for rego in sorted(POLICIES_DIR.glob("*.rego")):
        if rego.name.endswith("_test.rego"):
            continue
        verify_rego_default_deny(rego)

    engine = _opa_engine()
    # Payload vide -> refus ferme False
    assert engine.evaluate("data.trousse.policy.rule_of_two.allow", {}) is False
    # Outil P3 sans approbation -> refus ferme False
    p3_no_approval = _valid_opa_input(
        tool={
            "name": "virer_fonds",
            "tier": "P3",
            "exfiltration_capable": False,
            "egress_destination": "erp.ent.ca",
        }
    )
    assert (
        engine.evaluate("data.trousse.policy.rule_of_two.allow", p3_no_approval)
        is False
    )


def test_opa_static_check_rejects_missing_default_deny(
    tmp_path: Path,
) -> None:
    bad_rego = tmp_path / "missing_deny.rego"
    bad_rego.write_text(
        "# SPDX-License-Identifier: MIT\n"
        "package bad.policy\n"
        "import rego.v1\n"
        "allow := true\n",
        encoding="utf-8",
    )
    with pytest.raises(OpaStaticCheckError):
        verify_rego_default_deny(bad_rego)


def test_opa_coverage_100_percent() -> None:
    report = _opa_engine().run_coverage()
    assert report.passed is True
    assert report.tests_failed == 0
    assert report.tests_passed >= 30
    assert report.coverage_pct == 100.0
    assert report.not_covered_lines == 0


def test_deterministic_controls_opa_100_coverage() -> None:
    report = _opa_engine().run_coverage()
    assert report.coverage_pct == 100.0
    assert report.passed is True


def test_rule_of_two_interface_vs_write_separation() -> None:
    engine = _opa_engine()
    interface_agent = _valid_opa_input(
        tool={
            "name": "lire_courriel",
            "tier": "P1",
            "exfiltration_capable": False,
            "egress_destination": "catalogue.ent.ca",
        },
        session={
            "consumed_untrusted": False,
            "tainted_sources": [],
            "provenance_hops": ["spiffe://ent.ca/agent-interface"],
        },
    )
    Draft202012Validator(_load_schema("opa_authz_input.schema.json")).validate(
        interface_agent
    )
    assert (
        engine.evaluate(
            "data.trousse.policy.rule_of_two.allow", interface_agent
        )
        is True
    )


def test_rule_of_two_denies_untrusted_plus_exfiltration() -> None:
    engine = _opa_engine()
    trifecta = _valid_opa_input(
        tool={
            "name": "exporter_webhook",
            "tier": "P1",
            "exfiltration_capable": True,
            "egress_destination": "erp.ent.ca",
        },
        session={
            "consumed_untrusted": True,
            "tainted_sources": ["courriel-externe-99"],
            "provenance_hops": ["spiffe://ent.ca/agent-interface"],
        },
    )
    assert (
        engine.evaluate("data.trousse.policy.rule_of_two.allow", trifecta)
        is False
    )


def test_opa_rule_of_two_and_rar_mandate() -> None:
    engine = _opa_engine()
    h = "92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81"
    approved_p3 = _valid_opa_input(
        tool={
            "name": "emettre_paiement",
            "tier": "P3",
            "exfiltration_capable": True,
            "egress_destination": "erp.ent.ca",
        },
        session={
            "consumed_untrusted": True,
            "tainted_sources": ["doc-externe"],
            "provenance_hops": ["spiffe://ent.ca/agent-orch"],
        },
        computed_action_sha256=h,
        human_approval={
            "verified": True,
            "action_sha256": h,
            "approver_sub": "apb-5e19c2",
        },
    )
    assert (
        engine.evaluate("data.trousse.policy.rule_of_two.allow", approved_p3)
        is True
    )

    # Auto-approbation -> refuse
    self_approved = copy.deepcopy(approved_p3)
    self_approved["human_approval"]["approver_sub"] = "alice"
    assert (
        engine.evaluate("data.trousse.policy.rule_of_two.allow", self_approved)
        is False
    )


def test_camel_taint_propagation_across_agents() -> None:
    t0 = SessionTaintTracker(tenant_id="tenant-a")
    t1 = record_tool_output(
        t0, "courriel-externe", TaintLevel.UNTRUSTED_EXTERNAL
    )
    assert t1.consumed_untrusted is True
    assert "courriel-externe" in t1.tainted_sources

    # Propagation obligatoire vers agent aval (Can CaMeLs Talk?)
    t2 = delegate_taint_envelope(t1, "spiffe://ent.ca/agent-aval")
    assert t2.consumed_untrusted is True
    assert "spiffe://ent.ca/agent-aval" in t2.provenance_hops

    engine = _opa_engine()
    dropped = _valid_opa_input(
        session={
            "consumed_untrusted": True,
            "tainted_sources": ["courriel-externe"],
            "provenance_hops": ["spiffe://ent.ca/agent-aval"],
        },
        a2a_delegation={
            "enabled": True,
            "propagated_consumed_untrusted": False,
        },
    )
    assert (
        engine.evaluate("data.trousse.policy.camel_taint.allow", dropped)
        is False
    )

    propagated = copy.deepcopy(dropped)
    propagated["a2a_delegation"]["propagated_consumed_untrusted"] = True
    assert (
        engine.evaluate("data.trousse.policy.camel_taint.allow", propagated)
        is True
    )


def test_multitenant_context_taint_isolation() -> None:
    t_a = SessionTaintTracker(tenant_id="locataire-alpha")
    t_a_dirty = record_tool_output(t_a, "doc-alpha", TaintLevel.PII_RESTRICTED)
    t_b = SessionTaintTracker(tenant_id="locataire-beta")
    assert t_a_dirty.consumed_untrusted is True
    assert t_b.consumed_untrusted is False
    assert t_b.tainted_sources == []
    t_a_child = delegate_taint_envelope(t_a_dirty, "spiffe://ent.ca/agt-b")
    assert t_a_child.tenant_id == "locataire-alpha"


def test_acl_and_asi06_memory_protection() -> None:
    engine = _opa_engine()
    poisoned = _valid_opa_input(
        control_flow_source="UNTRUSTED_DATA",
        args_derived_from_untrusted=True,
        sensitive_args_grounded_against_sor=False,
    )
    assert (
        engine.evaluate("data.trousse.policy.camel_taint.allow", poisoned)
        is False
    )

    ungrounded = _valid_opa_input(
        control_flow_source="TRUSTED_PLAN",
        args_derived_from_untrusted=True,
        sensitive_args_grounded_against_sor=False,
    )
    assert (
        engine.evaluate("data.trousse.policy.camel_taint.allow", ungrounded)
        is False
    )


def test_sandbox_manifest_no_kvm_enforced() -> None:
    schema = _load_schema("sandbox_manifest.schema.json")
    manifest = _valid_sandbox_manifest()
    Draft202012Validator(schema).validate(manifest)
    assert validate_sandbox_manifest(manifest, schema) == []
    assert _opa_engine().evaluate("data.trousse.policy.sandbox.allow", manifest)


def test_sandbox_denies_egress_and_iana_ranges() -> None:
    schema = _load_schema("sandbox_manifest.schema.json")
    assert len(IANA_SPECIAL_CIDRS) == 11

    # Joker '*' interdit
    wildcard_manifest = _valid_sandbox_manifest()
    wildcard_manifest["network"]["mode"] = "allowlist"
    wildcard_manifest["network"]["allowlist"] = ["*"]
    assert len(validate_sandbox_manifest(wildcard_manifest, schema)) >= 1
    assert (
        _opa_engine().evaluate(
            "data.trousse.policy.sandbox.allow", wildcard_manifest
        )
        is False
    )

    # Chaque plage IANA speciale dans allowlist doit etre rejetee
    for ip_sample in (
        "127.0.0.1",
        "10.0.0.5",
        "100.64.0.10",
        "169.254.169.254",
        "172.16.0.1",
        "192.168.1.10",
        "::1",
        "fc00::1",
        "fe80::1",
        "::ffff:10.0.0.1",
        "64:ff9b::1",
    ):
        bad = _valid_sandbox_manifest()
        bad["network"]["mode"] = "allowlist"
        bad["network"]["allowlist"] = [ip_sample]
        assert len(validate_sandbox_manifest(bad, schema)) >= 1

    # Mode 'none' avec allowlist non vide et CIDR recoupant une plage IANA
    bad_none = _valid_sandbox_manifest()
    bad_none["network"]["mode"] = "none"
    bad_none["network"]["allowlist"] = ["erp.ent.ca"]
    assert len(validate_sandbox_manifest(bad_none, schema)) >= 1

    for cidr in ("10.1.0.0/16", "169.254.169.0/24"):
        bad_cidr = _valid_sandbox_manifest()
        bad_cidr["network"]["mode"] = "allowlist"
        bad_cidr["network"]["allowlist"] = [cidr]
        assert len(validate_sandbox_manifest(bad_cidr, schema)) >= 1


def test_sandbox_blocks_imds_169_254_169_254() -> None:
    assert IMDS_IPV4 == "169.254.169.254"
    schema = _load_schema("sandbox_manifest.schema.json")
    bad = _valid_sandbox_manifest()
    bad["network"]["imds_blocked"] = False
    assert len(validate_sandbox_manifest(bad, schema)) >= 1
    assert (
        _opa_engine().evaluate("data.trousse.policy.sandbox.allow", bad)
        is False
    )


def test_sandbox_rejects_env_secrets() -> None:
    schema = _load_schema("sandbox_manifest.schema.json")
    bad = _valid_sandbox_manifest()
    bad["env_secrets"] = ["AWS_SECRET_ACCESS_KEY"]
    assert len(validate_sandbox_manifest(bad, schema)) >= 1
    assert (
        _opa_engine().evaluate("data.trousse.policy.sandbox.allow", bad)
        is False
    )


def test_sandbox_three_level_timeouts() -> None:
    schema = _load_schema("sandbox_manifest.schema.json")
    for field, bad_val in (
        ("tool_s", 31),
        ("loop_s", 1201),
        ("lifetime_s", 3601),
    ):
        bad = _valid_sandbox_manifest()
        bad["timeouts"][field] = bad_val
        assert len(validate_sandbox_manifest(bad, schema)) >= 1
        assert (
            _opa_engine().evaluate("data.trousse.policy.sandbox.allow", bad)
            is False
        )


def test_sre_confinement_read_only_no_shell() -> None:
    schema = _load_schema("sandbox_manifest.schema.json")
    bad_root = _valid_sandbox_manifest()
    bad_root["read_only_root"] = False
    assert len(validate_sandbox_manifest(bad_root, schema)) >= 1

    bad_shell = _valid_sandbox_manifest()
    bad_shell["allow_shell"] = True
    assert len(validate_sandbox_manifest(bad_shell, schema)) >= 1
    assert (
        _opa_engine().evaluate("data.trousse.policy.sandbox.allow", bad_shell)
        is False
    )


def test_decimal_rejects_float_budget() -> None:
    with pytest.raises(TypeError):
        from_decimal_str(0.1)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        from_decimal_str(12.48)  # type: ignore[arg-type]

    a = from_decimal_str("0.10", currency="CAD")
    b = from_decimal_str(Decimal("0.20"), currency="CAD")
    c = from_decimal_str("0.30", currency="CAD")
    assert a.cents + b.cents == c.cents == 30
    rounded = from_decimal_str("12.345", currency="CAD")
    assert rounded.cents == 1234  # ROUND_HALF_EVEN


def test_saga_idempotency_409_and_422(tmp_path: Path) -> None:
    orch = SagaOrchestrator(db_path=tmp_path / "idem.sqlite")
    first = orch.submit_step_idempotent(
        "tache-1", "etape-1", {"montant_cents": 1000}
    )
    assert first["montant_cents"] == 1000

    # Rejeu idempotent exact -> retourne le resultat memorise
    replay = orch.submit_step_idempotent(
        "tache-1", "etape-1", {"montant_cents": 1000}
    )
    assert replay == first

    # Requete en cours -> HTTP 409
    with pytest.raises(IdempotencyConflictError) as exc_409:
        orch.submit_step_idempotent(
            "tache-2", "etape-1", {"montant_cents": 1000}, in_progress=True
        )
    assert exc_409.value.http_status == 409

    # Meme cle avec charge utile differente -> HTTP 422
    with pytest.raises(IdempotencyConflictError) as exc_422:
        orch.submit_step_idempotent(
            "tache-1", "etape-1", {"montant_cents": 2000}
        )
    assert exc_422.value.http_status == 422
