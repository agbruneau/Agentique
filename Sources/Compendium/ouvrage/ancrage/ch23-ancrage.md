# Journal d'ancrage atomique Wyvern G2 — Chapitre 23 (`ch23`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/08 - Partie VIII/Chapitre 23.md` (`4 351` mots de prose `verifie_manuscrit`, `4 720` mots `parser_plan`, plage `[4 076, 4 784]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch23-sources.md` (`[1]`–`[8]` en statut `L+`, `2` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) et trousse `Tome 8` (`evalops_prr/`, `policies_opa/`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-2`
- **Passe G2 initiale (supportés) :** 14
- **Rectifications appliquées lors de la passe G2 :** 18
- **Verdict final — supportés :** 32 / 32 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 23.md`

Toutes les formulations divergentes, sur-affirmées ou insuffisamment attribuées relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 23.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/08%20-%20Partie%20VIII/Chapitre%2023.md), sans toucher au bloc scellé `CA-G0-SYNC` (`G0-EX-CH04-02`, lignes `74–102`), en préservant les `owned_concepts` (`banc-evalops-hermetique`, `evaluation-agentique-bancs-capacite`, `dimensionnement-wilson-evalops`, `volant-distillation-dspy-multilora`, `tests-metamorphiques-fr-en-sans-oracle`, `evaluation-continue-derives`, `modele-comme-juge-biais-calibration`), les vedettes du glossaire, l'ensemble des renvois `[1]`–`[8]` et le calibrage (`4 351` / `4 720` mots dans `[4 076, 4 784]`) :

1. **Ancrage exact des études `MAP`, `HAL`, `τ-bench` et `MORTAR` (`L5`, `L23`, `L25`, `L66`) :** rattachement de l'étude `MAP` (`74 %` d'évaluation humaine dans la boucle, rareté des bancs formels et expertise nuancée, `SRC-027.txt`) au `Chapitre 01` et dissociation de l'exigence d'équité bilingue (`EXIG-SEC-24`, `EXIG-AMF-11`) des renvois `[3, 4]` ; alignement des observations de `HAL` (`SRC-030.txt` : recherche sur *HuggingFace*, fuites de données sur certains échafaudages, score nul sur abstentions prudentes) et séparation des bancs vérifiés dans `[3, 4]` (`SWE-bench`, *Online Mind2Web*, `τ-bench`, `BFCL` cité dans `[3]`, `GAIA`) de ceux cités au `Tome 1 § 6.3.3` (`WebArena`, `OSWorld`) ; clarification que `∼35 %` sur `τ-airline` mesure `pass^1` (et non `pass^8`) et ajout des proportions d'échecs vérifiées dans `SRC-029.txt` (`∼55 %` arguments/informations erronés, `25 %` infractions aux règles) ; correction de `MORTAR` (`SRC-092.txt`) pour décrire ses sept perturbations au niveau du dialogue (permutation, réduction, duplication de tours et combinaisons, sans reformulation sémantique) et qualifier `75,8 %` contre `60,8 %` (`METAL`) comme précision des défauts détectés (`+24,6 %` relatif).
2. **Séparation entre corpus `L+` fermé et littérature / cibles du `Corpus` (`L15`, `L27`, `L29`, `L34`, `L41`, `L68`, `L115`–`L127`) :** attribution explicite au `Tome 6 § 11.2.1–11.2.2` et à `evaluate_trajectory` de la grille `task`/`trial`/`transcript`/`outcome` et des modes `EXACT`/`IN_ORDER`/`ANY_ORDER` ; qualification de `AgentArcEval` (étude de cas unique, `Tome 3 § 23.8`) et de `PRR O-04` (cible durcie calibrée par criticité) ; correction du balisage mathématique \(\epsilon_R = \epsilon / p\) ; qualification de la suite `G0` sur vecteurs synthétiques (`L68`) ; rattachement explicite des quatre biais des juges (`Tome 1 § 6.3.2`), des treize modèles juges et du *criteria drift* (`Tome 6 § 11.2.4`) ainsi que de `Microsoft Foundry` (`11` évaluateurs dont `5` en préversion au `2 juin 2026`) et `Langfuse` (`Tome 1 § 39.1`) à l'index interne hors corpus `L+` fermé ; alignement exact de `F-23`, `F-52` et `H-12` sur `Tome 1 § 39.2` et `Tome 6 § 11.3.3` (`MMD`).
3. **Qualification de la recette cible `ADR-031` (`L15`, `L133`–`L144`, `Tableau 23.3`, `L165`) :** caractérisation explicite du volant `DSPy`/`MIPROv2` → `Multi-LoRA` (`ADR-031`, `PRR F-15`, acceptée sous réserve de validation empirique au `Tome 3 § 47.20–47.22`) et de ses paramètres (`S-LoRA`/`Punica`, `r = 32`, `67` Mo `FP16`, `V_min`, `2 000–15 000` trajectoires `SFT`, `14` jours, `200` canaris Carlini, `pass^5 ≥ 99 %` sur `holdout 15 %`, sentinelle `2 %`, cycle `90–180` jours, objectif `10×` plus sobre) comme cibles de conception à valider sans mesure interne sur un élève distillé.

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C23-01` à `C23-32`)

