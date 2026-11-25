# Annexe D — Homologation exécutable G0–G5, matrice EXIG / CAP / PRR-75 / C01–C40 / 5 SBB, licences et statut non-avis

Cette annexe publie le bilan exécutable des barrières `G0`–`G5`, la matrice de traçabilité `matrice-exig-prr-c40.json` (**95 liaisons** reliant `305 EXIG-*`, `52 CAP`, `24 PEX`, `PRR-75` dont `24` bloquantes, `C01–C40` et `5 SBB`), les extraits scellés `CA-G0-SYNC`, le catalogue des **57 spécifications ouvertes `L+`** et la clause `non-avis` (`AO-05`).

## 1. Bilan exécutable de la barrière logicielle `G0`

| Contrôle G0 | Mesure vérifiée | Statut |
|---|---|---|
| Verdict `execute_g0.py` | Code `0` (`PASS`) | Conforme |
| Suite `pytest` | `83` passés, `0` échecs, `0` ignorés | Conforme |
| Politiques `OPA / Rego` | Couverture `100,0 %`, `45` tests | Conforme |
| Audit `SPDX MIT` | `50` fichiers, `18` paquets | Conforme |
| Schémas JSON & Lockfile | `21` schémas, empreintes épinglées `True` | Conforme |
| Quatre vecteurs tiers | `4` suites, `14` extraits `CA-G0-SYNC` | Conforme |

Répartition `pytest` par module: `tests/test_authz_pqc_audit.py` (23), `tests/test_evalops_prr.py` (10), `tests/test_harness_proto.py` (14), `tests/test_policy_saga.py` (18), `tests/test_saga_10_faults.py` (11), `tests/test_third_party_vectors.py` (7).

- **`a2a_tck`**: statut `PASS`, `5` vecteurs vérifiés.
- **`nist_acvp`**: statut `PASS`, `12` vecteurs vérifiés.
- **`owasp_src055`**: statut `PASS`, `13` vecteurs vérifiés.
- **`rfc8785`**: statut `PASS`, `20` vecteurs vérifiés.

## 2. Clause `non-avis` et régime dual de licences (`CC-BY-4.0` / `MIT`)

Le présent traité et ses cent quinze schémas sont diffusés sous licence **`CC-BY-4.0`**, tandis que l'outillage d'homologation (`Compendium/ouvrage/outils/`) et la trousse compagnon (`Tome 8`) relèvent de la licence **`MIT`**. Conformément au statut `non-avis` arrêté au 2 décembre 2026, l'ouvrage constitue une référence technique pédagogique et ne tient lieu ni d'avis juridique, ni de certification réglementaire, ni d'homologation sur un système d'enregistrement en exploitation réelle.

## 3. Inventaire des 14 extraits scellés `CA-G0-SYNC` (`CA-20`)

- **`G0-EX-CH01-01`** (`ch04`): `schemas/harness_extraction.schema.json`, lignes `1-24`, `SHA-256` `6b4428a1f8a6`.
- **`G0-EX-CH01-02`** (`ch04`): `harness_proto/pipeline.py`, lignes `204-232`, `SHA-256` `75110799d751`.
- **`G0-EX-CH01-03`** (`ch07`): `harness_proto/mcp_pinning.py`, lignes `227-260`, `SHA-256` `350e1959e6f0`.
- **`G0-EX-CH01-04`** (`ch08`): `harness_proto/a2a_card.py`, lignes `157-182`, `SHA-256` `1a58d5eabab4`.
- **`G0-EX-CH02-01`** (`ch17`): `authz_pqc_audit/obo_dpop.py`, lignes `85-114`, `SHA-256` `d3c2d0ce031a`.
- **`G0-EX-CH02-02`** (`ch17`): `authz_pqc_audit/ciba_approval.py`, lignes `106-117`, `SHA-256` `423ebd61ce49`.
- **`G0-EX-CH02-03`** (`ch18`): `authz_pqc_audit/pqc_http431.py`, lignes `149-177`, `SHA-256` `c5c72e27a393`.
- **`G0-EX-CH02-04`** (`ch22`): `authz_pqc_audit/otel_pii_mapper.py`, lignes `235-265`, `SHA-256` `60bd160c1a50`.

- **`G0-EX-CH03-01`** (`ch20`): `policies_opa/rule_of_two.rego`, lignes `3-26`, `SHA-256` `c0adc5553c04`.
- **`G0-EX-CH03-02`** (`ch20`): `policies_opa/camel_taint.rego`, lignes `3-25`, `SHA-256` `bd873cf677b3`.
- **`G0-EX-CH03-03`** (`ch15`): `policy_saga/saga_orchestrator.py`, lignes `107-140`, `SHA-256` `a2aac944f6ae`.
- **`G0-EX-CH04-01`** (`ch35`): `evalops_prr/wilson_bounds.py`, lignes `43-70`, `SHA-256` `3e685cbef8de`.
- **`G0-EX-CH04-02`** (`ch23`): `evalops_prr/metamorphic.py`, lignes `38-63`, `SHA-256` `31ad0df04f19`.
- **`G0-EX-CH04-03`** (`ch34`): `schemas/adr_2027_b001.schema.json`, lignes `1-32`, `SHA-256` `4f0a41e72808`.

## 4. Ventilation du référentiel `CRE-IA-2026-01 v1.2` (`305` exigences)

Répartition par force normative: `DOIT` (255), `NE_DOIT_PAS` (34), `DEVRAIT` (16). Composition: 287 socle v1.1 + 12 EXIG-AMF (41 attentes Note AMF IA.pdf CRE-IA-2026-01-QC) + 6 ajouts PQC/ACVM/RTR/EN 18286.

