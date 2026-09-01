# 6 - Article — une prépublication, et pourquoi elle n'est pas le neuvième livrable

*Projection de l'état de ressource et délégation multicritère dans une plateforme HPC à
processeurs quantiques* — **38 p.**, prépublication au gabarit arXiv, v3 (révisée), datée du
**31 août 2026** en page de titre et composée le **1er septembre 2026**. Entrée au dépôt le même
jour, au commit `da6255b` (« Article ») : **une réouverture de plus** d'un dépôt déclaré clos le
8 août 2026, et **la première qui crée un dossier numéroté depuis le 20 août** — ⚠ *la chronique
datée de [`1 - Collection/README.md`](../1%20-%20Collection/README.md) s'arrête à la onzième
réouverture, celle du 21 août 2026 ; elle ne porte aucune des passes du 22 au 28 août, ni celle-ci.
Un lecteur qui compte les réouvertures sur cette chronique compte court.*

⚠ **Ce document n'instruit pas la question du dépôt.** Les huit livrables tiennent une seule
question — *comment une entreprise de services financiers canadienne déploie, gouverne et exploite
des agents d'IA autonomes sous contrainte réglementaire* — et celui-ci porte sur l'intégration de
processeurs quantiques dans une plateforme de calcul haute performance. **Il est publié ici, signé
de la même main, et il n'est pas rangé parmi les livrables** : *le motif est thématique, non
méthodologique, et c'est un motif neuf.* La note de veille SDLC de `4 - Veille/` est tenue hors des
huit pour **ce qui lui manque** — source unique, bibliographie non appariée, aucun contrôle qui
l'oppose à elle-même ; celui-ci l'est pour **ce dont il traite**. ⚠ *Le PRD ne porte aucune
décision sur ce document, pas plus que sur le huitième ni sur la note : le compte se renverse d'un
mot de l'auteur.*

☑ *Le lien n'est pourtant pas nul, et l'article le pose lui-même* : son § 2.8 fait des laboratoires
autopilotés et des agents scientifiques autonomes le **consommateur le plus exigeant** de la chaîne
de délégation qu'il spécifie — « pour lui, tout ce qui n'est pas publié comme état consommable
n'existe pas ». *C'est la thèse du corpus — l'agent comme consommateur d'états déclarés — reportée
sur un parc de ressources physiques. Ce n'est pas la même question ; c'en est un voisinage, et il
est déclaré.*

## Ce qu'il soutient

Les briques de l'intégration HPC-QPU existent et mûrissent — architectures de référence, interfaces
de dispositif et de ressource, intergiciel adaptatif, stratégies de partage mesurées, plateformes
déployées. **Ce qui manque n'est pas une brique, c'est la chaîne entre elles** : décider quelle
charge va sur quelle ressource en tenant compte du fait que la qualité de sortie d'un QPU *dérive
dans le temps sans qu'aucune panne ne survienne*. Les interfaces existantes couvrent deux niveaux
disjoints — les propriétés physiques changeantes du dispositif d'un côté, l'ordonnançabilité binaire
de l'autre — et le cadre qui décrirait la chaîne complète est qualifié de **visionnaire par ses
propres auteurs**.

Quatre contributions, formulées pour pouvoir être contestées : la **projection de l'état de
ressource** en objet de première classe daté et périssable ; une **architecture de référence** en
trois vues, adossée à six invariants, avec une machine d'états totale de quatre états et neuf
événements ; une **politique de délégation multicritère** déterministe et totale, vérifiable sans
matériel ni accès expérimental ; sept exigences d'**exploitabilité** avec six procédures, vingt
métriques et cinq objectifs de service, *là où la littérature opérationnelle n'en publie aucun*.

⚠ **Le travail est documentaire, et il le dit** : la plateforme n'est pas implémentée, la structure
livrée demeure numériquement non calibrée, et **huit conditions de réfutation observables par un
tiers** sont énoncées. *Seule la politique dispose d'une implémentation de référence — c'est
`rejeu-politique.py`, ci-dessous.*

## Ce que le dossier porte

⚠ **Deux des sept fichiers sont des points** : `ls` sans `-a` en montre cinq sur sept, et les deux
manquants sont le gabarit et les figures — *sans eux la source ne compile pas.*

| Fichier | | |
| --- | --- | --- |
| `article-hpc-qpu.typ` | **1 979 l. / 134 947 o.** | la source, en Typst direct — 11 sections de niveau 1, 39 de niveau 2, **26 figures**, ~19 200 mots |
| `article-hpc-qpu.pdf` | **38 p. / 750 902 o.** | le rendu livré |
| `references.bib` | **77 entrées / 676 l.** | ⭑ close dans les deux sens — voir plus bas |
| `rejeu-politique.py` | **163 l.** | ⭑ l'implémentation de référence de la politique (§ 7.2) et de la machine d'états (§ 6.4) |
| `.gabarit-arxiv.typ` | 100 l. | le gabarit *arXiv preprint* d'après `arxiv.sty` (G. Kour), porté en Typst |
| `.figures.typ` | 402 l. | les primitives de dessin des 26 planches — aucun `#figure` n'y vit, elles sont toutes appelées du corps |

