# 5 Architecture de référence

L’architecture de référence découpe l’entreprise agentique en six couches, de la demande jusqu’aux systèmes d’enregistrement, et en trois plans transversaux qui servent chacune d’elles. Sa règle centrale est simple : hors d’un poste de développement individuel sans justificatif de production, tout appel d’un agent vers un serveur MCP ou un pair A2A, quel que soit le domaine, et toute action de palier P2 ou P3 passent par la passerelle d’agents, vers un élément inscrit au catalogue d’entreprise (EXIG-ARC-01). Les composants décrits sont des rôles, et non des produits : le chapitre les fait correspondre à des blocs de solution remplaçables, précise l’architecture de la mémoire des agents et suit une demande de bout en bout.

## 5.1 Vue d’ensemble

Cette section présente la structure générale et la règle qui la tient ensemble; la figure 3 la résume.

> **[Figure]**
> - 1 Canaux et déclencheurs
> - Portails, clavardage
> - et applications
> - Outils de collaboration
> - (Teams, Slack)
> - Formulaires d’approbation humaine
> - Webhooks, tâches planifiées, événements
> - 2 Orchestration et état
> - Routeur sémantique
> - (qualification)
> - Moteur d’exécution durable (flux, sagas)
> - Coordination multiagent (A2A)
> - Points de contrôle, mémoire de travail
> - 3 Agents et exécution cognitive
> - Agents spécialisés
> - (internes, tiers)
> - Passerelle de modèles
> - (routage, cache, repli)
> - Bac à sable de code
> - (microVM, gVisor) et procédurale
> - 4 Médiation et connectivité
> - Passerelle d’agents MCP · A2A · politiques
> - Catalogue d’entreprise (outils, cartes d’agent)
> - Bus d’événements (CloudEvents, AsyncAPI)
> - 5 Outils et données
> - Serveurs MCP
> - de domaine
> - Adaptateurs OpenAPI outils
> - Outils de compensation
> - 6 Systèmes d’enregistrement
> - ERP, CRM, systèmes de dossiers, entrepôts de données, SaaS : exposés tels quels, sans réécriture
> - PLANS TRANSVERSAUX
> - A · Identité et sécurité
> - • Identité propre par agent (SPIFFE, OIDC)
> - • Jetons délégués courts (RFC 8693)
> - • Moteur de politiques, paliers d’outils
> - • Coffre de secrets, garde-fous, DLP
> - • Approbation humaine signée
> - B · Observabilité, évaluation, FinOps
> - • Traces OpenTelemetry (GenAI)
> - • Contexte W3C de bout en bout
> - • Budgets, coût par tâche réussie
> - C · Gouvernance et registre
> - • Registre des agents et serveurs MCP
> - • Classes de risque, niveaux N0 à N4
> - • Cycle de vie et homologation
> - • Dérogations, indicateurs
> - • Comité d’architecture et des
> - risques agentiques
> - Demandes descendantes (mandant, trace, plafonds) Résultats et artefacts remontants
> - • Journal d’audit chaîné et ancré
> - • Évaluation continue (3 étages)
> - Interdit : un agent n’atteint jamais un système ou un outil sans passer par la passerelle et le catalogue, hors fonction locale P0-P1 (EXIG-ARC-01)
> - Mémoire de travail
> - Ressources, mémoires épisodique et sémantique →

***Figure 3 — Architecture de référence : six couches et trois plans transversaux.** Les demandes descendent de la couche 1 vers la couche 6 en portant le mandant, la trace et les plafonds de la tâche; les résultats et artefacts remontent. Les trois plans transversaux servent chaque couche, et la passerelle d’agents ferme tout chemin qui contournerait le catalogue; sa portée exacte, tout appel MCP ou A2A quel que soit le domaine et toute action P2 ou P3, est celle de l’EXIG-ARC-01. Source : cadre CRE-IA-2026-01.*

Les six couches se lisent de haut en bas, dans le sens où circule une demande :

1. **Canaux et déclencheurs** : là où naît la demande, qu’elle vienne d’une personne (portail, clavardage, outil de collaboration) ou d’un système (appel HTTP automatique *(webhook)*, tâche planifiée, événement).
2. **Orchestration et état** : qui fait quoi, dans quel ordre, et où l’état de la tâche survit aux pannes.
3. **Agents et exécution cognitive** : là où l’on raisonne; on y trouve les agents, la passerelle de modèles et le bac à sable de code.

4. **Médiation et connectivité** : le passage obligé des échanges, avec la passerelle d’agents, le catalogue d’entreprise et le bus d’événements.
5. **Outils et données** : ce que les agents peuvent faire et savoir, au moyen de serveurs MCP de domaine, d’adaptateurs d’API, d’index et de graphes de connaissances.
6. **Systèmes d’enregistrement** : là où la vérité de l’entreprise est conservée (progiciel de gestion intégré ou ERP, gestion de la relation client ou CRM, systèmes de dossiers, entrepôts de données, logiciels-services ou SaaS).

Trois plans transversaux fournissent leurs services à toutes les couches : A Identité et sécurité (chapitre 9), B Observabilité, évaluation et FinOps (chapitre 10) et C Gouvernance et registre (chapitre 11).

### La règle centrale

La passerelle d’agents joue le rôle d’un poste de contrôle unique : on y vérifie l’identité de l’appelant, son droit de passage et le contenu de chaque appel, et l’on peut y fermer le passage d’un geste. Ce patron vient de l’architecture à confiance zéro du NIST, où un point d’application des politiques (PEP) ouvre, surveille et termine chaque connexion selon la décision d’un moteur de politiques**[73]**. Le catalogue d’entreprise, lui, dit ce qui a le droit d’exister : un outil, une carte d’agent ou un contrat d’événement qui n’y figure pas est injoignable.

Cette règle répond à une limite des plateformes : la gouvernance native de chacune s’arrête à sa frontière. Des éditeurs de passerelles, MuleSoft et TrueFoundry notamment, en tirent l’argument d’une application des politiques au niveau du transport, indépendante du fournisseur et du cadriciel**[44, 45]**. Le cadre retient le principe, sans reprendre de gains chiffrés qui n’ont pas été mesurés de façon indépendante.

`EXIG-ARC-01` **· DOIT**

**Passage obligatoire par la passerelle et le catalogue**

Dans tout environnement serveur, c’est-à-dire tout environnement autre qu’un poste de développement individuel sans justificatif de production (tableau 7), tout appel d’un agent vers un serveur MCP ou vers un pair A2A, quel que soit le domaine, et toute action de palier P2 ou P3 **DOIVENT** passer par la passerelle d’agents et viser un élément inscrit au catalogue d’entreprise à une version et une empreinte approuvées. Une action P2 ou P3 est toujours exposée comme outil MCP inscrit au catalogue. Seule une fonction locale de palier P0 ou P1, exécutée dans l’unité de déploiement de l’agent, sur les données de son propre domaine et inscrite au catalogue avec son palier, peut s’en dispenser; l’accès direct à une ressource de son domaine reste soumis à la décision par appel du serveur de ressources (EXIG-IAM-17). Une instance de la passerelle peut être déployée au plus près de l’agent (*sidecar*), à condition de partager la politique, le registre des identifiants de jetons d’approbation (`jti`) et le journal d’audit des autres instances. Sur un poste de développement, un serveur MCP local en `stdio`, ou en Streamable HTTP sur la boucle locale, obéit à l’EXIG-MCP-08; les événements relèvent du courtier (EXIG-ARC-13). La passerelle **DOIT** refuser tout appel vers un élément absent du catalogue.

