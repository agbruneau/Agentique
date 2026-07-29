# CLAUDE.md — dépôt *Agentique*

Guide pour Claude Code (claude.ai/code) à la **racine** du dépôt.

⚠ **Le dépôt s'appelle `Agentique`** (`github.com/agbruneau/Agentique`), pas « Monographies ». Ce
nom-là ne survit plus que dans le contenu gelé de la veille — les références [217] et [218] — et
**il n'y est pas corrigé en silence** : la veille est publiée. Les deux `index.html` qui portaient
d'anciennes URL `…/Monographies/…` ont été supprimés du dépôt le 22 juillet 2026 (commit `fd8f1be`) ;
ce reliquat est clos.

## Restructuration du 25 juillet 2026 — deux renommages et une suppression

Le commit **`60f57f6`** (« restructuration du repo ») a fait trois choses, et il faut les tenir
séparées :

| Geste | Avant | Après |
|---|---|---|
| Renommage | `1 - Corpus Agentique/` | **`1 - Corpus/`** |
| Renommage | `2 - Compendium Agentique/` | **`2 - Compendium/`** |
| Suppression | `…/1 - InteroperabiliteAgentique/Borealis-Go/` (démonstrateur Go, 12 ADR) | **retiré du dépôt** — 151 fichiers, 13 981 lignes supprimées, seule modification de contenu du commit |

⚠ **Le démonstrateur `Borealis-Go` n'est plus au dépôt, et la veille le cite toujours.** La
référence **[217]** (§4.12, « De la spécification au code ») désigne un corpus compagnon dont le
code n'est plus dans l'arbre de travail : il ne se lit plus que dans l'historique git
(`git show 60f57f6~1:'1 - Corpus Agentique/1 - InteroperabiliteAgentique/Borealis-Go/…'`).
*Un renvoi exact vers un fichier absent reste exact ; il cesse d'être opposable.* **Ne pas
« corriger » la veille** — elle est publiée, et son régime d'auto-citation est déclaré. **Ne pas
restaurer le dossier** non plus : la suppression est un geste d'auteur, daté et committé. Le fait
est consigné ici et au [`README.md`](README.md), et il n'est pas arbitré.

⚠ **Aucun `CLAUDE.md` de code ne subsiste dans le dépôt.** Celui du démonstrateur, qui primait
dans son répertoire, est parti avec lui : les quatre volumes n'ont plus que des `CLAUDE.md` de
rédaction, plus celui-ci.

## Ce que ce fichier régit — et ce qu'il ne régit pas

Ce dépôt réunit cinq livrables de périmètres distincts (voir le [`README.md`](README.md)). Les
règles ne sont **pas communes** d'un dossier à l'autre : chacun a ses conventions, et elles
divergent volontairement. Ce fichier régit deux choses seulement — la **racine du dépôt** et la
**veille technologique** qui y vit.

| Périmètre | Fichier qui fait autorité |
|---|---|
| Racine, veille technologique, arbitrages inter-volumes | **ce fichier** |
| Vol. I — *Interopérabilité agentique* (rédaction) | [`1 - Corpus/1 - InteroperabiliteAgentique/CLAUDE.md`](1%20-%20Corpus/1%20-%20InteroperabiliteAgentique/CLAUDE.md) |
| Vol. II — *L'autonomie encadrée* (rédaction, gouvernance PRD) | [`1 - Corpus/2 - OrchestrationAgentique/CLAUDE.md`](1%20-%20Corpus/2%20-%20OrchestrationAgentique/CLAUDE.md) |
| Vol. III — *L'entreprise agentique* (rédaction, gouvernance PRD) | [`1 - Corpus/3 - EntrepriseAgentique/CLAUDE.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/CLAUDE.md) |
| Vol. IV — *La somme agentique* (compendium, cadrage) | [`2 - Compendium/CLAUDE.md`](2%20-%20Compendium/CLAUDE.md) — le `TOC.md` du dossier reste la spécification de contenu |

