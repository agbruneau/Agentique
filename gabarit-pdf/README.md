# Gabarit PDF partagé de la collection

[Retour à l'index principal du dépôt](../README.md)

Gabarit éditorial Typst unique et compilateur unifié pour les 8 tomes du dépôt (fichiers consolidés `.md`/`.pdf` dans [Corpus/](../Corpus/README.md) et répertoires de travail `Tome 1` à `Tome 8` dans [Tomes/](../Tomes/README.md)), fondés sur la charte de référence de [Tome 8 - Ingénierie exécutable et homologation vérifiable.pdf](../Corpus/Tome%208%20-%20Ing%C3%A9nierie%20ex%C3%A9cutable%20et%20homologation%20v%C3%A9rifiable.pdf).

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| [gabarit-collection.typ](gabarit-collection.typ) | Module Typst autonome exportant `collection-pdf(...)`, `divider` et `horizontalRule`. |
| [postprocess_typst.py](postprocess_typst.py) | Post-traitement typographique `fr-CA` (rééquilibrage des tableaux y compris larges 8–11 colonnes, virgules décimales en math, légendes centrées, césure des URL et du code inline, espaces insécables, sections bibliographiques non justifiées). |
| [preprocess_md.py](preprocess_md.py) | Pré-traitement Markdown (YAML liminaire, retrait des couvertures aplaties et TDM statiques des tomes 1–6, normalisation des chemins d'images, injection des diagrammes rendus avec remplacement automatique des blocs `> **[Figure]**`). |
| [volumes.json](volumes.json) | Catalogue déclaratif des 8 tomes (`Tome 1` à `Tome 8` : répertoires et diagrammes sous `Tomes/`, sources `.md` et cibles `.pdf` dans `Corpus/`, métadonnées de couverture, mentions de référence, conventions de titres et options de pré-traitement). |
| [compile_diagrams.py](compile_diagrams.py) | Compilateur parallèle avec cache incrémental des diagrammes `.puml` (`plantuml` → `.svg`) et `.mmd` (`mmdc` → `.png` haute résolution) vers `Tomes/<Tome>/Diagrammes/rendus/` (noms canoniques courts, rapport console/JSON). |
| [compile_pdf.py](compile_pdf.py) | Interface CLI et API Python pour compiler un tome catalogué, toute la collection ou un fichier Markdown arbitraire. |
| [test_gabarit_pdf.py](test_gabarit_pdf.py) | Suite de tests automatisés (`pytest`) couvrant le catalogue, les transformations, `compile_diagrams.py` et la compilation Typst réelle. |

## Charte visuelle de référence (`Tome 8 - Ingénierie exécutable et homologation vérifiable`)

- **Format** : `6.14in × 9.21in`, marges `inside: 0.90in`, `outside: 0.78in`, `top: 0.92in`, `bottom: 0.90in` (largeur utile `4.46in`).
- **Typographie** : corps `Libertinus Serif` `10.6pt` (`fr-CA`, justifié, césure active), titres et éléments d'interface `Segoe UI`, code `Consolas` / `DejaVu Sans Mono`.
- **Palette** : marine foncé `#132238` (couverture et titres majeurs), bleu accent `#1B365D` (filets, en-têtes de tableaux, encadrés), ambre `#F59E0B` / `#B45309` (filets de couverture et séparateurs de parties), surfaces `#F8FAFC` / `#F1F5F9`, bordures `#CBD5E1`.
- **Structure éditoriale** : couverture pleine page `#132238` (badge de licence optionnel), page de titre intérieure avec encadré de mentions paramétré, table des matières en chiffres romains, en-têtes courants alternés (titre à gauche sur pages paires, chapitre courant à droite sur pages impaires, masqués sur les pages d'ouverture).
- **Robustesse multi-tomes** : prend en charge les séparateurs `Partie `, `Livre ` et `Annexes`, les chapitres `Chapitre `, `Annexe ` ou numérotés (`1 · ...`, `1 ...`, `A ...`), et autorise automatiquement la coupure de page sur les blocs de code de plus de 40 lignes et les encadrés dépassant `6.2in`.

## Utilisation rapide

```powershell
# Lister les 8 tomes catalogués (sources .md et cibles .pdf dans Corpus/)
python gabarit-pdf/compile_pdf.py --list

# Compiler les diagrammes (.puml -> .svg, .mmd -> .png) pour des tomes précis ou les tomes 1–6
python gabarit-pdf/compile_diagrams.py --volume 1,2,3
python gabarit-pdf/compile_diagrams.py --all
python gabarit-pdf/compile_diagrams.py --volume 5 --force --json-report build/diagrams-tome5.json
python gabarit-pdf/compile_diagrams.py --all --check-only

# Compiler un tome vers un dossier de sortie (sans écraser Corpus/)
python gabarit-pdf/compile_pdf.py --volume 5 --output-dir build/
python gabarit-pdf/compile_pdf.py --volume "Tome 5" --output-dir build/

# Compiler un tome et écrire aussi la source Typst intermédiaire
python gabarit-pdf/compile_pdf.py --volume 8 --output build/tome-8.pdf --emit-typst build/tome-8.typ

# Compiler un document Markdown arbitraire
python gabarit-pdf/compile_pdf.py --input mon-doc.md --output build/mon-doc.pdf --title "Mon titre"

# Régénérer un PDF directement dans Corpus/ (Tome 1 à Tome 8 ; diagrammes injectés automatiquement pour les tomes 1–6)
python gabarit-pdf/compile_pdf.py --volume 5 --in-place
python gabarit-pdf/compile_pdf.py --all --in-place
```

### Utilisation directe en Typst

```typst
#import "/gabarit-pdf/gabarit-collection.typ": collection-pdf, divider, horizontalRule

#show: collection-pdf.with(
  title: [Titre de l'ouvrage],
  subtitle: [Sous-titre analytique],
  author: [André-Guy Bruneau, M.Sc IT],
  pub-date: [janvier 2027],
  freeze-date: [2 décembre 2026],
  license-badge: [CC BY 4.0],
)

= Liminaire
Contenu de l'ouvrage.
```

## Raccordement avec `Tome 7` et `Tome 8`

Les assembleurs [Tomes/Tome 7 - Gouverner l'industrialisation cognitive/outils/assemble_livre.py](../Tomes/Tome%207%20-%20Gouverner%20l'industrialisation%20cognitive/outils/assemble_livre.py) et [Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/outils/assemble_livre.py](../Tomes/Tome%208%20-%20Ing%C3%A9nierie%20ex%C3%A9cutable%20et%20homologation%20v%C3%A9rifiable/outils/assemble_livre.py) utilisent désormais [gabarit-collection.typ](gabarit-collection.typ) (via `render_typst_document`), et [Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/outils/assemble_livre.py](../Tomes/Tome%208%20-%20Ing%C3%A9nierie%20ex%C3%A9cutable%20et%20homologation%20v%C3%A9rifiable/outils/assemble_livre.py) délègue également son post-traitement Typst à [postprocess_typst.py](postprocess_typst.py).

## Tests

```powershell
python -B -m pytest -p no:cacheprovider gabarit-pdf/test_gabarit_pdf.py -q
```
