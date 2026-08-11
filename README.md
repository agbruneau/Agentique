# Interopérabilité, orchestration et entreprise agentiques — un triptyque, sa veille, sa revue, sa somme, et un traité en marge

Travaux d'André-Guy Bruneau, M.Sc. IT, sur les agents d'IA en écosystème d'entreprise, et plus
particulièrement en services financiers. Le dépôt réunit **trois monographies** conçues en
progression — les protocoles, puis les cadres réglementaires, puis l'organisation qui doit les
faire tenir ensemble —, **une veille technologique autonome** qui les traverse et les tient à jour,
**une revue de la littérature académique** qui mesure ce que le champ savant sait de ce même objet,
**un compendium** qui refond les trois monographies en un seul ouvrage — arrêté en révision
finale, puis clos, non publiable —, et **un traité sur les systèmes multiagents en essaim** qui prend
l'objet par l'autre bout : ce qu'une population d'agents gagne à ne pas s'accorder, et ce qu'elle le
paie. **Sept livrables**, dont les deux derniers — la revue et le traité — sont entrés les 9 et
10 août 2026, après la clôture.

> # ⚠ DÉPÔT CLOS ET FINAL — 8 août 2026
>
> **Décision d'auteur D-13** ([`2 - Compendium/PRD/PRD.md`](2%20-%20Compendium/PRD/PRD.md) **v0.17**
> §16, [`TOC.md`](2%20-%20Compendium/PRD/TOC.md) **v0.33**). **Aucune passe n'est plus prévue** — ni
> de rédaction, ni de révision, ni d'appareil —, **sur aucun des cinq livrables** que le dépôt
> portait alors. La passe de révision ouverte par **D-11** le 30 juillet 2026 est **close sans
> exécution de son domaine résiduel**. Tout ce que ce fichier décrit est un état **définitif** —
> ⚠ *sous la réserve des quatre réouvertures déclarées plus bas, qui n'ont touché aucun des quatre
> volumes dans son corps.*
>
> ⚠ **Ce que la clôture ne fait pas, et il faut le lire avant tout le reste.** Elle **ne franchit
> aucune porte**, **ne lève aucune dérogation**, **ne satisfait aucun critère**, **ne referme aucune
> remontée** et **ne publie rien**. *Une dette qu'on cesse de suivre reste une dette ; elle change
> seulement de nom, et le nom qu'elle prend ici est **manque définitif**.* Le Vol. III garde ses
> quinze remontées ouvertes et sa dette de vote ; le Vol. IV garde ses quatre portes dérogées et ses
> deux critères non satisfaits. *Arrêter n'est ni terminer ni publier ; clore ne rapproche d'aucun
> des deux.*
>
> ⚠ **Le Vol. IV a été renommé le même jour** (décision 20 du TOC) : *« La somme agentique »* du
> 23 juillet au 8 août 2026, **« Interopérabilité et Orchestration Agentiques en Entreprise »**
> depuis. ⚠ **Depuis le 9 août 2026, ce titre est EXACTEMENT celui de la veille
> technologique** — sur instruction d'auteur, la veille a été alignée sur le compendium. *Ce n'est
> plus « à un mot près » : les deux documents du dépôt portent le même intitulé et ne se distinguent
> que par leur genre et leur numéro de volume.* ⚠ **Et la revue de littérature, déposée le même jour,
> en reprend le radical** — *« Interopérabilité et Orchestration Agentiques : revue de la littérature
> académique »* : **trois livrables sur six** partagent désormais ce début d'intitulé. ⚠ **Un renvoi
> qui les cite par leur seul titre ne désigne donc plus rien** : il faut nommer le livrable — « la
> veille technologique », « la revue de littérature » ou « le Vol. IV ».
>
> ⚠ **Le Vol. II a été renommé le même jour** : *« L'autonomie encadrée »* du 17 juillet au 8 août
> 2026, **« Orchestration agentique »** depuis — le nom que son dossier porte depuis l'origine.
> ⚠ *Le titre change, la thèse ne change pas* : l'**autonomie encadrée** (*framed autonomy*) reste la
> thèse centrale du volume, exposée à son chapitre 6 et instruite à son chapitre 13 ; elle cesse
> seulement d'en être l'intitulé. `Monographie.pdf` a été recomposé au renommage — **387 p.,
> inchangé**. ⚠ **Ce renommage est une passe postérieure à D-13** : la déclaration de réouverture que
> le présent fichier exige de tout commit reprenant le travail **reste à faire, et c'est une décision
> d'auteur**.
>
> ⚠ **ET LE RENOMMAGE N'ÉTAIT PAS SEUL DANS CE COMMIT — c'est le constat le plus lourd de la
> resynchronisation du 8 août 2026, seconde relecture.** Le commit `659241b` (8 août 2026, 14 h 24,
> **46 fichiers**), postérieur à D-13, porte **trois gestes de fond que ce fichier n'enregistrait
> pas** :
> *(a)* **un corpus de références est entré au dépôt** — [`1 - Corpus/0 - Références/`](1%20-%20Corpus/0%20-%20R%C3%A9f%C3%A9rences/),
> trois PDF de littérature source (**32,5 Mio** : *Mémoire de maîtrise* 1997, *Enterprise Integration
> Patterns* 2003, *Distributed Systems* 2007). ⚠ *Aucun document du dépôt ne les cite, aucun socle
> n'en porte d'entrée, et ils ne sont adossés à aucun volume* — **ce sont des pièces déposées, non des
> sources instruites** ;
> *(b)* **`1 - Corpus/3 - EntrepriseAgentique/verification/` a été supprimé en entier** — les
> **30 rapports** du Vol. III (15 lots, 11 relectures, 2 revalidations, la confrontation des thèses et
> le registre des remontées, ≈ 8 100 lignes). ⚠ **Le registre `remontees-gouvernance.md` est dans ce
> lot, et c'est lui qui portait le détail des quinze remontées R-G-43 à R-G-57** : *la dette reste
> ouverte, l'inventaire qui la nommait ne se lit plus qu'à l'historique git.* Les décomptes de « 30
> rapports » qui traînaient à quatre `README.md` sont corrigés dans la présente passe ;
> *(c)* ⚠ **un contrôle est passé au rouge sans que rien ne le signale** — voir la ligne
> `decompte.sh` du tableau ci-dessous.
> *Un commit qui dépose un corpus et en supprime un autre ne « renomme » pas : il reprend le travail.*
>
> ⚠ **Le dépôt ne porte aucune licence, et c'est une décision, non un oubli** : **droit d'auteur par
> défaut, tous droits réservés**. Seul le Vol. I porte un `LICENSE` propre.
>
> ⚠ **Une clôture ne s'auto-verrouille pas** : rien n'empêche un commit ultérieur, mais *un commit
> qui reprend le travail rouvre la clôture, et doit le déclarer*.
>
> ⚠⚠ **RÉOUVERTURE DÉCLARÉE — 8 août 2026, passe de veille et de refonte de format.** Conformément
> à la règle ci-dessus, **cette passe rouvre la clôture pour le seul livrable qu'elle touche** : la
> **veille technologique**, actualisée au 8 août 2026 puis **ramenée de 162 à 100 pages fermes**.
> ⚠ **Et elle a été prolongée le 9 août 2026 par trois gestes d'auteur** : la veille a **pris le titre
> du Vol. IV à l'identique**, un **sixième livrable** est entré au dépôt — une
> [revue de la littérature académique](Revue%20de%20litt%C3%A9rature.md) de **40 pages fermes** —,
> et le **compendium a été recomposé à mille pages exactement** (1 114 auparavant).
> *Le dépôt comptait cinq livrables à sa clôture ; il en comptait six le 9 août.*
>
> ⚠⚠ **RÉOUVERTURE DÉCLARÉE — 10 août 2026, dépôt d'un septième livrable.** Un **traité sur les
> systèmes multiagents en essaim** entre au dépôt —
> [`Traité.md`](Trait%C3%A9.md)
> → `.pdf`, **100 pages fermes**, **118 références**, sept chapitres. ⚠ **Il ne touche à rien de ce qui
> existait** : aucun des quatre volumes, ni la veille, ni la revue n'est repris. ⚠ **Et il ne
> s'articule à aucun d'eux** — *c'est le seul des sept qui ne cite aucun autre livrable du dépôt*,
> là où la veille et la revue s'auto-citent et le déclarent. Il **ne franchit aucune porte**, **ne
> lève aucune dérogation**, **ne referme aucune remontée** et **ne publie rien de ce qui est clos**.
> *Le dépôt compte sept livrables depuis le 10 août 2026.*
>
> ⚠ **Il a été renommé et recomposé le même jour, sur instruction d'auteur, et les deux gestes se
> déclarent.** *(a)* Le genre passe d'**essai** à **traité** — titre *« Traité sur les systèmes
> multiagents en essaim »*, fichiers renommés `Traité.md` / `Traité.pdf` : `Swarm Agentic Systems.md`
> / `.pdf` du 10 août 2026 au matin, `Traité.md` / `.pdf` depuis. ☑ *Le fichier rentre ainsi dans la
> convention du dépôt, dont il était le seul à sortir* — **les sept livrables se nomment par leur
> genre et non par leur titre** (`Veille Technologique`, `Revue de littérature`, `Monographie`,
> `Compendium`, `Traité`), et **les mentions de `Swarm Agentic Systems` plus bas dans ce fichier sont
> des constats datés qui gardent le nom de leur passe**. *(b)* Le rendu est **recomposé au
> gabarit d'article arXiv** — bloc de titre à courriel d'auteur, **mots-clés sous le résumé**,
> avant-propos et conclusion en sections non numérotées, **marges au pouce (2,54 cm)** et interligne
> de **13,6 pt**, celui d'un article LaTeX 11 pt *(13,9 pt jusqu'au recalage du 11 août 2026, qui a
> absorbé l'entrée des seize figures)*. ⚠ **Et il est calé à 100 pages exactement**, sur
> instruction d'auteur, *par le seul gabarit* : 99 pages au dépôt du matin, 115 à la recomposition
> arXiv, **100 après calage** — **aucun mot du corps n'a changé entre les trois**. ⚠ *La cible est
> constatée et non vérifiée* : rien ici ne joue le rôle de la porte de pagination du compendium, et
> **un mot ajouté la fera tomber en silence.**
>
> ⚠⚠ **LE TROISIÈME GESTE ROUVRE LA CLÔTURE DU VOL. IV, ET IL FAUT LE DIRE AVANT SES CHIFFRES.**
> `Compendium.pdf` est **recomposé le 9 août 2026 à 1 000 pages exactement**, sur instruction
> d'auteur, par trois réglages du seul gabarit : marges verticales ramenées de 24/26 mm à
> **18/18 mm**, pas d'interligne porté de 17,00 à **16,95 pt**, et **Annexe I composée plus serré
> que le corps** (9,8 pt sur 4,4 pt de pas — elle passe de 112 à **62 pages**). ⚠ *La cible est
> **vérifiée au build** et non constatée* : [`build/build-pdf.sh`](2%20-%20Compendium/build/build-pdf.sh)
> **échoue** si le rendu canonique ne fait pas exactement mille pages. ⚠ **Ce que ce geste ne fait
> pas** : *aucune des cinquante pièces `.md` n'est touchée* — pas un mot du corps ne change —, il
> **ne franchit aucune porte**, **ne lève aucune dérogation**, **ne referme aucune remontée** et **ne
> publie rien**. *Recomposer n'est pas récrire ; mais changer de gabarit un ouvrage clos, c'est
> reprendre son appareil, et cela se déclare.* ⚠ **Un point d'impression n'est pas validé** : à
> 18 mm de marge et 12 mm d'ascent, le titre courant et le folio tombent à **6 mm du bord de
> feuille**, sous la zone non imprimable usuelle de 6,35 mm.
>
> *La passe ne touche au corps d'aucun des quatre volumes* — deux fichiers de gouvernance sont
> néanmoins repris, et il faut le dire : [`2 - Compendium/PRD/TOC.md`](2%20-%20Compendium/PRD/TOC.md)
> et le `TOC.md` des chapitres du Vol. I **pointaient vers des numéros de référence et une édition de
> la veille que cette passe a déplacés**. *Corriger un renvoi qui ne résout plus n'est pas reprendre
> le travail, mais ce n'est pas rien non plus, et le taire serait pire.* Elle ne franchit aucune
> porte, ne lève aucune dérogation et ne referme aucune remontée — le Vol. III garde ses quinze remontées et sa dette de vote, le
> Vol. IV ses quatre portes dérogées. **La clôture D-13 reste en vigueur pour les quatre volumes.**
>
> ⚠ **Et cette passe a réfuté six affirmations porteuses de la veille en dix jours** — dont la
> première accroche textuelle de l'agentique en droit européen (2 août 2026), deux lectures de
> textes canadiens **renvoyées au corpus compagnon comme corrections de fond**, et le décompte
> d'attributs d'observabilité qui fondait un fait négatif et qui a changé de valeur entre deux gels.
> *Un corpus clos ne cesse pas d'avoir tort ; il cesse seulement d'être corrigé — sauf ici, et
> seulement ici.*

> **Où entrer.** Le lecteur pressé lit la [veille technologique](Veille%20Technologique.md) : c'est
> l'état de l'art le plus récent (**édition du 8 août 2026**, faits gelés à cette date, **100 pages**), et le seul document publié qui cite les volumes
> du dépôt. Le lecteur méthodique suit l'ordre des volumes, du général au spécifique. Le compendium
> se feuillette depuis le 29 juillet 2026 — [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf),
> **1 000 pages** re-mesurées le 9 août 2026, au format Letter depuis la refonte typographique du
> 31 juillet 2026 (1 114 pages jusqu'au calage du 9 août ; 921 pages au format 155 × 235 mm
> auparavant) —, et il est **arrêté en révision finale pour la bibliothèque personnelle de
> l'auteur** le même jour, puis **clos le 8 août 2026**. Ses cinquante chapitres restent un **brouillon écrit hors portes** : il se
> lit, il ne fait pas foi, et il ne se diffuse pas. *Arrêter n'est ni terminer ni publier.* Il se
> **feuillette aussi à l'écran** depuis le 4 août 2026 —
> [`Compendium.html`](2%20-%20Compendium/Compendium.html), appareil de lecture d'**un seul fichier
> sans dépendance externe**, dérivé des cinquante `.md` et **sans plus d'autorité que le PDF**.

## État au dépôt — CLOS le 8 août 2026, rouvert quatre fois depuis

Le dépôt est **clos** dans cet état, pour les quatre volumes. Les chiffres ci-dessous ont été
**re-mesurés sur pièce le 9 août 2026**, jamais recopiés d'un autre document ; les commandes qui les
produisent sont données plus bas (« Construire les PDF », « Ce qui reste vivant »). ⚠ *La pagination
est reprise à `pypdf`* — **6.15.0, installé depuis la passe du 9 août 2026** : le relevé direct du
`/Count` de l'objet `/Type /Pages`, auquel ce fichier s'était rabattu le 8 août faute de la
bibliothèque, **donne les mêmes valeurs**, et c'est désormais `pypdf` que la porte de pagination du
compendium interroge au build.

