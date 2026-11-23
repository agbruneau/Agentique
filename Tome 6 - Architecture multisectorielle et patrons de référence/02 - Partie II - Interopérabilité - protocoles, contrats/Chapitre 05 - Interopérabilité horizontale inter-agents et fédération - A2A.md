# Chapitre 5 — Interopérabilité horizontale inter-agents et fédération : A2A, AGNTCY et maillage multi-fournisseurs

Le chapitre précédent a établi comment le protocole vertical `MCP` normalise l’accès d’un agent unitaire aux outils et aux `Systems of Record` (`SoR`) d’un domaine. Dès qu’une chaîne de valeur franchit la frontière d’un département, d’une filiale ou d’un partenaire externe, cette intégration verticale atteint sa limite structurelle : un orchestrateur ne peut importer directement les outils bruts, les schémas privés ou les invites d’un système voisin sans briser le cloisonnement organisationnel ni la souveraineté métier [77] [78]. L’interopérabilité horizontale répond à ce basculement en remplaçant l’appel d’outil passif par une délégation contractuelle entre pairs autonomes opaques, portée par des standards ouverts sous la gouvernance neutre de la Linux Foundation et de l’*Agentic AI Foundation* (`AAIF`) [78] [79] [80].

Pour l’architecte d’entreprise (**EA**), l’enjeu consiste à prévenir la reconstitution de silos propriétaires entre agents SaaS achetés et agents assemblés en interne, tout en préservant l’imputabilité, la réversibilité du portefeuille et la maîtrise des coûts inter-domaines [78] [81]. Pour l’architecte de solutions (**SA**), le défi porte sur des contrats asynchrones capables d’absorber les délais variables, les interruptions humaines, la traversée des pare-feu, la diversité des cadriciels et les menaces propres aux échanges inter-agents [82] [83] [84]. Ce chapitre couvre exclusivement les contrats, annuaires, protocoles de session et ponts inter-agents ; les patrons algorithmiques de coordination multi-agents relèvent du chapitre 7.

## 5.1 Frontière décisionnelle entre outil passif (`MCP`) et pair autonome opaque (`A2A`)

### 5.1.1 Orthogonalité des axes vertical et horizontal

Traiter `Model Context Protocol` (`MCP`) et `Agent-to-Agent` (`A2A`) comme des standards concurrents constitue une erreur de conception fréquente. La spécification officielle d’`A2A` établit une complémentarité orthogonale entre deux axes [77]. Sur l’axe vertical, `MCP` confère de la profondeur à un agent individuel en le reliant à ses ressources déterministes, bases de données et fonctions utilitaires [77]. Sur l’axe horizontal, `A2A` donne de la portée au système d’information en permettant à des agents indépendants — relevant d’équipes, de nuages ou d’entreprises distinctes — de se découvrir, de négocier des modalités d’échange et de collaborer sur des tâches complexes en tant que pairs [82] [77].

Dans une topologie de référence, les deux axes s’emboîtent de façon récursive sans exposer les mécanismes internes d’un domaine à l’autre [77] [85]. Un orchestrateur client sollicite un pair spécialiste externe via `A2A` [77] [81]. Ce pair agit comme serveur `A2A` à sa frontière, mais exécute ses opérations métier en invoquant ses propres outils et `SoR` cloisonnés via des clients et passerelles `MCP` privés [77]. Comme le montre le retour d’architecture de Salesforce pour `Agentforce`, brancher directement des dizaines d’outils `MCP` hétérogènes dans un agent central unique sature sa fenêtre contextuelle, dégrade la précision du choix d’outils et crée un couplage inter-domaines rigide [86].

> **[Figure]**
> - Domaine A — Client
> - [system]
> - Frontière inter-domaines
> - [system]
> - Domaine B / SaaS — Pair
> - opaque
> - [system]
> - «container» Agent orchestrateur A
> - [Agent Harness]
> - Planifie et délègue
> - «container» MCP Gateway A
> - [Serveurs MCP]
> - Outils typés sans état
> - «container» SoR Domaine A
> - [ERP / CRM]
> - Données locales
> - «container» Passerelle API / A2A
> - [HTTPS + OAuth 2.0]
> - JWS, portées, quotas et traces
> - «container» Serveur A2A B
> - [AgentCard + Tasks]
> - Boîte noire : prompts et mémoire privés
> - «container» MCP privé B [Outils encapsulés]
> - Invisibles pour A
> - «container» SoR Domaine B
> - [SI partenaire]
> - Autorité cloisonnée
> - Horizontal : Task A2A
> - (HTTPS / JWS)
> - Délégation contrôlée
> - (JSON-RPC / gRPC)
> - Vertical : outils
> - (MCP)
> - Accès (Idempotent)
> - Vertical : outils
> - (MCP privé)
> - Exécution (Domaine B)

*Fig. 17. – Dualité verticale MCP et horizontale A2A entre domaines opaques*

Pour le `SA`, la démarcation entre `MCP` et `A2A` repose sur trois critères observables. Premièrement, l’**autonomie décisionnelle** : un outil `MCP` exécute une primitive bornée sans planification propre, alors qu’un pair `A2A` raisonne, planifie, enchaîne plusieurs outils internes et maintient un état conversationnel multi-tours [82] [77]. Deuxièmement, le **régime temporel** : l’appel d’outil vise un retour bref, tandis qu’une `Task` `A2A` est nativement asynchrone sur des minutes, des heures ou des jours [82] [87]. Troisièmement, l’**isolation contextuelle** : `MCP` injecte les définitions d’outils dans le contexte de l’agent appelant, alors qu’`A2A` préserve le cloisonnement hermétique des invites et de la mémoire du pair appelé [82] [85].

