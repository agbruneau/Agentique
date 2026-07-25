# Chapitre 15 — ISO 20022 : Lynx accompli, RTR imminent

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | F-28, F-29, F-45 ; **F-04** (§15.4, énumération des sources primaires d'AP2 que le socle porte) ; §10.5 et §10.9e (renvoi ch. 16) |
| Garde-fous à surveiller (PRD §8) | **R-4** (la cible T4 2026 *est* officiellement annoncée) et **réserve F-29** (elle demeure une cible : ne jamais écrire « lancé » ni « en production ») ; §8.2 (jalons de programme = communications d'opérateur, attribués à chaque occurrence) ; §8.4 (le rôle d'IBM Canada sur les rails est un fait de contexte, pas un argument de conformité) |
| Volumétrie cible | ~2800 mots |

> **Thèse ([TOC.md](../../TOC.md))** : la couche sémantique commune des paiements canadiens est en place — Lynx a achevé sa bascule ; **Paiements Canada annonce un RTR nativement ISO 20022 dès son lancement, visé au T4 2026**.

> ⚠ **Correctif de la rédaction (16 juill. 2026) — dette éteinte le 17 juill. 2026** : la section 15.4 prévue par [TOC.md](../../TOC.md) portait « Ce que la richesse des données change pour les agents ». F-28 et F-29 ne documentent **aucun attribut de richesse des données** — ni structure des données de remise, ni granularité des identifiants, ni comparaison avec le format retiré : la section prévue ne peut être écrite sans excéder le socle. Elle est **recentrée sur l'unicité du format** (« Ce que la couche sémantique commune change — et ce que le socle n'en dit pas »), et le refus est exposé en encadré « état de la connaissance vérifiable » (§15.4). **L'amendement de TOC.md, déclaré dû par le présent chapitre depuis son gel, a été exécuté le 17 juillet 2026 (TOC v1.5, suites de l'audit — constat M-11)** : la section 15.4 y porte désormais « Ce que la couche sémantique commune change — et ce que le socle n'en dit pas » (intitulé aligné mot pour mot sur le titre réel de cette section, pour la bijection J-2 stricte), et le correctif y est consigné. La bijection J-2 est rétablie ; aucune information nouvelle n'entre au chapitre, dont la date de gel demeure le 16 juillet 2026.

---

Un architecte d'entreprise qui conçoit aujourd'hui une chaîne de paiement canadienne travaille sur un terrain d'une asymétrie singulière. D'un côté, un rail achevé : le système de paiements de grande valeur Lynx a terminé sa migration vers ISO 20022, et l'alternative technique qui subsistait a été retirée. De l'autre, un rail annoncé, daté, testé — mais qui n'a pas encore traité un paiement en exploitation. Les deux parleront le même langage sémantique. L'un le parle déjà ; l'autre le parlera dès son premier jour, si ce jour arrive à la date visée.

Ce chapitre soutient que la couche sémantique commune des paiements canadiens est en place, et qu'il faut prendre ce verbe au sérieux dans les deux directions. « En place » signifie que le choix de format n'est plus une variable d'architecture : sur Lynx, il est arrêté et irréversible ; sur le **RTR** (*Real-Time Rail*), il est arrêté par construction. « En place » ne signifie pas « en exploitation partout » : la distinction entre un rail accompli et un rail imminent est précisément ce que ce chapitre s'attache à ne pas laisser confondre, parce que c'est la confusion la plus coûteuse qu'un dossier d'architecture puisse commettre à la mi-2026.

## 15.1 Lynx : une migration achevée, et ce que cela veut dire

Le fait central est daté. Le **22 novembre 2025**, la coexistence des messages MT et MX prend fin sur Lynx : les MT 1xx/2xx sont retirés au profit des pacs.008 et pacs.009, et les messages MT hérités ne sont plus pris en charge. Paiements Canada annonce l'achèvement le 26 novembre 2025. La bascule technique est alignée sur l'échéance mondiale SWIFT CBPR+[^1].

Cette date clôt une transition longue. La coexistence avait été ouverte par la Release 2 de **mars 2023** ; de mars 2023 au 22 novembre 2025, il s'écoule donc quelque **trente-deux mois** — deux ans et huit mois durant lesquels le rail a accepté l'un et l'autre format, chaque institution restant maîtresse du moment où elle basculait ses propres chaînes. Et la bascule finale n'a pas été un basculement. Selon Paiements Canada, **plus de 98 % des messages Lynx étaient déjà MX en octobre 2025**[^1] — moins de 2 % du trafic déclaré restait donc en MT à cette date ; le 22 novembre 2025 a mis fin à la coexistence et retiré les MT 1xx/2xx[^1].

