# Chapitre 48 — La sémantique d'effet : idempotence, compensation, réconciliation

*Livre V — Livrer et clore : l'agent comme livrable logiciel, horizon et frontière.
Premier mouvement — l'agent comme livrable logiciel : provenance, mise en service, sémantique
d'effet (ch. 47-48). Second et dernier chapitre du mouvement, et **troisième des trois fronts** de
matière neuve que l'audit v0.3 avait nommés puis écartés (décision 9 du TOC).*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — **rédigé avant G-3, G-5 et G-6** ; **ordre de rédaction du PRD §6 enfreint** ; instruction d'auteur du 27 juillet 2026. ⚠ **Une seule des trois portes a bougé depuis, et il faut la lire dans le bon sens** : ☑ **G-3 est FRANCHIE depuis le 28 juillet 2026** (PRD v0.14, socle consolidé à 159 entrées) ; ☐ **G-5 et G-6 restent ouvertes**, D-2 et D-3 prises n'étant ni l'une ni l'autre une porte franchie — *et une porte franchie après coup ne rattrape pas la rédaction qui l'a enfreinte.* ⚠ **Ce chapitre porte le SIÈGE DE LA SÉMANTIQUE D'EFFET pour toute la somme** (§ 48.1), et le siège existait avant sa désignation : **quatre pièces du Livre III y renvoyaient déjà** — ch. 22 § 22.5, ch. 23, ch. 24, ch. 27 —, plus le **ch. 1 § 1.5.2 et § 1.6.2.2**, soit **cinq pièces et six sections** au relevé du versement (27 juillet 2026) ; ⚠ **le domaine s'est élargi depuis, et il n'est pas re-cardinalisé ici** — *le corpus a doublé pendant et après cette passe* : il se re-mesure par le déclencheur de [`PRD/check-sieges.py`](../PRD/check-sieges.py), qui est l'instrument de l'abstention. ⚠ **Et il est FERMÉ à une matière par décision d'auteur** : **D-7** (périmètre assumé et déclaré) ferme les ch. 6, 37 et 48 à l'accord entre agents sous asynchronie et défaillance partielle ; *y ouvrir une section rouvrirait la décision, non le seul chapitre*. Voir la note de statut, § 48.6 |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Aucun gel de source n'est consommé** : « Fusion : aucune ». Les repérages hérités qu'il mobilise viennent du **Vol. I** (gel de **juin 2026**, régime **[C]**) et du **Vol. III** (gel du **21 juillet 2026**, niveaux conservés) par l'intermédiaire de pièces rédigées de la somme, ⚠ **et aucun des deux ne tient lieu du gel de la somme**. ⚠ **Volet résiduel de G-1 : son volet de FAITS est levé depuis le 28 juillet 2026** — les **123 entrées à sensibilité temporelle** du socle consolidé portées à leur source primaire ([`gel-2026-07-28-volet-residuel.md`](../PRD/gel-2026-07-28-volet-residuel.md)) —, **mais le volet dont ce chapitre dépend reste dû** : l'instruction des relèves atterrissant hors du Livre I, dont la **relève v0.10** qui fonde le § 48.5. *La préimpression n'a pas été ouverte, et aucune spécification protocolaire n'a été rebalayée pour le § 48.2* |
| **Socle mobilisé** | ⚠ **Le socle consolidé EXISTE depuis le 28 juillet 2026** — [`socle-consolide.md`](../PRD/socle-consolide.md) **v1.2, 159 entrées `S-001`…`S-159`** — **et ce chapitre n'en mobilise aucune**, non plus qu'aucune entrée propre : matière neuve, « Fusion : aucune » (décision 9 du TOC). *L'énoncé du champ n'a donc pas changé de lettre ; il a changé de motif, et le second est le seul qui vaille* — **avant, il n'y avait pas de socle où chercher ; désormais il y en a un, et la matière de ce chapitre n'y a pas de ligne.** Résolution effective : *(a)* **adossements internes** aux pièces rédigées — **ch. 1 § 1.5.2** et **§ 1.6.2.2** (idempotence, saga, résultats d'impossibilité au grain pré-agentique), **ch. 4 § 4.4.2** (l'idempotence comme propriété de conception d'outil), **ch. 8 § 8.2.3** (tâches asynchrones **expérimentales**), **ch. 22 § 22.5** (exécution durable) —, chacune portant ses entrées et ses niveaux, **non retranscrits ici** ; *(b)* deux **repérages [C] du Vol. I** cités par leur section — `Monographie` §5.7.5 (irréversibilité des rails temps réel) et §5.7.6 (encapsulation du cœur bancaire) — qui **corroborent et ne portent pas**, ⚠ **et dont aucune ligne du socle consolidé ne porte la provenance** (balayage de la chaîne « §5.7 » sur le fichier, 28 juillet 2026, **zéro occurrence** ; *un balayage de chaîne n'est pas un balayage sémantique*) ; *(c)* la **relève v0.10** du plan, en repérage [C], **dont aucun résultat chiffré n'est repris**. ⚠ **Régime de preuve le plus dur des trois** (PRD §7.2) : aucun vote adversarial n'a eu lieu, aucune source primaire n'a été extraite — **aucun énoncé n'est central au sens de CA-IV-01**, et **CA-IV-07 est porté à l'ouverture** |
| **Garde-fous balayés** | Vol. III — **R-14 (trois degrés d'absence) : neuf occurrences au corps** — ⚠ **décompte re-mesuré au commit du 28 juillet 2026 sous la règle littérale : le marqueur de la formule dans le corps (chapeau, § 48.1 à § 48.5), en-tête, bloc de réalignement de thèse et note de statut exclus** — soit **huit énoncés d'absence portant le degré 3** (chapeau ; § 48.2, *deux* ; § 48.3 ; § 48.4 ; § 48.5, *trois*) et **une qualification écartant le fait négatif vérifié** (chapeau). ⚠ **Le cardinal coïncide avec celui du relevé antérieur, sa localisation non — et c'est la localisation qui se vérifie.** Ce relevé créditait au **§ 48.1** « une qualification de fait négatif établi, reprise du ch. 16 § 16.1 » : *le § 48.1 ne porte ni cette formule ni ce renvoi*, l'énoncé visé est au **ch. 47 § 47.12**, et la qualification réelle est au **chapeau**. Le total est par ailleurs tenu par une occurrence neuve — l'issue d'échec du lot du § 48.5, écrite au commit du 28 juillet 2026 —, *ce qui montre qu'un cardinal juste peut recouvrir une ventilation fausse*. ☑ **Cardinal ET ventilation rejoués à la relecture du même jour, sur le corps re-extrait, et retrouvés à l'unité et au site** ; ⚠ *le rejeu était dû, la passe de relecture ayant elle-même ajouté de la prose au chapeau* ; ☑ **rejoués une troisième fois à la contre-relecture du 28 juillet 2026**, sur le corps re-extrait après ses propres corrections, **retrouvés à l'unité et au site** ; **R-02 (qualifier par ce que la spécification démontre) : deux occurrences, TOUTES DEUX au § 48.2** — l'énoncé sur ce que le mécanisme *ne démontre pas*, et la règle qui l'autorise —, ⚠ **cardinal et ventilation corrigés à la relecture du 28 juillet 2026** : *le relevé antérieur annonçait trois occurrences dont une au § 48.5, où le radical « démontr » ne figure pas* — les deux réserves qui y vivent portent sur la **qualité de la source**, non sur ce qu'une spécification démontre, et les compter en R-02 confondait deux garde-fous — ☑ **correction re-vérifiée à la contre-relecture du 28 juillet 2026 par balayage du radical « démontr » sur le corps entier : deux occurrences, toutes deux au § 48.2** ; **R-09 : une occurrence**, § 48.2, sur la révision protocolaire annoncée au brouillon ; **R-13 : zéro occurrence** — ni « control plane » ni « autonomie graduée » ne sont employés, ⚠ **et le faux ami est déclaré** : le « plan de contrôle » pré-agentique du ch. 1 § 1.3.4 n'est pas visé par R-13 et n'apparaît pas ici ; **R-01, R-03 à R-08, R-10 à R-12 : zéro occurrence**. Vol. II — **R-4 (RTR : « quatre cibles successives », jamais « lancé ») : une occurrence**, § 48.4, où le rail temps réel canadien est nommé **sans jamais être dit lancé** (réserve F-29) ; **R-1 à R-3, R-5 à R-8 : zéro occurrence** |
| **Volumétrie cible** | ≈ **4 700 mots** de corps (§ 48.1 à § 48.5), **cible dérivée par front** : 14 000 mots au premier mouvement du Livre (TOC v0.25, Volumétrie — le chiffre de l'audit v0.3 pour ses **trois** fronts), dont **un** porté par ce chapitre, soit ≈ 4 700 ; les deux autres sont au ch. 47 (≈ 9 300). ☑ **Décompte publiable depuis G-2** ; **réel : 3 800 mots** par [`PRD/decompte.sh`](../PRD/decompte.sh), seule autorité de décompte — **−19,1 %**, ⚠ **re-mesuré à la contre-relecture du 28 juillet 2026** (2 793 et −40,6 % au commit de rédaction ; 3 305 et −29,7 % au commit de correction ; 3 779 et −19,6 % à la relecture). ⚠ **Les quatre mesures montent, et le motif se déclare plutôt qu'il ne se devine** : *les 474 mots de la relecture et les 21 de la contre-relecture sont de l'appareil de bornage* — état des portes re-constaté, deux renvois de section corrigés, exclusion de socle d'une entrée citée, cardinaux re-mesurés, un `F-xx` désambiguïsé —, ⚠ **à une exception près, et elle se nomme plutôt qu'elle ne se noie** : l'explicitation du § 48.1, où la relecture a nommé les trois questions que la taxonomie fait tenir ensemble et leur a donné leurs renvois. **Pas une ligne de contenu de section-lot n'a été ajoutée.** ⚠ **L'écart reste en défaut et son motif est celui du ch. 47** : *sur un front sans socle, la volumétrie mesure ce qu'on peut écrire sans fabriquer* — et **deux des cinq sections sont des lots d'instruction**. ⚠ **D-4 interdit l'amputation comme le gonflement** : l'écart se documente et ne se corrige pas |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.30, entrée du chapitre 48)* — une action d'agent produit des effets dans des systèmes d'enregistrement, et ce qui advient quand elle réussit à moitié — idempotence, compensation, réconciliation — **n'est documenté par rien de ce que la somme a instruit, ni du côté des protocoles (Livre I) ni du côté de l'encadrement (Livre III)** ; c'est en finance que le coût de ce silence est maximal (un virement à moitié réussi n'est pas un incident d'observabilité, c'est un écart comptable).

