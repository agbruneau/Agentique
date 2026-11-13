# Chapitre 28 — Agents industriels et périphérie

*Question directrice : les mêmes protocoles valent-ils en usine ?*

> **Version 2 — 11 novembre 2026.** État de référence : prépublication IndustriConnect (25 mars 2026), brochure visIT de Fraunhofer IOSB (avril 2026), communiqué de l'OPC Foundation (20 avril 2026) et serveur MCP de l'OPC Foundation en version 2.0.2 (11 novembre 2026). Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [10] et [13] sont des pages primaires lues, [11] et [12] sont secondaires. Les renvois « chapitre N » pointent vers les autres chapitres du compendium. Chapitre audité et révisé le 12 novembre 2026.

Dans un système de gestion, un agent qui se trompe produit un mauvais enregistrement, que l'on corrige. Dans un atelier, il ouvre une vanne. La différence ne tient pas au protocole, mais à ce qui se trouve au bout de l'appel d'outil : un procédé physique, soumis à des exigences de sûreté et de continuité que l'informatique de gestion ne connaît pas.

La thèse tient en trois propositions. Les mêmes protocoles valent en usine s'ils restent à leur place : MCP s'y installe comme une couche d'accès au-dessus des standards industriels, qu'il ne remplace pas. Le sens des données vient d'OPC UA et de l'Asset Administration Shell, normalisés bien avant les agents. Enfin, ce que MCP formule en recommandations devient ici une obligation de conception, alors que la base de preuve reste mince : des prototypes, des démonstrateurs et des annonces.

---

## 28.1 Particularités des environnements opérationnels

### Trois conséquences pour un agent

Le NIST définit les technologies opérationnelles comme des systèmes programmables qui interagissent avec l'environnement physique, et fonde son guide de sécurité sur leurs exigences propres de performance, de fiabilité et de sûreté [9].

**Une commande n'est pas une transaction.** Selon la documentation du serveur MCP de l'OPC Foundation, une commande est une demande adressée au serveur; son acceptation ne prouve pas l'exécution physique. Un délai expiré ne prouve pas qu'une écriture n'a pas eu lieu : il faut relire l'état avant de décider d'un nouvel essai. Un refus n'en justifie aucun, et le serveur ne réessaie jamais implicitement une commande [4]. Or la révision du 28 juillet 2026 de MCP prévoit qu'une requête interrompue soit réémise (chapitre 5). Ce comportement, sain pour une lecture, est dangereux pour une consigne : la compensation suppose un effet annulable, et le chapitre 18 range la commande à un équipement parmi les points de non-retour (18.7).

**Le parc est hétérogène.** Les équipements parlent Modbus, MQTT avec Sparkplug B ou OPC UA [5], et chaque fabricant d'automates a son dialecte du langage Structured Text de la norme IEC 61131-3 [6]. Le problème se rapproche de celui des systèmes patrimoniaux (chapitre 25).

**Le temps de réponse n'est pas celui du modèle.** Sur simulateur local, le surcoût médian d'un adaptateur MCP va de 1,4 ms (Modbus) à 7,3 ms (OPC UA), réseau et inférence exclus [5]. Aucune des sources lues ne place un modèle de langage dans une boucle de régulation; toutes le situent au-dessus, dans l'analyse et l'assistance.

### Ce que « périphérie » veut dire ici

Trois architectures tracent le même partage. Le projet Teuken4OPC de Fraunhofer exécute en atelier les fonctions critiques en latence et en sécurité, et place au centre de données les composants gourmands en calcul : modèles de langage, bases de connaissances, surveillance [6]. GridCompanion, assistant pour salles de conduite de réseaux électriques, s'appuie sur un modèle hébergé localement [6]. L'assistant d'ingénierie de Beckhoff admet des modèles hébergés sur place, pour un fonctionnement isolé du réseau [10].

La périphérie désigne donc deux choses : l'adaptateur, qui doit se trouver près de l'équipement, et le modèle, qui peut s'en éloigner tant que le site accepte une dépendance réseau. Le modèle local touche aussi à la souveraineté (chapitre 37), à la distillation (chapitre 47) et au fonctionnement déconnecté (chapitre 46).

---

## 28.2 OPC UA et Asset Administration Shell comme couche sémantique

