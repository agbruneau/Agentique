# Composants sources et fabrique éditoriale (`Sources`)

[Index principal du dépôt](../README.md) · [Compendium publié (`../Compendium/`)](../Compendium/README.md) · [Archive des Tomes (`../Tomes/`)](../Tomes/README.md) · [MindMap HTML](Cartographie/MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html)

Ce répertoire regroupe tous les **composants sources, schémas, données cartographiques et outils de compilation** servant à produire, assembler et vérifier l'ouvrage maître [**Interopérabilité et automatisation agentique des systèmes d'entreprise**](../Compendium/README.md) ([`Compendium.pdf`](../Compendium/Compendium.pdf), [`Compendium.md`](../Compendium/Compendium.md)), tout en conservant l'archive source figée des huit tomes dans [`Tomes/`](Tomes/README.md).

## Organisation des 4 sous-dossiers

| Sous-dossier | Rôle dans la chaîne éditoriale | Cible publiée |
|---|---|---|
| [`Compendium/`](Compendium/README.md) | Usine éditoriale [`ouvrage/`](Compendium/ouvrage/) du traité *Interopérabilité et automatisation agentique des systèmes d'entreprise* (`12` parties `D01–D12`, `36` chapitres, `5` annexes `A–E`, `7` registres SSOT, `139` schémas et barrières `Wyvern G0–G5`) | [`../Compendium/`](../Compendium/README.md) (`Compendium.pdf`, `Compendium.md`) |
| [`Tomes/`](Tomes/README.md) | **Archive source figée en lecture seule** des **Tomes 1 à 8** (`319` diagrammes `.puml`/`.mmd` et rendus `.svg`/`.png`, ateliers des tomes 7–8, et trousse logicielle exécutable [`Tome 8.../trousse/`](Tomes/Tome%208%20-%20Ing%C3%A9nierie%20ex%C3%A9cutable%20et%20homologation%20v%C3%A9rifiable/trousse/README.md) consommée en lecture seule par `G0` / `CA-G0-SYNC`) | [`../Tomes/`](../Tomes/README.md) (`Tome 1..8.{pdf,md}`) |
| [`Cartographie/`](Cartographie/README.md) | Graphe thématique transversal du traité maître (`15` sections, `42` unités, `380` nœuds, `616` interrelations, `56` vedettes du glossaire, `5` parcours guidés) et [`MindMap HTML`](Cartographie/MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Compendium.html) autonome hors ligne (`4` vues) | [`Cartographie/`](Cartographie/README.md) et MindMap HTML autonome |
| [`gabarit-pdf/`](gabarit-pdf/README.md) | Gabarit `Typst` unifié `6,14 × 9,21 po` ([`gabarit-collection.typ`](gabarit-pdf/gabarit-collection.typ)), catalogue [`volumes.json`](gabarit-pdf/volumes.json) couvrant l'ouvrage maître (`0`) et les Tomes historiques (`1`–`8`), et scripts de compilation PDF/diagrammes | [`../Compendium/`](../Compendium/README.md) et [`../Tomes/`](../Tomes/README.md) |

## Commandes PowerShell rapides de recompilation PDF et Markdown

Exécuter depuis la racine du dépôt (`Agentique/`, une commande par ligne sous Windows PowerShell `5.1`) :

```powershell
# Lister les 9 volumes catalogués (Compendium [0] et Tomes historiques [1] à [8])
python -B Sources/gabarit-pdf/compile_pdf.py --list

# Réassembler et compiler l'ouvrage maître « Interopérabilité et automatisation agentique des systèmes d'entreprise » (Compendium.md + Compendium.pdf)
python -B Sources/Compendium/ouvrage/outils/assemble_livre.py --all

# Recompiler le PDF du Volume 0 via le compilateur générique Typst (équivalent métadonnées volumes.json)
python -B Sources/gabarit-pdf/compile_pdf.py --volume 0 --in-place

# (Archive historique figée : ne pas régénérer les Tomes 1–8 ni leurs 319 diagrammes lors des mises à jour du Compendium)

# Régénération intégrale de Cartographie/ et de la MindMap HTML 4 vues (dans l'ordre topologique exact en 6 étapes)
python -B Sources/Cartographie/outils/extraire_structure.py
python -B Sources/Cartographie/outils/inventorier_schemas_compendium.py
python -B Sources/Cartographie/outils/extraire_pivots_compendium.py
python -B Sources/Cartographie/outils/consolider_catalogue_schemas.py
python -B Sources/Cartographie/outils/synthetiser_graphe.py
python -B Sources/Cartographie/outils/compiler_mindmap.py
```

## Vérifications rapides

```powershell
python -B Sources/Compendium/ouvrage/outils/verifie_specs.py
python -B Sources/Compendium/ouvrage/outils/collecte_mlr_ouverte.py --verify
python -B Sources/Compendium/ouvrage/outils/execute_g0.py --verify-sync-manifest --output "$env:TEMP\rapports-g0.json"
python -B Sources/Compendium/ouvrage/outils/compile_schemas_compendium.py --check-only
python -B Sources/Compendium/ouvrage/outils/verifie_manuscrit.py --strict --check-deliverables
python -B -m pytest -p no:cacheprovider Sources/Compendium/ouvrage/outils -q
python -B -m pytest -p no:cacheprovider Sources/Cartographie/tests -q
python -B -m pytest -p no:cacheprovider Sources/gabarit-pdf/test_gabarit_pdf.py -q
```

Pour exécuter en lecture seule les suites hors ligne de la trousse compagnon (`pytest`, politiques `OPA / Rego` et vecteurs tiers), consulter [`Sources/Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/README.md`](Tomes/Tome%208%20-%20Ing%C3%A9nierie%20ex%C3%A9cutable%20et%20homologation%20v%C3%A9rifiable/trousse/README.md).
