# CLAUDE.md — Vol. IV, *La somme agentique* (compendium intégral)

Guide pour Claude Code (claude.ai/code) dans le dossier `2 - Compendium` (renommé le 25 juillet 2026,
`2 - Compendium Agentique` auparavant, commit `60f57f6`). **Le fichier le
plus spécifique gagne** : ici, celui-ci ; les règles valant pour tout le dépôt (langue, décomptes,
faits datés, périmètre des fichiers de doc) sont au [`CLAUDE.md` racine](../CLAUDE.md) et ne sont
pas répétées.

⚠ **ÉTAT AU 29 JUILLET 2026 — L'OUVRAGE EST ARRÊTÉ, et c'est la première chose à savoir avant
d'éditer quoi que ce soit ici.** La décision d'auteur **D-10** (PRD **v0.15** §14, TOC **v0.31**) place
le compendium au statut de révision **RÉVISION FINALE**, sous un **régime de diffusion en bibliothèque
personnelle** : lecture par l'auteur, **aucune mise à disposition d'un tiers**, aucun dépôt public,
**aucune opposabilité**. **Quatre choses en découlent pour qui édite.** *(1)* ⚠ **Plus aucune passe de
rédaction n'est prévue** : les cinquante chapitres sont **arrêtés dans leur état du 29 juillet 2026**.
Une modification de pièce reste possible — une faute se corrige —, mais elle **rouvre la passe** :
elle se recompose (`bash build/build-pdf.sh`) et se déclare. *(2)* ⚠ **« Arrêté » n'est ni « terminé »
ni « conforme », et les trois ne se substituent jamais l'un à l'autre.** **G-2, G-3 et G-7 sont
satisfaites sur pièce** ; **G-1 (deux volets résiduels), G-4 (fond), G-5 (balayage) et G-6 (trois
lots, socle du ch. 41) sont closes POUR CE SEUL RÉGIME, par dérogation nommée**, leur résidu entier et
écrit ; **CA-IV-11 et CA-IV-13 sont dérogés, non satisfaits** — il n'y a toujours pas de relecteur
distinct du rédacteur. *(3)* ⚠ **Le motif de la dérogation est étroit et il est unique** : *lecteur et
rédacteur sont la même personne, il n'y a aucun tiers à protéger d'une affirmation non réfutée.* **La
dérogation tombe avec ce motif** — à la première diffusion, les quatre portes et les deux critères
redeviennent exigibles dans leur état du PRD §5 et §11, et **citer le §14 hors de son régime serait
une fausse attestation** (CA-IV-14). *(4)* ⚠ **Rien de tout cela ne rend un énoncé central** :
CA-IV-01 reste tenu **par abstention**, **aucun vote adversarial n'a été conduit**, et **les trois
volumes sources font toujours foi**. *Ne jamais écrire « conforme à toutes les portes », « publiable »
ni « terminé » : écrire « arrêté », et renvoyer au PRD §14.*

⚠ **ÉTAT AU 28 JUILLET 2026 — la passe d'audit, et le seul changement de statut que le volume ait
connu jusque-là depuis son ouverture.** Un **audit intégral des cinq Livres** ([`audit.md`](audit.md), cent
constats sur le corpus du commit `8cb40fa`, un seul bloquant) a été conduit, puis **ses huit
remontées soldées** — TOC **v0.29**, PRD **v0.13**. **Cinq faits conditionnent toute édition ici.**
*(1)* ⚠ **LE SOCLE CONSOLIDÉ EXISTE** : [`PRD/socle-consolide.md`](PRD/socle-consolide.md) v1.0 porte
**159 entrées `S-001`…`S-159`** — 46 du Vol. II, 96 du Vol. III, 17 du Vol. I en `[C]` —, **deux
tables de correspondance**, **13 entrées héritées fondues**, **5 exclues**, identité de clôture
vérifiée (*177 sources = 159 + 13 + 5*). **La phrase « socle consolidé : zéro entrée », vraie depuis
l'ouverture du volume, ne l'est plus — ne plus l'écrire.** *(2)* ☑ ⚠ **LA PORTE G-3 EST FRANCHIE** (28 juillet 2026, PRD v0.14, jalon **J-IV-2 atteint**) — la première depuis G-2, et celle que le PRD déclare conditionner **toute rédaction**. Ses quatre termes sont livrés : socle numéroté, deux tables, **re-datation à la source primaire** des **123 entrées à sensibilité temporelle** (**91 inchangées, 10 changées, 22 non établies**, domaine déclaré et clos), et `check-compendium.py` **validé par mutation** (P1-P8, 17 mutations). **Trois portes sur sept sont désormais franchies.** ⚠ **Le résidu fait partie du franchissement et se cite avec lui** : **22 entrées portent une date non re-vérifiée, 28 sont partielles**, et **aucune des cinquante ne porte un fait central sur sa composante non re-vérifiée** ; les entrées **intégralement ré-établies sont 63 sur 123**. *Ne jamais écrire « 91 confirmées ».* **Aucun vote adversarial n'est conduit**, et il reste dû pour toute entrée appelée à porter un fait central. *(3)* ⚠ **Les NEUF décisions d'auteur sont prises** — **D-5** l'a été le
28 juillet (ancrage de la *Synthèse* du Vol. I à l'arbre gelé `fd8f1be~1`, vérifié sur pièce ;
restauration écartée, repointage interdit). *Ne plus écrire « sept sur neuf » ni « huit sur neuf ».*
*(4)* **L'appareil compte quatre contrôles**, chacun exécuté seul : `check-toc.py` (C1-C15),
`check-sieges.py` (**26 sièges** sur 50 pièces, 108 mutations), **`check-compendium.py` (P1-P8,
17 mutations)** et `decompte.sh`, plus le **registre de gel** à 50 lignes. ⚠ *Cette rangée portait
« P1-P7, 15 mutations » — la valeur d'avant le versement de **P8**, que le franchissement de G-3 a
justement ajouté ; corrigée le 29 juillet 2026 sur la sortie du script.* *(5)* ⚠ **La volumétrie a
bougé et se re-mesure, jamais ne se recopie** : **300 780 mots** de corps (I 64 750 · II 62 054 ·
III 91 477 · IV 56 025 · V 26 474) pour 308 000 d'enveloppe, **−2,3 %** — mais **cent trois points
d'amplitude** entre les pièces extrêmes. ⚠ **Le statut du volume ne change pas pour autant** : les
cinquante chapitres demeurent un **brouillon non publiable**, **CA-IV-11 et CA-IV-13 restent
insatisfaisables** faute de relecteur tiers, et la publication du premier mouvement du Livre V reste
bloquée par D-3.

⚠ **État au 27 juillet 2026, en tête parce qu'il conditionne toute édition : le Livre V — le DERNIER
du plan — est rédigé et arbitré, et sa publication est bloquée par une décision d'auteur.** Ses
**quatre chapitres** (ch. 47-50) vivent au dossier [`Livre V/`](Livre%20V/), en `.md` et `.html`, **hors
portes** : le premier mouvement (ch. 47-48) a été écrit avant **G-3, G-5 et G-6** — *les deux dernières
sont les portes que le PRD nomme pour ce mouvement précisément* —, le second avant **G-3 et G-4**. Six
faits à connaître avant d'y toucher. *(1)* **Ses seize remontées R-IV-60 à R-IV-75 sont soldées** (TOC
v0.26, PRD v0.11) ; le tableau des issues est au [`README.md` de `Livre V/`](Livre%20V/README.md) et
**n'est pas repris ici**. *(2)* ⚠ **Deux décisions d'auteur sont prises, et elles bornent sans combler**
: **D-2** — le risque 14 (la couche d'exécution) tranché en **sections dans l'existant, sans chapitre
neuf**, le plafond de cinquante interdisant d'en ouvrir un sans fusion ; **D-3** — la matière neuve en
**trois lots d'instruction ouverts, retrait non exécuté, publication du premier mouvement bloquée
jusqu'à leur clôture, une instruction infructueuse valant retrait**. **Sept décisions sur neuf étaient alors prises ; ⚠ les NEUF le sont depuis le 28 juillet 2026 (D-8 le 27, D-5 le 28) — la phrase qui suit est datée du 27 et n'est plus l'état courant.** *(Forme d'origine : « Sept décisions sur neuf sont
désormais prises** ; D-5 et D-8 restent ouvertes. *(3)* ⚠ **Aucune porte n'est franchie pour autant** :
*une décision prise n'est pas une porte franchie — D-3 ouvre des lots, elle ne constitue pas un socle.*
*(4)* ⚠ **Sa volumétrie est en DÉFAUT, et c'est le premier Livre dans ce cas** : **25 017 mots** pour une
enveloppe de 34 000, soit **−26,4 %**, l'écart se concentrant sur les deux chapitres sans socle (−42,7 %
et −40,6 %). *Sur un front dont la ligne Fusion déclare « sources primaires à constituer avant
rédaction », la volumétrie mesure l'absence de sources* — et **quatre sections sont des lots
d'instruction plutôt que du contenu**, seul geste que le régime de preuve autorisait. *(5)* **Deux
sièges y sont posés** (voir la table des sièges plus bas). *(6)* ⚠ **Un fait de terrain a marqué la
passe et il n'est pas au plan** : les Livres III et IV ont été rédigés **en parallèle**, le même jour,
hors d'elle — d'où une **collision d'identifiants de remontée** (R-IV-75, règle d'allocation portée au
PRD §13), un **numéro de version d'appareil revendiqué deux fois**, et l'obligation d'exécuter
`check-sieges.py` sur **le corpus que le commit produit** plutôt que sur l'arbre de travail. *Attester
« le contrôle passe » sur un corpus qu'on ne committe pas serait une attestation fausse.*

## Les livrables — un plan, sa gouvernance et sa vue synoptique, pas un ouvrage

⚠ **Réorganisation du 23 juillet 2026** : le PRD, le TOC et les deux scripts de contrôle vivent
désormais dans le sous-dossier [`PRD/`](PRD/) ; le README (conspectus) et ce `CLAUDE.md` restent à
la racine du dossier. Les chemins ci-dessous et la commande de contrôle (§ protocole) en tiennent
compte.

