# Chapitre 5 — MCP : le protocole agent-outil

*Question directrice : que standardise MCP, et que laisse-t-il à l'entreprise ?*

> **Chapitre pilote, version 2 — 11 novembre 2026.** État de référence : spécification `2026-07-28` et feuille de route du 22 août 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre; toutes sont des pages primaires lues pour ce chapitre, sauf [14], marquée secondaire. Les renvois « chapitre N » ont été vérifiés contre les chapitres rédigés. Chapitre audité et révisé le 12 novembre 2026.

Un agent qui ne peut rien lire ni rien faire hors de sa fenêtre de contexte n'est qu'un interlocuteur. Dès qu'on veut qu'il consulte un dossier client, interroge un entrepôt de données ou ouvre un billet, il faut le brancher sur un système. Sans standard, chaque branchement est un développement sur mesure : chaque application d'IA écrit son connecteur pour chaque système, et le nombre d'intégrations croît comme le produit des deux.

Le Model Context Protocol (MCP) remplace ce produit par une somme. Un système expose ses capacités une fois, sous la forme d'un serveur MCP; toute application qui parle le protocole peut s'en servir. Lancé par Anthropic à la fin de 2024 et donné à l'Agentic AI Foundation dès sa création, le 9 décembre 2025, MCP est l'un des dix projets que cette fondation de la Linux Foundation héberge [13] (chapitre 11).

MCP relie un agent à ses outils. Déléguer un objectif à un autre agent relève d'A2A, et la frontière entre les deux se trace selon le contrôle que l'appelant garde sur ce qui s'exécute de l'autre côté (chapitre 6).

Ce chapitre décrit ce que le protocole fixe, puis ce qu'il laisse aux décisions d'entreprise. La révision du 28 juillet 2026, qui a déplacé plusieurs éléments d'une liste à l'autre, sert de fil conducteur.

---

## 5.1 Le modèle : hôte, client, serveur

### Trois rôles

MCP distingue trois rôles [1].

L'**hôte** est l'application d'IA elle-même : un assistant de bureau, un environnement de développement, une plateforme d'agents. Il crée les clients, applique les politiques de sécurité et de consentement, coordonne l'appel au modèle de langage et agrège le contexte.

Le **client** est un connecteur créé par l'hôte. Chaque client parle à un seul serveur. Un hôte branché sur dix serveurs fait donc tourner dix clients, et c'est cette relation un pour un qui maintient une frontière de sécurité entre les serveurs.

Le **serveur** expose des capacités ciblées : les fichiers d'un dépôt, une base de données, une API externe. Il peut être un processus local ou un service distant.

Le protocole repose sur JSON-RPC. Il décrit les messages qui circulent entre client et serveur, pas le fonctionnement interne de l'hôte.

### Quatre principes de conception

La spécification énonce quatre principes [1], et chacun a une conséquence pratique.

1. **Un serveur doit être très facile à construire.** La complexité d'orchestration reste dans l'hôte. C'est ce qui explique la prolifération rapide des serveurs, et aussi leur qualité inégale.
2. **Les serveurs doivent être composables.** Chacun fait une chose; l'hôte les combine.
3. **Un serveur ne voit ni la conversation entière ni les autres serveurs.** L'historique complet reste dans l'hôte, qui contrôle toute interaction entre serveurs. Cette isolation est la principale garantie structurelle du protocole.
4. **Les fonctionnalités s'ajoutent progressivement.** Le cœur est minimal; le reste se négocie par capacités déclarées.

### Ce qu'un serveur expose

Un serveur offre trois primitives [1].

Les **outils** (`tools`) sont des fonctions que le modèle peut invoquer : interroger une base, appeler une API, lancer un calcul. Chaque outil porte un nom, une description, un schéma d'entrée en JSON Schema et, s'il y a lieu, un schéma de sortie [4]. La spécification qualifie les outils de « contrôlés par le modèle » : c'est le modèle qui décide de les appeler, à partir de leur description.

Les **ressources** (`resources`) sont des données identifiées par un URI, que le client peut lire et auxquelles il peut s'abonner.

Les **prompts** sont des gabarits que le serveur met à la disposition de l'application.

C'est sur les outils que portent presque toutes les questions de gouvernance.

### Ce qu'un serveur peut demander en retour

