# Chapitre 37 — Souveraineté

*Question directrice : où tournent les agents, et sous quelle juridiction ?*

> **État de référence :** Cloud Sovereignty Framework 1.2.1 (octobre 2025), Gaia-X Compliance Document 25.10, IDSA Rulebook 2026-1 et document de position de l'IDSA (9 juillet 2026). Les numéros entre crochets renvoient aux sources en fin de chapitre, toutes lues; [12] à [15] ont été ajoutées le 14 novembre 2026, dont [14] et [15] sont secondaires.

Une application classique a une adresse. Un agent en a plusieurs : le modèle de langage tourne chez un fournisseur d'inférence, la boucle d'orchestration ailleurs, la mémoire dans une base, les outils derrière des serveurs MCP, les traces dans une plateforme d'observabilité. Chaque appel fait circuler des données d'entreprise entre ces lieux, et chacun relève d'un exploitant, donc d'un droit.

La résidence des données est nécessaire, mais c'est le contrôle juridictionnel, soit la capacité d'une autorité à contraindre un exploitant, qui décide de la souveraineté. Les espaces de données européens offrent déjà un modèle de partage sous contrôle entre organisations, où les agents entrent sans nouveau protocole; ils y ajoutent un participant, le modèle lui-même.

---

## 37.1 Résidence ou contrôle juridictionnel

### Deux questions distinctes

La **résidence** porte sur le lieu : où les données sont-elles stockées et traitées ? Le **contrôle juridictionnel** porte sur l'autorité : qui peut obliger l'exploitant à les remettre ?

Le droit américain montre que les deux se séparent. L'article 2713 du titre 18 du U.S. Code, ajouté en 2018 par le CLOUD Act, oblige un fournisseur de services à respecter ses obligations de conservation et de communication, que les données se trouvent aux États-Unis ou à l'étranger. Le critère est la « possession, custody, or control » des données [1], non le lieu du serveur.

Le droit européen pose l'obligation inverse. L'article 32 du Data Act, applicable depuis le 12 septembre 2025, oblige les fournisseurs de services de traitement de données à prendre des mesures techniques, organisationnelles et juridiques contre tout accès gouvernemental de pays tiers aux données non personnelles détenues dans l'Union qui entrerait en conflit avec le droit de l'Union ou d'un État membre [2]. Une décision étrangère n'est reconnue que si elle repose sur un accord international; à défaut, le transfert obéit à des conditions strictes, se limite au minimum et, sauf exception liée aux enquêtes, est d'abord signalé au client.

Un fournisseur soumis aux deux régimes fait face à des obligations contraires. Pour son client, une région locale chez un fournisseur étranger règle la résidence, pas la juridiction.

### Une échelle pour mesurer

La Commission européenne a traduit cette distinction en grille d'achat. Son Cloud Sovereignty Framework évalue une offre selon huit objectifs, du juridique à la chaîne d'approvisionnement, et attribue à chacun un niveau d'assurance, le SEAL [3].

| Niveau | Intitulé | Sens |
|---|---|---|
| SEAL-0 | Aucune souveraineté | Contrôle exclusif de tiers hors UE, droit hors UE |
| SEAL-1 | Souveraineté juridictionnelle | Droit de l'UE applicable en principe, peu exécutoire en pratique |
| SEAL-2 | Souveraineté des données | Droit de l'UE exécutoire; contrôle indirect de tiers hors UE |
| SEAL-3 | Résilience numérique | Influence réelle mais incomplète d'acteurs de l'UE |
| SEAL-4 | Souveraineté numérique complète | Contrôle entier de l'UE, aucune dépendance critique |

