# 3 Concepts et définitions

« Agent », « orchestrateur » ou « autonomie » ne désignent pas la même chose d’une équipe ou d’un fournisseur à l’autre. Ce chapitre fixe le sens des termes employés dans tout le cadre, distingue les flux de travail des agents et les agents interactifs des agents ambiants, puis précise ce qu’un agent n’est pas. Le glossaire de l’annexe E complète ces définitions.

## 3.1 Définitions normatives

Les définitions du tableau 7 font foi dans tout le cadre et dans les documents qui s’y rattachent (section 1.4); pour les niveaux d’autonomie et les paliers d’outils, les tableaux 28 et 31 font foi, et les échelles ci-dessous en sont un résumé. Lorsqu’une norme ou une loi définit déjà un terme, le cadre reprend sa définition et la précise au besoin.

*Tableau 7 — Définitions normatives du cadre*

| **Terme** | **Définition** | **Référence** |
| --- | --- | --- |
| **Agent** | D’après ISO/IEC 22989 (paraphrase vérifiée par la fiche de catalogue et des sources secondaires, non au texte de la norme, section 1.7), entité automatisée qui perçoit son environnement, y réagit et agit pour atteindre ses buts. Pour le cadre, système logiciel qui poursuit un objectif en dirigeant lui-même sa boucle « raisonner, agir, observer » au moyen d’un modèle, d’outils et d’un état, sous un niveau d’autonomie déclaré. | ISO/IEC 22989:2022; oneM2M TR-0081, v0.2.0 (version préliminaire)**[59, 60]**; cadre |
| **Système d’IA** | Système automatisé conçu pour fonctionner à différents niveaux d’autonomie, qui peut faire preuve d’une capacité d’adaptation après son déploiement et qui, pour des objectifs explicites ou implicites, déduit, à partir des entrées qu’il reçoit, la manière de générer des sorties (prédictions, contenus, recommandations, décisions) pouvant influencer des environnements physiques ou virtuels. Le cadre considère tout agent comme un système d’IA. | Règlement (UE) 2024/1689 (RIA), art. 3(1)**[61, 62]** |
| **Déployeur** | Personne ou organisme qui utilise un système d’IA sous sa propre autorité. Si le RIA s’applique à elle (art. 2), l’entreprise l’est pour les agents qu’elle exploite, y compris ceux qu’elle achète (section 12.4). | RIA, art. 3(4)**[61]** |
| **Outil** | Capacité exposée à un agent (fonction, API, action), décrite par un contrat typé et classée P0 à P3 au catalogue. Un outil ne choisit pas lui-même, au moyen d’un modèle, les actions qu’il exécute, même s’il conserve l’état d’une tâche ou demande une précision (Tasks, élicitation MCP); une cible qui les choisit est un agent (section 6.2). Dans MCP, fonction exécutable que le modèle choisit d’appeler. | MCP**[63]**; cadre |
| **Ressource** | Donnée contextuelle identifiée par une URI, qu’un serveur met à la disposition d’un agent. Pour le cadre, sa lecture n’a aucun effet de bord; toute opération qui modifie un état est un outil. | MCP**[63, 64]**; cadre |
| **Invite** *(prompt)* | Instructions et contenu en langage naturel fournis à un modèle. Dans MCP, la primitive `Prompts` désigne des gabarits d’invite réutilisables qu’expose un serveur. | MCP**[63]** |
| **Flux déterministe** | Suite d’étapes dont le code fixe le chemin (graphe ou machine à états). Quand certaines étapes appellent un modèle, c’est un flux de travail assisté par IA : le chemin reste fixé par le code, et le flux est inscrit au registre avec le niveau qui correspond à ses écritures déclenchées par une sortie de modèle (section 3.2). | Anthropic *(workflows)***[6]** |
| **Orchestrateur, exécutant** | L’orchestrateur décompose une demande, affecte les sous-tâches, suit l’état, gère la reprise et consolide les résultats; l’exécutant, agent ou outil, traite une sous-tâche bornée. Le cadre limite la délégation à deux niveaux (choix du cadre, EXIG-ORC-04, section 7.2). | Cadre; Anthropic**[6]** |
| **Transfert** *(handoff)* | Cession explicite du contrôle d’une session, avec le contexte utile et le mandant, d’un agent source à un agent cible mieux qualifié; l’agent source se retire. | OpenAI**[66]** |
| **Chorégraphie** | Coordination sans composant central : chaque agent réagit aux événements d’un bus et publie les siens, ce qui complique le suivi et expose aux cycles. | Microsoft**[67]** |
| **Carte d’agent** *(Agent Card)* | Document lisible par machine, défini par A2A, par lequel un agent décrit son identité, ses interfaces, ses compétences et ses exigences de sécurité; en A2A 1.0, il est publié à `/.well-known/agent-card.json`. | A2A 1.0**[68]** |
| **Contrat d’agent** | Engagement formel d’un agent : carte d’agent, entrées et sorties typées, niveau d’autonomie, limites, niveaux de service et voie d’escalade. Outils et événements ont leurs équivalents; tout contrat est versionné au catalogue d’entreprise. | Cadre (EXIG-INT-03, section 6.1; section 6.8) |
| **Mandant** | Personne ou application au nom de laquelle une tâche est exécutée ou, en l’absence de mandant humain, agent initiateur de la chaîne. Le mandant d’une chaîne de délégation est toujours l’entité d’origine; un agent intermédiaire n’y apparaît que comme acteur (`act`). Les droits du mandant bornent ceux de l’agent, et son identité accompagne chaque appel de bout en bout. | Cadre |
| **Délégation** | Attribution à un agent de droits bornés en portée et en durée pour agir au nom d’un mandant, l’agent restant identifiable. Le cadre interdit l’usurpation, où l’agent devient indiscernable du mandant. Par extension, envoi d’une tâche à un autre agent, avec des droits effectifs au plus égaux à l’intersection des droits du mandant, de la portée de l’agent au registre et de la portée nécessaire à la tâche, sans élargissement d’un saut à l’autre (EXIG-IAM-10). | RFC 8693, § 1.1**[69]**; cadre |
| **Jeton délégué** | Jeton d’accès de courte durée, obtenu par échange de jetons, qui identifie le mandant (`sub`) et l’agent acteur (`act`) et ne vaut que pour un seul service; sa portée ne s’élargit jamais d’un saut à l’autre. | RFC 8693, 8707 et 9068**[69, 71, 72]**; cadre (durée courte, audience unique, portée jamais élargie) |
| **Passerelle d’agents** | Point d’application des politiques placé devant les outils et les agents : authentification, autorisation, garde-fous, plafonds, injection des secrets et journalisation de chaque appel. | Cadre; NIST SP 800-207**[73]** |
| **Passerelle de modèles** | Passage obligatoire entre les agents et les fournisseurs de modèles : clés, routage, cache, repli, quotas, mesure des jetons et filtrage des données sortantes. | Cadre (section 5.2) |
| **Catalogue d’entreprise** | Source unique des contrats des interfaces joignables (outils, cartes d’agent, événements), avec version et empreinte approuvées, palier et propriétaire. À distinguer du catalogue des protocoles (section 6.3). | Cadre (section 6.8) |
| **Registre** | Inventaire faisant autorité des agents et des serveurs MCP : une fiche par élément, avec parrain nommé, finalité, classe de risque, niveau d’autonomie et état de cycle de vie. | Cadre (section 11.4); GOVERN 1.6**[74]** |
| **Garde-fou** | Contrôle automatisé qui filtre ou bloque une entrée, une sortie ou une action d’un agent. Un garde-fou probabiliste réduit un risque sans l’éliminer. | Microsoft**[9]**; cadre |
| **Humain dans la boucle (HITL), sur la boucle (HOTL), hors de la boucle** *(human in the loop, human on the loop, human out of the loop)* | HITL : une personne approuve chaque action en écriture avant son exécution. HOTL : elle supervise, traite les exceptions et peut interrompre, sans approbation préalable. Hors de la boucle : aucune intervention pendant l’exécution; restent la surveillance automatisée, l’audit et l’arrêt. | AWS; IMDA (Infocomm Media Development Authority, Singapour), section 1.1.3, pour la gradation de l’implication humaine, les sigles HITL et HOTL n’y figurant pas**[75, 76]** |
| **Niveau d’autonomie** | Plafond, déclaré au registre, de ce qu’un agent fait sans approbation humaine : N1 à N4, NX étant interdit; N0 qualifie un flux, non un agent (définitions ci-dessous). | Cadre (section 8.1) |
| **Palier d’outil** | Risque propre à un outil, de P0 à P3, attribué au catalogue après revue et jamais déduit des déclarations du serveur (définitions ci-dessous). | Cadre (section 8.3) |
| **Compensation** | Action métier qui neutralise l’effet d’une étape déjà exécutée quand un flux échoue, par exemple un remboursement. Elle ne rétablit pas forcément l’état initial et doit pouvoir être réessayée sans danger. | Microsoft**[77]** |
| **Idempotence** | Propriété d’une opération dont la répétition produit le même effet qu’une seule exécution. Une clé d’idempotence, identique à chaque nouvel essai, permet de reconnaître une requête déjà reçue. | IETF; Temporal**[78, 79]** |
| **Exécution durable** | Persistance de l’état d’une exécution à chaque transition (point de contrôle), qui permet de reprendre après une panne ou un déploiement. Elle n’empêche pas à elle seule qu’un effet soit rejoué : il faut aussi l’idempotence. | Temporal; LangGraph**[80, 81, 82]** |
| **Session** | Au sens des EXIG-SEC-04 et EXIG-SEC-06 : la tâche racine et tout ce qui en dérive (sous-tâches, délégations A2A, reprises depuis un point de contrôle, événements publiés au titre de la tâche). Son état (contenu non fiable consommé, données sensibles consultées) est tenu par la passerelle dans un magasin à cohérence forte; un état illisible impose le refus. Un contexte vierge exclut tout rechargement de mémoire, de point de contrôle ou d’artefact étiqueté postérieur à la contamination. | Cadre (section 9.6) |
| **Environnement serveur** | Tout environnement d’exécution autre qu’un poste de développement individuel sans justificatif de production : développement partagé, préproduction et production, mais aussi poste de travail, navigateur, mobile ou périphérie dès qu’un agent y agit sur des systèmes ou des données de l’entreprise. | Cadre (EXIG-ARC-01) |

