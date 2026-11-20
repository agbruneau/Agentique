# Chapitre 8 — Chorégraphie réactive et Event Mesh d’entreprise

Le passage de la coordination par graphe d’état (chapitre 7) à l’exécution continue sur les flux opérationnels transforme la gestion du temps dans le système d’information. Tant qu’un système multi-agents demeure déclenché par une requête synchrone issue d’un `System of Engagement (SoE)` ou d’une API `A2A` point-à-point, la chaîne d’exécution reste prisonnière d’un couplage temporel : chaque saut cognitif bloque l’appelant en attente de la réponse suivante, amplifie la latence de queue et propage la moindre défaillance d’aval [148] [149] [150]. Or, la majorité des processus critiques — détection de fraude, triage d’incidents, rapprochement logistique, traitement de réclamations — naissent de flux continus d’événements métier plutôt que de dialogues interactifs isolés [148] [151].

Pour absorber ces flux sans ériger un monolithe distribué fragile, l’entreprise agentique s’appuie sur un **maillage événementiel (**`Event Mesh`**)** et sur une **chorégraphie réactive** encadrée [148] [149] [152]. Les agents y deviennent des consommateurs ambiants éveillés par des événements normalisés qui circulent sur un réseau de courtiers découplés [148] [153] [149]. Ce changement de régime impose une double discipline. En architecture d’entreprise (**EA**), il faut délimiter la frontière entre autonomie réactive des domaines métier et imputabilité réglementaire des processus transverses, tout en contenant l’exposition financière liée aux cascades d’inférence [154] [155] [156]. En architecture de solutions (**SA**), il faut gouverner les enveloppes et contrats asynchrones, choisir le substrat de courtage adapté et déployer des coupe-circuits contre quatre pathologies réactives propres aux agents probabilistes : tempêtes d’événements, boucles d’écho sémantiques, engorgement des files de lettres mortes (`DLQ`) et rupture de contre-pression face aux quotas `LLM` [157] [158] [159] [160] [161]. Ce chapitre traite le transport événementiel et la chorégraphie ; la reprise sur panne par rejeu déterministe et les Sagas compensatoires relèvent du chapitre 9.

## 8.1 Agents ambiants déclenchés par événements : Kafka, Solace, NATS, CloudEvents et AsyncAPI

### 8.1.1 Du déclenchement à la demande aux agents ambiants sur flux continus

Un agent ambiant est un acteur cognitif — encapsulé dans son `Agent Harness` (chapitre 3) — dont l’activation répond en continu aux messages publiés sur un maillage événementiel plutôt qu’à un appel synchrone [153] [149] [151]. En consommant les faits opérationnels au fil de l’eau, l’agent réduit l’écart entre l’événement métier et l’action tout en préservant le découplage entre producteurs et abonnés [148] [149]. Toutefois, l’évaluation en simulation contrôlée menée par Dhanyamraju et al. sur 208 scénarios et 393 événements montre que le passage d’une cohorte restreinte (`Persona`, moins de 10 agents) à une échelle `Department` (20 à 80 agents) puis `Enterprise` (200 agents) dégrade les scores de sélection en raison d’un espace de découverte plus confus et d’événements concurrents [151].

À l’instar des systèmes distribués analysés par Martin Fowler, le qualificatif « orienté événements » recouvre des sémantiques distinctes qu’il faut dissocier avant toute conception agentique [162] :

1. **Notification événementielle (**`Event Notification`**)** : le producteur émet un signal léger constatant un changement d’état minimal, obligeant l’agent abonné à rappeler la source (par exemple via une passerelle `MCP`) pour obtenir le contexte complet [162]. Cette option limite l’exposition de données sur le bus mais réintroduit un couplage de disponibilité sous rafale.

2. **Transfert d’état porté par l’événement (**`Event-Carried State Transfer`**)** : l’enveloppe embarque la projection métier utile à l’agent, supprimant tout rappel synchrone vers le `System of Record (SoR)` au prix d’une duplication maîtrisée et d’une gouvernance stricte des schémas [162].
3. **Tableau noir sur journal partagé (**`Event-Driven Blackboard`**)** : les agents lisent et publient leurs contributions incrémentales sur des topics partagés formant une mémoire collective rejouable à court terme, sans échanges point-à-point [149] [150].

Le choix entre ces modalités détermine la résilience du maillage : la notification légère convient aux données hautement sensibles restreintes au domaine source, tandis que le transfert d’état porté protège les `SoR` patrimoniaux contre les rafales de lectures agentiques et fournit une piste d’audit rejouable [149] [150] [162].

### 8.1.2 Substrats de courtage : Apache Kafka, Solace Event Mesh et NATS JetStream

L’infrastructure d’`Event Mesh` s’articule autour de trois substrats majeurs dont les garanties d’ordonnancement, de routage et de régulation répondent à des profils d’entreprise distincts.

