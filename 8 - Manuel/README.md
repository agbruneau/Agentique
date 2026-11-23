# Manuel Volume 8 — *Ingénierie exécutable de l'entreprise agentique*

Ce répertoire contient les sources éditoriales, les registres structurés (`SSOT`), le corpus documentaire vérifié (`L+`), les diagrammes, les journaux d'assurance qualité (`G0`–`G5`) et l'outillage de génération du manuel Volume 8. Le dépôt compagnon exécutable réside dans `../8 - Trousse/` (`MIT`).

> **Statut non-avis :** cet ouvrage et son dépôt compagnon relèvent d'un régime technique strictement hors modèle exécuté sur doublures synthétiques (`DC-P12`). Ils ne constituent ni un avis juridique, ni une certification réglementaire formelle.

---

## Livrables publiés

- **Édition Markdown consolidée :** `../0 - PDF-MD/8 - Manuel.md` (`CC BY 4.0`)
- **Édition imprimée PDF (`6,14 × 9,21 po`, corps `10,6 pt`, Typst) :** `../0 - PDF-MD/8 - Manuel.pdf` (`CC BY 4.0`)
- **Édition HTML autonome :** `./livrables/8 - Manuel.html` (seul fichier conservé dans `livrables/`)
- **Trousse compagnon exécutable :** `../8 - Trousse/` (`Python 3.12+`, `OPA / Rego`, licence `MIT`)

## Arborescence principale

- `manuscrit/` : liminaire (`00 - Liminaire.md`, cible `3 500` mots `± 8 %`), Partie I (`Chapitre 01`, `Chapitre 02`), Partie II (`Chapitre 03`, `Chapitre 04`), et Annexes générées (`Annexe A`, `Annexe B`), pour un budget global cible de `38 000` mots `± 8 %`.
- `diagrammes/` : sources et rendus des `9` figures originales (`Fig-00`..`Fig-03`, `Fig-05`..`Fig-07` en PlantUML SVG ; `Fig-04` et `Fig-08` en Mermaid PNG `300 DPI`), bornées entre `10` et `14` nœuds chacune.
- `specs/` et `registre/` : contrat éditorial, manifeste `manifest.json`, matrice de traçabilité `matrice-exig-prr-c40.json` (`24 [BLOQUANT] PRR`, `40` critères `C01–C40`, `5 SBB`, `2027-B001`) et table canonique des `5` discordances (`concordance-taxonomies.json`).
- `recherche/` et `sources/` : manifeste `L+` des `95` sources vérifiées par `SHA-256`, registre `statut F` (`AO-01`) et fiches bibliographiques chapitres (`ch00`–`ch04`).
- `ancrage/` et `aq/` : journaux atomiques Wyvern (`G2`), recollations stratifiées `G3` (`20270801` et `20270802`), journal adversarial `G4` (`gauntlet-log.md`), rapport `G0` (`rapports-g0.json`) et rapport `G5`/visuel (`rapport-lissage-et-visuel.md`).
- `outils/` : scripts déterministes `verifie_specs.py`, `execute_g0.py`, `compile_figures.py`, `genere_annexes.py`, `assemble_livre.py`, `verifie_manuscrit.py`, `echantillon_aq.py`, gabarit Typst (`gabarit-livre.typ`) et tests `pytest` (`test_outillage_aq.py`).

## Chaîne de reproduction hors ligne (`Python 3.12+`)

Exécuter depuis la racine du dépôt (`Agentique/`) dans l'ordre suivant :

```powershell
C:\Python314\python.exe -B "8 - Manuel/outils/verifie_specs.py"
C:\Python314\python.exe -B "8 - Manuel/outils/execute_g0.py"
C:\Python314\python.exe -B "8 - Manuel/outils/compile_figures.py" --strict --check-only
C:\Python314\python.exe -B "8 - Manuel/outils/genere_annexes.py"
C:\Python314\python.exe -B "8 - Manuel/outils/assemble_livre.py" --all
C:\Python314\python.exe -B "8 - Manuel/outils/verifie_manuscrit.py" --strict --check-deliverables
C:\Python314\python.exe -B -m pytest -p no:cacheprovider "8 - Manuel/outils" -v
```