Pourquoi : un point d’application unique est la condition pour authentifier, autoriser, tracer et couper chaque appel; un seul chemin de contournement suffit à rendre ces contrôles illusoires. La fonction locale admise ne peut ni écrire ni agir à l’extérieur : toute vérification d’approbation reste ainsi à la passerelle.

`EXIG-ARC-02` **· DOIT**

**Mandant, trace et plafonds dans chaque appel**

Chaque appel descendant **DOIT** transporter l’identité du mandant (jeton délégué, ou identité de l’agent autonome et de son parrain), le contexte de trace et la part restante de l’enveloppe de la tâche

(EXIG-FIN-04 : jetons de modèle, coût, appels d’outils, délai). L’homologation d’un composant incapable de les propager **DOIT** être refusée.

Pourquoi : ces trois éléments rendent chaque action imputable à une personne, reconstituable après coup et bornée dans ses effets et son coût; il suffit d’un maillon qui les perd pour rompre toute la chaîne.

### Des rôles, pas des produits

Chaque boîte de la figure 3 désigne un rôle. Un même produit peut en remplir plusieurs : Amazon Bedrock AgentCore, par exemple, réunit des services modulaires distincts pour l’exécution, la mémoire, la passerelle, l’identité, la politique, l’observabilité et le registre, utilisables séparément avec tout cadriciel**[102]**. À l’inverse, un rôle peut exiger plusieurs produits. La section 5.4 établit la correspondance entre rôles et produits.

## 5.2 Responsabilités et règles par couche

Cette section fixe, pour chaque couche, ce qu’elle fait, ce qu’elle ne fait pas et les exigences qui en découlent. Le fonctionnement détaillé des composants relève des chapitres thématiques indiqués en renvoi.

### Couche 1 — Canaux et déclencheurs

La couche 1 capte l’intention, diffuse les réponses en continu et affiche les formulaires d’approbation humaine. Elle authentifie la personne ou le système déclencheur, établit le mandant et ouvre la trace, mais ne décide de rien d’autre : elle ignore quel modèle sera appelé et quels outils seront employés. Un agent ambiant, qui réagit à un flux d’événements plutôt qu’à une personne, y est raccordé par un déclencheur (par exemple une tâche planifiée qui vérifie périodiquement les nouveaux événements)**[86]**. Les patrons d’interaction humaine propres à ces agents sont traités à la section 8.6.

`EXIG-ARC-03` **· NE DOIT PAS**

**Aucune logique d’agent dans les canaux**

Le code d’un canal (application Web, robot de clavardage, webhook, planificateur) **NE DOIT PAS** contenir d’invite, de choix de modèle, de séquence d’appels d’outils ni de logique d’orchestration; il transmet l’intention à la couche 2 et affiche ce qu’elle renvoie.

Pourquoi : une logique d’agent dispersée dans les canaux échappe au registre, aux évaluations et aux mises à jour; un même processus doit se comporter de la même façon, qu’on l’appelle d’un portail ou d’un outil de collaboration.

`EXIG-ARC-04` **· DOIT**

**Mandant établi et trace ouverte à l’entrée**

Tout déclencheur **DOIT** établir le mandant de la demande, soit la personne authentifiée, soit, pour un déclencheur système (planificateur, consommateur d’événements), l’identité du service et son propriétaire nommé, jamais un attribut porté par l’événement reçu (EXIG-EVT-07). Il **DOIT** aussi ouvrir une trace conforme à W3C Trace Context avant de transmettre la demande**[103]**; il ne poursuit une trace entrante que si elle vient d’une source de confiance, et la redémarre à une frontière de confiance (section 10.1).

Pourquoi : sans mandant établi à l’entrée, ni la délégation ni le filtrage des droits ne sont possibles plus bas; sans trace dès l’origine, la chaîne ne peut être reconstituée (section 10.1).

### Couche 2 — Orchestration et état

La couche 2 décide du chemin. Un routeur sémantique qualifie l’intention et choisit soit un flux déterministe, soit un agent; un moteur d’exécution durable conduit la tâche, conserve son état, attend les approbations et déclenche les compensations; la coordination entre agents passe par A2A. L’exécution durable signifie qu’une tâche reprend là où elle s’était arrêtée après une panne ou un redéploiement. Temporal, par exemple,

poursuit une exécution jusqu’à son terme sans limite de durée imposée et la reprend en rejouant son historique d’événements**[81]**. La documentation de Temporal borne toutefois cet historique (51 200 événements ou 50 Mo), si bien qu’une longue exécution doit repartir sous un nouvel historique (*Continue-As-New*), et ses activités sont réessayées sans limite par défaut, d’où la borne qu’exige l’EXIG-ORC-27 pour une activité à effet. Les flux Standard d’AWS Step Functions durent jusqu’à un an et n’exécutent jamais une tâche plus d’une fois, sauf si une règle `Retry` est déclarée, alors que les flux Express, limités à cinq minutes, s’exécutent au moins une fois en mode asynchrone (au plus une fois en mode synchrone) et sont mieux adaptés aux actions idempotentes**[104]**.

La persistance ne garantit pas, à elle seule, qu’une action ne sera pas répétée : à la reprise après une interruption, LangGraph réexécute le nœud depuis son début**[82]**. L’idempotence des effets reste donc nécessaire (section 7.4 et section 7.6).

`EXIG-ARC-05` **· DOIT**

**Exécution durable des tâches à effets**

Toute tâche qui produit un effet en écriture, attend une approbation humaine ou compte plus d’une étape (déclencheur commun avec l’EXIG-ORC-11) **DOIT** s’exécuter sous un moteur d’exécution durable qui persiste l’état hors du processus après chaque transition. Hors du poste de développement, l’état d’une telle tâche **DOIT** résider dans le magasin persistant, jamais seulement en mémoire de processus.

Pourquoi : un redémarrage de conteneur ne doit ni perdre une approbation obtenue ni relancer une écriture déjà faite; le Centre d’architecture Azure recommande de persister l’état partagé à l’extérieur de la mémoire et d’utiliser les points de contrôle**[9]**.

`EXIG-ARC-06` **· DOIT**

**Points de contrôle protégés comme des données de production**

Les magasins d’état et de points de contrôle **DOIVENT** être protégés comme des données de production (contrôle d’accès, chiffrement, contrôle d’intégrité). Un orchestrateur **DOIT** refuser de reprendre une exécution à partir d’un point de contrôle dont la provenance n’est pas vérifiée, ou plus ancien que la durée de conservation des clés d’idempotence des outils à effet de la tâche (EXIG-ORC-21); les autres règles de protection des points de contrôle sont celles de l’EXIG-ORC-13.

Pourquoi : un point de contrôle contient l’état complet de la tâche; la documentation de Microsoft Agent Framework qualifie son stockage de frontière de confiance**[105]**.

`EXIG-ARC-07` **· NE DOIT PAS**

**Le routage n’accorde aucun droit**

