# Chapitre 19 — L'architecture de référence par couches

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | **F-36, F-37, F-46** (assignés par [TOC.md](../../TOC.md)) ; **Partie II** — F-07, F-08, F-15, F-16, F-32, F-33. **Au-delà de l'assignation de TOC**, les deux couches que PRD §6 impose à cette architecture obligent à mobiliser : **F-01, F-02, F-04** (couche protocolaire — Partie I) et **F-09, F-25, F-26, F-27** (couche de gouvernance — Partie III) ; **F-35** (fait négatif vérifié, standard technique non désigné — porte l'exclusion de Z4 au §19.3 et la frontière d'abstraction au §19.4), avec **F-11** et **F-34** en compléments ; **F-17**, **F-21** et **F-28**, qui portent les faits du §19.2 (métriques auto-déclarées de TD et de la Banque Scotia ; bascule d'ISO 20022 sur Lynx) ; **F-10** en renvoi. Écart TOC ↔ PRD §6 signalé à la gouvernance |
| Garde-fous à surveiller (PRD §8) | **réserve F-09** (« attendu par E-23 », jamais « exigé » ; « documentation de modèle » / « inventaire », jamais « fiche de modèle ») ; **réserve F-01** (« cadre d'autorisation », jamais « sécurisé ») ; **réserves F-37** (préprint non révisé par les pairs ; chiffres en illustration seulement) ; **R-2** (identités et *blueprints*, jamais « registre centralisé » pour Entra) ; **R-3** (la spécification CSA **s'appuie sur** SPIFFE/SPIRE, ne l'impose pas) ; **§8.2.5** (statuts pré-normatifs) ; **§8.2.2 / §7.5** et **§8.2.3** (métriques auto-déclarées d'institutions et d'éditeurs) ; **réserve F-25** (jamais « en attente » ni « en projet ») ; **§8.4** (F-46 = position d'IBM, cas documenté et non recommandation ; instanciation renvoyée à la Partie VII) ; motif **R-7** (« E-23 ») : ressort en contexte réglementaire pur — aucune correspondance produit ↔ réglementation dans ce chapitre, filtré (PRDPlan §4.3) ; motifs **R-1** et **R-8** (« ACP », « control plane », « plan de contrôle ») : zéro occurrence ; **R-4 / réserve F-29** : le RTR n'est pas mobilisé (renvoi ch. 15) |
| Volumétrie cible | ~3000 mots |

> **Thèse ([TOC.md](../../TOC.md))** : Architecture cible neutre structurée par OO1–OO4, avec OO3/OO4 imposés sous exigence réglementaire stricte.

---

Le chapitre 18 s'achève sur un constat négatif : quinze croisements, aucun lien documenté, cinq zones où l'architecture doit compenser. Le présent chapitre construit — et doit dire d'abord à quel titre.

Une architecture de référence n'est pas une déduction du socle. C'est un ordonnancement : elle range ce que le socle documente, elle nomme ce qu'il ne documente pas, et elle pose entre les deux des liens qui sont d'un auteur — d'où, comme au chapitre 13, plus d'inférences marquées que dans les chapitres de fait. Elle est en outre **neutre** : aucun composant d'éditeur n'y est prescrit. L'instanciation sur un portefeuille réel — celui d'IBM, retenu comme cas documenté par sources primaires et non comme recommandation — est l'objet de la Partie VII[^1].

## 19.1 Les quatre couches et leurs responsabilités

L'architecture cible compte **quatre couches** : les protocoles, l'identité et le registre, l'orchestration, la gouvernance. Le découpage est imposé par le cahier des charges de l'ouvrage ; sa vertu est d'obliger à dire, couche par couche, ce que le socle documente et ce qu'il laisse vide.

| Couche | Ce que le socle documente | Responsabilité dans l'architecture | Ce qu'elle ne porte pas |
|---|---|---|---|
| **Protocoles** | MCP (*Model Context Protocol*) : accès aux outils, données typées, cadre d'autorisation (*authorization framework*)[^2] ; A2A (*Agent2Agent*) : délégation de pair à pair, cartes d'agents signées (*Signed Agent Cards*)[^3] ; leur complémentarité — « MCP dans les agents, A2A entre les agents » — est une doctrine **déclarée par le projet A2A**, et un critère de découpage n'est pas une contrainte (ch. 2)[^12] ; AP2 (*Agent Payments Protocol*), anatomie non portée[^4] | Format et habilitation à la frontière : **qui** parle, par quel format | Le processus, la trace d'instance, la décision, l'humain (ch. 18) |
| **Identité et registre** | Entra Agent ID : identités d'agents et *blueprints*, sur OAuth 2.0 et OIDC[^5] ; spécification CSA « Agent Registry », **brouillon** : profil ancré SCIM 2.0, `toolAccessList`, `permissionBoundaries`[^6] | Nommer l'agent ; borner ses outils et ses droits hors de lui | La conformité (statuts pré-normatifs), l'inventaire attendu par E-23 (objet distinct) |
| **Orchestration** | Taxonomie OO1–OO4, cinq propriétés, sept critères[^7] ; réalisations : workflows à base de graphes, points de contrôle (*checkpointing*), humain-dans-la-boucle (*human-in-the-loop*)[^8] | Tenir l'enchaînement ; produire la trace ; arrêter pour l'humain | La qualification juridique du processus ; le contenu des cadres (*frames*) |
| **Gouvernance** | E-23 : cinq domaines d'attentes opératoires, extraits du texte intégral[^9] ; ligne directrice IA de l'AMF : le calendrier seul[^10] ; avis 11-348 ; article 12.1[^11] | Inventaire, cotation, cycle de vie, documentation, surveillance | Ce que l'AMF attend — non porté par le socle |

**La couche protocolaire** répond à deux questions : comment un agent atteint un outil, comment un agent délègue à un autre (ch. 2 ; ch. 18). Une réserve commande sa place : MCP porte un **cadre d'autorisation** fondé sur OAuth, jamais un protocole « sécurisé » — la sécurité dépend de l'implémentation[^2].

**Lecture de l'auteur** : de ces quatre couches, la protocolaire est la mieux documentée du socle et la moins porteuse pour un processus réglementé — une spécification décrit un appel, et un appel n'est pas une décision. Le socle ne porte, ni pour MCP ni pour A2A, d'événement de décision, d'explication d'instance ni d'intervention humaine (ch. 18). **Le choix d'un protocole ne referme donc aucune des cinq zones de compensation.**

**La couche d'identité et de registre** appelle son statut avant son contenu. Entra Agent ID est documenté en disponibilité générale pour tous les clients Entra depuis le printemps 2026, des sous-fonctionnalités restant en préversion : **identités d'agents** (*agent identity*) et *blueprints*, sur OAuth 2.0 et OpenID Connect — dont les flux OBO/agent-token **étendent** ces RFC plutôt qu'ils ne s'y conforment[^5]. Le socle ne documente pas de registre d'agents centralisé pour cette capacité, et cet ouvrage n'en écrira pas : absence de documentation, non fait négatif vérifié (R-2). Le **registre d'agents** (*agent registry*) proprement dit relève d'une spécification de la Cloud Security Alliance publiée le 27 mars 2026, dont deux champs obligatoires intéressent cette architecture : `toolAccessList`, liste explicite des outils et serveurs MCP autorisés, et `permissionBoundaries`, bornes de moindre privilège[^6]. Son statut interdit d'en faire un point d'appui : **brouillon** de laboratoire, non norme ratifiée, dont le brouillon IETF d'ancrage SCIM a expiré le 19 avril 2026 ; elle **s'appuie sur** SPIFFE/SPIRE, sans que l'exigence stricte soit établie[^6]. Le chapitre 8 en porte le détail.

**Lecture de l'auteur** : ces deux champs sont, dans le vocabulaire du manifeste sur l'*Agentic Business Process Management*, un **frame opérationnel** (*operational frame*) — ce que l'agent peut faire, avec quels outils — écrit hors de l'agent, dans un objet lisible avant l'exécution[^13]. Le socle porte les deux termes ; il ne pose pas le rapprochement, et l'état pré-normatif de la spécification interdit d'en tirer autre chose qu'une direction. Un second rapprochement est à écarter : un registre d'agents et l'**inventaire** attendu par E-23 ne portent pas sur le même objet — le premier recense des agents, le second des modèles dont le risque inhérent est jugé non négligeable[^9]. Les confondre prêterait au régulateur un périmètre qu'il n'énonce pas.

**La couche d'orchestration** est celle où réside le cadre (*frame*), et donc celle où se joue tout ce chapitre. Le socle y documente, au niveau d'un cadriciel d'orchestration et à aucun niveau protocolaire, les deux mécanismes qui la rendent possible : les points de contrôle (*checkpointing*) et l'humain-dans-la-boucle (*human-in-the-loop*)[^8].

**La couche de gouvernance**, enfin, est la seule dont le socle porte des attentes opératoires — et il ne les porte que pour un texte sur deux. Depuis l'extraction du texte intégral de la ligne directrice E-23 du Bureau du surintendant des institutions financières — EN et FR, le 16 juillet 2026 —, le socle porte cinq domaines d'attentes : un **cycle de vie** à cinq volets, « not necessarily sequential » ; un **inventaire** d'entreprise « accurate, evergreen » dont l'Appendice 1 énumère les champs ; une **cotation graduée**, « Each model should be assigned a model risk rating » ; une **documentation de modèle** ; une **surveillance continue** visant « autonomous decision making, autonomous re-parametrization »[^9]. La modalité commande la rédaction de toute cette couche : E-23 est **fondée sur des principes** et rédigée au conditionnel — on écrira « attendu par E-23 », jamais « exigé »[^9].

Sur les agents eux-mêmes, la formulation est verrouillée : E-23 ne nomme ni l'agentique, ni les agents, ni l'orchestration — vérification mécanique sur le texte intégral, EN et FR. Sa définition de « modèle », laissée « intentionally broad », englobe les méthodes d'IA et d'apprentissage automatique, et le texte vise expressément la « prise de décision autonome » et la « reparamétrisation autonome » ; d'où une **couverture implicite** que les analystes juridiques canadiens (McCarthy Tétrault, Torys, Blakes, BLG, Sookman) tiennent pour acquise[^14].

La ligne directrice sur l'intelligence artificielle de l'Autorité des marchés financiers, finale depuis le 30 mars 2026, partage la date d'entrée en vigueur d'E-23 — le 1er mai 2027, dans neuf mois et quinze jours à la date de gel — mais n'est au socle que par son calendrier[^10]. **Lecture de l'auteur** : cette couche est donc spécifiable contre un texte et pas contre l'autre, alors que les deux entreront en vigueur le même jour. L'asymétrie n'est pas dans le droit ; elle est dans le socle de cet ouvrage, et le chapitre 21 la reprend.

