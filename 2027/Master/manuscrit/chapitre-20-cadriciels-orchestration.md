# Chapitre 20 — Cadriciels d'orchestration

*Question directrice : sur quoi bâtir, et comment éviter le verrouillage ?*

> **État de référence :** documentation des éditeurs telle que publiée à cette date (pages Microsoft datées des 22 et 23 octobre 2026, ADK 2.0, DSPy 3.5.0). Les numéros entre crochets renvoient aux sources en fin de chapitre; toutes sont des pages primaires lues pour ce chapitre, sauf [14], lue en résumé, et [15], secondaire et non lue; [16] à [21] ont été ajoutées le 14 novembre 2026, [21] par son seul résumé.

Un modèle de langage produit une réponse à partir d'un contexte. Tout le reste est du code à écrire autour : la boucle qui enchaîne les appels d'outils, l'état qui survit d'une étape à l'autre, la répartition du travail entre agents, la pause qui attend une approbation. Un cadriciel d'orchestration fournit ce code, et son choix passe pour structurant.

Ce chapitre soutient qu'il l'est moins qu'on le croit, pour deux raisons. La première : les cadriciels convergent. Presque tous proposent aujourd'hui les deux mêmes étages, une boucle d'agent et un workflow explicite, et se distinguent surtout par leurs attaches à un modèle, à un environnement d'exécution ou à une plateforme. La seconde : le cadriciel est la couche la plus périssable de l'architecture. Trois des produits décrits ici remplacent un prédécesseur du même éditeur. Le verrouillage ne s'évite donc pas en choisissant le « bon » cadriciel, mais en plaçant les frontières du système sur des protocoles ouverts, de sorte que le cadriciel reste un détail de mise en œuvre.

---

## 20.1 Critères

Le plan initial retient quatre critères et donne pour appui le relevé de Zhu et coll. [15]. Ce relevé n'a pas pu être lu; les critères sont donc appliqués à partir de la documentation de chaque produit. Un cinquième s'ajoute, parce que la question directrice l'exige.

### Gestion d'état

L'état est ce que le système sait entre deux appels au modèle. Les pages lues en montrent trois formes. La première est un état partagé et typé, que chaque étape lit et met à jour selon des règles de fusion déclarées : c'est le modèle de LangGraph [2]. La deuxième est une session, c'est-à-dire l'historique d'une conversation que la boucle d'agent prolonge : c'est le modèle des SDK des fournisseurs [9][12]. La troisième sépare l'état d'un workflow de l'historique des agents qu'il coordonne, comme le fait Microsoft Agent Framework [7].

### Coût en jetons

À chaque appel, le cadriciel décide de ce qui entre dans le contexte : instructions, descriptions d'outils, historique, messages échangés entre agents. Chaque couche d'abstraction y ajoute du texte, et chaque agent supplémentaire relit une partie de ce que les autres ont produit. C'est un raisonnement, pas une mesure : aucune page lue ne publie de chiffre comparatif.

Ce qui se vérifie, ce sont les leviers offerts. ADK documente la compression et la mise en cache du contexte [10]. L'agent « harnais » de Microsoft inclut la compaction du contexte [6]. Les sous-agents du Claude Agent SDK traitent une sous-tâche ciblée [12], ce qui borne ce que chaque contexte doit contenir. Le critère pratique est double : le cadriciel laisse-t-il voir ce qu'il envoie au modèle, et permet-il de le réduire (chapitres 13 et 40) ?

### Reprise sur échec

Trois niveaux se distinguent. Au plus bas, l'état vit en mémoire et disparaît avec le processus. Au milieu, le cadriciel écrit des points de contrôle dans un magasin et reprend depuis le dernier. Au plus haut, l'exécution est confiée à un moteur d'exécution durable, qui la récupère à travers plusieurs machines (chapitre 18).

### Philosophie

Un cadriciel prescrit plus ou moins. LangGraph ne prescrit ni prompts ni architecture d'agent [1]. CrewAI propose une métaphore d'organisation : des équipes d'agents [4]. Le Claude Agent SDK livre un agent complet, avec ses outils et sa gestion du contexte [12]. Plus la prescription est forte, plus le démarrage est rapide et plus le comportement dépend de choix que l'équipe n'a pas faits.

### Attaches

C'est le critère du verrouillage, en trois questions : le cadriciel fonctionne-t-il avec plusieurs modèles; exige-t-il un environnement d'exécution particulier; sous quels termes est-il distribué ?

