# Chapitre 27 — Stratégie multi-plateformes

*Question directrice : comment vivre avec plusieurs orchestrateurs ?*

> **Version 2 — 11 novembre 2026.** État de référence : feuille de route MCP du 22 août 2026, notes de version de MuleSoft Agent Fabric jusqu'au 9 novembre 2026, Règlement (UE) 2023/2854 et ligne directrice B-10 du BSIF. Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [10] sont des pages primaires lues, [11] est une note d'analyste, [12] une reproduction du règlement. Chapitre audité et révisé le 12 novembre 2026.

Une grande entreprise ne choisit pas son orchestrateur : elle en hérite plusieurs. Les agents arrivent avec le progiciel de gestion, l'outil de gestion des services, la suite bureautique, le fournisseur infonuagique et les équipes qui bâtissent les leurs. Le chapitre 26 a montré que chaque éditeur propose un plan de contrôle et recense les agents des autres, sans qu'aucun gouverne l'ensemble.

La thèse de ce chapitre tient en trois propositions. La pluralité est un état durable, à administrer plutôt qu'à résorber. Ce qui se fédère aujourd'hui est l'inventaire, pas l'application des politiques. L'entreprise doit donc posséder en propre un noyau restreint — registre de référence, identité, politiques, actifs en formats ouverts — et tenir chaque plateforme pour une cible de déploiement remplaçable, ce que le contrat doit rendre vrai.

---

## 27.1 La réalité multi-orchestrateurs

### Un constat d'analyste, pas une mesure

La note de Futurum du 1er juin 2026 décrit une concurrence entre Microsoft, Salesforce, ServiceNow, AWS et Google pour la couche de contrôle de la main-d'œuvre numérique, et affirme que la plupart des entreprises exploiteront des environnements hétérogènes [11]. C'est une opinion d'analyste, adressée aux éditeurs : son sondage n'a pas livré ses valeurs à la lecture, et elle ne traite ni de fédération ni de portabilité. Elle confirme le décor sans outiller la décision.

### Trois niveaux d'orchestration

Le mot « orchestrateur » recouvre trois objets.

| Niveau | Ce qui orchestre | Frontière utile |
|---|---|---|
| Dans une équipe | Un cadriciel (chapitre 20) | Aucune : choix local |
| Dans une plateforme | Le plan de contrôle de l'éditeur (chapitre 26) | MCP vers les systèmes |
| Entre plateformes | Rien, par défaut | A2A entre agents; registre et identité communs |

Le troisième niveau est vide par construction. Les protocoles décrivent des échanges entre deux parties (chapitres 5 et 6); ils ne désignent pas qui tient l'inventaire commun, qui tranche un conflit de politiques ni qui arrête un agent fautif. Entre organisations, la question devient contractuelle (chapitre 45).

### L'argument prudentiel

Viser une plateforme unique supprimerait le problème, au prix d'un autre. La ligne directrice B-10 du BSIF définit le risque de concentration comme la dépendance excessive envers un même tiers, un même sous-traitant ou une même région, et demande aux institutions financières fédérales d'envisager, en infonuagique, des stratégies de résilience comme une conception multinuage [9]. Le texte, de 2023, ne nomme pas les agents; l'appliquer aux plateformes agentiques est une déduction. Une plateforme qui héberge à la fois les agents, leur identité, leur mémoire et leurs traces concentre pourtant plusieurs activités chez un seul tiers.

---

## 27.2 Fédérer registres et gouvernance

### Ce que les mécanismes lus permettent

Quatre mécanismes de rapprochement entre registres ont été lus. Aucun n'est un protocole de fédération entre pairs.

