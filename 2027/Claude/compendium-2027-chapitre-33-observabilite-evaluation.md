# Chapitre 33 — Observabilité et évaluation

*Question directrice : comment savoir ce qu'un système d'agents a fait, et s'il l'a bien fait ?*

> **Version 2 — 11 novembre 2026.** État de référence : conventions sémantiques GenAI d'OpenTelemetry telles qu'elles figurent sur la branche `main` du dépôt `open-telemetry/semantic-conventions-genai` le 11 novembre 2026 (aucune version publiée), et quatre articles parus entre juin 2024 et juin 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre; toutes sont des pages primaires lues pour ce chapitre, sauf [15], marquée secondaire. Chapitre audité et révisé le 12 novembre 2026.

Un service classique se surveille par trois signaux : disponibilité, latence, taux d'erreur. Un agent peut les satisfaire tous les trois et accomplir la mauvaise tâche : répondre vite, sans erreur technique, à côté de la demande. La question directrice se dédouble donc. Savoir ce que le système a fait relève de l'observabilité; savoir s'il l'a bien fait relève de l'évaluation.

Les deux travaillent le même matériau : la trajectoire, c'est-à-dire la suite ordonnée des décisions, des appels de modèle et des appels d'outils qui mène d'une demande à un résultat. L'observabilité la consigne, l'évaluation la juge.

Ni l'une ni l'autre n'est stabilisée. Les conventions OpenTelemetry qui décrivent les traces d'agents sont toutes au statut « Development », et l'évaluation en production repose d'abord sur des humains. D'où la thèse de ce chapitre : l'entreprise ne peut déléguer ni son schéma de télémétrie à un standard encore mouvant, ni son jugement de qualité à un banc d'essai public.

---

## 33.1 Que tracer

### La trajectoire, pas la requête

Une trace distribuée est un arbre de spans, chacun décrivant une opération bornée dans le temps. Les conventions GenAI d'OpenTelemetry donnent à cet arbre un vocabulaire propre aux agents [3][4][5].

| Opération | Ce que le span décrit | Question à laquelle il répond |
|---|---|---|
| `invoke_workflow` | Un flux dont l'application fixe le déroulement | Quel processus s'est exécuté ? |
| `invoke_agent` | Un agent dont le modèle pilote le déroulement par ses appels d'outils | Quel agent a décidé ? |
| `plan` | Une étape de planification ou de décomposition | Qu'avait-il l'intention de faire ? |
| Inférence | Un appel au modèle de langage | Avec quel modèle, à quel coût en jetons ? |
| `execute_tool` | Un appel d'outil | Qu'a-t-il fait, et avec quels arguments ? |
| Récupération, mémoire | Une recherche de contexte, une lecture ou écriture en mémoire | Sur quoi s'est-il appuyé ? |

La convention distingue `invoke_workflow` et `invoke_agent` par l'auteur du flux de contrôle : l'application dans le premier cas, le modèle dans le second [4]. C'est la frontière entre région déterministe et région agentique du chapitre 17, inscrite dans la trace.

### Quatre familles d'information

Les attributs recommandés se rangent en quatre familles [4][9].

**L'identité.** `gen_ai.agent.id`, `gen_ai.agent.name` et `gen_ai.agent.version` désignent l'agent. L'identifiant devrait être celui, stable, que la plateforme attribue, et non un identifiant d'instance en mémoire. Ces attributs font la jonction avec l'identité des agents (chapitre 29) et leur inventaire (chapitre 39).

**La décision.** Le modèle demandé, la raison de fin de génération, l'outil appelé. Les arguments et le résultat d'un appel d'outil ne sont pas captés par défaut (section 33.4).

**Le coût.** `gen_ai.usage.input_tokens` et `gen_ai.usage.output_tokens`. Le total d'entrée comprend les jetons servis depuis le cache, le total de sortie les jetons de raisonnement, et si un fournisseur rapporte deux décomptes, c'est le décompte facturé qui se consigne [4]. La trace devient la source de l'imputation des coûts (chapitre 40).

**L'issue.** `error.type` en cas d'échec, et le résultat d'une évaluation, qui dispose de son propre événement (section 33.6).

### Trace et piste d'audit

