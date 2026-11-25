# Annexe A — Table maîtresse de traçabilité MindMap → PRD (12 domaines, 36 chapitres, 71 familles, 260 thèmes)

Cette annexe consolidée est générée mécaniquement à la date de gel du 2 décembre 2026 (`CA-17`) à partir de `specs/manifest.json`, `registre/mindmap-complet.json`, `registre/glossaire-termes.json`, `recherche/manifeste-sources-sha256.json`, `recherche/registre-statut-f.json` et des journaux `ancrage/`.

Le socle documentaire fermé recense **135 sources primaires ouvertes `L+`** hachées `SHA-256` (`0,0 %` `METADATA_ONLY`), **27 exclusions `statut F`** (`AO-01`) et **55 vedettes** assignées à un chapitre propriétaire unique dans `glossaire-termes.json`. La barrière `G2` totalise **37 / 37 journaux Wyvern**, passant de **674** assertions initialement validées à **1390** assertions `supportées` (`100,0 %` après rectifications).

## 1. Ventilation du corpus primaire ouvert `L+` par catégorie documentaire

La distribution typologique des 135 pièces `L+` s'établit comme suit: `preprint` (33), `standard_spec` (26), `standard_rfc` (22), `legislation` (7), `regulatory_filing` (6), `standard_draft` (5), `standard_gov` (5), `journal_article` (4), `official_report` (4), `regulatory_guideline` (4), `conference_paper` (3), `industry_report` (3), `industry_standard` (2), `official_statistics` (2), `standard_reference` (2), `working_paper` (2), `book_chapter` (1), `regulatory_notice` (1), `report` (1), `technical_spec` (1), `third_party_aggregator` (1). Chaque pièce intégrale est conservée localement en UTF-8 sous `recherche/corpus_l_plus/` avec empreinte vérifiée par `verifie_manuscrit.py --sources-only`, tandis que les huit tomes antérieurs du Corpus restent cantonnés à un rôle d'index heuristique (`AO-02`) soumis au contrôle anti-plagiat par 12-grammes (`CA-03`).

## 2. Table maîtresse de traçabilité des 36 chapitres, 71 familles et 260 thèmes

| Unité | Domaine | Fam. / Thm. | Schémas | Cible (mots) |
|---|---|---:|---|---:|
| `ch01` | `D01` | 2 / 8 | SCH-01-01, SCH-01-02, SCH-01-03 | 4620 |
| `ch02` | `D01` | 2 / 4 | SCH-02-01, SCH-02-02, SCH-02-03 | 3860 |
| `ch03` | `D01` | 2 / 8 | SCH-03-01, SCH-03-02, SCH-03-03 | 4620 |
| `ch04` | `D02` | 2 / 7 | SCH-04-01, SCH-04-02, SCH-04-03 | 4430 |
| `ch05` | `D02` | 2 / 4 | SCH-05-01, SCH-05-02, SCH-05-03 | 3860 |
| `ch06` | `D02` | 2 / 12 | SCH-06-01, SCH-06-02, SCH-06-03, SCH-06-04 | 5380 |
| `ch07` | `D03` | 2 / 6 | SCH-07-01, SCH-07-02, SCH-07-03 | 4240 |
| `ch08` | `D03` | 2 / 8 | SCH-08-01, SCH-08-02, SCH-08-03 | 4620 |
| `ch09` | `D03` | 2 / 11 | SCH-09-01, SCH-09-02, SCH-09-03, SCH-09-04 | 5190 |
| `ch10` | `D04` | 2 / 7 | SCH-10-01, SCH-10-02, SCH-10-03 | 4430 |
| `ch11` | `D04` | 2 / 5 | SCH-11-01, SCH-11-02, SCH-11-03 | 4050 |
| `ch12` | `D04` | 2 / 7 | SCH-12-01, SCH-12-02, SCH-12-03 | 4430 |
| `ch13` | `D05` | 2 / 10 | SCH-13-01, SCH-13-02, SCH-13-03 | 5000 |
| `ch14` | `D05` | 2 / 3 | SCH-14-01, SCH-14-02, SCH-14-03 | 3670 |
| `ch15` | `D05` | 2 / 7 | SCH-15-01, SCH-15-02, SCH-15-03 | 4430 |
| `ch16` | `D06` | 2 / 8 | SCH-16-01, SCH-16-02, SCH-16-03 | 4620 |
| `ch17` | `D06` | 2 / 7 | SCH-17-01, SCH-17-02, SCH-17-03 | 4430 |
| `ch18` | `D06` | 2 / 4 | SCH-18-01, SCH-18-02, SCH-18-03 | 3860 |
| `ch19` | `D07` | 2 / 7 | SCH-19-01, SCH-19-02, SCH-19-03 | 4430 |
| `ch20` | `D07` | 2 / 9 | SCH-20-01, SCH-20-02, SCH-20-03 | 4810 |
| `ch21` | `D07` | 2 / 4 | SCH-21-01, SCH-21-02, SCH-21-03 | 3860 |
| `ch22` | `D08` | 2 / 8 | SCH-22-01, SCH-22-02, SCH-22-03 | 4620 |
| `ch23` | `D08` | 2 / 7 | SCH-23-01, SCH-23-02, SCH-23-03 | 4430 |
| `ch24` | `D08` | 2 / 5 | SCH-24-01, SCH-24-02, SCH-24-03 | 4050 |
| `ch25` | `D09` | 2 / 10 | SCH-25-01, SCH-25-02, SCH-25-03 | 5000 |
| `ch26` | `D09` | 2 / 8 | SCH-26-01, SCH-26-02, SCH-26-03 | 4620 |
| `ch27` | `D09` | 2 / 5 | SCH-27-01, SCH-27-02, SCH-27-03 | 4050 |
| `ch28` | `D10` | 2 / 10 | SCH-28-01, SCH-28-02, SCH-28-03 | 5000 |
| `ch29` | `D10` | 2 / 8 | SCH-29-01, SCH-29-02, SCH-29-03 | 4620 |
| `ch30` | `D10` | 2 / 6 | SCH-30-01, SCH-30-02, SCH-30-03 | 4240 |
| `ch31` | `D11` | 2 / 11 | SCH-31-01, SCH-31-02, SCH-31-03 | 5190 |
| `ch32` | `D11` | 2 / 8 | SCH-32-01, SCH-32-02, SCH-32-03 | 4620 |
| `ch33` | `D11` | 1 / 3 | SCH-33-01, SCH-33-02, SCH-33-03 | 3670 |
| `ch34` | `D12` | 2 / 6 | SCH-34-01, SCH-34-02, SCH-34-03 | 4240 |
| `ch35` | `D12` | 2 / 5 | SCH-35-01, SCH-35-02, SCH-35-03 | 4050 |
| `ch36` | `D12` | 2 / 14 | SCH-36-01, SCH-36-02, SCH-36-03, SCH-36-04 | 5760 |