---

⚠ **Thèse réalignée au TOC v0.26** (décisions 8 et 14), sur la remontée **R-IV-65** ouverte par cette
pièce, **et inchangée depuis** : le plan est passé en v0.29 puis en **v0.30**, versions qui déclarent
l'une et l'autre n'avoir touché aucune thèse, et *la concordance mot à mot de la thèse citée
ci-dessus avec l'entrée du ch. 48 du TOC courant a été re-vérifiée le 28 juillet 2026*. La forme
antérieure écrivait « **n'est spécifié ni** par les protocoles **ni** par
l'encadrement » — un **quantificateur universel négatif qu'aucun balayage ne soutient**. Ce que le
corpus établit est une **absence de documentation**, au **degré 3** de l'échelle R-14 du Vol. III, et
*non un fait négatif vérifié*. **Le corps du chapitre n'a pas changé à la rédaction** : il écrivait
déjà l'énoncé sous la forme bornée. ⚠ **Le chapeau, en revanche, disséquait encore le libellé
antérieur ; il est réécrit sur la forme courante au commit du 28 juillet 2026** — *un corps qui
commente une thèse que sa propre tête ne porte plus fait se contredire la pièce sous les yeux du
lecteur qui ne lit pas ce bloc.*

⚠ **Ce bloc était absent du rendu `.html` jusqu'au 28 juillet 2026, et son emplacement en était la
cause** : placé **entre la thèse et le séparateur**, il tombait hors du corps que le générateur
projette. Il est déplacé **après le séparateur**, où les ch. 47 et 49 placent le leur. *Le défaut
n'était pas un rendu régénéré depuis un état intermédiaire mais une omission silencieuse du
générateur : le `.md` faisait foi et le `.html` ne le disait pas.* ⚠ **La dette est d'appareil et
elle reste ouverte** — *un contrôle de parité qui compare les titres de section ne voit pas cette
classe*, et rien de versionné ne l'attrape aujourd'hui.

