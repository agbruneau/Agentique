# Chapitre 9 — Exécution durable, gestion d’état transactionnel et résilience opérationnelle

Une topologie multi-agents structurée (chapitre 07) ou un maillage événementiel régulé (chapitre 08) ne garantit pas la fiabilité d’un processus métier dès que l’exécution dure plusieurs minutes, heures ou jours [176] [177]. Lorsqu’un `System of Agency` enchaîne appels `LLM`, invocations d’outils `MCP` et validations humaines, l’occurrence d’au moins une panne d’infrastructure devient quasi certaine [178] [176]. Conserver l’avancement de ces boucles en mémoire volatile expose l’entreprise à des reprises partielles opaques, à des doubles écritures dans les `Systems of Record` (`SoR`) et à la perte d’état lors des redéploiements [179] [176] [180].

Ce chapitre établit le socle d’exécution durable et de cohérence transactionnelle de la Partie III. Côté architecture de solutions (`SA`), il s’agit d’isoler le non-déterminisme derrière un journal d’exécution persistant, de garantir l’idempotence sans verrou distribué, d’orchestrer des Sagas compensatoires et de suspendre les attentes humaines sous `SLA` sans consommer de calcul [181] [182] [183] [184]. Côté architecture d’entreprise (`EA`), l’objectif est d’imposer l’auditabilité, de préserver l’intégrité comptable des `SoR` et d’éviter la dépendance critique à un fournisseur d’inférence unique [185] [186] [187]. Par frontière d’étanchéité, ce chapitre traite exclusivement de la fiabilité d’exécution, de la persistance de workflow et des Sagas : la mémoire cognitive relève du chapitre 06, l’instrumentation `OpenTelemetry` et les coupe-circuits `SRE` appartiennent au chapitre 11, tandis que le versionnement en vol et la topologie complète de l’`AI Gateway` sont traités au chapitre 13.

## 9.1 Modes de défaillance des boucles longues en mémoire volatile (`timeouts`, `429`, redéploiements)

### 9.1.1 La falaise de complexité des boucles agentiques

Dans les applications web classiques, les requêtes synchrones brèves limitent l’exposition aux redémarrages de nœuds [178] [179]. À l’inverse, l’utilité d’un agent d’entreprise augmente avec sa durée de raisonnement et le nombre d’outils sollicités [176]. À mesure que ces deux facteurs croissent, les boucles orchestrées en mémoire volatile franchissent une *falaise de complexité* (*complexity cliff*) [176].

Deux effets cumulatifs expliquent cette rupture [176]. D’une part, la probabilité qu’au moins une étape subisse un dépassement de délai, un rejet de quota ou une coupure réseau tend vers la certitude sur les chaînes multi-tours [178] [176]. D’autre part, lorsqu’un processus en mémoire vive échoue à mi-parcours, la perte du contexte intermédiaire force à relancer tout le traitement depuis l’origine, multipliant les coûts d’inférence et le risque d’effets de bord dupliqués [176] [180].

### 9.1.2 `Timeouts` réseau, coupures de flux `SSE` et propagation de délais

Chaque appel distant doit être borné par des délais d’expiration (`timeouts`) de connexion et de lecture afin d’éviter l’immobilisation prolongée de fils d’exécution, de connexions réseau et de mémoire jusqu’à l’épuisement du service [178]. Toutefois, les répartiteurs de charge et mandataires inverses d’entreprise imposent des plafonds synchrones courts, incompatibles avec des trajectoires agentiques combinant plusieurs passes d’inférence ou des modèles à raisonnement étendu.

En diffusion continue (*Server-Sent Events*, `SSE`), une réponse initiale `HTTP 200` masque parfois une erreur survenant au milieu du flux ou une coupure réseau avant l’achèvement complet [185] [180]. L’appelant se retrouve dans l’ambiguïté décrite par Stripe : il ignore si l’action distante a échoué avant exécution, réussi juste avant la coupure ou laissé un état partiel [180]. Faute de journal externe et de propagation de l’échéance globale (*deadline*), des tentatives de reprise non coordonnées entre couches empilées amplifient la charge sur un système déjà dégradé [178].

### 9.1.3 Saturation de débit (`429`, `503`), `Retry-After` et gigue aléatoire

Les API d’inférence appliquent des quotas multi-dimensionnels pour protéger leur capacité [185] [188]. La norme `RFC 6585` définit le code `429 Too Many Requests` accompagné d’un en-tête optionnel `Retry-After` et interdit la mise en cache de ces réponses [189]. Les fournisseurs répartissent ces plafonds selon les requêtes par minute (`RPM`), les requêtes par jour (`RPD`), ainsi que les jetons en entrée et en sortie (`ITPM`, `OTPM`, `TPM`), via un algorithme de seau à jetons (*token bucket*) réapprovisionné en continu [185] [188]. Des rafales brèves sur quelques secondes suffisent donc à provoquer un rejet même sous un débit moyen modéré [185].

