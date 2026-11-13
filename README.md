# Interopérabilité et Orchestration en Entreprise Agentique

Corpus documentaire sur la conception, l'intégration, la gouvernance et la supervision d'agents d'intelligence artificielle en contexte d'entreprise, plus particulièrement dans les services financiers réglementés au Canada. Le dépôt réunit deux éditions, une par dossier.

| Dossier | Contenu | Livrable principal |
| ------- | ------- | ------------------ |
| [`2026/`](2026/) | Six livrables en PDF (échelle de maturité, veille technologique, revue de littérature, cadre de référence, note AMF, compendium), une présentation en onze diapositives et la chaîne de recomposition des PDF. | [`2026/documents/`](2026/documents/) |
| [`2027/`](2027/) | Compendium 2027 : édition consolidée en dix parties, cinquante chapitres et huit annexes (1 059 pages), avec son manuscrit et sa chaîne de composition. | [`2027/CompendiumMaster.pdf`](2027/CompendiumMaster.pdf) |

## Édition 2026

Le détail (livrables, dates de gel, ordre de lecture, statut, limites) est dans [`2026/README.md`](2026/README.md).

- `documents/` : les six livrables en PDF, seuls fichiers de référence.
- `Presentation.html` : synthèse pour la haute direction; `index.html` y redirige.
- `sources/` : recomposition des PDF (Python 3 avec PyMuPDF, pandoc 3, Typst 0.15.1). Depuis `2026/` : `python sources/<livrable>/construire_pdf.py`.
- `outils/` : vérification de la mise en page et de l'intégrité de la présentation.

## Édition 2027

`CompendiumMaster.pdf` fusionne deux éditions d'origine du Compendium 2027, conservées telles quelles :

- `Claude/` : édition C, 47 chapitres et 5 annexes (A à E) en Markdown. Ses chapitres gardent leur numéro et leur texte.
- `Gemini/dist/compendium-2027-complet.html` : édition G. Chacun de ses chapitres devient le volet « Mise en œuvre » de son chapitre jumeau; son ouverture ouvre le volume et ses annexes A à C deviennent F à H.

Le reste est sous `Master/` :

- `manuscrit/` : manuscrit unifié (ouverture, 50 chapitres, annexes A à H, figures SVG), source du PDF. Les chapitres 48 à 50 (partie X, « Recherche scientifique ») n'ont pas d'édition d'origine : ils n'existent que là.
- `fusion/` : volets avant (`origine/`) et après (`reecrit/`) réécriture, avec leurs comptes rendus.
- `schemas/` : scripts qui produisent les schémas des exposés, et `schemas.json` qui les place.
- `audit/` : audit de publication; `corrections.json` est le registre unique des corrections appliquées au manuscrit.
- `recherche/` : fiches et notes à l'appui de la partie X.
- `gabarit.typ`, `filtres/` : gabarit Typst et filtres pandoc.

### Chaîne de composition

Dépendances : Python 3 avec PyMuPDF, pandoc et Typst sur le `PATH`. Les scripts se lancent depuis `2027/`; l'usage complet de chacun est dans son en-tête.

| Script (`Master/compendium-master-…`) | Rôle |
| ------------------------------------- | ---- |
| `manuscrit.py` | Génère le manuscrit à partir des éditions C et G. |
| `fusion.py` | Extrait, contrôle et intègre les volets « Mise en œuvre » réécrits (`--prepare`, `--controle ID`, `--bilan`, `--integre`). |
| `schemas.py` | Insère les schémas dans les exposés. |
| `audit.py` | Applique le registre des corrections (`--applique`, `--bilan`). |
| `assemble.py` | Compose `CompendiumMaster.pdf` à partir du manuscrit, sans le modifier. |
| `verifie.py` | Contrôle le manuscrit contre ses sources, puis le PDF; code de sortie 1 si un contrôle échoue. |

Pour recomposer et vérifier le PDF :

```bash
python Master/compendium-master-assemble.py
```

```bash
python Master/compendium-master-verifie.py
```

**Ne pas relancer `manuscrit.py`** tant que le manuscrit sert de source : le script efface `Master/manuscrit/` avant de le régénérer, ce qui supprime les chapitres 48 à 50 et les retouches faites directement dans le manuscrit.

## Licence

- Édition 2026 : documents sous [CC BY 4.0](2026/LICENSE), code de composition sous [licence MIT](2026/sources/LICENSE); la répartition exacte est dans [`2026/README.md`](2026/README.md#licence).
- Édition 2027 : aucun fichier de licence n'est versé à ce jour.

## Auteur

André-Guy Bruneau M.Sc. IT — agbruneau@gmail.com
