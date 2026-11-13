# Chapitre 1 — L'entreprise agentique

*Question directrice : qu'est-ce qui distingue une entreprise agentique d'une entreprise qui utilise des assistants ?*

> **Version 2 — 11 novembre 2026.** État de référence : cadre de gouvernance de Singapour pour l'IA agentique, version 1.5 (20 mai 2026, mise à jour le 5 juin 2026); page de l'initiative du NIST sur les standards d'agents, mise à jour le 9 novembre 2026; étude MAP, version 4 (4 juin 2026). Les numéros entre crochets renvoient aux sources en fin de chapitre : [1] à [10] sont primaires, dont [8] lue par son résumé seulement; [11] et [12] sont secondaires. Chapitre harmonisé avec les chapitres 2 à 43 d'après leurs points à retenir. Chapitre audité et révisé le 12 novembre 2026.

Une organisation peut installer un assistant sur chaque poste sans rien changer à son fonctionnement. L'assistant rédige, résume, répond; la personne lit, décide et agit. Les systèmes d'enregistrement ne voient passer que des humains.

L'entreprise agentique commence quand ce dernier point cesse d'être vrai : un logiciel dirigé par un modèle de langage ouvre lui-même le billet, modifie la commande, déclenche le paiement, puis confie la suite à un autre logiciel du même genre. Le mot « agentique » est devenu une étiquette commerciale, et il n'existe pas de consensus sur ce qu'est un agent [4]. Ce chapitre fixe donc le vocabulaire, puis propose une définition vérifiable.

Ce qui distingue une entreprise agentique n'est ni le nombre de ses agents ni la puissance de ses modèles. C'est le fait de déléguer des actions, et non plus seulement des réponses, à des logiciels dont elle borne l'autonomie et dont elle répond. Dès que cette délégation dépasse une équipe, deux conditions s'imposent : que les agents se branchent sur les systèmes et les uns sur les autres sans intégration sur mesure, et que leur travail commun soit coordonné de façon fiable. Ce sont l'interopérabilité et l'orchestration, les deux objets de ce compendium.

---

## 1.1 De l'assistant à l'agent

### Une boucle plutôt qu'un échange

Un assistant fonctionne par tours : une demande, une réponse. Un agent fonctionne en boucle. La description la plus dépouillée vient d'Anthropic : un agent est, le plus souvent, un modèle de langage qui utilise des outils dans une boucle, en se réglant sur ce que l'environnement lui renvoie [1]. À chaque étape, il obtient un résultat d'outil ou d'exécution, évalue son avancement et choisit la suite. Il peut s'arrêter à un point de contrôle pour consulter un humain; une condition d'arrêt, par exemple un nombre maximal d'itérations, sert à garder la maîtrise.

Le cadre de gouvernance de Singapour, faute de définition admise, retient des traits communs : une part de planification, de décision et d'action indépendantes, sur plusieurs étapes, vers un but fixé par l'utilisateur [4].

### Quatre propriétés

Quatre propriétés séparent l'agent de l'assistant. Aucune n'est binaire; chacune se règle.

**L'autonomie.** C'est le degré auquel le système décide lui-même de la marche à suivre. Elle dépend des instructions données, procédure détaillée ou jugement propre, et de la place laissée à l'humain [4]. La section 1.3 y revient.

**Les outils.** Un outil permet à l'agent d'agir sur un autre système : écrire dans un fichier ou une base, piloter un appareil, exécuter une transaction [4]. C'est par les outils que l'erreur d'un modèle cesse d'être une mauvaise phrase pour devenir une mauvaise écriture. Leur branchement est l'objet de MCP (chapitre 5).

**La mémoire.** Ce sont les informations conservées et accessibles au modèle, à court ou à long terme, tirées d'interactions passées ou de sources externes [4]. Elle donne à l'agent une continuité que l'assistant n'a pas, et ouvre des risques propres (chapitre 14).

