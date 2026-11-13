# Chapitre 43 — Maturité et prospective

*Question directrice : par où commencer, et vers quoi aller ?*

> **Version 2 — 11 novembre 2026.** État de référence : feuille de route de MCP du 22 août 2026, page de l'initiative du NIST mise à jour le 9 novembre 2026, règlement (UE) 2026/1744. Ce chapitre est une synthèse : ses propositions reposent sur les chapitres cités par « (chapitre N) », et les numéros entre crochets renvoient aux pages relues pour dater l'état des lieux. Le modèle de maturité, la feuille de route et les scénarios sont des propositions de l'ouvrage, non des résultats de recherche. Chapitre harmonisé le 12 novembre 2026 avec les chapitres 41 et 42 et avec la thèse du chapitre 1. Les chapitres 44 à 47, ajoutés ensuite, approfondissent quatre sujets sans modifier ces conclusions. Chapitre audité et révisé le 12 novembre 2026.

Les protocoles d'accès aux outils et d'échange entre agents sont utilisables; l'identité des agents, les registres, l'observabilité et la gouvernance ne sont pas stabilisés (chapitre 4). Une entreprise ne peut ni attendre que tout soit fixé, ni bâtir comme si tout l'était.

Ce chapitre propose un modèle de maturité par domaine d'affaires, une feuille de route où le contrôle précède l'autonomie, puis trois scénarios pour 2027-2030 et leurs signaux. La thèse : commencer étroit, posséder le noyau de gouvernance et n'élargir l'autonomie que sur preuve sont trois choix qui restent bons dans tous les scénarios envisagés.

---

## 43.1 Modèle de maturité

### Ce que mesurent les modèles existants

Les **échelles d'autonomie** classent ce qu'un agent a le droit de faire. Celle de la Cloud Security Alliance compte six niveaux, de 0 à 5 [5]; son auteur la présente comme une proposition à discuter et juge le niveau 5 inapproprié en entreprise. Une telle échelle qualifie un agent, pas l'organisation qui l'exploite (chapitres 1 et 22).

Les **modèles de pratique** classent ce qu'une équipe sait faire. Une prépublication propose une pyramide à quatre étages, de l'ingénierie de prompt à celle de spécification, sans validation mesurée [6] (chapitre 13).

La **grille d'interopérabilité** du chapitre 3 évalue une relation, entre deux agents ou entre un agent et un outil, sur cinq niveaux d'entente, chacun noté de 0 à 3.

Il manque une vue par domaine d'affaires, qui relie ces mesures à une décision : étendre ou consolider.

### Cinq stades

Le modèle qui suit est une proposition de l'ouvrage, sans validation empirique. Il ordonne les sept critères de l'entreprise agentique (chapitre 1) en stades cumulatifs et attache à chacun une preuve de sortie.

| Stade | État | Preuve de sortie | Chapitres |
|---|---|---|---|
| 0 — Essais | Assistants et prototypes; aucune écriture en production | Un cas retenu, avec base de référence mesurée | 4, 40 |
| 1 — Agent borné | Un agent écrit dans un système d'enregistrement, dans un espace d'action fermé | Limites appliquées hors du prompt; succès vérifié sur un banc d'essai interne | 17, 22, 33 |
| 2 — Parc gouverné | Identité propre, responsable nommé et inscription à l'inventaire pour chaque agent; chemin obligé par une passerelle | Inventaire rapproché du trafic observé; exécution reconstituée à partir des traces | 23, 24, 29, 39 |
| 3 — Composition | Des agents de sources différentes coopèrent par des protocoles standard, avec registre interne et exécution durable | Relations au stade 2 de la grille du chapitre 3; essai de reprise et de compensation réussi | 3, 8, 18, 21 |
| 4 — Autonomie réglée | L'autonomie de chaque classe de décision s'élargit et se retire selon des mesures | Retrait automatique démontré; coût par résultat réussi suivi; essai de sortie de plateforme | 22, 27, 34, 40, 44 |

**Le stade se mesure par domaine d'affaires.** Une même entreprise peut être au stade 3 dans son service à la clientèle et au stade 0 en finance.

**Le stade est celui du critère le plus faible.** Un domaine où des agents se composent par A2A sans inventaire ni responsable nommé est au stade 1, pas au stade 3 : il fonctionne, et personne n'en répond.

**Le sommet n'est pas une cible.** Le stade visé dépend du risque. Un domaine d'actions irréversibles ou réglementées peut rester durablement au stade 2, avec approbation humaine, et ce choix se défend.