Familles d'exigences: `EXIG-ARC` (25 — Architecture de référence, Chapitre 5), `EXIG-INT` (23 — Interopérabilité, contrats et catalogue d'entreprise, Sections 6.1–6.4, 6.8–6.9), `EXIG-MCP` (22 — Model Context Protocol, Section 6.5), `EXIG-A2A` (15 — Protocole Agent2Agent, Section 6.6), `EXIG-EVT` (10 — Interopérabilité événementielle, Section 6.7), `EXIG-ORC` (30 — Orchestration, Chapitre 7), `EXIG-AUT` (23 — Autonomie et supervision humaine, Chapitre 8), `EXIG-IAM` (21 — Confiance zéro, identité, délégation et passerelle d'agents, Sections 9.1–9.4), `EXIG-SEC` (28 — Menaces propres aux agents et défenses, Sections 9.5–9.9), `EXIG-OBS` (13 — Traçage et journal d'audit, Sections 10.1–10.3), `EXIG-EVA` (6 — Évaluation continue, Section 10.4), `EXIG-FIN` (10 — Économie de l'inférence et maîtrise des coûts, Sections 10.5–10.6), `EXIG-GOV` (20 — Gouvernance et cycle de vie, Chapitre 11), `EXIG-CON` (30 — Risques, conformité et réglementation, Chapitre 12 (sections 12.1–12.10)), `EXIG-AMF` (12 — Profil québécois AMF IA et gestion du risque de modèle, Section 12.10), `EXIG-APP` (17 — Approvisionnement et clauses contractuelles, Chapitre 13).

Dix interdictions absolues sans dérogation (`EXIG-GOV-17`): 1. Autonomie non bornée de niveau NX interdite en tout temps (EXIG-AUT-03) ; 2. Exécution d'une action P3 sans approbation humaine hors bande liée (EXIG-AUT-09, EXIG-AUT-12, EXIG-AUT-13) ; 3. Usurpation par un agent de l'identité de son mandant humain (EXIG-IAM-08, EXIG-IAM-09) ; 4. Relais direct d'un jeton entrant vers un serveur ou pair aval (EXIG-IAM-12, EXIG-MCP-11) ; 5. Exploitation sans fiche complète au registre ou parrain nommé (EXIG-GOV-01, 02, 04, 05, 07..11, 13..15) ; 6. Dépassement du plafond d'autonomie fixé par la classe de risque (EXIG-AUT-01, EXIG-AUT-02, EXIG-CON-02) ; 7. Autorisation au-delà de N2 d'un agent atteignant les seuils de la règle d'or (EXIG-AUT-07) ; 8. Exposition à la triade létale sans retrait déterministe des outils sortants (EXIG-SEC-06) ; 9. Exploitation d'un agent sans journal d'audit distinct, chaîné et ancré (EXIG-OBS-11) ; 10. Manquement à une obligation légale ou réglementaire applicable dont Loi 25 art. 12.1 (EXIG-AUT-22..23, EXIG-CON-04..22).

## 5. Grille `PRR-75`, trois blueprints `C01–C40` et cinq blocs `SBB`

La grille `PRR-75` rassemble **75 points de contrôle**, dont **24 bloquants**, **26 conditionnels** et **25 élevés ou moyens**.

### Trois blueprints `C01–C40`

- **`bp1_assistant_interne`**: §14.1 (traitement transactionnel réglementé SoR).
- **`bp2_rag_entreprise_acl`**: §14.3 (enclave souveraine, AI Gateway, RAG ACL, microVM).
- **`bp3_orchestration_multi_agents_b2b`**: §14.2 (maillage inter-départemental & B2B A2A/AGNTCY/Event Mesh).

### Cinq blocs logiciels (`SBB`)

- **`SBB-SECRETS-VAULT`** (`Plan A`, slot `secrets_vault`) → module `authz_pqc_audit/obo_dpop.py`.
- **`SBB-GUARDRAILS-ENGINE`** (`Plan A`, slot `guardrails_engine`) → module `policies_opa/opa_runner.py + rule_of_two.rego`.
- **`SBB-SIGNED-HUMAN-APPROVAL`** (`Plan A`, slot `signed_human_approval_service`) → module `authz_pqc_audit/ciba_approval.py`.
- **`SBB-IMMUTABLE-AUDIT-LEDGER`** (`Plan B`, slot `immutable_audit_ledger`) → module `authz_pqc_audit/audit_scitt_focus.py`.
- **`SBB-FINOPS-BUDGET-QUOTA`** (`Plan B`, slot `finops_budget_quota_controller`) → module `policy_saga/decimal_money.py + audit_scitt_focus.py`.

### Vingt-quatre portes bloquantes `PRR`

- **`S-01`** (grille `S`): Identité NHI unique inscrite à l’annuaire d’entreprise (aucune clé API partagée).
- **`S-03`** (grille `S`): Délégation OAuth 2.1 `On-Behalf-Of` (RFC 8693) préservant `sub` et la chaîne `act`.
- **`S-06`** (grille `S`): Séparation entre l’agent d’interface exposé et l’agent détenteur d’outils d’écriture.
- **`S-08`** (grille `S`): Marquage structurel des données externes non fiables contre l’injection indirecte (ASI01).
- **`S-09`** (grille `S`): Évaluation déterministe hors LLM (Cedar ou OPA) devant chaque appel d’outil mutatif.
- **`S-11`** (grille `S`): Exécution de tout code ou script dynamique en bac à sable isolé (OpenSandbox/microVM).
- **`S-14`** (grille `S`): Coupe-circuit centralisé du SOC, révoquant jetons et sessions en < 10 secondes.
- **`S-15`** (grille `S`): Validation de la séparation des tâches sur les flux financiers/sensibles.

- **`R-01`** (grille `R`): Inviolabilité des systèmes d’enregistrement (passage exclusif par des API/BAPI métiers validées).
- **`R-03`** (grille `R`): Clé d’idempotence déterministe transmise et honorée sur chaque outil à effet de bord.
- **`R-06`** (grille `R`): Définition explicite d’une action de compensation Saga ou d’un bail TTL par mutation.
- **`R-07`** (grille `R`): Tampon de pré-engagement (fenêtre de grâce ou approbation) devant toute action irréversible.
- **`R-14`** (grille `R`): Cloisonnement multilocataire du contexte et des caches d’inférence.
- **`O-02`** (grille `O`): Caviardage ou masquage automatique des renseignements personnels (PII) avant export OTel.
- **`O-09`** (grille `O`): Enveloppe budgétaire maximale en devises (`maxTotalCostCad`) active par transaction/saga.
- **`G-01`** (grille `G`): Propriétaire métier nominatif désigné.

- **`G-03`** (grille `G`): Qualification réglementaire de l’empreinte de déploiement.
- **`G-05`** (grille `G`): Évaluation des facteurs relatifs à la vie privée (ÉFVP — Loi 25 / RGPD).
- **`G-06`** (grille `G`): Mécanisme d’information, d’explication et de révision (Loi 25 art. 12.1).
- **`G-07`** (grille `G`): Divulgation de l’interaction avec une IA (EU AI Act art. 50, 2 août 2026).
- **`G-10`** (grille `G`): Droit à l’effacement et purge sélective vérifiable dans la mémoire à long terme.
- **`G-15`** (grille `G`): Archivage immuable et horodaté (WORM) des décisions critiques.
- **`F-04`** (grille `F`): Résidence juridictionnelle vérifiée des couches d’état (sections 46.1 et 46.9).
- **`F-14`** (grille `F`): Confinement du SRE autonome (lecture seule assainie, aucun shell libre, budget Cedar R1/R2 + H0).

## 6. Cinquante-deux capacités (`CAP-001`–`CAP-052`) et vingt-quatre propositions sectorielles (`PEX-001`–`PEX-024`)

Les **52 capacités** se répartissent par statut (`conditionnelle`: 10, `invariante`: 42) et par palier (`P1`: 30, `P2`: 18, `P3`: 4). Les **24 extensions `PEX`** couvrent les profils sectoriels: Banque (5), Patrimoine (5), Assurance personnes (5), Assurance dommages (5), Groupe diversifié (4).

- **`PEX-001`** (Banque, `M-14`): Rejet de l’accès par authentifiant client et vérification d’accréditation auprès de la Banque du Canada.
- **`PEX-002`** (Banque, `M-14`): Liaison cryptographique du consentement exprès par produit et conservation probatoire à double horizon (cinq et sept ans).
- **`PEX-003`** (Banque, `M-14`): Garde-fou déterministe d’exclusion du commerce de l’assurance non autorisée sur canal bancaire.
- **`PEX-004`** (Banque, `M-14`): Tampon d’irréversibilité et approbation liée aux paramètres avant émission d’un virement temps réel ISO 20022.
- **`PEX-005`** (Banque, `M-14`): Résidence canadienne des livres bancaires, alertes électroniques de solde et loyauté terminologique du traitement des plaintes.
- **`PEX-011`** (Patrimoine, `M-15`): Dossier explicable de convenance centrée sur le client et rattachement non délégable à une personne physique inscrite.
- **`PEX-012`** (Patrimoine, `M-15`): Double barrière des comptes d’exécution d’ordres sans conseils: non-recommandation et blocage des systèmes automatisés d’ordres des clients.
- **`PEX-013`** (Patrimoine, `M-15`): Approbation préalable d’un superviseur désigné, prévention des allégations trompeuses sur l’IA et archivage septennal durable.

- **`PEX-014`** (Patrimoine, `M-15`): Neutralité algorithmique face aux conflits d’intérêts rémunératoires et exclusion des rétrofacturations interdites.
- **`PEX-015`** (Patrimoine, `M-15`): Intégrité décimale et traçabilité quotidienne des ratios et frais de fonds entre gestionnaires et courtiers.
- **`PEX-021`** (Assurance personnes, `M-16`): Filtrage déterministe et caviardage préalable des résultats de tests génétiques.
- **`PEX-022`** (Assurance personnes, `M-16`): Attestation de consentement exprès distinct lors des requêtes auprès d’organismes de santé.
- **`PEX-023`** (Assurance personnes, `M-16`): Verrou de révision humaine qualifiée avant refus d’assurabilité ou cessation de prestations vitales.
- **`PEX-024`** (Assurance personnes, `M-16`): Déclaration obligatoire, homologation et collecte probatoire des agents exploités par les sociétés mandataires.
- **`PEX-025`** (Assurance personnes, `M-16`): Protection cryptographique agile et conservation multidécennale des dossiers d’assurance de personnes.
- **`PEX-031`** (Assurance dommages, `M-17`): Profil pré-homologué d’élasticité catastrophique et interdiction des refus automatisés d’indemnisation.

- **`PEX-032`** (Assurance dommages, `M-17`): Assemblage déterministe exclusif des formulaires et avenants approuvés en assurance automobile.
- **`PEX-033`** (Assurance dommages, `M-17`): Journalisation probatoire et neutralité comparative des soumissions multi-assureurs hors groupe en courtage.
- **`PEX-034`** (Assurance dommages, `M-17`): Identités d’agents dédiées par cabinet tiers et décontamination multimodale sur les passerelles externes.
- **`PEX-035`** (Assurance dommages, `M-17`): Qualification indépendante des modèles externes de catastrophe et traçabilité des émissions associées à l’assurance.
- **`PEX-041`** (Groupe diversifié, `M-18`): Cloisonnement technique inter-entités et blocage du partage banque-assurance dans le socle de groupe.
- **`PEX-042`** (Groupe diversifié, `M-18`): Jeton vérifiable de consentement exprès granulaire avant toute délégation inter-filiales.
- **`PEX-043`** (Groupe diversifié, `M-18`): Encadrement contractuel d’impartition intra-groupe, auditabilité par filiale et plans de sortie du noyau mutualisé.
- **`PEX-044`** (Groupe diversifié, `M-18`): Présentation désagrégée par métier réglementé des inventaires de modèles, des livres et des divulgations climatiques.

## 7. Liaisons exécutables `G0` par module de la trousse (`95` entrées)
- **`authz_pqc_audit`** (24 contrôles): `S-01`, `S-03`, `S-14`, `S-15`, `R-07`, `O-02`, `O-09`, `G-15`, `SBB-SECRETS-VAULT`, `SBB-SIGNED-HUMAN-APPROVAL`, `SBB-IMMUTABLE-AUDIT-LEDGER`, `CAP-046`, `EXIG-MCP-11`, `EXIG-OBS-06`, `EXIG-OBS-07` (+ 9 autres).
- **`evalops_prr`** (24 contrôles): `G-01`, `G-03`, `G-05`, `G-06`, `G-07`, `G-10`, `F-04`, `2027-B001`, `EXIG-SEC-24`, `EXIG-EVA-03`, `EXIG-AMF-11`, `C02`, `C04`, `C05`, `C06` (+ 9 autres).
- **`harness_proto`** (18 contrôles): `R-01`, `EXIG-MCP-03`, `EXIG-MCP-15`, `EXIG-MCP-16`, `EXIG-MCP-18`, `EXIG-MCP-19`, `EXIG-MCP-20`, `EXIG-A2A-03`, `C01`, `C07`, `C09`, `C10`, `C11`, `C12`, `C13` (+ 3 autres).
- **`policies_opa`** (10 contrôles): `S-06`, `S-09`, `F-14`, `SBB-GUARDRAILS-ENGINE`, `EXIG-SEC-06`, `EXIG-SEC-25`, `C03`, `C16`, `C25`, `C28`.
- **`policy_saga`** (19 contrôles): `S-08`, `S-11`, `R-03`, `R-06`, `R-14`, `SBB-FINOPS-BUDGET-QUOTA`, `EXIG-SEC-12`, `EXIG-SEC-13`, `EXIG-SEC-14`, `EXIG-SEC-15`, `EXIG-ORC-18`, `EXIG-ORC-20`, `EXIG-ORC-28`, `C15`, `C18` (+ 4 autres).

## 8. Spécifications techniques et normatives `L+` (`57` entrées)

Répartition par maturité: `FINAL_STANDARD` (38), `REGULATION_IN_FORCE` (5), `IETF_WORKING_GROUP_DRAFT` (4), `SPEC_DEVELOPMENT` (3), `FIPS_STANDARD` (3), `RC_OR_ALPHA` (2), `IETF_INDIVIDUAL_DRAFT` (1), `REGULATION_ADOPTED_FUTURE` (1) ; par licence: `IETF-Trust` (27), `Apache-2.0` (10), `MIT` (6), `NIST-PD` (3), `OIDF-Spec` (3), `EU-Public-Domain` (3), `Canada-OGL` (2), `CC-BY-4.0` (1), `BSD-3-Clause` (1), `QC-Public-Domain` (1).
- **`SPEC-MCP-2026-07-28-TOOLS`** (`2026-07-28@5f5440bb`, `FINAL_STANDARD`, `SRC-072`): Model Context Protocol (MCP) Server Tools.
- **`SPEC-MCP-2026-07-28-HTTP`** (`2026-07-28@5f5440bb`, `FINAL_STANDARD`, `SRC-074`): Model Context Protocol (MCP) Streamable HTTP Transport.
- **`SPEC-MCP-2026-07-28-SEC`** (`2026-07-28@5f5440bb`, `FINAL_STANDARD`, `SRC-078`): Model Context Protocol (MCP) Authorization Security Considerations.
- **`SPEC-MCP-2026-07-28-SCHEMA`** (`2026-07-28@5f5440bb`, `FINAL_STANDARD`, `SRC-080`): Model Context Protocol (MCP) TypeScript Schema.
- **`SPEC-MCP-SEP-2596`** (`Final@862397ce`, `FINAL_STANDARD`, `SRC-081`): MCP SEP-2596: Feature Lifecycle and Deprecation Policy.
- **`SPEC-MCP-SEP-3398`** (`Accepted@862397ce`, `SPEC_DEVELOPMENT`, `SRC-082`): MCP SEP-3398: Release Cycle Updates.
- **`SPEC-A2A-V1-0-1-SPEC`** (`v1.0.1@33035925`, `FINAL_STANDARD`, `SRC-083`): Agent2Agent (A2A) Protocol Specification.

- **`SPEC-A2A-V1-0-1-PROTO`** (`v1.0.1@33035925`, `FINAL_STANDARD`, `SRC-084`): Agent2Agent (A2A) Protobuf Contract.
- **`SPEC-A2A-V1-1-0-RC`** (`v1.1.0-rc@78e1d6a1`, `RC_OR_ALPHA`, `SRC-085`): Agent2Agent (A2A) Specification Release Candidate.
- **`SPEC-A2A-TCK-ALPHA3`** (`1.0.0.alpha3@5daf0144`, `RC_OR_ALPHA`, `SRC-086`): A2A Technology Compatibility Kit (a2a-tck).
- **`SPEC-OPA-REGO-V1-22-4`** (`v1.22.4@ba39415d`, `FINAL_STANDARD`, `SRC-087`): Open Policy Agent (OPA) Rego Language Reference.
- **`SPEC-OPA-TEST-V1-22-4`** (`v1.22.4@ba39415d`, `FINAL_STANDARD`, `SRC-088`): Open Policy Agent (OPA) Policy Testing & Coverage.
- **`SPEC-OTEL-V1-41-0`** (`v1.41.0@e018fe6f`, `FINAL_STANDARD`, `SRC-089`): OpenTelemetry Semantic Conventions GenAI Registry.
- **`SPEC-OTEL-GENAI-DEV-85`** (`244465e9@2026-10-31`, `SPEC_DEVELOPMENT`, `SRC-090`): OpenTelemetry semantic-conventions-genai (85 attributs Development).
- **`SPEC-OTEL-AGENT-SPANS`** (`2026-11-05@main`, `SPEC_DEVELOPMENT`, `SRC-037`): OpenTelemetry GenAI Agent and Framework Spans.

- **`SPEC-FOCUS-V1-4`** (`v1.4`, `FINAL_STANDARD`, `SRC-023`): FinOps Open Cost and Usage Specification (FOCUS).
- **`SPEC-JSON-SCHEMA-2020-12`** (`2020-12`, `FINAL_STANDARD`, `SRC-021`): JSON Schema Draft 2020-12 Core (draft-bhutton-json-schema-01).
- **`SPEC-CLOUDEVENTS-1-0-2`** (`v1.0.2`, `FINAL_STANDARD`, `SRC-035`): CloudEvents Specification.
- **`SPEC-RFC-7493-IJSON`** (`RFC 7493`, `FINAL_STANDARD`, `SRC-004`): RFC 7493: The I-JSON Message Format.
- **`SPEC-RFC-7515-JWS`** (`RFC 7515`, `FINAL_STANDARD`, `SRC-005`): RFC 7515: JSON Web Signature (JWS).
- **`SPEC-RFC-8032-EDDSA`** (`RFC 8032`, `FINAL_STANDARD`, `SRC-076`): RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA).
- **`SPEC-RFC-8693-OBO`** (`RFC 8693`, `FINAL_STANDARD`, `SRC-041`): RFC 8693: OAuth 2.0 Token Exchange.
- **`SPEC-RFC-8707-RESIND`** (`RFC 8707`, `FINAL_STANDARD`, `SRC-009`): RFC 8707: Resource Indicators for OAuth 2.0.

