# Rapport consolidé de lissage transversal (`G5`), recollation `G3` et inspection visuelle PDF

**Ouvrage :** *Ingénierie exécutable de l'entreprise agentique* (Volume 8 — `8 - Manuel/` et `8 - Trousse/`)  
**Date de gel documentaire :** `2026-12-02` (`2 décembre 2026`)  
**Critères couverts :** `CA-14`, `CA-16`, `CA-17`, `CA-18`

---

## 1. Lissage éditorial transversal (`G5` · `CA-16`) et rejeu différentiel `G2`

Le lissage éditorial transversal a unifié le français canadien technique, les conventions typographiques et la cohérence terminologique entre le liminaire, les quatre chapitres analytiques et les journaux d'ancrage :

- Alignement uniforme des intitulés de normalisation et de régulation (`BSIF`, `ACVM NC 31-103`), de la distinction typographique entre les paquets Python (`snake_case` dans `8 - Trousse/`) et les modules en prose (`harness-proto/`, `authz-pqc-audit/`, `policy-saga/`, `evalops-prr/`), ainsi que de la modalité prospective au futur pour les jalons postérieurs au `2 décembre 2026` (`30 mars 2027`, `28 juillet 2027`, `2 décembre 2027`).
- Validation par rejeu différentiel `G2` (`e9982661`) après lissage sans reliquat `imprécis` ni `non supporté`, suivie de micro-retouches localisées vérifiées hors dérive factuelle (`Chapitre 02#L335-341`, `Chapitre 04#L7`, `ancrage/ch00-ancrage.md#L90`, `ancrage/ch01-ancrage.md#L45,54,70,101,129`, `ancrage/ch04-ancrage.md#L3-6,23`).

---

## 2. Recollation finale à froid `G3` Passe 2 (`seed 20270802` · `CA-14`)