| Mécanisme | Sens | Ce qu'il transporte | Limite relevée |
|---|---|---|---|
| Sous-registre MCP [2] | Tirage depuis le registre amont | Métadonnées de serveurs, statut, enrichissements sous `_meta` | Préversion; aucune garantie de disponibilité ni de durabilité |
| AWS Agent Registry [6] | Publication, synchronisation depuis une URL | Serveurs MCP, agents, compétences, ressources à schéma libre | Détection automatique limitée aux ressources AgentCore d'une organisation AWS |
| Scanners MuleSoft [8] | Détection sur des plateformes tierces | Agents et serveurs trouvés | Ne voit que les plateformes prévues |
| Registre d'Agent 365 [7] | Inventaire unifié | Agents Microsoft et non Microsoft | Contrôles d'identité liés à Entra Agent ID et à sa licence |

Le modèle du sous-registre MCP est le plus instructif. Un agrégateur lit l'API REST du registre officiel à intervalles espacés, de l'ordre de l'heure, et conserve sa propre copie. S'il expose la même spécification OpenAPI, il devient un sous-registre consultable par les hôtes, et peut ajouter ses métadonnées sous une clé à son nom. Seul le statut d'un serveur change en principe; l'agrégateur doit le tenir à jour [2]. C'est une fédération hiérarchique, à sens unique, limitée aux serveurs MCP.

AWS Agent Registry se veut un catalogue unifié et expose un point d'accès MCP que tout client compatible interroge sans SDK d'AWS, avec un jeton du fournisseur d'identité de l'entreprise [6]. Chez Microsoft, Agent 365 devient le registre et le plan de contrôle unifiés, tandis qu'Entra garde l'identité; l'inventaire complet, agents sans identité Entra compris, ne se consulte que dans Agent 365 [7]. Chaque éditeur offre ainsi d'être le registre des autres (chapitre 8).

### L'inventaire se fédère, l'application non

Chez MuleSoft, les scanners détectent les agents d'Amazon Bedrock, de Google Vertex AI et de Microsoft Azure Copilot depuis janvier 2026, ceux de ServiceNow et les serveurs MCP de Kong Gateway depuis octobre. En août, les scanners d'API ont commencé à relever les politiques en place dans Apigee, Azure API Management et Kong Gateway, et des « politiques ouvertes » appliquées aux instances d'API se traduisent en politiques natives chez les fournisseurs qui les prennent en charge, dont Amazon API Gateway. Mais la note du 14 octobre retire l'onglet des politiques pour les instances d'agents et de serveurs MCP gérées par des passerelles tierces, comme Azure API Management ou Amazon API Gateway, au motif que l'application de politiques n'y est pas prise en charge [8].

L'asymétrie est nette : la lecture traverse les plateformes; l'écriture, quand elle les traverse, s'arrête aux API et n'atteint pas les agents. Elle rejoint l'échelle du chapitre 26, où l'agent tiers est presque toujours inventorié, parfois gouverné.

La feuille de route de MCP ne comble pas cet écart. Ses cinq priorités ne comptent ni fédération de registres, ni comportement des passerelles, ni portabilité de la configuration. Ce qui s'en rapproche relève de l'identité : fédération d'identités de charges de travail, ID-JAG et échange de jetons, confiés à un groupe de travail en formation, et sans engagement ferme [1].

### Un registre de référence, des registres sources

Proposition de ce chapitre :

- **Un registre de référence**, désigné par l'entreprise, comme l'inventaire de gouvernance du chapitre 39, fait autorité sur l'existence, le propriétaire et le statut de chaque agent et de chaque serveur. Les registres des plateformes restent des sources, alimentées localement et lues par synchronisation ou par scanner.
- **Une décision prise une fois, appliquée partout.** L'approbation et le retrait se décident au registre de référence. Leur exécution passe par le point de contrôle de chaque plateforme et par les passerelles (chapitre 24), puisque aucun mécanisme lu ne propage une politique d'agent d'un plan de contrôle à l'autre.
- **Une identité hors plateforme.** L'agent s'authentifie auprès du fournisseur d'identité de l'entreprise (chapitre 29); sans ce point fixe, chaque plateforme réinvente l'agent sous un autre nom.
- **Un socle minimal commun** : identifiant unique, propriétaire nommé, plateforme d'origine, statut, arrêt d'urgence (chapitre 34), traces versées dans un entrepôt commun (chapitre 33). Fédérer davantage aligne les politiques sur la plateforme la moins expressive.

