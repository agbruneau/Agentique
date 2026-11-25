# Journal d'ancrage atomique Wyvern G2 — Chapitre 13 (`ch13`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/05 - Partie V/Chapitre 13.md` (`4 835` mots de prose, plage `[4 600, 5 400]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch13-sources.md` (`[1]`–`[9]` en statut `L+`, `3` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b2-8`
- **Passe G2 initiale (supportés)** : 15
- **Rectifications appliquées lors de la passe G2 :** 29
- **Verdict final — supportés :** 44 / 44 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 13.md`

Toutes les formulations divergentes ou issues de sources non archivées en `L+` relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 13.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/05%20-%20Partie%20V/Chapitre%2013.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant `FACT-MAST-FAILURES` (`41 %` à `86,7 %`, `1 642` traces), la vedette propriétaire `effet Ringelmann multi-agents`, les `owned_concepts`, l'ensemble des renvois `[1]`–`[9]` et le calibrage (`4 835` mots dans `[4 600, 5 400]`) :

1. **Facteurs de surcoût en jetons et seuils de saturation (`L7`, `L19`, `L21`, `L23`) :** remplacement de la fourchette générique `3×` à `15×` par les grandeurs exactement mesurées dans `[1]` (`1,6×` à `6,2×` le budget de l'agent unique, jusqu'à `515 %` de tours supplémentaires) et dans `[3]` (`10×` à `45×` en jetons d'invite par agent effectif en débat homogène), ajout de l'argument de l'inégalité de traitement des données (`[2]`), précision des `260` configurations contrôlées de `[1]`, de la nuance multivariée (`E_c` et `O_%`), de *MMLU-Hard* et du placebo de bruit sur mathématiques libres (`[3]`), ainsi que de la séparation entre le seuil `> 45 %` (`[1]`) et `p > 0,5` (`[3]`).
2. **Statut du test `C26 § 29.4.1`, du cadre `OO1–OO4`, de l'encapsulation hybride et d'`APM` (`L9`, `L25`, `L27`, `L31`, `L46`, `L48`) :** requalification de `C26 § 29.4.1` en *test de qualification* (`Tome 1 § 29.4.1`), explicitation de l'origine conceptuelle interne (`Tome 1 § 22.1–22.7`, `Tome 3 § 17.2–17.4`), séparation de `strict: true` (profil de harnais) vis-à-vis de `JSON Schema Draft 2020-12 Core` (`additionalProperties: false`, `required` `[9]`), ajout des gains mesurés `ReAct` `[7]` et `ReWOO` `[8]`, et retrait des mentions de versions ou taux non archivés en `L+` (`Camunda 8.11`/`fromAi`/`10` invocations, `UiPath Maestro`, `41,1 %` à `96,3 %`).
3. **Cadriciels d'orchestration et preuve `EXIG-ORC-02` / `EXIG-ORC-30` (`L11`, `L80`, `L82`) :** alignement d'`EXIG-ORC-02` sur le test de non-infériorité (`IC 95 %`) et d'`EXIG-ORC-29` sur la réserve de dérogation formelle ; retrait des séries de bogues et dates de disponibilité non archivées en `L+` (`409`, `5 669` billets, `24,7 %`, `3 avril 2026`, `14 mai 2025`, `19 mai 2026`) au profit de `[1, 2, 9]` et de la grille d'épreuve `EXIG-ORC-30` (`Tome 2 § 7.10`).
4. **Cible de conception `B2B` `ADR-026` (`L86`, `L88`, `L90`, `L134`) :** qualification explicite de la scission Diplomate/Évaluateur, du rapprochement tripartite et des valeurs numériques (`4` tours, `±0,5 %`, `0,02` dollar, `≤ 3` requêtes de cotation par minute, politiques `Cedar`) comme cibles et paramètres illustratifs du traité (`Tome 3 § 45.4–45.10`), avec rappel de la limite des enclaves `TEE` sur les sorties.
5. **Taxonomie `MAST v3`, remèdes et incidents (`L92`, `L94`, `Tableau 13.3`, `L108`–`L114`) :** correction de la part agrégée `FM-2` de `32,4 %` à `32,3 %` (exacte selon la Figure 1 de `SRC-028.txt`, la somme des parts arrondies valant `32,35 %`), mention des deux valeurs `FM-2.4` (`0,85 %` au texte / `0,80 %` en figure), retrait de la série `v2` absente du corpus `L+` dans le `Tableau 13.3`, retrait des statistiques non archivées en `L+` (`MAS-FIRE`, `MultiAgentBench`, chiffres `Who&When`) au profit des interventions mesurées dans `SRC-028.txt` (`+9,4 %`, `+15,6 %`, `60 %`–`68 %` vs `1,56×`, \(\kappa = 0{,}77\)), rattachement des `7` pannes frontalières à la grille analytique interne (`Tome 1, Tableau 11.4`), et réancrage de l'incident `Replit` directement sur `OWASP ASI05` (`SRC-055.txt`) et `ASI08` (`[5, 6]`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C13-01` à `C13-44`)

