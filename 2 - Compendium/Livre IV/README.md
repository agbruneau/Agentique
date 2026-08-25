# Livre IV — Appliquer, exploiter, produire et composer : AgentMesh, AgentOps, fabrique d'agents et synthèse architecturale

Répertoire de rédaction du **Livre IV** du compendium *Interopérabilité et Orchestration en Entreprise Agentique* (Vol. IV). Il ne porte
aucune décision, aucun socle et aucun garde-fou propre : la spécification de contenu est le
[`PRD/TOC.md`](../PRD/TOC.md), la gouvernance de la rédaction le [`PRD/PRD.md`](../PRD/PRD.md). En cas
d'écart entre une pièce de ce dossier et le TOC, **le TOC prime** — sauf déviation fondée, qui se
déclare (décision 8 du TOC) et **se remonte, jamais se corrige au plan depuis ici**.

## ⚠ Le dépôt est CLOS depuis le 8 août 2026 — et « clos » n'est ni « terminé » ni « publiable »

La décision d'auteur **D-13** ([PRD **v0.17** §16](../PRD/PRD.md), [TOC **v0.33**](../PRD/TOC.md))
**clôt la passe de révision ouverte par D-11** le 30 juillet 2026 — *close, non achevée* — et
**clôt le dépôt entier**. **Trois conséquences pour ce Livre.** *(1)* **Aucune passe n'est plus
prévue**, ni de rédaction, ni de révision, ni d'appareil : ce qui suit décrit un état **définitif**.
*(2)* ⚠ **Rien n'est levé, et rien n'est soldé** : le régime de D-10 ci-dessous est inchangé et
devient définitif, les quatre portes dérogées le restent, **CA-IV-11 et CA-IV-13 demeurent non
satisfaits**. *(3)* ⚠ **Ce qui était dû devient un manque définitif, non une conformité** — *une
dette qu'on cesse de suivre reste une dette ; elle change seulement de nom.* Le domaine non exécuté
est nommé ligne à ligne au [PRD §16.2](../PRD/PRD.md). ⚠ **Le volume a été renommé le même jour**
(décision 20 du TOC) : il s'est appelé *« La somme agentique »* du 23 juillet au 8 août 2026.
⚠ **Une seconde révision de titre a suivi le 25 août 2026** (commit `8b25090`) : le titre du 8 août
— *« Interopérabilité et Orchestration Agentiques en Entreprise »* — devient **« Interopérabilité et
Orchestration en Entreprise Agentique »**. *Aucun mot du corps n'est touché.* ☑ **La passe est
datée** — **D-14** ([PRD §17](../PRD/PRD.md), v0.18) et **décision 21** ([TOC](../PRD/TOC.md)
v0.34) —, ⚠ *mais après son exécution* : la substitution avait précédé la décision, jusque dans le
libellé de la décision 20, depuis rétabli. ⚠ **La clôture est rouverte pour le titre seul**, dans
les termes du PRD §16.4.5.

## ⚠ Le volume est ARRÊTÉ depuis le 29 juillet 2026 — et « arrêté » n'est ni « terminé » ni « publiable »

La décision d'auteur **D-10** ([PRD **v0.15** §14](../PRD/PRD.md), [TOC **v0.31**](../PRD/TOC.md)) arrête
le compendium au statut **RÉVISION FINALE**, sous un **régime de diffusion en bibliothèque personnelle** :
lecture par l'auteur, **aucune mise à disposition d'un tiers**, aucun dépôt public, **aucune
opposabilité**. **Trois conséquences pour ce Livre.** *(1)* **Ses dix chapitres sont arrêtés dans leur
état du 29 juillet 2026** — plus aucune passe de rédaction n'est prévue ; une faute se corrige encore,
mais la correction **rouvre la passe** : elle se recompose (`bash build/build-pdf.sh` depuis
`2 - Compendium/`) et se déclare. *(2)* ⚠ **Rien de ce qui suit n'est levé, et l'écart de portes de ce
Livre — le plus large du compendium — le moins de tout** : **G-1 résiduel, G-4 fond, G-5 balayage et G-6
lots sont clos POUR CE SEUL RÉGIME par dérogation nommée**, leur résidu entier, et **G-5 conditionnait le
Livre entier** tandis que **G-6 et D-8 conditionnaient nommément l'existence du ch. 41** — *la dérogation
tombe à la première diffusion et rouvre tout ce qu'elle couvrait*. *(3)* ⚠ **CA-IV-11 et CA-IV-13 sont
dérogés, non satisfaits** : il n'y a toujours pas de relecteur distinct du rédacteur, et **aucun énoncé
n'est central** au sens de CA-IV-01. *Ne jamais écrire « conforme », « publiable » ni « terminé » —
écrire « arrêté », et renvoyer au PRD §14.* Les pièces sont composées dans
[`Compendium.pdf`](../Compendium.pdf) (**1 000 p.**, cible calée le 9 août 2026 ; 1 114 auparavant) : *composer n'est pas publier.*

## ⚠ État : le Livre est rédigé, arbitré, et toujours non publiable

Le Livre IV compte **dix chapitres** au plan (ch. 37-46), en **quatre mouvements** — appliquer
(ch. 37), exploiter (ch. 38-40), **produire (ch. 41)**, composer (ch. 42-46). **Les dix sont
rédigés** ; ils l'ont été **hors portes**, et ils restent en **brouillon non publiable**.

⚠ **L'écart de portes de ce Livre est le plus large du compendium à ce jour, et il tient à un cumul
plutôt qu'à une porte.** Le Livre I a été écrit avant **G-1, G-2 et G-3** ; le Livre II avant **G-3 et
G-4**. Celui-ci l'est avant **G-3**, **G-4** — préalable déclaré de son premier mouvement — **et G-5**,
⚠ **qui conditionne le Livre entier** ; et son **ch. 41** l'est en outre avant **G-6** et la décision
d'auteur **D-8**, *qui conditionnent nommément son existence*. Il enfreint enfin **l'ordre de rédaction
du PRD §6**, qui plaçait son second mouvement après les Livres I et III.

| | État au terme de la passe d'arbitrage |
|---|---|
| **Remontées ouvertes** | **zéro** — R-IV-38 à R-IV-59 et R-IV-100 à R-IV-109 closes, chacune là où elle fait foi |
| **Portes franchies** | **deux sur sept** — inchangé : **G-2** entièrement ; **G-1 pour le seul volet du Livre I**, dont ce Livre ne bénéficie pas |
| **Porte G-5** | ⚠ **la décision qui la conditionne — D-2 — EST PRISE**, mais **par une autre passe et après cette rédaction** : *le Livre a été écrit avant, et l'arbitrage qui suit ne rattrape pas l'infraction* |
| **Porte G-6 et D-8** | ⚠ **D-8 est prise par cette passe** — *socle non constitué, chapitre maintenu sous réserve*, voir R-IV-51 |
| **Volet résiduel de G-1** | ⚠ **dû, et il l'est plus lourdement ici qu'ailleurs** — **aucun fait périssable des dix pièces n'a été repris à la source primaire** |
| **Socle consolidé** | ⚠ **zéro entrée** — **G-3 n'est pas entamée** |
| **Énoncés centraux au sens de CA-IV-01** | ⚠ **aucun**, dans aucune des dix pièces |
| **Sièges posés** | ⚠ **CINQ, et non trois** — *le décompte publié en était faux* : trois versés à l'appareil le 27 juillet 2026, **deux découverts par l'audit du 28** (voir plus bas) |
| **Statut des pièces** | **brouillon non publiable** — inchangé |
| **Passe de correction du 28 juillet 2026** | ⚠ **douze constats d'audit soldés dans les dix pièces**, dont **dix thèses re-citées par copie** et **les dix champs « Garde-fous balayés » re-mesurés** sous la décision 16 — *aucune porte franchie, aucun statut changé* |

