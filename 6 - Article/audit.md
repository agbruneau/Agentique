# Audit intégral du dossier `6 - Article` et plan d'exécution

*Audit du 2 septembre 2026, sur le commit `b439bb2`. Périmètre : les sept fichiers du dossier — la
source Typst, son rendu, la bibliographie, le script de rejeu, le gabarit, les figures et le README.
Tout constat marqué ☑ a été **mesuré** ; ce qui est déduit le dit.*

## 1. Résumé

**Le dossier tient, et il tient mieux que les deux précédents : il est petit, il dit ce qu'il ne
contrôle pas, et ce qu'il affirme se remesure.** Le rendu est **reproductible à l'octet** aux seuls
horodatages près ; le script de rejeu sort 0 et ses huit valeurs attendues sont **toutes** dans
l'article ; la bibliographie est close dans les deux sens ; les 165 renvois « § X.Y » écrits à la
main résolvent tous ; les six fichiers texte sont en LF — **c'est le seul dossier de l'arbre de
travail conforme au `.gitattributes`**.

Ce qui ne tient pas est de trois ordres, et aucun n'est de fond :

1. **Un cardinal faux, répété trois fois** : « 26 figures » et « les 26 planches ». Il y a
   **8 planches et 20 tableaux**, et le PDF les légende ainsi — `Fig. 1-8`, `Tableau 1-20`.
2. **Deux cardinaux imprécis** : une taille de source mesurée sur un arbre CRLF (134 947 o. pour
   132 968), et un écart d'horodatage compté 60 quand il en fait 62.
3. **Rien ne garde ce que le README a mesuré une fois** : la clôture de la bibliographie, la parité
   source/rendu, la résolution des renvois, les cardinaux publiés. *Le README le dit lui-même pour
   la bibliographie ; c'est vrai de tout le reste.*

Le plan tient en **quatre phases, un commit** : un contrôle neuf éprouvé par mutation, le README
remis sur la mesure, le champ `/Author` corrigé à la source et recomposé, treize entrées
bibliographiques dotées de leurs auteurs depuis la source.

## 2. Méthode

Rejeu de `rejeu-politique.py` et lecture intégrale du script ; recomposition par
`typst compile` dans un répertoire de travail et comparaison **octet à octet** avec le PDF livré ;
extraction des métadonnées et du texte du PDF (`pypdf`, `pymupdf`) ; appariement des 77 clés du
`.bib` aux citations du corps dans les deux sens ; dénombrement des titres, figures, légendes,
étiquettes, renvois et identifiants dans la source ; **confrontation case par case de la table de
transitions publiée (§ 6.4) à la table du script** ; rejeu de `check-resume.py` et localisation du
texte qu'il prend pour un débordement ; lecture des trois documents de la racine qui décrivent ce
dossier.

## 3. Constats

### 3.1 Ce qui tient

| # | Constat mesuré |
|---|---|
| ☑ | `python rejeu-politique.py` → **0**, message conforme. Les **huit scores** qu'il attend (0,703 · 0,463 · 0,650 · 0,750 · 0,690 · 0,774 · 0,488 · 0,550), les deux parcs et les trois jeux de poids sont dans l'article, au chiffre près |
| ☑ | **Table de transitions : 35 cases sur 36 concordent exactement** entre le § 6.4 et le script, la 36e — `É × E2`, « → D si conforme, sinon → G » — n'étant exercée que sur sa branche conforme (voir A-07) |
| ☑ | `typst compile` rend **750 902 octets**, la taille du livré ; **identique à l'octet hors horodatage** ; `xmpMM:DocumentID` inchangé |
| ☑ | 38 pages ; `dc:title` avec l'apostrophe ; `/Creator` Typst 0.15.1 |
| ☑ | Bibliographie **77 définies, 77 citées, aucune clé morte, aucun doublon**, aucune année postérieure à 2026 |
| ☑ | Source : 1 979 l., 11 titres de niveau 1, 39 de niveau 2, numérotation `1.1` ; **165 renvois « § X.Y » à la main, tous résolvent** |
| ☑ | INV-1…6, PR-01…06, cinq SLO, sept exigences (tableau du § 8.1), vingt métriques (tableau de télémétrie), RÉF-1…8 : chaque cardinal annoncé se compte |
| ☑ | Les 8 planches de `.figures.typ` sont toutes appelées du corps ; aucune aide interne n'est morte |
| ☑ | `check-resume.py` : le texte à 42,5 pt en page 1 est le **folio « 1 »** — le diagnostic du README est confirmé sur pièce |
| ☑ | Six fichiers texte, **six en LF** — le seul dossier conforme au `.gitattributes` sur cet arbre |