### 5.1.2 Principe d’exécution opaque : propriété intellectuelle et gouvernance

La spécification `A2A` érige l’exécution opaque (*opaque execution*) en principe fondateur [82]. Un client `A2A` collabore avec un serveur distant uniquement au travers des capacités déclarées dans son manifeste public, des messages échangés et des livrables (`Artifacts`) retournés, sans accéder ni à ses instructions internes, ni à ses plans d’exécution, ni à ses outils privés [82] [85]. Ce principe protège la propriété intellectuelle des algorithmes métier, préserve la confidentialité des règles d’arbitrage et réduit la surface d’exposition des `SoR` sous-jacents [85] [78].

Pour l’`EA`, l’opacité contractuelle matérialise le découplage du Plan 3 introduit au chapitre 2. Chaque domaine conserve la pleine gouvernance de ses agents, du choix de ses modèles d’inférence et de ses contrôles d’accès aux données [85]. Une équipe peut remplacer son cadriciel interne sans rompre ses consommateurs tant que le contrat `AgentCard` et le schéma des `Artifacts` restent compatibles [82] [78]. À l’inverse, partager une mémoire vectorielle brute ou exposer directement des outils internes entre domaines ouvre la voie aux mouvements latéraux et à la propagation de données empoisonnées recensés par l’OWASP [84].

### 5.1.3 Arbitrage entre API déterministe, outil `MCP`, ressource hybride et pair `A2A`

Toutes les interactions inter-systèmes ne relèvent pas d’un protocole cognitif. Les guides d’ingénierie de Salesforce et Microsoft convergent sur une règle de parcimonie : lorsque l’échange suit des règles stables, manipule des données structurées et exige un haut débit prévisible, une API REST ou gRPC déterministe surpasse toute médiation agentique en latence et en coût [88] [86].

La documentation officielle d’`A2A` reconnaît toutefois un cas hybride : exposer une compétence d’un serveur `A2A` comme ressource ou outil `MCP` [77]. Ce compromis n’est valide que pour une compétence aux paramètres fermés, exécutable en un tour sans état ni interaction `INPUT_REQUIRED`, et dans une même frontière de confiance [77]. Dès que la tâche exige négociation, authentification secondaire ou suivi progressif, forcer un pair autonome dans un appel d’outil synchrone provoque des expirations et des pertes d’état [77] [87].

| Critère architectural | API déterministe (`REST` / `gRPC`) | Outil passif (`MCP`) | Pair autonome opaque (`A2A`) |
| --- | --- | --- | --- |
| Axe d’intégration | Code à code déterministe | Vertical : agent vers outils locaux | Horizontal : agent vers pair autonome [77] |
| Contrat et découverte | Contrat statique OpenAPI / Protobuf | Schéma `JSON` d’outil injecté dans le prompt [86] | `AgentCard` JSON signée via `.well-known` ou registre [82] |
| Opacité d’exécution | Boîte noire logicielle figée | Schéma explicite d’opération atomique [77] | Boîte noire cognitive : prompts, mémoire et outils masqués [82] |
| État et horizon temporel | Sans état (requête-réponse brève) | Sans état ou session courte [77] | `Task` à états (`contextId` + `taskId`), minutes à jours [82] [87] |
| Modes de livraison | Synchrone ou flux RPC typé | Appel synchrone ou progression courte | Bloquant, flux `SSE` et webhooks déconnectés [82] [87] |
| Gouvernance EA / SA | API Management et SLA technique | `MCP Gateway` avec contrôle de dérive [86] | Signatures `JWS`, mandats inter-domaines et isolement [82] [85] |

*Tableau 5.1 — Matrice décisionnelle comparant l’API déterministe, l’outil passif* `MCP` *et le pair autonome opaque* `A2A`*.*

L’arbre de décision suivant systématise ce tri en quatre paliers avant d’ouvrir une nouvelle interface inter-agents [83] [86].

*Fig. 18. – Arbre de décision entre API déterministe, MCP, A2A sur HTTP et pile fédérée AGNTCY*

> **Arbitrage EA / SA** — Imposer l’opacité inter-domaines comme invariant architectural : interdire à tout agent d’invoquer directement les serveurs `MCP` privés d’un autre domaine ou d’un partenaire externe [77] [85]. L’`EA` confine `MCP` à la profondeur locale de chaque domaine et impose `A2A` pour toute délégation cognitive inter-frontières [77] [78] ; le `SA` n’autorise l’exposition d’une compétence `A2A` en ressource `MCP` que pour des opérations idempotentes à tour unique, tout en maintenant les flux déterministes à haut volume sur des API classiques [77] [86].

## 5.2 Protocole `A2A` : `Agent Cards` signées, cycle de vie asynchrone des `Tasks`, SSE et `Artifacts`

### 5.2.1 Architecture normative en trois couches et liaisons protocolaires

Conçu par Google Cloud puis confié à la Linux Foundation avec le concours de plus de 150 organisations, le protocole `A2A` a atteint la maturité `v1.0.0` et dispose de SDK en Python, JavaScript, Java, Go et .NET [82] [78] [79]. La spécification s’articule en trois couches strictement découplées [82] :

