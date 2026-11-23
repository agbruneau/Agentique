# SPDX-License-Identifier: MIT
"""Suite pytest TDD pour Module 1 : harness_proto/."""

from __future__ import annotations

import base64
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import (
    decode_dss_signature,
)
from jsonschema import Draft202012Validator
import pytest

from harness_proto.a2a_card import AgentCardAdapter, validate_agent_card
from harness_proto.jcs import canonicalize_jcs, jcs_sha256_hex
from harness_proto.mcp_pinning import (
    DeprecatedTransportError,
    HeaderMismatchError,
    McpCatalogEntry,
    StreamableHttpAdapter,
    compute_tool_definition_digest,
    validate_mcp_headers,
    verify_tools_list_against_catalog,
)
from harness_proto.pipeline import (
    DeterministicHarness,
    HarnessConfig,
    StepStatus,
    validate_strict_schema,
)

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"


def _load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMAS_DIR / name).read_text(encoding="utf-8"))


def _b64u(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _sample_tool_def() -> dict[str, Any]:
    return {
        "name": "approvisionnement_creer_bon_commande",
        "title": "Creer un bon de commande",
        "description": "Cree un bon brouillon ou soumis dans ERP.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["idempotency_key", "centre_cout"],
            "properties": {
                "idempotency_key": {"type": "string"},
                "centre_cout": {
                    "type": "string",
                    "x-mcp-header": "Cost-Center",
                },
            },
        },
        "annotations": {
            "readOnlyHint": False,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    }


def _sign_agent_card(
    card_without_sig: dict[str, Any],
    *,
    kid: str = "cartes-agents-2026-10",
    jku: str = "https://cles.ent.ca/a2a/jwks.json",
) -> tuple[dict[str, Any], dict[str, Any]]:
    priv = ec.generate_private_key(ec.SECP256R1())
    pub_nums = priv.public_key().public_numbers()
    jwk = {
        "kty": "EC",
        "crv": "P-256",
        "kid": kid,
        "alg": "ES256",
        "use": "sig",
        "x": _b64u(pub_nums.x.to_bytes(32, "big")),
        "y": _b64u(pub_nums.y.to_bytes(32, "big")),
    }
    protected_obj = {"alg": "ES256", "typ": "JOSE", "kid": kid, "jku": jku}
    protected_b64 = _b64u(
        json.dumps(protected_obj, separators=(",", ":")).encode("utf-8")
    )
    payload_bytes = canonicalize_jcs(card_without_sig)
    signing_input = f"{protected_b64}.{_b64u(payload_bytes)}".encode("ascii")
    der_sig = priv.sign(signing_input, ec.ECDSA(hashes.SHA256()))
    r_val, s_val = decode_dss_signature(der_sig)
    raw_sig = r_val.to_bytes(32, "big") + s_val.to_bytes(32, "big")
    signed_card = copy.deepcopy(card_without_sig)
    signed_card["signatures"] = [
        {"protected": protected_b64, "signature": _b64u(raw_sig)}
    ]
    return signed_card, {"keys": [jwk]}


def _sample_card_base() -> dict[str, Any]:
    return {
        "name": "Agent risque credit",
        "description": "Analyse prudentielle selon politique CR-12.",
        "supportedInterfaces": [
            {
                "url": "https://passerelle-agents.ent.ca/a2a/risque-credit",
                "protocolBinding": "JSONRPC",
                "protocolVersion": "1.0",
            }
        ],
        "provider": {
            "organization": "Direction Gestion des risques",
            "url": "https://intranet.ent.ca/risque-credit",
        },
        "version": "2.3.0",
        "capabilities": {
            "streaming": True,
            "pushNotifications": True,
            "extendedAgentCard": True,
            "extensions": [
                {
                    "uri": "https://ent.ca/a2a/extensions/gouvernance/v1",
                    "description": "Niveau d'autonomie et classe de risque.",
                    "required": False,
                    "params": {"niveau_autonomie": "N2"},
                }
            ],
        },
        "securitySchemes": {
            "idp-entreprise": {
                "openIdConnectSecurityScheme": {
                    "openIdConnectUrl": (
                        "https://idp.ent.ca/.well-known/openid-configuration"
                    )
                }
            }
        },
        "securityRequirements": [
            {"schemes": {"idp-entreprise": {"list": ["risque-credit:invoke"]}}}
        ],
        "defaultInputModes": ["application/json"],
        "defaultOutputModes": ["application/json"],
        "skills": [
            {
                "id": "analyse-dossier-commercial",
                "name": "Analyse prudentielle",
                "description": "Evalue la solvabilite client.",
                "tags": ["credit", "risque"],
                "examples": ["Analyser le dossier 8841"],
                "securityRequirements": [
                    {
                        "schemes": {
                            "idp-entreprise": {
                                "list": ["risque-credit:analyze"]
                            }
                        }
                    }
                ],
            }
        ],
    }


def test_harness_enforces_schema_and_grounding() -> None:
    cfg = HarnessConfig(
        schema_path=SCHEMAS_DIR / "harness_extraction.schema.json",
        max_repair_retries=2,
        allowed_grounding_ids=frozenset({"DOS-2026"}),
    )

    def adapter(_ctx: dict[str, Any], _errs: list[str]) -> dict[str, Any]:
        return {
            "statut_analyse": "EXTRAIT",
            "categorie_sinistre": "degat_eau",
            "montant_reclame_cents": 124800,
            "reference_dossier": "DOS-2026",
            "motif_escalade": None,
        }

    harness = DeterministicHarness(cfg, adapter)
    outcome = harness.run(
        {"reference_dossier": "DOS-2026", "texte": "Facture 1248,00 CAD"},
        {"DOS-2026": {"max_montant_cents": 500000}},
    )
    assert outcome.status == StepStatus.OK
    assert outcome.validated_payload is not None
    assert outcome.validated_payload["reference_dossier"] == "DOS-2026"
    assert len(outcome.step_trace) == 8
    assert len(outcome.output_sha256) == 64

    # Echec si reference hors grounding_records
    bad_grounding = DeterministicHarness(
        cfg,
        lambda _c, _e: {
            "statut_analyse": "EXTRAIT",
            "categorie_sinistre": "degat_eau",
            "montant_reclame_cents": 124800,
            "reference_dossier": "DOS-9999",
            "motif_escalade": None,
        },
    )
    bad_out = bad_grounding.run(
        {"reference_dossier": "DOS-2026", "texte": "Facture"},
        {"DOS-2026": {"max_montant_cents": 500000}},
    )
    assert bad_out.status in {
        StepStatus.VALIDATION_FAILED,
        StepStatus.ESCALADED,
    }

    # Etape 2 : raw_input invalide -> VALIDATION_FAILED
    bad_in = harness.run({}, {"DOS-2026": {"max_montant_cents": 500000}})
    assert bad_in.status == StepStatus.VALIDATION_FAILED


def test_harness_partition_80_20_rules_outside_prompt() -> None:
    cfg = HarnessConfig(
        schema_path=SCHEMAS_DIR / "harness_extraction.schema.json",
        max_repair_retries=2,
        allowed_grounding_ids=frozenset({"DOS-1001"}),
    )
    # Le modele tente d'extraire un montant depassant la piece
    harness = DeterministicHarness(
        cfg,
        lambda _c, _e: {
            "statut_analyse": "EXTRAIT",
            "categorie_sinistre": "incendie",
            "montant_reclame_cents": 999999,
            "reference_dossier": "DOS-1001",
            "motif_escalade": None,
        },
    )
    outcome = harness.run(
        {"reference_dossier": "DOS-1001", "texte": "Demande"},
        {"DOS-1001": {"max_montant_cents": 100000}},
    )
    assert outcome.status in {
        StepStatus.ESCALADED,
        StepStatus.VALIDATION_FAILED,
        StepStatus.AMBIGU_ESCALADE,
    }


def test_strict_json_schema_2020_12() -> None:
    schema = _load_schema("harness_extraction.schema.json")
    valid = {
        "statut_analyse": "EXTRAIT",
        "categorie_sinistre": "bris_glace",
        "montant_reclame_cents": 45000,
        "reference_dossier": "DOS-4410",
        "motif_escalade": None,
    }
    assert validate_strict_schema(schema, valid) == []

    with_extra = {**valid, "champ_non_declare": 1}
    assert len(validate_strict_schema(schema, with_extra)) >= 1

    for bad_schema in (
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "additionalProperties": True,
            "required": ["a"],
            "properties": {"a": {"type": "string"}},
        },
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "additionalProperties": False,
            "required": ["nested"],
            "properties": {
                "nested": {
                    "type": "object",
                    "required": ["x"],
                    "properties": {"x": {"type": "string"}},
                }
            },
        },
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "additionalProperties": False,
            "required": [],
            "properties": {"a": {"type": "string"}},
        },
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "additionalProperties": False,
            "required": ["a"],
            "properties": {"a": {"type": "string"}},
            "if": {"properties": {"a": {"const": "x"}}},
            "then": {"required": ["a"]},
        },
    ):
        assert len(validate_strict_schema(bad_schema, {"a": "ok"})) >= 1


