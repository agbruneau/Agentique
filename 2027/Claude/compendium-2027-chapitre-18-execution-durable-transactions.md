# Chapitre 18 — Exécution durable et transactions

*Question directrice : que se passe-t-il quand un agent tombe en panne au milieu d'une tâche ?*

> **Version 2 — 11 novembre 2026.** État de référence : prépublication SagaLLM (arXiv 2503.11951, version 3 du 9 juillet 2025), brouillon IETF `draft-ietf-httpapi-idempotency-key-header-08` du 22 octobre 2026, documentation des éditeurs consultée le 11 novembre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [13] sont des pages primaires lues pour ce chapitre, [14] et [15] n'ont pas pu être lues. Les renvois « chapitre N » ont été vérifiés contre les chapitres rédigés. Chapitre audité et révisé le 12 novembre 2026.

Un agent chargé d'un remboursement a annulé la commande, crédité la carte, puis son processus est tué avant le courriel de confirmation. Au redémarrage, trois questions se posent : qu'est-ce qui a été fait, que peut-on refaire sans dommage, et que faut-il défaire ? Un agent qui ne sait pas y répondre recommence tout, et le client est remboursé deux fois, ou ne recommence rien, et la tâche reste à moitié faite.

L'exécution durable répond à la première question : elle garantit qu'un programme reprend là où il s'est arrêté. Elle ne répond pas aux deux autres. La thèse de ce chapitre tient en trois propositions. Un moteur durable garantit la reprise du programme, pas l'unicité de ses effets sur le monde. L'effet unique se construit, outil par outil, avec l'idempotence et la compensation. Ce qui n'est ni idempotent ni compensable se place derrière un point de non-retour explicite. Le modèle de langage ajoute deux contraintes : il ne se rejoue pas à l'identique, et il n'est pas un bon juge de sa propre reprise.

---

## 18.1 Tâches longues et pannes

### Pourquoi les tâches d'agent durent

Une tâche d'agent enchaîne des appels au modèle, des appels d'outils et des attentes : une approbation humaine, un traitement par lots, la réponse d'un autre agent. Les moteurs du marché sont dimensionnés en conséquence. Temporal n'impose aucune limite de durée à une exécution, qu'elle prenne des secondes ou des années [2]. AWS annonce des exécutions pouvant durer jusqu'à un an [9]. Microsoft parle d'orchestrations de plusieurs jours ou semaines [11]. Sur de telles durées, la panne n'est pas un accident : un redéploiement, un quota atteint ou une coupure de réseau surviendront à coup sûr.

### Cinq pannes, deux natures

| Panne | Ce qui est perdu | Qui la traite |
|---|---|---|
| Arrêt du processus | L'état en mémoire, dont le contexte du modèle | Le moteur durable |
| Délai dépassé, coupure de réseau | La réponse; l'effet a peut-être eu lieu | L'idempotence de l'outil |
| Échec d'un système appelé | Rien, mais la tâche est bloquée | Nouvel essai, puis compensation |
| Redéploiement en cours d'exécution | La correspondance entre code et historique | La gestion de versions |
| Plan erroné du modèle | Rien; l'exécution est fidèle à un mauvais plan | La validation indépendante |

Les quatre premières sont des pannes d'infrastructure. La dernière est une panne sémantique : tout s'est exécuté correctement, et le résultat est faux. Un moteur durable ne la voit pas. Il rejouera fidèlement une décision erronée.

Le deuxième cas est le plus retors. La requête est partie, la réponse n'est pas revenue : l'appelant ne sait pas si l'effet s'est produit. MCP l'inscrit désormais dans le protocole : depuis la révision du 28 juillet 2026, une requête dont le flux se rompt est réémise par le client, sous un nouvel identifiant (chapitre 5).