Le routeur sémantique et l’orchestrateur **NE DOIVENT PAS** accorder ni élargir de droits : ils choisissent un chemin, mais chaque appel qui en découle reste soumis à l’autorisation de la passerelle selon les droits effectifs de la chaîne (PRIN-03) et le palier de l’outil, décidée à chaque appel (EXIG-IAM-02).

Pourquoi : le routage repose souvent sur un modèle, donc sur une sortie probabiliste et manipulable; une intention mal qualifiée ou injectée doit mener à un refus, jamais à une élévation de privilèges (section 9.6).

### Couche 3 — Agents et exécution cognitive

La couche 3 exécute la boucle locale de chaque agent : raisonner, agir au moyen d’un outil, observer le résultat. Chaque agent s’exécute dans un environnement d’exécution indépendant du fournisseur de modèle, encadré par deux composants partagés. La passerelle de modèles centralise les identifiants des fournisseurs, le routage entre modèles, l’équilibrage de charge, le cache, le repli et les quotas de jetons. Agent Router, projet de l’AAIF anciennement nommé Envoy AI Gateway, illustre ce rôle : les développeurs y trouvent une interface unique vers les modèles, pendant que l’équipe plateforme y centralise fournisseurs, identifiants,

quotas, routage et basculement**[36, 106]**. Le bac à sable, quant à lui, exécute en isolement le code que l’agent produit (section 9.7).

`EXIG-ARC-08` **· DOIT**

**Passerelle de modèles obligatoire**

Tout appel d’inférence fait par un agent dont l’entreprise contrôle l’exécution, ou pour son compte (plongements, juges d’évaluation et classifieurs de garde-fous compris), **DOIT** passer par la passerelle de modèles de l’entreprise; l’agent ne détient aucune clé de fournisseur de modèles et n’appelle jamais un fournisseur directement. Un agent intégré à un logiciel-service relève de l’EXIG-ARC-21.

Pourquoi : c’est le seul endroit où l’on peut appliquer des quotas de jetons (comme le fait la politique `llm-token-limit` d’Azure API Management**[107]**), imputer les coûts, changer de fournisseur et révoquer un accès sans toucher aux agents.

`EXIG-ARC-09` **· DEVRAIT**

**Modèles désignés par un alias logique**

Un agent **DEVRAIT** désigner ses modèles par un alias logique que la passerelle résout, de sorte qu’un changement de modèle ou de fournisseur s’effectue par configuration, sans modification du code de l’agent, et toujours après la réévaluation qu’exige l’EXIG-GOV-12. L’alias se résout vers un instantané daté du modèle, épinglé et inscrit au registre.

Pourquoi : les modèles changent plus vite que les agents; l’alias isole l’agent de ces changements, tandis que la télémétrie consigne la version réellement servie.

`EXIG-ARC-10` **· DOIT**

**Code généré exécuté en bac à sable**

Le code qu’un agent produit ou choisit dynamiquement **DOIT** s’exécuter dans un bac à sable éphémère et isolé, sans accès réseau par défaut ni accès aux secrets, selon les exigences de la section 9.7; jamais dans le processus de l’agent ni sur son hôte.

Pourquoi : l’OWASP range l’exécution de code inattendue parmi les dix principaux risques des applications agentiques (ASI05 *Unexpected Code Execution*)**[28]**.

### Couche 4 — Médiation et connectivité

La couche 4 masque le paysage applicatif derrière des contrats uniformes. Elle réunit trois rôles : la passerelle d’agents, devant les serveurs MCP et les pairs A2A, mandataire inverse pour le trafic entrant et mandataire sortant pour le trafic qui quitte l’entreprise; le catalogue d’entreprise, source unique de ce qui est joignable; le bus d’événements, pour les échanges découplés dans le temps (section 6.7). Le rôle de passerelle est réalisable avec des produits documentés : Azure API Management expose et gouverne des serveurs MCP et des API d’agents A2A, et Amazon Bedrock AgentCore Gateway sert de point d’entrée unique aux outils, aux agents et aux modèles**[108, 109, 110]**. Une passerelle relaie toutefois le trafic A2A sans assumer l’état des tâches : le greffon AI A2A Proxy de Kong Gateway (3.14 et plus, édition AI Gateway Enterprise), par exemple, ne modifie pas le routage et ne gère pas cet état**[111]**. L’état reste du ressort de l’agent ou de l’orchestrateur.

`EXIG-ARC-11` **· DOIT**

**Passerelle d’agents dans les deux sens**

Dans tout environnement serveur, la passerelle d’agents **DOIT** s’interposer devant tous les serveurs MCP, internes et externes, et devant tous les pairs A2A, pour le trafic intradomaine et interdomaine comme pour celui qui entre dans l’entreprise ou qui en sort, et réévaluer l’autorisation à chaque appel.

Un agent intégré à un logiciel-service n’atteint les systèmes d’enregistrement de l’entreprise que par elle, comme client externe (EXIG-ARC-21). La portée du passage obligatoire est celle de l’EXIG-ARC-01, qui fait foi et que l’EXIG-IAM-17 reprend; ses fonctions obligatoires sont fixées à la section 9.4.

Pourquoi : l’agent d’un partenaire qui appelle l’entreprise et un agent interne qui appelle un SaaS franchissent la même frontière de confiance; la confiance zéro vise des décisions d’accès au moindre privilège prises requête par requête et une confiance réévaluée en continu pendant la session, et non une confiance acquise une fois pour toute la durée d’une session**[73]**.

`EXIG-ARC-12` **· DOIT**

**Liste d’autorisation tirée du catalogue**

La passerelle **DOIT** tirer sa liste d’autorisation du catalogue d’entreprise, seule source des outils, cartes d’agent et contrats d’événements joignables, avec leur version et leur empreinte approuvées (section 6.8). Aucune liste propre à un projet ne fait foi. La passerelle **DOIT** aussi appliquer la liste de suspension (agents, outils, versions) reçue par le canal signé de l’EXIG-IAM-18, même quand le plan de contrôle est indisponible.

Pourquoi : deux listes finissent toujours par diverger; une source unique permet de retirer partout, par une seule décision, un outil compromis, y compris pendant une panne du plan de contrôle.

`EXIG-ARC-13` **· DOIT**

**Aucun contournement par le bus d’événements**

Tout sujet ou canal d’événements produit ou consommé par un agent **DOIT** être inscrit au catalogue avec son contrat, et ses producteurs comme ses consommateurs **DOIVENT** s’authentifier auprès du bus et être autorisés par sujet selon l’entrée de catalogue (EXIG-EVT-07). Le courtier et l’intercepteur de publication sont le point d’application des politiques pour les événements (EXIG-EVT-07) : une publication par une session marquée non fiable y subit le même retrait que les outils d’envoi (EXIG-SEC-06), et toute action P2 ou P3 qu’un consommateur exécute à la suite d’un événement passe par la passerelle d’agents (EXIG-ARC-01).

Pourquoi : le bus est l’autre voie d’accès aux systèmes; s’il échappe au catalogue, un simple abonnement suffit à contourner la règle centrale.

### Couche 5 — Outils et données

