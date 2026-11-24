#!/usr/bin/env python3
"""Synthétiseur du graphe thématique et structurel du Corpus Agentique.

Charge :
- ``Cartographie/donnees/schema-cartographie.json``
- ``Cartographie/donnees/pivots-concordance.json``
- ``Cartographie/donnees/structure-integrale.json``
- Les 7 shards ``Cartographie/donnees/shards/*.json``

Produit et valide :
- ``Cartographie/donnees/synthese-transversale.json``
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Any

TOME_ORDER = ["R", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]
TOME_RANK = {tid: i for i, tid in enumerate(TOME_ORDER)}

# Rapprochement sémantique contrôlé pour fusionner les doublons stricts entre shards
SLUG_MERGE_MAP: dict[str, str] = {
    "regle-non-cumul-confinement-session": "regle-de-deux-opa",
    "protocole-decentralise-anp": "protocole-anp-did-wba",
}

# Correspondance exacte des sous-domaines personnalisés (ex. tome-1a) vers les 36 sous-domaines canoniques
SUBDOMAIN_OVERRIDE: dict[tuple[str, str], str] = {
    # D01
    ("D01", "Économie de l'interopérabilité"): "Économie de Coase et dettes agentiques",
    ("D01", "Fondements des systèmes agentiques"): "Rupture épistémique et Systems of Agency",
    ("D01", "Fiabilité probabiliste"): "Fiabilité probabiliste et loi de Lusser",
    ("D01", "Raisonnement et planification"): "Rupture épistémique et Systems of Agency",
    ("D01", "Économie de l'inférence"): "Économie de Coase et dettes agentiques",
    ("D01", "Systèmes multi-agents"): "Fiabilité probabiliste et loi de Lusser",
    ("D01", "Épistémologie des échanges"): "Rupture épistémique et Systems of Agency",
    # D02
    ("D02", "Échelles d'autonomie"): "Échelle d'autonomie L0–L4 et supervision humaine",
    ("D02", "Supervision et contrôle humain"): "Échelle d'autonomie L0–L4 et supervision humaine",
    ("D02", "Architecture de contrôle"): "Partition hybride 80/20 et harnais déterministe",
    ("D02", "Patrons d'agents"): "Partition hybride 80/20 et harnais déterministe",
    ("D02", "Ingénierie de l'outillage"): "Architecture de référence, plans et noyau possédé",
    # D03
    ("D03", "Cadres d'interopérabilité"): "Passerelles, découverte et anti-verrouillage",
    ("D03", "Gouvernance des standards"): "Passerelles, découverte et anti-verrouillage",
    ("D03", "Axe vertical agent-outil"): "Protocoles verticaux outil-modèle (MCP)",
    ("D03", "Axe horizontal agent-agent"): "Protocoles horizontaux pair-à-pair (A2A, AGNTCY, AP2)",
    ("D03", "Découverte et annuaires"): "Passerelles, découverte et anti-verrouillage",
    ("D03", "Infrastructure de transport"): "Protocoles horizontaux pair-à-pair (A2A, AGNTCY, AP2)",
    ("D03", "Couche économique et règlement"): "Protocoles horizontaux pair-à-pair (A2A, AGNTCY, AP2)",
    ("D03", "Gouvernance et terminologie"): "Protocoles horizontaux pair-à-pair (A2A, AGNTCY, AP2)",
    ("D03", "Médiation et exposition"): "Passerelles, découverte et anti-verrouillage",
    ("D03", "Contrats et conformité"): "Passerelles, découverte et anti-verrouillage",
    # D04
    ("D04", "Sémantique et graphes"): "Sémantique métier, ontologies et compilation de contexte",
    ("D04", "Sémantique agentique"): "Sémantique métier, ontologies et compilation de contexte",
    ("D04", "Contrats de données"): "Sémantique métier, ontologies et compilation de contexte",
    ("D04", "Mémoire et contexte"): "Mémoire CoALA, bi-temporalité et filtrage ACL",
    ("D04", "Récupération d'information"): "Sémantique métier, ontologies et compilation de contexte",
    ("D04", "Gouvernance des données"): "Mémoire CoALA, bi-temporalité et filtrage ACL",
    ("D04", "Intégration patrimoniale"): "Encapsulation patrimoniale, IT/OT et 6 substrats",
    # D05
    ("D05", "Architectures événementielles"): "Chorégraphie Event Mesh et bus asynchrone",
    ("D05", "Transactions et résilience"): "Exécution durable, idempotence et Saga compensatoire",
    ("D05", "Orchestration et topologies"): "Sobriété OO1–OO4 et topologies d'orchestration",
    ("D05", "Fiabilité inter-agents"): "Sobriété OO1–OO4 et topologies d'orchestration",
    # D06
    ("D06", "Socle IAM pré-agentique"): "Identité non humaine (NHI) et attestation SPIFFE/vLEI",
    ("D06", "Identité non humaine (NHI)"): "Identité non humaine (NHI) et attestation SPIFFE/vLEI",
    ("D06", "Émission et annuaires"): "Identité non humaine (NHI) et attestation SPIFFE/vLEI",
    ("D06", "Identité de charge de travail"): "Identité non humaine (NHI) et attestation SPIFFE/vLEI",
    ("D06", "Identité portable et passeport"): "Identité non humaine (NHI) et attestation SPIFFE/vLEI",
    ("D06", "Évaluation identitaire"): "Identité non humaine (NHI) et attestation SPIFFE/vLEI",
    ("D06", "Chaîne de mandat"): "Chaîne de mandat, OBO 2e saut et approbation CIBA",
    ("D06", "Admission inter-domaines"): "Chaîne de mandat, OBO 2e saut et approbation CIBA",
    ("D06", "Cycle de vie et révocation"): "Chaîne de mandat, OBO 2e saut et approbation CIBA",
    ("D06", "Cryptographie post-quantique"): "PKI automatisée 47 jours et cryptographie post-quantique",
    # D07
    ("D07", "Modèle de menace agentique"): "Menaces agentiques et surface d'attaque protocolaire",
    ("D07", "Surface d'attaque outillage"): "Menaces agentiques et surface d'attaque protocolaire",
    ("D07", "Taxonomie identitaire"): "Menaces agentiques et surface d'attaque protocolaire",
    ("D07", "Défense architecturale"): "Politiques hors modèle OPA/Rego, Règle de deux et CaMeL",
    ("D07", "Défense opérationnelle et SOC"): "Confinement SHADI/microVM, TEE et défense SOC/SOAR",
    ("D07", "Sûreté et alignement"): "Politiques hors modèle OPA/Rego, Règle de deux et CaMeL",
    # D08
    ("D08", "Observabilité distribuée"): "Observabilité OTel GenAI et double couloir probatoire",
    ("D08", "Preuve cryptographique"): "Observabilité OTel GenAI et double couloir probatoire",
    ("D08", "Évaluation et métrologie"): "Banc EvalOps hermétique E1–E3, Wilson et métamorphique",
    # D09
    ("D09", "Droit québécois"): "Droit québécois et prudentiel financier canadien",
    ("D09", "Régulation prudentielle canadienne"): "Droit québécois et prudentiel financier canadien",
    ("D09", "Régulation prudentielle québécoise"): "Droit québécois et prudentiel financier canadien",
    ("D09", "Régulation des marchés"): "Droit québécois et prudentiel financier canadien",
    ("D09", "Droit européen et comparatif"): "Réglementation européenne et référentiels internationaux",
    # D11
    ("D11", "Prospective et péremption"): "Scénarios 2028–2035, trajectoires DAPP et portes POR/SIG",
    ("D11", "Responsabilité et litiges"): "Gouvernance duale AE ↔ AS, thèses T1–T10 et pièges",
    # D12
    ("D12", "Épistémologie de vérification"): "Concordance inter-tomes (DIV-02, DISC-01..05) et Wyvern G0–G5",
    ("D12", "Structure de la somme"): "Concordance inter-tomes (DIV-02, DISC-01..05) et Wyvern G0–G5",
}

# Règles de regroupement propre des familles (Niveau 3) par (domain_id, subdomain)
# Chaque entrée : (nom_famille_canonique, mots_cles) ; la dernière entrée du sous-domaine sert de repli.
FAMILY_RULES: dict[tuple[str, str], list[tuple[str, list[str]]]] = {
    ("D01", "Rupture épistémique et Systems of Agency"): [
        ("Paradigme Systems of Agency", ["systems-of-agency", "rupture", "boucle", "taxonomie", "map", "adoption", "intentions"]),
        ("Généalogie et fondements", []),
    ],
    ("D01", "Fiabilité probabiliste et loi de Lusser"): [
        ("Loi de Lusser et erreurs en cascade", ["lusser", "silencieuses", "surcout", "cascade"]),
        ("Constance pass^k et métriques de fiabilité", []),
    ],
    ("D01", "Économie de Coase et dettes agentiques"): [
        ("Économie cognitive de Coase", ["coase", "industrialisation", "marche", "jetons", "slm"]),
        ("Dettes cognitive, technique et d'intention", []),
    ],
    ("D02", "Partition hybride 80/20 et harnais déterministe"): [
        ("Partition 80/20 et séparation déterministe", ["80-20", "separation", "patrons-boucle", "distinction", "usine", "outillage", "outils"]),
        ("Harnais déterministe à 8 étapes", []),
    ],
    ("D02", "Échelle d'autonomie L0–L4 et supervision humaine"): [
        ("Échelle L0–L4 et règle du maillon", ["echelle", "maillon", "maturite", "qos"]),
        ("Supervision HITL / HOTL et abstention", []),
    ],
    ("D02", "Architecture de référence, plans et noyau possédé"): [
        ("Noyau de contrôle possédé (42 CAP) et 31 ADR", ["noyau", "adr", "dec", "clauses-sortie"]),
        ("Cadres TOGAF / ArchiMate et 6 couches", []),
    ],
    ("D03", "Protocoles verticaux outil-modèle (MCP)"): [
        ("Spécification MCP et façades d'intention", ["protocole-mcp", "adaptateur-mcp", "facades", "aci", "webmcp", "web"]),
        ("Épinglage SHA-256 et sécurité MCP", []),
    ],
    ("D03", "Protocoles horizontaux pair-à-pair (A2A, AGNTCY, AP2)"): [
        ("Protocole pair-à-pair A2A et ANP", ["a2a", "anp", "acp", "agui", "a2ui", "interfaces"]),
        ("Piles AGNTCY/SLIM et paiements AP2", []),
    ],
    ("D03", "Passerelles, découverte et anti-verrouillage"): [
        ("Découverte Agent Card et registres", ["agent-card", "decouverte", "contrats", "routage", "plan-donnees", "b2b-federe"]),
        ("Passerelles PEP / AI Gateway et anti-verrouillage", []),
    ],
    ("D04", "Sémantique métier, ontologies et compilation de contexte"): [
        ("Ontologies métier (FIBO) et contrats ODCS", ["semantique", "ontolog", "ecart-accord", "formats", "donnees-pretes", "contrats-donnees"]),
        ("Compilation de contexte et RAG agentique", []),
    ],
    ("D04", "Mémoire CoALA, bi-temporalité et filtrage ACL"): [
        ("Architecture mémorielle CoALA à 4 tiroirs", ["coala", "memoire"]),
        ("Filtrage ACL amont et gouvernance RAG", []),
    ],
    ("D04", "Encapsulation patrimoniale, IT/OT et 6 substrats"): [
        ("Couche anti-corruption (ACL) et mainframes", ["anti-corruption", "mediation", "iso-20022", "coexistence", "cua"]),
        ("Encapsulation IT/OT et 6 substrats d'état", []),
    ],
    ("D05", "Sobriété OO1–OO4 et topologies d'orchestration"): [
        ("Arbre de sobriété OO1–OO4 et APM", ["sobriete", "oo1", "apm", "enveloppes"]),
        ("Topologies multi-agents, cadriciels et MAST", []),
    ],
    ("D05", "Chorégraphie Event Mesh et bus asynchrone"): [
        ("Dorsale Event Mesh (CloudEvents / AsyncAPI)", ["event-mesh", "choregraphie", "pathologies"]),
        ("Protocoles d'échange et négociation asynchrone", []),
    ],
    ("D05", "Exécution durable, idempotence et Saga compensatoire"): [
        ("Exécution durable (Temporal) et résilience", ["durable", "resilience", "contexte-minimal", "pont-ia", "lap"]),
        ("Idempotence JCS et Saga compensatoire", []),
    ],
    ("D06", "Identité non humaine (NHI) et attestation SPIFFE/vLEI"): [
        ("Identités NHI, OAuth 2.1 et registres", ["non-humaine", "socle-iam", "annuaires", "registres", "grille"]),
        ("Attestation SPIFFE/SPIRE, DID/VC et vLEI", []),
    ],
    ("D06", "Chaîne de mandat, OBO 2e saut et approbation CIBA"): [
        ("Délégation OBO (RFC 8693), DPoP et RAR", ["obo", "dpop", "rar", "signature"]),
        ("Approbation CIBA, KYA et révocation SSF/CAEP", []),
    ],
    ("D06", "PKI automatisée 47 jours et cryptographie post-quantique"): [
        ("Certificats TLS 100 j / 47 j et ACME", ["47-jours", "tls"]),
        ("Transition post-quantique ML-DSA / SLH-DSA", []),
    ],
    ("D07", "Menaces agentiques et surface d'attaque protocolaire"): [
        ("Injection indirecte et empoisonnement MCP", ["injection", "tool-poisoning", "chaine-approvisionnement", "non-compositionnalite"]),
        ("Taxonomies OWASP ASI, ATLAS et mandataire confus", []),
    ],
    ("D07", "Politiques hors modèle OPA/Rego, Règle de deux et CaMeL"): [
        ("Politiques OPA/Rego en échec fermé", ["opa-rego", "echec-ferme", "maillage-agents", "stamp", "stpa"]),
        ("Règle de deux et séparation contrôle/données CaMeL", []),
    ],
    ("D07", "Confinement SHADI/microVM, TEE et défense SOC/SOAR"): [
        ("Confinement SHADI, microVM, WASI et TEE", ["shadi", "opensandbox", "tee", "hyok"]),
        ("Défense SOC/SOAR, Red Team et coupe-circuit", []),
    ],
    ("D08", "Observabilité OTel GenAI et double couloir probatoire"): [
        ("Télémétrie OpenTelemetry GenAI et provenance", ["otel", "provenance", "indicateurs", "gitops"]),
        ("Double couloir PII, JCS et scellage SCITT", []),
    ],
    ("D08", "Banc EvalOps hermétique E1–E3, Wilson et métamorphique"): [
        ("Bancs EvalOps E1–E3 et bornes de Wilson", ["evalops", "wilson", "evaluation-agentique"]),
        ("Tests métamorphiques, juges et dérives", []),
    ],
    ("D08", "SRE agentique et FinOps FOCUS / CPO / carbone"): [
        ("FinOps FOCUS v1.4, CPO et carbone", ["finops", "cpo", "carbone", "inference"]),
        ("SRE agentique et volant de distillation SLM", []),
    ],
    ("D09", "Droit québécois et prudentiel financier canadien"): [
        ("Droit québécois : Loi 25, ÉFVP et AMF", ["loi-25", "efvp", "amf", "effacement", "mandat"]),
        ("Prudentiel canadien : BSIF E-23, ACVM et LSAC", []),
    ],
    ("D09", "Réglementation européenne et référentiels internationaux"): [
        ("Union européenne : EU AI Act, DORA, CRA et EN 18286", ["eu-ai-act", "en-18286", "maillage-reglementaire"]),
        ("Référentiels internationaux : NIST, ISO 42001 et G7", []),
    ],
    ("D09", "Approvisionnement réversible et clauses contractuelles"): [
        ("Clauses contractuelles EXIG-APP et sortie", ["clauses", "approvisionnement"]),
        ("Grille fournisseurs et souveraineté nuage", []),
    ],
    ("D10", "Cinq profils financiers réglementés et 24 PEX"): [
        ("Cinq profils financiers réglementés (M-14 à M-18)", ["profil-", "profils-financiers"]),
        ("Spécialisations financières, RTR et terrain canadien", []),
    ],
    ("D10", "Trois blueprints de référence et cas Groupe Boréal BEL"): [
        ("Trois blueprints multisectoriels (C01–C40)", ["blueprint"]),
        ("Cas fil rouge Groupe Boréal (BEL) et fédération", []),
    ],
    ("D10", "Usine logicielle GitOps et anti-patrons agentiques"): [
        ("Usine logicielle, GitOps et reprise cognitive", ["fabrique", "gitops", "iap", "reprise", "echelle", "plateformes"]),
        ("Catalogue des anti-patrons agentiques", []),
    ],
    ("D11", "Scénarios 2028–2035, trajectoires DAPP et portes POR/SIG"): [
        ("Trajectoires adaptatives DAPP, portes POR et signaux SIG", ["dapp", "portes", "signaux", "trajectoire-90j", "feuille-de-route", "priorites-90"]),
        ("Prospective, scénarios 2028–2035 et maturité", []),
    ],
    ("D11", "Gouvernance duale AE ↔ AS, thèses T1–T10 et pièges"): [
        ("Gouvernance duale AE ↔ AS, thèses T1–T10 et RACI", ["gouvernance-duale", "theses", "decisions-conjointes", "raci", "hub-and-spoke", "registre", "derogations"]),
        ("Sept pièges de gouvernance et responsabilité", []),
    ],
    ("D11", "Capital humain, atrophie des compétences et dynamique énergie/marché"): [
        ("Atrophie des compétences et vivier junior", ["atrophie", "vivier-junior", "approbation-reflexe"]),
        ("Dynamique énergie et marché du calcul", []),
    ],
    ("D12", "Exigences CRE-IA-2026-01, PRR-75 et 24 portes bloquantes"): [
        ("Socle CRE-IA-2026-01 (305 EXIG-*) et interdits GOV-17", ["exigences-cre-ia", "interdictions", "portee", "actualisation", "contrats-types"]),
        ("Grille PRR-75, 24 portes bloquantes et fiche 2027-B001", []),
    ],
    ("D12", "Trousse exécutable Tome 8 et vecteurs tiers"): [
        ("Trousse exécutable Python/OPA et 5 SBB", ["trousse", "sbb", "barriere-logicielle-g0"]),
        ("Validation des vecteurs tiers et CA-G0-SYNC", []),
    ],
    ("D12", "Concordance inter-tomes (DIV-02, DISC-01..05) et Wyvern G0–G5"): [
        ("Concordance inter-tomes (DIV-02 et 5 discordances)", ["concordance", "discordances", "reconciliation", "matrice-tracabilite", "glossaire", "architecture-collection"]),
        ("Protocole Wyvern, G0–G5, Typst et clause non-avis", []),
    ],
}


# Nœuds thématiques atomiques spécialisés extraits des pivots et facettes multi-tomes réels
SPECIALIZED_NODES_SPEC: list[dict[str, Any]] = [
    {
        "canonical_slug": "quadruple-dette-agentique",
        "parent_pivot": "dette-cognitive-vs-technique",
        "domain_id": "D01",
        "subdomain": "Économie de Coase et dettes agentiques",
        "title": "Quadruple dette agentique (technique, cognitive, intention, couplage)",
        "summary": "Engrenage fermé décrit au Tome 7 reliant dette technique, dette cognitive, dette d'intention et dette de couplage global lorsqu'une chaîne d'agents s'appuie sur le contexte du modèle plutôt que sur un noyau déterministe.",
        "autonomy_levels": ["L1", "L2", "L3"],
        "roles": ["AE", "AS", "Direction"],
        "horizon": "2026–2035",
        "tags": ["dette-cognitive", "dette-intention", "couplage", "T7"],
        "identifiers": ["T7 ch.04"],
        "tome_filter": ["T7", "T1", "T3"],
        "rel_to_pivot": ("amplification_synergie", "Engrenage composé de la dette cognitive et technique"),
    },
    {
        "canonical_slug": "validation-json-schema-ambigu-escalade",
        "parent_pivot": "harnais-deterministe-8-etapes",
        "domain_id": "D02",
        "subdomain": "Partition hybride 80/20 et harnais déterministe",
        "title": "Contrats JSON Schema Draft 2020-12 stricts et porte AMBIGU_ESCALADE",
        "summary": "Validation hors modèle par JSON Schema Draft 2020-12 (additionalProperties: false, réparation bornée) et droit explicite d'abstention typée AMBIGU_ESCALADE vers un superviseur humain (Tome 8 ch. 01).",
        "autonomy_levels": ["L0", "L1", "L2", "L3"],
        "roles": ["AS", "SRE"],
        "horizon": "2026–2030",
        "tags": ["JSON-Schema-2020-12", "AMBIGU_ESCALADE", "abstention"],
        "identifiers": ["EXIG-ARC-03", "EXIG-MCP-19", "G0-EX-CH01-01"],
        "tome_filter": ["T8", "T2", "T6"],
        "rel_to_pivot": ("operationnalisation", "Contrat de schéma et porte d'escalade du harnais 8 étapes"),
    },
    {
        "canonical_slug": "adaptateur-mcp-streamable-http-sep-3398",
        "parent_pivot": "protocole-mcp",
        "domain_id": "D03",
        "subdomain": "Protocoles verticaux outil-modèle (MCP)",
        "title": "Transport Streamable HTTP MCP 2026-07-28, rejet HTTP+SSE et adaptateur SEP-3398",
        "summary": "Épinglage normatif sur MCP 2026-07-28 sans état (Streamable HTTP, en-têtes Mcp-Method/Mcp-Name), rejet de HTTP+SSE (DISC-05) et isolation derrière McpTransportAdapter pour la fenêtre SEP-2596 (28 juill. 2027) et SEP-3398 (30 mars 2027).",
        "autonomy_levels": ["L1", "L2", "L3"],
        "roles": ["AS", "RSSI"],
        "horizon": "2026–2028",
        "tags": ["MCP-2026-07-28", "Streamable-HTTP", "SEP-2596", "SEP-3398"],
        "identifiers": ["EXIG-MCP-03", "EXIG-MCP-15", "EXIG-MCP-22", "DISC-05"],
        "tome_filter": ["T8", "T2", "T5"],
        "rel_to_pivot": ("operationnalisation", "Profil de transport épinglé et adaptateur post-gel de MCP"),
    },
    {
        "canonical_slug": "canal-compensation-isole-outbox",
        "parent_pivot": "saga-compensatoire",
        "domain_id": "D05",
        "subdomain": "Exécution durable, idempotence et Saga compensatoire",
        "title": "Point pivot, Transactional Outbox et canal de compensation isolé (EXIG-ORC-28)",
        "summary": "Voie de compensation dédiée dotée d'identité et budget propres (EXIG-ORC-28) avec Transactional Outbox et clé JCS idem-v1 garantissant la réversibilité avant le point pivot même après révocation de l'agent métier.",
        "autonomy_levels": ["L2", "L3", "L4"],
        "roles": ["AS", "SRE"],
        "horizon": "2026–2035",
        "tags": ["EXIG-ORC-28", "point-pivot", "Transactional-Outbox", "idem-v1"],
        "identifiers": ["EXIG-ORC-18", "EXIG-ORC-20", "EXIG-ORC-21", "EXIG-ORC-28"],
        "tome_filter": ["T8", "T5", "T2"],
        "rel_to_pivot": ("operationnalisation", "Garantie d'isolation et de persistance de la Saga compensatoire"),
    },
    {
        "canonical_slug": "liaison-jetons-dpop-mtls",
        "parent_pivot": "delegation-obo-deux-sauts",
        "domain_id": "D06",
        "subdomain": "Chaîne de mandat, OBO 2e saut et approbation CIBA",
        "title": "Liaison cryptographique DPoP (RFC 9449), mTLS (RFC 8705) et rejet du token passthrough",
        "summary": "Contrainte des jetons délégués à la clé de l'expéditeur contre le rejeu et interdiction stricte du passage direct de jeton (EXIG-MCP-11, EXIG-IAM-12, EXIG-IAM-14, RFC 9700).",
        "autonomy_levels": ["L2", "L3", "L4"],
        "roles": ["AS", "RSSI"],
        "horizon": "2026–2035",
        "tags": ["DPoP", "mTLS", "RFC-9449", "token-passthrough"],
        "identifiers": ["RFC 9449", "RFC 8705", "RFC 9700", "EXIG-IAM-14", "EXIG-MCP-11"],
        "tome_filter": ["T8", "T5", "T2", "T1"],
        "rel_to_pivot": ("dependance_technique", "Liaison à l'expéditeur requise pour sécuriser l'échange OBO"),
    },
    {
        "canonical_slug": "requetes-riches-rar-txn-tokens",
        "parent_pivot": "delegation-obo-deux-sauts",
        "domain_id": "D06",
        "subdomain": "Chaîne de mandat, OBO 2e saut et approbation CIBA",
        "title": "Autorisations fines RAR (RFC 9396) et Transaction Tokens O(1)",
        "summary": "Encadrement précis des objets authorization_details (RFC 9396) et propagation en taille constante O(1) via Transaction Tokens IETF sur chaînes multi-sauts (Tome 1, Tome 5, Tome 8).",
        "autonomy_levels": ["L2", "L3", "L4"],
        "roles": ["AS", "RSSI"],
        "horizon": "2026–2035",
        "tags": ["RAR", "RFC-9396", "Txn-Tokens", "authorization_details"],
        "identifiers": ["RFC 9396", "C27", "PRR S-03"],
        "tome_filter": ["T8", "T5", "T3", "T1"],
        "rel_to_pivot": ("amplification_synergie", "Précision de portée RAR et compacité O(1) des jetons OBO"),
    },
    {
        "canonical_slug": "saturation-http-431-ml-dsa-kid",
        "parent_pivot": "post-quantique-ml-dsa-slh-dsa",
        "domain_id": "D06",
        "subdomain": "PKI automatisée 47 jours et cryptographie post-quantique",
        "title": "Dimensionnement HTTP 431 sous ML-DSA-65/87 et référence JWKS par kid",
        "summary": "Mitigation de la saturation des en-têtes HTTP (HTTP 431) causée par la taille des signatures post-quantiques ML-DSA-65/87 via références de clés publiques JWKS par kid et Transaction Tokens (Tome 5, Tome 7, Tome 8).",
        "autonomy_levels": ["L1", "L2", "L3", "L4"],
        "roles": ["AS", "RSSI", "SRE"],
        "horizon": "2028–2035",
        "tags": ["HTTP-431", "ML-DSA", "kid", "JWKS"],
        "identifiers": ["FIPS 204", "POR-007", "C27", "EXIG-SEC-27"],
        "tome_filter": ["T8", "T7", "T5"],
        "rel_to_pivot": ("attenuation_risque", "Résout la saturation d'en-tête HTTP 431 induite par ML-DSA"),
    },
    {
        "canonical_slug": "echec-ferme-opa-default-deny",
        "parent_pivot": "politiques-opa-rego-hors-modele",
        "domain_id": "D07",
        "subdomain": "Politiques hors modèle OPA/Rego, Règle de deux et CaMeL",
        "title": "Échec en mode fermé (default allow := false) et couverture 100 % Rego",
        "summary": "Invariant déterministe OPA/Rego imposant le refus par défaut sur toute erreur, donnée manquante ou entrée mal typée, vérifié à 100,0 % de couverture de lignes (45/45 cas) dans la trousse du Tome 8.",
        "autonomy_levels": ["L0", "L1", "L2", "L3", "L4"],
        "roles": ["AS", "RSSI"],
        "horizon": "2026–2035",
        "tags": ["OPA", "Rego", "fail-closed", "default-deny"],
        "identifiers": ["EXIG-SEC-06", "EXIG-SEC-25", "PRR S-09"],
        "tome_filter": ["T8", "T2", "T6"],
        "rel_to_pivot": ("operationnalisation", "Garantit le mode fermé strict des politiques OPA/Rego"),
    },
    {
        "canonical_slug": "separation-controle-donnees-camel",
        "parent_pivot": "regle-de-deux-opa",
        "domain_id": "D07",
        "subdomain": "Politiques hors modèle OPA/Rego, Règle de deux et CaMeL",
        "title": "Séparation contrôle/données CaMeL et propagation de teinte inter-agents",
        "summary": "Architecture CaMeL isolant le graphe d'appels fiable des variables de données non approuvées et propageant les étiquettes de contamination entre agents (EXIG-SEC-07, PRR S-08, compromis utilité 77 % vs 84 %).",
        "autonomy_levels": ["L1", "L2", "L3"],
        "roles": ["AS", "RSSI"],
        "horizon": "2026–2035",
        "tags": ["CaMeL", "taint-tracking", "EXIG-SEC-07", "ASI01"],
        "identifiers": ["EXIG-SEC-07", "PRR S-08", "G0-EX-CH03-02"],
        "tome_filter": ["T8", "T7", "T5", "T1"],
        "rel_to_pivot": ("amplification_synergie", "Complète la Règle de deux par suivi de teinte structurel CaMeL"),
    },
    {
        "canonical_slug": "caviardage-pii-rp-bilingue",
        "parent_pivot": "double-couloir-probatoire-pii",
        "domain_id": "D08",
        "subdomain": "Observabilité OTel GenAI et double couloir probatoire",
        "title": "Caviardage PII/RP bilingue FR/EN sans contenu brut en télémétrie",
        "summary": "Processeur de filtrage OTel supprimant les invites brutes, réponses d'outils et renseignements personnels avant export opérationnel (EXIG-OBS-07, EXIG-OBS-09, PRR O-02, diagnostic <= 14 jours).",
        "autonomy_levels": ["L0", "L1", "L2", "L3", "L4"],
        "roles": ["AS", "RSSI", "SRE", "Juridique"],
        "horizon": "2026–2035",
        "tags": ["PII", "RP", "caviardage", "EXIG-OBS-07", "EXIG-OBS-09"],
        "identifiers": ["EXIG-OBS-07", "EXIG-OBS-08", "EXIG-OBS-09", "PRR O-02"],
        "tome_filter": ["T8", "T5", "T2"],
        "rel_to_pivot": ("operationnalisation", "Met en œuvre le couloir opérationnel sans PII du double couloir"),
    },
    {
        "canonical_slug": "canonisation-deterministe-jcs",
        "parent_pivot": "scellage-jcs-scitt",
        "domain_id": "D08",
        "subdomain": "Observabilité OTel GenAI et double couloir probatoire",
        "title": "Canonisation déterministe JCS (RFC 8785) pour idempotence, CIBA et audit",
        "summary": "Sérialisation JSON canonique IEEE-754 et tri UTF-16 (RFC 8785) assurant des condensats SHA-256 reproductibles pour l'épinglage MCP, les clés d'idempotence Saga, les preuves CIBA C.6 et le journal C.8.",
        "autonomy_levels": ["L0", "L1", "L2", "L3", "L4"],
        "roles": ["AS", "RSSI", "SRE"],
        "horizon": "2026–2035",
        "tags": ["JCS", "RFC-8785", "SHA-256", "I-JSON"],
        "identifiers": ["RFC 8785", "EXIG-OBS-12", "PRR R-07"],
        "tome_filter": ["T8", "T5", "T1", "T7"],
        "rel_to_pivot": ("dependance_technique", "Socle de canonisation avant scellement SCITT et SLH-DSA"),
    },
    {
        "canonical_slug": "tests-metamorphiques-fr-en-sans-oracle",
        "parent_pivot": "banc-evalops-hermetique",
        "domain_id": "D08",
        "subdomain": "Banc EvalOps hermétique E1–E3, Wilson et métamorphique",
        "title": "Tests métamorphiques sans oracle et invariance bilingue FR/EN (EXIG-SEC-24)",
        "summary": "Quatre relations métamorphiques (permutation d'outils, invariance injection FR/EN, monotonie budgétaire Decimal, paraphrase avec divulgation non-avis) testées sur >= 100 scénarios ASI01–ASI10 au Tome 8.",
        "autonomy_levels": ["L1", "L2", "L3", "L4"],
        "roles": ["AS", "SRE", "RSSI"],
        "horizon": "2026–2035",
        "tags": ["tests-metamorphiques", "FR-EN", "EXIG-SEC-24", "EXIG-AMF-11"],
        "identifiers": ["EXIG-SEC-24", "EXIG-AMF-11", "G0-EX-CH04-02"],
        "tome_filter": ["T8", "T2", "T1"],
        "rel_to_pivot": ("operationnalisation", "Complète les bancs pass^k/Wilson par tests sans oracle FR/EN"),
    },
    {
        "canonical_slug": "comptabilite-carbone-cap-046-bsif-b15",
        "parent_pivot": "finops-focus-cpo",
        "domain_id": "D08",
        "subdomain": "SRE agentique et FinOps FOCUS / CPO / carbone",
        "title": "Comptabilité énergétique, carbone portée 3 (CAP-046) et BSIF B-15",
        "summary": "Suivi des émissions d'inférence sous FOCUS v1.4 en réponse à la lacune CAP-046 de 2026 et à l'échéance BSIF B-15 portée 3 (fin 2028, ANC-106), couplé au routage frugal SLM et à la contrainte électrique AIE (SIG-016).",
        "autonomy_levels": ["L1", "L2", "L3"],
        "roles": ["AE", "SRE", "Direction"],
        "horizon": "2028–2035",
        "tags": ["CAP-046", "BSIF-B15", "portee-3", "carbone", "FOCUS-1.4"],
        "identifiers": ["CAP-046", "BSIF B-15", "ANC-106", "SIG-016"],
        "tome_filter": ["T8", "T5", "T4"],
        "rel_to_pivot": ("amplification_synergie", "Étend le pilotage FinOps CPO à l'empreinte énergétique et climatique"),
    },
    {
        "canonical_slug": "droit-effacement-portabilite-loi-25",
        "parent_pivot": "loi-25-article-12-1",
        "domain_id": "D09",
        "subdomain": "Droit québécois et prudentiel financier canadien",
        "title": "Droit à la portabilité (art. 27) et purge sélective vérifiable (Loi 25 art. 23)",
        "summary": "Obligations québécoises de communication en format structuré (en vigueur depuis le 22 sept. 2024) et de destruction/anonymisation vérifiable dans les mémoires CoALA et index RAG (EXIG-CON-10, PRR G-10).",
        "autonomy_levels": ["L1", "L2", "L3"],
        "roles": ["Juridique", "AE", "AS"],
        "horizon": "2024–2035",
        "tags": ["Loi-25-art-23", "portabilite", "oubli-selectif", "EXIG-CON-10"],
        "identifiers": ["EXIG-CON-10", "PRR G-10", "ANC-115"],
        "tome_filter": ["T5", "T4", "T3", "T2"],
        "rel_to_pivot": ("amplification_synergie", "Complète l'art. 12.1 Loi 25 sur la gouvernance mémorielle"),
    },
    {
        "canonical_slug": "systeme-qualite-en-18286-dora-cra",
        "parent_pivot": "eu-ai-act",
        "domain_id": "D09",
        "subdomain": "Réglementation européenne et référentiels internationaux",
        "title": "Système de management de la qualité EN 18286:2026, DORA et Cyber Resilience Act",
        "summary": "Articulation européenne de l'article 17 du RIA (présomption de conformité via EN 18286:2026 intégrée en CRE-IA v1.2 EXIG-CON-30), des tests de résilience DORA (art. 24–26) et des exigences SBOM du CRA.",
        "autonomy_levels": ["L2", "L3", "L4"],
        "roles": ["Juridique", "AE", "RSSI"],
        "horizon": "2026–2030",
        "tags": ["EN-18286", "DORA", "CRA", "SMQ", "EXIG-CON-30"],
        "identifiers": ["EXIG-CON-30", "EN 18286:2026", "DORA", "CRA"],
        "tome_filter": ["T8", "T5", "T2", "T4"],
        "rel_to_pivot": ("operationnalisation", "Concrétise les exigences QMS et résilience de l'EU AI Act"),
    },
    {
        "canonical_slug": "cadres-internationaux-imda-aica-g7",
        "parent_pivot": "iso-iec-42001-nist",
        "domain_id": "D09",
        "subdomain": "Réglementation européenne et référentiels internationaux",
        "title": "Repères internationaux IMDA (Singapour), AICA/IAIS et feuille de route G7",
        "summary": "Alignement comparatif sur le Model AI Governance Framework for Agentic AI v1.5 de l'IMDA (juin 2026), les principes IA en assurance de l'AICA/IAIS et la coordination PQC financière du G7 Cyber Expert Group.",
        "autonomy_levels": ["L1", "L2", "L3", "L4"],
        "roles": ["AE", "Juridique", "Direction"],
        "horizon": "2026–2035",
        "tags": ["IMDA-v1.5", "AICA", "IAIS", "G7-CEG"],
        "identifiers": ["IMDA v1.5", "AICA", "G7 CEG"],
        "tome_filter": ["T5", "T4", "T1"],
        "rel_to_pivot": ("concordance_inter_tomes", "Complète NIST AI RMF et ISO 42001 (statut F) par les repères IMDA/AICA/G7"),
    },
    {
        "canonical_slug": "blueprint-1-assistant-sor",
        "parent_pivot": "blueprints-reference-multisectoriels",
        "domain_id": "D10",
        "subdomain": "Trois blueprints de référence et cas Groupe Boréal BEL",
        "title": "Blueprint 1 — Traitement transactionnel réglementé orienté SoR (bp1_assistant_interne)",
        "summary": "Premier blueprint de référence (Tome 6 §14.1, validé en Tome 8 ch. 04 sous bp1_assistant_interne) couvrant l'orchestration durable Temporal, adaptateurs SoR sans SQL direct, 5 SBB et critères C01–C40.",
        "autonomy_levels": ["L1", "L2", "L3"],
        "roles": ["AS", "AE"],
        "horizon": "2026–2028",
        "tags": ["Blueprint-1", "SoR", "bp1_assistant_interne", "C01-C40"],
        "identifiers": ["bp1_assistant_interne", "C01", "C40"],
        "tome_filter": ["T6", "T8"],
        "rel_to_pivot": ("operationnalisation", "Instanciation du Blueprint 1 orienté systèmes d'enregistrement"),
    },
    {
        "canonical_slug": "blueprint-2-enclave-rag-acl",
        "parent_pivot": "blueprints-reference-multisectoriels",
        "domain_id": "D10",
        "subdomain": "Trois blueprints de référence et cas Groupe Boréal BEL",
        "title": "Blueprint 2 — Enclave souveraine haute confidentialité & RAG ACL (bp2_rag_entreprise_acl)",
        "summary": "Blueprint souverain (Tome 6 §14.3, identifié bp2_rag_entreprise_acl dans la trousse Tome 8) unissant AI Gateway locale, filtrage ACL amont, confinement microVM sans sortie réseau, 5 SBB et C01–C40.",
        "autonomy_levels": ["L1", "L2", "L3"],
        "roles": ["AS", "RSSI", "AE"],
        "horizon": "2026–2030",
        "tags": ["Blueprint-2", "RAG-ACL", "bp2_rag_entreprise_acl", "souverainete"],
        "identifiers": ["bp2_rag_entreprise_acl", "C15", "C16"],
        "tome_filter": ["T6", "T8"],
        "rel_to_pivot": ("operationnalisation", "Instanciation souveraine à haute confidentialité avec RAG ACL"),
    },
    {
        "canonical_slug": "blueprint-3-maillage-b2b",
        "parent_pivot": "blueprints-reference-multisectoriels",
        "domain_id": "D10",
        "subdomain": "Trois blueprints de référence et cas Groupe Boréal BEL",
        "title": "Blueprint 3 — Maillage inter-départemental et B2B (bp3_orchestration_multi_agents_b2b)",
        "summary": "Blueprint fédéré (Tome 6 §14.2, identifié bp3_orchestration_multi_agents_b2b au Tome 8) combinant A2A, AGNTCY/SLIM, Event Mesh CloudEvents, délégation OBO 2 sauts, 5 SBB et critères C01–C40.",
        "autonomy_levels": ["L2", "L3", "L4"],
        "roles": ["AS", "AE", "RSSI"],
        "horizon": "2027–2035",
        "tags": ["Blueprint-3", "B2B", "bp3_orchestration_multi_agents_b2b", "A2A"],
        "identifiers": ["bp3_orchestration_multi_agents_b2b", "C13", "C20"],
        "tome_filter": ["T6", "T8"],
        "rel_to_pivot": ("operationnalisation", "Instanciation du maillage inter-départemental et B2B"),
    },
    {
        "canonical_slug": "quinze-portes-homologation-por",
        "parent_pivot": "trajectoires-adaptatives-dapp",
        "domain_id": "D11",
        "subdomain": "Scénarios 2028–2035, trajectoires DAPP et portes POR/SIG",
        "title": "Quinze portes d'homologation de trajectoire (POR-001 à POR-016)",
        "summary": "Portes sur preuves système conditionnant le franchissement des Paliers P1 (POR-001..004), P2 (POR-005..009), P3 (POR-011..014) et la rétrogradation transversale (< 60 s POR-015, revue CPO POR-016).",
        "autonomy_levels": ["L1", "L2", "L3", "L4"],
        "roles": ["AE", "Direction", "Juridique"],
        "horizon": "2028–2035",
        "tags": ["POR-001..016", "DAPP", "P1-P3"],
        "identifiers": ["POR-001", "POR-007", "POR-015", "POR-016"],
        "tome_filter": ["T4", "T5"],
        "rel_to_pivot": ("operationnalisation", "Jalons de validation par preuves système de la trajectoire DAPP"),
    },
    {
        "canonical_slug": "vingt-sept-signaux-veille-sig",
        "parent_pivot": "trajectoires-adaptatives-dapp",
        "domain_id": "D11",
        "subdomain": "Scénarios 2028–2035, trajectoires DAPP et portes POR/SIG",
        "title": "Observatoire des 27 signaux de bascule DAPP (SIG-001..017, SIG-101..110)",
        "summary": "Signaux réglementaires, normalisateurs, post-quantiques, capacités et marché déclenchant une décision budgétaire ou architecturale sous 30 jours sans veille décorative (Tome 4 ch. M-25 / Annexe F, Tome 5, Tome 7).",
        "autonomy_levels": ["L1", "L2", "L3", "L4"],
        "roles": ["AE", "Direction", "Juridique"],
        "horizon": "2026–2035",
        "tags": ["SIG-001..110", "veille-signaux", "DAPP"],
        "identifiers": ["SIG-001", "SIG-009", "SIG-017", "SIG-101", "SIG-110"],
        "tome_filter": ["T4", "T5", "T7"],
        "rel_to_pivot": ("dependance_technique", "Déclencheurs mesurables gouvernant les bascules conditionnelles DAPP"),
    },
    {
        "canonical_slug": "dix-theses-t1-t10-tome-5",
        "parent_pivot": "gouvernance-duale-ae-as",
        "domain_id": "D11",
        "subdomain": "Gouvernance duale AE ↔ AS, thèses T1–T10 et pièges",
        "title": "Dix thèses structurantes (T1–T10) et six décisions conjointes AE ↔ AS",
        "summary": "Synthèse doctrinale du Tome 5 soudant les arbitrages portefeuille de l'Architecte d'entreprise (AE) et les spécifications techniques de l'Architecte de solutions (AS) sur l'horizon 2026–2035.",
        "autonomy_levels": ["L0", "L1", "L2", "L3", "L4"],
        "roles": ["AE", "AS", "Direction"],
        "horizon": "2026–2035",
        "tags": ["T1-T10", "AE-AS", "synthese-executive"],
        "identifiers": ["T1", "T10", "T5 Synthèse"],
        "tome_filter": ["T5", "R"],
        "rel_to_pivot": ("concordance_inter_tomes", "Formalise le contrat doctrinal croisé entre AE et AS"),
    },
    {
        "canonical_slug": "approbation-reflexe-biais-automatisation",
        "parent_pivot": "pieges-gouvernance",
        "domain_id": "D11",
        "subdomain": "Capital humain, atrophie des compétences et dynamique énergie/marché",
        "title": "Approbation réflexe (automation bias), dossiers témoins et vue différentielle",
        "summary": "Prévention de l'approbation machinale (ASI09, Goddard et al.) exposant au régime des décisions exclusivement automatisées (Loi 25 art. 12.1), via écrans différentiels, temps minimal de revue et dossiers témoins.",
        "autonomy_levels": ["L1", "L2", "L3", "L4"],
        "roles": ["AE", "AS", "Juridique", "Direction"],
        "horizon": "2026–2035",
        "tags": ["biais-automatisation", "rubber-stamping", "ASI09", "dossiers-temoins"],
        "identifiers": ["PRR G-11", "PRR G-12", "EXIG-AUT-19", "POR-014"],
        "tome_filter": ["T7", "T5", "T2", "T3"],
        "rel_to_pivot": ("attenuation_risque", "Parade ergonomique et organisationnelle contre l'approbation réflexe"),
    },
    {
        "canonical_slug": "sanctuarisation-vivier-junior-reprise",
        "parent_pivot": "atrophie-competences-humaines",
        "domain_id": "D11",
        "subdomain": "Capital humain, atrophie des compétences et dynamique énergie/marché",
        "title": "Sanctuarisation du vivier junior (quota > 70 % INI-043) et exercices de reprise manuelle",
        "summary": "Mesures architecturales contre la perte de relève et de capacité de reprise humaine : quota de dossiers formateurs dès 70 % d'automatisation (INI-043) et exercices annuels de reprise sans agent (POR-009, POR-014).",
        "autonomy_levels": ["L1", "L2", "L3", "L4"],
        "roles": ["Direction", "AE", "SRE"],
        "horizon": "2026–2035",
        "tags": ["vivier-junior", "reprise-manuelle", "INI-043", "POR-009"],
        "identifiers": ["INI-043", "POR-009", "POR-014"],
        "tome_filter": ["T4", "T5", "T7"],
        "rel_to_pivot": ("operationnalisation", "Garantit concrètement le maintien des compétences et la relève"),
    },
    {
        "canonical_slug": "dix-interdictions-exig-gov-17",
        "parent_pivot": "exigences-cre-ia-305",
        "domain_id": "D12",
        "subdomain": "Exigences CRE-IA-2026-01, PRR-75 et 24 portes bloquantes",
        "title": "Dix interdictions sans dérogation (EXIG-GOV-17) et protocole d'exception",
        "summary": "Noyau dur absolu ne tolérant aucune dispense à l'homologation (NX interdit, P3 sans CIBA, usurpation d'identité, relais de jeton, fiche absente, règle d'or, Règle de deux, audit manquant, manquement légal) réconcilié aux 46 ND de CAD26.",
        "autonomy_levels": ["L0", "L1", "L2", "L3", "L4"],
        "roles": ["AE", "RSSI", "Juridique", "Direction"],
        "horizon": "2026–2035",
        "tags": ["EXIG-GOV-17", "non-derogeable", "lignes-rouges"],
        "identifiers": ["EXIG-GOV-17", "EXIG-AUT-03", "EXIG-SEC-06", "EXIG-OBS-11"],
        "tome_filter": ["T2", "T5"],
        "rel_to_pivot": ("encadrement_normatif", "Noyau non dérogeable prioritaire dans l'ordre d'arbitrage CRE-IA"),
    },
    {
        "canonical_slug": "cinq-blocs-sbb-tableau-12",
        "parent_pivot": "trousse-executable-tome-8",
        "domain_id": "D12",
        "subdomain": "Trousse exécutable Tome 8 et vecteurs tiers",
        "title": "Cinq blocs de solution critiques (5 SBB du Tableau 12) et fiche 2027-B001",
        "summary": "Implémentation de référence en Tome 8 des 5 SBB laissés vides au Tableau 12 du Tome 2 (secrets_vault, guardrails_engine, signed_human_approval_service, immutable_audit_ledger, finops_budget_quota_controller) et validateur YAML/JSON Schema 2027-B001.",
        "autonomy_levels": ["L2", "L3", "L4"],
        "roles": ["AS", "SRE", "RSSI"],
        "horizon": "2026–2030",
        "tags": ["5-SBB", "Tableau-12", "2027-B001", "Adr2027B001"],
        "identifiers": ["SBB-SECRETS-VAULT", "SBB-GUARDRAILS-ENGINE", "SBB-SIGNED-HUMAN-APPROVAL", "SBB-IMMUTABLE-AUDIT-LEDGER", "SBB-FINOPS-BUDGET-QUOTA", "2027-B001"],
        "tome_filter": ["T8", "T2"],
        "rel_to_pivot": ("operationnalisation", "Comble exécutablement les 5 emplacements SBB du Tableau 12"),
    },
    {
        "canonical_slug": "cinq-discordances-inter-volumes-tome-8",
        "parent_pivot": "concordance-inter-tomes-div02",
        "domain_id": "D12",
        "subdomain": "Concordance inter-tomes (DIV-02, DISC-01..05) et Wyvern G0–G5",
        "title": "Résolution des cinq discordances inter-volumes (DISC-01 à DISC-05, Tome 8 §0.2)",
        "summary": "Table canonique de passage levant les cinq divergences entre Tomes 1–7 : L0–L4 déterministe vs lecture IA (DISC-01), 3 criticités et P0–P3 (DISC-02), Plans A/B/C et 4 modules (DISC-03), neutralité ArchiMate 3.2/4.0 (DISC-04) et épinglage MCP 2026-07-28 (DISC-05).",
        "autonomy_levels": ["L0", "L1", "L2", "L3", "L4"],
        "roles": ["AE", "AS", "SRE"],
        "horizon": "2026–2035",
        "tags": ["DISC-01", "DISC-02", "DISC-03", "DISC-04", "DISC-05"],
        "identifiers": ["DISC-01", "DISC-02", "DISC-03", "DISC-04", "DISC-05"],
        "tome_filter": ["T8"],
        "rel_to_pivot": ("concordance_inter_tomes", "Prolonge la fermeture DIV-02 en unifiant les 5 discordances pour le code G0"),
    },
    {
        "canonical_slug": "barriere-logicielle-g0-execute-g0",
        "parent_pivot": "protocole-wyvern-g0-g5",
        "domain_id": "D12",
        "subdomain": "Trousse exécutable Tome 8 et vecteurs tiers",
        "title": "Barrière logicielle G0 (execute_g0.py), 4 suites vecteurs tiers et CA-G0-SYNC",
        "summary": "Vérification hermétique à exit 0 (83/83 pytest, 45/45 OPA à 100 % de couverture, 21 validations sur 13 schémas JSON Schema 2020-12 stricts, 4 suites tierces RFC 8785 / NIST ACVP / a2a-tck / OWASP SRC-055 sur 50 fichiers, SPDX MIT et 14 extraits SHA-256 CA-G0-SYNC).",
        "autonomy_levels": ["L0", "L1", "L2", "L3", "L4"],
        "roles": ["AS", "SRE", "RSSI"],
        "horizon": "2026-2030",
        "tags": ["G0", "execute_g0", "CA-G0-SYNC", "vecteurs-tiers", "Oracle-Batisseur"],
        "identifiers": ["G0", "CA-G0-SYNC", "G0-EX-CH01-01", "G0-EX-CH04-03"],
        "tome_filter": ["T8", "R"],
        "rel_to_pivot": ("operationnalisation", "Ancre logicielle à exit 0 en amont des barrières éditoriales G1–G5"),
    },
    {
        "canonical_slug": "gabarit-typst-edition-4542-pages",
        "parent_pivot": "protocole-wyvern-g0-g5",
        "domain_id": "D12",
        "subdomain": "Concordance inter-tomes (DIV-02, DISC-01..05) et Wyvern G0–G5",
        "title": "Chaîne éditoriale Typst 6,14×9,21 po (4 542 pages, 319 diagrammes) et recollation CA-16",
        "summary": "Unification typographique des 8 ouvrages (4 542 pages PDF, 319 diagrammes dont 253 PlantUML .svg et 66 Mermaid .png), éditions HTML autonomes T7–T8, recollations stratifiées G3/CA-16 (40/40 T5, 60/60 T7/T8) et inspection visuelle G5.",
        "autonomy_levels": ["L0", "L1"],
        "roles": ["AE", "AS", "Direction"],
        "horizon": "2026-2027",
        "tags": ["Typst", "4542-pages", "319-diagrammes", "CA-16", "G5"],
        "identifiers": ["CA-16", "G3", "G4", "G5", "Typst"],
        "tome_filter": ["R", "T5", "T7", "T8"],
        "rel_to_pivot": ("operationnalisation", "Matérialise l'assurance qualité G1–G5 et l'édition unifiée du corpus"),
    },
]


def normalize_text(text: str) -> str:
    """Normalise grossièrement une chaîne pour comparaison par mots-clés."""
    s = text.lower()
    for a, b in [("é", "e"), ("è", "e"), ("ê", "e"), ("à", "a"), ("â", "a"), ("î", "i"), ("ô", "o"), ("û", "u"), ("ù", "u"), ("ç", "c"), ("œ", "oe")]:
        s = s.replace(a, b)
    return s


def normalize_horizon(value: str) -> str:
    """Normalise les tirets d'un horizon temporel vers le tiret ASCII '-'."""
    return str(value).strip().replace("–", "-").replace("—", "-")


