# Cartographie thématique et structurelle du Compendium (`Sources/Cartographie`)

[Compendium (`Compendium/`)](../../Compendium/README.md) · [Compendium PDF](../../Compendium/Compendium.pdf) · [Compendium MD](../../Compendium/Compendium.md) · [Retour à l'index principal](../../README.md) · [Sources (`Sources/`)](../README.md) · [Sources Compendium (`Sources/Compendium/`)](../Compendium/README.md) · [Tomes (`Tomes/`)](../../Tomes/README.md) · [Ouvrir la MindMap interactive](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html)

Application HTML autonome hors ligne (`file://`, sans CDN ni requête réseau externe) cartographiant l'intégralité du traité unifié [**Interopérabilité et automatisation agentique des systèmes d'entreprise**](../../Compendium/README.md) ([`Compendium.md`](../../Compendium/Compendium.md) et [`Compendium.pdf`](../../Compendium/Compendium.pdf)), avec concordance historique figée vers les `319` figures des Tomes `1` à `8` ([`Tomes/README.md`](../../Tomes/README.md)). Le nom du livrable [`MindMap - Cartographie thématique du Compendium.html`](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html) et la clé `localStorage` `agy_compendium_reading_v1` sont maintenus stables pour préserver les liens croisés du dépôt et le suivi de lecture existant.

## Métriques vérifiées du graphe et du Compendium

