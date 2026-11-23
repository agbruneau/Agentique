# SPDX-License-Identifier: MIT
"""Suite pytest TDD pour Module 2 : authz_pqc_audit/."""

from __future__ import annotations

import base64
import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
import pytest

from authz_pqc_audit.audit_scitt_focus import (
    AuditChainLedger,
    build_scitt_merkle_tree,
    compute_cpo_and_focus,
    generate_inclusion_proof,
    seal_merkle_root,
    verify_inclusion_proof,
)
from authz_pqc_audit.ciba_approval import (
    IJsonError,
    compute_action_hash_h,
    validate_ijson_strict,
    verify_ciba_approval_tokens,
)
from authz_pqc_audit.obo_dpop import extract_act_chain, validate_obo_delegation
from authz_pqc_audit.otel_pii_mapper import (
    GENAI_DEV_85_ATTRS,
    OtelGenAiMapper,
    map_span_attributes,
    redact_pii_bilingual,
)
from authz_pqc_audit.pqc_http431 import (
    ML_DSA_SPECS,
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
    keygen_slh_dsa_sha2_128s,
    verify_slh_dsa_sha2_128s,
)

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"
EXPECTED_C6_H = (
    "92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81"
)


def _load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMAS_DIR / name).read_text(encoding="utf-8"))


def _sha256_b64url(text: str) -> str:
    digest = hashlib.sha256(text.encode("ascii")).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")


def _sample_c5_claims(*, exp: int = 1793085600) -> dict[str, Any]:
    return {
        "iss": "https://idp.ent.ca",
        "sub": "alice",
        "aud": "https://mcp-finance.ent.ca",
        "client_id": "passerelle-agents",
        "scope": "finance:read",
        "authorization_details": [
            {"type": "lecture_depenses", "periode": "2026-T3"}
        ],
        "act": {
            "sub": "spiffe://ent.ca/agent-analyse-depenses",
            "act": {"sub": "spiffe://ent.ca/agent-orch"},
        },
        "cnf": {"jkt": "jkt-thumbprint-0123456789abcdef"},
        "iat": 1793084712,
        "exp": exp,
        "jti": "3b7e90a1-6c52-4d8e-9a17-c4e05b2f8d66",
    }


def _sample_dpop_proof(
    *,
    htm: str = "POST",
    htu: str = "https://mcp-finance.ent.ca/tools/call",
    access_token: str = "raw.jwt.access",
    jkt: str = "jkt-thumbprint-0123456789abcdef",
    jti: str = "dpop-jti-0001",
) -> dict[str, Any]:
    return {
        "typ": "dpop+jwt",
        "jwk_thumbprint": jkt,
        "htm": htm,
        "htu": htu,
        "ath": _sha256_b64url(access_token),
        "jti": jti,
        "iat": 1793084712,
    }


def _sample_c6_tokens() -> list[dict[str, Any]]:
    details = [
        {
            "type": "https://ent.ca/types/action-agent",
            "locations": [
                "https://passerelle-agents.ent.ca/mcp/approvisionnement"
            ],
            "actions": ["tools/call"],
            "identifier": (
                "mcp-approvisionnement/"
                "approvisionnement_creer_bon_commande@1.4.0"
            ),
            "fournisseur_id": "SUP-004512",
            "centre_cout": "CC-4410",
            "statut_demande": "soumis",
            "lignes": [
                {
                    "sku": "PRD-10442",
                    "quantite": 40,
                    "prix_unitaire_cents": 24960,
                },
                {
                    "sku": "PRD-20817",
                    "quantite": 12,
                    "prix_unitaire_cents": 20800,
                },
            ],
            "grandeur_seuil": {
                "valeur": 1248000,
                "unite": "cents_cad",
                "portee": "task",
            },
        }
    ]
    return [
        {
            "header": {
                "typ": "approbation+jwt",
                "alg": "ES256",
                "kid": "approbation-2026-10",
            },
            "claims": {
                "iss": "https://approbation.ent.ca",
                "aud": "https://passerelle-agents.ent.ca",
                "sub": "apb-5e19c2",
                "approbateur_role": "tiers",
                "iat": 1793093040,
                "exp": 1793093940,
                "jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28",
                "task_id": "tache-7f3c2a",
                "agent_id": "agt-achats-indirects@1.2.0",
                "action_sha256": EXPECTED_C6_H,
                "authorization_details": details,
            },
        },
        {
            "header": {
                "typ": "approbation+jwt",
                "alg": "ES256",
                "kid": "approbation-2026-10",
            },
            "claims": {
                "iss": "https://approbation.ent.ca",
                "aud": "https://passerelle-agents.ent.ca",
                "sub": "apb-91d4e8",
                "approbateur_role": "tiers",
                "iat": 1793093095,
                "exp": 1793093940,
                "jti": "7d4e9b12-3a6c-4e8f-9c01-8b2d6f4a3e19",
                "task_id": "tache-7f3c2a",
                "agent_id": "agt-achats-indirects@1.2.0",
                "action_sha256": EXPECTED_C6_H,
                "authorization_details": details,
            },
        },
    ]