### 3.2 Anomalies

| # | Gravité | Constat | Siège |
|---|---|---|---|
| A-01 | **M** | « **26 figures** » (README ×2, README racine l. 84) et « `.figures.typ` … les **26 planches** » : les 26 `#figure(` du corps sont **18 tableaux et 8 planches**, plus deux tableaux légendés hors `#figure(` en tête de ligne ; le PDF rend **`Fig.` 1-8 et `Tableau` 1-20**. Le mot *figure* confond le flottant Typst et l'illustration, et la phrase sur `.figures.typ` est fausse : il dessine huit planches | `README.md:60`, `:62` |
| A-02 | m | « **134 947 o.** » pour la source : mesuré **132 968**. L'écart vaut **1 979 — le nombre de lignes** : le README a compté un rendu CRLF d'un fichier LF | `README.md:60` |
| A-03 | m | « **60 octets** diffèrent, en cinq endroits » : mesuré **62**, et **six champs**, non cinq — `ModDate`, `CreationDate`, `xmp:ModifyDate`, `xmp:CreateDate`, `xmpMM:InstanceID` **et le `/ID` du trailer**, que le relevé ne nommait pas. ⚠ *L'audit lui-même n'a compté les six qu'à l'exécution : son contrôle de parité a échoué sur le sixième.* Repris par `APPAREIL.md:74` | `README.md:81` |
| A-04 | m | `/Author` lit **`M.Sc IT`** sans le point — relevé par le README et la racine, **non corrigé**. La correction tient en un caractère à la ligne 9 de la source, et la recomposition est reproductible | `article-hpc-qpu.typ:9` |
| A-05 | **M** | **Aucun contrôle ne garde ce que le README a mesuré** : ni la clôture de la bibliographie — *le README le dit* —, ni la parité source/rendu, ni la résolution des 165 renvois, ni les cardinaux publiés. Une entrée qui sortirait du corps, un PDF non recomposé, une section insérée : rien ne le signalerait | appareil |
| A-06 | m | **13 entrées sur 77 n'ont pas de champ `author`**, toutes des `@misc` qui sont des articles signés (le *survey*, openQSE, QMIO, la pile de Munich…) ; en style IEEE elles se rendent **sans auteur**. `iso15288` n'a ni `url` ni `doi` | `references.bib` |
| A-07 | m | `rejeu-politique.py` porte les valeurs publiées **en dur** : rien n'oppose ses constantes aux chiffres du § 7.5 — *copie contre copie*, égales aujourd'hui. Et la case `É × E2` porte une condition — « si conforme » — que le script **ne peut pas prendre** : il n'a pas d'entrée de conformité et n'implante que la branche → D | `rejeu-politique.py:69`, `:121-138` |
| A-08 | m | Deux étiquettes seulement dans la source — `<fig:chrono>` et `<sec:deroule>`, celle-ci employée une fois par `#ref(<sec:deroule>, supplement: [§])` à la RÉF-6. ⚠ *L'audit l'avait d'abord dite « jamais référencée » : il ne cherchait que la forme `@…`, et sa suppression a cassé la compilation — constat corrigé à l'exécution.* Les 165 autres renvois sont écrits à la main — ils résolvent, et **se décaleraient en silence** à la première section insérée | `article-hpc-qpu.typ:1231`, `:1876` |
| A-09 | m | Le gabarit se dit « d'après `arxiv.sty` (G. Kour) » et **ne reporte aucune mention de licence** de l'original (*MIT, à confirmer à la source*) | `.gabarit-arxiv.typ:1` |
| A-10 | m | Le dossier n'a **ni `build/`, ni `CLAUDE.md`** — le premier est justifié par le README (une seule commande), le second n'est pas discuté | dossier |

