# Interopérabilité et Orchestration en Entreprise Agentique

Corpus documentaire de référence consacré à l'architecture d'entreprise (AE / EA) et à l'architecture de solutions (AS / SA) pour concevoir, intégrer, sécuriser, orchestrer et gouverner des systèmes agentiques à l'échelle de l'organisation, avec un ancrage approfondi sur les services financiers réglementés au Canada fédéral et au Québec (horizon 2024–2035).

Le dépôt rassemble **6 ouvrages PDF** totalisant **2 917 pages** (état de référence : **novembre 2026**) :
- un **livre blanc architectural généraliste** ([`0 - Livre Blanc.pdf`](0%20-%20Livre%20Blanc.pdf), 251 p.) ;
- un **corpus principal en quatre volumes** ([`1`](1%20-%20Compendium%202026.pdf) à [`4`](4%20-%20Plan%20Directeur.pdf), 2 541 p.) couvrant la somme encyclopédique 2026, le cadre normatif, le compendium 2027 et le plan directeur 2028–2035 ;
- un **mémoire d'architecture AE / AS** ([`5 - Memoire.pdf`](5%20-%20Memoire.pdf), 125 p.) qui opère la synthèse et l'alignement formel des quatre volumes précédents.

---

## Vue d'ensemble des ouvrages

| # | Fichier | Sigle / ID | Rôle dans le corpus | Horizon | Pages | Taille | Édition / État |
|---|---|---|---|---|---:|---:|---|
| 0 | [`0 - Livre Blanc.pdf`](0%20-%20Livre%20Blanc.pdf) | Livre blanc EA/SA | Ouvrage de référence généraliste (double entrée EA / SA) | 2026–2027 | 251 | 5,5 Mo | Nov. 2026 (Pipeline Gemini / Wyvern) |
| 1 | [`1 - Compendium 2026.pdf`](1%20-%20Compendium%202026.pdf) | `C26` | Somme encyclopédique (5 livres, 50 chapitres) centrée sur les services financiers réglementés | 2024–2032 | 673 | 18,0 Mo | Nov. 2026 (gel 27 juill. 2026, actualisé 1er nov.) |
| 2 | [`2 - Cadre de Référence.pdf`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) | `CAD26` (`CRE-IA-2026-01`) | Cadre normatif d'architecture d'entreprise (12 principes, 305 exigences vérifiables) | 2026–2030 | 351 | 11,7 Mo | v1.2 — 19 nov. 2026 |
| 3 | [`3 - Compendium 2027.pdf`](3%20-%20Compendium%202027.pdf) | `C27` | Somme consolidée 2027 (exposés sourcés + 31 volets « Mise en œuvre » + recherche) | 2026–2030 | 1 117 | 16,1 Mo | Nov. 2026 (gel 11–14 nov. 2026) |
| 4 | [`4 - Plan Directeur.pdf`](4%20-%20Plan%20Directeur.pdf) | `PD28` | Prospective, architecture cible neutre (52 capacités) et plan directeur adaptatif | 2028–2035 | 400 | 7,5 Mo | 16–19 nov. 2026 |
| 5 | [`5 - Memoire.pdf`](5%20-%20Memoire.pdf) | Mémoire v2.0 | Synthèse exécutive et architecturale unifiée AE / AS des volumes `1` à `4` (~21:1) | 2026–2035 | 125 | 4,2 Mo | v2.0 — 19 nov. 2026 |

---

## Articulation du corpus et parcours de lecture

### Relation entre les six volumes

