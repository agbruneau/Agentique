# Chapitre 35 — Cadres internationaux

*Question directrice : quelles obligations s'appliquent à un système d'agents ?*

> **État de référence :** règlement (UE) 2024/1689 (AI Act) modifié par le règlement (UE) 2026/1744, en vigueur depuis le 27 juillet 2026; cadre de Singapour pour l'IA agentique, version 1.5 du 20 mai 2026; ISO/IEC 42105 au stade « en cours de publication » le 22 octobre 2026; NIST AI RMF 1.0, en révision. Les numéros entre crochets renvoient aux sources en fin de chapitre : [1] à [7] sont des pages primaires lues pour ce chapitre, [8] à [10] des sources secondaires; [11] à [15] ont été ajoutées le 14 novembre 2026 pour la section 35.7.

Aucun des grands cadres de gouvernance de l'IA n'a été écrit pour les agents. Le règlement européen vise des systèmes d'IA et des modèles. La norme ISO/IEC 42001 vise le système de management d'une organisation. Le cadre du NIST vise des risques. Un agent qui planifie, appelle des outils et modifie des systèmes tiers entre dans ces catégories sans y être nommé. Parmi les cadres examinés ici, seul Singapour en a publié un dont l'agent est l'objet, et ce cadre n'oblige à rien.

Les obligations existent déjà : elles découlent de l'usage de l'agent, non de son architecture. Ce qui manque, c'est la manière de les satisfaire quand le système décide lui-même de ses étapes. Le texte contraignant fixe le résultat sans décrire le moyen; le texte qui décrit le moyen n'est pas contraignant. La conformité consiste à joindre les deux.

Le droit canadien et québécois est traité au chapitre 38, la responsabilité civile au chapitre 36.

---

## 35.1 L'AI Act européen et les agents

La référence est une prépublication d'avril 2026, « AI Agents Under EU Law », qui se présente comme la première cartographie réglementaire systématique pour les fournisseurs d'agents [1]. Elle précède l'adoption du Digital Omnibus; la section 35.2 la met à jour.

### Un objet sans nom juridique

Le règlement ne définit pas l'agent. Les auteurs le rattachent à la définition du système d'IA de l'article 3(1), qui admet déjà des « niveaux d'autonomie variables » et une capacité d'adaptation après le déploiement [1]. Un agent est donc un système d'IA, pas un modèle.

Cette qualification crée deux objets réglementaires. Le modèle de langage sous-jacent, s'il est à usage général (GPAI), relève du chapitre V du règlement et de son propre fournisseur. L'agent construit dessus est un système, dont le fournisseur peut être une autre entreprise. Une organisation qui assemble un agent sur un modèle tiers hérite d'une chaîne documentaire : celle que le fournisseur du modèle doit lui remettre au titre de l'article 53 [1].

### Le risque suit l'usage

Le classement à haut risque dépend du domaine d'application et non de l'architecture [1]. Deux voies y mènent :

- l'article 6(1) : l'agent est un produit, ou un composant de sécurité d'un produit, couvert par la législation sectorielle de l'annexe I, par exemple un dispositif médical ou une machine, où l'on rejoint la sûreté fonctionnelle (chapitre 46);
- l'article 6(2) : l'agent sert à l'un des usages de l'annexe III, par exemple le recrutement ou l'évaluation de la solvabilité.

Le même cadriciel d'orchestration peut donc produire un système hors champ ou un système à haut risque, selon la tâche confiée. Les interdictions de l'article 5 sur la manipulation et l'exploitation des vulnérabilités s'appliquent à tout agent, quel que soit son classement; les auteurs rapportent que l'AI Office les juge particulièrement pertinentes pour les systèmes agentiques [1].

Un agent généraliste pose ici une difficulté pratique : son usage n'est pas borné d'avance. Le fournisseur reste tenu de définir la destination du système et d'évaluer le mauvais usage raisonnablement prévisible (article 9(2)(b)) [1].

### Quatre exigences mises à l'épreuve

Pour un agent à haut risque, la prépublication relève quatre points de friction [1].

