# Chapitre 24 — Passerelles et intégration

*Question directrice : où appliquer les contrôles entre agents, outils et API ?*

> **État de référence :** spécification MCP `2026-07-28`, brouillon « MCP Security Gateway 1.0 » de Microsoft, documentation d'agentgateway, d'Agent Router, d'Apigee, d'Azure API Management, de Kong et de MuleSoft Agent Fabric consultée les 11 et 12 novembre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre, toutes lues pour ce chapitre; [13] à [16] ont été ajoutées le 14 novembre 2026, [16] par son seul résumé. [1] et [6] sont des billets d'annonce : ils établissent ce qu'un projet ou un éditeur déclare, pas ce qu'un tiers a constaté.

MCP et A2A décrivent des messages. Ils ne disent pas qui, dans une organisation donnée, a le droit de les envoyer, combien de fois, ni ce qu'il faut en conserver. La spécification MCP rend l'autorisation facultative, recommande la validation humaine sans l'imposer et ne définit pas le comportement d'une passerelle (chapitre 5). Chaque hôte, chaque serveur et chaque équipe peut donc appliquer sa propre règle, ou aucune.

La passerelle est la réponse d'architecture à ce vide : un point de passage obligé, sur le chemin de chaque appel, où la politique de l'entreprise s'applique de la même façon quels que soient l'agent et l'outil. Le chapitre 23 l'a située dans le plan de données, sous l'autorité du plan de contrôle.

Une passerelle MCP n'est pas une passerelle d'API dotée d'un protocole de plus : elle doit lire un catalogue d'outils et des réponses destinées à un modèle. Ses contrôles se ramènent à cinq, et aucun ne vaut si un agent peut la contourner. Enfin, aucune évaluation indépendante ne départage les produits : le choix repose sur des propriétés que l'entreprise vérifie elle-même.

---

## 24.1 De la passerelle d'API à la passerelle MCP

### Ce qui se transpose

Une passerelle d'API authentifie l'appelant, applique des quotas, route la requête et la journalise. Tout cela reste nécessaire devant un serveur MCP. Dans Apigee, un point d'accès MCP est un proxy comme un autre, qui hérite d'OAuth 2.0, d'OpenID Connect, de la vérification de clés et des politiques existantes [6]. Dans Azure API Management, les politiques habituelles s'attachent au serveur MCP, après celles de portée globale [7].

### Ce qui ne se transpose pas

Quatre propriétés du trafic agentique mettent ce modèle en défaut.

**L'opération n'est pas dans l'URL.** Une API REST expose une route par opération; une passerelle classique décide sur le chemin et la méthode HTTP. Un serveur MCP reçoit tous ses appels sur un même chemin, et le nom de l'outil est dans le corps JSON-RPC. Apigee reçoit ainsi tous les appels sur `/mcp` et étiquette chaque requête du nom de l'outil invoqué [6]. La révision `2026-07-28` de MCP répond au même problème en recopiant la méthode et le nom de l'outil dans des en-têtes. Une politique fondée sur ces en-têtes suppose que le serveur rejette tout écart avec le corps et que la passerelle refuse les requêtes d'une version antérieure (chapitre 5).

**La réponse est un flux adressé à un modèle.** Le résultat d'un outil entre dans le contexte d'un modèle de langage; il peut porter une instruction injectée ou une donnée qui ne devrait pas sortir. L'inspecter suppose de le lire, ce qui se heurte au transport. La documentation d'Azure API Management déconseille de lire le corps de la réponse dans une politique de serveur MCP, car la mise en tampon perturbe la diffusion en flux et peut faire échouer le serveur; elle demande aussi de ne pas journaliser ce corps à la portée globale [7]. Inspection des réponses et diffusion en flux ne vont donc pas de soi ensemble.

**Le catalogue est lui-même une surface d'attaque.** La description d'un outil est du texte que le modèle lit avant de choisir. Une passerelle qui ne regarde que les appels laisse passer une description empoisonnée (chapitre 31). Le brouillon de Microsoft prévoit pour cette raison un balayage des définitions d'outils, distinct de l'interception des appels [4].

