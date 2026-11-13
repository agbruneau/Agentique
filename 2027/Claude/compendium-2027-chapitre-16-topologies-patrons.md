# Chapitre 16 — Topologies et patrons

*Question directrice : comment répartir le travail entre plusieurs agents ?*

> **Version 2 — 11 novembre 2026.** État de référence : deux études comparatives en prépublication (documents financiers, mars 2026; mise à l'échelle des systèmes d'agents, avril 2026) et la documentation d'orchestration de Microsoft, d'Anthropic, d'OpenAI et de LangChain, consultée à cette date. Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [11] sont des pages primaires lues pour ce chapitre, dont trois par leur seul résumé; [12], marquée secondaire, n'a pas pu être lue. Les renvois « chapitre N » pointent vers la table des matières du compendium. Chapitre audité et révisé le 12 novembre 2026.

Dès qu'une tâche dépasse ce qu'un agent accomplit seul, la tentation est d'en ajouter d'autres : un planificateur, des spécialistes, un vérificateur. L'analogie avec une équipe humaine rend le geste naturel. Elle masque trois coûts. Chaque agent consomme des jetons pour ses consignes, son contexte et son raisonnement. Chaque passage de relais ajoute de la latence. Chaque frontière entre agents est un endroit où une information se perd et où une erreur se propage.

Une topologie répond à deux questions : qui décide de la prochaine étape, et qui voit quoi. Les patrons de ce chapitre en sont les réponses types.

Les mesures disponibles en 2026 ne désignent aucune topologie supérieure aux autres. Elles montrent que la bonne topologie se déduit de la structure de la tâche, que l'agent unique est le point de départ, et que la coordination s'achète en jetons, en secondes et en modes de panne.

---

## 16.1 Taxonomie : trois topologies et un axe adaptatif

### Trois topologies

Le relevé de Zhu et coll. classe les systèmes selon trois topologies de coordination (centralisée, décentralisée, hiérarchique) et un axe orthogonal d'adaptativité [12]. Son texte n'a pas pu être lu : la taxonomie est reprise de la carte thématique et d'un résumé de moteur de recherche, et les définitions qui suivent sont celles de l'usage courant, recoupées avec une étude expérimentale [2].

- **Centralisée.** Un orchestrateur reçoit la demande, distribue le travail et assemble les résultats. Les autres agents ne communiquent qu'avec lui.
- **Décentralisée.** Les agents échangent directement entre pairs, sans point de passage obligé. La forme extrême est le tous-vers-tous, avec des cycles de débat et un consensus.
- **Hiérarchique.** La centralisation se répète sur plusieurs niveaux : un superviseur délègue à des superviseurs intermédiaires, qui dirigent chacun leur équipe.

L'étude de Kim et coll. ajoute deux variantes [2]. Dans l'architecture **indépendante**, des agents isolés travaillent en parallèle et un agrégateur concatène leurs sorties, sans vote ni validation croisée. Dans l'architecture **hybride**, un orchestrateur coexiste avec une communication latérale limitée entre pairs.

### L'axe adaptatif

Chaque topologie peut être statique ou dynamique. Dans une structure statique, le code fixe qui parle à qui et dans quel ordre. Dans une structure dynamique, un modèle le décide à l'exécution.

Les fournisseurs tracent tous cette ligne, sous des noms différents. Anthropic oppose les workflows, où modèles et outils suivent des chemins de code prédéfinis, aux agents, où le modèle dirige lui-même son processus [4]. OpenAI distingue l'orchestration par le code de l'orchestration par le LLM, et note que la première est plus prévisible en vitesse, en coût et en performance [7]. Microsoft caractérise chacun de ses patrons par son mode de routage, déterministe ou dynamique [5].

Cet axe pèse lourd sur l'auditabilité. Une structure statique se lit dans le code; une structure dynamique ne se lit que dans les traces d'exécution (chapitre 33). Le chapitre 17 traite du placement du non-déterminisme dans un processus d'affaires; celui-ci s'en tient à la forme de la coordination.

### Un vocabulaire éclaté

Les mêmes patrons portent des noms différents selon l'éditeur; le tableau donne les correspondances relevées.