Trois fichiers, par ordre d'autorité. [`PRD.md`](PRD/PRD.md) (**v0.15, 29 juillet 2026 — version
courante, celle de l'arrêt : D-10, régime de diffusion déclaré, conformité arrêtée porte par porte** ;
⚠ *la rangée annonçait « v0.11, 27 juillet 2026 » jusqu'au 29 juillet 2026, soit quatre versions de
retard — une estampille d'autorité en retard est fausse, à la différence d'un constat daté, et ce qui
suit est désormais lu comme **historique**.* — ⚠ **troisième passe d'arbitrage, celle du Livre V** : **D-2** tranchée — risque 14 en *sections dans l'existant, sans chapitre neuf* — et **D-3** — matière neuve en *trois lots ouverts, retrait non exécuté, publication du premier mouvement bloquée* ; **seize remontées soldées**, **sept décisions sur neuf**, **aucune porte franchie** ; seconde passe d'arbitrage : **D-4 tranchée** — enveloppes maintenues, amputation interdite — et **D-9 ouverte et prise** — lot d'instruction du § 17.5, bloquant pour les ch. 25 et 27 ; **vingt-quatre remontées soldées**, **aucune porte franchie** ; cumul : **cinq décisions sur neuf**, **deux portes sur sept**. ⚠ C'est aussi la version qui déclare **CA-IV-11 et CA-IV-13 insatisfaisables en l'état**, D-6 ne fournissant pas de relecteur tiers) régit la
**gouvernance de la rédaction** — portes de lancement, ordre, régimes de preuve, seuil de vote,
critères CA-IV, jalons, décisions d'auteur — et **prime en cas de conflit sur la gouvernance, le
socle et les lacunes**. [`TOC.md`](PRD/TOC.md) (**v0.31, 29 juillet 2026 — version courante : le plan
est arrêté, aucune structure ne bouge** ; ⚠ *la rangée annonçait « v0.26, 27 juillet 2026 » jusqu'au
29 juillet 2026, cinq versions de retard, corrigé dans la même passe que celle du PRD ci-dessus* — **historique — troisième arbitrage : structure inchangée, trois thèses réalignées (ch. 47 second mouvement, ch. 48, ch. 49 second mouvement), deux sièges désignés et versés, inventaire des lacunes du Vol. III requalifié ; second arbitrage : structure inchangée, cinq thèses réalignées (ch. 14, 15, 16, 17, 19), décision 14 posée, risque 17 ouvert, troisième table à l'Annexe C ; 50 chapitres en 5 livres,
projection ≈ 376 000–401 000 mots ; plafond de cinquante chapitres posé en décision 13 et contrôlé par C15 ;
le ch. 41, la fabrique d'agents, entré en v0.22, est payé par la fusion des ch. 47 et 48**) reste la *spécification de contenu* du compendium — autorité
sur le découpage et sur chaque chapitre (thèse, sections, ligne Fusion, socle, garde-fous) ;
**aucun chapitre n'est rédigé au sens des portes**. ⚠ **Tant que la somme n'est pas *recevable*, les
trois volumes sources font foi** (champ Statut du TOC), et une thèse de ce plan n'est pas une source
(sa propre décision 8). ⚠ *La formule antérieure — « tant que la somme n'est pas **écrite** » — est
périmée depuis le 27 juillet 2026 et corrigée le 29 : **les cinquante chapitres sont écrits**, et
c'est précisément le cas où la formule ancienne se lirait comme une levée de la règle de
substitution. **Écrit, arbitré, audité, composé et arrêté ne valent pas recevable.*** [`README.md`](README.md) est la **vue synoptique dérivée** du TOC (le « conspectus » du volume, même
version en tête) : il ne porte aucune décision, aucun socle, aucun garde-fou propre — en cas
d'écart, **le TOC prime**, et toute passe qui modifie le TOC réaligne le conspectus (version,
faits touchés) ou y déclare le retard en tête.

