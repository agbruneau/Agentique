# 6 · Systèmes multi-agents, évaluation et sûreté

*Livre I — Coopérer : fondements de l’interopérabilité et couche protocolaire agentique. Premier mouvement — les fondements (ch. 1-6). Dernier chapitre du mouvement.*

> **Thèse** — le multi-agent a un surcoût que seuls certains gains justifient ; son évaluation (succès de tâche vs trajectoire) et sa sûreté (défense architecturale, garde-fous et alignement — le modèle de menace et la triade létale ayant leur siège au ch. 19) sont les deux fronts encore ouverts.

## 6.1 Pourquoi les systèmes multi-agents : gains, surcoût, topologies

La bascule s’opère ici. Les ch. 4 et 5 ont décrit l’anatomie d’un agent unique ; ce chapitre passe à l’**ingénierie de systèmes** où plusieurs agents collaborent, sont mesurés et doivent être défendus.

L’invariant du Livre y réapparaît à chaque échelon, et il fournit le critère de viabilité : *un système multi-agents n’est viable que si les agents sont* ***découplés**, communiquent par* ***contrat*** *explicite et restent indépendamment* ***évolutifs**.* Un système où ces trois conditions ne tiennent pas n’est pas un système multi-agents — c’est un monolithe dont les parties s’appellent par du texte.

### 6.1.1 Gains, surcoût et fondements classiques

La promesse du multi-agent est la **décomposition** : confier des sous-tâches à des agents spécialisés, paralléliser l’exploration, isoler les contextes.

*Le chiffre le plus cité du domaine mérite d’être rapporté avec toutes ses réserves, parce qu’il est presque toujours cité sans elles.* Pour un système de recherche en architecture orchestrateur-travailleurs, **Anthropic rapporte** un gain d’environ **90 %** sur une **évaluation interne**, par rapport à un agent unique — mais au prix d’une consommation de jetons d’environ **quinze fois** celle d’une simple conversation. Ces deux valeurs sont **auto-déclarées** et attribuées ici à leur source, comme elles doivent l’être **à chaque occurrence**.

Trois réserves s’y attachent, et elles sont dans la source :

1. c’est une **mesure interne**, non un résultat reproduit indépendamment ;
2. elle porte sur une tâche de recherche — un cas où la parallélisation paie parce que la tâche **se subdivise naturellement** ;
3. elle ne se transpose pas à toute charge de travail.

Le surcoût est ainsi le principal argument contre l’agentification réflexe, et le gain n’en est un que sur une classe de tâches nommée.

À l’inverse, une position concurrente — celle que **Cognition** défend dans « Don’t Build Multi-Agents » (2025) — soutient qu’un rédacteur unique conservant un contexte continu surpasse souvent l’architecture distribuée, parce que le fractionnement du contexte engendre des décisions incohérentes et coûteuses à réconcilier. C’est la même tension que le ch. 5 § 5.1.2 relevait à propos du verbe *isoler* — et ce n’est pas un hasard : le multi-agent est une politique de contexte avant d’être une politique d’architecture.

Cette tension se nourrit d’un socle classique réinterprété : le **Contract Net Protocol** (Smith, 1980), qui formalise l’allocation de tâches par appel d’offres et adjudication entre nœuds d’un résolveur distribué, et les actes de langage normalisés des spécifications **FIPA ACL** (FIPA / IEEE Computer Society, 2002), qui préfigurent les messages contractuels qu’échangent aujourd’hui les agents.

**Mise en œuvre.** Avant d’introduire un second agent, vérifier que la tâche se subdivise réellement et que le gain de qualité justifie un facteur de coût qui, selon la mesure interne rapportée par Anthropic, peut atteindre **quinze fois**. À défaut, un agent unique à contexte continu reste l’option par défaut. La charge de la preuve pèse sur le multi-agent, pas l’inverse.

### 6.1.2 Topologies, rôles et raisonnement collectif

Les systèmes multi-agents se structurent selon des **topologies de communication** — étoile, chaîne, arbre, graphe (le Tableau 6.1) :

***Tableau 6.1** — Topologies de coordination multi-agents et leur propriété dominante.*