| Patron | Topologie | Qui choisit l'étape suivante | Autres noms |
|---|---|---|---|
| Pipeline | Centralisée, statique | Le code | sequential, prompt chaining, linear delegation [4][5] |
| Fan-out | Centralisée | Le code ou un initiateur | concurrent, parallelization, scatter-gather, map-reduce [4][5] |
| Routeur | Centralisée | Un classifieur | routing, router [4][6] |
| Superviseur | Centralisée, dynamique | Un agent orchestrateur | orchestrator-workers, subagents, agents as tools [4][6][7] |
| Hiérarchie | Hiérarchique | Un superviseur par niveau | supervisor-worker [1] |
| Planificateur à registre | Centralisée, dynamique | Un gestionnaire qui révise son plan | magentic, dynamic orchestration [5] |
| Débat | Décentralisée | Les pairs, par tours | group chat, roundtable, council, multiagent debate [5][8] |
| Réflexion | Boucle à deux rôles | Le vérificateur | evaluator-optimizer, maker-checker, critic loop [4][5] |
| Transfert, essaim | Décentralisée, dynamique | L'agent actif | handoff, triage, transfer [5][7] |

### La question du contexte

La documentation de LangChain place l'ingénierie du contexte au centre de la conception multi-agents : il s'agit de décider quelle information chaque agent voit. Elle ajoute que, avec un contexte infini et une latence nulle, on mettrait tout dans un seul prompt [6]. Répartir le travail entre agents est d'abord une technique de cloisonnement du contexte (chapitre 13), ensuite seulement une division du travail.

---

## 16.2 Superviseur et hiérarchie

### Le superviseur

Le superviseur place un agent au centre. Il analyse la demande, la découpe, confie chaque morceau à un spécialiste et assemble la réponse. Les spécialistes ne se parlent pas.

Anthropic le nomme orchestrator-workers et précise ce qui le sépare d'un fan-out : les sous-tâches ne sont pas prédéfinies, l'orchestrateur les détermine d'après l'entrée [4]. Les cadriciels le réalisent en exposant chaque spécialiste comme un outil de l'agent principal : subagents chez LangChain [6], agents as tools dans l'OpenAI Agents SDK, où l'agent principal garde la conversation et produit seul la réponse finale [7].

Trois propriétés le rendent attrayant.

**L'isolation du contexte.** Chaque spécialiste travaille dans sa propre fenêtre, avec ses propres outils, et ne renvoie qu'un résultat condensé. Le superviseur ne porte pas le détail des explorations.

**Un point de contrôle unique.** Les garde-fous communs et la réponse finale se logent à un seul endroit, ce que la documentation d'OpenAI donne comme critère de choix du patron [7].

**Une vérification centrale.** Dans l'étude de Kim et coll., les architectures sans vérification centralisée propagent davantage les erreurs. Mesurée sur les traces, l'amplification des erreurs par rapport à l'agent unique atteint 17,2 fois pour des agents indépendants, contre 4,4 fois avec un orchestrateur [2]. Le facteur mesuré au niveau de la tâche est bien plus faible (1,1 à 1,3), et l'effet n'est pas statistiquement significatif dans le modèle final : les auteurs attribuent les écarts davantage au surcoût de coordination qu'à la propagation des erreurs.

### Ce que la délégation exige

Le système de recherche multi-agents décrit par Anthropic en juin 2025 suit ce patron : un agent principal élabore une stratégie et lance en parallèle des sous-agents de recherche, puis rédige la synthèse [3]. Le retour d'expérience publié contient trois leçons transposables.

1. **Une consigne de délégation complète.** Chaque sous-agent doit recevoir un objectif, un format de sortie, des indications sur les outils et les sources, et des limites claires. Sans cela, les sous-agents dupliquent le travail ou laissent des trous.
2. **Un effort proportionné.** Une requête simple mobilise un agent et quelques appels d'outils; une recherche complexe peut mobiliser plus de dix sous-agents.
3. **Le choix du synchronisme.** L'agent principal attend la fin d'un lot de sous-agents avant de poursuivre. C'est simple à coordonner, mais cela crée un goulot. L'exécution asynchrone promet plus de parallélisme, au prix de difficultés de cohérence d'état.

Le même texte rappelle que les erreurs se composent : une défaillance mineure peut faire dérailler une exécution entière. La réponse retenue combine points de contrôle, relances automatiques et reprise au point d'arrêt, soit l'exécution durable du chapitre 18.

### La hiérarchie