## 3. Ventilation analytique des douze domaines (`D01`–`D12`)

### D01 — Fondements épistémiques, économiques et rupture agentique

Le domaine `D01` couvre les chapitres `ch01` à `ch03` (3 chapitres, cible **13100** mots) et regroupe **6 familles**, **20 thèmes**, **9 schémas** ainsi que **35 études `L+`** indexées sur cet axe. Passage des copilotes passifs aux Systèmes d'agentivité, loi de fiabilité de Lusser, erreurs silencieuses en cascade, constance multi-essais pass^k par rapport à pass@1, coûts de transaction cognitifs de Coase et distinction entre dette cognitive et dette technique.

Familles affectées en propriété exclusive: Paradigme des Systèmes d'agentivité ; Généalogie et fondements ; Loi de Lusser et erreurs en cascade ; Constance pass^k et métriques de fiabilité ; Économie cognitive de Coase ; Dettes cognitive, technique et d'intention.

### D02 — Architecture d'entreprise, partition 80/20 et échelle d'autonomie (L0–L4)

Le domaine `D02` couvre les chapitres `ch04` à `ch06` (3 chapitres, cible **13670** mots) et regroupe **6 familles**, **23 thèmes**, **10 schémas** ainsi que **19 études `L+`** indexées sur cet axe. Séparation entre exosquelette déterministe (80 %) et nœuds cognitifs (20 %), échelle L0–L4 et règle du maillon le plus élevé, supervision HITL/HOTL et abstention, harnais déterministe à 8 étapes sous JSON Schema strict, modélisation TOGAF/ArchiMate, 4 plans, 6 couches et DIV-02, noyau de contrôle possédé (42 CAP invariantes et 10 conditionnelles) et arbitrage entre achat, assemblage et construction.

Familles affectées en propriété exclusive: Partition 80/20 et séparation déterministe ; Harnais déterministe à 8 étapes ; Échelle L0–L4 et règle du maillon ; Supervision HITL / HOTL et abstention ; Noyau de contrôle possédé (42 CAP) et 31 ADR ; Cadres TOGAF / ArchiMate et 6 couches.

### D03 — Interopérabilité protocolaire, découverte et passerelles (MCP, A2A, AGNTCY, AP2)

Le domaine `D03` couvre les chapitres `ch07` à `ch09` (3 chapitres, cible **14050** mots) et regroupe **6 familles**, **25 thèmes**, **10 schémas** ainsi que **29 études `L+`** indexées sur cet axe. Cadre EIF à 4 couches, protocole vertical MCP avec épinglage cryptographique SHA-256 des schémas, protocole horizontal A2A et cartes AgentCard signées, initiatives AGNTCY/SLIM et AP2, Open Responses/SKILL.md, registres de découverte, passerelle PEP/AI Gateway à 9 contrôles et prévention du verrouillage fournisseur.

Familles affectées en propriété exclusive: Spécification MCP et façades d'intention ; Épinglage SHA-256 et sécurité MCP ; Protocole pair-à-pair A2A et ANP ; Piles AGNTCY/SLIM et paiements AP2 ; Découverte Agent Card et registres ; Passerelles PEP / AI Gateway et anti-verrouillage.

### D04 — Sémantique métier, contexte, mémoire CoALA et intégration patrimoniale (ACL/OT)

Le domaine `D04` couvre les chapitres `ch10` à `ch12` (3 chapitres, cible **12910** mots) et regroupe **6 familles**, **19 thèmes**, **9 schémas** ainsi que **8 études `L+`** indexées sur cet axe. Dette sémantique et ontologies métier (FIBO), compilation déterministe du contexte et RAG agentique, architecture mémorielle CoALA à quatre compartiments mémoriels isolés, propagation ACL en amont et effacement vérifiable (bi-temporalité), façade anti-corruption (ACL) devant ERP/SAP/Mainframe/BPM/RPA, encapsulation IT/OT et cloisonnement des 6 substrats d'état.

Familles affectées en propriété exclusive: Ontologies métier (FIBO) et contrats ODCS ; Compilation de contexte et RAG agentique ; Architecture mémorielle CoALA à quatre compartiments ; Filtrage ACL amont et gouvernance RAG ; Couche anti-corruption (ACL) et mainframes ; Encapsulation IT/OT et 6 substrats d'état.

### D05 — Orchestration hybride, chorégraphie événementielle et exécution durable (Saga)

Le domaine `D05` couvre les chapitres `ch13` à `ch15` (3 chapitres, cible **13100** mots) et regroupe **6 familles**, **20 thèmes**, **9 schémas** ainsi que **14 études `L+`** indexées sur cet axe. Arbre de sobriété OO1–OO4, 8 patrons de topologies multi-agents et lois d'échelle, dorsale événementielle CloudEvents/AsyncAPI, exécution durable (Temporal/Restate), idempotence JCS SHA-256, sémantique d'effet, Saga compensatoire autour d'un point pivot avec canal de compensation isolé et suite de 10 scénarios de fautes.

Familles affectées en propriété exclusive: Arbre de sobriété OO1–OO4 et APM ; Topologies multi-agents, cadriciels et MAST ; Dorsale Event Mesh (CloudEvents / AsyncAPI) ; Protocoles d'échange et négociation asynchrone ; Exécution durable (Temporal) et résilience ; Idempotence JCS et Saga compensatoire.

### D06 — Identité non humaine (NHI), chaîne de mandat et post-quantique

Le domaine `D06` couvre les chapitres `ch16` à `ch18` (3 chapitres, cible **12910** mots) et regroupe **6 familles**, **19 thèmes**, **9 schémas** ainsi que **33 études `L+`** indexées sur cet axe. OAuth 2.1/OIDC/SCIM, identités non humaines (NHI) éphémères sans secret statique, attestation SPIFFE/SPIRE, DID/VC/vLEI et passeport d'agent, grille des 5 questions et KYA, délégation atténuée au 2e saut (RFC 8693 OBO, RFC 9449 DPoP, RFC 9396 RAR), approbation hors bande CIBA+FIDO2, cycles TLS 100 j / 47 j et transition post-quantique ML-DSA/ML-KEM/SLH-DSA.

