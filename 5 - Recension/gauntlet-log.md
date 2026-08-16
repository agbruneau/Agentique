# Journal de la boucle — Rapport de l'art (recensio)

Journal en ajout seul. Un bloc par tour : morceau, verdict A/B, écart retenu, coût.

## Cadre fixé avant le lancement

| | |
|---|---|
| **Objectif** | `5 - Recension/Rapport de l'art.md` + `.pdf` — recension exhaustive de l'état du champ, établie sur le seul contenu du dépôt |
| **Barre** | `2 - Compendium/Livre I/01-interoperabilite-integration-entreprise.md` — ~15 000 mots, le standard de tenue le plus exigeant du dépôt |
| **Comparaison** | à l'aveugle, étiquettes retirées, ordre alterné d'un tour à l'autre ; verdict binaire, pas de note sur 10 |
| **Plafond de budget** | ~1,2 M tokens — deux vagues. C'est le budget qui ferme la boucle, pas un nombre de tours. |
| **Gabarit PDF** | celui du compendium — Pandoc → Typst, `2 - Compendium/build/compendium.template`, filtre `accentuation.lua`. Sans la porte des mille pages, qui est propre au compendium. |
| **Sortie de boucle** | victoire à l'aveugle, budget épuisé, gains marginaux sur deux tours, ou arrêt demandé |

**Le prompt donné aux bâtisseurs**, sans architecture — le découpage en chapitres est le mien, l'écriture leur appartient :

> Dans le dépôt `Agentique`, produis un rapport de l'art — une recension exhaustive de l'état du champ
> de l'interopérabilité, de l'orchestration et de la coordination agentiques — en Markdown et en PDF.
> Sa matière est le seul contenu du dépôt : `5 - Recension/OnePager.html` fournit l'introduction et la
> mise en contexte ; `2 - Compendium/Compendium.pdf`, `3 - Traité/Traité.pdf`,
> `4 - Veille/Veille Technologique.pdf` et `4 - Veille/Revue de littérature.pdf` fournissent les
> chapitres thématiques ; l'épilogue se construit sur ce que les chapitres ont établi, et sur rien
> d'autre. Aucune source ouverte hors du dépôt. Chaque énoncé hérite du régime de preuve du livrable
> qui le porte, jamais d'un meilleur. La barre : chaque chapitre doit tenir côte à côte avec
> `2 - Compendium/Livre I/01-interoperabilite-integration-entreprise.md` et gagner la comparaison à
> l'aveugle — même densité, même sourçage, même tenue. Le découpage, le nombre de chapitres et l'ordre
> du travail t'appartiennent.

## Découpage — six morceaux jugeables indépendamment

| | Chapitre | Matière principale |
|---|---|---|
| C1 | Le socle protocolaire | Compendium Livre I ch. 1, 2, 8, 9, 10 ; veille ; revue |
| C2 | Identité, délégation et fabrique de confiance | Compendium Livre II ch. 12-18, 21 |
| C3 | Modes de défaillance, sécurité et sûreté | Compendium Livre I ch. 3, 6, 11 ; Livre II ch. 19, 20 ; revue |
| C4 | Orchestration en entreprise et cadre réglementaire | Compendium Livre III ch. 22-36 |
| C5 | Exploiter, produire, livrer | Compendium Livre IV ch. 37-46 ; Livre V ch. 47-50 |
| C6 | Coordination sans coordinateur | Traité ; Compendium Livre I ch. 4, 5 ; revue |

L'introduction vient du `OnePager.html`, l'épilogue se construit sur les six chapitres une fois
qu'ils sont arrêtés. Les deux passent par la même boucle, après la première vague.

---

## Tour 0 — la chaîne de rendu, avant tout jugement de contenu

**Morceau** : la chaîne PDF. Un critique qui ne peut pas ouvrir l'artefact rend un tour nul ; la
chaîne se règle donc avant que quoi que ce soit ne se juge.

`build/recension.template` dérive de `2 - Compendium/build/compendium.template` — grille, fontes,
palette, tableaux et encadrés au trait près — avec quatre écarts, tous structurels :

1. **pas de Livres** — l'ouverture pleine page `ouverture-livre` est retirée ;
2. **ouvertures étiquetées** — `ouverture-chapitre(n)` et `ouverture-annexe()` cèdent à un
   `ouverture-piece(etiquette, rang)` unique. ⚠ Le rang est **posé par l'assembleur**, jamais
   compté : un décompte des titres de niveau 1 donnerait « chapitre 1 » à la pièce liminaire et
   décalerait les six ;
3. **aucune porte de pagination** — les mille pages exactes sont une instruction propre au
   compendium ; ici le nombre de pages est un constat ;
4. **page de titre et colophon** propres au rapport.

`build/rendre-recension.py` compose depuis `Rapport de l'art.md`, **seule source qui fait foi** —
les pièces de `chapitres/` sont le brouillon de la boucle et cessent d'être lues à l'assemblage.
Le filtre `accentuation.lua` du compendium est repris tel quel.

**Preuve** : maquette de deux chapitres et deux liminaires composée, puis rendue en PNG à 110 ppp
et inspectée page à page. Vérifiés à l'œil sur le rendu, non déclarés depuis la source : page de
titre sur une seule page, table des matières où l'ouverture et l'épilogue **ne consomment aucun
rang**, bandeau « CHAPITRE 2 » sur le deuxième chapitre, sections auto-numérotées 1.1 / 1.1.1,
tableau à filets *booktabs* avec sa rangée de tête en accent, et la règle d'accentuation appliquée
— une saillance en italique, le reste du gras long rendu au romain.

**Défaut trouvé et corrigé au rendu** : les pièces liminaires entraient à la table des matières en
bas de casse (« à lire avant tout le reste »), la queue de l'intitulé devenant le titre sans reprise
de majuscule. Corrigé dans l'assembleur, revérifié sur le rendu.