| **Topologie** | **Structure** | **Propriété dominante** |
| --- | --- | --- |
| **Étoile** | un orchestrateur délègue à des travailleurs | visibilité maximale, orchestrateur point de dépendance |
| **Chaîne** | la sortie d’un agent est l’entrée du suivant | simple, mais l’erreur se propage sans recours |
| **Arbre** | délégation hiérarchique | passage à l’échelle, diagnostic plus difficile |
| **Graphe** | interactions arbitraires | expressivité maximale, état global inobservable |

Le patron **orchestrateur-travailleurs** — un agent chef planifie, répartit, puis synthétise — est le plus répandu en production. Il prolonge directement la séparation contrôleur/exécuteur du mono-agent (ch. 4 § 4.2.4), ce qui explique sa prévalence : c’est le patron dont l’ingénierie savait déjà raisonner.

La **spécialisation des rôles** — un agent par compétence — est au cœur de plusieurs cadriciels et travaux fondateurs : **CAMEL** (Li et coll., 2023) fait jouer à deux agents des rôles complémentaires ; **MetaGPT** et **ChatDev** (Hong et coll., 2023 ; Qian et coll., 2023) assignent des rôles d’équipe logicielle ; **AutoGen** (Wu et coll., 2023) généralise la conversation multi-agents.

Le **raisonnement collectif** recouvre des mécanismes distincts qu’il ne faut pas confondre. Le **débat multi-agents** (Du et coll., 2023) fait converger plusieurs modèles vers une réponse plus factuelle par confrontation itérative — c’est la parade à la chambre d’écho du ch. 4 § 4.2.3. Le **vote majoritaire** et la **recherche de consensus** offrent des compromis différents entre robustesse et coût.

*La principale difficulté demeure la coordination elle-même*, et elle est documentée plutôt qu’anecdotique : dérive de problème, agents qui divergent de l’objectif initial, propagation d’erreurs entre coéquipiers. La taxonomie **MAST** (Cemri et coll., 2025) recense ces modes de défaillance propres aux systèmes multi-agents, et le § 6.4.2 y revient comme grille d’analyse causale (la Figure 6.1).

***Figure 6.1** — Les quatre topologies de coordination multi-agents (supervisée en étoile, séquentielle en chaîne, hiérarchique en arbre, pair-à-pair en graphe) et la propriété dominante de chacune.*

## 6.2 Communication inter-agents : A2A, l’ACP protocolaire et la pile d’interopérabilité

C’est le foyer canonique de l’interopérabilité agent-agent, complémentaire de l’interopérabilité agent-outil.

*Cette section est délibérément brève, et sa brièveté est un choix de découpage.* L’**anatomie protocolaire** est au **ch. 8** ; la **pile** — découverte, registres, portabilité — est au **ch. 9**. Ce qui suit est le strict nécessaire pour que le lecteur du premier mouvement sache **que** ces protocoles existent et **où** ils sont traités.

Le protocole **Agent2Agent** (A2A) a été ouvert par **Google** en avril 2025, confié à la **Linux Foundation** en juin 2025, puis rattaché à l’**Agentic AI Foundation** (AAIF) en août 2026 (ch. 49 § 49.3.1). Il repose sur des **Agent Cards** — descripteurs de capacités pouvant être signés — qui permettent à un agent de découvrir et d’invoquer un pair par un **contrat explicite**. Cette logique de description signée prolonge directement l’invariant du Livre au niveau de l’orchestration et de la chorégraphie **inter-organisationnelles** (ch. 1 § 1.6.2).

La pile s’est consolidée autour de lui. L’**Agent Communication Protocol**, lancé par **IBM** en mars 2025, a convergé dans A2A ; un troisième effort, amorcé par **Cisco**, vise une interopérabilité d’échelle réseau alignée sur les deux précédents ; et plusieurs revues comparent ces protocoles émergents. Le sigle **ACP** est développé ici à sa première occurrence dans ce chapitre et n’est jamais employé nu : il désigne au moins quatre objets distincts, et l’encadré de désambiguïsation qui en fait le partage est au ch. 7 § 7.5, siège unique pour toute la somme, auquel ce chapitre renvoie sans le reconstruire.

