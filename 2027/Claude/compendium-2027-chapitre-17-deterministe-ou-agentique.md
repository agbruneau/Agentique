# Chapitre 17 — Déterministe ou agentique

*Question directrice : où placer le non-déterminisme dans un processus d'affaires ?*

> **Version 2 — 11 novembre 2026.** État de référence : documentation Camunda 8.11 (branche « next », non publiée; la dernière version publiée est la 8.10), documentation UiPath Maestro pour Automation Cloud, prépublication Routine (v2, 22 juillet 2025). Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [12] sont des pages primaires lues pour ce chapitre, [13] et [14] sont secondaires. Les renvois « chapitre N » pointent vers les autres chapitres du compendium. Chapitre audité et révisé le 12 novembre 2026.

Un processus d'affaires est une promesse de répétabilité : la même demande, traitée deux fois, suit le même chemin et laisse la même trace. Un modèle de langage offre l'inverse. Il interprète une entrée imprévue, choisit une suite d'actions que personne n'a écrite, et ne garantit pas de refaire le même choix. Les deux propriétés sont utiles, mais pas au même endroit.

Le débat « workflow ou agent » est donc mal posé. Le chapitre 1 a fixé le critère qui sépare les deux : qui décide du chemin, le concepteur ou le modèle. La question de ce chapitre vient ensuite : dans un processus donné, quelles décisions confier au modèle, et sous quelle enveloppe.

La thèse tient en une phrase. Le non-déterminisme se place dans une région bornée du processus, là où la variabilité des cas le justifie; l'enveloppe — séquence imposée, contrôles, approbations, effets irréversibles, trace — reste déterministe. Le moteur de processus, la gestion de cas et la planification structurée sont trois façons de bâtir cette enveloppe. Le processus exposé comme outil en est une quatrième, vue depuis l'agent.

---

## 17.1 Un spectre : workflow, étapes agentiques, agent borné, agent ouvert

### Deux pôles

La distinction de référence vient d'un texte d'ingénierie d'Anthropic publié en décembre 2024 [1]. Un *workflow* orchestre des modèles et des outils selon des chemins de code prédéfinis. Un *agent* laisse le modèle diriger lui-même son processus et son usage des outils. Le texte y joint un conseil de sobriété : chercher la solution la plus simple, quitte à ne pas construire d'agent, et n'ajouter de la complexité que si elle améliore les résultats de façon démontrable. Il nomme aussi le prix de l'autonomie : latence, coût, et erreurs qui s'accumulent d'une étape à l'autre.

### Quatre positions

Entre ces deux pôles, la pratique d'entreprise occupe au moins quatre positions.

| Position | Qui décide du chemin | Ce que décide le modèle | Forme typique |
|---|---|---|---|
| Workflow | Le concepteur, entièrement | Le contenu d'une étape : classer, extraire, rédiger | Tâche qui appelle un modèle; chaînage, routage [1] |
| Étapes agentiques | Le concepteur, entre les étapes | La conduite d'une étape, outils compris | Agent appelé comme tâche d'un processus [8] |
| Agent borné | Le modèle, dans une région délimitée | Les outils, leur ordre et leurs paramètres, dans une liste fermée et sous un plafond | Sous-processus ad hoc [3][4]; plan structuré [11] |
| Agent ouvert | Le modèle | Le plan, les outils, le critère d'arrêt | Agent autonome muni d'un catalogue d'outils |

La position est une propriété d'une **région** du processus, non du système entier. Un même traitement de réclamation peut commencer par une extraction (workflow), confier l'enquête à un agent borné, puis revenir à une séquence fixe pour le paiement.

La frontière entre la deuxième et la troisième position est une frontière de **visibilité**. Dans une étape agentique, l'agent est une boîte dont le processus ne connaît que l'entrée et la sortie. Dans un agent borné, chaque appel d'outil est une activité du processus lui-même. Camunda trace exactement cette ligne quand il distingue ses propres agents, dont la boucle tourne dans le moteur, des agents externes, dont il ne voit que ce que leur environnement d'exécution renvoie [3].