| Exigence | Ce que demande le règlement | Pourquoi l'agent la met à l'épreuve |
|---|---|---|
| Supervision humaine (art. 14) | Des personnes peuvent surveiller le système en service, en comprendre les limites, interpréter ses sorties, les écarter, l'arrêter (chapitre 22) | Chaînes de décision longues, sorties intermédiaires rarement montrées, exécutions de longue durée |
| Cybersécurité (art. 15(4)) | Résistance à l'usage non autorisé | Le moindre privilège doit être appliqué hors du modèle, au niveau des API et non par le prompt; l'outillage n'existe pas encore sur étagère |
| Transparence (art. 50) | Signaler l'interaction avec une IA; marquer les contenus synthétiques | L'obligation peut s'étendre aux tiers touchés par une action, comme le destinataire d'un courriel |
| Modification substantielle (art. 3(23)) | Tout changement non prévu à l'évaluation de conformité initiale relance celle-ci | La dérive de comportement est continue et n'a pas de date |

Un comportement adaptatif prévu et évalué, comme le choix d'un outil dans un catalogue documenté ou la récupération de documents, n'est pas une modification substantielle. L'apprentissage continu après le déploiement et la dérive émergente peuvent en être une. L'article 43(4) admet des changements prédéterminés, mais rien ne dit qu'une dérive graduelle puisse l'être. D'où la formule des auteurs : un système agentique à haut risque dont la dérive n'est pas traçable ne peut pas, aujourd'hui, satisfaire aux exigences essentielles du règlement [1]. Par extension, selon la lecture de ce chapitre, le routage entre modèles (chapitre 44), la bascule de fournisseur (chapitre 46) ou un modèle distillé (chapitre 47) devraient figurer d'avance parmi les changements prévus.

La chaîne de valeur ajoute une incertitude. Selon l'article 25, un déployeur ou un tiers devient fournisseur s'il appose son nom sur un système à haut risque, le modifie substantiellement ou en change la destination [1]. Dans un système assemblé à partir de composants de plusieurs entreprises, plusieurs participants peuvent acquérir ce statut. Le moindre privilège est traité au chapitre 30.

### Des normes harmonisées qui s'arrêtent avant l'agent

La conformité passera en pratique par les normes harmonisées que le CEN-CENELEC prépare à la demande de la Commission. La prépublication en donne l'état de janvier 2026 [1] : prEN 18286 (système de management de la qualité), prEN 18228 (gestion des risques), prEN 18229-1 (journalisation, transparence, supervision), prEN 18229-2 (exactitude, robustesse), prEN 18282 (cybersécurité), prEN 18284 et prEN 18283 (qualité des données, biais).

Le projet de norme de cybersécurité ne traiterait en substance que deux des cinq catégories de menaces agentiques que les auteurs distinguent. Le projet sur la supervision doit définir une supervision effective pour des chaînes à plusieurs étapes sans méthode validée pour le faire. Trois sujets ne sont couverts par aucun projet : l'orchestration multi-agents, l'accumulation d'état d'une session à l'autre et la découverte dynamique d'outils. Les auteurs recommandent de les traiter par des spécifications techniques internes [1].

### Les autres textes

Un fournisseur d'agents relève aussi, selon le cas, du RGPD, du Cyber Resilience Act, du Digital Services Act, du Data Act, de la directive NIS2, de la directive révisée sur la responsabilité du fait des produits et du droit sectoriel [1]. La prépublication relie chaque type d'action de l'agent au texte qu'elle déclenche, et ordonne la mise en conformité en douze étapes, de la délimitation du système à la surveillance après la mise sur le marché, détection de la dérive comprise.

La tâche fondatrice, selon les auteurs, est un inventaire exhaustif : actions externes de l'agent, flux de données, systèmes connectés, personnes touchées [1]. Il rejoint celui du chapitre 39.

---

## 35.2 Le Digital Omnibus : nouveau calendrier

### Un report devenu loi

Le règlement (UE) 2026/1744 du 8 juillet 2026, dit Digital Omnibus on AI, modifie l'AI Act. Publié au Journal officiel le 24 juillet 2026, il est entré en vigueur le 27 juillet [2][3].

La proposition initiale de la Commission, en novembre 2025, liait l'application des obligations à haut risque à la disponibilité des normes harmonisées [1]. Les colégislateurs ont remplacé ce mécanisme conditionnel par des dates fixes [8], que confirme le texte publié [2][3].