### Où en sont les déploiements observés

L'étude Measuring Agents in Production combine 20 études de cas et un sondage dont 86 réponses, sur 306 valides, décrivent des systèmes en production ou en pilote. Elle dépeint des agents de stade 1 : 68 % exécutent moins de dix étapes avant une intervention humaine (« au plus dix » selon le résumé), 14 cas sur 20 pilotent par prompt un modèle du commerce sans en ajuster les poids, 74 % des répondants dépendent surtout d'une évaluation humaine [3]. L'étude ne mesure pas les stades 2 à 4. Le chapitre 42 va dans le même sens : un seul déploiement à grande échelle trouvé dans un article évalué par les pairs, aucun cas documenté de MCP, d'A2A ou d'un système multi-agents en production. Le stade 3 n'a donc pas d'exemple publié, et le modèle sert à ordonner des décisions, non à situer une entreprise par rapport à une moyenne de marché, qu'aucune source lue ne fournit.

---

## 43.2 Feuille de route d'adoption

### Quatre jalons

La feuille de route se découpe en jalons franchis sur preuve, non en trimestres.

**Jalon 1 : choisir.** Le premier cas réunit quatre propriétés : une tâche bornée, des effets réversibles, un résultat vérifiable sans se fier au compte rendu de l'agent, une base de référence déjà mesurée (chapitres 16, 34 et 40). Un agent unique outillé suffit. Ce jalon produit aussi le banc d'essai interne, tiré de cas réels (chapitre 33).

**Jalon 2 : fonder.** Avant un deuxième agent, l'entreprise met en place le noyau qu'elle doit posséder : registre de référence, identité par agent, politiques appliquées à une passerelle, traces dans un schéma qu'elle maîtrise (chapitres 23 et 27). Ce jalon ne livre aucune fonctionnalité visible, d'où la tentation de le sauter. Son report coûte cher : un inventaire dressé après coup doit retrouver des agents non déclarés, ce qu'aucun cadre lu ne décrit (chapitre 39).

**Jalon 3 : étendre.** Un second domaine s'ajoute, puis la composition entre agents. Les outils qui produisent des effets deviennent idempotents ou compensables, et les processus longs passent sous exécution durable (chapitre 18). Les relations qui traversent une frontière d'organisation s'évaluent une à une avec la grille du chapitre 3; un réseau de partenaires relève du chapitre 45.

**Jalon 4 : élargir l'autonomie.** L'approbation humaine se retire classe de décision par classe de décision, sur la foi des mesures accumulées, avec un mécanisme de retrait qui ne dépend pas d'une personne (chapitres 22 et 34). Le rythme est borné par la capacité de supervision, pour laquelle aucun ratio d'agents par personne n'est établi (chapitre 41).

### La règle d'ordre

**Le contrôle précède l'autonomie.** Chaque jalon installe le moyen de vérifier le suivant : le banc d'essai avant la production, l'inventaire avant la prolifération, la compensation avant l'irréversible.

**Le stable se standardise, l'instable s'isole.** Le cœur de MCP et ses extensions stables peuvent porter une architecture (chapitre 5). L'identité des agents et la télémétrie ne le peuvent pas encore : le groupe de travail de MCP est en formation [1], et les conventions d'OpenTelemetry restent au statut « Development » (chapitre 33) [8]. Dans les deux cas, une couche interne (émetteur de jetons, schéma de traces) évite qu'un changement de standard se propage à tous les agents.

### Les échéances externes

| Échéance | Objet | Effet sur la feuille de route |
|---|---|---|
| 1er mai 2027 | Entrée en vigueur de la ligne directrice E-23 du BSIF pour les institutions financières fédérales [10] | Inventaire des modèles et cote de risque; le texte ne nomme pas les agents (chapitre 38) |
| Février à août 2027 | Horizon de six à douze mois de la feuille de route de MCP [1] | Prochaine révision à prévoir : événements, identité, forme des résultats d'outils |
| Été 2027, au plus tôt | Fin de la fenêtre minimale de dépréciation ouverte en juillet 2026 (chapitre 5) | Migration des fonctions dépréciées à terminer |
| 2 décembre 2027 | Application des obligations de l'AI Act au haut risque de l'annexe III [9] | Inventaire, traçabilité et supervision prêts pour les usages visés (chapitre 35) |
| 2 août 2028 | Même application pour l'annexe I [9] | Agents intégrés à des produits réglementés |

