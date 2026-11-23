# 12 Risques, conformité et réglementation

Ce chapitre relie la classe de risque d’un agent aux obligations qui en découlent. Il traduit en exigences vérifiables la Loi 25 et le droit québécois, le cadre fédéral et sectoriel canadien, le règlement européen sur l’IA, le NIST AI RMF et ISO/IEC 42001, puis les réunit dans une matrice de correspondance et un index de preuves unique. Il fixe enfin la transparence due aux personnes, la réponse aux incidents agentiques et une évaluation d’impact unifiée. L’état du droit est celui du 27 octobre 2026.

**ATTENTION**

Ce chapitre résume l’intention des textes; leur application à un cas précis relève des affaires juridiques.

Le principe est simple : on ne bâtit pas un programme de conformité par texte de loi. Chaque agent reçoit une classe de risque, et cette classe déclenche un ensemble de contrôles dont les preuves (traces, journal d’audit, évaluations d’impact, résultats d’évaluation) servent à la fois à la Loi 25, au règlement européen et aux référentiels volontaires. Les seuils, délais internes et fréquences de revue propres au cadre sont signalés comme tels.

## 12.1 Classes de risque des agents

La classe de risque mesure ce qui arrive si l’agent se trompe; elle détermine l’intensité de la gouvernance qui s’applique à lui.

Trois notions coexistent et ne se confondent pas. Le **niveau d’autonomie** (N0 à N4, section 8.1) dit jusqu’où l’agent agit sans approbation. Le **palier d’outil** (P0 à P3, section 8.3) dit ce que fait chaque outil. La **classe de risque** dit quelles conséquences un agent peut produire sur des personnes, sur l’entreprise ou sur des tiers. La classe fixe le plafond du niveau d’autonomie, et le contrôle d’un appel est l’union des contrôles qu’exigent la classe, le niveau et le palier (EXIG-AUT-10).

Cette gradation répond à un constat partagé. Selon Gartner (communiqué du 26 mai 2026), appliquer une gouvernance uniforme à tous les agents mènera à des échecs; l’analyste recommande une gouvernance proportionnelle **[95]**. Le cadre de gouvernance de l’IA agentique de l’Infocomm Media Development Authority (IMDA, Singapour) désigne la portée des actions de l’agent, leur réversibilité et son niveau d’autonomie comme déterminants du risque **[76]**. La ligne directrice E-23 du BSIF suit la même logique pour les modèles : une cote de risque détermine l’intensité de la gouvernance, la fréquence des examens et l’autorité d’approbation **[8]**. Les quatre critères d’analyse du cadre qui fixent le niveau d’autonomie sous le plafond de la classe (rayon d’impact, réversibilité, délai de détection et de récupération, observabilité reconstructive) sont décrits à la section 8.2; ce ne sont pas les critères du tableau 46.

*Tableau 46 — Classes de risque des agents : critères, plafond d’autonomie et contrôles minimaux*

| **Classe** | **Critères (un seul suffit)** | **Plafond d’autonomie** | **Contrôles minimaux** | **Revue** |
| --- | --- | --- | --- | --- |
| **Élevée** | Décision à effet important sur une personne (crédit, emploi, assurance, accès à un service essentiel); décision fondée exclusivement sur un traitement automatisé de RP (art. 12.1 de la Loi sur le privé; art. 65.2 de la Loi sur l’accès pour les organismes publics); système à haut risque au sens du règlement européen sur l’IA; action financière, juridique ou irréversible au-delà des seuils de classe que la fonction risques et conformité arrête pour l’agent (EXIG-CON-01), distincts du seuil d’exécution autonome d’un outil; renseignements personnels sensibles | N2 | EFVP si l’agent traite des RP (EXIG-CON-04) et évaluation d’impact unifiée (section 12.9); équipe rouge avant production (section 9.9); homologation par le comité d’architecture et des risques agentiques; P3 approuvé par deux approbateurs distincts, dont au moins un n’est pas le mandant (EXIG-AUT-15), hors bande comme pour toute classe (EXIG-AUT-09) | Semestrielle |
| **Modérée** | RP non sensibles ou données confidentielles; actions P2 réversibles ou compensables en production; échanges avec des partenaires, des clients ou le public | N3, avec des seuils plus bas et une revue a posteriori renforcée | EFVP si l’agent traite des RP (EXIG-CON-04); volet impact algorithmique si l’agent décide ou recommande à l’égard d’une personne (EXIG-CON-26); revue de sécurité; exercice d’équipe rouge avant production puis annuel (EXIG-SEC-23); évaluation continue (section 10.4) | Annuelle |
| **Faible** | Données publiques ou internes non confidentielles (aucun RP, aucun tiers); lecture seule ou actions internes réversibles bornées au domaine de l’agent; aucun effet sur une personne | N3; N4 sur décision du comité | Autoévaluation documentée; évaluation continue; inscription au registre | Annuelle |

Plafonds repris de l’EXIG-CON-02, qui fait foi. Choix du cadre. Les fréquences de revue sont des valeurs par défaut que la déclaration de tolérance au risque peut resserrer (EXIG-CON-17).

Un seul critère suffit : la classe retenue est la plus élevée dont un critère est rempli, jamais une moyenne. Les conséquences ne se compensent pas : un agent en lecture seule qui consulte des dossiers médicaux reste de classe élevée, parce qu’une fuite ne se répare pas.

**EXEMPLE**

Un agent de préqualification de prêts personnels lit des données et produit un avis « admissible » ou « non admissible ». Si cet avis est communiqué au client sans examen réel par un employé, il s’agit d’une décision fondée exclusivement sur un traitement automatisé : l’agent est de classe élevée et plafonné à N2, alors que tous ses outils sont de palier P1. La classe s’apprécie au niveau d’autonomie demandé et au pire cas de supervision (EXIG-CON-01). À l’inverse, un agent qui reclasse des billets d’assistance internes en écriture réversible (P2), sans RP, relève de la classe modérée et peut atteindre N3 sous des seuils déclarés.

`EXIG-CON-01` **· DOIT**

**Classe de risque attribuée avant l’inscription**

Chaque agent **DOIT** recevoir une classe de risque (faible, modérée ou élevée) selon le tableau 46, attribuée par la fonction risques et conformité avant son inscription au registre (section 11.4) : la fiche est inscrite à l’état « proposé » avec sa classe approuvée. La classe s’évalue sur l’autonomie maximale envisagée et sur le parcours de décision déclaré, avant tout plafonnement; le critère de décision fondée exclusivement sur un traitement automatisé s’apprécie au niveau d’autonomie demandé et au pire cas de supervision. Une classe élevée retenue à ce titre ne redescend qu’après que les mesures de l’EXIG-AUT-21 ont établi une révision humaine significative (EXIG-CON-08) pendant au moins un trimestre. Un niveau demandé au-delà du plafond de l’EXIG-CON-02 est refusé. La classe retenue est la plus élevée dont au moins un critère est rempli; la justification est consignée dans la fiche d’agent.

Pourquoi : une moyenne des critères masquerait la conséquence la plus grave, qui seule commande les contrôles.

`EXIG-CON-02` **· DOIT**

**Plafond d’autonomie par classe**

Le niveau d’autonomie déclaré au registre **DOIT** respecter le plafond de la classe : N2 pour la classe élevée, N3 pour les classes modérée et faible. N4 n’est permis qu’à un agent de classe faible, sur décision consignée du comité d’architecture et des risques agentiques. Un agent **NE DOIT PAS** opérer au niveau NX, quelle que soit sa classe. La présente exigence est la seule source des plafonds par classe; la section 8.1, le tableau 46 et l’EXIG-GOV-17 y renvoient.

Pourquoi : les plafonds par classe sont un choix du cadre; pour les systèmes à haut risque, le règlement européen exige des mesures de supervision humaine proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation (art. 14(3)) **[412]**.

`EXIG-CON-03` **· DOIT**

**Réévaluation à chaque changement significatif**

La classe de risque **DOIT** être réévaluée, avant la mise en service du changement, à chaque déclencheur de l’EXIG-GOV-12, qui en tient la seule liste; cette liste couvre les modifications d’un modèle et de ses données qu’E-23 tient pour importantes. La même réévaluation déclenche la mise à jour de l’EFVP et de l’évaluation d’impact unifiée (EXIG-CON-26).

Pourquoi : le guide de la Commission d’accès à l’information (CAI) demande de mettre à jour une EFVP lorsque le projet change, et E-23 fait des modifications d’un modèle et de ses données un déclencheur de revue indépendante **[8, 413]**.

## 12.2 Loi 25 et droit québécois

Cette section traduit en exigences les obligations québécoises qui touchent directement les agents : évaluation préalable, communication hors Québec, consentement, décisions automatisées, conservation, secteur public et sanctions.

La *Loi modernisant des dispositions législatives en matière de protection des renseignements personnels* (L.Q. 2021, c. 25, « Loi 25 ») a été sanctionnée le 22 septembre 2021. Elle est entrée en vigueur par étapes : le 22 septembre 2022 pour le responsable de la protection des renseignements personnels (RPRP) et les incidents de confidentialité **[56]**, le 22 septembre 2023 pour l’essentiel **[56]**, et le 22 septembre 2024 pour le droit à la portabilité (quelques dispositions accessoires l’étant dès le 22 septembre 2021) **[7, 56]**. Elle modifie la *Loi sur la protection des renseignements personnels dans le secteur privé* (RLRQ, c. P-39.1, « Loi sur le privé ») et la *Loi sur l’accès aux documents des organismes publics et sur la protection des renseignements personnels* (RLRQ, c. A-2.1, « Loi sur l’accès »). Sauf mention contraire, les articles cités sont ceux de la Loi sur le privé.

Un point de départ s’impose : l’entreprise demeure responsable des RP qu’elle détient, même lorsqu’un fournisseur de modèles, de plateforme d’agents ou de serveur MCP les conserve ou les traite pour elle (art. 1 et 3.1) **[56]**; selon la CAI, elle conserve aussi ses obligations en cas d’incident **[414]**. La loi ne connaît pas de responsabilité « conjointe » : le fournisseur est un mandataire lié par un contrat écrit (art. 18.3) **[56]** (tableau 47).

*Tableau 47 — Articles de la Loi sur le privé qui touchent les agents*

| **Article** | **Obligation (résumé)** | **Application aux agents (interprétation du cadre)** |
| --- | --- | --- |
| 3.1 | La personne ayant la plus haute autorité exerce la fonction de responsable de la protection des RP, délégable par écrit; titre et coordonnées publiés sur le site Web. | Le responsable est consulté sur chaque agent qui traite des RP et participe à l’homologation des agents de classe élevée (section 11.1). |
| 3.2 | Politiques et pratiques de gouvernance (conservation, destruction, rôles, plaintes) approuvées par le responsable; information publiée en termes simples et clairs. | Les règles de conservation des traces et des mémoires d’agents font partie de ces politiques. |
| 3.3 | EFVP pour tout projet d’acquisition, de développement ou de refonte d’un système d’information ou de prestation électronique de services impliquant des RP; responsable consulté dès le début; portabilité permise. | Tout nouvel agent, et tout changement de modèle ou d’outils touchant des RP (EXIG-CON-03 et EXIG-CON-04). |
| 3.5 à 3.8 | Incidents de confidentialité : mesures pour diminuer le risque; avis « avec diligence » à la CAI et aux personnes en cas de risque de préjudice sérieux; registre de tous les incidents. | Réponse aux incidents agentiques (section 12.8). |
| 8.1 | Informer au préalable du recours à une technologie permettant d’identifier, de localiser ou de profiler une personne, et des moyens d’activer ces fonctions. | Un agent qui évalue le rendement au travail, la situation économique, la santé, les préférences ou le comportement d’une personne fait du profilage. |
| 9.1 | Produit ou service technologique offert au public et doté de paramètres de confidentialité : plus haut niveau de confidentialité par défaut. | Mémoire persistante, partage de conversations et personnalisation désactivés par défaut dans les agents offerts au public. |
| 11 | RP à jour et exacts au moment d’une décision; conservés au moins un an après celle-ci. | Conservation des éléments de décision au dossier de décision (EXIG-CON-09, EXIG-OBS-11). |
| 12 | Utilisation limitée aux fins de la collecte, sauf consentement (exprès s’il est sensible) ou exception prévue; la prospection commerciale ou philanthropique n’est pas une fin compatible. | Aucune réutilisation de conversations ou de traces à d’autres fins sans base légale documentée (EXIG-CON-06). |
| 12.1 | Décision fondée exclusivement sur un traitement automatisé : informer, expliquer sur demande, permettre la rectification et des observations à un membre du personnel en mesure de réviser la décision. | EXIG-CON-07, EXIG-CON-08 et EXIG-CON-21. |
| 28 et 28.1 | Rectification d’un renseignement inexact, incomplet ou équivoque, ou dont la collecte, la communication ou la conservation n’est pas autorisée (art. 28); cessation de la diffusion ou désindexation, aux conditions de l’art. 28.1. | La rectification ou la suppression atteint chaque mémoire, index, cache et dossier de décision de l’agent (EXIG-CON-10). |
| 14 | Consentement manifeste, libre, éclairé, donné à des fins spécifiques et demandé pour chacune d’elles, en termes simples et clairs; présenté distinctement s’il est demandé par écrit. | Fin principale (inférence nécessaire au service demandé) et fins secondaires (entraînement, ajustement) distinguées; seules les secondes exigent un consentement distinct ou une autre exception documentée. |
| 17 | Avant toute communication hors Québec : EFVP tenant compte de la sensibilité, de la finalité, des mesures de protection et du régime juridique de l’État de destination; protection adéquate; entente écrite. | Tout modèle, serveur MCP, agent délégataire ou magasin de mémoire situé hors Québec (EXIG-CON-05). |
| 18.3 | Mandat ou contrat de service écrit : mesures de confidentialité, usage limité au mandat, aucune conservation après l’expiration, avis sans délai de toute violation, droit de vérification. | Clauses fournisseurs (section 13.3), dont l’interdiction d’entraîner des modèles sur les données confiées. |
| 23 | Destruction ou anonymisation une fois les fins accomplies, selon le Règlement sur l’anonymisation; un renseignement dépersonnalisé demeure un RP. | Cycle de vie des mémoires et des index vectoriels (EXIG-CON-10). |
| 27 et 32 | Accès et copie; transcription écrite et intelligible; depuis le 22 septembre 2024, portabilité des renseignements informatisés recueillis auprès de la personne; réponse écrite au plus tard dans les 30 jours. | Les inférences produites par un agent sont visées par le droit d’accès, mais pas par la portabilité. |
| 90.1 et suiv., 91, 93.1 | Sanctions administratives pécuniaires, infractions pénales, dommages-intérêts punitifs. | Voir « Sanctions et recours » ci-dessous. |

