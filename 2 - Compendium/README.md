# Conspectus — Interopérabilité et Orchestration en Entreprise Agentique

*Autonomie encadrée et fabrique de confiance : déployer des agents en services financiers réglementés (2024-2032).* Le Vol. IV réunit
les trois monographies de [`1 - Collection/`](../1%20-%20Collection/), dédoublonnées et re-datées à la source, en cinquante chapitres sur
quatre plans : coopérer, faire confiance, encadrer, livrer.

**Statut :** archive de travail, hors compte des livrables — fixé le 15 septembre 2026 par la décision [D-18](PRD/PRD.md#d-18), option DA-2 (a) ;
dépôt rouvert le même jour par [D-17](PRD/PRD.md#d-17), re-clos le 16 septembre 2026 par [D-19](PRD/PRD.md#d-19). Le volume reste au dépôt, entier ; ses cinquante pièces se déclarent brouillon non
publiable, et les trois volumes sources font foi. Faute de relecteur distinct du rédacteur, CA-IV-11 et CA-IV-13 ne sont pas satisfaits.

| Champ | Valeur |
|---|---|
| Source | [`TOC.md`](PRD/TOC.md) v0.36, du 2 septembre 2026 — le plan, seul à faire autorité ; cette page le suit |
| Rendu | [`Compendium.pdf`](Compendium.pdf), 1 000 pages, cible que la chaîne de composition vérifie |
| Pièces | cinquante chapitres, chacun en `.md`, qui fait foi, et en `.html` : [Livre I](Livre%20I/README.md), ch. 1-11 · [II](Livre%20II/README.md), 12-21 · [III](Livre%20III/README.md), 22-36 · [IV](Livre%20IV/README.md), 37-46 · [V](Livre%20V/README.md), 47-50 |
| Socle | [`PRD/socle-consolide.md`](PRD/socle-consolide.md), l'Annexe B : 159 entrées, S-001 à S-159 |
| Annexes | [`annexe-bibliographie.md`](annexe-bibliographie.md), l'Annexe I, et [`annexe-references.md`](annexe-references.md), hors plan |
| Figures | 118, décrites par [`figures/contenu*.py`](figures/) et gravées par [`figures/genere.py`](figures/genere.py), selon le [programme](figures/programme.md) |
| Gouvernance | [`PRD/PRD.md`](PRD/PRD.md), dont l'annexe A porte les décisions d'auteur ; [`PRD/registre-gel.md`](PRD/registre-gel.md) |

**Par où entrer :** l'[objet et la thèse](JOURNAL.md#lobjet-et-la-thèse), puis le [parcours de l'ouvrage](JOURNAL.md#parcours-de-louvrage), livre
par livre, tels que le conspectus les écrivait au 15 septembre 2026 ; ensuite la page du Livre voulu.

**Refaire :** depuis ce dossier, `bash build/build-pdf.sh` recompose `Compendium.pdf` et échoue si le rendu n'a pas mille pages ;
`python build/rendre-piece.py` rend les cinquante `.html` depuis leurs `.md` ; `python figures/genere.py` regrave et pose les figures.

**Vérifier :** depuis ce dossier, un contrôle à la fois, jamais en chaîne `&&` — `python PRD/check-toc.py` pour le plan,
`python PRD/check-sieges.py` pour les sièges, `python PRD/check-compendium.py` pour les pièces, chacun doublé de son harnais
`*-mutations.py` ; `bash PRD/decompte.sh --verifier`, seule autorité de décompte, que `python PRD/reporter-volumetrie.py` reporte aux trois
sites qui la publient ; `python build/verifier-piece.py`, qui oppose chaque `.html` à ce que son `.md` produit.

**Journal :** [`JOURNAL.md`](JOURNAL.md) — arrêt en révision finale, clôture et réouvertures, renommages et recompositions, le conspectus
entier et les pages des cinq Livres, tels qu'ils étaient écrits au 15 septembre 2026.
