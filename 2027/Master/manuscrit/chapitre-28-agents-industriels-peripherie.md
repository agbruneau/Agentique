# Chapitre 28 — Agents industriels et périphérie

*Question directrice : les mêmes protocoles valent-ils en usine ?*

> **État de référence :** prépublication IndustriConnect (25 mars 2026), brochure visIT de Fraunhofer IOSB (avril 2026), communiqué de l'OPC Foundation (20 avril 2026) et serveur MCP de l'OPC Foundation en version 2.0.2 (11 novembre 2026). Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [10] et [13] sont des pages primaires lues, [11] et [12] sont secondaires.

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
| Interface | Lecture, écriture, navigation, abonnement, appel de méthode [3] | API de dépôts, de registres et de découverte (Industrial Digital Twin Association, IDTA, partie 2) [8] |

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

MCP recommande, sans l'imposer, qu'un humain puisse refuser une invocation, et tient les annotations d'un outil pour non fiables (chapitre 5). En usine, ces garde-fous doivent être rendus effectifs par l'adaptateur et par l'équipement, pas par l'hôte seul.

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

## Mise en œuvre — Orchestration cyber-physique : convergence IT/OT, OPC UA et jumeaux numériques {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : relier la fabrique agentique aux usines, aux réseaux énergétiques ou aux sites miniers apporte des gains : maintenance prédictive couplée aux stocks ERP, rééquilibrage dynamique de lignes, sobriété énergétique. Une proposition erronée transmise à une machine-outil peut détruire un actif coûteux, arrêter la production ou mettre en danger les opérateurs.
- **Décisions architecturales structurantes** :
  1. *Irréversible* : asymétrie entre lecture et écriture IT/OT. Aucun modèle de langage, grand ou petit, n’a d’accès direct en écriture à un automate programmable, à une commande numérique (CNC) ou à un système instrumenté de sécurité (SIS).
  2. *Structurante dès le jour 1* : respecter la segmentation en zones et conduits de l’IEC 62443 (modèle Purdue, zone démilitarisée industrielle IDMZ au niveau 3.5), en exposant OPC UA et MQTT Sparkplug B par des réplicas en lecture seule qui protègent les bus de terrain.
  3. *Sas obligatoire d’action corrective* (recommandation du chapitre, section 28.4) : toute modification proposée par un agent traverse un jumeau numérique déterministe, qui valide les contraintes physiques et signe cryptographiquement un certificat éphémère avant la traduction en recette homologuée (ISA-88, ISA-95) pour le MES ou le SCADA.
- **Indicateurs de gouvernance associés** : zéro paquet IP direct de l’IT vers les niveaux 1 et 0; taux d’interception préventive des propositions hors enveloppe par le jumeau numérique; fraîcheur garantie de l’état du capteur à l’application ($\Delta t \le 5\,\text{s}$); gain de taux de rendement synthétique (OEE).
::::

## 28.6 Contraintes temps réel, sûreté fonctionnelle et segmentation réseau (modèle Purdue / IEC 62443)

Les exigences propres aux technologies opérationnelles (OT) sont posées à la section 28.1. Elles inversent la triade de sécurité et les constantes de temps de l’informatique de gestion (IT), où la confidentialité prime et où une latence variable de deux secondes est bénigne. En OT, la sûreté des personnes et la disponibilité déterministe priment : une boucle d’asservissement sur automate s’exécute à cycle fixe, entre 0,5 et 10 millisecondes, et des requêtes réseau non bornées qui la perturbent suffisent à provoquer un arrêt de sécurité de la ligne.

Un agent dont l’inférence dure plusieurs secondes et reste probabiliste doit donc être découplé du procédé, dans l’espace et dans le temps, selon le modèle Purdue (ISA-95) et la norme IEC 62443.

![Architecture de convergence IT/OT conforme IEC 62443 (modèle Purdue) : télémétrie OPC UA / MQTT Sparkplug en lecture seule et sas obligatoire par Jumeau numérique déterministe.](figures/fig-28-a-1.svg)

### Règles d’urbanisation par niveau Purdue et conduits IEC 62443

La norme IEC 62443-3-2 divise l’usine en zones, chacune dotée d’un niveau de sécurité cible (SL-1 à SL-4), reliées par des conduits filtrés. L’invariant : aucune session réseau initiée dans le nuage ou dans le réseau IT (niveaux 4 et 5) ne franchit directement le réseau d’usine (niveau 3 et inférieurs). Toute communication subit une rupture de protocole dans l’IDMZ (niveau 3.5).