Source des obligations : Loi sur le privé (RLRQ, c. P-39.1), modifiée par la L.Q. 2021, c. 25 **[56]**; les obligations sont relevées dans la loi modificative, et le texte consolidé n’a pas été relu pour le présent cadre. La colonne de droite est une interprétation du cadre.

### Évaluation des facteurs relatifs à la vie privée

L’EFVP est obligatoire dans deux situations qui visent directement les agents : tout projet d’acquisition, de développement ou de refonte d’un système d’information ou de prestation électronique de services impliquant des RP (art. 3.3), et toute communication de RP à l’extérieur du Québec (art. 17) **[413]**. Elle ne vise donc pas « tout système » en exploitation, mais tout projet qui en crée ou en modifie un. La loi exige qu’elle soit proportionnée à la sensibilité, à la finalité, à la quantité, à la répartition et au support des renseignements, sans prescrire de forme ni de signature **[56]**. Le guide de la CAI (version 3.1, avril 2024) est recommandé : il prévoit une évaluation de la conformité, une analyse des risques avec stratégies d’atténuation, un inventaire et un « parcours » des renseignements, puis une réévaluation de la nécessité et de la proportionnalité; il cite « améliorer un modèle d’intelligence artificielle » et « rendre une décision automatisée » parmi les finalités à examiner **[413]**.

Pour un agent, le parcours des renseignements est plus long que pour une application classique : invite, contexte récupéré, appels d’outils MCP, délégations A2A, mémoire, traces. L’EFVP du cadre inventorie donc les RP outil par outil et délégation par délégation. La loi n’exige pas d’évaluer les biais dans l’EFVP; le cadre l’exige pour tout agent qui décide ou recommande à l’égard d’une personne, dans le prolongement de la recommandation de la CAI (dès 2020) d’imposer, pour les systèmes de décision automatisée, une EFVP et une analyse d’impact algorithmique couvrant tous les droits fondamentaux, et de celle du gouvernement du Québec pour les décisions automatisées **[318, 415]**.

`EXIG-CON-04` **· DOIT**

**EFVP avant tout projet d’agent impliquant des RP**

Tout projet d’acquisition, de développement ou de refonte d’un agent impliquant des RP **DOIT** faire l’objet d’une EFVP terminée avant le passage en pilote. Le responsable de la protection des RP **DOIT** être consulté dès le début du projet. L’EFVP **DOIT** inventorier les RP par outil, par délégation et par mémoire, et, lorsque l’agent décide ou recommande à l’égard d’une personne, **DOIT** y joindre le volet impact algorithmique de l’EXIG-CON-26, dont l’analyse des biais tient lieu d’analyse des biais de l’EFVP (exigence propre au cadre).

Pourquoi : article 3.3 de la Loi sur le privé, qui ne prescrit pas le contenu de l’EFVP; l’analyse des biais est une exigence propre au cadre, appuyée par les orientations de la CAI (discrimination parmi les conséquences à évaluer; analyse d’impact algorithmique recommandée au législateur), non une obligation légale **[56, 413, 415]**.

### Communication hors Québec et lois étrangères

Confier à un fournisseur situé hors Québec la tâche d’utiliser ou de conserver des RP pour le compte de l’entreprise, par exemple en appelant l’API d’un modèle hébergé ailleurs, relève de l’article 17. L’entreprise réalise d’abord une EFVP qui tient compte de la sensibilité des renseignements, de la finalité, des mesures de protection, y compris contractuelles, et du régime juridique de l’État de destination. La communication est permise si les renseignements bénéficient d’une protection adéquate, et elle fait l’objet d’une entente écrite **[56, 416]**. Le texte de l’article 17 vise toute communication à l’extérieur du Québec et ne distingue pas les provinces; un index vectoriel hébergé dans une région infonuagique en Ontario déclenche donc l’article 17 au même titre qu’un hébergement aux États-Unis : toute zone hors du Québec en relève **[56, 416]**.

La résidence des données ne règle pas tout. Le CLOUD Act américain (2018) oblige, sur réquisition légale, les fournisseurs assujettis au droit américain à préserver et à divulguer les données en leur possession, sous leur garde ou sous leur contrôle, qu’elles soient situées aux États-Unis ou à l’étranger **[417]**. Le cadre fédéral de souveraineté numérique (novembre 2025) constate que le stockage au Canada ne place pas à lui seul les données hors de la compétence de tribunaux étrangers, tout en notant que le gouvernement du Canada n’a relevé aucun cas documenté de gouvernement étranger cherchant à accéder aux données d’entreprises canadiennes détenues par des fournisseurs **[418]**. Le risque est donc réel, mais à pondérer dans l’EFVP. Le cadre retient comme mesures compensatoires le chiffrement à clés tenues hors de portée du fournisseur (gestion externe des clés), une conservation nulle, ou bornée et déclarée, des invites et des sorties chez le fournisseur (EXIG-APP-10) et, pour les RP sensibles, le recours à des fournisseurs sous compétence canadienne. Le chiffrement au repos ne protège pas les données en cours d’inférence, que le modèle traite en clair; le calcul confidentiel attesté est une option à évaluer dans l’EFVP.

`EXIG-CON-05` **· DOIT**

**Cartographie des lieux de traitement**

La fiche de chaque agent **DOIT** indiquer le lieu de traitement (province ou pays, région et fournisseur) de chaque modèle appelé, serveur MCP, agent délégataire et magasin de mémoire ou de traces, en précisant si le point d’accès peut traiter hors de la région déclarée (point d’accès mondial ou interrégional). Tout flux de RP vers l’extérieur du Québec, y compris vers une autre province, **DOIT** être couvert par une EFVP au sens de l’article 17 et par une entente écrite avant sa mise en service. Pour tout agent autorisé à traiter des RP, la localisation s’applique sur les trois chemins, par route déclarée au catalogue et non par analyse du contenu : la passerelle de modèles (inférence), la passerelle d’agents (appels MCP et délégations A2A) et le plan mémoire et les index **DOIVENT** refuser toute route vers l’extérieur du Québec qui n’est pas couverte.

Pourquoi : l’article 17 vise toute communication « à l’extérieur du Québec », autres provinces comprises, et un routage dynamique entre modèles peut créer un transfert que personne n’a décidé **[56, 416]**.

### Consentement et finalités

Un RP ne peut servir qu’aux fins pour lesquelles il a été recueilli, sauf consentement (exprès s’il est sensible) ou exception prévue par la loi : fins compatibles ayant un lien pertinent et direct avec les fins initiales, bénéfice manifeste de la personne, prévention de la fraude, fourniture d’un service demandé, recherche ou statistiques avec des renseignements dépersonnalisés. La prospection commerciale ou philanthropique n’est jamais une fin compatible (art. 12) **[56]**. Le consentement doit être manifeste, libre, éclairé et donné à des fins spécifiques; il est demandé pour chacune de ces fins, en termes simples et clairs (art. 14) **[56, 419]**. La loi n’emploie pas la notion de consentement « groupé », mais l’exigence d’un consentement par finalité conduit le cadre à distinguer la fin principale, l’inférence nécessaire au service demandé, qui relève de l’exception « fourniture d’un service demandé » ou du consentement initial, des fins secondaires (entraînement ou ajustement fin de modèles), qui exigent un consentement distinct ou une autre exception documentée.

`EXIG-CON-06` **· DOIT**

**Finalité vérifiée avant toute réutilisation**

Toute réutilisation de conversations, de traces, de mémoires ou de sorties d’agents à une autre fin que celle de la collecte, notamment l’entraînement ou l’ajustement fin de modèles, **DOIT** reposer sur un consentement distinct ou sur une exception légale documentée. Les données **DOIVENT** porter une étiquette de finalité, vérifiée aux points de sortie des magasins (API d’export des traces, des mémoires et des conversations; chaînes d’entraînement et d’ajustement) par la plateforme de données; la passerelle d’agents la vérifie pour les seuls flux agentiques (section 9.4). Un modèle ou un adaptateur ajusté sur des RP est un magasin dérivé : il est inscrit à la fiche, soumis à l’EXIG-CON-10 (durée de vie; réentraînement ou destruction à l’échéance ou au retrait du consentement) et à un test d’extraction lors de l’exercice d’équipe rouge (EXIG-SEC-23).

Pourquoi : articles 12 et 14 de la Loi sur le privé; un contrôle technique empêche qu’une équipe réutilise de bonne foi des traces pour une fin non couverte.

### Décisions fondées exclusivement sur un traitement automatisé

L’article 12.1 s’applique lorsqu’une décision concernant une personne est fondée exclusivement sur un traitement automatisé de ses RP. L’entreprise doit l’en informer au plus tard au moment où elle l’informe de la décision. À sa demande, elle doit aussi l’informer des RP utilisés, des raisons et des principaux facteurs et paramètres ayant mené à la décision, ainsi que de son droit de faire rectifier ces renseignements. La personne doit avoir l’occasion de présenter ses observations à un membre du personnel en mesure de réviser la décision **[56]**. Le défaut d’informer la personne ou de lui permettre de présenter ses observations est expressément un motif de sanction administrative pécuniaire (art. 90.1, par. 5°) **[56, 317]**.

Quand une décision est-elle « exclusivement » automatisée? Selon l’interprétation du gouvernement du Québec pour l’article 65.2 de la Loi sur l’accès, rédigé comme l’article 12.1 et que le cadre transpose par analogie à ce dernier, c’est le cas lorsqu’aucune personne physique n’a exercé un contrôle important. Une intervention humaine mineure, sans effet réel sur le résultat, ne fait pas échapper à l’obligation; en revanche, un outil d’aide à la décision qui fournit des éléments à un employé qui décide lui-même n’est pas visé **[318]**. Pour un agent de niveau N2, la conséquence est concrète : un bouton « Approuver » cliqué sans information, sans temps et sans autorité réelle ne transforme pas la décision de l’agent en décision humaine. Le même document précise qu’il n’est pas requis de divulguer l’algorithme : le mot « principaux » limite l’explication aux facteurs et paramètres déterminants, ce qui protège les renseignements industriels et commerciaux.

**DROIT APPLICABLE**

Article 12.1 de la Loi sur le privé (article 65.2 de la Loi sur l’accès pour les organismes publics) : avis au plus tard au moment où la personne est informée de la décision; sur demande, RP utilisés, raisons, principaux facteurs et paramètres, droit de rectification; observations à un membre du personnel en mesure de réviser. L’article 12.1 ne fixe aucun délai de réponse : le délai de 30 jours de l’article 32 vise les demandes d’accès et de rectification. Les RP utilisés pour décider sont conservés au moins un an après la décision (art. 11) **[56]**.

`EXIG-CON-07` **· DOIT**

**Avis et explication des décisions automatisées**

Pour toute décision concernant une personne fondée exclusivement sur le traitement automatisé de ses RP par un agent, le système **DOIT** : informer la personne au plus tard au moment où la décision lui est communiquée; pouvoir produire sur demande, à partir du dossier de décision (EXIG-OBS-11), les RP utilisés, les raisons et les principaux facteurs et paramètres ayant mené à la décision; indiquer le droit de rectification; offrir un canal pour présenter des observations à un membre du personnel en mesure de réviser la décision, rôle désigné doté d’un titulaire et d’un suppléant et dimensionné selon le volume des décisions. Les principaux facteurs et paramètres s’établissent à partir des facteurs déterministes du processus : la décision est rendue, ou bornée, par une règle ou un modèle de pointage versionné qui consigne ses facteurs au dossier de décision, et jamais établie à partir du raisonnement affiché du modèle; un agent dont la décision n’est ni rendue ni bornée ainsi **NE DOIT PAS** rendre ces décisions. Le délai de réponse aux observations **DOIT** être d’au plus 30 jours (choix du cadre; l’article 12.1 ne fixe aucun délai). La présente exigence est la seule source des obligations envers la personne au titre de l’article 12.1 de la Loi sur le privé et de l’article 65.2 de la Loi sur l’accès; l’EXIG-AUT-22 et l’EXIG-CON-21 y renvoient.