Le jalon 2 sert pour chacune : un inventaire d'agents rattachés à des responsables répond à une partie de chaque obligation (chapitre 38).

---

## 43.3 Scénarios 2027-2030

### Deux incertitudes

Parmi les six hypothèses du chapitre 4, deux portent sur des questions que l'entreprise ne tranche pas et qui commandent son architecture.

**La couche standard montera-t-elle jusqu'à l'identité et à la gouvernance ?** Elle s'arrête aujourd'hui à l'accès aux outils et aux échanges entre agents. Une analyse de cinq protocoles, en prépublication, conclut que la gouvernance est une couche d'architecture manquante au-dessus des standards plutôt qu'une fonction à leur ajouter [7].

**Les plans de contrôle se fédéreront-ils ?** Plusieurs éditeurs vendent chacun le leur, et ce qui se fédère aujourd'hui se limite à l'inventaire (chapitre 27).

Ces deux questions, auxquelles s'ajoute la géopolitique des standards (chapitre 11), donnent trois scénarios. Aucune probabilité ne leur est attachée.

| Scénario | Ce qui se produit | Ce qui prend de la valeur | Ce qui en perd |
|---|---|---|---|
| A — Socle étendu | Un profil d'identité d'agent est publié et adopté; les registres se fédèrent par une interface commune; la télémétrie se stabilise | Les actifs en formats ouverts; la capacité de changer de plateforme | Les couches d'isolation internes, devenues superflues |
| B — Archipel | Les standards restent aux niveaux technique et syntaxique; chaque plateforme gouverne ses agents | Le noyau possédé; les clauses de sortie éprouvées | Le pari sur une plateforme unique |
| C — Blocs | Les modèles de confiance divergent par juridiction, autour de racines d'identité et d'exigences de souveraineté distinctes | L'architecture régionalisée; la preuve portable d'un domaine à l'autre | Les agents conçus pour un seul espace de confiance |

Le scénario B prolonge l'état de 2026. Le scénario A suppose que les chantiers ouverts aboutissent, dont l'identité d'agent que vise la feuille de route de MCP, en coordination avec les groupes OAuth et WIMSE de l'IETF [1]. Le scénario C n'exclut pas les deux autres : une multinationale peut vivre A ou B à l'intérieur d'un bloc, et C entre les blocs (chapitres 11 et 37). Les lettres diffèrent du chapitre 11 : Blocs prolonge sa « bifurcation régionale » (B); l'Archipel est voisin de sa « prolifération » (C).

### Une variable transversale : la portée des agents

L'ouvrage suppose que les agents en production restent bornés et que le verrou tient à la conception du système plus qu'au modèle (chapitre 4, hypothèses H2 et H3). La taxonomie MAST recense quatorze modes d'échec, dont la plupart tiennent à la conception et à la coordination [4] (chapitre 21). Si une génération de modèles faisait disparaître ces échecs, le jalon 4 s'atteindrait plus vite. Les jalons 1 à 3 resteraient nécessaires : un agent plus capable a toujours besoin d'une identité, d'un inventaire et d'une piste d'audit.

### Ce qui vaut dans tous les cas

Quatre investissements sont sans regret : le noyau possédé (registre, identité, politiques, traces), les outils idempotents, le banc d'essai interne et l'essai de sortie. À l'inverse, deux paris sont fragiles dans au moins un scénario : confier toute la gouvernance à une seule plateforme (fragile en B et en C), et bâtir en propre ce qu'un standard s'apprête à fournir (coûteux en A).

---

## 43.4 Signaux à surveiller