Surtout, tous les rejets ne doivent pas être réessayés [185] [188]. Sur la plateforme Claude d’Anthropic, un dépassement de cadence retourne `429` (`rate_limit_error`) avec un en-tête `retry-after`, alors que l’atteinte d’un plafond budgétaire mensuel retourne également `429` mais avec le code `enforced_spend_limit_reached` et sans `retry-after`, rendant toute reprise automatique stérile [185]. De même, OpenAI distingue le code `slow_down` (`429`) lors d’une hausse de trafic trop abrupte du code `server_is_overloaded` (`503 service_unavailable_error`) [188].

Face aux erreurs transitoires, des reprises immédiates ou un recul exponentiel purement déterministe synchronisent les clients en échec et créent des vagues de congestion répétées [178] [190]. La pratique recommandée consiste à respecter prioritairement la temporisation `Retry-After`, à appliquer sinon un recul exponentiel plafonné (`cap`) et à y injecter une gigue aléatoire (*jitter*) afin d’étaler les nouvelles tentatives dans le temps [178] [188] [190].

### 9.1.4 Éphémérité des conteneurs : `SIGTERM`, `SIGKILL` et perte de pile

Les infrastructures conteneurisées aggravent la vulnérabilité des boucles non persistées [179]. Dans Kubernetes, les pods sont des entités éphémères : lors d’une mise à jour continue, d’une éviction ou d’une préemption de nœud, le plan de contrôle retire le pod des `EndpointSlices`, exécute l’éventuel crochet `preStop` et émet le signal `SIGTERM` [179]. Le compte à rebours `terminationGracePeriodSeconds` — fixé par défaut à **30 secondes** — démarre aussitôt [179]. Si une boucle agentique reste bloquée sur une inférence lente au-delà de cette fenêtre de grâce, le `kubelet` envoie `SIGKILL`, détruisant le processus ainsi que sa pile d’appels et les références de mutations déjà reçues, comme l’illustre la figure 9.1 [179] [176].

> **[Figure]**
> - Boucle Agent (Pod K8s volatile)
> - API Inférence (LLM Externe)
> - MCP Gateway
> - / SoR
> - Contrôleur K8s (RollingUpdate)
> - Boucle Agent (Pod K8s volatile)
> - API Inférence (LLM Externe)
> - MCP Gateway
> - / SoR
> - Contrôleur K8s (RollingUpdate)
> - 1. Saturation débit et tempête de reprises (sans gigue)
> - 1 POST /messages (Tour N, contexte en RAM)
> - 2 HTTP 429 rate_limit_error (Retry-After) ou 503 overloaded
> - Sans backoff ni gigue : reprises synchronisées des workers. Risque de timeout proxy HTTP 504.
> - 2. Éviction de pod et perte de pile en mémoire vive
> - 3 Mutation 1 : réserver inventaire (POST)
> - 4 HTTP 201 Réservation #R-402
> - 5 Tour N+1 : planifier facturation
> - 6 SIGTERM (déploiement / nœud préempté) Décompte terminationGracePeriodSeconds (30s)
> - Appel LLM en cours > 30s : le délai expire avant la fin du tour.
> - 7 SIGKILL (arrêt brutal du conteneur)
> - Pile d'appels, historique de session et reçu #R-402 perdus en RAM. La relance à zéro risque la double écriture.

*Fig. 33. – Anatomie des modes de défaillance d’une boucle agentique exécutée en mémoire volatile*

| Mode de défaillance | Déclencheur | Impact en mémoire volatile | Contre-mesure SA | Exigence EA |
| --- | --- | --- | --- | --- |
| Expiration ou coupure `SSE` | Délai passerelle ou perte de flux après `200` [178] [185] | Incertitude d’exécution et perte de contexte [180] | Découplage asynchrone et reprise sur journal [178] [181] | Interdiction des boucles synchrones longues depuis `SoE` [176] |
| Saturation `429` / `503` | Rafale `RPM` /`TPM`, `slow_down` ou surcharge [185] [188] | Tempêtes synchronisées et épuisement de fils [178] [190] | `Retry-After`, backoff plafonné avec *jitter* [178] [188] | Arrêt immédiat sur plafond budgétaire (sans reprise) [185] |
| Arrêt brutal (`SIGKILL`) | Déploiement ou préemption dépassant 30 s [179] | Perte de pile et risque de double écriture [179] [176] | État externalisé en moteur durable [179] [181] | Zéro perte de dossier lors des mises en production [176] |
| Reprises empilées | Couches applicatives réessayant en cascade [178] | Amplification multiplicative de charge [178] [180] | Reprise centralisée et clé d’idempotence [178] [182] | Politique unique de tentatives bornées par criticité [178] |

*Tableau 9.1 — Taxonomie des modes de défaillance en mémoire volatile et contre-mesures EA / SA.*

> **Arbitrage EA / SA** — Interdire le maintien de l’état d’avancement d’une boucle multi-étapes dans la mémoire volatile d’un pod ou d’une fonction sans serveur dès qu’interviennent des appels externes ou des mutations métier [179] [176]. Le `SA` supprime les reprises empilées entre couches, respecte `Retry-After` avec recul exponentiel plafonné et *jitter* sur les fautes transitoires, et interrompt immédiatement les erreurs budgétaires ou de validation [178] [185]. L’`EA` impose qu’aucun redéploiement courant ne détruise un dossier en cours d’instruction [179] [176].