Pourquoi : article 12.1; le défaut constitue un motif de sanction administrative pécuniaire **[56, 317]**.

`EXIG-CON-08` **· NE DOIT PAS**

**Aucune approbation nominale**

Une approbation humaine **NE DOIT PAS** être considérée comme retirant le caractère exclusivement automatisé d’une décision si l’approbateur ne réunit pas les quatre conditions suivantes : l’autorité de modifier ou d’annuler la décision; la compétence pour l’examiner; l’accès à toutes les données pertinentes, et non à la seule recommandation de l’agent; le temps nécessaire pour l’examiner. La qualification se fait a priori, à l’EFVP et à la fiche, et une décision est réputée exclusivement automatisée tant que ces conditions ne sont pas établies. Le taux d’approbation sans modification est suivi en permanence, par approbateur (EXIG-AUT-21, section 8.7); une mesure qui révèle une approbation nominale requalifie la décision, et les obligations de l’EXIG-CON-07 s’appliquent. La présente exigence est la seule source de ce test; l’EXIG-AUT-23 y renvoie.

Pourquoi : selon l’interprétation gouvernementale, une intervention humaine mineure, sans effet réel sur le résultat, ne fait pas échapper à l’obligation **[318]**.

`EXIG-CON-09` **· DOIT**

**Conservation des éléments de décision**

Les éléments de toute décision d’agent touchant une personne **DOIVENT** être conservés au moins un an après la décision, sous une forme qui permet de répondre aux demandes prévues aux articles 12.1 et 27 : RP en entrée, résultats d’outils qui ont servi à décider, versions de l’agent, du modèle et des outils, facteurs retenus et approbations. Le dossier de décision (EXIG-OBS-11) en est la source, et non les traces ni le journal d’audit, qui ne portent ni le contenu ni les résultats d’outils; la personne reçoit une transcription écrite et intelligible.

Pourquoi : l’article 11, dans la lecture qu’en fait le cadre d’après la loi modificative (sans relecture du texte consolidé), exige de conserver au moins un an les RP utilisés pour décider; la conservation des versions et des facteurs va au-delà du minimum légal pour rendre l’explication possible **[56]**.

### Conservation, mémoire et destruction

Une fois les fins accomplies, l’entreprise doit détruire le renseignement ou l’anonymiser pour des fins sérieuses et légitimes, selon les critères du Règlement sur l’anonymisation des renseignements personnels (art. 23); un renseignement dépersonnalisé, notion définie à l’article 12, demeure un renseignement personnel. La CAI estime en outre que certaines données, dont les données génétiques, biométriques et de géolocalisation, ne peuvent être adéquatement anonymisées **[56, 420]**. Pour un agent, la règle vise la mémoire épisodique et sémantique (section 5.5), les index vectoriels et les traces. Un plongement vectoriel *(embedding)* calculé à partir d’un RP n’est pas anonyme du seul fait qu’il est illisible pour un humain : le cadre le traite comme un RP.

`EXIG-CON-10` **· DOIT**

**Durée de vie des mémoires et des traces**

Chaque magasin de mémoire, index vectoriel, dépôt de traces, historique d’exécution durable, journal de saga, sujet d’événements, dossier de décision et modèle ou adaptateur ajusté sur des RP (EXIG-CON-06) d’un agent **DOIT** avoir une durée de conservation liée à sa finalité, inscrite dans la fiche d’agent et appliquée automatiquement. Cette durée respecte les minimums suivants, dont le plus long l’emporte quand plusieurs s’appliquent : traces d’un agent à haut risque au sens du RIA, six mois (art. 26); journal d’audit, 24 mois (EXIG-OBS-13); journal d’exécution des bacs à sable, 24 mois (EXIG-SEC-16, choix du cadre); dossier de décision, un an après la décision (EXIG-CON-09, EXIG-OBS-11); registre des incidents de confidentialité, cinq ans (EXIG-CON-24); captures de débogage, 14 jours au plus (EXIG-OBS-08); dépôt d’évaluation, durée bornée à la fiche, 30 jours par défaut (EXIG-EVA-04). À l’échéance, sous réserve du gel des preuves d’un incident (EXIG-CON-23) et de toute conservation pour litige notifiée, les données **DOIVENT** être détruites ou anonymisées selon le règlement; les plongements calculés à partir de RP suivent le même régime que les RP d’origine. Une demande de rectification ou de suppression (art. 28) **DOIT** atteindre, dans le délai de l’article 32, chaque mémoire, index, cache et dossier de décision inscrits à la fiche, avec une suppression physique vérifiable (compactage ou reconstruction de l’index); les données sous gel sont marquées et exclues de toute nouvelle décision.

Pourquoi : article 23 de la Loi sur le privé; une mémoire sans échéance accumule des RP au-delà de leur finalité.

### Secteur public québécois

Les organismes publics appliquent les dispositions équivalentes de la Loi sur l’accès : décisions fondées exclusivement sur un traitement automatisé (art. 65.2), EFVP (art. 63.5), règles de gouvernance (art. 63.3), incidents de confidentialité (art. 63.8 à 63.11) et communication hors Québec (art. 70.1); l’article 63.1 porte sur les mesures de sécurité **[56, 318]**. Trois textes gouvernementaux s’y ajoutent :

- l’indication d’application IA-RI-2025-003-OP sur l’IA générative, en vigueur le 5 décembre 2025, exige notamment une EFVP dès la conception de tout système d’IA générative, même sans RP apparent, la classification préalable des données numériques gouvernementales, des essais de fiabilité, une supervision humaine proportionnée à l’autonomie, l’interdiction d’entrer des renseignements confidentiels dans un système d’IA générative public et, pour les données confidentielles, la préférence pour des fournisseurs québécois ou canadiens hébergés au Québec ou au Canada **[421]**;
- l’Énoncé de principes pour une utilisation responsable de l’IA par les organismes publics (édition 2025) compte 12 principes; le principe 11 vise expressément l’IA agentique et exige des mécanismes permettant la validation, l’intervention humaine ou l’arrêt des actions du système, par exemple des validations avant certaines actions critiques et des mécanismes d’arrêt d’urgence **[379]**;

- l’Énoncé de politique de souveraineté numérique et d’approvisionnement en TI (février 2026) oriente l’État vers l’hébergement souverain, des centres de données relevant de la compétence du Québec et le logiciel libre **[422]**.

L’indication d’application et l’Énoncé de principes lient les organismes publics; l’énoncé de politique de souveraineté numérique énonce une orientation de l’État. Pour les entreprises privées, le cadre les retient comme référence de bonne pratique. Le gouvernement met aussi à la disposition des organismes des outils officiels : analyse des décisions automatisées, modèle de registre des incidents, analyse du régime juridique d’une communication hors Québec et schéma de décision sur l’EFVP **[423]**. Ils constituent de bons points de départ pour les gabarits du cadre.

### Sanctions et recours

La CAI peut imposer une sanction administrative pécuniaire d’au plus 50 000 $ à une personne physique et, à une entreprise, d’au plus 10 000 000 $ ou 2 % du chiffre d’affaires mondial de l’exercice précédent, selon le montant le plus élevé (art. 90.12) **[56]**; un engagement accepté par la CAI et respecté écarte la sanction **[317]**. Les infractions pénales (art. 91) entraînent une amende de 5 000 $ à 100 000 $ pour une personne physique et, pour une entreprise, de 15 000 $ à 25 000 000 $ ou 4 % du chiffre d’affaires mondial, selon le montant le plus élevé; les amendes sont portées au double en cas de récidive (art. 92.1). Une atteinte illicite intentionnelle ou résultant d’une faute lourde donne en outre droit à des dommages-intérêts punitifs d’au moins 1 000 $ (art. 93.1) **[56]**. La page des sanctions de la CAI et son rapport annuel 2024-2025 ne font état d’aucune sanction liée aux décisions automatisées : le risque tient aux plafonds légaux, non à des précédents **[424]**.

Le droit évolue. Dans son rapport quinquennal déposé le 11 juin 2026, la CAI formule 74 recommandations, dont une meilleure prise en compte des inférences algorithmiques et une meilleure définition du processus d’EFVP **[425]**. Le cadre traite dès maintenant les inférences produites par les agents comme des RP à gouverner.

## 12.3 Cadre fédéral et sectoriel canadien

Cette section situe les obligations fédérales et sectorielles qui s’ajoutent au droit québécois, et distingue ce qui est en vigueur de ce qui n’est encore qu’un projet (tableau 48).

*Tableau 48 — Textes fédéraux et sectoriels canadiens : statut au 27 octobre 2026 et effet sur les agents*

| **Texte** | **Statut** | **Ce qu’il implique pour les agents** |
| --- | --- | --- |
| LPRPDE (Loi sur la protection des renseignements personnels et les documents électroniques) | En vigueur | Atteinte présentant un risque réel de préjudice grave : déclaration au Commissariat et avis aux personnes « le plus tôt possible » (LPRPDE, par. 10.1(2) et (6)); toutes les atteintes sont consignées, registre conservé 24 mois **[426, 427]**. |
| Projet de loi C-27, dont la Loi sur l’intelligence artificielle et les données (LIAD) | Resté à l’étape du comité à la fin de la session, le 6 janvier 2025; mort au Feuilleton à la prorogation **[428, 429]** | Aucune obligation : la LIAD n’existe pas. |
| Projet de loi C-36, Loi sur la protection de la vie privée et des données des consommateurs | Déposé et lu une première fois le 15 juin 2026; à l’étape de la deuxième lecture; non en vigueur **[430]** | Viserait tout système décisionnel automatisé qui appuie ou remplace le jugement humain; lorsqu’il sert à faire des prédictions, des recommandations ou des décisions pouvant avoir un effet juridique ou un effet important semblable : usage décrit dans l’information rendue publique (art. 62), explication sur demande et observations écrites à un employé pouvant réviser (art. 63). Les sanctions administratives (art. 113 et 114) ne visent que certaines dispositions, dont l’art. 62(1) mais pas l’art. 63; le plafond est le plus élevé de 10 M$ et de 3 % des revenus mondiaux bruts **[431]**. |
| Directive sur la prise de décisions automatisée du Secrétariat du Conseil du Trésor du Canada (SCT) et évaluation de l’incidence algorithmique (EIA) | S’applique à l’administration fédérale | Systèmes développés ou acquis après le 1er avril 2020 qui remplacent ou appuient le jugement humain dans des décisions administratives; EIA obligatoire (65 questions de risque, 41 d’atténuation, niveaux d’incidence I à IV), faite au début de la conception, mise à jour avant la production, résultats publiés **[432, 433]**. |
| Guide sur l’utilisation de l’IA agentique (gouvernement du Canada, 2026) | Orientation pour l’administration fédérale | Autonomie bornée, lecture seule par défaut, points de contrôle humains pour les actions qui modifient l’état des systèmes, propriétaire humain désigné, identifiant unique par agent, journalisation dans un système que l’agent ne peut modifier, coupe-circuit externe, texte externe traité comme des données **[353]**. |
| Ligne directrice E-23 du BSIF, Gestion du risque de modèle | Publiée le 11 septembre 2025; en vigueur le 1er mai 2027 pour les institutions financières fédérales **[8]** | « Modèle » inclut les méthodes d’IA et d’apprentissage automatique (la prise de décision autonome relève des principes de surveillance); inventaire d’entreprise des modèles à risque non négligeable, y compris ceux des fournisseurs, cote de risque, revue indépendante, surveillance de la dérive. |
| Avis du BSIF sur le signalement des incidents liés à la technologie et à la cybersécurité | En vigueur depuis le 13 août 2021 **[434]** | Signalement écrit au BSIF dans les 24 heures, ou plus tôt si possible. |
| Ligne directrice B-13 du BSIF, Gestion des risques liés à la technologie et au cyberrisque | Publiée en juillet 2022 (lettre du BSIF du 13 juillet 2022); en vigueur depuis le 1er janvier 2024 **[435, 436]** | Gestion des identités et des accès fondée sur le risque (authentification multifacteur, accès privilégiés, moindre privilège, attestation périodique, surveillance des comptes de service); journalisation continue et centralisée; incidents d’origine tierce visés. |
| Code de conduite volontaire sur l’IA générative avancée (Innovation, Sciences et Développement économique Canada, ISDE) | Septembre 2023; volontaire **[437]** | Six résultats : responsabilisation, sécurité, justice et équité, transparence, surveillance humaine, validité et robustesse. |
| Principes des commissaires à la protection de la vie privée pour une IA générative responsable | 7 décembre 2023, cosignés par la CAI **[438]** | Neuf principes; menaces propres à l’IA (injection, inversion de modèle, débridage); mécanisme de contestation avec révision humaine pour les décisions assistées par l’IA. |

