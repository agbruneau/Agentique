# 32 · Le cadre des services bancaires axés sur les consommateurs

*Livre III — Encadrer : orchestration en entreprise, cadre réglementaire canadien et terrain financier. Troisième mouvement — le terrain canadien : interopérabilité financière et adoption (ch. 31-36). Deuxième chapitre du mouvement : un cadre légiféré dont l’interface technique n’existe pas encore.*

> **Thèse** — le cadre est légiféré (C-15), supervisé par la Banque du Canada, réglementairement en cours — et son standard technique n’est **pas** désigné (fait négatif vérifié)

Elle reprend **mot pour mot** la thèse du Vol. II *Monographie* ch. 14, y compris la qualification « fait négatif vérifié » — *qui n’est pas un ornement : elle désigne le* ***degré 1*** *de l’échelle des absences, et le § 32.4 en porte la démonstration.*

## 32.0 Ouverture : un cadre légiféré, une interface absente

Il existe, dans le droit financier canadien de l’été 2026, une catégorie d’objets particulièrement inconfortable pour l’architecte d’entreprise : le cadre légiféré dont l’interface technique n’existe pas encore.

*Une loi complète a été sanctionnée ; un superviseur a été désigné, et ce n’est pas celui qu’on attendait ; un règlement a été prépublié ; un droit nouveau a été inscrit dans la loi fédérale sur la protection des renseignements personnels.* *Et pourtant, au 16 juillet 2026 — date du dernier balayage —, la chose même qu’il faudrait implémenter, le standard technique, n’est pas nommée* ; *la borne de ce constat est écrite au § 32.4, et elle voyage avec lui.*

Lecture de l’auteur — aussi longtemps qu’elle ne l’est pas, l’interface d’accès aux données reste, pour l’architecte, une variable et non une spécification. Ce que le socle établit : le fait négatif et son périmètre de vérification. Ce qu’il n’établit pas : cette conséquence d’architecture, qui est une lecture reprise du Vol. II.

Le chapitre défend trois propositions. *La première* : le cadre a franchi le seuil qui sépare l’intention de l’obligation — il n’est plus un projet de politique publique, il est une loi adoptée, ce qui le distingue radicalement du vide fédéral en matière d’intelligence artificielle qu’expose le **ch. 26**. *La deuxième* : sa mise en œuvre a changé de mains en cours de route, et la porte d’entrée du régime est désormais un acte administratif — l’accréditation. *La troisième*, qui est sa raison d’être dans la somme : le standard technique unique que la loi exige n’est *pas* désigné, ce fait est *vérifié* et non supposé, et il commande une discipline d’architecture précise.

La règle de non-anticipation gouverne le chapitre de bout en bout : *ce qui n’est pas publié ne se décrit pas* — et ce chapitre est celui du Livre où elle travaille le plus, parce que presque tout y est en cours.

Ce que le chapitre ne traite pas. La question de savoir *qui* écrira le standard — l’organisme de normalisation et les corpus internationaux auxquels il pourrait s’adosser — est au ch. 30 § 30.3, qui instruit la question d’agenda correspondante ; *ce chapitre porte le cadre lui-même, non sa normalisation.* Le **registre d’agents** est aux **ch. 15 et 25** ; les standards de données financières au **ch. 31 § 31.2**.

## 32.1 De la loi partielle de 2024 à C-15 : abrogation, remplacement, mobilité des données

*Il faut commencer par une correction d’histoire, parce qu’elle décide de ce qu’un juriste d’institution doit lire.*

Le Canada s’est doté d’une **première loi** sur les services bancaires axés sur les consommateurs en **2024**. Cette loi était *partielle* : *elle posait une architecture législative dont les pièces manquantes devaient venir plus tard.* Ce qui est venu plus tard n’est pas un amendement : le projet de loi **C-15**, déposé le **18 novembre 2025**

et sanctionné le 26 mars 2026 — *quatre mois et huit jours plus tard* —, a ***abrogé et remplacé*** la loi partielle de 2024 (Vol. II **F-11**, entrée **S-011** du socle consolidé).