## 19.2 Le positionnement des options d'orchestration par cas d'usage

Le chapitre 13 a énoncé le principe directeur : **sous exigence réglementaire stricte, le processus est imposé de façon déterministe par le cadre, qui invoque les agents ; les agents n'orchestrent pas le processus** — soit les positions OO3 et OO4 de la taxonomie des options d'orchestration (*orchestration options*)[^7]. **Lecture de l'auteur** : ce principe est construit par transposition de trois sources dont le socle n'établit l'application ni au Canada ni à la finance canadienne[^15]. Il dit où placer la main qui commande, non comment qualifier un processus.

Le cadre de la TU Munich fournit pour cela sept **critères qualitatifs de sélection** : la complexité du but, la supervision humaine, les contraintes, l'action humaine, l'espace de décision, l'effort initial et la maintenance[^7]. Deux avertissements du chapitre 5 les accompagnent. Le socle écrit « contraintes » **sans adjectif** : les contraintes réglementaires en sont une espèce, non le genre — un budget de latence sur un rail de paiement en est une autre[^16]. Et ces critères orientent un jugement sans calculer de réponse : aucune pondération ni fonction de score ne les relie aux quatre options[^7].

> **État de la recherche — le socle ne documente l'option d'orchestration d'aucun déploiement agentique canadien**
>
> Question : les systèmes agentiques que la Partie V documente en production dans les institutions financières canadiennes occupent-ils une position identifiable sur la taxonomie OO1–OO4 ?
>
> Lacune ouverte le 16 juillet 2026 ; **aucune passe de recherche n'a été conduite** — hors périmètre de la phase P0, qui a instruit l'adoption sans instruire l'architecture. Les entrées de la Partie V documentent des fonctions, des volumes déclarés et des gouvernances internes ; aucune ne dit qui, du cadre ou de l'agent, commande l'enchaînement. Le socle ne porte par ailleurs **aucune application documentée de la taxonomie à un processus d'institution financière** (PRD §10.10). Source à retrouver : documentation d'architecture des institutions concernées, non publique à la connaissance de cet ouvrage. Aucune inférence n'est proposée ici — et **les trois classes ci-dessous ne sont pas des architectures réelles** : elles sont construites à partir des seules *fonctions* que les sources primaires décrivent.

**Classe 1 — la décision de crédit avec mémo à un souscripteur humain.** Selon un communiqué de TD du 21 mai 2026, la banque **déclare** que son premier modèle d'IA agentique, développé par Layer 6, effectue la pré-adjudication du prêt garanti par l'immobilier et génère des mémos de synthèse pour les souscripteurs, ramenant un traitement d'environ quinze heures à moins de trois minutes ; cette donnée est auto-déclarée et n'a pas fait l'objet d'une vérification indépendante[^17]. **Lecture de l'auteur**, sur la classe seulement : cinq des sept critères y sont saturés — complexité du but, supervision humaine, espace de décision, action humaine par construction puisqu'un souscripteur reçoit le mémo, et contraintes denses dès lors que des renseignements personnels sont traités au Québec (article 12.1) et que le modèle sous-jacent relève de la **couverture implicite** d'E-23 **via sa définition large de « modèle »** — inférence d'analystes, non qualification de cet ouvrage (§19.1)[^14]. Le principe du chapitre 13 y conclut à OO3 ou OO4. Le socle ne dit pas où se positionne le système de TD, et cet ouvrage ne le déduit pas d'un gain de temps déclaré.

**Classe 2 — l'acheminement autonome de courriels commerciaux.** Selon les Perspectives de la Banque Scotia de juillet 2025, la banque **déclare** que les capacités agentiques ajoutées à son outil AIDox traitent de façon autonome environ 90 % d'environ 1 500 courriels clients par jour, les cas complexes étant escaladés à un humain ; ces données sont auto-déclarées et n'ont pas fait l'objet d'une vérification indépendante[^18]. **Lecture de l'auteur** : la classe est instructive par ce qu'elle rend indécidable. Un acheminement est-il une « décision fondée exclusivement sur un traitement automatisé » au sens de l'article 12.1[^11] ? Le socle ne le dit pas, et cet ouvrage n'émet pas d'avis juridique. Le critère « contraintes » ne se remplit donc pas par lecture d'un texte, mais par une qualification que l'institution doit assumer et dont le positionnement OO dépend entièrement. **La qualification précède l'architecture.**

**Classe 3 — le paiement de grande valeur sur un rail à sémantique commune.** Lynx a achevé sa bascule vers ISO 20022 le 22 novembre 2025, fin de la coexistence MT/MX[^19]. **Lecture de l'auteur** : la contrainte dominante y est d'une autre nature — non d'explication mais d'exécution, le rail imposant une forme de message et un budget de temps. L'enseignement du préprint s'applique : un délai à tenir ne se confie pas à un composant dont la durée d'exécution n'est pas bornée[^16]. La conclusion — l'agent observe, le rail reste déterministe — est celle qu'instancie le chapitre 23.

**Lecture de l'auteur** : les trois classes se distinguent non par leur degré d'automatisation, mais par la nature de ce qui les contraint — expliquer, qualifier, exécuter. Le socle établit les sept critères et les faits de chaque classe ; il n'établit ni cette tripartition, ni son exhaustivité.

## 19.3 Les points de contrôle obligatoires

Précaution terminologique. Le glossaire réserve « **point de contrôle** » à la traduction de *checkpointing* — la persistance de l'état d'un workflow agentique[^8] — alors que le titre de cette section désigne autre chose : les points où l'architecture doit obligatoirement porter une garantie. Le second peut s'implémenter par le premier ; cet ouvrage écrira « **point de contrôle obligatoire** » pour la seconde notion. La collision est signalée à la gouvernance ; ce chapitre ne modifie pas le glossaire.

Ces points ne sont pas déduits d'une source : ce sont les cinq zones de compensation du chapitre 18, chacune assignée à la couche qui doit la porter. **Quatre deviennent ici des points de contrôle obligatoires ; la cinquième — l'interface d'accès du cadre bancaire (Z4) — n'en est pas un**, faute d'objet : au 16 juillet 2026, aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans les textes officiels ; la candidature de FDX relève du commentaire d'industrie[^20]. Elle est une frontière d'abstraction (§19.4). Un cinquième point s'ajoute, issu non d'une zone mais de la table de traduction du chapitre 13. Total : **cinq points de contrôle obligatoires**.

**PC1 — l'événement de décision.** L'article 12.1 impose d'informer la personne « au plus tard au moment de la décision » — seule des trois obligations à ne pas être subordonnée à une demande[^11]. **Lecture de l'auteur**, posée au chapitre 13 : le moment de la décision doit être un événement daté, émis par la couche d'orchestration. Un système qui ne sait dire quand la décision a été prise ne peut satisfaire une obligation qui se déclenche à cet instant.

**PC2 — la trace d'instance, produite par le cadre.** L'article 12.1 exige, sur demande, « les raisons, ainsi que les principaux facteurs et paramètres, ayant mené à la décision »[^11] : l'objet est l'instance. Le préprint de la TU Munich enseigne que la journalisation confiée aux agents « n'est généralement pas recommandée »[^16] ; le rapport conjoint du Bureau du surintendant des institutions financières et de l'Agence de la consommation en matière financière du Canada établit que les relations causales entre entrées et sorties sont souvent indéterminables[^21]. **Lecture de l'auteur**, posée au chapitre 13 : quatre producteurs candidats, trois écartés — l'agent par le préprint, le modèle par le rapport conjoint, le protocole par la matrice du chapitre 18, dont le typage donne un substrat de frontière et non une trace d'instance. La trace revient au cadre ; aucune source ne désigne ce producteur, l'élimination est de l'auteur (ch. 18 §18.4, Z1).

**PC3 — le point d'arrêt humain.** L'article 12.1 exige l'occasion de présenter ses observations à un membre du personnel « en mesure de réviser la décision »[^11]. Le socle ne documente d'humain dans aucun protocole ; il documente l'humain-dans-la-boucle au niveau d'un cadriciel d'orchestration[^8]. La compensation revient donc à cette couche, et elle est double. **Lecture de l'auteur** : un point d'arrêt ne vaut que si les effets aval de la décision sont bornés — donc défaisables (ch. 13) ; le socle ne l'énonce pas.

**PC4 — la séparation de l'adaptation et de l'évolution.** Le manifeste scinde l'auto-modification en deux régimes : l'**adaptation**, éphémère, d'instance, et l'**évolution**, persistante, qui modifie le modèle de processus[^13]. L'avis 11-348 capte les systèmes dont l'autonomie et l'adaptativité varient après déploiement[^22] ; E-23 attend une surveillance continue visant la « reparamétrisation autonome »[^9]. **Lecture de l'auteur** : un système qui traite les deux régimes par le même chemin technique rend indétectable, dans ses journaux, le moment où une exception est devenue une règle. Deux chemins distincts, donc, et deux régimes d'autorisation. Aucune des trois sources ne l'énonce ; leur conjonction est de l'auteur (ch. 6 ; ch. 13).

**PC5 — le confinement local.** Le manifeste pose l'opérationnalisation **locale** des frames comme frontière de sécurité et de confidentialité : restreindre le contexte et les capacités de chaque agent limite l'impact d'un agent compromis — confinement, non prévention[^13]. Le manifeste nomme aussi le « paradoxe de confidentialité » de l'explicabilité : ce que PC2 exige d'exposer, PC5 exige de restreindre. **Lecture de l'auteur** : l'arbitrage se documente, il ne se déclare pas résolu (ch. 6).

**Lecture de l'auteur** : ces cinq points partagent une propriété que le chapitre 5 nomme. Quatre des cinq propriétés d'évaluation du cadre de la TU Munich — spécificité de tâche, **assurance de correction** (*correctness assurance*), réactivité, **traçabilité/tractabilité** (*traceability / tractability*) — sont celles que l'exploitant **démontre** à un tiers, et ce sont exactement celles que le cadre instrumente ; la cinquième, l'autonomie, n'a au socle aucune métrique[^23]. Les cinq points relèvent tous du premier registre : chacun est un endroit où l'exploitant doit pouvoir produire quelque chose, non un endroit où le système doit être bon.

## 19.4 Alternatives, variantes et frontières d'abstraction

Cette architecture est neutre ; elle n'en est pas moins réalisable, et le socle documente de quoi.