### Ce que montre la pratique

L'étude Measuring Agents in Production, fondée sur vingt études de cas et un sondage de 306 réponses, dont 86 sur des systèmes déployés, rapporte que 68 % de ces systèmes exécutent moins de dix étapes avant une intervention humaine (au plus dix selon son résumé), et que la fiabilité, premier défi cité, se traite surtout par la conception du système [12]. Les chapitres 4 et 22 exploitent ces résultats; selon le chapitre 42, seize des vingt cas reposent sur des workflows prédéfinis : les déploiements réels occupent surtout les trois premières positions.

---

## 17.2 BPMN comme enveloppe : le sous-processus ad hoc

### Un élément ancien pour un besoin nouveau

BPMN possède un élément conçu pour le travail dont l'ordre n'est pas connu d'avance : le sous-processus ad hoc, marqué d'un tilde. Dans la mise en œuvre de Camunda, il regroupe des activités qui peuvent s'exécuter dans n'importe quel ordre, plusieurs fois ou pas du tout; il ne contient ni événement de début ni événement de fin, et des flux de séquence peuvent y imposer une structure partielle quand certaines activités dépendent l'une de l'autre [4].

C'est la forme qu'il faut à un agent borné : une frontière nette, une liste fermée d'actions, un ordre libre à l'intérieur.

### La boucle confinée

Camunda définit l'agent par sa boucle : le modèle décide de la prochaine action, des outils à appeler et du moment d'arrêter. Un appel de modèle sans boucle ni choix d'outil n'est pas un agent [3]. Cette boucle est logée dans un sous-processus ad hoc, selon une convention simple [2][4] :

- chaque élément BPMN du sous-processus est exposé au modèle comme un outil;
- l'identifiant de l'élément sert de nom d'outil, et son champ de documentation, de description;
- les paramètres attendus du modèle sont déclarés par la fonction `fromAi`.

Le partage des responsabilités est explicite [3]. Le modèle choisit l'outil, l'ordre et les paramètres. Le moteur exécute l'activité choisie, conserve les variables, gère les nouvelles tentatives et les incidents, route les tâches humaines et les événements.

Le mécanisme sous-jacent porte la garantie. Le sous-processus ad hoc peut être piloté par un *job worker* : le moteur crée un travail à l'activation, puis un nouveau à chaque fin de flux interne, et attend qu'on lui dise quels éléments activer ou si le sous-processus est terminé [4]. Le connecteur d'agent tient ce rôle. Le modèle n'exécute donc jamais rien : il propose, le moteur active. Pour l'activation par expression, la documentation précise qu'un identifiant étranger au sous-processus crée un incident, non une action [4].

**Un outil peut contenir toute la logique BPMN.** Un outil peut être une tâche de service, un sous-processus entier ou l'appel d'un autre processus [2]. La partie déterministe ne s'arrête donc pas à la frontière de l'agent : elle se retrouve à l'intérieur de chacun de ses outils.

**La boucle a un plafond.** Le connecteur limite le nombre d'appels au modèle, à dix par défaut, et borne la fenêtre de contexte à vingt messages par défaut [5]. La documentation précise que ce plafond ne remplace pas la surveillance des coûts chez le fournisseur du modèle (chapitre 40).

**Le processus peut interrompre le raisonnement.** Des sous-processus d'événements non interruptifs permettent de réagir à un message externe ou à une minuterie pendant que l'agent travaille [2]. Deux comportements sont offerts : attendre la fin des appels d'outils en cours, ou les annuler et en informer le modèle [5].

**La qualité des descriptions devient une question de fiabilité.** Le modèle choisit sur la foi du nom et de la documentation de chaque élément; une description vague multiplie les mauvais choix et les appels répétés [2]. Modéliser le processus, c'est aussi rédiger du contexte (chapitre 13).