# Corrections ciblées d'occurrences de shards pointant hors de la sous-section exacte
OCCURRENCE_FIXES: dict[tuple[str, str, int], dict[str, Any]] = {
    ("agntcy-slim", "T7", 124): {
        "line_start": 34,
        "line_end": 37,
        "section": "0.1 De l'humain intégrateur au tissu conjonctif agentique",
    },
    ("did-vc-passeport-agent", "T7", 146): {
        "line_start": 56,
        "line_end": 71,
        "section": "0.2 L'interopérabilité au-delà du transport syntaxique",
    },
}


# Métadonnées curées en fr-CA pour les 24 unités non couvertes directement par chapters_mapped
CURATED_UNIT_METADATA: dict[str, dict[str, Any]] = {
    "r-u0002": {
        "themes": [
            "trousse-executable-tome-8",
            "concordance-inter-tomes-div02",
            "gabarit-typst-edition-4542-pages",
            "clause-non-avis-licences",
        ],
        "replace_themes": True,
        "summary": "Table maîtresse des huit tomes de la collection (PDF et Markdown intégraux de Corpus/, éditions structurées Tomes/, horizons 2024-2035, pagination physique 4 542 pages et liens vers les éditions HTML autonomes T7–T8 ainsi que la trousse exécutable du Tome 8).",
        "key_terms": ["Tomes 1 à 8", "Corpus", "Typst", "4 542 pages", "HTML autonome", "trousse exécutable"],
    },
    "r-u0003": {
        "themes": [
            "protocole-wyvern-g0-g5",
            "barriere-logicielle-g0-execute-g0",
            "gabarit-typst-edition-4542-pages",
            "trousse-executable-tome-8",
            "clause-non-avis-licences",
        ],
        "replace_themes": True,
        "summary": "Métriques consolidées et bilans d'assurance qualité de la collection : 3 973 pages / 287 diagrammes (T1–T6), bilans Wyvern G1–G5 du Tome 7 (258 p., 79 sources L+ SHA-256), barrières G0–G5 du Tome 8 (311 p., 83/83 pytest, 45/45 OPA, 13 schémas JSON Schema 2020-12 stricts, 4 suites tierces), licences CC-BY-4.0 / MIT et clause non-avis DC-P12.",
        "key_terms": ["G0–G5", "Typst", "319 diagrammes", "79 sources L+", "95 sources L+", "CC-BY-4.0", "MIT", "DC-P12"],
    },
    "t2-u0274": {
        "themes": [
            "grille-homologation-et-fiche-agent",
            "exigences-cre-ia-305",
            "registre-agents-cycle-de-vie-et-attestations",
            "contrats-types-executes-ci-annexe-c",
            "glossaire-normatif-tome-2",
            "audit-validation-sources-121-449",
            "actualisation-novembre-2026-unification-v1-2",
            "clause-non-avis-licences",
        ],
        "replace_themes": False,
        "summary": "Ensemble des huit annexes opérationnelles du Tome 2 (A à H) : grille d'homologation avant production, gabarit de fiche d'agent, exemples de contrats exécutés en CI, registre des 305 exigences EXIG-*, glossaire normatif, audit des sources, bibliographie et actualisation CRE-IA v1.2 (AMF, PQC NIST IR 8547, ACVM 11-348, EN 18286).",
        "key_terms": ["Annexes A–H", "EXIG-*", "fiche d'agent", "contrats CI", "CRE-IA-2026-01 v1.2"],
    },
    "t3-u1898": {
        "themes": [
            "referentiel-annexes-protocoles-chronologie",
            "homologation-prr-75-points",
            "decisions-architecture-adr-001-031",
            "protocole-probatoire-l-plus-statut-f",
            "protocole-mcp",
            "protocole-a2a",
            "agntcy-slim",
            "regle-maillon-plus-eleve",
            "observabilite-otel-genai",
            "loi-25-article-12-1",
        ],
        "replace_themes": False,
        "summary": "Ensemble des huit annexes techniques du Tome 3 (A à H) : glossaire bilingue, fiches protocoles (MCP, A2A, AGNTCY/SLIM, AP2), grilles comparatives, chronologie 2024-2028, bibliographie probatoire L+/F, catalogue ADR-001 à ADR-031, liste PRR-75 points avant production et index des standards.",
        "key_terms": ["Annexes A–H", "PRR-75", "ADR-001..031", "MCP", "A2A", "AGNTCY/SLIM", "L+"],
    },
    "t4-u0411": {
        "themes": [
            "noyau-controle-possede-cap",
            "trajectoires-adaptatives-dapp",
            "concordance-inter-tomes-div02",
            "principes-architecture-pri-001-015",
            "catalogue-31-adr-12-dec",
            "quinze-portes-homologation-por",
            "vingt-sept-signaux-veille-sig",
            "bsif-e-23",
            "eu-ai-act",
            "post-quantique-ml-dsa-slh-dsa",
        ],
        "replace_themes": False,
        "summary": "Ensemble des huit annexes prospectives du Tome 4 (A à H) : calendrier consolidé 2027-2035, registres CAP-001 à CAP-052, PRI/DEC/POR-001..016/INI/PEX, matrice de traçabilité sectorielle, correspondances des modèles de maturité, observatoire des 27 signaux SIG, glossaire et bibliographie.",
        "key_terms": ["Annexes A–H", "CAP-052", "POR-001..016", "SIG-001..110", "DAPP", "PQC"],
    },
    "t5-u0098": {
        "themes": [
            "concordance-inter-tomes-div02",
            "echelle-autonomie-l0-l4",
            "noyau-controle-possede-cap",
            "exigences-cre-ia-305",
            "catalogue-31-adr-12-dec",
            "regle-de-deux-opa",
            "scellage-jcs-scitt",
            "protocole-wyvern-g0-g5",
            "clause-non-avis-licences",
            "profil-banque-m14",
        ],
        "replace_themes": False,
        "summary": "Six annexes instrumentales du Tome 5 (A à F) : tables de concordance 2026-2035 et pont CAP/PEX vers EXIG-*, catalogue de poche des décisions AE/AS, grille unifiée d'homologation, guide d'orientation vers les tomes sources, glossaire de 385 sigles et bibliographie primaire sélective (70 sources).",
        "key_terms": ["Annexes A–F", "pont CAP/PEX -> EXIG-*", "glossaire 385 entrées", "AE/AS", "DIV-02"],
    },
    "t6-u0004": {
        "themes": [
            "protocole-wyvern-g0-g5",
            "clause-non-avis-licences",
            "gabarit-typst-edition-4542-pages",
        ],
        "replace_themes": True,
        "summary": "Colophon éditorial du Tome 6 documentant la production agentique sous protocole Wyvern, le contrôle probatoire des assertions factuelles sur sources primaires (statut F) et le renvoi explicite aux clauses de licences et de non-avis.",
        "key_terms": ["Wyvern", "statut F", "colophon", "non-avis", "CC-BY-4.0"],
    },
    "t6-u0005": {
        "themes": [
            "gouvernance-duale-ae-as",
            "partition-hybride-80-20",
            "cadre-togaf-archimate-4-plans",
            "echelle-autonomie-l0-l4",
            "bsif-e-23",
            "finops-focus-cpo",
            "clause-non-avis-licences",
        ],
        "replace_themes": True,
        "summary": "Résumé exécutif destiné à l'architecture d'entreprise (AE) : équilibre entre accélération agentique et maîtrise prudentielle (BSIF E-23, AMF, Loi 25), ancrage sur le cadre TOGAF/ArchiMate à 4 plans, partition 80/20, paliers d'autonomie L0–L4 et pilotage FinOps par coût par résultat (CPO).",
        "key_terms": ["AE", "TOGAF/ArchiMate", "80/20", "L0–L4", "BSIF E-23", "CPO"],
    },
    "t6-u0006": {
        "themes": [
            "partition-hybride-80-20",
            "harnais-deterministe-8-etapes",
            "protocole-mcp",
            "protocole-a2a",
            "memoire-coala-4-tiroirs",
            "saga-compensatoire",
            "blueprints-reference-multisectoriels",
        ],
        "replace_themes": True,
        "summary": "Résumé exécutif destiné à l'architecture de solutions (AS) : mise en œuvre du harnais déterministe 80/20 en huit étapes, médiation MCP et A2A, mémoire CoALA à quatre tiroirs, exécution durable et compensation Saga avant d'instancier les trois blueprints multisectoriels.",
        "key_terms": ["AS", "harnais 8 étapes", "MCP", "A2A", "CoALA", "Saga", "blueprints"],
    },
    "t6-u0007": {
        "themes": [
            "gouvernance-duale-ae-as",
            "cadre-togaf-archimate-4-plans",
            "partition-hybride-80-20",
            "blueprints-reference-multisectoriels",
            "protocole-wyvern-g0-g5",
        ],
        "replace_themes": True,
        "summary": "Guide d'orientation du Tome 6 par profil (AE, AS, RSSI, FinOps, juridique, SRE) et conventions de modélisation ArchiMate et C4 appliquées uniformément aux blueprints multisectoriels.",
        "key_terms": ["parcours de lecture", "ArchiMate", "C4", "AE/AS", "blueprints"],
    },
    "t7-u0002": {
        "themes": [
            "systems-of-agency",
            "agntcy-slim",
            "protocole-mcp",
            "protocole-a2a",
            "bsif-e-23",
            "iso-iec-42001-nist",
            "eu-ai-act",
        ],
        "replace_themes": True,
        "summary": "Analyse le basculement des systèmes d'enregistrement vers les systems of agency et le tissu conjonctif inter-agent (MCP, A2A, AGNTCY, NANDA), et montre pourquoi la souveraineté exige de reprendre la propriété de la couche de contrôle sous contrainte BSIF E-23, NIST et EU AI Act.",
        "key_terms": ["systems of agency", "MCP", "A2A", "AGNTCY", "NANDA", "souveraineté", "BSIF E-23"],
    },
    "t7-u0003": {
        "themes": [
            "systems-of-agency",
            "did-vc-passeport-agent",
            "protocole-mcp",
            "protocole-a2a",
            "dette-semantique-ontologies",
            "memoire-coala-4-tiroirs",
            "saga-compensatoire",
            "supervision-hitl-hotl-abstention",
            "bsif-e-23",
        ],
        "replace_themes": True,
        "summary": "Démontre pourquoi l'interopérabilité syntaxique (MCP/A2A) est nécessaire mais insuffisante : elle doit être complétée par des ontologies partagées, une mémoire CoALA gouvernée, une sémantique transactionnelle Saga, des passeports vérifiables DID/VC et une supervision humaine calibrée.",
        "key_terms": ["interopérabilité sémantique", "ontologies", "CoALA", "Saga", "DID/VC", "HITL/HOTL"],
    },
    "t7-u0004": {
        "themes": [
            "loi-de-lusser",
            "erreurs-silencieuses-cascade",
            "partition-hybride-80-20",
            "arbre-sobriete-oo1-oo4",
            "saga-compensatoire",
            "trajectoires-adaptatives-dapp",
        ],
        "replace_themes": True,
        "summary": "Énonce l'orchestration agentique comme discipline de retenue : loi de Lusser sur la chute de fiabilité en chaîne, amplification silencieuse d'erreurs, arbitrage entre autonomie et partition déterministe 80/20, sobriété de topologie, compensation Saga et trajectoires adaptatives DAPP.",
        "key_terms": ["loi de Lusser", "cascade d'erreurs", "80/20", "sobriété", "Saga", "DAPP"],
    },
    "t7-u0005": {
        "themes": [
            "echelle-autonomie-l0-l4",
            "regle-maillon-plus-eleve",
            "partition-hybride-80-20",
            "atrophie-competences-humaines",
            "trajectoires-adaptatives-dapp",
            "supervision-hitl-hotl-abstention",
        ],
        "replace_themes": True,
        "summary": "Présente l'architecture en quatre parties du Tome 7, énonce la règle du maillon le plus élevé (alignement de la gouvernance sur l'acteur au plus haut niveau L0–L4) et avertit contre l'atrophie silencieuse des compétences humaines et de reprise manuelle à l'horizon 2035.",
        "key_terms": ["quatre parties", "règle du maillon le plus élevé", "L0–L4", "atrophie des compétences", "capital humain"],
    },
    "t7-u0006": {
        "themes": [
            "clause-non-avis-licences",
            "protocole-wyvern-g0-g5",
            "protocole-mcp",
            "protocole-a2a",
            "bsif-e-23",
            "loi-25-article-12-1",
            "eu-ai-act",
        ],
        "replace_themes": True,
        "summary": "Délimite la frontière probatoire du Tome 7 : distinction entre évidences datées (gel des faits au 2 décembre 2026) et projections prospectives 2027-2035, mention des sources de statut F, transparence des protocoles/lois cités et rappel de la clause de non-avis.",
        "key_terms": ["hygiène probatoire", "gel 2 décembre 2026", "statut F", "non-avis"],
    },
    "t7-u0007": {
        "themes": [
            "protocole-wyvern-g0-g5",
            "clause-non-avis-licences",
            "gabarit-typst-edition-4542-pages",
        ],
        "replace_themes": True,
        "summary": "Colophon d'intégrité du Tome 7 précisant le protocole d'ancrage et de révision Wyvern (G1–G5), les licences duales CC-BY-4.0 (texte et figures) et MIT (outillage), le format Typst unifié et l'avis de non-conseil juridique ou prudentiel.",
        "key_terms": ["Wyvern G1–G5", "CC-BY-4.0", "MIT", "Typst", "non-avis"],
    },
    "t7-u0083": {
        "themes": [
            "noyau-controle-possede-cap",
            "partition-hybride-80-20",
            "regle-de-deux-opa",
            "injection-indirecte-prompt",
            "trajectoires-adaptatives-dapp",
            "loi-25-article-12-1",
            "bsif-e-23",
            "eu-ai-act",
            "protocole-wyvern-g0-g5",
            "did-vc-passeport-agent",
        ],
        "replace_themes": False,
        "summary": "Trois annexes de référence du Tome 7 (A à C) : glossaire raisonné français-anglais de l'entreprise agentique, chronologie réglementaire et cryptographique consolidée 2026-2035, méthodologie bibliométrique, bibliographie L+ hachée SHA-256 et bilan d'assurance qualité G1–G5.",
        "key_terms": ["Annexes A–C", "glossaire", "chronologie 2026-2035", "79 sources L+", "G1–G5"],
    },
    "t8-u0002": {
        "themes": [
            "bsif-e-23",
            "trousse-executable-tome-8",
            "harnais-deterministe-8-etapes",
            "epinglage-schemas-mcp",
            "constance-pass-k",
            "exigences-cre-ia-305",
            "partition-hybride-80-20",
        ],
        "replace_themes": True,
        "summary": "Pose le problème central du Tome 8 : combler l'écart entre la norme en prose (CRE-IA-2026-01, BSIF E-23) et la preuve logicielle exécutable, en traduisant l'invariance sémantique, l'épinglage MCP, les bornes décimales et la constance pass^k dans un harnais déterministe 80/20.",
        "key_terms": ["CRE-IA-2026-01", "BSIF E-23", "preuve exécutable", "épinglage MCP", "pass^k", "harnais 80/20"],
    },
    "t8-u0003": {
        "themes": [
            "cadre-togaf-archimate-4-plans",
            "concordance-inter-tomes-div02",
            "echelle-autonomie-l0-l4",
            "noyau-controle-possede-cap",
            "cinq-discordances-inter-volumes-tome-8",
            "adaptateur-mcp-streamable-http-sep-3398",
        ],
        "replace_themes": True,
        "summary": "Établit la table canonique de passage entre les Tomes 1–7 et le code du Tome 8 en fermant les cinq discordances inter-volumes (DISC-01 à DISC-05) : niveaux L0–L4 déterministes, 3 criticités / P0–P3, Plans A/B/C, neutralité ArchiMate et épinglage MCP 2026-07-28.",
        "key_terms": ["DISC-01..05", "table de passage", "L0–L4", "ArchiMate", "MCP 2026-07-28"],
    },
    "t8-u0004": {
        "themes": [
            "trousse-executable-tome-8",
            "cinq-blocs-sbb-tableau-12",
            "barriere-logicielle-g0-execute-g0",
            "clause-non-avis-licences",
        ],
        "replace_themes": True,
        "summary": "Décrit l'architecture bicéphale du Tome 8 combinant un manuel de spécifications testables (licence CC-BY-4.0) et une trousse logicielle exécutable MIT couvrant les 5 SBB critiques du Tableau 12 sous barrière logicielle G0 (execute_g0.py).",
        "key_terms": ["architecture bicéphale", "manuel CC-BY-4.0", "trousse MIT", "5 SBB", "G0"],
    },
    "t8-u0005": {
        "themes": [
            "trousse-executable-tome-8",
            "harnais-deterministe-8-etapes",
            "delegation-obo-deux-sauts",
            "politiques-opa-rego-hors-modele",
            "saga-compensatoire",
            "banc-evalops-hermetique",
            "cinq-blocs-sbb-tableau-12",
        ],
        "replace_themes": True,
        "summary": "Structure les deux parties et quatre modules exécutables Python/OPA du Tome 8 : harnais déterministe 8 étapes et médiation MCP/A2A (ch. 01), délégation OBO deux sauts / CIBA / PQC (ch. 02), politiques OPA hors modèle et Saga (ch. 03) et suite EvalOps métamorphique PRR-75 / C01–C40 (ch. 04).",
        "key_terms": ["quatre modules", "Python/OPA", "harnais", "OBO/PQC", "OPA/Saga", "EvalOps"],
    },
    "t8-u0006": {
        "themes": [
            "anti-verrouillage-standards",
            "certificats-tls-47-jours",
            "clause-non-avis-licences",
            "iso-iec-42001-nist",
            "ligne-directrice-amf",
            "trousse-executable-tome-8",
            "barriere-logicielle-g0-execute-g0",
            "bsif-e-23",
            "loi-25-article-12-1",
            "eu-ai-act",
        ],
        "replace_themes": True,
        "summary": "Fixe l'hygiène probatoire du Tome 8 au gel du 2 décembre 2026 : quatre suites officielles de vecteurs tiers (RFC 8785, NIST ACVP, a2a-tck, OWASP SRC-055), échéances TLS 47 jours et réglementaires (BSIF E-23, AMF, Loi 25, EU AI Act), mention statut F et délimitation hors modèle DC-P12.",
        "key_terms": ["gel 2 décembre 2026", "vecteurs tiers", "TLS 47 jours", "DC-P12", "statut F"],
    },
    "t8-u0007": {
        "themes": [
            "protocole-wyvern-g0-g5",
            "clause-non-avis-licences",
            "barriere-logicielle-g0-execute-g0",
            "trousse-executable-tome-8",
            "gabarit-typst-edition-4542-pages",
        ],
        "replace_themes": True,
        "summary": "Colophon d'intégrité du Tome 8 attestant la validation des six barrières G0–G5 (83/83 pytest, 45/45 OPA, 21 validations sur 13 schémas JSON Schema 2020-12 stricts, CA-G0-SYNC, CA-16), le gabarit Typst et la clause de non-avis juridique ou prudentiel (AO-05).",
        "key_terms": ["G0–G5", "83/83 pytest", "45/45 OPA", "13 schémas", "CA-G0-SYNC", "AO-05"],
    },
    "t8-u0081": {
        "themes": [
            "protocole-wyvern-g0-g5",
            "trousse-executable-tome-8",
            "exigences-cre-ia-305",
            "concordance-inter-tomes-div02",
            "clause-non-avis-licences",
            "harnais-deterministe-8-etapes",
            "delegation-obo-deux-sauts",
            "politiques-opa-rego-hors-modele",
            "banc-evalops-hermetique",
            "barriere-logicielle-g0-execute-g0",
        ],
        "replace_themes": False,
        "summary": "Deux annexes de référence du Tome 8 (A et B) : registre des 95 sources primaires L+ SHA-256, statut F et journaux d'ancrage atomique Wyvern G2 (chapitres 00 à 04), suivis de la matrice complète EXIG/CAP/PRR-75/C01–C40/5 SBB, du catalogue des vecteurs tiers et du bilan AQ G0–G5 & CA-16.",
        "key_terms": ["Annexes A–B", "95 sources L+", "G2 Wyvern", "PRR-75", "C01–C40", "5 SBB", "G0–G5"],
    },
}