⚠ **La thèse est déclarée *construction d'auteur, socle à constituer* par le TOC lui-même**, et elle
porte deux propositions de statuts inégaux qu'il faut séparer avant d'entrer dans le chapitre. La
seconde — *un virement à moitié réussi est un écart comptable* — est une **lecture d'auteur**, et
elle est reprise comme telle. La première — *cela n'est documenté par rien de ce que la somme a
instruit, ni du côté des protocoles ni du côté de l'encadrement* — est une **absence**, et la forme
que la thèse porte depuis son réalignement dit exactement à quoi elle est bornée : ⚠ **elle porte
sur le corpus instruit par la somme, non sur les protocoles ni sur l'encadrement eux-mêmes.** C'est
une *absence de documentation dans le corpus de la somme*, au **degré 3** de l'échelle R-14 du
Vol. III, **non un fait négatif vérifié** — et **aucun balayage documenté ne l'élève au-dessus de ce
degré**. ⚠ *La borne est désormais dans la thèse, et elle se lit comme une borne, non comme une
atténuation de style* : le chapitre ne peut pas écrire que les protocoles n'en disent rien ; il écrit
que rien de ce que la somme a instruit ne le documente, ce qui n'est pas la même proposition et
n'autorise pas la même conclusion.

⚠ **Un fait neuf du 28 juillet 2026 change ce que ce chapitre pourrait un jour établir, sans rien
changer à ce qu'il établit aujourd'hui.** Le **socle consolidé existe** depuis le franchissement de
G-3 : *pour la première fois, « ce que la somme a instruit » désigne un corpus fini, numéroté et
balayable*, là où la thèse visait jusqu'ici un objet qu'aucun instrument ne délimitait. **Le degré ne
bouge pas pour autant** — *un balayage de chaînes n'est pas un balayage sémantique*, et le conduire
est un acte d'instruction, non de relecture. ⚠ **R-IV-65 offrait deux issues et une seule a été
prise** : le réalignement de la thèse, ☑ soldé en v0.26 ; le **balayage documenté qui l'établirait**
ne l'a pas été, et il n'était alors conductible sur aucun corpus fini. *Il l'est depuis le 28 juillet
2026*, et le constat est porté au § 48.6 sans qu'un identifiant de remontée y soit alloué — *une
passe qui court en parallèle d'autres n'alloue pas dans une série partagée* (PRD §13).

## § 48.1 — Taxonomie des effets d'une action d'agent

> ⚠ **SIÈGE DE LA SÉMANTIQUE D'EFFET POUR TOUTE LA SOMME.** La matière — *idempotence,
> compensation, réconciliation* — est posée **ici une seule fois**. Le **ch. 1 § 1.5.2** et
> **§ 1.6.2.2** en posent les fondements **au grain pré-agentique** et y renvoient ; les **ch. 22
> § 22.5**, **ch. 23**, **ch. 24** et **ch. 27** l'**appliquent** et y renvoient nommément ; aucun de
> ces chapitres ne la reconstruit. *C'est l'économie de la fusion côté « effets d'une action », et
> elle n'a lieu que si ces chapitres s'y tiennent.*

Lecture de l'auteur — la taxonomie qui suit est une construction de ce chapitre. **Ce que le socle
établit** : rien — **aucune des trois classes ne résout contre une entrée numérotée**, ni du socle
consolidé, ni d'aucun des trois socles sources. **Ce qu'il n'établit pas** : que ces trois classes
soient les bonnes, qu'elles soient exhaustives, ni qu'une action réelle se rattache à une seule
d'entre elles. Elle vaut comme **vocabulaire de travail** — et son seul mérite est de faire tenir
ensemble trois questions que les chapitres amont posent séparément : *le rejeu d'un appel d'outil*
(ch. 4 § 4.4.2), *l'annulation sémantique d'une étape engagée* (ch. 1 § 1.6.2.2) et *la reprise d'une
trajectoire interrompue* (ch. 22 § 22.5).