**Apache Kafka** constitue la dorsale privilégiée pour les journaux partitionnés à forte rétention et les traitements rejouables [149] [150]. Par le partitionnement sur clé, un processeur de flux tel qu’`Apache Flink` maintient l’état contextuel et distribue des tâches ordonnées vers des agents travailleurs tout en conservant l’historique complet [149] [150]. Sur le plan opérationnel, la référence `Kafka 4.1` met en évidence deux leviers critiques pour les nœuds `LLM` lents : `max.poll.interval.ms` (`300000` ms par défaut, soit cinq minutes) plafonne le délai maximal entre deux appels à `poll()` avant que le consommateur ne soit jugé défaillant et ne provoque un rééquilibrage du groupe, tandis que `max.poll.records` (`500` par défaut) borne le lot livré par appel [157]. L’usage de `group.instance.id` stabilise l’appartenance lors des redémarrages transitoires et `read_committed` isole les lectures transactionnelles [157].

**Solace PubSub+ Event Mesh** fédère un réseau de courtiers interconnectés à travers centres de données sur site, nuages publics ou privés et périphérie (`edge`) afin de distribuer dynamiquement les événements d’une application à toute autre sans codage en dur des chemins [148]. Adossé à ce maillage, `Solace Agent Mesh` structure les agents en microservices asynchrones exécutés sur un moteur `Go` extensible par outils `Python` ou `Go` isolés : des `Entrypoints` assurent authentification et contrôle d’accès, les agents délèguent des tâches en mode asynchrone selon `A2A` sur les sujets du courtier et invoquent des outils `MCP` confinés, permettant une mise à l’échelle horizontale indexée sur le volume de messages plutôt que sur le nombre d’agents [153].

**NATS JetStream** privilégie la légèreté, le routage par sujets hiérarchiques et le contrôle de flux explicite vers la périphérie [158]. Sous politique de rétention `WorkQueue`, chaque message n’est conservé dans le flux que jusqu’à l’acquittement du premier consommateur qui le retire pour l’ensemble du pool, tout en gardant les limites de taille comme filet de sécurité [163]. Les travailleurs utilisent des consommateurs en tirage (`pull consumers`) avec acquittement explicite (`AckPolicy.Explicit`, `Nak` et plafond `MaxDeliver` pour borner les relivraisons) [164], en choisissant `fetch` (lots bornés par `batch` et `expires`) ou `consume` (flux continu), ainsi que `max_bytes` pour plafonner l’empreinte mémoire [158]. Surtout, `MaxAckPending` (`1000` par défaut) borne globalement les messages en vol non acquittés sur l’ensemble du pool, offrant une contre-pression native côté serveur [158].

> **[Figure]**
> - Producteurs et Contrats
> - [system] Event Mesh d'entreprise
> - [system]
> - Agents ambiants
> - découplés
> - [system]
> - «container» Systems of Record
> - & CDC [Debezium / API]
> - Émet les faits métier en CloudEvents v1.0.2
> - «container» Catalogue AsyncAPI 3.0
> - & Schema Registry
> - [Contrats versionnés]
> - Valide canaux, actions
> - et en-têtes ce_*
> - «container» Dorsale Kafka [Journal partitionné]
> - Rétention longue, compactage et replay
> - «container» Courtiers Solace
> - [Maillage multi-sites]
> - Routage dynamique
> - sur Event Mesh
> - «container» NATS JetStream
> - [Pull / WorkQueue]
> - Périphérie et files à contre-pression
> - «container» Agent Triage
> - [Agent Harness]
> - Filtre ce_type et planifie sous quota
> - «container» Agent Conformité
> - [Agent Harness]
> - Consomme par groupe
> - ou file bornée
> - «container» MCP Gateway locale
> - [Outils typés]
> - Exécute les actions idempotentes sur SoR
> - CloudEvent (ce_*)
> - Stream / poll
> - Abonnement
> - Contrats Fédère
> - Ponte Isole
> - Outils (MCP)
> - Sujet hiérarchique
> - Pull / MaxAckPending

*Fig. 29. – Topologie C4 d’un Event Mesh d’entreprise alimentant des agents ambiants*

### 8.1.3 Enveloppes normalisées (`CloudEvents v1.0.2`) et contrats asynchrones (`AsyncAPI 3.0`)

Sans contrat partagé, un maillage reliant `Kafka`, `Solace` et `NATS` sombre dans l’hétérogénéité des en-têtes. La normalisation repose sur `CloudEvents v1.0.2` pour l’enveloppe de transport et sur `AsyncAPI 3.0.0` pour la description exécutable des interfaces [165] [166].

La spécification `CloudEvents v1.0.2` de la `CNCF` impose quatre attributs de contexte obligatoires en minuscules ASCII alphanumériques (`id`, `source`, `specversion`, `type`) et des attributs optionnels normalisés (`datacontenttype`, `dataschema`, `subject`, `time`), complétés par des extensions [165]. Les intermédiaires inspectent et routent ainsi l’enveloppe sans désérialiser la charge utile `data` [165]. Sur `Apache Kafka` (`kafka-protocol-binding`), le mode par lots est exclu et deux modes coexistent [167] :

- **Mode binaire (**`Binary Content Mode`**)** : la donnée brute `data` forme la valeur Kafka tandis que les attributs et extensions `CloudEvents` sont encodés en UTF-8 dans des en-têtes préfixés `ce_` (`ce_id`, `ce_type`, `ce_source`, `ce_specversion`), avec correspondance directe entre `content-type` et `datacontenttype` [167].
- **Mode structuré (**`Structured Content Mode`**)** : enveloppe et charge utile sont sérialisées ensemble dans la valeur de l’enregistrement, préservant la portabilité intégrale lors de transitions multi-protocoles [167].