### L'agent comme tâche

UiPath Maestro adopte, dans son canevas BPMN, l'autre construction. L'agent y est représenté par une tâche de service. Le processus lui envoie des paramètres d'entrée, attend, puis reçoit une sortie en JSON dont chaque paramètre doit être affecté à une variable de processus. La suite — branchements (*gateways*), affectations, actions — s'appuie sur ces variables [8]. L'agent peut être hébergé chez UiPath ou être un agent externe joint par un connecteur; la page cite notamment CrewAI, Databricks et Google Vertex.

La page ne parle pas de déterminisme; selon la lecture proposée ici, la boucle de l'agent reste hors du modèle de processus, et l'enveloppe repose sur deux choses, un contrat de sortie strict et un routage fixé à la conception.

| | Boucle confinée | Agent comme tâche |
|---|---|---|
| Où tourne la boucle | Dans le moteur de processus | Dans l'agent appelé |
| Ce que voit le processus | Chaque appel d'outil, comme activité | L'entrée, la sortie, et la trace que l'agent fournit |
| Ce qui borne l'agent | Liste fermée d'outils, plafond d'appels, événements | Contrat de sortie, routage en aval |

Les deux constructions ne s'excluent pas : Camunda prend aussi en charge des agents externes [3].

### Règles de conception

La page de conception de Camunda énonce des principes qui valent au-delà du produit [2] :

- partir du problème du processus, et n'introduire un agent que s'il aide à le résoudre;
- encadrer l'agent d'une vérification (*guardrail sandwich*) : un agent exécute, un second contrôle le raisonnement et la conformité, et un échec renvoie à un humain;
- donner à l'agent des sorties déterministes, et non seulement des niveaux de confiance;
- prévoir un chemin d'escalade vers un humain (chapitre 22);
- versionner les prompts, pour pouvoir revenir en arrière.

Un agent qui ne rend qu'un niveau de confiance reporte le problème sur le branchement suivant, qui devra choisir un seuil. Un agent tenu de rendre l'une de quelques issues nommées donne au processus une variable sur laquelle router.

---

## 17.3 Gestion de cas et processus à exceptions

### Quand le diagramme ne suffit plus

Un sinistre, un litige de facturation ou une remédiation de conformité avancent par retours en arrière, attendent des pièces, changent de mains. Les représenter en BPMN strict oblige à prévoir chaque exception par un branchement, jusqu'à rendre le diagramme illisible.

UiPath Maestro consacre à cette classe de problèmes un canevas de gestion de cas, Case, distinct de son canevas BPMN, avec un test simple pour choisir : si l'étape suivante dépend de ce qui vient de se passer, le cas convient; si le processus suit toujours le même chemin, BPMN suffit [10]. Les indices retenus sont une durée qui se compte en heures ou en semaines, des exceptions attendues et non rares, plusieurs équipes, des retours fréquents à une étape antérieure, des délais de service à suivre par phase.

### Les règles d'abord, l'agent ensuite

Un cas se compose de phases (*stages*), primaires pour le parcours principal et secondaires pour les exceptions, de règles d'entrée, de complétion, de sortie et de réentrée, et de tâches de types variés : action humaine, robot, appel d'API, agent, processus BPMN, cas enfant [10].

Le chemin se décide à l'exécution, par trois mécanismes ordonnés [10] :

1. les règles du plan de cas, déterministes, traitent les scénarios prévus;
2. un agent gestionnaire de cas (*Case Manager*), fondé sur un modèle de langage, raisonne sur l'état du cas, le plan et les politiques, et prend le relais pour les écarts;
3. si ni les règles ni l'agent ne peuvent trancher — données ambiguës, politiques contradictoires, décision hors de son autorité —, le cas est escaladé à un humain.

Cet ordre est une règle de placement en soi : le modèle n'intervient que là où les règles s'arrêtent.

### Une symétrie utile

La gestion de cas place le non-déterminisme à l'inverse des étapes agentiques.

