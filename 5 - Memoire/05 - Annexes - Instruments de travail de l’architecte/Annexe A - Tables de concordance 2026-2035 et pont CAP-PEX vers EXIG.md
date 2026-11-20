# Annexe A — Tables de concordance 2026-2035 et pont CAP/PEX vers EXIG-*

Générée automatiquement depuis `registre/concordances.json` (synthèse tabulaire `justification_tableau` ; analyses complètes `justification_detaillee` intégralement préservées dans le registre JSON et consultables dans `Memoire/Presentation.html`). Socle unifié CRE-IA-2026-01 v1.2 (exigences.json) : 305 EXIG-* (287 v1.1 + 12 EXIG-AMF issues de 2026/documents/Note AMF IA.pdf, CRE-IA-2026-01-QC, 41 attentes AMF-G/R/C/V/P + 6 PQC/ACVM/RTR/EN 18286 ; 255 DOIT, 34 NE DOIT PAS, 16 DEVRAIT).

## A.1 Passage entre les quatre découpages architecturaux (DIV-02 résorbée)

| Modèle pivot (5 couches + 3 volets) | CAD26 § 5.2–5.3 (6 vraies couches + 3 plans) | Écart DIV-02 corrigé | C26 ch. 43 | C27 § 0.1 | Rattachement CAP / EXIG |
| --- | --- | --- | --- | --- | --- |
| C1. interaction (canaux, approbation, transparence) | Couche 1 : Canaux et déclencheurs (zéro logique agent) | Intitulé exact CAD26 § 5.2 | Nulle couche UI (Tab. 43.1 [S]) ; Z2 → PC3 [S] en C3 | C5 Interaction humain-agent (§ 0.1) | CAP-001..006 ; EXIG-ARC-03, 04, EXIG-AUT-09, 12..16, 19..23 |
| C2. agents-orchestration (durable, sagas, A2A) | Couche 2 : Orchestration et état + volet Agents (C3) | Sépare Orchestration (C2) et Agents (C3) | C3 Orchestration (OO1–OO4, PC1–PC3, Z2 [S]), C1 A2A | C4 durable + C3 horizontale | CAP-007..014 ; EXIG-ARC-02, 05..07, 13, EXIG-INT-04, 05, 11, 22, EXIG-ORC-01..30, EXIG-A2A-01..15, EXIG-EVT-01..10, EXIG-AUT-17 |
| C3. contexte-connaissance (sémantique, mémoire CoALA) | Travail (C2), procédurale (C3), Couche 5 : Outils et données | Nulle C3 Connaissance (placée en C5) | Nulle couche dédiée (Tab. 43.1 [S]) ; ch. 2, Z5, PC4 [S] | C2 Sémantique, contexte, mémoire | CAP-015..021 ; EXIG-ARC-16, 22..25, EXIG-INT-01, 02, 12..16, 19 |
| C4. acces (passerelle PEP, patrimoine, OT) | C4 Médiation et connectivité, C5 Outils et données, C6 Systèmes d’enregistrement | C4 Médiation, C5 Outils, C6 Enregistrement | C4 Maillage (ch. 37), C1 MCP, Z4 [S] | C1 IT/OT + C3 fédération | CAP-022..028 ; EXIG-ARC-01, 11, 12, 14, 15, 17, 18, 21, EXIG-INT-03, 06, 07, EXIG-MCP-01..22 |
| C5. modeles (inférence, substrats, bacs) | Couche 3 : Agents et exécution cognitive (passerelle modèles, confinement) | Modèles et bacs en C3, non C6 | Nulle couche modèles/bacs (Tab. 43.1 [S]) ; PC5/Z5 [S] en C4 | Socle silicium, confinement, inférence | CAP-029..034 ; EXIG-ARC-08..10, EXIG-SEC-08..17 |
| Plan A. controle-identite-securite | Plan transversal A : Identité et sécurité (ch. 9) | Aligné sur CAD26 § 5.3 | C2 Identité/registre (fabrique) + C4 Maillage (PC5, Z5 [S]) | Pilier gauche Zero Trust, NHI | CAP-035..041 ; EXIG-IAM-01..21, EXIG-SEC-01..07, 18..28, EXIG-AUT-03, 08, 10, 11, EXIG-INT-21 |
| Plan B. controle-observabilite-finops | Plan transversal B : Observabilité, évaluation et FinOps (ch. 10) | Aligné sur CAD26 § 5.3 | C5 Exploitation — AgentOps (ch. 38–40 ; Z1, Z3/PC4 [S]) | Pilier droit AgentOps, FinOps | CAP-042..046 ; EXIG-OBS-01..13, EXIG-EVA-01..06, EXIG-FIN-01..10 |
| Plan C. controle-gouvernance-registre | Plan transversal C : Gouvernance et registre (ch. 11–13) | Aligné (volet dédié vs C27) | C6 Gouvernance (ch. 25–30), C2 registre, ch. 41 [S] | C6 gouvernance/B2B, deux piliers | CAP-047..052 ; EXIG-ARC-19..20, EXIG-AUT-01..07, 18, EXIG-INT-08..10, 17..23, GOV-01..20, CON-01..30, AMF-01..12, APP-01..17 |

