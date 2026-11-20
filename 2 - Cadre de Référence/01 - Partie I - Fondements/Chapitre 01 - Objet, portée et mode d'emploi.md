# 1 Objet, portée et mode d’emploi

Ce chapitre dit ce que le cadre règle, à quels systèmes il s’applique et à qui il s’adresse. Il explique comment lire une exigence, comment le document est organisé et comment il évolue. Il présente enfin la méthode qui a servi à l’établir et à vérifier ses faits.

## 1.1 Objet

Le cadre CRE-IA-2026-01 fixe les règles communes qui permettent aux agents d’IA de l’entreprise de se brancher aux systèmes, de collaborer entre eux et d’être orchestrés de façon sûre, traçable, réversible et économiquement maîtrisée, quel que soit le fournisseur. La présente version 1.2, datée du 19 novembre 2026, consolide le socle unifié de 305 exigences normatives (exportées dans `exigences.json`) à des fins de consultation par les architectes d’entreprise (AE) et de solutions (AS). Le cadre poursuit quatre objectifs :

- donner à toutes les équipes un vocabulaire commun (chapitre 3);
- fixer les protocoles retenus, les patrons d’orchestration autorisés et les niveaux d’autonomie permis (chapitres 5 à 8);
- encadrer l’identité, la sécurité, l’observabilité, les coûts, la gouvernance et la conformité des agents (chapitres 9 à 13);
- offrir une trajectoire de maturité mesurable et une grille d’homologation applicable à chaque projet (chapitres 14 et 15, annexe A).

Le cadre est normatif et neutre à l’égard des fournisseurs. Il règle ce qui doit rester sous le contrôle de l’entreprise, quelle que soit la plateforme : contrats d’interface, identités et délégations, passage obligé par la passerelle d’agents, traces et journal d’audit, registre, plafonds d’autonomie et de coûts. Il ne choisit aucun produit : ceux qu’il cite sont des exemples non limitatifs, à l’état du 27 octobre 2026. Il ne tient pas lieu d’avis juridique (chapitre 12).

## 1.2 Portée

Cette section délimite les systèmes visés (tableau 1). Le critère est fonctionnel : ce qui compte n’est pas l’étiquette commerciale d’un système, mais sa capacité à appeler des outils ou à agir sur des systèmes et des données de l’entreprise.

*Tableau 1 — Portée du cadre*

| **Catégorie** | **Dans la portée** | **Hors portée** |
| --- | --- | --- |
| Agents internes | Tout agent bâti à l’interne, en pilote ou en production, qui lit ou modifie des systèmes ou des données de l’entreprise | Assistant conversationnel sans outil ni capacité d’action, régi par la politique d’usage de l’IA |
| Agents achetés | Agents intégrés aux logiciels-services *(software as a service, SaaS)* et aux progiciels, dès qu’ils peuvent agir sur des systèmes ou des données de l’entreprise, qu’ils aient été activés par l’éditeur, par une équipe ou par un employé (EXIG-ARC-21) | Fonction dite « agentique » qui n’appelle aucun outil et n’agit sur rien |
| Agents de tiers | Agents de partenaires, de fournisseurs ou de clients qui échangent avec les agents ou les systèmes de l’entreprise | Fonctionnement interne de ces agents : le cadre en régit les interfaces, les identités et les contrats |
| Outils et données | Serveurs MCP internes ou externes, outils, API, événements et sources de données exposés aux agents | Systèmes d’enregistrement eux-mêmes, dont le cadre n’impose pas la réécriture (un ajout minimal pour l’idempotence ou la trace reste permis, EXIG-ARC-14) |
| Plateformes | Plateformes et moteurs d’orchestration, passerelles d’agents et de modèles, registres et catalogues | Choix des fournisseurs de modèles, qui relève de l’architecture d’entreprise et de l’approvisionnement |
| Modèles et automatisation | Usage des modèles par les agents; flux de travail assisté par IA (section 3.2); flux déterministe qui appelle un agent ou qui est appelé par lui, soumis aux contrôles de cet agent | Entraînement et ajustement fin des modèles; automatisation robotisée des processus (RPA) sans composante agentique |

