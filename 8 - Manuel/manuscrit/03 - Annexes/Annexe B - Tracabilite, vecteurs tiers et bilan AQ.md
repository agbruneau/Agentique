# Annexe B — Matrice de traçabilité (EXIG-* / CAP-* / PRR-75 / C01–C40 / 5 SBB), catalogue des vecteurs tiers, rapports CI G0 et bilan d'assurance qualité G0–G5 & CA-16

Cette annexe rassemble de façon déterministe la matrice de traçabilité reliant l'architecture de référence aux composants exécutables de `8 - Trousse/`, la table canonique de passage des cinq discordances inter-volumes, le bilan des quatre suites officielles de vecteurs tiers, les compteurs d'exécution de la barrière logicielle `G0` et le rapport consolidé des six barrières d'assurance qualité (`G0` à `G5` et lissage `CA-16`) arrêtés à la date de gel du 2 décembre 2026.

## Concordance des cinq discordances inter-volumes (`concordance-taxonomies.json`)

| ID | Sujet | Choix canonique Volume 8 | Section |
|---|---|---|---|
| `DISC-01` | Échelle d'autonomie L0–L4 : flux purement déterministe sans IA vs lecture/synthèse assistée par IA | Conservation de l'échelle L0–L4 comme gradation des droits de mutation et de sortie externe, avec distinction explicite entre cas exclus purement déterministes sans modèle (0.2) et profil L0–L1 en lecture seule sans écriture ni exfiltration. | 0.2 |
| `DISC-02` | Échelles de criticité et de risque : N0–N4, P0–P3, R1–R4, Classes 1–6 / Stades 0–4 / Paliers 1–3 | Conformément à AO-03, la prose du Volume 8 proscrit « Classe 1–6 », « Stade 0–4 » et « Palier 1–3 » ; le noyau technique utilise exclusivement les 3 niveaux de criticité (BLOQUANT, OBLIGATOIRE, RECOMMANDE) et les paliers d'outils P0–P3 avec table de correspondance dans 0.2. | 0.2 |
| `DISC-03` | Découpage architectural : 4 plans SI (Vol. 6) vs 4 plans du noyau déterministe (Vol. 7) vs 6 couches + 3 plans A/B/C (Vol. 2) vs C1–C5 (Vol. 5) | Les quatre modules techniques de 8 - Trousse/ ancrent leurs composants dans les Plans A (policies_opa, authz_pqc_audit coffre/approbation), B (otel_pii_mapper, audit_scitt_focus, evalops_prr) et C (harness_proto) du Cadre 2026 tout en exposant le noyau déterministe en quatre modules exécutables. | 0.2 |
| `DISC-04` | Notation d'architecture d'entreprise : ArchiMate 3.2 (Vol. 6) vs ArchiMate 4.0 C260 (Vol. 1 & Vol. 5) | Neutralité de notation : aucun artefact ArchiMate propriétaire n'est requis au gate G0 ; les stéréotypes de séparation contrôleur/acteur/politique restent compatibles aussi bien avec les profils 3.2 qu'avec 4.0 (C260). | 0.2 |
| `DISC-05` | Révision normative MCP : MCP 2025-11-25 (Vol. 7) vs MCP 2026-07-28 stateless et SEP-2596/SEP-3398 (Vol. 1, 2, 3, 5, 6, 8) | Épinglage normatif strict sur MCP 2026-07-28 (commit 5f5440bb) avec refus explicite du transport déprécié HTTP+SSE dans StreamableHttpAdapter (harness_proto/mcp_pinning.py) et isolation par McpTransportAdapter pour la fenêtre SEP-2596 jusqu'au 2027-07-28 et la cible SEP-3398 du 30 mars 2027. | 0.2 |

## Synthèse de la matrice de traçabilité (`matrice-exig-prr-c40.json`)

| Famille contractuelle | Entrées mappées | Modules cibles (`8 - Trousse/`) |
|---|---:|---|
| `ADR_TEMPLATE` | 1 | `evalops_prr` |
| `C40` | 40 | `authz_pqc_audit, evalops_prr, harness_proto, policies_opa, policy_saga` |
| `CAP` | 1 | `authz_pqc_audit` |
| `EXIG` | 24 | `authz_pqc_audit, evalops_prr, harness_proto, policies_opa, policy_saga` |
| `PRR_BLOCKING` | 24 | `authz_pqc_audit, evalops_prr, harness_proto, policies_opa, policy_saga` |
| `SBB` | 5 | `authz_pqc_audit, policies_opa, policy_saga` |

## Bilan exécutable de la barrière logicielle `G0` (`aq/rapports-g0.json`)

| Indicateur CI `G0` | Valeur vérifiée | Statut |
|---|---|---|
| Verdict global `execute_g0.py` | Code de retour `0` (`PASS`) | Conforme |
| Audit `SPDX MIT` & `requirements.lock` | `50` fichiers, `18` paquets | Conforme |
| Politiques `OPA / Rego` (`default allow := false`) | Couverture `100.0 %`, `45` tests | Conforme |
| Harnais `pytest` & schémas `2020-12` | `83` passés, `0` échecs, `0` ignorés | Conforme |
| Quatre suites vecteurs tiers & `CA-G0-SYNC` | `rfc8785` (PASS), `nist_acvp` (PASS), `a2a_tck` (PASS), `owasp_src055` (PASS) ; `14` extraits scellés | Actif |

## Couverture `MLR` (`RQ1`–`RQ6`) et bilan des six barrières (`G0`–`G5`)