En complément, **AsyncAPI 3.0.0** découple structurellement les `Channels` (adresses et schémas de messages admis) des `Operations` (`action: send` ou `receive` pointant par `$ref` vers le canal), tout en formalisant `Operation Reply`, `Correlation ID` et `Multi Format Schema` [166]. Ce découplage permet au catalogue `EA` d’enregistrer plusieurs agents abonnés sur un même canal sans dupliquer sa topologie, tandis que les liaisons officielles encapsulent la configuration de chaque courtier :

- **Kafka (**`0.5.0`**)** : `schemaRegistryUrl` et `schemaRegistryVendor` (`confluent`, `apicurio`, `ibm`, `karapace`) sur le serveur ; `topic`, `partitions`, `replicas` et `topicConfiguration` sur le canal ; `groupId` sur l’opération [168].
- **Solace (**`0.4.0`**)** : `msgVpn` et `clientName` sur le serveur, objet canal vide réservé pour usage ultérieur, et `destinations` (`topic` ou `queue`, `deliveryMode` `direct` ou `persistent`) sur l’opération [169].
- **NATS (**`0.1.0`**)** : objets serveur, canal et message neutres, et champ `queue` (≤ 255 caractères) sur l’opération pour documenter le groupe de répartition [170].

| Critère technique | Apache Kafka (`4.1`) | Solace PubSub+ (`Event Mesh`) | NATS JetStream (`2.15`) |
| --- | --- | --- | --- |
| Topologie native | Journal partitionné distribué et ordonné par clé | Maillage de courtiers interconnectés multi-sites [148] | Bus léger à sujets hiérarchiques et flux `JetStream` |
| Routage et filtrage | Topics, partitions et processeurs de flux (`Flink`) [150] | Sujets hiérarchiques et routage dynamique d’abonnements [148] | Sujets hiérarchiques avec jokers et files de travail |
| Rétention et rejeu | Longue durée configurable, compactage et rejeu d’offsets | Persistance par files selon abonnements et modes de livraison | `Limits`, `Interest` ou `WorkQueue` (purge à l’`Ack`) [163] |
| Régulation consommateur | `max.poll.records`, `max.poll.interval.ms` (`300000` ms) [157] | Files persistantes isolées et équilibrage par message [153] | Pull `fetch` /`consume`, `MaxAckPending` (`1000`), `max_bytes` [158] |
| Enveloppe `CloudEvents` | Mode binaire (`ce_*` UTF-8) ou mode structuré [167] | Attributs portés sur propriétés ou charge utile du sujet | En-têtes NATS ou charge JSON structurée |
| Liaison `AsyncAPI 3.0` | `schemaRegistryUrl`, `partitions`, `topicConfiguration`, `groupId` [168] | `msgVpn`, `clientName` (serveur), `destinations` (opération) [169] | `queue` (≤ 255 car.) sur l’objet opération [170] |
| Cas d’emploi cible | Dorsale analytique, mémoire partagée (`Blackboard`), `Flink` [149] | Fédération hybride multi-nuages, `Agent Mesh` `A2A` /`MCP` [148] [153] | Périphérie (`edge`), pools `WorkQueue` et faible empreinte [158] [163] |

*Tableau 8.1 — Comparatif architectural des substrats événementiels et liaisons AsyncAPI pour agents ambiants.*

> **Arbitrage EA / SA** — Imposer l’enveloppe `CloudEvents v1.0.2` (mode binaire `ce_*` sur `Kafka`) et la spécification `AsyncAPI 3.0.0` sur tout flux inter-agents transitant par l’`Event Mesh` [165] [167] [166]. L’`EA` interdit les canaux non enregistrés au catalogue et répartit les usages par rôle (`Kafka` pour le journal rejouable et le `Blackboard`, `Solace` pour le maillage multi-nuages et `Agent Mesh`, `NATS JetStream` pour la périphérie et les files `WorkQueue`) [148] [149] [163]. Le `SA` dimensionne `max.poll.records` /`max.poll.interval.ms` sous `Kafka` et `MaxAckPending` /`max_bytes` sous `JetStream` d’après la latence réelle d’inférence afin d’éviter rééquilibrages et saturation mémoire [157] [158].

## 8.2 Arbitrage architectural entre orchestration centralisée et chorégraphie décentralisée

### 8.2.1 Distinction sémantique fondatrice : événements contre commandes

De nombreux échecs d’intégration découlent d’une confusion entre **événement** et **commande** [155]. Comme le précisent Camunda et Martin Fowler, un événement constate un fait passé (`FactureEmise`, `SinistreDeclare`) diffusé sans connaissance des récepteurs ni attente d’action directe [162] [155]. Une commande exprime au contraire une instruction impérative adressée à un destinataire précis (`VerifierSolvabilite`), engageant une responsabilité d’exécution, un suivi de résultat et une gestion explicite des délais [155].

Lorsque des équipes modélisent un processus métier multi-étapes en pure chorégraphie, elles déguisent souvent des commandes en événements sur un bus partagé : chaque émetteur anticipe implicitement la réaction de l’abonné suivant sans qu’aucun composant ne détienne l’état consolidé [155]. Gregor Hohpe oppose à cette dérive le patron `Process Manager` : contrairement à un itinéraire figé dès l’émission (`Routing Slip`), le `Process Manager` maintient l’état courant du processus et détermine dynamiquement la commande suivante selon les résultats intermédiaires reçus [171]. Dans un système multi-agents, ce pilotage explicite devient d’autant plus nécessaire que les sorties cognitives sont non déterministes et requièrent des branchements conditionnels et une gestion de priorité [150] [151].