def classify_family(domain_id: str, subdomain: str, slug: str, title: str, raw_family: str) -> str:
    """Assigne une famille thématique canonique à partir des règles par sous-domaine."""
    rules = FAMILY_RULES.get((domain_id, subdomain))
    if not rules:
        return raw_family or "Thématiques générales"
    hay = normalize_text(f"{slug} {title} {raw_family}")
    for fam_name, keywords in rules:
        if not keywords:
            return fam_name
        if any(kw in hay for kw in keywords):
            return fam_name
    return rules[-1][0]


def make_theme_node_id(slug: str) -> str:
    """Construit un identifiant stable pour un nœud thématique."""
    clean = re.sub(r"[^a-z0-9-]+", "-", slug.lower()).strip("-")
    return f"THM_{clean}"


def build_structure_indexes(struct: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, list[dict[str, Any]]], dict[str, list[str]]]:
    """Indexe toutes les unités de structure-integrale.json par ID, fichier et relation parent->enfants."""
    by_id: dict[str, dict[str, Any]] = {}
    by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    children_map: dict[str, list[str]] = defaultdict(list)

    def walk(unit: dict[str, Any], file_path: str, parent_uid: str | None) -> None:
        entry = {
            "unit_id": unit["unit_id"],
            "tome_id": unit["tome_id"],
            "file": file_path,
            "level": unit["level"],
            "kind": unit["kind"],
            "title": unit["title"],
            "line_start": unit["line_start"],
            "line_end": unit["line_end"],
            "word_count": unit.get("word_count", 0),
            "part_title": unit.get("part_title", ""),
            "identifiers": unit.get("identifiers", []),
            "parent_uid": parent_uid,
        }
        by_id[unit["unit_id"]] = entry
        by_file[file_path].append(entry)
        if parent_uid:
            children_map[parent_uid].append(unit["unit_id"])
        for ch in unit.get("children", []):
            walk(ch, file_path, unit["unit_id"])

    for f in struct.get("files", []):
        fpath = f["file"]
        for root_u in f.get("tree", []):
            walk(root_u, fpath, None)

    return by_id, by_file, children_map