1. **Volet généraliste autonome** : [`0 - Livre Blanc.pdf`](0%20-%20Livre%20Blanc.pdf) offre une référence complète, agnostique au secteur, structurée autour de la règle hybride **80/20** (80 % de contrôle déterministe, 20 % cognitif), de quatre plans découplés, de trois blueprints instanciables et d'une feuille de route 90 / 180 / 360 jours.
2. **Collection consolidée 2026–2035 (`1` à `5`)** :
   - [`1 - Compendium 2026.pdf`](1%20-%20Compendium%202026.pdf) (`C26`) pose les fondations théoriques, protocolaires, identitaires, réglementaires et opérationnelles en services financiers réglementés.
   - [`2 - Cadre de Référence.pdf`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) (`CAD26` / `CRE-IA-2026-01` v1.2) traduit ces fondations en exigences normatives opposables (`PRIN-01`–`PRIN-12`, 305 `EXIG-*`).
   - [`3 - Compendium 2027.pdf`](3%20-%20Compendium%202027.pdf) (`C27`) élargit l'état de l'art (protocoles 2026–2027, mémoire, orchestration, plateforme, FinOps, recherche scientifique) et ajoute 31 volets d'application technique, 31 ADR et une liste d'homologation en 75 points.
   - [`4 - Plan Directeur.pdf`](4%20-%20Plan%20Directeur.pdf) (`PD28`) projette la trajectoire 2028–2035 sous incertitude profonde (méthode DAPP, 3 scénarios sans probabilité), définit 52 capacités cibles neutres et décline 5 profils financiers (banque, patrimoine, assurance de personnes, assurance de dommages, groupe diversifié).
   - [`5 - Memoire.pdf`](5%20-%20Memoire.pdf) soude les 2 541 pages de `C26`, `CAD26`, `C27` et `PD28` (incluant la réconciliation formelle des modèles de couches — fermeture de la divergence `DIV-02` — et les tables de concordance `CAP` / `PEX` ↔ `EXIG-*`).

### Par où commencer selon votre rôle

| Profil | Point d'entrée recommandé | Approfondissements ciblés |
|---|---|---|
| **Découverte rapide (AE / AS)** | [`5 - Memoire.pdf`](5%20-%20Memoire.pdf) (Synthèse exécutive, pp. 6–8, puis Ch. 1–2) | [`0 - Livre Blanc.pdf`](0%20-%20Livre%20Blanc.pdf) (Liminaire EA/SA, pp. 5–8) |
| **Architecture d'entreprise (AE)** | [`5 - Memoire.pdf`](5%20-%20Memoire.pdf) (Partie IV & Annexes A–C) → [`2 - Cadre de Référence.pdf`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) (Ch. 1–5, 11–15) | [`4 - Plan Directeur.pdf`](4%20-%20Plan%20Directeur.pdf) (Parties III–VI) |
| **Architecture de solutions & Plateforme (AS / SRE)** | [`0 - Livre Blanc.pdf`](0%20-%20Livre%20Blanc.pdf) (Ch. 3–11, 13–14) → [`5 - Memoire.pdf`](5%20-%20Memoire.pdf) (Parties II–III) | [`3 - Compendium 2027.pdf`](3%20-%20Compendium%202027.pdf) (volets « Mise en œuvre », Annexes F–G) |
| **Sécurité, IAM & Risques** | [`2 - Cadre de Référence.pdf`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) (Ch. 8–9) → [`5 - Memoire.pdf`](5%20-%20Memoire.pdf) (Ch. 3, 6, 7) | [`1 - Compendium 2026.pdf`](1%20-%20Compendium%202026.pdf) (Livre II — Faire confiance) et [`4 - Plan Directeur.pdf`](4%20-%20Plan%20Directeur.pdf) (Ch. M-5 PQC) |
| **Conformité, Droit & Audit financier** | [`2 - Cadre de Référence.pdf`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) (Ch. 12 & Annexe D) → [`5 - Memoire.pdf`](5%20-%20Memoire.pdf) (Ch. 10 & Annexe C) | [`1 - Compendium 2026.pdf`](1%20-%20Compendium%202026.pdf) (Livre III) et [`4 - Plan Directeur.pdf`](4%20-%20Plan%20Directeur.pdf) (Ch. M-3, M-14 à M-18) |

---

## Contenu détaillé de chaque PDF

### 0. [`0 - Livre Blanc.pdf`](0%20-%20Livre%20Blanc.pdf) — Ouvrage de référence architecturale (EA / SA)