La couche 5 expose les capacités de l’entreprise sous forme d’outils et de ressources : serveurs MCP de domaine, adaptateurs qui traduisent une API existante en outils, index et graphes de connaissances, et outils de compensation qui défont ou corrigent une action (section 7.5). Des produits convertissent déjà des API en outils sans toucher aux services : AgentCore Gateway transforme des API OpenAPI ou Smithy et des fonctions Lambda en outils MCP, et IBM ContextForge virtualise des services REST ou gRPC en MCP**[110, 113]**.

Un bon outil n’est pas le miroir d’un point d’accès. Anthropic recommande de choisir délibérément les outils plutôt que d’envelopper chaque point d’accès d’une API, de regrouper les opérations en plusieurs étapes et de renvoyer un contexte signifiant plutôt que des identifiants techniques**[114]**. OpenAI propose de vérifier qu’une personne pourrait utiliser la fonction avec la seule information fournie**[115]**. Ainsi, plutôt que trois outils « lire le client », « lire les factures » et « lire les paiements », on expose un outil `consulter_situation_compte` qui rend la synthèse utile à la tâche.

`EXIG-ARC-14` **· DOIT**

**Exposition sans réécriture des services**

Les capacités existantes **DOIVENT** être exposées aux agents par des serveurs MCP ou des adaptateurs placés devant les API en place, sans réécriture de la logique métier des services d’origine. L’ajout minimal qui rend une écriture idempotente ou traçable (champ de clé d’idempotence, référence de trace, lecture par clé, écriture conditionnelle) est permis. Un adaptateur qui ne dispose ni d’un tel mécanisme du service, ni d’un registre de clés durable mis à jour dans la même transaction que l’effet ou complété par une requête d’état qui le constate, déclare l’outil non idempotent (EXIG-ORC-22).

Pourquoi : l’intégration agentique s’ajoute au patrimoine applicatif sans le déstabiliser, et les règles métier restent là où elles sont déjà testées.

`EXIG-ARC-15` **· DEVRAIT**

**Outils conçus pour la tâche**

Les outils **DEVRAIENT** être conçus selon les tâches des agents (opérations regroupées, réponses paginées et filtrées, contexte signifiant) plutôt que de reproduire un à un les points d’accès d’une API; les règles de conception détaillées figurent à la section 6.5.

Pourquoi : chaque outil superflu consomme du contexte et accroît les erreurs de sélection (section 7.3).

`EXIG-ARC-16` **· DOIT**

**Résultats filtrés selon les droits du mandant**

Un outil **DOIT** filtrer ses résultats selon les droits effectifs de la chaîne (PRIN-03), de sorte qu’aucun agent ne reçoive une donnée que le mandant ne pourrait pas consulter lui-même ou qui excède la portée de l’agent au registre.

Pourquoi : le Centre d’architecture Azure demande ce filtrage de sécurité *(security trimming)* dans chaque agent**[9]**; le cadre le place à la source, dans l’outil, où il ne dépend pas du comportement d’un modèle.

### Couche 6 — Systèmes d’enregistrement

La couche 6 regroupe les systèmes qui font foi : ERP, CRM, systèmes de dossiers, entrepôts de données et SaaS. Ils sont exposés aux agents tels quels. L’entreprise agentique ne les remplace pas et ne les contourne pas : elle les appelle par leurs interfaces, sous leurs propres contrôles.

`EXIG-ARC-17` **· DOIT**

**Écriture par les interfaces qui appliquent les règles métier**

Un agent **DOIT** écrire dans un système d’enregistrement uniquement par une interface qui applique les contrôles métier de ce système (API ou service métier), sans accès direct aux tables ni compte technique qui contourne ces contrôles.

Pourquoi : validations, séparation des tâches et journaux du système d’enregistrement sont des contrôles éprouvés; un agent qui les contourne annule cette assurance.

`EXIG-ARC-18` **· DEVRAIT**

**Référence de trace sur chaque écriture**

Chaque écriture d’agent dans un système d’enregistrement **DEVRAIT** porter une référence de trace que le système cible conserve avec l’opération, en plus de la clé d’idempotence qu’exige l’EXIG-ORC-21 (section 7.6).

Pourquoi : lors d’un incident, on doit pouvoir remonter d’une ligne de l’ERP à la trace de l’agent qui l’a créée, et une reprise ne doit jamais créer de doublon.

## 5.3 Plans transversaux

Les trois plans transversaux fournissent à toutes les couches des services communs, conçus une fois et consommés partout; le tableau 11 indique ce que chacun apporte à chaque couche.

**A — Identité et sécurité.** Chaque agent reçoit une identité propre, délivrée par une infrastructure d’identité de charge de travail comme SPIFFE/SPIRE, projets diplômés de la Cloud Native Computing Foundation (CNCF)**[116, 117]**, ou par fédération OpenID Connect (OIDC) infonuagique. Lorsqu’il agit pour une personne, il obtient un jeton délégué par échange de jetons (RFC 8693)**[69]**; le cadre exige que ce jeton soit de courte durée. Le plan fournit aussi le moteur de politiques, les paliers d’outils, le coffre de secrets, les garde-fous et l’approbation humaine signée (chapitre 9 et section 8.5).

**B — Observabilité, évaluation et FinOps.** Les couches 1 à 5 émettent des traces OpenTelemetry reliées par un même contexte W3C Trace Context**[103]**, selon une version épinglée des conventions GenAI, qui distinguent notamment les spans `invoke_workflow`, `invoke_agent` et `execute_tool`**[119, 120]**. S’y ajoutent le journal d’audit chaîné et ancré, distinct des traces, l’évaluation continue et la mesure du coût par tâche réussie (chapitre 10).

**C — Gouvernance et registre.** Le registre des agents et des serveurs MCP porte la classe de risque, le niveau d’autonomie (N0 à N4), le parrain, le responsable technique et l’état du cycle de vie de chaque agent (chapitre 11). Les plans de contrôle des éditeurs couvrent une partie de ce rôle, sans le couvrir entièrement : Microsoft Agent 365, en disponibilité générale depuis le 1er mai 2026, offre un registre et des contrôles comme le blocage des agents non gérés, mais les actions de cycle de vie sur des agents infonuagiques tiers y sont encore annoncées comme à venir**[46]**. D’où l’exigence d’un coupe-circuit appliqué à la passerelle à tout agent qui la traverse, quel que soit son éditeur (section 9.4); un agent qui s’exécute chez l’éditeur d’un logiciel-service est arrêté par le mécanisme propre de l’EXIG-ARC-21.

*Tableau 11 — Apport des plans transversaux à chaque couche*

| **Couche** | **A — Identité et sécurité** | **B — Observabilité, évaluation, FinOps** | **C — Gouvernance et registre** |
| --- | --- | --- | --- |
| 1. Canaux et déclencheurs | Authentification de la personne ou du service; établissement du mandant | Ouverture de la trace; latence perçue | Canaux autorisés par agent; avis à la personne qu’elle interagit avec un agent (section 12.7) |
| 1. Orchestration et état | Jeton délégué de la tâche; approbations humaines signées | Spans de flux; enveloppe budgétaire de la tâche | Patron d’orchestration et niveau d’autonomie déclarés |
| 1. Agents et exécution cognitive | Identité propre par agent; garde-fous d’entrée et de sortie | Spans d’agent et d’inférence; jetons et coût par appel; évaluation continue | Versions de l’agent et du modèle inscrites; classe de risque |
| 1. Médiation et connectivité | Point d’application des politiques; coupe-circuit | Journalisation de chaque appel; propagation du contexte de trace | Catalogue, versions épinglées, liste d’autorisation |
| 1. Outils et données | Portées par outil; jetons à audience unique; secrets injectés hors de l’agent | Spans d’outil; erreurs par outil | Palier P0 à P3, propriétaire, compensation déclarée |
| 1. Systèmes d’enregistrement | Contrôles d’accès natifs conservés | Corrélation par référence de trace et clé d’idempotence | Classification des données; EFVP pour tout projet d’acquisition, de développement ou de refonte de système impliquant des RP, et avant leur communication hors Québec (section 12.2) |