Trois règles tranchent les cas limites. Un assistant qui reçoit un premier outil, même en lecture seule, ou un premier accès à une ressource ou à des données de l’entreprise (un index documentaire, par exemple), entre dans la portée dès ce moment. À l’inverse, une fonction qu’un éditeur qualifie d’agentique n’y entre que si elle appelle des outils ou agit; l’étiquetage agentique abusif que relève Gartner est traité à la section 2.1 **[3]**. En cas de doute, le système est traité comme visé et inscrit au registre (section 11.4).

## 1.3 Public cible et usages par rôle

Le cadre s’adresse à toutes les fonctions qui conçoivent, exploitent, financent ou contrôlent des agents. Personne n’a besoin de tout lire : le tableau 2 indique, pour chaque rôle, par où commencer.

*Tableau 2 — Parcours de lecture par rôle*

| **Rôle** | **À lire en priorité** |
| --- | --- |
| Direction TI et comité d’architecture et des risques agentiques | Sommaire, chapitres 2, 4, 14 et 15 |
| Architectes d’entreprise et de solutions | Chapitres 3 à 8, annexe A |
| Équipes de plateforme et d’intégration | Chapitres 5, 6, 9 et 10, annexe C |
| Équipes produit qui bâtissent des agents | Chapitres 3, 7, 8 et 10, annexes A à C |
| Sécurité de l’information | Chapitres 8 et 9, section 12.8 |
| Risques, conformité, affaires juridiques et protection des renseignements personnels (RP) | Chapitres 11 et 12, section 8.8 |
| FinOps | Sections 10.5 et 10.6, chapitre 13 |
| Responsables métier, parrains d’agents | Sommaire, chapitres 3, 8 et 11, annexe B |
| Approvisionnement | Chapitre 13, section 6.3 |
| Audit interne | Annexes A et D, sections 11.4 et 12.6 |

### Appliquer le cadre à un projet

1. Vérifier la portée et inscrire le système au registre dès la conception (annexe B).
2. Classer le risque (section 12.1), fixer le niveau d’autonomie sous le plafond de la classe (EXIG-CON-02, section 12.1) et déterminer les évaluations d’impact requises (section 12.9).
3. Retenir l’option la plus simple qui suffit, puis le patron d’orchestration (section 7.3).
4. Choisir les protocoles (section 6.3) et publier les contrats au catalogue d’entreprise (section 6.8).
5. Appliquer les exigences pertinentes (annexe D); justifier par écrit tout écart à une recommandation (niveau DEVRAIT) et obtenir une dérogation pour tout écart à une obligation (niveau DOIT) (section 11.6).
6. Remplir la grille d’homologation (annexe A) avant toute mise en production.

## 1.4 Force normative

Cette section explique comment lire une exigence. Le cadre emploie trois degrés d’obligation (tableau 3), inspirés des mots-clés de la RFC 2119 de l’Internet Engineering Task Force (IETF) et mis en évidence dans le texte.

*Tableau 3 — Degrés d’obligation*

| **Expression** | **Sens** | **Écart admis** |
| --- | --- | --- |
| doit, ne doit pas | Obligation | Aucun, sauf dérogation écrite approuvée par le comité (ou, pour un agent de classe faible, par l’architecture d’entreprise sur délégation du comité, pour 90 jours au plus et par une autre personne que celle qui a instruit la demande), limitée dans le temps et assortie de mesures compensatoires (section 11.6, EXIG-GOV-15). Les points de l’EXIG-GOV-17, seule liste qui fasse foi, n’admettent aucune dérogation. |
| devrait, ne devrait pas | Recommandation | Admis s’il est justifié par écrit dans la fiche d’agent ou la décision d’architecture; la revue d’architecture contrôle la justification. |
| peut | Option | Sans objet. |

