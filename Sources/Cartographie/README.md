# Cartographie thématique et structurelle du Compendium (`Sources/Cartographie`)

[Compendium (`Compendium/`)](../../Compendium/README.md) · [Compendium PDF](../../Compendium/Compendium.pdf) · [Compendium MD](../../Compendium/Compendium.md) · [Retour à l'index principal](../../README.md) · [Sources (`Sources/`)](../README.md) · [Sources Compendium (`Sources/Compendium/`)](../Compendium/README.md) · [Tomes (`Tomes/`)](../../Tomes/README.md) · [Ouvrir la MindMap interactive](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html) · [PRD Web autonome](PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) · [PRD maître (`../Compendium/prd.md`)](../Compendium/prd.md)

Application HTML autonome hors ligne (`file://`, sans CDN ni requête réseau externe) cartographiant l'intégralité du [**Compendium de l'entreprise agentique**](../../Compendium/README.md) ([`Compendium.md`](../../Compendium/Compendium.md) et [`Compendium.pdf`](../../Compendium/Compendium.pdf)), avec concordance historique vers les `319` figures des Tomes `1` à `8` ([`Tomes/README.md`](../../Tomes/README.md)).

## Métriques vérifiées du graphe et du Compendium

- **Périmètre source (Compendium)** : [`Compendium/Compendium.pdf`](../../Compendium/Compendium.pdf) (`837` pages, `23 175 718` octets) et [`Compendium/Compendium.md`](../../Compendium/Compendium.md) (`8 408` lignes, `241 759` mots, `1 868 863` octets, `401` titres `H1–H4`) organisés en `15` sections (`R`, `LIM`, `P01`–`P12`, `ANN`) et `42` unités éditoriales (`00-liminaire`, `ch01`–`ch36`, `annexe-a`–`annexe-e`).
- **Structure extraite (`CommonMark` strict)** : `406` titres `H1–H6` sur les `15` sections (`8 464` lignes, `242 488` mots, hors `14` blocs de code clôturés filtrés), `927` identifiants normatifs et techniques uniques (`EXIG-*`, `CAP-*`, `PEX-*`, `SCH-*`, `SRC-*`, `POR-*`, `SIG-*`, `INI-*`, `OO1–OO4`, `PRR-75`, `C01–C40`, `L0–L4`, `DIV-02`, `SBB-*`, `G0–G5`).
- **Arbre thématique (5 niveaux)** : `380` nœuds (`1` racine, `12` domaines `D01–D12`, `36` sous-domaines, `71` familles thématiques, `260` thèmes détaillés), `100 %` ancrés aux lignes exactes de `Compendium/Compendium.md`.
- **Couverture & interrelations** : `616` interrelations typées sur les `8` types canoniques (`0` arête cassée, `0` auto-boucle), `42 / 42` unités éditoriales mappées (`0` orphelin) et `1 301` unités structurelles liées directement aux thèmes (`180` cellules `12 × 15` dans la matrice de concordance).
- **Schémas, glossaire & socle probatoire** : `115` schémas compilés (`52` PlantUML `.svg`, `23` Mermaid `.png`, `40` SVG infographies), `56` vedettes du glossaire (dont **`Agentivité des systèmes`** / *system agency* rattachée à `ch01`), `135` sources `L+` hachées `SHA-256`, `27` exclusions `Statut F`, `14` extraits `CA-G0-SYNC`, `37/37` journaux Wyvern `G2`, `86` jalons chronologiques consolidés (`2018–2035`), `5` discordances résolues (`DISC-01`..`DISC-05`) + fermeture `DIV-02`, et `237` entrées uniques de traçabilité (`40` `C01–C40`).
- **Livrables HTML autonomes (`file://`)** :
  - [`MindMap - Cartographie thématique du Compendium.html`](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html) (`7 073 227` octets, `5` vues dont le PRD intégré avec `115` schémas Compendium, le glossaire des `56` vedettes et l'Annexe E, thèmes `Auto / Clair / Sombre`).
  - [`PRD - Référentiel directeur de l'entreprise agentique.html`](PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) (`4 393 858` octets, lecteur web autonome du PRD avec glossaire `56` vedettes, pont `MindMap` / `Graphe`, `115` schémas Compendium, barre de lecture collante, progression de défilement et concordance historique `319` figures).
- **PRD maître compilé** : [`../Compendium/prd.md`](../Compendium/prd.md) (`12` domaines `D01–D12`, `36` chapitres, `71` familles, `260` thèmes, `5` annexes normatives `A–E`, `115` schémas de vulgarisation raccordés aux `319` figures des Tomes, `7 560` lignes, `270 382` mots, `1 423` ancres GFM).

## Les 5 vues dynamiques

1. **MindMap Thématique & Interrelations** *(vue par défaut, ouverte à `Niv. 2`)* : disposition **Horizontale (`G→D`)** ou **Radiale (`360°`)**, contrôle de profondeur (`Niv. 1` à `Niv. 5`), pastilles `(+N)`, projection intelligente des liens sur l'ancêtre visible, bouton **Déplier les cibles liées**.
2. **Structure Intégrale (`15 sections` / `42 unités` du Compendium)** : exploration hiérarchique de `Compendium/README.md` et des `401` titres `H1–H4` de `Compendium/Compendium.md` (`8 408` lignes) avec plages de lignes, comptage de mots, liens directs `../../Compendium/Compendium.md#Lxxx` et pastilles cliquables vers les thèmes associés.
3. **Graphe Synaptique & Explorateur de Chemins (`A → B`)** : vue réseau **Circulaire par domaine** ou **Force-directed**, filtrage d'ego-réseau (`1 saut`, `2 sauts`, `Complet`) et **calculateur de plus court chemin sémantique** détaillant chaque saut et sa justification.
4. **Concordance, Glossaire & Socle probatoire** : `5` sous-onglets interactifs incluant la carte thermique `12 domaines × 15 sections` (`180` cellules, 1re colonne collante et fiche détaillée refermable), les fiches `DISC-01..05` et `DIV-02`, la chronologie filtrable `2018–2035` (`86` jalons), la matrice unifiée (`237` entrées `EXIG / CAP / PRR-75 / C01–C40 / 5 SBB / PEX / ADR`) et le registre glossaire/preuves (`56` vedettes dont **`Agentivité des systèmes`**, `135` `L+`, `27` `Statut F`, `14` `CA-G0-SYNC`, `37/37` `G2`).
5. **PRD Maître** : lecteur complet du PRD (`Sommaire exécutif` avec Panorama visuel `SCH-00`, `12` Parties, `36` Chapitres incluant `01.3–36.3 Schémas de vulgarisation`, `71` Familles, `260` Thèmes, `5` Annexes `A–E` incluant le catalogue des `115` schémas et la concordance historique des `319` figures des Tomes en blocs dépliables), barre de lecture collante (`.prd-reading-nav`), bascule `Chapitre ciblé / Document intégral`, TDM latérale par Parties repliables filtrable, filtres multi-facettes et pont bidirectionnel natif avec la MindMap, le Graphe et l'Inspecteur.

La barre d'outils supérieure offre un lien d'évitement clavier (`.skip-link`), une navigation clavier sur les onglets, une recherche plein-texte instantanée (`Ctrl+K` avec en-tête collant et badges de catégorie couvrant thèmes, glossaire et schémas), `6` filtres multi-facettes escamotables par défaut (`Section`, `Domaine`, `Autonomie`, `Rôle`, `Horizon`, `Relation`) avec bandeau de synthèse des filtres actifs (`#active-filters-strip`), un inspecteur latéral contextuel (ancrages `Compendium.md`, schémas et glossaire rattachés) ainsi que l'export `SVG` et `JSON` filtré.

## Arborescence & outillage

| Fichier | Rôle |
|---|---|
| [`MindMap - Cartographie thématique du Compendium.html`](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html) | Application interactive autonome hors ligne (`file://`, `5` vues dont PRD intégré, `7 073 227` octets) |
| [`PRD - Référentiel directeur de l'entreprise agentique.html`](PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) | Page web autonome dédiée au PRD complet (`file://`, pont MindMap et glossaire `56` vedettes, `4 393 858` octets) |
| [`../Compendium/prd.md`](../Compendium/prd.md) | PRD maître exhaustif (`12` domaines, `36` chapitres, `71` familles, `260` thèmes, `5` annexes `A–E`, `115` schémas, `7 560` lignes, `270 382` mots) |
| [`outils/extraire_structure.py`](outils/extraire_structure.py) | Parseur CommonMark strict de `Compendium/README.md` et `Compendium/Compendium.md` (`15` sections, `42` unités) → `structure-integrale.json` |
| [`outils/inventorier_schemas_compendium.py`](outils/inventorier_schemas_compendium.py) | Inventorie et vérifie sur disque les `115` schémas du Compendium (`52` PlantUML, `23` Mermaid, `40` SVG) → `inventaire-115-schemas-compendium.json` |
| [`outils/extraire_pivots_compendium.py`](outils/extraire_pivots_compendium.py) | Extrait glossaire (`56` vedettes), `135` `L+`, `27` `Statut F`, `14` `CA-G0-SYNC`, `37/37` `G2`, jalons et matrice → `pivots-concordance.json` |
| [`outils/synthetiser_graphe.py`](outils/synthetiser_graphe.py) | Assemble le graphe transversal du Compendium (`380` nœuds, `616` relations, `180` cellules) → `synthese-transversale.json` |
| [`outils/consolider_catalogue_schemas.py`](outils/consolider_catalogue_schemas.py) | Valide les `7` shards de schémas et produit `catalogue-schemas-prd.json` (`115` schémas + concordance `319` figures) |
| [`outils/compiler_prd.py`](outils/compiler_prd.py) | Compile les `7` shards PRD, le catalogue des `115` schémas, le schéma et les pivots vers `../Compendium/prd.md` |
| [`outils/preparer_donnees_prd_web.py`](outils/preparer_donnees_prd_web.py) | Assemble la source web structurée du PRD → `prd-web-data.json` |
| [`outils/compiler_mindmap.py`](outils/compiler_mindmap.py) | Assemble `corpus-mindmap-data.json` et compile `template_mindmap.html` → MindMap HTML |
| [`outils/compiler_prd_web.py`](outils/compiler_prd_web.py) | Compile `prd-web-data.json` dans `template_prd_web.html` → page PRD Web HTML |
| [`outils/inventorier_diagrammes_tomes.py`](outils/inventorier_diagrammes_tomes.py) | Inventorie les `319` diagrammes historiques des Tomes `1` à `8` pour la concordance de l'Annexe E → `inventaire-319-diagrammes.json` |
| [`outils/template_mindmap.html`](outils/template_mindmap.html) | Gabarit HTML/CSS/JS autonome `5` vues (`light-dark`, SVG, testable sous Node.js) |
| [`outils/template_prd_web.html`](outils/template_prd_web.html) | Gabarit HTML/CSS/JS autonome dédié PRD (`PrdWebEngine`, testable sous Node.js) |
| [`donnees/schema-cartographie.json`](donnees/schema-cartographie.json) | Schéma formel des `12` domaines, `8` relations et structures JSON |
| [`donnees/schema-prd-shard.json`](donnees/schema-prd-shard.json) | Schéma JSON Schema 2020-12 des `7` shards de rédaction du PRD (`prd_shards/`) |
| [`donnees/schema-prd-vulgarisation.json`](donnees/schema-prd-vulgarisation.json) | Schéma JSON Schema 2020-12 des `7` shards de schémas de vulgarisation (`prd_schemas_shards/`) |
| [`donnees/prd_shards/`](donnees/prd_shards/) | `7` shards JSON du référentiel PRD (`prd-global-et-annexes.json`, `prd-d01-d02.json`..`prd-d11-d12.json`) |
| [`donnees/prd_schemas_shards/`](donnees/prd_schemas_shards/) | `7` shards JSON des `115` schémas de vulgarisation (`schemas-global-et-annexe-e.json`, `schemas-d01-d02.json`..`schemas-d11-d12.json`) |
| [`donnees/inventaire-115-schemas-compendium.json`](donnees/inventaire-115-schemas-compendium.json) | Inventaire vérifié des `115` schémas compilés du Compendium (`52` puml, `23` mmd, `40` svg) |
| [`donnees/inventaire-319-diagrammes.json`](donnees/inventaire-319-diagrammes.json) | Inventaire historique vérifié des `319` diagrammes des Tomes `1` à `8` (concordance Annexe E) |
| [`donnees/catalogue-schemas-prd.json`](donnees/catalogue-schemas-prd.json) | Catalogue consolidé des `115` schémas (`4` `SCH-00` + `111` `SCH-01..36`) et de la couverture Tomes |
| [`donnees/pivots-concordance.json`](donnees/pivots-concordance.json) | Tables pivots (glossaire `56` vedettes, `135` `L+`, `27` `Statut F`, `14` `CA-G0-SYNC`, `37` `G2`, chronologie `86` jalons, `237` entrées) |
| [`donnees/structure-integrale.json`](donnees/structure-integrale.json) | Arbre intégral `H1–H6` des `15` sections / `42` unités du Compendium (`406` titres dont `401` dans `Compendium.md`) |
| [`donnees/synthese-transversale.json`](donnees/synthese-transversale.json) | Graphe thématique unifié (`380` nœuds, `616` relations, `1 301` unités structurelles liées) |
| [`donnees/prd-web-data.json`](donnees/prd-web-data.json) | Données structurées du PRD web (`5 710 649` octets : `12/36/71/260/5`, `115` schémas, `56` vedettes, concordance `319` figures) |
| [`donnees/corpus-mindmap-data.json`](donnees/corpus-mindmap-data.json) | Bundle unifié (`9 732 561` octets : graphe + structure + pivots + PRD) injecté dans la MindMap HTML |
| [`tests/test_cartographie.py`](tests/test_cartographie.py) | Suite `pytest` + validation syntaxique et DOM `5` vues sous `Node.js` |
| [`tests/test_prd.py`](tests/test_prd.py) | Suite `pytest` vérifiant `prd.md`, `prd-web-data.json`, glossaire, schémas `115`/`319` et page PRD Web HTML |

## Commandes de régénération et de vérification

```powershell
# 1. Extraire la structure Compendium, inventorier les 115 schémas et extraire les pivots
python -B Sources/Cartographie/outils/extraire_structure.py
python -B Sources/Cartographie/outils/inventorier_schemas_compendium.py
python -B Sources/Cartographie/outils/extraire_pivots_compendium.py

# 2. Synthétiser le graphe transversal et consolider le catalogue des 115 schémas PRD
python -B Sources/Cartographie/outils/synthetiser_graphe.py
python -B Sources/Cartographie/outils/consolider_catalogue_schemas.py

# 3. Compiler le PRD maître (Sources/Compendium/prd.md) et extraire prd-web-data.json
python -B Sources/Cartographie/outils/compiler_prd.py
python -B Sources/Cartographie/outils/preparer_donnees_prd_web.py

# 4. Compiler la MindMap 5 vues et la page web autonome PRD
python -B Sources/Cartographie/outils/compiler_mindmap.py
python -B Sources/Cartographie/outils/compiler_prd_web.py

# (Optionnel : réactualiser la concordance historique des 319 figures des Tomes 1–8)
python -B Sources/Cartographie/outils/inventorier_diagrammes_tomes.py

# 5. Exécuter les suites complètes de tests (Cartographie + Node.js + PRD + Schémas)
python -B -m pytest -p no:cacheprovider Sources/Cartographie/tests -q
```