| Patron | Routage entre les étapes | Contenu des étapes |
|---|---|---|
| Étapes agentiques | Fixé à la conception | Confié à un agent |
| Gestion de cas | Décidé à l'exécution, règles puis agent | Souvent déterministe : processus, robot, action humaine |

Les deux se composent. Un cas peut lancer un processus BPMN pour une phase linéaire, et un processus BPMN peut ouvrir un cas [10]. Camunda décrit la même combinaison avec d'autres mots : orchestration déterministe pour les chemins clairs, les décisions répétables et les séquences qu'impose la réglementation; orchestration dynamique pour le tri, la classification et l'enquête. Son exemple est la connaissance du client, où un agent guide la personne et ajuste le niveau de risque sans que la conformité cesse d'être prévisible [2].

Réserve de maturité : dans la documentation lue, l'entité de cas, c'est-à-dire l'objet de données persistant qui sert de source unique de vérité, est marquée comme à venir [10].

---

## 17.4 Planification structurée

### Le plan comme artefact

Entre le chemin codé dans un moteur et le chemin improvisé par le modèle, il existe une voie moyenne : écrire le chemin en langage naturel structuré, et demander au modèle de le suivre. Le cadre Routine, décrit dans une prépublication de 2025, en donne la forme la plus aboutie parmi les sources lues [11].

Une Routine est un plan en étapes numérotées. Chaque étape porte un nom, une description avec ses conditions d'exécution, au besoin une description des entrées et des sorties, et un seul outil. Les branches sont numérotées elles aussi, de sorte que le modèle sait où il se trouve. Le plan naît d'un brouillon rédigé par un expert du domaine; un modèle de planification le décompose et rattache chaque étape à un outil disponible, puis un expert relit le résultat.

Trois choix d'architecture accompagnent ce format [11].

- **Deux modèles.** Un grand modèle planifie, en amont. Un petit modèle exécute : il suit la Routine et ne produit que des appels d'outils. La réponse finale est rédigée par un outil de synthèse à la dernière étape.
- **Une mémoire procédurale.** Les Routines sont rangées dans une base, et celle qui convient est retrouvée par similarité avec la demande. Le contexte ne porte qu'une procédure à la fois.
- **Une mémoire de variables.** Un résultat d'outil trop long est rangé sous une clé, que le modèle transmet à sa place.

### Ce que disent les chiffres, et leur portée

Sur un scénario réel de ressources humaines, avec sept Routines et vingt-cinq outils exposés par MCP, les auteurs rapportent que la précision des appels d'outils passe de 41,1 % à 96,3 % pour GPT-4o, et de 32,6 % à 83,3 % pour un modèle plus petit, Qwen3-14B. Affiné sur des exemples distillés du scénario, ce dernier atteint 95,5 % [11]; la distillation vers de petits modèles relève du chapitre 47.

Trois réserves s'imposent. Ces résultats viennent d'une prépublication et d'une seule expérience, mesurée par ses auteurs. Le gain dépend de brouillons d'experts, ce qui limite la généralisation quand les outils ou les procédures changent; les auteurs le reconnaissent. Et la mesure porte sur la justesse des appels d'outils, non sur le résultat d'affaires.

### Guider n'est pas contraindre

Une Routine guide le modèle; elle ne le contraint pas. Rien, dans le cadre décrit, n'empêche le modèle de sauter une étape : il ne le fait pas, la plupart du temps. Un moteur de processus, lui, ne peut pas sauter une étape. Le reliquat d'erreur d'une planification structurée, même faible, doit donc être rattrapé par autre chose : une validation en aval, une approbation, ou un outil qui refuse d'agir si l'étape préalable manque.

La planification structurée convient quand les procédures sont nombreuses et changeantes, que leur auteur est un expert du métier plutôt qu'un modélisateur, et qu'une erreur d'ordre se détecte et se corrige. Elle convient mal à une séquence que la réglementation impose. Le conditionnement de connaissances procédurales, dont les Agent Skills, relève du chapitre 13.