### 3.3 Hors dossier, à remonter

| Site | Ce qu'il porte | Ce qu'il devrait porter |
|---|---|---|
| `README.md` racine, l. 84 | « 26 figures » | « 8 planches et 20 tableaux » |
| `APPAREIL.md`, l. 74 | « 60 octets d'écart en cinq endroits » | « une cinquantaine d'octets, dans six champs » |

## 4. Plan d'exécution

**Cadre.** Quatre phases, un seul commit. Chaque phase se rejoue par les commandes du § 6. Ce
dossier est un document publié : **aucune phase ne touche le propos** ; la seule modification de la
source est un point dans une chaîne de métadonnées.

### Phase 0 — appareil

| Tâche | Constats | Geste |
|---|---|---|
| 0.1 | A-05, A-01 | Écrire `check-article.py`, quatre contrôles : **[1]** clôture de la bibliographie dans les deux sens, les étiquettes `fig:`/`sec:` et l'adresse écartées ; **[2]** parité source/rendu — recomposer dans un répertoire temporaire et comparer les octets hors des cinq champs volatils ; **[3]** résolution des renvois « § X.Y » contre les titres numérotés ; **[4]** les cardinaux que le README publie — planches, tableaux, notices, pages — égaux à la mesure |
| 0.2 | A-07 | Au même script, **[5]** : les huit scores que `rejeu-politique.py` attend sont **lus dans le § 7.5 de l'article** et opposés aux constantes du script — la copie opposée à l'original |
| 0.3 | — | Éprouver les cinq par mutation : `check-article-mutations.py`, une faute par classe, ligne de base tenue |
| 0.4 | A-07 | Dans `rejeu-politique.py`, dire à la case `É × E2` ce que le script n'exerce pas, et pourquoi |

Critère de sortie : les deux scripts sortent 0 ; les mutations sont toutes vues.

### Phase 1 — le README et la source, remis sur la mesure

| Tâche | Constats | Geste |
|---|---|---|
| 1.1 | A-01 | « 26 figures » → « 8 planches et 20 tableaux » (deux sites) ; « les 26 planches » → « les 8 planches » |
| 1.2 | A-02, A-03 | 134 947 → 132 968 avec la cause ; 60 → 62 |
| 1.3 | A-04 | `M.Sc IT` → `M.Sc. IT` à la ligne 9, **recomposer**, vérifier la parité, mettre à jour le paragraphe du README qui déclarait le relevé non corrigé |
| 1.4 | A-08 | *Rien* : l'étiquette est employée ; la tâche telle qu'écrite reposait sur un constat faux, et son exécution l'a montré |
| 1.5 | A-09 | Porter dans l'en-tête du gabarit la provenance exacte de l'original et la condition de sa licence |

### Phase 2 — la bibliographie

| Tâche | Constats | Geste |
|---|---|---|
| 2.1 | A-06 | Pour les treize entrées sans auteur : **lire les auteurs à la source** — l'API arXiv pour celles qui portent un identifiant arXiv, et **rien par inférence**. Celles dont la source n'est pas atteignable restent telles quelles, nommées |
| 2.2 | A-06 | `iso15288` : l'adresse de la norme |
| 2.3 | — | Recomposer si le rendu bouge (les auteurs changent le rendu IEEE), rejouer la parité |

### Phase 3 — les deux remontées

| Tâche | Geste |
|---|---|
| 3.1 | `README.md` racine l. 84 et `APPAREIL.md` l. 74 : les deux cardinaux, une ligne chacun — *ce sont les nombres de ce dossier, republiés* |

## 5. Limites de cet audit

Le **propos** de l'article n'est pas audité : ni la justesse de la politique, ni la pertinence des
sources, ni les huit conditions de réfutation sur le fond. Seule RÉF-6 est exécutée, par le script
du dossier. La licence de `arxiv.sty` est **supposée** MIT et non lue à la source. Le compte de mots
(~19 200 au README, ≈ 18 700 par un autre dépouillement) n'est pas tranché : la méthode n'est écrite
nulle part.