⚠ **Ce tableau est un constat daté et deux de ses lignes ont été DÉPASSÉES depuis — le rappel est du
8 août 2026, il ne réécrit rien.** ☑ **La porte G-3 est franchie le 28 juillet 2026** et le socle
consolidé ne compte plus zéro entrée mais **159**, `S-001`…`S-159`
([`PRD/socle-consolide.md`](../PRD/socle-consolide.md) ; `python PRD/check-compendium.py` → *P1-P8,
sortie 0*). ☑ **La table `SIEGES` porte 26 sièges sur 50 pièces** (`python PRD/check-sieges.py`).
⚠ **Rien d'autre n'a bougé** : *aucun énoncé n'est central au sens de CA-IV-01, CA-IV-11 et CA-IV-13
demeurent non satisfaisables, et les pièces restent un brouillon arrêté, non publiable* — **une porte
franchie n'est pas un ouvrage recevable.**

*Zéro remontée ouverte ne veut pas dire pièce recevable : cela veut dire qu'aucune question n'attend
plus de réponse qui ne soit déjà tranchée.* ⚠ **Et une condition de publication n'est satisfaisable par
aucune passe de ce volume en l'état** : **CA-IV-11 et CA-IV-13 exigent un relecteur distinct du
rédacteur**, que **D-6 ne fournit pas** — *arbitrer n'est pas relire*.

## ⚠ Une collision de numérotation a eu lieu, et elle est consignée plutôt que lissée

**Ce Livre a été rédigé pendant qu'une passe distincte écrivait les Livres III et V dans le même
dépôt, le même jour.** Les trois passes ont numéroté leurs remontées dans une **série unique et
partagée** sans coordination préalable, et **la collision s'est produite**.

| Passe | Plage revendiquée | État |
|---|---|---|
| **Livre IV** (cette passe) | **R-IV-38 à R-IV-59**, puis **R-IV-100 à R-IV-109** | ⚠ **dix numéros renumérotés à la découverte de la collision** |
| **Livre V** (passe concurrente) | **R-IV-60 à R-IV-75** | inchangé — *déjà arbitré au TOC et au PRD* |
| **Livre III** (passe concurrente) | **R-IV-76 à R-IV-99** | inchangé — *la passe avait elle-même détecté et déclaré la concurrence* |

: Répartition finale des plages de remontées, après renumérotation. ⚠ **Aucun numéro n'est partagé.**

⚠ **La renumérotation a porté sur ce Livre-ci, et le motif du choix se déclare** : *les remontées
R-IV-60 à R-IV-75 de la passe concurrente étaient **déjà soldées au TOC et au PRD** au moment de la
découverte ; renuméroter les siennes aurait obligé à réécrire une gouvernance publiée, ce que la
décision 13d du TOC proscrit pour les cartes de correspondance.* **Les dix numéros de ce Livre —
ch. 44, 45 et 46 — sont donc passés de R-IV-60…69 à R-IV-100…109**, *et la correspondance est
ci-dessous.*

| Ancien | Nouveau | Pièce |
|---|---|---|
| R-IV-60 → **R-IV-100** ; R-IV-61 → **R-IV-101** ; R-IV-62 → **R-IV-102** | | ch. 44 |
| R-IV-63 → **R-IV-103** ; R-IV-64 → **R-IV-104** ; R-IV-65 → **R-IV-105** ; R-IV-66 → **R-IV-106** | | ch. 45 |
| R-IV-67 → **R-IV-107** ; R-IV-68 → **R-IV-108** ; R-IV-69 → **R-IV-109** | | ch. 46 |

: Carte de renumérotation des remontées du Livre IV. ⚠ **Elle se chaîne, elle ne se réécrit pas** : *un « R-IV-61 » cité dans une pièce du Livre IV avant cette passe désigne le **R-IV-101** courant ; le même identifiant cité dans une pièce du Livre V désigne une autre remontée, qui n'a pas bougé.*

⚠ **La leçon vaut au-delà de ce Livre, et elle est de méthode** : *une série d'identifiants partagée
entre passes concurrentes **sans allocation préalable** produit une collision silencieuse — **aucun des
contrôles versionnés ne la voit**, `check-toc.py` ne lisant pas les pièces et `check-sieges.py` ne
lisant pas les identifiants de remontée.* **Elle n'a été trouvée qu'en comparant les plages à la
main.**

## Volumétrie réelle — et une leçon symétrique de celle du Livre II

☑ **Mesure du jour : 59 962 mots** de corps pour les dix pièces, relevés le **10 août 2026** par
[`PRD/decompte.sh`](../PRD/decompte.sh), **seule autorité de décompte du volume** — contre une
enveloppe de Livre de **69 000** au TOC, soit **−13,1 %**.

⚠ **Le chiffre publié ici — 56 025 mots au 28 juillet 2026 — ne se reproduit plus, et les pièces de ce
dossier le démentaient déjà** : le champ *Volumétrie cible* du
[ch. 40](40-indicateurs-agentops-finops.md) porte **« réel : 6 080 mots »** là où le tableau
ci-dessous lui attribue **5 564**. Le solde jusqu'à la mesure du jour est postérieur au 28 juillet :
les **figures du barème A ont été posées dans les pièces le 31 juillet 2026**, et la légende de
chacune entre au corps que la commande mesure ; *les dix pièces en portent au moins une.*
**Le cardinal courant d'une pièce se lit à son champ *Volumétrie cible*, jamais ici.**

⚠ **Ce chiffre remplace les 55 249 publiés le 27 juillet 2026, et l'écart a DEUX causes qu'il faut
tenir séparées.** *(1)* **Un mot venait d'une mesure prise avant une retouche du même commit** : le
marqueur de siège du **ch. 45 § 45.6** est passé de « SIÈGE UNIQUE DE CETTE MATIÈRE POUR TOUTE LA
SOMME » (neuf mots) à « SIÈGE DE L'ORGANISATION DE LA FABRIQUE POUR TOUTE LA SOMME » (dix) **après**
le décompte, dans le commit qui le publiait — *la vraie valeur au commit `0fac01c` était **55 250**,
non 55 249.* ⚠ ***Une mesure se prend sur le corpus que le commit produit***, et c'est la règle que
cet écart d'un mot enfreignait. *(2)* **Les 775 mots restants sont ceux de la passe de correction du
28 juillet 2026** — thèses re-citées sous leur forme réalignée, blocs de désalignement reformulés au
passé, identifiants de corpus portés aux cinq lots du ch. 41, renvois de siège écrits. ⚠ **Aucun n'est
du gonflement** : *ils sont tous dans des sections que l'audit a nommées, et **D-4 interdit autant le
gonflement que l'amputation***.