---

## 20.2 Graphes d'état : LangGraph

LangGraph se décrit comme un cadriciel et un runtime d'orchestration de bas niveau, pour des agents à état et de longue durée [1]. Son modèle tient en trois éléments [2].

L'**état** est un instantané partagé de l'application, le plus souvent un schéma typé, rangé dans des canaux nommés. Les **nœuds** sont des fonctions ordinaires qui lisent l'état, font un travail et renvoient des mises à jour. Les **arêtes**, fixes ou conditionnelles, déterminent le nœud suivant. Le graphe se compile avant exécution; la compilation vérifie sa structure et attache le magasin de points de contrôle et les points d'arrêt.

Deux mécanismes donnent sa précision au modèle. Chaque clé de l'état a un **réducteur**, fonction qui combine la valeur courante et la mise à jour d'un nœud : par défaut la nouvelle valeur remplace l'ancienne, mais un réducteur peut l'ajouter à une liste. La façon dont deux agents écrivent au même endroit est ainsi déclarée, non laissée au hasard de l'ordre d'exécution. L'exécution, elle, avance par **super-étapes**, à la manière du système Pregel de Google : les nœuds parallèles partagent une super-étape, les nœuds en séquence en occupent chacun une, et l'exécution s'arrête quand plus aucun nœud n'est actif [2].

Le routage dynamique passe par trois constructions : une arête conditionnelle, dont une fonction lit l'état et nomme le ou les nœuds suivants; `Command`, quand une même étape doit modifier l'état et choisir la suite; `Send`, pour lancer un nœud une fois par élément quand leur nombre n'est connu qu'à l'exécution. Une limite de récursion, fixée par défaut à 10 007 super-étapes depuis la version 1.1.4, interrompt un graphe qui boucle [2].

**Ce que ce modèle apporte.** La documentation met en avant le mélange d'étapes déterministes et agentiques dans un même graphe, la persistance avec reprise, la pause pour inspection ou correction humaine, la mémoire à court et à long terme, et la diffusion en continu [1]. Le premier compte le plus : le graphe est une enveloppe déterministe dans laquelle le non-déterminisme est confiné à certains nœuds (chapitre 17).

**La persistance.** Un *checkpointer* enregistre l'état d'un fil d'exécution, désigné par un `thread_id` [3]. Les magasins en mémoire perdent tout au redémarrage; la documentation recommande SQLite ou Postgres. LangGraph se situe ainsi au niveau intermédiaire de l'échelle de reprise (modes de durabilité : chapitre 18).

**Les attaches.** LangGraph ne requiert pas LangChain. L'éditeur renvoie vers les agents LangChain ou Deep Agents pour une boucle de plus haut niveau, et réserve LangGraph aux cas qui exigent un contrôle explicite de l'état et du flux [1]. Le déploiement géré est un produit distinct, LangSmith Deployment; avec son Agent Server, la persistance n'est plus à configurer [1][3]. L'attache est donc graduée : nulle pour la bibliothèque, réelle dès que la persistance et l'exploitation sont déléguées au produit.

**Les protocoles.** Deux points se précisent à la lecture de pages voisines. Côté outils, LangChain fournit un adaptateur MCP qui découvre les outils d'un serveur et les rend utilisables par un agent; il est en bêta, et la page prévient que son API peut changer [16]. Côté agents, la bibliothèque seule ne parle pas A2A : c'est Agent Server qui expose chaque assistant à `/a2a/{assistant_id}`, avec sa carte [17]. Il sert la liaison JSON-RPC de la version 1.0 et accepte encore les noms de méthode de la 0.3. gRPC et HTTP+JSON ne sont pas mis en œuvre, la forme des réponses reste celle de la 0.3, et le graphe doit porter une clé `messages`. LangGraph est distribué sous licence MIT [19].

**La contrepartie.** Il faut écrire le schéma d'état, les nœuds et le routage, et le graphe doit prévoir les chemins. Une tâche réellement ouverte s'y plie mal.

---

## 20.3 Rôles et équipes : CrewAI, Microsoft Agent Framework

### CrewAI

CrewAI organise le travail autour de deux notions [4]. Une **Crew** est une équipe d'agents autonomes qui collaborent pour accomplir des tâches. Un **Flow** est un workflow structuré et événementiel qui gère l'état et contrôle l'exécution, avec branchements, boucles et persistance des données d'une étape à l'autre.

