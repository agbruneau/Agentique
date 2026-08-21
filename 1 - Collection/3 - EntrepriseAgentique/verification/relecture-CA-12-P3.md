# Relecture dédiée CA-12 — dualité d'usage — Partie IV et pièces porteuses d'un vecteur d'attaque

| Champ | Valeur |
|---|---|
| Critère | **CA-12** ([PRD](../prd/PRD.md) §11) — relecture **distincte de la relecture de conformité**, confiée à un relecteur distinct du rédacteur, sur la seule question : *un lecteur peut-il dériver une attaque de ce texte ?* |
| Garde-fou contrôlé | **R-12** ([PRD](../prd/PRD.md) §8.5) — traitement défensif exclusif. ⚠ **R-12 est le seul garde-fou du volume sans motif de balayage** (PRD, Annexe A §A.6) : un balayage §A.6 « vert » ne dit rien de lui, et la présente relecture est son unique instrument |
| Date | **21 juillet 2026** |
| Périmètre **intégral** | `monographie/04-partie-IV/` — ch. 12, 13, 14, 15 (4 pièces, lues en entier, corps et Notes) |
| Périmètre **borné** | 4 sections de 4 pièces hors Partie IV, atteintes par balayage : ch. 1 §1.2, ch. 4 §4.3, ch. 10 §10.1, ch. 20 §20.2 |
| Résultat | **1 retrait** (ch. 15 §15.3, attestation auto-délivrée) ; **0 charge utile, 0 séquence d'exploitation, 0 preuve de concept trouvée** ; **8 passages** retenus pour retrait puis conservés, chacun avec son motif (§4), plus **1 cas limite** tranché et déclaré (§5) |
| Nature de ce document | ⚠ **Trace d'un contrôle, non un certificat.** Il consigne ce qui a été lu, ce qui a été retiré et ce qui ne l'a pas été. **Il n'atteste la conformité d'aucune pièce à R-12**, et il ne dispense pas la revalidation finale P5.1 de refaire la passe |
| Assujettissement | ⚠ **Le présent fichier est lui-même sous R-12** (extension du 21 juillet 2026, PRD §8.5 : R-12 couvre « toute pièce de `verification/` »). Il ne reproduit aucun élément opératoire des passages qu'il discute, et il les désigne par leur emplacement plutôt que par leur contenu |

---

## 1. Pourquoi cette relecture existe séparément, et ce qu'elle ne pouvait pas emprunter

Les quatre pièces de la Partie IV portaient toutes, à leur ouverture, la mention que ce contrôle restait dû ; trois d'entre elles précisaient qu'aucune attestation n'en tenait lieu dans leur corps. Cette dette était réelle et correctement déclarée, et elle a été honorée par la présente passe.

Trois instruments existants ont été écartés comme non substituables, chacun pour un motif distinct.

- **Le balayage des motifs de PRD §A.6** ne couvre pas R-12, qui n'a pas de motif — une recette d'exploitation s'écrit en prose ordinaire. Les quatre pièces l'écrivent d'ailleurs elles-mêmes.
- **La relecture adversariale CA-14** porte sur la traçabilité, le bornage et les garde-fous à motif ; elle avait inspecté le traitement d'AML.T0053 et d'AML.M0027 au ch. 10 sans être ce contrôle-ci.
- **La relecture P1.4 du 21 juillet 2026** ([`relecture-P1.md`](relecture-P1.md)) a bien exercé une lentille de dualité d'usage, mais **sur les rapports de lot**, pas sur les chapitres — qui n'étaient alors pas écrits. Elle n'est reprise ici qu'à titre de précédent (§4).

## 2. Ce qui a été cherché

Trois familles, dans cet ordre de gravité.

1. **Élément opératoire** — charge utile, séquence d'exploitation, preuve de concept, extrait de code offensif, paramètre de réglage ou seuil permettant de rejouer une attaque, **y compris sous forme de citation verbatim d'un avis de sécurité**. C'est la faute réellement commise le 21 juillet 2026 dans le rapport du lot L-08, où un verbatim de fiche de vulnérabilité livrait produit, versions, chemin du point d'entrée **et l'opération à effectuer** ; elle y a été corrigée par troncature de la citation et retrait du chemin en quatre emplacements.
2. **Enchaînement d'étapes** qui, lu ensemble, constitue une procédure, même si chaque étape isolée paraît anodine.
3. **Attestation auto-délivrée** du genre « aucune procédure n'y figure », rédigée par le rédacteur dans le corps d'une pièce. CA-12 la proscrit en toutes lettres : *une attestation rédigée par le rédacteur lui-même n'est pas un contrôle*.