⚠ **La leçon du Livre I a de nouveau été appliquée, et de nouveau elle n'a pas suffi — mais l'écart a
changé de signe.** *Les dix cibles dérivées ont été additionnées **avant la première ligne** et valent
**exactement 69 000**.* **Le Livre I avait dépassé faute d'addition ; le Livre II avait dépassé malgré
elle ; celui-ci reste en deçà malgré elle.** ⚠ **La dérivation n'est donc en cause dans aucun des trois
cas** : *ce qui varie est la matière.*

| Pièce | Cible dérivée | Réel au 27 juill. (publié) | **Réel au 28 juill. (commit)** | Écart à la cible |
|---|---|---|---|---|
| [Ch. 37](37-maillage-agents-point-application.md) | 11 000 | 9 724 | **9 756** | −11,3 % |
| [Ch. 38](38-observabilite-agentique.md) | 6 000 | 5 628 | **5 693** | **−5,1 %** |
| [Ch. 39](39-cycle-de-vie-operationnel.md) | 6 500 | 6 136 | **6 165** | **−5,2 %** |
| [Ch. 40](40-indicateurs-agentops-finops.md) | 6 500 | 5 541 | **5 564** | −14,4 % |
| [Ch. 41](41-fabrique-agents.md) | 5 000 | 3 329 | **3 765** | **−24,7 %** |
| [Ch. 42](42-matrice-protocoles-exigences.md) | 4 000 | 3 529 | **3 529** | −11,8 % |
| [Ch. 43](43-architecture-reference-couches.md) | 6 500 | 5 839 | **5 839** | −10,2 % |
| [Ch. 44](44-formalisation-archimate.md) | 8 500 | 6 016 | **6 016** | **−29,2 %** |
| [Ch. 45](45-blueprint-instancie-cycle-de-vie.md) | 12 000 | 6 751 | **6 781** | **−43,5 %** |
| [Ch. 46](46-instrumentation-feuille-route.md) | 3 000 | 2 756 | **2 917** | −2,8 % |
| **Livre** | **69 000** | 55 249 | **56 025** | **−18,8 %** |

: Volumétrie du Livre IV, aux commits des 27 et 28 juillet 2026. ⚠ **Constat daté et dépassé — ce tableau et les paragraphes d'analyse qui le suivent** — *voir l'avertissement ci-dessus, et la mesure du 10 août 2026.* *L'écart se documente ; il ne se corrige ni par amputation ni par **gonflement** — et c'est la seconde interdiction qui porte ici.* ⚠ **Trois pièces sont inchangées** — ch. 42, 43 et 44 —, *toutes leurs corrections tombant dans l'en-tête ou dans la note de statut, que la commande de décompte exclut du corps.*

⚠ **Les trois plus forts écarts ont trois causes distinctes, et aucune n'est une coupe.**

1. **Ch. 41, −24,7 % — un chapitre sans source ne développe pas.** *Il n'a **aucun volume source,
   aucune entrée de socle, aucun garde-fou assigné** ; ce qu'il produit à la place d'un contenu est
   **cinq lots d'instruction formulés**.* ⚠ **La brièveté y est l'indicateur, non le défaut** : *un
   chapitre sans socle qui atteindrait sa cible aurait produit du plausible.* ⚠ **L'écart s'est réduit
   de −33,4 % à −24,7 % le 28 juillet 2026, et le motif compte** : *la passe de correction a porté aux
   cinq lots **les identifiants du corpus qu'ils doivent instruire** (décision 15 du TOC, alinéa b-iii)
   — **un critère de clôture qui ne nomme pas ses sources est inexécutable**, et le cinquième lot,
   celui du § 41.7, n'avait ni corpus ni critère écrits.* **Aucun fait n'a été ajouté ; ce sont des
   points d'entrée, pas des sources.**
2. **Ch. 44, −29,2 % — le garde-fou de non-redondance mord plus fort ici qu'à sa source.** *La règle
   héritée est : **si l'on retire le mot « ArchiMate » et que la phrase tient encore comme un exposé
   des chapitres amont, c'est une redondance à renvoyer**. Au Vol. I ce chapitre suivait **cinq**
   chapitres ; ici il en suit **quarante-trois**.* ⚠ *Le même garde-fou, appliqué à huit fois plus
   d'amont, retire huit fois plus de prose.*
3. **Ch. 45, −43,5 % — et c'est la leçon propre au compendium.** *Huit de ses quinze sections ont
   **leur siège ailleurs dans la somme** : le point d'application au ch. 37, la trace au ch. 38,
   l'évaluation et la révocation au ch. 39, les points de contrôle et le modèle de maturité au
   ch. 43, le registre des stéréotypes au ch. 44.* ⚠ **Un chapitre d'instanciation dans un compendium
   **renvoie** là où une monographie **développe**.**

⚠ **C'est la leçon symétrique de celle du Livre II, et les deux se lisent ensemble.** *Le Livre II
dépassait de **+24,1 %** au 28 juillet 2026 — **+37,5 %** à la mesure du 10 août — parce que **le
bornage allonge** : un chapitre qui doit dire, à chaque énoncé, ce que sa source démontre et ne
démontre pas est plus long qu'un chapitre qui affirme.* **Celui-ci reste en deçà — **−18,8 %** au
28 juillet, **−13,1 %** au 10 août — parce que **le siège raccourcit** : un chapitre qui renvoie où
un autre a posé est plus court qu'un chapitre qui reconstruit.** ⚠ *Le sens de l'écart n'a pas
changé de signe en treize jours ; c'est la seule chose que la mesure du jour confirme ici.* ⚠ ***Les deux forces jouent dans tous
les Livres ; ce qui change est laquelle domine*** — et **l'enveloppe héritée n'avait budgété ni l'une
ni l'autre.** *La mesure alimente **D-4**, dont le re-calibrage est remis à une passe unique de
clôture sur les cinq Livres.*

## Les dix pièces