Quand un superviseur dirige trop de spécialistes, son contexte enfle et son choix se dégrade. La hiérarchie répond en ajoutant des niveaux. Le banc d'essai sur les documents financiers en donne une forme concrète : un superviseur répartit les champs à extraire, réassigne ceux dont la confiance tombe sous un seuil de 0,85 et borne la réextraction à deux itérations [1]. Le superviseur y porte une boucle de contrôle de qualité bornée.

### Le planificateur à registre

Microsoft décrit une variante plus dynamique, l'orchestration « magentic » [5]. Un agent gestionnaire construit un registre de tâches, le révise à mesure que les spécialistes rapportent leurs résultats, et vérifie si la demande est satisfaite ou si le travail piétine. Le registre peut être présenté à un humain avant l'exécution (chapitre 22). Le patron vise les problèmes ouverts, sans chemin de solution connu. Il est déconseillé quand la tâche est simple, quand le temps presse ou quand le chemin est déterministe; son coût est le plus variable de tous.

### Ce que coûte le centre

Le passage obligé par le superviseur a un prix. Dans la comparaison que publie LangChain, une requête simple demande quatre appels de modèle avec des sous-agents, contre trois avec les autres patrons, parce que le résultat repasse par l'agent principal [6]. Dans l'étude de Kim et coll., l'architecture centralisée consomme en moyenne 27,7 tours par essai, contre 7,2 pour l'agent unique [2].

Le superviseur est aussi un point de défaillance unique, et son contexte grossit à chaque retour de spécialiste. Microsoft recommande de compacter le contexte entre agents, par résumé ou élagage [5].

---

## 16.3 Pipeline et fan-out

### Le pipeline

Le pipeline enchaîne les agents dans un ordre fixe. Chacun traite la sortie du précédent. Le choix de l'agent suivant est défini par le workflow et n'est pas laissé aux agents [5]. C'est le patron le plus statique, et le plus facile à auditer.

Il convient aux processus dont les étapes ont des dépendances linéaires claires et au raffinement progressif du type brouillon, révision, finition [5]. Anthropic y voit un échange de latence contre précision, chaque appel traitant une tâche plus simple, et souligne qu'on peut insérer des contrôles programmés entre les étapes [4].

Sa faiblesse est connue : une erreur en amont se propage vers l'aval. Microsoft déconseille le patron quand rien n'empêche les étapes suivantes de traiter une sortie dégradée, quand le travail exige des retours en arrière, ou quand les étapes tiendraient dans un seul agent [5].

### Le fan-out

Le fan-out lance plusieurs agents en même temps, puis réunit leurs résultats. Anthropic en distingue deux usages [4]. Le **découpage** répartit des sous-tâches indépendantes pour gagner du temps. Le **vote** exécute plusieurs fois la même tâche pour obtenir des sorties diverses et une confiance plus élevée.

Tout se joue à la fusion. Microsoft énumère les stratégies : vote ou règle de majorité pour une classification, fusion pondérée pour des recommandations notées, synthèse par un modèle pour concilier des résultats en un texte cohérent [5]. Dans le banc d'essai financier, un routeur répartit les sections du document entre trois extracteurs spécialisés, et un agent de réconciliation tranche les conflits par un vote pondéré par la confiance [1].

Une fusion sans validation est l'architecture « indépendante » de Kim et coll., celle dont l'amplification d'erreurs est la plus forte [2]. Un fan-out a donc besoin d'une étape de fusion qui vérifie, non d'une simple concaténation.

Le patron est à éviter quand les agents doivent bâtir sur le travail des autres, quand aucune stratégie de résolution des conflits n'existe, ou quand les quotas de modèle rendent le parallélisme illusoire [5]. Microsoft range aussi parmi les antipatrons le partage d'un état modifiable entre agents concurrents, source de données incohérentes (chapitre 14).

### Le routeur

Le routeur est le cas limite : une étape de classification envoie l'entrée vers un spécialiste, ou vers quelques-uns dont on synthétise les réponses [4][6]. Anthropic en donne un usage économique : diriger les requêtes simples vers un petit modèle et les difficiles vers un modèle plus capable [4]. Le chapitre 44 traite ce routage de modèles : aucun routeur n'y domine dans la seule comparaison indépendante lue. Quand le bon agent se reconnaît dès l'entrée, Microsoft préfère ce routage à un transfert dynamique [5].

Ces trois formes se combinent : Microsoft conseille de ne pas forcer un workflow entier dans un seul patron [5]. Quand le déclencheur est un événement plutôt qu'un appel, elles se transposent sur un flux (chapitre 19).