Familles affectées en propriété exclusive: Identités NHI, OAuth 2.1 et registres ; Attestation SPIFFE/SPIRE, DID/VC et vLEI ; Délégation OBO (RFC 8693), DPoP et RAR ; Approbation CIBA, KYA et révocation SSF/CAEP ; Certificats TLS 100 j / 47 j et ACME ; Transition post-quantique ML-DSA / SLH-DSA.

### D07 — Sécurité hors modèle, confinement déterministe (OPA, Règle de deux) et défense SOC

Le domaine `D07` couvre les chapitres `ch19` à `ch21` (3 chapitres, cible **13100** mots) et regroupe **6 familles**, **20 thèmes**, **9 schémas** ainsi que **15 études `L+`** indexées sur cet axe. Asymétrie capacité/sûreté, injection indirecte de consignes, tool poisoning et dérive silencieuse (rug pull), mandataire confus et kill chain multi-agents (OWASP ASI01–ASI10), politiques déterministes hors modèle OPA/Rego (default allow:= false), Règle de deux et séparation contrôle/données CaMeL, confinement sans réseau sortant (SHADI/microVM/WASI), TEE, SOC/SOAR, coupe-circuit (< 10 s) et Red Team.

Familles affectées en propriété exclusive: Injection indirecte et empoisonnement MCP ; Taxonomies OWASP ASI, ATLAS et mandataire confus ; Politiques OPA/Rego en échec fermé ; Règle de deux et séparation contrôle/données CaMeL ; Confinement SHADI, microVM, WASI et TEE ; Défense SOC/SOAR, Red Team et coupe-circuit.

### D08 — Observabilité probatoire, EvalOps hermétique et FinOps au résultat conforme