Prendre ce registre chez un éditeur crée une dépendance de plus; l'exploiter soi-même coûte une équipe. Dans les deux cas, son contenu doit rester exportable (section 27.5).

---

## 27.3 Portabilité : agents, compétences, mémoire, configuration

Deux propriétés se confondent sous ce mot. L'**interchangeabilité** permet d'appeler un composant sans savoir où il tourne : c'est ce que donnent les protocoles. La **transférabilité** permet de le déplacer d'une plateforme à une autre : aucun protocole ne la promet.

| Actif | Format ou protocole ouvert | Ce qui reste captif |
|---|---|---|
| Outils | MCP (chapitre 5) | Connexions, secrets, politiques de passerelle |
| Agents | A2A comme frontière d'appel (chapitre 6) | Graphe, état, points de contrôle (chapitre 20) |
| Compétences | Agent Skills [3] | Scripts liés à l'environnement; outils préapprouvés |
| Instructions | AGENTS.md [4] | Tout ce qui n'est pas du texte destiné à l'agent |
| Mémoire | Aucun standard (chapitre 14) | Index, plongements, structures internes |
| Appels au modèle | Open Responses, format commun d'API annoncé [5]; passerelle d'inférence (chapitre 44) | Prompts réglés pour un modèle (chapitre 46) |
| Configuration | Rien | Permissions, garde-fous, routage, approbations |

**Les compétences** sont l'actif le plus transférable. Une skill est un répertoire qui contient un fichier `SKILL.md`, dont deux champs seulement sont obligatoires, `name` et `description`. La spécification marque elle-même les bornes : le champ `compatibility` sert à déclarer le produit visé ou les paquets requis, le champ `allowed-tools` est expérimental et sa prise en charge varie selon les agents, les langages de script dépendent de la mise en œuvre [3]. Le format relève de l'AAIF depuis le 22 octobre 2026; il voyage, mais le comportement se réévalue à l'arrivée (chapitre 13).

**Les instructions** suivent une convention plus légère encore. AGENTS.md est du Markdown ordinaire, sans champ obligatoire. Le format vise les agents de programmation [4]; il ne dit rien des agents d'affaires d'une plateforme d'entreprise.

**La configuration** est le point aveugle. Permissions, garde-fous, règles de routage et circuits d'approbation s'expriment dans le langage de chaque plateforme. La feuille de route de MCP n'évoque que la fourniture sécurisée d'options de configuration aux serveurs, et hors de ses livrables [1].

**La mémoire** n'a pas de format d'échange. Le chapitre 14 recommande de conserver les sources en texte et de reconstruire les index.

Règle de conduite : tout actif transférable vit dans un dépôt de l'entreprise, sous gestion de versions, et la plateforme n'en reçoit qu'une copie déployée. Ce qui ne s'écrit que dans la console d'un éditeur est captif. La preuve se fait par l'essai : redéployer périodiquement un agent représentatif sur une seconde cible et mesurer ce qu'il a fallu réécrire.

---

## 27.4 Construire, acheter ou fédérer

La question se pose par couche, non pour l'ensemble.

| Couche | Option par défaut | Raison |
|---|---|---|
| Agent logé dans un système d'enregistrement | Acheter, chez l'éditeur du système | Il possède les données, les droits et le contexte (chapitre 25) |
| Agent transversal ou différenciateur | Construire, exposer par A2A | La logique est un actif; la frontière le rend remplaçable (chapitre 20) |
| Passerelle | Acheter ou adopter un projet ouvert | Fonction d'infrastructure (chapitre 24) |
| Registre de référence, identité, politiques | Posséder | C'est le noyau que l'entreprise ne peut pas déléguer |
| Plan de contrôle d'ensemble | Fédérer | Aucun éditeur ne gouverne les agents des autres comme les siens (chapitre 26) |

Quatre critères font pencher la décision : l'endroit où vivent les données, le caractère différenciateur de la logique, la capacité de l'équipe à exploiter ce qu'elle bâtit, et le coût de sortie.