Une trace sert au diagnostic et peut être échantillonnée. Une piste d'audit sert à rendre compte et doit être complète. Nubank, qui exploite des agents de service à la clientèle à l'échelle de cent millions d'utilisateurs, décrit la seconde : chaque appel d'outil est journalisé avec ses entrées, ses sorties, sa latence et ses erreurs, à des fins de conformité, de débogage et d'analyse après coup [12].

La règle pratique est de produire les deux à partir de la même instrumentation, puis de les séparer : la piste d'audit n'est jamais échantillonnée et suit les règles de conservation du domaine. Le chapitre 24 traite de l'enregistrement d'audit exigé d'une passerelle.

---

## 33.2 Conventions OpenTelemetry : portée et instabilité

### Ce que les conventions couvrent

L'index du dépôt recense trois groupes de documents [3]. Les signaux de base : inférence, plongements (*embeddings*), exécution d'outil, récupération, invocation d'agent distant, spans d'agent, événements, exceptions, métriques, génération en temps réel. Les conventions propres à une technologie : Anthropic, Azure AI Inference, AWS Bedrock, OpenAI. Et deux protocoles : MCP et A2A (chapitres 5 et 6).

### Rien n'est stable

Chaque document lu pour ce chapitre porte le statut « Development » : l'index, les spans d'agent, les spans GenAI, les événements, l'invocation d'agent distant, MCP et A2A [3][4][5][6][7][8][9]. Ce statut autorise des changements incompatibles.

L'instabilité est aussi organisationnelle. La page des conventions GenAI sur le site d'OpenTelemetry ne contient plus qu'un avis : le contenu a été déplacé vers un dépôt dédié [1]. Ce dépôt n'a publié aucune version. Son journal des changements se réduit à une section « Unreleased » vide, et son fichier de présentation indique « TODO » à la place de l'adresse du schéma [2][10]. Il n'existe donc aucun numéro de version auquel épingler une mise en œuvre, hors un identifiant de commit.

Une analyse indépendante, mise à jour le 3 novembre 2026, précise la chronologie [15]. Selon elle, la version 1.42.0 des conventions générales, du 12 juin 2026, a déprécié et déplacé tout le contenu `gen_ai.*`; c'est la dernière coupe versionnée. Elle rapporte trois ruptures antérieures : le renommage des compteurs de jetons, le remplacement de `gen_ai.system` par `gen_ai.provider.name`, puis la scission du span `invoke_agent` en une variante cliente et une variante interne. Elle signale le retrait de la métrique `gen_ai.client.token.usage` sur `main`, le 22 septembre 2026, et relève que les cadriciels n'émettent pas tous la même génération d'attributs. Son constat de statut concorde avec les pages primaires.

### Un décalage avec les protocoles

La convention MCP illustre un second risque : le retard sur le protocole décrit. La page lue cite en exemple la version `2025-06-18` du protocole et renvoie à la spécification `2025-11-25`. Elle recommande l'attribut `mcp.session.id` et définit deux métriques de durée de session [7]. Or la révision `2026-07-28` de MCP a supprimé la session (chapitre 5). La page, relue en entier, ne mentionne ni cette révision ni le mode sans état. Un serveur conforme à la révision de juillet n'a pas de session à rapporter.

### Ce qu'il faut en conclure

OpenTelemetry reste le format d'échange à retenir : la spécification MCP y renvoie elle-même la journalisation qu'elle abandonne (chapitre 5). Mais un produit « compatible OpenTelemetry » ne garantit pas un schéma : c'est l'opinion de l'analyse citée, que les faits lus appuient [15].

1. **Tenir un schéma interne.** Tableaux de bord, alertes et évaluations lisent un modèle de données propre à l'entreprise, pas les attributs `gen_ai.*` bruts. C'est aussi la condition d'un entrepôt de traces commun à plusieurs plateformes (chapitre 27).
2. **Normaliser au collecteur.** La traduction entre générations d'attributs se fait à un seul endroit, à l'entrée de l'entrepôt.
3. **Épingler et vérifier.** Chaque instrumentation est fixée à une version, et un span réellement exporté est inspecté à chaque mise à jour.
4. **Garder ses attributs hors de l'espace `gen_ai.*`**, pour éviter une collision avec une future convention.

---

## 33.3 Corrélation entre agents