### Les deux échelles du cadre

Ces échelles s’appliquent partout; le chapitre 8 en précise les contrôles.

**Niveaux d’autonomie**

- **N0 Automatisation déterministe** : aucun choix d’action laissé à un modèle; le code fixe chaque pas (flux codé, règles, RPA, API), et un modèle peut y transformer une donnée sans choisir l’action. N0 qualifie un flux, non un agent : repère de base hors portée agentique, il entre dans la portée dès qu’il appelle un agent ou qu’un agent l’appelle, et suit alors les contrôles de cet agent (section 1.2).
- **N1 Consultatif** : l’agent lit, analyse, recommande, rédige; aucun effet en écriture; l’humain exécute; outils P0 et P1 seulement.
- **N2 Exécution approuvée** : l’agent prépare; chaque action en écriture attend une approbation explicite (humain dans la boucle).

- **N3 Autonomie bornée et supervisée** : sur une tâche demandée par une personne, l’agent exécute seul les actions P2 sous des seuils déclarés, dans un domaine de conception opérationnel documenté (ODD, *operational design domain*); il escalade les exceptions à une personne désignée, qui les traite dans un délai borné déclaré à la fiche; une action P3 exige une approbation hors bande, une à une (humain sur la boucle, et dans la boucle pour les actions P3).
- **N4 Autonomie étendue sous ODD certifié** : l’agent exécute seul des tâches déclenchées sans demande d’une personne (événement, horaire), dans un ODD certifié; la passerelle lit l’origine de la tâche, attribut posé par l’orchestrateur ou par le courtier, et refuse à un agent qui n’est pas N4 toute écriture sans approbation au titre d’une tâche ainsi déclenchée; l’humain est hors de la boucle d’exécution, mais sur la boucle de gouvernance; une action P3 est toujours approuvée hors bande, une à une; ce niveau n’est permis qu’à un agent de classe faible, sur décision du comité (EXIG-CON-02).
- **NX Autonomie non bornée** : l’agent fixe ses objectifs, modifie ses permissions ou exécute du code hors contraintes. Ce niveau est interdit.

