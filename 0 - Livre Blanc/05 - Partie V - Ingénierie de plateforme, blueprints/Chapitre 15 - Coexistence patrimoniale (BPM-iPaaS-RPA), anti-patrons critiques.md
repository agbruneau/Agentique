# Chapitre 15 — Coexistence patrimoniale (BPM/iPaaS/RPA), anti-patrons critiques et feuille de route d’adoption

Les quatorze chapitres précédents ont défini l’architecture cible de l’entreprise agentique : séparation des `Systems of Record (SoR)` et des `Systems of Agency`, règle hybride `80/20`, contrats ouverts `MCP` et `A2A`, souveraineté mémorielle, exécution durable, sécurité `Zero-Trust`, observabilité `OpenTelemetry` /`EvalOps`, gouvernance `FinOps`, plateforme interne (`IAP`) et blueprints sectoriels. En pratique, aucune organisation ne déploie cette architecture sur table rase : les directions technologiques exploitent déjà des moteurs `BPMN`, des bus `iPaaS` et de gestion d’API, ainsi qu’un parc d’automates `RPA` (*Robotic Process Automation*) [365] [366] [367]. Or les constats empiriques rappellent la fragilité de la transition : après entretiens avec 65 praticiens, la `RAND Corporation` établit que plus de 80 % des projets d’IA échouent — le double des projets informatiques classiques — par incompréhension du problème métier et déficit d’infrastructure [368], tandis qu’Acharya souligne que seuls 21 % des dirigeants disposent d’une gouvernance mature et que 40 % des projets agentiques risquent l’échec d’ici 2027 faute de contrôles et de maîtrise des coûts [369].

Ce chapitre clôt l’ouvrage sur la rationalisation du patrimoine, les leçons d’échec et la trajectoire d’adoption, sans introduire de nouveau protocole. En **lecture** `EA`, il arbitre le devenir des outils `BPMN`, `iPaaS` et `RPA`, combat l’étalement agentique et séquence la montée en maturité sur 360 jours. En **lecture** `SA`, il formalise l’encapsulation des automates hérités, la migration incrémentale *Strangler Fig* en quatre stades et les remédiations aux douze anti-patrons majeurs.

## 15.1 Rationalisation et coexistence avec l’automatisation existante (BPMN, iPaaS/API Management, RPA)

Remplacer brutalement les orchestrateurs et intégrations existants par des boucles cognitives compromet la conformité, alourdit le coût unitaire et fragilise les flux prévisibles [370] [371] [372]. La rationalisation répartit plutôt les responsabilités entre logique déterministe et nœuds cognitifs dans le prolongement de la règle `80/20` (chapitre 3) et de l’architecture en quatre plans (chapitre 2).

### 15.1.1 Complémentarité structurelle avec les moteurs BPMN 2.0

Les moteurs `BPMN 2.0` exécutables (`Camunda 8` sur `Zeebe`, `UiPath Maestro`) gouvernent déjà des chaînes critiques soumises à des exigences strictes de conformité et de traçabilité [365] [366]. Plutôt que de les écarter, l’architecture hybride maintient le diagramme `BPMN` comme colonne vertébrale déterministe et ouvre des poches d’autonomie bornées via le **sous-processus ad hoc** (`~`) [365] [373]. Dépourvu d’événements de début ou de fin internes, ce conteneur regroupe tâches de service, connecteurs et tâches humaines *Human-in-the-Loop* qu’un agent peut activer dans un ordre dynamique ou répétitif jusqu’à une `completionCondition` explicite [365]. Couplé au connecteur `AI Agent Sub-process`, le modèle raisonne à l’intérieur de ce périmètre puis rend la main au flux structuré, tandis qu’un simple `AI Agent Task` suffit aux appels unitaires sans boucle [373].

En **lecture** `EA`, les processus audités déjà modélisés en `BPMN` conservent leur moteur comme autorité d’état et de `SLA` [365] [366]. En **lecture** `SA`, les nouveaux services agentiques orientés code exploitent l’exécution durable de l’`IAP` (chapitres 9 et 13), et les flux `BPMN` patrimoniaux évoluent progressivement grâce à la migration d’instances en vol [374].

### 15.1.2 Extension des plateformes iPaaS et API Management

Les plateformes `iPaaS` et de gestion d’API (`MuleSoft`, `Kong`) assurent déjà la connectivité inter-applicative et le contrôle du trafic API [367] [375]. Leur rôle s’étend vers un plan de contrôle sémantique sans reconstruire les connecteurs existants. D’un côté, des ponts tels que le `MCP Bridge` de `MuleSoft Agent Fabric` exposent des API gouvernées en outils `MCP` réutilisables, sous réserve d’appliquer l’ergonomie d’intention définie au chapitre 4 [367]. De l’autre, des passerelles comme `Kong AI Gateway` étendent l’authentification, la limitation de débit, la sécurité des données et l’observabilité aux échanges `LLM`, `MCP` et `A2A` [375].