**Pour la couche d'orchestration**, trois réalisations sont au socle : le Microsoft Agent Framework, en disponibilité générale depuis le 3 avril 2026, qui porte les workflows à base de graphes, les points de contrôle et l'humain-dans-la-boucle[^8] ; la plateforme LangGraph, en disponibilité générale depuis le 14 mai 2025, dont le support A2A n'est confirmé de première main que pour la **plateforme commerciale**, non pour la bibliothèque open source `langgraph`[^24] ; et l'orchestration événementielle de Confluent — passée au portefeuille IBM à la clôture du 17 mars 2026 (ch. 22) —, dont les Streaming Agents déclarent un appel d'outils MCP natif et une intégration A2A en préversion ouverte, sans qu'aucun client ni chiffre d'adoption ne figure à la source[^25]. Le chapitre 7 les traite. Temporal, au niveau de preuve [C], ne porte aucun fait central de ce chapitre[^26] ; CrewAI non plus — seul son support A2A est de première main [B], son support MCP et ses chiffres d'adoption restant auto-déclarés au niveau [C] (PRD §7.6, §10.3).

Une seule de ces réserves engage ce chapitre : le socle documente des limites connues du *checkpoint-store* du Microsoft Agent Framework en déploiement distribué multi-pods[^8]. **Lecture de l'auteur** : la persistance de l'état est un mécanisme dont dépend PC3, le point d'arrêt humain ; le socle ne relie le *checkpoint-store* à aucun des autres points. Une limite connue de ce mécanisme est un risque d'architecture, non un détail d'exploitation.

**Pour la variante d'encadrement**, le socle documente une position de fournisseur : le pattern d'architecture « Agentic AI » publié par IBM recommande explicitement les **workflows statiques** (*static workflows*, BPMN/BPEL) pour les processus sous surveillance réglementaire, au nom de l'auditabilité, de la conformité et de transferts définis[^27]. Deux réserves l'encadrent. Le pattern est **générique** : le socle établit qu'IBM ne publie aucune architecture agentique spécifique aux services financiers. Et la convergence dont ce pattern est le troisième terme doit s'énoncer dans sa forme exacte : **le principe est formulé, dans la littérature de la mi-2026, par un manifeste académique, une expérimentation et un pattern de fournisseur, dont deux partagent une autrice et deux une organisation**[^27]. Le chapitre 13 en a tiré la portée.

**Pour la frontière d'abstraction** que constitue Z4 : le cadre des services bancaires axés sur le consommateur exige un standard technique unique, mais au 16 juillet 2026, aucun organisme de normalisation technique n'a été désigné par arrêté ministériel et aucun standard n'est nommé dans les textes officiels ; la candidature de FDX relève du commentaire d'industrie[^20]. Le chapitre 14 en tire la discipline : traiter le standard d'accès comme une variable derrière une frontière d'abstraction. Cette architecture le range en variante de la couche protocolaire, sans lui affecter de composant. L'instrumentation des quatre couches est l'objet du chapitre 20[^1].

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis. **Premièrement**, quatre couches, dont une seule — la gouvernance — porte des attentes opératoires au socle, et seulement pour un texte sur les deux qui entreront en vigueur le 1er mai 2027 ; la protocolaire, la mieux documentée, referme le moins de zones de compensation. **Deuxièmement**, un positionnement OO qui ne se calcule pas : sept critères qualitatifs, dont les « contraintes » ne se réduisent pas aux contraintes réglementaires, et trois classes de processus — expliquer, qualifier, exécuter. **Troisièmement**, cinq points de contrôle obligatoires — événement de décision, trace d'instance produite par le cadre, point d'arrêt humain à effets aval bornés, séparation de l'adaptation et de l'évolution, confinement local —, dont quatre viennent des zones du chapitre 18 ; la cinquième zone n'a pas d'objet tant que le standard technique n'est pas désigné.

Il ne dit pas, en revanche, que cette architecture soit conforme à quoi que ce soit : la conformité est une qualification juridique, et cet ouvrage n'en émet aucune. Il ne dit pas que les cinq points de contrôle obligatoires soient exhaustifs — ils procèdent des cinq zones du chapitre 18 et d'une table de traduction dont une entrée sur six ne produit rien — celle de la ligne directrice de l'AMF, dont le contenu n'est pas au socle (PRD §10.4). L'entrée E-23 de cette table, stérile au chapitre 13, ne l'est plus depuis que l'extraction du 16 juillet 2026 a enrichi F-09 de cinq domaines d'attentes opératoires (§19.1). Il ne dit pas que la taxonomie OO1–OO4 soit validée : elle repose sur une source unique, préprint non révisé par les pairs, sans reproduction indépendante ni application documentée à un processus d'institution financière (ch. 5 ; ch. 21). Il ne dit pas où se positionnent les systèmes canadiens en production. Il ne dit pas, enfin, avec quels composants la bâtir — la Partie VII en documente un cas, et un cas n'est pas une prescription.

Une architecture de référence ne prouve rien : elle range ce qui est démontrable et nomme ce qui ne l'est pas. Dans un domaine où le socle est plus mince que les catalogues, c'est déjà l'essentiel de son office.

---

## Notes

[^1]: PRD §8.4 (neutralité fournisseur — règle « obligatoire — Partie VII et Annexe B »). Le portefeuille IBM est retenu comme **cas d'instanciation documenté par sources primaires**, pas comme recommandation d'achat ni verdict comparatif. Le présent chapitre est en Partie VI : la règle ne le lie pas par son périmètre, mais il l'applique à F-46 (note [^27]), seule position de fournisseur qu'il mobilise. Instanciation : ch. 22 à 24 ; instrumentation : ch. 20.

[^2]: PRD §7.1, **F-01** (niveau [A]). Sources primaires : spécification MCP, révision **2025-11-25** (modelcontextprotocol.io), revalidée le 16 juillet 2026 ; annonce Anthropic de novembre 2024. **Réserve F-01, contraignante ici** : dire « cadre d'autorisation », jamais « sécurisé » — la sécurité dépend de l'implémentation. **Fait chaud (PRD §8.3)** : une révision majeure était attendue le 28 juillet 2026, douze jours après la date de gel du présent chapitre — à resurveiller en P4.1. Anatomie : ch. 2 ; risques : ch. 4.

[^3]: PRD §7.1, **F-02** (niveau [A]). Sources primaires : a2a-protocol.org/latest/announcing-1.0 ; communiqué de la Linux Foundation du 9 avril 2026 ; releases du dépôt a2aproject/A2A. Le socle **ne documente ni l'ancrage de confiance, ni la révocation, ni la gouvernance des clés** des *Signed Agent Cards* (PRD §10.9) : aucune responsabilité de couche n'est construite ici sur ces points. Ch. 2 §2.2.

[^4]: PRD §7.1, **F-04** (niveau [A]). Sources primaires : annonce Google Cloud du 16 septembre 2025 ; communiqué de la Linux Foundation du 9 avril 2026. **Réserve F-04** : endossement déclaré, pas adoption en production vérifiée. Le socle ne porte **ni structure de message, ni mandat, ni preuve d'intention** pour AP2, ni aucun transfert de gouvernance (PRD §10.9) — d'où l'absence de responsabilité de couche assignée à ce protocole. Ch. 3 ; articulation aux rails canadiens : ch. 16 (lacune PRD §10.5).

[^5]: PRD §7.2, **F-07** (niveau [A]). Source primaire : Microsoft Learn (mise à jour juin 2026). Disponibilité générale ~avril-mai 2026 pour tous les clients Entra : identités d'agents et *blueprints*, sur OAuth 2.0 (autorisation) et OpenID Connect (authentification), scénarios *app-only* et délégués. **Réserves du socle, toutes reprises** : sous-fonctionnalités en préversion ; fonctions de sécurité étendues sous licences additionnelles ; les flux OBO/agent-token **étendent** les RFC — ne pas présenter comme du « pur RFC ». **Garde-fou R-2** (PRD §8.1) : « Entra Agent ID inclut un registre d'agents centralisé » est **interdit** (CA-2) — parler d'identités et de *blueprints*. Traitement : ch. 8 §8.1.

[^6]: PRD §7.2, **F-08** (niveau [A] — **statut BROUILLON**). Sources primaires : labs.cloudsecurityalliance.org (spécification « Agent Registry », 27 mars 2026) ; datatracker.ietf.org. Profil d'agent ancré dans l'extension SCIM 2.0 (RFC 7643 + brouillon IETF draft-abbey-scim-agent-extension-00, Okta) ; champs obligatoires `toolAccessList` et `permissionBoundaries`. **Garde-fou R-3** : la spécification **s'appuie sur** SPIFFE/SPIRE comme fondation ; « impose une identité SPIFFE obligatoire » est **interdit**. **§8.2.5** appliqué : brouillon de labs, pas une norme ratifiée ; le brouillon IETF a **expiré le 19 avril 2026** (consolidation en cours, IETF 125) — formulation imposée PRDPlan §4.4 (« statut pré-normatif »). Traitement : ch. 8 §8.2-§8.3.

[^7]: PRD §7.7, **F-37** (niveau [B] — article lu intégralement ; confiance haute pour le cadre, moyenne pour les chiffres). Source primaire : Rinderle-Ma, Mangler et al. (TU Munich), « Design and Implementation of Agentic Orchestrations and Orchestration of Agents », arXiv:2606.31518v1, 30 juin 2026. Formulation imposée (PRDPlan §4.4, cas « préprint académique ») : **préprint non révisé par les pairs** dont les auteurs déclarent eux-mêmes des menaces à la validité (expériences initiales, invites non comparées, facteurs confondants) — le cadre conceptuel est repris ici, les résultats chiffrés à titre d'illustration seulement et **aucun n'est repris dans ce chapitre**. Éléments mobilisés : taxonomie OO1–OO4 (apport 1) ; **sept critères qualitatifs de sélection** — complexité du but, supervision humaine, contraintes, action humaine, espace de décision, effort initial, maintenance (apport 3) ; le socle écrit « contraintes » **sans adjectif** (PRD §6 : « ne pas les restreindre aux contraintes réglementaires »), et ne documente ni pondération, ni fonction de score, ni règle de décision. Traitement : ch. 5.

[^8]: PRD §7.6, **F-15** (niveau [A]). Source primaire : Microsoft Learn (mise à jour du 10 juillet 2026) ; guides de migration DevBlogs. Successeur direct de Semantic Kernel et d'AutoGen ; **GA 1.0 le 3 avril 2026** ; support MCP natif ; orchestration multi-agents par **workflows à base de graphes** avec routage typé, **points de contrôle (*checkpointing*)** et **humain-dans-la-boucle (*human-in-the-loop*)**. **Réserves du socle, mobilisées en §19.4** : SDK Go en préversion ; **limites connues du *checkpoint-store* en déploiement distribué multi-pods** (GitHub discussion #2305). Le socle documente ces deux mécanismes au niveau d'**un cadriciel d'orchestration** — entrée unique, d'où le singulier (constat établi au ch. 18 §18.4, Z2) —, jamais au niveau des protocoles. Formes terminologiques : Annexe D §D.2. Traitement : ch. 7 §7.1.