Trois conséquences pratiques en découlent. D’abord, une institution financière fédérale devrait traiter chaque agent comme un compte de service privilégié, dans l’esprit de B-13 : identité propre, accès minimal, surveillance (section 9.2). Ensuite, le projet C-36 viserait aussi les décisions partiellement automatisées; le cadre conçoit donc l’explicabilité des agents pour couvrir les deux régimes, sans attendre l’adoption du projet (EXIG-CON-21). Enfin, le guide fédéral sur l’IA agentique converge avec les exigences des chapitres 8 à 10. Les institutions financières de compétence québécoise intègrent en outre les attentes de l’Autorité des marchés financiers (AMF) en matière d’IA, énoncées dans sa Ligne directrice sur l’utilisation de l’intelligence artificielle (document daté de mars 2026, publié en avril 2026, en vigueur le 1er mai 2027) **[492]**, dont les douze exigences EXIG-AMF-01 à EXIG-AMF-12 (issues du profil CRE-IA-2026-01-QC) sont intégrées directement à la section 12.10 dans la version 1.2 du présent cadre.

La veille porte aussi sur deux textes connexes : la Loi concernant la cybersécurité (ancien projet de loi C-8), sanctionnée le 15 juin 2026 (L.C. 2026, ch. 9), et le projet de loi C-22 sur l’accès légal, à l’étude au Sénat en octobre 2026 **[439, 440]**. Si sa partie 2 reprend le régime de l’ancien projet de loi C-26, la Loi concernant la cybersécurité vise aussi directement les exploitants désignés de cybersystèmes essentiels, dont des systèmes bancaires et de compensation (programme de cybersécurité, déclaration des incidents); ce point est à vérifier sur le texte sanctionné (section H.5). L’effet de ces deux textes sur les agents et sur leurs fournisseurs est suivi par la veille réglementaire de l’EXIG-GOV-20.

`EXIG-CON-11` **· DOIT**

**Régimes applicables inscrits à la fiche**

La fiche de chaque agent **DOIT** énumérer les régimes juridiques et sectoriels qui s’appliquent à lui (Loi sur le privé ou Loi sur l’accès, LPRPDE, règlement européen sur l’IA, RGPD, lignes directrices et avis du BSIF, lignes directrices de l’AMF pour une institution de compétence québécoise, directive fédérale, Loi concernant la cybersécurité pour un exploitant désigné, textes gouvernementaux québécois) et, pour chacun, les obligations retenues et l’exigence du cadre qui y répond. L’équipe risques et conformité valide cette liste à l’homologation et à chaque réévaluation (EXIG-GOV-12).

Pourquoi : un même agent peut relever de plusieurs régimes dont les seuils et les délais diffèrent; seule une liste explicite permet de satisfaire chacun selon son propre déclencheur et son propre délai (EXIG-CON-25).

`EXIG-CON-12` **· DOIT**

**Arrimage à E-23 pour les institutions financières fédérales**

Une institution financière fédérale **DOIT**, au plus tard le 1er mai 2027, inscrire chaque agent et chaque modèle qu’il utilise, y compris ceux des fournisseurs, à l’inventaire des modèles attendu par la ligne directrice E-23 (le cadre étend l’inscription à chaque agent et à chaque modèle utilisé), avec le parrain (propriétaire au sens d’E-23), la cote de risque, la version et l’état de validation. Elle **DOIT** ensuite inscrire tout agent ou modèle nouveau avant sa mise en production. L’inventaire est le registre d’entreprise (section 11.4), que l’équipe plateforme opère et où le parrain inscrit l’agent (tableau 44). E-23 ne fixe aucune échéance de validation des modèles existants : l’exigence porte sur l’inventaire et l’état de validation, et les validations sont planifiées selon la cote de risque (choix du cadre). Un changement de modèle, de fournisseur, de sources ou de catégories de données d’entrée déclenche la réévaluation de l’EXIG-GOV-12 et, s’il s’agit d’une modification importante, la revue prévue par E-23.

Pourquoi : E-23 inclut les méthodes d’IA et d’apprentissage automatique dans sa définition de modèle, traite de la prise de décision autonome dans ses principes de surveillance et attend un inventaire d’entreprise **[8]**.

## 12.4 Règlement européen sur l’IA

Cette section indique quand le règlement (UE) 2024/1689 (RIA) s’applique à une entreprise canadienne et ce qu’il exige d’un agent à haut risque.

### Portée : l’utilisation des sorties dans l’Union

Le RIA ne s’applique pas parce qu’une entreprise « opère en Europe ». Selon l’article 2(1), il vise notamment les fournisseurs qui mettent un système d’IA sur le marché ou en service dans l’Union, où qu’ils soient établis, les déployeurs établis ou situés dans l’Union, ainsi que les fournisseurs et déployeurs établis dans un pays tiers lorsque les sorties produites par le système sont utilisées dans l’Union **[61, 441]**. Un agent exploité à Montréal dont les recommandations servent à une filiale européenne peut donc être visé. Le RIA définit le système d’IA comme un système automatisé conçu pour fonctionner à différents niveaux d’autonomie, qui déduit des entrées qu’il reçoit la manière de générer des sorties pouvant influencer des environnements physiques ou virtuels (art. 3(1)); le déployeur est celui qui l’utilise sous sa propre autorité (art. 3(4)) **[61]**. Le cadre considère tout agent comme un système d’IA au sens de cette définition.

Les systèmes à haut risque relèvent de l’article 6 et des annexes I et III. L’annexe III couvre huit domaines : biométrie; infrastructures critiques; éducation et formation; emploi et gestion des travailleurs; accès aux services essentiels privés et publics, dont l’évaluation de la solvabilité et la tarification en assurance vie et maladie; répression; migration, asile et contrôle des frontières; administration de la justice et processus démocratiques **[442]**.

### Calendrier modifié par le règlement (UE) 2026/1744

Le RIA est entré en vigueur le 1er août 2024. Les pratiques interdites s’appliquent depuis le 2 février 2025, les règles sur les modèles d’IA à usage général depuis le 2 août 2025, et l’application générale, dont les obligations de transparence de l’article 50, depuis le 2 août 2026, avec une transition au 2 décembre 2026 pour le marquage de l’article 50(2) des systèmes génératifs mis sur le marché avant le 2 août 2026 **[57]**. Le règlement (UE) 2026/1744 du 8 juillet 2026, dit « omnibus numérique sur l’IA », en vigueur depuis le 27 juillet 2026, a reporté les obligations du haut risque : au 2 décembre 2027 pour les systèmes de l’annexe III et au 2 août 2028 pour ceux de l’annexe I (produits réglementés) **[58, 443]**. Il ajoute des interdictions applicables le 2 décembre 2026 (hypertrucages sexuels non consentis, matériel d’abus pédosexuel) et prévoit au moins un bac à sable réglementaire de l’IA opérationnel dans chaque État membre au 2 août 2027 **[57]**.

**ATTENTION**

Un report n’est pas un moratoire. Le règlement (UE) 2026/1744 ne suspend ni les pratiques interdites ni les obligations des modèles d’IA à usage général **[443]**. Surtout, les journaux et la documentation d’un agent ne se reconstituent pas après coup : un agent conçu en 2026 sans eux ne sera pas conforme en décembre 2027.

*Tableau 49 — Articles du règlement européen sur l’IA et réponse du cadre*

| **Article** | **Rôle visé (F : fournisseur; D : déployeur)** | **Exigence (résumé)** | **Réponse du cadre** |
| --- | --- | --- | --- |
| 2 | F, D | Portée : fournisseurs et déployeurs, y compris hors Union lorsque les sorties y sont utilisées. | Applicabilité consignée dans la fiche (EXIG-CON-13). |
| 4 | Fournisseur et déployeur. Maîtrise de l’IA : prendre des mesures pour soutenir la maîtrise de l’IA de leur personnel et des autres personnes qui exploitent ou utilisent les systèmes pour leur compte, selon leurs connaissances, le contexte d’emploi et les personnes visées; aucun niveau précis n’est exigé d’une personne (art. 4(1), remplacé par le règlement (UE) 2026/1744). La Commission et les États membres soutiennent ces efforts (art. 4(2)). | Approbateurs habilités et formés (EXIG-AUT-15); pour les autres personnes qui exploitent ou utilisent les agents, mesures de maîtrise de l’IA à prévoir dans le programme de formation de l’entreprise (aucune exigence du cadre). |  |
| 6, annexes I et III | F, D | Classification des systèmes à haut risque. | Classe élevée d’office (EXIG-CON-01 et EXIG-CON-13; choix du cadre : la dérogation de l’art. 6(3) n’est pas utilisée). La détection de la fraude financière est exclue de l’annexe III, point 5(b). |
| 9 | F | Système de gestion des risques continu et itératif sur tout le cycle de vie. | Classe de risque et réévaluations (EXIG-CON-01, EXIG-CON-03); cycle de vie (section 11.5). |
| 12 | F (conception), D (conservation, art. 26(6)) | Enregistrement automatique des événements pendant toute la durée de vie. | Traçage (section 10.1) et journal d’audit (section 10.3); la signature et l’enregistrement à cinq éléments sont des choix du cadre, au-delà du minimum légal. |
| 13 | F | Transparence et notice d’utilisation destinées aux déployeurs. | Fiche d’agent (annexe B) et carte d’agent remises aux équipes qui déploient l’agent. |
| 14 | F (conception), D (mise en œuvre, art. 26) | Supervision humaine effective : comprendre le système, rester conscient du biais d’automatisation, ignorer ou inverser une sortie, interrompre le système et le mettre dans un état sûr. | Approbation vérifiable (section 8.5), lutte contre l’approbation machinale (section 8.7), coupe-circuit (section 7.8). |
| 15 | F | Exactitude, robustesse et cybersécurité. | Évaluation continue (section 10.4) et sécurité (chapitre 9). |
| 11, 16, 17, 43, 47 à 49 | F, ou D devenu F (art. 25) | Documentation technique (art. 11), obligations générales (art. 16), système de gestion de la qualité (art. 17), évaluation de la conformité (art. 43), déclaration UE de conformité et marquage CE (art. 47 et 48), enregistrement (art. 49). | Applicables si l’entreprise est ou devient fournisseur (EXIG-CON-15). |
| 25 | D devenu F | Un déployeur devient fournisseur s’il appose son nom, modifie substantiellement le système ou en change la destination; accord écrit avec les tiers fournisseurs de composants intégrés (25(4)), sauf pour les outils, services et composants rendus publics sous licence libre et ouverte, hors modèles d’IA à usage général. | Revue de requalification (EXIG-CON-15); clauses fournisseurs (section 13.3). |
| 26 | D | Obligations du déployeur : notice, supervision compétente, données d’entrée pertinentes, surveillance et suspension, journaux conservés au moins six mois, information des travailleurs et des personnes visées. | EXIG-CON-16. |
| 27 | D | Analyse d’impact sur les droits fondamentaux (AIDF) avant la première utilisation, pour certains déployeurs. | Évaluation d’impact unifiée (section 12.9). |
| 50 | F, D | Informer les personnes qu’elles interagissent avec un système d’IA; marquer les contenus synthétiques; informer les personnes exposées à un système de reconnaissance des émotions ou de catégorisation biométrique (art. 50(3)). | EXIG-CON-19 et EXIG-CON-20. |
| 72 | F | Surveillance après commercialisation pendant toute la durée de vie, y compris l’interaction avec d’autres systèmes d’IA. | Traces des délégations A2A et analyse des chaînes multiagents dans le plan de surveillance. |
| 73 | F (le D informe d’abord le F, art. 26(5)) | Signalement des incidents graves aux autorités de surveillance du marché. | Réponse aux incidents (section 12.8). |
| 86 | D | Toute personne visée par une décision prise sur la base des sorties d’un système à haut risque de l’annexe III (sauf le point 2), qui produit des effets juridiques ou l’affecte de façon importante, a droit à des explications claires et pertinentes sur le rôle du système et sur les principaux éléments de la décision. | Explication des décisions, entièrement ou partiellement automatisées (EXIG-CON-21, EXIG-CON-07). |

Sources : règlement (UE) 2024/1689, tel que modifié par le règlement (UE) 2026/1744 (EUR-Lex) **[58, 61]**; lecture article par article des articles 9, 13 et 72, à titre secondaire, sur le site non officiel du Future of Life Institute **[444, 445, 446]**. La colonne du milieu désigne le rôle visé : fournisseur ou déployeur.

`EXIG-CON-13` **· DOIT**

**Applicabilité du RIA déterminée par l’usage des sorties**

La fiche de chaque agent **DOIT** indiquer si ses sorties sont utilisées dans l’Union européenne, ou destinées à l’être (destinataires, filiales ou clients qui s’y trouvent), et si son usage relève d’un domaine de l’annexe III. Un agent dont les sorties sont utilisées dans l’Union pour un usage de l’annexe III **DOIT** être classé en classe élevée dès la décision de classement (EXIG-CON-01), donc avant le passage en pilote, et soumis aux exigences du tableau 49 qui visent son rôle, sans attendre le 2 décembre 2027.

Pourquoi : pour un fournisseur ou un déployeur établi hors de l’Union, le critère de l’article 2(1)(c) est l’utilisation des sorties dans l’Union; les preuves exigées ne se constituent qu’en cours d’exploitation (raisonnement du cadre) **[441]**.

`EXIG-CON-14` **· NE DOIT PAS**

**Aucun usage interdit**

Un agent **NE DOIT PAS** être homologué pour une pratique interdite par le RIA, quel que soit le lieu d’utilisation de ses sorties (choix du cadre). Le registre tient la liste de ces pratiques, mise à jour selon le règlement (UE) 2026/1744, et la revue d’homologation vérifie la finalité de l’agent contre cette liste.

