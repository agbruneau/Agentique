# Cartographie thématique et structurelle du Corpus (`Cartographie`)

[Retour à l'index principal](../README.md) · [Suite intégrale (`Corpus/`)](../Corpus/README.md) · [Ouvrir la MindMap interactive](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html) · [PRD Web autonome](PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) · [PRD maître (`prd.md`)](../prd.md)

Application HTML autonome hors ligne (`file://`, sans CDN ni requête réseau externe) cartographiant l'ensemble des **9 fichiers Markdown** du corpus ([`Corpus/README.md`](../Corpus/README.md) et `Tome 1` à `Tome 8`).

## Métriques vérifiées du graphe et du corpus

- **Périmètre source** : `9` fichiers `.md`, `69 821` lignes, `1 537 423` mots (`split()`), `4 542` pages PDF et `319` diagrammes.
- **Structure extraite (`CommonMark` strict)** : `4 434` titres `H1–H6` (hors `143` blocs de code clôturés filtrés), `564` identifiants normatifs et techniques uniques (`EXIG-*`, `CAP-*`, `PEX-*`, `OO1–OO4`, `T1–T10`, `PRR-75`, `C01–C40`, `L0–L4`, `DIV-02`, `SBB-*`, `G0–G5`).
- **Arbre thématique (5 niveaux)** : `380` nœuds (`1` racine, `12` domaines `D01–D12`, `36` sous-domaines, `71` familles thématiques, `260` thèmes détaillés), `1 931` occurrences ancrées aux lignes exactes.
- **Couverture & interrelations** : `616` interrelations typées sur les `8` types canoniques (`0` arête cassée, `0` auto-boucle), `290 / 290` chapitres/liminaires/annexes mappés (`0` orphelin) et `1 636` unités structurelles liées directement aux thèmes.
- **Pivots de concordance** : `5` discordances résolues (`DISC-01`..`DISC-05`, Tome 8 §0.2) + fermeture `DIV-02` (Tome 5), `86` jalons chronologiques consolidés (`2018–2035`) et `237` entrées uniques de traçabilité (`0` doublon, couvrant `95` tests exécutables Tome 8 dont `30` identifiants fusionnés : `PRR-75`, `CAP`, `C01–C40`, `EXIG`, `PEX`, `CRE-IA`, `5 SBB`, `ADR_TEMPLATE`).
- **Livrables HTML autonomes (`file://`)** :
  - [`MindMap - Cartographie thématique du Corpus.html`](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html) (`6 056 679` octets, 5 vues dont le PRD intégré, thèmes `Auto / Clair / Sombre`).
  - [`PRD - Référentiel directeur de l'entreprise agentique.html`](PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) (`2 053 782` octets, lecteur web autonome du PRD avec pont `MindMap` / `Graphe`).
- **PRD maître compilé** : [`../prd.md`](../prd.md) (`12` domaines `D01–D12`, `36` chapitres, `71` familles, `260` thèmes, `4` annexes normatives `A–D`, `4 764` lignes, `164 431` mots, `223` titres `H1–H6`).

## Les 5 vues dynamiques

1. **MindMap Thématique & Interrelations** *(vue par défaut)* : disposition **Horizontale (`G→D`)** ou **Radiale (`360°`)**, contrôle de profondeur (`Niv. 1` à `Niv. 5`), pastilles `(+N)`, projection intelligente des liens sur l'ancêtre visible, bouton **Déplier les cibles liées** et **Mode Rayon X** au clic/survol.
2. **Structure Intégrale (`9 fichiers .md`)** : exploration hiérarchique de `Corpus/README.md` et des `Tomes 1..8` jusqu'aux `4 434` sections `H1–H6` avec plages de lignes, comptage de mots, liens directs `../Corpus/<fichier>.md#Lxxx` et pastilles cliquables vers les thèmes associés.
3. **Graphe Synaptique & Explorateur de Chemins (`A → B`)** : vue réseau **Circulaire par domaine** ou **Force-directed**, filtrage d'ego-réseau (`1 saut`, `2 sauts`, `Complet`) et **calculateur de plus court chemin sémantique** détaillant chaque saut et sa justification.
4. **Concordance & Réconciliations** : carte thermique interactive `Domaines / Sous-domaines × 9 fichiers (R, T1..T8)`, fiches `DISC-01..05` et `DIV-02`, chronologie consolidée filtrable `2018–2035` (`86` jalons) et matrice cherchable unifiée (`237` entrées uniques `EXIG / CAP / PRR-75 / C01–C40 / 5 SBB / PEX / ADR`).
5. **PRD Maître** : lecteur complet du PRD (`Sommaire exécutif`, `12` Parties, `36` Chapitres, `71` Familles, `260` Thèmes, `4` Annexes `A–D`), bascule `Chapitre ciblé / Document intégral`, TDM latérale filtrable, filtres multi-facettes et pont bidirectionnel natif avec la MindMap, le Graphe et l'Inspecteur.

La barre d'outils supérieure offre une recherche plein-texte instantanée (`Ctrl+K`), `6` filtres multi-facettes (`Tome`, `Domaine`, `Autonomie`, `Rôle`, `Horizon`, `Relation`), un inspecteur latéral détaillé ainsi que l'export `SVG` et `JSON` filtré.

## Arborescence & outillage

| Fichier | Rôle |
|---|---|
| [`MindMap - Cartographie thématique du Corpus.html`](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html) | Application interactive autonome hors ligne (`file://`, 5 vues dont PRD intégré) |
| [`PRD - Référentiel directeur de l'entreprise agentique.html`](PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) | Page web autonome dédiée au PRD complet (`file://`, pont MindMap) |
| [`../prd.md`](../prd.md) | PRD maître exhaustif (`12` domaines, `36` chapitres, `71` familles, `260` thèmes, `4` annexes) |
| [`outils/extraire_structure.py`](outils/extraire_structure.py) | Parseur CommonMark strict des 9 `.md` → `structure-integrale.json` |
| [`outils/synthetiser_graphe.py`](outils/synthetiser_graphe.py) | Fusion des shards et pivots → `synthese-transversale.json` |
| [`outils/preparer_donnees_prd_web.py`](outils/preparer_donnees_prd_web.py) | Assemble la source web structurée du PRD → `prd-web-data.json` |
| [`outils/compiler_mindmap.py`](outils/compiler_mindmap.py) | Assemble `corpus-mindmap-data.json` (incluant PRD) et compile `template_mindmap.html` |
| [`outils/compiler_prd.py`](outils/compiler_prd.py) | Compile les 7 shards PRD, le schéma et les pivots vers `../prd.md` |
| [`outils/compiler_prd_web.py`](outils/compiler_prd_web.py) | Compile `prd-web-data.json` dans `template_prd_web.html` → page PRD HTML |
| [`outils/template_mindmap.html`](outils/template_mindmap.html) | Gabarit HTML/CSS/JS autonome 5 vues (`light-dark`, SVG, Node-testable) |
| [`outils/template_prd_web.html`](outils/template_prd_web.html) | Gabarit HTML/CSS/JS autonome dédié PRD (`PrdWebEngine`, Node-testable) |
| [`donnees/schema-cartographie.json`](donnees/schema-cartographie.json) | Schéma formel des 12 domaines, 8 relations et structures JSON |
| [`donnees/schema-prd-shard.json`](donnees/schema-prd-shard.json) | Schéma JSON Schema 2020-12 des shards de rédaction du PRD |
| [`donnees/pivots-concordance.json`](donnees/pivots-concordance.json) | Tables pivots (chronologie, `DISC-01..05`, `DIV-02`, `EXIG/CAP/PRR/C40/SBB`) |
| [`donnees/structure-integrale.json`](donnees/structure-integrale.json) | Arbre intégral `H1–H6` des 9 fichiers (`4 434` titres) |
| [`donnees/synthese-transversale.json`](donnees/synthese-transversale.json) | Graphe thématique unifié (`380` nœuds, `616` relations) |
| [`donnees/prd-web-data.json`](donnees/prd-web-data.json) | Données structurées du PRD web (`12/36/71/260/4`, lookup `379` nœuds) |
| [`donnees/corpus-mindmap-data.json`](donnees/corpus-mindmap-data.json) | Bundle unifié (graphe + structure + pivots + PRD) injecté dans la MindMap HTML |
| [`tests/test_cartographie.py`](tests/test_cartographie.py) | Suite `pytest` + validation syntaxique et DOM 5 vues sous `Node.js` |
| [`tests/test_prd.py`](tests/test_prd.py) | Suite `pytest` vérifiant `prd.md`, `prd-web-data.json` et la page PRD HTML |

## Commandes de régénération et de vérification

```powershell
# 1. Extraire l'arbre structurel H1–H6 des 9 fichiers de Corpus/
python Cartographie/outils/extraire_structure.py

# 2. Synthétiser le graphe transversal depuis les shards et pivots
python Cartographie/outils/synthetiser_graphe.py

# 3. Compiler le PRD maître à la racine (prd.md) et extraire prd-web-data.json
python Cartographie/outils/compiler_prd.py
python Cartographie/outils/preparer_donnees_prd_web.py

# 4. Compiler la page web autonome PRD et le bundle + MindMap 5 vues
python Cartographie/outils/compiler_prd_web.py
python Cartographie/outils/compiler_mindmap.py

# 5. Exécuter les suites complètes de tests (Cartographie + Node.js + PRD)
python -m pytest Cartographie/tests/test_cartographie.py Cartographie/tests/test_prd.py -v
```