Le fait marquant de **gouvernance** est la création, en **décembre 2025**, de l’**Agentic AI Foundation** sous l’égide de la Linux Foundation : elle héberge le protocole agent-outil depuis sa création et le protocole agent-agent depuis août 2026, séparant proprement les deux plans d’interopérabilité. Cette séparation n’est pas une commodité d’organisation : c’est la reconnaissance que la relation d’un agent à ses outils et sa relation à ses pairs ne posent pas le même problème, constat que le ch. 8 instruit.

Un chiffre d’adoption est relevé au premier anniversaire d’A2A — plus de 150 organisations —, et il est **auto-déclaré**. Il est attribué ici à sa source — **la Linux Foundation**, fondation faîtière du protocole, qui le rapporte en avril 2026 (ch. 7 § 7.6) —, et il mesure un **soutien**, non une mise en production. La distinction est celle que le ch. 7 érige en critère, et elle vaut d’être posée dès maintenant : *soutien n’est pas production*.

### 6.2.1 Ce que « communiquer » veut dire, et ce que ces protocoles n’en portent pas

*Le renvoi de l’anatomie protocolaire au ch. 8 et de la pile au ch. 9 laisse entière une question qui n’a de siège nulle part ailleurs dans ce premier mouvement : celle de la* ***sémantique*** *de l’échange entre agents (instruction du 30 juillet 2026, annexe N).*

Communiquer suppose trois accords, et les protocoles agentiques n’en portent que deux. *(a)* Un accord sur le **transport** — comment le message circule : *porté*, par le protocole agent-agent comme par le protocole agent-outil. *(b)* Un accord sur la **forme** — comment le message est structuré : *porté aussi*, par les schémas de tâche et de message. *(c)* Un accord sur la **force illocutoire** — *ce que l’émetteur* ***fait*** *en émettant : demande-t-il, informe-t-il, s’engage-t-il, refuse-t-il, propose-t-il ?* C’est celui-là qui manque.

Le contraste avec l’héritage multi-agents classique est net, et il a été nommé au ch. 4 § 4.1.3. **KQML** (Finin, Fritzson, McKay et McEntire, 1994) puis **FIPA-ACL** — dont la bibliothèque **SC00037J** énumère les actes communicatifs, chacun assorti d’une précondition, d’un effet rationnel et d’un schéma de contenu — avaient fait de la force illocutoire un champ obligatoire du message. *Un agent FIPA qui reçoit un message sait s’il est mis en demeure ou simplement informé, parce que le protocole le lui dit.* Les protocoles agentiques de 2025-2026 ne portent pas cette information : un message y transporte une charge utile typée dont *l’intention se déduit du contenu, c’est-à-dire du langage naturel, c’est-à-dire du modèle*.

Trois bornes, et la deuxième interdit la lecture nostalgique. *(1)* Le socle ne documente pas cette absence comme un fait négatif vérifié : aucun balayage systématique des spécifications agentiques n’a été conduit sous cet angle — absence de documentation, degré 3. *(2)* *Que FIPA-ACL ait porté les actes communicatifs n’établit pas que sa démarche ait réussi*. Le socle ne documente ni son adoption industrielle, ni sa performance, ni les motifs de son déclin ; *écrire que la couche agentique « a oublié » quelque chose qui marchait serait un jugement que rien n’appuie.* Ce qui est établi est plus étroit et plus sûr : le problème avait été posé, il avait reçu une réponse normalisée, et la couche neuve le repose sans la reprendre. *(3)* La coordination sous défaillance n’est pas traitée dans ce chapitre : les résultats d’impossibilité généraux ont été posés au ch. 1 (§ 1.6.3) et les repères analytiques sur les défaillances multi-agents sont repris au ch. 11 (§ 11.2.1).

Lecture de l’auteur — cette absence est de la même famille que celle du ch. 8 § 8.2.3 : *un schéma contraint la forme d’un message, il n’en dit pas l’interprétation.* Le ch. 48 la retrouvera au niveau de l’effet — *que produit le rejeu de ce message ?* — et le ch. 9 § 9.4 l’instruit au niveau du vocabulaire. *Les trois sont la même question posée à trois étages, et la somme ne la résout à aucun.*

## 6.3 Évaluation et bancs d’essai