| Axe | Thème de recherche | Seuil | Retenus `L+` | État |
|---|---|---:|---:|---|
| `RQ1` | Harnais déterministes 80/20 sous schémas JSON Schema Draft 2020-12 stricts, épinglage MCP 2026-07-28 et médiation A2A v1.0.1 | 6 | 23 | Conforme |
| `RQ2` | Identité non humaine, délégation OAuth 2.0 OBO à deux sauts, DPoP/CIBA et dimensionnement HTTP 431 sous ML-DSA-65/87 | 6 | 28 | Conforme |
| `RQ3` | Politiques OPA/Rego hors modèle (default allow := false), Règle de deux, contamination CaMeL, confinement sans KVM et Sagas compensables | 5 | 15 | Conforme |
| `RQ4` | Adaptateurs de transport post-gel et double couloir probatoire (OTel GenAI v1.41.0, caviardage PII, JCS, SCITT, SLH-DSA, FOCUS v1.4) | 5 | 21 | Conforme |
| `RQ5` | Bancs EvalOps hermétiques, constance pass^k, bornes de Wilson (>= 3/p), tests métamorphiques sans oracle et menaces OWASP SRC-055 | 6 | 26 | Conforme |
| `RQ6` | Traçabilité exécutable des portes bloquantes PRR/C01–C40/5 SBB, ancrage réglementaire CA/QC/UE borné et clause non-avis | 5 | 27 | Conforme |

| Barrière (ordre chronologique) | Rôle de contrôle indépendant | Critères | État constaté |
|---|---|---|---|
| `G0` — Banc logiciel `execute_g0.py` | `auteur-tests-oracle` ≠ `batisseur-code`, `OPA 100 %`, `4` vecteurs | `CA-19`, `CA-20` | PASS (`exit 0`) |
| `G1` — Garde déterministe sans modèle | Script `verifie_manuscrit.py --strict` (`CA-G0-SYNC`) | `CA-01`..`CA-11`, `CA-17`, `CA-20` | Contrôle actif |
| `G2` — Ancrage atomique Wyvern | Cinq `auditeur-wyvern` neufs (`00`–`04`) | `CA-10`, `CA-12` | 5 / 5 journaux (580 -> 577, 100 % supportées) |
| `G3` — Recollation passe 1 (`20270801`) | Agent `recollateur-1` (`4` strates × `15`, `≥ 8`/unité) | `CA-07`, `CA-13` | En attente d'exécution |
| `G4` — Critique à l'aveugle (`gauntlet-loop`) | Duels A/B vs étalons français + rejeu `G0+G1+G2` diff | `CA-15` | En attente d'exécution |
| `G5` — Lissage transversal (`CA-16`) | `lisseur-editorial` neuf + rejeu `G0+G1+G2` diff | `CA-16` | En attente d'exécution |
| `G3` — Recollation finale à froid (`20270802`) | `recollateur-2` disjoint sur texte et code finaux | `CA-14` | En attente d'exécution |
| `G5` — Annexes SSOT, rendu & visuel | `genere_annexes.py`, `assemble_livre.py`, `100 %` pages PDF | `CA-17`, `CA-18` | Contrôle actif |

## Étanchéité double aveugle et reproductibilité des livrables

Le manuel intègre **9 figures originales (7 schémas vectoriels `PlantUML` `-failfast2` et 2 organigrammes `Mermaid` à `300 DPI`)**, chacune bornée entre dix et quatorze nœuds. Aucun bloc de code n'est rédigé à la main dans la prose : les quatorze extraits d'au plus quarante lignes sont injectés depuis `8 - Trousse/` et contrôlés octet pour octet par empreinte `SHA-256` (`CA-G0-SYNC`) dès que `verifie_manuscrit.py` lève son masquage.

La séparation entre l'agent concepteur des tests (`auteur-tests-oracle`) et l'agent implémenteur (`batisseur-code`) en barrière `G0`, renforcée par l'exécution hors ligne des quatre suites de vecteurs tiers (`RFC 8785`, `NIST ACVP FIPS 204/205`, `a2aproject/a2a-tck 1.0.0.alpha3` et `OWASP SRC-055 L+`), élimine le risque d'auto-validation circulaire intra-essaim. De même, les recollations à l'aveugle `G3` garantissent une couverture équilibrée de `60` énoncés répartis en quatre strates de `15` items (`empiriques`, `juridiques`, `spécifications techniques datées` et `assertions CI G0`) avec un plancher de huit affirmations vérifiées par unité narrative.

Les deux annexes demeurent régénérées mécaniquement depuis les registres JSON SSOT, le rapport `aq/rapports-g0.json` et les journaux d'assurance qualité `G2`–`G5`, interdisant toute divergence entre les chiffres annoncés dans les chapitres, les résultats exécutés dans `8 - Trousse/` et les éditions assemblées finale Markdown, HTML autonome et PDF Typst (`6,14 × 9,21 po` à `10,6 pt`).

## Catalogue des quatre suites officielles de vecteurs tiers

L'intégrité hors ligne de chaque vecteur est contrôlée par `execute_g0.py` contre `8 - Trousse/vectors/vectors-manifest.json` avant toute exécution de test :

1. **`RFC 8785` (`JCS`)** : vecteurs de canonisation IEEE-754 ECMAScript et tri UTF-16 (`Appendices A/B` et `cyberphone/json-canonicalization`) face à `harness_proto/jcs.py`.
2. **`NIST FIPS 204 / 205` (`ACVP`)** : jeux officiels `usnistgov/ACVP-Server` pour `ML-DSA-65`, `ML-DSA-87` et `SLH-DSA-SHA2-128s/128f` face à `authz_pqc_audit/`.
3. **`a2aproject/a2a-tck` (`1.0.0.alpha3`)** : cas de conformité `AgentCard`, signatures `JWS` sur `JCS` et invariants obligatoires `MUST` pour `A2A v1.0.1`.
4. **`OWASP SRC-055` (`L+`)** : cartographie ouverte des dix menaces agentiques `ASI01`–`ASI10` (hors `genai.owasp.org`, bloqué `HTTP 403` `statut F` sous `AO-01`).

La synthèse détaillée de chaque exigence mappée et des empreintes `CA-G0-SYNC` est archivée dans le bloc structuré final afin de préserver la concision de la lecture principale.

