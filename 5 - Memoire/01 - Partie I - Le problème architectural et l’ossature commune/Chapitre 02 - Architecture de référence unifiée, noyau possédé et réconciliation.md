# Chapitre 2 — Architecture de référence unifiée, noyau possédé et réconciliation des modèles (DIV-02)

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[CAD26 Sommaire exécutif, ch. 4 | PRIN-01..12, ch. 5 § 5.1–5.5, Tableau 12 | EXIG-ARC-01..25, ch. 11 | EXIG-GOV-07, EXIG-GOV-08, EXIG-GOV-16, EXIG-GOV-17, EXIG-GOV-18, ch. 12 | EXIG-CON-02, EXIG-CON-06, ch. 13, 14, Annexes A, D, H]` · `[C26 ch. 7 § 7.5, ch. 41 § 41.1, ch. 42–44]` · `[C27 § 0.1, § 0.4, ch. 1, 20, 23, 26, 27, 43, Annexe F]` · `[PD28 M-2 § 2.4, M-9 à M-13 | PRI-001..015, CAP-001..052, DEC-001..012, PEX-041, Annexe E]`.

*Question directrice : Quelle ossature architecturale unique permet à l’AE et à l’AS de parler le même langage entre le cadre normatif 2026, le compendium 2027 et la cible 2035 ?*

**Thèse du chapitre :** Les cadriciels d’agents rompent leur compatibilité en moins de douze mois `[M]`, et les suites commerciales demeurent fermées sur le plan de contrôle `[É]`. La confrontation sur pièce des quatre volumes ferme `DIV-02`. Elle raccorde les six couches normatives de 2026 aux cinquante-deux capacités cibles de 2028–2035 `[N]`. L’institution réglementée doit posséder son noyau de contrôle et fédérer les silos selon la gravité des données. Elle sépare chaque bloc d’architecture neutre (`ABB`) de ses solutions substituables (`SBB`) P : PRI-001 P : PRI-015 P : DEC-007 E : EXIG-ARC-01 E : EXIG-ARC-17 E : EXIG-ARC-19 E : EXIG-ARC-20 E : EXIG-ARC-21.

## 2.1 Réconciliation sur pièce des quatre découpages et fermeture de DIV-02

Les quatre volumes juxtaposent quatre découpages : six couches et deux piliers (`C27 § 0.1`), six couches et cinq points de contrôle (`C26 ch. 43`), six couches et trois plans transversaux (`CAD26 § 5.2–5.3`), puis cinq couches et trois volets (`PD28 M-9`). Faute d’accès au dossier `2026/`, `PD28 Annexe E.1` avait reconstitué par déduction les couches de `CAD26`. Elle avait aussi marqué les vingt-quatre `PEX` du statut provisoire `corpus_2026_absent` (`DIV-02`). L’inspection sur pièce de `CAD26` (`CRE-IA-2026-01` v1.2, pp. 37–43) résorbe cet écart.

Sur l’horizon 2026–2035, le mémoire retient le pivot de `PD28 M-9` : **cinq couches horizontales (**`C1` **à** `C5`**) et trois volets de contrôle (**`Plan A`**,** `Plan B`**,** `Plan C`**)**. Ce pivot dérive de `C27 ch. 23 § 23.1`, palliant l’absence de pilier registre en `C27 § 0.1`. Confronté à `CAD26 § 5.2`, il rétablit les **six vraies couches normatives de 2026** et rectifie trois suppositions de `PD28 Annexe E.1` :

1. **Couche 1 — Canaux et déclencheurs** (`CAD26` p. 37) : interfaces et déclencheurs authentifiant le mandant et ouvrant la trace, zéro logique ni invite E : EXIG-ARC-03 E : EXIG-ARC-04 (`C1 interaction`, Couche 5 de `C27 § 0.1`).
2. **Couche 2 — Orchestration et état** (`CAD26` pp. 37–38) : moteur durable, routeur sans octroi de droit, `A2A` et mémoire de travail E : EXIG-ARC-05 E : EXIG-ARC-06 E : EXIG-ARC-07, distincts de la boucle d’agent en Couche 3 (réunis sous `C2`).
3. **Couche 3 — Agents et exécution cognitive** (`CAD26` pp. 38–39) : boucle d’agent, mémoire procédurale, **passerelle de modèles** (alias sous `EXIG-ARC-09`, `DEVRAIT`) et **bac à sable de code** E : EXIG-ARC-08 E : EXIG-ARC-09 E : EXIG-ARC-10 E : EXIG-ARC-24. *Rectification 1* : modèles et confinement siègent en Couche 3 de `CAD26` (non en Couche 6 supposée), soit `C5 modeles`.

4. **Couche 4 — Médiation et connectivité** (`CAD26` pp. 39–40) : passerelle d’agents (`PEP`), catalogue d’entreprise et bus d’événements E : EXIG-ARC-01 E : EXIG-ARC-11 E : EXIG-ARC-12 E : EXIG-ARC-13.
5. **Couche 5 — Outils et données** (`CAD26` pp. 40–41) : serveurs `MCP`, adaptateurs `OpenAPI` (`EXIG-ARC-15`, `DEVRAIT`), index, graphes et mémoires épisodique et sémantique E : EXIG-ARC-15 E : EXIG-ARC-16 E : EXIG-ARC-22 E : EXIG-ARC-23 E : EXIG-ARC-25. *Rectification 2* : nulle Couche 3 « Connaissance » dans `CAD26` ; `C3 contexte-connaissance` couvre Couches 2, 3 et 5.
6. **Couche 6 — Systèmes d’enregistrement** (`CAD26` p. 41) : cœurs bancaires, assurantiels, ERP et CRM gardant intégrité métier et référence de trace (`EXIG-ARC-18`, `DEVRAIT`) E : EXIG-ARC-14 E : EXIG-ARC-17 E : EXIG-ARC-18. *Rectification 3* : l’enregistrement siège en Couche 6 (non C5), encapsulé sous `C4 acces`.

Les trois plans transversaux s’alignent terme à terme entre `PD28 M-9 § 9.2` et `CAD26 § 5.3` (p. 42). L’Annexe A relie ainsi les `52/52` capacités aux `305/305` **exigences** `CAD26` **v1.2** (`255 DOIT`, `34 NE DOIT PAS`, `16 DEVRAIT`, intégrant `12 EXIG-AMF` et `6` ajouts PQC/ACVM/RTR/EN 18286). Chaque lien porte un type explicite (`couverture_directe`, `ancrage_extension` ou `comble_lacune_2026`). Les `24/24` `PEX` se ventilent en `13` **spécialisations** et `11` **comblements** de lacunes de 2026 (`LSAC` art. 171, muraille art. 416, `ISO 20022 pacs.008` du *Real-Time Rail* `RTR`, `OCRI 3400/3241`, `NI 31-103`, `L.C. 2017, ch. 3`, post-quantique vie/rentes, `LDPSF` et `BSIF B-15`).

> **[Figure]**
> - Architecture unifiée (5 couches + 3 volets) ↔ 6 couches CAD26 § 5.2 Résorption DIV-02 et frontière noyau de contrôle possédé / suites SaaS
> - Pivot PD28 (5 couches) DIV 6 vraies couches CAD26 § 5.2
> - C1 · Interaction CAP-001..006
> - Canaux, CIBA, Loi 25
> - C2 · Agents & orch. CAP-007..014
> - OO3/OO4 [S], Saga, A2A
> - C3 · Contexte & conn. CAP-015..021
> - ACL, sémantique, CoALA
> - C4 · Accès & outils CAP-022..028
> - PEP, MCP, COMP-3, OT
> - C5 · Modèles CAP-029..034
> - Routage, MicroVM, 6 sub.
> - 1. Canaux & déclencheurs
> - Zéro logique · ARC-03..04
> - 2. Orchestration & état
> - Durable, A2A, mém. trav.
> - 3. Agents & exéc. cognit.
> - Agents, modèles, MicroVM
> - 4. Médiation & connect.
> - PEP, catalogue, bus EVT
> - 5. Outils & données
> - MCP, index, mém. ép./sém.
> - 6. Syst. d’enregistrement
> - Cœurs via API · ARC-17
> - Noyau de contrôle possédé — 42 CAP invariantes (Plans A, B, C)
> - Plan A · Identité
> - NHI SPIFFE, RFC 8693
> - PDP hors modèle, PQC
> - Plan B · Obs./FinOps
> - Double couloir, JCS
> - Éval. E1–E3 & CPO
> - Plan C · Gouvernance
> - Registre 7 états, E-23
> - 3 lignes & clauses APP
> - Frontière SaaS & SBB remplaçables (EXIG-ARC-21) :
> - Mono-silo sous PEP, NHI propre, export OTel, arrêt propre (max N2)
> - DIV-02 : Modèles en C3 CAD26 (non C6) · C3 Contexte → C2/C3/C5 · C6 Enreg.

*Fig. 2. – Architecture de référence unifiée à 5 couches et 3 volets de contrôle, raccordement exact aux 6 couches de CAD26 § 5.2 (fermeture DIV-02) et délimitation du noyau possédé face aux suites SaaS.*

| Pivot (`PD28 M-9` / `C27 § 23.1`) | `CAD26 § 5.2–5.3` (6 couches + 3 plans) | `C26 ch. 43` | `C27 § 0.1` (6 couches + 2 piliers) | Rattachement `CAP` / `EXIG-*` |
| --- | --- | --- | --- | --- |
| **C1.** `interaction` | Couche 1 : Canaux et déclencheurs | Nulle couche UI (`Tab. 43.1` `[S]`) ; `Z2 → PC3` `[S]` en C3 | C5 Interaction humain-agent | `CAP-001..006` (`4` inv., `2` cond.) ; `EXIG-ARC-03, 04, EXIG-AUT-09, 12..16, 19..23` |
| **C2.** `agents-orchestration` | Couche 2 : Orchestration et état + volet Agents (C3) | C3 Orchestration (`OO1–OO4, PC1–PC3, Z2` `[S]`), C1 `A2A` | C4 durable + C3 horizontale | `CAP-007..014` (`6` inv., `2` cond.) ; `EXIG-ARC-02, 05..07, 13, EXIG-INT-04, 05, 11, 22, EXIG-ORC-01..30, EXIG-A2A-01..15, EXIG-EVT-01..10, EXIG-AUT-17` |
| **C3.** `contexte-connaissance` | Travail (C2), procédurale (C3), Couche 5 : Outils et données | Nulle couche dédiée (`Tab. 43.1` `[S]`) ; `ch. 2, Z5, PC4` `[S]` | C2 Sémantique, contexte, mémoire | `CAP-015..021` (`7` inv.) ; `EXIG-ARC-16, 22..25, EXIG-INT-01, 02, 12..16, 19` |
| **C4.** `acces` | C4 Médiation et connectivité, C5 Outils et données, C6 Systèmes d’enregistrement | C4 Maillage (`ch. 37`), C1 `MCP`, `Z4` `[S]` | C1 IT/OT + C3 fédération | `CAP-022..028` (`4` inv., `3` cond.) ; `EXIG-ARC-01, 11, 12, 14, 15, 17, 18, 21, EXIG-INT-03, 06, 07, EXIG-MCP-01..22` |
| **C5.** `modeles` | Couche 3 : Agents et exécution cognitive (modèles, confinement) | Nulle couche modèles/bacs (`Tab. 43.1` `[S]`) ; `PC5/Z5` `[S]` en C4 | Socle silicium, confinement, inférence | `CAP-029..034` (`4` inv., `2` cond.) ; `EXIG-ARC-08..10, EXIG-SEC-08..17` |
| **Plan A.** `controle-identite-securite` | Plan transversal A : Identité et sécurité | C2 Identité/registre (fabrique) + C4 Maillage (`PC5, Z5` `[S]`) | Pilier gauche *Zero Trust*, `NHI` | `CAP-035..041` (`6` inv., `1` cond.) ; `EXIG-IAM-01..21, EXIG-SEC-01..07, 18..26, EXIG-AUT-03, 08, 10, 11, EXIG-INT-21` |
| **Plan B.** `controle-observabilite-finops` | Plan transversal B : Observabilité, évaluation et FinOps | C5 Exploitation — `AgentOps` (`ch. 38–40` ; `Z1, Z3/PC4` `[S]`) | Pilier droit *AgentOps*, *FinOps* | `CAP-042..046` (`5` inv.) ; `EXIG-OBS-01..13, EXIG-EVA-01..06, EXIG-FIN-01..10` |
| **Plan C.** `controle-gouvernance-registre` | Plan transversal C : Gouvernance et registre | C6 Gouvernance (`ch. 25–30`), C2 registre, `ch. 41` `[S]` | C6 gouvernance/B2B, deux piliers | `CAP-047..052` (`6` inv.) ; `EXIG-ARC-19, 20, EXIG-AUT-01, 02, 04..07, 18, EXIG-INT-08..10, 17, 18, 20, 23, EXIG-GOV-01..20, EXIG-CON-01..26, EXIG-APP-01..17` |

*Note méthodologique (*`Annexe A.1` *vs* `A.3`*) —* Ce tableau et `Annexe A.1` ventilent sans doublon les `305 EXIG-*` v1.2 par ancrage architectural `CAD26 § 5.2–5.3`. L’`Annexe A.3` les rattache aux capacités `CAP-001..052` (`42` inv., `10` cond. ; `5` lacunes `2026` sans `EXIG-*` direct : `CAP-025, 028, 033, 046, 052`).

## 2.2 Effectivité du plan de contrôle, points PC1–PC5 et harmonisation des échelles

Un plan de contrôle ne gouverne effectivement que sous trois conditions (`C27 ch. 23 § 23.2` ; `CAD26` Décision 2) E : EXIG-ARC-01 E : EXIG-GOV-07 E : EXIG-GOV-08 E : EXIG-OBS-11 E : EXIG-OBS-12. Il exige un **chemin réseau obligé** (`PEP`), un **registre central faisant seul autorité** (zéro justificatif sans fiche active) et une **preuve immuable** émise hors de portée du modèle.

Ce cadre dissipe les quatre acceptions de *(agentic) control plane* (`C26 ch. 7 § 7.5`) et sépare **fabrique d’identité** et **fabrique d’agents** (`C26 ch. 41 § 41.1`, `ch. 43`). Il distingue aussi la sauvegarde d’état de **cinq points de contrôle obligatoires** (`PC1–PC5`, construit `[S]` en `C26 § 43.3` Tableau 43.2, opposables sans passeport d’agent). `PC1` couvre la décision et la notification horodatée (`Loi 25 art. 12.1`). `PC2` scelle la trace d’instance (`Z1` `[S]`) et `PC3` impose l’arrêt humain sur effets défaisables (`Z2` `[S]`). `PC4` sépare adaptation éphémère et évolution persistante (`Z3` `[S]`, `ACVM 11-348`, `BSIF E-23`). Enfin, `PC5` assure le confinement local (`Z5` `[S]`), `Z4` `[S]` restant une frontière d’abstraction (`§ 43.6`).

L’Annexe A.2 unifie les échelles de maturité et d’autonomie (`PD28 M-12` ; `CAD26 ch. 8, 14` ; `C27 § 0.4, § 43.1` ; `C26 ch. 1, 14, 22`, `0` modèle de maturité au socle en `§ 43.5`) P : PRI-006 :

- **Maturité par domaine (**`D1–D8`**, au critère le plus faible)** : pont analytique `[S]` croisant `5/7` niveaux `LCIM` (`C26 Tableau 7.1`) et les `3` approches `ISO 11354-1 FEI` (*Intégrée*, *Unifiée*, *Fédérée*, `C26 § 1.2.1`) — `Stade 0` (*Sans agents*, `N0`, FEI *Intégrée*) → `Stade 1` (*Pilotes isolés*, 90 j, `N0–N1`) → `Stade 2` (*Usage encadré*, Niveaux 2–3 *Défini* de `CAD26`, sémantique / FEI *Unifiée* `[S]`, seuil minimal réglementé) → `Stade 3` (*Orchestration en production*, Niveau 4 *Géré*, pragmatique / FEI *Unifiée* `[S]`, cible majoritaire) → `Stade 4` (*Inter-organisations*, Niveau 5 *Optimisé*, dynamique / FEI *Fédérée* `[S]`, sélectif en Palier 3 sur 2033–2035 C : A, C ; SIG-007 et exclu en `D2` `Stades 2–3` comme en `D6`, coté `Stade 3` interne en `PD28 M-12` malgré `3–4` en `M-15`/`M-18`).
- **Autonomie par acte** : hors classe (`N0` / `L0` / `OO3` pur `[S]`), `Classe 1` (*Lire*, `N1` sur `P0–P1`), `Classe 2` (*Agir réversible*, `N3` borné ou `N2` sur `P2`), `Classe 3` (*Agir matériel*, `N2` par défaut, `JCS SHA-256`, `PC3` `[S]`), `Classe 4` (*Irréversible critique*, `P3` jamais seul même en `N4`, `CIBA` + `FIDO2` `≤ 15 min`), `Classe 5` (*Visant une personne*, plafonnée `N2` sous `EXIG-CON-02` et règle d’or `EXIG-AUT-07`, `OO3/OO4` `[S]`, `Q-E` `[S]`), et `Classe 6` (*Hors mandat*, `NX` interdit sans dérogation E : EXIG-AUT-03 E : EXIG-GOV-17).

## 2.3 Noyau de contrôle possédé, gravité des données et séparation des systèmes

Les cadriciels d’agents périment en moins de douze mois (`C27 ch. 20`). De plus, les suites commerciales restent **« ouvertes sur le fil et fermées sur le plan de contrôle »** (`C27 § 26.9, § 27.1–27.4` ; `CAD26 § 2.4, § 13.1`). Elles enferment identité, politiques, mémoire, traces et facturation sans traiter un agent tiers à égalité avec un agent natif.

Le portefeuille (`PD28 M-10–M-11`) ancre donc `42` **capacités invariantes sans regret** dans un **noyau de contrôle possédé** P : PRI-015 P : DEC-007 E : PRIN-09 E : EXIG-ARC-19. Ce noyau couvre registre (`CAP-047`), identités `SPIFFE` et jetons (`CAP-035, 036`), politiques et arrêt (`CAP-037, 039`), passerelles (`CAP-022, 029`), double couloir et audit (`CAP-042, 049`), et contrats (`CAP-015, 018`). Il s’accompagne de `10` **capacités conditionnelles** (`CAP-004, 006, 013, 014, 025, 027, 028, 033, 034, 041`) activées sur signaux jusqu’en 2035 C : A, B, C ; SIG-002, SIG-016.

La frontière progicielle suit la **gravité des données** P : CAP-013 P : DEC-007 E : EXIG-ARC-21. Une tâche mono-silo peut rester dans l’agent SaaS sous les contrôles cumulatifs de `EXIG-ARC-21` : fiche au registre, transit `PEP` vers l’externe, clauses `EXIG-APP-05, 06, 08, 13`, schémas épinglés `EXIG-INT-02`, arrêt propre (`OAuth`/`CAEP`) testé chaque trimestre (`EXIG-SEC-26`) et plafond `N2` sans approbation `P3` équivalente à `EXIG-AUT-12`. Dès deux silos traversés, l’orchestration remonte dans le moteur durable possédé. Elle propage mandant, trace et budget dans chaque appel descendant E : EXIG-ARC-02, avec étiquette immuable d’entité juridique sur actifs et mémoire P : CAP-021 P : PEX-041 E : EXIG-CON-06. Le *System of Action* reste séparé des *Systems of Record* (`ADR-001`, `C27 § 1.8`) E : EXIG-ARC-14 E : EXIG-ARC-17 E : EXIG-ARC-18. Tout `SQL` direct est proscrit : chaque écriture passe par une interface validant intégrité, idempotence et trace (`EXIG-ARC-18`, `DEVRAIT`).

## 2.4 Blocs ABB → SBB substituables (2026), arbitrage des principes et ArchiMate

À l’homologation, chaque solution documente ses **blocs d’architecture (**`ABB`**)** et **de solution (**`SBB`**)** exposant les standards retenus E : EXIG-ARC-20 E : EXIG-ARC-21. L’AE les révise chaque trimestre avec le catalogue protocolaire (`CAD26 § 5.4`, p. 44 ; `Tableau 12`) E : EXIG-GOV-18. Outre passerelle et plans transversaux, s’imposent moteur durable sur écriture (`EXIG-ARC-05`), passerelle de modèles (`EXIG-ARC-08`) et bac à sable (`EXIG-ARC-10`). Un `SBB` partiel exige un `SBB` complémentaire ou une dérogation écrite (`≤ 6` mois, ou `≤ 90` j en classe faible), renouvelable une fois E : EXIG-GOV-16.

Correspondance `ABB → SBB` (exemples non limitatifs, état au 28 oct.–14 nov. 2026) :

| Couche / Plan (`CAD26` ↔ Pivot) | `ABB` (bloc neutre) | Capacités exigées | Exemples de `SBB` substituables (état au 28 oct.–14 nov. 2026) |
| --- | --- | --- | --- |
| **1. Canaux et déclencheurs** (`C1`) | Interface d’interaction/approbation ; déclencheurs | Authentifier, ouvrir la trace, montrer l’action exacte, zéro invite | Portails internes déclaratifs, `webhooks` et planificateurs |
| **2. Orchestration et état** (`C2`) | Moteur durable, routeur et magasin d’état | Persistance par transition, reprise, attente d’approbation, Saga | `Temporal`, `Restate`, `AWS Step Functions`, `LangGraph` (persistance externe), `Microsoft Agent Framework`, `Google ADK` |
| **3. Agents et exécution cognitive** (`C2/C5`) | Exécution d’agent ; passerelle modèles ; bac à sable | Boucle `MCP`/`A2A`/`OTel` ; routage, cache, quotas ; réseau fermé | `Strands Agents`, `OpenAI Agents SDK` (+ `SBB` `A2A`/`OTel`) ; `Agent Router`, `agentgateway`, `Kong AI Gateway` ; `Firecracker`, `gVisor`, `Kata Containers`, `WASI` |
| **4. Médiation et connectivité** (`C4`) | Passerelle `PEP`, catalogue privé, bus d’événements | Coupure `MCP`/`A2A`, empreintes `SHA-256`, `CloudEvents`/`AsyncAPI` | `agentgateway`, `IBM ContextForge`, `Azure API Management` (+ `A2A`), `MuleSoft Agent Fabric`, `Apache Kafka` |
| **5. Outils et données** (`C3/C4`) | Serveurs `MCP`, adaptateurs, index et graphes | Intention métier, filtrage `ACL` mandant, bi-temporalité | Adaptateurs `MCP`/`OpenAPI`, `Graphiti`, `Zep`, index hybrides cités |
| **6. Systèmes d’enregistrement** (`C4`) | Progiciels et cœurs métiers existants | Contrôles métier intacts, écriture corrélée et décimal exact | Aucun nouveau `SBB` central : adaptateurs validants uniquement |
| **Plan A — Identité et sécurité** | Identité `NHI`, autorisation, `PDP`, coffre, `CIBA` | Jetons `RFC 8693`, politiques hors modèle, secrets en aval | `SPIFFE` / `SPIRE`, `Microsoft Entra Agent ID`, `OPA`, `Cedar` ; coffre et approbation signée à l’homologation |
| **Plan B — Observabilité et FinOps** | Collecteur `OTel`, banc `E1–E3`, audit, quotas | Double couloir sans renseignements personnels (`RP`, ou `PII` dans les standards techniques), audit `JCS` ancré/h, `CPO` | `OpenTelemetry Collector` (caviardage) ; voûte d’audit et quotas désignés à l’homologation |
| **Plan C & SaaS encadrés** | Registre d’agents ; suites à agents intégrés | Cycle à 7 états, coupe-circuit ; contrôles `EXIG-ARC-21` | `ServiceNow AI Control Tower`, `Microsoft Agent 365` ; `Copilot Studio`, `Salesforce Agentforce` sous `PEP` |

En cas de tension (`CAD26 § 4.3`, `Tableau 10` p. 33, dont `84 % → 77 %` sous `CaMeL` en classe élevée), l’arbitrage suit un ordre strict : **droit applicable → 10 interdits** `EXIG-GOV-17` **→** `DOIT` **sur** `DEVRAIT` **→ principes de protection (**`PRIN-03..07, 10, 12`**) → principes d’architecture (**`PRIN-01, 02, 08, 09, 11`**)**. L’Annexe B croise `15 PRI`, `12 PRIN`, `10` décisions `CAD26` et `31 ADR` de `C27` (`8` **maintenues**, `7` **à réviser**, `16` **généralisées en** `12 DEC`).

La modélisation `ArchiMate` (`C26 ch. 44`, construit `[S]` sur *ArchiMate 4* `C260` du 27 avril 2026 compatible `3.2`) emploie `Specialization`, `<<…>>` et `Profiles` (`§ 44.1.1, § 44.1.9`). Elle impose quatre règles : agent actif distinct de son substrat ; humain imputable sans `Flow` direct entre proposeur et approbateur (`§ 44.1.7`) ; décomposition de la mémoire, du contexte et de l’objet sémantique (`§ 44.1.8`) ; zéro `Requirement` **réglementaire orphelin** (`C26 § 44.6`). Un modèle statique n’atteste jamais l’exécution d’instance (`§ 44.9`).

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. Adopter le pivot à 5 couches et 3 volets raccordé aux 6 vraies couches de `CAD26 § 5.2` et sanctuariser le noyau possédé (`42 CAP` invariantes) P : PRI-001 P : PRI-015 P : DEC-007 E : EXIG-ARC-19.
2. Gouverner par gravité des données : confiner tout agent SaaS à son silo sous `EXIG-ARC-21` et rapatrier toute orchestration inter-silos P : CAP-013 E : EXIG-ARC-21.
3. Appliquer `CAD26 § 4.3` (`EXIG-GOV-17` en tête), réviser trimestriellement `ABB → SBB` (`CAD26 § 5.4`) E : EXIG-ARC-20 E : EXIG-GOV-18 et proscrire tout `Requirement` réglementaire orphelin (`C26 § 44.6`).

Spécifications AS

1. Couvrir 100 % des capacités de chaque `ABB` requis par des `SBB` conformes aux standards (ou `SBB` complémentaire) et bannir toute logique ou invite en Couche 1 E : EXIG-ARC-03 E : EXIG-ARC-20 E : EXIG-ARC-21.
2. Isoler le *System of Action* des *Systems of Record* (`ADR-001`) : zéro `SQL` direct ; écriture via interfaces validant règles métier, idempotence et trace (`EXIG-ARC-18`, `DEVRAIT`) E : EXIG-ARC-14 E : EXIG-ARC-17 E : EXIG-ARC-18.
3. Propager mandant, trace et budget dans chaque appel descendant E : EXIG-ARC-02, et attacher l’étiquette immuable d’entité juridique à chaque actif et mémoire P : CAP-021 P : DEC-007 P : PEX-041 E : EXIG-CON-06.

## 2.5 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Plan de contrôle face aux suites métiers | Noyau possédé en propre (registre, identité, politiques, passerelles, traces) fédérant les silos P : PRI-015 | Tâche strictement mono-silo sans accès transversal, sous contrôles compensatoires E : EXIG-ARC-21 | `[É]` `C27` § 26.9, § 27.2–27.4 ; `CAD26` § 5.4, § 13.1 |
| Écriture dans un système d’enregistrement | Passage exclusif par interfaces applicatives ou adaptateurs validant règles métier et idempotence E : EXIG-ARC-17 | Jamais en écriture directe en base (`ADR-001` maintenue, intégrité des livres) | `[N]` `BSIF` B-13 / E-23 (`ANC-103`) ; `CAD26` `PRIN-05`, `EXIG-ARC-14` |
| Logique ou invite dans les canaux | Interdiction stricte : la Couche 1 authentifie le mandant, ouvre la trace et affiche l’action E : EXIG-ARC-03 | Jamais en production ; l’orchestration et les invites vivent en Couches 2 et 3 de `CAD26` | `[É]` `[S]` `CAD26` § 5.2 (p. 37) ; `PD28` `CAP-001` |
| `SBB` à couverture partielle | Adjonction obligatoire d’un bloc complémentaire couvrant les contrôles manquants avant homologation E : EXIG-ARC-20 | Dérogation écrite bornée (`≤ 6` mois, ou `≤ 90` j en classe faible) avec compensations E : EXIG-GOV-16 | `[É]` `CAD26` § 5.4 Tableau 12 (pp. 44–45) |
| Échange inter-organisations et enclaves | Interfaces modulaires réservées sans déploiement immédiat (`10` capacités conditionnelles `P1–P3`, dont `9` en `P2–P3`) | Franchissement avéré des signaux correspondants (`SIG-002, 007, 016, 103`) | `[S]` `PD28` M-11 § 11.3 (`42` inv. vs `10` cond.) |
| Arbitrage simplicité vs sûreté / vie privée | Primauté du droit, des 10 interdits E : EXIG-GOV-17 puis des principes de protection (`PRIN-03..07, 10, 12`) | Jamais contre la loi ni `EXIG-GOV-17` ; décision consignée en comité | `[N]` `Loi 25` ; `CAD26` § 4.3 Tableau 10 (p. 33) |

## 2.6 Limites et renvois

`TOGAF` et `ISO/IEC 42001` restent au `statut F` (aucun `[N]`). *ArchiMate 4* (`C260`) n’a été vérifiée en `C26 § 44.1.1, § 44.1.9` (`§ 44.0.4`) que sur extraits du 29 octobre 2026 ; ses stéréotypes et `PC1–PC5` (`C26 ch. 43`) demeurent `[S]`. Quatre coquilles internes de `CAD26` v1.1 sont rectifiées :

`EXIG-APP-18` p. 32, `EXIG-APP-12` au lieu d’`EXIG-APP-17` p. 233, `EXIG-MEM-01` au lieu d’`EXIG-ARC-22` pp. 258/342, et `EXIG-ARC-02` au lieu d’`EXIG-ARC-21` (pp. 195–257). L’interdiction des frais de transfert du *Data Act* européen au 12 janvier 2027 D (`ANC-003`) vise l’UE. Renvois : `CAD26 Sommaire, ch. 4, 5, 11–14, Ann. A, B, D, H` ; `C26 ch. 7, 41–44` ; `C27 § 0.1, 0.4, ch. 1, 20, 23, 26, 27, 43, Ann. F` ; `PD28 M-2, M-9 à M-13, Ann. E` ; Annexes A à F.