## 9.2 `Durable Execution` (`Temporal`, `Restate`, `Dapr`) : journalisation déterministe, `replay` et `checkpointing`

### 9.2.1 Principes du `Durable Execution` : journalisation déterministe et `Replay`

Les moteurs d’exécution durable (`Durable Execution`) garantissent qu’un processus applicatif progresse jusqu’à complétion sans limite de durée imposée, malgré les pannes de travailleurs ou coupures réseau [181] [176] [191]. Leur mécanisme repose sur la journalisation immuable de chaque transition d’état avant le passage à l’étape suivante, couplée à un rejeu (*replay*) déterministe lors d’une reprise [181] [191].

Pour que le rejeu reconstitue exactement les variables locales sans dupliquer les effets de bord, le code orchestrateur doit respecter des **contraintes de déterminisme** strictes [190] [192]. À entrées et historique identiques, il doit produire la même séquence de commandes [190]. Il est donc proscrit d’exécuter directement dans le code de workflow des appels réseau, requêtes `LLM`, accès SQL, lectures d’horloge système ou tirages aléatoires non amorcés [190] [192]. Toute opération non déterministe est isolée dans une primitive dédiée (`Activity` ou `ctx.run`) dont la sortie sérialisée est inscrite au journal ; au rejeu, le moteur restitue cette sortie enregistrée sans ré-exécuter l’opération [181] [191] [192].

Ce journal transactionnel demeure distinct des mémoires cognitives du chapitre 06 : un résumé conversationnel ou épisodique ne doit jamais servir à reconstruire le curseur d’exécution d’un workflow [181] [193]. Quant aux techniques de compatibilité lors des mises à jour de code sur des instances dormantes (`Patching`, `Worker Versioning`), elles relèvent du cycle `GitOps` étudié au chapitre 13 [190].

### 9.2.2 `Temporal` : `Workflows`, `Activities`, `Task Queues` et `Heartbeats`

`Temporal` incarne l’architecture de référence à séparation stricte entre coordination et exécution externe [190] [181] :

1. **Les** `Workflow Definitions` portent la logique déterministe de boucle, d’embranchement et de reprise [190] [181]. Lors de leur exécution sur un travailleur, elles émettent des `Commands` (planifier une activité, démarrer un minuteur, signaler un workflow) que le serveur transforme en événements dans un journal immuable (`Event History`) [190] [181].
2. **Les** `Activities` exécutent le code non déterministe (appels `LLM`, requêtes `MCP`, écritures `SoR`) sur des travailleurs dédiés qui scrutent des files de tâches (`Task Queues`) en mode *pull* [190] [181] [176]. Chaque activité s’appuie sur une `RetryPolicy` déclarative gérée par le moteur [176].

Temporal fournit quatre temporisations complémentaires pour détecter finement les pannes d’activité [194] : `Schedule-To-Start` (attente en file), `Start-To-Close` (durée d’une tentative), `Schedule-To-Close` (enveloppe totale incluant les reprises) et `Activity Heartbeats` [194]. Sur une tâche longue, le travailleur émet des battements de cœur périodiques porteurs d’un curseur de progression : si le pod subit un `SIGKILL`, l’expiration du `Heartbeat Timeout` déclenche la relance immédiate sur un nœud sain à partir du dernier curseur enregistré [179] [194]. De plus, les `Durable Timers` gérés côté serveur permettent à un même travailleur d’attendre simultanément des millions de minuteurs sur des jours ou des mois sans consommer de ressources de calcul [177].

### 9.2.3 `Restate` : journalisation en ligne, `Virtual Objects` et exécution sans serveur

`Restate` propose une architecture centrée sur un mandataire serveur unique écrit en Rust, appuyé sur un journal distribué répliqué en flux continu, qui pousse les requêtes vers les services applicatifs par HTTP/RPC (*push*) [191] [195]. Cette topologie évite l’exploitation d’une grappe multi-composants avec base de données externe et réduit la latence de persistance par étape à quelques millisecondes, ce qui rend la journalisation fine viable sur des boucles agentiques comptant des milliers d’étapes [191] [195].

- Dans le code applicatif, le développeur ne sépare pas physiquement workflow et activité : il écrit une fonction impérative standard et encapsule chaque étape non déterministe dans un bloc `ctx.run( — )` dont le résultat sérialisé rejoint le journal d’exécution [191] [192]. Les politiques de reprise gèrent les fautes transitoires et s’arrêtent sur `TerminalError` [192]. Surtout, Restate introduit les `Virtual Objects`, qui associent à une clé unique (par exemple un identifiant de session agentique) un stockage clé-valeur (`KV`) intégré, des journaux d’exécution et une exécution strictement sérialisée par clé [191]. Les sessions multi-tours évitent ainsi les accès concurrents conflictuels sans verrou externe tout en se suspendant totalement en calcul sans serveur lors des attentes [191] [195].

### 9.2.4 `Dapr Workflow` et `Checkpointers` de graphe (`LangGraph`)