| Pièce | Chapitre | Mouvement |
|---|---|---|
| [`37-maillage-agents-point-application.md`](37-maillage-agents-point-application.md) · [`.html`](37-maillage-agents-point-application.html) | Ch. 37 — Le maillage d'agents : du *service mesh* au point d'application (PEP/PDP et *zero trust* agentique) | appliquer |
| [`38-observabilite-agentique.md`](38-observabilite-agentique.md) · [`.html`](38-observabilite-agentique.html) | Ch. 38 — L'observabilité agentique | exploiter |
| [`39-cycle-de-vie-operationnel.md`](39-cycle-de-vie-operationnel.md) · [`.html`](39-cycle-de-vie-operationnel.html) | Ch. 39 — Le cycle de vie opérationnel : évaluation continue, dérive et incident | exploiter |
| [`40-indicateurs-agentops-finops.md`](40-indicateurs-agentops-finops.md) · [`.html`](40-indicateurs-agentops-finops.html) | Ch. 40 — Les indicateurs de l'AgentOps et le FinOps des agents | exploiter |
| [`41-fabrique-agents.md`](41-fabrique-agents.md) · [`.html`](41-fabrique-agents.html) | Ch. 41 — La fabrique d'agents : produire, certifier et réémettre le parc | **produire** |
| [`42-matrice-protocoles-exigences.md`](42-matrice-protocoles-exigences.md) · [`.html`](42-matrice-protocoles-exigences.html) | Ch. 42 — La matrice protocoles × exigences réglementaires | composer |
| [`43-architecture-reference-couches.md`](43-architecture-reference-couches.md) · [`.html`](43-architecture-reference-couches.html) | Ch. 43 — L'architecture de référence unifiée par couches | composer |
| [`44-formalisation-archimate.md`](44-formalisation-archimate.md) · [`.html`](44-formalisation-archimate.html) | Ch. 44 — La formalisation ArchiMate | composer |
| [`45-blueprint-instancie-cycle-de-vie.md`](45-blueprint-instancie-cycle-de-vie.md) · [`.html`](45-blueprint-instancie-cycle-de-vie.html) | Ch. 45 — Le blueprint instancié et son cycle de vie : de Boréalis au portefeuille IBM, puis la naissance, la vie et la mort d'un agent d'entreprise | composer |
| [`46-instrumentation-feuille-route.md`](46-instrumentation-feuille-route.md) · [`.html`](46-instrumentation-feuille-route.html) | Ch. 46 — Instrumentation et feuille de route vers le 1ᵉʳ mai 2027 | composer |

⚠ **Deux de ces chapitres portent deux mouvements chacun** — les **ch. 37 et 45**, issus des **fusions
v0.20** (décision 11 du TOC). *Les deux entrées y sont conservées intégralement, avec leurs deux
thèses ; la rédaction ne les fond pas en une troisième.* ⚠ **Le Livre compte donc **dix chapitres mais
douze thèses**, et c'est le domaine de balayage de la décision 14.**

⚠ **Un chapitre est sans source, et il se lit à un autre régime** : le **ch. 41** est de la **matière
neuve**, « Fusion : aucune », **sans volume source, sans entrée de socle et sans garde-fou hérité
assigné**. *Ne pas le lire au même régime de preuve que ses voisins.*

## ⚠ CINQ sièges posés ici pour toute la somme — et le décompte de trois était faux

| Siège | Pièce | État à l'appareil | Ce qu'il interdit de refaire ailleurs |
|---|---|---|---|
| **Les cinq points de contrôle obligatoires** | **ch. 43 § 43.3** | ☑ versé le 27 juill. 2026 | la liste et sa dérivation des cinq zones de compensation ; les **ch. 37, 38, 39, 41 et 45** y renvoient |
| **Le modèle de maturité et les trois échelles d'autonomie** | **ch. 43 § 43.5** | ☑ versé le 27 juill. 2026 | le croisement par palier et la **désambiguïsation des trois échelles homonymes du Vol. I** — ⚠ *le ch. 39 § 39.6 s'abstient explicitement d'en produire un autre* |
| **L'organisation de la fabrique** | **ch. 45 § 45.6** | ☑ versé le 27 juill. 2026 | la répartition des rôles ; le **ch. 41 § 41.7** y renvoie **sans la reprendre**, *et c'est pourquoi sa table détaillée ne porte aucun marqueur de provenance* |
| ⚠ **La collision « fabrique »** (décision 12c du TOC) | **ch. 43 § 43.1** | ☑ **versé** — *par la passe de gouvernance du 28 juill. 2026 ; présence relevée sur le script le 8 août 2026* | la désambiguïsation des quatre emplois du mot ; le **ch. 41 § 41.1** y renvoie |
| ⚠ **La conformité traçable** | **ch. 44 § 44.6** | ☑ **versé** — *par la passe de gouvernance du 28 juill. 2026 ; présence relevée sur le script le 8 août 2026* | la chaîne *pilote → évaluation → exigence → réalisation → élément exécutable* et son critère d'auditabilité ; les **ch. 45 § 45.14** et **ch. 46 § 46.2.3** y renvoient |

: Les cinq sièges du Livre IV. ⚠ **Le décompte publié le 27 juillet 2026 — « trois » — était faux, et c'est l'audit du 28 qui l'a établi** (constat IV.1).

⚠ **Les deux sièges découverts portaient déjà la forme pleine du marqueur, et c'est ce qui rend
l'omission coûteuse.** *La règle du dossier est que **les trois gestes vont ensemble — la table,
le marqueur, le harnais — jamais deux sur trois** ; ici deux gestes sur trois étaient faits, et le
manquant est celui qui outille l'abstention : **une reconstruction de la désambiguïsation « fabrique »
ou de la chaîne de conformité traçable ailleurs dans la somme passait tous les contrôles.***
⚠ **La passe de correction des pièces n'a PAS versé la table elle-même** — *elle est hors de sa zone* :
elle a **conservé les deux marqueurs mot pour mot**, dont la signature est prise telle qu'elle est
écrite, **vérifié les renvois entrants annoncés** et **écrit celui qui manquait** (ch. 46 § 46.2.3).

☑ **Les trois premiers sont contrôlés depuis la passe du 27 juillet 2026, les deux autres depuis le
commit du 28** — *relevé sur [`PRD/check-sieges.py`](../PRD/check-sieges.py) le 8 août 2026 : les CINQ
sièges de ce Livre sont à la table `SIEGES`, sur un total de 26.* ⚠ **Et le contrôle a trouvé deux défauts réels au
premier passage sur ce Livre**, *avant même le versement des trois sièges alors comptés* : **(1)** le
**ch. 41 portait la signature de forme de l'encadré à quatre branches du ch. 7 § 7.5** — *une table
dont les rangées commençaient par « (a) » à « (d) », sur un tout autre objet* : **renumérotée F1-F4**,
⚠ *car réutiliser la forme d'un siège pour une autre table rend le contrôle aveugle ou bruyant* ;
**(2)** le **ch. 43 touchait la matière du socle IAM sans renvoyer au ch. 3** — *renvoi ajouté au
§ 43.1.2*. **Le second est exactement le défaut que le contrôle existe pour trouver.**

## Les trente-deux remontées — soldées le 27 juillet 2026

Chacune a été **portée là où elle fait foi**, jamais déclarée close sur place : au
[PRD](../PRD/PRD.md) pour une décision d'auteur ou un domaine de porte, au [TOC](../PRD/TOC.md) pour
un réalignement de plan, à l'appareil pour une dette d'outillage. ☑ **Le détail de chaque clôture vit
désormais dans la note de statut de la pièce qui l'avait ouverte**, sous la forme d'une ligne
« ☑ **Issue, 27 juillet 2026 —** … » appendue à chaque remontée. ⚠ **Cette affirmation était FAUSSE
avant le 28 juillet 2026, et l'audit l'a établi** (constat IV.2) : *les dix notes ne consignaient que
les **ouvertures**, jamais les issues, et le seul lieu où elles vivaient était le tableau ci-dessous.*
**Les trente-deux issues ont été portées aux pièces**, une par une, et le décompte a été re-mesuré
— **trente-deux lignes insérées pour trente-deux remontées**.

