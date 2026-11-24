# Cartographie thématique et structurelle du Corpus (`Cartographie`)

[Retour à l'index principal](../README.md) · [Suite intégrale (`Corpus/`)](../Corpus/README.md) · [Ouvrir la MindMap interactive](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html) · [PRD maître (`prd.md`)](../prd.md)

Application HTML autonome hors ligne (`file://`, sans CDN ni requête réseau externe) cartographiant l'ensemble des **9 fichiers Markdown** du corpus ([`Corpus/README.md`](../Corpus/README.md) et `Tome 1` à `Tome 8`).

## Métriques vérifiées du graphe et du corpus

- **Périmètre source** : `9` fichiers `.md`, `69 821` lignes, `1 537 418` mots (`split()`), `4 542` pages PDF et `319` diagrammes.
- **Structure extraite (`CommonMark` strict)** : `4 434` titres `H1–H6` (hors `143` blocs de code clôturés filtrés), `564` identifiants normatifs et techniques uniques (`EXIG-*`, `CAP-*`, `PEX-*`, `OO1–OO4`, `T1–T10`, `PRR-75`, `C01–C40`, `L0–L4`, `DIV-02`, `SBB-*`, `G0–G5`).
- **Arbre thématique (5 niveaux)** : `380` nœuds (`1` racine, `12` domaines `D01–D12`, `36` sous-domaines, `71` familles thématiques, `260` thèmes détaillés), `1 931` occurrences ancrées aux lignes exactes.
- **Couverture & interrelations** : `616` interrelations typées sur les `8` types canoniques (`0` arête cassée, `0` auto-boucle), `290 / 290` chapitres/liminaires/annexes mappés (`0` orphelin) et `1 636` unités structurelles liées directement aux thèmes.
- **Pivots de concordance** : `5` discordances résolues (`DISC-01`..`DISC-05`, Tome 8 §0.2) + fermeture `DIV-02` (Tome 5), `100` jalons chronologiques (`2023–2035`) et `267` entrées de traçabilité (`EXIG / CAP / PRR-75 / C01–C40 / 5 SBB`).
- **Livrable autonome** : [`MindMap - Cartographie thématique du Corpus.html`](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html) (`4 061 419` octets, thèmes `Auto / Clair / Sombre`).
- **PRD maître compilé** : [`../prd.md`](../prd.md) (`12` domaines `D01–D12`, `36` chapitres, `71` familles, `260` thèmes, `4` annexes normatives `A–D`, `4 512` lignes, `134 709` mots).

## Les 4 vues dynamiques

1. **MindMap Thématique & Interrelations** *(vue par défaut)* : disposition **Horizontale (`G→D`)** ou **Radiale (`360°`)**, contrôle de profondeur (`Niv. 1` à `Niv. 5`), pastilles `(+N)`, projection intelligente des liens sur l'ancêtre visible, bouton **Déplier les cibles liées** et **Mode Rayon X** au clic/survol.
2. **Structure Intégrale (`9 fichiers .md`)** : exploration hiérarchique de `Corpus/README.md` et des `Tomes 1..8` jusqu'aux `4 434` sections `H1–H6` avec plages de lignes, comptage de mots, liens directs `../Corpus/<fichier>.md#Lxxx` et pastilles cliquables vers les thèmes associés.
3. **Graphe Synaptique & Explorateur de Chemins (`A → B`)** : vue réseau **Circulaire par domaine** ou **Force-directed**, filtrage d'ego-réseau (`1 saut`, `2 sauts`, `Complet`) et **calculateur de plus court chemin sémantique** détaillant chaque saut et sa justification.
4. **Concordance & Réconciliations** : carte thermique interactive `Domaines / Sous-domaines × 9 fichiers (R, T1..T8)`, fiches `DISC-01..05` et `DIV-02`, chronologie filtrable `2023–2035` et matrice cherchable `EXIG / CAP / PRR-75 / C01–C40 / 5 SBB`.

La barre d'outils supérieure offre une recherche plein-texte instantanée (`Ctrl+K`), `6` filtres multi-facettes (`Tome`, `Domaine`, `Autonomie`, `Rôle`, `Horizon`, `Relation`), un inspecteur latéral détaillé ainsi que l'export `SVG` et `JSON` filtré.

## Arborescence & outillage

| Fichier | Rôle |
|---|---|
| [`MindMap - Cartographie thématique du Corpus.html`](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html) | Application interactive autonome hors ligne (`file://`) |
| [`../prd.md`](../prd.md) | PRD maître exhaustif (`12` domaines, `36` chapitres, `71` familles, `260` thèmes, `4` annexes) |
| [`outils/extraire_structure.py`](outils/extraire_structure.py) | Parseur CommonMark strict des 9 `.md` → `structure-integrale.json` |
| [`outils/synthetiser_graphe.py`](outils/synthetiser_graphe.py) | Fusion des shards et pivots → `synthese-transversale.json` |
| [`outils/compiler_mindmap.py`](outils/compiler_mindmap.py) | Assemble `corpus-mindmap-data.json` et injecte le JSON échappé dans `template_mindmap.html` |
| [`outils/compiler_prd.py`](outils/compiler_prd.py) | Compile les 7 shards PRD et `corpus-mindmap-data.json` vers `../prd.md` |
| [`outils/template_mindmap.html`](outils/template_mindmap.html) | Gabarit HTML/CSS/JS autonome (`light-dark`, SVG, Node-testable) |
| [`donnees/schema-cartographie.json`](donnees/schema-cartographie.json) | Schéma formel des 12 domaines, 8 relations et structures JSON |
| [`donnees/schema-prd-shard.json`](donnees/schema-prd-shard.json) | Schéma JSON Schema 2020-12 des shards de rédaction du PRD |
| [`donnees/pivots-concordance.json`](donnees/pivots-concordance.json) | Tables pivots (chronologie, `DISC-01..05`, `DIV-02`, `EXIG/CAP/PRR/C40/SBB`) |
| [`donnees/structure-integrale.json`](donnees/structure-integrale.json) | Arbre intégral `H1–H6` des 9 fichiers (`4 434` titres) |
| [`donnees/synthese-transversale.json`](donnees/synthese-transversale.json) | Graphe thématique unifié (`380` nœuds, `616` relations) |
| [`donnees/corpus-mindmap-data.json`](donnees/corpus-mindmap-data.json) | Bundle unifié injecté dans la MindMap HTML |
| [`tests/test_cartographie.py`](tests/test_cartographie.py) | Suite `pytest` + validation syntaxique et fonctionnelle `Node.js` |
| [`tests/test_prd.py`](tests/test_prd.py) | Suite `pytest` vérifiant couverture, ancres `CommonMark` et liens de `prd.md` |

## Commandes de régénération et de vérification

```powershell
# 1. Extraire l'arbre structurel H1–H6 des 9 fichiers de Corpus/
python Cartographie/outils/extraire_structure.py

# 2. Synthétiser le graphe transversal depuis les shards et pivots
python Cartographie/outils/synthetiser_graphe.py

# 3. Compiler le bundle JSON et la MindMap HTML autonome
python Cartographie/outils/compiler_mindmap.py

# 4. Compiler le PRD maître à la racine du dépôt (prd.md)
python Cartographie/outils/compiler_prd.py

# 5. Exécuter les suites complètes de tests (Cartographie + Node.js + PRD)
python -m pytest Cartographie/tests/test_cartographie.py Cartographie/tests/test_prd.py -v
```