⚠ **Le 28 juillet 2026, le Vol. IV a changé de statut pour la première fois depuis son ouverture, et
trois faits valent au niveau de la racine.** Un **audit intégral de ses cinq Livres** a été conduit
([`2 - Compendium/audit.md`](2%20-%20Compendium/audit.md) — cent constats, un seul bloquant) et **ses
huit remontées ont été soldées** (TOC v0.29, PRD v0.13). *(a)* ⚠ **Le socle consolidé existe** —
[`socle-consolide.md`](2%20-%20Compendium/PRD/socle-consolide.md), **159 entrées `S-001`…`S-159`**,
deux tables de correspondance : **la phrase « socle consolidé à zéro entrée », vraie depuis
l'ouverture du volume et répétée partout dans ce fichier, ne l'est plus** — la conserver ailleurs
dans ce document est un fait daté du 27 juillet, non l'état courant. *(b)* ☑ ⚠ **LA PORTE G-3 EST FRANCHIE** le 28 juillet 2026 (PRD v0.14, jalon **J-IV-2 atteint**) —
la première depuis G-2, et celle qui conditionne toute rédaction : **trois portes sur sept** le sont
désormais. Les **123 entrées à sensibilité temporelle du socle ont été portées à leur source
primaire** — **91 inchangées, 10 changées, 22 non établies**, domaine déclaré et clos. **Les neuf
décisions d'auteur sont prises** (D-5 le 28 juillet) : *ne plus écrire « sept sur neuf »*.
⚠ **Le résidu se cite avec le franchissement** : **22 entrées portent une date non re-vérifiée,
28 sont partielles**, et **aucune des cinquante ne porte un fait central sur sa composante non
re-vérifiée** — *91 « inchangées » n'est pas 91 « confirmées ».*
*(c)* **Le statut du volume ne change pas pour autant** : les cinquante chapitres demeurent un
**brouillon non publiable**, et **CA-IV-11 comme CA-IV-13 restent insatisfaisables** faute d'un
relecteur distinct du rédacteur. Le détail vit au [`CLAUDE.md` du
dossier](2%20-%20Compendium/CLAUDE.md) et **n'est pas repris ici**.

⚠ **Le 27 juillet 2026, le Livre V du Vol. IV — le dernier du plan — a été rédigé et arbitré, et deux
faits de ce geste valent au niveau de la racine.** Ses quatre chapitres (ch. 47-50) existent en `.md` et
`.html`, **hors portes** ; ses **seize remontées R-IV-60 à R-IV-75 sont soldées** (TOC v0.26, PRD
v0.11) ; **deux décisions d'auteur y ont été prises — D-2 et D-3 —, ce qui en porte le total à sept sur
neuf**. ⚠ **Le statut du volume ne change pas** : *une décision prise n'est pas une porte franchie* —
deux portes sur sept restent franchies, le socle consolidé compte toujours zéro entrée, et **la
publication du premier mouvement du Livre V est en outre bloquée par D-3**. Le détail vit au
[`CLAUDE.md` du dossier](2%20-%20Compendium/CLAUDE.md) et au
[`README.md` de `Livre V/`](2%20-%20Compendium/Livre%20V/README.md), et **n'est pas repris ici**.

⚠ **Le second fait est de méthode et il dépasse le Vol. IV : deux passes de rédaction ont couru en
parallèle le même jour sur le même appareil.** Le télescopage a produit trois défauts qu'**aucun
contrôle du dépôt ne voit** — une **collision d'identifiants de remontée** (deux passes puisant les
mêmes numéros), un **numéro de version d'appareil revendiqué deux fois**, et un **contrôle inter-pièces
en échec pour des fichiers qu'une autre passe n'avait pas encore committés**. *La parade retenue est une
règle d'attestation, non un outil* : **un contrôle nomme le corpus sur lequel il porte**, et quand
l'arbre de travail contient le travail d'une autre passe, il s'exécute sur **le corpus que le commit
produit**. ⚠ *Attester « le contrôle passe » sur un corpus qu'on ne committe pas est une attestation
fausse* — c'est la règle des attestations sur pièce du dépôt, appliquée au parallélisme. La règle
d'allocation des identifiants vit au PRD du volume (§13).