`EXIG-ARC-19` **· DOIT**

**Services transversaux mutualisés**

Les services des plans transversaux (identité des agents, moteur de politiques, coffre de secrets, collecte de télémétrie, journal d’audit, registre) **DOIVENT** être fournis par l’équipe plateforme (section 11.1) et consommés par toutes les couches. Un projet **DOIT** obtenir une dérogation pour en déployer un équivalent parallèle (section 11.6).

Pourquoi : un registre ou une chaîne de télémétrie parallèle crée un angle mort que ni le comité ni l’équipe de garde ne voient.

## 5.4 Blocs de construction

Cette section relie les rôles de l’architecture aux produits qui peuvent les remplir. Le cadre reprend la distinction de TOGAF : les blocs de construction d’architecture (ABB) capturent les exigences et orientent le développement des blocs de construction de solution (SBB); les SBB désignent les produits et composants qui mettent en œuvre la fonction et dépendent du produit ou du fournisseur**[121]**. Le passage des uns aux autres est itératif : les ABB se définissent surtout aux phases A à D de la méthode de développement d’architecture (ADM), puis se raffinent en SBB, dont l’identification relève surtout de la phase E**[121]**. Concrètement, « passerelle d’agents » est un ABB neutre et durable; le produit retenu pour la réaliser est un SBB remplaçable.

`EXIG-ARC-20` **· DOIT**

**Correspondance ABB-SBB documentée**

Toute solution agentique présentée à l’homologation **DOIT** documenter la correspondance entre les ABB du tableau 12 et les SBB qu’elle emploie. L’homologation **DOIT** être refusée tant qu’un ABB du tableau 12 nécessaire à la solution n’a pas de SBB désigné. Sont toujours nécessaires la passerelle d’agents (EXIG-ARC-01) et les services des plans transversaux (EXIG-ARC-19), ainsi que, selon la solution, le moteur d’exécution durable pour toute écriture ou approbation (EXIG-ARC-05), la passerelle de modèles pour toute inférence (EXIG-ARC-08) et le bac à sable pour tout code généré (EXIG-ARC-10); une solution ne peut déclarer non nécessaire un ABB qu’exige l’une de ces exigences.

Pourquoi : la correspondance révèle les rôles orphelins, par exemple un agent sans passerelle de modèles, avant qu’ils ne deviennent des incidents.

`EXIG-ARC-21` **· DOIT**

**SBB exposés par les standards retenus**

Un SBB **DOIT** exposer ses fonctions d’interopérabilité par les standards retenus au catalogue des protocoles (section 6.3), de sorte qu’on puisse le remplacer sans réécrire les agents. Une fonction offerte seulement par une interface propriétaire exige une dérogation. PRIN-09, l’EXIG-ARC-03 et l’EXIG-ARC-08 visent les agents dont l’entreprise contrôle l’exécution. Un agent intégré à un logiciel-service, qui s’exécute chez son éditeur, **DOIT** : être inscrit au registre avec sa classe, son niveau d’autonomie et les actions qu’il exécute dans le logiciel-service; n’atteindre les systèmes d’enregistrement de l’entreprise que par la passerelle d’agents, comme client externe; relever d’un contrat qui comporte les clauses des EXIG-APP-05, EXIG-APP-06, EXIG-APP-08 et EXIG-APP-13, dont un préavis opposable de changement de modèle; disposer d’un mécanisme d’arrêt propre (fournisseur d’identité, retrait des consentements OAuth, CAEP), documenté à la fiche et éprouvé à l’exercice de l’EXIG-SEC-26; et n’employer que des schémas d’outils de tiers épinglés et approuvés au catalogue (EXIG-INT-02). Une action P3 exécutée dans le logiciel-service exige un mécanisme d’approbation du

fournisseur jugé équivalent à l’EXIG-AUT-12 à l’homologation; à défaut, l’agent est plafonné à N2, et chaque action P3 est approuvée dans la console de l’éditeur, approbation consignée à la fiche. La quarantaine (EXIG-GOV-10) et la suspension d’un tel agent passent par son mécanisme d’arrêt propre, et non par la passerelle.

Pourquoi : le risque de verrouillage s’est déplacé des protocoles vers les plateformes et leurs extensions (section 13.1), et un agent qui infère et agit chez son éditeur ne peut ni passer par la passerelle de modèles ni être arrêté par la passerelle d’agents; les contrôles compensatoires portent donc sur l’accès aux systèmes de l’entreprise, les contrats et les identités.

Les exemples du tableau sont non limitatifs et établis au 27 octobre 2026. Ils ne constituent ni une exigence ni une recommandation d’achat; l’architecture d’entreprise les révise chaque trimestre, avec le catalogue des protocoles (section 11.7). Un SBB qui ne couvre pas toutes les capacités exigées de son ABB (par exemple une passerelle limitée aux outils MCP, ou un environnement d’exécution sans A2A ni OpenTelemetry documentés) n’est admis qu’avec un SBB complémentaire ou une dérogation (EXIG-ARC-21); à défaut, l’homologation est refusée (EXIG-ARC-20).

*Tableau 12 — Correspondance des blocs de construction d’architecture (ABB) et des blocs de construction de solution (SBB)*