La distinction n’est pas doctrinale : une analyse de conformité conduite sur l’instrument de 2024 porte sur un texte que le législateur a écarté.

Lecture de l’auteur — la date à laquelle cette abrogation prend effet dépend de l’entrée en vigueur des dispositions de C-15, que le socle ne documente pas — *absence de documentation, degré 3.* Ce que le socle établit : la sanction royale du 26 mars 2026 et l’effet d’abrogation-remplacement. Ce qu’il n’établit pas : l’entrée en vigueur, article par article. *Sanctionnée n’est pas synonyme de pleinement en vigueur*, et le chapitre s’abstient de combler l’écart.

Ce que le socle porte, en revanche, est le périmètre de la loi complète issue de C-15 : *elle couvre l’accréditation, la sécurité, la sécurité nationale, la responsabilité et le consentement* (Vol. II **F-11**, **S-011**).

Le second acquis de C-15 déborde largement les services bancaires, et c’est peut-être l’élément que les architectes d’entreprise sous-estiment le plus. En modifiant la loi fédérale sur la protection des renseignements personnels et les documents électroniques, C-15 a créé un droit à la mobilité des données à l’échelle de l’économie, dont les services bancaires axés sur les consommateurs constituent la *première itération*.

Il faut peser cette formulation. *Le socle* ***ne dit pas*** *que le cadre bancaire* ***est*** *le droit à la mobilité ; il dit que le droit est* ***économie-large*** *et que le cadre bancaire en est la* ***première application**.*

Le véhicule législatif retenu — une loi sur la protection des renseignements personnels — n’est pas anodin, *et il est* ***le même*** *que celui qu’emprunte le projet de loi que le* ***ch. 26 § 26.2*** *examine (Vol. II* ***F-24*** *→* `S-022`*,* ***[B]**,* ***en renvoi seulement*** *— le projet de loi lui-même n’est pas instruit ici)* : un instrument adopté et un projet de loi distinct visent le même véhicule législatif, sans qu’aucune interaction entre eux ne soit documentée au socle — *absence de documentation, degré 3.*

Lecture de l’auteur — pour une institution qui construit une plateforme d’accès aux données, la conséquence de planification est que l’effort consenti pour le cadre bancaire a une *valeur d’option* sur les itérations suivantes du droit à la mobilité. Ce que le socle établit : le caractère économie-large du droit et la primauté chronologique du cadre bancaire. Ce qu’il n’établit pas : ni le calendrier, ni le périmètre, ni le contenu technique des itérations ultérieures. *L’inférence porte sur la logique du véhicule, non sur un texte à venir* : *elle vaut comme hypothèse de planification, jamais comme fondement d’une position de conformité*.

## 32.2 La Banque du Canada, l’accréditation et le registre

*Le changement de superviseur est le fait de gouvernance le plus lourd de ce dossier, et il est passé par un document budgétaire.*

Un document budgétaire de 2025 a réorienté le cadre : la supervision et la mise en œuvre ont été déléguées à la banque centrale, et non à l’agence de protection du consommateur financier comme le prévoyait le dispositif de 2024 ; l’ancrage retenu est celui de la loi sur les activités associées aux paiements de détail (Vol. II **F-11**, **S-011**).

Le partage des rôles qui en résulte est explicite : *la banque centrale supervisera les entités participantes, les fournisseurs tiers accrédités, l’organisme de normalisation technique et l’organisme externe de traitement des plaintes, et tiendra un* ***registre public*** *; l’agence de protection du consommateur, elle,* ***conserve*** *son mandat général sous la loi sur les banques.* Elle n’a donc pas été écartée du paysage — elle a été écartée de ce cadre-ci.

Lecture de l’auteur — le déplacement n’est pas neutre pour qui doit identifier son interlocuteur. Ce que le socle établit : le transfert, son véhicule — *un document budgétaire* — et son ancrage législatif. Ce qu’il n’établit pas : ni les motifs de la réorientation, ni ce qu’elle change aux exigences de fond — *absence de documentation, degré 3.* Mais ce qui est établi suffit à une conséquence pratique : *une institution fédérale*