⚠ **Deux livres entiers existent pourtant dans le dossier, et ils sont hors portes — fait signalé
ici, non arbitré.** Le **27 juillet 2026, sur instruction d'auteur**, les répertoires
[`Livre I/`](Livre%20I/) et [`Livre II/`](Livre%20II/) ont été créés et **leurs vingt et un
chapitres** — onze au Livre I, dix au Livre II — y ont été rédigés en deux rendus chacun (`.md`
source, `.html` de lecture à thème sombre), **avant** le franchissement des portes que le PRD §5 pose
comme préalables. ⚠ **Les deux écarts ne sont pas du même ordre, et les confondre effacerait le
second.** Le Livre I a été écrit avant **G-1, G-2 et G-3** ; le **Livre II** l'est avant **G-3 et
G-4** — et **G-4, la collation de fond contre le Vol. III rédigé, est le préalable que le PRD nomme
pour ce Livre précisément**, sa source se déclarant elle-même *non publiable*. Il enfreint en outre
**l'ordre de rédaction du PRD §6**, qui le plaçait en troisième position. ⚠ **Le Livre II a ouvert
vingt-quatre remontées — R-IV-14 à R-IV-37, dont deux bloquantes — et LES VINGT-QUATRE SONT SOLDÉES
depuis le 27 juillet 2026** (TOC v0.25, PRD v0.9) ; leur tableau d'issues est au
[`README.md` de `Livre II/`](Livre%20II/README.md) et **n'est pas repris ici**. ⚠ **Sa volumétrie réelle est de 61 677 mots pour une enveloppe de 50 000 — soit
+23,4 %** (re-mesurée au terme de la passe d'arbitrage ; elle valait 61 165 à la rédaction, quatre
corrections ayant touché le corps de leur pièce), et c'est la **mesure que la décision d'auteur D-4 attendait** : *la somme des dix cibles
dérivées avait pourtant été additionnée avant rédaction et valait exactement 50 000 — le dépassement
vient de la matière, non de la dérivation.* Quatre choses à savoir avant d'y toucher.
*(a)* ⚠ **Le statut de gouvernance a partiellement bougé le 27 juillet 2026 — DEUX passes d'arbitrage,
PRD v0.9 et TOC v0.25.** Chaque pièce se déclare toujours *brouillon, non publiable*, et **le socle
consolidé reste à 0 entrée** : **G-3 n'est pas entamée**, aucun énoncé n'est central au sens de
CA-IV-01. Ce qui a changé : **deux portes sur sept sont franchies** — **G-2** entièrement
([`PRD/decompte.sh`](PRD/decompte.sh), éprouvée sur les trois corpus entiers) et **G-1 pour le seul
volet du Livre I** ([`PRD/gel-2026-07-27.md`](PRD/gel-2026-07-27.md)) — et **cinq décisions d'auteur
sur neuf sont prises** : **D-1** (gel unique au 27 juillet 2026), **D-4** (enveloppes maintenues,
re-calibrage remis à une passe unique de clôture, ⚠ **amputation interdite**), **D-6** (l'instance
d'arbitrage est l'auteur, sans délégation), **D-7** (risque 15 : **périmètre assumé et déclaré**) et
**D-9** (neuve : lot d'instruction du § 17.5 ouvert, ⚠ **bloquant pour les ch. 25 et 27**). **D-2,
D-3, D-5 et D-8 restent ouvertes**, les risques 13, 14, 16 et **17** restent déclarés non comblés.
⚠ **La seconde passe n'a franchi AUCUNE porte** : *cinq thèses collationnées ne sont pas une collation
de fond*, et le volet de fond de G-4 reste entier. ⚠ **Ne pas en
tirer une requalification du volume** : *deux portes franchies sur sept ne font pas un volume
recevable*, et un brouillon écrit hors portes ne franchit aucune porte — il en documente le coût.
*(b)* ⚠ **Le TOC, le PRD et le conspectus n'ont pas été touchés PAR LA RÉDACTION — ils l'ont été par
la passe d'arbitrage qui a suivi, et la distinction est toute la règle d'escalade.** À la rédaction,
aucun des trois n'a bougé, conformément au PRD (Annexe A) : *un rédacteur ne corrige jamais le TOC,
ce PRD ni le Conspectus — il **remonte**.* Ce sont les **remontées** qui ont ensuite été traitées, par
deux passes de plan et de gouvernance distinctes (TOC v0.24 puis v0.25, PRD v0.8 puis v0.9, conspectus
réaligné à chaque fois) — jamais une
pièce corrigeant son propre cahier des charges. **Leurs champs Statut disent toujours zéro pièce
**recevable**, et c'est correct** : vingt et un brouillons hors portes n'en font aucune. Ne pas les
« corriger » pour ces pièces.
*(c)* ⚠ **Les treize remontées ouvertes par cette rédaction — R-IV-01 à R-IV-13 — sont SOLDÉES depuis
le 27 juillet 2026 ; il n'en reste aucune d'ouverte.** Chacune a été **portée là où elle fait foi**,
jamais close sur place : au **PRD** pour une décision d'auteur, au **TOC** pour un réalignement de
plan (décision 8), à **l'appareil** pour une dette d'outillage. **Le tableau des issues est au
[`README.md` de `Livre I/`](Livre%20I/README.md)** et n'est pas repris ici. Quatre points sont à
connaître au niveau du dossier. **(1)** **R-IV-01 est close par D-7 — périmètre assumé et déclaré** :
la somme ne traite pas l'accord entre agents sous défaillance, et les **ch. 6, 37 et 48 sont fermés**
à cette matière — les rouvrir rouvrirait la décision. **(2)** **R-IV-05 et R-IV-09 sont closes par
versement d'appareil** : [`PRD/check-sieges.py`](PRD/check-sieges.py) vérifie **inter-pièces** qu'un
siège déclaré n'est pas reconstruit ailleurs et que toute pièce touchant sa matière y renvoie —
validé par mutation, il a trouvé **quatre défauts réels** au premier passage — dont **deux sièges sur
trois ne portaient aucun marqueur** dans le texte. **(3)** **R-IV-12 et R-IV-13 sont closes par
réalignement du TOC**, et la classe qu'elles nommaient est désormais **écrite en règle à l'Annexe C**
— voir ci-dessous. **(4)** ⚠ **Une remontée close ne rend pas la pièce recevable** : *zéro remontée
ouverte veut dire qu'aucune question n'attend plus de réponse qui ne soit déjà tranchée*, rien de
plus.

⚠ **Les vingt-quatre du Livre II — R-IV-14 à R-IV-37 — sont soldées de la même manière, et quatre
enseignements de leur clôture valent au niveau du dossier ; le tableau des issues, lui, est au
[`README.md` de `Livre II/`](Livre%20II/README.md).** **(1)** ⚠ **Cinq des treize thèses du Livre portaient
une forme que leur source avait corrigée après coup** — ch. 14, 15, 16, 17 et 19, bornées à la source le
21 juillet 2026 et reportées dans ses pièces le 22, sans que le plan suive. *Cinq reports qui
n'avaient pas été faits, non cinq divergences à arbitrer* — et **aucune pièce ne pouvait le voir
seule**, chacune citant fidèlement un énoncé périmé. La **décision 14 du TOC** en fait une obligation
de passe, **domaine de balayage déclaré** (**treize thèses examinées, cinq réalignées** — *le Livre compte dix chapitres mais treize thèses, les ch. 12, 20 et 21 en portant deux chacun au titre des fusions v0.20*) : *un cardinal
d'écarts sans domaine de balayage est un relevé, pas une couverture.* **(2)** ⚠ **Instruire les
remontées en a trouvé une qui n'était pas ouverte et en a réfuté une qui l'était.** Le § 15.1.4
portait « ce que la carte **prouve** », verbe que **R-02 proscrit** et que le plan assignait pourtant
en garde-fou à ce chapitre — défaut **hérité**, ouvert chez la source, **corrigé ici et signalé
là-bas**. À l'inverse, **R-IV-37 était fausse pour moitié** : le siège du tri prospectif **existait**
(ch. 49 § 49.0), seuls les renvois manquaient. *Une passe d'arbitrage qui exécute ses remontées sans
les vérifier fabrique le défaut qu'elle croit corriger.* **(3)** **Deux remontées bloquantes, deux
réponses opposées, et l'écart est le résultat** : **R-IV-32** est close **sans lot** — la source avait
**réfuté** la proportion au vote adversarial, et *dénombrer pour établir un énoncé que la source tient
pour non soutenu aurait produit un chiffre sans thèse à porter* ; **R-IV-27** est close **par un lot
ouvert et un blocage maintenu** (D-9), deux chapitres du Livre III devant **prescrire** la parade dont
le § 17.5 est la limite empirique. *La différence n'est pas de gravité mais de dépendance.*
**(4)** ⚠ **Une obligation reste due que ce dossier ne peut pas payer** : **CA-IV-11 et CA-IV-13**
exigent un **relecteur distinct du rédacteur**, et **D-6 ne fournit pas de tiers** — *arbitrer n'est
pas relire*. L'écart est déclaré au PRD §11 ; *une lacune de socle se comble par une source, celle-ci
par une seconde personne.*
*(d)* **Le `.html` est un rendu, jamais une seconde source** : toute correction se fait au `.md` et
se reporte au même commit. ⚠ **Depuis la purge du 29 juillet 2026, il ne porte QUE le corps
technique** : l'**en-tête à cinq champs**, la **thèse citée depuis le TOC** et la **note de statut**
en ont été retirés des cinquante pièces — *la même coupe que `build/assemble.py` opère pour le PDF*,
appliquée au rendu de lecture. **Quatre points.** **(1)** ⚠ **Retirer n'est pas ignorer** : le
générateur du skill **exige** les trois à la lecture et **échoue** si l'un manque. **(2)** ⚠ **Les
quinze renvois du corps vers la note retirée sont marqués d'une dague, jamais supprimés**
(`§ 40.7 †`), et le pied de page en donne la lecture. **(3)** ⚠ **Le contrôle [6] du vérificateur a
changé de sens** : il exige l'appareil **au `.md`** et le **refuse** au `.html` — harnais rejoué,
**quatorze mutations, toutes détectées**. **(4)** ⚠ **Le décompte des dagues diffère de celui du
PDF** — **quinze** ici, **vingt-trois** là —, et l'écart n'est pas un défaut : *les deux coupes ne
tombent pas au même endroit*, le paragraphe d'appareil qui suit la thèse restant dans le corps que
`assemble.py` produit. **Ne pas « aligner » un cardinal sur l'autre** : chacun se mesure sur son
propre rendu. Le rendu `.html` et ses huit contrôles sont outillés par le skill (voir
plus bas) ; ⚠ **le vérificateur ne se tuyaute jamais dans un enchaînement `&&`**, le code de sortie
du dernier maillon masquant son échec — faute déjà commise sur le ch. 6, poussé avec un défaut de
rendu alors que le contrôle échouait.

⚠ **Un TROISIÈME rendu existe depuis le 29 juillet 2026 : [`compendium.pdf`](compendium.pdf),
810 pages, composé par [`build/build-pdf.sh`](build/build-pdf.sh).** La phrase « le compendium n'a
pas de pipeline de rendu », vraie jusque-là, ne l'est plus. **Ce pipeline n'est PAS une quatrième
copie du FESP** : les trois copies du FESP appartiennent aux Vol. I, II et III, et aucune n'a été
copiée ici — celui-ci est propre au volume (gabarit `build/springer.template`, format 155 × 235 mm,
Times 10/12, titres courants alternés) et un correctif à l'un des quatre ne se propage à
aucun autre. **Cinq points à connaître avant d'y toucher.** *(a)* ⚠ **Le
`.md` reste la seule source** : le PDF se régénère (`bash build/build-pdf.sh`), il ne se corrige
jamais — et il se régénère **dans le commit qui touche une pièce**, la règle du PDF versionné avec sa
source ([`CLAUDE.md` racine](../CLAUDE.md)) valant pour ce rendu comme pour les trois monographies.
*Un `.md` de chapitre poussé sans son PDF recomposé est un commit incomplet.* *(b)* ⚠ **Le rendu
RETIRE trois appareils, et il les retire parce que le volume les déclare hors corps** : l'en-tête à
cinq champs, la **thèse citée depuis le TOC** et la **note de statut** — les trois hors du corps que
mesure `PRD/decompte.sh` (PRD §6, skill §7). ⚠ **Retirer n'est pas ignorer** : l'assemblage **exige**
les trois à la lecture et **échoue** si l'un manque, faute de quoi une pièce déformée passerait sans
bruit. *(c)* ⚠ **La coupe de la note de statut laisse pendre les renvois du corps qui la
visent** — **vingt-trois** —, et ils sont **marqués d'une dague, jamais supprimés** ; le script en
publie le cardinal à chaque exécution, et le colophon en donne la lecture. *Un renvoi
supprimé serait plus commode et moins honnête qu'un renvoi marqué.* *(d)* ⚠ **Le rendu ne comporte
AUCUNE page blanche** *(instruction d'auteur du 29 juillet 2026)* : ni faux-titre, ni verso blanc, ni
ouverture forcée au recto — d'où des **marges symétriques**. **Ne pas y réintroduire de
`pagebreak(to: "odd")`** sans rouvrir la consigne. ⚠ **En revanche, la phrase « un seul titre
courant », vraie du premier gabarit, ne l'est plus** : la refonte du 29 juillet 2026 sur les deux
monographies Springer a repris leur **titre courant alterné**, et *la parité d'une page reliée reste
un fait physique que l'absence d'ouverture au recto ne supprime pas* — le folio va toujours à
l'extérieur, le verso porte le chapitre, le recto la section. **Ce n'est pas une réouverture de la
consigne** : aucune page blanche n'y revient. *(e)* ⚠ **Le statut du volume n'est pas touché par l'existence d'un rendu paginé** — *composer n'est
pas publier* —, et le **colophon de la page de titre** le déclare une fois pour les cinquante ; la
page d'avertissement séparée a été retirée le 29 juillet 2026, **sa substance repliée au colophon,
non supprimée**. ⚠ **Depuis D-10 (29 juillet 2026), ce colophon porte le statut « révision finale —
diffusion en bibliothèque personnelle » et ses réserves** : portes dérogées, vote adversarial non
conduit, CA-IV-11 et CA-IV-13 non satisfaits, aucun énoncé central. **Toute modification du colophon
se fait au gabarit [`build/springer.template`](build/springer.template) et se recompose dans le même
commit** ; ⚠ *le colophon tient au pied d'une page de titre qui doit rester **une seule page*** — y
ajouter un paragraphe sans reprendre les deux `#v(…)` de tête l'a déjà fait déborder sur la page 2,
défaut qu'aucun contrôle ne voit et que seul le décompte de pages a montré.

⚠ **Le rendu porte, depuis le 29 juillet 2026, une SIXIÈME pièce que le plan ne connaît pas : une
annexe hors plan, placée après le chapitre 50** — [`annexe-references.md`](annexe-references.md), la
**liste des 159 entrées** du socle consolidé, ajoutée **sur instruction d'auteur**. **Six points
avant d'y toucher.** *(a)* ⚠ **Elle n'est aucune des neuf annexes A à I du [`TOC.md`](PRD/TOC.md) et
n'en tient lieu pour aucune** — l'**Annexe I, la bibliographie générale consolidée, reste à écrire**.
*Ne pas la requalifier en annexe du plan, ni écrire que le compendium porte désormais une
bibliographie.* *(b)* ⚠ **Ce n'est pas une bibliographie, et l'annexe le dit elle-même** : elle
inventorie les **faits** sur lesquels la somme adosse ses énoncés, non les **documents** dont ces
faits proviennent. Chaque ligne porte quatre champs — identifiant, objet, niveau, provenance —, plus
la datation de la source quand l'entrée en a une ; ⚠ *une ligne ne remplace pas son entrée*, et le
socle ([`PRD/socle-consolide.md`](PRD/socle-consolide.md)) reste la source de tout ce qu'elle abrège.
*(c)* **Elle ne consomme aucun numéro de chapitre** : le plafond de cinquante tient. Le gabarit porte
pour cela `#ouverture-annexe()`, sans numéro, et la table des matières **fige son compteur** au
marqueur `<ouverture-annexe>` — *sans quoi l'annexe s'annoncerait « 51 » et contredirait la
décision 13a.* *(d)* **Son gabarit de lecture n'est pas celui d'une pièce** : ni en-tête à cinq
champs, ni thèse citée, ni note de statut — la fonction `annexe()` de
[`build/assemble.py`](build/assemble.py) exige un titre et une ligne de situation, et rien d'autre.
*(e)* ⚠ **Un second fichier existe et il n'est PAS relié** :
[`audit-references.md`](audit-references.md), l'inventaire et la validation des 159 références sur
cinq critères — **rapport de mesure sans autorité**, du régime d'[`audit.md`](audit.md) : ni source,
ni socle, ni décision, **jamais citable à l'appui d'un énoncé**, ses constats étant des **remontées
non arbitrées**, et il n'alloue aucun identifiant (PRD §13). *Les deux se distinguent par leur nom :
l'`annexe-` est reliée, l'`audit-` ne l'est pas.* *(f)* **Le décompte de pages a bougé deux fois le
même jour — 847 → 857 par l'annexe, puis 857 → 810 par la refonte du gabarit —, et il vit en cinq
endroits** : les deux `README.md` et les deux `CLAUDE.md`, plus la rangée d'état du dépôt. ⚠ *Les
deux mouvements ne se composent pas* : le premier mesure l'annexe **au gabarit Palatino**, le second
mesure le corpus entier — annexe comprise — **au gabarit Times**. Le coût de l'annexe n'a pas été
re-mesuré après la refonte, et **écrire « 810 contre 800 auparavant » serait une extrapolation, non
une mesure**. *Les journaux datés, eux, gardent le chiffre de leur passe.*

## ⚠ Refonte du gabarit sur deux monographies Springer (29 juillet 2026)

⚠ **Sur instruction d'auteur, [`build/springer.template`](build/springer.template) a été RELEVÉ sur
deux monographies Springer fournies en PDF au dossier** — *Interoperability Principles and Standards*
(ACES 16, 2025) et *Agentic AI: Theories and Practices* (2025) —, et le rendu recomposé en entier :
**810 pages**, contre 857 au gabarit précédent. **Le gabarit n'imitait « le style Springer » que de
mémoire ; il en porte désormais les mesures.** **Cinq faits avant d'y toucher.**

*(a)* **Les deux modèles partagent exactement la même maquette, et elle est mesurée au point près** :
155 × 235 mm, pavé **117 × 190 mm** (marges 19 mm latérales, **21 mm** en tête, **24 mm** en pied),
corps **Times 10 sur 12** — **45 lignes par page** —, alinéa 1,2 em et aucun alinéa après un titre,
titre courant **Times 8,5 pt noir**, § N.M gras 12 pt, § N.M.K gras italique 12 pt, § N.M.K.L gras
10 pt. ⚠ **Le gris a disparu du texte** : les deux modèles n'en portent nulle part, et il ne sert
plus qu'aux filets de tableau (0,61 de gris, la valeur relevée).

*(b)* ⚠ **LE PIÈGE DE CETTE REFONTE EST UN MODÈLE DE LIGNE, ET IL A COÛTÉ UN RENDU ENTIER.** Typst
place par défaut le bord haut d'une ligne à sa **hauteur de capitale** et son bord bas à la **ligne de
base** (`top-edge: "cap-height"`, `bottom-edge: "baseline"`) : une ligne de Times 10 pt mesure donc
**6,62 pt**, non 11,07 pt comme le donnerait un calcul sur l'ascendante et la descendante. Un
interligne calculé sur le mauvais modèle — 0,09 em au lieu de **0,538 em** — a produit un pas de
7,5 pt et **un rendu de 561 pages qu'aucun contrôle n'a signalé**. *Toute valeur verticale de ce
gabarit se compte de ligne de base à ligne de base, jamais de bord de bloc à bord de bloc*, et
`top-edge`/`bottom-edge` y sont **figés aux métriques de Times** pour qu'une ligne portant un ⚠ ou un
☑ — rendu par la police de repli — ne décroche pas de la grille (onze pour cent des lignes du corpus).

*(c)* ⚠ **L'ouverture de chapitre place sa ligne de situation à une ordonnée FIXE**, pas à une
distance fixe du titre : dans les deux modèles, l'« Abstract » commence à 190,6 pt du bord que le
titre tienne sur une ou deux lignes (vérifié à leurs chapitres 3 et 8). Le gabarit le reproduit par un
pavé de titre de **hauteur fixe, 114 pt** — ⚠ *fixe, non minimale* : un titre de trois lignes
déborderait vers le bas plutôt que de repousser la suite. Aucun des cinquante n'y arrive.

*(d)* ⚠ **Deux défauts de la sortie Pandoc sont corrigés dans `build-pdf.sh`, par `sed`, et ils ne
sont pas interchangeables** : le `align(center)` autour des tableaux (déjà là), et un
`table.hline()` explicite sous la rangée de tête qui **écrase en 0,5 pt le filet de 1 pt** que les
deux modèles y portent. *Le second ne se voit pas à la lecture du gabarit : il se voit en mesurant
les filets du PDF.*

*(e)* ⚠ **Le contrôle de cette refonte n'est pas outillé et il n'existe aucun script qui le tienne.**
Ce qui l'a vérifiée est une **confrontation de mesures** entre le rendu et les deux modèles —
première et dernière ligne de base (69,0 et 597,0), pas de grille (12,0), ordonnée du titre courant
(34,9), chute d'ouverture (132,7), largeur et couleur des filets, parité des titres courants sur les
**740 pages** qui en portent. *Une refonte de gabarit ne se déclare pas conforme depuis sa source :
elle se mesure sur son PDF* — c'est la règle des livrables rendus par un pipeline, appliquée ici.

## ⚠ Livre III — quinze chapitres rédigés hors portes, D-9 enfreinte deux fois (27 juillet 2026)

⚠ **Sur instruction d'auteur, [`Livre III/`](Livre%20III/) a été créé le 27 juillet 2026 et ses
quinze chapitres — ch. 22 à 36 — y ont été rédigés en deux rendus chacun**, puis **ses vingt-quatre
remontées R-IV-76 à R-IV-99 soldées** (TOC **v0.27**, PRD **v0.10**). ⚠ **Le statut du volume est
inchangé** : socle consolidé à **zéro entrée**, **G-3 non entamée**, aucun énoncé central au sens de
CA-IV-01, **CA-IV-11 et CA-IV-13 toujours insatisfaites** — *arbitrer n'est pas relire*. **Six choses
à savoir avant d'éditer ici** ; le tableau des issues et la volumétrie sont au
[`README.md` de `Livre III/`](Livre%20III/README.md) et **ne sont pas repris**.

*(a)* ⚠ **L'écart de portes de ce Livre est d'un ordre que les deux précédents n'avaient pas atteint :
il enfreint une DÉCISION D'AUTEUR, pas seulement une porte.** **D-9** ouvre un lot d'instruction du
§ 17.5 déclaré **bloquant pour les ch. 25 et 27** ; les deux ont été rédigés, **et ils prescrivent
l'un et l'autre la parade humaine dont ce lot est la limite empirique**. L'infraction est **nommée à
chaque pièce**, au PRD et au journal du TOC. ⚠ *Le régime est celui que D-7 a appliqué au ch. 6 :
**un arbitrage qui suit une infraction la solde ; il ne la rattrape pas.*** **G-4 conditionne en
outre trois chapitres** — ch. 25, 27 et 30, qui consomment le Vol. III — **et son volet de fond reste
entier**.

*(b)* ⚠ **La classe de défaut de plan trouvée ici est l'INVERSE de celle du Livre II, et c'est le fait
de méthode qui vaut au-delà du Livre.** Là-bas, cinq thèses **citaient fidèlement** une forme que leur
source avait bornée après coup — *le plan n'avait pas suivi*. Ici, **deux thèses avaient elles-mêmes
retranché une borne en la reprenant** : le ch. 25 avait perdu « d'**analystes** » (effaçant l'objet du
garde-fou d'attribution) et converti une **lecture de l'auteur** en prescription ; le ch. 27 avait
perdu « **sous l'article 12.1 du moins** ». ⚠ **Cette seconde classe est plus difficile à voir que la
première** : *la source est intacte, le corps de la pièce est correct — les deux rédacteurs avaient
écrit sous la forme bornée — et **seule la comparaison mot à mot de la thèse citée avec la thèse
rédigée la révèle**.* **Domaine déclaré : quinze thèses examinées, deux réalignées** (décision 14).

*(c)* ⚠ **Un arbitrage a été DÉFAIT plutôt que confirmé, et le motif se généralise.** Le plan
tranchait la date de la ligne directrice québécoise en faveur du Vol. II ; le Vol. I en portait un
troisième terme ; et le Vol. III, **par extraction à la source primaire**, établit qu'**aucune des
deux dates arbitrées ne figure aux pages officielles**. ⚠ ***Une divergence dont on découvre
qu'aucun de ses termes n'est à la source n'est plus une divergence : c'est une absence de datation***
— *et l'arbitrage qui la tranchait portait sur un objet inexistant.* La somme écrit « avril 2026 » et
déclare les trois états (R-IV-88).

*(d)* ⚠ **Une décision de régime a été prise au PRD §7.1, et c'est une EXCLUSION du socle** (R-IV-97) :
les affirmations que le **Vol. I déclare lui-même hors de son propre corpus bibliographique**
**n'entrent pas au socle consolidé**, à aucun niveau. *Le motif est que **[C] n'est pas assez bas** :
[C] atteste **une vérification des références** ; une affirmation hors corpus **n'a pas même reçu
cette vérification-là**.* Elles restent **citables avec leur réserve, jamais versables**.

*(e)* ⚠ **Une enveloppe tenue à +0,3 % ne prouve rien sur ses pièces, et le dire est le résultat le
plus transférable du Livre.** La cible du Livre est tenue **par compensation** : les écarts
individuels vont de **−19,9 % à +31,9 %**, cinquante et un points d'amplitude. ⚠ ***Un agrégat
conforme est compatible avec une dispersion que la conformité de l'agrégat masque*** — c'est
exactement la mesure que **D-4** attendait, et elle **interdit toujours l'amputation**.

*(f)* ☐ **Deux dettes restent dues, avec leur motif écrit.** **Huit sièges déclarés** — six au ch. 31,
deux domiciles au ch. 24 — **ne sont PAS versés à [`PRD/check-sieges.py`](PRD/check-sieges.py)** : ce
fichier était **écrit en parallèle par la rédaction des Livres IV et V le même jour**, et ⚠ *payer une
dette d'outillage pendant qu'un autre l'écrit produirait une table incohérente que le harnais de
mutation ne détecterait pas*. **Les pièces portent leurs huit marqueurs** ; **table et harnais restent
dus, en une passe unique après la clôture des deux Livres.** ⚠ **La même concurrence a déplacé les
numéros de remontées** : la passe des Livres IV et V avait consommé **R-IV-38 à R-IV-75** et la
**v0.26** ; *le Livre III a été renuméroté en R-IV-76 à R-IV-99 à la découverte de la collision, et
**aucun numéro n'est partagé**.* ☑ **La numérotation de version du PRD, elle, est réconciliée** : la
**v0.10** (arbitrage du Livre III) et la **v0.11** (arbitrage du Livre V) **s'empilent dans l'ordre**,
la seconde par-dessus la première — *les deux passes se fusionnent, elles ne se remplacent pas*, et
**aucune ne réécrit la rangée de l'autre**.

⚠ **Une classe de défaut propre à la somme s'est révélée en rédigeant les ch. 10 et 11, et elle est
consignée ici parce qu'elle vaut pour tout le compendium.** Dans les deux cas, une **lacune déclarée
du socle d'un volume** est **comblée par le texte rédigé d'un autre volume** — l'autre source de la
**même ligne Fusion**. *Ce ne sont pas des contradictions* : « le socle de A ne documente pas X » et
« B documente X » sont **logiquement compatibles**, et l'énoncé du volume le plus ancien **reste
exact dans son périmètre** — il ne se corrige pas après coup, sa lacune de couverture étant une
information datée. **Trois conséquences.** *(1)* Une pièce se rédige sur **l'intégralité de son
périmètre de fusion**, jamais sur la seule source que le plan met en avant — le ch. 7 a dû être
corrigé pour avoir manqué cette règle. *(2)* ☑ **La règle est écrite depuis la v0.24 du TOC**, au
registre de l'**Annexe C** : la **collation de fond (porte G-4)** pose la distinction *lacune de
couverture / contradiction* et balaie systématiquement les lacunes déclarées d'un volume contre le
texte rédigé des deux autres. ⚠ **Elle oblige aussi à ne pas confondre deux verbes** : **instruire**
une lacune, c'est lui verser une **source primaire nouvelle datée** (cas de §10.9e) ; **requalifier**
une lacune, c'est constater que sa **couverture** a changé sans qu'aucune source nouvelle soit entrée
(cas de §10.8). *Une lacune requalifiée reste une lacune ; elle change de motif, pas d'état.*
*(3)* **Aucun contrôle outillé ne le fait, et aucun ne le fera** — c'est un contrôle de fond, pas de
forme, et le vérificateur du skill ne s'y substituera pas. ⚠ **Ne pas le confondre avec
`PRD/check-sieges.py`**, qui est bien inter-pièces mais **de forme** : il vérifie qu'un siège n'est
pas reconstruit, non qu'une lacune est bien qualifiée.

**Un skill de projet porte la procédure de rédaction.** Depuis le 27 juillet 2026,
[`.claude/skills/chapitre-compendium/`](../.claude/skills/chapitre-compendium/SKILL.md) tient la
marche à suivre pour rédiger une pièce : état des portes, quatre lectures préalables, squelette et
en-tête à cinq champs, conventions de renvoi et pièges datés, gabarit HTML commun aux pièces, et un
vérificateur validé par mutation (`scripts/verifier-piece.py`). Il **ne porte aucune décision** —
le TOC reste la spécification, le PRD la gouvernance ; il exécute, il n'arbitre pas. Le mettre à
jour quand une passe change une convention, plutôt que de laisser diverger la pratique et la règle.

⚠ **`audit.md` n'est pas un quatrième livrable.** C'est un rapport d'audit daté (**28 juillet 2026** — audit intégral des cinq Livres sur le corpus du commit `8cb40fa`, cent constats, un seul bloquant ; il succède au rapport de couverture du 24 juillet 2026, supprimé au commit `f6183bf`, dont les constats retenus avaient été portés là où ils font foi — risque 15 du TOC, décision D-7 du PRD, passe v0.15). **Sans autorité** : ni source, ni socle, ni décision. Ne jamais le citer à l'appui d'un énoncé ni s'en servir pour modifier le plan — ses constats sont des remontées en attente d'arbitrage, **aucun n'est arbitré**, et il n'alloue aucun identifiant de remontée (l'allocation relève du PRD §13). Un audit suit toujours la même règle : il **remonte**, il ne tranche pas.

⚠ **Le TOC porte, depuis la v0.16 (25 juillet 2026), une table des matières détaillée par chapitre — et ces tables sont subordonnées.** Chaque entrée de chapitre est suivie du dépliage de ses sections et sous-sections, chacune portant sa **provenance** (`← Vol. N` *document* `§N.M`), plus une **table de couverture** par chapitre (décision 6). Les 57 entrées en sont pourvues, dérivées du **texte rédigé** des trois monographies. ⚠ **Une exception depuis la v0.22** : le **ch. 41** porte une table détaillée **sans aucun marqueur `←`** — matière neuve, il n'a pas de texte source à déplier, et l'absence de provenance y est rendue visible **par la forme**, pas seulement par une mention. ⚠ **Une table déplie une ligne Fusion, elle ne la re-décide pas** : en cas d'écart, **la ligne Fusion prime**, et quand le chapitre sera rédigé, c'est **lui** qui corrigera la table (décision 8). *Le travail a vécu dans un fichier séparé, `TOCAll.md`, renommé sur le TOC à sa complétion ; ce fichier n'existe plus, ses quatre commits restent à l'historique.*

⚠ **Condensation v0.20 (26 juillet 2026), sur instruction d'auteur : cinq livres, cinquante chapitres — et rien de soustrait.** Les dix livres sont devenus **cinq** (anciens I+II → I ; III → II ; IV+V+VI → III ; VII+VIII → IV ; IX+X → V) et les 57 chapitres **50**, par **sept fusions** : 12+13, 21+22, 23+24, 25+26, 41+42, 49+50, 55+56. ⚠ **Une fusion ne coupe pas** : chaque paire conserve ses **deux entrées intégralement**, en **deux mouvements** portant chacun son ancien titre et son ancien numéro — dispositif de la décision 10, étendu aux chapitres par la **décision 11**, où vit la correspondance complète. Invariants mesurés avant et après, tous égaux : 57 thèses, 58 lignes Fusion, 309 titres de section, 456 renvois de provenance. ⚠ **Trois numérotations coexistent désormais dans le fichier** — chapitres, sections et livres —, et deux conventions les départagent des renvois aux volumes sources : un renvoi source **colle sa section au § sans espace** (`ch. 21 §21.2`) là où le compendium **l'en sépare** (`ch. 44 § 44.1`), et il porte son marqueur de document. **Toute renumérotation future doit protéger ces deux formes** — la v0.22 l'a fait et l'a vérifié (voir plus bas) : la v0.20 a d'abord renuméroté treize renvois du Vol. II à tort — le marqueur suivait le numéro (« le ch. 20 du Vol. III »), cas qu'aucun masquage vers l'amont n'attrape. ⚠ **Les journaux et rangées d'historique, gelés, citent la numérotation de leur passe** : un « Livre IX » gelé désigne la matière neuve, aujourd'hui premier mouvement du Livre V ; un « ch. 57 » gelé désigne le ch. 50. **Ne jamais les corriger** — C4 et C13 exemptent pour cela les lignes à marqueur de correspondance.

⚠ **Insertion v0.22 (27 juillet 2026), sur instruction d'auteur : un chapitre neuf au Livre IV — et une seconde renumérotation à chaîner.** Le **ch. 41, « La fabrique d'agents : produire, certifier et réémettre le parc »**, entre comme **troisième mouvement du Livre IV** (*produire*), entre *exploiter* (ch. 38-40) et *composer* (ch. 42-46) : la somme décrivait le maillage qui **admet** les agents et l'AgentOps qui les **mesure**, et ne nommait nulle part le plan qui les **produit** (balayage mesuré de la zone des chapitres, zéro occurrence). ⚠ **Rien n'est soustrait ni réécrit** — les 57 entrées conservées en mouvements le restent —, mais **les ch. 41-50 deviennent 42-51** (décision 12). Quatre points à connaître avant d'éditer. **(a) Les correspondances se chaînent, elles ne se réécrivent pas** : la carte de la décision 11 se lit en numérotation v0.21, celle de la décision 12 par-dessus — un « ch. 57 » gelé désigne le ch. 50 de la v0.21, donc le **ch. 51** courant. **(b) Le ch. 41 est de la matière neuve dans un livre qui a un socle** : « Fusion : aucune », thèse en construction d'auteur, table détaillée **sans marqueur `←`**, table de couverture remplacée par une table d'appuis — régime de la décision 9 étendu hors du Livre V, et **risque 16** ouvert avec son issue de retrait. **(c) Un garde-fou de désambiguïsation est ouvert (décision 12c)** : « fabrique » désigne quatre objets, dont **deux vivent déjà dans ce fichier** — la fabrique d'identité du ch. 43 § 43.1 et la fabrique d'agents du ch. 41 ; ne jamais employer le mot sans que le sens soit déterminable de la phrase. **(d) Le ch. 41 ne comble ni le risque 14 ni le risque 15** : produire n'est pas exécuter, le harnais reste sans chapitre, et **D-7 comme D-8 restent ouvertes**. ⚠ **Le défaut de la passe est consigné plutôt que tu** : le remappage ne voyait que la borne gauche des intervalles de sections et a produit **14 formes fautives** du genre `§ 51.1-50.3`, qu'**aucun des quatorze contrôles ne signale** — seule la relecture du diff les a montrées. **Toute renumérotation future relit son diff ligne à ligne** ; le script ne le fera pas à sa place.

⚠ **Plafond v0.23 (27 juillet 2026), sur instruction d'auteur : la fusion qui paie l'insertion de la v0.22.** Le plan étant passé à 51 chapitres, la règle du plafond (section ci-dessous) est posée et **payée dans la même passe** : les **ch. 47 et 48 de la v0.22** — provenance des composants ; mise en service d'un artefact non reproductible — sont fusionnés en **ch. 47, « L'artefact livré »**, et les **ch. 49-51 deviennent 48-50** (décision 13d). ⚠ **Trois choses à savoir avant d'éditer.** **(a) Les trois fronts de l'audit v0.3 restent trois** : deux mouvements au ch. 47, un chapitre au ch. 48 — la fusion supprime un en-tête, jamais une matière. **(b) Les sections du second mouvement sont passées de § 48.1-48.5 à § 47.8-47.12**, à la suite de celles du premier : tout renvoi entrant « ch. 48 § 48.x » se lit désormais « ch. 47 § 47.(x+7) ». **(c) La paire n'a pas été choisie à l'estime** : c'est la seule du plan dont la fusion ne touche **aucun** renvoi de provenance (les deux chapitres n'en portent pas), et le critère est écrit en décision 13c pour la prochaine fois. ⚠ **Le défaut propre de cette passe est le plus silencieux rencontré jusqu'ici, et il est consigné** : le remappage avait **réécrit trois correspondances gelées** — la carte de la décision 12b et la rangée Version de la v0.22, qui se cite verbatim en descendant à l'historique. Une carte réécrite **reste cohérente à la lecture** et fait résoudre les renvois gelés au mauvais chapitre. Restaurées ; règle en décision 13d. **Trois passes de structure consécutives ont vu leur défaut échapper au script (v0.18, v0.22, v0.23) : une passe de structure se relit ligne à ligne.**