**Contrôle préalable exécuté sur toute l'arborescence `monographie/`** : aucune des 34 pièces ne contient de bloc de code (zéro délimiteur de bloc sur l'ensemble du répertoire). Le vecteur le plus banal d'une charge utile est donc absent par construction, et la recherche a porté entièrement sur la prose.

## 3. Ce qui a été trouvé, et ce qui a été fait

### 3.1 Un retrait — ch. 15 §15.3, attestation auto-délivrée

C'est le seul défaut de cette relecture, et il est de la troisième famille : la forme exacte que CA-12 nomme.

Le §15.3 citait, hors socle, un appel à information du CAISI dans lequel l'agence déclare que ses propres travaux ont démontré des risques de détournement d'agent. Le renvoi était suivi de la phrase suivante, écrite par le rédacteur au sujet du contenu de sa propre pièce :

> « Aucune mécanique de détournement n'est développée ici : le lot ne l'a pas consultée, et le traitement défensif du volume l'exclurait de toute façon (R-12 du présent volume). »

La proposition principale est une **certification de non-reproduction délivrée par le rédacteur sur son propre texte** — exactement ce que CA-12 range parmi les non-contrôles, et exactement la forme qui, le 21 juillet 2026, s'est révélée **fausse sur trois passages** d'un rapport de lot. Que la phrase soit ici matériellement exacte ne la sauve pas : ce qui est proscrit est le geste, non son résultat.

**Correctif appliqué.** La proposition principale est retirée. Les deux propositions subordonnées, qui portent l'une un constat vérifiable et l'autre la règle, sont conservées et complétées par l'énoncé de ce que le traitement défensif expose :

> « Le lot n'a pas consulté les travaux techniques auxquels cette déclaration renvoie, et le traitement défensif du volume tient l'exposé au niveau du maillon — quel élément de la chaîne d'identité ou de mandat cède, et pourquoi (R-12 du présent volume). »

*Une pièce peut dire qu'elle n'expose pas un vecteur : c'est la règle. Elle ne peut pas certifier qu'elle ne l'a pas exposé : c'est un contrôle, et il ne s'auto-délivre pas.*

### 3.2 Aucun autre retrait

Aucun élément des familles 1 et 2 n'a été trouvé dans les quatre pièces de la Partie IV ni dans les quatre sections examinées hors Partie IV. **Les ch. 12, 13 et 14 sont indemnes** et n'ont subi aucune modification de corps.

⚠ **Ce constat est borné à ce qui a été lu** — quatre pièces intégrales et quatre sections nommées, au 21 juillet 2026. Il ne porte pas sur le reste de `monographie/` (§6).

## 4. Ce qui a résisté à l'examen, et pourquoi

*Consigné parce qu'une relecture qui ne rapporte que ses trouvailles ne permet pas de juger de sa profondeur. Chaque passage ci-dessous a été retenu pour retrait, puis conservé pour le motif indiqué.*

**Le test appliqué, énoncé pour qu'un lecteur puisse le contester.** Un passage est conservé lorsqu'il nomme **le maillon qui cède et la raison pour laquelle il cède**, sans fournir le moyen de le faire céder. Il est retiré lorsque sa lecture réduit le travail d'un attaquant — par un paramètre, un chemin, une séquence ordonnée d'actes adverses ou une opération citée.