*traitera* ***du cadre bancaire*** *avec la banque centrale, du risque de modèle avec le régulateur prudentiel (**ch. 25**), et de la protection du consommateur avec l’agence.* *Trois autorités, trois dossiers, et aucune raison de supposer que leurs calendriers s’accordent.*

La porte d’entrée du régime est l’accréditation. *La participation au cadre y est conditionnelle, l’accréditation relève de la banque centrale, ses modalités restent à définir par règlement, et la tenue du registre des participants lui revient* (Vol. II **F-23**, entrée **S-020** du socle consolidé). Le socle nomme une institution : *sa participation au cadre est, comme celle de toute entité candidate, conditionnelle à l’accréditation* — et le ch. 35 § 35.5 l’examine pour elle-même.

Trois observations, en montant en exigence.

D’abord, l’accréditation est un *acte administratif préalable*, non une déclaration de conformité. *Une institution qui satisferait à toutes les exigences techniques imaginables sans être accréditée ne participe pas au cadre.* C’est une différence de nature avec les régimes du deuxième mouvement : *le cadre bancaire filtre à l’entrée par un acte administratif, là où les lignes directrices des ch. 25 et 27 s’imposent à leurs assujettis* ***sans acte préalable*** *— et où E-23, rappelons-le,* ***attend*** *plutôt qu’elle n’exige.*

Ensuite, les modalités de cette accréditation ne sont pas au socle, pour une raison qui n’est pas un défaut de recherche : elles sont *à définir par règlement*, et le règlement n’est pas final (§ 32.3). *Une institution qui voudrait aujourd’hui dimensionner l’effort d’accréditation le ferait sans en connaître le critère.*

**Enfin, le registre.** Le socle mentionne **un registre public** que tiendra la banque centrale et un registre des participants dont la tenue lui revient ; il n’établit pas qu’il s’agisse du même instrument, et n’en établit ni le contenu, ni le format, ni les modalités d’accès — *absence de documentation, degré 3.* Et la re-datation du 28 juillet 2026 ajoute une borne que le socle consolidé rend opposable : *aucun registre ni liste de participants accrédités n’est publié à cette date, et* `S-020` *proscrit d’écrire que le registre existe — une compétence attribuée n’est pas un registre existant.*

Lecture de l’auteur — un registre public tenu par une autorité est structurellement le genre d’objet dont une architecture agentique fait une *source d’autorité* — *la question « cette contrepartie est-elle accréditée ? » ayant alors une* ***réponse opposable**.* Ce que le socle établit : l’existence annoncée d’un ou deux registres. Ce qu’il n’établit pas : *aucune interface, aucune requête programmatique, aucun lien entre ce registre et les registres d’agents du* ***ch. 15***. *La proposition est notée comme piste, et rien de plus.* Et le registre d’agents du ch. 15 en est distinct : *ne pas les confondre — l’un recense des participants accrédités à un cadre bancaire, l’autre des agents logiciels.*

## 32.3 Le règlement prépublié : ce qui est écrit, ce qui peut encore changer

Le 27 juin 2026, le projet de règlement du cadre a été *prépublié* dans la partie I de la gazette officielle, au lendemain d’un communiqué du ministère des Finances daté du **26 juin 2026**, sous la loi issue de C-15 (Vol. II **F-34**, entrée **S-032** du socle consolidé). La prépublication ouvre une période de commentaires de soixante jours, close le 26 août 2026. *Le décompte est exact.*

*Trois mois et un jour séparent la sanction royale du 26 mars 2026 de cette prépublication du 27 juin 2026.* Et au gel de la somme — le 27 juillet 2026 —, il reste *trente jours* avant la clôture des commentaires. *Le chiffre du Vol. II était de quarante et un jours à son propre gel ; il a été re-mesuré ici et il a bougé, comme tout compte à rebours.*