![Dates d'application de l'AI Act telles que les fixe le Digital Omnibus (règlement (UE) 2026/1744) : les échéances de 2025 et d'août 2026 restent inchangées, une échéance s'ajoute en décembre 2026 et les obligations à haut risque sont reportées à 2027 et 2028.](figures/fig-35-e1.svg)

| Date d'application | Objet | Effet de l'Omnibus |
|---|---|---|
| 2 août 2025 | Obligations des modèles GPAI | Inchangé [8] |
| 2 août 2026 | Transparence de l'article 50 | Inchangé [3][8] |
| 2 décembre 2026 | Marquage des contenus (art. 50(2)) pour les systèmes génératifs mis sur le marché avant le 2 août 2026; nouvelles interdictions de l'article 5 | Délai transitoire de quatre mois; interdictions nouvelles [2][3] |
| 2 août 2027 | Un bac à sable réglementaire par État membre | Reporté [3] |
| 2 décembre 2027 | Haut risque, annexe III | Reporté [2][3] |
| 2 août 2028 | Haut risque, annexe I | Reporté [2][3] |

À la date de ce chapitre, les obligations de transparence s'appliquent donc déjà. Un agent qui converse avec des clients ou leur écrit doit se déclarer comme tel, que son usage soit ou non à haut risque.

### Les autres modifications utiles à un architecte

Le texte ne se limite pas au calendrier [3][8].

- **Compétence de l'AI Office.** L'Office reçoit, sauf exceptions, une compétence exclusive sur les systèmes d'IA bâtis sur un modèle GPAI du même fournisseur, et sur ceux intégrés aux très grandes plateformes en ligne, avec des pouvoirs d'enquête, d'inspection et de sanction. L'agent vendu par l'éditeur de son propre modèle relève donc de l'Office; celui d'un intégrateur relève, en principe, d'une autorité nationale.
- **Chaîne de valeur (art. 25).** Quand un acteur en aval modifie substantiellement un système, les rôles se déplacent et le fournisseur initial doit coopérer avec le nouveau. Les accords écrits avec les fournisseurs de composants doivent préciser l'information nécessaire à la conformité, outils libres exclus.
- **Cybersécurité (art. 42).** Un système à haut risque couvert par le Cyber Resilience Act, et conforme à ses exigences, est réputé satisfaire aux exigences de cybersécurité de l'article 15.
- **Composant de sécurité (art. 6).** Un système sans fonction de sécurité n'est plus à haut risque du seul fait de son intégration à un produit réglementé, sauf si sa défaillance met en danger la santé ou la sécurité.
- **Analyse d'impact (art. 27).** Le déployeur peut renvoyer à son analyse d'impact relative à la protection des données.
- **Allègements.** L'obligation de maîtrise de l'IA (art. 4) devient un devoir de soutien à la formation; les PME obtiennent notamment un système de management de la qualité simplifié [3] et, selon [8], des amendes adaptées.

Les nouvelles interdictions visent les systèmes qui génèrent des images intimes non consenties ou du matériel d'abus sexuel d'enfants [3].

### Comment lire ce report

Le report n'est pas un répit : le cabinet Gibson Dunn, commentant l'accord provisoire, conseillait d'employer le délai à bâtir le dispositif de conformité [8]. L'argument vaut doublement pour les agents, dont les risques propres échappent aux normes harmonisées [1]. Il ne règle pas non plus le fond : la prépublication relevait que l'AI Office n'avait publié aucune orientation sur les agents ni sur la modification substantielle [1], et rien, dans les parties lues de l'Omnibus, ne traite de la dérive.

---

## 35.3 Le cadre de Singapour

### Nature du texte

Le Model AI Governance Framework for Agentic AI a été annoncé par l'IMDA le 22 janvier 2026, à Davos [9]. La version 1.5 porte la date du 20 mai 2026, avec une mise à jour au 5 juin; elle intègre les commentaires de plus de soixante entreprises [4].

Le document s'adresse aux organisations qui déploient des agents, développés à l'interne ou achetés. Il rassemble des pratiques recommandées; le texte lu ne mentionne ni obligation ni sanction. Il se dit évolutif et reconnaît l'absence de consensus sur la définition de l'agent [4].

### Ce que le cadre nomme

Le cadre décrit l'agent par ses composants : modèle, instructions, mémoire, planification, outils et protocoles, où MCP et A2A sont cités. La version 1.5 y ajoute deux composants de sûreté, les contrôles (contrôles d'accès, garde-fous, approbations humaines) et la journalisation avec surveillance [4].