def test_nhi_unique_identity_required() -> None:
    claims = _sample_c5_claims()
    del claims["act"]
    res = validate_obo_delegation(
        claims,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=_sample_dpop_proof(),
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084800,
        access_token="raw.jwt.access",
    )
    assert res.accepted is False
    assert res.rejection_code is not None


def test_no_static_secret_or_passthrough() -> None:
    claims = _sample_c5_claims()
    claims["aud"] = "https://passerelle-agents.ent.ca"
    res = validate_obo_delegation(
        claims,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=_sample_dpop_proof(),
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084800,
        access_token="raw.jwt.access",
    )
    assert res.accepted is False

    # Rejet jeton porteur sans preuve DPoP (aucun secret nu)
    no_pop = validate_obo_delegation(
        _sample_c5_claims(),
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=None,
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084800,
        access_token="raw.jwt.access",
    )
    assert no_pop.accepted is False

    no_cnf_claims = _sample_c5_claims()
    del no_cnf_claims["cnf"]
    no_cnf = validate_obo_delegation(
        no_cnf_claims,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=_sample_dpop_proof(),
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084800,
        access_token="raw.jwt.access",
    )
    assert no_cnf.accepted is False


def test_obo_sub_and_act_chain_max_two_hops() -> None:
    claims = _sample_c5_claims()
    Draft202012Validator(
        _load_schema("delegated_token_claims.schema.json")
    ).validate(claims)
    chain = extract_act_chain(claims)
    assert chain == (
        "spiffe://ent.ca/agent-analyse-depenses",
        "spiffe://ent.ca/agent-orch",
    )

    used_jtis: set[str] = set()
    ok = validate_obo_delegation(
        claims,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=_sample_dpop_proof(),
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084800,
        max_hops=2,
        access_token="raw.jwt.access",
        used_dpop_jtis=used_jtis,
    )
    assert ok.accepted is True
    assert ok.principal_sub == "alice"
    assert ok.hop_count == 2

    # 3 sauts -> refus
    claims_3hops = copy.deepcopy(claims)
    claims_3hops["act"]["act"]["act"] = {"sub": "spiffe://ent.ca/agent-3"}
    bad_3 = validate_obo_delegation(
        claims_3hops,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=_sample_dpop_proof(jti="dpop-jti-0002"),
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084800,
        max_hops=2,
        access_token="raw.jwt.access",
        used_dpop_jtis=used_jtis,
    )
    assert bad_3.accepted is False


def test_reject_token_passthrough() -> None:
    claims = _sample_c5_claims()
    claims["aud"] = "https://autre-service.ent.ca"
    res = validate_obo_delegation(
        claims,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=_sample_dpop_proof(),
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084800,
        access_token="raw.jwt.access",
    )
    assert res.accepted is False