def test_reject_external_network_schema_ref() -> None:
    bad_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": ["id"],
        "properties": {
            "id": {"$ref": "https://attacker.example/ssrf.schema.json"}
        },
    }
    errs = validate_strict_schema(bad_schema, {"id": "123"})
    assert any("http" in e.lower() or "ref" in e.lower() for e in errs)


def test_harness_8_steps_ok_and_ambigu_escalade() -> None:
    cfg = HarnessConfig(
        schema_path=SCHEMAS_DIR / "harness_extraction.schema.json",
        max_repair_retries=2,
        allowed_grounding_ids=frozenset({"DOS-7777"}),
    )
    ambigu = DeterministicHarness(
        cfg,
        lambda _c, _e: {
            "statut_analyse": "AMBIGU_ESCALADE",
            "categorie_sinistre": "non_determine",
            "montant_reclame_cents": None,
            "reference_dossier": "DOS-7777",
            "motif_escalade": "Deux montants contradictoires sur la facture.",
        },
    )
    res = ambigu.run(
        {"reference_dossier": "DOS-7777", "texte": "500$ ou 900$"},
        {"DOS-7777": {"max_montant_cents": 200000}},
    )
    assert res.status == StepStatus.AMBIGU_ESCALADE
    assert res.escalade_reason is not None
    assert len(res.step_trace) == 8

    insuff = DeterministicHarness(
        cfg,
        lambda _c, _e: {
            "statut_analyse": "DONNEES_INSUFFISANTES",
            "categorie_sinistre": "inconnu",
            "montant_reclame_cents": None,
            "reference_dossier": "DOS-7777",
            "motif_escalade": "Piece illisible.",
        },
    ).run(
        {"reference_dossier": "DOS-7777", "texte": "flou"},
        {"DOS-7777": {"max_montant_cents": 200000}},
    )
    assert insuff.status == StepStatus.DONNEES_INSUFFISANTES