Il sépare ensuite deux notions. L'**espace d'action** désigne ce que l'agent peut faire, selon ses outils et ses permissions. L'**autonomie** désigne sa latitude pour décider comment agir.

Cinq types de risques sont retenus : actions erronées, actions non autorisées, actions biaisées, fuites de données et perturbation des systèmes connectés. La version 1.5 ajoute les risques systémiques et multi-agents : vitesse et volume qui débordent la supervision, effets en cascade, prolifération d'agents, défaillances de collaboration (mauvaise coordination, conflit, collusion; chapitre 45) et comportements émergents que l'essai de chaque agent isolé ne révèle pas [4].

### Quatre dimensions

| Dimension | Mesures principales [4] |
|---|---|
| Évaluer et borner les risques en amont | Choisir les cas d'usage; limiter outils et accès dès la conception; préférer des limites déterministes; identité et permissions de l'agent; juger le risque résiduel |
| Rendre les humains réellement imputables | Répartir les responsabilités dans l'organisation et le long de la chaîne de valeur; approbation aux points à fort enjeu ou irréversibles; audit de l'efficacité de la supervision |
| Mettre en place des contrôles techniques | Contrôles à la conception; essais avant déploiement; déploiement graduel, surveillance continue, gestion des changements |
| Permettre la responsabilité de l'utilisateur | L'informer du champ d'action de l'agent et de ses accès; former; préserver le savoir-faire |

**L'identité de l'agent.** Le cadre admet que les systèmes actuels gèrent mal les agents : portées statiques, authentification pensée pour un individu unique, délégation récursive à des sous-agents. Il recommande une identité unique et vérifiable par cryptographie, rattachée à un humain, à un agent superviseur ou à une unité administrative, distinguée selon la capacité dans laquelle l'agent agit, et émise par un système central qui en tient le catalogue. Les autorisations devraient être délimitées, bornées dans le temps, non transférables, et ne jamais excéder celles de l'humain qui délègue [4]. Le chapitre 29 traite ce chantier.

**La chaîne de valeur.** Cinq maillons sont distingués : développeurs de modèles, fournisseurs de plateformes, fournisseurs de systèmes ou développeurs d'applications, déployeurs, utilisateurs finaux, auxquels s'ajoutent les fournisseurs d'outillage. Le principe est net : l'organisation qui déploie et les humains qui supervisent restent imputables des actes de l'agent [4].

**La mesure de la supervision.** Le cadre propose des indicateurs contre le biais d'automatisation, dont le taux de rejet ou de modification par l'humain et son temps de réponse, et recommande de refuser l'action par défaut quand l'infrastructure d'approbation est indisponible [4]. Le chapitre 22 les met en œuvre.

C'est un guide de mise en œuvre, non une source d'obligations.

---

## 35.4 ISO/IEC 42001 et projets en cours

### La famille

ISO/IEC 42001:2023 fixe les exigences d'un système de management de l'IA. Selon une synthèse d'octobre 2026, c'est le seul membre certifiable de sa famille, et aucun amendement ni révision n'était enregistré au début du mois [10]. La mention « 2026 » de la désignation européenne EN ISO/IEC 42001:2026 indique l'année d'adoption en Europe, pas une nouvelle édition.

| Document | Objet | État [7][10] |
|---|---|---|
| ISO/IEC 42001:2023 | Système de management de l'IA | Publié |
| ISO/IEC 42005:2025 | Étude d'impact d'un système d'IA | Publié |
| ISO/IEC 42006:2025 | Exigences pour les organismes de certification | Publié |
| ISO/IEC 23894:2023 | Orientations de gestion des risques | Publié |
| ISO/IEC 22989:2022 | Concepts et terminologie | Publié; amendement sur l'IA générative en projet final |
| ISO/IEC 42105 | Orientations sur la supervision humaine | En cours de publication |
| ISO/IEC 24970 | Journalisation des systèmes d'IA | Projet final (FDIS), selon le chapitre 11 |

### ISO/IEC 42105