Le rapport entre les deux a changé de sens. La documentation qualifie le Flow d'épine dorsale de l'application et recommande, pour toute application destinée à la production, de **commencer par un Flow**; une Crew s'insère dans une étape du Flow quand une tâche complexe demande une équipe [4]. Le cadriciel emblématique de l'approche par rôles conseille donc lui-même une enveloppe déterministe : c'est l'indice le plus net de la convergence.

Pour les outils, un agent CrewAI déclare ses serveurs MCP dans un champ `mcps`, par URL ou par configuration, sur trois transports : stdio, SSE et Streamable HTTP. Seuls les outils sont adaptés; les ressources et les prompts de MCP ne sont pas intégrés. La page demande de ne brancher qu'un serveur de confiance et signale le risque de réassociation DNS sur le transport SSE [18]. Le cadriciel est sous licence MIT [19].

### Microsoft Agent Framework

Microsoft Agent Framework se présente comme le successeur direct de Semantic Kernel et d'AutoGen, créé par les mêmes équipes [6]. Il reprend les abstractions simples du second, les fonctions d'entreprise du premier (état par session, typage, intergiciels, télémétrie) et y ajoute des workflows.

Le cadriciel réunit quatre volets [6] : les agents, qui appellent des outils et des serveurs MCP et fonctionnent avec plusieurs fournisseurs de modèles (Microsoft Foundry, Anthropic, Azure OpenAI, OpenAI, Ollama); un agent « harnais », préconfiguré pour les tâches longues; les workflows; et les intégrations.

La documentation tranche entre agent et workflow.

| Un agent quand… | Un workflow quand… |
|---|---|
| la tâche est ouverte ou conversationnelle | le processus a des étapes bien définies |
| il faut un usage autonome des outils et de la planification | il faut maîtriser l'ordre d'exécution |
| un seul appel au modèle, avec outils, suffit | plusieurs agents ou fonctions doivent se coordonner |

Elle ajoute une règle qui vaut pour tout le chapitre : si une fonction suffit, écrire la fonction plutôt qu'un agent [6].

Les workflows définissent des chemins d'exécution explicites et inspectables [7]. Tous les SDK offrent une API à graphe : des exécuteurs typés reliés par des arêtes et des conditions, avec fan-out et fan-in, et des points de contrôle écrits aux frontières de super-étapes. Python ajoute une API fonctionnelle, expérimentale, où le flux s'exprime en code natif. La demande d'information à un humain est une primitive du workflow (chapitre 22). Un workflow peut enfin s'exposer comme un agent, donc s'emboîter dans un autre ou se publier derrière un protocole.

Sur l'échelle de reprise, ces points de contrôle relèvent du niveau intermédiaire; une extension durable, en préversion, vise le niveau supérieur (chapitre 18).

**État du produit.** Les paquets .NET cités s'installent encore avec l'option de préversion, le SDK Go est en préversion publique, sans agents déclaratifs ni workflows fonctionnels [6]. Une équipe qui s'engage doit vérifier le statut langage par langage. Le dépôt est sous licence MIT [19].

**La leçon de la succession.** Une organisation qui avait bâti sur AutoGen ou sur Semantic Kernel fait face à une migration, guides à l'appui [6]. Le même mouvement s'observe ailleurs : l'OpenAI Agents SDK remplace Swarm [9], et le Claude Agent SDK remplace les paquets du Claude Code SDK [12]. La durée de vie d'un cadriciel se compte en années, celle d'un processus d'affaires en décennies.

---

## 20.4 SDK des fournisseurs de modèles : OpenAI, Google, Anthropic

Les cadriciels des trois grands fournisseurs ne répondent pas à la même question.

| | OpenAI Agents SDK [9] | Google ADK [10] | Claude Agent SDK [12] |
|---|---|---|---|
| Se présente comme | Un paquet léger, à très peu d'abstractions | Un cadriciel ouvert pour bâtir, déboguer et déployer des agents à l'échelle de l'entreprise | Claude Code offert comme bibliothèque |
| Primitives | Agents, transferts (*handoffs*) ou agents comme outils, garde-fous | Agents à modèle, workflows gabarits (séquence, boucle, parallèle), workflows à graphe | Outils intégrés, hooks, sous-agents, permissions, sessions |
| État | Sessions | Sessions, état, mémoire, artefacts | Sessions, à reprendre ou à dupliquer |
| Modèles | OpenAI par défaut; autres fournisseurs par adaptateurs | « Presque tout modèle »; accès direct à Gemini | Non précisé dans la page lue; la bibliothèque exécute le binaire Claude Code |
| Protocoles cités | MCP | MCP, A2A | MCP |

