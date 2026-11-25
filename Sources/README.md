# Composants sources et fabrique éditoriale (`Sources`)

[Index principal du dépôt](../README.md) · [Compendium publié (`../Compendium/`)](../Compendium/README.md) · [Tomes publiés (`../Tomes/`)](../Tomes/README.md) · [PRD maître](Compendium/prd.md) · [PRD Web](Cartographie/PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) · [MindMap HTML](Cartographie/MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html)

Ce répertoire regroupe tous les **composants sources, schémas, données cartographiques et outils de compilation** servant à fabriquer, assembler et vérifier les PDF publiés et leurs fichiers Markdown correspondants dans [`../Compendium/`](../Compendium/README.md) et [`../Tomes/`](../Tomes/README.md).

## Organisation des 4 sous-dossiers

| Sous-dossier | Rôle dans la chaîne éditoriale | Cible publiée |
|---|---|---|
| [`Compendium/`](Compendium/README.md) | Référentiel directeur [`prd.md`](Compendium/prd.md) et usine éditoriale [`ouvrage/`](Compendium/ouvrage/) (`12` parties, `36` chapitres, `5` annexes `A–E`, `115` schémas de vulgarisation et contrôles AQ `G0`–`G5`) | [`../Compendium/`](../Compendium/README.md) (`Compendium.pdf`, `Compendium.md`) |
| [`Tomes/`](Tomes/README.md) | Dossiers sources des **Tomes 1 à 8** (chapitres découpés, `319` diagrammes `.puml`/`.mmd` et rendus `.svg`/`.png`, spécifications et AQ des tomes 7–8, et trousse logicielle exécutable [`Tome 8.../trousse/`](Tomes/Tome%208%20-%20Ing%C3%A9nierie%20ex%C3%A9cutable%20et%20homologation%20v%C3%A9rifiable/trousse/README.md)) | [`../Tomes/`](../Tomes/README.md) (`Tome 1..8.{pdf,md}`) |
| [`Cartographie/`](Cartographie/README.md) | Graphe thématique transversal (`380` nœuds, `616` interrelations), compilateur du [`prd.md`](Compendium/prd.md), [`MindMap HTML`](Cartographie/MindMap%20-%20Cartographie%20th%C3%A9matique%20du%20Corpus.html) et [`PRD Web`](Cartographie/PRD%20-%20R%C3%A9f%C3%A9rentiel%20directeur%20de%20l%27entreprise%20agentique.html) autonomes hors ligne | [`Sources/Compendium/prd.md`](Compendium/prd.md) et vues HTML autonomes |
| [`gabarit-pdf/`](gabarit-pdf/README.md) | Gabarit `Typst` unifié `6,14 × 9,21 po` ([`gabarit-collection.typ`](gabarit-pdf/gabarit-collection.typ)), catalogue [`volumes.json`](gabarit-pdf/volumes.json) couvrant le Compendium (`0`) et les Tomes `1`–`8`, et scripts de compilation PDF/diagrammes | [`../Compendium/`](../Compendium/README.md) et [`../Tomes/`](../Tomes/README.md) |

## Commandes PowerShell rapides de recompilation PDF et Markdown

Exécuter depuis la racine du dépôt (`Agentique/`) :

```powershell
# Lister les 9 volumes catalogués (Compendium [0] et Tomes [1] à [8])
python -B Sources/gabarit-pdf/compile_pdf.py --list

# Recompiler les diagrammes des Tomes 1 à 6 (.puml -> .svg, .mmd -> .png)
# (Le Compendium et les Tomes 7–8 utilisent leurs scripts dédiés : compile_schemas_compendium.py et compile_figures.py)
python -B Sources/gabarit-pdf/compile_diagrams.py --all

# Recompiler un PDF précis ou toute la collection via le gabarit Typst unifié
python -B Sources/gabarit-pdf/compile_pdf.py --volume 0 --in-place
python -B Sources/gabarit-pdf/compile_pdf.py --all --in-place

# Réassembler et compiler les ouvrages complets (Markdown + PDF) depuis leurs chapitres sources
python -B Sources/Compendium/ouvrage/outils/assemble_livre.py --all
python -B "Sources/Tomes/Tome 7 - Gouverner l'industrialisation cognitive/outils/assemble_livre.py" --all
python -B "Sources/Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/outils/assemble_livre.py" --all

# Régénération intégrale de Cartographie/, prd.md, PRD Web HTML et MindMap HTML (dans l'ordre)
python -B Sources/Cartographie/outils/extraire_structure.py
python -B Sources/Cartographie/outils/inventorier_diagrammes_tomes.py
python -B Sources/Cartographie/outils/synthetiser_graphe.py
python -B Sources/Cartographie/outils/consolider_catalogue_schemas.py
python -B Sources/Cartographie/outils/compiler_prd.py
python -B Sources/Cartographie/outils/preparer_donnees_prd_web.py
python -B Sources/Cartographie/outils/compiler_prd_web.py
python -B Sources/Cartographie/outils/compiler_mindmap.py
```

## Vérifications rapides

```powershell
python -B -m pytest -p no:cacheprovider Sources/gabarit-pdf/test_gabarit_pdf.py -q
python -B -m pytest -p no:cacheprovider Sources/Cartographie/tests/test_cartographie.py Sources/Cartographie/tests/test_prd.py -q
python -B Sources/Compendium/ouvrage/outils/verifie_specs.py
python -B Sources/Compendium/ouvrage/outils/verifie_manuscrit.py --strict --check-deliverables
python -B -m pytest -p no:cacheprovider Sources/Compendium/ouvrage/outils -q
python -B "Sources/Tomes/Tome 7 - Gouverner l'industrialisation cognitive/outils/verifie_specs.py"
python -B "Sources/Tomes/Tome 7 - Gouverner l'industrialisation cognitive/outils/verifie_manuscrit.py" --strict --check-deliverables
python -B -m pytest -p no:cacheprovider "Sources/Tomes/Tome 7 - Gouverner l'industrialisation cognitive/outils" -q
python -B "Sources/Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/outils/verifie_specs.py"
python -B "Sources/Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/outils/verifie_manuscrit.py" --strict --check-deliverables
python -B -m pytest -p no:cacheprovider "Sources/Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/outils" -q
```

Pour exécuter les suites hors ligne de la trousse (`pytest`, politiques `OPA / Rego` et validation `G0`), consulter [`Sources/Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/README.md`](Tomes/Tome%208%20-%20Ing%C3%A9nierie%20ex%C3%A9cutable%20et%20homologation%20v%C3%A9rifiable/trousse/README.md).
