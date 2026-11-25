# Journal d'ancrage atomique Wyvern G2 — Chapitre 24 (`ch24`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/08 - Partie VIII/Chapitre 24.md` (`4 032` mots de prose `verifie_manuscrit` / `4 311` mots `parser_plan`, plage `[3 726, 4 374]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch24-sources.md` (`[1]`–`[6]` en statut `L+`, `2` exclusions `statut F` sur `gartner.com` et `iso.org`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-{023,068,089,090,110,123}.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json` et trousse `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-3`
- **Passe G2 initiale (supportés)** : 8
- **Rectifications appliquées lors de la passe G2 :** 25
- **Verdict final — supportés :** 33 / 33 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 24.md`

Toutes les formulations divergentes, sur-généralisées ou rattachées à des repérages hors corpus `L+` fermé lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 24.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/08%20-%20Partie%20VIII/Chapitre%2024.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant les `owned_concepts` (`finops-focus-cpo`, `plan-inference-routage-carbone`, `comptabilite-carbone-cap-046-bsif-b15`, `cycle-vie-operationnel-derives-gitops`, `indicateurs-agentops-horizon-tache`), les vedettes propriétaires du glossaire (`Coût par résultat conforme`, `coût complet par résultat conforme`), l'ensemble des renvois `[1]`–`[6]` et le calibrage (`4 032` mots `verifie_manuscrit` / `4 311` mots `parser_plan` dans `[3 726, 4 374]`, `0` erreur `G1 --strict`) :

1. **Routage `SLM` (`Belcak et coll.` `[5]`) vs cibles fictives Boréal (`L13`, `L39`, `Figure 1`, `Tableau 24.1`, `Tableau 24.3`, `L122`) :** remplacement de l'affirmation attribuant `73 %` à `86 %` à l'entreprise et à `[5]` (`SRC-123.txt`) par les fourchettes réellement documentées dans `SRC-123.txt` (`40 %` à `70 %` de requêtes transférables sur *Open Operator* `40 %`, *MetaGPT* `60 %` et *Cradle* `70 %` ; économie estimée de `10×` à `30×` pour un `SLM` de `7` milliards de paramètres face à un `LLM` de `70–175` milliards). Les taux de `73 %` et `86 %` présents dans `SCH-24-01.svg` proviennent du scénario fictif *Groupe Boréal* (`Tome 3 § 44.10, § 47.21`) et sont désormais explicitement qualifiés de cibles illustratives hors preuve empirique.
2. **Spécification `FOCUS v1.4` (`[1]`), colonne héritée `ProviderName`, extensions `x_` et `OTel GenAI` (`[2, 3]`) (`L11`, `L15`, `L29`, `L40`, `L44`, `L46`, `Tableau 24.1`, `L87`, `L90`, `Tableau 24.2`, `L121`) :** rectification de la mention erronée présentant `ProviderName` comme « en transition vers `ServiceProviderName`/`HostProviderName` (`v1.4`/`v1.5`) », alors que `SRC-023.txt` (`L5237`) confirme que `ProviderName` a déjà été retirée en `v1.3` et que seul le schéma strict `G0` `focus_carbon_record.schema.json` la conserve comme champ hérité ; dissociation stricte entre le mécanisme d'extension `x_` de `FOCUS v1.4` `[1]`, les champs `x_energy_kwh`/`x_carbon_gco2e` (`CAP-046` en `G0`) et le calculateur `compute_cpo_and_focus` (`audit_scitt_focus.py`) qui somme `EffectiveCost` et `BilledCost` ; dissociation de `cache_creation` (`v1.41.0` `[2]`) et `cache_write` (`semantic-conventions-genai` `[3]`), retrait du renvoi hors portée `[2, 3]` sur les rabais tarifaires `~90 %` (`1/10` à `1/40`), et alignement de la description d'`OTel GenAI` (`L87`, `Tableau 24.2`) sur une instrumentation unitaire avec `gen_ai.agent.name` sans énumération globale de parc.
3. **Qualification des repérages hors socle `L+` et des seuils propres au cadre (`L5`, `L13`, `L21`, `L23`, `L31`, `L40`–`L42`, `L46`, `L48`, `L67`–`L71`, `L83`) :** rattachement explicite aux repérages antérieurs hors socle `L+` des ordres de grandeur issus des tomes (`> 97 %` de relecture sur banc SEC `Tome 3 § 40.1` ; `~4×` agent unique et `~15×` multi-agents par rapport au clavardage simple ; asymétrie `5×`, écart `35 %` entre segmenteurs, rabais `~90 %` `KV-cache`, `-50 %` lots `24` h et palier `SaaS` à `125 %` dans `Tome 2 § 10.5` ; fourchette haute `700–1 700 TWh` `AIE` `SIG-016` ; modèle `burn rate` `14,4×`/`6×`/`1×` et patrons `Temporal Replayer`/`LangGraph Time Travel` `Tome 6 § 11.3` ; `GitOps` à `3` objets `Tomes 3 & 6` ; grille `AgentOps` `Tome 1 § 40.2` et taux `~93 %` auto-déclaré par un éditeur sur son agent de programmation `Tome 3 § 22.5`). Distinction nette entre les seuils propres au cadre (`70 %` `ADR-023`, `80 %`/`100 %` `EXIG-FIN-04/05`, alerte cache `> 20` pts / `7` j `EXIG-FIN-07`) et entre la revue de valeur à `2` mois (`EXIG-FIN-10`) et le déclassement à `2` trimestres (`POR-016`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C24-01` à `C24-33`)