**La délégation.** L'agent agit pour le compte d'une personne ou d'une organisation, et peut à son tour confier du travail : un agent superviseur appelle un agent spécialisé comme il appellerait un outil [4]. La délégation à un agent qu'on ne contrôle pas est l'objet d'A2A (chapitre 6). Elle pose une question que l'assistant ne posait pas : sous quelle identité, et avec quelle part de l'autorité de son mandant, l'agent agit-il (chapitre 29) ?

### Les composants, y compris ceux qui retiennent

Le cadre de Singapour décompose un agent en huit composants [4]. Six le rendent capable : le modèle, les instructions, la mémoire, la planification et le raisonnement, les outils, et les protocoles, dont MCP et A2A, par lesquels il communique avec des outils et d'autres agents. Deux le rendent sûr : les contrôles (contrôles d'accès, garde-fous, approbations humaines) et la journalisation avec la surveillance.

Ces deux derniers ont rejoint les composants de base dans la version 1.5 [4] : ce qui borne et ce qui trace l'agent fait désormais partie de sa définition.

### Ce que l'autonomie coûte

Les systèmes agentiques échangent souvent de la latence et du coût contre une meilleure exécution de la tâche, et leur autonomie accroît le risque d'erreurs qui se composent d'une étape à l'autre [1][4]. Le routage entre modèles déplace une part de ce coût (chapitre 44). D'où la recommandation d'Anthropic : chercher la solution la plus simple, et n'ajouter de la complexité que si elle se justifie. Pour bien des applications, un seul appel de modèle, enrichi de récupération et d'exemples, suffit [1].

---

## 1.2 Taxonomie

Cinq termes reviennent dans tout l'ouvrage, du plus simple au plus englobant.

| Terme | Définition retenue | Qui décide du chemin | Source |
|---|---|---|---|
| LLM augmenté | Un modèle doté de récupération, d'outils et de mémoire | Le modèle, sur un appel | [1] |
| Workflow agentique | Des modèles et des outils orchestrés selon des chemins de code prédéfinis | Le concepteur | [1] |
| Agent | Un système où le modèle dirige lui-même son déroulement et son usage des outils | Le modèle | [1] |
| Système multi-agents | Plusieurs agents qui travaillent ensemble, chacun avec sa spécialité, ses outils et ses permissions | Les modèles, dans une topologie donnée | [4] |
| Système d'IA composé | Un système fait de plusieurs composants en interaction : appels multiples à des modèles, récupérateurs, outils externes | Variable | [2] |

### Workflow ou agent : qui choisit les étapes

La distinction d'Anthropic est la plus utile en pratique, parce qu'elle tient à un seul critère [1]. Dans un workflow, le chemin est écrit d'avance et le modèle intervient à des étapes fixées. Dans un agent, le modèle choisit ses étapes. Les workflows conviennent aux tâches bien définies; les agents, aux cas qui demandent de la souplesse.

Cet ouvrage suit cet usage : « agent » désigne un système où le modèle choisit ses étapes, « workflow agentique » un système au chemin prédéfini, « système agentique » l'ensemble. Le cadre de Singapour observe d'ailleurs qu'en entreprise la plupart des mises en œuvre sont hybrides : des règles déterministes, et une part d'autonomie [4]. Le chapitre 17 place cette frontière sur quatre positions : workflow, étapes agentiques, agent borné, agent ouvert.

### Système multi-agents

Répartir le travail entre plusieurs agents permet de les spécialiser et de les faire travailler en parallèle. Cela permet aussi de borner séparément les outils et les permissions de chacun, au lieu de confier beaucoup d'outils à un seul [4]. Le cadre de Singapour retient trois patrons simples (séquentiel, superviseur, essaim), sans en tenir aucun pour universel.

Un relevé de 2026, connu ici par des sources secondaires, classe les topologies en centralisées, décentralisées et hiérarchiques, avec un axe adaptatif [11] (chapitre 16).

### Système d'IA composé

C'est la catégorie la plus large. Le terme vient d'un billet du laboratoire BAIR de Berkeley, en février 2024, qui constatait un déplacement : les meilleurs résultats venaient de moins en moins d'un modèle seul, et de plus en plus d'un système, qui peut chercher des données à jour, appliquer des contrôles d'accès et vérifier ses sorties [2]. La contrepartie : des difficultés nouvelles de conception, d'optimisation et d'exploitation.