Chaque exigence occupe un bloc qui réunit un identifiant stable (par exemple EXIG-AUT-09), son degré d’obligation, un titre court, un énoncé vérifiable en revue d’architecture ou en test (ou, à défaut, par une justification consignée), et une justification introduite par « Pourquoi ». Dans l’énoncé d’un bloc, toute phrase à l’indicatif qui prescrit un comportement a la force du degré d’obligation inscrit à l’en-tête du bloc, même sans mot-clé en gras; la justification et les exemples sont informatifs. Créent une obligation normative :

- les blocs d’exigences (chapitres 5 à 13) et les principes directeurs PRIN-01 à PRIN-12 (chapitre 4);
- les règles d’interprétation des sections 1.2 (critère de portée et règle du doute), 1.4 (force de l’indicatif dans un bloc), 1.5, 1.6, 4.2 (devoir de l’architecte) et 4.3;
- les définitions du tableau 7; pour les niveaux d’autonomie et les paliers d’outils, les tableaux 28 et 31 font foi, et la section 3.1 en donne un résumé;
- les tableaux et les structures d’annexe auxquels une exigence renvoie expressément : l’annexe A par l’EXIG-GOV-11, le contenu (non la forme) de l’annexe B par l’EXIG-GOV-07, C.1 et C.2 par l’EXIG-ORC-22 et l’EXIG-MCP-20, C.6 par l’EXIG-AUT-12, C.8 par l’EXIG-OBS-12;
- la liste des neuf contrôles de la passerelle d’agents (section 9.4, « Fonctions obligatoires »), à laquelle renvoie l’EXIG-IAM-17; la figure 18 l’illustre;
- la définition des trois indicateurs d’économie unitaire (section 10.6, « Imputation et économie unitaire »), à laquelle renvoie l’EXIG-FIN-10;
- le tableau 58, pour ses phases d’exigibilité (régime transitoire de la section 11.6) et pour les critères de ses jalons;
- les règles de progression et l’encadré « Jalon 2a » de la section 15.1, les règles de mesure des indicateurs de la section 15.3 et la règle de recul de maturité de la section 14.2, dont les « doit » et les « ne doit pas » ont la force du tableau 3, sans bloc d’exigence propre.

Le reste du texte, y compris l’annexe H, les exemples et les figures, est informatif. Est une mise en production tout usage d’un agent avec des justificatifs de production ou des données réelles, pilote compris (EXIG-GOV-08).

### Exigence externe ou choix du cadre

Le cadre distingue toujours ce qui vient d’un texte externe de ce qu’il décide lui-même. « La spécification MCP exige » ou « selon l’article 14 du règlement (UE) 2024/1689 sur l’IA (RIA) » rapportent le contenu d’une norme ou d’une loi, vérifié à la source. « Le cadre fixe » ou « choix du cadre » signalent une décision interne, que le comité peut réviser. Exemple : le guide de Microsoft recommande un plafond d’itérations pour la boucle producteur-vérificateur (évaluateur-optimiseur au chapitre 7), sans en fixer la valeur **[9]**; le plafond de trois itérations retenu au chapitre 7 est donc un choix du cadre. Le cadre n’attribue jamais à une norme une exigence qu’elle ne contient pas et présente ses seuils chiffrés (délais, plafonds, fréquences) comme les siens.

**À RETENIR**

Trois règles de lecture : un fait externe porte sa source et sa date; un chiffre de fournisseur est présenté comme une allégation de ce fournisseur; un produit cité est un exemple, jamais une exigence.

## 1.5 Structure du document et identifiants

Le document compte quinze chapitres en quatre parties : Fondements (chapitres 1 à 4); Architecture, interopérabilité et orchestration (5 à 8); Confiance et exploitation (9 et 10); Gouvernance, conformité et mise en œuvre (11 à 15). Huit annexes, de A à H, fournissent les outils d’application, le glossaire et les références; l’annexe H, informative, consigne l’actualisation du 1er novembre 2026.