⚠ **Depuis la v0.18 (26 juillet 2026), ces tables sont en titres markdown, et la hiérarchie de niveaux fait convention.** `## LIVRE N` → `### Chapitre N` → `#### § N.M` : les sections sont les **enfants directs** du chapitre, ce qui expose le plan complet du fichier dans tout afficheur de plan (éditeur, forge, table des matières Pandoc). Trois corollaires, qu'une passe ultérieure ne doit pas « corriger » en croyant réparer une anomalie : **(a)** « Table des matières détaillée du chapitre N » et « Table de couverture (décision 6) » sont des **paragraphes gras, pas des titres** — les promouvoir en `####` les interposerait entre le chapitre et ses sections ; **(b)** les **sous-sections restent en listes**, délibérément — ce sont des phrases descriptives portant leur provenance, non des intitulés, et les promouvoir produirait un plan de plus de mille entrées, donc illisible ; **(c)** il n'y a **aucun index de tête**, et il n'en faut pas — un index serait un cardinal de plus à tenir à jour (risque 1) là où les titres se dérivent d'eux-mêmes. ⚠ **Et le point qui compte le plus : `check-toc.py` ne voit rien de cette forme.** Ses quatorze contrôles portent sur des motifs de ligne (titre de chapitre, titre de livre, rangées du bandeau, enveloppes de tête, registre des lacunes) ; aucun ne connaît les tables détaillées. Un reformatage passe donc **sans être validé par l'appareil versionné**, et le seul contrôle qui en prouve la fidélité est la comparaison du **flux de mots** avant/après (v0.18 : 72 764 mots, séquence identique) — à refaire, et à déclarer au journal, à toute passe qui touche à la forme.