| Signal | État au 11 novembre 2026 | Ce qu'un changement indiquerait |
|---|---|---|
| Identité d'agent dans MCP | Groupe de travail en formation; DPoP à finaliser [1] | Profil publié : scénario A; révision des émetteurs de jetons internes |
| Registre MCP | Préversion; ruptures et remises à zéro possibles avant la disponibilité générale [12] | Disponibilité générale : fédération de registres envisageable |
| Conventions GenAI d'OpenTelemetry | Statut « Development » (chapitre 33); dépôt dédié sans version publiée [13] | Version stable : retrait possible du schéma interne (chapitre 33) |
| Initiative du NIST | Lignes directrices volontaires annoncées sans date; aucun profil d'interopérabilité mentionné [2] | Publication datée : repère pour les secteurs réglementés |
| Gouvernance dans les protocoles | Aucun des cinq protocoles analysés n'encode l'ensemble des primitives de gouvernance [7] | Extension officielle d'approbation ou d'audit : scénario A sur la couche qui manque le plus |
| Projets de l'AAIF | Dix projets, sur trois niveaux depuis septembre 2026 (chapitre 11); la page des projets n'affiche pas ces niveaux [11] | Promotion ou archivage d'un projet dont dépend l'architecture (chapitre 11) |
| Portée des agents en production | Moins de dix étapes pour 68 % des agents étudiés [3] | Étude comparable montrant des parcours longs : hypothèse H2 à revoir |
| Échecs de coordination | Quatorze modes recensés [4] | Analyse refaite sur des modèles récents : hypothèse H3 confirmée ou infirmée |
| Protocoles ouverts en production | Aucun cas documenté (chapitre 42) | Étude évaluée par les pairs sur un déploiement MCP ou A2A : premier appui empirique à la thèse du chapitre 1 |

**Chaque signal a un responsable et une source primaire désignée.** Une synthèse de presse ne suffit pas : le profil d'interopérabilité que des sources secondaires prêtent au NIST ne figure pas sur la page de l'initiative [2].

**Chaque signal est rattaché à une décision qu'il ferait changer.** Sans cela, il n'est qu'une lecture.

**La revue est périodique.** Un rythme trimestriel convient : la feuille de route de MCP porte sur six à douze mois [1].

---

## 43.5 Dix recommandations

1. **Commencer par un agent unique et borné**, sur une tâche dont le résultat se vérifie. Le multi-agents se justifie par une tâche décomposable, non par principe (chapitre 16).
2. **Mesurer avant d'automatiser.** Une base de référence, un succès vérifié indépendamment de l'agent et un coût par résultat réussi précèdent toute extension (chapitres 33 et 40).
3. **Posséder le noyau** : registre de référence, identité, politiques et traces, en formats ouverts. Le reste peut s'acheter (chapitre 27).
4. **Donner à chaque agent une identité propre et un responsable nommé.** Ni clé partagée, ni justificatif visible du modèle (chapitres 29 et 39).
5. **Imposer un chemin obligé.** Une politique qu'aucun point de contrôle technique n'applique n'est pas une politique (chapitres 23 et 24).
6. **Standardiser sur le stable, isoler l'instable.** Le cœur des protocoles d'un côté; de l'autre, l'identité, la télémétrie et les extensions bêta derrière des couches internes (chapitres 5, 6 et 33).
7. **Concevoir pour la réémission.** Outils idempotents, compensation tenue par le propriétaire de l'outil, pivot explicite avant l'irréversible (chapitre 18).
8. **Gouverner par classe de décision.** L'autonomie s'élargit sur preuve et se retire sur signal; une limite écrite seulement dans un prompt n'en est pas une (chapitres 22 et 34).
9. **Traiter la fiabilité multi-agents comme une conception d'organisation** : division du travail, autorité, vérification de l'objectif et non du seul format (chapitre 21).
10. **Préparer la sortie et la conformité dès le premier agent.** Une clause de sortie se prouve par un essai, et un modèle de secours qualifié d'avance prépare la perte d'un fournisseur (chapitre 46); un inventaire tenu à jour est le premier geste de conformité (chapitres 27, 35 et 38).

### Retour sur la thèse

Le chapitre 1 pose que l'interopérabilité et l'orchestration conditionnent la mise à l'échelle. Au terme de l'ouvrage, la thèse tient comme argument et reste à prouver par la mesure, faute de cas publié (chapitre 42). Les protocoles règlent les niveaux technique et syntaxique; le sens, l'organisation et la confiance reviennent à l'entreprise (chapitre 3). La fiabilité d'un système multi-agents relève de sa conception (chapitre 21). Les recommandations qui précèdent restent bonnes si la thèse se révèle trop optimiste.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Unité d'évaluation de la maturité | Le domaine d'affaires, noté par son critère le plus faible | Très petite organisation : une seule évaluation |
| Stade à atteindre avant un second domaine | Stade 2 | Second domaine limité à des prototypes sans écriture |
| Ordre des investissements | Noyau de gouvernance avant la composition | Agent unique en lecture seule |
| Standard instable (identité, télémétrie) | Couche interne d'isolation | Standard devenu stable et pris en charge des deux côtés |
| Élargissement de l'autonomie | Par classe de décision, sur mesures, avec retrait automatique | Actions irréversibles ou réglementées : approbation maintenue |
| Hypothèse de planification | Scénario B, avec les investissements sans regret | Signaux convergents vers A ou C |