### OpenAI Agents SDK

Le SDK d'OpenAI revendique la sobriété : assez de fonctions pour valoir la peine, assez peu de primitives pour s'apprendre vite [9]. La coordination multi-agents se réduit à deux gestes, le transfert de la conversation à un autre agent ou l'appel d'un agent comme outil. Il n'y a pas de graphe : l'orchestration s'écrit en code ordinaire autour de la boucle. S'y ajoutent des garde-fous sur les entrées et les sorties, des sessions, l'humain dans la boucle, le traçage et des agents en bac à sable aux sessions reprenables.

Le traçage est relié aux outils d'évaluation et d'ajustement d'OpenAI, et les modèles d'OpenAI passent par défaut par son API Responses [9]. Le SDK accepte d'autres fournisseurs, mais sa pente naturelle mène à la plateforme de l'éditeur.

### Google ADK

ADK est le plus large des trois : cinq langages (Python, TypeScript, Go, Java, Kotlin), des adaptateurs pour d'autres modèles que Gemini, y compris locaux, et un déploiement par conteneur autohébergé ou sur Google Cloud (Agent Runtime, Cloud Run, GKE) [10]. Il couvre aussi l'évaluation et l'observabilité.

La version 2.0, annoncée en disponibilité générale pour TypeScript, introduit les **workflows à graphe**, qui mêlent code déterministe et raisonnement adaptatif [10]. Un SDK de fournisseur rejoint ainsi le modèle de la section 20.2. ADK est aussi le seul des trois dont la page lue cite A2A, et il sait exposer un agent comme serveur MCP.

### Claude Agent SDK

Le Claude Agent SDK ne fournit pas des primitives à assembler : il fournit les outils, la boucle d'agent et la gestion du contexte qui animent Claude Code, programmables en Python et en TypeScript [12]. La bibliothèque exécute le binaire Claude Code. L'agent arrive avec la lecture et l'écriture de fichiers, l'exécution de commandes et la recherche web; l'intégrateur règle son comportement par des hooks, des permissions qui distinguent les outils automatiques de ceux qui exigent une approbation, des sous-agents, des Agent Skills et des serveurs MCP.

Avec le Client SDK [12], le développeur écrit lui-même la boucle d'outils. Avec Managed Agents, Anthropic héberge le harnais, les sessions tournant dans un bac à sable géré par l'éditeur ou autohébergé. L'Agent SDK occupe le milieu : le harnais de l'éditeur, dans un processus que l'organisation exploite.

Deux attaches ressortent. L'une est écrite : l'usage est régi par les conditions commerciales d'Anthropic, non par une licence libre, sauf pour les composants qui portent la leur. L'autre se déduit : le harnais est conçu autour d'un modèle, ce qui fait sa qualité et ce qui lie.

### Deux objets sous un même nom

Une distinction pèse plus que le nom du fournisseur. Une **bibliothèque de primitives** laisse l'équipe construire sa boucle et sa topologie. Un **harnais** livre une boucle déjà réglée (planification, compaction du contexte, accès aux fichiers, approbations) et se pilote par configuration. Microsoft offre les deux dans le même cadriciel [6]. Le harnais convient aux tâches longues et ouvertes; il transfère à l'éditeur des décisions d'ingénierie du contexte (chapitre 13).

---

## 20.5 Approches déclaratives : DSPy, MetaGPT

Les cadriciels précédents décrivent comment le travail circule. Deux projets décrivent plutôt ce qui est attendu, et laissent le système en déduire les prompts.

**DSPy** en est la forme la plus aboutie. Né au groupe de traitement du langage de Stanford, il a pour devise de programmer les modèles au lieu de leur écrire des prompts [13]. Une **signature** déclare une tâche par ses entrées et ses sorties typées. Un **module** fixe la stratégie d'exécution de la signature : prédiction directe, raisonnement en chaîne, boucle ReAct. Un **optimiseur** ajuste le programme à partir d'exemples et d'une fonction de score; la documentation en nomme plusieurs, dont GEPA et MIPROv2.