Tout workflow agentique, tout agent et tout système multi-agents est un système d'IA composé. L'inverse est faux : un pipeline de génération augmentée par récupération est composé sans être agentique. La notion rappelle que la qualité se joue dans l'assemblage autant que dans le modèle.

---

## 1.3 Niveaux d'autonomie : premier aperçu

### Deux axes, pas un

Le cadre de Singapour sépare deux notions que le langage courant confond [4]. L'**espace d'action** est l'étendue de ce que l'agent peut faire. Il dépend des outils accordés et des permissions sur ces outils : bac à sable, systèmes internes ou externes; lecture ou écriture. L'**autonomie** est le degré auquel l'agent décide comment atteindre le but. Elle dépend des instructions et de la part laissée à l'humain.

Un agent peut décider seul dans un espace minuscule, ou demander une approbation à chaque pas dans un espace vaste. Le risque se lit sur les deux axes à la fois.

Un article publié par le Knight First Amendment Institute ajoute une idée : l'autonomie est une décision de conception, que le développeur peut fixer indépendamment de la capacité du modèle [5].

### Trois échelles

L'échelle de Feng et ses coauteurs définit cinq niveaux d'après le rôle de l'utilisateur [5]. Celle de Singapour, qui cite la précédente, en retient quatre [4]. Celle de la Cloud Security Alliance (CSA), calquée sur les niveaux de conduite automatisée SAE J3016, en compte six [6].

| Rôle de l'humain | Feng et coll. [5] | Singapour [4] | CSA [6] |
|---|---|---|---|
| Exécute tout; l'IA informe | — | — | 0, aucune autonomie |
| Dirige, ou approuve chaque action | L1, opérateur | L'agent propose, l'humain opère | 1, assistée |
| Partage le travail; approuve un plan ou les étapes importantes | L2, collaborateur | L'agent et l'humain collaborent | 2, supervisée |
| Est consulté pour ses préférences | L3, consultant | — | — |
| N'intervient qu'aux limites : actions critiques, blocages | L4, approbateur | L'agent opère, l'humain approuve | 3, conditionnelle |
| Observe; traite les anomalies ou audite après coup | L5, observateur | L'agent opère, l'humain observe | 4, autonomie élevée |
| Supervision stratégique seulement | — | — | 5, autonomie complète |

L'alignement des lignes est une lecture propre à ce chapitre : les trois échelles ne se recouvrent qu'approximativement. Le chapitre 22 les compare en détail.

### Quatre enseignements

**Le niveau se fixe par agent et par classe d'action, pas pour l'entreprise.** Un même agent peut lire sans approbation et ne payer qu'avec approbation. La CSA envisage aussi qu'un agent redescende de niveau dès qu'une anomalie est détectée [6].

**Les niveaux élevés ne sont pas la cible.** L'auteur de l'échelle de la CSA juge le niveau 5 inapproprié en entreprise aujourd'hui, et estime que le niveau 4 devrait exiger une autorisation de la direction et une acceptation de risque documentée. Il ajoute que les limites d'autonomie doivent être appliquées techniquement, et non seulement écrites dans une politique [6].

**L'approbation humaine ne passe pas à l'échelle.** Le cadre de Singapour reconnaît qu'une supervision continue de tous les agents devient impraticable, et qu'elle nourrit le biais d'automatisation. Il recommande de réserver l'approbation à des points de contrôle significatifs, comme les actions irréversibles ou à fort enjeu [4].

**La pratique est prudente.** L'étude MAP repose sur vingt études de cas et sur une enquête de 306 répondants, dont 86 décrivent des systèmes déployés, dans 26 domaines [7]. Parmi ces systèmes, 68 % exécutent moins de dix étapes avant une intervention humaine (« au plus dix » selon le résumé), et 74 % dépendent surtout d'une évaluation humaine. Chaque proportion repose sur quelques dizaines de réponses.

---

## 1.4 Définition opérationnelle de l'entreprise agentique

