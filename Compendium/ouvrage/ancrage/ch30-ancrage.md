# Journal d'ancrage atomique Wyvern G2 — Chapitre 30 (`ch30`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/10 - Partie X/Chapitre 30.md` (`4 186` mots de prose `verifie_manuscrit` / `4 471` mots `parser_plan`, plage `[3 901, 4 579]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch30-sources.md` (`[1]`–`[7]` en statut `L+`, `3` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b5-1`
- **Passe G2 initiale (supportés) :** 4
- **Rectifications appliquées lors de la passe G2 :** 25
- **Verdict final — supportés :** 29 / 29 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 30.md`

Toutes les formulations divergentes, sur-affirmées ou issues du corpus interne hors socle `L+` fermé relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 30.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/10%20-%20Partie%20X/Chapitre%2030.md), sans altérer les invariants ni la structure, en préservant l'ensemble des `owned_concepts` (`plateformes-saas-et-asymetrie-tiers`, `fabrique-agents-certification-reemission`, `passage-echelle-parc-agents`, `plateforme-iap-gitops-cognitif`, `anti-patrons-agentiques`, `modele-maturite-feuille-360j`), les renvois `[1]`–`[7]`, les trois figures (`SCH-30-01.svg`, `SCH-30-02.png`, `SCH-30-03.svg`), les trois tableaux et le calibrage (`4 186` mots `verifie_manuscrit` / `4 471` mots `parser_plan` dans `[3 901, 4 579]`) :

1. **Régime de dérogation `EXIG-ORC-29`, causes Gartner/Deloitte et collision `CA-03` (`L3`, `L5`, `L7`, `L53`, `L60`, `L92`) :** alignement sur l'intitulé exact d'`EXIG-ORC-29` dans le `Tome 2` (`Aucun anti-patron sans dérogation`, où tout écart exige une dérogation formelle en comité `ARB`) en remplaçant « rejet bloquant sans dérogation » par « rejet bloquant par défaut (sauf dérogation formelle documentée) » ; alignement des causes d'abandon de `40 %` des projets sur `SRC-011.txt` (`[7]`, coûts imprévus, complexité d'échelle et risques imprévus) et élimination de la collision 12-gramme avec le `Tome 7`.
2. **Veille `SaaS`, `a2a-tck` `[2]` et laboratoire `Borealis-Bench` (`L13–L27`, `Tableau 30.1`) :** qualification explicite des dix plateformes `SaaS`, de l'échelle non normative à quatre statuts et du quadrant d'automne `2026` (`statut F`) comme issus de la veille documentaire indexée au `Tome 3` (chapitre 26, documentations auto-déclarées d'éditeurs et presse spécialisée pour `ServiceNow`, hors corpus `L+` fermé) ; dissociation stricte entre le contenu vérifié de `SRC-086.txt` `[2]` (`CARD-SIGN-001` à `CARD-SIGN-004` marquées `NOT_AUTOMATABLE` et absence de vecteurs `a2a-jcs-v01`) et la revue du dépôt (`Tome 3 § 26.9`) ; qualification de `Borealis-Bench` (`9/9`, `100,0 %`) comme évaluation artificielle interne (`FEDS`, Campagne 3) en laboratoire et suppression de la collision 12-gramme sur `A2A`.
3. **Fabrique d'agents, `IAP`, `GitOps` cognitif et validation `JSON Schema` (`L33–L45`) :** qualification de la fabrique d'agents (`Tome 1 § 41`) et des quatre conditions de réfutation (`Tableau 41.3`) comme construction architecturale du traité sans étude empirique `L+` dédiée ; rattachement de `Backstage`/`Kratix`/`Crossplane`, `OpenGitOps v1.0.0`, `SLSA v1.2`, `Sigstore Cosign`, `Argo CD` et `Temporal Worker Versioning` à la pile de référence du `Tome 6` (`§ 13.1–13.4`) ; séparation exacte entre la validation du descripteur `server.json` contre `server.schema.json` et la validation structurelle des contrats JSON du harnais contre `JSON Schema Draft 2020-12` `[5]`.
4. **Taxonomie `MAST`, cinq exclusions, `OPA` et `ArchiMate` (`L60–L92`) :** alignement du volume `MAST` sur le registre SSOT `faits-empiriques.json` (`1 642` traces annotées, `41 %` à `86,7 %` d'échecs sur sept cadriciels, détenu par `ch13`) ; ajout des risques `OWASP ASI01`, `ASI06` et `ASI10` `[1]` en cohérence avec le `Tableau 30.2` ; remplacement d'`ADR-009` par `ADR-031` dans les fondements des cinq exclusions (`ADR-001`, `ADR-005`, `ADR-011`, `ADR-031`, `§ 43.2`, `§ 31.2.6`) ; rattachement de l'intervalle `5–12` façades au `Tome 3 § 5.11`, de l'algorithme *brownfield* au `Tome 3 § 43.10`, de la couverture `100,0 %` (`45/45` tests OPA et `21` validations de schémas sans violation stricte) à `[4]` et `aq/rapports-g0.json`, des neuf défauts `Tableau 44.2` au `Tome 1 § 44.8` (`ArchiMate 4` / `C260`), et de l'acception financière/télécom d'`ACP` au `Tome 1 § 35.8.2`.
5. **Modèle `AAGMM`, `750` simulations d'Acharya et `ISO/IEC 42001` (`L100–L128`, `Tableau 30.3`, `Figure 96`) :** qualification d'`AAGMM`, d'`Acharya` (`750` simulations, `-94,3 %`, `-96,4 %`, `+32,6 %`) et de la feuille de route `360` jours comme repris de la littérature secondaire et prescriptive indexée au `Tome 6 § 15.4` (hors corpus `L+` fermé), et signalement explicite du **`statut F`** d'`ISO/IEC 42001` (norme payante hors preuve `L+`) en prose et au `Tableau 30.3`.

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C30-01` à `C30-28`)