⚠ **Une règle de portée du Vol. IV se signale ici parce qu'elle borne le livrable, pas seulement sa
rédaction** : depuis le 27 juillet 2026, le compendium compte **au plus cinquante chapitres**, et
toute insertion se paie par une fusion dans la même passe. La règle, son protocole et son contrôle
exécutable (`C15`) vivent au [`CLAUDE.md` du dossier](2%20-%20Compendium/CLAUDE.md) et en décision 13
de son `TOC.md` — **ils ne sont pas repris ici** (périmètre des fichiers de doc : le niveau supérieur
situe et renvoie).

⚠ **Le Vol. IV n'est plus tout à fait un cadrage nu : deux livres entiers y sont rédigés, hors
portes.** Le 27 juillet 2026, sur instruction d'auteur, `2 - Compendium/Livre I/` puis
`2 - Compendium/Livre II/` ont été créés et **leurs vingt et un chapitres** — onze et dix — y ont été
rédigés en `.md` et en `.html`, **avant** les portes du PRD du volume. Quatre conséquences pour qui
édite au niveau de la racine. *(a)* Le **statut du volume est inchangé** — cadrage, **socle à zéro
entrée** : ne pas requalifier le Vol. IV en « rédigé » dans les décomptes ni dans les tableaux d'état,
un brouillon hors portes ne franchissant aucune porte.
⚠ **Deux passes d'arbitrage du 27 juillet 2026 ont fait bouger des chiffres de ce constat, et rien
d'autre** (PRD v0.9, TOC v0.25) : les **trente-sept remontées R-IV-01 à R-IV-37 sont soldées** —
treize du Livre I, vingt-quatre du Livre II —, **deux portes sur sept sont franchies** (G-2
entièrement ; G-1 pour le seul volet du Livre I) et **cinq décisions d'auteur sur neuf sont prises**
(D-1, D-4, D-6, D-7, et **D-9**, ouverte et prise dans la même passe). ⚠ **Rien
de cela ne requalifie le volume** : **G-3 n'est pas entamée**, le socle consolidé compte toujours zéro
entrée, aucun énoncé n'est central au sens de CA-IV-01, et *deux portes franchies sur sept ne font pas
un volume recevable*. *(b)* ⚠ **Le Livre II enfreint une porte de plus que le Livre I, et l'arbitrage
ne l'efface pas.** Il est rédigé avant **G-3 et G-4** — et **G-4, la collation de fond contre le
Vol. III rédigé, est le préalable que le PRD nomme pour ce Livre précisément**, sa source se déclarant
elle-même *non publiable* ; il enfreint en outre l'**ordre de rédaction** du PRD §6. ⚠ **Le fait de
méthode que sa clôture a établi vaut au-delà de lui** : **cinq de ses treize thèses portaient une forme
que leur source avait bornée le 21 juillet 2026 et reportée dans ses pièces le 22**, sans que le plan
suive — *cinq reports qui n'avaient pas été faits, non cinq divergences à arbitrer* —, et **aucune
pièce ne pouvait le voir seule**, chacune étant cohérente isolément. La **décision 14 du TOC** en fait
une obligation de passe, domaine de balayage déclaré. ⚠ **Et une condition de publication n'est
satisfaisable par aucune passe du volume en l'état** : CA-IV-11 et CA-IV-13 exigent un **relecteur
distinct du rédacteur**, que D-6 ne fournit pas — *arbitrer n'est pas relire*, et *une lacune de socle
se comble par une source ; celle-ci ne se comble que par une seconde personne.*
*(c)* **Le régime de la veille ne bouge pas non plus** :
sa réf. [220] décrit le Vol. IV comme un cadrage sans chapitre, et cela reste vrai *à sa date* — c'est
un troisième écart de la même famille que les deux déjà consignés plus bas (Vol. III rédigé,
démonstrateur retiré), **signalé ici, jamais corrigé dans la veille**. *(d)* Le détail, l'issue de
chaque remontée, la volumétrie des deux livres et le régime des deux rendus vivent au
[`CLAUDE.md` du dossier](2%20-%20Compendium/CLAUDE.md) et aux `README.md` de `Livre I/` et de
`Livre II/` — ils ne sont pas repris ici.