**Coût** : ~55 k tokens.

---

## Révision du plafond, 16 août 2026

Le plafond de 1,2 M était **faux d'un facteur deux**, et le journal doit le dire plutôt que de
l'absorber. Deux bâtisseurs sur sept ont consommé 582 k à eux seuls — 216 k pour les liminaires,
366 k pour le chapitre 6. Le dimensionnement supposait des bâtisseurs qui rédigent ; ce sont des
bâtisseurs qui **fouillent** — un traité de 458 Ko, un PRD de 2 200 lignes et un registre de
décisions pour retrouver cinq écarts de mesure et distinguer lesquels contredisent le traité.

Nouveau plafond, arrêté par l'utilisateur : **~2,2 M**, la boucle complète — sept critiques à
l'aveugle, une seconde vague sur les pièces les plus faibles seulement, lissage, épilogue et rendu.

---

## Tour 1 — pièce 00, les deux liminaires

**Morceau** : `chapitres/00-liminaires.md` — avertissement de régime, puis ouverture sur l'échelle
de maturité à six niveaux du `OnePager.html`.

**Comparaison à l'aveugle** : A et B remis à un critique à contexte neuf, étiquettes retirées,
copiés hors du dépôt sous des noms neutres. A = chapitre 01 du compendium (la barre), B = notre
pièce. Le critique ignorait laquelle était en jeu.

**Verdict : B.** Notre pièce gagne. Le motif tient en une ligne, et il porte contre la barre :

> A est exact mais anonyme — sur ~11 000 mots, six attributions seulement, et une déclaration de
> régime en en-tête qui tient lieu de provenance pour tout le reste ; B ancre chaque énoncé sur un
> fichier et une section, et les ancrages tiennent à la vérification.

Le critique a contrôlé une douzaine de renvois de B contre le dépôt — les sept gels, 12/32/145 sur
189, 46 entrées F-01…F-48, 428 tests, les cinq écarts du traité, la divergence de dates du README
racine, le §1.1.2.1 du Vol. I : **tous se résolvent exactement**. Il a aussi relevé, contre la
barre, que le chapitre 01 du compendium **dé-nomme ce que sa source nommait** — « une spécification
dédiée » là où le Vol. I écrit « Arazzo 1.0.0 », « un courtier de files mûr » pour Kafka,
RabbitMQ, Pulsar et NATS. *Constat sur la barre, pas sur notre travail : rien à en tirer ici sinon
que la barre n'est pas hors d'atteinte.*

**Écart retenu contre nous, un seul** : « re-vérifiées intégralement » vaut pour 303 références sur
342 et 176 sur 192, et le texte ne le dit pas. Les deux couples de cardinaux sont exacts et
proviennent du même fichier ; 39 références de la veille et 16 de la revue ne sont couvertes par
aucun des deux énoncés. Défaut d'autant plus net que la pièce **sanctionne ce genre-là quatre
paragraphes plus haut**, en posant sa règle de résolution contre le README racine — mais ici les
deux cardinaux vivent à l'intérieur du même livrable, et aucune règle ne les départage.

**Repart au bâtisseur.** Reprise ciblée, nouveau contexte, sur ce seul écart.

**Coût du tour** : 216 k (bâtisseur) + 132 k (critique) = 348 k.

---

## Tour 1 — pièce 06, coordination sans coordinateur

**Morceau** : `chapitres/06-coordination-sans-coordinateur.md`, ≈ 4 500 mots.

Le bâtisseur rend les cinq écarts traité/mesure en tableau avec la ligne de partage explicite —
trois contredisent un énoncé du traité (budget de retard du mode « moyeu » ; dérive de la somme
sans relance, dont *la conséquence mesurée est pire que l'énoncé réfuté*, l'erreur devenant
indétectable par l'attente ; Φ_c), deux ne contredisent rien. Il rapporte aussi une observation
que le dépôt ne fait nulle part : le §3.1 de la **troisième** édition du traité porte désormais la
valeur mesurée, l'écart ayant été reporté dans le texte qui l'avait causé pendant que le registre
continue de le compter.

**Verdict : B.** Notre chapitre gagne, sur le même motif que la pièce 00 :

> Dans B, chaque énoncé factuel porte sa provenance à l'endroit où il est avancé (« §1.2 du
> traité », « PRD §8.3 », `bancs/nf05-debit/VERDICT.md`), et mes trois vérifications sont tombées
> exactement juste ; dans A, l'appareil de provenance est entièrement dans l'en-tête et entièrement
> absent du texte qu'il gouverne — une quarantaine de faits datables sans une seule source
> consultable.

Trois vérifications du critique sur nous : métadonnées du traité (exact), régimes de preuve du
corpus arXiv et l'écart +80,8 % / −70,0 % (exact, y compris la restriction correcte au sous-corpus
de 189 pièces alors que la revue en compte 192). L'arithmétique interne se vérifie sans le dépôt et
tient : π/(4×99) = 7,933 × 10⁻³, √((1−0,05)/10⁻³) = 30,82, amplitude Φ_c de 0,055 soit dix-huit
fois la précision annoncée.

**Écart retenu contre nous, un seul** : les blocs « Mesuré » — toute l'autorité du chapitre —
n'indiquent presque jamais la **taille de population**, dans un chapitre dont le sujet est l'échelle
et dont l'instrument rate sa cible d'échelle d'un facteur ~70. Le chapitre porte les deux faits
côte à côte — NF-05 non atteinte en Θ(*n*²), et « vérifier à *n* = 5 ne dit rien de *n* = 5 000 » —
sans jamais écrire celui qui les joint : *le plafond de débit interdit les grands n, donc la colonne
« Ce que la mesure donne » est une colonne petit-n, et le lecteur ne peut pas le savoir.*