Dans un système multi-agents, la question « qui a décidé quoi » traverse des processus et des protocoles. Trois identifiants se partagent le travail, et aucun ne suffit seul.

| Identifiant | Portée | Limite |
|---|---|---|
| Contexte de trace (`traceparent`) | Une chaîne d'appels synchrones | Se rompt quand le travail reprend dans un autre processus ou plus tard |
| `gen_ai.conversation.id` | Une conversation ou un contexte | N'existe que si la plateforme en fournit un |
| Identifiant de tâche (`a2a.task.id`) | Une tâche de longue durée | Propre à un protocole |

### Vers les outils : MCP

La convention MCP fixe le mécanisme. Le contexte de trace est injecté dans l'objet `params._meta` de la requête, sous les clés `traceparent`, `tracestate` et `baggage`; le récepteur l'extrait et en fait le parent distant de son span [7]. Le span client MCP est toujours le parent du span serveur. Le contexte de la couche de transport se consigne par des liens de span, parce qu'une requête MCP peut s'étaler sur plusieurs requêtes HTTP et qu'une requête HTTP peut porter plusieurs messages MCP.

Une règle évite les doublons : si l'instrumentation GenAI trace déjà l'exécution de l'outil, l'instrumentation MCP devrait enrichir ce span plutôt qu'en créer un second [7].

### Vers les autres agents : A2A

L'instrumentation A2A ne rapporte que les requêtes du protocole, pas les opérations d'agent de plus haut niveau. Son span peut être l'enfant d'un span d'invocation d'agent distant [8][9].

Trois règles comptent pour la corrélation [8]. L'identifiant de contexte d'A2A se consigne dans `gen_ai.conversation.id`. La tâche se suit par `a2a.task.id` et `a2a.task.state`. Et l'interrogation périodique d'une tâche produit des spans frères sous le span parent de l'agent, non des enfants de l'envoi initial; menée dans un autre processus ou sans le contexte parent, elle produit des traces séparées, que seul l'identifiant de tâche relie.

Deux lacunes sont à noter. La page lue ne décrit pas comment le contexte de trace passe du client au serveur A2A, et ne donne aucune consigne pour les notifications poussées [8]. La convention d'invocation d'agent distant ne dit pas comment le span client se rattache au span interne de l'agent appelé [9].

### L'identifiant de conversation n'est pas un bouche-trou

`gen_ai.conversation.id` ne se renseigne que si un identifiant réel existe. Il ne faut lui substituer ni un UUID neuf, ni l'identifiant de trace, ni une empreinte du contenu [4][9]. Au sein d'un même processus, il peut se propager aux instrumentations imbriquées [3]. Rien n'est prévu pour le maintenir cohérent d'un agent à l'autre.

### Conséquence d'architecture

Une trace unique ne survit pas à l'exécution durable. Un dossier qui attend une approbation, puis reprend sur une autre machine, produit plusieurs traces (chapitres 18 et 22). La corrélation de bout en bout exige donc un identifiant d'affaires, celui du dossier ou de la demande, porté par chaque événement (chapitre 19) et recopié sur chaque span racine.

Cet identifiant conditionne aussi l'attribution des échecs, que les méthodes automatiques réussissent mal (chapitre 21) : la trace qui relie chaque délégation à son auteur se prépare à la conception.

---

## 33.4 Données sensibles dans la télémétrie

### Le contenu est exclu par défaut

Les prompts, les réponses, les instructions système et les arguments d'outils contiennent ce que l'entreprise a de plus sensible : renseignements personnels, données de clients, secrets d'affaires. Les conventions en tirent une règle nette : une instrumentation ne devrait pas capter ce contenu par défaut [5].

La variable `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT` règle le comportement. Elle vaut `NO_CONTENT` par défaut, et une valeur invalide y ramène. Elle régit les messages, les instructions système, les arguments et résultats d'outils, les requêtes de récupération et les enregistrements de mémoire [5].

| Option | Mécanisme | Usage prévu par la convention |
|---|---|---|
| Ne rien consigner | Valeur par défaut | Production, sauf décision contraire |
| Consigner dans la trace | Attributs `gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions` | Volume maîtrisable et stockage conforme, par exemple en préproduction |
| Stocker à part et consigner une référence | Attributs suffixés `_ref`, qui portent un URI | Recommandé en production quand le volume ou la sensibilité l'exige |

