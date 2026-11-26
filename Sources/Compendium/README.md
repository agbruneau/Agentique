# Sources du Compendium (`Sources/Compendium/`)

[Accueil du dépôt](../../README.md) · [Compendium publié (`../../Compendium/`)](../../Compendium/README.md) · [Tomes publiés (`../../Tomes/`)](../../Tomes/README.md) · [Index des sources (`../`)](../README.md) · [Cartographie (`../Cartographie/`)](../Cartographie/README.md) · [Référentiel directeur (`prd.md`)](prd.md) · [PRD Web](../Cartographie/PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) · [MindMap HTML](../Cartographie/MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html)

Ce répertoire regroupe les spécifications maîtresses (`prd.md`) et l'usine éditoriale `ouvrage/` qui produit, vérifie et publie le **Compendium de l'entreprise agentique** vers [`../../Compendium/Compendium.pdf`](../../Compendium/Compendium.pdf) et [`../../Compendium/Compendium.md`](../../Compendium/Compendium.md).

---

## Contenu du répertoire

- [**`prd.md`**](prd.md) : référentiel directeur d'exigences produit, d'architecture et d'homologation (`12` domaines `D01–D12`, `36` chapitres, `71` familles, `260` thèmes, `5` annexes `A–E`, `115` schémas de vulgarisation raccordés aux `319` diagrammes des Tomes `1` à `8`, `7 560` lignes, `270 382` mots).
- **`ouvrage/`** : atelier complet de rédaction, d'ancrage probatoire et d'assemblage publiant vers [`../../Compendium/`](../../Compendium/README.md) :
  - `specs/` : manifeste normatif (`manifest.json`, `42` unités, `180 000` mots cibles) et protocole de collecte ouverte (`protocole-mlr-compendium.json`, gel au `2 décembre 2026`).
  - `manuscrit/` : `00 - Liminaire.md`, `12` parties (`36` chapitres) et `5` annexes déterministes (`13 - Annexes/Annexe A..E.md`).
  - `schemas/` : `115` sources iconographiques (`52` `.puml`, `23` `.mmd`, `40` `.svg`) et leurs rendus compilés sous `schemas/rendus/`.
  - `sources/` et `recherche/` : `37` bases documentaires fermées (`ch00..ch36-sources.md`), corpus primaire ouvert `L+` haché `SHA-256` et registre d'exclusions `Statut F`.
  - `registre/` : `7` registres JSON SSOT (`mindmap-complet.json`, `specifications-lplus.json`, `matrice-exig-prr-c40.json`, `concordance-taxonomies.json`, `ancres-chronologiques.json`, `faits-empiriques.json`, `glossaire-termes.json` à `56` vedettes dont **`Agentivité des systèmes`**).
  - `ancrage/` et `aq/` : `37` journaux d'audit atomique `G2`, rapport `G0` (`rapports-g0.json`), doubles recollations `G3`, journaux `G4`/`G5`.
  - `outils/` : `14` fichiers — `9` scripts Python déterministes (`_communs.py`, `verifie_specs.py`, `collecte_mlr_ouverte.py`, `compile_schemas_compendium.py`, `execute_g0.py`, `genere_annexes.py`, `echantillon_aq.py`, `verifie_manuscrit.py`, `assemble_livre.py`) et `5` suites `pytest` totalisant `43` tests (`test_collecte_mlr.py`, `test_compile_schemas.py`, `test_execute_g0.py`, `test_outillage_aq.py`, `test_verifie_specs.py`).

---

## Livrables publiés (`../../Compendium/`)

- [`Compendium.pdf`](../../Compendium/Compendium.pdf) : `837` pages (`Typst 6,14 × 9,21 po`, `23 175 718` octets).
- [`Compendium.md`](../../Compendium/Compendium.md) : édition Markdown consolidée (`1 868 863` octets, `8 408` lignes, `241 759` mots, `42` unités, `115` figures).

---

## Commandes de validation et de publication

Exécuter depuis la racine du dépôt (`-B` et `-p no:cacheprovider` évitent la génération de caches ; ajouter `--output <chemin-temporaire.json>` à `execute_g0.py` pour ne pas modifier l'horodatage de `aq/rapports-g0.json`) :

```powershell
python -B Sources/Compendium/ouvrage/outils/verifie_specs.py
python -B Sources/Compendium/ouvrage/outils/compile_schemas_compendium.py --check-only
python -B Sources/Compendium/ouvrage/outils/execute_g0.py --verify-sync-manifest --output "$env:TEMP\rapports-g0.json"
python -B Sources/Compendium/ouvrage/outils/genere_annexes.py
python -B Sources/Compendium/ouvrage/outils/assemble_livre.py --all
python -B Sources/Compendium/ouvrage/outils/verifie_manuscrit.py --strict --check-deliverables
python -B -m pytest -p no:cacheprovider Sources/Compendium/ouvrage/outils -q
```