| **Couche** | **ABB** | **Capacités exigées** | **Exemples de SBB (non limitatifs, état au 27 octobre 2026)** |
| --- | --- | --- | --- |
| 1. Canaux et déclencheurs | Interface conversationnelle et d’approbation; déclencheurs système | Authentifier, établir le mandant, ouvrir la trace, diffuser en continu, montrer l’action exacte à approuver | Portails et outils de collaboration existants; canaux intégrés des logiciels-services (dernière ligne); webhooks et planificateurs |
| 1. Orchestration et état | Moteur d’exécution durable; orchestrateur et routeur; magasin d’état | Persistance après chaque transition, reprise, attente d’approbation, compensation | Temporal, dont l’intégration avec l’OpenAI Agents SDK est en disponibilité générale depuis le 23 mars 2026**[122]**; AWS Step Functions; LangGraph 1.0 avec persistance intégrée de l’état d’exécution (*checkpointer*)**[123, 124]**; Microsoft Agent Framework 1.0**[125]**; agents de flux de Google ADK**[126]** |
| 1. Agents et exécution cognitive | Environnement d’exécution d’agents | Boucle d’agent, appels MCP et A2A, télémétrie OpenTelemetry, indépendance du modèle | OpenAI Agents SDK (boucle d’agent, MCP, traçage intégré et fournisseurs non OpenAI; A2A et OpenTelemetry non documentés), Strands Agents, Google ADK, Microsoft Agent Framework, LangGraph**[127, 128, 129]**; AgentCore Runtime |
| 1. Agents et exécution cognitive | Passerelle de modèles | Identifiants centralisés, routage, repli, cache, quotas de jetons, imputation des coûts | Agent Router (AAIF)**[130]**; fonction de passerelle de modèles d’agentgateway**[131]**; Kong AI Gateway**[132]**; Azure API Management |
| 1. Agents et exécution cognitive | Bac à sable de code | Isolation par microVM, noyau applicatif ou environnement WebAssembly sans autorité ambiante, réseau fermé par défaut, exécution éphémère | MicroVM Firecracker**[133]**; gVisor**[134]**; Kata Containers**[135]**; WebAssembly et WASI**[136]**; agent-sandbox pour Kubernetes**[137]** |
| 1. Médiation et connectivité | Passerelle d’agents (PEP pour MCP et A2A) | Mandataire inverse en entrée et mandataire sortant en sortie, autorisation par appel, garde-fous, plafonds, journalisation, coupe-circuit | agentgateway, projet de l’AAIF sous licence Apache 2.0**[31]**; Azure API Management (outils MCP seulement, agents A2A en JSON-RPC seulement)**[108, 109]**; AgentCore Gateway**[110]**; Kong AI Gateway**[132]**; MuleSoft Agent Fabric et sa passerelle Flex Gateway**[138]**; IBM ContextForge (licence Apache 2.0; modèle de soutien non précisé par le projet)**[113]**; portails MCP de Cloudflare**[139]** |
| 1. Médiation et connectivité | Catalogue d’entreprise et registre privé | Source unique des outils, cartes et contrats; versions et empreintes; cycle de vie | Azure API Center; AgentCore Registry (publication, revue et approbation)**[102]**; Agent Registry de MuleSoft Agent Fabric |
| 1. Médiation et connectivité | Bus d’événements | Enveloppe CloudEvents, contrats AsyncAPI, rétention et rejeu | Apache Kafka, qui garantit par défaut une livraison au moins une fois**[140]**; services infonuagiques équivalents |
| 1. Outils et données | Serveurs MCP de domaine et adaptateurs | Outils conçus pour la tâche, effets déclarés, filtrage selon le mandant | Conversion d’API en outils par AgentCore Gateway, Azure API Management ou IBM ContextForge; serveur MCP Action Fabric de ServiceNow**[50]** |
| 1. Outils et données | Index et graphes de connaissances | Recherche hybride avec citations, provenance, validité temporelle | GraphRAG (génération augmentée par récupération sur graphe); Zep et Graphiti (section 5.5) |
| 1. Systèmes d’enregistrement | Systèmes existants | Contrôles métier conservés; corrélation des écritures | Aucun nouveau SBB : seuls des adaptateurs s’ajoutent |
| Plan A | Identité de charge de travail; serveur d’autorisation; moteur de politiques; coffre de secrets; garde-fous; service d’approbation humaine signée | Identité par agent, jetons délégués, décision par appel; secrets jamais exposés à l’agent (EXIG-SEC-14); approbation signée par une personne (section 8.5) | SPIFFE/SPIRE; Microsoft Entra Agent ID**[90]**; AgentCore Identity et AgentCore Policy (langage de règles compatible avec Cedar)**[102]**; coffre de secrets, garde-fous et service d’approbation : SBB à désigner à l’homologation (EXIG-ARC-20), sans exemple retenu ici |
| Plan B | Collecte et traitement de la télémétrie; évaluation; journal d’audit; budgets et quotas | Collecte OpenTelemetry, caviardage, évaluation continue; journal d’audit chaîné, signé et ancré (EXIG-OBS-12, EXIG-OBS-13); enveloppes et quotas de coûts (EXIG-FIN-04, EXIG-FIN-05) | OpenTelemetry Collector et son processeur de caviardage *(redaction)***[141]**; AgentCore Observability et Evaluations**[102]**; journal d’audit et budgets : SBB à désigner à l’homologation (EXIG-ARC-20), sans exemple retenu ici |
| Plan C | Registre et plan de contrôle des agents | Inventaire, quarantaine, cycle de vie, coupe-circuit | Microsoft Agent 365; ServiceNow AI Control Tower**[47, 51]**; AgentCore Registry; MuleSoft Agent Fabric |
| Couches 1 à 3 | Logiciel-service à agents intégrés | MCP et A2A natifs, identité par agent, télémétrie exportable; contrôles compensatoires de l’EXIG-ARC-21 (accès aux systèmes de l’entreprise par la passerelle, clauses contractuelles, arrêt propre) | Microsoft Copilot Studio (A2A en disponibilité générale depuis avril 2026; identité Entra Agent ID créée pour chaque nouvel agent)**[48]**; Salesforce Agentforce (A2A entrant et sortant, client et serveur MCP)**[49]**; ServiceNow AI Agent Fabric |

Les performances annoncées par les fournisseurs, comme celles d’agentgateway**[142]** et de TrueFoundry**[143, 144]**, ne remplacent pas une mesure (encadré de la section 9.4).

## 5.5 Mémoire des agents

Cette section distingue le contexte du modèle de la mémoire, définit quatre types de mémoire et fixe les contrôles qui encadrent leur écriture.

### Le contexte n’est pas une mémoire

Les fenêtres de contexte atteignent environ un million de jetons chez les modèles de pointe, par exemple GPT-5.4 d’OpenAI (mars 2026, 1,05 million) et Gemini 2.5 Pro ou Gemini 3 Pro de Google (1 million) de jetons**[145, 146, 147]**. Elles ne rendent pas la mémoire inutile, pour trois raisons. D’abord, la qualité baisse quand le contexte s’allonge : les modèles exploitent mieux l’information placée au début ou à la fin de l’entrée qu’au milieu, même lorsqu’ils sont conçus pour les longs contextes**[148]**. Anthropic décrit ce phénomène de « pourrissement du contexte » *(context rot)* : le rappel diminue à mesure que les jetons s’accumulent, et le contexte doit être traité comme une ressource finie**[149]**; une étude de Chroma sur 18 modèles montre qu’un seul distracteur suffit à réduire la performance**[150]**. Ensuite, chaque jeton réinjecté se paie à chaque appel. Enfin, le contexte disparaît à la fin de la session. La règle qui en découle : ce qui doit durer est persisté hors du modèle, puis récupéré au moment où il sert.

### Quatre types de mémoire

Le cadre reprend la taxonomie CoALA (Sumers et coll., 2024), qui distingue une mémoire de travail à court terme et trois mémoires à long terme : épisodique (expériences passées), sémantique (connaissances sur le monde et sur l’agent lui-même) et procédurale (savoir-faire)**[100]**. Pour CoALA, la mémoire procédurale comprend aussi les poids du modèle; l’ajustement des modèles étant hors de la portée du cadre, celui-ci la limite aux invites système, aux contrats de compétences et aux flux d’outils validés. LangChain applique la même grille : des faits sur l’utilisateur relèvent de la mémoire sémantique, des exemples tirés d’actions antérieures de la mémoire épisodique, et l’invite système de la mémoire procédurale**[151]**. La figure 4 et le tableau 13 en présentent l’organisation.