**Repart au bâtisseur.** Reprise ciblée, nouveau contexte.

**Coût du tour** : 366 k (bâtisseur) + 103 k (critique) = 469 k.

---

## Tour 2 — pièce 00, reprise sur l'écart

**Résultat : l'écart était plus large que le critique ne l'avait vu, et dans le sens défavorable.**
Le bâtisseur de reprise est descendu aux livrables au lieu de s'arrêter au README, et les deux cas
se séparent :

- ☑ **La revue tranche le sien en faveur du régime fort.** Ses seize entrées neuves
  « [177-192] » sont « retenues au même critère que la passe neuve », et les notices arXiv ont été
  « reprises une seconde fois, intégralement, le 15 août 2026 : 189 notices demandées, 189
  obtenues […] les 173 du premier relevé **et les seize entrées depuis** ». La réconciliation ferme :
  173 + 3 à DOI = 176, 173 + 16 = 189, 189 + 3 = 192.
- ⚠ **La veille dément « intégralement » au-delà de la marge signalée.** Elle écrit que la passe du
  15 août « ne rouvre pas la bibliographie entière mais les sources vivantes », sa colonne
  *Énoncés* pour cette passe est vide, et son annexe de traçabilité porte un tableau
  « Références non rouvertes, ni au premier ni au second tour ». Elle ne déclare jamais 342 — ce
  cardinal vient de `check-veille.py`, pas du texte.

**Aussi** : la prémisse du critique était inexacte sur un point, et à notre avantage — les deux
cardinaux ne coexistent pas dans le même livrable, ils sont tous deux dans un **README**. La règle
que la pièce posait déjà résolvait donc le cas telle quelle, une fois descendu aux livrables. La
pièce le dit désormais, et clôt en registre : *« Le dépôt ne permet donc pas de dire quelle part du
corpus de la veille le régime le plus fort du 15 août atteint ; il permet de dire que ce n'est pas
la totalité. »*

**Pièce 00 : sortie de boucle** — victoire à l'aveugle au tour 1, écart soldé au tour 2.

**Coût du tour** : 115 k.

---

## Tour 1 — pièce 05, exploiter, produire, livrer

Bâtisseur livré : 4 499 mots, onze sections. Il rapporte deux points que les README traitent
autrement que le lecteur ne s'y attendrait — l'écart de volumétrie en défaut des Livres IV et V
(−13,1 % et −9,6 %) est traité par le dépôt comme **une mesure de l'absence de sources** et non
comme un défaut ; et le manque du Livre V est **définitif et non en attente**, sa publication étant
bloquée par D-3 sur un dépôt clos par D-13. Il déclare de lui-même deux réserves sur sa propre
passe : deux chapitres du compendium ouverts au titre seulement, dont il ne tire aucun énoncé.

**Critique à l'aveugle en cours.** Coût du bâtisseur : 415 k.

---

## Levée du plafond, 16 août 2026

Le plafond de ~2,2 M est franchi à ≈ 2,34 M avec deux bâtisseurs encore en vol. Instruction
d'auteur : **procéder en totalité jusqu'à ce que la boucle soit complète**. Le budget ne ferme donc
plus la boucle ; ce qui la ferme est l'épuisement des écarts — victoire à l'aveugle sur chaque
pièce, écart soldé, puis lissage.

**Ce que la mesure du coût aura appris, et qui vaut au-delà de cette course** : les bâtisseurs
coûtent 360 à 460 k chacun parce qu'ils **fouillent** au lieu de rédiger — C1 a ouvert onze
fichiers dont quatre chapitres de 60 à 100 Ko, C4 en a ouvert seize, C6 a lu un traité de 458 Ko et
un PRD de 2 200 lignes. Les critiques coûtent 100 à 130 k, **et ce sont eux qui produisent le
verdict**. Le rapport coût/rendement de la technique est dans ce rapport-là.

⚠ **Défaut de découpe relevé par un bâtisseur contre l'arbitre, et retenu** : la bande de
3 000-4 500 mots que j'ai imposée par morceau a fait **supprimer des faits sourcés** au chapitre 1 —
jalons de la matrice de maturité du ch. 9 § 9.2.5, résultats de Tuan et Sanyal (2026), tableau des
rails de cartes du ch. 10 § 10.3.3, pyramide d'évaluation du ch. 9 § 9.5.1. Contre un étalon de
10 859 mots, une contrainte de longueur travaille **contre** la barre qu'elle sert. Les reprises
lèvent la bande.

---

## Le biais de la consigne, relevé contre moi-même

Quatre pièces sur quatre ont gagné à l'aveugle, et **toujours pour le même motif** : la provenance
est à l'endroit de l'énoncé chez nous, dans l'en-tête chez la barre. Or c'est exactement l'axe que
mon prompt de bâtisseur imposait — « chaque énoncé factuel porte sa provenance en clair ». *La
comparaison était donc partiellement pipée par ma propre consigne : la barre est réelle, mais je
la faisais juger sur le terrain où nous étions préparés.*

Deux contrôles ont été posés en conséquence, à partir de la pièce 03 :

1. **Ordre retourné** — notre pièce passe en A, la barre en B. Si elle gagne aussi en première
   position, le biais de position est écarté.
2. **Avantage de consigne retiré au critique** — on lui dit explicitement que la provenance au
   point d'énoncé *n'est pas le seul critère*, que la valeur du contenu et la profondeur comptent
   autant, et qu'**une saturation de gras et de marqueurs est un défaut au même titre qu'une source
   absente**.

Résultat : la pièce 03 gagne quand même, **en position A**, et le critique a *mesuré* l'objection
typographique au lieu de la supposer — 42 « ⚠ » et 223 passages en gras pour 4 284 mots, un gras
tous les 19 mots contre un tous les 46 chez la barre. Il l'a jugée réelle et non décisive, chaque
marqueur introduisant une réserve distincte. **La mesure est reportée à la passe de lissage.**