L'intérêt pour ce chapitre est la portabilité. Un prompt rédigé à la main est réglé pour un modèle; une signature ne l'est pas, et l'optimiseur peut refaire le réglage pour un autre. La page cite un cas de migration de prompts d'un grand modèle vers un plus petit [13]. La condition est sévère : il faut des exemples et une métrique, donc une évaluation outillée (chapitre 33); le chapitre 47 décrit MIPROv2 et la boucle de données qui l'alimente. DSPy n'est pas un orchestrateur; il se loge à l'intérieur des nœuds d'un graphe.

**MetaGPT** déclare autre chose : la procédure. Ses auteurs partent d'un constat, les incohérences logiques dues aux hallucinations en cascade quand on enchaîne naïvement des modèles, et y répondent en encodant des procédures opérationnelles normalisées dans des séquences de prompts [14]. Les agents reçoivent des rôles selon un paradigme de chaîne de montage et vérifient les résultats intermédiaires. Le résumé annonce des solutions plus cohérentes que les systèmes multi-agents antérieurs en génie logiciel, sans chiffre.

L'idée centrale dépasse le projet : une procédure écrite, avec des livrables intermédiaires vérifiables, discipline mieux une équipe d'agents qu'une conversation libre. Le chapitre 21 en montre le prix : face à ChatDev, MetaGPT réduit de 60 % à 68 % les défauts de spécification et de coordination, mais compte 1,56 fois plus d'échecs de vérification. La procédure ne dispense pas d'un vérificateur.

---

## 20.6 Les protocoles comme assurance de portabilité

### Ce que les protocoles rendent portable

Deux frontières sont désormais standardisées. Un outil exposé par MCP est utilisable par tout cadriciel qui possède un client MCP : c'est le cas de Microsoft Agent Framework, de l'OpenAI Agents SDK, d'ADK et du Claude Agent SDK, d'après leurs propres pages [6][9][10][12]. LangChain et CrewAI en fournissent un aussi, limité aux outils dans les pages lues [16][18]. Un agent exposé par A2A est appelable par un agent bâti autrement : CrewAI, Microsoft Agent Framework et ADK documentent les deux rôles, client et serveur [5][8][11]. Les protocoles eux-mêmes sont décrits aux chapitres 5 et 6.

D'autres actifs se transportent aussi : les Agent Skills, que lisent ADK et le Claude Agent SDK [10][12], dont le format voyage, mais non le comportement (chapitre 13); et les traces, si elles suivent OpenTelemetry (chapitre 33).

### Ce qu'ils ne rendent pas portable

Tout ce qui vit à l'intérieur du cadriciel lui reste propre : définition du graphe, schéma d'état, format des points de contrôle, prompts réglés pour un modèle, mécanismes d'approbation. Changer de cadriciel, c'est réécrire cela.

### Où placer la frontière

La documentation d'ADK donne la règle la plus utile [11]. Des sous-agents locaux tournent dans le même processus et se comportent comme des modules internes : ils conviennent à l'organisation du code, aux opérations sensibles à la performance et au partage de contexte. Un agent distant, joint par A2A, est un service séparé : il convient quand l'agent appartient à une autre équipe ou à une autre organisation, quand il est écrit dans un autre langage ou un autre cadriciel, ou quand il faut un contrat formel entre composants.

À l'intérieur d'une équipe, le cadriciel peut rester un choix local. Entre équipes, la frontière passe par A2A; vers les systèmes, par MCP. Un workflow entier, exposé comme agent [7] puis publié par A2A [8], devient un composant remplaçable : son cadriciel n'est plus visible de ses appelants.

### Les réserves

**Les versions divergent.** La documentation de CrewAI donne 0.3.0 comme version de protocole par défaut de son serveur A2A [5]. Les exemples de Microsoft publient des cartes d'agent en version 1.0 et exigent la version 1 du SDK A2A [8]. Or la version 1.0 rompt avec la 0.3 (chapitre 6). Deux cadriciels qui « parlent A2A » ne s'entendent donc pas forcément sans réglage. Certains produits font le pont : Agent Server sert la version 1.0 tout en acceptant les noms de méthode de la 0.3 [17].

**Le contrat reste lâche.** CrewAI permet de demander un format de réponse à un agent distant, puis précise qu'A2A ne l'impose pas : l'agent appelé n'est pas tenu de l'honorer [5]. La validation des sorties reste à la charge de l'appelant.

