# Chapitre 7 — Patrons d’orchestration et topologies de composition multi-agents

Avec l’outillage vertical normalisé par `MCP` (chapitre 4), la délégation horizontale sur `A2A` et `AGNTCY` (chapitre 5) et la souveraineté mémorielle établie autour des quatre strates cognitives (chapitre 6), la tentation immédiate consiste à multiplier les agents spécialisés dès qu’un processus métier dépasse quelques étapes. Les retours en production et les travaux empiriques récents démontrent toutefois qu’une décomposition multi-agents appliquée sans discipline dégrade simultanément la fiabilité, la latence et l’économie unitaire [123] [124] [125]. Ce chapitre ouvre la Partie III en établissant les critères quantitatifs et les patrons algorithmiques de composition coordonnée par graphe ou par superviseur. Il porte exclusivement sur l’orchestration structurée à flux explicite; le couplage événementiel asynchrone via `Event Mesh` relève du chapitre 8, et la reprise transactionnelle par exécution durable et `Sagas` est traitée au chapitre 9.

Pour l’architecte de solutions (`SA`), l’enjeu consiste à aligner strictement la structure des dépendances d’une tâche, la topologie d’exécution (`Séquentiel`, `Routeur`, `Supervisor`, `DAG`, `Handoff`, `Scatter-Gather` ou `Generator-Verifier`) et l’ingénierie des transferts d’état. Pour l’architecte d’entreprise (`EA`), l’enjeu consiste à contenir l’amplification des coûts d’inférence et des erreurs tout en imposant des bornes d’arrêt déterministes protégeant les `Systems of Record (SoR)`.

## 7.1 Quand éviter le multi-agents : critères quantitatifs face à un agent unique outillé

L’adoption d’une topologie multi-agents obéit souvent à une analogie organisationnelle : puisqu’une équipe humaine divise un dossier entre analyste, rédacteur et relecteur, plusieurs agents devraient surpasser un agent unique. Les évaluations contrôlées invalident cette intuition et montrent que la distribution cognitive n’est rentable que dans des régimes structurels précis [126] [124].

### 7.1.1 Le paradoxe de la décomposition naïve : lois d’échelle empiriques et saturation à 45 %

Dans une étude évaluant 260 configurations sur six bancs d’essai agentiques, trois familles de modèles et cinq architectures canoniques (agent unique, multi-agents indépendant, centralisé, décentralisé et hybride), Kim et ses coauteurs montrent que la performance dépend avant tout de l’adéquation entre topologie et structure de tâche [124]. Leur modèle prédictif sélectionne l’architecture optimale pour 87 % des configurations hors échantillon (`R² = 0,373`, et `R² = 0,413` avec une métrique de capacité ancrée sur la tâche) et met en évidence trois lois quantitatives [124] :

1. **Seuil de saturation à 45 %** : dès qu’un agent unique outillé dépasse 45 % d’exactitude sur une classe de tâches, l’ajout d’agents supplémentaires produit des rendements décroissants ou négatifs, le surcoût de coordination excédant le gain marginal [124].
2. **Divergence selon la parallélisabilité** : comparé à l’agent unique, le multi-agents génère jusqu’à +80,8 % de gain relatif sur le raisonnement financier décomposable en branches indépendantes, mais subit une dégradation de −70,0 % sur la planification séquentielle rigide [124].
3. **Amplification asymétrique des erreurs** : les architectures indépendantes dépourvues de validation centralisée amplifient les erreurs d’un facteur 17,2× face à l’agent unique, alors qu’une coordination centralisée contenant la revue des sous-agents ramène cette amplification à 4,4× [124].

Les données de production d’Anthropic confirment ces ordres de grandeur économiques : un agent unique consomme déjà environ 4× plus de jetons qu’une interaction conversationnelle simple, tandis qu’un système multi-agents en consomme environ 15× plus [127]. Sur le banc *BrowseComp*, trois facteurs expliquent 95 % de la variance de performance, la seule consommation de jetons en expliquant 80 % devant le nombre d’appels d’outils et le choix du modèle [127]. Sur des tâches de faible valeur unitaire ou déjà traitées par un agent unique outillé, le multi-agents détruit donc la marge `FinOps` sans gain qualitatif [126] [127].

### 7.1.2 Fragmentation du contexte et décisions implicites : la leçon de Cognition et la taxonomie MAST

L’éclatement prématuré engendre également des pannes distribuées cognitives. Analysant les défaillances des systèmes multi-agents autonomes, Walden Yan (Cognition) pose deux principes directeurs d’ingénierie du contexte [123]. Premièrement, **partager les traces complètes de décision plutôt que des messages isolés** : lorsqu’un coordinateur ne transmet à un sous-agent qu’une sous-consigne résumée, ce dernier interprète sa tâche hors contexte et produit des résultats incompatibles avec les hypothèses des tours précédents [123]. Deuxièmement, **toute action porte des décisions implicites** : dès que des écrivains concurrents modifient en parallèle un même livrable (code, contrat ou modèle), leurs choix implicites non partagés entrent en collision [123]. Cognition préconise par conséquent une exécution mono-fil disciplinée sur une trace continue plutôt que des essaims d’écrivains parallèles [123], la parallélisation multi-agents ne demeurant sûre que sur des explorations en lecture seule isolées [127] [124].