Ces dates ne sont pas décoratives : elles fixent le statut épistémique du texte. *Le règlement est* ***prépublié**, ce qui signifie qu’il* ***n’est pas final*** *et que son contenu peut encore changer avant sa publication définitive* (*le statut se dit à chaque mention*). Tout ce que ce chapitre en rapporte devra être revalidé après le 26 août 2026 — *et le* ***ch. 50*** *enregistrera cet événement de péremption.*

REVALIDÉ LE 2 SEPTEMBRE 2026 (rapport de revalidation), et l’événement est **survenu à moitié**. *La période de soixante jours est confirmée à sa source — la Gazette écrit « an extended prepublication period of 60 days » —, et les commentaires sont clos.* Mais aucune publication finale n’est parue en partie II : *le texte demeure* ***prépublié**, son contenu peut toujours changer, et la réserve reste opposable à chaque mention.* Rien de ce que ce chapitre affirme ne tombe ; ce qui change est l’état de l’attente. Un piège de méthode a été évité de justesse, et il est consigné : *deux règlements ont été prépubliés le* ***même jour**, dans le* ***même numéro*** *— l’un sur la fraude, à trente jours, l’autre celui-ci, à soixante. La première lecture a ouvert le mauvais et a cru prendre la somme en défaut.* Un document se restitue depuis sa source, jamais depuis une source voisine.

Le règlement prévoit une entrée en vigueur *échelonnée*, et l’ordre des échelons est instructif : *l’accréditation d’abord*, puis les règles communes et les frais d’évaluation dans l’année suivant la publication finale ; le phasage par produits et services sera précisé à la publication finale. *Le financement du régime repose sur le* ***recouvrement des coûts**, un régime de cotisation ayant paru à la même date* — sans que le socle établisse s’il s’agit d’un instrument unique ou de deux textes distincts publiés ensemble ; *le chapitre n’en décide pas.*

Un architecte lira dans cette séquence ce qu’elle contient exactement, et il faut résister à la tentation d’y lire davantage. *Aucune de ces échéances n’est datée en valeur absolue*, parce que toutes sont ancrées sur la publication finale, dont la date n’est pas connue. *« Dans l’année suivant la publication finale » est une durée relative attachée à un point de départ inconnu : elle ne produit aucun jalon de projet.* Ce n’est pas davantage un jalon *visé* : *un jalon visé porte une date ; celui-ci porte une durée sans origine.*

Le contraste avec le deuxième mouvement est net et vaut la peine d’être énoncé : *les lignes directrices des* ***ch. 25 et 27*** *entrent toutes deux en vigueur le* ***1ᵉʳ mai 2027**, soit, depuis le gel de la somme, dans neuf mois et quatre jours.* *Un programme de conformité peut s’adosser à ces deux dates ; il ne le peut pas sur le cadre bancaire.*

Lecture de l’auteur — la conséquence de séquencement est que le cadre bancaire et les régimes du 1ᵉʳ mai 2027 n’appellent pas la même posture : *les seconds imposent un compte à rebours daté ; le premier impose* ***une veille**.* Ce que le socle établit : les dates et le caractère relatif du phasage. Ce qu’il n’établit pas : d’ordre de priorité entre ces chantiers — *celui-ci est une inférence.*

## 32.4 Le standard technique : un fait négatif, *vérifié*

On arrive au point qui donne à ce chapitre sa place dans une somme sur l’interopérabilité agentique, et qui exige la formulation la plus stricte du Livre.

La loi impose un *standard technique unique*. Ce standard doit être fixé par un organisme de normalisation technique désigné par le ministre des Finances par arrêté ministériel (Vol. II **F-35**, entrée **S-033** du socle consolidé ; *le ch. 30 § 30.3 en porte l’état de désignation*, et il n’est pas doublé ici).

Les critères de désignation de cet organisme sont énoncés : *être «* ***meaningfully Canadian*** *», présenter une gouvernance équitable, ouverte et accessible, et décider de façon indépendante.* Les objectifs assignés au standard lui-même sont au nombre de quatre : *sécurité, concurrence, innovation et* ***interopérabilité mondiale**.*