Aucune des sources lues ne définit l'entreprise agentique. McKinsey parle d'« organisation agentique » et décrit, d'après les résumés consultés, de petites équipes orientées résultats et des structures aplaties [12] (chapitre 41). La définition qui suit est une proposition de cet ouvrage.

> Une entreprise agentique est une organisation qui confie couramment à des agents logiciels des actions sur ses systèmes et auprès de ses partenaires, dans des limites d'autonomie explicites, sous des identités propres et sous une imputabilité humaine désignée, et qui compose ces agents entre eux par-delà les frontières d'équipe, de plateforme et d'organisation.

### Ce qui change par rapport aux assistants

| Dimension | Entreprise qui utilise des assistants | Entreprise agentique |
|---|---|---|
| Unité de travail | Une réponse | Une tâche menée à terme |
| Déclencheur | Une personne | Une personne, un événement ou un autre agent |
| Effet | Du texte; la personne agit | Des écritures dans les systèmes |
| Identité | Celle de l'utilisateur | Une identité d'agent, liée à un mandant |
| Intégration | Connecteurs propres à chaque produit | Protocoles ouverts et registres |
| Contrôle | Relecture par l'utilisateur | Espace d'action borné, garde-fous, points d'approbation |
| Imputabilité | L'utilisateur | Une chaîne désignée : propriétaire, superviseur, fournisseur |

La colonne de droite décrit un état plus exigeant, pas un état meilleur.

### Sept critères vérifiables

La définition se décline en sept questions, auxquelles on répond par une preuve et non par une déclaration.

1. **Action.** Des agents écrivent-ils dans des systèmes d'enregistrement, en production ?
2. **Limites.** Chaque agent a-t-il un espace d'action et un niveau d'autonomie déclarés, appliqués par des moyens techniques ?
3. **Identité.** Chaque agent agit-il sous une identité distincte de celle d'un employé ou d'un compte partagé (chapitre 29) ?
4. **Imputabilité.** Une personne nommée répond-elle de chaque agent, et une piste d'audit permet-elle de reconstituer ce qu'il a fait ?
5. **Inventaire.** L'organisation sait-elle quels agents et quels outils sont en service, et qui les a approuvés (chapitre 39) ?
6. **Composition.** Des agents de sources différentes coopèrent-ils par des interfaces standard, sans intégration propre à chaque paire ?
7. **Mesure.** Les résultats des agents sont-ils évalués en continu, et pas seulement leur disponibilité (chapitre 33) ?

Le premier critère fait l'agent; les quatre suivants le rendent gouvernable; le sixième fait de l'ensemble une question d'entreprise; le septième autorise à élargir l'autonomie, ou à la retirer (chapitre 34). Une organisation qui satisfait au premier sans les suivants n'est pas agentique, elle est exposée. Le cadre de Singapour nomme ce risque : une prolifération d'agents sans gestion centralisée, avec des problèmes de provenance et d'incompatibilité entre générations [4].

Les critères s'appliquent par domaine d'affaires : une entreprise peut être agentique dans son service à la clientèle et pas dans sa finance. Le chapitre 43 les ordonne en cinq stades, chacun assorti d'une preuve de sortie.

---

## 1.5 Thèse de l'ouvrage

### L'argument

Un agent, dans une équipe, branché sur cinq outils, n'a besoin d'aucun standard. La difficulté vient avec le nombre, et elle prend deux formes.

**La première est le branchement.** Sans protocole commun, chaque application d'IA écrit son connecteur pour chaque système, et le nombre d'intégrations croît comme le produit des deux (chapitre 5). Le même raisonnement vaut entre agents de fournisseurs différents (chapitre 6), entre organisations (chapitre 45), puis pour l'identité, la découverte et le sens des données. L'interopérabilité désigne l'ensemble de ces accords, que le chapitre 3 ordonne en cinq niveaux.

**La seconde est la coordination.** Brancher des agents ne suffit pas à les faire coopérer. La taxonomie MAST, tirée de traces de sept cadriciels multi-agents, recense quatorze modes d'échec en trois catégories : conception du système, désalignement entre agents, vérification de la tâche [8] (chapitre 21). L'étude MAP rapporte que la fiabilité est la première difficulté des équipes, et qu'elles y répondent surtout par la conception du système [7]. L'orchestration désigne cette conception : qui fait quoi, dans quel ordre, avec quelle reprise en cas d'échec et quelle intervention humaine.