⚠ **Le paragraphe qui précède est daté, et son cardinal — « deux livres » — est périmé sans être
remplaçable aujourd'hui.** Le **27 juillet 2026**, toujours sur instruction d'auteur,
[`2 - Compendium/Livre III/`](2%20-%20Compendium/Livre%20III/) a été créé et **ses quinze chapitres**
— ch. 22 à 36 — y ont été rédigés en deux rendus chacun, puis **ses vingt-quatre remontées R-IV-76 à
R-IV-99 soldées** (TOC v0.27, PRD v0.10) ; **une passe distincte écrivait simultanément les Livres IV
et V dans le même dépôt**. ⚠ **Le total n'est donc PAS recalculé ici** : *un cardinal mesuré pendant
que des pièces s'écrivent est faux à la seconde où on le publie* — il se re-mesure **au terme des deux
passes**, ensemble, comme la règle des décomptes l'exige. **Quatre faits valent au niveau de la
racine.** *(a)* ⚠ **Le statut du Vol. IV reste inchangé** — cadrage, socle à **zéro entrée**, **G-3 non
entamée** : *ne pas le requalifier en « rédigé »*, trois livres de brouillon hors portes n'en faisant
pas davantage que deux. *(b)* ⚠ **L'écart du Livre III est d'un ordre neuf : il enfreint une DÉCISION
D'AUTEUR, non une seule porte.** Les **ch. 25 et 27** ont été rédigés alors que **D-9** déclare son lot
d'instruction **bloquant pour eux deux**, et **ils prescrivent l'un et l'autre la parade dont ce lot est
la limite empirique** ; *l'infraction est nommée à chaque pièce, et l'arbitrage qui l'a suivie la solde
sans la rattraper.* *(c)* ⚠ **Le régime de la veille ne bouge pas davantage** : sa réf. [220] décrit le
Vol. IV comme un cadrage sans chapitre, et cela **reste vrai à sa date** — même famille que les trois
écarts déjà consignés, **signalé ici, jamais corrigé dans la veille**. *(d)* ⚠ **Deux réconciliations
sont dues entre les passes concurrentes** : la **numérotation de version du PRD**, et le **versement des
huit sièges du Livre III** à `check-sieges.py`, reporté parce que *payer une dette d'outillage pendant
qu'un autre écrit le même fichier produirait une table incohérente que le harnais de mutation ne
détecterait pas*. Le détail vit au [`CLAUDE.md` du dossier](2%20-%20Compendium/CLAUDE.md) et au
`README.md` de `Livre III/`.

⚠ **Les deux passes concurrentes sont closes depuis le 27 juillet 2026, et le cardinal se re-mesure
enfin — il vaut CINQ.** Les **dix chapitres du Livre IV** (ch. 37-46) et les **quatre du Livre V**
(ch. 47-50) ont été rédigés et arbitrés le même jour ; **les cinq livres du plan existent donc en
brouillon hors portes**, soit **cinquante chapitres sur cinquante**. ⚠ **Rien de cela ne requalifie le
volume** : *le socle consolidé compte toujours **zéro entrée**, **G-3 n'est pas entamée**, aucun énoncé
n'est central au sens de CA-IV-01, et **CA-IV-13 n'est satisfaite pour aucune pièce*** — **ne pas
écrire « Vol. IV rédigé » dans un décompte ni dans un tableau d'état**. *Cinquante chapitres écrits
hors portes ne franchissent aucune porte ; ils en documentent le coût.* **Trois faits de la passe du
Livre IV valent au niveau de la racine.** *(a)* ⚠ **Une collision d'identifiants entre passes
concurrentes s'est produite et a été résolue** : *trois passes numérotant dans une série partagée sans
allocation préalable ont alloué **dix numéros deux fois** ; la renumérotation a porté sur le Livre IV,
dont l'arbitrage n'était pas publié, et ses remontées des ch. 44-46 passent de R-IV-60…69 à
**R-IV-100…109**.* ⚠ **Aucun instrument versionné ne rapproche deux plages de remontées** — *la
collision n'a été trouvée qu'à la main, et c'est une dette d'appareil déclarée qui vaut pour tout le
dépôt.* *(b)* ⚠ **Une classe de désalignement neuve est apparue, INTERNE AU PLAN** : *le TOC se
contredisait lui-même en deux endroits — une numérotation de sous-sections empruntée à un autre
chapitre, un titre de section contredisant sa propre note de provenance —, et **aucun des quinze
contrôles ne voit cette classe**.* *(c)* ⚠ **Une réconciliation reste due et elle s'alourdit** : *le
**versement des huit sièges du Livre III** à `check-sieges.py` n'a pas été fait, la table portant
aujourd'hui **douze sièges** — les trois du Livre I, les quatre du Livre II, les deux du Livre V et
les trois du Livre IV.* **La numérotation de version du PRD, elle, est réconciliée** : les passes se
sont succédé en v0.10, v0.11 puis **v0.12**, et aucune rangée n'est en double.

