# Chapitre 6 — A2A : le protocole agent-agent

*Question directrice : comment déléguer une tâche à un agent qu'on ne contrôle pas ?*

> **Version 2 — 11 novembre 2026.** État de référence : spécification A2A `1.0`, dans sa version corrective `1.0.1` du 28 mai 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre, toutes primaires : [1] à [9] lues à la rédaction, [10] à [12] lues à l'audit. Les renvois « chapitre N » pointent vers les chapitres du compendium. Chapitre audité et révisé le 12 novembre 2026.

Le chapitre précédent décrivait comment un agent atteint un outil. Un outil est un objet simple : il a une signature, il reçoit des arguments, il rend un résultat. L'agent qui l'appelle sait ce qu'il va obtenir.

Déléguer à un autre agent est une affaire différente. L'autre agent raisonne, planifie, utilise ses propres outils, peut poser des questions, peut refuser, peut prendre des heures. Il appartient souvent à une autre équipe, à un autre éditeur ou à une autre organisation, qui n'a aucune intention d'exposer son fonctionnement interne. On ne lui passe pas des arguments : on lui confie un objectif.

Le protocole Agent2Agent (A2A) standardise cette délégation. Sa thèse centrale tient en un mot, l'**opacité** : pour le client, l'agent distant est une boîte noire dont les rouages, la mémoire et les outils restent cachés [3]. Tout le protocole découle de ce choix. Puisqu'on ne voit pas l'intérieur, il faut un document qui décrit l'agent de l'extérieur, un objet qui suit le travail confié, et des moyens d'en recevoir des nouvelles.

---

## 6.1 Origine et gouvernance

A2A a été lancé par Google en avril 2025, avec l'appui d'une cinquantaine d'organisations [8]. Son parcours institutionnel compte cinq jalons.

| Date | Étape | Preuve |
|---|---|---|
| Avril 2025 | Lancement par Google | [8] |
| 23 juin 2025 | Don à la Linux Foundation | [11] |
| 29 août 2025 | Fusion annoncée avec ACP, le protocole d'IBM | [10] |
| 12 mars 2026 | Version 1.0, première spécification stable | [8][12] |
| 27 août 2026 | Entrée à l'Agentic AI Foundation, au stade « Growth » | [7] |

La dernière étape place A2A dans la même fondation que MCP. Le billet du projet, daté du 27 août 2026, présente A2A comme la pièce qui standardise la manière dont des agents autonomes se trouvent, se délèguent des tâches et collaborent entre cadriciels et fournisseurs [7]. L'Agentic AI Foundation recense aujourd'hui les deux protocoles parmi ses dix projets [9].

Ce regroupement compte pour un acheteur. Deux protocoles complémentaires gouvernés séparément peuvent diverger; sous un même toit, la coordination devient possible, sans être garantie. La feuille de route publiée au premier anniversaire du projet mentionne d'ailleurs une spécification d'interopérabilité et une consolidation des registres [8].

En août 2025, le billet annonçant la fusion d'ACP situait au comité de pilotage technique des représentants d'AWS, de Cisco, de Google, d'IBM, de Microsoft, de Salesforce, de SAP et de ServiceNow, IBM y entrant à cette occasion [10]. Le communiqué d'avril 2026 nomme ces huit mêmes entreprises comme soutiens du protocole, sans décrire le comité [8].

---

## 6.2 Le modèle

### Trois acteurs

A2A distingue l'**utilisateur**, personne ou service qui a un objectif; le **client A2A**, application ou agent qui agit pour lui et engage la communication; et le **serveur A2A**, ou agent distant, qui expose un point d'accès, traite les tâches et rend des résultats [3].

Un agent peut tenir les deux rôles. Il est serveur pour celui qui lui délègue une tâche, et client quand il en délègue une partie à un troisième. C'est ainsi que se forment les chaînes de délégation, dont les conséquences pour l'autorisation sont traitées au chapitre 30.

### L'Agent Card : décrire sans dévoiler

L'Agent Card est un document JSON qui présente un agent à ses clients potentiels. Tout serveur A2A doit en rendre une disponible [1].