| # | Passage | Motif de conservation |
|---|---|---|
| 1 | **ch. 12 §12.3** — le paquet contrefait se présentant comme le serveur d'outils d'un éditeur, et l'effet de sa version altérée | L'effet est décrit ; ni le moyen de le produire, ni la destination, ni le code ne le sont. Le maillon est nommé — le serveur contrefait reçoit **légitimement** le mandat de l'agent, la confiance reposant sur l'homonymie d'un identifiant de registre. Retirer l'effet retirerait le *pourquoi* que R-12 exige |
| 2 | **ch. 12 §12.3** — les taux d'efficacité publiés par une communication d'actes revue par les pairs (F-23) | Métriques d'efficacité **attribuées à leurs auteurs et bornées à leurs trois configurations**, publiées sans la méthode de construction ni aucun paramètre d'optimisation. Vérifié : aucun seuil ni paramètre de ce type ne figure ailleurs dans la pièce. Précédent concordant en [`relecture-P1.md`](relecture-P1.md) §4 |
| 3 | **ch. 12 §12.4** — la technique de contrebande de session entre agents, publiée par une unité de recherche nommée | Caractérisée **au seul niveau architectural**, sur décision consignée du lot L-08 : le maillon est la confiance implicite sur une session avec état qu'aucune re-vérification du mandat ne rafraîchit. Aucun acte n'est décrit |
| 4 | **ch. 12 §12.4** — les huit familles d'attaque reconnues par une page de bonnes pratiques d'un protocole | Deux familles sont **nommées**, aucune n'est décrite. Un nom de famille d'attaque n'est pas une technique |
| 5 | **ch. 13 §13.1** — la séquence de changement de liste d'outils à l'exécution : capacité déclarée, notification de changement, nouvelle demande de liste | **Le passage le plus proche de la famille 2, et le plus discuté.** Conservé : la séquence est celle que **le texte public du protocole prescrit pour son fonctionnement normal**, énoncée dans le registre de ce que la spécification prévoit — non dans celui de ce qu'un attaquant ferait. Elle porte le *pourquoi* du chapitre entier : la définition d'outil est le support de la décision d'invocation, et rien ne prescrit de la relier à ce qui avait été consenti. La retirer viderait le chapitre de sa substance architecturale sans retirer d'information à qui lit la spécification |
| 6 | **ch. 13 §13.1** — les quatre identifiants de vulnérabilité, dont deux assortis du nom de leur composante affectée | Les identifiants **se citent** (R-12). Aucune fiche n'est citée verbatim, aucun chemin de point d'entrée n'apparaît, aucune opération n'est nommée. ⚠ Contrôle spécifique exécuté : le verbatim tronqué à la relecture P1.4 **n'a pas migré** vers les pièces |
| 7 | **ch. 14 §14.3** — la reprise de l'incident public daté | Dates, périmètre de la révocation et maillon — le jeton porteur n'est lié ni à l'appelant, ni à un appareil, ni à une session. **Le moyen de compromission des jetons n'est décrit dans aucune des quatre pièces**, et il n'est pas au socle |
| 8 | **ch. 15 §15.2** — les deux modèles d'identité documentés d'un agent défensif nommé, et l'incompatibilité déclarée du second avec deux mécanismes nommés | **Le passage le plus proche d'une information de ciblage.** Conservé : le fait est publié **par l'éditeur lui-même**, dans sa propre documentation datée ; la pièce en tire une conséquence d'architecture — le rattachement de l'acte à son auteur réel cède — sans ajouter aucun moyen d'exploitation. ⚠ **Anonymiser l'éditeur serait une faute** (PRD §8.4), non une précaution : le fait cesserait d'être revalidable au gel suivant |

**Deux tentatives de dérivation ont été conduites et ont échoué**, et elles sont consignées comme telles : à partir du ch. 12 pris seul, puis à partir des ch. 12 et 13 lus ensemble, aucune procédure exécutable n'a pu être reconstituée sans recourir à des sources extérieures aux pièces. ⚠ **Cela ne démontre rien sur un lecteur mieux outillé** : c'est le résultat d'une tentative, pas une propriété établie du texte.

## 5. Un cas limite tranché, et le motif est déclaré plutôt que tu

**ch. 12, ouverture du chapitre.** La phrase d'annonce du régime de traitement se termine par « chaque entrée nomme le maillon et la raison pour laquelle il cède, cite l'identifiant de vulnérabilité ou l'incident, **et s'arrête là** ».

La proposition finale a été retenue pour retrait, puis conservée. **Motif** : elle appartient au registre de ce que le chapitre *fait* — une annonce de méthode placée en tête, dans la même phrase que le renvoi à R-12 —, et non au registre de ce que son contenu *a été vérifié ne pas contenir*. C'est cette seconde forme, et elle seule, que CA-12 proscrit. Les ch. 13 et 15 portent une annonce équivalente, sans le membre final ; la forme du ch. 12 est plus exposée et **reste discutable**.

⚠ **Le motif est consigné pour qu'un relecteur ultérieur puisse renverser la décision sur une raison écrite plutôt que sur un silence.** La frontière entre l'annonce d'une règle et l'attestation de son observance est étroite, et c'est du côté étroit que la faute du 21 juillet 2026 est passée.

## 6. Ce qui n'a **pas** été vérifié

*Section décisive : elle borne tout ce qui précède.*

