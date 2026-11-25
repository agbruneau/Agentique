# Audit de fidélité au PRD et de qualité éditoriale — Lot 1 (`REV-03`)

- **Auditeur** : `audit-prd-lot1` (mode audit indépendant, lecture seule sur le manuscrit et les schémas)
- **Référentiel maître** : `Compendium/prd.md` (Sommaire exécutif global, Parties I à III, Annexe C et Annexe D)
- **Périmètre audité** : `10` unités narratives (`00 - Liminaire`, `CH-01` à `CH-09`) et `33` schémas sources/rendus (`SCH-00-01` à `SCH-09-04`, incluant `SCH-06-04` et `SCH-09-04`)
- **Bilan quantitatif** : **`21` constats** — **`3` BLOQUANTS**, **`8` MAJEURS**, **`10` MINEURS**
  - Par axe : `couverture_prd` (`4`), `coherence` (`6`), `edition` (`8`), `schemas` (`3`)

---

## 1. Synthèse exécutive

Le socle doctrinal du Lot 1 est globalement solide et fidèle à l'esprit du référentiel : les grandes invariants (`80/20`, `L0–L4`/`N0–N4`, `DISC-01` à `DISC-05`, fermeture `DIV-02`, `MCP 2026-07-28`, `A2A v1.0.1`, `AP2` au statut `Surveiller`, passerelle `PEP` à neuf contrôles, partition `8/7/16` des `31 ADR` vers `12 DEC`, extraits `G0` vérifiés par `SHA-256`, citations bibliographiques `100 %` résolues et fins de ligne `LF` conformes) sont traités avec rigueur.

En revanche, l'audit met au jour **trois anomalies bloquantes** et **huit défauts majeurs** qui compromettent soit l'exactitude normative, soit la cohérence entre la prose et les schémas, soit le rendu typographique final :