[^9]: PRD §7.3, **F-09** (niveau **[A/B mixte]** — marquage rectifié au socle, PRD v1.7). L'entrée porte **deux strates de preuve**, et ce chapitre mobilise les deux : **[A]** (vote adversarial 3-0, passes 1-2) pour la date de publication, l'entrée en vigueur, la portée, la définition de « modèle » incluant les méthodes d'IA et d'AA, et le fait que la couverture agentique est une inférence d'analystes ; **[B]** (extraction du texte intégral d'E-23, EN et FR, le 16 juillet 2026 — lecture directe de la source officielle, sans vote adversarial) pour les **exigences opératoires** — cycle de vie, inventaire, cotation, documentation et Appendice 1, surveillance continue — ainsi que pour la vérification négative mécanique. Les cinq domaines d'attentes du §19.1 et de la couche de gouvernance relèvent de la seconde strate ; les faits de date et de portée ci-dessous, de la première. **Point de méthode (1)** : une extraction de source primaire n'« élève » pas une entrée déjà votée 3-0 — dans la taxonomie du PRD §7, [B] est **sous** [A] ; elle l'**enrichit** d'un contenu de rang inférieur. Un état antérieur de cette note écrivait « niveau [B] — élevée [C]→[B] … PRD v1.6 » : **doublement faux** (l'entrée n'a jamais été [C], et [B] n'est pas au-dessus de [A]), et aggravé par l'emploi de cette étiquette sur des faits de strate [A]. Rectifié le 17 juillet 2026 sur le marquage du socle en vigueur, à l'identique des ch. 18 et 20. Source primaire : osfi-bsif.gc.ca, ligne directrice E-23 « Gestion du risque de modélisation (2027) », version finale du 11 septembre 2025, **en vigueur le 1er mai 2027** ; institutions financières fédérales, y compris succursales étrangères dans la mesure compatible ; les régimes de retraite fédéraux sont retirés du périmètre final. **Réserve F-09, contraignante dans tout ce chapitre (PRDPlan §4.4)** : ligne directrice **fondée sur des principes**, rédigée au conditionnel (« should ») — écrire « **attendu par** E-23 », jamais « exigé » ; écrire « **documentation de modèle** » et « **inventaire** », jamais « fiche de modèle » (0 occurrence, EN et FR). Cinq domaines mobilisés : **cycle de vie (§A.4)** à cinq volets, « not necessarily sequential » ; **inventaire (§C.1, principe 2.1)** — « a comprehensive inventory of models whose inherent risk is determined to be non-negligible », « maintained at the enterprise level », « accurate, evergreen » ; **cotation graduée (§A.3, §C.2, principes 2.2-2.3)** — « Each model should be assigned a model risk rating » ; **documentation (§D.2, principe 3.3)** et **Appendice 1 « Information tracking for models »** ; **surveillance continue (§D.2, principe 3.6)** — « processes for handling AI/ML's unique challenges, such as autonomous decision making, autonomous re-parametrization ». **Point de méthode (2)** : le présent chapitre cite F-09 **au socle en vigueur** et non la lecture qu'en faisait le ch. 13, antérieure à l'extraction du 16 juillet 2026 — leçon consignée à la relecture du ch. 18. Traitement : ch. 9.

[^10]: PRD §7.3, **F-25** (niveau [A]). Sources : lautorite.qc.ca ; Norton Rose Fulbright ; rapport annuel Desjardins 2025. Projet publié le 3 juillet 2025 ; **version finale publiée le 30 mars 2026, en vigueur le 1er mai 2027** — même date qu'E-23. **Réserve F-25** appliquée : ne jamais écrire « en attente » ni « en projet » (Annexe D §D.7). Le socle ne porte que le calendrier ; le contenu article par article relève de la lacune PRD §10.4, reprise au ch. 21. **Décompte** : du 16 juillet 2026 au 1er mai 2027 = neuf mois et quinze jours (16 juill. 2026 → 16 avril 2027 = neuf mois ; 16 avril → 1er mai 2027 = quinze jours ; 289 jours) — concordant avec les ch. 9, 11, 14 et 18. Traitement : ch. 11 §11.1.

[^11]: PRD §7.3, **F-27** (niveau [B] — texte officiel consulté sur LégisQuébec). Article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (RLRQ, c. P-39.1), en vigueur depuis le **22 septembre 2023**. Trois obligations, dont les formules entre guillemets sont citées verbatim du texte officiel (Annexe D §D.5 : citer, ne pas paraphraser) : informer « au plus tard au moment de la décision » ; sur demande, communiquer « les raisons, ainsi que les principaux facteurs et paramètres, ayant mené à la décision » ; donner « l'occasion de présenter ses observations à un membre du personnel de l'entreprise en mesure de réviser la décision ». **Réserve d'interprétation du socle (niveau [C])** : selon l'analyse Fasken, une intervention humaine significative avant la décision écarterait l'application de l'article — nuance non confrontée aux positions de la CAI (PRD §10.4) ; **aucun point de contrôle du §19.3 n'est construit sur elle**. La question de savoir si l'article atteint les institutions sous charte fédérale est laissée ouverte au ch. 11. Traitement : ch. 11 §11.2-§11.3 ; traduction en contraintes : ch. 13 §13.1.

[^12]: PRD §7.6, **F-16** (niveau [A]). Source primaire : a2a-protocol.org/latest/announcing-1.0 (« Complementary to MCP, not a replacement »). **Attribution** : cette doctrine est celle du **projet A2A** ; le socle ne documente aucun endossement conjoint par le projet MCP. Le constat qu'« un critère n'est pas une contrainte » est établi au **ch. 2 §2.4**.

[^13]: PRD §7.7, **F-36** (niveau [B] — article lu intégralement ; confiance « haute **pour l'attribution** » : ce qui est établi, c'est que ces auteurs soutiennent ces thèses). Calvanese, De Giacomo, Dumas, Kampik, Montali, Rinderle-Ma, Weber et al. (18 auteurs — universités et industrie, dont IBM Research, SAP et l'Université d'Ottawa), « Agentic Business Process Management: A Research Manifesto », *Information Systems* 140, 102738 (2026) / arXiv:2603.18916v3. Éléments mobilisés : *frames* **normatifs** (déontiques) distincts des *frames* **opérationnels** (apport 2) ; **auto-modification** scindée en **adaptation** (éphémère, d'instance) et **évolution** (persistante, du modèle de processus) (apport 3) ; **opérationnalisation locale des frames comme frontière de sécurité et de confidentialité** (apport 4) ; défi **C2** (sécurité holistique, dont le « paradoxe de confidentialité » de l'explicabilité). **Réserve de sous-caractérisation (PRD §10.10)** : le socle ne caractérise pas le *frame* opérationnel — seul le normatif l'est ; le rapprochement de §19.1 avec `toolAccessList` / `permissionBoundaries` est **de l'auteur** et marqué comme tel. **R-1** : le manifeste cite l'ACP protocolaire (*Agent Communication Protocol*, IBM Research/BeeAI) parmi les protocoles d'interopérabilité — mention antérieure à sa fusion dans A2A, non reprise ici. Traitement : ch. 6.

[^14]: PRD §8.2.4 (règle d'attribution : la couverture agentique d'E-23 est une **inférence d'analystes juridiques** — jamais « le BSIF exige pour l'IA agentique », toujours « couverture implicite via la définition de modèle ») ; **formulation imposée par PRDPlan §4.4**, reproduite intégralement en §19.1, les cinq membres compris. Sur le statut des analystes nommés : ch. 9 ; aucun argument du présent chapitre n'en dépend. Développement : ch. 9 §9.3.

[^15]: Ch. 13 §13.4 (principe directeur et ses quatre conditions) ; PRD §7.7-§7.8, **F-36**, **F-37**, **F-46**. Le principe est une **inférence d'auteur** : le socle n'établit, pour aucune des trois sources, d'application au Canada, à la finance canadienne, à E-23, à la ligne directrice de l'AMF, à l'avis 11-348 ni à l'article 12.1 (encadré du ch. 13 §13.2). « Exigence réglementaire stricte » n'est pas défini par le socle : le verdict du préprint borne son domaine aux situations où des exigences strictes d'exécution et de documentation s'appliquent (F-37, apport 5, processus de don de sang sous directive européenne 2002/98/CE — hors finance et hors Canada).

[^16]: PRD §7.7, **F-37**, apport (4) : enseignements de conception — la journalisation confiée aux agents « n'est généralement pas recommandée » ; les contraintes temporelles exigent des *frames* ou des outils externes, les temps de raisonnement des modèles de langage étant imprévisibles. Source primaire : arXiv:2606.31518v1, sous les réserves de la note [^7]. Ce sont des **énoncés de conception**, distincts des résultats chiffrés (F1 de 0,40 / 0,97 / 1,00 sur un scénario d'éclairage prédictif), lesquels ne sont pas repris ici. Traitement : ch. 5 §5.4.