def test_harness_repair_loop_stops_after_max_retries() -> None:
    calls = {"count": 0}
    cfg = HarnessConfig(
        schema_path=SCHEMAS_DIR / "harness_extraction.schema.json",
        max_repair_retries=2,
        allowed_grounding_ids=frozenset({"DOS-3333"}),
    )

    def broken_adapter(
        _ctx: dict[str, Any], _errs: list[str]
    ) -> dict[str, Any]:
        calls["count"] += 1
        return {"invalide": True}

    out = DeterministicHarness(cfg, broken_adapter).run(
        {"reference_dossier": "DOS-3333", "texte": "x"},
        {"DOS-3333": {"max_montant_cents": 1000}},
    )
    assert out.repair_attempts == 2
    assert calls["count"] <= 3
    assert out.status in {StepStatus.ESCALADED, StepStatus.VALIDATION_FAILED}


def test_harness_rejects_oversized_payload_and_root_allof() -> None:
    cfg = HarnessConfig(
        schema_path=SCHEMAS_DIR / "harness_extraction.schema.json",
        max_payload_bytes=64,
    )
    out = DeterministicHarness(cfg, lambda _c, _e: {}).run(
        {"reference_dossier": "DOS-1111", "texte": "A" * 200},
        {},
    )
    assert out.status == StepStatus.VALIDATION_FAILED

    schema_allof = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "allOf": [{"required": ["a"]}],
        "required": ["a"],
        "properties": {"a": {"type": "string"}},
    }
    assert len(validate_strict_schema(schema_allof, {"a": "ok"})) >= 1