| Champ | Rôle |
|---|---|
| `name`, `description`, `version` | Identité de l'agent |
| `supportedInterfaces` | Points d'accès : URL, protocole de liaison, version du protocole, locataire |
| `capabilities` | Flux, notifications poussées, extensions, carte étendue |
| `skills` | Compétences offertes : identifiant, nom, description, étiquettes, exemples |
| `defaultInputModes`, `defaultOutputModes` | Types de contenu acceptés et produits |
| `securitySchemes`, `securityRequirements` | Mécanismes d'authentification exigés |
| `provider` | Organisation responsable |
| `signatures` | Signatures cryptographiques de la carte |

La carte décrit **ce que l'agent sait faire**, pas comment il le fait. Une compétence (`skill`) est une description en langage naturel, avec étiquettes et exemples, non une signature de fonction typée. Cette différence avec un outil MCP est voulue : on s'adresse à un agent par un message, pas par un appel typé.

Deux mécanismes complètent la carte publique.

La **carte étendue** permet à un agent de ne publier qu'une description sommaire, et de réserver une version plus détaillée aux clients authentifiés. L'opération qui la renvoie doit exiger une authentification, et son contenu peut varier selon l'identité de l'appelant [1].

La **signature** de la carte, introduite en version 1.0, repose sur JWS et sur une mise en forme canonique du JSON. Un client devrait vérifier au moins une signature avant de se fier à une carte; une clé expirée ou révoquée ne doit pas servir à la vérification [1]. La signature répond à une question simple : cette carte vient-elle bien de l'organisation qu'elle nomme ? Elle ne dit rien de la qualité ni de l'honnêteté de l'agent.

### La tâche : l'unité de travail

La tâche (`Task`) est l'objet central du protocole. C'est une unité de travail à état, dotée d'un identifiant unique généré par le serveur et d'un cycle de vie défini [1][3]. La version 1.0 préfixe ses états par `TASK_STATE_` (`TASK_STATE_COMPLETED`) [2]; le tableau les abrège.

| État | Nature | Signification |
|---|---|---|
| `SUBMITTED` | En cours | Reçue, pas encore commencée |
| `WORKING` | En cours | En traitement |
| `INPUT_REQUIRED` | Interrompu | L'agent attend une information du client |
| `AUTH_REQUIRED` | Interrompu | L'agent attend une autorisation |
| `COMPLETED` | Terminal | Terminée avec succès |
| `FAILED` | Terminal | Échec |
| `CANCELED` | Terminal | Annulée |
| `REJECTED` | Terminal | Refusée par l'agent |

Deux états distinguent A2A d'un simple suivi de tâche asynchrone.

`REJECTED` reconnaît qu'un agent autonome peut **refuser** un travail. Un outil échoue ou réussit; un agent peut décliner, parce que la demande sort de son mandat ou contrevient à sa politique.

`AUTH_REQUIRED` reconnaît qu'un agent peut découvrir en cours de route qu'il lui faut une autorisation qu'il n'a pas : un jeton pour un système tiers, ou l'approbation d'une personne. La section 6.6 y revient.

Une tâche dans un état terminal n'accepte plus de message. Les tâches liées se regroupent par un identifiant de contexte (`contextId`), qui porte le fil d'une collaboration sur plusieurs échanges [3]. Le serveur peut le générer ou accepter celui que fournit le client [1].

### Messages, parties et artefacts

Un **message** est un tour de communication. Il a un rôle, utilisateur ou agent, et contient une ou plusieurs **parties** (`Part`) : du texte, des octets bruts, une URL ou des données structurées [1].

Un **artefact** est un livrable produit par la tâche : un document, une image, un jeu de données. La spécification pose ici une règle qui a des conséquences de conception : les messages ne doivent pas être tenus pour un mécanisme de livraison fiable de l'information critique; les artefacts sont le moyen à privilégier pour rendre des résultats [1]. Les messages servent à converser, les artefacts à livrer.

---

## 6.3 Les modes d'interaction

A2A définit onze opérations [1]. Elles forment quatre groupes : envoyer un message, avec ou sans flux; consulter, lister, annuler une tâche ou s'y abonner; gérer les configurations de notification poussée; obtenir la carte étendue.