Le niveau est un plafond déclaré au registre, à la manière du « certificat d’autonomie » de Feng, McDonald et Zhang**[83]**; il est distinct de la topologie (le nombre d’agents) et de la capacité du modèle. Plafond par classe de risque : celui que fixe EXIG-CON-02 selon la classe attribuée au tableau 46 (section 12.1).

**Paliers d’outils** : **P0** lecture publique (un outil de recherche publique dont la requête est en texte libre reste un outil d’envoi au sens de l’EXIG-SEC-06); **P1** lecture interne ou sensible; **P2** écriture réversible, ou compensable vers un état métier équivalent, à impact borné; **P3** action critique, externe ou irréversible, même si une compensation est déclarée, jamais exécutée seule par un agent (tableau 31, EXIG-AUT-08).

**À RETENIR**

Quatre axes à ne pas confondre : classe de risque de l’agent (section 12.1), niveau d’autonomie, palier de l’outil et topologie (chapitre 7). Pour un appel, le contrôle appliqué est l’union des contrôles qu’exigent ces axes, calculée par la passerelle selon l’EXIG-AUT-10 (section 8.4).

## 3.2 Flux de travail ou agent?

Cette section distingue deux façons de faire travailler un modèle, qui n’appellent ni les mêmes contrôles ni les mêmes coûts.