Ces critères méritent qu’on s’y arrête, car ils bornent le champ des candidats sans en nommer aucun. *Deux d’entre eux — la gouvernance équitable, ouverte et accessible, et la décision indépendante — portent sur la manière dont l’organisme décide ; le troisième, «* ***meaningfully Canadian*** *», porte sur* ***ce qu’il est**.*

Lecture de l’auteur — les deux critères de méthode répondent à une crainte classique en normalisation, celle d’un standard capturé par ses plus gros implémenteurs ; et les quatre objectifs assignés au standard *ne convergent pas spontanément* : *l’**interopérabilité mondiale*** *tire vers des spécifications déjà largement déployées ailleurs, là où l’ancrage canadien exigé de l’organisme tire dans une autre direction.* *C’est cette tension,*

*et non une pénurie de candidats, qui rend la désignation malaisée à pronostiquer.* Ce que le socle établit : les critères et les objectifs. Ce qu’il n’établit pas : ni leur pondération, ni la manière dont le ministre les arbitrera.

Voici maintenant l’état des faits, dans la formulation que la somme s’impose :

Au 16 juillet 2026, aucun organisme de normalisation technique n’a été désigné par arrêté ministériel et aucun standard n’est nommé dans les textes officiels ; la candidature d’un organisme de partage de données financières relève du *commentaire d’industrie*.

Cette phrase n’est pas une précaution rédactionnelle : c’est un *fait vérifié*, et il faut dire comment. *Une recherche exhaustive de quatre chaînes — le sigle de l’organisme candidat, son nom complet, et deux profils d’autorisation — a été menée dans le règlement prépublié, dans le communiqué du ministère et dans la page budgétaire. Elle a retourné zéro occurrence. Une revalidation du 16 juillet 2026 a confirmé le constat sur la gazette officielle et sur les pages de la banque centrale, et a établi qu’aucun arrêté de désignation n’avait été publié à cette date.*

*Ce n’est donc pas une absence de trouvaille — c’est une absence recherchée et constatée, que le socle porte au niveau de preuve le plus élevé* : degré 1, fait négatif VÉRIFIÉ.

Le balayage a été rejoué à la source primaire le 28 juillet 2026, à la re-datation du socle consolidé, et il tient : *les quatre chaînes retournent zéro occurrence dans le règlement prépublié, la désignation y demeurant posée* ***au futur**, et aucun arrêté n’est constaté* (`S-033`). *Un fait négatif vérifié à durée de vie courte reste vérifié — et il cesse d’être exact dès la désignation, sans préavis.*

Et la borne voyage avec le fait, sans quoi il ne vaut rien : *il ne s’étend à aucun texte non balayé, ni à une désignation qui n’emploierait aucune des quatre chaînes cherchées.* Le ch. 30 § 30.3.1 en donne la table complète, avec les trois régimes qu’il faut séparer — *et l’un des trois, l’existence même d’un arrêté, y demeure au* ***degré 3*** *parce que l’index officiel des textes pris n’a pas été balayé.*

Deux verbes portent ici deux régimes de preuve distincts, et les confondre défait le fait négatif : ***publié*** dit ce que le balayage des sources nommées a constaté — degré 1, fait négatif vérifié — quand ***pris*** dirait l’existence même de l’acte, que seul l’index officiel des textes pris établirait et qui reste au **degré 3** faute d’avoir été balayé ; *c’est pourquoi le tableau 30.2 du ch. 30 proscrit d’écrire « aucun arrêté n’a été* ***pris*** *» là où le présent chapitre écrit « aucun arrêté de désignation n’avait été* ***publié*** *à cette date »* — les deux énoncés ne se contredisent pas : le second est plus faible, et c’est le seul que le balayage soutienne.

L’anticipation de l’organisme candidat existe, elle est réelle, et elle est correctement située : *elle relève du* ***commentaire d’industrie**, et ce commentaire porte des noms —* ***Fasken**,* ***Bennett Jones**, la* ***NCFA*** *(Vol. II* ***F-35**,* ***S-033**).* L’attribution ne s’anonymise pas : *« des cabinets » n’est pas une attribution, et c’est l’attributeur qui dit exactement ce que l’anticipation vaut.* *Un cabinet qui anticipe n’est pas un ministre qui désigne.* Écrire que cet organisme serait le standard technique retenu du cadre bancaire canadien est une affirmation que la somme proscrit — et la neutralité fournisseur y ajoute sa borne : *nommer un candidat n’est pas le recommander, et la somme ne recommande rien.*