**Lecture de l'auteur** : le 22 novembre n'a vraisemblablement pas déplacé le volume — il a supprimé un reliquat, et surtout il a supprimé l'option ; le socle donne la part déjà basculée en octobre 2025, non la part résiduelle à la date de bascule elle-même. Pour l'architecte, la valeur de cette date ne tient donc pas à la nouveauté d'un format, elle tient à la **disparition d'une alternative**. Tant que la coexistence durait, la question « quel format ce flux émet-il ? » restait ouverte et devait être tranchée composant par composant, avec la logique conditionnelle, les tests et la dette que cela suppose. Le socle établit le retrait des MT et l'arrêt de leur prise en charge par le rail ; il n'établit pas ce que chaque institution a fait de ses propres chaînes internes en amont. Ce que la fin de la coexistence garantit, c'est qu'à la frontière du rail il n'existe plus de branche à maintenir. Ce qu'elle ne garantit pas, c'est qu'il n'en subsiste aucune à l'intérieur des institutions — question qui relève de l'inventaire de chacune, pas de ce chapitre.

Un mot, encore, sur l'alignement de la date. Le socle précise que la bascule du 22 novembre 2025 était **alignée sur l'échéance mondiale SWIFT CBPR+**[^1] — et cette précision, souvent lue comme un détail de calendrier, mérite mieux. Elle situe la date canadienne sur un calendrier qui n'est pas propre au Canada, mais commun aux correspondants bancaires du monde entier. **Lecture de l'auteur** : la date de bascule paraît ainsi tenir à une contrainte extérieure, et un architecte qui aurait cherché à négocier un report de sa date de bascule interne aurait négocié contre un calendrier qu'aucun acteur canadien ne maîtrisait. Le socle établit l'alignement ; il n'établit pas que l'échéance mondiale ait été la cause de la date canadienne, seulement qu'elles coïncident. La nuance est mince, mais elle est de celles qui séparent une observation d'une reconstruction rétrospective, et cet ouvrage s'astreint à la première.

Le rail lui-même a une histoire industrielle qu'il vaut de rappeler, parce qu'elle éclaire la section suivante. **IBM Canada est le « lead technology partner » de Lynx** : la sélection est annoncée le 2 mai 2019 et couvre l'hébergement, l'intégration de systèmes, la bascule du LVTS vers Lynx et l'exploitation ; le système est lancé le 1er septembre 2021 — **vingt-huit mois** après l'annonce du partenariat — et un centre de données additionnel s'y ajoute en octobre 2023[^2]. Deux réserves accompagnent ce fait et doivent être portées avec lui : les montants des contrats ne sont pas publics, et — conformément à la règle de neutralité fournisseur de cet ouvrage — le rôle d'IBM Canada sur les rails canadiens est un **fait de contexte**, jamais un argument de conformité réglementaire[^3]. Le socle ne documente aucun lien entre ce rôle et les lignes directrices E-23 ou B-13 du BSIF.

## 15.2 RTR : une chronologie vérifiée, une cible annoncée, une cible reportée

Le RTR n'est pas un projet dont on ignorerait l'état d'avancement. C'est, au contraire, l'un des objets les mieux jalonnés du socle de cet ouvrage — neuf affirmations confirmées par vote adversarial unanime, sur quatre pages officielles de Paiements Canada dont la page RTR revalidée le 16 juillet 2026[^4]. La difficulté n'est pas de savoir où il en est ; elle est de dire son statut sans le surqualifier ni le sous-qualifier, deux fautes symétriques et également disqualifiantes dans un dossier d'architecture.

La chronologie, telle que Paiements Canada la communique, est la suivante. Interac avait livré la composante d'échange en **juin 2023**. Le programme est **repris le 16 avril 2024**, avec IBM Canada et CGI comme nouveaux partenaires de livraison et d'exploitation aux côtés d'Interac ; la page officielle des partenaires de livraison, revalidée le 16 juillet 2026, liste également **Deloitte Canada** comme quatrième partenaire, **sans en détailler le rôle** — le socle enregistre la présence, pas la fonction, et cet ouvrage n'en dira pas davantage. La construction de la composante compensation et règlement est entamée à la fin de l'été 2024 et **complétée au T3 2025**. Les tests internes (SIT) sont **complétés au T4 2025**, les tests d'acceptation utilisateur **au T1 2026**. Suivent les tests de performance, de sécurité et de résilience, puis les **tests industriels** (*industry solution assurance testing*), **en cours à la mi-2026**[^4].