| Livrable | Rendu mesuré (`pypdf`) | Pièces | Appareil de contrôle |
|---|---|---|---|
| Veille technologique | **100 p.** *(162 p. jusqu'au 8 août 2026)*, **303 références** | 14 sections, **18 tableaux**, 25 questions ouvertes | `python Python/check-veille.py` → **sortie 0** ; `python Python/check-resume.py` → **sortie 0** (résumé à **y = 119,4 pt**, 45,7 pt de dégagement) |
| Revue de littérature | **40 p.** fermes, **176 références** | 19 sections, 8 tableaux, 10 fronts ; **12 pièces sur 173 à publication attestée**, 133 sans revue | `python Python/check-revue.py` → **sortie 0** (4 contrôles, **six mutants tombent**) |
| Traité — *Systèmes multiagents en essaim* | **100 p.** *(cible d'auteur tenue ; 109 p. à l'entrée des seize figures le 11 août 2026, ramenées à 100 le même jour en composant l'appareil — tableaux, pseudocode, bibliographie — à 9 pt ; 99 p. au dépôt du matin, 115 p. à la recomposition arXiv)*, **118 références** *(9 prépublications arXiv, déclarées telles)* | 7 chapitres, 21 sous-sections, **20 tableaux**, 9 algorithmes en pseudocode, **16 figures** *(SVG générés, `figures/contenu.py`)* ; **118 renvois cités, 118 notices déclarées, bijection vérifiée** | ⚠ **aucun contrôle propre**, et ⚠ **aucune porte de pagination** — les 100 p. sont **constatées à chaque build, jamais vérifiées** : c'est cette absence qui a laissé la cible tomber en silence le 11 août, comme ce fichier l'annonçait ; `check-resume.py` sort 1 sur son PDF **sans qu'une ligne y soit rognée** : sa marge basse est codée à 73,7 pt (les 2,6 cm de la veille) quand le traité compose à 2,54 cm, et il compte le folio de la page de titre ; le bloc résumé et mots-clés finit à **y = 284,0 pt**, 212 pt de dégagement |
| Vol. I — *Interopérabilité* | **569 p.** | 7 chapitres + 7 bibliographies + Annexe B, **28 diagrammes** | — (vérification adverse des citations) |
| Vol. II — *Orchestration agentique* | **387 p.** | **29 pièces** + registre de gel, socle de 46 entrées | grille CA-1…CA-8 |
| Vol. III — *L'entreprise agentique* | **427 p.** | **34 pièces** + registre de gel ; ⚠ **plus aucun rapport de vérification** — les **30** que le dossier portait ont été **supprimés le 8 août 2026** (commit `659241b`) et se relisent au seul historique git | CA-01…CA-14, 15 remontées ouvertes — ⚠ *leur registre est dans le lot supprimé* |
| Vol. IV — *Interopérabilité et Orchestration Agentiques en Entreprise* | **1 000 p.** *(cible d'auteur du 9 août 2026, **vérifiée au build** ; 1 114 p. du 31 juillet au 9 août, 921 p. au format 155 × 235 mm auparavant)* | **50 chapitres** en 5 Livres *(corps : 928 p.)* + **2 annexes** (hors plan : 159 entrées, **10 p.** ; **Annexe I** : 1 154 entrées, **62 p.**), socle de **159 entrées** ; **0 page blanche sur 1 000** | `check-toc.py` (C1-C15), `check-sieges.py` (**26 sièges / 50 pièces**), `check-compendium.py` (**P1-P8**) → **sortie 0** ; porte de pagination de `build-pdf.sh` → **1 000/1 000** ; ⚠ **`decompte.sh --verifier` → SORTIE 1**, voir ci-dessous |

⚠ **`decompte.sh --verifier` ÉCHOUE, et le motif est le renommage lui-même.** Rejoué sur l'arbre
courant depuis [`2 - Compendium/`](2%20-%20Compendium/), il **sort 1** : le Vol. II mesure **93 239**
mots là où le script en attend **93 242**, et l'agrégat des trois corpus par commande unique tombe de
**479 390** à **479 387**. La cause tient en trois phrases — le commit `659241b` a récrit, dans
**trois pièces de `monographie/`** (`ch-06-autonomie-encadree.md` § 6.2, `ch-13-pont-frames.md`
§ 13.2, `annexe-d-glossaire.md`), les formules qui appelaient l'autonomie encadrée le *titre* de
l'ouvrage pour en faire sa *thèse*, et **trois jetons sont tombés** — un au ch. 6, deux au
glossaire, aucun au ch. 13. *(Le script mesure les pièces, non le `Monographie.md` assemblé : le
changement de titre de la page de garde n'y entre pour rien.)*
⚠ **Rien de tout cela n'est une erreur de mesure** : le script a raison, sa valeur d'ancrage est
périmée d'un renommage, et *personne ne la remettra à jour — le dépôt est clos*. Les trois autres
contrôles du Vol. IV restent en **sortie 0**, comme les trois contrôles de [`Python/`](Python/)
(`check-veille.py`, `check-resume.py`, `check-revue.py`) — **les six rejoués le 9 août 2026**, après
la recomposition du compendium, **et les trois de `Python/` rejoués le 10 août 2026** après leur
déplacement, toujours en sortie 0. ⚠ *Ils vivaient à la racine jusqu'à cette date* : ils lisent leurs
sources par chemin relatif au répertoire courant et **s'invoquent donc depuis la racine du dépôt**,
`python Python/check-veille.py`, jamais depuis `Python/`.
*Le renommage se donnait pour un identifiant sans conséquence de fait ; il a coûté trois mots à un
décompte opposable, et c'est exactement la classe d'écart que ce dépôt prend pour objet.*

Gouvernance du Vol. IV à sa date de clôture, relevée sur pièce le 8 août 2026 : **TOC v0.33**,
**PRD v0.17**, décision d'auteur **D-13**. *Trois états se sont succédé en dix jours, et aucun ne
s'efface* : **D-10** arrête l'ouvrage le 29 juillet (TOC v0.31, PRD v0.15) ; **D-11** rouvre cet
arrêt le 30 juillet (TOC v0.32, PRD v0.16) pour une passe de révision, sur un **rapport d'arbitrage
externe** qui conclut à une *révision majeure — accepté sur le fond, non diffusable en l'état* ;
**D-13 clôt cette passe le 8 août, sans exécuter son domaine résiduel**, et clôt le dépôt. Le statut
**RÉVISION FINALE — bibliothèque personnelle** est inchangé d'un bout à l'autre, et devient
définitif.

⚠ **Ce que ce dépôt ne clôt pas, et qu'il faut lire avant d'en tirer quoi que ce soit.** *(a)* **Deux
volumes ne sont pas publiables et le déclarent** : le Vol. III (quinze remontées ouvertes R-G-43 à
R-G-57, dette de vote sur F-92 et F-96, phase P5 close sans être achevée) et le Vol. IV (quatre
portes closes par dérogation nommée pour le seul régime de bibliothèque personnelle, **CA-IV-11 et
CA-IV-13 non satisfaits** faute de relecteur tiers). *Arrêter n'est ni terminer ni publier ; rouvrir
un arrêt ne rapproche d'aucun des deux, et le clore non plus.* *(b)* **Les deux décisions d'auteur que
ce fichier réservait sont tranchées, et il faut lire comment** : l'étiquette git **`mono-v1.0` est
posée** le 8 août 2026, au commit de clôture — ⚠ *elle marque donc l'arbre clos et non celui du
17 juillet qu'elle nomme, de sorte que les vingt mentions du volume cessent d'être fausses sans
devenir exactes* ; et **aucune licence n'est déposée**, ce qui est le régime **droit d'auteur par
défaut, tous droits réservés** — cohérent avec un corpus dont le volume terminal exclut toute
diffusion. ⚠ *La troisième décision que ce fichier réservait — retirer du suivi git trois fichiers de
bytecode Python — **n'avait plus d'objet** dès le 8 août : `git ls-files | grep pycache` n'en rend
**aucun**, `.gitignore` les couvre.* *(c)* **Les reliquats listés en fin de fichier sont désormais
définitifs** : ce ne sont plus des dettes suivies mais des **manques datés et écrits**. *(d)* **La
veille est rattrapée sur un seul point, et par exception nommée** : ses références **[220]** et
**[259]** portent le **titre neuf** du Vol. IV, chacune assortie de la mention du titre d'alors — *un
titre est un identifiant, non un fait daté*. ⚠ *La seconde s'est appelée **[266]** jusqu'à la refonte
du 8 août 2026, qui a renuméroté la bibliographie de 269 à 303 entrées ; les mentions de « [266] »
plus bas dans ce fichier sont des **constats datés** et gardent le numéro de leur passe.* Ses
références **[217]**, **[219]**, **[259]** — qui donne le compendium à **1 114 pages** — et le reste
de son contenu factuel **décrivent l'état de leurs sources au gel de leur édition**, et cela ne se
corrige pas après coup : *le compendium en fait mille depuis le 9 août, et la veille ne le dira pas.*

## Les sept livrables

Les trois volumes vivent sous [`1 - Corpus/`](1%20-%20Corpus/) ; la veille, **la revue de
littérature et le traité sur les essaims** sont à la racine ; le compendium a son propre dossier.
*(Les deux dossiers ont été renommés le 25 juillet 2026 — `1 - Corpus Agentique/` et
`2 - Compendium Agentique/` auparavant, commit `60f57f6`.)*

⚠ **Trois des sept portent le même début de titre**, et un renvoi qui les cite par leur
seul intitulé ne désigne plus rien : la **veille** et le **Vol. IV** sont **homonymes exacts**
depuis le 9 août 2026, et la **revue de littérature** en reprend le radical
(*« Interopérabilité et Orchestration Agentiques : revue de la littérature académique »*, aligné le
même jour). *Il faut nommer le genre du livrable, jamais son seul titre.* ☑ **Et c'est bien par le
genre que les fichiers se nomment, ce que le septième a mis au jour en y contrevenant.**
`Veille Technologique`, `Revue de littérature`, `Monographie`, `Compendium` : aucun de ces noms n'est
un titre, tous sont des genres. Le septième s'appelait `Swarm Agentic Systems.md` — **ni genre, ni
titre, et le seul nom de fichier en anglais du dépôt**. Le renommage du 10 août 2026 en
[`Traité.md`](Trait%C3%A9.md) **le fait rentrer dans la convention**, qui n'était écrite nulle part
avant d'être enfreinte.

| | **Veille technologique** | **Revue de littérature** | **Vol. I — Interopérabilité** | **Vol. II — Orchestration** | **Vol. III — Entreprise** | **Vol. IV — Compendium** | **Traité — Essaim** |
|---|---|---|---|---|---|---|---|
| **Dossier** | racine du dépôt | racine du dépôt | [`1 - Corpus/1 - InteroperabiliteAgentique/`](1%20-%20Corpus/1%20-%20InteroperabiliteAgentique/) | [`1 - Corpus/2 - OrchestrationAgentique/`](1%20-%20Corpus/2%20-%20OrchestrationAgentique/) | [`1 - Corpus/3 - EntrepriseAgentique/`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/) | [`2 - Compendium/`](2%20-%20Compendium/) | racine du dépôt |
| **Titre** | Interopérabilité et Orchestration Agentiques en Entreprise *(aligné sur le Vol. IV le 9 août 2026 — ⚠ les deux sont désormais homonymes)* | Interopérabilité et Orchestration Agentiques : revue de la littérature académique | Interopérabilité agentique en entreprise dans le domaine des services financiers | Orchestration agentique | L'entreprise agentique — la fabrique de confiance | Interopérabilité et Orchestration Agentiques en Entreprise | Traité sur les systèmes multiagents en essaim *(☑ fichier `Traité.md` depuis le 10 août 2026, au genre comme les six autres — `Swarm Agentic Systems.md` auparavant)* |
| **Rôle** | État de l'art vérifié, mis à jour par éditions | Ce que la littérature académique sait, et à quel régime de preuve | Cadre général, mondial et théorique | Cas canadien réglementé, instruit au grain du droit | Le verrou commun : identité, maillage, exploitation | Omnibus terminal : absorbe et remplace les trois volumes | Où passe la frontière entre coordonner par accord et coordonner par le milieu |
| **Portée** | Mondiale | Mondiale, dix fronts de recherche | Mondiale (UE / É.-U. / R.-U. / Asie) | Canada-Québec (E-23, AMF, Loi 25, ACVM, Lynx/RTR) | Organisation et cycle de vie (NHI, *agent mesh*, AgentOps) | Les trois portées réunies (2024-2032) | Le régime de coordination lui-même, de l'essaim robotique au journal d'événements |
| **Thèse** | « L'agent d'entreprise fiable de 2026 est un agent *enveloppé* » | « Les trois quarts du champ n'ont franchi aucun comité » | « Autonomie graduée sous contrôle de finalité » | « Autonomie encadrée » (*framed autonomy*) | « La confiance ne se décrète pas, elle se fabrique » | Les trois thèses sont trois coupes d'un même objet | « Déplacer la coordination dans le milieu, et payer ce que le déplacement coûte » |
| **Méthode** | Revue structurée, vérification adverse à trois votants | Notices ouvertes une à une, métadonnées reprises à l'API arXiv | Formalisme d'ingénierie (ArchiMate 4, ADS « Boréalis ») | Socle factuel F-01…F-48, niveaux de preuve [A]/[B]/[C] | Double héritage codifié : entrées du Vol. II à niveau conservé, du Vol. I en [C] | Méthode unifiée, gel unique (annoncée) | Chaque mécanisme sous son modèle de panne, son hypothèse de synchronisme et son coût en messages et en tours ; sources primaires consultées directement |
| **Gel de l'information** | 8 août 2026 (édition du 8 août 2026 ; les sections antérieures gardent leur date d'état) | 9 août 2026 | Juin 2026 | 16-17 juillet 2026 | — (hérite de deux gels : juin et 16-17 juillet 2026) | 27 juillet 2026 (décision d'auteur D-1) ; volet des faits levé le 28 juillet 2026 | 10 août 2026 |
| **État** | Publiée (**100 p.**, **303 références**) — format ferme depuis le 8 août 2026 | Publiée (**40 p. fermes**, **176 références**) — déposée le 9 août 2026 et **révisée le même jour** (dixième front), sixième livrable du dépôt | Rédaction terminée (569 p., **233 257 mots** — `wc -w` sur `Monographie.md`, point d'ancrage de `decompte.sh --verifier` ; 225 258 par la commande de référence du dépôt. ⚠ *Le chiffre de ≈ 263 600 mots que ce fichier portait n'est reproductible par aucune des deux commandes* ; synthèse retirée le 22 juillet 2026, démonstrateur `Borealis-Go` retiré le 25 juillet 2026) | Publiée, millésime `mono-v1.0` (387 p. ; synthèse retirée le 22 juillet 2026) | **Rédigé, non publié, et clos en l'état** — 34 pièces rédigées et relues (≈ 160 900 mots), gouvernance PRD v1.3 / TOC v0.8 / PRDPlan v0.5 ; **finalisation P5 close sans être achevée** le 8 août 2026 (dernière passe de fond : relecture de révision du 24 juillet 2026) ; **PDF réassemblé le 24 juillet 2026** (427 p., gabarit FESP, page de note d'état retirée), non publiable en l'état — *et il ne le deviendra pas : quinze remontées R-G-43 à R-G-57 et la dette de vote sur F-92 et F-96 restent ouvertes à titre définitif* | **CLOS ET FINAL** (D-13, 8 août 2026 ; TOC v0.33 / PRD v0.17), statut de révision finale en bibliothèque personnelle maintenu et devenu définitif — *la passe de révision ouverte par D-11 le 30 juillet 2026 (TOC v0.32 / PRD v0.16) est **close sans exécution de son domaine résiduel**, sur l'arrêt initial D-10 du 29 juillet 2026 (TOC v0.31 / PRD v0.15)* : les **cinquante chapitres** des cinq Livres, rédigés **hors portes** le 27 juillet, relus, arbitrés et audités, sont arrêtés et composés en [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) (**1 000 p.**, cible d'auteur calée et vérifiée au build le 9 août 2026 — 1 114 p. auparavant —, dont une **annexe hors plan** — la liste des 159 références, ajoutée au rendu le 29 juillet 2026 ; gabarit relevé sur deux monographies Springer le même jour, porté au format Letter le 31 juillet 2026, puis calé à mille pages le 9 août 2026). ⚠ **Arrêté n'est ni terminé ni publiable** : trois portes satisfaites sur pièce (G-2, G-3, G-7), **quatre closes pour ce seul régime par dérogation**, **CA-IV-11 et CA-IV-13 non satisfaits** faute de relecteur tiers ; **aucune diffusion à un tiers, aucune opposabilité** | Publié (**100 p. fermes**, **118 références**) — déposé le 10 août 2026, septième livrable du dépôt, **renommé, recomposé au gabarit d'article arXiv et calé à cent pages le même jour** ; ⚠ **il ne cite aucun autre livrable**, et **ni contrôle exécutable ni porte de pagination ne lui sont attachés** |

## Veille technologique — le document transversal

[`Veille Technologique.md`](Veille%20Technologique.md) → `Veille Technologique.pdf` (**100 p.**,
14 sections numérotées, **303 références**, 18 tableaux — **édition du 8 août 2026**, faits gelés à
cette date ; résumé sur la page de titre). ⚠ **Le format est ferme depuis le 8 août 2026** : la
revue est passée de 162 à 100 pages **sans changement de gabarit** — 11 pt, marges inchangées —,
toute la réduction venant de la réécriture. *L'appareil seul — page de titre, résumé et
303 références — pèse **32 de ces 100 pages** ; le corps a donc dû perdre près de trois cinquièmes
de ses mots à faits constants.* Revue vérifiée où chaque énoncé factuel
est adossé à une source primaire consultée et soumis à contradiction — vérificateurs indépendants
chargés de *réfuter*, contre-vérification directe sinon. Elle couvre les trois protocoles
structurants (MCP, A2A, ANP), leur gouvernance, l'adoption documentée, la sécurité, et **sept
couches** que la pile protocolaire laisse implicites : événementielle, de contrôle,
transactionnelle, sémantique, de confiance, d'orchestration des processus d'affaires et —
depuis l'édition intégrale — d'**exploitation** (observabilité agentique, évaluation continue,
révocation).

**Elle est aussi le point d'articulation du corpus.** L'**édition intégrale du 18 juillet 2026**
rend compte des **quatre** volumes, dans une section 13 qui leur est consacrée — mais à deux
régimes strictement distincts, et c'est l'écart qui compte :

- les **Vol. I et II sont rédigés** et fournissent des faits — **§4.12 — « De la spécification au
  code »** confronte le corpus documentaire à l'épreuve du démonstrateur `Borealis-Go`
  (référence [217]) ; **§8.4 — « L'instruction sectorielle canadienne »** reprend le croisement
  systématique entre trajectoire protocolaire et textes canadiens (référence [218]) ;
- les **Vol. III et IV y sont des cadrages** — zéro chapitre, zéro entrée de socle propre — et ne
  fournissent **aucun fait** (références [219] et [220], qui portent la réserve en toutes lettres).
  Ils prêtent des *instruments* : la grille des cinq questions du Vol. III organise les §7.6 à 7.10,
  les décisions de fusion du Vol. IV servent de contrôle de couverture. Traiter un plan comme un
  corpus serait la faute que ces deux cadrages prennent eux-mêmes pour objet.

⚠ **Ce tableau de régimes est celui de la veille à son gel, et le dépôt l'a dépassé sur trois
points — signalés ici, non corrigés là-bas.** Le **Vol. III est rédigé depuis le 22 juillet 2026**
(34 pièces, socle propre de 98 entrées), alors que la réf. [219] le décrit sans chapitre ; le
**démonstrateur de la réf. [217] a été retiré du dépôt le 25 juillet 2026** (commit `60f57f6`) — la
citation reste exacte, elle cesse d'être vérifiable ailleurs que dans l'historique git ; et le
**Vol. IV a cinquante chapitres rédigés depuis le 27 juillet 2026, un socle consolidé de 159 entrées
depuis le 28 et un PDF composé depuis le 29 — 1 000 pages au 9 août 2026**, alors que la réf. [220] le décrit comme un
cadrage sans chapitre. ⚠ **Le troisième écart ne fait pas du Vol. IV une source de fait pour
autant** : ses pièces se déclarent brouillon non publiable, et *un brouillon ne porte pas plus de
fait qu'un cadrage*. Une revue publiée décrit l'état de ses sources à sa date : la rattraper après
coup effacerait la seule information qu'elle porte.

L'échange est bidirectionnel, et l'édition du 8 août 2026 en change la nature : aux corrections de
datation que la veille rendait au corpus s'ajoutent désormais **deux corrections de fond**, toutes
deux portant sur des lectures de texte juridique. *(a)* L'**article 12.1 de la Loi 25** n'exige pas
d'« intervention humaine déterminante » : il se déclenche lorsque la décision est fondée
**exclusivement** sur un traitement automatisé, et n'impose alors qu'information et possibilité de
présenter des observations à un employé en mesure de réviser — il borne l'absence totale d'humain,
il ne prescrit pas le degré d'autonomie d'un agent. *(b)* L'**avis ACVM 11-348** ne contient ni
*agent*, ni *agentique*, ni *autonomie* : l'opposition que le corpus construisait — accroche
textuelle par l'ACVM contre accroche par inférence par E-23 — **tombe, les deux accrochant par
inférence**. ⚠ *Ce sont les deux corrections les plus lourdes que la veille ait renvoyées au
corpus, et les volumes ne les reçoivent pas : ils sont clos.* La veille
**rétracte par ailleurs la certitude d'une de ses propres datations** (voir « Divergences
factuelles » plus bas).
L'auto-citation est assumée et divulguée ; ses limites (circularité possible, implémentation
unique, chiffres institutionnels auto-déclarés, deux volumes non rédigés) sont exposées en
section 10 de la veille.

*Historique des éditions : 2, 4, 7, 12, 13, 15, 18 juillet 2026, l'édition intégrale du
18 juillet 2026, l'édition d'août datée du 1er août (faits gelés au 29 juillet), puis l'**édition du
8 août 2026**. Chaque édition ajoute une couche ou un corpus et revérifie les faits périssables ;
celle du 8 août est la première à **retrancher** — audit intégral des références, six réfutations
d'affirmations porteuses, et un format ramené à 100 pages fermes.*

## Revue de littérature — le versant académique

[`Revue de littérature.md`](Revue%20de%20litt%C3%A9rature.md) → `Revue de littérature.pdf`
(**40 p. fermes**, 19 sections, **176 références**, 8 tableaux — arrêtée au **9 août 2026**),
sous le titre *« Interopérabilité et Orchestration Agentiques : revue de la littérature
académique »* — ⚠ *radical aligné le 9 août 2026 sur celui que la veille et le Vol. IV portent déjà :
**trois livrables sur six** partagent désormais ce début d'intitulé, et seul le genre les distingue.*
Où la veille dit ce que le monde déployé fait, sur spécifications, dépôts et textes réglementaires,
cette revue dit **ce que la littérature académique sait**, et à quel régime de preuve. Les deux ne
coïncident pas, et c'est l'intérêt.

Le corpus a deux origines : les **50 pièces académiques de la veille**, reprises et re-vérifiées, et
une passe de recherche neuve sur **dix fronts** — protocoles, sécurité, identité et délégation,
systèmes multi-agents, évaluation, couche transactionnelle, processus d'affaires, gouvernance, Web
agentique, et **chorégraphie et essaim** depuis le 9 août 2026. Les métadonnées des 173 pièces arXiv
ont été **reprises à l'API du dépôt**, ce qui a
corrigé plusieurs statuts que la passe de recherche rapportait comme « à comité de lecture » sur la
seule foi d'un champ de commentaire libre.

⚠ **Le résultat principal tient à la forme du corpus, non à son contenu.** **Douze pièces sur 173 —
7 % — portent une attestation de publication en notice** ; vingt-huit annoncent une acceptation dans
un champ que personne ne vérifie ; **cent trente-trois, soit 77 %, ne présentent aucun signe de revue
par les pairs**. Soixante pour cent du corpus a été déposé en 2026 et la moitié n'a jamais été
révisée. *Un champ dont les trois quarts des énoncés n'ont franchi aucun comité ne peut pas fonder
une décision d'architecture au même titre qu'une littérature établie.*

⚠ **Et l'annexe pousse le constat plus loin.** Des **123 pièces versées par la passe neuve, six
seulement** sont attestées — et **aucune n'appartient aux fronts sécurité, identité, multi-agents,
évaluation, transactionnel ni chorégraphie**, c'est-à-dire à ceux qui portent les énoncés les plus conséquents de
la revue. *Le champ produit ses résultats les plus décisifs là où son appareil de contrôle est le
plus faible.*

**Elle rend trois verdicts à la veille**, dont deux la modifient : le déficit de délégation au-delà
de deux sauts est un déficit **d'adoption et non d'invention** — trois brouillons documentent des
chaînes à N sauts, aucun n'est adopté ; la dissymétrie entre agents et formalismes de processus est
**industrielle, non scientifique** — quatre formalismes sont proposés *pour* les agents, aucun n'est
repris par un protocole ; et l'absence de vocabulaire de trace décrivant une chaîne de mandat est
**confirmée par une seconde voie, plus sévère** — la seule pièce arbitrée du front étend le modèle de
provenance du W3C **sans instancier `actedOnBehalfOf`**.

L'auto-citation est assumée et divulguée : la veille mise à l'épreuve est du même auteur.

## Traité sur les systèmes multiagents en essaim — le livrable qui ne cite personne

[`Traité.md`](Trait%C3%A9.md)
→ `Traité.pdf`
(**100 p.**, 7 chapitres et 21 sous-sections, **118 références**, 20 tableaux, 9 algorithmes en
pseudocode, **16 figures** — daté du **10 août 2026**, figures entrées et rendu recalé le
**11 août 2026**), sous le titre *« Traité sur les systèmes multiagents en essaim —
la coordination par le milieu : ce qu'un essaim d'agents logiciels gagne à ne pas s'accorder, et ce
qu'il le paie »*.

⚠ **Le genre a changé le jour même du dépôt, et le fichier avec lui** — `Swarm Agentic Systems.md` au
matin, `Traité.md` depuis, *au genre comme les six autres livrables*. Le document se donnait pour un
**essai** ; il est **traité** depuis le 10 août 2026, sur instruction d'auteur — sept chapitres
numérotés, définitions posées, algorithmes en pseudocode, tableaux de garanties et 118 références
tiennent mal dans le genre bref et digressif dont « essai » porte le nom. ⚠ **La substitution du mot
dans le corps s'est réduite à une occurrence**, l'ouvrage se nommant partout ailleurs *« l'ouvrage »*
ou *« le livre »* : *le genre était dans le paratexte, pas dans le texte.* **Deux occurrences ont été
délibérément laissées** — un *banc d'essai* au §2.3, qui est un montage d'épreuve et non un genre
littéraire, et l'*« essai d'interprétation »* du titre de Grassé 1959 (réf. [4]), qu'on ne récrit pas
sans falsifier une citation.

⚠ **C'est le seul des sept qui ne cite aucun autre.** Ni la veille, ni la revue, ni aucun des quatre
volumes ne figure à ses 118 références ; les protocoles qui structurent tout le reste du dépôt n'y
paraissent qu'une fois, par la spécification MCP (sa réf. [30]), prise en exemple de milieu et non
en objet. *Il ne prolonge pas le triptyque : il en attaque l'hypothèse de coordination par l'autre
bout.* Corollaire à porter au crédit du livrable : **l'auto-citation, assumée et divulguée dans la
veille comme dans la revue, y est nulle**.

⚠ **Il ne porte aucune divulgation d'assistance par modèle de langage, et c'est le seul livrable du
dépôt dans ce cas.** Sa page de titre en portait une, en note d'astérisque — champ `thanks` de
l'en-tête — du dépôt du 10 août 2026 au matin **jusqu'au retrait du même jour, sur instruction
d'auteur**. *La divulgation ne subsiste qu'au niveau du dépôt*, à la rubrique « Assistance par
agents » des [avertissements](#avertissements), qui couvre l'ensemble des travaux — **le fichier
diffusé seul ne la porte plus**.

Sa thèse : passé quelques dizaines d'agents, et lorsque la défaillance partielle devient l'état
normal, le coût du consensus explicite — messages, latence de queue, couplage temporel — croît plus
vite que la valeur qu'il procure ; l'architecture gagnante déplace alors la coordination vers un
**substrat événementiel partagé, durable et ordonné localement**, où les agents déposent et lisent
des traces au lieu de négocier des décisions — transposition de la **stigmergie** de la robotique en
essaim. *Le déplacement n'est pas une suppression* : le point partagé n'est pas détruit, il est
transporté dans le milieu, qui devient le composant que tout le monde touche, qu'il faut répliquer,
exploiter et facturer.

⚠ **L'ouvrage écrit la contrepartie au lieu de l'escamoter** : la sûreté globale est troquée contre
la vivacité, le comportement cesse d'être reproductible à l'échelle de l'exécution, et la charge de
preuve passe à la traçabilité et au point de reprise. Sa discipline est celle de la borne — chaque
mécanisme porte son modèle de panne, son hypothèse de synchronisme, son coût en messages et en
tours, sa condition d'arrêt et son mode de défaillance ; chaque transposition depuis la robotique
nomme ce qu'elle conserve et ce qu'elle casse. Trois résultats la bordent et ne se contournent pas
— l'impossibilité du consensus asynchrone dès **une seule** panne par arrêt (réf. [1]),
l'incompatibilité de l'atomicité et de la disponibilité sous partition (réf. [2]), la loi d'échelle
qui donne un **maximum** et non un rendement décroissant (réf. [3]) —, et un quatrième trace la
frontière : les programmes décentralisables sans coordination sont exactement les programmes
monotones (réf. [6]). *Un agent qui accumule se passe d'accord ; un agent qui compte exactement une
fois ne le peut pas, et la coordination n'est alors pas évitable, seulement déplaçable.*

⚠ **Sa conclusion est un aveu de métrologie, et il faut la lire avant d'en tirer une architecture.**
Ce que le livre laisse ouvert n'est pas une théorie manquante mais une **mesure** manquante : le
protocole qui estimerait la contention et le coût de cohérence d'un essaim réel n'est pas écrit — le
point de retournement chiffré au ch. 2 reste une **illustration arithmétique**, non un seuil que le
lecteur puisse recalculer chez lui ; la corrélation des fautes, que toutes les bornes probabilistes
citées supposent nulle, n'a pas d'estimateur qui ne redemande pas la vue globale qu'on cherchait à
éviter ; et le verdict le plus utile de l'ouvrage lui est contraire — *à petite et moyenne échelle,
la solution centralisée par diffusion demeure vraisemblablement le meilleur choix* (réf. [95]).
**La frontière annoncée au titre est argumentée, non mesurée**, et le texte préfère le dire
nettement.

⚠ **Son rendu suit le gabarit d'article arXiv depuis le 10 août 2026**, et c'est le seul livrable de
la racine dans ce cas. Le bloc de titre porte **titre, sous-titre, auteur et courriel, date**, puis
le **résumé suivi des mots-clés** ; la table des matières vient ensuite, l'avant-propos et la
conclusion sont des **sections non numérotées** et la numérotation des sept chapitres reste **écrite
à la main dans les titres** — *le gabarit Typst numéroterait par-dessus, et l'ouvrage renvoie à ses
propres numéros en une centaine d'endroits.* ⚠ **Le champ `thanks` a été retiré de l'en-tête le
10 août 2026** : la page de titre ne porte plus ni astérisque ni note de bas de page, et le rendu
perd du même coup sa divulgation d'assistance par modèle de langage.

⚠ **Et le rendu est calé à 100 pages exactement, sur instruction d'auteur du 10 août 2026.** Le
calage se prend sur **deux réglages du seul en-tête**, et sur rien d'autre : marges portées **au
pouce — 2,54 cm sur les quatre côtés**, la géométrie canonique d'un article LaTeX, et
`linestretch: 0.9`, qui ramène l'interligne du gabarit Typst de 14,65 pt à **13,9 pt** pour un corps
de 11 pt. ⚠ *Ce second réglage n'est pas une compression* : l'interligne d'un article LaTeX 11 pt
vaut 13,6 pt, et le défaut de Typst — 1,33 fois le corps — était simplement plus aéré que la norme
de l'espèce. **Trois paginations se sont succédé en un jour, à contenu strictement inchangé** :
99 pages au dépôt du matin (marges 2,18 × 2,35 cm), 115 à la recomposition arXiv (2,8 × 3,2 cm),
**100 après calage**. ⚠ **La cible est constatée, non vérifiée** : le compendium fait échouer son
build hors de sa cible, *le traité n'a pas d'équivalent* — **la pagination est une fonction en
escalier, et un mot ajouté fera tomber les cent pages sans que rien ne le dise.**

☒ **C'est arrivé le 11 août 2026, et non par un mot** : **seize figures** sont entrées dans le corps,
et le rendu est passé de 100 à **109 pages** en silence, aucune porte ne s'y opposant.

☑ **Le traité a été recalé le même jour, et les cent pages sont reprises sur l'appareil, non sur
l'argument.** Les seize figures pèsent **3 686 pt de hauteur cumulée, soit 5,7 pages de corps** : elles
ne se rattrapent pas à l'interligne, et le tenter aurait porté celui-ci à ~10,4 pt pour un corps de
11 pt, très en dessous de toute norme. Le calage passe donc par ce qu'un gabarit d'article compose
**déjà** plus petit que son texte courant — **les 20 tableaux, les 9 blocs de pseudocode et les
118 notices de références à 9 pt** —, plus un resserrement de l'espace **au-dessus** des figures
(0,6 em ; celui du dessous reste à 1,2 em, sans quoi la légende se colle au paragraphe suivant).
L'interligne ne descend que de 13,9 pt à **13,6 pt**, *qui est la valeur exacte d'un article LaTeX
11 pt* : le calage s'arrête à la norme de l'espèce, il ne passe pas dessous. ⚠ **Les marges au pouce
et le corps de 11 pt ne sont pas touchés** — le gabarit arXiv du 10 août tient. Contributions
mesurées, au rendu : tableaux −3 p., bibliographie −3 p., espace des figures −1 p., pseudocode et
interligne −2 p. ensemble *(les leviers ne s'additionnent pas : la pagination est une fonction en
escalier)*.

☑ **Un défaut de balisage a été trouvé à la recomposition et corrigé.** L'introduction et la
conclusion écrivaient leurs renvois en **doubles crochets** — `[[5]]`, **16 occurrences sur
10 lignes** — quand le corps en écrit **512 en crochets simples**. *Pandoc ne connaît pas cette
forme et la composait littéralement* : le PDF déposé le matin affichait « [[5]] » en toutes lettres
dans ses deux sections d'encadrement, et nulle part ailleurs. Normalisé sur la forme majoritaire,
puis vérifié : **118 renvois cités, 118 notices déclarées, aucun orphelin dans un sens ni dans
l'autre**.

☑ **Il a été audité en totalité le 10 août 2026, par boucle bâtisseur/critique — 168 correctifs.**
Deux axes, et deux seulement : la tenue du français technique, et la fiabilité des sources. Huit
morceaux jugeables, un bâtisseur et un juge à l'aveugle par morceau, chaque juge comparant un extrait
du traité à un extrait de la veille technologique **sans savoir lequel des deux était lequel**, ordre
alterné et extraits tronqués à longueur comparable. **Le traité gagne 7 comparaisons sur 8** — il perd
les chapitres 2 et 3. Le détail, tour par tour, était au journal de boucle `gauntlet-log.md` —
⚠ **purgé de l'arbre le 10 août 2026, et il ne se relit plus qu'à l'historique git.**
État vérifié au rendu final : **100 pages**, **0 page blanche**,
**20 tableaux numérotés 1 à 20**, bijection des renvois intacte.

⚠ **Les 118 notices ont été confrontées à leur source primaire, et ce que la confrontation a trouvé
compte plus que le décompte** — 108 confirmées telles quelles, 10 corrigées, **0 non confirmée** :
*(a)* **un titre inventé**, à la réf. 93, dont les auteurs, la revue et l'année étaient pourtant
exacts — **un cas sur 118**, et le seul ; *(b)* **quatre statuts éditoriaux faux, tous dans le même
sens** — des pièces déposées sur arXiv annoncées comme prépublications alors qu'elles sont **parues
arbitrées** (CAV 2013, CAV 2017, *IEEE Software* 2016, *CACM* 2020). ⚠ *L'erreur sous-évaluait le
corpus au lieu de le gonfler ; elle n'en était pas moins fausse, et dans un ouvrage dont la
déclaration de statut est précisément la discipline* ; *(c)* **12 cibles mouvantes ancrées** — des
notices citant du code sur la branche `trunk`, où rien de ce qui est allégué n'est retrouvable —,
réancrées sur des SHA et des étiquettes **ouverts et relus**, les valeurs alléguées au ch. 6 ayant été
retrouvées dans le code à l'étiquette 4.1.0 ; *(d)* **13 paginations ouvertes ou absentes** fermées sur
Crossref, DataCite ou dblp.

⚠ **Aucun contrôle exécutable ne lui est attaché**, contrairement à la veille et à la revue. Le seul
rejouable sur son PDF, [`check-resume.py`](Python/check-resume.py), **sort 1 sans qu'une ligne y soit
rognée** : sa marge basse est codée en dur à **73,7 pt** — les 2,6 cm de la veille — alors que le
traité compose à **2,54 cm**, et il compte le **folio** de la page de titre, que la veille et la
revue n'ont pas. Le bloc du résumé et des mots-clés finit à **y = 284,0 pt**, soit **212 pt de
dégagement** ; ce qui descend à 42,9 pt est le numéro de page, à sa place. *Le contrôle a raison sur
ce qu'il mesure et tort sur ce qu'il conclut, faute d'avoir été calibré pour un troisième gabarit —
et personne ne le calibrera : le dépôt est clos.*

## Vol. I — Interopérabilité agentique

Monographie de science et génie informatique, construite **en spirale du général au spécifique**,
pour un double public (recherche et praticien-architecte). Invariant transversal : *découplage,
contrat, évolution*.

- **Monographie** (`Monographie.pdf`, **569 p.**) — 7 chapitres : interopérabilité des SI, IA
  agentique, interopérabilité agentique, en entreprise, dans le domaine financier, blueprint
  ArchiMate, horizon 2027-2032.
- **Architecture détaillée de solution** (Annexe B) — la monographie projetée sur une entreprise
  fictive, la *Coopérative financière Boréalis*, consolidée sur la pile IBM ; 18 sections,
  6 sous-annexes, 28 diagrammes Mermaid, rendus dans le PDF principal.
- **Article de synthèse** — *retiré du dossier le 22 juillet 2026* (`Synthese Monographie.md` / `.pdf`,
  69 p.). La monographie et son Annexe B restent les seuls livrables du volume.
- **Démonstrateur `Borealis-Go/`** — *retiré du dépôt le 25 juillet 2026* (commit `60f57f6`).
  C'était du code Go exécutable matérialisant l'ADS : **5 agents A2A** et **4 serveurs MCP**
  orchestrant une pré-qualification de crédit (jamais un octroi ferme), sur les SDK officiels des
  deux protocoles ; **12 ADR**, journal d'audit à chaîne de hachage, vérification adverse à chaque
  phase, invariants critiques prouvés par mutation ; couverture déclarée 96,2 % au rapport final.
  C'est lui qui fournissait la §4.12 de la veille (référence [217]) — **cette référence ne se
  vérifie plus que dans l'historique git**, et la veille n'est pas corrigée pour autant.

## Vol. II — Orchestration agentique

Monographie sur l'interopérabilité et l'orchestration agentique en services financiers canadiens,
publiée sous le millésime `mono-v1.0`. **92 056 mots** en 29 pièces (24 chapitres, avant-propos,
annexes A-D) selon son README — ⚠ **92 059 au 17 juillet 2026**, les trois jetons perdus au commit
`659241b` touchant **les deux** commandes de décompte et non la seule `decompte.sh` ;
`Monographie.pdf` **387 p.** (article de synthèse, 66 p., retiré du dossier le 22 juillet 2026).

⚠ `mono-v1.0` a été un **millésime éditorial sans étiquette git** du 17 juillet au 8 août 2026 :
aucune référence de ce nom n'existait dans le dépôt, ni en local ni sur le distant (vérifié le
18 juillet, re-vérifié le 8 août 2026 — `git tag -l` vide), alors que trois documents de gouvernance
du volume et dix-sept pièces l'annonçaient comme posée. ☑ **L'étiquette est posée le 8 août 2026, au
commit de clôture du dépôt**, sur décision d'auteur. ⚠ **Elle ne rétablit pas la vérité de ces vingt
mentions, et il faut le dire** : *elle marque l'arbre clos, pas l'arbre du 17 juillet* — les mentions
cessent d'être fausses sans devenir exactes, et `git show mono-v1.0` le montre.

Sa contribution la plus citable est un **résultat négatif** : en croisant trois protocoles
(MCP, A2A, AP2) et cinq corpus de textes canadiens, **aucun lien documenté par source primaire** —
quinze croisements, zéro lien. D'où sa thèse probatoire : sous exigence réglementaire stricte, le
cadre déterministe invoque les agents, jamais l'inverse, parce que le cadre est la seule pièce
dont l'exploitant puisse démontrer la teneur devant un tiers.

Sa méthode est son autre apport : socle factuel de **46 entrées** (F-01 à F-48) cotées par niveau
de preuve — **[A]** vote adversarial 3-0 > **[B]** source primaire extraite > **[C]** repérage —,
huit garde-fous de formulation, onze lacunes exposées plutôt que comblées.

## Vol. III — L'entreprise agentique

**Rédigé de bout en bout, non encore publié.** Les **34 pièces** — avant-propos, 28 chapitres en
9 parties, 5 annexes — sont **rédigées, relues adversarialement et corrigées** (statut constaté sur
pièce le 22 juillet 2026), pour **≈ 160 900 mots réels** (re-mesure du 24 juillet 2026, après la relecture de révision) au regard d'une cible indicative de
**≈ 102 500**. Le socle factuel propre compte **98 entrées** (F-01 à F-98), sur **33 entrées
héritées** (H-01 à H-33) ; les **15 lots d'instruction sont clos**. Le volume s'organise autour de
trois capacités — *émettre* une identité opposable (le passeport d'agent), l'*appliquer* au
maillage d'agents, l'*exploiter* dans la durée (AgentOps) — sous l'horloge post-quantique.

⚠ **Rédigé ne vaut pas publiable.** La phase de finalisation (**P5**) a couru jusqu'au 24 juillet
2026 — revalidation temporelle finale, rejeu des motifs de balayage sur les 34 pièces, pipeline de
rendu créé le 23 juillet (copie du FESP du Vol. II) — et elle est **close sans être achevée** depuis
la clôture du dépôt, le 8 août 2026. **Quinze remontées de gouvernance demeurent ouvertes**
(R-G-43 à R-G-57), dont plusieurs relèvent de l'auteur, et **elles le demeureront**. **Le PDF est
assemblé (427 p., gabarit FESP) ; rédigé ne vaut pas publiable, et clore une phase n'est pas la
terminer.**

Le dossier porte **deux répertoires** — la gouvernance dans `prd/`, la rédaction dans
`monographie/` —, plus un [`README.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/README.md) au
lecteur *(déposé le 29 juillet 2026 : le volume était le seul des trois à n'en porter aucun)*.
⚠ **Il en portait un troisième, `verification/`, et il a été supprimé le 8 août 2026** (commit
`659241b`) : ses **30 rapports** — 15 lots d'instruction, 11 relectures, 2 revalidations, la
confrontation des thèses et le registre des remontées — **ne se lisent plus qu'à l'historique git**.
⚠ *La suppression ne solde rien de ce qu'ils portaient* : les quinze remontées R-G-43 à R-G-57 et la
dette de vote sur F-92 et F-96 restent ouvertes à titre définitif, et **le registre qui les
détaillait n'est plus sur l'arbre** — la dette survit à son inventaire.
Documents de gouvernance, par ordre d'autorité :

1. [`prd/PRD.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/prd/PRD.md) **v1.3** —
   contenu, héritage du socle, quatorze garde-fous, critères d'acceptation ; **prime en cas de
   conflit**, y compris sur le TOC ;
2. [`prd/TOC.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/prd/TOC.md) **v0.8** —
   autorité sur le découpage (28 chapitres, 9 parties, 34 pièces) ;
3. [`prd/PRDPlan.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/prd/PRDPlan.md)
   **v0.5** — plan d'exécution (phases P0 à P5).

Le volume naît des lacunes des deux précédents : identité non humaine et délégation multi-saut
(verrou identifié au Vol. I), mécanique des attaques et valeur cryptographique des Agent Cards
(questions ouvertes du Vol. II).

## Vol. IV — Interopérabilité et Orchestration Agentiques en Entreprise (compendium)

**Clos et final depuis le 8 août 2026, arrêté en révision finale pour une bibliothèque personnelle
depuis le 29 juillet.** Le dossier
[`2 - Compendium/`](2%20-%20Compendium/) porte une table des matières
commentée ([`TOC.md`](2%20-%20Compendium/PRD/TOC.md), **v0.33 du 8 août 2026** — chaque
entrée de chapitre y est suivie de sa **table des matières détaillée**, provenance par
sous-section et table de couverture, **portée en titres markdown depuis la v0.18** : le plan du
fichier expose la hiérarchie livre → chapitre → section), son
**PRD de gouvernance de la rédaction** ([`PRD.md`](2%20-%20Compendium/PRD/PRD.md), **v0.17 du
8 août 2026** — portes de lancement, régimes de preuve, critères d'acceptation, jalons), son
**socle consolidé** ([`socle-consolide.md`](2%20-%20Compendium/PRD/socle-consolide.md), **159 entrées**
`S-001`…`S-159`), sa vue synoptique dérivée ([`README.md`](2%20-%20Compendium/README.md)), ses
exécutables de contrôle ([`check-toc.py`](2%20-%20Compendium/PRD/check-toc.py) et trois autres,
chacun avec son harnais de validation par mutation), ses **cinq Livres rédigés** et — depuis
le 29 juillet 2026 — leur rendu paginé,
[`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) —
**c'est une refonte des trois volumes, pas une nouvelle thèse.**

⚠ **Les cinquante chapitres sont rédigés, et ils le sont hors portes.** Le 27 juillet 2026, sur
instruction d'auteur, les cinq répertoires [`Livre I/`](2%20-%20Compendium/Livre%20I/) à
[`Livre V/`](2%20-%20Compendium/Livre%20V/) ont été créés et **leurs cinquante chapitres** y ont été
rédigés en deux rendus chacun (`.md` source, `.html` de lecture à thème sombre — **corps technique
seul depuis la purge du 29 juillet 2026**, l'appareil de gouvernance restant au `.md`), **avant** le
franchissement des portes que le PRD pose comme préalables ; chaque pièce se déclare elle-même
**brouillon, non publiable** et porte, en section hors plan, les conséquences de cet écart. Les passes
d'arbitrage qui ont suivi ont soldé leurs remontées, puis un **audit intégral des cinq Livres**
(`audit.md`, cent constats — ⚠ **rapport retiré du dépôt depuis**, récupérable au seul historique git)
et une relecture des cinquante pièces ont
précédé le franchissement de la **porte G-3** le 28 juillet 2026 — le socle consolidé, resté vide
depuis l'ouverture du volume, porte désormais **159 entrées**. ⚠ **Rien de cela ne requalifie
l'ouvrage** : *une porte franchie n'est pas un ouvrage recevable, c'est une condition qui cesse de
manquer* — **G-4, G-5 et G-6 restent ouvertes**, et **CA-IV-11 comme CA-IV-13 demeurent
insatisfaisables** faute d'un relecteur distinct du rédacteur. *Un brouillon écrit hors portes ne
franchit aucune porte* — et *zéro remontée ouverte ne veut pas dire pièce recevable.* Le détail par
Livre vit aux `README.md` des cinq dossiers.

⚠ **Le volume est arrêté depuis le 29 juillet 2026 — et « arrêté » n'est ni « terminé » ni
« publiable ».** La décision d'auteur **D-10** (PRD [v0.15 §14](2%20-%20Compendium/PRD/PRD.md), TOC
v0.31) place le compendium au statut de révision **RÉVISION FINALE**, sous un **régime de diffusion en
bibliothèque personnelle** : lecture par l'auteur, **aucune mise à disposition d'un tiers**, aucun
dépôt public, **aucune opposabilité**. La conformité est arrêtée sous **trois états qui ne se
confondent pas** — **satisfaite sur pièce** pour G-2, G-3 et G-7 (plus les quatre contrôles outillés,
rejoués le même jour, sorties 0) ; **close pour ce seul régime, par dérogation nommée**, pour G-1
(volets résiduels), G-4 (volet de fond), G-5 (balayage du Livre IV) et G-6 (trois lots, socle du
ch. 41), **dont le résidu reste entier et écrit** ; **non satisfaisable** pour **CA-IV-11 et
CA-IV-13**, qui exigent un relecteur distinct du rédacteur. ⚠ **Le motif de la dérogation est unique
et étroit** — *lecteur et rédacteur sont la même personne, il n'y a aucun tiers à protéger d'une
affirmation non réfutée* — et **elle tombe avec lui** : à la première diffusion, les quatre portes et
les deux critères redeviennent exigibles dans leur état. **Aucun énoncé n'est central** au sens de
CA-IV-01, **aucun vote adversarial n'a été conduit**, et **les trois volumes sources font toujours
foi**.

⚠ **L'arrêt a été rouvert le 30 juillet 2026, et rien de la réserve ci-dessus ne s'en trouve allégé.**
La décision d'auteur **D-11** (PRD [v0.16 §15](2%20-%20Compendium/PRD/PRD.md), TOC **v0.32**) **rouvre
D-10** pour une **passe de révision**, prise au titre de D-6. Son déclencheur est un **rapport
d'arbitrage externe** du 30 juillet 2026 — `eval.html`, **retiré de l'arbre depuis** et lisible au seul
historique git — qui conclut à une **révision majeure : accepté sur le fond, non diffusable en l'état**
(huit faiblesses majeures, sept mineures, dix recommandations ; **22 affirmations vérifiées, 19
confirmées, 3 partielles, 0 infirmée**). ⚠ **Ce rapport n'a lui-même aucune autorité** : il déclare en
sa §10 ne satisfaire ni CA-IV-11 ni CA-IV-13, ses dix rapporteurs étant des instances d'un même modèle
de langage — *des convergences entre rapports ne sont pas des convergences entre esprits
indépendants*. Ses constats entrent comme **remontées**, arbitrées par l'auteur. **Ce que D-11 change,
et c'est tout** : une seule décision de plan en découle, la **décision 18 du TOC**, qui **renverse la
décision 15a** — *la citation nominative l'emporte, la péremption se gérant par datation et non par
anonymat*. **Ce que D-11 ne change pas** : le statut **RÉVISION FINALE — bibliothèque personnelle est
maintenu pendant toute la durée de la passe** ; **CA-IV-11 et CA-IV-13 demeurent dérogés, non
satisfaits** ; **G-1 résiduel, G-4, G-5 et G-6 restent clos pour ce seul régime** ; la relecture tierce
que le rapport réclame **n'est pas fournie par le rapport lui-même**, et il l'écrit.

⚠ **La passe de révision est CLOSE depuis le 8 août 2026 — close, non achevée.** La décision d'auteur
**D-13** (PRD [v0.17 §16](2%20-%20Compendium/PRD/PRD.md), TOC **v0.33**) la referme **sans exécuter
son domaine résiduel**, et clôt le dépôt entier. **Ce qui ne sera pas fait est nommé ligne à ligne au
§16.2 du PRD** : la relecture tierce (RA-R1), l'élévation hors **[C]** des sept sources nommées
(RA-R2), le balayage des **261 tournures indéfinies** dans 44 pièces (résidu de RA-R4), la date de la
ligne directrice AMF (RA-R6, **quatre refus d'accès de l'hôte** — *une propriété de la source, non un
incident*), le ch. 46 (RA-R8), et le versement des `S-nnn` au corps (RA-R10, **674 emplois nus**
mesurés). ⚠ **Aucun de ces manques ne devient une conformité en cessant d'être suivi** : *une dette
qu'on cesse de suivre reste une dette ; elle change seulement de nom.* Le volume n'est donc ni
publiable, ni recevable, ni appelé à le devenir — **et le même jour, il change de titre** :
*« La somme agentique »* jusqu'au 8 août 2026, **« Interopérabilité et Orchestration Agentiques en
Entreprise »** depuis (décision 20 du TOC).

⚠ **Un rendu paginé existe depuis le 29 juillet 2026, et il ne requalifie rien non plus.**
[`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) — **1 000 pages** (re-mesurées le 9 août 2026), les cinquante chapitres des
cinq Livres **et une annexe hors plan** (la liste des 159 références du socle, ajoutée le
29 juillet 2026), **format Letter (215,9 × 279,4 mm) depuis la refonte typographique du 31 juillet
2026**, **sans aucune page blanche** — vérifié sur le rendu courant, **0 sur 1 000** —
est composé par [`build/build-pdf.sh`](2%20-%20Compendium/build/build-pdf.sh), **quatrième pipeline
du dépôt et le seul qui ne dérive pas du FESP**. ⚠ **Depuis le 9 août 2026, le script porte une
porte de pagination** : la cible de **mille pages exactement** est une instruction d'auteur, et le
build **échoue** si le rendu canonique ne la tient pas. *La pagination est une fonction en escalier
— un mot ajouté suffit à changer de marche —, et une cible qu'on constate au lieu de la vérifier se
perd au commit suivant, en silence.* Le calage se prend sur trois réglages du seul gabarit, tous
documentés dans [`build/compendium.template`](2%20-%20Compendium/build/compendium.template) : marges
verticales à **18/18 mm** (24/26 auparavant), pas d'interligne à **16,95 pt** (17,00 auparavant —
17,00 rend 1 001 pages, 16,90 en rend 999) et **Annexe I composée à 9,8/4,4 pt**, plus serré que le
corps, ce qui la fait passer de 112 à **62 pages**. ⚠ **Le bloc horizontal relevé sur les
monographies (30,0 à 187,0 mm) et le corps de 13 pt ne bougent pas** : le calage ne se prend pas sur
ce qui a été mesuré ailleurs. Le rendu retire du corps les trois appareils que le
volume tient hors corps (en-tête à cinq champs, thèse citée depuis le TOC, note de statut) et
**marque d'une dague les vingt-trois renvois** que cette coupe laisserait pendre, plutôt que de les
supprimer. ⚠ **Un second rendu existe depuis le 4 août 2026, et il ne requalifie rien davantage** :
[`Compendium.html`](2%20-%20Compendium/Compendium.html), **appareil de lecture à l'écran** du volume
— déposé ce jour-là sous le nom `presentation.html`, renommé le même jour (commit `d473913`).
**Un seul fichier de 1,75 Mio** (**1 832 473 octets**, re-mesurés le 9 août 2026 après le report du calage à mille pages — 1 831 155 du 8 au 9 août ; le
fichier versionné est en fins de ligne `LF` pures, et le décompte est celui de ses octets au dépôt.
⚠ *Ce n'est pas le décompte sur disque, et la version antérieure de cette phrase disait le
contraire* : le dépôt ne portant pas de `.gitattributes`, un poste réglé sur `core.autocrlf=true` —
celui de cette passe — obtient une copie de travail en `CRLF` de **1 836 452 octets**, soit
**3 979 de plus**, un par fin de ligne. Les deux arrondissent à 1,75 Mio, et *seul le premier se
reproduit d'un poste à l'autre*)**, sans
dépendance externe** et un seul lien sortant, vers le PDF : les
**118 figures** du volume y sont embarquées en SVG `data:` et retournées pour fond sombre, la
typographie reprend les deux fontes du rendu imprimé (Constantia, Corbel) et la justification est
réglée sur la mesure du livre, **79 signes**. Douze entrées — thèse, horloge, instruments, les cinq
Livres, socle, parcours, index des 56 notions, probité ; *le colophon existe en section mais n'a pas
d'entrée de navigation, et l'énumération antérieure le comptait à tort pour une treizième*. ⚠ **Trois choses qu'il n'est
pas.** *(a)* Il **ne fait pas autorité** : son propre colophon le déclare dérivé, et *le `.md` reste
la seule source*. *(b)* Il **n'est publié nulle part** — aucune page GitHub Pages, aucune diffusion :
c'est un fichier du dépôt, servi en local par
[`.claude/launch.json`](2%20-%20Compendium/.claude/launch.json) (`python -m http.server 8731`), et le
régime de **D-10**, maintenu par **D-11**, le gouverne comme il gouverne le PDF. *(c)* ⚠ **Il ne se régénère pas.** **Aucun
script du dépôt ne le reconstruit** depuis les cinquante `.md` : il est écrit à la main, ses
décomptes sont relevés à la main, et *un rendu sans chaîne se périme en silence* — c'est la
différence exacte d'avec `Compendium.pdf`, qui se recompose dans le commit de la pièce qu'il rend.
⚠ **Son horloge, elle, est calculée à l'ouverture** : la position d'« aujourd'hui » et l'âge du gel
se recalculent à chaque affichage — *cette page vieillit avec l'ouvrage qu'elle présente, sans
vieillir avec le texte qu'elle en tire.* ⚠ **Le rendu ne porte AUCUN avertissement de statut, et c'est une instruction d'auteur du
30 juillet 2026** : un bloc de colophon portant le **statut de révision finale, son régime de
diffusion et ses réserves** — portes dérogées, vote adversarial non conduit, CA-IV-11 et CA-IV-13 non
satisfaits, aucun énoncé central — a été écrit ce jour-là, **après qu'une mesure du PDF eut montré
qu'il manquait alors que trois documents de gouvernance le déclaraient présent**, puis **retiré sur
instruction**. ⚠ ***Le régime de diffusion vit donc au dépôt seul*** — PRD §14 et §15, TOC,
conspectus, en-tête des cinquante pièces —, et **un lecteur qui n'aurait que le PDF ne le lit nulle
part**. *Composer n'est pas publier* : le `.md` reste la seule source, et le PDF se régénère avec
elle.

Sa nature le distingue des trois autres : ce n'est ni un quatrième panneau ni un méta-index, mais
un **omnibus qui absorbe les Vol. I, II et III** en un seul ouvrage réordonné et dédoublonné, à
numérotation continue — **50 chapitres** en 5 livres, ≈ 376 000 à 401 000 mots projetés. Le décompte
est un **plafond dur** depuis la v0.23 (décision 13 du TOC, contrôle `C15`) : la somme ne dépasse
jamais cinquante chapitres, et toute insertion se paie par une **fusion** dans la même passe — les
deux entrées fusionnées étant conservées intégralement, en deux mouvements. C'est ainsi que le
**ch. 41, la fabrique d'agents** (entré en v0.22 sur instruction d'auteur, matière neuve sans volume
source, déclarée telle) a été payé par la fusion des ch. 47 et 48. Une fois **recevable** — et il ne
l'est pas : rédigé et composé ne valent pas publiable —, il se substituera à la lecture des trois
volumes ; **jusque-là, les trois volumes sources font foi.** Ses décisions structurantes :
numérotation continue, déduplication tracée sous chaque entrée, divergences héritées tranchées (et non plus signalées), méthode et gel unifiés, couverture
totale tracée — chaque section des sources est affectée à un chapitre d'arrivée ou marquée « coupe
assumée ».

⚠ Sa volumétrie est explicitement **indicative et non normative** : elle agrège des décomptes pris
par des commandes différentes, non comparables entre eux. La première tâche de sa rédaction est de
re-mesurer les trois corpus par une commande de référence unique.

## Ordre de lecture et renvois

**Vol. I → Vol. II → Vol. III**, la veille servant d'entrée rapide ou de mise à jour. ⚠ **Le Vol. IV
devait les remplacer tous les trois une fois recevable ; il ne le sera pas** — il est écrit, composé,
arrêté et clos, il n'est pas publiable, et [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) se
feuillette sans faire foi. *La règle de substitution n'est pas levée : elle est devenue sans objet.*

- **Vol. II présuppose Vol. I** pour la théorie du découplage, l'ingénierie des agents LLM,
  l'anatomie des protocoles, la sécurité de la couche agentique et la cryptographie post-quantique.
- **Vol. I illustre mondialement** ce que **Vol. II instruit au grain du droit canadien**.
- **Vol. III prolonge les deux** sur leur verrou commun, l'identité et son exploitation.
- **La veille les cite tous les quatre, à deux régimes distincts.** Les volumes *rédigés*
  fournissent des faits : §4.12 pour le Vol. I (réf. [217]), §8.4 pour le Vol. II (réf. [218]).
  Les volumes de *cadrage* ne fournissent aucun fait et ne prêtent que des instruments d'analyse :
  Vol. III (réf. [219], grille des cinq questions, §7.6 à 7.10), Vol. IV (réf. [220], décisions de
  fusion). Sa section 13 est le siège de ce rendu de compte, et son §13.1 pose la règle : un volume
  sans chapitre rédigé ni socle propre ne porte aucun fait.
- **Vol. IV les absorbe** : ses renvois inter-volumes deviennent des renvois internes.
- Un lecteur pressé côté canadien peut entrer directement par le **chapitre 13** du Vol. II
  (« le pont : des contraintes réglementaires aux frames déterministes »), son pivot.
- ⚠ **Le traité sur les essaims est hors de cet ordre, et il n'y entre par aucun bout.** Il ne cite
  aucun des six autres livrables, aucun ne le cite, et son objet n'est pas la pile protocolaire mais
  le régime de coordination qui la précède. *Il se lit seul, avant ou après n'importe lequel des
  autres* — et le lecteur qui cherche un pont entre lui et le triptyque devra l'écrire lui-même.

## Divergences factuelles entre volumes

Deux faits datés divergent d'un corpus à l'autre. Ils sont **signalés, non arbitrés** — la veille
les expose en §8.4, et le lecteur doit les trancher à sa date de citation :

| Objet | Vol. II (gel 16-17 juill.) | Veille (édition intégrale, 18 juill.) | État après revalidation |
|---|---|---|---|
| Ligne directrice IA de l'AMF — version finale | 30 mars 2026, avec **dette de vérification déclarée** (`lautorite.qc.ca` renvoie 403 aux outils) | 7 avril 2026 | **divergence ouverte** — la revalidation du 18 juillet a buté sur le **même 403** (sept tentatives, cinq adresses) ; aucune des deux dates n'est établie sur une source primaire directement consultée |
| Gouvernance d'AP2 | aucun transfert documenté au socle | don à la FIDO Alliance, **28 avril 2026** | **résolue** — source primaire datée, accessible et antérieure au gel du Vol. II ; frontière de socle, non désaccord |

L'entrée en vigueur du 1er mai 2027 est, elle, concordante entre les corpus, et ne l'a jamais cessé.

Les deux cas portent la même leçon sous deux formes. Sur AP2, deux corpus vérifiés de bonne foi
divergent parce que **leurs périmètres de sources diffèrent** — argument pour le millésimage
systématique. Sur l'AMF, ils divergent parce que **la source elle-même est inaccessible aux
outils** : c'est l'accessibilité de la source qui est mesurée, non la rigueur inégale des corpus,
et aucune discipline de veille ne corrige cela. ⚠ **L'édition intégrale de la veille rétracte en
conséquence la certitude de sa propre datation** (§13.6) : sa date du 7 avril repose sur des
sources secondaires, et n'est donc pas mieux étayée que celle du Vol. II.

⚠ **Le cadrage du Vol. IV tranchait ces deux divergences en faveur du Vol. II** — ligne directrice
AMF finale au 30 mars 2026, aucun transfert de gouvernance d'AP2 documenté (ch. 10) —
donc *contre* les lectures de la veille. L'arbitrage est consigné à son Annexe C. Sur AP2 il est
**périmé par une source primaire datée** ; ⚠ **sur l'AMF il a été DÉFAIT par le Vol. IV lui-même** :
la remontée R-IV-88 (TOC v0.27, réalignée en v0.29) établit, par extraction du 21 juillet 2026,
qu'**aucune des deux dates arbitrées ne figure aux pages officielles** — la somme écrit désormais
**« avril 2026 »**, déclare les trois états, et **proscrit de rétablir « 30 mars 2026 »**. *Une
divergence dont aucun terme n'est à la source n'est plus une divergence tranchée : c'est une absence
de datation.* Le chapitre porteur est le **ch. 27** (Livre III), non le ch. 31, qui n'écrit pas une
fois « AMF ». Et de
toute manière, tant que le compendium n'est pas **recevable** — ses cinquante chapitres sont un
brouillon écrit hors portes, que le PDF compose sans le publier —, **cet arbitrage n'a aucune
autorité** : les volumes sources font foi et la divergence reste ouverte — le plan le dit lui-même.

⚠ **L'édition du 8 août 2026 ajoute deux divergences d'une autre nature, et celles-là ne sont pas
des dates.** La veille corrige deux **lectures de texte juridique** que le corpus portait : l'article
12.1 de la Loi 25 (qui borne l'absence totale d'humain et ne prescrit aucun degré d'autonomie, contre
l'« intervention humaine déterminante » que le corpus lui prêtait) et l'avis ACVM 11-348 (qui ne
contient ni *agent*, ni *agentique*, ni *autonomie*, ce qui fait tomber l'opposition entre accroche
textuelle et accroche par inférence sur laquelle le Vol. II bâtissait son §8.4). **Ces deux
divergences sont tranchées, non ouvertes** : la lecture de la veille est adossée au texte, celle du
corpus ne l'était pas. ⚠ *Mais les volumes sont clos et ne les recevront pas — le lecteur qui cite
le Vol. II sur ces deux points cite un énoncé que la veille a réfuté.*

> ⚠ Le fichier `commun/faits-partages.md`, évoqué par le cadrage du Vol. III comme source unique
> de vérité pour les faits partagés, **n'existe pas et ne sera pas créé** : son PRD §7.5 a tranché
> de porter lui-même ces divergences. Chaque volume porte donc ses propres faits datés.

## Structure du dépôt

```
.
├── README.md                              ← ce fichier (avant-propos croisé)
├── Veille Technologique.md / .pdf         ← veille autonome, édition du 8 août 2026, faits gelés à cette date (100 p., 303 réf.)
├── Revue de littérature.md / .pdf         ← revue de la littérature académique, arrêtée au 9 août 2026 (40 p., 176 réf.)
├── Traité.md / .pdf                       ← traité « Systèmes multiagents en essaim », 10 août 2026 (100 p., 118 réf., 16 figures)
│                                             ⚠ ne cite aucun autre livrable, et aucun ne le cite ; seul rendu au gabarit d'article arXiv
│                                             (`Swarm Agentic Systems.md / .pdf` jusqu'au renommage du 10 août 2026)
├── figures/                               ← les 16 figures du traité, entrées le 11 août 2026
│   │                                         ⚠ COPIE ADAPTÉE des primitives du compendium, et non un import : viewBox de 468 unités
│   │                                         (6,5 po de corps) contre 445 là-bas, sans `venn` ni `frise`, avec `courbe` et `barres`
│   ├── dessine.py                           primitives ; ⚠ `rendu()` refuse une figure sans réserve
│   └── contenu.py                           les 16 entrées et leur rendu — `python figures/contenu.py`
├── Python/                                ← les trois contrôles de la racine, regroupés le 10 août 2026
│   │                                         ⚠ ils lisent leurs sources par chemin relatif au répertoire courant :
│   │                                         à lancer DEPUIS LA RACINE (`python Python/check-veille.py`), jamais d'ici
│   ├── check-veille.py                      contrôles de publication de la veille (renvois, cardinaux, bibliographie)
│   ├── check-resume.py                      budget de mise en page : le résumé tient-il sur la page de titre du PDF
│   └── check-revue.py                       contrôles de publication de la revue (appariement, tableaux, doublons, régimes)
│                                          ⚠ `gauntlet-log.md`, journal append-only des boucles bâtisseur/critique,
│                                            était ici jusqu'au 10 août 2026 — purgé, il ne se relit qu'à l'historique git
├── .gitignore                             ← couvre notamment les `__pycache__` (aucun bytecode au suivi git)
├── 1 - Corpus/                            ← le triptyque
│   ├── README.md                            synthèse consolidée des trois monographies
│   ├── 0 - Références/                      ⚠ 3 PDF de littérature source (32,5 Mio), déposés le 8 août 2026
│   │                                          — cités par AUCUN document du dépôt, aucune entrée de socle
│   ├── 1 - InteroperabiliteAgentique/       Vol. I
│   │   ├── README.md                          présentation du volume
│   │   ├── Chapitres/                         7 chapitres + 7 bibliographies + Annexe B (ADS) + TOC.md
│   │   ├── Monographie.md / .pdf              assemblage (569 p.)
│   │   ├── build/                             pipeline FESP (Mermaid → Pandoc → Typst)
│   │   └── LICENSE, .gitignore                seul `LICENSE` du dépôt — il ne vaut que pour ce volume
│   ├── 2 - OrchestrationAgentique/          Vol. II
│   │   ├── README.md                          présentation du volume
│   │   ├── monographie/                       29 pièces (parties I-VII, annexes, registre des gels)
│   │   │                                      + README.md, l'index de lecture des 29 pièces
│   │   ├── prd/                               PRD, PRDPlan, TOC, audit + 2 PDF sources — gouvernance
│   │   ├── verification/                      revalidations et grille de conformité CA-1..CA-8
│   │   ├── build/                             assemblage + pipeline Pandoc → Typst
│   │   ├── Monographie.md / .pdf              assemblage (387 p.)
│   │   └── .gitignore
│   └── 3 - EntrepriseAgentique/             Vol. III
│       ├── README.md                          présentation du volume (déposée le 29 juill. 2026)
│       ├── prd/                               PRD v1.3, TOC v0.8, PRDPlan v0.5 — gouvernance
│       ├── monographie/                       34 pièces rédigées + registre des gels
│       │                                      ⚠ verification/ (30 rapports) SUPPRIMÉ le 8 août 2026 — historique git seul
│       ├── build/                             pipeline FESP (copie du Vol. II) + assemble.py
│       └── Monographie.md / .pdf              assemblage (427 p., gabarit FESP) — non publiable
└── 2 - Compendium/                        ← Vol. IV
    ├── README.md                            vue synoptique dérivée du TOC (le « conspectus » du volume)
    ├── annexe-references.md                 liste des 159 références du socle — annexe hors plan du rendu
    ├── annexe-bibliographie.md              Annexe I — bibliographie générale consolidée (1 154 entrées), reliée au rendu
    ├── figures/                             les 118 SVG des chapitres + programme des figures et scripts de génération
    ├── Compendium.pdf                       rendu paginé des 50 chapitres + 2 annexes (1 000 p.) — brouillon non publiable, recomposé au calage du 9 août 2026
    ├── Compendium.html                      appareil de lecture à l'écran du volume (4 août 2026, ex-`presentation.html`)
    │                                          un fichier, sans dépendance externe, 118 figures embarquées — ⚠ écrit à la main, aucune chaîne ne le régénère
    ├── .claude/launch.json                  sert le dossier en local (python -m http.server 8731) pour lire Compendium.html
    ├── build/                               pipeline propre au volume (PAS une copie du FESP) — 8 fichiers
    │   ├── assemble.py                        50 pièces + 2 annexes → compendium.md, 23 renvois portés en note de marge
    │   ├── assemble-bibliographie.py          réunion dédoublonnée des bibliographies sources → annexe-bibliographie.md
    │   ├── accentuation.lua                   filtre Pandoc — règle d'accentuation du corps (31 juill. 2026)
    │   ├── compendium.template                gabarit COURANT — identité propre, Letter, marges relevées sur les monographies, Constantia/Corbel
    │   │                                      ⚠ calé le 9 août 2026 sur mille pages : marges 18/18 mm, pas 16,95 pt, Annexe I à 9,8/4,4 pt
    │   ├── springer.template                  gabarit précédent (29 juill. 2026), conservé — 155 × 235 mm, Times 10/12
    │   ├── echantillon.py / .template         échantillon de design — deux mêmes tranches de texte sous deux gabarits
    │   └── build-pdf.sh                       bash build/build-pdf.sh → Compendium.pdf ; ⚠ porte de pagination : ÉCHOUE hors de 1 000 p.
    ├── Livre I/ … Livre V/                  ⚠ rédaction hors portes — 50 pièces sur 50, brouillons
    │   ├── README.md                          état du livre, issues des remontées, sièges, volumétrie
    │   └── NN-….md / .html                    un chapitre par pièce — source + page à thème sombre
    └── PRD/                                 gouvernance de la rédaction (sous-dossier) — 13 fichiers
        ├── PRD.md                           v0.17 — portes, régimes de preuve, jalons ; §15 = D-11, §16 = D-13 (clôture)
        ├── TOC.md                           table des matières commentée (v0.33) — spécification
        ├── socle-consolide.md               socle consolidé S-001…S-159 (porte G-3, 28 juill. 2026)
        ├── registre-gel.md                  registre de gel, une ligne par chapitre
        ├── gel-2026-07-27.md                registre du gel unique (D-1) — volet Livre I de G-1, 12 faits repris à la source
        ├── gel-2026-07-28-volet-residuel.md volet résiduel de G-1 — 123 entrées à sensibilité temporelle sur 123 instruites
        ├── check-toc.py                     contrôles C1-C15 (python PRD/check-toc.py)
        ├── check-sieges.py                  contrôles S1-S5 inter-pièces — 26 sièges sur 50 pièces
        ├── check-compendium.py              contrôles P1-P8 du socle consolidé
        ├── decompte.sh                      commande de décompte de référence (porte G-2) — ⚠ SORTIE 1 sur l'arbre courant
        └── *-mutations.py                   validation par mutation des trois contrôles (3 fichiers)
```

**Où sont les `README.md`.** **Douze**, même date de comptage : la racine, le conteneur
[`1 - Corpus/`](1%20-%20Corpus/README.md) (la synthèse consolidée), les **trois** volumes du triptyque
— celui du Vol. III déposé le 29 juillet 2026 —, l'index de lecture des 29 pièces du Vol. II, le
conspectus du Vol. IV, et les **cinq** répertoires de Livres du compendium. *(Cardinal re-compté sur
l'arbre le 9 août 2026 : **12**, inchangé — `git ls-files | grep README`.)*
⚠ **`1 - Corpus/0 - Références/` n'en porte aucun**, et c'est le seul répertoire du dépôt **portant
des pièces déposées** dans ce cas : *trois PDF déposés sans un mot qui dise ce qu'ils font là.*
*(Les trente autres répertoires sans `README.md` sont des répertoires d'appareil ou de découpage —
`build/`, `prd/`, `PRD/`, `figures/`, `Chapitres/`, `verification/`, `.claude/`, le `monographie/`
du Vol. III, les **seize** sous-répertoires de parties et les **deux** `90-annexes/` — dont le
contenu est décrit par le `README.md` du dossier qui les porte.)*

## Construire les PDF

**Sept** chaînes distinctes, à lancer depuis le dossier concerné — une par livrable. *(Ce fichier
en annonçait **cinq** jusqu'au 9 août 2026, alors qu'il en listait déjà six : la revue de littérature
avait sa commande sans être comptée. La septième est entrée avec le traité sur les essaims, le
10 août 2026.)*

**Veille technologique** (racine) — invocation Pandoc directe, gabarit Typst par défaut :

```bash
pandoc "Veille Technologique.md" --pdf-engine=typst --toc -o "Veille Technologique.pdf"
```

**Revue de littérature** (racine) — même invocation que la veille, même gabarit :

```bash
pandoc "Revue de littérature.md" --pdf-engine=typst --toc -o "Revue de littérature.pdf"
```

**Traité** (racine) — **même invocation que les deux autres**, tout le réglage étant dans l'en-tête
YAML : **gabarit d'article arXiv** depuis le 10 août 2026 — marges **au pouce (2,54 cm)** sur les
quatre côtés (2,8 × 2,6 cm pour la veille et la revue), **`linestretch: 0.858`** qui porte l'interligne
à 13,6 pt pour un corps de 11 pt — *la valeur exacte d'un article LaTeX 11 pt ; c'était `0.9` et
13,9 pt jusqu'au recalage du 11 août 2026* —, **folio dès la page de titre**, **mots-clés dans le bloc du
résumé**, **pas de `section-numbering`**. ⚠ *Ce dernier point n'est pas un oubli* : les sept chapitres
portent leurs numéros **écrits à la main dans les titres**, et le gabarit Typst numéroterait
par-dessus — « 0.3.2 3.2 Titre ». ⚠ **La cible de 100 pages est tombée le 11 août 2026**, à 109, avec
l'entrée des seize figures, et elle est tombée exactement comme ce fichier l'annonçait : *sans porte
de pagination, rien ne le signale.* ☑ **Elle a été reprise le même jour**, en composant l'appareil —
tableaux, pseudocode, bibliographie — à 9 pt et en portant `linestretch` à **0.858**, soit 13,6 pt
d'interligne, la valeur exacte d'un article LaTeX 11 pt ; **les marges au pouce et le corps de 11 pt
sont inchangés**. ⚠ *C'est l'écart de marge, et lui seul, qui
fait sortir `check-resume.py` en 1
sur ce PDF* :

```bash
python figures/contenu.py                                    # → les 16 SVG
pandoc "Traité.md" --pdf-engine=typst --toc -o "Traité.pdf"
```

⚠ **Trois réglages Typst propres aux figures vivent dans `include-before`** de l'en-tête YAML, et
aucun n'est cosmétique. `#set image(width: 100%)` : les SVG sont dessinés à **468 unités**, soit la
largeur exacte du corps, une unité valant un point — sans cette règle Typst les lit comme des pixels,
rend à 351 pt, et les corps de texte des figures tombent d'un quart. `#show figure.where(kind: image):
set figure(numbering: none)` : **les figures portent leur numéro dans leur légende**, comme les sept
chapitres portent le leur dans leur titre, et Typst numéroterait par-dessus — « Fig. 3. – Figure 2.1c ».
Les deux dernières lignes composent la légende à 9 pt et la ferrent à gauche.

**Vol. I** — pipeline FESP, avec pré-rendu des 28 diagrammes Mermaid ; depuis
`1 - Corpus/1 - InteroperabiliteAgentique/` :

```bash
bash build/build-pdf.sh                              # Monographie.pdf
```

**Vol. II** — assemblage des 29 pièces, puis une **copie** du même pipeline ; depuis
`1 - Corpus/2 - OrchestrationAgentique/` :

```bash
python build/assemble.py                    # monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md    # → Monographie.pdf
```

☑ **L'assemblage du Vol. II remarche depuis le 8 août 2026.** `build/assemble.py` cherchait `TOC.md` à
la racine du volume alors qu'il vit dans `prd/`, et échouait avant d'écrire une ligne. ⚠ **La reprise a
trouvé un second défaut que rien ne signalait, et il touchait aussi le Vol. III** : les deux
assembleurs ne rebasaient pas les cibles relatives des pièces, si bien qu'un renvoi valide dans
`monographie/03-partie-III/` mourait une fois concaténé à la racine du volume. Les deux scripts
rebasent désormais. Les copies du pipeline évoluent séparément ; un correctif au Vol. I ne se propage
pas au Vol. II.

**Vol. III** — assemblage des 34 pièces, puis une **troisième copie** du même pipeline
(créée le 23 juillet 2026, au gabarit des monographies) ; depuis
`1 - Corpus/3 - EntrepriseAgentique/` :

```bash
python build/assemble.py                    # monographie/ → Monographie.md
bash   build/build-pdf.sh Monographie.md    # → Monographie.pdf (427 p.)
```

Les trois copies du FESP évoluent séparément. ⚠ La **note d'état** que le PDF du Vol. III portait en
page 2 a été **retirée le 24 juillet 2026** sur demande de l'auteur (constante `ETAT` supprimée de
`build/assemble.py`) : la page de titre est directement suivie du résumé. *Le statut non publiable
ne dépend d'aucune page qui le déclare* — il tient aux quinze remontées ouvertes (R-G-43 à R-G-57)
et à la dette de vote sur F-92 et F-96.

**Vol. IV** — assemblage des 50 pièces des cinq Livres, puis un pipeline **propre au volume** (créé
le 29 juillet 2026, gabarit Typst relevé sur deux monographies Springer) ; depuis `2 - Compendium/` :

```bash
bash build/build-pdf.sh                     # Livre I/ … Livre V/ + 2 annexes → Compendium.pdf (1 000 p.)
```

⚠ Ce quatrième pipeline **ne dérive d'aucune des trois copies du FESP, et aucune ne dérive de lui** :
la règle d'indépendance vaut donc pour **quatre**. Le script publie à chaque exécution ce qu'il a
assemblé et marqué (50 chapitres, 5 livres, 23 renvois marqués d'une dague), et il **échoue** si une
pièce ne porte pas les trois appareils qu'il retire — une pièce déformée passerait sinon sans bruit.
⚠ **Depuis le 9 août 2026, il échoue aussi hors de la cible de mille pages.** La porte ne vaut que
pour le **rendu canonique** — un essai (`OUT_PDF=…`) ou le gabarit `springer` composent une maquette
qui n'a pas cette cible —, et *elle n'avertit que si `pypdf` manque* : sans lui, le PDF est écrit et
la cible **n'est pas vérifiée**. C'est la seule des sept chaînes qui oppose une condition au rendu
qu'elle vient d'écrire.

⚠ **Les sept chaînes ne produisent que des PDF.** Les `.html` du Vol. IV — les **cinquante pages de
chapitre** et [`Compendium.html`](2%20-%20Compendium/Compendium.html), l'appareil de lecture du
volume — **ne sortent d'aucune d'entre elles** : `build/` ne contient aucun générateur HTML, et ces
fichiers sont écrits à la main. *Il n'y a donc pas de commande à donner ici, et c'est précisément le
problème* : la règle du « rendu versionné avec sa source » ne peut pas s'y appliquer, et rien ne
signale qu'une page est en retard sur le `.md` dont elle est tirée. Pour lire
`Compendium.html`, depuis `2 - Compendium/` :

```bash
python -m http.server 8731
```

⚠ **Le budget de mise en page a désormais un contrôle, et il n'en avait pas.** Ce fichier notait que
« *aucun contrôle ne voit ce budget — ni `check-veille.py`, ni le rendu : un débordement qui se fait
rogner ne lève aucune erreur* ». C'était exact, et la passe du 8 août 2026 l'a vérifié à ses dépens :
en rallongeant le résumé, elle a fait tomber sa dernière ligne à **y = −27,2 pt**, soit **100,8 pt
sous la marge basse** — une dizaine de lignes composées hors page et **rognées en silence**, avec
`pandoc` en sortie 0. [`check-resume.py`](Python/check-resume.py) mesure désormais la chose elle-même,
dans le PDF rendu — **depuis la racine du dépôt** :

```bash
python Python/check-resume.py
```

Il décompresse le flux de la page de titre et relève l'ordonnée la plus basse où du texte est
réellement posé. ⚠ *Deux pièges y sont neutralisés, ne pas les réintroduire* : `/Type/PageLabel`
contient `/Page` et fait prendre un objet d'étiquetage pour une page ; et le gabarit **ne met pas la
position dans la matrice de texte** — `Tm` y vaut `1 0 0 -1 0 0`, la position réelle étant portée par
le `cm` qui précède chaque `BT`. *Mesurer `Tm` rend zéro partout, ce qui ressemble à un résultat.*
Le contrôle a été **calibré sur le PDF de l'édition précédente**, où il retrouve les **104,8 pt** que
ce fichier avait relevés à la main le 29 juillet 2026.

⚠ **Et ce calibrage est exactement sa limite, découverte le 10 août 2026.** La marge basse y est une
**constante**, `MARGE_BASSE = 73.7`, tirée de l'en-tête de la veille ; le contrôle mesure par
ailleurs *tout* texte posé en page 1, **folio compris**. Rejoué sur `Traité.pdf`, qui compose à
**2,54 cm** et numérote dès la page de titre, il **sort 1 sur le numéro de page** — le bloc du résumé
et des mots-clés, lui, finit **212 pt au-dessus de la marge**. *Un contrôle transporté sur un gabarit
pour lequel il n'a pas été calibré ne mesure plus ce qu'il annonce ; il n'a pas été corrigé, et le
dépôt est clos.* ⚠ *Le verdict a tenu aux trois réglages successifs du traité en une journée — marges
à 2,35 cm, puis 3,2 cm, puis 2,54 cm : il sortait 1 les trois fois, toujours sur le folio.*

**Prérequis :** Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf` — ☑ *`pypdf` **6.15.0** est installé
depuis la passe du 9 août 2026, et il cesse d'être facultatif : la **porte de pagination du
compendium l'interroge au build** et se contente d'un avertissement s'il manque. Les décomptes du
8 août, pris par lecture directe du `/Count` de l'objet `/Type /Pages` faute de la bibliothèque, ont
été **confrontés à `pypdf` le 9 août : mêmes valeurs sur les six PDF*** ; polices Liberation Sans et
DejaVu Sans (pipeline FESP), New Computer Modern (veille), Times New Roman (compendium — repli
Libertinus Serif, signalé à l'exécution) ; pour les diagrammes, Node ≥ 18 +
[`@mermaid-js/mermaid-cli`](https://github.com/mermaid-js/mermaid-cli) et un Chromium. Les quatre
`build-pdf.sh` exportent eux-mêmes `PYTHONUTF8=1` — inutile de le faire à la main sous Windows.
**Règle permanente :** régénérer et versionner le PDF avec sa source — jamais la source seule.

## Ce qui reste vivant

Le domaine se périme par trimestres, et ces corpus par morceaux. Échéances datées à revalider
avant toute réutilisation ou publication.

⚠ **Le dépôt étant clos, personne ne les revalidera : la charge passe entièrement au lecteur.** Ce
tableau ne décrit plus un plan de maintenance mais **la carte de ce qui périmera ces documents**, et
chaque ligne échue après le 8 août 2026 rend son objet faux sans que rien dans le dépôt ne l'indique.
*Un corpus clos ne cesse pas de vieillir ; il cesse seulement d'être rattrapé.*

| Échéance | Objet | Documents touchés |
|---|---|---|
| ☑ **échue le 28 juillet 2026** | Révision de la spécification MCP (protocole sans état) — **la révision `2026-07-28` est versée à la veille** (§4.1 : noyau sans état, `server/discover`, dépréciation de Roots, Sampling, Logging et de l'enregistrement dynamique de client). ⚠ **Les volumes ne sont PAS rattrapés** : le Vol. I ch. 3 et le Vol. II ch. 1, 2, 7 décrivent l'état antérieur **à leur date de gel**, et le Vol. II l'écrit lui-même en toutes lettres — *un chapitre gelé douze jours avant une révision annoncée décrit en connaissance de cause un état daté* | Veille §4.1 (**à jour**) ; Vol. I ch. 3, Vol. II ch. 1, 2, 7 (**périmés, non corrigés**) |
| après le 26 août 2026 | Texte final du règlement du cadre bancaire canadien ; arrêté désignant l'organisme de normalisation | Veille §8.4 ; Vol. II ch. 14, 15, 24 |
| cible T4 2026 | Lancement effectif du RTR — cible précédée de quatre cibles abandonnées depuis 2019 | Veille §8.4 ; Vol. II ch. 15, 24 |
| ☑ **échue le 2 août 2026** | **Obligations de transparence de l'article 50** du règlement européen sur l'IA, **marquage compris** — et activation des pouvoirs de la Commission sur les modèles à usage général (amendes jusqu'à 3 % du chiffre d'affaires mondial). ⚠ **Ce dépôt annonçait le marquage au 2 décembre 2026, et c'était mal cadré** : décembre n'est qu'un **délai de grâce de quatre mois pour le seul article 50(2)**, réservé aux systèmes mis sur le marché avant le 2 août 2026 | Veille §8.1, §12.1 (**corrigées**) ; Vol. I à IV (**périmés, non corrigés**) |
| ☑ **échue le 2 août 2026** | **Première accroche textuelle de l'agentique en droit européen** : la Commission range explicitement les « AI agents » parmi les systèmes à interaction directe soumis à l'article 50(1) | Veille §8.1 (**à jour**) |
| 24 août 2026 | Entrée en vigueur du règlement administratif n° 10 relatif au RTR (DORS/2026-133) — cadre juridique, **non mise en service** | Veille §8.4, §12.1 ; Vol. II ch. 15, 24 |
| 2 décembre 2026 | Fin du délai de grâce de l'article 50(2) ; et nouvelles interdictions des articles 5(1)(ba) et 5(1)(bb) annoncées pour ce mois | Veille §8.1, §12.1 |
| **1er mai 2027** | Entrée en vigueur simultanée d'E-23 (BSIF) et de la ligne directrice IA de l'AMF | Veille §4.11.5, §8.4 ; Vol. I ch. 5 à 7 ; Vol. II ch. 9, 11, 20 |
| continue | Trajectoire du projet de loi C-36 — ⚠ **première lecture le 15 juin 2026, aucune activité en deuxième lecture au 8 août 2026** ; et c'est une loi sur la vie privée, non un cadre d'IA, ce que ce dépôt présentait trop largement | Veille §8.4 ; Vol. II ch. 10 |
| ☑ **survenue le 13 juillet 2026** | Bulletin ***Generative and Agentic AI*** du BSIF — saines pratiques non contraignantes, définition de l'IA agentique, chaînage d'outils et accès surprivilégié. *Le régulateur prudentiel canadien nomme l'agentique avant l'entrée en vigueur de sa ligne directrice* | Veille §8.4 (**à jour**) ; Vol. II ch. 9, 14 (**périmés**) |

## Avertissements

- **Aucun avis juridique ni conseil d'investissement.** Ces ouvrages rapportent des textes et en
  proposent des lectures d'architecture qui engagent leur auteur seul.
- **Aucune recommandation de fournisseur.** Les instanciations sur une pile d'éditeur (IBM
  notamment) sont des cas documentés, pas des verdicts comparatifs.
- **Statuts et chiffres.** Les métriques d'adoption sont, sauf mention contraire, auto-déclarées
  par les acteurs et attribuées comme telles ; les statuts *preview* ne sont jamais présentés comme
  *disponibilité générale* ; les projections d'analystes portent leur millésime.
- **Lacunes exposées, non comblées.** Le Vol. II en recense onze ; le Vol. III, **vingt-deux** — dont
  **trois closes**, et non quatre : son PRD §10 ne porte « INSTRUITE ET CLOSE » qu'aux entrées 1, 2
  et 11, la 10 étant « instruite, non arbitrée » et la 15 « instruite, **non close** » ; la veille,
  **vingt-cinq questions ouvertes** (§11, cardinal confirmé par
  `check-veille.py`). Aucune n'est comblée par une
  source de moindre qualité.
- **Assistance par agents.** Ces travaux ont été produits avec l'assistance de pipelines de
  recherche multi-agents, selon les méthodes de vérification décrites dans chaque document ; la
  responsabilité éditoriale est celle de l'auteur.

## Notes de maintenance

Le `README.md` de la racine a été resynchronisé le 18 juillet 2026 sur
l'arborescence réelle, sur l'accession du Vol. III à une gouvernance complète (`doc/`) et sur les
décomptes **re-mesurés** — veille 142 p. / 244 réf. / 14 sections, Vol. I
569 p. / 69 p. / 28 diagrammes / 12 ADR, Vol. II 387 p. / 66 p. / 29 pièces / 46 entrées de socle,
tous inchangés. Le 23 juillet 2026, la passe complémentaire de la veille (sous-section 12.4,
l'après-agentique en préimpression) porte ses décomptes à **144 p. / 256 réf.**, re-mesurés sur le
PDF régénéré ; les chiffres du 18 juillet ci-dessus décrivent l'état de cette date-là. La passe de
révision du même 23 juillet (corrections vérifiées et aération des sections 4.10 et 10, en vue de
la publication arXiv) porte la pagination à **145 p.**, références inchangées. Une dernière passe du
même 23 juillet — révision interne à six dimensions (retrait du saut de page avant la section 13,
34 correctifs vérifiés) puis correction du sourcing du cas d'adoption de Block (§6.4, référence [257]
ajoutée) — porte les décomptes à **146 p. / 257 réf.**, re-mesurés sur le PDF régénéré.

Le même 23 juillet 2026, une passe de cohérence a réaligné les `README.md` sur l'état
réel du dépôt : Vol. IV porté à **TOC v0.11** (57 chapitres, 10 livres, ≈ 369 000–394 000 mots
projetés) avec son `README.md` ; renommage `doc/` → `prd/` (Vol. II) et
suppressions des articles de synthèse et des `index.html` (Vol. I et II) constatés **committés**
(commit `fd8f1be`, arbre de travail propre) ; création du pipeline FESP du Vol. III (troisième copie
indépendante) enregistrée ; nom du dépôt corrigé de « Monographies » en `Agentique` dans les
fichiers du démonstrateur `Borealis-Go`.

**Le 25 juillet 2026**, les cinq `README.md` du dépôt ont été resynchronisés
sur la restructuration du commit `60f57f6` : renommages `1 - Corpus Agentique/` → **`1 - Corpus/`**
et `2 - Compendium Agentique/` → **`2 - Compendium/`** répercutés dans tous les chemins et tous les
liens ; **suppression du démonstrateur `Borealis-Go/`** consignée là où il était annoncé comme
livrable vivant (README de la racine et du Vol. I), avec ses conséquences sur la
référence [217] de la veille — signalées, **non corrigées dans la veille**. Décomptes **re-mesurés
sur pièce** à cette date, tous inchangés : veille **146 p. / 257 réf.** (`python check-veille.py`,
sortie 0), Vol. I **569 p. / 28 diagrammes**, Vol. II **387 p. / 29 pièces**, Vol. III **427 p. /
34 pièces / 30 rapports de vérification**. Un renvoi cassé a été corrigé dans le périmètre de la
passe — les quatre lignes `../doc/…` de `…/2 - OrchestrationAgentique/monographie/README.md`,
repointées vers `../prd/…`.

**Le 29 juillet 2026**, ce `README.md` a été resynchronisé sur **l'ajout de [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf)** et sur le
quatrième pipeline qui le compose : chaînes de rendu portées de quatre à **cinq**, arborescence du
Vol. IV réalignée sur ses cinq Livres et son `build/`, règle du « PDF versionné avec sa source »
étendue au compendium. Décomptes **re-mesurés sur pièce** à cette date : **847 pages**
(`pypdf`, sur le PDF versionné), **50 chapitres en 5 livres** et **23 renvois marqués d'une dague**
(sortie de `build/assemble.py`), **159 entrées** au socle consolidé, TOC **v0.30** et PRD **v0.14**.
⚠ **Aucun de ces chiffres ne requalifie le volume** : les cinquante chapitres demeurent un brouillon
non publiable, et *composer n'est pas publier*. Le reste de l'état du Vol. IV — issues des remontées,
volumétrie par Livre, décisions d'auteur — vit aux documents de gouvernance du volume et n'est pas
repris ici.

**Le 29 juillet 2026, seconde passe du même jour** : le Vol. IV est **arrêté en révision finale pour
une diffusion en bibliothèque personnelle** (décision d'auteur **D-10**, PRD **v0.15** §14, TOC
**v0.31**), et les porteurs de statut ont été réalignés — ce `README.md`
et les deux fichiers du volume. Le **colophon** du rendu a été
récrit et [`Compendium.pdf`](2%20-%20Compendium/Compendium.pdf) **recomposé** : **847 pages**,
re-mesurées (`pypdf`). ⚠ **Un défaut de composition a été trouvé et corrigé dans la passe** : le
colophon allongé débordait sur une seconde page — *la page de titre doit rester unique*, et seul le
décompte de pages l'a montré, aucun contrôle ne voyant cette classe. **Conformité arrêtée sous trois
états** : **satisfaite sur pièce** (G-2, G-3, G-7, plus les quatre contrôles rejoués le même jour,
sorties 0), **close pour ce seul régime par dérogation nommée** (G-1 résiduel, G-4 fond, G-5 balayage,
G-6 lots), **non satisfaisable** (CA-IV-11, CA-IV-13). ⚠ **Aucun de ces gestes ne rend l'ouvrage
publiable** : *arrêter n'est ni terminer ni publier*, et la dérogation tombe à la première diffusion.

**Le 29 juillet 2026, troisième passe du même jour** : sur instruction d'auteur, le rendu du Vol. IV
reçoit une **annexe hors plan après le chapitre 50** —
`audit-references.md`, l'**inventaire et la validation des
159 références** du socle consolidé. Décomptes **re-mesurés sur pièce** : **863 pages** (`pypdf`, sur
le PDF versionné), **50 chapitres en 5 livres plus 1 annexe** et **23 renvois marqués d'une dague**
(sortie de `build/assemble.py`). ⚠ **Trois choses que cette passe ne fait pas.** *(a)* Elle **n'ajoute
aucune annexe au plan** : l'annexe n'est **aucune des neuf A à I** du `TOC.md`, et l'**Annexe I — la
bibliographie générale consolidée — reste à écrire** ; le compendium **n'a toujours pas de
bibliographie**, ni la moindre URL. *(b)* ⚠ **Être relié n'est pas faire autorité** : c'est un
**rapport de mesure sans autorité**, du régime d'`audit.md`, **jamais
citable à l'appui d'un énoncé** ; ses constats sont des **remontées non arbitrées**. *(c)* Elle **ne
consomme aucun numéro de chapitre** — le plafond de cinquante tient —, **ne franchit aucune porte** et
**ne requalifie rien**. Le `TOC.md` et le `PRD.md` **ne sont pas touchés** : *un rapport remonte, il ne
tranche pas.*

**Le 29 juillet 2026, quatrième passe du même jour** : l'annexe reliée est **simplifiée en une liste**,
sur instruction d'auteur. Le rendu reçoit désormais
[`annexe-references.md`](2%20-%20Compendium/annexe-references.md) — les **159 entrées** du socle,
identifiant, objet, niveau, provenance et datation de la source, groupées par volume d'origine — à la
place du rapport d'analyse. Le rapport reste alors au dépôt sous le nom `audit-references.md`, **hors
rendu**, avec son régime inchangé — sans autorité, jamais citable à l'appui d'un énoncé. *Les deux se
distinguent par leur nom : l'`annexe-` est reliée, l'`audit-` ne l'est pas.* ⚠ **Ce constat a été
dépassé depuis** : `audit-references.md` a été retiré de l'arbre, comme `audit.md` et `eval.html` — les
trois ne se lisent plus qu'à l'historique git (voir « Reliquats définitifs à la clôture »). Décomptes **re-mesurés sur
pièce** : **1 114 pages** au 8 août 2026, après la refonte typographique du 31 juillet 2026 ; l'annexe pesait dix pages au gabarit de la refonte
Springer, contre vingt-sept
pour le rapport — ⚠ *ce coût-là n'a pas été re-mesuré au gabarit neuf.* La ligne de `sed` qui élargissait
les tables à sept colonnes est **retirée du script**, sa grille n'étant plus composée. ⚠ **Ce que la
passe ne change pas** : l'annexe **n'est toujours aucune des neuf annexes A à I**, elle **n'est pas une
bibliographie** — elle inventorie des **faits**, non les **documents** dont ils proviennent —, et
l'**Annexe I reste à écrire**. ⚠ **Ce dernier point a cessé d'être vrai le lendemain, et ce fichier ne
le portait pas** : l'**Annexe I existe depuis le 30 juillet 2026** —
[`annexe-bibliographie.md`](2%20-%20Compendium/annexe-bibliographie.md), **1 154 entrées uniques**,
réunion verbatim et dédoublonnée des bibliographies des trois volumes sources. *Elle est une réunion,
non une vérification* : son propre régime interdit d'y lire le niveau de preuve d'un fait, qui se lit
à l'entrée de socle. Le compendium a donc une bibliographie ; il n'a toujours **aucune URL**.

**Le 29 juillet 2026, cinquième passe du même jour** : l'**édition d'août 2026 de la veille
technologique**, sur instruction d'auteur — « fondée sur le compendium et une recherche exhaustive
sur le net ». Faits **gelés au 29 juillet 2026**, édition datée du 1er août. Décomptes
**re-mesurés sur le PDF régénéré** : **159 p. / 266 réf.** (contre 146 / 257), 14 sections et
15 tableaux inchangés, `python check-veille.py` en sortie 0. **Ce que la passe verse** : la révision
**2026-07-28** de MCP — noyau sans état, `server/discover`, requêtes à plusieurs allers-retours,
routage par en-têtes, dépréciation de Roots, Sampling, Logging et de l'enregistrement dynamique de
client, et **première politique de dépréciation datée** du corpus protocolaire (§4.1) ; le fait de
tempo qui lui répond — **A2A n'a rien publié depuis le 28 mai 2026** (§4.2) ; le **règlement (UE)
2026/1744**, publié au JO le 24 juillet et en vigueur le 27, avec ce qui s'applique **le 2 août
2026** malgré le report du haut risque (§8.1) ; la charte du second groupe communautaire du W3C
(§5.2) ; les superpositions COSAiS du NIST (§8.2) ; l'échéance du rail canadien (§8.4) ; et
**deux sous-sections neuves sur le corpus compagnon** (§13.8, §13.9). ⚠ **Trois choses que cette
passe ne fait pas.** *(1)* **Son régime est plus faible et il est déclaré** : consultation directe
des sources primaires, **sans ronde de vérification adverse** — celui de la §12.4, non celui des
§4.6 à §4.13 (§2.2 et §10). *(2)* Elle **n'a pas versé** les métriques d'adoption les plus citées du
domaine, faute d'avoir atteint leur publication primaire (§6.5) — *un chiffre qu'on ne peut pas
rattacher à son éditeur n'est pas un fait affaibli, ce n'est pas un fait*. *(3)* Elle **ne fait
reposer aucun énoncé sur le Vol. IV arrêté** : le refus est inchangé, ses **motifs le sont
entièrement** — diffusion bornée sans opposabilité, socle dérivé sans source primaire propre,
dérogation conditionnelle (§13.8). ⚠ **Deux défauts de la passe sont consignés plutôt que tus, et
aucun des deux n'a été trouvé par le contrôle seul.** `check-veille.py` a rattrapé **trois doublons
bibliographiques** que la rédaction avait introduits — AIP [23], le groupe W3C d'identité d'agents
[31] et la page des publications d'A2A [98] figuraient **déjà** au corpus, et le protocole AIP y
était même **discuté au corps** ; les entrées surnuméraires ont été retirées. Mais **cinq renvois
visaient la section 4.2 pour MCP, qui est la section 4.1** : *un renvoi qui existe mais désigne la
mauvaise section, aucun contrôle ne le voit* — seule la collation du plan réel l'a montré. Un
sixième écart est **signalé sans être corrigé**, la règle du dépôt l'interdisant : la réf. [217]
pointe un démonstrateur retiré de l'arbre le 25 juillet 2026, et la limite est portée à la §10 de
l'édition plutôt qu'à la référence.

**Le 29 juillet 2026, sixième passe du même jour** : deux **budgets de mise en page** posés par
l'auteur sur la veille — le **résumé doit tenir sur la page de titre**, le **sommaire exécutif sur
trois pages** (5, 6 et 7). Les deux étaient enfreints par la passe précédente, et **le premier
silencieusement** : le gabarit Typst compose le résumé dans un bloc **qui ne se scinde pas**, si bien
qu'un résumé trop long ne passe pas à la page suivante — il **se fait rogner sous la marge**, et
`pandoc` sort sans erreur. Mesuré sur le PDF : la dernière ligne du résumé tombait à **y = −24,6 pt**,
soit **98 pt sous la marge basse** (73,7 pt), et le sommaire mordait de **344 caractères** sur une
quatrième page. **Corrigé par condensation, en trois passes mesurées** : le résumé passe de
**3 451 à 2 750 caractères** et de six paragraphes à quatre — la grille des cinq questions rejoint le
paragraphe des couches, dont elle est le diagnostic — ; les constats 11 et 12 sont resserrés ; et
« Méthode en bref » perd son détail par édition, qui vit déjà en §2.2 et n'a rien à faire dans un
sommaire. **Aucun énoncé n'est retiré**, et l'occasion a servi à corriger une formule que la §13.8
avait périmée : le résumé disait « deux cadrages », il dit désormais **quatre volumes tous rédigés
dont deux ne fournissent aucun fait**. **État vérifié sur le rendu** : résumé à **y = 104,8 pt**
(31 pt de dégagement), sommaire **pages 5-7**, « 1 Introduction » en page **8**. Décomptes re-mesurés :
**158 p. / 266 réf.**, `check-veille.py` en sortie 0. ⚠ **Aucun contrôle ne voit ce budget** — ni
`check-veille.py`, ni le rendu : *un débordement qui se fait rogner ne lève aucune erreur.*

**Le 29 juillet 2026, septième passe du même jour** : la veille reçoit le titre que l'auteur énonce —
**« Interopérabilité et orchestration agentique en entreprise »** — et, avec lui, la section qui le
rend exact. ⚠ **Le titre antérieur disait « orchestration des processus d'affaires », et l'écart
n'était pas de style mais de périmètre** : les six sous-sections de la §4.11 traitent toutes de
l'orchestration des *processus*. Le balayage du document entier a mesuré l'autre orchestration —
celle des *agents* — à **zéro occurrence** sur douze motifs (« orchestration multi-agent », « patron
d'orchestration », « agent superviseur », « framework d'agents », « planificateur », *handoff*,
*swarm*, « sous-agent », « graphe d'agents », « délégation hiérarchique », « mémoire partagée »,
ReAct). **La réponse est une sous-section neuve, la §4.14**, fondée sur la recherche `/last30days`
(« Agentic interoperability and orchestration in the enterprise » — 45 éléments, 3 sources sur 5 ;
X et YouTube absents faute d'authentification) puis **sur sources primaires vérifiées** : la
taxonomie **MAST** (quatorze modes en trois catégories, 150 traces annotées, validée sur plus de
1 600 traces de sept cadriciels), la documentation du SDK d'agents d'OpenAI (les transferts *sont*
des outils, `transfer_to_<nom_agent>`, historique complet transmis par défaut), la bibliothèque
`langgraph-supervisor`, et l'annonce de disponibilité générale du harnais géré d'AgentCore — **déjà
au corpus en réf. [106]**, doublon que `check-veille.py` a repris. Trois références neuves, [267] à
[269]. ⚠ **Le fait négatif est le cœur de la section** : *aucun* des trois protocoles ne décrit de
topologie d'orchestration, et c'est pourquoi elle **n'est pas comptée comme une huitième couche** —
les sept ont chacune un porteur candidat, celle-ci n'en a aucun. **Le décompte de sept est
maintenu.** ⚠ **Et la passe a trouvé mieux qu'un manque : la lacune était celle de la veille
seule.** Le **ch. 2 du Vol. I** traite ce front depuis juin 2026 — balayage sur pièce : six
occurrences de MAST, sept de ReAct, sept de l'orchestrateur, trois du sous-agent, deux du
superviseur, trente-sept de la mémoire. *C'est exactement la classe de défaut que la §13 prend pour
objet — une lacune de couverture d'un document du dépôt, comblée par le texte rédigé d'un autre.*
Une question ouverte s'ajoute (**QO 25**, cardinal porté à vingt-cinq). ⚠ **Ce que la passe a refusé
de verser** : les cinq patrons canoniques tels que les publient les blogues de contenu, et le chiffre
très cité « LangGraph dans 43 % des déploiements agentiques d'entreprise » — aucune publication
primaire atteinte. Décomptes re-mesurés : **161 p. / 269 réf.**, `check-veille.py` en sortie 0, et
**les deux budgets de mise en page tiennent** (résumé à y = 104,8 pt ; sommaire en pages 5-7).

**Le 29 juillet 2026, huitième passe du même jour — la passe de dépôt final** : les **onze `README.md`**
que portait le dépôt ont été relus et resynchronisés, sur instruction d'auteur, et **un douzième
`README.md` a été déposé** — celui du Vol. III. *(Cardinal re-compté sur l'arbre à cette date :
**12 `README.md`** après la passe.)* **Ce que la passe a trouvé, et corrigé.** *(1)* **Six estampilles de version périmées**, toutes
décrivant un état *courant* et non un fait daté : ce `README.md` annonçait **TOC v0.30 / PRD v0.14** en
deux endroits (section du Vol. IV et arborescence) alors que le dépôt porte **v0.31 / v0.15** ; la
gouvernance du Vol. IV annonçait **PRD v0.11 et TOC v0.26** dans sa
section d'autorité, soit quatre et cinq versions de retard, et créditait `check-compendium.py` de
**P1-P7 / 15 mutations** quand le script en porte **P1-P8 / 17**. ⚠ *Une estampille de version en retard
ne se distingue d'un constat daté que par sa fonction : celle qui dit « voici l'autorité courante » est
fausse, celle qui dit « voici ce que la passe a lu » est exacte.* *(2)* **Le Vol. III a reçu son premier
[`README.md`](1%20-%20Corpus/3%20-%20EntrepriseAgentique/README.md)** : il était **le seul des trois
volumes à n'en porter aucun**, et le lecteur n'avait aucune entrée qui lui fût destinée.
Document **dérivé**, sans fait neuf. *(3)* **Deux `.pyc` versionnés de plus** ont été relevés
sous `2 - Compendium/PRD/__pycache__/` — le total suivi est de **trois**, non d'un —, et l'**absence de
licence à la racine** est portée au tableau des reliquats. ⚠ **Ni l'un ni l'autre n'est corrigé ici** :
retirer un fichier versionné et déposer une licence sont des gestes qui se demandent. **Décomptes
re-mesurés sur pièce à cette date, tous inchangés** : veille **161 p. / 269 réf.**
(`check-veille.py`, sortie 0), Vol. I **569 p. / 28 diagrammes** (motif ancré), Vol. II **387 p. /
29 pièces**, Vol. III **427 p. / 34 pièces / 30 rapports**, Vol. IV **863 p.** *(⚠ chiffre de la passe,
rétabli le 8 août 2026 : ce fichier portait ici **1 096 p.**, valeur postérieure à la refonte du
31 juillet et **indûment reversée dans un constat daté du 29** — la passe du 4 août l'avait classée
parmi les deux occurrences « à laisser telles quelles », à tort)* **/ 50 chapitres /
159 entrées de socle**, et les **quatre contrôles du Vol. IV en sortie 0** — `check-toc.py`,
`check-sieges.py` (**26 sièges sur 50 pièces**), `check-compendium.py` (**P1-P8**, trois rapports
déclaratifs), `decompte.sh`. ⚠ **Ce que la passe ne fait pas** : elle **ne requalifie aucun statut** —
le Vol. III reste non publiable, le Vol. IV **arrêté et non publiable** —, **ne touche à aucune pièce
rédigée**, **ne corrige pas la veille** et **ne referme aucune remontée**. *Resynchroniser des
porteurs de décomptes n'avance aucune porte.*

**Le 4 août 2026** — passe documentaire — ce `README.md` et le
[conspectus du Vol. IV](2%20-%20Compendium/README.md) ont été resynchronisés sur le dépôt de
[`Compendium.html`](2%20-%20Compendium/Compendium.html), **appareil de lecture à l'écran** du
compendium : déposé le même jour sous le nom `presentation.html` (commit `76d001c`), révisé deux
fois, puis renommé (commit `d473913`). **Ce que la passe enregistre** : un fichier de **1,75 Mio**
(1 829 940 octets — *la passe avait écrit 1,79 Mio, conversion fausse de son propre décompte d'octets*),
**sans dépendance externe** et à **un seul lien sortant** — vers le PDF —, **118 figures SVG
embarquées** en `data:` (relevé sur pièce : 118 occurrences, autant que le rendu imprimé en porte),
douze entrées de sommaire, et une **horloge calculée à l'ouverture**. **Ce que la passe refuse de
laisser croire, et c'est le fond de l'entrée** : ⚠ **cette page ne se régénère pas.** Le balayage de
[`2 - Compendium/build/`](2%20-%20Compendium/build/) ne trouve **aucun générateur HTML** — les cinq
chaînes du dépôt ne produisent que des PDF —, si bien que `Compendium.html`, comme les **cinquante
pages de chapitre** déposées avant elle, est **écrite à la main et relevée à la main**. *La règle du
« rendu versionné avec sa source » ne s'y applique donc pas, et rien ne signale qu'elle a pris du
retard.* ⚠ **Elle ne requalifie rien** : dérivée, sans autorité — son colophon le déclare —, **non
publiée**, et tenue par le régime de **D-10** comme l'est le PDF.

**Trois défauts trouvés dans la passe, tous par ouverture de la pièce, aucun corrigé ici.** *(1)* ⚠
**Le décompte de pages du compendium est faux à ce `README.md`** : `pypdf` mesure **1 114 pages**
sur le PDF versionné, quand ce fichier en annonce **1 096** — le conspectus du volume et le colophon
de `Compendium.html`, eux, portent le bon chiffre. Le motif compte **sept occurrences**, mais elles
ne sont pas du même régime : **cinq annoncent un état courant** (encadré d'entrée, tableau d'état,
section du Vol. IV, arborescence, commentaire de la commande de rendu) et sont **fausses** ; **deux
sont des constats datés** des passes du 29 juillet, et *un constat daté ne retarde pas, il
enregistre.* La correction porte donc sur **cinq lignes**, et elle se demande. *(2)* ⚠ **Trois liens de ces `README.md` ne pointent sur
rien** — `audit.md`, `audit-references.md` et `eval.html` sont cités par la racine, le conspectus,
le `PRD.md`, le `TOC.md` et le ch. 4, et **ils ne sont ni sur le disque ni au suivi git**. *Un renvoi
vers un fichier absent, aucun des quatre contrôles du volume ne le voit.* *(3)* Le PDF s'appelle
`Compendium.pdf` sur le disque et `compendium.pdf` à l'index git, que `core.ignorecase` rend aveugle
à l'écart : les liens résolvent — ils visent le nom indexé —, mais **le premier dépôt fait sur un
système sensible à la casse produira un renommage fantôme**. **Décomptes re-mesurés sur pièce à
cette date** : `Compendium.html` **1 829 940 octets / 118 figures embarquées** ; `compendium.pdf`
**1 114 p.** (`pypdf`) ; **12 `README.md`** au suivi git, cardinal inchangé depuis le 29 juillet —
**deux d'entre eux sont touchés par la passe**, la racine et le conspectus du Vol. IV. ⚠ **Ce que la
passe ne fait pas** : elle **ne touche à aucune pièce
rédigée**, **ne franchit aucune porte**, **ne corrige aucun des trois défauts** et **ne publie rien**.

⚠ Le décompte des diagrammes du Vol. I se mesure avec un motif **ancré** :
`grep -c '^```mermaid'` donne 28. Le motif non ancré en retourne 29 — il attrape une ligne de prose
de la note de production qui cite la balise.

**Le 8 août 2026** — passe d'audit et de correction — les **197 fichiers `.md` du dépôt et le
compendium entier** ont été audités, et **les correctifs ont été appliqués**, non seulement signalés.
C'est ce qui distingue cette passe des précédentes : *les trois défauts que la passe du 4 août avait
trouvés sans les corriger sont refermés ici*, et le tableau des reliquats a été récrit sur mesure
plutôt que reconduit. Chaque chiffre ci-dessous a été **re-mesuré sur la pièce**, par un bâtisseur puis
par un critique en contexte neuf qui ne connaissait pas son travail.

**Ce que la passe a corrigé.**

- ⚠ **La pagination du compendium était fausse partout où elle s'annonçait au présent** : **1 114 p.**
  mesurées, contre **1 096** à ce fichier (cinq annonces) et **810** à six autres — le tableau d'état,
  le paragraphe des régimes de la veille, `1 - Corpus/README.md` et les cinq `Livre */README.md`.
  ⚠ *Deux constats datés du 29 juillet portant 847 et 863 pages sont laissés tels quels : un constat
  daté enregistre, il ne retarde pas.*
- ⚠ **La gouvernance du Vol. IV avait neuf jours de retard, et c'est le plus gros écart de la passe** :
  ce fichier annonçait l'ouvrage **arrêté** sous **D-10 / PRD v0.15 / TOC v0.31**, alors que **D-11
  a rouvert cet arrêt le 30 juillet 2026** (**PRD v0.16 §15, TOC v0.32**) sur un rapport d'arbitrage
  externe. *Une estampille d'autorité courante en retard ne se rattrape pas par une note : elle est
  fausse.* Corrigée en cinq endroits, et la réouverture est désormais exposée.
- **L'écart de casse du PDF est refermé aux deux bouts** : l'index git est normalisé sur le disque
  (`compendium.pdf` → **`Compendium.pdf`**) et **`build/build-pdf.sh` écrit désormais le nom
  canonique**. ⚠ *Le second geste était indispensable au premier* : le script composait en minuscule,
  si bien que la première recomposition après le renommage aurait produit un **second fichier** au lieu
  de remplacer le rendu versionné. Trente et quelques renvois repointés, dont deux `href` de
  `Compendium.html` — GitHub est sensible à la casse.
- **Renvois internes morts : 151 → 6** (hors produit d'assemblage), sur 1 641 liens relatifs balayés.
  Les **48 renvois du `monographie/` du Vol. II** sont repointés vers `prd/`, les **17 locateurs
  `fichier.md:ligne`** de son `audit.md` convertis en ancres `#L21` — *préfixer `../` ne suffisait pas,
  le suffixe invalidant le chemin* —, et les renvois vers les fichiers **supprimés délibérément**
  (`audit.md`, `audit-references.md`, `eval.html`, six `CLAUDE.md`, les scripts de `.claude/skills/`)
  sont retirés en conservant les noms et en datant le retrait.
- **L'assemblage du Vol. II est remis en service** — le script cherchait `TOC.md` à la racine du volume
  quand il vit dans `prd/`. ⚠ **Et la reprise a trouvé mieux que la panne annoncée** : les deux
  assembleurs ne rebasaient pas les cibles relatives des pièces, si bien que le **Vol. III portait le
  même défaut sans que rien ne le signale** — *le témoin réputé sain était malade de la même chose.*
  Les deux scripts sont corrigés et les deux `Monographie.md` régénérés ; contrôle préalable : chaque
  assembleur reproduit sa sortie versionnée **à l'octet près**.
- ⚠ **L'Annexe I n'était pas « à écrire » : elle existe depuis le 30 juillet 2026** —
  `annexe-bibliographie.md`, **1 154 entrées uniques**. Quatre documents la déclaraient manquante.
- **La veille : « vingt-deux questions ouvertes » contre vingt-cinq**, et le contredit venait de son
  propre appareil de contrôle — `check-veille.py` compte **25**, comme le tableau d'état du même
  fichier. *Un décompte faux à côté du contrôle qui le dément est le défaut le moins excusable du lot.*
- ⚠ **Le Vol. I annonçait ≈ 263 600 mots, qu'aucune commande du dépôt ne produit** : **233 257**
  (`wc -w`, point d'ancrage de `decompte.sh --verifier`) ou 225 258 (commande de référence). ⚠ **La
  correction a une conséquence que le corpus ne s'attendait pas à payer** : son agrégat tombe sous les
  ≈ 516 500 annoncés — **486 206 mots** en sommant les trois chiffres publiés, *chacun pris par la
  méthode propre de son volume* (233 257 + 92 059 + 160 890 : trois commandes différentes, et la somme
  le déclare) — ⚠ **486 203 depuis la re-mesure du 10 août 2026**, le Vol. II tombant à 92 056 —, ou
  **479 390** par la **commande unique** de `decompte.sh --verifier`. *Les deux mesures
  sont sous le seuil des 500 000 que le corpus s'attribuait, et il le perd dans les deux cas.*
- **Deux erreurs d'unité, mêmes octets mal convertis** : la passe du 4 août avait écrit **1,79 Mio**
  pour `Compendium.html` là où ses propres 1 829 940 octets en font **1,75** ; et le colophon du volume
  donnait « 12,7 Mo » pour le PDF là où 13 304 911 octets font **12,7 Mio** — 13,3 Mo. ⚠ **Le premier
  correctif a lui-même été repris par le juge de cette passe** : reporter 1,75 Mio au présent était
  faux, le fichier ayant changé depuis ; il pèse **1 826 464 octets, soit 1,74 Mio**, en fins de ligne
  `LF` pures. *Une conversion juste sur un décompte périmé reste un chiffre faux.*
- **Le registre de gel du Vol. IV** portait un total de Livre I faux de 3 903 mots (**71 980**, non
  68 077) et, par propagation, un agrégat et sept écarts en pourcentage faux.
- ⚠ **La couverture des figures était annoncée complète et ne l'est pas** : le conspectus et
  `Compendium.html` affirmaient que « les cinquante chapitres en portent au moins une ». Balayage des
  cinquante pièces : **quarante-neuf**. Le **ch. 28** n'en porte aucune, et le programme des figures dit
  pourquoi — il ne lui accordait que **deux candidates, toutes deux au barème B**, qu'une passe de
  barème A ne pouvait pas couvrir. *Le décompte de 118 figures est juste ; c'est la couverture qui ne
  l'était pas.*
- ⚠ **Le colophon attestait la non-blancheur d'un rendu qu'il n'avait plus** : « 0 sur **1 072**
  mesurées », sans date, deux lignes sous « 1 114 pages ». Le relevé est du **30 juillet 2026**, pris
  sur le rendu d'alors ; la refonte au format Letter du 31 juillet a porté l'ouvrage à 1 114 pages, et
  *l'attestation ne couvre pas les quarante-deux dernières.* Datée et bornée, non refaite.

**Ce que la passe a refusé de faire, et pourquoi.** Elle **ne requalifie aucun statut** — le Vol. III
reste non publiable, le Vol. IV en passe de révision ouverte —, **ne franchit aucune porte**,
**ne corrige pas la veille**, **ne referme aucune remontée** et **ne publie rien**. ⚠ **Elle laisse
aussi les constats datés qui divergent de la mesure d'aujourd'hui** : le PRD du Vol. IV crédite `P3` de
670 et `P5` de 9 là où le contrôle en mesure 674 et 12, mais ses deux tables se déclarent « constats
d'exécution du 29 juillet 2026 ». *Corriger un constat daté, c'est effacer la seule chose qu'il
apporte.*

☑ **Le rendu a été recomposé avec sa source, et c'est un critique qui l'a exigé.** La passe avait
corrigé la prose des deux annexes **reliées** dans `Compendium.pdf` sans recomposer le livre — si bien
que le PDF versionné, identique à l'octet près à son état d'avant la passe, imprimait encore page 977
« l'Annexe I […] reste à écrire », **114 pages avant cette même Annexe I reliée dans le même fichier**.
C'est la violation littérale de la règle permanente énoncée plus haut — *régénérer et versionner le PDF
avec sa source, jamais la source seule* — et c'est **la classe d'écart qu'aucun des cinq contrôles ne
voit** : ils lisent les `.md`, rien ne compare le rendu à sa source. **Recomposé le 8 août 2026** par
`bash build/build-pdf.sh` : **1 114 pages, décompte inchangé**, 50 chapitres + 2 annexes + 23 renvois
marqués, et `pdftotext` confirme — « reste à écrire » : zéro occurrence ; « 1 154 entrées uniques » :
une.

⚠ **Une entorse à sa propre règle, déclarée plutôt que défaite.** La passe s'était interdit de toucher
à la **prose** d'une pièce rédigée, et un critique en contexte neuf a relevé qu'elle l'avait fait à
**deux annexes** du Vol. IV : `annexe-references.md` déclarait l'**Annexe I « reste à écrire »** — un
énoncé faux depuis le 30 juillet 2026 —, et `annexe-bibliographie.md` renvoyait au rapport
`audit-references.md` comme s'il était au dépôt. Les deux énoncés sont redressés, et **les cinquante
chapitres, eux, n'ont changé que par la cible de leurs liens** — deux fichiers, une ligne chacune, texte
visible identique. ⚠ *Le motif de l'exception est étroit et il ne s'étend pas* : une annexe qui se
trompe sur le **contenu de son propre volume** n'énonce pas un fait daté, elle induit en erreur sur
l'état présent du dépôt — ce qu'un audit ne peut pas laisser passer sans se contredire.

⚠ **Deux corrections de méthode, dont une contre cette passe elle-même.** *(1)* `pypdf`, que cinq
documents donnent pour instrument de pagination, **n'est pas installé** : les décomptes de cette passe
sont pris par lecture du `/Count` de l'objet `/Type /Pages`, et c'est cela qui est écrit. *(2)* ⚠ **La
passe a d'abord publié une mise en garde fausse contre un motif de comptage, et un critique l'a
reprise en réexécutant la commande — c'est le défaut le plus instructif du lot.** Trois choses en une
phrase, toutes vérifiées sur les cinq PDF du dépôt : le motif `/Type /Page` **avec l'espace rend 0**,
Typst écrivant `/Type/Page` sans espace ; le décompte doublé que la passe avait obtenu (2 228 pour
1 114) venait d'une **classe d'exclusion trop étroite** — elle écartait `/Type/Pages` mais laissait
passer `/Type/PageLabel`, dont il existe **un objet par page** ; et un motif correctement ancré rend
la pagination juste du premier coup — `grep -aoP '/Type/Page(?![sL])' | wc -l` donne **569, 387, 427,
1 114 et 161**. *Une commande de contrôle publiée sans avoir été réexécutée sur son domaine entier est
un instrument qui ment avec l'autorité d'une mesure* — et c'est précisément la classe de défaut que ce
dépôt prend pour objet. *(La même réserve vaut pour le décompte des diagrammes du Vol. I ; elle est
écrite une fois, à l'entrée du 4 août 2026 ci-dessus, et ne se répète pas ici.)*

**Le 8 août 2026, seconde passe du même jour — LA PASSE DE CLÔTURE.** Sur instruction d'auteur, le
dépôt est **clos et final**. *C'est la dernière entrée de ce journal, et elle décrit un état qui ne
bougera plus.*

**Trois gestes de gouvernance, et rien d'autre.** *(1)* **La décision d'auteur `D-13` est prise**
(PRD **v0.17** §16, TOC **v0.33**) : la passe de révision ouverte par `D-11` le 30 juillet 2026 est
**close sans exécution de son domaine résiduel**, et le dépôt entier est clos. Le §16.2 du PRD nomme
**ligne à ligne** ce qui ne sera pas fait — relecture tierce, élévation hors **[C]**, les **261
tournures indéfinies** de 44 pièces, la date AMF, le ch. 46, les **674 emplois de socle nus**.
*(2)* **La `décision 20` du TOC renomme le Vol. IV** : *« La somme agentique »* devient
**« Interopérabilité et Orchestration Agentiques en Entreprise »**, et le sous-titre perd son premier
terme, que le titre porte désormais. *(3)* **La `décision 19` pose la seule règle de lecture qui suive
d'une clôture** : *un manque définitif ne devient jamais une conformité.*

**Ce que la passe a touché, et pourquoi.** Le renommage est un **identifiant, non un fait daté** —
c'est le motif pour lequel il se propage là où un fait daté ne se propagerait pas. **55 fichiers** le
portent : les **50 pages de chapitre** et [`Compendium.html`](2%20-%20Compendium/Compendium.html), les
**trois gabarits Typst**, `check-toc.py`, et les documents de gouvernance. ⚠ **Deux conséquences
mesurées, et aucune n'était prévisible depuis la source.** *(a)* **Le titre a dû passer de 52 pt à
34 pt** sur la page de titre : à 52 pt, « Interopérabilité » **seul** déborde des 148 mm de la page, et
*Typst ne le signale pas*. Vérifié sur le rendu : page de titre **unique**, **1 114 pages inchangées**,
zéro occurrence de l'ancien titre (`pdftotext`). *(b)* ⚠ **La veille technologique passe de 161 à
162 pages** : la mention du titre d'alors, portée à ses références **[220]** et **[266]**, a poussé la
bibliographie d'une page. *Le rattrapage de la veille est une **exception nommée** à la règle du dépôt
— elle vaut pour un identifiant, jamais pour un fait daté, et aucun énoncé factuel de la veille n'est
touché.*

**Ce que la passe a purgé.** `2 - Compendium/build/compendium-assemble.md` — **2,7 Mio** de produit
d'assemblage périmé, que `build-pdf.sh` n'utilise pas (il écrit dans un répertoire temporaire) et qui
portait à lui seul **123 des renvois morts** du dépôt ; les **cinq répertoires `__pycache__`** du
disque, non suivis. **Trois documents de travail ont été retirés par l'auteur dans la même passe** :
`gauntlet-log.md` (journal de la boucle d'audit du 8 août) et les deux rapports d'**évaluation
académique** du même jour — ⚠ *aucun n'était cité par un document du dépôt, et le seul suivi par git
se lit à l'historique.*

**Deux décisions d'auteur en attente depuis le 18 juillet sont tranchées** : l'étiquette git
**`mono-v1.0` est posée** au commit de clôture (⚠ *elle marque l'arbre clos, non celui du 17 juillet
qu'elle nomme*), et **aucune licence n'est déposée** — droit d'auteur par défaut, **tous droits
réservés**. Détail au tableau ci-dessous.

**Contrôles rejoués à la clôture, tous en sortie 0** : `check-veille.py`, `check-toc.py` (C1-C15),
`check-sieges.py` (S1-S5), `check-compendium.py` (P1-P8), `bash decompte.sh --verifier`. **Renvois
internes re-balayés** : **1 667 liens relatifs, 6 morts** — les six connus et documentés au tableau
ci-dessous (cinq citations verbatim d'un rapport de lot, un faux positif dans un bloc clôturé), et
*la purge du produit d'assemblage a retiré les 123 autres.* ⚠ **Cette mesure reste externe à
l'appareil** : *aucun des cinq contrôles ne résout un seul lien markdown*, et rien ne la rejouera.
⚠ **Ce que la passe ne fait pas** : elle **ne franchit aucune porte**, **ne lève aucune dérogation**,
**ne referme aucune remontée**, **ne touche à la prose d'aucune des cinquante pièces rédigées** — leur
en-tête déclare « brouillon non publiable », *énoncé que la clôture confirme plutôt qu'elle ne le
périme* — et **ne publie rien**.

**Reliquats DÉFINITIFS à la clôture** — re-mesurés le 8 août 2026. ⚠ **Ce tableau ne liste plus des
dettes suivies : il liste ce qui restera en l'état.** Deux lignes ont été tranchées par la clôture et
portent leur issue ; les autres sont des contradictions non arbitrées, ou des renvois dont la
correction exigerait une information que le dépôt ne porte pas — *et personne ne l'apportera.*

| Fichier | Reliquat |
|---|---|
| racine du dépôt | ☑ **TRANCHÉ le 8 août 2026 — aucune licence, et c'est le régime choisi** : **droit d'auteur par défaut, tous droits réservés**. Seul le Vol. I porte un `LICENSE` propre, qui ne vaut que pour lui. ⚠ *Le motif est de cohérence, non d'omission* : le volume terminal du dépôt exclut toute mise à disposition d'un tiers, et une licence ouverte à la racine contredirait le régime que quatre documents de gouvernance déclarent |
| `1 - Corpus/2 - OrchestrationAgentique/` | ☑ **TRANCHÉ le 8 août 2026 — l'étiquette git `mono-v1.0` est posée**, au commit de clôture. ⚠ **Elle ne rend pas vraies les vingt mentions qui l'annonçaient** : **trois documents de gouvernance** (`PRD.md`, `PRDPlan.md`, `audit.md`) **et dix-sept pièces** la donnent pour posée depuis le 17 juillet 2026, dont l'une écrit « `mono-v1.0` existe » — *l'étiquette marque l'arbre clos du 8 août, non celui du 17 juillet, et `git show mono-v1.0` le montre.* Les deux `README.md` du volume portent le correctif ; la prose des vingt mentions **n'a pas été réécrite, et ne le sera pas** |
| `1 - Corpus/1 - InteroperabiliteAgentique/Chapitres/TOC.md` | l'Annexe B y est déclarée **≈ 17 500 mots** quand `wc -w` en mesure **20 655** (+18 %). La colonne « Méthode » dit honnêtement « décompte **déclaré** en tête d'ADS », mais l'en-tête du même fichier revendique que tout décompte est **relevé, non projeté** — **contradiction interne à arbitrer** |
| `1 - Corpus/2 - OrchestrationAgentique/` | **trois volumétries concurrentes, toutes justes sous leur méthode** : **92 056** (PRDPlan §4.2, locale C — chiffre publié ; 92 059 au 17 juillet 2026), **93 239** (`decompte.sh`, locale UTF-8, où l'espace insécable sépare ; 93 242 à sa valeur d'ancrage), 90 362 (clôture de P4, datée). Le §4.2 documente lui-même son sous-comptage de 1,3 % et **refuse** de le corriger : aucune n'est fausse, et le choix est éditorial. ⚠ **Les deux premières ont perdu les mêmes trois jetons au commit `659241b`** — ils sont dans le **corps** des pièces, que les deux commandes mesurent : *l'écart entre les deux méthodes est d'assiette de jetons, pas d'assiette de texte* |
| `2 - Compendium/` — volumétries des cinq `Livre */README.md` et colonne `Réel` du registre de gel | périmées de quatre passes de révision du français (31 juillet → 3 août 2026). ⚠ **Non corrigées pour une raison de contrôle, non de paresse** : la colonne est **opposée par `check-compendium.py` P6 aux en-têtes des cinquante pièces**, qui sont de la prose gelée — la corriger d'un seul côté ferait échouer P6 sur 26 lignes. La mesure courante (**331 791 mots**) est écrite au registre avec ce motif |
| `2 - Compendium/Compendium.html` + les 50 `.html` de chapitre | **aucune chaîne ne les régénère** : `build/` ne porte pas de générateur HTML, ces pages sont écrites et relevées à la main. La règle du « rendu versionné avec sa source » ne s'y applique pas — *le retard sur le `.md` ne se signale nulle part* |
| `2 - Compendium/Livre */README.md` | leurs blocs de procédure invoquent `rendre-piece.py` et `verifier-piece.py`, **scripts d'un skill supprimé le 31 juillet 2026** (commit `41666d0`). Le retrait est désormais déclaré à chaque fichier, mais les commandes sont laissées telles quelles : **le dépôt ne dit pas par quoi elles ont été remplacées** |
| racine du dépôt et `2 - Compendium/build/` — `gauntlet-log.md`, les deux rapports d'**évaluation académique** du 8 août 2026, `compendium-assemble.md` | **purgés à la clôture du 8 août 2026.** Les trois premiers sont des documents de travail qu'**aucun fichier du dépôt ne citait** ; `gauntlet-log.md` était suivi par git et se relit à l'historique, les deux rapports ne l'étaient pas et **ne se relisent nulle part**. `compendium-assemble.md` était un **produit d'assemblage périmé de 2,7 Mio** que la chaîne n'utilise pas — il portait **123 des renvois morts** du dépôt à lui seul. ⚠ *Purger un produit dérivé est sans conséquence ; purger un journal non suivi est irréversible, et c'est écrit ici plutôt que constaté plus tard*. ⚠ **DÉPASSÉ DEUX FOIS POUR LA MÊME LIGNE, ET REVENU À SON ÉTAT INITIAL** : `gauntlet-log.md` **est revenu à l'arbre le 8 août 2026**, redéposé par la passe de veille, a reçu deux blocs de plus depuis (revue de littérature, 9 août ; audit du traité, 10 août), puis **a été purgé de nouveau le 10 août 2026** — *la ligne redit donc vrai, par un aller-retour et non par une constance.* Le journal ne racontait que les boucles bâtisseur/critique de la veille, de la revue et du traité — il ne couvre ni les quatre volumes, ni le calage du compendium à mille pages. Les deux rapports d'évaluation et `compendium-assemble.md` n'ont, eux, jamais reparu |
| `2 - Compendium/` — `audit.md`, `audit-references.md`, `eval.html`, six `CLAUDE.md`, `.claude/skills/` | **supprimés délibérément** (`f6183bf`, `73e7c4e`, `982ef3a`, `41666d0`), et non perdus : ils se lisent à l'historique git. Les renvois qui les visaient sont retirés, le retrait daté. ⚠ *Le rapport d'arbitrage `eval.html` qui a déclenché **D-11** est dans ce lot : la décision est opposable, la pièce qui la motive ne se lit plus qu'au journal* |
| `1 - Corpus/3 - EntrepriseAgentique/verification/` — les **30 rapports** | ☑ **SANS OBJET depuis le 8 août 2026, et pas parce qu'il a été soldé** : le répertoire entier a été **supprimé** (commit `659241b`), les cinq renvois morts de `lot-L-04-…md` avec lui. ⚠ *Ils étaient conservés à dessein — liens internes de pages tierces reproduits verbatim dans des blockquotes de preuve, que les réécrire aurait altérés ; ils disparaissent avec la preuve qu'ils citaient.* Ce que la suppression emporte vraiment : `remontees-gouvernance.md`, **le registre des quinze remontées R-G-43 à R-G-57**, et les 30 rapports que quatre `README.md` donnaient encore pour présents. **La dette reste, l'inventaire part** ; tout se relit à l'historique git. ⚠⚠ **ET ELLE EMPORTE PLUS QUE CE QUE LA CLÔTURE A COMPTÉ — mesuré le 9 août 2026 sur les 168 `.md` du dépôt** : **152 renvois relatifs meurent avec le répertoire**, visant **20 rapports distincts** depuis **34 fichiers** — 88 aux pièces de `monographie/`, 52 à `prd/`, 11 au `Monographie.md` assemblé, et **un au socle consolidé du Vol. IV**. *La passe de clôture annonçait « 1 667 liens relatifs, 6 morts » et celle du 8 août au soir « quatre renvois morts, tous dans le `README.md` du Vol. III » : les deux mesures ont été prises **avant** le balayage complet d'après suppression, et elles sous-estiment de deux ordres de grandeur.* ⚠ **Rien n'est réécrit, et c'est délibéré** : ces renvois citent des rapports **par leur nom, à l'appui d'une preuve**, dans des pièces gelées d'un volume clos — *les réécrire altérerait la citation, les retirer effacerait la trace de ce qui a été vérifié.* **Constat porté ici, correction non faite, et personne ne la fera** |
| `1 - Corpus/3 - EntrepriseAgentique/prd/PRDPlan.md` | un sixième renvoi « mort » est un **faux positif** : le chemin vit dans un bloc `sh` clôturé, c'est le **gabarit d'en-tête de pièce**, correct à la profondeur de sa destination. Y toucher casserait le gabarit |
| Vol. I et Vol. III — `Chapitres/TOC.md`, `monographie/`, `prd/` *(et `verification/`, avant sa suppression)* | citent `Borealis-Go` et `Synthese Monographie.md`, retirés du dépôt les 25 et 22 juillet 2026 : **citations exactes, plus opposables**, à consigner et non à réécrire. Le tableau des livrables du Vol. I porte désormais ce régime en clair |
| `1 - Corpus/0 - Références/` | **trois PDF déposés le 8 août 2026** (commit `659241b`, **32,5 Mio**) : *Mémoire de maîtrise* 1997, *Enterprise Integration Patterns* 2003, *Distributed Systems* 2007. ⚠ **Aucun document du dépôt ne les cite, aucune entrée de socle ne s'y adosse, le répertoire ne porte pas de `README.md`** — leur statut n'est écrit nulle part. *Une pièce déposée sans régime déclaré n'est pas une source : c'est un fichier.* **Régime à écrire, et personne ne l'écrira** |
| `2 - Compendium/PRD/decompte.sh` | ⚠ **sa valeur d'ancrage du Vol. II est périmée d'un renommage** : il attend **93 242** mots, l'arbre courant en mesure **93 239** depuis que le commit `659241b` a récrit trois phrases de trois pièces de `monographie/`. **Le contrôle sort donc 1**, et la clôture le donne encore en sortie 0 — *constat daté du matin, faux dès l'après-midi.* Le corriger supposerait de trancher entre remettre la valeur d'ancrage à jour et rendre au Vol. II les trois mots perdus : **arbitrage d'auteur, non de resynchronisation** |
| `2 - Compendium/Compendium.html`, section « index » | trois entrées d'index publient des **totaux d'occurrences qui ne se reproduisent pas** (« niveau de preuve » 921, « péremption » 399, « registre de gel » 70) : les **cardinaux de chapitres se reproduisent**, les totaux non — aucun motif unique ne rend les deux à la fois, et la règle de comptage n'est écrite nulle part. Les **56 notions**, elles, sont exactes. Page écrite à la main : requalifier ces totaux exigerait la règle d'origine, que le dépôt ne porte pas |
| l'appareil de contrôle entier | **aucun des sept contrôles ne résout un seul lien markdown** *(cinq jusqu'au 9 août 2026 ; `check-resume.py` et `check-revue.py` s'y ajoutent sans rien y changer)* : leurs appels à `exists()` gardent des entrées de script, jamais une cible de renvoi. L'état « zéro lien mort » ne tient que par une mesure externe que rien ne rejoue — et pour l'appareil, **retirer un renvoi est indistinguable de réparer sa cible**. ⚠ **La démonstration a eu lieu, et elle est datée** : la suppression de `verification/` le 8 août 2026 a laissé **152 renvois morts** que personne n'a vus pendant vingt-quatre heures, deux passes de resynchronisation ayant publié « 6 morts » puis « quatre » entre-temps. *Un état déclaré par une mesure qu'aucun contrôle ne rejoue est une hypothèse, pas un fait* |
| `2 - Compendium/` | le compendium **n'a toujours aucune URL** : son Annexe I réunit les bibliographies des sources sans en vérifier une seule, et *une entrée présente n'y atteste de rien* |

⚠ **Aucune publication GitHub Pages, pour aucun volume.** ⚠ **La formule antérieure — « plus de
pages de présentation » — a cessé d'être exacte le 4 août 2026** et elle est corrigée ici : le
Vol. IV en porte désormais, [`Compendium.html`](2%20-%20Compendium/Compendium.html) et les cinquante
pages de chapitre. *Ce qui a disparu n'est pas la page de présentation, c'est sa publication en
ligne* — les nouvelles ne sont **pas publiées** et se lisent depuis le dépôt, en local. Les deux
`index.html` (Vol. I et Vol. II) ont été supprimés le 22 juillet 2026 (commit `fd8f1be`). Ils
annonçaient « Lire en ligne » sous `https://agbruneau.github.io/Monographies/…`, et leurs balises
`canonical`, `og:url` et liens « Dépôt GitHub » nommaient tous `Monographies` — adresses fausses de
toute façon, le dépôt s'appelant `Agentique` (`github.com/agbruneau/Agentique`), et cause des 404
relevés. Rétablir une publication en ligne supposerait de repartir de la bonne base
(`https://agbruneau.github.io/Agentique/`) et de vérifier que Pages est bien activé pour ce dépôt.

**Le 8 août 2026, troisième passe du même jour — resynchronisation des `README.md` sur l'arbre
d'après la clôture.** ⚠ *L'entrée précédente se déclarait « la dernière de ce journal » ; deux commits
l'ont suivie, et c'est pour cela que celle-ci existe.* La passe porte sur les **douze `README.md` du
dépôt** et **sur eux seuls** : aucune pièce rédigée, aucun document de gouvernance, aucun rendu n'est
touché.

**Ce que la relecture a trouvé, et corrigé.**

- ⚠ **Le commit `659241b` n'était enregistré que pour son renommage, et il portait deux gestes de
  fond de plus** : le dépôt du corpus [`1 - Corpus/0 - Références/`](1%20-%20Corpus/0%20-%20R%C3%A9f%C3%A9rences/)
  (trois PDF, **32,5 Mio**, cités par rien) et la **suppression intégrale de
  `1 - Corpus/3 - EntrepriseAgentique/verification/`** — **30 rapports**, dont le registre des quinze
  remontées ouvertes. *Un commit qui dépose un corpus et en supprime un autre reprend le travail ; le
  décrire comme un renommage est une description fausse, pas une description partielle.*
- ⚠ **`decompte.sh --verifier` sort 1, et la clôture le donne en sortie 0** — Vol. II mesuré à
  **93 239** mots contre **93 242** attendus, agrégat à **479 387** contre 479 390. *La cause est le
  renommage : dans trois pièces de `monographie/`, les formules qui appelaient l'autonomie encadrée
  le titre de l'ouvrage disent désormais sa thèse, et trois jetons sont tombés.* Le renommage se
  donnait pour un identifiant sans conséquence de fait ; il a coûté trois mots à un décompte
  opposable.
- **Quatre renvois morts, tous dans le `README.md` du Vol. III**, vers des rapports du
  `verification/` supprimé ; **le décompte de « 30 rapports » traînait à quatre fichiers**. Corrigés
  aux quatre.
- ⚠ **Le poids de `Compendium.html` était donné « sur disque » et ne l'était pas** : **1 831 155
  octets** est la mesure du **fichier versionné**, en `LF` ; le dépôt ne portant pas de
  `.gitattributes`, un poste en `core.autocrlf=true` obtient **1 835 118 octets** en `CRLF`.
  *Une conversion juste sur le mauvais objet reste un chiffre faux.*

**Ce que la passe a re-mesuré sur pièce, et qui tient — toutes valeurs inchangées.** ⚠ *Constat daté
du 8 août 2026, matin : ses trois valeurs relatives à la veille — 162 p., 269 références et
15 tableaux — ont été **périmées le même jour** par la passe de refonte (100 p., 303 références,
18 tableaux). Le constat n'est pas
corrigé, parce qu'un constat daté vaut à sa date ; c'est le tableau d'état, plus haut, qui porte
l'autorité courante.* Pagination par
`grep -aoP '/Type/Page(?![sL])'` : **162, 569, 387, 427 et 1 114 p.** ; Vol. I **28 diagrammes**
(motif ancré) et **233 257 mots** (`wc -w`) ; **50 chapitres**, **118 figures SVG** et **118 SVG
embarqués** au Vol. IV ; socle **159 entrées**, Annexe I **1 154 entrées** ; veille **269 références,
25 questions ouvertes, 15 tableaux** (`check-veille.py`, sortie 0) ; `check-toc.py`, `check-sieges.py`
(**26 sièges / 50 pièces**) et `check-compendium.py` (**P1-P8**) en sortie 0 ; **12 `README.md`** au
suivi git.

⚠ **Ce que la passe ne fait pas.** Elle **ne rouvre pas la clôture** — resynchroniser un porteur de
décompte n'est pas reprendre le travail —, **ne franchit aucune porte**, **ne referme aucune
remontée**, **ne restaure aucun fichier supprimé**, **ne corrige ni `decompte.sh` ni le corps du
Vol. II** (l'écart de trois mots est un arbitrage d'auteur), **ne dote `0 - Références/` d'aucun
régime** et **ne publie rien**. ⚠ *Elle laisse intacts les constats datés qui divergent de la mesure
d'aujourd'hui* — « tous les contrôles en sortie 0 », 847 et 863 pages, 479 390 mots : *un constat daté
enregistre ce qu'une passe a lu ; le corriger effacerait la seule chose qu'il apporte.*


**Le 8 août 2026, seconde passe du même jour — actualisation de la veille et refonte de son format.**
⚠ **Cette passe rouvre la clôture pour le seul livrable qu'elle touche**, et la déclaration est
portée en tête de fichier. Elle procède de deux gestes distincts, conduits dans cet ordre.

*(a) Actualisation, au régime fort demandé par l'auteur.* Une passe de veille sur la fenêtre du
**29 juillet au 8 août 2026** (six agents, un par grappe thématique — corpus protocolaire,
réglementation, identité et sécurité, couche transactionnelle et sémantique, adoption et analystes,
exploitation et orchestration), à consigne de **source primaire exclusive**, doublée d'un **audit
d'authenticité de l'intégralité des références** — neuf agents rouvrant une à une les **269 entrées**
de la bibliographie antérieure sur leur source primaire. **Verdicts : 179 confirmées, 54 corrigées,
30 non reconfirmables, 6 auto-citations, aucune introuvable.** ⚠ *Seize de ces trente non-reconfirmables
tiennent à un refus de consultation automatisée — organismes de normalisation, cabinets d'analyse,
régulateurs, tous en HTTP 403 — et les quatorze autres à des pages sans date, mouvantes ou rendues en
script : ce n'est pas la source qui manque, c'est l'accès.* L'audit a
notamment établi qu'une référence pointait vers une page traitant du **secteur public** là où le
texte citait une disposition du **secteur privé**, et qu'un communiqué d'éditeur s'était vu prêter
deux faits venus d'un communiqué postérieur d'un an. ⚠ **Aucune ronde de vérification adverse à
plusieurs votants n'a été conduite** : le régime est celui, plus faible, déjà déclaré pour la
sous-section 12.4 — et il est déclaré comme tel en §2.2 et en §10 de la veille.

*(b) Réduction à cent pages fermes, par compression éditoriale seule.* **Gabarit inchangé** — 11 pt,
marges inchangées, aucun gain typographique. Le corps est passé de **70 552 à 29 211 mots**, soit
**−59 %**, à faits constants ; l'appareil (page de titre, résumé, bibliographie) pèse **32 des
100 pages**, la bibliographie ayant elle-même grossi de 269 à 303 entrées. La compression a été conduite morceau par morceau, chaque morceau étant ensuite
**comparé à l'aveugle** à la version de 162 pages par un juge à contexte neuf ne sachant pas lequel
des deux textes était lequel, l'ordre de présentation alternant d'un morceau à l'autre. **Les quatre
morceaux soumis au jugement ont été préférés à la version longue**, sur des motifs portant chaque
fois sur la densité de fait vérifié et la netteté du statut épistémique. Deux écarts relevés par les
juges ont été corrigés dans la foulée — trois légendes de tableau qui dataient d'une passe et
portaient des faits d'une autre, et trois entrées de la liste des contributions comprimées jusqu'à
n'annoncer plus aucun résultat.

**Décomptes re-mesurés sur le PDF régénéré : 100 p. / 303 références**, contre 162 p. / 269 auparavant ;
14 sections et 25 questions ouvertes inchangées, **18 tableaux** (contre 15 : trois ont été ajoutés
pour absorber en forme dense de la prose énumérative, et **tous les renvois « tableau N » du document
ont été recalibrés en conséquence** — la numérotation de Pandoc est positionnelle).
`python check-veille.py` en **sortie 0** sur les quatre contrôles.

⚠ **Ce que la passe a réfuté, et c'est son principal résultat.** Six affirmations porteuses de la
veille sont tombées en dix jours : *(1)* « aucun protocole ne dispose de suite de conformité
publique » — `modelcontextprotocol/conformance` et `a2a-tck` existent, sans qu'aucune conformité soit
pour autant opposable par un tiers ; *(2)* « au-delà de deux sauts, aucun mécanisme **documenté** » —
trois brouillons individuels IETF en décrivent désormais, aucun n'étant adopté, ce qui déplace le
déficit de l'invention vers l'adoption ; *(3)* le marquage européen des contenus générés, annoncé au
2 décembre 2026, s'applique **depuis le 2 août 2026** ; *(4)* l'article 12.1 de la Loi 25 n'exige pas
d'intervention humaine déterminante ; *(5)* l'avis ACVM 11-348 ne mentionne pas l'agentique ;
*(6)* les soixante et un attributs `gen_ai.*` sont **soixante-trois** depuis le 7 août 2026. Deux
projections d'analystes ont par ailleurs été retirées comme **inattribuables ou mal citées** (les
1 300 G$ de 2029, qui portent sur la dépense totale en IA, et les 70 % de consolidation d'ici 2030,
sans aucune publication primaire). ⚠ *Les quatre volumes ne reçoivent aucune de ces corrections :
ils sont clos, et deux d'entre elles portent sur des énoncés qu'ils contiennent.*

⚠ **Ce que la passe ne fait pas.** Elle **ne touche à aucun des quatre volumes**, **ne franchit
aucune porte**, **ne lève aucune dérogation**, **ne referme aucune remontée**, **ne corrige pas
`decompte.sh`** et **ne publie rien**. La clôture **D-13 reste en vigueur pour les quatre volumes**.

**Le 9 août 2026 — dépôt de la revue de littérature, calage du compendium à mille pages, et
resynchronisation des porteurs de décomptes.** ⚠ *Trois gestes d'auteur, dont **le second rouvre la
clôture du Vol. IV** — le premier depuis D-13 à toucher un volume, fût-ce par son seul appareil.*

**(a) Un sixième livrable entre au dépôt.** [`Revue de littérature.md`](Revue%20de%20litt%C3%A9rature.md)
et son PDF — **40 pages fermes, 161 références, 18 sections, 8 tableaux**, neuf fronts de recherche —,
avec son contrôle propre, [`check-revue.py`](Python/check-revue.py) (quatre contrôles, **validés par
mutation**, sortie 0). ⚠ *Ces décomptes sont ceux du dépôt et ils sont laissés tels quels : la
**seconde passe du même jour**, en fin de fichier, porte la revue à **176 références et dix fronts**.
Un constat daté enregistre, il ne retarde pas.* Son titre est **aligné le même jour** sur le radical que la veille et le
Vol. IV portent déjà : *« Interopérabilité et Orchestration Agentiques : revue de la littérature
académique »*. ⚠ **Trois livrables sur six partagent désormais ce début d'intitulé**, et *un renvoi
qui cite par le seul titre ne désigne plus rien* — la mise en garde que ce fichier portait pour deux
documents en vise maintenant trois.

**(b) `Compendium.pdf` est recomposé à MILLE PAGES EXACTEMENT** (1 114 auparavant), sur instruction
d'auteur. ⚠ **C'est une réouverture de la clôture pour le Vol. IV, et elle est déclarée en tête de
fichier** — *aucune des cinquante pièces `.md` n'est touchée, pas un mot du corps ne change, mais
changer le gabarit d'un ouvrage clos, c'est reprendre son appareil.* Le calage se prend sur **trois
réglages du seul gabarit**, tous mesurés au voisinage de la cible sur le rendu complet : marges
verticales de 24/26 mm à **18/18 mm** (les relevés du 31 juillet portaient sur le **bloc horizontal**
et sur lui seul — *la verticale n'avait jamais été mesurée sur les monographies, et c'est ce qui la
rendait disponible*) ; pas d'interligne de 17,00 à **16,95 pt** (17,00 rend **1 001** pages, 16,95 en
rend **1 000**, 16,90 en rend **999** — *cinq centièmes de point séparent deux marches*) ; et
**Annexe I composée à 9,8/4,4 pt**, plus serré que le corps. ⚠ **Le corps de 13 pt et le bloc de
157,0 mm ne bougent pas** : ils sont relevés, et *on ne compense pas sur ce qui a été mesuré
ailleurs.* **Répartition du retrait, mesurée sur les deux rendus** : corps des cinquante chapitres
**991 → 928 p.** (−63), annexe hors plan **11 → 10** (−1), **Annexe I 112 → 62** (−50) — *la moitié
du gain vient d'une pièce qui se déclare elle-même « réunion, sans autorité propre », et c'est là
qu'il coûte le moins au fond.* ☑ **La cible est désormais VÉRIFIÉE et non constatée** :
[`build/build-pdf.sh`](2%20-%20Compendium/build/build-pdf.sh) **échoue** si le rendu canonique n'a pas
mille pages. *La pagination est une fonction en escalier ; une cible qu'on se contente de constater
se perd au commit suivant, en silence.* ⚠ **Un point d'impression n'est pas validé et il est écrit** :
à 18 mm de marge et 12 mm d'ascent, titre courant et folio tombent à **6 mm du bord de feuille**,
sous la zone non imprimable usuelle de **6,35 mm** — la compensation, si un imprimeur la refuse, se
prend sur l'ascent et le descent, jamais sur les marges qui portent la cible.

**(c) Les porteurs de décomptes sont resynchronisés.** ⚠ **Onze fichiers annonçaient 1 114 pages au
présent** : ce `README.md` (quatre annonces), le [conspectus du Vol. IV](2%20-%20Compendium/README.md),
[`1 - Corpus/README.md`](1%20-%20Corpus/README.md), les **cinq** `Livre */README.md`,
[`figures/programme.md`](2%20-%20Compendium/figures/programme.md) et
[`Compendium.html`](2%20-%20Compendium/Compendium.html) (trois annonces). *Les constats datés des
passes antérieures — 847, 863, 1 096 et 1 114 pages — sont laissés tels quels : un constat daté
enregistre, il ne retarde pas.* Quatre autres écarts, trouvés en resynchronisant :

- ⚠ **Ce fichier annonçait « cinq chaînes » de rendu en en listant six** — la revue de littérature
  avait sa commande sans être comptée —, et le paragraphe suivant disait déjà « les six chaînes ».
  *Une contradiction interne à deux paragraphes de distance, qu'aucun contrôle ne voit.*
- ⚠ **La section « Les cinq livrables » en décrivait cinq alors que l'encadré d'entrée en annonçait
  six** depuis la veille. Le tableau reçoit sa colonne « Revue de littérature ».
- ☑ **`pypdf` est installé — 6.15.0 — et il cesse d'être facultatif** : la porte de pagination
  l'interroge au build. *Les décomptes du 8 août, pris par lecture directe du `/Count` faute de la
  bibliothèque, ont été confrontés le 9 août aux trois méthodes* — `pypdf`, `/Count` et
  `grep -aoP '/Type/Page(?![sL])'` — **sur les six PDF : 100, 40, 569, 387, 427 et 1 000, identiques
  par les trois voies.**
- ⚠ **La référence de la veille qui porte le titre neuf du Vol. IV a changé de numéro** : **[266]**
  jusqu'à la refonte du 8 août, **[259]** depuis que la bibliographie est passée de 269 à 303 entrées.
  Ce fichier citait encore l'ancien numéro au présent. *La veille, elle, n'est pas corrigée sur sa
  pagination du compendium — sa réf. [259] donne 1 114 pages, ce qui était exact à son gel.*
- ⚠ **Le tableau des reliquats donnait `gauntlet-log.md` pour purgé, et il est revenu à l'arbre le
  8 août 2026**, avec deux blocs de plus depuis. La ligne porte désormais son dépassement.
- ⚠ **`build/compendium.template` annonçait l'Annexe I à 72 pages sous son nouveau régime ; elle en
  fait 62.** *Le chiffre venait d'un rendu d'essai pris avant la réduction des marges — juste à sa
  date, faux au rendu final.* Corrigé au commentaire, avec sa mesure.
- ⚠⚠ **Et le plus lourd, trouvé en balayant : la suppression de `verification/` a fait 152 renvois
  morts, non quatre.** Balayage des **168 `.md` du dépôt, 1 488 renvois relatifs, 160 morts** —
  dont **152 vers le `verification/` du Vol. III supprimé le 8 août 2026**, visant **20 rapports
  distincts** depuis **34 fichiers** (88 aux pièces de `monographie/`, 52 à `prd/`, 11 au
  `Monographie.md` assemblé, **1 au socle consolidé du Vol. IV**) ; les huit autres sont des **faux
  positifs** déjà documentés — motifs d'expression rationnelle et gabarits de chemin dans des blocs
  clôturés. *La clôture annonçait « 1 667 liens relatifs, 6 morts », et la passe du soir « quatre
  renvois morts, tous dans le `README.md` du Vol. III » : ni l'une ni l'autre n'a rebalayé l'arbre
  après la suppression, et les deux sous-estiment de deux ordres de grandeur.* ⚠ **Aucun n'est
  réécrit** : ils citent des rapports **par leur nom, à l'appui d'une preuve**, dans des pièces
  gelées d'un volume clos — *les réécrire altérerait la citation, les retirer effacerait la trace de
  ce qui a été vérifié.* Le constat entre au tableau des reliquats. ⚠ *Et il confirme la ligne
  « appareil de contrôle » de ce même tableau : **aucun des sept contrôles du dépôt ne résout un lien
  markdown** — les quatre renvois trouvés le 8 août l'ont été à la main, dans le seul fichier qu'on
  relisait ce jour-là ; **les 152 autres sont restés morts vingt-quatre heures sans que rien ne le
  signale**, et ils le resteront.*

**Contrôles rejoués le 9 août 2026, après recomposition** — `check-veille.py`, `check-resume.py`
(résumé à **y = 119,4 pt**), `check-revue.py`, `check-toc.py` (C1-C15), `check-sieges.py` (S1-S5,
26 sièges), `check-compendium.py` (P1-P8, trois rapports déclaratifs) : **six en sortie 0**.
⚠ **`decompte.sh --verifier` sort toujours 1** — Vol. II à 93 239 mots contre 93 242 attendus : *le
calage typographique ne touche à aucun corps, et l'écart de trois mots reste un arbitrage d'auteur.*

⚠ **Ce que la passe ne fait pas.** Elle **ne touche à la prose d'aucune des cinquante pièces du
Vol. IV**, **ne franchit aucune porte**, **ne lève aucune dérogation**, **ne referme aucune
remontée**, **ne corrige ni `decompte.sh` ni le corps du Vol. II**, **ne rattrape ni la veille ni la
revue sur leurs faits datés**, **ne dote `0 - Références/` d'aucun régime** et **ne publie rien**.
⚠ **Et elle ne régénère pas ce qui n'a pas de chaîne** : `Compendium.html` et les cinquante `.html`
de chapitre sont **relevés et corrigés à la main**, comme toujours — *le calage à mille pages a
changé une valeur que trois lignes de cette page portaient, et rien dans le dépôt ne l'aurait
signalé.*

**Le 9 août 2026, seconde passe du même jour — la revue de littérature reçoit un dixième front, et
quatre erreurs d'arithmétique tombent en recalculant.** Sur instruction d'auteur, la revue intègre la
**chorégraphie agentique en essaim multiagents** — la coordination sans chef d'orchestre, par
protocole d'interaction plutôt que par superviseur — et **reste à 40 pages fermes**. ⚠ *Le format
ferme n'était pas une contrainte de forme : c'est lui qui a rendu la passe coûteuse, et c'est lui qui
a révélé ce qui suit.*

**(a) Un dixième front, et quinze pièces versées.** Trois agents de recherche à consigne de source
primaire ont rapporté **17 pièces, une en doublon, 15 retenues** ; **les 17 notices ont été rouvertes
à l'API du dépôt par l'orchestrateur, non par les agents qui les rapportaient** — titres, dates,
versions et champs concordent tous. Corpus **161 → 176 entrées**, **158 → 173 arXiv**. Le front neuf
prend **[159-173]**, les trois pièces à DOI reculent en **[174-176]**. ⚠ **Aucune des quinze n'est
publiée en comité de lecture** — deux annoncent une acceptation au seul champ de commentaire, une y
annonce une simple *soumission* : *le front qui porte les résultats les plus conséquents sur la
coordination sans chef ne compte aucune publication arbitrée, et la thèse de la revue se durcit de
76 % à **77 %** au lieu de se diluer.*

**(b) Ce que la barre a attrapé et qu'aucun contrôle ne voyait.** La révision a été conduite en
boucle bâtisseur/critique, chaque morceau jugé **à l'aveugle** contre la version actuelle, étiquettes
retirées. **Score : deux morceaux sur trois gagnent.** ⚠ **Les deux compressions du premier tour
tenaient leur quota au mot près et passaient tous les contrôles exécutables ; les deux ont perdu, pour
le même motif — *elles avaient échangé de la preuve contre du slogan*.** Un juge : « *la loi d'échelle
collaborative établie jusqu'à plus d'un millier d'agents est logistique, donc saturante* réduit à
*échelle saturante* — le résultat y est redevenu une étiquette de sujet ». *Une boucle qui n'aurait
mesuré que les 40 pages les aurait déclarées réussies.* ⚠ **La clôture, perdante au premier tour, a
été reprise mais non rejugée** : le budget fixé avant de lancer était atteint. *C'est un plafond, et
il est déclaré ici plutôt que tu.*

**(c) Une erreur de fait, trouvée en creusant un écart de juge.** La revue écrivait à **deux
endroits** que l'observabilité complète des traces *porte l'attribution à 76 %* **[89]**. La notice
dit : *full traces improve attribution accuracy **by up to 76 %** over a partial-observation
counterpart.* C'est un **gain relatif**, la notice ne donne ni effectif de banc ni condition, et il
**ne partage aucun dénominateur** avec le 53,5 % de **[88]** auquel il était opposé. ⚠ *La phrase
causale qui en découlait — « ce plafond tient à l'instrumentation » — n'avait donc pas de mesure sous
elle.* Corrigée aux deux endroits, l'énoncé redevient une hypothèse. **Aucun contrôle exécutable ne
pouvait l'attraper : il fallait un juge qui demande d'où vient le chiffre.**

**(d) Quatre erreurs d'arithmétique préexistantes, mises au jour par le recalcul.** Elles ne viennent
pas du dixième front. *(i)* §3.2 comptait « cinq » pièces attestées au socle puis « les sept autres »,
en rangeant **[44]** et **[158]** dans des fronts qu'il déclarait ensuite n'en compter aucune — c'est
**six et six**. *(ii)* L'annexe annonçait « **cinq seulement** » puis en énumérait six. *(iii)*
L'annexe donnait **quatre** pièces du socle antérieures à 2025 ; il y en a **deux**. *(iv)* §12.3
annonçait « 120 pièces des dix fronts » quand le tableau de §3.2 en compte **123**, avec des
dénominateurs par front — sécurité 10/**12** pour un front de 11, gouvernance 2/**12** pour 11,
protocoles 4/**12** pour 13 — contredisant ce même tableau ; corrigé en **67 sur 123, soit 54 %**.
⚠ *Les numérateurs restent hérités du décompte antérieur et n'ont pas été revérifiés pièce à pièce,
sauf celui du front neuf — 11 sur 15, établi sur dossier. C'est écrit plutôt que tu.*

**(e) Le contrôle réparé avant d'être cru.** [`check-revue.py`](Python/check-revue.py) codait en dur
`sur 158` et `(Vingt-six|Trente et une)`. ⚠ **Passé à 28 auto-déclarations, le motif ne serait pas
tombé : il aurait cessé de chercher, et le contrôle serait passé au vert sur un document faux.** Les
alternatives couvrent désormais l'ancienne et la nouvelle valeur, un cinquième motif surveille le
compte des pièces sans revue, et le jeu de mutants passe de quatre à **six — tous tombent**.

**(f) Deux pages gagnées sans rien perdre, cherchées avant de couper dans l'argument.** Chaque entrée
de bibliographie écrivait son identifiant arXiv **deux fois** : en clair, puis dans l'URL en toutes
lettres. Replier l'URL derrière l'identifiant rend **2 pages sur 173 entrées** — même cible, même
identifiant lisible, un seul exemplaire, et le contrôle des doublons continue de passer parce qu'il
lisait déjà les deux séparément. La troisième page s'est prise dans des doublons **entre sections** :
un paragraphe de §6.2 rejouait intégralement le premier énoncé de la veille jusqu'à la même phrase de
clôture en gras, §3.2 et l'annexe tenaient le même compte des douze attestées, §3.1 énumérait les
revues que le tableau de l'annexe redonne colonne par colonne. **475 mots repris, aucun chiffre ni
mécanisme touché.** ⚠ **L'en-tête YAML n'est pas touché** : *atteindre la pagination par la
typographie serait contourner la contrainte, pas la satisfaire.*

**Contrôles rejoués après recomposition** — `check-revue.py` (4 contrôles, **six mutants tombent**),
`check-resume.py` (résumé à **y = 222,0 pt**, 148,3 pt de dégagement) : **deux en sortie 0**, PDF à
**40 pages** vérifiées au `/Count`.

⚠ **Ce que la passe ne fait pas.** Elle **ne touche à aucun des quatre volumes ni à la veille**,
**ne franchit aucune porte**, **ne lève aucune dérogation**, **ne referme aucune remontée**,
**ne revérifie pas pièce à pièce les numérateurs hérités de §12.3**, **ne rejuge pas la clôture** et
**ne publie rien**. Le journal détaillé de la boucle, tour par tour, était dans `gauntlet-log.md`,
⚠ **purgé le 10 août 2026 et relisible au seul historique git**.

**Le 10 août 2026 — dépôt d'un septième livrable, et resynchronisation de ce fichier sur lui.** Un
**essai sur les systèmes multiagents en essaim** entre à la racine du dépôt —
`Swarm Agentic Systems.md` et son PDF, [renommés `Traité.md` / `.pdf`](Trait%C3%A9.md) l'après-midi
même —, et ce `README.md` est
réaligné : quatrième réouverture déclarée, section « Les **sept** livrables » et sa septième colonne,
ligne au tableau de l'état, section propre au livrable, entrée à l'arborescence, septième chaîne de
rendu, et une réserve à l'ordre de lecture.

Décomptes **pris sur pièce** à cette date : **99 pages** (`pypdf`, sur le PDF versionné),
**118 références** dont **9 prépublications arXiv déclarées telles**, **7 chapitres** et
**21 sous-sections**, **20 tableaux**, **9 algorithmes** en pseudocode, gel au **10 août 2026**.

⚠ **Trois constats de la passe, dont deux sont des écarts.** *(a)* **Le fichier ne porte pas le titre
de l'ouvrage** : `Swarm Agentic Systems.md` contre *« Systèmes multiagents en essaim »* — c'est le
seul livrable du dépôt dans ce cas, et le seul dont le nom de fichier soit en anglais ; *un renvoi
pris sur le nom de fichier ne nomme donc pas l'ouvrage.* *(b)* **L'essai ne cite aucun autre
livrable, et aucun ne le cite** : ses 118 références ne contiennent ni la veille, ni la revue, ni
aucun des quatre volumes, et les protocoles du dépôt n'y paraissent qu'une fois, par la
spécification MCP prise en exemple de milieu. *Le dépôt gagne un livrable et non un renvoi* — en
contrepartie, c'est le seul des sept dont l'auto-citation soit **nulle**. *(c)* ⚠ **Un contrôle du
dépôt sort 1 sur ce PDF sans qu'il y ait de défaut** : [`check-resume.py`](Python/check-resume.py) code sa
marge basse en dur à **73,7 pt** (les 2,6 cm de la veille) et compte le folio, quand l'essai compose
à 2,35 cm et numérote dès la page de titre. Mesures relevées : dernière ligne du **résumé** à
**y = 325,7 pt**, soit **259 pt de dégagement** ; texte le plus bas de la page à **39,1 pt**, qui est
le **numéro de page**. *Le contrôle mesure juste et conclut faux ; il n'a pas été corrigé.*

⚠ **Ce que la passe ne fait pas.** Elle **ne touche à aucun des quatre volumes**, **ni à la veille**,
**ni à la revue**, **ne modifie pas l'essai déposé**, **ne corrige pas `check-resume.py`**, **ne
franchit aucune porte**, **ne lève aucune dérogation**, **ne referme aucune remontée**, **ne rejuge
pas la clôture** et **ne publie rien de ce qui est clos**. La clôture **D-13 reste en vigueur pour
les quatre volumes**.

**Le 10 août 2026, seconde passe du même jour — le septième livrable change de genre, de nom et de
gabarit.** Sur instruction d'auteur, le document déposé le matin passe d'**essai** à **traité** :
titre porté à *« Traité sur les systèmes multiagents en essaim »*, fichiers renommés
`Swarm Agentic Systems.md` / `.pdf` → [`Traité.md`](Trait%C3%A9.md) / `.pdf`, et rendu **recomposé au
gabarit d'article arXiv**. ☑ **Le renommage referme le seul écart de nomenclature du dépôt** : les
sept fichiers se nomment par leur **genre** — `Veille Technologique`, `Revue de littérature`,
`Monographie`, `Compendium`, `Traité` —, convention que rien n'écrivait avant qu'un nom anglais ne
l'enfreigne.

**Ce que la recomposition change, réglage par réglage** : marges de 2,18 × 2,35 cm à
**2,8 × 3,2 cm** ; bloc de titre à **courriel d'auteur** et date sur sa propre ligne ; **mots-clés
versés dans le bloc du résumé**, sous lui, où arXiv les attend ; **avant-propos et conclusion passés
en sections non numérotées** (`{-}`), comme la bibliographie l'était déjà. ⚠ **Ce qu'elle ne change
pas, et pourquoi** : `section-numbering` **reste absent de l'en-tête**, les sept chapitres portant
leurs numéros écrits à la main dans les titres — *le gabarit Typst numéroterait par-dessus et
produirait « 0.3.2 3.2 Titre », alors que l'ouvrage renvoie à ses propres numéros en une centaine
d'endroits.* ⚠ Et `keywords` **reste absent lui aussi** : le gabarit injecte cette variable sans
guillemets dans un tableau Typst, ce qui **casse la compilation**. Décomptes re-mesurés sur pièce :
**115 pages** (`pypdf`, sur le PDF versionné, contre 99 au gabarit précédent), **118 références**,
contenu inchangé.

☑ **Un défaut de balisage a été trouvé à la recomposition, et il ne se voyait qu'au rendu.**
L'introduction et la conclusion écrivaient leurs renvois en **doubles crochets** — `[[5]]`,
**16 occurrences sur 10 lignes** — quand le corps en écrit **512 en crochets simples**. *Pandoc ne
connaît pas cette forme et la composait littéralement* : le PDF du matin affichait « [[5]] » en
toutes lettres dans ses deux sections d'encadrement, et nulle part ailleurs. Normalisé sur la forme
majoritaire, puis contrôlé : **118 renvois cités, 118 notices déclarées, aucun orphelin dans un sens
ni dans l'autre.**

⚠ **La substitution « essai » → « traité » n'a touché qu'une occurrence du corps, et deux ont été
laissées à dessein.** L'ouvrage se nomme partout ailleurs *« l'ouvrage »* ou *« le livre »* : *le
genre était dans le paratexte, pas dans le texte.* Les deux exceptions sont nommées ici pour qu'une
passe ultérieure ne les prenne pas pour un oubli — un **banc d'essai** au §2.3, qui est un montage
d'épreuve et non un genre littéraire, et l'**« essai d'interprétation »** du titre de Grassé 1959
(réf. [4]), *qu'on ne récrit pas sans falsifier une citation*.

⚠ **Ce que la passe ne fait pas.** Elle **ne touche à aucun des quatre volumes**, **ni à la veille**,
**ni à la revue**, **ne change pas un énoncé du traité** — hors le mot de genre et la forme des
renvois —, **ne corrige pas `check-resume.py`**, **ne franchit aucune porte**, **ne lève aucune
dérogation**, **ne referme aucune remontée**, **ne rejuge pas la clôture** et **ne publie rien de ce
qui est clos**. La clôture **D-13 reste en vigueur pour les quatre volumes**.

**Le 10 août 2026, troisième passe du même jour — le traité est calé à cent pages exactement.** Sur
instruction d'auteur, `Traité.pdf` passe de **115 à 100 pages**, et **le calage se prend sur le seul
en-tête YAML** : marges portées **au pouce — 2,54 cm sur les quatre côtés** — et `linestretch: 0.9`.
⚠ **Aucun mot du corps ne change**, ni un renvoi, ni une référence : *recomposer n'est pas récrire*,
et **trois paginations se sont succédé en un jour à contenu strictement identique** — 99 pages au
dépôt du matin (marges 2,18 × 2,35 cm), 115 à la recomposition arXiv (2,8 × 3,2 cm), **100 après
calage**.

⚠ **Le second réglage mérite d'être justifié, parce qu'il ressemble à une compression et n'en est
pas une.** `linestretch: 0.9` ramène l'interligne du gabarit Typst par défaut — `leading:
linestretch × 0,65em`, soit **14,65 pt mesurés** au corps de 11 pt — à **13,9 pt**. *Un article
LaTeX 11 pt compose à 13,6 pt* : le réglage rapproche le traité de la norme de l'espèce au lieu de
l'en écarter, et le défaut de Typst, à 1,33 fois le corps, était simplement plus aéré qu'elle. Les
marges au pouce sont, elles, la géométrie canonique de l'article. **Le calage améliore donc la
conformité arXiv au lieu de la payer.**

⚠ **Deux variantes atteignaient la cible, et le choix est écrit ici pour qu'on n'ait pas à le
refaire.** L'autre était un corps de 10,5 pt à interligne intact, marges autour de 2,7 cm ; elle a
été écartée parce qu'elle **quitte les corps normalisés** (10, 11, 12 pt) et la géométrie au pouce,
*pour un gain de lisibilité nul*. Un balayage de huit réglages a servi à trancher ; il n'est pas
versé au dépôt.

⚠ **La cible n'a pas de porte, et c'est le manque le plus lourd de cette passe.** Le compendium fait
**échouer son build** hors de ses mille pages ; le traité se rend par une invocation `pandoc` nue,
qui **écrit son PDF quel qu'en soit le nombre de pages**. *La pagination est une fonction en escalier
— un mot ajouté suffit à changer de marche —, et une cible qu'on constate au lieu de la vérifier se
perd au commit suivant, en silence.* Elle est ici **constatée** : `pypdf` sur le PDF versionné,
**100 pages**. Mesures de page de titre après calage : bloc du résumé et des mots-clés à
**y = 284,0 pt**, **212 pt de dégagement** ; folio à 42,9 pt. `check-resume.py` **sort 1**, toujours
sur le folio et toujours par sa constante de marge, comme aux deux gabarits précédents.

⚠ **Ce que la passe ne fait pas.** Elle **ne touche à aucun des quatre volumes**, **ni à la veille**,
**ni à la revue**, **ne change pas un caractère du corps du traité**, **n'ajoute aucune porte de
pagination**, **ne corrige pas `check-resume.py`**, **ne franchit aucune porte**, **ne lève aucune
dérogation**, **ne referme aucune remontée**, **ne rejuge pas la clôture** et **ne publie rien de ce
qui est clos**. La clôture **D-13 reste en vigueur pour les quatre volumes**.

**Le 10 août 2026, quatrième passe du même jour — la note de titre du traité est retirée.** Sur
instruction d'auteur, le champ **`thanks` est supprimé de l'en-tête** de [`Traité.md`](Trait%C3%A9.md) :
la page de titre perd l'**astérisque** qui suivait le mot « essaim » et la **note de bas de page**
qu'il appelait. ⚠ **Ce que cette note portait, et qui disparaît du fichier avec elle** : la
divulgation d'assistance par modèle de langage — *« Ce document a été rédigé avec l'assistance d'un
modèle de langage (Claude, Anthropic) : recherche documentaire, rédaction des chapitres, vérification
des références et montage de l'ouvrage. L'auteur en assume la sélection des sources, les arbitrages
de contenu et les erreurs résiduelles. »* — reproduite ici pour qu'elle reste lisible quelque part.

⚠ **Le traité devient ainsi le seul des sept livrables à ne porter aucune divulgation d'assistance
dans son rendu.** La veille et la revue déclarent la leur dans leur corps ; les quatre volumes la
tiennent de leur appareil de gouvernance. *Elle ne subsiste, pour le traité, qu'à la rubrique
« Assistance par agents » des [avertissements](#avertissements) de ce fichier, qui couvre l'ensemble
des travaux* — **le PDF diffusé seul ne la porte plus**, et c'est une conséquence à connaître si le
fichier quitte le dépôt.

☑ **La cible de cent pages tient au retrait**, re-mesurée sur pièce après recomposition : `pypdf`
rend **100 pages**. *La note vivait sur la page de titre, sous le résumé, dans une zone que le calage
ne disputait pas.*

⚠ **Ce que la passe ne fait pas.** Elle **ne touche à aucun autre livrable**, **ne change pas un
caractère du corps du traité**, **ne modifie aucun autre champ de l'en-tête**, **n'ajoute aucune
porte de pagination**, **ne franchit aucune porte**, **ne lève aucune dérogation**, **ne referme
aucune remontée**, **ne rejuge pas la clôture** et **ne publie rien de ce qui est clos**. La clôture
**D-13 reste en vigueur pour les quatre volumes**.

**Le 10 août 2026, cinquième passe du même jour — audit intégral du traité par boucle
bâtisseur/critique.** Sur instruction d'auteur : auditer [`Traité.md`](Trait%C3%A9.md) en totalité,
corriger tous les écarts, **maintenir 100 pages**. Deux axes fixés par l'auteur — tenue du français
technique, fiabilité des sources —, gagés sur la pièce du dépôt qui les incarne, la **veille
technologique**. Huit morceaux jugeables ; un bâtisseur et un juge à l'aveugle par morceau ; ordre
A/B alterné et extraits tronqués à longueur comparable, pour qu'aucun juge ne devine à la taille.
**Le traité gagne 7 comparaisons sur 8.** Journal complet : `gauntlet-log.md`, ⚠ **purgé de l'arbre à
la passe suivante du même jour — il ne se relit plus qu'à l'historique git.**

**168 correctifs appliqués, 0 rejeté**, plus 3 déplacements de légende : 97 au premier tour
(−214 car.), 44 au second (+973), 27 à la passe de lissage (−113). ⚠ *Aucun bâtisseur n'a écrit dans
le fichier* : huit agents en parallèle sur un même `.md` s'écrasent, chacun a donc rendu des
correctifs à ancre exacte et unique, appliqués centralement par un script qui **rejette** toute ancre
non unique et tout delta déclaré non conforme. **État vérifié sur pièce au rendu final** : 100 pages,
0 page blanche, 20 tableaux numérotés 1 à 20, **118 renvois cités pour 118 notices, aucun orphelin**.

⚠ **Ce que la confrontation des 118 notices à leur source primaire a trouvé.** 108 confirmées,
10 corrigées, 0 non confirmée — mais le décompte n'est pas le résultat. *(a)* **Un titre inventé**
(réf. 93), auteurs, revue et année exacts par ailleurs : **un cas sur 118**. *(b)* **Quatre statuts
éditoriaux faux, tous dans le même sens** : des pièces arXiv annoncées prépublications alors qu'elles
sont parues arbitrées — CAV 2013, CAV 2017, *IEEE Software* 2016, *CACM* 2020. ⚠ *L'erreur
sous-évaluait le corpus au lieu de le gonfler ; dans un ouvrage dont la déclaration de statut est la
discipline, elle n'en est pas moins une faute.* *(c)* **12 cibles mouvantes** — du code cité sur la
branche `trunk`, où rien de ce qui est allégué ne se retrouve — ancrées sur des SHA et des étiquettes
**ouverts et relus** : les valeurs de réplication alléguées au ch. 6 ont été retrouvées dans le code à
l'étiquette 4.1.0. *(d)* **13 paginations ouvertes ou absentes** fermées sur Crossref, DataCite ou dblp.

⚠ **Deux arbitrages de la course méritent d'être connus, parce qu'ils vont contre le réflexe.**
*(a)* **Un signalement d'agent s'est révélé faux à la vérification** : trois légendes de tableau
placées avant leur tableau étaient annoncées comme un défaut de rendu. *Pandoc accepte les deux
formes*, les vingt tableaux sont numérotés au PDF, aucune légende n'est perdue — constat rétrogradé
d'un bogue à une incohérence de source, puis aligné sur la convention majoritaire. *Un rapport
d'agent se vérifie avant de se croire.* *(b)* **« une invariante » a été normalisée au masculin, huit
occurrences avec tous leurs accords.** Le mot est masculin en informatique, mais **le féminin était
majoritaire dans l'ouvrage, 12 contre 2** — donc une convention d'auteur, et une convention se
remonte au lieu de se corriger. Elle avait été portée à l'arbitrage et laissée en l'état ; c'est un
bâtisseur qui, en en corrigeant deux dans son seul morceau, a rendu l'abstention impossible. *Un
texte à moitié normalisé est pire que l'un ou l'autre état.* ☑ Les deux occurrences féminines qui
subsistent sont les bonnes : l'adjectif y accorde avec un sujet féminin, le solécisme ne portait que
sur le nom.

⚠ **Ce que la passe ne fait pas.** Elle **ne touche à aucun autre livrable**, **n'ajoute aucune porte
de pagination** — la cible de cent pages reste **constatée et non vérifiée au rendu** —, **ne corrige
pas `check-resume.py`**, **ne lève aucune des réserves de fond du traité** — la frontière qu'il
annonce reste argumentée et non mesurée, et sa conclusion le dit elle-même —, **ne franchit aucune
porte**, **ne referme aucune remontée**, **ne rejuge pas la clôture** et **ne publie rien de ce qui
est clos**. La clôture **D-13 reste en vigueur pour les quatre volumes**.

**Le 10 août 2026, sixième passe du même jour — purge de la racine, et resynchronisation de ce
fichier sur elle.** Sur instruction d'auteur, deux gestes sur l'outillage, aucun sur un livrable :
*(a)* **les trois contrôles quittent la racine pour [`Python/`](Python/)** — `check-veille.py`,
`check-resume.py`, `check-revue.py`, déplacés sans qu'une ligne de leur code change ; *(b)*
**`gauntlet-log.md` est supprimé**, le journal des boucles bâtisseur/critique de la veille, de la
revue et de l'audit du traité. *La racine ne porte plus que les sept rendus, ce fichier, `.gitignore`
et les trois dossiers de travail.*

☑ **Les trois contrôles ont été rejoués après déplacement, et ils sortent 0** : `python
Python/check-veille.py`, `python Python/check-revue.py`, `python Python/check-resume.py`.
⚠ **Une condition d'exécution est née du déplacement et il faut la connaître** : les trois scripts
ouvrent leurs sources par **chemin relatif au répertoire courant** (`SRC = 'Veille Technologique.md'`,
`SRC = 'Revue de littérature.md'`, `'Veille Technologique.pdf'` par défaut). Ils marchent donc
**depuis la racine du dépôt, et échouent depuis `Python/`** — *rien dans le code ne le signale, et
aucun d'eux ne résout son propre chemin d'installation.* Le comportement sur le traité est inchangé :
`python Python/check-resume.py "Traité.pdf"` **sort 1** sur sa constante de marge et son folio,
toujours sans qu'une ligne soit rognée.

⚠ **La purge du journal était prévisible et elle est irréversible en lecture directe.** Le tableau
des reliquats donnait déjà `gauntlet-log.md` pour purgé le 8 août, puis notait son retour ; il repart,
et la ligne est remise à jour avec **l'aller-retour complet** plutôt qu'avec son seul état final. *Le
journal était suivi par git : il se relit à l'historique, ce qui n'était pas le cas des deux rapports
d'évaluation académique purgés le même jour que lui la première fois.*

☑ **Ce que cette passe répare dans ce fichier, et qui aurait été un renvoi mort silencieux.**
**Cinq liens** visaient les scripts à la racine et **quatre** visaient le journal : **neuf renvois
seraient morts au déplacement**, tous corrigés ici — les cinq repointés sur `Python/`, les quatre
convertis en mention avec leur date de purge. ⚠ *C'est exactement la classe d'écart que le tableau
des reliquats décrit à sa dernière ligne* : **aucun des sept contrôles du dépôt ne résout un lien
markdown**, un déplacement de fichier ne lève donc aucune erreur, et **rien n'aurait signalé ces neuf
renvois** si la resynchronisation n'avait pas été faite à la main. *Le contrôle qui manque est
toujours le même, et il manque toujours.*

⚠ **Ce que la passe ne fait pas.** Elle **ne modifie aucun des sept livrables**, **ne change pas une
ligne des trois scripts**, **ne corrige pas `check-resume.py`**, **n'ajoute aucune porte de
pagination ni aucun contrôle de renvois**, **ne franchit aucune porte**, **ne lève aucune
dérogation**, **ne referme aucune remontée**, **ne rejuge pas la clôture** et **ne publie rien de ce
qui est clos**. La clôture **D-13 reste en vigueur pour les quatre volumes**.