### 8.2.2 Forces et limites structurelles : de l’autonomie réactive à l’anti-patron « flipper »

La chorégraphie décentralisée offre des avantages indéniables dans un périmètre maîtrisé : elle supprime le point de défaillance unique d’un coordonnateur central, isole la mise à l’échelle de chaque consommateur et permet d’ajouter de nouveaux abonnés analytiques ou de surveillance sans modifier l’émetteur [152] [154]. Le patron `Blackboard` sur journal d’événements autorise ainsi plusieurs spécialistes à enrichir un cas en parallèle sans couplage direct [149].

En revanche, appliquée sans garde-fous à des chaînes métier longues ou multi-domaines, la chorégraphie dégénère vers l’anti-patron de la **machine à boules (**`Pinball Machine`**)** : les événements rebondissent entre agents sur le maillage sans propriétaire de bout en bout [152] [155]. Microsoft Azure Architecture Center, AWS Prescriptive Guidance et Camunda convergent sur quatre limites critiques [152] [154] [155] :

1. **Perte de visibilité bout-en-bout** : la logique du processus se disperse dans des abonnements et des consignes locales, rendant le suivi d’avancement et le débogage asynchrone coûteux [152] [155].
2. **Couplage sémantique caché** : malgré l’absence d’appels HTTP directs, l’évolution d’une séquence métier exige de modifier conjointement plusieurs services liés par des attentes implicites sur l’ordre des événements [155].
3. **Dépendances cycliques** : des composants réagissant mutuellement à leurs propres émissions forment des cycles difficiles à détecter statiquement [152].
4. **Dégradation de la précision à grande échelle** : la simulation contrôlée de Dhanyamraju et al. montre que la précision des appels dégrade lorsque le registre passe à 200 agents (`Enterprise`), alors que `DAG Plan & Execute` conserve une meilleure précision d’invocation tandis que `ReAct` obtient un meilleur rappel dans plusieurs conditions [151].

> **[Figure]**
> - A. Orchestration dirigée (Process
> - Manager explicite)
> - B. Chorégraphie pure non bornée
> - (Dérive « Pinball Machine »)
> - Déclencheur métier
> - Orchestrateur d'état (Process Manager)
> - Agent A (Extraction)
> - Agent B (Risque)
> - Agent C (Validation)
> - Événement initial
> - Event Mesh (Sujets partagés)
> - Agent X (Triage)
> - Agent Y (Enrichissement)
> - Agent Z (Décision)
> - 1 . Démarre instance
> - 2. Commande corrélée
> - 3. Commande suivante
> - 4. Commande finale
> - Émet fait
> - Réagit
> - Ré-émet
> - Réagit
> - Ré-émet
> - Réagit
> - Écho implicite (boucle / état diffus)

*Fig. 30. – Contraste topologique entre orchestration dirigée et dérive « flipper » en chorégraphie pure*

### 8.2.3 Grille d’arbitrage multicritère EA / SA

Le choix architectural dépend donc du niveau de risque, de la traversée de frontières organisationnelles et du besoin de contrôle transactionnel [152] [154] [155]. Même sur une infrastructure `Kafka`, Confluent démontre l’intérêt d’introduire `Apache Flink` comme orchestrateur à état interprétant le contexte et routant dynamiquement les tâches afin d’éviter la communication anarchique tous-azimuts [149] [150]. Réciproquement, imposer un orchestrateur pour diffuser des faits vers des consommateurs analytiques indépendants rigidifie inutilement l’architecture [154].

| Critère d’arbitrage | Orchestration centralisée (`Process Manager`) | Chorégraphie décentralisée (`Event Mesh`) | Patron hybride cible (section 8.4) |
| --- | --- | --- | --- |
| Pilotage des échanges | Commandes explicites émises par un coordonnateur à état [171] [155] | Réaction autonome aux faits (`events`) diffusés sur courtier [152] [154] | Commandes macro inter-domaines ; événements bornés intra-domaine |
| Visibilité et audit (`EA`) | Élevée : état global, branchements et piste d’audit centralisés [154] [155] | Faible : logique fragmentée entre abonnés et journaux dispersés [152] [155] | Élevée sur les jalons réglementaires ; souple dans chaque domaine |
| Couplage organisationnel | Élevé si l’orchestrateur gère les détails internes des domaines | Faible initialement, mais couplage sémantique caché sur flux longs [155] | Contenu par frontière de domaine borné (*Bounded Context*) |
| Gestion des délais et erreurs | Native : délais contractuels (`SLA`), escalades et reprises [154] [155] | Complexe : exige corrélation distribuée et files `DLQ` par abonné [152] [159] | `SLA` portés au plan macro ; `DLQ` et réessais gérés localement |
| Élasticité aux rafales | Dépend du partitionnement de l’état de l’orchestrateur [150] [151] | Maximale par découplage temporel et file dédiée [148] [158] | Amortissement asynchrone aux deux niveaux sans blocage |
| Risque de dérive (`ASI08`) | Faible sous bornage des étapes de planification [156] [151] | Élevé en chaînes profondes ou boucles récursives `LLM` [152] [161] | Maîtrisé par `TTL` intra-domaine et gouvernance macro |
| Domaine d’application | Flux multi-domaines réglementés, portes `HITL`, délais stricts [154] | Notifications multi-abonnés, enrichissement local simple [152] [154] | Référence cible pour l’entreprise agentique |