def test_obo_rejects_exp_extension_and_dpop_replay() -> None:
    claims = _sample_c5_claims(exp=1793086500)
    res_exp = validate_obo_delegation(
        claims,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,  # tente de prolonger au-dela du parent
        dpop_proof=_sample_dpop_proof(jti="dpop-jti-exp"),
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084800,
        access_token="raw.jwt.access",
    )
    assert res_exp.accepted is False

    # Rejeu jti DPoP et mauvais ath / htm
    used: set[str] = set()
    valid_claims = _sample_c5_claims()
    proof = _sample_dpop_proof(jti="dpop-replay-1")
    first = validate_obo_delegation(
        valid_claims,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=proof,
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084800,
        access_token="raw.jwt.access",
        used_dpop_jtis=used,
    )
    assert first.accepted is True
    replay = validate_obo_delegation(
        valid_claims,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=proof,
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793084801,
        access_token="raw.jwt.access",
        used_dpop_jtis=used,
    )
    assert replay.accepted is False

    # Rejet jeton expire, mauvais ath, mauvais htm, mauvais htu, cnf divergent
    expired = validate_obo_delegation(
        valid_claims,
        expected_audience="https://mcp-finance.ent.ca",
        parent_exp=1793085600,
        dpop_proof=_sample_dpop_proof(jti="dpop-exp"),
        http_method="POST",
        http_uri="https://mcp-finance.ent.ca/tools/call",
        now_ts=1793085601,
        access_token="raw.jwt.access",
    )
    assert expired.accepted is False

    bad_ath = _sample_dpop_proof(jti="dpop-ath", access_token="autre.jwt")
    assert (
        validate_obo_delegation(
            valid_claims,
            expected_audience="https://mcp-finance.ent.ca",
            parent_exp=1793085600,
            dpop_proof=bad_ath,
            http_method="POST",
            http_uri="https://mcp-finance.ent.ca/tools/call",
            now_ts=1793084800,
            access_token="raw.jwt.access",
        ).accepted
        is False
    )
    bad_htm = _sample_dpop_proof(jti="dpop-htm", htm="GET")
    assert (
        validate_obo_delegation(
            valid_claims,
            expected_audience="https://mcp-finance.ent.ca",
            parent_exp=1793085600,
            dpop_proof=bad_htm,
            http_method="POST",
            http_uri="https://mcp-finance.ent.ca/tools/call",
            now_ts=1793084800,
            access_token="raw.jwt.access",
        ).accepted
        is False
    )
    bad_htu = _sample_dpop_proof(
        jti="dpop-htu", htu="https://evil.example/call"
    )
    assert (
        validate_obo_delegation(
            valid_claims,
            expected_audience="https://mcp-finance.ent.ca",
            parent_exp=1793085600,
            dpop_proof=bad_htu,
            http_method="POST",
            http_uri="https://mcp-finance.ent.ca/tools/call",
            now_ts=1793084800,
            access_token="raw.jwt.access",
        ).accepted
        is False
    )
    bad_jkt = _sample_dpop_proof(jti="dpop-jkt", jkt="autre-thumbprint")
    assert (
        validate_obo_delegation(
            valid_claims,
            expected_audience="https://mcp-finance.ent.ca",
            parent_exp=1793085600,
            dpop_proof=bad_jkt,
            http_method="POST",
            http_uri="https://mcp-finance.ent.ca/tools/call",
            now_ts=1793084800,
            access_token="raw.jwt.access",
        ).accepted
        is False
    )


def test_spiffe_nhi_lifecycle_and_revocation() -> None:
    fsm = RevocationStateMachine()
    spiffe = "spiffe://ent.ca/agt-achats-indirects"
    assert fsm.get_state(spiffe) == AgentAuthState.ACTIVE
    assert fsm.assert_active(spiffe, "jti-1", 1793084800) is True

    fsm.apply_event(
        CaepRevocationEvent(
            event_id="evt-1",
            spec_source="SSF_CAEP_FINAL",
            subject_spiffe=spiffe,
            jti="jti-1",
            issued_at=1793084805,
            reason="anomalie_temporaire",
            action="SUSPEND",
        )
    )
    assert fsm.get_state(spiffe) == AgentAuthState.SUSPENDED
    assert fsm.assert_active(spiffe, "jti-1", 1793084806) is False

    fsm.apply_event(
        CaepRevocationEvent(
            event_id="evt-2",
            spec_source="SSF_CAEP_FINAL",
            subject_spiffe=spiffe,
            jti=None,
            issued_at=1793084810,
            reason="rehabilitation",
            action="REINSTATE",
        )
    )
    assert fsm.get_state(spiffe) == AgentAuthState.ACTIVE


def test_soc_killswitch_caep_revocation_terminal() -> None:
    fsm = RevocationStateMachine()
    spiffe = "spiffe://ent.ca/agt-compromis"
    fsm.apply_event(
        CaepRevocationEvent(
            event_id="evt-kill",
            spec_source="IETF_INDIVIDUAL_DRAFT_AGENT_REVOCATION_01",
            subject_spiffe=spiffe,
            jti="jti-kill",
            issued_at=1793084900,
            reason="soc_killswitch",
            action="REVOKE",
        )
    )
    assert fsm.get_state(spiffe) == AgentAuthState.REVOKED
    assert fsm.assert_active(spiffe, "jti-kill", 1793084901) is False

    # REVOKED est terminal : la rehabilitation doit echouer
    fsm.apply_event(
        CaepRevocationEvent(
            event_id="evt-try-reinstate",
            spec_source="SSF_CAEP_FINAL",
            subject_spiffe=spiffe,
            jti=None,
            issued_at=1793084905,
            reason="tentative_retour",
            action="REINSTATE",
        )
    )
    assert fsm.get_state(spiffe) == AgentAuthState.REVOKED


def test_ciba_c6_action_hash_exact_match() -> None:
    arguments = {
        "centre_cout": "CC-4410",
        "fournisseur_id": "SUP-004512",
        "idempotency_key": (
            "80351869ca990c86c8c6a314a7ac23d80b509a03f9a11dd173d2f1112c10eca7"
        ),
        "lignes": [
            {"prix_unitaire_cents": 24960, "quantite": 40, "sku": "PRD-10442"},
            {"prix_unitaire_cents": 20800, "quantite": 12, "sku": "PRD-20817"},
        ],
        "statut_demande": "soumis",
    }
    h = compute_action_hash_h(
        outil="mcp-approvisionnement/approvisionnement_creer_bon_commande",
        version="1.4.0",
        definition_digest=(
            "sha256:"
            "e8c1ccd755dd196d40fb358447998a964dd643fa03614e9e8fbbfa66abf643b6"
        ),
        agent_id="agt-achats-indirects@1.2.0",
        task_id="tache-7f3c2a",
        arguments=arguments,
    )
    assert h == EXPECTED_C6_H