Pourquoi : les interdictions s’appliquent depuis le 2 février 2025, de nouvelles s’ajoutent le 2 décembre 2026, et le report du haut risque ne les touche pas **[57, 443]**.

`EXIG-CON-15` **· DOIT**

**Revue de requalification en fournisseur**

Toute orchestration qui affecte un modèle, un agent ou un système d’IA à usage général à un usage de l’annexe III, qui modifie substantiellement un système à haut risque ou qui y appose le nom de l’entreprise **DOIT** déclencher, avant l’homologation, une revue de requalification en fournisseur au sens de l’article 25(1). Si l’entreprise devient fournisseur, elle **DOIT** satisfaire aux obligations du fournisseur (art. 16 et lignes du tableau 49 marquées « Fournisseur »), dont les accords écrits avec les tiers qui fournissent des outils, services, composants ou modèles intégrés au système (art. 25(4)).

Pourquoi : la composition d’agents peut, à elle seule, changer la destination d’un composant et faire basculer l’entreprise dans le rôle de fournisseur (art. 25(1)) **[61]**.

`EXIG-CON-16` **· DOIT**

**Obligations du déployeur d’un agent à haut risque**

Pour un agent à haut risque au sens du RIA, l’entreprise **DOIT** : confier la supervision humaine à des personnes compétentes, formées et dotées de l’autorité nécessaire; veiller à la pertinence des données d’entrée qu’elle contrôle; surveiller le fonctionnement et suspendre l’usage en cas de risque; conserver les journaux sous son contrôle au moins six mois (le cadre exige davantage pour le journal d’audit, EXIG-OBS-13; les minimums par magasin sont ceux de l’EXIG-CON-10); informer les travailleurs concernés avant une mise en service en milieu de travail et les personnes visées par une décision prise ou assistée par le système.

Pourquoi : article 26 du RIA, applicable aux systèmes de l’annexe III à compter du 2 décembre 2027 **[57, 447]**.

## 12.5 NIST AI RMF, ISO/IEC 42001 et normes associées

Cette section situe les référentiels volontaires et certifiables qui structurent la gestion des risques de l’IA et retient les sous-catégories et mesures les plus utiles aux agents.

### NIST AI RMF 1.0 et profil IA générative

Le NIST AI RMF 1.0 (NIST AI 100-1), publié le 26 janvier 2023, s’articule autour de quatre fonctions : Gouverner (GOVERN), fonction transversale, Cartographier (MAP), Mesurer (MEASURE) et Gérer (MANAGE). Il est d’application volontaire; le NIST indique qu’il est en cours de révision dans le cadre du plan d’action américain sur l’IA, sans calendrier publié pour la version révisée, le document prévoyant lui-même un examen formel au plus tard en 2028 **[74, 448]**. Il compte 72 sous-catégories (GOVERN 1.1 à 6.2, MAP 1.1 à 5.2, MEASURE 1.1 à 4.3, MANAGE 1.1 à 4.3) et définit sept caractéristiques d’une IA digne de confiance : valide et fiable; sûre; sécurisée et résiliente; responsable et transparente; explicable et interprétable; respectueuse de la vie privée; équitable, avec gestion des biais nuisibles **[74]**. Le profil IA générative (NIST AI 600-1, 26 juillet 2024) décrit douze risques propres à l’IA générative ou aggravés par elle; au moins cinq touchent directement les agents : la sécurité de l’information (section 9.6), la confabulation (section 12.7), la vie privée (section 12.2), la configuration humain-IA (biais d’automatisation, dépendance excessive) et l’intégration de la chaîne de valeur et des composants (intégration non traçable de composants tiers) **[449]**.

Les sous-catégories suivantes sont les plus directement utiles aux agents **[74]** :

- **GOVERN 1.3** : processus qui déterminent le niveau d’activités de gestion des risques selon la tolérance au risque de l’organisation; **GOVERN 1.6** : mécanismes d’inventaire des systèmes d’IA, dotés de ressources selon les priorités de risque (le registre d’agents); **GOVERN 1.7** : déclassement sécuritaire (le cadre y rattache la révocation des identifiants);
- **GOVERN 6.1** et **6.2** : politiques sur les risques liés aux tiers et contingence en cas de défaillance d’un système de tiers jugé à haut risque (serveurs MCP et agents externes);
- **MAP 3.5** : processus de supervision humaine définis, évalués et documentés;
- **MEASURE 2.4** : surveillance en production du fonctionnement et du comportement du système; **MEASURE 2.7** : évaluation de la sécurité et de la résilience; **MEASURE 3.1** : suivi des risques émergents;
- **MANAGE 2.3** : réponse aux risques jusque-là inconnus et reprise; **MANAGE 2.4** : mécanismes et responsabilités pour supplanter, désengager ou désactiver un système (le coupe-circuit); **MANAGE 4.1** : plans de surveillance après déploiement couvrant le recours et la neutralisation par un humain *(appeal and override)*, l’intervention en cas d’incident, la reprise, la gestion du changement et le déclassement.

### ISO/IEC 42001 et normes associées

ISO/IEC 42001:2023 (1re édition, 18 décembre 2023) spécifie les exigences d’un système de management de l’IA (SMIA). Elle suit la structure harmonisée des normes de systèmes de management, comme ISO/IEC 27001 : articles 4 (contexte), 5 (leadership), 6 (planification, dont l’appréciation des risques en 6.1.2, leur traitement en 6.1.3 et l’évaluation d’impact des systèmes d’IA en 6.1.4), 7 (support), 8 (fonctionnement), 9 (évaluation des performances) et 10 (amélioration) **[395]**. Son annexe A, normative, compte 38 mesures réparties en neuf objectifs (A.2 à A.10). Les plus directement applicables aux agents sont A.5 (évaluation des impacts des systèmes d’IA), A.6.2.6 (exploitation et surveillance), A.6.2.8 (enregistrement des journaux d’événements), A.9 (utilisation responsable et usage prévu) et A.10 (relations avec les tiers et les clients) **[395]**. La certification est délivrée par des organismes conformes à ISO/IEC 17021-1 et à ISO/IEC 42006:2025 **[451]**.

Trois normes complètent l’ensemble. ISO/IEC 42005:2025 donne des lignes directrices pour évaluer l’impact d’un système d’IA sur les personnes et la société, à quels moments du cycle de vie, et pour intégrer cette évaluation au SMIA; ISO/IEC 23894:2023 traite de la gestion des risques propres à l’IA; ISO/IEC 22989:2022 établit la terminologie et définit l’agent d’IA (3.1.1) **[59, 452, 453]**. Le NIST AI RMF et ISO/IEC 42001 sont complémentaires (appréciation du présent cadre) : le premier est un cadre d’application volontaire, la seconde une norme d’exigences certifiable par tierce partie **[448, 451]**. Une entreprise qui vise la certification tient une déclaration d’applicabilité qui rattache les exigences du présent cadre aux mesures de l’annexe A; le lien avec le modèle de maturité est traité à la section 14.3.

### Ce que ces référentiels ne sont pas

AI TRiSM *(AI Trust, Risk and Security Management)* est un cadre d’analyste propriétaire de Gartner, non une norme : le cadre ne le place pas au même rang que le RIA, ISO/IEC 42001 ou le NIST AI RMF. La littérature scientifique l’a adapté aux systèmes multiagents autour de l’explicabilité, du ModelOps, de la sécurité et de la confidentialité, chacun sous l’angle de la gouvernance du cycle de vie **[454]**. De même, aucune publication du NIST ne fixe encore de profil d’interopérabilité des agents. L’AI Agent Standards Initiative du Center for AI Standards and Innovation (CAISI) du NIST, lancée le 17 février 2026, et le projet de superpositions de contrôles SP 800-53 (COSAiS, *Control Overlays for Securing AI Systems*, renommé COSIS, *Control Overlays for Super Intelligence Systems*; page du projet mise à jour le 20 octobre 2026), qui prévoit des cas d’usage « agent unique » et « multiagents », relèvent de la veille (section 11.7) **[411, 455]**. Il en va de même de la note de concept du 7 avril 2026 sur un profil consacré aux infrastructures critiques, document préparatoire non contraignant **[456]**.

`EXIG-CON-17` **· DOIT**

**Déclaration de tolérance au risque**

Le comité d’architecture et des risques agentiques **DOIT** faire approuver par le conseil d’administration ou la haute direction une déclaration de tolérance au risque qui fixe, pour chaque classe, sans être moins stricte que le tableau 46 ni que les obligations légales, le niveau d’activités de gestion des risques (contrôles, fréquence des revues, autorité d’approbation) et les seuils au-delà desquels un agent est suspendu (au minimum : incidents par gravité, dérive de l’évaluation continue, taux d’approbation sans modification et coût). La déclaration **DOIT** être revue chaque année et après tout incident grave (section 12.8).

Pourquoi : GOVERN 1.3 demande de proportionner la gestion des risques à la tolérance de l’organisation; sans seuils écrits, chaque équipe fixe les siens **[74]**.

## 12.6 Matrice de correspondance

La matrice relie les quatre fonctions du NIST AI RMF aux articles d’ISO/IEC 42001, aux obligations de la Loi 25, du RIA et des textes du BSIF (E-23, avis d’incident), et aux artefacts du cadre qui en font la preuve. Elle constitue une interprétation interne du cadre, non une table de correspondance publiée par le NIST ou l’ISO.

*Tableau 50 — Matrice de correspondance : NIST AI RMF, ISO/IEC 42001, Loi 25, BSIF, RIA et artefacts du cadre*

| **Fonction NIST** | **ISO/IEC 42001** | **Loi 25 (Loi sur le privé)** | **RIA** | **BSIF** | **Artefacts et contrôles du cadre** |
| --- | --- | --- | --- | --- | --- |
| **Gouverner** : GOVERN 1.1, 1.2, 1.3, 1.6, 1.7, 2.1, 6.1, 6.2 | Art. 4 et 5 (5.2 politique, 5.3 rôles); A.2, A.3, A.10 | Art. 3.1, 3.2, 18.3 | Art. 25 et 26 | E-23 : inventaire des modèles, cote de risque, gouvernance du risque de modèle | Déclaration de tolérance au risque (EXIG-CON-17); registre avec parrain nommé (section 11.4); matrice RACI (section 11.2); clauses fournisseurs (section 13.3); retrait avec révocation des identités (section 11.5) |
| **Cartographier** : MAP 1.1 à 5.2, dont MAP 3.5 | Art. 6 (6.1.2 à 6.1.4); A.5 | Art. 3.3, 8.1, 17 | Art. 6 et annexe III; art. 9, 27 et 50 | E-23 : identification des modèles, y compris de tiers | Classe de risque (EXIG-CON-01); niveau d’autonomie et paliers d’outils (chapitre 8); lieux de traitement (EXIG-CON-05); évaluation d’impact unifiée (EXIG-CON-26) |
| **Mesurer** : MEASURE 2.4, 2.5, 2.7, 3.1 | Art. 9 (9.1 à 9.3); A.6.2.4, A.6.2.6, A.6.2.8, A.7.4 | Art. 11, 12.1, 27 | Art. 12, 15, 72 | E-23 : validation et surveillance de la dérive | Traçage (section 10.1); journal d’audit (section 10.3); évaluation continue (section 10.4); taux d’approbation sans modification (section 8.7) |
| **Gérer** : MANAGE 2.3, 2.4, 4.1 | Art. 8 et 10; A.9 | Art. 3.5 à 3.8, 12.1 (révision), 23 | Art. 14, 26, 73, 86 | E-23 : revue indépendante des modifications; avis d’incident (24 heures); B-13 | Coupe-circuit (section 7.8); compensation (section 7.5); approbation vérifiable (section 8.5); réponse aux incidents (EXIG-CON-23 à EXIG-CON-25); destruction des mémoires (EXIG-CON-10) |

Interprétation du cadre, établie à partir de NIST AI 100-1 et du catalogue d’ISO/IEC 42001 **[74, 395]**.

Deux confusions courantes sont à éviter. L’objectif A.7 d’ISO/IEC 42001 porte sur les données des systèmes d’IA (acquisition, qualité, provenance, préparation), et non sur l’évaluation des performances, l’audit interne ou la revue de direction, qui relèvent de l’article 9. Les sous-catégories MANAGE 3.1 et 3.2 visent les ressources de tiers et les modèles préentraînés; le coupe-circuit relève de MANAGE 2.4 et le déclassement sécuritaire de GOVERN 1.7 **[74]**. Pour les preuves, la matrice s’applique par identifiant d’exigence (EXIG-CON-18) : les régimes que ses colonnes ne nomment pas (LPRPDE, Loi sur l’accès, RGPD, MANAGE 3.1 et 3.2) se rattachent par la liste des régimes de la fiche (EXIG-CON-11).

`EXIG-CON-18` **· DOIT**

**Base de preuves unique**

Chaque preuve produite par la plateforme ou par les équipes (trace, enregistrement d’audit, dossier de décision, EFVP, évaluation d’impact, résultat d’évaluation, rapport d’équipe rouge, décision d’homologation) **DOIT** être référencée une seule fois dans un index de preuves, qui porte ses étiquettes (identifiants des exigences du cadre auxquelles elle répond et, par le tableau 50, les dispositions externes), son empreinte et son emplacement. La preuve reste dans son magasin d’origine (journal d’audit en ajout seul, traces, dossier de décision, outil de gouvernance, risque et conformité), en une seule version qui fait foi, sauvegardes non comprises. L’index est exigible dès le jalon 2; sa consolidation outillée vient en phase Industrialisation. L’équipe risques et conformité **DOIT** revoir la matrice chaque année.