Fédérer n'est pas gratuit : intégration des registres, double inventaire à réconcilier, traduction des politiques plateforme par plateforme. Trois signaux indiquent qu'il faut plutôt consolider : deux plateformes font la même chose pour les mêmes utilisateurs, une plateforme ne peut pas exposer ses agents dans les deux sens, ou personne ne possède les agents qui y tournent.

---

## 27.5 Clauses contractuelles d'interopérabilité et de sortie

### Deux ancrages lus

**Le règlement européen sur les données** s'applique depuis le 12 septembre 2025 et consacre son chapitre VI au changement de fournisseur de services de traitement de données [10]. Le contrat doit prévoir un préavis d'au plus deux mois, une période de transition de 30 jours civils, portée à sept mois au plus en cas d'impossibilité technique, la liste exhaustive des données et actifs numériques exportables, une période de récupération d'au moins 30 jours, puis l'effacement (article 25). Les frais de changement sont interdits à compter du 12 janvier 2027 (article 29). Les services autres que d'infrastructure doivent offrir sans frais des interfaces ouvertes et, faute de spécification commune, exporter dans un format structuré, couramment utilisé et lisible par machine (article 30). Les services sur mesure et les versions d'essai bénéficient d'exemptions (article 31).

Deux réserves. L'article 2, point 8, vise l'accès à la demande à des ressources informatiques partagées, configurables et élastiques [12]; une plateforme d'agents en logiciel-service s'y range vraisemblablement, sans que ce soit acquis pour chaque offre. Et le texte ne dit pas ce qu'est une donnée exportable pour un agent : prompts, mémoire et traces restent à nommer dans le contrat.

**La ligne directrice B-10** vise les institutions financières fédérales canadiennes [9]. Elle attend des plans de sortie proportionnés au risque, avec un scénario de sortie ordonnée et un scénario sous contrainte pour les ententes critiques. L'entente devrait prévoir un préavis de résiliation, le retour des données dans un format qui permette de poursuivre les activités, et un avis en cas de sous-traitance.

### Clauses à négocier

La liste est une proposition, non un avis juridique.

1. **Standards nommés** : protocole, version, délai de mise à niveau (chapitre 11).
2. **Deux sens, en disponibilité générale** : la plateforme appelle des agents externes et se laisse appeler (chapitre 26).
3. **Inventaire exportable** : accès programmatique au registre, sans supplément.
4. **Liste exhaustive des actifs exportables** : définitions d'agents, prompts, compétences, configuration des outils, mémoire en texte, traces, jeux d'évaluation, journaux d'audit, avec format et fréquence.
5. **Identité** : fournisseur d'identité de l'entreprise accepté pour les agents.
6. **Égalité de traitement des agents tiers**, ou description écrite des écarts.
7. **Préavis en cas de changement de modèle ou de sous-traitant** : un modèle remplacé change le comportement d'un agent (chapitre 46).
8. **Transition** : durée, assistance, frais, récupération, effacement.
9. **Droit de répétition** : un essai de sortie pendant la durée du contrat.

Une clause ne crée pas une capacité technique. Elle ne vaut que si l'essai de sortie réussit avant que la sortie soit nécessaire.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Nombre de plateformes | Admettre la pluralité; plafonner par domaine | Petite organisation, parc chez un seul éditeur |
| Registre de référence | Un seul, désigné, alimenté par les registres sources | Plateforme unique : son registre suffit |
| Application des politiques | Au point de contrôle de chaque plateforme et aux passerelles | Aucun cas : l'inventaire fédéré ne l'assure pas |
| Identité des agents | Fournisseur d'identité de l'entreprise | Agent confiné à une plateforme |
| Périmètre fédéré | Inventaire, identité, arrêt d'urgence, traces | Plus large seulement si chaque plateforme l'exprime |
| Actifs | Dépôt de l'entreprise, formats ouverts, déploiement en copie | Prototype jetable |
| Construire ou acheter | Acheter près des données, construire ce qui différencie | Équipe sans capacité d'exploitation : acheter |
| Contrat | Liste d'actifs exportables, standards versionnés, essai de sortie | Service d'essai ou sans données propres |