Intégré à l’écosystème Cloud Native Computing Foundation (`CNCF`), `Dapr Workflow` embarque le moteur `durabletask-go` directement dans le *sidecar* Dapr de chaque pod applicatif, relié au SDK par un flux gRPC bidirectionnel [196]. Le moteur orchestre des acteurs virtuels internes (`Workflow actor` et `Activity actor`) garantissant une exécution mono-fil par instance et délègue la persistance des points de reprise à un magasin d’état enfichable (`PostgreSQL`, `Redis`, etc.) [196]. Ce choix favorise la standardisation Kubernetes et la portabilité des bases d’état, au prix d’une exécution couplée au cycle de vie du sidecar par pod et d’une sémantique dépendante du `State Store` configuré [196].

Enfin, les `Checkpointers` intégrés aux cadriciels d’agents tels que `LangGraph` enregistrent l’état d’un graphe par fil d’exécution (`thread_id`) à chaque frontière de super-étape pour offrir tolérance aux pannes locales, reprise après interruption humaine et voyage temporel, en complément de `Stores` dédiés à la mémoire transversale inter-fils [193]. Toutefois, un checkpointer de graphe seul ne fournit ni files de tâches distribuées avec travailleurs indépendants, ni minuteurs serveur persistants multi-semaines, ni détection par battements de cœur [194] [177] [193]. En entreprise, les graphes cognitifs gagnent donc à être encapsulés dans un moteur d’exécution durable complet [176] [195] [193]. La figure 9.2 compare ces architectures.

> **[Figure]**
> - Modèle Temporal (Pull +
> - Replay) [container]
> - Modèle Restate (Push +
> - Journal en ligne)
> - [container]
> - Modèle Dapr Workflow
> - (Sidecar CNCF)
> - [container]
> - «component» Workflow Worker
> - [Code déterministe]
> - Rejoue l'historique, émet des Commands
> - «component» Temporal Service
> - [Event History]
> - Journal immuable, timers et Task Queues
> - «component» Activity Worker [Code non déterministe]
> - Appels LLM / MCP, RetryPolicy et Heartbeats
> - «component» Restate Server (Rust)
> - [Proxy + Log répliqué]
> - Journalise étapes en ligne,
> - sérialise par clé
> - «component» Service / Virtual Object
> - [Handler + ctx.run()]
> - Logique métier, état KV et suspension sans serveur
> - «component» Application SDK
> - [Flux gRPC]
> - Enregistre workflows
> - et activités métier
> - «component» Sidecar Dapr
> - [durabletask-go]
> - Orchestre via Workflow
> - et Activity Actors
> - «component» State Store enfichable
> - [PostgreSQL / Redis]
> - Persiste points de reprise
> - et files d'acteurs
> - Scrute Task Queue /
> - envoie Commands
> - Distribue tâches
> - d'Activity
> - Pousse RPC HTTP +
> - journaux d'état
> - Échange items
> - sur flux gRPC
> - Persiste état
> - des acteurs

*Fig. 34. – Topologie comparative des moteurs d’exécution durable : Temporal, Restate et Dapr Workflow*

| Critère architectural | Temporal | Restate | Dapr Workflow | Checkpointer (`LangGraph`) |
| --- | --- | --- | --- | --- |
| Modèle de programmation | `Workflow` déterministe / `Activity` séparée [190] [181] | Code impératif unifié avec blocs `ctx.run()` [191] [192] | SDK gRPC vers sidecar `durabletask-go` [196] | Sauvegarde d’état par super-étape (`thread_id`) [193] |
| Dispatch et latence d’étape | *Pull* sur `Task Queues` (surcoût de file modéré) [181] [195] | *Push* HTTP/RPC en flux continu (quelques ms) [191] [195] | Flux gRPC local vers sidecar du pod [196] | En processus vers base cible [193] |
| État et concurrence | État rejoué + historique sur DB externe [181] [195] | `Virtual Objects` avec `KV` intégré sérialisé par clé [191] | `State Store` enfichable via acteurs Dapr [196] | `Checkpointer` (fil) + `Store` (inter-fils) [193] |
| Détection et délais longs | `Heartbeats`, 4 timeouts, `Durable Timers` serveur [194] [177] | Reprises, `TerminalError`, suspension sans serveur [191] [192] | Reprises et rappels via acteurs Dapr [196] | Reprise locale d’étape ; sans files distribuées [193] |
| Cas d’usage cible EA / SA | Workflows critiques longs et forte observabilité [176] [177] | Boucles agentiques rapides et déploiement sans serveur [191] [195] | Plateforme Kubernetes standardisée sur Dapr CNCF [196] | Sous-graphes cognitifs hébergés dans un moteur durable [193] |

*Tableau 9.2 — Matrice comparative des moteurs d’exécution durable et des couches de persistance.*

> **Arbitrage EA / SA** — Exiger un moteur d’exécution durable complet (`Temporal`, `Restate` ou `Dapr Workflow`) pour tout processus agentique comportant des écritures `SoR`, des délais longs ou des validations humaines, plutôt qu’un simple checkpointer de graphe isolé [176] [196] [193]. Le `SA` choisit `Temporal` pour les processus longs à forte séparation de files et suivi par `Heartbeats` [194] [195], `Restate` pour les boucles fines à faible latence, les `Virtual Objects` par session ou l’exécution sans serveur [191] [195], et `Dapr Workflow` lorsque la pile Kubernetes s’appuie déjà sur le sidecar CNCF [196]. L’`EA` maintient le cloisonnement strict entre le journal d’exécution et les bases cognitives du chapitre 06.