## Refaire le PDF

```bash
typst compile article-hpc-qpu.typ
```

⚠ **C'est le seul dossier de document du dépôt sans `build/build-pdf.sh`**, et c'est aussi le seul
dont la source n'est pas du Markdown : les sept chaînes des autres dossiers passent par
**Pandoc → Typst**, celle-ci est du **Typst direct**. *Il n'y a donc rien à scripter d'autre que la
ligne ci-dessus — pas d'assemblage, pas d'injection de pagination, pas de gravure de figures : elles
se dessinent à la composition.* Prérequis : **Typst 0.15.1** (la version du champ `/Creator` du PDF
livré), polices **New Computer Modern** et **DejaVu Sans Mono**.

☑ **Vérifié le 1er septembre 2026 : la recomposition rend exactement 750 902 octets**, la taille du
PDF livré, et **60 octets diffèrent, en cinq endroits, tous d'horodatage** — `ModDate`,
`CreationDate`, `xmp:ModifyDate`, `xmp:CreateDate` et `xmpMM:InstanceID`. *Le `xmpMM:DocumentID`,
lui, ne bouge pas : il est dérivé du contenu, et c'est ce qui rend la comparaison concluante.*
⚠ *`SOURCE_DATE_EPOCH` ne rend pas l'octet et ne sert à rien ici : Typst compose alors l'horodatage
en UTC — `D:20260901100946Z` au lieu de `D:20260901060946-04'00` —, six caractères de moins qui
décalent tout ce qui suit, et l'écart passe de 60 à 45 342 octets.*

## Les contrôles

**☑ `python rejeu-politique.py` → 0.** *« Rejeu conforme : déroulés A et B, sensibilité, table de
transitions (36/36), gardes de hors_service. RÉF-6 non déclenchée. »* Le script rejoue les deux
déroulés publiés au § 7.5 et l'analyse de sensibilité du § 7.5.1, vérifie que la table de
transitions est **totale** — 4 états × 9 événements, aucune case absente — et éprouve les gardes de
sortie de `hors_service`. **Toute divergence fait échouer une assertion, et c'est l'exécution de la
condition de réfutation RÉF-6** : un lecteur qui referait le calcul à la main et trouverait autre
chose réfuterait la contribution. *C'est le seul contrôle du dépôt qui exécute une condition de
réfutation d'un document plutôt que de mesurer sa forme.*

**⚠⚠ `check-resume.py` sort 1 sur ce PDF, et le verdict est faux — ne pas l'enchaîner à cette
chaîne.** Le contrôle de `4 - Veille/Python/` mesure l'ordonnée la plus basse où du texte est posé
en page 1 et la confronte à une marge basse de 72 pt ; il rend ici **44,3 pt, soit −27,7 pt**. *Ses
deux prémisses tombent avec le gabarit* : **(a)** le gabarit FESP ne numérote pas sa page de titre,
celui d'arXiv y pose un folio en pied — et un pied de page vit **sous** la marge par construction,
c'est ce que le contrôle prend pour un débordement ; **(b)** le gabarit FESP compose le résumé dans
un bloc qui **ne se scinde pas**, d'où le risque de rognage silencieux qui justifie le contrôle,
quand celui-ci le compose en `pad()` de texte courant, que Typst **reporte** à la page suivante
plutôt que de le rogner. *Le risque que le contrôle surveille n'existe pas dans ce gabarit ; son
verdict n'y mesure que le numéro de page.* **Contrôle inapplicable, pas contrôle en échec.**

**☑ La bibliographie est close dans les deux sens — 77 entrées, 77 citées, et toute clé `@…` du
corps est définie.** *C'est exactement la propriété que `check-veille.py` vérifie pour la veille et
que la note de veille SDLC n'a pas.* ⚠ **Mais c'est une mesure faite pour cette passe, par aucun
script du dépôt** : rien ne la garde, et une entrée qui sortirait du corps à la prochaine révision
ne serait signalée par rien. *Deux faux positifs sont à écarter à la mesure — `fig:chrono`, qui est
une étiquette de figure, et `gmail`, pris dans l'adresse de l'auteur.*

## Deux relevés de métadonnées

⚠ **Le champ `/Author` lit `André-Guy Bruneau, M.Sc IT` — sans le point après « Sc ».** *Huitième
PDF du dépôt à porter la mention, huitième graphie possible et la seule qui l'écrive ainsi* : sept
PDF portent `M.Sc. IT`, les Vol. I, II et III portent le nom seul. **Relevé le 1er septembre 2026,
non corrigé** — la correction demande une recomposition, et elle tient en un point à la source.

☑ **Le `dc:title` porte bien l'apostrophe** — *Projection de l'état de ressource…* — là où celui de
l'état de l'art de `5 - Recension/` perd la sienne. **C'est une corroboration directe du diagnostic
posé au [`README.md` de la racine](../README.md)** : la perte se produit dans la fonction
`content-to-string` du gabarit **Pandoc**, qui rend vide sur le `smartquote` de Typst — et *cette
chaîne-ci n'a pas de Pandoc*. Le seul PDF du dépôt composé sans Pandoc est aussi le seul dont un
titre à apostrophe traverse intact.
