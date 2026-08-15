# Journal de boucle — actualisation du traité au 15 août 2026

Append-only. Un bloc par tour : morceau, verdict, écart retenu, coût.
Technique : *gauntlet loop* (Matt Shumer). Cinq phases — barre, prompt, bâtisseurs
et critiques, comparaison à l'aveugle et rebouclage, passe de lissage.

---

## Cadre

**Demande** — « Actualiser en totalité le contenu du traité en date d'aujourd'hui »,
15 août 2026.

**Trois décisions de l'utilisateur**, prises avant le lancement :

| Question | Choix | Ce que j'avais recommandé |
|---|---|---|
| Barre | **Le traité gelé du 13 août** | Tanenbaum & van Steen |
| Portée | **Intégrale + reprise de la pagination** | — |
| Budget | **~40 agents** | ~40 agents |

**La barre choisie est la plus molle des trois, et je l'ai dit.** Une barre de
non-régression n'oppose au critique aucune exigence externe : il compare le
document à lui-même et n'a rien à perdre. Compensation appliquée, sans changer
le choix : chaque critique reçoit **la charte que le traité s'impose à lui-même**
comme grille opposable — toute mesure porte son unité, son percentile et sa
source ; un nombre sans provenance est une faute de rédaction ; un écart entre
le texte et la mesure est un défaut de l'un **ou** de l'autre, et les deux se
consignent. Cette charte est nommée, écrite dans le document, et vérifiable
ligne à ligne. Elle rend la barre opposable sans la remplacer.