Un serveur peut avoir besoin de quelque chose du client en cours de traitement. L'**élicitation** lui permet de demander une information à l'utilisateur, par formulaire ou par redirection vers une page web; depuis juillet 2026, cette demande passe par le patron d'allers-retours décrit en 5.2 [2]. Deux autres mécanismes historiques, l'échantillonnage (`sampling`, où le serveur demande une complétion au modèle de l'hôte) et les racines (`roots`, où le client indique au serveur les répertoires accessibles), sont **dépréciés** depuis la révision de juillet 2026, de même que la journalisation par le protocole [2]. Ils fonctionnent encore pendant la fenêtre de dépréciation, mais une nouvelle mise en œuvre ne devrait pas les adopter.

La spécification propose des substituts : passer les répertoires en paramètres d'outil ou en configuration, appeler directement l'API du fournisseur de modèle, journaliser sur la sortie d'erreur standard ou avec OpenTelemetry. Le mouvement est cohérent : le protocole se recentre sur l'accès aux outils et rend à l'infrastructure ce qui relève d'elle.

### La négociation de capacités

Client et serveur déclarent ce qu'ils savent faire. Depuis juillet 2026, le client joint ses capacités à **chaque requête**, et le serveur publie les siennes en réponse à une méthode dédiée, `server/discover`, que tout serveur doit mettre en œuvre [1][2]. Chaque partie doit s'en tenir à ce qui a été déclaré. Ce déplacement, de la poignée de main initiale vers la requête, est le changement central de la révision.

---

## 5.2 La révision 2026-07-28 : un protocole sans état

Jusqu'à la version `2025-11-25`, une connexion MCP commençait par une poignée de main (`initialize`), établissait une session identifiée par un en-tête, et gardait un état côté serveur. Ce modèle convenait à un serveur local lancé par un assistant de bureau. Il convenait mal à un service distant derrière un répartiteur de charge.

La révision du 28 juillet 2026 supprime cet état [2]. Sept changements en découlent.

| Changement | Avant | Depuis 2026-07-28 |
|---|---|---|
| Poignée de main | `initialize` obligatoire | Supprimée; version et capacités voyagent dans chaque requête |
| Session | En-tête `Mcp-Session-Id` | Supprimée; l'état passe par des identifiants explicites |
| Découverte | Implicite, dans la poignée de main | `server/discover`, obligatoire côté serveur |
| Notifications | Flux GET permanent, `resources/subscribe` | `subscriptions/listen`, un flux par abonnement explicite |
| Requêtes du serveur vers le client | Messages initiés par le serveur | Réponse « entrée requise », puis nouvel essai du client |
| Reprise de flux | `Last-Event-ID` | Supprimée; une requête interrompue est réémise |
| Tâches longues | Expérimentales, dans le cœur | Extension officielle distincte |

### L'état devient un argument

Sans session, un serveur ne peut plus relier implicitement deux appels. La spécification recommande un patron simple : un outil de création renvoie un identifiant (un panier, une transaction, un contexte de navigation), et les appels suivants le reçoivent en argument [4]. C'est le modèle qui transporte l'identifiant d'un appel à l'autre.

Trois précautions accompagnent ce patron. Sur un serveur authentifié, l'identifiant est un nom, pas un droit : le serveur doit vérifier l'autorisation de l'appelant à chaque appel. L'identifiant doit être opaque, pour ne pas inviter à le deviner. Sa durée de vie doit figurer dans la description de l'outil, pour que le modèle la connaisse au moment de créer l'état.

### Les allers-retours multiples

Un serveur ne peut plus envoyer de requête de sa propre initiative. S'il lui manque une information, il renvoie un résultat de type `input_required` qui énumère ce qu'il lui faut; le client rassemble les réponses et **réémet la requête d'origine** avec elles [2][3]. Tout résultat porte désormais un champ `resultType` obligatoire, qui vaut `complete` ou `input_required`.

Ce patron, appelé Multi Round-Trip Requests, a un effet d'architecture important : toute interaction reste une paire requête-réponse HTTP ordinaire. Il n'y a plus de canal de retour à maintenir ouvert.

### Des en-têtes pour les intermédiaires

La révision copie dans des en-têtes HTTP certains champs du corps JSON-RPC [3] :

```http
POST /mcp HTTP/1.1
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: execute_sql
Mcp-Param-Region: us-west1
```

`Mcp-Method` est obligatoire sur toute requête; `Mcp-Name` l'est pour un appel d'outil, une lecture de ressource ou l'obtention d'un prompt. Un serveur peut en outre désigner, par la propriété `x-mcp-header` du schéma d'entrée, des paramètres d'outil que le client est alors tenu de refléter dans des en-têtes `Mcp-Param-*` [3].

L'intention est explicite : permettre aux répartiteurs de charge, aux passerelles et aux outils d'observabilité de router et d'inspecter une requête sans analyser son corps. Une passerelle peut ainsi appliquer une limite de débit par outil, ou router par région, sur la seule foi des en-têtes.

Cette commodité crée un risque classique : deux composants qui se fient à deux sources de vérité différentes. La spécification le traite de front. Tout serveur qui lit le corps **doit** rejeter une requête dont les en-têtes ne correspondent pas au corps, avec un statut 400 et une erreur `HeaderMismatch` [3]. Un intermédiaire qui applique une politique sur la foi des en-têtes devrait en outre refuser une requête dont la version annoncée précède cette validation, ou qui n'en annonce aucune [3]. La spécification déconseille aussi de refléter un paramètre sensible, puisque les en-têtes sont visibles des intermédiaires [4].

### Le cache entre dans le protocole

Les listes d'outils, de prompts, de ressources et de modèles de ressources, ainsi que les lectures de ressources, portent maintenant deux champs obligatoires : `ttlMs`, une durée de fraîcheur, et `cacheScope`, qui vaut `public` ou `private` et indique si un intermédiaire partagé peut mettre la réponse en cache [2]. Les serveurs devraient aussi renvoyer leurs outils dans un ordre déterministe, pour faciliter le cache côté client et améliorer le taux de succès du cache de prompts du modèle quand la liste d'outils est injectée dans le contexte [2].

Ce second motif intègre au protocole une considération de coût d'inférence : l'économie des jetons pèse désormais sur la conception des standards (chapitres 13, 40 et 44). Une passerelle qui filtre les listes selon l'appelant les rend toutefois propres à chaque requête, ce qui réduit l'effet du cache (chapitre 24).

### La traçabilité

La révision documente enfin la propagation du contexte de trace OpenTelemetry dans les métadonnées de requête [2]. Un appel d'outil peut donc s'inscrire dans une trace distribuée qui commence chez l'agent et se poursuit dans le système appelé. Les conventions sémantiques qui décrivent ces traces ne sont, elles, pas encore stables, et celles qui visent MCP renvoient encore à la session supprimée (chapitre 33).

### Ce que cela change pour l'entreprise

Un serveur MCP distant devient une charge HTTP ordinaire. Il se déploie derrière un répartiteur sans affinité de session, se met à l'échelle horizontalement, se place derrière une passerelle d'API existante. La contrepartie est qu'une requête en cours est perdue si son flux de réponse se rompt : le client doit la réémettre avec un nouvel identifiant [2]. Les outils qui produisent des effets doivent donc être conçus pour supporter une réémission, ce qui ramène à l'idempotence et aux patrons de compensation du chapitre 18. Pour une consigne envoyée à un équipement, une réémission automatique devient même dangereuse (chapitre 28).

---

## 5.3 Le transport

MCP définit deux transports.

**Streamable HTTP** sert aux serveurs distants. Le serveur expose un point d'accès unique qui accepte des requêtes POST. Chaque message du client est un POST distinct. Le serveur répond soit par un objet JSON, soit par un flux d'événements (SSE) limité à cette requête, qui transporte des notifications de progression puis la réponse finale [3]. Fermer le flux vaut annulation de la requête.

**stdio** sert aux serveurs locaux, lancés comme sous-processus par l'hôte et joints par l'entrée et la sortie standard.

Deux exigences de sécurité s'attachent au transport HTTP [3]. Le serveur doit valider l'en-tête `Origin` de toute connexion entrante, pour bloquer les attaques par réassociation DNS (DNS rebinding), et répondre 403 si l'origine est invalide. Un serveur local devrait n'écouter que sur l'adresse de bouclage. Sans ces protections, un site web distant peut atteindre un serveur MCP qui tourne sur le poste d'un employé.

L'ancien transport HTTP+SSE de 2024, déprécié depuis la révision `2025-03-26`, relève désormais de la politique de dépréciation : il peut être retiré dans une révision future [2][3].

**La suite.** La coexistence de deux transports a un coût : chaque fonctionnalité fondée sur HTTP doit être repensée pour stdio, et les SDK entretiennent deux chaînes. La feuille de route vise un modèle unique, où Streamable HTTP serait parlé aussi sur l'entrée et la sortie standard, probablement au moyen de HTTP/2 [12]. Elle prévoit également d'étendre le cache aux ETags, ce qui permettrait de versionner des résultats, y compris ceux d'appels d'outils. Ce sont des orientations et non des engagements, la feuille de route le précise elle-même.

---

## 5.4 Le travail de longue durée

Un appel d'outil ne rend pas toujours la main en une seconde. Un pipeline d'intégration continue, un traitement par lots ou une approbation humaine durent des minutes, parfois des heures. Tenir une connexion ouverte tout ce temps n'est pas viable : les intermédiaires imposent des délais, et une déconnexion fait tout perdre.

### L'extension Tasks

La réponse de MCP est une extension officielle, `io.modelcontextprotocol/tasks` [7]. Quand un serveur juge qu'une requête sera longue, il renvoie un identifiant de tâche durable au lieu du résultat. Le client interroge ensuite l'état de la tâche avec `tasks/get`, fournit au besoin une information avec `tasks/update`, et peut demander l'annulation avec `tasks/cancel`.

| État | Signification |
|---|---|
| `working` | Traitement en cours |
| `input_required` | Le serveur attend une information du client |
| `completed` | Terminé; le résultat est disponible |
| `failed` | Une erreur s'est produite |
| `cancelled` | Annulé |

**C'est le serveur qui décide.** Le client déclare une fois qu'il accepte les tâches; le serveur choisit, requête par requête, de répondre directement ou par une tâche. Le client doit donc traiter les deux formes de résultat.

**L'identifiant survit à la connexion.** La tâche est créée durablement avant l'envoi de la réponse. Un client qui redémarre peut reprendre l'interrogation, à condition d'avoir conservé l'identifiant.

**L'annulation est coopérative.** Le serveur prend acte de la demande, mais n'est pas tenu d'arrêter le travail. Une tâche annulée peut tout de même se terminer.

L'état `input_required` fait de cette extension le support naturel de l'humain dans la boucle : une tâche s'arrête à un point d'approbation, expose la demande, puis reprend (chapitre 22).

### Un statut à surveiller

L'extension est au stade **bêta**, avec pour destination déclarée l'intégration au cœur du protocole [8]. À ce stade, des changements incompatibles restent permis, même s'ils sont censés être rares. Les tâches avaient d'ailleurs une première forme expérimentale dans le cœur, que la révision de juillet a retirée et redessinée [2]. Une entreprise qui bâtit dessus doit prévoir une adaptation.

### Notifications et événements

Par défaut, le client interroge le serveur à intervalles. S'il préfère être averti, il ouvre un flux `subscriptions/listen` en précisant les types de notifications qu'il veut recevoir : changement de la liste d'outils, de prompts ou de ressources, mise à jour d'une ressource suivie [2]. L'extension Tasks y ajoute ses propres notifications d'état (`notifications/tasks`), qui portent l'état complet et dispensent d'un `tasks/get` tant que le flux reste ouvert [7]. La spécification ne prévoit aucun rattrapage des notifications manquées pendant une rupture : à la reconnexion, un `tasks/get` reste nécessaire [16].

La feuille de route range ce sujet parmi ses cinq priorités, sous le nom de primitives de messagerie agentique [12]. Elle reconnaît un risque : avoir trois réponses différentes à la question « le serveur n'a pas fini », sans cycle de vie, modèle d'annulation ni surface d'erreur communs. Les travaux en cours portent sur des événements poussés par le serveur, y compris par webhooks, afin d'éviter une interrogation coûteuse. Le chapitre 19 replace ces mécanismes dans l'orchestration événementielle.

---

## 5.5 L'autorisation

C'est la partie du protocole où l'écart entre ce qui est fixé et ce qui est laissé à l'entreprise est le plus grand.

### Facultative, mais stricte

L'autorisation est **facultative** dans MCP [5]. Un serveur peut n'en exiger aucune, même si le transport HTTP recommande d'authentifier toute connexion [3]. Quand elle est mise en œuvre sur HTTP, elle suit OAuth 2.1 selon un profil précis. Sur stdio, la spécification recommande de ne pas l'appliquer et de tirer les identifiants de l'environnement.

Le serveur MCP joue le rôle de serveur de ressources OAuth, le client MCP celui de client OAuth, et un serveur d'autorisation, hébergé ou non avec le serveur MCP, émet les jetons. Le profil impose quelques règles fermes :

- le serveur MCP **doit** publier ses métadonnées de ressource protégée (RFC 9728), qui indiquent au client quel serveur d'autorisation utiliser;
- le client **doit** préciser la ressource visée dans ses demandes de jeton (RFC 8707);
- le serveur MCP **doit** vérifier qu'un jeton a été émis pour lui, et **ne doit ni accepter ni relayer** un autre jeton.

Cette dernière règle interdit le passage de jeton en aval : un serveur MCP ne peut pas réutiliser le jeton reçu pour appeler une autre API. Elle empêche qu'un jeton émis pour un service serve à en atteindre un autre, mais oblige à prévoir un échange de jeton distinct pour atteindre les systèmes derrière le serveur (chapitre 25). L'autorisation de MCP s'arrête d'ailleurs au serveur : le système qu'il pilote, un robot par exemple, garde sa propre sécurité (chapitre 46).

Les portées se demandent progressivement. Le serveur indique dans sa réponse 401 ou 403 les portées nécessaires à l'opération; le client en fait l'union avec celles déjà obtenues et relance une autorisation. Le principe du moindre privilège est ainsi inscrit dans le flux lui-même.

### L'enregistrement des clients

Un client doit obtenir un identifiant auprès du serveur d'autorisation. Trois voies existent : les Client ID Metadata Documents, où l'identifiant du client est une URL HTTPS qui pointe vers ses métadonnées; le préenregistrement; et l'enregistrement dynamique (RFC 7591). La révision de juillet 2026 recommande la première et **déprécie** la troisième, conservée pour les serveurs d'autorisation qui n'offrent pas la première [2][5]. Elle lie aussi les justificatifs du client au serveur d'autorisation qui les a émis, sans réemploi auprès d'un autre, et oblige le client à vérifier l'émetteur (`iss`) d'une réponse d'autorisation quand il est présent (RFC 9207) [2].

### Le modèle grand public ne suffit pas

Le flux de base suppose qu'une personne, devant un navigateur, consent à ce qu'un client accède à un serveur. C'est le bon modèle pour une application grand public. En entreprise, il crée trois difficultés : chaque employé doit autoriser chaque serveur un à un, l'équipe de sécurité ne peut pas imposer une politique uniforme, et le départ d'un employé exige de révoquer ses accès service par service [6].

### L'autorisation gérée par l'entreprise

L'extension Enterprise-Managed Authorization, au stade **stable**, répond à ces difficultés en plaçant le fournisseur d'identité de l'organisation au centre de la décision [6][8].

Le flux tient en quatre étapes. L'employé ouvre une session dans le client MCP avec son identité d'entreprise. Le client échange l'assertion d'identité obtenue (jeton OpenID ou assertion SAML) contre un jeton particulier, l'Identity Assertion JWT Authorization Grant (ID-JAG), auprès du fournisseur d'identité, qui évalue alors sa politique. Le client présente cet ID-JAG au serveur d'autorisation du serveur MCP, qui le valide et émet un jeton d'accès. Le client appelle enfin le serveur MCP. L'employé n'est jamais redirigé vers une page de consentement propre au serveur.

Quatre bénéfices en résultent : une politique centralisée dans les outils d'identité existants, une authentification unique, une évaluation des règles (groupe, rôle, accès conditionnel) avant toute émission de jeton, et une révocation centralisée.

Deux réserves s'imposent. D'abord, l'ID-JAG est défini par un brouillon du groupe de travail OAuth de l'IETF, et les produits suivent des révisions différentes de ce brouillon; la documentation de l'extension recommande de vérifier la révision visée par chaque fournisseur [6]. Ensuite, la prise en charge est inégale. Le 12 novembre 2026, la page de l'extension recense douze produits; quelques-uns, dont Okta, Ping Identity et Descope, émettent et acceptent des ID-JAG en version de production, tandis que d'autres n'en sont qu'à l'accès anticipé ou à l'expérimental [6]. La liste se dit non exhaustive : un produit absent n'est pas pour autant incompatible. Les conditions commerciales comptent aussi : chez Okta, l'émission incluse dans l'offre d'authentification unique est plafonnée à 250 ID-JAG par utilisateur, par application et par mois, et un volume supérieur exige un produit distinct [6].

Une seconde extension stable, OAuth Client Credentials, couvre l'authentification de machine à machine, sans utilisateur [8].

### L'identité des agents, chantier ouvert

Les concepteurs du protocole le disent sans détour : l'autorisation de MCP suppose une personne devant un navigateur au moment du consentement, alors que l'appelant est de plus en plus un agent, c'est-à-dire une charge de travail infonuagique qui agit pour un utilisateur absent ou qui lance des sous-agents censés recevoir une autorité plus étroite que la sienne [12]. En pratique, beaucoup de serveurs s'appuient encore sur des clés d'API collées à la main et sur des jetons de rafraîchissement de longue durée.

Un groupe de travail sur l'identité des agents est en formation. Son programme comprend la preuve de possession des jetons (DPoP), la fédération d'identités de charges de travail, l'ID-JAG et l'échange de jetons (RFC 8693), en coordination avec les groupes OAuth et WIMSE de l'IETF. L'attestation de présence humaine, qui distinguerait un client interactif d'un agent sans surveillance, est à l'étude [12]. Le chapitre 29 traite ce chantier dans son ensemble; le chapitre 30, la délégation à autorité réduite et l'attestation de présence humaine.

---

## 5.6 Extensions et gouvernance

### Un cœur minimal, des extensions optionnelles

La révision de juillet 2026 officialise un cadre d'extensions [2][8]. Une extension est un ajout facultatif au protocole, identifié par un préfixe de fournisseur et un nom; les extensions officielles portent le préfixe `io.modelcontextprotocol`. Client et serveur annoncent celles qu'ils prennent en charge dans leurs capacités.

Chaque extension passe par trois stades.

| Stade | Changements permis | Ce qu'on peut en attendre |
|---|---|---|
| Expérimental | N'importe lesquels, sans préavis | Rien; le concept peut disparaître |
| Bêta | Tous, les ruptures devant rester rares | Un usage réel est bienvenu; les ruptures sont documentées |
| Stable | Seulement avec une nouvelle révision du protocole | Comportement figé pour une révision donnée |

Pour devenir stable, une extension doit présenter deux mises en œuvre indépendantes et interopérables, l'une côté client et l'autre côté serveur, ainsi qu'un scénario de conformité.

À la date de rédaction, les extensions officielles sont les suivantes [8] :

- **OAuth Client Credentials** et **Enterprise-Managed Authorization** (stables);
- **MCP Apps** (stable), qui permet à un serveur d'afficher des éléments d'interface interactifs dans la conversation;
- **MCP Tasks** (bêta, destinée au cœur);
- **Skills over MCP** (bêta sans destination déclarée, bien que sa proposition SEP-2640 soit au statut Final [15]), pour découvrir et lire des Agent Skills depuis un serveur;
- **Server Cards** (bêta), pour découvrir les métadonnées d'un serveur avant de s'y connecter.

Deux règles pèsent sur les choix d'entreprise. Une extension est **toujours désactivée par défaut** et exige une activation explicite. Et un SDK n'est pas tenu de mettre en œuvre les extensions pour être conforme. Bâtir sur une extension, c'est donc vérifier sa prise en charge des deux côtés, chez chaque fournisseur. Si une seule partie la prend en charge, elle doit se rabattre sur le comportement du cœur ou rejeter la requête.

### Qui décide

MCP est constitué en série de LF Projects, LLC, structure de la Linux Foundation, qui doit aussi approuver tout changement de gouvernance; ses contributions de code et de spécification sont publiées sous licence Apache 2.0 [9]. Sa gouvernance technique est hiérarchique, sur le modèle de projets comme Python ou PyTorch : des contributeurs, des mainteneurs responsables d'un composant, des mainteneurs principaux qui orientent l'ensemble, et deux mainteneurs en chef qui ont le dernier mot.

Un point mérite l'attention d'un acheteur : les sièges appartiennent à des **personnes, non à des entreprises**. Aucun siège n'est réservé à un fournisseur. Cela ne supprime pas l'influence des employeurs, mais l'autorité formelle ne se négocie pas entre sociétés.

Toute modification de la spécification passe par une proposition écrite, la Specification Enhancement Proposal (SEP). Le travail se répartit entre des groupes d'intérêt, qui formulent les problèmes, et des groupes de travail, qui produisent les solutions. Une entreprise qui veut peser sur le protocole a donc une voie d'entrée claire : rejoindre le groupe de travail concerné et y faire porter sa proposition, les SEP soutenues par un groupe et alignées sur la feuille de route étant traitées en priorité [12].

### Une politique de dépréciation

La révision de juillet adopte une politique de cycle de vie des fonctionnalités : trois états (active, dépréciée, retirée), un registre des fonctionnalités dépréciées et une fenêtre de dépréciation d'**au moins douze mois** [2]. C'est une garantie utile pour planifier : une fonctionnalité dépréciée en juillet 2026 ne peut pas disparaître avant l'été 2027.

### Des SDK classés par niveau

Les SDK officiels sont classés en trois niveaux [10]. Le premier exige la réussite de 100 % des tests de conformité applicables, la prise en charge des nouveautés avant la publication d'une révision, un tri des signalements en deux jours ouvrables et la correction des bogues critiques en sept jours. Le deuxième exige 80 % de réussite et les nouveautés dans les six mois. Le troisième n'impose aucun seuil.

Un SDK peut être rétrogradé si ses tests échouent pendant quatre semaines consécutives. Le niveau d'un SDK est donc un critère de sélection vérifiable et révisable.

---

## 5.7 Le registre

Un protocole ne suffit pas à trouver un serveur. Le registre MCP est le dépôt central officiel de métadonnées sur les serveurs accessibles publiquement [11]. Son nom prête à confusion.

**Il est en préversion.** La page officielle prévient que des changements incompatibles ou des remises à zéro des données peuvent survenir avant la disponibilité générale.

**Il contient des métadonnées, pas du code.** Chaque serveur y est décrit par un fichier `server.json` : nom unique, emplacement (un paquet npm, une image, une URL), instructions d'exécution. Le code reste dans les registres de paquets habituels.

**Il authentifie les espaces de noms.** Les noms suivent un format de DNS inversé, lié à un compte GitHub ou à un domaine vérifié. Seul le propriétaire légitime peut publier sous son espace.

**Il ne vérifie pas le code.** L'analyse de sécurité est déléguée aux registres de paquets sous-jacents et aux agrégateurs en aval; les mainteneurs peuvent seulement retirer à la main un serveur indésirable ou malveillant. Le registre garantit qui publie, pas ce qui est publié.

**Il ne prend pas en charge les serveurs privés.** Un serveur accessible seulement sur un réseau interne n'y a pas sa place; la page recommande d'héberger pour cela son propre registre privé.

**Il n'est pas conçu pour être interrogé directement par les applications.** Il alimente des agrégateurs, tels que des places de marché, qui ajoutent curation et évaluations. Une spécification OpenAPI permet à d'autres registres d'offrir la même interface.

La conséquence pour l'entreprise est nette : il lui faut **son propre registre**. Celui-ci recense les serveurs internes, que le registre public exclut, et une sélection approuvée de serveurs publics. S'il met en œuvre l'interface standard, les applications hôtes compatibles peuvent le consulter sans adaptation. La base de code du registre officiel n'est toutefois pas prévue pour l'autohébergement. Le chapitre 8 compare les modèles de découverte, et le chapitre 24 situe ce registre par rapport aux passerelles.

---

## 5.8 Ce que MCP ne règle pas

Minimal par choix, le protocole laisse plusieurs questions d'entreprise sans réponse normative.

| Question | Ce que dit la spécification | Ce qui revient à l'entreprise |
|---|---|---|
| Faut-il une autorisation ? | Elle est facultative [5] | L'exiger sur tout serveur distant |
| Qui approuve un serveur ? | Rien; le registre n'authentifie que l'éditeur [11] | Un processus d'approbation et un registre interne |
| Le code du serveur est-il sûr ? | Analyse déléguée [11] | Analyse, épinglage de versions, surveillance |
| Peut-on se fier aux annotations d'un outil ? | Non, sauf si le serveur est de confiance [4] | Définir ce qu'est un serveur de confiance |
| Un humain valide-t-il les appels ? | « Devrait », sans obligation [4] | Une politique par classe d'action |
| Les appels sont-ils journalisés ? | Le client « devrait » le faire [4] | Une piste d'audit imposée, hors protocole |
| Deux serveurs ont un outil de même nom | Le client « devrait » lever l'ambiguïté [4] | Une convention de nommage à la passerelle |
| Quelle identité porte l'agent ? | Chantier en cours [12] | Une solution transitoire (chapitre 29) |
| Comment se comporte une passerelle ? | Non défini | Un choix de produit et de configuration (chapitres 24 et 44) |

Trois de ces lacunes appellent un commentaire.

**Les annotations ne sont pas une garantie.** Un outil peut se déclarer en lecture seule ou non destructif. La spécification exige que le client tienne ces annotations pour non fiables, sauf si elles viennent d'un serveur de confiance [4]. La description même d'un outil est du texte injecté dans le contexte du modèle, donc un vecteur d'attaque : c'est le mécanisme de l'empoisonnement d'outil, étudié au chapitre 31.

**La validation humaine est recommandée, pas imposée.** Le texte dit qu'il devrait toujours y avoir un humain en mesure de refuser une invocation, que l'application devrait montrer les entrées avant l'appel et demander confirmation pour les opérations sensibles [4]. Ce sont des « devrait ». Un hôte peut être conforme et n'en rien faire.

**La gouvernance d'entreprise n'est pas dans le cœur.** D'après un résumé de presse, la feuille de route de mars 2026 laissait délibérément ouverts les pistes d'audit, le comportement des passerelles et la portabilité de la configuration [14]. La feuille de route d'août n'en fait pas des livrables [12]. Une prépublication de juin 2026, non évaluée par les pairs, arrive à une conclusion voisine pour l'ensemble des protocoles d'agents : certaines exigences de gouvernance n'y sont pas exprimables (chapitre 11).

### Ce qui vient

La feuille de route du 22 août 2026 retient cinq priorités pour les six à douze mois suivants [12] :

1. **Primitives de messagerie agentique** : événements poussés par le serveur, composition des tâches et des abonnements.
2. **Transport unifié** : HTTP sur stdio, cache par ETags.
3. **Identité d'agent et sécurité d'entreprise** : DPoP, délégation, fédération d'identités de charges.
4. **Primitives améliorées** : forme des résultats d'outils, découverte progressive, annotations.
5. **Expérience des SDK** : contrat des extensions, génération d'artefacts à partir de la spécification.

La **découverte progressive** répond à un problème que toute entreprise rencontre vite. Un hôte branché sur des dizaines de serveurs charge des centaines de descriptions d'outils dans le contexte du modèle, ce qui coûte des jetons et dégrade le choix de l'outil. L'idée est que le client apprenne les outils d'un serveur au fur et à mesure de ses besoins, au lieu d'ingérer le catalogue entier, en accord avec les travaux sur le cache (chapitres 13 et 40).

La feuille de route avertit qu'elle reflète une réflexion en cours et non des engagements fermes : c'est une indication de direction.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Version cible du protocole | `2026-07-28` pour tout nouveau serveur distant | Clients imposés qui ne parlent qu'une version à poignée de main : prévoir la double compatibilité |
| Transport | Streamable HTTP pour le distant, stdio pour le local | Aucun cas pour HTTP+SSE, déprécié |
| Autorisation | Obligatoire sur tout serveur distant, avec vérification de l'audience | Serveur local sans données sensibles |
| Modèle d'autorisation | Enterprise-Managed Authorization si le fournisseur d'identité et les clients la prennent en charge | Sinon, flux OAuth de base avec préenregistrement des clients |
| Enregistrement des clients | Client ID Metadata Documents | Enregistrement dynamique seulement si le serveur d'autorisation n'offre rien d'autre |
| Politique à la passerelle | Sur les en-têtes `Mcp-*` des requêtes `2026-07-28` | Version antérieure ou absente : refuser, ou analyser le corps |
| État entre appels | Identifiants explicites, opaques, vérifiés à chaque appel | — |
| Opérations longues | Extension Tasks, en acceptant son statut bêta | Opération courte : flux de réponse avec notifications de progression |
| Effets de bord | Outils idempotents ou compensables | — |
| Découverte | Registre interne à interface standard | Très petit parc : configuration statique |
| SDK | Niveau 1 | Langage sans SDK de niveau 1 : niveau 2 avec plan de suivi |
| Extensions | Stables seulement en production | Bêta si le bénéfice justifie un coût d'adaptation prévu |
| Annotations d'outils | Ignorées pour toute décision de sécurité | Serveur interne dont le code est maîtrisé |

---

## Points à retenir

- MCP standardise la manière dont une application d'IA découvre et appelle des outils. Il laisse l'orchestration à l'hôte et la délégation entre agents à A2A (chapitre 6).
- Depuis la révision `2026-07-28`, le protocole est sans état. Un serveur distant est une charge HTTP ordinaire, que les passerelles peuvent router par en-têtes, à condition que le serveur valide la concordance des en-têtes et du corps.
- L'autorisation est facultative dans la spécification. C'est à l'entreprise de la rendre obligatoire.
- L'extension Enterprise-Managed Authorization confie la décision d'accès au fournisseur d'identité. Elle est stable, mais repose sur un brouillon de l'IETF et sa prise en charge varie selon les produits.
- L'identité des agents reste un chantier ouvert, de l'aveu même des mainteneurs.
- Le registre officiel est en préversion, n'authentifie que l'éditeur et exclut les serveurs privés. Un registre interne est nécessaire.
- Les tâches longues passent par une extension encore en bêta.
- Validation humaine, journalisation et confiance dans les annotations sont des recommandations. Les rendre effectives est une décision de gouvernance, pas une propriété du protocole.
- Les dépréciations disposent d'une fenêtre minimale de douze mois, et les SDK d'un classement vérifiable : deux appuis concrets pour planifier.

---

## Sources

Pages primaires lues le 11 novembre 2026; [2], [3], [6], [7], [8], [9], [11] et [12] relues le 12 novembre 2026 pour l'audit :

1. [Architecture — spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)
2. [Changements clés — spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)
3. [Transport Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)
4. [Outils](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)
5. [Autorisation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization.md)
6. [Extension Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization.md)
7. [Extension Tasks](https://modelcontextprotocol.io/extensions/tasks/overview.md)
8. [Vue d'ensemble des extensions](https://modelcontextprotocol.io/extensions/overview.md)
9. [Gouvernance](https://modelcontextprotocol.io/community/governance.md)
10. [Niveaux de SDK](https://modelcontextprotocol.io/community/sdk-tiers.md)
11. [Le registre MCP](https://modelcontextprotocol.io/registry/about)
12. [Feuille de route, mise à jour du 22 août 2026](https://modelcontextprotocol.io/development/roadmap.md)
13. [Agentic AI Foundation — projets](https://aaif.io/projects)

Source secondaire :

14. [The New Stack — feuille de route d'entreprise des mainteneurs de MCP](https://thenewstack.io/mcp-maintainers-enterprise-roadmap/) — résumé de recherche seulement, page non lue.

Pages primaires lues le 12 novembre 2026 pour la reprise :

15. [Extension Skills](https://modelcontextprotocol.io/extensions/skills/overview.md)
16. [Abonnements — spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)

## Limites de ce chapitre

- La date de lancement de MCP par Anthropic (fin 2024) et sa description comme réponse au problème des intégrations en N × M viennent de la connaissance générale, non d'une page lue. La date du don à l'AAIF est reprise du chapitre 11.
- Les pages de la spécification sur les ressources, les prompts et l'élicitation n'ont pas été lues; ces primitives sont décrites à partir de la page d'architecture et du journal des changements.
- Les pages [1], [4], [5], [10] et [13] n'ont pas été relues pendant l'audit. Les affirmations sur les annotations, les paramètres sensibles et les collisions de noms d'outils, sur l'union des portées et sur les seuils des niveaux de SDK reposent sur une lecture condensée du 11 novembre.
- La liste des produits qui prennent en charge l'ID-JAG, relue le 12 novembre 2026, change vite et se revérifie avant tout choix.
- La mention du « délégué confus » à propos du non-relais des jetons a été retirée : selon les chapitres 24 et 31, la spécification désigne ainsi un autre cas, celui du mandataire OAuth à identifiant client statique.
- Aucune donnée d'adoption (nombre de serveurs, part des entreprises) n'est citée, faute de source primaire vérifiée.