## 6. Commandes de rejeu

```bash
cd "6 - Article"
python rejeu-politique.py
python check-article.py
python check-article-mutations.py
typst compile article-hpc-qpu.typ /tmp/essai.pdf
```

---

## 7. Journal d'exécution — 2 septembre 2026

*Les quatre phases ont été exécutées le jour de l'audit, sur instruction d'auteur. Ce journal dit
ce qui a été fait, ce que l'exécution a démenti dans l'audit lui-même, et ce qui reste.*

### 7.1 Ce qui a été fait

| Phase | État | Ce qu'elle laisse derrière |
|---|---|---|
| **0 — appareil** | ☑ | `check-article.py`, cinq contrôles ; `check-article-mutations.py`, sept mutations dont une « ne doit pas voir », **toutes vues** ; la case `É × E2` du script dit ce qu'elle n'exerce pas |
| **1 — README et source** | ☑ | « 26 figures » → **8 planches et 20 tableaux** (deux sites) ; 134 947 → **132 969** avec la cause ; « 60 octets, cinq endroits » → **six champs**, le nombre déclaré variable ; `/Author` **`M.Sc. IT`** à la source, recomposé, parité vérifiée ; licence de l'original portée au gabarit — **MIT, © 2020 George Kour**, lue au `License.txt` du dépôt d'origine |
| **2 — bibliographie** | ☑ | **13 champs `author` posés**, lus verbatim aux pages arXiv des treize prépublications ; le rendu IEEE les imprime — 750 902 → **752 159 octets**, 38 pages inchangées |
| **3 — remontées** | ☑ | `README.md` racine l. 84 et `APPAREIL.md` l. 74 alignés, fins de ligne conservées |

### 7.2 Ce que l'exécution a démenti dans l'audit

1. ⚠ **A-08 était faux.** `<sec:deroule>` n'est pas une étiquette morte : la RÉF-6 l'emploie par
   `#ref(<sec:deroule>, supplement: [§])`, forme que le balayage n'avait pas cherchée — il ne
   connaissait que `@…`. **Sa suppression a cassé la compilation**, et c'est Typst qui a corrigé
   l'audit. La tâche 1.4 est annulée, le constat réécrit.
2. ⚠ **A-03 comptait cinq champs volatils ; il y en a six.** Le `/ID` du trailer change à chaque
   rendu comme les dates, et le README du 1er septembre ne le nommait pas — il comptait tous les
   octets et ne listait que cinq champs. **Le contrôle de parité a échoué à son premier passage sur
   ce sixième**, à 51 octets de la fin du fichier. *Un contrôle qui échoue sur le dossier intact
   enseigne quelque chose au contrôle, pas au dossier.*
3. ⚠ **L'exécution a elle-même produit la faute qu'elle corrigeait.** La première passe d'édition a
   écrit trois fichiers en **CRLF** — le réglage par défaut de Python sur Windows —, et le contrôle
   [4] l'a vu aussitôt : 134 934 octets pour une source de 132 968, **1 966 de trop, un par ligne**.
   Le dossier était le seul de l'arbre conforme au `.gitattributes` ; il l'est resté, parce qu'un
   contrôle l'a exigé.

### 7.3 Ce qui n'a pas été fait

☐ **`iso15288` reste sans adresse** : `iso.org` répond 403 à toute lecture automatisée, et la page
IEEE essayée désigne une autre norme. *Une adresse qu'on n'a pas lue ne se pose pas.* La tâche 2.2
est reportée, nommée.

☐ **Le compte de mots** (~19 200 au README) n'est toujours pas tranché : la méthode n'est écrite
nulle part, et l'audit n'en impose pas une.

☐ **Le propos** — politique, sources, sept des huit conditions de réfutation — n'est pas audité.
Seule RÉF-6 est exécutée, par le script du dossier, sur trente-cinq cases et demie.

### 7.4 État final

`python rejeu-politique.py` → 0 · `python check-article.py` → 0, cinq contrôles · 
`python check-article-mutations.py` → 0, sept mutations vues · dix fichiers, **tous en LF**.