---

## 17.5 Le processus exposé comme outil

### Renverser la perspective

Les sections précédentes logeaient l'agent dans le processus. L'inverse consiste à loger le processus derrière un outil, et laisser un agent, borné ou ouvert, décider de le lancer.

Un billet de Camunda du 18 août 2026 distingue trois directions pour MCP [6].

| Direction | Mécanisme | Usage |
|---|---|---|
| Le processus appelle un serveur MCP | Connecteurs MCP Client dans un sous-processus ad hoc | Donner à l'agent des outils externes, dont le choix reste visible dans le processus |
| Un client appelle le moteur | Point d'accès MCP du cluster d'orchestration | Consulter les instances, résoudre des incidents, démarrer un processus en langage naturel |
| Un processus devient un outil | Gabarit *MCP start event* et Processes MCP Server | Laisser un agent externe déclencher un processus |

Dans la troisième direction, le nom de l'outil, sa description et ses entrées sont définis dans le modèle BPMN, et l'outil est découvert au déploiement. L'appel démarre le processus et renvoie aussitôt une clé d'instance : l'agent déclenche et suit, il n'attend pas le résultat [6].

### Deux façons d'appeler, deux traces

Pour un agent Camunda qui appelle un autre processus, la documentation compare deux voies [2].

| | Activité d'appel (*call activity*) | Client MCP |
|---|---|---|
| Portée | Même cluster | Autre cluster |
| Résultat | L'appel attend la fin et renvoie la sortie à l'agent | L'outil renvoie la clé d'instance, sans la sortie |
| Hiérarchie | Instance enfant, visible dans l'arbre | Aucun lien structurel avec l'appelant |
| Audit | Trace complète de la hiérarchie | Déclenchement externe, sans lien avec l'agent |

Le choix a un coût d'audit : franchir une frontière de cluster par MCP rompt le lien entre l'agent et ce qu'il a déclenché, sauf à le reconstituer par corrélation. Un processus lancé sans attente est aussi un travail de longue durée, à suivre et à reprendre (chapitres 5 et 18).

### Pourquoi le patron compte

Exposé comme outil, un processus n'est plus un appel d'API, mais une transaction d'affaires entière, avec ses contrôles internes. L'agent décide s'il faut la lancer et quand; il ne peut pas en sauter la troisième étape. Un agent ouvert accède ainsi aux systèmes d'enregistrement sans en recevoir la séquence; le chapitre 25 en fait un principe d'intégration au patrimoine.

La deuxième direction appelle la prudence inverse. Un point d'accès qui démarre des instances et résout des incidents, avec la même authentification que l'API REST [6], est un accès opérationnel, à soumettre à l'autorisation par opération (chapitre 30).

### A2A : un état à dater

⚠ La prise en charge d'A2A par Camunda est partielle à la date de rédaction. La documentation présente trois connecteurs clients — envoi de messages et lecture de l'Agent Card, interrogation des tâches asynchrones, réception par webhook — rangés parmi les fonctionnalités alpha. Elle avertit qu'ils ne prennent pas encore en charge l'authentification auprès d'un serveur A2A distant [7]. Les notes de version de la 8.9 (avril 2026) les introduisent, pour la collaboration multi-agents avec le connecteur d'agent [14]. Selon un résumé non vérifié, ils peuvent servir soit de tâche de service déterministe, soit d'outil offert à l'agent [13]. Aucune page lue ne décrit l'exposition d'un processus Camunda comme agent A2A. Conclusion prudente : un usage expérimental tant que l'authentification manque.

Côté UiPath, les pages Maestro lues ne mentionnent ni MCP ni A2A [8][9]; le chapitre 26 relève toutefois, dans la documentation d'Orchestrator, une prise en charge d'A2A en préversion.

---

## 17.6 Critères de placement

### Sept critères