D'où l'énoncé qui doit être tenu mot pour mot, et que le lecteur pressé retiendra de préférence à tout le reste : **à la mi-juillet 2026, le RTR n'est pas en production**[^4]. Aucune formulation de ce chapitre — ni d'aucun autre chapitre de cet ouvrage — ne doit laisser entendre qu'il serait lancé ou exploité[^5].

Symétriquement, et c'est l'autre versant du garde-fou, il serait tout aussi faux d'écrire qu'aucune date n'aurait été annoncée. **Paiements Canada vise un lancement au T4 2026, à l'issue des tests industriels en cours ; la cible a été successivement reportée — 2019, puis 2022, puis 2023, puis 2026**[^5]. Ces quatre valeurs sont les **cibles successives**, non les dates auxquelles les reports ont été décidés — la distinction importe, faute de quoi la phrase raconterait une histoire que le socle ne porte pas. Paiements Canada annonce un **lancement graduel**, dont le déploiement se poursuivrait en 2027, et — point décisif pour ce chapitre — **ISO 20022 dès le lancement**[^4].

Posons l'écart, puisqu'il structure toute planification qui s'appuierait sur ce rail. En retenant le trimestre civil — le socle ne précise pas la convention de Paiements Canada, et un exercice financier décalé déplacerait tous les intervalles qui suivent —, l'ouverture du T4 2026 tombe le 1er octobre. Du 16 avril 2024, date de la reprise du programme, à cette ouverture, il s'écoule **un peu moins de trente mois**. Et de la première cible annoncée, 2019, à la cible en vigueur, 2026, **sept ans** séparent l'intention initiale de l'échéance actuellement visée.

**Lecture de l'auteur** : ces deux nombres ne disent pas la même chose et ne doivent pas être lus ensemble sans précaution. Le socle établit quatre cibles successives ; il n'établit ni les causes des reports, ni une quelconque probabilité que le T4 2026 soit tenu. Un historique de reports n'est pas un pronostic — il est une information sur la classe de risque à laquelle appartient l'engagement, non sur l'engagement lui-même. Ce que l'architecte prudent en tire n'est pas « le RTR sera reporté », affirmation que rien n'autorise, mais une exigence de conception : **tout plan dont la valeur dépend d'une date de disponibilité du RTR doit porter son scénario de report**, au même titre qu'il porterait celui de tout fournisseur externe. Le socle fournit les jalons ; l'inférence de gestion appartient à l'institution.

Une dernière précision, négative, mérite d'être consignée parce qu'elle protège le lecteur d'une source vieillie. **Aucune source primaire du socle ne mentionne Mastercard ni Vocalink parmi les partenaires actuels du RTR**[^4] ; les partenaires établis sont Interac, IBM Canada, CGI et Deloitte Canada, ce dernier au rôle non détaillé par la source. **Lecture de l'auteur** : un dossier qui citerait Mastercard ou Vocalink comme partenaires actuels contredirait les sources primaires disponibles au 16 juillet 2026 — le socle ne dit rien, en revanche, d'une éventuelle association passée, et l'auteur n'en infère aucune.

Le rôle d'IBM, enfin, s'inscrit dans la continuité de la section précédente. IBM Canada est partenaire de livraison et d'exploitation du RTR depuis le 16 avril 2024, avec CGI et Interac, pour la construction de la composante compensation et règlement et son exploitation, au titre de ses « IBM Payments Centre capabilities »[^2]. La même réserve s'applique, à l'identique : montants non publics, fait de contexte, aucun argument de conformité n'en découle[^3].

## 15.3 By-law no 10 : l'instrument juridique précède le rail

Le règlement administratif du RTR — **By-law No. 10** — a été publié dans la **Gazette du Canada, partie II, le 1er juillet 2026**, et **entre en vigueur le 24 août 2026**[^4]. Quinze jours séparent cette publication de la date de gel du présent chapitre ; à cette date, l'instrument est donc publié mais **pas encore en vigueur**, et le lecteur qui consulte ces pages après le 24 août 2026 lit un chapitre dont ce fait précis a changé de temps grammatical.