**Note méthodologique —** A.1 ventile les 305 EXIG-* v1.2 par ancrage CAD26 § 5.2–5.3 ; A.3 les rattache aux 52 CAP typées DC-P07 (couverture_directe, ancrage_extension, comble_lacune_2026), dont CAP-040 rattachée aux EXIG PQC (SEC-27/28), 4 extensions explicites (CAP-014, 027, 031, 034) et 5 lacunes 2026 (CAP-025, 028, 033, 046, 052).

## A.2 Concordance des échelles de maturité et des grilles d’autonomie

**Note méthodologique —** Pont analytique [S] : 0 modèle de maturité en C26 § 43.5 ; LCIM retient 5/7 niveaux (Tab. 7.1) et ISO 11354-1 FEI 3 approches (Intégrée, Unifiée, Fédérée, § 1.2.1).

| Stade (PD28 / C27) | Maturité 5×5 (CAD26 ch. 14) | LCIM / ISO 11354 FEI (C26) | Règle d’usage |
| --- | --- | --- | --- |
| Stade 0 : Sans agents [S] | Niveau 1 Initial (pré-agentique) | Technique/Syntaxique ; FEI Intégrée [S] | Référence N0 avant toute agentification |
| Stade 1 : Pilotes isolés [S] | Niveau 1 Initial → 2 Reproductible | Syntaxique ; FEI Intégrée/Unifiée [S] | Transitoire 90 j (plafond N0–N1, POR-001) |
| Stade 2 : Usage encadré [S] | Niveau 2 Reproductible → 3 Défini | Sémantique (Tab. 7.1) ; FEI Unifiée [S] | Seuil minimal production réglementée (POR-001..004) |
| Stade 3 : Orchestration prod. [S] | Niveau 4 Géré par mesures | Pragmatique (Tab. 7.1) ; FEI Unifiée [S] | Cible suffisante majorité D1–D8 (sortie P2) |
| Stade 4 : Inter-organisations [S] | Niveau 5 Optimisé fédéré | Dynamique (Tab. 7.1) ; FEI Fédérée [S] | Sélectif P3 (POR-013) ; proscrit D2, D6 = Stade 3 interne (M-12 vs 3–4 M-15/M-18) |

| Classe d’acte (PD28) | Niveau × Palier (CAD26 ch. 8) | C27 (L0–L4) | C26 (OO / Q) | Contrôle obligatoire |
| --- | --- | --- | --- | --- |
| Hors classe (flux fixe) | N0 Déterministe sans choix modèle | L0 déterministe | OO3 pur / code [S] | Tests logiciels et revue de code |
| Classe 1 : Lire et analyser | N1 Consultatif outils P0–P1 | L1 lecture filtrée | OO1/OO2, Q-A/Q-D [S] | Filtrage ACL amont, télémétrie sans contenu |
| Classe 2 : Réversible borné | N3 sous ODD (faible/modérée) ou N2, P2 | L3 borné / L2 | OO3/OO4 sous cadre [S] | Idempotence, compensation Saga, échantillonnage |
| Classe 3 : Matériel coûteux | N2 par défaut (N3 sous seuil), P2 | L2 (L3 restreint) | OO3/OO4, arrêt PC3 [S] | Approbation JCS SHA-256 par action élevée |
| Classe 4 : Irréversible critique | Outil P3 jamais seul (même N4) | L2 hors bande | OO3/OO4 (§ 31.1) [S] | CIBA + FIDO2 lié à h (≤ 15 min) |
| Classe 5 : Décision visant personne | Classe élevée plafonnée N2 (EXIG-CON-02) | L2/L3 art. 12.1 | OO3/OO4 (§ 29.4.1), Q-E [S] | Avis, facteurs, réexamen humain, dossier 1 an |
| Classe 6 : Hors mandat | NX interdit sans dérogation (EXIG-AUT-03, GOV-17) | Exclu L0–L4 | Violation PC4 / Z3 [S] | Blocage hors modèle et coupe-circuit immédiat |