### Section 23.0 — Titre, question directrice et cadrage introductif (`L1–L7`)

- **C23-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice couvrant les bancs hermétiques `E1–E3`, les bornes de Wilson, les tests métamorphiques `FR`/`EN` et la distillation contrôlée du sous-domaine `SUB_D08_02`.
  - **Appui vérifié :** `specs/manifest.json` (`ch23`, `D08`, `SUB_D08_02`, `owned_concepts`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-02 (`L5`)** — *Affirmation :* L'étude `MAP` (`← Chapitre 01`) relève que `74 %` des systèmes déployés s'appuient principalement sur l'évaluation humaine dans la boucle (rareté des bancs formels et tâches exigeant une expertise nuancée), tandis que l'antipatron `AP-12` masque les régressions silencieuses lors des mises à jour derrière alias ou refontes d'invites, menaçant la constance d'exécution `[3, 4]` et l'équité bilingue `FR`/`EN` (`EXIG-SEC-24`, `EXIG-AMF-11`).
  - **Appui vérifié :** `corpus_l_plus/SRC-027.txt` (`L1840`, `74 %`, `§ 7.2`, propriétaire `ch01`), `SRC-029.txt` (`[3]`), `SRC-030.txt` (`[4]`), `Corpus/Tome 6` (`L4842`, `AP-12`), `registre/matrice-exig-prr-c40.json` (`EXIG-SEC-24`, `EXIG-AMF-11`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché `MAP` à `← Chapitre 01` avec sa formulation exacte, singularisé `antipatron AP-12` et dissocié `[3, 4]` de l'exigence bilingue `EXIG-SEC-24` / `EXIG-AMF-11` · **Verdict : supporté**

- **C23-03 (`L7`)** — *Affirmation :* Cadrage `EvalOps` de `D08` au gel du `2 décembre 2026`, continuité avec `pass^k` (`← Chapitre 02`) et `SOC`/`SOAR` (`← Chapitre 21`), extrait vérifié `G0-EX-CH04-02` (`evalops_prr/metamorphic.py`), clause `non-avis` (`AO-05`) et restriction des preuves exécutables aux doublures synthétiques hors modèle.
  - **Appui vérifié :** `specs/protocole-mlr-compendium.json` (`2026-12-02`), `aq/rapports-g0.json` (`G0-EX-CH04-02`, `L162–168`), `evalops_prr/metamorphic.py`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 23.1 — Résumé exécutif (`L9–L15`)

- **C23-04 (`L11`)** — *Affirmation :* Règle 1 (`EXIG-EVA-01` à `EXIG-EVA-06`, `EXIG-GOV-12`, `EXIG-SEC-24`, `EXIG-AMF-11`, `CAP-043`, `CAP-044`, `DEC-010`, `ADR-022`, `ADR-031`) : manifestes `SemVer+Intent` sans `latest`, relance obligatoire `E1`/`E2` (`MockMcpServer` sans `SoR` réel), promotion fantôme puis canari, et surveillance `E3` sur `≥ 5 %` du trafic réel (`10 %` recommandé) et `100,0 %` des anomalies.
  - **Appui vérifié :** `Corpus/Tome 2` (`L5021–5051`, `EXIG-EVA-01..04`), `registre/matrice-exig-prr-c40.json` (`CAP-043`, `CAP-044`, `DEC-010`, `ADR-022`).
  - **Passe initiale :** écart rectifié · **Action :** reformulé `≥ 5–10 %` en `≥ 5 % du trafic réel (10 % recommandé)` selon `EXIG-EVA-04` · **Verdict : supporté**

- **C23-05 (`L13`)** — *Affirmation :* Règles 2 et 3 : substitution de `pass@k` par la **Constance pass^k** / **constance multi-essais** (`k ≥ 3` minimal, `k ≥ 5` critique), **Borne de Wilson** unilatérale à `95 % < p` (`n ≥ ceil(3/p)`, `300` essais donnant `0,8938 % < 1 %`, rejetant Wald et `n = 299`) `[1, 2, 3]`, et **Test métamorphique sans oracle** sur `≥ 100` scénarios `FR`/`EN` couvrant `OWASP ASI01–10` `[5, 6, 7, 8]`.
  - **Appui vérifié :** `SRC-022.txt` (`[1]`), `SRC-094.txt` (`[2]`), `SRC-029.txt` (`[3]`), `SRC-091.txt` (`[5]`), `SRC-092.txt` (`[6]`), `SRC-093.txt` (`[7]`), `SRC-055.txt` (`[8]`), `registre/faits-empiriques.json` (`FACT-WILSON-3P`), `registre/glossaire-termes.json`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-06 (`L15`)** — *Affirmation :* Règles 4 et 5 : juge hétérogène à paires permutées ré-étalonné trimestriellement sur annotations humaines (p. ex. `κ ≥ 0,6`) hors chemin critique, sentinelle des `3+1` dérives avec abaissement automatique d'autonomie après `3` mois hors `SLO` (`EXIG-EVA-06`), et recette cible `DSPy` → `Multi-LoRA` (`ADR-031`, acceptée sous réserve de validation) sur trajectoires validées sans compensation ni `PII`, testées par canaris et porte cible `pass^5`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L5053–5066`, `EXIG-EVA-05..06`), `Corpus/Tome 3` (`L26026–26035`, `ADR-031`), `registre/matrice-exig-prr-c40.json` (`ADR-031`, `PRR F-15`).
  - **Passe initiale :** écart rectifié · **Action :** exemplifié le seuil contractuel `κ ≥ 0,6` et qualifié `DSPy` → `Multi-LoRA` de recette cible `ADR-031` acceptée sous réserve de validation · **Verdict : supporté**

### Section 23.2.1 — Bancs EvalOps hermétiques E1–E3, constance `pass^k` et bornes de Wilson (`L19–L60`)

- **C23-07 (`L21`)** — *Affirmation :* Dans `HAL` (`[4]`), Kapoor et ses collègues exécutent `21 730` essais sur `9` modèles et `9` bancs pour `2,5` milliards de jetons et environ `40 000 \$ US`, montrant que hausser l'effort de raisonnement donne une précision inférieure ou au mieux égale dans `21` combinaisons sur `36`.
  - **Appui vérifié :** `SRC-030.txt` (`L44–51`, `L95–96`, `L745–746`, `L955–959`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-08 (`L23`)** — *Affirmation :* L'inspection des journaux de `HAL` (`[4]`) relève la recherche de corrigés sur *HuggingFace*, l'usage erroné de numéros de carte simulés, des fuites de données sur certains échafaudages et des barèmes attribuant zéro aux abstentions prudentes ; les bancs ciblés couvrent `SWE-bench`, *Online Mind2Web*, `WebArena` et `OSWorld` (`Tome 1 § 6.3.3`), ainsi que `τ-bench`, `BFCL` (cité dans `[3]`) et `GAIA` (`[3, 4]`), exigeant une analyse de la distribution complète sous décontamination.
  - **Appui vérifié :** `SRC-030.txt` (`L48–50`, `L100+`, fuites `TAU-bench Few Shot`, `abstain`/`abstention`, `Online Mind2Web`, `SWE-bench`, `GAIA`), `SRC-029.txt` (`L121`, `BFCL`), `Corpus/Tome 1` (`L1626–1630`, `WebArena`, `OSWorld`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé « fuites de harnais et consignes d'abstention » par les constats exacts de `SRC-030.txt` et dissocié les bancs présents dans `[3, 4]` de ceux indexés au `Tome 1 § 6.3.3` · **Verdict : supporté**

- **C23-09 (`L25`)** — *Affirmation :* Dans `τ-bench` (`[3]`), `gpt-4o` (appel de fonctions) atteint environ `61 %` en `pass^1` sur `τ-retail` contre environ `35 %` en `pass^1` sur `τ-airline`, puis chute sous `25 %` à `pass^8` sur `τ-retail`, avec environ `55 %` d'échecs liés aux arguments ou informations erronées et `25 %` aux infractions aux règles métier ; à `75 %` de succès unitaire, `pass@3 = 98,44 %` contre `pass^3 = 42,19 %`.
  - **Appui vérifié :** `SRC-029.txt` (`L18`, `L105–107`, `L476`, `L488–489`, `L534–544`) et calcul arithmétique direct (\(1 - 0{,}25^3 = 0{,}984375\), \(0{,}75^3 = 0{,}421875\)).
  - **Passe initiale :** écart rectifié · **Action :** levé l'ambiguïté entre `pass^1` (`∼35 %` sur `τ-airline`) et `pass^8` (`< 25 %` sur `τ-retail`), et inscrit les taux de ventilation `∼55 %` et `25 %` de `SRC-029.txt` · **Verdict : supporté**

- **C23-10 (`L27`, `L29`)** — *Affirmation :* Séparation en quatre objets (*task*, *trial*, *transcript*, *outcome*, `Tome 6 § 11.2.1`) et découplage de l'infrastructure de notation `[3, 4]` ; modes de contrôle des outils (`EXACT`, `IN_ORDER`, `ANY_ORDER`) et compteurs informatifs d'efficience (`Tome 6 § 11.2.2`, `evaluate_trajectory` en `G0`).
  - **Appui vérifié :** `SRC-029.txt` (`[3]`), `SRC-030.txt` (`[4]`), `Corpus/Tome 6` (`L3500`, `L3514`), `evalops_prr/mock_mcp_harness.py` (`evaluate_trajectory`, `L106–141`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement le vocabulaire `transcript`/`outcome` et les trois modes `EXACT`/`IN_ORDER`/`ANY_ORDER` au `Tome 6 § 11.2.1–11.2.2` et à `evaluate_trajectory` · **Verdict : supporté**

- **C23-11 (`L31`, `L33`)** — *Affirmation :* Banc `E1–E3` déclenché sur tout changement visé par `EXIG-GOV-12` ; l'étage `E1` sans modèle valide `JSON Schema 2020-12` (rejet `$ref` réseau non résolus), `a2a-tck` (`MUST` bloquant), `OPA`/`Rego` (`default allow := false`) et fautes `Saga`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L5004`, `L5025`), `aq/rapports-g0.json` (`L26–50`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-12 (`L34`)** — *Affirmation :* L'étage `E2` exécute l'agent contre `MockMcpServer` (catalogue trié déterministe, graine fixée, copie profonde, rejet `float` `IEEE-754` pour `Decimal`) et simulateurs du traité (`OpenEnv`, `τ-bench`, `AgentArcEval` documenté sur une étude de cas au `Tome 3 § 23.8`) sous pannes `HTTP 429`/`503` `[3, 4]`, sur `≥ 50` scénarios `CAD26` (`EXIG-EVA-02`) et `≥ 100` en cible durcie `PRR O-04` calibrée par criticité (avec sous-ensemble secret), joués `k ≥ 3` (`k ≥ 5` critique) via `compute_pass_k` (`ValueError` sur `pass@k`), avant mode fantôme puis canari.
  - **Appui vérifié :** `evalops_prr/mock_mcp_harness.py` (`L23–104`), `Corpus/Tome 2` (`L5033`), `Corpus/Tome 3` (`L12558`), `registre/matrice-exig-prr-c40.json` (`PRR O-04`), `Compendium/prd.md` (`L4322`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `AgentArcEval` (étude de cas unique au `Tome 3 § 23.8`) et `PRR O-04` (cible durcie calibrée par criticité), et scindé la phrase de tête pour respecter `CA-05` (`≤ 70` mots) · **Verdict : supporté**

- **C23-13 (`L35`)** — *Affirmation :* L'étage `E3` échantillonne au moins `5 %` du trafic réel (`10 %` recommandé) et `100,0 %` des anomalies (`EXIG-EVA-04`, dépôt chiffré `30` jours, événement `gen_ai.evaluation.result`), déclenche un repli en `< 60 s` (`POR-015`) sur épuisement du budget d'erreur, ouvre une revue après `2` mois hors cible et abaisse l'autonomie d'un palier après `3` mois consécutifs hors `SLO` (`EXIG-EVA-06`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L5049`, `L5065`, `L5069`), `registre/matrice-exig-prr-c40.json` (`POR-015`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la formulation sur `au moins 5 % (10 % recommandé)` selon `EXIG-EVA-04` · **Verdict : supporté**

- **C23-14 (`L37–L39`, Figure 1)** — *Affirmation :* La Figure 1 (`SCH-23-01.svg`) illustre les trois étages `E1–E3`, les doublures `MockMcpServer`, la contrainte `pass^k` / Wilson (`≥ 300`), la promotion fantôme → canari et la rétrogradation après `3` mois hors `SLO`.
  - **Appui vérifié :** `specs/manifest.json` (`ch23`, `SCH-23-01`), `schemas/SCH-23-01.puml`, `schemas/rendus/SCH-23-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-15 (`L41`, `L43`, `L45`)** — *Affirmation :* Sous `EXIG-EVA-03`, le dimensionnement repose sur `NIST/SEMATECH § 7.2.4.1` `[1]` et McGrath & Burke (`arXiv:2109.02516`) `[2]` : l'intervalle de Wald s'effondre près de `0` (borne nulle à `0` échec, borne inférieure négative) et la précision doit être relative à `p` (\(\epsilon_R = \epsilon / p\)) ; l'intervalle du score de Wilson (1927) s'exprime exactement par \(U_{\text{Wilson}}(k, N, z)\).
  - **Appui vérifié :** `SRC-022.txt` (`L26–85`, `L126–139`), `SRC-094.txt` (`L68–95`, `L210–213`), `evalops_prr/wilson_bounds.py` (`L43–54`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé le rendu mathématique de \(\epsilon_R = \epsilon / p\) (retiré les backticks littéraux) · **Verdict : supporté**

- **C23-16 (`L47`, `L49`, `L51`)** — *Affirmation :* Le module `wilson_bounds.py` vérifié en `G0` applique le quantile unilatéral `z = 1,644854` (`0,8938 % < 1 %` à `N = 300`, `k = 0`) contre `1,2643 %` en bilatéral (`z = 1,959964`, exigeant `381` essais pour `0,9982 % < 1 %`), impose conjointement `wilson_failure_upper_95 < p` et `n ≥ ceil(3/p)` (`n = 299` à `0,8967 %` rejeté ; `k = 1` à `N = 300` → `1,4801 %` rejeté ; `p = 5 %` → `60` à `4,3147 %` ; `p = 0,5 %` → `600` à `0,4489 %`) et contrôle l'unicité `scenario_ids` (`[1, 2, 3]`, `FACT-WILSON-3P`).
  - **Appui vérifié :** `evalops_prr/wilson_bounds.py`, `tests/test_evalops_prr.py` (`L173–223`), `registre/faits-empiriques.json` (`FACT-WILSON-3P`), vérification numérique Python directe.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-17 (`L53–L60`, Tableau 23.1)** — *Affirmation :* Le `Tableau 23.1` résume les étages `E1–E3` et la borne de Wilson en cohérence avec la prose et la barrière `G0`.
  - **Appui vérifié :** `Chapitre 23.md` (`L31–L51`), `aq/rapports-g0.json`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 23.2.2 — Tests métamorphiques `FR`/`EN`, étalonnage des juges, `3+1` dérives et volant `DSPy` → `Multi-LoRA` (`L62–L144`)

- **C23-18 (`L64`)** — *Affirmation :* Consignation en `statut F` (`AO-01`, `HTTP 403`) de `dl.acm.org/doi/10.1145/3143561` et `genai.owasp.org` hors évidence directe, le socle s'appuyant sur des textes ouverts `L+`.
  - **Appui vérifié :** `sources/ch23-sources.md` (`L99–102`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-19 (`L66`)** — *Affirmation :* Bozic & Wotawa (`[5]`, `HAL`) appliquent les relations métamorphiques aux agents conversationnels sans oracle ; `MORTAR` (`[6]`, `SRC-092`) couvre le multi-tours (`> 63 %` des dialogues réels dépassant `2` tours) par sept perturbations au niveau du dialogue (permutation, réduction, duplication de tours et combinaisons), révélant `51 %` de bogues supplémentaires par cas d'essai face à `METAL` et atteignant `75,8 %` de précision des défauts détectés après inspection manuelle contre `60,8 %` (`+24,6 %` relatif) ; Chen, Besenk & Stocco (`[7]`, `SRC-093`) obtiennent `2,30×` plus de cas vérifiés révélateurs de défauts via `BNLI` et `LPS` que les stratégies heuristiques.
  - **Appui vérifié :** `SRC-091.txt` (`[5]`), `SRC-092.txt` (`L21–26`, `L99`, `L290–296`, `L1870`, `L1896–1905`, `L2030`), `SRC-093.txt` (`L23–25`, `L79–80`).
  - **Passe initiale :** écart rectifié · **Action :** supprimé l'allégation de « reformulation sémantique » sur les sept perturbations de `MORTAR`, précisé `75,8 %` / `60,8 %` comme précision des défauts détectés (`+24,6 %` relatif face à `METAL`) et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C23-20 (`L68`)** — *Affirmation :* Batterie métamorphique sans oracle sur `≥ 100` scénarios `FR`/`EN` (`EXIG-SEC-24`, `EXIG-AMF-11`) couvrant `OWASP ASI01`–`ASI10` (`v1.0` CC BY-SA 4.0 avec mention non-avis, `[8]`) et contrôles synthétiques en trois couches (`rule_of_two.rego` sur `ASI01`/`02`/`04`/`08`/`10`, `camel_taint.rego` sur `ASI06`/`07`, `sandbox_confinement.rego` sur `ASI03`/`05`, et paires `FR`/`EN` sur `ASI01`–`ASI10`).
  - **Appui vérifié :** `SRC-055.txt` (`[8]`, `L13–18`), `tests/test_third_party_vectors.py` (`L359–469`), `policies_opa/{rule_of_two.rego, camel_taint.rego, sandbox_confinement.rego}`.
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement de « suite synthétique `G0` » la batterie de vérification `OPA` + `metamorphic.py` · **Verdict : supporté**

- **C23-21 (`L70`)** — *Affirmation :* Jalons réglementaires préparés : Loi 25 art. `12.1` (`22 septembre 2023`), art. `50` `EU AI Act` (`août 2026`, régime transitoire `2 décembre 2026`), Annexe III (`2 décembre 2027`), Annexe I (`2 août 2028`), prise d'effet attendue de `BSIF E-23` (`1er mai 2027`, repère suivi côté `AMF` sous réserve du `statut F` de `lautorite.qc.ca`) et trajectoire `G7` `2030–2035`.
  - **Appui vérifié :** `registre/ancres-chronologiques.json` (`2026-LOI25-ART12-1`, `2026-08-02-EU-AI-ACT-ART50`, `2027-05-01-BSIF-E23-AMF`, `2027-12-02-EU-AI-ACT-ANNEXE-III`, `2028-08-02-EU-AI-ACT-ANNEXE-I`, `2030-2035-G7-PQC-FINANCE`, `ANC-112`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-22 (`L72–L104`)** — *Affirmation :* Extrait scellé `G0-EX-CH04-02` (`evalops_prr/metamorphic.py`, lignes `38–63`, SHA-256 `31ad0df04f1930471a8cec511d897834f72c35851e98f9c7cae1aa82002c1472`) et explication de `b.blocked`, `is_non_avis_disclosed` ainsi que des cas négatifs `G0` (`0,90 \$ CA` vs `0,50 \$ CA`).
  - **Appui vérifié :** `aq/rapports-g0.json` (`L162–168`), `evalops_prr/metamorphic.py` (`L38–63`), `tests/test_evalops_prr.py` (`L258–419`), bloc `CA-G0-SYNC` intact.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-23 (`L106–L113`, Tableau 23.2)** — *Affirmation :* Tableau des quatre relations métamorphiques, propriétés invariantes, scénarios négatifs bloqués en `G0` et rattachements (`EXIG-EVA-03`, `EXIG-SEC-24`, `EXIG-FIN-04`, `EXIG-AMF-11`, `ASI01`–`ASI10` `[8]`).
  - **Appui vérifié :** `evalops_prr/metamorphic.py`, `tests/test_evalops_prr.py`, `registre/matrice-exig-prr-c40.json`, `SRC-055.txt` (`[8]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-24 (`L115–L120`)** — *Affirmation :* Encadrement des `LLM-as-a-Judge` (`EXIG-EVA-05`) : quatre biais (position, longueur, auto-préférence, piratage/chaîne infidèle), étude sur `13` modèles juges (accord brut et indulgence) et *criteria drift* rapportés dans la littérature des `Tomes 1 § 6.3.2` et `6 § 11.2.4` (hors corpus `L+` fermé de `ch23`), assortis de quatre verrous normatifs (`famille distincte`, permutation, seuil contractuel p. ex. `κ ≥ 0,6`, exécution asynchrone hors chemin critique).
  - **Appui vérifié :** `Corpus/Tome 1` (`L1608–1618`), `Corpus/Tome 6` (`L3553–3562`), `Corpus/Tome 2` (`L5053–5059`, `EXIG-EVA-05`).
  - **Passe initiale :** écart rectifié · **Action :** attribué les biais, les treize modèles juges et le *criteria drift* aux `Tomes 1` et `6` (hors corpus `L+` fermé) et exemplifié `κ ≥ 0,6` selon `EXIG-EVA-05` · **Verdict : supporté**

- **C23-25 (`L122–L127`)** — *Affirmation :* Surveillance continue `E3` mobilisant des plateformes d'outillage documentées au `Tome 1 § 39.1` (`Microsoft Foundry` — `11` évaluateurs dont `5` en préversion au `2 juin 2026` — et `Langfuse`, sans identifiant commun ni portée probante réglementaire directe) et ciblant `3+1` dérives (`Tome 1 § 39.2`, `Tome 6 § 11.3.3`) : `F-23` (dérive modèle/mémoire, risques d'empoisonnement et classifieur/`MMD` du `Tome 6`), `F-52` (dérive outil `MCP` palliant l'absence de champ version/empreinte relevée dans `MCP 2025-11-25` par `JCS`/`SHA-256`, `← Chapitre 22`), `H-12` (glissement d'autonomie, où la préimpression `H-12` relève un déficit d'instrumentation face aux attentes `BSIF E-23`) et `4e` source (auto-apprentissage en ligne interdit sans ré-homologation `E1–E2`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L9211–9257`, `L9319–9335`), `Corpus/Tome 6` (`L3596–3603`, `MMD`), `schemas/SCH-23-02.svg`.
  - **Passe initiale :** écart rectifié · **Action :** aligné la définition exacte de `Microsoft Foundry`, `Langfuse`, `F-23`, `F-52` et `H-12` sur `Tome 1 § 39.1–39.2` et `Tome 6 § 11.3.3` · **Verdict : supporté**

- **C23-26 (`L129–L131`, Figure 2)** — *Affirmation :* La Figure 2 (`SCH-23-02.svg`) représente les quatre relations métamorphiques `FR`/`EN` (Z1), l'encadrement asynchrone des juges à `κ ≥ 0,6` (Z2) et la sentinelle des `3+1` dérives (Z3).
  - **Appui vérifié :** `specs/manifest.json` (`ch23`, `SCH-23-02`), `schemas/rendus/SCH-23-02.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-27 (`L133–L135`)** — *Affirmation :* La recette cible `ADR-031` (`PRR F-15`, acceptée sous réserve de validation empirique au `Tome 3 § 47.20–47.22`) formalise le volant `DSPy`/`MIPROv2` → `Multi-LoRA` (`SLM 3B–8B`) avec mutualisation cible `S-LoRA`/`Punica` (`r = 32`, `∼67` Mo en `FP16` par adaptateur `8B` à `32` couches selon `Tome 3 § 47.20`, sans mesure interne sur élève distillé) et seuil cible de rentabilité mensuel `V_min`.
  - **Appui vérifié :** `Corpus/Tome 3` (`L25835–25963`, `L26024–26035`, `ADR-031`), `registre/matrice-exig-prr-c40.json` (`ADR-031`, `PRR F-15`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement le dispositif de recette cible à valider sans mesure interne sur un élève distillé selon `Tome 3 § 47.20–47.22` · **Verdict : supporté**

- **C23-28 (`L137–L140`)** — *Affirmation :* Les quatre verrous cibles du volant `ADR-031` (`Tome 3 § 47.18–47.20`) prévoient : (1) sélection `SFT` (fourchette illustrative `2 000–15 000` trajectoires sans compensation, réouverture à `14` jours ni violation `Cedar`) + `DPO` (`HOTL`) ; (2) sas `Loi 25` (exclusion `aiTrainingProhibited`, filtre `ASI06`, `200` canaris synthétiques Carlini en paramètre cible) ; (3) porte cible à valider `pass^5 ≥ 99 %` sur `holdout 15 %` ; (4) sentinelle ombre cible à `2 %` sur `agentgateway` et retrait au terme d'un cycle cible de `90–180` jours.
  - **Appui vérifié :** `Corpus/Tome 3` (`L25769–25821`, `L25886`, `L25931–25971`, `L26024–26035`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié l'ensemble des volumes, seuils (`99 %`, `200` canaris, `2 %`, `90–180` jours) comme paramètres et cibles de conception à valider selon `Tome 3 § 47.20` · **Verdict : supporté**

- **C23-29 (`L142–L144`, Figure 3)** — *Affirmation :* La Figure 3 (`SCH-23-03.svg`) illustre la boucle fermée cible `ADR-031` du volant `DSPy` → `Multi-LoRA` (objectif illustratif `10×` plus sobre à valider).
  - **Appui vérifié :** `specs/manifest.json` (`ch23`, `SCH-23-03`), `schemas/SCH-23-03.puml`, `schemas/rendus/SCH-23-03.svg`, `Corpus/Tome 3` (`L25898`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié en légende la boucle fermée cible `ADR-031` et l'objectif illustratif `10×` plus sobre à valider · **Verdict : supporté**

### Section 23.3 — Synthèse architecturale, livrables et portes de contrôle (`L146–L165`)

- **C23-30 (`L148–L150`)** — *Affirmation :* Interfaces amont (`ch02`, `ch21`, `ch22`, `ch25`) et aval (`ch09`, `ch11`, `ch19`, `ch24`, `ch30`, `ch32`), quatre pièces du dossier de mise en production, séparation `Oracle`/`Bâtisseur` et cloisonnement `D08` (`ch22`, `ch24`) dans le respect de `CA-21`.
  - **Appui vérifié :** `specs/manifest.json` (`ch23`, `owned_concepts`), `Compendium/prd.md` (`L4364–4385`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C23-31 (`L152–L159`, Tableau 23.3)** — *Affirmation :* Le `Tableau 23.3` synthétise les quatre livrables d'ingénierie, les exigences et capacités rattachées (`EXIG-EVA-01..06`, `EXIG-GOV-12`, `EXIG-SEC-24`, `EXIG-AMF-11`, `CAP-043`, `CAP-044`, `DEC-010`, `ADR-022`, `ADR-031`, `POR-015`, `PRR O-04`, `PRR F-15`) et les critères exécutables `G0`–`G1` (`mock_mcp_harness.py`, `wilson_bounds.py`, `metamorphic.py`, protocole juges / `3+1` dérives / cible `ADR-031`).
  - **Appui vérifié :** `aq/rapports-g0.json`, `evalops_prr/{mock_mcp_harness.py, wilson_bounds.py, metamorphic.py}`, `registre/matrice-exig-prr-c40.json`.
  - **Passe initiale :** écart rectifié · **Action :** ajouté `PRR F-15` et qualifié `cible à valider` sur les canaris Carlini et `ADR-031` · **Verdict : supporté**

- **C23-32 (`L161–L165`)** — *Affirmation :* Trois invariants exécutables du Chapitre 23 récapitulant (1) herméticité `E1–E2` et `pass^k`, (2) borne unilatérale de Wilson (`300` → `0,8938 % < 1 %`) et suite métamorphique `FR`/`EN` (`G0-EX-CH04-02`), et (3) juges hétérogènes asynchrones (p. ex. `κ ≥ 0,6`), rétrogradation `SLO` à `3` mois et recette cible `DSPy` → `Multi-LoRA`.
  - **Appui vérifié :** `Chapitre 23.md` (`L11–L157`), `aq/rapports-g0.json`, `evalops_prr/`, `Corpus/Tome 2` (`EXIG-EVA-01..06`), `Corpus/Tome 3` (`ADR-031`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié l'exemple contractuel `(p. ex. κ ≥ 0,6)` et la `recette cible DSPy → Multi-LoRA` dans l'invariant 3 · **Verdict : supporté**

- **C23-33 (`REV-04`, `PRD-L3-011/012/013`, `PRD-L4-002`)** — *Affirmation :* Nettoyage des `5` échappements `\$` dans backticks (`40 000 $ US`, `0,90 $ CA`, `0,50 $ CA`), uniformisation `Figure 73`..`Figure 75`, et corrections de schémas `SCH-23-01.puml` (`k ≥ 3 ; k ≥ 5 critique`), `SCH-23-02.svg` (`Pare les biais de position et longueur`) et `SCH-23-03.puml` (distinction seuil volume `V_min`, porte `pass^5 ≥ 99 %` / écart `≤ 1 %` et sentinelle ombre `2 %` / alerte `> 1,5 pt`).
  - **Appui vérifié :** `Corpus/Tome 3` (`ADR-031`, `Extrait 47.10`), `schemas/SCH-23-01.puml`, `schemas/SCH-23-02.svg`, `schemas/SCH-23-03.puml`.
  - **Passe REV-04 :** intégré et vérifié · **Verdict : supporté**
