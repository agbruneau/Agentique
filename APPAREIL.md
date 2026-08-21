# L'appareil du dépôt — refaire, ou vérifier

*Ce fichier est l'annexe technique du [`README.md`](README.md), sortie de la page parce qu'elle ne
sert à personne qui vient **lire** les huit documents : tout y est déjà rendu en PDF. Elle sert à les
**refaire**, ou à vérifier qu'ils tiennent encore.* ⚠ *Comme le `README.md`, ce fichier n'est pas
versionné.*

## Les onze contrôles

Onze contrôles, huit passent, trois sortent 1. Rien n'est câblé en intégration continue — pas de
`.github/` —, et chacun se lance seul, depuis le dossier indiqué. *Relevé du 21 août 2026 ; toutes
les commandes ci-dessous ont été rejouées pour ce relevé, sauf mention contraire.*

**a. « Ce document tient-il ? » — un contrôle par livrable**

| Commande | Depuis | Verdict |
|---|---|---|
| `python Python/check-veille.py` | `4 - Veille/` | ☑ **0** — 94 sections, 342 entrées, appariement cité ↔ défini clos dans les deux sens |
| `python Python/check-revue.py` | `4 - Veille/` | ☑ **0** — 192 définies, 8 tableaux, 12 attestées / 32 auto-déclarées / 145 sans revue sur 189 arXiv |
| `python Python/check-traite.py` | `3 - Traité/` | ☑ **0** — 143 pages, recomptées à **deux sources du PDF qui doivent concorder** ; 123 notices citées nommément ; 72 110 mots |
| `python PRD/check-compendium.py` | `2 - Compendium/` | ☑ **0** — les 50 pièces tiennent (P1-P8), 3 rapports déclaratifs |
| `python PRD/check-toc.py` · `PRD/check-sieges.py` | `2 - Compendium/` | ☑ **0** — C1-C15 ; 26 sièges sur 50 pièces (S1-S5) |
| `python "4 - Veille/Python/check-resume.py" <fichier.pdf>` | racine | ☑ **0** sur les quatre PDF essayés — il mesure la **géométrie** de la page de titre : le gabarit compose le résumé dans un bloc qui ne se scinde pas, donc un résumé trop long se fait rogner sous la marge basse sans que Pandoc sorte autre chose que 0 |
| `bash PRD/decompte.sh --verifier` | `2 - Compendium/` | ⚠ **1** — Vol. I et Vol. III tiennent ; **le Vol. II mesure 93 239 mots pour 93 242 attendus**. Trois jetons retirés du corps par un commit de renommage, jamais reportés sur l'ancre |
| ⚠ *Le Vol. I n'a aucun contrôle propre.* | | |

**b. « Les contrôles tiennent-ils ? » — validation par mutation**

Chaque harnais copie le corpus dans un dossier temporaire, y injecte des fautes connues et exige que
le contrôle les attrape. À lancer après toute retouche du contrôle correspondant.

| Commande | Depuis | Verdict |
|---|---|---|
| `python PRD/check-sieges-mutations.py` | `2 - Compendium/` | ☑ **0** — attrape les **108** mutations |
| `python PRD/check-toc-mutations.py` | `2 - Compendium/` | ⚠ **1** — 22 sur 23 ; **M14 échappe à C14** |
| `python PRD/check-compendium-mutations.py` | `2 - Compendium/` | ⚠ **1** — s'arrête en `AssertionError` à la mutation M6 : le motif qu'elle réécrit n'existe plus au registre. *Le harnais échoue en le disant, comme son en-tête l'annonce* |

**c. « La chaîne se refait-elle ? » — graver, assembler, composer**

Ordre réel de fabrication : **graver les figures → assembler la source → composer le PDF.** Les deux
premières étapes ont été rejouées ici ; la troisième, non — et pour cinq des neuf PDF, aucun script
ne la porte — point 1 de « Ce qui accroche », au [`README.md`](README.md).

| Commande | Depuis | Verdict |
|---|---|---|
| `python figures/contenu.py` | racine | ☑ **19 SVG du traité regravés, identiques à l'octet** (`dessine.py` n'est pas un point d'entrée : il porte les primitives) |
| `python figures/dessine.py` | `5 - Recension/` | ☑ **5 SVG regravés, identiques à l'octet** |
| `python figures/genere.py [--verifier]` | `2 - Compendium/` | ☑ **115 figures regravées** sur 49 pièces, identiques à l'octet ; insertion idempotente, aucune pièce touchée |
| `python build/assemble.py` | `1 - Corpus/2 -…/` et `/3 -…/` | ☑ **reproduit le `Monographie.md` livré à l'octet près**, sur les deux volumes |
| `python build/assemble.py <sortie.md>` | `2 - Compendium/` | ☑ 50 chapitres, 5 livres, 2 annexes → 31 028 l. / 2,72 Mo |
| `bash build/build-pdf.sh` | Vol. I, II, III, Compendium | **Non rejoué ici.** Prérequis déclarés dans les scripts : Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf`, polices nommées ; Node ≥ 18 + `mermaid-cli` pour les 28 diagrammes du Vol. I |
| `cargo build` · `cargo test --workspace` | `3 - Traité/` | ⚠⚠ **ÉCHEC IMMÉDIAT, exit 101** — voir « Le workspace Rust ne se construit pas en l'état », au [`README.md`](README.md) |

⚠ **Cinq autres points d'entrée existent, hors de ces tableaux et non rejoués ici** :
`2 - Compendium/build/assemble-bibliographie.py`, `build/echantillon.py` (maquette Springer, avec
`echantillon.template` et `springer.template`), et les trois `build/inject-pagination.py` des
volumes du corpus.

## D'où viennent les chiffres du `README.md`

Tous relevés le **21 août 2026**, sur l'arbre de travail, par ces commandes et par elles seules :

- **Pages** — `pypdf`, `len(PdfReader(f).pages)` sur les 15 PDF versionnés. Aucun nombre de pages
  n'est repris d'un autre `README.md`.
- **Titres et auteurs** — champs `/Title` et `/Author` des PDF, et en-têtes YAML des sources.
- **Lignes, octets, cardinaux de fichiers** — `wc -l` / `wc -c` / `git ls-files`. *Les tailles sont
  décimales : 1 Mo = 10⁶ octets.*
- **Historique** — `git log --format='%an'`, `git log --merges` (quatre fusions, et
  `git log --all --grep='#4'` ne rend rien), `git tag`, `git branch -r`, et
  `git log --all --diff-filter=A --name-only` pour ce que l'arbre ne porte plus.
- **Références, sections, tableaux, mots** — sortie des contrôles du dépôt eux-mêmes
  (`check-veille.py`, `check-revue.py`, `check-traite.py`, `decompte.sh`), rejoués ici ; les 312
  notices de l'état de l'art recomptées à part sur sa bibliographie.
- **Reproductibilité des chaînes** — assembleurs et graveurs relancés sur une copie de sauvegarde,
  puis comparés fichier à fichier avec `cmp` ; l'arbre a été remis en état après chaque essai.
- **Renvois morts** — résolution de chaque cible relative des quinze `README.md` versionnés **et du
  `README.md` de la racine** contre le système de fichiers.
- **Diagrammes Mermaid** — `grep -cFx` sur la ligne d'ouverture de bloc `mermaid` : 28 dans le
  Vol. I, 64 dans tout le dépôt.