**Le protocole ne livre pas le service.** Chez Microsoft, l'adaptateur Python traduit l'agent en événements A2A, mais l'application assemble le reste : carte d'agent, magasin de tâches, routes, authentification, déploiement. La page avertit aussi que les métadonnées transmises ne constituent pas une frontière d'authentification [8]. CrewAI renvoie les besoins de production (état distribué, authentification d'entreprise, mise à l'échelle) vers sa plateforme commerciale, AMP [5].

**La délégation devient un choix du modèle.** Dans CrewAI, l'agent analyse chaque tâche et décide de la traiter lui-même ou de la confier à un agent distant [5]. Le routage entre organisations hérite alors du non-déterminisme du modèle; une politique explicite est préférable pour les actions sensibles (chapitre 22) et pour les échanges entre entreprises (chapitre 45).

Le verrouillage se déplace donc plus qu'il ne disparaît. Il quitte la bibliothèque, souvent libre, pour l'environnement d'exécution géré, l'outillage d'observabilité et la plateforme (chapitres 26 et 27).

---

## 20.7 Grille de sélection

« Non lue » signale un point que les pages lues ne traitent pas.

| Cadriciel | Unité de composition | État et reprise | Attaches relevées |
|---|---|---|---|
| LangGraph [1][2][3] | Graphe : état typé, nœuds, arêtes | Points de contrôle par fil; magasin à choisir | Bibliothèque autonome sous licence MIT; déploiement géré et A2A dans un produit distinct |
| CrewAI [4][5] | Flow qui enveloppe des Crews | État de Flow persistant | Licence MIT; production A2A renvoyée à la plateforme commerciale AMP |
| Microsoft Agent Framework [6][7][8] | Agent, harnais, workflow à graphe | Sessions; points de contrôle par super-étape; extension durable | Multi-modèles; licence MIT; paquets en préversion selon le langage |
| OpenAI Agents SDK [9] | Agent, transfert, garde-fou | Sessions; bac à sable reprenable | Pente vers l'API et le traçage de l'éditeur |
| Google ADK [10][11] | Agents, workflows gabarits et à graphe | Sessions, état, mémoire; reprise non lue | Multi-modèles; déploiement libre ou Google Cloud |
| Claude Agent SDK [12] | Harnais, sous-agents, hooks | Sessions à reprendre ou dupliquer | Binaire Claude Code; conditions commerciales |
| DSPy [13] | Signature, module, optimiseur | Hors sujet : couche de prompt | Python; exige exemples et métrique |

Quatre questions, dans cet ordre, suffisent à réduire la liste.

1. **La tâche a-t-elle besoin d'un agent ?** Si une fonction suffit, la question du cadriciel ne se pose pas [6]. Si un seul agent suffit, un SDK léger ou un harnais convient (chapitre 16).
2. **Le chemin est-il connu d'avance ?** Si oui, un workflow à graphe ou un moteur de processus (chapitre 17). Si non, un harnais, borné par des permissions.
3. **Que coûte une interruption ?** Une tâche de quelques secondes se relance. Une tâche de plusieurs heures, ou à effets irréversibles, exige des points de contrôle en base de données, voire un moteur d'exécution durable (chapitre 18).
4. **Quelles attaches l'organisation accepte-t-elle ?** Modèle unique ou non, runtime exploité en interne ou géré, licence. C'est ici, et non sur les fonctionnalités, que les produits diffèrent le plus.

### Ce que disent les études de défauts

Deux études empiriques éclairent la fragilité de cette couche. La première analyse 409 bogues corrigés dans cinq cadriciels : LangChain, LangGraph, CrewAI, AutoGen et SmolAgents [20]. Plus de la moitié (52 %) sont des fautes de programmation ordinaires, 22 % des fautes propres aux agents, surtout liées au modèle, et 12 % des fautes de documentation, le plus souvent un exemple de code erroné. La couche qui intègre le modèle est la plus touchée (24,7 % des bogues), et moins de la moitié de ses correctifs sont accompagnés d'un test. Les conditions de déclenchement tiennent à la configuration dans 92 % des cas analysés, d'abord aux réglages du modèle. Enfin, 16 des 35 bogues rejoués se transposent à un autre cadriciel. Les auteurs ne classent pas les produits : leurs décomptes portent sur des bogues corrigés, non sur des taux de défaut.