---

## 16.4 Débat, réflexion, autocorrection

Ces patrons partagent une idée : confronter une sortie à un autre regard avant de la livrer. Ils diffèrent par le nombre de regards et par ce qui arrête la boucle.

### Le débat

Dans le débat multi-agents, plusieurs instances de modèle proposent chacune une réponse et un raisonnement, puis les confrontent pendant plusieurs tours jusqu'à une réponse commune. L'article fondateur de Du et coll. rapporte, selon son résumé, une amélioration du raisonnement mathématique et stratégique et de la validité factuelle, avec une réduction des hallucinations, sur des modèles en boîte noire [8].

L'évaluation de Smit et coll. tempère ce résultat. Selon son résumé, les systèmes de débat, dans leur forme d'alors, ne surpassent pas de façon fiable d'autres stratégies plus simples, dont l'autocohérence et les ensembles de chaînes de raisonnement; ils sont plus sensibles aux hyperparamètres et difficiles à optimiser, même si un réglage du niveau d'accord entre agents peut les améliorer nettement [9]. Ces deux articles datent de 2023 et de 2024; leurs conclusions n'ont pas été revérifiées sur les modèles de 2026.

Les mesures de Kim et coll. situent le coût : l'architecture décentralisée, à débat et consensus, consomme 26,1 tours par essai en moyenne, et son amplification d'erreurs mesurée sur les traces est de 7,8 fois, entre l'orchestrateur et les agents indépendants [2].

Microsoft range le débat dans l'orchestration en conversation de groupe, où un gestionnaire décide qui parle [5]. Les agents y sont en général en lecture seule : ils discutent, ils ne modifient pas de systèmes. Le fil unique donne transparence et auditabilité, et un humain peut y participer. La maîtrise se perd vite avec le nombre : la page suggère de s'en tenir à trois agents ou moins.

### La réflexion

La boucle de réflexion est un débat réduit à deux rôles. Un agent produit, un autre évalue selon des critères définis et renvoie un retour précis; le premier révise. Anthropic la nomme evaluator-optimizer et la réserve aux cas où les critères d'évaluation sont clairs et où le raffinement itératif apporte une valeur mesurable [4].

Microsoft formule trois exigences [5] : des critères d'acceptation assez nets pour que le vérificateur décide de façon cohérente; un plafond d'itérations; un repli quand le plafond est atteint, par exemple l'escalade vers un réviseur humain ou la livraison du meilleur résultat avec un avertissement.

### L'autocorrection mesurée

Le banc d'essai financier chiffre le compromis. Son architecture réflexive enchaîne extraction, vérification (format, cohérence entre champs, ancrage dans la source), critique et correction, avec trois itérations au plus. Elle obtient la meilleure précision des quatre architectures comparées, et aussi le coût et la latence les plus élevés [1]. Les chiffres figurent à la section 16.6.

La vérification gagne donc à être un rôle distinct de la production, avec ses propres critères. Elle ne suffit pas à elle seule : la taxonomie MAST fait de la vérification de la tâche l'une de ses trois catégories d'échec [10] (chapitre 21). Le chapitre 18 traite de la validation indépendante avant une action irréversible.

---

## 16.5 Essaim et pair-à-pair

### Le transfert

Dans le transfert (handoff), l'agent actif juge s'il peut traiter la demande ou s'il doit la céder à un agent mieux placé. Le contrôle passe en entier d'un agent à l'autre; un seul agent travaille à la fois [5]. Dans l'OpenAI Agents SDK, un agent d'aiguillage transfère la conversation à un spécialiste, qui répond directement à l'utilisateur [7]. La différence avec le superviseur tient à qui garde la conversation.

Le patron convient quand le spécialiste requis n'apparaît qu'en cours de traitement. L'exemple type est le soutien à la clientèle : un agent de triage traite les cas courants, cède les autres à un agent technique ou de facturation, et peut passer la main à un employé [5].

Microsoft signale deux risques : la boucle de transferts sans fin et un parcours imprévisible [5]. Selon la comparaison de LangChain, sur une requête répétée, les transferts économisent des appels, puisque le spécialiste reste actif : cinq appels sur deux tours, contre huit avec des sous-agents. Sur une question qui touche plusieurs domaines, ils coûtent davantage : sept appels ou plus, contre cinq [6]. Ces chiffres viennent de scénarios illustratifs d'un éditeur, non d'une mesure indépendante.