Le premier cas prend chez l'agent une forme propre : la perte de contexte. La fenêtre du modèle est un état volatil. Si elle n'est pas enregistrée, l'agent qui redémarre ne sait plus pourquoi il agissait. SagaLLM range cette perte parmi les quatre faiblesses de la planification par LLM, avec l'autovalidation peu fiable, l'absence de garde-fous transactionnels et la coordination insuffisante entre agents [1].

---

## 18.2 État et checkpointing

### Quel état enregistrer

SagaLLM distingue trois états [1]. L'**état applicatif** décrit les entités du domaine et leurs instantanés. L'**état des opérations** conserve les entrées, les sorties, l'horodatage, les traces de raisonnement du modèle et les métadonnées de compensation. L'**état des dépendances** tient les contraintes, leurs critères de satisfaction et le graphe qui les relie. Cette troisième catégorie est souvent oubliée. Or c'est elle qui permet, après une panne, de savoir quelles étapes en aval sont invalidées.

Cet état d'exécution n'est pas la mémoire de l'agent, qui sert un usage futur et relève du chapitre 14. Sa localisation et la détention de ses clés relèvent du chapitre 46 (section 46.1).

### Deux mécanismes

**L'instantané.** L'état est écrit à intervalles dans un magasin. LangGraph procède ainsi : un *checkpointer* enregistre l'état du graphe pour un fil d'exécution désigné par un `thread_id` [5]. Le moment de l'écriture se règle par un paramètre de durabilité à trois valeurs : `sync` écrit avant le début de l'étape suivante, `async` écrit pendant qu'elle s'exécute, `exit` n'écrit qu'à la sortie du graphe [6]. Le choix est un arbitrage entre débit et fenêtre de perte.

**Le journal rejoué.** Chaque opération est consignée avec son résultat. Après une panne, le code est réexécuté depuis le début, mais les opérations déjà terminées ne sont pas refaites : leur résultat est lu dans le journal. Temporal appelle ce journal l'*Event History*, et le rejeu vérifie que les commandes produites par le code correspondent à l'historique [2]. Restate décrit le même principe [8], AWS aussi : le code repart du début et saute les points de contrôle achevés [9].

### La contrainte de déterminisme

Le rejeu suppose que le code d'orchestration reprenne le même chemin. Microsoft le dit en toutes lettres : déterministe signifie que le code s'exécute de la même manière quand il est rejoué après une panne [11].

Un appel à un modèle de langage ne satisfait pas cette condition. La conséquence, déduite ici du fonctionnement décrit par ces documentations, est qu'un appel au modèle doit être traité comme un effet de bord : il est enveloppé dans une étape dont la sortie est journalisée. Au rejeu, la décision enregistrée est relue; le modèle n'est pas réinterrogé. La boucle de l'agent devient ainsi déterministe par construction, sans que le modèle le soit.

### Granularité, versions, croissance

**L'étape est l'unité de reprise.** Temporal donne un exemple : si une activité enchaîne trois opérations et que la troisième échoue, le nouvel essai refait les trois; il recommande donc de les séparer [4]. Chaque appel d'outil à effet mérite sa propre étape.

**Le code change pendant que la tâche court.** AWS met en garde contre le renommage d'une étape pendant que des exécutions sont en cours : le moteur ne peut plus associer l'état sauvegardé à sa définition [10]. Microsoft demande de vérifier la compatibilité de rejeu avant de brancher un exécutant mis à jour sur d'anciens historiques [11]. Par extension, modifier le prompt système, la liste d'outils ou le modèle d'un agent revient à modifier le code d'une exécution en cours, et demande la même discipline de versions. Le chapitre 34 propose de réunir cet ensemble sous un manifeste de version unique, soumis à une barrière de rejeu (section 34.2).

**L'état grossit.** LangGraph conseille d'élaguer les points de contrôle ou de fixer une politique de rétention [5]. Temporal offre *Continue-As-New*, qui poursuit une exécution dans un nouveau maillon de la même chaîne [2].