### Section 13.1 — Titre, question directrice et résumé (`L1–L11`)

- **C13-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant l'arbitrage entre code déterministe, agent unique outillé et collectif multi-agents via l'échelle `OO1–OO4`, un catalogue fermé de topologies portables et les parades aux `14` modes `MAST` et à l'effet Ringelmann.
  - **Appui vérifié :** `specs/manifest.json` (`ch13`, `D05`, `SUB_D05_01`), `SRC-028.txt` (`[4]`), `SRC-032.txt` (`[3]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-02 (`L7`)** — *Affirmation :* L'ajout de participants dégrade souvent l'efficacité sur les tâches séquentielles couplées, alourdit les budgets de jetons de `1,6×` à `6,2×` par rapport à un agent unique `[1]` et de `10×` à `45×` en jetons d'invite par agent effectif en débat homogène `[3]`, tandis qu'à budget de réflexion égal un agent unique bien outillé surpasse ou égale le multi-agents en raisonnement multi-sauts `[2]`.
  - **Appui vérifié :** `SRC-003.txt` (`L18–19`, `L946–947` : `1.6–6.2×`), `SRC-032.txt` (`L628` : `10–45×`), `SRC-031.txt` (`L21–22`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé `3×` à `15×` par les facteurs exacts vérifiés dans `[1, 3]` et précisé l'apport de `[2]` · **Verdict : supporté**

- **C13-03 (`L9`)** — *Affirmation :* L'arbre `OO1–OO4` (`EXIG-ORC-01`, `EXIG-ORC-02`, `ADR-002`, `CAP-007`, `PRI-002`, `PRR O-06`) bascule impérativement vers `OO3`/`OO4` lorsque les trois conditions cumulatives du test de qualification `C26 § 29.4.1` (`Tome 1 § 29.4.1`) sont réunies, en confinant le non-déterminisme dans `BPMN 2.0`, `CMMN`, la planification structurée ou les *frames* `APM` (*Agentic Business Process Management*).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`ORC`, `CAP-007`, `ADR-002`, `PRI-002`, `O-06`), `Corpus/Tome 1` (`L5149–5340`, `L6759–6771`), `Corpus/Tome 2` (`L2759–2773`).
  - **Passe initiale :** écart rectifié · **Action :** requalifié `C26 § 29.4.1` en test de qualification, développé `APM` et retiré la référence produit implicite de `Routine` · **Verdict : supporté**

- **C13-04 (`L11`)** — *Affirmation :* Sous preuve de non-infériorité (`pass^k`, `IC 95 %`, couverture `CPO`), les topologies se verrouillent sur les huit patrons `ADR-011` (`EXIG-ORC-03..10`), proscrivent sauf dérogation les dix anti-patrons (`EXIG-ORC-29`) et les salles quadratiques \(O(n^2)\), assurent la portabilité `MCP`/`A2A` (`EXIG-ORC-30`), et neutralisent les `14` modes `MAST v3` `[4]` et la grille interne des `7` pannes frontalières via `EXIG-ORC-23..25` et `ADR-026`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L2767–2902`, `L3213–3322`), `SRC-028.txt` (`[4]`), `Corpus/Tome 1` (`Tableau 11.4`, `L3092–3104`), `Corpus/Tome 3` (`L23436–23910`).
  - **Passe initiale :** écart rectifié · **Action :** précisé la non-infériorité (`EXIG-ORC-02`), la dérogation formelle (`EXIG-ORC-29`), retiré le statut GA groupé de cinq produits et rattaché les `7` pannes à la grille interne · **Verdict : supporté**

### Section 13.2.1 — Arbre `OO1–OO4`, encapsulation hybride et paradigme `APM` (`L17–L52`, Tableau 13.1, Figure 1)