| Niveau Purdue et zone IEC 62443 | Constante de temps | Cible SL-T | Prérogatives autorisées aux composants agentiques | Interdictions d’architecture |
|:----------------------|:-----------|:--------|:-----------------------------|:----------------------------|
| Niveaux 4 et 5 — entreprise IT (ERP, fabrique agentique, nuage) | Secondes à heures | SL-2 / SL-3 | Sagas logistiques, corrélation carnets SAP / alertes OT, planification prédictive | Aucun routage IP direct vers l’atelier; aucune clé privée de signature OT dans le nuage |
| Niveau 3.5 — zone démilitarisée industrielle (IDMZ) | 100 ms à secondes | SL-3 strict | Hébergement du serveur MCP OT en lecture seule (sur miroir OPC UA/MQTT) et sas d’inspection des demandes | Aucun relais d’explorations Browse non bornées vers les automates de terrain |
| Niveau 3 — opérations du site (MES, historien, jumeau numérique) | 100 ms à minutes | SL-3 | Exécution du jumeau numérique déterministe (FMI 3.0); réception par le MES de recettes signées Ed25519 | Aucune mutation d’ordre de fabrication sans certificat valide du jumeau et contrôle d’échéance |
| Niveau 2 — supervision de cellule (SCADA, IHM) | 50 ms à 1 s | SL-3 | Restitution diagnostique à l’opérateur (A2UI); acquittement local HOTL / HITL | Aucun contournement des barrières d’occupation ni du mode « Manuel / Maintenance » |
| Niveau 1 — contrôle temps réel (PLC, CNC, RTU) | 0,5 à 10 ms (dur) | SL-3 / SL-4 | Aucun agent à modèle de langage. Réception exclusive de recettes homologuées, chargées par MES/SCADA entre deux cycles | Aucune écriture directe d’un registre d’automate par un outil MCP ou par un agent |
| Zone isolée — SIS (IEC 61511 SIL 2/3) | `< 5 ms` matériel | SL-4 isolé | Lecture unidirectionnelle après événement (diode matérielle) pour l’analyse de cause racine | Isolation physique et logique totale : aucun canal entrant pouvant altérer un seuil d’arrêt d’urgence |

### Conception de l’IDMZ (niveau 3.5) : diodes logiques, courtiers miroirs et identités SPIFFE

Pour atteindre le niveau SL-3 de l’IEC 62443-3-3, l’IDMZ ne se limite pas à un sous-réseau traversé par des règles NAT : elle termine les sessions TCP et applicatives dans les deux sens.

- **Sens montant (OT vers IT).** La connexion est initiée exclusivement depuis le niveau 3, ou transite par une passerelle unidirectionnelle à isolation optique pour les sites classés critiques, vers un courtier réplica MQTT Sparkplug B et un serveur d’agrégation OPC UA situés dans l’IDMZ. Le pare-feu interne entre l’IDMZ et le niveau 3 peut donc bloquer 100 % des paquets SYN entrants vers l’atelier sur la voie de télémétrie. Le serveur MCP interrogé par les agents de diagnostic du niveau 4 ne voit que cette copie, synchronisée à la milliseconde près. Même si un agent dans le nuage est compromis, ou si 5 000 appels MCP simultanés surviennent par accident, seul le réplica en supporte la charge; les automates du niveau 1 ne sont pas touchés.
- **Sens descendant (IT vers OT).** Le conduit inverse n’expose qu’un point de terminaison HTTPS, authentifié mutuellement par des certificats courts SPIFFE (mTLS). Un validateur matériel de schéma JSON rejette tout paquet de plus de 16 Ko ou contenant des champs non déclarés, avant que l’intention parvienne au sas du jumeau numérique du niveau 3.

---

## 28.7 Exploration sémantique et diagnostic autonome sur OPC UA, MQTT Sparkplug et historiens

Deux standards industriels lèvent l’ambiguïté d’un registre brut tel que `HR40012 = 18432` pour les agents de diagnostic (L1) :

1. **OPC UA (IEC 62541) et ses Companion Specifications** (OPC 40001 Machinery, OPC 40501 Machine Tools, PackML). Le modèle d’information est décrit à la section 28.2. Le canal chiffré est obligatoire : `SecurityPolicy` `Aes128_Sha256_RsaOaep` ou Basic256Sha256 en mode `SignAndEncrypt`, profil None rejeté sans exception. Le serveur expose un graphe d’objets typé (*AddressSpace*) où chaque variable porte ses unités d’ingénierie UNECE (`EngineeringUnits`, par exemple °C, `mm/s`, kW), sa plage nominale (EURange), son horodatage source (`SourceTimestamp`) et son code de qualité (`StatusCode` : Good, Uncertain, `Bad_SensorFailure`).
2. **MQTT Sparkplug B et l’*Unified Namespace* (UNS).** Pour des milliers de capteurs, Sparkplug B impose une arborescence ISA-95 normalisée, une charge Protobuf typée et des certificats d’état de vie (NBIRTH et NDEATH, liés au testament MQTT *Last Will*). Le courtier miroir de l’IDMZ est alimenté en *Report-by-Exception*, sans scrutation des automates. Quand une passerelle du niveau 3 perd sa liaison montante, NDEATH marque aussitôt ses métriques aval comme invalides : aucun agent ne raisonne sur un dernier état figé.