⚠ **Les ch. 47-48 (Livre V) et le ch. 41 (Livre IV) n'ont aucune table de provenance, et c'est un fait, non un manque.** Matière neuve, « Fusion : aucune » (décision 9) : aucun renvoi `←` n'y est possible, les seuls appuis sont **internes** (chapitres de la somme) et tout énoncé y est au mieux un **repérage [C] à instruire**. La décision 6 (couverture tracée) y est sans objet ; la **décision 8 s'y applique doublement**.

⚠ **Ajouter du contenu à un chapitre peut périmer un identifiant qu'on n'a pas touché** — leçon de la v0.16, et le piège le plus contre-intuitif de ce fichier. Le ch. 32 ne consommait que le Vol. II : son garde-fou « R-5 » nu était décidable. La table détaillée y a introduit une mention de l'**échelle R-14 du Vol. III**, ce qui en a fait un **chapitre mixte** et rendu ce « R-5 » indécidable (C8). Le défaut n'était pas dans la ligne ancienne mais dans son **voisinage neuf**, et seule l'exécution de `check-toc.py` l'a montré — la relecture ne l'attrape pas. Même classe au ch. 43 (« R-8 »). **Exécuter le contrôle après toute addition, même quand on n'a rien retiré ni renuméroté.**

⚠ **Convention de renvoi (décision 7), appliquée par les tables détaillées** : le Vol. III vit en numérotation multiple, et **ses chapitres sont désormais rédigés** — un renvoi au texte s'y écrit `Vol. III `*Monographie*` §N.M`, un renvoi au plan `Vol. III `*TOC*` §N.x`. ⚠ Le **TOC du Vol. III n'a pas de titres `§N.M`** : il nomme ses sections en prose sous des `### Chapitre N`, comme celui du compendium — un renvoi « Vol. III *TOC* §N.M » ne s'y vérifie donc pas par titre, et c'est contre la *Monographie* rédigée qu'il résout, à numérotation et titre concordants (constat de la collation v0.14, re-vérifié le 25 juillet 2026 sur les sept renvois de ce domaine).