L'appel d'offres fixe un niveau minimal par objectif; l'offre qui ne l'atteint pas est rejetée. L'objectif juridique pèse l'exposition aux lois étrangères extraterritoriales. L'objectif « données et IA » y ajoute le contrôle exclusif du client sur les clés de chiffrement, l'auditabilité de l'usage des modèles, et la mesure dans laquelle les modèles sont développés, entraînés, hébergés et gouvernés sous contrôle européen [3]. Le modèle entre ainsi dans le périmètre de la souveraineté au même titre que le stockage.

Ce cadre est un instrument de marché public européen : sa structure se transpose ailleurs, ses seuils non. Le cas canadien est traité au chapitre 38.

### Trois instruments en mouvement

Trois textes prolongent cette grille, à des stades inégaux.

**SecNumCloud, en France.** Le référentiel de l'ANSSI, dont la version 3.2 date de mars 2022, ajoute aux exigences de sécurité une protection contre le droit extra-européen : le prestataire doit avoir son siège dans un État membre de l'Union, et son actionnariat est encadré pour limiter le poids d'entités non européennes [15]. Un arrêté du 12 août 2026 a approuvé ce référentiel pour les prestataires qui traitent des données particulièrement sensibles de l'État, de ses opérateurs et de ses groupements d'intérêt public; la conformité s'atteste par une qualification de l'ANSSI ou par une certification européenne jugée équivalente [14]. Le texte du référentiel n'a pas pu être chargé : ces éléments viennent de deux commentaires de cabinets.

**EUCS, bloqué.** Le schéma européen de certification des services infonuagiques, dont l'ENISA a publié un premier projet en décembre 2020, devait porter au niveau de l'Union une exigence du même ordre : siège et contrôle européens pour le niveau d'assurance le plus élevé. Sept États s'y sont opposés en 2022; quatre l'ont soutenue, dont la France et l'Allemagne. La version de mars 2024 l'a retirée et a renvoyé la question aux régulateurs nationaux [13]. Le schéma n'était adopté ni en novembre 2025 [13] ni en juin 2026, selon la Commission, qui annonce la reprise des travaux [12].

**Le Cloud and AI Development Act, proposé.** La Commission a déposé le 3 juin 2026 une proposition de règlement qui reprend l'idée par une autre voie [12]. Elle crée un cadre de souveraineté des services infonuagiques à quatre niveaux d'assurance, reconnus dans toute l'Union : le premier sur déclaration de conformité du fournisseur, les autres après audit. Les États membres évalueraient quels usages publics exigent quel niveau, l'objectif étant que les usages hautement critiques du secteur public reposent d'ici 2035 sur des services souverains. Un service contrôlé depuis un pays tiers ne pourrait prétendre au troisième niveau que si ce pays bénéficie d'une décision d'adéquation et n'a aucune mesure contraire aux règles d'accès de l'article 32 du Data Act. L'exposé des motifs chiffre la dépendance : la part de marché des fournisseurs européens est passée de 29 % en 2017 à 15 % en 2022, et trois fournisseurs non européens détiennent plus de 70 % du marché.

La proposition nomme les agents. Un considérant prévoit des plateformes d'IA souveraines pour déployer et orchestrer des agents à grande échelle, avec des cadres d'orchestration qui assurent la transparence et l'imputabilité des interactions entre agents, et des méthodes d'essai pour limiter les comportements autonomes imprévus [12]. Ce n'est qu'un considérant d'un texte non adopté, applicable au plus tôt un an après son entrée en vigueur. Il signale toutefois que la souveraineté européenne s'étend de l'hébergement à l'orchestration.

---

## 37.2 Gaia-X et espaces de données

Un espace de données est un écosystème fédéré où des organisations indépendantes partagent des données selon des règles, des politiques et des contrats communs, chacune gardant le contrôle de ses actifs [9][10].

**Gaia-X** définit des critères de conformité pour les offres de services. Son Compliance Document 25.10 distingue une conformité standard et trois niveaux de label, et décrit les offres par des justificatifs vérifiables [4].