**Le piège du pilote.** Les magasins en mémoire de LangGraph perdent tout au redémarrage; la documentation recommande une base de données en production [5]. Un prototype qui « reprend » en démonstration peut donc ne rien reprendre en exploitation.

---

## 18.3 Sémantiques de livraison et idempotence

### Trois sémantiques

La documentation de Kafka publiée par Confluent donne les définitions de référence [12]. **Au plus une fois** : un message peut être perdu, jamais redélivré. **Au moins une fois** : aucun message n'est perdu, mais un message peut être livré plusieurs fois. **Exactement une fois** : chaque message est livré une seule fois, même en cas de panne.

La troisième n'existe qu'à l'intérieur d'un système fermé. Kafka l'obtient en écrivant la position du consommateur dans la même transaction que sa sortie. Dès que la sortie va vers un système externe, il faut que ce système stocke la position avec la donnée; sinon, la garantie par défaut redevient « au moins une fois » [12].

### Ce que les moteurs garantissent vraiment

Les éditeurs formulent cette frontière avec une franchise inégale.

Temporal garantit qu'une activité dont la politique autorise les nouveaux essais sera *observée* comme terminée exactement une fois, tout en précisant qu'elle peut s'exécuter, voire s'achever en partie, plusieurs fois. Le cas type : un exécutant finit le travail, tombe avant d'en rendre compte, et l'activité est relancée [4]. Microsoft est plus direct : le checkpointing durable ne rend ni les outils ni les écritures externes transactionnels ou exécutés exactement une fois; une panne survenue après une écriture externe, mais avant la validation durable, peut faire rejouer l'opération [11]. Restate écrit qu'une invocation s'exécute exactement une fois quelles que soient les pannes [8]; à la lumière des deux précédents, cette promesse se lit comme valable pour ce que le moteur journalise, non pour le système tiers au bout de l'appel.

La règle pratique en découle : **effet unique = livraison au moins une fois + outil idempotent**.

### La clé d'idempotence

Une opération est idempotente si l'exécuter plusieurs fois donne le même résultat que l'exécuter une fois [4]. Une lecture l'est par nature, de même qu'une écriture qui fixe une valeur absolue. Créer, incrémenter, envoyer ou payer ne le sont pas.

Pour ces opérations, l'appelant joint une clé unique, et le système appelé reconnaît les doublons. Temporal précise deux points [4] : l'idempotence est assurée par le service appelé, non par le code de l'activité, et la clé peut combiner l'identifiant d'exécution et celui de l'activité.

Un brouillon de l'IETF normalise ce patron pour HTTP. L'en-tête `Idempotency-Key` rend tolérantes aux pannes des méthodes non idempotentes comme POST et PATCH [7]. Trois règles en ressortent :

- la clé doit être unique et ne doit pas être réutilisée avec un contenu différent; le serveur peut y joindre une empreinte du contenu pour le vérifier;
- un nouvel essai reçu pendant que la requête d'origine est en cours devrait recevoir une réponse 409; une clé réutilisée avec un autre contenu, une réponse 422; une clé manquante là où elle est exigée, une réponse 400;
- la ressource doit publier sa spécification d'idempotence, y compris, s'il y a lieu, sa politique d'expiration des clés.

Le texte en est à la révision 08, document actif du groupe de travail `httpapi`, et n'est pas une RFC.

### Le piège propre aux agents

Deux erreurs de conception annulent la protection.

**Laisser le modèle fabriquer la clé.** Après une reprise, un modèle réinterrogé peut produire un appel légèrement différent et une clé nouvelle : le doublon passe. La clé doit dériver de l'identité durable de l'étape, comme le suggère Temporal, et être injectée par l'orchestrateur. Microsoft donne une consigne voisine pour ses propres réponses sans résultat : ne pas en déduire l'issue de l'historique de conversation, ni les resoumettre automatiquement sous une nouvelle identité [11].