1. **Couche 1 — Modèle de données canonique (**`spec/a2a.proto`**)** : les structures normatives (`Task`, `Message`, `AgentCard`, `Part`, `Artifact`, `Extension`) sont définies en Protocol Buffers pour empêcher toute divergence entre langages [82].
2. **Couche 2 — Opérations abstraites** : onze opérations forment le contrat fonctionnel commun (`SendMessage`, `SendStreamingMessage`, `GetTask`, `ListTasks`, `CancelTask`, `SubscribeToTask`, les quatre opérations sur `TaskPushNotificationConfig` et `GetExtendedAgentCard`) [82].
3. **Couche 3 — Liaisons protocolaires** : les agents exposent ces opérations via `JSON-RPC 2.0` sur HTTP(S), `gRPC` ou `HTTP+JSON/REST`, tout serveur multi-liaisons devant garantir une équivalence sémantique exacte et un mappage uniforme des erreurs (`-32001` à `-32009` en JSON-RPC alignés sur les statuts gRPC et HTTP) [82].

Dans les sérialisations JSON, la version `v1.0.0` prescrit la notation `camelCase` pour les champs (`contextId`, `protocolVersion`, `defaultInputModes`), la convention `ProtoJSON` `SCREAMING_SNAKE_CASE` pour les énumérations (`TASK_STATE_WORKING`, `ROLE_USER`) et le format ISO 8601 UTC (`Z`) pour les horodatages [82]. Les paramètres transverses `A2A-Version` et `A2A-Extensions` voyagent dans les en-têtes HTTP ou métadonnées gRPC plutôt que dans le corps JSON [82]. Pour le `SA`, cette séparation permet aux passerelles réseau d’appliquer routage, limitation de débit et propagation `W3C Trace Context` sans désérialiser les charges utiles applicatives [82] [85].

### 5.2.2 Découverte via `AgentCard`, canonisation `RFC 8785` et signature `JWS`

Tout serveur `A2A` publie son manifeste descriptif `AgentCard`, découvrable via l’URI normalisée `https://{domaine}/.well-known/agent-card.json`, un catalogue central ou une configuration directe [82] [89]. L’`AgentCard` déclare obligatoirement l’identité (`name`, `description`, `version`), la liste ordonnée des interfaces (`supportedInterfaces` précisant URL, `protocolBinding`, `protocolVersion` et `tenant` éventuel), les capacités (`streaming`, `pushNotifications`, `extendedAgentCard`, `extensions`), les types MIME par défaut (`defaultInputModes`, `defaultOutputModes`) et le catalogue de compétences (`skills` de type `AgentSkill`, dotés de `tags` descriptifs) [82].

Pour différencier les droits d’accès selon l’appelant, la carte publique ne divulgue que les schémas d’authentification (`securitySchemes` alignés sur OpenAPI et `securityRequirements`) [82] [85]. Après authentification hors bande (OAuth 2.0 ou OpenID Connect), le client appelle `GetExtendedAgentCard` pour obtenir des compétences réservées ou des quotas dédiés, sans jamais exposer d’URL internes ni de secrets [82]. Côté trafic réseau, serveurs et clients doivent exploiter la mise en cache HTTP (`RFC 9111`) via `Cache-Control`, `ETag` et `If-None-Match` [82].

Pour bloquer l’usurpation de manifestes et le détournement d’endpoints (`OWASP ASI07`) [84], la spécification `v1.0.0` formalise la signature cryptographique de l’`AgentCard` dans le champ `signatures` (`AgentCardSignature`) au format *JSON Web Signature* (`JWS`, `RFC 7515`) [82]. La vérification obéit à une séquence déterministe stricte [82] :

1. **Normalisation des champs et exclusion de** `signatures` : les champs `optional` non renseignés et les valeurs par défaut implicites sont omis (tout en conservant les champs `REQUIRED` et les champs `optional` explicitement définis), puis le tableau `signatures` est retiré avant signature [82].
2. **Canonisation déterministe (**`JCS`**,** `RFC 8785`**)** : l’objet JSON épuré est trié lexicographiquement par clé et débarrassé de tout espace superflu afin d’assurer un condensat reproductible entre langages [82].
3. **Vérification via en-tête protégé et** `JWKS` : l’en-tête JWS protégé déclare `alg` (par exemple `ES256` ou `RS256`), `typ` (`JOSE`) et `kid` (ainsi que `jku` en HTTPS vers le jeu de clés publiques), ce qui autorise la coexistence de plusieurs signatures durant une rotation de clés [82].

Pour l’`EA`, la validation JWS conditionne toute approbation d’agents découverts via un annuaire partagé : le seul certificat TLS du domaine hôte ne prémunit pas contre la falsification d’une fiche mise en cache chez un courtier tiers [82] [84].

### 5.2.3 Cycle de vie asynchrone des `Tasks`, états interrompus et reprise multi-tours

Dans `A2A`, l’unité de travail persistante est la `Task`, identifiée par un `id` serveur et regroupée par un `contextId` partagé sur toute une conversation collaborative [82] [87]. Si une requête triviale peut recevoir un simple `Message` direct, toute opération multi-étapes produit une `Task` régie par un automate à neuf états (`TaskState`) [82] :

- **États actifs** : `TASK_STATE_SUBMITTED` et `TASK_STATE_WORKING` [82].

- **États interrompus** : `TASK_STATE_INPUT_REQUIRED` (attente d’une information complémentaire ou d’une validation humaine) et `TASK_STATE_AUTH_REQUIRED` (suspension jusqu’à obtention hors bande d’une accréditation secondaire pour un outil ou service aval) [82] [85].
- **États terminaux immuables** : `TASK_STATE_COMPLETED`, `TASK_STATE_FAILED`, `TASK_STATE_CANCELED` et `TASK_STATE_REJECTED` (ainsi que `TASK_STATE_UNSPECIFIED`) [82].