Fraunhofer formule l'exigence : des données ouvertes et bien décrites ne suffisent pas; il faut des API normalisées, des modèles de données cohérents et une sémantique inscrite dans le modèle lui-même [6]. L'industrie dispose de deux standards qui y répondent.

| | OPC UA | Asset Administration Shell (AAS) |
|---|---|---|
| Objet | Données et commandes d'un équipement en marche | Jumeau numérique d'un actif |
| Ce que le modèle porte | Structures, méthodes, états, attributs, relations [1] | Métamodèle des actifs, interfaces uniformes, sémantique partagée [6] |
| Extension par domaine | Plus de 430 Companion Specifications [2] | Sous-modèles et descriptions de concepts [8] |
| Interface | Lecture, écriture, navigation, abonnement, appel de méthode [3] | API de dépôts, de registres et de découverte (IDTA, partie 2) [8] |

### OPC UA : un modèle d'information, pas seulement un transport

OPC UA (IEC 62541) transporte des valeurs, mais surtout il les type et les relie. Un article commandité, publié par l'OPC Foundation, en fait son argument central : la donnée arrive structurée et porteuse de sens, ce qui réduit le travail d'interprétation laissé au modèle de langage [1].

L'OPC Foundation en a tiré deux chantiers [2]. Le premier, livré en prototype (UA-for-AI), transforme les spécifications de base en fichiers Markdown, en fragments pour la recherche augmentée et en interfaces MCP et REST. Le second, annoncé sans calendrier, étend cette conversion à toutes les Companion Specifications. Holger Kenn, qui dirige le groupe de travail sur l'IA, pose un principe à retenir : un système agentique doit être au moins aussi fiable et exact que les méthodes d'ingénierie existantes.

### L'AAS : décrire l'actif plutôt que le signal

Un agent peut consulter l'AAS : dans un démonstrateur de Fraunhofer, un assistant y lit des géométries 3D et des métadonnées pour proposer un plan d'emballage [6]. Il peut aussi la construire : l'outil FA³ST CreAitor extrait l'information de fiches techniques, puis la relie à des ontologies de domaine. L'utilisateur y révise l'information extraite, car le modèle de langage ignore les conventions propres à l'entreprise [6].

Le chapitre 12 traite la couche sémantique d'entreprise. Le point propre à l'usine est que cette couche existe déjà sous une forme normalisée : un agent industriel devrait s'y brancher plutôt que la reconstituer.

---

## 28.3 Adaptateurs MCP industriels

### Un patron commun

Les mises en œuvre lues suivent le même patron : un serveur MCP par protocole industriel, qui traduit des appels d'outils en opérations natives sans modifier les systèmes de commande [5][6]. Dans Teuken4OPC, les outils sont fournis une fois, au lieu de relier chaque machine à un modèle [6]. C'est, à l'échelle de l'atelier, le passage du produit à la somme décrit au chapitre 5.

| Adaptateur | Ce qu'il expose | Écritures | État |
|---|---|---|---|
| IndustriConnect, prépublication [5] | Modbus (17 outils), MQTT/Sparkplug B (15), OPC UA (7) | Régies par des drapeaux de configuration | Évalué sur simulateurs |
| Serveur MCP de l'OPC Foundation [3][4] | Services OPC UA, profils par domaine (robotique, machines-outils, pompes) | Capacités privilégiées désactivées par défaut | Version 2.0.2 |
| `aas-mcp-server` de SAP, code ouvert [8] | API AAS, à partir de leur description OpenAPI | Lecture seule par défaut | Statut non déclaré |
| Teuken4OPC, Fraunhofer [6] | Outils OPC UA et AAS | Lecture seule ou commande simple, selon le scénario | Trois démonstrateurs |
| Adaptateur OPC UA × MCP, Takebishi [1] | Données d'un serveur OPC multi-fabricants | Non précisé | Annoncé |
| TwinCAT CoAgent, Beckhoff [10] | Client MCP relié à des serveurs pour l'automate, les E/S et l'IHM | Approuvées par l'ingénieur | Ingénierie; exploitation à venir |

### Ce que mesure le seul banc d'essai publié