| Classe d'effet | Ce qu'une reprise produit | Ce qui la borne | Où la somme en traite |
|---|---|---|---|
| **Lecture** | rien : rejouer une lecture ne change pas l'état du système d'enregistrement | le coût et la fraîcheur, non la correction | ch. 1 § 1.5.2 (déduplication, condition de version) |
| **Écriture** | un doublon, **sauf si l'opération est idempotente** | l'idempotence est une **propriété de l'outil**, jamais du protocole qui l'invoque (ch. 4 § 4.4.2) | § 48.2 ; ch. 22 § 22.5 (reprise d'un moteur durable) |
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
spécifications protocolaires en disent — *à instruire, jamais présumé* ».** Aucune passe
d'instruction protocolaire n'a été conduite pour ce chapitre. Ce qui suit est donc **ce que des
pièces rédigées de la somme portent déjà**, plus l'état de l'absence — jamais une lecture de
spécification faite ici.

**Ce que la somme porte, et c'est peu mais c'est précis.** Le **ch. 8 § 8.2.3** établit que les
**tâches asynchrones** du protocole agent-outil sont **expérimentales**, que le mécanisme *se
rapproche, sans s'y identifier*, de l'exécution durable de l'intégration d'entreprise, et surtout
qu'il **ne fournit pas les garanties de reprise et d'idempotence** d'un moteur durable — *leur
contrat ne saurait être présenté comme stable*. ⚠ **C'est un énoncé sur ce que le mécanisme ne
démontre pas, et il est repris tel quel** : R-02 du Vol. III veut qu'un mécanisme se qualifie par ce
que sa spécification démontre, jamais par la parenté qu'on lui prête. *Le rapprochement avec un
moteur durable est précisément ce que le ch. 8 refuse de tenir pour une équivalence.*

**Ce que la somme porte du côté de l'outil.** Le **ch. 4 § 4.4.2** range l'idempotence parmi les
propriétés de conception d'un outil — *une même requête répétée produit le même état*, ce qui protège
des réessais et des duplications d'effets de bord. Lecture de l'auteur — **la conséquence est
dissymétrique et elle est le cœur de la section** : *l'idempotence est une propriété de l'outil
invoqué, pas du protocole qui l'invoque, ni de l'agent qui décide de l'invoquer.* **Ce que le socle
établit** : la propriété et son intérêt, par le ch. 4. **Ce qu'il n'établit pas** : qu'un protocole
agentique la prescrive, l'exprime dans un champ, ou permette à un appelant de savoir si l'outil
qu'il appelle la possède.

⚠ **L'absence, à son degré exact.** **Le socle consolidé de la somme ne documente aucune
spécification protocolaire prescrivant l'idempotence d'un appel d'outil, ni aucun champ qui la
déclarerait — degré 3, absence de documentation dans le corpus de cet ouvrage.** Deux bornes
accompagnent ce constat, et sans elles il serait faux. *(1)* Le balayage sur lequel il s'appuie n'a
pas été mené pour cette question : le **ch. 20 § 20.1** rapporte l'énumération des **huit champs** du
type qui décrit un outil, dont aucun ne porte de version, d'empreinte ni de signature — *ce
balayage-là portait sur l'intégrité, non sur l'idempotence*, et il était **borné à une page d'une
révision nommée**.
*L'étendre à l'idempotence serait exactement l'élargissement que le contrôle de bornage du Vol. III
écarte.* *(2)* ⚠ **Une révision majeure du protocole agent-outil est annoncée au brouillon** — dont la
date n'est pas confirmée à la source (R-09 du Vol. III) — et **tout constat de cette section est à
rejouer sur la révision publiée** : il ne vaut pas par avance pour elle.

**Le lot d'instruction, formulé pour qu'il soit ouvrable.** *Question* : une spécification
protocolaire agentique prescrit-elle, exprime-t-elle ou permet-elle de déclarer l'idempotence d'une
opération invocable, et sous quelle forme un appelant peut-il l'établir avant d'invoquer ?
*Corpus à ouvrir*, ⚠ **nommé par ses identifiants et non par des périphrases, faute de quoi le critère
de clôture ne serait pas exécutable** : les pages de définition d'outil des révisions courantes de
**MCP** (agent-outil) et d'**A2A** (agent-agent), les deux protocoles dont le **ch. 8** tient
l'anatomie, dans leur texte intégral ; côté IETF, **RFC 9110** (*HTTP Semantics*, Fielding, Nottingham
et Reschke, 2022), qui définit les méthodes idempotentes — ⚠ *le document de l'IETF sur les clés de
requête (« Idempotency-Key ») n'est nommé par aucune pièce ni par aucune relève du plan : son
identifiant est à établir à l'ouverture du lot, et cet établissement en est le premier acte* ; les
contrats de tâche des moteurs d'exécution durable relevés au ch. 22 § 22.5.
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
fournisse un. **Le socle consolidé ne documente aucun dispositif de compensation dont la portée soit
une trajectoire d'agent non fixée à la conception — degré 3.**

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
ailleurs** : cette section est, selon le TOC — **v0.25 au constat d'origine, mention reconduite
jusqu'à la v0.30** —, la **seule occurrence de « sagas » de toute la zone des chapitres**, et elle
l'est **au grain d'une action unique**. *C'est ce constat, et non une
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
imposée** : le rail temps réel canadien se nomme sans jamais s'écrire « lancé » (réserve **F-29 du
Vol. II**, garde-fou **R-4** du même volume — ⚠ *le Vol. III porte lui aussi une F-29, sur tout autre
objet : la forme nue serait indécidable*) ; le ch. 33 en est le siège, et ce chapitre n'en date rien.

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
**Le socle consolidé ne documente aucun mécanisme de réconciliation dont le périmètre déclaré couvre
les effets d'une action d'agent — degré 3.**

