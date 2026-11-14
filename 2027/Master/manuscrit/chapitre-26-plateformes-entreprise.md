# Chapitre 26 — Plateformes d'entreprise

*Question directrice : que valent les promesses d'ouverture des éditeurs ?*

> **État de référence :** documentation des éditeurs consultée le 11 novembre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre : [1] à [14] sont des pages primaires lues, [15] à [19] des sources secondaires, non lues ou lues lors de l'audit, marquées comme telles; [20] à [22], primaires, ont été ajoutées le 14 novembre 2026. Les pages d'éditeurs établissent ce qu'un éditeur déclare, pas ce qu'un tiers a constaté.

Les grands éditeurs annoncent presque tous la prise en charge de MCP et d'A2A. L'acheteur qui s'arrête à cette mention conclut que la question de l'ouverture est réglée. Elle ne l'est pas. Un protocole fixe la forme des messages; il ne dit ni qui tient l'inventaire des agents, ni qui leur donne une identité, ni quelles règles s'appliquent à un agent venu d'ailleurs.

La thèse de ce chapitre tient en une phrase : les plateformes sont ouvertes sur le fil et fermées sur le plan de contrôle. Chaque éditeur accepte que ses agents parlent à ceux des autres; chacun veut être celui qui les recense, les identifie et les gouverne. Une promesse d'ouverture se mesure donc au sens des échanges, au statut des fonctions, au traitement des agents tiers et aux conditions commerciales.

---

## 26.1 Grille d'analyse

Six questions permettent de lire une annonce d'interopérabilité.