Les douze principes directeurs portent les identifiants PRIN-01 à PRIN-12. Chaque exigence porte un identifiant de la forme EXIG-XXX-NN : un préfixe de trois caractères propre à un domaine, puis un numéro à deux chiffres, continu pour chaque préfixe. Les chapitres 1 à 4, 14 et 15 et les annexes ne créent pas d’exigences numérotées; l’annexe D récapitule toutes les exigences dans l’ordre du document, soit 305 dans la version 1.2 (287 dans la version 1.1, auxquelles s’ajoutent 12 exigences EXIG-AMF et 6 exigences PQC, ACVM 11-348, RTR/ISO 20022 et EN 18286:2026). Choix du cadre : un identifiant n’est jamais réattribué, et une exigence retirée lors d’une révision conserve son numéro, marqué « retirée »; une exigence devenue un renvoi garde son identifiant et son titre. Le tableau 4 donne la liste des préfixes.

*Tableau 4 — Identifiants des principes et préfixes des exigences*

| **Identifiant ou préfixe** | **Domaine** | **Emplacement** |
| --- | --- | --- |
| PRIN-01 à PRIN-12 | Principes directeurs | Chapitre 4 |
| EXIG-ARC | Architecture de référence | Chapitre 5 |
| EXIG-INT | Interopérabilité, contrats et catalogue d’entreprise | Sections 6.1 à 6.4, 6.8 et 6.9 |
| EXIG-MCP | Model Context Protocol | Section 6.5 |
| EXIG-A2A | Protocole Agent2Agent | Section 6.6 |
| EXIG-EVT | Interopérabilité événementielle | Section 6.7 |
| EXIG-ORC | Orchestration | Chapitre 7 |
| EXIG-AUT | Autonomie et supervision humaine | Chapitre 8 |
| EXIG-IAM | Confiance zéro, identité, délégation et passerelle d’agents | Sections 9.1 à 9.4 |
| EXIG-SEC | Menaces propres aux agents et défenses | Sections 9.5 à 9.9 |
| EXIG-OBS | Traçage et journal d’audit | Sections 10.1 à 10.3 |
| EXIG-EVA | Évaluation continue | Section 10.4 |
| EXIG-FIN | Économie de l’inférence et maîtrise des coûts | Sections 10.5 et 10.6 |
| EXIG-GOV | Gouvernance et cycle de vie | Chapitre 11 |
| EXIG-CON | Risques, conformité et réglementation | Chapitre 12 (sections 12.1 à 12.10) |
| EXIG-AMF | Profil québécois AMF IA et gestion du risque de modèle | Section 12.10 |
| EXIG-APP | Approvisionnement et clauses contractuelles | Chapitre 13 |

Un terme anglais figure entre parenthèses et en italique à sa première occurrence, comme transfert *(handoff)*; les noms de protocoles, de champs et de méthodes restent en police à chasse fixe, comme `tools/call`. Les appels de citation renvoient à l’annexe G.

## 1.6 Relation avec les autres politiques et cycle de révision

Le cadre complète, sans les remplacer, les politiques de sécurité de l’information, de gouvernance des données, de protection des RP, d’usage de l’IA, de gestion des risques et d’approvisionnement. Celles-ci continuent de régir leur objet; le cadre en précise l’application aux agents. Choix du cadre : lorsqu’une règle du cadre et celle d’une autre politique visent le même objet, les deux s’appliquent si elles sont cumulables; sinon, l’ordre de départage de la section 4.3 tranche et la contradiction est soumise au comité. Le droit applicable prime toujours; les engagements contractuels en vigueur à l’adoption du cadre priment pour une transition bornée et inscrite au registre, sauf sur les points de l’EXIG-GOV-17 (section 4.3).

Deux rythmes de révision coexistent, semestriel pour le cadre et trimestriel pour le catalogue; les versions applicables suivent celui du catalogue.