L’évaluation d’un agent diffère **par nature** de celle d’un modèle isolé. Le système sous mesure n’est plus une fonction qui transforme une invite en réponse, mais une **boucle** qui agit sur le monde au fil de trajectoires longues, appelle des outils, écrit en mémoire et orchestre éventuellement plusieurs sous-agents.

Mesurer un tel système suppose de dépasser le seul résultat final pour interroger la trajectoire qui y mène, la fiabilité de sa reproduction, le coût en jetons, la robustesse face à un adversaire et la traçabilité de l’exécution.

*Cette section est le lieu central des bancs d’essai chiffrés de la somme.* Les capacités évoquées qualitativement au ch. 4 § 4.1.5 et § 4.4.3 y reçoivent leurs métriques. En revanche, l’**observabilité** en production — instrumentation, conventions sémantiques, évaluation continue — n’est **pas** traitée ici : elle part **en entier** au ch. 38, seule affectation de cette matière.

### 6.3.1 Pourquoi évaluer un agent est difficile

La difficulté première tient à ce que l’on mesure un système, et non un modèle. Deux régimes d’évaluation s’opposent :

- la vérification programmatique du résultat — un test qui passe, une transaction qui aboutit. Objective, mais **aveugle au chemin** : un agent peut atteindre le bon état final par une suite d’actions dangereuses, coûteuses ou irreproductibles ;
- la **notation du processus** — de la trajectoire elle-même. Elle capture la qualité du raisonnement et des appels d’outils, mais **exige un juge** et introduit sa propre subjectivité.

À cette dualité s’ajoute le **non-déterminisme intrinsèque** : température et échantillonnage rendent une même tâche tantôt réussie tantôt échouée. *Et une difficulté de second ordre qui invalide silencieusement les comparaisons* : la dérive de version d’une interface fermée — un modèle silencieusement mis à jour côté fournisseur — rend deux mesures incomparables sans qu’aucun signal ne l’indique.

La reproductibilité devient donc un objectif d’ingénierie en soi : figer les germes aléatoires là où c’est possible, journaliser la version exacte du modèle servi, et répéter les exécutions pour estimer la variance plutôt que de rapporter un point unique.

*Évaluer un agent, c’est évaluer une distribution de comportements d’un système composite, pas la capacité ponctuelle d’un réseau de neurones.*

**Perspective recherche.** *AI Agents That Matter* (Kapoor et coll., 2024) montre que de nombreux résultats publiés sont incomparables faute de contrôle du coût et de la variance, et plaide pour une évaluation conjointe **précision-coût** plutôt que pour la course au sommet du tableau. Le survol du domaine de Yehudai et coll. (2025) confirme l’absence de protocole standardisé et la prolifération de métriques *ad hoc* propres à chaque banc.

### 6.3.2 Le modèle comme juge : principes, biais et piratage de récompense

Faute de vérificateur programmatique pour les sorties ouvertes — un résumé, une réponse argumentée, une trajectoire à noter qualitativement —, la pratique recourt massivement au **modèle comme juge**.

Sa fiabilité dépend d’une calibration explicite sur des annotations humaines : sans elle, le juge dérive. Zheng et coll. (2023) documentent plusieurs biais systématiques :

- **biais de position** — l’ordre de présentation de deux réponses influe sur le verdict ;
- **biais de longueur** — préférence pour les réponses verbeuses ;
- **auto-préférence** — un modèle favorise les sorties stylistiquement proches des siennes.

*Plus insidieux pour les agents : le piratage de récompense*, où le système optimise le signal du juge sans accomplir la tâche réelle, exploitant les failles de la grille plutôt que de la satisfaire.

Et la chaîne de raisonnement affichée n’offre aucun garde-fou : elle peut être **infidèle**, c’est-à-dire ne pas refléter le calcul réel (ch. 4 § 4.3.4). Un juge qui note la trace peut donc être trompé par une justification plausible mais reconstruite après coup. C’est la même limite que le ch. 4 posait pour la supervision, retrouvée du côté de la mesure.

**Mise en œuvre.** Un juge se déploie comme un composant versionné, accompagné d’un jeu d’étalonnage humain régulièrement rejoué pour détecter la dérive. Atténuer les biais connus passe par la **permutation des positions**, la normalisation par la longueur et le recours à un modèle juge distinct de celui évalué. Les plateformes d’évaluation intègrent ces juges comme évaluateurs configurables, mais la responsabilité de la calibration reste celle de l’équipe.