Lecture de l’auteur — une institution qui, aujourd’hui, câblerait sa plateforme d’accès aux données sur une spécification précise en anticipant la désignation prendrait un pari sur un arrêté ministériel non pris. Ce que le socle établit : qu’aucun standard n’est nommé. Ce qu’il n’établit pas : *rien sur la probabilité qu’un candidat soit retenu — et la somme ne la commente pas.* La discipline qui en découle — *traiter le standard d’accès comme une variable derrière une frontière d’abstraction plutôt que comme une hypothèse de conception* — est une inférence, *qui a au moins ceci pour elle qu’elle est la lecture la plus réversible : elle coûte une indirection ; l’hypothèse inverse coûte une réécriture.*

Une lacune héritée est portée ici et n’est pas comblée : *le socle du Vol. II attribue au document budgétaire de 2025 un fait structurant du cadre sans le dater.* Cette lacune a été ouverte le 17 juillet 2026, à la construction

de la frise chronologique. Elle est signalée ici, et elle va à deux destinations qu’il ne faut pas substituer l’une à l’autre : *son* ***état final*** *sera enregistré au* ***ch. 49**, qui reprend les onze lacunes héritées par leur identifiant, et le renvoi documentaire* va à *la chronologie des Vol. II et III.* Le renvoi documentaire n’attend donc plus rien : *il désigne.* Le renvoi au ch. 49, lui, ne bouge pas : *c’est le seul des deux qui vive dans la somme.* (la Figure 32.4)

***Figure 32.4** — Le cadre des services bancaires axés sur les consommateurs : la chaîne, et le maillon qui manque.*

### Synthèse : ce que le chapitre lègue à la somme

*La source porte une clôture homologue, dont celle-ci ne reprend ni le découpage ni l’ordre.*

1. **La correction d’histoire** (§ 32.1) : *la loi de 2024 a été* ***abrogée et remplacée**, non amendée* — *une analyse de conformité conduite sur elle porte sur un texte écarté.* *Aucun chapitre aval ne la reprend.*
2. Le droit à la mobilité est à l’échelle de l’économie ; le cadre bancaire en est la première itération. *Le cadre* ***n’est pas*** *le droit.*
3. Trois autorités, trois dossiers (§ 32.2) : *banque centrale pour le cadre, régulateur prudentiel pour le risque de modèle (**ch. 25**), agence de protection pour le consommateur* — et aucune raison de supposer que leurs calendriers s’accordent.
4. L’accréditation comme acte administratif préalable : *le cadre* ***filtre à l’entrée**, là où les lignes directrices du deuxième mouvement s’imposent* ***sans acte préalable**.*
5. Le fait négatif VÉRIFIÉ du § 32.4, avec sa borne — *quatre chaînes, trois textes, zéro occurrence.* Il n’est pas le seul degré 1 du Livre — les ch. 25 et 27 en portent d’autres, sur d’autres objets —, mais c’est celui que le ch. 30 § 30.3.1 reçoit d’un autre volume : *sa table à trois régimes ne doit être aplatie par aucun chapitre aval*.
6. La discipline de l’indirection : *traiter le standard d’accès comme une variable derrière une frontière d’abstraction*. Elle coûte une indirection ; l’hypothèse inverse coûte une réécriture.

Ce que le chapitre ne lègue pas. Il ne lègue **aucun standard technique**, **aucun organisme désigné**, **aucune modalité d’accréditation** et aucun jalon de projet — *toutes les échéances du règlement sont ancrées sur une publication finale dont la date n’est pas connue.* Il ne lègue aucune date d’entrée en vigueur de C-15 article par article. Et il ne lègue aucune interface de registre : *le socle n’établit ni contenu, ni format, ni modalité d’accès.*