Dès qu’une `Task` atteint un état terminal, elle devient immuable : tout message envoyé vers son `taskId` échoue avec `UnsupportedOperationError` (`-32004`) [82] [90]. Un nouveau tour dans la même session doit créer une nouvelle `Task` liée par le même `contextId` et, au besoin, `referenceTaskIds` [82] [90]. Pour éviter la surcharge mémoire et réseau lors du suivi de longues sessions, `GetTask` et `ListTasks` supportent le plafonnement d’historique (`historyLength`), la pagination par curseur (`pageToken` /`nextPageToken`) triée par dernière mise à jour décroissante, et l’exclusion par défaut des livrables (`includeArtifacts: false`) [82].

> **[Figure]**
> - Client A2A (Domaine A)
> - Endpoint Well-Known / JWKS
> - Serveur A2A
> - (Pair B)
> - Récepteur Webhook
> - (Domaine A)
> - Client A2A (Domaine A)
> - Endpoint Well-Known / JWKS
> - Serveur A2A
> - (Pair B)
> - Récepteur Webhook
> - (Domaine A)
> - 1. Découverte et vérification cryptographique (RFC 8785 + RFC 7515)
> - 1 GET /.well-known/agent-card.json
> - 2 AgentCard JSON + signatures[] (JWS ES256)
> - 3 GET jwks.json (clé publique selon kid)
> - 4 JWKS (vérification JCS RFC 8785 + JWS)
> - 2. Cycle asynchrone SSE et interruption multi-tours
> - 5 SendStreamingMessage (Authorization: Bearer, contextId)
> - 6 HTTP 200 text/event-stream : Task (SUBMITTED)
> - 7 TaskStatusUpdateEvent (TASK_STATE_WORKING)
> - 8 TaskStatusUpdateEvent (INPUT_REQUIRED) + Artifact Interrupt
> - Le flux SSE se ferme sur état interrompu. Validation ou précision requise.
> - 9 SendMessage (taskId, contextId, DataPart resume)
> - 10 TaskArtifactUpdateEvent (append: true, lastChunk: true)
> - 1 1 TaskStatusUpdateEvent (TASK_STATE_COMPLETED)
> - 3. Tâche longue en mode déconnecté (Push Notification)
> - 12 SendMessage (returnImmediately: true, TaskPushNotificationConfig)
> - 13 Task (TASK_STATE_WORKING, taskId)
> - Traitement autonome différé (minutes ou heures)
> - 14 HTTP POST webhook URL (Bearer token, StreamResponse)
> - 15 HTTP 200 OK (traitement idempotent)
> - 16 GetTask (id: taskId)
> - 17 Task (TASK_STATE_COMPLETED + Artifacts finaux)

*Fig. 19. – Séquence protocolaire A2A v1.0 : AgentCard signée, SSE, interruption et webhook*

### 5.2.4 Livraison asynchrone : flux `SSE`, webhooks et structure multimodale des `Artifacts`

La spécification `A2A` couvre trois régimes temporels via le champ `returnImmediately`, les flux continus et les webhooks [82] [87]. Par défaut (`returnImmediately: false`), `SendMessage` bloque jusqu’à un état terminal ou interrompu ; à `true`, il retourne aussitôt la `Task` active, déléguant le suivi au client [82].

Sur des durées interactives, `SendStreamingMessage` ouvre un flux *Server-Sent Events* (`text/event-stream`) qui émet d’abord l’objet `Task` initial, puis une série de `StreamResponse` alternant `TaskStatusUpdateEvent` et `TaskArtifactUpdateEvent` [82] [87]. Chaque `Artifact` agrège un ou plusieurs objets `Part` mutuellement exclusifs (`oneOf` : `text`, `raw` en octets Base64, `url` de fichier ou `data` JSON structuré) typés par `mediaType` MIME [82]. L’assemblage incrémental des livrables volumineux s’appuie sur les indicateurs `append` et `lastChunk` [82] [87]. En cas de rupture réseau avant un état terminal ou interrompu, `SubscribeToTask` rétablit le flux en commençant impérativement par l’état courant complet de la `Task` afin d’éliminer toute perte d’événement entre interrogation et réabonnement [82].