### La référence externe

La troisième option est la plus utile en entreprise. Le contenu part vers un stockage distinct, doté de ses propres contrôles d'accès; la trace ne garde qu'un pointeur [5]. L'équipe d'exploitation voit la structure et les coûts sans lire les conversations.

Deux mises en garde l'accompagnent [4][9]. L'URI ne doit pas embarquer de justificatif, comme les paramètres d'une URL signée. Et il peut révéler à lui seul des métadonnées de stockage.

La convention prévoit un crochet (`hook`) qui reçoit le contenu avant son envoi et peut le modifier, quelle que soit la décision d'échantillonnage du span [5]. C'est le point d'insertion naturel du masquage.

### Les fuites latérales

Le contenu ne passe pas seulement par les attributs prévus pour lui. Les conventions signalent comme sensibles les définitions d'outils, que la variable de capture ne régit pas, et le message d'une exception [4][5]. Côté A2A, le corps des requêtes HTTP est un attribut facultatif, désactivé par défaut [8]. L'explication en texte libre d'un résultat d'évaluation peut recopier un fragment de conversation; la page des événements ne donne aucune consigne à ce sujet [6]. Les bagages (`baggage`) propagés avec le contexte de trace voyagent enfin jusque chez le tiers appelé.

L'analyse indépendante déjà citée signale que l'instrumentation Python lit encore `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT`, et non la variable de la convention [15]. Seule l'inspection de ce qui est exporté établit donc ce qui quitte le processus.

### La tension avec l'évaluation

Sans contenu, une trace dit ce que l'agent a fait, pas s'il a eu raison. Nubank décrit le compromis qu'elle applique : champs sensibles masqués dans les journaux, durées de conservation liées aux obligations légales, et accès aux conversations et aux jeux d'évaluation accordé par rôle, journalisé et limité dans le temps [12].

Le patron qui s'en dégage sépare deux zones. La zone de télémétrie reçoit la structure, les coûts et les scores. La zone de contenu reçoit les conversations, sous accès restreint et clés détenues par l'entreprise (chapitre 46); les évaluateurs, humains ou automatiques, y travaillent et n'en font sortir que des résultats. La boucle qui tire des exemples d'entraînement des traces y puise aussi, après masquage (chapitre 47). Les obligations propres au Québec et au Canada relèvent du chapitre 38.

---

## 33.5 Évaluer : humains, juges automatiques, simulation

### L'état de la pratique

L'étude *Measuring Agents in Production* (MAP) repose sur vingt études de cas et un sondage de 306 réponses valides, dont 86 portent sur des systèmes déployés [11]. À la question des méthodes d'évaluation, que 31 répondants seulement ont traitée (figure 8), 74 % s'appuient surtout sur l'évaluation humaine, 52 % emploient un modèle de langage comme juge et 42 % des vérifications à base de règles. Les trois quarts des équipes étudiées évaluent sans jeu de bancs d'essai, et toutes celles qui emploient un juge automatique le doublent d'une revue humaine.

Ces chiffres se lisent avec les réserves des auteurs : participation volontaire, équipes concentrées dans les Amériques, entretiens plutôt qu'audits.

### Trois instruments

| Instrument | Ce qu'il mesure bien | Sa limite |
|---|---|---|
| Humain expert | La justesse dans un domaine, les cas inédits | Ne suit pas le volume |
| Juge automatique | Un critère précis, à grande échelle | Ne vaut que par son étalonnage |
| Simulation | Le comportement sur plusieurs tours, la constance | Dépend du réalisme de l'utilisateur simulé |

### Le juge automatique s'étalonne

Le cas de Nubank, publié à KDD 2026, est le plus détaillé des textes lus [12]. Les critères sont binaires. Trois analystes étiquettent chaque échantillon avec une justification écrite, et la majorité l'emporte. Les auteurs estiment que quelques centaines d'étiquettes suffisent. Le prompt du juge est ensuite optimisé contre ces étiquettes.

L'optimisation améliore l'exactitude du juge sur le jeu de test pour chacun des quatre critères rapportés, par exemple de 68,88 % à 88,89 % sur l'un d'eux. Et l'accord entre deux modèles juges munis du prompt initial peut être nul : un kappa de Cohen de 0,000 entre GPT-4.1 et GPT-4.1-mini, ce dernier rangeant tous les cas dans une seule classe, porté à 0,745 après optimisation.

