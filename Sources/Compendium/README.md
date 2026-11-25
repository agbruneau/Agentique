# Sources du Compendium (`Sources/Compendium/`)

[Accueil du dépôt](../../README.md) · [Compendium publié (`../../Compendium/`)](../../Compendium/README.md) · [Tomes publiés (`../../Tomes/`)](../../Tomes/README.md) · [Index des sources (`../`)](../README.md) · [Cartographie (`../Cartographie/`)](../Cartographie/README.md) · [Référentiel directeur (`prd.md`)](prd.md) · [PRD Web](../Cartographie/PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) · [MindMap HTML](../Cartographie/MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html)

Ce répertoire regroupe les spécifications maîtresses (`prd.md`) et l'usine éditoriale `ouvrage/` qui produit, vérifie et publie le **Compendium de l'entreprise agentique** vers [`../../Compendium/Compendium.pdf`](../../Compendium/Compendium.pdf) et [`../../Compendium/Compendium.md`](../../Compendium/Compendium.md).

---

## Contenu du répertoire

- [**`prd.md`**](prd.md) : référentiel directeur d'exigences produit, d'architecture et d'homologation (`12` domaines `D01–D12`, `36` chapitres, `71` familles, `260` thèmes, `5` annexes `A–E`, `115` schémas de vulgarisation raccordés aux `319` diagrammes des Tomes `1` à `8`).
- **`ouvrage/`** : atelier complet de rédaction, d'ancrage probatoire et d'assemblage publiant vers [`../../Compendium/`](../../Compendium/README.md) :
  - `specs/` : manifeste normatif (`manifest.json`, `42` unités, `180 000` mots cibles) et protocole de collecte ouverte (`protocole-mlr-compendium.json`, gel au `2 décembre 2026`).
  - `manuscrit/` : `00 - Liminaire.md`, `12` parties (`36` chapitres) et `5` annexes déterministes (`13 - Annexes/Annexe A..E.md`).
  - `schemas/` : `115` sources iconographiques (`52` `.puml`, `23` `.mmd`, `40` `.svg`) et leurs rendus compilés sous `schemas/rendus/`.
  - `sources/` et `recherche/` : `37` bases documentaires fermées (`ch00..ch36-sources.md`), corpus primaire ouvert `L+` haché `SHA-256` et registre d'exclusions `Statut F`.
  - `registre/` : `7` registres JSON SSOT (`mindmap-complet.json`, `specifications-lplus.json`, `matrice-exig-prr-c40.json`, `concordance-taxonomies.json`, `ancres-chronologiques.json`, `faits-empiriques.json`, `glossaire-termes.json`).
  - `ancrage/` et `aq/` : `37` journaux d'audit atomique `G2`, rapport `G0` (`rapports-g0.json`), doubles recollations `G3`, journaux `G4`/`G5`.
  - `outils/` : scripts Python déterministes d'inspection, de génération et d'assemblage (`verifie_specs.py`, `compile_schemas_compendium.py`, `execute_g0.py`, `genere_annexes.py`, `assemble_livre.py`, `verifie_manuscrit.py`) et leur suite `pytest`.

---

## Livrables publiés (`../../Compendium/`)

- [`Compendium.pdf`](../../Compendium/Compendium.pdf) : `834` pages (`Typst 6,14 × 9,21 po`, `23 122 392` octets).
- [`Compendium.md`](../../Compendium/Compendium.md) : édition Markdown consolidée (`1 859 417` octets, `8 362` lignes, `42` unités, `115` figures).

---

## Commandes de validation et de publication

Exécuter depuis la racine du dépôt (`-B` et `-p no:cacheprovider` évitent la génération de caches) :

```powershell
python -B Sources/Compendium/ouvrage/outils/verifie_specs.py
python -B Sources/Compendium/ouvrage/outils/compile_schemas_compendium.py --check-only
python -B Sources/Compendium/ouvrage/outils/genere_annexes.py
python -B Sources/Compendium/ouvrage/outils/assemble_livre.py --all
python -B Sources/Compendium/ouvrage/outils/verifie_manuscrit.py --strict --check-deliverables
python -B -m pytest -p no:cacheprovider Sources/Compendium/ouvrage/outils -q
```
