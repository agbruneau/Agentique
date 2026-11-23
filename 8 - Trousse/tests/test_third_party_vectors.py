# SPDX-License-Identifier: MIT
"""Suite pytest TDD pour les 4 suites de vecteurs officiels tiers."""

from __future__ import annotations

import base64
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import struct

from dilithium_py.ml_dsa import ML_DSA_65, ML_DSA_87
from jsonschema import Draft202012Validator
import pytest

from authz_pqc_audit.slh_dsa_fips205 import (
    keygen_slh_dsa_sha2_128f,
    keygen_slh_dsa_sha2_128s,
    sign_slh_dsa_sha2_128f,
    sign_slh_dsa_sha2_128s,
    verify_slh_dsa_sha2_128f,
    verify_slh_dsa_sha2_128s,
)
from evalops_prr.metamorphic import (
    MetamorphicRelation,
    TrajectoryResult,
    verify_metamorphic_pair,
)
from evalops_prr.prr_validators import validate_adr_2027_b001
from harness_proto.a2a_card import validate_agent_card
from harness_proto.jcs import JcsError, canonicalize_jcs
from policy_saga.opa_runner import OpaPolicyEngine

ROOT_DIR = Path(__file__).resolve().parent.parent
VECTORS_DIR = ROOT_DIR / "vectors"
SCHEMAS_DIR = ROOT_DIR / "schemas"
POLICIES_DIR = ROOT_DIR / "policies_opa"
OPA_BIN = ROOT_DIR / ".tools" / (
    "opa.exe" if Path("C:/").exists() else "opa"
)


def test_vectors_manifest_integrity_four_suites() -> None:
    manifest = json.loads(
        (VECTORS_DIR / "vectors-manifest.json").read_text(encoding="utf-8")
    )
    assert manifest["freeze_date"] == "2026-12-02"
    assert set(manifest["suites"]) == {
        "rfc8785",
        "nist_acvp",
        "a2a_tck",
        "owasp_src055",
    }
    assert manifest["file_count"] == len(manifest["files"]) == 50


def test_rfc8785_appendix_b_and_utf16_vectors() -> None:
    data = json.loads(
        (VECTORS_DIR / "rfc8785/rfc8785_appendix_b_and_utf16.json").read_text(
            encoding="utf-8"
        )
    )
    for sample in data["appendix_b_number_samples"]:
        num = struct.unpack(">d", bytes.fromhex(sample["ieee754_hex"]))[0]
        if sample["must_reject"]:
            with pytest.raises(JcsError):
                canonicalize_jcs(num)
        else:
            assert (
                canonicalize_jcs(num).decode("utf-8")
                == sample["expected_json"]
            )

    s322 = data["section_3_2_2_and_3_2_4_sample"]
    obj_322 = json.loads(s322["input_json_text"])
    assert canonicalize_jcs(obj_322) == bytes.fromhex(s322["expected_utf8_hex"])

    s323 = data["section_3_2_3_utf16_sorting"]
    obj_323 = json.loads(s323["input_json_text"])
    canon_323 = json.loads(canonicalize_jcs(obj_323).decode("utf-8"))
    assert list(canon_323.values()) == s323["expected_value_order"]

    edge = data["utf16_bmp_vs_astral_edge_case"]
    out_edge = canonicalize_jcs(edge["input"]).decode("utf-8")
    assert out_edge == edge["expected_canonical"]


def test_rfc8785_cyberphone_testdata_byte_for_byte() -> None:
    in_dir = VECTORS_DIR / "rfc8785/testdata/input"
    out_dir = VECTORS_DIR / "rfc8785/testdata/output"
    hex_dir = VECTORS_DIR / "rfc8785/testdata/outhex"
    files = sorted(in_dir.glob("*.json"))
    assert len(files) == 6

    for infile in files:
        obj = json.loads(infile.read_text(encoding="utf-8"))
        actual = canonicalize_jcs(obj)
        expected = (out_dir / infile.name).read_bytes()
        expected_hex = bytes.fromhex(
            "".join(
                (hex_dir / f"{infile.stem}.txt")
                .read_text(encoding="utf-8")
                .split()
            )
        )
        assert actual == expected == expected_hex