| Source industrielle | Richesse sémantique native | Acquisition vers l’IDMZ | Risque OT en cas d’exposition brute | Patron d’exposition MCP recommandé |
|:---------------|:--------------------|:-------------------|:---------------------|:------------------------|
| Agrégateur OPC UA (Companion Specifications) | Maximale : graphe typé, unités UNECE, EURange, états PackML | Abonnement *MonitoredItems* vers un réplica dans l’IDMZ | Saturation du processeur d’un petit automate en cas de parcours récursif direct | Serveur MCP connecté uniquement au réplica de l’IDMZ, avec certificat X.509 en lecture seule |
| Courtier MQTT Sparkplug B | Élevée : hiérarchie ISA-95, cycle NBIRTH/NDEATH | Pont TLS unidirectionnel sortant du niveau 3 vers l’IDMZ | Très faible (découplage entre publication et abonnement) | Ressources MCP temps réel et déclencheurs sur franchissement de seuil |
| Historien (AVEVA PI / Timescale) | Moyenne à élevée (avec modèle d’actifs) | Réplica de lecture agrégé dans l’IDMZ | Saturation mémoire si extraction brute à 1 kHz sur 30 jours | Outils MCP imposant un calcul statistique côté serveur (rms, kurtosis, centiles) |
| API MES (ISA-95 / B2MML) | Métier manufacturier : ordres, lots, généalogie, OEE | Passerelle HTTPS mTLS dans l’IDMZ | Modéré (système informatique du niveau 3) | Outils MCP de corrélation de production et guichet unique des recettes signées |

**Mesure non exploitable.** Une sonde coupée peut renvoyer une valeur figée, avec `StatusCode = Bad_SensorFailure` ou un `SourceTimestamp` nul; un outil MCP qui transmettrait ce chiffre seul induirait l’agent en erreur. Le serveur MCP rejette par défaut : il masque toute mesure dont le code n’est pas Good, sans horodatage source ou périmée.

#### Extrait 28.1 — Serveur MCP Python en lecture seule stricte mappant l’espace sémantique OPC UA (réplica IDMZ)

Le serveur est en lecture seule; chaque mesure revient avec son unité, sa plage et son âge.

``` python
from datetime import datetime, timezone
from typing import Any
from asyncua import Client, ua

class ReadOnlyOpcUaMcpServer:
    """
    Serveur MCP déployé en IDMZ (Niveau 3.5) sur le réplica OPC-UA.
    Aucune méthode Write/Call n'est exposée ; certificat X.509 'ObserverOnly'.
    """

    def __init__(
        self, idmz_replica_url: str, max_staleness_sec: float = 10.0
    ) -> None:
        self._endpoint = idmz_replica_url
        self._max_staleness_sec = max_staleness_sec

    async def read_machinery_telemetry_snapshot(
        self,
        asset_node_id: str,
        parameter_browse_names: list[str],
    ) -> dict[str, Any]:
        if len(parameter_browse_names) > 25:
            raise ValueError("MCP_OT_GUARD: Maximum 25 nœuds par lecture")

        async with Client(url=self._endpoint, timeout=3.0) as client:
            asset_node = client.get_node(asset_node_id)
            asset_name = await asset_node.read_display_name()
            readings: dict[str, Any] = {}
            now_utc = datetime.now(timezone.utc)

            for name in parameter_browse_names:
                var_node = await asset_node.get_child(name)
                dv: ua.DataValue = await var_node.read_data_value()
                status_ok = dv.StatusCode.is_good()
                src_ts = dv.SourceTimestamp
                if src_ts is not None and src_ts.tzinfo is None:
                    src_ts = src_ts.replace(tzinfo=timezone.utc)
                age_sec = (
                    (now_utc - src_ts).total_seconds()
                    if src_ts is not None
                    else float("inf")
                )

                unit_str = "dimensionless"
                eu_bounds = None
                for prop in await var_node.get_properties():
                    pname = (await prop.read_browse_name()).Name
                    if pname == "EngineeringUnits":
                        eu = await prop.read_value()
                        disp = getattr(eu, "DisplayName", ua.LocalizedText(""))
                        unit_str = disp.Text or "raw"
                    elif pname == "EURange":
                        r = await prop.read_value()
                        eu_bounds = {"low": float(r.Low), "high": float(r.High)}

                stale_or_invalid = (
                    not status_ok
                    or age_sec < -1.0
                    or age_sec > self._max_staleness_sec
                )
                if stale_or_invalid:
                    readings[name] = {
                        "usableForDecision": False,
                        "opcStatusCode": dv.StatusCode.name,
                        "stalenessSeconds": (
                            round(age_sec, 2) if src_ts is not None else None
                        ),
                        "value": None,
                        "unit": unit_str,
                    }
                else:
                    readings[name] = {
                        "usableForDecision": True,
                        "opcStatusCode": dv.StatusCode.name,
                        "stalenessSeconds": round(age_sec, 2),
                        "value": round(float(dv.Value.Value), 4),
                        "unit": unit_str,
                        "physicalRange": eu_bounds,
                    }

            return {
                "assetNodeId": asset_node_id,
                "assetDisplayName": asset_name.Text,
                "capturedAtUtc": now_utc.isoformat(),
                "telemetry": readings,
            }
```

