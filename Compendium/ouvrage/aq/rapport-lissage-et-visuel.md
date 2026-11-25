# Rapport de lissage éditorial (`G5`) et d'inspection visuelle intégrale (`CA-16`)

- **Rôle exécutant :** `inspecteur-visuel` (`T9-S3`) et `revise-outils-livrables` (`REV-05` — actualisation post-révision `PRD`)
- **Date de référence et de gel :** `2 décembre 2026` (`2026-12-02`)
- **Livrables inspectés (post-révision `REV-05`) :**
  - `Compendium/ouvrage/livrables/Compendium.pdf` (`23 123 417` octets, `834` pages, `400` signets)
  - `Compendium/ouvrage/livrables/Compendium.html` (`10 530 440` octets, `115/115` figures base64)
  - `Compendium/ouvrage/livrables/Compendium.md` (`1 856 321` octets, `8 362` lignes)
- **Statut de clôture visuelle :** **CONFORME — 0 défaut bloquant**

---

## 1. Inspection intégrale du livrable PDF (`100,0 %` des `834` pages)

Toutes les `834` pages de `Compendium.pdf` recompilé à l'issue de la campagne `REV-01`–`REV-05` ont été balayées algorithmiquement (`pymupdf` / `fitz`), puis complétées par une inspection visuelle directe (`read_file` à `140 DPI`) sur les zones critiques et l'ensemble des corrections apportées.

### 1.1 Métriques automatisées sur `834 / 834` pages (`100,0 %`)

| Contrôle automatisé | Périmètre | Résultat observé | Statut |
|---|---:|---|---|
| Décompte exact des pages | `834` pages | `834` pages (couverture `p. 1` à dernière page `p. 834`, `400` signets) | Conforme |
| Débordement hors page (`bbox`) | `834 / 834` pages | `0` boîte texte, image ou dessin hors limites de page | Conforme |
| Pages blanches anormales | `834 / 834` pages | `0` page blanche ni page à faible encre anormale | Conforme |
| Formules LaTeX/Typst brutes (`\\(`, `\\)`, `\\$`, `Syntax Error`) | `834 / 834` pages | `0` occurrence résiduelle | Conforme |
| Glyphes manquants (`\ufffd`) | `834 / 834` pages | `0` occurrence | Conforme |
| Corruptions textuelles (`//[É]/`, `[N]//`, `policies_opa/opa_runner.py`) | `834 / 834` pages | `0` occurrence | Conforme |
| Table des matières (`passᵏ`) | `p. 3–6` | `passᵏ` composé en exposant typographique (`0` `pass^k` brut) | Conforme |
| Numérotation séquentielle des `115` figures | `115 / 115` schémas | `Figure 1` à `Figure 115` uniques et ordonnées sans doublon ni reset | Conforme |
| Citations `[k]` et bibliographies d'unités | `37 / 37` unités | `37/37` sous-sections « Références » injectées, `0` citation orpheline | Conforme |

### 1.2 Inspection visuelle directe (`read_file` sur captures PNG pleine résolution `REV-05`)

1. **Table des matières (`p. 3`)** : hiérarchie propre, pagination exacte incluant `Références du liminaire` (`p. 14`) et titre du Chapitre 02 composé avec exposant typographique **`passᵏ`** (`p. 35`).
2. **Bibliographie injectée en fin d'unité (`p. 39`, Chapitre 01)** : sous-section **« Références du chapitre »** nette et lisible (`[1] SRC-027` à `[6] SRC-014`), sans URL débordante ni fuite d'atelier.
3. **Schémas bloquants corrigés et recompilés** :
   - `Figure 11 — SCH-03-01` (`p. 62`, Mermaid `300 DPI`) : routage logique corrigé (`Porte 1` Non → `Portes 2–3` Ouvert → `ACHETER`, Fermé → `Rejet ou confinement`).
   - `Figure 43 — SCH-13-01` (`p. 234`, SVG) : dissociation nette entre l'arbre de sobriété (`N0` → multi-agents, `EXIG-ORC-01`) et la grille d'autorité `OO1–OO4` (`Tome 1 § 22.1`).
   - `Figure 60 — SCH-18-03` (`p. 323`, Mermaid `300 DPI`) : mesures exactes `pqc_http431.py` (`2 sauts : 9,6–38,8 Ko` ; `5 sauts : 24,5–97,4 Ko, max 97 403 o`) alignées au `Tableau 18.1` juste au-dessus.