Trois modes d'interaction en découlent [3].

**Requête-réponse.** Le client envoie un message et attend. Par défaut, l'opération est bloquante : elle rend la main quand la tâche atteint un état terminal ou interrompu. Un paramètre, `returnImmediately`, permet au client de reprendre la main tout de suite et d'interroger la tâche plus tard. Le serveur peut aussi répondre par un simple message, sans créer de tâche, quand la demande ne le justifie pas.

**Flux.** Le client garde une connexion ouverte et reçoit des mises à jour en continu : changements d'état, fragments d'artefacts. Les événements doivent être livrés dans l'ordre où ils ont été produits. Plusieurs flux peuvent suivre la même tâche en parallèle, et un client peut se réabonner à une tâche en cours [1].

**Notifications poussées.** Pour les tâches longues ou les clients déconnectés, le client enregistre un webhook; l'agent y envoie une requête POST à chaque mise à jour significative. L'agent doit tenter la livraison au moins une fois; les nouvelles tentatives sont permises à la section 4.3.3, mais recommandées à la 13.2. Le client doit accuser réception par un statut 2xx et devrait traiter les notifications de manière idempotente, des doublons étant possibles [1].

Les notifications poussées ouvrent une surface d'attaque particulière : un client malveillant peut demander à un agent d'appeler une adresse interne. La spécification y répond. L'agent doit joindre à ses appels les éléments d'authentification configurés et devrait valider les adresses de rappel, en rejetant les plages privées, de bouclage et locales au lien; le client doit vérifier que la notification porte sur une tâche attendue et devrait en vérifier la source [1].

L'annulation, comme dans MCP (chapitre 5), est une demande dont le succès n'est pas garanti.

---

## 6.4 Ce que la version 1.0 a stabilisé

La version 1.0, publiée le 12 mars 2026, est la première spécification stable du protocole [8][12]. Un correctif, 1.0.1, a suivi le 28 mai 2026 : préférence pour le type de média `application/a2a+json` dans la liaison HTTP, erreurs de transcodage, valeurs d'état corrigées [12]. La version 1.0 rompt avec la version 0.3 sur de nombreux points, ce qui en fait à la fois un jalon et un chantier de migration.

### Une architecture en trois couches

La spécification se structure en trois couches [1] :

1. un **modèle de données canonique**, indépendant de tout protocole, exprimé en Protocol Buffers;
2. des **opérations abstraites**, indépendantes de la liaison;
3. des **liaisons de protocole** : JSON-RPC, gRPC et HTTP+JSON.

Le fichier de définition Protocol Buffers est la source normative; les SDK et les autres représentations en sont dérivés. Les trois liaisons doivent offrir un comportement équivalent, et un agent déclare dans sa carte celles qu'il prend en charge [1][2]. Une liaison sur mesure reste possible, à condition de mettre en œuvre toutes les opérations et de documenter ses correspondances.

Une entreprise peut ainsi exposer le même agent en gRPC pour ses échanges internes à haut débit, et en HTTP+JSON pour ses partenaires, sans maintenir deux modèles.

### Les ajouts

| Ajout | Ce qu'il apporte |
|---|---|
| Cartes signées | Vérification cryptographique de l'origine d'une Agent Card |
| Multilocation | Un champ `tenant` permet de servir plusieurs agents depuis un même point d'accès |
| Versionnement | Chaque interface déclare sa version; le client envoie un en-tête `A2A-Version` |
| Liste des tâches | Nouvelle opération, avec filtres et pagination par curseur |
| Extensions versionnées | Identifiées par URI, déclarées obligatoires ou non, demandées par l'en-tête `A2A-Extensions` |
| Sécurité | TLS mutuel parmi les mécanismes déclarables; flux OAuth implicite et par mot de passe abandonnés au profit du code d'autorisation avec PKCE; flux par code d'appareil ajouté |

Le versionnement suit une règle simple : seuls comptent les numéros majeur et mineur. Un agent peut prendre en charge plusieurs versions en exposant plusieurs interfaces. Une version non prise en charge provoque une erreur explicite, et un en-tête vide est interprété comme la version 0.3 [1].