def test_mcp_tools_list_deterministic_sort_and_cache() -> None:
    t1 = _sample_tool_def()
    t2 = {
        "name": "approvisionnement_lister_fournisseurs",
        "title": "Lister fournisseurs",
        "description": "Lecture seule des fournisseurs.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": False,
            "required": [],
            "properties": {},
        },
    }
    d1 = compute_tool_definition_digest(t1)
    d2 = compute_tool_definition_digest(t2)
    catalog = {
        t1["name"]: McpCatalogEntry(
            ref=f"mcp-appro/{t1['name']}@1.4.0",
            server_id="mcp-appro",
            tool_name=t1["name"],
            contract_version="1.4.0",
            definition_digest=d1,
            tier="P2",
            allowed_header_projections=frozenset({"Cost-Center"}),
        ),
        t2["name"]: McpCatalogEntry(
            ref=f"mcp-appro/{t2['name']}@1.0.0",
            server_id="mcp-appro",
            tool_name=t2["name"],
            contract_version="1.0.0",
            definition_digest=d2,
            tier="P0",
        ),
    }
    # Desordre d'entree -> sortie deterministe triee et prefixee
    res = verify_tools_list_against_catalog(
        [t2, t1], catalog, server_id="mcp-appro"
    )
    assert list(res.active_tools.keys()) == [
        "mcp-appro.approvisionnement_creer_bon_commande",
        "mcp-appro.approvisionnement_lister_fournisseurs",
    ]
    assert res.suspended_tools == ()
    assert res.server_suspended is False

    # Cles volatiles ignorees lors du calcul d'empreinte JCS
    t1_vol = copy.deepcopy(t1)
    t1_vol["_meta"] = {"lastUpdated": "2026-12-01"}
    assert (
        compute_tool_definition_digest(
            t1_vol, volatile_meta_keys=("_meta",)
        )
        == d1
    )

    # Validation schema strict C.2 (window="task" et window_s=86400)
    c2_entry = {
        "ref": (
            "mcp-approvisionnement/"
            "approvisionnement_creer_bon_commande@1.4.0"
        ),
        "tool_name": t1["name"],
        "contract_version": "1.4.0",
        "definition_digest": d1,
        "server": {
            "id": "mcp-approvisionnement",
            "endpoint": "https://passerelle-agents.ent.ca/mcp/appro",
            "mcp_revision": "2026-07-28",
            "extensions_allowed": [],
        },
        "lifecycle_state": "production",
        "tier": "P2",
        "approval_thresholds": [
            {
                "measure": (
                    "sum(lignes[].quantite * lignes[].prix_unitaire_cents)"
                ),
                "computed_by": "gateway",
                "unit": "cents_cad",
                "scope": "task",
                "window": "task",
                "max_without_approval": 500000,
                "inclusive": True,
            },
            {
                "measure": (
                    "sum(lignes[].quantite * lignes[].prix_unitaire_cents)"
                ),
                "computed_by": "gateway",
                "unit": "cents_cad",
                "scope": "counterparty:fournisseur_id",
                "window_s": 86400,
                "max_without_approval": 2000000,
                "inclusive": True,
            },
        ],
        "compensation": {
            "ref": "mcp-approvisionnement/annuler@1.2.0",
            "tier": "P2",
        },
        "idempotency": {
            "argument": "idempotency_key",
            "mode": "native",
            "checked_by_server": True,
            "on_conflict": "reject",
            "on_in_progress": "refuse",
            "on_duplicate": "replay_result",
            "key_retention_s": 864000,
        },
        "oauth_scope": "approvisionnement:write",
        "header_projection": {"centre_cout": "Mcp-Param-Cost-Center"},
        "data_classification_max": "confidentiel",
        "personal_information": False,
        "owner": "Direction Approvisionnement",
        "on_call_team": "garde-plateforme-erp",
        "known_consumers": ["agt-achats-indirects"],
        "reviewed_by": ["responsable-outil", "securite"],
        "approved_on": "2026-10-06",
        "next_review": "2027-04-06",
    }
    cat_schema = _load_schema("mcp_tool_catalog.schema.json")
    assert validate_strict_schema(cat_schema, c2_entry) == []

    # Outil absent du catalogue + collision de nom refuses (EXIG-MCP-20)
    rogue_res = verify_tools_list_against_catalog(
        [t1, {"name": "outil_inconnu", "description": "rogue"}],
        catalog,
        server_id="mcp-appro",
    )
    assert "outil_inconnu" in rogue_res.suspended_tools
    dup_res = verify_tools_list_against_catalog(
        [t1, t1], catalog, server_id="mcp-appro"
    )
    assert dup_res.server_suspended is True


def test_mcp_streamable_http_and_pinning() -> None:
    adapter = StreamableHttpAdapter(
        endpoint="https://passerelle-agents.ent.ca/mcp/appro",
        expected_revision="2026-07-28",
    )
    caps = adapter.capabilities()
    assert caps["revision"] == "2026-07-28"
    assert caps["transport"] == "streamable_http"
    ok_resp = adapter.send_jsonrpc(
        "tools/list", {}, {"MCP-Protocol-Version": "2026-07-28"}
    )
    assert isinstance(ok_resp, dict)

    with pytest.raises(DeprecatedTransportError):
        StreamableHttpAdapter(
            endpoint="https://passerelle-agents.ent.ca/mcp/sse",
            expected_revision="2025-11-25",
            transport_mode="http+sse",
        ).send_jsonrpc("tools/list", {}, {})