Les intervalles se calculent simplement. De la publication à l'entrée en vigueur : du 1er juillet au 24 août 2026, **cinquante-quatre jours**. De l'entrée en vigueur à l'ouverture du trimestre visé pour le lancement — le 1er octobre 2026, sous la réserve de convention posée plus haut : du 24 août au 1er octobre 2026, **trente-huit jours**, un peu plus de cinq semaines.

Ce que le socle établit ici s'arrête à ces trois dates et à leur ordre. Il n'établit **pas le contenu du by-law**, et ce chapitre s'interdit donc d'en décrire les obligations, les seuils ou les mécanismes.

**Lecture de l'auteur** : la seule chose que la séquence autorise à observer, c'est que l'instrument juridique **entre en vigueur avant** l'ouverture du trimestre visé, et non après. C'est l'ordonnancement attendu d'un rail dont la participation est réglementée ; le passage des contraintes réglementaires aux frames déterministes est l'objet du **chapitre 13**. Le socle donne la chronologie ; il ne dit rien du contenu du by-law, ni de l'intention qui a produit cet ordonnancement, et l'auteur ne les lui prête pas.

Il faut par ailleurs relever ce que cette date fait au reste du chapitre. Le 24 août 2026 est **postérieur à la date de gel** du présent chapitre de trente-neuf jours — du 16 juillet au 24 août 2026 —, ce qui en fait l'un des points de revalidation de cet ouvrage : au 16 juillet 2026, l'entrée en vigueur est un fait annoncé, pas un fait constaté. La distinction paraîtra excessive ; elle ne l'est pas. C'est exactement la même distinction que celle qui sépare, quelques paragraphes plus haut, une cible de lancement d'un lancement — et la discipline qui consiste à la tenir partout, y compris là où elle semble ne rien coûter, est ce qui permet de la tenir là où elle coûte cher.

## 15.4 Ce que la couche sémantique commune change — et ce que le socle n'en dit pas

Reste la question que la Partie IV pose à cet ouvrage : qu'est-ce que tout cela change pour des agents ?

Commençons par ce que le socle établit, et qui n'est pas rien. **Après le 22 novembre 2025, Lynx ne connaît plus qu'un jeu de messages ; le RTR, s'il est lancé au T4 2026 comme Paiements Canada le vise, le sera nativement ISO 20022**[^1] [^4]. Ces deux rails auront donc une **couche sémantique commune** — et cette communauté n'est pas le fruit d'une convergence progressive à laquelle il faudrait encore laisser du temps : elle est acquise sur l'un par retrait de l'alternative, et posée sur l'autre par construction.

**Lecture de l'auteur** : la conséquence d'architecture est une conséquence de **surface**, pas de capacité. Un système appelé à interagir avec les deux rails n'a plus deux vocabulaires à apprendre, mais un ; ce qui était une question de traduction devient une question de routage. Pour un composant logiciel — agentique ou non — cela réduit le nombre de représentations à maintenir, donc le nombre d'endroits où une erreur de correspondance peut naître. Le socle établit l'unicité du format sur Lynx et son adoption native prévue sur le RTR ; il n'établit pas que cette unicité produise un gain mesurable, et aucune source de cet ouvrage ne le quantifie.

Il faut ici marquer nettement la frontière, car c'est le point où un chapitre de cette nature dérape ordinairement.