### Les ruptures

La liste des changements incompatibles est longue [2] : opérations renommées, types de parties fusionnés en un seul, énumérations réécrites, pagination par curseur, chemins HTTP modifiés, format des erreurs remplacé. Un agent écrit pour la version 0.3 ne parle pas la version 1.0 sans adaptation.

Le projet recommande une migration en trois temps : une couche de compatibilité qui lit les deux formats, une période de double prise en charge, puis l'abandon de l'ancien format [2]. Il suggère de traiter d'abord l'analyse des parties, des événements de flux et des cartes, puis la pagination et les énumérations dans le mois, et enfin la vérification des signatures et les nouvelles erreurs dans les trois mois.

L'enseignement dépasse A2A : un protocole adopté avant sa version stable fait payer cette avance. Les organisations qui ont déployé A2A en 2025 ont une dette de migration que n'ont pas celles qui arrivent en 2026.

---

## 6.5 L'absorption d'ACP

En mars 2025, IBM Research avait lancé son propre protocole de communication entre agents, l'Agent Communication Protocol (ACP), pour animer sa plateforme BeeAI, donnée à la Linux Foundation le même mois [10]. Pendant quelques mois, deux standards ouverts se sont disputé le même terrain.

Le 29 août 2025, LF AI & Data a annoncé la fusion d'ACP dans A2A, sous l'égide de la Linux Foundation : l'équipe d'ACP cessait le développement actif de son protocole et apportait sa technologie à A2A. Un adaptateur rend conformes à A2A les agents construits avec le cadriciel BeeAI, et un guide de migration accompagne les utilisateurs d'ACP [10]. D'après des résumés de recherche, le dépôt d'ACP a depuis été archivé.

Cet épisode est le signal le plus net de convergence dans la couche agent-agent. Il n'a pas tout unifié : ANP poursuit une approche décentralisée, et AGNTCY bâtit une infrastructure autour de MCP et d'A2A plutôt qu'un concurrent (chapitre 7); la Chine a publié une série nationale non obligatoire, GB/Z 185-2026, dont la description d'agent serait proche de l'Agent Card selon une analyse (chapitre 11). Mais dans l'écosystème ouvert d'origine occidentale, la question « quel protocole entre agents ? » a aujourd'hui une réponse par défaut.

---

## 6.6 Composer MCP et A2A

### Vertical et horizontal

La documentation d'A2A résume la relation entre les deux protocoles par une image : MCP est **vertical**, il approfondit un agent en lui donnant des outils et des données; A2A est **horizontal**, il relie des agents par-delà les frontières d'équipe, de service ou d'organisation [5]. La formule proposée est qu'avec A2A des agents s'associent sur des tâches, alors qu'avec MCP un agent utilise des capacités.

L'exemple canonique est celui d'un atelier de réparation automobile. Le client décrit un bruit suspect à un agent « gérant d'atelier », par A2A, et le dialogue de diagnostic se poursuit sur plusieurs tours. Un agent « mécanicien » utilise MCP pour ses outils : lecteur de diagnostic, base de manuels, pont élévateur. Pour commander une pièce, le mécanicien s'adresse par A2A à l'agent d'un fournisseur.

| Critère | MCP | A2A |
|---|---|---|
| Cible | Un outil, une ressource | Un agent autonome |
| Ce qu'on transmet | Des arguments typés | Un objectif, par message |
| Description | Schéma d'entrée et de sortie | Compétences en langage naturel |
| Visibilité | L'outil est décrit précisément | L'agent est opaque |
| Durée typique | Courte; tâches longues par extension | Longue; la tâche est au cœur |
| Peut refuser ? | Non, il échoue ou réussit | Oui, état `REJECTED` |
| Frontière habituelle | Dans le périmètre d'un agent | Entre équipes ou organisations |

### La frontière est moins nette qu'il n'y paraît

Trois observations nuancent cette répartition; hormis ce qui est cité, elles relèvent de l'analyse de ce chapitre.