def test_mcp_rug_pull_single_char_drift_suspends() -> None:
    orig = _sample_tool_def()
    digest = compute_tool_definition_digest(orig)
    entry = McpCatalogEntry(
        ref="mcp-appro/approvisionnement_creer_bon_commande@1.4.0",
        server_id="mcp-appro",
        tool_name=orig["name"],
        contract_version="1.4.0",
        definition_digest=digest,
        tier="P2",
    )
    tampered = copy.deepcopy(orig)
    tampered["description"] = orig["description"] + " "  # +1 char drift
    res = verify_tools_list_against_catalog(
        [tampered],
        {orig["name"]: entry},
        server_id="mcp-appro",
        max_drift_before_suspend=1,
    )
    assert orig["name"] in res.suspended_tools
    assert res.active_tools == {}
    assert res.server_suspended is True


def test_mcp_header_mismatch_raises_400_32020() -> None:
    body = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "supprimer_base",
            "arguments": {"centre_cout": "CC-4410"},
            "_meta": {
                "io.modelcontextprotocol/protocolVersion": "2026-07-28"
            },
        },
    }
    headers = {
        "MCP-Protocol-Version": "2026-07-28",
        "Mcp-Method": "tools/call",
        "Mcp-Name": "recherche_publique",
    }
    with pytest.raises(HeaderMismatchError) as exc_info:
        validate_mcp_headers(headers, body)
    assert exc_info.value.http_status == 400
    assert exc_info.value.jsonrpc_code == -32020

    # Divergence MCP-Protocol-Version, Mcp-Method, et Mcp-Param-*
    for bad_hdrs in (
        {
            "MCP-Protocol-Version": "2025-11-25",
            "Mcp-Method": "tools/call",
            "Mcp-Name": "supprimer_base",
        },
        {
            "MCP-Protocol-Version": "2026-07-28",
            "Mcp-Method": "tools/list",
            "Mcp-Name": "supprimer_base",
        },
        {
            "MCP-Protocol-Version": "2026-07-28",
            "Mcp-Method": "tools/call",
            "Mcp-Name": "supprimer_base",
            "Mcp-Param-Cost-Center": "CC-9999",
        },
    ):
        with pytest.raises(HeaderMismatchError) as exc_sub:
            validate_mcp_headers(bad_hdrs, body)
        assert exc_sub.value.http_status == 400
        assert exc_sub.value.jsonrpc_code == -32020


def test_mcp_meta_allowlist_purges_unreserved() -> None:
    entry = McpCatalogEntry(
        ref="mcp-appro/outil@1.0.0",
        server_id="mcp-appro",
        tool_name="outil",
        contract_version="1.0.0",
        definition_digest="sha256:" + "0" * 64,
        allowed_header_projections=frozenset({"Cost-Center"}),
        allowed_meta_keys=frozenset({"traceparent"}),
    )
    body = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "outil",
            "arguments": {"centre_cout": "CC-4410"},
            "_meta": {
                "io.modelcontextprotocol/protocolVersion": "2026-07-28",
                "traceparent": (
                    "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa-01"
                ),
                "tenant": "admin",
                "authenticated": True,
                "clientInfo": {"name": "rogue-admin"},
            },
        },
    }
    headers = {
        "MCP-Protocol-Version": "2026-07-28",
        "Mcp-Method": "tools/call",
        "Mcp-Name": "outil",
        "Mcp-Param-Cost-Center": "CC-4410",
    }
    cleaned = validate_mcp_headers(headers, body, entry)
    meta = cleaned["params"]["_meta"]
    assert "io.modelcontextprotocol/protocolVersion" in meta
    assert "traceparent" in meta
    assert "tenant" not in meta
    assert "authenticated" not in meta
    assert "clientInfo" not in meta