Une architecture de référence proposée par Megagon Labs illustre le lien entre les deux [3]. Elle place au centre un registre d'agents et un registre de données, que des planificateurs consultent pour décomposer une demande en plan, sous des exigences de coût, de précision et de latence (chapitre 23). Sans description commune des agents et des données, pas de planification; sans planification, la description ne sert à rien.

La thèse en découle : **l'interopérabilité et l'orchestration sont les conditions de la mise à l'échelle.** Des agents interopérables mais mal orchestrés échouent ensemble. Des agents bien orchestrés mais fermés restent prisonniers d'une plateforme (chapitre 27).

### Ce que la preuve permet de dire

La thèse est un argument, pas un constat, et trois résultats de l'ouvrage la bornent. Aucun cas documenté ne montre MCP, A2A ou un système multi-agents en production (chapitre 42). Sur six bancs d'essai, l'écart moyen entre multi-agents et agent unique est à peu près nul : la coordination aide les tâches décomposables et nuit aux autres (chapitre 16). Et la capacité humaine de supervision borne la mise à l'échelle autant que la technique (chapitre 41). Les deux conditions sont donc nécessaires par raisonnement, non démontrées par la mesure, et elles ne suffisent pas.

### Un terrain qui se structure

L'Agentic AI Foundation héberge dix projets, dont MCP et A2A, ainsi que des formats de contexte et des passerelles [10]. L'initiative du NIST vise des agents qui fonctionnent de façon sûre pour le compte des utilisateurs et qui interopèrent; elle repose sur trois piliers : des normes menées par l'industrie, des protocoles menés par la communauté, et l'investissement en recherche [9]. C'est une démarche de consultation, sans texte normatif à ce jour (chapitre 11). Les protocoles expriment toutefois peu l'organisation et le droit (chapitre 3) : une part durable du travail reste à l'entreprise.

### Ce que la thèse ne dit pas