Pourquoi : un index unique évite de produire quatre dossiers pour un même contrôle et permet de démontrer, pour une demande précise à une date précise, qu’un engagement a été respecté.

## 12.7 Transparence envers les personnes

Une personne a le droit de savoir qu’elle a affaire à un agent, de reconnaître un contenu produit par un agent et de comprendre une décision qui la concerne.

L’article 50 du RIA, applicable depuis le 2 août 2026, oblige les fournisseurs à concevoir les systèmes qui interagissent directement avec des personnes de façon qu’elles sachent qu’elles interagissent avec un système d’IA, sauf si c’est évident, et à marquer de façon lisible par machine les contenus synthétiques. Les déployeurs divulguent les hypertrucages et les textes générés publiés pour informer le public sur des questions d’intérêt public, sauf contrôle éditorial humain, et informent les personnes exposées à un système de reconnaissance des émotions ou de catégorisation biométrique (art. 50(3)). L’information est claire et fournie au plus tard lors de la première interaction; un délai transitoire jusqu’au 2 décembre 2026 vise le marquage des systèmes déjà sur le marché avant le 2 août 2026 **[57, 457]**. Le cadre va un peu plus loin que ce minimum : il informe toute personne, même lorsque l’interaction paraît évidente, et identifie tout contenu d’agent diffusé à l’externe.

Au Québec, la transparence passe aussi par l’avis préalable au profilage (art. 8.1), la confidentialité par défaut (art. 9.1), l’information des décisions automatisées (art. 12.1) et le droit d’accès à une transcription intelligible (art. 27). Les principes des commissaires à la protection de la vie privée demandent un mécanisme de contestation avec révision humaine pour les décisions assistées par l’IA, et pas seulement pour celles qui sont entièrement automatisées **[438]**. Le raisonnement affiché par un modèle n’est pas forcément une explication fidèle : l’IMDA rappelle qu’il peut ne pas refléter fidèlement les actions de l’agent **[76]**.

`EXIG-CON-19` **· DOIT**

**Divulgation de l’interaction avec un agent**

Toute personne qui interagit avec un agent, par écrit ou par la voix, **DOIT** en être informée clairement au plus tard lors de la première interaction, même lorsque la nature artificielle de l’interlocuteur paraît évidente (choix du cadre). Un agent **NE DOIT PAS** se présenter comme une personne. La personne exposée à une analyse de ses émotions ou de ses caractéristiques biométriques par un agent **DOIT** en être informée de même (art. 50(3) du RIA).

Pourquoi : article 50 du RIA, que le cadre étend à toutes les interactions pour éviter une appréciation au cas par cas de ce qui est « évident » **[457]**.

`EXIG-CON-20` **· DOIT**

**Identification des contenus produits par un agent**

Tout contenu produit ou substantiellement modifié par un agent et diffusé à l’externe (courriel, publication, document, image, audio) **DOIT** être identifié comme tel. Est substantiellement modifié un contenu dont la substance n’a pas été rédigée par une personne; la relecture humaine ne dispense pas de l’identification, dont le format est fixé par canal (mention dans le courriel, métadonnées du document, filigrane de l’image ou de l’audio). Lorsque l’entreprise fournit un système génératif visé par l’article 50 du RIA, le marquage **DOIT** en outre être lisible par machine.

Pourquoi : l’article 50 n’impose l’identification que de certains contenus; l’identification de tout contenu diffusé à l’externe est un choix du cadre, qui permet aussi de retrouver la trace d’un contenu en cas d’incident ou de plainte.

`EXIG-CON-21` **· DOIT**

**Explication intelligible et canal de révision**

Chaque avis de décision rendu à l’égard d’une personne avec l’aide d’un agent, que la décision soit entièrement ou partiellement automatisée, **DOIT** indiquer le canal de révision humaine et ses coordonnées. Pour une décision fondée exclusivement sur un traitement automatisé, les obligations de l’EXIG-CON-07 s’appliquent; le cadre les étend, délai de 30 jours compris, aux décisions partiellement automatisées (choix du cadre), ce qui couvre aussi l’explication due au titre de l’article 86 du RIA. L’explication fournie sur demande présente en langage clair les principaux facteurs et paramètres de la décision, établis selon l’EXIG-CON-07, sans divulguer l’algorithme ni les poids du modèle; le raisonnement affiché par le modèle n’en tient jamais lieu.

Pourquoi : l’interprétation gouvernementale limite l’explication aux facteurs déterminants, et couvrir les décisions partiellement automatisées anticipe le projet C-36 et les principes des commissaires **[318, 431]**.

`EXIG-CON-22` **· DOIT**

**Vérification humaine du contenu juridique**

Tout contenu juridique produit par un agent et destiné à un usage externe (tribunal, autorité, client, partenaire) **DOIT** être vérifié avant sa diffusion par une personne compétente, qui confirme son exactitude et, s’il cite des sources, que chacune existe et appuie l’énoncé. Est un contenu juridique : un avis juridique, un acte de procédure, une communication à une autorité, ou un engagement contractuel nouveau ou modifié; une réponse tirée d’un gabarit approuvé par les affaires juridiques n’en est pas un. La personne compétente est un rôle inscrit à la fiche. L’outil d’envoi externe de ces contenus est classé P3 au catalogue, de sorte que la vérification prend la forme de l’approbation de l’EXIG-AUT-09.

Pourquoi : dans *Specter Aviation c. Laprade* (2025 QCCS 3521), la Cour supérieure du Québec a imposé une sanction de 5 000 $, en vertu de l’article 342 du Code de procédure civile, pour le dépôt de références inexistantes générées par l’IA **[458]**.

## 12.8 Incidents agentiques

Un incident agentique se gère comme un incident de sécurité, avec deux particularités : l’agent peut continuer d’agir pendant qu’on l’analyse, et ses effets peuvent exiger une compensation métier.

Le cadre définit l’incident agentique comme tout événement de sécurité, de confidentialité, d’intégrité ou de disponibilité qui implique un agent, ses identités, ses mémoires ou ses outils, que l’agent en soit l’auteur ou la cible : action non autorisée, fuite ou perte de données, décision erronée ayant produit un effet, contournement de garde-fou, emballement des coûts, vol d’un jeton, exfiltration d’une mémoire, compromission d’un serveur MCP ou panne. Tout incident de confidentialité au sens de la Loi 25 qui implique un agent en est un cas particulier, par exemple un connecteur MCP trop permissif qui expose le dossier d’un autre client. L’enjeu n’est pas théorique : en 2024-2025, la CAI a reçu 514 avis d’incidents de confidentialité, en hausse de 16 %, dont 80 % du secteur privé, et les accès non autorisés y dominent (251 avis) **[424]**.

Chaque incident reçoit une gravité, de S1 (la plus grave) à S4, selon son rayon d’atteinte, la présence de RP, l’irréversibilité de ses effets et les régimes de notification qu’il déclenche; la fonction risques et conformité l’attribue, indépendamment de l’équipe dont l’agent est en cause. Est un incident grave, au sens du cadre, tout incident S1 ou S2, ainsi que tout incident grave au sens du RIA (art. 3(49)). Les cinq temps s’appliquent en entier aux incidents S1 et S2; pour S3 et S4, la contention peut se limiter à l’outil ou à la fonction en cause. Un incident qui touche un composant partagé (serveur MCP, passerelle, modèle) relève d’un plan de réponse de plateforme, porté par l’équipe plateforme, qui coordonne les agents touchés.

> **[Figure]**
> - 1
> - Contenir
> - Coupe-circuit de l’agent;
> - 2
> - Préserver
> - 3
> - Évaluer et aviser
> - Impact et rayon d’atteinte; incident de confidentialité : registre, avis à la CAI et aux personnes si risque de préjudice
> - sérieux, avec diligence
> - 4
> - Corriger et compenser
> - 5
> - Apprendre
> - Retour d’expérience sans
> - blâme; mise à jour des
> - contrôles et du cadre
> - Incident agentique : action non autorisée, fuite de données, décision erronée à effet, contournement de garde-fou ou emballement des coûts
> - jetons et accès révoqués;
> - bacs à sable conservés
> - Gel des traces, de l’audit, de la mémoire, des bacs à sable, des tâches A2A, des approbations;
> - purges suspendues
> - en parallèle
> - Sagas en cours compensées;
> - actions terminées réparées
> - par le métier; correctif; relance des étages d’évaluation

***Figure 26 — Réponse à un incident agentique.** Les cinq temps se lisent de gauche à droite : on contient l’agent avant de chercher la cause, sans détruire ses preuves volatiles (bacs à sable, contexte), et on fige les preuves avant de corriger; la qualification et le premier avis démarrent en parallèle dès la contention; puis on répare et on apprend. Source : cadre CRE-IA-2026-01.*

1. **Contenir.** L’équipe de garde actionne le coupe-circuit de l’agent (EXIG-IAM-20, EXIG-ORC-28) : coupure du réseau de ses bacs à sable et désactivation de son identité, révocation de ses jetons et de ses accès, suspension de ses délégations en cours (état de chaque tâche A2A lu avant son annulation) et annulation, consignée, des actions en attente d’approbation. Les bacs à sable et le contexte d’exécution sont conservés, et non détruits (dérogation à l’EXIG-SEC-09 pendant l’incident), et le canal de compensation reste ouvert (EXIG-ORC-17). La contention est acquise lorsque le délai de révocation mesuré est écoulé et que l’annulation ou le refus des tâches A2A externes est confirmé.
2. **Préserver.** Les traces, le journal d’audit, les instantanés de mémoire, les bacs à sable, le contexte d’exécution, l’état des tâches A2A déléguées, les approbations annulées, les captures de débogage en cours, les dossiers de décision en cause et les versions exactes de l’agent, du modèle, des invites et des définitions d’outils sont figés; les purges et l’échantillonnage sont suspendus pour l’agent visé. Pour un modèle consommé par API, le gel porte sur l’identifiant de version et sur l’accès contractuel à cette version pendant l’enquête (EXIG-APP-13). Pour un système à haut risque, le RIA interdit au fournisseur, dans l’enquête qui suit le signalement d’un incident grave, d’altérer le système d’une manière susceptible de nuire à l’évaluation ultérieure des causes avant d’en informer les autorités compétentes (art. 73(6)); le déployeur y est soumis lorsqu’il ne peut joindre le fournisseur (art. 26(5)) **[61, 459]**.
3. **Évaluer et aviser.** Ce temps démarre dès la contention, en parallèle de la préservation. Les traces et le journal d’audit bornent le rayon d’atteinte (systèmes et partenaires touchés); le nombre et la résidence des personnes touchées s’établissent à partir des dossiers de décision et des systèmes sources, sous le contrôle du RPRP. L’équipe qualifie l’incident, gravité (S1 à S4) comprise, au regard de chaque régime (incident de confidentialité, atteinte au sens de la LPRPDE, incident technologique au sens du BSIF, incident grave au sens du RIA) et déclenche les avis du tableau 51. Pour un incident grave au sens du RIA, aucune correction qui altère le système n’est faite avant l’avis aux autorités (art. 73(6)).
4. **Corriger et compenser.** Les sagas en cours à la contention sont compensées automatiquement par le canal de compensation (EXIG-ORC-17, section 7.5). Les actions terminées font l’objet d’une réparation métier, décidée par le propriétaire métier après vérification de l’état courant des données, jamais d’une compensation aveugle; les effets irréversibles appellent un avis aux tiers touchés, des recours et des mesures d’atténuation. Le correctif est appliqué, puis les étages d’évaluation (E1 à E3) sont relancés avant toute remise en service; le niveau d’autonomie peut être abaissé.
5. **Apprendre.** Un retour d’expérience sans blâme met à jour les contrôles, les jeux d’évaluation et, au besoin, le cadre.

*Tableau 51 — Délais de notification applicables aux incidents agentiques*

| **Régime** | **Déclencheur** | **Destinataires** | **Délai** |
| --- | --- | --- | --- |
| Loi sur le privé, art. 3.5 | Incident de confidentialité présentant un risque de préjudice sérieux | CAI et personnes concernées | « Avec diligence »; aucun délai en heures |
| Loi sur le privé, art. 3.8, et Règlement sur les incidents de confidentialité | Tout incident de confidentialité, même sans risque de préjudice sérieux | Registre interne, transmis à la CAI sur demande | Tenu à jour; conservé au moins cinq ans |
| LPRPDE | Atteinte présentant un risque réel de préjudice grave | Commissariat et personnes concernées | « Le plus tôt possible »; registre de toutes les atteintes conservé 24 mois |
| Avis du BSIF (2021) | Incident lié à la technologie ou à la cybersécurité d’une institution financière fédérale | BSIF | Par écrit, dans les 24 heures ou plus tôt si possible |
| Loi sur l’accès, art. 63.8 à 63.11 (organismes publics) | Incident de confidentialité | CAI et personnes concernées (risque de préjudice sérieux); registre | « Avec diligence »; registre tenu à jour |
| LPRPDE, art. 10.2 | Atteinte avisée aux personnes | Organisations et institutions susceptibles de réduire le risque de préjudice ou d’en atténuer les conséquences | Dès que possible |
| RGPD, art. 33 et 34 | Violation de données à caractère personnel d’un traitement soumis au RGPD | Autorité de contrôle compétente; personnes concernées en cas de risque élevé | Autorité : dans les 72 heures après en avoir pris connaissance, si possible; personnes : dans les meilleurs délais |
| Loi concernant la cybersécurité, partie 2 (à vérifier sur le texte sanctionné) | Incident visant un cybersystème essentiel d’un exploitant désigné | Autorités désignées par la loi | Délai fixé par la loi et ses règlements |
| RIA, art. 73 (fournisseur) et art. 26(5) (déployeur : informer d’abord le fournisseur) | Incident grave impliquant un système à haut risque | Autorités de surveillance du marché | Dès l’établissement d’un lien de causalité (ou de sa probabilité raisonnable) et, dans tous les cas, au plus tard 15 jours après la prise de connaissance de l’incident grave par le fournisseur ou, le cas échéant, le déployeur; 10 jours en cas de décès; 2 jours en cas d’infraction généralisée ou de perturbation grave et irréversible d’une infrastructure critique |