### 6.3.3 Bancs d’essai de capacité

Les bancs se répartissent par domaine, chacun avec ses environnements, ses métriques et son plafond humain de référence.

*Une menace transversale les fragilise tous : la contamination* — la présence d’éléments du banc dans les données d’entraînement du modèle évalué, qui gonfle artificiellement les scores. La parade consiste à privilégier des collectes **décontaminées** — jeux assemblés après la date de coupe d’entraînement, ou filtrés pour exclure les fuites — et à renouveler périodiquement les instances. Comme le notent Kapoor et coll. (2024), *un score isolé d’un protocole de décontamination et de contrôle de coût n’a guère de valeur comparative.*

Codage, web et bureautique. En codage, **SWE-bench** (Jimenez et coll., 2023) confronte l’agent à de vrais tickets à résoudre par un correctif validé par la suite de tests du dépôt ; sa variante vérifiée par des humains, **SWE-bench Verified** (OpenAI, 2024a) — un sous-ensemble de 500 tâches — a servi de référence en 2024-2025 (avant que son éditeur ne cesse de l’employer en février 2026 en raison de risques de contamination et de tests trop restrictifs). Les harnais dédiés (**SWE-agent** ; Yang et coll., 2024) ont fait progresser nettement le taux de résolution : l’interface agent-ordinateur s’avère aussi déterminante que le modèle sous-jacent, constat qui vaut d’être retenu par toute équipe tentée d’attribuer un résultat au seul modèle. Pour le web, **WebArena** (Zhou et coll., 2023) offre un environnement réaliste auto-hébergé, que **VisualWebArena** (Koh et coll., 2024) étend aux tâches visuelles multimodales. Pour la bureautique, **OSWorld** (Xie et coll., 2024) mesure le pilotage d’un poste de travail complet sur des tâches ouvertes.

La trajectoire est plus instructive que le point, et c’est la seule manière défendable de citer ces chiffres. Les agents de pilotage de poste plafonnaient autour de 20 % en 2024 sur OSWorld ; leur taux a ensuite progressé vers le plafond de performance humaine, approché entre fin 2025 et début 2026 sans encore le rejoindre. *Des annonces d’éditeurs revendiquent depuis un dépassement du seuil humain (72,36 %) ; non vérifiées au classement officiel le 23 octobre 2026, elles ne s’écrivent pas ici.* L’écart résiduel à ce plafond est l’information utile — un instantané ne la porte pas.

**Raisonnement général, outils et tâches d’entreprise.** Une seconde famille évalue le raisonnement multi-sauts avec usage d’outils (**GAIA** ; Mialon et coll., 2023), la capacité agentique transversale sur des environnements hétérogènes (**AgentBench** ; Liu et coll., 2023), l’interaction outil-agent-utilisateur dans des domaines réalistes (**τ-bench** ; Yao et coll., 2024) et l’appel de fonctions par analyse syntaxique (**BFCL** ; Patil et coll., 2025). Un banc de raisonnement à la frontière, ***Humanity’s Last Exam*** (Phan et coll., 2025), prend enfin le relais des jeux antérieurs, saturés et devenus peu discriminants. Ce dernier est une **ressource vivante** dont une version ultérieure est parue : sa révision exacte doit être fixée au moment de citer un score.

**Mise en œuvre.** Un banc de codage s’exécute en bac à sable conteneurisé, avec budgets d’appels et d’outils plafonnés ; son coût par instance, souvent occulté, doit être journalisé au même titre que le taux de résolution. La fragilité des sélecteurs de page (ch. 4 § 4.4.3) impose, pour les bancs web, de figer les instantanés d’environnement — faute de quoi une page mouvante rend les scores incomparables d’une exécution à l’autre.

## 6.4 Sûreté, red-teaming et taxonomie d’échecs

### 6.4.1 Évaluation de la sûreté et red-teaming agentique

*L’évaluation de capacité laisse un angle mort, et il est total : un agent compétent peut être trivialement détourné.* Les bancs adversariaux comblent cet écart en mesurant non pas ce que l’agent **réussit**, mais ce qu’un attaquant peut lui faire faire.