## A.3 Pont condensé des 52 capacités cibles vers les exigences CAD26

| Capacité | Intitulé condensé | Type | Exigences CAD26 (`EXIG-*`) | Justification |
| --- | --- | --- | --- | --- |
| CAP-001 | Interfaces sur catalogues déclaratifs | Directe | EXIG-ARC-03, EXIG-MCP-04, EXIG-MCP-19 | Canaux sans logique agent ni script |
| CAP-002 | Supervision liée aux paramètres | Directe | EXIG-AUT-09, EXIG-AUT-12, EXIG-AUT-13, EXIG-AUT-14, EXIG-AUT-15, EXIG-AUT-16, EXIG-AUT-19, EXIG-AUT-20, EXIG-AUT-21 | JCS hors bande, écran fidèle, témoins |
| CAP-003 | Transparence client et révision | Directe | EXIG-AUT-22, EXIG-AUT-23, EXIG-CON-07, EXIG-CON-08, EXIG-CON-21, EXIG-AMF-12 | Avis, facteurs explicables, recours art. 12.1 et AMF-12 |
| CAP-004 | Interaction vocale et multimodale | Directe | EXIG-ARC-04, EXIG-CON-19 | Trace à l’entrée et divulgation |
| CAP-005 | Contrôle communications externes | Directe | EXIG-CON-20, EXIG-CON-22, EXIG-CON-28 | Marquage, revue juridique et anti-AI washing ACVM |
| CAP-006 | Encadrement agents externes entrants | Extension | EXIG-A2A-09, EXIG-IAM-01 | Extension agents entrants sur ancrage A2A-09/IAM-01 |
| CAP-007 | Enveloppe déterministe d’agents | Directe | EXIG-ARC-02, EXIG-ARC-07, EXIG-ORC-01, EXIG-ORC-03, EXIG-ORC-24, EXIG-ORC-26, EXIG-ORC-29 | Séquencement maître, mandant/trace/plafonds |
| CAP-008 | Exécution durable et revalidation | Directe | EXIG-ARC-05, EXIG-ARC-06, EXIG-ORC-11, EXIG-ORC-12, EXIG-ORC-13, EXIG-ORC-14, EXIG-ORC-27, EXIG-AUT-17 | Persistance chiffrée, réessais bornés, réveil |
| CAP-009 | Idempotence, sagas et tampon | Directe | EXIG-ORC-15, EXIG-ORC-16, EXIG-ORC-17, EXIG-ORC-18, EXIG-ORC-19, EXIG-ORC-21, EXIG-ORC-22, EXIG-CON-29 | Clé JCS SHA-256, sagas et tampon RTR ISO 20022 |
| CAP-010 | Topologies multiagents homologuées | Directe | EXIG-ORC-02, EXIG-ORC-04, EXIG-ORC-05, EXIG-ORC-06, EXIG-ORC-07, EXIG-ORC-09, EXIG-ORC-10 | Gain mesuré, deux sauts, boucles bornées |
| CAP-011 | Dorsale événementielle et rejeu | Directe | EXIG-ARC-13, EXIG-INT-11, EXIG-EVT-01, EXIG-EVT-02, EXIG-EVT-03, EXIG-EVT-04, EXIG-EVT-05, EXIG-EVT-07, EXIG-EVT-08, EXIG-EVT-09, EXIG-EVT-10 | CloudEvents, AsyncAPI, zéro renseignement personnel (RP) |
| CAP-012 | Délégation A2A et anti-boucle | Directe | EXIG-INT-04, EXIG-INT-05, EXIG-A2A-01, EXIG-A2A-02, EXIG-A2A-05, EXIG-A2A-07, EXIG-A2A-13, EXIG-A2A-15, EXIG-EVT-06, EXIG-ORC-08 | A2A 1.0 corrélé et compteur sauts |
| CAP-013 | Fédération multi-plateformes par gravité | Extension | EXIG-ARC-19, EXIG-ARC-20, EXIG-ARC-21, EXIG-A2A-06 | Extension gravité multi-plateformes sur ABB-SBB |
| CAP-014 | Négociation diplomate et évaluateur | Extension | EXIG-A2A-10, EXIG-A2A-12, EXIG-INT-22, EXIG-ORC-25 | Extension diplomate/tripartite sur ancrage A2A/INT-22 |
| CAP-015 | Couche sémantique et contrats | Directe | EXIG-INT-01, EXIG-INT-02 | Indicateurs gouvernés sans requêtes brutes |
| CAP-016 | Médiation vers standards sectoriels | Extension | EXIG-INT-13, EXIG-INT-14 | Extension médiation sectorielle sur SemVer 60 j |
| CAP-017 | Compilation contexte et ACL amont | Directe | EXIG-ARC-16, EXIG-ARC-22, EXIG-ORC-23 | Filtrage mandant, contexte minimal structuré |
| CAP-018 | Bibliothèque signée de compétences | Directe | EXIG-ARC-24, EXIG-INT-15, EXIG-INT-16 | Mémoire procédurale épinglée gérée comme code |
| CAP-019 | Mémoire bi-temporelle et oubli | Directe | EXIG-ARC-23, EXIG-ARC-25, EXIG-CON-10, EXIG-AMF-10 | Magasins isolés, bi-temporalité, purge Loi 25 |
| CAP-020 | Contrats données et quarantaine | Directe | EXIG-INT-12, EXIG-INT-19 | Contrat validé et détection ruptures |
| CAP-021 | Cloisonnement entité, consentement, loi | Directe | EXIG-CON-04, EXIG-CON-06, EXIG-CON-14 | ÉFVP, finalité par entité, interdits RIA |
| CAP-022 | Passerelle unifiée de médiation | Directe | EXIG-ARC-01, EXIG-ARC-11, EXIG-ARC-12, EXIG-MCP-01, EXIG-MCP-08, EXIG-MCP-09, EXIG-MCP-17, EXIG-MCP-22, EXIG-IAM-17, EXIG-IAM-19, EXIG-SEC-21 | Coupure PEP, domaines MCP isolés, HMAC |
| CAP-023 | Outils d’intention et épinglage | Directe | EXIG-ARC-15, EXIG-MCP-02, EXIG-MCP-03, EXIG-MCP-05, EXIG-MCP-06, EXIG-MCP-07, EXIG-MCP-14, EXIG-MCP-15, EXIG-MCP-16, EXIG-MCP-18, EXIG-MCP-20, EXIG-MCP-21 | Zéro CRUD brut, empreintes SHA-256 |
| CAP-024 | Encapsulation patrimoniale décimale exacte | Directe | EXIG-ARC-14, EXIG-ARC-17, EXIG-ARC-18 | API métier validantes, décimal exact, trace |
| CAP-025 | Sas dérogatoire et extinction CUA | Lacune 2026 | — (lacune 2026) | Lacune CAD26 automates écran (retrait 12 mois) |
| CAP-026 | Passerelles de partage financier ouvert | Extension | EXIG-INT-06, EXIG-INT-07, EXIG-MCP-10, EXIG-MCP-12, EXIG-MCP-13 | Extension partage ouvert sur consentement/portées |
| CAP-027 | Connecteurs d’espaces fédérés | Extension | EXIG-INT-03, EXIG-A2A-08, EXIG-A2A-11 | Extension espaces fédérés sur ancrage INT-03/A2A |
| CAP-028 | Sas OT et continuité déconnectée | Lacune 2026 | — (lacune 2026) | Lacune CAD26 sas OT et quotas 72 h [S] |
| CAP-029 | Plan d’inférence, routage et cache | Directe | EXIG-ARC-08, EXIG-ARC-09, EXIG-FIN-06, EXIG-FIN-07 | Alias logique et préfixe cache |
| CAP-030 | Bac à sable sans réseau | Directe | EXIG-ARC-10, EXIG-SEC-08, EXIG-SEC-09, EXIG-SEC-10, EXIG-SEC-11, EXIG-SEC-12, EXIG-SEC-13, EXIG-SEC-14, EXIG-SEC-15, EXIG-SEC-16, EXIG-SEC-17 | MicroVM fermée, IOMMU GPU, validation code |
| CAP-031 | Continuité bimodèle poids ouverts | Extension | EXIG-SEC-22, EXIG-APP-14 | Extension bimodèle poids ouverts sur SEC-22/APP-14 |
| CAP-032 | Cloisonnement des six substrats | Directe | EXIG-CON-05, EXIG-APP-11 | Lieux cartographiés et clés souveraines |
| CAP-033 | Inférence en enclave attestée | Lacune 2026 | — (lacune 2026) | Lacune CAD26 enclaves matérielles attestées |
| CAP-034 | Consignes compilées et distillation | Extension | EXIG-ARC-24, EXIG-CON-10 | Extension distillation/sas anti-RP [S] sur ARC-24 |
| CAP-035 | Identités NHI parrainées courtes | Directe | EXIG-IAM-02, EXIG-IAM-03, EXIG-IAM-04, EXIG-IAM-05, EXIG-IAM-06, EXIG-IAM-07, EXIG-IAM-16 | NHI distincte, zéro secret statique |
| CAP-036 | Délégation atténuée et possession | Directe | EXIG-IAM-08, EXIG-IAM-09, EXIG-IAM-10, EXIG-IAM-11, EXIG-IAM-12, EXIG-IAM-13, EXIG-IAM-14, EXIG-IAM-15, EXIG-MCP-11 | RFC 8693, DPoP/mTLS, zéro relais |
| CAP-037 | Politiques déterministes hors modèle | Directe | EXIG-IAM-18, EXIG-IAM-21, EXIG-AUT-03, EXIG-AUT-08, EXIG-AUT-10, EXIG-AUT-11 | Politiques en code, échec fermé |
| CAP-038 | Décontamination et défense anti-injection | Directe | EXIG-SEC-01, EXIG-SEC-02, EXIG-SEC-03, EXIG-SEC-04, EXIG-SEC-05, EXIG-SEC-06, EXIG-SEC-07, EXIG-SEC-23, EXIG-SEC-24, EXIG-SEC-25 | Règle de deux, retrait, banc bilingue |
| CAP-039 | Coupe-circuit et révocation rapide | Directe | EXIG-IAM-20, EXIG-ORC-28, EXIG-SEC-18, EXIG-SEC-20, EXIG-SEC-26, EXIG-APP-06, EXIG-APP-16 | Arrêt < 10 s [S] (15 min CAD26), SBOM |
| CAP-040 | Agilité crypto et post-quantique | Directe | EXIG-SEC-19, EXIG-OBS-12, EXIG-SEC-27, EXIG-SEC-28 | Couverture directe PQC NIST IR 8547 (SEC-27/28) |
| CAP-041 | Identité légale et mandats externes | Extension | EXIG-A2A-03, EXIG-A2A-04, EXIG-INT-21 | Extension identité légale sur cartes signées A2A |
| CAP-042 | Télémétrie à double couloir | Directe | EXIG-OBS-01, EXIG-OBS-02, EXIG-OBS-03, EXIG-OBS-04, EXIG-OBS-05, EXIG-OBS-06, EXIG-OBS-07, EXIG-OBS-08, EXIG-OBS-09, EXIG-OBS-10 | OTel épinglé sans contenu, débogage ≤ 14 j |
| CAP-043 | Qualification multi-essais et chaos | Directe | EXIG-EVA-01, EXIG-EVA-02, EXIG-EVA-03, EXIG-ORC-20, EXIG-ORC-30, EXIG-A2A-14 | Bancs E1–E2 pass^k et fautes |
| CAP-044 | Surveillance continue et budgets SLO | Directe | EXIG-EVA-04, EXIG-EVA-05, EXIG-EVA-06, EXIG-AUT-05 | Échantillonnage E3, juge étalonné, repli |
| CAP-045 | Pilotage au coût par résultat | Directe | EXIG-FIN-01, EXIG-FIN-02, EXIG-FIN-03, EXIG-FIN-04, EXIG-FIN-05, EXIG-FIN-06, EXIG-FIN-08, EXIG-FIN-09, EXIG-FIN-10, EXIG-APP-05 | CPO FOCUS, lots −50 %, petit modèle |
| CAP-046 | Comptabilisation énergétique et carbone | Lacune 2026 | — (lacune 2026) | Lacune CAD26 carbone ; portée 3 B-15 |
| CAP-047 | Registre central et blocage | Directe | EXIG-GOV-05, EXIG-GOV-06, EXIG-GOV-07, EXIG-GOV-08, EXIG-GOV-09, EXIG-GOV-10, EXIG-GOV-11, EXIG-GOV-14, EXIG-GOV-15, EXIG-GOV-16, EXIG-INT-08, EXIG-INT-09, EXIG-INT-10, EXIG-INT-17, EXIG-INT-18, EXIG-INT-20, EXIG-INT-23, EXIG-AMF-06 | 7 états, catalogue et dérogations bornées |
| CAP-048 | Gouvernance d’autonomie et relève | Directe | EXIG-AUT-01, EXIG-AUT-02, EXIG-AUT-04, EXIG-AUT-06, EXIG-AUT-07, EXIG-AUT-18, EXIG-CON-02, EXIG-CON-09, EXIG-GOV-01, EXIG-GOV-13, EXIG-AMF-07 | Plafonds classes, dossier 1 an, relève |
| CAP-049 | Empreinte juridictionnelle et preuves | Directe | EXIG-OBS-11, EXIG-OBS-13, EXIG-CON-01, EXIG-CON-03, EXIG-CON-11, EXIG-CON-12, EXIG-CON-13, EXIG-CON-15, EXIG-CON-16, EXIG-CON-17, EXIG-CON-18, EXIG-CON-23, EXIG-CON-24, EXIG-CON-25, EXIG-CON-26, EXIG-CON-27, EXIG-CON-30, EXIG-AMF-05, EXIG-AMF-08, EXIG-AMF-11 | Preuves uniques, ACVM, EN 18286 et profil AMF |
| CAP-050 | Validation indépendante 2e/3e lignes | Directe | EXIG-GOV-02, EXIG-GOV-03, EXIG-GOV-04, EXIG-GOV-12, EXIG-GOV-17, EXIG-GOV-18, EXIG-GOV-19, EXIG-GOV-20, EXIG-AMF-01, EXIG-AMF-02, EXIG-AMF-03, EXIG-AMF-04, EXIG-AMF-09 | Séparation rôles, E-23 et gouvernance conseil AMF |
| CAP-051 | Gouvernance tiers et sortie | Directe | EXIG-APP-01, EXIG-APP-02, EXIG-APP-03, EXIG-APP-04, EXIG-APP-07, EXIG-APP-08, EXIG-APP-09, EXIG-APP-10, EXIG-APP-12, EXIG-APP-13, EXIG-APP-15, EXIG-APP-17 | Grille éliminatoire, dix clauses, sortie |
| CAP-052 | Ingénierie assistée ségrégée | Lacune 2026 | — (lacune 2026) | Lacune CAD26 usine ; zéro interpréteur libre |