Ce document guide le contrôle et la surveillance d'un système d'IA par des personnes. Il prolonge la spécification technique ISO/IEC TS 8200 et vise toute organisation, sur l'ensemble du cycle de vie [7]. Le catalogue d'un organisme national de normalisation l'affiche au stade 60.00, « norme en cours de publication », en date du 22 octobre 2026 [7]; une synthèse du début d'octobre le situait au vote final [10]. Le texte n'a pas été lu.

Ce sont des orientations, non certifiables, et rien dans les pages consultées n'indique qu'elles traitent des agents en propre.

### Ce que la famille ne contient pas

Aucune norme ISO/IEC propre aux agents n'a été trouvée : la synthèse consultée n'en mentionne aucune [10], et le chapitre 11 interprète cette absence. La prépublication européenne range ISO/IEC 42001 hors du lot des normes harmonisées; le système de management de la qualité attendu au titre de l'AI Act fait l'objet d'un projet distinct, prEN 18286 [1]. Une certification ISO/IEC 42001 ne vaut donc pas, à elle seule, conformité au règlement. Sa valeur comme preuve d'assurance est examinée au chapitre 32.

---

## 35.5 NIST AI RMF

Le AI Risk Management Framework du NIST, version 1.0, a été publié le 26 janvier 2023. Il est d'application volontaire et vise à intégrer la fiabilité à tout le cycle de vie des systèmes d'IA [5]. Il s'organise en quatre fonctions : Govern, Map, Measure, Manage.

Ses compléments comprennent un guide pratique (Playbook) et un profil pour l'IA générative, NIST AI 600-1, paru le 26 juillet 2024. Le 7 avril 2026, le NIST a publié une note conceptuelle en vue d'un profil sur l'IA de confiance dans les infrastructures essentielles [5].

**Le cadre est en révision**, au titre du plan d'action de la Maison-Blanche sur l'IA, sans calendrier publié [5].

**Il n'existe pas de profil pour les agents.** Ni la page du cadre ni celle de l'initiative du NIST sur les standards d'agents, mise à jour le 9 novembre 2026, n'en mentionnent [5][6]. Le profil pour l'IA générative reste le complément le plus proche.

**Le travail sur les agents se fait ailleurs.** L'initiative de février 2026 s'articule autour de trois axes : standards portés par l'industrie, protocoles communautaires, recherche sur l'authentification et l'identité des agents. Ses premiers livrables étaient une demande d'information sur la sécurité des agents et un projet de document du NCCoE sur l'identité et l'autorisation [6]. Le chapitre 11 en fait l'analyse.

Le AI RMF sert de vocabulaire commun avec des partenaires américains et de structure pour un programme de gestion des risques. Il ne tranche aucune question propre aux agents.

---

## 35.6 Table de correspondance entre cadres

Une case marquée « — » signifie que les pages lues ne permettent pas de se prononcer, non que le cadre est muet.

| Thème | AI Act [1][3] | Singapour v1.5 [4] | ISO/IEC [7][10] | NIST AI RMF [5][6] |
|---|---|---|---|---|
| Statut | Règlement, obligations datées | Pratiques recommandées | Norme volontaire; 42001 certifiable | Cadre volontaire |
| Objet | Système d'IA et modèle GPAI | Agent et système agentique | Système de management | Risques de l'IA |
| Agent défini | Non | Par ses composants | Non | Non |
| Classement du risque | Par usage (annexes I et III) | Espace d'action, réversibilité, autonomie | Orientations (23894), étude d'impact (42005) | Quatre fonctions |
| Supervision humaine | Art. 14 | Points d'approbation; audit de la supervision | 42105 | — |
| Identité et permissions | Art. 15(4), moindre privilège | Identité unique, autorisations bornées | — | Projet du NCCoE |
| Chaîne de valeur | Art. 25 | Cinq maillons | — | — |
| Après le déploiement | Surveillance, incidents graves | Déploiement graduel, surveillance continue | — | — |
| Multi-agents | Hors des normes en projet | Risques nommés | Rien trouvé | Rien trouvé |

Les cadres ne se contredisent pas : ils opèrent à des niveaux différents, et un même dispositif interne peut les servir tous. Leur zone aveugle est commune : aucun ne prescrit de règles pour l'orchestration multi-agents, et seul Singapour en nomme les risques.

---

## 35.7 Autres juridictions : un relevé