def resolve_struct_unit(
    file_path: str,
    line_start: int,
    line_end: int,
    candidate_uid: str | None,
    struct_by_id: dict[str, dict[str, Any]],
    struct_by_file: dict[str, list[dict[str, Any]]],
    prefer_max_level: int | None = None,
) -> dict[str, Any] | None:
    """Résout une référence de chapitre ou d'occurrence vers son unité exacte dans structure-integrale.json."""
    if candidate_uid and candidate_uid in struct_by_id:
        u = struct_by_id[candidate_uid]
        if u["file"] == file_path:
            return u

    units = struct_by_file.get(file_path, [])
    if not units:
        return None

    pool = [u for u in units if u["kind"] != "toc"] or units
    if prefer_max_level is not None:
        sub = [u for u in pool if u["level"] <= prefer_max_level]
        if sub:
            pool = sub

    # 1. Correspondance exacte de bornes sur les unités hors TOC
    exact_bounds = [u for u in pool if u["line_start"] == line_start and u["line_end"] == line_end]
    if exact_bounds:
        return sorted(exact_bounds, key=lambda x: x["level"])[0]

    # 1b. Correspondance exacte de bornes sur toutes les unités (y compris TOC, ex. T1 Table des matières L35-106)
    exact_all = [u for u in units if u["line_start"] == line_start and u["line_end"] == line_end]
    if prefer_max_level is not None:
        sub_all = [u for u in exact_all if u["level"] <= prefer_max_level]
        if sub_all:
            exact_all = sub_all
    if exact_all:
        return sorted(exact_all, key=lambda x: x["level"])[0]

    # 2. Unité englobant strictement line_start (plus spécifique possible sous prefer_max_level)
    containing = [u for u in pool if u["line_start"] <= line_start <= u["line_end"]]
    if containing:
        return sorted(containing, key=lambda x: (-x["level"], x["line_end"] - x["line_start"]))[0]

    # 3. Correspondance quasi-exacte sur line_start (ex. métadonnées en L1 avant un H1 en L3)
    near_start = [u for u in pool if abs(u["line_start"] - line_start) <= 2]
    if near_start:
        return sorted(near_start, key=lambda x: (abs(x["line_start"] - line_start), x["level"]))[0]

    # 4. Plus fort recouvrement d'intervalle
    def overlap(u: dict[str, Any]) -> int:
        return max(0, min(line_end, u["line_end"]) - max(line_start, u["line_start"]) + 1)

    best = max(pool, key=lambda u: (overlap(u), -abs(u["line_start"] - line_start)))
    return best