⚠ **Un « PRDPlan §N » nu est indécidable entre deux documents** — collision relevée au balayage du 25 juillet 2026, de la classe même que la décision 7 proscrit (« un R-7 nu est indécidable »). Le TOC emploie la forme nue pour **deux** PRDPlan : §4.2 et §4.4 désignent celui du **Vol. II** (formulations types, boucle qualité), §1.5 et §5.3 celui du **Vol. III** (commande de décompte, règle d'escalade). Le contexte tranche à la lecture, jamais le renvoi. **L'occurrence en zone normative est nommée depuis la v0.17** (`PRDPlan Vol. II §4.4`, ch. 25) ; celles de l'avant-propos et des journaux gelés gardent leur forme d'origine. **Nommer le volume à toute occurrence neuve.**

⚠ **Les treize écarts relevés par la v0.16 sont soldés par la v0.17** — chacun par une règle que le plan porte déjà (décisions 2, 6, 7 et 8), **jamais par un choix de contenu neuf**. Détail au journal v0.17 du TOC. Trois d'entre eux valent d'être connus avant d'éditer :

- **Une source vide, corrigée par la décision 8.** Le « volet RGPD » que les ch. 27 et 30 se partageaient n'existe plus : le Vol. III rédigé l'a retiré de son ch. 20 le 22 juillet 2026 (arbitrage **R-G-38**), son socle ne documentant « ni le règlement général sur la protection des données ni aucun de ses articles » — *absence de documentation*, degré 3, **non** fait négatif vérifié. Le ch. 27 reçoit ce chapitre **en entier**, le ch. 30 garde sa matière RGPD par le **Vol. I** (§4.8.4, §5.3). ⚠ **La lacune 16 du Vol. III est entrée au registre de l'Annexe C, dans une SECONDE table** : les lacunes du Vol. III forment une série distincte des onze du Vol. II, et les fondre périmerait un cardinal contrôlé. **Cette seconde table se déclare incomplète** — une entrée, non un inventaire ; le dresser est un préalable de la collation de fond (porte G-4).
- **Une classe de double revendication qu'aucun contrôle n'attrape.** Quand une ligne Fusion absorbe un **intervalle de chapitres** (« Vol. III ch. 5-7 ») pendant qu'un autre chapitre en prélève **une section** nommée (« §7.4 »), les deux renvois sont valides isolément et vivent à des grains différents : `check-toc.py` ne les rapproche pas. **Collation manuelle, à refaire à chaque révision d'une ligne Fusion citant un intervalle.**
- **Une arrivée se déclare aux deux bouts.** Le §2.8.5 du Vol. I était déclaré à son *départ* (ch. 6) et nulle part à son *arrivée* (ch. 4) : un chapitre rédigé sur sa seule liste de sections aurait perdu la section que la v0.5 avait sauvée.

⚠ **Ce que la v0.17 n'a pas touché, et qu'une passe de cohérence ne doit jamais toucher** : les **risques 13, 14, 16 et — depuis la v0.25 — 17** (Livre V sans socle, couche d'exécution sans chapitre, un chapitre sans socle dans un livre qui en a un, et **la quatrième pièce du passeport, qui n'a ni chapitre ni socle**) portent sur du **contenu manquant**, non sur une incohérence — leur arbitrage est une décision d'auteur (**D-2**, **D-3**, **D-8** du PRD), et **une passe de cohérence ne les tranche pas**. De même la thèse forte du ch. 19, à instruire par dénombrement. ⚠ **Le risque 15 sort de cette liste depuis la v0.24, et il faut lire comment** : il est **tranché par D-7 — périmètre assumé et déclaré** —, ce qui **ne le comble pas** mais le **borne**. Les ch. 6, 37 et 48 sont **fermés** à l'accord entre agents sous défaillance ; y ajouter une section rouvrirait la décision d'auteur, non le seul chapitre. *Un périmètre assumé n'est pas un angle mort résorbé : c'est un angle mort dont le lecteur est prévenu.*

## ⚠ Livre IV — dix chapitres rédigés hors portes, et une collision d'identifiants entre passes concurrentes (27 juillet 2026)

⚠ **Sur instruction d'auteur, [`Livre IV/`](Livre%20IV/) a été créé le 27 juillet 2026 et ses dix
chapitres (ch. 37-46) y ont été rédigés en `.md` et en `.html`, hors portes.** Ils sont **arbitrés**
depuis le même jour — **TOC v0.28, PRD v0.12** — et demeurent un **brouillon non publiable**. Le
tableau des trente-deux issues, la volumétrie et les arbitrages de périmètre vivent au
[`README.md` de `Livre IV/`](Livre%20IV/README.md) et **ne sont pas repris ici**. **Cinq faits valent
au niveau du dossier.**

*(a)* ⚠ **L'écart de portes de ce Livre est le plus large du compendium, et il tient à un CUMUL.** Il
est rédigé avant **G-3**, avant **G-4** — préalable déclaré de son premier mouvement — et avant
**G-5**, ⚠ **qui conditionne le Livre entier** ; et son **ch. 41** l'est en outre avant **G-6** et
**D-8**, *qui conditionnent nommément son existence*. ⚠ **Une infraction n'est pas rattrapée par
l'arbitrage qui l'a suivie** : *la décision **D-2** qui conditionne G-5 a été prise le même jour — par
une autre passe, et **après** cette rédaction.*

*(b)* ⚠ **Une collision d'identifiants entre passes concurrentes s'est produite, et c'est un fait de
méthode qui vaut au-delà de ce Livre.** *Trois passes ont écrit et arbitré les Livres III, IV et V
dans le même dépôt le même jour, en numérotant leurs remontées dans une **série unique et partagée
sans allocation préalable** ; **dix numéros — R-IV-60 à R-IV-69 — ont été alloués deux fois**.* **La
renumérotation a porté sur le Livre IV**, dont l'arbitrage n'était pas publié : ses remontées des
ch. 44, 45 et 46 passent de R-IV-60…69 à **R-IV-100…109**, et **aucun numéro n'est partagé**. ⚠ **La
carte se chaîne, elle ne se réécrit pas**, et elle vit au README du Livre. ⚠ **Aucun instrument
versionné ne rapproche deux plages de remontées** — *la collision n'a été trouvée qu'à la main, et
c'est une dette d'appareil déclarée.*

*(c)* ⚠ **Une classe de désalignement neuve est apparue, et elle est INTERNE AU PLAN.** Deux remontées
de ce Livre ne portent pas sur un écart entre le plan et sa source : **le plan se contredit
lui-même** — *neuf sous-sections numérotées « 43.1.x » sous le chapitre 44, et un titre de section
écrivant « Confrontation externe » quand sa propre note de provenance écrit « interne au corpus »*.
⚠ **Aucun des quinze contrôles ne voit cette classe** : `check-toc.py` porte sur des motifs de ligne et
**ne connaît pas les tables détaillées**. *Seule la lecture conjointe d'un titre et de sa note l'a
montrée* — quatrième passe consécutive dont le défaut échappe au script.

*(d)* ⚠ **Dix thèses sur douze étaient désalignées — la proportion la plus élevée des cinq Livres**, et
le domaine de balayage se déclare : *douze thèses examinées, dix réalignées ; le Livre compte **dix
chapitres mais douze thèses**, les ch. 37 et 45 en portant deux chacun au titre des fusions v0.20.*
**Seules celles des ch. 44 et 46 résistent à la collation.**

*(e)* ⚠ **La volumétrie de ce Livre enseigne l'inverse de celle du Livre II, et les deux se lisent
ensemble.** *Le Livre II dépassait de **+23,4 %** parce que **le bornage allonge** ; celui-ci reste à
**−19,9 %** (55 249 mots pour 69 000) parce que **le siège raccourcit** — huit des quinze sections de
son ch. 45 ont leur siège ailleurs dans la somme, et **un chapitre d'instanciation renvoie là où une
monographie développe**.* ⚠ **Les deux forces jouent dans tous les Livres ; ce qui change est laquelle
domine**, et *l'enveloppe héritée n'avait budgété ni l'une ni l'autre.* **La mesure alimente D-4**,
dont le re-calibrage reste remis à une passe unique de clôture.

⚠ **Trois sièges neufs sont versés à l'appareil par ce Livre** — les **cinq points de contrôle
obligatoires** et le **modèle de maturité avec les trois échelles d'autonomie** (ch. 43), l'**organisation
de la fabrique** (ch. 45) —, portant la table de [`PRD/check-sieges.py`](PRD/check-sieges.py) à **douze
sièges** et le harnais à **onze mutations**. ⚠ **S5 est désactivé pour deux d'entre eux, avec un motif
mesuré** : *une pièce du Livre II et quatre pièces hors passe emploient la matière sans renvoyer au
siège, et les aligner dépasse le mandat de la passe qui verse* — **un contrôle bruyant est un contrôle
ignoré**.

## ⚠ Plafond dur : cinquante chapitres, jamais plus

**Règle d'auteur du 27 juillet 2026, sans exception.** Le compendium compte **au plus cinquante
chapitres** — avant-propos et annexes non comptés. Ce n'est pas une cible mais une **borne** : elle
prime sur l'opportunité éditoriale d'un chapitre neuf, et **un plan qui la dépasse n'est pas
publiable**. La règle est posée en **décision 13** du TOC et **appliquée par `check-toc.py`,
contrôle C15** — une règle de plan sans motif exécutable qui la contrôle n'en est pas une (même
doctrine que pour les cardinaux, et que pour `check-veille.py` à la racine).