En **lecture** `EA`, des scanners automatisés relient API patrimoniales, serveurs `MCP` et agents dans un registre unique afin d’éviter la prolifération de connecteurs redondants [367]. En **lecture** `SA`, les synchronisations massives, flux *batch* et transformations `ETL` déterministes restent confinés à l’`iPaaS` : aucun agent ne remplace un bus d’intégration structuré [370] [371] [372].

### 15.1.3 Sortie maîtrisée du RPA fragile et coexistence par encapsulation

Le `RPA` classique (`Power Automate desktop flows`, `Robot Framework` sous `Camunda RPA`, `UiPath`) automatise des gestes répétitifs par sélecteurs d’interface graphique, images, coordonnées d’écran ou émulateurs de terminaux là où aucune API n’existe [376] [366] [377]. Sensible aux refontes d’écran, ce parc engendre une maintenance élevée et alimente la fragmentation s’il échappe à l’orchestration centrale [376] [369]. La rationalisation proscrit autant le simple réétiquetage marketing de bots en « agents » que le pilotage non confiné d’interfaces critiques par des agents généralistes [378] [369]. Elle applique trois voies :

1. **Décommissionnement par API ou** `ACL` : retirer chaque robot `RPA` dès qu’une API ou une isolation par couche anti-corruption (`ACL`) et capture de changements (`CDC`, chapitre 4) devient disponible [367] [379].
2. **Encapsulation sous orchestration** : confiner les automates résiduels (mainframes ou progiciels fermés) comme travailleurs déterministes appelés par le moteur `BPMN` ou derrière l’`ACL`, l’orchestrateur conservant seul l’état et les reprises [376] [366] [379].
3. **Cantonnement des manipulations dynamiques d’interface** : limiter l’exploration cognitive d’écran aux exceptions non structurées à faible volume, dans un bac à sable durci sous privilèges minimaux et validation humaine avant toute action irréversible [380] [381] [382].

> **[Figure]**
> - Orchestration hybride
> - [system]
> - Médiation iPaaS &
> - Passerelles
> - [system]
> - Exécution patrimoniale &
> - SoR [system]
> - «container» Moteur BPMN 2.0
> - [Camunda / Maestro]
> - Flux réglementaires, SLA et tâches humaines
> - «container» Sous-processus ad hoc (~)
> - [AI Agent Connector]
> - Boucle cognitive bornée
> - sur outils déclarés
> - «container» iPaaS & API Management
> - [MuleSoft / Kong]
> - Flux ETL stables, Agent Registry et MCP Bridge
> - «container» AI & MCP Gateway
> - [Plan de contrôle]
> - Quotas jetons, OPA Intent Gate,
> - télémétrie OTel et routage
> - «container» Couche Anti-Corruption
> - [ACL + CDC/CQRS]
> - Traduction sémantique, idempotence et projection
> - «container» Worker RPA confiné
> - [Desktop / Robot]
> - Écrans sans API uniquement,
> - encapsulé en tâche bornée
> - «container» Systems of Record
> - [ERP / Mainframe]
> - Autorité comptable
> - et transactionnelle
> - «person»
> - Opérateur / Client
> - SoE et portes HITL
> - Initie dossier / HITL
> - Délègue exception
> - Appels modèles & MCP Appels haute volumétrie
> - Pont MCP Bridge
> - Contrats typés
> - Sous-tâche sans API
> - CQRS / écriture idempotente Action UI bornée

*Fig. 57. – Topologie de coexistence patrimoniale unissant BPMN hybride, iPaaS, AI/MCP Gateway et RPA confiné*