### L'essaim

Un essaim est un ensemble d'agents qui se passent le travail par transferts, sans superviseur. Aucun agent n'a de vue d'ensemble; la coordination émerge des décisions locales. Il n'y a pas d'orchestrateur à écrire, mais la difficulté se reporte sur l'observabilité : reconstituer qui a décidé quoi exige une trace complète de chaque transfert (chapitre 33).

Multiplier les canaux ne s'amortit pas de soi. L'architecture hybride de Kim et coll., qui ajoute des échanges latéraux à un orchestrateur, est la plus coûteuse de l'étude : 44,3 tours par essai en moyenne, six fois plus que l'agent unique [2].

### Le pair-à-pair imposé

Une situation échappe au choix. Quand les agents appartiennent à des plateformes ou à des organisations différentes, aucun superviseur commun n'est possible : nul ne détient l'autorité sur tous, ni l'accès à tous les contextes. La topologie décentralisée est alors une donnée. C'est le terrain d'A2A, qui standardise la délégation entre agents opaques l'un pour l'autre (chapitre 6), de la découverte par registres (chapitre 8) et des réseaux B2B fédérés (chapitre 45).

Il en découle une règle de composition, qui relève du raisonnement plus que de la mesure : pair-à-pair entre domaines, par protocole; topologie centralisée à l'intérieur d'un domaine, où une seule équipe maîtrise les agents, leurs contextes et leurs permissions. La frontière de domaine coïncide souvent avec une frontière de sécurité, critère que Microsoft retient pour justifier plusieurs agents [5]. Les chaînes de délégation qui traversent ces frontières sont traitées aux chapitres 29 et 30.

---

## 16.6 Compromis coût, précision, latence

### Un banc d'essai chiffré

L'étude de Kulkarni et Kulkarni compare quatre architectures sur 10 000 dépôts réglementaires américains (formulaires 10-K, 10-Q et 8-K), avec 25 types de champs à extraire et cinq modèles [1]. Le tableau donne les résultats du modèle le plus performant de l'étude, Claude 3.5 Sonnet.

| Architecture | F1 | Exactitude par document | Latence médiane | Coût par document | Jetons par document |
|---|---|---|---|---|---|
| Pipeline séquentiel | 0,903 | 0,648 | 38,7 s | 0,187 $ | 146 160 |
| Fan-out avec fusion | 0,914 | 0,672 | 21,3 s | 0,221 $ | 172 930 |
| Hiérarchique | 0,929 | 0,718 | 46,2 s | 0,261 $ | 203 120 |
| Réflexive | 0,943 | 0,758 | 74,1 s | 0,430 $ | 321 610 |

**Aucune architecture ne domine.** Le pipeline est le moins cher, le fan-out le plus rapide, la boucle réflexive la plus précise. Chaque point de F1 gagné se paie.

**La hiérarchie offre le meilleur compromis.** D'après les tableaux, elle atteint 98,5 % du F1 de l'architecture réflexive pour 60,7 % de son coût. L'introduction de l'article annonce 97,7 % et 60,9 %, et son résumé un F1 de 0,921, qui est celui de GPT-4o; ces écarts ne sont pas expliqués.

**La queue de latence compte.** Au 99e centile, l'architecture réflexive prend 247,3 secondes, contre 68,3 pour le fan-out.

**L'exactitude par document reste modeste.** Même la meilleure architecture ne rend tous les champs corrects que pour trois documents sur quatre environ. La topologie ne dispense pas d'une révision humaine en aval (chapitre 22).

### L'optimisation pèse autant que la topologie

Les ablations de la même étude portent sur l'architecture hiérarchique [1]. Un routage à deux niveaux de modèles ramène le coût de 0,261 $ à 0,127 $ par document, pour un F1 de 0,912. La configuration qui combine cache sémantique, routage de modèles et relance adaptative atteint un F1 de 0,924 pour 0,148 $ et 30,2 secondes : moins chère et plus rapide que le pipeline naïf, et plus précise que lui.

Microsoft donne la même consigne : attribuer à chaque agent un modèle à la mesure de sa tâche et mesurer la consommation de jetons par agent et par exécution [5]. Les chapitres 40 et 44 développent cette discipline.

### Le classement change sous la charge