⚠ **Trois renvois de cette section portent la matière que le chapitre n'a pas, et leurs trois cibles
sont désormais dans le MÊME état — ce qui déplace la réserve sans la lever.** Le plan situe les flux
ISO 20022 au **ch. 33** et au **ch. 45 § 45.12**, et le **trou de responsabilité** au **ch. 36
§ 36.2.6** : ⚠ **les trois chapitres sont écrits et committés depuis, hors de cette passe, et aucun
n'a été relu par elle** — les deux derniers étaient encore des renvois de plan à la rédaction. *La
conséquence est à écrire plutôt qu'à taire : la partie de cette section qui rattacherait la sémantique
d'effet à un flux de règlement réel reste celle qui manque, mais elle ne manque plus faute de
chapitre — elle manque faute d'une confrontation que cette passe n'a pas conduite, et **une cible qui
existe sans avoir été lue n'est pas plus opposable qu'une cible absente**.*

## § 48.5 — Tracer l'effet, pas seulement l'appel

**La question est étroite : ce qu'une trace d'exécution enregistre est un appel, non son effet.** Le
plan situe le *chaînon manquant* au **ch. 38 § 38.5** — ⚠ **écrit et committé depuis, hors de cette
passe, et non relu par elle** —, et ce chapitre le prolonge au seul grain qui lui appartient : *ce
qui manque n'est pas la trace de l'appel, c'est la jointure entre l'appel tracé et l'effet enregistré
ailleurs.*

**Deux constats hérités du Vol. III cadrent la difficulté, et ils sont plus précis que ce que ce
chapitre pourrait produire.** *(1)* Sa **lacune 21** — *corrélation entre trace d'exécution et chaîne
de mandat protocolaire* — est déclarée **non instruite** : la pièce de jonction n'a été ouverte par
aucun de ses lots. *(2)* Le `Monographie` **§26.3** du même volume établit que les compteurs d'appels
des conventions relevées comptent les appels **directs**, les appels de sous-agents ou d'agents
auxquels la tâche est transférée étant **attribués séparément** — de sorte qu'*une chaîne de
délégation n'est pas reconstituable par sommation de ces compteurs*, non par insuffisance de
l'instrument mais **par construction déclarée de sa sémantique**. ⚠ **Les deux constats entrent sous
G-4 non franchie** : ils viennent d'un volume qui se déclare *rédigé mais non publiable*, et *le
volet de fond de la collation reste dû*.

⚠ **Le franchissement de G-3 a durci la réserve du second plutôt que de la lever, et c'est le fait
neuf de cette section.** L'entrée qui l'établit est **`F-96` du Vol. III**, portée par sa source avec
la marque *vote dû, non conduit* ; le **socle consolidé l'EXCLUT** — elle est l'une des **deux
entrées écartées pour dette de vote**, avec **`F-92` du Vol. III** (§6.1 du socle). ⚠ **Elle ne porte
donc aucun identifiant `S-nnn` et n'est versable à aucun titre** : *elle reste citable avec sa
marque, exactement comme ici, et elle ne peut jamais devenir centrale.* La **lacune 21**, elle, entre
au socle avec l'entrée qui la déclare — **`S-140`**, dont la re-datation du 28 juillet 2026 constate
qu'elle **demeure ouverte et non instruite**. *La réserve du premier constat trouve donc un appui au
socle, celle du second une exclusion — et aucun des deux ne devient un fait.*

Lecture de l'auteur — **ce que ces deux constats permettent de dire de l'effet, et c'est neuf :**
si une chaîne d'appels n'est pas reconstituable, *l'effet observé au bout de la chaîne n'est
rattachable à aucun mandat déterminé*. **Ce que le socle établit** : la sémantique des compteurs et
la non-instruction de la jointure (Vol. III, avec ses réserves). **Ce qu'il n'établit pas** : qu'une
clé de jointure existe, ni qu'aucune n'existe. **Le socle consolidé ne documente aucune clé
rattachant un effet enregistré à la trace de l'appel qui l'a produit — degré 3.**

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

⚠ **Le lot d'instruction, et il commence par un identifiant qui manque.** *Question* : la taxonomie
des quatre divergences résiste-t-elle à l'ouverture de son texte, et l'une des quatre porte-t-elle
une clé rattachant un effet enregistré à l'appel qui l'a produit ? *Corpus à ouvrir* : ⚠ **la relève
v0.10 du plan ne porte ni identifiant arXiv, ni titre, ni auteurs pour cette préimpression de mai
2026 — seule sa date et ses quatre divergences nommées la désignent.** *Établir cet identifiant est
le premier acte du lot, non son résultat* : sans lui, aucun tiers ne peut ouvrir la même source, et
*un critère de clôture qui ne nomme pas la source qu'il attend n'est pas opposable.* S'y ajoutent les
entrées nommées ci-dessus : **`S-140`** pour la **lacune 21**, et **`F-96` du Vol. III** pour le
`Monographie` **§26.3** — ⚠ *cette dernière hors socle consolidé, l'instruction du lot devant donc
passer par sa source et non par une ligne de l'Annexe B.* *Critère de clôture* : le texte de la
préimpression, cité par son identifiant et sa version, énonçant la clé de jointure **ou** son
absence. *Échec documenté* : si le texte ne la porte pas, l'énoncé qui en sort reste au **degré 3**,
et la préimpression sort du corpus candidat plutôt que d'y demeurer indéfinie.