Un juge non étalonné mesure le modèle qui juge autant que l'agent jugé; changer de modèle juge, c'est changer d'instrument, et cela exige un nouvel étalonnage contre des étiquettes humaines. L'article affirme imposer un seuil minimal d'accord avec les humains, sans le chiffrer dans le texte lu.

### La simulation mesure la constance

Le banc d'essai τ-bench en fixe le modèle [13]. Un modèle de langage joue l'utilisateur; l'agent dispose d'outils et d'une politique à respecter. Le succès se juge en comparant l'état final de la base de données à un état cible annoté, et non le texte produit. Une métrique, pass^k, mesure la fiabilité sur plusieurs essais d'une même tâche.

Le résumé de l'article rapporte qu'un agent fondé sur gpt-4o réussissait moins de la moitié des tâches, et que pass^8 tombait sous 25 % dans le commerce de détail. Ces chiffres datent de 2024. Deux principes demeurent : juger l'état du système plutôt que le discours de l'agent, et répéter l'essai, parce qu'un succès isolé surestime la fiabilité.

Nubank rapporte que ses métriques de simulation hors ligne vont de pair avec les résultats en ligne : les variantes dont le taux d'échec hors ligne baisse le plus sont celles dont la satisfaction mesurée monte le plus [12]. L'article parle d'une forte corrélation sans en donner le coefficient, et le texte lu ne décrit pas la construction des utilisateurs simulés. L'assurance fondée sur la trajectoire entière relève du chapitre 32.

---

## 33.6 Évaluation continue à coût maîtrisé

### Une boucle, pas une étape

Chez Nubank, l'évaluation forme une boucle : évaluation hors ligne, simulation, déploiement progressif à partir de 1 % du trafic, mesures en ligne, puis retour vers les jeux d'évaluation [12]. Les mesures en ligne sont des indicateurs d'affaires : NPS transactionnel (tNPS), taux de libre-service (part des demandes résolues sans transfert à un humain), taux d'escalade, taux d'erreur. Pour la livraison de cartes, l'essai comparatif rapporte un gain de 37 points de tNPS et de 29 points de libre-service par rapport à la variante initiale, sans valeur absolue; l'agent reste environ 10 points de tNPS sous les experts humains [12] (chapitre 42).

La boucle sert aussi de filet lors d'un changement de modèle. Le passage de GPT-4.1 à GPT-5 a réduit le taux d'échec sur trois critères, l'a aggravé sur la concision des réponses, et il a fallu modifier le prompt [12]. Sans jeu d'évaluation, cette régression n'aurait été vue qu'en production.

### Les leviers de coût

Juger une trajectoire par un modèle ajoute des appels d'inférence à ceux de l'agent. Aucun des textes lus ne chiffre ce coût; ils décrivent en revanche des leviers.

| Levier | Principe | Source |
|---|---|---|
| Règles | Des vérifications déterministes, sans appel de modèle | [11] |
| Petit juge | Un modèle léger classe; le modèle fort ne sert qu'à optimiser le prompt du juge | [12] |
| Aiguillage par confiance | Les sorties à faible confiance vont aux experts; un échantillon aléatoire des autres est contrôlé | [11] |
| Filtre hors ligne | Les variantes faibles sont écartées avant l'essai en ligne, plus coûteux | [12] |
| Peu d'étiquettes | Quelques centaines d'exemples suffisent à étalonner un juge | [12] |
| Échantillonnage | L'évaluation porte sur une fraction du trafic | [4] |

Le dernier levier touche à l'instrumentation. Les conventions demandent que le nom de l'agent, l'opération et le modèle soient posés à la création du span, pour servir aux décisions d'échantillonnage [4]. On peut ainsi évaluer davantage un agent récemment modifié. L'échantillon aléatoire des sorties jugées sûres reste indispensable : lui seul révèle un juge trop confiant.

### Consigner le verdict

Les conventions définissent un événement, `gen_ai.evaluation.result` [6]. Il porte le nom du critère, un score numérique, une étiquette, une explication en texte libre et l'identifiant de la réponse évaluée. Il devrait être rattaché au span de l'opération jugée.