def test_reject_x_mcp_header_pii_or_token() -> None:
    bad_body = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "outil_sensible",
            "arguments": {"token": "secret", "nas": "123456789"},
            "inputSchema": {
                "type": "object",
                "properties": {
                    "token": {
                        "type": "string",
                        "x-mcp-header": "Auth-Token",
                    },
                    "nas": {
                        "type": "string",
                        "x-mcp-header": "Citizen-NAS",
                    },
                },
            },
            "_meta": {
                "io.modelcontextprotocol/protocolVersion": "2026-07-28"
            },
        },
    }
    headers = {
        "MCP-Protocol-Version": "2026-07-28",
        "Mcp-Method": "tools/call",
        "Mcp-Name": "outil_sensible",
    }
    with pytest.raises(ValueError):
        validate_mcp_headers(headers, bad_body)


def test_a2a_agent_card_jws_es256_and_pinned_jku() -> None:
    schema = _load_schema("a2a_agent_card.schema.json")
    pinned_jku = "https://cles.ent.ca/a2a/jwks.json"
    card, jwks = _sign_agent_card(_sample_card_base(), jku=pinned_jku)
    Draft202012Validator(schema).validate(card)

    verdict = validate_agent_card(
        card,
        jwks=jwks,
        pinned_jku=pinned_jku,
        approved_extensions={
            "https://ent.ca/a2a/extensions/gouvernance/v1"
        },
        schema=schema,
    )
    assert verdict.valid is True
    assert verdict.signer_kid == "cartes-agents-2026-10"
    assert len(verdict.card_etag) >= 16

    # Flux authorizationCode standard accepte par schema A2A
    oauth_ok_base = _sample_card_base()
    oauth_ok_base["securitySchemes"] = {
        "oauth": {
            "oauth2SecurityScheme": {
                "flows": {
                    "authorizationCode": {
                        "authorizationUrl": "https://idp.ent.ca/auth",
                        "tokenUrl": "https://idp.ent.ca/token",
                        "pkceRequired": True,
                        "scopes": {"risque-credit:invoke": "Invoke"},
                    }
                }
            }
        }
    }
    oauth_ok_base["securityRequirements"] = [
        {"schemes": {"oauth": {"list": ["risque-credit:invoke"]}}}
    ]
    oauth_ok_card, oauth_jwks = _sign_agent_card(oauth_ok_base, jku=pinned_jku)
    assert (
        validate_agent_card(
            oauth_ok_card,
            jwks=oauth_jwks,
            pinned_jku=pinned_jku,
            approved_extensions={
                "https://ent.ca/a2a/extensions/gouvernance/v1"
            },
            schema=schema,
        ).valid
        is True
    )

    # Adaptateur versionne A2A v1.1.0-rc -> v1.0.1
    adapted = AgentCardAdapter(protocol_version="1.1.0-rc").adapt(card)
    assert isinstance(adapted, dict)

    # JKU SSRF non epingle -> rejet
    bad_jku = validate_agent_card(
        card,
        jwks=jwks,
        pinned_jku="https://autre.ent.ca/jwks.json",
        approved_extensions={
            "https://ent.ca/a2a/extensions/gouvernance/v1"
        },
        schema=schema,
    )
    assert bad_jku.valid is False

    # Signature alteree -> rejet
    tampered = copy.deepcopy(card)
    tampered["description"] = "Description modifiee"
    bad_sig = validate_agent_card(
        tampered,
        jwks=jwks,
        pinned_jku=pinned_jku,
        approved_extensions={
            "https://ent.ca/a2a/extensions/gouvernance/v1"
        },
        schema=schema,
    )
    assert bad_sig.valid is False

    # Extension non approuvee -> rejet
    bad_ext = validate_agent_card(
        card,
        jwks=jwks,
        pinned_jku=pinned_jku,
        approved_extensions=set(),
        schema=schema,
    )
    assert bad_ext.valid is False

    # Flux password et implicit interdits -> rejet
    for banned_flow in ("password", "implicit"):
        bad_oauth_base = _sample_card_base()
        bad_oauth_base["securitySchemes"] = {
            "legacy": {
                "oauth2SecurityScheme": {
                    "flows": {
                        banned_flow: {
                            "tokenUrl": "https://idp.ent.ca/token"
                        }
                    }
                }
            }
        }
        bad_oauth_card, bad_jwks = _sign_agent_card(
            bad_oauth_base, jku=pinned_jku
        )
        bad_flow = validate_agent_card(
            bad_oauth_card,
            jwks=bad_jwks,
            pinned_jku=pinned_jku,
            approved_extensions={
                "https://ent.ca/a2a/extensions/gouvernance/v1"
            },
            schema=schema,
        )
        assert bad_flow.valid is False