def dedup_preserve(items: list[str]) -> list[str]:
    """Déduplique une liste de chaînes tout en préservant l'ordre d'apparition."""
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        s = str(item).strip()
        if s and s not in seen:
            seen.add(s)
            out.append(s)
    return out


def synthesize_graph(repo_root: Path) -> dict[str, Any]:
    """Exécute la synthèse complète et retourne l'objet synthese-transversale.json."""
    donnees_dir = repo_root / "Cartographie" / "donnees"
    shards_dir = donnees_dir / "shards"

    schema = json.loads((donnees_dir / "schema-cartographie.json").read_text(encoding="utf-8"))
    pivots = json.loads((donnees_dir / "pivots-concordance.json").read_text(encoding="utf-8"))
    structure = json.loads((donnees_dir / "structure-integrale.json").read_text(encoding="utf-8"))

    shard_files = sorted(shards_dir.glob("*.json"))
    expected_shards = {
        "tome-1a.json",
        "tome-1b.json",
        "tome-2.json",
        "tome-3a.json",
        "tome-3b.json",
        "tome-4-5.json",
        "tome-6-7-8-readme.json",
    }
    found_names = {p.name for p in shard_files}
    missing_shards = expected_shards - found_names
    if missing_shards:
        raise FileNotFoundError(f"Shards manquants : {sorted(missing_shards)}")

    shards = [json.loads(p.read_text(encoding="utf-8")) for p in shard_files]
    domains_by_id = {d["domain_id"]: d for d in schema["domains"]}
    canon_subdomains = {d["domain_id"]: set(d["subdomains_canonical"]) for d in schema["domains"]}
    valid_rel_types = {rt["type_id"] for rt in schema["relation_types"]}

    struct_by_id, struct_by_file, struct_children = build_structure_indexes(structure)

    # 1. Agrégation des nœuds bruts des 7 shards par canonical_slug rapproché
    raw_by_slug: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    for sh in shards:
        sid = sh["shard_id"]
        for node in sh["thematic_nodes"]:
            slug = SLUG_MERGE_MAP.get(node["canonical_slug"], node["canonical_slug"])
            raw_by_slug[slug].append((sid, node))

    # 2. Consolidation des nœuds thématiques fusionnés
    theme_nodes_by_slug: dict[str, dict[str, Any]] = {}
    for slug, entries in sorted(raw_by_slug.items()):
        dom_counts = Counter(n["domain_id"] for _, n in entries)
        domain_id = dom_counts.most_common(1)[0][0]

        # Normalisation du sous-domaine vers les 36 sous-domaines canoniques
        sub_candidates = []
        for _, n in entries:
            raw_sub = n["subdomain"]
            if raw_sub in canon_subdomains[domain_id]:
                sub_candidates.append(raw_sub)
            elif (domain_id, raw_sub) in SUBDOMAIN_OVERRIDE:
                sub_candidates.append(SUBDOMAIN_OVERRIDE[(domain_id, raw_sub)])
        if sub_candidates:
            subdomain = Counter(sub_candidates).most_common(1)[0][0]
        else:
            subdomain = domains_by_id[domain_id]["subdomains_canonical"][0]

        # Choix du titre (privilégier les synthèses T5 / T7 / T8 / T2 / T6 si plusieurs)
        role_prio = {"synthese": 0, "gouvernance": 1, "norme": 2, "executable": 3, "patron": 4, "prospective": 5, "etat_de_l_art": 6, "fondation": 7}
        best_title = entries[0][1]["title"]
        best_score = 99
        summaries: list[str] = []
        seen_sum_prefix: set[str] = set()
        raw_families: list[str] = []
        all_autonomy: list[str] = []
        all_roles: list[str] = []
        all_horizons: list[str] = []
        all_tags: list[str] = []
        all_ids: list[str] = []
        all_roles_in_tome: list[str] = []
        source_shards: list[str] = []
        occurrences: list[dict[str, Any]] = []
        seen_occ_keys: set[tuple[Any, ...]] = set()
        chapter_unit_ids: list[str] = []

        for sid, n in entries:
            source_shards.append(sid)
            raw_families.append(n.get("family", ""))
            all_autonomy.extend(n.get("autonomy_levels", []))
            all_roles.extend(n.get("roles", []))
            if n.get("horizon"):
                all_horizons.append(normalize_horizon(n["horizon"]))
            all_tags.extend(n.get("tags", []))
            all_ids.extend(n.get("identifiers", []))

            summary_txt = str(n.get("summary", "")).strip()
            if summary_txt and summary_txt[:60].lower() not in seen_sum_prefix:
                seen_sum_prefix.add(summary_txt[:60].lower())
                summaries.append(summary_txt)

            occs = n.get("occurrences", [])
            for raw_occ in occs:
                occ = dict(raw_occ)
                fix_key = (slug, occ["tome_id"], int(occ["line_start"]))
                if fix_key in OCCURRENCE_FIXES:
                    occ.update(OCCURRENCE_FIXES[fix_key])

                occ_ls = int(occ["line_start"])
                occ_le = int(occ["line_end"])
                role_t = occ.get("role_in_tome", "")
                if role_t:
                    all_roles_in_tome.append(role_t)
                prio = role_prio.get(role_t, 8)
                if prio < best_score or (prio == best_score and len(n["title"]) > len(best_title)):
                    best_score = prio
                    best_title = n["title"]

                resolved = resolve_struct_unit(
                    occ["file"],
                    occ_ls,
                    occ_le,
                    occ.get("unit_id"),
                    struct_by_id,
                    struct_by_file,
                )
                if resolved and resolved["unit_id"].endswith("-u0001") and occ_ls < resolved["line_start"] <= occ_le:
                    occ_ls = resolved["line_start"]
                uid = resolved["unit_id"] if resolved else None
                occ_key = (occ["tome_id"], occ["file"], occ_ls, occ_le, uid)
                if occ_key in seen_occ_keys:
                    continue
                seen_occ_keys.add(occ_key)
                occ_copy = {
                    "tome_id": occ["tome_id"],
                    "file": occ["file"],
                    "chapter": occ.get("chapter", resolved["title"] if resolved else ""),
                    "section": occ.get("section", ""),
                    "line_start": occ_ls,
                    "line_end": occ_le,
                    "role_in_tome": role_t,
                }
                if uid:
                    occ_copy["unit_id"] = uid
                    chapter_unit_ids.append(uid)
                occurrences.append(occ_copy)

        # Fallback si aucune occurrence n'a modifié best_score
        if best_score == 99:
            best_title = max((n["title"] for _, n in entries), key=len)

        occurrences.sort(key=lambda o: (TOME_RANK.get(o["tome_id"], 99), o["line_start"]))
        tomes_present = sorted(dedup_preserve([o["tome_id"] for o in occurrences]), key=lambda t: TOME_RANK.get(t, 99))
        autonomy_sorted = sorted(dedup_preserve([a for a in all_autonomy if a in {"L0", "L1", "L2", "L3", "L4"}]))
        horizons_dedup = dedup_preserve([normalize_horizon(h) for h in all_horizons])
        merged_summary = " ".join(summaries[:3])
        if len(merged_summary) > 650:
            merged_summary = merged_summary[:647].rstrip() + "…"

        family = classify_family(domain_id, subdomain, slug, best_title, raw_families[0] if raw_families else "")

        theme_nodes_by_slug[slug] = {
            "node_id": make_theme_node_id(slug),
            "canonical_slug": slug,
            "parent_id": "",  # complété à la construction de l'arbre
            "children_ids": [],
            "depth": 4,
            "node_kind": "theme",
            "domain_id": domain_id,
            "subdomain": subdomain,
            "family": family,
            "title": best_title,
            "summary": merged_summary,
            "autonomy_levels": autonomy_sorted or ["L1", "L2"],
            "roles": dedup_preserve(all_roles) or ["AE", "AS"],
            "horizons": horizons_dedup,
            "horizon": normalize_horizon(horizons_dedup[0]) if horizons_dedup else "2026-2035",
            "tags": dedup_preserve(all_tags),
            "identifiers": dedup_preserve(all_ids),
            "roles_in_tome": dedup_preserve(all_roles_in_tome),
            "tomes_present": tomes_present,
            "source_shards": dedup_preserve(source_shards),
            "occurrences": occurrences,
            "chapter_unit_ids": dedup_preserve(chapter_unit_ids),
            "occurrence_count": len(occurrences),
            "relation_degree": 0,
        }

    # 3. Ajout des nœuds thématiques atomiques spécialisés ancrés sur les occurrences réelles des pivots parents
    specialized_relations: list[dict[str, Any]] = []
    for spec in SPECIALIZED_NODES_SPEC:
        slug = spec["canonical_slug"]
        if slug in theme_nodes_by_slug:
            continue
        parent_pivot = spec["parent_pivot"]
        pivot_node = theme_nodes_by_slug.get(parent_pivot)
        if not pivot_node:
            raise KeyError(f"Pivot parent introuvable pour {slug} : {parent_pivot}")

        tome_filter = set(spec.get("tome_filter", []))
        inherited_occs = [
            dict(o)
            for o in pivot_node["occurrences"]
            if not tome_filter or o["tome_id"] in tome_filter
        ]
        if not inherited_occs:
            inherited_occs = [dict(o) for o in pivot_node["occurrences"][:3]]

        tomes_present = sorted(dedup_preserve([o["tome_id"] for o in inherited_occs]), key=lambda t: TOME_RANK.get(t, 99))
        chapter_uids = dedup_preserve([o["unit_id"] for o in inherited_occs if o.get("unit_id")])
        family = classify_family(spec["domain_id"], spec["subdomain"], slug, spec["title"], "")
        spec_horizon = normalize_horizon(spec["horizon"])

        theme_nodes_by_slug[slug] = {
            "node_id": make_theme_node_id(slug),
            "canonical_slug": slug,
            "parent_id": "",
            "children_ids": [],
            "depth": 4,
            "node_kind": "theme",
            "domain_id": spec["domain_id"],
            "subdomain": spec["subdomain"],
            "family": family,
            "title": spec["title"],
            "summary": spec["summary"],
            "autonomy_levels": spec["autonomy_levels"],
            "roles": spec["roles"],
            "horizons": [spec_horizon],
            "horizon": spec_horizon,
            "tags": spec["tags"],
            "identifiers": spec["identifiers"],
            "roles_in_tome": dedup_preserve([o.get("role_in_tome", "") for o in inherited_occs]),
            "tomes_present": tomes_present,
            "source_shards": pivot_node["source_shards"],
            "occurrences": inherited_occs,
            "chapter_unit_ids": chapter_uids,
            "occurrence_count": len(inherited_occs),
            "relation_degree": 0,
        }

        rel_type, rel_label = spec["rel_to_pivot"]
        specialized_relations.append(
            {
                "source_slug": slug,
                "target_slug": parent_pivot,
                "type": rel_type,
                "label": rel_label,
                "justification": spec["summary"],
                "tomes": tomes_present,
                "source_shards": ["synthetiseur_graphe"],
            }
        )

    # 4. Résolution et couverture à 100 % des chapitres et unités structurelles
    chapters_out: list[dict[str, Any]] = []
    chap_by_uid: dict[str, dict[str, Any]] = {}
    unit_to_slugs: dict[str, list[str]] = defaultdict(list)

    for sh in shards:
        sid = sh["shard_id"]
        for ch in sh["chapters_mapped"]:
            resolved = resolve_struct_unit(
                ch["file"],
                int(ch["line_start"]),
                int(ch["line_end"]),
                ch.get("unit_id"),
                struct_by_id,
                struct_by_file,
                prefer_max_level=2,
            )
            uid = resolved["unit_id"] if resolved else ch["unit_id"]
            mapped_slugs = [
                SLUG_MERGE_MAP.get(s, s)
                for s in ch.get("themes_addressed", [])
                if SLUG_MERGE_MAP.get(s, s) in theme_nodes_by_slug
            ]
            if not mapped_slugs:
                # Fallback par domaine primaire
                pdom = ch.get("primary_domain", "D01")
                mapped_slugs = [s for s, tn in theme_nodes_by_slug.items() if tn["domain_id"] == pdom][:2]

            for s in mapped_slugs:
                unit_to_slugs[uid].append(s)

            if uid not in chap_by_uid:
                chap_by_uid[uid] = {
                    "unit_id": uid,
                    "shard_unit_id": ch["unit_id"],
                    "tome_id": ch["tome_id"],
                    "file": ch["file"],
                    "part_title": ch.get("part_title") or (resolved["part_title"] if resolved else ""),
                    "chapter_title": resolved["title"] if resolved else ch["chapter_title"],
                    "line_start": resolved["line_start"] if resolved else int(ch["line_start"]),
                    "line_end": resolved["line_end"] if resolved else int(ch["line_end"]),
                    "summary": ch["summary"],
                    "primary_domain": ch["primary_domain"],
                    "secondary_domains": dedup_preserve(ch.get("secondary_domains", [])),
                    "themes_addressed": dedup_preserve(mapped_slugs),
                    "key_terms": dedup_preserve(ch.get("key_terms", [])),
                    "normative_refs": dedup_preserve(ch.get("normative_refs", [])),
                    "source_shards": [sid],
                }
            else:
                existing = chap_by_uid[uid]
                existing["themes_addressed"] = dedup_preserve(existing["themes_addressed"] + mapped_slugs)
                existing["secondary_domains"] = dedup_preserve(existing["secondary_domains"] + ch.get("secondary_domains", []))
                existing["key_terms"] = dedup_preserve(existing["key_terms"] + ch.get("key_terms", []))
                existing["normative_refs"] = dedup_preserve(existing["normative_refs"] + ch.get("normative_refs", []))
                existing["source_shards"] = dedup_preserve(existing["source_shards"] + [sid])

    # Compléter toute unité structurelle hors TOC (chapter, annex, liminaire, document, part, section level<=2)
    def collect_descendant_slugs(uid: str, depth_guard: int = 0) -> list[str]:
        if depth_guard > 8:
            return []
        found = list(unit_to_slugs.get(uid, []))
        for child_uid in struct_children.get(uid, []):
            found.extend(collect_descendant_slugs(child_uid, depth_guard + 1))
        return dedup_preserve(found)

    # Remonter d'abord les slugs de chaque occurrence directe aux unités structurelles
    direct_unit_slugs: dict[str, list[str]] = defaultdict(list)
    for slug, tn in theme_nodes_by_slug.items():
        for uid in tn["chapter_unit_ids"]:
            direct_unit_slugs[uid].append(slug)
            unit_to_slugs[uid].append(slug)

    # Associer toutes les unités level<=2 (hors toc) et toutes unités kind in {chapter, annex, liminaire, document, part}
    for uid, u in struct_by_id.items():
        if u["kind"] == "toc":
            continue
        if u["kind"] in ("chapter", "annex", "liminaire", "document", "part") or u["level"] <= 2:
            curated = CURATED_UNIT_METADATA.get(uid)
            if curated:
                valid_curated = [s for s in curated["themes"] if s in theme_nodes_by_slug]
                if curated.get("replace_themes"):
                    merged_curated = dedup_preserve(direct_unit_slugs.get(uid, []) + valid_curated)
                else:
                    desc_slugs = collect_descendant_slugs(uid)
                    merged_curated = dedup_preserve(valid_curated + direct_unit_slugs.get(uid, []) + desc_slugs)[:10]
                unit_to_slugs[uid] = merged_curated
            elif not unit_to_slugs.get(uid):
                # 1. Héritage des enfants
                slugs_found = collect_descendant_slugs(uid)
                # 2. Sinon héritage du parent direct
                if not slugs_found and u.get("parent_uid"):
                    cur_p = u["parent_uid"]
                    while cur_p and not slugs_found:
                        slugs_found = list(unit_to_slugs.get(cur_p, []))
                        cur_p = struct_by_id.get(cur_p, {}).get("parent_uid")
                # 3. Sinon correspondance sur le fichier
                if not slugs_found:
                    slugs_found = [s for s, tn in theme_nodes_by_slug.items() if u["tome_id"] in tn["tomes_present"]][:3]
                if not slugs_found:
                    slugs_found = ["concordance-inter-tomes-div02"]
                unit_to_slugs[uid] = dedup_preserve(slugs_found[:6])

            # Enregistrer dans chapters_out si chapitre/annexe/liminaire/document non encore présent
            if u["kind"] in ("chapter", "annex", "liminaire", "document") and uid not in chap_by_uid:
                linked_s = dedup_preserve(unit_to_slugs[uid])[:10]
                unit_to_slugs[uid] = linked_s
                first_tn = theme_nodes_by_slug[linked_s[0]]
                if curated:
                    summary_text = curated["summary"]
                    key_terms_list = curated.get("key_terms", [])
                else:
                    top_titles = ", ".join(theme_nodes_by_slug[s]["title"] for s in linked_s[:3])
                    summary_text = f"{u['title']} ({u['tome_id']}, L{u['line_start']}-{u['line_end']}) : développe {top_titles}."
                    key_terms_list = []
                chap_by_uid[uid] = {
                    "unit_id": uid,
                    "shard_unit_id": uid,
                    "tome_id": u["tome_id"],
                    "file": u["file"],
                    "part_title": u.get("part_title", ""),
                    "chapter_title": u["title"],
                    "line_start": u["line_start"],
                    "line_end": u["line_end"],
                    "summary": summary_text,
                    "primary_domain": first_tn["domain_id"],
                    "secondary_domains": dedup_preserve([theme_nodes_by_slug[s]["domain_id"] for s in linked_s[1:]]),
                    "themes_addressed": linked_s,
                    "key_terms": key_terms_list,
                    "normative_refs": u.get("identifiers", [])[:12],
                    "source_shards": ["synthetiseur_graphe"],
                }

    # Propager la liaison bidirectionnelle vers chapter_unit_ids de chaque nœud thématique
    for uid, slugs in unit_to_slugs.items():
        for s in dedup_preserve(slugs):
            if s in theme_nodes_by_slug:
                tn = theme_nodes_by_slug[s]
                if uid not in tn["chapter_unit_ids"]:
                    tn["chapter_unit_ids"].append(uid)

    chapters_out = sorted(
        chap_by_uid.values(),
        key=lambda c: (TOME_RANK.get(c["tome_id"], 99), c["line_start"]),
    )

    # 5. Construction de la hiérarchie MindMap complète à 5 niveaux (depth 0..4)
    nodes_out: list[dict[str, Any]] = []
    root_node = {
        "node_id": "NODE_ROOT",
        "canonical_slug": "corpus-agentique-racine",
        "parent_id": None,
        "children_ids": [],
        "depth": 0,
        "node_kind": "root",
        "domain_id": None,
        "subdomain": None,
        "family": None,
        "title": "Corpus Agentique (8 Tomes · 4 542 pages)",
        "summary": "Cartographie intégrale de l'interopérabilité, de l'orchestration déterministe, de la confiance cryptographique, de la conformité prudentielle et de l'homologation vérifiable (Tomes 1 à 8 + index).",
        "autonomy_levels": ["L0", "L1", "L2", "L3", "L4"],
        "roles": ["AE", "AS", "RSSI", "Juridique", "SRE", "Direction"],
        "horizons": ["2023-2035"],
        "horizon": "2023-2035",
        "tags": ["corpus-integral", "80/20", "DAPP", "Wyvern"],
        "identifiers": ["CRE-IA-2026-01", "PRR-75", "C01–C40", "DIV-02"],
        "roles_in_tome": ["fondation", "norme", "etat_de_l_art", "prospective", "synthese", "patron", "gouvernance", "executable"],
        "tomes_present": list(TOME_ORDER),
        "source_shards": ["synthetiseur_graphe"],
        "occurrences": [],
        "chapter_unit_ids": [],
        "occurrence_count": 0,
        "relation_degree": 0,
    }
    nodes_out.append(root_node)

    themes_by_dom_sub_fam: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for tn in theme_nodes_by_slug.values():
        themes_by_dom_sub_fam[(tn["domain_id"], tn["subdomain"], tn["family"])].append(tn)

    for dom in sorted(schema["domains"], key=lambda d: d["order"]):
        did = dom["domain_id"]
        dom_nid = f"DOM_{did}"
        root_node["children_ids"].append(dom_nid)
        dom_node = {
            "node_id": dom_nid,
            "canonical_slug": f"domaine-{did.lower()}",
            "parent_id": "NODE_ROOT",
            "children_ids": [],
            "depth": 1,
            "node_kind": "domain",
            "domain_id": did,
            "subdomain": None,
            "family": None,
            "title": dom["title"],
            "summary": dom["summary"],
            "autonomy_levels": [],
            "roles": [],
            "horizons": [],
            "horizon": "2026-2035",
            "tags": dom.get("pivot_slugs", [])[:6],
            "identifiers": dom.get("key_identifiers", []),
            "roles_in_tome": [],
            "tomes_present": [],
            "source_shards": ["schema-cartographie"],
            "occurrences": [],
            "chapter_unit_ids": [],
            "occurrence_count": 0,
            "relation_degree": 0,
        }
        nodes_out.append(dom_node)

        for sub_idx, sub_title in enumerate(dom["subdomains_canonical"], 1):
            sub_nid = f"SUB_{did}_{sub_idx:02d}"
            dom_node["children_ids"].append(sub_nid)
            sub_node = {
                "node_id": sub_nid,
                "canonical_slug": f"sous-domaine-{did.lower()}-{sub_idx:02d}",
                "parent_id": dom_nid,
                "children_ids": [],
                "depth": 2,
                "node_kind": "subdomain",
                "domain_id": did,
                "subdomain": sub_title,
                "family": None,
                "title": sub_title,
                "summary": f"Sous-domaine de {did} : {sub_title}.",
                "autonomy_levels": [],
                "roles": [],
                "horizons": [],
                "horizon": "2026-2035",
                "tags": [],
                "identifiers": [],
                "roles_in_tome": [],
                "tomes_present": [],
                "source_shards": ["schema-cartographie"],
                "occurrences": [],
                "chapter_unit_ids": [],
                "occurrence_count": 0,
                "relation_degree": 0,
            }
            nodes_out.append(sub_node)

            # Familles dans ce sous-domaine (ordre canonique de FAMILY_RULES)
            rules_order = [r[0] for r in FAMILY_RULES.get((did, sub_title), [])]
            present_fams = sorted(
                {f for (d0, s0, f) in themes_by_dom_sub_fam if d0 == did and s0 == sub_title},
                key=lambda fname: (rules_order.index(fname) if fname in rules_order else 999, fname),
            )
            for fam_idx, fam_title in enumerate(present_fams, 1):
                fam_nid = f"FAM_{did}_{sub_idx:02d}_{fam_idx:02d}"
                sub_node["children_ids"].append(fam_nid)
                fam_themes = sorted(
                    themes_by_dom_sub_fam[(did, sub_title, fam_title)],
                    key=lambda x: (-x["occurrence_count"], x["title"]),
                )
                fam_node = {
                    "node_id": fam_nid,
                    "canonical_slug": f"famille-{did.lower()}-{sub_idx:02d}-{fam_idx:02d}",
                    "parent_id": sub_nid,
                    "children_ids": [t["node_id"] for t in fam_themes],
                    "depth": 3,
                    "node_kind": "family",
                    "domain_id": did,
                    "subdomain": sub_title,
                    "family": fam_title,
                    "title": fam_title,
                    "summary": f"Famille thématique ({len(fam_themes)} thèmes) dans « {sub_title} ».",
                    "autonomy_levels": sorted(dedup_preserve([a for t in fam_themes for a in t["autonomy_levels"]])),
                    "roles": dedup_preserve([r for t in fam_themes for r in t["roles"]]),
                    "horizons": dedup_preserve([normalize_horizon(h) for t in fam_themes for h in t["horizons"]]),
                    "horizon": normalize_horizon(fam_themes[0]["horizon"]) if fam_themes else "2026-2035",
                    "tags": dedup_preserve([tg for t in fam_themes for tg in t["tags"]])[:12],
                    "identifiers": dedup_preserve([idn for t in fam_themes for idn in t["identifiers"]])[:16],
                    "roles_in_tome": dedup_preserve([rt for t in fam_themes for rt in t["roles_in_tome"]]),
                    "tomes_present": sorted(dedup_preserve([tm for t in fam_themes for tm in t["tomes_present"]]), key=lambda x: TOME_RANK.get(x, 99)),
                    "source_shards": dedup_preserve([sd for t in fam_themes for sd in t["source_shards"]]),
                    "occurrences": [],
                    "chapter_unit_ids": [],
                    "occurrence_count": sum(t["occurrence_count"] for t in fam_themes),
                    "relation_degree": 0,
                }
                nodes_out.append(fam_node)

                for t in fam_themes:
                    t["parent_id"] = fam_nid
                    nodes_out.append(t)

            # Propagation ascendante vers sous-domaine
            fam_children = [n for n in nodes_out if n["parent_id"] == sub_nid]
            sub_node["autonomy_levels"] = sorted(dedup_preserve([a for c in fam_children for a in c["autonomy_levels"]]))
            sub_node["roles"] = dedup_preserve([r for c in fam_children for r in c["roles"]])
            sub_node["horizons"] = dedup_preserve([normalize_horizon(h) for c in fam_children for h in c["horizons"]])
            sub_node["horizon"] = sub_node["horizons"][0] if sub_node["horizons"] else "2026-2035"
            sub_node["roles_in_tome"] = dedup_preserve([rt for c in fam_children for rt in c["roles_in_tome"]])
            sub_node["tomes_present"] = sorted(dedup_preserve([tm for c in fam_children for tm in c["tomes_present"]]), key=lambda x: TOME_RANK.get(x, 99))
            sub_node["occurrence_count"] = sum(c["occurrence_count"] for c in fam_children)

        # Propagation ascendante vers domaine
        sub_children = [n for n in nodes_out if n["parent_id"] == dom_nid]
        dom_node["autonomy_levels"] = sorted(dedup_preserve([a for c in sub_children for a in c["autonomy_levels"]]))
        dom_node["roles"] = dedup_preserve([r for c in sub_children for r in c["roles"]])
        dom_node["horizons"] = dedup_preserve([normalize_horizon(h) for c in sub_children for h in c["horizons"]])
        dom_node["horizon"] = dom_node["horizons"][0] if dom_node["horizons"] else "2026-2035"
        dom_node["roles_in_tome"] = dedup_preserve([rt for c in sub_children for rt in c["roles_in_tome"]])
        dom_node["tomes_present"] = sorted(dedup_preserve([tm for c in sub_children for tm in c["tomes_present"]]), key=lambda x: TOME_RANK.get(x, 99))
        dom_node["occurrence_count"] = sum(c["occurrence_count"] for c in sub_children)

    root_node["occurrence_count"] = sum(n["occurrence_count"] for n in nodes_out if n["depth"] == 1)

    # 6. Fusion et déduplication des interrelations
    raw_rels: list[tuple[str, dict[str, Any]]] = []
    for sh in shards:
        sid = sh["shard_id"]
        for r in sh["relations"]:
            raw_rels.append((sid, r))
    for r in specialized_relations:
        raw_rels.append(("synthetiseur_graphe", r))

    grouped_rels: dict[tuple[str, str, str], list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    for sid, r in raw_rels:
        s_slug = SLUG_MERGE_MAP.get(r["source_slug"], r["source_slug"])
        t_slug = SLUG_MERGE_MAP.get(r["target_slug"], r["target_slug"])
        rtype = r["type"]
        if s_slug == t_slug:
            continue
        if s_slug not in theme_nodes_by_slug or t_slug not in theme_nodes_by_slug:
            continue
        if rtype not in valid_rel_types:
            continue
        grouped_rels[(s_slug, t_slug, rtype)].append((sid, r))

    relations_out: list[dict[str, Any]] = []
    deg_counter: Counter[str] = Counter()
    for rel_idx, ((s_slug, t_slug, rtype), items) in enumerate(sorted(grouped_rels.items()), 1):
        src_node = theme_nodes_by_slug[s_slug]
        tgt_node = theme_nodes_by_slug[t_slug]
        labels = dedup_preserve([it[1]["label"] for it in items])
        justs = dedup_preserve([it[1]["justification"] for it in items])
        tomes = sorted(
            dedup_preserve([tm for _, it in items for tm in it.get("tomes", [])]),
            key=lambda x: TOME_RANK.get(x, 99),
        )
        if not tomes:
            tomes = sorted(
                dedup_preserve(src_node["tomes_present"] + tgt_node["tomes_present"]),
                key=lambda x: TOME_RANK.get(x, 99),
            )
        combined_just = " | ".join(justs[:2])
        if len(combined_just) > 520:
            combined_just = combined_just[:517].rstrip() + "…"
        if not combined_just.strip():
            combined_just = f"Relation {rtype} attestée entre {src_node['title']} et {tgt_node['title']}."

        relations_out.append(
            {
                "relation_id": f"REL_{rel_idx:04d}",
                "source": src_node["node_id"],
                "target": tgt_node["node_id"],
                "source_slug": s_slug,
                "target_slug": t_slug,
                "type": rtype,
                "label": labels[0],
                "justification": combined_just,
                "tomes": tomes,
                "source_shards": dedup_preserve([it[0] for it in items]),
                "weight": len(items),
            }
        )
        deg_counter[src_node["node_id"]] += 1
        deg_counter[tgt_node["node_id"]] += 1

    for n in nodes_out:
        if n["node_kind"] == "theme":
            n["relation_degree"] = deg_counter.get(n["node_id"], 0)

    # 7. Calcul de la matrice de concordance (Domaines & Sous-domaines × 9 fichiers MD)
    concordance_matrix: list[dict[str, Any]] = []
    files_meta = {f["tome_id"]: f["file"] for f in schema["corpus_scope"]["files"]}
    themes_list = [n for n in nodes_out if n["node_kind"] == "theme"]

    for dom in schema["domains"]:
        did = dom["domain_id"]
        dom_themes = [t for t in themes_list if t["domain_id"] == did]
        for tid in TOME_ORDER:
            matched_themes = [t for t in dom_themes if tid in t["tomes_present"]]
            occ_count = sum(1 for t in dom_themes for o in t["occurrences"] if o["tome_id"] == tid)
            chap_ids = {o["unit_id"] for t in dom_themes for o in t["occurrences"] if o["tome_id"] == tid and o.get("unit_id")}
            roles_t = dedup_preserve([o["role_in_tome"] for t in dom_themes for o in t["occurrences"] if o["tome_id"] == tid and o.get("role_in_tome")])
            ids_t = dedup_preserve([i for t in matched_themes for i in t["identifiers"]])[:10]
            concordance_matrix.append(
                {
                    "granularity": "domain",
                    "domain_id": did,
                    "subdomain": None,
                    "tome_id": tid,
                    "file": files_meta[tid],
                    "node_count": len(matched_themes),
                    "occurrence_count": occ_count,
                    "chapter_count": len(chap_ids),
                    "roles_in_tome": roles_t,
                    "top_node_ids": [t["node_id"] for t in sorted(matched_themes, key=lambda x: -x["occurrence_count"])[:5]],
                    "sample_identifiers": ids_t,
                }
            )
        for sub_title in dom["subdomains_canonical"]:
            sub_themes = [t for t in dom_themes if t["subdomain"] == sub_title]
            for tid in TOME_ORDER:
                matched_sub = [t for t in sub_themes if tid in t["tomes_present"]]
                occ_count = sum(1 for t in sub_themes for o in t["occurrences"] if o["tome_id"] == tid)
                chap_ids = {o["unit_id"] for t in sub_themes for o in t["occurrences"] if o["tome_id"] == tid and o.get("unit_id")}
                roles_t = dedup_preserve([o["role_in_tome"] for t in sub_themes for o in t["occurrences"] if o["tome_id"] == tid and o.get("role_in_tome")])
                concordance_matrix.append(
                    {
                        "granularity": "subdomain",
                        "domain_id": did,
                        "subdomain": sub_title,
                        "tome_id": tid,
                        "file": files_meta[tid],
                        "node_count": len(matched_sub),
                        "occurrence_count": occ_count,
                        "chapter_count": len(chap_ids),
                        "roles_in_tome": roles_t,
                        "top_node_ids": [t["node_id"] for t in sorted(matched_sub, key=lambda x: -x["occurrence_count"])[:4]],
                        "sample_identifiers": [],
                    }
                )

    # 8. Validation interne stricte avant écriture
    node_ids_set = {n["node_id"] for n in nodes_out}
    for rel in relations_out:
        assert rel["source"] in node_ids_set, f"Source manquante: {rel}"
        assert rel["target"] in node_ids_set, f"Cible manquante: {rel}"
        assert rel["source"] != rel["target"], f"Auto-boucle: {rel}"
        assert rel["type"] in valid_rel_types, f"Type invalide: {rel}"
        assert rel["justification"].strip(), f"Justification vide: {rel}"

    # Vérifier couverture 12 domaines, 9 fichiers, 0 chapitre/unité orpheline
    themes_by_dom = Counter(t["domain_id"] for t in themes_list)
    assert len(themes_by_dom) == 12, f"Domaines couverts != 12 : {themes_by_dom}"
    tomes_covered = {tm for t in themes_list for tm in t["tomes_present"]}
    assert tomes_covered == set(TOME_ORDER), f"Fichiers manquants : {set(TOME_ORDER) - tomes_covered}"

    # Vérifier zéro unité structurelle orpheline (hors TOC) parmi chapter/annex/liminaire/document/part
    all_linked_uids = {uid for t in themes_list for uid in t["chapter_unit_ids"]}
    orphan_struct = [
        (u["tome_id"], u["unit_id"], u["kind"], u["title"])
        for uid, u in struct_by_id.items()
        if u["kind"] != "toc"
        and (u["kind"] in ("chapter", "annex", "liminaire", "document", "part") or u["level"] <= 2)
        and uid not in all_linked_uids
    ]
    assert not orphan_struct, f"Unités structurelles orphelines détectées : {orphan_struct[:10]}"

    for ch in chapters_out:
        assert ch["unit_id"] in struct_by_id, f"Chapitre inconnu de structure-integrale: {ch['unit_id']}"
        assert len(ch["themes_addressed"]) >= 1, f"Chapitre sans thème: {ch['unit_id']}"
        assert not ch["summary"].startswith("Unité structurelle ("), f"Résumé générique interdit sur {ch['unit_id']}"
        for s in ch["themes_addressed"]:
            assert s in theme_nodes_by_slug, f"Thème inconnu {s} sur chapitre {ch['unit_id']}"
            assert ch["unit_id"] in theme_nodes_by_slug[s]["chapter_unit_ids"], (
                f"Lien bidirectionnel manquant : {ch['unit_id']} absent de {s}.chapter_unit_ids"
            )

    # Vérifier normalisation des horizons (aucun tiret demi-cadratin/cadratin), 0 occurrence hors bornes et exactitude des correctifs
    for n in nodes_out:
        hz_values = [n.get("horizon", "")] + list(n.get("horizons", []))
        assert all("–" not in h and "—" not in h for h in hz_values), f"Tiret non normalisé dans horizon de {n['node_id']}: {hz_values}"
        if n["node_kind"] == "theme":
            for occ in n["occurrences"]:
                uid = occ.get("unit_id")
                assert uid in struct_by_id, f"Occurrence sans unit_id valide sur {n['canonical_slug']}: {occ}"
                u = struct_by_id[uid]
                assert u["line_start"] <= occ["line_start"] <= u["line_end"], (
                    f"Occurrence hors bornes sur {n['canonical_slug']} ({uid} L{u['line_start']}-{u['line_end']}): {occ}"
                )
                assert occ["line_start"] <= occ["line_end"], f"Plage inversée: {occ}"

    assert "agntcy-slim" not in chap_by_uid["t7-u0005"]["themes_addressed"]
    assert "t7-u0005" not in theme_nodes_by_slug["agntcy-slim"]["chapter_unit_ids"]
    assert "agntcy-slim" in chap_by_uid["t7-u0002"]["themes_addressed"]
    assert "did-vc-passeport-agent" not in chap_by_uid["t7-u0006"]["themes_addressed"]
    assert "t7-u0006" not in theme_nodes_by_slug["did-vc-passeport-agent"]["chapter_unit_ids"]
    assert "did-vc-passeport-agent" in chap_by_uid["t7-u0003"]["themes_addressed"]
    assert "anti-verrouillage-standards" not in chap_by_uid["t8-u0007"]["themes_addressed"]
    assert "t8-u0007" not in theme_nodes_by_slug["anti-verrouillage-standards"]["chapter_unit_ids"]
    assert "anti-verrouillage-standards" in chap_by_uid["t8-u0006"]["themes_addressed"]

    rel_by_type = dict(sorted(Counter(r["type"] for r in relations_out).items()))
    nodes_by_kind = dict(sorted(Counter(n["node_kind"] for n in nodes_out).items()))

    return {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lang": "fr-CA",
        "generator": "Cartographie/outils/synthetiser_graphe.py",
        "totals": {
            "total_nodes": len(nodes_out),
            "theme_nodes": len(themes_list),
            "nodes_by_kind": nodes_by_kind,
            "relations": len(relations_out),
            "relations_by_type": rel_by_type,
            "chapters_mapped": len(chapters_out),
            "structural_units_linked": len(all_linked_uids),
            "domains_covered": len(themes_by_dom),
            "files_covered": len(tomes_covered),
            "shards_merged": len(shards),
        },
        "hierarchy_levels": schema["thematic_hierarchy_levels"],
        "nodes": nodes_out,
        "relations": relations_out,
        "chapters": chapters_out,
        "concordance_matrix": concordance_matrix,
        "pivots_summary": {
            "collection_metrics": pivots["collection_metrics"],
            "cinq_discordances_count": len(pivots["discordances_resolues"]["cinq_discordances_tome_8"]["entries"]),
            "div_02_statut": pivots["discordances_resolues"]["div_02_tome_5"]["statut"],
            "exig_total": pivots["matrices"]["exig_cre_ia_2026_v1_2"]["total"],
            "cap_total": len(pivots["matrices"]["cap_52"]),
            "pex_total": len(pivots["matrices"]["pex_24"]),
            "prr_total": pivots["matrices"]["prr_75"]["total"],
            "prr_blocking": pivots["matrices"]["prr_75"]["blocking_count"],
        },
        "validation_report": {
            "broken_edges": 0,
            "self_loops": 0,
            "orphan_chapters": 0,
            "orphan_structural_units_level12": 0,
            "domains_covered": 12,
            "files_covered": 9,
            "passed": True,
        },
    }


def main() -> int:
    """Point d'entrée CLI pour la synthèse du graphe transversal."""
    parser = argparse.ArgumentParser(description="Synthétise le graphe thématique transversal du Corpus.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Racine du dépôt Agentique.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    result = synthesize_graph(repo_root)
    out_path = repo_root / "Cartographie" / "donnees" / "synthese-transversale.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    t = result["totals"]
    print(
        f"Synthèse réussie : {t['theme_nodes']} thèmes ({t['total_nodes']} nœuds sur 5 niveaux), "
        f"{t['relations']} interrelations, {t['chapters_mapped']} chapitres, "
        f"{t['structural_units_linked']} unités structurelles liées, "
        f"{t['domains_covered']}/12 domaines, {t['files_covered']}/9 fichiers -> {out_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