Une **épreuve finale non pipée** reste à courir, et elle est la seule qui vaille : le rapport
assemblé contre le « Rapport de l'art » purgé de 20 437 mots — même genre, même corpus, même
commande, aucun avantage de consigne.

---

## Tours 1 et 2 — les cinq chapitres thématiques

Le tableau donne le verdict, l'écart retenu et ce que la reprise a trouvé. **Cinq sur cinq gagnent
à l'aveugle**, donc la sortie de boucle de chaque pièce est la victoire ; la reprise solde l'écart.

| | Verdict | Écart retenu | Ce que la reprise a trouvé — et qui excédait l'écart |
|---|---|---|---|
| **01** Socle protocolaire | **B** *(nous)* | Le § 1.8 bâtit sa seule conséquence opposable sur un plancher de douze mois que le § 1.3 avait lui-même déclaré dérogeable à quatre-vingt-dix jours | Une **seconde dérogation perdue** par la première passe — retrait du transport HTTP+SSE, compte à rebours démarrant à un statut de proposition **non daté**, donc non bornable. Le plancher réel est « douze mois par défaut, quatre-vingt-dix jours sous risque actif, indéterminé pour un transport ». Les queues de fichiers non lues portaient **toute la matière « responsabilité »** que le titre du § 1.7 annonçait sans la livrer. 4 500 → **7 462 mots** |
| **03** Défaillance et sûreté | **A** *(nous, ordre retourné)* | « ramène le succès moyen de **84,7 %** à 2,3 % » — le 84,7 % n'a aucun antécédent ; tout ce qui vient de la revue arrive en pourcentages anonymes là où ce qui vient du compendium nomme ses auteurs | *(reprise en cours)* |
| **04** Orchestration et réglementaire | **B** *(nous)* | Le § 4.7 relaie une contradiction frontale sans la nommer — le compendium dit que l'avis ACVM 11-348 nomme l'autonomie dans son texte, la veille dit qu'il ne contient pas le mot | **Aucun des deux livrables n'a lu le texte anglais de l'avis.** La veille balaie trois chaînes *françaises* sans déclarer la langue ; le compendium porte la réserve CA-5 disant qu'il restitue en français un instrument rédigé en anglais ; et le corpus avait **retiré ses gloses « autonomy » et « adaptiveness » le 17 juillet 2026**, trois semaines avant le balayage, au motif qu'il restituait un original qu'il n'avait pas lu. Règle posée : *un mot qu'on n'a pas cherché ne peut pas être déclaré absent.* § 4.7 : 430 → **1 450 mots** |
| **05** Exploiter, produire, livrer | **B** *(nous)* | Le § 5.10 s'intitule « ce que le champ ne sait pas, **écrit au même rang que ce qu'il sait** » et n'écrit que le premier terme ; rien ne tempère « aucune n'est recevable » | Six acquis inscrits **avec leur degré**, du résultat d'impossibilité — seul acquis *de champ* — au repérage non extrait. Le « +90 % de qualité pour ~15× les jetons » est rendu à ce que la source dit, c'est-à-dire **sans dénominateur** : ni jeu d'épreuves, ni métrique, ni effectif, ni protocole |
| **06** Coordination sans coordinateur | **B** *(nous)* | Les blocs « Mesuré » n'indiquent presque jamais la taille de population, dans un chapitre dont le sujet est l'échelle | La **borne supérieure de fait est *n* = 64** — le banc mesure 599 s simulées/s-cœur à *n* = 64, 15,2 à *n* = 1 000, et déclare bloqué l'usage à *n* = 12 500 que le traité prend pour exemple. Aucun des cinq écarts n'est établi au-delà de *n* = 100, le plus lourd l'est à *n* = 24. Les *n* des phases 3, 4 et 6 **ne sont publiés dans aucun document** — ni PRD, ni SPEC, ni VERDICT : ils ne se lisent que dans les tests. Et le scénario C **ne simule rien**, il applique une formule avec 5 % de bruit |

**Deux erreurs trouvées dans le compendium lui-même**, et qui ne sont donc pas des défauts de la
recension : le ch. 43 annonce « les huit principes directeurs du blueprint » là où le ch. 45 en pose
six ; et le dénominateur du « ×15 jetons » diverge à l'intérieur du dépôt — « un agent unique » au
Vol. I §2.11.1 et §4.9.4, « une simple conversation » au §2.8.1 et §4.6.1. *Le rapport ne les
propage pas.*

---

## Tours 1 et 2 — pièce 02, et le contrôle qui vaut

**Verdict : A** *(nous)* — **en position retournée et avec la consigne débiaisée**. Le critique a
compté au lieu d'estimer : 51 « ⚠ » pour 4 625 mots chez nous contre 22 pour 11 118 chez la barre,
soit **5,5 fois la densité**, et 275 séquences en gras contre 242. Il a jugé le défaut réel, il ne
l'a pas jugé suffisant : *« il ne suffit pas à renverser l'écart de matière, de profondeur et
d'utilité »*.

**Écart retenu** : le § 2.10 est la seule section sans un seul renvoi, et c'est celle qui porte les
affirmations les plus lourdes — « un arbitrage de type CAP déguisé en question d'identité, dont
aucune des deux pièces en présence ne reconnaît la position adverse », sans que ces deux pièces
soient jamais nommées.