L'étiquette a une raison d'être : un même score peut signifier des choses opposées d'un système d'évaluation à l'autre, la valeur 1 désignant ici « pertinent » et là « non pertinent » [6].

Rattaché à la trace, le verdict se lit dans le même entrepôt que la latence et le coût, par agent, par version et par outil. C'est le fondement des objectifs de niveau de service fondés sur les résultats (chapitre 34). Cet événement est lui aussi au statut « Development ».

---

## 33.7 Bancs d'essai d'entreprise

### Pourquoi les bancs publics ne suffisent pas

Les praticiens interrogés donnent trois raisons d'écarter les bancs d'essai publics [11]. Les domaines réglementés manquent de données publiques. La personnalisation par client rend un banc standard impraticable. Et un banc bâti pour un déploiement se réutilise mal ailleurs.

Les bancs publics qui imitent l'entreprise gardent deux usages : présélectionner un modèle, et servir de gabarit de conception. EnterpriseBench réunit ainsi 500 tâches dans quatre domaines, avec des sources fragmentées et des hiérarchies de contrôle d'accès; son résumé rapporte 41,8 % d'achèvement pour le meilleur agent testé [14]. Le chapitre 15 compare cinq bancs de ce type. Aucun ne mesure un déploiement réel.

### Construire le sien

Parmi les vingt cas de MAP, cinq équipes ont bâti un banc sur mesure : une à partir de zéro, avec une vérité de référence étiquetée par des experts, et quatre en le synthétisant à partir de tests existants, de journaux ou de billets de soutien [11]. Le chemin le plus court part donc de ce que l'entreprise possède déjà, et l'entrepôt de traces en est la première source.

Six propriétés d'un banc interne utile se dégagent des textes lus.

1. **Il sort de la production.** Les cas viennent de trajectoires réelles, y compris celles qui ont échoué.
2. **Il juge un état.** Le critère de réussite est un état vérifiable du système, non une ressemblance de texte [13].
3. **Il répète.** Chaque tâche s'exécute plusieurs fois, et la constance se rapporte à part [13].
4. **Il contient des refus.** Les demandes à ne pas satisfaire et les règles d'accès y figurent (chapitre 15).
5. **Il garde un jeu réservé.** Nubank répartit ses données d'étalonnage en 40 % pour l'entraînement, 30 % pour la validation et 30 % pour le test [12].
6. **Il est versionné.** Un score ne se compare qu'à version de banc, de juge et de modèle constante.

Un tel banc est un actif de l'entreprise. C'est lui qui dit si un agent survit à un changement de modèle ou de plateforme (chapitres 20 et 27), et si un palier de modèle moins coûteux (chapitre 44) ou un modèle distillé (chapitre 47) suffit.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Format de télémétrie | OpenTelemetry, conventions GenAI | Plateforme fermée : exiger au moins un export |
| Schéma consommé par les tableaux de bord | Schéma interne, alimenté par normalisation au collecteur | Parc d'un seul cadriciel, à version épinglée |
| Version des conventions | Commit épinglé, span exporté vérifié à chaque mise à jour | — |
| Capture du contenu | Désactivée en production | Préproduction, ou stockage conforme et volume maîtrisé |
| Contenu nécessaire à l'évaluation | Stockage distinct, référence dans la trace, accès par rôle | — |
| Corrélation de bout en bout | Identifiant d'affaires sur chaque span racine et chaque événement | Flux entièrement synchrone : le contexte de trace suffit |
| Piste d'audit | Distincte de la trace, jamais échantillonnée | — |
| Évaluateur | Règles, puis juge étalonné (réétalonné à chaque changement de modèle juge), puis expert sur les cas incertains | Faible volume ou risque élevé : revue humaine intégrale |
| Critère de réussite | État final vérifiable, sur plusieurs essais | Tâche sans état observable : grille de critères jugée |
| Banc d'essai | Interne, tiré des traces de production | Présélection d'un modèle : banc public |
| Mise en service d'une variante | Filtre hors ligne, puis fraction du trafic | — |

---

## Points à retenir