La section « European Control » du document reprend la distinction de la section 37.1 [5]. À tous les niveaux, le fournisseur s'interdit d'accéder aux données du client sans son autorisation, sauf si le droit applicable l'exige, sans préciser lequel. Au niveau 2, il doit offrir l'option d'un traitement et d'un stockage exclusivement dans l'UE ou l'EEE. Au niveau 3, cette localisation devient obligatoire, et cinq exigences s'ajoutent : un fournisseur établi dans un État de l'UE ou de l'EEE, l'absence de contrôle par des actionnaires non européens, aucun accès de sous-traitants non européens aux données ni à la gestion des identités, des garanties vérifiées face aux demandes d'accès, et une autonomie d'exploitation continue. Le label 2 porte donc sur la résidence; le label 3 y ajoute le contrôle juridictionnel et capitalistique. Ces critères de localisation et de contrôle s'attestent toutefois par simple déclaration, en attendant l'accréditation d'un organisme externe [5].

**L'IDSA** (International Data Spaces Association) fournit l'architecture de référence et les règles de participation. Son Rulebook 2026-1, annoncé le 5 mai 2026, fait de la décentralisation le modèle par défaut, traite la confiance comme une évaluation continue et s'aligne sur ISO/IEC 20151, le Dataspace Protocol (DSP), le Decentralized Claims Protocol (DCP) et Eclipse Dataspace Components [6]. DSP normalise la négociation de contrats entre organisations; DCP permet de prouver le respect d'une politique par des justificatifs vérifiables, sans fournisseur d'identité commun [7]. Chez chaque participant, un connecteur met ces échanges en œuvre et laisse au fournisseur la maîtrise de l'usage de ses données [9] (chapitre 45).

---

## 37.3 Les agents comme participants d'un espace de données

Le Rulebook 2026-1 comporte un chapitre sur les agents d'IA, que le billet d'annonce présente comme un premier jeu d'exigences pour des acteurs autonomes ou semi-autonomes [6]. Le texte ne contient pourtant aucune exigence normative : il décrit des scénarios et formule des recommandations [7].

### Deux scénarios

**L'espace d'abord.** L'organisation de l'agent a déjà négocié des droits. Les données sont transférées chez elle, ce qui est simple mais les laisse vieillir, ou l'agent y accède par un serveur MCP derrière une façade qui fait respecter le contrat.

**L'agent d'abord.** L'agent découvre une offre sans y avoir accès. Il passe par une adhésion humaine, ou négocie lui-même si le fournisseur l'accepte.

### Un partage des rôles entre protocoles

DSP et DCP établissent la confiance entre organisations et aboutissent à un contrat. L'agent en reçoit l'adresse du serveur MCP, un jeton d'accès et les usages permis; MCP gère ensuite l'accès à la ressource (chapitre 5) [7]. Les protocoles des espaces de données donnent le droit d'appeler, les protocoles agentiques portent l'appel.

### La thèse de l'IDSA

Selon le document de position de l'IDSA (version 1.0, 9 juillet 2026), un agent peut participer par un connecteur, sans nouveau protocole [8][10]. Il agit sous une identité déléguée, liée au participant juridiquement responsable : chaque action reste attribuable à une organisation et soumise aux politiques, justificatifs et pistes d'audit d'un participant humain.

Le support proposé est un justificatif vérifiable, le Delegated Agent Participant ID, dont le connecteur vérifie six éléments avant toute transaction : organisation, instance d'agent, modèle, outils permis, finalité, qui doit concorder avec les politiques ODRL du fournisseur, et niveau d'assurance. Un agent qui en mandate un autre lui transmet ces limites. L'application, ajoute le document, doit être déterministe et tenue hors du contexte du modèle [10].

Ce n'est ni un avis juridique ni une spécification complète. Le document admet que ni la déclaration de la délégation ni la délégation en cascade ne sont normalisées [10]. Son groupe de travail range parmi les questions ouvertes l'identité des agents, la responsabilité, les limites de décision et la divergence des règles régionales [8] (chapitres 29, 36 et 45).