Lorsque les délais atteignent plusieurs heures ou impliquent des clients sans serveur persistant, le client fournit une `TaskPushNotificationConfig` (URL HTTPS, jeton unique et schéma `AuthenticationInfo`) [82] [87]. Comme le serveur `A2A` initie alors des requêtes HTTP `POST` sortantes, la section 13.2 impose une protection stricte contre la falsification de requête côté serveur (`SSRF`) : rejet des réseaux privés (`127.0.0.0/8`, `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), de `localhost` et des adresses de lien local, listes blanches de domaines, délais d’attente de 10 à 30 secondes et tentatives à backoff exponentiel [82] [87]. Le récepteur webhook doit pour sa part valider les identifiants, vérifier la correspondance du `taskId`, traiter les notifications de manière idempotente et récupérer les livrables via `GetTask` [82] [87].

> **Arbitrage EA / SA** — Proscrire tout appel `SendMessage` bloquant au-delà de quelques secondes depuis le `SoE` et exiger la signature JWS (`RFC 7515` + `RFC 8785`) sur toute `AgentCard` exposée hors d’une enclave privée [82] [87]. Le `SA` sélectionne `SendStreamingMessage` (`SSE` + `SubscribeToTask`) pour les dialogues interactifs et `returnImmediately: true` avec webhooks `TaskPushNotificationConfig` durcis anti-SSRF pour les traitements différés [82] [87] ; l’`EA` vérifie que `ListTasks` applique un cloisonnement strict par locataire (`tenant`) et que toute autorisation ou refus d’accès reste auditable [82] [85].

## 5.3 Infrastructure fédérée `AGNTCY` : schémas `OASF`, `Agent Directory Service` et messagerie `SLIM` /`MLS`

### 5.3.1 Limites d’un maillage `A2A` purement HTTP à l’échelle fédérée

À l’échelle d’une fédération multi-organisations ou d’essaims dynamiques d’agents, le recours exclusif à `A2A` sur HTTP/HTTPS rencontre trois limites structurelles [91] [92] [83] :

1. **Absence de requête sémantique multi-critères** : l’accès à `/.well-known/agent-card.json` suppose de connaître le domaine cible et ne permet pas d’interroger un annuaire distribué par intersection de compétences, de domaines réglementaires et de traits techniques [91].
2. **Contrainte d’exposition entrante (**`NAT` **/ pare-feu)** : HTTP et gRPC classiques attendent un point d’écoute joignable par le client, compliquant le déploiement d’agents derrière des pare-feu d’entreprise ou en périphérie sans tunnel sur mesure [92] [83].

3. **Chiffrement saut-par-saut et absence de groupe dynamique** : `TLS` se termine aux répartiteurs et passerelles intermédiaires qui accèdent aux charges en clair, et le chiffrement point-à-point ne passe pas à l’échelle pour des groupes multi-agents dynamiques [92] [83] [93].

Versé à la Linux Foundation après son lancement par Cisco Outshift, l’écosystème `AGNTCY` fournit ces trois briques complémentaires — schéma fédéré, annuaire décentralisé et plan de messagerie chiffré — compatibles aussi bien avec `A2A` qu’avec `MCP` [78] [94] [91] [95].

### 5.3.2 Modélisation unifiée par schémas `OASF`

L’*Open Agentic Schema Framework* (`OASF`), dérivé de l’*Open Cybersecurity Schema Framework* (`OCSF`), définit l’objet `record` comme représentation normalisée et extensible d’un agent [94]. Là où les `tags` d’une `AgentSkill` `A2A` demeurent des chaînes libres [82], `OASF` structure la description autour de trois axes taxonomiques typés [94] [91] :

- **Compétences (**`skills`**)** : chemins hiérarchiques pointés (comme `nlp.summarization.abstractive`) à profondeur bornée (`≤ 4`) et versionnement sémantique monotone afin de maîtriser la complexité d’indexation [91].
- **Domaines (**`domains`**)** : contexte métier, linguistique ou réglementaire (tel que `healthcare` ou `finance.retail`) [91].
- **Modules et traits (**`modules` **/** `features`**)** : extensions plates et descripteurs protocolaires (`A2A`, `MCP`, signaux d’évaluation), identifiés par un triplet unique `(namespace, name, version)` pour éviter toute collision entre extensions privées d’entreprise validées sur un serveur `OASF` dédié [94] [91].

Pour l’`EA`, `OASF` devient le pivot sémantique du registre de portefeuille : un seul modèle de fiche indexe des agents issus de plusieurs éditeurs sans dépendre de leurs métadonnées propriétaires [94] [91].

### 5.3.3 Annuaire fédéré `ADS` : stockage `OCI` /`ORAS`, `Kademlia DHT` et provenance `Sigstore`

L’*Agent Directory Service* (`ADS`, dépôt `agntcy/dir`) opérationnalise `OASF` sous forme d’un annuaire distribué qui dissocie l’indexation des capacités de la localisation physique par un mappage à deux niveaux [91]. Le premier niveau associe les attributs taxonomiques à des identifiants de contenu immuables (`CID` calculés en `SHA-256`) ; le second niveau associe chaque `CID` aux registres hébergeant l’artefact [91]. Toute recherche multi-axes doit comporter au moins une compétence (`skill`) afin de préserver la localité d’index et d’éviter l’explosion combinatoire [91].

Sur le plan du stockage et de la sécurité de chaîne d’approvisionnement, `ADS` réutilise l’infrastructure mature des registres `OCI` (tels que *Zot*) et d’`ORAS` sur stockage objet (`S3`, `GCS`, `Azure Blob`) [91]. Les fiches `OASF` sont stockées comme manifestes `OCI` immuables, auxquels les signatures cryptographiques, jeux d’évaluation et graphes de composition se rattachent en tant que référents `OCI` sans altérer le condensat initial [91]. La provenance s’appuie sur `Sigstore` sans nécessiter de tiers de confiance central, tandis que la fédération inter-organisations repose sur une table de hachage distribuée `Kademlia` (`DHT`) offrant trois stratégies de réplication : tirage à la demande (*On-Demand Cross-Pull*), réplication sélective et ancrage stratégique multi-juridictionnel [91].

> **[Figure]**
> - Découverte fédérée (OASF
> - + ADS)
> - [system]
> - Transport et session (SLIM
> - + MLS RFC 9420)
> - [system]
> - «container» Annuaire Kademlia DHT
> - [ADS (agntcy/dir)]
> - Index 2 niveaux : Skill -> CID -> Pair
> - «container» Registre OCI / ORAS
> - [SHA-256 + Sigstore]
> - Records immuables
> - et référents signés
> - «container» Descripteur OASF
> - [Schema Record]
> - Skills, domaines, locators A2A/MCP
> - «container» Endpoint Agent A
> - [SLIM SDK + SPIRE]
> - Derrière NAT, session MLS E2E
> - «container» Nœuds Data Plane SLIM
> - [gRPC HTTP/2 / WS]
> - Routage hiérarchique
> - org/ns/svc/<id>
> - «container» Endpoint Pair B
> - [SLIM SDK + SPIRE]
> - Déchiffrement E2E, SLIMRPC ou A2A/MCP
> - «container» SLIM Control Plane [Controller & Channel Mgr]
> - Tables de routage et
> - groupes MLS
> - Annonce Skill -> CID Publie et signe
> - Connexion sortante
> - TLS / HTTP/2
> - Relais chiffré MLS (RFC 9420)
> - Requête multi-axes Tire OASF + Sigstore
> - Configure routes
> - et adhésions

*Fig. 20. – Architecture fédérée AGNTCY : enregistrement OASF/ADS et session chiffrée SLIM/MLS*

### 5.3.4 Transport `SLIM`, nommage hiérarchique et chiffrement de groupe `MLS` (`RFC 9420`)

Le protocole `SLIM` (*Secure Low-Latency Interactive Messaging*, spécifié dans `draft-mpsb-agntcy-slim-03`) complète `ADS` par un plan de données et une couche de session pair-à-pair conçus pour transporter `A2A`, `MCP` et `ACP` [92] [95]. Ses nœuds de routage en Rust acheminent des enveloppes `Protocol Buffers` sur `gRPC` streaming `HTTP/2` ou `WebSocket` selon un modèle d’enregistrement par connexion sortante : seuls les routeurs doivent être joignables sur le réseau, permettant aux agents privés derrière `NAT` ou pare-feu de communiquer dans les deux sens sans exposer de port entrant [92] [83].

Les agents y sont adressés par noms hiérarchiques `organization/namespace/service/<id>`, où le préfixe pilote les tables d’acheminement (`FIB` en `anycast` ou `unicast`) et le suffixe dérive de l’identité cryptographique (`SPIRE` ou `DID`) [92] [95]. `SLIM` supporte quatre motifs natifs : point-à-point, groupe/multidiffusion, `SLIMRPC` point-à-point et `SLIMRPC` multicast [92] [95]. Pour la confidentialité de bout en bout, la couche session intègre de manière optionnelle *Messaging Layer Security* (`MLS`, `RFC 9420`), qui gère des clés de groupe sur arbres de cliquet (*ratcheting trees*) via les primitives `KeyPackage`, `Proposal` et `Commit` en coût logarithmique `O(log N)`, assurant confidentialité persistante (`FS`) et sécurité post-compromission (`PCS`) de deux à plusieurs milliers de participants [95] [93].

Le document IETF `draft-mpsb-agntcy-messaging-03` met toutefois en garde le `SA` contre deux pièges d’architecture [83]. D’abord, la fiabilité configurable de `SLIM` ne garantit pas un traitement *exactly-once* applicatif, rendant l’idempotence indispensable [83]. Ensuite, lorsque `MLS` chiffre la charge utile de bout en bout, les routeurs et passerelles intermédiaires ne voient que les métadonnées de routage [95] [83]. L’inspection de contenu en ligne (masquage de renseignements personnels ou garde-fous sémantiques sur une *Agent Gateway*) ne peut alors plus opérer sur un simple relais réseau : elle doit résider aux extrémités avant chiffrement et après déchiffrement, ou bien la passerelle doit être admise comme participant explicite du groupe `MLS`, ce qui déplace explicitement la frontière de confiance [83]. De même, la révocation d’un identifiant dans un annuaire d’identité n’expulse pas d’elle-même un pair d’une époque `MLS` en cours sans transaction `Commit` explicite [83].

| Dimension technique | `A2A` sur `HTTP` / `gRPC` | Courtiers (`AMQP`, `Kafka`, `NATS`) | `AGNTCY SLIM` + `MLS` (`RFC 9420`) |
| --- | --- | --- | --- |
| Adressage | URI HTTPS ou `gRPC` par endpoint | Files, partitions ou sujets de courtier [83] | Nom hiérarchique `org/ns/svc/<id>` (unicast / anycast) [92] [95] |
| Traversée `NAT` / pare-feu | Requiert passerelle ou reverse-proxy exposé | Enregistrement sortant vers courtier (ou feuilles `NATS`) [83] | Connexion sortante `gRPC HTTP/2` ou `WebSocket` [92] [83] |
| Confidentialité réseau | `TLS` saut-par-saut (terminaison au proxy) [85] [83] | `TLS` saut-par-saut ; courtier voit les messages [92] [83] | Chiffrement E2E `MLS` ; routeurs aveugles au contenu [95] [83] |
| Groupes dynamiques | Aucun canal multicast natif (`A2A` = 1:1) | Fan-out par sujet ; pas de `PCS` en `O(log N)` [92] [83] | Groupes `MLS` (`FS`, `PCS`) et `SLIMRPC` multicast [92] [93] |
| Inspection en ligne (*Gateway*) | Directe à la terminaison `TLS` [83] | Proxy protocolaire ou adaptateur producteur/consommateur [83] | Aux extrémités ou passerelle membre `MLS` [83] |
| Usage privilégié | Appels B2B standards et intégration SaaS [82] [78] | Bus d’événements et télémétrie interne [83] | Maillages sensibles multi-org, périphérie et groupes [92] [95] |

*Tableau 5.2 — Comparaison architecturale des substrats de transport et de session pour l’interopérabilité inter-agents.*

> **Arbitrage EA / SA** — Déployer `AGNTCY` de manière incrémentale plutôt que dogmatique [94] [91] [83]. L’`EA` adopte dès le départ les schémas `OASF` dans son catalogue interne pour unifier la taxonomie des capacités et exige une provenance signée (`JWS` ou `Sigstore` via `ADS`) lors des échanges inter-organisations [82] [91] ; le `SA` réserve `SLIM` /`MLS` aux topologies nécessitant traversée de pare-feu sans exposition entrante, chiffrement bout en bout face à des relais tiers ou sessions de groupe dynamiques, tout en plaçant les contrôles `PII` dans l’enclave d’extrémité avant chiffrement `MLS` [92] [83].

## 5.4 Ponts inter-cadriciels (`LangGraph`, `Semantic Kernel`, `AutoGen`) et fédération B2B avec agents SaaS tiers

### 5.4.1 Convergence des cadriciels applicatifs derrière le contrat `A2A`

Dans les grandes organisations, les agents internes cohabitent sur des cadriciels hétérogènes choisis par affinité métier ou linguistique [78] [90] [96]. Le protocole `A2A v1.0` sert de contrat d’abstraction commun permettant à ces piles de coopérer sans exposer leurs graphes d’exécution ni coupler leurs cycles de mise à jour [82] [78].

- Côté `LangGraph`, l’*Agent Server* expose nativement tout assistant sous `/a2a/{assistant_id}` et génère sa carte à `/.well-known/agent-card.json?assistant_id={assistant_id}` [90]. Il illustre la mécanique exacte d’un pont protocolaire : prise en charge de la liaison `JSON-RPC` `v1.0` et des quatre méthodes `v0.3` (`message/send`, `message/stream`, `tasks/get`, `tasks/cancel`), mappage direct du `contextId` vers le `thread_id` `LangGraph` pour corréler les traces dans `LangSmith`, et extension `history-scope/v1` (`historyScope: "task"` ou en-tête `LangGraph-A2A-History-Scope`, avec plafond `historyLength ≤ 10` hors streaming SSE) évitant le rejeu redondant de l’historique multi-tâches [90]. Sur les flux humains, tout appel à `interrupt()` fait basculer la tâche vers `TASK_STATE_INPUT_REQUIRED` avec un `Artifact` nommé `Interrupt` portant `id`, `value` et `response_schema` dans une `DataPart`, la reprise s’effectuant par envoi d’une `DataPart` `{"data": {"resume": — }}` sur les mêmes `taskId` et `contextId` [90].

Dans l’écosystème Microsoft, les équipes à l’origine de `Semantic Kernel` (gestion de session, middleware, télémétrie) et d’`AutoGen` (abstractions multi-agents orientées événements) ont unifié les deux piles au sein du **Microsoft Agent Framework** (disponible en .NET, Python et Go) [88]. Côté consommation, le module `A2AAgent` (`Microsoft.Agents.AI.A2A`) encapsule tout pair `A2A` découvert par `A2ACardResolver`, catalogue ou client direct (`A2AClient`, `A2AHttpJsonClient`, `A2AGrpcClient`) derrière l’interface uniforme `AIAgent` (`RunAsync`, `RunStreamingAsync`, `AgentSession`) en négociant la liaison via `PreferredBindings` [89].

Dans le nuage AWS, **Amazon Bedrock AgentCore Runtime** héberge des agents `Strands` ou `LangGraph` encapsulés avec `a2a-sdk` dans des microVM isolées sur le port `9000` (chemin `/`), en assurant le passage transparent des charges `JSON-RPC` et de `/.well-known/agent-card.json` tout en appliquant `SigV4` ou `JWT` `OAuth 2.0` /`OIDC` (Cognito, Okta) et la télémétrie `OpenTelemetry` [96].

| Plateforme ou cadriciel | Exposition et découverte `A2A` | Liaisons et versions | Correspondance d’état et `HITL` | Contrôle de frontière notable |
| --- | --- | --- | --- | --- |
| `LangGraph` / `Agent Server` | `/a2a/{assistant_id}` et `/.well-known/agent-card.json? assistant_id=...` [90] | `JSON-RPC` `v1.0` et 4 méthodes `v0.3` (`gRPC` et `REST` absents) [90] | `contextId` → `thread_id` ; `interrupt()` → `INPUT_REQUIRED` + `DataPart` `resume` [90] | Extension `historyScope`, `historyLength ≤ 10`, SSE sans filtre d’historique [90] |
| `Microsoft Agent Framework` (`SK` + `AutoGen`) | `A2ACardResolver` (`.well-known`), catalogue ou client direct ; hébergement `A2A` [88] [89] | `JSONRPC`, `HTTP+JSON` et `gRPC` (`A2A.Grpc`), choix via `PreferredBindings` [89] | `AgentSession` persistée derrière `AIAgent` (`RunAsync`) [88] [89] | Validation obligatoire des réponses distantes comme entrées non fiables [89] |
| `Amazon Bedrock AgentCore Runtime` | Port `9000` (`/`), `/.well-known/agent-card.json`, relais `JSON-RPC` transparent [96] | `JSON-RPC` sur HTTP avec streaming (`a2a-sdk`, exécuteur `Strands` A2A) [96] | Isolation microVM avec fabrique d’agent par `context_id` [96] | Authentification `SigV4` ou `JWT` `OIDC` (`CUSTOM_JWT`) et en-têtes filtrés [96] |
| `Salesforce Agentforce` | `Agent Card` (contribuée à `A2A`) et écosystème `Agentforce` [86] [81] | `A2A` sur HTTPS avec négociation de version et OAuth 2.0 [86] [81] | Continuité par identifiant de conversation et *Trust Score* [81] | Suspension auto d’outils `MCP` si dérive ; tri API vs MCP vs A2A [86] |
| Plateformes partenaires (`ServiceNow`, `SAP`, `Foundry`) | Adoptants fondateurs d’`A2A` pour interopérabilité inter-nuages et SaaS [78] | `A2A` standardisé entre contrôleurs métier et agents externes [78] | Délégation asynchrone multi-éditeurs sans partage de mémoire [78] | Authentification HTTP, portées par compétence et API Management [85] [78] |

*Tableau 5.3 — Matrice d’interopérabilité contractuelle des principaux cadriciels, environnements infonuagiques et plateformes SaaS B2B.*

### 5.4.2 Fédération B2B avec agents SaaS tiers et mandats transactionnels

Sur le plan métier, `A2A` autorise la fédération B2B directe entre agents internes et agents SaaS d’éditeurs (`Salesforce Agentforce`, `ServiceNow`, `SAP`, `Microsoft Copilot Studio`) sans centralisation préalable des données [78] [86] [81]. Dans le scénario B2B documenté par Salesforce, l’agent de service après-vente d’un détaillant délègue l’inspection technique de dommages à l’agent spécialiste d’un manufacturier tout en vérifiant les conditions de retour auprès de l’agent du transporteur [81]. Chaque entreprise demeure souveraine de ses `SoR`, de ses barèmes et de ses données sensibles [85] [81].

Trois mécanismes complètent l’accord contractuel en contexte B2B. Premièrement, l’évaluation préalable de la fiabilité des pairs au moyen de métadonnées de conformité et d’un indice de confiance (*Agent Trust Score*) [91] [81]. Deuxièmement, le cloisonnement multi-locataires (`tenant` sur `AgentInterface` et portées OAuth par `AgentSkill`), dont les mécanismes cryptographiques `SPIFFE` /`SPIRE` et `OAuth 2.0 On-Behalf-Of` sont traités au chapitre 10 [82] [85]. Troisièmement, lorsque la collaboration engage un acte financier, l’extension *Agent Payments Protocol* (`AP2`), appuyée par plus de 60 organisations, attache aux échanges une preuve cryptographique du consentement utilisateur [78].

### 5.4.3 Menaces propres au maillage inter-agents (`OWASP ASI07` / `ASI08`) et clauses `FinOps`

La fédération inter-agents déplace deux risques critiques de l’*OWASP Top 10 for Agentic AI* sur la couche d’interopérabilité [84] :

- `ASI07` **— Communication inter-agents non sécurisée** : des canaux dépourvus d’authentification mutuelle, de signatures ou de validation stricte exposent les workflows à l’usurpation d’identité, au rejeu, à la rétrogradation de protocole (forçage vers une version dépourvue de contrôles) et à l’interception agent-du-milieu [84]. La parade combine `TLS 1.2/1.3` avec `HSTS`, validation obligatoire des signatures `JWS` ou `Sigstore`, et traitement de toute sortie distante comme une entrée applicative non fiable [82] [89] [84].
- `ASI08` **— Défaillances en cascade entre agents** : lorsqu’un agent consomme sans vérification les `Artifacts` produits par un pair amont, une faute logique, une boucle récursive ou une donnée empoisonnée s’amplifie sur toute la chaîne fédérée [84]. Le `SA` impose donc la validation `JSON Schema` sur chaque `DataPart` reçue, une borne explicite sur la profondeur de délégation inter-agents et des coupe-circuits par compétence [82] [84].

Enfin, sur le plan `FinOps`, déléguer une `Task` ouverte à un agent SaaS externe facturé à la tâche ou à l’usage expose le client à un risque de dérive budgétaire si le pair distant s’enferme dans des boucles d’outils internes opaques. L’`EA` doit donc exiger contractuellement l’annonce de plafonds de ressources par tâche, le maintien d’un droit d’interruption effectif via `CancelTask`, la propagation des identifiants `W3C Trace Context` pour l’imputation des coûts et une clause de réversibilité fondée sur les schémas ouverts `A2A` et `OASF` [82] [85] [78] [94].

> **Arbitrage EA / SA** — Exiger que toute fédération avec un agent SaaS tiers ou un cadriciel distinct transite exclusivement par des contrats `A2A v1.0` derrière une passerelle gouvernée, et traiter chaque `Message` ou `Artifact` retourné comme une entrée non fiable [82] [89] [84]. Le `SA` restreint les extensions autorisées (`capabilities.extensions`), valide chaque `DataPart` par schéma typé, borne la profondeur de délégation et applique le routage par `tenant` pour contenir `ASI07` et `ASI08` [82] [90] [84] ; l’`EA` conditionne l’homologation d’un pair externe à la signature de son `AgentCard`, au support effectif de `CancelTask` sous plafond `FinOps` et au référencement dans le catalogue `OASF` interne pour préserver la substituabilité des fournisseurs [82] [78] [94].

## Synthèse architecturale et transition

L’interopérabilité horizontale parachève le modèle d’outillage vertical : `MCP` apporte la profondeur locale sur les outils d’un domaine, tandis qu’`A2A` confère la portée inter-domaines entre pairs autonomes opaques [77]. Grâce au modèle `Protobuf` unique, aux `AgentCard` signées en `JWS` après canonisation `RFC 8785`, aux états asynchrones des `Tasks` (`SSE`, `INPUT_REQUIRED`, `AUTH_REQUIRED` et webhooks durcis anti-SSRF), `A2A v1.0` réunit `LangGraph`, le `Microsoft Agent Framework`, `Amazon Bedrock AgentCore` et les agents SaaS d’entreprise derrière un contrat stable [82] [78] [90] [89] [96]. Lorsque le maillage requiert une recherche sémantique fédérée et un chiffrement de bout en bout insensible aux relais réseau ou aux pare-feu, `AGNTCY` (`OASF`, `ADS` sur `OCI` /`Kademlia` /`Sigstore` et `SLIM` /`MLS`) complète la pile protocolaire [91] [92] [95] [93].

Standardiser la découverte et l’échange de tâches ne règle cependant ni la souveraineté des connaissances partagées ni les algorithmes qui coordonnent plusieurs pairs. Le chapitre 6 traite de l’ingénierie du contexte, de la mémoire distribuée et de la souveraineté sémantique des données, avant que le chapitre 7 ne formalise les patrons d’orchestration multi-agents qui exploitent ces contrats horizontaux.