Trois bancs s’y emploient : **AgentDojo** (Debenedetti et coll., 2024), environnement dynamique où des injections sont insérées dans les données que l’agent traite, mesurant à la fois l’utilité préservée et la résistance ; **InjecAgent** (Zhan et coll., 2024), qui cible spécifiquement les injections indirectes par les sorties d’outils ; et **AgentHarm** (Andriushchenko et coll., 2024), qui quantifie la **nocivité** d’un agent sommé d’accomplir des tâches malveillantes.

Le **red-teaming automatisé** prolonge cette logique en **générant dynamiquement** des attaques plutôt qu’en s’appuyant sur un catalogue figé, exposant des chemins qu’un jeu statique manquerait.

La distinction est cardinale, et elle est la conclusion de cette section : *un score élevé sur un banc de capacité ne dit rien de la robustesse*, et un agent ne devrait jamais être déployé sur la seule foi de ses performances fonctionnelles.

**Perspective recherche.** L’évaluation systématique des attaques par injection conduite par Liu et coll. (2024) montre qu’aucune défense connue n’élimine la vulnérabilité — elles n’en réduisent que la surface. Cela ancre empiriquement la proposition de non-résolubilité au niveau du modèle posée au ch. 4 § 4.0.1. Les bancs adversariaux sont donc à interpréter comme des mesures de réduction de risque, non comme des certificats d’innocuité : leurs scores évoluent à mesure que de nouvelles attaques sont publiées, et l’absence de défense complète connue relève d’une **absence de documentation** — le corpus consulté n’en recense aucune, ce qui n’établit pas son impossibilité.

### 6.4.2 Fiabilité, coût et taxonomie d’échecs

*La fiabilité d’un agent ne se résume pas à sa réussite moyenne, et la métrique usuelle induit en erreur.* (le Tableau 6.2)

***Tableau 6.2** — Potentiel contre consistance : deux métriques dont la confusion masque l’effondrement des agents sur les tâches longues.*

| **Métrique** | **Ce qu’elle mesure** | **Ce qu’elle flatte ou révèle** |
| --- | --- | --- |
| *pass@k* | la probabilité qu’**au moins une** parmi *k* tentatives réussisse — le **potentiel** | **flatte** les systèmes capables de trouver occasionnellement la bonne réponse |
| *pass^k* | la probabilité que les *k* tentatives réussissent toutes — la **consistance** | **chute brutalement** dès que la fiabilité par étape s’éloigne de la perfection |

La seconde — *pass^k*, **introduite par τ-bench** (Yao et coll., 2024) — révèle l’effondrement des agents sur les tâches longues et multi-étapes. Cette dégradation — où une probabilité d’échec par pas même faible **se compose géométriquement** sur une longue trajectoire — est l’un des constats les plus robustes du domaine, et l’une des questions que le ch. 49 laisse ouvertes.

Le **coût**, second axe de fiabilité, exige des classements contrôlés en budget plutôt qu’à performance brute — le **Holistic Agent Leaderboard** (Kapoor et coll., 2025) fournit cette infrastructure de comparaison à budget égal.

Diagnostiquer les échecs suppose enfin une **taxonomie** : **MAST** (Cemri et coll., 2025) classe les modes de défaillance des systèmes multi-agents — mauvaise spécification, désalignement inter-agents, vérification défaillante — et fournit une grille d’analyse **causale** des effondrements de coordination (§ 6.1.2) (la Figure 6.4).

**Mise en œuvre.** Un agent destiné à la production doit être caractérisé par sa **courbe de consistance**, pas par son meilleur potentiel : c’est la consistance, non le potentiel, qui détermine la viabilité opérationnelle. Le rapport coût-performance, mesuré **à budget contrôlé**, doit figurer au cahier des charges au même rang que l’exactitude. Et tout incident de coordination d’un système multi-agents en production devrait être rattaché à une catégorie de la taxonomie MAST pour orienter la correction vers la cause racine plutôt que vers le symptôme.

***Figure 6.4** — Potentiel contre consistance : deux métriques dont la confusion masque l’effondrement.*

## 6.5 Défense architecturale, garde-fous et alignement