## A.4 Raccordement des 24 propositions d’exigence sectorielles (`PEX`)

| PEX | Profil | Type rattachement | Exigences CAD26 (`EXIG-*`) | Synthèse (CRE-IA v1.2) |
| --- | --- | --- | --- | --- |
| PEX-001 | Banque | Lacune 2026 | EXIG-IAM-01, EXIG-IAM-09, EXIG-IAM-17 | Lacune LSAC art. 171 anti-grattage et registre BdC |
| PEX-002 | Banque | Extension | EXIG-CON-06, EXIG-CON-10, EXIG-OBS-13 | Extension consentement exprès 5 ans et plaintes 7 ans |
| PEX-003 | Banque | Lacune 2026 | EXIG-IAM-21, EXIG-CON-06, EXIG-CON-11 | Lacune muraille bancassurance art. 416 Loi banques |
| PEX-004 | Banque | Directe | EXIG-CON-29, EXIG-INT-22, EXIG-AUT-09, EXIG-AUT-12, EXIG-ORC-21 | Directe EXIG-CON-29 : tampon RTR ISO 20022 pacs.008 |
| PEX-005 | Banque | Extension | EXIG-CON-05, EXIG-CON-19, EXIG-OBS-13 | Extension livres Canada art. 239 et plaintes 56 j |
| PEX-011 | Patrimoine | Directe | EXIG-CON-27, EXIG-GOV-01, EXIG-AUT-22, EXIG-CON-09, EXIG-CON-21 | Directe EXIG-CON-27 : convenance ACVM 11-348 / OCRI |
| PEX-012 | Patrimoine | Lacune 2026 | EXIG-ARC-12, EXIG-IAM-21, EXIG-CON-11 | Lacune double barrière sans conseils OEO OCRI 3241 |
| PEX-013 | Patrimoine | Directe | EXIG-CON-28, EXIG-CON-19, EXIG-CON-20, EXIG-CON-22, EXIG-OBS-13 | Directe EXIG-CON-28 : anti-AI washing et archive 7 ans |
| PEX-014 | Patrimoine | Extension | EXIG-CON-27, EXIG-IAM-21, EXIG-EVA-02, EXIG-CON-26 | Extension conflits NI 31-103, fin rétrofacturations 2028 |
| PEX-015 | Patrimoine | Lacune 2026 | EXIG-INT-02, EXIG-INT-12, EXIG-ARC-17 | Lacune calcul décimal quotidien frais NI 31-103 |
| PEX-021 | Assurance personnes | Lacune 2026 | EXIG-ARC-23, EXIG-CON-06, EXIG-CON-10 | Lacune purge pénale tests génétiques L.C. 2017 |
| PEX-022 | Assurance personnes | Extension | EXIG-CON-04, EXIG-CON-06, EXIG-OBS-12 | Extension consentement limité réseau santé québécois |
| PEX-023 | Assurance personnes | Directe | EXIG-AUT-07, EXIG-AUT-09, EXIG-AUT-22, EXIG-AUT-23, EXIG-CON-07, EXIG-AMF-12 | Directe EXIG-CON-07 / AMF-12 : refus vital art. 12.1 |
| PEX-024 | Assurance personnes | Extension | EXIG-GOV-07, EXIG-SEC-22, EXIG-APP-13, EXIG-AMF-06 | Extension sociétés mandataires et répertoire AMF-06 |
| PEX-025 | Assurance personnes | Directe | EXIG-SEC-27, EXIG-SEC-28, EXIG-OBS-12, EXIG-OBS-13, EXIG-CON-05, EXIG-CON-10 | Directe EXIG-SEC-27/28 : agilité PQC vie et rentes |
| PEX-031 | Assurance dommages | Extension | EXIG-ORC-27, EXIG-AUT-09, EXIG-AUT-23, EXIG-CON-07, EXIG-AMF-12 | Extension élasticité B-9/E-21 et refus humain AMF-12 |
| PEX-032 | Assurance dommages | Extension | EXIG-ARC-24, EXIG-CON-22, EXIG-IAM-21 | Extension assemblage déterministe formulaires auto AMF |
| PEX-033 | Assurance dommages | Lacune 2026 | EXIG-OBS-11, EXIG-OBS-12, EXIG-CON-21, EXIG-AMF-11 | Lacune neutralité ≥ 3 assureurs hors groupe (LDPSF) |
| PEX-034 | Assurance dommages | Extension | EXIG-IAM-03, EXIG-IAM-07, EXIG-SEC-03, EXIG-SEC-04, EXIG-SEC-06 | Extension NHI courtiers B-10, décontamination multimodale |
| PEX-035 | Assurance dommages | Lacune 2026 | EXIG-CON-11, EXIG-CON-12, EXIG-AMF-05, EXIG-EVA-03 | Lacune modèles catastrophe B-9 et émissions B-15 |
| PEX-041 | Groupe diversifié | Extension | EXIG-CON-06, EXIG-ARC-16, EXIG-ARC-25, EXIG-IAM-21 | Extension étiquette entité immuable, muraille groupe |
| PEX-042 | Groupe diversifié | Extension | EXIG-IAM-08, EXIG-IAM-10, EXIG-CON-06 | Extension jeton consentement exprès inter-filiales |
| PEX-043 | Groupe diversifié | Extension | EXIG-GOV-05, EXIG-APP-01, EXIG-APP-13, EXIG-APP-14, EXIG-AMF-01 | Extension ententes intra-groupe B-10 et AMF-01 |
| PEX-044 | Groupe diversifié | Extension | EXIG-GOV-07, EXIG-CON-05, EXIG-CON-11, EXIG-CON-12, EXIG-CON-25, EXIG-AMF-05, EXIG-AMF-08 | Extension livres, E-23, AMF-05/08 et portée 3 B-15 |
