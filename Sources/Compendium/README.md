# Sources de l'ouvrage maître (`Sources/Compendium/`)

[Accueil du dépôt](../../README.md) · [Compendium publié (`../../Compendium/`)](../../Compendium/README.md) · [Archive des Tomes (`../../Tomes/`)](../../Tomes/README.md) · [Index des sources (`../`)](../README.md) · [Cartographie (`../Cartographie/`)](../Cartographie/README.md) · [MindMap HTML](../Cartographie/MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html)

Ce répertoire abrite l'usine éditoriale `ouvrage/` qui produit, vérifie et publie le traité unifié **Interopérabilité et automatisation agentique des systèmes d'entreprise** — *Traité unifié d'architecture hybride, de gouvernance hors modèle et d'homologation vérifiable (non-avis)* — vers les livrables canoniques [`../../Compendium/Compendium.pdf`](../../Compendium/Compendium.pdf) et [`../../Compendium/Compendium.md`](../../Compendium/Compendium.md).

---

## Contenu du répertoire

- **`ouvrage/`** : atelier complet de spécification, de rédaction, d'ancrage probatoire et d'assemblage publiant vers [`../../Compendium/`](../../Compendium/README.md) :
  - `specs/` : manifeste normatif (`manifest.json`, titre directeur de `70` caractères, sous-titre `(non-avis)` de `104` caractères, `12` `part_titles`, `42` unités, budget cible `180 000` mots `± 8 %`) et protocole de collecte ouverte (`protocole-mlr-compendium.json`, gel au `2 décembre 2026`).
  - `manuscrit/` : `00 - Liminaire.md`, `12` parties (`36` chapitres `D01`–`D12`) et `5` annexes déterministes (`13 - Annexes/Annexe A..E.md` générées sans édition manuelle par `outils/genere_annexes.py`).
  - `schemas/` : `139` sources iconographiques (`58` `.puml`, `23` `.mmd`, `58` `.svg`) et leurs rendus compilés sous `schemas/rendus/`.
  - `sources/` et `recherche/` : `37` bibliographies fermées (`ch00..ch36-sources.md`), corpus primaire ouvert de `135` sources `L+` hachées `SHA-256` et registre de `27` exclusions `Statut F`.
  - `registre/` : `7` registres JSON SSOT (`mindmap-complet.json` à `380` nœuds et `616` relations, `specifications-lplus.json` à `57` entrées, `matrice-exig-prr-c40.json` à `305 EXIG-*` et `52 CAP` dont `42` invariantes, `concordance-taxonomies.json`, `ancres-chronologiques.json` à `77` jalons uniques, `faits-empiriques.json` à `16` faits, `glossaire-termes.json` à `56` vedettes incluant **`Automatisation agentique`**, **`Continuum d'automatisation`**, **`Système d'entreprise`** et **`Agentivité des systèmes`**).
  - `ancrage/` et `aq/` : `37` journaux d'audit atomique `G2`, rapport `G0` (`rapports-g0.json` scellant `14/14` extraits `CA-G0-SYNC` sur `Tome 8/trousse/`), doubles recollations `G3` (`148 × 2`), journaux `G4`/`G5`.
  - `outils/` : `14` fichiers — `9` scripts Python déterministes (`_communs.py`, `verifie_specs.py`, `collecte_mlr_ouverte.py`, `compile_schemas_compendium.py`, `execute_g0.py`, `genere_annexes.py`, `echantillon_aq.py`, `verifie_manuscrit.py`, `assemble_livre.py`) et `5` suites `pytest` totalisant `43` tests (`test_collecte_mlr.py`, `test_compile_schemas.py`, `test_execute_g0.py`, `test_outillage_aq.py`, `test_verifie_specs.py`).

---

## Livrables publiés (`../../Compendium/`)

- [`Compendium.pdf`](../../Compendium/Compendium.pdf) : `872` pages (`Typst 6,14 × 9,21 po`, `25 300 905` octets).
- [`Compendium.md`](../../Compendium/Compendium.md) : édition Markdown consolidée (`1 924 974` octets, `8 638` lignes, `247 581` mots totaux, `183 655` mots de prose `CA-01`, `42` unités, `37` bibliographies, `139` figures).

---

## Commandes de validation et de publication

Exécuter depuis la racine du dépôt (`-B` et `-p no:cacheprovider` évitent la génération de caches ; ajouter `--output <chemin-temporaire.json>` à `execute_g0.py` pour ne pas modifier l'horodatage de `aq/rapports-g0.json`) :

```powershell
python -B Sources/Compendium/ouvrage/outils/verifie_specs.py
python -B Sources/Compendium/ouvrage/outils/collecte_mlr_ouverte.py --verify
python -B Sources/Compendium/ouvrage/outils/compile_schemas_compendium.py --check-only
python -B Sources/Compendium/ouvrage/outils/execute_g0.py --verify-sync-manifest --output "$env:TEMP\rapports-g0.json"
python -B Sources/Compendium/ouvrage/outils/genere_annexes.py
python -B Sources/Compendium/ouvrage/outils/assemble_livre.py --all
python -B Sources/Compendium/ouvrage/outils/verifie_manuscrit.py --strict --check-deliverables
python -B -m pytest -p no:cacheprovider Sources/Compendium/ouvrage/outils -q
```