def test_reject_self_approval_by_principal_sub() -> None:
    tokens = _sample_c6_tokens()
    tokens[0]["claims"]["sub"] = "alice"
    verdict = verify_ciba_approval_tokens(
        tokens,
        expected_h=EXPECTED_C6_H,
        expected_task_id="tache-7f3c2a",
        expected_agent_id="agt-achats-indirects@1.2.0",
        principal_sub="alice",
        required_approvers=2,
        now_ts=1793093100,
    )
    assert verdict.approved is False


def test_ciba_approval_token_valid_and_single_use() -> None:
    schema = _load_schema("approval_token_c6.schema.json")
    tokens = _sample_c6_tokens()
    for tok in tokens:
        Draft202012Validator(schema).validate(tok)

    consumed: set[str] = set()
    verdict = verify_ciba_approval_tokens(
        tokens,
        expected_h=EXPECTED_C6_H,
        expected_task_id="tache-7f3c2a",
        expected_agent_id="agt-achats-indirects@1.2.0",
        principal_sub="alice",
        required_approvers=2,
        now_ts=1793093100,
        consumed_jtis=consumed,
    )
    assert verdict.approved is True
    assert verdict.approver_subs == ("apb-5e19c2", "apb-91d4e8")

    # Reutilisation jti interdite (usage unique)
    replay = verify_ciba_approval_tokens(
        tokens,
        expected_h=EXPECTED_C6_H,
        expected_task_id="tache-7f3c2a",
        expected_agent_id="agt-achats-indirects@1.2.0",
        principal_sub="alice",
        required_approvers=2,
        now_ts=1793093101,
        consumed_jtis=consumed,
    )
    assert replay.approved is False

    # Confusion typ == at+jwt interdite
    bad_typ = copy.deepcopy(tokens)
    bad_typ[0]["header"]["typ"] = "at+jwt"
    verdict_typ = verify_ciba_approval_tokens(
        bad_typ,
        expected_h=EXPECTED_C6_H,
        expected_task_id="tache-7f3c2a",
        expected_agent_id="agt-achats-indirects@1.2.0",
        principal_sub="alice",
        required_approvers=2,
        now_ts=1793093100,
        consumed_jtis=set(),
    )
    assert verdict_typ.approved is False

    # Rejet : jeton expire, mauvais action_sha256, doublon d'approbateur, tache
    expired_toks = copy.deepcopy(tokens)
    assert (
        verify_ciba_approval_tokens(
            expired_toks,
            expected_h=EXPECTED_C6_H,
            expected_task_id="tache-7f3c2a",
            expected_agent_id="agt-achats-indirects@1.2.0",
            principal_sub="alice",
            required_approvers=2,
            now_ts=1793093941,
            consumed_jtis=set(),
        ).approved
        is False
    )
    bad_hash = copy.deepcopy(tokens)
    bad_hash[1]["claims"]["action_sha256"] = "0" * 64
    assert (
        verify_ciba_approval_tokens(
            bad_hash,
            expected_h=EXPECTED_C6_H,
            expected_task_id="tache-7f3c2a",
            expected_agent_id="agt-achats-indirects@1.2.0",
            principal_sub="alice",
            required_approvers=2,
            now_ts=1793093100,
            consumed_jtis=set(),
        ).approved
        is False
    )
    dup_approver = copy.deepcopy(tokens)
    dup_approver[1]["claims"]["sub"] = dup_approver[0]["claims"]["sub"]
    assert (
        verify_ciba_approval_tokens(
            dup_approver,
            expected_h=EXPECTED_C6_H,
            expected_task_id="tache-7f3c2a",
            expected_agent_id="agt-achats-indirects@1.2.0",
            principal_sub="alice",
            required_approvers=2,
            now_ts=1793093100,
            consumed_jtis=set(),
        ).approved
        is False
    )
    assert (
        verify_ciba_approval_tokens(
            copy.deepcopy(tokens),
            expected_h=EXPECTED_C6_H,
            expected_task_id="autre-tache",
            expected_agent_id="agt-achats-indirects@1.2.0",
            principal_sub="alice",
            required_approvers=2,
            now_ts=1793093100,
            consumed_jtis=set(),
        ).approved
        is False
    )