### Agrégation fréquentielle en périphérie : pourquoi les agents ne lisent pas des flux bruts à 10 kHz

Une erreur classique consiste à injecter des séries temporelles à haute fréquence (accéléromètres piézoélectriques échantillonnés à 10 kHz, courants moteurs à 2 kHz) dans la fenêtre de contexte d’un modèle de langage : le coût en jetons est élevé, et les transformeurs traitent mal des dizaines de milliers de flottants bruités.

Le patron sépare le traitement numérique du signal, déterministe ou confié à un petit modèle spécialisé en séries temporelles, du raisonnement contextuel de l’agent. Un module de précalcul en périphérie calcule en continu la transformée de Fourier rapide (FFT), l’énergie par bande harmonique caractéristique des bagues interne et externe du roulement (*BPFI* et *BPFO*), la valeur efficace (RMS) et l’aplatissement (kurtosis). Le serveur MCP livre à l’agent une vingtaine d’indicateurs physiques interprétables et dimensionnés, qui lui permettent de croiser la signature mécanique avec l’historique des lots d’acier usinés dans Siemens Opcenter MES et la nomenclature des pièces de rechange dans SAP.

---

## 28.8 Validation pré-exécution obligatoire sur jumeau numérique et passage de consigne signée vers MES/SCADA

Passer du diagnostic (L1) à l’action corrective (L2/L3), par exemple moduler la cadence d’un centre d’usinage dont le roulement chauffe afin de terminer un lot urgent avant l’arrêt programmé, place l’agent devant les non-linéarités de la physique. Sur un acier réfractaire ou un alliage de titane, réduire trop l’avance par dent sans adapter la vitesse de coupe provoque un écrouissage thermique, qui accroît l’échauffement et brise l’outil. Un modèle de langage raisonne par analogie qualitative (« ralentir chauffe moins »); seul un solveur physique déterministe résout les équations thermomécaniques. Cette chaîne va au-delà de ce que retient l’exposé pour l’exploitation : l’agent y est une aide à la décision, qui lit, explique et propose (section 28.5), et la commande simple n’est prévue que sur installation d’essai, confirmée par l’opérateur (grille de décision). Ici l’agent se borne à proposer; l’opérateur valide avant toute écriture (section 28.4) et seul le MES ou le SCADA charge la recette. Le qualificatif « obligatoire » du titre est, comme à la section 28.4, une recommandation de ce chapitre : aucune norme lue ne l’impose en ces termes.

### Architecture du sas par jumeau numérique déterministe

Toute consigne descendante franchit trois barrières déterministes; les deux premières sont décrites ici, la troisième (le récepteur côté MES/SCADA) plus bas :

1. **Proposition paramétrique sur gabarit homologué.** L’agent planificateur d’atelier ne cible aucun registre d’automate. Il propose le choix d’une recette pré-cataloguée ISA-88 (par exemple `DERATED_THERMAL_86`) et, le cas échéant, une répartition de lot.
2. **Simulation déterministe avant exécution (niveau 3, solveur FMI 3.0 / FMU).** Le jumeau numérique simule sur l’horizon $H$ la trajectoire physique à partir de l’état réel $x(t_0)$ et vérifie :

$$\forall t \in [t_0, t_0+H], \; \Phi(x(t), u) \le 0 \;\land\; C(u) = 1$$

où $\Phi$ regroupe les plafonds physiques (température palier $\le 78\,^\circ\text{C}$, charge broche $\le 88\,\%$, épaisseur minimale de copeau anti-écrouissage) et $C(u)$ valide la qualité géométrique. En cas de succès, le jumeau signe en matériel (Ed25519 sur TPM/HSM de niveau 3) un jeton d’attestation à validité courte, lié à l’ordre de fabrication exact; sinon, il rejette la proposition, motif à l’appui.

#### Extrait 28.2 — Sas TypeScript de validation pré-exécution auprès du jumeau numérique déterministe (FMI 3.0)

Le sas `DeterministicDigitalTwinGate` rejette par défaut : bornes statiques violées, solveur indisponible, verdict hors enveloppe ou sans signature.