☑ ⚠ **DEUX DEMI-RÉPONSES EXISTENT DÉJÀ, et ne pas les inventorier était le reproche le plus fondé
que l'arbitrage externe adresse à ce chapitre.** *La question qu'il pose est neuve ; le domaine n'est
pas vierge, et une question neuve posée sur un domaine réputé vierge est une question mal posée.*
Les deux ont été relevées à leur source le 30 juillet 2026 — **fiches de document, non textes
extraits**.

**Première demi-réponse — l'en-tête d'idempotence, côté appel** (relève le § 48.2). Le brouillon
**`draft-ietf-httpapi-idempotency-key-header`**, *The Idempotency-Key HTTP Header Field*, de **Jena et
Dalal**, groupe de travail **httpapi** de l'IETF, spécifie un en-tête par lequel un client marque une
requête non idempotente — POST, PATCH — d'une clé permettant au serveur de **reconnaître un réessai
plutôt que de l'exécuter deux fois**. ⚠ **Son statut se dit à chaque mention et il est sévère
(R-09)** : **révision -07 du 15 octobre 2025**, et le document est **EXPIRÉ** — *il n'a pas atteint
le stade de RFC, et rien n'établit qu'il l'atteindra.* ⚠ **La conclusion du § 48.2 n'est donc pas
levée** : *l'écosystème n'a même pas d'en-tête normalisé pour dire « ceci est un réessai » — il en a
eu un projet, et ce projet a expiré*, ce qui est un constat plus dur que l'absence pure.

**Seconde demi-réponse — la clé de bout en bout, côté effet** (relève le § 48.4 et la question
propre de cette section). L'écosystème des paiements normalisés porte depuis des années **exactement
l'objet que ce chapitre déclare introuvable** : l'**UETR** — *Unique End-to-end Transaction
Reference* —, identifiant **UUID de version 4** (RFC 4122), **obligatoire** dans les messages de
valeur ISO 20022 `pacs.008`, `pacs.009` et `pacs.004`, **inchangé sur toute la chaîne de paiement**,
et exploité par le dispositif de suivi qui recueille l'état auprès de chaque établissement traversé.
S'y ajoute la **pratique de réconciliation** attachée — messages d'exception et d'investigation
adossés à cette même clé.

⚠ **Quatre bornes, et la troisième interdit d'en conclure ce qu'on aimerait en conclure.** *(1)*
**L'UETR répond à la question dans le domaine du paiement, et il y répond bien** : *une clé unique,
obligatoire, immuable, portée par le message lui-même et non par l'infrastructure qui le transporte.*
*(2)* ⚠ **Il ne rattache pas un effet à l'appel d'agent qui l'a produit** : il rattache un **message
de paiement** à ses **états successifs**. *Entre l'appel d'outil qu'un agent émet et le `pacs.008`
qu'un système bancaire finit par produire, l'UETR ne dit rien* — **la jointure que ce chapitre cherche
reste absente, degré 3**, et l'écrire autrement serait la transposition abusive que le ch. 22
proscrit. *(3)* ⚠ **Le patron, en revanche, est instructif et il est transférable** : *une clé de
jointure ne s'obtient pas en corrélant des traces après coup — elle s'obtient en la rendant
**obligatoire dans le contrat**, portée par la charge utile, immuable, et vérifiable par chaque
maillon.* **Lecture de l'auteur** : c'est la seule voie que ce chapitre puisse nommer, et **le socle
ne l'établit pour aucun protocole agentique** — ni MCP, ni A2A, ni AP2 n'imposent un identifiant de
bout en bout de cette nature. *(4)* **Aucun des deux ne monte au socle** : repérages datés, ni l'un ni
l'autre extrait.

⚠ **Le lot du § 48.5 s'en trouve élargi, non clos** : à la préimpression de mai 2026 s'ajoutent
**deux corpus nommés et opposables** — le registre de documents de l'IETF pour l'en-tête
d'idempotence, le corpus ISO 20022 pour l'UETR et les messages d'investigation. *Un lot qui nomme
trois corpus est exécutable ; un lot qui n'en nommait qu'un, dont l'identifiant manquait, ne l'était
pas.*

⚠ **Ce que ce chapitre lègue, et ce qu'il ne lègue pas.** Il lègue **une taxonomie de travail**
(§ 48.1), **deux lots d'instruction** (§ 48.2, § 48.5) — ⚠ *le second élargi le 30 juillet 2026 à
deux corpus nommés* — et **le siège** que cinq pièces rédigées attendaient. Il ne lègue **aucun
mécanisme** : ni idempotence prescrite, ni compensation spécifiée, ni clé de jointure — ⚠ *mais il
lègue désormais le **patron** d'une clé de jointure qui fonctionne ailleurs, et la borne qui interdit
de la transposer sans travail.* *La somme sait désormais nommer ce qui advient quand une action d'agent réussit à
moitié ; elle ne sait pas encore ce qu'un exploitant doit en faire, et le ch. 49 § 49.14 l'enregistre
à ce titre.*