La seconde, connue par son résumé, porte sur 5 669 rapports de bogue et 809 demandes de fonction dans cinq cadriciels. Selon sa propre classification, 76 % des bogues se manifestent par un comportement fonctionnel incorrect, et leurs causes relèvent davantage des API, de la configuration, de l'analyse et de la sérialisation que dans les cadriciels d'apprentissage profond [21].

Trois précautions en découlent, déduites ici : essayer la combinaison exacte de fournisseur et de modèle employée, plutôt que de se fier à la prise en charge annoncée; vérifier qu'un réglage est bien appliqué; ne pas tenir un exemple de documentation pour valide dans la version installée. La parenté des défauts d'un cadriciel à l'autre va dans le sens de la thèse du chapitre : le choix du produit pèse moins que la discipline d'essai (chapitre 34).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Faut-il un cadriciel ? | Non, tant qu'une fonction ou un appel de modèle avec outils suffit | Boucle, état ou coordination à maintenir |
| Processus aux étapes connues | Workflow à graphe, non-déterminisme confiné aux nœuds | Processus déjà modélisé en BPMN : moteur de processus (chapitre 17) |
| Tâche longue et ouverte | Harnais, avec permissions et hooks | Besoin de maîtriser chaque appel : bibliothèque de primitives |
| Persistance | Points de contrôle en base de données dès le pilote | Durée de plusieurs heures ou effets irréversibles : exécution durable (chapitre 18) |
| Outils | Exposés par MCP, jamais comme fonctions propres au cadriciel | Fonction purement interne à un agent |
| Frontière entre équipes | A2A, version de protocole fixée et testée | Même équipe, même processus : sous-agents locaux |
| Modèle | Cadriciel multi-modèles, condition du routage (chapitre 44) et d'un modèle de secours (chapitre 46) | Harnais lié à un modèle, si le gain est mesuré et la sortie prévue |
| Prompts | Rédigés et versionnés | Jeu d'exemples et métrique disponibles : signatures optimisées |
| Environnement d'exécution | Exploité par l'organisation | Runtime géré, si l'état reste exportable |

---

## Points à retenir

- Les cadriciels convergent vers deux étages : une boucle d'agent et un workflow explicite. CrewAI recommande de commencer par un Flow; ADK 2.0 ajoute des graphes; Microsoft réunit agents, harnais et workflows.
- Le cadriciel est la couche la plus périssable. AutoGen, Semantic Kernel, Swarm et le Claude Code SDK ont tous un successeur; il faut budgéter une migration.
- La règle de Microsoft vaut partout : si une fonction peut faire le travail, il ne faut pas d'agent.
- « SDK » recouvre deux objets : une bibliothèque de primitives ou un harnais déjà réglé. Le second accélère et lie davantage.
- La portabilité se gagne aux frontières : MCP pour les outils, A2A entre équipes. L'intérieur du cadriciel (graphe, état, points de contrôle) n'est pas portable.
- « Compatible A2A » ne suffit pas : CrewAI sert la version 0.3.0 par défaut, Microsoft la 1.0, et l'authentification, le magasin de tâches et la mise à l'échelle restent à construire.
- Une procédure écrite réduit les défauts de spécification et de coordination, mais laisse paraître plus d'échecs de vérification.
- Le verrouillage se déplace de la bibliothèque vers le runtime géré, l'observabilité et la plateforme.
- Aucun chiffre comparatif de coût en jetons n'a été lu; le critère vérifiable est la maîtrise du contexte envoyé au modèle.
- Les études de défauts montrent des bogues surtout ordinaires, concentrés dans l'intégration du modèle et souvent transposables d'un cadriciel à l'autre : la discipline d'essai compte plus que le produit.

---

## Sources

Pages primaires lues le 11 novembre 2026; [2], [5], [6], [8], [9], [10], [12] et [13] relues le 12 novembre 2026 :