⚠ **Un fait de méthode se signale ici parce qu'il vaut au-delà du Vol. IV.** La rédaction des ch. 10
et 11 a révélé deux fois la même classe de défaut : une **lacune déclarée du socle d'un volume**
comblée par le **texte rédigé d'un autre volume** du dépôt. *Ce n'est pas une contradiction entre
volumes* — « le socle de A ne documente pas X » et « B documente X » sont logiquement compatibles —,
et **le volume le plus ancien ne se corrige pas** : sa lacune de couverture est une information
datée, du même ordre que la date d'une revue publiée. La règle générale du dépôt (« deux faits datés
divergent entre la veille et le Vol. II : ils sont **signalés, non arbitrés** ») s'y applique
intégralement.

**Le fichier le plus spécifique gagne.** En travaillant dans un dossier de volume, appliquer son
`CLAUDE.md`, pas celui-ci.

## Divergences de conventions entre volumes — à ne pas uniformiser

Ces écarts sont **délibérés** ; les corriger « pour la cohérence » casserait des références
croisées ou l'historique d'un volume.

| | Vol. I | Vol. II |
|---|---|---|
| Messages de commit | courts, **en français**, par livrable (`Chapitre 5`, `Annexe B`) | **Conventional Commits en anglais** (`docs(mono): …`) |
| Autorité de contenu | les conventions de chapitres du `CLAUDE.md` | le **PRD** (`prd/PRD.md`), qui prime sur tout |
| Traçabilité des faits | vérification adverse des citations, bilan par bibliographie | socle factuel **F-xx** avec niveaux **[A]/[B]/[C]** |
| Pipeline PDF | FESP (Mermaid → Pandoc → Typst) | **copie** du FESP + `assemble.py` en amont |

Les trois pipelines PDF **FESP** (Vol. I, Vol. II et — depuis le 23 juillet 2026 — Vol. III) sont des
copies indépendantes : **un correctif à l'un ne se propage pas aux autres.** La veille, elle,
n'utilise aucun des trois (voir plus bas). Le Vol. III a reçu sa copie en P5.4, sur demande de
l'auteur, au gabarit FESP des monographies : c'était bien une troisième copie, décidée et datée.

⚠ **Un QUATRIÈME pipeline existe depuis le 29 juillet 2026, et ce n'est pas une quatrième copie du
FESP.** Le Vol. IV a reçu le sien — [`2 - Compendium/build/`](2%20-%20Compendium/build/) : gabarit
Typst propre, format 155 × 235 mm au style des monographies Springer, sortie
[`compendium.pdf`](2%20-%20Compendium/compendium.pdf), **847 pages, sans aucune page blanche**. Il ne dérive d'aucune des trois
copies et aucune ne dérive de lui ; la règle d'indépendance vaut donc pour **quatre**. ⚠ **Composer
n'est pas publier** : le rendu ne requalifie rien, les cinquante chapitres demeurent un **brouillon
non publiable** et le PDF le déclare en liminaire. Le détail — ce que le rendu retire, et comment il
marque les renvois que la coupe laisserait pendre — vit au [`CLAUDE.md` du
dossier](2%20-%20Compendium/CLAUDE.md) et **n'est pas repris ici**.