| Remontée | Ouverte au | Issue |
|---|---|---|
| **R-IV-38** | ch. 37 | ☑ **TOC, décisions 8 et 14** — thèse réalignée : la source **définit** par filiation, elle n'affirme pas que le maillage **est** une réinstanciation ; ⚠ **et le membre « ce qu'il recouvre réellement / en marketing » tombe** — *la source déclare en coût de sa thèse qu'elle n'affirme rien de cet écart* |
| **R-IV-39** | ch. 37 | ☑ **TOC, décisions 8 et 14** — « **le** lieu où le passeport **devient** opposable » devient « **un** lieu où il **pourrait** le devenir, et le seul que l'ouvrage instruise » ; *report que la source avait fait le 21 juill. 2026 et que le plan n'avait pas suivi* |
| **R-IV-40** | ch. 37 | ☑ **close sur constat — D-2 EST PRISE**, *sections dans l'existant, sans chapitre neuf*. ⚠ **Mais elle l'a été par une autre passe et APRÈS cette rédaction** : *le Livre a été écrit avant G-5, et l'arbitrage ne rattrape pas l'infraction — il la solde* |
| **R-IV-41** | ch. 37 | ☑ **PRD, domaine de G-4** — les trois écarts de cardinal hérités (cinq réalisations contre six objets ; quatrième catégorie contre troisième degré ; disponibilité restreinte hors nomenclature) entrent au domaine de la collation de fond ; ⚠ *le compendium ne re-tranche pas un cardinal de son volume source* |
| **R-IV-42** | ch. 38 | ☑ **TOC, décisions 8 et 14** — « dont **le socle de standardisation est** » tombe : *la source écrit que **leur état interdit de parler d'un socle acquis*** ; et « l'AgentOps commence par l'observabilité » est déclaré **ordonnancement d'auteur** |
| **R-IV-43** | ch. 38 | ☑ **TOC** (ligne de sections) **et PRD** (domaine de G-1) — l'alternative binaire *stable/expérimental* est **réfutée par l'échelle à cinq échelons** ; ⚠ **et l'ancre de version du plan est antérieure de deux mois au déplacement qui l'a périmée** — *exactement le défaut que le § 38.2.3 documente chez un éditeur* |
| **R-IV-44** | ch. 38 | ☑ **TOC, Annexe C** — la relève v0.10 est **scindée à son point d'atterrissage** : *le volet **parade** est **couvert en [C]** par le Vol. I et entre à la troisième table des lacunes de couverture ; le volet **thèse** reste un repérage [C] entier, au domaine de G-1* |
| **R-IV-45** | ch. 39 | ☑ **TOC, décisions 8 et 14** — la boucle n'**est** pas la réalisation du quatrième terme : *la source marque sa thèse « Lecture de l'auteur » en totalité* ; ⚠ **et « le passeport certifie » tombe** — *R-01 : il ne figure dans aucune spécification* |
| **R-IV-46** | ch. 39 | ☑ **PRD, domaine de G-1** — les relèves v0.10 (mémoire) et v0.11 (auto-évolution) sont inscrites **avec leur chapitre codestinataire déclaré** : ch. 5 pour l'une, ch. 47 pour l'autre ; ⚠ *leur statut de repérage se rappelle au point d'atterrissage* |
| **R-IV-47** | ch. 39 | ☑ **PRD, registre des corrections dues de G-3** — la **dette de vote de F-92** est constatée **au versement**, et le chapitre consommateur est enregistré au domaine de G-4 |
| **R-IV-48** | ch. 40 | ☑ **TOC, décisions 8 et 14 — thèse TRIPLE réalignée** : borne du corpus rétablie ; « métriques **publiées** … **hétérogènes** » tombe ; ⚠ **et « dérivée des **obligations** » tombe aussi** — *un seul des quatre instruments impose, et confondre les régimes enfreint R-06 du Vol. III* |
| **R-IV-49** | ch. 40 | ☑ **PRD — périmètre de D-9 ÉTENDU** : le **§ 40.4 est inscrit comme troisième dépendant** du lot d'instruction, avec les ch. 25 et 27 ; ⚠ **la clôture du lot conditionne toute proposition de seuil** sur le délai médian de révision et le taux de renversement |
| **R-IV-50** | ch. 40 | ☑ **PRD, G-3** — **l'issue de repli est déclarée** pour les pièces consommatrices de F-92 et F-96 : *reprise à la source primaire, ou réécriture du § 40.1 sur les seules entrées sans dette* |
| **R-IV-51** | ch. 41 | ☑ **D-8 PRISE** — ⚠ **socle non constitué, chapitre maintenu sous réserve, retrait non exécuté** : *la pièce a produit **cinq lots formulés et zéro fait versé**, ce qui est le résultat que la décision attendait ; le retrait reste l'issue si les lots échouent.* **Le blocage est levé pour la rédaction, non pour la publication** |
| **R-IV-52** | ch. 41 | ☑ **TOC, table d'appuis** — « la **série** *Agent Factory* » devient « **un titre** » : *le constat sur pièce établit une publication dont le titre porte l'expression, non une série* ; ⚠ *le seul relevé daté d'un chapitre sans socle méritait d'être exact au mot près* |
| **R-IV-53** | ch. 41 | ☑ **PRD, domaine de G-4** — le **contrôle des adossements mutuels** entre chapitres de matière neuve et chapitres consommateurs entre au domaine ; ⚠ **`check-sieges.py` ne voit pas cette classe** : *il contrôle qu'un siège n'est pas reconstruit, non qu'un renvoi ne boucle pas* |
| **R-IV-54** | ch. 42 | ☑ **TOC, décisions 8 et 14 — thèse DOUBLE** : *(a)* « révèle **où les standards suffisent** » tombe — *la matrice est un tableau de vides et n'en trouve aucun* ; *(b)* « et la grille des cinq questions » est **déclarée addition du compendium** à la ligne Fusion, ⚠ *une addition de plan non déclarée étant indiscernable d'une reprise de source* |
| **R-IV-55** | ch. 42 | ☑ **PRD, spécification de `check-compendium.py` (G-3)** — un **motif de balayage des identifiants de socle non préfixés** est inscrit à construire et à valider par mutation ; ⚠ *ce chapitre est le premier à mobiliser les deux séries F-xx en volume* |
| **R-IV-56** | ch. 42 | ☑ **TOC, Annexe C + PRD, domaine de G-1** — la divergence de date sur la ligne directrice de l'AMF est **maintenue au registre avec sa réserve**, ⚠ *l'arbitrage du cadrage n'ayant aucune autorité tant que la somme n'est pas rédigée* |
| **R-IV-57** | ch. 43 | ☑ **TOC, décisions 8 et 14** — « **et la fabrique d'identité** imposée sous exigence réglementaire stricte » : ⚠ **l'extension est déclarée construction d'auteur à la ligne Fusion**, *aucune des deux sources ne la portant, et « imposé » étant une formule d'obligation que R-06 borne* |
| **R-IV-58** | ch. 43 | ☑ **PRD, domaine de G-4** — le couple « le Vol. I écrit *réglementairement exigé* / le Vol. II établit une **attente** » entre au domaine ; ⚠ **ce n'est pas une contradiction** : *lacune de couverture apparente, et le volume le plus ancien ne se corrige pas* |
| **R-IV-59** | ch. 43 | ☑ **appareil** — les **trois sièges alors comptés** versés à la table `SIEGES`, **harnais de mutation rejoué** ; ⚠ **deux défauts réels trouvés au premier passage**, dont *un chapitre qui touchait la matière d'un siège sans y renvoyer*. ⚠ **Ce que la clôture avait manqué, et que l'audit du 28 juillet 2026 a établi** : *le Livre pose **cinq** sièges, non trois — la collision « fabrique » (ch. 43 § 43.1) et la conformité traçable (ch. 44 § 44.6) portaient leur marqueur sans entrée de table* ; ☐ **leur versement est dû au commit du 28** |
| **R-IV-100** | ch. 44 | ☑ **TOC, décision 8** — les **neuf sous-sections numérotées « 43.1.x » sous le chapitre 44** et la **table de couverture dirigeant vers « § 43 »** sont réalignées ; ⚠ **classe de défaut déjà consignée pour trois passes de structure consécutives** — *aucun des quinze contrôles ne lit les tables détaillées* |
| **R-IV-101** | ch. 44 | ☑ **PRD, volet résiduel de G-1, DOMAINE DÉCLARÉ** — la **re-vérification du mécanisme d'extension sur le document normatif** est inscrite avec son domaine : *liste des éléments retirés ou renommés, mécanisme d'extension, état du support d'outillage*. ⚠ **Le blocage tient pour la publication du § 44.1.9 et, par dépendance, du ch. 45** : *le registre reste publié sous réserve* |
| **R-IV-102** | ch. 44 | ☑ **PRD, G-3** — la **voie d'élévation** est déclarée pour ce chapitre : *lecture des sources primaires que le Vol. I cite*, ⚠ **avec sa borne** — *une entrée sans source primaire tierce reste une thèse attribuée et ne porte jamais un fait central* |
| **R-IV-103** | ch. 45 | ☑ **TOC, décisions 8 et 14** — ⚠ **le désalignement le plus net du Livre** : la thèse écrit « chaque transition jouée **au grain d'un cas** », *quand la source déclare en tête les avoir jouées **au grain générique des mécanismes**, le cas étant joué en une passe unique* ; et « le blueprint **se prouve** » tombe — *la source écrit **épreuve de cohérence**, non réfutation externe* |
| **R-IV-104** | ch. 45 | ☑ **TOC, décision 8** — « § 45.15 — Confrontation **externe** » réaligné sur sa propre note de provenance, qui écrit « confrontation **interne** au corpus » ; ⚠ *désalignement **interne à une entrée du plan**, qu'aucun contrôle de renvoi ni de cardinal ne voit* |
| **R-IV-105** | ch. 45 | ☑ **TOC, décisions 8 et 14** — le quantificateur « **chaque** couche porte son positionnement OO […] et son point d'intégration » est borné : *aucune source ne porte de positionnement, plusieurs couches n'en portent aucun, et la source de l'intégration traite **trois existants**, non huit couches* |
| **R-IV-106** | ch. 45 | ☑ **TOC, Annexe C** — la **lacune héritée du PRD du Vol. II sur le portefeuille instancié** entre au registre **avec son identifiant d'origine**, et son chapitre porteur est confirmé ; ⚠ *une lacune héritée dont le porteur n'est pas rédigé n'avait aucun lieu où être enregistrée* |
| **R-IV-107** | ch. 46 | ☑ **TOC, ligne Fusion** — le **partage 4 → 3** des propriétés instrumentées est **motivé à la ligne Fusion** : *l'objet mesuré — artefact de conception contre comportement en exploitation* ; ⚠ **et la borne est écrite** : *la raison de fond disponible appuie les **quatre**, non les trois* |
| **R-IV-108** | ch. 46 | ☑ **PRD, volet résiduel de G-1, DOMAINE DÉCLARÉ** — les **six jalons externes** entrent au domaine **avec le critère de reprise de chacun** : *une désignation publiée, un arrêté, une ratification, une publication de version* ; ⚠ *un tableau de jalons dont aucun n'est re-daté au gel est daté d'un autre jour* |
| **R-IV-109** | ch. 46 | ☑ **TOC, ligne Fusion** — le **partage avec le ch. 40 est déclaré** : *la grille dérivée d'un côté, l'instrumentation candidate de l'autre* ; ⚠ *deux chapitres qui produisent le même constat sans se déclarer se répéteront à la relecture, ou se contrediront* |