## 9.3 Cohérence sans verrou distribué : idempotence de bout en bout, `Outbox` et Sagas compensatoires

### 9.3.1 Impossibilité du protocole `Two-Phase Commit` (`2PC`) en contexte agentique

Garantir la reprise de l’orchestrateur ne protège pas à lui seul l’intégrité des systèmes cibles dès que le workflow sollicite des `Systems of Record`, des serveurs `MCP` et des API SaaS possédant chacun leur propre stockage [197] [183]. Le protocole de validation distribuée `Two-Phase Commit` (`2PC`) s’avère inopérant pour trois motifs structurels [197] [186] [183]. D’abord, la majorité des progiciels modernes, des API HTTP et des courtiers de messages ne supportent pas de coordinateur XA distribué [197]. Ensuite, comme l’ont démontré Garcia-Molina et Salem pour les transactions de longue durée (*Long-Lived Transactions*), maintenir des verrous de base de données pendant des appels lents effondre la concurrence et multiplie les interblocages [186] [183]. Enfin, les reprises automatiques et la livraison au-moins-une-fois (*at-least-once*) imposent de rendre chaque frontière tolérante aux réémissions [180] [198].

### 9.3.2 Idempotence de bout en bout : contrat `Idempotency-Key` et phases atomiques

Selon `RFC 9110`, rappelée par le projet de norme IETF `draft-ietf-httpapi-idempotency-key-header-08`, les méthodes `GET`, `PUT` et `DELETE` sont idempotentes, contrairement à `POST` et `PATCH` qui dominent les mutations métier et appels d’outils [182]. L’orchestrateur doit donc associer à chaque commande mutatrice un en-tête `Idempotency-Key` déterministe — dérivé de l’identifiant du workflow et du rang logique de l’étape — afin que toute reprise émette exactement la même clé [181] [182].

Côté récepteur (`MCP Gateway` ou couche anti-corruption `ACL` devant un `SoR`), trois règles garantissent la sûreté sans verrou prolongé [182] [180] :

1. **Contrôle d’empreinte (*Idempotency Fingerprint*)** : le serveur lie la clé à une empreinte cryptographique de la charge utile. Selon le projet IETF, l’absence d’une clé requise retourne `400 Bad Request`, tandis que sa réutilisation sur un corps différent retourne `422 Unprocessable Content`, bloquant toute dérive d’intention lors d’un rejeu ou d’une erreur d’agent [182].
2. **Machine à trois états** : enregistrer la clé uniquement après réussite ouvre une faille de concurrence. Le stockage d’idempotence doit distinguer l’état absent, l’état « en vol » — retournant `409 Conflict` si une reprise survient pendant l’appel initial — et l’état achevé, dont le statut et le corps exacts sont rejoués à l’identique jusqu’à expiration de la clé [182] [180].
3. **Phases ACID brèves et points de reprise** : suivant l’architecture de Stripe documentée par Brandur Leach, un service ne maintient jamais une transaction SQL ouverte durant un appel réseau externe ; il encadre l’appel distant par de courtes transactions locales consignant des points de reprise (*recovery points*) [180].

### 9.3.3 Patron `Transactional Outbox` et capture `CDC` sans double écriture

Lorsqu’un composant métier doit simultanément modifier sa base locale et publier un message vers un courtier événementiel, l’exécution séquentielle crée le risque de **double écriture** (*dual-write*) : une panne entre la validation SQL et la publication désynchronise durablement le système [197] [198].

Le patron `Transactional Outbox` supprime cette faille sans `2PC` en écrivant le message sortant dans une table `Outbox` au sein de la même transaction ACID locale que l’entité métier [197] [198]. Un relais asynchrone publie ensuite ces lignes vers le bus de messages [197]. Plutôt qu’une scrutation SQL coûteuse, la capture de données modifiées (`CDC`) via Debezium lit directement le journal de transactions (`WAL`) sans verrou ni impact sur les requêtes métier, applique le routage `EventRouter` et délivre les événements ordonnés en sémantique *at-least-once*, en parfaite synergie avec l’idempotence des consommateurs [198]. Ce patron protège les frontières des `SoR` et services existants appelés par le workflow, tandis que le moteur durable assure lui-même l’atomicité de son propre journal d’orchestration [181] [191] [197].

### 9.3.4 Sagas compensatoires : compensable, pivot, réessayable et irréversible

Lorsqu’un traitement répartit des mutations sur plusieurs systèmes autonomes, l’échec d’une étape aval impose d’annuler sémantiquement les étapes précédentes sans verrou global [186] [183]. Une **Saga**, introduite par Garcia-Molina et Salem, enchaîne des transactions locales `T1..Tn` et associe aux étapes réversibles des transactions compensatoires `C1..Cn-1` exécutées en ordre inverse en cas d’échec [186].