``` typescript
export interface MachiningRegimeProposal {
  readonly sagaId: string;
  readonly workOrderId: string;
  readonly targetCellId: string;
  readonly catalogRecipeTemplateId: string;
  readonly spindleRpm: number;
  readonly feedRateMmPerMin: number;
  readonly splitLotQtyToTwinCell?: number;
}

export interface TwinSimulationVerdict {
  readonly approved: boolean;
  readonly simulationRunId: string;
  readonly predictedPeakBearingTempC: number;
  readonly predictedSpindleLoadPct: number;
  readonly chipLoadMinSatisfied: boolean;
  readonly violationReasons: ReadonlyArray<string>;
  readonly baselineStateHash: string;
  readonly expiresAtEpochMs: number;
  readonly ed25519AttestationSignature?: string;
}

export class DeterministicDigitalTwinGate {
  constructor(
    private readonly twinSolverEndpoint: string,
    private readonly maxBearingTempC: number = 78.0,
    private readonly maxSpindleLoadPct: number = 88.0
  ) {}

  public async validateBeforeShopfloorDispatch(
    proposal: MachiningRegimeProposal,
    currentTelemetry: Record<string, number>
  ): Promise<TwinSimulationVerdict> {
    if (proposal.spindleRpm < 800 || proposal.spindleRpm > 12000) {
      throw new Error("TWIN_STATIC_BOUND_VIOLATION: RPM hors domaine physique");
    }

    const res = await fetch(this.twinSolverEndpoint + "/v3/fmu/simulate-regime", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        proposal,
        initialState: currentTelemetry,
        horizonMinutes: 90
      })
    });
    if (!res.ok) {
      throw new Error("TWIN_SOLVER_UNAVAILABLE_FAIL_CLOSED:" + String(res.status));
    }

    const v = (await res.json()) as TwinSimulationVerdict;
    if (
      !v.approved ||
      !v.chipLoadMinSatisfied ||
      v.predictedPeakBearingTempC > this.maxBearingTempC ||
      v.predictedSpindleLoadPct > this.maxSpindleLoadPct ||
      !v.ed25519AttestationSignature
    ) {
      return { ...v, approved: false, ed25519AttestationSignature: undefined };
    }
    return v;
  }
}
```

### Protocole de passage de consigne signée vers MES/SCADA et contrôle de non-dérive ($\Delta t$)

Entre la capture $t_0$ de la simulation et la réception aux niveaux 3 et 2 (Siemens Opcenter MES, SCADA), l’atelier a évolué. Avant de charger la recette, et une fois la validation humaine acquise (section 28.4), le récepteur déterministe vérifie quatre conditions atomiques :

- **Signature.** La signature Ed25519 du jumeau numérique est valide sur les paramètres exacts de la recette et le `workOrderId` courant, ce qui empêche le rejeu entre lots d’alliages distincts et toute falsification depuis la zone IT.
- **Fraîcheur temporelle et non-dérive physique.** Certificat non expiré, âge du capteur local $\Delta t \le 5\,\text{s}$, écart thermique depuis $t_0$ inférieur à $\delta_{\max} = 1{,}5\,^\circ\text{C}$.
- **Interverrouillage de sûreté.** Barrières immatérielles dégagées et sélecteur physique sur AUTO (hors cadenassage de maintenance, LOTO).
- **Frontière de cycle PackML.** Application différée à la fin de la pièce en cours (COMPLETE ou IDLE), jamais au milieu d’une passe d’usinage.

#### Extrait 28.3 — Récepteur déterministe côté MES/SCADA contrôlant signature, fraîcheur et interverrouillages

Le récepteur applique ces contrôles, puis met la recette en attente jusqu’à la frontière de cycle.