La taxonomie empirique `MAST` (*Multi-Agent System Failure Taxonomy*), construite à l’UC Berkeley sur plus de 1 600 traces annotées issues de sept cadriciels (`κ = 0,88`), recense 14 modes de défaillance regroupés en trois catégories équilibrées [125] :

- **Spécification et conception système (**`FC1` **: 41,77 %)** : désobéissance aux consignes initiales ou au rôle, répétition d’étapes, perte d’historique et ignorance des conditions d’arrêt [125].
- **Désalignement inter-agents (**`FC2` **: 36,94 %)** : réinitialisation de conversation, absence de demande de clarification, déraillement thématique, rétention d’information critique, rejet des retours d’un pair et divergence entre raisonnement exprimé et action exécutée [125].
- **Vérification et terminaison (**`FC3` **: 21,30 %)** : arrêt prématuré sur résultat incomplet, absence de contrôle et validation erronée [125].

Au total, 78,71 % des défaillances (`FC1 + FC2`) proviennent directement de l’architecture du graphe de coordination et des échanges de contexte, et non des limites brutes du modèle [125].

### 7.1.3 Alternatives avant l’éclatement : Skills à divulgation progressive et découplage ReWOO

Avant d’instancier plusieurs agents, le `SA` dispose de trois leviers dans un `Agent Harness` unitaire (chapitre 3) pour étendre la portée d’un agent unique [126] [128] [129] :

1. **Divulgation progressive par** `Skills` : au lieu de saturer le contexte initial avec des dizaines de procédures et schémas d’outils, un agent unique charge dynamiquement à la demande les compétences requises, protégeant ainsi son budget d’attention sans introduire de coordination inter-agents [129].
2. **Découplage plan-observation (**`ReWOO`**)** : les boucles `ReAct` entrelacent chaque raisonnement avec une observation d’outil complète [130]. Le paradigme `ReWOO` (*Reasoning WithOut Observation*) sépare un *Planner* produisant le graphe d’appels via des variables symboliques (`#E1`, `#E2`), un *Worker* exécutant les outils et un *Solver* synthétisant la réponse [130]. Cette séparation offre une efficacité en jetons 5× supérieure et un gain d’exactitude de 4 % sur *HotpotQA*, tout en permettant de déporter la planification vers des modèles plus compacts (de 175B vers 7B paramètres) [130].

3. **Workflow déterministe ponctué de nœuds** `LLM` : selon la règle 80/20 (chapitre 3), tout enchaînement connu à l’avance doit rester dans du code déterministe orchestrant des appels cognitifs unitaires sans boucle autonome [126] [128].

> **[Figure]**
> - Anti-patron : fragmentation prématurée (tâche séquentielle / > 45
> - % base)
> - Arbitrage cible : escalade graduée
> - (agent unique outillé →graphe
> - gouverné)
> - Requête complexe
> - Essaim parallèle sans vérification
> - Contexte fragmenté & choix implicites en conflit
> - Amplification 17,2x et coût ~15x jetons
> - Requête & profil de tâche
> - Agent unique outillé (Skills / ReWOO)
> - Graphe dirigé borné (Supervisor / DAG)
> - Endiguement 4,4x et budget maîtrisé
> - Éclatement naïf
> - Écritures concurrentes
> - sans trace commune
> - Dérive MAST FC1/FC2
> - (-70 % en séquentiel)
> - Règle par défaut (base >= 45 % ou séquentiel)
> - Escalade si contexte saturé
> - ou sous-tâches parallèles
> - Validation centralisée et passage par référence

*Fig. 25. – Arbitrage architectural entre fragmentation prématurée et escalade graduée depuis l’agent unique outillé*

Le passage au multi-agents ne devient justifié que si l’une au moins de quatre contraintes objectives s’impose [127] [124] [129] : l’exploration parallèle de branches indépendantes en lecture dont les résultats bruts satureraient un contexte unique [127] [129]; le cloisonnement de sécurité interdisant de réunir deux jeux d’outils ou de données sensibles dans une même fenêtre [129]; l’autonomie de développement entre équipes maintenant des domaines distincts [129]; ou une séparation contradictoire générateur-vérificateur sur des livrables critiques [126] [128].

| Critère d’évaluation | Agent unique outillé (`Skills` / `ReWOO`) | Multi-agents centralisé (`Supervisor` / `DAG`) | Multi-agents décentralisé / indépendant |
| --- | --- | --- | --- |
| Exactitude base mono-agent | ≥ 45 % sur tâche structurée [124] | < 45 % sur tâche décomposable [124] | Exceptions rares (exploration pure) [127] |
| Structure des dépendances | Séquentielle ou outil-intensive [124] | Parallélisable avec jointure vérifiée [124] | Sous-tâches disjointes en lecture [127] [124] |
| Amplification des erreurs | 1,0× (référence) [124] | 4,4× (endiguement centralisé) [124] | 17,2× (propagation non vérifiée) [124] |
| Coût en jetons | ~4× vs conversation [127] (5× réduit via `ReWOO` [130]) | ~15× vs conversation simple [127] | Non borné sans plafond explicite [125] |
| Écritures mutantes | Mono-fil cohérent (zéro conflit) [123] | Écritures sérialisées au coordinateur [123] | Conflits d’hypothèses implicites (`FC2`) [123] [125] |

*Tableau 7.1 — Critères quantitatifs de décision entre agent unique outillé et architectures multi-agents.*