- **Titre complet** : *Interopérabilité et Orchestration en Entreprise Agentique — Architecture de référence, protocoles ouverts et gouvernance d'exécution pour architectes d'entreprise et de solutions*
- **Production** : Cellule d'architecture automatisée — Pipeline Gemini / Wyvern (novembre 2026) · 251 pages, 59 figures, 52 tableaux.
- **Thèse centrale** : La fiabilité de l'entreprise agentique tient à l'ingénierie des frontières plutôt qu'à la puissance des modèles. Maintenir environ **80 %** du contrôle, des règles, des identités et des mutations en logique déterministe et confiner les **20 %** cognitifs sous contrats typés, télémétrie et réversibilité.
- **Structure** :
  - **Liminaire** : Colophon d'ingénierie 100 % IA et protocole Wyvern, doubles résumés exécutifs (EA et SA), parcours par rôle.
  - **Partie I — Fondations architecturales** (Ch. 1–3) : stratification *Systems of Record / Engagement / Agency*, non-déterminisme et blast radius, échelle d'autonomie `L0`–`L4`, quadruple dette (technique, cognitive, d'intention, CACE), extension TOGAF ADM / ArchiMate (`«Cognitive Actor»`), topologie en 4 plans, *Agent Harness* (SHADI, microVM), partition 80/20 et Structured Outputs (JSON Schema).
  - **Partie II — Interopérabilité** (Ch. 4–6) : MCP sans état (`2026-07-28`), ergonomie ACI (contre *Swagger-to-MCP*), MCP Gateways, couches anti-corruption sur SI patrimonial ; A2A v1.0, fédération AGNTCY (OASF, ADS, SLIM/MLS), ponts inter-cadriciels ; 4 mémoires d'entreprise, Agentic RAG fédéré, souveraineté sémantique et propagation des ACL.
  - **Partie III — Orchestration, chorégraphie et exécution durable** (Ch. 7–9) : critères contre le multi-agents injustifié, topologies dirigées et collaboratives, transfert par *Artifact URI* et *Goal Pinning* ; Event Mesh (Kafka, Solace, NATS, CloudEvents, AsyncAPI) ; *Durable Execution* (Temporal, Restate, Dapr), idempotence, Outbox, Sagas compensatoires et cycles HOTL.
  - **Partie IV — Confiance, sécurité Zero-Trust, observabilité et gouvernance** (Ch. 10–12) : OWASP Agentic Top 10 / MAESTRO, SPIFFE/SPIRE, OAuth 2.0 OBO (`RFC 8693`), Intent Gates (OPA/Cedar), confinement (Firecracker, gVisor, WASM) ; OpenTelemetry GenAI, pipeline EvalOps, SRE agentique et coupe-circuits cognitifs ; gouvernance (registre, 3LoD, Loi 25, LPRPDE, EU AI Act, BSIF E-23, NIST AI RMF, ISO/IEC 42001) et FinOps (FOCUS, coût par résultat).
  - **Partie V — Ingénierie de plateforme, blueprints et transformation** (Ch. 13–15) : *Internal Agentic Platform* (IAP), AI Gateway hybride, GitOps cognitif ; 3 blueprints instanciables (transactionnel réglementé, maillage B2B, exploitation souveraine) ; coexistence BPM/iPaaS/RPA, migration *Strangler Fig*, 12 anti-patrons (`AP-01`–`AP-12`), maturité `M1`–`M5` et feuille de route 90 / 180 / 360 jours.
  - **Annexes A–D** : glossaire bilingue FR-CA/EN, gabarit ADR + liste de contrôle d'homologation EA/SA (40 critères), bibliographie maîtresse (394 sources primaires), bilan d'ancrage atomique Wyvern (1 002 affirmations vérifiées, 88,1 % supportées au premier jet, 119 rectifiées/retirées).

---

### 1. [`1 - Compendium 2026.pdf`](1%20-%20Compendium%202026.pdf) — Somme encyclopédique (`C26`)