> **État de la connaissance vérifiable — ce que le socle n'établit pas sur ISO 20022 et les agents**
>
> Deux questions se posent naturellement à cet endroit, et aucune ne trouve de réponse dans le socle de cet ouvrage.
>
> **(1) Le contenu informationnel des messages.** Vérification menée contre le socle le 16 juillet 2026 : F-28 nomme les types de messages en cause sur Lynx (pacs.008, pacs.009, en remplacement des MT 1xx/2xx) ; F-29 établit l'adoption d'ISO 20022 dès le lancement du RTR, sans nommer de type de message. **Ni l'une ni l'autre ne documente d'attribut de richesse des données** — ni structure des données de remise, ni granularité des identifiants, ni comparaison avec le format retiré. Toute affirmation sur ce que les messages ISO 20022 « portent de plus » excéderait ce que ce socle permet d'écrire, et n'est donc pas proposée ici.
>
> **(2) L'usage agentique des rails canadiens.** Recherche menée le 16 juillet 2026 (PRD §10.5) : aucune source du socle ne documente l'articulation entre les protocoles de transaction agentique et les rails de paiement canadiens[^6]. Le périmètre balayé doit être énoncé exactement, faute de quoi le constat vaudrait plus large que ce qui l'appuie : d'un côté, les quatre pages officielles de Paiements Canada, dont la page RTR revalidée le 16 juillet 2026, où AP2 n'est pas mentionné (F-29) ; de l'autre, les deux seules sources primaires d'AP2 que le socle porte — l'annonce Google Cloud du 16 septembre 2025 et le communiqué de la Linux Foundation du 9 avril 2026 (F-04) —, qui ne nomment aucun rail canadien. **La spécification d'AP2 elle-même n'est pas au socle** (PRD §10.9e : aucune structure de message, aucun mandat, aucune preuve d'intention), et le socle ne porte aucun communiqué d'Interac : ni l'une ni les autres n'ont donc été balayés, et le présent chapitre ne les compte pas au nombre des sources consultées. La question échoue faute de source primaire, non faute d'avoir été cherchée. En l'absence de source primaire, la question reste **ouverte** ; aucune inférence n'est proposée ici. Elle fait l'objet du **chapitre 16**, explicitement prospectif, et n'est pas anticipée ici.

Ce qui peut, en revanche, être dit sans excéder le socle tient en une phrase d'ordonnancement. À la date de gel, **l'un des deux rails est un acquis et l'autre est une cible**[^4] ; un dossier d'architecture qui les traiterait au même titre — parce que tous deux « seront en ISO 20022 » — mélangerait un fait établi et une prévision conditionnelle. Le premier se conçoit contre une spécification en exploitation ; le second se conçoit contre un engagement d'opérateur assorti d'un historique de reports. Ce sont deux régimes de preuve, et le présent ouvrage refuse de les additionner.

Enfin, sur le versant proprement agentique, la Partie VI et la Partie VII développent ce que l'encadrement déterministe implique pour un flux de paiement : le principe est posé au chapitre 13, l'architecture de référence au chapitre 19, et le flux de bout en bout — un paiement ISO 20022 vers Lynx, où le rail demeure déterministe et l'agent observateur — est traité au **chapitre 23**. Le présent chapitre en fournit le substrat factuel : les dates, les formats, les statuts. Il ne conclut pas à leur place.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Quatre acquis, datés au 16 juillet 2026. **Premièrement**, Lynx a achevé sa migration ISO 20022 : la coexistence MT/MX a pris fin le 22 novembre 2025, alignée sur l'échéance mondiale SWIFT CBPR+, après une transition de quelque trente-deux mois dont Paiements Canada déclare que plus de 98 % du volume était déjà basculé dès octobre 2025. **Deuxièmement**, le RTR est jalonné et testé — composante compensation et règlement complétée au T3 2025, tests internes au T4 2025, acceptation utilisateur au T1 2026, tests industriels en cours à la mi-2026 selon Paiements Canada — mais il **n'est pas en production**. **Troisièmement**, Paiements Canada **vise** un lancement au T4 2026, à l'issue des tests industriels en cours, avec ISO 20022 dès le lancement et un déploiement graduel se poursuivant en 2027 ; la cible a été **successivement reportée** — 2019, puis 2022, puis 2023, puis 2026 (ce sont les cibles successives, non les dates auxquelles les reports ont été décidés). **Quatrièmement**, le règlement administratif du RTR est publié depuis le 1er juillet 2026 et entre en vigueur le 24 août 2026, soit trente-huit jours avant l'ouverture du trimestre visé — en retenant le trimestre civil, le socle ne fixant pas la convention.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas que le RTR sera lancé au T4 2026 : il dit que Paiements Canada le vise, et que la cible a un historique. Il ne dit pas non plus que le RTR sera reporté — le socle ne porte aucun pronostic, et l'auteur n'en formule aucun. Il ne dit rien du contenu du By-law No. 10, dont seules les dates sont au socle. Il ne dit rien de la richesse informationnelle des messages ISO 20022, que le socle ne documente pas. Il ne dit rien, enfin, de l'usage d'un protocole de paiement agentique sur ces rails : cette question est ouverte, elle est celle du chapitre 16, et elle ne reçoit ici aucune réponse anticipée.

La couche sémantique commune est en place. Elle est une condition de ce qui suit, pas une réponse.

---

## Notes

[^1]: PRD §7.4, **F-28** (niveau [A] — quatre affirmations confirmées par vote adversarial 3-0). Sources primaires : deux pages officielles de payments.ca (Paiements Canada) ; corroboration SWIFT, BNY, J.P. Morgan. Faits repris : adoption complète d'ISO 20022 (messages MX) en novembre 2025 ; fin de la coexistence MT/MX le 22 novembre 2025 (retrait des MT 1xx/2xx au profit de pacs.008/pacs.009), alignée sur l'échéance mondiale SWIFT CBPR+ ; annonce le 26 novembre 2025 ; messages MT hérités plus pris en charge ; coexistence ouverte par la Release 2 de mars 2023 ; plus de 98 % des messages Lynx déjà MX en octobre 2025. Le chiffre de 98 % est une **communication d'opérateur** et est attribué à Paiements Canada à chaque occurrence (§8.2).

[^2]: PRD §7.8, **F-45** (niveau [B]). Sources primaires : payments.ca (pages officielles) ; canada.newsroom.ibm.com. Faits repris : IBM Canada « lead technology partner » de Lynx (annonce du 2 mai 2019 — hébergement, intégration de systèmes, bascule LVTS→Lynx, exploitation ; lancement du 1er septembre 2021 ; centre de données additionnel en octobre 2023) ; partenaire de livraison et d'exploitation du RTR (16 avril 2024, avec CGI et Interac — construction de la composante compensation/règlement et exploitation, « IBM Payments Centre capabilities », citation de Craig Eaket). **Réserves F-45** : les montants des contrats Lynx et RTR ne sont pas publics ; aucun lien n'est documenté entre IBM et les lignes directrices B-13 ou E-23 du BSIF.

[^3]: PRD §8.4, règle de neutralité fournisseur, point (5) : le rôle d'IBM Canada dans Lynx et le RTR est un **fait de contexte, pas un argument de conformité**. Le portefeuille IBM est traité comme cas d'instanciation documenté en Partie VII (ch. 22 à 24), sans valeur de recommandation.

[^4]: PRD §7.4, **F-29** (niveau [A] — neuf affirmations confirmées par vote adversarial 3-0). Sources primaires : payments.ca (quatre pages officielles, page RTR vérifiée le 16 juillet 2026). Faits repris : composante d'échange livrée par Interac en juin 2023 ; reprise du programme le 16 avril 2024 avec IBM Canada et CGI aux côtés d'Interac ; **Deloitte Canada** listé comme quatrième partenaire de livraison, **rôle non détaillé dans la source** ; composante compensation/règlement entamée fin été 2024 et complétée au T3 2025 ; tests internes (SIT) complétés au T4 2025 ; UAT complété au T1 2026 ; tests de performance/sécurité/résilience puis tests industriels (« industry solution assurance testing ») en cours à la mi-2026 ; **système non en production à la mi-juillet 2026** ; cible officielle de lancement au T4 2026 (lancement graduel, déploiement se poursuivant en 2027) avec ISO 20022 dès le lancement ; By-law No. 10 publié à la Gazette du Canada, partie II, le 1er juillet 2026, en vigueur le 24 août 2026 ; aucune source primaire ne mentionne Mastercard ou Vocalink parmi les partenaires actuels. **Réserves F-29** : les jalons sont des **communications d'opérateur** (jalons discrets corroborés par des tiers), attribuées à Paiements Canada à chaque occurrence (§8.2) ; le T4 2026 est une **cible**, pas un fait accompli.

[^5]: PRD §8.1, garde-fou **R-4** — l'affirmation « Paiements Canada n'annonce aucune date de lancement fixe pour le RTR » a été **réfutée 0-3** : la cible T4 2026 est officiellement annoncée. Versant complémentaire, **réserve F-29** : ne jamais écrire « lancé » ni « en production ». Formulation imposée par PRDPlan §4.4 (« cible vs fait accompli »), y compris la précision que 2019, 2022, 2023 et 2026 sont les **cibles successives** et non les dates auxquelles les reports ont été décidés. Formes proscrites : Annexe D §D.7 du glossaire (`monographie/90-annexes/annexe-d-glossaire.md`).

[^6]: PRD §10.5 (lacune ouverte) : aucune source ne documente l'usage d'un protocole de transaction agentique sur les rails de paiement canadiens (RTR, Interac). Périmètre des sources effectivement balayées, énuméré au §15.4 : **F-29** (quatre pages officielles de payments.ca, page RTR revalidée le 16 juillet 2026) et **F-04** (PRD §7.1 — les deux seules sources primaires d'AP2 que le socle porte : annonce Google Cloud du 16 septembre 2025, communiqué de la Linux Foundation du 9 avril 2026). La **spécification d'AP2 n'est pas au socle** (**PRD §10.9e** : aucune structure de message, mandat ni preuve d'intention pour AP2), non plus qu'aucun communiqué d'Interac : ces sources ne sont pas balayées et ne peuvent pas être énumérées comme telles — le ch. 16 (§16.3, Q3) pose la spécification d'AP2 comme ce qui trancherait, précisément parce que le socle ne la porte pas. Question portée par le **chapitre 16** (prospectif) et reprise par renvoi au chapitre 21 — non anticipée ici, conformément à la règle de non-duplication de [TOC.md](../../TOC.md).

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026)
     2. Traçabilité (CA-1, CA-5) . fait (6 notes ; termes anglais entre parenthèses et en italique à la 1re occurrence :
                                   Real-Time Rail, industry solution assurance testing. Sigles repris tels que le socle
                                   les donne — « tests internes (SIT) », F-29 : ne pas développer un sigle que le socle
                                   ne développe pas)
     3. Balayage garde-fous ...... fait. R-4 : la cible T4 2026 est dite officiellement annoncée à chaque occurrence,
                                   jamais « aucune date annoncée ». Réserve F-29 : aucune occurrence de « lancé » ou
                                   « en production » appliquée au RTR au présent — le fait négatif « pas en production
                                   à la mi-juillet 2026 » est posé explicitement (§15.2). §8.2 : les jalons du RTR et le
                                   98 % de Lynx sont attribués à Paiements Canada à chaque occurrence. §8.4 : le rôle
                                   d'IBM Canada est marqué « fait de contexte » aux deux occurrences (§15.1, §15.2) ;
                                   aucune correspondance IBM↔réglementation n'est proposée (R-7 sans objet ici).
                                   R-5 : le motif « standard technique » ne ressort pas — hors périmètre (ch. 14).
                                   R-8 : aucun emploi de « ACP » ni de « control plane » dans ce chapitre.
     4. Relecture adversariale ... FAIT (deux relecteurs indépendants, 16 juillet 2026 — 4 constats bloquants,
                                   12 réserves ; 16/16 vérifiés fondés contre PRD §7.4 / PRDPlan §4.4 / TOC / Annexe D,
                                   16/16 appliqués. Ce que la relecture a réfuté :
                                   — [bloquant] « un dossier qui les citerait encore travaillerait sur un état antérieur
                                     du programme » (Mastercard/Vocalink) : reconstruction rétrospective présupposant une
                                     présence passée que F-29 n'établit pas. Le fait négatif est borné au présent, la
                                     mise en garde marquée « Lecture de l'auteur » (§15.2).
                                   — [bloquant] « La bascule technique n'a pas été choisie isolément » (§15.1) :
                                     affirmation sur le processus de décision ; F-28 n'établit qu'un alignement. Le
                                     chapitre se contredisait six paragraphes plus loin. Réduit à l'alignement.
                                   — [bloquant] libellé d'un principe directeur attribué au ch. 13 (§15.3) : le ch. 13
                                     n'est pas rédigé et TOC lui assigne l'énoncé (§13.4) ; le libellé donné n'était tracé
                                     à aucune entrée. Remplacé par un renvoi simple.
                                   — [bloquant] §15.4 : bijection TOC rompue (la section prévue portait sur la richesse
                                     des données, que F-28/F-29 ne documentent pas). Position du chapitre maintenue —
                                     encadré « Correctif de la rédaction » ajouté ; AMENDEMENT TOC.md DÛ — **exécuté le
                                     17 juill. 2026 (TOC v1.5), voir la passe corrective ci-dessous**.
                                   — [réserves] prémisse du trimestre civil explicitée (T4 2026 → 1er oct., convention non
                                     au socle) ; reliquat < 2 % redaté d'octobre 2025 et l'effet de la date rendu au
                                     paragraphe marqué ; obligation faite aux systèmes amont retirée (F-28 ne l'établit
                                     pas) ; fait négatif IBM borné à E-23/B-13 (PRDPlan §4.4, cas général) ; F-28 et F-29
                                     dissociées dans l'encadré (seule F-28 nomme les types de messages) ; formulation
                                     imposée « cible vs fait accompli » rétablie mot pour mot dans le récapitulatif
                                     (« vise », attribution nominale, glose des cibles successives) ; §15.2 « la cible
                                     officielle prévoit » → « Paiements Canada annonce » (§8.2, à chaque occurrence) ;
                                     « les deux rails canadiens » et « pour la première fois » retirés (non tracés ;
                                     §10.5 nomme Interac comme troisième rail) ; « RTR (Real-Time Rail) » remis dans
                                     l'ordre du glossaire D.5 ; membre « Recherche menée le [date] » ajouté au point (2)
                                     de l'encadré de lacune (PRDPlan §4.4).
                                   Volumétrie après corrections : ~2966 mots de corps (cible 2800, tolérance ±10 %).
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel et publiée
                                   (étiquette mono-v1.0). ⚠ Statut rectifié le 17 juillet 2026 (audit global) : il portait
                                   « À FAIRE » sur une pièce publiée depuis son gel. Défaut systémique — 16 des 29 pièces
                                   le portaient ; l'audit n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
                                   AMENDEMENT TOC.md : **FAIT le 17 juillet 2026 (TOC v1.5)**. L'intitulé de la
                                   section 15.4 y porte désormais « Ce que la couche sémantique commune change pour les
                                   agents » et le correctif y est consigné. La bijection J-2 est rétablie ; la demande que
                                   le présent chapitre portait depuis son gel est honorée et la dette est éteinte.

     6. PASSE CORRECTIVE DE CONFORMITÉ — 17 juillet 2026 (suites de l'audit `audit.md`, constats M-10, M-11, obs. 18).
        AUCUNE information nouvelle : la date de gel reste le 16 juillet 2026, aucun fait n'est ajouté, retiré ni redaté.
          - [M-10, §15.4] SURDÉCLARATION DU PÉRIMÈTRE VÉRIFIÉ, corrigée. L'encadré énumérait comme balayées « pages
            officielles de Paiements Canada, spécification AP2, communiqués Interac ». Or la **spécification d'AP2 n'est
            pas au socle** (F-04 : deux sources primaires seulement — annonce Google Cloud du 16 sept. 2025, communiqué
            LF du 9 avril 2026 ; PRD §10.9e : aucune structure de message, mandat ni preuve d'intention) et **aucun
            communiqué d'Interac n'y figure**. Le ch. 16 (§16.3, Q3) disait déjà correctement « la spécification d'AP2
            elle-même, que le socle ne porte pas » : les deux chapitres se contredisaient. Énumération refaite sur ce que
            le socle porte réellement (F-29 : quatre pages officielles de payments.ca ; F-04 : les deux sources primaires
            d'AP2), et le non-balayé est désormais nommé comme tel. Conclusion (« la question reste ouverte ; aucune
            inférence ») inchangée — elle était juste, et elle l'est à plus juste titre sur un périmètre exact.
            Effets de bord assumés, exigés par CA-1 : **F-04 ajouté à l'en-tête « Socle mobilisé »** (il est désormais
            mobilisé au corps, et un en-tête qui l'ignorerait serait la faute que l'audit relève au ch. 19) ; note [^6]
            complétée du périmètre et du renvoi §10.9e.
          - [M-11, bandeau] DETTE ÉTEINTE. Le bandeau déclarait « L'amendement de TOC.md reste dû » : il l'a été cinq mois,
            il ne l'est plus (TOC v1.5, 17 juill. 2026). Le bandeau porte désormais l'exécution et sa date ; la démonstration
            (F-28/F-29 ne documentent aucun attribut de richesse des données) est conservée intégralement — elle est juste,
            et c'est elle qui explique le titre de la section.
          - [obs. 18, thèse] FUTUR CATÉGORIQUE NON ATTRIBUÉ, retiré. Le bandeau de thèse portait « le RTR **naîtra**
            nativement ISO 20022 » — reproduction fidèle du TOC v1.4, dont la faute était la source : le corps du chapitre
            attribuait correctement à ses trois occurrences (« Paiements Canada annonce », « s'il est lancé… comme
            Paiements Canada le vise »), et le seul énoncé non attribué du chapitre était celui qu'il recopiait du plan.
            La thèse actuelle du TOC v1.5 est reproduite : « Paiements Canada annonce un RTR nativement ISO 20022 dès son
            lancement, visé au T4 2026 ». R-4 et la réserve F-29 sont tenus par le bandeau comme ils l'étaient par le corps.
          - Décomptes re-vérifiés après la passe : 6 notes ([^1] à [^6]), toutes appelées et définies, aucune orpheline ;
            aucun décompte du corps n'est touché par ces corrections (les intervalles de §15.1 à §15.3 sont intacts).
-->

<!-- Relecture adversariale de la passe corrective : DUE avant toute republication (PRDPlan §4.2.4 — relecteur distinct
     du rédacteur de la passe). La présente passe est une correction de conformité au socle, sans apport factuel. -->