| Question | Ce qu'elle distingue | Pourquoi elle compte |
|---|---|---|
| Dans quel sens ? | Entrant (un agent externe appelle la plateforme) ou sortant (la plateforme appelle l'extérieur) | Une plateforme qui ne fait que consommer ne se laisse pas orchestrer de l'extérieur |
| À quel statut ? | Disponibilité générale, préversion, feuille de route | Seule la disponibilité générale engage l'éditeur |
| Quelle version ? | Révision du protocole réellement mise en œuvre | Deux produits « compatibles A2A » peuvent ne pas se comprendre |
| À quelle profondeur ? | Ce que la plateforme fait d'un agent tiers | Inventorier n'est pas gouverner |
| Avec quelle identité ? | Fournisseur d'identité exigé, portabilité des identités d'agents | L'identité est le point d'ancrage du verrouillage (chapitre 29) |
| À quelles conditions ? | Licences, prérequis, clauses | L'ouverture technique peut être fermée par contrat |

La quatrième question appelle une échelle, proposée par ce chapitre et non normative.

1. **Inventorié** : l'agent tiers figure au registre.
2. **Observé** : ses traces et ses appels d'outils remontent au plan de contrôle.
3. **Gouverné** : une identité, des politiques d'accès et un pouvoir de blocage s'appliquent à lui.
4. **De plein droit** : il reçoit les mêmes rapports, les mêmes garde-fous et les mêmes capacités qu'un agent natif.

Presque toutes les plateformes examinées atteignent le niveau 1 pour les agents tiers. Aucune page lue ne documente le niveau 4.

---

## 26.2 Microsoft

Microsoft présente Agent 365 comme une plateforme d'observabilité bâtie sur quatre piliers : gestion, gouvernance, sécurité et valeur d'affaires [2]. Une autre page de sa documentation, citée au chapitre 27, le dit plan de contrôle, autour de trois fonctions : observer, gouverner, sécuriser. Le produit est en disponibilité générale depuis le 1er mai 2026 pour le segment commercial, sous licence par utilisateur. La documentation indique Microsoft E5 comme prérequis conseillé [2].

Le registre d'agents converge vers Agent 365, tandis qu'Entra conserve l'identité des agents et les politiques d'accès [1] (chapitres 8 et 23). L'inventaire complet, qui comprend des agents d'autres éditeurs et des agents sans identité Entra, se consulte sans licence particulière, avec un simple rôle de lecture. L'application de contrôles, comme l'accès conditionnel ou la gouvernance des identités, exige en revanche la licence d'Entra Agent ID [1]. Voir demande un rôle; gouverner, une licence.

La page des agents partenaires montre comment un tiers y entre [3]. Elle recense 23 intégrations de deux sortes : des agents prêts à déployer depuis le centre d'administration, et des « fabriques d'agents », plateformes dont chaque agent créé reçoit automatiquement une identité Entra et hérite des contrôles d'Agent 365. Un tableau indique trois capacités par partenaire : inscrit, observable et accès aux outils Work IQ, qui ouvrent les données de Microsoft 365. Les 23 intégrations sont inscrites et observables; quatre seulement disposent de Work IQ. Cinq sont annoncées comme à venir, et les « coéquipiers IA » sont réservés aux participants du programme Frontier.

La même page signale que les agents déjà construits sur Google Vertex AI ou Amazon Bedrock peuvent être rendus visibles dans le centre d'administration sans développement [3]. Elle ne dit pas qu'ils deviennent observables ou gouvernés : c'est le niveau 1 de l'échelle, déduit de ce que la page tait.

Aucune des trois pages lues sur Agent 365 et Entra [1][2][3] ne mentionne MCP ou A2A. L'entrée d'un agent tiers dans le plan de contrôle passe par le SDK d'Agent 365 et par une identité Entra. A2A est intégré ailleurs dans l'offre, à Azure AI Foundry et à Copilot Studio, selon le bilan de la Linux Foundation (chapitres 4 et 6), mais la gouvernance repose sur un mécanisme propre à l'éditeur.

La documentation de Copilot Studio en précise le sens, sortant [21]. Un agent Copilot Studio se connecte à un agent externe qui parle A2A, par son point d'accès et non par sa carte, avec trois modes d'authentification : aucun, clé d'API ou OAuth 2.0. La connexion emprunte l'infrastructure des connecteurs personnalisés, ce qui permet de joindre un agent sur site ou dans un réseau virtuel. La page renvoie à MCP pour les outils. Datée du 26 août 2026, elle ne donne ni statut de disponibilité ni version du protocole; elle cherche encore la carte à l'ancien chemin `/.well-known/agent.json`, et son exemple emploie le nom de méthode `message/send`, antérieur à la version 1.0 (chapitre 6).

Une note y laisse au client le soin de vérifier, pour l'agent connecté, les flux de données, les permissions, l'observabilité et la supervision humaine [21]. La plateforme relie; elle ne gouverne pas l'agent d'autrui.

---

## 26.3 Salesforce

Le guide d'architecture d'Agentforce sur l'interopérabilité décrit quatre voies [4].

| Voie | Sens | Ce que dit le guide |
|---|---|---|
| Client MCP | Sortant | Un administrateur inscrit des serveurs MCP externes; leurs outils deviennent utilisables par les agents |
| Serveur MCP hébergé | Entrant | Expose des capacités d'Agentforce à des hôtes externes |
| A2A sortant | Sortant | Un agent Agentforce collabore avec un agent tiers, après inscription manuelle de ses capacités |
| A2A entrant | Entrant | Un agent externe appelle un agent Agentforce comme expert |

Les deux sens sont donc couverts, pour les deux protocoles, et le guide est franc sur les limites. Un changement dans le contrat d'un serveur MCP peut faire échouer l'intégration jusqu'à ce qu'elle soit rafraîchie ou réinscrite. La voie A2A sortante exige d'inscrire à la main les capacités de l'agent tiers et d'aligner les mécanismes d'authentification. En entrée, c'est le système externe qui porte la logique d'orchestration et de transfert. La délégation entre agents est volontairement limitée à un seul niveau de profondeur.

Le guide attribue aussi au client MCP des protections contre l'empoisonnement d'outil (chapitre 31); ce sont des affirmations de l'éditeur.

Le guide n'est pas daté et ne donne aucun statut de disponibilité pour MCP ni pour A2A, alors qu'il en donne pour d'autres fonctions. Un billet de Salesforce du 1er avril 2026 les qualifie de fonctions bêta [19]; le statut actuel reste à vérifier dans les notes de version.

Salesforce dispose d'un second levier, MuleSoft Agent Fabric, dont le registre détecte les agents sur d'autres plateformes (chapitres 8 et 24). Selon un compte rendu du Magic Quadrant de Gartner, c'est cette capacité de plan de contrôle multi-plateformes qui est portée à son crédit, la réserve portant sur la prévisibilité des coûts, entre abonnements, crédits et facturation à l'usage [15].

Les résultats du deuxième trimestre de l'exercice 2027, publiés le 26 août 2026, annoncent un revenu annuel récurrent d'Agentforce supérieur à 1,5 milliard de dollars, en hausse de plus de 240 % sur un an [5]. Le communiqué précise que la mesure englobe, depuis ce trimestre, d'autres offres d'IA, dont Slackbot et Headless 360 : la croissance n'est pas établie à périmètre constant. Surtout, il ne dit rien de l'interopérabilité.

---

## 26.4 ServiceNow

ServiceNow a lancé AI Control Tower le 6 mai 2025, en disponibilité générale, avec la promesse de surveiller et de gérer tout agent, modèle ou flux de travail, natif ou tiers, en un seul endroit [6]. Le même communiqué annonçait AI Agent Fabric, couche de communication fondée sur MCP et A2A, alors réservée à des clients précoces et promise en disponibilité générale pour le troisième trimestre de 2025. Douze partenaires y étaient nommés, mais ils « prévoyaient » d'offrir les premières intégrations. Une liste de partenaires n'est pas une liste d'intégrations livrées.

La suite n'est connue que par la presse, les pages de ServiceNow ayant refusé l'accès. Selon The Register, qui rend compte de la conférence de mai 2026 à partir du breffage de l'éditeur, AI Control Tower couvre désormais cinq domaines (découverte, observation, gouvernance, sécurité, mesure) et s'étend hors de la plateforme par une trentaine de connecteurs vers AWS, Google Cloud, Microsoft Azure, SAP, Oracle et Workday [16]. Une nouvelle offre, Action Fabric, expose le moteur de flux de travail aux agents externes. Son serveur MCP serait en disponibilité générale et inclus dans les licences d'IA de l'éditeur, d'autres fonctions étant prévues pour le second semestre de 2026. Chaque action d'un agent externe passerait par AI Control Tower, qui vérifie l'identité, borne les permissions et tient la piste d'audit.

Le compte rendu du Magic Quadrant ajoute un trait distinctif : agents, modèles, jeux de données et serveurs MCP sont gérés comme des éléments de configuration, rattachés à des propriétaires, à des services et à des processus de risque [15].

L'ouverture est donc double : ServiceNow gouverne les agents des autres et laisse ceux-ci agir chez lui, à condition que tout passe par sa tour de contrôle. Le statut de chaque fonction n'a pas pu être confirmé à la source.

---

## 26.5 SAP et Workday

### SAP

Le centre d'architecture de SAP consacre une architecture de référence à A2A et à MCP, mise à jour le 26 octobre 2026 [7]. Elle distingue trois dispositifs.

- L'**Agent Gateway** est la voie entrante : des clients externes consomment les agents Joule par un point d'accès A2A.
- **Bring Your Own Agent** est la voie sortante : Joule, client A2A, appelle un agent externe qui expose un serveur A2A.
- La **passerelle MCP** de l'Integration Suite, gérée par le client, expose des API SAP et non SAP et des serveurs MCP tiers comme outils gouvernés.

La version d'A2A visée est la 0.3.0, alors que la version 1.0 du protocole date de mars 2026 (chapitre 6). L'identité repose sur les jetons d'application à application de SAP Cloud Identity Services, avec le contexte de l'utilisateur nommé; un agent externe doit établir une relation de confiance avec ce service. En sortie, seul le type de message textuel est pris en charge, et Joule attend une réponse synchrone en 60 secondes; au-delà, il faut des notifications poussées. La page rappelle aussi qu'A2A ne garantit ni la livraison ni le traitement unique.

Deux avertissements figurent en toutes lettres. Certains composants de l'architecture ne sont pas encore en disponibilité générale, sans que la page dise lesquels. Et la communication bidirectionnelle avec des agents tiers ou autohébergés par l'Agent Gateway n'est pas encore prise en charge; elle est annoncée pour bientôt, sans date. L'architecture de référence décrit donc en partie une cible.

### Workday

Workday définit son Agent System of Record comme un cadre centralisé qui permet de trouver, d'inscrire, de configurer, de surveiller et de gérer des agents depuis un seul centre de contrôle [8]. Il est inclus dans l'abonnement de base. La page, mise à jour le 23 octobre 2026, ne donne pas de date de disponibilité.

Cinq types d'agents y sont reconnus, dont les agents externes, que le client définit et inscrit par une API. L'inscription en production suppose l'adhésion à une entente-cadre de services particulière : une condition contractuelle précède l'ouverture technique. Chaque agent configuré reçoit un compte système propre, et les permissions d'interaction avec l'agent sont séparées des permissions d'exécution de ses outils; un utilisateur doit satisfaire aux deux.

L'asymétrie apparaît dans les rapports. Plusieurs analyses, dont les totaux de sessions et les rapports d'entrées et de sorties, ne sont offertes que pour les agents construits par Workday [8]. Un agent externe est inscrit et gouverné, mais moins observé. La page ne mentionne ni MCP ni A2A.

SAP et Workday sont des systèmes d'enregistrement : leur plan de contrôle protège d'abord leurs données, et l'ouverture y est un accès encadré à ces données (chapitre 25).

---

## 26.6 Infonuagique : AWS et Google

### AWS

Amazon Bedrock AgentCore se présente comme un ensemble de services modulaires, utilisables ensemble ou séparément, avec n'importe quel cadriciel et n'importe quel modèle, y compris hors d'Amazon Bedrock [9]. Cinq d'entre eux touchent l'interopérabilité.

| Service | Fonction | Ouverture déclarée |
|---|---|---|
| Runtime | Exécution sans serveur des agents | Cadriciels ouverts, modèles tiers, MCP et A2A |
| Gateway | Conversion d'API et de fonctions en outils MCP | Serveurs MCP existants |
| Identity | Identité et authentification des agents | Fournisseurs d'identité existants, dont Okta et Entra ID |
| Policy | Règles déterministes sur chaque appel d'outil | Langage compatible avec Cedar |
| Registry | Catalogue d'agents, de serveurs MCP, d'outils et de compétences | Ressources déployées sur AWS, sur site ou dans un autre nuage |

L'offre est la plus modulaire de celles examinées : une entreprise peut n'adopter que la passerelle ou que le registre. La page d'ensemble ne donne toutefois le statut d'aucun service. Le compte rendu du Magic Quadrant retient une plateforme tournée vers les développeurs et note que les agents situés hors d'AWS peuvent demander un travail d'intégration supplémentaire [15].

### Google

Chez Google, l'Agent Registry catalogue les agents, les serveurs et outils MCP, les points d'accès et les compétences [10]. Il s'appuie sur MCP et A2A pour localiser et joindre ces composants. L'Agent Gateway, point d'application sur le réseau, interroge le registre avant de router une requête, évalue les politiques d'accès et applique une inspection des entrées et des sorties.

La page décrit sans détour une asymétrie. Les charges prises en charge et déployées dans un projet Google Cloud sont inscrites **automatiquement**. Les composants distants, hébergés sur site ou dans un autre nuage, s'inscrivent **manuellement**. Le registre accueille donc l'extérieur, mais au prix d'un travail que l'intérieur n'exige pas.

La page lue ne donne ni statut ni version de protocole. Les notes de version situent au 18 juin 2026 la disponibilité générale de la passerelle et du registre, ce dernier avec A2A 1.0 [17]. Depuis le 11 novembre, une préversion limitée étend la passerelle aux grappes Kubernetes hors de Google Cloud.

Les deux fournisseurs offrent des briques plutôt qu'une suite, mais leur plan de contrôle reste centré sur leurs propres projets et comptes. Ils revendent aussi des modèles de tiers, selon leur propre calendrier de retrait (chapitre 46).

---

## 26.7 IBM, UiPath et Camunda

### IBM

IBM affirme que watsonx Orchestrate gère, évalue et optimise les agents sur tout leur cycle de vie, y compris ceux développés hors de ses technologies, et parle d'un plan de contrôle agentique [11]. Ces affirmations viennent d'un billet d'annonce, qui ne mentionne ni MCP ni A2A et ne décrit aucun mécanisme. La documentation du kit de développement décrit, elle, le mécanisme [20]. Un agent externe s'inscrit sous l'un de plusieurs types : un point d'accès de complétion de conversation à la manière d'OpenAI, que la page dit le plus courant; A2A, en version 0.3.0 ou 1.0.0, les versions antérieures étant dépréciées; ou un connecteur propre à une plateforme, dont Salesforce Agentforce et Microsoft Copilot Studio. Une commande de découverte recense les agents d'Amazon Bedrock, d'Azure AI Foundry et de Vertex AI, dans l'offre en mode service seulement. L'identité de l'utilisateur peut être transmise à un agent A2A par échange de jeton (RFC 8693).

Les limites sont déclarées. Un agent externe ne peut servir que de collaborateur d'un agent natif. A2A n'est pris en charge que sur JSON-RPC, et les notifications poussées sont en aperçu technique, la plateforme procédant par interrogation périodique. La page ne décrit ni observation ni gouvernance appliquées à l'agent externe, hormis un réglage qui le réserve au plan de contrôle. Elle établit donc l'inventaire, premier niveau de l'échelle de la section 26.1, et rien au-delà. L'écart avec le billet d'annonce se réduit, sans disparaître.

### UiPath

Dans Maestro, un agent est une tâche de service d'un processus BPMN [12]. Deux formes existent : l'agent hébergé chez UiPath et l'agent externe, joint par un connecteur. La documentation nomme cinq plateformes externes, dont Azure AI Foundry, Google Vertex et CrewAI, cette dernière en préversion. L'appel passe par des points d'accès REST; la page recommande de préférer les connecteurs propres à l'éditeur quand ils existent. L'intégration de référence passe donc par des connecteurs, pas par un protocole ouvert.

La prise en charge d'A2A existe, mais en préversion [13]. En entrée, tout agent conversationnel déployé sur UiPath parle A2A et publie sa carte, sans configuration. En sortie, un agent externe s'inscrit une fois, avec sa carte et ses identifiants, dans la passerelle d'agents; les appels héritent alors des permissions de dossier, des garde-fous, des traces et de l'audit de la plateforme. La page ne précise pas la version du protocole.

### Camunda

Un billet de Camunda du 18 août 2026 distingue trois usages de MCP selon le sens de l'appel [14]. Camunda est **client** quand un agent, dans un sous-processus, appelle un serveur MCP externe. Il est **serveur** quand un client externe interroge le moteur d'orchestration pour inspecter des instances ou résoudre des incidents; ce point d'accès est offert sur les grappes en mode service dès la version 8.9. Enfin, un **processus devient un outil** MCP : l'appel lance une instance et renvoie aussitôt sa clé, sans attendre la fin.

Pour l'auteur, la question utile est « qui interroge qui ». Dans les trois sens, les appels d'outils et les décisions d'agents sont inscrits dans la piste d'audit du processus. Le billet ignore A2A, que Camunda prend partiellement en charge : trois connecteurs clients, en alpha depuis la 8.9, sans authentification auprès du serveur distant (chapitre 17).

Chez UiPath comme chez Camunda, l'agent est une étape d'un processus modélisé, et l'interopérabilité sert d'abord à le maintenir sous le contrôle de ce processus (chapitre 17).

---

## 26.8 Lire les évaluations d'analystes

Gartner a publié à l'automne 2026 son premier Magic Quadrant sur les plateformes de gestion d'agents d'IA. Le rapport n'a pas été lu : la page de Gartner a refusé l'accès [18]. Ce qui suit vient de deux textes du 2 novembre 2026 : le billet d'IBM, dont le graphique est daté d'octobre 2026 [11], et un compte rendu de presse [15].

Treize éditeurs y figurent. Le compte rendu classe Microsoft, IBM et ServiceNow parmi les leaders, AWS et Salesforce parmi les quatre « challengers ». Il contient cependant une incohérence : son chapeau range ServiceNow parmi les challengers, son corps parmi les leaders. Le placement de ServiceNow reste donc à confirmer dans le rapport.

**Vérifier ce qui est évalué.** Selon le compte rendu, la catégorie désigne des outils centralisés de gestion des agents, où qu'ils s'exécutent, réunissant sécurité, gouvernance et suivi des coûts. Elle n'évalue ni la construction ni l'orchestration. Google, SAP, Workday, UiPath et Camunda ne figurent pas dans la liste, ce qui renseigne sur le périmètre retenu, non sur la qualité de leurs produits.

**Remonter à la source.** Un billet d'éditeur ne cite que ses forces, et le compte rendu lu ne rapporte aucune réserve pour les trois leaders. Citer un placement sans avoir lu les réserves revient à citer une publicité.

**Dater.** Le graphique reflète un état d'octobre 2026, et plusieurs pages lues pour ce chapitre ont été modifiées ce même mois. Un placement vieillit plus vite que le contrat qu'il a servi à justifier.

**Chercher le motif transversal.** Une réserve revient, dans le compte rendu, pour six éditeurs hors du groupe des leaders : les contrôles les plus profonds ne s'exercent que dans l'environnement d'exécution natif ou sur le trafic qui traverse la passerelle de l'éditeur [15]. La question décisive, conclut l'article, est de savoir si un éditeur peut gouverner les agents que l'organisation possède déjà, y compris hors de son écosystème.

---

## 26.9 Interopérabilité déclarée et interopérabilité constatée

Dans le tableau, « documenté » signifie écrit dans la documentation de l'éditeur, non vérifié par un essai.

| Éditeur | Sens documentés | Réserve principale |
|---|---|---|
| Microsoft | Agents tiers intégrés par SDK; inventaire d'agents Vertex AI et Bedrock [3]; A2A sortant dans Copilot Studio [21] | Gouvernance par mécanisme propre; licences [1][2]; ni statut ni version d'A2A [21] |
| Salesforce | MCP et A2A, entrant et sortant [4] | Aucun statut dans le guide; bêta en avril 2026 [19] |
| ServiceNow | MCP et A2A; gouvernance d'agents tiers [6][16] | Documentation non lue; état de 2026 en source secondaire |
| SAP | A2A entrant et sortant, passerelle MCP [7] | A2A 0.3.0; composants non disponibles; bidirectionnel à venir |
| Workday | Inscription d'agents externes par API [8] | Rapports réservés aux agents natifs; condition contractuelle |
| AWS | MCP et A2A; registre multi-nuage [9] | Aucun statut par service dans la page lue |
| Google | MCP et A2A 1.0; composants distants [10][17] | Inscription manuelle hors de Google Cloud |
| IBM | A2A 0.3.0 et 1.0.0 sortant, connecteurs, découverte sur trois nuages [20] | Agent externe limité au rôle de collaborateur; gouvernance non documentée |
| UiPath | Connecteurs; A2A entrant et sortant [12][13] | A2A en préversion |
| Camunda | MCP dans trois sens [14] | A2A partiel (alpha) |

**Les protocoles sont presque partout, la gouvernance n'y passe nulle part.** La plupart des éditeurs documentent MCP ou A2A. Aucun ne s'en remet à eux pour gouverner : la gouvernance passe par un SDK, des connecteurs, un registre ou une passerelle propres à l'éditeur. C'est cohérent avec ce que les protocoles laissent ouvert (chapitres 5 et 6), mais le verrouillage se déplace du fil vers le plan de contrôle. Une passerelle neutre comme agentgateway, à l'Agentic AI Foundation (AAIF), offre un point d'application hors des éditeurs (chapitres 24 et 44).

**L'agent natif et l'agent tiers ne sont pas traités de la même façon.** L'inscription est automatique pour l'un, manuelle pour l'autre chez Google. Les rapports complets sont réservés aux agents natifs chez Workday. L'accès aux données de travail n'est ouvert qu'à quelques partenaires chez Microsoft. Les messages se limitent au texte en sortie chez SAP. L'asymétrie est la règle.

**Le statut et la version comptent autant que la fonction.** Une part notable de ce qui est annoncé est en préversion, à venir ou sans statut. Et les versions divergent : SAP cible A2A 0.3.0 quand le registre de Google accepte la version 1.0, incompatible avec elle (chapitre 6).

**Chacun inventorie les autres.** Microsoft rend visibles les agents de Vertex AI et de Bedrock; ServiceNow se connecte à AWS, à Google Cloud, à Azure, à SAP et à Workday; MuleSoft détecte les agents de plateformes concurrentes (chapitre 8); le registre d'AWS accepte des ressources de tout nuage. Une grande entreprise aura donc plusieurs plans de contrôle qui se recensent mutuellement, et aucun qui gouverne l'ensemble (chapitre 27).

Aucun essai d'interopérabilité indépendant entre ces plateformes n'a été trouvé : l'interopérabilité « constatée » se réduit ici à ce que la documentation admet. Une entreprise ne comble ce manque que par ses propres essais, sur trois scénarios au moins : un agent externe appelle la plateforme, la plateforme appelle un agent externe, puis un agent tiers est inscrit, restreint et révoqué depuis le plan de contrôle.

Un instrument commun existe pour une partie du premier scénario : la conformité au protocole du point d'accès que la plateforme sert. Le projet A2A publie une trousse de compatibilité (TCK), suite d'essais qui valide une mise en œuvre sur trois transports : gRPC, JSON-RPC et HTTP+JSON [22]. Elle lit la carte de l'agent testé, crée un client pour chaque interface déclarée et classe ses essais selon le niveau d'exigence de la spécification : un « MUST » non respecté est un échec, un « SHOULD » ne bloque pas la compatibilité, un « MAY » n'est essayé que si la capacité est déclarée. Le dépôt prévient qu'un résultat automatisé de 100 % n'établit pas la conformité tant que des obligations à vérifier à la main restent en suspens. Il ne publie aucune liste de mises en œuvre qui l'ont passée, et la page lue ne dit pas quelles versions du protocole il couvre. Demander à un éditeur le rapport de la trousse sur son point d'accès A2A est une exigence vérifiable.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Preuve exigée d'un éditeur | Page de documentation datée, avec statut et version | Jamais sur la foi d'un communiqué ou d'une liste de partenaires |
| Fonction admise en production | Disponibilité générale seulement | Préversion, si un plan d'adaptation est budgété |
| Sens à valider | Entrant et sortant, pour chaque protocole | Plateforme utilisée comme seul système d'enregistrement : entrant d'abord |
| Version d'A2A | Exiger la version mise en œuvre et un calendrier vers la 1.0 | — |
| Conformité à A2A | Rapport de la trousse de compatibilité sur le point d'accès de l'éditeur | Éditeur qui ne sert pas A2A en entrée |
| Agents tiers | Viser le niveau « gouverné »; noter l'écart avec l'agent natif | Niveau « inventorié » acceptable pour un simple recensement |
| Identité des agents | Fournisseur d'identité de l'entreprise, non celui de la plateforme | Plateforme unique et pérenne |
| Choix du plan de contrôle | Celui qui gouverne le plus d'agents déjà en place | Parc homogène chez un seul éditeur |
| Évaluations d'analystes | Lire le rapport, réserves comprises | Reprise d'éditeur : indice, pas preuve |
| Vérification | Essai interne sur trois scénarios avant engagement | — |

---

## Points à retenir

- La plupart des éditeurs examinés documentent MCP, A2A ou les deux. Cette mention ne dit rien du sens, du statut, de la version ni du traitement des agents tiers.
- L'ouverture s'arrête au plan de contrôle : la gouvernance passe par des mécanismes propres à chaque éditeur, non par les protocoles.
- L'agent tiers est presque toujours inventorié, parfois gouverné; aucune page lue ne le traite à égalité avec un agent natif.
- Les documentations les plus précises sont aussi celles qui avouent le plus de limites; l'absence de limites déclarées n'est pas un bon signe.
- Une liste de partenaires, un revenu récurrent ou un placement d'analyste ne sont pas des preuves d'interopérabilité.
- Le premier Magic Quadrant sur la gestion d'agents n'a été lu qu'en reprises; le placement de ServiceNow y est rapporté de façon incohérente.
- Chaque éditeur inventorie les agents des autres : la coexistence de plusieurs plans de contrôle est l'hypothèse de travail réaliste.
- Faute d'essais indépendants, la seule interopérabilité constatée est celle que l'entreprise vérifie elle-même. La trousse de compatibilité d'A2A en fournit un instrument, sans liste publique de résultats.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Microsoft Learn — convergence du registre d'agents vers Agent 365](https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence)
2. [Microsoft Learn — vue d'ensemble d'Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/overview)
3. [Microsoft Learn — agents partenaires offerts dans Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/third-party-agents)
4. [Salesforce — guide d'architecture sur l'interopérabilité d'Agentforce](https://www.salesforce.com/agentforce/resources/interoperability-guide/)
5. [Salesforce — résultats du T2 de l'exercice 2027](https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/)
6. [ServiceNow — communiqué de lancement d'AI Control Tower, 6 mai 2025](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-Launches-AI-Control-Tower-a-Centralized-Command-Center-to-Govern-Manage-Secure-and-Realize-Value-From-Any-AI-Agent-Model-and-Workflow/default.aspx)
7. [SAP Architecture Center — A2A et MCP pour l'interopérabilité des agents](https://architecture.learning.sap.com/docs/ref-arch/76ec36)
8. [Workday — Agent System of Record, considérations de mise en place](https://doc.workday.com/admin-guide/en-us/workday-ai/agents/setup-considerations--agent-system-of-record.html)
9. [AWS — Amazon Bedrock AgentCore, vue d'ensemble](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
10. [Google Cloud — Agent Registry, vue d'ensemble](https://docs.cloud.google.com/agent-registry/overview)
11. [IBM — annonce du Magic Quadrant 2026 sur les plateformes de gestion d'agents](https://www.ibm.com/new/announcements/ibm-named-a-leader-in-the-2026-gartner-magic-quadrant-for-ai-agent-management-platforms)
12. [UiPath — utiliser des agents dans Maestro](https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/using-agents-in-maestro.md)
13. [UiPath — agents A2A](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-a2a-agents)
14. [Camunda — trois usages de MCP](https://camunda.com/blog/2026/08/three-ways-camunda-speaks-mcp-and-why-the-direction-matters/)

Sources secondaires, non lues ou lues lors de l'audit :

15. [CX Today — premier Magic Quadrant sur la gestion d'agents d'IA](https://cxtoday.com/gartner-unveils-inaugural-magic-quadrant-for-ai-agent-management) — compte rendu de presse, lu.
16. [The Register — annonces de ServiceNow, 5 mai 2026](https://theregister.com/2026/05/05/servicenow_clears_agents_for_landing/) — article de presse, lu.
17. [Google Cloud — notes de version de Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes) — page d'éditeur, lue lors de l'audit.
18. [Gartner — résumé du Magic Quadrant](https://www.gartner.com/doc/8557473) — accès refusé.
19. [Salesforce — choisir un patron d'intégration pour Agentforce, 1er avril 2026](https://www.salesforce.com/blog/how-to-choose-integration-pattern-for-agentforce/) — billet d'éditeur, lu lors de l'audit.

Pages primaires lues le 14 novembre 2026, une page par source :

20. [IBM watsonx Orchestrate — agents externes, documentation du kit de développement](https://developer.watson-orchestrate.ibm.com/agents/connect_agent.md)
21. [Microsoft Learn — Copilot Studio, connexion à un agent par le protocole A2A (page datée du 26 août 2026)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-agent-agent-to-agent)
22. [A2A — trousse de compatibilité (TCK), dépôt](https://github.com/a2aproject/a2a-tck)

## Limites de ce chapitre

- Le rapport de Gartner n'a pas été lu. Sa définition de la catégorie, ses placements et ses réserves ne sont connus que par le billet d'IBM et un compte rendu de presse, relus lors de l'audit; ce dernier se contredit toujours sur ServiceNow.
- Les pages de produit et de documentation de ServiceNow ont refusé l'accès. L'état de 2026 repose sur un article de presse issu d'un breffage de l'éditeur.
- La page de SAP n'emploie pas le terme « Agent Hub » que retient le plan initial; elle parle d'Agent Gateway. Le chapitre suit la page.
- La date de disponibilité de l'Agent System of Record de Workday, que le plan initial situe en 2026, ne figure pas sur la page lue.
- De watsonx Orchestrate [20] et de Copilot Studio [21], une seule page a été lue, le 14 novembre 2026. La documentation d'Azure AI Foundry et de la passerelle d'agents de UiPath ne l'a pas été. L'absence de MCP ou d'A2A dans une page lue ne prouve pas son absence dans le produit.
- Plusieurs pages ont été lues au moyen d'un outil d'extraction qui en condense le contenu; une nuance du texte d'origine peut avoir échappé. La date du registre de Google est déduite de la place de son entrée dans les notes de version.
- L'échelle à quatre niveaux de la section 26.1 et l'essai en trois scénarios sont des propositions de ce chapitre, sans source externe.
- Aucun essai d'interopérabilité entre plateformes n'a été réalisé ni trouvé. La trousse de compatibilité d'A2A [22] n'a pas été exécutée; seule la page d'accueil de son dépôt a été lue.
- Les ajouts du 14 novembre 2026 sont les paragraphes sur Copilot Studio (26.2), sur la documentation d'IBM (26.7) et sur la trousse de compatibilité (26.9), avec les lignes correspondantes du tableau de 26.9 et de la grille. Le rattachement de la documentation d'IBM au premier niveau de l'échelle est une lecture de ce chapitre.
- L'audit du 12 novembre 2026 a relu [1], [2], [3], [5], [11], [15], [17] et [19] : faits confirmés, réserve « résumé seulement » levée pour [17] et [19], date du registre de Google corrigée (un résumé indiquait le 25 juin). Les statuts chez Salesforce, ServiceNow, AWS, SAP et UiPath n'ont pas été revérifiés.