---

## § 48.6 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.**

**Ce qui est enfreint.** Portes **G-3**, **G-5** et **G-6**, ouvertes à la rédaction ; volet résiduel
de **G-1** non instruit ; **ordre de rédaction du PRD §6** — ce mouvement vient en cinquième
position, après les ch. 41-46. Instruction d'auteur du 27 juillet 2026.

⚠ **Deux de ces quatre états ont bougé le 28 juillet 2026, et l'infraction ne bouge pas avec eux.**
☑ **G-3 est FRANCHIE** (PRD v0.14) : le socle consolidé existe, **159 entrées**, re-daté à la source.
☑ **Le volet de FAITS du volet résiduel de G-1 est levé** ; ☐ **celui des relèves reste dû**, et
c'est celui dont le § 48.5 dépend. ☐ **G-5 et G-6 restent ouvertes.** ⚠ *Une porte franchie le
lendemain ne rétroagit pas sur la pièce écrite la veille : ce chapitre reste rédigé hors portes, et
le seul effet du franchissement est de rendre ses énoncés d'absence **vérifiables** — non de les
vérifier.*

⚠ **Les deux décisions d'auteur que ces portes attendaient ont été prises depuis, et l'état se lit en
deux temps.** *À la rédaction*, **D-2** et **D-3** n'étaient prises ni l'une ni l'autre. *Depuis le
27 juillet 2026*, ☑ **D-2 est prise** — sections dans l'existant, sans chapitre neuf ; ce chapitre
n'en est pas un point d'atterrissage, les deux étant au ch. 47 § 47.8.1 et au ch. 50 § 50.2 —, et
☑ **D-3 est prise** — matière neuve en **trois lots d'instruction ouverts**, **retrait non exécuté**,
⚠ **publication du premier mouvement bloquée jusqu'à leur clôture, une instruction infructueuse
valant retrait**. **Les deux lots de ce chapitre — § 48.2 et § 48.5 — sont le lot L3 de D-3.**
⚠ **Aucune porte n'est franchie pour autant** : *une décision prise n'est pas une porte franchie*, et
l'infraction de rédaction n'est pas rattrapée par l'arbitrage qui l'a suivie.

1. **Aucun énoncé n'est central au sens de CA-IV-01.** Le régime applicable est le plus dur des trois
   (PRD §7.2, « Matière neuve ») : **toutes** les affirmations centrales au vote adversarial, plancher
   « sources primaires seules ». **Zéro vote, zéro extraction.**
2. **Les décomptes sont publiables** (G-2). Écart de **−19,1 %** sur la cible dérivée par front —
   ⚠ **re-mesuré à la contre-relecture du 28 juillet 2026** : −40,6 % au commit de rédaction,
   −29,7 % au commit de correction, −19,6 % à la relecture, **−19,1 % ici**, l'écart se réduisant
   par ajout d'appareil et **jamais par ajout de contenu de section-lot**.
3. **Les renvois se partagent en deux régimes, et non plus trois.** ⚠ **Les cinquante chapitres du
   plan existent en brouillon** — décompte qui a bougé **deux fois** pendant la rédaction de cette
   pièce, les Livres III et IV ayant été écrits puis committés **en parallèle, hors de cette passe**,
   portant le corpus de 25 à 50 pièces de chapitre. **Aucun renvoi de plan ne subsiste donc**, et ce
   qui subsiste est plus exigeant à déclarer : **la part du corpus que la présente passe n'a pas
   relue**. ⚠ **Elle n'est pas cardinalisée ici, et l'abstention est la règle plutôt que le renoncement**
   (décision 16 du TOC) : *un cardinal de pièces non relues se re-mesure au commit, et cette pièce ne
   voit pas le commit qui la porte* — le domaine se lit au groupe *(b)*, qui est exhaustif pour ce
   chapitre. **(a)** Résolvent contre du **texte rédigé, relu par cette passe** : ch. 1 § 1.5.2 et
   § 1.6.2.2, ch. 4 § 4.4.2, ch. 8 § 8.2.3, ch. 20 § 20.1 — ⚠ *ces deux renvois de section sont
   corrigés à la relecture du 28 juillet 2026 : la pièce écrivait « ch. 4 § 4.6 », qui est la note de
   statut **du ch. 4**, et « ch. 8 § 8.3 », qui est la section de gouvernance **du ch. 8** ; **la
   matière citée est bien celle des § 4.4.2 et § 8.2.3**, vérifiée sur pièce* — et **ch. 47, ch. 49
   § 49.9 et § 49.14**, rédigés dans la **même passe de rédaction que ce chapitre**, non par la
   relecture. ⚠ *Le « ch. 16 § 16.1 » que cette liste portait avait
   déjà été retiré au commit du 28 juillet 2026 : aucun renvoi du corps ne le résolvait.* **(b)**
   Résolvent contre du **texte rédigé hors de cette passe et non relu par elle** : ch. 22 § 22.5,
   ch. 23, ch. 24, ch. 27, ch. 33, ch. 36 § 36.2.6, ch. 38 § 38.5, ch. 45 § 45.12 — ⚠ *les deux
   derniers étaient encore des renvois de plan à la rédaction ; **l'existence de leur cible est
   vérifiée, son contenu ne l'est pas**.*