def test_ciba_ijson_rejects_float_nan_and_surrogates() -> None:
    validate_ijson_strict({"montant_cents": 1248000, "lignes": [{"q": 40}]})
    with pytest.raises(IJsonError):
        validate_ijson_strict({"montant": 12.34})
    with pytest.raises(IJsonError):
        validate_ijson_strict({"val": float("nan")})
    with pytest.raises(IJsonError):
        validate_ijson_strict({"val": float("inf")})
    with pytest.raises(IJsonError):
        validate_ijson_strict({"val": "\ud800"})
    with pytest.raises(IJsonError):
        validate_ijson_strict({"big": 2**53})


def test_pqc_http431_vs_transaction_token_o1() -> None:
    assert ML_DSA_SPECS["ML-DSA-65"] == {"sig_bytes": 3309, "pk_bytes": 1952}
    assert ML_DSA_SPECS["ML-DSA-87"] == {"sig_bytes": 4627, "pk_bytes": 2592}

    for alg in ("ML-DSA-65", "ML-DSA-87"):
        m_jwk_h1 = evaluate_http_431(alg, PqcProfile.JWT_EMBEDDED_JWK, hops=1)
        assert m_jwk_h1.header_bytes > 8192
        assert m_jwk_h1.exceeds_limit is True
        assert m_jwk_h1.http_status == 431

        m_kid_h2 = evaluate_http_431(alg, PqcProfile.JWT_KID_REF, hops=2)
        assert m_kid_h2.header_bytes > 8192
        assert m_kid_h2.http_status == 431

        m_cose_h2 = evaluate_http_431(alg, PqcProfile.CBOR_COSE_CWT, hops=2)
        assert m_cose_h2.header_bytes > 8192
        assert m_cose_h2.http_status == 431

        m_x5c_h1 = evaluate_http_431(alg, PqcProfile.JWT_X5C_CHAIN, hops=1)
        assert m_x5c_h1.header_bytes > 8192
        assert m_x5c_h1.http_status == 431

        sizes = []
        for hop in range(1, 6):
            tx = evaluate_http_431(
                alg, PqcProfile.TRANSACTION_TOKEN_CBOR, hops=hop
            )
            assert tx.header_bytes < 8192
            assert tx.exceeds_limit is False
            assert tx.http_status == 200
            sizes.append(tx.header_bytes)
        assert max(sizes) - min(sizes) == 0  # strictement O(1)

    tx_jwt = evaluate_http_431(
        "ML-DSA-65", PqcProfile.TRANSACTION_TOKEN_JWT, hops=2
    )
    assert tx_jwt.header_bytes < 8192
    assert tx_jwt.http_status == 200

    frame = build_signed_delegation_frame(
        "ML-DSA-65",
        PqcProfile.TRANSACTION_TOKEN_CBOR,
        hops=3,
        claims={"sub": "alice", "task_id": "t-1"},
    )
    assert isinstance(frame, bytes) and len(frame) > 3309


def test_otel_v141_to_genai_dev_cache_write_and_join() -> None:
    assert len(GENAI_DEV_85_ATTRS) == 85
    raw = {
        "gen_ai.system": "anthropic",
        "gen_ai.usage.cache_creation.input_tokens": 128,
        "gen_ai.client.token.usage": 512,
        "gen_ai.request.model": "claude-haiku-5.5",
        "ca.entreprise.task_id": "tache-7f3c2a",
        "ca.entreprise.autonomy_level": "L3",
        "ca.entreprise.approval.jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28",
        "ca.entreprise.cost_center": "CC-4410",
        "ca.entreprise.approver_sub": "apb-5e19c2",
    }
    mapped = map_span_attributes(raw, target_dialect="genai_dev")
    assert mapped["gen_ai.provider.name"] == "anthropic"
    assert mapped["gen_ai.usage.cache_write.input_tokens"] == 128
    assert mapped["gen_ai.client.inference.usage.input_tokens"] == 512
    assert "ca.entreprise.approver_sub" not in mapped

    mapper = OtelGenAiMapper()
    assert mapper.map_attributes(raw)["gen_ai.provider.name"] == "anthropic"

    # Absence de cle de jointure trace <-> mandat (lacune 21) -> rejet
    missing_join = dict(raw)
    del missing_join["ca.entreprise.approval.jti"]
    with pytest.raises(ValueError):
        map_span_attributes(missing_join, target_dialect="genai_dev")


def test_otel_rejects_generic_enterprise_prefix() -> None:
    raw = {
        "enterprise.tenant": "finance",
        "otel.internal_flag": True,
        "ca.entreprise.task_id": "tache-1",
        "ca.entreprise.autonomy_level": "L2",
        "ca.entreprise.approval.jti": "jti-1",
        "ca.entreprise.cost_center": "CC-1000",
    }
    with pytest.raises(ValueError):
        map_span_attributes(raw, target_dialect="genai_dev")