### Un premier résultat expérimental

Une prépublication d'octobre 2026 éprouve ce schéma [11] : un système multi-agents bâti sur LangGraph et Eclipse Dataspace Components négocie par DSP à partir de demandes en langage naturel, sous condition des justificatifs vérifiables du consommateur. Avec un petit modèle à poids ouverts hébergé localement (Magistral Small), 600 exécutions donnent 88,7 % de réussite et aucune violation de garde-fou; le taux passe de 98 % pour des requêtes techniques à 72 % pour des requêtes informelles, et les échecs sont surtout des refus. Une seconde série de 600 exécutions bloque au connecteur toutes les requêtes régionales non autorisées.

Les auteurs attribuent la conformité au protocole, qui applique les contraintes indépendamment du raisonnement des agents; le modèle décide seulement si la tâche aboutit. Le banc reste étroit, de leur aveu : un seul modèle, des utilisateurs simulés, des contraintes simples, et un canal d'injection de prompts par le texte des catalogues (chapitre 31).

---

## 37.4 Des espaces de données aux « espaces d'agents »

Un article de position présenté en mai 2026 à l'atelier Semantics in Dataspaces pose la question que l'IDSA effleure : que devient la souveraineté quand le modèle est lui-même un acteur de l'espace ? [9]

Les auteurs décrivent un espace de données qui s'enrichit de graphes de connaissances, d'outils, puis de modèles agentiques agissant pour les participants. Deux obstacles demeurent : la sensibilité des données et la mise à l'échelle de l'accord sémantique (chapitre 12).

Les agents aggravent le premier. Le modèle et son fournisseur deviennent parties prenantes de l'espace; le suivi des usages doit dire quel agent a utilisé quelle donnée, pour qui et dans quel but, et la gouvernance ne vaut que si ce nouvel acteur respecte contrats et politiques. Or les auteurs jugent que des modèles réellement souverains ne sont pas pour demain, tant que l'entraînement, les données et l'inférence restent aux mains de quelques fournisseurs. Un modèle local n'offre pas non plus de garantie complète, puisqu'un agent peut s'écarter du but fixé.

Leur « espace d'agents » (Agent Space), esquisse délibérément conceptuelle, combine des modèles agentiques souverains exploités par chaque participant, des graphes de connaissances liés et des garde-fous symboliques, soit des règles déterministes exprimées dans des vocabulaires comme ODRL. Dans leurs expériences, les petits modèles ouverts restent en retrait des grands sur les données structurées.

Deux enseignements valent dès maintenant : l'application des politiques doit se faire hors du modèle, et le fournisseur du modèle doit figurer dans l'analyse de souveraineté comme tout autre sous-traitant.

---

## 37.5 Options d'architecture

Cinq options se combinent plus qu'elles ne s'excluent.

| Option | Ce qu'elle règle | Ce qu'elle laisse ouvert |
|---|---|---|
| Région locale d'un fournisseur mondial | Résidence | Juridiction du fournisseur [1] |
| Même région, clés détenues par le client | Accès aux données au repos [3] | Données en clair pendant l'inférence, sauf environnement d'exécution de confiance (chapitre 46) |
| Fournisseur sous contrôle local, de type Label 3 | Résidence et contrôle juridictionnel [5] | Chaîne d'approvisionnement; offre de modèles |
| Modèle à poids ouverts autohébergé | Le modèle sort de la liste des tiers | Capacité parfois moindre [9]; exploitation |
| Espace de données avec connecteur | Partage entre organisations sous contrat [7] | Délégation et responsabilité de l'agent [8][10] |

La démarche part des données, non de la plateforme. Chaque classe de données reçoit un niveau d'exigence, et chaque composant de l'agent est rattaché à un exploitant et à une juridiction. Le routage vers le bon modèle se fait à la passerelle, selon la classe de la requête (chapitres 24 et 44). Un modèle hébergé à l'étranger sert alors les tâches sans données sensibles, un modèle local le reste (chapitre 28).