- **Titre complet** : *Interopérabilité et orchestration en entreprise agentique — Autonomie encadrée et fabrique de confiance : déployer des agents en services financiers réglementés (2024-2032)*
- **Auteur & édition** : André-Guy Bruneau M.Sc. IT · Édition intégrale de novembre 2026 (faits gelés au 27 juillet 2026, revalidations jusqu'au 29 octobre 2026, actualisation au 1er novembre 2026 en Annexe N) · 673 pages.
- **Fil conducteur** : L'interopérabilité et l'orchestration sont des propriétés à maintenir, gouvernées par un invariant à quatre termes — **découplage, contrat, évolution et exploitation** — appuyé sur une identité opposable, un contrôle de finalité et une provenance attestée.
- **Structure (5 livres, 50 chapitres, 3 annexes)** :
  - **Livre I — Coopérer** (Ch. 1–11) : intégration d'entreprise, pile canonique d'interopérabilité et LCIM, sémantique et ontologies, héritage IAM, ingénierie agentique, mémoire et RAG agentique, multi-agents, anatomie MCP / A2A, découverte et registres, AP2 et AGNTCY, taxonomie des risques protocolaires.
  - **Livre II — Faire confiance** (Ch. 12–21) : identités non humaines (NHI), OAuth/OIDC/SCIM, identité décentralisée (DID/VC), grille des cinq questions (`Q-A` à `Q-E`), Agent Cards signées, passeport d'agent, chaîne de mandat et problème des deux sauts, *Know Your Agent* (KYA), attaques d'identité/délégation, révocation et SOC agentique, transition post-quantique.
  - **Livre III — Encadrer** (Ch. 22–36) : options d'orchestration (`OO1`–`OO4`) et passage à l'échelle ; cadre réglementaire canadien et québécois (BSIF E-23, vide fédéral C-27/C-36, ligne directrice IA de l'AMF et Loi 25 art. 12.1, ACVM 11-348, pont vers les frames déterministes, maillage international) ; vertical financier (services bancaires axés sur les consommateurs, ISO 20022 / Lynx / RTR, banque, assurance, patrimoine, études de cas canadiennes 2025–2026, prospective AP2).
  - **Livre IV — Appliquer, exploiter, produire et composer** (Ch. 37–46) : *AgentMesh* (PEP/PDP Zero-Trust), observabilité, évaluation continue et dérive, indicateurs AgentOps et FinOps, fabrique d'agents, matrice protocoles × exigences réglementaires (constat 0/15 lien natif), architecture de référence unifiée par couches, formalisation ArchiMate, blueprint instancié et feuille de route vers le 1er mai 2027.
  - **Livre V — Livrer et clore** (Ch. 47–50) : provenance logicielle et mise en service, sémantique d'effet (idempotence, compensation, réconciliation), horizon 2027–2032, péremption et protocole de revalidation.
  - **Annexes B, I et N** : 159 fiches sources (`S-001`–`S-159`), bibliographie générale consolidée et actualisation du 1er novembre 2026 (incluant les reports de la Note AMF IA).

---

### 2. [`2 - Cadre de Référence.pdf`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) — Cadre normatif d'architecture d'entreprise (`CAD26` / `CRE-IA-2026-01`)

- **Titre complet** : *Interopérabilité et orchestration en entreprise agentique — Cadre de référence d'architecture d'entreprise*
- **Auteur & version** : André-Guy Bruneau M.Sc. IT · Identifiant `CRE-IA-2026-01`, **version 1.2 (19 novembre 2026)** · 351 pages, 28 figures, 72 tableaux · Licence `CC BY 4.0` / `MIT`.
- **Portée normative** : Énonce **12 principes directeurs** (`PRIN-01` à `PRIN-12`), **10 décisions structurantes** et un registre unifié de **305 exigences vérifiables** (`EXIG-*` : 255 `DOIT`, 34 `NE DOIT PAS`, 16 `DEVRAIT`), incluant en v1.2 les 12 exigences québécoises `EXIG-AMF-01`–`12` issues de la Note AMF IA ainsi que 6 exigences couvrant la transition post-quantique (`NIST IR 8547`), `ACVM 11-348`, `RTR / ISO 20022` et `EN 18286:2026`.
- **Structure (4 parties, 15 chapitres, 8 annexes)** :
  - **Partie I — Fondements** (Ch. 1–4) : objet, parcours par rôle, degrés d'obligation, contexte et enjeux, définitions normatives, 12 principes directeurs et arbitrages de tensions.
  - **Partie II — Architecture, interopérabilité et orchestration** (Ch. 5–8) : architecture de référence en **6 couches** (canaux, orchestration, agents, médiation, outils, systèmes d'enregistrement) et **3 plans transversaux** (identité, observabilité, gouvernance), correspondance ABB/SBB, mémoire ; interopérabilité (`MCP 2026-07-28`, `A2A 1.0`, CloudEvents/AsyncAPI, catalogue trimestriel) ; orchestration (simplicité d'abord, 8 patrons autorisés, anti-patrons proscrits, exécution durable et Sagas) ; autonomie graduée (`N0`–`N4`), paliers de risque d'outils (`P0`–`P3`) et approbation humaine signée.
  - **Partie III — Confiance et exploitation** (Ch. 9–10) : confiance zéro, NHI, délégation `RFC 8693`, passerelle d'agents obligatoire, défense contre l'injection et OWASP ASI, isolation de code ; observabilité `OpenTelemetry GenAI`, évaluation en 3 étages, audit chaîné et FinOps (enveloppes budgétaires).
  - **Partie IV — Gouvernance, conformité et mise en œuvre** (Ch. 11–15) : gouvernance (RACI, modèle en étoile, cycle de vie), conformité (Loi 25, BSIF E-23, RIA / EU AI Act, NIST AI RMF, ISO/IEC 42001), approvisionnement et anti-verrouillage, modèle de maturité en 5 niveaux, feuille de route en 4 phases (calée sur 2027–2030) et plan des 90 premiers jours.
  - **Annexes A–H** : grille d'homologation, gabarit de fiche d'agent, exemples de contrats, registre des 305 exigences, glossaire, audit et validation des sources, bibliographie (449 + 22 références) et actualisation de novembre 2026.

---

### 3. [`3 - Compendium 2027.pdf`](3%20-%20Compendium%202027.pdf) — Édition consolidée 2027 (`C27`)

- **Titre complet** : *Interopérabilité et Orchestration en Entreprise Agentique — Compendium 2027 (Protocoles, sémantique, orchestration, architecture, confiance et gouvernance)*
- **Production** : Corpus Agentique — Production autonome IA, usage consultatif AE / AS (novembre 2026 ; faits arrêtés aux 11–14 novembre 2026) · 1 117 pages · Licence `CC BY 4.0` / `MIT`.
- **Construction** : Réunit en un seul volume un exposé de référence sourcé (50 chapitres) et une édition d'architecture appliquée comptant **31 volets « Mise en œuvre »** (architectures prescrites, extraits de code, décisions d'architecture ADR, listes de contrôle et fil rouge illustratif *Groupe Boréal Inc.*).
- **Structure (Ouverture, 10 parties, 50 chapitres, 8 annexes)** :
  - **Ouverture** : tissu conjonctif en 6 couches + 2 plans transversaux, 6 parcours par rôle, échelle `L0`–`L4`, carte des standards 2027.
  - **Parties I à IV** (Ch. 1–22) : fondements et état des lieux 2026–2027 ; protocoles MCP, A2A, périphériques, découverte/registres, web et commerce agentique (`AP2`, `x402`), géopolitique des standards (AAIF) ; couche sémantique, ingénierie du contexte, mémoire distribuée bi-temporelle et données prêtes pour les agents ; topologies d'orchestration, découplage déterministe/probabiliste, exécution durable, événements, cadriciels, fiabilité et humain dans la boucle.
  - **Parties V à VIII** (Ch. 23–43) : architecture d'entreprise, passerelles, intégration au patrimoine sans API (CUA, RPA/APA, mainframes), fédération des silos SaaS, convergence IT/OT et périphérie ; identité NHI, autorisation/délégation, menaces OWASP ASI, bacs à sable/coupe-circuits, OpenTelemetry GenAI, ADLC/chaos ; cadres juridiques internationaux, responsabilité, souveraineté, Canada/Québec, gouvernance interne ; FinOps (*Cost-per-Outcome*), modèle opérationnel, études de cas et maturité (niveaux 1 à 5).
  - **Parties IX et X** (Ch. 44–50) : approfondissements (plan de données d'inférence et routage cognitif, réseaux B2B fédérés, inférence confidentielle et IA physique, usine logicielle agentique, Agentic DataOps et distillation LLM → SLM) et recherche scientifique (revue de littérature, veille technologique, projection 2027–2030 et étude de marché).
  - **Annexes A–H** : glossaire FR-EN, fiches protocoles, grilles d'évaluation, chronologie 2024–2028, bibliographie et niveaux de preuve, registre des **31 ADR** (`ADR-001`–`ADR-031`), listes de contrôle d'homologation avant production (**75 points PRR**) et index des standards.

---

### 4. [`4 - Plan Directeur.pdf`](4%20-%20Plan%20Directeur.pdf) — Prospective et architecture cible 2028–2035 (`PD28`)

- **Titre complet** : *Interopérabilité et Orchestration en Entreprise Agentique — Prospective, architecture cible et plan directeur 2028-2035*
- **Production** : Corpus Agentique — Production autonome IA (état de référence : 16–19 novembre 2026 ; statut informatif) · 400 pages · Licence `CC BY 4.0` / `MIT`.
- **Thèse vérifiée** : Toutes les échéances fermes qui lient le secteur financier canadien et québécois d'ici 2035 portent sur la **preuve, la gouvernance, la transparence et la cryptographie**, jamais sur une obligation d'autonomisation. La cible invariante de l'institution est le **noyau de contrôle possédé en propre**.
- **Rigueur documentaire** : Appuyé sur **98 textes primaires bruts** (`L+`) conservés localement, **67 ancres chronologiques**, **27 signaux de veille** (`SIG`), séparation explicite des sources inaccessibles (statut `F`) et double recollation indépendante (`CA-16`) sur 120 énoncés distincts (2 tirages de 60 énoncés, 100 % conformes après correction).
- **Structure (6 parties, 26 chapitres `M-1` à `M-26`, 8 annexes)** :
  - **Parties I–II — Cadrage et Prospective 2028–2035** (`M-1` à `M-8`) : méthode, marques d'énoncé (`[D]`, `[A]`, `[C]`), état de référence 2027, calendriers réglementaire et prudentiel, normalisation, transition post-quantique de l'identité et de la délégation, capacités des agents, marché/coûts/énergie/compétences, et **3 scénarios DAPP sans probabilité** (A : Socle étendu, B : Archipel de plateformes propriétaires, C : Blocs juridictionnels).
  - **Partie III — Architecture cible 2035** (`M-9` à `M-13`) : architecture neutre vis-à-vis des éditeurs en **5 couches horizontales** et **3 volets de contrôle**, **15 principes** (`PRI-001`–`PRI-015`), **52 capacités cibles** (`CAP-001`–`CAP-052` : **42 invariantes sans regret** + **10 conditionnelles**), autonomie par domaine et classe de décision, révision des 31 ADR et 12 décisions nouvelles (`DEC-001`–`DEC-012`).
  - **Partie IV — Profils sectoriels** (`M-14` à `M-18`) : déclinaison réglementaire et capacitaire pour **Banque**, **Gestion de patrimoine**, **Assurance de personnes**, **Assurance de dommages** et **Groupe financier diversifié** (24 propositions d'exigences sectorielles `PEX`).
  - **Parties V–VI — Feuille de route et Pilotage** (`M-19` à `M-26`) : analyse d'écarts, trajectoire en **3 paliers franchis sur preuve** (Palier 1 : 2028–2029, Palier 2 : 2030–2032, Palier 3 : 2033–2035), portefeuille d'initiatives (`INI`), **15 portes** (`POR`), registre de veille (27 `SIG`) et gestion des risques du plan.
  - **Annexes A–H** : calendrier consolidé 2027–2035, registres des capacités, principes, décisions, portes, initiatives et `PEX`, matrice de traçabilité, correspondances inter-modèles, registre de veille, glossaire et bibliographie.

---

### 5. [`5 - Memoire.pdf`](5%20-%20Memoire.pdf) — Mémoire d'architecture unifié AE / AS (v2.0)

- **Titre complet** : *Interopérabilité et Orchestration en Entreprise Agentique — Architecture de référence, patrons de solutions et trajectoire 2026-2035 — Mémoire sous forme de livre blanc à l'intention des architectes d'entreprise et des architectes de solutions*
- **Production** : Corpus Agentique — Production autonome IA, **version 2.0 (19 novembre 2026)** · 125 pages · Licence `CC BY 4.0` / `MIT`.
- **Rôle clé** : Point d'entrée synthétique du corpus consolidé. Compresse (~21:1) les 2 541 pages de `C26`, `CAD26`, `C27` et `PD28` (plus la Note AMF IA et l'extension `CRE-IA-2027 v2.0`), ferme la divergence `DIV-02` en raccordant le modèle 5 couches / 3 volets de `PD28` aux 6 couches de `CAD26`, et scelle **10 thèses structurantes (`T1`–`T10`)** ainsi que **6 décisions conjointes AE ↔ AS**.
- **Structure (4 parties, 12 chapitres, 6 annexes)** :
  - **Synthèse exécutive** : contrat de lecture croisé AE / AS, thèses `T1`–`T10`, 6 décisions conjointes, trajectoire unifiée 90 jours → 18 mois → Paliers `P1`–`P3`.
  - **Partie I — Problème architectural et ossature commune** (Ch. 1–2) : constat empirique fin 2026, loi de Lusser, sobriété agentique, réconciliation des modèles (`DIV-02`) et séparation ABB → SBB.
  - **Partie II — Chantier de l'architecte de solutions** (Ch. 3–6) : couche protocolaire (`MCP`, `A2A`, événements) et passerelle PEP à 9 contrôles ; sémantique métier, contexte compilé, mémoire CoALA et encapsulation patrimoniale (`EBCDIC`/`COMP-3`, CUA, IT/OT) ; orchestration hybride (`OO1`–`OO4`), exécution durable et Sagas ; autonomie graduée et liaison cryptographique (`CIBA` + `FIDO2` + `JCS SHA-256`).
  - **Partie III — Socle partagé AE / AS** (Ch. 7–9) : fabrique de confiance (NHI `SPIFFE`, `RFC 8693`, `DPoP`, défense anti-injection `CaMeL`, PKI 47 jours et PQC `ML-DSA` / `SCITT`) ; observabilité à double couloir PII (`OpenTelemetry`), audit JCS, évaluation `E1`–`E3` et FinOps CPO ; plan d'inférence, six substrats d'état, confidentialité matérielle, continuité bimodèle et réseaux B2B.
  - **Partie IV — Chantier de l'architecte d'entreprise** (Ch. 10–12) : conformité dès la conception (Canada, Québec, UE) et 5 profils financiers ; modèle opérationnel à trois lignes, usine logicielle interne et approvisionnement réversible ; homologation unifiée et trajectoire adaptative DAPP.
  - **Annexes A–F** : tables de concordance 2026–2035 (`CAP`/`PEX` → `EXIG-*`), catalogue de poche des décisions AE / AS, grille unifiée d'homologation avant mise en production, guide d'orientation vers les 2 541 pages sources, glossaire unifié (**385 entrées**) et bibliographie primaire sélective (**70 normes, lois et études**).

---

## Repères transversaux (architecture, protocoles et échéances)

- **Principe directeur commun** : Le contrôle déterministe, l'identité vérifiable et la capacité de preuve précèdent toute extension d'autonomie (du flux déterministe à l'agent unique outillé, puis au multi-agents uniquement sur gain mesuré).
- **Pile protocolaire et technique de référence** :
  - *Agent ↔ Outil* : `MCP` (révision `2026-07-28`, sans état) derrière une passerelle d'agents (PEP) et un registre/catalogue gouverné.
  - *Agent ↔ Agent* : `A2A` (`v1.0` / `v1.0.1`, *Agent Cards* signées) et fédération `AGNTCY` (`OASF`, `SLIM`/`MLS`).
  - *Événements et exécution durable* : `CloudEvents 1.0`, `AsyncAPI 3.0`, moteurs durables (`Temporal`, `Restate`, `Dapr`), idempotence et Sagas compensatoires.
  - *Identité, sécurité et observabilité* : `SPIFFE`/`SPIRE`, `OAuth 2.0/2.1` (`RFC 8693`, `RFC 8707`, `RFC 9396`, `DPoP`), `CIBA`/`FIDO2`, `OPA`/`Cedar`, `OWASP ASI01–10`, `OpenTelemetry GenAI` (`gen_ai.*`), `FOCUS` (FinOps).
- **Échéances réglementaires et cryptographiques structurantes** :
  - **En vigueur** : Loi 25 du Québec (notamment art. 12.1 sur les décisions exclusivement automatisées et ÉFVP), avis `ACVM 11-348`, transparence `EU AI Act` art. 50 (août 2026).
  - **15 mars 2027** : abaissement de la durée de validité des certificats TLS à 100 jours (puis 47 jours le **15 mars 2029**).
  - **1er mai 2027** : entrée en vigueur de la ligne directrice **BSIF E-23** (risque de modèle incluant l'IA générative et agentique) et prise d'effet de la ligne directrice IA de l'**AMF** au Québec.
  - **2 décembre 2027** : application de l'Annexe III (systèmes à haut risque) du règlement européen sur l'IA (`EU AI Act`, calendrier révisé).
  - **2028** : interdiction des rétrofacturations en gestion de patrimoine (1er oct. 2028) et divulgation portée 3 sous **BSIF B-15**.
  - **2030–2035** : fenêtre de transition post-quantique coordonnée du secteur financier du G7 (`NIST IR 8547`, `FIPS 203–205`) et temporisation des lois financières fédérales canadiennes (**30 juin 2033**).

---

## Statut éditorial, périmètre probatoire et licences

- **Usage consultatif** : Les ouvrages de ce dépôt constituent des référentiels techniques et architecturaux à des fins de consultation par les architectes d'entreprise et de solutions. Ils ne constituent **ni un avis juridique, ni une homologation réglementaire**.
- **Périmètre démontré vs extrapolations** : L'appareil réglementaire et probatoire des volumes `1` à `5` porte sur les **services financiers réglementés** (Canada fédéral, Québec et obligations transfrontalières UE) et sur l'ingénierie de contrôle déterministe hors modèle. Les mentions hors finance (santé, IT/OT, industrie, énergie, secteur public non financier) y sont balisées comme extrapolations illustratives.
- **Transparence sur la production IA** : Les volumes [`0`](0%20-%20Livre%20Blanc.pdf), [`3`](3%20-%20Compendium%202027.pdf), [`4`](4%20-%20Plan%20Directeur.pdf) et [`5`](5%20-%20Memoire.pdf) documentent explicitement leur production et leur vérification automatisées par agents d'IA (ancrage atomique Wyvern, recollation sur textes bruts `CA-16`, séparation des textes inaccessibles de statut `F`, absence de relecture humaine intégrale). Les volumes [`1`](1%20-%20Compendium%202026.pdf) et [`2`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf) portent la mention d'auteur d'**André-Guy Bruneau M.Sc. IT** (le volume `2` v1.2 précisant également le régime de production autonome IA pour consultation AE / AS).
- **Licences mentionnées dans les documents** : Les volumes [`2`](2%20-%20Cadre%20de%20R%C3%A9f%C3%A9rence.pdf), [`3`](3%20-%20Compendium%202027.pdf), [`4`](4%20-%20Plan%20Directeur.pdf) et [`5`](5%20-%20Memoire.pdf) indiquent une diffusion sous **CC BY 4.0** (textes, figures et registres) et **MIT** (code, scripts et outils). Les volumes [`0`](0%20-%20Livre%20Blanc.pdf) et [`1`](1%20-%20Compendium%202026.pdf) ne comportent pas de mention de licence explicite en page de titre.