### Section introductive — Titre, question directrice et cadrage (`L1–L7`)

- **C24-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant le pilotage économique au `Cost-per-Outcome` (`FOCUS v1.4`), les disjoncteurs budgétaires atomiques, le routage frugal à affinité de cache et la comptabilité carbone opposable jusqu'aux indicateurs prudentiels du conseil.
  - **Appui vérifié :** `specs/manifest.json` (`ch24`, `D08`, `SUB_D08_03`, `owned_concepts`), `registre/mindmap-complet.json`.
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C24-02 (`L5`)** — *Affirmation :* En boucle multi-tours non bornée, un banc externe d'extraction documentaire du repérage antérieur (hors `L+`) attribue plus de `97 %` des jetons à la relecture du contexte ; des mesures internes d'éditeur du même repérage chiffrent `~4×` (agent unique) et `~15×` (multi-agents) par rapport à une conversation simple, illustrés par le scénario synthétique à `41 000 \$ CAD` en `11` heures (fil rouge hors preuve empirique).
  - **Appui vérifié :** `Corpus/Tome 3` (`L335`, `L20730–20736`, `L21301`), `Corpus/Tome 1` (`L9508`, `L9535`), `Corpus/Tome 5` (`L1230`, `L1275`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié le banc `> 97 %` de repérage externe hors `L+`, corrigé le comparatif `~4×` / `~15×` face au clavardage simple (au lieu d'un écart entre simple et multi-agents) et explicité le statut hors preuve empirique du scénario synthétique · **Verdict : supporté**

- **C24-03 (`L7`)** — *Affirmation :* Clôture de `D08` au `2 décembre 2026` prolongeant `ch22` (`OTel GenAI`) et `ch23` (`EvalOps`), couvrant `CPO` sur `FOCUS v1.4` `[1]`, enveloppes à coupure nette, routage frugal, portée 3 `BSIF B-15` `[4]`, `GitOps` à trois objets et `AgentOps` vers `BSIF E-23` / `AMF`, sous exclusion `statut F` (`gartner.com`, `iso.org`, `HTTP 403`, `AO-01`) et statut `non-avis` (`AO-05`).
  - **Appui vérifié :** `sources/ch24-sources.md` (`L1–80`), `specs/protocole-mlr-compendium.json` (`AO-01`, `2026-12-02`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

### Section 24.1 — Résumé exécutif (`L9–L15`)

- **C24-04 (`L11`)** — *Affirmation :* Gouvernance économique et `SRE` agentique sous `EXIG-FIN-01`..`10`, `EXIG-ARC-08/09`, `PRI-014`, `CAP-029`, `CAP-034`, `CAP-045/046`, `DEC-006/011`, `ADR-014/015/023` et `PRR O-09/O-12/O-13` : rejet d'`AP-03` au profit du `CPO` en dollars canadiens (`Decimal` exact sans `IEEE-754`, réessais, échecs, évaluation, confinement et `HOTL` selon `EXIG-FIN-01/02`) sur factures normalisées `FOCUS v1.4` `[1]` et grilles révisées trimestriellement.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`CAP-029`, `CAP-034`, `CAP-045`, `CAP-046`, `PRI-014`, `DEC-006`, `DEC-011`, `ADR-014`, `ADR-015`, `ADR-023`, `O-09`, `O-12`, `O-13`), `registre/glossaire-termes.json` (`CPO`), `Corpus/Tome 2` (`L5091–5101`), `SRC-023.txt` `[1]`, `audit_scitt_focus.py` (`L244–282`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié la formule normative `CPO` (`EXIG-FIN-01/02`) des factures normalisées `FOCUS v1.4` `[1]` · **Verdict : supporté**

- **C24-05 (`L13`)** — *Affirmation :* Routage frugal `E2` derrière alias logiques : d'après Belcak et collaborateurs `[5]`, des `SLM` absorbent `40 %` à `70 %` des requêtes sur leurs trois cas d'étude avec un gain estimé de `10×` à `30×` (`7B` contre `70–175B`), les taux `73 %` à `86 %` restant des cibles illustratives Boréal hors preuve empirique ; `KV-cache` (`~90 %` selon grilles du repérage antérieur), lots asynchrones (`-50 %` sur `24` h selon ce repérage) et disjoncteurs du cadre (`70 %` `ADR-023`, `80 %`/`100 %` `EXIG-FIN-04/05`, hors compensations `Saga`).
  - **Appui vérifié :** `SRC-123.txt` (`L194–195`, `L791`, `L815`, `L836`), `Corpus/Tome 2` (`L5079`, `L5141–5150`, `L5181`), `Corpus/Tome 3` (`L21337`, `L23310`, `L26019`), `Corpus/Tome 5` (`L1275`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé `73 %` à `86 %` attribués à `[5]` par `40 %` à `70 %` (`[5]`), qualifié `73 %–86 %` de cibles fictives Boréal et rattaché `~90 %`/`-50 %` et `70/80/100 %` à leurs sources exactes · **Verdict : supporté**

- **C24-06 (`L15`)** — *Affirmation :* Jointure `gen_ai.usage.*` `[2, 3]` + `ca.entreprise.cost_center` ↔ `FOCUS v1.4` `[1]` étendu par `x_` (`x_energy_kwh`, `x_carbon_gco2e`, `CAP-046`), trajectoire `Showback` (`POR-004`) → `Chargeback` (`POR-009`), revue à `2` mois (`EXIG-FIN-10`) et déclassement à `2` trimestres (`POR-016`), portée 3 `BSIF B-15` fin `2028` `[4]`, `GitOps` à trois objets et `AgentOps` vers `1er mai 2027` (`BSIF E-23` et `AMF`).
  - **Appui vérifié :** `SRC-023.txt` (`L150`, `L954`), `SRC-089.txt` (`L62–66`), `SRC-090.txt` (`L83–93`), `SRC-110.txt` (`L482–545`), `registre/matrice-exig-prr-c40.json` (`POR-004`, `POR-009`, `POR-016`, `CAP-046`), `registre/ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`, `2028-12-31-BSIF-B15-PORTEE3`).
  - **Passe initiale :** écart rectifié · **Action :** explicité le mécanisme `x_` de `FOCUS` et distingué `EXIG-FIN-10` (`2` mois, revue) de `POR-016` (`2` trimestres, déclassement) · **Verdict : supporté**

### Section 24.2.1 — Pilotage au `CPO`, routage frugal et comptabilité carbone (`L19–L61`, Figure 1, Tableau 24.1)

- **C24-07 (`L21`)** — *Affirmation :* En boucle `ReAct` de `T` étapes sans compaction ni cache, la consommation croît en \(T \times P + \Delta \times T(T - 1) / 2\) (\(O(T^2)\)), avec `> 97 %` de relecture sur le banc SEC du repérage antérieur (hors `L+`), ainsi que des repères fournisseurs hors `L+` : asymétrie sortie/entrée jusqu'à `5×`, écart jusqu'à `35 %` entre segmenteurs d'un même fournisseur, et consommation `~4×` (agent unique) / `~15×` (multi-agents) face au clavardage.
  - **Appui vérifié :** `Corpus/Tome 2` (`L5077`), `Corpus/Tome 3` (`L20732–20736`), `Corpus/Tome 5` (`L1230`, `L1270`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié les valeurs `> 97 %`, `5×`, `35 %`, `~4×` et `~15×` comme repères externes hors socle `L+` et corrigé l'échelle `~4×`/`~15×` face au clavardage · **Verdict : supporté**

- **C24-08 (`L23`)** — *Affirmation :* Coût réel doublé ou triplé par les échecs/réparations d'un modèle bon marché ; conversion et plafonnement des crédits `SaaS` (`EXIG-FIN-03`) avec alerte avant des paliers de désactivation tel `125 %` de capacité prépayée observé sur une offre `SaaS` au repérage antérieur (hors `L+`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L5085`, `L5107`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `125 %` comme exemple observé sur une offre `SaaS` au repérage antérieur hors `L+` · **Verdict : supporté**

- **C24-09 (`L25–L27`)** — *Affirmation :* Formule du `CPO` (`PRI-014`, `CAP-045`, `DEC-011`, `EXIG-FIN-01`, `EXIG-FIN-02`) à cinq postes au numérateur (incluant plans de sortie `BSIF B-10` `[6]`) divisés par `compliant_outcomes ≥ 1`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L5187`), `Corpus/Tome 5` (`L1234`), `SRC-068.txt` (`§ 2.3.5`, `L443–461`), `audit_scitt_focus.py` (`L257–260`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C24-10 (`L29`)** — *Affirmation :* Calcul financier exclusif en `Decimal` exact rejetant `IEEE-754` par `TypeError`, vérifié en `G0` par `compute_cpo_and_focus` (`authz_pqc_audit/audit_scitt_focus.py`) sur les champs `EffectiveCost` et `BilledCost` `FOCUS` `[1]`, avec révision au moins trimestrielle des grilles tarifaires et taux `CAD` (`EXIG-FIN-02`).
  - **Appui vérifié :** `audit_scitt_focus.py` (`L244–282`), `aq/rapports-g0.json` (`L43`), `SRC-023.txt` (`[1]`), `Corpus/Tome 2` (`L5099`).
  - **Passe initiale :** écart rectifié · **Action :** précisé que `compute_cpo_and_focus` opère sur `EffectiveCost` et `BilledCost` des enregistrements `FOCUS` `[1]` · **Verdict : supporté**

- **C24-11 (`L31–L35`)** — *Affirmation :* La passerelle détient seule côté serveur l'état atomique des enveloppes par `task_id` (`EXIG-FIN-04`) et des plafonds mensuels par agent (`EXIG-FIN-05`), avec réservation du coût maximal avant appel sans réinitialisation à la délégation, et trois seuils propres au cadre (`70 %` `SLM` `ADR-023`, `80 %` alerte, `100 %` refus « budget épuisé » préservant le canal isolé `Saga`, `ch15`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L5117`, `L5141–5150`), `Corpus/Tome 3` (`L21337`).
  - **Passe initiale :** écart rectifié · **Action :** explicité que `70 %`, `80 %` et `100 %` sont des seuils propres au cadre (`EXIG-FIN-04`, `EXIG-FIN-05`, `ADR-023`) · **Verdict : supporté**

- **C24-12 (`L37–L39`)** — *Affirmation :* Plan d'inférence derrière alias logiques (`CAP-029`, `DEC-006`, `EXIG-ARC-08/09`, `EXIG-FIN-06`) : selon Belcak et collaborateurs (`arXiv:2506.02153`, juin 2025 `[5]`), leurs trois études de cas estiment `40 %` à `70 %` de requêtes transférables (`40 %` *Open Operator*, `60 %` *MetaGPT*, `70 %` *Cradle*) avec économie de calcul, latence et énergie de `10×` à `30×` (`7B` vs `70–175B`), les taux `73 %`–`86 %` (Figure 1) étant des cibles illustratives Boréal hors preuve empirique ; renforcement local par distillation `Multi-LoRA` `pass^5` (`CAP-034`, `SIG-015/016`, `ch23`).
  - **Appui vérifié :** `SRC-123.txt` (`L1`, `L54`, `L194–195`, `L791`, `L815`, `L836`), `registre/faits-empiriques.json` (`FACT-SLM-AGENTIC`), `registre/matrice-exig-prr-c40.json` (`CAP-029`, `CAP-034`, `SIG-015`, `SIG-016`), `Corpus/Tome 3` (`L23310`, `L26019`).
  - **Passe initiale :** écart rectifié · **Action :** réancré strictement les pourcentages sur `SRC-123.txt` (`40–70 %`) et qualifié `73–86 %` de cibles illustratives Boréal hors preuve empirique · **Verdict : supporté**

- **C24-13 (`L40`)** — *Affirmation :* Préfixe ordonné du plus stable au plus variable (`EXIG-FIN-07`) pour le `KV-cache`, abattement jusqu'à `~90 %` (`1/10` à `1/40` du tarif d'entrée) d'après les grilles fournisseurs du repérage antérieur (`Tome 2 § 10.5`, hors `L+`), mesuré via `gen_ai.usage.cache_read.input_tokens` `[2, 3]`, ordonnancement vers réplique chaude (`TTFT`) et analyse à `> 20` points de baisse sur `7` jours (`EXIG-FIN-07`).
  - **Appui vérifié :** `SRC-089.txt` (`L63`), `SRC-090.txt` (`L83`), `Corpus/Tome 2` (`L5079`, `L5157`, `L5171`).
  - **Passe initiale :** écart rectifié · **Action :** retiré le renvoi `[2, 3]` des multiplicateurs tarifaires `~90 %` (`1/10`–`1/40`), rattachés au repérage fournisseur, et limité `[2, 3]` à `gen_ai.usage.cache_read.input_tokens` · **Verdict : supporté**

- **C24-14 (`L41`)** — *Affirmation :* Cache sémantique vectoriel borné sous contrôle d'accès `ACL` et durée de vie courte, sans taux d'économie préjugé sans mesure locale.
  - **Appui vérifié :** `Corpus/Tome 2` (`L5083`), `Corpus/Tome 1` (`L9532`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté la réserve méthodologique excluant tout taux d'économie sans mesure locale (`Tome 2 § 10.5`) · **Verdict : supporté**

- **C24-15 (`L42`)** — *Affirmation :* Lots asynchrones différables jusqu'à `24` heures offrant `-50 %` selon les grilles fournisseurs du repérage antérieur (`EXIG-FIN-08`), et arbitrage capacité `PTU` avec débordement *spillover* vers `PAYG`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L5079`, `L5179–5181`), `Corpus/Tome 6` (`L4083`, `L4154`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement `-50 %` aux grilles fournisseurs du repérage antérieur (`Tome 2 § 10.5`) · **Verdict : supporté**

- **C24-16 (`L44`)** — *Affirmation :* Appariement `OpenTelemetry GenAI` (`cache_creation` en `v1.41.0` `[2]` puis `cache_write` dans `semantic-conventions-genai` `[3]`, `ca.entreprise.cost_center` `EXIG-FIN-09`) et `FOCUS v1.4` (`4 juin 2026` `[1]`) : dix colonnes centrales normalisées, `ServiceProviderName` et `HostProviderName` remplaçant `ProviderName` retirée dès la `v1.3` `[1]`, et champ hérité `ProviderName` maintenu dans `focus_carbon_record.schema.json` (`G0`).
  - **Appui vérifié :** `SRC-023.txt` (`L4`, `L368`, `L1402`, `L5237`), `SRC-089.txt` (`L62–66`), `SRC-090.txt` (`L83–93`), `focus_carbon_record.schema.json` (`L7–27`), `registre/specifications-lplus.json` (`SPEC-FOCUS-V1-4`), `registre/faits-empiriques.json` (`FACT-OTEL-GENAI-ATTRS`), `Corpus/Tome 8` (`L817`).
  - **Passe initiale :** écart rectifié · **Action :** rectifié le statut de `ProviderName` (retirée en `v1.3` dans `FOCUS` `[1]` et héritée uniquement dans `focus_carbon_record.schema.json` `G0`) et distingué `cache_creation` `[2]` de `cache_write` `[3]` · **Verdict : supporté**

- **C24-17 (`L46`)** — *Affirmation :* Demande électrique des centres de données (`700` à `1 700 TWh` projetés pour `2035` par l'AIE, reprise sous `SIG-016` hors `L+`) ; `BSIF B-15` (`7 mars 2025` `[4]`, `ANC-106`) imposant la divulgation des émissions absolues brutes de portée 3 pour l'exercice `2028` (`fin 2028`) ; extension `x_` de `FOCUS v1.4` `[1]` portant `x_energy_kwh` et `x_carbon_gco2e` (`CAP-046`, `focus_carbon_record.schema.json` en `G0`) ; différenciation réseau (hydroélectricité Québec vs thermique) et réserve sur l'opacité partielle des facteurs portée 3 d'inférence (`SIG-016`).
  - **Appui vérifié :** `SRC-110.txt` (`L13–15`, `L484–545`), `SRC-023.txt` (`L150`, `L954`), `focus_carbon_record.schema.json` (`L11`, `L25–26`), `registre/matrice-exig-prr-c40.json` (`SIG-016`, `CAP-046`), `registre/ancres-chronologiques.json` (`2028-12-31-BSIF-B15-PORTEE3`), `Corpus/Tome 3` (`L20756`), `Corpus/Tome 5` (`L1275`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `700–1 700 TWh` comme fourchette haute AIE hors `L+`, rattaché `x_energy_kwh`/`x_carbon_gco2e` au mécanisme `x_` de `[1]` + `CAP-046` `G0`, et ajouté la réserve sur l'opacité des facteurs d'inférence · **Verdict : supporté**

- **C24-18 (`L48`)** — *Affirmation :* Trajectoire `Showback` (`POR-004`) → `Chargeback` (`POR-009`), revue de valeur après `2` mois civils consécutifs hors cible (`EXIG-FIN-10`) et déclassement ou reconception après `2` trimestres déficitaires (`POR-016`), articulation `BSIF B-10` `[6]`, `Loi 25 art. 12.1` (`22 septembre 2023`) et jalons `15 mars 2027`, `15 mars 2029` et `2030–2035`.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`POR-004`, `POR-009`, `POR-016`), `Corpus/Tome 2` (`L5203`), `SRC-068.txt` (`L199`, `L417–461`), `registre/ancres-chronologiques.json` (`2026-LOI25-ART12-1`, `2027-03-15-TLS-100J`, `2029-03-15-TLS-47J`, `2030-2035-G7-PQC-FINANCE`).
  - **Passe initiale :** écart rectifié · **Action :** distingué la revue de valeur à `2` mois (`EXIG-FIN-10`) du déclassement/reconception à `2` trimestres (`POR-016`) · **Verdict : supporté**

- **C24-19 (`L50–L52`, Figure 1)** — *Affirmation :* Concordance de `SCH-24-01.svg` opposant le tarif au jeton (`Z1`) au plan frugal `KV-cache`/lots/cascade `SLM` illustrée à `73–86 %` en scénario cible Boréal (`Z2`) et au `CPO` `Decimal` sur `FOCUS v1.4` avec seuils `70 %`/`80 %`/`100 %` (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch24`, `SCH-24-01`), `Compendium/ouvrage/schemas/SCH-24-01.svg` (`L1–94`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié en légende les taux `73–86 %` affichés dans `SCH-24-01` d'illustration en scénario cible Boréal · **Verdict : supporté**

- **C24-20 (`L54–L61`, Tableau 24.1)** — *Affirmation :* Synthèse tabulaire des `4` leviers `FinOps` / carbone : calculateur `Decimal` (`10` col. `FOCUS` + `ProviderName` `G0` + `x_energy_kwh`/`x_carbon_gco2e` `[1, 4]`), enveloppes `70/80/100 %`, cascade `SLM` `40–70 %` (`10×–30×` `7B` vs `70–175B` `[5]` ; cible Boréal `73–86 %`) + `cache ~90 %` / `lots -50 %` (repérage hors `L+`), et revue `2` mois / déclassement `2` trimestres (`BSIF B-10` `[6]`).
  - **Appui vérifié :** `SRC-023.txt` `[1]`, `SRC-089.txt` `[2]`, `SRC-090.txt` `[3]`, `SRC-110.txt` `[4]`, `SRC-123.txt` `[5]`, `SRC-068.txt` `[6]`, `focus_carbon_record.schema.json`.
  - **Passe initiale :** écart rectifié · **Action :** aligné les cellules sur `ProviderName` héritée `G0`, `SLM` `40–70 %` `[5]`, le statut hors `L+` de `~90 %`/`-50 %` et la distinction `2` mois / `2` trimestres · **Verdict : supporté**

### Section 24.2.2 — `SRE` agentique, `GitOps` à trois objets et grille `AgentOps` (`L63–L105`, Figures 2–3, Tableau 24.2)

- **C24-21 (`L65`)** — *Affirmation :* Couplage des `SLI` d'infrastructure (`TTFT`, `TPOT`, erreurs `429`/`5xx`, durée) et des `SLI` comportementaux (conformité `JSON Schema` au premier essai, validité d'outils, garde-fous).
  - **Appui vérifié :** `Corpus/Tome 6` (`L3580–3581`), `Corpus/Tome 2` (`Tableau 42`, `L5010–5018`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C24-22 (`L67`)** — *Affirmation :* Sur un `SLO` mensuel à `99,9 %` (`0,1 %` budget d'erreur), alertes multi-fenêtres sur vitesse de consommation (`14,4×` sur `5 min`/`1 h` soit `2 %`, `6×` sur `30 min`/`6 h` soit `5 %`, `1×` sur `6 h`/`3 j` soit `10 %`) selon le modèle du *Google SRE Workbook* repris au `Tome 6 § 11.3.2` (hors socle `L+`).
  - **Appui vérifié :** `Corpus/Tome 6` (`L3585–3592`).
  - **Passe initiale :** écart rectifié · **Action :** attribué explicitement le barème multi-fenêtres au modèle *Google SRE Workbook* repris au `Tome 6 § 11.3.2` hors socle `L+` · **Verdict : supporté**

- **C24-23 (`L69`)** — *Affirmation :* Séparation stricte de deux patrons de référence du `Tome 6 § 11.3.4` (hors `L+`) : rejeu déterministe à coût nul (`Temporal Replayer`) et bifurcation cognitive (`LangGraph Time Travel`) confinée en `MockMcpServer` (`ch23`) pour prévenir toute ré-écriture sur `P2`/`P3` ou altération d'audit.
  - **Appui vérifié :** `Corpus/Tome 6` (`L3631–3637`), `Tome 8` (`MockMcpServer`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `Temporal Replayer` et `LangGraph Time Travel` de patrons de référence du `Tome 6 § 11.3.4` hors socle `L+` · **Verdict : supporté**

- **C24-24 (`L71–L77`)** — *Affirmation :* Modèle **GitOps à trois objets indissociables** (manifeste + `NHI` + invites, schémas `MCP` `SHA-256`, règles `OPA`/`Cedar`) versionnés sous `SemVer+Intent` (zéro `latest`), synthétisé des Tomes 3 et 6 (hors `L+` hors `BSIF B-10` `[6]`), avec portes `E1–E2`, attestation `SLSA`/`Sigstore`, promotion fantôme → canari avec épinglage `Temporal`, retour arrière atomique sur seuil de dérive et bascule `BSIF B-10` `[6]`.
  - **Appui vérifié :** `Corpus/Tome 3` (`L18703–18775`), `Corpus/Tome 6` (`L4166–4250`), `SRC-068.txt` (`§ 2.3.5`, `L443–461`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié le patron `GitOps` à trois objets et `SemVer+Intent` de synthèse des Tomes 3 et 6 hors `L+` (hors `BSIF B-10` `[6]`) · **Verdict : supporté**

- **C24-25 (`L79–L81`, Figure 2)** — *Affirmation :* Concordance de `SCH-24-02.svg` (`SCH-24-02.puml`) illustrant le triplet indissociable (`Z1`), les portes `E1–E2` / `SLSA` / canari `Temporal` (`Z2`) et le retour arrière atomique sur seuil (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch24`, `SCH-24-02`), `Compendium/ouvrage/schemas/SCH-24-02.puml` (`L1–87`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C24-26 (`L83`)** — *Affirmation :* Liaison vers `BSIF E-23` (`1er mai 2027`) et `AMF` (sous réserve `statut F`, `ch25`) par une **grille minimale AgentOps à quatre familles** (construction d'auteur du `Tome 1 § 40.2`), intégrant temps d'examen et taux d'approbation sans modification (`HOTL`) face au taux d'acceptation de `~93 %` rapporté par un éditeur sur son agent de programmation hors `L+` (`ch33`).
  - **Appui vérifié :** `registre/ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`), `Corpus/Tome 1` (`L9446–9460`), `Corpus/Tome 3` (`L12175`, `L12181`), `Corpus/Tome 5` (`L1275`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié la grille de construction d'auteur (`Tome 1 § 40.2`) et rattaché `~93 %` au chiffre auto-déclaré d'un éditeur sur son agent de programmation hors `L+` · **Verdict : supporté**

- **C24-27 (`L85–L90`)** — *Affirmation :* Quatre prérequis instrumentaux à construire dans le noyau possédé : (1) dénominateur du parc (`CAP-047`) face à `OTel GenAI` `[2, 3]` unitaire avec `gen_ai.agent.name` sans énumération globale ; (2) clé de jointure `ca.entreprise.*` (`lacune 21`, `ch22`) absente d'`OTel` `[2, 3]` ; (3) délai de révocation mesuré via `SSF`/`CAEP` + `PEP` (`ch17`, `ch21`) ; (4) horodatage par l'événement `gen_ai.evaluation.result` (`Development`, `EXIG-EVA-04`).
  - **Appui vérifié :** `SRC-089.txt` (`L19–28`), `SRC-090.txt` (`L11–21`), `Corpus/Tome 1` (`L9393–9413`, `L9452–9459`), `Corpus/Tome 2` (`L5008`, `L5049`), `Corpus/Tome 8` (`L728–730`).
  - **Passe initiale :** écart rectifié · **Action :** aligné le point 1 sur le périmètre exact de `SRC-089/090` (opérations unitaires avec `gen_ai.agent.name` sans énumération de parc), ajouté `[2, 3]` aux points 1–2 et précisé le statut `Development` et l'ancrage `EXIG-EVA-04` de `gen_ai.evaluation.result` · **Verdict : supporté**

- **C24-28 (`L92`)** — *Affirmation :* Trois mouvements coordonnés vers le `1er mai 2027` : inventaire du parc et des dépendances (`BSIF B-10` `[6]`, `E-23`), cotation de matérialité avec bornes/budgets, et surveillance continue déclenchant ré-étalonnage ou rétrogradation d'autonomie avec propriétaire nommé et délai de remédiation.
  - **Appui vérifié :** `SRC-068.txt` (`L199`, `L217–249`), `Corpus/Tome 2` (`L5065`), `Corpus/Tome 1` (`L9437–9457`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C24-29 (`L94–L96`, Figure 3)** — *Affirmation :* Concordance de `SCH-24-03.png` (`SCH-24-03.mmd`) reliant les `4` familles `AgentOps` (`Z1`), les `4` lacunes comblées (`Z2`) et les `KPI` prudentiels `BSIF E-23` et `AMF` (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch24`, `SCH-24-03`), `Compendium/ouvrage/schemas/SCH-24-03.mmd` (`L1–30`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C24-30 (`L98–L105`, Tableau 24.2)** — *Affirmation :* Tableau de correspondance des `4` familles `AgentOps` vers les `KPI` prudentiels `BSIF E-23`/`AMF` (`1er mai 2027`) : inventaire et `SemVer+Intent` (`OTel` unitaire `[2, 3]` + registre), traçabilité (`4` clés `ca.entreprise.*`, `TCR`/`TER`/`pass^k`/dérives `3+1`), `HOTL`/`CIBA`/`SSF`/`CAEP`, et économie unitaire/carbone (`CPO` `FOCUS`, `cost_center`, `B-10` `[6]`, portée 3 `B-15` `[4]`).
  - **Appui vérifié :** `SRC-023.txt` `[1]`, `SRC-089.txt` `[2]`, `SRC-090.txt` `[3]`, `SRC-110.txt` `[4]`, `SRC-068.txt` `[6]`, `Corpus/Tome 1` (`L9450–9459`), `Corpus/Tome 5` (`L1220`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé `OTel à faible cardinalité` par `OTel unitaire sans inventaire de parc [2, 3]` en ligne 1 · **Verdict : supporté**

### Section 24.3 — Synthèse, livrables et invariants (`L107–L123`, Tableau 24.3)

- **C24-31 (`L109`)** — *Affirmation :* Interfaces amont (`ch04`, `ch09`, `ch10`, `ch13`, `ch15`, `ch20`, `ch21`, `ch22`, `ch23`) et aval (`ch25`, `ch26`, `ch27`, `ch30`, `ch32`) conformes à la partition `CA-21`.
  - **Appui vérifié :** `specs/manifest.json` (`owned_concepts` et découpage `ch01`–`ch36`), `verifie_manuscrit.py` (`CA-21`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C24-32 (`L111–L117`, Tableau 24.3)** — *Affirmation :* Trois livrables d'ingénierie et critères `G0`–`G1` : calculateur `CPO` `Decimal` (`compute_cpo_and_focus`, `focus_carbon_record.schema.json`, `[1, 4]`), passerelle à alias logiques (`SLM` `40–70 %` `[5]` ; cible Boréal `73–86 %`, préfixe `KV-cache` `[2, 3]`, enveloppes `70/80/100 %` hors `Saga`), et dépôt `GitOps` à `3` objets + matrice `AgentOps → E-23/AMF` `[4, 6]`.
  - **Appui vérifié :** `audit_scitt_focus.py`, `focus_carbon_record.schema.json`, `aq/rapports-g0.json`, `SRC-023.txt` `[1]`, `SRC-089/090.txt` `[2, 3]`, `SRC-110.txt` `[4]`, `SRC-123.txt` `[5]`, `SRC-068.txt` `[6]`.
  - **Passe initiale :** écart rectifié · **Action :** aligné la ligne 2 sur `SLM` `40–70 %` `[5]` + cible Boréal `73–86 %` et précisé le renvoi `OTel` `[2, 3]` · **Verdict : supporté**

- **C24-33 (`L119–L123`, Encadré `Trois invariants exécutables`)** — *Affirmation :* Trois invariants exécutables du Chapitre 24 : (1) pilotage `CPO` `Decimal` sur `FOCUS v1.4` `[1]` + traces `OTel` `[2, 3]` (clé `ca.entreprise.cost_center`) + colonnes `x_` `[1]` (`x_energy_kwh`, `x_carbon_gco2e` en `G0`) pour `BSIF B-15` fin `2028` `[4]` ; (2) passerelle d'alias logiques en `E2` (`40–70 %`, `10×–30×` `7B` vs `70–175B` `[5]`), `KV-cache` `[2, 3]`, lots `-50 %` (repérage fournisseur) et seuils du cadre `70/80/100 %` hors `Saga` ; (3) triplet `GitOps` `SemVer+Intent`, `4` familles `AgentOps` (`HOTL`) vers `BSIF E-23`/`AMF` avec réversibilité `BSIF B-10` `[6]`, revue à `2` mois (`EXIG-FIN-10`) et déclassement à `2` trimestres (`POR-016`).
  - **Appui vérifié :** `SRC-023.txt` `[1]`, `SRC-089/090.txt` `[2, 3]`, `SRC-110.txt` `[4]`, `SRC-123.txt` `[5]`, `SRC-068.txt` `[6]`, `registre/matrice-exig-prr-c40.json`, `audit_scitt_focus.py`.
  - **Passe initiale :** écart rectifié · **Action :** ajouté les renvois `[1]`–`[6]` dans les trois invariants, réancré le levier `SLM` sur `[5]` (`40–70 %`, `10×–30×` `7B` vs `70–175B`), scindé l'invariant 2 (`CA-05`), distingué la revue à `2` mois du déclassement à `2` trimestres, et en recollation `G3` (`seed=20270901`), dissocié `ca.entreprise.cost_center` des conventions `[2, 3]` et `x_energy_kwh`/`x_carbon_gco2e` (`G0`) du mécanisme `x_` `[1]` · **Verdict : supporté**