- Les signaux classiques ne détectent pas un agent qui accomplit la mauvaise tâche. Il faut tracer la trajectoire et juger son résultat.
- Les conventions GenAI d'OpenTelemetry couvrent l'inférence, les outils, les agents, MCP et A2A. Toutes sont au statut « Development », et leur dépôt dédié n'a publié aucune version.
- La convention MCP lue décrit encore des sessions que la révision `2026-07-28` a supprimées. Un schéma interne et une normalisation au collecteur protègent de ces décalages.
- Le contexte de trace ne survit pas à l'exécution durable. Un identifiant d'affaires est nécessaire.
- Le contenu des échanges est exclu de la télémétrie par défaut. Le stockage par référence concilie exploitation et évaluation.
- Dans l'étude MAP, l'évaluation repose surtout sur des humains, et tout juge automatique observé est doublé d'une revue humaine.
- Un juge automatique s'étalonne contre des étiquettes humaines; changer de modèle juge, c'est changer d'instrument.
- Le coût de l'évaluation continue se maîtrise par un petit juge, l'aiguillage par confiance et l'échantillonnage.
- Le banc d'essai utile est interne, tiré des traces, fondé sur des états vérifiables et répété.

---

## Sources

Pages primaires lues le 11 novembre 2026; [2], [5], [7], [11], [12] et [14] relues le 12 novembre 2026 :

1. [OpenTelemetry — conventions GenAI, avis de déplacement](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
2. [Dépôt open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)
3. [Index des conventions GenAI](https://github.com/open-telemetry/semantic-conventions-genai/tree/main/docs/gen-ai)
4. [Spans d'agent et de cadriciel](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-agent-spans.md)
5. [Spans GenAI — consignation du contenu](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md)
6. [Événements GenAI — résultat d'évaluation](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-events.md)
7. [Conventions MCP](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/mcp.md)
8. [Conventions A2A](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/a2a.md)
9. [Invocation d'agent distant](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/client-invoke-agent.md)
10. [Journal des changements du dépôt](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/CHANGELOG.md)
11. [Measuring Agents in Production (arXiv 2512.04123, v4)](https://arxiv.org/html/2512.04123v4)
12. [Building Customer Support AI Agents at 100M-User Scale — Nubank, KDD 2026 (arXiv 2606.08867)](https://arxiv.org/html/2606.08867v1)
13. [τ-bench (arXiv 2406.12045)](https://arxiv.org/abs/2406.12045) — résumé seulement.
14. [EnterpriseBench (arXiv 2510.27287, EMNLP 2025)](https://arxiv.org/abs/2510.27287) — résumé seulement.

Source secondaire :

15. [John Hodge — état des conventions GenAI d'OpenTelemetry, mis à jour le 3 novembre 2026](https://john-hodge.com/blog/opentelemetry-genai-semantic-conventions/) — billet d'un particulier, lu et relu le 12 novembre 2026.

## Limites de ce chapitre

- Les pages ont été lues au moyen d'un outil d'extraction qui résume le texte; les noms d'attributs et les valeurs sont repris tels que rapportés, sans relecture du texte brut. La fin de la page MCP [7] a été relue à l'audit; la seconde moitié de l'article [11] n'a pas été lue.
- La date du déplacement des conventions, l'historique des renommages et le retrait de `gen_ai.client.token.usage` viennent de la seule source secondaire [15]; les notes de version du dépôt principal n'ont pas été lues.
- MAP exprime en pourcentage (75 %) la part des équipes sans banc d'essai, que ce chapitre et le chapitre 42 rendent par « les trois quarts ».
- Le sens du statut « Development », le caractère échantillonnable des traces et la propagation des bagages jusqu'au tiers appelé relèvent de la connaissance générale d'OpenTelemetry.
- Les documents sur l'exécution d'outil, la récupération, les métriques et les fournisseurs n'ont pas été lus; le tableau de la section 33.1 les décrit d'après l'index et les pages voisines.
- Les sections 33.5 à 33.7 reposent en bonne partie sur un seul déploiement, celui de Nubank, décrit par ses auteurs et non vérifié de façon indépendante.
- La séparation de la trace et de la piste d'audit, le patron à deux zones, l'ordre des évaluateurs dans la grille et les six propriétés d'un banc interne sont des synthèses de ce chapitre, non des prescriptions d'une source.
- Aucune étude du coût de l'évaluation continue n'a été trouvée.
- Aucun produit d'observabilité commercial n'est comparé.