``` typescript
import { verify } from "node:crypto";

export interface SignedShopfloorDispatch {
  readonly dispatchId: string;
  readonly proposal: {
    readonly workOrderId: string;
    readonly targetCellId: string;
    readonly catalogRecipeTemplateId: string;
    readonly spindleRpm: number;
    readonly feedRateMmPerMin: number;
  };
  readonly twinAttestation: {
    readonly simulationRunId: string;
    readonly baselineBearingTempC: number;
    readonly expiresAtEpochMs: number;
    readonly ed25519SignatureHex: string;
  };
}

export interface LiveCellInterlockState {
  readonly sensorAgeMs: number;
  readonly currentBearingTempC: number;
  readonly safetyLightCurtainClear: boolean;
  readonly selectorMode: "AUTO" | "MANUAL_JOG" | "MAINTENANCE_LOCKOUT";
  readonly packMlState: "IDLE" | "EXECUTE" | "HOLD" | "COMPLETE" | "ABORTED";
}

export function verifyAndStageMesRecipe(
  dispatch: SignedShopfloorDispatch,
  liveCell: LiveCellInterlockState,
  twinPublicKeyPem: string
): { staged: true; applyOnPackMlBoundary: string } {
  const canonical = Buffer.from(
    JSON.stringify({
      runId: dispatch.twinAttestation.simulationRunId,
      workOrder: dispatch.proposal.workOrderId,
      cell: dispatch.proposal.targetCellId,
      recipe: dispatch.proposal.catalogRecipeTemplateId,
      rpm: dispatch.proposal.spindleRpm,
      feed: dispatch.proposal.feedRateMmPerMin,
      baseTemp: dispatch.twinAttestation.baselineBearingTempC,
      exp: dispatch.twinAttestation.expiresAtEpochMs
    }),
    "utf8"
  );

  const valid = verify(
    null,
    canonical,
    twinPublicKeyPem,
    Buffer.from(dispatch.twinAttestation.ed25519SignatureHex, "hex")
  );
  if (!valid) {
    throw new Error("OT_SECURITY_REJECT: Signature Ed25519 invalide");
  }
  if (Date.now() > dispatch.twinAttestation.expiresAtEpochMs) {
    throw new Error("OT_STALE_SIMULATION_REJECT: Certificat expiré");
  }
  if (liveCell.sensorAgeMs > 5_000) {
    throw new Error("OT_SENSOR_STALE_REJECT: Télémétrie > 5000 ms");
  }

  const drift = Math.abs(
    liveCell.currentBearingTempC - dispatch.twinAttestation.baselineBearingTempC
  );
  if (drift > 1.5) {
    throw new Error(`OT_STATE_DRIFT_REJECT: Dérive ${drift.toFixed(2)} °C`);
  }
  if (!liveCell.safetyLightCurtainClear || liveCell.selectorMode !== "AUTO") {
    throw new Error("OT_HUMAN_SAFETY_INTERLOCK_ACTIVE: Cellule hors mode AUTO");
  }
  if (liveCell.packMlState === "ABORTED") {
    throw new Error("OT_CELL_ABORTED: Acquittement HMI requis");
  }

  const boundary =
    liveCell.packMlState === "IDLE" ? "IMMEDIATE_AT_IDLE" : "NEXT_PART_COMPLETE";
  return { staged: true, applyOnPackMlBoundary: boundary };
}
```

### Gouvernance de l’écart simulation-réalité et repli automatique après application

La sûreté du sas dépend de la fidélité du modèle physique sous-jacent (Functional Mock-up Unit, FMU, selon la norme ouverte FMI 3.0). Or une machine vieillit : un échangeur de liquide de refroidissement qui s’encrasse en été, ou un lot de brut de fonderie plus dur que la norme, dégrade peu à peu la précision prédictive des équations initiales.

Deux mécanismes encadrent le jumeau en exploitation continue :

- **Surveillance post-application et retour automatique au profil sûr.** Dès qu’une nouvelle recette homologuée entre en vigueur sur la cellule, un chien de garde déterministe local compare toutes les dix secondes la courbe thermique mesurée $T_{\text{réel}}(t)$ à la trajectoire prédite $T_{\text{sim}}(t)$ lors de l’attestation. Si l’écart résiduel dépasse $2{,}0\,^\circ\text{C}$ pendant trois cycles consécutifs, le SCADA révoque la recette active sans attendre d’ordre de l’IT, rebascule la cellule en repli conservateur pré-programmé et notifie l’orchestrateur Temporal.
- **Réétalonnage hors ligne gouverné.** Les résidus d’observation sont accumulés dans l’historien pour recalibrer périodiquement les coefficients de transfert thermique de la FMU. Selon les principes de gestion du changement industriel, aucune mise à jour des paramètres internes du jumeau n’est déployée de façon autonome en ligne : chaque nouvelle version de FMU passe une batterie de tests de validation sur des incidents historiques rejoués et reçoit le visa d’un ingénieur procédés avant signature et mise en service au niveau 3.

### Coordination intralogistique multi-constructeurs (VDA 5050) et horizon OPC UA FX sur TSN

Le rééquilibrage d’une cadence d’usinage a des effets immédiats sur la logistique interne des usines et des centres de distribution automatisés : chariots filoguidés (AGV) et robots mobiles autonomes (AMR) amènent les bruts de fonderie et évacuent les palettes usinées. Avec des robots mobiles de trois fabricants, l’enfermement propriétaire propre au SaaS menace aussi les niveaux 2 et 3.

Le sas déterministe s’étend à l’intralogistique par le standard ouvert VDA 5050 sur MQTT. Quand le jumeau d’atelier valide un délestage de lot (par exemple, réorienter 35 % des pièces de CNC02 vers CNC04), le MES n’envoie aux robots mobiles aucune trajectoire libre calculée par un modèle de langage. Il publie une mission de haut niveau au gestionnaire de flotte maître (*Master Control*) VDA 5050. Celui-ci calcule de façon déterministe les réservations de nœuds topologiques d’allées, l’évitement des embouteillages aux intersections et le respect des zones de croisement piétonnes surveillées par des scrutateurs laser de sécurité (PL d selon ISO 13849-1).