**La découverte dépend de l'appelant.** Filtrer `tools/list` selon les droits de l'agent réduit à la fois le risque et la taille du contexte. Apigee ne renvoie dans `tools/list` que les outils du produit d'API auquel le client est abonné [6]. agentgateway désactive la mise en cache des réponses qu'il relaie, dont `server/discover` et `tools/list`, parce que ses politiques peuvent les rendre propres à chaque requête [3]. Le mécanisme de cache introduit par la révision de juillet (chapitre 5) perd donc de son effet derrière une passerelle qui filtre.

### Trois familles

| Famille | Produits lus | Point de départ | Apport propre |
|---|---|---|---|
| Gestion d'API étendue | Apigee, Azure API Management, Kong | Un parc d'API déjà gouverné | Politiques existantes appliquées aux outils; conversion d'API en outils |
| Passerelle agentique dédiée | agentgateway, Agent Router | Le trafic des agents | Inférence et MCP sur un même plan de données, A2A aussi chez agentgateway; fédération de serveurs |
| iPaaS agentique | MuleSoft Agent Fabric | Un parc d'intégrations | Registre, détection sur d'autres plateformes, courtier |

Ces familles se recouvrent; elles diffèrent surtout par ce que l'entreprise possède déjà.

Une quatrième offre recoupe ces familles : la passerelle gérée par un fournisseur infonuagique. Amazon Bedrock AgentCore Gateway se décrit comme un point d'entrée unique pour le trafic agentique, vers les outils, les autres agents et les modèles [13]. Il convertit en outils MCP des API décrites en OpenAPI ou en Smithy et des fonctions Lambda, relaie d'autres agents, A2A compris, et route l'inférence entre fournisseurs de modèles. Il prend en charge l'authentification entrante de l'agent et l'authentification sortante vers chaque outil, avec injection des justificatifs. Sa recherche sémantique d'outils répond au catalogue trop gros (section 24.3) : l'agent cherche parmi les outils disponibles au lieu de les charger tous. La page lue est une présentation; les règles et le contrôle d'accès fin, décrits ailleurs dans la documentation, n'ont pas été lus.

---

## 24.2 Cinq contrôles par appel d'outil

Le brouillon « MCP Security Gateway 1.0 », publié dans l'Agent Governance Toolkit de Microsoft, donne la description la plus détaillée d'un pipeline de passerelle parmi les textes lus [4]. La passerelle travaille en deux temps : interception de l'appel avant sa transmission, puis balayage de la réponse avant son retour à l'agent. L'interception évalue, dans cet ordre, la liste de refus, la liste d'autorisation, le caractère sensible de l'outil et le budget de débit.

Rapproché de la documentation des produits, ce pipeline se ramène à cinq contrôles.