Les sections précédentes couvrent quatre cadres. Cinq autres comptent pour une entreprise présente à l'international. Ce relevé en donne l'état d'après une source par juridiction, sans l'analyse des sections 35.1 à 35.5.

| Juridiction | Instrument | Force | Les agents y sont-ils nommés ? |
|---|---|---|---|
| Corée du Sud | Loi-cadre sur l'IA, en vigueur le 22 janvier 2026 [11] | Loi; amendes après un délai de grâce | Non, d'après le commentaire lu |
| Japon | Loi de promotion de l'IA; deuxième plan de base du 14 juillet 2026 [12] | Loi de principes et plan gouvernemental | Oui : l'IA agentique est le premier thème du plan |
| Royaume-Uni | Aucune loi sur l'IA [13] | Régulateurs sectoriels | Non traité dans la source lue |
| Chine | Avis d'application sur les agents intelligents, 8 mai 2026 [14] | Avis administratifs | Oui : les agents en sont l'objet |
| OCDE | Rapport sur le paysage de l'IA agentique, février 2026 [15] | Travail d'experts, non contraignant | Oui : définitions comparées |

**Corée du Sud.** La loi s'applique aux exploitants qui développent l'IA comme à ceux qui l'intègrent à leurs produits, y compris hors de Corée quand le système touche des utilisateurs ou des marchés coréens. Une entreprise étrangère sans établissement doit désigner un représentant local au-delà de seuils de revenu ou d'audience [11]. La loi crée une catégorie d'IA « à fort impact », pour des secteurs comme la santé, l'énergie, les transports, l'embauche et l'analyse biométrique, assortie d'obligations d'explication, de plan de protection des utilisateurs, d'intervention et de supervision humaines, et de documentation. Tout exploitant d'IA générative ou à fort impact doit en prévenir l'utilisateur. Les amendes, plafonnées à 30 millions de wons, ne seraient appliquées qu'après un délai de grâce d'un an [11]. Le classement suit l'usage, comme dans l'AI Act.

**Japon.** La loi de promotion de l'IA est une loi de principes; le plan de base en est l'instrument. Le deuxième plan, arrêté le 14 juillet 2026, s'ouvre sur l'adaptation à l'essor de l'IA agentique et retient deux axes : adopter l'IA agentique, y compris dans l'administration, et bâtir une « souveraineté de l'IA » [12]. Il constate que les risques deviennent plus complexes, en particulier dans l'IA agentique, annonce une révision continue des lois et des lignes directrices, et confie à l'institut japonais de sécurité de l'IA l'évaluation des modèles, la traçabilité et les garde-fous. Le résumé lu n'énonce aucune obligation propre aux agents.

**Royaume-Uni.** Selon un commentaire de septembre 2026, le pays reste sans cadre législatif d'ensemble sur l'IA, et un projet de loi n'est pas attendu avant la fin de 2027 [13]. La seule initiative parlementaire relevée, un projet de loi d'un député visant à interdire les systèmes de superintelligence, a peu de chances d'aboutir. Le régime applicable aux agents est donc celui des régulateurs sectoriels et du droit de la protection des données, que ce chapitre n'a pas lu.

**Chine.** L'Administration du cyberespace a publié le 8 mai 2026 des avis d'application sur l'usage normalisé et le développement innovant des agents intelligents, qui tracent un cadre de gouvernance propre aux agents [14]. La fiche lue n'en donne ni le contenu ni la date d'effet. Avec la série de normes GB/Z 185-2026 (chapitre 11), la Chine est, des juridictions relevées ici, celle qui prend le plus directement l'agent pour objet.

**OCDE.** Un groupe d'experts a publié en février 2026 un rapport sur le paysage de l'IA agentique et ses fondements conceptuels. Ses auteurs distinguent l'agent d'IA, système qui perçoit son environnement et y agit avec une certaine autonomie en se servant d'outils, de l'IA agentique, où plusieurs agents coordonnés décomposent des tâches et poursuivent des buts complexes dans la durée, avec peu de supervision [15]. Le rapport rattache ces traits à la définition du système d'IA de l'OCDE, que reprennent des régulateurs financiers canadiens (chapitre 38). Ses auteurs réclament des typologies utiles aux politiques, fondées sur le degré d'autonomie, l'adaptabilité, le domaine et l'échelle d'impact, et davantage de données d'adoption.