: Les trente-deux remontées du Livre IV et leur issue, au 27 juillet 2026.

### Ce que la clôture a coûté, et ce qu'elle a trouvé

**Cinq constats méritent d'être retenus.**

1. ⚠ **Dix des douze thèses du Livre étaient désalignées, et c'est la proportion la plus élevée des
   quatre Livres arbitrés à ce jour.** *Le Livre II en avait cinq sur treize ; celui-ci en a **dix sur
   douze** — ch. 37 (les deux), 38, 39, 40, 42, 43, 45 (les deux), et le ch. 46 partiellement.*
   ⚠ **Deux seulement résistent à la collation** : *les ch. 44 et 46, dont les thèses sont portées mot
   pour mot par leur source.* **Domaine de balayage déclaré : douze thèses examinées, dix réalignées**
   — ⚠ *le Livre compte dix chapitres mais douze thèses, les ch. 37 et 45 en portant deux chacun au
   titre des fusions v0.20.* *Un cardinal d'écarts sans domaine de balayage est un relevé, pas une
   couverture.*
2. ⚠ **Un désalignement d'une classe neuve est apparu, et il est INTERNE AU PLAN.** *R-IV-100 et
   R-IV-104 ne portent pas sur un écart entre le plan et sa source : **le plan se contredit
   lui-même**.* Au ch. 44, *neuf sous-sections sont numérotées dans la numérotation d'un autre
   chapitre* ; au ch. 45, *un titre de section écrit « externe » quand sa propre note de provenance
   écrit « interne »*. ⚠ ***Aucun contrôle ne voit cette classe*** : *`check-toc.py` porte sur des
   motifs de ligne et ne connaît pas les tables détaillées ; le reste ne lit pas le plan.* **Seule la
   lecture conjointe d'un titre et de sa note l'a montrée.**
3. ⚠ **Une collision d'identifiants entre passes concurrentes s'est produite, et elle était
   invisible aux contrôles.** *Trois passes ont numéroté dans une série partagée le même jour ; dix
   numéros ont été alloués deux fois.* **Aucun instrument versionné ne rapproche deux plages de
   remontées** — *elle n'a été trouvée qu'en comparant les plages à la main*, et **la renumérotation a
   porté sur la passe dont l'arbitrage n'était pas encore publié**.
4. ⚠ **Deux remontées bloquantes, deux réponses opposées — et l'écart est de nouveau de dépendance.**
   **R-IV-51** (ch. 41) est close **par une décision d'auteur qui maintient le chapitre sous réserve** :
   *la pièce a produit ce que D-8 attendait — cinq lots formulés, zéro fait versé —, et le retrait
   reste l'issue si les lots échouent.* **R-IV-101** (ch. 44) est close **par un domaine déclaré et un
   blocage maintenu** : *le registre des stéréotypes reste publié sous réserve, et le ch. 45 en hérite.*
   ⚠ *La première libère la rédaction sans libérer la publication ; la seconde ne libère ni l'une ni
   l'autre.*