| Critère | Penche vers le déterministe | Penche vers l'agentique |
|---|---|---|
| Variabilité du chemin | Le même chemin à chaque fois [10] | L'étape suivante dépend de ce qui vient de se passer [10] |
| Nature des entrées | Structurées, validées par schéma | Non structurées : tri, classification, enquête [2] |
| Séquence imposée | Par la réglementation ou le contrôle interne [2] | Aucune contrainte d'ordre |
| Coût et réversibilité de l'erreur | Effet irréversible ou coûteux | Erreur détectable et corrigible |
| Volume, latence, coût unitaire | Fort volume, délai serré [1] | Faible volume, valeur élevée par cas |
| Vérifiabilité du résultat | Difficile à vérifier après coup | Vérifiable par une règle ou un second regard |
| Rythme de changement | Procédure stable | Procédures nombreuses et changeantes [11] |

Un critère seul ne tranche pas. Une enquête de fraude a des entrées non structurées et un chemin variable, mais son issue, le gel d'un compte, est un effet lourd. La réponse est de découper : enquête agentique, décision par règle ou par un humain, exécution déterministe.

### Trois types de décisions

Le découpage se fait mieux en distinguant ce que le modèle décide. Cette typologie est une proposition du chapitre.

- **Interpréter** : classer une demande, extraire des champs, résumer un dossier. Le non-déterminisme porte sur une valeur, que le processus peut valider avant de s'en servir. C'est le placement le moins risqué, à condition de valider : un routeur fondé sur un modèle change souvent de choix devant une simple reformulation (chapitre 44).
- **Choisir** : sélectionner l'outil suivant, l'ordre, les paramètres. Le non-déterminisme porte sur le chemin. Il demande une liste fermée, un plafond et une trace de chaque choix.
- **Engager** : produire un effet dans un système d'enregistrement ou vis-à-vis d'un tiers. Le modèle peut le proposer; l'exécution passe par une étape déterministe et, selon la classe d'action, par une approbation.

Certaines décisions ne se délèguent pas au modèle, quel que soit le patron : la vérification d'une autorisation, le calcul d'un montant, l'application d'un seuil réglementaire, le franchissement d'un point de non-retour (chapitre 18). Elles s'expriment par des règles ou du code, que le modèle appelle ou que le processus applique après lui.

### Un ordre de progression

Les sources convergent sur le point de départ : la solution la plus simple qui fonctionne, et l'agent seulement s'il résout un problème du processus [1][2]. La progression va du workflow vers l'agent borné, région par région, sur preuve (chapitre 22). La répartition du travail entre plusieurs agents relève du chapitre 16.

---

## 17.7 Auditabilité

### Deux questions

Un auditeur pose deux questions : que s'est-il passé, et pourquoi. L'enveloppe déterministe répond à la première. La seconde, pour la part confiée au modèle, n'a qu'une réponse partielle.

### Ce que l'enveloppe enregistre

Dans la construction à boucle confinée, la trace est celle du moteur de processus. Chaque appel d'outil est une activité exécutée, avec ses variables; chaque agent spécialisé appelé comme processus apparaît comme une instance enfant; la découverte des outils d'un serveur MCP figure elle-même dans la piste d'audit [2][3][6]. Cette trace a des angles morts.

- **Le lieu de stockage de la conversation.** L'historique affiché dans l'outil d'exploitation vient d'une API propre aux instances d'agent, distincte du stockage du contexte. Seul le stockage dans les variables de processus permet d'inspecter le JSON brut; avec le stockage documentaire, assorti d'une durée de vie, la variable ne contient qu'une référence [5]. Une durée de vie plus courte que l'obligation de conservation efface la justification avant l'échéance.
- **Les frontières.** Un processus déclenché par MCP sur un autre cluster n'est pas rattaché à l'agent appelant [2]. Un agent externe ne livre que ce que son environnement renvoie [3].