Deux constats s'ajoutent à ceux de la section 35.6. Le texte contraignant nouveau, en Corée, classe par usage et ne nomme pas l'agent, comme le règlement européen. Les textes qui le nomment, au Japon, en Chine et à l'OCDE, sont des plans, des avis ou des travaux d'experts. L'écart relevé en ouverture de ce chapitre se retrouve donc hors d'Europe.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Cadre interne | Un seul dispositif, calé sur l'exigence applicable la plus stricte, avec Singapour comme guide de mise en œuvre | Activité sans lien avec l'UE : le cadre local prime (chapitre 38) |
| Classement d'un agent | Par cas d'usage, raisonnement documenté | Agent généraliste : borner la destination, sinon évaluer le pire usage prévisible |
| Calendrier européen | Viser décembre 2027 et août 2028, en commençant maintenant | Transparence de l'article 50 : déjà applicable |
| Lacunes des normes harmonisées | Spécifications internes pour l'orchestration, l'état entre sessions et la découverte d'outils | — |
| Dérive de comportement | Enveloppe de comportement documentée et détection continue | Haut risque avec apprentissage continu : s'abstenir tant que la méthode d'évaluation manque |
| Supervision humaine | Approbation aux actions à fort enjeu ou irréversibles; refus par défaut si l'approbation est indisponible | Action réversible et à faible enjeu : vérification après coup |
| Certification ISO/IEC 42001 | À rechercher si les clients ou le marché la demandent | Ne pas la présenter comme preuve de conformité à l'AI Act |
| NIST AI RMF | Vocabulaire commun avec des partenaires américains | Attendre la révision avant d'y aligner un outillage coûteux |
| Activité en Corée, au Japon, au Royaume-Uni ou en Chine | Vérifier le texte local, à partir du relevé de la section 35.7 | — |

---

## Points à retenir