- **Le cadre** est révisé chaque semestre par le comité, à partir des dérogations accordées, des incidents, des résultats d’homologation et de la veille; une révision extraordinaire suit tout incident grave (section 12.8) ou changement réglementaire majeur. Une règle qui suscite des dérogations répétées est à revoir.
- **Le catalogue des protocoles et standards** est révisé au moins chaque trimestre par l’architecture d’entreprise, qui soumet les changements de statut à l’approbation du comité (EXIG-GOV-18, sections 6.3 et 11.7); pour un standard au statut Adopter ou Contenir, la publication d’une version incompatible, d’une dépréciation, d’un retrait accéléré ou d’un correctif de sécurité déclenche une révision extraordinaire, dans les 15 jours ouvrables.
- **Les versions applicables**, comme MCP 2026-07-28 ou A2A 1.0, sont épinglées au catalogue des protocoles. Là où une exigence renvoie à « la version épinglée au catalogue », le catalogue fait foi, et la version citée dans le texte en est la valeur initiale; une échéance datée par une exigence (la migration MCP de l’EXIG-MCP-22, par exemple) reste dans le texte et ne change que par une révision du cadre.

Chaque révision porte un numéro de version et une date, et s’accompagne d’un relevé des modifications. La mise en conformité des agents déjà en service suit le régime transitoire de la section 11.6 (EXIG-GOV-16 et EXIG-GOV-17); les phases et les jalons du chapitre 15 en ordonnent la planification.

## 1.7 Méthode d’élaboration

La version 1.0 consolide quatre ébauches : une recherche documentaire appuyée sur 121 références, deux versions de travail successives du cadre et une version structurée en exigences. Elle suit la structure de la version de travail la plus récente, y intègre les exigences des autres ébauches et les réécrit pour qu’elles soient vérifiables. Chaque fait a ensuite été vérifié, aux 27 et 28 octobre 2026, contre des sources primaires ou, à défaut, secondaires reconnues, en trois passes :

1. la validation, une à une, des 121 références : chaque affirmation qui en citait une a été confrontée à la source (427 liens au total), au contenu réel de la page lorsqu’elle était accessible (108 références sur 121) et, sinon, à des sources équivalentes, faute de quoi elle a été déclarée invérifiable;
2. onze vérifications thématiques, de MCP au droit québécois, qui ont confronté les ébauches aux textes primaires et recueilli des faits complémentaires;
3. un audit final de cohérence interne, factuelle et juridique de l’ensemble des chapitres, le 28 octobre 2026, qui a rouvert les 428 références alors citées et examiné 1 409 affirmations; l’annexe G comptait alors 473 entrées dont 25 doublons (448 sources distinctes); les 25 doublons ont depuis été fusionnés dans leurs entrées canoniques et la version 1.1 y ajoute la référence [474] (RFC 7515, ex-[496]), soit 449 sources distinctes ordonnées de [1] à [474], suivies des références [475] à [496] en annexe H (annexe F.1).

Les sources sont classées en trois catégories : A, primaires ou officielles; B, secondaires reconnues; C, blogues de positionnement ou agrégateurs. Une source de catégorie C n’appuie jamais une exigence, une obligation légale ni un fait; un argument d’éditeur peut seulement être rapporté comme tel. Un fait réfuté ou invérifiable a été corrigé, retiré ou, lorsqu’il exprimait une décision utile, conservé comme choix du cadre et signalé comme tel.

La vérification a deux limites. Elle reflète l’état des sources au 27 octobre 2026, vérifié les 27 et 28 octobre 2026, alors que plusieurs standards évoluent d’un trimestre à l’autre. Certains textes payants, comme les normes ISO/IEC, ont été vérifiés par leur fiche de catalogue et des sources secondaires concordantes; le cadre évite donc de les citer textuellement. L’annexe F détaille la méthode, le bilan et les corrections.

Deux reprises ont suivi ces vérifications. L’actualisation du 1er novembre 2026 a rouvert sur leur source primaire les sources datées dont dépend une exigence ou une échéance (annexe H, sections H.1 à H.5; seuls ses errata corrigent le corps). La revue contradictoire du 3 novembre 2026 a fait intégrer au corps des correctifs de cohérence interne, de précision normative et de vérification bibliographique (section H.6).