def test_otel_drops_raw_prompt_and_tool_payloads() -> None:
    raw = {
        "gen_ai.input.messages": [{"role": "user", "content": "secret"}],
        "gen_ai.output.messages": [{"role": "assistant", "content": "ok"}],
        "gen_ai.system_instructions": "Ne rien divulguer",
        "gen_ai.tool.call.arguments": {"nas": "123-456-789"},
        "gen_ai.tool.call.result": {"balance": 50000},
        "gen_ai.request.model": "modele-compact",
        "ca.entreprise.task_id": "tache-1",
        "ca.entreprise.autonomy_level": "L2",
        "ca.entreprise.approval.jti": "jti-1",
        "ca.entreprise.cost_center": "CC-1000",
    }
    mapped = map_span_attributes(raw, target_dialect="genai_dev")
    for forbidden in (
        "gen_ai.input.messages",
        "gen_ai.output.messages",
        "gen_ai.system_instructions",
        "gen_ai.tool.call.arguments",
        "gen_ai.tool.call.result",
    ):
        assert forbidden not in mapped


def test_otel_pii_redaction_and_closed_allowlist() -> None:
    raw = {
        "gen_ai.request.model": "modele-compact",
        "custom.unapproved.attr": "should_drop",
        "ca.entreprise.task_id": "tache-2",
        "ca.entreprise.autonomy_level": "L2",
        "ca.entreprise.approval.jti": "jti-2",
        "ca.entreprise.cost_center": "CC-4410",
    }
    mapped = map_span_attributes(raw, target_dialect="genai_dev")
    assert "custom.unapproved.attr" not in mapped
    assert mapped["gen_ai.request.model"] == "modele-compact"


def test_pii_redaction_bilingual_and_drop_raw_content() -> None:
    key = b"trousse-hmac-secret-key-2026-12"
    text_fr = (
        "Client NAS 123-456-789, RAMQ DUPJ 8405 1201, courriel "
        "jean.dupont@ent.ca, tel +1-514-555-0199, IBAN "
        "FR7630006000011234567890189, carte 4532-0155-8812-3456, "
        "Bearer eyJhbGciOiJFUzI1NiJ9.payload.sig"
    )
    redacted_fr, cats_fr = redact_pii_bilingual(text_fr, key)
    for raw_val in (
        "123-456-789",
        "DUPJ 8405 1201",
        "jean.dupont@ent.ca",
        "514-555-0199",
        "FR7630006000011234567890189",
        "4532-0155-8812-3456",
        "eyJhbGciOiJFUzI1NiJ9",
    ):
        assert raw_val not in redacted_fr
    assert len(cats_fr) >= 6

    text_en = "SIN 987 654 321 phone +33 1 42 68 55 00 email a.b@corp.com"
    redacted_en, cats_en = redact_pii_bilingual(text_en, key)
    assert "987 654 321" not in redacted_en
    assert "a.b@corp.com" not in redacted_en
    assert len(cats_en) >= 3

    # Pseudonymisation deterministe par HMAC-SHA256 et sensibilite a la cle
    redacted_fr_2, _ = redact_pii_bilingual(text_fr, key)
    redacted_fr_other, _ = redact_pii_bilingual(
        text_fr, b"autre-cle-hmac-2026"
    )
    assert redacted_fr == redacted_fr_2
    assert redacted_fr != redacted_fr_other


def test_c8_five_element_canonized_record() -> None:
    schema = _load_schema("audit_record_c8.schema.json")
    ledger = AuditChainLedger(flux="passerelle-agents-03")
    payload = {
        "action": {
            "arguments_sha256": "c" * 64,
            "definition_sha256": "sha256:" + "e" * 64,
            "definition_version": "1.4.0",
            "issue": "succes",
            "outil": "mcp-approvisionnement/creer_bon",
            "palier": "P2",
            "reference_resultat": "BC-2026-118734",
        },
        "agent": {
            "id": "agt-achats-indirects",
            "identite": "spiffe://ent.ca/agt-achats-indirects",
            "invite_systeme": "sha256:" + "4" * 64,
            "version": "1.2.0",
        },
        "autorite": {
            "approbations": [
                {
                    "approbateur": "apb-5e19c2",
                    "jti": "c2f7a1d4-8e3b-4f6a-b0d9-5a1e7c3f9b28",
                    "role": "tiers",
                }
            ],
            "classe_risque": "moderee",
            "controle": "approbation_requise_au_dela_du_seuil",
            "empreinte_approbation": EXPECTED_C6_H,
            "grandeur_seuil": 1248000,
            "niveau_autonomie": "N3",
            "version_politique": "politiques-passerelle@2026.10.3",
        },
        "correlation": {
            "cle_idempotence": "8" * 64,
            "etape": "etape-03/creer-bon#1",
            "span_id": "b7ad6b7169203331",
            "tache": "tache-7f3c2a",
            "trace_id": "0af7651916cd43dd8448eb211c80319c",
        },
        "horodatage": "2026-10-27T09:26:03.412Z",
        "intention_sequence": 1,
        "mandant": {
            "jeton_delegue_jti": "4e8b2c71-0d93-4a6f-9b15-7c2e8f40a6d3",
            "pseudonyme": "u-58c1d7",
            "type": "user",
        },
        "modele": {
            "fournisseur": "fournisseur-local",
            "servi": "modele-compact",
            "version": "2026-08-14",
        },
        "nature": "issue",
    }
    rec = ledger.append_record(payload)
    Draft202012Validator(schema).validate(rec)
    assert rec["enregistrement"]["sequence"] == 1
    assert rec["empreinte"].startswith("sha256:")