Le Vol. III prolonge l'appareil du Vol. II mais s'en écarte sur quatre points (motifs de balayage,
commande de décompte, escalade de gouvernance, numérotation des garde-fous). Ces écarts sont
consignés et motivés dans [son propre `CLAUDE.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/CLAUDE.md) —
**les y lire avant d'appliquer une règle du Vol. II de mémoire.**

## Veille technologique — le livrable de la racine

`Veille Technologique.md` → `Veille Technologique.pdf` (**146 p.**, 14 sections numérotées,
**257 références**, 15 tableaux — **édition intégrale du 18 juillet 2026, passe complémentaire du
23 juillet 2026** : sous-section 12.4, l'après-agentique en préimpression, références [245] à [256],
régime déclaré — résumés arXiv seuls consultés, sans vérification adverse ; la 257e, ajoutée le même
jour, réattribue les métriques du cas Block du playbook [62] à l'exposé public qui les porte [257],
sous réserve de régime). Document **autonome** :
il n'est repris dans aucune monographie, et il est le seul à citer les volumes du dépôt.

⚠ **Depuis l'édition intégrale, la veille cite les quatre volumes — mais à deux régimes distincts,
et l'écart est la règle qui compte.** Les Vol. I et II sont **rédigés** et fournissent des faits :
§4.12 pour le démonstrateur `Borealis-Go` (réf. [217]), §8.4 pour le croisement canadien
(réf. [218]). Les Vol. III et IV y sont des **cadrages** — zéro chapitre, zéro entrée de socle
propre — et ne fournissent **aucun fait** : ils prêtent des instruments d'analyse (la grille des
cinq questions, les décisions de fusion), marqués comme constructions d'auteur, et leurs entrées
bibliographiques [219] et [220] portent cette réserve en toutes lettres. **Ne jamais élever un
cadrage au rang de source de fait** en le citant à l'appui d'un énoncé : c'est la faute que ces deux
cadrages prennent eux-mêmes pour objet. Le régime est posé en §13.1 et tenu à chaque occurrence.

⚠ **Ce régime est celui de la veille à sa date, et deux faits l'ont dépassé sans le périmer.**
*(a)* Le **Vol. III est rédigé depuis le 22 juillet 2026** — 34 pièces, socle propre de 98 entrées —
alors que la réf. [219] le décrit comme un cadrage sans chapitre ; *(b)* le **démonstrateur de la
réf. [217] a été retiré du dépôt le 25 juillet 2026**. Les deux écarts se **signalent ici, jamais
dans la veille** : une revue publiée décrit l'état de ses sources à son gel, et la rattraper
après coup effacerait la seule information qu'elle porte — sa date. Une future édition les reprendra
comme faits nouveaux, sous son propre régime de vérification.

⚠ **La section 13 porte une date propre.** Elle est passée sur la **v0.3 du `TOC.md` du Vol. IV,
datée du 19 juillet 2026** — soit le lendemain de la date d'édition de la veille. L'écart est
assumé et déclaré dans le texte (§13.5 et §2.2) ; les sections 1 à 12 restent à leur date d'état.
Ne pas « harmoniser » cette date : un cadrage qui se révise plus vite que la revue ne se gèle est
un constat de la §10, pas une incohérence à lisser.

La section 13 (« Le corpus compagnon : quatre volumes, un compendium, un même objet ») est le siège de ce rendu
de compte ; la Conclusion est devenue la section **14**. L'auto-citation est assumée et divulguée ;
ses limites — dont le risque de circularité, quatre volumes partageant un auteur — sont exposées
en section 10.

### Rendu

Invocation Pandoc **directe**, gabarit Typst *par défaut* — jamais `build/build-pdf.sh` :

```bash
pandoc "Veille Technologique.md" --pdf-engine=typst --toc -o "Veille Technologique.pdf"
```

Son identité visuelle (police New Computer Modern, mise en page) vient du gabarit par défaut, pas
d'un `.template` du dépôt. **Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, police New Computer Modern.

### Conventions de rédaction

- **En-tête YAML complet** : titre, auteur (avec la date d'édition), résumé,
  `mainfont: "New Computer Modern"`, `section-numbering: "1.1.1"`.
- **Sections `#` numérotées automatiquement** par Pandoc (Introduction = 1 … Conclusion = **14**) ;
  ⚠ **le corps cite ses sections en clair** (« section 4.11.5 », « section 9.6 ») : insérer une
  section de tête au milieu décale toute la numérotation aval et casse ces renvois. Ajouter en
  **sous-section** (l'ajout en queue ne décale rien) ou, si une section de tête est nécessaire,
  l'insérer juste avant la Conclusion et corriger les renvois. Même piège pour les **tableaux**,
  numérotés automatiquement : une table insérée en amont décale les « tableau N » cités en aval.
  Ces deux pièges sont couverts par `check-veille.py` (voir plus bas). Les sous-sections `##` deviennent `N.1` ; les
  sections liminaires ou finales sans numéro portent `{-}` (`# Sommaire exécutif {-}`,
  `# Divulgation {-}`, `# Références {-}`). **Toute table porte une légende** (ligne `: …`) : une
  table sans légende consomme quand même un numéro et creuse un trou dans la série.
- **Décomptes annoncés en toutes lettres.** Le corps annonce ses propres cardinaux — « dix
  constats », « quatorze contributions », « vingt questions ouvertes ». ⚠ **Ils ne se mettent pas à
  jour tout seuls** : ajouter un item sans re-mesurer produit une contradiction interne que la
  relecture attrape mais que le rendu ne signale pas. Le piège n'est pas le nombre posé au titre de
  la liste — c'est celui qui la **cite à distance** (sommaire exécutif, conclusion, divulgation).
  Couvert par `check-veille.py`.
- **Tri épistémique** : la section 12 (*Horizon prospectif 2027-2030*) trie ses sous-sections en
  **PROGRAMMÉ / PROJETÉ / SPÉCULATIF** — même logique que le ch. 7 du Vol. I. Ne jamais présenter
  du spéculatif comme acquis.
- **Références manuelles** : liste numérotée sous `# Références {-}`, dans un bloc
  `::: {#refs} … :::`. Le corps cite par crochets **littéraux** `[N]` — **pas** de champ
  `bibliography` Pandoc, **pas** de clés `@…`. Toucher au compte oblige à reporter le nouveau total
  ici, dans le [`README.md`](README.md) et dans le bilan de vérification de la veille.
- **Ressources vivantes** : les références précédées de ⚠ sont des pages sans version datée stable ;
  ne pas retirer le marqueur sans avoir figé une version. ⚠ **Le marqueur ne sert qu'à cela.** Une
  réserve portant sur le *contenu* d'une source (« non adopté », « errata publiés après parution »,
  « aucun chapitre rédigé ») s'écrit **`**Réserve —**`**, jamais avec ⚠ : surcharger le marqueur
  rend indistinguables une page qui bouge et un fait qu'il faut nuancer.
- **Pas deux entrées pour un même document.** Avant d'ajouter une référence, vérifier qu'aucune
  entrée ne porte déjà la même URL, le même DOI ou le même identifiant arXiv — l'édition intégrale
  a dû en fusionner deux paires. Couvert par `check-veille.py`, qui normalise les URL (`http`/`https`,
  `www`, barre finale, `/abs/` vs `/pdf/`, suffixe de version) : deux formes différentes du même
  document ne se voient pas à l'œil.

### Contrôles de publication — `check-veille.py`

```bash
python check-veille.py    # sortie 0 si tout passe, 1 sinon
```

**À exécuter avant chaque `pandoc`.** Couvre les quatre défauts que le rendu ne signale jamais :
renvois de section et de tableau non résolus (y compris `§N.M` et `QO n`), tables sans légende,
cardinaux en toutes lettres périmés, doublons bibliographiques, références pendantes ou orphelines.

⚠ **Ce script est du contenu : il se vérifie comme le reste.** Trois faux positifs y sont déjà
neutralisés, et les réintroduire en « simplifiant » un motif rendrait le contrôle bruyant donc
ignoré : `(8.9)` et `(2.0)` sont des **numéros de version**, pas des renvois ; « quatre-vingt-dix »
contient « vingt-dix », qui n'est pas un nombre ; « constats » et « questions » servent aussi à des
énumérations **locales** légitimes (« Trois constats se dégagent », la grille des « cinq questions »
de la §7.6) — d'où l'ancrage des cardinaux sur la tournure d'annonce et non sur le nom nu. Avant de
publier une modification du script, la valider par mutation : introduire chacune des fautes dans une
copie et vérifier que le script **échoue**, après avoir constaté qu'il **passe** sur le document
intact — sans cette seconde vérification, un script cassé « détecte » tout.
- **Sauts de page** via blocs Typst bruts ` ```{=typst} #pagebreak(weak: true) ``` ` ; le saut avant
  la table des matières passe par `header-includes`
  (`#show outline: it => [#pagebreak(weak: true) #it]`).

### Méthode

Revue **structurée et vérifiée** : chaque énoncé factuel est adossé à une source primaire consultée
et soumis à contradiction — vérificateurs indépendants chargés de *réfuter*, contre-vérification
directe sinon. Les métriques d'adoption auto-déclarées sont attribuées à leur source à chaque
occurrence ; un statut *preview* n'est jamais présenté comme une disponibilité générale.

## Règles valant pour tout le dépôt

- **Flux git — committer tout et pousser sur `main`.** *(Consigne d'auteur du 27 juillet 2026.)*
  Le travail terminé se **committe en entier** — jamais de fichier laissé de côté — et se **pousse
  directement sur `main`**, sans passer par une branche de travail ni par une *pull request*.
  Ne pas demander confirmation à chaque fois : la consigne vaut autorisation permanente. Trois
  précisions qui la bornent sans l'affaiblir. *(a)* **Rien ne dispense des contrôles** : `check-veille.py`
  et `PRD/check-toc.py` s'exécutent **avant** le commit qui touche leur domaine, et un contrôle en
  échec interdit de pousser — pousser vite n'est pas pousser n'importe quoi. *(b)* **La règle du PDF
  versionné avec sa source tient** (voir ci-dessous) : un `.md` poussé sans son `.pdf` régénéré est un
  commit incomplet, quelle que soit la hâte. *(c)* **La consigne ne couvre pas le destructif** :
  réécriture d'historique, poussée forcée, suppression de branche ou de fichier versionné se
  demandent, comme avant. ⚠ Cette règle est un **choix de flux, pas une doctrine de qualité** : elle
  supprime l'étape de revue, elle ne supprime pas la relecture.
  L'allègement des invites correspondant est au [`.claude/settings.json`](.claude/settings.json),
  versionné pour survivre au reclonage du dépôt.
- **Langue.** Livrables et prose en **français canadien** soutenu ; ton professionnel et neutre
  (pas de marketing, pas de première personne). Terminologie technique anglaise entre parenthèses à
  la première occurrence ; citations verbatim en langue originale.
- **PDF versionné avec sa source.** Régénérer et pousser le `.pdf` avec le `.md` — jamais la source
  seule. Vaut pour la veille, pour les **trois** monographies et — depuis le 29 juillet 2026 — pour
  le **compendium** : toucher une pièce d'un Livre du Vol. IV oblige à recomposer
  [`compendium.pdf`](2%20-%20Compendium/compendium.pdf) dans le même commit
  (`bash build/build-pdf.sh` depuis `2 - Compendium/`). ⚠ **Cinq rendus, pas quatre**, et le PDF du
  compendium est le seul qui compose des pièces qui se déclarent elles-mêmes non publiables.
- **Décomptes.** Toute pagination, tout compte de références, de chapitres ou de pièces annoncé
  dans un `README.md` ou un `CLAUDE.md` doit être **re-mesuré** avant d'être modifié, jamais
  recopié d'un autre document. Un même chiffre vit souvent à plusieurs endroits (README du dépôt,
  README du volume, `CLAUDE.md`, PRD, TOC, registre de gel) : les mettre à jour ensemble.
- **Faits datés.** Le domaine se périme par trimestres. Les échéances à revalider sont tenues dans
  la section « Ce qui reste vivant » du [`README.md`](README.md) ; chaque volume porte en plus ses
  propres dates de gel. Deux faits datés divergent entre la veille et le Vol. II : ils sont
  **signalés, non arbitrés** — ne pas les uniformiser en silence.
- **Lacunes exposées, non comblées.** Aucune lacune déclarée d'un volume ne se comble par une
  source de moindre qualité.
- **Périmètre des fichiers de doc.** Un `README.md` s'adresse au lecteur, un `CLAUDE.md` à l'agent
  qui édite. Ne pas dupliquer d'un niveau à l'autre : le niveau supérieur situe et renvoie, le
  niveau inférieur détaille.