**Confondre identifiant de requête et clé d'idempotence.** Dans MCP, une requête réémise porte un nouvel identifiant (chapitre 5). L'identifiant de protocole ne permet donc pas au serveur de reconnaître un doublon. La clé doit voyager comme argument de l'outil, et le schéma de l'outil doit l'exiger.

La combinaison clé et empreinte a un bénéfice secondaire. Si l'agent, après reprise, renvoie la même clé avec des arguments différents, le serveur répond 422 : la divergence entre le plan d'origine et le plan repris devient visible au lieu de produire un second effet. Le commerce agentique rencontre le même problème sous l'angle de la sécurité, car une réémission légitime ressemble au rejeu d'un mandat par un attaquant (chapitre 10).

---

## 18.4 Patron Saga et compensation

### Le principe

Les outils d'un agent touchent des systèmes qui ne partagent aucun coordinateur de transactions. Le patron Saga remplace la transaction globale par une suite de transactions locales. SagaLLM en reprend la définition d'origine, attribuée à Garcia-Molina et Salem (1987) [1][14] : une transaction de longue durée est découpée en sous-transactions T1 à Tn, chacune atomique localement et associée à une compensation; si une étape échoue, les compensations des étapes déjà validées s'exécutent en ordre inverse, de Cn à C1.

### Ce qui est relâché

Les auteurs disent relâcher les garanties ACID strictes sans dresser le bilan propriété par propriété [1]. La lecture de leur formalisation donne ceci. L'atomicité n'est plus « tout ou rien » : elle est obtenue par compensation. La cohérence est maintenue comme préservation d'invariants entre agents. La durabilité repose sur l'enregistrement des états validés. L'isolation est posée comme exigence, sans mécanisme décrit.

Ce dernier point est le prix du patron. Entre une étape et sa compensation, l'état intermédiaire est visible : un autre agent peut lire une réservation qui sera annulée, et décider sur cette base.

### Compenser n'est pas annuler

Une compensation est une nouvelle action qui rétablit un état acceptable; elle n'efface pas la première. L'exemple de SagaLLM le montre : compenser une réservation de vol, c'est annuler le billet, libérer le siège, rembourser et rétablir le budget [1]. Le client aura vu passer un débit puis un crédit.

La reprise suit cinq étapes dans SagaLLM [1] : détecter l'échec, analyser le graphe de dépendances, exécuter les compensations en ordre inverse, vérifier l'état obtenu, puis replanifier la partie touchée à partir du contexte conservé. Le recours à une personne n'intervient que si la replanification ne satisfait pas les contraintes.

### Qui écrit la compensation

SagaLLM range la vérification formelle du code de compensation généré par un LLM parmi ses travaux futurs [1]. Autrement dit, rien ne garantit aujourd'hui qu'une compensation improvisée par le modèle rétablisse l'état. La règle prudente en découle : la compensation est déclarée par le propriétaire de l'outil, enregistrée avec lui, et l'agent ne fait que la déclencher.

Une compensation s'exécute sous le même régime que le reste, au moins une fois. Elle doit donc être elle-même idempotente, et son échec doit avoir une issue prévue, en général l'escalade vers une personne.

Le patron se décline en orchestration, où un coordinateur déclenche étapes et compensations, ou en chorégraphie, où chaque participant réagit aux événements des autres (chapitre 19).

---

## 18.5 Validation indépendante et reprise

### Ne pas laisser l'agent juger sa reprise

Après une panne, quelqu'un doit décider si l'état est cohérent et quoi faire ensuite. Confier cette décision à l'agent qui a échoué est le choix par défaut, et le moins sûr. SagaLLM soutient que les LLM manquent d'autovalidation robuste et cite des travaux selon lesquels l'autocorrection ne répare pas de façon fiable les erreurs logiques profondes [1].