**Un agent peut se présenter comme un outil.** La documentation d'A2A le reconnaît : un agent distant peut exposer certaines compétences bien définies sous une forme compatible avec MCP, ce qui fonctionne surtout quand ces compétences s'appellent de manière ponctuelle et sans état [5]. Elle ajoute que la force d'A2A est ailleurs, dans la collaboration souple et à état. En pratique, le choix entre « exposer comme outil » et « exposer comme agent » est une décision d'architecture, pas une évidence.

**Les deux protocoles se rapprochent.** Depuis sa révision de juillet 2026, MCP encadre des extensions officielles, dont deux en bêta : Tasks, dont les états recoupent ceux d'A2A, et Server Cards, pour la découverte (chapitres 5 et 8). A2A, de son côté, sait livrer des résultats structurés. Les deux s'appuient sur HTTP pour l'accès distant et déclarent leurs capacités.

**Le critère utile est l'opacité, pas la technique.** La bonne question n'est pas « est-ce un agent ou un outil ? », mais « qui contrôle ce qui se passe de l'autre côté ? ». Si l'appelant maîtrise ou connaît précisément le comportement attendu, un outil convient. S'il délègue un objectif à un système qui décide lui-même de la manière de l'atteindre, c'est une délégation entre agents, avec ce qu'elle implique de négociation, de refus possible et de vérification du résultat.

### L'autorisation en cours de tâche

Dans MCP, le serveur réclame des portées supplémentaires au moment de l'appel (chapitre 5). A2A prévoit qu'une autorisation manque au milieu d'un travail long : l'agent doit alors faire passer la tâche à l'état `AUTH_REQUIRED` et expliquer ce qu'il lui faut [1]. Le client peut alors négocier, refuser, s'adresser à un tiers ou satisfaire la demande par un autre canal. Si le client est lui-même un agent, il peut à son tour faire passer sa propre tâche dans le même état : la demande d'autorisation **remonte la chaîne de délégation** jusqu'à quelqu'un qui peut y répondre.

Trois règles encadrent ce mécanisme. Les justificatifs doivent être obtenus hors du protocole, sauf mécanisme négocié par ailleurs, et devraient transiter par un canal sûr. Un agent ne doit pas traiter le passage à l'état `AUTH_REQUIRED` comme une autorisation en soi : la portée de ce qui est accordé doit être définie par la mise en œuvre, par l'émetteur du justificatif ou par une extension. Enfin, un justificatif obtenu dans cet état ne vaut pas d'office pour les messages suivants de la tâche [1]. Le protocole fournit donc le signal, pas la sémantique. Ce que vaut une approbation donnée trois maillons plus haut reste à définir par l'entreprise (chapitre 30).

---

## 6.7 Adoption et limites

### Ce qu'on sait de l'adoption

Le bilan publié par la Linux Foundation en avril 2026 donne quelques repères [8] : plus de 150 organisations soutiennent le protocole, contre une cinquantaine un an plus tôt; le dépôt principal a dépassé 22 000 étoiles; des SDK existent en cinq langages; Microsoft a intégré A2A à Azure AI Foundry et à Copilot Studio, et AWS à Amazon Bedrock AgentCore Runtime.

Le même communiqué affirme l'existence de déploiements en production dans la chaîne logistique, les services financiers, l'assurance et les opérations informatiques. Il **ne nomme aucune organisation**. Le soutien déclaré d'un éditeur et l'usage réel par ses clients sont deux choses différentes, et les sources disponibles ne permettent pas de mesurer le second.

### Ce qu'A2A ne règle pas

| Question | Ce que dit la spécification | Ce qui revient à l'entreprise |
|---|---|---|
| Comment trouver un agent ? | Un emplacement `/.well-known/agent-card.json`; aucune API de registre [4] | Un registre d'agents et sa gouvernance (chapitre 8) |
| Comment le client obtient-il ses identifiants ? | Hors protocole [6] | Le choix du mécanisme et la distribution des secrets (chapitre 29) |
| Qui a le droit de faire quoi ? | Le serveur doit autoriser chaque opération; la logique lui appartient [1][6] | La politique, par compétence et par appelant |
| Que vaut une approbation en cours de tâche ? | Le signal existe; sa portée n'est pas définie [1] | La sémantique de la délégation (chapitre 30) |
| Le résultat est-il correct ? | Rien; l'agent est opaque | La vérification des livrables (chapitres 21 et 32) |
| L'agent est-il digne de confiance ? | La signature atteste l'origine de la carte [1] | L'évaluation et l'approbation des agents tiers |
| Qui répond d'un dommage ? | Rien | Le contrat entre organisations (chapitre 36) |