- **`SPEC-RFC-8785-JCS`** (`RFC 8785`, `FINAL_STANDARD`, `SRC-077`): RFC 8785: JSON Canonicalization Scheme (JCS).
- **`SPEC-RFC-9334-RATS`** (`RFC 9334 (Informational)`, `FINAL_STANDARD`, `SRC-010`): RFC 9334: Remote ATtestation procedureS (RATS) Architecture.

## 9. Chaîne d'étanchéité `G0`–`G5` et double recollation stratifiée `G3`

Les deux passes de recollation à l'aveugle portent chacune sur cent quarante-huit items répartis en quatre strates égales de trente-sept assertions (`empirique`, `juridique`, `spec_technique` et `assertions_g0`), avec un plancher de quatre items par unité narrative et un chevauchement nul entre passes. Les deux campagnes effectives consignent **148** items (`seed=20270901`) et **148** items (`seed=20270902`), atteignant `148 / 148` (`100,0 %`) après rectifications.

## 10. Chaînes d'opérationnalisation et d'encadrement normatif du graphe (`295` liaisons)

Axe `D01` sous `attenuation_risque` (2 liaisons): `REL_0235` (de `erreurs-silencieuses-cascade` vers `choregraphie-event-mesh`: Coupe les boucles par compteur de sauts), `REL_0236` (de `erreurs-silencieuses-cascade` vers `dette-semantique-ontologies`: Prévient les écarts sémantiques par schémas typés).

