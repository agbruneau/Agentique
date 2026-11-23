# Gabarit PDF partagé de la collection

Gabarit éditorial Typst unique et compilateur unifié pour les 8 volumes du dépôt (`0 - PDF-MD/`), fondés sur la charte de référence de [8 - Manuel.pdf](../0%20-%20PDF-MD/8%20-%20Manuel.pdf).

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `gabarit-collection.typ` | Module Typst autonome exportant `collection-pdf(...)`, `divider` et `horizontalRule`. |
| `postprocess_typst.py` | Post-traitement typographique `fr-CA` (rééquilibrage des tableaux, virgules décimales en math, légendes centrées, césure des URL et du code inline, espaces insécables). |
| `preprocess_md.py` | Pré-traitement Markdown (YAML liminaire, retrait des couvertures aplaties et TDM statiques des volumes 1–6, normalisation des chemins d'images, injection optionnelle de diagrammes rendus). |
| `volumes.json` | Catalogue déclaratif des 8 volumes (métadonnées de couverture, mentions de référence, conventions de titres et options de pré-traitement). |
| `compile_pdf.py` | Interface CLI et API Python pour compiler un volume catalogué, toute la collection ou un fichier Markdown arbitraire. |
| `test_gabarit_pdf.py` | Suite de tests automatisés (`pytest`) couvrant le catalogue, les transformations et la compilation Typst réelle. |

## Charte visuelle de référence (`8 - Manuel.pdf`)

- **Format** : `6.14in × 9.21in`, marges `inside: 0.90in`, `outside: 0.78in`, `top: 0.92in`, `bottom: 0.90in` (largeur utile `4.46in`).
- **Typographie** : corps `Libertinus Serif` `10.6pt` (`fr-CA`, justifié, césure active), titres et éléments d'interface `Segoe UI`, code `Consolas` / `DejaVu Sans Mono`.
- **Palette** : marine foncé `#132238` (couverture et titres majeurs), bleu accent `#1B365D` (filets, en-têtes de tableaux, encadrés), ambre `#F59E0B` / `#B45309` (filets de couverture et séparateurs de parties), surfaces `#F8FAFC` / `#F1F5F9`, bordures `#CBD5E1`.
- **Structure éditoriale** : couverture pleine page `#132238` (badge de licence optionnel), page de titre intérieure avec encadré de mentions paramétré, table des matières en chiffres romains, en-têtes courants alternés (titre à gauche sur pages paires, chapitre courant à droite sur pages impaires, masqués sur les pages d'ouverture).
- **Robustesse multi-volumes** : prend en charge les séparateurs `Partie `, `Livre ` et `Annexes`, les chapitres `Chapitre `, `Annexe ` ou numérotés (`1 · ...`, `1 ...`, `A ...`), et autorise automatiquement la coupure de page sur les blocs de code de plus de 40 lignes et les encadrés dépassant `6.2in`.

## Utilisation rapide

```powershell
# Lister les 8 volumes catalogués
python gabarit-pdf/compile_pdf.py --list

# Compiler un volume vers un dossier de sortie (sans écraser 0 - PDF-MD/)
python gabarit-pdf/compile_pdf.py --volume 5 --output-dir build/

# Compiler un volume et écrire aussi la source Typst intermédiaire
python gabarit-pdf/compile_pdf.py --volume 8 --output build/8-manuel.pdf --emit-typst build/8-manuel.typ

# Compiler un document Markdown arbitraire
python gabarit-pdf/compile_pdf.py --input mon-doc.md --output build/mon-doc.pdf --title "Mon titre"

# Regénérer un PDF directement dans 0 - PDF-MD/ (explicite)
python gabarit-pdf/compile_pdf.py --volume 8 --in-place
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

## Raccordement avec `7 - Livre` et `8 - Manuel`

Les assembleurs [7 - Livre/outils/assemble_livre.py](../7%20-%20Livre/outils/assemble_livre.py) et [8 - Manuel/outils/assemble_livre.py](../8%20-%20Manuel/outils/assemble_livre.py) utilisent désormais `gabarit-pdf/gabarit-collection.typ` (via `render_typst_document`), et [8 - Manuel/outils/assemble_livre.py](../8%20-%20Manuel/outils/assemble_livre.py) délègue également son post-traitement Typst à `gabarit-pdf/postprocess_typst.py`.

## Tests

```powershell
python -m pytest gabarit-pdf/test_gabarit_pdf.py -q
```