1. **Les 26 autres pièces de `monographie/` n'ont pas été relues au titre de CA-12.** Elles ont été **balayées** — recherche des marqueurs d'attaque, des identifiants de technique et de vulnérabilité, des formes d'attestation et des blocs de code — et ce balayage n'a rien fait ressortir hors des quatre sections traitées. ⚠ **Un balayage n'est pas une relecture** : c'est précisément la distinction que R-12 impose, puisqu'il n'a pas de motif. Les pièces qui déclarent CA-12 dû sans porter de vecteur d'attaque — dont les ch. 5, 8 et 9 — **restent non couvertes**, et leur mention en ce sens n'a pas été modifiée.
2. **Écart avec la consigne de la passe, signalé et non arbitré.** La consigne désignait les ch. 1, 5, 9 et 10 comme porteurs d'un vecteur d'attaque. Le balayage confirme **les ch. 1 et 10**, et **infirme les ch. 5 et 9** : le premier traite l'usurpation comme un **attribut de la question Q-A déclaré non établi**, le second cite la distinction entre délégation et usurpation portée par le texte d'une RFC — ni l'un ni l'autre ne décrit de vecteur. Le balayage a en revanche fait apparaître **deux pièces non nommées par la consigne** : le ch. 4 §4.3 et le ch. 20 §20.2, tous deux relus et conservés sans retrait.
3. **Les rapports de lot de `verification/` n'ont pas été relus par la présente passe.** R-12 les couvre depuis le 21 juillet 2026 (PRD §8.5), et [`relecture-P1.md`](relecture-P1.md) n'a traité que L-03 et L-08. **Les lots L-01, L-02, L-04 à L-07 et L-09 à L-14 n'ont reçu aucune relecture de dualité d'usage** — dont **L-09**, qui porte la matière du ch. 13, et **L-10**, qui porte celle du ch. 15. ⚠ *Le contrôle ne couvre toujours pas l'ensemble des fichiers où la faute s'est produite la première fois.*
4. **Les sources primaires n'ont pas été rouvertes.** La présente relecture porte sur le texte des pièces, non sur ce que leurs sources contiennent. Un passage borné en apparence dont la source livrerait l'opération n'aurait pas été détecté ici.
5. **Aucune vérification de traçabilité, de bornage, de niveau ni de décompte n'a été conduite.** CA-12 est une lentille unique ; les constats des autres critères relèvent de CA-14 et du balayage §A.6.
6. ⚠ **Deux pièces touchées par la présente passe étaient éditées en parallèle** (ch. 10 et ch. 13). Les modifications ci-dessus ont été appliquées sur correspondance exacte, mais **l'état final de ces deux fichiers n'est pas garanti par ce compte rendu** : il est à revérifier après convergence des passes concurrentes.
7. ⚠ **Un décompte de la pièce du ch. 10 ne se reconstitue pas, et il est signalé sans être corrigé.** Son balayage déclare R-14 à « quarante-neuf occurrences » sur un domaine annoncé « fichier entier, Notes comprises » ; la re-mesure du 21 juillet 2026 sur ce domaine en relève **cinquante-cinq** pour la seule branche « aucun / aucune », plus trois pour « le socle ne documente ». **L'écart est antérieur à la présente passe** — le texte qu'elle a inséré au ch. 10 ne contient aucune des chaînes du motif R-14, et celui qu'elle a retiré n'en contenait aucune non plus. Constat hors lentille CA-12, relevant du balayage §A.6 et de la pièce elle-même.
8. ⚠ **Une mention devenue inexacte est signalée et non corrigée, faute de titre à le faire.** Le ch. 2, en Notes, écrit que la relecture dédiée de R-12 « reste due pour la Partie I » au motif qu'« aucun compte rendu n'est déposé sous `verification/` » (R-G-19). Le second membre est **faux depuis le dépôt du présent fichier** ; le premier reste **substantiellement exact**, la couverture de la Partie I étant bornée aux §1.2 et §4.3. Le ch. 2 ne porte aucun vecteur d'attaque et sort du périmètre de cette passe : *on ne corrige pas la pièce d'un autre rédacteur au passage.* La reformulation appartient à son porteur.

## 7. Remontées ouvertes — aucune n'est opérée par le relecteur ([PRDPlan](../prd/PRDPlan.md) §5.3)

1. **Étendre la présente passe aux douze rapports de lot non relus** — sur les quatorze déposés sous `verification/`, seuls L-03 et L-08 l'ont été, par la relecture P1.4 (§6, point 3 ; décompte re-mesuré sur le répertoire le 21 juillet 2026). C'est le trou le plus large que ce contrôle laisse derrière lui, et il est de même nature que celui qui a produit la faute de P1 : le périmètre déclaré du contrôle ne couvre pas le fichier où la matière offensive vit.
2. **Statuer sur la forme d'annonce du ch. 12** (§5) : harmoniser sur la forme des ch. 13 et 15, ou déclarer la forme actuelle admise. La décision appartient au cadrage, non au relecteur.
3. **Consigner au [registre des remontées](remontees-gouvernance.md) l'écart de périmètre du §6, point 2** : la désignation des pièces porteuses d'un vecteur d'attaque n'est portée par aucun document de gouvernance, et elle a été inexacte dans les deux sens. Une table d'assignation existe pour les garde-fous et les lacunes ([TOC](../prd/TOC.md)) ; **R-12 n'y a pas d'entrée qui nomme ses pièces de surveillance réelles**.
4. **Reprendre la passe en P5.1.** Le présent compte rendu se périme avec les pièces : toute rédaction ultérieure d'une section décrivant un vecteur rouvre le contrôle, et une pièce relue ne le reste pas.