IndustriConnect est la seule évaluation chiffrée trouvée [5]. Le banc d'essai compte 870 exécutions et 2 820 appels d'outils. En conditions normales, toutes les tâches réussissent. Les sept scénarios de panne produisent une erreur structurée; une valeur hors de la plage d'un registre de 16 bits est rejetée avant d'atteindre l'équipement. La reprise après redémarrage fonctionne pour les trois protocoles. Sous charge, un scénario échoue entièrement : des appels MQTT émis dans la seconde qui suit un redémarrage, échec attribué au délai de reconnexion de la bibliothèque cliente; avec trois secondes, la reprise réussit.

Ce résultat porte sur l'adaptateur, pas sur l'agent : ni modèle de langage ni équipement réel ne figurent dans la boucle, et les appels de méthode OPC UA, c'est-à-dire les commandes, sont exclus de la mesure.

### Deux sauts, deux sécurités

Un adaptateur crée deux liaisons indépendantes : du client MCP vers l'adaptateur, puis de l'adaptateur vers l'équipement [4]. La sécurité OPC UA (certificats, chiffrement du jeton d'utilisateur) protège la seconde, pas la première. Une connexion MCP distante doit être protégée séparément par HTTPS authentifié, et l'acceptation automatique des certificats est réservée aux essais. Les arguments d'un outil pouvant rester dans l'historique de conversation, les traces ou le stockage d'audit du client, un jeton de production ne doit jamais y figurer.

Le serveur s'exécute en stdio ou en Streamable HTTP [3]. L'identité de l'agent face à l'équipement relève des chapitres 29 et 30.

### Ingénierie et exploitation

Les annonces de fabricants portent d'abord sur l'ingénierie : programmation d'automates, configuration des entrées-sorties, documentation [10]. L'agent branché sur une machine en marche reste le fait de projets de recherche et d'adaptateurs à code ouvert.

**⚠ Fabricants d'automates.** Un communiqué de Beckhoff décrit une architecture MCP pour son environnement d'ingénierie [10], sans documentation technique des outils. Un serveur MCP intégré à CODESYS est rapporté par un résultat de recherche, page non lue [11]. Rien d'officiel n'a été trouvé pour Siemens, Rockwell Automation ou Schneider Electric; les serveurs repérés pour leurs produits sont communautaires [12]. L'avertissement tient pour l'exploitation.

---

## 28.4 Garde-fous : lecture seule par défaut, supervision humaine obligatoire

MCP recommande, sans l'imposer, qu'un humain puisse refuser une invocation, et tient les annotations d'un outil pour non fiables (chapitre 5). En usine, ces garde-fous doivent être rendues effectives par l'adaptateur et par l'équipement, pas par l'hôte seul.

### Lecture seule par défaut

Les mises en œuvre les plus soignées inscrivent ce défaut dans le code. Le serveur AAS de SAP n'expose que des lectures tant qu'une option explicite n'active pas les écritures, et une liste d'autorisation détermine les opérations visibles [8]. Le serveur de l'OPC Foundation sépare deux notions : un profil choisit un catalogue d'outils, mais ce choix, selon sa documentation, « is not an execution grant » [4]. Écrire une valeur ou appeler une méthode exige une capacité activée par l'hôte, une autorisation accordée à l'appelant précis, des règles réseau et, en HTTP, une identité authentifiée.

À l'inverse, le prototype IndustriConnect n'a ni authentification, ni contrôle d'accès par rôle, ni journal d'audit; ses auteurs les rangent parmi les préalables à la production, avec une approbation humaine des écritures critiques pour la sûreté [5]. Un adaptateur n'est pas sûr du seul fait qu'il parle MCP.

Le démonstrateur le plus instructif est la presse à injecter de Teuken4OPC : l'assistant, en lecture seule, explique les relations entre paramètres et qualité des pièces et signale des pistes d'optimisation sans régler la machine [6]. La valeur vient de l'explication, pas de la commande.

### Supervision humaine

GridCompanion fixe le modèle le plus net [6]. L'agent n'effectue aucune manœuvre, ne modifie aucune consigne et ne déclenche aucune action automatique; toute décision finale revient à l'opérateur. Il orchestre des outils de calcul déterministes, et chaque recommandation renvoie aux calculs et aux documents qui la fondent. La chaîne complète (appels d'outils, paramètres, résultats intermédiaires) s'inspecte pas à pas. C'est le partage du chapitre 17 : le modèle raisonne, des outils déterministes calculent, l'humain décide.