En s’appuyant sur la typologie de l’Azure Architecture Center, le `SA` classe chaque outil mutateur d’agent selon sa position par rapport au point de non-retour [183] :

1. **Transactions compensables** : actions annulables par opération inverse (`réserverCrédit` / `libérerCrédit`), exécutées avant le pivot et empilées dynamiquement pour repli éventuel [183] [199].
2. **Transaction pivot** : point de non-retour de la Saga ; avant son succès, la compensation inverse reste possible, alors qu’une fois le pivot validé, le workflow doit converger vers son achèvement [183].
3. **Transactions réessayables** : étapes idempotentes situées après le pivot, garanties de réussir à terme par reprises bornées ou durables [183].
4. **Actions externes non compensables** : les agents manipulent fréquemment des effets irréversibles sans compensation réelle (envoi d’un courriel externe, virement instantané, soumission réglementaire) [183]. Elles doivent impérativement être placées **après le pivot** ou derrière une validation humaine durable (`HOTL`) [183] [184].

Contrairement à une Saga purement chorégraphiée dont le suivi devient fragile au-delà de trois participants (chapitre 08), la **Saga orchestrée** dans `Temporal` ou `Restate` empile les fermetures compensatoires en code impératif et les exécute en ordre inverse dès qu’une `TerminalError` survient [183] [199]. La durabilité du journal garantit l’achèvement de la séquence de compensation même si un nœud redémarre pendant le retour arrière, chaque appel compensatoire portant sa propre `Idempotency-Key` [182] [199]. La figure 9.3 synthétise cette chaîne de cohérence.