Dans la construction à agent comme tâche, le processus conserve l'historique de chaque instance, avec les entrées et les sorties de l'agent; UiPath mentionne des données de trace — outils utilisés, décisions — pour le débogage et la transparence [8][9]. Leur profondeur dépend de l'agent appelé, surtout s'il est externe.

### Rejouer et expliquer

Un processus déterministe se rejoue : mêmes entrées, même chemin. Une étape agentique ne se rejoue pas, elle se consigne. La piste d'audit doit donc conserver ce qui permet de reconstituer la décision sans la reproduire : la version du prompt [2], l'identité du modèle, la liste d'outils offerte, les entrées, chaque appel et son résultat, la sortie. La justification que rédige le modèle est un élément du dossier, non une preuve de son raisonnement.

Plus la région agentique est petite, plus la part inexpliquée du dossier l'est aussi. Et les sorties déterministes de la section 17.2 servent autant l'audit que le routage : une issue nommée se compte et se contrôle. Les conventions de trace sont traitées au chapitre 33, l'imputabilité au chapitre 36.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Point de départ | Workflow; agent seulement si un problème du processus l'exige | Travail d'enquête ou de tri sans chemin stable |
| Forme de la région agentique | Agent borné : liste fermée d'outils, plafond d'appels | Agent externe déjà en place : l'appeler comme tâche, avec contrat de sortie |
| Processus à exceptions | Gestion de cas, règles d'abord, agent en repli, humain en dernier recours | Exceptions rares : BPMN avec quelques branchements |
| Sortie d'un agent | Issues nommées, routables | Niveau de confiance seulement comme information d'appoint |
| Procédures nombreuses et changeantes | Plan structuré rédigé par le métier, validé en aval | Séquence réglementaire : moteur de processus |
| Accès d'un agent ouvert aux systèmes d'enregistrement | Processus exposé comme outil | Lecture seule : outil direct |
| Appel d'un processus par un agent | Activité d'appel dans le même cluster | Autre cluster : MCP, avec corrélation explicite pour l'audit |
| Effets irréversibles | Étape déterministe, approbation selon la classe d'action | — |
| Agents distants par A2A depuis Camunda | Hors production tant que l'authentification manque côté connecteur | Pilote sans données sensibles |

---

## Points à retenir