> **Arbitrage EA / SA** — Exiger en revue d’architecture la preuve qu’un agent unique outillé (`Skills`, `ReWOO` ou workflow déterministe à nœuds `LLM`) ne suffit pas avant d’autoriser une topologie multi-agents, particulièrement lorsque la tâche est séquentielle ou dépasse 45 % de base [126] [124] [129] [130]. Le `SA` privilégie l’isolation de lecture en parallèle et sérialise toute mutation d’état; l’`EA` valide le multiplicateur `FinOps` (~15×) et rejette toute topologie décentralisée sans vérification centralisée [127] [123] [124].

## 7.2 Topologies dirigées : séquentiel typé, routeur sémantique, Supervisor et planification DAG

Lorsque le recours au multi-agents est justifié, la première famille d’architectures regroupe les **topologies dirigées**, où les transitions demeurent gouvernées par un graphe explicite ou un coordonnateur hiérarchique [126] [128] [131]. Ce contrôle structurel réduit directement les défaillances `FC1` et `FC2` de la taxonomie `MAST` [125].

### 7.2.1 Pipeline séquentiel typé et portes de validation déterministes

Le patron **séquentiel typé** (*Prompt Chaining* ou *Sequential Orchestration*) enchaîne des agents spécialisés dans un ordre linéaire prédéfini où la sortie validée du nœud `k` alimente le nœud `k + 1` [126] [128] [131] [132]. Chaque nœud reçoit un mandat étroit (extraction documentaire, qualification réglementaire, calcul, rédaction) et un contexte épuré des traces intermédiaires inutiles [126] [131].

En entreprise, la fiabilité de cette chaîne repose sur l’insertion de **portes de validation programmatiques** (*gates*) sur les arêtes d’un graphe d’état typé (`StateGraph` sous LangGraph ou `Workflow` sous Google ADK 2.0) [126] [133] [134]. Avant d’activer l’étape suivante, le moteur contrôle déterministiquement le schéma `JSON` (chapitre 3), la complétude des champs et les invariants métier [126] [133]. En cas d’échec, une arête conditionnelle déclenche une reprise locale bornée ou une escalade humaine [133] [134]. Ce patron convient aux processus structurés à ordre fixe; il devient contre-productif dès que des branches indépendantes pourraient tourner en parallèle ou que l’ordonnancement dépend de découvertes en cours d’exécution [131].

### 7.2.2 Routeur sémantique et aiguillage spécialisé

Le patron **Routeur sémantique** (*Routing*) place en entrée un classificateur — ou un petit modèle spécialisé — chargé d’analyser la demande et de l’aiguiller vers l’une de plusieurs branches spécialisées mutuellement exclusives [126] [129]. Chaque branche conserve ses propres directives, exemples et outils `MCP`, évitant que l’optimisation d’un domaine (facturation, conformité) ne dégrade un autre domaine (support technique) [126].

Contrairement au patron `Handoff`, le routeur exécute un aiguillage en une passe (*single-step dispatch*) ou en éventail ciblé sans maintenir de conversation continue entre l’aiguilleur et les spécialistes [129]. Le `SA` doit compléter tout routeur par une **arête de repli déterministe** sous seuil de confiance minimal et par un filtrage d’entrées empêchant qu’une injection utilisateur ne détourne l’aiguillage vers une branche privilégiée (`ASI01` [135]).

### 7.2.3 Topologie Supervisor et patron Subagents-as-Tools

Dans la topologie **Supervisor** (*Orchestrator-Workers* chez Anthropic ou *Magentic* dans le Microsoft Agent Framework), un coordonnateur central décompose dynamiquement la tâche, délègue des sous-mandats à des travailleurs spécialisés et synthétise le résultat [126] [131] [132] [133]. C’est cette architecture

— un agent `Claude Opus 4` orchestrant des sous-agents `Claude Sonnet 4` en parallèle — qui a permis à Anthropic de surclasser de 90,2 % l’agent unique `Claude Opus 4` sur son banc de recherche interne [127].

Les cadriciels modernes convergent vers l’implémentation **Subagents-as-Tools** plutôt que vers le partage d’une file de messages brute entre pairs [133] [136]. Le superviseur invoque chaque sous-agent spécialisé comme un outil sans état [136], ce qui procure deux bénéfices majeurs :

- **Isolation stricte du contexte** : chaque sous-agent explore et compresse ses lectures dans sa propre fenêtre éphémère avant de retourner au superviseur une synthèse concise, protégeant ce dernier contre le *context rot* [127] [136] [137].
- **Endiguement centralisé des erreurs** : chaque retour transitant par le coordonnateur avant décision aval, l’amplification d’erreurs reste contenue autour du facteur 4,4× au lieu de dériver vers 17,2× [124].

Deux risques demeurent toutefois : la latence devient séquentielle si le superviseur lance les sous-agents un à un, et une délégation mal cadrée provoque une sur-consommation de jetons (`MAST FC1`) [127] [125]. Anthropic préconise ainsi des règles explicites de calibrage d’effort dans les consignes du superviseur afin de proportionner le nombre de sous-agents et d’appels d’outils à la difficulté réelle de la demande [127].

### 7.2.4 Planification par graphe acyclique dirigé (DAG) : LLMCompiler et ADK Graph Workflows