*Tableau 8.2 — Matrice décisionnelle : orchestration centralisée, chorégraphie décentralisée et patron hybride.*

> **Arbitrage EA / SA** — Rejeter en revue d’architecture (`ARB`) toute chorégraphie pure pour les processus franchissant plusieurs domaines métier ou soumis à des exigences d’audit réglementaire, de `SLA` ou d’approbation humaine [152] [154] [155]. L’`EA` exige qu’un `Process Manager` identifiable porte la traçabilité bout-en-bout des flux critiques ; le `SA` réserve la chorégraphie pure à la diffusion d’événements vers des consommateurs indépendants ou aux collaborations internes d’un domaine maîtrisé par une équipe unique [171] [154].

## 8.3 Pathologies réactives : tempêtes d’événements, boucles d’écho sémantiques, DLQ et backpressure LLM

Contrairement aux microservices déterministes dont le coût unitaire reste marginal et l’exécution sub-seconde, un agent `LLM` combine latence multi-seconde, consommation variable de jetons et interprétation probabiliste capable d’émettre de nouveaux messages [156] [161]. Quatre pathologies réactives doivent être prévenues de manière déterministe dans la couche transport et le harnais.

### 8.3.1 Tempêtes d’événements, cascades grégaires et détection précoce

Une **tempête d’événements** éclate lorsqu’un déclencheur unique provoque une ramification exponentielle de sous-événements entre agents réactifs [149] [156]. Cette amplification mécanique est aggravée par une vulnérabilité propre aux modèles de langage : l’étude empirique d’Hashemi et al. montre que des populations d’agents `LLM` exposées aux choix cumulés de leurs pairs subissent des boucles de rétroaction endogènes, un comportement grégaire (`herding`) et des cascades divergentes nettement plus marqués que chez les humains, tout en peinant à s’autocorriger [161]. Ce mécanisme illustre la menace `ASI08` (*Cascading Agent Failures*) du référentiel `OWASP Top 10 for Agentic AI`, où un défaut initial ou un biais sémantique se propage à la vitesse machine avant toute supervision humaine [156].

La surveillance limitée au contenu textuel de chaque message réagit trop tard. Luo et al. démontrent que dans les cascades multi-agents, les échanges initiaux restent sémantiquement fluides et conformes en apparence tandis que la géométrie du graphe d’interaction se déforme déjà en redondance et goulets d’étranglement ; en mesurant la courbure discrète d’Ollivier–Ricci (`ORC`) couplée aux signaux sémantiques, leur cadre détecte ces anomalies structurelles plusieurs tours avant la violation explicite et identifie l’agent ou le lien déclencheur [172]. Sur le plan opérationnel, Dhanyamraju et al. établissent qu’un gestionnaire de tâches léger (`Task Manager`) pratiquant inférence de priorité, fusion d’événements corrélés et préemption réduit de 14 à 75 % la latence de queue prioritaire et améliore de plus de vingt points la complétude sur événements liés à l’échelle `Enterprise` [151].

### 8.3.2 Boucles d’écho sémantiques : garde-fous protocolaires de corrélation et de TTL

La **boucle d’écho sémantique** survient lorsque deux ou plusieurs agents se renvoient des reformulations sur un sujet partagé : l’agent A publie une analyse, l’agent B l’interprète comme une sollicitation et publie un complément paraphrasé, puis l’agent A — sans conscience causale hors contexte — réagit à sa propre production déguisée [152] [161]. Sans borne déterministe, cette boucle alimente une dérive hors mandat (`ASI10`, *Rogue Agents*) et consomme le budget d’inférence en continu [156].

L’`Agent Harness` neutralise ces cycles avant même d’invoquer le modèle grâce à quatre attributs d’extension `CloudEvents` (`ce_*` sous Kafka) reliés à `Correlation ID` d’`AsyncAPI 3.0.0` [165] [166] :