[^17]: PRD §7.5, **F-17** (niveau [A]). Source primaire : stories.td.com (21 mai 2026). **Règle transversale PRD §7.5 et §8.2.2** : métrique auto-déclarée, attribution obligatoire **à chaque occurrence** ; formulation imposée PRDPlan §4.4 (« métrique auto-déclarée »). Le socle documente une **fonction** (pré-adjudication du prêt garanti par l'immobilier, mémos de synthèse pour souscripteurs) et un **résultat préliminaire déclaré** (~15 heures → moins de 3 minutes) ; il ne documente **ni l'architecture, ni le positionnement OO** du système — voir l'encadré du §19.2. Traitement : ch. 17 §17.1.

[^18]: PRD §7.5, **F-21** (niveau [A]). Sources : scotiabank.com Perspectives (juillet 2025) ; corroboration MIT Sloan Management Review. **Réserve du socle** : page rendue en JS, contenu vérifié par index et corroborations. Métrique auto-déclarée, attribution obligatoire à chaque occurrence (PRD §7.5, §8.2.2). Le socle documente le traitement autonome des courriels clients en services bancaires aux entreprises (~90 % d'environ 1 500 courriels/jour) et l'escalade humaine des cas complexes ; il ne documente **aucune qualification juridique** de cet acheminement au regard de l'article 12.1, et cet ouvrage n'émet aucun avis juridique (PRD §3, non-objectifs). Traitement : ch. 17 §17.2.

[^19]: PRD §7.4, **F-28** (niveau [A]). Sources primaires : payments.ca (deux pages officielles ; corroboration SWIFT, BNY, J.P. Morgan) — votes 3-0 ×4 affirmations. Lynx a atteint l'adoption complète d'ISO 20022 en novembre 2025 : **fin de la coexistence MT/MX le 22 novembre 2025**, alignée sur l'échéance mondiale SWIFT CBPR+. Le **RTR n'est pas mobilisé** dans ce chapitre : sa cible de lancement au T4 2026 et les réserves attachées (R-4 ; réserve F-29 — ne pas écrire « lancé » ni « en production ») relèvent du ch. 15 et du ch. 24. Le flux de paiement instancié relève du ch. 23 (PRD Annexe B.4, flux 2).

[^20]: PRD §7.4, **F-35** (niveau [A] — **fait négatif vérifié 9-0**). Sources primaires : gazette.gc.ca ; canada.ca (communiqué de Finances Canada, page Budget 2025) ; bankofcanada.ca. Formulation imposée par PRDPlan §4.4 (« fait négatif vérifié — standard technique »), reprise intégralement — ancrage temporel et clause FDX compris — en §19.3 et §19.4. **Garde-fou R-5** : « FDX est le standard technique retenu pour le cadre bancaire canadien » est **interdit** (CA-2) ; l'anticipation de FDX relève du **commentaire d'industrie** (Fasken, Bennett Jones, NCFA). Portée du fait négatif : bornée aux chaînes cherchées — « FDX », « Financial Data Exchange », « FAPI », « OAuth » — dans le règlement prépublié, le communiqué et la page Budget 2025. Reconduit par la revalidation du 16 juillet 2026 (`verification/revalidation-2026-07-16.md`) : aucun arrêté de désignation publié. Compléments : **F-11** (C-15, sanction royale du 26 mars 2026) et **F-34** (règlement **prépublié** le 27 juin 2026, commentaires clos le 26 août 2026 — le texte final peut changer). Traitement : ch. 14 §14.4 ; zone Z4 : ch. 18 §18.4 ; flux : ch. 23 §23.4.

[^21]: PRD §7.3, **F-10** (niveau [A]) — **renvoi**. Rapport conjoint du BSIF et de l'ACFC, 24 septembre 2024 (osfi-bsif.gc.ca) : risque de modèle accru propre à l'IA — très grand nombre de paramètres appris de façon autonome, **relations causales entrées-sorties souvent indéterminables**. La projection d'adoption (~70 % d'ici 2026) n'est pas mobilisée ici ; elle est présentée comme projection de ses auteurs au ch. 9 §9.4 (PRD §8.2.6). La conséquence d'architecture est posée au **ch. 13 §13.1** ; le présent chapitre en tire l'assignation de couche.

[^22]: PRD §7.3, **F-26** (niveau [B] — consulté directement sur osc.ca). « CSA Staff Notice and Consultation 11-348 », **5 décembre 2024**. Éléments mobilisés : définition de « système d'IA » incluant explicitement des **niveaux variables d'autonomie et d'adaptativité après déploiement** ; doctrine — les lois existantes s'appliquent, l'avis ne crée ni ne modifie aucune exigence (formule rapportée du socle en français, l'instrument étant en anglais : ce n'est pas une citation verbatim). Le rapprochement avec la scission adaptation/évolution de F-36 est une **inférence d'auteur** posée au ch. 13 §13.1 et reprise ici. Suites de la consultation (close le 31 mars 2025) : lacune PRD §10.4. Traitement : ch. 12.

[^23]: PRD §7.7, **F-37**, apport (2) : cinq propriétés d'évaluation — autonomie, spécificité de tâche, réactivité, **assurance de correction**, **traçabilité/tractabilité** ; apport (3), volet quantitatif : complexité cyclomatique et métrique ABC pour la spécificité ; précision, rappel et F1 pour la correction ; taux de faux négatifs et vitesse de réaction pour la réactivité ; correction du journal pour la traçabilité. **L'entrée F-37 du socle ne rapporte aucune métrique quantitative pour l'autonomie** — constat sur l'entrée du socle, non sur l'article (ch. 5 §5.4 ; PRD §10.10). Le partage des cinq propriétés entre celles qui se démontrent et celle qui ne se mesure pas est une **lecture posée au ch. 5 §5.2**, non un énoncé du socle. Formes terminologiques : Annexe D §D.2. Candidature de ces métriques comme indicateurs de risque de modèle : ch. 20 (inférences marquées).

[^24]: PRD §7.6, **F-32** (niveau [B] — annonce primaire extraite avec citations verbatim). Source : langchain.com/blog (billet de disponibilité générale du **14 mai 2025**) ; docs.langchain.com/langsmith/server-a2a. Métrique **auto-déclarée par l'éditeur** (PRD §8.2.3) : près de 400 entreprises avaient déployé des agents en production via la plateforme depuis la bêta de juin 2024 ; formulation imposée PRDPlan §4.4. **Réserve de périmètre (élévation du 16 juillet 2026)** : le support A2A est confirmé de première main pour **LangGraph Platform / LangSmith Deployment** (endpoint `/a2a/{assistant_id}`), **non pour la bibliothèque open source `langgraph`** (requête ouverte, GitHub langchain-ai/langgraph#7398) — distinction à tenir. Le billet GA ne mentionne ni MCP ni A2A. Traitement : ch. 7 §7.2.

[^25]: PRD §7.6, **F-33** (niveau [B] — annonces primaires extraites avec citations verbatim). Sources : confluent.io/blog (annonce « Streaming Agents », août 2025 ; mise à jour Q1 2026 du **26 février 2026**). Appel d'outils via MCP déclaré nativement ; **intégration A2A en Open Preview** ; communication inter-agents transportée « sur une dorsale Kafka fiable et rejouable ». **Réserves du socle, toutes reprises** : fonctionnalités **pré-GA** (Open Preview / Early Access) ; **aucun client nommé ni chiffre d'adoption** dans la source — l'adoption en production ne peut pas en être inférée. L'acquisition de Confluent par IBM (clôturée le **17 mars 2026** — F-41) fait de cette trajectoire celle du portefeuille IBM : renvoi ch. 22, hors périmètre du présent chapitre. Traitement : ch. 7 §7.3.

[^26]: PRD §7.6, niveau **[C]** (Temporal — billet officiel : intégration OpenAI Agents SDK en Public Preview ; recettes MCP dans docs.temporal.io) ; PRD §10.3 : chiffres d'adoption entreprise non vérifiés. **Règle PRD §10** : « les entrées de niveau [C] du socle ne peuvent porter un fait central sans élévation préalable » — d'où la mention en renvoi seul. Traitement : ch. 7 §7.4.

[^27]: PRD §7.8, **F-46** (niveau [B] ; confiance « haute **pour l'attribution** »). Source primaire : ibm.com/think/architectures/patterns/agentic-ai (pattern officiel « Agentic AI », mis à jour le 21 février 2025, lu via navigateur). Éléments mobilisés : orchestration d'agents par LLM **ou par workflows statiques** (BPMN/BPEL) ; « workflows statiques » **explicitement recommandés pour les processus sous surveillance réglementaire** (auditabilité, conformité, transferts définis). **Réserve du socle** : pattern **générique** — IBM ne publie pas d'architecture agentique spécifique aux services financiers (vérifié : introuvable sur ibm.com/architectures et Redbooks). **Correctif du 16 juillet 2026 (PRD v1.5) — l'adjectif « indépendantes » est RETIRÉ** : Rinderle-Ma cosigne F-36 et F-37 ; IBM Research figure parmi les organisations des 18 auteurs de F-36 et IBM publie F-46. **Formulation imposée**, reprise mot pour mot en §19.4 : « le principe est formulé, dans la littérature de la mi-2026, par un manifeste académique, une expérimentation et un pattern de fournisseur, dont deux partagent une autrice et deux une organisation » — jamais « trois sources indépendantes recommandent l'encadrement déterministe ». **§8.4** : position d'IBM, attribuée, retenue comme cas documenté et non comme recommandation. Portée de la convergence : ch. 13 §13.2.

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026). Volumétrie : cible 3000 ±10 % = 2700-3300.
                                   Ce chapitre porte UN TABLEAU (§19.1). Méthode de décompte reprise du ch. 18
                                   (deux bases, rapportées à la CIBLE) :
                                     B) tableau + titres inclus, délimiteurs « | » et ligne de séparation
                                        exclus ......................................... 3570  +19,0 % : HORS
                                                                                                TOLÉRANCE
                                     C) prose seule (hors tableau et titres) ........... 3289   +9,6 % : CONFORME
                                   ARBITRAGE RETENU (identique au ch. 18) : la consigne porte sur le « corps de
                                   PROSE » ; un tableau n'est pas de la prose. Le décompte C fait donc foi et il
                                   est conforme — mais la marge n'est que de 11 MOTS sous le plafond : toute
                                   reprise du corps doit retirer avant d'ajouter.
                                   HONNÊTETÉ DU JOURNAL : le premier jet de ce bloc annonçait « B 3211 / C 3010,
                                   les DEUX bases conformes » — CHIFFRES INVENTÉS AVANT MESURE. Le jet réel
                                   mesurait C=3846 (+28 %). Les passes de retrait ont ramené C à 3281 ; B reste
                                   hors tolérance. Les deux bases ne sont PAS conformes, contrairement à ce que
                                   ce journal affirmait. Le tableau §19.1 pèse 281 mots (3570-3289) et porte la
                                   responsabilité et le NON-PORTÉ de chaque couche — contenu tracé, non réductible
                                   sans sous-déclarer les quatre couches. Même point de méthode qu'au ch. 18
                                   (sa gouvernance g), à trancher en P4.3 : si B devait faire foi, ce chapitre ET
                                   le ch. 18 sont structurellement hors tolérance et ce sont les cibles de TOC
                                   qu'il faut réviser, pas les tableaux.
                                   APRÈS RELECTURE ADVERSARIALE (2 relecteurs, 4 bloquants + 12 réserves) : les
                                   correctifs ont ajouté ~130 mots de contenu EXIGÉ (attribution §8.2.4 en classe 1,
                                   réserves F-07 au corps, ancrage daté du fait négatif ×2, CrewAI, rattachement
                                   IBM de Confluent, marqueurs PC2/PC3). Pour rester sous plafond, retrait de
                                   DUPLICATION SEULE, jamais de contenu tracé : paragraphe « Trois propositions »
                                   de l'introduction (dupliquait mot pour mot les « Trois acquis » de la
                                   conclusion), reprise du tableau §19.1 dans la prose protocolaire, phrase de
                                   renvoi Partie VII du §19.4 (déjà portée par l'intro et la note [^1]).
                                   Tous les décomptes de ce bloc sont RE-MESURÉS après correctifs (leçon du
                                   CLAUDE.md global : re-vérifier tout décompte annoncé après ajout de contenu).
                                   Commandes reproductibles (F = ce fichier) :
                                     B) awk '/^> \*\*Thèse/{f=1;next} /^## Notes/{f=0} f' F \
                                          | grep -vE '^\|[-| :]+\|$' | sed 's/|/ /g' | wc -w
                                     C) awk '/^> \*\*Thèse/{f=1;next} /^## Notes/{f=0} f' F \
                                          | grep -v '^|' | grep -v '^#' | wc -w
                                   En-tête, exergue de thèse, notes et commentaires exclus dans les deux cas ;
                                   encadré de lacune inclus (contenu exigé par CA-6).
     2. Traçabilité (CA-1, CA-5) . fait (27 notes). Tout fait central tracé : F-01, F-02, F-04, F-07, F-08, F-09,
                                   F-10, F-11, F-15, F-16, F-17, F-21, F-25, F-26, F-27, F-28, F-32, F-33, F-34,
                                   F-35, F-36, F-37, F-46 ; Temporal [C] et F-41 en renvoi seul.
                                   EN-TÊTE RESYNCHRONISÉ sur cette liste (relecture adversariale, réserve 2) : la
                                   ligne « Socle mobilisé » omettait F-35, F-11 et F-34 que ce poste listait
                                   pourtant — désynchronisation en-tête ↔ journal, et sous-déclaration du socle,
                                   que CA-1 contrôle PAR L'EN-TÊTE. F-35 porte un fait central (exclusion de Z4
                                   au §19.3 ; frontière d'abstraction au §19.4) : ajouté nommément, avec F-11 et
                                   F-34 en compléments.
                                   ⚠ SECONDE RESYNCHRONISATION, 17 juill. 2026 (audit, constat m-26) : l'en-tête
                                   rangeait **F-17, F-21 et F-28 « en renvoi »** — sous-déclaration. Ces trois
                                   entrées PORTENT les faits du corps : F-17 la métrique déclarée de TD (§19.2,
                                   classe 1), F-21 celle de la Banque Scotia (classe 2), F-28 la date de bascule
                                   d'ISO 20022 sur Lynx (classe 3) — les trois classes du §19.2 ne tiennent que
                                   par elles. Reclassées comme porteuses ; **F-10 reste en renvoi**, seul de la
                                   liste à l'être réellement (note [^21], mobilisé pour l'indéterminabilité causale
                                   au titre d'un constat posé au ch. 13). MÊME CLASSE DE FAUTE que la première
                                   resynchronisation, et même mécanique : CA-1 contrôle PAR L'EN-TÊTE, or l'en-tête
                                   n'était pas re-dérivé du corps après les correctifs qui y avaient ajouté du
                                   contenu tracé. Un « renvoi » est un fait qu'on peut retirer sans rien perdre ;
                                   ce test n'avait pas été appliqué entrée par entrée.
                                   ⚠ ATTESTATION RECTIFIÉE LE 17 JUILL. 2026 (audit du 17 juill., constat M-13).
                                   Ce poste attestait : « NIVEAUX DE PREUVE VÉRIFIÉS entrée par entrée contre PRD
                                   v1.6 : F-09 est [B] (élevée le 16 juill. 2026) ». ATTESTATION PÉRIMÉE ET FAUSSE,
                                   sur les deux termes. (i) Le socle marque F-09 **[A/B mixte]** depuis PRD v1.7 :
                                   [A] pour les faits des passes 1-2 (vote 3-0) — publication du 11 sept. 2025,
                                   entrée en vigueur du 1er mai 2027, portée, définition de « modèle », couverture
                                   agentique = inférence d'analystes ; [B] pour les exigences opératoires extraites
                                   le 16 juill. 2026 (cycle de vie, inventaire, cotation, documentation, surveillance).
                                   (ii) « élevée [C]→[B] » est la formulation que le PRD déclare lui-même DOUBLEMENT
                                   FAUSSE (§7.3, F-09) : l'entrée n'a jamais été [C], et [B] est SOUS [A] — une
                                   extraction de source primaire n'élève pas une entrée votée 3-0, elle l'ENRICHIT
                                   d'un contenu de rang inférieur (PRD §7 ; CLAUDE.md). Ce chapitre reproduisait la
                                   formule fautive MOT POUR MOT, et sous l'étiquette [B] il rangeait des faits de
                                   strate [A] (version finale du 11 sept. 2025, entrée en vigueur, portée — note [^9]).
                                   La passe corrective de PRD v1.7 avait atteint les ch. 18 et 20, jamais celui-ci :
                                   cascade interrompue, non erreur de lecture. NE PAS SUR-CORRIGER EN SENS INVERSE :
                                   l'entrée n'est pas [B] pour tout (faute commise puis relevée au ch. 18) — le
                                   marquage doit dire, à chaque mobilisation, LAQUELLE des deux strates est mobilisée.
                                   ALIGNÉ SUR PRD v1.7+ : F-09 est **[A/B mixte]**, ce chapitre mobilise les DEUX
                                   strates (note [^9] : [A] pour les dates et la portée du §19.1 ; [B] pour les cinq
                                   domaines d'attentes de la couche de gouvernance et du §19.3, PC4).
                                   NIVEAUX DE PREUVE DES AUTRES ENTRÉES, vérifiés entrée par entrée : F-26, F-27, F-32, F-33, F-36, F-37,
                                   F-46 sont [B] ; F-01, F-02, F-04, F-07, F-08, F-10, F-11, F-15, F-16, F-17, F-21,
                                   F-25, F-28, F-34, F-35 sont [A] ; Temporal [C].
                                   Termes anglais entre parenthèses et en italique à la 1re occurrence du chapitre,
                                   liste RE-VÉRIFIÉE terme à terme contre le corps (17) :
                                   orchestration options, Model Context Protocol, authorization framework,
                                   Agent2Agent, Signed Agent Cards, Agent Payments Protocol, agent identity,
                                   agent registry, checkpointing, human-in-the-loop, frame, operational frame,
                                   Agentic Business Process Management, correctness assurance,
                                   traceability / tractability, static workflows, Agent Communication Protocol
                                   (note [^13], qualifié).
                                   ⚠ CORRIGÉ LE 17 JUILL. 2026 (audit, constat m-27) : « frames » figurait NU dans
                                   la 4e ligne du tableau §19.1 (« le contenu des frames »), soit AVANT sa première
                                   glose, laquelle n'arrivait qu'en prose (« un frame opérationnel (*operational
                                   frame*) », puis « le cadre (*frame*) »). CA-5 impose la glose à la PREMIÈRE
                                   occurrence du chapitre, et le tableau précède la prose : cellule corrigée en
                                   « le contenu des cadres (*frames*) ». La glose de prose de §19.1 est conservée
                                   (redondance sans faute ; la retirer sortirait du périmètre de l'audit).
                                   LEÇON : l'attestation « liste RE-VÉRIFIÉE terme à terme contre le corps » de ce
                                   poste était vraie sur l'ENSEMBLE des termes et fausse sur leur RANG — elle
                                   contrôlait la présence des gloses, pas leur position. Un tableau de §19.1 est du
                                   corps ; il était hors du champ de la re-vérification sans que celle-ci le dise.
                                   ⚠ « normative frame » RETIRÉ de cette liste (relecture adversariale, réserve 12) :
                                   le jet antérieur le déclarait glosé à sa 1re occurrence, mais le terme est
                                   ABSENT du corps — `grep -inE "normati"` ne ressort que « pré-normatif(s) » (×2).
                                   Ce chapitre ne mobilise que le frame OPÉRATIONNEL (§19.1), ce qui est cohérent
                                   avec son propos : le défaut était dans l'attestation, pas dans le texte —
                                   aucune modification du corps requise. Même classe de faute que la volumétrie
                                   inventée ci-dessus : décompte annoncé, jamais mesuré.
                                   Marqueur d'inférence unique imposé (PRDPlan §4.4) : « Lecture de l'auteur »
                                   — 15 occurrences au corps, recomptées par extraction après correctifs (12 au
                                   jet antérieur ; +3 : PC2, PC3 et le principe directeur du §19.2). Aucun emploi
                                   d'« inférence de lecture ». « inférence d'auteur » : 0 occurrence AU CORPS —
                                   la forme est réservée aux notes (lien de tableau, PRD B.3/§8.2.4) ; l'emploi
                                   fautif du §19.2 (prose) est corrigé en « Lecture de l'auteur » (réserve 11).
     3. Balayage garde-fous ...... fait :
                                   - réserve F-09 (motif « exigé par E-23|E-23 impose|exigence.*E-23|fiche de
                                     modèle|model card ») : « exigé par E-23 » = 0 ; « E-23 impose » = 0 ;
                                     « fiche de modèle » / « model card » = 0 (« documentation de modèle » et
                                     « inventaire » employés) ; « exigence.*E-23 » : 0 au corps. Formes employées :
                                     « attendu par E-23 », « les attentes », « E-23 attend ».
                                     ⚠ MOTIF ÉLARGI À `oblig` (relecture adversariale, constat bloquant 3) : le
                                     motif du plan ne capte QUE « exigé/exigence/impose » et laissait passer le
                                     verbe « obliger ». Le jet antérieur écrivait « les deux [textes] OBLIGERONT
                                     le même jour » (§19.1) et « un texte sur les deux qui OBLIGERONT le 1er mai
                                     2027 » (conclusion) — soit exactement ce que la réserve F-09 interdit (ligne
                                     fondée sur des principes, rédigée au conditionnel : elle n'oblige pas, elle
                                     attend), et, pour l'AMF, une force obligatoire que le socle n'établit PAS
                                     (F-25 ne porte que le calendrier). Corrigé aux deux endroits en « entreront
                                     en vigueur » (forme datée neutre). Balayage `oblig` re-passé : 2 occurrences
                                     restantes, toutes deux innocentes (« obliger à dire » §19.1 ; « obligatoirement
                                     porter une garantie » §19.3) ; « obligeront » = 0. Élargissement du motif
                                     §4.3 à signaler à la gouvernance ;
                                   - réserve F-01 (motif « sécuris ») : « sécurisé » n'apparaît qu'en négation
                                     explicite (§19.1) ; « cadre d'autorisation » partout ailleurs ;
                                   - R-2 (motif « registre centralisé|Entra.*registre ») : 1 occurrence, verbatim
                                     EXTRAIT du corps par la commande de balayage elle-même — « Le socle ne
                                     documente pas de registre d'agents centralisé pour cette capacité, et cet
                                     ouvrage n'en écrira pas : absence de documentation, non fait négatif vérifié
                                     (R-2) » ; « identités et *blueprints* » employé.
                                     ⚠ RÈGLE CONSIGNÉE (relecture adversariale, constat bloquant 2) : le jet
                                     antérieur portait ici, ENTRE GUILLEMETS, une phrase de négation du registre
                                     centralisé ABSENTE du corps — recopiée d'un jet mort et jamais revérifiée.
                                     Elle n'existait QUE dans ce bloc : le journal citait sa propre citation, et
                                     le contrôle R-2 devenait irreconstituable sans rouvrir le fichier. La chaîne
                                     fautive n'est pas reproduite ici, pour ne pas la réintroduire dans le fichier
                                     qu'elle est censée décrire. AUCUN verbatim ne peut être porté à ce bloc sans
                                     avoir été extrait du fichier par la commande de balayage elle-même — jamais
                                     recopié d'un jet antérieur ni de mémoire ;
                                   - R-3 (motif « SPIFFE|SVID ») : 1 occurrence — « s'appuie sur », jamais
                                     « impose » ; « SVID » = 0 ;
                                   - §8.2.5 (motif « CSA|SCIM|IETF ») : 4 occurrences au corps, recomptées par
                                     extraction (CSA ×1, SCIM ×2, IETF ×1 — le jet antérieur annonçait 3, décompte
                                     faux) ; toutes assorties du statut pré-normatif (brouillon de labs ; brouillon
                                     IETF expiré le 19 avril 2026) ;
                                   - R-4 / réserve F-29 (motif « RTR|Real-Time Rail|T4 2026 ») : 0 occurrence au
                                     corps — le RTR est explicitement écarté du chapitre (note [^19]) ; la classe 3
                                     est bâtie sur Lynx (F-28, fait accompli) ;
                                   - R-5 (motif « FDX|Financial Data Exchange|standard technique ») : 4 occurrences
                                     au corps, recomptées par extraction, toutes inspectées ; FDX n'apparaît qu'au
                                     titre du commentaire d'industrie.
                                     ⚠ CORRIGÉ (relecture adversariale, réserves 3 et 8) : le jet antérieur
                                     affirmait la formulation imposée §4.4 « reprise MOT POUR MOT en §19.3 et
                                     §19.4 » — affirmation FAUSSE pour les deux. Le §19.3 supprimait l'ancrage
                                     temporel « Au [date] » ET la clause FDX ; le §19.4 supprimait l'ancrage
                                     temporel. Or l'ancrage est ce qui borne un fait négatif dans le temps et le
                                     rend revalidable (§8.3 ; la désignation par arrêté est la lacune §10.1 « à
                                     surveiller ») — sans date, un fait négatif se lit comme permanent. Forme
                                     complète restaurée aux DEUX endroits : « au 16 juillet 2026 » + clause FDX ;
                                     vérifié par extraction = 2 occurrences de « au 16 juillet 2026, aucun
                                     organisme ». Note [^20] corrigée (« reprise intégralement », plus « mot pour
                                     mot ») ;
                                   - réserve F-25 (motif « en attente|en projet ») : 0 occurrence fautive ; forme
                                     datée employée (« finale depuis le 30 mars 2026, en vigueur le 1er mai 2027 ») ;
                                   - R-6 (motif « Gartner|Magic Quadrant|iPaaS ») : 0 occurrence ;
                                   - R-7 (motif « E-23|B-13 ») : « E-23 » ressort 11 fois au corps (recompté par
                                     extraction après correctifs), TOUTES
                                     inspectées une à une, TOUTES en contexte réglementaire pur — aucune
                                     correspondance produit ↔ réglementation n'est posée dans ce chapitre
                                     (territoire des ch. 20 et 23) : filtré, PRDPlan §4.3. « B-13 » = 0 au corps.
                                     Le seul voisinage produit ↔ E-23 du chapitre est le rapprochement registre
                                     d'agents ↔ inventaire, qui est posé pour être ÉCARTÉ (§19.1) ;
                                   - R-1 et R-8 (motifs « ACP », « control plane », « plan de contrôle ») : le corps
                                     n'en porte AUCUNE occurrence ; « ACP » apparaît une seule fois, en note [^13],
                                     sous sa forme qualifiée complète (« l'ACP protocolaire (*Agent Communication
                                     Protocol*, IBM Research/BeeAI) »), au passé, pour écarter la mention du
                                     manifeste. Sigle nu : 0. « control plane » / « plan de contrôle » : 0 —
                                     le positionnement d'IBM (branche c) n'est pas mobilisé ici (ch. 22) ;
                                   - §8.2.2 / §7.5 (motifs « [0-9]+ ?% », « heures », « M$|G$ ») : 2 métriques
                                     institutionnelles au corps (TD ~15 h → <3 min ; Scotia ~90 % de ~1 500
                                     courriels/jour), TOUTES DEUX portant l'attribution nominative à la source
                                     primaire ET la formule imposée §4.4 (« déclare » + « auto-déclarée et n'a pas
                                     fait l'objet d'une vérification indépendante ») — règle §7.5 : à CHAQUE
                                     occurrence ; chacune n'apparaît qu'une fois ;
                                   - §8.2.3 (métriques d'éditeurs) : 0 occurrence AU CORPS après resserrement —
                                     le « ~400 entreprises » de LangGraph a été retiré du corps (il ne servait
                                     aucun argument de ce chapitre) et ne subsiste qu'en note [^24], où il porte
                                     l'attribution à LangChain et la qualification d'auto-déclaré ;
                                   - §8.2.6 (motif « 70 % ») : 0 occurrence — F-10 mobilisé pour l'indéterminabilité
                                     causale seulement, la projection explicitement écartée (note [^21]) ;
                                   - §8.2.7 (motif « Forrester|TEI|Celent|ROI ») : 0 occurrence réelle.
                                     ⚠ PIÈGE DE BALAYAGE À SIGNALER (PRDPlan §4.3) : passé en `rg -i` sans bornes
                                     de mot, ce motif ressort 17 fois sur ce chapitre — « ROI » matche à
                                     l'intérieur de « trois », « droit », « introduit ». Tous faux positifs :
                                     avec `\b(Forrester|TEI|Celent|ROI)\b`, 0 occurrence. Le motif du plan est à
                                     border en P4.2, sans quoi CA-3 produira 17 fausses alertes par chapitre ;
                                   - §8.4 : le chapitre est en Partie VI, hors périmètre déclaré du garde-fou —
                                     mais F-46 est la seule position de fournisseur mobilisée et elle est traitée
                                     sous §8.4 : attribuée à IBM, réserve de généricité dite, formulation de
                                     convergence imposée reprise mot pour mot, aucun superlatif, aucune
                                     recommandation. Les trois réalisations d'orchestration (F-15, F-32, F-33)
                                     sont exposées avec LEURS RÉSERVES (checkpoint-store multi-pods ; périmètre
                                     A2A de LangGraph ; pré-GA et absence de client nommé chez Confluent) : les
                                     faits négatifs du socle sont exposés au même titre que les capacités.
                                     ⚠ CORRIGÉ (réserve 9) : le §19.4 s'ouvre sur « Cette architecture est neutre »
                                     et l'introduction promet « aucun composant d'éditeur n'y est prescrit », mais
                                     le corps énumérait Microsoft, LangGraph et Confluent À PARITÉ, sans dire que
                                     la troisième est filiale à 100 % d'IBM depuis la clôture du 17 mars 2026
                                     (F-41). Le PRD §8.4 qualifie lui-même « Confluent PRÉ-ACQUISITION » quand il
                                     la range parmi les alternatives non-IBM : le socle distingue les deux états,
                                     le corps les confondait. Un lecteur vérifiant la neutralité sur le corps seul
                                     concluait à trois éditeurs indépendants ; il y en a deux plus une trajectoire
                                     IBM. La note [^25] portait déjà le fait, mais c'est le CORPS qui porte la
                                     déclaration de neutralité : rattachement rendu visible en incise (12 mots),
                                     sans empiéter sur le ch. 22.
     4. Arithmétique ............. tous les décomptes posés à partir des dates et chiffres du socle, deux fois :
                                   - 4 couches (protocoles ; identité et registre ; orchestration ; gouvernance) :
                                     imposées par PRD §6 et TOC ; recomptées sur le tableau §19.1 = 4 lignes.
                                   - 5 zones de compensation au ch. 18 (Z1..Z5) → 4 points de contrôle obligatoires
                                     (Z1→PC2, Z2→PC3, Z3→PC4, Z5→PC5) + 1 zone SANS objet de contrôle (Z4, standard
                                     non désigné — F-35) + 1 point issu de la table du ch. 13 §13.1 (PC1, obligation
                                     d'informer, F-27) = 5 points de contrôle obligatoires. Vérifié : 4 + 1 = 5
                                     points ; 4 + 1 = 5 zones. Les deux « 5 » ne recouvrent PAS le même ensemble —
                                     le texte le dit explicitement plutôt que de laisser croire à une bijection.
                                   - 5 domaines d'attentes opératoires d'E-23 (cycle de vie, inventaire, cotation,
                                     documentation, surveillance) : recomptés contre F-09, strate [B] (17 juill.
                                     2026 — le pointeur « v1.6 » de ce poste est retiré : le socle en vigueur
                                     marque l'entrée [A/B mixte] depuis v1.7, et le décompte de 5 est inchangé
                                     par la rectification, qui portait sur l'étiquette et non sur le contenu).
                                   - 5 volets du cycle de vie d'E-23 (conception, revue, déploiement, surveillance,
                                     mise hors service) : F-09 ; non énumérés au corps, seul le décompte est repris.
                                   - 7 critères de sélection (F-37) : énumérés et recomptés = 7.
                                   - 5 propriétés d'évaluation (F-37), dont 4 instrumentées et 1 sans métrique
                                     au socle (autonomie) : 4 + 1 = 5. CONFORME (ch. 5 §5.4).
                                   - 5 des 7 critères saturés en classe 1 : recomptés au texte — complexité du but,
                                     supervision humaine, espace de décision, action humaine, contraintes = 5 ;
                                     les 2 restants (effort initial, maintenance) ne sont pas des propriétés du
                                     processus mais de son coût de possession (ch. 5 §5.3) — d'où « cinq des sept ».
                                   - 3 obligations de l'art. 12.1 (F-27) ; 3 classes de processus ; 3 réalisations
                                     d'orchestration au socle (F-15, F-32, F-33) + Temporal [C] écarté ET CrewAI
                                     écarté avec son motif (relecture adversariale, réserve 6 : le jet antérieur
                                     omettait CrewAI SANS motif alors qu'il écartait Temporal AVEC le sien —
                                     traitement asymétrique. PRD §6 nomme CrewAI parmi les réalisations de la
                                     Partie II et son support A2A est élevé [B] depuis le 16 juill. 2026 ; son
                                     support MCP et ses chiffres d'adoption restent [C] : il ne porte donc aucun
                                     fait central, comme Temporal. Le décompte de 3 est maintenu, l'omission
                                     est comblée au corps §19.4).
                                   - PC2 : 4 producteurs candidats, 3 écartés (agent — F-37 ; modèle — F-10 ;
                                     protocole — matrice ch. 18 §18.4, Z1). CORRIGÉ (réserve 5) : le jet antérieur
                                     écrivait « 3 candidats, 2 écartés », décompte du ch. 13 qui PERD l'apport
                                     propre du ch. 18 — l'exclusion du protocole — alors que le chapitre ouvre en
                                     revendiquant cet héritage et que PC2 EST la zone Z1.
                                   - RETIRÉ (réserve 1) : « la persistance de l'état est le mécanisme dont dépendent
                                     DEUX des cinq points de contrôle » (§19.4) — décompte dérivé NON vérifiable,
                                     que ce poste 4 n'avait pas posé malgré sa clause « Aucun autre calcul n'est
                                     posé dans ce chapitre » (le journal se déclarait donc exhaustif à tort). Rien
                                     au socle ni au chapitre n'établit cette dépendance pour deux points exactement ;
                                     F-15 documente le *checkpointing* sans le relier à aucun des cinq points, qui
                                     sont construits par ce chapitre. Remplacé par un énoncé borné et nommé : la
                                     persistance de l'état est UN mécanisme dont dépend PC3, le socle ne la reliant
                                     à aucun autre point.
                                   - neuf mois et quinze jours (16 juill. 2026 → 1er mai 2027 = 289 j) : recalculé
                                     à partir des dates du socle (F-09, F-25), concordant avec les ch. 9, 11, 14, 18.
                                   - douze jours (16 juill. → 28 juill. 2026, révision MCP) : recalculé, concordant
                                     avec les ch. 2, 4 et 18 (note [^2] seulement).
                                   - 15 croisements et 5 zones au ch. 18 : repris tels quels, revérifiés contre le
                                     ch. 18 fusionné.
                                   - 18 auteurs du manifeste (F-36) ; « deux partagent une autrice et deux une
                                     organisation » (F-46, formulation imposée) : conformes au socle.
                                   Aucun autre calcul n'est posé dans ce chapitre.
     5. Relecture adversariale ... FAITE (2 relecteurs indépendants, distincts du rédacteur — PRDPlan §4.2.4).
                                   Premier jet RÉFUTÉ : 4 constats bloquants + 12 réserves. Décomptes concordants
                                   des deux relecteurs (C=3281). TOUS LES CONSTATS VÉRIFIÉS AU SOCLE AVANT
                                   APPLICATION ; aucun n'était infondé ; tous appliqués.
                                   BLOQUANTS CORRIGÉS :
                                   1) Conclusion, « deux entrées sur six ne produisent rien, faute que le socle
                                      porte le contenu de la ligne directrice de l'AMF » : DOUBLE FAUTE.
                                      (a) misattribution — les deux entrées stériles du ch. 13 sont E-23 ET l'AMF,
                                      l'entrée E-23 l'étant pour un motif distinct (aucune exigence opératoire au
                                      socle À L'ÉPOQUE) ; (b) contradiction interne — le §19.1 du MÊME chapitre
                                      affirme, sur F-09 tel qu'enrichi par l'extraction du 16 juill. 2026, que le
                                      socle porte cinq domaines d'attentes, et la note
                                      [^9] déclare la lecture du ch. 13 « PÉRIMÉ, non repris » : la conclusion
                                      citait pourtant un décompte qui dépend de cette lecture morte. Au socle
                                      postérieur à l'extraction, le décompte est 1/6, pas 2/6. Corrigé, avec renvoi
                                      explicite à l'enrichissement de F-09 (§19.1) — les pointeurs « v1.6 » et le
                                      mot « élévation » de ce paragraphe sont rectifiés le 17 juill. 2026 (audit,
                                      M-13) : ce que l'extraction a produit est un ENRICHISSEMENT de rang inférieur,
                                      et le constat de fond du relecteur (décompte 1/6) est inchangé.
                                      → gouvernance (a) : le ch. 13 §13.1 et §13.4 portent
                                      EUX-MÊMES la lecture périmée et doivent être repris en P4.
                                   2) Journal, R-2 : CITATION FABRIQUÉE — voir poste 3, règle consignée.
                                   3) §19.1 (l. 46) et conclusion : « les deux [textes] OBLIGERONT » — voir poste 3,
                                      motif élargi à `oblig`. → gouvernance (b).
                                   4) §19.2 classe 1 : « dès lors que […] le modèle sous-jacent ENTRE DANS LE
                                      PÉRIMÈTRE attendu par E-23 » posait la couverture agentique en PRÉMISSE, sur
                                      un système NOMMÉ d'une institution NOMMÉE (F-17, TD/Layer 6), alors que
                                      §8.2.4 la réserve à une inférence d'analystes juridiques, à attribuer à eux
                                      et jamais à l'auteur — le marqueur « Lecture de l'auteur » n'y remédiait pas.
                                      Incohérence décisive : la classe 2 REFUSE ce geste (« cet ouvrage n'émet pas
                                      d'avis juridique ») et la conclusion promet n'émettre aucune qualification de
                                      conformité ; la classe 1 en émettait une. Reformulé en « couverture implicite
                                      via sa définition large de "modèle" — inférence d'analystes, non qualification
                                      de cet ouvrage », renvoi [^14].
                                   RÉSERVES CORRIGÉES : 12/12 — en-tête resynchronisé (F-35/F-11/F-34, poste 2) ;
                                   note [^20] « mot pour mot » → « intégralement » et ancrage daté restauré ×2
                                   (poste 3) ; réserves F-07 (préversion, extension des RFC) portées AU CORPS et
                                   négation « ni base d'inventaire d'entreprise » RETIRÉE — sans appui au socle,
                                   elle convertissait une absence de documentation en fait négatif vérifié, ce que
                                   §4.4 interdit ; PC2 aligné sur le ch. 18 (4 candidats, 3 écartés) ; CrewAI traité
                                   avec son motif ; marqueurs ajoutés à PC2 et PC3 (PC1/PC4/PC5 les portaient déjà) ;
                                   Confluent rattaché au portefeuille IBM au corps ; décompte « deux des cinq
                                   points » retiré ; « inférence d'auteur » en prose → « Lecture de l'auteur » ;
                                   « normative frame » retiré de la liste CA-5 (poste 2).
                                   POINTS QUE LES RELECTEURS ONT CONTRÔLÉS SANS RIEN TROUVER À REPRENDRE :
                                   a) §19.2, classes de processus construites sur F-17/F-21 — le texte se défend
                                      explicitement (encadré + « sur la classe seulement » + « le socle ne dit pas
                                      où se positionne le système de TD ») ; tenu.
                                   b) §19.1, rapprochement `toolAccessList`/`permissionBoundaries` ↔ frame
                                      opérationnel (PRD §10.10) : marqué, borné, et ne fonde aucun point du §19.3.
                                   c) §19.3, PC1 : repris du ch. 13 §13.1 comme inférence, pas comme lecture d'un
                                      texte.
                                   d) « neuf mois et quinze jours » et double date du 1er mai 2027 : recalculés.
     6. Passe de correction ...... 17 juill. 2026 — AUDIT GLOBAL DU 17 JUILL. 2026, constats M-13, m-26, m-27.
        (audit du 17 juill. 2026)  Aucune réécriture ; date de gel INCHANGÉE (16 juillet 2026). Quatre corrections :
                                   (a) M-13 — marquage F-09 : note [^9] refondue sur le modèle des ch. 18 et 20
                                       (deux strates explicitées, [A] pour les faits votés 3-0, [B] pour les
                                       exigences opératoires du 16 juill.) ; prose de la conclusion (« depuis
                                       l'élévation de F-09 en [B] » → « depuis que l'extraction du 16 juillet 2026
                                       a enrichi F-09 de cinq domaines d'attentes opératoires ») ; attestation du
                                       poste 2 rectifiée et datée ; pointeurs « v1.6 » du poste 4 et du poste 5
                                       retirés. BALAYAGE DE COMPLÉTUDE, exigé parce que c'est l'incomplétude de la
                                       passe v1.7 qui a produit ce constat — motif `élev|v1\.6|\[C\]→\[B\]` passé
                                       sur le FICHIER ENTIER, corps, notes et journal : 6 occurrences trouvées,
                                       5 traitées, 1 CONSERVÉE À DESSEIN (poste 4, « son support A2A est élevé [B]
                                       depuis le 16 juill. 2026 » — CrewAI, non F-09 : là, [C]→[B] est une VRAIE
                                       élévation, attestée par PRD §10.3. Sur-corriger celle-là aurait été la faute
                                       symétrique de celle qu'on corrige).
                                   (b) m-26 — en-tête : F-17, F-21, F-28 reclassés de « renvoi » à porteurs
                                       (voir poste 2).
                                   (c) m-27 — CA-5 : glose de « frames » portée à sa première occurrence, dans le
                                       tableau §19.1 (voir poste 2).
                                   VOLUMÉTRIE RE-MESURÉE APRÈS CES CORRECTIONS (leçon du CLAUDE.md global : tout
                                   décompte annoncé est re-vérifié après ajout de contenu — c'est l'omission de ce
                                   geste que l'audit sanctionne en m-30 et m-31 sur le ch. 21). Commandes B et C
                                   du poste 1, réexécutées : B = 3576 ; C = 3294. Le décompte C fait foi
                                   (arbitrage du poste 1, inchangé) : 3294 sur un plafond de 3300 — CONFORME, marge
                                   de 6 MOTS. La marge s'est resserrée de 11 à 6 : les corrections (a) et (b) ne
                                   touchent que l'en-tête, les notes et le journal, tous hors décompte ; seuls les
                                   +5 mots de la prose de conclusion pèsent. La glose de « frames » (+1 mot) pèse
                                   sur B seul, le tableau étant hors de la base C. AVERTISSEMENT MAINTENU ET
                                   DURCI : toute reprise du corps doit retirer avant d'ajouter.
-->