def test_audit_chain_jcs_and_scitt_merkle_seal() -> None:
    ledger = AuditChainLedger(flux="flux-test")
    base = {
        "action": {
            "arguments_sha256": "a" * 64,
            "definition_sha256": "sha256:" + "b" * 64,
            "definition_version": "1.0.0",
            "issue": "succes",
            "outil": "outil-test",
            "palier": "P1",
            "reference_resultat": "RES-1",
        },
        "agent": {
            "id": "agt-1",
            "identite": "spiffe://ent.ca/agt-1",
            "invite_systeme": "sha256:" + "1" * 64,
            "version": "1.0.0",
        },
        "autorite": {
            "approbations": [],
            "classe_risque": "faible",
            "controle": "autonome",
            "empreinte_approbation": None,
            "grandeur_seuil": 0,
            "niveau_autonomie": "N2",
            "version_politique": "v1",
        },
        "correlation": {
            "cle_idempotence": "2" * 64,
            "etape": "etape-1",
            "span_id": "span-1",
            "tache": "tache-1",
            "trace_id": "trace-1",
        },
        "horodatage": "2026-10-27T10:00:00Z",
        "intention_sequence": 0,
        "mandant": {
            "jeton_delegue_jti": "jti-deleg-1",
            "pseudonyme": "u-1",
            "type": "user",
        },
        "modele": {
            "fournisseur": "local",
            "servi": "compact",
            "version": "1.0",
        },
        "nature": "intention",
    }
    r1 = ledger.append_record(copy.deepcopy(base))
    r2 = ledger.append_record(copy.deepcopy(base))
    assert r2["enregistrement"]["precedent_sha256"] == r1["empreinte"]
    assert ledger.verify_chain([r1, r2]).valid is True


def test_audit_chain_tamper_detection() -> None:
    ledger = AuditChainLedger(flux="flux-tamper")
    rec_base = {
        "action": {
            "arguments_sha256": "a" * 64,
            "definition_sha256": "sha256:" + "b" * 64,
            "definition_version": "1.0.0",
            "issue": "succes",
            "outil": "outil-test",
            "palier": "P1",
            "reference_resultat": "RES-1",
        },
        "agent": {
            "id": "agt-1",
            "identite": "spiffe://ent.ca/agt-1",
            "invite_systeme": "sha256:" + "1" * 64,
            "version": "1.0.0",
        },
        "autorite": {
            "approbations": [],
            "classe_risque": "faible",
            "controle": "autonome",
            "empreinte_approbation": None,
            "grandeur_seuil": 0,
            "niveau_autonomie": "N2",
            "version_politique": "v1",
        },
        "correlation": {
            "cle_idempotence": "2" * 64,
            "etape": "etape-1",
            "span_id": "span-1",
            "tache": "tache-1",
            "trace_id": "trace-1",
        },
        "horodatage": "2026-10-27T10:00:00Z",
        "intention_sequence": 0,
        "mandant": {
            "jeton_delegue_jti": "jti-deleg-1",
            "pseudonyme": "u-1",
            "type": "user",
        },
        "modele": {"fournisseur": "local", "servi": "compact", "version": "1"},
        "nature": "intention",
    }
    r1 = ledger.append_record(copy.deepcopy(rec_base))
    r2 = ledger.append_record(copy.deepcopy(rec_base))
    tampered = copy.deepcopy([r1, r2])
    tampered[0]["enregistrement"]["action"]["reference_resultat"] = "MODIFIE"
    verdict = ledger.verify_chain(tampered)
    assert verdict.valid is False
    assert verdict.broken_sequence == 1

    # Alteration directe du maillon precedent_sha256 -> rupture sequence 2
    broken_link = copy.deepcopy([r1, r2])
    broken_link[1]["enregistrement"]["precedent_sha256"] = "sha256:" + "f" * 64
    v_link = ledger.verify_chain(broken_link)
    assert v_link.valid is False
    assert v_link.broken_sequence == 2