L'architecture proposée sépare deux contrôles. La **validation intra-agent** vérifie la sortie d'un agent : syntaxe, sémantique, exactitude factuelle, respect des contraintes, préservation du contexte. La **validation inter-agents** vérifie les messages échangés : conformité au contrat, dépendances satisfaites, cohérence entre agents, ordre temporel, accord sur l'état partagé. Un agent de validation global, extérieur aux agents de tâche, voit l'historique, les communications et l'état complets. Trois réponses sont prévues : le rejet, qui déclenche la compensation; l'augmentation, qui ajoute des précisions; la rétroaction, consignée pour adaptation [1].

Ce découpage rejoint un constat du chapitre 21 (section 21.4) : les défauts de vérification forment une catégorie entière des échecs multi-agents, et la seule présence d'un vérificateur ne suffit pas s'il contrôle la forme plutôt que l'objectif.

### Ce que la validation vérifie à la reprise

Trois vérifications s'imposent, la première découlant directement de la section 18.3.

- **Le journal et le monde concordent-ils ?** Pour toute étape dont l'issue est inconnue, l'état du système cible est relu avant tout nouvel essai.
- **Les contraintes tiennent-elles encore ?** Le monde a bougé pendant l'arrêt : un prix a changé, un créneau s'est fermé. C'est le scénario de replanification réactive que SagaLLM met à l'épreuve [1].
- **Les étapes en aval restent-elles valides ?** Le graphe de dépendances désigne celles qu'une compensation invalide.

### Quatre issues

| Situation | Issue |
|---|---|
| Panne transitoire, outil idempotent | Nouvel essai de l'étape |
| Contrainte devenue fausse | Replanification à partir du dernier point de contrôle |
| Objectif inatteignable | Compensation en ordre inverse, puis abandon |
| Compensation en échec ou état incertain | Escalade vers une personne |

Les nouveaux essais se bornent. AWS note que les exécutions durables en échec ne sont pas relancées automatiquement après une invocation asynchrone, et recommande une file de lettres mortes pour conserver l'événement d'origine [10]. Chaque replanification consomme en outre des jetons (chapitre 40).

### Le niveau de preuve

SagaLLM est un argument de conception, pas une mesure. L'évaluation porte sur quatre problèmes du banc d'essai REALM, deux de planification séquentielle et deux de planification réactive, et compare le cadriciel à Claude 3.7, DeepSeek R1, GPT-4o et GPT-o1 employés seuls; les résultats sont décrits cas par cas, sans taux de réussite [1]. Le texte se présente comme un retour d'expérience et renvoie les algorithmes à un article compagnon, ALAS.

---

## 18.6 Moteurs d'exécution durable

### Deux familles

La première réunit des moteurs généralistes, qui hébergent la boucle de l'agent comme n'importe quel workflow. La seconde réunit les cadriciels d'agents dotés de leur propre persistance (chapitre 20). Microsoft trace lui-même la frontière : le stockage de points de contrôle de ses workflows standards aide à reprendre une exécution dans le runtime de l'agent, tandis que son extension durable exécute le workflow sur une infrastructure qui le récupère à travers des exécutants distribués [11].

| Moteur | Mécanisme | Ce que la documentation dit des effets | À noter |
|---|---|---|---|
| Temporal [2][3][4] | Journal d'événements rejoué | Activités à rendre idempotentes; relance automatique selon une politique | Aucune limite de durée; un *heartbeat* sert de point de contrôle interne |
| Restate [8] | Journal rejoué; l'état voyage avec chaque requête | Déduplication par clé d'idempotence | Serveur en un seul binaire; services sans état |
| AWS Lambda durable functions [9][10] | Points de contrôle et rejeu | Étapes avec nouveaux essais; pas de relance automatique de l'exécution | Jusqu'à un an; attentes non facturées |
| Extension durable de Microsoft Agent Framework [11] | Orchestrations déterministes sur Durable Task | Ni transactionnel ni « exactement une fois » pour les écritures externes | Azure Functions ou calcul autogéré; paquets en préversion |
| LangGraph [5][6] | Instantanés par fil | Non traité dans les pages lues | Trois modes de durabilité |

