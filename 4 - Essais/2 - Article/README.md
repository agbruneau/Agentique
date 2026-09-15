# 4 - Essais / 2 - Article — une prépublication HPC-QPU

*Projection de l'état de ressource et délégation multicritère dans une plateforme HPC à processeurs quantiques* — prépublication au
gabarit arXiv, v3, datée du 31 août 2026. Les briques de l'intégration HPC-QPU existent ; ce qui manque est la chaîne entre elles, quand
la qualité de sortie d'un processeur quantique dérive sans qu'aucune panne ne survienne. Quatre contributions : la projection de l'état de
ressource en objet daté et périssable, une architecture de référence à machine d'états totale, une politique de délégation multicritère
vérifiable sans matériel, sept exigences d'exploitabilité. Le travail est documentaire et énonce huit conditions de réfutation.

**Statut :** publié, hors livrables — fixé le 15 septembre 2026 par la décision [D-18](../../2%20-%20Compendium/PRD/PRD.md#d-18) : il
n'instruit pas la question du corpus. Son voisinage avec elle — l'agent scientifique autonome comme consommateur d'états déclarés,
au § 2.8 — est posé par l'article lui-même.

**Lire :** [`article-hpc-qpu.pdf`](article-hpc-qpu.pdf).

| Fichier | Mesure | Rôle |
|---|---|---|
| `article-hpc-qpu.pdf` | 38 p. / 752 159 o. | le rendu |
| `article-hpc-qpu.typ` | 1 979 l. / 132 969 o. | la source, en Typst direct : 11 sections de niveau 1, 39 de niveau 2, 8 planches et 20 tableaux légendés |
| `references.bib` | 77 entrées / 689 l. | la bibliographie, close dans les deux sens |
| `rejeu-politique.py` | | l'implémentation de référence de la politique et de la machine d'états |
| `check-article.py`, `check-article-mutations.py` | | le contrôle du dossier et son harnais |
| `.gabarit-arxiv.typ`, `.figures.typ` | | le gabarit et les primitives des planches — fichiers à point, qu'un `ls` sans `-a` ne montre pas |

**Refaire :** depuis ce dossier, `typst compile article-hpc-qpu.typ`, avec Typst 0.15.1 et les polices New Computer Modern et DejaVu Sans
Mono ; c'est la seule chaîne du dépôt sans Pandoc, et la recomposition rend le PDF livré à l'octet, hors six champs d'horodatage.

**Vérifier :** `python rejeu-politique.py` rejoue les déroulés publiés et exerce les 37 transitions de la machine d'états — la seule
condition de réfutation que le dépôt exécute. `python check-article.py` vérifie la bibliographie, la parité du rendu, les renvois « § »,
les mesures du tableau ci-dessus, les scores et le rejeu ; `python check-article-mutations.py` prouve qu'il voit ses fautes.
`check-resume.py` ne s'applique pas à ce gabarit, qui pose un folio sous la marge de la page de titre.

**Journal :** [`JOURNAL.md`](JOURNAL.md) — entrée au dépôt le 1er septembre 2026, motif du rangement hors livrables, relevés de
métadonnées et de parité, et les corrections de la page qui les consignait.