- La question n'est pas « workflow ou agent », mais quelle région d'un processus confier au modèle, et sous quelle enveloppe. Quatre positions se distinguent : workflow, étapes agentiques, agent borné, agent ouvert.
- Le sous-processus ad hoc de BPMN donne sa forme à l'agent borné : le modèle propose un outil dans une liste fermée, le moteur l'exécute et en garde la trace.
- L'autre construction appelle l'agent comme une tâche et fait reposer l'enveloppe sur un contrat de sortie et un routage fixe. Elle voit moins, mais accueille des agents externes.
- La gestion de cas inverse le placement : le routage se décide à l'exécution, les règles d'abord et l'agent ensuite, alors que le contenu des étapes reste souvent déterministe.
- Un plan structuré guide le modèle sans le contraindre. Son reliquat d'erreur doit être rattrapé par l'enveloppe.
- Exposer un processus comme outil donne à un agent une transaction entière qu'il peut lancer, mais non réordonner.
- Interpréter, choisir, engager : le risque croît dans cet ordre. Autorisations, montants, seuils et points de non-retour restent hors du modèle.
- Une étape agentique se consigne, elle ne se rejoue pas. La taille de la région agentique fixe la part inexpliquée du dossier d'audit.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Anthropic — Building effective agents (19 décembre 2024)](https://www.anthropic.com/engineering/building-effective-agents)
2. [Camunda — Agentic orchestration : design and architecture (8.11, « next »)](https://docs.camunda.io/docs/next/components/agentic-orchestration/ao-design/)
3. [Camunda — AI agents](https://docs.camunda.io/docs/next/components/agentic-orchestration/ai-agents/)
4. [Camunda — Ad-hoc sub-processes](https://docs.camunda.io/docs/next/components/modeler/bpmn/ad-hoc-subprocesses/)
5. [Camunda — AI Agent Sub-process connector](https://docs.camunda.io/docs/next/components/connectors/out-of-the-box-connectors/agentic-ai-aiagent-subprocess/)
6. [Camunda — Three ways Camunda speaks MCP (18 août 2026)](https://camunda.com/blog/2026/08/three-ways-camunda-speaks-mcp-and-why-the-direction-matters/) — billet de fournisseur
7. [Camunda — A2A Client (fonctionnalités alpha)](https://docs.camunda.io/docs/next/components/early-access/alpha/a2a-client/)
8. [UiPath Maestro — Using agents in Maestro](https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/using-agents-in-maestro)
9. [UiPath Maestro — What you get with Maestro](https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/value-proposition)
10. [UiPath Maestro — Maestro BPMN vs. Maestro Case](https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/maestro-bpmn-vs-maestro-case-when-to-use-case-management)
11. [Routine: A Structural Planning Framework for LLM Agent System in Enterprise (arXiv 2507.14447v2)](https://arxiv.org/html/2507.14447v2) — prépublication
12. [Measuring Agents in Production (arXiv 2512.04123)](https://arxiv.org/abs/2512.04123) — version 4

Sources secondaires :

13. [Camunda — Designing A2A Orchestration with Camunda (février 2026)](https://camunda.com/blog/2026/02/using-a2a-to-achieve-your-business-goals-pt-1/) — résumé de recherche seulement, page non lue.
14. [Camunda — notes de version 8.9](https://docs.camunda.io/docs/reference/announcements-release-notes/890/890-release-notes/) — page de documentation, lue lors de l'audit du 12 novembre 2026.

## Limites de ce chapitre

- Les pages ont été lues par un outil d'extraction qui condense le contenu; la formulation exacte n'a pas été vérifiée mot à mot.
- La documentation Camunda lue est celle de la branche « next » (8.11, non publiée). Les valeurs par défaut citées peuvent différer de celles de la version 8.10.
- La page UiPath donnée en appui par la carte thématique (« agentic automation ») renvoie une erreur 404 au 11 novembre 2026; les pages voisines [8] à [10] l'ont remplacée. Le canevas Flow de Maestro n'a pas été étudié.
- Les spécifications BPMN 2.0 et CMMN de l'OMG n'ont pas été lues. Le sous-processus ad hoc est décrit d'après Camunda; son appartenance au standard BPMN et sa destination d'origine reposent sur la connaissance générale, de même que l'affirmation qu'un BPMN strict devient illisible pour un processus à exceptions (17.3).
- La lecture « routage fixe » de UiPath Maestro, la typologie interpréter-choisir-engager, les critères de coût, de réversibilité et de vérifiabilité (17.6) et la liste des éléments à consigner (17.7) sont des analyses du chapitre, non des énoncés des sources.
- Routine est une prépublication évaluée par ses auteurs sur un seul scénario. Le corps de MAP a été lu le 12 novembre 2026 pour l'échantillon et le nombre d'étapes. L'article sur l'architecture pour l'IA composée, cité par la carte, n'a pas été lu et n'est pas utilisé.
- Les cadriciels à graphe d'état, autre forme d'enveloppe, sont laissés au chapitre 20; les moteurs d'exécution durable, au chapitre 18; le contrôleur vérifié qui encadre un contrôleur appris en robotique, au chapitre 46.
- L'audit du 12 novembre 2026 a relu [5] à [8], [11] et le résumé de [12], et lu [14] : faits confirmés. L'apparition des connecteurs A2A en 8.9 est établie; leur double usage, tâche de service ou outil d'agent, ne repose que sur [13]. [1] à [4], [9] et [10] n'ont pas été relus.
- Aucune évaluation indépendante des produits cités n'a été trouvée : les sections 17.2, 17.3 et 17.5 reposent sur la documentation des éditeurs.