**Reprise** : les trois énoncés nus sont portés, et au même endroit — le front *L'identité, la
délégation et la révocation* de la revue. Les deux positions de l'arbitrage sont Parakhin [75], qui
suppose un point de sérialisation partagé, et Deochake [80], qui refuse tout aller-retour à la
vérification et assume une fenêtre résiduelle égale à l'intervalle de battement. Les quatre régimes
européens sont nommés. Le RFC 9964 est rendu à sa portée réelle — il **enregistre des identifiants**
pour JOSE *et* COSE, il ne *normalise* pas les algorithmes, qui le sont depuis le 13 août 2024.
Marqueurs 51 → 12, gras 60,0 ‰ → 21,9 ‰ contre 21,8 chez l'étalon.

**Trouvaille du chapitre** : le RFC 8693 §4.1 admet l'imbrication sans profondeur maximale **et**
proscrit que les acteurs antérieurs entrent dans une décision d'autorisation. *La traçabilité de
bout en bout n'est pas omise, elle est écartée par prescription* — ce qui recadre le problème des
deux sauts comme un choix de périmètre, non une négligence.

**Coût** : 581 k (bâtisseur, la pièce la plus chère de la course) + 108 k + 128 k = 817 k.

---

## Tours 1 et 2 — l'épilogue

**Barre changée, et le motif est de genre** : un épilogue contre un chapitre d'ouverture est un
mauvais appariement. La comparaison s'est faite contre la **pièce de clôture du même compendium**,
`Livre V/49-horizon-frontiere-connaissance-verifiable.md`.

**Verdict : B** *(nous)*. Le critique a compté les deux pièces :

| | la barre (19 111 mots) | l'épilogue (3 506 mots) |
|---|---|---|
| ⚠ | **222** (1 par ~86 mots) | **0** |
| gras | **1 057** (1 par ~18 mots) | **9** |
| avant la première phrase de fond | **1 987 mots** d'en-tête | 0 |
| matière déclarée « à retirer à la publication » | **2 531 mots** | 0 |

Il a vérifié trois renvois de l'épilogue aux chapitres — les trois portent exactement ce qu'on leur
fait dire, ponctuation des chiffres comprise.

**Écart retenu** : un renvoi faux au premier item de « ce que les chapitres se disent entre eux ».
L'épilogue mettait en scène comme correction inter-chapitres une borne que **les deux chapitres
portent déjà** — le ch. 3 restreint le 90,0 % dans le paragraphe même du chiffre.