Le plan de contrôle et les journaux font partie du périmètre : une inférence locale dont les traces partent à l'étranger n'est pas souveraine (chapitre 33). La souveraineté se négocie aussi par contrat, avec l'avis au client en cas de demande d'une autorité, la réversibilité et les clauses de sortie (chapitre 27).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Critère de souveraineté | Contrôle juridictionnel, en plus de la résidence | Données non sensibles : la résidence suffit |
| Périmètre de l'analyse | Inférence, orchestration, mémoire, outils et traces | — |
| Hébergement du modèle | Selon la classe de données, avec routage à la passerelle | Une seule classe de données |
| Données réglementées ou stratégiques | Fournisseur sous contrôle local ou modèle autohébergé | Clés du client, si la donnée n'atteint pas l'inférence |
| Évaluation d'un fournisseur | Grille par objectifs, de type Cloud Sovereignty Framework | Hors UE : adapter les seuils |
| Partage entre organisations | Espace de données, agent derrière un connecteur et sous identité déléguée | Échange bilatéral ponctuel |
| Application des politiques d'usage | Hors du modèle : connecteur, passerelle, règles déterministes | — |
| Preuve de souveraineté d'un fournisseur européen | Qualification nationale existante, comme SecNumCloud | Niveau d'assurance de l'Union, si le règlement proposé est adopté |

---

## Points à retenir

- Résidence et contrôle juridictionnel sont deux questions. Une région locale chez un fournisseur étranger ne répond qu'à la première, et les droits américain et européen lui imposent des obligations contraires.
- Un agent se répartit sur plusieurs exploitants. L'analyse de souveraineté se fait par composant, traces comprises.
- Le Cloud Sovereignty Framework et le label Gaia-X de niveau 3 sont des grilles européennes; leur structure se réutilise, pas leurs seuils. Les critères de contrôle du label 3 s'attestent encore par déclaration.
- Un agent peut participer à un espace de données par un connecteur, sous une identité déléguée, sans nouveau protocole. DSP et DCP donnent le droit d'accès, MCP porte l'appel.
- L'IDSA propose un justificatif d'agent délégué, vérifié par le connecteur; la délégation en cascade reste à normaliser, la responsabilité et les limites de décision à trancher.
- Le modèle et son fournisseur sont des parties prenantes; les modèles réellement souverains restent un objectif de recherche.
- Les politiques d'usage s'appliquent hors du modèle, au connecteur. L'IDSA le pose, et le seul résultat expérimental cité, sur un banc étroit, va dans ce sens.
- La certification de la souveraineté reste nationale : SecNumCloud en France, le schéma européen EUCS n'étant pas adopté. La Commission propose depuis juin 2026 quatre niveaux d'assurance de l'Union, dans un texte qui nomme l'orchestration d'agents.

---

## Sources

Pages lues les 11 et 12 novembre 2026 :