En ingénierie, Beckhoff pose la même règle : l'ingénieur approuve chaque résultat avant son application [10]. Dans le profil machines-outils du serveur de l'OPC Foundation, les outils de mutation exigent une confirmation explicite [4]. L'approbation liée aux paramètres exacts est développée aux chapitres 7 (7.4) et 22.

### La sûreté reste hors de portée

La documentation de l'OPC Foundation trace la frontière : ses outils de robotique ne changent pas le mode de fonctionnement, ne lèvent pas un arrêt et ne contournent pas le système de sûreté du robot [4]. Un agent n'entre pas dans la chaîne de sûreté; il reste soumis aux mêmes verrouillages que tout autre utilisateur. Le chapitre 46 (46.7) situe cette frontière quand un contrôleur appris entre dans la commande.

Le qualificatif « obligatoire » du titre est une recommandation de ce chapitre, tirée de la convergence de ces pratiques. Aucune norme lue ne l'impose en ces termes.

---

## 28.5 Maturité : des prototypes

1. **La seule évaluation chiffrée est simulée.** Ses auteurs la disent limitée aux simulateurs, sans modèle de langage dans la boucle, sans évaluation de sécurité ni référence humaine. Ils nomment la suite : matériel réel, contrôle d'accès, plusieurs modèles, opérateur dans la boucle [5].
2. **Les démonstrateurs sont de laboratoire.** Teuken4OPC a réalisé trois scénarios; GridCompanion en est à ses premiers essais pratiques [6].
3. **Le même institut tient deux discours.** Sa brochure situe l'IA agentique industrielle entre prototypes et premiers déploiements, et nomme comme défis l'intégration, la validation en milieu critique pour la sûreté et la robustesse en conditions réelles [6]. Sa page commerciale présente ces technologies comme prêtes pour la production [7]. Le premier énoncé est le seul étayé.
4. **L'organisme de normalisation avance sans calendrier.** Son serveur MCP a atteint la version 2.0.0 le 7 octobre 2026 et totalisait environ 1 100 téléchargements le 12 novembre [3]; la conversion des Companion Specifications reste une intention [2].
5. **Les offres commerciales sont annoncées ou cantonnées à l'ingénierie** [1][10].

La réponse à la question directrice est donc nuancée. Les mêmes protocoles valent en usine pour lire, expliquer et proposer. Pour agir, ils valent sous des contraintes que le protocole ne porte pas. Entre agents (chapitre 6), aucune source lue ne décrit d'usage en atelier; seul un projet de norme, l'IEEE P3945.1 autorisé le 12 février 2026, vise un profil d'interopérabilité agent-à-agent industriel [13] (chapitre 11). Le sujet reste celui de l'agent et de ses outils.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Rôle de l'agent en exploitation | Aide à la décision : lire, expliquer, proposer | Commande simple sur installation d'essai, confirmée par l'opérateur |
| Accès aux équipements | Adaptateur MCP au-dessus d'OPC UA, sans modifier les automates | Équipement sans OPC UA : adaptateur propre au protocole |
| Écritures | Désactivées par défaut; activées par outil et par appelant | — |
| Fonctions de sûreté | Hors de portée de tout agent | Aucun cas |
| Validation humaine | Obligatoire avant toute écriture | Aucun cas en exploitation |
| Échec ou délai sur une écriture | Pas de nouvel essai automatique; relire l'état | Écriture démontrée idempotente |
| Couche sémantique | OPC UA pour le procédé; AAS pour la description des actifs | Parc sans modèle : modéliser d'abord |
| Emplacement | Adaptateur en atelier; modèle au centre de données | Site isolé ou données sensibles : modèle local |
| Provenance de l'adaptateur | Organisme de normalisation ou éditeur, version épinglée | Adaptateur communautaire : banc d'essai seulement |

---

## Points à retenir