def test_nist_acvp_ml_dsa_fips204_keygen_siggen_sigver() -> None:
    acvp = VECTORS_DIR / "nist_acvp"
    cls_map = {"ML-DSA-65": ML_DSA_65, "ML-DSA-87": ML_DSA_87}

    kg_p = json.loads(
        (acvp / "ML-DSA-keyGen-FIPS204/prompt.json").read_text("utf-8")
    )
    kg_e = json.loads(
        (acvp / "ML-DSA-keyGen-FIPS204/expectedResults.json").read_text(
            "utf-8"
        )
    )
    for grp, egrp in zip(kg_p["testGroups"], kg_e["testGroups"]):
        cls = cls_map[grp["parameterSet"]]
        for tc, exp in zip(grp["tests"], egrp["tests"]):
            pk, sk = cls.key_derive(bytes.fromhex(tc["seed"]))
            assert pk.hex().upper() == exp["pk"]
            assert sk.hex().upper() == exp["sk"]

    sg_p = json.loads(
        (acvp / "ML-DSA-sigGen-FIPS204/prompt.json").read_text("utf-8")
    )
    sg_e = json.loads(
        (acvp / "ML-DSA-sigGen-FIPS204/expectedResults.json").read_text(
            "utf-8"
        )
    )
    for grp, egrp in zip(sg_p["testGroups"], sg_e["testGroups"]):
        cls = cls_map[grp["parameterSet"]]
        if (
            grp.get("signatureInterface") == "external"
            and grp.get("preHash") == "pure"
        ):
            for tc, exp in zip(grp["tests"], egrp["tests"]):
                sk = bytes.fromhex(tc["sk"])
                msg = bytes.fromhex(tc["message"])
                ctx = bytes.fromhex(tc.get("context", ""))
                if grp["deterministic"]:
                    sig = cls.sign(sk, msg, ctx=ctx, deterministic=True)
                else:
                    m_prime = b"\x00" + len(ctx).to_bytes(1, "big") + ctx + msg
                    sig = cls._sign_internal(
                        sk, m_prime, bytes.fromhex(tc["rnd"])
                    )
                assert sig.hex().upper() == exp["signature"]
        elif (
            grp.get("signatureInterface") == "internal"
            and not grp.get("externalMu", False)
        ):
            for tc, exp in zip(grp["tests"], egrp["tests"]):
                rnd = (
                    bytes(32)
                    if grp["deterministic"]
                    else bytes.fromhex(tc["rnd"])
                )
                sig = cls._sign_internal(
                    bytes.fromhex(tc["sk"]),
                    bytes.fromhex(tc["message"]),
                    rnd,
                )
                assert sig.hex().upper() == exp["signature"]

    sv_p = json.loads(
        (acvp / "ML-DSA-sigVer-FIPS204/prompt.json").read_text("utf-8")
    )
    sv_e = json.loads(
        (acvp / "ML-DSA-sigVer-FIPS204/expectedResults.json").read_text(
            "utf-8"
        )
    )
    for grp, egrp in zip(sv_p["testGroups"], sv_e["testGroups"]):
        cls = cls_map[grp["parameterSet"]]
        if (
            grp.get("signatureInterface") == "external"
            and grp.get("preHash") == "pure"
        ):
            for tc, exp in zip(grp["tests"], egrp["tests"]):
                ok = cls.verify(
                    bytes.fromhex(tc["pk"]),
                    bytes.fromhex(tc["message"]),
                    bytes.fromhex(tc["signature"]),
                    ctx=bytes.fromhex(tc.get("context", "")),
                )
                assert ok is exp["testPassed"]
        elif (
            grp.get("signatureInterface") == "internal"
            and not grp.get("externalMu", False)
        ):
            for tc, exp in zip(grp["tests"], egrp["tests"]):
                ok = cls._verify_internal(
                    bytes.fromhex(tc["pk"]),
                    bytes.fromhex(tc["message"]),
                    bytes.fromhex(tc["signature"]),
                )
                assert ok is exp["testPassed"]