| Strate existante | Rôle conservé | Limite principale | Coexistence cible | Critère de retrait / bascule |
| --- | --- | --- | --- | --- |
| `BPMN 2.0` (`Camunda`, `Maestro`) | Macro-flux audités, `SLA`, tâches humaines | Rigidité face aux entrées ambiguës | Sous-processus ad hoc (`~`) borné | Maintenu si réglementaire; neuf sur `IAP` durable |
| `iPaaS` **/** `API Mgmt` (`MuleSoft`, `Kong`) | Flux `ETL`/API haute volumétrie, lignage | Insuffisant seul sur jetons et `MCP` /`A2A` | `AI & MCP Gateway` + `MCP Bridge` curé | Flux déterministes maintenus hors boucle LLM |
| `RPA` (`Power Automate`, `Robot`) | Gestes répétitifs sans API disponible | Fragilité UI et silos locaux | Worker isolé sous `BPMN` ou `ACL` | Retiré dès ouverture d’API ou flux `CDC` |
| `Systems of Agency` | Triage ambigu, synthèse, exceptions | Coût variable et non-déterminisme | Nœuds cognitifs (`20 %`) sous `Intent Gates` | Repli instantané vers flux `L0` sur anomalie |

*Tableau 15.1 — Matrice de rationalisation et de coexistence : BPMN 2.0, iPaaS/API Management, RPA et Systems of Agency.*

> **Arbitrage EA / SA** — Interdire toute réécriture opportuniste des workflows `BPMN` réglementaires et des flux `iPaaS` stables en boucles d’agents libres, ainsi que la requalification cosmétique de scripts `RPA` en capacités agentiques [365] [369] [372]. L’`EA` gèle les nouveaux développements `RPA` hors systèmes strictement dépourvus d’API et rattache API, connecteurs `MCP` et bots au registre central [367] [381]. Le `SA` expose les intégrations par façades curées sur la passerelle, confine l’autonomie `BPMN` dans des sous-processus ad hoc à condition d’achèvement explicite et isole chaque automate `RPA` résiduel derrière une `ACL` [365] [376] [379].

## 15.2 Migration incrémentale (Strangler Fig agentique) : ombre, recommandation, action bornée, autonomie sous contrat

Remplacer d’un seul tenant un processus patrimonial par un système agentique reproduit l’échec des réécritures *Big Bang* : les comportements implicites accumulés échappent aux spécifications et les besoins d’affaires évoluent durant la refonte [383] [368]. Formalisé par Martin Fowler [383] et outillé par `AWS` et `Azure` [384] [385], le patron **Strangler Fig** substitue une façade d’interception devant le système hôte pour migrer chaque capacité incrémentalement sous coexistence réversible jusqu’au retrait du patrimoine [383] [384] [385].

### 15.2.1 Du Strangler Fig applicatif à l’étranglement progressif des flux cognitifs

La transposition agentique conserve les trois phases d’`AWS Prescriptive Guidance` (**Transformer**, **Coexister**, **Éliminer**) [384] en ajoutant deux garanties propres aux systèmes probabilistes. Premièrement, la façade de routage logée dans l’`AI` /`API Gateway` s’appuie sur une **couche anti-corruption (**`ACL`**)**

empêchant les schémas hérités du `SoR` de polluer le contexte et les contrats des agents; elle doit intégrer reprises bornées et coupe-circuits pour ne pas devenir un goulot ou point de défaillance unique [385] [379].

Deuxièmement, parce qu’un agent techniquement disponible peut néanmoins poser des actes erronés [382], la bascule franchit des portes d’évaluation continue (`EvalOps`) [386] et suit une **graduation stricte d’autorité** alignée sur le déploiement par étapes (*staged deployment*) d’`OpenAI` [380] et le principe d’autonomie contrôlée d’`AWS` [378]. Pour les dossiers longs déjà ouverts, la migration d’instances en vol (comme dans `Camunda 8` [374]) préserve l’état actif sans interruption.

### 15.2.2 Les quatre stades de montée en autonomie sous contrat

L’étranglement suit quatre stades cloisonnés, chacun muni d’un repli immédiat vers la branche patrimoniale `L0` [384] [387] [380] :

1. **Stade 1 — Mode ombre (*Shadow Mode*)** : inspirée du patron *Shadow Tests* [387], la façade duplique de façon asynchrone les requêtes réelles vers la chaîne agentique candidate sans modifier la réponse retournée à l’usager ni écrire dans le `SoR`. En contexte agentique, le `SA` maintient les outils mutateurs en simulation ou lecture seule et compare hors chemin critique exactitude de trajectoire, latence et coût unitaire à la référence patrimoniale [387] [386] [382].
2. **Stade 2 — Mode recommandation (*Assistive*)** : après validation en mode ombre, l’agent produit une proposition structurée avec pièces probantes et différentiel d’action dans le `SoE` ou une tâche utilisateur `BPMN` [373] [380] [372]. L’humain ou le moteur déterministe exécute seul la mutation finale, et les taux d’acceptation mesurent le gain réel face à la ligne de base métier (*business baseline*) [386] [388].
3. **Stade 3 — Action bornée (*Bounded Autonomy*)** : en routage canari ciblé, l’agent exécute seul les opérations réversibles ou compensables sous plafonds programmatiques et portes `Intent Gate` [380] [378]. Toute action irréversible, hors domaine ou sous seuil de confiance suspend l’exécution pour approbation humaine préalable [380] [382].
4. **Stade 4 — Autonomie sous contrat (*Contracted Autonomy*)** : le flux cible absorbe le segment sous contrat `SLO`, détection continue de dérive et arrêt d’urgence (*shutdown*) basculant instantanément vers `L0` [380] [382]. Le composant patrimonial n’est retiré qu’après stabilisation prolongée et vérification des règles de conservation [383] [385] [382].

> **[Figure]**
> - Façade d'interception (Passerelle)
> - Stades progressifs d'autonomie sous
> - contrat
> - Routeur de façade (AI & API Gateway) Flux patrimonial L0 (BPMN / API / RPA)
> - Stade 1 : Mode ombre Trafic dupliqué hors chemin critique Zéro écriture SoR / outils simulés
> - Stade 2 : Recommandation Proposition structurée + preuves Validation & écriture humain / BPMN
> - Stade 3 : Action bornée Écritures réversibles sous seuils OPA Porte HITL sur pivots irréversibles
> - Stade 4 : Autonomie sous contrat Exécution durable sous SLO et budget Coupe-circuit + retrait patrimonial
> - Trafic de référence
> - (100 % initial)
> - Copie miroir (Shadow traffic)
> - Écart EvalOps <= seuil
> - et coût validé
> - Taux d'acceptation stable
> - et contrôle ACL
> - Dégradation qualité
> - ou dérive
> - Zéro incident R3/R4
> - et conformité SLO
> - Repli coupe-circuit (FORCED_OPEN -> L0)
> - Retrait ou échec
> - ROI baseline

*Fig. 58. – Cycle de migration Strangler Fig agentique en quatre stades sous façade et mécanismes de repli*

| Stade *Strangler Fig* | Autorité sur `SoR` | Routage façade | Critère d’avancement | Protection et repli |
| --- | --- | --- | --- | --- |
| **1. Mode ombre** | Nulle; lecture isolée ou simulée | Miroir asynchrone; réponse patrimoniale | Exactitude `EvalOps`, latence et coût validés | Zéro impact client; coupure du miroir |
| **2. Recommandation** | Indirecte; validation humaine ou `BPMN` | Brouillon agentique; écriture héritée | Taux d’acceptation et gain vs *baseline* | Désactivation suggestion; retour formulaire |
| **3. Action bornée** | Écritures réversibles sous seuils; pivots `HITL` | Canari par segment à risque maîtrisé | Zéro violation `OPA`, `pass^k` stable | Rejet `Intent Gate`, compensation, canari `0 %` |
| **4. Autonomie sous contrat** | Exécution complète sous `SLO` et `R1–R4` | `100 %` du segment; migration en vol | Respect soutenu `SLO` /`FinOps`, audit `3LoD` | Arrêt d’urgence vers `L0` avant retrait |

*Tableau 15.2 — Critères de transition et garde-fous des quatre stades du Strangler Fig agentique.*

> **Arbitrage EA / SA** — Interdire le passage direct d’un pilote à l’autonomie en production ainsi que le décommissionnement du flux de repli avant validation du stade 4 [383] [380] [382]. L’`EA` subordonne chaque promotion à l’accord de l’`Agent Owner` sur le gain prouvé face à la *baseline* [388] [382]. Le `SA` place la façade dans la passerelle couplée à une `ACL`, simule les écritures au stade 1, automatise le blocage `EvalOps` avant canari et maintient un basculement immédiat vers `L0` [384] [379] [387] [386].

## 15.3 Catalogue diagnostique des 12 anti-patrons majeurs : symptômes, causes racines et remédiations

Les analyses empiriques convergent sur les moteurs d’échec en production. La `RAND Corporation` lie les plus de 80 % d’échecs à une définition floue du problème métier, des données insuffisantes, la poursuite technologique et un déficit d’infrastructure [368]. Sur les graphes multi-agents, la taxonomie `MAST` (plus de 1 600 traces issues de sept cadriciels) établit que la majorité des 14 modes de panne relève de la conception système et du désalignement inter-agents [389]. La taxonomie du `Microsoft AI Red Team` [390], l’`OWASP Top 10 for Agentic AI` (`ASI01` –`ASI10`) [391] et l’étude sur l’étalement agentique (`AAGMM`) [369] complètent ce diagnostic en douze anti-patrons répartis en quatre familles.

### 15.3.1 Famille A — Stratégie, portefeuille et économie

`AP-01` **Syndrome du marteau agentique (*Technology-First*)**. *Symptômes* : des flux prévisibles à règles fixes sont réécrits avec des boucles `LLM` plus lentes et onéreuses, ou des scripts classiques sont rebaptisés agents [370] [369] [372]. *Cause racine* : poursuite de la nouveauté (*shiny object syndrome* [368]) sans tri entre automatisation déterministe et raisonnement [372]. *Remédiation* : appliquer l’arbre

`80/20` (code déterministe ou `RAG` sans boucle sur les cas structurés) et exiger en revue `ARB` la justification écrite de toute boucle cognitive [370] [371] [372].

`AP-02` **Étalement et agents fantômes (*Agent Sprawl*)**. *Symptômes* : prolifération sur plateformes *low-code* d’agents redondants, d’agents orphelins sans responsable et de délégations non inventoriées [369] [381]. *Cause racine* : ouverture de la création d’agents sans registre central ni politique de retrait [367] [369]. *Remédiation* : raccorder des scanners de découverte au registre central (chapitre 12), imposer un `Agent Owner` nominatif et une identité attestée, et suspendre les agents orphelins [367] [369] [381] [382].

`AP-03` **Cécité économique (*Demo-Driven ROI*)**. *Symptômes* : des pilotes applaudis en démonstration échouent à l’échelle faute de rentabilité démontrée ou sous l’explosion des frais d’inférence [369] [388]. *Cause racine* : absence de *business baseline*, confusion entre temps gagné et valeur financière nette, et suivi limité au coût du jeton [369] [388]. *Remédiation* : chiffrer la référence avant projet, intégrer tous les postes (`inférence`, `intégration`, `gouvernance`, `HITL`) et instaurer le *Showback* avant le *Chargeback* (chapitre 12) [388].

### 15.3.2 Famille B — Intégration, outils et patrimoine

`AP-04` **Exposition brute et *Tool Sprawl***. *Symptômes* : l’agent reçoit un trop grand nombre d’outils issus directement d’API existantes, confond des signatures voisines et gaspille sa fenêtre d’attention en schémas [367] [370]. *Cause racine* : exposition mécanique d’interfaces conçues pour des humains sans conception d’*Agent-Computer Interface* (`ACI`, chapitre 4) [370]. *Remédiation* : agréger les opérations en façades d’intention via la passerelle (`MCP Bridge` curé), filtrer les outils par rôle et optimiser descriptions et retours d’erreur [367] [370].

`AP-05` **Surcouche cognitive sur** `RPA` **fragile**. *Symptômes* : un agent pilote des scripts de clics locaux sur des écrans instables; les changements d’interface déclenchent des boucles de réessais et des saisies incomplètes [376] [366] [377]. *Cause racine* : empilement d’un raisonnement probabiliste sur une dette d’intégration UI sans contrat transactionnel [376] [379]. *Remédiation* : remplacer le `RPA` par des API ou projections `CDC`; sinon, confiner le robot en tâche déterministe sous moteur `BPMN` hors de l’agent [376] [366] [379].

`AP-06` **Accès direct non amorti aux** `Systems of Record`. *Symptômes* : les appels exploratoires saturent `ERP` ou `mainframes`, alourdissent les licences et causent des doubles écritures [379] [380]. *Cause racine* : couplage direct entre logique cognitive et contraintes transactionnelles patrimoniales [379]. *Remédiation* : interposer une couche anti-corruption (`ACL`, chapitre 4), déporter les lectures sur projections découplées et imposer idempotence et réversibilité [379] [380].

### 15.3.3 Famille C — Orchestration, contexte et exécution

`AP-07` **Essaim multi-agents prématuré (*Parallel Writers*)**. *Symptômes* : des sous-agents parallèles produisent des résultats conflictuels (`MAST` [389]) et s’avèrent moins fiables qu’un agent unique [370] [392] [371]. *Cause racine* : fragmentation des traces décisionnelles et décisions implicites concurrentes sur les écritures, identifiées par `Cognition` [392]. *Remédiation* : privilégier un agent unique outillé ou un workflow structuré [370] [371] [372], sérialiser toute écriture sur une trace continue et réserver le parallélisme aux lectures isolées (chapitre 7) [392] [372].

`AP-08` **Boucle volatile non bornée**. *Symptômes* : une boucle en échec répété consume les quotas, propage des pannes en cascade (`ASI08` [391]) ou perd tout état lors d’un redéploiement [374] [371]. *Cause racine* : exécution d’un processus long en mémoire éphémère sans plafond programmatique [380] [370].

*Remédiation* : loger les boucles longues sur moteur durable ou `BPMN` avec migration d’instances [374], borner les itérations et déployer des coupe-circuits (chapitres 9 et 11) [380] [378].

`AP-09` **Dilution du contexte et abstraction opaque**. *Symptômes* : l’exactitude s’effondre au fil des tours et les équipes ne diagnostiquent plus les échecs cachés sous des cadriciels opaques [370] [392]. *Cause racine* : accumulation brute de traces sans compaction et sur-abstraction logicielle [370] [392]. *Remédiation* : utiliser un harnais sobre au-dessus des API de modèles [370], compacter les décisions clés (*Context Engineering*) [392] et externaliser les charges volumineuses par référence (chapitre 7).

### 15.3.4 Famille D — Sécurité, confiance et exploitation

`AP-10` **Politique métier dans le prompt (*Prompt-as-Policy*)**. *Symptômes* : une injection indirecte détourne l’objectif (`ASI01`) et exploite outils (`ASI02`) ou identités sur-privilégiées (`ASI03`) [391] [381]. *Cause racine* : confusion entre consigne probabiliste en texte et frontière de sécurité déterministe [380] [378]. *Remédiation* : déplacer les invariants dans une `Intent Gate` (`Policy-as-Code`, chapitre 10), bannir les secrets statiques au profit d’identités `NHI` éphémères et appliquer le moindre privilège [380] [391] [381].

`AP-11` **Mémoire partagée non assainie (*Memory Poisoning*)**. *Symptômes* : une entrée corrompue en mémoire persistante fausse les sessions futures ou sert de pivot d’exfiltration (`ASI06`, `ASI08`) [390] [391]. *Cause racine* : absence de validation de provenance à l’écriture et de propagation des `ACL` à la lecture [390] [391]. *Remédiation* : cloisonner les locataires, filtrer par `ACL` à chaque requête (chapitre 6), contrôler la provenance des écritures et versionner les instructions par `GitOps` (chapitre 13) [390] [391] [378].

`AP-12` **Production sans** `EvalOps` **ni coupe-circuit**. *Symptômes* : les mises à jour de modèles provoquent des régressions silencieuses, la revue `HITL` devient une validation mécanique (`ASI09`) et aucun arrêt rapide n’endigue un agent déviant (`ASI10`) [380] [391] [386] [382]. *Cause racine* : lancement au jugé sans évaluation automatisée ni procédure d’arrêt [386] [382]. *Remédiation* : imposer des seuils `EvalOps` bloquants sur chaque évolution [386] [382], afficher l’impact `SoR` exact aux valideurs et tester le repli `L0` [380] [382].

| Code et anti-patron | Famille | Symptôme clé | Cause racine | Remédiation `EA` /`SA` |
| --- | --- | --- | --- | --- |
| `AP-01` Marteau agentique | Stratégie | Coût/latence excessifs sur flux fixe | Effet de mode sans tri `80/20` | Code déterministe ou `RAG` simple |
| `AP-02` Étalement fantôme | Stratégie | Doublons, agents orphelins | Création sans registre central | Scanners + registre + `Agent Owner` |
| `AP-03` Cécité économique | Stratégie | Abandon après pilote coûteux | Zéro *baseline* ni `TCO` complet | Coût par résultat réussi + *Showback* |
| `AP-04` *Tool Sprawl* (`CRUD`) | Intégration | Mauvais choix d’outils, saturation | API brutes sans ergonomie `ACI` | Façades d’intention `MCP Bridge` |
| `AP-05` Surcouche sur `RPA` | Intégration | Boucles d’échec sur sélecteurs UI | Pansement sur dette d’API | Sortie API/`CDC`, sinon tâche `BPMN` |
| `AP-06` Accès direct `SoR` | Intégration | Surcharge `ERP`, écritures doubles | Zéro tampon sémantique | `ACL` + `CQRS` + idempotence |
| `AP-07` Essaim prématuré | Orchestration | Conflits d’écriture, dérive `MAST` | Traces fragmentées, parallélisme | Agent unique / workflow; sérialiser |
| `AP-08` Boucle volatile | Orchestration | Perte d’état, pannes en cascade | Mémoire volatile, zéro plafond | Moteur durable / `BPMN` + coupe-circuit |
| `AP-09` Dilution de contexte | Orchestration | Oubli de consignes, opacité | Zéro compaction, cadriciel lourd | Harnais sobre + compaction structurée |
| `AP-10` *Prompt-as-Policy* | Sécurité | Détournement `ASI01`, abus `ASI03` | Prompt utilisé comme pare-feu | `Intent Gate` + `NHI` moindre privilège |
| `AP-11` Mémoire empoisonnée | Sécurité | Corruption persistante `ASI06` | Écritures non vérifiées, zéro `ACL` | Cloisonnement, `ACL` requête, provenance |
| `AP-12` *Vibe-Testing* | Exploitation | Régressions, `HITL` mécanique | Absence d’`EvalOps` et d’arrêt | `EvalOps` bloquant en CI + repli `L0` |

*Tableau 15.3 — Catalogue synthétique de diagnostic des 12 anti-patrons critiques (symptômes, causes racines et remédiations).*

> **Arbitrage EA / SA** — Ériger les douze anti-patrons `AP-01` à `AP-12` en liste de contrôle bloquante de l’`ARB` avant toute promotion au stade 3 [368] [369] [382]. L’`EA` refuse l’homologation sans *baseline* `ROI`, sans `Agent Owner` ou hors registre (`AP-01` à `AP-03`) [369] [388] [381]. Le `SA` rejette toute architecture exposant des routes `CRUD` brutes, contournant l’`ACL` des `SoR`, parallélisant des écrivains ou confiant une règle impérative à un prompt (`AP-04` à `AP-12`) [379] [370] [392] [391].

## 15.4 Modèle de maturité en 5 paliers et feuille de route séquencée (90 / 180 / 360 jours)

Industrialiser ces leçons à l’échelle exige une progression disciplinée plutôt qu’une somme d’initiatives isolées [393] [369] [372]. Le cadre retenu unifie les cinq paliers d’`AAGMM` sur douze domaines arrimés à `NIST AI RMF` et `ISO/IEC 42001` [369], la boucle continue *Govern–Map–Measure–Manage* du `NIST AI RMF Playbook` [394], les stades d’`AWS` (*Envision*, *Experiment*, *Launch*, *Scale*) [393] et le modèle opérationnel de `Microsoft CAF` [372] [381] [382].

### 15.4.1 Modèle de maturité agentique en 5 paliers

Les 750 simulations d’Acharya établissent l’impact mesurable de cette progression : entre le palier initial et les paliers gouvernés (`M4–M5`), l’indice d’étalement chute de **94,3 %**, les incidents de risque reculent de **96,4 %** et l’achèvement effectif progresse de **32,6 %** [369]. Les cinq paliers (`M1` à `M5`) couvrent cinq axes conjoints `EA` /`SA` détaillés au Tableau 15.4 :

- `M1` **— Ad hoc** : prototypes locaux sans registre, sans `Agent Owner`, clés statiques, bots `RPA` isolés et zéro référence économique [393] [369] [388].
- `M2` **— Réactif (*Experiment*)** : création d’un pôle d’excellence (`AI CoE`), inventaire initial (*Map* [394]), première passerelle `AI Gateway` et pilotes *Strangler Fig* en ombre ou recommandation avec *baseline* chiffrée [387] [393] [388].
- `M3` **— Défini (*Launch*)** : registre obligatoire avec paliers `R1–R4`, plateforme `IAP` (*Golden Paths*, `MCP Gateway` sur `ACL`, `NHI` /`OBO`, `Intent Gates`), `EvalOps` en intégration continue, `Showback` `FinOps` et actions bornées (`Stade 3`) ou `BPMN` ad hoc [365] [380] [393] [369] [382].
- `M4` **— Géré (*Scale*)** : exécution durable généralisée, détection automatisée d’étalement et de dérive, retrait planifié du `RPA` fragile, ouverture `A2A` inter-domaines et `Chargeback` `FOCUS` sous revue `3LoD` [376] [374] [390] [369] [388].
- `M5` **— Optimisé (*Governance-as-Code*)** : conformité vérifiée par le code (*Policy-as-Code*), maillage fédéré `OASF` /`Event Mesh`, autonomie sous contrat (`Stade 4`), exercices de bascule multi-fournisseurs et repli `L0` pilotés par `ROI` ajusté du risque [367] [380] [378] [369].

| Palier | Gouvernance (`EA`) | Architecture (`SA`) | Sécurité & `NHI` | `EvalOps` & SRE | `FinOps` / `ROI` |
| --- | --- | --- | --- | --- | --- |
| `M1` **Ad hoc** | Zéro registre; *Shadow AI* et orphelins | Appels directs; `RPA` isolés | Clés statiques; droits hérités | Tests manuels; zéro trace | Factures opaques; zéro *baseline* |
| `M2` **Réactif** | `AI CoE`, charte, inventaire initial | `AI Gateway`, 1re façade + `ACL` | Comptes isolés sur pilotes | Mode ombre et recommandation | *Baseline* et plafonds pilotes |
| `M3` **Défini** | Registre obligatoire, `Agent Owner`, `R1–R4` | `IAP`, `MCP Gateway`, `BPMN` ad hoc | `NHI` éphémères, `OBO`, `Intent Gates` | `EvalOps` CI/CD, `OTel`, *kill switch* | Coût par résultat + `Showback` |
| `M4` **Géré** | Détection auto d’étalement; audit `3LoD` | Durable généralisé; `A2A`; sortie `RPA` | `microVM`, `ACL` mémoire, `AISPM` | `SLO`, détection dérive, rejeu | `Chargeback`, routage `SLM` |
| `M5` **Optimisé** | *Governance-as-Code* continu (`NIST` /`ISO`) | Maillage `OASF` /`Event Mesh`; `Stade 4` | Révocation temps réel fédérée | Exercices périodiques repli `L0` | `ROI` ajusté du risque; portabilité |

*Tableau 15.4 — Modèle de maturité de l’entreprise agentique en cinq paliers (*`M1` *à* `M5`*).*

### 15.4.2 Feuille de route séquencée : horizons 90, 180 et 360 jours

Les trois horizons prescriptifs de **90, 180 et 360 jours** cadencent le passage de `M1` /`M2` vers `M3` puis `M4–M5` devant trois jalons de revue de l’`ARB` :

**Horizon 1 — Jours 0 à 90 : Assainissement, passerelle unique et pilotes en ombre (**`M1 → M2`**)**. Côté `EA`, installer le parrainage exécutif et le pôle `AI CoE` [393] [388], inventorier le *Shadow AI* et le parc `RPA` [369] [381], promulguer le tri `80/20` et les paliers `R1–R4`, et retenir deux à trois cas réversibles dotés d’un `Agent Owner` et d’une *baseline* chiffrée [372] [388]. Côté `SA`, étendre la zone d’atterrissage existante avec l’`AI Gateway` unifiée, poser la première façade `MCP` derrière une `ACL` [375] [379] [381] et lancer les pilotes en **Stade 1 (Ombre)** puis **Stade 2 (Recommandation)** avec un premier jeu `EvalOps` [387] [386]. *Jalon J90 (*`ARB 1`*)* : aucune nouvelle clé modèle hors passerelle et fidélité validée en mode ombre.

**Horizon 2 — Jours 90 à 180 : Plateforme** `IAP`**, identités** `NHI` **et action bornée (**`M2 → M3`**)**. Côté `EA`, rendre le registre central obligatoire, ouvrir le *Showback* `FinOps` par dossier réussi [369] [388] [381] et lancer le retrait des robots `RPA` sur systèmes désormais dotés d’API [376] [367]. Côté `SA`, livrer les *Golden Paths* de l’`IAP` (harnais `80/20`, `GitOps` conjoint, `OpenTelemetry`), remplacer les secrets statiques par des identités `NHI` avec `OBO` et `Intent Gates` [391] [378] [381], rendre `EvalOps` bloquant en intégration continue et promouvoir les cas `R2–R3` au **Stade 3 (Action bornée)** sur moteur durable ou sous-processus ad hoc `BPMN` [365] [374] [380] [386]. *Jalon J180 (*`ARB 2`*)* : 100 % de la production enregistrée sous `NHI` /`Agent Owner` et test réussi du repli `L0`.

**Horizon 3 — Jours 180 à 360 : Fédération inter-domaines, autonomie sous contrat et optimisation (**`M3 → M4/M5`**)**. Côté `EA`, passer au *Chargeback* comptable, systématiser les audits `3LoD` alignés sur `NIST AI RMF` et `ISO/IEC 42001` ainsi que sur les cadres juridiques du chapitre 12 [369] [394], piloter par le `ROI` ajusté du risque et tester la bascule multi-fournisseurs [378] [388]. Côté `SA`, ouvrir la délégation `A2A` signée entre domaines mûrs [367] [375], automatiser la détection d’étalement et de dérive [367] [369] [382], optimiser le routage `SLM` /`LLM` [371] [378] et promouvoir les flux éprouvés au **Stade 4 (Autonomie sous contrat)** avant de décommissionner les briques héritées [383] [380] [382]. *Jalon J360 (*`ARB 3`*)* : premier lot patrimonial retiré, coût unitaire stabilisé et revue `3LoD` conforme.

> **[Figure]**
> - Horizon 1 : J0-J90 (M1 -> M2)
> - Horizon 2 : J90-J180 (M2 -> M3)
> - Horizon 3 : J180-J360 (M3 -> M4/M5)
> - EA : Inventaire Shadow AI, Agent Owners, R1-R4 & Baseline
> - SA : AI/MCP Gateway, 1re ACL,
> - pilote Strangler Ombre / Reco
> - Jalon J90 (ARB 1)
> - Périmètre assaini
> - EA : Registre central, Showback,
> - sortie des bots RPA fragiles
> - SA : Golden Paths IAP, NHI/OBO,
> - EvalOps CI, Durable / BPMN
> - Jalon J180 (ARB 2)
> - Socle IAP en prod
> - EA : Chargeback, ROI ajusté,
> - réversibilité & audit 3LoD
> - SA : Autonomie sous SLO, fédération A2A/OASF, anti-sprawl
> - Jalon J360 (ARB 3) Portefeuille M4/M5 gouverné
> - valide
> - valide
> - ouvre H2
> - valide
> - valide
> - ouvre H3
> - atteint
> - atteint

*Fig. 59. – Trajectoire d’urbanisation ArchiMate et feuille de route séquencée sur 90, 180 et 360 jours*

> **Arbitrage EA / SA** — Interdire l’ouverture de la fédération `A2A` et du stade 4 d’autonomie avant la consolidation du socle `J90–J180` (registre central, `AI/MCP Gateway`, `NHI`, `EvalOps` et exécution durable) [393] [369] [381] [382]. L’`EA` conditionne les enveloppes trimestrielles (`ARB 1` à `ARB 3`) à la baisse de l’étalement et au retrait de dette `RPA`, tandis que le `SA` fournit des *Golden Paths* rendant la voie conforme plus rapide à emprunter que le contournement *Shadow AI* [367] [393] [369].

## Synthèse et clôture de l’ouvrage

Ce chapitre achève l’ouvrage en ancrant l’entreprise agentique dans le système d’information existant. La coexistence préserve l’autorité des moteurs `BPMN 2.0` grâce aux sous-processus ad hoc bornés, étend les couches `iPaaS` et de gestion d’API en plans de contrôle `MCP` /`A2A`, et confine puis résorbe les automates `RPA` fragiles derrière des couches anti-corruption [365] [367] [375] [379]. La migration *Strangler Fig* remplace les refontes risquées par une élévation réversible en quatre stades — ombre, recommandation, action bornée et autonomie sous contrat [383] [387] [380]. Enfin, les douze anti-patrons (`AP-01` à `AP-12`) et la feuille de route à 360 jours tracent un chemin vérifiable du palier `M1` aux paliers `M4–M5` pour déjouer les taux d’échec du secteur [368] [369].

Au terme des cinq parties de cet ouvrage, une règle constante s’impose : l’entreprise agentique fiable repose sur l’ingénierie des frontières plutôt que sur la seule puissance des modèles. En maintenant `80 %` du contrôle transactionnel, des identités et des règles impératives dans des mécanismes déterministes et

en confinant les `20 %` de liberté cognitive sous télémétrie, évaluation continue et contrat réversible, les architectes d’entreprise et de solutions transforment l’autonomie agentique en capacité industrielle durable [380] [370] [378] [388]. Les annexes qui suivent fournissent le glossaire bilingue normatif, le gabarit d’*Architecture Decision Record* (`ADR`) avec la liste de contrôle `EA` /`SA`, ainsi que les registres consolidés de bibliographie et d’ancrage.