L'étude fait varier le volume sur une grappe fixe de huit nœuds [1].

| Documents par jour | Pipeline | Fan-out | Hiérarchique | Réflexive |
|---|---|---|---|---|
| 1 000 | 0,903 | 0,914 | 0,929 | 0,943 |
| 50 000 | 0,894 | 0,906 | 0,907 | 0,898 |
| 100 000 | 0,886 | 0,898 | 0,891 | 0,871 |

L'architecture réflexive, la meilleure à faible volume, devient la moins bonne à 100 000 documents par jour : les délais d'attente tronquent ses boucles de correction. Le pipeline se dégrade le moins. Les seuils dépendent de l'infrastructure, les auteurs le soulignent. Le constat demeure : un patron validé en pilote doit être réévalué au volume de production.

### Les jetons comme variable cachée

Anthropic rapporte que ses agents consomment environ quatre fois plus de jetons qu'une conversation, et ses systèmes multi-agents environ quinze fois plus. Sur une évaluation interne de recherche, son système multi-agents dépasse de 90,2 % l'agent unique; sur le banc d'essai BrowseComp, la quantité de jetons utilisée explique à elle seule 80 % de la variance de performance [3].

Ces chiffres viennent d'un billet de fournisseur. Ils suggèrent qu'une part du gain des architectures multi-agents tient à ce qu'elles dépensent plus de jetons, en parallèle et dans des fenêtres séparées. Selon le même texte, elles ne se justifient que pour des tâches dont la valeur couvre ce coût.

Une réserve vaut pour toute la section : le banc d'essai financier est une prépublication qui porte sur un seul domaine, des modèles de 2024 et des tarifs de janvier 2025 [1]. Les rapports entre architectures se transposent mieux que les valeurs absolues.

---

## 16.7 Quand un seul agent suffit

### La consigne des éditeurs

Les fournisseurs, qui ont intérêt à vendre de l'orchestration, recommandent pourtant la retenue. Anthropic conseille de chercher la solution la plus simple et de n'ajouter de complexité que si elle améliore les résultats [4]. Microsoft pose trois niveaux (appel direct au modèle, agent unique avec outils, orchestration multi-agents), demande de retenir le plus bas qui répond au besoin, et tient l'agent unique outillé pour le bon choix par défaut dans bien des cas d'entreprise [5]. LangChain écrit qu'un agent unique bien outillé suffit souvent [6].

### Ce que disent les mesures

L'étude de Kim et coll. donne à cette prudence une base expérimentale : 260 configurations, six bancs d'essai, cinq architectures et trois familles de modèles, avec outils, prompts et budget de calcul alignés pour isoler l'effet de l'architecture [2]. Sur l'ensemble, l'écart moyen des systèmes multi-agents par rapport à l'agent unique est de −0,3 %, avec un intervalle de confiance à 95 % qui va de −58,7 % à +77,2 %. La moyenne ne dit rien; tout dépend de la tâche.

| Banc d'essai | Écart le plus favorable | Écart le plus défavorable relevé |
|---|---|---|
| Finance-Agent (raisonnement décomposable) | Centralisée, +80,8 % | Aucun écart négatif |
| BrowseComp-Plus | Décentralisée, +9,2 % | Indépendante, environ −35 % |
| WorkBench | Décentralisée, +5,6 % | Environ −11 % |
| SWE-bench Verified | Hybride, −2,1 % | Indépendante, −14,9 % |
| Terminal-Bench | Indépendante, +1,7 % | Centralisée, −19,2 % |
| PlanCraft (planification séquentielle) | Hybride, −39,1 % | Indépendante, −70,0 % |

Trois régularités ressortent de l'article.

**La structure de la tâche décide.** Une tâche décomposable en sous-problèmes indépendants profite fortement de la coordination. Une tâche de planification séquentielle, où chaque étape dépend de l'état laissé par la précédente, se dégrade dans toutes les architectures multi-agents.

**Un plafond de capacité.** Quand l'agent unique réussit déjà au-delà d'environ 45 % sur une tâche, la coordination donne des rendements décroissants ou négatifs.

**Un compromis entre outils et coordination.** Les tâches riches en outils pénalisent davantage les architectures coûteuses en coordination; avec quatre outils ou moins, l'effet est négligeable.

Les auteurs présentent ces résultats comme des tendances; SWE-bench Verified et Terminal-Bench reposent sur vingt instances seulement.

