# Journal d'ancrage Wyvern G2 — Chapitre 01 (`ch01`)

- **Unité auditée :** [Chapitre 01.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/01%20-%20Partie%20I/Chapitre%2001.md) (`4 836` mots, plage `[4 251, 4 989]`)
- **Base documentaire fermée :** [ch01-sources.md](file:///c:/Github/Agentique/Compendium/ouvrage/sources/ch01-sources.md) (`[1]`–`[9]` en statut `L+`, `3` exclusions `statut F`) ; registres `registre/{ancres-chronologiques, faits-empiriques, glossaire-termes}.json` ; protocole `specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; manifeste `recherche/manifeste-sources-sha256.json` (`135` sources `L+`) et `recherche/registre-statut-f.json` (`27` exclusions)
- **Date de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-01`
- **Passe G2 initiale (supportés) :** 21
- **Rectifications appliquées lors de la passe G2 :** 17
- **Verdict final — supportés :** 41 / 41 (100,0 %)

---

## Inventaire atomique et confrontation aux sources `L+`

### Introduction et question directrice (L3–L7)

- **C01-01 (L3)** — *Affirmation :* La question directrice délimite la rupture épistémique entre un assistant conversationnel sans effet de bord et un Système d'agentivité opérant en boucle fermée sur les systèmes d'entreprise, ainsi que la hiérarchie probante de mise en production.
  - **Appui vérifié :** Prescription structurante du domaine `D01` (concordante avec `SRC-027` et `SRC-122`).
  - **Verdict : supporté**

- **C01-02 (L5)** — *Affirmation :* L'IA générative pénètre la couche d'exécution opérationnelle sous l'impulsion d'une **industrialisation cognitive** rapide.
  - **Appui vérifié :** `glossaire-termes.json` (vedette propriétaire `industrialisation cognitive`, ancrée sur `SRC-001`) et `SRC-001.txt` (`L132–L180`).
  - **Verdict : supporté**

- **C01-03 (L5)** — *Affirmation :* Genewein et coll. `[4]` estiment la croissance annuelle du stock de calcul effectif à environ `10×` par an, issue du produit `1,5×` (efficacité matérielle par dollar) × `2,5×` (dépenses d'investissement matériel) × `3×` (progrès algorithmiques) = `11,25×`, prudemment arrondi à `10×`.
  - **Appui vérifié :** `SRC-001.txt` (`L132–L134`, `L153–L160` note 2 p. 4 : « `1.5 * 2.5 * 3 = 11.25, which we round down to 10× per year` », `L173–L174`, `L3084`) et `faits-empiriques.json` (`FACT-COMPUTE-10X`).
  - **Verdict : supporté**

- **C01-04 (L7)** — *Affirmation :* Le chapitre couvre les fondements de la Partie I (`D01`) : boucle fermée, cinq paliers, cinq archétypes, enquêtes de terrain, contrats comportementaux observables, limites des planificateurs autorégressifs, hiérarchie probante à six niveaux et revue `PRISMA-ScR`.
  - **Appui vérifié :** Plan vérifié sur les sections `1.1` à `1.3` de `Chapitre 01.md` et `specs/manifest.json` (`D01`, `SUB_D01_01`).
  - **Verdict : supporté**

### Section 1.1.1 — Boucle fermée et strate `System of Action` (L13–L21)

- **C01-05 (L13)** — *Affirmation :* Un assistant conversationnel classique fonctionne en requête-réponse à tour unique sans état persistant ni actionneur externe, alors qu'une boucle d'itération outillée (perception, décision, action, observation jusqu'à une condition d'arrêt) franchit une frontière épistémique produisant des effets de bord réels `[2]`.
  - **Appui vérifié :** `SRC-122.txt` §2 et §6.1.2–6.1.3 (`L2557–L2613` : passage des prédicteurs statiques et de l'inférence en une passe vers une boucle itérative *Reasoning, Action, Observation* avec appels d'outils/API modifiant des systèmes réels).
  - **Verdict : supporté**

- **C01-06 (L15)** — *Affirmation :* La spécification architecturale du traité formalise cette boucle à l'aide des cadres `PEAS` (*Performance*, *Environment*, *Actuators*, *Sensors*), `BDI` (garde-fou déterministe anti-replanification `EXIG-ORC-16`) et `POMDP` sous contrainte de ressources bornées (temps de calcul, étapes, jetons).
  - **Appui vérifié :** Spécification normative propre au présent traité (`EXIG-ORC-16`, `Corpus/Tome 2` `L3081` ; attribution à `[2]` circonscrite au modèle `BDI`).
  - **Verdict : supporté**

- **C01-07 (L15)** — *Affirmation :* Sur le plan délibératif, le modèle `BDI` (*Beliefs-Desires-Intentions*) distingue les croyances actualisées des intentions engagées `[2]`, ce qui fonde dans la présente architecture un garde-fou déterministe contre la dérive de replanification.
  - **Appui vérifié :** `SRC-122.txt` (`L94–L97` : architectures `BDI` pour le comportement orienté but d'agents logiciels) et règle architecturale interne du traité (rectification G2 appliquée : ancrage `[2]` circonscrit au modèle `BDI`).
  - **Verdict : supporté**

- **C01-08 (L17)** — *Affirmation :* Sans critère d'arrêt externe (`EXIG-ORC-26` et résilience `EXIG-ORC-27` : tours maximaux `≤ 10` étapes en pratique `[1]`, appels d'outils, budget de jetons, coût, durée totale, délai de garde, réessais bornés et repli borné), la boucle risque l'oscillation ou les écritures redondantes ; en production, les équipes limitent délibérément les étapes et la profondeur d'exploration en raison de la complexité, du non-déterminisme de planification, de la latence et des contraintes de vérification `[1, 2]`.
  - **Appui vérifié :** `SRC-027.txt` §5.4 (`L668–L669`), `SRC-122.txt` §2 & §5.2 (`L374`, `L2286–2387`) et spécifications normatives internes `EXIG-ORC-26`/`EXIG-ORC-27` (`Corpus/Tome 2`).
  - **Verdict : supporté**

- **C01-09 (L19)** — *Affirmation :* Cette boucle s'incarne dans les **Systèmes d'agentivité** `[1, 2]`, désignés dans l'architecture du traité sous l'appellation *System of Action* (`SoA`), interposés entre `SoE` et `SoR` selon `ADR-001` sans requête SQL directe et régis par sept critères vérifiables (`action`, `limites`, `identité`, `imputabilité`, `inventaire`, `composition`, `mesure`).
  - **Appui vérifié :** `SRC-027.txt` et `SRC-122.txt` (`[1, 2]`) pour les Systèmes d'agentivité, `glossaire-termes.json` (`Système d'agentivité`), et spécification `ADR-001` du traité (rectification G2 appliquée : attribution `[1, 2]` clarifiée).
  - **Verdict : supporté**

- **C01-10 (L21)** — *Affirmation :* L'isolement de la strate `SoA` vise à remplacer `N×M` connecteurs point-à-point par `N+M` contrats normalisés derrière un point d'application unique et un catalogue gouverné (détaillés aux Chapitres 09 et 10).
  - **Appui vérifié :** Prescription architecturale du traité et partition documentaire vers `ch09` et `ch10`.
  - **Verdict : supporté**

### Section 1.1.2, Tableau 1.1 et Figure 5 (L25–L45)

- **C01-11 (L25)** — *Affirmation :* Sapkota et coll. `[2]` distinguent les agents d'IA unitaires orientés tâches des Systèmes d'agentivité multi-acteurs coordonnant des rôles spécialisés en contexte partagé.
  - **Appui vérifié :** `SRC-122.txt` (`L23–L35`, `L182–L196` : taxonomie différenciant *AI Agents* modulaires orientés tâches et *Agentic AI* multi-agents à coordination et contexte partagé).
  - **Verdict : supporté**

- **C01-12 (L27)** — *Affirmation :* Le référentiel classe les systèmes en cinq paliers (modèle augmenté, flux de travail agentique, agent unique, système multi-agents, système d'IA composé sur `L0–L3`) selon l'entité qui décide du prochain pas d'exécution.
  - **Appui vérifié :** Taxonomie normative propre au présent traité (`specs/manifest.json` `THM_taxonomie-acteurs-agentiques`).
  - **Verdict : supporté**

- **C01-13 (L29)** — *Affirmation :* En cohérence avec le principe de moindre privilège et la défense contre les risques OWASP `ASI01` à `ASI10` `[9]`, le traité proscrit le « super-agent universel » monolithique.
  - **Appui vérifié :** `SRC-055.txt` (`L237–L238` : principes *Least-Privilege* et *Least-Agency* contre l'autonomie excessive ; `L260–L319` : risques `ASI01` à `ASI10`) et règle normative du traité.
  - **Verdict : supporté**

- **C01-14 (L31–L39, Tableau 1.1)** — *Affirmation :* Toute architecture logicielle doit scinder les responsabilités entre cinq archétypes à privilèges disjoints : `Agent d'interface`, `Spécialiste de domaine`, `Travailleur de tâche`, `Orchestrateur` et `Méta-gouverneur`.
  - **Appui vérifié :** Spécification normative d'architecture du traité (`Tableau 1.1`).
  - **Verdict : supporté**

- **C01-15 (L41–L45, Figure 5)** — *Affirmation :* Cette séparation facilite le ciblage économique et sécuritaire des modèles selon la tâche et correspond à la Figure 5 (`SCH-01-01`, zones `Z1`–`Z3`).
  - **Appui vérifié :** Justification architecturale interne et concordance vérifiée avec `schemas/SCH-01-01.puml`.
  - **Verdict : supporté**

### Section 1.1.3 — Écart pilote-production et règle « soutien n'est pas production » (L49–L61)

- **C01-16 (L49)** — *Affirmation :* Les séries de Statistique Canada pour le deuxième trimestre de 2026 (`33-10-1167-01`) mesurent un recours effectif à l'IA au cours des douze derniers mois de `19,2 %` pour l'ensemble des industries et de `40,4 %` en finance et assurances `[6]`.
  - **Appui vérifié :** `SRC-014.txt` (`L3` : SCIAN ensemble des industries = `"19.2"` % ; `L183` : `Finance et assurances [52]` = `"40.4"` %) et `faits-empiriques.json` (`FACT-STATCAN-IA-2026`).
  - **Verdict : supporté**

- **C01-17 (L49)** — *Affirmation :* Au troisième trimestre de 2026 (`33-10-1207-01`), les prévisions d'utilisation pour les douze mois suivants s'établissent à `25,2 %` globalement et à `35,5 %` en finance et assurances `[7]`.
  - **Appui vérifié :** `SRC-015.txt` (`L3` : ensemble des industries = `"25.2"` % prévoyant d'utiliser l'IA au cours des 12 prochains mois ; `L192` : `Finance et assurances [52]` = `"35.5"` %). Rectification G2 appliquée pour distinguer l'usage rétrospectif T2 des prévisions prospectives T3.
  - **Verdict : supporté**

- **C01-18 (L51)** — *Affirmation :* Le document analytique `2026-22` de la Banque du Canada (`2 juin 2026`, `314` entreprises) confirme l'asymétrie sectorielle et montre que `70 %` des dirigeants répondants utilisent personnellement l'IA chaque semaine, mais que seuls `8 %` des établissements déclarent un usage opérationnel important (`21 %` modéré, `29 %` expérimental ou très occasionnel), concentré sur texte, visuel et traitement de données, et freiné par le manque de pertinence opérationnelle perçue, la pénurie de personnel qualifié, l'incompatibilité matérielle/logicielle, les difficultés de données et les obstacles réglementaires `[8]`.
  - **Appui vérifié :** `SRC-016.txt` (`L4–L5`, `L90`, `L94–L98`, `L158–L169`, `L209–L248` Chart 3, `L371–L373`). Rectification G2 appliquée pour aligner les pourcentages exacts et la liste fidèle des usages et obstacles.
  - **Verdict : supporté**

- **C01-19 (L53)** — *Affirmation :* L'étude *Measuring Agents in Production* (`MAP`, Pan et coll., `2 décembre 2025`) a recueilli `306` réponses valides dans `26` domaines — dont `86` points de données en phase pilote ou de production — et conduit `20` études de cas approfondies `[1]`.
  - **Appui vérifié :** `SRC-027.txt` (`L18–L20`, `L306–L316` : `306 valid responses ... 26 application domains`, filtrés à `86 data points explicitly in production or pilot phases`, plus `20 in-depth cases`). Rectification G2 appliquée sur la qualification exacte des `86` points de données.
  - **Verdict : supporté**

- **C01-20 (L53)** — *Affirmation :* Selon `MAP` `[1]`, `68 %` des agents déployés exécutent au plus `10` étapes avant intervention humaine, `80 %` des cas (`16` sur `20`) reposent sur un flux structuré fixe, `70 %` utilisent des modèles sur étagère par invites sans réentraînement supervisé et `74 %` (`74,2 %`) dépendent d'une évaluation humaine directe (complétée dans `51,6 %` des cas par un modèle-juge).
  - **Appui vérifié :** `SRC-027.txt` (`L25–L28`, `L133–L140`, `L541–L542`, `L639–L640`, `L659–L671`, `L858–L864` Figure 8) et `faits-empiriques.json` (`FACT-MAP-STUDY`).
  - **Verdict : supporté**

- **C01-21 (L55)** — *Affirmation :* Le rapport `TMT Predictions 2026` de Deloitte (`18 novembre 2025`) rapporte que plus de `40 %` des projets d'IA agentique risquent d'être annulés à l'horizon `2027` sous l'effet de coûts sous-estimés, d'une mise à l'échelle complexe ou de risques mal maîtrisés, reprenant une estimation de Gartner consignée en statut F `[5]`.
  - **Appui vérifié :** `SRC-011.txt` (`L413`, `L443` : « `more than 40% of today's agentic AI projects could be canceled by 2027, due to unanticipated cost, complexity of scaling, or unexpected risks` », note 3 `L719`), `ch01-sources.md` (`HTTP 403` sur `gartner.com`) et `faits-empiriques.json` (`FACT-GARTNER-ABANDON-2027`). Rectification G2 appliquée sur la formulation exacte des motifs.
  - **Verdict : supporté**

- **C01-22 (L57)** — *Affirmation :* Trois pressions structurelles vérifiées se dégagent : (1) l'enquête *Tech Value Survey* de Deloitte (~`550` dirigeants US) mesure `28 %` de maturité et `12 %` de ROI attendu sous trois ans avec agents contre `80 %` et `45 %` pour l'automatisation de base `[5]` ; (2) la fragmentation des interfaces et protocoles menace de créer des silos propriétaires et des coûts de conformité `[5]` ; (3) le référentiel OWASP souligne les risques liés à la violation de *Least-Agency*, au déficit d'attribution (`ASI03`) et aux pannes en cascade (`ASI08`) `[9]`.
  - **Appui vérifié :** `SRC-011.txt` (`L469`, `L515–L555`), `SRC-055.txt` (`L237–L242`, `L545–L550`, `L1082–L1091`). Rectification G2 appliquée pour substituer ces constats vérifiés aux trois grandeurs dépourvues de pièce `L+` dans le corpus.
  - **Verdict : supporté**

- **C01-23 (L59–L61)** — *Affirmation :* Le traité institue la règle « soutien n'est pas production », appuyée par `MAP` `[1]` où `85 %` des équipes (`17` sur `20`) développent des implémentations internes sur mesure (dont des boucles `ReAct` dédiées) plutôt que des cadriciels rigides, et où les migrations de modèles brisent des flux couplés aux comportements d'un modèle précis (obligeant à maintenir des modèles hérités en parallèle) ; les budgets doivent cibler des boucles `≤ 10` étapes à points d'arrêt humains `[1, 5]`.
  - **Appui vérifié :** `SRC-027.txt` §5.1, §5.4 et §5.5 (`L528–L538`, `L654–L689` : `85 %` `17/20`, `C10` migration de modèle, `C12` `ReAct` sur mesure) et `SRC-011.txt` `[5]`. Rectification G2 appliquée pour remplacer l'exemple hors corpus par ces preuves directes de `SRC-027`.
  - **Verdict : supporté**

### Section 1.1.4, Figure 6 et Trois invariants exécutables (L65–L82)

- **C01-24 (L63)** — *Affirmation :* Les contrats purement syntaxiques (`OpenAPI`, JSON Schema statique) ne garantissent plus la cohérence sémantique d'intentions sous-spécifiées ; le référentiel impose des **contrats comportementaux probabilistes** (`EXIG-D01-01.3`) fixant seuils `pass^k` (`k ≥ 3` minimal, `k ≥ 5` en flux critique, Chapitre 02), tolérance d'écart sémantique, assertions déterministes sur état final et protocole borné d'essais répétés (Chapitres 10 et 23).
  - **Appui vérifié :** Prescription normative d'architecture du traité (`D01`, `EXIG-D01-01.3` et renvois vers `ch02`, `ch10` et `ch23`).
  - **Verdict : supporté**

- **C01-25 (L69–L71)** — *Affirmation :* L'architecture récuse le mentalisme des protocoles classiques (`FIPA-ACL` `SC00061G`/`SC00037J`, `KQML`) au profit d'**engagements sociaux observables** datés, signés et vérifiables depuis l'extérieur afin d'établir objectivement les manquements contractuels.
  - **Appui vérifié :** Règle doctrinale et contractuelle propre au présent traité.
  - **Verdict : supporté**

- **C01-26 (L73–L77, Figure 6)** — *Affirmation :* La Figure 6 (`SCH-01-02`) confronte le discours promotionnel aux données `MAP`, Statistique Canada et Deloitte (`Z1`), applique la règle « soutien n'est pas production » (`Z2`) et illustre le passage aux engagements observables (`Z3`).
  - **Appui vérifié :** Concordance vérifiée avec `schemas/SCH-01-02.svg` et les sources `[1, 5, 6, 7]`.
  - **Verdict : supporté**

- **C01-27 (L79–L82)** — *Affirmation :* L'encadré pose trois invariants exécutables du Chapitre 1 : isolement strict `SoA` (`ADR-001`) sans SQL direct vers `SoR`, répudiation du super-agent avec vérificateur externe (`LLM-Modulo`), et démystification probante sur texte intégral.
  - **Appui vérifié :** Synthèse normative du chapitre conforme à `CA-04`.
  - **Verdict : supporté**

### Section 1.2.1 — Calcul à l'inférence, `PlanBench` et `LLM-Modulo` (L88–L94)

- **C01-28 (L88)** — *Affirmation :* L'expansion du calcul à l'inférence (*test-time scaling* : `Chain-of-Thought`, `ReAct`, `Tree of Thoughts`, modèles « pensants ») plafonne rapidement sur de nombreux benchmarks `[4]`, et Kambhampati et coll. (`2 février 2024`) sur `PlanBench` réfutent la planification fiable en autonomie pure `[3]`.
  - **Appui vérifié :** `SRC-001.txt` (`L228`, `L254`, `L887`, `L1637–L1640`, `L3129–L3130`) et `SRC-121.txt` (`L1–L43`, `L263–L269`, `L392`). Rectification G2 appliquée pour retirer les variantes absentes du corpus `L+`.
  - **Verdict : supporté**

- **C01-29 (L90)** — *Affirmation :* Sur les domaines IPC de `PlanBench` `[3]`, `GPT-4` ne produit en moyenne qu'environ `12 %` de plans exécutables sans erreur, et les performances s'effondrent sous obfuscation `Mystery BW` (en *zero-shot* : `GPT-4` de `34,6 %` à `0,16 %`, `GPT-4o` de `35,5 %` à `0 %`, `Claude-3-Opus` de `59,3 %` à `0 %`), démontrant une récupération approximative plutôt qu'une planification formelle, que ni `Chain-of-Thought` ni `ReAct` ne corrigent sans vérificateur externe.
  - **Appui vérifié :** `SRC-121.txt` (`L47–L49`, `L172–L174`, `L179–L248` Table 1, `L254–L269`). Rectification G2 appliquée pour ancrer exactement les mécanismes et chiffres sur `SRC-121`.
  - **Verdict : supporté**

- **C01-30 (L92)** — *Affirmation :* Le modèle linguistique reste un générateur heuristique utile à condition d'être inséré dans un cadre hybride **`LLM-Modulo`** (distinct d'une traduction unidirectionnelle `LLM+P`) couplé à des vérificateurs et critiques externes déterministes (ex. `VAL`, solveurs, règles métier) qui certifient le plan ou renvoient des contre-exemples structurés `[3]`.
  - **Appui vérifié :** `SRC-121.txt` §1 et §3 (`L68–L74`, `L120–L147`, `L481–L583`). Rectification G2 appliquée pour refléter la distinction exacte de `SRC-121` entre `LLM-Modulo` et `LLM+P`.
  - **Verdict : supporté**

- **C01-31 (L94)** — *Affirmation :* La trace de raisonnement `Chain-of-Thought` souffre d'infidélité : incapable d'auto-vérification fiable `[3]`, le modèle peut aussi voir ses objectifs détournés (`ASI01`) ou subir des pannes en cascade (`ASI08`) tout en dissimulant des erreurs à la supervision `[9]` ; cette trace ne doit jamais tenir lieu de mécanisme de sécurité ni de piste d'audit opposable.
  - **Appui vérifié :** `SRC-121.txt` §2.2 (`L270–L321`), `SRC-055.txt` (`L325–L345`, `L1082–L1091`, `L2041–L2043`) et prescription normative du traité. Rectification G2 appliquée pour ancrer strictement chaque clause sur `[3, 9]`.
  - **Verdict : supporté**

### Section 1.2.2, Tableau 1.2 et Figure 7 (L98–L123)

- **C01-32 (L98–L109, Tableau 1.2)** — *Affirmation :* La hiérarchie probante à six niveaux classe : (1) les études de production arbitrées par les pairs (rares au gel du `2 décembre 2026`, aucune ne documentant encore `MCP` ou `A2A` à grande échelle en finance `[1, 5]`) ; (2) les enquêtes systématiques de terrain (`MAP` `[1]`) ; (3) les études ou enquêtes publiées par des éditeurs ou cabinets (*Tech Value Survey* via Deloitte `[5]`) ; (4) les bancs contrôlés reproductibles (`PlanBench` et `TravelPlanner` `[3]`, passant avec `GPT-3.5-Turbo` de `0,7 %` à `6×` sous `LLM-Modulo`) ; (5) les enquêtes statistiques générales sans audit d'isolation (`[6, 7, 8]`) ; (6) le déclaratif non audité ou bloqué en statut F (exclu).
  - **Appui vérifié :** `SRC-027.txt` `[1]`, `SRC-121.txt` (`L733–L746` pour `TravelPlanner` `0,7 %` et gain `6×` `[3]`), `SRC-011.txt` `[5]`, `SRC-014.txt` `[6]`, `SRC-015.txt` `[7]`, `SRC-016.txt` `[8]`. Rectification G2 appliquée pour remplacer les exemples externes non archivés par des preuves intégrales `L+`.
  - **Verdict : supporté**

- **C01-33 (L111–L113)** — *Affirmation :* Au gel du `2 décembre 2026`, aucune étude de niveau 1 de la base fermée ne documentait encore `MCP` ou `A2A` à grande échelle en finance critique `[1, 5]` ; l'écart entre les scores sur `PlanBench` (`~12 %` en moyenne, `0 %`–`0,16 %` sous obfuscation `[3]`) ou l'écart de niveau 5 (`70 %` personnel vs `8 %` opérationnel `[8]`) et les exigences bancaires impose des mesures internes avant généralisation.
  - **Appui vérifié :** `ch01-sources.md`, `SRC-027.txt` `[1]`, `SRC-121.txt` `[3]`, `SRC-011.txt` `[5]`, `SRC-014.txt` `[6]`, `SRC-015.txt` `[7]`, `SRC-016.txt` `[8]`. Rectification G2 appliquée pour retirer les références absentes du corpus `L+`.
  - **Verdict : supporté**

- **C01-34 (L115–L117)** — *Affirmation :* La veille documentaire suit le protocole `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`AO-01` / `AO-02`) sur `11` interfaces ouvertes (`2023–2026` et classiques fondateurs jusqu'au `2 décembre 2026`), consignant `27` exclusions en statut F sans contournement (`3` dans `ch01-sources.md` : Gartner, Statistique Canada HTML `11-621-m`, `genai.owasp.org`) et réunissant `135` textes intégraux `L+` `SHA-256` (`AACODS` `9,0` à `12,0/12`, moyenne `11,13/12`, `0,0 %` `METADATA_ONLY`, dont `9` au Chapitre 01 de `9,5` à `11,5/12`) sur les `12` domaines `D01` à `D12`.
  - **Appui vérifié :** `specs/protocole-mlr-compendium.json`, `recherche/manifeste-sources-sha256.json`, `recherche/registre-statut-f.json`, `sources/ch01-sources.md`. Rectification G2 appliquée pour remplacer les métriques d'un lot antérieur par les métriques exactes vérifiées sur les registres du Compendium.
  - **Verdict : supporté**

- **C01-35 (L119–L123, Figure 7)** — *Affirmation :* La Figure 7 (`SCH-01-03`) illustre la logique de tamisage probatoire en reprenant le modèle visuel issu du tri préliminaire `W3.2` opérationnalisé sous `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`, articulé à la pyramide à six niveaux et au filtre `LLM-Modulo`.
  - **Appui vérifié :** Concordance vérifiée avec `schemas/SCH-01-03.puml` et `specs/protocole-mlr-compendium.json`. Rectification G2 appliquée pour clarifier la filiation entre le diagramme figé et le protocole consolidé.
  - **Verdict : supporté**

### Section 1.3 et Tableau 1.3 (L127–L145)

- **C01-36 (L127–L137, Tableau 1.3)** — *Affirmation :* Cinq exigences normatives (`EXIG-D01-01.1` à `EXIG-D01-01.5`) fixent les artefacts de preuve exigés avant mise en production : fiche `SoA`/`SoR` (`ADR-001`, `7` critères), matrice des `5` archétypes et `5` paliers, contrats comportementaux et engagements observables, harnais `LLM-Modulo` (`PlanBench` `[3]`) avec exclusion de `Chain-of-Thought` comme barrière `[9]`, et tableau de bord `MLR` dissociant soutien (`≤ 10` étapes) et production sur les `6` niveaux (`SHA-256`, `0,0 %` sur résumé).
  - **Appui vérifié :** Spécification normative du traité (`Tableau 1.3`), appuyée sur `[3]` (`SRC-121`), `[9]` (`SRC-055`) et `protocole-mlr-compendium.json`.
  - **Verdict : supporté**

- **C01-37 (L139–L141)** — *Affirmation :* Le chapitre respecte une partition stricte des concepts avec l'aval (`ch08`, `ch09`, `ch10`, `ch15`, `ch23`, `ch31`) et l'amont (`ch03`, `ch05`, `ch12`, `ch13`, `ch25`, `ch30`, `ch32`, `ch36`).
  - **Appui vérifié :** Cohérence vérifiée avec `specs/manifest.json` (`owned_concepts`) et `CA-21`.
  - **Verdict : supporté**

- **C01-38 (L143–L145)** — *Affirmation :* Cinq livrables concrets matérialisent le chapitre avant exploitation réelle (fiche `SoA` + matrice des `5` archétypes, spécification `PEAS`/`POMDP`, banc `LLM-Modulo`, dossier probatoire `6` niveaux / `PRISMA-ScR`, tableau de bord soutien vs production), en prélude à l'étude de la dégradation en série au Chapitre 02.
  - **Appui vérifié :** Prescriptions opérationnelles du traité et transition vérifiée vers `ch02`.
  - **Verdict : supporté**

---

## Mise à jour post-révision PRD (`REV-04`)

- **C01-REV-01 (`§ 1.1.3`, `§ 1.1.4`, `SCH-01-02.svg`, `PRD-L1-004`, `PRD-L1-012`)** — *Affirmation :* Raccord explicite entre la base fermée `L+` du chapitre (`MAP`, Statistique Canada, Banque du Canada, Deloitte, OWASP) et les repères de veille du corpus affichés dans `SCH-01-02.svg` (`McKinsey 40 %`, `MIT NANDA 95 %`, `CyberArk 82:1`, `AIE 415 → 945 TWh`, cas `Nubank KDD 2026` sur `5` agents `ReAct` sans `MCP`/`A2A`), et mention des jalons conceptuels `Bhardwaj (2026)`, `Singh (1998)` et `Yolum & Singh (2002)`.
  - **Appui vérifié :** `Compendium/prd.md` (`L441`, `L445`, `L453`, `L466`), `schemas/SCH-01-02.svg`, `SRC-027` (`[1]`), `SRC-011` (`[5]`), `SRC-055` (`[9]`).
  - **Verdict : supporté**

- **C01-REV-02 (`§ 1.2.1`, `Tableau 1.2`, `§ 1.2.2`, `SCH-01-03.puml`, `PRD-L1-004`, `PRD-L1-012`, `PRD-L1-015`)** — *Affirmation :* Ajout de `Graph of Thoughts`, `LATS`, `DeepSeek-R1`, `PRM` par rapport à `ORM`, alignement délibératif et `arXiv:2507.11473` (veille corpus), complétion du *Tableau 1.2* (`Nubank`, `ServiceNow`, `SEC 0,758`, `ITBench 10–25 %`, `ORCA-bench`, `Eurostat 2025`, `MCN 432`), retrait de `vs` (`L104`), et explicitation du raccord `PRISMA-ScR W3.2` (`582 → 453 → 223 → 160`, `AACODS 9,97/12`, `κ = 0,7935`) vers la base fermée `L+` (`135` textes `SHA-256`, `AACODS 11,13/12`, `27` exclusions `F`) alignée sur `SCH-01-03.puml`.
  - **Appui vérifié :** `Compendium/prd.md` (`L466`, `L470`, `L474`), `schemas/SCH-01-03.puml`, `recherche/manifeste-sources-sha256.json`.
  - **Verdict : supporté**

- **C01-REV-03 (`L29`, `§ 1.1.2`)** — *Affirmation :* Distinction conceptuelle entre la strate architecturale `SoA` et **l'agentivité des systèmes** (*system agency*), propriété émergente et composite de l'assemblage sociotechnique complet (opposant oracle purement cognitif et boucle outillée gouvernée hors modèle, calibrée selon le principe de moindre agence).
  - **Appui vérifié :** `SRC-001.txt` (`[4]`, `L1810–L1817`), `SRC-122.txt` (`[2]`, `L26–L30`), `SRC-055.txt` (`[9]`, `L237–L242`), `registre/glossaire-termes.json` (vedette `Agentivité des systèmes`).
  - **Verdict : supporté**

- **Contrôle `REV-05` :** `4 682` mots (`verifie_manuscrit.py`) dans `[4 251, 4 989]`, `verifie_manuscrit.py --unit ch01 --strict` = `exit 0`. **Verdict final : `41 / 41` (`100,0 %` supporté).**