- MCP ne remplace aucun protocole industriel. Il enveloppe OPC UA, Modbus ou MQTT dans un adaptateur, sans toucher aux systèmes de commande.
- La couche sémantique existe déjà : le modèle d'information OPC UA pour l'équipement en marche, l'AAS pour la description de l'actif.
- Une commande acceptée n'est pas une action exécutée. La réémission automatique que tolère une lecture est à proscrire pour une écriture.
- Les adaptateurs sérieux désactivent les écritures par défaut et séparent le choix d'un catalogue d'outils de l'autorisation de s'en servir.
- La sécurité se joue sur deux sauts indépendants : du client vers l'adaptateur, de l'adaptateur vers l'équipement.
- En exploitation, le modèle de référence est l'aide à la décision : l'agent orchestre des outils déterministes, l'opérateur décide, la sûreté reste hors de portée.
- La preuve est mince : aucune évaluation lue ne place un modèle de langage devant un équipement réel, et l'offre des fabricants d'automates porte sur l'ingénierie.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [OPC Connect, juin 2026 — OPC UA et agents IA (article commandité par Takebishi)](https://opcconnect.opcfoundation.org/2026/06/toward-realizing-ai-utilization-in-manufacturing-exploring-the-potential-of-integrating-the-opc-ua-information-model-with-ai-agents/)
2. [OPC Foundation — communiqué du 20 avril 2026](https://opcfoundation.org/news/press-releases/opc-foundation-advances-opc-ua-for-the-ai-era-with-companion-specifications-optimized-for-agentic-ai/)
3. [NuGet — OPCFoundation.NetStandard.Opc.Ua.Mcp](https://www.nuget.org/packages/OPCFoundation.NetStandard.Opc.Ua.Mcp)
4. [OPC Foundation — documentation du serveur MCP](https://raw.githubusercontent.com/OPCFoundation/UA-.NETStandard/master/docs/McpServer.md)
5. [IndustriConnect (arXiv 2603.24703)](https://arxiv.org/abs/2603.24703) — prépublication, résumé et texte lus.
6. [Fraunhofer IOSB — visIT, « Agentic Industrial AI », avril 2026](https://www.iosb.fraunhofer.de/content/dam/iosb/iosbtest/documents/publikationen/visit/Fraunhofer_visIT_Agentic-Industrial-Ai_web.pdf)
7. [Fraunhofer IOSB — Agent-Based Systems for Industrial Applications](https://www.iosb.fraunhofer.de/en/projects-and-products/agent-based-systems.html)
8. [SAP — aas-mcp-server](https://github.com/SAP/aas-mcp-server)
9. [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — page de présentation seulement.
10. [Beckhoff — communiqué du 23 juin 2026 sur TwinCAT CoAgent](https://www.beckhoff.com/en-us/company/press/open-model-independent-ai-assistance-for-automation-programming-and-controls-engineering-2026-06.html)

Sources secondaires, résumés de recherche seulement, pages non lues :

11. [CODESYS — AI-supported Engineering](https://www.codesys.com/products/engineering/ai-supported-engineering/)
12. [mcpservers.org — serveur communautaire pour TIA Portal](https://mcpservers.org/servers/a4webdev/tiacommander-mcp)

Page primaire lue pendant l'audit, le 12 novembre 2026 :

13. [IEEE — projet P3945.1](https://standards.ieee.org/ieee/3945.1/12437)

## Limites de ce chapitre

- Seule la brochure [6] a été lue en texte intégral. Les autres pages l'ont été par un outil qui en restitue un résumé. L'audit a relu ainsi [2] à [5], [8] et [10], qui confirment profils, versions, téléchargements et chiffres du banc d'essai; [1], [6], [7] et [9] n'ont pas été relus.
- Les normes n'ont pas été lues : IEC 62541, spécifications de l'IDTA sur l'AAS, IEC 61131-3, IEC 62443, normes de sûreté fonctionnelle. Du guide du NIST, seule la page de présentation l'a été.
- Le caractère physique et parfois irréversible d'une commande relève du raisonnement et de la connaissance générale; les sources lues l'illustrent sans le démontrer.
- L'état de l'offre des fabricants d'automates repose sur un communiqué [10] et des résultats de recherche [11][12]. Une annonce d'agent d'ingénierie par Siemens en juillet 2026, signalée par un résultat de recherche, n'a pas été vérifiée et n'est pas reprise.
- Aucun déploiement en production n'est documenté par une source lue; cela n'établit pas qu'il n'en existe pas.
- Du projet IEEE P3945.1, seule la fiche d'autorisation a été lue; son rapport au protocole A2A, que la fiche cite, reste inconnu.