- **C13-05 (`L17`)** — *Affirmation :* L'arbre `OO1–OO4` ordonne le choix selon la détention explicite du processus et le commandement de la transition (`N0`/`OO1` déterministe jusqu'à `OO4`), et `EXIG-ORC-01` exige une justification écrite préalable de l'insuffisance des paliers inférieurs.
  - **Appui vérifié :** `Corpus/Tome 1` (`L5171–5203`), `Corpus/Tome 2` (`L2759–2765`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-06 (`L19`)** — *Affirmation :* Kim et coll. `[1]` montrent sur `260` configurations contrôlées (6 bancs, 5 architectures, 3 familles) des gains jusqu'à `+80,8 %` en raisonnement financier décomposable contre une chute jusqu'à `−70,0 %` en planification séquentielle.
  - **Appui vérifié :** `SRC-003.txt` (`L10–12`, `L18–19`, `L668–676`).
  - **Passe initiale :** écart rectifié · **Action :** précisé `260` configurations et aligné les deux domaines expérimentaux sur *Finance Agent* et *PlanCraft* · **Verdict : supporté**

- **C13-07 (`L19`)** — *Affirmation :* Les architectures indépendantes amplifient les erreurs sur traces de `17,2×` contre `4,4×` sous coordination centralisée, bien que la régression multivariée attribue principalement les écarts à l'efficacité de coordination et au surcoût en jetons (`1,6×` à `6,2×`, jusqu'à `515 %` en hybride) `[1]`.
  - **Appui vérifié :** `SRC-003.txt` (`L154–157`, `L920–952`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté la nuance de la régression multivariée et les valeurs exactes de surcoût de `SRC-003.txt` · **Verdict : supporté**

- **C13-08 (`L21`)** — *Affirmation :* Tran et Kiela `[2]` démontrent, par l'inégalité de traitement des données et des essais à budget de jetons de réflexion égal, qu'un agent unique égale ou surpasse le multi-agents sur le raisonnement multi-sauts tant que le contexte unifié ne se dégrade pas.
  - **Appui vérifié :** `SRC-031.txt` (`L12–22`, `L144–224`).
  - **Passe initiale :** écart rectifié · **Action :** précisé l'inégalité de traitement des données et la condition de dégradation du contexte · **Verdict : supporté**

- **C13-09 (`L21`)** — *Affirmation :* Bertalanič et Fortuna `[3]` établissent l'**effet Ringelmann multi-agents** sur `44` cellules ajustées par \(R(N) = 1 / (1 + c(N - 1)N^{-\beta})\) (\(R^2 > 0{,}99\)) avec plafond dur \(1/c\) ; trente agents homogènes en débat n'apportent pas plus de diversité de réponses qu'un agent unique sur *MMLU-Hard*, et un placebo de bruit égale l'auto-correction sur mathématiques libres.
  - **Appui vérifié :** `SRC-032.txt` (`L8–24`, `L593–605`) et `registre/glossaire-termes.json` (`L335–341`, vedette propriétaire `effet Ringelmann multi-agents`).
  - **Passe initiale :** écart rectifié · **Action :** précisé *MMLU-Hard* et le résultat du placebo de bruit sur les mathématiques libres · **Verdict : supporté**

- **C13-10 (`L23`)** — *Affirmation :* En cohérence avec la loi de Lusser (`ch02`), `EXIG-ORC-02` (`PRR O-06`) impose une preuve hermétique (`IC 95 %` de non-infériorité en `pass^k`) couvrant le surcoût (`1,6×`–`6,2×` `[1]`, `10×`–`45×` `[3]`) sans heurter les seuils de saturation (`> 45 %` `[1]`, `p > 0,5` `[3]`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L2767–2773`), `SRC-003.txt` (`L152`, `L947`), `SRC-032.txt` (`L626–632`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé `3×` à `15×` et dissocié les seuils de `[1]` et `[3]` · **Verdict : supporté**

- **C13-11 (`L25`)** — *Affirmation :* `ReAct` `[7]` (`+34 %` *ALFWorld*, `+10 %` *WebShop*) entrelace raisonnement et action au prix d'une croissance du contexte, tandis que `ReWOO` `[8]` (*Planner*, *Worker*, *Solver*, jusqu'à `5×` d'efficacité en jetons et `+4 %` sur *HotpotQA*) découple planification et exécution, avec validation `JSON Schema Draft 2020-12 Core` (`additionalProperties: false`, `required`, types explicites `[9]`) et mode strict du harnais.
  - **Appui vérifié :** `SRC-115.txt` (`L26–29`, `L281`), `SRC-118.txt` (`L28–29`, `L104–112`), `SRC-021.txt` (`L2292–2304`, `L2605–2606`).
  - **Passe initiale :** écart rectifié · **Action :** intégré les mesures exactes `[7, 8]` et dissocié `strict: true` de `SRC-021.txt` `[9]` · **Verdict : supporté**

- **C13-12 (`L27`)** — *Affirmation :* L'arbitrage `OO1–OO4` (`Tome 1 § 22.1–22.4`) mobilise quatre propriétés instrumentables (complexité cyclomatique/`ABC`, précision/rappel/`F1`, taux de faux négatifs/vitesse, exactitude du journal) et une propriété non métrique (autonomie), en déconseillant la journalisation confiée aux agents.
  - **Appui vérifié :** `Corpus/Tome 1` (`L5208–5252`).
  - **Passe initiale :** écart rectifié · **Action :** explicité le rattachement au cadre conceptuel du `Tome 1 (§ 22.1–22.4)` · **Verdict : supporté**

- **C13-13 (`L29`)** — *Affirmation :* Sept critères qualitatifs de sélection distinguent la supervision humaine (point d'observation) de l'action humaine (point d'arrêt) ainsi que l'effort initial de modélisation et la maintenance (`Tome 1 § 22.3`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L5220–5234`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-14 (`L31`)** — *Affirmation :* La discontinuité `OO2 → OO3` (lecture architecturale du traité, `Tome 1 § 22.1`) sépare la consigne non contraignante de la commande déterministe ; dès que les trois conditions cumulatives du test `C26 § 29.4.1` (`Tome 1 § 29.4.1`) sont réunies, `OO1` et `OO2` cèdent devant `OO3`/`OO4`.
  - **Appui vérifié :** `Corpus/Tome 1` (`L5191–5194`, `L6759–6771`).
  - **Passe initiale :** écart rectifié · **Action :** explicité le statut de lecture architecturale et de test de qualification · **Verdict : supporté**

- **C13-15 (`L33–L40`, Tableau 13.1)** — *Affirmation :* Le `Tableau 13.1` résume les quatre options `OO1–OO4`, détenteur du modèle, autorité d'enchaînement, lisibilité préalable et régime admissible.
  - **Appui vérifié :** `Corpus/Tome 1` (`Tableau 22.1`, `L5197–5202`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-16 (`L42–L44`, Figure 1)** — *Affirmation :* La Figure 1 (`SCH-13-01.svg`) illustre l'arbre `OO1–OO4`, la bascule `OO2 → OO3` et les capsules `BPMN`, `CMMN`, `Routine` et `APM`.
  - **Appui vérifié :** `specs/manifest.json` (`ch13`, `SCH-13-01`), `schemas/SCH-13-01.svg`, `schemas/rendus/SCH-13-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-17 (`L46`)** — *Affirmation :* Quatre patrons d'encapsulation hybride retenus dans l'ingénierie des processus du traité (`Tome 3 § 17.2–17.4`) confinent le raisonnement stochastique : sous-processus ad hoc `BPMN 2.0` borné, activité typée `JSON Schema Draft 2020-12` `[9]`, `CMMN`/`DMN`, et planification structurée avec contrôles aval et exposition en outil `MCP`.
  - **Appui vérifié :** `Corpus/Tome 3` (`L9085–9230`), `SRC-021.txt` (`[9]`).
  - **Passe initiale :** écart rectifié · **Action :** retiré les références et chiffres non archivés en `L+` (`Camunda 8.11`/`fromAi`/`10` invocations, `UiPath Maestro`, `41,1 %` à `96,3 %`) et réancré sur les quatre mécanismes structurels · **Verdict : supporté**

- **C13-18 (`L48–L50`)** — *Affirmation :* Le paradigme `APM` (*Agentic Business Process Management*, `Tome 1 § 22.6–22.7`) distingue automatisation (séquence figée) et autonomie (décision déléguée dans des *frames*), ainsi que *frames* normatifs et opérationnels (exigeant une correspondance bijective en architecture).
  - **Appui vérifié :** `Corpus/Tome 1` (`L5298–5325`).
  - **Passe initiale :** écart rectifié · **Action :** explicité l'origine `Tome 1 § 22.6–22.7` et le nom complet `APM` · **Verdict : supporté**

- **C13-19 (`L52`)** — *Affirmation :* Le modèle `APM` distingue trois scénarios d'encadrement (decideur unique sur processus, plusieurs décideurs par agent isolé, plusieurs décideurs sur cadre commun), quatre capacités (dont l'actionnabilité conversationnelle sans critère exécutable normalisé) et la séparation entre adaptation éphémère et évolution persistante.
  - **Appui vérifié :** `Corpus/Tome 1` (`L5326–5355`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 13.2.2 — Catalogue fermé, portabilité, scission `B2B` et taxonomie `MAST` (`L56–L114`, Tableaux 13.2–13.3, Figures 2–3)

- **C13-20 (`L56`)** — *Affirmation :* `ADR-011`, `CAP-010` et `EXIG-ORC-03` imposent un catalogue fermé de huit patrons autorisés et une variante débat (`EXIG-ORC-04..10`), incluant flux déterministe (`PRIN-08`), chaîne séquentielle, transfert, parallélisation à écrivain unique (`EXIG-ORC-07`) et chorégraphie (`EXIG-ORC-08`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L2826–2901`), `registre/matrice-exig-prr-c40.json` (`CAP-010`, `ADR-011`, `PRIN-08`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-21 (`L58`)** — *Affirmation :* Le patron orchestrateur-exécutants est plafonné à `2` niveaux / `2` sauts (`EXIG-ORC-04`, `RFC 8693`), l'évaluateur-optimiseur exécute d'abord les contrôles déterministes avant un critique distinct et escalade à `≤ 3` itérations (`EXIG-ORC-05`), l'agent unique consolide au-delà de `15` outils (`EXIG-ORC-09`) et la scission suit les frontières de contexte et sécurité (`EXIG-ORC-10`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L2864–2878`, `L2970–2984`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-22 (`L60`)** — *Affirmation :* La variante débat réunit `≤ 3` participants sous un gestionnaire (`EXIG-ORC-06`), `EXIG-ORC-29` proscrit dix anti-patrons (Tableau 26 du `Tome 2`), et trois verrous complètent le dispositif (`Claim-Check`, `Goal Pinning`, gestion de l'opacité `A2A`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L2880–2887`, `L3273–3295`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-23 (`L62–L74`, Tableau 13.2)** — *Affirmation :* Le `Tableau 13.2` consolide les huit topologies homologuées et la variante débat d'`ADR-011` avec leurs bornes maximales (`xagentmaxhops = 4`, `≤ 2` sauts, `≤ 3` itérations, `≤ 15` outils, `≤ 3` participants).
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 24`, `L2446`, `L7229`, `L2826–2838`), `Chapitre 14.md` (`L34`, `L103`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-24 (`L76–L78`, Figure 2)** — *Affirmation :* La Figure 2 (`SCH-13-02.svg`) oppose les dix anti-patrons d'`EXIG-ORC-29` au catalogue fermé d'`ADR-011` et à l'isolation des cadriciels aux frontières `MCP`/`A2A`.
  - **Appui vérifié :** `specs/manifest.json` (`ch13`, `SCH-13-02`), `schemas/SCH-13-02.svg`, `schemas/rendus/SCH-13-02.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-25 (`L80`)** — *Affirmation :* La portabilité s'établit aux frontières `MCP` et `A2A` en raison de la pénalité de surcharge sur les workflows outillés (`β = −0,096`) `[1]`, de la fragmentation informationnelle des dialogues multi-agents `[2]` et du besoin de contrats stricts `[9]`.
  - **Appui vérifié :** `SRC-003.txt` (`L149–150`), `SRC-031.txt` (`L12–22`), `SRC-021.txt` (`[9]`).
  - **Passe initiale :** écart rectifié · **Action :** retiré les comptages de billets non archivés en `L+` (`409`, `5 669`, `24,7 %`) et réancré sur `[1, 2, 9]` · **Verdict : supporté**

- **C13-26 (`L82`)** — *Affirmation :* L'exigence `EXIG-ORC-30` (`Tome 2 § 7.10`) soumet toute pile d'orchestration (exemples d'écosystème indexés au `Tome 2 § 7.10` : `LangGraph`, `Microsoft Agent Framework`, `Temporal`, `CrewAI`, `Google ADK`, `DSPy`, `Confluent`) à une preuve de concept couvrant neuf capacités techniques vérifiables.
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 27`, `L3300–3322`).
  - **Passe initiale :** écart rectifié · **Action :** retiré les dates et statuts commerciaux non vérifiés dans `corpus_l_plus/` et recentré sur l'épreuve `EXIG-ORC-30` · **Verdict : supporté**

- **C13-27 (`L84`)** — *Affirmation :* `EXIG-ORC-23..25` imposent une enveloppe `JSON Schema Draft 2020-12` `[9]` sans historique brut ni jetons dans la charge utile, avec références `URI` hors bande, `traceparent` `W3C`, budget résiduel, palier/classe les plus contraignants, validation du retour (`EXIG-ORC-24`) et filtrage selon les droits du mandant (`EXIG-ORC-25`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L3213–3235`), `SRC-021.txt` (`[9]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-28 (`L86`)** — *Affirmation :* Aux frontières `B2B`, la cible de conception `ADR-026` (`CAP-014`, `Tome 3 § 45.4, § 45.9`) scinde l'agent **Diplomate** en `DMZ` `A2A`/`EDC` (plafonné à titre illustratif à `4` tours) de l'**Évaluateur** interne détenteur des seuils financiers.
  - **Appui vérifié :** `Corpus/Tome 3` (`L23436–23453`, `L23688–23698`), `registre/matrice-exig-prr-c40.json` (`ADR-026`, `CAP-014`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement la scission comme cible de conception et `4` tours comme plafond illustratif · **Verdict : supporté**

- **C13-29 (`L88`)** — *Affirmation :* Un analyseur syntaxique strict `[9]` et des politiques hors modèle (telles que `Cedar` en exemple `B2B`) bloquent l'accès du Diplomate aux secrets internes ; les calculs conjoints sur secrets mutuels s'exécutent en enclave `TEE` attestée à distance (`Intel TDX`, `AMD SEV-SNP`) à sortie agrégée ou booléenne, complétés par des sessions bilatérales en étoile anti-collusion (`Tome 3 § 45.5–45.9`).
  - **Appui vérifié :** `Corpus/Tome 3` (`L23454–23496`, `L23699–23730`, `L23787–23791`), `SRC-021.txt` (`[9]`).
  - **Passe initiale :** écart rectifié · **Action :** présenté `Cedar` comme exemple du profil et souligné la limite de l'enclave sur le format de sortie · **Verdict : supporté**

- **C13-30 (`L90`)** — *Affirmation :* Avant règlement `AP2`/`x402`, un arbitre déterministe exécute la cible de rapprochement tripartite (`Tome 3 § 45.7, § 45.10`) avec tolérances illustratives (`±0,5 %`, `0,02` dollar) et pare-feu asymétrique indicatif (`≤ 3` requêtes de cotation par minute).
  - **Appui vérifié :** `Corpus/Tome 3` (`L23498–23528`, `L23709`, `L23796–23861`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié le rapprochement de cible de conception et les seuils numériques de paramètres illustratifs/indicatifs · **Verdict : supporté**

- **C13-31 (`L92`)** — *Affirmation :* La taxonomie `MAST v3` (`[4]`, `SRC-028.txt`) analyse `1 642` traces de `7` cadriciels (`MetaGPT`, `ChatDev`, `HyperAgent`, `AppWorld`, `AG2`, `Magentic-One`, `OpenManus`), rapporte \(\kappa = 0{,}88\) de Cohen et `41 %` à `86,7 %` d'échecs, et répartit `14` modes en `44,2 %` (`FM-1`), `32,3 %` (`FM-2`, ou `32,35 %` par somme des parts arrondies) et `23,5 %` (`FM-3`).
  - **Appui vérifié :** `SRC-028.txt` (`L29`, `L93–95`, `L106–115`, `L127`, `L144–241`, `L524–573`) et `registre/faits-empiriques.json` (`FACT-MAST-FAILURES`).
  - **Passe initiale :** écart rectifié · **Action :** rectifié `32,4 %` en `32,3 %` conformément à la Figure 1 de `SRC-028.txt` (en mentionnant `32,35 %` sur somme des modes arrondis) · **Verdict : supporté**

- **C13-32 (`L94`)** — *Affirmation :* Quatre modes dominent (`FM-1.3` `15,7 %`, `FM-2.6` `13,2 %`, `FM-1.5` `12,4 %`, `FM-1.1` `11,8 %`), tandis que `FM-2.4` (`0,85 %` au texte de section, `0,80 %` en figure), `FM-1.2` (`1,5 %`) et `FM-2.5` (`1,9 %`) restent marginaux `[4]`.
  - **Appui vérifié :** `SRC-028.txt` (`L80–92`, `L529–551`).
  - **Passe initiale :** écart rectifié · **Action :** explicité les deux valeurs relevées dans `SRC-028.txt` pour `FM-2.4` (`0,85 %` en texte `L550` et `0,80 %` en figure `L90`) · **Verdict : supporté**

- **C13-33 (`L96–L102`, Tableau 13.3)** — *Affirmation :* Le `Tableau 13.3` ventile les trois catégories `MAST v3` (`44,2 %`, `32,3 %`, `23,5 %`) et leurs parades architecturales exigées.
  - **Appui vérifié :** `SRC-028.txt` (`L93–95`, `L524–573`), `Corpus/Tome 2` (`EXIG-ORC-05`, `EXIG-ORC-23`).
  - **Passe initiale :** écart rectifié · **Action :** retiré les parts `v2` absentes du corpus `L+` et aligné `FM-2` sur `32,3 %` · **Verdict : supporté**

- **C13-34 (`L104–L106`, Figure 3)** — *Affirmation :* La Figure 3 (`SCH-13-03.svg`) cartographie les `14` modes `MAST v3` et `7` pannes frontalières face à l'enveloppe `EXIG-ORC-23..25` et à la scission `DMZ`/`TEE`.
  - **Appui vérifié :** `specs/manifest.json` (`ch13`, `SCH-13-03`), `schemas/SCH-13-03.svg`, `schemas/rendus/SCH-13-03.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-35 (`L108`)** — *Affirmation :* Quatre familles de remèdes structurels complètent `MAST` `[4]`, et les interventions de Cemri et coll. montrent sur `ChatDev` (`GPT-4o`) un gain de `+9,4 %` par clarification des rôles et de `+15,6 %` par vérification de haut niveau sur *ProgramDev*, tandis que `MetaGPT` réduit de `60 %` à `68 %` les échecs `FM-1`/`FM-2` mais subit `1,56×` plus d'échecs `FM-3` `[4]`.
  - **Appui vérifié :** `SRC-028.txt` (`L137–141`, `L542–543`, `L586–587`, `L659–662`).
  - **Passe initiale :** écart rectifié · **Action :** retiré les résultats non archivés en `L+` de `MAS-FIRE` (`> 40 %`) et réancré sur les mesures directes de `SRC-028.txt` · **Verdict : supporté**

- **C13-36 (`L110`)** — *Affirmation :* L'annotateur automatique de `MAST` atteint \(\kappa = 0{,}77\) face aux experts `[4]`, et la difficulté d'attribution *a posteriori* (relevée avec `Who&When` dans `[4]`) justifie la prévention contractuelle préalable (`[9]`, `EXIG-ORC-23..26`).
  - **Appui vérifié :** `SRC-028.txt` (`L298–300`, `L464`).
  - **Passe initiale :** écart rectifié · **Action :** retiré les métriques non archivées en `L+` (`127` systèmes, `53,5 %`, `14,2 %`, `93`–`130` étapes, `84` h, `184` cas, `15 %`–`30 %`, `MultiAgentBench`) et réancré sur `SRC-028.txt` · **Verdict : supporté**

- **C13-37 (`L112`)** — *Affirmation :* La grille analytique interne du traité (`Tome 1, Tableau 11.4`) prolonge `MAST` `[4]` par sept défaillances frontalières (routage erroné, perte de contexte, incompatibilité de schéma, impasse sans médiateur, défaut de clarification `FM-2.2` `6,8 %` malgré `MCP`/`A2A`, dérive cumulative d'objectif, interblocage circulaire).
  - **Appui vérifié :** `Corpus/Tome 1` (`L3092–3104`), `SRC-028.txt` (`L549`, `L558–562`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement la grille de construction analytique interne prolongeant `[4]` · **Verdict : supporté**

- **C13-38 (`L114`)** — *Affirmation :* La non-compositionnalité aux frontières (`OWASP ASI08` `[5, 6]`), illustrée par l'exécution autonome destructive sur `Replit` supprimant ou écrasant des données de production documentée dans `OWASP ASI05` `[5]`, exige `EXIG-ORC-23..25`, arbitres externes et coupe-circuits sous `10` secondes (`ch21`).
  - **Appui vérifié :** `SRC-055.txt` (`L797–799`, `L1072–1160`), `SRC-059.txt` (`L33–35`), `Corpus/Tome 1` (`L3124`).
  - **Passe initiale :** écart rectifié · **Action :** réancré l'incident `Replit` directement sur `SRC-055.txt` (`L797–799`) plutôt que sur le seul identifiant externe `#1152` · **Verdict : supporté**

### Section 13.3 — Schémas, livrables, exigences probatoires et trois invariants exécutables (`L118–L134`)

- **C13-39 (`L118`)** — *Affirmation :* Les figures `SCH-13-01`, `SCH-13-02` et `SCH-13-03` matérialisent la chaîne de décision complète aux sections `13.2.1` et `13.2.2`.
  - **Appui vérifié :** `specs/manifest.json` (`ch13`), `Chapitre 13.md` (`L42`, `L76`, `L104`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-40 (`L120–L124`)** — *Affirmation :* Quatre livrables vérifiables conditionnent l'exploitation : dossier `OO1–OO4` `AE`/`AS` (`EXIG-ORC-01..02`, `PRR O-06`), graphe conforme `ADR-011`, schéma `JSON Schema Draft 2020-12` (`additionalProperties: false`, `required`, profil strict `[9]`) pour `EXIG-ORC-23..25` + `Claim-Check`, et rapport d'injection de fautes (`14` modes `MAST v3` `[4]`, `7` pannes frontalières).
  - **Appui vérifié :** `SRC-021.txt` (`[9]`), `SRC-028.txt` (`[4]`), `registre/matrice-exig-prr-c40.json` (`ADR-011`, `O-06`, `EXIG-ORC-01..25`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la formulation `EXIG-ORC-02` (non-infériorité `IC 95 %`), `JSON Schema 2020-12` (`[9]`) et le renvoi `[4]` · **Verdict : supporté**

- **C13-41 (`L126`)** — *Affirmation :* Le chapitre s'interface en amont (`ch02`, `ch04`, `ch08`, `ch14`, `ch15`, `ch19`, `ch21`, `ch30`) et en aval (`ch01`, `ch04`, `ch05`, `ch09`, `ch14`, `ch24`, `ch27`, `ch32`) dans le respect de la partition `CA-21`.
  - **Appui vérifié :** `specs/manifest.json` (`owned_concepts` et découpage `ch01`–`ch36`), `verifie_manuscrit.py` (`CA-21`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-42 (`L128`)** — *Affirmation :* Le socle probatoire s'arrête au `2 décembre 2026` sous `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`[1]`–`[9]` de `ch13-sources.md` et validation `G0` de `rapports-g0.json`, clause `non-avis`) avec exclusion en `statut F` de `genai.owasp.org`, `gartner.com` et `hbs.edu` (`HTTP 403`), compensée pour `OWASP` par `[5, 6]`.
  - **Appui vérifié :** `sources/ch13-sources.md` (`L1–114`), `recherche/registre-statut-f.json` (`L40–49`, `L171–203`), `aq/rapports-g0.json` (`L11–30`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C13-43 (`L130–L133`)** — *Affirmation :* Invariants exécutables 1 et 2 : échec en revue `PRR O-06` sans preuve comparative (`IC 95 %`, `pass^k`, `CPO`) contre agent unique (`≤ 15` outils) et bascule vers `OO3`/`OO4` sous le test `C26 § 29.4.1` ; catalogue fermé `ADR-011` (`≤ 2` sauts, `≤ 3` itérations, `≤ 3` participants) et isolation des moteurs aux frontières `MCP`/`A2A`.
  - **Appui vérifié :** `Corpus/Tome 1` (`L6759–6771`), `Corpus/Tome 2` (`L2767–2902`, `L2970–2975`), `registre/matrice-exig-prr-c40.json`.
  - **Passe initiale :** écart rectifié · **Action :** précisé `satisfaisant au test C26 § 29.4.1` et uniformisé `moteur` dans l'Invariant 2 · **Verdict : supporté**

- **C13-44 (`L134`)** — *Affirmation :* Invariant exécutable 3 : délégation par objet `JSON Schema Draft 2020-12` (`additionalProperties: false` `[9]`) sans historique brut ni jeton ; en `B2B`, politiques hors modèle isolant le Diplomate en `DMZ` (cible illustrative `≤ 4` tours) des prix de réserve de l'Évaluateur ou du `TEE` (`ADR-026`).
  - **Appui vérifié :** `SRC-021.txt` (`[9]`), `Corpus/Tome 2` (`EXIG-ORC-23..25`), `Corpus/Tome 3` (`ADR-026`, `L23688–23730`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié `strict: true` de `[9]`, généralisé `politiques hors modèle` et qualifié `≤ 4` tours de cible illustrative · **Verdict : supporté**