Selon Anthropic, un flux de travail orchestre le modèle et les outils par des chemins de code prédéfinis, alors qu’un agent dirige lui-même son processus et l’usage de ses outils. Les deux reposent sur la même brique, le modèle augmenté *(augmented LLM)*, doté de capacités de recherche, d’outils et de mémoire**[6]**. Un agent fonctionne en boucle : la méthode ReAct fait alterner raisonnement et actions sur des sources externes, ce qui a réduit les hallucinations par rapport à la chaîne de pensée seule et amélioré le taux de réussite sur les tâches interactives (ALFWorld, WebShop) dans les essais de ses auteurs, au prix d’une exactitude parfois moindre sur les questions à plusieurs étapes (HotpotQA)**[84]**.

### Quand chacun convient

La question décisive est simple : qui doit choisir le prochain pas, le code ou le modèle? La section 7.3 en fait un arbre de décision.

- **Code ou règle (N0).** Si une fonction suffit, on écrit la fonction plutôt qu’un agent**[85]**.
- **Appel direct au modèle.** Pour une transformation en un seul passage : classer, résumer, traduire**[9]**.
- **Flux de travail assisté par IA.** Quand le chemin est connu d’avance, réglementé ou audité. C’est le patron par défaut du cadre; il est inscrit au registre avec le niveau qui correspond à ses écritures déclenchées par une sortie de modèle (sans approbation : N3 et ODD).

- **Agent unique outillé.** Quand les étapes dépendent de ce que l’agent découvre en chemin, pour des requêtes variées dans un même domaine.
- **Système multiagent.** Quand il faut protéger le contexte, paralléliser des pistes réellement indépendantes, spécialiser les outils ou séparer des frontières de sécurité, et seulement sur preuve mesurée de gain (section 7.1 et section 7.3).

Les deux se combinent : un flux peut contenir une étape agentique, et un agent peut appeler un flux comme un outil. La distinction ne dit rien de l’autonomie : un agent N1 choisit ses étapes, mais ne fait que recommander.

**À RETENIR**

Le modèle ne décide que là où le chemin ne peut pas être écrit d’avance. Ce qu’une règle peut trancher (routage, calcul, contrôle de sécurité) reste dans le code (PRIN-08).

## 3.3 Agents interactifs et agents ambiants

Cette section distingue deux modes de déclenchement, qui pèsent sur la conception d’un agent.

Un agent interactif répond à une personne présente, dans une conversation ou une application. Un agent ambiant, selon LangChain, écoute un flux d’événements et agit en conséquence, éventuellement sur plusieurs événements à la fois, sans être nécessairement entièrement autonome; une tâche planifiée peut aussi le lancer**[86]**. Le tableau 8 en tire les conséquences.

*Tableau 8 — Agents interactifs et agents ambiants : conséquences de conception*

