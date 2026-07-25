# Chapitre 14 — Le cadre des services bancaires axés sur le consommateur

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | **F-11**, **F-23**, **F-34**, **F-35** ; F-09, F-24, F-25, F-28, F-29 en renvoi (ch. 9, 10, 11, 15) ; F-23b en renvoi (Desjardins, ch. 17) |
| Garde-fous à surveiller (PRD §8) | **R-5** (chapitre porteur principal — aucun standard technique désigné, FDX = anticipation d'industrie) ; §8.3 (sensibilité temporelle : texte réglementaire **prépublié**, susceptible de changer ; arrêté de désignation à venir) ; lacune **§10.1** (encadré, §14.4) |
| Volumétrie cible | ~3000 mots |

> **Thèse ([TOC.md](../../TOC.md))** : Le cadre est légiféré (C-15), supervisé par la Banque du Canada, réglementairement en cours — et son standard technique n'est **pas** désigné (fait négatif vérifié).

---

Il existe, dans le droit financier canadien de l'été 2026, une catégorie d'objets particulièrement inconfortable pour l'architecte d'entreprise : le cadre légiféré dont l'interface technique n'existe pas encore. Le cadre des services bancaires axés sur le consommateur en est le spécimen le plus abouti. Une loi complète a été sanctionnée ; un superviseur a été désigné et ce n'est pas celui qu'on attendait ; un règlement a été prépublié ; un droit nouveau a été inscrit dans la loi fédérale sur la protection des renseignements personnels. Et pourtant, à la date de gel du présent chapitre, la chose même qu'il faudrait implémenter — le standard technique — n'est pas nommée. **Lecture de l'auteur** : aussi longtemps qu'elle ne l'est pas, l'interface d'accès aux données reste, pour l'architecte, une variable et non une spécification.

Ce chapitre établit ces deux faits ensemble, et soutient qu'ils ne se contredisent pas. Il défend trois propositions. La première est que le cadre a franchi le seuil qui sépare l'intention de l'obligation : il n'est plus un projet de politique publique, il est une loi adoptée, ce qui le distingue radicalement du vide fédéral en matière d'intelligence artificielle qu'expose le chapitre 10. La deuxième est que sa mise en œuvre a changé de mains en cours de route — la supervision, prévue en 2024 pour l'Agence de la consommation en matière financière du Canada (ACFC), a été confiée à la Banque du Canada — et que la porte d'entrée du régime est désormais un acte administratif : l'accréditation. La troisième, qui est la raison d'être de ce chapitre dans une monographie sur l'agentique, est que le standard technique unique (*single technical standard*) que la loi exige n'est **pas** désigné, que ce fait est vérifié et non supposé, et qu'il commande une discipline d'architecture précise.

## 14.1 De la loi partielle de 2024 à C-15 : abrogation, remplacement, mobilité des données

Il faut commencer par une correction d'histoire, parce qu'elle décide de ce qu'un juriste d'institution doit lire.

Le Canada s'est doté d'une première loi sur les services bancaires axés sur les consommateurs en **2024**. Cette loi était **partielle** : elle posait une architecture législative dont les pièces manquantes devaient venir plus tard. Ce qui est venu plus tard n'est pas un amendement. Le projet de loi **C-15**, déposé le **18 novembre 2025** et sanctionné le **26 mars 2026** — quatre mois et huit jours plus tard —, a **abrogé et remplacé** la loi partielle de 2024[^1]. La distinction n'est pas doctrinale : une analyse de conformité conduite sur l'instrument de 2024 porte sur un texte que le législateur a écarté. **Lecture de l'auteur** : la date à laquelle cette abrogation prend effet dépend de l'entrée en vigueur des dispositions de C-15, que le socle ne documente pas (voir infra) ; le chapitre ne se prononce pas sur l'état du droit applicable au 16 juillet 2026. La loi complète issue de C-15 couvre l'accréditation, la sécurité, la sécurité nationale, la responsabilité et le consentement[^1].

Une précision de statut s'impose ici, et elle est de celles qu'un chapitre daté doit énoncer plutôt que laisser deviner. Le socle documente la **sanction royale** du 26 mars 2026 ; il ne documente pas l'entrée en vigueur, article par article, des dispositions de la loi. Ce qu'il documente en matière de calendrier porte sur le **règlement**, dont §14.3 traite. Sanctionnée n'est pas synonyme de pleinement en vigueur, et le présent chapitre s'abstient de combler l'écart.

Le second acquis de C-15 déborde largement les services bancaires, et c'est peut-être l'élément que les architectes d'entreprise sous-estiment le plus. En modifiant la Loi sur la protection des renseignements personnels et les documents électroniques (LPRPDE), C-15 a créé un **droit à la mobilité des données (*data portability*) à l'échelle de l'économie**, dont les services bancaires axés sur le consommateur constituent la **première itération**[^1].

Il faut peser cette formulation. Le socle ne dit pas que le cadre bancaire *est* le droit à la mobilité ; il dit que le droit est économie-large et que le cadre bancaire en est la première application. Le véhicule législatif retenu — une loi sur la protection des renseignements personnels — n'est pas anodin, et il est le même que celui qu'emprunte le projet de loi C-36 (*Protecting Privacy and Consumer Data Act*), en deuxième lecture au 16 juillet 2026, que le chapitre 10 examine : un instrument adopté et un projet de loi distinct visent le même véhicule législatif, sans qu'aucune interaction entre eux ne soit documentée au socle[^2].

**Lecture de l'auteur** : pour une institution qui construit une plateforme d'accès aux données, la conséquence de planification est que l'effort consenti pour le cadre bancaire a une valeur d'option sur les itérations suivantes du droit à la mobilité. Le socle établit le caractère économie-large du droit et la primauté chronologique du cadre bancaire ; il n'établit ni le calendrier, ni le périmètre, ni le contenu technique des itérations ultérieures — et cet ouvrage ne les invente pas. L'inférence porte sur la logique du véhicule, non sur un texte à venir : elle vaut comme hypothèse de planification, jamais comme fondement d'une position de conformité.

## 14.2 La Banque du Canada, l'accréditation et le registre

Le changement de superviseur est le fait de gouvernance le plus lourd de ce dossier, et il est passé par un document budgétaire.

Le **Budget 2025** a réorienté le cadre : la supervision et la mise en œuvre ont été **déléguées à la Banque du Canada**, et non à l'ACFC comme le prévoyait le dispositif de 2024 ; l'ancrage retenu est celui de la Loi sur les activités associées aux paiements de détail[^1]. Le partage des rôles qui en résulte est explicite : la Banque du Canada supervisera les entités participantes, les fournisseurs tiers accrédités, l'organisme de normalisation technique et l'organisme externe de traitement des plaintes, et tiendra un **registre public** ; l'ACFC, elle, **conserve** son mandat général de protection des consommateurs sous la Loi sur les banques[^3]. L'ACFC n'a donc pas été écartée du paysage — elle a été écartée de ce cadre-ci.

**Lecture de l'auteur** : le déplacement n'est pas neutre pour qui doit identifier son interlocuteur. Le socle documente le transfert, son véhicule — un document budgétaire — et son ancrage dans la Loi sur les activités associées aux paiements de détail ; il ne documente ni les motifs de la réorientation, ni ce qu'elle change aux exigences de fond, et ce chapitre ne comble ni l'un ni l'autre. Ce qui est établi suffit néanmoins à une conséquence pratique : une institution fédérale traitera du cadre bancaire avec la Banque du Canada, du risque de modèle (*model risk*) avec le BSIF (voir ch. 9), et de la protection du consommateur sous la Loi sur les banques avec l'ACFC. Trois autorités, trois dossiers, et aucune raison de supposer que leurs calendriers s'accordent.

La porte d'entrée du régime est l'**accréditation**. La participation au cadre y est conditionnelle, et l'accréditation relève de la Banque du Canada ; ses modalités restent **à définir par règlement**, et la Banque du Canada tient le registre des participants[^4]. Le socle nomme une institution : la participation de Desjardins au cadre est, comme celle de toute entité candidate, conditionnelle à l'accréditation par la Banque du Canada — le rapport annuel 2025 (rapport de gestion, 24 février 2026) est la source primaire de ce constat, corroborée par Finances Canada et par les analyses Fasken, DLA Piper, McCarthy Tétrault et Baker McKenzie ; le chapitre 17 examine cette institution pour elle-même[^4].

Trois observations, en montant en exigence.

D'abord, l'accréditation est un **acte administratif préalable**, non une déclaration de conformité. Une institution qui satisferait à toutes les exigences techniques imaginables sans être accréditée ne participe pas au cadre. C'est une différence de nature avec les régimes examinés en Partie III — **Lecture de l'auteur** : le cadre bancaire filtre à l'entrée par un acte administratif, là où les lignes directrices de la Partie III s'imposent à leurs assujettis sans acte préalable (voir ch. 9 et ch. 11).

Ensuite, les modalités de cette accréditation ne sont pas au socle, pour une raison qui n'est pas un défaut de recherche : elles sont **à définir par règlement**[^4], et le règlement n'est pas final (§14.3). Une institution qui voudrait aujourd'hui dimensionner l'effort d'accréditation le ferait sans en connaître le critère.

Enfin, le registre. Le socle mentionne un **registre public** que tiendra la Banque du Canada[^3] et un **registre des participants** tenu par la Banque du Canada[^4] ; il n'établit pas qu'il s'agit du même instrument, et n'en établit ni le contenu, ni le format, ni les modalités d'accès. **Lecture de l'auteur** : un registre public tenu par une autorité est structurellement le genre d'objet dont une architecture agentique fait une source d'autorité — la question « cette contrepartie est-elle accréditée ? » ayant une réponse opposable. Le socle ne porte pas cette lecture : il ne documente aucune interface, aucune requête programmatique, aucun lien entre ce registre et les registres d'agents examinés au chapitre 8. La proposition est notée ici comme piste, et rien de plus.

## 14.3 Le règlement prépublié : ce qui est écrit, ce qui peut encore changer

Le 27 juin 2026, le projet de règlement du cadre a été **prépublié dans la Gazette du Canada, partie I** (vol. 160, no 26), au lendemain d'un communiqué de Finances Canada daté du 26 juin 2026, sous la Loi sur les services bancaires axés sur les consommateurs issue de C-15[^5]. La prépublication ouvre une période de commentaires de **soixante jours**, close le **26 août 2026**[^5]. Le décompte est exact : du 27 juin au 26 août 2026, il s'écoule bien soixante jours.

Trois mois et un jour séparent la sanction royale du 26 mars 2026 de cette prépublication du 27 juin 2026. À la date de gel du présent chapitre, le 16 juillet 2026, il reste **quarante et un jours** avant la clôture des commentaires.

Ces dates ne sont pas décoratives : elles fixent le statut épistémique du texte. Le règlement est **prépublié**, ce qui signifie qu'il n'est pas final et que **son contenu peut encore changer** avant sa publication définitive[^6]. Tout ce que le présent chapitre en rapporte est daté du 16 juillet 2026 et devra être revalidé après le 26 août 2026 — le chapitre 21 §21.3 traite des conditions de péremption de l'ouvrage, et le chapitre 24 §24.2 des événements qui périment le blueprint.

Le règlement prévoit une **entrée en vigueur échelonnée**, et l'ordre des échelons est instructif : l'**accréditation d'abord**, puis les **règles communes et les frais d'évaluation dans l'année suivant la publication finale** ; le **phasage par produits et services** sera précisé à la publication finale[^5]. Le financement du régime repose sur le **recouvrement des coûts**, un régime de cotisation ayant lui aussi paru à la Gazette du Canada, partie I, le 27 juin 2026[^1] — même date de Gazette que le règlement du cadre, sans que le socle établisse s'il s'agit d'un instrument unique ou de deux textes distincts publiés ensemble ; le présent chapitre n'en décide pas.

Un architecte lira dans cette séquence ce qu'elle contient exactement, et il faut résister à la tentation d'y lire davantage. Aucune de ces échéances n'est datée en valeur absolue, parce que toutes sont ancrées sur la **publication finale**, dont la date n'est pas connue au 16 juillet 2026. « Dans l'année suivant la publication finale » est une durée relative attachée à un point de départ inconnu : elle ne produit aucun jalon de projet. Le contraste avec les régimes de la Partie III est net et vaut la peine d'être énoncé : la ligne directrice E-23 du BSIF et la ligne directrice sur l'intelligence artificielle de l'AMF entrent toutes deux en vigueur le **1er mai 2027**, soit, depuis la date de gel du présent chapitre, dans neuf mois et quinze jours (voir ch. 9 et ch. 11)[^7]. Un programme de conformité peut s'adosser à ces deux dates ; il ne le peut pas sur le cadre bancaire.

**Lecture de l'auteur** : la conséquence de séquencement est que le cadre bancaire et les régimes du 1er mai 2027 n'appellent pas la même posture. Les seconds imposent un compte à rebours daté ; le premier impose une veille. Le socle établit les dates et le caractère relatif du phasage ; il n'établit aucun ordre de priorité entre ces chantiers, et celui-ci est une inférence de l'auteur.

## 14.4 Le standard technique : un fait négatif, vérifié

On arrive au point qui donne à ce chapitre sa place dans une monographie sur l'interopérabilité agentique, et qui exige la formulation la plus stricte de tout l'ouvrage.

La loi impose un **standard technique unique** (*single technical standard*). Ce standard doit être fixé par un **organisme de normalisation technique désigné par le ministre des Finances par arrêté ministériel**. Les critères de désignation de cet organisme sont énoncés : être « *meaningfully Canadian* », présenter une gouvernance équitable, ouverte et accessible, et décider de façon indépendante. Les objectifs assignés au standard lui-même sont au nombre de quatre : sécurité, concurrence, innovation et interopérabilité mondiale[^3].

Ces critères méritent qu'on s'y arrête, car ils bornent le champ des candidats sans en nommer aucun. Deux d'entre eux — la gouvernance équitable, ouverte et accessible, et la décision indépendante — portent sur la **manière dont l'organisme décide** ; le troisième, « *meaningfully Canadian* », porte sur **ce qu'il est**. **Lecture de l'auteur** : les deux premiers répondent à une crainte classique en normalisation, celle d'un standard capturé par ses plus gros implémenteurs ; et les quatre objectifs assignés au standard ne convergent pas spontanément — l'interopérabilité mondiale tire vers des spécifications déjà largement déployées ailleurs, là où l'ancrage canadien exigé de l'organisme tire dans une autre direction. C'est cette tension, et non une pénurie de candidats, qui rend la désignation malaisée à pronostiquer. Le socle établit les critères et les objectifs ; il n'établit ni leur pondération, ni la manière dont le ministre des Finances les arbitrera, et ce chapitre ne le devine pas.

Voici maintenant l'état des faits, dans la formulation que le présent ouvrage s'impose. **Au 16 juillet 2026, aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans les textes officiels ; la candidature de FDX relève du commentaire d'industrie**[^8].

Cette phrase n'est pas une précaution rédactionnelle : c'est un fait vérifié, et il faut dire comment. Une recherche exhaustive des chaînes « FDX », « Financial Data Exchange », « FAPI » et « OAuth » a été menée dans le règlement prépublié, dans le communiqué de Finances Canada et dans la page du Budget 2025. Elle a retourné **zéro occurrence**[^3]. La revalidation du 16 juillet 2026 a confirmé le constat sur la Gazette du Canada et sur les pages de la Banque du Canada, et a établi qu'aucun arrêté de désignation n'avait été publié à cette date[^6]. Ce n'est donc pas une absence de trouvaille — c'est une absence recherchée et constatée, que le socle porte au niveau de preuve le plus élevé.

L'anticipation de FDX comme candidat probable existe, elle est réelle, et elle est correctement située : elle relève du **commentaire d'industrie** — Fasken, Bennett Jones, la NCFA[^3]. Un cabinet qui anticipe n'est pas un ministre qui désigne. Écrire que FDX serait le standard technique retenu du cadre bancaire canadien est une affirmation que cet ouvrage proscrit[^8].

> **État de la connaissance vérifiable — quel organisme de normalisation technique sera désigné, et quel standard fixera-t-il ?**
>
> Recherche : la constitution du socle (F-35) a mené une recherche exhaustive des chaînes « FDX », « Financial Data Exchange », « FAPI » et « OAuth » dans le règlement prépublié, le communiqué de Finances Canada et la page du Budget 2025 — zéro occurrence. La passe de revalidation P0.1 du 16 juillet 2026 a reconduit le constat sur la Gazette du Canada, partie I, et sur les pages de la Banque du Canada, et établi qu'aucun arrêté de désignation n'avait été publié à cette date. Ces sources établissent l'**exigence** d'un standard technique unique, les **critères** de désignation de l'organisme et le **mécanisme** de la désignation par arrêté ministériel ; elles n'établissent ni le nom de l'organisme, ni le contenu du standard. La désignation est le fait qui déterminera quel standard s'imposera ; FDX — et, par extension, FAPI et OAuth — n'est à ce jour qu'une anticipation du commentaire d'industrie (Fasken, Bennett Jones, NCFA), sans reprise officielle. En l'absence de source primaire, la question reste ouverte ; aucune inférence n'est proposée ici[^9].

**Lecture de l'auteur** — et la marque s'impose, car le socle porte un fait négatif, non une doctrine d'architecture. Une institution qui, aujourd'hui, câblerait sa plateforme d'accès aux données sur une spécification précise en anticipant la désignation prendrait un pari sur un arrêté ministériel non pris. Le socle établit qu'aucun standard n'est nommé ; il n'établit rien sur la probabilité que FDX soit retenu, et cet ouvrage ne la commente pas. La discipline qui en découle — traiter le standard d'accès comme une variable derrière une frontière d'abstraction plutôt que comme une hypothèse de conception — est une inférence de l'auteur, que le chapitre 23 instancie sur son troisième flux illustratif. Elle a au moins ceci pour elle qu'elle est la lecture la plus réversible : elle coûte une indirection ; l'hypothèse inverse coûte une réécriture.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis, pour la suite de l'ouvrage. **Premièrement**, le cadre des services bancaires axés sur le consommateur est **légiféré** : C-15, déposé le 18 novembre 2025 et sanctionné le 26 mars 2026, a abrogé et remplacé la loi partielle de 2024, et a créé au passage, en modifiant la LPRPDE, un droit à la mobilité des données à l'échelle de l'économie dont ce cadre est la première itération. **Deuxièmement**, sa mise en œuvre relève de la **Banque du Canada** depuis le Budget 2025 — et non de l'ACFC comme prévu en 2024 —, la participation y est conditionnelle à une **accréditation** dont les modalités restent à définir par règlement, et un registre public est prévu, tenu par la Banque du Canada. **Troisièmement**, le règlement est **prépublié** depuis le 27 juin 2026, ses commentaires closent le 26 août 2026, son entrée en vigueur est échelonnée et ancrée sur une publication finale non datée — et **aucun organisme de normalisation technique n'a été désigné par arrêté ministériel au 16 juillet 2026, aucun standard n'étant nommé dans les textes officiels ; la candidature de FDX relève du commentaire d'industrie**.

Ce que ce chapitre ne dit pas mérite la même netteté. Il ne dit pas que FDX sera, ou ne sera pas, le standard technique du cadre : le socle documente une absence de désignation et une anticipation d'industrie, pas un pronostic — l'encadré ci-dessus expose pourquoi la question demeure ouverte. Il ne dit pas quelles seront les modalités de l'accréditation, ni le contenu du registre public : ni les unes ni l'autre ne sont au socle. Il ne dit pas que la loi issue de C-15 soit intégralement en vigueur : le socle documente une sanction royale, non un calendrier d'entrée en vigueur des dispositions. Il ne dit rien, enfin, de la couche sémantique des paiements canadiens — ISO 20022, Lynx et le système de paiement en temps réel dont le lancement est visé au T4 2026 sont l'objet du chapitre 15[^10] —, ni de l'articulation entre les protocoles de transaction agentique et les rails canadiens, question que le chapitre 16 traite comme explicitement prospective.

Le cadre bancaire canadien offre à l'architecte un objet rare : une obligation certaine dont l'implémentation est indéterminée. Ce n'est pas une raison d'attendre. C'est une raison de concevoir en sachant ce que l'on ignore.

---

## Notes

[^1]: PRD §7.4, **F-11** (niveau [A]). Sources primaires : Finances Canada (Budget 2025) ; parl.ca (projet de loi C-15) ; Gazette du Canada (régime de cotisation, partie I, 27 juin 2026). **Réserves F-11**, appliquées ici : (1) mécaniquement, C-15 a **abrogé et remplacé** la loi partielle de 2024 — il ne s'agit pas d'un simple amendement ; (2) C-15 est cité **au passé** (loi adoptée) ; (3) la citation canada.ca est vérifiée par corroboration convergente, le *fetch* direct retournant une erreur 403. **Réserve non levée signalée à la gouvernance** : le socle porte le titre de la loi au pluriel (« Loi sur les services bancaires axés sur les consommateurs ») avec la mention « à confirmer sur parl.ca en P0.1 » — la passe P0.1 du 16 juillet 2026 n'a pas traité ce point (`verification/revalidation-2026-07-16.md`). Le présent chapitre retient la forme du socle et distingue le **cadre** (« axés sur le consommateur », singulier) de la **loi** (« axés sur les consommateurs », pluriel), conformément aux formes du socle ; la confirmation reste à obtenir en P4.1.

[^2]: PRD §7.3, **F-24** (niveau [B] — revalidé le 16 juillet 2026 par consultation directe de parl.ca/LEGISinfo, 45-1/c-36). Le projet de loi **C-36** (titre officiel : *Protecting Privacy and Consumer Data Act*, PPCDA), parrainé par Evan Solomon, a fait l'objet d'une **première lecture le 15 juin 2026** et se trouve à l'étape de la **deuxième lecture au 16 juillet 2026** : il n'est **pas** adopté et ne modifie donc rien à ce jour. **Précision de portée imposée par le socle** : C-36 est une réforme de la protection des renseignements personnels (modification de la LPRPDE, création de la *Digital Safety and Data Protection Commission of Canada*) portant des volets IA — transparence algorithmique, droit à l'effacement, données des enfants —, et **non une loi IA autonome** de type LIAD (forme du glossaire §D.7). Son examen relève du ch. 10 ; il n'est mobilisé ici que pour le constat de véhicule législatif commun. Aucune source ne documente d'interaction entre C-15 et C-36.

[^3]: PRD §7.4, **F-35** (niveau [A] — **fait négatif vérifié 9-0**). Sources primaires : gazette.gc.ca ; canada.ca (communiqué de Finances Canada et page du Budget 2025) ; bankofcanada.ca. L'entrée porte : l'exigence d'un standard technique unique fixé par un organisme de normalisation technique **désigné par le ministre des Finances par arrêté ministériel** ; les critères de désignation (« *meaningfully Canadian* » — cité verbatim en langue originale, CA-5 —, gouvernance équitable, ouverte et accessible, décision indépendante) ; les quatre objectifs du standard (sécurité, concurrence, innovation, interopérabilité mondiale) ; le périmètre de supervision de la Banque du Canada (entités participantes, fournisseurs tiers accrédités, organisme de normalisation technique, organisme externe de traitement des plaintes) et son registre public ; le maintien du mandat général de l'ACFC sous la Loi sur les banques. **Recherche exhaustive des chaînes « FDX », « Financial Data Exchange », « FAPI » et « OAuth » dans le règlement prépublié, le communiqué et la page Budget 2025 : zéro occurrence.** L'anticipation de FDX relève du **commentaire d'industrie** (Fasken, Bennett Jones, NCFA), attribué comme tel à chaque occurrence.

[^4]: PRD §7.4, **F-23** (niveau [A]). Sources : rapport annuel Desjardins 2025 (rapport de gestion, 24 février 2026) ; Finances Canada ; analyses Fasken, DLA Piper, McCarthy Tétrault, Baker McKenzie (corroboration secondaire, PRD §9.2 — jamais source unique d'un fait central). Participation au cadre conditionnelle à l'**accréditation par la Banque du Canada** ; **modalités à définir par règlement** ; **registre des participants tenu par la Banque du Canada**. Desjardins est mentionnée ici au seul titre de l'accréditation ; son traitement pour elle-même relève du ch. 17 (**F-23b**).

[^5]: PRD §7.4, **F-34** (niveau [A]). Sources primaires : gazette.gc.ca (texte du règlement prépublié, partie I, vol. 160, no 26, 27 juin 2026) ; canada.ca/Finances (communiqué du 26 juin 2026). Période de commentaires de **60 jours**, close le **26 août 2026** — décompte revérifié à la rédaction (27 juin → 26 août 2026 = 60 jours). Entrée en vigueur **échelonnée** : accréditation d'abord, puis règles communes et frais d'évaluation **dans l'année suivant la publication finale** ; phasage par produits et services précisé à la publication finale. Le règlement est pris sous la Loi sur les services bancaires axés sur les consommateurs (sanction royale de mars 2026 via C-15, F-11).

[^6]: PRD §8.3 (sensibilité temporelle) et rapport `verification/revalidation-2026-07-16.md`, ligne « Règlement du cadre bancaire — commentaires / désignation » : verdict **INCHANGÉ** — période de commentaires toujours fixée au 26 août 2026, aucun amendement recensé ; **aucun arrêté ministériel de désignation de l'organisme de normalisation technique publié à ce jour** ; aucune mention officielle de FDX/FAPI/OAuth dans le texte réglementaire ni sur les pages de la Banque du Canada. **Piège de datation explicite de PRD §8.3** : le règlement est **prépublié** — le texte final peut changer. Revalidation exigée après le 26 août 2026 (PRDPlan P4.1 ; conditions de péremption de l'ouvrage : ch. 21 §21.3 ; événements de péremption du blueprint : ch. 24 §24.2).

[^7]: PRD §7.3, **F-09** — entrée de niveau **[A/B mixte]** : **[A]** pour les faits des passes 1-2 (vote adversarial 3-0), **[B]** pour les exigences opératoires extraites du texte intégral le 16 juill. 2026 (source primaire lue, sans vote — niveau **inférieur** à [A] dans la taxonomie du PRD §7 : l'extraction enrichit l'entrée, elle ne l'élève pas). **Le présent chapitre ne mobilise que la strate [A]** — ligne directrice E-23 du BSIF, version finale du 11 septembre 2025, en vigueur le 1er mai 2027 (source primaire : osfi-bsif.gc.ca) ; aucune exigence opératoire d'E-23 (cycle de vie, inventaire, cotation, documentation, surveillance) n'est citée ici. Et **F-25** (niveau [A], ligne directrice sur l'IA de l'AMF, **finale depuis le 30 mars 2026**, en vigueur le 1er mai 2027 — source primaire : lautorite.qc.ca). Renvois aux ch. 9 et 11, où ces instruments sont traités. **Réserve F-25** appliquée : ne jamais écrire « en attente » ni « en projet ». Décompte revérifié à la rédaction : du 16 juillet 2026 au 1er mai 2027 = neuf mois et quinze jours (concordant avec le ch. 10). La portée d'E-23 sur l'agentique n'est pas discutée ici (territoire du ch. 9) : elle relève de la formulation imposée par PRD §8.2.4.

[^8]: PRD §8.1, garde-fou **R-5** : « FDX est le standard technique retenu pour le cadre bancaire canadien » est une affirmation **interdite** dans l'ouvrage (CA-2) — aucun standard n'est nommé dans les textes officiels (F-35) ; FDX est une anticipation d'industrie ; la désignation par arrêté ministériel est à venir. La formulation du fait négatif est **imposée par PRDPlan §4.4** (« fait négatif vérifié — standard technique ») et reprise mot pour mot en §14.4. Substitut terminologique imposé : glossaire §D.7 (`monographie/90-annexes/annexe-d-glossaire.md`), « organisme de normalisation à désigner par arrêté ministériel ».

[^9]: Encadré au format imposé par PRDPlan §4.4 (« encadré de lacune »), clause de clôture reprise mot pour mot. Lacune **PRD §10.1** — « Désignation de l'organisme de normalisation technique du cadre bancaire » : arrêté ministériel à venir ; texte final du règlement attendu après le 26 août 2026 ; surveiller gazette.gc.ca et bankofcanada.ca. Recherche documentée : `verification/revalidation-2026-07-16.md`. Assignation de la lacune au présent chapitre : [TOC.md](../../TOC.md), « Contrôle de couverture », ligne 10.1 — « ch. 14 (R-5) », sans autre chapitre porteur inscrit.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026 ; corps = 3 290 mots après relecture adversariale, cible 3 000,
                                   tolérance ±10 % = 2 700-3 300 ; décompte recompté sur le texte corrigé — les correctifs de
                                   relecture ont ajouté du fond tracé (note F-24, note F-28/F-29, dissociation des registres),
                                   deux redondances introduites par ces mêmes correctifs ont été resserrées pour rentrer sous
                                   le plafond)
     2. Traçabilité (CA-1, CA-5) . fait (10 notes, numérotation séquentielle revérifiée APRÈS insertion des notes F-24 et
                                   F-28/F-29 — renumérotation complète par ordre de premier renvoi ; chaque affirmation centrale
                                   tracée F-11/F-23/F-34/F-35, renvois F-09/F-24/F-25/F-28/F-29/F-23b notés comme tels ; termes anglais en
                                   italique entre parenthèses à la 1re occurrence du chapitre : single technical standard,
                                   data portability ; « meaningfully Canadian » cité verbatim en langue originale)
     3. Balayage garde-fous ...... fait :
                                   - R-5 (motif « FDX|Financial Data Exchange|standard technique ») : toutes les occurrences
                                     inspectées. FDX n'apparaît JAMAIS comme standard retenu ; à chaque occurrence il est
                                     qualifié « anticipation d'industrie » / « commentaire d'industrie » avec attribution
                                     nominative (Fasken, Bennett Jones, NCFA). Formulation imposée §4.4 reprise MOT POUR MOT
                                     en §14.4. Substitut §D.7 employé.
                                   - §8.3 : le règlement est dit « prépublié » et « susceptible de changer » à chaque
                                     mention de son contenu ; date de gel rappelée dans le corps ; renvoi P4.1/ch. 24.
                                   - réserve F-25 (motif « en attente|en projet ») : aucune occurrence près de l'AMF —
                                     la seule mention de l'AMF (§14.3) la dit « finale », note [^7].
                                   - R-4 / réserve F-29 (motif « RTR|Real-Time Rail|T4 2026 ») : une occurrence, en
                                     conclusion, formulée « dont le lancement est visé au T4 2026 » (substitut imposé §D.7),
                                     en renvoi au ch. 15 — ni « lancé », ni « en production », ni « aucune date annoncée ».
                                   - R-7 (motif « E-23|B-13 ») : deux occurrences en contexte réglementaire pur, sans objet
                                     (filtrage prévu par PRDPlan §4.3) ; aucun contexte produit dans ce chapitre.
                                   - R-8 (motif « ACP|control plane|plan de contrôle ») : zéro occurrence.
                                   - §8.2.2/§7.5 (métriques auto-déclarées) : aucune métrique institutionnelle citée ;
                                     Desjardins mentionnée sans chiffre, au seul titre de l'accréditation (F-23).
                                   - §8.2.4 (E-23 x agentique) : la portée d'E-23 sur l'agentique n'est PAS discutée ici
                                     (territoire du ch. 9) ; le renvoi ne porte que la date d'entrée en vigueur. La
                                     caractérisation du mode d'assujettissement d'E-23, non tracée au socle, a été retirée du
                                     corps en relecture (voir 5, réserve 6).
     4. Arithmétique ............. fait (chaque durée posée depuis les dates du socle et revérifiée deux fois) :
                                   - 18 nov. 2025 -> 26 mars 2026 = 128 j = quatre mois et huit jours
                                   - 26 mars 2026 -> 27 juin 2026 = 93 j = trois mois et un jour
                                   - 27 juin 2026 -> 26 août 2026 = 60 j (concorde avec les « 60 jours » de F-34)
                                   - 16 juill. 2026 -> 26 août 2026 = 41 j = quarante et un jours
                                   - 16 juill. 2026 -> 1er mai 2027 = 289 j = neuf mois et quinze jours (concorde ch. 10)
                                   Aucun calcul tenté sur « dans l'année suivant la publication finale » (point de départ
                                   inconnu) ni sur l'écart 2024 -> C-15 (le socle ne date pas la loi de 2024 au mois près).
     5. Relecture adversariale ... FAIT — deux relecteurs indépendants (PRDPlan §4.2.4). Premier jet RÉFUTÉ : 6 constats
                                   bloquants + 10 réserves, tous vérifiés au socle avant application ; 15 fondés et appliqués,
                                   1 réserve reportée à la gouvernance (voir plus bas). Ce que la relecture a réfuté :
                                   - BLOQUANT — statut de C-36 : « deux instruments distincts MODIFIENT la LPRPDE » affirmait
                                     au présent qu'un projet de loi en 2e lecture modifie déjà le droit (F-24). Corrigé :
                                     « un instrument adopté et un projet de loi distinct visent le même véhicule », statut daté
                                     rappelé, note F-24 ajoutée. C'était le piège de datation de PRD §8.3 que le chapitre
                                     proscrit lui-même deux paragraphes plus haut.
                                   - BLOQUANT — R-5 dans l'encadré : « La désignation déterminera si FDX [...] devient le
                                     standard canadien » — seule des 4 occurrences de FDX à avoir perdu sa qualification, dans
                                     le passage le plus citable du chapitre, et suivie de « aucune inférence n'est proposée ici ».
                                     Le balayage R-5 du premier jet se déclarait pourtant complet : FAUX. Corrigé, attribution
                                     nominative restituée (Fasken, Bennett Jones, NCFA).
                                   - BLOQUANT — méthode de l'encadré : la passe P0.1 se voyait attribuer 5 sources et une
                                     recherche exhaustive de chaînes que le rapport de revalidation ne porte pas (périmètre réel :
                                     gazette.gc.ca + bankofcanada.ca). L'encadré contredisait le corps (l. 75), qui distinguait
                                     correctement les deux passes. Corrigé : constitution du socle (F-35) et P0.1 dissociées.
                                   - BLOQUANT — Desjardins : « source primaire auditée » (le socle dit rapport de GESTION, hors
                                     opinion d'auditeur) et « traite l'accréditation comme une étape à venir » (caractérisation
                                     absente de F-23, qui repose sur un faisceau). Corrigé ici et en note ; « auditée » supprimé.
                                   - BLOQUANT — abrogation : « le texte de 2024 n'est plus le droit applicable » (présent)
                                     contredisait les deux aveux du chapitre lui-même sur l'entrée en vigueur non documentée.
                                     Corrigé : passé mécanique + Lecture de l'auteur explicite.
                                   - BLOQUANT — ouverture : « aucune institution ne peut écrire une ligne de code contre ce
                                     cadre » — inférence non marquée en l. 1, plus forte que ce que §14.4 défend, et fournissant
                                     un argument d'attentisme que la conclusion réfute. Marquée et bornée.
                                   - RÉSERVES appliquées : futur du socle restitué (F-35 « supervisera / tiendra », §14.2 et
                                     conclusion) ; registre public (F-35) et registre des participants (F-23) dissociés — le
                                     socle n'établit pas leur identité ; renvoi de péremption redirigé (ch. 21 §21.3 pour
                                     l'ouvrage, ch. 24 §24.2 pour le blueprint) ; caractérisation d'E-23 retirée ; forme imposée
                                     §4.4 restituée INTÉGRALEMENT en synthèse (3e clause « la candidature de FDX relève du
                                     commentaire d'industrie » manquait) ; note F-28/F-29 ajoutée + socle d'en-tête complété ;
                                     « se sécher sur » (non français) → « s'adosser à ».
     6. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.
     Passe de correction F-09 (16 juill. 2026, enrichissement de l'entrée par extraction du texte intégral d'E-23) : 1 correction —
     note [^7] remarquée « [A/B mixte] » avec mention explicite que le chapitre ne mobilise que la strate [A] (dates) et que [B] est
     SOUS [A] dans la taxonomie §7 ; corps intact (volumétrie inchangée). Sans objet ici : affirmation d'absence d'extraction (aucune),
     « exigé par E-23 » (aucune — les occurrences d'« exigence »/« impose » portent sur C-15/F-35, pas sur E-23), « fiches de modèles »
     (zéro occurrence, chapitre sans contexte produit).
     Points signalés à la gouvernance (non corrigés ici — CLAUDE.md, règle de chirurgie) :
     - F-11 porte « titre au pluriel — à confirmer sur parl.ca en P0.1 » ; la passe P0.1 du 16 juillet 2026 n'a PAS traité
       ce point (le rapport de revalidation ne le mentionne pas). Réserve toujours ouverte, à porter en P4.1.
     - F-11 et F-34 datent tous deux du 27 juin 2026 une parution à la Gazette, partie I : le régime de cotisation
       (recouvrement des coûts, F-11) et le règlement du cadre (F-34). Le socle n'établit pas s'il s'agit d'un instrument
       unique ou de deux textes distincts. Le chapitre expose les deux faits sans trancher. À clarifier au socle.
     - TOC assigne au ch. 14 le socle F-11, F-23, F-34, F-35. La section 14.3 (imposée par TOC) appelle un point de
       comparaison calendaire avec les régimes du 1er mai 2027 : F-09 et F-25 ajoutés en renvoi par la rédaction, sans
       empiéter sur les ch. 9 et 11 (seules les dates d'entrée en vigueur sont reprises). PRD §6 (ligne ch. 14) porte en
       outre F-28 et F-29 au socle du chapitre : ajoutés en renvoi à l'en-tête en relecture, note dédiée, traitement au ch. 15.
     - F-11 documente une sanction royale (26 mars 2026) mais aucun calendrier d'entrée en vigueur des dispositions de la
       loi elle-même (par opposition au règlement, F-34). Le chapitre le dit et s'abstient. Écart de socle à combler en P4.1
       si l'ouvrage doit affirmer que la loi est en vigueur.
     - PRD §10.1 / renvoi ch. 21 — RÉSERVE DE RELECTURE NON RÉSOLUE, ARBITRAGE REQUIS. Le premier jet annonçait « le
       chapitre 21 la reprend » (corps + note) ; vérification faite, TOC.md « Contrôle de couverture » ligne 10.1 porte
       « ch. 14 (R-5) » et AUCUN renvoi au ch. 21 — contrairement à la ligne 10.5, qui inscrit explicitement
       « ch. 16 (prospectif) ; renvoi ch. 21 ». La bijection étant un instrument de gouvernance, la mention a été RETIRÉE
       du corps et de la note (option la plus réversible ; TOC.md hors périmètre de cette tâche). Le ch. 21 est par ailleurs
       décrit au TOC comme « reprise honnête de §10 » (§21.1) : l'intention d'une reprise est donc plausible. À trancher :
       soit inscrire « renvoi ch. 21 » à la ligne 10.1 de TOC.md (version++) et restaurer la phrase, soit laisser §10.1
       portée par le seul ch. 14. Ne pas rédiger le ch. 21 avant l'arbitrage — risque d'orphelin ou de doublon non contrôlé.
-->

[^10]: PRD §7.4, **F-28** (niveau [A], Lynx : adoption complète d'ISO 20022 — messages MX — en novembre 2025, fin de la coexistence MT/MX le 22 novembre 2025 ; source primaire : payments.ca) et **F-29** (niveau [A], Real-Time Rail : tests industriels en cours à la mi-2026, système non en production ; **cible officielle de lancement au T4 2026**, ISO 20022 dès le lancement ; source primaire : payments.ca, page revalidée le 16 juillet 2026). **Réserve F-29 appliquée (garde-fou R-4)** : le T4 2026 est une **cible**, non un fait accompli — historique de reports (2019 → 2022 → 2023 → 2026) ; substitut terminologique du glossaire §D.7 employé (« dont le lancement est visé au T4 2026 »). Ces deux entrées sont mobilisées ici **en renvoi seulement** : leur traitement relève du ch. 15 (TOC).