**Reprise étendue aux huit items**, et l'extension a payé : **quatre autres renvois faux** que le
critique n'avait pas vus — un § omis au titre de l'item 2, une confrontation requalifiée à l'item 4
(le ch. 4 retire un *texte* d'appui, non un *appui*), un cardinal faux à l'item 8 (l'ouverture pose
quatre écarts, pas deux), et un renvoi au ch. 2 qui pointait le § 2.10 pour un fait du § 2.2.

**Coût** : 174 k + 137 k + 194 k = 505 k *(plus une reprise perdue sur expiration de jeton, sans
effet sur les fichiers)*.

---

## Passe de lissage

Un agent neuf, qui n'avait vu aucun tour, a lu les huit pièces ensemble — ce qu'aucun rédacteur ni
aucun critique n'avait fait.

**Ce qu'il a trouvé, et que la boucle ne pouvait pas voir** : le registre typographique divergeait
**d'un facteur vingt** d'un chapitre à l'autre, de 2,4 ‰ de gras à 44,0 ‰. Après passe, les huit
tiennent entre 14,2 et 24,6 ‰, contre 21,8 chez l'étalon ; les marqueurs, de 0 à 12,2 ‰ avant,
tiennent sous 2,9 ‰. *Le balisage a été retiré, jamais les mots* — 22 à 14 spans par fichier ont
été rétrécis à l'identifiant qu'ils contenaient plutôt que supprimés.

Trois autres coutures, invisibles morceau par morceau :

- **Huit déclarations de régime pour un seul ouvrage.** Chaque chapitre rouvrait la leçon que les
  liminaires posent déjà. Retiré ce qui était général, gardé ce qui est propre — l'auto-citation du
  ch. 2, le durcissement `[C]` du ch. 3, l'infraction à D-9 du ch. 4.
- **~200 renvois ambigus**, retagués sur une convention unique : *le document, puis le chapitre,
  puis la section*. Les cas résolus sont ceux qui se lisaient des deux côtés — `§ 4.1` de la veille
  contre `§ 4.1` du rapport, `ch. 8` du traité contre `ch. 8` du compendium, et **deux PRD** qui se
  citaient pareil en portant tous deux un §7 et un §9.
- **Quatre redites au long**, chacune renvoyée à son chapitre de siège : l'incident UNC6395, les
  douze brouillons IETF de délégation, l'auto-arbitrage à 54 %, les scanners MCP à 96,89 %.

**Ce qu'il a refusé de corriger, et il a eu raison de le signaler plutôt que de trancher** — six
points, dont deux repartis en correction ciblée :

1. ⚠ **Deux chapitres annoncent chacun « le minimum » d'auto-arbitrage** et ne peuvent avoir raison
   tous les deux — 4 sur 13 au ch. 1, 2 sur 11 au ch. 3. *Reparti en correction.*
2. ⚠ **Un énoncé faux est sorti par la porte du doublon, non par celle de l'arbitrage** : le ch. 2
   décrivait la veille comme « produite par vérification adverse à trois votants », ce que trois
   autres pièces contredisent — les passes d'août 2026 n'ont aucune ronde adverse. Il a disparu avec
   la redite de régime. *Si l'arbitrage doit être rouvert, c'est là.*
3. Un renvoi de l'épilogue attribuant une formule au mauvais chapitre. *Reparti en correction.*
4. Un renvoi irrésoluble dans les liminaires — `Monographie.md §2.2.4` sans dire de quel volume ;
   le trancher demanderait d'ouvrir une source, ce que le régime du rapport interdit.
5. Deux marqueurs hors système survivent — `☑` et `✎`. La règle donnée ne visait que `⚠` et le gras.
6. L'erreur du compendium sur les huit principes n'est propagée nulle part. *Vérifié sur les huit
   fichiers.*

**Coût** : 436 k.

---

## Correction des deux contradictions résiduelles

Les points 1 et 3 du lissage repartent en correction ciblée, parce qu'ils demandaient d'ouvrir une
source que le lisseur n'avait pas le droit d'ouvrir.

**Le « minimum » d'auto-arbitrage — le ch. 1 avait tort.** La revue écrit, au § *Proposer n'est pas
prouver* : « minimum en gouvernance (2/11) et en protocoles (4/13) ». Elle nomme **deux fronts au
bas** de la distribution ; le minimum strict est la gouvernance, en compte comme en part. Le ch. 1
avait promu au rang de minimum le **second de la paire**. Les deux chapitres portent désormais la
paire complète, chacun avec sa provenance — une seule grandeur, pas deux.

**Le renvoi de l'épilogue.** La formule « exact à son gel et faux dix jours plus tard » est du
ch. 3 § 3.9 ; le ch. 5 § 5.2 porte le même fait en d'autres mots. Le fait garde son renvoi au
ch. 5, la formule va à son auteur.

**Coût** : 119 k.

---

## Assemblage et rendu

`Rapport de l'art.md` — **43 103 mots**, neuf pièces, soixante-neuf sections. Composé en
`Rapport de l'art.pdf` : **101 pages**, dont 97 foliotées, au gabarit du compendium.

**Vérifié sur le rendu, non déclaré depuis la source** : page de titre sur une page, table des
matières où l'avertissement, la mise en contexte et l'épilogue **ne consomment aucun rang** de
chapitre, bandeaux « CHAPITRE N » aux six, titres courants portant le rang de la pièce et le § de la
section courante, sections auto-numérotées à deux et trois termes, tableaux à filets *booktabs*.

---

## Épreuve finale — le rapport contre le rapport purgé

**Le motif de cette épreuve est un aveu.** Sept pièces sur sept ont battu la barre, et toujours sur
le même axe — la provenance au point d'énoncé — qui était **exactement celui que mon prompt de
bâtisseur imposait**. Deux contrôles ont écarté le biais de position et l'avantage de critère, mais
ils ne pouvaient pas écarter le troisième : la barre était un **chapitre**, notre pièce un chapitre
de **rapport dérivé**, et les deux genres n'ont pas les mêmes obligations.

L'épreuve finale les met à égalité : le rapport assemblé contre le
« Rapport de l'art » de 20 437 mots produit le 16 août 2026 puis purgé du dépôt
(`git show 432ac8d:"Rapport de l'art.md"`). **Même commande, même corpus, même genre, même auteur
des travaux sources, aucun avantage de consigne.** C'est la seule comparaison de la course dont le
résultat vaille sans réserve de méthode.

**Verdict : A** — notre rapport. Le motif :

> A est le seul des deux dont on peut aller vérifier les énoncés — chaque affirmation porte son
> livrable, son chapitre, sa section et son régime de preuve —, et mes deux sondages dans A sont
> tombés juste, là où mes deux sondages dans B sont tombés sur un chiffre qui avait perdu ou
> amélioré sa source.

Les deux sondages dans le rapport purgé ont trouvé de vraies fautes : « plus de 950 serveurs au
**répertoire officiel** » là où la veille désigne nommément *le répertoire de connecteurs curé d'un
fournisseur, non le registre*, et publie sa propre mesure par pagination — 21 767 enregistrements,
73 072 sans filtre de version, chiffre que le rapport purgé ne porte nulle part ; et un tableau de
volumétrie servi en ouverture sans réserve avec les cardinaux des **éditions antérieures** — 100 p.
et 303 réf. pour une veille qui en fait 141 et 342.

**Contre l'intuition, c'est le rapport purgé qui est le plus saturé.** Le critique a compté :

| | notre rapport | le rapport purgé |
|---|---|---|
| gras / 1 000 mots | **19,6** | **36,2** |
| italiques / 1 000 mots | 13,2 | 7,0 |
| ⚠ / 1 000 mots | 2,2 | 0,05 |

Notre défaut propre reste réel et il est nommé : 91 marqueurs employés indistinctement pour une URL
morte, une réserve d'auteur, une contradiction non arbitrée et un chiffre périmé.

---

## Tour final — l'écart retenu vise encore la découpe, et il rouvre la boucle

> **Le plan suit le dépôt, pas le champ, et une région entière de l'état de l'art y disparaît.**
> Les six chapitres épousent les Livres du compendium, si bien que ce que le compendium n'a pas
> instruit, le rapport ne le couvre pas — même quand la veille le porte. Conséquence chiffrable sur
> 41 000 mots : « CloudEvents », « event mesh », « UCP », « DMN », « fouille de processus » comptent
> **zéro occurrence** ; « BPMN » en compte **une**. Un lecteur finit le rapport sans savoir que la
> couche la mieux normalisée du champ existe.

C'est le troisième défaut que la boucle impute à **l'arbitre et non aux bâtisseurs** — après la
bande de longueur et l'avantage de consigne. Découper le rapport sur les Livres du compendium était
commode et faux : cela faisait hériter au rapport **le périmètre d'un de ses livrables** au lieu du
périmètre du champ.

**La boucle ne se ferme donc pas sur la victoire.** Un chapitre 7, *La couche installée*, est
instruit **directement depuis la veille**, et l'épilogue sera repris pour en tenir compte.

---

## Tours 1 et 2 — chapitre 7, *La couche installée*

Instruit depuis la veille technologique, non depuis le compendium — c'est le point.

**Verdict : B** *(nous)*, avec la consigne débiaisée. Le critique a vérifié trois faits normatifs
versionnés, et les trois confirment : ISO/CEI 19510:2013 vaut **BPMN 2.0.1 et non 2.0.2** (OMG
formal/13-12-09) ; XES est **IEEE 1849, révisée le 9 août 2023, active jusqu'en 2033** ;
CloudEvents a son cœur **figé en 1.0.2 depuis février 2022**, gradué CNCF le 25 janvier 2024.

Retombée du premier sur la barre : le chapitre 01 du compendium écrit « seule BPMN a été reprise
comme norme internationale (ISO/IEC 19510:2013) » **sans dire que le texte ISO est en retrait d'une
révision**. L'énoncé n'est pas faux, il est périmé d'un cran — exactement le décalage que le
chapitre 7 existe pour porter.

**Écart retenu — le meilleur de la course, parce qu'il est auto-réfutant** : le § 7.1 fondait
l'existence du chapitre sur un balayage lexical du compendium (dix termes, « zéro occurrence »), et
le § 7.9 du **même chapitre** démontrait que ce balayage est faux dans son sens — « UCP » y rend
zéro alors que le protocole y est traité sous périphrase. *Les dix premiers termes n'avaient reçu
que le contrôle dont le chapitre avait lui-même établi l'insuffisance sur le onzième.*

**La reprise a refait le contrôle par objet, terme par terme, et la thèse en sort réduite :**

- **sept des dix** sont absents en sigle *et* en périphrase — XES, IEEE 1849, OCEL, fouille de
  processus, *process mining*, BOAT, Step Functions ;
- **deux sont instruits sous périphrase** — RPA et robotisation, sous « le pilotage d'interface »,
  à trois emplacements datés du compendium, mais **sur leur seul versant agentique** : ni le
  marché, ni ses éditeurs, ni leur reconversion ;
- **un décompte était faux au marqueur même** — le TCK est présent, sigle compris, à l'annexe
  bibliographique.

Le chapitre écrit désormais que le constat qui le fonde en sort **réduit, non renversé**. La reprise
a aussi corrigé une prémisse que je lui avais donnée à tort : R-8/R-13 n'est pas une convention
générale de nommage par description, c'est l'encadré de désambiguïsation d'un seul sigle ; le vrai
générateur de périphrases est la **parade de péremption**, qui retire du corps les dénominations
commerciales et les numéros de version. Et le compendium porte lui-même la règle que le § 7.1
enfreignait : *un décompte d'occurrences porte sur le marqueur littéral de l'identifiant.*

**Coût** : 326 k + 107 k + 168 k = 601 k.

---

## Reprise de l'épilogue — de six chapitres à sept

Six confrontations, dont **quatre neuves**, et deux qui portent sur la méthode du rapport entier :

- **ch. 7 § 7.4 contre ch. 5 § 5.10** — le chapitre 7 ne touche pas au résultat d'impossibilité ;
  il montre que **trois portées disjointes se vendent sous son nom**, plus une quatrième dont le
  fournisseur tait la portée, et que le compendium loge le résultat et une promesse d'éditeur *à
  trois cents pages d'écart sans les confronter*. En retour le ch. 5 borne le ch. 7 : aucune des
  trois portées ne s'achète au niveau protocolaire.
- **ch. 7 §§ 7.1 et 7.9 contre ch. 4 § 4.7** — la **réciproque** de la règle du mot non cherché :
  *un sigle cherché et rendu à zéro ne prouve pas l'absence de l'objet*. Les deux règles se tiennent
  et ont le même effet — chacune retire un appui à qui l'applique.
- **ch. 7 §§ 7.2 et 7.7 contre ch. 1 § 1.8** — le ch. 1 relève qu'aucun protocole agentique n'est
  norme *de jure* ; le ch. 7 montre que la couche voisine en a **deux**, et que ce sont exactement
  ses régions figées. *L'absence relevée est un régime, non un état d'avancement.*
- **ch. 7 § 7.10 contre le ch. 0** — la dissymétrie que ni le ch. 4 ni le ch. 5 ne portaient : le
  moteur de processus produit un artefact qui **précède** l'exécution, l'orchestration d'agents ne
  laisse qu'un appel d'outil dans un journal.

Et la limite de plan est écrite sans atténuation : *le plan a épousé le périmètre d'un livrable au
lieu de celui du champ ; le ch. 7 est la réparation d'un trou que le rapport s'était creusé
lui-même, défaut de méthode et non d'omission — et rien dans l'exercice n'établit que ce trou était
le seul.*

**Coût** : 179 k.

---

## Assemblage final

`Rapport de l'art.md` — **52 361 mots**, dix pièces, quatre-vingts sections. Composé en
`Rapport de l'art.pdf` : **120 pages**. Vérifié sur le rendu : page de titre tenant sur une page
malgré le septième chapitre au colophon, table des matières sur trois pages où l'avertissement, la
mise en contexte et l'épilogue ne consomment aucun rang, sept bandeaux de chapitre, sections
numérotées jusqu'à `7.11`.

---

## Épreuve finale, second tour — sur le tout élargi, ordre retourné

Le rapport à sept chapitres, contre le même rapport purgé, **avec notre pièce en position B** cette
fois. **Verdict : B.** Deuxième victoire à l'aveugle sur le document entier, position inversée.

Le critique a compté : le rapport purgé porte **35 gras pour mille mots**, le nôtre **18,5** — la
saturation de gras est un défaut de l'adversaire, presque du double. Mais il relève le nôtre en
retour : **106 marqueurs contre un seul**, et *« à ce rythme le marqueur ne discrimine plus rien »*.
Ses quatre vérifications : deux des nôtres exactes, deux des siennes fausses — dont, à nouveau, les
cardinaux d'éditions périmées servis sous un gel qu'ils ne portent pas.

**Écart retenu — et c'est la confirmation d'une réserve que le rapport avait lui-même posée** :

> Le droit européen manque entièrement, et c'est le fait corrigé le plus lourd de la source la plus
> fraîche du rapport. « article 50 » : zéro occurrence. « DORA » : zéro. « haut risque » : zéro. Le
> règlement (UE) 2024/1689 paraît une seule fois, pour porter un énoncé du compendium en régime
> faible. Or la veille range parmi les six réfutations qu'elle s'inflige : *la transparence
> européenne s'applique depuis le 2 août 2026, et la Commission y range explicitement les agents —
> première accroche par le texte et non par inférence.* Le rapport laisse tomber **le seul
> instrument opposable du corpus qui nomme l'agentique**, contrepoint direct de son propre § 4.4 où
> le Canada n'accroche que par inférence. **L'épilogue écrit « rien n'établit que ce trou-là était
> le seul » ; il y en avait un second, et il est plus gros.**

---

## Comblement — et le diagnostic est pire que l'écart

La section `§ 4.12 — L'Europe : la seule accroche par le texte, et une échéance déjà échue` porte
désormais l'article 50(1) applicable **depuis le 2 août 2026**, le 2 décembre 2026 rendu à ce qu'il
est — *un délai de grâce de quatre mois pour l'art. 50(2) et les systèmes antérieurs*, non une date
d'entrée —, les pouvoirs de sanction, le report du haut risque par le règlement (UE) 2026/1744,
DORA, et la gradation qui compte : **le règlement ne nomme pas les agents au sens obligationnel** —
une occurrence d'*Agentic AI*, en nomenclature, sans obligation attachée — ce sont les **lignes
directrices du 20 juillet 2026**, instrument **non contraignant**, qui les rangent sous l'art. 50(1)
par un critère de capacité.

> *Ce n'est pas un régulateur canadien qui nomme les agents, c'est un régulateur européen, et pas
> dans son règlement mais dans ses lignes directrices.*

⚠ **Et le diagnostic est plus dur que l'écart ne le disait.** Le compendium **portait** la matière
européenne — son ch. 30 y consacre ses deux premières sections. C'est la **lecture du rapport** qui
n'en avait retenu que le § 30.3, canadien. *Le trou n'était donc pas hérité du compendium ; il a été
creusé par le rapport lui-même.* L'épilogue l'écrit sans l'atténuer, et en tire ce qui suit : **ce
que deux trous trouvés par deux lectures indépendantes établissent sur le nombre de trous restants
est : rien.**

Trois autres corrections du même tour : l'énoncé périmé du ch. 1 § 1.7 rendu au régime de la veille ;
le renvoi du ch. 7 § 7.1 — les cinq chiffres et le renvoi étaient exacts, c'est « l'une des trois
seules » qui était faux, **et la veille se contredit elle-même** entre sa prose (trois passes
nommées) et son tableau (un quatrième lot entier, sans fraction), *divergence consignée et non
arbitrée* ; et un **quatrième** renvoi cassé de l'épilogue, trouvé au-delà des trois signalés.

---

## Clôture

**Livrable** : `Rapport de l'art.md` — 54 929 mots, dix pièces, quatre-vingt-une sections — et
`Rapport de l'art.pdf`, **126 pages**, dont 122 foliotées, au gabarit du compendium.

**Typographie du tout, mesurée sur le fichier assemblé** : **19,4 ‰ de gras et 2,0 ‰ de marqueurs**,
contre 21,8 et 2,0 au chapitre étalon. Les termes que deux critiques donnaient à zéro sont présents :
*article 50* (11), *BPMN* (24), *CloudEvents* (6), *fouille de processus* (6), *OCEL* (4),
*IEEE 1849* (3), *DORA* (2).

**Ce qui a fermé la boucle** : la victoire à l'aveugle, obtenue **neuf fois sur neuf** — sept pièces
contre le chapitre étalon du compendium, l'épilogue contre la pièce de clôture du même compendium,
et deux fois le document entier contre le rapport purgé, en position A puis en position B. Chaque
écart retenu a été soldé par un bâtisseur neuf.

**Ce qui reste ouvert, et le rapport le porte lui-même :**

- ⚠ **Rien ne borne le nombre de trous de couverture restants.** Deux ont été trouvés par deux
  lectures indépendantes ; le second était plus gros que le premier ; aucune des deux lectures ne
  cherchait de trou.
- ⚠ **Un énoncé faux est sorti par la porte du doublon, non par celle de l'arbitrage** — la veille
  décrite comme « produite par vérification adverse à trois votants ». Le lissage l'a retiré comme
  redite ; il n'a jamais été arbitré.
- Un renvoi irrésoluble dans les liminaires, que le régime du rapport interdit de trancher.
- Deux marqueurs hors système, `☑` et `✎`, que la règle de lissage ne visait pas.
- La divergence prose/tableau de la veille sur ses passes adverses, consignée et non arbitrée.

**Coût total** : ≈ **7,5 M tokens** — 2,9 M de bâtisseurs, 0,8 M de critiques, 1,0 M de reprises,
0,5 M pour l'épilogue, 0,6 M pour le chapitre 7, 0,5 M pour les deux épreuves finales, 0,44 M de
lissage et de coutures, 0,6 M pour la section européenne et ses raccords, ~0,25 M d'arbitrage.

**Trois des défauts trouvés visaient l'arbitre, non les bâtisseurs** : la bande de longueur imposée
par morceau, qui faisait supprimer des faits sourcés ; l'avantage de consigne, qui faisait juger la
barre sur le terrain où nous étions préparés ; et la découpe sur les Livres du compendium, qui a
fait hériter au rapport le périmètre d'un de ses livrables au lieu du périmètre du champ. *C'est le
rendement propre de la technique : un bâtisseur ne voit pas la consigne qui le borne, un critique à
contexte neuf la voit.*