def test_nist_acvp_slh_dsa_fips205_keygen_siggen_sigver() -> None:
    acvp = VECTORS_DIR / "nist_acvp"
    kg_fns = {
        "SLH-DSA-SHA2-128s": keygen_slh_dsa_sha2_128s,
        "SLH-DSA-SHA2-128f": keygen_slh_dsa_sha2_128f,
    }
    sg_fns = {
        "SLH-DSA-SHA2-128s": sign_slh_dsa_sha2_128s,
        "SLH-DSA-SHA2-128f": sign_slh_dsa_sha2_128f,
    }
    sv_fns = {
        "SLH-DSA-SHA2-128s": verify_slh_dsa_sha2_128s,
        "SLH-DSA-SHA2-128f": verify_slh_dsa_sha2_128f,
    }

    kg_p = json.loads(
        (acvp / "SLH-DSA-keyGen-FIPS205/prompt.json").read_text("utf-8")
    )
    kg_e = json.loads(
        (acvp / "SLH-DSA-keyGen-FIPS205/expectedResults.json").read_text(
            "utf-8"
        )
    )
    for grp, egrp in zip(kg_p["testGroups"], kg_e["testGroups"]):
        fn = kg_fns[grp["parameterSet"]]
        for tc, exp in zip(grp["tests"], egrp["tests"]):
            pk, sk = fn(
                bytes.fromhex(tc["skSeed"]),
                bytes.fromhex(tc["skPrf"]),
                bytes.fromhex(tc["pkSeed"]),
            )
            assert pk.hex().upper() == exp["pk"]
            assert sk.hex().upper() == exp["sk"]

    sg_p = json.loads(
        (acvp / "SLH-DSA-sigGen-FIPS205/prompt.json").read_text("utf-8")
    )
    sg_e = json.loads(
        (acvp / "SLH-DSA-sigGen-FIPS205/expectedResults.json").read_text(
            "utf-8"
        )
    )
    for grp, egrp in zip(sg_p["testGroups"], sg_e["testGroups"]):
        if grp.get("preHash") == "preHash":
            continue
        fn = sg_fns[grp["parameterSet"]]
        iface = grp.get("signatureInterface", "external")
        for tc, exp in zip(grp["tests"], egrp["tests"]):
            addr_rnd = (
                None
                if grp["deterministic"]
                else bytes.fromhex(tc["additionalRandomness"])
            )
            sig = fn(
                bytes.fromhex(tc["sk"]),
                bytes.fromhex(tc["message"]),
                addr_rnd=addr_rnd,
                ctx=bytes.fromhex(tc.get("context", "")),
                interface=iface,
            )
            assert sig.hex().upper() == exp["signature"]

    sv_p = json.loads(
        (acvp / "SLH-DSA-sigVer-FIPS205/prompt.json").read_text("utf-8")
    )
    sv_e = json.loads(
        (acvp / "SLH-DSA-sigVer-FIPS205/expectedResults.json").read_text(
            "utf-8"
        )
    )
    for grp, egrp in zip(sv_p["testGroups"], sv_e["testGroups"]):
        if grp.get("preHash") == "preHash":
            continue
        fn = sv_fns[grp["parameterSet"]]
        iface = grp.get("signatureInterface", "external")
        for tc, exp in zip(grp["tests"], egrp["tests"]):
            ok = fn(
                bytes.fromhex(tc["pk"]),
                bytes.fromhex(tc["message"]),
                bytes.fromhex(tc["signature"]),
                ctx=bytes.fromhex(tc.get("context", "")),
                interface=iface,
            )
            assert ok is exp["testPassed"]


