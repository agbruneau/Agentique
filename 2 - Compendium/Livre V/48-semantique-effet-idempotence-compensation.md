# Chapitre 48 — La sémantique d'effet : idempotence, compensation, réconciliation

*Livre V — Livrer et clore : l'agent comme livrable logiciel, horizon et frontière.
Premier mouvement — l'agent comme livrable logiciel : provenance, mise en service, sémantique
d'effet (ch. 47-48). Second et dernier chapitre du mouvement, et **troisième des trois fronts** de
matière neuve que l'audit v0.3 avait nommés puis écartés (décision 9 du TOC).*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — portes **G-3**, **G-5** et **G-6** ouvertes ; volet résiduel de **G-1** non instruit ; **ordre de rédaction du PRD §6 enfreint** ; instruction d'auteur du 27 juillet 2026. ⚠ **Ce chapitre porte le SIÈGE DE LA SÉMANTIQUE D'EFFET pour toute la somme** (§ 48.1) : **quatre pièces rédigées y renvoient déjà** — ch. 22 § 22.5, ch. 23, ch. 24, ch. 27 —, plus le **ch. 1 § 1.5.2 et § 1.6.2.2**, et **aucune ne reconstruit la matière**. ⚠ **Et il est FERMÉ à une matière par décision d'auteur** : **D-7** (périmètre assumé et déclaré) ferme les ch. 6, 37 et 48 à l'accord entre agents sous asynchronie et défaillance partielle ; *y ouvrir une section rouvrirait la décision, non le seul chapitre*. Voir la note de statut, § 48.6 |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Aucun gel de source n'est consommé** : « Fusion : aucune ». Les repérages hérités qu'il mobilise viennent du **Vol. I** (gel de **juin 2026**, régime **[C]**) et du **Vol. III** (gel du **21 juillet 2026**, niveaux conservés) par l'intermédiaire de pièces rédigées de la somme, ⚠ **et aucun des deux ne tient lieu du gel de la somme**. ⚠ **Volet résiduel de G-1 non instruit** : la préimpression du § 48.5 n'a pas été ouverte, et aucune spécification protocolaire n'a été rebalayée pour le § 48.2 |
| **Socle mobilisé** | **Aucune entrée du socle consolidé** (G-3) **et aucune entrée propre** — matière neuve, « Fusion : aucune » (décision 9 du TOC). Résolution effective : *(a)* **adossements internes** aux pièces rédigées — **ch. 1 § 1.5.2** et **§ 1.6.2.2** (idempotence, saga, résultats d'impossibilité au grain pré-agentique), **ch. 4 § 4.6** (l'idempotence comme propriété de conception d'outil), **ch. 8 § 8.3** (tâches asynchrones **expérimentales**), **ch. 22 § 22.5** (exécution durable) —, chacune portant ses entrées et ses niveaux, **non retranscrits ici** ; *(b)* deux **repérages [C] du Vol. I** cités par leur section — `Monographie` §5.7.5 (irréversibilité des rails temps réel) et §5.7.6 (encapsulation du cœur bancaire) — qui **corroborent et ne portent pas** ; *(c)* la **relève v0.10** du plan, en repérage [C], **dont aucun résultat chiffré n'est repris**. ⚠ **Régime de preuve le plus dur des trois** (PRD §7.2) : aucun vote adversarial n'a eu lieu, aucune source primaire n'a été extraite — **aucun énoncé n'est central au sens de CA-IV-01**, et **CA-IV-07 est porté à l'ouverture** |
| **Garde-fous balayés** | Vol. III — **R-14 (trois degrés d'absence) : neuf occurrences au corps, re-mesurées** — **huit énoncés d'absence portant le degré 3** (chapeau, § 48.2, § 48.3, § 48.4, § 48.5) et **une qualification de fait négatif établi** (§ 48.1, reprise du ch. 16 § 16.1) ; **R-02 (qualifier par ce que la spécification démontre) : trois occurrences**, § 48.2 (deux, dont le refus d'assimiler les tâches asynchrones à un moteur durable), § 48.5 ; **R-09 : une occurrence**, § 48.2, sur la révision protocolaire annoncée au brouillon ; **R-13 : zéro occurrence** — ni « control plane » ni « autonomie graduée » ne sont employés, ⚠ **et le faux ami est déclaré** : le « plan de contrôle » pré-agentique du ch. 1 § 1.3.4 n'est pas visé par R-13 et n'apparaît pas ici ; **R-01 à R-08, R-10 à R-12 : zéro occurrence**. Vol. II — **R-4 (RTR : « quatre cibles successives », jamais « lancé ») : une occurrence**, § 48.4, où le rail temps réel canadien est nommé **sans jamais être dit lancé** (réserve F-29) ; **R-1 à R-3, R-5 à R-8 : zéro occurrence** |
| **Volumétrie cible** | ≈ **4 700 mots** de corps (§ 48.1 à § 48.5), **cible dérivée par front** : 14 000 mots au premier mouvement du Livre (TOC v0.25, Volumétrie — le chiffre de l'audit v0.3 pour ses **trois** fronts), dont **un** porté par ce chapitre, soit ≈ 4 700 ; les deux autres sont au ch. 47 (≈ 9 300). ☑ **Décompte publiable depuis G-2** ; **réel : 2 793 mots** par [`PRD/decompte.sh`](../PRD/decompte.sh), seule autorité de décompte — **−40,6 %**. ⚠ **L'écart est en défaut et son motif est celui du ch. 47** : *sur un front sans socle, la volumétrie mesure ce qu'on peut écrire sans fabriquer* — et **deux des cinq sections sont des lots d'instruction**. ⚠ **D-4 interdit l'amputation comme le gonflement** : l'écart se documente et ne se corrige pas |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.26, entrée du chapitre 48)* — une action d'agent produit des effets dans des systèmes d'enregistrement, et ce qui advient quand elle réussit à moitié — idempotence, compensation, réconciliation — **n'est documenté par rien de ce que la somme a instruit, ni du côté des protocoles (Livre I) ni du côté de l'encadrement (Livre III)** ; c'est en finance que le coût de ce silence est maximal (un virement à moitié réussi n'est pas un incident d'observabilité, c'est un écart comptable).

⚠ **Thèse réalignée au TOC v0.26** (décisions 8 et 14), sur la remontée **R-IV-65** ouverte par cette
pièce. La forme antérieure écrivait « **n'est spécifié ni** par les protocoles **ni** par
l'encadrement » — un **quantificateur universel négatif qu'aucun balayage ne soutient**. Ce que le
corpus établit est une **absence de documentation**, au **degré 3** de l'échelle R-14 du Vol. III, et
*non un fait négatif vérifié*. **Le corps du chapitre n'a pas changé** : il écrivait déjà l'énoncé sous
la forme bornée, et son chapeau posait la distinction avant d'entrer dans les sections.

---

⚠ **La thèse est déclarée *construction d'auteur, socle à constituer* par le TOC lui-même**, et elle
porte deux propositions de statuts inégaux qu'il faut séparer avant d'entrer dans le chapitre. La
seconde — *un virement à moitié réussi est un écart comptable* — est une **lecture d'auteur**, et
elle est reprise comme telle. La première — *ce n'est spécifié ni par les protocoles ni par
l'encadrement* — est une **absence**, et **elle n'a pas été établie par balayage** : c'est une
*absence de documentation dans le corpus de la somme*, au **degré 3** de l'échelle R-14 du Vol. III,
non un fait négatif vérifié. *Le chapitre ne peut donc pas écrire que les protocoles n'en disent
rien ; il écrit que rien de ce que la somme a instruit ne le documente*, ce qui n'est pas la même
proposition et n'autorise pas la même conclusion.

## § 48.1 — Taxonomie des effets d'une action d'agent

> ⚠ **SIÈGE DE LA SÉMANTIQUE D'EFFET POUR TOUTE LA SOMME.** La matière — *idempotence,
> compensation, réconciliation* — est posée **ici une seule fois**. Le **ch. 1 § 1.5.2** et
> **§ 1.6.2.2** en posent les fondements **au grain pré-agentique** et y renvoient ; les **ch. 22
> § 22.5**, **ch. 23**, **ch. 24** et **ch. 27** l'**appliquent** et y renvoient nommément ; aucun de
> ces chapitres ne la reconstruit. *C'est l'économie de la fusion côté « effets d'une action », et
> elle n'a lieu que si ces chapitres s'y tiennent.*

Lecture de l'auteur — la taxonomie qui suit est une construction de ce chapitre. **Ce que le socle
établit** : rien ; il n'y a pas de socle, et aucune des trois classes ne résout contre une entrée
numérotée d'aucun volume. **Ce qu'il n'établit pas** : que ces trois classes soient les bonnes,
qu'elles soient exhaustives, ni qu'une action réelle se rattache à une seule d'entre elles. Elle vaut
comme **vocabulaire de travail** — et son seul mérite est de faire tenir ensemble trois questions que
les chapitres amont posent séparément.

| Classe d'effet | Ce qu'une reprise produit | Ce qui la borne | Où la somme en traite |
|---|---|---|---|
| **Lecture** | rien : rejouer une lecture ne change pas l'état du système d'enregistrement | le coût et la fraîcheur, non la correction | ch. 1 § 1.5.2 (déduplication, condition de version) |
| **Écriture** | un doublon, **sauf si l'opération est idempotente** | l'idempotence est une **propriété de l'outil**, jamais du protocole qui l'invoque (ch. 4 § 4.6) | § 48.2 ; ch. 22 § 22.5 (reprise d'un moteur durable) |
| **Engagement** | un second engagement, **que rien ne défait** | seule la **compensation** agit, et elle est sémantique, non transactionnelle | § 48.3 ; § 48.4 pour le cas financier |

: Tableau 48.1 — Les trois classes d'effet d'une action d'agent, construction d'auteur du présent chapitre au 27 juillet 2026. **Aucune ligne ne résout contre une entrée de socle** ; la colonne de droite renvoie aux sièges qui traitent la matière, jamais à une source qui l'établirait.

**Ce que la taxonomie fait voir, et c'est le seul point qu'elle établisse : la frontière qui compte
n'est pas celle du succès et de l'échec, mais celle de la reprise.** Un système qui reprend une
trajectoire interrompue rejoue des lectures sans conséquence, des écritures avec conséquence si
l'outil n'est pas idempotent, et des engagements qu'aucune reprise ne peut annuler. *La question
« l'action a-t-elle réussi » est mal posée ; la question opérante est « que produit son rejeu ».*

⚠ **Le fondement de cette distinction est un résultat d'impossibilité, et il est déjà posé.** Le
**ch. 1 § 1.5.2** établit que la livraison exactement-une-fois est **irréalisable sous pannes** —
instance du problème des deux généraux —, et que la voie praticable est le **traitement**
exactement-une-fois, obtenu en combinant une livraison au-moins-une-fois avec un consommateur
idempotent. Ce chapitre en tire la conséquence que le ch. 1 lui assigne : *si la livraison ne peut
être garantie, l'effet doit l'être ; et c'est l'effet, non le message, que la sémantique de ce
chapitre prend pour objet.*

## § 48.2 — Idempotence et rejouabilité des appels d'outils

⚠ **Le plan borne cette section par une formule qu'il faut appliquer à la lettre : « ce que les
spécifications protocolaires en disent — **à instruire, jamais présumé** ».** Aucune passe
d'instruction protocolaire n'a été conduite pour ce chapitre. Ce qui suit est donc **ce que des
pièces rédigées de la somme portent déjà**, plus l'état de l'absence — jamais une lecture de
spécification faite ici.

**Ce que la somme porte, et c'est peu mais c'est précis.** Le **ch. 8 § 8.3** établit que les
**tâches asynchrones** du protocole agent-outil sont **expérimentales**, que le mécanisme *se
rapproche, sans s'y identifier*, de l'exécution durable de l'intégration d'entreprise, et surtout
qu'il **ne fournit pas les garanties de reprise et d'idempotence** d'un moteur durable — *leur
contrat ne saurait être présenté comme stable*. ⚠ **C'est un énoncé sur ce que le mécanisme ne
démontre pas, et il est repris tel quel** : R-02 du Vol. III veut qu'un mécanisme se qualifie par ce
que sa spécification démontre, jamais par la parenté qu'on lui prête. *Le rapprochement avec un
moteur durable est précisément ce que le ch. 8 refuse de tenir pour une équivalence.*

**Ce que la somme porte du côté de l'outil.** Le **ch. 4 § 4.6** range l'idempotence parmi les
propriétés de conception d'un outil — *une même requête répétée produit le même état*, ce qui protège
des réessais et des duplications d'effets de bord. Lecture de l'auteur — **la conséquence est
dissymétrique et elle est le cœur de la section** : *l'idempotence est une propriété de l'outil
invoqué, pas du protocole qui l'invoque, ni de l'agent qui décide de l'invoquer.* **Ce que le socle
établit** : la propriété et son intérêt, par le ch. 4. **Ce qu'il n'établit pas** : qu'un protocole
agentique la prescrive, l'exprime dans un champ, ou permette à un appelant de savoir si l'outil
qu'il appelle la possède.

⚠ **L'absence, à son degré exact.** **Le socle de la somme ne documente aucune spécification
protocolaire prescrivant l'idempotence d'un appel d'outil, ni aucun champ qui la déclarerait —
degré 3, absence de documentation dans le corpus de cet ouvrage.** Deux bornes accompagnent ce
constat, et sans elles il serait faux. *(1)* Le balayage sur lequel il s'appuie n'a pas été mené pour
cette question : le **ch. 20 § 20.1** rapporte l'énumération des **huit champs** du type qui décrit un
outil, dont aucun ne porte de version, d'empreinte ni de signature — *ce balayage-là portait sur
l'intégrité, non sur l'idempotence*, et il était **borné à une page d'une révision nommée**.
*L'étendre à l'idempotence serait exactement l'élargissement que le contrôle de bornage du Vol. III
écarte.* *(2)* ⚠ **Une révision majeure du protocole agent-outil est annoncée au brouillon** — dont la
date n'est pas confirmée à la source (R-09 du Vol. III) — et **tout constat de cette section est à
rejouer sur la révision publiée** : il ne vaut pas par avance pour elle.

**Le lot d'instruction, formulé pour qu'il soit ouvrable.** *Question* : une spécification
protocolaire agentique prescrit-elle, exprime-t-elle ou permet-elle de déclarer l'idempotence d'une
opération invocable, et sous quelle forme un appelant peut-il l'établir avant d'invoquer ?
*Corpus à ouvrir* : les pages de définition d'outil des révisions courantes des deux protocoles du
Livre I, dans leur texte intégral ; les documents de l'IETF sur les méthodes idempotentes et les clés
de requête ; les contrats de tâche des moteurs d'exécution durable relevés au ch. 22 § 22.5.
*Critère de clôture* : un champ nommé, ou un énoncé normatif cité et daté, portant l'idempotence
d'une opération — non une recommandation de bonne pratique dans une page de guide. *Échec documenté* :
si le corpus n'en porte pas, l'énoncé qui en sort reste au degré 3, et la thèse du chapitre est
**confirmée dans sa lettre sans être établie** — nuance qui doit survivre à l'instruction.

## § 48.3 — Compensation et sagas au grain de l'agent

**Le patron est acquis et ne se reconstruit pas ici.** Le **ch. 1 § 1.6.2.2** pose la saga —
renoncement à l'atomicité globale au profit d'une suite de transactions locales, chacune assortie
d'une **compensation** qui **annule sémantiquement** son effet —, ses deux variantes orchestrée et
chorégraphiée, et le régime de cohérence dans lequel ce renoncement s'inscrit. Le **ch. 22 § 22.5**
porte l'exécution durable, sa reprise et son rejeu. *Ce chapitre applique ; il ne réexpose ni l'un ni
l'autre.*

Lecture de l'auteur — **ce que « au grain de l'agent » change, et c'est la seule proposition propre
de la section.** Une saga classique suppose que l'ensemble des étapes soit **connu du concepteur** :
la compensation de l'étape *k* est écrite en même temps que l'étape *k*. Un agent qui **compose sa
trajectoire à l'exécution** — c'est la définition même que le ch. 22 donne de l'orchestration pilotée
par un agent générateur de plans — produit des suites d'étapes que personne n'a écrites, donc des
suites dont personne n'a écrit les compensations. **Ce que le socle établit** : le patron et ses
variantes (ch. 1 § 1.6.2.2) ; que la trajectoire d'un agent générateur de plans n'est pas fixée à la
conception (ch. 22 § 22.5, avec ses niveaux propres). **Ce qu'il n'établit pas** : qu'un mécanisme de
compensation ait été spécifié pour une trajectoire composée à l'exécution, ni qu'un moteur durable en
fournisse un. **Le socle ne documente aucun dispositif de compensation dont la portée soit une
trajectoire d'agent non fixée à la conception — degré 3.**

⚠ **Deux bornes ferment cette section, et la seconde est une décision d'auteur qu'il est interdit de
rouvrir ici.**

*(1)* **La compensation n'est pas l'annulation.** Elle *annule sémantiquement* — un remboursement
compense un débit, il ne le supprime pas ; les deux écritures subsistent. C'est la formule du
**ch. 1 § 1.6.2.2**, et elle décide de tout le § 48.4 : *dans un système d'enregistrement, la
compensation laisse une trace, et c'est cette trace que la réconciliation lit.*

*(2)* ⚠ **L'accord entre agents sous asynchronie et défaillance partielle n'est pas traité, et cette
absence est un périmètre assumé, non un oubli.** Le **ch. 1 § 1.6.2.2** pose les résultats
d'impossibilité **au grain pré-agentique** et déclare qu'il est le **seul endroit de l'ouvrage** où
ils figurent ; la **décision d'auteur D-7**, prise le 27 juillet 2026 (risque 15 du TOC), a arbitré
la matière en **périmètre assumé et déclaré**, ce qui **ferme** les ch. 6, 37 et **48**. *Y ouvrir une
section ne rouvrirait pas ce chapitre : elle rouvrirait la décision.* ⚠ **Et la conséquence pour le
lecteur est celle que le ch. 1 énonce** : les architectures inter-institutions que la somme prescrit
— maillage inter-domaines, vérification d'agent tiers, rails de paiement — **opèrent sous un régime
de défaillance que l'ouvrage ne caractérise pas**. *Un périmètre assumé n'est pas un angle mort
résorbé : c'est un angle mort dont le lecteur est prévenu.* Le **ch. 49** en enregistre l'état final.

⚠ **Un fait de plan est consigné ici parce qu'il est le motif du risque 15 et qu'il se lit mal
ailleurs** : cette section est, selon le TOC v0.25, la **seule occurrence de « sagas » de toute la
zone des chapitres**, et elle l'est **au grain d'une action unique**. *C'est ce constat, et non une
préférence d'architecture, qui a fondé le risque 15 — et D-7 l'a borné sans le combler.*

## § 48.4 — Réconciliation des flux financiers

**La thèse place ici le coût maximal du silence, et cette section dit pourquoi — sans pouvoir
l'établir.** Trois propriétés se cumulent dans un système d'enregistrement financier, et chacune est
portée par un renvoi, non par une source de ce chapitre.

*Premièrement, l'irréversibilité.* Le **Vol. I** `Monographie` **§5.7.5** traite les paiements temps
réel et leur irréversibilité, et son **§7.9.3** — repris au **ch. 49 § 49.9** — pose que le règlement
sur monnaie programmable est **sans mécanisme de rétrofacturation**, de sorte qu'une erreur d'agent
n'y est pas rattrapable *a posteriori*. ⚠ **Les deux entrées sont en [C]** : le Vol. I entre au
régime le plus faible, sa vérification portant sur ses références et non sur le contenu de ses
affirmations (PRD §7.1) — *elles corroborent, elles ne portent pas*. ⚠ **Et une formulation est
imposée** : le rail temps réel canadien se nomme sans jamais s'écrire « lancé » (réserve F-29, R-4 du
Vol. II) ; le ch. 33 en est le siège, et ce chapitre n'en date rien.

*Deuxièmement, l'encapsulation.* Le **Vol. I** `Monographie` **§5.7.6** porte la règle invariante
selon laquelle **aucun agent n'accède en écriture directe au grand livre**, la couche d'exposition ne
publiant que des capacités **bornées et idempotentes** — en **[C]** de nouveau. *L'idempotence y est
donc une exigence de l'exposition, ce qui rejoint exactement le constat dissymétrique du § 48.2 : la
propriété est portée par ce qui expose l'outil, jamais par ce qui l'appelle.*

*Troisièmement, l'écart comptable.* Lecture de l'auteur — **c'est la seconde proposition de la thèse,
et elle est une lecture, non un fait** : un virement dont l'ordre est parti et dont la confirmation
n'est pas revenue laisse deux systèmes dans deux états, et *ce désaccord n'est pas un défaut de
supervision, c'est une différence entre deux enregistrements*. **Ce que le socle établit** :
l'irréversibilité et l'encapsulation, en [C]. **Ce qu'il n'établit pas** : qu'un tel écart ait été
observé sur un flux agentique, ni qu'un dispositif de réconciliation ait été spécifié pour ce cas.
**Le socle ne documente aucun mécanisme de réconciliation dont le périmètre déclaré couvre les
effets d'une action d'agent — degré 3.**

⚠ **Trois renvois de cette section portent la matière que le chapitre n'a pas, et leurs trois cibles
sont dans trois états différents.** Le plan situe les flux ISO 20022 au **ch. 33** — ⚠ **rédigé le
même jour hors de cette passe, à re-vérifier au commit** —, au **ch. 45 § 45.12** — ⚠ **renvoi de
plan, chapitre non rédigé** — et le **trou de responsabilité** au **ch. 36 § 36.2.6** — ⚠ **renvoi de
plan, chapitre non rédigé**. *La conséquence est à écrire plutôt qu'à taire : la partie de cette
section qui rattacherait la sémantique d'effet à un flux de règlement réel est celle qui manque, et
elle manque parce que deux de ses trois chapitres d'appui n'existent pas encore.*

## § 48.5 — Tracer l'effet, pas seulement l'appel

**La question est étroite : ce qu'une trace d'exécution enregistre est un appel, non son effet.** Le
plan situe le *chaînon manquant* au **ch. 38 § 38.5** — ⚠ **rédigé le même jour hors de cette passe,
à re-vérifier au commit** — et ce chapitre le prolonge au seul grain qui lui appartient : *ce qui manque n'est pas la trace de
l'appel, c'est la jointure entre l'appel tracé et l'effet enregistré ailleurs.*

**Deux constats hérités du Vol. III cadrent la difficulté, et ils sont plus précis que ce que ce
chapitre pourrait produire.** *(1)* Sa **lacune 21** — *corrélation entre trace d'exécution et chaîne
de mandat protocolaire* — est déclarée **non instruite** : la pièce de jonction n'a été ouverte par
aucun de ses lots. *(2)* Son **§26.3** établit que les compteurs d'appels des conventions relevées
comptent les appels **directs**, les appels de sous-agents ou d'agents auxquels la tâche est
transférée étant **attribués séparément** — de sorte qu'*une chaîne de délégation n'est pas
reconstituable par sommation de ces compteurs*, non par insuffisance de l'instrument mais **par
construction déclarée de sa sémantique**. ⚠ **Les deux constats entrent sous G-4 non franchie** : ils
viennent d'un volume qui se déclare *rédigé mais non publiable*, et *le volet de fond de la collation
reste dû*. ⚠ **Et le second porte une réserve de vote à sa source** — l'entrée qui l'établit est
marquée *vote dû, non conduit* : elle est reprise avec cette marque, jamais sans elle.

Lecture de l'auteur — **ce que ces deux constats permettent de dire de l'effet, et c'est neuf :**
si une chaîne d'appels n'est pas reconstituable, *l'effet observé au bout de la chaîne n'est
rattachable à aucun mandat déterminé*. **Ce que le socle établit** : la sémantique des compteurs et
la non-instruction de la jointure (Vol. III, avec ses réserves). **Ce qu'il n'établit pas** : qu'une
clé de jointure existe, ni qu'aucune n'existe. **Le socle ne documente aucune clé rattachant un effet
enregistré à la trace de l'appel qui l'a produit — degré 3.**

⚠ **Une taxonomie candidate existe déjà, en vocabulaire de sûreté, et elle dit la même chose depuis
l'autre bout.** Une **préimpression adverse de mai 2026** tient la **détection des divergences entre
l'action effectuée et son enregistrement d'audit** pour la propriété porteuse d'un *runtime*
agentique, et en énumère **quatre** : contournement de garde, falsification du journal, échec
silencieux de l'hôte, cible erronée. *C'est, dit autrement, la question de ce chapitre.*

⚠ **Deux réserves, et aucune n'est facultative.** *(1)* La préimpression **n'est pas révisée par les
pairs**, et **son texte n'a pas été ouvert par cette passe** — ce qui est rapporté est ce que la
relève du plan en porte, **degré 3** sur tout le reste. *(2)* Elle **propose une implémentation
concurrente de l'objet qu'elle mesure** : son intérêt est inverse de celui de l'éditeur, *ce qui ne
le neutralise pas* mais interdit de la lire comme un relevé neutre. **Taxonomie à instruire ; aucun
de ses résultats chiffrés n'est repris ici** — et *un chiffre non repris ne se devine pas davantage
qu'il ne se cite*.

⚠ **Ce que ce chapitre lègue, et ce qu'il ne lègue pas.** Il lègue **une taxonomie de travail**
(§ 48.1), **deux lots d'instruction** (§ 48.2, § 48.5) et **le siège** que quatre pièces rédigées
attendaient. Il ne lègue **aucun mécanisme** : ni idempotence prescrite, ni compensation spécifiée,
ni clé de jointure. *La somme sait désormais nommer ce qui advient quand une action d'agent réussit à
moitié ; elle ne sait pas encore ce qu'un exploitant doit en faire, et le ch. 49 § 49.14 l'enregistre
à ce titre.*

---

## § 48.6 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.**

**Ce qui est enfreint.** Portes **G-3**, **G-5** (D-2 non prise) et **G-6** (D-3 non prise) ; volet
résiduel de **G-1** non instruit ; **ordre de rédaction du PRD §6** — ce mouvement vient en cinquième
position, après les ch. 41-46. Instruction d'auteur du 27 juillet 2026.

1. **Aucun énoncé n'est central au sens de CA-IV-01.** Le régime applicable est le plus dur des trois
   (PRD §7.2, « Matière neuve ») : **toutes** les affirmations centrales au vote adversarial, plancher
   « sources primaires seules ». **Zéro vote, zéro extraction.**
2. **Les décomptes sont publiables** (G-2). Écart de **−40,6 %** sur la cible dérivée par front.
3. **Les renvois se partagent en trois régimes** — ⚠ **relevé horodaté du 27 juillet 2026 :
   les cinquante chapitres du plan existent désormais en brouillon** — ⚠ *et ce décompte a bougé DEUX
   FOIS pendant la rédaction de cette pièce*, les Livres III et IV ayant été écrits puis committés **en
   parallèle, hors de cette passe**, portant le corpus de 25 à 50 pièces de chapitre. **Aucun renvoi de
   plan ne subsiste donc**, et ce qui subsiste est plus exigeant à déclarer : **dix-neuf pièces sur
   cinquante que la présente passe n'a pas relues.** **(a)**
   Résolvent contre du **texte rédigé, relu par cette passe** : ch. 1 § 1.5.2 et § 1.6.2.2, ch. 4
   § 4.6, ch. 8 § 8.3, ch. 16 § 16.1, ch. 20 § 20.1 — et **ch. 47, ch. 49 § 49.9 et § 49.14**,
   rédigés dans la présente passe. **(b)** Résolvent contre du **texte rédigé le même jour, hors de
   cette passe et non relu par elle** : ch. 22 § 22.5, ch. 23, ch. 24, ch. 27, ch. 33, ch. 38
   § 38.5 — ⚠ *à re-vérifier au commit*. **(c)** **Renvois de plan : aucun au commit** — ⚠ *les ch. 36 § 36.2.6 et ch. 45 § 45.12 l'étaient
   encore à la rédaction, et ont été écrits depuis, hors de cette passe : ils passent au groupe (b) et
   **se re-vérifient**.*
4. **Une matière est absente par décision d'auteur, non par omission** : l'accord entre agents sous
   asynchronie et défaillance partielle, fermé au ch. 48 par **D-7**. *La déclarer est la seule chose
   que ce chapitre pouvait faire ; l'écrire aurait rouvert la décision.*

**Remontées ouvertes par ce chapitre :**

- **R-IV-64 — non bloquante, de siège et d'appareil ; elle constate qu'un siège existait avant sa
  pièce.** **Quatre pièces du Livre III** — ch. 22 § 22.5, ch. 23, ch. 24, ch. 27 — et **deux sections
  du ch. 1** déclarent que « la sémantique d'effet est au **ch. 48**, qui en est le siège », **alors
  que le TOC ne désigne nulle part ce chapitre comme siège** et que `check-sieges.py` n'en portait
  aucune trace. *Le marqueur est posé par la présente pièce et le siège est versé à l'appareil* — mais
  la **désignation** relève du plan. **Demande remontée** : inscription du siège de la sémantique
  d'effet à l'entrée du ch. 48 du TOC, comme la v0.25 l'a fait pour le siège du tri prospectif au
  ch. 49 § 49.0. ⚠ *Un siège qu'aucun plan ne désigne et que cinq pièces citent est un siège qui
  disparaît au premier remaniement.*
- **R-IV-65 — non bloquante, de thèse.** La thèse citée affirme que la sémantique d'effet « n'est
  spécifié ni par les protocoles (Livre I) ni par l'encadrement (Livre III) ». ⚠ **C'est un
  quantificateur universel négatif, et aucun balayage ne le soutient** : le corpus de la somme n'en
  documente rien — **degré 3** —, ce qui n'établit pas l'absence. *La classe de défaut est celle que
  la décision 14 du TOC nomme, et le chapitre écrit son corps sous la forme bornée sans toucher à la
  thèse.* **Demande remontée** : réalignement de la thèse sur la forme bornée, ou balayage documenté
  qui l'établirait.
- **R-IV-66 — non bloquante, de dépendance.** Le **§ 48.4** est la section dont la matière dépend le
  plus de chapitres que cette passe n'a pas relus : ch. 33 (flux ISO 20022, rédigé le même jour hors
  d'elle), ch. 36 § 36.2.6 (trou de responsabilité, **non rédigé**), ch. 45 § 45.12 (**non
  rédigé**). **Demande remontée** : que la section soit **re-vérifiée après la rédaction du
  Livre III et du second mouvement du Livre IV**, et non tenue pour acquise. ⚠ *Le plan plaçait ce
  mouvement en dernier précisément pour cette raison ; l'ordre a été enfreint, et le § 48.4 en porte
  le coût.*

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.25 (structure inchangée en v0.26)** — § 48.1 à
§ 48.5, dans l'ordre exact. La **table d'appuis** est respectée : les adossements internes sont **des
renvois, jamais des sources**, et **aucune entrée F-xx, aucun garde-fou hérité** n'est revendiqué.
**Le siège est posé et marqué** (§ 48.1), et **versé à [`PRD/check-sieges.py`](../PRD/check-sieges.py)
dans la même passe**, avec son harnais de mutation rejoué. **Aucun siège d'un autre chapitre n'est
reconstruit** : les résultats d'impossibilité et le patron saga restent au **ch. 1 § 1.6.2.2**,
l'exécution durable au **ch. 22 § 22.5**, l'anatomie des tâches asynchrones au **ch. 8 § 8.3**,
l'énumération des huit champs au **ch. 20 § 20.1**. **La matière fermée par D-7 n'est pas écrite.**
**Les neuf occurrences de R-14 portent leur degré**, dont huit au **degré 3**, et **aucune absence
propre à ce chapitre n'est écrite comme fait négatif vérifié**. **Les trois occurrences de R-02**
énoncent ce que la source démontre **et**
ne démontre pas — dont le refus explicite d'assimiler les tâches asynchrones à un moteur durable.
**Les quatre divergences de la préimpression sont nommées, ses deux réserves portées, et aucun de ses
chiffres n'est repris.** **Le rail temps réel canadien n'est jamais dit lancé** (R-4). Enfin, **la
réserve de vote de l'entrée du Vol. III est reprise avec l'entrée**, jamais détachée d'elle.