## Règles de validation finale avant clôture

Aucune publication n'est acceptée tant que `execute_g0.py` ne retourne pas `0` et que `verifie_manuscrit.py --strict --check-deliverables` ne valide pas simultanément les vingt critères d'acceptation (`CA-01` à `CA-20`), incluant la présence d'un unique fichier HTML autonome dans `livrables/`, l'intégrité des éditions consolidées à la racine de `0 - PDF-MD/` et l'inspection visuelle de `100 %` des pages rendues consignée dans `aq/rapport-lissage-et-visuel.md`.

## Gouvernance des vingt-quatre portes `PRR` et des cinq `SBB`

La matrice de traçabilité `matrice-exig-prr-c40.json` relie chaque exigence opérationnelle de la famille `EXIG-*`, les vingt-quatre portes bloquantes de mise en production (`PRR-75`) ainsi que la fiche architecturale bloquante `2027-B001` à au moins un symbole exécutable et un nœud de test vérifié en barrière `G0`. L'objectif de cette liaison stricte consiste à supprimer toute prescription déclarative dépourvue de mécanisme d'essai : aucun principe architectural ne figure dans la matrice sans correspondance directe dans `8 - Trousse/` ni ancrage explicite vers le corpus de référence.

En parallèle, la correspondance avec les cinq blocs fonctionnels normalisés (`5 SBB`, Tableau 12 du cadre de référence) et les trois plans types `C01` à `C40` garantit que les quatre couches d'exécution — harnais typé, identité et couloir probatoire, politiques hors modèle avec sémantique Saga et banc statistique `EvalOps` — couvrent l'ensemble de la surface de contrôle sans zone grise.

## Protocoles statistiques `G3`, critique `G4` et lissage `G5`

Les deux passes de recollation à froid `G3` s'appuient sur des graines pseudo-aléatoires distinctes et des sélections disjointes afin d'éviter qu'un même énoncé ne soit réexaminé par inertie. Chaque échantillon de soixante vérifications équilibre quinze assertions empiriques, quinze renvois juridiques, quinze spécifications datées et quinze assertions logicielles extraites des rapports `G0`, tout en garantissant au minimum huit contrôles sur chacune des cinq unités narratives.

À l'étape `G4`, la boucle adversariale compare les chapitres du manuscrit contre les étalons stylistiques du corpus de façon anonyme afin d'élever la densité technique et la fluidité du français canadien sans altérer les faits vérifiés. Tout ajustement rédactionnel validé en `G4` ou lors du lissage transversal `G5` déclenche un rejeu différentiel complet de `G0`, `G1` et `G2` avant que le liseur final ne scelle l'ensemble documentaire.

## Intégrité visuelle, portabilité multi-plateforme et archivage

L'assemblage final génère simultanément l'édition Markdown consolidée, la page HTML autonome et le volume PDF mis en page par `Typst` sans coupure de tableau orpheline, ni débordement de code, ni figure tronquée. Les scripts d'outillage normalisent les fins de lignes Unix (`LF`) avant le calcul de chaque empreinte `SHA-256` et résolvent les binaires de vérification dans l'environnement épinglé de `8 - Trousse/` afin qu'un audit tiers puisse rejouer intégralement la validation hors ligne avec un résultat strictement identique.

<!-- BIBLIOGRAPHIE_BRUTE_DEBUT -->
## Matrice détaillée `EXIG` / `PRR` / `C01–C40` / `5 SBB`