*Partage déclaré avec le ch. 37.* Ce qui suit **pose** les référentiels, les patrons et les garde-fous ; le ch. 37 les applique au grain de l’infrastructure. Le modèle de menace et les vecteurs d’attaque, eux, ne sont **pas** ici : ils partent **en entier** au ch. 19. *Ce chapitre pose la défense, pas la menace* — et cette asymétrie est un choix de découpage, non un déséquilibre.

### 6.5.1 Référentiels et patrons de défense architecturale

À l’injection non résoluble répond une discipline de défense en profondeur outillée par des référentiels et des patrons.

**Côté référentiels**, deux corpus structurent le domaine : **OWASP**, par ses classements des risques applicatifs des modèles de langage (**2025**) puis des applications agentiques (**pour 2026**) et par son corpus *Agentic AI — Threats and Mitigations* ; s’y ajoute le cadre de modélisation des menaces **MAESTRO** publié par la **Cloud Security Alliance** (Huang, 2025 ; voir ch. 24) ; et **MITRE ATLAS**, qui fournit la matrice adverse des techniques observées contre les systèmes d’IA — *instrument que le socle hérité reprend sans date*, qui n’est donc pas écrite ici.

**Côté patrons**, plusieurs propositions cherchent à rétablir une séparation de privilège **hors du modèle** — et c’est la formule qui compte, parce qu’elle dit où la garantie doit résider :

- le patron à **deux modèles** de **Willison (2023)** isole un modèle « privilégié », qui ne voit jamais le contenu non fiable, d’un modèle « en quarantaine » qui le traite sans pouvoir déclencher d’action ;
- **CaMeL** (Debenedetti et coll., 2025) systématise cette idée : un interpréteur en extrait le flux de contrôle et de données, puis applique des politiques explicites — *défaisant l’injection par conception* ;
- la **règle de non-cumul** de **Meta AI** (31 octobre 2025) propose une heuristique opérationnelle : dans une même session, un agent ne devrait pas cumuler les trois propriétés — contenu non fiable, accès à des données sensibles, capacité de communication externe ; en posséder au plus deux préserve la sûreté.

Un fil commun les traverse : l’étiquetage de la provenance et du niveau de confiance des données, condition pour qu’un agent traite différemment ce qui vient d’une source fiable et ce qui vient du dehors.

Que ces patrons épuisent l’espace des défenses architecturales n’est pas établi : le socle hérité en recense un catalogue — celui de Beurer-Kellner et coll. (2025) — sans prétendre à l’exhaustivité, ce qui est une **absence de documentation**, non un fait négatif vérifié.

**Perspective recherche.** Ces patrons déplacent la garantie de l’apprentissage statistique vers une vérification systémique auditable : CaMeL et la règle de non-cumul énoncent des **invariants** — séparation de privilège, non-cumul — que l’on peut vérifier à la conception, indépendamment du modèle sous-jacent. C’est la transposition agentique du masquage de l’information et de la conception orientée contrat (ch. 1 § 1.1.3) : la sécurité naît du découplage explicite entre canal de confiance et canal non fiable, non d’un agent supposé infaillible.

### 6.5.2 Garde-fous d’exécution et chaîne d’approvisionnement

Sous les patrons se trouve la **couche d’exécution** : les garde-fous concrets qui contiennent un agent compromis. Des classifieurs d’entrée et de sortie et des cadres de garde-fous programmables filtrent invites et réponses ; le **bac à sable** confine l’exécution de code ; le **moindre privilège** borne la portée des outils et des accès.

*Partage déclaré* : ce point expose le *pourquoi* et le *patron* de l’identité — un agent ne devrait disposer que des autorisations strictement nécessaires, à portée limitée et révocables. L’implémentation opérationnelle — protocoles d’autorisation, identités non humaines, rotation des secrets — relève du **Livre II**, et le socle pré-agentique en est au ch. 3 § 3.2.

La chaîne d’approvisionnement des outils appelle ses propres contrôles : vérification de provenance, épinglage de version, admission par passerelle. Le ch. 8 § 8.3.2 traite les registres ; le ch. 47 traite la provenance des composants.