> **[Figure]**
> - Orchestrateur Durable
> - (Saga)
> - Base Locale + Table Outbox
> - Relais CDC (Debezium WAL)
> - MCP Gateway (Idempotency Store)
> - System of Record
> - (ERP / Paiement)
> - Orchestrateur Durable
> - (Saga)
> - Base Locale + Table Outbox
> - Relais CDC (Debezium WAL)
> - MCP Gateway (Idempotency Store)
> - System of Record
> - (ERP / Paiement)
> - 1. Transactional Outbox (élimination du dual-write sans 2PC)
> - 1 BEGIN TX : MAJ état + INSERT Outbox
> - 2 COMMIT ACID local
> - 3 Lit journal WAL (zéro verrou)
> - 4 Publie événement ordonné (at-least-once)
> - 2. Contrat Idempotency-Key à 3 états et étape compensable
> - 5 POST /reserve (Idempotency-Key: K1, hash H1)
> - Enregistre K 1 en état « En vol ». Si K 1 concurrent : HTTP 409. Si K 1 avec autre corps : HTTP 422.
> - 6 Réserver crédit client
> - 7 HTTP 200 Réservation #R1
> - 8 HTTP 200 (stocke réponse sur K1)
> - Empile compensation C1 : annulerReservation(#R1)
> - 3. Échec d'étape et compensation inverse avant le pivot
> - 9 POST /provision (Idempotency-Key: K2, hash H2)
> - 10 Allouer licence partenaire
> - 1 1 Refus métier définitif (TerminalError)
> - 12 Erreur terminale non réessayable
> - 13 Compensation C1 : POST /release/#R1 (Key: C-K1)
> - 14 Libère crédit #R1
> - 15 HTTP 200 Compensé

*Fig. 35. – Chaîne de cohérence sans verrou distribué : Transactional Outbox, Idempotency-Key à 3 états et Saga orchestrée*

| Catégorie d’étape | Position vs pivot | Réversibilité et idempotence | Exemple agentique | Gestion d’échec |
| --- | --- | --- | --- | --- |
| Compensable (`T_i`, `C_i`) | Avant le pivot [183] | Réversible via action opposée ; `Idempotency-Key` requise [182] [183] | Pré-autorisation financière, réservation de stock ERP | Empiler `C_i` (clé `C-K_i`) ; dérouler en sens inverse sur `TerminalError` [199] |
| Pivot | Point de bascule [183] | Non compensable ; valide l’engagement métier [183] | Validation ferme de commande, capture comptable | Reprises transitoires possibles ; aucun retour arrière après succès [183] |
| Réessayable | Après le pivot [183] | Idempotence stricte ; achèvement garanti à terme [182] [183] | Émission de facture, mise à jour d’index ou notification | Reprises durables jusqu’à complétion sans compenser l’amont [183] |
| Irréversible externe | Après pivot ou sous `HOTL` [183] [184] | Aucune compensation sémantique fiable | Courriel client définitif, déclaration légale, virement | Interdite avant pivot ; exige approbation humaine et clé unique [182] [184] |

*Tableau 9.3 — Classification transactionnelle des actions agentiques dans une Saga orchestrée.*

> **Arbitrage EA / SA** — Proscrire le protocole `2PC` dans l’orchestration agentique et imposer une classification `Compensable` / `Pivot` / `Réessayable` pour chaque outil mutateur [197] [186] [183]. Le `SA` exige le contrat `Idempotency-Key` à trois états avec contrôle d’empreinte (`400` /`409` /`422`) sur toute mutation `MCP` /`SoR`, protège les écritures locales couplées à des événements par `Transactional Outbox` sous `CDC`, et privilégie la Saga orchestrée dans le moteur durable dès trois participants [182] [198] [183] [199]. L’`EA` interdit de placer toute action externe non compensable avant le pivot transactionnel [186] [183].

## 9.4 Cycles longs `Human-on-the-Loop`, escalades asynchrones sous `SLA` et bascule multi-fournisseurs

### 9.4.1 Suspension durable `Human-on-the-Loop` : `Signals`, `Updates` et `Awakeables`

Lorsque l’autonomie gouvernée (chapitre 01) exige une validation humaine avant un pivot critique, l’attente peut s’étirer de quelques heures à plusieurs jours [176] [177]. Là où le protocole `A2A` signale l’interruption au pair appelant via `INPUT_REQUIRED` (chapitre 05), le moteur durable suspend l’instance sur disque et libère totalement threads et mémoire jusqu’à la reprise [177] [200].

Deux jeux de primitives répondent à ce besoin selon le moteur retenu [201] [200] :

1. **Dans** `Temporal`, l’*Approval Pattern* bloque l’exécution sur une condition d’attente (`wait_condition`, `condition`, `await`) alimentée par un `Signal` asynchrone ou un `Update` synchrone validé [184] [201]. Les `Queries` permettent aux portails `SoE` de lire le contexte sans bloquer le workflow, tandis que la charge d’approbation capture l’identité de l’approbateur, la décision (`APPROVED`, `REJECTED`, `ESCALATED`), les commentaires et l’horodatage à des fins d’audit [184] [201].
2. **Dans** `Restate`, les `Signals` adressés par identifiant d’invocation pilotent les interactions continues, les `Workflow promises` synchronisent les gestionnaires internes et les `Awakeables` fournissent un jeton unique à usage unique transmis à un portail de validation ou webhook [200]. L’instance libère toute ressource de calcul sans serveur jusqu’à ce qu’un appel externe résolve ou rejette l’`Awakeable` [191] [200].

### 9.4.2 Escalades asynchrones sous `SLA` et expiration compensatoire

Pour éviter qu’une absence d’opérateur ne gèle indéfiniment un dossier ou ne laisse expirer des réservations amont, le workflow fait concourir la réception du signal humain avec des minuteurs durables gérés côté serveur (`Durable Timers`) [177] [184]. Ce mécanisme supprime les tâches *cron* externes et les courses critiques entre expiration et décision tardive, car le journal d’événements tranche séquentiellement quel événement survient le premier [181] [184].

L’escalade suit un enchaînement déterministe à deux paliers [177] [199] [184]. À l’expiration d’un premier minuteur (`SLA N1`), le workflow émet une activité idempotente de relance ou de réaffectation vers un superviseur `N2` puis arme un second minuteur de clôture. Si aucun signal valide n’arrive à l’échéance finale, l’exécution bascule sur la branche d’expiration (`Timeout/Rejected`) et déroule automatiquement en ordre inverse les compensations empilées avant d’informer le demandeur [199] [184].

### 9.4.3 Bascule multi-fournisseurs préservant le déterminisme du rejeu

Enfin, les boucles durables doivent absorber les pannes prolongées ou saturations (`429`, `503`) d’un fournisseur d’inférence ou d’une région [185] [188] [202]. Le patron `Circuit Breaker` à trois états (`Closed`, `Open`, `Half-Open`) prévient l’engorgement des travailleurs en passant en échec rapide (`Open`) dès le franchissement d’un seuil d’erreurs, puis en testant prudemment le rétablissement via quelques sondes à l’issue du délai d’attente (`Half-Open`) [202]. En façade réseau, une passerelle d’inférence telle que l’`AI Gateway` d’Azure API Management ou un routeur `LiteLLM` (dont la topologie hybride complète relève du chapitre 13) applique équilibrage de charge, coupe-circuits sur pools et politiques `fallbacks` entre modèles et régions après `num_retries` [187] [203].

Toutefois, côté moteur durable, un impératif s’impose : **l’exécution du coupe-circuit et de la bascule multi-fournisseurs doit impérativement résider à l’intérieur de l’**`Activity` **ou du bloc** `ctx.run()`**, jamais dans le code pur du workflow** [190] [192]. Évaluer directement dans le workflow l’état mutable d’un coupe-circuit pour changer de fournisseur provoquerait une divergence lors d’un rejeu ultérieur si l’état du circuit avait entre-temps évolué [190]. Encapsulée dans l’activité, la tentative retient un fournisseur sain, retourne à la fois le texte produit, l’identifiant du modèle effectivement exécuté et le motif éventuel de bascule ; au rejeu, le moteur restitue cette sortie immuable sans ré-exécuter d’inférence [181] [191]. Le modèle retenu est simultanément transmis à la télémétrie et aux garde-fous `SRE` décrits au chapitre 11. La figure 9.4 illustre cette séquence complète.

> **[Figure]**
> - Workflow Durable (Suspendu hors RAM)
> - Activity Inférence
> - + Circuit Breaker
> - LLM Principal
> - (Région A)
> - LLM Secours (Région B / Souverain)
> - Portail HOTL (Signals / Awakeables)
> - Approbateurs
> - (N1 -> N2)
> - Workflow Durable (Suspendu hors RAM)
> - Activity Inférence
> - + Circuit Breaker
> - LLM Principal
> - (Région A)
> - LLM Secours (Région B / Souverain)
> - Portail HOTL (Signals / Awakeables)
> - Approbateurs
> - (N1 -> N2)
> - 1. Bascule multi-fournisseurs journalisée (préservation du replay)
> - 1 Exécuter nœud cognitif (étape S3)
> - 2 Requête inférence
> - 3 HTTP 429 / 503 répétés (seuil dépassé)
> - Coupe-circuit passe à Open. Bascule vers fournisseur secondaire.
> - 4 Requête de repli (contrat typé identique)
> - 5 HTTP 200 Réponse + proposition P3
> - 6 Journalise (fournisseur=LLM2, sortie=P3)
> - En cas de replay ultérieur, Wf lit LLM2/P3 depuis le journal sans ré-interroger LLM1 ni LLM2.
> - 2. Attente asynchrone HOTL et escalade sous SLA
> - 7 Émet demande d'approbation (Awakeable ID / Workflow ID)
> - 8 Démarre Durable Timer (SLA N1 = 4 heures)
> - Libère thread et RAM. Zéro consommation de worker.
> - 9 Notifie Approbateur N1
> - Délai SLA N1 expiré sans réponse
> - 10 Déclenche escalade vers N2 + nouveau Durable Timer (SLA N2)
> - 1 1 Notifie Approbateur N2 (prioritaire)
> - 12 Valide dossier P3
> - 13 Signal / Resolve Awakeable (APPROUVÉ, identité, horodatage)
> - 14 Reprend et engage le pivot transactionnel

*Fig. 36. – Séquence de bascule multi-fournisseurs journalisée et d’escalade Human-on-the-Loop sous SLA*

| Classe de processus | Délai SLA d’attente HOTL | Escalade et expiration | Bascule multi-fournisseurs | Contrainte EA |
| --- | --- | --- | --- | --- |
| Transaction financière ou contractuelle | Court à moyen (minutes à heures) [184] | Relance `N1`, escalade `N2`, compensation automatique à l’échéance [199] [184] | Repli restreint aux fournisseurs et régions homologués [187] [203] | Piste d’audit signée (`approver`, décision, horodatage) [184] |
| Processus interne structurant (achats, RH, IT) | Moyen à long (heures à plusieurs jours) [177] [184] | `Durable Timer` sans RAM ; réaffectation vers file d’équipe puis annulation [177] [200] | Bascule via `AI Gateway` / `LiteLLM` avec coupe-circuit multi-régions [187] [203] | Maîtrise des coûts de rétention et continuité d’équipe [177] |
| Dossier souverain ou réglementé | Long (jusqu’à plusieurs semaines) [177] | `Signal` / `Awakeable` avec re-vérification de fraîcheur à la reprise [201] [200] | Repli exclusif vers enclave souveraine interne ; arrêt propre sinon [202] [203] | Interdiction de débordement hors juridiction autorisée [187] |
| Analyse asynchrone tolérante à la latence | Sans objet (autonome borné) | Échec rapide si budget épuisé ; alerte opérateur asynchrone [178] [202] | Cascade complète après `num_retries` avec `jitter` [178] [203] | Traçabilité du modèle effectif pour `EvalOps` (chapitre 11) [181] |

*Tableau 9.4 — Grille d’arbitrage des escalades* `HOTL` *sous* `SLA` *et des bascules multi-fournisseurs.*

> **Arbitrage EA / SA** — Implémenter toute attente `Human-on-the-Loop` par primitives durables (`Signals` /`Updates` avec `wait_condition` dans Temporal ou `Awakeables` /`Signals` dans Restate) couplées à des minuteurs serveur sous `SLA`, sans jamais immobiliser de processus ni recourir à la scrutation [177] [184] [200]. Le `SA` confine l’appel `LLM`, le coupe-circuit et la bascule multi-fournisseurs dans une `Activity` ou un bloc `ctx.run()` retournant le fournisseur retenu afin de préserver le déterminisme du rejeu [190] [192] [203]. L’`EA` limite les chaînes de repli aux juridictions homologuées et impose la compensation automatique en fin de `SLA` [199] [184] [187].

## Synthèse et transition vers la Partie IV

L’exécution durable ancre la fiabilité opérationnelle de l’entreprise agentique. En remplaçant la mémoire volatile par un journal déterministe isolant les appels externes (`Activities` ou `ctx.run`), en sécurisant les mutations via `Idempotency-Key` à trois états et `Transactional Outbox`, en ordonnant les Sagas compensatoires autour d’un pivot et en suspendant les attentes `HOTL` sous `SLA`, l’architecture concilie fragilité réseau et rigueur des `SoR` [181] [191] [182] [183] [184]. La Partie III achève ainsi la couche d’exécution et de coordination (chapitres 07 à 09) avant d’aborder au chapitre 10 la sécurité `Zero-Trust` et les identités non humaines (`NHI`).