**Protocole d'insertion, à suivre dans l'ordre.** Ajouter un chapitre reste possible ; le faire
sans payer ne l'est pas.

1. **Vérifier le plafond avant d'écrire quoi que ce soit** : le plan est plein (50/50). Toute
   insertion est donc **conditionnée** à une fusion.
2. **Choisir la paire à fusionner par le critère de la décision 13c**, dans cet ordre : deux
   chapitres **adjacents**, du **même mouvement**, de **même régime de preuve**, sous la même porte
   et la même décision d'auteur ; à égalité, celle dont la fusion touche le **moins de renvois de
   provenance `←`**. Le motif du choix **s'écrit au journal** — une fusion non motivée est
   indiscernable d'une coupe arbitraire.
3. **Fusionner sans rien soustraire** (règle 11a, reconduite) : les deux entrées sont conservées
   **intégralement**, en **deux mouvements** portant chacun son ancien titre et son ancien numéro ;
   les sections du second mouvement se renumérotent **à la suite** de celles du premier.
4. **Insertion et fusion dans la même passe.** Ne jamais laisser la dette à une passe ultérieure :
   elle aurait à choisir sous contrainte ce que la passe fautive a choisi librement.
5. **Enveloppes** : une fusion ne retire rien, donc **aucune enveloppe ne bouge** ; seul le
   chapitre neuf en ajoute une. Ne pas « compenser » un ajout de mots par une fusion — les deux
   gestes sont indépendants (décision 13b).
6. **Exécuter `python PRD/check-toc.py`** : **C15** refuse le dépassement, **C1** la discontinuité.

⚠ **QUATRE contrôles vivent dans `PRD/`, et ils ne se tuyautent jamais l'un dans l'autre** —
le code de sortie du dernier maillon masquerait l'échec des précédents : `check-toc.py` (C1-C15, le
plan), **`check-sieges.py` (S1-S5, inter-pièces — qu'un siège déclaré ne soit pas reconstruit
ailleurs, et que toute pièce touchant sa matière y renvoie ; **26 sièges sur 50 pièces**)**,
**`check-compendium.py` (P1-P8, le socle consolidé — trois de ses rapports sont **déclaratifs** et
n'échouent pas)**, et `decompte.sh --verifier` (la volumétrie, quatre points d'ancrage sur les trois
corpus sources). Chacun a son harnais de mutation et se vérifie comme le reste : *un script de
contrôle est du contenu.* ⚠ *Ce paragraphe annonçait « trois contrôles » jusqu'au 29 juillet 2026 : il
datait d'avant `check-compendium.py`, que le franchissement de G-3 a versé, et **le bloc d'en-tête de
ce fichier en comptait quatre au même moment** — c'est le genre d'écart interne qu'aucun script ne
voit. **Les quatre ont été exécutés le 29 juillet 2026, sortie 0 pour les quatre.***

⚠ **Deux fichiers de bytecode sont versionnés par mégarde sous [`PRD/__pycache__/`](PRD/)** —
`check-compendium` et `check-sieges` —, relevés le 29 juillet 2026 (`git ls-files | grep pycache` en
rend **trois** au dépôt, le troisième étant au Vol. II). **Ne pas les retirer d'autorité** : retirer un
fichier versionné est un geste destructif, il se demande. Le fait est consigné au tableau des reliquats
du [`README.md` du dépôt](../README.md).

⚠ **Elle est passée de sept à NEUF le 27 juillet 2026, avec la rédaction du Livre V** (remontées
R-IV-64 et R-IV-68), et s'éprouve désormais sur **25 pièces** : s'ajoutent le **siège de la sémantique
d'effet** (ch. 48 § 48.1) et le **siège du tri prospectif** (ch. 49 § 49.0). ⚠ **Le premier existait
avant sa pièce, et c'est le fait à retenir** : **six sections rédigées** — ch. 1 § 1.5.2 et § 1.6.2.2,
ch. 22 § 22.5, ch. 23, ch. 24, ch. 27 — écrivaient déjà « la sémantique d'effet est au ch. 48, qui en
est le siège » **alors que le TOC ne le désignait nulle part et qu'aucun instrument ne le
contrôlait** ; il est désigné en v0.26. ⚠ **Le second est versé À MOITIÉ, et l'écart est chiffré** :
son contrôle **S5 est désactivé** — sur les **treize pièces** qui trient des énoncés prospectifs,
**six ne renvoient pas au siège** (ch. 13, 18, 19, 20 du Livre II ; ch. 25 du Livre III ; ch. 37 du
Livre IV) ; *activer S5 produirait six échecs sur des pièces hors de la passe qui verse le siège, et un
contrôle bruyant est un contrôle ignoré.* **La réactivation est due après alignement des six.** ⚠ **Une
garde neuve est entrée au script pour cela** — `renvoi: None` désactive S5 pour un siège nommé, **sans
désactiver S4** : une mutation du harnais l'éprouve (huit mutations depuis cette passe). ⚠ **Et le
harnais accepte désormais une racine paramétrable** (`COMPENDIUM_RACINE`) : *quand deux passes écrivent
en parallèle, le temps 1 — « le contrôle passe-t-il sur le corpus intact ? » — n'est interprétable que
sur le corpus que la passe **committe***.

⚠ **La table des sièges est passée de trois à sept le 27 juillet 2026, avec la rédaction du
Livre II** (remontées R-IV-24 et R-IV-37) : aux trois du Livre I s'ajoutent le **KYA** (ch. 18
§ 18.1), la **triade létale** (ch. 19 § 19.2), l'**horloge post-quantique** (ch. 21 § 21.1) et
l'**encadré des affirmations écartées**, qui porte R-2 et R-3 du Vol. II (ch. 16 § 16.2). Elle
s'éprouve désormais sur **21 pièces**. ⚠ **Le versement a trouvé un défaut réel au premier passage,
et il était dans le siège lui-même** : la signature de la triade létale **ne résolvait pas contre sa
propre pièce** (contrôle **S3**), un retour à la ligne coupant l'un des trois sommets — *une signature
qui ne voit pas son propre siège ne verrait pas non plus une copie.* ⚠ **Un siège neuf s'ajoute à la
table `SIEGES`, la pièce porteuse écrit son marqueur, et le harnais de mutation se rejoue** — les
trois gestes, jamais deux sur trois.

⚠ **Ce que le plafond n'autorise pas : retirer un chapitre pour faire de la place.** Une somme qui
perd de la matière pour tenir un décompte a échangé un défaut visible — un chapitre de trop —
contre un défaut invisible — une matière disparue. C'est exactement ce que la condensation v0.20
s'était interdit, et le plafond ne rouvre pas cette porte.

⚠ **Et le plafond ne vaut pas dispense d'arbitrage.** Les risques 14, 15 et 16 nomment des objets
que la somme ne traite pas ou traite sans socle ; le plafond **ne les tranche pas** — il rend
seulement explicite le coût de les combler par un chapitre. L'arbitrage reste une décision
d'auteur (D-7, D-8 du PRD).