def test_scitt_merkle_inclusion_and_slh_dsa_seal() -> None:
    with pytest.raises(ValueError):
        build_scitt_merkle_tree([])

    single = [hashlib.sha256(b"single").digest()]
    t_single = build_scitt_merkle_tree(single)
    p_single = generate_inclusion_proof(t_single, 0)
    assert (
        verify_inclusion_proof(single[0], p_single, t_single.root_hash, 0, 1)
        is True
    )

    leaves = [hashlib.sha256(f"leaf-{i}".encode()).digest() for i in range(5)]
    tree = build_scitt_merkle_tree(leaves)
    for idx in range(5):
        proof_i = generate_inclusion_proof(tree, idx)
        assert (
            verify_inclusion_proof(leaves[idx], proof_i, tree.root_hash, idx, 5)
            is True
        )
    proof = generate_inclusion_proof(tree, 2)
    assert (
        verify_inclusion_proof(leaves[3], proof, tree.root_hash, 2, 5) is False
    )
    assert (
        verify_inclusion_proof(leaves[2], proof, b"\x00" * 32, 2, 5) is False
    )

    pk, sk = keygen_slh_dsa_sha2_128s(
        bytes.fromhex("173D04C938C1C36BF289C3C022D04B14"),
        bytes.fromhex("63AE23C41AA546DA589774AC20B745C4"),
        bytes.fromhex("0D794777914C99766827F0F09CA972BE"),
    )
    seal = seal_merkle_root(tree.root_hash, sk)
    assert seal["alg"] == "SLH-DSA-SHA2-128s"
    assert seal["root_hash_hex"] == tree.root_hash.hex()
    assert (
        verify_slh_dsa_sha2_128s(pk, tree.root_hash, seal["signature"]) is True
    )


def test_focus_cpo_and_budget_ceiling_decimal() -> None:
    records = [
        {
            "BillingAccountId": "ACC-FIN-01",
            "ChargePeriodStart": "2026-10-27T09:00:00Z",
            "ChargePeriodEnd": "2026-10-27T10:00:00Z",
            "ProviderName": "PasserelleModele",
            "ServiceName": "InferenceCompact",
            "ResourceId": "agt-achats-indirects",
            "BilledCost": "0.10",
            "EffectiveCost": "0.10",
            "ConsumedQuantity": "1000",
            "ConsumedUnit": "Tokens",
            "PricingCurrency": "CAD",
            "x_carbon_gco2e": "0.42",
            "x_energy_kwh": "0.0012",
        },
        {
            "BillingAccountId": "ACC-FIN-01",
            "ChargePeriodStart": "2026-10-27T09:00:00Z",
            "ChargePeriodEnd": "2026-10-27T10:00:00Z",
            "ProviderName": "PasserelleModele",
            "ServiceName": "InferenceCompact",
            "ResourceId": "agt-achats-indirects",
            "BilledCost": "0.20",
            "EffectiveCost": "0.20",
            "ConsumedQuantity": "2000",
            "ConsumedUnit": "Tokens",
            "PricingCurrency": "CAD",
            "x_carbon_gco2e": "0.84",
            "x_energy_kwh": "0.0024",
        },
    ]
    summary = compute_cpo_and_focus(records, compliant_outcomes=2)
    assert summary.total_effective_cost_cad == Decimal("0.30")
    assert summary.cpo_cad == Decimal("0.15")

    with pytest.raises(ValueError):
        compute_cpo_and_focus(records, compliant_outcomes=0)


def test_focus_carbon_cap046_fields() -> None:
    schema = _load_schema("focus_carbon_record.schema.json")
    rec = {
        "BillingAccountId": "ACC-FIN-01",
        "ChargePeriodStart": "2026-10-27T09:00:00Z",
        "ChargePeriodEnd": "2026-10-27T10:00:00Z",
        "ProviderName": "PasserelleModele",
        "ServiceName": "InferenceCompact",
        "ResourceId": "agt-achats-indirects",
        "BilledCost": "0.52",
        "EffectiveCost": "0.52",
        "ConsumedQuantity": "41200",
        "ConsumedUnit": "Tokens",
        "PricingCurrency": "CAD",
        "x_carbon_gco2e": "1.75",
        "x_energy_kwh": "0.0050",
    }
    Draft202012Validator(schema).validate(rec)
    summary = compute_cpo_and_focus([rec], compliant_outcomes=1)
    assert summary.total_carbon_gco2e == Decimal("1.75")
    assert summary.total_energy_kwh == Decimal("0.0050")
    for out_rec in summary.focus_records:
        Draft202012Validator(schema).validate(out_rec)
