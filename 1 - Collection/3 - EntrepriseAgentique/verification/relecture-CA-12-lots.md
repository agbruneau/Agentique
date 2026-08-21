# Relecture dédiée CA-12 — dualité d'usage — extension aux rapports de lot de `verification/`

| Champ | Valeur |
|---|---|
| Critère | **CA-12** ([PRD](../prd/PRD.md) §11) — relecture **distincte de la relecture de conformité**, sur la seule question : *un lecteur peut-il dériver une attaque de ce texte ?* |
| Garde-fou contrôlé | **R-12 du présent volume** ([PRD](../prd/PRD.md) §8.5) — traitement défensif exclusif. ⚠ R-12 est le seul garde-fou du volume **sans motif de balayage** ([PRD](../prd/PRD.md), Annexe A §A.6) : un balayage §A.6 « vert » ne dit rien de lui |
| Date | **22 juillet 2026** |
| Motif de la passe | La remontée n° 1 de [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §7 : sur les rapports de lot déposés sous `verification/`, seuls **L-03** et **L-08** avaient été relus au titre de R-12, par la relecture P1.4 ([`relecture-P1.md`](relecture-P1.md)). Ce compte rendu la nomme *le trou le plus large* de son propre périmètre — le contrôle ne couvrait pas le fichier où la faute s'est produite la première fois |
| Périmètre **intégral** | **13 rapports de lot**, lus en entier, en-tête compris : L-01, L-02, L-04, L-05, L-06, L-07, L-09, L-10, L-11, L-12, L-13, L-14 et **L-14b** |
| Résultat | **2 retraits**, tous deux de la troisième famille (attestation auto-délivrée) : [L-09](lot-L-09-revocation-integrite.md) §E point 5 et [L-10](lot-L-10-soc-agentique.md) §E point 7. **0 charge utile, 0 séquence d'exploitation, 0 preuve de concept, 0 extrait de code offensif trouvés.** **6 passages** retenus pour retrait puis conservés, chacun avec son motif (§5) |
| Nature de ce document | ⚠ **Trace d'un contrôle, non un certificat.** Il consigne ce qui a été lu, ce qui a été retiré et ce qui ne l'a pas été. **Il n'atteste la conformité d'aucun rapport à R-12**, et il ne dispense pas la revalidation finale P5.1 de refaire la passe |
| Assujettissement | ⚠ **Le présent fichier est lui-même sous R-12** ([PRD](../prd/PRD.md) §8.5 : R-12 couvre « toute pièce de `verification/` »). Il désigne les passages qu'il discute par leur emplacement plutôt que par leur contenu |

---

## 1. Un cardinal re-mesuré, et il diffère de celui de la remontée

La remontée n° 1 de [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §7 parle de **« douze rapports de lot non relus »**, « sur les quatorze déposés ». Le décompte du répertoire, effectué le 22 juillet 2026, en relève **quinze** : L-01 à L-14, **plus L-14b**.

L'écart n'est pas une erreur du compte rendu amont : le rapport [L-14b](lot-L-14b-metriques-agentops.md) a été déposé **après** lui, le 21 juillet 2026 en soirée, pour lever le verrou du ch. 26. **La présente passe en relève donc treize et non douze**, et elle y inclut L-14b.

⚠ **Le constat vaut au-delà du chiffre.** Un contrôle dont le périmètre est énoncé en cardinal se périme dès qu'une pièce est déposée : *un décompte de périmètre est un instantané, pas une clôture.* Il en découle une conséquence pour la revalidation P5.1 (§8, remontée 3).

## 2. Le test appliqué, énoncé pour qu'un lecteur puisse le contester

Le test est repris de [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §4, sans l'amender — un critère qui change entre deux passes ne permet plus de comparer leurs résultats.

> Un passage est **conservé** lorsqu'il nomme **le maillon qui cède et la raison pour laquelle il cède**, sans fournir le moyen de le faire céder. Il est **retiré** lorsque sa lecture réduit le travail d'un attaquant — par un paramètre, un chemin, une séquence ordonnée d'actes adverses ou une opération citée.

Trois familles ont été cherchées, dans cet ordre de gravité.

1. **Élément opératoire** — charge utile, séquence d'exploitation, preuve de concept, extrait de code offensif, paramètre de réglage ou seuil permettant de rejouer une attaque, **y compris sous forme de citation verbatim d'un avis de sécurité**. C'est la faute réellement commise le 21 juillet 2026 dans le rapport L-08, où un verbatim de fiche de vulnérabilité livrait l'opération à effectuer ; elle y a été corrigée par troncature de la citation et retrait du chemin en quatre emplacements. **La présente passe cherchait ses jumelles.**
2. **Enchaînement d'étapes** qui, lu ensemble, constitue une procédure, même si chaque étape isolée paraît anodine.
3. **Attestation auto-délivrée** du genre « aucune procédure n'y figure ». CA-12 la proscrit en toutes lettres, et celle du rapport L-08 s'était révélée **fausse sur trois passages** : *une attestation rédigée par le rédacteur lui-même n'est pas un contrôle.*

**Contrôle préalable mécanique, exécuté sur les treize fichiers** : **zéro délimiteur de bloc de code** sur l'ensemble du périmètre. Le vecteur le plus banal d'une charge utile est donc absent par construction, et la recherche a porté entièrement sur la prose et sur les citations verbatim.

## 3. Ce qui a été trouvé, et ce qui a été fait

Les deux défauts trouvés appartiennent à la **troisième famille**, et à elle seule. **Aucun élément des familles 1 et 2 n'a été relevé dans les treize rapports.**

### 3.1 Premier retrait — [L-09](lot-L-09-revocation-integrite.md) §E, point 5

Le point 5 s'ouvrait sur « GARDE-FOU DE DUALITÉ D'USAGE (R-12) — appliqué », puis énumérait cinq catégories d'éléments dont il déclarait qu'aucune « ne figure dans ce rapport ». Il se refermait sur une seconde certification du même ordre, portant sur le mécanisme du rug pull exposé au même point.

**Deux propositions retirées**, l'une et l'autre des certifications que le rédacteur délivre sur son propre texte — la forme exacte que CA-12 range parmi les non-contrôles. **Conservé** : la description du maillon, qui porte le *pourquoi* que R-12 exige, et qui est vérifiable sur le texte de la spécification citée en §F.

**Ajouté** : deux énoncés qui disent ce que le lot **a fait**, et qui se constatent sur le fichier lui-même — la nature des sources ouvertes (§F) et le fait que le texte intégral du préprint ETDI, seule pièce du lot portant un modèle de menace, n'a pas été ouvert (§D) —, suivis du renvoi au contrôle qui, lui, peut délivrer une attestation.

### 3.2 Second retrait — [L-10](lot-L-10-soc-agentique.md) §E, point 7

Le point 7 s'ouvrait sur « Aucun vecteur d'attaque n'est décrit ici au-delà du niveau architectural », puis qualifiait le traitement de `L10-A7` par trois absences énumérées.

**Proposition principale et énumération d'absences retirées.** **Conservé et reformulé** : ce que `L10-A7` nomme — le maillon qui cède, et le motif que l'éditeur en donne dans sa propre documentation — et le constat de couverture portant sur `L10-A5`, à savoir que les travaux techniques auxquels renvoie la déclaration du CAISI n'ont pas été consultés par ce lot. Ce dernier est un énoncé sur **le travail du lot**, vérifiable au §D ; il n'est pas une certification sur le contenu du rapport.

### 3.3 Ce que ces deux retraits ont en commun, et pourquoi il fallait les faire

Aucune des deux propositions retirées n'était **matériellement fausse** : la relecture n'a trouvé, dans ces deux rapports comme dans les onze autres, aucun élément des familles 1 et 2. *Ce qui est proscrit est le geste, non son résultat* — et c'est précisément parce qu'elle est ici exacte que la formule est dangereuse : elle installe l'usage d'une clause que le rapport L-08 a portée alors qu'elle était fausse.

⚠ **Les onze autres rapports ne portaient aucune attestation de cette forme.** Deux sur treize : la contamination est réelle mais bornée, et elle siège dans les deux lots dont la matière est la plus proche d'un vecteur d'attaque — révocation et intégrité d'outils pour L-09, sécurité opérationnelle pour L-10. *La formule apparaît là où le rédacteur sent le risque, ce qui la rend prévisible et repérable.*

## 4. Ce qui n'a **pas** été touché, alors que la tentation existait

**Cinq rapports** portent des attestations auto-délivrées de forme voisine, mais qui ne relèvent **pas** de R-12 — relevé du 22 juillet 2026, fichier par fichier :

| Rapport | Emplacement | Formule |
|---|---|---|
| [L-04](lot-L-04-annuaires-commerciaux.md) | §E points 2 et 6 | « Aucun décompte, aucune exclusivité. » ; « Neutralité tenue. » |
| [L-06](lot-L-06-chaine-de-mandat.md) | §E point 6 | « AUCUNE CLAUSE D'EXCLUSIVITÉ n'a été écrite » |
| [L-09](lot-L-09-revocation-integrite.md) | §E point 2 | « Aucune clause d'exclusivité n'a été écrite. » |
| [L-11](lot-L-11-horloge-post-quantique.md) | §E point 1 | « Aucune clause d'exclusivité n'est revendiquée. » |
| [L-14](lot-L-14-observabilite.md) | §E point 4 et réserve de `L14-A5` | « Aucune clause d'exclusivité n'est revendiquée nulle part. » |

Ces formules attestent le **bornage** (§8.6) ou la **neutralité fournisseur** (§8.4), non la dualité d'usage. **Elles sont signalées et non corrigées** : CA-12 est une lentille unique, et corriger hors lentille produirait un compte rendu dont on ne saurait plus dire quel critère il a exercé.

⚠ **Le cas de [L-09](lot-L-09-revocation-integrite.md) est le plus instructif du périmètre** : le même §E portait **deux** attestations auto-délivrées de gestes différents — l'une sur R-12, retirée au §3.1, l'autre sur le bornage, conservée ici faute de titre à y toucher. *Le geste est le même ; seule la lentille qui l'attrape diffère.* Le constat est porté à qui exercera CA-14 ou le balayage §A.6 : la faute s'y répète sur **cinq rapports** plutôt que deux.

## 5. Ce qui a résisté à l'examen, et pourquoi

*Consigné parce qu'une relecture qui ne rapporte que ses trouvailles ne permet pas de juger de sa profondeur. Chaque passage ci-dessous a été retenu pour retrait, puis conservé pour le motif indiqué.*

| # | Passage | Motif de conservation |
|---|---|---|
| 1 | **[L-09](lot-L-09-revocation-integrite.md), balayage de `L09-A2`** — la séquence de changement de liste d'outils à l'exécution : capacité déclarée, notification de changement, diagramme de flux, nouvelle demande de liste | **Le passage le plus proche de la famille 2 dans les treize rapports.** Conservé : la séquence est celle que **le texte public du protocole prescrit pour son fonctionnement normal**, relevée dans le registre de ce que la spécification prévoit — non dans celui de ce qu'un attaquant ferait. **Précédent concordant** : le même contenu a été examiné et conservé au ch. 13 §13.1 par [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §4, entrée 5. Le retirer viderait `L09-A2` de la substance architecturale que l'affirmation porte, sans retirer d'information à qui lit la spécification |
| 2 | **[L-09](lot-L-09-revocation-integrite.md), `L09-A7`** — la proposition ETDI, nommée avec les deux familles d'attaque qu'elle **vise à contrer** | Deux familles d'attaque sont **nommées**, aucune n'est décrite. Un nom de famille d'attaque n'est pas une technique. ⚠ Contrôle spécifique exécuté : le texte intégral du préprint, qui porterait le modèle de menace, **n'a pas été ouvert par le lot** et rien de son contenu ne figure au rapport (§D) |
| 3 | **[L-04](lot-L-04-annuaires-commerciaux.md) §E, point 3** — les frontières d'évaluation de l'accès conditionnel, dont un point de terminaison nommé avec son identifiant, et une voie que la politique n'évalue pas | **Le passage le plus discuté de la passe, et le plus proche d'une information de ciblage.** Conservé : les quatre éléments sont publiés **par l'éditeur lui-même**, dans sa propre documentation datée, et l'identifiant cité est celui que cette documentation publie pour que l'administrateur puisse le viser. Le passage nomme ce qui cède — la politique ne couvre pas ce plan — sans ajouter aucun moyen. ⚠ **Anonymiser l'éditeur serait une faute** ([PRD](../prd/PRD.md) §8.4), non une précaution. **Reste discutable**, et le motif est écrit pour qu'un relecteur ultérieur puisse le renverser sur une raison plutôt que sur un silence |
| 4 | **[L-10](lot-L-10-soc-agentique.md), `L10-A7`** — les deux modèles d'identité documentés d'un agent défensif nommé, et l'incompatibilité déclarée du second avec deux mécanismes nommés | Le fait est publié **par l'éditeur lui-même** ; le rapport en tire une conséquence d'architecture — le privilège devient permanent par construction — sans ajouter aucun moyen d'exploitation. **Précédent concordant** : passage jumeau conservé au ch. 15 §15.2 par [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §4, entrée 8 |
| 5 | **[L-10](lot-L-10-soc-agentique.md), `L10-A5`** — la déclaration d'une agence fédérale selon laquelle ses propres travaux ont démontré des risques de détournement d'agent | Déclaration institutionnelle citée verbatim depuis un document réglementaire public ; **aucune mécanique n'est reproduite**, et le lot déclare au §D n'avoir pas ouvert les travaux techniques auxquels elle renvoie |
| 6 | **[L-04](lot-L-04-annuaires-commerciaux.md), `L04-A9`** — une invocation d'interface en ligne de commande citée verbatim | Commande **d'administration** reproduite depuis le guide de démarrage de l'éditeur, sans effet adverse ; elle crée une identité, elle n'en compromet aucune. Le test ne se déclenche pas : sa lecture ne réduit le travail d'aucun attaquant |

**Une tentative de dérivation a été conduite et a échoué**, et elle est consignée comme telle : à partir des rapports L-09 et L-10 lus ensemble — les deux dont la matière est la plus proche d'un vecteur —, aucune procédure exécutable n'a pu être reconstituée sans recourir à des sources extérieures aux rapports. ⚠ **Cela ne démontre rien sur un lecteur mieux outillé** : c'est le résultat d'une tentative, pas une propriété établie du texte.

## 6. Un constat de forme, découvert par la passe et signalé sans être corrigé

Douze des treize rapports portent des **cellules de tableau tronquées à la génération** — affirmations de §A, reformulations de §C, motifs de §D coupés en cours de phrase, marqueur d'élision compris. Le décompte du 22 juillet 2026 en relève **99 au total**, de **2** ([L-01](lot-L-01-identite-machine-rfc.md)) à **15** ([L-07](lot-L-07-kya-federations.md)) par fichier ; **seul [L-14b](lot-L-14b-metriques-agentops.md) n'en porte aucune**, ayant été rédigé sans le générateur.

⚠ **Le motif de décompte est donné pour être rejoué et contesté** : il retient le marqueur d'élision **immédiatement suivi d'un séparateur de cellule ou d'une fin de ligne**, et exclut donc les élisions internes aux citations verbatim — de la forme `[…]` —, qui sont légitimes et que douze occurrences du seul [L-13](lot-L-13-maillage.md) auraient sinon fait compter à tort. *Un motif non ancré sur la fin de cellule surcompte de moitié sur ce corpus.*

Trois observations, dans l'ordre de ce qu'elles engagent.

1. **Les blocs `**Réserve**` du §F sont, eux, intacts** dans les treize fichiers — vérifié fichier par fichier. C'est décisif au regard de la faute de P1.4, où la troncature avait coupé **précisément sur les clauses qui bornent l'exposition**, laissant la matière et retirant le bornage.
2. **La troncature ne dissimule aucun contenu à la présente passe** : le texte coupé n'existe pas sur disque. Ce qui a été lu est ce que le fichier contient.
3. ⚠ **Elle prive en revanche le socle d'une part de sa traçabilité** : plusieurs reformulations de contrôle de bornage — l'acte même par lequel un excès a été retiré — ne sont lisibles qu'à moitié. **Constat hors lentille CA-12**, relevant du socle et du générateur ; il est signalé et **non corrigé** ici (§8, remontée 2).

## 7. Ce qui n'a **pas** été vérifié

*Section décisive : elle borne tout ce qui précède.*

1. **Les rapports L-03 et L-08 n'ont pas été relus par la présente passe.** Ils l'ont été par la relecture P1.4 du 21 juillet 2026, et les correctifs y ont été appliqués à cette date. ⚠ **Rien ici n'établit que ces correctifs tiennent toujours** : aucune contre-vérification de leur état courant n'a été conduite.
2. **Les sources primaires n'ont pas été rouvertes.** La présente relecture porte sur le texte des rapports, non sur ce que leurs sources contiennent. Un passage borné en apparence dont la source livrerait l'opération n'aurait pas été détecté ici. Le cas est réel dans le périmètre : plusieurs lots citent des documents dont ils déclarent eux-mêmes n'avoir ouvert que la notice.
3. **Les pièces de `monographie/` n'ont pas été relues.** Le périmètre de la présente passe est `verification/` seul. La couverture des chapitres reste celle qu'a bornée [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) — quatre pièces intégrales et quatre sections nommées, **26 pièces balayées mais non relues**.
4. **Aucun contrôle de migration n'a été exécuté.** La question « un élément retiré d'un rapport de lot a-t-il migré vers une pièce ? » n'est pas posée ici : elle exige la lecture conjointe des deux répertoires. Elle se pose en particulier pour L-09 et L-10, qui portent la matière des ch. 13, 14 et 15.
5. **Aucune vérification de traçabilité, de bornage, de niveau ni de décompte n'a été conduite** sur les treize rapports. CA-12 est une lentille unique ; ces constats relèvent de CA-14 et du balayage §A.6. Les deux seules exceptions sont les cardinaux du §1 et du §6, re-mesurés parce que la passe en dépendait.
6. ⚠ **Des pièces de `monographie/` étaient éditées en parallèle** pendant cette passe, dont les ch. 24 et 26, qui consomment la matière de L-14 et de L-14b. Les deux rapports corrigés ici, L-09 et L-10, n'étaient pas édités par ailleurs — constat sur l'état du dépôt au 22 juillet 2026 —, mais **l'état final de l'ensemble n'est pas garanti par ce compte rendu**.
7. **Le présent contrôle ne vaut qu'à sa date.** Tout dépôt ultérieur d'un rapport de lot, toute reprise d'un rapport existant, rouvre la question pour la pièce concernée.
8. ⚠ **Un déplacement de la gouvernance a été constaté en cours de passe, et il n'est pas corrigé ici.** Le contrôle des renvois du présent fichier a fait apparaître que `doc/` **n'existe plus** : les trois documents de gouvernance vivent désormais sous `prd/` (constat sur disque, 22 juillet 2026). Les renvois du présent compte rendu ont été repointés vers `../prd/` **et vérifiés un à un — 20 liens relatifs, 20 résolus**. ⚠ **Les autres fichiers de `verification/` n'ont pas été repointés** : le relevé du 22 juillet 2026 y dénombre **18 renvois vers `../doc/`, répartis sur les huit fichiers suivants** — [`relecture-P3.md`](relecture-P3.md) (5), [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) (4), [`remontees-gouvernance.md`](remontees-gouvernance.md) (2), [`revalidation-2026-07-21.md`](revalidation-2026-07-21.md) (2), [`theses-P4-confrontation.md`](theses-P4-confrontation.md) (2), [`relecture-P1.md`](relecture-P1.md) (1), [L-03](lot-L-03-agent-card.md) (1), [L-08](lot-L-08-attaques.md) (1). **Le `CLAUDE.md` du volume désigne lui aussi `doc/` comme l'emplacement tranché.** Constat **entièrement hors lentille CA-12** : *on ne corrige pas au passage le renvoi d'un fichier dont on n'a pas la charge* (§8, remontée 6).

## 8. Remontées ouvertes — aucune n'est opérée par le relecteur ([PRDPlan](../prd/PRDPlan.md) §5.3)

1. **Statuer sur la forme d'annonce du régime R-12 dans les rapports de lot.** Les deux retraits du §3 laissent, dans L-09 et L-10, une annonce de méthode ; les onze autres rapports n'en portent aucune. Deux options se présentent, et le choix appartient au cadrage : imposer la forme d'annonce à tous les rapports, ou n'en imposer aucune. **La situation actuelle est la troisième, et c'est la moins tenable** — deux rapports annoncent, onze se taisent, et le lecteur ne peut pas savoir si le silence signifie l'absence de régime ou son évidence.
2. **Consigner la troncature de génération (§6) comme constat de socle.** Elle affecte douze rapports sur treize et ampute des reformulations de contrôle de bornage. Elle ne relève ni de CA-12 ni du relecteur ; elle relève du générateur de rapports et de la traçabilité que le PRD §7 attend d'un lot.
3. **Doter R-12 d'une règle de périmètre plutôt que d'un cardinal.** L'écart du §1 — douze annoncés, treize sur disque — vient de ce que le périmètre d'un contrôle a été énoncé en nombre de fichiers. Une règle de la forme *« toute pièce déposée sous `verification/` depuis la dernière passe CA-12 »* ne se périmerait pas. ⚠ La remontée n° 3 de [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §7 demandait déjà une **table d'assignation** nommant les pièces de surveillance de R-12 ; **la présente remontée est son pendant côté `verification/`**, et les deux se traitent ensemble ou pas du tout.
4. **Exécuter le contrôle de migration du §7, point 4.** Il est le seul qui puisse établir qu'un élément retiré d'un rapport n'a pas été recopié dans une pièce. ⚠ **Énoncé borné le 22 juillet 2026, phase P5 — la formulation antérieure était un absolu faux.** Elle écrivait « Aucune passe ne l'a conduit à ce jour », et le compte rendu que la présente passe cite elle-même comme amont la contredit : [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) **§4, entrée 6**, daté du 21 juillet 2026, porte « **Contrôle spécifique exécuté : le verbatim tronqué à la relecture P1.4 n'a pas migré vers les pièces** ». Constat pris en ouvrant les deux fichiers. **Formulation exacte** : *aucune passe n'a conduit le contrôle de migration à titre général ; le seul contrôle documenté est celui de [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) §4, entrée 6, borné au verbatim tronqué en P1.4 et au ch. 13 §13.1.* Le contrôle général demeure dû. *Un contrôle borné à un objet et à un siège reste un contrôle conduit et rendu ; l'écrire inexistant efface la seule couverture acquise.*
   ⚠ **Tension déclarée avec R-G-07 — « un rapport de lot ne se réécrit pas » —, et elle est écrite plutôt qu'ignorée.** Le présent fichier est un **compte rendu de relecture**, non un rapport de lot : la règle ne le vise pas à sa lettre. Mais **elle n'est pas stabilisée pour cette classe de document**, et la même passe qui l'invoque a déjà réécrit deux rapports de lot (§3, retraits L-09 et L-10, ouverts sous **R-G-49**). *Le régime de réécriture des documents de `verification/` est une question de cadrage ; la présente correction est opérée au titre d'un énoncé faux — catégorie « exécution » de [PRDPlan](../prd/PRDPlan.md) §5.3 — et non au titre d'un arbitrage sur ce régime, qui demeure ouvert.*
5. **Reprendre la passe en P5.1.** Le présent compte rendu se périme avec les rapports qu'il a lus, et **il n'atteste la conformité d'aucun d'eux** : il consigne un contrôle, à une date, sous une lentille unique.
6. **Arbitrer le déplacement `doc/` → `prd/` (§7, point 8), et repointer d'un seul geste.** Le volume a déjà payé ce déplacement une fois : le `CLAUDE.md` consigne, pour le passage à `doc/` du 18 juillet 2026, deux renvois cassés dont l'un vivait dans le **gabarit** que les 34 pièces recopient, et rappelle que le Vol. II porte **48 renvois cassés** pour avoir déplacé après vingt-neuf pièces rédigées. **Le déplacement vers `prd/` a eu lieu après trente-quatre pièces déposées sous `monographie/` et vingt-deux fichiers sous `verification/`** — le vingt-troisième étant le présent compte rendu. ⚠ **Le décompte du §7, point 8 ne porte que sur `verification/`** : ni `monographie/`, ni le `CLAUDE.md`, ni les `README.md` n'ont été balayés par la présente passe, et le gisement réel est nécessairement plus large. *La leçon consignée au `CLAUDE.md` — le chemin relatif se vérifie à la création de chaque pièce, en l'ouvrant — vaut d'abord pour celui qui déplace le répertoire.*