1. **Inversion logique dans l'arbre décisionnel `SCH-03-01.mmd` (`PRD-L1-001`, BLOQUANT)** : un flux non critique muni d'un plan de contrôle et d'une sortie `B-10` ouverts est routé vers `ASSEMBLER` au lieu d'`ACHETER`, tandis qu'un plan fermé mène vers `Acheter SaaS confiné`.
2. **Collision d'identifiant normatif sur `CAP-033` (`PRD-L1-002`, BLOQUANT)** : `00 - Liminaire.md` (Tableau 0.2, L84) attribue `CAP-033` au cycle de vie `PKI` (`TLS 100 j → 47 j`), alors que `Chapitre 06.md` (L58, Tableau 6.1) et `prd.md` Annexe D (L7111, L7118) définissent `CAP-033` comme l'inférence confidentielle en enclave `TEE` et rattachent l'agilité cryptographique / `PKI` / `PQC` à `CAP-040`.
3. **Six formules LaTeX enfermées dans des backticks (`PRD-L1-003`, BLOQUANT)** dans `Chapitre 06.md` (`L17`, `L152`, `L158`), empêchant leur rendu mathématique sur les seuils éliminatoires de `S_ready`.
4. **Ruptures systématiques prose ↔ schémas sur les chiffres retirés ou recalibrés (`PRD-L1-004` à `PRD-L1-007`, MAJEURS)** : lors du durcissement probatoire `L+` des chapitres `CH-01`, `CH-02`, `CH-03` et `CH-05`, plusieurs chiffres du PRD (`160` études `W3.2` / `AACODS 9,97/12` / `Nubank KDD 2026` / `82:1` / `415 → 945 TWh`, `METR v1.1 17,4 h / 3,1 h`, `MAST 32,4 %`, dispersion marché `1 à 59`, `93 %` d'approbation réflexe) ont été supprimés ou remplacés dans la prose, mais **conservés tels quels dans les schémas `SCH-01-02`, `SCH-01-03`, `SCH-02-01`, `SCH-02-02`, `SCH-02-03`, `SCH-03-01`, `SCH-03-02` et `SCH-05-03`**.
5. **Défauts transversaux de rendu et de charte (`PRD-L1-008`, `PRD-L1-009`, `PRD-L1-011`, MAJEURS)** : numérotation globale des figures (`Figure 1` à `Figure 13`) rompue à partir de `CH-04` (retour à `Figure 1` à chaque chapitre), `55` occurrences de `\$` échappés à l'intérieur de backticks (`00 - Liminaire`, `CH-02`, `CH-03`, `CH-04`), et backticks Markdown littéraux rendus dans les titres SVG de `SCH-04-01`, `SCH-05-01` et `SCH-06-01`.

---

## 2. Tableau de couverture par unité du Lot 1

| Unité | Thèmes PRD | Schémas | Statut fidélité PRD | Constats associés |
|---|---|---|---|---|
| `00-liminaire` | Sommaire §1–§5 | `SCH-00-01..04` (`4`) | Partiel (`CAP-033`, omissions §0.2/§0.4/§0.5, placement `SCH-00-04`) | `PRD-L1-002` (B), `PRD-L1-009` (M), `PRD-L1-010` (M), `PRD-L1-017` (m) |
| `ch01` | `8/8` (2 familles) | `SCH-01-01..03` (`3`) | Écart majeur prose ↔ schémas (`W3.2` vs `135 L+`, `Nubank` absent) | `PRD-L1-004` (M), `PRD-L1-012` (m), `PRD-L1-015` (m) |
| `ch02` | `4/4` (2 familles) | `SCH-02-01..03` (`3`) | Écart majeur prose ↔ schémas (`METR`, `32,3 %`/`32,4 %`, `HAL`) | `PRD-L1-005` (M), `PRD-L1-009` (M), `PRD-L1-013` (m), `PRD-L1-015` (m) |
| `ch03` | `8/8` (2 familles) | `SCH-03-01..03` (`3`) | Erreur logique `SCH-03-01`, écart `1 à 59` et `82:1` | `PRD-L1-001` (B), `PRD-L1-006` (M), `PRD-L1-009` (M), `PRD-L1-014` (m), `PRD-L1-015` (m) |
| `ch04` | `7/7` (2 familles) | `SCH-04-01..03` (`3`) | Très bonne couverture ; numérotation figures, backticks SVG, `2_input` | `PRD-L1-008` (M), `PRD-L1-009` (M), `PRD-L1-011` (M), `PRD-L1-015` (m), `PRD-L1-016` (m), `PRD-L1-021` (m) |
| `ch05` | `4/4` (2 familles) | `SCH-05-01..03` (`3`) | Bonne couverture ; écart `93 %` sur `SCH-05-03`, italique cassé | `PRD-L1-007` (M), `PRD-L1-008` (M), `PRD-L1-011` (M), `PRD-L1-015` (m), `PRD-L1-016` (m), `PRD-L1-018` (m), `PRD-L1-021` (m) |
| `ch06` | `12/12` (2 familles) | `SCH-06-01..04` (`4`) | Excellente couverture ; `6` LaTeX dans backticks, backticks SVG | `PRD-L1-003` (B), `PRD-L1-008` (M), `PRD-L1-011` (M), `PRD-L1-015` (m), `PRD-L1-016` (m), `PRD-L1-021` (m) |
| `ch07` | `6/6` (2 familles) | `SCH-07-01..03` (`3`) | Très bonne couverture ; fuites atelier, redite `EXIG-MCP-18`, `ne DOIT` | `PRD-L1-008` (M), `PRD-L1-016` (m), `PRD-L1-017` (m), `PRD-L1-018` (m), `PRD-L1-019` (m) |
| `ch08` | `8/8` (2 familles) | `SCH-08-01..03` (`3`) | Très bonne couverture ; `chaîne de invites`, redite SSRF, fuites | `PRD-L1-008` (M), `PRD-L1-016` (m), `PRD-L1-017` (m), `PRD-L1-018` (m), `PRD-L1-019` (m) |
| `ch09` | `11/11` (2 familles) | `SCH-09-01..04` (`4`) | Très bonne couverture ; écarts `SCH-09-01/03/04`, `ISO 11354-1` | `PRD-L1-008` (M), `PRD-L1-016` (m), `PRD-L1-018` (m), `PRD-L1-020` (m) |

---

## 3. Constats détaillés

### Constats BLOQUANTS (`3`)

#### `PRD-L1-001` — Inversion logique de l'arbre décisionnel `SCH-03-01.mmd` (`Acheter` / `Assembler` / `Construire`)
- **Unité** : `ch03` · **Axe** : `schemas` · **Fichier** : `Compendium/ouvrage/schemas/SCH-03-01.mmd` (et rendu `SCH-03-01.png`)
- **Constat** : Dans `SCH-03-01.mmd`, lorsque `N3` (*Portes 1–2 : Flux critique et transversal ?*) répond `Non`, l'arbre évalue `N4` (*Porte 3 : Plan de contrôle et sortie B-10 ouverts ?*), puis route **`Fermé`** vers `N5` (*Acheter SaaS confiné*) et **`Ouvert`** vers `N7` (*ASSEMBLER*). Cette topologie contredit à la fois le *Tableau 3.1* de `Chapitre 03.md` (`L50–52`) et le PRD (`L871`) : un flux non critique muni d'un plan de contrôle et d'une sortie `B-10` **ouverts** est précisément le seul cas où **`Acheter` (SaaS autorisé)** s'applique, tandis qu'un plan **fermé** conduit au rejet ou au confinement strict en lecture seule.
- **Résolution requise** : Corriger `SCH-03-01.mmd` (et regénérer `SCH-03-01.png`) pour router `N4 -->|Ouvert| Acheter (SaaS ouvert autorisé)` et `N4 -->|Fermé| Rejet ou confinement lecture seule (BSIF B-10)`, en réservant `ASSEMBLER` (défaut) à la branche critique (`N3 -->|Oui|`).

#### `PRD-L1-002` — Attribution contradictoire de `CAP-033` entre `00 - Liminaire.md` et `Chapitre 06.md`
- **Unité** : `00-liminaire` · **Axe** : `coherence` · **Fichiers** : `Compendium/ouvrage/manuscrit/00 - Liminaire.md` (`L84`), `Chapitre 06.md` (`L31`, `L58`), `Compendium/prd.md` (`L294`, `L7111`, `L7118`)
- **Constat** : Le *Tableau 0.2* du Liminaire (`L84`) rattache le *Cycle de vie PKI (`100 j → 47 j`)* à `CAP-033` (recopié de `prd.md` L294). Or `Chapitre 06.md` (`L31`, `L58`) et l'Annexe D du PRD (`L7111`) définissent `CAP-033` comme l'*inférence confidentielle en enclave matérielle attestée (`TEE`)* dans la couche `C5 Modèles`, tandis que l'agilité cryptographique / `PKI` / `PQC` relève de **`CAP-040`** (`Plan A`, `prd.md` L7118).
- **Résolution requise** : Remplacer `CAP-033` par `CAP-040` dans le *Tableau 0.2* de `00 - Liminaire.md` (L84) et consigner l'erratum correspondant sur `prd.md` L294.

#### `PRD-L1-003` — Six formules LaTeX enfermées dans des backticks dans `Chapitre 06.md`
- **Unité** : `ch06` · **Axe** : `edition` · **Fichier** : `Compendium/ouvrage/manuscrit/02 - Partie II/Chapitre 06.md` (`L17`, `L152`, `L158`)
- **Constat** : Six expressions mathématiques LaTeX en ligne sont encapsulées dans des backticks de code : `` `\(S_{\text{ready}} < 50\)` `` (`L17`, `L158`), `` `\(c_{\text{sec}} < 60\)` `` (`L17`, `L158`), `` `\(\tau_{\min} = 60\)` `` (`L152`) et `` `\(\mathbb{I}(c_{\text{sec}} \ge 60)\)` `` (`L158`). Tout moteur Markdown/Pandoc/Typst rendra littéralement la syntaxe brute `\( ... \)` au lieu des formules, altérant la lisibilité des seuils éliminatoires de `S_ready`.
- **Résolution requise** : Retirer les backticks encadrant ces six expressions afin qu'elles soient traitées comme des mathématiques en ligne `\( ... \)` (comme aux lignes 154–156 et dans `00 - Liminaire` / `CH-02`).

---

### Constats MAJEURS (`8`)

#### `PRD-L1-004` — Contradiction frontale entre `Chapitre 01.md` et ses figures `SCH-01-02` / `SCH-01-03`
- **Unité** : `ch01` · **Axe** : `coherence` · **Fichiers** : `Chapitre 01.md` (`L53–59`, `L98–119`), `SCH-01-02.svg`, `SCH-01-03.puml`
- **Constat** :
  1. `SCH-01-02.svg` présente `Cas Nubank KDD 2026 : 5 agents ReAct sur graphes déterministes, sans MCP ni A2A`, `95 % sans ROI chiffré` (`MIT NANDA`), `40 % grandes organisations` (`McKinsey`), `Ratio 82:1 NHI / humain` et `Énergie AIE : 415 → 945 TWh`. Aucun de ces repères ni `Nubank` (exemple canonique Niveau 1 dans `prd.md` L466) ne figure dans la prose de `Chapitre 01.md`.
  2. `SCH-01-03.puml` représente l'entonnoir `PRISMA-ScR W3.2` (`582` notices → `453` dédupliquées, `AACODS 9,97/12`, `223` textes intégraux `SHA-256`, `160` études incluses, `κ = 0,7935`) ainsi que `Nubank`, `SEC`, `ITBench`, `ORCA` et `Registre MCN (432)`. En regard, `Chapitre 01.md` (`L113`) décrit un autre protocole (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`, `11` interfaces, `27` exclusions, `135` textes intégraux `L+`, `AACODS 11,13/12`) sans jamais expliquer le lien numérique entre `W3.2` (`160`) et la base du Compendium (`135`), ni nommer `Nubank`, `SEC`, `ITBench`, `ORCA` ou `MCN (432)`.
- **Résolution requise** : Aligner explicitement la prose et les schémas `SCH-01-02` / `SCH-01-03` — soit en rétablissant dans la prose le raccord clair entre les chiffres de veille du corpus (`W3.2`, `Nubank`, `82:1`, `AIE`, `MCN`) et la base fermée `L+` du Compendium (`135` textes), soit en mettant à jour les deux schémas pour qu'ils reflètent exactement les chiffres retenus dans le chapitre.

#### `PRD-L1-005` — Divergences chiffrées et conceptuelles entre `Chapitre 02.md` et `SCH-02-01` / `SCH-02-02` / `SCH-02-03`
- **Unité** : `ch02` · **Axe** : `coherence` · **Fichiers** : `Chapitre 02.md` (`L29–31`, `L41`, `L45`, `L68–78`, `L111`), `SCH-02-01.svg`, `SCH-02-02.puml`, `SCH-02-03.puml`
- **Constat** :
  1. `SCH-02-01.svg` affiche `Falaise d'horizon METR v1.1 : 17,4 h à 50 % · chute 5–6× vers 3,1 h à 80 %`, alors que `Chapitre 02.md` (`L31`, `L111`) s'appuie sur `arXiv:2503.14499v4` (`o3 ~110 minutes` à `50 %`, facteur `4× à 6×`) sans citer `METR v1.1` ni `17,4 h` / `3,1 h`.
  2. `SCH-02-02.puml` indique `32,4 %` pour la catégorie `FM-2` de `MAST` (identique à `prd.md` L618), tandis que `Chapitre 02.md` (`L29`, `L41`, `L45`) écrit systématiquement `32,3 %`.
  3. `SCH-02-03.puml` place `HAL` dans la zone rouge *Palmarès publics contaminés (`> 25 %` biaisés : HAL, SWE-bench)* alors que `Z2` du même schéma s'appuie sur la courbe `HAL` et que `Chapitre 02.md` (`L68–70`) présente `HAL` comme l'étude qui *révèle* les biais de harnais et les fuites (et ne mentionne pas `> 25 %`). En outre, `Z3` de `SCH-02-03.puml` agrège `n ≥ ceil(3/p) sur ≥ 50 à 100 scénarios`, alors que `Chapitre 02.md` (`L76–78`) distingue à juste titre `50–100` scénarios CI (`E2`, `k = 5`) et `n ≥ 300` scénarios distincts pour `p = 1 %`.
- **Résolution requise** : Synchroniser `32,3 %` vs `32,4 %` (vérifier la somme exacte de `MAST v3`), harmoniser la référence `METR` entre prose et `SCH-02-01`, retirer `HAL` de la boîte « palmarès contaminés » dans `SCH-02-03.puml` et y distinguer explicitement le jeu CI (`50–100` scénarios × `k = 5`) du dimensionnement Wilson `p = 1 %` (`n ≥ 300`).

#### `PRD-L1-006` — Rupture prose ↔ schémas sur la dispersion du marché (`1 à 59`) et le ratio `NHI 82:1` dans `Chapitre 03.md`
- **Unité** : `ch03` · **Axe** : `coherence` · **Fichiers** : `Chapitre 03.md` (`L5`, `L23–25`, `L83`), `SCH-03-01.mmd`, `SCH-03-02.svg`
- **Constat** : `SCH-03-01.mmd` (`Z1`) affiche `Dispersion marché 1 à 59 (1,5–88,2 G$ US sur 6 périmètres)` (conforme à `prd.md` L755, L791), mais `Chapitre 03.md` (`L5`, `L23–25`) ne cite que `Grand View Research` (`5,3 G$ US`) et `Mordor Intelligence` (`9,89 G$ US` en `2026`, variation « du simple au triple ») sans jamais mentionner le facteur `1 à 59`, les six périmètres emboîtés, ni la distinction revenus / valeur utilisateur (`450 G$ US`) / `GMV`. De même, `SCH-03-02.svg` (`Z1`) mentionne `Ratio NHI 82:1` (prescrit par `EXIG-D01-03.6`), alors que ce ratio n'apparaît nulle part dans `Chapitre 03.md`.
- **Résolution requise** : Harmoniser les grandeurs de marché et le ratio `82:1` entre `Chapitre 03.md`, `SCH-03-01.mmd` et `SCH-03-02.svg` (en précisant le statut probatoire de chaque série lorsque les sources primaires sont en statut `F`).

#### `PRD-L1-007` — Chiffre « `93 %` d'approbation réflexe » maintenu dans `SCH-05-03.puml` malgré son retrait de `Chapitre 05.md`
- **Unité** : `ch05` · **Axe** : `coherence` · **Fichiers** : `Chapitre 05.md` (`L69–71`, `L88–90`, `L107`), `SCH-05-03.puml` (`L36`, `L50`)
- **Constat** : `Chapitre 05.md` a retiré le taux de `93 %` d'approbation machinale (et `+26 %`) de toute sa prose ainsi que du titre de la Figure 3 (`L88`, `L90`) suite à l'exclusion en statut `F` de `PMC3240751`, en s'appuyant à la place sur `AL-Ali et coll.` (`12,36 %` / `> 15 %`, `L71`). Or `SCH-05-03.puml` conserve `93 % réflexe bloqué` (`N3`) et `Supervision HITL de façade (93 % réflexe ASI09)` (légende), créant une contradiction directe entre le texte et le schéma qui l'illustre.
- **Résolution requise** : Aligner `SCH-05-03.puml` (et regénérer `SCH-05-03.svg`) sur les chiffres retenus dans `Chapitre 05.md` (`12,36 %` non calibré / `> 15 %` sous cadence, `AL-Ali 2026`), ou documenter explicitement dans la prose le statut de la référence `93 %`.

#### `PRD-L1-008` — Rupture de convention dans la numérotation des figures entre la Partie I et les Parties II–III
- **Unité** : `ch04` (transversal `ch04`–`ch09`) · **Axe** : `edition` · **Fichiers** : `00 - Liminaire.md` à `Chapitre 09.md`
- **Constat** : `00 - Liminaire.md` et la Partie I (`CH-01` à `CH-03`) emploient une numérotation globale continue (`Figure 1` à `Figure 13`), alors que tous les chapitres des Parties II et III (`CH-04` à `CH-09`) réinitialisent le compteur à `Figure 1` à chaque chapitre (`Figure 1` à `Figure 3` ou `Figure 4`). Les tableaux, quant à eux, suivent partout la convention par chapitre (`Tableau 0.1`, `Tableau 1.1` … `Tableau 9.3`).
- **Résolution requise** : Unifier la numérotation des figures sur l'ensemble du manuscrit selon une seule règle — idéalement `Figure X.Y` (`Figure 0.1` à `Figure 9.4`) par cohérence avec `Tableau X.Y`, ou numérotation continue globale (`Figure 1` à `Figure 115`) — et mettre à jour tous les renvois en prose.

#### `PRD-L1-009` — Cinquante-cinq occurrences de `\$` échappés à l'intérieur de backticks (`00 - Liminaire`, `CH-02`, `CH-03`, `CH-04`)
- **Unité** : `00-liminaire` (transversal `00-liminaire`, `ch02`, `ch03`, `ch04`) · **Axe** : `edition` · **Fichiers** : `00 - Liminaire.md` (`L80`, `L92` : `4`), `Chapitre 02.md` (`L17`, `L82` : `14`), `Chapitre 03.md` (`L23`, `L25`, `L27`, `L29` : `31`), `Chapitre 04.md` (`L17`, `L95`, `L166`, `L183` : `6`)
- **Constat** : Cinquante-cinq montants monétaires encadrés de backticks conservent un échappement LaTeX/Markdown `\$` littéral (ex. `` `10 M\$ CA` ``, `` `0,00 \$` ``, `` `496,723 G\$ US` ``). Dans un segment de code en ligne Markdown, la barre oblique inversée n'échappe rien et s'affiche telle quelle à l'écran et à l'impression.
- **Résolution requise** : Remplacer `\$` par `$` à l'intérieur de tous les backticks (ou retirer les backticks autour des montants en prose courante, les backticks étant réservés aux jetons de code et identifiants selon `prd.md` §5.4).

#### `PRD-L1-010` — Couverture incomplète du Sommaire exécutif (`00 - Liminaire.md`) et point d'insertion erroné de `SCH-00-04`
- **Unité** : `00-liminaire` · **Axe** : `couverture_prd` · **Fichier** : `Compendium/ouvrage/manuscrit/00 - Liminaire.md` (`L23–110`)
- **Constat** : Par rapport à `prd.md` (`L275–300`, `L386`), quatre lacunes cumulées affaiblissent le Sommaire exécutif :
  1. `§0.2` omet l'exposé explicite de la **règle du maillon le plus élevé (`≤ N2`)** et du **harnais déterministe à huit étapes** (`JSON Schema Draft 2020-12`, `additionalProperties: false`, `AMBIGU_ESCALADE`, règle `H-31`), qui n'apparaissent qu'en filigrane dans la légende de la Figure 1.
  2. `§0.4` omet les **dix thèses `T1–T10`**, les **six décisions conjointes `AE ↔ AS`**, ainsi que plusieurs ancrages du tableau directeur (`PRR F-11`, `maxTotalCostCad`, `PRR O-13`, `G0-EX-CH04-01`, `CA/B Forum v2.3.1`, `NIST IR 8547`).
  3. `§0.5` omet la mention de `EN 18286:2026`, `DORA`, `Cyber Resilience Act`, `ISO/IEC 42001`, `NIST AI RMF`, le numéro d'article `art. 17` pour l'ÉFVP, et le résultat `G0` de `21/21` validations de schémas `JSON Schema 2020-12`.
  4. `SCH-00-04` est inséré à la fin de `§0.5` (`L108`) au lieu de la suite du tableau directeur KPI/SLO en `§0.4` (`prd.md` L386).
- **Résolution requise** : Compléter `§0.2`, `§0.4` et `§0.5` avec ces éléments structurants du PRD et déplacer l'insertion de `SCH-00-04` à la fin de `§0.4`.

#### `PRD-L1-011` — Backticks Markdown littéraux dans les titres SVG (`SCH-04-01`, `SCH-05-01`, `SCH-06-01`) et écart `2_input_schema`
- **Unité** : `ch04` (transversal `ch04`, `ch05`, `ch06`) · **Axe** : `schemas` · **Fichiers** : `SCH-04-01.svg`, `SCH-05-01.svg`, `SCH-06-01.svg` (et leurs copies dans `schemas/rendus/`)
- **Constat** :
  1. Les titres `<text>` de trois infographies SVG contiennent des backticks Markdown bruts rendus littéralement à l'affichage : `` `AMBIGU_ESCALADE` `` dans `SCH-04-01.svg`, `` `N0–N4` `` / `` `L0–L4` `` / `` `NX` `` / `` `D1–D8` `` / `` `Classes 1–6` `` dans `SCH-05-01.svg`, et `` `DIV-02` `` / `` `ArchiMate 4.0` `` / `` `PC1–PC5` `` dans `SCH-06-01.svg`.
  2. Dans `SCH-04-01.svg`, le jalon 2 du harnais est libellé `2_input_schema`, alors que le code source exécutable `G0-EX-CH01-02` (`pipeline.py`, `CH-04` L58) et `prd.md` (`L960`) le nomment exactement `2_input`.
- **Résolution requise** : Supprimer tous les backticks bruts dans les balises `<text>` des trois SVG (source et `rendus/`) et renommer `2_input_schema` en `2_input` dans `SCH-04-01.svg`.

---

### Constats MINEURS (`10`)

#### `PRD-L1-012` — Omissions ciblées de repères PRD dans `Chapitre 01.md`
- **Unité** : `ch01` · **Axe** : `couverture_prd` · **Fichier** : `Chapitre 01.md` (`L65–67`, `L86–92`, `L98–106`)
- **Constat** : `§1.2.1` omet `Graph of Thoughts`, `LATS`, `DeepSeek-R1`, la distinction `PRM` par rapport à `ORM`, l'alignement délibératif et `arXiv:2507.11473` (`prd.md` L470). `§1.1.4` développe bien les contrats comportementaux et les engagements sociaux observables sans citer `Bhardwaj (2026)` ni `Singh (1998)` / `Yolum & Singh (2002)` (`prd.md` L441). Le *Tableau 1.2* omet `ServiceNow`, `10 000 dépôts SEC (0,758)`, `ITBench (10–25 %)`, `ORCA-bench` et `Eurostat 2025` (`prd.md` L446, L466).
- **Résolution requise** : Enrichir `§1.1.4`, `§1.2.1` et le *Tableau 1.2* des repères manquants (en précisant le statut documentaire lorsque la source n'est pas archivée dans la base locale).

#### `PRD-L1-013` — Omissions mineures de couverture PRD et signe moins ASCII dans `Chapitre 02.md`
- **Unité** : `ch02` · **Axe** : `couverture_prd` · **Fichier** : `Chapitre 02.md` (`L15–19`, `L43–45`)
- **Constat** : `§2.1.1` omet `OWASP LLM06`, `NIST AI 600-1` et le plafond simulé de détection d'écart d'intention (`27,9 %`, `prd.md` L614–615). `§2.1.3` omet `CAMEL` et `Contract Net` (`prd.md` L622) et ne nomme pas Cognition (« *Don't Build Multi-Agents* ») ni Anthropic (`15×` / `+90 %`). À la ligne 43, `-70,0 %` emploie un trait d'union ASCII au lieu du signe moins Unicode `−70,0 %`.
- **Résolution requise** : Compléter ces références dans `§2.1.1` et `§2.1.3` et remplacer `-70,0 %` par `−70,0 %`.

#### `PRD-L1-014` — Omissions PRD, inversion `N`/`M` et redite dans `Chapitre 03.md`
- **Unité** : `ch03` · **Axe** : `couverture_prd` · **Fichier** : `Chapitre 03.md` (`L64–70`, `L106–114`)
- **Constat** : (1) `§3.2.2` omet la norme `ISO/IEC 25010:2023 (SQuaRE)` (`prd.md` L800), `§3.1.3` omet `CAP-029`, `CAP-034` (`EXIG-D01-03.5`, `prd.md` L767) et la part `> 97 %` des jetons d'entrée ; (2) les variables `N` et `M` sont inversées entre `L106` (« `N` agents ... à `M` systèmes ») et `L110` (« \(M\) agents ... à \(N\) systèmes ») ; (3) l'exemple `4 agents × 5 systèmes = 20 → 9 contrats` est répété à quatre lignes d'intervalle (`L110` et `L114`).
- **Résolution requise** : Ajouter `ISO/IEC 25010:2023`, `CAP-029`/`CAP-034` et `> 97 %`, harmoniser `N` (agents) et `M` (systèmes) à la ligne 110, et condenser la redite `L110`/`L114`.

#### `PRD-L1-015` — Emplois de l'abréviation proscrite `vs` hors code (charte PRD §5.3)
- **Unité** : `ch01` (transversal `ch01`–`ch06`) · **Axe** : `edition` · **Fichiers** : `Chapitre 01.md` (`L104`), `Chapitre 02.md` (`L115`), `Chapitre 03.md` (`L139`, `L144`), `SCH-02-01.svg`, `SCH-04-03.puml`, `SCH-05-03.puml`, `SCH-06-02.puml`
- **Constat** : La charte rédactionnelle (`prd.md` L308) proscrit explicitement l'abréviation `vs` hors code dans la prose et les schémas. Quatre occurrences subsistent dans le manuscrit (`CH-01` L104, `CH-02` L115, `CH-03` L139 et L144) et cinq dans les sources de schémas (`SCH-02-01.svg` : `HT vs TTC` ; `SCH-04-03.puml` : `Spécificateur vs Bâtisseur` ; `SCH-05-03.puml` : `Agent interactif vs ambiant`, `PC3 vs Loi 25 art. 12.1` ; `SCH-06-02.puml` : `42 CAP invariantes vs 10 sur signal`).
- **Résolution requise** : Substituer « par rapport à », « contre » ou « face à » à chacune de ces neuf occurrences et regénérer les rendus des schémas concernés.

#### `PRD-L1-016` — Fuites de métadonnées internes d'atelier éditorial dans la prose (`CH-04` à `CH-09`)
- **Unité** : `ch07` (transversal `ch04`–`ch09`) · **Axe** : `edition` · **Fichiers** : `Chapitre 04.md` (`L7`, `L81`, `L95`), `Chapitre 05.md` (`L9`, `L107`), `Chapitre 06.md` (`L7`, `L168`), `Chapitre 07.md` (`L19`, `L167`), `Chapitre 08.md` (`L11`, `L29`, `L49`, `L161`), `Chapitre 09.md` (`L42`, `L76`, `L153`)
- **Constat** : La prose destinée au lecteur expose des artefacts internes de l'atelier de rédaction qui n'existent pas dans l'ouvrage publié : la clé de manifeste `owned_concepts` (`CH-07` L167, `CH-08` L161, `CH-09` L153), les slugs JSON MindMap (`protocole-mcp`, `metriques-soutien-vs-production`, etc., dans `CH-07` L19, `CH-08` L29, `CH-09` L42/L76), les identifiants `SUB_D02_01..03` (`CH-04`–`CH-06`) et des chemins ou codes internes (`aq/rapports-g0.json`, `registre/ancres-chronologiques.json`, `SRC-039`, `SRC-055`, `SRC-063`, `SRC-083`).
- **Résolution requise** : Reformuler ces passages en français éditorial (« partition thématique de l'ouvrage », « rapport de vérification `G0` », « registre chronologique de l'Annexe C ») et réserver les slugs/IDs techniques aux annexes de traçabilité (`Annexe A`, `Annexe D`).

#### `PRD-L1-017` — Faute d'élision `fr-CA` (`chaîne de invites`) et casse RFC 2119 (`ne DOIT JAMAIS`)
- **Unité** : `ch08` (et `ch07`, `00-liminaire`) · **Axe** : `edition` · **Fichiers** : `Chapitre 08.md` (`L9`, `L15`), `Chapitre 07.md` (`L148`), `00 - Liminaire.md` (`L7`)
- **Constat** : (1) `Chapitre 08.md` (`L9`) comporte la faute d'élision « de **chaîne de invites** » au lieu de « de **chaîne d'invites** » ; (2) `Chapitre 07.md` (`L148`) et `Chapitre 08.md` (`L15`) écrivent `ne DOIT JAMAIS` au lieu de `NE DOIT JAMAIS` prescrit par `prd.md` L306 ; (3) `00 - Liminaire.md` (`L7`) énumère les mots-clés RFC 2119 sans inclure `NE DOIT JAMAIS`.
- **Résolution requise** : Corriger l'élision (`chaîne d'invites`), normaliser `NE DOIT JAMAIS` en majuscules intégrales dans `CH-07`/`CH-08` et l'ajouter à la liste RFC 2119 du Liminaire.

#### `PRD-L1-018` — Italique brisé dans une légende (`CH-05`) et hétérogénéité éditoriale inter-parties (`CH-07`–`CH-09`)
- **Unité** : `ch05` (et `ch07`–`ch09`) · **Axe** : `edition` · **Fichiers** : `Chapitre 05.md` (`L61`), `Chapitre 07.md`–`Chapitre 09.md` (`L3`, fin de chapitre)
- **Constat** : (1) Dans `Chapitre 05.md` (`L61`), `*Figure 2 — SCH-05-02 : Règle du maillon le plus élevé (*High-Water Mark*) et règle d'or ...*` imbrique `*...*` dans une légende déjà en italique, ce qui désactive l'italique sur `High-Water Mark` ou rompt le rendu Markdown ; (2) contrairement à `00 - Liminaire` et `CH-01`–`CH-06`, les chapitres `CH-07`–`CH-09` mettent toute la question directrice en italique (`L3`) et placent l'encadré *Trois invariants exécutables* en toute fin de chapitre plutôt qu'en §X.1 ou §X.2.
- **Résolution requise** : Corriger la légende de `CH-05` L61 (retirer les astérisques internes ou passer `High-Water Mark` entre guillemets/backticks) et uniformiser la mise en forme de la *Question directrice* et la position de l'encadré des invariants sur tout le manuscrit.

#### `PRD-L1-019` — Redites rapprochées dans `CH-07` / `CH-08` et préfixe `Tomes/` divergent dans `CA-G0-SYNC`
- **Unité** : `ch07` (et `ch08`) · **Axe** : `edition` · **Fichiers** : `Chapitre 07.md` (`L94`, `L100`, `L108`), `Chapitre 08.md` (`L51`, `L53`, `L55`)
- **Constat** : (1) `Chapitre 07.md` répète presque à l'identique à six lignes d'écart (`L94` et `L100`) le blocage `EXIG-MCP-18` sur `x-mcp-header` (`token`, `password`, `nas`, `iban`, `cookie`) ; (2) `Chapitre 08.md` répète à deux lignes d'intervalle (`L51` et `L53`) le durcissement `DOIT` des gardes anti-SSRF (`EXIG-A2A-12`, `EXIG-SEC-12`, `127.0.0.0/8`, `169.254.169.254`) ; (3) les commentaires HTML `CA-G0-SYNC` de `CH-07` (`L108`) et `CH-08` (`L55`) utilisent le préfixe `Tomes/Tome 8 - ...` qui diffère du champ `source_path` de `aq/rapports-g0.json` et de `CH-04` (`Tome 8 - ...`), bien que les empreintes `SHA-256` concordent à `100 %`.
- **Résolution requise** : Supprimer les deux paragraphes/phrases redondants dans `CH-07` et `CH-08` et uniformiser le format de `path` dans les balises `CA-G0-SYNC`.

#### `PRD-L1-020` — Écarts mineurs prose ↔ schémas (`SCH-09-01`, `SCH-09-03`, `SCH-09-04`) et omissions `ISO 11354-1` / `EIRA 6.1.0` dans `Chapitre 09.md`
- **Unité** : `ch09` · **Axe** : `schemas` · **Fichiers** : `Chapitre 09.md` (`L21`, `L36`, `L80`, `L104`, `L110`), `SCH-09-01.puml`, `SCH-09-03.svg`, `SCH-09-04.puml`
- **Constat** :
  1. La légende de la Figure 1 (`CH-09` L21) annonce la « désambiguïsation du maillage » dans `SCH-09-01` (conforme à `prd.md` L1996 `Z3`), mais `SCH-09-01.puml` n'inclut aucune boîte distinguant les trois acceptions d'`AgentMesh` (`Istio`/`agentgateway`, `Solace`, `AgentMesh`). De plus, `SCH-09-01.puml` affiche `CloudEvents 1.0` et `maxhops = 4`, alors que la prose (`L36`) cite `CloudEvents 1.0.2` sans mentionner `maxhops = 4`.
  2. `SCH-09-03.svg` indique `Préavis sortie 12 mois`, tandis que `CH-09` (`L104`, Tableau 9.3) précise `préavis écrit minimal de 90 jours` (`EXIG-APP-13`), `transition de 6 mois` (`EXIG-APP-14`) et `dépréciation 12 mois` côté standards (`SEP-2596`).
  3. `SCH-09-04.puml` affiche `−90 % coût relecture`, chiffre absent de la prose (`CH-09` L110).
  4. `Chapitre 09.md` (`L80`) ne nomme pas explicitement `ISO 11354-1:2011` (et le constat « palier unifié malgré ambition fédérée »), `EIRA 6.1.0` ni `ISO/IEC 19941` (`prd.md` L1897–1898).
- **Résolution requise** : Compléter `SCH-09-01.puml` (bloc désambiguïsation maillage + `CloudEvents 1.0.2`) ou ajuster la légende de Figure 1, harmoniser le libellé de préavis dans `SCH-09-03.svg` et le gain KV-cache dans `SCH-09-04.puml`, et ajouter `ISO 11354-1:2011`, `EIRA 6.1.0` et `ISO/IEC 19941` à `CH-09` L80.

#### `PRD-L1-021` — Nuances d'harmonisation mineures dans la Partie II (`LCIM`, `9` vs `10` clauses, `Plan-and-Solve`, `ISO/IEC 42105`)
- **Unité** : `ch06` (et `ch04`, `ch05`) · **Axe** : `coherence` · **Fichiers** : `Chapitre 04.md` (`L31`), `Chapitre 05.md` (`L29`), `Chapitre 06.md` (`L70`, `L74`, `L115`), `SCH-06-02.puml`
- **Constat** : (1) `Chapitre 06.md` (`L115`) présente `LCIM` sur `5 paliers` (Tome 1 Tableau 7.1), alors que `prd.md` CH-06 (`L1333`) évoque `4 paliers` (Tableau 43.4) et `Chapitre 09.md` (`L80`) expose le modèle complet à `7 niveaux` (`0` à `6`) : un renvoi d'une phrase expliciterait l'emboîtement sans ambiguïté ; (2) `SCH-06-02.puml` et la légende de Figure 2 (`CH-06` L74) mentionnent `9 clauses de sortie` alors que la prose et le Tableau 6.3 (`L11`, `L17`, `L177`) normalisent `10 clauses` (`EXIG-APP-07..16`, expliquées en `L70`) ; (3) `CH-04` (`L31`) omet `Plan-and-Solve` et le nom explicite `Self-Refine` (`prd.md` L968) et `CH-05` omet `ISO/IEC 42105` (`prd.md` L1148).
- **Résolution requise** : Ajouter une phrase de pont sur l'emboîtement `LCIM` (`4`/`5`/`7` paliers) dans `CH-06` L115, préciser `(9 de négociation → 10 EXIG-APP-07..16)` dans la légende de `SCH-06-02`, et mentionner `Plan-and-Solve` / `Self-Refine` (`CH-04`) et `ISO/IEC 42105` (`CH-05`).