Axe `D02` sous `attenuation_risque` (8 liaisons): `REL_0308` (de `harnais-deterministe-8-etapes` vers `constance-pass-k`: Élève la constance multi-essais vers pass^5 ≥ 95 %), `REL_0309` (de `harnais-deterministe-8-etapes` vers `erreurs-silencieuses-cascade`: Intercepte les sorties plausibles mais invalides avant propagation), `REL_0400` (de `partition-hybride-80-20` vers `loi-de-lusser`: Encapsule le non-déterminisme contre la chute exponentielle), `REL_0540` (de `separation-controleur-executeur-determinisme` vers `constance-pass-k`: Réduction du non-déterminisme par flux déterministe), `REL_0565` (de `supervision-hitl-hotl-abstention` vers `approbation-ciba`: Neutralise la fatigue d'approbation de 93 % sur les points critiques), `REL_0567` (de `supervision-hitl-hotl-abstention` vers `atrophie-competences-humaines`: Vue différentielle et quotas contre le clic réflexe), `REL_0574` (de `supervision-hitl-hotl-abstention` vers `rupture-modele-conversationnel-agent-boucle`: Libération humaine H-31 sur les actions irréversibles), `REL_0608` (de `usine-logicielle-agentic-sdlc` vers `dette-cognitive-vs-technique`: Résorption patrimoniale RPG/COBOL sous oracle).

Axe `D03` sous `attenuation_risque` (7 liaisons): `REL_0027` (de `anti-verrouillage-standards` vers `dette-cognitive-vs-technique`: Remplacement du couplage N×M propriétaire par des standards N+M), `REL_0028` (de `anti-verrouillage-standards` vers `fusion-acp-collision-terminologique`: Fondation neutre assurant une sortie ordonnée lors d'une fusion), `REL_0029` (de `anti-verrouillage-standards` vers `pieges-gouvernance`: Noyau possédé et réversibilité contre la rente SaaS), `REL_0231` (de `epinglage-schemas-mcp` vers `protocole-mcp`: Condensats SHA-256 contre le rug-pull MCP), `REL_0233` (de `epinglage-schemas-mcp` vers `tool-poisoning-rug-pull`: Épinglage et liste d'admission contre le rug-pull MCP), `REL_0234` (de `ergonomie-aci-anti-swagger` vers `tool-poisoning-rug-pull`: Réduit la confusion d'outils (AP-04)), `REL_0415` (de `passerelle-mcp-ai-gateway` vers `tool-poisoning-rug-pull`: Passerelle MCP centralisant admission et politiques).

Axe `D04` sous `attenuation_risque` (13 liaisons): `REL_0143` (de `confinement-cua-patrimoine-sans-api` vers `injection-indirecte-prompt`: Verrouille les zones d'écran et touches destructrices des CUA), `REL_0153` (de `contrats-donnees-write-audit-publish` vers `dette-semantique-ontologies`: Quarantaine WAP contre dérive silencieuse), `REL_0159` (de `couche-anti-corruption-acl` vers `dette-semantique-ontologies`: Exactitude Decimal COMP-3 sans IEEE 754), `REL_0160` (de `couche-anti-corruption-acl` vers `encapsulation-patrimoine-it-ot`: Protège la charge et l'intégrité des systèmes d'enregistrement), `REL_0161` (de `couche-anti-corruption-acl` vers `erreurs-silencieuses-cascade`: Protège les SoR des rafales et doubles écritures), `REL_0185` (de `dette-semantique-ontologies` vers `erreurs-silencieuses-cascade`: Élimine les erreurs sémantiques silencieuses du SQL libre), `REL_0296` (de `gouvernance-acces-rag-ancrage` vers `injection-indirecte-prompt`: Filtrage RBAC/ABAC par fragment et attribution vérifiable), `REL_0367` (de `memoire-coala-4-tiroirs` vers `efvp-transfert-hors-quebec`: Isolation et oubli bi-temporel sous Loi 25).

Axe `D05` sous `attenuation_risque` (9 liaisons): `REL_0041` (de `arbre-sobriete-oo1-oo4` vers `pathologies-reactives-backpressure`: Prévient les échecs MAST et l'effet Ringelmann), `REL_0120` (de `choregraphie-event-mesh` vers `erreurs-silencieuses-cascade`: Retient les effets irréversibles via le tampon à fenêtre de grâce), `REL_0378` (de `negociation-b2b-diplomate-evaluateur` vers `responsabilite-mandat-contrats-b2b`: Protection secrets et erreur en B2B), `REL_0397` (de `paradigme-apm-autonomie-encadree` vers `supervision-hitl-hotl-abstention`: Compensation par frames locaux lorsque l'humain sature), `REL_0431` (de `pont-ia-physique-ros2-simplex` vers `erreurs-silencieuses-cascade`: Enveloppe physique Simplex IEC 61508), `REL_0526` (de `saga-compensatoire` vers `erreurs-silencieuses-cascade`: Répare les échecs partiels sans verrou 2PC), `REL_0528` (de `saga-compensatoire` vers `modes-echecs-emergents-frontiere`: Idempotence et compensations bornant les effets partiels), `REL_0537` (de `semantique-effet-idempotence-uetr` vers `production-agentique-canadienne-2025-2026`: Prévention des doubles exécutions financières et traçabilité comptable).

Axe `D06` sous `attenuation_risque` (12 liaisons): `REL_0036` (de `approbation-ciba` vers `supervision-hitl-hotl-abstention`: Preuve FIDO2 contre approbation complaisante), `REL_0173` (de `delegation-obo-deux-sauts` vers `anti-patrons-agentiques`: Parade contre l'emprunt et le délégué confus), `REL_0174` (de `delegation-obo-deux-sauts` vers `erreurs-silencieuses-cascade`: Atténuation des privilèges à chaque saut et fraîcheur CRL/OCSP), `REL_0175` (de `delegation-obo-deux-sauts` vers `identite-non-humaine-nhi`: Parade au délégué confus au 2e saut), `REL_0177` (de `delegation-obo-deux-sauts` vers `injection-indirecte-prompt`: Borne le rayon d'impact par échange RFC 8693 et DPoP), `REL_0315` (de `identite-non-humaine-nhi` vers `kya-verification-agent-tiers`: Suppression des secrets statiques et traçabilité du cycle de vie NHI), `REL_0436` (de `post-quantique-ml-dsa-slh-dsa` vers `delegation-obo-deux-sauts`: Transaction Tokens contre HTTP 431 PQ), `REL_0440` (de `post-quantique-ml-dsa-slh-dsa` vers `scellage-jcs-scitt`: Protection SCITT + SLH-DSA contre la ruine probatoire).

Axe `D07` sous `attenuation_risque` (20 liaisons): `REL_0017` (de `alignement-deceptif-red-teaming-adversarial` vers `defense-hors-modele-camel-confinement`: Évaluation adversariale quantifiant les angles morts défensifs), `REL_0141` (de `confidentialite-materielle-tee-hyok` vers `six-substrats-etat-souverainete`: Séquestre HYOK, TEE et continuité bimodèle), `REL_0145` (de `confinement-opensandbox-firecracker-wasi` vers `injection-indirecte-prompt`: Confinement microVM anti-exfiltration), `REL_0146` (de `confinement-shadi-sandbox` vers `chaine-approvisionnement-agent-skills`: Isole l'exécution des scripts et composants non fiables), `REL_0147` (de `confinement-shadi-sandbox` vers `injection-indirecte-prompt`: Confinement matériel sans réseau ni secret), `REL_0149` (de `confinement-shadi-sandbox` vers `tool-poisoning-rug-pull`: Isole l'exécution de code arbitraire (ASI05)), `REL_0172` (de `defense-hors-modele-camel-confinement` vers `injection-indirecte-prompt`: Séparation de privilège hors modèle contre l'injection indirecte), `REL_0319` (de `injection-indirecte-prompt` vers `confinement-shadi-sandbox`: Confine l'exécution du code généré après lecture non fiable).

Axe `D08` sous `attenuation_risque` (6 liaisons): `REL_0061` (de `banc-evalops-hermetique` vers `erreurs-silencieuses-cascade`: Détection pass^k et chaos pré-production), `REL_0111` (de `canonicalisation-jcs-rfc8785` vers `signature-agent-card-ancrage`: Canonicalisation RFC 8785 fiabilisant la vérification JWS), `REL_0199` (de `double-couloir-probatoire-pii` vers `loi-25-article-12-1`: Évite l'exposition de PII en télémétrie courante), `REL_0253` (de `evaluation-continue-derives` vers `tool-poisoning-rug-pull`: Détection continue en production de la dérive silencieuse d'outil), `REL_0283` (de `finops-focus-cpo` vers `erreurs-silencieuses-cascade`: Disjoncteur budgétaire anti-emballement), `REL_0487` (de `provenance-artefacts-aibom-5-horloges` vers `tool-poisoning-rug-pull`: Détection des dérives d'outils par attestation et AIBOM).

Axe `D09` sous `attenuation_risque` (1 liaisons): `REL_0556` (de `souverainete-espaces-donnees-tee-hyok` vers `efvp-transfert-hors-quebec`: HYOK et TEE face au CLOUD Act).

Axe `D10` sous `attenuation_risque` (2 liaisons): `REL_0019` (de `anti-patrons-agentiques` vers `dette-cognitive-vs-technique`: Éradique les 12 modes d'échec structurels en ARB), `REL_0273` (de `federation-multi-plateformes-gravite` vers `soc-soar-coupe-circuit`: Prévient les boucles circulaires de webhooks inter-SaaS).

Axe `D11` sous `attenuation_risque` (1 liaisons): `REL_0037` (de `approbation-reflexe-biais-automatisation` vers `pieges-gouvernance`: Parade ergonomique et organisationnelle contre l'approbation réflexe).

Axe `D01` sous `encadrement_normatif` (1 liaisons): `REL_0237` (de `erreurs-silencieuses-cascade` vers `topologies-patrons-orchestration`: Impose la preuve mesurée avant multiagent).

Axe `D02` sous `encadrement_normatif` (4 liaisons): `REL_0193` (de `distinction-agent-flux-ambiant` vers `identite-non-humaine-nhi`: Exclut comptes humains et secrets partagés), `REL_0204` (de `douze-principes-directeurs-prin` vers `exigences-cre-ia-305`: Fonde les 305 exigences vérifiables), `REL_0211` (de `echelle-autonomie-l0-l4` vers `classes-risque-agents-et-plafonds`: Plafonne l'autonomie par la classe de risque), `REL_0513` (de `regle-maillon-plus-eleve` vers `echelle-autonomie-l0-l4`: Étend le périmètre de sécurité du maillon le plus élevé en amont).

Axe `D03` sous `encadrement_normatif` (5 liaisons): `REL_0011` (de `agntcy-slim` vers `contrats-interfaces-catalogue-entreprise`: Subordonne OASF/ADS au catalogue d'entreprise), `REL_0024` (de `anti-verrouillage-standards` vers `bsif-e-23`: Exigences de diligence de tiers dans les institutions réglementées), `REL_0097` (de `cadre-eif-4-couches` vers `eu-ai-act`: Basculement vers l'obligation légale via l'Interoperable Europe Act), `REL_0373` (de `metriques-soutien-vs-production` vers `regime-preuve-trois-degres-absence`: Règle anti-amalgame sur les décomptes auto-déclarés de soutien), `REL_0462` (de `protocole-ap2` vers `approbation-ciba`: Soumet tout paiement agentique à l'approbation P3 signée).

<!-- BIBLIOGRAPHIE_BRUTE_DEBUT -->
## Matrice complète `EXIG / CAP / PRR / C01–C40 / SBB`, spécifications `L+` et extraits `CA-G0-SYNC`

- `S-01` (PRR_BLOCKING, `ch17`) → `authz_pqc_audit.obo_dpop.validate_obo_delegation`.
- `S-03` (PRR_BLOCKING, `ch17`) → `authz_pqc_audit.obo_dpop.extract_act_chain`.
- `S-06` (PRR_BLOCKING, `ch20`) → `policies_opa.opa_runner.OpaPolicyEngine.evaluate`.
- `S-08` (PRR_BLOCKING, `ch20`) → `policy_saga.taint_camel.delegate_taint_envelope`.
- `S-09` (PRR_BLOCKING, `ch20`) → `policies_opa.opa_runner.verify_rego_default_deny`.
- `S-11` (PRR_BLOCKING, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest`.
- `S-14` (PRR_BLOCKING, `ch17`) → `authz_pqc_audit.revocation_fsm.RevocationStateMachine`.
- `S-15` (PRR_BLOCKING, `ch17`) → `authz_pqc_audit.ciba_approval.verify_ciba_approval_tokens`.
- `R-01` (PRR_BLOCKING, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run`.
- `R-03` (PRR_BLOCKING, `ch15`) → `policy_saga.saga_orchestrator.compute_idempotency_key`.
- `R-06` (PRR_BLOCKING, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator`.
- `R-07` (PRR_BLOCKING, `ch17`) → `authz_pqc_audit.ciba_approval.compute_action_hash_h`.
- `R-14` (PRR_BLOCKING, `ch20`) → `policy_saga.taint_camel.SessionTaintTracker`.
- `O-02` (PRR_BLOCKING, `ch22`) → `authz_pqc_audit.otel_pii_mapper.redact_pii_bilingual`.
- `O-09` (PRR_BLOCKING, `ch24`) → `authz_pqc_audit.audit_scitt_focus.compute_cpo_and_focus`.
- `G-01` (PRR_BLOCKING, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001`.
- `G-03` (PRR_BLOCKING, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001`.
- `G-05` (PRR_BLOCKING, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking`.
- `G-06` (PRR_BLOCKING, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking`.
- `G-07` (PRR_BLOCKING, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking`.
- `G-10` (PRR_BLOCKING, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking`.
- `G-15` (PRR_BLOCKING, `ch24`) → `authz_pqc_audit.audit_scitt_focus.AuditChainLedger`.
- `F-04` (PRR_BLOCKING, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking`.
- `F-14` (PRR_BLOCKING, `ch20`) → `policies_opa.opa_runner.OpaPolicyEngine.evaluate`.
- `SBB-SECRETS-VAULT` (SBB, `ch17`) → `authz_pqc_audit.obo_dpop.validate_obo_delegation`.
- `SBB-GUARDRAILS-ENGINE` (SBB, `ch20`) → `policies_opa.opa_runner.OpaPolicyEngine`.
- `SBB-SIGNED-HUMAN-APPROVAL` (SBB, `ch17`) → `authz_pqc_audit.ciba_approval.verify_ciba_approval_tokens`.
- `SBB-IMMUTABLE-AUDIT-LEDGER` (SBB, `ch24`) → `authz_pqc_audit.audit_scitt_focus.AuditChainLedger`.
- `SBB-FINOPS-BUDGET-QUOTA` (SBB, `ch12`) → `policy_saga.decimal_money.from_decimal_str`.
- `2027-B001` (ADR_TEMPLATE, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001`.
- `CAP-046` (CAP, `ch24`) → `authz_pqc_audit.audit_scitt_focus.compute_cpo_and_focus`.
- `EXIG-MCP-03` (EXIG, `ch07`) → `harness_proto.mcp_pinning.verify_tools_list_against_catalog`.
- `EXIG-MCP-11` (EXIG, `ch17`) → `authz_pqc_audit.obo_dpop.validate_obo_delegation`.
- `EXIG-MCP-15` (EXIG, `ch07`) → `harness_proto.mcp_pinning.validate_mcp_headers`.
- `EXIG-MCP-16` (EXIG, `ch07`) → `harness_proto.mcp_pinning.validate_mcp_headers`.
- `EXIG-MCP-18` (EXIG, `ch07`) → `harness_proto.mcp_pinning.validate_mcp_headers`.
- `EXIG-MCP-19` (EXIG, `ch04`) → `harness_proto.pipeline.validate_strict_schema`.
- `EXIG-MCP-20` (EXIG, `ch07`) → `harness_proto.mcp_pinning.compute_tool_definition_digest`.
- `EXIG-A2A-03` (EXIG, `ch08`) → `harness_proto.a2a_card.validate_agent_card`.
- `EXIG-OBS-06` (EXIG, `ch22`) → `authz_pqc_audit.otel_pii_mapper.map_span_attributes`.
- `EXIG-OBS-07` (EXIG, `ch22`) → `authz_pqc_audit.otel_pii_mapper.map_span_attributes`.
- `EXIG-OBS-09` (EXIG, `ch22`) → `authz_pqc_audit.otel_pii_mapper.redact_pii_bilingual`.
- `EXIG-OBS-12` (EXIG, `ch24`) → `authz_pqc_audit.audit_scitt_focus.AuditChainLedger.append_record`.
- `EXIG-SEC-06` (EXIG, `ch20`) → `policies_opa.opa_runner.OpaPolicyEngine.evaluate`.
- `EXIG-SEC-12` (EXIG, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest`.
- `EXIG-SEC-13` (EXIG, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest`.
- `EXIG-SEC-14` (EXIG, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest`.
- `EXIG-SEC-15` (EXIG, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest`.
- `EXIG-SEC-24` (EXIG, `ch23`) → `evalops_prr.metamorphic.verify_metamorphic_pair`.
- `EXIG-SEC-25` (EXIG, `ch20`) → `policies_opa.opa_runner.OpaPolicyEngine.run_coverage`.
- `EXIG-ORC-18` (EXIG, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator`.
- `EXIG-ORC-20` (EXIG, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator`.
- `EXIG-ORC-28` (EXIG, `ch15`) → `policy_saga.saga_orchestrator.CompensationChannel`.
- `EXIG-EVA-03` (EXIG, `ch23`) → `evalops_prr.wilson_bounds.evaluate_wilson_gate`.
- `EXIG-AMF-11` (EXIG, `ch23`) → `evalops_prr.metamorphic.verify_metamorphic_pair`.
- `C01` (C40, `ch04`) → `harness_proto.pipeline.DeterministicHarness`.
- `C02` (C40, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40`.
- `C03` (C40, `ch20`) → `policies_opa.opa_runner.OpaPolicyEngine`.
- `C04` (C40, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40`.
- `C05` (C40, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001`.
- `C06` (C40, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking`.
- `C07` (C40, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run`.
- `C08` (C40, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40`.
- `C09` (C40, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run`.
- `C10` (C40, `ch04`) → `harness_proto.pipeline.validate_strict_schema`.
- `C11` (C40, `ch07`) → `harness_proto.mcp_pinning.StreamableHttpAdapter`.
- `C12` (C40, `ch07`) → `harness_proto.mcp_pinning.verify_tools_list_against_catalog`.
- `C13` (C40, `ch08`) → `harness_proto.a2a_card.validate_agent_card`.
- `C14` (C40, `ch08`) → `harness_proto.a2a_card.validate_agent_card`.
- `C15` (C40, `ch20`) → `policy_saga.taint_camel.SessionTaintTracker`.
- `C16` (C40, `ch20`) → `policies_opa.opa_runner.OpaPolicyEngine.evaluate`.
- `C17` (C40, `ch23`) → `evalops_prr.mock_mcp_harness.evaluate_trajectory`.
- `C18` (C40, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest`.
- `C19` (C40, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run`.
- `C20` (C40, `ch24`) → `authz_pqc_audit.audit_scitt_focus.AuditChainLedger`.
- `C21` (C40, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator`.
- `C22` (C40, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator`.
- `C23` (C40, `ch15`) → `policy_saga.saga_orchestrator.compute_idempotency_key`.
- `C24` (C40, `ch17`) → `authz_pqc_audit.ciba_approval.verify_ciba_approval_tokens`.
- `C25` (C40, `ch20`) → `policies_opa.taint_camel.delegate_taint_envelope`.
- `C26` (C40, `ch17`) → `authz_pqc_audit.revocation_fsm.RevocationStateMachine`.
- `C27` (C40, `ch18`) → `authz_pqc_audit.pqc_http431.evaluate_http_431`.
- `C28` (C40, `ch20`) → `policies_opa.opa_runner.OpaPolicyEngine.evaluate`.
- `C29` (C40, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest`.
- `C30` (C40, `ch22`) → `authz_pqc_audit.otel_pii_mapper.map_span_attributes`.
- `C31` (C40, `ch23`) → `evalops_prr.mock_mcp_harness.compute_pass_k`.
- `C32` (C40, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40`.
- `C33` (C40, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40`.
- `C34` (C40, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run`.
- `C35` (C40, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001`.
- `C36` (C40, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40`.
- `C37` (C40, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking`.
- `C38` (C40, `ch24`) → `authz_pqc_audit.audit_scitt_focus.seal_merkle_root`.
- `C39` (C40, `ch24`) → `authz_pqc_audit.audit_scitt_focus.compute_cpo_and_focus`.
- `C40` (C40, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40`.
- `SPEC-MCP-2026-07-28-TOOLS` (`2026-07-28@5f5440bb`, `SRC-072`): Model Context Protocol (MCP) Server Tools.
- `SPEC-MCP-2026-07-28-HTTP` (`2026-07-28@5f5440bb`, `SRC-074`): Model Context Protocol (MCP) Streamable HTTP Transport.
- `SPEC-MCP-2026-07-28-SEC` (`2026-07-28@5f5440bb`, `SRC-078`): Model Context Protocol (MCP) Authorization Security Considerations.
- `SPEC-MCP-2026-07-28-SCHEMA` (`2026-07-28@5f5440bb`, `SRC-080`): Model Context Protocol (MCP) TypeScript Schema.
- `SPEC-MCP-SEP-2596` (`Final@862397ce`, `SRC-081`): MCP SEP-2596: Feature Lifecycle and Deprecation Policy.
- `SPEC-MCP-SEP-3398` (`Accepted@862397ce`, `SRC-082`): MCP SEP-3398: Release Cycle Updates.
- `SPEC-A2A-V1-0-1-SPEC` (`v1.0.1@33035925`, `SRC-083`): Agent2Agent (A2A) Protocol Specification.
- `SPEC-A2A-V1-0-1-PROTO` (`v1.0.1@33035925`, `SRC-084`): Agent2Agent (A2A) Protobuf Contract.
- `SPEC-A2A-V1-1-0-RC` (`v1.1.0-rc@78e1d6a1`, `SRC-085`): Agent2Agent (A2A) Specification Release Candidate.
- `SPEC-A2A-TCK-ALPHA3` (`1.0.0.alpha3@5daf0144`, `SRC-086`): A2A Technology Compatibility Kit (a2a-tck).
- `SPEC-OPA-REGO-V1-22-4` (`v1.22.4@ba39415d`, `SRC-087`): Open Policy Agent (OPA) Rego Language Reference.
- `SPEC-OPA-TEST-V1-22-4` (`v1.22.4@ba39415d`, `SRC-088`): Open Policy Agent (OPA) Policy Testing & Coverage.
- `SPEC-OTEL-V1-41-0` (`v1.41.0@e018fe6f`, `SRC-089`): OpenTelemetry Semantic Conventions GenAI Registry.
- `SPEC-OTEL-GENAI-DEV-85` (`244465e9@2026-10-31`, `SRC-090`): OpenTelemetry semantic-conventions-genai (85 attributs Development).
- `SPEC-OTEL-AGENT-SPANS` (`2026-11-05@main`, `SRC-037`): OpenTelemetry GenAI Agent and Framework Spans.
- `SPEC-FOCUS-V1-4` (`v1.4`, `SRC-023`): FinOps Open Cost and Usage Specification (FOCUS).
- `SPEC-JSON-SCHEMA-2020-12` (`2020-12`, `SRC-021`): JSON Schema Draft 2020-12 Core (draft-bhutton-json-schema-01).
- `SPEC-CLOUDEVENTS-1-0-2` (`v1.0.2`, `SRC-035`): CloudEvents Specification.
- `SPEC-RFC-7493-IJSON` (`RFC 7493`, `SRC-004`): RFC 7493: The I-JSON Message Format.
- `SPEC-RFC-7515-JWS` (`RFC 7515`, `SRC-005`): RFC 7515: JSON Web Signature (JWS).
- `SPEC-RFC-8032-EDDSA` (`RFC 8032`, `SRC-076`): RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA).
- `SPEC-RFC-8693-OBO` (`RFC 8693`, `SRC-041`): RFC 8693: OAuth 2.0 Token Exchange.
- `SPEC-RFC-8707-RESIND` (`RFC 8707`, `SRC-009`): RFC 8707: Resource Indicators for OAuth 2.0.
- `SPEC-RFC-8785-JCS` (`RFC 8785`, `SRC-077`): RFC 8785: JSON Canonicalization Scheme (JCS).
- `SPEC-RFC-9334-RATS` (`RFC 9334 (Informational)`, `SRC-010`): RFC 9334: Remote ATtestation procedureS (RATS) Architecture.
- `SPEC-RFC-9396-RAR` (`RFC 9396`, `SRC-042`): RFC 9396: OAuth 2.0 Rich Authorization Requests (RAR).
- `SPEC-RFC-9449-DPOP` (`RFC 9449`, `SRC-043`): RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP).
- `SPEC-RFC-9943-SCITT` (`RFC 9943`, `SRC-044`): RFC 9943: Supply Chain Integrity, Transparency, and Trust (SCITT) Architecture.
- `SPEC-RFC-9964-MLDSA` (`RFC 9964`, `SRC-012`): RFC 9964: ML-DSA for JOSE and COSE.
- `SPEC-DRAFT-TXTOKENS-11` (`draft-ietf-oauth-transaction-tokens-11`, `SRC-013`): OAuth Transaction Tokens (Internet-Draft).
- `SPEC-DRAFT-AGENT-REVOC-01` (`draft-chen-oauth-agent-revocation-01`, `SRC-017`): OAuth 2.0 Agent Authorization Explicit Revocation (Internet-Draft).
- `SPEC-DRAFT-WIMSE-PRAC-08` (`draft-ietf-wimse-workload-identity-practices-08`, `SRC-047`): WIMSE Workload Identity Practices (Internet-Draft).
- `SPEC-DRAFT-WIMSE-AIMS-01` (`draft-ietf-wimse-aims-01`, `SRC-048`): WIMSE AI Identity Management System (Internet-Draft).
- `SPEC-DRAFT-IDEMPOTENCY-KEY` (`draft-ietf-httpapi-idempotency-key-header-09`, `SRC-036`): The Idempotency-Key HTTP Header Field (Internet-Draft).
- `SPEC-NIST-FIPS-203` (`FIPS 203`, `SRC-049`): NIST FIPS 203: ML-KEM Key-Encapsulation Mechanism.
- `SPEC-NIST-FIPS-204` (`FIPS 204`, `SRC-050`): NIST FIPS 204: ML-DSA Digital Signature Standard.
- `SPEC-NIST-FIPS-205` (`FIPS 205`, `SRC-018`): NIST FIPS 205: SLH-DSA Stateless Hash-Based Signature Standard.
- `SPEC-OPENID-CIBA-1-0` (`1.0`, `SRC-045`): OpenID Connect Client-Initiated Backchannel Authentication Core 1.0.
- `SPEC-OPENID-SSF-1-0` (`1.0`, `SRC-019`): OpenID Shared Signals Framework Specification 1.0.
- `SPEC-OPENID-CAEP-1-0` (`1.0`, `SRC-020`): OpenID Continuous Access Evaluation Profile (CAEP) 1.0.
- `SPEC-REG-EU-AI-ACT-2024-1689` (`(UE) 2024/1689 + (UE) 2026/1744`, `SRC-060`): Règlement (UE) 2024/1689 sur l'intelligence artificielle (EU AI Act).
- `SPEC-REG-EN-18286-2026` (`(UE) 2026/2274`, `SRC-067`): Décision d'exécution (UE) 2026/2274 — Norme harmonisée EN 18286:2026 (QMS Art. 17).
- `SPEC-REG-DORA-2022-2554` (`(UE) 2022/2554`, `SRC-062`): Règlement (UE) 2022/2554 sur la résilience opérationnelle numérique (DORA).
- `SPEC-REG-QC-LOI25-2021-C25` (`LQ 2021, c. 25`, `SRC-063`): LQ 2021, c. 25 — Loi modernisant la protection des renseignements personnels (Loi 25).
- `SPEC-REG-BSIF-E23-2027` (`E-23 (eff. 2027-05-01)`, `SRC-065`): BSIF / OSFI Ligne directrice E-23 — Gestion du risque de modélisation.
- `SPEC-REG-BSIF-B10-2023` (`B-10 (2023)`, `SRC-068`): BSIF / OSFI Guideline B-10 — Third-Party Risk Management.
- `SPEC-RFC-2119` (`RFC 2119 (1997-03)`, `SRC-125`): RFC 2119: Key words for use in RFCs to Indicate Requirement Levels.
- `SPEC-RFC-6902` (`RFC 6902 (2013-04)`, `SRC-126`): RFC 6902: JavaScript Object Notation (JSON) Patch.
- `SPEC-RFC-8555` (`RFC 8555 (2019-03)`, `SRC-127`): RFC 8555: Automatic Certificate Management Environment (ACME).
- `SPEC-RFC-8705` (`RFC 8705 (2020-02)`, `SRC-128`): RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication.
- `SPEC-RFC-9207` (`RFC 9207 (2022-03)`, `SRC-129`): RFC 9207: OAuth 2.0 Authorization Server Issuer Identification.
- `SPEC-RFC-9420` (`RFC 9420 (2023-07)`, `SRC-130`): RFC 9420: The Messaging Layer Security (MLS) Protocol.
- `SPEC-RFC-9421` (`RFC 9421 (2024-02)`, `SRC-131`): RFC 9421: HTTP Message Signatures.
- `SPEC-RFC-9562` (`RFC 9562 (2024-05)`, `SRC-132`): RFC 9562: Universally Unique IDentifiers (UUIDs / UUIDv7).
- `SPEC-RFC-9700` (`RFC 9700 (2025-01)`, `SRC-133`): RFC 9700: Best Current Practice for OAuth 2.0 Security (BCP 240).
- `SPEC-RFC-9728` (`RFC 9728 (2025-04)`, `SRC-134`): RFC 9728: OAuth 2.0 Protected Resource Metadata.
- `SPEC-RFC-9745` (`RFC 9745 (2025-04)`, `SRC-135`): RFC 9745: The Deprecation HTTP Response Header Field.
- `G0-EX-CH01-01` (`ch04`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/schemas/harness_extraction.schema.json` L1–24 (`6b4428a1f8a6abcd2029280cded86b0e983ddb349d0f05c6ba0192c010f95aac`).
- `G0-EX-CH01-02` (`ch04`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/harness_proto/pipeline.py` L204–232 (`75110799d751ee4b93c58c7aff4e2b6ce0c2c8d29c50b6d1668b4bf895dfc275`).
- `G0-EX-CH01-03` (`ch07`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/harness_proto/mcp_pinning.py` L227–260 (`350e1959e6f0c54ce549afc77b4ef14959851bc9e45ad1a2eee52b9b36f4fc95`).
- `G0-EX-CH01-04` (`ch08`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/harness_proto/a2a_card.py` L157–182 (`1a58d5eabab4361028420c902df71ef3b305f84bfd139e14c75c7318c545b899`).
- `G0-EX-CH02-01` (`ch17`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/authz_pqc_audit/obo_dpop.py` L85–114 (`d3c2d0ce031a283ba8b3e85fc230c51f6fa036a46942a573dfd77351922d2991`).
- `G0-EX-CH02-02` (`ch17`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/authz_pqc_audit/ciba_approval.py` L106–117 (`423ebd61ce4996bf314c2fcecab18e48129d46e379a70eaf57780b5e1e395307`).
- `G0-EX-CH02-03` (`ch18`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/authz_pqc_audit/pqc_http431.py` L149–177 (`c5c72e27a3932180e70ba9ebd63c109c5cc146c3af50d1327aed293f0e614855`).
- `G0-EX-CH02-04` (`ch22`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/authz_pqc_audit/otel_pii_mapper.py` L235–265 (`60bd160c1a507c6df31fd1dfc3811c866a6f17e8b623e961b2511c00c7e41889`).
- `G0-EX-CH03-01` (`ch20`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/policies_opa/rule_of_two.rego` L3–26 (`c0adc5553c040a592151fbcff54a27e85412764f82815220c5297e79ba652036`).
- `G0-EX-CH03-02` (`ch20`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/policies_opa/camel_taint.rego` L3–25 (`bd873cf677b35787f6054b97b6a2de30c0cb7c6a5a52375c8bce7275ab03637b`).
- `G0-EX-CH03-03` (`ch15`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/policy_saga/saga_orchestrator.py` L107–140 (`a2aac944f6ae06fe63c2f6482618bae3356d6270f3c5f6a3756c8592ebd1a536`).
- `G0-EX-CH04-01` (`ch35`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/evalops_prr/wilson_bounds.py` L43–70 (`3e685cbef8dea03f3c2c217d37c25e292295858505eae0769706570955f913ba`).
- `G0-EX-CH04-02` (`ch23`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/evalops_prr/metamorphic.py` L38–63 (`31ad0df04f1930471a8cec511d897834f72c35851e98f9c7cae1aa82002c1472`).
- `G0-EX-CH04-03` (`ch34`): `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/schemas/adr_2027_b001.schema.json` L1–32 (`4f0a41e7280851ce1413efeb6accb3632bb3ee6a0bfefc4fa7d92338156e36ae`).
<!-- BIBLIOGRAPHIE_BRUTE_FIN -->