Le retour d'expérience d'Anthropic concorde : les systèmes multi-agents conviennent mal aux domaines où tous les agents doivent partager le même contexte ou dont les sous-tâches sont très interdépendantes, et le texte range la plupart des tâches de programmation dans ce cas [3].

### Les raisons légitimes d'en ajouter

Les pages lues convergent sur une courte liste [3][5][6] :

- la tâche est large et se parallélise;
- elle dépasse la fenêtre de contexte d'un agent;
- l'agent a trop d'outils et choisit mal;
- des frontières de sécurité distinctes s'imposent entre agents;
- des équipes indépendantes développent et entretiennent chacune leur agent.

Les deux dernières tiennent à la sécurité et à l'organisation.

Avant d'ajouter un agent, une solution intermédiaire mérite examen : l'agent unique qui charge à la demande des consignes et des connaissances spécialisées, que LangChain classe parmi ses patrons sous le nom de skills [6] (chapitre 13).

---

## 16.8 Grille de choix

La fiche des annexes du relevé de Zhu et coll. signale un arbre de décision pour le choix d'un patron [11]; il n'a pas été lu. La séquence qui suit est une synthèse des sources de ce chapitre.

1. **Un agent unique outillé suffit-il ?** Le mesurer d'abord. S'il réussit déjà bien, la coordination a peu de chances d'ajouter quelque chose [2].
2. **Les étapes sont-elles connues d'avance ?** Si oui, une structure statique est plus prévisible et plus auditable [5][7].
3. **Les sous-tâches sont-elles indépendantes ?** Si oui, fan-out ou superviseur. Sinon, pipeline ou agent unique [2][5].
4. **Existe-t-il un critère d'acceptation vérifiable, et l'erreur coûte-t-elle cher ?** Boucle de réflexion bornée [4][5].
5. **Les agents relèvent-ils d'autorités différentes ?** Pair-à-pair par protocole (chapitre 6).
6. **Le patron tient-il au volume de production ?** Le vérifier sous charge [1].

| Caractéristique de la tâche | Patron indiqué | Signal d'alerte |
|---|---|---|
| Étapes fixes, dépendances linéaires | Pipeline | Erreur amont non détectée |
| Sous-tâches indépendantes et connues | Fan-out avec fusion vérifiée | État partagé, quotas |
| Catégories d'entrée distinctes | Routeur | Classification incertaine |
| Sous-tâches indépendantes, imprévisibles | Superviseur | Contexte du superviseur qui enfle |
| Problème ouvert, plan à construire | Planificateur à registre | Piétinement, coût imprévisible |
| Expertise qui émerge en cours de route | Transfert | Boucles de transferts |
| Qualité critique, critères nets | Réflexion bornée | Latence, dégradation sous charge |
| Étapes fortement couplées, contexte commun | Agent unique | Fenêtre de contexte saturée |

Le choix du cadriciel vient ensuite; la plupart mettent en œuvre plusieurs de ces patrons (chapitre 20).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Nombre d'agents | Un agent outillé | Tâche parallélisable, contexte saturé, trop d'outils, frontière de sécurité ou d'équipe |
| Structure | Statique, fixée par le code | Sous-tâches imprévisibles : superviseur dynamique |
| Topologie dans un domaine | Centralisée | Expertise qui émerge en conversation : transfert |
| Topologie entre domaines | Pair-à-pair par protocole | Plateforme unique sous une seule autorité |
| Fusion d'un fan-out | Étape de validation ou de vote | Résultats indépendants, sans agrégation requise |
| Vérification | Rôle distinct de la production, critères écrits | Tâche à faible enjeu |
| Boucles | Plafond d'itérations et repli défini | — |
| Débat | Trois agents au plus, en lecture seule | Animation par un humain |
| Modèle par agent | Proportionné à la tâche de l'agent | Faible volume : un seul modèle |
| Validation du patron | Mesure contre l'agent unique, puis sous charge | — |

---

## Points à retenir