AWS situe par ailleurs ses fonctions durables par rapport à Step Functions : les premières s'écrivent en code dans Lambda, le second est un service distinct fondé sur un langage de graphe [9].

### Ce que les moteurs apportent aux agents

Trois apports dépassent la reprise sur panne.

**L'attente gratuite.** Une exécution suspendue ne consomme pas de calcul chez AWS [9], ni chez Microsoft en hébergement sans serveur [11]. Un point d'approbation humaine qui dure trois jours ne coûte donc rien, ce qui lève un frein à l'humain dans la boucle (chapitre 22).

**La session durable.** L'extension de Microsoft conserve la conversation de l'agent à travers pannes, redémarrages et mises à l'échelle [11]. L'état volatil de la section 18.1 devient un état géré.

**L'historique comme piste d'audit.** Le journal qui sert au rejeu documente aussi ce que l'agent a décidé et fait à chaque étape (chapitres 17 et 33).

### La durabilité entre organisations

Un moteur durable s'arrête à la frontière de l'organisation. Au-delà, ce sont les protocoles qui portent la poignée durable : l'identifiant de tâche de l'extension Tasks de MCP survit à la connexion (chapitre 5), et A2A définit un cycle de vie de tâche (chapitre 6). L'un et l'autre désignent une tâche; ils ne disent rien de ce que le serveur fait d'une réémission. L'effet unique redevient alors une clause d'interface : UCP demande au marchand d'imposer l'idempotence contre les doubles débits (chapitre 10), et le chapitre 45 subordonne tout règlement à un rapprochement à trois voies, un paiement indu se traitant par compensation (section 45.7).

Aucun banc d'essai indépendant comparant ces moteurs sous charge agentique n'a été lu pour ce chapitre. Le tableau reflète ce que chaque éditeur dit de son produit.

---

## 18.7 Actions irréversibles : les points de non-retour

### Ce qui ne se compense pas

Certaines actions n'ont pas de compensation : un courriel envoyé, une donnée divulguée, un virement réglé, une suppression définitive, une commande à un équipement (chapitres 28 et 46). La Saga suppose que chaque étape a son inverse. Ces actions brisent l'hypothèse.

### Ordonner autour d'un pivot

La pratique des architectures de microservices, rapportée ici de connaissance générale, classe les étapes d'une Saga en trois groupes : les étapes compensables, une étape pivot après laquelle on ne revient plus, et des étapes rejouables qui finiront par réussir. Le plan d'un agent devrait suivre cet ordre. Tout ce qui peut échouer se place avant le pivot. Après lui, seule la reprise vers l'avant est possible; les étapes restantes doivent donc être idempotentes.

L'ordre n'est pas laissé au modèle. La classe de chaque outil, soit lecture, compensable, pivot ou rejouable, s'inscrit au registre et s'applique par l'orchestrateur ou la passerelle. Les annotations qu'un serveur MCP déclare sur ses propres outils ne suffisent pas, puisque le client doit les tenir pour non fiables (chapitre 5).

### Repousser l'irréversibilité

Quatre techniques réduisent la part de l'irréversible.

- **Réserver avant de confirmer.** Une autorisation de paiement précède la capture; une réservation provisoire précède l'émission. L'action irréversible devient une action compensable suivie d'une confirmation.
- **Préparer sans émettre.** L'agent dépose le courriel ou l'écriture dans une zone d'attente; l'émission est une étape distincte, déclenchée après validation. Pour les données, c'est le patron Write-Audit-Publish (chapitre 47, section 47.5).
- **Rendre l'annulation possible.** GoEX défend la validation après coup : juger une action sur son résultat est souvent plus facile que de la juger d'avance, à condition de pouvoir l'annuler [13].
- **Confiner les dégâts.** Quand l'annulation est impossible, la même proposition borne la portée de ce que l'action peut toucher [13]. Des plafonds de montant et des périmètres d'accès étroits y concourent (chapitre 30).