### Préambule et cadrage (`L1–L7`)

- **C30-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant l'usine logicielle interne (`IAP` et `GitOps` cognitif), l'asymétrie des plateformes `SaaS` tierces et le rejet bloquant par défaut devant le comité d'architecture.
  - **Appui vérifié :** `specs/manifest.json` (`ch30`, `D10`, `SUB_D10_03`), `Corpus/Tome 2` (`EXIG-ORC-29`, `L3288–3292`), `registre/matrice-exig-prr-c40.json` (`C33`, `C35`, `C36`, `EXIG-ORC-29`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé « rejet bloquant sans dérogation » par « rejet bloquant par défaut » en cohérence avec `EXIG-ORC-29` · **Verdict : supporté**

- **C30-02 (`L5`)** — *Affirmation :* La réplication sans usine ni barrière reconstitue une dette cognitive ; Deloitte (`SRC-011.txt` `[7]`) rapporte l'estimation de marché (`statut F` sur le communiqué primaire Gartner) selon laquelle plus de `40 %` des projets agentiques pourraient être abandonnés avant `2028` sous l'effet de coûts imprévus, de la complexité d'échelle ou de risques non anticipés.
  - **Appui vérifié :** `SRC-011.txt` (`L443`, `L719`), `recherche/registre-statut-f.json` (`L172–180`), `registre/faits-empiriques.json` (`FACT-GARTNER-ABANDON-2027`).
  - **Passe initiale :** écart rectifié · **Action :** aligné les trois causes d'abandon sur le libellé exact de `SRC-011.txt` (`L443`) et levé la collision 12-gramme `CA-03` avec le `Tome 7` · **Verdict : supporté**

- **C30-03 (`L7`)** — *Affirmation :* Structure en trois sections : asymétrie des dix plateformes `SaaS` relevées au traité, fabrique d'agents et `IAP`/`GitOps` cognitif (`C33`, `C35`, `C36`) ; verrou bloquant par défaut (`EXIG-ORC-29`, `AP-01` à `AP-12`, cinq exclusions, `Tableau 44.2`) ; feuille de route `360` jours (`AAGMM` `M1–M5`, `ARB 1–3`, *Strangler Fig* `RPA`).
  - **Appui vérifié :** `specs/manifest.json` (`ch30`), `registre/matrice-exig-prr-c40.json` (`C33`, `C35`, `C36`, `EXIG-ORC-29`), `Corpus/Tome 6` (`§ 13`, `§ 15`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté « relevées au traité » et qualifié le verrou d'architecture de « bloquant par défaut » · **Verdict : supporté**

### Section 30.1.1 — Asymétrie des dix plateformes SaaS tierces et quatre statuts (`L11–L27`, Tableau 30.1)

- **C30-04 (`L13`)** — *Affirmation :* Selon la veille documentaire indexée au `Tome 3` (chapitre 26, hors corpus `L+` fermé), dix grands éditeurs (`Microsoft` `Agent 365`/`Copilot Studio`, `Salesforce` `Agentforce`/`MuleSoft`, `ServiceNow` `AI Control Tower` connu uniquement par presse suite au refus d'accès de son portail, `SAP` `Joule`/`CIS`, `Workday`, `AWS` `AgentCore`, `Google` `Agent Registry`/`Agent Gateway`, `IBM` `watsonx Orchestrate`, `UiPath` `Maestro`, `Camunda`) annoncent leur ouverture à `MCP`/`A2A` sur le fil tout en maintenant fermé le plan de contrôle.
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 26.2–26.9`, `L13672`, `L13696–13853`, `L13935`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié ces constats de veille documentaire auto-déclarée indexée au `Tome 3` (`§ 26`) et signalé le recours aux sources de presse pour `ServiceNow` ; scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C30-05 (`L15`)** — *Affirmation :* Trois asymétries : révisions `A2A` divergentes (`0.3.0` telle `SAP` qui signale l'absence de garantie native de livraison ou d'unicité de traitement, ou préversions sans disponibilité générale vs `1.0`, et inscription manuelle des agents distants) ; rapports parfois réservés aux natifs et licences additionnelles (telle `Entra Agent ID`) ; rôle de collaborateur pour un agent externe.
  - **Appui vérifié :** `Corpus/Tome 3` (`L13700`, `L13723`, `L13753`, `L13763`, `L13787`, `L13799`, `L13848–13850`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché l'absence de garantie native à `SAP` (`Tome 3 L13753`) et reformulé le segment pour éliminer la collision 12-gramme `CA-03` · **Verdict : supporté**

- **C30-06 (`L17`)** — *Affirmation :* `a2a-tck` (`v1.0.0.alpha3`, `SRC-086.txt` `[2]`) marque `CARD-SIGN-001` à `CARD-SIGN-004` comme `NOT_AUTOMATABLE` et ne fournit pas `conformance-vectors/a2a-jcs-v01` (la revue du dépôt au `Tome 3 § 26.9` notant l'absence de liste publique certifiée) ; en évaluation artificielle interne (`FEDS`, Campagne 3 du `Tome 3` hors `L+`), `Borealis-Bench` (`LangGraph`, `AutoGen`, `CrewAI`) atteint `9/9` (`100,0 %`), montrant en laboratoire la faisabilité sous plan de contrôle possédé tandis que les suites commerciales fermées restent non testées.
  - **Appui vérifié :** `SRC-086.txt` (`L133–184`), `registre/specifications-lplus.json` (`SPEC-A2A-TCK-ALPHA3`, `L135–148`), `sources/ch30-sources.md` (`L20–29`), `Corpus/Tome 3` (`L13854–13870`, `L13941`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié les constats directs de `[2]` de la revue du dépôt et qualifié `Borealis-Bench` d'évaluation artificielle interne `FEDS` en laboratoire · **Verdict : supporté**

- **C30-07 (`L19`)** — *Affirmation :* La grille non normative à quatre statuts (`Tome 3 § 26.1` : `1` inventorié, `2` observé, `3` gouverné, `4` de plein droit) ne relève le statut `4` sur aucune documentation commerciale consultée jusqu'en novembre `2026` ; registre, politiques `OPA` (`[3]`) et comptabilité restent dans le noyau possédé, sans s'en remettre au quadrant d'automne `2026` inaccessible (`statut F`).
  - **Appui vérifié :** `Corpus/Tome 3` (`L13687–13694`, `L13815–13827`, `L13892`), `SRC-087.txt` (`[3]`), `sources/ch30-sources.md` (`L90`).
  - **Passe initiale :** écart rectifié · **Action :** précisé le caractère non normatif et daté (novembre `2026`) de la grille et de la lecture documentaire · **Verdict : supporté**

- **C30-08 (`L21–L27`, Tableau 30.1)** — *Affirmation :* Le `Tableau 30.1` synthétise, d'après la veille documentaire non testée du `Tome 3` (chapitre 26), l'ouverture déclarée, l'asymétrie et le statut maximal (`1–2` ou `1–3`, jamais `4`) des dix suites réparties en trois familles.
  - **Appui vérifié :** `Corpus/Tome 3` (`L13696–13845`, `Tableau 26.9`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté dans le tableau et sa légende l'origine documentaire non testée (`Tome 3 ch. 26`) et le canal presse pour `ServiceNow` · **Verdict : supporté**

### Section 30.1.2 — Fabrique d'agents, gabarits gouvernés et réémission (`L29–L35`)

- **C30-09 (`L31`)** — *Affirmation :* Distinction des quatre emplois du terme « fabrique » (`Tome 1 § 41.1`, `Tableau 41.1`) : fabrique d'agents (`F1`), fabrique d'identité (`F2`, ch. 16), titre de publication éditoriale (`F3`) et patron logiciel *factory* (`F4`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L9582–9591`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C30-10 (`L33`)** — *Affirmation :* Construction architecturale du traité (`Tome 1 § 41`, sans étude empirique primaire dans `L+`) à quatre mécanismes : gabarit gouverné, séparation catalogue interne / registre gouverné, barrière d'admission (`PC1–PC5`) confrontée au problème de l'oracle, et boucle de réémission vers le gabarit source.
  - **Appui vérifié :** `Corpus/Tome 1` (`L9576`, `L9607–9661`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié le mécanisme de construction architecturale du traité sans étude empirique `L+` et resserré le paragraphe (`CA-05`) · **Verdict : supporté**

- **C30-11 (`L35`)** — *Affirmation :* Risque de point de défaillance unique (`SPOF`, `§ 41.6`) et quatre conditions conceptuelles de réfutation (`Tableau 41.3`, non éprouvées empiriquement à la date de gel) : monoculture de gabarit, engorgement de certification, indisponibilité de l'équipe-fabrique et écart non mesuré d'admission.
  - **Appui vérifié :** `Corpus/Tome 1` (`L9662–9673`).
  - **Passe initiale :** écart rectifié · **Action :** précisé le statut conceptuel non éprouvé des quatre conditions (`Tableau 41.3`) et scindé la phrase (`CA-05`) · **Verdict : supporté**

### Section 30.1.3 — Plateforme IAP et GitOps cognitif (`L37–L54`, Figure 94)

- **C30-12 (`L39`)** — *Affirmation :* Passage à l'échelle simultané sur trois plans (applicatif, données, collaboration humain-agent) sous gouvernance fédérée *hub-and-spoke* animée par un `CoE` adossé à `LCIM` maîtrisant la contention GPU.
  - **Appui vérifié :** `Corpus/Tome 1` (`L262`), `Corpus/Tome 5` (`L204–220`), `Corpus/Tome 6` (`§ 13.1`, `L4001–4017`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C30-13 (`L41`)** — *Affirmation :* L'`IAP` (*Thinnest Viable Platform*) répond aux critères `C33`, `C35` et `C36` et expose des *Golden Paths* combinant, selon la pile du `Tome 6 § 13.1`, `Backstage`, `Kratix Promises` et `Crossplane`, avec pré-câblage `NHI`, `OpenTelemetry`, `AI`/`MCP Gateway` et `EvalOps`.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`C33`, `C35`, `C36`), `Corpus/Tome 6` (`L4005–4017`, `L5043–5046`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement la pile `Backstage`/`Kratix`/`Crossplane` au `Tome 6` (`section 13.1`) · **Verdict : supporté**

- **C30-14 (`L43`)** — *Affirmation :* Le `GitOps` cognitif (`Tome 6 § 13.3`, transposant `OpenGitOps v1.0.0`) co-versionne cinq artefacts : code `80/20`, invites/hyperparamètres, contrats `OASF`/`MCP`, politiques `OPA`/`Rego` `[3]` et bancs `EvalOps` ; les descripteurs `server.json` sont validés contre `server.schema.json` tandis que les contrats JSON du harnais sont vérifiés sous `JSON Schema Draft 2020-12` `[5]` (typage et champs stricts), et les éditions critiques `R3–R4` passent par demande d'intégration.
  - **Appui vérifié :** `SRC-021.txt` (`[5]`, `L2597–2606`, `L2785–2790`), `SRC-087.txt` (`[3]`), `Corpus/Tome 6` (`L4168–4190`, `Tableau 13.3`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié la validation de `server.json` (`server.schema.json`) de celle des contrats sous `JSON Schema Draft 2020-12` `[5]` et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C30-15 (`L45`)** — *Affirmation :* Selon la pile du `Tome 6` (`§ 13.3–13.4`), chaque version validée reçoit provenance `SLSA v1.2` et signature `Sigstore Cosign` vérifiées par `Argo CD`, avec livraisons progressives *Shadow*, *Canary* et *Blue-Green* appuyées sur `Temporal Worker Versioning` et soumission des dérogations aux mêmes contrats.
  - **Appui vérifié :** `Corpus/Tome 6` (`L4065`, `L4192`, `L4239–4258`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié ces composants comme pile de référence du `Tome 6` (`sections 13.3–13.4`) · **Verdict : supporté**

- **C30-16 (`L47–L49`, Figure 94)** — *Affirmation :* La Figure 94 (`SCH-30-01.svg`) articule les *Golden Paths* `IAP` (`Z1`), le `GitOps` cognitif sous `SLSA v1.2` et réémission `SPOF` (`Z2`), et l'encadrement des dix suites `SaaS` (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch30`, `SCH-30-01`), `schemas/SCH-30-01.puml`, `schemas/rendus/SCH-30-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C30-17 (`L51–L54`)** — *Affirmation :* Les trois invariants exécutables du Chapitre 30 fixent le maintien du noyau possédé + quintette `GitOps` (`C33`, `C35`, `C36`), le rejet bloquant `ARB` par défaut sauf dérogation formelle documentée (`EXIG-ORC-29`, `AP-01` à `AP-12`, `Tableau 44.2`) et le séquencement `AAGMM` à trois portes (`J90`, `J180`, `J360`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`C33`, `C35`, `C36`, `EXIG-ORC-29`), `Corpus/Tome 2` (`L3288–3292`), `Corpus/Tome 6` (`§ 13`, `§ 15`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé le deuxième invariant pour refléter la dérogation formelle documentée prévue par `EXIG-ORC-29` · **Verdict : supporté**

### Section 30.2.1 — Catalogue des anti-patrons, exclusions et OPA (`L56–L81`, Tableau 30.2)

- **C30-18 (`L60`)** — *Affirmation :* La taxonomie `MAST` (`1 642` traces annotées, analysées au `ch13` avec `41 %` à `86,7 %` d'échecs sur sept cadriciels) établit le poids des défauts de conception ; le recensement de Kraishan (`arXiv:2609.14119`, `SRC-057.txt` `[6]`) sur `21 643` serveurs `MCP` (`72 606` versions) mesure parmi `8 900` serveurs multi-versions `51,09 %` de mutations, `40,58 %` de dérive sémantique et `4,16 %` de redirections d'hôte (`OR = 2,96`) ; `EXIG-ORC-29` (« aucun anti-patron sans dérogation ») érige `10` anti-patrons d'orchestration (`Tableau 26`, Tome 2 : `AP-01`, `AP-06`–`AP-09`, `AP-12`) en motifs de rejet bloquant par défaut en comité `ARB`, complétés par le catalogue à `12` codes `AP-01` à `AP-12` (Tome 6 : `AP-02`–`AP-05`, `AP-10`, `AP-11`) face à `OWASP ASI01`–`ASI03`, `ASI06`, `ASI08`–`ASI10` (`SRC-055.txt` `[1]`).
  - **Appui vérifié :** `registre/faits-empiriques.json` (`FACT-MAST-FAILURES`, `FACT-MCP-DRIFT-4058`), `SRC-057.txt` (`L13`, `L553–558`, `L640`), `SRC-055.txt` (`L50–166`), `Corpus/Tome 2` (`L3271–3294`), `Corpus/Tome 6` (`L4808`).
  - **Passe initiale :** écart rectifié · **Action :** précisé `1 642` traces (`41 %` à `86,7 %` d'échecs), le régime de dérogation formelle `EXIG-ORC-29`, l'ensemble des risques `ASI` mobilisés, scindé la phrase (`CA-05`) et relié explicitement les `10` motifs `Tableau 26` aux `12` codes `AP-01`–`AP-12` (lissage G5) · **Verdict : supporté**

- **C30-19 (`L62`)** — *Affirmation :* Cinq exclusions architecturales fondées sur `ADR-001`, `ADR-005`, `ADR-011`, `ADR-031`, `§ 43.2` et `§ 31.2.6`, et remédiation à `Swagger-to-MCP 1:1` (`AP-04`, `50+` outils `CRUD`) par `5` à `12` façades d'intention (`Tome 3 § 5.11`) validées par `JSON Schema Draft 2020-12` (`additionalProperties: false`, champs `required` obligatoires, typage strict `[5]`).
  - **Appui vérifié :** `Corpus/Tome 3` (`L1083`, `L2243`, `L2486`, `L2761`, `L8988`, `L26026–26035`), `Corpus/Tome 1` (`L7244–7260`, `L9894–9916`), `SRC-021.txt` (`L2597–2606`, `L2785–2790`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé la référence erronée `ADR-009` par `ADR-031` et rattaché la plage `5–12` façades au `Tome 3` (`section 5.11`) · **Verdict : supporté**

- **C30-20 (`L64`)** — *Affirmation :* Rejet immédiat de `Prompt-as-Policy` (`AP-10`), déport des règles en `Rego` sous `OPA v1.22.4` (`default allow := false` `[3]`), couverture à `100,0 %` via `opa test --coverage --format=json` `[4]` éprouvée en `G0` sur trois paquets `policies_opa/*.rego` (`45/45` tests et `21` validations de schémas sans violation stricte), et triage *brownfield* (`Tome 3 § 43.10` : `DECOMMISSION`, `QUARANTINE_L1`, `REMEDIATE`, `PROMOTE`).
  - **Appui vérifié :** `SRC-087.txt` (`L13`, `L80–99`, `L3302`), `SRC-088.txt` (`L625–692`), `aq/rapports-g0.json` (`L26–37`), `Corpus/Tome 3` (`L22719–22724`).
  - **Passe initiale :** écart rectifié · **Action :** précisé la couverture des règles évaluées, le bilan exact `G0` (`3` paquets, `45/45` tests, `21` schémas), le rattachement du triage au `Tome 3 § 43.10` et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C30-21 (`L68–L83`, Tableau 30.2)** — *Affirmation :* Le `Tableau 30.2` cartographie les douze anti-patrons (`AP-01` à `AP-12`) entre `EXIG-ORC-29`, risques `OWASP ASI` `[1]`, `JSON Schema` `[5]`, `OPA`/`Rego` `[3, 4]` et remédiations obligatoires `ARB`.
  - **Appui vérifié :** `SRC-055.txt` (`[1]`), `SRC-087.txt` (`[3]`), `SRC-088.txt` (`[4]`), `SRC-021.txt` (`[5]`), `Corpus/Tome 6` (`Tableau 15.3`, `L4844–4859`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C30-29 (`L66`, § 30.2.1 — ajout post-G4)** — *Affirmation :* Protocole écrit d'exception face à `EXIG-ORC-29` (`Tome 2 § 11.6`, `EXIG-GOV-15..17` ; `Tome 6 § 13.1.3`) : dossier précisant risque résiduel, plan de retour à la conformité et contrôles compensatoires ; instruction `ARB` (avis sécurité, conformité, `RPRP`) et décision de comité pour au plus `6` mois renouvelable une fois avec alerte à `30` jours (ou délégation `≤ 90` jours en classe Faible hors instructeur), sans jamais déroger aux dix interdits `EXIG-GOV-17` ; sous `GitOps`/`OPA` (`default allow := false` `[3]`, `Argo CD`), bascule automatique vers suspension administrative à expiration ou retrait.
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 11.6`, `EXIG-GOV-15..17`), `Corpus/Tome 6` (`§ 13.1.3` `L4061`), `registre/matrice-exig-prr-c40.json` (`dix_interdictions_sans_derogation_gov_17`), `SRC-087.txt` `[3]`.
  - **Passe initiale :** ajout post-G4 · **Action :** vérification différentielle `G2` · **Verdict : supporté**

### Section 30.2.2 — Neuf défauts ArchiMate, homonymies et statut F (`L83–L96`, Figure 95)

- **C30-22 (`L85`)** — *Affirmation :* Neuf défauts de modélisation `ArchiMate 4` (`C260`, `Tableau 44.2` du `Tome 1 § 44.8`, hors corpus `L+` fermé) entraînant un blocage par défaut en comité `ARB` (quatre structurels, cinq disciplinaires).
  - **Appui vérifié :** `Corpus/Tome 1` (`L10062`, `L10267–10283`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché le `Tableau 44.2` au `Tome 1 § 44.8` (`ArchiMate 4` / `C260`) et précisé le blocage par défaut · **Verdict : supporté**

- **C30-23 (`L87–L90`)** — *Affirmation :* Levée de trois homonymies : `AgentMesh` (*Solace* vs *Solo.io* `agentgateway`), `Fabrique` (d'agents `§ 41` vs d'identité `§ 43.1` vs patron *factory*) et `ACP` (protocole fusionné dans `A2A` vs plan de contrôle d'un consortium financier/télécom dont un acteur canadien vs *Agentic Commerce Protocol*).
  - **Appui vérifié :** `Corpus/Tome 1` (`L1925–1936`, `L8428–8434`, `L8720`, `L9582–9590`), `Corpus/Tome 3` (`L27808`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la description du consortium `ACP` sur le `Tome 1 § 35.8.2` · **Verdict : supporté**

- **C30-24 (`L92–L96`, Figure 95)** — *Affirmation :* Consignation en `statut F` (`AO-01`) de `gartner.com`, `mckinsey.com` et `genai.owasp.org` (compensée par `[1]` et `[7]`) et formalisation dans `SCH-30-02.png` de l'entonnoir `ARB` à trois filtres de blocage par défaut (`10` motifs `EXIG-ORC-29` intégrés aux `12` codes `AP-01` à `AP-12` en `Z2`).
  - **Appui vérifié :** `sources/ch30-sources.md` (`L88–92`), `specs/manifest.json` (`ch30`, `SCH-30-02`), `schemas/SCH-30-02.mmd`, `schemas/rendus/SCH-30-02.png`.
  - **Passe initiale :** écart rectifié · **Action :** remplacé « barrages sans dérogation » par « filtres de blocage par défaut (sous réserve des dérogations formelles prévues par `EXIG-ORC-29`) », et harmonisé la légende `Figure 95` (lissage G5) · **Verdict : supporté**

### Section 30.3 — Modèle AAGMM et feuille de route à 360 jours (`L98–L128`, Tableau 30.3, Figure 96)

- **C30-25 (`L100–L102`)** — *Affirmation :* Modèle `AAGMM` (`M1` à `M5`), repris de la littérature secondaire du `Tome 6 § 15.4` (relié à `NIST AI RMF` et `ISO/IEC 42001` en `statut F` hors preuve `L+`) ; dans les `750` simulations d'Acharya citées au `Tome 6`, baisse simulée de `94,3 %` de l'étalement et `96,4 %` des incidents, hausse de `32,6 %` de l'achèvement (repère académique non versé au corpus `L+`), et règle du maillon le plus faible plafonnant vers la cible `M3`.
  - **Appui vérifié :** `Corpus/Tome 6` (`L4865–4876`), `recherche/registre-statut-f.json` (`L216–224`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié la source secondaire `Tome 6 § 15.4` hors `L+`, signalé le `statut F` d'`ISO/IEC 42001` et scindé le paragraphe (`CA-05`) · **Verdict : supporté**

- **C30-26 (`L104–L112`, Tableau 30.3)** — *Affirmation :* Le `Tableau 30.3` décline les cinq paliers `AAGMM` (`M1` à `M5`) sur cinq axes, en mobilisant `OPA` `[3]` et `EvalOps` CI `100,0 %` `[4]` en `M3` et en consignant `ISO/IEC 42001` en `statut F` en `M5`.
  - **Appui vérifié :** `Corpus/Tome 6` (`Tableau 15.4`, `L4877–4885`), `SRC-087.txt` (`[3]`), `SRC-088.txt` (`[4]`), `recherche/registre-statut-f.json` (`L216–224`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté la mention `statut F` en cellule `M5` et en légende du `Tableau 30.3` · **Verdict : supporté**

- **C30-27 (`L114–L126`, Figure 96)** — *Affirmation :* Feuille de route prescriptive (`Tome 6 § 15.4.2`) en trois horizons (`J0–J90` `ARB 1` `M1 → M2`, `J90–J180` `ARB 2` `M2 → M3` incluant la sortie *Strangler Fig* du `RPA` en quatre stades, `J180–J360` `ARB 3` `M3 → M4/M5`) illustrée par `SCH-30-03.svg` (mentionnant les `750` simulations d'Acharya).
  - **Appui vérifié :** `Corpus/Tome 6` (`L4795–4802`, `L4887–4927`), `specs/manifest.json` (`ch30`, `SCH-30-03`), `schemas/SCH-30-03.svg`.
  - **Passe initiale :** écart rectifié · **Action :** qualifié la feuille de route de prescriptive (`Tome 6 § 15.4.2`) et rattaché la légende de la `Figure 96` aux `750` simulations rapportées par Acharya · **Verdict : supporté**

- **C30-28 (`L128`)** — *Affirmation :* Clôture de la Partie X (`D10`) articulant les profils sectoriels, les trois blueprints de référence et l'usine `IAP` encadrée vers la Partie XI (`D11`, `DAPP`, `AE ↔ AS`, capital humain).
  - **Appui vérifié :** `specs/manifest.json` (`ch28`, `ch29`, `ch30`, `ch31–ch33`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé « validés mécaniquement » / « immunisée » par « de référence » / « encadrée » · **Verdict : supporté**