def test_a2a_tck_alpha3_jcs_and_negative_cases() -> None:
    tck_dir = VECTORS_DIR / "a2a_tck"
    cases = json.loads(
        (tck_dir / "agent_card_tck_cases.json").read_text("utf-8")
    )
    vectors = json.loads(
        (tck_dir / "agent_card_vectors.json").read_text("utf-8")
    )
    must_reqs = json.loads(
        (tck_dir / "a2a_tck_must_requirements.json").read_text("utf-8")
    )
    assert cases["upstream_tag"] == "1.0.0.alpha3"
    assert vectors["a2a_jcs_v01_present"] is False
    assert must_reqs["must_requirements_count"] == 114

    s841 = vectors["spec_8_4_1_jcs_canonicalization"]
    assert (
        canonicalize_jcs(s841["input_after_default_omission"]).decode("utf-8")
        == s841["expected_jcs_canonical"]
    )

    s842 = vectors["spec_8_4_2_jws_format"]
    b64_hdr = s842["signature_object"]["protected"]
    padded = b64_hdr + "=" * ((4 - len(b64_hdr) % 4) % 4)
    decoded_hdr = json.loads(base64.urlsafe_b64decode(padded).decode("utf-8"))
    assert decoded_hdr == s842["expected_decoded_protected_header"]

    req_fields = set(cases["required_agent_card_fields"])
    for key in ("spec_8_5_sample_agent_card", "sut_python_agent_card"):
        assert req_fields.issubset(vectors[key].keys())

    schema = json.loads(
        (SCHEMAS_DIR / "a2a_agent_card.schema.json").read_text("utf-8")
    )
    for neg in vectors["derived_negative_cases"]:
        if "payload" in neg:
            verdict = validate_agent_card(
                neg["payload"],
                jwks={"keys": []},
                pinned_jku="https://example.com/agent/jwks.json",
                approved_extensions=set(),
                schema=schema,
            )
            assert verdict.valid is False
        elif "protected_header" in neg:
            hdr_bytes = json.dumps(
                neg["protected_header"], separators=(",", ":")
            ).encode("utf-8")
            hdr_b64 = (
                base64.urlsafe_b64encode(hdr_bytes).rstrip(b"=").decode("ascii")
            )
            card_bad_sig = copy.deepcopy(vectors["spec_8_5_sample_agent_card"])
            card_bad_sig["signatures"] = [
                {"protected": hdr_b64, "signature": "AAAA" * 16}
            ]
            verdict = validate_agent_card(
                card_bad_sig,
                jwks={"keys": []},
                pinned_jku="https://example.com/agent/jwks.json",
                approved_extensions=set(),
                schema=schema,
            )
            assert verdict.valid is False