> **[Figure]**
> - Agent en cours d’exécution
> - 1 · Mémoire de travail
> - Fenêtre de contexte du modèle :
> - instructions, contrats d’outils,
> - sous-objectif, derniers échanges
> - État de la tâche persisté hors du
> - modèle à chaque transition (points
> - de contrôle du moteur durable)
> - Durée : la tâche · coût : chaque jeton
> - réinjecté est payé à chaque appel
> - Ce qui doit durer est persisté hors du modèle.
> - récupérer
> - consolider
> - 2 · Mémoire épisodique
> - Résumés horodatés des interactions, trajectoires d’outils et résolutions
> - passées; provenance consignée pour chaque entrée Calendrier de conservation · exposée en ressources ou outils MCP
> - 3 · Mémoire sémantique
> - Connaissances du domaine : index vectoriels et lexicaux, graphes de
> - connaissances, documentation; recherche hybride avec citations
> - Mise à jour par les propriétaires des données · exposée par MCP
> - 4 · Mémoire procédurale
> - Savoir-faire : invites système versionnées, contrats de compétences,
> - flux et séquences d’outils validés Gérée comme du code : revue, version, évaluation avant déploiement
> - Validation et provenance de la source · isolation par mandant ou par locataire (tableau 13) · expiration · instantanés restaurables
> - Interdits : état qui n’existe qu’en mémoire de processus · transcriptions brutes comme mémoire longue · magasin partagé en écriture entre plusieurs agents ou serveurs MCP
> - Contrôles obligatoires avant toute écriture en mémoire épisodique ou sémantique (EXIG-ARC-23); mémoire procédurale : changement logiciel (EXIG-ARC-24)

***Figure 4 — Quatre types de mémoire et contrôles d’écriture.** La mémoire de travail vit dans le contexte du modèle et dans les points de contrôle du moteur durable; les trois mémoires longues sont persistées hors du modèle et récupérées au besoin; les mémoires épisodique et sémantique sont protégées par les contrôles d’écriture de l’EXIG-ARC-23, la mémoire procédurale par le processus de changement logiciel (EXIG-ARC-24). Le tableau 13 fait foi pour l’isolation de chaque type. Source : cadre CRE-IA-2026-01, d’après la taxonomie CoALA (Sumers et coll., 2024).*

*Tableau 13 — Types de mémoire des agents et contrôles applicables*

| **Type** | **Contenu** | **Durée de vie** | **Exposition** | **Contrôles** |
| --- | --- | --- | --- | --- |
| Travail | Instructions, contrats d’outils, sous-objectif, derniers échanges; état de la tâche | La tâche; état persisté à chaque transition | Fenêtre de contexte; points de contrôle du moteur durable | Contexte minimal, compaction, aucun état qui n’existe qu’en mémoire de processus (EXIG-ARC-05) |
| Épisodique | Résumés horodatés des interactions, trajectoires d’outils, résolutions passées | Durée liée à la finalité, avec expiration par entrée (EXIG-CON-10) | Ressources ou outils MCP | Provenance de chaque entrée, filtrage des RP, isolation par locataire, par mandant et par serveur MCP, expiration par entrée (EXIG-ARC-23) |
| Sémantique | Connaissances du domaine : index vectoriels et lexicaux, graphes de connaissances, documentation | Tant que la source est valide | Ressources ou outils MCP; recherche hybride avec citations | Mise à jour par les propriétaires des données; isolation par locataire et par serveur MCP; filtrage en lecture selon les droits effectifs (EXIG-ARC-16); expiration avec la validité de la source (EXIG-ARC-23) |
| Procédurale | Invites système versionnées, contrats de compétences, flux et séquences d’outils validés | La version de l’agent | Déployée avec l’agent; inscrite au registre | Revue, version, évaluation avant déploiement; aucune modification par l’agent |

### Écrire en mémoire longue

L’écriture peut se faire dans le chemin critique, en temps réel (transparente, mais plus lente), ou en arrière-plan (sans latence, mais avec une fréquence à choisir)**[151]**. Le cadre accepte les deux modes, à condition qu’ils passent par les mêmes contrôles. En arrière-plan, le tampon des transcriptions en attente de consolidation porte l’identité du mandant captée pendant la session, est chiffré, a une durée de rétention maximale déclarée à la fiche et est purgé après la consolidation. Anthropic, pour son outil mémoire exécuté côté client, exige de valider chaque chemin d’accès contre la traversée de répertoires et recommande de filtrer les données sensibles avant l’écriture, de plafonner la taille des fichiers et de supprimer les mémoires longtemps inutilisées**[152]**. Les renseignements personnels conservés en mémoire sont détruits ou anonymisés une fois leurs fins accomplies, comme l’exige l’article 23 de la Loi sur la protection des renseignements personnels dans le secteur privé (RLRQ, c. P-39.1, ci-après « Loi sur le privé ») (EXIG-CON-10, section 12.2).

`EXIG-ARC-22` **· NE DOIT PAS**

**Pas d’historique brut comme mémoire**

L’historique brut des échanges **NE DOIT PAS** être réinjecté dans le contexte du modèle au-delà de la borne de contexte, exprimée en jetons, que déclare la fiche de l’agent (annexe B), ni conservé tel quel comme mémoire longue. Au-delà de cette borne, l’historique est compacté; ce qui doit durer est consolidé (résumé, fait, décision), persisté hors du modèle et récupéré au besoin.

Pourquoi : un historique brut coûte à chaque appel, dégrade le rappel et accumule du bruit sans limite.

`EXIG-ARC-23` **· DOIT**

**Contrôles avant toute écriture en mémoire épisodique ou sémantique**

Toute écriture en mémoire épisodique ou sémantique **DOIT** passer par des contrôles qui consignent la provenance de l’entrée, valident sa source, retirent les secrets et les renseignements personnels non nécessaires et permettent de restaurer un instantané antérieur. En mémoire épisodique, l’entrée est en outre isolée par locataire, par mandant et par serveur MCP, et porte une date d’expiration (EXIG-CON-10). En mémoire sémantique, connaissance partagée du domaine, elle est isolée par locataire et par serveur MCP, filtrée en lecture selon les droits effectifs (EXIG-ARC-16) et expire avec la validité de sa source. Valider la source d’un résumé produit par un modèle, c’est le contrôler contre un schéma qui fixe les champs admis et exclut le texte libre issu des outils. Une entrée écrite par une session marquée porte l’étiquette de cette session (EXIG-SEC-04); toute entrée relue est un contenu non fiable (EXIG-SEC-03), et l’outil de mémoire est marqué au catalogue.

Pourquoi : une information fausse inscrite en mémoire oriente toutes les décisions suivantes; l’OWASP en fait un risque distinct, l’empoisonnement de la mémoire et du contexte (ASI06 *Memory & Context Poisoning*)**[28]**.

`EXIG-ARC-24` **· DOIT**

**Mémoire procédurale gérée comme du code**

Toute modification de la mémoire procédurale (invites système, contrats de compétences, flux et séquences d’outils validés) **DOIT** suivre le processus de changement logiciel : revue, version, évaluation avant déploiement et inscription au registre. Un agent **DOIT** être privé de tout droit d’écriture sur sa propre mémoire procédurale en production.