### L'approbation au pivot

Le pivot est l'endroit naturel d'un point d'approbation humaine. Deux précautions tiennent à l'exécution durable.

L'approbation est un résultat d'étape : elle se journalise comme les autres. Sinon, une reprise repose la question à l'approbateur ou, pire, franchit le pivot sans réponse enregistrée.

L'approbation porte sur des paramètres exacts. Si une replanification modifie le montant ou le destinataire, l'approbation précédente ne vaut plus. L'empreinte de la section 18.3 sert ici : approbation et clé d'idempotence se lient au même contenu. Le protocole LAP fait de cette liaison une primitive : un jeton de confirmation lié à l'empreinte des paramètres et à usage unique (chapitre 7).

Reste le cas où le pivot a été franchi à tort. Il ne relève plus de la transaction, mais de la gestion d'incident (chapitre 34).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Persistance de l'état | Magasin durable dès le premier environnement partagé | Prototype jetable : magasin en mémoire |
| Mécanisme de reprise | Journal rejoué pour les tâches à effets externes | Agent conversationnel sans effet : instantanés par fil |
| Appel au modèle | Étape journalisée, relue au rejeu | — |
| Granularité | Une étape par appel d'outil à effet | Lectures groupées dans une même étape |
| Moment d'écriture | Synchrone avant toute étape à effet | Asynchrone pour les étapes sans effet, si le débit l'exige |
| Garantie visée | Au moins une fois, avec outils idempotents | Au plus une fois pour une action irréversible sans clé possible |
| Clé d'idempotence | Dérivée de l'étape durable, exigée par le schéma de l'outil | Outil idempotent par nature |
| Compensation | Déclarée par le propriétaire de l'outil, idempotente | Jamais générée à la volée pour un système d'enregistrement |
| Décision de reprise | Validateur distinct de l'agent de tâche | Tâche à faible enjeu : nouvel essai borné |
| Action irréversible | Après le pivot, avec approbation liée aux paramètres | Montant sous un plafond fixé par classe de décision |
| Changement de prompt, d'outils ou de modèle | Versionné; les exécutions en cours finissent sur l'ancienne version | Correctif de sécurité : arrêt et compensation |
| Échec définitif | File de lettres mortes et escalade humaine | — |

---

## Points à retenir