def test_owasp_src055_asi01_asi10_full_coverage() -> None:
    owasp_dir = VECTORS_DIR / "owasp_src055"
    catalog = json.loads(
        (owasp_dir / "asi01_asi10_catalog.json").read_text("utf-8")
    )
    summary = json.loads(
        (owasp_dir / "crosswalk_web_summary.json").read_text("utf-8")
    )
    assert catalog["coverage_count"] == 10
    assert summary["ao_01_status"] == "L+"
    assert "genai.owasp.org" in catalog["ao_01_exclusion_notice"]

    expected_ids = [f"ASI{i:02d}" for i in range(1, 11)]
    assert [t["id"] for t in catalog["threats"]] == expected_ids
    for asi_id in expected_ids:
        entry_path = owasp_dir / "crosswalk_entries" / f"{asi_id}.json"
        assert entry_path.is_file()

    # Couverture OPA (rule_of_two, camel_taint, sandbox), metamorphic, B001
    opa_bin = OPA_BIN if OPA_BIN.is_file() else None
    engine = OpaPolicyEngine(POLICIES_DIR, opa_bin=opa_bin)
    # ASI01/ASI02/ASI04/ASI08/ASI10 : exfiltration + contamination refusee
    assert (
        engine.evaluate(
            "data.trousse.policy.rule_of_two.allow",
            {
                "tool": {
                    "name": "exfil",
                    "tier": "P2",
                    "exfiltration_capable": True,
                    "egress_destination": "erp.ent.ca",
                },
                "session": {"consumed_untrusted": True},
                "human_approval": {
                    "verified": False,
                    "action_sha256": None,
                    "approver_sub": None,
                },
                "computed_action_sha256": "a" * 64,
                "principal_sub": "alice",
                "egress_allowlist": ["erp.ent.ca"],
            },
        )
        is False
    )
    # ASI06/ASI07 : contamination A2A / memoire bloquee par camel_taint
    assert (
        engine.evaluate(
            "data.trousse.policy.camel_taint.allow",
            {
                "control_flow_source": "UNTRUSTED_DATA",
                "args_derived_from_untrusted": True,
                "sensitive_args_grounded_against_sor": False,
                "session": {"consumed_untrusted": True},
                "a2a_delegation": {
                    "enabled": True,
                    "propagated_consumed_untrusted": False,
                },
            },
        )
        is False
    )
    # ASI03/ASI05 : secret env ou shell libre bloque par sandbox
    assert (
        engine.evaluate(
            "data.trousse.policy.sandbox.allow",
            {
                "sandbox_id": "sbx-asi05",
                "network": {
                    "mode": "none",
                    "allowlist": [],
                    "imds_blocked": True,
                    "special_iana_blocked": True,
                },
                "env_secrets": ["TOKEN"],
                "read_only_root": True,
                "allow_shell": True,
                "timeouts": {"tool_s": 30, "loop_s": 1200, "lifetime_s": 3600},
            },
        )
        is False
    )
    # ASI01..ASI10 : invariance attaque FR/EN via metamorphic.py
    for asi_id in expected_ids:
        en_tr = TrajectoryResult(
            scenario_id=f"{asi_id}-EN",
            language="en",
            tool_calls=(),
            blocked=True,
            decision=f"DENY_{asi_id}",
            cost_cad=Decimal("0.01"),
            grounded_answer="Blocked",
        )
        fr_tr = TrajectoryResult(
            scenario_id=f"{asi_id}-FR",
            language="fr",
            tool_calls=(),
            blocked=True,
            decision=f"DENY_{asi_id}",
            cost_cad=Decimal("0.01"),
            grounded_answer="Bloque",
        )
        assert (
            verify_metamorphic_pair(
                MetamorphicRelation.BILINGUAL_FR_EN_INJECTION_INVARIANCE,
                en_tr,
                fr_tr,
            ).passed
            is True
        )

    # Validation 2027-B001 couvrant toutes les 10 categories ASI01..ASI10
    adr_schema = json.loads(
        (SCHEMAS_DIR / "adr_2027_b001.schema.json").read_text("utf-8")
    )
    adr_all_asi = {
        "adr_id": "ADR-2027-055",
        "title": "Couverture complete OWASP Agentic Top 10",
        "status": "Accepted",
        "date": "2026-12-02",
        "owners": {
            "architecture_lead": "arch@ent.ca",
            "named_business_owner": "owner@ent.ca",
        },
        "risk_and_autonomy": {
            "autonomy_ceiling": "L3",
            "regulatory_footprint": {
                "bsif_e23_materiality": "High",
                "quebec_law25_automated_decision": False,
                "eu_ai_act_tier": "Art50",
            },
            "owasp_asi_mitigated": expected_ids,
        },
        "technical_invariants": {
            "vertical_protocol": "MCP Streamable HTTP (pinned SHA-256)",
            "horizontal_protocol": "A2A v1.0 via agentgateway",
            "durable_runtime": "Temporal",
            "compensation_strategy": "Saga inverse",
            "max_cost_per_outcome_cad": 0.75,
            "minimum_eval_gate": "pass^5 >= 0.96",
        },
        "fallback_and_killswitch": {
            "degraded_mode": "File manuelle",
            "soc_killswitch_id": "ks-owasp-01",
        },
        "review_trigger": "Trimestrielle",
    }
    assert validate_adr_2027_b001(adr_all_asi, adr_schema) == []