- Aucun cadre contraignant ne définit l'agent. Dans l'AI Act, un agent est un système d'IA, distinct du modèle sur lequel il repose.
- Le classement à haut risque dépend de l'usage, non de l'architecture.
- Le Digital Omnibus fixe l'application du haut risque au 2 décembre 2027 (annexe III) et au 2 août 2028 (annexe I). Les obligations de transparence et celles des modèles GPAI n'ont pas été reportées, hormis un délai de quatre mois pour le marquage des contenus.
- La dérive de comportement est le point non résolu : selon la prépublication de référence, un système à haut risque dont la dérive n'est pas traçable ne peut pas aujourd'hui satisfaire aux exigences essentielles.
- Les normes harmonisées en préparation ne couvrent ni l'orchestration multi-agents, ni l'état accumulé entre sessions, ni la découverte dynamique d'outils. L'entreprise doit écrire ces spécifications.
- Le cadre de Singapour (version 1.5) est le seul des quatre à prendre l'agent pour objet. Il n'oblige à rien, mais fournit le mode d'emploi qui manque aux autres.
- ISO/IEC 42001 certifie un système de management, pas un agent; ISO/IEC 42105, sur la supervision humaine, est en cours de publication. Le NIST AI RMF est volontaire, en révision, et sans profil pour les agents.
- Le premier geste de conformité : inventorier ce que l'agent peut faire, à quoi il est branché et qui il touche.
- Hors d'Europe, le même écart se retrouve : la loi coréenne classe par usage sans nommer l'agent; le Japon, la Chine et l'OCDE le nomment dans des plans, des avis ou des rapports.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Nannini et coll., « AI Agents Under EU Law », arXiv 2604.04604](https://arxiv.org/abs/2604.04604) — prépublication du 6 avril 2026; résumé et corps du texte, lu en partie.
2. [Règlement (UE) 2026/1744 — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) — titre et considérants.
3. [Digital Omnibus on AI — AI Act Explorer](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/) — texte du règlement reproduit par un site tiers.
4. [IMDA — Model AI Governance Framework for Agentic AI, version 1.5](https://www.imda.gov.sg/assets/d1e45a56-d898-4b9f-972e-8ae94be1a5a5.pdf)
5. [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
6. [NIST — AI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative)
7. [Institut de normalisation de Serbie — fiche du projet ISO/IEC 42105](https://iss.rs/en/project/show/iso:proj:86902)

Sources secondaires, lues :

8. [Gibson Dunn — EU AI Act Omnibus Agreement, 27 mai 2026](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) — commente l'accord provisoire, avant l'adoption.
9. [Allen & Gledhill — lancement du cadre de Singapour, 13 février 2026](https://www.allenandgledhill.com/sg/publication/articles/32314/launches-new-model-ai-governance-framework-for-agentic-ai)
10. [GAICC — état de la famille ISO/IEC 42000, 7 octobre 2026](https://gaicc.org/blog/iso-42000-standards-family/)

Sources ajoutées le 14 novembre 2026, pour la section 35.7 :

11. [Cooley — South Korea's AI Basic Act: Overview and Key Takeaways (27 janvier 2026)](https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways) — commentaire de cabinet, secondaire.
12. [Cabinet du Japon — Summary of the Japan's Second AI Basic Plan (décision du 14 juillet 2026)](https://www8.cao.go.jp/cstp/ai/ai_plan/aiplan_g_eng_20260714.pdf) — résumé officiel, six pages.
13. [Lewis Silkin — AI judgment day on the horizon while UK lawmakers play catch up (14 septembre 2026)](https://www.lewissilkin.com/insights/2026/09/14/ai-judgment-day-on-the-horizon-while-uk-lawmakers-play-catch-up) — commentaire de cabinet, secondaire.
14. [Digital Policy Alert — avis d'application de l'Administration du cyberespace de Chine sur les agents intelligents (8 mai 2026)](https://digitalpolicyalert.org/event/39795-cyberspace-administration-of-china-issued-implementation-opinion-on-standardised-application-and-innovative-development-of-intelligent-agents) — fiche d'un observatoire, secondaire.
15. [OECD.AI — Can we create a clear understanding of what agentic AI is and does? (3 mars 2026)](https://oecd.ai/en/wonk/what-agentic-ai-is-and-does) — billet des auteurs du rapport de l'OCDE.

## Limites de ce chapitre

- Le texte de l'AI Act n'a pas été lu directement. Le contenu des articles 3, 6, 9, 12, 14, 15, 25, 43 et 50 est rapporté d'après la prépublication [1], dont environ un quart du texte (fin et conclusions) n'a pas été chargé.
- EUR-Lex n'a pas pu être relu à l'audit. À l'audit, l'article 113 modifié et les dispositions citées en 35.2 ont été relus dans [3], par un outil qui résume la page; ils concordent. Le calendrier des modèles GPAI et les amendes adaptées aux PME reposent encore sur une note de cabinet antérieure à l'adoption [8]. Les projets de normes prEN n'ont pas été consultés; leur état date de janvier 2026.
- Le catalogue de l'ISO a refusé l'accès. L'état de la famille repose sur [10], celui d'ISO/IEC 24970 sur le chapitre 11; le stade et l'objet d'ISO/IEC 42105 ont été relus à l'audit sur [7]. Le contenu de ces normes n'a pas été lu.
- Le NIST AI RMF n'est connu que par sa page de présentation, relue à l'audit avec [6] : le contenu des quatre fonctions n'est pas détaillé.
- Le résumé de [1] et les passages cités de [4] ont été relus à l'audit; du cadre de Singapour, les sections 2.3 et 2.4 et les études de cas restent survolées, et son caractère non contraignant est déduit de sa formulation.
- La table 35.6 est une lecture propre à ce chapitre, non une correspondance officielle. Sont aussi des déductions : l'attribution d'un agent d'intégrateur aux autorités nationales, et l'extension de la modification substantielle au routage, à la bascule de fournisseur et à la distillation.
- La section 35.7, ajoutée le 14 novembre 2026, n'est qu'un relevé : une source par juridiction, dont trois secondaires. La loi coréenne est décrite d'après un commentaire de cabinet antérieur à la publication de tous ses décrets [11]. Le Japon l'est d'après le résumé officiel de son plan [12], sans lecture de ses lignes directrices pour les entreprises. Le Royaume-Uni l'est d'après un commentaire qui ne traite pas des régulateurs sectoriels [13]. La Chine l'est d'après la fiche d'un observatoire, qui ne donne ni le contenu ni la date d'effet des avis [14]. L'OCDE l'est d'après un billet des auteurs du rapport, non d'après le rapport [15]. La série chinoise GB/Z 185-2026 est présentée au chapitre 11.