Le déploiement progressif en 2026–2027 d’OPC UA FX (*Field eXchange*) sur Ethernet déterministe TSN (*Time-Sensitive Networking*, IEEE 802.1Qbv) fait converger la couche de transport physique des ateliers neufs, sans abolir la frontière logique de gouvernance. Le partitionnement temporel des trames TSN réserve aux flux d’asservissement isochrones du niveau 1 une bande passante, à la microseconde près, que le trafic de télémétrie OPC UA PubSub montant vers l’IDMZ ne peut pas retarder.

---

## 28.9 Éclairages sectoriels : sûreté fonctionnelle (SIL) et périphérie industrielle déconnectée

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Énergie, mines et sûreté fonctionnelle — isolement des systèmes SIS (IEC 61511 SIL 2/3) et NERC CIP**
:::

Dans une centrale électrique soumise à NERC CIP, ou dans un procédé lourd régi par IEC 61508 et IEC 61511, le contrôle de procédé courant (BPCS : SCADA, automates) est doublé d’un système instrumenté de sécurité (SIS) certifié SIL 2 ou SIL 3, qui ramène physiquement l’installation à un état sûr avant tout emballement critique. La fabrique agentique n’a aucun lien d’écriture, logique ou électrique, vers le SIS (section 28.4).

- Toute modification dynamique d’un seuil SIS par un agent invaliderait l’homologation légale d’exploitation et engagerait la responsabilité pénale de la direction.
- Même si l’agent et le jumeau numérique sont défaillants en même temps sur une consigne du MES, le SIS, câblé indépendamment, garde son autorité matérielle pour couper l’énergie avant tout dommage humain ou structurel.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Sites miniers éloignés et résilience du WAN — inférence locale d’un petit modèle de langage sur Industrial Edge**
:::

Une mine souterraine nordique ou une usine forestière éloignée subit régulièrement des coupures de liaison satellite ou fibre (WAN); dépendre d’un modèle infonuagique distant pour les alarmes critiques d’aérage ou de concassage est inacceptable.

Le patron déploie au niveau 3 du site un serveur durci Industrial Edge qui exécute :

1. Le serveur MCP OPC UA local, le jumeau numérique FMU et un travailleur d’orchestration durable autonome.
2. Un petit modèle de langage quantifié (7 à 14 milliards de paramètres), spécialisé sur les manuels techniques et les codes de défaut des équipements du site. En mode isolé, le diagnostic prédictif, la validation par jumeau numérique et le guidage des électromécaniciens restent opérationnels à 100 %, puis les journaux sont resynchronisés au retour du lien WAN.
::::

---

## 28.10 Application au fil rouge : orchestration cyber-physique à l’usine Boréal de Trois-Rivières

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Maintenance prédictive et rééquilibrage de cadence à l'usine de Trois-Rivières**
:::

**Problème industriel initial (T2 2027)** : l’usine de Boréal Équipements & Logistique (BEL) à Trois-Rivières usine des corps de compresseurs sur six cellules robotisées 5 axes (Siemens Sinumerik OPC UA), pilotées par Siemens Opcenter MES et SAP S/4HANA. Faute de pont entre maintenance et ordonnancement, une dégradation de roulement de broche entraînait soit une casse en cours d’usinage (38 000 \$ CAD de rebut de fonte nodulaire et 18 heures d’arrêt), soit un arrêt préventif abrupt déclenchant des pénalités de retard client.

**Architecture déployée sous IEC 62443-3-3 SL-3 (T3 2027)** : une IDMZ (niveau 3.5) isole l’atelier du nuage corporatif via un réplica OPC UA (OPC 40501) et un pont MQTT Sparkplug B :

1. **Diagnostic en lecture seule (L1).** Par `ReadOnlyOpcUaMcpServer` (Extrait 28.1), l’agent vibratoire détecte sur TRV-CELL-CNC02 une élévation spectrale et thermique (69,4 °C, `StatusCode = Good`) limitant la vie résiduelle (RUL) à 11 heures à pleine charge.
2. **Corrélation IT/OT.** Temporal croise Opcenter MES (14 heures restantes sur la commande urgente SO-77410) et SAP Joule (roulement céramique en stock local et créneau de maintenance libre à 22 h 00).
3. **Sas du jumeau numérique (`DeterministicDigitalTwinGate`).** Une première suggestion de l’agent (-22 % d’avance) est rejetée par le solveur FMU pour risque d’écrouissage thermique. La seconde itération (`DERATED_THERMAL_86` à -14 %, qui plafonne le palier à 72,1 °C, avec délestage de 35 % du lot vers la cellule jumelle CNC04) est homologuée et signée Ed25519.
4. **Exécution HOTL et intralogistique VDA 5050.** Après acquittement sur pupitre IHM par le chef d’îlot, le MES vérifie la signature, la fraîcheur du capteur (420 ms) et les barrières immatérielles (Extrait 28.3), bascule la recette à l’état PackML COMPLETE, puis notifie le gestionnaire de flotte VDA 5050 afin que deux chariots autonomes AMR réacheminent automatiquement les palettes d’ébauches vers CNC04, sans croiser l’allée piétonne principale.