## L'appareil interne du TOC fait loi

Le TOC porte ses propres règles de gouvernance ; les lire avant d'éditer, ne pas les réinventer :

- **Décision 7** — tout renvoi nomme son document (*Monographie*/*Synthèse*/*PRD*/*TOC*), sa série
  (deux séries « Q n » au Vol. II) et son volume (R-1…R-8 du Vol. II ≠ R-01…R-14 du Vol. III).
- **Décision 8** — le plan s'aligne sur le chapitre rédigé, jamais l'inverse ; une déviation fondée
  se déclare.
- **Décision 14 (v0.25)** — ⚠ **la collation d'une thèse contre le texte rédigé de sa source est une
  obligation de passe, à mener AVANT la rédaction et non à la relecture.** *Une citation fidèle d'un
  énoncé périmé reste périmée* — et la thèse se cite verbatim depuis le TOC (PRD §6). **Le rédacteur
  ne réaligne rien** : il écrit son corps sous la forme bornée, cite la thèse telle qu'elle est, et
  **remonte**. ⚠ **Le balayage déclare son domaine** : annoncer *n* réalignements sans dire **sur
  combien** ils ont porté est un relevé, pas une couverture. Motif : **cinq des treize thèses du Livre II**
  portaient une forme que leur source avait bornée un mois plus tôt.
- **Décisions 11, 12 et 13 (v0.20, v0.22, v0.23)** — les trois cartes de renumérotation **se chaînent et ne se
  réécrivent jamais** : un « ch. 57 » gelé désigne le ch. 50 de la v0.21, le ch. 51 de la v0.22, le **ch. 50**
  courant. La **13a** pose le plafond de cinquante chapitres, la **13b** que toute insertion se paie par une
  fusion dans la même passe, la **13c** le critère de choix de la paire, la **13d** qu'un remappage ne touche
  jamais une carte de correspondance ni une rangée qui se cite verbatim.
- **Décisions 9 et 10 (v0.8-v0.9)** — la matière neuve se déclare (Livre IX : « Fusion : aucune »,
  thèses marquées construction d'auteur) ; **le second mouvement du Livre V (clôture) reste terminal** — toute
  insertion se fait avant lui, renvois corrigés ; la décision 10 fixe la carte des dix livres, à
  chapitres strictement inchangés.
- **Autorité des sources** : sur le socle et les lacunes, le **PRD** d'un volume prime son TOC
  (Vol. II : onze lacunes, pas dix ; Vol. III : le PRD postdate et corrige le TOC).

## Pièges spécifiques à ce fichier

- ⚠ **Deux renumérotations gelées dans les journaux.** (1) Chapitres, v0.8 : les anciens ch. 52-54
  (horizon / frontière / péremption) sont devenus les **ch. 55-57** — correspondance au journal
  v0.8. (2) Livres, v0.9 : treize livres condensés en **dix** (anciens III-V = III ; anciens
  IX-X = VII ; VI→IV, VII→V, VIII→VI, XI→VIII, XII→IX, XIII→X) — correspondance au journal v0.9 ;
  un « Livre IX » de journal gelé désigne l'AgentMesh, non le livre de matière neuve. Les journaux
  et les rangées d'historique du bandeau citent la numérotation de leur passe — ne jamais les
  « corriger ».
- ⚠ **Cardinaux multi-sites** : tout décompte annoncé (50 chapitres, cinq livres, enveloppes,
  fourchette, « onze lacunes »…) vit en plusieurs endroits — rangée Version, Volumétrie, champ
  Contrôles, risques 1 et 11 — et se **re-mesure** avant d'être modifié, jamais recopié. La forme
  `~N 000 mots` est **réservée aux enveloppes de tête** (elle entre dans la somme contrôlée).
- ⚠ **Erreur documentée des TOC sources** : la *Synthèse* du Vol. I est numérotée **§1-§12** ; les
  TOC des Vol. I et III portent encore « §3-§12 », qui est faux. Une collation contre eux
  réintroduirait l'erreur en croyant la corriger (décision 7 et risque 10 du TOC).
- ⚠ **Deux sources citées par le plan ne sont plus au dépôt, et la collation doit le savoir avant
  de la lancer.** *(a)* `Synthese Monographie.md` (Vol. I et Vol. II) a été supprimée le 22 juillet
  2026, commit `fd8f1be` ; *(b)* le démonstrateur `Borealis-Go/` (Vol. I) l'a été le 25 juillet
  2026, commit `60f57f6`. Toute collation de fond qui les vise se fait **contre l'historique git ou
  contre rien** — la décision 7 (« tout renvoi nomme son document ») ne suffit plus : elle désigne
  un document, elle ne dit pas s'il est présent. *Le plan ne se réécrit pas pour autant : ses
  renvois sont exacts, ils cessent d'être opposables.* La distinction se déclare à la passe qui
  ouvrira le Livre II ou le Livre IV (l'ADS Boréalis y siège, annexe H).
- ⚠ **Corpus d'appui du Vol. III : filiation retirée** (P0.2 tranchée le 21 juillet 2026, L-15
  close par échec documenté — **réversible** par dépôt ultérieur) : les mentions « corpus
  d'appui » des chapitres consommateurs sont des marqueurs conditionnels de réouverture, jamais
  des sources ; aucun chapitre ne se rédige en s'appuyant sur ces ouvrages sans dépôt effectif.
- ⚠ **Le Vol. III est rédigé depuis le 22 juillet 2026** (34 pièces, socle F-01…F-98 + H-01…H-33,
  PRD v1.3 / TOC v0.8), mais « **rédigé ne vaut pas publiable** » : remontées ouvertes, arbitrages
  révocables, dette de vote (F-92, F-96 du Vol. III). La collation de fond contre son texte rédigé
  (l'homologue de la v0.6) est un **préalable déclaré** aux Livres II et IV, **dont la v0.14 du TOC
  a levé le volet structurel** (couverture complète et résolution des renvois de section, zéro écart —
  seul le volet de fond reste dû) ; et un « F-xx » nu
  est désormais **indécidable entre deux socles** — convention transitoire en décision 7 du TOC.
- ⚠ **Relèves v0.7, v0.10, v0.11 et v0.19** : marquées « à instruire à la source primaire » — aucune
  n'entre au socle, ne re-tranche une divergence ni ne clôt une lacune sans extraction de la
  source primaire. Les relèves v0.11 (l'après-agentique) citent des préimpressions arXiv dont
  seuls les résumés ont été consultés : repérages [C], jamais des faits. ⚠ **Les huit relèves
  v0.19** (couverture en science et génie informatique — ch. 6, 17, 19, 24, 37 et 47 depuis la
  fusion v0.23, qui a réuni sur ce dernier deux chapitres marqués : **six chapitres, huit relèves**) citent
  au contraire des **documents normatifs et des articles de revue consultés à leur source**
  (RFC 8693 et 9334, SLSA v1.2, in-toto, CycloneDX 1.7 / ECMA-424, SPDX 3.0, NIST SP 800-218A,
  NIST AI 100-2 E2025, OPA/Rego, FLP, Gilbert-Lynch, Castro-Liskov, Dean-Barroso, test
  métamorphique). **Le régime ne change pas pour autant** : un document lu à la source reste une
  **relève**, jamais une entrée de socle — la refonte du socle est la porte G-3 du PRD, pas le
  produit d'une passe de plan. ⚠ **Trois réserves de relevé sont portées dans le texte** (date
  d'approbation de SLSA v1.2, version de SPDX que fixe l'ISO/IEC 5962:2021, DOI de Castro-Liskov) :
  ne pas les « compléter » de mémoire — ce qui n'a pas été vu à la source ne s'écrit pas comme vu.
  ⚠ **Ces marques sont contrôlées depuis la v0.21** : C11 couvre les listes v0.10, v0.11 et v0.19,
  inscrites dans le script et validées par mutation (M11c, M11d) — la dette d'appareil que le
  journal v0.19 déclarait est payée.
- ⚠ **L'angle mort du harnais est déclaré, non comblé** (risque 14, v0.10) : la couche d'exécution
  n'a de chapitre nulle part, et trois des huit relèves v0.10 atterrissent dans le Livre V. **Ne
  pas en tirer un chapitre ni un livre** — la somme porte déjà un livre sans socle (risque 13), et
  l'arbitrage est une décision d'auteur, pas une décision de passe.

## Éditer le TOC — protocole de passe

1. Toute passe = **nouvelle version** : nouvelle rangée Version au bandeau (l'ancienne descend en
   rangée Historique, verbatim), champ Date mis à jour, **journal daté ajouté en fin de fichier**.
   Les journaux sont en ajout seul — un journal publié ne se réécrit pas, ses écarts se consignent
   dans la passe suivante.
2. **Contrôles** : `python PRD/check-toc.py` (versionné dans `PRD/` depuis la v0.12 du 23 juillet
   2026 — contrôles **C1-C15** depuis la v0.23, domaine : chapitres 1-50, cinq livres depuis la v0.20 ;
   **C15 est le plafond dur** de la décision 13a) **avant toute publication** ;
   sortie 0 exigée, et le journal de la passe déclare son exécution. ⚠ **Ce script est du
   contenu : il se vérifie comme le reste** (même règle que `check-veille.py` au `CLAUDE.md`
   racine). Toute modification se valide par mutation avec `PRD/check-toc-mutations.py` (versionné
   dans `PRD/`) : constat de passage sur le document intact, puis chaque classe de faute détectée. Des
   faux positifs y sont déjà neutralisés — zones gelées (rangées Historique, journaux) exemptées
   des contrôles de motifs, spans « … » et `` ` … ` `` retirés, marqueurs de correspondance des
   anciens numéraux de livres (Nature, décisions 9-10, risques 1 et 13) — les réintroduire en
   « simplifiant » un motif rendrait le contrôle bruyant donc ignoré. L'exécutable des passes
   v0.3-v0.6 (« contrôles 1-17 ») demeure perdu : les journaux gelés se lisent dans leur
   numérotation d'origine, correspondances en commentaire du script (C7 ≈ 17, C8 ≈ 11).
3. **Git** : messages courts en français, par livrable (« TOC v0.8 — … »), comme l'historique du
   dossier ; chemins explicites à l'ajout.