5. ⚠ **Une infraction n'a pas été rattrapée par l'arbitrage qui l'a suivie, et il faut le dire.**
   **La porte G-5 conditionne le Livre IV entier**, et la décision **D-2** qui la conditionne **a été
   prise le même jour — par une autre passe, et après cette rédaction**. *Le Livre a été écrit avant.*
   ⚠ ***Un arbitrage postérieur solde une remontée ; il n'efface pas l'ordre dans lequel les gestes ont
   été faits.***

## ⚠ La passe de correction du 28 juillet 2026 — douze constats d'audit soldés dans les pièces

**Sur instruction d'auteur, en réponse à l'audit du 28 juillet 2026, §7 et §3.** La
passe **corrige, elle ne réédite pas** : aucune section n'est ajoutée, aucun fait n'est versé, aucune
thèse n'est réécrite. ⚠ **Elle ne franchit aucune porte et ne change aucun statut** — *le socle
consolidé compte toujours zéro entrée, G-3 n'est pas entamée, CA-IV-13 reste insatisfaite, et les dix
pièces restent un brouillon non publiable.*

| Constat | Ce qui a été corrigé, et où |
|---|---|
| **IV.8** *(le plus gros lot)* | **Les dix thèses réalignées en v0.28 sont re-citées dans les pièces**, **par copie littérale** depuis l'entrée courante du plan — ch. 37 (les deux mouvements), 38, 39, 40, 42, 43, 45 (les deux), **46**. ⚠ **Les ch. 41 et 44 sont les deux seules thèses inchangées** : leur ancrage passe à v0.28 pour dire qu'elles y ont été **re-collationnées**, non qu'elles auraient changé. **Le bloc qui déclarait le désalignement d'origine est conservé, reformulé au passé**, avec la forme v0.25 citée (décision 17 du TOC, alinéa c) |
| **IV.2** | **Les trente-deux issues sont portées aux dix notes de statut**, chacune sous la remontée qui l'avait ouverte |
| **IV.3** | **Les dix points 3 des notes sont réalignés sur l'état final de la passe** — *les cinquante chapitres existent, les renvois internes résolvent contre du texte* —, l'information datée étant conservée comme telle. ⚠ **Neuf mentions du corps** « ch. N n'est pas rédigé » (ch. 38, 39, 40, 41, 46) sont corrigées de la même manière |
| **IV.4** *et T-1* | **Les dix champs « Garde-fous balayés » sont re-mesurés** sous la **décision 16** : cardinal = **marqueur littéral de l'identifiant dans le corps**, en-tête et note exclus ; **le domaine est déclaré sans cardinal** là où le garde-fou est appliqué sans que son identifiant soit écrit. **Les attestations des dix notes** suivent la même règle |
| **IV.7** | **Ch. 38, synthèse** : « le ch. 40 hérite de cet état pour ses **douze** métriques » → le cardinal est cité **dans sa valeur re-mesurée au ch. 40 § 40.1.2, seize** (douze de F-90, quatre de F-95) |
| **IV.5** | **Trois intitulés réalignés** : ch. 39 § 39.4 (« versionner le **mandat protocolaire** »), ch. 46 § 46.2 (« inventaire, encadrement, surveillance »), ch. 38 § 38.2 (« OpenTelemetry »). ⚠ **Quinze autres déviations sont déclarées plutôt que corrigées** — ch. 37 § 37.9 ; ch. 39 § 39.2 ; ch. 40 § 40.3 et § 40.4 ; ch. 41 § 41.3 ; ch. 44 § 44.2, § 44.3, § 44.5 et § 44.9 ; ch. 45 § 45.1, § 45.7, § 45.9, § 45.11, § 45.12 et § 45.14 — *une déviation fondée se déclare* (décision 8), et **la parade de péremption reste en vigueur pour les dénominations commerciales** (décision 15, alinéa a) |
| **IV.9** | **Ch. 45 § 45.4** : « un fait négatif du socle, établi et **central** » → « **déterminant pour la section** », *« central » étant le terme technique de CA-IV-01 que l'en-tête de la même pièce déclare inatteint* |
| **IV.10** | **Ch. 41, synthèse** : « les ch. **42-51** de la numérotation antérieure reviennent » → **les ch. 42-50 redeviennent les ch. 41-49**, *l'état v0.22 étant périmé depuis la fusion v0.23* |
| **IV.1** | **Les deux marqueurs de siège sont conservés mot pour mot** ; **les renvois entrants annoncés sont vérifiés** — ch. 45 § 45.14 existait, **ch. 46 § 46.2.3 a été écrit**. Le versement à l'appareil est **hors zone** et dû au même commit |
| **IV.6** | **La volumétrie est re-mesurée sur le corpus que le commit produit** (tableau ci-dessus), et *l'écart d'un mot est localisé et expliqué dans la note du ch. 45* |
| **III.C.3** *étendu* | **Le renvoi au siège du tri prospectif (ch. 49 § 49.0) est écrit** au **ch. 37 § 37.7** et au **ch. 46 § 46.3** — *les deux seules pièces du Livre qui écrivent « tri prospectif », balayage exhaustif* |
| **T-4** *(décision 15)* | **Les cinq lots du ch. 41 portent les identifiants de leur corpus** — *un critère de clôture qui ne nomme pas ses sources est inexécutable* —, et **le cinquième (§ 41.7) reçoit le corpus et le critère qu'il n'avait pas** |

: Les douze constats d'audit soldés par la passe du 28 juillet 2026, et le geste de chacun. ⚠ **Domaine du balayage des décomptes, déclaré plutôt que chiffré** : *les **dix champs « Garde-fous balayés »** et les **dix attestations de clôture** ont été re-mesurés entrée par entrée ; le cardinal des entrées n'est pas publié ici, faute d'être re-mesurable autrement qu'en les recomptant* — **c'est la décision 16 appliquée à ce README même.**

⚠ **Trois choses que cette passe n'a PAS faites, et qui se déclarent.** *(1)* **Elle n'a touché ni le
TOC, ni le PRD, ni le conspectus du volume** — *un rédacteur ne les corrige jamais, il remonte.*
*(2)* **Elle n'a versé aucun siège à l'appareil** : la table est hors de sa zone, et *attester un
versement qu'on n'a pas constaté serait l'attestation fausse que le dépôt proscrit* — **les pièces
écrivent « dû », pas « fait ».** *(3)* ⚠ **Elle n'a pas re-nommé le corpus** : la parade de péremption
reste en vigueur pour les dénominations commerciales et les versions (décision 15, alinéa a) ; seuls
les trois interdits d'attribution ont été corrigés.

⚠ **Un défaut de rendu a été trouvé par le vérificateur et il vaut d'être connu.** *La thèse du
premier mouvement du ch. 45, copiée littéralement, refermait une borne de gras **sur** le marqueur
« Lecture de l'auteur », que le générateur de page reconnaît avec sa balise fermante :* **le rendu
produisait un gras jamais refermé, sur tout le reste du paragraphe.** *La borne a été rouverte devant
le marqueur — **aucun mot changé, aucun mot ne perdant son gras** — et l'accommodation est déclarée
dans la pièce.* ⚠ ***C'est la règle du dépôt sur les livrables rendus par un pipeline** : n'employer
que le balisage que ce pipeline accepte, et le vérifier sur la sortie.*