Le domaine `D08` couvre les chapitres `ch22` à `ch24` (3 chapitres, cible **13100** mots) et regroupe **6 familles**, **20 thèmes**, **9 schémas** ainsi que **26 études `L+`** indexées sur cet axe. Télémétrie OpenTelemetry GenAI sans contenu brut, double couloir probatoire (métadonnées caviardées PII/RP par opposition à la voûte d'audit scellée JCS RFC 8785, SCITT RFC 9943 et SLH-DSA), banc EvalOps hermétique à 3 paliers E1–E3, constance pass^k, bornes statistiques de Wilson (≥ 3/p), tests métamorphiques bilingues FR/EN, SRE et budgets d'erreur, ainsi que FinOps FOCUS v1.4 piloté par le coût complet par résultat conforme (CPO) et la cascade SLM/LLM.

Familles affectées en propriété exclusive: Télémétrie OpenTelemetry GenAI et provenance ; Double couloir PII, JCS et scellage SCITT ; Bancs EvalOps E1–E3 et bornes de Wilson ; Tests métamorphiques, juges et dérives ; FinOps FOCUS v1.4, CPO et carbone ; SRE agentique et volant de distillation SLM.

### D09 — Droit, régulation prudentielle (QC, CA, UE, int.) et contrats

Le domaine `D09` couvre les chapitres `ch25` à `ch27` (3 chapitres, cible **13670** mots) et regroupe **6 familles**, **23 thèmes**, **9 schémas** ainsi que **20 études `L+`** indexées sur cet axe. Obligations applicables et jalons vérifiés: Québec (Loi 25 art. 12.1 et art. 17 ÉFVP, CAI, AMF Ligne directrice IA et 12 EXIG-AMF), Canada fédéral (BSIF E-23 mai 2027, B-10, B-13, B-15, E-21, ACVM Avis 11-348 et NI 31-103, LSAC, vide fédéral C-27/C-36), Europe (EU AI Act art. 50 / Annexe III / EN 18286, RGPD, DORA, CRA, Data Act), repères internationaux (ISO/IEC 42001 statut F, NIST AI RMF, IMDA, G7) et clauses contractuelles de réversibilité.

Familles affectées en propriété exclusive: Droit québécois: Loi 25, ÉFVP et AMF ; Prudentiel canadien: BSIF E-23, ACVM et LSAC ; Union européenne: EU AI Act, DORA, CRA et EN 18286 ; Référentiels internationaux: NIST, ISO 42001 et G7 ; Clauses contractuelles EXIG-APP et sortie ; Grille fournisseurs et souveraineté nuage.

### D10 — Architectures sectorielles, blueprints et cas métier

Le domaine `D10` couvre les chapitres `ch28` à `ch30` (3 chapitres, cible **13860** mots) et regroupe **6 familles**, **24 thèmes**, **9 schémas** ainsi que **18 études `L+`** indexées sur cet axe. Déclinaison des 5 profils financiers (Banque, Gestion de patrimoine, Assurance de personnes, Assurance de dommages, Groupe financier diversifié) et 24 PEX, 3 blueprints multisectoriels et fédérés de référence (couvrant C01–C40 et 5 SBB), cas fil rouge Groupe Boréal Inc. (BEL: SAP S/4HANA, WMS, SOX — balisé comme illustratif et fictif), usine GitOps et 12 anti-patrons agentiques.

Familles affectées en propriété exclusive: Cinq profils financiers réglementés (M-14 à M-18) ; Spécialisations financières, RTR et terrain canadien ; Trois blueprints multisectoriels (C01–C40) ; Cas fil rouge Groupe Boréal (BEL) et fédération ; Usine logicielle, GitOps et reprise cognitive ; Catalogue des anti-patrons agentiques.

### D11 — Prospective 2028–2035, trajectoires DAPP et capital humain

Le domaine `D11` couvre les chapitres `ch31` à `ch33` (3 chapitres, cible **13480** mots) et regroupe **5 familles**, **22 thèmes**, **9 schémas** ainsi que **21 études `L+`** indexées sur cet axe. Scénarios prospectifs 2028–2035, planification adaptative DAPP (43 initiatives sans regret et conditionnelles, 15 portes POR, 27 signaux SIG), rampe 90 jours / 180 jours / 18 mois et Paliers P1–P3, 52 capacités CAP-*, 31 ADR et 12 DEC, gouvernance duale AE ↔ AS (10 thèses T1–T10, 6 décisions conjointes, 3 lignes de maîtrise), 7 pièges de gouvernance, prévention de l'atrophie des compétences humaines et du vivier junior, et contraintes énergétiques et de marché.

Familles affectées en propriété exclusive: Trajectoires adaptatives DAPP, portes POR et signaux SIG ; Prospective, scénarios 2028–2035 et maturité ; Gouvernance duale AE ↔ AS, thèses T1–T10 et RACI ; Sept pièges de gouvernance et responsabilité ; Atrophie des compétences et vivier junior.

### D12 — Homologation vérifiable, trousse exécutable, concordance et Wyvern/G0–G5

Le domaine `D12` couvre les chapitres `ch34` à `ch36` (3 chapitres, cible **14050** mots) et regroupe **6 familles**, **25 thèmes**, **10 schémas** ainsi que **23 études `L+`** indexées sur cet axe. Socle normatif CRE-IA-2026-01 v1.2 (305 EXIG-*), grille unifiée PRR-75 dont 24 portes bloquantes, fiche 2027-B001, 5 SBB et C01–C40, trousse logicielle exécutable Python 3.12+/OPA/JSON Schema 2020-12 du Tome 8 (83 pytest, 45 OPA 100%, 4 suites de vecteurs tiers), fermeture de DIV-02 et résolution des 5 discordances DISC-01..05, protocole d'ancrage atomique Wyvern, sources L+ SHA-256, statut F, chaîne G0–G5, CA-16, gabarit Typst (4 542 pages, 319 diagrammes), licences CC-BY-4.0/MIT et clause non-avis.

Familles affectées en propriété exclusive: Socle CRE-IA-2026-01 (305 EXIG-*) et interdits GOV-17 ; Grille PRR-75, 24 portes bloquantes et fiche 2027-B001 ; Trousse exécutable Python/OPA et 5 SBB ; Validation des vecteurs tiers et CA-G0-SYNC ; Concordance inter-tomes (DIV-02 et 5 discordances) ; Protocole Wyvern, G0–G5, Typst et clause non-avis.

## 4. Partition bijective des 260 thèmes par chapitre (`CA-21`)

- **`ch01`** (`D01`, cible 4620 mots ; ancrage `G2`: 38/38 assertions `supportées` (initial 21)) — 8 thèmes: Constat empirique de fin 2026: soutien par rapport à la production et déploiements bornés ; De l'échange de données à l'échange d'intentions et contrats comportementaux probabilistes ; Du modèle conversationnel à l'agent qui agit en boucle (PEAS, BDI, POMDP) ; Écart pilote-production, étude MAP et statistiques d'adoption 2026-2027 ; Taxonomie des systèmes d'IA composés et 5 archétypes d'acteurs ; Hiérarchie des preuves (6 niveaux) et bilan empirique des études de cas ; Raisonnement à l'inférence, modèles de raisonnement et limites des planificateurs LLM ; Revue multivocale PRISMA-ScR / Garousi (MLR W3.2) sur textes intégraux OA.

- **`ch02`** (`D01`, cible 3860 mots ; ancrage `G2`: 44/44 assertions `supportées` (initial 23)) — 4 thèmes: Rupture entre validité syntaxique et erreurs sémantiques silencieuses ; Loi de Lusser, taxonomie MAST (1 642 traces) et saturation METR ; Gains et surcoût du multi-agent (~15× jetons), raisonnement collectif et taxonomie MAST ; Primauté de la constance pass^k sur pass@k et transfert de techniques.

- **`ch03`** (`D01`, cible 4620 mots ; ancrage `G2`: 50/50 assertions `supportées` (initial 23)) — 8 thèmes: Économie de la preuve (//[É]/), dispersion de marché et dette de revue ; Dispersion des estimations de marché (2025–2030) et adoption réelle ; Industrialisation cognitive, moteurs composés (10x/an) et matrice Acheter/Assembler/Construire ; Économie des jetons, budget de réflexion et routage dynamique SLM/LLM ; Coûts de transaction cognitifs de Coase et économies d'agents virtuels ; Quadruple dette agentique (technique, cognitive, intention, couplage) ; Coût de la non-interopérabilité, dette d'intégration et invariant à quatre termes ; Généalogie EAI, SOA, API, EDA, FIPA-ACL et déplacement du sens.

- **`ch04`** (`D02`, cible 4430 mots ; ancrage `G2`: 53/53 assertions `supportées` (initial 31)) — 7 thèmes: Primauté du contrôle et enveloppe déterministe autour du raisonnement probabiliste ; Enveloppe déterministe, séparation System of Action / Systems of Record et 5 horloges ; Usine logicielle agentique (AST/SCIP), séparation des devoirs et Figuier étrangleur ; Patrons de boucle mono-agent (ReAct, ReWOO, Reflexion, CodeAct) et pilotage d'interface ; Minimisation de la surface agentique et séparation contrôleur/exécuteur ; Contrats JSON Schema Draft 2020-12 stricts et porte AMBIGU_ESCALADE ; Pont réglementaire: de BSIF E-23, AMF et Loi 25 aux frames déterministes.

- **`ch05`** (`D02`, cible 3860 mots ; ancrage `G2`: 36/36 assertions `supportées` (initial 20)) — 4 thèmes: Gouvernance matricielle: 8 domaines D1–D8 × Stades 0–4 × Classes 1–6 × N0–N4/P0–P3 ; Règle du critère le plus faible, union la plus stricte et règle d'or (≤ N2) ; Ergonomie anti-complaisance (ASI09), vue différentielle et distinction entre PC3 et art. 12.1 ; Distinction normative entre flux déterministe, agent interactif et agent ambiant.

- **`ch06`** (`D02`, cible 5380 mots ; ancrage `G2`: 51/51 assertions `supportées` (initial 33)) — 12 thèmes: Plan de contrôle d'agents, registre gouverné et distinction avec le catalogue interne ; Modèle à 5 couches + 3 volets, séparation ABB → SBB et règles ArchiMate 4 ; Sort des 31 ADR de 2027 (8/7/16) et les 12 décisions neutres DEC-001 à DEC-012 ; Interchangeabilité et transférabilité, dépôts d'actifs et clauses de sortie ; Registre des 31 décisions d'architecture (ADR-001 à ADR-031) et gabarit CI/CD ; Modèle de maturité N1–N5, diagnostic patrimonial et portail à portes G1–G4 ; Architecture de référence à 6 couches et 2 piliers transversaux ; Les 15 principes directeurs PRI-001 à PRI-015 et l'ordre d'arbitrage normatif ; Appel de fonctions contraint, ergonomie cognitive d'outils et erreurs actionnables ; Douze principes directeurs (PRIN-01 à PRIN-12) et hiérarchie d'arbitrage ; Critères d'évaluation technologique et budgets QoS (coût, précision, latence) ; Architecture de référence unifiée à six couches et points de contrôle PC1–PC5.

- **`ch07`** (`D03`, cible 4240 mots ; ancrage `G2`: 43/43 assertions `supportées` (initial 21)) — 6 thèmes: Protocole MCP (2026-07-28) sans état, ≤ 15 outils d'intention et bascule juillet 2027 ; Web agentique: WebMCP, NLWeb, Web Bot Auth (RFC 9421) et llms.txt ; Façades MCP orientées intention métier, structuredContent et resource_link ; Transport Streamable HTTP MCP 2026-07-28, rejet HTTP+SSE et adaptateur SEP-3398 ; Agent-Computer Interface (ACI), façades d'intention et Code Mode contre Swagger-to-MCP ; Épinglage cryptographique SHA-256 des outils MCP et analyse des 102 fiches NVD.

- **`ch14`** (`D05`, cible 3670 mots ; ancrage `G2`: 31/31 assertions `supportées` (initial 9)) — 3 thèmes: Dorsale événementielle sobre (CloudEvents/AsyncAPI, xagentmaxhops = 4) et fédération par gravité ; Taxonomie MAST (14 modes), tempêtes d'événements, boucles d'écho, DLQ et backpressure LLM ; Passerelle MCP ↔︎ ROS 2/DDS, vérification LOTO et arbitre matériel Simplex.

<!-- BIBLIOGRAPHIE_BRUTE_DEBUT -->
## Registre complet des sources `L+`, exclusions `statut F` et journaux `G2`

- **SRC-001** — From AGI to ASI (`edd192381975`).
- **SRC-002** — Design Patterns for Securing LLM Agents against Prompt Injections (`b3e1ed3304dd`).
- **SRC-003** — Towards a Science of Scaling Agent Systems (`991148d77ecd`).
- **SRC-004** — RFC 7493: The I-JSON Message Format (`79cf90d87551`).
- **SRC-005** — RFC 7515: JSON Web Signature (JWS) (`d5c3662fb6fe`).
- **SRC-006** — SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning (`c2565e8391cc`).
- **SRC-007** — Defeating Prompt Injections by Design (CaMeL) (`7a9735abcbdc`).
- **SRC-008** — Artificial Intelligence Index Report 2026 (`752f0d68bbd7`).
- **SRC-009** — RFC 8707: Resource Indicators for OAuth 2.0 (`7fb70d66034a`).
- **SRC-010** — RFC 9334: Remote ATtestation procedureS (RATS) Architecture (`9cf8aa2510be`).
- **SRC-011** — Agentic AI orchestration: TMT Predictions 2026 (`e7d41d25e64a`).
- **SRC-012** — RFC 9964: ML-DSA for JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) (`a7c42dac175c`).
- **SRC-013** — Transaction Tokens (Internet-Draft draft-ietf-oauth-transaction-tokens-11 — brouillon IETF WG) (`64447dddda3a`).
- **SRC-014** — Utilisation de l'intelligence artificielle par les entreprises au Canada, deuxième trimestre de 2026 (Tableau 33-10-1167-01) (`2e07bdc05646`).
- **SRC-015** — Utilisation de l'intelligence artificielle par les entreprises au Canada, troisième trimestre de 2026 (Tableau 33-10-1207-01) (`ea9fc801ab53`).
- **SRC-016** — Staff Analytical Paper 2026-22: Survey Evidence on Firm AI Adoption and its Implications (`b46da71236a3`).
- **SRC-017** — OAuth 2.0 Agent Authorization Explicit Revocation (Internet-Draft draft-chen-oauth-agent-revocation-01 — brouillon individuel) (`25d9788ca0cb`).
- **SRC-018** — NIST FIPS 205: Stateless Hash-Based Digital Signature Standard (SLH-DSA) (`c27445a0f736`).
- **SRC-019** — OpenID Shared Signals Framework Specification 1.0 (`68263a1cbe31`).
- **SRC-020** — OpenID Continuous Access Evaluation Profile (CAEP) 1.0 (`f3114cfa038f`).
- **SRC-021** — JSON Schema: A Media Type for Describing JSON Documents (Draft 2020-12 Core, draft-bhutton-json-schema-01) (`ece40a120598`).
- **SRC-022** — NIST/SEMATECH e-Handbook of Statistical Methods — Section 7.2.4.1 Confidence Intervals for a Binomial Proportion (Wilson / Exact) (`7cd7f651da8a`).
- **SRC-023** — FinOps Open Cost and Usage Specification (FOCUS) v1.4 — Spécification normative complète (`67f651d7a5b0`).
- **SRC-024** — NIST/SEMATECH e-Handbook of Statistical Methods — Section 8.1.8.1 Series Model (Lusser Reliability Law) (`8734d2a71190`).
- **SRC-025** — Measuring AI Ability to Complete Long Software Tasks (arXiv:2503.14499v4) (`816b90ee61a7`).
- **SRC-026** — Cognitive Architectures for Language Agents (CoALA) (`831e99a3f99a`).
- **SRC-027** — Measuring Agents in Production (MAP) (`3f8f34adaeb5`).
- **SRC-028** — Why Do Multi-Agent LLM Systems Fail? (MAST) (`7eeb1c6dfd09`).
- **SRC-029** — τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (`659469b4a86d`).
- **SRC-030** — Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation (HAL) (`4f1e326b6b31`).
- **SRC-031** — Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets (`80b064f92eb1`).
- **SRC-032** — The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size (`dd138f578d07`).
- **SRC-033** — Sagas (`61c64fc79006`).
- **SRC-034** — Temporal SDKs — Durable Execution, Event History and Deterministic Replay (`95aa625eecff`).
- **SRC-035** — CloudEvents Specification — Version 1.0.2 (`8f4d59dd27f8`).
- **SRC-036** — The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header) (`d737453f458f`).
- **SRC-037** — OpenTelemetry Semantic Conventions for Generative AI Agent & Execute Tool Spans (gen_ai.operation.name) (`1b2526202e8a`).
- **SRC-038** — Model Context Protocol (MCP) Specification — Revision 2025-11-25 (corpus normatif complet) (`938fca60c06c`).
- **SRC-039** — Agent2Agent (A2A) Protocol Specification (`fb9823ce1338`).
- **SRC-040** — From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI (`ea4b2e2a02be`).
- **SRC-041** — RFC 8693: OAuth 2.0 Token Exchange (`22f271006669`).
- **SRC-042** — RFC 9396: OAuth 2.0 Rich Authorization Requests (RAR) (`e334d06f1408`).
- **SRC-043** — RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP) (`5e0267f9b880`).
- **SRC-044** — RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT) (`1ed0ffb4007b`).
- **SRC-045** — OpenID Connect Client-Initiated Backchannel Authentication Flow — Core 1.0 (`fb983307e736`).
- **SRC-046** — SPIFFE Concepts — Workload Identity, SPIFFE ID and SVID (`d85539da6604`).
- **SRC-047** — Workload Identity Practices (draft-ietf-wimse-workload-identity-practices-08) (`863cee96178b`).
- **SRC-048** — AI Identity Management System (draft-ietf-wimse-aims-01) (`ab53c74913dd`).
- **SRC-049** — NIST FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM) (`bb840af1e6a3`).
- **SRC-050** — NIST FIPS 204: Module-Lattice-Based Digital Signature Standard (ML-DSA) (`14b6c1706d2c`).
- **SRC-051** — NIST IR 8547: Transition to Post-Quantum Cryptography Standards (Final, October 2026) (`80e6a458907c`).
- **SRC-052** — Advancing a Coordinated Roadmap for the Transition to Post-Quantum Cryptography in the Financial Sector (`cab48e350b29`).
- **SRC-053** — Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates (incl. Ballot SC-081v3) (`8d44ae9b57d6`).
- **SRC-054** — NIST AI 100-2e2025: Adversarial Machine Learning — A Taxonomy and Terminology of Attacks and Mitigations (`1f113bf38b90`).
- **SRC-055** — OWASP Top 10 for Agentic Applications 2026 (v1.0, December 2025 — document complet CC BY-SA 4.0) (`4d9f1c9f067f`).
- **SRC-056** — Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks (`490ff7dc6d69`).
- **SRC-057** — Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem (`cae21acac54f`).
- **SRC-058** — STAMP/STPA Informed Characterization of Factors Leading to Loss of Control in AI Systems (`78b03417f4de`).
- **SRC-059** — OWASP Agentic AI Top 10 Crosswalk (GitHub Pages miroir ouvert CC BY-SA 4.0) (`e5a50552cb52`).
- **SRC-060** — Règlement (UE) 2024/1689 (EU AI Act) (`e0a79e4f278c`).
- **SRC-061** — Règlement (UE) 2026/1744 du 8 juillet 2026 modifiant le règlement (UE) 2024/1689 (simplification / échéances IA) (`cafaf35193ed`).
- **SRC-062** — Règlement (UE) 2022/2554 sur la résilience opérationnelle numérique du secteur financier (DORA) (`6e4b138de7f0`).
- **SRC-063** — Loi modernisant des dispositions législatives en matière de protection des renseignements personnels (Loi 25 / LQ 2021, c. 25, art. 12.1) (`829e67f777ca`).
- **SRC-064** — Rapport quinquennal 2026 sur l'application de la Loi sur la protection des renseignements personnels dans le secteur privé (`db8153ade9d5`).
- **SRC-065** — Ligne directrice E-23 — Gestion du risque de modélisation à l'échelle de l'entreprise (édition 2027) (`60ef80b531aa`).
- **SRC-066** — Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security and Operational Risk (`5a1b1a2e004b`).
- **SRC-067** — Décision d'exécution (UE) 2026/2274 de la Commission du 12 octobre 2026 concernant les normes harmonisées relatives aux systèmes d'IA à haut risque (EN 18286:2026) (`3d1dcffce8ae`).
- **SRC-068** — Guideline B-10: Third-Party Risk Management (`db7ccc401ea3`).
- **SRC-069** — First harmonised standard supporting the AI Act published in the Official Journal (EN 18286:2026) (`647fbb09b0ec`).
- **SRC-070** — Loi sur les banques (L.C. 1991, ch. 46 — révision statutaire au 30 juin 2033) (`0e1fc9323793`).
- **SRC-071** — AIBanks.ca — The Canadian Bank AI Index (2026 Q4 edition, agrégateur tiers indépendant) (`2d39751c5fed`).
- **SRC-072** — Model Context Protocol (MCP) Revision 2026-07-28 — Server Tools (tools.mdx) (`ed550806a58e`).
- **SRC-073** — Calibrated adaptive framework for trustworthy human and artificial intelligence decision systems (`f06eb8eca755`).
- **SRC-074** — Model Context Protocol (MCP) Revision 2026-07-28 — Streamable HTTP Transport (streamable-http.mdx) (`22574bf11e00`).
- **SRC-075** — Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents (`a0b7c487a5e0`).
- **SRC-076** — RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA) (`29c43d9f68a7`).
- **SRC-077** — RFC 8785: JSON Canonicalization Scheme (JCS) (`be00e8aeddaf`).
- **SRC-078** — Model Context Protocol (MCP) Revision 2026-07-28 — Authorization Security Considerations (security-considerations.mdx) (`71dd5f0f236c`).
- **SRC-079** — GLEIF verifiable LEI (vLEI) Trust Chain & WebOfTrust vLEI KERI/ACDC Ecosystem Specifications (ISO 17442-3) (`2ccc0f09f7c8`).
- **SRC-080** — Model Context Protocol (MCP) Revision 2026-07-28 — TypeScript Schema (schema.ts) (`742750af0bb8`).
- **SRC-081** — MCP SEP-2596: Specification Feature Lifecycle and Deprecation Policy (Status: Final) (`6608969be121`).
- **SRC-082** — MCP SEP-3398: Release Cycle Updates (Status: Accepted) (`64aee02f2717`).
- **SRC-083** — Agent2Agent (A2A) Protocol Specification v1.0.1 (docs/specification.md) (`627ccfe6ffb1`).
- **SRC-084** — Agent2Agent (A2A) Protocol Protobuf Contract v1.0.1 (specification/a2a.proto) (`e195bf96ab63`).
- **SRC-085** — Agent2Agent (A2A) Protocol Specification v1.1.0-rc (Release Candidate post-gel adaptateur) (`25a940c30c00`).
- **SRC-086** — A2A Technology Compatibility Kit (a2a-tck) v1.0.0.alpha3 — AgentCard Requirements (tck/requirements/agent_card.py) (`4889ec96433a`).
- **SRC-087** — Open Policy Agent (OPA) v1.22.4 — Rego Policy Language Reference (policy-language.md) (`4b242f9eee53`).
- **SRC-088** — Open Policy Agent (OPA) v1.22.4 — Policy Testing & Coverage (policy-testing.md) (`4e566ce11e03`).
- **SRC-089** — OpenTelemetry Semantic Conventions v1.41.0 — GenAI Attribute Registry (gen-ai.md) (`74e99ecc4e35`).
- **SRC-090** — OpenTelemetry semantic-conventions-genai (commit 244465e9 — 85 attributs Development incluant cache_write) (`b05fc94233aa`).
- **SRC-091** — Testing Chatbots Using Metamorphic Relations (`069cee64fd68`).
- **SRC-092** — MORTAR: Multi-turn Metamorphic Testing for LLM-based Dialogue Systems (`0e9939c49f50`).
- **SRC-093** — Explanation-Guided Metamorphic Testing of Specialized Language Models: An Empirical Study (`619e05baae21`).
- **SRC-094** — Binomial confidence intervals for rare events: importance of defining margin of error relative to magnitude of proportion (`538950454399`).
- **SRC-095** — Attested Tool-Server Admission: A Security Extension to the Model Context Protocol (`61dc1007669d`).
- **SRC-096** — Virtual Agent Economies (`f475a70c3b55`).
- **SRC-097** — The Coasean Singularity? Demand, Supply, and Market Design with AI Agents (`45b9200d9e59`).
- **SRC-098** — An Economy of AI Agents (`c87fd1c3cd81`).
- **SRC-099** — Experimental evidence on the productivity effects of generative artificial intelligence (`454df0409d08`).
- **SRC-100** — The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers (`6d5df87a4d49`).
- **SRC-101** — Agentic AI Market Size & Share Analysis — Growth Trends and Forecast (`d36ecb1c274c`).
- **SRC-102** — Enterprise Agentic AI Market Size, Share & Trends Analysis Report (`575dae06de09`).
- **SRC-103** — Alphabet Inc. Form 8-K Exhibit 99.1 — Q3 2026 Financial Results (`ebfea816ab26`).
- **SRC-104** — Amazon.com, Inc. Form 8-K Exhibit 99.1 — Q3 2026 Financial Results and 2026 CapEx Guidance (`8da73deea031`).
- **SRC-105** — Meta Platforms, Inc. Form 8-K Exhibit 99.1 — Q3 2026 Results and 2026 CapEx Guidance (`bb4724559067`).
- **SRC-106** — Microsoft Corporation Form 10-Q — Quarter Ended September 30, 2026 (Q1 FY2027) (`6d7b4822b23d`).
- **SRC-107** — Microsoft Corporation Form 10-K — Fiscal Year Ended June 30, 2026 (`bdd42cefdb9a`).
- **SRC-108** — Microsoft Corporation Form 10-Q — Six Months Ended December 31, 2025 (Q2 FY2026) (`c840108cea52`).
- **SRC-109** — System level governance of generative AI risks in cross border e-commerce supply chains (`ccfeca2f7bdc`).
- **SRC-110** — Guideline B-15: Climate Risk Management (`8136e1e00218`).
- **SRC-111** — CSA / OSC Notice of Amendments to National Instrument 31-103 — Prohibition of Chargebacks (`70b2dbd2b698`).
- **SRC-112** — Dynamic Adaptive Policy Pathways (DAPP) (`7977e2b1fb07`).
- **SRC-113** — How does Agentic AI Influence the Developer Skills in the Software Industry? — A Literature Review (`323acadcd6fb`).
- **SRC-114** — Loi sur les services bancaires axés sur les consommateurs (L.C. 2026, ch. 3, art. 224) (`dba003d4dce0`).
- **SRC-115** — ReAct: Synergizing Reasoning and Acting in Language Models (`02f512999e00`).
- **SRC-116** — Toolformer: Language Models Can Teach Themselves to Use Tools (`65cd388c2bd5`).
- **SRC-117** — Gorilla: Large Language Model Connected with Massive APIs (`64274c0deb63`).
- **SRC-118** — ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models (`7d2660c4b45e`).
- **SRC-119** — ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs (`9edc88138dde`).
- **SRC-120** — Executable Code Actions Elicit Better LLM Agents (CodeAct) (`fde6ea4999c0`).
- **SRC-121** — LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks (`69bb9cf7eb55`).
- **SRC-122** — AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges (`67346c9a4959`).
- **SRC-123** — Small Language Models are the Future of Agentic AI (`89d5cb83654b`).
- **SRC-124** — Benchmarking LLM Agents for Wealth-Management Workflows (`cb7d7cb81886`).
- **SRC-125** — RFC 2119: Key words for use in RFCs to Indicate Requirement Levels (`c7db148fd518`).
- **SRC-126** — RFC 6902: JavaScript Object Notation (JSON) Patch (`d2627c569ee6`).
- **SRC-127** — RFC 8555: Automatic Certificate Management Environment (ACME) (`1c656cf6f144`).
- **SRC-128** — RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens (`f3a8ff8dc00c`).
- **SRC-129** — RFC 9207: OAuth 2.0 Authorization Server Issuer Identification (`033ca79b0d49`).
- **SRC-130** — RFC 9420: The Messaging Layer Security (MLS) Protocol (`450cb6f07225`).
- **SRC-131** — RFC 9421: HTTP Message Signatures (`1b23937c2708`).
- **SRC-132** — RFC 9562: Universally Unique IDentifiers (UUIDs) (`a3d609ca981c`).
- **SRC-133** — RFC 9700: Best Current Practice for OAuth 2.0 Security (BCP 240) (`7ffb6c499888`).
- **SRC-134** — RFC 9728: OAuth 2.0 Protected Resource Metadata (`148d22364f63`).
- **SRC-135** — RFC 9745: The Deprecation HTTP Response Header Field (`72fc72057a4f`).
- `statut F`: `https://dl.acm.org/doi/10.1145/3143561` (HTTP_403).
- `statut F`: `https://economics.mit.edu/sites/default/files/2024-11/The%20Effects%20of%20Generative%20AI%20on%20High-Skilled%20Work.pdf` (HTTP_404).
- `statut F`: `https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=OJ:L_202401689` (WAF_OR_CHALLENGE:aws-waf).
- `statut F`: `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/` (HTTP_403).
- `statut F`: `https://ieeexplore.ieee.org/document/11580353/` (HTTP_202_NON_FINAL).
- `statut F`: `https://lautorite.qc.ca/` (HTTP_403).
- `statut F`: `https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x` (HTTP_403).
- `statut F`: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/` (WAF_OR_CHALLENGE:g-recaptcha).
- `statut F`: `https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf` (NETWORK_ERROR:URLError).
- `statut F`: `https://publications.gc.ca/site/fra/9.505677/publication.html` (HTTP_202_NON_FINAL).
- `statut F`: `https://standards.cencenelec.eu/dyn/www/f?p=CEN:110:0::::FSP_PROJECT:82555` (HTTP_500).
- `statut F`: `https://www.ciro.ca/rules-and-guidance/investment-dealer-and-partially-consolidated-rules` (HTTP_403).
- `statut F`: `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13776542/fullTextXML` (NETWORK_ERROR:TimeoutError).
- `statut F`: `https://www.fasken.com/en/knowledge/topics/artificial-intelligence` (HTTP_403).
- `statut F`: `https://www.fortunebusinessinsights.com/agentic-ai-market-114233` (HTTP_403).
- `statut F`: `https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027` (HTTP_403).
- `statut F`: `https://www.gleif.org/organizational-identity/lei-vlei/vlei-ecosystem-governance-framework/` (HTTP_404).
- `statut F`: `https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7282.pdf` (HTTP_403).
- `statut F`: `https://www.idc.com/getdoc.jsp?containerId=prUS53863225` (HTTP_403).
- `statut F`: `https://www.iso.org/standard/81230.html` (HTTP_403).
- `statut F`: `https://www.legisquebec.gouv.qc.ca/fr/document/lc/P-39.1` (HTTP_403).
- `statut F`: `https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai` (NETWORK_ERROR:TimeoutError).
- `statut F`: `https://www.mdpi.com/2079-8954/14/4/447` (HTTP_403).
- `statut F`: `https://www.polarismarketresearch.com/industry-analysis/enterprise-agentic-ai-market` (WAF_OR_CHALLENGE:challenges.cloudflare.com).
- `statut F`: `https://www.reuters.com/technology/over-40-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says-2025-06-25/` (HTTP_401).
- `statut F`: `https://www.securities-administrators.ca/news/` (HTTP_403).
- `statut F`: `https://www150.statcan.gc.ca/n1/pub/11-621-m/11-621-m2026010-fra.htm` (HTTP_403).
- `00-liminaire` (`ch00-ancrage.md`): 53 initial → 63 final (`100,0 %` supporté).
- `ch01` (`ch01-ancrage.md`): 21 initial → 38 final (`100,0 %` supporté).
- `ch02` (`ch02-ancrage.md`): 23 initial → 44 final (`100,0 %` supporté).
- `ch03` (`ch03-ancrage.md`): 23 initial → 50 final (`100,0 %` supporté).
- `ch04` (`ch04-ancrage.md`): 31 initial → 53 final (`100,0 %` supporté).
- `ch05` (`ch05-ancrage.md`): 20 initial → 36 final (`100,0 %` supporté).
- `ch06` (`ch06-ancrage.md`): 33 initial → 51 final (`100,0 %` supporté).
- `ch07` (`ch07-ancrage.md`): 21 initial → 43 final (`100,0 %` supporté).
- `ch08` (`ch08-ancrage.md`): 19 initial → 36 final (`100,0 %` supporté).
- `ch09` (`ch09-ancrage.md`): 31 initial → 47 final (`100,0 %` supporté).
- `ch10` (`ch10-ancrage.md`): 17 initial → 34 final (`100,0 %` supporté).
- `ch11` (`ch11-ancrage.md`): 28 initial → 39 final (`100,0 %` supporté).
- `ch12` (`ch12-ancrage.md`): 26 initial → 42 final (`100,0 %` supporté).
- `ch13` (`ch13-ancrage.md`): 15 initial → 44 final (`100,0 %` supporté).
- `ch14` (`ch14-ancrage.md`): 9 initial → 31 final (`100,0 %` supporté).
- `ch15` (`ch15-ancrage.md`): 18 initial → 36 final (`100,0 %` supporté).
- `ch16` (`ch16-ancrage.md`): 19 initial → 40 final (`100,0 %` supporté).
- `ch17` (`ch17-ancrage.md`): 17 initial → 37 final (`100,0 %` supporté).
- `ch18` (`ch18-ancrage.md`): 20 initial → 33 final (`100,0 %` supporté).
- `ch19` (`ch19-ancrage.md`): 9 initial → 39 final (`100,0 %` supporté).
- `ch20` (`ch20-ancrage.md`): 16 initial → 38 final (`100,0 %` supporté).
- `ch21` (`ch21-ancrage.md`): 10 initial → 36 final (`100,0 %` supporté).
- `ch22` (`ch22-ancrage.md`): 13 initial → 33 final (`100,0 %` supporté).
- `ch23` (`ch23-ancrage.md`): 14 initial → 32 final (`100,0 %` supporté).
- `ch24` (`ch24-ancrage.md`): 8 initial → 33 final (`100,0 %` supporté).
- `ch25` (`ch25-ancrage.md`): 13 initial → 28 final (`100,0 %` supporté).
- `ch26` (`ch26-ancrage.md`): 9 initial → 31 final (`100,0 %` supporté).
- `ch27` (`ch27-ancrage.md`): 6 initial → 32 final (`100,0 %` supporté).
- `ch28` (`ch28-ancrage.md`): 7 initial → 29 final (`100,0 %` supporté).
- `ch29` (`ch29-ancrage.md`): 13 initial → 36 final (`100,0 %` supporté).
- `ch30` (`ch30-ancrage.md`): 4 initial → 29 final (`100,0 %` supporté).
- `ch31` (`ch31-ancrage.md`): 11 initial → 32 final (`100,0 %` supporté).
- `ch32` (`ch32-ancrage.md`): 26 initial → 33 final (`100,0 %` supporté).
- `ch33` (`ch33-ancrage.md`): 15 initial → 28 final (`100,0 %` supporté).
- `ch34` (`ch34-ancrage.md`): 14 initial → 28 final (`100,0 %` supporté).
- `ch35` (`ch35-ancrage.md`): 15 initial → 35 final (`100,0 %` supporté).
- `ch36` (`ch36-ancrage.md`): 27 initial → 41 final (`100,0 %` supporté).
<!-- BIBLIOGRAPHIE_BRUTE_FIN -->
