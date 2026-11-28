# Annexe D — Homologation exécutable G0–G5 des systèmes d'entreprise, matrice EXIG / CAP / PRR-75 / C01–C40 / 5 SBB, licences et statut non-avis

Cette annexe publie le bilan exécutable des barrières `G0`–`G5` appliquées à l'homologation des systèmes d'entreprise, la matrice unifiée de traçabilité (**95 liaisons exécutables `G0`** reliant `305 EXIG-*` — dont un tronc multisectoriel universel de `291` exigences incluant `87` exigences d'interopérabilité et `84` exigences d'encadrement d'automatisation — `52 CAP`, `24 PEX`, `PRR-75` dont `24` bloquantes, `C01–C40` et `5 SBB`), les extraits scellés `CA-G0-SYNC`, le catalogue des **57 spécifications ouvertes `L+`** et la clause `non-avis` (`AO-05`).

## 1. Bilan exécutable de la barrière logicielle `G0`

|Contrôle G0|Mesure vérifiée|Statut|
|---|---|---|
|Verdict `execute_g0.py`|Code `0` (`PASS`)|Conforme|
|Suite `pytest`|`83` passés, `0` échecs, `0` ignorés|Conforme|
|Politiques `OPA/Rego` (`policy_saga/opa_runner.py`)|Couverture `100,0 %`, `45` tests|Conforme|
|Audit `SPDX MIT`|`50` fichiers, `18` paquets vérifiés (`17` épinglés dans `requirements.lock`)|Conforme|
|Schémas JSON et Lockfile|`21` schémas, empreintes épinglées `True`|Conforme|
|Quatre vecteurs tiers|`4` suites, `14` extraits `CA-G0-SYNC`|Conforme|

*Tableau D.1 — Bilan exécutable de la barrière logicielle `G0` sur la trousse compagnon (`Tome 8`).*

Répartition `pytest` par module : `tests/test_authz_pqc_audit.py` (23), `tests/test_evalops_prr.py` (10), `tests/test_harness_proto.py` (14), `tests/test_policy_saga.py` (18), `tests/test_saga_10_faults.py` (11), `tests/test_third_party_vectors.py` (7). Note de concordance `requirements.lock` et `SPDX` : le fichier verrouillé `requirements.lock` épingle dix-sept paquets tiers avec empreintes `SHA-256` (vérifiés en Chapitre 35), tandis que le contrôle `SPDX MIT` couvre `18` paquets incluant le métapaquet de la trousse exécutable. Quatre suites de vecteurs tiers sont vérifiées : `a2a_tck` (PASS, `5` vecteurs), `nist_acvp` (PASS, `12` vecteurs), `owasp_src055` (PASS, `13` vecteurs), `rfc8785` (PASS, `20` vecteurs).

## 2. Clause `non-avis` et régime dual de licences (`CC-BY-4.0` / `MIT`)

Le présent traité *Interopérabilité et automatisation agentique des systèmes d'entreprise* et ses **139 schémas** sont diffusés sous licence **`CC-BY-4.0`**, tandis que l'outillage déterministe d'homologation et la trousse compagnon (`Tome 8`) relèvent de la licence **`MIT`**. Conformément au statut `non-avis` arrêté au 2 décembre 2026, l'ouvrage constitue une référence technique pédagogique couvrant l'ensemble des systèmes d'entreprise (`ERP`, `CRM`, `SIRH`, `ITSM`, `SCM`, cœurs transactionnels et interfaces `IT/OT`) ainsi que l'étalon prudentiel de haute régulation, mais ne tient lieu ni d'avis juridique, ni de certification réglementaire, ni d'homologation sur un système d'enregistrement ou d'exploitation réelle.

## 3. Inventaire des 14 extraits scellés `CA-G0-SYNC` (`CA-20`)

Les extraits de code publiés dans les chapitres sont vérifiés octet par octet contre la trousse exécutable : `G0-EX-CH01-01` (`ch04`, `schemas/harness_extraction.schema.json`, lignes `1-24`, `SHA-256` `6b4428a1f8a6`) ; `G0-EX-CH01-02` (`ch04`, `harness_proto/pipeline.py`, lignes `204-232`, `SHA-256` `75110799d751`) ; `G0-EX-CH01-03` (`ch07`, `harness_proto/mcp_pinning.py`, lignes `227-260`, `SHA-256` `350e1959e6f0`) ; `G0-EX-CH01-04` (`ch08`, `harness_proto/a2a_card.py`, lignes `157-182`, `SHA-256` `1a58d5eabab4`) ; `G0-EX-CH02-01` (`ch17`, `authz_pqc_audit/obo_dpop.py`, lignes `85-114`, `SHA-256` `d3c2d0ce031a`) ; `G0-EX-CH02-02` (`ch17`, `authz_pqc_audit/ciba_approval.py`, lignes `106-117`, `SHA-256` `423ebd61ce49`) ; `G0-EX-CH02-03` (`ch18`, `authz_pqc_audit/pqc_http431.py`, lignes `149-177`, `SHA-256` `c5c72e27a393`) ; `G0-EX-CH02-04` (`ch22`, `authz_pqc_audit/otel_pii_mapper.py`, lignes `235-265`, `SHA-256` `60bd160c1a50`) ; `G0-EX-CH03-01` (`ch20`, `policies_opa/rule_of_two.rego`, lignes `3-26`, `SHA-256` `c0adc5553c04`) ; `G0-EX-CH03-02` (`ch20`, `policies_opa/camel_taint.rego`, lignes `3-25`, `SHA-256` `bd873cf677b3`) ; `G0-EX-CH03-03` (`ch15`, `policy_saga/saga_orchestrator.py`, lignes `107-140`, `SHA-256` `a2aac944f6ae`) ; `G0-EX-CH04-01` (`ch35`, `evalops_prr/wilson_bounds.py`, lignes `43-70`, `SHA-256` `3e685cbef8de`) ; `G0-EX-CH04-02` (`ch23`, `evalops_prr/metamorphic.py`, lignes `38-63`, `SHA-256` `31ad0df04f19`) ; `G0-EX-CH04-03` (`ch34`, `schemas/adr_2027_b001.schema.json`, lignes `1-32`, `SHA-256` `4f0a41e72808`).

## 4. Ventilation du référentiel `CRE-IA-2026-01 v1.2` (`305` exigences)

Répartition par force normative : `DOIT` (255), `NE_DOIT_PAS` (34), `DEVRAIT` (16). Composition : 287 socle v1.1 + 12 EXIG-AMF (41 attentes Note AMF IA.pdf CRE-IA-2026-01-QC) + 6 ajouts PQC/ACVM/RTR/EN 18286.

Familles d'exigences : `EXIG-ARC` (25, Architecture de référence, Chapitre 5), `EXIG-INT` (23, Interopérabilité, contrats et catalogue d'entreprise, Sections 6.1–6.4, 6.8–6.9), `EXIG-MCP` (22, Model Context Protocol, Section 6.5), `EXIG-A2A` (15, Protocole Agent2Agent, Section 6.6), `EXIG-EVT` (10, Interopérabilité événementielle, Section 6.7), `EXIG-ORC` (30, Orchestration, Chapitre 7), `EXIG-AUT` (23, Autonomie et supervision humaine, Chapitre 8), `EXIG-IAM` (21, Confiance zéro, identité, délégation et passerelle d'agents, Sections 9.1–9.4), `EXIG-SEC` (28, Menaces propres aux agents et défenses, Sections 9.5–9.9), `EXIG-OBS` (13, Traçage et journal d'audit, Sections 10.1–10.3), `EXIG-EVA` (6, Évaluation continue, Section 10.4), `EXIG-FIN` (10, Économie de l'inférence et maîtrise des coûts, Sections 10.5–10.6), `EXIG-GOV` (20, Gouvernance et cycle de vie, Chapitre 11), `EXIG-CON` (30, Risques, conformité et réglementation, Chapitre 12 (sections 12.1–12.10)), `EXIG-AMF` (12, Profil québécois AMF IA et gestion du risque de modèle, Section 12.10), `EXIG-APP` (17, Approvisionnement et clauses contractuelles, Chapitre 13).

Dix interdictions absolues sans dérogation (`EXIG-GOV-17`) : 1. Autonomie non bornée de niveau NX interdite en tout temps (EXIG-AUT-03) ; 2. Exécution d'une action P3 sans approbation humaine hors bande liée (EXIG-AUT-09, EXIG-AUT-12, EXIG-AUT-13) ; 3. Usurpation par un agent de l'identité de son mandant humain (EXIG-IAM-08, EXIG-IAM-09) ; 4. Relais direct d'un jeton entrant vers un serveur ou pair aval (EXIG-IAM-12, EXIG-MCP-11) ; 5. Exploitation sans fiche complète au registre ou parrain nommé (EXIG-GOV-01, 02, 04, 05, 07..11, 13..15) ; 6. Dépassement du plafond d'autonomie fixé par la classe de risque (EXIG-AUT-01, EXIG-AUT-02, EXIG-CON-02) ; 7. Autorisation au-delà de N2 d'un agent atteignant les seuils de la règle d'or (EXIG-AUT-07) ; 8. Exposition à la triade létale sans retrait déterministe des outils sortants (EXIG-SEC-06) ; 9. Exploitation d'un agent sans journal d'audit distinct, chaîné et ancré (EXIG-OBS-11) ; 10. Manquement à une obligation légale ou réglementaire applicable dont Loi 25 art. 12.1 (EXIG-AUT-22..23, EXIG-CON-04..22).

## 5. Grille `PRR-75`, critères `C01–C40` (`18/15/7`), trois blueprints et cinq blocs `SBB`

La grille `PRR-75` rassemble **75 points de contrôle**, dont **24 bloquants**, **26 conditionnels** et **25 élevés ou moyens** (51 points non bloquants intégralement restitués en section 10). Les quarante critères `C01–C40` des trois blueprints se ventilent en **`18` `BLOQUANT`**, **`15` `OBLIGATOIRE`** et **`7` `RECOMMANDÉ`**. Par convention de désambiguïsation des notations `C*`, `C1–C5` désigne les cinq couches du modèle pivot (`PD28`), `C1–C6` les six couches sectorielles (`C26`), `C1–C8` les huit strates techniques des trois blueprints (`ch29`), `C01–C40` les quarante critères d'homologation et `C.1–C.8` les contrats de l'Annexe C du `Tome 8`.

Trois blueprints de référence déclinent `C01–C40` : `bp1_assistant_interne` (§29.1.2 (Tome 6 §14.1 : traitement transactionnel réglementé SoR)) ; `bp2_rag_entreprise_acl` (§29.1.3 (Tome 6 §14.3 : enclave souveraine, AI Gateway, RAG ACL, microVM)) ; `bp3_orchestration_multi_agents_b2b` (§29.1.4 (Tome 6 §14.2 : maillage inter-départemental & B2B A2A/AGNTCY/Event Mesh)). Cinq blocs logiciels (`SBB`) matérialisent les emplacements critiques : `SBB-SECRETS-VAULT` (`Plan A`, slot `secrets_vault`, module `authz_pqc_audit/obo_dpop.py`) ; `SBB-GUARDRAILS-ENGINE` (`Plan A`, slot `guardrails_engine`, module `policy_saga/opa_runner.py + policies_opa/rule_of_two.rego`) ; `SBB-SIGNED-HUMAN-APPROVAL` (`Plan A`, slot `signed_human_approval_service`, module `authz_pqc_audit/ciba_approval.py`) ; `SBB-IMMUTABLE-AUDIT-LEDGER` (`Plan B`, slot `immutable_audit_ledger`, module `authz_pqc_audit/audit_scitt_focus.py`) ; `SBB-FINOPS-BUDGET-QUOTA` (`Plan B`, slot `finops_budget_quota_controller`, module `policy_saga/decimal_money.py + audit_scitt_focus.py`).

Les vingt-quatre portes bloquantes exécutées en barrière `G0` couvrent : `S-01` (grille `S`, Identité NHI unique inscrite à l'annuaire d'entreprise (aucune clé API partagée)) ; `S-03` (grille `S`, Délégation OAuth 2.1 `On-Behalf-Of` (RFC 8693) préservant `sub` et la chaîne `act`) ; `S-06` (grille `S`, Séparation entre l'agent d'interface exposé et l'agent détenteur d'outils d'écriture) ; `S-08` (grille `S`, Marquage structurel des données externes non fiables contre l'injection indirecte (ASI01)) ; `S-09` (grille `S`, Évaluation déterministe hors LLM (Cedar ou OPA) devant chaque appel d'outil mutatif) ; `S-11` (grille `S`, Exécution de tout code ou script dynamique en bac à sable isolé (OpenSandbox/microVM)) ; `S-14` (grille `S`, Coupe-circuit centralisé du SOC, révoquant jetons et sessions en < 10 secondes) ; `S-15` (grille `S`, Validation de la séparation des tâches sur les flux financiers/sensibles) ; `R-01` (grille `R`, Inviolabilité des systèmes d'enregistrement (passage exclusif par des API/BAPI métiers validées)) ; `R-03` (grille `R`, Clé d'idempotence déterministe transmise et honorée sur chaque outil à effet de bord) ; `R-06` (grille `R`, Définition explicite d'une action de compensation Saga ou d'un bail TTL par mutation) ; `R-07` (grille `R`, Tampon de pré-engagement (fenêtre de grâce ou approbation) devant toute action irréversible) ; `R-14` (grille `R`, Cloisonnement multilocataire du contexte et des caches d'inférence) ; `O-02` (grille `O`, Caviardage ou masquage automatique des renseignements personnels (PII) avant export OTel) ; `O-09` (grille `O`, Enveloppe budgétaire maximale en devises (`maxTotalCostCad`) active par transaction/saga) ; `G-01` (grille `G`, Propriétaire métier nominatif désigné) ; `G-03` (grille `G`, Qualification réglementaire de l'empreinte de déploiement) ; `G-05` (grille `G`, Évaluation des facteurs relatifs à la vie privée (ÉFVP — Loi 25 / RGPD)) ; `G-06` (grille `G`, Mécanisme d'information, d'explication et de révision (Loi 25 art. 12.1)) ; `G-07` (grille `G`, Divulgation de l'interaction avec une IA (EU AI Act art. 50, 2 août 2026)) ; `G-10` (grille `G`, Droit à l'effacement et purge sélective vérifiable dans la mémoire à long terme) ; `G-15` (grille `G`, Archivage immuable et horodaté (WORM) des décisions critiques) ; `F-04` (grille `F`, Résidence juridictionnelle vérifiée des couches d'état (ch. 12 et ch. 26 / Tome 3 §46.1–46.9)) ; `F-14` (grille `F`, Confinement du SRE autonome (lecture seule assainie, aucun shell libre, budget Cedar R1/R2 + H0)).

## 6. Cinquante-deux capacités (`CAP-001`–`CAP-052`), tronc multisectoriel et vingt-quatre propositions d'exigence (`PEX-001`–`PEX-044`)

Les **52 capacités** (dépliées intégralement en section 9) se répartissent par statut (`conditionnelle` : 10, `invariante` : 42) et par palier (`P1` : 30, `P2` : 18, `P3` : 4) : le tronc multisectoriel invariant de quarante-deux capacités possédées encadre tout système d'entreprise (`ERP`, `CRM`, `SIRH`, `ITSM`, `SCM`, portes bloquantes `R-01` sur l'inviolabilité des systèmes d'enregistrement et `F-14` sur le sas `IT/OT`), tandis que dix capacités conditionnelles (`CAP-026` à `CAP-028`, fédération `B2B`, post-quantique avancé) s'activent par profil d'exposition. À l'étage de haute régulation prudentielle, les **24 propositions d'exigence `PEX`** (`PEX-001`–`PEX-044`, numérotées par dizaines de profil : `001–005`, `011–015`, `021–025`, `031–035`, `041–044`) et les douze `EXIG-AMF` constituent l'étalon sectoriel couvrant les cinq profils réglementés (Banque : 5, Patrimoine : 5, Assurance personnes : 5, Assurance dommages : 5, Groupe diversifié : 4) : `PEX-001` (Banque, `M-14`, Rejet de l'accès par authentifiant client et vérification d'accréditation auprès de la Banque du Canada) ; `PEX-002` (Banque, `M-14`, Liaison cryptographique du consentement exprès par produit et conservation probatoire à double horizon (cinq et sept ans)) ; `PEX-003` (Banque, `M-14`, Garde-fou déterministe d'exclusion du commerce de l'assurance non autorisée sur canal bancaire) ; `PEX-004` (Banque, `M-14`, Tampon d'irréversibilité et approbation liée aux paramètres avant émission d'un virement temps réel ISO 20022) ; `PEX-005` (Banque, `M-14`, Résidence canadienne des livres bancaires, alertes électroniques de solde et loyauté terminologique du traitement des plaintes) ; `PEX-011` (Patrimoine, `M-15`, Dossier explicable de convenance centrée sur le client et rattachement non délégable à une personne physique inscrite) ; `PEX-012` (Patrimoine, `M-15`, Double barrière des comptes d'exécution d'ordres sans conseils : non-recommandation et blocage des systèmes automatisés d'ordres des clients) ; `PEX-013` (Patrimoine, `M-15`, Approbation préalable d'un superviseur désigné, prévention des allégations trompeuses sur l'IA et archivage septennal durable) ; `PEX-014` (Patrimoine, `M-15`, Neutralité algorithmique face aux conflits d'intérêts rémunératoires et exclusion des rétrofacturations interdites) ; `PEX-015` (Patrimoine, `M-15`, Intégrité décimale et traçabilité quotidienne des ratios et frais de fonds entre gestionnaires et courtiers) ; `PEX-021` (Assurance personnes, `M-16`, Filtrage déterministe et caviardage préalable des résultats de tests génétiques) ; `PEX-022` (Assurance personnes, `M-16`, Attestation de consentement exprès distinct lors des requêtes auprès d'organismes de santé) ; `PEX-023` (Assurance personnes, `M-16`, Verrou de révision humaine qualifiée avant refus d'assurabilité ou cessation de prestations vitales) ; `PEX-024` (Assurance personnes, `M-16`, Déclaration obligatoire, homologation et collecte probatoire des agents exploités par les sociétés mandataires) ; `PEX-025` (Assurance personnes, `M-16`, Protection cryptographique agile et conservation multidécennale des dossiers d'assurance de personnes) ; `PEX-031` (Assurance dommages, `M-17`, Profil pré-homologué d'élasticité catastrophique et interdiction des refus automatisés d'indemnisation) ; `PEX-032` (Assurance dommages, `M-17`, Assemblage déterministe exclusif des formulaires et avenants approuvés en assurance automobile) ; `PEX-033` (Assurance dommages, `M-17`, Journalisation probatoire et neutralité comparative des soumissions multi-assureurs hors groupe en courtage) ; `PEX-034` (Assurance dommages, `M-17`, Identités d'agents dédiées par cabinet tiers et décontamination multimodale sur les passerelles externes) ; `PEX-035` (Assurance dommages, `M-17`, Qualification indépendante des modèles externes de catastrophe et traçabilité des émissions associées à l'assurance) ; `PEX-041` (Groupe diversifié, `M-18`, Cloisonnement technique inter-entités et blocage du partage banque-assurance dans le socle de groupe) ; `PEX-042` (Groupe diversifié, `M-18`, Jeton vérifiable de consentement exprès granulaire avant toute délégation inter-filiales) ; `PEX-043` (Groupe diversifié, `M-18`, Encadrement contractuel d'impartition intra-groupe, auditabilité par filiale et plans de sortie du noyau mutualisé) ; `PEX-044` (Groupe diversifié, `M-18`, Présentation désagrégée par métier réglementé des inventaires de modèles, des livres et des divulgations climatiques).

## 7. Liaisons exécutables `G0` (95), spécifications `L+` (57) et portefeuille `DAPP`

Les liaisons exécutables se répartissent par module de la trousse : `authz_pqc_audit` (24 contrôles : `S-01`, `S-03`, `S-14`, `S-15`, `R-07`, `O-02`, `O-09`, `G-15`, `SBB-SECRETS-VAULT`, `SBB-SIGNED-HUMAN-APPROVAL` et 14 autres en section 12) ; `evalops_prr` (24 contrôles : `G-01`, `G-03`, `G-05`, `G-06`, `G-07`, `G-10`, `F-04`, `2027-B001`, `EXIG-SEC-24`, `EXIG-EVA-03` et 14 autres en section 12) ; `harness_proto` (18 contrôles : `R-01`, `EXIG-MCP-03`, `EXIG-MCP-15`, `EXIG-MCP-16`, `EXIG-MCP-18`, `EXIG-MCP-19`, `EXIG-MCP-20`, `EXIG-A2A-03`, `C01`, `C07` et 8 autres en section 12) ; `policy_saga` (29 contrôles : `S-06`, `S-08`, `S-09`, `S-11`, `R-03`, `R-06`, `R-14`, `F-14`, `SBB-GUARDRAILS-ENGINE`, `SBB-FINOPS-BUDGET-QUOTA` et 19 autres en section 12).

Les **57 spécifications techniques ouvertes `L+`** (inventaire complet en section 11) se ventilent par maturité (`FINAL_STANDARD` : 38, `REGULATION_IN_FORCE` : 5, `IETF_WORKING_GROUP_DRAFT` : 4, `SPEC_DEVELOPMENT` : 3, `FIPS_STANDARD` : 3, `RC_OR_ALPHA` : 2, `IETF_INDIVIDUAL_DRAFT` : 1, `REGULATION_ADOPTED_FUTURE` : 1) et par licence (`IETF-Trust` : 27, `Apache-2.0` : 10, `MIT` : 6, `NIST-PD` : 3, `OIDF-Spec` : 3, `EU-Public-Domain` : 3, `Canada-OGL` : 2, `CC-BY-4.0` : 1, `BSD-3-Clause` : 1, `QC-Public-Domain` : 1).

Le portefeuille prospectif `DAPP` (renvoyé depuis le Chapitre 31) est intégralement déplié en section 12 : **43 initiatives `INI-*`**, **15 portes `POR-*`** et **27 signaux `SIG-*`**, accompagnés des **43 rubriques** de la grille unifiée `EXIG / PRR / Portes`.

La Figure 139 illustre la ventilation par préfixe des 305 exigences face aux 24 portes bloquantes et aux 95 contrôles `G0`.

![Ventilation des 305 exigences CRE-IA, 24 portes bloquantes PRR et 95 liaisons G0](././schemas/rendus/SCH-AD-01.svg)

*Figure 139 — SCH-AD-01 : Ventilation quantitative des 305 exigences `EXIG-*` sur les seize préfixes normatifs, croisée aux 24 portes bloquantes `PRR-75` (`S/R/O/G/F`) et aux 95 liaisons exécutables de la barrière `G0` (`matrice-exig-prr-c40.json`).*

## 8. Chaîne d'étanchéité `G0`–`G5`, double recollation `G3` et liaisons d'opérationnalisation

Les deux passes de recollation à l'aveugle portent chacune sur cent quarante-huit items répartis en quatre strates égales de trente-sept assertions (`empirique`, `juridique`, `spec_technique` et `assertions_g0`), avec un plancher de quatre items par unité narrative et un chevauchement nul entre passes. Les deux campagnes effectives consignent **148** items (`seed=20270901`) et **148** items (`seed=20270902`), atteignant `148/148` (`100,0 %`) après rectifications. Par ailleurs, le graphe relie l'architecture exécutable aux exigences par **293 liaisons** (`operationnalisation` : 129, `encadrement_normatif` : 82, `attenuation_risque` : 82), intégralement listées dans l'Annexe B (section 6).

### Couverture exclusive des concepts par unité (`00-liminaire` et `ch01`–`ch36`)

En amont des trente-six chapitres, le `00-liminaire` introduit les concepts directeurs transversaux (`liminaire_doctrine_80_20_et_lusser`, `liminaire_topologie_12_domaines_616_interrelations`, `liminaire_gouvernance_duale_ae_as_kpi_slo`, `liminaire_cadre_reglementaire_2023_2035_non_avis`, `liminaire_concordance_div02_disc_01_05`, `liminaire_panorama_visuel_sch_00_01_04`).

- **`ch01` (`D01`) : `systems-of-agency`, `echanges-intentions-contrats-probabilistes`, `rupture-modele-conversationnel-agent-boucle`, `etat-des-lieux-adoption-map-2027`, `taxonomie-acteurs-agentiques`, `hierarchie-preuves-etudes-cas`, `raisonnement-inference-limites-planification`, `revue-litterature-mlr-prisma`**.

- **`ch02` (`D01`) : `erreurs-silencieuses-cascade`, `loi-de-lusser`, `surcout-multi-agent-debat-mast`, `constance-pass-k`**.

- **`ch03` (`D01`) : `dette-cognitive-vs-technique`, `marche-ia-agentique-dispersion`, `economie-industrialisation-cognitive`, `economie-jetons-routage-slm`, `couts-transaction-coase`, `quadruple-dette-agentique`, `cout-non-interop-dette-integration`, `genealogie-eai-soa-fipa-llm`**.

- **`ch04` (`D02`, `CA-G0-SYNC`) : `partition-hybride-80-20`, `harnais-deterministe-8-etapes`, `usine-logicielle-agentic-sdlc`, `patrons-boucle-mono-agent-codeact`, `separation-controleur-executeur-determinisme`, `validation-json-schema-ambigu-escalade`, `pont-reglementation-frames-deterministes`**.

- **`ch05` (`D02`) : `echelle-autonomie-l0-l4`, `regle-maillon-plus-eleve`, `supervision-hitl-hotl-abstention`, `distinction-agent-flux-ambiant`**.

- **`ch06` (`D02`) : `noyau-controle-possede-cap`, `cadre-togaf-archimate-4-plans`, `catalogue-31-adr-12-dec`, `clauses-sortie-portabilite-interchangeabilite`, `decisions-architecture-adr-001-031`, `grille-evaluation-maturite-n1-n5`, `architecture-reference-6-couches-2-piliers`, `principes-architecture-pri-001-015`, `architecture-outils-fiables-erreurs-actionnables`, `douze-principes-directeurs-prin`, `criteres-qos-cout-precision-latence`, `architecture-reference-six-couches-pc1-pc5`**.

- **`ch07` (`D03`, `CA-G0-SYNC`) : `protocole-mcp`, `web-agentique-webmcp-webbotauth`, `facades-mcp-intention-metier`, `adaptateur-mcp-streamable-http-sep-3398`, `ergonomie-aci-anti-swagger`, `epinglage-schemas-mcp`**.

- **`ch08` (`D03`, `CA-G0-SYNC`) : `protocole-a2a`, `protocole-ap2`, `protocole-anp-did-wba`, `protocoles-interfaces-agui-a2ui-webrtc`, `fusion-acp-collision-terminologique`, `rails-paiement-commerce-agentique`, `agntcy-slim`, `maillage-b2b-federe-edc-odrl`**.

- **`ch09` (`D03`) : `agent-card-decouverte`, `contrats-interfaces-catalogue-entreprise`, `contrats-api-versionnement-conformite`, `plan-donnees-inference-kv-cache`, `routage-cognitif-hybride-3-paliers`, `anti-verrouillage-standards`, `passerelle-mcp-ai-gateway`, `cadre-eif-4-couches`, `metriques-soutien-vs-production`, `maillage-agentique-trois-acceptions`, `matrice-protocoles-exigences-reglementaires`**.

- **`ch10` (`D04`) : `dette-semantique-ontologies`, `contrats-donnees-write-audit-publish`, `donnees-pretes-agents-odcs-openlineage`, `ecart-accord-protocolaire-comprehension`, `formats-echange-registres-schemas`, `iso-20022-lynx-rtr`, `rag-agentique-contexte`**.

- **`ch11` (`D04`) : `memoire-coala-4-tiroirs`, `memoire-partagee-concurrence-effacement`, `memoire-bi-temporelle-et-purge`, `propagation-acl-memoire-silo`, `gouvernance-acces-rag-ancrage`**.

- **`ch12` (`D04`) : `couche-anti-corruption-acl`, `encapsulation-patrimoine-it-ot`, `confinement-cua-patrimoine-sans-api`, `mediation-b2b-esb-traducteurs`, `coexistence-bpm-ipaas-rpa`, `six-substrats-etat-souverainete`, `synchronisation-edge-crdt`**.

- **`ch13` (`D05`) : `arbre-sobriete-oo1-oo4`, `enveloppes-bpmn-cas-routine`, `paradigme-apm-autonomie-encadree`, `topologies-patrons-orchestration`, `cadriciels-orchestration-portabilite`, `negociation-b2b-diplomate-evaluateur`, `fiabilite-coordination-taxonomie-mast`, `modes-echecs-emergents-frontiere`, `contexte-minimal-delegation-interagents`, `frameworks-orchestration-entreprise`**.

- **`ch14` (`D05`) : `choregraphie-event-mesh`, `pathologies-reactives-backpressure`, `pont-ia-physique-ros2-simplex`**.

- **`ch15` (`D05`, `CA-G0-SYNC`) : `execution-durable-temporal`, `resilience-orchestration-repli-plafonds`, `protocoles-ressources-physiques-lap`, `saga-compensatoire`, `canal-compensation-isole-outbox`, `saga-dix-scenarios-fautes`, `semantique-effet-idempotence-uetr`**.

- **`ch16` (`D06`) : `identite-non-humaine-nhi`, `grille-cinq-questions-identite`, `annuaires-commerciaux-risque-standard-de-fait`, `socle-iam-federe-oauth-fapi`, `registres-gouvernes-trois-modeles`, `did-vc-passeport-agent`, `spiffe-spire-attestation`, `signature-agent-card-ancrage`**.

- **`ch17` (`D06`, `CA-G0-SYNC`) : `delegation-obo-deux-sauts`, `requetes-riches-rar-txn-tokens`, `liaison-jetons-dpop-mtls`, `profil-oauth-9700-et-liaison-expediteur`, `approbation-ciba`, `kya-verification-agent-tiers`, `inventaire-revocation-asymetrie`**.

- **`ch18` (`D06`, `CA-G0-SYNC`) : `certificats-tls-47-jours`, `post-quantique-ml-dsa-slh-dsa`, `crypto-agilite-migration-pqc`, `saturation-http-431-ml-dsa-kid`**.

- **`ch19` (`D07`) : `injection-indirecte-prompt`, `tool-poisoning-rug-pull`, `non-compositionnalite-surete-surface-attaques`, `chaine-approvisionnement-agent-skills`, `taxonomie-attaques-identite-mandataire-confus`, `taxonomie-owasp-asi-mcp-maestro`, `red-teaming-continu-empoisonnement-memoire`**.

- **`ch20` (`D07`, `CA-G0-SYNC`) : `politiques-opa-rego-hors-modele`, `echec-ferme-opa-default-deny`, `controle-surete-stamp-stpa`, `maillage-agents-pep-pdp-zero-trust`, `regle-de-deux-opa`, `separation-controle-donnees-camel`, `sre-autonome-rayon-impact-cedar`, `defense-hors-modele-camel-confinement`, `alignement-deceptif-red-teaming-adversarial`**.

- **`ch21` (`D07`) : `confinement-shadi-sandbox`, `confidentialite-materielle-tee-hyok`, `confinement-opensandbox-firecracker-wasi`, `soc-soar-coupe-circuit`**.

- **`ch22` (`D08`, `CA-G0-SYNC`) : `observabilite-otel-genai`, `provenance-artefacts-aibom-5-horloges`, `double-couloir-probatoire-pii`, `scellage-jcs-scitt`, `caviardage-pii-rp-bilingue`, `canonisation-deterministe-jcs`, `canonicalisation-jcs-rfc8785`, `journalisation-probatoire-audit`**.

- **`ch23` (`D08`, `CA-G0-SYNC`) : `banc-evalops-hermetique`, `evaluation-agentique-bancs-capacite`, `dimensionnement-wilson-evalops`, `volant-distillation-dspy-multilora`, `tests-metamorphiques-fr-en-sans-oracle`, `evaluation-continue-derives`, `modele-comme-juge-biais-calibration`**.

- **`ch24` (`D08`) : `finops-focus-cpo`, `plan-inference-routage-carbone`, `comptabilite-carbone-cap-046-bsif-b15`, `cycle-vie-operationnel-derives-gitops`, `indicateurs-agentops-horizon-tache`**.

- **`ch25` (`D09`) : `loi-25-article-12-1`, `ligne-directrice-amf`, `droit-effacement-portabilite-loi-25`, `efvp-transfert-hors-quebec`, `bsif-e-23`, `avis-acvm-11-348`, `gouvernance-interne-registre-trois-lignes`, `services-bancaires-consommateurs-c15`, `feuille-route-1er-mai-2027`, `vide-federal-ia-c27-c36`**.

- **`ch26` (`D09`) : `eu-ai-act`, `systeme-qualite-en-18286-dora-cra`, `maillage-reglementaire-international`, `iso-iec-42001-nist`, `souverainete-espaces-donnees-tee-hyok`, `cadres-internationaux-imda-aica-g7`, `classes-risque-agents-et-plafonds`, `incidents-agentiques-et-notification-multiregime`**.

- **`ch27` (`D09`) : `approvisionnement-reversible-contrats`, `clauses-reversibilite-cloud-souverain`, `clauses-contractuelles-normatives-app`, `responsabilite-mandat-contrats-b2b`, `criteres-evaluation-fournisseurs-grille`**.

- **`ch28` (`D10`) : `profils-financiers-5-secteurs`, `profil-assurance-dommages-m17`, `profil-assurance-personnes-m16`, `profil-banque-m14`, `profil-gestion-patrimoine-m15`, `profil-groupe-diversifie-m18`, `eclats-sectoriels-extrapoles`, `vertical-financier-durci`, `tampon-deterministe-rtr-iso20022`, `production-agentique-canadienne-2025-2026`**.

- **`ch29` (`D10`) : `blueprints-reference-multisectoriels`, `blueprint-1-assistant-sor`, `blueprint-2-enclave-rag-acl`, `blueprint-3-maillage-b2b`, `fil-rouge-groupe-boreal-bel`, `federation-multi-plateformes-gravite`, `reprise-sinistre-cognitif-continuite`, `reseaux-b2b-federes-p3`**.

- **`ch30` (`D10`) : `plateformes-saas-et-asymetrie-tiers`, `fabrique-agents-certification-reemission`, `passage-echelle-parc-agents`, `plateforme-iap-gitops-cognitif`, `anti-patrons-agentiques`, `modele-maturite-feuille-360j`**.

- **`ch31` (`D11`) : `trajectoires-adaptatives-dapp`, `vingt-sept-signaux-veille-sig`, `quinze-portes-homologation-por`, `trajectoire-90j-18m-p1-p3`, `feuille-de-route-phases-90-jours-indicateurs`, `trajectoire-consolidation-standards-2027-2028`, `priorites-90-jours-gouvernance`, `tri-prospectif-peremption-feuilles-route`, `frontiere-capacites-metr-veille`, `modele-maturite-5-niveaux-dimensions`, `horizon-2027-2032-tri-prospectif`**.

- **`ch32` (`D11`) : `gouvernance-duale-ae-as`, `modele-operationnel-hub-and-spoke`, `dix-theses-t1-t10-tome-5`, `gouvernance-raci-modele-en-etoile`, `regime-derogations-et-transition-cohorte`, `registre-agents-cycle-de-vie-et-attestations`, `pieges-gouvernance`, `responsabilite-litiges-commerce-agentique`**.

- **`ch33` (`D11`) : `atrophie-competences-humaines`, `sanctuarisation-vivier-junior-reprise`, `approbation-reflexe-biais-automatisation`**.

- **`ch34` (`D12`, `CA-G0-SYNC`) : `exigences-cre-ia-305`, `dix-interdictions-exig-gov-17`, `portee-et-force-normative-cre-ia`, `homologation-prr-75-points`, `referentiel-annexes-protocoles-chronologie`, `grille-homologation-et-fiche-agent`**.

- **`ch35` (`D12`, `CA-G0-SYNC`) : `barriere-logicielle-g0-execute-g0`, `trousse-executable-tome-8`, `cinq-blocs-sbb-tableau-12`, `calibration-feds-ema`, `contrats-types-executes-ci-annexe-c`**.

- **`ch36` (`D12`) : `concordance-inter-tomes-div02`, `architecture-collection-tome-1-preambule`, `reconciliation-inter-volumes-tome1`, `cinq-discordances-inter-volumes-tome-8`, `glossaire-normatif-tome-2`, `clause-non-avis-licences`, `protocole-wyvern-g0-g5`, `regime-preuve-trois-degres-absence`, `gabarit-typst-edition-4542-pages`, `protocole-probatoire-l-plus-statut-f`, `audit-validation-sources-121-449`, `actualisation-novembre-2026-unification-v1-2`, `peremption-revalidation-annexe-n`, `registre-sources-tracees-annexe-b`**.

Sur l'axe `D02`, la catégorie `attenuation_risque` rassemble 9 liaisons, notamment `REL_0236` (`validation-json-schema-ambigu-escalade` vers `erreurs-silencieuses-cascade`), `REL_0308` (`harnais-deterministe-8-etapes` vers `constance-pass-k`), `REL_0309` (`harnais-deterministe-8-etapes` vers `erreurs-silencieuses-cascade`), `REL_0400` (`partition-hybride-80-20` vers `loi-de-lusser`), `REL_0540` (`separation-controleur-executeur-determinisme` vers `constance-pass-k`), `REL_0565` (`supervision-hitl-hotl-abstention` vers `approbation-ciba`).

Sur l'axe `D03`, la catégorie `attenuation_risque` rassemble 8 liaisons, notamment `REL_0027` (`anti-verrouillage-standards` vers `dette-cognitive-vs-technique`), `REL_0028` (`anti-verrouillage-standards` vers `fusion-acp-collision-terminologique`), `REL_0029` (`anti-verrouillage-standards` vers `pieges-gouvernance`), `REL_0231` (`epinglage-schemas-mcp` vers `protocole-mcp`), `REL_0233` (`epinglage-schemas-mcp` vers `tool-poisoning-rug-pull`), `REL_0234` (`ergonomie-aci-anti-swagger` vers `tool-poisoning-rug-pull`).

Sur l'axe `D04`, la catégorie `attenuation_risque` rassemble 13 liaisons, notamment `REL_0143` (`confinement-cua-patrimoine-sans-api` vers `injection-indirecte-prompt`), `REL_0153` (`contrats-donnees-write-audit-publish` vers `dette-semantique-ontologies`), `REL_0159` (`couche-anti-corruption-acl` vers `dette-semantique-ontologies`), `REL_0160` (`couche-anti-corruption-acl` vers `encapsulation-patrimoine-it-ot`), `REL_0161` (`couche-anti-corruption-acl` vers `erreurs-silencieuses-cascade`), `REL_0185` (`dette-semantique-ontologies` vers `erreurs-silencieuses-cascade`).

Sur l'axe `D05`, la catégorie `attenuation_risque` rassemble 11 liaisons, notamment `REL_0041` (`arbre-sobriete-oo1-oo4` vers `pathologies-reactives-backpressure`), `REL_0120` (`choregraphie-event-mesh` vers `erreurs-silencieuses-cascade`), `REL_0235` (`choregraphie-event-mesh` vers `pathologies-reactives-backpressure`), `REL_0237` (`topologies-patrons-orchestration` vers `erreurs-silencieuses-cascade`), `REL_0378` (`negociation-b2b-diplomate-evaluateur` vers `responsabilite-mandat-contrats-b2b`), `REL_0397` (`paradigme-apm-autonomie-encadree` vers `supervision-hitl-hotl-abstention`).

Sur l'axe `D06`, la catégorie `attenuation_risque` rassemble 12 liaisons, notamment `REL_0036` (`approbation-ciba` vers `supervision-hitl-hotl-abstention`), `REL_0173` (`delegation-obo-deux-sauts` vers `anti-patrons-agentiques`), `REL_0174` (`delegation-obo-deux-sauts` vers `erreurs-silencieuses-cascade`), `REL_0175` (`delegation-obo-deux-sauts` vers `identite-non-humaine-nhi`), `REL_0177` (`delegation-obo-deux-sauts` vers `injection-indirecte-prompt`), `REL_0315` (`identite-non-humaine-nhi` vers `kya-verification-agent-tiers`).

Sur l'axe `D07`, la catégorie `attenuation_risque` rassemble 20 liaisons, notamment `REL_0017` (`alignement-deceptif-red-teaming-adversarial` vers `defense-hors-modele-camel-confinement`), `REL_0141` (`confidentialite-materielle-tee-hyok` vers `six-substrats-etat-souverainete`), `REL_0145` (`confinement-opensandbox-firecracker-wasi` vers `injection-indirecte-prompt`), `REL_0146` (`confinement-shadi-sandbox` vers `chaine-approvisionnement-agent-skills`), `REL_0147` (`confinement-shadi-sandbox` vers `injection-indirecte-prompt`), `REL_0149` (`confinement-shadi-sandbox` vers `tool-poisoning-rug-pull`).

Sur l'axe `D08`, la catégorie `attenuation_risque` rassemble 6 liaisons, notamment `REL_0061` (`banc-evalops-hermetique` vers `erreurs-silencieuses-cascade`), `REL_0111` (`canonicalisation-jcs-rfc8785` vers `signature-agent-card-ancrage`), `REL_0199` (`double-couloir-probatoire-pii` vers `loi-25-article-12-1`), `REL_0253` (`evaluation-continue-derives` vers `tool-poisoning-rug-pull`), `REL_0283` (`finops-focus-cpo` vers `erreurs-silencieuses-cascade`), `REL_0487` (`provenance-artefacts-aibom-5-horloges` vers `tool-poisoning-rug-pull`).

<!-- BIBLIOGRAPHIE_BRUTE_DEBUT -->
## 9. Inventaire intégral des 52 capacités (`CAP-001`–`CAP-052`)

- **`CAP-001`** (`invariante`, `P1`, `interaction`) — Rendu d'interfaces génératives sur catalogues déclaratifs bornés ; exigences : `EXIG-ARC-03`, `EXIG-MCP-04`, `EXIG-MCP-19`.
- **`CAP-002`** (`invariante`, `P1`, `interaction`) — Postes de supervision humaine instrumentés et approbation liée aux paramètres ; exigences : `EXIG-AUT-09`, `EXIG-AUT-12`, `EXIG-AUT-13`, `EXIG-AUT-14`, `EXIG-AUT-15`, `EXIG-AUT-16`, `EXIG-AUT-19`, `EXIG-AUT-20`, `EXIG-AUT-21`.
- **`CAP-003`** (`invariante`, `P1`, `interaction`) — Transparence client, avis contemporain et canal de révision humaine effective ; exigences : `EXIG-AUT-22`, `EXIG-AUT-23`, `EXIG-CON-07`, `EXIG-CON-08`, `EXIG-CON-21`, `EXIG-AMF-12`.
- **`CAP-004`** (`conditionnelle`, `P2`, `interaction`) — Interaction vocale et multimodale en temps réel avec gestion d'interruption ; exigences : `EXIG-ARC-04`, `EXIG-CON-19`.
- **`CAP-005`** (`invariante`, `P1`, `interaction`) — Contrôle préalable et archivage supervisé des communications externes assistées ; exigences : `EXIG-CON-20`, `EXIG-CON-22`, `EXIG-CON-28`.
- **`CAP-006`** (`conditionnelle`, `P3`, `interaction`) — Authentification et encadrement des agents externes sur les canaux numériques ; exigences : `EXIG-A2A-09`, `EXIG-IAM-01`.
- **`CAP-007`** (`invariante`, `P1`, `agents-orchestration`) — Enveloppe de séquencement déterministe autour des cellules agentiques bornées ; exigences : `EXIG-ARC-02`, `EXIG-ARC-07`, `EXIG-ORC-01`, `EXIG-ORC-03`, `EXIG-ORC-24`, `EXIG-ORC-26`, `EXIG-ORC-29`.
- **`CAP-008`** (`invariante`, `P1`, `agents-orchestration`) — Exécution durable, journalisation déterministe et revalidation au réveil ; exigences : `EXIG-ARC-05`, `EXIG-ARC-06`, `EXIG-ORC-11`, `EXIG-ORC-12`, `EXIG-ORC-13`, `EXIG-ORC-14`, `EXIG-ORC-27`, `EXIG-AUT-17`.
- **`CAP-009`** (`invariante`, `P1`, `agents-orchestration`) — Idempotence transactionnelle de bout en bout, sagas à compensation et tampon d'irréversibilité ; exigences : `EXIG-ORC-15`, `EXIG-ORC-16`, `EXIG-ORC-17`, `EXIG-ORC-18`, `EXIG-ORC-19`, `EXIG-ORC-21`, `EXIG-ORC-22`, `EXIG-CON-29`.
- **`CAP-010`** (`invariante`, `P2`, `agents-orchestration`) — Catalogue homologué de topologies multi-agents et revue contradictoire hétérogène ; exigences : `EXIG-ORC-02`, `EXIG-ORC-04`, `EXIG-ORC-05`, `EXIG-ORC-06`, `EXIG-ORC-07`, `EXIG-ORC-09`, `EXIG-ORC-10`.
- **`CAP-011`** (`invariante`, `P2`, `agents-orchestration`) — Dorsale événementielle asynchrone et rejouabilité d'audit ; exigences : `EXIG-ARC-13`, `EXIG-INT-11`, `EXIG-EVT-01`, `EXIG-EVT-02`, `EXIG-EVT-03`, `EXIG-EVT-04`, `EXIG-EVT-05`, `EXIG-EVT-07`, `EXIG-EVT-08`, `EXIG-EVT-09`, `EXIG-EVT-10`.
- **`CAP-012`** (`invariante`, `P2`, `agents-orchestration`) — Protocole normalisé de délégation inter-agents interne et garde anti-boucle ; exigences : `EXIG-INT-04`, `EXIG-INT-05`, `EXIG-A2A-01`, `EXIG-A2A-02`, `EXIG-A2A-05`, `EXIG-A2A-07`, `EXIG-A2A-13`, `EXIG-A2A-15`, `EXIG-EVT-06`, `EXIG-ORC-08`.
- **`CAP-013`** (`conditionnelle`, `P2`, `agents-orchestration`) — Fédération d'orchestration multi-plateformes selon la gravité des données ; exigences : `EXIG-ARC-19`, `EXIG-ARC-20`, `EXIG-ARC-21`, `EXIG-A2A-06`.
- **`CAP-014`** (`conditionnelle`, `P3`, `agents-orchestration`) — Négociation et exécution inter-organisations à séparation négociateur-évaluateur ; exigences : `EXIG-A2A-10`, `EXIG-A2A-12`, `EXIG-INT-22`, `EXIG-ORC-25`.
- **`CAP-015`** (`invariante`, `P2`, `contexte-connaissance`) — Couche sémantique gouvernée et contrats ontologiques métiers versionnés ; exigences : `EXIG-INT-01`, `EXIG-INT-02`.
- **`CAP-016`** (`invariante`, `P2`, `contexte-connaissance`) — Médiation sémantique canonique vers les standards de données sectoriels et d'entreprise (ISO 20022, FIBO, EDI/UBL, FHIR, ISA-95) ; exigences : `EXIG-INT-13`, `EXIG-INT-14`.
- **`CAP-017`** (`invariante`, `P1`, `contexte-connaissance`) — Compilation déterministe du contexte, filtrage d'accès en amont et passage par référence ; exigences : `EXIG-ARC-16`, `EXIG-ARC-22`, `EXIG-ORC-23`.
- **`CAP-018`** (`invariante`, `P1`, `contexte-connaissance`) — Bibliothèque gouvernée, versionnée et signée de compétences procédurales portables ; exigences : `EXIG-ARC-24`, `EXIG-INT-15`, `EXIG-INT-16`.
- **`CAP-019`** (`invariante`, `P2`, `contexte-connaissance`) — Mémoire persistante bi-temporelle auditable à date, garde anti-empoisonnement et oubli sélectif ; exigences : `EXIG-ARC-23`, `EXIG-ARC-25`, `EXIG-CON-10`, `EXIG-AMF-10`.
- **`CAP-020`** (`invariante`, `P2`, `contexte-connaissance`) — Contrats formels de qualité des données et sas de quarantaine avant exposition ; exigences : `EXIG-INT-12`, `EXIG-INT-19`.
- **`CAP-021`** (`invariante`, `P1`, `contexte-connaissance`) — Cloisonnement contextuel par entité juridique, finalité de consentement et données prohibées ; exigences : `EXIG-CON-04`, `EXIG-CON-06`, `EXIG-CON-14`.
- **`CAP-022`** (`invariante`, `P1`, `acces`) — Passerelle unifiée de médiation et des neuf contrôles par invocation d'outil (7 aller, 2 retour, incluant le noyau des 5 contrôles) ; exigences : `EXIG-ARC-01`, `EXIG-ARC-11`, `EXIG-ARC-12`, `EXIG-MCP-01`, `EXIG-MCP-08`, `EXIG-MCP-09`, `EXIG-MCP-17`, `EXIG-MCP-22`, `EXIG-IAM-17`, `EXIG-IAM-19`, `EXIG-SEC-21`.
- **`CAP-023`** (`invariante`, `P1`, `acces`) — Conception d'outils orientés intention métier et épinglage cryptographique des schémas ; exigences : `EXIG-ARC-15`, `EXIG-MCP-02`, `EXIG-MCP-03`, `EXIG-MCP-05`, `EXIG-MCP-06`, `EXIG-MCP-07`, `EXIG-MCP-14`, `EXIG-MCP-15`, `EXIG-MCP-16`, `EXIG-MCP-18`, `EXIG-MCP-20`, `EXIG-MCP-21`.
- **`CAP-024`** (`invariante`, `P1`, `acces`) — Encapsulation déterministe des systèmes centraux patrimoniaux en arithmétique décimale exacte ; exigences : `EXIG-ARC-14`, `EXIG-ARC-17`, `EXIG-ARC-18`.
- **`CAP-025`** (`conditionnelle`, `P1`, `acces`) — Harnais dérogatoire sous double validation et extinction programmée des agents d'interface graphique ; exigences : complémentaire.
- **`CAP-026`** (`invariante`, `P2`, `acces`) — Passerelles d'interfaces réglementées pour le partage financier ouvert et les tiers accrédités ; exigences : `EXIG-INT-06`, `EXIG-INT-07`, `EXIG-MCP-10`, `EXIG-MCP-12`, `EXIG-MCP-13`.
- **`CAP-027`** (`conditionnelle`, `P3`, `acces`) — Connecteurs d'espaces de données fédérés sous politiques d'usage exécutables ; exigences : `EXIG-INT-03`, `EXIG-A2A-08`, `EXIG-A2A-11`.
- **`CAP-028`** (`conditionnelle`, `P2`, `acces`) — Sas déterministe pour flux physiques ou télématiques et continuité locale hors réseau ; exigences : complémentaire.
- **`CAP-029`** (`invariante`, `P1`, `modeles`) — Plan de données d'inférence, routage cognitif à trois paliers et affinité de cache ; exigences : `EXIG-ARC-08`, `EXIG-ARC-09`, `EXIG-FIN-06`, `EXIG-FIN-07`.
- **`CAP-030`** (`invariante`, `P1`, `modeles`) — Confinement d'exécution en bac à sable isolé matériellement sans réseau sortant ; exigences : `EXIG-ARC-10`, `EXIG-SEC-08`, `EXIG-SEC-09`, `EXIG-SEC-10`, `EXIG-SEC-11`, `EXIG-SEC-12`, `EXIG-SEC-13`, `EXIG-SEC-14`, `EXIG-SEC-15`, `EXIG-SEC-16`, `EXIG-SEC-17`.
- **`CAP-031`** (`invariante`, `P2`, `modeles`) — Continuité cognitive bimodèle et bascule éprouvée vers un profil à poids ouverts ; exigences : `EXIG-SEC-22`, `EXIG-APP-14`.
- **`CAP-032`** (`invariante`, `P1`, `modeles`) — Cloisonnement juridictionnel des six substrats d'état et maîtrise souveraine des clés ; exigences : `EXIG-CON-05`, `EXIG-APP-11`.
- **`CAP-033`** (`conditionnelle`, `P2`, `modeles`) — Inférence confidentielle en enclave matérielle attestée sur processeurs et accélérateurs ; exigences : complémentaire.
- **`CAP-034`** (`conditionnelle`, `P2`, `modeles`) — Compilation déclarative des consignes et distillation contrôlée sous sas anti-renseignements personnels ; exigences : `EXIG-ARC-24`, `EXIG-CON-10`.
- **`CAP-035`** (`invariante`, `P1`, `controle-identite-securite`) — Identités non humaines uniques par classe d'agent, parrainage nominatif et attestations éphémères ; exigences : `EXIG-IAM-02`, `EXIG-IAM-03`, `EXIG-IAM-04`, `EXIG-IAM-05`, `EXIG-IAM-06`, `EXIG-IAM-07`, `EXIG-IAM-16`.
- **`CAP-036`** (`invariante`, `P1`, `controle-identite-securite`) — Délégation cryptographique à portée atténuée par saut et preuve de possession ; exigences : `EXIG-IAM-08`, `EXIG-IAM-09`, `EXIG-IAM-10`, `EXIG-IAM-11`, `EXIG-IAM-12`, `EXIG-IAM-13`, `EXIG-IAM-14`, `EXIG-IAM-15`, `EXIG-MCP-11`.
- **`CAP-037`** (`invariante`, `P1`, `controle-identite-securite`) — Point de décision de politique déterministe hors modèle et preuve formelle d'invariants ; exigences : `EXIG-IAM-18`, `EXIG-IAM-21`, `EXIG-AUT-03`, `EXIG-AUT-08`, `EXIG-AUT-10`, `EXIG-AUT-11`.
- **`CAP-038`** (`invariante`, `P1`, `controle-identite-securite`) — Décontamination des entrées externes non fiables et défense contre les menaces agentiques ; exigences : `EXIG-SEC-01`, `EXIG-SEC-02`, `EXIG-SEC-03`, `EXIG-SEC-04`, `EXIG-SEC-05`, `EXIG-SEC-06`, `EXIG-SEC-07`, `EXIG-SEC-23`, `EXIG-SEC-24`, `EXIG-SEC-25`.
- **`CAP-039`** (`invariante`, `P1`, `controle-identite-securite`) — Coupe-circuit opérationnel hiérarchisé et révocation instantanée des sessions et jetons ; exigences : `EXIG-IAM-20`, `EXIG-ORC-28`, `EXIG-SEC-18`, `EXIG-SEC-20`, `EXIG-SEC-26`, `EXIG-APP-06`, `EXIG-APP-16`.
- **`CAP-040`** (`invariante`, `P2`, `controle-identite-securite`) — Agilité cryptographique, inventaire CBOM et transition post-quantique (ML-DSA et SLH-DSA) ; exigences : `EXIG-SEC-19`, `EXIG-OBS-12`, `EXIG-SEC-27`, `EXIG-SEC-28`.
- **`CAP-041`** (`conditionnelle`, `P3`, `controle-identite-securite`) — Identité légale d'organisation vérifiable et justificatifs cryptographiques de mandat externe ; exigences : `EXIG-A2A-03`, `EXIG-A2A-04`, `EXIG-INT-21`.
- **`CAP-042`** (`invariante`, `P1`, `controle-observabilite-finops`) — Télémétrie causale distribuée normalisée au collecteur et double couloir de confidentialité ; exigences : `EXIG-OBS-01`, `EXIG-OBS-02`, `EXIG-OBS-03`, `EXIG-OBS-04`, `EXIG-OBS-05`, `EXIG-OBS-06`, `EXIG-OBS-07`, `EXIG-OBS-08`, `EXIG-OBS-09`, `EXIG-OBS-10`.
- **`CAP-043`** (`invariante`, `P1`, `controle-observabilite-finops`) — Qualification pré-production par simulation multi-tours répétée, chaos et déploiement progressif ; exigences : `EXIG-EVA-01`, `EXIG-EVA-02`, `EXIG-EVA-03`, `EXIG-ORC-20`, `EXIG-ORC-30`, `EXIG-A2A-14`.
- **`CAP-044`** (`invariante`, `P2`, `controle-observabilite-finops`) — Surveillance continue en production, détection de dérive et pilotage par budgets d'erreur ; exigences : `EXIG-EVA-04`, `EXIG-EVA-05`, `EXIG-EVA-06`, `EXIG-AUT-05`.
- **`CAP-045`** (`invariante`, `P1`, `controle-observabilite-finops`) — Pilotage économique par le coût complet du résultat conforme et disjoncteurs budgétaires ; exigences : `EXIG-FIN-01`, `EXIG-FIN-02`, `EXIG-FIN-03`, `EXIG-FIN-04`, `EXIG-FIN-05`, `EXIG-FIN-06`, `EXIG-FIN-08`, `EXIG-FIN-09`, `EXIG-FIN-10`, `EXIG-APP-05`.
- **`CAP-046`** (`invariante`, `P2`, `controle-observabilite-finops`) — Comptabilisation énergétique et carbone des charges d'inférence et des fournisseurs ; exigences : complémentaire.
- **`CAP-047`** (`invariante`, `P1`, `controle-gouvernance-registre`) — Registre central d'inventaire, de cote de risque inhérent et de blocage des agents non homologués ; exigences : `EXIG-GOV-05`, `EXIG-GOV-06`, `EXIG-GOV-07`, `EXIG-GOV-08`, `EXIG-GOV-09`, `EXIG-GOV-10`, `EXIG-GOV-11`, `EXIG-GOV-14`, `EXIG-GOV-15`, `EXIG-GOV-16`, `EXIG-INT-08`, `EXIG-INT-09`, `EXIG-INT-10`, `EXIG-INT-17`, `EXIG-INT-18`, `EXIG-INT-20`, `EXIG-INT-23`, `EXIG-AMF-06`.
- **`CAP-048`** (`invariante`, `P1`, `controle-gouvernance-registre`) — Gouvernance dynamique de l'autonomie par domaine et par classe de décision avec maintien des compétences humaines ; exigences : `EXIG-AUT-01`, `EXIG-AUT-02`, `EXIG-AUT-04`, `EXIG-AUT-06`, `EXIG-AUT-07`, `EXIG-AUT-18`, `EXIG-CON-02`, `EXIG-CON-09`, `EXIG-GOV-01`, `EXIG-GOV-13`, `EXIG-AMF-07`.
- **`CAP-049`** (`invariante`, `P1`, `controle-gouvernance-registre`) — Qualification réglementaire par empreinte juridictionnelle et archivage probatoire intègre ; exigences : `EXIG-OBS-11`, `EXIG-OBS-13`, `EXIG-CON-01`, `EXIG-CON-03`, `EXIG-CON-11`, `EXIG-CON-12`, `EXIG-CON-13`, `EXIG-CON-15`, `EXIG-CON-16`, `EXIG-CON-17`, `EXIG-CON-18`, `EXIG-CON-23`, `EXIG-CON-24`, `EXIG-CON-25`, `EXIG-CON-26`, `EXIG-CON-27`, `EXIG-CON-30`, `EXIG-AMF-05`, `EXIG-AMF-08`, `EXIG-AMF-11`.
- **`CAP-050`** (`invariante`, `P1`, `controle-gouvernance-registre`) — Validation indépendante de deuxième ligne et assurance d'audit interne des trois lignes ; exigences : `EXIG-GOV-02`, `EXIG-GOV-03`, `EXIG-GOV-04`, `EXIG-GOV-12`, `EXIG-GOV-17`, `EXIG-GOV-18`, `EXIG-GOV-19`, `EXIG-GOV-20`, `EXIG-AMF-01`, `EXIG-AMF-02`, `EXIG-AMF-03`, `EXIG-AMF-04`, `EXIG-AMF-09`.
- **`CAP-051`** (`invariante`, `P1`, `controle-gouvernance-registre`) — Gouvernance des tiers, clauses contractuelles de sortie, notification et réversibilité éprouvée ; exigences : `EXIG-APP-01`, `EXIG-APP-02`, `EXIG-APP-03`, `EXIG-APP-04`, `EXIG-APP-07`, `EXIG-APP-08`, `EXIG-APP-09`, `EXIG-APP-10`, `EXIG-APP-12`, `EXIG-APP-13`, `EXIG-APP-15`, `EXIG-APP-17`.
- **`CAP-052`** (`invariante`, `P2`, `controle-gouvernance-registre`) — Ingénierie logicielle, modernisation patrimoniale et exploitation assistées à séparation des tâches ; exigences : complémentaire.

## 10. Inventaire intégral des 75 points de contrôle `PRR-75` (24 bloquants, 51 non bloquants)

- **`S-01`** (grille `S`, `BLOQUANT`) : Identité NHI unique inscrite à l'annuaire d'entreprise (aucune clé API partagée). Preuve : Entrée du registre d'agents et identifiant SPIFFE / Entra Agent ID.
- **`S-02`** (grille `S`, `Élevée`) : Attestation cryptographique de la provenance du code et de la configuration système. Preuve : Signature Sigstore/cosign vérifiée au démarrage du pod.
- **`S-03`** (grille `S`, `BLOQUANT`) : Délégation OAuth 2.1 `On-Behalf-Of` (RFC 8693) préservant `sub` et la chaîne `act`. Preuve : Capture d'un jeton JWT décodé en pré-production.
- **`S-04`** (grille `S`, `Conditionnel`) : Atténuation de portée à chaque saut inter-agents. Preuve : Test automatisé de rejet hors portée (obligatoire si multi-sauts).
- **`S-05`** (grille `S`, `Élevée`) : Durée de vie courte des jetons (≤ 15 min) et contrainte au détenteur (DPoP/mTLS). Preuve : Configuration du serveur d'autorisation et test de rejeu négatif.
- **`S-06`** (grille `S`, `BLOQUANT`) : Séparation entre l'agent d'interface exposé et l'agent détenteur d'outils d'écriture. Preuve : Diagramme de flux réseau et politique d'accès passerelle.
- **`S-07`** (grille `S`, `Conditionnel`) : Épinglage cryptographique (empreinte SHA-256) des descriptions et schémas MCP. Preuve : Manifeste d'empreintes SHA-256 signé et alerte sur modification distante (*rug pull*).
- **`S-08`** (grille `S`, `BLOQUANT`) : Marquage structurel des données externes non fiables contre l'injection indirecte (ASI01). Preuve : Rapport d'équipe rouge automatisée et contrôles hors modèle.
- **`S-09`** (grille `S`, `BLOQUANT`) : Évaluation déterministe hors LLM (Cedar ou OPA) devant chaque appel d'outil mutatif. Preuve : Jeu de règles Cedar/Rego versionné et tests unitaires associés.
- **`S-10`** (grille `S`, `Conditionnel`) : Approbation hors bande asynchrone (CIBA) activée pour les actions à haut risque. Preuve : Démonstration de suspension/reprise signée (profil CIBA non normalisé).
- **`S-11`** (grille `S`, `BLOQUANT`) : Exécution de tout code ou script dynamique en bac à sable isolé (OpenSandbox/microVM). Preuve : Spécification prouvant l'absence de privilèges hôte et de sortie libre.
- **`S-12`** (grille `S`, `Élevée`) : Protection contre l'empoisonnement de la mémoire partagée (ASI06) et validation d'écriture. Preuve : Politique de validation et approbation avant écriture mémoire.
- **`S-13`** (grille `S`, `Conditionnel`) : Chiffrement mutuel et intégrité des messages inter-agents (mTLS ; SLIM/MLS optionnel). Preuve : Politique mTLS interdisant le clair (MLS = RFC 9420 ; SLIM = transport AGNTCY en évolution).
- **`S-14`** (grille `S`, `BLOQUANT`) : Coupe-circuit centralisé du SOC, révoquant jetons et sessions en < 10 secondes. Preuve : Procès-verbal d'exercice de déclenchement du coupe-circuit.
- **`S-15`** (grille `S`, `BLOQUANT`) : Validation de la séparation des tâches sur les flux financiers/sensibles. Preuve : Preuve qu'aucun identifiant NHI unique ne peut instruire et approuver seul.
- **`R-01`** (grille `R`, `BLOQUANT`) : Inviolabilité des systèmes d'enregistrement (passage exclusif par des API/BAPI métiers validées). Preuve : Revue des connecteurs confirmant l'absence d'écriture SQL directe.
- **`R-02`** (grille `R`, `Conditionnel`) : Ancrage de tout flux multi-étapes mutatif dans un moteur durable (Temporal/Restate). Preuve : Code source distinguant logique déterministe et activités (si flux long).
- **`R-03`** (grille `R`, `BLOQUANT`) : Clé d'idempotence déterministe transmise et honorée sur chaque outil à effet de bord. Preuve : Test de double envoi prouvant l'absence de doublon métier.
- **`R-04`** (grille `R`, `Conditionnel`) : Compteur dur de sauts restants (`maxRemainingHops`) dans l'enveloppe d'action. Preuve : Test unitaire d'arrêt à épuisement du TTL (si délégation multi-agents).
- **`R-05`** (grille `R`, `Élevée`) : Détection des boucles circulaires inter-plateformes SaaS par vecteur de corrélation. Preuve : Test croisé entre deux orchestrateurs simulant un renvoi mutuel.
- **`R-06`** (grille `R`, `BLOQUANT`) : Définition explicite d'une action de compensation Saga ou d'un bail TTL par mutation. Preuve : Matrice des étapes de la saga et test automatisé de retour arrière.
- **`R-07`** (grille `R`, `BLOQUANT`) : Tampon de pré-engagement (fenêtre de grâce ou approbation) devant toute action irréversible. Preuve : Architecture du connecteur courriel/paiement/publication externe.
- **`R-08`** (grille `R`, `Élevée`) : Revalidation des préconditions métiers et des droits IAM au réveil d'une pause longue (T4). Preuve : Scénario de test simulant une révocation d'accès pendant l'attente.
- **`R-09`** (grille `R`, `Moyenne`) : Retour d'erreurs structurées et exploitables cognitivement par les serveurs MCP. Preuve : Catalogue des codes d'erreur d'outils (transitoire ou fatal).
- **`R-10`** (grille `R`, `Élevée`) : Politique de réessai avec recul exponentiel et gigue, hors du LLM. Preuve : Configuration de la passerelle et du moteur durable.
- **`R-11`** (grille `R`, `Élevée`) : Mode dégradé déterministe documenté en cas d'indisponibilité du fournisseur de modèle. Preuve : Test de bascule multi-fournisseurs ou de routage vers une file humaine.
- **`R-12`** (grille `R`, `Conditionnel`) : Confinement des agents d'utilisation d'interface graphique (CUA), avec assertions visuelles. Preuve : Harnais de sécurité CUA (uniquement si CUA employé).
- **`R-13`** (grille `R`, `Conditionnel`) : Validation sur jumeau numérique déterministe avant toute consigne vers l'univers OT. Preuve : Rapport de test du sas IT/OT (uniquement si périmètre OT ; ch. 12 et ch. 14).
- **`R-14`** (grille `R`, `BLOQUANT`) : Cloisonnement multilocataire du contexte et des caches d'inférence. Preuve : Test d'étanchéité inter-clients / inter-divisions sous charge.
- **`R-15`** (grille `R`, `Élevée`) : Campagne d'ingénierie du chaos réussie (latence extrême, erreurs HTTP 429/500, JSON tronqué). Preuve : Rapport d'exécution du harnais de chaos sans corruption d'état.
- **`O-01`** (grille `O`, `Conditionnel`) : Émission de traces distribuées (conventions OpenTelemetry `gen_ai.*`, statut *Development*). Preuve : Visualisation d'une trace complète (schéma OTel évolutif, ch. 22).
- **`O-02`** (grille `O`, `BLOQUANT`) : Caviardage ou masquage automatique des renseignements personnels (PII) avant export OTel. Preuve : Configuration du processeur de filtrage avant export.
- **`O-03`** (grille `O`, `Élevée`) : Versionnage SemVer + Intent du code, des instructions, du modèle, des schémas et politiques. Preuve : Manifeste de version immuable dans le dépôt Git et le registre.
- **`O-04`** (grille `O`, `Conditionnel`) : Suite de simulation multi-tours représentative (dont cas adversariaux). Preuve : Dossier de scénarios versionné (taille calibrée par criticité).
- **`O-05`** (grille `O`, `Conditionnel`) : Seuil de constance pass^k atteint (k ≥ 5) sur les invariants métiers critiques. Preuve : Rapport CI/CD affichant pass^5 au seuil fixé dans l'ADR.
- **`O-06`** (grille `O`, `Élevée`) : Détection automatique en temps réel des boucles sémantiques (verrouillages actifs répétitifs). Preuve : Règle d'alerte et d'interruption configurée sur la télémétrie.
- **`O-07`** (grille `O`, `Élevée`) : Procédure de déploiement progressif (mode fantôme, puis canari à 1–5 %). Preuve : Routage pondéré et critères de retour arrière.
- **`O-08`** (grille `O`, `Élevée`) : Retour arrière automatisé vers la version N-1 stable (cible `< 2 min`). Preuve : Journal d'un test de retour arrière déclenché sur anomalie.
- **`O-09`** (grille `O`, `BLOQUANT`) : Enveloppe budgétaire maximale en devises (`maxTotalCostCad`) active par transaction/saga. Preuve : Test démontrant l'arrêt propre au dépassement du plafond FinOps.
- **`O-10`** (grille `O`, `Moyenne`) : Routage cognitif hybride privilégiant les SLM pour l'extraction et le triage. Preuve : Répartition mesurée des appels par palier de modèle.
- **`O-11`** (grille `O`, `Moyenne`) : Optimisation et mesure du taux de réutilisation du préfixe / KV-cache inter-tours. Preuve : Tableau de bord TTFT et ratio de jetons en cache.
- **`O-12`** (grille `O`, `Élevée`) : Imputation analytique des coûts par unité d'affaires, processus et client. Preuve : Étiquettes FinOps (affichage avant refacturation, ch. 24 / Tome 1 §40.2).
- **`O-13`** (grille `O`, `Élevée`) : Définition formelle de l'événement métier de succès pour calculer le coût par résultat. Preuve : Formule analytique reliant coût technique et résultat validé.
- **`O-14`** (grille `O`, `Élevée`) : Surveillance continue de la dérive sémantique et du taux d'escalade. Preuve : Tableau de bord AgentOps hebdomadaire avec seuils d'alerte.
- **`O-15`** (grille `O`, `Moyenne`) : Protocole de décommissionnement propre (révocation NHI, archivage, redirection). Preuve : Procédure d'extinction d'agent validée par l'équipe plateforme.
- **`G-01`** (grille `G`, `BLOQUANT`) : Propriétaire métier nominatif désigné. Preuve : Fiche de responsabilité au registre d'agents d'entreprise.
- **`G-02`** (grille `G`, `Élevée`) : Inscription au système de management de l'IA conforme à ISO/IEC 42001. Preuve : Fiche d'impact, analyse de risques et cycle PDCA.
- **`G-03`** (grille `G`, `BLOQUANT`) : Qualification réglementaire de l'empreinte de déploiement. Preuve : Grille qualifiant tous les systèmes aval connectés.
- **`G-04`** (grille `G`, `Conditionnel`) : Conformité BSIF/OSFI E-23 (échéance 1ᵉʳ mai 2027). Preuve : Cote de matérialité et validation (si institution fédérale canadienne).
- **`G-05`** (grille `G`, `BLOQUANT`) : Évaluation des facteurs relatifs à la vie privée (ÉFVP — Loi 25 / RGPD). Preuve : Dossier ÉFVP et cartographie des flux transfrontaliers.
- **`G-06`** (grille `G`, `BLOQUANT`) : Mécanisme d'information, d'explication et de révision (Loi 25 art. 12.1). Preuve : Parcours testé lorsqu'une décision exclusivement automatisée s'applique.
- **`G-07`** (grille `G`, `BLOQUANT`) : Divulgation de l'interaction avec une IA (EU AI Act art. 50, 2 août 2026). Preuve : Mention explicite dans les interfaces, voix et courriels (si périmètre UE).
- **`G-08`** (grille `G`, `Conditionnel`) : Dossier technique et supervision renforcée si haut risque (EU AI Act Annexe III). Preuve : Documentation technique (si cas d'usage Annexe III, déc. 2027).
- **`G-09`** (grille `G`, `Moyenne`) : Alignement sémantique des concepts critiques (Apache Ossie `0.1.1` optionnel, en incubation). Preuve : Dictionnaire de métriques gouverné (ne rien bâtir sur `0.3.0.dev0`, ch. 10).
- **`G-10`** (grille `G`, `BLOQUANT`) : Droit à l'effacement et purge sélective vérifiable dans la mémoire à long terme. Preuve : Test d'oubli d'une entité sans dégradation résiduelle.
- **`G-11`** (grille `G`, `Élevée`) : Ergonomie HOTL présentant les preuves contradictoires (prévention ASI09). Preuve : Revue d'interface d'approbation sans incitation biaisée.
- **`G-12`** (grille `G`, `Moyenne`) : Dispositif périodique de maintien de vigilance des superviseurs (HOTL). Preuve : Dossiers tests d'étalonnage et suivi du temps de revue.
- **`G-13`** (grille `G`, `Conditionnel`) : Plafonds et mandats signés (p. ex. AP2) pour toute transaction commerciale B2B. Preuve : Politique de délégation de signature financière et mandats SD-JWT.
- **`G-14`** (grille `G`, `Conditionnel`) : Garde-fous anti-collusion algorithmique sur les agents de prix ou d'enchères. Preuve : Audit des consignes et journaux (si tarification ou enchères).
- **`G-15`** (grille `G`, `BLOQUANT`) : Archivage immuable et horodaté (WORM) des décisions critiques. Preuve : Politique de rétention conforme aux délais légaux.
- **`F-01`** (grille `F`, `Conditionnel`) : Authentification légale vLEI et contrat d'usage ODRL 2.2 sur canal B2B. Preuve : Accord EDC et test de rejet non signé (si fédération B2B).
- **`F-02`** (grille `F`, `Conditionnel`) : Scission entre l'agent diplomate B2B et l'évaluateur interne (aucun secret en DMZ). Preuve : Revue d'architecture et test d'extraction (si négociation B2B).
- **`F-03`** (grille `F`, `Conditionnel`) : Rapprochement tripartite déterministe (Cedar) avant libération AP2 / x402. Preuve : Test d'intégration couvrant écarts (si règlement agentique B2B).
- **`F-04`** (grille `F`, `BLOQUANT`) : Résidence juridictionnelle vérifiée des couches d'état (ch. 12 et ch. 26 / Tome 3 §46.1–46.9). Preuve : Matrice de géorepérage pour les classes C2 (Loi 25) et C3 (E-23).
- **`F-05`** (grille `F`, `Élevée`) : Clés de chiffrement d'état et de pseudonymisation détenues localement (HYOK en HSM). Preuve : Preuve de révocation d'accès HSM rendant les journaux illisibles.
- **`F-06`** (grille `F`, `Conditionnel`) : Attestation matérielle distante CPU+GPU (TEE) avant déchiffrement de charge C3. Preuve : Politique PCR du vérificateur (si charge C3 sur enclave distante).
- **`F-07`** (grille `F`, `Conditionnel`) : Profil de secours à poids ouverts testé (cible de conception `RTO < 15 min`). Preuve : Compte rendu d'exercice de coupure primaire (RTO calibré par SLA).
- **`F-08`** (grille `F`, `Conditionnel`) : Survie hors ligne en périphérie (durée calibrée par site, cible 72 h) et baux CRDT. Preuve : Rapport d'essai WAN coupé sans double dépense (si site isolé).
- **`F-09`** (grille `F`, `Conditionnel`) : Enveloppe matérielle Simplex (`ISO 10218-1:2025` / IEC 61508) sur pont MCP ↔︎ ROS 2. Preuve : Homologation sécurité machine (uniquement si robotique mobile).
- **`F-10`** (grille `F`, `Conditionnel`) : Distribution signée TUF/Sigstore à double clé en périphérie, avec bascule A/B. Preuve : Test de rejet d'archive altérée ou expirée (si flotte périphérique).
- **`F-11`** (grille `F`, `Conditionnel`) : Séparation des devoirs dans l'usine logicielle (bâtisseur interdit sur les tests d'or). Preuve : Règles Git et confinement bac de compilation (si usine ADLC).
- **`F-12`** (grille `F`, `Conditionnel`) : Porte de mutation et parité en exécution miroir (cibles 85 % / 30 j calibrées par ADR). Preuve : Rapport de parité dans le seuil de tolérance fixé par l'ADR (si refonte).
- **`F-13`** (grille `F`, `Élevée`) : Contrats de données ODCS `v3.2.0` et Write-Audit-Publish (données) + contrôle pré-DDL (schéma). Preuve : Test de gel WAP sur dérive PSI et rejet pré-DDL sur rupture de schéma.
- **`F-14`** (grille `F`, `BLOQUANT`) : Confinement du SRE autonome (lecture seule assainie, aucun shell libre, budget Cedar R1/R2 + H0). Preuve : Politique Cedar interdisant shell libre et arbitre avec hypothèse nulle H0.
- **`F-15`** (grille `F`, `Conditionnel`) : Sas anti-PII à canaris et porte pass^5 ≥ 99 % (cible à valider) avant promotion SLM. Preuve : Test d'exposition (type Carlini) et jeu de réserve (si distillation LoRA).

## 11. Catalogue intégral des 57 spécifications techniques et normatives ouvertes `L+`

- **`SPEC-MCP-2026-07-28-TOOLS`** (`2026-07-28@5f5440bb`, `FINAL_STANDARD`, `MIT`, `SRC-072`) : Model Context Protocol (MCP) Server Tools.
- **`SPEC-MCP-2026-07-28-HTTP`** (`2026-07-28@5f5440bb`, `FINAL_STANDARD`, `MIT`, `SRC-074`) : Model Context Protocol (MCP) Streamable HTTP Transport.
- **`SPEC-MCP-2026-07-28-SEC`** (`2026-07-28@5f5440bb`, `FINAL_STANDARD`, `MIT`, `SRC-078`) : Model Context Protocol (MCP) Authorization Security Considerations.
- **`SPEC-MCP-2026-07-28-SCHEMA`** (`2026-07-28@5f5440bb`, `FINAL_STANDARD`, `MIT`, `SRC-080`) : Model Context Protocol (MCP) TypeScript Schema.
- **`SPEC-MCP-SEP-2596`** (`Final@862397ce`, `FINAL_STANDARD`, `MIT`, `SRC-081`) : MCP SEP-2596 : Feature Lifecycle and Deprecation Policy.
- **`SPEC-MCP-SEP-3398`** (`Accepted@862397ce`, `SPEC_DEVELOPMENT`, `MIT`, `SRC-082`) : MCP SEP-3398 : Release Cycle Updates.
- **`SPEC-A2A-V1-0-1-SPEC`** (`v1.0.1@33035925`, `FINAL_STANDARD`, `Apache-2.0`, `SRC-083`) : Agent2Agent (A2A) Protocol Specification.
- **`SPEC-A2A-V1-0-1-PROTO`** (`v1.0.1@33035925`, `FINAL_STANDARD`, `Apache-2.0`, `SRC-084`) : Agent2Agent (A2A) Protobuf Contract.
- **`SPEC-A2A-V1-1-0-RC`** (`v1.1.0-rc@78e1d6a1`, `RC_OR_ALPHA`, `Apache-2.0`, `SRC-085`) : Agent2Agent (A2A) Specification Release Candidate.
- **`SPEC-A2A-TCK-ALPHA3`** (`1.0.0.alpha3@5daf0144`, `RC_OR_ALPHA`, `Apache-2.0`, `SRC-086`) : A2A Technology Compatibility Kit (a2a-tck).
- **`SPEC-OPA-REGO-V1-22-4`** (`v1.22.4@ba39415d`, `FINAL_STANDARD`, `Apache-2.0`, `SRC-087`) : Open Policy Agent (OPA) Rego Language Reference.
- **`SPEC-OPA-TEST-V1-22-4`** (`v1.22.4@ba39415d`, `FINAL_STANDARD`, `Apache-2.0`, `SRC-088`) : Open Policy Agent (OPA) Policy Testing & Coverage.
- **`SPEC-OTEL-V1-41-0`** (`v1.41.0@e018fe6f`, `FINAL_STANDARD`, `Apache-2.0`, `SRC-089`) : OpenTelemetry Semantic Conventions GenAI Registry.
- **`SPEC-OTEL-GENAI-DEV-85`** (`244465e9@2026-10-31`, `SPEC_DEVELOPMENT`, `Apache-2.0`, `SRC-090`) : OpenTelemetry semantic-conventions-genai (85 attributs Development).
- **`SPEC-OTEL-AGENT-SPANS`** (`2026-11-05@main`, `SPEC_DEVELOPMENT`, `Apache-2.0`, `SRC-037`) : OpenTelemetry GenAI Agent and Framework Spans.
- **`SPEC-FOCUS-V1-4`** (`v1.4`, `FINAL_STANDARD`, `CC-BY-4.0`, `SRC-023`) : FinOps Open Cost and Usage Specification (FOCUS).
- **`SPEC-JSON-SCHEMA-2020-12`** (`2020-12`, `FINAL_STANDARD`, `BSD-3-Clause`, `SRC-021`) : JSON Schema Draft 2020-12 Core (draft-bhutton-json-schema-01).
- **`SPEC-CLOUDEVENTS-1-0-2`** (`v1.0.2`, `FINAL_STANDARD`, `Apache-2.0`, `SRC-035`) : CloudEvents Specification.
- **`SPEC-RFC-7493-IJSON`** (`RFC 7493`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-004`) : RFC 7493 : The I-JSON Message Format.
- **`SPEC-RFC-7515-JWS`** (`RFC 7515`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-005`) : RFC 7515 : JSON Web Signature (JWS).
- **`SPEC-RFC-8032-EDDSA`** (`RFC 8032`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-076`) : RFC 8032 : Edwards-Curve Digital Signature Algorithm (EdDSA).
- **`SPEC-RFC-8693-OBO`** (`RFC 8693`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-041`) : RFC 8693 : OAuth 2.0 Token Exchange.
- **`SPEC-RFC-8707-RESIND`** (`RFC 8707`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-009`) : RFC 8707 : Resource Indicators for OAuth 2.0.
- **`SPEC-RFC-8785-JCS`** (`RFC 8785`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-077`) : RFC 8785 : JSON Canonicalization Scheme (JCS).
- **`SPEC-RFC-9334-RATS`** (`RFC 9334 (Informational)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-010`) : RFC 9334 : Remote ATtestation procedureS (RATS) Architecture.
- **`SPEC-RFC-9396-RAR`** (`RFC 9396`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-042`) : RFC 9396 : OAuth 2.0 Rich Authorization Requests (RAR).
- **`SPEC-RFC-9449-DPOP`** (`RFC 9449`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-043`) : RFC 9449 : OAuth 2.0 Demonstrating Proof of Possession (DPoP).
- **`SPEC-RFC-9943-SCITT`** (`RFC 9943`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-044`) : RFC 9943 : Supply Chain Integrity, Transparency, and Trust (SCITT) Architecture.
- **`SPEC-RFC-9964-MLDSA`** (`RFC 9964`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-012`) : RFC 9964 : ML-DSA for JOSE and COSE.
- **`SPEC-DRAFT-TXTOKENS-11`** (`draft-ietf-oauth-transaction-tokens-11`, `IETF_WORKING_GROUP_DRAFT`, `IETF-Trust`, `SRC-013`) : OAuth Transaction Tokens (Internet-Draft).
- **`SPEC-DRAFT-AGENT-REVOC-01`** (`draft-chen-oauth-agent-revocation-01`, `IETF_INDIVIDUAL_DRAFT`, `IETF-Trust`, `SRC-017`) : OAuth 2.0 Agent Authorization Explicit Revocation (Internet-Draft).
- **`SPEC-DRAFT-WIMSE-PRAC-08`** (`draft-ietf-wimse-workload-identity-practices-08`, `IETF_WORKING_GROUP_DRAFT`, `IETF-Trust`, `SRC-047`) : WIMSE Workload Identity Practices (Internet-Draft).
- **`SPEC-DRAFT-WIMSE-AIMS-01`** (`draft-ietf-wimse-aims-01`, `IETF_WORKING_GROUP_DRAFT`, `IETF-Trust`, `SRC-048`) : WIMSE AI Identity Management System (Internet-Draft).
- **`SPEC-DRAFT-IDEMPOTENCY-KEY`** (`draft-ietf-httpapi-idempotency-key-header-09`, `IETF_WORKING_GROUP_DRAFT`, `IETF-Trust`, `SRC-036`) : The Idempotency-Key HTTP Header Field (Internet-Draft).
- **`SPEC-NIST-FIPS-203`** (`FIPS 203`, `FIPS_STANDARD`, `NIST-PD`, `SRC-049`) : NIST FIPS 203 : ML-KEM Key-Encapsulation Mechanism.
- **`SPEC-NIST-FIPS-204`** (`FIPS 204`, `FIPS_STANDARD`, `NIST-PD`, `SRC-050`) : NIST FIPS 204 : ML-DSA Digital Signature Standard.
- **`SPEC-NIST-FIPS-205`** (`FIPS 205`, `FIPS_STANDARD`, `NIST-PD`, `SRC-018`) : NIST FIPS 205 : SLH-DSA Stateless Hash-Based Signature Standard.
- **`SPEC-OPENID-CIBA-1-0`** (`1.0`, `FINAL_STANDARD`, `OIDF-Spec`, `SRC-045`) : OpenID Connect Client-Initiated Backchannel Authentication Core 1.0.
- **`SPEC-OPENID-SSF-1-0`** (`1.0`, `FINAL_STANDARD`, `OIDF-Spec`, `SRC-019`) : OpenID Shared Signals Framework Specification 1.0.
- **`SPEC-OPENID-CAEP-1-0`** (`1.0`, `FINAL_STANDARD`, `OIDF-Spec`, `SRC-020`) : OpenID Continuous Access Evaluation Profile (CAEP) 1.0.
- **`SPEC-REG-EU-AI-ACT-2024-1689`** (`(UE) 2024/1689 + (UE) 2026/1744`, `REGULATION_IN_FORCE`, `EU-Public-Domain`, `SRC-060`) : Règlement (UE) 2024/1689 sur l'intelligence artificielle (EU AI Act).
- **`SPEC-REG-EN-18286-2026`** (`(UE) 2026/2274`, `REGULATION_IN_FORCE`, `EU-Public-Domain`, `SRC-067`) : Décision d'exécution (UE) 2026/2274 — Norme harmonisée EN 18286:2026 (QMS Art. 17).
- **`SPEC-REG-DORA-2022-2554`** (`(UE) 2022/2554`, `REGULATION_IN_FORCE`, `EU-Public-Domain`, `SRC-062`) : Règlement (UE) 2022/2554 sur la résilience opérationnelle numérique (DORA).
- **`SPEC-REG-QC-LOI25-2021-C25`** (`LQ 2021, c. 25`, `REGULATION_IN_FORCE`, `QC-Public-Domain`, `SRC-063`) : LQ 2021, c. 25 — Loi modernisant la protection des renseignements personnels (Loi 25).
- **`SPEC-REG-BSIF-E23-2027`** (`E-23 (eff. 2027-05-01)`, `REGULATION_ADOPTED_FUTURE`, `Canada-OGL`, `SRC-065`) : BSIF / OSFI Ligne directrice E-23 — Gestion du risque de modélisation.
- **`SPEC-REG-BSIF-B10-2023`** (`B-10 (2023)`, `REGULATION_IN_FORCE`, `Canada-OGL`, `SRC-068`) : BSIF / OSFI Guideline B-10 — Third-Party Risk Management.
- **`SPEC-RFC-2119`** (`RFC 2119 (1997-03)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-125`) : RFC 2119 : Key words for use in RFCs to Indicate Requirement Levels.
- **`SPEC-RFC-6902`** (`RFC 6902 (2013-04)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-126`) : RFC 6902 : JavaScript Object Notation (JSON) Patch.
- **`SPEC-RFC-8555`** (`RFC 8555 (2019-03)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-127`) : RFC 8555 : Automatic Certificate Management Environment (ACME).
- **`SPEC-RFC-8705`** (`RFC 8705 (2020-02)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-128`) : RFC 8705 : OAuth 2.0 Mutual-TLS Client Authentication.
- **`SPEC-RFC-9207`** (`RFC 9207 (2022-03)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-129`) : RFC 9207 : OAuth 2.0 Authorization Server Issuer Identification.
- **`SPEC-RFC-9420`** (`RFC 9420 (2023-07)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-130`) : RFC 9420 : The Messaging Layer Security (MLS) Protocol.
- **`SPEC-RFC-9421`** (`RFC 9421 (2024-02)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-131`) : RFC 9421 : HTTP Message Signatures.
- **`SPEC-RFC-9562`** (`RFC 9562 (2024-05)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-132`) : RFC 9562 : Universally Unique IDentifiers (UUIDs / UUIDv7).
- **`SPEC-RFC-9700`** (`RFC 9700 (2025-01)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-133`) : RFC 9700 : Best Current Practice for OAuth 2.0 Security (BCP 240).
- **`SPEC-RFC-9728`** (`RFC 9728 (2025-04)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-134`) : RFC 9728 : OAuth 2.0 Protected Resource Metadata.
- **`SPEC-RFC-9745`** (`RFC 9745 (2025-04)`, `FINAL_STANDARD`, `IETF-Trust`, `SRC-135`) : RFC 9745 : The Deprecation HTTP Response Header Field.

## 12. Matrice exécutable complète (`95` liaisons `G0`, extraits `CA-G0-SYNC`, grille unifiée `C1` et portefeuille `DAPP`)

### Liaisons exécutables `G0` par exigence et contrôle `PRR`

- **`S-01`** (`PRR_BLOCKING`, `BLOQUANT`, `ch17`) → `authz_pqc_audit.obo_dpop.validate_obo_delegation` (`tests/test_authz_pqc_audit.py::test_nhi_unique_identity_required`).
- **`S-03`** (`PRR_BLOCKING`, `BLOQUANT`, `ch17`) → `authz_pqc_audit.obo_dpop.extract_act_chain` (`tests/test_authz_pqc_audit.py::test_obo_sub_and_act_chain_max_two_hops`).
- **`S-06`** (`PRR_BLOCKING`, `BLOQUANT`, `ch20`) → `policy_saga.opa_runner.OpaPolicyEngine.evaluate` (`tests/test_policy_saga.py::test_rule_of_two_interface_vs_write_separation`).
- **`S-08`** (`PRR_BLOCKING`, `BLOQUANT`, `ch20`) → `policy_saga.taint_camel.delegate_taint_envelope` (`tests/test_policy_saga.py::test_camel_taint_propagation_across_agents`).
- **`S-09`** (`PRR_BLOCKING`, `BLOQUANT`, `ch20`) → `policy_saga.opa_runner.verify_rego_default_deny` (`tests/test_policy_saga.py::test_opa_default_deny_before_mutative_tool`).
- **`S-11`** (`PRR_BLOCKING`, `BLOQUANT`, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest` (`tests/test_policy_saga.py::test_sandbox_manifest_no_kvm_enforced`).
- **`S-14`** (`PRR_BLOCKING`, `BLOQUANT`, `ch17`) → `authz_pqc_audit.revocation_fsm.RevocationStateMachine` (`tests/test_authz_pqc_audit.py::test_soc_killswitch_caep_revocation_terminal`).
- **`S-15`** (`PRR_BLOCKING`, `BLOQUANT`, `ch17`) → `authz_pqc_audit.ciba_approval.verify_ciba_approval_tokens` (`tests/test_authz_pqc_audit.py::test_reject_self_approval_by_principal_sub`).
- **`R-01`** (`PRR_BLOCKING`, `BLOQUANT`, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run` (`tests/test_harness_proto.py::test_harness_enforces_schema_and_grounding`).
- **`R-03`** (`PRR_BLOCKING`, `BLOQUANT`, `ch15`) → `policy_saga.saga_orchestrator.compute_idempotency_key` (`tests/test_saga_10_faults.py::test_fault_03_lost_response_idempotent_replay`).
- **`R-06`** (`PRR_BLOCKING`, `BLOQUANT`, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator` (`tests/test_saga_10_faults.py::test_fault_01_step_t2_compensates_c1`).
- **`R-07`** (`PRR_BLOCKING`, `BLOQUANT`, `ch17`) → `authz_pqc_audit.ciba_approval.compute_action_hash_h` (`tests/test_authz_pqc_audit.py::test_ciba_c6_action_hash_exact_match`).
- **`R-14`** (`PRR_BLOCKING`, `BLOQUANT`, `ch20`) → `policy_saga.taint_camel.SessionTaintTracker` (`tests/test_policy_saga.py::test_multitenant_context_taint_isolation`).
- **`O-02`** (`PRR_BLOCKING`, `BLOQUANT`, `ch22`) → `authz_pqc_audit.otel_pii_mapper.redact_pii_bilingual` (`tests/test_authz_pqc_audit.py::test_pii_redaction_bilingual_and_drop_raw_content`).
- **`O-09`** (`PRR_BLOCKING`, `BLOQUANT`, `ch24`) → `authz_pqc_audit.audit_scitt_focus.compute_cpo_and_focus` (`tests/test_authz_pqc_audit.py::test_focus_cpo_and_budget_ceiling_decimal`).
- **`G-01`** (`PRR_BLOCKING`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001` (`tests/test_evalops_prr.py::test_adr_2027_b001_requires_agent_owner`).
- **`G-03`** (`PRR_BLOCKING`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001` (`tests/test_evalops_prr.py::test_adr_2027_b001_regulatory_footprint`).
- **`G-05`** (`PRR_BLOCKING`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking` (`tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete`).
- **`G-06`** (`PRR_BLOCKING`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking` (`tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete`).
- **`G-07`** (`PRR_BLOCKING`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking` (`tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete`).
- **`G-10`** (`PRR_BLOCKING`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking` (`tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete`).
- **`G-15`** (`PRR_BLOCKING`, `BLOQUANT`, `ch24`) → `authz_pqc_audit.audit_scitt_focus.AuditChainLedger` (`tests/test_authz_pqc_audit.py::test_audit_chain_jcs_and_scitt_merkle_seal`).
- **`F-04`** (`PRR_BLOCKING`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking` (`tests/test_evalops_prr.py::test_prr_24_blocking_gates_complete`).
- **`F-14`** (`PRR_BLOCKING`, `BLOQUANT`, `ch20`) → `policy_saga.opa_runner.OpaPolicyEngine.evaluate` (`tests/test_policy_saga.py::test_sre_confinement_read_only_no_shell`).
- **`SBB-SECRETS-VAULT`** (`SBB`, `OBLIGATOIRE`, `ch17`) → `authz_pqc_audit.obo_dpop.validate_obo_delegation` (`tests/test_authz_pqc_audit.py::test_no_static_secret_or_passthrough`).
- **`SBB-GUARDRAILS-ENGINE`** (`SBB`, `BLOQUANT`, `ch20`) → `policy_saga.opa_runner.OpaPolicyEngine` (`tests/test_policy_saga.py::test_opa_coverage_100_percent`).
- **`SBB-SIGNED-HUMAN-APPROVAL`** (`SBB`, `BLOQUANT`, `ch17`) → `authz_pqc_audit.ciba_approval.verify_ciba_approval_tokens` (`tests/test_authz_pqc_audit.py::test_ciba_approval_token_valid_and_single_use`).
- **`SBB-IMMUTABLE-AUDIT-LEDGER`** (`SBB`, `BLOQUANT`, `ch24`) → `authz_pqc_audit.audit_scitt_focus.AuditChainLedger` (`tests/test_authz_pqc_audit.py::test_audit_chain_tamper_detection`).
- **`SBB-FINOPS-BUDGET-QUOTA`** (`SBB`, `BLOQUANT`, `ch12`) → `policy_saga.decimal_money.from_decimal_str` (`tests/test_policy_saga.py::test_decimal_rejects_float_budget`).
- **`2027-B001`** (`ADR_TEMPLATE`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001` (`tests/test_evalops_prr.py::test_adr_2027_b001_schema_validation`).
- **`CAP-046`** (`CAP`, `RECOMMANDE`, `ch24`) → `authz_pqc_audit.audit_scitt_focus.compute_cpo_and_focus` (`tests/test_authz_pqc_audit.py::test_focus_carbon_cap046_fields`).
- **`EXIG-MCP-03`** (`EXIG`, `OBLIGATOIRE`, `ch07`) → `harness_proto.mcp_pinning.verify_tools_list_against_catalog` (`tests/test_harness_proto.py::test_mcp_tools_list_deterministic_sort_and_cache`).
- **`EXIG-MCP-11`** (`EXIG`, `BLOQUANT`, `ch17`) → `authz_pqc_audit.obo_dpop.validate_obo_delegation` (`tests/test_authz_pqc_audit.py::test_reject_token_passthrough`).
- **`EXIG-MCP-15`** (`EXIG`, `BLOQUANT`, `ch07`) → `harness_proto.mcp_pinning.validate_mcp_headers` (`tests/test_harness_proto.py::test_mcp_header_mismatch_raises_400_32020`).
- **`EXIG-MCP-16`** (`EXIG`, `OBLIGATOIRE`, `ch07`) → `harness_proto.mcp_pinning.validate_mcp_headers` (`tests/test_harness_proto.py::test_mcp_meta_allowlist_purges_unreserved`).
- **`EXIG-MCP-18`** (`EXIG`, `BLOQUANT`, `ch07`) → `harness_proto.mcp_pinning.validate_mcp_headers` (`tests/test_harness_proto.py::test_reject_x_mcp_header_pii_or_token`).
- **`EXIG-MCP-19`** (`EXIG`, `BLOQUANT`, `ch04`) → `harness_proto.pipeline.validate_strict_schema` (`tests/test_harness_proto.py::test_reject_external_network_schema_ref`).
- **`EXIG-MCP-20`** (`EXIG`, `BLOQUANT`, `ch07`) → `harness_proto.mcp_pinning.compute_tool_definition_digest` (`tests/test_harness_proto.py::test_mcp_rug_pull_single_char_drift_suspends`).
- **`EXIG-A2A-03`** (`EXIG`, `BLOQUANT`, `ch08`) → `harness_proto.a2a_card.validate_agent_card` (`tests/test_harness_proto.py::test_a2a_agent_card_jws_es256_and_pinned_jku`).
- **`EXIG-OBS-06`** (`EXIG`, `OBLIGATOIRE`, `ch22`) → `authz_pqc_audit.otel_pii_mapper.map_span_attributes` (`tests/test_authz_pqc_audit.py::test_otel_rejects_generic_enterprise_prefix`).
- **`EXIG-OBS-07`** (`EXIG`, `BLOQUANT`, `ch22`) → `authz_pqc_audit.otel_pii_mapper.map_span_attributes` (`tests/test_authz_pqc_audit.py::test_otel_drops_raw_prompt_and_tool_payloads`).
- **`EXIG-OBS-09`** (`EXIG`, `BLOQUANT`, `ch22`) → `authz_pqc_audit.otel_pii_mapper.redact_pii_bilingual` (`tests/test_authz_pqc_audit.py::test_otel_pii_redaction_and_closed_allowlist`).
- **`EXIG-OBS-12`** (`EXIG`, `BLOQUANT`, `ch24`) → `authz_pqc_audit.audit_scitt_focus.AuditChainLedger.append_record` (`tests/test_authz_pqc_audit.py::test_c8_five_element_canonized_record`).
- **`EXIG-SEC-06`** (`EXIG`, `BLOQUANT`, `ch20`) → `policy_saga.opa_runner.OpaPolicyEngine.evaluate` (`tests/test_policy_saga.py::test_rule_of_two_denies_untrusted_plus_exfiltration`).
- **`EXIG-SEC-12`** (`EXIG`, `BLOQUANT`, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest` (`tests/test_policy_saga.py::test_sandbox_denies_egress_and_iana_ranges`).
- **`EXIG-SEC-13`** (`EXIG`, `BLOQUANT`, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest` (`tests/test_policy_saga.py::test_sandbox_blocks_imds_169_254_169_254`).
- **`EXIG-SEC-14`** (`EXIG`, `BLOQUANT`, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest` (`tests/test_policy_saga.py::test_sandbox_rejects_env_secrets`).
- **`EXIG-SEC-15`** (`EXIG`, `OBLIGATOIRE`, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest` (`tests/test_policy_saga.py::test_sandbox_three_level_timeouts`).
- **`EXIG-SEC-24`** (`EXIG`, `BLOQUANT`, `ch23`) → `evalops_prr.metamorphic.verify_metamorphic_pair` (`tests/test_evalops_prr.py::test_bilingual_fr_en_attack_suite_100_cases`).
- **`EXIG-SEC-25`** (`EXIG`, `BLOQUANT`, `ch20`) → `policy_saga.opa_runner.OpaPolicyEngine.run_coverage` (`tests/test_policy_saga.py::test_deterministic_controls_opa_100_coverage`).
- **`EXIG-ORC-18`** (`EXIG`, `BLOQUANT`, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator` (`tests/test_saga_10_faults.py::test_fault_08_two_comp_failures_escalate`).
- **`EXIG-ORC-20`** (`EXIG`, `BLOQUANT`, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator` (`tests/test_saga_10_faults.py::test_saga_all_10_deterministic_faults`).
- **`EXIG-ORC-28`** (`EXIG`, `BLOQUANT`, `ch15`) → `policy_saga.saga_orchestrator.CompensationChannel` (`tests/test_saga_10_faults.py::test_fault_10_isolated_compensation_channel`).
- **`EXIG-EVA-03`** (`EXIG`, `BLOQUANT`, `ch23`) → `evalops_prr.wilson_bounds.evaluate_wilson_gate` (`tests/test_evalops_prr.py::test_wilson_3p_independent_scenarios_gate`).
- **`EXIG-AMF-11`** (`EXIG`, `OBLIGATOIRE`, `ch23`) → `evalops_prr.metamorphic.verify_metamorphic_pair` (`tests/test_evalops_prr.py::test_bilingual_fr_en_fairness_and_non_avis_gate`).
- **`C01`** (`C40`, `OBLIGATOIRE`, `ch04`) → `harness_proto.pipeline.DeterministicHarness` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C02`** (`C40`, `OBLIGATOIRE`, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C03`** (`C40`, `BLOQUANT`, `ch20`) → `policy_saga.opa_runner.OpaPolicyEngine` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C04`** (`C40`, `RECOMMANDE`, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C05`** (`C40`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C06`** (`C40`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C07`** (`C40`, `RECOMMANDE`, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C08`** (`C40`, `RECOMMANDE`, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C09`** (`C40`, `BLOQUANT`, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run` (`tests/test_harness_proto.py::test_harness_partition_80_20_rules_outside_prompt`).
- **`C10`** (`C40`, `BLOQUANT`, `ch04`) → `harness_proto.pipeline.validate_strict_schema` (`tests/test_harness_proto.py::test_strict_json_schema_2020_12`).
- **`C11`** (`C40`, `BLOQUANT`, `ch07`) → `harness_proto.mcp_pinning.StreamableHttpAdapter` (`tests/test_harness_proto.py::test_mcp_streamable_http_and_pinning`).
- **`C12`** (`C40`, `OBLIGATOIRE`, `ch07`) → `harness_proto.mcp_pinning.verify_tools_list_against_catalog` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C13`** (`C40`, `BLOQUANT`, `ch08`) → `harness_proto.a2a_card.validate_agent_card` (`tests/test_harness_proto.py::test_a2a_agent_card_jws_es256_and_pinned_jku`).
- **`C14`** (`C40`, `RECOMMANDE`, `ch08`) → `harness_proto.a2a_card.validate_agent_card` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C15`** (`C40`, `OBLIGATOIRE`, `ch20`) → `policy_saga.taint_camel.SessionTaintTracker` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C16`** (`C40`, `BLOQUANT`, `ch20`) → `policy_saga.opa_runner.OpaPolicyEngine.evaluate` (`tests/test_policy_saga.py::test_acl_and_asi06_memory_protection`).
- **`C17`** (`C40`, `RECOMMANDE`, `ch23`) → `evalops_prr.mock_mcp_harness.evaluate_trajectory` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C18`** (`C40`, `OBLIGATOIRE`, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest` (`tests/test_policy_saga.py::test_sandbox_three_level_timeouts`).
- **`C19`** (`C40`, `OBLIGATOIRE`, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C20`** (`C40`, `OBLIGATOIRE`, `ch24`) → `authz_pqc_audit.audit_scitt_focus.AuditChainLedger` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C21`** (`C40`, `OBLIGATOIRE`, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C22`** (`C40`, `BLOQUANT`, `ch15`) → `policy_saga.saga_orchestrator.SagaOrchestrator` (`tests/test_saga_10_faults.py::test_fault_02_crash_after_outbox_resumes`).
- **`C23`** (`C40`, `BLOQUANT`, `ch15`) → `policy_saga.saga_orchestrator.compute_idempotency_key` (`tests/test_saga_10_faults.py::test_fault_06_pivot_blocks_backward_compensation`).
- **`C24`** (`C40`, `OBLIGATOIRE`, `ch17`) → `authz_pqc_audit.ciba_approval.verify_ciba_approval_tokens` (`tests/test_authz_pqc_audit.py::test_ciba_approval_token_valid_and_single_use`).
- **`C25`** (`C40`, `BLOQUANT`, `ch20`) → `policy_saga.taint_camel.delegate_taint_envelope` (`tests/test_policy_saga.py::test_camel_taint_propagation_across_agents`).
- **`C26`** (`C40`, `BLOQUANT`, `ch17`) → `authz_pqc_audit.revocation_fsm.RevocationStateMachine` (`tests/test_authz_pqc_audit.py::test_spiffe_nhi_lifecycle_and_revocation`).
- **`C27`** (`C40`, `BLOQUANT`, `ch18`) → `authz_pqc_audit.pqc_http431.evaluate_http_431` (`tests/test_authz_pqc_audit.py::test_pqc_http431_vs_transaction_token_o1`).
- **`C28`** (`C40`, `BLOQUANT`, `ch20`) → `policy_saga.opa_runner.OpaPolicyEngine.evaluate` (`tests/test_policy_saga.py::test_opa_rule_of_two_and_rar_mandate`).
- **`C29`** (`C40`, `BLOQUANT`, `ch21`) → `policy_saga.sandbox_manifest.validate_sandbox_manifest` (`tests/test_policy_saga.py::test_sandbox_manifest_no_kvm_enforced`).
- **`C30`** (`C40`, `OBLIGATOIRE`, `ch22`) → `authz_pqc_audit.otel_pii_mapper.map_span_attributes` (`tests/test_authz_pqc_audit.py::test_otel_v141_to_genai_dev_cache_write_and_join`).
- **`C31`** (`C40`, `BLOQUANT`, `ch23`) → `evalops_prr.mock_mcp_harness.compute_pass_k` (`tests/test_evalops_prr.py::test_mock_mcp_pass_k_consistency_gate`).
- **`C32`** (`C40`, `OBLIGATOIRE`, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C33`** (`C40`, `RECOMMANDE`, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C34`** (`C40`, `OBLIGATOIRE`, `ch04`) → `harness_proto.pipeline.DeterministicHarness.run` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C35`** (`C40`, `OBLIGATOIRE`, `ch34`) → `evalops_prr.prr_validators.validate_adr_2027_b001` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C36`** (`C40`, `OBLIGATOIRE`, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C37`** (`C40`, `BLOQUANT`, `ch34`) → `evalops_prr.prr_validators.validate_prr_24_blocking` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).
- **`C38`** (`C40`, `BLOQUANT`, `ch24`) → `authz_pqc_audit.audit_scitt_focus.seal_merkle_root` (`tests/test_authz_pqc_audit.py::test_scitt_merkle_inclusion_and_slh_dsa_seal`).
- **`C39`** (`C40`, `OBLIGATOIRE`, `ch24`) → `authz_pqc_audit.audit_scitt_focus.compute_cpo_and_focus` (`tests/test_authz_pqc_audit.py::test_focus_cpo_and_budget_ceiling_decimal`).
- **`C40`** (`C40`, `RECOMMANDE`, `ch29`) → `evalops_prr.prr_validators.validate_blueprints_and_c40` (`tests/test_evalops_prr.py::test_blueprints_cover_c01_to_c40`).

### Grille unifiée `EXIG / PRR / Portes` (43 rubriques)

*Note : l'astérisque (`*`) placé hors backticks signale une porte `PRR` bloquante (`24` critères bloquants en `PRR-75`).*

- **`A.2.1`** — Fiche registre et parrain actif : `EXIG-GOV-01, EXIG-GOV-05, EXIG-GOV-06, EXIG-GOV-07, EXIG-GOV-08, EXIG-GOV-09, EXIG-GOV-10, EXIG-GOV-11, EXIG-GOV-13, EXIG-GOV-14` ; PRR : `G-01`* ; Portes : `POR-001, POR-015`.
- **`A.2.2`** — Séparation des fonctions et RACI : `EXIG-GOV-02, EXIG-GOV-03, EXIG-GOV-04` ; PRR : `S-15`*, `F-11` ; Portes : `POR-003, POR-015`.
- **`A.2.3`** — Classe de risque et plafonds : `EXIG-CON-01, EXIG-CON-02, EXIG-AUT-01, EXIG-AUT-02, EXIG-AUT-03, EXIG-AUT-06, EXIG-AUT-07` ; PRR : `G-03`*, `G-04` ; Portes : `POR-001, POR-014`.
- **`A.2.4`** — Domaine ODD et sobriété topologique : `EXIG-AUT-04, EXIG-AUT-05, EXIG-ORC-01, EXIG-ORC-02, EXIG-ORC-03` ; PRR : `G-02` ; Portes : `POR-003, POR-006`.
- **`A.2.5`** — Réévaluation, dérogations et catalogue : `EXIG-GOV-12, EXIG-GOV-15, EXIG-GOV-16, EXIG-GOV-17, EXIG-GOV-18, EXIG-GOV-19, EXIG-GOV-20, EXIG-CON-03` ; PRR : `O-03` ; Portes : `POR-001, POR-015`.
- **`A.2.6`** — Qualification SaaS et prérequis achat : `EXIG-ARC-21, EXIG-APP-01, EXIG-APP-02, EXIG-APP-03, EXIG-APP-04, EXIG-APP-05, EXIG-APP-06` ; PRR : `R-12` ; Portes : `POR-004, POR-008`.
- **`A.3.1`** — Sémantique et contrats du catalogue : `EXIG-INT-01, EXIG-INT-02, EXIG-INT-03, EXIG-INT-04, EXIG-INT-05, EXIG-INT-06, EXIG-INT-07, EXIG-INT-08, EXIG-INT-09, EXIG-INT-10, EXIG-INT-11` ; PRR : `G-09`, `F-13` ; Portes : `POR-005`.
- **`A.3.2`** — Épinglage, coexistence et paiements tiers : `EXIG-INT-12, EXIG-INT-13, EXIG-INT-14, EXIG-INT-15, EXIG-INT-16, EXIG-INT-17, EXIG-INT-18, EXIG-INT-19, EXIG-INT-20, EXIG-INT-21, EXIG-INT-22, EXIG-INT-23` ; PRR : `G-13`, `F-01`, `F-03` ; Portes : `POR-001, POR-013`.
- **`A.3.3`** — Serveurs MCP sans état sécurisés : `EXIG-MCP-01, EXIG-MCP-02, EXIG-MCP-03, EXIG-MCP-04, EXIG-MCP-08, EXIG-MCP-09, EXIG-MCP-10, EXIG-MCP-12, EXIG-MCP-13, EXIG-MCP-22` ; PRR : `R-09` ; Portes : `POR-001, POR-008`.
- **`A.3.4`** — Intention métier et hygiène MCP : `EXIG-MCP-05, EXIG-MCP-06, EXIG-MCP-07, EXIG-MCP-14, EXIG-MCP-15, EXIG-MCP-16, EXIG-MCP-17, EXIG-MCP-18, EXIG-MCP-19, EXIG-MCP-20, EXIG-MCP-21` ; PRR : `S-07` ; Portes : `POR-001`.
- **`A.3.5`** — Cartes signées et tâches A2A : `EXIG-A2A-01, EXIG-A2A-02, EXIG-A2A-03, EXIG-A2A-04, EXIG-A2A-05, EXIG-A2A-06, EXIG-A2A-07, EXIG-A2A-08, EXIG-A2A-09, EXIG-A2A-10, EXIG-A2A-11, EXIG-A2A-12, EXIG-A2A-13, EXIG-A2A-14, EXIG-A2A-15` ; PRR : `S-13`, `F-02`, `G-14` ; Portes : `POR-006, POR-013`.
- **`A.3.6`** — Bus CloudEvents et anti-boucle : `EXIG-EVT-01, EXIG-EVT-02, EXIG-EVT-03, EXIG-EVT-04, EXIG-EVT-05, EXIG-EVT-06, EXIG-EVT-07, EXIG-EVT-08, EXIG-EVT-09, EXIG-EVT-10` ; PRR : `R-04`, `R-05` ; Portes : `POR-006`.
- **`A.4.1`** — Couches et interfaces métier validantes : `EXIG-ARC-02, EXIG-ARC-03, EXIG-ARC-04, EXIG-ARC-07, EXIG-ARC-13, EXIG-ARC-14, EXIG-ARC-15, EXIG-ARC-16, EXIG-ARC-17, EXIG-ARC-18, EXIG-ARC-19, EXIG-ARC-20` ; PRR : `R-01`*, `R-13`, `F-12` ; Portes : `POR-004, POR-008`.
- **`A.4.2`** — Exécution durable et reprise d'état : `EXIG-ARC-05, EXIG-ARC-06, EXIG-ORC-11, EXIG-ORC-12, EXIG-ORC-13, EXIG-ORC-14` ; PRR : `R-02`, `O-08` ; Portes : `POR-003`.
- **`A.4.3`** — Clés d'idempotence et pré-engagement : `EXIG-ORC-21, EXIG-ORC-22` ; PRR : `R-03`*, `R-07`* ; Portes : `POR-003`.
- **`A.4.4`** — Sagas, compensations et injection fautes : `EXIG-ORC-15, EXIG-ORC-16, EXIG-ORC-17, EXIG-ORC-18, EXIG-ORC-19, EXIG-ORC-20` ; PRR : `R-06`*, `R-15` ; Portes : `POR-003`.
- **`A.4.5`** — Gouvernance des patrons multi-agents : `EXIG-ORC-04, EXIG-ORC-05, EXIG-ORC-06, EXIG-ORC-07, EXIG-ORC-08, EXIG-ORC-09, EXIG-ORC-10, EXIG-ORC-23, EXIG-ORC-24, EXIG-ORC-25, EXIG-ORC-29, EXIG-ORC-30` ; PRR : `O-06` ; Portes : `POR-006`.
- **`A.4.6`** — Plafonds, repli bimodèle et coupe-circuit : `EXIG-ORC-26, EXIG-ORC-27, EXIG-ORC-28, EXIG-IAM-20, EXIG-SEC-26` ; PRR : `S-14`*, `R-10`, `R-11`, `F-07`, `F-08`, `F-09` ; Portes : `POR-003, POR-006, POR-015`.
- **`A.5.1`** — Paliers d'outils et union stricte : `EXIG-AUT-08, EXIG-AUT-10, EXIG-AUT-11` ; PRR : `S-09`* ; Portes : `POR-001, POR-003`.
- **`A.5.2`** — Approbation hors bande liée P3 : `EXIG-AUT-09, EXIG-AUT-12, EXIG-AUT-13, EXIG-AUT-14` ; PRR : `S-10` ; Portes : `POR-003`.
- **`A.5.3`** — Ergonomie fidèle et vigilance humaine : `EXIG-AUT-15, EXIG-AUT-16, EXIG-AUT-19, EXIG-AUT-20, EXIG-AUT-21` ; PRR : `G-11`, `G-12` ; Portes : `POR-009, POR-014`.
- **`A.5.4`** — Agents ambiants et persistance pré-effet : `EXIG-AUT-17, EXIG-AUT-18` ; PRR : `R-08` ; Portes : `POR-015`.
- **`A.5.5`** — Décisions automatisées Loi 25 : `EXIG-AUT-22, EXIG-AUT-23, EXIG-CON-07, EXIG-CON-08, EXIG-CON-09` ; PRR : `G-06`* ; Portes : `POR-002, POR-014`.
- **`A.6.1`** — Identité NHI sans secret statique : `EXIG-IAM-01, EXIG-IAM-02, EXIG-IAM-03, EXIG-IAM-04, EXIG-IAM-05, EXIG-IAM-06, EXIG-IAM-07` ; PRR : `S-01`* ; Portes : `POR-001, POR-011`.
- **`A.6.2`** — Échange RFC 8693 sans relais : `EXIG-IAM-08, EXIG-IAM-09, EXIG-IAM-10, EXIG-IAM-11, EXIG-IAM-12, EXIG-MCP-11` ; PRR : `S-03`*, `S-04` ; Portes : `POR-001, POR-011`.
- **`A.6.3`** — Profil OAuth et liaison expéditeur : `EXIG-IAM-13, EXIG-IAM-14, EXIG-IAM-15, EXIG-IAM-16` ; PRR : `S-05` ; Portes : `POR-007, POR-011`.
- **`A.6.4`** — Coupure passerelles d'agents et modèles : `EXIG-ARC-01, EXIG-ARC-08, EXIG-ARC-09, EXIG-ARC-11, EXIG-ARC-12, EXIG-IAM-17, EXIG-IAM-18, EXIG-IAM-19, EXIG-IAM-21` ; PRR : `S-06`*, `F-14`* ; Portes : `POR-001, POR-012`.
- **`A.6.5`** — Règle de deux anti-exfiltration : `EXIG-SEC-01, EXIG-SEC-02, EXIG-SEC-03, EXIG-SEC-04, EXIG-SEC-05, EXIG-SEC-06, EXIG-SEC-07` ; PRR : `S-08`* ; Portes : `POR-003`.
- **`A.6.6`** — Bac à sable réseau fermé : `EXIG-ARC-10, EXIG-SEC-08, EXIG-SEC-09, EXIG-SEC-10, EXIG-SEC-11, EXIG-SEC-12, EXIG-SEC-13, EXIG-SEC-14, EXIG-SEC-15, EXIG-SEC-16, EXIG-SEC-17` ; PRR : `S-11`* ; Portes : `POR-003`.
- **`A.6.7`** — Provenance signée et tests adverses : `EXIG-SEC-18, EXIG-SEC-19, EXIG-SEC-20, EXIG-SEC-21, EXIG-SEC-22, EXIG-SEC-23, EXIG-SEC-24, EXIG-SEC-25` ; PRR : `S-02`, `F-10` ; Portes : `POR-003, POR-007`.
- **`A.6.8`** — Agilité cryptographique et transition post-quantique (NIST IR 8547) : `EXIG-SEC-27, EXIG-SEC-28` ; PRR : `S-14`* ; Portes : `POR-002, POR-007`.
- **`A.7.1`** — Traces OpenTelemetry épinglées au collecteur : `EXIG-OBS-01, EXIG-OBS-02, EXIG-OBS-03, EXIG-OBS-04, EXIG-OBS-05, EXIG-OBS-06` ; PRR : `O-01` ; Portes : `POR-002`.
- **`A.7.2`** — Double couloir RP (PII) sans contenu : `EXIG-OBS-07, EXIG-OBS-08, EXIG-OBS-09, EXIG-OBS-10` ; PRR : `O-02`*, `F-15` ; Portes : `POR-002`.
- **`A.7.3`** — Journal d'audit JCS chaîné ancré : `EXIG-OBS-11, EXIG-OBS-12, EXIG-OBS-13` ; PRR : `G-15`* ; Portes : `POR-002, POR-007, POR-011`.
- **`A.7.4`** — Évaluation E1–E3 pass^k et dérive : `EXIG-EVA-01, EXIG-EVA-02, EXIG-EVA-03, EXIG-EVA-04, EXIG-EVA-05, EXIG-EVA-06` ; PRR : `O-04`, `O-05`, `O-07`, `O-14` ; Portes : `POR-003, POR-014, POR-015`.
- **`A.7.5`** — Enveloppes FinOps, CPO et carbone : `EXIG-FIN-01, EXIG-FIN-02, EXIG-FIN-03, EXIG-FIN-04, EXIG-FIN-05, EXIG-FIN-06, EXIG-FIN-07, EXIG-FIN-08, EXIG-FIN-09, EXIG-FIN-10` ; PRR : `O-09`*, `O-10`, `O-11`, `O-12`, `O-13` ; Portes : `POR-004, POR-009, POR-016`.
- **`A.8.1`** — ÉFVP préalable et finalités vérifiées : `EXIG-CON-04, EXIG-CON-06` ; PRR : `G-05`* ; Portes : `POR-002, POR-012`.
- **`A.8.2`** — Six substrats d'état et clés : `EXIG-CON-05` ; PRR : `F-04`*, `F-05`, `F-06` ; Portes : `POR-002`.
- **`A.8.3`** — Isolation CoALA et effacement vérifiable : `EXIG-ARC-22, EXIG-ARC-23, EXIG-ARC-24, EXIG-ARC-25, EXIG-CON-10` ; PRR : `S-12`, `R-14`*, `G-10`* ; Portes : `POR-005`.
- **`A.8.4`** — Conformité multi-régimes E-23, AMF, RIA : `EXIG-CON-11, EXIG-CON-12, EXIG-CON-13, EXIG-CON-14, EXIG-CON-15, EXIG-CON-16, EXIG-CON-17, EXIG-CON-18, EXIG-CON-21` ; PRR : `G-08` ; Portes : `POR-002, POR-012`.
- **`A.8.5`** — Transparence, incidents et impact unifié : `EXIG-CON-19, EXIG-CON-20, EXIG-CON-22, EXIG-CON-23, EXIG-CON-24, EXIG-CON-25, EXIG-CON-26` ; PRR : `G-07`* ; Portes : `POR-002`.
- **`A.8.6`** — Évaluation fournisseurs, dix clauses contractuelles et sortie : `EXIG-APP-07, EXIG-APP-08, EXIG-APP-09, EXIG-APP-10, EXIG-APP-11, EXIG-APP-12, EXIG-APP-13, EXIG-APP-14, EXIG-APP-15, EXIG-APP-16, EXIG-APP-17` ; PRR : `O-15` ; Portes : `POR-004, POR-016`.
- **`A.8.7`** — Secteurs financiers ACVM 11-348, RTR ISO 20022, EN 18286 et AMF : `EXIG-CON-27, EXIG-CON-28, EXIG-CON-29, EXIG-CON-30, EXIG-AMF-01, EXIG-AMF-02, EXIG-AMF-03, EXIG-AMF-04, EXIG-AMF-05, EXIG-AMF-06, EXIG-AMF-07, EXIG-AMF-08, EXIG-AMF-09, EXIG-AMF-10, EXIG-AMF-11, EXIG-AMF-12` ; PRR : `G-15`* ; Portes : `POR-004, POR-009`.

### Portefeuille prospectif déplié : 43 initiatives `INI-*`, 15 portes `POR-*` et 27 signaux `SIG-*`

*Conventions de plages : `INI-001`–`029` initiatives sans regret et `INI-041`–`054` conditionnelles (`030`–`040` réservés) ; `POR-001`–`016` sans `POR-010` (`15` portes actives) ; `SIG-001`–`017` technologiques et `SIG-101`–`110` réglementaires/sectorielles.*

- **`INI-001`** (`P1`, `sans_regret`, signal `SIG-101`) : Déploiement du registre central d'inventaire, de cote de risque inhérent et de blocage réseau.
- **`INI-002`** (`P1`, `sans_regret`, signal `SIG-003`) : Mise en service des identités non humaines parrainées, de l'automatisation TLS à 47 jours et de l'échange de jetons à portée atténuée.
- **`INI-003`** (`P1`, `sans_regret`, signal `SIG-005`) : Interposition de la passerelle d'outils aux neuf contrôles (7 aller, 2 retour) et épinglage cryptographique des schémas.
- **`INI-004`** (`P1`, `sans_regret`, signal `SIG-101`) : Externalisation du point de décision de politique déterministe, décontamination et coupe-circuit.
- **`INI-005`** (`P1`, `sans_regret`, signal `SIG-006`) : Instrumentation de la télémétrie causale normalisée au collecteur et de la voûte forensique régionale.
- **`INI-006`** (`P1`, `sans_regret`, signal `SIG-107`) : Cartographie juridictionnelle des six substrats d'état et mise sous clés souveraines.
- **`INI-007`** (`P1`, `sans_regret`, signal `SIG-015`) : Mise en place du plan de données d'inférence tri-palier et des bacs à sable d'exécution sans réseau.
- **`INI-008`** (`P1`, `sans_regret`, signal `SIG-014`) : Standardisation de l'enveloppe déterministe, de l'exécution durable et des sagas à compensation.
- **`INI-009`** (`P1`, `sans_regret`, signal `SIG-106`) : Déploiement des interfaces déclaratives bornées, des postes de supervision liée et du canal de recours client.
- **`INI-010`** (`P1`, `sans_regret`, signal `SIG-005`) : Industrialisation de la compilation déterministe du contexte et de la bibliothèque signée de compétences.
- **`INI-011`** (`P1`, `sans_regret`, signal `SIG-015`) : Encapsulation déterministe en décimal exact des programmes centraux bancaires et actuariels prioritaires.
- **`INI-012`** (`P1`, `sans_regret`, signal `SIG-013`) : Mise en service des bancs internes de qualification multi-essais et de l'outillage indépendant des deuxième et troisième lignes.
- **`INI-013`** (`P1`, `sans_regret`, signal `SIG-001`) : Automatisation de la qualification par empreinte juridictionnelle et de la comptabilité au coût par résultat.
- **`INI-014`** (`P1`, `sans_regret`, signal `SIG-002`) : Renégociation des clauses contractuelles de notification, de non-réemploi et de sortie des tiers.
- **`INI-015`** (`P1`, `conditionnelle`, signal `SIG-103`) : Encadrement dérogatoire confiné et plan d'extinction à douze mois des agents d'interface graphique résiduels.
- **`INI-016`** (`P2`, `sans_regret`, signal `SIG-110`) : Déploiement de la couche sémantique gouvernée et des médiateurs vers les standards financiers et d'assurance.
- **`INI-017`** (`P2`, `sans_regret`, signal `SIG-106`) : Ouverture contrôlée de la mémoire bi-temporelle à oubli sélectif et des sas de contrats de qualité des données.
- **`INI-018`** (`P2`, `sans_regret`, signal `SIG-004`) : Homologation des topologies multi-agents bornées, de la dorsale événementielle et de la délégation anti-boucle.
- **`INI-019`** (`P2`, `sans_regret`, signal `SIG-009`) : Migration hybride post-quantique (ML-DSA et SLH-DSA) des identités, jetons délégués et scellement des archives longues.
- **`INI-020`** (`P2`, `sans_regret`, signal `SIG-002`) : Qualification et exercices trimestriels de bascule vers les profils de continuité cognitive à poids ouverts.
- **`INI-021`** (`P2`, `sans_regret`, signal `SIG-103`) : Mise en production des passerelles réglementées de partage financier ouvert en lecture et préparation synchronisée de l'écriture.
- **`INI-022`** (`P2`, `sans_regret`, signal `SIG-015`) : Activation de la surveillance continue de dérive par budgets d'erreur et passage à la refacturation interne.
- **`INI-023`** (`P2`, `sans_regret`, signal `SIG-016`) : Intégration de la comptabilité énergétique et carbone des charges d'inférence dans le routage et la reddition climatique.
- **`INI-024`** (`P2`, `sans_regret`, signal `SIG-017`) : Industrialisation de l'usine de modernisation patrimoniale en miroir sans écart et de l'exploitation sans shell libre.
- **`INI-025`** (`P2`, `conditionnelle`, signal `SIG-004`) : Fédération d'orchestration multi-plateformes selon la gravité des données autour du noyau neutre.
- **`INI-026`** (`P2`, `conditionnelle`, signal `SIG-102`) : Ouverture des canaux vocaux et multimodaux en temps réel pour l'accueil et la déclaration assistée de sinistres.
- **`INI-027`** (`P2`, `conditionnelle`, signal `SIG-016`) : Déploiement d'enclaves matérielles attestées pour l'inférence sur dossiers médicaux, actuariels et secrets stratégiques.
- **`INI-028`** (`P2`, `conditionnelle`, signal `SIG-015`) : Mise en service de la filière de compilation de consignes et de distillation sous sas de désidentification.
- **`INI-029`** (`P2`, `conditionnelle`, signal `SIG-109`) : Déploiement du sas déterministe télématique et des trousses d'opération locale hors réseau pour équipes d'indemnisation.
- **`INI-041`** (`P3`, `sans_regret`, signal `SIG-009`) : Achèvement de la migration post-quantique native des identités d'agents, des chaînes de délégation et du ré-horodatage probatoire.
- **`INI-042`** (`P3`, `sans_regret`, signal `SIG-108`) : Mise en conformité post-temporisation fédérale de juin 2033 des règles déterministes de cloisonnement et de gouvernance de groupe.
- **`INI-043`** (`P3`, `sans_regret`, signal `SIG-017`) : Élargissement sélectif sur preuve des mandats supervisés sur exception en Classes 3 et 5 et sanctuarisation des filières de relève humaine.
- **`INI-044`** (`P3`, `sans_regret`, signal `SIG-015`) : Rationalisation patrimoniale continue en miroir et extinction résiduelle des adaptateurs transitoires.
- **`INI-045`** (`P3`, `conditionnelle`, signal `SIG-103`) : Ouverture encadrée des canaux numériques aux agents externes mandatés et initiation transactionnelle sous norme accréditée.
- **`INI-046`** (`P3`, `conditionnelle`, signal `SIG-007`) : Déploiement de cellules de négociation inter-organisations à séparation négociateur-évaluateur et rapprochement tripartite.
- **`INI-047`** (`P3`, `conditionnelle`, signal `SIG-007`) : Mise en service des justificatifs cryptographiques d'identité légale d'organisation et de mandats externes vérifiables.
- **`INI-048`** (`P3`, `conditionnelle`, signal `SIG-110`) : Raccordement aux espaces de données fédérés d'assurance, de réassurance et de finance durable sous politiques d'usage exécutables.
- **`INI-049`** (`P3`, `conditionnelle`, signal `SIG-016`) : Consolidation de la souveraineté cognitive et énergétique par distillation interne de petits modèles et inférence confidentielle.
- **`INI-050`** (`P3`, `conditionnelle`, signal `SIG-109`) : Extension des sas déterministes hors réseau et de l'orchestration déconnectée à quotas pour la résilience territoriale et catastrophique.
- **`INI-051`** (`P1–P3`, `sans_regret`, signal `SIG-008`) : Instrumentation du tableau de bord des parcours adaptatifs, des délais de préparation et des réservations d'interface.
- **`INI-052`** (`P1–P3`, `sans_regret`, signal `SIG-015`) : Dispositif budgétaire d'arbitrage trimestriel, de gel d'autonomie et de déclassement des initiatives hors cible économique.
- **`INI-053`** (`P2`, `conditionnelle`, signal `SIG-002`) : Exécution coordonnée d'un plan de sortie et de migration hors d'un fournisseur critique de modèles ou de plateforme.
- **`INI-054`** (`P2`, `conditionnelle`, signal `SIG-010`) : Reconfiguration accélérée du portefeuille sur alerte cryptanalytique post-quantique ou requalification réglementaire transfrontalière.
- **`POR-001`** (`P1`, `M-20`) : Étanchéité de l'inventaire central, des identités non humaines, des certificats TLS 47 jours, des bacs à sable et de la passerelle d'outils.
- **`POR-002`** (`P1`, `M-20`) : Conformité juridique des six substrats d'état, du double couloir de traces et des recours clients.
- **`POR-003`** (`P1`, `M-20`) : Qualification indépendante de deuxième ligne, résilience d'exécution durable et coupe-circuit.
- **`POR-004`** (`P1`, `M-20`) : Sortie du Palier 1 (Stade 2 atteint) : coût complet affiché, clauses de réversibilité et retrait planifié des dérogations d'écran.
- **`POR-005`** (`P2`, `M-21`) : Intégrité sémantique inter-domaines, mémoire bi-temporelle auditable à date et quarantaine de données.
- **`POR-006`** (`P2`, `M-21`) : Sûreté de l'orchestration multi-systèmes, garde anti-boucle inter-plateformes et continuité bimodèle.
- **`POR-007`** (`P2`, `M-21`) : Jalon de la fenêtre post-quantique : signatures hybrides ML-DSA et SLH-DSA, enclaves attestées et scellement probatoire des archives longues.
- **`POR-008`** (`P2`, `M-21`) : Homologation des interfaces réglementées de partage financier ouvert et extinction complète des agents d'écran.
- **`POR-009`** (`P2`, `M-21`) : Sortie du Palier 2 (Stade 3 atteint) : refacturation effective, empreinte carbone tracée et résilience des compétences humaines.
- **`POR-011`** (`P3`, `M-22`) : Homologation de l'achèvement cryptographique post-quantique des identités, délégations et archives d'agents (sortie P3).
- **`POR-012`** (`P3`, `M-22`) : Conformité statutaire post-temporisation 2033 et intégrité du cloisonnement des groupes financiers (sortie P3).
- **`POR-013`** (`P3`, `M-22`) : Homologation des échanges inter-organisations de Stade 4 sous mandat légal vérifiable et rapprochement hors modèle (sortie P3).
- **`POR-014`** (`P3`, `M-22`) : Validation de l'élargissement sélectif des mandats de Classes 3 et 5 et du maintien de la relève humaine (sortie P3).
- **`POR-015`** (`P1–P3`, `M-24`) : Protocole transversal d'octroi, de suspension et de rétrogradation automatique d'autonomie par budget d'erreur.
- **`POR-016`** (`P1–P3`, `M-24`) : Revue périodique de viabilité au coût complet par résultat conforme et d'exercice réel de réversibilité.
- **`SIG-001`** (`reglementation`, cadence `semestrielle`) : Modification des cas d'usage financiers de l'Annexe III de l'AI Act européen.
- **`SIG-002`** (`reglementation`, cadence `semestrielle`) : Réexamen de DORA sur les prestataires tiers critiques TIC et les systèmes automatisés.
- **`SIG-003`** (`normalisation`, cadence `trimestrielle`) : Normalisation formelle de l'identité d'agent et de l'échange de jetons délégués à l'IETF.
- **`SIG-004`** (`normalisation`, cadence `semestrielle`) : Livraison ou glissement des jalons IETF DAWN et AGENTPROTO sur la découverte et le dialogue d'agents.
- **`SIG-005`** (`normalisation`, cadence `trimestrielle`) : Rupture de compatibilité ou refonte d'identité dans le protocole d'accès aux outils (MCP).
- **`SIG-006`** (`normalisation`, cadence `trimestrielle`) : Stabilisation des conventions sémantiques OpenTelemetry pour les agents et les protocoles A2A/MCP.
- **`SIG-007`** (`normalisation`, cadence `semestrielle`) : Adoption de justificatifs de mandat organisationnel vérifiables (vLEI / W3C VC 2.0 / SPICE) dans les paiements.
- **`SIG-008`** (`normalisation`, cadence `annuelle`) : Création d'une norme ISO/IEC dédiée spécifiquement aux systèmes agentiques au sein du JTC 1/SC 42.
- **`SIG-009`** (`post-quantique`, cadence `semestrielle`) : Transformation de la feuille de route PQC financière du G7 en exigence prudentielle contraignante au Canada.
- **`SIG-010`** (`post-quantique`, cadence `semestrielle`) : Accélération de la menace quantique (CRQC) ou percée cryptanalytique sur les réseaux euclidiens.
- **`SIG-011`** (`post-quantique`, cadence `semestrielle`) : Prise en charge native des RFC post-quantiques (RFC 9964 ; RFC 10024 et RFC 10073 à confirmer à la source primaire IETF) dans les passerelles et HSM.
- **`SIG-012`** (`post-quantique`, cadence `trimestrielle`) : Incidents opérationnels liés à la réduction à 100 puis 47 jours de la validité des certificats TLS.
- **`SIG-013`** (`capacites`, cadence `semestrielle`) : Publication d'une suite d'évaluation fiable au-delà de 16 heures et sur tâches métier non algorithmiques.
- **`SIG-014`** (`capacites`, cadence `trimestrielle`) : Persistance des taux d'échec de coordination multi-agents en production.
- **`SIG-015`** (`marche`, cadence `trimestrielle`) : Divergence entre le coût unitaire du jeton et le coût complet par résultat réussi.
- **`SIG-016`** (`marche`, cadence `annuelle`) : Contrainte énergétique régionale ou rationnement de capacité de calcul pour l'inférence.
- **`SIG-017`** (`marche`, cadence `annuelle`) : Écart d'adoption en production et érosion de la relève qualifiée dans le secteur financier canadien.
- **`SIG-101`** (`reglementation`, cadence `trimestrielle`) : Conversion du bulletin du BSIF sur l'IA générative et agentique en ligne directrice prudentielle contraignante.
- **`SIG-102`** (`reglementation`, cadence `trimestrielle`) : Publication ouverte ou durcissement des lignes directrices de l'AMF sur l'intelligence artificielle et la distribution numérique sans représentant.
- **`SIG-103`** (`reglementation`, cadence `trimestrielle`) : Décrets d'entrée en vigueur, désignation de la norme technique unique et ouverture de l'accès en écriture des services bancaires axés sur les consommateurs.
- **`SIG-104`** (`normalisation`, cadence `semestrielle`) : Mise en production générale du Rail en temps réel (RTR) ISO 20022 et accès direct des fournisseurs de services de paiement enregistrés.
- **`SIG-105`** (`reglementation`, cadence `semestrielle`) : Adoption par les ACVM ou l'OCRI de règles contraignantes faisant suite à l'Avis 11-348 sur la convenance et l'explicabilité des systèmes d'IA.
- **`SIG-106`** (`reglementation`, cadence `semestrielle`) : Interprétation jurisprudentielle ou administrative de l'article 12.1 de la Loi 25 sur les décisions assistées par agent face aux décisions exclusivement automatisées.
- **`SIG-107`** (`reglementation`, cadence `semestrielle`) : Réforme fédérale de la LPRPDE instaurant un régime légal pancanadien des décisions automatisées dans le secteur privé.
- **`SIG-108`** (`reglementation`, cadence `annuelle`) : Révision législative fédérale précédant l'échéance de temporisation du 30 juin 2033 des lois régissant les banques, sociétés d'assurances et sociétés de fiducie.
- **`SIG-109`** (`reglementation`, cadence `semestrielle`) : Fixation par le BSIF des dates de mise en œuvre des plans de transition climatique et actualisation pancanadienne de l'encadrement de la télématique en assurance.
- **`SIG-110`** (`normalisation`, cadence `annuelle`) : Ouverture d'interfaces standardisées d'agents dans les normes sectorielles d'assurance et de partage financier (ACORD, CSIO, FDX).

### Empreintes `SHA-256` intégrales des 14 extraits `CA-G0-SYNC`

- **`G0-EX-CH01-01`** (`ch04`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/schemas/harness_extraction.schema.json` lignes `1-24` (`6b4428a1f8a6abcd2029280cded86b0e983ddb349d0f05c6ba0192c010f95aac`).
- **`G0-EX-CH01-02`** (`ch04`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/harness_proto/pipeline.py` lignes `204-232` (`75110799d751ee4b93c58c7aff4e2b6ce0c2c8d29c50b6d1668b4bf895dfc275`).
- **`G0-EX-CH01-03`** (`ch07`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/harness_proto/mcp_pinning.py` lignes `227-260` (`350e1959e6f0c54ce549afc77b4ef14959851bc9e45ad1a2eee52b9b36f4fc95`).
- **`G0-EX-CH01-04`** (`ch08`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/harness_proto/a2a_card.py` lignes `157-182` (`1a58d5eabab4361028420c902df71ef3b305f84bfd139e14c75c7318c545b899`).
- **`G0-EX-CH02-01`** (`ch17`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/authz_pqc_audit/obo_dpop.py` lignes `85-114` (`d3c2d0ce031a283ba8b3e85fc230c51f6fa036a46942a573dfd77351922d2991`).
- **`G0-EX-CH02-02`** (`ch17`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/authz_pqc_audit/ciba_approval.py` lignes `106-117` (`423ebd61ce4996bf314c2fcecab18e48129d46e379a70eaf57780b5e1e395307`).
- **`G0-EX-CH02-03`** (`ch18`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/authz_pqc_audit/pqc_http431.py` lignes `149-177` (`c5c72e27a3932180e70ba9ebd63c109c5cc146c3af50d1327aed293f0e614855`).
- **`G0-EX-CH02-04`** (`ch22`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/authz_pqc_audit/otel_pii_mapper.py` lignes `235-265` (`60bd160c1a507c6df31fd1dfc3811c866a6f17e8b623e961b2511c00c7e41889`).
- **`G0-EX-CH03-01`** (`ch20`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/policies_opa/rule_of_two.rego` lignes `3-26` (`c0adc5553c040a592151fbcff54a27e85412764f82815220c5297e79ba652036`).
- **`G0-EX-CH03-02`** (`ch20`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/policies_opa/camel_taint.rego` lignes `3-25` (`bd873cf677b35787f6054b97b6a2de30c0cb7c6a5a52375c8bce7275ab03637b`).
- **`G0-EX-CH03-03`** (`ch15`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/policy_saga/saga_orchestrator.py` lignes `107-140` (`a2aac944f6ae06fe63c2f6482618bae3356d6270f3c5f6a3756c8592ebd1a536`).
- **`G0-EX-CH04-01`** (`ch35`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/evalops_prr/wilson_bounds.py` lignes `43-70` (`3e685cbef8dea03f3c2c217d37c25e292295858505eae0769706570955f913ba`).
- **`G0-EX-CH04-02`** (`ch23`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/evalops_prr/metamorphic.py` lignes `38-63` (`31ad0df04f1930471a8cec511d897834f72c35851e98f9c7cae1aa82002c1472`).
- **`G0-EX-CH04-03`** (`ch34`) : `Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/schemas/adr_2027_b001.schema.json` lignes `1-32` (`4f0a41e7280851ce1413efeb6accb3632bb3ee6a0bfefc4fa7d92338156e36ae`).
<!-- BIBLIOGRAPHIE_BRUTE_FIN -->