- `S-01` (`PRR_BLOCKING`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.obo_dpop.validate_obo_delegation` | test `tests/test_authz_pqc_audit.py::test_nhi_unique_identity_required` | ancre `3 - Compendium 2027.md L28464 (SRC-046, SRC-047)`.
- `S-03` (`PRR_BLOCKING`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.obo_dpop.extract_act_chain` | test `tests/test_authz_pqc_audit.py::test_obo_sub_and_act_chain_max_two_hops` | ancre `3 - Compendium 2027.md L28466 (RFC 8693, SRC-041)`.
- `S-06` (`PRR_BLOCKING`, `BLOQUANT`, `ch03`) -> `policies_opa.opa_runner.OpaPolicyEngine.evaluate` | test `tests/test_policy_saga.py::test_rule_of_two_interface_vs_write_separation` | ancre `3 - Compendium 2027.md L28469 (EXIG-SEC-06, SRC-007)`.
- `S-08` (`PRR_BLOCKING`, `BLOQUANT`, `ch03`) -> `policy_saga.taint_camel.delegate_taint_envelope` | test `tests/test_policy_saga.py::test_camel_taint_propagation_across_agents` | ancre `3 - Compendium 2027.md L28471 (ASI01, SRC-055, SRC-056)`.
- `S-09` (`PRR_BLOCKING`, `BLOQUANT`, `ch03`) -> `policies_opa.opa_runner.verify_rego_default_deny` | test `tests/test_policy_saga.py::test_opa_default_deny_before_mutative_tool` | ancre `3 - Compendium 2027.md L28472 (SRC-087, SRC-088)`.
- `S-11` (`PRR_BLOCKING`, `BLOQUANT`, `ch03`) -> `policy_saga.sandbox_manifest.validate_sandbox_manifest` | test `tests/test_policy_saga.py::test_sandbox_manifest_no_kvm_enforced` | ancre `3 - Compendium 2027.md L28474 (EXIG-SEC-12..14, SRC-055)`.
- `S-14` (`PRR_BLOCKING`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.revocation_fsm.RevocationStateMachine` | test `tests/test_authz_pqc_audit.py::test_soc_killswitch_caep_revocation_terminal` | ancre `3 - Compendium 2027.md L28477 (SSF/CAEP SRC-019, SRC-020)`.
- `S-15` (`PRR_BLOCKING`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.ciba_approval.verify_ciba_approval_tokens` | test `tests/test_authz_pqc_audit.py::test_reject_self_approval_by_principal_sub` | ancre `3 - Compendium 2027.md L28478 (CIBA SRC-045, SRC-004)`.
- `R-01` (`PRR_BLOCKING`, `BLOQUANT`, `ch01`) -> `harness_proto.pipeline.DeterministicHarness.run` | test `tests/test_harness_proto.py::test_harness_enforces_schema_and_grounding` | ancre `3 - Compendium 2027.md L28484 (JSON Schema 2020-12 SRC-021)`.
- `R-03` (`PRR_BLOCKING`, `BLOQUANT`, `ch03`) -> `policy_saga.saga_orchestrator.compute_idempotency_key` | test `tests/test_saga_10_faults.py::test_fault_03_lost_response_idempotent_replay` | ancre `3 - Compendium 2027.md L28486 (Draft Idempotency-Key SRC-036)`.
- `R-06` (`PRR_BLOCKING`, `BLOQUANT`, `ch03`) -> `policy_saga.saga_orchestrator.SagaOrchestrator` | test `tests/test_saga_10_faults.py::test_fault_01_step_t2_compensates_c1` | ancre `3 - Compendium 2027.md L28489 (SagaLLM SRC-006, SRC-033)`.
- `R-07` (`PRR_BLOCKING`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.ciba_approval.compute_action_hash_h` | test `tests/test_authz_pqc_audit.py::test_ciba_c6_action_hash_exact_match` | ancre `3 - Compendium 2027.md L28490 (2 - Cadre de Référence.md L7300-L7310)`.
- `R-14` (`PRR_BLOCKING`, `BLOQUANT`, `ch03`) -> `policy_saga.taint_camel.SessionTaintTracker` | test `tests/test_policy_saga.py::test_multitenant_context_taint_isolation` | ancre `3 - Compendium 2027.md L28497 (SRC-056)`.
- `O-02` (`PRR_BLOCKING`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.otel_pii_mapper.redact_pii_bilingual` | test `tests/test_authz_pqc_audit.py::test_pii_redaction_bilingual_and_drop_raw_content` | ancre `3 - Compendium 2027.md L28505 (EXIG-OBS-07/09, LQ-2021-C25 SRC-063)`.
- `O-09` (`PRR_BLOCKING`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.audit_scitt_focus.compute_cpo_and_focus` | test `tests/test_authz_pqc_audit.py::test_focus_cpo_and_budget_ceiling_decimal` | ancre `3 - Compendium 2027.md L28512 (FOCUS v1.4 SRC-023)`.
- `G-01` (`PRR_BLOCKING`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_adr_2027_b001` | test `tests/test_evalops_prr.py::test_adr_2027_b001_requires_agent_owner` | ancre `3 - Compendium 2027.md L28524 (2027-B001)`.
- `G-03` (`PRR_BLOCKING`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_adr_2027_b001` | test `tests/test_evalops_prr.py::test_adr_2027_b001_regulatory_footprint` | ancre `3 - Compendium 2027.md L28526 (SRC-060, SRC-063, SRC-065)`.
- `G-05` (`PRR_BLOCKING`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_prr_24_blocking` | test `tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete` | ancre `3 - Compendium 2027.md L28528 (LQ-2021-C25, CAI 2026 SRC-064)`.
- `G-06` (`PRR_BLOCKING`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_prr_24_blocking` | test `tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete` | ancre `3 - Compendium 2027.md L28529 (Loi 25 art. 12.1 SRC-063)`.
- `G-07` (`PRR_BLOCKING`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_prr_24_blocking` | test `tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete` | ancre `3 - Compendium 2027.md L28530 (EU AI Act art. 50 SRC-060, SRC-061)`.
- `G-10` (`PRR_BLOCKING`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_prr_24_blocking` | test `tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete` | ancre `3 - Compendium 2027.md L28533 (LQ-2021-C25 / RGPD SRC-063)`.
- `G-15` (`PRR_BLOCKING`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.audit_scitt_focus.AuditChainLedger` | test `tests/test_authz_pqc_audit.py::test_audit_chain_jcs_and_scitt_merkle_seal` | ancre `3 - Compendium 2027.md L28538 (RFC 9943 SRC-044, FIPS 205 SRC-018)`.
- `F-04` (`PRR_BLOCKING`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_prr_24_blocking` | test `tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete` | ancre `3 - Compendium 2027.md L28547 (BSIF / Loi sur les banques SRC-070)`.
- `F-14` (`PRR_BLOCKING`, `BLOQUANT`, `ch03`) -> `policies_opa.opa_runner.OpaPolicyEngine.evaluate` | test `tests/test_policy_saga.py::test_sre_confinement_read_only_no_shell` | ancre `3 - Compendium 2027.md L28557 (SRC-087)`.
- `SBB-SECRETS-VAULT` (`SBB`, `OBLIGATOIRE`, `ch02`) -> `authz_pqc_audit.obo_dpop.validate_obo_delegation` | test `tests/test_authz_pqc_audit.py::test_no_static_secret_or_passthrough` | ancre `2 - Cadre de Référence.md L1360 (Plan A)`.
- `SBB-GUARDRAILS-ENGINE` (`SBB`, `BLOQUANT`, `ch03`) -> `policies_opa.opa_runner.OpaPolicyEngine` | test `tests/test_policy_saga.py::test_opa_coverage_100_percent` | ancre `2 - Cadre de Référence.md L1360 (Plan A, SRC-087)`.
- `SBB-SIGNED-HUMAN-APPROVAL` (`SBB`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.ciba_approval.verify_ciba_approval_tokens` | test `tests/test_authz_pqc_audit.py::test_ciba_approval_token_valid_and_single_use` | ancre `2 - Cadre de Référence.md L1360 (Plan A, SRC-045)`.
- `SBB-IMMUTABLE-AUDIT-LEDGER` (`SBB`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.audit_scitt_focus.AuditChainLedger` | test `tests/test_authz_pqc_audit.py::test_audit_chain_tamper_detection` | ancre `2 - Cadre de Référence.md L1361 (Plan B, SRC-044)`.
- `SBB-FINOPS-BUDGET-QUOTA` (`SBB`, `BLOQUANT`, `ch03`) -> `policy_saga.decimal_money.from_decimal_str` | test `tests/test_policy_saga.py::test_decimal_rejects_float_budget` | ancre `2 - Cadre de Référence.md L1361 (Plan B, FOCUS SRC-023)`.
- `2027-B001` (`ADR_TEMPLATE`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_adr_2027_b001` | test `tests/test_evalops_prr.py::test_adr_2027_b001_schema_validation` | ancre `3 - Compendium 2027.md L28423-L28448 (schemas/adr_2027_b001.schema.json)`.
- `CAP-046` (`CAP`, `RECOMMANDE`, `ch02`) -> `authz_pqc_audit.audit_scitt_focus.compute_cpo_and_focus` | test `tests/test_authz_pqc_audit.py::test_focus_carbon_cap046_fields` | ancre `4 - Plan Directeur.md L2559; 5 - Memoire.md L1797 (FOCUS v1.4 SRC-023)`.
- `EXIG-MCP-03` (`EXIG`, `OBLIGATOIRE`, `ch01`) -> `harness_proto.mcp_pinning.verify_tools_list_against_catalog` | test `tests/test_harness_proto.py::test_mcp_tools_list_deterministic_sort_and_cache` | ancre `2 - Cadre de Référence.md L7537 (MCP 2026-07-28 SRC-072)`.
- `EXIG-MCP-11` (`EXIG`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.obo_dpop.validate_obo_delegation` | test `tests/test_authz_pqc_audit.py::test_reject_token_passthrough` | ancre `2 - Cadre de Référence.md L7545 (MCP Auth SRC-078)`.
- `EXIG-MCP-15` (`EXIG`, `BLOQUANT`, `ch01`) -> `harness_proto.mcp_pinning.validate_mcp_headers` | test `tests/test_harness_proto.py::test_mcp_header_mismatch_raises_400_32020` | ancre `2 - Cadre de Référence.md L2025, L7549 (MCP 2026-07-28 SRC-074)`.
- `EXIG-MCP-16` (`EXIG`, `OBLIGATOIRE`, `ch01`) -> `harness_proto.mcp_pinning.validate_mcp_headers` | test `tests/test_harness_proto.py::test_mcp_meta_allowlist_purges_unreserved` | ancre `2 - Cadre de Référence.md L2038, L7550 (MCP 2026-07-28 SRC-080)`.
- `EXIG-MCP-18` (`EXIG`, `BLOQUANT`, `ch01`) -> `harness_proto.mcp_pinning.validate_mcp_headers` | test `tests/test_harness_proto.py::test_reject_x_mcp_header_pii_or_token` | ancre `2 - Cadre de Référence.md L2052, L7552 (MCP 2026-07-28 SRC-078)`.
- `EXIG-MCP-19` (`EXIG`, `BLOQUANT`, `ch01`) -> `harness_proto.pipeline.validate_strict_schema` | test `tests/test_harness_proto.py::test_reject_external_network_schema_ref` | ancre `2 - Cadre de Référence.md L2062, L7553 (JSON Schema 2020-12 SRC-021)`.
- `EXIG-MCP-20` (`EXIG`, `BLOQUANT`, `ch01`) -> `harness_proto.mcp_pinning.compute_tool_definition_digest` | test `tests/test_harness_proto.py::test_mcp_rug_pull_single_char_drift_suspends` | ancre `2 - Cadre de Référence.md L2074, L7554 (Silent Drift 40,58 % SRC-057)`.
- `EXIG-A2A-03` (`EXIG`, `BLOQUANT`, `ch01`) -> `harness_proto.a2a_card.validate_agent_card` | test `tests/test_harness_proto.py::test_a2a_agent_card_jws_es256_and_pinned_jku` | ancre `2 - Cadre de Référence.md L7559 (A2A v1.0.1 SRC-083, a2a-tck SRC-086)`.
- `EXIG-OBS-06` (`EXIG`, `OBLIGATOIRE`, `ch02`) -> `authz_pqc_audit.otel_pii_mapper.map_span_attributes` | test `tests/test_authz_pqc_audit.py::test_otel_rejects_generic_enterprise_prefix` | ancre `2 - Cadre de Référence.md L7701 (OTel v1.41.0 SRC-089)`.
- `EXIG-OBS-07` (`EXIG`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.otel_pii_mapper.map_span_attributes` | test `tests/test_authz_pqc_audit.py::test_otel_drops_raw_prompt_and_tool_payloads` | ancre `2 - Cadre de Référence.md L7702 (OTel genai SRC-090)`.
- `EXIG-OBS-09` (`EXIG`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.otel_pii_mapper.redact_pii_bilingual` | test `tests/test_authz_pqc_audit.py::test_otel_pii_redaction_and_closed_allowlist` | ancre `2 - Cadre de Référence.md L7704 (LQ-2021-C25 SRC-063)`.
- `EXIG-OBS-12` (`EXIG`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.audit_scitt_focus.AuditChainLedger.append_record` | test `tests/test_authz_pqc_audit.py::test_c8_five_element_canonized_record` | ancre `2 - Cadre de Référence.md L7707 (C.8, RFC 8785 SRC-077, RFC 9943 SRC-044)`.
- `EXIG-SEC-06` (`EXIG`, `BLOQUANT`, `ch03`) -> `policies_opa.opa_runner.OpaPolicyEngine.evaluate` | test `tests/test_policy_saga.py::test_rule_of_two_denies_untrusted_plus_exfiltration` | ancre `2 - Cadre de Référence.md L7673 (CaMeL SRC-007, SRC-056, OWASP SRC-055)`.
- `EXIG-SEC-12` (`EXIG`, `BLOQUANT`, `ch03`) -> `policy_saga.sandbox_manifest.validate_sandbox_manifest` | test `tests/test_policy_saga.py::test_sandbox_denies_egress_and_iana_ranges` | ancre `2 - Cadre de Référence.md L7679 (OPA v1.22.4 SRC-087)`.
- `EXIG-SEC-13` (`EXIG`, `BLOQUANT`, `ch03`) -> `policy_saga.sandbox_manifest.validate_sandbox_manifest` | test `tests/test_policy_saga.py::test_sandbox_blocks_imds_169_254_169_254` | ancre `2 - Cadre de Référence.md L7680 (WIMSE SRC-047)`.
- `EXIG-SEC-14` (`EXIG`, `BLOQUANT`, `ch03`) -> `policy_saga.sandbox_manifest.validate_sandbox_manifest` | test `tests/test_policy_saga.py::test_sandbox_rejects_env_secrets` | ancre `2 - Cadre de Référence.md L7681 (OWASP ASI03 SRC-055)`.
- `EXIG-SEC-15` (`EXIG`, `OBLIGATOIRE`, `ch03`) -> `policy_saga.sandbox_manifest.validate_sandbox_manifest` | test `tests/test_policy_saga.py::test_sandbox_three_level_timeouts` | ancre `2 - Cadre de Référence.md L7682 (30s / 1200s / 3600s)`.
- `EXIG-SEC-24` (`EXIG`, `BLOQUANT`, `ch04`) -> `evalops_prr.metamorphic.verify_metamorphic_pair` | test `tests/test_evalops_prr.py::test_bilingual_fr_en_attack_suite_100_cases` | ancre `2 - Cadre de Référence.md L7691 (OWASP SRC-055, MORTAR SRC-092)`.
- `EXIG-SEC-25` (`EXIG`, `BLOQUANT`, `ch03`) -> `policies_opa.opa_runner.OpaPolicyEngine.run_coverage` | test `tests/test_policy_saga.py::test_deterministic_controls_opa_100_coverage` | ancre `2 - Cadre de Référence.md L7692 (OPA testing SRC-088)`.
- `EXIG-ORC-18` (`EXIG`, `BLOQUANT`, `ch03`) -> `policy_saga.saga_orchestrator.SagaOrchestrator` | test `tests/test_saga_10_faults.py::test_fault_08_two_comp_failures_escalate` | ancre `2 - Cadre de Référence.md L7611 (SagaLLM SRC-006)`.
- `EXIG-ORC-20` (`EXIG`, `BLOQUANT`, `ch03`) -> `policy_saga.saga_orchestrator.SagaOrchestrator` | test `tests/test_saga_10_faults.py::test_saga_all_10_deterministic_faults` | ancre `2 - Cadre de Référence.md L7613 (10 scénarios d'injection de fautes)`.
- `EXIG-ORC-28` (`EXIG`, `BLOQUANT`, `ch03`) -> `policy_saga.saga_orchestrator.CompensationChannel` | test `tests/test_saga_10_faults.py::test_fault_10_isolated_compensation_channel` | ancre `2 - Cadre de Référence.md L7621 (Canal de compensation isolé)`.
- `EXIG-EVA-03` (`EXIG`, `BLOQUANT`, `ch04`) -> `evalops_prr.wilson_bounds.evaluate_wilson_gate` | test `tests/test_evalops_prr.py::test_wilson_3p_independent_scenarios_gate` | ancre `2 - Cadre de Référence.md L5041, L7711 (NIST 7.2.4.1 SRC-022)`.
- `EXIG-AMF-11` (`EXIG`, `OBLIGATOIRE`, `ch04`) -> `evalops_prr.metamorphic.verify_metamorphic_pair` | test `tests/test_evalops_prr.py::test_bilingual_fr_en_fairness_and_non_avis_gate` | ancre `2 - Cadre de Référence.md L7785 (AIBanks.ca SRC-071; portail AMF en statut F)`.
- `C01` (`C40`, `OBLIGATOIRE`, `ch01`) -> `harness_proto.pipeline.DeterministicHarness` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5007 (Tri L0-L4)`.
- `C02` (`C40`, `OBLIGATOIRE`, `ch04`) -> `evalops_prr.prr_validators.validate_blueprints_and_c40` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5008 (DISC-04)`.
- `C03` (`C40`, `BLOQUANT`, `ch03`) -> `policies_opa.opa_runner.OpaPolicyEngine` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5009 (DISC-03)`.
- `C04` (`C40`, `RECOMMANDE`, `ch04`) -> `evalops_prr.prr_validators.validate_blueprints_and_c40` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5010`.
- `C05` (`C40`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_adr_2027_b001` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5011 (Agent Owner / DISC-02)`.
- `C06` (`C40`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_prr_24_blocking` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5012 (3LoD / BSIF E-23 SRC-065)`.
- `C07` (`C40`, `RECOMMANDE`, `ch01`) -> `harness_proto.pipeline.DeterministicHarness.run` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5013`.
- `C08` (`C40`, `RECOMMANDE`, `ch04`) -> `evalops_prr.prr_validators.validate_blueprints_and_c40` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5014`.
- `C09` (`C40`, `BLOQUANT`, `ch01`) -> `harness_proto.pipeline.DeterministicHarness.run` | test `tests/test_harness_proto.py::test_harness_partition_80_20_rules_outside_prompt` | ancre `6 - Livre Blanc.md L5015 (Partition 80/20)`.
- `C10` (`C40`, `BLOQUANT`, `ch01`) -> `harness_proto.pipeline.validate_strict_schema` | test `tests/test_harness_proto.py::test_strict_json_schema_2020_12` | ancre `6 - Livre Blanc.md L5016 (SRC-021)`.
- `C11` (`C40`, `BLOQUANT`, `ch01`) -> `harness_proto.mcp_pinning.StreamableHttpAdapter` | test `tests/test_harness_proto.py::test_mcp_streamable_http_and_pinning` | ancre `6 - Livre Blanc.md L5017 (MCP 2026-07-28 SRC-074)`.
- `C12` (`C40`, `OBLIGATOIRE`, `ch01`) -> `harness_proto.mcp_pinning.verify_tools_list_against_catalog` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5018`.
- `C13` (`C40`, `BLOQUANT`, `ch01`) -> `harness_proto.a2a_card.validate_agent_card` | test `tests/test_harness_proto.py::test_a2a_agent_card_jws_es256_and_pinned_jku` | ancre `6 - Livre Blanc.md L5019 (A2A v1.0.1 SRC-083)`.
- `C14` (`C40`, `RECOMMANDE`, `ch01`) -> `harness_proto.a2a_card.validate_agent_card` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5020`.
- `C15` (`C40`, `OBLIGATOIRE`, `ch03`) -> `policy_saga.taint_camel.SessionTaintTracker` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5021 (CoALA SRC-026)`.
- `C16` (`C40`, `BLOQUANT`, `ch03`) -> `policies_opa.opa_runner.OpaPolicyEngine.evaluate` | test `tests/test_policy_saga.py::test_acl_and_asi06_memory_protection` | ancre `6 - Livre Blanc.md L5022 (ASI06 SRC-055)`.
- `C17` (`C40`, `RECOMMANDE`, `ch04`) -> `evalops_prr.mock_mcp_harness.evaluate_trajectory` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5023 (Kim et al. SRC-003)`.
- `C18` (`C40`, `OBLIGATOIRE`, `ch03`) -> `policy_saga.sandbox_manifest.validate_sandbox_manifest` | test `tests/test_policy_saga.py::test_sandbox_three_level_timeouts` | ancre `6 - Livre Blanc.md L5024`.
- `C19` (`C40`, `OBLIGATOIRE`, `ch01`) -> `harness_proto.pipeline.DeterministicHarness.run` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5025`.
- `C20` (`C40`, `OBLIGATOIRE`, `ch02`) -> `authz_pqc_audit.audit_scitt_focus.AuditChainLedger` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5026 (CloudEvents 1.0.2 SRC-035)`.
- `C21` (`C40`, `OBLIGATOIRE`, `ch03`) -> `policy_saga.saga_orchestrator.SagaOrchestrator` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5027`.
- `C22` (`C40`, `BLOQUANT`, `ch03`) -> `policy_saga.saga_orchestrator.SagaOrchestrator` | test `tests/test_saga_10_faults.py::test_fault_02_crash_after_outbox_resumes` | ancre `6 - Livre Blanc.md L5028 (Temporal/Durable SRC-034)`.
- `C23` (`C40`, `BLOQUANT`, `ch03`) -> `policy_saga.saga_orchestrator.compute_idempotency_key` | test `tests/test_saga_10_faults.py::test_fault_06_pivot_blocks_backward_compensation` | ancre `6 - Livre Blanc.md L5029 (Saga SRC-006, SRC-036)`.
- `C24` (`C40`, `OBLIGATOIRE`, `ch02`) -> `authz_pqc_audit.ciba_approval.verify_ciba_approval_tokens` | test `tests/test_authz_pqc_audit.py::test_ciba_approval_token_valid_and_single_use` | ancre `6 - Livre Blanc.md L5030 (CIBA SRC-045)`.
- `C25` (`C40`, `BLOQUANT`, `ch03`) -> `policies_opa.taint_camel.delegate_taint_envelope` | test `tests/test_policy_saga.py::test_camel_taint_propagation_across_agents` | ancre `6 - Livre Blanc.md L5031 (OWASP SRC-055, CaMeL SRC-007, SRC-056)`.
- `C26` (`C40`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.revocation_fsm.RevocationStateMachine` | test `tests/test_authz_pqc_audit.py::test_spiffe_nhi_lifecycle_and_revocation` | ancre `6 - Livre Blanc.md L5032 (SPIFFE SRC-046, WIMSE SRC-047)`.
- `C27` (`C40`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.pqc_http431.evaluate_http_431` | test `tests/test_authz_pqc_audit.py::test_pqc_http431_vs_transaction_token_o1` | ancre `6 - Livre Blanc.md L5033 (RFC 8693/8707/9449, Txn-Tokens SRC-013)`.
- `C28` (`C40`, `BLOQUANT`, `ch03`) -> `policies_opa.opa_runner.OpaPolicyEngine.evaluate` | test `tests/test_policy_saga.py::test_opa_rule_of_two_and_rar_mandate` | ancre `6 - Livre Blanc.md L5034 (OPA SRC-087, RAR RFC 9396 SRC-042)`.
- `C29` (`C40`, `BLOQUANT`, `ch03`) -> `policy_saga.sandbox_manifest.validate_sandbox_manifest` | test `tests/test_policy_saga.py::test_sandbox_manifest_no_kvm_enforced` | ancre `6 - Livre Blanc.md L5035`.
- `C30` (`C40`, `OBLIGATOIRE`, `ch02`) -> `authz_pqc_audit.otel_pii_mapper.map_span_attributes` | test `tests/test_authz_pqc_audit.py::test_otel_v141_to_genai_dev_cache_write_and_join` | ancre `6 - Livre Blanc.md L5036 (OTel v1.41.0 SRC-089, GenAI SRC-090)`.
- `C31` (`C40`, `BLOQUANT`, `ch04`) -> `evalops_prr.mock_mcp_harness.compute_pass_k` | test `tests/test_evalops_prr.py::test_mock_mcp_pass_k_consistency_gate` | ancre `6 - Livre Blanc.md L5037 (tau-bench SRC-029)`.
- `C32` (`C40`, `OBLIGATOIRE`, `ch04`) -> `evalops_prr.prr_validators.validate_blueprints_and_c40` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5038`.
- `C33` (`C40`, `RECOMMANDE`, `ch04`) -> `evalops_prr.prr_validators.validate_blueprints_and_c40` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5039`.
- `C34` (`C40`, `OBLIGATOIRE`, `ch01`) -> `harness_proto.pipeline.DeterministicHarness.run` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5040`.
- `C35` (`C40`, `OBLIGATOIRE`, `ch04`) -> `evalops_prr.prr_validators.validate_adr_2027_b001` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5041`.
- `C36` (`C40`, `OBLIGATOIRE`, `ch04`) -> `evalops_prr.prr_validators.validate_blueprints_and_c40` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5042`.
- `C37` (`C40`, `BLOQUANT`, `ch04`) -> `evalops_prr.prr_validators.validate_prr_24_blocking` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5043 (Loi 25 SRC-063, EU AI Act SRC-060, EN 18286 SRC-067)`.
- `C38` (`C40`, `BLOQUANT`, `ch02`) -> `authz_pqc_audit.audit_scitt_focus.seal_merkle_root` | test `tests/test_authz_pqc_audit.py::test_scitt_merkle_inclusion_and_slh_dsa_seal` | ancre `6 - Livre Blanc.md L5044 (SCITT SRC-044, FIPS 205 SRC-018)`.
- `C39` (`C40`, `OBLIGATOIRE`, `ch02`) -> `authz_pqc_audit.audit_scitt_focus.compute_cpo_and_focus` | test `tests/test_authz_pqc_audit.py::test_focus_cpo_and_budget_ceiling_decimal` | ancre `6 - Livre Blanc.md L5045 (FOCUS v1.4 SRC-023)`.
- `C40` (`C40`, `RECOMMANDE`, `ch04`) -> `evalops_prr.prr_validators.validate_blueprints_and_c40` | test `tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40` | ancre `6 - Livre Blanc.md L5046`.

## Catalogue vérifié des extraits `CA-G0-SYNC`

- `G0-EX-CH01-01` (`ch01`) : `8 - Trousse/schemas/harness_extraction.schema.json` L1-24 (24 L) — `SHA-256: 6b4428a1f8a6abcd2029280cded86b0e983ddb349d0f05c6ba0192c010f95aac`.
- `G0-EX-CH01-02` (`ch01`) : `8 - Trousse/harness_proto/pipeline.py` L204-232 (29 L) — `SHA-256: 75110799d751ee4b93c58c7aff4e2b6ce0c2c8d29c50b6d1668b4bf895dfc275`.
- `G0-EX-CH01-03` (`ch01`) : `8 - Trousse/harness_proto/mcp_pinning.py` L227-260 (34 L) — `SHA-256: 350e1959e6f0c54ce549afc77b4ef14959851bc9e45ad1a2eee52b9b36f4fc95`.
- `G0-EX-CH01-04` (`ch01`) : `8 - Trousse/harness_proto/a2a_card.py` L157-182 (26 L) — `SHA-256: 1a58d5eabab4361028420c902df71ef3b305f84bfd139e14c75c7318c545b899`.
- `G0-EX-CH02-01` (`ch02`) : `8 - Trousse/authz_pqc_audit/obo_dpop.py` L85-114 (30 L) — `SHA-256: d3c2d0ce031a283ba8b3e85fc230c51f6fa036a46942a573dfd77351922d2991`.
- `G0-EX-CH02-02` (`ch02`) : `8 - Trousse/authz_pqc_audit/ciba_approval.py` L106-117 (12 L) — `SHA-256: 423ebd61ce4996bf314c2fcecab18e48129d46e379a70eaf57780b5e1e395307`.
- `G0-EX-CH02-03` (`ch02`) : `8 - Trousse/authz_pqc_audit/pqc_http431.py` L149-177 (29 L) — `SHA-256: c5c72e27a3932180e70ba9ebd63c109c5cc146c3af50d1327aed293f0e614855`.
- `G0-EX-CH02-04` (`ch02`) : `8 - Trousse/authz_pqc_audit/otel_pii_mapper.py` L235-265 (31 L) — `SHA-256: 60bd160c1a507c6df31fd1dfc3811c866a6f17e8b623e961b2511c00c7e41889`.
- `G0-EX-CH03-01` (`ch03`) : `8 - Trousse/policies_opa/rule_of_two.rego` L3-26 (24 L) — `SHA-256: c0adc5553c040a592151fbcff54a27e85412764f82815220c5297e79ba652036`.
- `G0-EX-CH03-02` (`ch03`) : `8 - Trousse/policies_opa/camel_taint.rego` L3-25 (23 L) — `SHA-256: bd873cf677b35787f6054b97b6a2de30c0cb7c6a5a52375c8bce7275ab03637b`.
- `G0-EX-CH03-03` (`ch03`) : `8 - Trousse/policy_saga/saga_orchestrator.py` L107-140 (34 L) — `SHA-256: a2aac944f6ae06fe63c2f6482618bae3356d6270f3c5f6a3756c8592ebd1a536`.
- `G0-EX-CH04-01` (`ch04`) : `8 - Trousse/evalops_prr/wilson_bounds.py` L43-70 (28 L) — `SHA-256: 3e685cbef8dea03f3c2c217d37c25e292295858505eae0769706570955f913ba`.
- `G0-EX-CH04-02` (`ch04`) : `8 - Trousse/evalops_prr/metamorphic.py` L38-63 (26 L) — `SHA-256: 31ad0df04f1930471a8cec511d897834f72c35851e98f9c7cae1aa82002c1472`.
- `G0-EX-CH04-03` (`ch04`) : `8 - Trousse/schemas/adr_2027_b001.schema.json` L1-32 (32 L) — `SHA-256: 4f0a41e7280851ce1413efeb6accb3632bb3ee6a0bfefc4fa7d92338156e36ae`.
<!-- BIBLIOGRAPHIE_BRUTE_FIN -->