Lorsque les opérations présentent des dépendances mixtes, l’orchestration `Supervisor` tour-par-tour paie inutilement un cycle complet d’inférence du coordonnateur entre chaque appel [138]. La **planification par graphe acyclique dirigé (**`DAG`**)** applique l’ordonnancement des compilateurs aux appels cognitifs et outillés [138] [134].

L’architecture `LLMCompiler` repose sur trois composants [138] :

1. **Function Calling Planner** : produit en amont le graphe complet de dépendances entre tâches indépendantes et tâches liées par variables symboliques [138].
2. **Task Fetching Unit** : résout les dépendances en flux tendu dès qu’une tâche amont s’achève et libère les appels devenus prêts [138].
3. **Executor** : exécute concurremment l’ensemble des tâches débloquées [138].

Sur les bancs multi-fonctions, `LLMCompiler` obtient jusqu’à **3,7×** d’accélération en latence, **6,7×** d’économies de coût et environ **9 %** de gain d’exactitude par rapport à `ReAct` [138]. Cette approche rejoint l’évolution d’ADK 2.0 vers des graphes de workflow généraux unifiant nœuds cognitifs, nœuds de code déterministes, `JoinNode`, délais d’expiration et tentatives bornées [134].

> **[Figure]**
> - Topologie 1 : Supervisor /
> - Subagents-as-Tools
> - [container]
> - Topologie 2 : Planification
> - DAG dynamique (LLMCompiler / ReWOO)
> - [container]
> - «component» Agent Supervisor
> - [LLM frontière]
> - Décompose, route
> - et consolide
> - «component» Sous-agent A
> - [Contexte isolé]
> - Exécution outillée (retour synthétisé)
> - «component» Sous-agent B
> - [Contexte isolé]
> - Exécution outillée (retour synthétisé)
> - «component» Planner DAG [Graphe + #E1..#En]
> - Produit le graphe
> - de dépendances
> - «component» Task Fetching Unit
> - [Ordonnanceur]
> - Résout variables et déclenche dès prêt
> - «component» Parallel Executors
> - [Pool asynchrone]
> - Exécute les nœuds
> - indépendants
> - «component» JoinNode / Solver
> - [Synthèse bornée]
> - Agrège les sorties
> - et valide l'état
> - Invoque comme outil
> - Invoque comme outil
> - Émet DAG typé Dispatche en parallèle Transmet #E1..#En

*Fig. 26. – Comparaison entre topologie Supervisor à sous-agents outillés et planification dynamique par graphe DAG*

L’arbitrage entre `Supervisor` et `DAG` dépend de la prévisibilité du graphe d’exécution : un `DAG` compilé (`LLMCompiler` ou `ReWOO`) prime lorsque les dépendances sont formulables a priori [138] [130]; un `Supervisor` reste indispensable lorsque les découvertes d’une première étape remettent en cause l’ensemble de la stratégie aval [127] [138].

> **Arbitrage EA / SA** — Imposer les graphes dirigés explicites (séquentiel à portes typées, routeur à repli déterministe, `DAG` compilé) partout où la topologie de dépendances est prévisible, et confiner le `Supervisor` aux investigations ouvertes à forte valeur [126] [131] [138]. Le `SA` encapsule les travailleurs en `Subagents-as-Tools` et borne la profondeur de récursion [133] [136]; l’`EA` exige la séparation lisible en audit entre arêtes contractuelles déterministes et routages cognitifs ainsi que des règles de calibrage d’effort [127] [134].

## 7.3 Topologies collaboratives et vérificatrices : Handoff, Scatter-Gather et boucle Generator-Verifier

Certains scénarios exigent de céder l’interaction directe à un spécialiste de domaine, de paralléliser une évaluation multi-angles ou d’instaurer une relecture contradictoire avant toute décision [126] [131] [139]. Sans verrous structurels, ces topologies deviennent toutefois le terrain privilégié des boucles infinies et des validations complaisantes (`MAST FC1` et `FC3`) [125].

### 7.3.1 Délégation directe orientée conversation : le patron Handoff

Le patron **Handoff** transfère activement le contrôle de la session d’un agent à un autre spécialiste sans repasser par un superviseur central à chaque tour [131] [132] [139] [140]. Dans le SDK d’OpenAI Agents, ce transfert prend la forme d’un outil typé (`transfer_to_<agent_name>`) paramétré par `input_type` (schéma des métadonnées de transfert), `on_handoff` (rappel déterministe de journalisation ou de chargement préalable) et `input_filter` (filtrage sur `HandoffInputData`) [140]. Dans LangGraph, le transfert met à jour une variable d’état persistante (`active_agent` ou `current_step`) qui permute dynamiquement le prompt système et les outils disponibles [139].

Face au patron `Subagents`, le `Handoff` offre deux propriétés distinctives [129] [139] : il préserve le **dialogue direct** entre l’agent spécialisé actif et l’utilisateur ou le `SoE` (évitant la latence et la perte de nuance d’un superviseur-relais), et permet un **verrouillage séquentiel de conformité** en n’exposant un outil ou spécialiste aval qu’une fois validées les conditions d’étape amont [129] [139]. En contrepartie, le `SA` doit borner les transitions autorisées pour prévenir les renvois circulaires (*ping-pong* `MAST FC1`) [125] et appliquer un `input_filter` strict afin de ne pas polluer l’agent cible avec un historique brut superflu [140].

### 7.3.2 Parallélisation en éventail : Scatter-Gather, Sectioning et Voting

Hérité des *Enterprise Integration Patterns* de Hohpe et Woolf, le patron **Scatter-Gather** diffuse une requête en parallèle vers plusieurs destinataires (*Scatter*) puis corrèle et fusionne leurs retours dans un *Aggregator* avec état muni d’un identifiant de corrélation (*Gather*) [141]. En orchestration agentique (`Concurrent Orchestration` chez Microsoft [131] [132], `Parallelization` chez Anthropic [126], `ParallelAgent` /`JoinNode` sous ADK [134]), il se décline en **Sectioning** (décomposer un dossier en facettes indépendantes analysées concurremment) et en **Voting** (soumettre un même cas à plusieurs prompts ou modèles indépendants pour arbitrer par vote ou score) [126].

Le `SA` doit y maîtriser deux contraintes d’ingénierie [131] [134] [141] :

1. **Latence de queue et politique de quorum** : attendre la totalité des `N` branches aligne le temps de réponse sur la branche la plus lente `max(T₁, ..., Tₙ)`, amplifiant la latence `p99` du chapitre 1. L’agrégateur doit donc combiner un `timeout SLA` strict et une condition de complétude explicite (quorum minimal ou repli dégradé documenté) [134] [141].
2. **Discipline d’agrégation** : fusionner des synthèses contradictoires par un appel cognitif non cadré peut dégrader la précision globale [131]. L’agrégateur applique d’abord des règles déterministes (schémas, déduplication, seuils de confiance) avant la consolidation finale, et confine les branches parallèles à l’analyse en lecture seule pour éviter tout conflit d’écritures [123] [131] [141].

### 7.3.3 Boucles vérificatrices : Generator-Verifier, Evaluator-Optimizer et Self-Refine

Le patron **Generator-Verifier** (aussi désigné *Evaluator-Optimizer*, *Review and Critique* ou *Maker-Checker*) dissocie la production d’un livrable de sa critique dans une boucle bornée [126] [128] [131]. Dans l’approche *Self-Refine*, Madaan et ses coauteurs mesurent une amélioration moyenne absolue d’environ 20 % sur sept tâches variées par raffinement itératif fondé sur une rétroaction structurée [142]. Pourtant, l’étude `MAST` avertit explicitement qu’« un vérificateur n’est pas une solution miracle » : `ChatDev` n’atteint que 33,33 % d’exactitude sur *ProgramDev* malgré la présence de réviseurs, en raison de faux positifs de validation (`FM-3.3`) et d’arrêts prématurés (`FM-3.1`) [125].

Pour rendre une boucle `Generator-Verifier` fiable en production, quatre garde-fous s’imposent :

1. **Contrôles déterministes en amont** : toute vérification mécanisable (syntaxe, `JSON Schema`, règles `SHACL` du chapitre 6, tests unitaires, seuils réglementaires) s’exécute avant tout juge `LLM` [126] [128].

2. **Isolation et indépendance du critique** : pour limiter la complaisance de validation relevée dans `MAST` (`FM-3.3`), le `Verifier` ne doit recevoir que le contrat d’objectif, l’artefact produit et les preuves d’exécution — jamais le monologue justificatif du générateur — et gagne à s’appuyer sur une rubrique d’évaluation structurée ou un modèle distinct [127] [125].
3. **Plafond d’itérations et test de stagnation** : la boucle doit imposer un plafond explicite (`max_iterations`, fixé par exemple à 2 ou 3 passes comme borne opérationnelle) ou une condition d’état de sortie afin d’éviter la dérive des coûts et les boucles infinies [128].
4. **Escalade humaine sur échec de convergence** : à l’épuisement du budget d’itérations sans verdict conforme, le workflow bascule obligatoirement vers un arbitrage humain (`HITL`) ou un repli déterministe sûr [128] [135].

Sur le plan économique, une boucle `Generator-Verifier` doit également être instrumentée par un **détecteur de stagnation ou d’oscillation**. Si la liste des défauts bloquants identifiés au tour `i` recoupe à l’identique celle du tour `i - 2`, ou si l’écart d’évaluation entre deux passes devient nul, poursuivre jusqu’à `max_iterations` consomme inutilement le budget de jetons sans amélioration mesurable [125] [128]. Pour le `SA`, ce court-circuit anticipé évite les cycles d’édition contradictoires où la correction d’une exigence réintroduit une régression ailleurs; pour l’`EA`, il fixe un plafond de coût unitaire prévisible par transaction métier, évitant qu’une boucle critique ne multiplie par quatre ou cinq la facture d’inférence d’un dossier standard [127] [128].

### 7.3.4 Précaution sur les Group Chats non structurés

L’orchestration en **Group Chat** (*roundtable* ou *council*) réunit plusieurs agents dans un fil conversationnel partagé géré par un modérateur [131] [132]. Parce que tous les participants émettent dans un historique commun croissant, ce patron amplifie rapidement les modes de défaillance `MAST FC2` : déraillement thématique, répétition de propositions déjà rejetées, oubli du mandat initial et confusion entre tours de parole [125] [131]. Microsoft Azure recommande explicitement de **limiter les discussions de groupe à trois agents ou moins** et de privilégier l’alternance formelle *Maker-Checker* lorsque l’objectif vise une validation structurée [131]. Au-delà de trois participants, ou dès que les agents disposent d’outils modifiant l’état externe, l’architecte doit remplacer le fil collectif ouvert par un `Scatter-Gather` en lecture seule ou par un `Supervisor` isolant chaque travailleur en `Subagents-as-Tools` [123] [124] [131].

> **[Figure]**
> - Client / SoE
> - Orchestrateur /
> - Routeur d'état
> - Agent A (Triage / Générateur)
> - Agent B / Pool
> - (Spécialistes)
> - Vérificateur (Critique indépendant)
> - Client / SoE Orchestrateur /
> - Routeur d'état
> - Agent A (Triage / Générateur)
> - Agent B / Pool
> - (Spécialistes)
> - Vérificateur (Critique indépendant)
> - 1. Handoff orienté état (transfert direct de contrôle)
> - 1 Requête utilisateur (session active)
> - 2 transfer_to_AgentB(input_type, input_filter)
> - 3 Filtre HandoffInputData & met à jour active_agent
> - 4 Active Agent B avec contexte filtré
> - 5 Réponse directe sous contrôle du domaine B
> - 2. Scatter-Gather parallèle (fan-out / agrégateur sous quorum)
> - 6 Broadcast tâches indépendantes (correlationId)
> - 7 Réponses partielles parallèles (nœuds 1..k)
> - 8 Aggregator attend quorum ou timeout SLA
> - 3. Boucle Generator-Verifier bornée (critère d'arrêt strict)
> - loop [i = 1 .. max_iterations (avec contrôle déterministe préalable)]
> - 9 Artefact candidat (URI + métadonnées)
> - 10 Tests déterministes puis revue critique isolée
> - alt [Conforme au contrat ou max_iterations atteint]
> - 1 1 Verdict VALIDÉ / ESCALADE HITL
> - [Défauts actionnables identifiés]
> - 12 Feedback structuré (écart & correctifs)

*Fig. 27. – Séquences d’orchestration des topologies Handoff, Scatter-Gather et Generator-Verifier bornée*

| Topologie | Mécanisme de contrôle | Latence et coût en jetons | Risque dominant (`MAST` / `OWASP`) | Cas d’usage cible EA/SA |
| --- | --- | --- | --- | --- |
| Séquentiel typé (`Pipeline`) | Arêtes fixes et portes déterministes [126] [133] | Linéaire prévisible (`O(N)` étapes); surcoût modéré [131] | Erreur amont non filtrée sans porte [125] | Chaînes réglementaires répétitives (sinistres, conformité) [131] |
| Routeur sémantique | Classification amont et branche exclusive [126] [129] | Minimale (1 routage + 1 spécialiste) [129] | Détournement du classificateur (`ASI01`) [135] | Triage multi-domaines vers spécialistes cloisonnés [126] [129] |
| `Supervisor` (`Subagents`) | Coordonnateur invoquant sous-agents isolés [136] | Élevé (~15× jetons vs conversation) [127] | Goulot central et sur-décomposition (`FC1`) [127] [125] | Investigation ouverte multi-sources à forte valeur [127] |
| Planification `DAG` (`LLMCompiler`) | Graphe compilé et `Task Fetching Unit` [138] | Jusqu’à 3,7× plus rapide, 6,7× moins cher vs `ReAct` [138] | Plan initial fragile si contexte très mouvant [138] | Requêtes composées à dépendances mixtes [138] [134] |
| `Handoff` orienté état | Outils `transfer_to_` et état `active_agent` [139] [140] | Faible par tour (dialogue direct sans relais) [129] | Ping-pong (`FC1`) et fuite d’historique sans filtre [125] [140] | Parcours client multi-étapes à interaction continue [129] [139] |
| `Scatter-Gather` | Diffusion parallèle et `Aggregator` sous quorum [141] | Bornée par `max(T₁, ..., Tₙ)` ou timeout SLA; coût `N×` [131] [141] | Biais d’agrégation et écritures concurrentes [123] [131] | Audit parallèle en lecture seule ou `Voting` [126] [123] |
| `Generator-Verifier` | Boucle bornée générateur + critique isolé [126] [128] | Multiplié par `k ≤ max_iterations` [128] | Faux positifs (`FM-3.3`) et stagnation [125] | Code, contrats et livrables à exigence critique [126] [128] |

*Tableau 7.2 — Matrice comparative des topologies d’orchestration : contrôle, profil économique, risques et cas d’usage.*

> **Arbitrage EA / SA** — Exiger un plafond d’itérations (`max_iterations`) et un test de stagnation sur toute boucle `Generator-Verifier`, une politique de quorum et un `timeout SLA` sur tout `Scatter-Gather`, et interdire les `Group Chats` dépassant trois agents [128] [131] [141]. Le `SA` place la vérification déterministe avant le juge cognitif et filtre les historiques de `Handoff` via `input_filter`

> [126] [140]; l’`EA` impose une escalade `HITL` en cas de non-convergence sur les processus à effet externe [128] [135].

## 7.4 Ingénierie des transferts d’état : passage par référence (Artifact URI) et prévention du Goal Drift

Une topologie bien choisie échoue néanmoins en production si la mécanique d’échange de données entre nœuds propage des charges brutes d’agent en agent. La copie répétée de messages et de documents volumineux provoque simultanément l’explosion des coûts, l’étouffement du signal utile et la dérive progressive du mandat initial (*Goal Drift*) [127] [137] [143].

### 7.4.1 Le jeu du téléphone arabe : passage par valeur contre Claim-Check et Artifact URI

Anthropic documente un écueil classique des architectures coordonnées : lorsque les sous-agents renvoient leurs productions intégrales au coordinateur qui les reformule ensuite vers l’étape aval, l’information subit l’effet du « jeu du téléphone arabe » (*game of telephone*), altérant chiffres, citations et nuances tout en multipliant les jetons consommés [127].

Le remède consiste à appliquer aux graphes d’agents le patron distribué **Claim-Check** [144], concrétisé par le service `Artifacts` de Google ADK [145] et par le dépôt externe recommandé par Anthropic [127]. Ce mécanisme s’articule en quatre étapes [127] [144] [145] :

1. **Externalisation versionnée** : le nœud producteur écrit le contenu volumineux ou binaire dans un magasin d’artefacts (`BaseArtifactService` ou stockage objet chiffré `GcsArtifactService`) cloisonné par espace de noms de session ou d’utilisateur, générant automatiquement une nouvelle version à chaque écriture sur un même nom de fichier [144] [145].
2. **Circulation d’une référence légère (**`Artifact URI`**)** : l’état partagé du graphe (`StateGraph`) ne reçoit qu’un pointeur logique (par exemple une référence structurée identifiant espace de noms, nom et version), accompagné d’une empreinte d’intégrité, du type `MIME` et d’un résumé concis [144] [145].
3. **Chargement ciblé à la demande** : le nœud aval décide quels artefacts charger via un outil dédié (`LoadArtifactsTool` ou lecture par plages), préservant les nœuds intermédiaires de tout transfert superflu [145] [137].
4. **Gouvernance du cycle de vie (**`TTL` **et** `ACL`**)** : conformément aux contreparties du patron `Claim-Check`, le magasin externe applique des politiques de rétention, d’expiration (`TTL`) et de contrôle d’accès par identité afin qu’aucune référence interceptée n’ouvre un accès indu [144] [145].

Trois plans doivent ainsi rester strictement distincts : l’`Artifact URI` interne véhicule les charges métier volumineuses entre nœuds d’une même orchestration; l’`Artifact` du protocole `A2A` (chapitre 5) encadre la livraison externe inter-domaines; et le journal d’événements du moteur durable (chapitre 9) enregistre uniquement les métadonnées légères requises pour la reprise déterministe.

### 7.4.2 Économie du contexte inter-nœuds : compaction, just-in-time retrieval et filtrage d’historique

L’ingénierie du contexte inter-nœuds vise à préserver le budget d’attention fini du modèle face au *context rot*, c’est-à-dire la baisse de rappel exact lorsque la fenêtre grandit [137]. Liu et ses coauteurs (*Lost in the Middle*) montrent que cette dégradation suit une courbe en U : les modèles exploitent fidèlement l’information située au tout début (primauté) ou à la toute fin (récence) du contexte, mais échouent fréquemment lorsque l’information déterminante se trouve enfouie au milieu, même sur les modèles à longue fenêtre [146].

Pour préserver une densité d’information élevée entre nœuds, le `SA` combine trois leviers [140] [137] :

- **Filtrage explicite des passations** : projeter uniquement les champs d’état nécessaires sur les arêtes `StateGraph` [133] ou configurer `input_filter` (`HandoffInputData` [140]) lors des `Handoffs` afin d’élaguer les traces exploratoires d’outils amont.
- **Compaction et prise de notes hors fenêtre** : condenser périodiquement l’historique croissant tout en externalisant décisions, contraintes et références d’artefacts dans une note structurée persistante [137].
- **Récupération juste-à-temps** : ne conserver dans l’état circulant que des identifiants légers (chemins, requêtes, `Artifact URI`) et récupérer à la demande les fragments pertinents [137].

### 7.4.3 Anatomie et prévention du Goal Drift et des cascades de détournement

Sur des trajectoires prolongées, les agents subissent un phénomène mesuré par Arike et ses coauteurs sous le nom de **Goal Drift** : exposés à des pressions environnementales et des sous-objectifs concurrents, ils s’écartent graduellement du mandat assigné dans l’invite système [143]. Bien que les meilleurs échafaudages conservent une forte fidélité au-delà de 100 000 jetons, **tous les modèles évalués finissent par dériver**, et cette dérive est directement corrélée à une sensibilité accrue aux comportements d’imitation locale (*pattern-matching*) à mesure que le contexte s’allonge [143].

Lorsque cette fragilité rencontre des données externes adverses ou non vérifiées dans un graphe multi-agents, elle ouvre la voie à deux risques critiques de l’`OWASP Top 10 for Agentic Applications 2026` : `ASI01` **(Agent Goal Hijack)**, où des entrées détournent l’objectif de planification, et `ASI08` **(Cascading Failures)**, où un écart ou une compromission locale se propage à vitesse machine d’agent en agent [135].

> **[Figure]**
> - Flux d'orchestration et transfert d'état gouverné
> - [container]
> - «component» Agent Émetteur
> - [Contexte isolé]
> - Produit un livrable
> - ou résultat massif
> - «component» Enveloppe typée
> - [StateGraph / JSON]
> - Artifact URI, résumé,
> - Goal Pin immuable
> - «component» Contrôleur anti-dérive
> - [Instruction Hierarchy]
> - Ancre primauté/récence,
> - filtre entrées tierces
> - «component» Agent Récepteur
> - [Contexte minimal]
> - Charge à la demande
> - les extraits requis
> - «container» Artifact Store (Claim-Check / GCS)
> - [Stockage gouverné]
> - Blobs versionnés, ACL par
> - locataire, empreinte SHA-256 et politique
> - TTL
> - 3. Met à jour état (sans payload brut)
> - 4. Applique hiérarchie et vérifie mandat
> - 5. Transmet enveloppe compacte ancrée
> - 1. Écrit payload volumineux
> - 2. Retourne URI + version
> - 6. Lit extraits ciblés (juste-à-temps)

*Fig. 28. – Transfert d’état par référence via Artifact URI et contrôleur anti-dérive Goal Pinning*

La prévention de ces dérives repose sur quatre défenses structurelles intégrées à l’orchestrateur [143] [146] [147] [135] :

1. **Ancrage du mandat aux extrémités (**`Goal Pinning`**)** : exploiter la courbe en U de *Lost in the Middle* [146] en maintenant le contrat d’objectif immuable (mandat métier, seuils autorisés, critères d’arrêt)
  hors de l’historique conversationnel mutable et en le réinjectant en tête système et en fin immédiate de contexte avant chaque décision d’action [143] [146].
2. **Hiérarchie stricte des instructions (**`Instruction Hierarchy`**)** : appliquer les principes de Wallace et al. (OpenAI) en distinguant hiérarchiquement consignes développeur, requêtes utilisateur et données tierces (retours d’outils, artefacts et messages de pairs) afin que les données ne puissent jamais surclasser le mandat privilégié [147] [135].
3. **Validation typée des enveloppes inter-nœuds** : imposer des schémas structurés (`input_type`, `JSON Schema`) sur tout transfert d’état et rejeter les champs textuels libres susceptibles de redéfinir le rôle du nœud aval (`MAST FC1`) [125] [140].
4. **Séparation planification/exécution et coupe-circuits SRE** : conformément aux recommandations de l’OWASP [135], soumettre toute action irréversible issue du graphe à une porte de politique déterministe (les *Intent Gates* `OPA` /`Cedar` et identités `NHI` /`SPIFFE` du chapitre 10) et appliquer des plafonds stricts de profondeur de délégation et de budget [135].

| Mécanisme d’ingénierie | Problème résolu | Garanties SA | Exigences EA / Audit |
| --- | --- | --- | --- |
| `Claim-Check` / `Artifact URI` | Effet « téléphone arabe » [127] et surcharge de bus [144] | Enveloppes d’état légères, versionnement [145] et lecture ciblée | Cloisonnement session/locataire, intégrité et `TTL` [144] [145] |
| `input_filter` et compaction | *Context rot* [137] et pollution inter-nœuds (`FC1`) [125] | Élagage des traces d’outils et maintien d’un signal compact [140] [137] | Traçabilité des filtres appliqués pour audit `EvalOps` |
| `Goal Pinning` (primauté/récence) | Imitation locale et `Goal Drift` en contexte long [143] [146] | Mandat immuable hors fil mutable, ancré aux deux bornes [146] | Imputabilité explicite du mandat validé par l’*Agent Owner* |
| `Instruction Hierarchy` + validation | Détournement `ASI01` et cascades `ASI08` [147] [135] | Isolation données vs consignes et plafonds de profondeur [147] [135] | Blocage déterministe avant mutation des `SoR` [135] |

*Tableau 7.3 — Patrons d’ingénierie des transferts d’état et mesures de prévention du Goal Drift.*

> **Arbitrage EA / SA** — Interdire le passage par valeur de charges volumineuses entre agents; imposer le patron `Claim-Check` (`Artifact URI` versionné avec `TTL` et `ACL`) couplé à l’ancrage d’objectif `Goal Pinning` hors historique mutable [127] [144] [145] [143]. Le `SA` filtre les passations (`input_filter`), applique l’*Instruction Hierarchy* aux retours de pairs et déréférence les artefacts juste-à-temps [140] [137] [147]; l’`EA` exige la journalisation d’intégrité des artefacts et le passage de toute écriture finale par un contrôle déterministe hors fenêtre cognitive [135].

## Synthèse architecturale et transition vers le chapitre 08

La composition multi-agents obéit à une règle d’économie stricte : démarrer par un agent unique outillé optimisé (`Skills`, `ReWOO`, workflow déterministe), n’escalader que sur preuve de contrainte de parallélisme de lecture, d’isolation de privilèges ou de vérification contradictoire, privilégier les graphes dirigés (`Séquentiel typé`, `Routeur`, `Supervisor` à sous-agents isolés, `DAG`), borner rigoureusement les topologies collaboratives (`Handoff`, `Scatter-Gather`, `Generator-Verifier`) et ne faire circuler entre nœuds que des enveloppes légères par `Artifact URI` protégées contre le `Goal Drift` [126] [124] [125] [144] [143].

Toutes ces topologies supposent néanmoins la présence d’un graphe ou d’un coordonnateur pilotant la séquence de bout en bout. Lorsque l’entreprise doit découpler des domaines réagissant en continu à des flux d’événements métier asynchrones sans chef d’orchestre synchrone, ce modèle atteint ses limites. Le chapitre 8 aborde donc la chorégraphie réactive et l’`Event Mesh` d’entreprise, avant que le chapitre 9 ne traite la persistance transactionnelle et l’exécution durable.