- **Périmètre source (Compendium)** : [`Compendium/Compendium.pdf`](../../Compendium/Compendium.pdf) (`872` pages, `25 300 905` octets) et [`Compendium/Compendium.md`](../../Compendium/Compendium.md) (`8 638` lignes, `247 581` mots, `1 924 974` octets, `404` titres `H1–H4`) organisés en `15` sections (`R`, `LIM`, `P01`–`P12`, `ANN`) et `42` unités éditoriales (`00-liminaire`, `ch01`–`ch36`, `annexe-a`–`annexe-e`).
- **Structure extraite (`CommonMark` strict)** : `409` titres `H1–H6` sur les `15` sections (`8 695` lignes, `248 511` mots, hors `14` blocs de code clôturés filtrés), `952` identifiants normatifs et techniques uniques (`EXIG-*`, `CAP-*`, `PEX-*`, `SCH-*`, `SRC-*`, `POR-*`, `SIG-*`, `INI-*`, `OO1–OO4`, `PRR-75`, `C01–C40`, `L0–L4`, `DIV-02`, `SBB-*`, `G0–G5`).
- **Arbre thématique (5 niveaux)** : `380` nœuds (`1` racine, `12` domaines `D01–D12`, `36` sous-domaines, `71` familles thématiques, `260` thèmes détaillés), `100 %` ancrés aux lignes exactes de `Compendium/Compendium.md` et aux pages de `Compendium/Compendium.pdf`.
- **Couverture & interrelations** : `616` interrelations typées sur les `8` types canoniques (`0` arête cassée, `0` auto-boucle), `42 / 42` unités éditoriales mappées (`0` orphelin) et `1 301` unités structurelles liées directement aux thèmes (`180` cellules `12 × 15` dans la matrice de concordance).
- **Schémas, glossaire & socle probatoire** : `139` schémas compilés (`58` PlantUML `.svg`, `23` Mermaid `.png`, `58` SVG infographies), `56` vedettes du glossaire (incluant **`Automatisation agentique`**, **`Continuum d'automatisation`**, **`Système d'entreprise`** et **`Agentivité des systèmes`** / *system agency*), `135` sources `L+` hachées `SHA-256`, `27` exclusions `Statut F`, `14` extraits `CA-G0-SYNC`, `37/37` journaux Wyvern `G2`, `77` jalons chronologiques consolidés (`2018–2035`), `5` discordances résolues (`DISC-01`..`DISC-05`) + fermeture `DIV-02`, et `237` entrées uniques de traçabilité (`40` `C01–C40`).
- **Cinq parcours de lecture guidés par rôle** :
  1. `essentiel` (*Parcours Essentiel — Interopérabilité, 80/20 & Systèmes d'entreprise*, `7` unités) ;
  2. `ae-strategie` (*Architecte d'Entreprise (AE) — Systèmes d'entreprise, Anti-verrouillage & Portefeuille*, `9` unités) ;
  3. `as-ingenierie` (*Architecte de Solutions (AS) — Interopérabilité MCP/A2A, Patrimoine & Automatisation Saga*, `11` unités) ;
  4. `rssi-securite` (*RSSI & Sécurité — Identité NHI, Passerelles PEP & Sûreté des systèmes d'entreprise*, `9` unités) ;
  5. `juridique-2035` (*Juridique, Conformité & Homologation vérifiable des systèmes d'entreprise*, `9` unités).

## Les 4 vues dynamiques

1. **MindMap Thématique & Interrelations** *(vue par défaut, ouverte à `Niv. 2`)* : disposition **Horizontale (`G→D`)** ou **Radiale (`360°`)**, contrôle de profondeur (`Niv. 1` à `Niv. 5`), pastilles `(+N)`, projection intelligente des liens sur l'ancêtre visible, bouton **Déplier les cibles liées** et accès direct au Compendium (`PDF p. N`, *Question directrice*, extrait et sous-sections) dès `Niv. 2–4`.
2. **Structure Intégrale (`15 sections` / `42 unités` du Compendium)** : exploration hiérarchique de `Compendium/README.md` et des titres `H1–H4` de `Compendium/Compendium.md` avec plages de pages PDF (`p. X–Y`), durée estimée (`~min`), plages de lignes, liens directs `Compendium.pdf#page=N` et `../../Compendium/Compendium.md#Lxxx`, filtre d'état de lecture (`Toutes / À lire / Lues`) et pastilles cliquables vers les thèmes associés.
3. **Graphe Synaptique & Explorateur de Chemins (`A → B`)** : vue réseau **Circulaire par domaine** ou **Force-directed**, filtrage d'ego-réseau (`1 saut`, `2 sauts`, `Complet`) et **calculateur de plus court chemin sémantique** détaillant chaque saut et sa justification.
4. **Concordance, Glossaire & Socle probatoire** : `6` sous-onglets interactifs incluant la carte thermique `12 domaines × 15 sections` (`180` cellules avec pont *Filtrer dans la MindMap*), les fiches `DISC-01..05` et `DIV-02`, la chronologie filtrable `2018–2035` (`77` jalons), la matrice unifiée (`237` entrées ancrées sur le Compendium), le registre glossaire/preuves (`56` vedettes, `135` `L+`, `27` `Statut F`, `14` `CA-G0-SYNC`, `37/37` `G2`) et la **Galerie des `139` schémas** avec visionneuse modale.

## Arborescence & outillage

| Fichier | Rôle |
|---|---|
| [`MindMap - Cartographie thématique du Compendium.html`](MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html) | Application interactive autonome hors ligne (`file://`, `4` vues, `4 270 301` octets) |
| [`outils/index_pdf_compendium.py`](outils/index_pdf_compendium.py) | Indexeur PDF `pymupdf` alignant les titres hors TDM et les `139` schémas sur les signets et pages de `Compendium/Compendium.pdf` |
| [`outils/extraire_structure.py`](outils/extraire_structure.py) | Parseur CommonMark strict de `Compendium/README.md` et `Compendium/Compendium.md` (`15` sections, `42` unités) → `structure-integrale.json` |
| [`outils/inventorier_schemas_compendium.py`](outils/inventorier_schemas_compendium.py) | Inventorie et vérifie sur disque les `139` schémas du Compendium (`58` PlantUML, `23` Mermaid, `58` SVG) → `inventaire-139-schemas-compendium.json` |
| [`outils/extraire_pivots_compendium.py`](outils/extraire_pivots_compendium.py) | Extrait glossaire (`56` vedettes), `135` `L+`, `27` `Statut F`, `14` `CA-G0-SYNC`, `37/37` `G2`, jalons et matrice → `pivots-concordance.json` |
| [`outils/consolider_catalogue_schemas.py`](outils/consolider_catalogue_schemas.py) | Valide les `7` shards PRD de schémas et produit `catalogue-schemas-prd.json` (`139` schémas + concordance `319` figures pour l'Annexe E) |
| [`outils/synthetiser_graphe.py`](outils/synthetiser_graphe.py) | Assemble le graphe transversal du Compendium (`380` nœuds, `616` relations, `180` cellules) → `synthese-transversale.json` |
| [`outils/compiler_mindmap.py`](outils/compiler_mindmap.py) | Assemble `corpus-mindmap-data.json`, construit les `5` parcours guidés et compile `template_mindmap.html` → MindMap HTML |
| [`outils/inventorier_diagrammes_tomes.py`](outils/inventorier_diagrammes_tomes.py) | Utilitaire d'inventaire historique des `319` diagrammes des Tomes `1` à `8` (`inventaire-319-diagrammes.json`, gelé en lecture seule) |
| [`outils/template_mindmap.html`](outils/template_mindmap.html) | Gabarit HTML/CSS/JS autonome `4` vues (`light-dark`, SVG, testable sous Node.js) |
| [`donnees/schema-cartographie.json`](donnees/schema-cartographie.json) | Schéma formel des `12` domaines, `15` sections, `8` types de relations et invariants JSON |
| [`donnees/schema-prd-vulgarisation.json`](donnees/schema-prd-vulgarisation.json) | Schéma JSON Schema 2020-12 des `7` shards de schémas (`prd_schemas_shards/`) |
| [`donnees/prd_schemas_shards/`](donnees/prd_schemas_shards/) | `7` shards JSON des `139` schémas (`schemas-global-et-annexe-e.json`, `schemas-d01-d02.json`..`schemas-d11-d12.json`) |
| [`donnees/inventaire-139-schemas-compendium.json`](donnees/inventaire-139-schemas-compendium.json) | Inventaire vérifié des `139` schémas compilés du Compendium (`58` puml, `23` mmd, `58` svg) |
| [`donnees/inventaire-319-diagrammes.json`](donnees/inventaire-319-diagrammes.json) | Inventaire historique scellé des `319` diagrammes des Tomes `1` à `8` (concordance Annexe E, ne pas régénérer) |
| [`donnees/catalogue-schemas-prd.json`](donnees/catalogue-schemas-prd.json) | Catalogue consolidé des `139` schémas (`5` `SCH-00` + `131` `SCH-01..36` + `3` Annexes) et de la couverture Tomes |
| [`donnees/pivots-concordance.json`](donnees/pivots-concordance.json) | Tables pivots (glossaire `56` vedettes, `135` `L+`, `27` `Statut F`, `14` `CA-G0-SYNC`, `37` `G2`, chronologie `77` jalons, `237` entrées) |
| [`donnees/structure-integrale.json`](donnees/structure-integrale.json) | Arbre intégral `H1–H6` des `15` sections / `42` unités du Compendium |
| [`donnees/synthese-transversale.json`](donnees/synthese-transversale.json) | Graphe thématique unifié (`380` nœuds, `616` relations, occurrences vérifiées dans `Compendium.md`) |
| [`donnees/corpus-mindmap-data.json`](donnees/corpus-mindmap-data.json) | Bundle unifié (`5 454 367` octets : graphe + structure + pivots + schémas + parcours) injecté dans la MindMap HTML |
| [`tests/test_cartographie.py`](tests/test_cartographie.py) | Suite `pytest` (`12` tests) + validation syntaxique et DOM `4` vues sous `Node.js` |

## Commandes de régénération et de vérification

Exécuter dans l'ordre topologique exact depuis la racine du dépôt :

```powershell
# 1. Extraire la structure Compendium, inventorier les 139 schémas et extraire les pivots
python -B Sources/Cartographie/outils/extraire_structure.py
python -B Sources/Cartographie/outils/inventorier_schemas_compendium.py
python -B Sources/Cartographie/outils/extraire_pivots_compendium.py

# 2. Consolider le catalogue des 139 schémas (Annexe E) et synthétiser le graphe transversal
python -B Sources/Cartographie/outils/consolider_catalogue_schemas.py
python -B Sources/Cartographie/outils/synthetiser_graphe.py

# 3. Compiler le bundle et la MindMap HTML 4 vues
python -B Sources/Cartographie/outils/compiler_mindmap.py

# 4. Exécuter la suite complète de tests (12/12 pytest + smoke-tests DOM Node.js)
python -B -m pytest -p no:cacheprovider Sources/Cartographie/tests -q
```