Sources : L.Q. 2021, c. 25; Règlement sur les incidents de confidentialité; Commissariat à la protection de la vie privée; BSIF; RIA **[56, 61, 426, 427, 434, 460]**. La cible interne de 72 heures pour l’avis initial à la CAI (EXIG-CON-24) n’est pas un régime : c’est une cible du cadre, de force DEVRAIT, et non une exigence de la Loi 25.

L’avis écrit à la CAI comporte onze éléments, dont l’organisation et son numéro d’entreprise du Québec (NEQ), une personne-ressource, les renseignements visés, les circonstances et la cause, la date ou la période de l’incident, la date de prise de connaissance, le nombre de personnes touchées (dont les résidents du Québec), les motifs du risque de préjudice et les mesures d’atténuation; les compléments sont transmis avec diligence **[460]**. L’événement d’incident préremplit, à partir de la télémétrie et du journal d’audit, l’identification, les dates, les agents, les outils et les catégories de données déclarées au catalogue pour chaque outil en cause. Le nombre et la résidence des personnes touchées s’établissent à partir des dossiers de décision et des systèmes sources, sous le contrôle du RPRP (levée de la pseudonymisation, EXIG-OBS-13); les motifs du risque et les mesures d’atténuation relèvent de l’équipe de réponse. L’avis ne dépend ainsi pas d’une reconstitution manuelle des faits.

`EXIG-CON-23` **· DOIT**

**Réponse en cinq temps et gel des preuves**

Le plan de réponse aux incidents de chaque agent, et le plan de plateforme pour un composant partagé, **DOIVENT** suivre les cinq temps de la figure 26, gradués selon la gravité (S1 à S4) attribuée par la fonction risques et conformité. La contention (coupe-circuit, coupure du réseau et désactivation de l’identité, révocation des jetons) **DOIT** être exécutable par l’équipe de garde sans approbation préalable; elle conserve les bacs à sable et le contexte d’exécution (dérogation à l’EXIG-SEC-09 pendant l’incident) et laisse ouvert le canal de compensation (EXIG-ORC-17). L’ouverture du dossier d’incident gèle, avant toute correction et toute destruction : les traces, le journal d’audit, les instantanés de mémoire, les bacs à sable, le contexte, l’état des tâches A2A déléguées, les approbations annulées, les captures de débogage, les dossiers de décision en cause et les versions exactes de l’agent, du modèle (instantané s’il est autohébergé, sinon identifiant et accès contractuel de l’EXIG-APP-13), des invites et des définitions d’outils. Le gel suspend les purges et l’échantillonnage pour l’agent visé.

Pourquoi : sans versions figées, l’analyse des causes devient impossible; MANAGE 2.4 demande des mécanismes et des responsabilités clairs pour désactiver un système **[74]**.

`EXIG-CON-24` **· DOIT**

**Registre et avis des incidents de confidentialité**

Tout incident de confidentialité impliquant un agent **DOIT** être inscrit au registre des incidents avec le contenu prévu par le Règlement sur les incidents de confidentialité et conservé au moins cinq ans. S’il présente un risque de préjudice sérieux, la CAI et les personnes concernées sont avisées avec diligence; le cadre fixe une cible interne de 72 heures pour l’avis initial à la CAI, que l’équipe de réponse **DEVRAIT** respecter (choix du cadre).

Pourquoi : articles 3.5 et 3.8 de la Loi sur le privé et articles 7 et 8 du règlement; la loi n’impose aucun délai en heures, d’où une cible interne explicite **[56, 414, 460]**.

`EXIG-CON-25` **· DOIT**

**Règle la plus exigeante entre régimes de notification**

Le plan de réponse **DOIT** recenser, pour chaque agent, les régimes de notification applicables (au minimum, selon le cas : Loi sur le privé ou Loi sur l’accès, LPRPDE, BSIF, RIA, RGPD, Loi concernant la cybersécurité) et les cumuler : la règle la plus exigeante s’entend ainsi de chaque régime applicable, satisfait selon son propre déclencheur, son destinataire et son délai (tableau 51), ce qui suppose la double analyse du « préjudice sérieux » (Québec) et du « risque réel de préjudice grave » (fédéral). Seuls les paramètres communs prennent la valeur la plus stricte : registre unique des incidents, conservé cinq ans, et contenu minimal de l’avis. Les cibles internes gardent la force que leur donne leur exigence (EXIG-CON-24). L’événement d’incident, préparé à partir de la télémétrie, du journal d’audit et du dossier d’incident, comporte les champs de l’avis exigé par le règlement québécois.

Pourquoi : une organisation soumise à plusieurs régimes doit pouvoir satisfaire chacun sans reconstituer les faits sous la pression du délai.

## 12.9 Évaluation d’impact unifiée

Plutôt que plusieurs analyses rédigées par plusieurs équipes, le cadre exige un seul livrable par agent de classe élevée, structuré pour répondre à chaque régime, en volets séparables dont chacun porte sa classification de diffusion.

Les régimes se recoupent largement. L’EFVP examine les RP et leur parcours. L’analyse d’impact sur les droits fondamentaux (AIDF) du RIA est obligatoire avant la première utilisation pour les déployeurs de systèmes à haut risque visés à l’art. 6(2), sauf ceux de l’annexe III, point 2, qui sont des organismes de droit public ou des entités privées fournissant des services publics, ainsi que pour les déployeurs de systèmes d’évaluation de la solvabilité ou de tarification en assurance vie et maladie (annexe III, point 5, b) et c)); elle décrit les processus, la durée et la fréquence d’utilisation, les personnes touchées, les risques, les mesures de supervision humaine et les mesures prévues si les risques se matérialisent, peut renvoyer aux sections pertinentes de l’analyse d’impact relative à la protection des données (AIPD) du règlement général sur la protection des données (RGPD, art. 35) ou en intégrer des parties lorsque celle-ci remplit déjà certaines obligations (art. 27(4), tel que modifié par le règlement (UE) 2026/1744), et est notifiée à l’autorité de surveillance du marché **[58, 61, 461]**. ISO/IEC 42005:2025 fournit la méthode : quand et comment évaluer l’impact sur les personnes et la société, et comment l’intégrer au SMIA **[452]**. Un seul livrable évite que les mêmes faits soient décrits trois fois, avec trois versions différentes.

*Tableau 52 — Volets de l’évaluation d’impact unifiée*

| **Volet** | **Source** | **Contenu minimal** | **Obligatoire lorsque** |
| --- | --- | --- | --- |
| Vie privée (EFVP) | Loi sur le privé, art. 3.3 et 17; Loi sur l’accès, art. 63.5 et 70.1 | Inventaire et parcours des RP par outil, délégation et mémoire; conformité; risques et atténuation; nécessité et proportionnalité; lieux de traitement | Projet d’acquisition, de développement ou de refonte d’un système d’information ou de prestation électronique de services impliquant des RP (art. 3.3); communication hors Québec (art. 17) |
| Droits fondamentaux (AIDF) | RIA, art. 27 | Processus, durée et fréquence d’utilisation; personnes touchées; risques; supervision humaine; mesures si le risque se matérialise | Déployeurs visés par l’article 27, avant la première utilisation |
| Impact algorithmique | Recommandation du gouvernement du Québec; EIA fédérale | Erreurs, discrimination et biais; niveau d’incidence | Tout agent qui décide ou recommande à l’égard d’une personne, quelle que soit sa classe (choix du cadre, EXIG-CON-26); EIA pour les institutions fédérales assujetties à la directive |
| Impact sur les personnes et la société | ISO/IEC 42005; ISO/ IEC 42001, 6.1.4 et A.5 | Méthode, moments du cycle de vie, documentation et intégration au SMIA | Toujours (méthode de référence du cadre pour tous les volets) |
| Décision sur le risque résiduel | Cadre | Classe, niveau d’autonomie, mesures retenues, risque résiduel accepté par le propriétaire métier et par le comité | Avant le passage en pilote, confirmée à l’homologation, et avant tout relèvement du niveau d’autonomie |

Sources : **[61, 318, 413, 432, 452]**.

`EXIG-CON-26` **· DOIT**

**Évaluation d’impact unifiée par agent de classe élevée**

Chaque agent de classe élevée **DOIT** disposer d’une évaluation d’impact unifiée couvrant les volets applicables du tableau 52, approuvée par le propriétaire métier et par le comité d’architecture et des risques agentiques avant le passage en pilote et avant tout relèvement de son niveau d’autonomie. Elle est mise à jour à chaque déclencheur de l’EXIG-GOV-12, revue au moins une fois par année (choix du cadre) et référencée dans la fiche d’agent (annexe B); ses volets sont séparables, et chacun porte sa classification de diffusion. Tout agent qui décide ou recommande à l’égard d’une personne, quelle que soit sa classe, **DOIT** disposer au moins du volet impact algorithmique, approuvé par le propriétaire métier avant le passage en pilote.

Pourquoi : l’AIDF peut s’appuyer sur l’AIPD (art. 27(4)) et ISO/IEC 42005 fournit une méthode commune; un livrable unique garde les faits cohérents entre régimes **[61, 452]**.

## 12.10 Exigences sectorielles financières, harmonisation EN 18286:2026 et profil québécois AMF

La version 1.2 unifie dans le corps normatif quatre volets réglementaires et sectoriels identifiés lors des audits inter-volumes : la gouvernance de l’IA en valeurs mobilières selon l’Avis 11-348 des ACVM **[497]**, l’encadrement déterministe des virements irrévocables ISO 20022 sur le Rail en temps réel (RTR, en production depuis le 9 novembre 2026) **[498]**, l’arrimage à la première norme harmonisée du RIA (EN 18286:2026, JO L du 14 octobre 2026) **[490, 491]**, et l’intégration complète des douze exigences québécoises EXIG-AMF-01 à EXIG-AMF-12 issues de la Note AMF IA (CRE-IA-2026-01-QC) **[492]**.

### Valeurs mobilières (ACVM 11-348), paiements temps réel (RTR/ISO 20022) et norme harmonisée (EN 18286:2026)

`EXIG-CON-27` **· DOIT**

**Gouvernance IA en valeurs mobilières et convenance rattachée à une personne inscrite (ACVM 11-348)**

Dans toute activité de courtage, de conseil en valeurs mobilières ou de gestion de patrimoine, toute recommandation de placement, évaluation de convenance ou décision discrétionnaire préparée avec l’assistance d’un agent **DOIT** être liée cryptographiquement à l’identifiant d’une personne physique inscrite qui en conserve la responsabilité juridique non délégable. Le système **DOIT** persister un dossier explicable et auditable (conservé au moins 7 ans) restituant à date les six dimensions de connaissance du client, la diligence sur le produit, l’incidence des coûts, l’éventail raisonnable de solutions de rechange et la démonstration d’absence de biais rémunératoire, conformément au Règlement 31-103, aux règles de l’OCRI et à l’Avis 11-348 des ACVM.

Pourquoi : l’Avis 11-348 des ACVM rappelle que l’usage de l’IA ne délègue ni la responsabilité d’une personne inscrite ni les obligations de convenance et de gestion des conflits d’intérêts en valeurs mobilières **[497]**.

`EXIG-CON-28` **· DOIT**

**Véracité des déclarations d’IA et interdiction de l’AI washing (ACVM 11-348)**

Toute communication destinée aux clients, aux investisseurs ou au public qui décrit les capacités, l’autonomie ou la performance d’un agent **DOIT** être soumise avant diffusion à la pré-approbation documentée d’un superviseur désigné et s’appuyer exclusivement sur des preuves vérifiées issues des étages d’évaluation (EXIG-EVA-01 à EXIG-EVA-03). Les contrôles éditoriaux et filtres de sortie **DOIVENT** bloquer toute allégation exagérée ou trompeuse sur l’IA (AI washing), et l’ensemble des communications approuvées et preuves de supervision **DOIVENT** être archivés sous forme durable pendant au moins 7 ans.

Pourquoi : l’Avis 11-348 des ACVM et les règles de supervision des communications en courtage proscrivent les déclarations non fondées sur les capacités d’IA des cabinets **[497]**.

`EXIG-CON-29` **· DOIT**

**Tampon déterministe et validation ISO 20022 sur le Rail en temps réel (RTR)**