## Ce que le Livre couvre — et ce qu'il ne couvre pas

Chaque pièce suit section par section la table des matières détaillée de son entrée au TOC et respecte
sa table de couverture. **Sept arbitrages de périmètre valent d'être connus, parce qu'ils cassent une
table de couverture si on les défait.**

| Matière | Destination | Régime |
|---|---|---|
| Socle IAM pré-agentique et *zero-trust* | **ch. 3 § 3.2-3.3** (Livre I) | **siège amont** — *ni le ch. 37 ni le ch. 43 ne le reconstruisent* |
| Encadré de désambiguïsation à quatre branches | **ch. 7 § 7.5** (Livre I) | **siège amont** — *renvoi à chaque emploi, jamais reconstruction* |
| Socle transposable du maillage de services | **ch. 1 § 1.3.4** (Livre I) | **arrivée** au ch. 37 § 37.1 pour la seule déclinaison agentique ; ⚠ *le coût mesuré du modèle latéral **reste au ch. 1** et ne se transpose pas* |
| Défenses architecturales et garde-fous d'exécution | **ch. 6 § 6.5** (Livre I) | **partage déclaré aux deux bouts** — *posés là-bas, appliqués au ch. 37 § 37.6* |
| Fondements de l'évaluation, et le §2.9 du Vol. I | **ch. 6** (Livre I) | **hors périmètre** des ch. 38 et 39 — *seul le §2.9.6 arrive, en **seule affectation*** |
| Propagation du contexte de trace | **ch. 38 § 38.3** | **prélevé au ch. 9**, *qui déclare la sortie à son bout* |
| Métrique d'horizon de tâche déléguée | **ch. 40 § 40.3** et **ch. 49 § 49.13** | **partage déclaré** — *la métrique et son état ici, l'énoncé de recherche là-bas* |

⚠ **Et trois matières que le Livre déclare sans les traiter.** *(a)* **La couche d'exécution — le
harnais** : *le **ch. 41 § 41.8** écrit qu'il n'est traité par aucun chapitre*, et ⚠ **D-2 a depuis
tranché pour des sections dans l'existant, sans chapitre neuf** — *sections que ce Livre n'a pas
écrites, ayant été rédigé avant.* *(b)* **L'accord entre agents sous asynchronie et défaillance
partielle** : ⚠ **D-7 a fermé le ch. 37 à cette matière** — *y ajouter une section rouvrirait la
décision, non le seul chapitre.* *(c)* **Le biais d'automatisation et la supervision de façade** : *le
**ch. 40 § 40.4** propose deux indicateurs **sans seuil**, et **s'inscrit au lot de D-9 comme troisième
dépendant*** — ⚠ *mesurer la révision n'est pas mesurer le discernement.*

## Les deux formats

Chaque pièce existe en **deux rendus**, versionnés ensemble — ⚠ **et depuis la purge du 29 juillet 2026 ils ne portent plus la même matière** :

- le **`.md`** — la source ; **c'est lui qui fait foi**, et **lui seul porte l'appareil** : en-tête à cinq champs, thèse citée depuis le TOC, note de statut ;
- le **`.html`** — page autonome à thème sombre orange, **sans aucune ressource externe**, prose
  justifiée avec césure, navigation de chapitre, barre de progression, styles d'impression. ⚠ La
  césure s'appuie sur l'attribut `lang="fr-CA"` : *le retirer désactiverait la coupure des mots **sans
  prévenir**.*

⚠ **Le `.html` est un rendu, pas une seconde source.** Toute correction se fait dans le `.md` puis se
**régénère** :

```bash
python .claude/skills/chapitre-compendium/scripts/rendre-piece.py "2 - Compendium/Livre IV/<pièce>.md"
```

```bash
python .claude/skills/chapitre-compendium/scripts/verifier-piece.py "2 - Compendium/Livre IV/<pièce>"
```

Puis les contrôles du volume, **chacun exécuté seul**, sortie 0 exigée :

```bash
python "2 - Compendium/PRD/check-toc.py"
```

```bash
python "2 - Compendium/PRD/check-sieges.py"
```

```bash
sh "2 - Compendium/PRD/decompte.sh" --verifier
```

⚠ **Le vérificateur ne se tuyaute jamais dans un enchaînement `&&`** : le code de sortie du dernier
maillon masquerait son échec. *La faute a déjà été commise sur le ch. 6 du Livre I.*

## Avant d'ajouter ou de reprendre une pièce ici

**Le skill de projet `chapitre-compendium` portait
la procédure complète.** ⚠ **Il n'est plus au dépôt depuis le 31 juillet 2026** (commit `41666d0`), non
plus que ses scripts : les invocations ci-dessus ne résolvent donc plus. Ce qui suit est le seul rappel
qui subsiste, avec **les quatre points que cette passe a payés**.

1. Lire l'entrée du chapitre au
   [`TOC.md`](../PRD/TOC.md) : thèse, sections, ligne Fusion, table détaillée, table de couverture.
2. **Lire l'intégralité du périmètre de fusion** — leçon reconduite, et **ce Livre l'a payée au
   ch. 44**, dont la source unique est un chapitre entier d'un volume qui entre en [C].
3. ⚠ **Comparer la thèse du TOC au texte rédigé de sa source avant d'écrire.** *Dix thèses sur douze
   étaient désalignées* : la pièce cite verbatim et **écrit son corps sous la forme bornée**, mais le
   repérage se fait **avant**, pas à la relecture.
4. ⚠ **Lire aussi le plan CONTRE LUI-MÊME.** *Deux désalignements de cette passe sont **internes à une
   entrée du plan*** — une numérotation de sous-sections dans un autre chapitre, un titre qui
   contredit sa propre note de provenance. **Aucun contrôle ne les voit.**
5. ⚠ **Vérifier l'allocation des identifiants de remontée avant d'en ouvrir un.** *Trois passes
   concurrentes ont numéroté dans une série partagée le même jour, et dix numéros ont été alloués deux
   fois.* **Aucun instrument ne rapproche deux plages.**
6. ⚠ **Ne jamais réutiliser la forme d'un siège pour une autre table.** *Le ch. 41 portait une table à
   quatre rangées « (a) » à « (d) » sur un tout autre objet que l'encadré du ch. 7 § 7.5 :
   `check-sieges.py` y a lu une reconstruction.* **Il a eu raison de la signaler.**
7. Porter l'en-tête à cinq champs du PRD §6, **garde-fous à zéro occurrence compris**, puis la thèse
   citée depuis le TOC.
8. **Un siège neuf s'ajoute à la table `SIEGES` de [`PRD/check-sieges.py`](../PRD/check-sieges.py)**,
   la pièce porteuse écrit son marqueur, **et le harnais de mutation se rejoue** — *les trois gestes,
   jamais deux sur trois.*
9. Écrire le `.md` et le `.html` **dans la même passe**, faire passer les huit contrôles, et les
   committer ensemble.