1. [LangGraph — vue d'ensemble](https://docs.langchain.com/oss/python/langgraph/overview)
2. [LangGraph — Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)
3. [LangGraph — persistance](https://docs.langchain.com/oss/python/langgraph/durable-execution) (l'adresse sert la page sur la persistance)
4. [CrewAI — introduction](https://docs.crewai.com/en/introduction)
5. [CrewAI — délégation d'agents par A2A](https://docs.crewai.com/en/learn/a2a-agent-delegation)
6. [Microsoft Agent Framework — vue d'ensemble](https://learn.microsoft.com/en-us/agent-framework/overview/) (page datée du 23 octobre 2026)
7. [Microsoft Agent Framework — concepts de workflow](https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/) (22 octobre 2026)
8. [Microsoft Agent Framework — héberger des agents avec A2A](https://learn.microsoft.com/en-us/agent-framework/hosting/self-hosting/a2a/server) (23 octobre 2026)
9. [OpenAI Agents SDK — documentation Python](https://openai.github.io/openai-agents-python/)
10. [Agent Development Kit — accueil](https://adk.dev/)
11. [Agent Development Kit — introduction à A2A](https://adk.dev/a2a/intro/)
12. [Claude Agent SDK — vue d'ensemble](https://code.claude.com/docs/en/agent-sdk/overview)
13. [DSPy — accueil](https://dspy.ai/)
14. [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework (arXiv 2308.00352)](https://arxiv.org/abs/2308.00352) — résumé seulement

Source secondaire :

15. [Zhu et coll. — LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns](https://www.preprints.org/manuscript/202604.2147) — prépublication non lue (accès refusé), citée comme appui par le plan initial.

Sources ajoutées le 14 novembre 2026 :

16. [LangChain — MCP](https://docs.langchain.com/oss/python/langchain/mcp)
17. [LangSmith — point d'accès A2A d'Agent Server](https://docs.langchain.com/langsmith/server-a2a)
18. [CrewAI — MCP, vue d'ensemble](https://docs.crewai.com/en/mcp/overview)
19. Dépôts de [LangGraph](https://github.com/langchain-ai/langgraph), de [CrewAI](https://github.com/crewAIInc/crewAI) et de [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — licence indiquée sur la page d'accueil.
20. [Zhang, Zhang et Tan — Dissecting Bug Triggers and Failure Modes in Modern Agentic Frameworks: An Empirical Study (arXiv 2604.08906, 10 avril 2026)](https://arxiv.org/html/2604.08906v1) — prépublication.
21. [Zhu et coll. — Where Agent Frameworks Fall Short: Examining Functional Challenges and Usability Concerns (arXiv 2602.21806, version 4 du 6 août 2026)](https://arxiv.org/abs/2602.21806) — prépublication; résumé seulement.

## Limites de ce chapitre

- Le relevé [15], appui prévu par le plan initial, n'a pas été lu, et sa parution dans *Future Internet* n'a pas été confirmée. Sa comparaison des cadriciels n'est donc pas reprise, et rien n'établit que les quatre critères de la section 20.1 en proviennent.
- La plupart des pages ont été lues par un outil d'extraction qui en restitue le contenu en condensé; les pages de Microsoft et d'Anthropic l'ont été en texte intégral. La version A2A par défaut de CrewAI et la limite de récursion de LangGraph, à revérifier, ont été confirmées à la relecture.
- La page d'accueil d'ADK n'annonce la version 2.0 en disponibilité générale que pour TypeScript; le statut des autres langages n'a pas été lu.
- Une à quatre pages par produit ont été lues; restent non décrits la reprise sur échec dans ADK et dans l'OpenAI Agents SDK, et les modèles acceptés par le Claude Agent SDK. La prise en charge de MCP par LangChain et par CrewAI, celle d'A2A par Agent Server et les licences de LangGraph, de CrewAI et de Microsoft Agent Framework ont été lues le 14 novembre 2026, de [16] à [19]; les licences viennent de la page d'accueil des dépôts, non du texte des licences.
- Aucun chiffre de coût en jetons ni d'adoption n'est cité, faute de source lue; le raisonnement de la section 20.1 sur le coût des abstractions est une analyse. Les seuls chiffres de performance, sur MetaGPT et ChatDev, sont repris du chapitre 21 sans relecture de MAST.
- La convergence des cadriciels, le déplacement du verrouillage et la distinction entre bibliothèque et harnais sont des synthèses de ce chapitre, non des thèses lues dans une source.
- MetaGPT n'est connu que par le résumé de son article; son rangement parmi les approches « déclaratives » suit le plan initial et convient mieux à DSPy.
- La sous-section sur les études de défauts (20.7) date du 14 novembre 2026. [21] n'est connue que par son résumé, et ses versions antérieures portaient un autre titre et un échantillon plus petit. Les trois précautions sont des déductions de ce chapitre; [20] ne classe pas les cadriciels.
- Un critère (« attaches ») a été ajouté aux quatre du plan initial.