Elle ne dit pas que plus d'agents, ou plus d'autonomie, vaut mieux. Les sources lues convergent sur l'inverse : commencer simple [1], borner l'espace d'action [4], réserver l'autonomie élevée à des cas autorisés [6]. Elle dit que, pour une organisation qui choisit de déléguer des actions, la valeur plafonne tant que les agents ne peuvent ni se brancher ni se coordonner de façon gouvernée (état de l'adoption : chapitre 4).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Forme de la solution | La plus simple qui suffit : appel unique enrichi, puis workflow, puis agent | Chemin impossible à prévoir, et valeur qui justifie le coût et la latence |
| Un agent ou plusieurs | Un seul | Tâche décomposable en sous-tâches indépendantes, ou besoin de cloisonner outils et permissions (chapitre 16) |
| Espace d'action initial | Lecture seule, puis écriture dans les systèmes internes | Écriture externe : seulement avec identité propre et piste d'audit |
| Niveau d'autonomie | Fixé par agent et par classe d'action; approbation pour l'irréversible et le fort enjeu | Actions réversibles et à faible enjeu, dans un périmètre appliqué techniquement |
| Contrôles et journalisation | Exigés dès la conception, comme composants de l'agent | Prototype en bac à sable, sans accès à un système réel |
| Branchement des outils et des agents | Protocoles ouverts et registre | Parc très restreint dans une seule équipe |

---

## Points à retenir

- Un assistant produit une réponse et laisse l'humain agir. Un agent agit : il utilise des outils en boucle et choisit ses étapes.
- Quatre propriétés règlent le passage : autonomie, outils, mémoire, délégation.
- « Workflow agentique » et « agent » se distinguent par un critère : qui décide du chemin. La plupart des mises en œuvre d'entreprise sont hybrides.
- L'espace d'action et l'autonomie sont deux axes distincts. L'autonomie est une décision de conception, indépendante de la capacité du modèle.
- Les agents en production restent courts et surveillés : selon l'étude MAP, 68 % exécutent moins de dix étapes avant une intervention humaine.
- Une entreprise est agentique quand elle délègue des actions dans des limites explicites, sous des identités propres et une imputabilité désignée, et qu'elle compose ses agents par-delà ses frontières. Sept critères le vérifient.
- L'interopérabilité permet aux agents de se brancher; l'orchestration, de coopérer de façon fiable. Les deux conditionnent la mise à l'échelle : c'est un argument, qu'aucun cas documenté ne confirme encore.

---

## Sources

Pages primaires lues le 11 novembre 2026; [4], [6] à [10] relues le 12 novembre 2026 :

1. [Anthropic — Building effective agents (19 décembre 2024)](https://www.anthropic.com/engineering/building-effective-agents)
2. [BAIR — The Shift from Models to Compound AI Systems (18 février 2024)](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/)
3. [Kandogan et coll. — Orchestrating Agents and Data for Enterprise: A Blueprint Architecture for Compound AI (arXiv 2504.08148)](https://arxiv.org/html/2504.08148)
4. [IMDA — Model AI Governance Framework for Agentic AI, version 1.5](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) — pages 1 à 12.
5. [Feng, McDonald et Zhang — Levels of Autonomy for AI Agents (arXiv 2506.12469)](https://arxiv.org/html/2506.12469)
6. [Cloud Security Alliance — Leveling Up Autonomy in Agentic AI (28 janvier 2026)](https://cloudsecurityalliance.org/blog/2026/01/28/levels-of-autonomy)
7. [Pan et coll. — Measuring Agents in Production (arXiv 2512.04123, version 4)](https://arxiv.org/abs/2512.04123) — résumé, puis première moitié du texte à l'audit.
8. [Cemri et coll. — Why Do Multi-Agent LLM Systems Fail? (arXiv 2503.13657, version 3)](https://arxiv.org/abs/2503.13657) — résumé seulement.
9. [NIST — AI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative)
10. [Agentic AI Foundation — projets](https://aaif.io/projects)

Sources secondaires :

11. [Zhu et coll. — LLM-Based Multi-Agent Orchestration: A Survey](https://www.preprints.org/manuscript/202604.2147) — article non lu (accès refusé); taxonomie reprise de la carte thématique. [Fiche Zenodo des annexes](https://zenodo.org/records/19774440), lue.
12. [McKinsey — The agentic organization](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era) — page non lue (délai dépassé); contenu repris de la carte thématique.

## Limites de ce chapitre

- Les pages [1] à [3] et [5] à [10] ont été lues au moyen d'un outil qui extrait et condense le contenu. Seul [4] a été lu en texte intégral, sur ses douze premières pages, puis interrogé en entier à l'audit.
- MAP a été relue à l'audit sur la première moitié de son texte : son résumé dit « au plus dix étapes », son corps « moins de dix ». Les sous-échantillons comptent de 22 à 69 réponses selon le chapitre 4 (31 pour l'évaluation). Les parts des échecs selon MAST ne sont pas reprises, seul le résumé ayant été lu (chapitre 21).
- La fiche Zenodo annonce [11] à paraître dans *Future Internet*; le 12 novembre 2026, aucune parution n'a été trouvée (chapitre 16). Le rattachement de [3] à ICDEW 2025 ne figure pas sur la page lue; le chapitre 23 cite une version antérieure de la même architecture (arXiv 2406.00584).
- La section « Ce que la preuve permet de dire » et les renvois reprennent les points à retenir des chapitres cités, vérifiés à l'audit, sans relecture de leurs sources.
- La définition de l'entreprise agentique, ses sept critères, le tableau de la section 1.4 et l'alignement des trois échelles d'autonomie sont des propositions de ce chapitre, non des résultats tirés d'une source.
- L'argument du produit des intégrations est repris du chapitre 5, qui le rattache à la connaissance générale. La référence à SAE J3016 vient du billet de la CSA; la norme n'a pas été consultée.
- Aucun chiffre d'adoption n'est cité; ils relèvent du chapitre 4.