---

## Points à retenir

- La maturité se mesure par domaine d'affaires et par preuve, non par le nombre d'agents déployés. Le stade est celui du critère le plus faible.
- Les échelles d'autonomie et les modèles de pratique existants sont des propositions non validées. Le modèle en cinq stades de ce chapitre l'est aussi.
- Les déploiements étudiés se situent au stade 1 : agents courts, pilotés par prompt, évalués par des personnes. Aucun cas publié ne montre MCP, A2A ou un système multi-agents en production.
- La feuille de route avance par jalons franchis sur preuve. Le contrôle précède l'autonomie, et le noyau de gouvernance est le jalon à ne pas sauter.
- Deux incertitudes commandent l'horizon 2030 : l'extension des standards à l'identité et à la gouvernance, et la fédération des plans de contrôle.
- Le scénario de l'archipel prolonge l'état de 2026. Le noyau possédé, les outils idempotents, le banc d'essai interne et l'essai de sortie valent dans les trois scénarios.
- Deux échéances fermes encadrent la période : le 1er mai 2027 pour les institutions financières fédérales canadiennes, le 2 décembre 2027 pour le haut risque européen de l'annexe III.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [MCP — feuille de route, mise à jour du 22 août 2026](https://modelcontextprotocol.io/development/roadmap.md)
2. [NIST — AI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative)
3. [Measuring Agents in Production (arXiv 2512.04123, version 4)](https://arxiv.org/abs/2512.04123) — résumé; première moitié du texte relue le 12 novembre 2026.
4. [Why Do Multi-Agent LLM Systems Fail? (arXiv 2503.13657, version 3)](https://arxiv.org/abs/2503.13657) — résumé.
5. [Cloud Security Alliance — Leveling Up Autonomy in Agentic AI, 28 janvier 2026](https://cloudsecurityalliance.org/blog/2026/01/28/levels-of-autonomy)
6. [Context Engineering: From Prompts to Corporate Multi-Agent Architecture (arXiv 2603.09619, version 2)](https://arxiv.org/abs/2603.09619) — résumé; prépublication.
7. [Governance Gaps in Agent Interoperability Protocols (arXiv 2606.31498)](https://arxiv.org/abs/2606.31498) — résumé; prépublication.
8. [OpenTelemetry — conventions sémantiques GenAI (page déplacée)](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
9. [AI Act Explorer — Digital Omnibus on AI, règlement (UE) 2026/1744](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/) — reproduction non officielle, première moitié.
10. [BSIF — ligne directrice E-23, lettre d'accompagnement](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027-letter)
11. [Agentic AI Foundation — projets](https://aaif.io/projects)
12. [Le registre MCP](https://modelcontextprotocol.io/registry/about)
13. [OpenTelemetry — dépôt semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai) — lu le 12 novembre 2026.

Sources secondaires : aucune.

## Limites de ce chapitre

- Le modèle de maturité, les jalons, les scénarios et les recommandations sont des propositions de synthèse, non validées; aucune source lue ne répartit les entreprises par stade.
- Les articles [4], [6] et [7] ont été lus par leur résumé seulement; [3], par son résumé et la première moitié de son texte. Les pages [2], [5], [8] à [11] et [13] ont été lues par un outil qui en extrait le contenu; seules [1] et [12] l'ont été en texte intégral. Relues à l'audit : [1] à [4], [8] et [11]. Le règlement [9] a été lu sur un site non officiel, pour sa première moitié. Le texte de E-23, lu pour le chapitre 38, confirme l'inventaire et la cote de risque.
- MAP écrit « au plus dix étapes » dans son résumé, « moins de dix » dans son corps, sans expliquer l'écart; son 74 % porte sur 31 réponses.
- Les renvois « (chapitre N) » reprennent ces chapitres sans relecture de leurs sources; ils ont été vérifiés sur leurs points à retenir et, pour les chapitres 3, 4, 11, 13 et 39, sur la section visée.
- L'intervalle « février à août 2027 » est déduit de l'horizon de six à douze mois annoncé le 22 août 2026; la feuille de route ne date pas la prochaine révision.
- Le statut « Development » des conventions d'OpenTelemetry vient du chapitre 33; ni la page [8] ni le dépôt [13] ne l'affichent.