**Résultats vérifiés sur deux trimestres à Trois-Rivières** :

- **Arrêts non planifiés sur bris de broche** : baisse de 78 % (zéro rebut thermique de corps de compresseur).
- **Taux de rendement synthétique (OEE) sur les 6 cellules** : hausse de 4,6 points, générant 1,9 M\$ CAD de marge industrielle annualisée.
- **Conformité cyber IEC 62443** : homologation SL-3 validée, 0 paquet IT sous le niveau 3.5, et 34 propositions hors enveloppe bloquées par le jumeau numérique.
::::

---

## 28.11 Décision d’architecture normative et points de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-017 — Architecture en sas par Jumeau numérique et validation déterministe pour toute consigne IT→OT**
:::

- **Statut** : Acceptée (recommandation du chapitre, non imposée par une norme lue; section 28.4) \| Périmètre : usines, entrepôts automatisés et réseaux OT \| Révision : annuelle (CISO et Direction Ingénierie Industrielle)
- **Contexte** : connecter des agents de planification aux équipements industriels améliore l’OEE, mais expose l’outil de production et le personnel aux propositions physiquement erronées, à la perturbation des bus temps réel et aux mouvements latéraux IT → OT.
- **Options évaluées** :
  1. *Isolement complet sans passerelle agentique* : rejetée; maintient des délais manuels de plusieurs jours entre l’alerte du capteur, le stock ERP et l’ordonnancement.
  2. *Serveurs MCP en lecture/écriture directe sur automates OPC UA / Modbus* : rejetée, pour danger physique et violation de l’IEC 62443.
  3. *Segmentation IDMZ, avec lecture sur réplica et sas obligatoire par jumeau numérique déterministe avant recette signée MES/SCADA* : retenue.
- **Décision** : (a) toute lecture OT s’effectue sur un réplica dans l’IDMZ (niveau 3.5), avec validation du `StatusCode` et de l’âge du signal; (b) tout accès direct d’un agent aux automates du niveau 1 ou au SIS est interdit; (c) toute consigne descendante cible un gabarit de recette pré-homologué, obtient du jumeau numérique une signature Ed25519, avec rejet par défaut, et franchit les contrôles de fraîcheur ($\Delta t \le 5\,\text{s}$), d’interverrouillage humain et d’état PackML au niveau MES/SCADA. Ces contrôles automatiques ne dispensent pas de la validation humaine, obligatoire avant toute écriture (section 28.4).
- **Conséquences** :
  - *Positives* (effets attendus; aucun déploiement en production n’est documenté par une source lue, section 28.5) : sûreté physique visée, déterminisme `< 10 ms` préservé, certification IEC 62443 SL-3 et adhésion des équipes d’automaticiens.
  - *Négatives (coûts assumés)* : étalonnage continu des modèles physiques FMU du jumeau et exploitation de la zone IDMZ.
- **Condition de révision** : déploiement sur de nouvelles usines ou évolution des standards OPC UA FX et IEC 62443.
::::

### Liste de contrôle de mise en production

Avant tout raccordement d’un flux agentique à une installation industrielle, exigez la validation conjointe IT et OT sur ces huit points, qui s’ajoutent à la validation humaine obligatoire avant toute écriture (section 28.4) :

1. **Rupture de protocole dans l’IDMZ.** Aucun flux IP initié depuis le réseau IT ou le nuage ne passe-t-il directement sous le niveau 3.5 ?
2. **Isolement du SIS.** Est-il prouvé matériellement qu’aucun composant logiciel, jumeau compris, n’a de canal d’écriture vers les automates de sécurité (IEC 61511 SIL 2/3) ?
3. **Protection contre la saturation.** Le serveur MCP interroge-t-il uniquement un réplica OPC UA, un pont MQTT Sparkplug ou un historien en IDMZ, sans jamais scruter directement les automates ?
4. **Unités et `StatusCode` vérifiés.** Toute mesure Bad, Uncertain ou périmée est-elle neutralisée automatiquement avant transmission à l’agent, avec ses unités UNECE explicites ?
5. **Jumeau numérique en rejet par défaut.** Toute indisponibilité du solveur FMU ou tout dépassement de l’enveloppe physique entraîne-t-il le rejet de la consigne ?
6. **Signature Ed25519 obligatoire.** Le MES/SCADA rejette-t-il toute recette dépourvue d’une signature cryptographique valide et non expirée du jumeau numérique ?
7. **Contrôle de non-dérive et sûreté des personnes.** L’automate de supervision vérifie-t-il la fraîcheur du capteur ($\Delta t \le 5\,\text{s}$), l’absence de dérive thermique, le mode AUTO et l’intégrité des barrières immatérielles ?
8. **Synchronisation PackML.** Le changement de recette s’applique-t-il exclusivement sur une frontière d’état machine sûre (IDLE ou COMPLETE) ?