1. **Corrélation et causalité (**`ce_correlationid`**,** `ce_causationid`**)** : rattachent tout événement dérivé à son événement racine pour tracer le graphe causal hors modèle [166].
2. **Compteur de sauts et plafond configurable (**`ce_hopcount` **/** `ce_ttl`**)** : le harnais incrémente `ce_hopcount` de manière déterministe à chaque ré-émission et déroute immédiatement vers la `DLQ` tout message dont `ce_hopcount > ce_ttl` selon le plafond certifié pour le domaine [156].
3. **Identité d’origine et déduplication (**`ce_originagent`**,** `ce_idempotencykey`**)** : bloque l’auto-consommation directe sur un canal bidirectionnel et rejette les empreintes causales déjà traitées.
4. **Ségrégation des canaux d’entrée et de sortie** : interdit à tout agent de s’abonner au canal sur lequel il publie ses verdicts [152].

### 8.3.3 Isolation des poisons sémantiques : DLQ, topics de réessai non bloquants et piège de `max.poll.interval.ms`

Une charge malformée, une sortie violant le contrat `AsyncAPI` ou un événement provoquant une exception systématique forme un poison (*poison pill*) qui paralyse une partition s’il bloque les tentatives sur place [159]. Confluent formalise quatre patrons progressifs de gestion d’erreurs sous `Kafka` [159] :

1. **Arrêt sur erreur (**`Stop on error`**)** : interrompt immédiatement le traitement lorsqu’aucune perte d’ordre n’est acceptable, notamment sur les flux `CDC` alimentant des projections `SoR` (chapitre 4) [159].
2. **File de lettres mortes (**`Dead Letter Queue`**,** `DLQ`**)** : déroute vers un topic d’erreur les messages irrécupérables tout en laissant le flux principal progresser, en enrichissant les en-têtes (topic d’origine, cause, horodatage) pour le diagnostic [159].
3. **Topic de réessai différé (**`Retry Topic`**)** : isole les conditions récupérables (dépendance absente ou indisponibilité temporaire) vers un topic séparé traité périodiquement par des instances dédiées, préservant ainsi la cadence du consommateur principal [159].
4. **Préservation d’ordonnancement sur redirection** : maintient l’ordre relatif des événements d’une même entité afin qu’un message postérieur ne dépasse pas un prédécesseur redirigé en réessai [159].

L’oubli de cette séparation devient fatal face aux temps de réponse `LLM`. Sous `Apache Kafka 4.1`, `max.poll.interval.ms` (`300000` ms par défaut) déclenche l’expulsion du consommateur et un rééquilibrage des partitions si `poll()` n’est pas rappelé dans le délai imparti [157]. Un agent tirant `500` messages (`max.poll.records` par défaut) et exécutant des appels `LLM` lents assortis d’attentes locales épuise cette fenêtre et provoque des tempêtes de rééquilibrage en chaîne [157]. La réduction stricte de `max.poll.records` pour les travailleurs cognitifs, le recours à `group.instance.id` et le déport des échecs transitoires vers des `Retry Topics` (ou sous `NATS JetStream` via `Nak` borné par `MaxDeliver`) garantissent la continuité du flux [157] [159] [164].

### 8.3.4 Backpressure LLM : découplage de cadence entre courtiers et inférence sous quotas de jetons

Un courtier événementiel absorbe des milliers de messages par seconde là où l’inférence `LLM` reste contrainte par la mémoire GPU et les quotas de jetons par minute (`TPM`). Selon le *Reactive Manifesto* et *Reactive Streams*, un système résilient remplace la poussée aveugle par une **contre-pression (**`backpressure`**)** non bloquante (formalisée par `Subscription.request(n)`), laissant les files d’attente en attente dans le courtier plutôt que de saturer la mémoire des travailleurs [173] [174].

Or, les mécanismes HTTP standards peinent à refléter ce goulot : l’IETF `draft-ietf-httpapi-ratelimit-headers-11` normalise `RateLimit-Policy` (`q`, `qu`, `w`, `pk`) et `RateLimit` (`r`, `t`, `pk`) pour anticiper les rejets `429`, mais ses unités normatives `qu` se cantonnent à `requests`, `content-bytes` et `concurrent-requests` [175]. Comme une requête d’agent varie fortement en taille d’invite et en volume généré, `Agent Router` (`Envoy AI Gateway`) introduit dans `AIGatewayRoute` le bloc `llmRequestCosts`, qui extrait `InputToken`, `CachedInputToken`, `OutputToken`, `TotalToken` ou des expressions `CEL` pour débiter un quota partagé dans `Redis` et déclencher HTTP `429` sur budget `TPM` [160]. Pour propager cette contrainte jusqu’au maillage, le `SA` combine trois mécanismes :

1. **Tirage borné sur le courtier** : utilisation de `pull consumers` `NATS JetStream` avec `MaxAckPending` calibré sur la capacité d’inférence concurrente et `max_bytes` borné, ou lots `max.poll.records` très réduits sous `Kafka` [157] [158].

2. **Réessai différé aligné sur** `RateLimit` **/** `Retry-After` : déport non bloquant vers un `Retry Topic` ou `Nak` temporisé plutôt qu’attente active sur le fil de consommation, en exploitant les valeurs `r` (quota restant) et `t` (fenêtre de réinitialisation) [159] [175] [164].
3. **Admission prioritaire par** `Task Manager` : fusion des événements corrélés et préemption avant inférence pour préserver le quota `TPM` sur les flux critiques [151].

> **[Figure]**
> - Courtier (Kafka / NATS)
> - Garde-fou Mesh
> - (TTL & Dédup)
> - Agent ambiant
> - (Pull borné)
> - Retry Topics
> - & DLQ
> - AI Gateway (Quota TPM / 429)
> - Courtier (Kafka / NATS)
> - Garde-fou Mesh
> - (TTL & Dédup)
> - Agent ambiant
> - (Pull borné)
> - Retry Topics
> - & DLQ
> - AI Gateway (Quota TPM / 429)
> - Lot borné (max.poll.records / batch)
> - Contrôle ce_idempotencykey
> - et ce_hopcount ≤ce_ttl
> - alt [Boucle d'écho ou saut > ce_ttl]
> - Isoler en DLQ (echo_loop_ttl)
> - Ack / Flux principal débloqué
> - [Événement admissible]
> - Message corrélé (ce_correlationid)
> - Requête inférence (quota TPM)
> - alt [Saturation GPU / TPM dépassé]
> - HTTP 429 + RateLimit (r=0, t)
> - Router vers Retry-Topic différé
> - Clore lot (< max.poll.interval.ms)
> - [Capacité disponible]
> - Réponse structurée + RateLimit (r, t)
> - Ack + CloudEvent (ce_hopcount + 1 )

*Fig. 31. – Séquence de confinement des pathologies réactives : anti-écho, files de réessai non bloquantes et backpressure LLM*

| Pathologie réactive | Mécanisme déclencheur | Signal précoce | Contre-mesure `SA` | Garde-fou `EA` (`FinOps` / Risque) |
| --- | --- | --- | --- | --- |
| Tempête d’événements et cascade grégaire | Fan-out non borné et rétroaction endogène (`ASI08`) [156] [161] | Anomalie de courbure `ORC` et pic d’émissions dérivées [172] | Coupe-circuits par sujet, fusion d’événements et préemption [151] | Plafonds `TPM` par domaine et audit des graphes `AsyncAPI` [166] [160] |
| Boucle d’écho sémantique | Paraphrase mutuelle sans causalité ni borne (`ASI10`) [156] [161] | Répétition de `ce_correlationid` et hausse de `ce_hopcount` | Plafond `ce_hopcount ≤ ce_ttl`, dédup `ce_idempotencykey` [165] [166] | Certification `ARB` du `ce_ttl` maximal et interdiction de boucles ouvertes |
| Engorgement `DLQ` et rééquilibrage | Lot excédant la fenêtre `poll()` (`300000` ms) [157] [159] | Rééquilibrages en série et hausse du lag consommateur | `max.poll.records` réduit, `Retry Topics` et `DLQ` enrichie [157] [159] | `SLA` de traitement des `DLQ` et traçabilité des rejets [159] |
| Rupture de backpressure (`HTTP 429`) | Cadence courtier supérieure au quota `TPM` GPU [173] [160] | Chute de `r` dans `RateLimit`, hausse des `429` et backlog [175] | Pull `MaxAckPending`, réessai différé et `llmRequestCosts` [158] [160] | Quotas `TPM` cloisonnés par locataire et priorisation métier [160] [151] |

*Tableau 8.3 — Catalogue des pathologies réactives en Event Mesh agentique : mécanismes de défaillance et contre-mesures EA / SA.*

> **Arbitrage EA / SA** — Aucun agent ambiant ne doit rejoindre l’`Event Mesh` sans quatre verrous déterministes hors modèle : propagation `ce_correlationid` avec plafond `ce_ttl`, isolation des erreurs par `Retry Topics` et `DLQ` enrichie, tirage borné (`MaxAckPending` ou `max.poll.records` calibré) et limitation par jetons `TPM` à la passerelle [165] [157] [158] [159] [160]. L’`EA` impose une capacité d’isolement immédiat face aux dérives `ASI08` /`ASI10` [156] ; le `SA` proscrit toute boucle d’attente bloquante sur le fil `poll()` Kafka [157] [159].

## 8.4 Patron hybride cible : orchestration macro-réglementaire et chorégraphie intra-domaine

### 8.4.1 Inversion ciblée à l’ère agentique : pourquoi le macro-plan doit rester orchestré

Dans les architectures microservices déterministes inspirées du *Domain-Driven Design (DDD)*, il est courant de recommander la chorégraphie entre contextes bornés et l’orchestration à l’intérieur de chacun d’eux afin d’éviter un ESB central monolithique [155]. Toutefois, l’introduction d’acteurs cognitifs probabi

listes dans des processus réglementés (octroi de crédit, triage clinique, conformité douanière ou financière) impose d’inverser cette répartition aux frontières critiques.

AWS Prescriptive Guidance rappelle que la chorégraphie convient lorsque l’équipe maîtrise toutes les dépendances dans son périmètre, tandis que les processus franchissant plusieurs frontières organisationnelles avec exigence de suivi d’état, de délais ou de contrôle d’erreur relèvent de l’orchestration [154]. Les résultats en simulation contrôlée confirment ce découpage : à l’échelle d’un petit groupe de spécialistes (`Persona`, moins de 10 agents), la réactivité locale reste précise, alors qu’à l’échelle `Enterprise` (200 agents), la confusion de découverte pénalise l’autonomie non encadrée face à une planification structurée (`DAG Plan & Execute`) [151].

Le **patron hybride cible** repose donc sur deux strates complémentaires :

1. **Orchestration macro-réglementaire inter-domaines** : un `Process Manager` dédié à une chaîne de valeur gouverne les transitions entre domaines distincts [171] [154]. Il émet des commandes typées (`AsyncAPI action: send`), veille au respect des `SLA`, déclenche les portes d’approbation humaine (`Human-in-the-Loop`) et consolide le journal d’audit réglementaire [166] [171] [155].
2. **Chorégraphie réactive bornée intra-domaine** : à l’intérieur d’un domaine géré par une même équipe produit et regroupant un nombre restreint d’agents spécialisés, l’exécution interne s’appuie sur un segment isolé de l’`Event Mesh` (par exemple `Kafka` + `Flink` ou un domaine `Solace Agent Mesh`), favorisant le parallélisme et l’enrichissement incrémental sans exposer les états intermédiaires hors du domaine [153] [150] [154] [151].

### 8.4.2 Contrat d’articulation inter-strates : commandes macro, jalons et frontière durable

Quatre règles d’interface maintiennent l’étanchéité entre les deux strates :

1. **Isolation des espaces de noms par domaine** : les sujets internes circulent dans des partitions ou `Message VPN` cloisonnés (`AsyncAPI` / `Solace`), interdisant à un domaine B de s’abonner aux événements internes intermédiaires d’un domaine A [169] [148].
2. **Frontière de traduction commande / jalon** : le `Process Manager` adresse uniquement l’`Entrypoint` ou le contrat public `AsyncAPI 3.0` du domaine par commande explicite, et ne reçoit en retour que des jalons consolidés au format `Event-Carried State Transfer` (`AnalyseTerminée`, `ConformitéValidée`) [166] [153] [162] [155].
3. **Bornage réactif interne** : chaque domaine applique intégralement les garde-fous de la section 8.3 (`ce_ttl` borné, déduplication `ce_idempotencykey`, `DLQ` locale et quota `TPM` dédié), empêchant toute tempête ou boucle interne de contaminer le plan macro [165] [159] [160] [156].
4. **Délégation de la reprise transactionnelle au chapitre 9** : le transport événementiel et ce patron hybride assurent le découplage de flux et la visibilité macro, mais ne remplacent pas un moteur de persistance d’état long. Dès qu’une orchestration macro doit survivre à des pannes en vol multi-jours, garantir un rejeu déterministe d’historique ou exécuter des compensations transactionnelles multi-`SoR`, la conception s’appuie sur l’`Exécution durable` et les Sagas du chapitre 9 [154] [155].

> **[Figure]**
> - Plan macro-réglementaire
> - [system]
> - Domaine A — Analyse
> - [system]
> - Domaine B — Conformité
> - [system]
> - «container» Orchestrateur de flux
> - réglementaire [Process Manager / SLA]
> - Détient l'état global, les jalons et la piste d'audit
> - «container» Porte HITL / Intent Gate
> - [Approbation & Audit]
> - Valide les seuils légaux et irréversibles
> - «container» Bus intra-domaine A
> - [Kafka / NATS]
> - Sujets privés (ce_ttl borné, DLQ locale)
> - «container» Agent Enrichisseur
> - [Agent Harness]
> - Réagit à DemandeOuverte
> - «container» Agent Évaluateur
> - [Agent Harness]
> - Émet jalon AnalyseTerminée
> - «container» Bus intra-domaine B
> - [Solace / Kafka]
> - Isolation par Message VPN / ACL
> - «container» Agent Contrôle KYC
> - [Agent Harness]
> - Vérification sous contrat
> - «container» MCP Gateway Domaine B
> - [Façade SoR]
> - Écriture idempotente sur System of Record
> - 3. Contrôle réglementaire
> - 1. Commande (AsyncAPI send)
> - Souscription
> - Événement interne
> - (hop + 1)
> - 2. Jalon AnalyseTerminée
> - 4. Commande engagement
> - Souscription
> - Outils (MCP)
> - 5. Jalon final DossierClôturé

*Fig. 32. – Topologie C4 du patron hybride cible : macro-orchestration réglementaire et chorégraphie intra-domaine*

> **Arbitrage EA / SA** — Retenir le patron hybride à deux strates comme standard d’entreprise pour toute chaîne de valeur agentique inter-domaines : orchestration macro-réglementaire explicite entre domaines et chorégraphie réactive bornée à l’intérieur de chaque domaine [171] [154] [155] [151]. L’`EA` garantit l’imputabilité réglementaire, le contrôle des portes humaines et l’allocation budgétaire `TPM` par domaine [160] [156] ; le `SA` préserve l’autonomie évolutive des équipes derrière des contrats `AsyncAPI 3.0` étanches, élimine les graphes « flipper » et arrime la reprise sur panne aux mécanismes durables du chapitre 9 [166] [152] [159].

## Synthèse et transition vers le chapitre 9

Un `Event Mesh` gouverné par `CloudEvents v1.0.2` et `AsyncAPI 3.0.0` affranchit l’entreprise agentique du blocage synchrone sur `Apache Kafka`, `Solace PubSub+` ou `NATS JetStream` [165] [166] [148] [158] [149]. Cette réactivité ne demeure fiable en production qu’en verrouillant ses quatre pathologies spécifiques — tempêtes d’événements, boucles d’écho sémantiques, engorgement `DLQ` sous `max.poll.interval.ms` et rupture de contre-pression `LLM` — et en combinant orchestration macro-réglementaire inter-domaines et chorégraphie bornée intra-domaine [157] [171] [154] [159] [160] [161].

Lorsque surviennent un redéploiement en plein vol, une indisponibilité prolongée de fournisseur d’inférence ou l’échec partiel d’une mutation déjà engagée sur un `System of Record`, le transport asynchrone de messages atteint toutefois ses limites. Le chapitre 9 prend alors le relais avec l’exécution durable (`Temporal`, `Restate`, `Dapr`), le *Transactional Outbox* et les Sagas compensatoires.