Tout virement de crédit irrévocable ou ordre de paiement initié ou préparé par un agent à destination du Rail en temps réel (RTR) de Paiements Canada (en production depuis le 9 novembre 2026) ou sur message ISO 20022 (`pacs.008`, `camt.*`) **DOIT** traverser un tampon déterministe hors modèle appliquant : la validation stricte de schéma ISO 20022 en arithmétique décimale exacte; une clé d’idempotence dérivée de l’opération racine (EXIG-ORC-21); un contrôle antifraude synchrone et de plafonds de liquidité; et, en palier P3, une approbation humaine hors bande liée au condensat JCS exact du bénéficiaire, du compte et du montant (EXIG-AUT-12), assortie d’une fenêtre de rétention configurable d’au moins 30 secondes pour les opérations dépassant le seuil de risque de l’institution.

Pourquoi : l’irrévocabilité immédiate d’un virement RTR ISO 20022 rend impossible toute compensation a posteriori par saga; la maîtrise du risque exige un tampon déterministe et un verrou d’approbation avant émission **[498]**.

`EXIG-CON-30` **· DOIT**

**Système de management de la qualité harmonisé pour agents à haut risque (EN 18286:2026)**

Lorsque l’organisation agit comme fournisseur ou est requalifiée fournisseur d’un agent à haut risque au sens de l’article 25 du RIA (EXIG-CON-15), son système de management de la qualité prévu à l’article 17 du RIA **DOIT** être aligné sur la norme harmonisée EN 18286:2026 (Décision d’exécution (UE) 2026/2274 du 12 octobre 2026, JO L du 14 octobre 2026) au plus tard au jalon J2a (1er novembre 2027, avant l’échéance annexe III du 2 décembre 2027). Le dossier qualité **DOIT** faire l’objet d’une revue annuelle documentée et assurer la traçabilité complète des versions de modèles et d’invites, des jeux d’essai E1 à E3, de la surveillance après commercialisation et des déclarations d’incidents graves.

Pourquoi : EN 18286:2026 est la première norme harmonisée publiée au Journal officiel de l’Union européenne à l’appui de l’article 17 du RIA, fournissant un référentiel auditable de système de management de la qualité **[490, 491]**.

### Profil réglementaire québécois intégré (Ligne directrice IA de l’AMF, EXIG-AMF-01 à EXIG-AMF-12)

Les douze exigences ci-dessous intègrent normativement dans la version 1.2 les attentes de la Ligne directrice sur l’utilisation de l’intelligence artificielle de l’AMF (prise d’effet le 1er mai 2027) et de sa Ligne directrice sur la gestion du risque de modèle (juin 2025), issues de la Note AMF IA (CRE-IA-2026-01-QC) **[492]**. Elles s’appliquent à toute institution financière assujettie à l’AMF et, dans un groupe financier mixte, selon la règle de la disposition la plus stricte.

`EXIG-AMF-01` **· DOIT**

**Membre de la haute direction imputable**

L’institution assujettie à l’AMF **DOIT** désigner nommément, au registre, un membre de la haute direction imputable de l’ensemble de ses agents et de ses systèmes d’IA (SIA). Le comité d’architecture et des risques agentiques lui rend compte au moins chaque trimestre, chaque parrain d’agent (EXIG-GOV-01) répond devant lui de son agent, et les responsables des modèles des agents (EXIG-AMF-05) l’informent au même rythme trimestriel de l’état de ces modèles.

Pourquoi : attentes AMF-G-04, G-07 et G-08 de la Ligne directrice IA de l’AMF (§ 4.2 et note 8), reliant l’imputabilité par agent à une imputabilité de haute direction **[492]**.

`EXIG-AMF-02` **· DOIT**

**Information du conseil d’administration**

Le membre imputable **DOIT** présenter au conseil d’administration, au moins deux fois par année, une évaluation globale des risques liés aux agents (parc par classe et niveau d’autonomie, incidents, dérogations, exposition inhérente et résiduelle selon EXIG-AMF-08, résultats de surveillance d’équité selon EXIG-AMF-11 et tendances), accompagnée chaque année de la position de la haute direction sur l’usage responsable. La même évaluation **DOIT** être remise au moins chaque trimestre aux responsables des SIA, aux gestionnaires des équipes qui les utilisent ou les valident et à la haute direction, avec avis sans délai lors de tout changement modifiant le profil de risque (premier agent N3 ou N4, première action P3 en production, premier agent au contact client, incident grave).

Pourquoi : attentes AMF-G-01, G-02 et R-04 de la Ligne directrice IA de l’AMF (§ 4.1 et § 5) **[492]**.

`EXIG-AMF-03` **· DOIT**

**Compétences par population**

L’institution **DOIT** tenir un plan de compétences agentiques fixant, pour six populations (conseil, haute direction, auteurs de politiques, équipes du cycle de vie, développeurs et acheteurs, mandants et utilisateurs avec les responsables des lignes d’affaires), les connaissances attendues et leur preuve datée (contenu et effectif visé). La fiche d’agent **DOIT** attester que ses mandants et les utilisateurs de ses sorties ont reçu ses limites et usages exclus avant leur premier accès, en complément d’EXIG-AUT-15 et d’EXIG-AUT-23.

Pourquoi : attentes AMF-G-03, G-05 et G-09 à G-12 de la Ligne directrice IA de l’AMF (§ 4.1 et § 4.2) **[492]**.

`EXIG-AMF-04` **· DOIT**

**Éthique applicable aux agents**

Le code d’éthique de l’institution **DOIT** viser expressément l’usage des agents. Les positions éthiques servant de référence au déclencheur de revalidation « désalignement éthique » (EXIG-AMF-09) **DOIVENT** être consignées, accessibles aux équipes du cycle de vie et référencées dans chaque fiche d’agent.

Pourquoi : attentes AMF-G-01 et P-01 de la Ligne directrice IA de l’AMF (§ 4.1, § 7.1 et § 8.1) **[492]**.

`EXIG-AMF-05` **· DOIT**

**Arrimage à la gestion du risque de modèle de l’AMF**

Une institution assujettie à l’AMF **DOIT** attribuer une cote de risque de modèle à chaque modèle utilisé par un agent, y compris ceux des fournisseurs, au plus tard aux semaines 9 et 10 de la phase Fondations (cote provisoire conservatrice) et définitive au plus tard le 1er mai 2027 ou avant toute mise en production ultérieure. Elle **DOIT** inscrire au répertoire des modèles, au plus tard le 1er mai 2027 et avant toute mise en production ultérieure, chaque modèle utilisé par un agent de classe modérée ou élevée avec ses rôles (approbateur, concepteur, responsable de la validation), et mettre à jour ce répertoire avant la production à chaque changement de modèle, y compris derrière un même alias (EXIG-EVA-01). Cette exigence est le pendant québécois d’EXIG-CON-12.

Pourquoi : attentes AMF-R-02, G-08, C-02 et C-03 et Ligne directrice sur la gestion du risque de modèle de l’AMF (juin 2025, § 2.2 et § 5.1) **[492]**.

`EXIG-AMF-06` **· DOIT**

**Registre aligné sur le répertoire centralisé**

Le registre des agents **DOIT** être une vue du répertoire centralisé des SIA et modèles de l’institution (EXIG-AMF-05), ou y être rapproché au moins chaque trimestre, afin qu’aucun agent de risque non négligeable n’en soit absent. La fiche d’agent **DOIT** porter les champs d’identification et de surveillance requis par l’annexe 2 de la Ligne directrice IA de l’AMF.

Pourquoi : attente AMF-C-02 de la Ligne directrice IA de l’AMF (§ 6.1 et annexe 2) **[492]**.

`EXIG-AMF-07` **· DOIT**

**Facteurs de la classe et primauté des contraintes**

La classe de risque (EXIG-CON-01) **DOIT** être évaluée en un seul passage non récursif, avant tout plafonnement, en tenant compte, outre les critères du tableau 46, de la cote de risque de chaque modèle utilisé, de l’autonomie maximale envisagée (et du pire cas de supervision) ainsi que du risque de non-conformité aux régimes qualifiés à la fiche (EXIG-CON-11). La classe ainsi arrêtée fixe ensuite unidirectionnellement le plafond d’autonomie applicable (EXIG-CON-02) : tout niveau demandé au-delà est refusé sans recalculer la classe à la baisse (rupture de toute circularité). Un agent utilisant un modèle à cote élevée ne peut être de classe faible; en cas d’information incomplète, il reçoit une classe provisoire au moins modérée. En cas de conflit, les plafonds de l’agent priment sur ceux de ses modèles.

Pourquoi : attentes AMF-C-01, C-03 et C-05 (§ 6.2 et § 6.3), avec rupture explicite de la dépendance circulaire par évaluation en un seul passage **[492]**.

`EXIG-AMF-08` **· DOIT**

**Registre institutionnel des risques agentiques**

Le comité **DOIT** tenir un registre institutionnel des risques importants liés aux agents, incluant les risques de conformité et de réputation, en quantifier l’exposition inhérente et l’exposition résiduelle pour l’ensemble du parc, le réviser au moins chaque semestre et en tirer l’évaluation globale présentée au conseil (EXIG-AMF-02). Pour chaque risque de conformité et de réputation inscrit, il **DOIT** fixer un indicateur de surveillance et vérifier la capacité des équipes de surveillance.

Pourquoi : attentes AMF-R-01, R-03, R-04, C-01 et V-09 de la Ligne directrice IA de l’AMF (§ 5 et § 7.1) **[492]**.

`EXIG-AMF-09` **· DOIT**

**Validation fondée sur les familles de risque de l’AMF**

Pour chaque agent, des déclencheurs de revalidation **DOIVENT** couvrir les neuf familles de risque de l’AMF (en plus des changements d’EXIG-GOV-12), chacun doté d’un signal mesurable. La validation **DOIT** vérifier avant production l’explicabilité des extrants pour les parties prenantes (au-delà des seules décisions visant une personne), l’adéquation des données, systèmes et outils, ainsi que la fiabilité des extrants. Chaque revalidation **DOIT** réévaluer le besoin et les solutions de rechange (dont la solution sans agent, EXIG-ORC-01), et la classe visée ainsi que l’explicabilité modulée **DOIVENT** figurer aux critères d’approvisionnement (EXIG-APP-17).

Pourquoi : attentes AMF-R-05, V-02, V-04, V-05, V-06 et V-08 de la Ligne directrice IA de l’AMF (§ 5.1 et § 7.1) **[492]**.

`EXIG-AMF-10` **· DOIT**

**Données d’apprentissage et calibrage dynamique**

L’institution **DOIT** assurer et documenter la qualité des données qui façonnent le comportement d’un agent (documents indexés, écritures en mémoire persistante et origine de toute donnée secondaire). Tout agent qui écrit dans une mémoire persistante ou un index **DOIT** être déclaré à calibrage dynamique dans sa fiche avec les limites imposées à ces écritures (l’écriture en mémoire procédurale restant interdite en production, EXIG-ARC-24), et respecter des normes de surveillance propres approuvées par le comité (en N3 et N4, celles d’EXIG-AUT-04 et d’EXIG-AUT-21).

Pourquoi : attentes AMF-V-03 et V-09 de la Ligne directrice IA de l’AMF (§ 3, § 7.1 et annexe 2) **[492]**.

`EXIG-AMF-11` **· DOIT**

**Preuves d’équité**

Pour tout agent pouvant avoir une incidence sur les clients, en complément d’EXIG-CON-04 et d’EXIG-CON-26 : une liste des facteurs et variables de substitution interdits **DOIT** être versée à la fiche et communiquée aux équipes du cycle de vie; des jeux d’essai appariés **DOIVENT** tester ces interdits avant production et à chaque changement (palier E2, EXIG-EVA-01); tout usage détecté d’un facteur discriminatoire **DOIT** entraîner sans délai la suspension ou la réduction d’autonomie de l’agent (EXIG-EVA-06) jusqu’à correction documentée; un rapport de surveillance et de correction **DOIT** être transmis aux instances pertinentes; et, pour une décision touchant un client, la fiche **DOIT** nommer les groupes surveillés.

Pourquoi : attentes AMF-P-02 à P-05 de la Ligne directrice IA de l’AMF (§ 8.2) **[492]**.

`EXIG-AMF-12` **· DOIT**

**Communication au client**

Tout agent dont les sorties parviennent à un client, directement ou par un représentant, **DOIT** : divulguer sa nature par tout mode d’échange (écrit, voix, vidéo et modes dynamiques, en complément d’EXIG-CON-19), annoncer le droit de demander une personne et assurer son intervention dans un délai cible inscrit au contrat de niveau de service (EXIG-EVA-06); marquer de façon saillante tout contenu produit avec sa participation, y compris celui remis à un représentant; et joindre d’office à l’avis de toute décision prise ou recommandée une explication claire et simple de ses principaux motifs, en complément d’EXIG-CON-21.

Pourquoi : attentes AMF-P-06 à P-09 de la Ligne directrice IA de l’AMF (§ 8.3) **[492]**.

**À RETENIR**

La classe de risque commande tout le reste : plafond d’autonomie, EFVP et évaluation d’impact, fréquence des revues, intensité des tests. Une décision qu’aucun humain n’a réellement examinée reste automatisée, quel que soit le bouton cliqué. Les délais légaux de notification diffèrent selon les régimes; le cadre satisfait chacun selon son propre délai et s’appuie sur un index de preuves unique.