| **Dimension** | **Agent interactif** | **Agent ambiant** |
| --- | --- | --- |
| Déclencheur | Demande d’une personne dans un canal | Événement (message, alerte, changement d’état) ou tâche planifiée |
| Contrainte de temps | Réponse attendue en direct : appels d’outils et itérations bornés en conséquence | Délai relâché : traitement de fond, par lots au besoin |
| Interaction humaine | Dans la session, par un jeton d’approbation signé émis hors de l’interface de l’agent (EXIG-AUT-12, EXIG-AUT-13); une action P3 est approuvée hors bande (section 8.5) | File persistante : notifier, questionner, réviser (section 8.6) |
| État et reprise | Persistance requise dès qu’une approbation ou une tâche longue intervient | Exécution durable, qui survit aux pannes et aux redéploiements (section 7.4) |
| Risque dominant | Un « oui » dans la conversation pris à tort pour une approbation | Volume : saturation des approbateurs (menace T10 de l’OWASP)**[87]** et tempêtes d’événements (section 6.7) |

Le mode de déclenchement ne fixe pas le niveau d’autonomie. Un agent ambiant peut se borner à signaler (N1) ou préparer des actions soumises à approbation (N2). Dès qu’il exécute seul des écritures sur des tâches déclenchées sans demande d’une personne, il relève du niveau N4 : c’est l’origine de la tâche, lue par la passerelle, qui distingue N4 de N3 (section 3.1). Pour les traitements de fond non urgents, Anthropic et OpenAI accordent chacun, au 27 octobre 2026, un rabais de 50 % sur les jetons traités par lots, dans une fenêtre de 24 heures**[88, 89]** (section 10.6).

## 3.4 Ce qu’un agent n’est pas

Cette section écarte trois confusions qui minent la sécurité et l’imputabilité; les chapitres 9 et 11 en tirent les exigences.

### Pas un compte d’utilisateur

Un agent n’emprunte jamais le compte d’une personne, même pour agir en son nom. Microsoft déconseille d’attribuer aux agents un compte d’utilisateur ordinaire ou un principal de service traditionnel, et a créé pour eux un type d’identité propre**[90]**. À l’inverse, une personne n’utilise jamais l’identité d’un agent : l’OWASP range cet usage parmi les dix principaux risques des identités non humaines (NHI10)**[91]**. Pour agir au nom de quelqu’un, l’agent reçoit une délégation qui l’identifie aux côtés de la personne (section 9.3).

### Pas un principal de service partagé

Chaque agent a sa propre identité, et chaque instance la sienne dès que des instances servent des mandants différents ou doivent pouvoir être révoquées séparément**[92]**. Un compte ou une clé d’API commun à plusieurs agents empêche de savoir lequel a agi et de révoquer l’un sans arrêter les autres. Le brouillon « AI Identity Management System » (AIMS) du groupe de travail WIMSE de l’IETF exige un identifiant unique par agent et qualifie les clés d’API statiques d’anti-patron; l’OWASP classe la réutilisation d’identités non humaines parmi les risques majeurs (NHI9)**[91, 93]**.

### Pas un responsable

Un agent ne répond pas de ses actes, ne consent pas et n’approuve rien. Une personne nommée, le propriétaire métier (parrain), répond de chaque agent, de ses effets et de son retrait (section 11.1). Le droit et la pratique vont dans ce sens : l’art. 26, par. 2, du RIA oblige le déployeur d’un système à haut risque, à compter de la date d’application à ces systèmes (section 12.4), à confier la supervision humaine à des personnes physiques compétentes, formées et dotées de l’autorité nécessaire**[61, 94]**; Microsoft Entra Agent ID associe à chaque agent un parrain, responsable métier, et un « propriétaire » au sens d’Entra, chargé de l’administration technique (que le cadre nomme « responsable technique », section 11.1)**[90]**. Une approbation exigée par le cadre vient donc toujours d’une personne, jamais d’un autre agent (section 8.5).

**À RETENIR**

Un agent a une identité propre, des droits délégués et bornés, et une personne nommée qui en répond. Sans ces trois conditions, il ne satisfait pas aux exigences des chapitres 9 et 11.