**La découverte reste artisanale.** La spécification standardise le format de la carte et son emplacement, pas la manière d'interroger un catalogue. La documentation décrit trois stratégies : l'emplacement bien connu, les registres organisés et la configuration directe. Elle précise qu'aucune API standard de registre n'est prescrite et que la communauté explore la question [4]. Chaque plateforme propose donc son registre, ce qui recrée de la fragmentation à l'étage supérieur.

**L'opacité a un prix.** Elle protège la propriété intellectuelle et simplifie l'intégration, mais elle prive le client de tout moyen de constater comment un résultat a été obtenu. Dans un système multi-agents, où les échecs naissent de la spécification, du désalignement entre agents et de la vérification (chapitre 21), déléguer à une boîte noire exige de contrôler ce qu'elle rend. Quand l'agent distant sert un intérêt contraire, comme dans une négociation entre entreprises, A2A transporte l'échange mais ne protège ni les secrets ni le règlement : ces protections relèvent de composants déterministes ou contractuels (chapitre 45).

**La sécurité est renvoyée aux standards du web.** A2A ne définit pas d'identité propre : l'authentification se fait à la couche HTTP, par les mécanismes déclarés dans la carte, et l'identité ne voyage pas dans les messages [6]. C'est un choix sain, qui permet de réutiliser l'infrastructure existante. Il laisse cependant entière la question de l'identité d'un agent qui agit pour le compte d'un utilisateur d'une autre organisation (chapitres 29 et 45).

La spécification impose tout de même quelques garanties de fond. Le serveur doit autoriser chaque opération, et la vérification doit précéder toute requête en base, afin de ne pas révéler l'existence d'une ressource. Une ressource introuvable et une ressource interdite ne devraient pas pouvoir être distinguées par l'appelant. La liste des tâches ne renvoie que celles que le client a le droit de voir [1].

Enfin, la documentation recommande fortement de placer les serveurs A2A exposés à l'extérieur derrière une solution de gestion d'API, et de participer au traçage distribué par propagation du contexte de trace [6]. Ce sont des recommandations d'exploitation, non des exigences du protocole. Des passerelles agentiques, comme agentgateway, projet de l'Agentic AI Foundation, relaient A2A sur le même plan de données que MCP et l'inférence (chapitres 24 et 44).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Exposer une capacité comme outil ou comme agent | Outil (MCP) si le comportement est ponctuel, typé et maîtrisé par l'appelant | Agent (A2A) si la capacité raisonne, dialogue, dure ou appartient à une autre équipe |
| Version cible | 1.0, avec son correctif 1.0.1, pour tout nouvel agent | Partenaires encore en 0.3 : exposer deux interfaces pendant la transition |
| Liaison | HTTP+JSON ou JSON-RPC pour l'externe | gRPC pour les échanges internes à haut débit |
| Carte publique | Description minimale, sans secret ni URL interne | Carte étendue, après authentification, pour le détail |
| Signature des cartes | Signer ses cartes; vérifier celles des tiers | Aucun écart justifié en production entre organisations |
| Découverte | Registre interne organisé | Emplacement bien connu pour un agent public; configuration directe pour un couplage fixe |
| Suivi d'une tâche longue | Notifications poussées, avec validation de leur authenticité | Interrogation périodique si le client ne peut pas recevoir d'appels entrants |
| Livraison des résultats | Artefacts | Message seul pour un échange purement conversationnel |
| Autorisation en cours de tâche | Justificatifs obtenus hors protocole; portée et durée de validité définies par politique | — |
| Exposition externe | Derrière une passerelle de gestion d'API | Agent strictement interne |
| Vérification des livrables | Contrôle systématique de ce que rend un agent tiers | Agent interne dont le comportement est évalué en continu |

---