1. [18 U.S.C. § 2713 — Legal Information Institute](https://www.law.cornell.edu/uscode/text/18/2713)
2. [Règlement (UE) 2023/2854 (Data Act), articles 32 et 50](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202302854)
3. [Commission européenne — Cloud Sovereignty Framework 1.2.1](https://commission.europa.eu/document/download/09579818-64a6-4dd5-9577-446ab6219113_en)
4. [Gaia-X Compliance Document 25.10 — introduction](https://docs.gaia-x.eu/policy-rules-committee/compliance-document/25.10/Introduction_and_scope/)
5. [Gaia-X Compliance Document 25.10 — critères](https://docs.gaia-x.eu/policy-rules-committee/compliance-document/25.10/criteria_cloud_services/)
6. [IDSA — annonce du Rulebook 2026-1](https://internationaldataspaces.org/idsa-rulebook-2026-1-structural-clarifications-for-operational-data-spaces/)
7. [IDSA Rulebook — chapitre sur les agents d'IA](https://kb.internationaldataspaces.org/external/rulebook/130_AI_Agents/)
8. [IDSA — Task Force Data Spaces and AI](https://github.com/International-Data-Spaces-Association/Task-Force-Data-Spaces-and-AI)
9. [Polleres et coll. — From Data Spaces to Agent Spaces (SDS 2026)](https://aic.ai.wu.ac.at/~polleres/publications/poll-etal-2026SDS_ESWC_Agent_Spaces.pdf)
10. [IDSA — Data Spaces and AI: Trustworthy Agentic Participation in Data Spaces (v1.0)](https://doi.org/10.5281/zenodo.21279055)
11. [Grunewald et coll. — Agentic Orchestration of EDC Data Space Retrieval (arXiv 2610.26548)](https://arxiv.org/abs/2610.26548)

Sources ajoutées le 14 novembre 2026 :

12. [Commission européenne — proposition de règlement « Cloud and AI Development Act », COM(2026) 502 final, 3 juin 2026 (document du Conseil 10104/26)](https://data.consilium.europa.eu/doc/document/ST-10104-2026-INIT/en/pdf) — texte officiel, lu par passages.
13. [Bômont — Technical is political: When a cloud certification scheme divides Europe, Institut d'études de sécurité de l'Union européenne, 3 novembre 2025](https://iss.europa.eu/publications/briefs/technical-political-when-cloud-certification-scheme-divides-europe)
14. [Landot — billet du 17 août 2026 sur l'arrêté du 12 août 2026 approuvant le référentiel SecNumCloud](https://blog.landot-avocats.net/2026/08/17/important-notamment-pour-certains-marches-publics-evolution-du-referentiel-dexigences-relatif-aux-prestataires-de-services-dinformatique-en-nuage/) — commentaire de cabinet, secondaire.
15. [CMS Francis Lefebvre — SecNumCloud : un référentiel technico-juridique désirable, bientôt incontournable ? (24 octobre 2022)](https://cms.law/fr/fra/news-information/secnumcloud-un-referentiel-technico-juridique-desirable-bientot-incontournable) — commentaire de cabinet, secondaire.

## Limites de ce chapitre

- [3] et [9] ont été lus en texte intégral; les autres pages, par un outil qui en restitue le contenu, sans contrôle mot à mot. L'audit du 12 novembre a relu [5] à [8] et lu [11] en entier, ce qui en confirme les chiffres; [1], [2] et [4] n'ont pas été relues.
- De [10], seuls la synthèse, le modèle d'identité et les perspectives ont été lus; les projets pilotes ne sont pas traités.
- Aucune donnée d'adoption n'est citée (Gaia-X Magazine de juin 2026 non chargé).
- Viennent de la connaissance générale : le rattachement de l'article 2713 au CLOUD Act et les réserves sur l'offre de modèles des fournisseurs locaux. L'état en clair des données pendant l'inférence est appuyé au chapitre 46.
- Le régime des données personnelles n'est pas traité, faute de source lue. SecNumCloud, EUCS et la proposition de Cloud and AI Development Act le sont depuis le 14 novembre 2026 (37.1), avec trois réserves. Le référentiel SecNumCloud n'a pas pu être chargé (erreur 404) et n'est connu que par deux commentaires de cabinets [14][15], dont l'un date de 2022. L'état d'EUCS repose sur une note de novembre 2025 [13] et sur l'exposé des motifs de [12]. Enfin, [12] a été lu par recherche de passages dans ses 130 pages, sans lecture de son annexe II, qui définit les niveaux; l'avancement de la proposition après juin 2026 n'a pas été vérifié.
- La décomposition d'un agent en composants (introduction, 37.5) est une grille proposée ici, sans source; le chapitre 46 la prolonge par état de l'agent.