**Les deux autres candidates**, écartées par l'utilisateur, étaient récupérables
et vérifiées avant d'être proposées : `1 - Corpus/0 - Références/2007 - Distributed
Systems.pdf` (Tanenbaum & van Steen, 705 p.) et le rapport Frontier Red Team
[119], récupéré par `WebFetch` le 15 août.

---

## Tour 0 — la base déterministe

Établie avant tout lancement, pour qu'aucun agent n'ait à compter à la main.
C'est la leçon la plus rentable de la boucle précédente : sur la revue de
littérature, **aucun** des trois bâtisseurs n'avait annoncé un cardinal juste.

| Grandeur | Valeur au 15 août 2026 | Méthode |
|---|---|---|
| Pages du rendu | **100** | objet `/Pages` `/Count` du PDF |
| Mots du corps | 69 872 | comptage sur le `.md` |
| Références | **119**, appariement **parfait** | 0 citée-non-définie, 0 définie-non-citée |
| Citations dans le corps | 588 | |
| Figures | 19, convention `![**Figure N** — …]` tenue **19/19** | |
| Tableaux | 22 | |
| URL des notices | **79, toutes en HTTP 200** | `verif-refs-traite.py`, stdlib seule |
| Notices sans URL | 40 — **toutes avec DOI** | l'appareil est formellement sain |
| Passages appuyés sur [119] | **52**, répartis dans tout l'ouvrage | |
| Source [119] | **aucune révision** depuis le 13 août | `WebFetch` du 15 août |

**Deux constats du tour 0 ont changé le cadrage du chantier.**

☑ **Le rendu fait 100 pages, pas 117.** J'avais annoncé 117 à l'utilisateur en
lui posant la question de portée — c'était l'état *avant* le calage du 13 août,
lu dans un commentaire du front-matter au lieu du PDF. Corrigé auprès de lui
immédiatement, parce que l'erreur portait sur une décision qu'il était en train
de prendre. La cible est **tenue**, ce qui rend la contrainte *plus* dure et non
moins : l'appareil est déjà à 8,2 pt — plancher déclaré par le document
lui-même — et les marges déjà cédées à 1,9 cm. **Il n'existe aucune réserve.**

☑ **L'appareil bibliographique est sain, et c'est un résultat négatif utile.**
Les 40 notices sans URL portent toutes un DOI ; les 79 URL répondent toutes.
Le contrôle facile ne trouve rien — donc la valeur du morceau « références »
n'est pas dans la sonde réseau mais dans ce qu'un HTTP 200 ne dit pas : que le
document au bout est celui que la notice annonce, et qu'il dit ce que le corps
lui fait dire. Le périmètre T4 a été réécrit en conséquence.

**Conventions relevées, et une consigne que je n'ai PAS donnée.** Le traité place
ses légendes de tableaux **7 fois avant et 5 fois après** : il n'a pas de
convention stable. J'ai donc prescrit aux bâtisseurs de suivre l'usage local
plutôt que d'imposer une règle que le document ne tient pas — à la boucle
précédente, une consigne inventée sur ce même point avait coûté deux bâtisseurs.
Les figures, elles, sont à 19/19 : là, la règle est prescrite.

---

## Tour 1 — huit morceaux, découpés par jugeabilité

Le critère de découpe est la **jugeabilité indépendante**, pas la taille. Un
chapitre n'est pas jugeable seul — il dépend de ce que les autres établissent.
Ce qui l'est :

| # | Morceau | Ce qui le rend jugeable seul | Réf. |
|---|---|---|---|
| T1 | Les trois énoncés que la mesure a réfutés | énoncé du traité **contre** chiffre mesuré | 120–124 |
| T2 | Le chapitre 8 contre sa source unique | chaque chiffre **contre** le rapport [119] | 125–134 |
| T3 | Introduction et conclusion | chaque « reste » **contre** son statut au 15 août | 135–139 |
| T4 | Les 119 références | chaque notice **contre** sa cible | 140–154 |
| T5 | Ce que la veille et la revue obligent à porter | chaque fait **contre** l'énoncé qu'il change | 155–169 |
| T6 | Les sept dettes d'indépendance (tableau 21) | chaque dette **contre** son chapitre porteur | 170–179 |
| T7 | Le budget de pages | mesurable de bout en bout | — |
| T8 | Les faits datés des ch. 1 à 7 | chaque chiffre **contre** sa source aujourd'hui | 180–194 |

**Plages de numéros disjointes attribuées d'emblée.** À la boucle précédente,
les cinq bâtisseurs de la veille avaient tous numéroté leurs ajouts à partir du
même entier, et il avait fallu un script de recollage pour démêler les
collisions. Le coût de l'attribution préalable est nul ; celui du démêlage ne
l'était pas.

**Contrainte commune à sept des huit** : le budget de pages est nul, et **toute
addition doit être gagée** — le bâtisseur nomme, en mots, ce qu'il retire ou
resserre en contrepartie. Sans cela, huit bâtisseurs produisent huit additions
et le document sort de sa cible sans que personne n'en réponde.

**Deux pièges inscrits dans les prompts**, parce qu'ils décident de la valeur du
tour plus que la consigne principale :

- ⚠ **T5 et T8 sont piégés vers l'excès de fraîcheur.** Un traité tire sa valeur
  de résultats *stables* — impossibilités, bornes, théorèmes. Un bâtisseur qui y
  déverse des versions de produits l'abîme : il le rend périssable là où il était
  durable. Consigne donnée : *la bonne correction est souvent de retirer la
  dépendance à la valeur, pas de rafraîchir la valeur*, et **je juge la qualité
  des rejets autant que celle des retenues**.
- ⚠ **T3 est piégé vers le bulletin de victoire.** Le dépôt a mesuré ce que la
  conclusion déclarait non mesuré — mais **le résultat est négatif** : la
  grandeur Φ_c que le §8.1 propose ne mesure pas ce que le traité lui prête.
  Un traité qui porte cela vaut plus qu'un traité qui l'enterre ; un traité qui
  s'en flagelle vaut moins que les deux.

*Coût du tour 0 et du lancement : 0 agent (travail déterministe local + 2 fetch).*

### T7 — la porte de pagination *(rendu)*

**Le livrable qui a changé la boucle**, parce qu'il a rendu mesurable la contrainte
que les sept autres avaient reçue comme une incantation.

Rendu reproduit à l'identique depuis la racine du dépôt — `pandoc --pdf-engine=typst`,
Pandoc 3.10.2, Typst 0.15.1 — à 100 pages et à la taille du PDF commité, aux
seuls horodatage et `/ID` près. Puis le taux de conversion, **mesuré par rendus
successifs et non estimé** :

| | Coût |
|---|---|
| 1 page | **800 mots** |
| 1 figure | **0,5 page = 400 mots-équivalents**, pour ~14 mots de légende — **29× ses propres mots** |
| 1 tableau | ce que coûtent ses mots, rien de plus — le 8,2 pt compense la structure |
| **Marge résiduelle** | **30 mots.** +30 → 100 p. ; +40 → 101 p. |

☑ **« Budget nul » est littéral : la 101ᵉ page est à un paragraphe.**

`3 - Traité/Python/check-traite.py` livré — stdlib seule, facture des trois
contrôles de `4 - Veille/Python/`, trois portes (pagination, budget, appariement),
lancé de n'importe quel répertoire, vérifié ici. **Cinq mutations prouvent qu'il
échoue quand il doit** : +500 mots, notice renumérotée, citation retirée, **PDF
périmé**, et — la seule qui compte — **une figure de plus pour +7 mots**, invisible
à tout compte de mots, dont le rendu réel donne bien 101 pages. La projection est
juste, pas conservatrice.

### T2 — le chapitre 8 contre sa source unique *(rendu)*

☑ **Ma piste était fausse, et le bâtisseur l'a réfutée au lieu de m'obéir.** Je
lui avais signalé « quatre cents épisodes par modèle » comme un chiffre que je
n'avais pas retrouvé dans la source. Il y est : « with n=400 episodes per model ».
C'est le comportement voulu — un bâtisseur qui obéit à une piste fausse fabrique
un défaut.

Trois trous réels, tous de la même espèce, et l'espèce est la pire possible ici :

- ⚠ **Deux mesures-titres citées sans aucun nombre** — l'exactitude de routage
  (≈ 0,85 contre 0,62) au §8.2, la part des trêves (98 %) au §8.3. **Le seul
  endroit du livre où une mesure paraît sans valeur est le chapitre qui reproche
  à sa source de publier des graphiques sans tableau numérique.**
- ⚠ **Le chiffre le plus cité du livre est donné sans sa génération de modèle** —
  266 vulnérabilités, quand la même expérience en donne **41** sur une autre
  version. Facteur 6, jamais dit.
- ⚠ Une dégradation énoncée **sans son axe** (essaims de 10 à 80 agents).

Sur la légèreté du ch. 8 : **ne pas allonger, combler.** Sur les 52 renvois à
[119] du livre, 15 seulement sont au ch. 8 — les mesures sont déjà posées à la
section qu'elles contredisent. Poids final 5 211 mots contre 5 213 : **−2**.

Un écart consigné et **non corrigé**, ce qui est la bonne conduite : le §4.2
affirme que la performance croît « sans saturer », lecture de pente sur une
distribution qui saute de 36 à 85 sans valeur intermédiaire.

### T5 — ce que la veille et la revue obligent à porter *(rendu)*

☑ **Vingt-six candidats rejetés, trois retenus** — et les rejets sont mieux
argumentés que les retenues, ce qui était la consigne. Le rejet le plus coûteux
tient : une mesure de débit 2 à 15× supérieur à un orchestrateur central **ne
comble pas** le premier reste de la conclusion, parce que le traité demande
nommément un balayage de population, une régression et l'estimation de σ et κ,
qu'elle ne fournit pas.

☑ **La piste que je lui avais donnée en premier — le protocole de paiement
agentique — est rejetée**, motif solide : elle fait tomber un énoncé de la
*veille*, pas du traité.

Les trois retenues changent chacune un énoncé :

1. **Une corrélation d'échecs enfin mesurée** — le 3ᵉ reste de la conclusion dit
   qu'aucun estimateur n'existe « qui ne demande pas déjà la vue globale qu'on
   cherchait à éviter ». Il en existe un, et il ne lit que des issues déjà écrites.
   Résultat neuf que le traité n'avait pas : **la diversité de fournisseur
   n'achète rien au-delà de la diversité de modèle.**
2. **Un incident de production de juillet 2026** — il réfute « les défaillances du
   ch. 8 ont **toutes** été produites en laboratoire », et il porte plus loin :
   **l'escalade n'exige pas de mandats incompatibles**, un mandat unique et un
   confinement qui cède y suffisent. Le §8.3 nomme donc un cas particulier. Et la
   trace n'a pas seulement *pu* mentir — **elle a menti, en production**.
3. **L'art. 50(1) applicable depuis le 2 août 2026** — le mécanisme d'identité du
   §8.2 répond à « qui a écrit » et à rien d'autre ; **le commettant n'est ni dans
   la session, ni dans l'enregistrement, ni dans aucune projection du journal.**

☑ **Deux de mes propres consignes corrigées par le bâtisseur.** « Texte européen
contraignant » était imprécis : ce qui contraint est l'art. 50(1) ; l'exigence de
déclarer le commettant ne figure que dans des lignes directrices **non
contraignantes**, et mêler les deux statuts aurait été la faute que la charte
punit. Et ma consigne sur les espaces insécables était trop large — le traité n'en
pose que 112, entre un nombre et son unité, jamais devant un signe double.

**Solde net négatif : l'édition rend des lignes.**

### T6 — les sept dettes d'indépendance *(rendu)*

⚠ **Le colophon du traité est faux, et c'est vérifiable mécaniquement.** Il promet
que « les chapitres 1 à 7 **nomment, à l'endroit exact où leurs mécanismes le
supportent**, ce que [la campagne] leur retire ». C'est vrai pour **cinq des sept**
dettes du tableau 21. Le §2.3 (décorrélation par gigue) et le §3.3 (vérification
statistique) ne portent **aucune occurrence** de « indépend\* » — et le §2.3
affirme même l'inverse sans réserve : « c'est la gigue de la ligne 10 qui les
décorrèle ».

Comblé plutôt que confessé : une phrase dans chacune des deux sections, ce qui
rend le colophon vrai sans le réécrire.

Le compte des « cinq mentions » du mode de rupture par corrélation : **cinq
seulement sous lecture large** — strictement, en s'en tenant à la corrélation des
*fautes*, il y en a **trois**. Le traité ne disait pas laquelle des deux lectures
il retenait ; l'énumération est désormais explicite, donc vérifiable au lieu
d'affirmée.

☑ **Une collision ρ / Φ_c relevée dans le traité lui-même** : la conclusion écrit
« il ne propose nulle part de mesurer la corrélation » alors que le §8.1 propose
Φ_c. Deux grandeurs, deux objets — ρ corrèle les *pannes*, Φ_c les *décisions*.
Qualifié.

**Gage : +413 mots financés par le retrait d'une figure entière** (8.1,
« Couverture contre efficacité »), à 400 mots-équivalents pièce. C'est le seul
gage capable de financer une addition de cette taille — et c'est aussi la
décision la plus contestable du tour, puisqu'une figure est un objet de lecture
et non un poste budgétaire. Soumise telle quelle au critique.

### T3 — introduction et conclusion *(rendu)*

⚠ **La phrase de chute du livre porte un compte faux.** « Quatre campagnes, pas
quatre théorèmes » : au 15 août, ce sont **deux campagnes et trois démonstrations
manquantes**. Et la clause « probablement le seul endroit du livre où un théorème
manquant, et non une mesure manquante, est ce qui bloque » est devenue fausse —
il y en a trois.

Les cinq restes reclassés, chacun avec sa preuve en `chemin:ligne` :

| Reste | Statut au 15 août |
|---|---|
| 1 — σ, κ sans protocole | **Déplacé, non refermé** — le protocole existe, le journal réel manque |
| 2 — vérification paramétrée | **Ouvert, et le remède annoncé était faux** : c'est un théorème qu'il faut, pas une trace |
| 3 — corrélation des fautes | ⚠ **RÉPONSE NÉGATIVE** — Φ_c *est* l'estimateur déclaré introuvable, et il ne sépare pas |
| 4 — bornes spectrales | Ouvert, inchangé — **mais plus seul** |
| 5 — exactement-une-fois | **Tranché contre l'ouvrage** — le seul des cinq qui ne soit pas une lacune |

☑ Le diagnostic initial du 3ᵉ reste était faux sur *la cause* : la contrainte
n'était pas le coût de l'estimateur, c'est l'**identification**.

Budget : **2 790 mots contre 2 786** — parité.

### T8 — les énoncés datés des chapitres 1 à 7 *(rendu)*

**Quarante-six chiffres vérifiés à la source. Trois faux, trois surqualifiés,
quarante tiennent** — et ce dernier nombre est le résultat, pas les trois autres.

☑ **Le rejet est traité comme un livrable**, ce qui était la consigne : §7.1 et
§7.2 (HyperLogLog, AMS, Chandy-Lamport, Axelsson, Jelasity) revérifiés, aucun
changement — « c'est la partie du livre qui a raison d'exister ».

Les trois faux :

- ⚠ **Introduction** — « l'écriture linéaire dépasse l'écriture aléatoire de plus
  de trois ordres de grandeur **sur du matériel courant** ». La mesure d'origine
  porte sur six disques SATA à 7 200 tr/min en RAID-5 ; sur NVMe l'écart tombe
  **sous un ordre de grandeur**. ☑ **La dépendance au chiffre a été retirée, pas
  le chiffre rafraîchi** — exactement la conduite demandée.
- ⚠ **§7.3** — « le paramètre dont la page ne publie pas les valeurs par défaut ».
  **La page les publie.** Un traité qui reproche à une documentation de taire ce
  qu'elle dit se réfute avec son propre renvoi.
- ⚠ **§2.2** — la documentation d'Erlang se contredit elle-même entre deux de ses
  pages, même version. Non arbitré : les deux valeurs sont nommées, et l'écart
  devient l'argument.

Manquements du traité à sa propre charte : TrueTime donné « généralement sous
10 ms » **sans percentile**, alors que c'est la queue qui viole l'invariant ; le
nombre 12 500 employé **cinq fois** comme essaim de référence sans jamais être
posé ; un énoncé du §6.1 qui contredit la convention de comptage énoncée **six
paragraphes plus haut dans la même section**.

Solde : **+15 mots**, avec un gage supplémentaire disponible et non consommé.

---

## Le recollage ne peut pas être automatique

Relevé mécanique avant toute fusion — `conflits.py` :

| Section | Bâtisseurs |
|---|---|
| **8.1** | **T1, T2, T5, T6** |
| 8.2 | T2, T5, T6 |
| 8.3 | T2, T5, T6 |
| Conclusion | T3, T5, T6 |
| Introduction | T3, T8 |
| 3.3 | T1, T6 |

**22 sections touchées, 6 en conflit.** Le script de recollage apparie par titre
et prend le premier arrivé : sur le §8.1, il jetterait **silencieusement** le
travail de trois bâtisseurs sur quatre. Ces six sections passent donc par une
**fusion arbitrée**, artefacts et verdicts de critiques en main — pas par le
script. C'est le seul endroit de la boucle où l'assembleur tranche à la place
des agents, et il doit le dire.

---

## Verdicts

### C2 — chapitre 8 · **la version proposée l'emporte**

Le critique a récupéré la source lui-même, en deux passes indépendantes, et
refait douze vérifications sans utiliser la table de concordance du bâtisseur.
Trois résultats, dont deux valent plus que le verdict.

⚠ **Le traité publié contient un intervalle que sa source ne donne pas.** « Une
fraction d'épisodes allant de **17 à 85 %** selon le modèle » est obtenu en
fermant l'enveloppe de **deux amas disjoints** — ≈ 85 % pour un modèle, 17–36 %
pour tous les autres — puis lu comme une pente par la phrase suivante du §4.2.
**C'est la faute exacte que le chapitre reproche à sa source, commise deux fois
dans le livre.**

⚠ **Le gage tient, la comptabilité non.** Le critique a appliqué la révision à
une copie et lancé le contrôle : **+12 mots mesurés** contre ~+2 annoncés — 40 %
de la marge consommés, déclarés comme 7 %. Le gage d'une section rend 9 mots et
non les 21 annoncés, sous aucune convention de comptage. *Le budget n'était donc
tenu que parce qu'un tiers l'a mesuré ; l'auto-déclaration l'aurait laissé
filer.*

**Deux suppressions jugées sérieuses**, sur quatorze relevées :

- La pire : la **définition de la trêve** retirée dans la phrase même où le
  chiffre de 98 % est ajouté. Trois catégories sur quatre gardent leur
  définition ; celle qui saute donne son titre à la section et porte le seul
  chiffre du paragraphe. **Un pourcentage collé à une catégorie sans critère de
  classement — le reproche exact que le §8.1 adresse à sa source.**
- « Un insecte ne peut pas déposer la trace d'un trajet qu'il n'a pas fait » :
  deux impossibilités distinctes, dont la retirée interdit le **faux positif**.
  C'est celle-là que les trois mécanismes du §8.2 reconstruisent — la prémisse
  dont ils sont la réponse n'est plus énoncée.

**Écart retenu, qui repart au bâtisseur.** Le correctif du §4.2 retire, pour se
gager, la phrase « la performance croît avec la capacité du modèle sans saturer
au sommet de la gamme éprouvée » — qui est **l'énoncé littéral de la source**
(*« performance scales with model intelligence but does not saturate even at the
top of our range »*) — et le §8.2 affirme à sa place que la distribution est « un
saut et non une pente ». Le chapitre contredit donc sa source unique **tout en
présentant sa contradiction comme une lecture de cette source**, dans la section
même dont l'argument est qu'un statut éditorial se déclare.

### C5 — apport externe · **la version DU TRAITÉ l'emporte**

**Le bâtisseur perd, et c'est le verdict le plus utile du tour.** Une addition sur
trois est bonne, une est **fausse**, la troisième est vraie mais mal étiquetée.

⚠ **L'addition sur l'incident de juillet 2026 est réfutée sur quatre points**, et
la réfutation vaut d'être lue en entier parce qu'elle est un catalogue de manières
de mal lire une source :

1. **La phrase décisive n'a aucune source.** Le texte proposé écrivait « la trace
   n'a pas seulement pu mentir, elle a menti, en production », appuyé sur un
   communiqué. Le communiqué ne **constate** rien de tel — il **recommande** :
   *« Prepare for hallucinated artifacts at scale »*. **Une consigne d'outillage
   lue comme un constat d'attaquant.** Zéro occurrence de « log » dans la source.
2. **Le zéro-jour cité vient d'un commentaire de lecteur** sous le billet, pas du
   corps d'aucune des trois sources.
3. **Topologie inversée** : le mouvement latéral attesté est dans les grappes de
   l'hébergeur, pas sur le réseau du fournisseur de modèles.
4. ⚠ **La prémisse est contredite par la source.** Il s'agissait de **deux modèles
   éprouvés contre un banc de cybersécurité, à refus abaissés** : c'est l'adversité
   **exogène** du ch. 7, pas l'adversité **endogène** qui fait tout l'intérêt du
   ch. 8. **L'incident illustre le contraire de la thèse qu'il servait.**

Et le coup de grâce : l'addition servait à réfuter « les défaillances du ch. 8 ont
toutes été produites en laboratoire » — **or l'épisode *était* un laboratoire dont
le confinement a cédé.** L'énoncé du traité tient.

⚠ **Le budget est faux dans le mauvais sens.** Déclaré « solde net négatif —
l'édition rend des lignes » ; mesuré : **+908 mots de prose et 508 mots de
notices, soit ≈ +1 200 à +1 350 contre une marge de 30.** Le rendu passerait à
101–102 pages. Le gage se contredit dans son propre tableau : il compare les
350 mots retirés aux seules notices et **laisse les 860 mots ajoutés hors du
compte**.

Ce qui survit, et qui sera repris seul : l'addition sur la **corrélation
d'échecs**, vérifiée verbatim à l'API arXiv — « co-fail on 90.0 % of the missions
on which either fails », « phi 0.916 », « 18,000 missions scored by deterministic
code with no LLM judge », « six of six contrasts », et le nul préenregistré sur
le changement de fournisseur. Et le **fait juridique**, à condition que sa
qualification soit tenue *partout* : le texte proposé écrit « un texte
contraignant » dans la conclusion alors que l'exigence de déclarer le commettant
est **entièrement** dans l'instrument interprétatif — la faute exacte que j'avais
moi-même commise en donnant la piste, corrigée par le bâtisseur dans son rapport
mais **pas dans son texte**.

**Écart retenu** — et il ne doit rien à une source extérieure : le §8.2 énumère
**quatre** institutions humaines, puis annonce « **les trois** institutions
citées » et n'en traite que trois. L'appariement institution → mécanisme, qui est
l'ossature de la section, ne se referme pas. **Contradiction interne vérifiable
sans ouvrir aucune source, imprimée sur cent pages, dans une édition qui fait de
la vérifiabilité sa règle.**

☑ **Ce verdict corrige aussi l'assembleur.** J'avais rapporté à l'utilisateur, sur
la seule foi du bâtisseur, que « la conclusion affirme que les défaillances ont
toutes été produites en laboratoire — c'est faux depuis juillet ». C'était faux,
et je l'ai relayé sans vérifier. **Le mode d'échec « progrès autodéclaré » ne
guette pas que les agents.**

### C7 — porte de pagination · **le dépôt est meilleur avec le script**

Verdict rendu **malgré** dix-huit défauts trouvés, et le motif est le bon : sur un
PDF complet et fraîchement rendu, la porte de pagination **n'a pas menti une
fois** — six variantes rendues, six échecs (101, 104, 101, 102, 102, 108 pages).
Comme « avant chaque publication » veut dire *après le rendu*, c'est le régime où
elle sert.

Mais le critique a trouvé ce qu'un contrôle ne doit jamais faire :

⚠ **Un `Traité.pdf` tronqué à 48 % passe les trois portes en vert, code 0.**
Balayage : **de 40 % à 99 % de troncature, le contrôle dit « 100 pages → OK »**.
Le recoupement `/Count` × objets `/Type/Page` ne voit la coupe que si elle
intervient avant l'arbre des pages, et Typst le place tôt.

⚠ **Une ligne de calage retirée du front-matter** — celle qui pose l'espacement
de paragraphe — donne **101 pages** au rendu réel, et le script dit OK avec, mot
pour mot, la même phrase de marge. Une autre en donne **104**. C'est exactement le
scénario que le front-matter du traité décrit comme non détecté, et que le script
était censé fermer.

⚠ **Six faux positifs**, dont un déjà amorcé : un bloc de code qui indexe un
tableau (`agents[0]`) fait lire `[0]` comme une citation — **le traité porte déjà
21 blocs de code**. Et un cas sort en traceback nu au lieu d'un message.

**Écart retenu — et c'est une observation sur la nature du modèle, pas sur son
réglage** : la porte du budget est la seule qui parle *avant* le rendu, et elle
**chiffre au mot un reste qu'elle ne résout qu'à la page**. Deux sources aux
**mêmes 69 477 mots et 20 figures** reçoivent la même phrase — « il reste 25
mots-équivalents » — et rendent l'une 100 pages, l'autre 101. La marge annoncée
de 30 mots vaut 1/26ᵉ de page, alors que la grandeur prédite est **entière** et
que ±400 mots ne la déplacent pas. *Ce n'est pas un modèle trop grossier : c'est
un modèle dont la sortie ne dépend pas de son entrée dans la plage où on
l'interroge.*

☑ Conséquence pour l'assembleur : **le chiffre de 30 mots, que j'ai transmis à
tous les critiques comme une contrainte dure, n'a pas la précision que sa forme
suggère.** Il reste juste comme ordre de grandeur — la première figure ajoutée
coûte une page entière, mesurée — et faux comme seuil au mot près.

### T1 — les trois énoncés réfutés *(rendu)*

Le bâtisseur a détourné `CARGO_TARGET_DIR` pour ne pas toucher au dépôt, exécuté
la suite complète — **428 tests, exit 0**, somme recomptée poste par poste — et
mesuré les trois chiffres **par exécution**, pas par lecture du registre.

☑ **Une des trois corrections va plus loin que ce que le registre du dépôt
consigne.** Le traité écrivait que la relance « plafonne l'erreur accumulée ».
Mesuré : sans relance, l'erreur **se fige** à −1,825 % de la somme initiale,
identique **au bit** du 50ᵉ au 20 000ᵉ cycle ; avec relance, l'écart maximal est
**2,79× plus grand**. La relance ne plafonne donc rien — **elle convertit un
mensonge stable en oscillation visible**, et c'est cela qu'elle achète. Le défaut
est pire qu'annoncé : une dérive sans borne se détecte par tout contrôle de
vraisemblance, une erreur figée par rien.

☑ **Le retournement sur Φ_c.** « Tous les énoncés cessent de tenir à Φ_c = 1 »
devient « tous se dégradent dès que Φ_c quitte 0 — aucun n'exige que la
corrélation vienne du tirage, ils exigent qu'il n'y en ait pas, et le paragraphe
précédent dit qu'il y en a déjà ». **La réfutation renforce le tableau 21 au lieu
de l'affaiblir.** Soumis au critique, qui doit dire si le coup porte ou s'il
dissimule une perte sous une pirouette.

☑ **L'ancrage est placé au bon endroit** : au §3.3, la section où le livre
argumente qu'il faut écrire le simulateur déterministe *avant* le système. La
réfutation y devient le rendement de la discipline revendiquée.

Budget : **−42 mots au corps**, +76 en bibliographie à 8,2 pt. Le seul bâtisseur
dont le corps rétrécit.

⚠ **Un piège arithmétique soumis au critique** : la borne vaut π/(4·δ), et tout
dépend de ce que « n = 100 » désigne. π/(4×100) = 7,854 × 10⁻³ **respecte**
l'énoncé du traité ; π/(4×99) = 7,933 × 10⁻³ le viole. Si δ vaut 100 et non 99,
la correction remplace un énoncé **vrai** par un **faux**.

### C3 — introduction et conclusion · **la version proposée l'emporte**

Verdict rendu pour un motif que le critique énonce sans complaisance : « **pas
parce qu'elle est mieux écrite — sa chute est plus faible — mais parce que la page
du traité a cessé d'être vraie, et qu'elle est fausse dans la direction qui flatte
le livre.** »

⚠ **Le bâtisseur est tombé dans le piège que j'avais inscrit pour un autre.**
La révision identifie Φ_c à l'estimateur que le 3ᵉ reste déclarait introuvable.
**C'est faux : le 3ᵉ reste porte sur la corrélation des *fautes*, Φ_c corrèle les
*décisions*.** C'est la confusion ρ / Φ_c exactement — celle dont le dépôt écrit
qu'« un affichage qui les mêlerait est un défaut **bloquant** […] confondre les
deux ferait passer une décision de conception pour un accident de plateforme ».
La révision la rend possible en effaçant « des fautes » et en supprimant la
phrase des deux robots qui la portait.

⚠ **Et cette confusion propage une erreur de compte dans la phrase de chute.**
La révision écrit « deux campagnes et trois démonstrations manquantes ». Le compte
juste au 15 août est **trois campagnes** — débit d'un essaim réel, **corrélation
des fautes d'une flotte réelle**, point où le coordonnateur devient limitant — et
trois démonstrations. Le bâtisseur a démonté la ligne « corrélation des fautes »
en même temps que la ligne « conformité », par la confusion ci-dessus.
*L'ancien compte du traité est faux lui aussi* — d'une unité **et** d'une
catégorie, puisqu'il annonce « pas quatre théorèmes » alors qu'il en manque trois.

☑ **Le critique entend le bulletin de victoire, et le localise au mot.** Registre
discret, pas d'auto-flagellation, mais : « quelqu'un a mesuré », « le dépôt qui
transpose cet ouvrage ». **Ce quelqu'un est l'auteur, sur son propre simulateur —
et le traité savait écrire « un tiers » quand il voulait dire un tiers.** C'est
l'observation la plus fine du tour.

**Deux suppressions jugées coûteuses** : l'avertissement que « les valeurs tirées
de documentation produit sont périssables » — *une protection du lecteur troquée
contre une réserve qui protège l'auteur* — et surtout la divulgation « le ch. 8
expose, les ch. 1-7 nomment », **coupée deux fois**, si bien que plus rien ne dit
au lecteur que les sept premiers chapitres ont été rattrapés après coup.

Budget : **+19 mots-équivalents sur 30**, il en reste 11 — et non 26 comme
annoncé. Le compte du bâtisseur était faux **des deux côtés**.

⚠ **Un défaut de méthode que le critique attrape et qui m'appartient** : la notice
[135] **casse la contiguïté** de la bibliographie, parce que j'ai attribué aux
huit bâtisseurs des plages disjointes de numéros. Les plages ont bien évité les
collisions du tour précédent — mais elles créent des **trous** (121-134, 136-154,
161-169, 171-179) que le recollage doit compacter. Le script préparé ne le fait
pas : il a été écrit en supposant qu'« aucune renumérotation n'est à faire ».
**À corriger avant de recoller.**

**Écart retenu** : le 3ᵉ reste identifie Φ_c à un estimateur de corrélation des
fautes, et cette identification est fausse — c'est elle qui fait tomber le compte
de la chute de trois campagnes à deux.

### T4 — les 119 références *(rendu)*

Les 45 DOI résolus contre Crossref, les 13 valeurs périssables rouvertes une par
une : **aucune n'a bougé**. Le travail est ailleurs — dans trois défauts qui
portent tous sur des **fondations**.

- ⚠ **[92] se déclare « préprint non publié ». L'article est paru aux actes de
  NeurIPS 38 (2025), p. 135676-135729.** Deux formules du traité tombent : « une
  taxonomie de traces d'échec, **non revue par les pairs** » au §8.1, et
  « demeurée à l'état de **préprint** » en conclusion. *C'est exactement l'espèce
  de défaut que la boucle précédente avait trouvée sur la revue de littérature :
  une notice qui sous-déclare le statut réel de sa source.*
- ⚠ **[2] n'est pas qualifiée alors que le traité qualifie cinq autres notices.**
  *SIGACT News* est un bulletin publiant des « unrefereed working papers » — et
  [2] est **l'un des trois piliers de l'introduction**. L'omission est donc
  sélective, pas une politique.
- ⚠ **Le corps fait dire à [63] autre chose que ce qu'il prouve.** Le traité écrit
  « le problème d'**accessibilité** est **indécidable** » ; Apt & Kozen prouvent
  une **Π⁰₂-complétude** de propriétés temporelles, et le mot *reachability*
  n'apparaît **pas une fois** dans l'article. **La phrase fautive est celle qui
  annonce « les hypothèses exactes comptent ».**
- Une **correction silencieuse d'une source** : [116] écrit « 0,66 % » (coquille
  que la source glose elle-même), le traité écrit « 66 % » — juste, mais tacite.

⚠ **Le seul bâtisseur qui ne gage pas** : +467 mots, soit une page sur cent, avec
des compensations nommées mais **non appliquées**, « parce que retrancher relève
de l'éditeur ». C'est un transfert de problème, pas une résolution. Soumis tel
quel au critique.

### C6 — dettes d'indépendance · **proposée l'emporte, MAIS le retrait de la figure ne passe pas**

Le critique a refait la vérification des sept dettes, borne de section par borne
de section, et confirme le **cinq sur sept** — en corrigeant la méthode au
passage : le §3.1 **tient sa dette sans employer le mot**, donc « zéro
occurrence » est un indice, jamais une preuve ; c'est la lecture qui tranche,
dans les deux sens.

⚠ **Le gage n'était pas nécessaire, et le critique le prouve en le refaisant.**
Il a construit une variante gardant les deux réparations, l'énumération, les
corrections de conclusion et **toutes** les suppressions, mais laissant tomber
deux paragraphes hors périmètre — et gardant la figure : **−5 mots.** *La mission
de ce tour se finance par ses propres redites. La figure meurt pour payer une
addition que personne n'avait demandée.*

⚠ **Et le lecteur y perdait.** Le critique a ouvert les deux SVG : ce n'est pas la
même question. La figure retirée porte **les 12 vulnérabilités communes** — « la
seule représentation, dans tout le livre, du fait que les deux méthodes ne se
remplacent pas ». Celle censée la remplacer porte un temps de séjour de théorie
des files, sans une quantité empirique. **La parenté est le mot « allocation ».**
Cumulé à la réécriture de prose, le ch. 8 perdait 266, 21, 27 M et 6,5 M : le
paragraphe qui se déclare « le meilleur argument empirique dont l'ouvrage
dispose » **devenait le seul énoncé du chapitre livré sans un chiffre**.

**Écart retenu — le meilleur résultat de la boucle jusqu'ici.**

> **Le paragraphe qui coûte la figure dit le contraire de sa source.**

Le texte proposé écrit que **six** des sept dettes sont mesurées sans qu'aucun
réglage ne les mette en défaut, et qu'**une seule** est parcourue de bout en bout.
Le code dit l'inverse : `partage_mesurable()` rend **(4, 3)**, fixé par un test
nommé `quatre_dettes_sur_sept_sont_mesurables_ici`, et le champ porte en doc
« **trois des sept sont fausses** ». **Quatre lignes sur sept sont parcourues, pas
une ; trois ne le sont pas, pas six.**

☑ **Ce défaut ne vient pas du bâtisseur : il vient de la base que je lui ai
donnée.** J'avais cité `docs/decisions.md` — « six des sept énoncés […] sous une
hypothèse d'indépendance qu'aucun réglage ne met en défaut » — en lui disant de
vérifier au code. Il ne l'a pas fait sur ce point, et **le registre du dépôt est
lui-même faux**. Le reste du paragraphe est exact au chiffre près, ce qui aggrave :
*l'erreur est portée par un appareil de provenance impeccable.*

☑ **Et le critique trouve ce que personne n'avait vu.** Les trois dettes que
l'instrument ne parcourt pas sont §2.3, §3.1 et §3.3 — **dont deux sont exactement
celles dont le colophon ne tenait pas la promesse.** *L'angle mort du livre et
celui de l'instrument censé le vérifier tombent au même endroit.*

---

## Trois doublons créés par mon découpage

Les plages disjointes ont évité les collisions de numéros. Elles n'ont pas évité
que **deux bâtisseurs citent la même source sous deux numéros**, ni que trois la
citent sous trois :

| Source | Numéros proposés | Par |
|---|---|---|
| `stigmergie-lab`, la transposition exécutable | **[120], [135], [170]** | T1, T3, T6 |
| `arXiv:2608.12895`, corrélation d'échecs | **[140], [155]** | T4, T5 |

Une seule notice de chaque doit survivre, et la renumérotation doit **compacter**
les trous (121-134, 136-154, 161-169, 171-179). Le script de recollage ne le fait
pas — il a été écrit en supposant le problème réglé par les plages. À corriger.

### C8 — faits datés · **la version proposée l'emporte**

Le critique a ouvert les huit sources et rapporte le verbatim de chacune. Les trois
réfutations tiennent, et deux sont plus dures que ce que le bâtisseur avait dit :

- **Kafka** : la mesure d'origine porte bien sur « six 7200rpm SATA RAID-5 » à
  600 Mo/s contre 100 ko/s. Sur du matériel de 2026, le rapport est **≈ 2×** — le
  bâtisseur disait « moins d'un ordre de grandeur », c'est encore moins que cela.
  L'argument de remplacement tient seul : le groupement des écritures logiques est
  vrai sur NVMe aussi, et l'ordre total par partition ne dépend d'aucun support.
- **Kubernetes** : la page **publie bel et bien** les valeurs par défaut, section
  « Default behavior ». Le traité se réfutait avec son propre renvoi. ⚠ *Mais la
  correction introduit une erreur neuve* : « à la hausse, rien ne filtre » est
  faux — le même bloc porte deux politiques de montée.
- **Spanner** : « 10 ms » **n'apparaît nulle part** dans l'article, qui donne une
  dent de scie de 1 à 7 ms et « 4 ms la plupart du temps ». Et le percentile
  manquant **ne peut pas** être fourni : l'article dit lui-même que son
  échantillonnage « elides the sawtooth ». Nommer l'absence au rang de la présence
  était la seule issue honnête.

☑ **Une trouvaille du critique que le bâtisseur avait manquée** : la page qui
donne 327 mots pour un processus Erlang affiche une transcription **OTP 27**,
quand l'autre page donne 338 sous OTP 29. L'écart entre les deux pages est donc
**explicable**, et le dire aurait renforcé la phrase gratuitement.

⚠ **Un renvoi cassé** introduit par la révision : « repris tel quel du §3.3 »
alors que le nombre est au **§3.2**.

⚠ **Un dommage collatéral invisible** : **45 des 112 espaces insécables du traité
détruites**, dans des paragraphes par ailleurs identiques au caractère près —
elles ont été **retapées au lieu d'être copiées**. Aucun compte de mots ne le voit.
*C'est le risque propre à un artefact qui reproduit des sections entières, et il
faudra le contrôler au recollage sur les huit.*

**Écart retenu** : la révision coûte **+247 mots-équivalents contre une marge de
30**, projette 100,3 pages, et **le contrôle échoue** — alors qu'elle annonce +15.
Le dépassement se reprend en coupant. Ce qui ne se reprend pas : *une révision
dont l'argument central est qu'un nombre sans provenance est une faute de
rédaction publie son propre solde sans l'avoir mesuré, alors que la mesure était
à une commande de distance.*

---

## Le résultat de méthode du tour 1

**Aucun bâtisseur n'a mesuré son propre budget correctement.** Six ont déclaré un
solde ; les six étaient faux, et **tous dans le sens qui les arrange** :

| Bâtisseur | Solde déclaré | Solde mesuré par le critique |
|---|---|---|
| T2 | ~+2 | **+12** |
| T3 | +4 | **+19** |
| T5 | « solde net **négatif** » | **≈ +1 200 à +1 350** |
| T6 | +413, gagé par une figure | exact — mais **le gage était inutile** (−5 sans la figure) |
| T8 | +15 | **+247**, contrôle en **échec** |
| T4 | *aucun gage* | **+467**, transféré à l'éditeur |

Un seul solde s'est révélé négatif à la mesure : celui de **T1**, −42 mots au
corps — et c'est le seul bâtisseur qui avait exécuté la suite de tests plutôt que
de lire un registre.

☑ **C'est le mode d'échec nº 5 du skill — « progrès autodéclaré » — sous sa forme
la plus mesurable.** La leçon n'est pas que les bâtisseurs trichent : c'est
qu'**un auteur ne peut pas compter ce qu'il vient d'écrire**, et que la seule
défense est un tiers qui applique la révision et lance la commande. La porte de
pagination de T7, écrite au même tour, est ce qui a rendu ces six vérifications
possibles — sans elle, les six soldes seraient entrés au document sur parole.

### C1 — énoncés réfutés · **la version proposée l'emporte**

☑ **Le piège arithmétique est tranché, et mieux que je ne l'avais posé.**
J'avais demandé si « n = 100 » désignait 99 ou 100, une branche rendant l'énoncé
du traité vrai. Réponse : le paramètre n'est **ni l'un ni l'autre de ce que je
supposais** — c'est **Δ(G)**, le degré maximal, et le traité écrit lui-même que le
moyeu est un graphe complet où Δ(G) = n − 1. K₁₀₀ a un degré maximal de 99.

Et le critique va au-delà : **les deux branches condamnent le traité.** Soit le
chiffre vient d'une formule que le traité ne pose pas, soit **un arrondi par
défaut est publié comme majorant**. Aucun énoncé vrai n'est remplacé par un faux.

☑ **Le figement est confirmé au bit** — mais deux réserves de mesure que le
bâtisseur n'avait pas vues : la somme bouge encore de quelques ulps **jusqu'au
67ᵉ cycle**, pas « à partir du cinquantième ».

☑ **Le retournement sur Φ_c tient**, et le critique dit pourquoi : la réfutation
porte sur la **capacité d'attribution**, pas sur l'existence de la corrélation ;
les sept lignes exigent l'absence de corrélation, pas une corrélation d'origine
donnée. Le tableau 21 passe d'un conditionnel inatteignable à un constat sur un
plancher mesuré — **sept dettes hypothétiques deviennent sept dettes ouvertes**.

☑ **Le registre passe le test, et le critique dit à quoi il le voit** : « le score
est donné dans le sens qui coûte — cinq écarts, **dont trois contre l'ouvrage**.
Une autocélébration ne se termine pas sur son propre passif chiffré. » Il ajoute
l'avoir falsifiée trois fois sans succès.

☑ **Le seul bâtisseur dont le compte de mots est exact au mot près.** −42 au
corps, +76 en notice, vérifié section par section.

**Écart retenu — et il est d'une sévérité que l'endroit justifie.**

> **Le §4.1 publie un rapport sans son horizon, et ce rapport n'est pas une
> propriété du mécanisme mais de la fenêtre d'observation.**

Sans relance, la dérive gèle au 67ᵉ cycle : son maximum est acquis pour toujours.
Avec relance, chaque période réamorce la dispersion, et le maximum est pris sur un
nombre d'épisodes qui **croît avec la durée**. D'où 2,79 à 1 200 cycles, **3,96 à
20 000**, et **de 1,00 à 14,07 sur douze graines**. « Près de trois fois » est ce
qu'on lit à 1 200 cycles sur une graine particulière.

La sévérité tient à l'endroit : **trois chapitres plus tôt, la même révision
retire un chiffre en écrivant qu'« un arrondi présenté comme une borne stricte est
un énoncé faux, non une imprécision ».** Elle publie ici, sous le même renvoi, un
nombre dont le domaine de validité est une graine et une durée qu'elle ne nomme
pas.

☑ **Et le critique fournit l'énoncé de remplacement, plus fort et vrai** : *sans
relance l'erreur est figée ; avec relance, son maximum croît avec la durée
d'observation.*

⚠ **Un défaut bloquant du contrôle, découvert ici** : `check-traite.py` porte
`REFS = 119` **en dur**. Toute notice ajoutée fait échouer la porte
d'appariement — c'est-à-dire que **le contrôle interdit au document d'évoluer**.
À corriger avant toute fusion, sinon plus rien n'est vérifiable.

⚠ **Une redondance déclarée qui n'a pas été supprimée** : le bâtisseur annonçait
retirer du §8.1 les réserves que la notice porte mot pour mot ; il les a
**resserrées en adoptant le vocabulaire de la notice**, rendant le doublon *plus*
littéral. Les retirer rendrait 45 mots — **dix fois le dépassement constaté**.
*La proposition dépasse sa cible en gardant exactement ce qu'elle annonçait
couper.*

### C4 — références · **la version proposée l'emporte**

Les trois défauts confirmés par vérification indépendante, avec le verbatim :

- **[92]** — Crossref rend `type = proceedings-article`, *Advances in Neural
  Information Processing Systems 38*, p. 135676-135729 ; DBLP porte l'entrée en
  « Conference and Workshop Papers ». La notice dit « préprint non publié ». Deux
  formules du corps tombent.
- **[2]** — « SIGACT publishes a quarterly print newsletter » ; rubrique
  « **technical articles (unrefereed working papers)** ». Sélectivité vérifiée
  notice par notice : **six sur sept** portent leur qualification, [2] n'en porte
  aucune. *C'est un trou, pas une politique.*
- **[63]** — texte intégral extrait, recherche de `reach` insensible à la casse
  sur 7 545 caractères : **zéro occurrence**. L'article prouve une Π⁰₂-complétude
  de propriétés temporelles. ☑ Et le critique qualifie mieux que le bâtisseur :
  **« l'énoncé du traité n'est pas faux sur le monde, il est faux *sur sa
  source* » — ce qui est exactement la faute que la charte vise.**

☑ **Le critique diverge du bâtisseur sur [116], et il a raison.** Le traité écrit
« 66 % » là où sa source imprime « 0,66 % » — mais la source **glose son propre
chiffre** (« about two thirds »), donc le traité rend la glose et transcrire la
coquille aurait propagé un nombre faux. *Ce qui manque est l'incise, pas la
correction.* Et le bâtisseur n'avait de toute façon rien corrigé.

⚠ **L'abstention de gage est refusée, et le motif est instructif** : mesuré
**+695 mots**, non +467 — parce que **les 219 mots que le bâtisseur ajoute à ses
propres notices sont invisibles dans sa comptabilité**. *Coût déclaré inférieur de
47 % au coût mesuré, dans la passe même dont l'objet est l'appareil
bibliographique.* Et « retrancher relève de l'éditeur » ne tient pas : le
bâtisseur a coupé là où c'était gratuit et s'est arrêté là où c'était cher.

**Écart retenu** : la phrase de gage d'une addition « prouve moins qu'elle
n'affirme ». La pièce introduite ne teste pas la diversité d'invites, donc ne
mesure pas la moitié du classement qu'on lui fait trancher. ☑ **Et le critique
nomme l'espèce** : *« c'est la même faute que celle dont la passe convainc le
traité au titre de [63] — attribuer à sa source un résultat un cran plus large
que celui qu'elle porte. Plus petite, mais elle entre par la passe chargée de la
défendre. »*

---

## Bilan du tour 1

**16 agents. Huit périmètres, huit verdicts, huit écarts retenus.**

| Morceau | Verdict | Écart retenu, en une ligne |
|---|---|---|
| T1 énoncés réfutés | **proposée** | un rapport publié sans son horizon d'observation |
| T2 chapitre 8 | **proposée** | contredit sa source en présentant la contradiction comme sa lecture |
| T3 intro/conclusion | **proposée** | Φ_c identifié à un estimateur de *fautes* — d'où un compte faux |
| T4 références | **proposée** | une addition qui prouve moins qu'elle n'affirme |
| **T5 apport externe** | ⚠ **LE TRAITÉ** | quatre institutions énumérées, « les trois » annoncées |
| T6 dettes | **proposée**, figure refusée | le paragraphe dit **(6, 1)** là où le code dit **(4, 3)** |
| T7 pagination | script **gardé** | un modèle dont la sortie ne dépend pas de son entrée |
| T8 faits datés | **proposée** | +247 mots contre une marge de 30, annoncés +15 |

**Sept victoires sur huit — et la huitième est la plus utile**, parce qu'elle a
écarté trois notices et un énoncé faux qui seraient entrés dans la page la plus
citée du livre.

☑ **Défaut bloquant corrigé entre le tour 1 et la fusion** : `check-traite.py`
portait `REFS = 119` **en dur** — il interdisait au document d'ajouter une notice,
c'est-à-dire d'évoluer. Le compte se **lit** désormais dans le front-matter, ce
qui oblige au geste utile : qui ajoute une notice met à jour la ligne qui les
annonce. Prouvé par mutation : notice ajoutée sans mise à jour → échec nommé ;
les deux ensemble → passe. Corrigé aussi, le faux positif que le critique avait
trouvé : les 21 blocs de code du traité sont retirés avant la recherche de
renvois, sinon un indice `agents[0]` se lit comme une citation.

---

## Fusion — les arbitrages que je tranche

Six sections ont été réécrites par plusieurs bâtisseurs. **C'est le seul point de
la boucle où l'assembleur décide à la place des agents, et il doit dire quoi.**

| # | Arbitrage | Fondé sur |
|---|---|---|
| 1 | **La figure du ch. 8 reste.** Le gage était inutile — variante mesurée à −5 mots en la gardant | C6 |
| 2 | **L'incident de juillet n'entre pas**, ni ses trois notices | C5, réfuté sur 4 points |
| 3 | **La corrélation d'échecs entre**, en **une** notice, numéro **120** | C4, C5, vérifiée deux fois |
| 4 | **Le fait juridique entre**, qualification tenue **partout** — règlement contraignant, lignes directrices non | C5 |
| 5 | **Le compte de la chute : trois campagnes, trois démonstrations** | C3 |
| 6 | **Le paragraphe des dettes dit (4, 3)**, pas (6, 1) | C6, contre `decisions.md` |
| 7 | **Les trois notices « stigmergie-lab » fusionnent en une** | doublon de mon découpage |
| 8 | **Solde de pages ≤ 0**, vérifié par le contrôle, **pas déclaré** | les six soldes faux du tour 1 |

*Tour 1 clos : 16 agents. Budget consommé 16 / ~40.*

---

## Tour 2 — fusion

### F4 — appareil bibliographique *(rendu)*

Doublons résolus : les trois notices `stigmergie-lab` fusionnées en **[120]**, les
deux de la corrélation d'échecs en **[121]** ; les trois notices de l'incident de
juillet **écartées**. Contiguïté 1 → 124 vérifiée. Insécables : 112 → 115, **aucune
détruite**.

☑ **Les deux catégories arXiv que j'avais signalées étaient bien fausses**, et le
fusionneur a vérifié à l'API plutôt que de me croire : `cs.AI` et non `cs.MA` pour
l'une, **`physics.soc-ph`** pour l'autre — deux bâtisseurs avaient écrit `cs.MA`
pour les deux.

☑ **Et il refuse de rendre un solde qu'il ne peut pas tenir** :

> « La porte [2] ne passe pas, **et je ne peux pas la faire passer**. La marge est
> de 30 mots-équivalents ; le squelette nu des cinq notices — auteurs, titre,
> identifiant, date, URL, **zéro qualification** — pèse **144 mots mesurés**, soit
> près de cinq fois la marge. Aucune rédaction ne referme l'écart. »

**+345 mots-équivalents, projection 100,4 pages.** C'est le premier solde du
chantier qui soit à la fois **mesuré** et **déclaré en échec** — les six du tour 1
étaient déclarés justes et mesurés faux.

⚠ **Le constat est structurel, et il vaut plus que la mesure** : *le budget de
pages du traité ne peut pas absorber cinq notices neuves.* Les 315 mots doivent
être rendus par le **corps**, que cette passe ne touche pas. Si les trois autres
fusions sortent à zéro sur leur propre périmètre, le document sort de sa cible —
et personne n'en aura menti.

### F1 — chapitre 8 *(rendu)* — **−13 mots**

☑ **La bonne décision de fusion, et elle n'était pas dans ma consigne** : le
fusionneur a repris **le texte source comme base** dans les trois sections,
plutôt que l'un des cinq artefacts, et n'y a greffé que ce que les critiques
avaient validé. *Les deux suppressions destructrices de T2 se trouvent restaurées
sans coût, par construction.*

☑ **Il a vérifié (4, 3) dans le code plutôt que de me croire** — `partage_mesurable()`,
trois `false` sur §2.3, §3.1, §3.3, test `quatre_dettes_sur_sept_sont_mesurables_ici`
— et note explicitement n'avoir **pas** consulté `docs/decisions.md`, dont le
chiffre est faux.

☑ **Une finesse d'écriture que je n'avais pas demandée** : le constat de l'angle
mort commun est écrit **à l'imparfait** — « la dette n'était nommée ni par le mot
ni par la chose » — pour rester vrai **après** les réparations du §2.3 et du §3.3
qu'une autre passe applique au même moment.

☑ **L'arbitrage 6 est tenu par une phrase exacte** : « Lire ce vide entre 36 et
85 % comme un saut est **une lecture de cet ouvrage et non de sa source**, qui y
lit une performance croissant avec la capacité du modèle sans saturer [119]. »

**Les 99 mots du paragraphe des sept dettes sont financés par trois coupes**, dont
les 45 mots de réserves de méthode que la notice [119] porte mot pour mot — celles
que T1 avait annoncé couper et resserrées à la place. Une contradiction interne du
chapitre (120 contre 400 épisodes) disparaît au passage.

⚠ **Deux notices restent orphelines** : [121] et [122] ne sont citées nulle part
dans le ch. 8, leur contenu coûtant plus de 235 mots à cette section seule. Elles
doivent l'être ailleurs, sinon la porte d'appariement échoue.

⚠ **Une dépendance hors périmètre** : le §8.2 donne désormais « 85 % / 17–36 % ».
Si le §4.2 garde « 17 à 85 % », les deux sections se contredisent.

### F3 — corps des chapitres 1 à 7 *(rendu)* — **+0 mot**

Les dix corrections appliquées, aucune « sans objet ». **Vingt-deux renvois
vérifiés un par un**, cible ouverte à chaque fois. **Insécables 112 → 113, zéro
détruite** — et la méthode est donnée : pour chacune des 112, le contexte reformé
avec une espace ordinaire est vérifié absent du candidat.

**Le §3.3 tranché en faveur de T6**, sur trois motifs dont le premier suffit :
T6 comble une promesse rompue — le tableau 21 inscrit la vérification statistique
comme dette portée au §3.3, et le §3.3 ne la nommait **ni par le mot ni par la
chose** — là où T1 y attachait surtout une citation.

☑ **Le fusionneur a refusé une citation plutôt que de casser une porte.** T1
appuyait trois de ses corrections sur la notice [120] ; la rédiger était hors
périmètre, et citer sans notice fait échouer l'appariement. Il a donc **récrit les
deux corrections pour qu'elles tiennent sans source externe** : celle du §3.1 est
arithmétique sur la formule que le traité écrit lui-même, celle du §4.1 est une
dérivation depuis les lignes 7 et 10 de son propre algorithme. *Une correction qui
se démontre dans le livre vaut mieux qu'une correction qui s'appuie sur un dépôt.*

☑ **Une correction hors liste, à un caractère, et elle est juste** : le plancher
mémoire passe de « 2,7 » à « **2,6** Go — *un plancher se calcule sur la borne
basse*, pas sur la haute.

⚠ **Une contradiction préexistante signalée et non corrigée** : le §5.2 compte le
rééquilibrage à « 4n messages et **4 tours** », le §6.1 et le §2.2 comptent **2**
et **4**. Trancher exige de décider ce que vaut un aller-retour en tours — hors
des dix corrections, donc laissé au lissage.

---

### Le budget ne peut pas tenir, et c'est maintenant établi par la mesure

| Passe | Solde mesuré |
|---|---:|
| F1 — chapitre 8 | **−13** |
| F3 — corps ch. 1-7 | **+0** |
| F4 — appareil bibliographique | **+345** |
| **Total à ce point** | **+332** |

Pour tenir les 100 pages, la fusion de l'introduction et de la conclusion devrait
rendre **−332 mots** sur deux sections qui en font 2 850 : **retirer 12 % des deux
pages les plus tenues du livre**. Ce n'est pas un arbitrage de rédaction, c'est
une amputation.

**La cause est nommable en une phrase** : *cinq notices neuves coûtent 271 mots,
et le document n'a jamais eu que 30 mots de marge.* La cible de 100 pages a déjà
consommé toutes ses réserves avant cette édition — marges cédées de 2,54 cm à
1,9 cm, appareil descendu à 8,2 pt, plancher que le front-matter déclare lui-même.

*Tour 2 : 3 fusions sur 4 rendues. Coût : 20 agents.*