4. **Une matière est absente par décision d'auteur, non par omission** : l'accord entre agents sous
   asynchronie et défaillance partielle, fermé au ch. 48 par **D-7**. *La déclarer est la seule chose
   que ce chapitre pouvait faire ; l'écrire aurait rouvert la décision.*

**Remontées ouvertes par ce chapitre — et leur issue.** ⚠ **Les trois sont SOLDÉES**, et le dire est
la moitié de l'information : *une remontée soldée ne rend pas la pièce recevable, elle constate
qu'aucune question n'attend plus de réponse qui ne soit déjà tranchée.*

- **R-IV-64 — non bloquante, de siège et d'appareil ; elle constatait qu'un siège existait avant sa
  pièce.** **Quatre pièces du Livre III** — ch. 22 § 22.5, ch. 23, ch. 24, ch. 27 — et **deux sections
  du ch. 1** déclaraient que « la sémantique d'effet est au **ch. 48**, qui en est le siège », **alors
  que le TOC ne désignait nulle part ce chapitre comme siège** et que `check-sieges.py` n'en portait
  aucune trace. ⚠ *Un siège qu'aucun plan ne désigne et que cinq pièces citent est un siège qui
  disparaît au premier remaniement.* ☑ **Soldée — TOC v0.26 et appareil** : le siège est **désigné à
  l'entrée du ch. 48**, comme la v0.25 l'avait fait pour le tri prospectif au ch. 49 § 49.0, **versé
  à `check-sieges.py` et validé par mutation**.
- **R-IV-65 — non bloquante, de thèse.** La thèse citée affirmait que la sémantique d'effet « n'est
  spécifié ni par les protocoles (Livre I) ni par l'encadrement (Livre III) ». ⚠ **C'était un
  quantificateur universel négatif qu'aucun balayage ne soutenait** : le corpus de la somme n'en
  documente rien — **degré 3** —, ce qui n'établit pas l'absence. *La classe de défaut est celle que
  la décision 14 du TOC nomme, et le chapitre a écrit son corps sous la forme bornée sans toucher à
  la thèse.* ☑ **Soldée — TOC v0.26, décisions 8 et 14** : la thèse est réalignée sur la forme bornée.
  ⚠ **La seconde issue qu'elle proposait — « ou balayage documenté qui l'établirait » — n'a PAS été
  prise, et elle vient de devenir conductible** : le socle consolidé donne pour la première fois un
  corpus fini à balayer. *Le constat est consigné ici sans identifiant de remontée* — l'allocation
  dans une série partagée relève de la passe d'arbitrage (PRD §13), et **cette relecture ne dispose
  pas de l'état des séries des autres passes**.
- **R-IV-66 — non bloquante, de dépendance.** Le **§ 48.4** était la section dont la matière dépendait
  le plus de chapitres que la passe de rédaction n'avait pas relus : ch. 33, ch. 36 § 36.2.6, ch. 45
  § 45.12 — les deux derniers alors **non rédigés**. ⚠ *Le plan plaçait ce mouvement en dernier
  précisément pour cette raison ; l'ordre a été enfreint, et le § 48.4 en porte le coût.* ☑ **Soldée
  — PRD v0.11, jalon J-IV-8** : la re-vérification du § 48.4 après la rédaction du Livre III et du
  second mouvement du Livre IV est **portée au jalon**. ⚠ **Elle n'est pas exécutée pour autant** :
  les trois chapitres existent désormais et **aucun n'a été lu par la présente relecture** ; *porter
  une obligation à un jalon est un engagement, non une exécution.*

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.25 — structure
inchangée jusqu'à la v0.30** — § 48.1 à § 48.5, dans l'ordre exact. La **table d'appuis** est
respectée : les adossements internes sont **des renvois, jamais des sources**, et **aucune entrée
F-xx, aucun garde-fou hérité** n'est revendiqué. **Le siège est posé et marqué** (§ 48.1), et **versé
à [`PRD/check-sieges.py`](../PRD/check-sieges.py) dans la même passe**, avec son harnais de mutation
rejoué. **Aucun siège d'un autre chapitre n'est reconstruit** : les résultats d'impossibilité et le
patron saga restent au **ch. 1 § 1.6.2.2**, l'exécution durable au **ch. 22 § 22.5**, l'anatomie des
tâches asynchrones au **ch. 8 § 8.2.3**, l'énumération des huit champs au **ch. 20 § 20.1**. **La
matière fermée par D-7 n'est pas écrite.** **Les neuf occurrences de R-14 portent leur degré**, dont
huit au **degré 3** — ⚠ **cardinal et localisation re-mesurés à la relecture du 28 juillet 2026 sous
la règle littérale, corps seul, puis rejoués à la contre-relecture du même jour et retrouvés à
l'unité** —, et **aucune absence propre à ce chapitre n'est écrite comme fait négatif vérifié**.
**Les deux occurrences de R-02**, toutes deux au § 48.2, énoncent ce que la source démontre **et** ne
démontre pas — dont le refus explicite d'assimiler les tâches asynchrones à un moteur durable.
**Les quatre divergences de la préimpression sont nommées, ses deux réserves portées, et aucun de ses
chiffres n'est repris.** **Le rail temps réel canadien n'est jamais dit lancé** (R-4) — ⚠ *et la
réserve qui l'impose porte son volume depuis la contre-relecture du 28 juillet 2026 : la série
`F-xx` est allouée dans deux socles, et « F-29 » nu y était indécidable* (décision 7 du TOC).
Enfin, **la réserve de vote de l'entrée du Vol. III est reprise avec l'entrée**, jamais détachée
d'elle.