---

## Points à retenir

- Plusieurs orchestrateurs coexistent durablement; aucun protocole ne désigne qui gouverne entre eux.
- Ce qui se fédère aujourd'hui est l'inventaire. Chez MuleSoft, les politiques atteignent au mieux les API des passerelles tierces, pas leurs agents ni leurs serveurs MCP.
- Le sous-registre MCP offre un modèle de fédération hiérarchique, limité aux serveurs et en préversion. La feuille de route de MCP ne prévoit ni fédération de registres ni portabilité de la configuration.
- L'entreprise doit posséder un noyau : registre de référence, identité, politiques, actifs en formats ouverts.
- Interchangeabilité n'est pas transférabilité. Les compétences et les instructions se déplacent; la configuration et la mémoire, non.
- Construire, acheter ou fédérer se décide par couche. Fédérer a un coût et tire les politiques vers le plus petit dénominateur.
- Le règlement européen sur les données et la ligne directrice B-10 fournissent des appuis pour les clauses de sortie; ni l'un ni l'autre ne nomme les agents.
- Une clause de sortie se prouve par un essai, pas par sa rédaction.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [MCP — feuille de route, mise à jour du 22 août 2026](https://modelcontextprotocol.io/development/roadmap.md)
2. [Registre MCP — agrégateurs et sous-registres](https://modelcontextprotocol.io/registry/registry-aggregators.md)
3. [Agent Skills — spécification](https://agentskills.io/specification)
4. [AGENTS.md](https://agents.md/)
5. [Agentic AI Foundation — projets](https://aaif.io/projects)
6. [AWS Agent Registry — capacités](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-key-capabilities.html)
7. [Microsoft — convergence du registre d'agents vers Agent 365](https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence)
8. [MuleSoft Agent Fabric — notes de version](https://docs.mulesoft.com/general/agent-fabric-release-notes)
9. [BSIF — ligne directrice B-10, gestion du risque lié aux tiers](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/third-party-risk-management-guideline)
10. [Règlement (UE) 2023/2854 sur les données, chapitre VI](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202302854)

Sources secondaires lues :

11. [Futurum — Who Will Control the Enterprise Agentic Workforce? (1er juin 2026)](https://futurumgroup.com/insights/who-will-control-the-enterprise-agentic-workforce-cios-face-a-new-platform-war/) — note d'analyste.
12. [Springlex — Règlement (UE) 2023/2854, article 2](https://www.springlex.eu/en/packages/data-act/data-act-regulation/article-2/) — reproduction du Journal officiel, lue le 12 novembre 2026.

## Limites de ce chapitre

- Aucune donnée chiffrée sur le nombre de plateformes par entreprise n'a été trouvée; la pluralité repose sur une note d'analyste et sur les constats du chapitre 26.
- Le registre de référence, le socle minimal, les critères de la section 27.4 et la liste de clauses sont des propositions de ce chapitre, sans source externe ni validation juridique.
- Du règlement européen, les articles 23 à 31, 41 et 50 ont été lus en anglais à la rédaction, mais EUR-Lex n'a pas pu être relu à l'audit; l'article 2 l'a été dans une reproduction [12]. Les clauses types de la Commission n'ont pas été lues.
- La page de la ligne directrice B-10, relue à l'audit, n'indique pas sa date d'entrée en vigueur.
- La spécification d'Open Responses n'a pas été lue; seule sa description par la fondation est reprise.
- Les notes de MuleSoft, relues à l'audit, ne donnent ni le statut des fonctions citées ni la liste des fournisseurs qui reçoivent les politiques ouvertes. La documentation de ServiceNow, de Google et de SAP sur la fédération n'a pas été lue.
- Les pages ont été lues au moyen d'un outil d'extraction qui en condense le contenu; une nuance a pu échapper.
- Aucun essai de fédération ou de migration entre plateformes n'a été réalisé ni trouvé.