- Une topologie répond à deux questions : qui décide de l'étape suivante, et qui voit quoi. Répartir le travail, c'est d'abord cloisonner le contexte.
- Trois topologies (centralisée, décentralisée, hiérarchique) et un axe adaptatif suffisent à situer les patrons, malgré un vocabulaire qui varie d'un éditeur à l'autre.
- Aucune topologie ne domine. Sur six bancs d'essai, l'écart moyen entre multi-agents et agent unique est à peu près nul, et va de +80,8 % à −70,0 % : la coordination aide les tâches décomposables et nuit aux tâches séquentielles couplées.
- L'agent unique outillé est le point de départ; les éditeurs eux-mêmes le recommandent.
- Le superviseur vaut par son contrôle central, mais ajoute des appels et un goulot. Une délégation sans objectif, format ni limites produit doublons et lacunes.
- La boucle réflexive donne la meilleure précision au coût et à la latence les plus élevés, et se dégrade le plus vite sous charge; la hiérarchie offre le meilleur compromis mesuré en traitement de documents financiers.
- Routage de modèles, cache et relances adaptatives déplacent le coût autant que le choix de topologie.
- Entre organisations, le pair-à-pair s'impose : la topologie suit les frontières d'autorité.

---

## Sources

Pages primaires lues le 11 novembre 2026 ([1] à [3] et [5] à [7] relues le 12 novembre 2026) :

1. [Kulkarni et Kulkarni — Benchmarking Multi-Agent LLM Architectures for Financial Document Processing (arXiv 2603.22651v1)](https://arxiv.org/html/2603.22651v1) — prépublication.
2. [Kim et coll. — Towards a Science of Scaling Agent Systems (arXiv 2512.08296v3)](https://arxiv.org/html/2512.08296v3) — prépublication; résumé et première moitié du texte.
3. [Anthropic — How we built our multi-agent research system, 13 juin 2025](https://www.anthropic.com/engineering/built-multi-agent-research-system) — billet de fournisseur.
4. [Anthropic — Building effective agents, 19 décembre 2024](https://www.anthropic.com/engineering/building-effective-agents) — billet de fournisseur.
5. [Microsoft, Azure Architecture Center — AI agent orchestration patterns, page datée du 12 février 2026](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
6. [LangChain — Multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent)
7. [OpenAI Agents SDK — Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)
8. [Du et coll. — Improving Factuality and Reasoning in Language Models through Multiagent Debate (arXiv 2305.14325)](https://arxiv.org/abs/2305.14325) — résumé seulement.
9. [Smit et coll. — Should we be going MAD? (arXiv 2311.17371)](https://arxiv.org/abs/2311.17371) — résumé seulement.
10. [Cemri et coll. — Why Do Multi-Agent LLM Systems Fail? (arXiv 2503.13657v3)](https://arxiv.org/abs/2503.13657) — résumé seulement.
11. [Zenodo — annexes du relevé de Zhu et coll.](https://zenodo.org/records/19774440) — fiche du dépôt; l'archive n'a pas été ouverte.

Source secondaire :

12. [Zhu et coll. — LLM-Based Multi-Agent Orchestration: A Survey of Frameworks, Communication Protocols, and Emerging Patterns](https://www.preprints.org/manuscript/202604.2147) — prépublication non lue (accès refusé); taxonomie reprise de la carte thématique et de résumés de recherche.

## Limites de ce chapitre

- Le relevé [12], appui principal prévu par la table des matières, n'a pas été lu : le 12 novembre 2026, sa page refuse toujours l'accès, et une recherche ne trouve aucune parution dans *Future Internet*. La liste d'auteurs diffère entre la prépublication et la fiche Zenodo. Les définitions des topologies viennent de l'usage courant et de [2], non du relevé.
- Les pages ont été lues, puis relues pour six d'entre elles, au moyen d'un outil qui en condense le contenu. Les chiffres cités concordent d'une lecture à l'autre, mais n'ont pas été recoupés avec les tableaux d'origine.
- [1] se contredit par endroits, notamment sur les gains d'optimisation qu'il annonce; ce sont les valeurs de ses tableaux qui sont citées.
- [2] n'a été lu que sur sa première moitié; le tableau de la section 16.7 ne garantit pas qu'aucune architecture ne fasse pire que l'écart relevé.
- [1] et [2] sont des prépublications; [3] à [7] sont des documents d'éditeurs qui décrivent leurs propres produits.
- La description de l'essaim et la règle « pair-à-pair entre domaines, centralisé à l'intérieur » relèvent de la connaissance générale et du raisonnement.
- Le routeur et le planificateur à registre s'ajoutent à la table des matières; l'essaim est traité avec le transfert.
- Aucune donnée d'adoption des patrons en entreprise n'est citée, faute de source vérifiée.