- **Enrichissement sans décalage :** enrichissement sur place de passages ciblés du liminaire et des chapitres `02`, `03` et `04` sans scission ni ajout de paragraphe (`0` décalage d'index `Pnnn`).
- **Échantillonnage stratifié disjoint :** génération via `echantillon_aq.py --seed 20270802` à l'exclusion de `aq/recollation-seed-20270801.json`, produisant `60` énoncés répartis en `4` strates de `15` items et respectant le plancher minimal par unité (`00-liminaire`: `10`, `ch01`: `11`, `ch02`: `13`, `ch03`: `11`, `ch04`: `15`), avec `0` chevauchement sur `claim_loc` ni `paragraph_loc`.
- **Verdict indépendant consigné dans `aq/recollation-seed-20270802.md` :** `59/60` conformes en première passe, puis **`60/60` conformes (`100 % supportés`)** après rectification ciblée de l'item `7` (`00-liminaire:P026:S01` sur `SEP-3398` `Accepted` et ajout `[16] SRC-082` dans `sources/ch00-sources.md`), confirmée ensuite par `execute_g0.py --verify-sync-manifest` (`exit 0`), `genere_annexes.py` (`exit 0`) et `verifie_manuscrit.py --strict` (`exit 0`).

---

## 3. Inspection visuelle intégrale du premier tirage PDF (`314 / 314` pages · `100 %`)

L'intégralité du premier tirage PDF (`0 - PDF-MD/8 - Manuel.pdf`, `314` pages) a été rastérisée à `150 DPI` et inspectée page par page en `14` lots visuels couvrant les pages `1` à `314` (`100 %`). Ce contrôle visuel exhaustif a mis au jour sept catégories de défauts de mise en forme et de lisibilité :

1. **Annotations `/Link` tronquées en PDF :** Typst réinterprétait les URLs contenant `\u200b` à l'intérieur de `#link("URL")[...]` via son détecteur automatique, tronquant `106+` liens bibliographiques en Annexe A à leur premier préfixe (`https://www.rfc-`, `https://arxiv.org/`, etc.).
2. **Tableaux multi-colonnes (`Annexe A` 6–7 colonnes et tableaux du corps) :**
   - Les tableaux pandoc avec `columns: N` ou `align: (auto, ...)` héritaient d'un alignement centré et de largeurs trop étroites sur les colonnes identifiants/verdicts.
   - Les longs identifiants CamelCase ou accentués en code inline (`OpaStaticCheckError`, `SessionTaintTracker`, `CompensationChannel`, `SimulatedCrashError`, `OpaPolicyEngine`, `rétrocompatibilité`) ainsi que les mots français longs après élision (`d’approvisionnement`) provoquaient des débordements de cellules ; en sens inverse, un découpage arbitraire tranchait des identifiants courts hors tableaux (`DeterministicHarness`, `StreamableHttpAdapter`) et certains nombres décimaux (`0.0089`).
   - `Tableau 2.2` était détaché de sa légende entre deux pages (`p. 64` → `p. 65`).
3. **Blocs de code et encadrés `#quote` :** quelques blocs d'au plus `40` lignes comportant des lignes de `74–78` caractères (dont `G0-EX-CH04-03`) subissaient des retours forcés sur largeur `4,46 po`, et les pastilles de code inline (`#F1F5F9`) se confondaient avec le fond `#F1F5F9` des encadrés `#quote`.
4. **Espaces insécables, flèches et césures :** séparations orphelines sur `%`, `\$ CA` / `\$ US`, séparateurs de milliers, unités (`o`, `s`, `Kio`), `§`, signes `−`, dépôts (`8 - Trousse/`), flèches `- / >`, tirets de drapeaux (`-failfast2`, `EXIG-*`), `#divider()` précédant immédiatement un titre, et justification trop étirée dans les listes d'Annexe A/B.
5. **Figures (`Fig-00` à `Fig-08`) :** flèche probabiliste non ambrée et croisement de légende sur `Fig-00` ; rognage en bordure sur `Fig-01` ; collisions flèche/bordure sur `Fig-02`, `Fig-05`, `Fig-06` et `Fig-07` ; largeur excessive (`1 222 px`) sur `Fig-03` ; orientation verticale inverse de la prose et omission de `cost_center` / citation `EXIG-OBS-13` inexistante sur `Fig-04` ; étiquettes `Oui`/`Non` sans fond blanc opaque et `pass^k` littéral sur `Fig-08`.
6. **Micro-coquilles rédactionnelles :** absence de ligne vide avant `*Figure 4*` et de ligne `>` après le titre de l'encadré final au Chapitre 2 (`L335-341`), répétition de `*Scénario illustratif.*` en `Chapitre 04#L7`, mise en forme LaTeX brute résiduelle dans `ancrage/ch01-ancrage.md`, retours à la ligne en en-tête de `ancrage/ch04-ancrage.md`, coquille `aucune contournement` et parenthèses doubles `((UE)` dans `genere_annexes.py`.

---

## 4. Remédiations appliquées, contrôle PyMuPDF et réinspection visuelle finale

Toutes les anomalies ci-dessus ont été corrigées dans `gabarit-livre.typ`, `assemble_livre.py`, `genere_annexes.py`, `test_outillage_aq.py`, les neuf sources de diagrammes (`Fig-00`..`Fig-08`) et les micro-cibles du manuscrit et des journaux d'ancrage :

- **`compile_figures.py --strict` :** `9/9` figures recompilées (`7` SVG PlantUML et `2` PNG Mermaid, `10..14` nœuds, `0` motif banni) et vérifiées visuellement une à une (`Fig-04` en `flowchart LR` avec `Couloir 2` supérieur et `Couloir 1` inférieur, `EXIG-OBS-12` et `cost_center` ; `Fig-08` avec `pass<sup>k</sup>`, trait ambre et pastilles blanches opaques).
- **`gabarit-livre.typ` & `assemble_livre.py` :** protection globale des `#link("https?://...")` par `#text(hyphenate: false)[#("...")]` avec césure `.` / `-` / `/` ; `align: auto -> left` y compris sur `columns: N` ; découpe cellulaire sur CamelCase, opérateurs, élisions françaises et jetons accentués `>= 16` caractères sans altérer les décimaux (`0.0089`), tout en préservant les identifiants `< 26` caractères hors tableaux ; liaison des petits tableaux (`<= 16` lignes) à leur légende `Tableau X.Y` ; `inset: (x: 3.0pt, y: 3.5pt)` en tableaux (`7.0 pt` / `6.5 pt`) et `6.7 pt` / `inset: 5 pt` sur blocs de code ; pastilles blanches dans `#quote` ; espaces insécables (`\u00a0`) et `→` ; `justify: false` sur bibliographie/journaux d'Annexe A et listes finales d'Annexe B.
- **Vérification automatisée PyMuPDF et réinspection visuelle (`311` pages) :**
  - `EXT_LINKS = 189`, **`0` lien `/Link` tronqué**.
  - **`0` dépassement horizontal (`x1 > 392,0 pt`)** sur les `311` pages du manuel assemblé.
  - **`0` occurrence** résiduelle de `\$`, `\(`, `\)` ou `Syntax Error`.
  - Réinspection visuelle par `read_file` effectuée sur l'ensemble des `9` figures en contexte page, `Tableau 2.2`, le bloc `G0-EX-CH04-03`, l'encadré `Trois invariants exécutables — Chapitre 2`, le début et la bibliographie d'Annexe A, `ch00-ancrage` (`CH00-028`), `ch01-ancrage` (`CH01-009`, `CH01-029`, `CH01-050`), les tableaux `ch03-ancrage` (`CH03-001` à `CH03-085`), `ch04-ancrage` et les synthèses/listes d'Annexe B (`0` défaut résiduel constaté).

---

## 5. Verdict final (`CA-16` · `CA-18`)

- **Lissage éditorial transversal (`G5`) :** validé et contre-ancré (`G2` différentiel à `100 %`).
- **Recollation à froid (`G3` Passe 2) :** `60/60` (`100 %` supportées).
- **Inspection visuelle PDF (`100 %` passe initiale `314` pages + réinspection ciblée finale `311` pages + audit intégral PyMuPDF) :** **CONFORME**.