4. **Annexes `A` à `E` refondues sans troncature et fin d'ouvrage (`p. 636`, `673`, `738`, `774`, `823`, `831`, `834`)** :
   - **Annexe A (`p. 636`)** : `Tableau A.1` complet (`Ch.`, `Domaine`, `Sous-domaine node_id`, `Fam./Thm.`, `Occ.`, `Tomes`, `Schémas`), zéro colonne `Cible (mots)`, typographie `fr-CA` exacte.
   - **Annexe B (`p. 673`)** : enchaînement continu `1.` → `Tableau B.1` → `2. Analyse des vingt-cinq nœuds carrefours`, catalogue intégral des `616/616` interrelations sans doublon.
   - **Annexe C (`p. 738`)** : décompte chronologique exact (`12` acquis au gel / `74` post-gel et paliers `DAPP`), `Emplacement Compendium : Liminaire § 0.2 ; Chapitre 36`, zéro fuite `Volume 8`.
   - **Annexe D (`p. 774`)** : `policy_saga/opa_runner.py`, note de concordance `17` paquets `requirements.lock` / `18` paquets `SPDX`, plage `PEX-001`–`PEX-044`, inventaires complets `52 CAP`, `75 PRR`, `57` specs `L+`, `95` liaisons `G0`, `43 INI` / `15 POR` / `27 SIG`.
   - **Annexe E (`p. 823`, `p. 831`, `p. 834`)** : `Tableau E.1` (`267/319 = 83,70 %`), `Tableau E.2` (`8` archétypes visuels), présence intégrale de **Partie XII (`D12`, `Figure 106` à `Figure 115`)** et clôture propre en dernière page (`p. 834`).

---

## 2. Inspection du livrable HTML autonome (`Compendium.html`) et du Markdown (`Compendium.md`)

- **`Compendium.html` (`10 530 440` octets)** : `115/115` figures embarquées en `data:image/...;base64` (`92` SVG + `23` PNG), `0` dépendance réseau externe dans `<img>`, `<script>` ou `<link>`, `0` ancre interne cassée, `0` marqueur `BIBLIOGRAPHIE_BRUTE`, `0` `//[É]/`, `0` doublon TOC (`<nav id="TOC">` unique), `pass<sup>k</sup>` rendu.
- **`Compendium.md` (`1 856 321` octets, `8 362` lignes)** : `## Table des matières` GFM en tête, `37/37` bibliographies d'unités (`0` citation `[k]` orpheline), `Figure 1`..`Figure 115` uniques, `0` `\$` littéral, `0` marqueur `BIBLIOGRAPHIE_BRUTE`, `100 %` des légendes de tableaux uniformément placées en dessous.

---

## 3. Synthèse du lissage `G5` et de la campagne de révision `REV-01`–`REV-06`

- **Recollation à froid double passe `G3`** : deux passes strictement disjointes — `seed=20270901` (`148/148`) et `seed=20270902` (`148/148`), soit **`296 / 296` énoncés validés (`100,0 %`)**.
- **Révision intégrale `PRD` (`REV-01`–`REV-05`)** : `107/107` constats (`12` références + `95` PRD) corrigés et vérifiés, `115/115` schémas recompilés (`--strict`), `5/5` Annexes déterministes calibrées simultanément sous `vm` et `pp` (`42/42` unités conformes sur le tableau de bord).

## 4. Verdict de clôture

Le Compendium satisfait intégralement aux critères éditoriaux, normatifs, visuels et d'autonomie documentaire (`CA-01` à `CA-22`, `G0`–`G5`) : **0 défaut bloquant** sur les `834` pages PDF, le HTML autonome, le Markdown consolidé et les `115` schémas.