Pourquoi : CoALA juge l’écriture en mémoire procédurale nettement plus risquée que l’écriture épisodique ou sémantique**[100]**; elle change le comportement de l’agent pour toutes les tâches à venir, comme un déploiement de code.

`EXIG-ARC-25` **· NE DOIT PAS**

**Aucun magasin de mémoire longue partagé en écriture**

Une mémoire longue **NE DOIT PAS** être accessible en écriture directe à plus d’un composant, agent ou serveur MCP; le partage passe par des ressources en lecture seule ou par un service de mémoire qui applique les contrôles de l’EXIG-ARC-23, n’accepte que des écritures conditionnelles (ETag ou numéro de version) et tient un journal des écritures. Chaque écrivain direct a sa propre identité de charge de travail et son propre espace de noms dans le magasin.

Pourquoi : le Centre d’architecture Azure proscrit le partage d’état mutable entre agents concurrents**[9]**; un magasin partagé permet à un composant compromis d’empoisonner tous les autres.

**ANTI-PATRONS PROSCRITS**

- Conserver un état qui n’existe qu’en mémoire de processus : le *checkpointer* en mémoire de LangGraph, par exemple, perd ses points de contrôle au redémarrage**[124]**.
- Archiver les transcriptions brutes comme mémoire longue.
- Partager en écriture une table de mémoire entre plusieurs agents ou serveurs MCP.
- Stocker des secrets, des jetons ou des approbations dans le contexte du modèle ou en mémoire longue (l’état d’orchestration ne conserve qu’une référence à l’approbation signée et au jeton, dans le magasin protégé de l’EXIG-ARC-06).
- Laisser un agent réécrire ses propres invites système ou contrats de compétences.

Plusieurs technologies réalisent ces rôles; elles sont citées à titre d’exemples non normatifs. LangGraph sépare les *checkpointers*, qui conservent l’état par fil d’exécution, d’un magasin distinct pour la mémoire à long terme partagée entre fils**[124]**. Letta maintient le patron MemGPT, qui déplace l’information entre le contexte et un stockage externe à la manière d’une mémoire virtuelle**[153, 154]**. Zep s’appuie sur Graphiti, un graphe de connaissances temporel qui conserve l’historique des relations, utile pour l’audit puisqu’on peut savoir à quel moment un fait était vrai**[155]**. GraphRAG construit un graphe d’entités et des résumés de communautés qui aident à répondre aux questions de synthèse sur un vaste corpus**[156]**. Le cadre ne fixe ni produit ni latence cible : ces paramètres se mesurent dans l’environnement de l’entreprise.

## 5.6 Parcours d’une demande de bout en bout

Cette section suit une demande à travers les six couches pour montrer comment les règles s’enchaînent. Exemple : une conseillère du service à la clientèle demande l’émission d’un avoir de 1 200 $ sur la facture d’un client. L’agent de facturation est de classe de risque modérée, plafonné au niveau N3, car aucun avoir qu’il peut émettre n’excède le seuil de classe que la fonction risques et conformité arrête pour lui (tableau

46); l’outil `emettre_avoir` est de palier P2 (écriture réversible), et le catalogue lui fixe un seuil d’exécution autonome de 500 $, valeur propre à l’exemple et distincte du seuil de classe.

1. **Canal.** La conseillère formule sa demande dans l’outil de collaboration. Le canal l’authentifie, établit le mandant, ouvre la trace et transmet l’intention sans la transformer (EXIG-ARC-03, EXIG-ARC-04).
2. **Routage.** Le routeur qualifie l’intention (« émettre un avoir ») et choisit le flux déterministe de traitement des avoirs inscrit au catalogue d’entreprise, plutôt qu’un agent libre; ce choix ne confère aucun droit (EXIG-ARC-07).
3. **Ouverture de la tâche.** Le moteur d’exécution durable crée la tâche, lui attribue son enveloppe budgétaire (jetons, coût, appels d’outils, délai) et obtient pour l’agent un jeton délégué au nom de la conseillère, destiné à la passerelle (section 9.3); l’état est persisté.
4. **Raisonnement.** L’étape d’analyse invoque l’agent de facturation, qui appelle son modèle par la passerelle de modèles; celle-ci résout l’alias, applique les quotas et impute jetons et coût au centre de coûts (EXIG-ARC-08, EXIG-ARC-09).
5. **Lecture.** L’agent appelle l’outil MCP `consulter_situation_compte` (palier P1) par la passerelle d’agents, qui vérifie le catalogue, obtient en tant que client, par échange de jetons (RFC 8693, paramètre `resource` de la RFC 8707), un jeton à audience unique pour ce serveur, et propage la trace; l’outil filtre ses résultats selon les droits de la conseillère (EXIG-ARC-16).
6. **Délégation éventuelle.** Si une vérification relève d’un autre domaine, la conformité par exemple, une branche du flux, déclarée au registre, délègue la sous-tâche par A2A à l’agent de ce domaine, toujours par la passerelle; la séquence détaillée figure à la section 6.6.
7. **Approbation.** L’agent prépare l’appel à `emettre_avoir`. Le montant, calculé par la passerelle à partir des arguments, dépasse le seuil déclaré : le moteur suspend la tâche, état persisté, et l’action exacte est présentée à une approbatrice, dont la décision produit un jeton signé lié à cette action, remis à la passerelle et jamais à l’agent (section 8.5).
8. **Écriture.** Le moteur reprend la tâche, et l’agent rejoue l’appel avec sa clé d’idempotence et la référence de la demande d’approbation. La passerelle obtient un nouveau jeton délégué, ce qui revérifie les droits actuels de la conseillère (EXIG-IAM-02), apparie à l’appel le jeton d’approbation qu’elle conserve et le relaie; l’approbation sépare les tâches sans ajouter de droit, et la conseillère doit détenir elle-même le droit d’émettre l’avoir; le serveur MCP de facturation appelle l’API de l’ERP, qui applique ses propres contrôles et enregistre l’avoir avec la référence de trace (EXIG-ARC-17, EXIG-ARC-18).
9. **Résultat ou compensation.** L’artefact remonte au canal, et la conseillère reçoit la confirmation, avec la référence d’audit, une fois la dernière étape compensable terminée. Si une étape ultérieure échoue avant ce point sans reprise possible, le moteur exécute la compensation déclarée, ici l’annulation de l’avoir, sous l’identité de compensation de l’orchestrateur (EXIG-ORC-28), et en avise la conseillère et l’approbatrice (section 7.5).
10. **Audit et apprentissage.** Le journal d’audit consigne le mandant, l’agent et sa version, le modèle, l’outil et l’empreinte de ses arguments, ainsi que l’approbation (section 10.3). Les traces alimentent l’évaluation continue et le coût par tâche réussie; un résumé validé de la résolution entre en mémoire épisodique (EXIG-ARC-23).

**À RETENIR**

Trois éléments descendent avec chaque appel : le mandant, le contexte de trace et la part restante de l’enveloppe de la tâche. Trois éléments remontent : le résultat, ses artefacts et les mesures de coût et de qualité. En environnement serveur, aucun appel MCP ou A2A, quel que soit le domaine, ni aucune

action P2 ou P3 n’échappe à la passerelle, et aucune écriture n’atteint un système d’enregistrement sans ses propres contrôles métier.