## Points à retenir

- A2A standardise la délégation d'un objectif à un agent opaque : on ne voit ni ses outils, ni sa mémoire, ni son raisonnement.
- Trois objets portent le protocole : l'Agent Card, qui décrit l'agent de l'extérieur; la tâche, qui suit le travail; l'artefact, qui livre le résultat.
- Un agent peut refuser une tâche ou réclamer une autorisation en cours de route. Ces deux états n'ont pas d'équivalent pour un outil.
- La version 1.0 apporte les cartes signées, la multilocation, trois liaisons équivalentes et un versionnement explicite, au prix d'une rupture avec la version 0.3.
- La fusion d'ACP et l'entrée à l'Agentic AI Foundation font d'A2A le protocole par défaut entre agents dans l'écosystème ouvert d'origine occidentale.
- MCP et A2A se complètent, mais leur frontière se brouille. Le critère de choix utile est le degré de contrôle de l'appelant sur ce qui s'exécute de l'autre côté.
- Le protocole ne standardise ni l'interrogation des registres, ni l'obtention des identifiants, ni la portée d'une approbation donnée en cours de tâche.
- La signature d'une carte atteste son origine, pas la fiabilité de l'agent. La vérification des résultats reste à la charge du client.
- L'adoption par les éditeurs est documentée; l'usage en production est affirmé sans qu'aucune organisation soit nommée.

---

## Sources

Pages primaires lues le 11 novembre 2026, [1], [2] et [8] relues à l'audit :

1. [Spécification A2A 1.0](https://a2a-protocol.org/latest/specification/)
2. [Nouveautés de la version 1.0](https://a2a-protocol.org/latest/whats-new-v1/)
3. [Concepts clés](https://a2a-protocol.org/latest/topics/key-concepts/)
4. [Découverte des agents](https://a2a-protocol.org/latest/topics/agent-discovery/)
5. [A2A et MCP](https://a2a-protocol.org/latest/topics/a2a-and-mcp/)
6. [Fonctions d'entreprise](https://a2a-protocol.org/latest/topics/enterprise-ready/)
7. [Annonces du projet A2A](https://a2a-protocol.org/latest/blog/category/announcements/)
8. [Linux Foundation — bilan de la première année d'A2A, 9 avril 2026](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)
9. [Agentic AI Foundation — projets](https://aaif.io/projects)

Pages primaires lues lors de l'audit, le 12 novembre 2026 :

10. [LF AI & Data — ACP Joins Forces with A2A, 29 août 2025](https://lfaidata.foundation/?p=7689)
11. [Linux Foundation — lancement du projet Agent2Agent, 23 juin 2025](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)
12. [Dépôt a2aproject/A2A — versions publiées](https://github.com/a2aproject/A2A/releases)

## Limites de ce chapitre

- La section de la spécification consacrée à la liaison JSON-RPC n'a pas été lue; les liaisons gRPC et HTTP+JSON l'ont été.
- Levé à l'audit par les pages [10] à [12] : dates du don à la Linux Foundation, de la fusion d'ACP, des versions 1.0 et 1.0.1, et composition du comité de pilotage en août 2025. Restent invérifiées la date d'approbation par l'Agentic AI Foundation, seul le billet étant daté [7], et la composition actuelle du comité.
- La page de la spécification affiche encore 1.0.0 comme dernière version, alors que le dépôt marque 1.0.1 comme la plus récente [12]. Les exigences citées ont été lues sur la page de la spécification.
- Pour les flux OAuth implicite et par mot de passe, la page des nouveautés les dit retirés [2], la spécification les dit dépréciés [1].
- La page « Concepts clés » présente encore JSON-RPC comme format unique des échanges, ce qui ne correspond plus aux trois liaisons de la version 1.0. La spécification fait foi.
- L'archivage du dépôt d'ACP ne figure pas dans le billet d'annonce lu [10]; il vient de résumés de recherche.
- La comparaison avec MCP de la section 6.6 est une analyse propre à ce chapitre.
- Aucun déploiement en production n'est cité, faute de source qui en nomme un.
- Les pages ont été lues par un outil qui les condense; la spécification l'a été par segments.