- L'exécution durable garantit qu'un programme reprend, pas que ses effets sur le monde n'ont lieu qu'une fois. Microsoft l'écrit explicitement dans sa documentation.
- « Exactement une fois » ne vaut qu'à l'intérieur d'un système fermé. Vers un système externe, l'effet unique s'obtient par une livraison au moins une fois et un outil idempotent.
- La clé d'idempotence dérive de l'étape durable et voyage comme argument de l'outil. Ni le modèle ni l'identifiant de requête du protocole ne peuvent en tenir lieu.
- Un appel au modèle est un effet de bord : sa sortie se journalise et se relit au rejeu.
- Changer le prompt, les outils ou le modèle d'un agent, c'est changer le code d'exécutions en cours.
- Une Saga relâche l'isolation : les états intermédiaires sont visibles des autres agents.
- La compensation appartient au propriétaire de l'outil. Rien ne garantit la justesse d'une compensation générée par le modèle.
- La reprise se décide hors de l'agent qui a échoué. L'appui universitaire de ce principe reste qualitatif.
- Les actions irréversibles se placent après un pivot explicite, avec une approbation journalisée et liée aux paramètres exacts.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning — arXiv 2503.11951v3](https://arxiv.org/html/2503.11951v3) (résumé et texte)
2. [Temporal — Workflow Execution](https://docs.temporal.io/workflow-execution)
3. [Temporal — Activities](https://docs.temporal.io/activities)
4. [Temporal — Activity Definition](https://docs.temporal.io/activity-definition)
5. [LangGraph — persistance et checkpointers](https://docs.langchain.com/oss/python/langgraph/durable-execution) (l'adresse sert la page sur la persistance)
6. [LangGraph — référence du type `Durability`](https://reference.langchain.com/python/langgraph/types/Durability)
7. [IETF — The Idempotency-Key HTTP Header Field, draft-08](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/)
8. [Restate — Durable Execution](https://docs.restate.dev/concepts/durable_execution)
9. [AWS — Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
10. [AWS — Best practices for Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-best-practices.html)
11. [Microsoft Agent Framework — Durable Extension](https://learn.microsoft.com/en-us/agent-framework/hosting/durable-extension) (page datée du 31 août 2026, mise à jour le 6 novembre 2026)
12. [Confluent — Kafka, sémantiques de livraison](https://docs.confluent.io/kafka/design/delivery-semantics.html)
13. [GoEX: Perspectives and Designs Towards a Runtime for Autonomous LLM Applications — arXiv 2404.06921](https://arxiv.org/abs/2404.06921) (résumé)

Sources non lues :

14. [Garcia-Molina et Salem, « Sagas », SIGMOD 1987](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf) — PDF numérisé, illisible par l'outil; citée d'après [1].
15. [Agentic AI Pipelines for Enterprise Decision-Making (Nexus)](https://consensus.app/papers/details/22a0c58efa5153b194fcbf5d89fbe04c/) — fiche inaccessible (erreur 403), original introuvable.

## Limites de ce chapitre

- **L'architecture Nexus, second appui prévu par la table des matières, n'a pas été lue** [15]. Deux recherches par titre n'ont retrouvé ni l'article ni son éditeur, et la carte thématique n'en donne que le titre. Le chapitre ne lui emprunte rien.
- L'article d'origine sur les Sagas [14] n'a pas été lu; sa définition est reprise de SagaLLM. Ce que cet article dit des actions non compensables n'a donc pas pu être cité.
- Viennent de la connaissance générale, non d'une page lue : le classement des étapes en compensables, pivot et rejouables; les patrons d'autorisation puis capture et de zone d'attente; l'absence de coordinateur de transactions commun aux systèmes d'entreprise.
- Sont des déductions, non des faits lus : le traitement de l'appel au modèle comme étape journalisée, l'assimilation d'un changement de prompt, d'outils ou de modèle à un changement de version, la lecture restrictive de la promesse de Restate, les deux erreurs de conception de la section 18.3 (la première appuyée en partie par la consigne de Microsoft), et la liaison entre approbation et empreinte.
- La page de LangGraph sur l'exécution durable n'a pas été obtenue : l'adresse sert désormais la page sur la persistance. Les règles de rejeu de ce cadriciel et la valeur par défaut du mode de durabilité ne sont donc pas décrites.
- La publication de SagaLLM dans une revue n'est pas confirmée : l'arXiv n'indique aucune référence de revue, et la page porte un gabarit PVLDB aux champs non remplis. Ses 8 500 derniers caractères n'ont pas été lus.
- Relues à la source pendant l'audit du 12 novembre : [1] (historique des versions, évaluation, conclusion), [4], [7], [8], [9], [10] et [11]. Le statut de préversion de l'extension de Microsoft, auparavant déduit, est confirmé : la page parle de paquets en préversion. Les pages [2], [3], [5], [6], [12] et [13] n'ont pas été relues.
- DBOS, Inngest, Cloudflare Workflows, Dapr et Camunda ne sont pas couverts, faute de pages lues. Aucune donnée d'adoption ni de performance n'est citée.
- Les renvois aux chapitres 7, 10, 34, 45, 46 et 47 reprennent ce que ces chapitres affirment, sans relecture de leurs sources.
- Fusion et ajustement : aucun. Les sept sections suivent la table des matières.