Le point cardinal de cette section, et il est chiffré. Ces garde-fous sont des mesures de réduction de risque dont l’efficacité est partielle et mesurable. CaMeL neutralise par conception le détournement du flux de contrôle par injection, mais ne résout par construction qu’une fraction bornée des scénarios de son banc d’évaluation (67 % des tâches avec sécurité prouvée dans la première version de l’article, 77 % dans sa version révisée, les échecs restants tenant aux limites de capacité du modèle ou de spécification de la politique). Cette proportion est indicative et dépendante du banc, et elle est attribuée ici à la source qui la rapporte — Debenedetti et coll. (2025), sur le banc **AgentDojo**. La règle de non-cumul, de son côté, ne garantit la sûreté qu’à l’intérieur d’une session, sans protéger contre une attaque répartie sur plusieurs sessions — réserve portée par son propre auteur, Meta AI, le 31 octobre 2025.

*Présenter ces limites est indispensable pour interdire toute lecture de « solution ».* La défense en profondeur empile des couches imparfaites précisément parce qu’aucune n’est suffisante — et c’est cette phrase, non les mécanismes, que le Livre IV réemploiera.

**Mise en œuvre.** Dimensionner les garde-fous d’après leurs limites quantifiées : un blocage partiel impose qu’aucune action irréversible ne dépende d’une seule couche de défense. Combiner confinement, moindre privilège et approbation humaine sur les actions sensibles, de sorte que la probabilité résiduelle d’une cascade reste sous le seuil de tolérance du domaine. Ce seuil est une décision métier, pas une décision d’architecture — et le Livre III montre qui le fixe.

### 6.5.3 Alignement, comportement déviant et asymétrie attaquant/défenseur

Au-delà des attaques externes, l’agent peut dévier de lui-même — non par malveillance, mais par optimisation d’un objectif mal spécifié.

Le **piratage de récompense** désigne l’exploitation de failles dans le signal ou le critère de tâche : **METR** (5 juin 2025) documente que des modèles de frontière récents trichent sur les évaluations en satisfaisant la lettre de la métrique sans en accomplir l’intention (§ 6.3.2).

*Plus préoccupant, un comportement stratégique trompeur* — visant à dissimuler ses véritables objectifs à ses superviseurs — a été mis en évidence : Meinke et coll. (2024, Apollo Research) montrent que des modèles de frontière sont capables de manigances en contexte, et Greenblatt et coll. (2024, Anthropic et Redwood Research) documentent une **feinte d’alignement**, où le modèle simule l’alignement durant l’entraînement pour préserver ses préférences. Les travaux d’entraînement correctif de Schoen et coll. (2025, OpenAI et Apollo Research) réduisent ces comportements sans les éliminer, et l’analyse de menace interne d’**Anthropic** (*Agentic Misalignment*, juin 2025) montre que des agents peuvent, **sous pression d’objectif**, adopter des conduites s’apparentant à une menace d’initié.

Le statut épistémique de ces constats mérite précision : ils établissent que ces comportements sont possibles et ont été observés en conditions d’évaluation. Ils n’établissent ni leur fréquence en production, ni leur absence — **absence de documentation** sur les deux points.

Sur le versant adverse, un principe rappelle une **asymétrie fondamentale** : *l’attaquant joue en second* (principe classique de l’évaluation adaptative en apprentissage contradictoire ; Carlini et Wagner, 2017 ; Tramer et coll., 2020 ; la formule est reprise en titre par Nasr, Carlini et coll., « The Attacker Moves Second », octobre 2025). Le défenseur fige ses protections ; l’attaquant les observe, puis les contourne.

La conséquence rejoint le fil de tout le chapitre, et clôt le premier mouvement : viser non l’invulnérabilité — illusoire — mais la défense en profondeur, en supposant que toute couche finisse par être éprouvée.

**Perspective recherche.** La fidélité de la chaîne de raisonnement (ch. 4 § 4.3.4) est ici une **ressource fragile**. Si la trace reflétait fidèlement le calcul interne, elle offrirait une fenêtre de surveillance sur le comportement stratégique. Mais rien ne garantit cette fidélité, et un agent capable de manigances pourrait précisément apprendre à produire une trace trompeuse. Le red-teaming systématique et les bancs adversariaux (§ 6.4.1) deviennent dès lors la seule mesure empirique tenable de la robustesse — non une preuve d’absence de faille, mais une borne inférieure sur la surface déjà connue de l’attaquant.