![Les cinq contrôles qu'une passerelle applique à un appel d'outil : l'appel traverse les cinq avant d'atteindre l'outil, et la réponse repasse par l'inspection avant son retour à l'agent. Le regroupement en cinq contrôles est une grille de lecture tirée du brouillon de Microsoft et de la documentation des produits, pas un résultat éprouvé.](figures/fig-24-e1.svg)

| Contrôle | Question posée | Décision typique |
|---|---|---|
| 1. Identité | Qui appelle, et ce jeton est-il émis pour ce destinataire ? | Rejet si le jeton est absent ou d'une autre audience |
| 2. Autorisation par outil | Cet appelant peut-il voir et invoquer cet outil ? | Liste, rôle ou règle; découverte filtrée |
| 3. Approbation | Cet appel exige-t-il un accord humain ? | Suspension jusqu'à décision |
| 4. Quota et budget | L'appelant a-t-il épuisé son débit ou son enveloppe ? | Refus jusqu'à la fenêtre suivante |
| 5. Inspection des contenus | Que contiennent les arguments, la réponse et la définition de l'outil ? | Blocage, expurgation ou simple signalement |

### Identité

La passerelle termine la connexion MCP : pour le client, elle est le serveur, et la règle du protocole s'applique à elle : un serveur MCP ne doit accepter aucun jeton qui n'a pas été émis explicitement pour lui, et le relais d'un jeton vers l'aval est interdit [10]. La passerelle doit se présenter aux systèmes qu'elle protège avec un justificatif distinct, obtenu par échange de jeton ou détenu en propre (chapitre 30). Azure API Management l'illustre : son dépannage attribue une erreur 401 de l'arrière-plan à l'en-tête d'autorisation non transmis, et propose d'attacher un jeton par politique [7].

Une passerelle qui sert d'intermédiaire OAuth vers une API tierce avec un identifiant client statique entre dans le cas du délégué confus décrit par la spécification : elle doit obtenir un consentement par client avant de lancer le flux tiers [10]. Vers l'aval, le brouillon de Microsoft refuse par défaut un serveur sans authentification et exige TLS [4].

### Autorisation par outil

L'unité de décision est l'outil, pas le serveur. Dans le brouillon, la liste de refus prime la liste d'autorisation, et une liste d'autorisation non vide exclut tout ce qu'elle ne nomme pas; vide, elle laisse tout passer [4], piège relevé au chapitre 30. Apigee regroupe les opérations permises dans un produit d'API [6]; agentgateway exprime l'accès aux outils et aux ressources par des règles CEL [2]; Kong annonce des contrôles d'accès par outil [9]. C'est ici que le registre devient contraignant : la passerelle refuse tout appel vers un serveur que le registre n'a pas approuvé, et un retrait du registre doit la couper (chapitre 8).

### Approbation

Les outils déclarés sensibles déclenchent un rappel d'approbation qui renvoie trois états : approuvé, refusé, en attente. Seul le premier laisse passer l'appel, et l'absence de rappel configuré vaut refus [4]. La passerelle ne décide pas quelles actions méritent un humain (chapitre 22); elle garantit que la règle ne dépend pas de la bonne volonté de l'hôte. Ce modèle est synchrone : une approbation qui prend des heures appelle plutôt l'extension Tasks de MCP (chapitre 5).

### Quota et budget

Le brouillon tient un budget d'appels par agent sur une fenêtre glissante, par défaut 100 appels par 300 secondes, et normalise l'identifiant d'agent pour qu'une variation de casse ou d'espaces ne contourne pas le compteur [4]. Apigee permet un quota par outil [6]. L'exemple donné par Azure limite le débit par adresse IP [7], clé peu adaptée quand de nombreux agents sortent par la même plateforme : le compteur devrait porter sur l'identité de l'agent (chapitre 29). Les plafonds budgétaires d'agentgateway [1] et la gestion de budgets de MuleSoft [8] étendent le contrôle au coût, traité au chapitre 40.

### Inspection des contenus

Le balayage des réponses cherche cinq catégories de menaces : balises d'instruction, injonctions en langage naturel, fuites de justificatifs, fuites de renseignements personnels et URL d'exfiltration. Trois politiques sont possibles : bloquer (par défaut), expurger ou journaliser [4].

Le balayage des définitions vise les instructions cachées, l'injection dans les descriptions, l'abus de schéma et les attaques entre serveurs. Un nom d'outil à une distance de Levenshtein de 2 au plus d'un outil enregistré sur un autre serveur est signalé comme tentative d'usurpation. Et une empreinte SHA-256 de la description et du schéma est conservée : tout écart ultérieur doit produire une alerte critique, ce qui détecte la substitution d'un outil après son approbation [4].

Sans configuration propre, le scanner emploie des motifs d'exemple et devrait en avertir [4] : la détection ne vaut que par ses règles, et aucune mesure d'efficacité n'accompagne le brouillon.

### Deux propriétés transversales

**Chaque décision laisse une trace.** Le brouillon exige un enregistrement d'audit pour toute décision, qu'elle autorise, refuse ou expurge [4]. Kong journalise la méthode JSON-RPC, la charge utile, la latence et les erreurs [9]. Journaliser les charges utiles y déplace toutefois des données sensibles (chapitre 33).

**Une erreur vaut refus.** Le premier principe du brouillon est l'échec fermé : tout composant refuse en cas d'erreur [4]. Encore faut-il voir le refus. Dans agentgateway, un appel d'outil rejeté par un garde-fou ou une limite de débit revient avec un code HTTP 200 et un résultat marqué en erreur [3]. Une surveillance fondée sur les codes HTTP ne compte donc pas ces refus.

### Portée de ces textes

Le brouillon de Microsoft, au statut « Draft » et daté du 28 juillet 2025, spécifie une boîte à outils et vise ses propres SDK [4] : ce n'est pas une norme sectorielle. Le cadre de Narajala et Habler (prépublication, 2025) recommande pare-feu applicatifs et passerelles d'API devant le trafic MCP, ainsi que la validation et la signature des descriptions d'outils; sa validation est conceptuelle, sans mesure expérimentale [5]. Les cinq contrôles sont une grille de lecture, pas un résultat éprouvé.

---

## 24.3 Transformer les API existantes en outils

Les éditeurs de gestion d'API promettent d'exposer comme outils des API déjà décrites, sécurisées et surveillées, sans écrire de serveur MCP.

| Produit | Mécanisme | Limites déclarées |
|---|---|---|
| Apigee | Un proxy de découverte MCP créé à partir d'une spécification OpenAPI 3.0.x; chaque opération devient un outil [6] | MCP désactivé par défaut; dans Apigee hybrid, version 1.17.0 ou ultérieure, organisations Subscription et Evaluation |
| Azure API Management | Une API REST gérée est exposée comme serveur MCP distant; les opérations à exposer se choisissent une à une [7] | Outils seulement, ni ressources ni prompts; non offert dans les espaces de travail |
| Kong | Un module convertit des schémas d'API en définitions d'outils et agrège plusieurs API derrière un point d'accès [9] | Non précisées sur la page lue |
| MuleSoft | MCP Bridge; prise en charge d'OpenAPI 3.1 et 3.2 depuis le 9 novembre 2026, schémas de sortie depuis le 31 août [8] | Statut de disponibilité non indiqué |

Dans Apigee hybrid, le plan de données MCP s'exécute dans la grappe Kubernetes du client, et le trafic des requêtes n'en sort pas [6], propriété qui compte pour la résidence des données (chapitre 37).

### La conversion mécanique ne suffit pas

Qu'une opération devienne un outil est une équivalence syntaxique. Quatre écarts subsistent.

**Une description d'API s'adresse à un développeur.** Le modèle choisit un outil d'après sa description (chapitre 5). Un résumé d'opération écrit pour une documentation de référence ne dit pas quand appeler l'outil ni quand s'en abstenir.

**Le catalogue grossit vite.** Une API convertie en entier charge dans le contexte autant de définitions que d'opérations, ce qui pèse sur le coût et sur le choix de l'outil (chapitre 13).

**La politique s'applique au serveur.** Dans Azure API Management, les politiques d'un serveur MCP valent pour tous les outils qu'il expose [7]. Traiter différemment lecture et écriture conduit alors à découper l'API en plusieurs serveurs.

**Un outil peut être réémis.** Depuis la révision sans état, le client réémet une requête dont le flux s'est rompu (chapitre 5). Une opération d'écriture non idempotente devient un risque dès qu'un agent l'invoque (chapitre 18).

D'où une curation : exposer d'abord les lectures, choisir les opérations une à une, réécrire les descriptions pour le modèle et regrouper au besoin plusieurs opérations en un outil de niveau métier. L'encapsulation des systèmes patrimoniaux est traitée au chapitre 25.

---

## 24.4 L'iPaaS agentique

Les plateformes d'intégration possèdent déjà des connecteurs vers les systèmes d'enregistrement et un catalogue de ce qui est branché. Les notes de version de MuleSoft Agent Fabric, lues jusqu'au 9 novembre 2026, montrent quatre fonctions au-dessus de la passerelle [8].

| Fonction | Contenu d'après les notes de version | Renvoi |
|---|---|---|
| Registre | Découverte des agents et des serveurs MCP dans Exchange (octobre 2025) | Chapitre 8 |
| Scanners | Détection sur Amazon Bedrock, Google Vertex AI et Microsoft Azure Copilot (janvier 2026), puis des agents de ServiceNow et des serveurs MCP de Kong Gateway (octobre 2026) | Chapitre 8 |
| Politiques des autres passerelles | Relevé dans Apigee, Azure API Management et Kong Gateway, politiques ouvertes appliquées aux API (août 2026); pas aux agents ni serveurs MCP tiers (octobre 2026) | Chapitre 27 |
| Courtier | Agent brokers, service de routage contextuel (octobre 2025); réseaux d'agents avec orchestration par graphe et A2A v1.0 (juillet 2026) | Chapitres 16 et 20 |

Les scanners d'API relèvent, API par API, les politiques de ces plateformes (les notes disent « write policies from »), sans les écrire. Les politiques ouvertes se traduisent en politiques natives des passerelles prises en charge, dont Amazon API Gateway, sur les instances d'API; la note du 14 octobre retire l'onglet des politiques des agents et serveurs MCP gérés par une passerelle tierce, faute d'application possible [8]. L'iPaaS agentique vise le plan de contrôle d'un plan de données hétérogène (chapitre 23), mais ne l'exerce encore que sur les API (chapitre 27).

Les notes n'indiquent aucun statut de disponibilité, hormis l'offre dans les régions infonuagiques du Canada et du Japon depuis avril 2026 [8]. L'orchestration s'écrit dans un format propre à l'éditeur, ce qui engage la portabilité, et un scanner ne voit que les plateformes qu'il interroge.

---

## 24.5 Routage et passerelles ouvertes

### Deux projets sous gouvernance neutre

L'Agentic AI Foundation héberge deux passerelles parmi ses dix projets [11].

**agentgateway** se présente comme un plan de données unifié pour le trafic MCP, A2A, d'inférence, HTTP et gRPC. Son billet d'entrée à la fondation énumère authentification par JWT ou clé d'API, contrôle d'accès par rôle, mTLS, limitation de débit, filtres de prompts et plafonds budgétaires. La configuration se met à jour par xDS sans interruption. Le projet est écrit en Rust, sous licence Apache 2.0; il revendique plus de 300 contributeurs actifs dans plus de 60 organisations [1].

**Agent Router** est décrit par la fondation comme une passerelle d'IA à code source ouvert, bâtie sur Envoy, qui relie des applications à des modèles et à des outils MCP [11]. C'est l'ancien Envoy AI Gateway, renommé [12]. Son README route vers des fournisseurs hébergés, de l'inférence autohébergée et des serveurs MCP; il ne mentionne ni A2A ni fédération de serveurs MCP [12].

La page de la fondation n'attribue aucun stade de maturité à ces projets [11]. L'hébergement règle la question de la neutralité, pas celle de l'aptitude à la production.

### Trois objets de routage

Une passerelle agentique route vers trois destinations. Vers les **modèles**, elle choisit le fournisseur d'inférence [1] : choix du modèle traité au chapitre 44, sujet d'économie (chapitre 40) et voie de bascule en cas de panne (chapitre 46). Vers les **agents**, elle relaie A2A (chapitre 6). Vers les **outils**, elle fait davantage que router : elle fédère.

### La fédération de serveurs

agentgateway regroupe plusieurs serveurs MCP derrière un point d'accès, sous la forme d'un serveur virtuel assorti de politiques par outil [1][2]. Sa documentation de compatibilité décrit ce que cela exige [3].

- **Traduire les versions.** La passerelle prend en charge la révision sans état `2026-07-28` et continue d'accepter le flux `initialize`; un client récent devant un serveur ancien se rabat sur l'ancien flux, ce que la passerelle gère. Les versions antérieures sont dites fonctionner en général, sans garantie.
- **Trouver un dénominateur commun.** Quand un point d'accès fédère plusieurs serveurs, la passerelle retient l'intersection des versions que tous peuvent servir. Un seul serveur ancien fixe le niveau de l'ensemble.
- **Recomposer les listes.** La pagination s'appuie sur un curseur combiné et chiffré, que le client doit renvoyer tel quel.
- **Préfixer les noms.** Le préfixage des noms d'outils est configurable; il règle la collision que le protocole laisse au client (chapitre 5).

La fédération déplace une garantie. Dans MCP, un serveur ne voit pas les autres, et l'hôte maintient cette isolation (chapitre 5). Derrière un serveur virtuel, l'hôte ne voit plus qu'un serveur : la séparation entre outils d'origines différentes repose sur la passerelle. Raison de plus d'y examiner les définitions d'outils, noms voisins compris (24.2).

### Premières mesures

Trois sources chiffrent quelque chose. Aucune ne suffit à départager les produits.

**Un banc de cabinet d'analyse.** AIMultiple a mesuré six passerelles MCP devant un serveur factice de seize outils, avec un client déterministe, sans modèle [14]. Le surcoût médian d'un appel relayé va de 0,84 ms à 23 ms pour les trois passerelles autohébergées mesurées. Les deux passerelles hébergées, jointes par le réseau étendu, affichent 55,5 ms et 211,1 ms, délais de réseau compris. Activer les contrôles de contenu ajoute 11,5 % chez l'une et fait passer une autre de 55,5 ms à 172,1 ms. Sur 60 injections placées dans des réponses d'outils, une passerelle en arrête 60 et une autre 55; les quatre autres laissent l'instruction atteindre le client. Quatre produits sur six appliquent une autorisation par outil, trois livrent leurs contrôles de contenu désactivés, et deux ne journalisent pas les appels bloqués.

Le banc ne teste ni le contournement de la passerelle ni le comportement d'un modèle, n'emploie que deux formes d'injection, et ses auteurs précisent qu'il n'établit pas de classement. L'un des éditeurs testés est client du cabinet pour ses services de mesure, ce que la page déclare [14].

**Un filtre évalué par ses auteurs.** MCP-Guard, mandataire à trois étages (motifs, détecteur neuronal, arbitrage par un modèle), rapporte un score F1 moyen de 89,1 % et une latence moyenne de 455,9 ms sur huit modèles d'arbitrage, soit environ la moitié de celle d'un modèle employé seul [15]. L'évaluation est faite hors ligne, sur un jeu de 70 448 échantillons composé à 97 % d'instructions de débridage. Le dispositif n'a pas été placé devant de vrais serveurs, et les auteurs jugent sa latence trop élevée pour certains usages.

**Des scanners qui se contredisent.** Sur une collection de 64 611 serveurs, les scanners existants signalent 96,89 % des serveurs comme risqués, et moins de la moitié des alertes vérifiées à la main sont fondées [16]. Le balayage des définitions d'outils (section 24.2) hérite de cette limite (chapitre 8).

### Ce qui manque

Aucune de ces mesures ne porte sur les passerelles décrites dans ce chapitre, ni sur une charge de production. La faible latence mise en avant par agentgateway reste une déclaration du projet [1]. Le cadre de Narajala et Habler range lui-même le surcoût de performance de l'inspection parmi ses limites [5].

---

## 24.6 Critères de choix

Faute de mesure comparative probante (section 24.5), le choix repose sur des questions dont la réponse se vérifie dans une documentation ou par un essai.

| Critère | Question vérifiable |
|---|---|
| Couverture | Quelles révisions de MCP, avec ou sans état ? A2A et inférence sur le même plan ? |
| Granularité | La politique se pose-t-elle par outil, ou seulement par serveur ? |
| Découverte | `tools/list` est-il filtré selon l'appelant ? |
| Identité | L'audience du jeton est-elle validée ? Comment la passerelle s'authentifie-t-elle en aval ? |
| Inspection | Les réponses sont-elles lues sans rompre le flux ? Les définitions sont-elles balayées ? |
| Défaillance | Une erreur vaut-elle refus ? Sous quelle forme le refus est-il signalé ? |
| Audit | Toute décision est-elle tracée et exportable ? Où vont les charges utiles ? |
| Réglages d'origine | Les contrôles de contenu sont-ils actifs sans configuration ? Les refus sont-ils journalisés ? |
| Registre | Une entrée retirée du registre cesse-t-elle d'être joignable ? |
| Emplacement | Où s'exécute le plan de données ? |
| Gouvernance | Licence, fondation hôte, format des politiques |

Trois essais valent mieux qu'une fiche de produit : soumettre à la passerelle un jeu de descriptions d'outils piégées et compter ce qu'elle arrête; mesurer la latence ajoutée sous la charge réelle; tenter de joindre un serveur sans passer par elle.

Ce dernier essai fixe la limite du dispositif. Une passerelle réseau ne voit ni les serveurs locaux lancés sur un poste par stdio, que la spécification traite comme une surface d'attaque distincte [10], ni l'agent qui détient un justificatif direct vers un système. Elle ne gouverne que si la politique réseau interdit les autres chemins. Elle juge en outre les appels un à un : une suite d'appels tous permis peut former une trajectoire qui ne l'est pas (chapitre 32).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Point d'application | Passerelle sur le chemin de tout appel à un serveur distant | Outil local sans donnée sensible, sous politique du poste |
| Famille de produit | Étendre la gestion d'API déjà en place | Trafic A2A et d'inférence à unifier : passerelle agentique dédiée |
| Unité de politique | L'outil | Serveur interne homogène, en lecture seule |
| Jeton en aval | Échange de jeton ou justificatif propre à la passerelle; jamais de relais | — |
| Outils sensibles | Approbation à la passerelle; refus sans approbateur configuré | Délai long : extension Tasks (chapitres 5 et 22) |
| Clé de quota | Identité de l'agent | Adresse IP si l'identité est indisponible |
| Réponses | Balayage avec blocage par défaut | Expurgation, après mesure des faux positifs |
| Définitions d'outils | Balayage à l'inscription, empreinte suivie ensuite | — |
| Erreur de la passerelle | Refus | — |
| API existantes | Conversion suivie d'une curation, lectures d'abord | Prototype interne : conversion intégrale |
| Réglages d'origine | Vérifier que les contrôles de contenu sont activés et que les refus sont journalisés | — |

---

## Points à retenir

- Les protocoles laissent ouvert le comportement d'une passerelle. C'est là que l'entreprise rend obligatoire ce que MCP recommande.
- Une passerelle MCP diffère d'une passerelle d'API sur quatre points : l'opération est dans le corps, la réponse est un flux lu par un modèle, le catalogue est une surface d'attaque et la découverte dépend de l'appelant.
- Cinq contrôles s'appliquent à chaque appel : identité, autorisation par outil, approbation, quota, inspection des contenus. L'audit et l'échec fermé valent pour les cinq.
- La passerelle ne relaie jamais le jeton reçu. Elle se présente en aval avec un justificatif distinct.
- Convertir une API en outils est mécanique; la rendre utilisable par un modèle demande une curation des opérations et des descriptions.
- L'iPaaS agentique vise le plan de contrôle : MuleSoft applique des politiques aux API d'autres passerelles, pas encore aux agents ni aux serveurs MCP.
- La fédération de serveurs transfère à la passerelle l'isolation que l'hôte assurait.
- Les premières mesures sont minces : un banc de cabinet d'analyse sur six passerelles, dont aucune n'est décrite ici, un filtre évalué par ses auteurs, et des scanners qui se contredisent. Le brouillon de Microsoft et le cadre universitaire cité restent des propositions.
- Une passerelle contournable ne gouverne rien : serveurs locaux et justificatifs directs lui échappent.

---

## Sources

Pages primaires lues le 11 novembre 2026, sauf [12], lue le 12 :

1. [agentgateway — entrée à l'Agentic AI Foundation](https://agentgateway.dev/blog/2026-06-04-agentgateway-joins-aaif/) — billet du projet.
2. [agentgateway — documentation MCP](https://agentgateway.dev/docs/standalone/latest/mcp/)
3. [agentgateway — compatibilité avec les révisions de MCP](https://agentgateway.dev/docs/standalone/latest/documentation/mcp/spec-compatibility/)
4. [Microsoft, Agent Governance Toolkit — MCP Security Gateway 1.0 (brouillon)](https://microsoft.github.io/agent-governance-toolkit/specs/MCP-SECURITY-GATEWAY-1.0/)
5. [Narajala et Habler — Enterprise-Grade Security for the Model Context Protocol (arXiv 2504.08623v2)](https://arxiv.org/html/2504.08623v2) — prépublication.
6. [Google — MCP dans Apigee hybrid](https://developers.googleblog.com/announcing-mcp-support-in-apigee-hybrid-agentic-tools-that-run-in-your-own-cluster/) — billet de l'éditeur, 14 octobre 2026.
7. [Microsoft Learn — exposer une API REST comme serveur MCP dans Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
8. [MuleSoft Agent Fabric — notes de version](https://docs.mulesoft.com/general/agent-fabric-release-notes)
9. [Kong — MCP dans Kong AI Gateway](https://developer.konghq.com/mcp/)
10. [MCP — bonnes pratiques de sécurité, spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices.md)
11. [Agentic AI Foundation — projets](https://aaif.io/projects)
12. [Agent Router — README du dépôt](https://github.com/theagentrouter/agent-router)

Sources ajoutées le 14 novembre 2026 :

13. [AWS — Amazon Bedrock AgentCore Gateway, guide du développeur](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) — page de présentation.
14. [AIMultiple — banc d'essai de passerelles MCP (page mise à jour le 9 novembre 2026)](https://aimultiple.com/de/mcp-gateway) — banc d'un cabinet d'analyse; version allemande lue.
15. [MCP-Guard: A Multi-Stage Defense-in-Depth Framework for Securing Model Context Protocol in Agentic AI (arXiv 2508.10991, version 4 du 8 janvier 2026)](https://arxiv.org/html/2508.10991v4) — prépublication.
16. [Chen et coll. — Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability (arXiv 2607.11086, 13 juillet 2026)](https://arxiv.org/abs/2607.11086) — prépublication; résumé seulement.

Sources secondaires : aucune n'est citée.

## Limites de ce chapitre

- Les pages ont été lues par un outil qui en restitue un résumé. L'audit du 12 novembre a relu [3], [4] (ses 100 000 premiers caractères), [6], [7], [8], [10] et [11], et lu [12] : les faits cités y sont confirmés, sauf trois points sur MuleSoft (24.4). La date du brouillon, 28 juillet 2025, est celle que porte la page.
- Que les scanners de MuleSoft relèvent les politiques sans les écrire est une interprétation des notes, qui ne le disent pas explicitement.
- Le découpage en cinq contrôles est une synthèse de ce chapitre; aucun texte lu ne l'énonce tel quel.
- Les fonctions d'une passerelle d'API classique viennent de la connaissance générale. Les remarques sur les descriptions d'API, la taille du catalogue, la clé de quota et l'approbation asynchrone sont des raisonnements.
- [1], [2] et [9], seule page lue sur Kong, n'ont pas été relus. Les pages d'agentgateway sur l'authentification, l'autorisation et les garde-fous n'ont pas été lues.
- D'AWS AgentCore Gateway, seule la page de présentation [13] a été lue. Les autres iPaaS et les passerelles centrées sur l'inférence n'ont pas été lus.
- Les seules données de performance citées viennent des sources [14] à [16], ajoutées le 14 novembre 2026. [14] est le banc d'un cabinet d'analyse dont un des éditeurs testés est client; aucun des produits décrits dans ce chapitre n'y figure. [15] est évalué par ses auteurs, hors ligne. [16] n'est connu que par son résumé. Aucune donnée d'adoption n'est citée, hormis les contributeurs déclarés par agentgateway.
- Le paragraphe sur la passerelle gérée (24.1), la sous-section « Premières mesures » (24.5) et les lignes « Réglages d'origine » du tableau de 24.6 et de la grille datent du 14 novembre 2026.
