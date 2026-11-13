# Divergences entre exposés et volets « Mise en œuvre »

Relevé produit en novembre 2026 par les agents qui ont réécrit les volets, puis traité par une seconde passe d'alignement : 142 divergences dans 31 volets. L'exposé de référence, sourcé et audité, fait foi. Chaque divergence a été revérifiée dans les deux textes avant traitement; ni le relevé ni les traitements n'ont été relus un à un par une personne.

Traitements appliqués :

- **corrigé** (73) : le volet reprend le fait, la date, le terme ou le statut de l'exposé;
- **nuance** (38) : la prescription du volet est gardée, avec une phrase disant qu'elle va au-delà de ce que retient l'exposé;
- **avertissement** (16) : un extrait de code, une figure ou un titre intouchable est précédé d'une phrase qui dit ce que l'exposé indique à la place;
- **relevé inexact** (7) : après vérification, le volet ne contredit pas l'exposé; rien n'a changé;
- **laissé** (4) : chiffres ou faits du cas fictif du Groupe Boréal;
- **sans objet** (4) : le passage avait déjà été retiré à la réécriture.

Les remarques de fin de volet signalent ce qui reste : contradictions internes que l'exposé ne tranche pas, affirmations sans source dans l'exposé, détails de code d'une version antérieure.

## Chapitre 1 — L'entreprise agentique

### Volet « De l'assistance conversationnelle à la main-d'œuvre d'exécution asynchrone »

- **Un agent ou plusieurs; solution la plus simple** — *nuance*
  - Exposé : Section 1.1 (recommandation d'Anthropic) et grille de décision : commencer simple, un seul agent par défaut; section 1.5 : sur six bancs d'essai, l'écart moyen entre multi-agents et agent unique est à peu près nul.
  - Volet, avant alignement : Synthèse exécutive, section 1.7 et ADR-001 : séparation obligatoire en cinq archétypes dès le jour 1, interdiction du « super-agent » universel; tout système de niveau L2 à L4 doit s'y conformer.
  - Traitement : Relevé confirmé : l'exposé garde un seul agent par défaut (section 1.1, grille de décision), le volet impose cinq archétypes dès le jour 1. La règle est conservée et une phrase dit qu'elle va au-delà de l'exposé dans trois passages : synthèse exécutive (point 2), fin de l'intro de la section 1.7 (avec l'écart à peu près nul sur six bancs d'essai, section 1.5), et phrase d'introduction avant l'ADR-001.
- **Échelle et niveau d'autonomie** — *nuance*
  - Exposé : Section 1.3 : trois échelles (Feng L1 à L5, Singapour à quatre niveaux, CSA de 0 à 5, où L3 de Feng est « consultant » et 3 de la CSA « conditionnelle »); le niveau se fixe par agent et par classe d'action.
  - Volet, avant alignement : Échelle propre L0 à L4 où L3 correspond à la supervision sur exception (HOTL) et L2 à l'approbation préalable; la liste de contrôle classe chaque cas d'usage selon le maillon le plus élevé de la chaîne.
  - Traitement : Relevé confirmé : un paragraphe ajouté avant le tableau des archétypes précise que L0 à L4 est l'échelle propre au volet (L2 approbation préalable, L3 HOTL) et que ses numéros ne se transposent pas aux trois échelles de l'exposé (L3 « consultant » chez Feng et coll., 3 « conditionnelle » chez la CSA, section 1.3); le point 1 de la liste de contrôle reçoit une phrase disant que la règle du maillon le plus élevé va au-delà de l'exposé, qui fixe le niveau par agent et par classe d'action (section 1.3).
- **Agent appelé comme un outil** — *nuance*
  - Exposé : Section 1.1 (cadre de Singapour) : un agent superviseur appelle un agent spécialisé comme il appellerait un outil.
  - Volet, avant alignement : Loi 2 : exposer un agent autonome comme un « outil MCP » est une confusion; la délégation entre pairs relève d'A2A.
  - Traitement : Relevé confirmé : la Loi 2 est conservée, et un paragraphe ajouté après ses deux puces rappelle que, selon le cadre de Singapour, un agent superviseur appelle un agent spécialisé comme il appellerait un outil (section 1.1), et que la délégation à un agent qu'on ne contrôle pas est l'objet d'A2A (chapitre 6).
- **Preuve de production de MCP, A2A et du multi-agents** — *laissé*
  - Exposé : Section 1.5 : aucun cas documenté ne montre MCP, A2A ou un système multi-agents en production (chapitre 42).
  - Volet, avant alignement : Encadré du fil rouge : résultats mesurés sur 60 jours de production pilote, avec MCP, A2A et plusieurs agents.
  - Traitement : Rien modifié : les 60 jours de production pilote, MCP, A2A et plusieurs agents appartiennent au cas fictif du Groupe Boréal (encadré fil rouge, section 1.10), qui ne contient aucune affirmation générale sur le monde réel.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (6469 -> 6434 mots). Les quatre divergences du relevé étaient exactes; aucun code, figure, formule, titre d'extrait ni titre d'ADR n'a été touché, et la liste de contrôle garde huit points. Hors relevé et non traités : la boîte « Éditeurs SaaS B2B » (section 1.8) dit qu'une plateforme moderne « expose désormais » un serveur MCP et une façade A2A, ce que l'exposé (section 1.5, aucun cas documenté en production) ne confirme pas; les chiffres et « études en facteurs humains » de la section 1.9 et le récit des limites de la génération 2 en production (section 1.6) ne viennent pas non plus de l'exposé. Les contradictions internes signalées (révision semestrielle ou annuelle de l'ADR, « cinq à douze » ou « moins de douze » outils, 1,20 ou 1,50 $ CAD, Logistique ou Stocks) sont laissées, l'exposé ne les tranchant pas.

## Chapitre 5 — MCP : le protocole agent-outil

### Volet « Connectivité verticale : outils, ressources, compétences et web »

- **Version du protocole, poignée de main et session** — *avertissement*
  - Exposé : Sections 5.1, 5.2 et grille de décision : la version cible est `2026-07-28` pour tout nouveau serveur distant; la poignée de main `initialize` et l'en-tête `Mcp-Session-Id` sont supprimés, version et capacités voyagent dans chaque requête et la découverte passe par `server/discover`.
  - Volet, avant alignement : L'Extrait 5.1 montre `MCP-Protocol-Version: 2025-06-18`, une requête `initialize`, la réponse `InitializeResult` et `notifications/initialized`; l'encadré Tip parle encore de Mcp-Session-Id. Conservé tel quel (code intouchable).
  - Traitement : Extrait 5.1 intact; la phrase d'introduction dit qu'il suit le protocole d'avant la révision `2026-07-28` et rappelle que `initialize` est supprimée, que version et capacités voyagent dans chaque requête et que la découverte passe par `server/discover` (sections 5.1 et 5.2), avec « Dans cet échange » devant le commentaire de la réponse; l'encadré Tip est de plus corrigé (session et Mcp-Session-Id supprimés, état par identifiants explicites, section 5.2).
- **Reprise d'un flux interrompu** — *corrigé*
  - Exposé : Section 5.2 : la reprise par `Last-Event-ID` est supprimée; une requête interrompue est réémise avec un nouvel identifiant.
  - Volet, avant alignement : Règles de transport (5.9) : une exécution longue répond en `text/event-stream` « avec reprise par Last-Event-ID ».
  - Traitement : Dans la règle « Streamable HTTP par défaut » (5.9), « avec reprise par Last-Event-ID » est remplacé par : flux SSE limité à la requête (section 5.3), reprise supprimée et requête interrompue réémise avec un nouvel identifiant (section 5.2).
- **Échantillonnage (sampling) et racines (roots)** — *nuance*
  - Exposé : Section 5.1 : les deux mécanismes sont dépréciés depuis la révision de juillet 2026; une nouvelle mise en œuvre ne devrait pas les adopter (substituts : paramètres d'outil, appel direct de l'API du fournisseur de modèle).
  - Volet, avant alignement : Section 5.10, tableau et point 6 de la liste de contrôle : les présente comme des primitives à exploiter en entreprise, avec garde-fous (contexte isolé, `maxTokens`, vérification `realpath`), sans mention de la dépréciation.
  - Traitement : Deux phrases ajoutées à l'introduction de 5.10 : racines et échantillonnage dépréciés depuis juillet 2026, encore fonctionnels pendant la fenêtre de dépréciation mais à ne pas adopter en nouvelle mise en œuvre (section 5.1), garde-fous conservés pour qui les utilise; mention « dépréciées/déprécié » dans les deux lignes du tableau et point 6 de la liste de contrôle reformulé au conditionnel (« Si l'échantillonnage, déprécié (section 5.1), est encore utilisé… »).
- **Élicitation et requêtes initiées par le serveur** — *corrigé*
  - Exposé : Sections 5.1 et 5.2 : depuis juillet 2026 un serveur ne peut plus envoyer de requête de sa propre initiative; l'élicitation passe par un résultat `input_required` et la réémission de la requête d'origine par le client.
  - Volet, avant alignement : Sections 5.9 et 5.10 : `elicitation/create` et `sampling/createMessage` sont décrits comme des requêtes du serveur vers l'hôte qui suspendent l'appel en cours; `notifications/progress` sur le flux.
  - Traitement : Puce Élicitation de 5.10 reformulée sur le mécanisme de l'exposé (le serveur renvoie `input_required`, le client réémet la requête d'origine, section 5.2), `elicitation/create` retiré de cette puce, de la règle de transport 5.9 et du point 6; `notifications/progress` sur le flux SSE n'était pas en contradiction et est conservé; `sampling/createMessage` reste, couvert par la divergence précédente.
- **Abonnements et notifications de changement de liste** — *corrigé*
  - Exposé : Sections 5.2 et 5.4 : `resources/subscribe` et le flux GET permanent sont remplacés par `subscriptions/listen`, un flux par abonnement explicite.
  - Volet, avant alignement : Section 5.10 : abonnement optionnel par `resources/subscribe`, et blocage à la passerelle des `notifications/tools/list_changed` non scellées.
  - Traitement : Puce Ressources de 5.10 : `resources/subscribe` remplacé par un abonnement par flux `subscriptions/listen` (section 5.4); le blocage à la passerelle des `notifications/tools/list_changed` non scellées est laissé, l'exposé ne contredisant pas cette règle.
- **Passage de jeton et « délégué confus »** — *corrigé*
  - Exposé : Section 5.5 et « Limites de ce chapitre » : le passage de jeton en aval désigne la réutilisation par le serveur du jeton reçu pour appeler une autre API; la mention du délégué confus à propos du non-relais des jetons a été retirée, la spécification désignant ainsi un autre cas (mandataire OAuth à identifiant client statique).
  - Volet, avant alignement : Section 5.9 : appelle « Token Passthrough » l'acceptation d'un jeton dont l'audience ne désigne pas le serveur, et dit que son rejet élimine le risque de « Confused Deputy ». Affirmation conservée, rendue par « délégué confus ».
  - Traitement : Dans la puce de la passerelle (5.9), « (délégué confus) » est retiré, le passage de jeton est défini comme la réutilisation du jeton reçu pour appeler une autre API, et le rejet d'un jeton à mauvaise audience est présenté comme ce qui empêche qu'un jeton émis pour un service serve à en atteindre un autre (section 5.5); l'expression « Token Passthrough » n'apparaissait plus dans le volet.
- **Modèle d'autorisation retenu** — *nuance*
  - Exposé : Section 5.5 et grille de décision : option par défaut = Enterprise-Managed Authorization (ID-JAG) si le fournisseur d'identité et les clients la prennent en charge, sinon flux OAuth de base; DPoP et l'échange de jetons RFC 8693 sont au programme d'un groupe de travail en formation (chantier ouvert).
  - Volet, avant alignement : Synthèse, 5.9, ADR-005 et liste de contrôle : OAuth 2.1 avec échange On-Behalf-Of (RFC 8693) et DPoP imposés à la passerelle comme standard unique; aucune mention de l'extension Enterprise-Managed Authorization.
  - Traitement : Une phrase ajoutée dans la puce de la passerelle (5.9) et une dans la décision 1 de l'ADR-005 : exiger DPoP et l'échange On-Behalf-Of va au-delà de ce que retient la section 5.5 (option par défaut Enterprise-Managed Authorization (ID-JAG) si le fournisseur d'identité et les clients la prennent en charge, sinon flux OAuth de base; DPoP et RFC 8693 au programme d'un groupe de travail en formation); Synthèse, liste de contrôle et fil rouge laissés tels quels.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (5192 mots vers 5275, 102 %). Seul le volet a été modifié (12 lignes). Contradictions internes (plafond d'outils 5 à 12, 12 à 15 et 15; révision semestrielle ou annuelle) laissées : l'exposé ne les tranche pas. Résidus d'avant 2026-07-28 non relevés et non touchés : le second bloc JSON de l'Extrait 5.1 n'a pas de `resultType` (obligatoire selon 5.2), les capacités `roots` et `sampling` du bloc `initialize`, et « mode sans état privilégié » dans l'ADR-005 alors que le protocole est désormais sans état.

## Chapitre 6 — A2A : le protocole agent-agent

### Volet « Coordination horizontale, découverte et réseau inter-agents »

- **Date de la fusion d'ACP** — *sans objet*
  - Exposé : Section 6.1 et 6.5 : fusion annoncée le 29 août 2025.
  - Volet, avant alignement : 6.8 d'origine (passage retiré) : « Fin 2025, les deux initiatives ont fusionné ».
  - Traitement : Le passage « Fin 2025, les deux initiatives ont fusionné » est déjà retiré du volet (aucune occurrence), et le reste du volet ne date pas la fusion; rien n'a changé.
- **Maturité de production d'A2A** — *corrigé*
  - Exposé : Section 6.7 : des déploiements en production sont affirmés sans qu'aucune organisation soit nommée, et les sources ne permettent pas de mesurer l'usage réel.
  - Volet, avant alignement : 6.8 d'origine (passage retiré) : spécification « généralisée en production en 2027 »; le tableau de 6.11 donne A2A comme standard industriel (Maturité 2027).
  - Traitement : Le passage « généralisée en production en 2027 » est déjà retiré; dans le tableau de 6.11, la cellule « Standard industriel (LF / AAIF) » est remplacée par ce que l'exposé établit : spécification 1.0 stable, protocole par défaut dans l'écosystème ouvert d'origine occidentale (sections 6.4 et 6.5), usage en production affirmé sans organisation nommée (section 6.7).
- **Noms des états de tâche** — *corrigé*
  - Exposé : Section 6.2 : états préfixés `TASK_STATE_` et écrits en majuscules (`INPUT_REQUIRED`, `AUTH_REQUIRED`), valeurs corrigées en 1.0.1 (6.4).
  - Volet, avant alignement : États en minuscules avec tiret (`input-required`, `auth-required`), y compris dans l'Extrait 6.1; conservés tels quels dans le texte.
  - Traitement : Dans le texte et les tableaux de 6.8, les états passent en majuscules à l'abréviation de l'exposé (`SUBMITTED` … `REJECTED`, `INPUT_REQUIRED`, `AUTH_REQUIRED`), avec une phrase sur le préfixe `TASK_STATE_` et les valeurs corrigées en 1.0.1 (sections 6.2 et 6.4), et l'Extrait 6.1 est laissé intact derrière une phrase d'avertissement; ADR-006 (option 1) harmonisé, fil rouge laissé (voir remarques).
- **Noms des opérations et champs de configuration** — *avertissement*
  - Exposé : Sections 6.3 et 6.4 : onze opérations, opérations renommées en 1.0, paramètre `returnImmediately`.
  - Volet, avant alignement : Opérations et champs du style de la version 0.3 : `message/send`, `message/stream`, `tasks/get`, `tasks/cancel`, `tasks/resubscribe`, `blocking: false`, `pushNotificationConfig`, `agent/authenticatedExtendedCard`, `supportsAuthenticatedExtendedCard`.
  - Traitement : L'exposé ne donne aucun nom d'opération de la 1.0 (seulement « onze opérations », « opérations renommées » et `returnImmediately`), donc rien n'est renommé : un paragraphe ajouté à la fin de « Choix de la version 1.0 » liste ces noms et les déclare à vérifier (sections 6.3 et 6.4), et l'avertissement de l'Extrait 6.1 y renvoie.
- **Types de parties** — *corrigé*
  - Exposé : Section 6.4 : types de parties fusionnés en un seul en 1.0; section 6.2 : une partie contient du texte, des octets, une URL ou des données structurées.
  - Volet, avant alignement : Trois types distincts (`TextPart`, `DataPart`, `FilePart`) et un champ `kind` dans l'Extrait 6.1.
  - Traitement : Le point 3 de « Choix de la version 1.0 » décrit maintenant un seul type `Part` (texte, octets, URL ou données structurées; sections 6.2 et 6.4) et le point 5 de la liste de contrôle parle de « parties de données structurées »; l'Extrait 6.1 (champ `kind`) est conservé et couvert par la phrase d'avertissement.
- **Suivi d'une tâche longue** — *nuance*
  - Exposé : Grille de décision : notifications poussées par défaut, interrogation périodique admise si le client ne peut pas recevoir d'appels entrants.
  - Volet, avant alignement : ADR-006 (décision 3) et liste de contrôle (point 3) : notifications poussées obligatoires au-delà de 60 secondes, sans boucle d'interrogation `tasks/get`.
  - Traitement : Les notifications poussées obligatoires au-delà de 60 secondes sont conservées dans la décision 3 de l'ADR-006 et au point 3 de la liste de contrôle, avec une phrase disant que la règle va au-delà de la grille de décision, qui garde les notifications poussées par défaut et admet l'interrogation périodique si le client ne peut pas recevoir d'appels entrants.
- **Structure de l'Agent Card** — *sans objet*
  - Exposé : Section 6.2 : l'Agent Card est décrite à la section 6.2.
  - Volet, avant alignement : 6.8 d'origine renvoie à « la structure présentée au chapitre 1 »; renvoi remplacé par la section 6.2, car le passage est devenu un rappel.
  - Traitement : Le renvoi « structure présentée au chapitre 1 » n'existe plus : le volet renvoie déjà à la section 6.2 (« structure à la section 6.2 »); rien n'a changé.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (5387 mots, 5619 après, 104 %). Deux choix à valider : j'ai laissé les `input-required` du fil rouge (6.12) et de l'Extrait 6.1, par la règle des cas fictifs, ce qui laisse une incohérence de casse avec le reste du volet; et l'affirmation que les noms d'opérations diffèrent de la 1.0 repose sur « opérations renommées » (section 6.4), l'exposé n'en donnant aucun nom. Contradictions internes non touchées, l'exposé ne tranchant pas : flux SSE jusqu'à 3 minutes (T2) contre notifications dès 60 secondes, et vingt fournisseurs (6.11) contre 25 (fil rouge).\n\nPoints hors relevé, non modifiés : « hérité d'ACP » (liaison REST, distinction message/tâche) et « Migré vers la liaison REST d'A2A v1.0 » (tableau 6.8) ne figurent pas dans l'exposé de ce chapitre; les colonnes de maturité AGNTCY (« Production mature », « Production haute sécurité ») et l'encadré sectoriel « En 2027, les chargeurs… 38 heures à 14 minutes » sont des affirmations d'adoption que l'exposé ne couvre pas, et « JSON-RPC reste le profil universel » cadre mal avec l'équivalence des trois liaisons (section 6.4).

## Chapitre 10 — Commerce agentique

### Volet « Interfaces humain-agent, multimodalité temps réel et protocoles transactionnels »

- **Noms et format des mandats AP2** — *corrigé*
  - Exposé : Section 10.2 : la v0.2 définit un Checkout Mandate et un Payment Mandate, chacun ouvert ou fermé, au format SD-JWT.
  - Volet, avant alignement : Section 10.11 : deux preuves, Intent Mandate (sans présence humaine) et Cart Mandate (avec présence humaine), au format W3C VC 2.0 et signées par FIDO2/WebAuthn ou HSM.
  - Traitement : Dans la synthèse exécutive, le titre 10.11, la sous-section AP2, le tableau et l'ADR, Intent Mandate / Cart Mandate / W3C VC 2.0 sont remplacés par Checkout Mandate, Payment Mandate, ouverts ou fermés, SD-JWT (section 10.2), avec la liste de partenaires d'AP2 retirée; un avertissement précède l'Extrait 10.2, laissé intact, ainsi que le fil rouge.
- **Responsabilité en cas de litige** — *corrigé*
  - Exposé : Sections 10.2 et 10.7 : AP2 exclut expressément la résolution des litiges et ne répartit pas la responsabilité entre les rôles; la preuve existe, la règle qui dit quoi en faire n'y est pas.
  - Volet, avant alignement : Section 10.11 : l'architecture AP2 règle la question de l'attribution de responsabilité; si le règlement respecte les bornes du mandat, l'acheteur ne peut répudier la dépense, sinon la faute est établie côté passerelle ou facilitateur.
  - Traitement : Le paragraphe de 10.11 qui disait qu'AP2 règle l'attribution de responsabilité dit maintenant qu'il l'exclut et ne répartit pas la responsabilité (sections 10.2 et 10.7), avec le renvoi à la piste d'audit; la cellule « gestion des litiges » du tableau est ramenée à « litiges hors du champ d'AP2 ».
- **Qui signe les mandats et détient les clés** — *nuance*
  - Exposé : Section 10.2 : en parcours sans présence humaine, l'agent signe lui-même les mandats fermés avec sa propre clé, publiée dans la revendication cnf du mandat ouvert.
  - Volet, avant alignement : Section 10.11 (encadré et point 6 de la liste de contrôle) : aucun conteneur d'agent ne détient de clé de signature financière; la passerelle signe PAYMENT-SIGNATURE et les mandats sont signés hors du conteneur agentique.
  - Traitement : La règle de ségrégation des clés est gardée (encadré et point 6 de la liste de contrôle), avec une phrase précisant qu'elle va au-delà de l'exposé, selon lequel l'agent signe lui-même les mandats fermés avec sa propre clé publiée dans `cnf` (section 10.2).
- **Lien entre AP2 et x402, et garanties de x402** — *corrigé*
  - Exposé : Sections 10.1 et 10.5 : protocoles distincts, AP2 pouvant porter l'autorisation et x402 le règlement; les pages x402 lues ne décrivent aucune autorisation distincte du paiement et ne disent rien du litige ni de l'identité du payeur.
  - Volet, avant alignement : Section 10.11 : x402 est intégré comme extension d'AP2; PAYMENT-SIGNATURE lie l'Idempotency-Key et le hachage SHA-256 de la requête, et la réponse 200 OK porte un reçu immuable.
  - Traitement : « Extension d'AP2 » devient « protocole distinct, AP2 portant l'autorisation et x402 le règlement » (sections 10.1 et 10.5), l'origine « Coinbase et Cloudflare » est ramenée au dépôt chez Coinbase transféré sous la x402 Foundation, « reçu immuable » est retiré, la garantie d'idempotence est présentée comme relevant de la passerelle puisque l'exposé n'en décrit pas dans x402, et un avertissement précède l'Extrait 10.3, laissé intact.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (109 % de la longueur d'origine, près du plafond de 110 %). J'ai aussi changé « W3C VC » en « SD-JWT » dans le titre `## 10.11` et le titre `### AP2`, par cohérence : à annuler si les titres doivent rester fixes. Le volet garde « Intent Mandate » / « Cart Mandate » dans le fil rouge, les extraits et leurs commentaires; les deux avertissements l'expliquent. Non touchés : les seuils de 180 ms (purge audio) et de 200 ms (interruption), car l'exposé ne couvre pas WebRTC, et la contradiction SSE 3 minutes / notifications à 60 s signalée dans les remarques du relevé pour un autre volet. Pour la nuance sur les clés, j'ai jugé la règle du volet compatible avec l'exposé (clé de l'agent gardée à la passerelle), ce que l'exposé ne tranche pas.

## Chapitre 11 — Géopolitique et gouvernance des standards

### Volet « Gouvernance des standards et anatomie de la pile interopérable »

- **Projets fondateurs de l'AAIF** — *corrigé*
  - Exposé : Section 11.2 : trois projets fondateurs (MCP, goose, AGENTS.md) à l'annonce du 9 décembre 2025; dix projets hébergés au 11 novembre 2026.
  - Volet, avant alignement : Section 11.11, introduction du tableau : « les dix projets fondateurs de l'AAIF » (formule conservée).
  - Traitement : Dans l'introduction du tableau (11.11), « dix projets fondateurs » devient « dix projets hébergés par l'AAIF au 11 novembre 2026 (section 11.2) », l'exposé ne comptant que trois projets fondateurs (MCP, goose, AGENTS.md).
- **Composition et gouvernance de l'AAIF (passage retiré comme redite de 11.2)** — *sans objet*
  - Exposé : Section 11.2 : huit membres platine (dont Bloomberg), gouvernance à deux étages (fondation réglée par la cotisation, projet par le mérite individuel).
  - Volet, avant alignement : Section 11.11 d'origine : dix entreprises citées, dont Solo.io, Hugging Face et Alibaba, « sous une gouvernance tripartite neutre ».
  - Traitement : Le passage sur les dix entreprises citées et la « gouvernance tripartite neutre » n'existe plus dans le volet (aucune occurrence de « tripartite »); Solo.io, Hugging Face et Alibaba ne subsistent que dans la colonne « Origine initiale » du tableau, laissée telle quelle.
- **Maturité des projets de l'AAIF** — *corrigé*
  - Exposé : Sections 11.2 et 11.10 : le niveau de neuf projets sur dix n'a pas pu être établi; seuil de production à Growth ou Impact; un projet Sandbox est un essai et peut être archivé.
  - Volet, avant alignement : Section 11.11 : un statut de production est attribué à chacun des dix projets (tableau); le fil rouge et l'ADR-004 placent tous ces projets au socle obligatoire; l'encadré « Important » donne agentgateway, Agent Skills et AGENTS.md pour matures fin 2026.
  - Traitement : Dans le tableau de 11.11, la colonne de statut ne retient plus que ce que l'exposé établit (A2A au niveau Growth; MCP « texte mis en œuvre; niveau non établi »; « niveau non établi » pour les huit autres, avec « obligatoire pour code dynamique » conservé pour OpenSandbox); l'encadré « Important » ne donne plus agentgateway, Agent Skills et AGENTS.md pour matures fin 2026 mais pour des briques dont le niveau n'a pas pu être établi; une phrase signale que le fil rouge et l'ADR-004 (socle obligatoire) vont au-delà du seuil Growth ou Impact et de la vérification du niveau que retient l'exposé (sections 11.2 et 11.10), sans toucher au fil rouge ni à l'ADR.
- **Statut de l'IETF et de WIMSE** — *corrigé*
  - Exposé : Sections 11.4 et 11.10 : aucun RFC propre aux agents; document WIMSE informatif, aucun RFC de WIMSE; posture « suivre de près ».
  - Volet, avant alignement : Section 11.11 : « L'IETF normalise la chaîne de confiance réseau », identité multi-environnements WIMSE comprise.
  - Traitement : La puce de 11.11 ne dit plus que l'IETF « normalise la chaîne de confiance réseau, WIMSE comprise » : elle dit que l'IETF étend des standards existants sans RFC propre aux agents (section 11.4), et que WIMSE n'est qu'un document informatif sans RFC, à suivre de près (sections 11.4 et 11.10).
- **Découverte et registres** — *nuance*
  - Exposé : Section 11.10 : adopter un registre interne et suivre le reste; projet IEEE naissant.
  - Volet, avant alignement : Sections 11.11 à 11.15 : AGNTCY OASF et Agent Directory au socle obligatoire (anneau 1, couche 5, ADR-004).
  - Traitement : Une phrase ajoutée à la puce AGNTCY (11.11) indique que retenir OASF et Agent Directory au socle obligatoire (section 11.14, ADR-004) va au-delà de l'exposé, qui recommande d'adopter un registre interne et de suivre le reste (registre officiel en préversion, projet IEEE naissant; section 11.10); fil rouge et ADR laissés intacts.
- **WebMCP et groupes communautaires du W3C** — *corrigé*
  - Exposé : Sections 11.3 et 11.10 : groupes communautaires sans aval du W3C; « rien n'est prêt » de ce côté pour la production.
  - Volet, avant alignement : Section 11.11 : « Le W3C encadre ... WebMCP »; déploiement par paliers en 2027 (encadré « Important », couche 6, condition de révision de l'ADR-004).
  - Traitement : « Le W3C encadre ... WebMCP » est remplacé, dans la puce de 11.11, par la mention d'un groupe communautaire hébergé sans aval du W3C, aux rapports qui ne sont pas des Recommandations (section 11.3); dans l'encadré « Important », WebMCP quitte la liste des standards déployés par paliers en 2027 et renvoie à la section 11.10 (rien de prêt côté groupes communautaires).

Ce qui reste, selon l'agent d'alignement : Seul chapitre-11-volet-a.md est modifié (15 lignes : introduction du tableau, 10 cellules de statut, 3 puces, l'encadré « Important »); le contrôle répond « conforme » (103 %). Le relevé est exact sur cinq points; l'exposé ne nomme jamais WebMCP, et le traitement s'appuie sur la mention « Community Group » que porte le volet lui-même, hypothèse à confirmer. Laissés tels quels, car ils ne figurent pas au relevé : le bloc de l'extrait 11.1, qui n'admet que deux versions MCP antérieures à la révision de juillet 2026 (exposé 11.6, sans identifiant de version); ANP à la couche 5; les déploiements AGNTCY et AP2/x402 « par paliers en 2027 », sur lesquels l'exposé est muet; la clause de 48 heures et la cible de moins de 4 heures, objets distincts que l'exposé ne tranche pas.

## Chapitre 12 — Couche sémantique et ontologies

### Volet « Couches sémantiques normalisées et ontologies d'entreprise »

- **Version et maturité d'Ossie** — *corrigé*
  - Exposé : 12.4 et grille de décision : aucune version 1.0 n'existe, la seule version parue est la 0.1.1, la branche 0.3.0.dev0 se déclare impropre à la production, et rien ne doit être bâti en production dessus.
  - Volet, avant alignement : Le manifeste de l'Extrait 12.1 déclare `version: "1.0.0"`; l'ADR-009 est « Acceptée » et adopte Apache Ossie pour la production, avec une condition de révision calée sur les « versions majeures d'Apache Ossie »; la synthèse parle d'une couche « normalisée sous Apache Ossie ».
  - Traitement : Synthèse : « normalisée sous Apache Ossie » devient « décrite dans le format d’échange Apache Ossie (section 12.4), projet en incubation dont la seule version parue est la 0.1.1 »; ADR-009 : « versions majeures » devient « versions publiées », et une phrase avant l’encadré rappelle l'absence de version 1.0, la branche 0.3.0.dev0 impropre à la production et la recommandation de la grille de décision; une phrase avant l'Extrait 12.1 signale que son `version: "1.0.0"` ne correspond à aucune version existante (section 12.4); statut « Acceptée » laissé (décision fictive de Boréal).
- **Statut du projet à l'ASF** — *corrigé*
  - Exposé : 12.4 : projet en incubation, sans aval complet de l'Apache Software Foundation et sans rapport d'étape.
  - Volet, avant alignement : Le tableau comparatif de 12.8 qualifie Ossie de « standard ASF » (portabilité « Maximale »).
  - Traitement : Dans le tableau de 12.8, « Maximale (standard ASF) » devient « Maximale (format d’échange en incubation à l’ASF; section 12.4) ».
- **Cibles de compilation et exposition aux agents** — *corrigé*
  - Exposé : 12.4 : le dépôt fournit des convertisseurs de référence vers dbt, GoodData, Polaris et Salesforce; la spécification ne décrit aucune interface d'interrogation. 12.5 : l'exposition aux agents passe par des serveurs MCP propres à chaque éditeur.
  - Volet, avant alignement : Le manifeste est compilé par CI/CD vers Snowflake Semantic Views, Databricks Unity Catalog Metric Views, dbt, Cube et des serveurs MCP analytiques de la fabrique agentique; le résolveur de l'Extrait 12.3 interroge Ossie par un client `OssieClient.query`.
  - Traitement : En 12.9, une phrase précède la liste des cibles : le dépôt fournit des convertisseurs vers dbt, GoodData, Polaris et Salesforce, la spécification ne décrit aucune interface d’interrogation et l'exposition passe par des serveurs MCP propres à chaque éditeur (sections 12.4 et 12.5), l'architecture visant des cibles plus larges; la synthèse dit « vise à compiler »; avant l'Extrait 12.3, un avertissement signale que `OssieClient.query` suppose une interface que la spécification ne définit pas (travail futur de la feuille de route).
- **SQL libre en production** — *nuance*
  - Exposé : 12.5 (règle 4) et grille de décision : borner le SQL libre (lecture seule, périmètre restreint, permissions de l'appelant); le SQL libre en lecture seule reste admis pour l'exploration ponctuelle d'un analyste.
  - Volet, avant alignement : ADR-009, décision (a), et point 1 de la liste de contrôle : le SQL libre sur tables physiques est interdit en production pour tout agent L1 à L4.
  - Traitement : Une phrase avant la liste de contrôle dit que le point 1 et la décision (a) de l'ADR-009 vont au-delà de la section 12.5, qui borne le SQL libre (lecture seule, périmètre restreint, permissions de l'appelant) et l'admet en lecture seule pour l'exploration ponctuelle d'un analyste; l'interdiction est gardée.
- **Ontologie : quand l'imposer** — *nuance*
  - Exposé : 12.3 et grille de décision : aucune ontologie au départ; à réserver aux domaines bornés à fort enjeu ou aux secteurs dotés d'une ontologie de référence. 12.4 : la spécification d'ontologie d'Ossie est jeune, sans moteur d'inférence défini.
  - Volet, avant alignement : L'ontologie opérationnelle causale est « structurante dès le jour 1 » et exigée pour tout outil MCP mutatif L2+ (ADR-009, décision (c)); il s'agit d'un registre propre à la plateforme (Extrait 12.2), non de la spécification d'ontologie d'Ossie.
  - Traitement : En 12.10, deux phrases ajoutées à la fin du paragraphe d'introduction : l'exigence de la décision (c) va au-delà de la section 12.3 (aucune ontologie au départ, réservée aux domaines bornés à fort enjeu ou aux secteurs dotés d'une ontologie de référence), et elle repose sur le registre de l'Extrait 12.2, non sur la spécification d'ontologie d'Ossie, jeune et sans moteur d'inférence défini (section 12.4).
- **Terme à deux propriétaires (« client actif »)** — *avertissement*
  - Exposé : 12.7 : quand deux domaines définissent un terme différemment, on ne choisit pas : on nomme deux métriques distinctes, on documente l'écart et on retire le terme nu du catalogue exposé aux agents.
  - Volet, avant alignement : Le groupe arrête une définition normative unique du « client actif » (`is_active_commercial_customer`), les synonymes « client actif » restant rattachés à cette seule métrique.
  - Traitement : Avant l'Extrait 12.1, une phrase dit que le manifeste arrête une définition unique du « client actif » alors que la section 12.7 recommande, pour un terme à deux propriétaires, deux métriques nommées, l'écart documenté et le terme nu retiré du catalogue exposé aux agents; le code et les synonymes sont inchangés.
- **Exactitude du SQL libre sur schéma d'entreprise** — *corrigé*
  - Exposé : 12.1 : banc d'essai de 2023, 16 % de bonnes réponses en SQL direct contre 54 % sur graphe de connaissances (résumé d'article, modèle dépassé).
  - Volet, avant alignement : Plus Dépasse 90 % sur une base de démonstration de huit tables; « 55–72 % sur ERP réels » dans le tableau comparatif; aucune source citée.
  - Traitement : En 12.8, la phrase sur les « 90 % » et les huit tables est remplacée par le banc d'essai de 2023 de la section 12.1 (16 % en SQL direct contre 54 % sur graphe de connaissances, résumé d'article, modèle dépassé, 54 % n'étant pas un résultat de production); la cellule « 55–72 % sur ERP réels » du tableau reprend le 16 % avec le renvoi à la section 12.1.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (106 % de la longueur d'origine). Les chiffres du fil rouge Boréal, le statut « Acceptée » de l'ADR et le rappel « Structurante dès le jour 1 » de la synthèse sont laissés. Les incohérences internes relevées (Extraits 9.2 et 9.3, PARTS_COMMITTED, AllocateReplacementPart, vingt-cinq contre 24 agents) restent telles quelles, l'exposé ne tranchant pas. Non relevés donc non traités : les noms de champs du manifeste, que l'exposé dit à vérifier dans le dépôt, et quelques chiffres illustratifs sans source (« > 99 % compilé », 0,999, 14 000 tables, 8 à 25 %).

## Chapitre 13 — Ingénierie du contexte

### Volet « Le mur du contexte d'entreprise : ingénierie du contexte à grande échelle »

- **Tarif de lecture au cache KV** — *corrigé*
  - Exposé : Section 13.5 : une lecture au cache coûte un dixième du prix d'entrée de base sur la plupart des modèles, jusqu'à un quarantième sur certains (tarif d'un seul fournisseur, API de Claude).
  - Volet, avant alignement : Section 13.7 (équation du coût) : le préfixe est lu au tarif réduit, « cinq à dix fois inférieur au tarif plein ».
  - Traitement : Dans le paragraphe qui suit l'équation de la section 13.7, « cinq à dix fois inférieur au tarif plein » devient « un dixième du tarif plein sur la plupart des modèles, jusqu'à un quarantième sur certains », avec la mention du tarif d'un seul fournisseur (API de Claude) et le renvoi à la section 13.5; la formule est intacte.
- **Résumé génératif comme technique de compaction** — *nuance*
  - Exposé : Section 13.1 : la compaction par résumé est l'une des trois techniques de base pour les tâches longues; grille de décision : en travail multi-agents, « seul un résumé remonte ».
  - Volet, avant alignement : Tableau de la section 13.7 et option 2 de l'ADR : le résumé glissant ou génératif est jugé dangereux (perte de seuils et d'exclusions) et rejeté seul, au profit d'une enveloppe de transfert typée à quatre volets (section 13.10).
  - Traitement : Une phrase ajoutée avant le tableau de la section 13.7 dit que le rejet du résumé glissant seul (tableau et ADR-008, section 13.12) va au-delà de la section 13.1, où la compaction par résumé est l'une des trois techniques de base et où les sous-agents ne renvoient qu'un résumé condensé; tableau et ADR inchangés.
- **Contexte de domaine chargé d'office** — *relevé inexact*
  - Exposé : Grille de décision : par défaut, ne pas fournir de vue d'ensemble d'un domaine, sauf documentation absente ou inaccessible; section 13.4 : chaque ligne de contexte permanent se paie.
  - Volet, avant alignement : Section 13.8, Strate 1 : cadre sémantique de domaine (glossaire Ossie, politiques de la division, invariants du dossier) chargé à chaque session, quota de 1 200 à 2 400 jetons. Divergence discutable : le volet parle de définitions et d'invariants, non d'une vue d'ensemble.
  - Traitement : Rien modifié : la Strate 1 charge des définitions applicables, des politiques et des invariants, non une vue d'ensemble du domaine, et la section 13.5 place justement les politiques parmi ce qui est stable en tête de préfixe.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (4518 à 4573 mots). Le troisième point reste discutable, car la grille de décision déconseille la vue d'ensemble d'un domaine et le contexte permanent long; le relevé le dit lui-même. Je ne l'ai pas retenu parce que la Strate 1 est bornée (1 200 à 2 400 jetons) et ne contient que des éléments non déductibles. Non traités, faute d'appui dans l'exposé : le « quadruple » de la facture et de la latence en cas d'invalidation du préfixe, et le « 70 à 90 % » de l'ADR, qui sont des chiffres propres au volet. L'encadré sectoriel Juridique & Assurance et la liste de contrôle (point 6) rejettent aussi la paraphrase des clauses; la phrase de nuance ne les couvre pas.

## Chapitre 14 — Mémoire

### Volet « Architectures de mémoire agentique distribuée et bi-temporelle »

- **Architecture par défaut** — *nuance*
  - Exposé : Grille de décision : fichiers par agent ou par projet par défaut; graphe seulement si la temporalité et le lignage sont exigés; pas de mémoire à long terme tant qu'un besoin entre sessions n'est pas établi (14.2 et Grille de décision).
  - Volet, avant alignement : Impose l'architecture hybride Letta + Graphiti bi-temporelle, avec garde d'écriture et effacement crypto-sélectif, pour les agents au long cours en contexte réglementé (synthèse exécutive, ADR-010, statut « Acceptée »).
  - Traitement : Phrase ajoutée au début de la section 14.11, avant l'encadré ADR : la synthèse exécutive et l'ADR-010 vont au-delà de l'exposé, qui retient par défaut des fichiers par agent ou par projet, un graphe seulement si la temporalité et le lignage sont exigés, et aucune mémoire à long terme sans besoin établi entre sessions (section 14.2 et grille de décision).
- **Contenu de la mémoire procédurale** — *relevé inexact*
  - Exposé : Selon CoALA, la mémoire procédurale couvre les poids du modèle et le code de l'agent (section 14.1).
  - Volet, avant alignement : La définit comme un répertoire de plans types et de recettes de résolution validées, tenu dans un dépôt Git de compétences ou de graphes certifiés (section 14.7).
  - Traitement : Rien modifié : le volet restreint la mémoire procédurale à la part que l'entreprise gouverne (plans types et recettes validées dans un dépôt Git de compétences). Cela ne contredit pas l'exposé, dont les exemples en entreprise sont « consignes, compétences, prompts système » et qui range Agent Skills et AGENTS.md dans cette mémoire.
- **Datation d'une arête du graphe temporel** — *corrigé*
  - Exposé : Quand une donnée nouvelle contredit une ancienne, Graphiti marque la relation comme invalide à partir d'une date (section 14.2, d'après un compte rendu secondaire).
  - Volet, avant alignement : Chaque arête porte quatre horodatages sur deux axes (validité métier et temps transactionnel), et l'ancienne arête est fermée sur les deux axes (section 14.8).
  - Traitement : Au début de « Graphiti : mémoire partagée sans écrasement » (14.8), le texte attribuait à Graphiti les quatre horodatages et la fermeture sur deux axes. Il rapporte maintenant ce que l'exposé établit (graphe temporel, relation marquée invalide à partir d'une date, d'après un compte rendu secondaire, section 14.2), puis présente le modèle à quatre horodatages comme le contrat d'accès de l'architecture. Dans le paragraphe suivant, « le moteur » devient « le magasin bi-temporel ».
- **Effacement d'un fait dérivé** — *nuance*
  - Exposé : Zep ne supprime un fait que si aucun épisode restant ne le soutient; sans lignage, l'effacement ne peut pas être exécuté avec certitude (section 14.6).
  - Volet, avant alignement : Indexe data_subject_id sur chaque souvenir dérivé et purge toutes les arêtes personnelles du sujet, avec régénération des communautés touchées (section 14.9, point 3).
  - Traitement : Phrase ajoutée en 14.9, point 3, après les deux invariants : selon ZenML, Zep ne supprime un fait que si aucun épisode restant ne le soutient (section 14.6). La purge par sujet va au-delà en retirant toutes les arêtes personnelles. Elle suppose que data_subject_id suive chaque fait dérivé, car sans lignage l'effacement ne peut pas être exécuté avec certitude.
- **Protection contre les écritures malveillantes** — *avertissement*
  - Exposé : Confirmation humaine avant d'enregistrer un souvenir, contre l'écriture différée par instruction dormante; contrôles appliqués par l'infrastructure (section 14.5).
  - Volet, avant alignement : S'appuie sur un garde déterministe (motifs rejetés par expression régulière, empreinte SHA-256 d'une preuve) sans confirmation humaine (section 14.9, point 2).
  - Traitement : Dans le paragraphe qui précède l'Extrait 14.2 (14.9, point 2), « correspond aux contrôles » devient « correspond à une partie des contrôles ». Une phrase ajoutée précise que l'exposé retient en outre, contre l'écriture différée par instruction dormante, la confirmation humaine avant d'enregistrer un souvenir (section 14.5), que le garde de l'extrait ne prévoit pas.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (4351 à 4500 mots). Il reste, hors du relevé et par choix de ne pas étendre la retouche, des attributions à Graphiti du modèle à quatre dates : la synthèse exécutive, le tableau comparatif (« arêtes à 4 dates », « insertion exacte sur valid_from »), l'option 3 de l'ADR et la légende de figure (intouchable). Je les ai laissées, mais un relecteur pourrait vouloir les harmoniser. Sur la mémoire procédurale, la définition du volet est plus étroite que celle de CoALA (poids et code compris, section 14.1). Une phrase de rappel serait possible si on la juge utile. Les incohérences internes signalées (renvoi « Extraits 10.1 à 10.3 », ADR-010, cibles chiffrées) ne sont pas tranchées par l'exposé et sont laissées telles quelles.

## Chapitre 16 — Topologies et patrons

### Volet « Topologies d'orchestration et de chorégraphie multi-agents »

- **Débat et graphes cycliques libres** — *nuance*
  - Exposé : Section 16.4 et grille de décision : le débat est admis à trois agents au plus, en lecture seule, sous un gestionnaire; la section 16.5 traite le transfert et l'essaim comme des patrons valides.
  - Volet, avant alignement : La synthèse exécutive et la décision d'architecture interdisent en production tout graphe cyclique libre (« débat ouvert entre pairs ») et n'autorisent que la boucle planificateur–exécuteur–critique bornée; l'anti-patron « comité bavard » vise quatre à six agents sans arbitre déterministe. Transfert et essaim ne sont pas traités.
  - Traitement : Dans la section 16.9, après la mention du débat de la section 16.4, une phrase dit que l'interdiction du volet va au-delà de l'exposé, qui admet le débat à trois agents au plus, en lecture seule, sous un gestionnaire (section 16.4 et grille de décision), et traite le transfert et l'essaim comme des patrons valides (section 16.5); synthèse exécutive, ADR et « comité bavard » inchangés.
- **Mécanisme de coordination entre domaines** — *nuance*
  - Exposé : Sections 16.5 et grille de décision : entre domaines, pair-à-pair par protocole (A2A, chapitre 6); topologie centralisée à l'intérieur d'un domaine.
  - Volet, avant alignement : Entre domaines, chorégraphie par événements métier immuables publiés sur un courtier (Kafka, Solace), avec orchestration déterministe à l'intérieur de chaque contexte borné; A2A sert surtout aux délégations à l'intérieur des cellules.
  - Traitement : Dans la section 16.9, à la fin du paragraphe sur la dualité, une phrase dit que la règle s'écarte de l'exposé (section 16.5 et grille : pair-à-pair par protocole entre domaines, centralisé à l'intérieur d'un domaine) et que la grille ne propose l'écart que pour une plateforme unique sous une seule autorité; la chorégraphie par événements est conservée.
- **État partagé modifiable entre agents concurrents** — *nuance*
  - Exposé : Section 16.3 : Microsoft range parmi les antipatrons le partage d'un état modifiable entre agents concurrents, source de données incohérentes (chapitre 14).
  - Volet, avant alignement : La topologie 4 (tableau noir partagé) repose sur un état partagé écrit par des agents concurrents, protégé par concurrence optimiste (ETag) sur sous-clés; le risque ASI06 (empoisonnement d'état partagé) y est noté.
  - Traitement : À la fin de la topologie 4 (tableau noir), une phrase rappelle que Microsoft range parmi les antipatrons le partage d'un état modifiable entre agents concurrents (section 16.3, chapitre 14), que l'exposé ne traite pas le tableau noir, et que la concurrence optimiste (ETag) est la parade propre au volet.
- **Surcoût de la topologie centralisée** — *relevé inexact*
  - Exposé : Section 16.2 : quatre appels de modèle contre trois (LangChain); 27,7 tours par essai pour l'architecture centralisée contre 7,2 pour l'agent unique (Kim et coll.).
  - Volet, avant alignement : La matrice donne au superviseur hiérarchique un multiplicateur de coût en jetons de 1,3 à 2,0 fois, qualifié de faible à modéré. Les mesures diffèrent (jetons, tours) et ne se comparent pas directement.
  - Traitement : Rien modifié : l'exposé ne donne aucun multiplicateur en jetons pour le superviseur, ses mesures (4 appels contre 3, 27,7 tours contre 7,2) sont d'une autre nature, et le relevé admet lui-même qu'elles ne se comparent pas; la matrice ne contredit donc pas l'exposé.
- **Coût de la coordination décentralisée** — *corrigé*
  - Exposé : Sections 16.2 et 16.4 : 26,1 tours par essai pour l'architecture décentralisée (débat et consensus), soit un peu moins que les 27,7 de la centralisée; amplification d'erreurs de 7,8 fois, entre l'orchestrateur et les agents indépendants.
  - Volet, avant alignement : Section 16.9 : le maillage conversationnel non contraint fait croître de façon quadratique les canaux et les jetons, et échoue en production pour des raisons « mathématiques et économiques mesurables »; aucune mesure indépendante n'est citée.
  - Traitement : Dans la section 16.9, l'affirmation « en production, elle échoue pour des raisons que l'on peut mesurer » est remplacée par les mesures de l'exposé (26,1 tours par essai contre 27,7 pour la centralisée; amplification d'erreurs de 7,8 fois, entre l'orchestrateur et les agents indépendants; sections 16.2 et 16.4), avec une phrase précisant que le calcul quadratique est un modèle, non une mesure; formules inchangées.
- **Taxonomie des patrons** — *corrigé*
  - Exposé : Section 16.1 : trois topologies (centralisée, décentralisée, hiérarchique) et un axe adaptatif; neuf patrons au tableau (pipeline, fan-out, routeur, superviseur, hiérarchie, planificateur à registre, débat, réflexion, transfert et essaim).
  - Volet, avant alignement : Un catalogue de six topologies canoniques censé couvrir la quasi-totalité des cas de production. Il regroupe superviseur, hiérarchie et routeur, prolonge la réflexion, et ajoute le DAG planifié, le tableau noir, le Contract Net et l'hybride BPMN/DMN, absents de l'exposé; débat, transfert, essaim, pipeline et fan-out autonomes n'y figurent pas.
  - Traitement : Dans l'introduction de la section 16.10, l'affirmation que l'expérience de fin 2026 ramène la quasi-totalité des cas de production à six topologies est remplacée par : le volet retient six topologies, alors que l'exposé, qui ne cite aucune donnée d'adoption, classe neuf patrons selon trois topologies et un axe adaptatif (section 16.1); titre, figure, ADR et liste de contrôle inchangés.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (6984 mots -> 6878 mots, 98 %). Les incohérences internes sur N_max (2 ou 3, code entre 1 et 4, fil rouge à 2 contre maxIterations à 3 dans le BPMN) et les tâches BPMN non définies restent telles quelles : l'exposé ne fixe aucune valeur de plafond, seulement « un plafond d'itérations ». Ne figurent pas au relevé et n'ont pas été touchés : plusieurs chiffres que l'exposé ne confirme pas (multiplicateurs de la matrice, 60 %, 70 %, facteur 3 à 5, ratios 12:1 et 8×), les trois « dégradations » de la section 16.9, l'affirmation d'adoption « Entre 2024 et 2025, plusieurs cadriciels… » et le titre « Anti-patrons observés en production ».

## Chapitre 17 — Déterministe ou agentique

### Volet « Le grand découplage : contrôle déterministe et autonomie probabiliste »

- **Rôle du niveau de confiance dans la sortie d'un agent** — *nuance*
  - Exposé : Sections 17.2 (règles de conception) et grille de décision : l'agent rend des issues nommées et routables; le niveau de confiance ne sert que d'information d'appoint, car un seuil reporte le problème sur le branchement suivant.
  - Volet, avant alignement : La garde de sortie route sur un seuil de confiance calibrée τ (0,90 ou 0,82 dans l'Extrait 17.2; τ = 0,90 dans le fil rouge), en plus de l'énumération fermée avec abstention UNKNOWN. Le seuil décide du repli; conservé tel quel.
  - Traitement : Le seuil de confiance τ est conservé; une phrase ajoutée avant l'Extrait 17.2 (section 17.9) dit qu'il s'ajoute aux issues nommées et va au-delà de l'exposé, qui demande des issues nommées et routables et ne tient le niveau de confiance que pour une information d'appoint, car un seuil reporte le problème sur le branchement suivant (section 17.2).
- **Outils à effets offerts au modèle** — *nuance*
  - Exposé : Sections 17.2 et 17.5, grille de décision : un outil de l'agent borné peut être une tâche de service, un sous-processus ou un processus entier (le modèle propose, le moteur exécute, effets compris); un agent ouvert accède aux systèmes d'enregistrement par un processus exposé comme outil.
  - Volet, avant alignement : Les outils d'une cellule sont restreints à la lecture et à la simulation; toute écriture est exécutée par l'épine dorsale après la garde de sortie (organe 3, ADR-002, point 3 de la liste de contrôle). Règle plus stricte que celle de l'exposé; conservée telle quelle.
  - Traitement : La restriction des outils à la lecture et à la simulation est conservée; une phrase ajoutée au même endroit rappelle que l'exposé admet comme outil d'agent borné une tâche de service, un sous-processus entier ou l'appel d'un autre processus, que le moteur exécute (section 17.2), et donne à un agent ouvert accès aux systèmes d'enregistrement par un processus exposé comme outil (section 17.5).

Ce qui reste, selon l'agent d'alignement : Les deux nuances tiennent en un seul paragraphe de trois phrases inséré entre la liste des quatre éléments de la section 17.9 et l'introduction de l'Extrait 17.2; rien d'autre n'a été touché (code, fil rouge, ADR-002 et liste de contrôle intacts). Le « effets compris » du relevé n'est pas littéral dans l'exposé : la phrase s'en tient à « le moteur exécute » et au processus exposé comme outil. Les incohérences internes du relevé (valeurs de rootCauseCode, N_max, K_max, interface TypeScript) sont dans des blocs de code ou des éléments à conserver, et l'exposé ne les tranche pas : laissées telles quelles.

## Chapitre 18 — Exécution durable et transactions

### Volet « Moteurs d'exécution durable et gestion des cycles de vie de longue durée »

- **Statut de l'extension durable de Microsoft Agent Framework** — *corrigé*
  - Exposé : Section 18.6 (tableau) : paquets de l'extension durable en préversion; le checkpointing durable ne rend pas les écritures externes transactionnelles ni exécutées exactement une fois.
  - Volet, avant alignement : Section 18.9 : le Microsoft Agent Framework « s'appuie en production sur le moteur Durable Task Framework »; aucune mention de la préversion.
  - Traitement : Section 18.9 : « s'appuie en production » devient « Son extension durable s'appuie sur » le moteur Durable Task Framework, et une phrase ajoute que les paquets sont en préversion et que le checkpointing durable ne rend pas les écritures externes transactionnelles ni exécutées exactement une fois (section 18.6); « Il unifie » devient « Le cadriciel unifie » pour lever l'ambiguïté du pronom.
- **Modèle d'état de Restate** — *corrigé*
  - Exposé : Section 18.6 (tableau) : journal rejoué, l'état voyage avec chaque requête, services sans état.
  - Volet, avant alignement : Section 18.9 : Virtual Objects, acteurs à état clé-valeur persistant avec un seul écrivain par clé (aussi dans le tableau comparatif).
  - Traitement : Section 18.9 : retrait de « acteurs à état clé-valeur persistant » dans l'item Virtual Objects, avec une phrase renvoyant à la section 18.6 (journal rejoué, état porté par la requête, services sans état); cellule du tableau comparatif réécrite dans le même sens; avertissement ajouté dans l'introduction de l'Extrait 18.3 (code intact) sur l'état ctx.get/ctx.set.
- **Moteur durable côté AWS** — *nuance*
  - Exposé : Section 18.6 : AWS Lambda durable functions, points de contrôle et rejeu, exécutions jusqu'à un an, attentes non facturées.
  - Volet, avant alignement : Section 18.9 : côté AWS, seul Bedrock AgentCore est présenté; pour les sagas réglementaires de plusieurs semaines (T4), AWS Step Functions sert de trame d'ensemble. Lambda durable functions n'est pas traité.
  - Traitement : Section 18.9 : l'association Step Functions et Bedrock AgentCore pour les sagas T4 est gardée, suivie d'une phrase disant qu'elle va au-delà de l'exposé, qui présente côté AWS les Lambda durable functions (points de contrôle et rejeu, jusqu'à un an, attentes non facturées), situées par rapport à Step Functions (section 18.6).
- **Latences de journalisation par moteur** — *corrigé*
  - Exposé : Section 18.6 : aucun banc d'essai indépendant comparant ces moteurs sous charge agentique n'a été lu; le tableau reflète ce que chaque éditeur dit de son produit, sans chiffre de latence.
  - Volet, avant alignement : Section 18.9 : latences chiffrées de journalisation par pas (Temporal 8 à 25 ms, Restate 1 à 5 ms, Durable Task 10 à 35 ms), sans source.
  - Traitement : Retrait des chiffres 8 à 25 ms, 1 à 5 ms, 10 à 35 ms (tableau, remplacés par « Aucune latence chiffrée (section 18.6) »), de « 1 à 4 millisecondes » (prose Restate, avec renvoi à 18.6), de « quelques millisecondes » (introduction de l'Extrait 18.3) et de « Latence sous 5 ms » (tableau de profils).
- **Durée et taille d'une exécution Temporal** — *corrigé*
  - Exposé : Sections 18.1 et 18.6 : Temporal n'impose aucune limite de durée à une exécution; Continue-As-New sert à poursuivre une exécution dont l'état grossit (18.2).
  - Volet, avant alignement : Sections 18.9 et 18.11 : horizon « mois à années »; une instance plafonne autour de 51 200 événements ou 50 Mo d'historique sérialisé, d'où le compactage par Continue-As-New.
  - Traitement : Tableau : « Mois à années » devient « Aucune limite de durée à une exécution (section 18.1) »; section 18.11 : le plafond de 51 200 événements ou 50 Mo est remplacé par l'énoncé de l'exposé (aucune limite de durée, l'état grossit, Continue-As-New poursuit l'exécution dans un nouveau maillon, section 18.2).
- **Nom de l'en-tête d'idempotence** — *avertissement*
  - Exposé : Section 18.3 : le brouillon de l'IETF normalise l'en-tête `Idempotency-Key`.
  - Volet, avant alignement : Extrait 18.2 (code, conservé tel quel) : l'appel à la passerelle LLM utilise l'en-tête `X-Idempotency-Key`.
  - Traitement : Extrait 18.2 : le code est intact; une phrase ajoutée dans l'introduction signale que le code emploie `X-Idempotency-Key` alors que l'exposé indique `Idempotency-Key`, normalisé par le brouillon de l'IETF (section 18.3).

Ce qui reste, selon l'agent d'alignement : Contrôle « conforme » (6878 à 6839 mots). L'incohérence Restate « 1 à 4 ms » contre « 1 à 5 ms » disparaît avec les chiffres; les trois compositions de la clé d'idempotence, l'écart de 14 jours contre 29 à 13,5 jours (fil rouge) et l'apostrophe de 18.13 sont laissés, l'exposé ne tranchant pas. Non relevés donc non touchés, à voir : seuils de 10 000 événements (tableau de profils) et M = 1 000 (18.11), « objets virtuels par équipement » (ADR et tableau de profils), et plusieurs affirmations absentes de l'exposé (« la référence » pour Temporal, Bedrock AgentCore, Dapr, Entra ID).

## Chapitre 19 — Orchestration événementielle

### Volet « Maillage événementiel asynchrone et patron Saga à compensation »

- **Seuil d'emploi de la chorégraphie** — *corrigé*
  - Exposé : Section 19.7 : la chorégraphie garde sa place quand les réactions sont indépendantes, sans annulation ni ordre requis; dès qu'une transaction d'affaires traverse plusieurs agents, il faut un coordinateur (Saga orchestrée).
  - Volet, avant alignement : Section 19.10 et ADR-013 : la chorégraphie pure sans coordinateur est proscrite au-delà de trois acteurs ou sous régime réglementé (BSIF E-23), et rejetée pour les flux inter-divisions. Le seuil de trois acteurs n'existe pas dans l'exposé.
  - Traitement : Dans la section 19.10, le seuil « au-delà de trois acteurs » (absent de l'exposé) est remplacé par le critère de la section 19.7 (« dès qu'une transaction d'affaires traverse plusieurs agents », il faut un coordinateur); la proscription sous régime réglementé (BSIF E-23) est gardée, avec une phrase disant qu'elle va au-delà de la section 19.7, où la chorégraphie reste admise pour des réactions indépendantes, sans annulation ni ordre requis; l'ADR-013 (rejet de la chorégraphie pure) est compatible avec l'exposé et n'est pas touché.
- **Appel direct ou dorsale d'événements par défaut** — *corrigé*
  - Exposé : Grille de décision (après la section 19.7) : appel direct par défaut; aucune dorsale tant qu'un déclencheur direct suffit; dorsale si relecture, pointes de charge ou consommateurs multiples.
  - Volet, avant alignement : Synthèse, section 19.8 et ADR-013 : au-delà de trois systèmes d'enregistrement traversés, les appels synchrones sont écartés au profit d'un maillage asynchrone; le socle hybride Solace/Kafka est retenu pour toute mutation touchant au moins deux systèmes d'enregistrement.
  - Traitement : Dans la Synthèse, le seuil « au-delà de trois systèmes d'enregistrement » est remplacé par les conditions de l'exposé (travail plus long qu'une connexion, consommateurs multiples, pointes de charge; section 19.1 et grille de décision) et une phrase rappelle que l'appel direct reste le défaut, sans dorsale tant qu'un déclencheur direct suffit; au début de la section 19.13, une phrase avant l'encadré ADR-013 indique que retenir le maillage Solace/Kafka pour toute mutation touchant deux systèmes d'enregistrement va au-delà de la grille de décision. La section 19.8 ne contient pas le seuil et reste inchangée.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (5057 à 5181 mots). Le second traitement combine une correction de la Synthèse (chiffre sans source dans l'exposé) et une nuance devant l'ADR, qui reste identique, titre compris; ce dosage est un jugement, car on pouvait aussi garder le seuil de trois systèmes avec une simple nuance. Non traité, hors relevé : l'exposé ne couvre ni Solace ni NATS (« autres courtiers non traités », Limites), donc le choix des courtiers de la section 19.8 et le socle Solace/Kafka n'ont pas d'appui dans l'exposé.

## Chapitre 25 — Intégration au patrimoine

### Volet « Intégration du patrimoine sans API : Computer-Use Agents (CUA), RPA/APA et mainframes »

- **Interface utilisateur pilotée par un agent (CUA)** — *avertissement*
  - Exposé : Limites de ce chapitre : le pilotage de l'interface utilisateur par un agent, dernier recours quand aucune interface programmable n'existe, n'est couvert par aucune source lue et n'est pas traité.
  - Volet, avant alignement : Les sections 25.6, 25.8 et 25.10 le traitent en détail (harnais, tableau de défaillances, latence, coût, fil rouge), avec des chiffres sans source.
  - Traitement : Ajouté une phrase au début de la section 25.6 : l'exposé ne traite pas le pilotage de l'interface par un agent (aucune source lue, « Limites de ce chapitre ») et les chiffres du volet à son sujet, dont le « jusqu'à 60 % » de la synthèse, ne reposent sur aucune source, hors cas fictif du Groupe Boréal; sections, tableaux et chiffres conservés.
- **Cache de lecture et lieu de la limite de débit** — *nuance*
  - Exposé : 25.2 : une valeur en cache de lecture n'a pas d'autorité, la décision relit la donnée à la source ou porte la date de sa copie. 25.5 : la limite de débit se pose par agent et par outil, à la passerelle.
  - Volet, avant alignement : 25.7 : les outils MCP de l'ordinateur central appliquent eux-mêmes un cache court (TTL 15–60 s) et un limiteur de cadence calé sur les fenêtres de lots, sans mention de datation ni de passerelle.
  - Traitement : Ajouté deux phrases à la fin du point 3 de la section 25.7 : une valeur en cache n'a pas d'autorité, la décision relit la source ou porte la date de sa copie (section 25.2); le limiteur propre aux outils va au-delà de la limite de débit par agent et par outil à la passerelle que retient l'exposé (section 25.5).
- **Palier de départ et voie d'écriture** — *laissé*
  - Exposé : 25.3 et Grille de décision : premier palier en lecture seule; écriture réversible par outil de niveau métier; voie d'écriture par l'interface d'affaires du système.
  - Volet, avant alignement : 25.10 : le CUA écrit en production sur le sous-module de 2008 par saisie d'écran (touche F9 après relecture), sans palier de lecture seule mentionné; l'adaptateur de l'extrait 25.1 écrit aussi une ligne dans la table MCP_IDEMPOTENCY_LOG sur le système.
  - Traitement : Rien modifié : l'écriture du CUA par saisie d'écran (F9) relève du cas fictif du fil rouge en 25.10; la ligne MCP_IDEMPOTENCY_LOG de l'extrait 25.1 est la trace propre à l'adaptateur et non une écriture directe dans les tables d'affaires, et l'exposé (25.5) charge la couche de porter l'idempotence sans dire où la consigner.
- **Contenu de la couche d'encapsulation** — *avertissement*
  - Exposé : 25.4 : la couche anticorruption se limite à la traduction, ni règles d'affaires ni orchestration; la validation et l'assainissement des entrées s'y placent.
  - Volet, avant alignement : Extrait 25.1 : l'adaptateur borne le montant demandé (supérieur à 0 et au plus 25 000 en valeur de code) et décide des codes retour acceptés (0000, 0104), ce qui peut relever de règles d'affaires plutôt que de validation d'entrées.
  - Traitement : Ajouté une phrase juste avant l'extrait 25.1 (code intact) : la borne de montant et le choix des codes retour ne sont à leur place dans l'adaptateur que s'ils relèvent de la validation des entrées, l'exposé limitant la couche à la traduction, sans règles d'affaires ni orchestration (section 25.4).

Ce qui reste, selon l'agent d'alignement : Divergence 3 : le volet n'énonce nulle part de règle contraire au palier de lecture seule; seule la fiction l'écrit. Si le relecteur veut tout de même un rappel du palier (section 25.3, grille de décision), une phrase en 25.8 suffirait. Les contradictions internes (part des CUA de 5 à 8 %, au plus 8 %, 5 à 10 % et 6,5 %; latence 8 à 30 s contre 8–35 s; « BEL » non défini) sont laissées : l'exposé ne tranche pas et ne couvre pas les CUA. Le fil rouge, les blocs de code, figures, extraits, titre ADR et liste de contrôle sont intacts; contrôle conforme à 105 % du volume.

## Chapitre 27 — Stratégie multi-plateformes

### Volet « Fédération des jardins clos SaaS et problème de l'« orchestrateur d'orchestrateurs » »

- **Plan de contrôle d'ensemble : fédérer ou posséder** — *nuance*
  - Exposé : Section 27.4 : le plan de contrôle d'ensemble se fédère (aucun éditeur ne gouverne les agents des autres comme les siens); l'entreprise ne possède que le registre de référence, l'identité et les politiques.
  - Volet, avant alignement : Section 27.7 et ADR-015 : l'entreprise détient en propre un plan neutre d'orchestration (Temporal, agentgateway, médiation iPaaS) qui devient l'orchestrateur de toute saga touchant au moins deux silos.
  - Traitement : Ajouté en fin du paragraphe de l'approche C (section 27.7) une phrase disant que posséder le plan neutre, comme le prescrit l'ADR-015 (section 27.11), va au-delà de ce que retient l'exposé, qui recommande à la section 27.4 de fédérer le plan de contrôle d'ensemble et de ne posséder que le registre de référence, l'identité et les politiques.
- **Essais de fédération entre plateformes** — *laissé*
  - Exposé : Limites de ce chapitre : aucun essai de fédération ou de migration entre plateformes n'a été réalisé ni trouvé.
  - Volet, avant alignement : Section 27.10 (fil rouge) : résultats mesurés après 90 jours chez Groupe Boréal (coût par saga de 4,15 à 0,68 $ CAD, 19 cycles bloqués, 100 % d'écritures nominatives).
  - Traitement : Rien modifié : les résultats après 90 jours (4,15 à 0,68 $ CAD, 19 cycles bloqués, 100 % d'écritures nominatives) appartiennent au cas fictif du Groupe Boréal (section 27.10, encadré fil rouge) et ne contiennent aucune affirmation générale sur le monde réel.
- **Calendrier de référence** — *corrigé*
  - Exposé : En-tête du chapitre : état de référence au 9 novembre 2026 (règlement européen et frais de changement interdits à compter du 12 janvier 2027, donc à venir).
  - Volet, avant alignement : Sections 27.6, 27.8, 27.10 : 2027 est traité comme le présent (T1 et T2 2027, résultats après 90 jours).
  - Traitement : Retiré le « 2027 » pris pour le présent dans trois affirmations sur le monde réel : « en 2027, chaque grand éditeur… » devient « aujourd'hui, chaque grand éditeur… » dans la synthèse, « (2027) » est ôté de l'en-tête du tableau de la section 27.6, et « est en 2027 un motif de blocage immédiat » devient « est un motif de blocage immédiat » en 27.8; T1 et T2 2027 et les 90 jours du fil rouge (27.10) sont laissés.
- **Registre et annuaire des agents** — *nuance*
  - Exposé : Section 27.2 : un registre de référence unique, désigné par l'entreprise, dont les registres des plateformes sont des sources; en prendre un chez un éditeur crée une dépendance de plus.
  - Volet, avant alignement : Section 27.7 : les Agent Cards sont publiées dans un annuaire fédéré OASF derrière MuleSoft Agent Fabric (Agent Registry), sans dire s'il s'agit du registre de référence.
  - Traitement : Ajouté à la fin de la puce « Versionnement asynchrone » (section 27.7) deux phrases : l'annuaire OASF derrière MuleSoft Agent Fabric n'est le registre de référence que si l'entreprise le désigne, sinon il compte parmi les registres sources (section 27.2); prendre un registre de référence chez un éditeur crée une dépendance de plus et son contenu doit rester exportable (section 27.5).

Ce qui reste, selon l'agent d'alignement : Le volet ne contredit pas frontalement l'exposé sur la divergence 4 (il se tait sur le statut de l'annuaire OASF); j'ai posé une nuance conditionnelle plutôt que d'affirmer que l'annuaire n'est pas le registre de référence, car l'exposé admet de le prendre chez un éditeur au prix d'une dépendance. Laissés faute d'arbitrage de l'exposé : les quatre contradictions internes relevées (trois frictions annoncées pour quatre listées, « triple taxation » pour quatre taxes, deux ans contre dix-huit mois dans l'encadré M&A, « Token Bucket »). Hors relevé mais à vérifier : l'encadré M&A « Jour 90 » (27.9) affirme ce que la fédération A2A « permet » alors que l'exposé dit qu'aucun essai de fédération n'a été trouvé, et SAP et Workday ne figurent pas parmi les éditeurs de l'exposé.

## Chapitre 28 — Agents industriels et périphérie

### Volet « Orchestration cyber-physique : convergence IT/OT, OPC-UA et jumeaux numériques »

- **Validation humaine avant écriture** — *corrigé*
  - Exposé : Grille de décision et 28.4 : validation humaine obligatoire avant toute écriture, aucun cas d'écart en exploitation; l'approbation est liée aux paramètres exacts.
  - Volet, avant alignement : 28.8, ADR (décision c) et liste de contrôle : la recette signée est chargée après des contrôles automatiques (signature, fraîcheur, interverrouillages, état PackML). Un acquittement humain n'apparaît que dans le tableau du niveau 2 (HOTL / HITL) et dans le fil rouge (chef d'îlot), pas dans la décision ni la liste de contrôle.
  - Traitement : Relevé exact : ni la décision (c) de l'ADR ni la liste de contrôle ne prévoyaient de validation humaine. J'ai ajouté, avec renvoi à la section 28.4 et à la règle de l'exposé (obligatoire avant toute écriture), une phrase à la décision (c), une incise à l'introduction de la liste de contrôle (8 points inchangés) et une incise avant les quatre conditions du récepteur en 28.8.
- **Rôle de l'agent en exploitation** — *nuance*
  - Exposé : Grille de décision et 28.5 : aide à la décision (lire, expliquer, proposer); commande simple seulement sur installation d'essai, confirmée par l'opérateur.
  - Volet, avant alignement : 28.8 et 28.10 : l'agent propose une consigne qui, après le sas du jumeau numérique, est appliquée en production sur les cellules d'usinage.
  - Traitement : Dans le premier paragraphe de 28.8, j'ai gardé le sas et dit qu'il va au-delà de ce que l'exposé retient (aide à la décision : lire, expliquer, proposer, section 28.5; commande simple seulement sur installation d'essai, confirmée par l'opérateur), en précisant que l'agent se borne à proposer et que seul le MES ou le SCADA charge la recette; 28.10 est un cas fictif, laissé tel quel.
- **Maturité et déploiement en production** — *corrigé*
  - Exposé : 28.5 et Limites : prototypes et démonstrateurs, seule évaluation chiffrée sur simulateur, aucun déploiement en production documenté par une source lue.
  - Volet, avant alignement : 28.10 et ADR : résultats « vérifiés sur deux trimestres » à l'usine, homologation SL-3 validée, ADR « Acceptée », « sûreté physique démontrable ».
  - Traitement : Dans l'ADR, les conséquences positives sont qualifiées d'effets attendus, sans déploiement en production documenté par une source lue (section 28.5), et « sûreté physique démontrable » devient « sûreté physique visée »; les résultats vérifiés sur deux trimestres et l'homologation SL-3 de 28.10 (fil rouge fictif) et le statut « Acceptée » de l'ADR sont laissés.
- **Statut du qualificatif « obligatoire »** — *corrigé*
  - Exposé : 28.4 (fin) : « obligatoire » est une recommandation du chapitre; aucune norme lue ne l'impose en ces termes.
  - Volet, avant alignement : Titre de 28.8, synthèse et ADR (« Norme critique de sûreté industrielle ») : le sas par jumeau numérique est présenté comme une norme et une obligation.
  - Traitement : Le statut de l'ADR « norme critique de sûreté industrielle » est remplacé par « recommandation du chapitre, non imposée par une norme lue; section 28.4 »; la synthèse (puce 3) reçoit la même mention et 28.8 une phrase disant que « obligatoire » est, comme en 28.4, une recommandation du chapitre; les titres, la légende de figure et les points de la liste de contrôle sont inchangés.
- **Protocole A2A en atelier** — *corrigé*
  - Exposé : 28.5 : aucune source lue ne décrit d'usage agent-à-agent en atelier.
  - Volet, avant alignement : Encadré de 28.9 (sites miniers) : les journaux A2A sont resynchronisés au retour du lien WAN.
  - Traitement : Dans l'encadré des sites miniers (28.9), « les journaux A2A sont resynchronisés » devient « les journaux sont resynchronisés », puisque l'exposé (28.5) ne documente aucun usage agent-à-agent en atelier.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (4831 à 4974 mots, 103 %). Les trois incohérences internes du relevé (trois barrières annoncées mais deux énumérées, constante de temps de 0,5 à 10 ms contre 1 à 10 ms, OEE) sont laissées, l'exposé ne les tranchant pas. Hors relevé et donc non touchés : d'autres affirmations d'adoption dans 28.7 et 28.8 que l'exposé ne couvre pas (OPC UA FX sur TSN « déployé en 2026–2027 », VDA 5050, A2UI, normes IEC 62443 et IEC 61511) pourraient mériter un second relevé.

## Chapitre 30 — Autorisation et délégation

### Volet « Identités non humaines (NHI) de première classe et délégation cryptographique »

- **Chaîne des acteurs (act) et atténuation de saut en saut** — *corrigé*
  - Exposé : Section 30.2 : les acteurs antérieurs de la RFC 8693 sont informatifs et n'entrent pas dans la décision d'accès; le jeton ne porte pas la chaîne de façon probante, l'orchestrateur la consigne; aucune norme adoptée ne garantit l'atténuation de saut en saut.
  - Volet, avant alignement : Le tableau de la section 30.7 donne une « chaîne récursive complète et signée »; un corollaire pose l'absence d'amplification de privilèges; le serveur MCP vérifie « l'intégralité du chemin d'orchestration traversé (act imbriqué) »; l'ADR exige que le jeton empile act. Gardé tel quel, avec « Dans ce modèle » devant le corollaire.
  - Traitement : Cellule « Généalogie des agents (act) » du tableau 30.7 ramenée à une chaîne imbriquée informative selon la RFC 8693 et consignée par l'orchestrateur; le serveur MCP « vérifie » seulement sub, ent_sponsor, le plafond et cnf, et lit les acteurs antérieurs, informatifs (section 30.2); phrase avant la formule : la loi est une cible, aucune norme ne garantit l'atténuation de saut en saut (section 30.2); corollaire déjà introduit par « Dans ce modèle », laissé; ADR traité par le renvoi placé avant l'encadré (nuance, sections 30.2 à 30.4).
- **Approbation humaine par CIBA** — *avertissement*
  - Exposé : Section 30.4 : aucun standard ne couvre l'attestation de présence humaine; CIBA ne prévoit qu'une demande lancée par le client et la confirmation en cours d'exécution appelle une spécification supplémentaire; le lien avec la RFC 9396 est une déduction du chapitre.
  - Volet, avant alignement : Le flux CIBA complet (tx_hash, séparation des tâches, signature FIDO2) est présenté comme la solution d'escalade, sans réserve. L'original disait que CIBA « résout nativement » le découplage; j'ai retiré l'adverbe sans changer le flux.
  - Traitement : Phrase ajoutée avant la séquence CIBA de 30.9 (code et extrait 30.3 intacts) : aucun standard ne couvre l'attestation de présence humaine, CIBA ne prévoit qu'une demande lancée par le client et la confirmation en cours d'exécution appelle une spécification supplémentaire (section 30.4); l'ADR est signalé comme allant plus loin dans la phrase placée avant lui.
- **RFC 9396 appliquée aux agents** — *nuance*
  - Exposé : Section 30.3 : ni MCP ni AIMS ne s'appuient sur la RFC 9396; aucun profil ne l'applique aux agents.
  - Volet, avant alignement : La combinaison OAuth 2.1, RFC 8693, RFC 9396 et DPoP/mTLS est présentée comme « réponse architecturale normalisée » (formule retirée du texte réécrit) et rendue obligatoire à chaque saut par l'ADR.
  - Traitement : Phrase ajoutée à l'introduction de 30.9, après les quatre briques : cette combinaison va au-delà de ce que retient l'exposé, ni MCP ni AIMS ne s'appuient sur la RFC 9396 et aucun profil ne l'applique aux agents (section 30.3); l'exigence de l'ADR à chaque saut est signalée de la même façon avant l'encadré.
- **Chiffres d'adoption et de résultats** — *corrigé*
  - Exposé : Limites du chapitre : aucun chiffre d'adoption ou d'efficacité n'est cité, les sources lues n'en donnent pas.
  - Volet, avant alignement : La synthèse affirme que plus de 70 % des déploiements initiaux audités fin 2026 utilisent le jeton humain ou un compte statique, sans source; le fil rouge donne des résultats chiffrés (64 secrets à 0, -94 %, 6,8 ms). Conservés.
  - Traitement : Dans la synthèse exécutive, le chiffre « plus de 70 % des déploiements initiaux audités fin 2026 » est retiré et la phrase décrit seulement ce qu'un agent peut faire (réutiliser le jeton de l'employé ou un compte de service statique); les résultats chiffrés du fil rouge (64 secrets à 0, -94 %, 6,8 ms) relèvent de la fiction et sont laissés.
- **Portée de l'interdiction du relais de jeton** — *corrigé*
  - Exposé : Section 30.1 : MCP interdit à un serveur d'accepter ou de relayer un jeton qui n'a pas été émis pour lui.
  - Volet, avant alignement : La section 30.7 dit que la spécification de sécurité de MCP interdit le relais du jeton le long de toute la chaîne (client, agent d'interface, agent spécialiste, serveur). Gardé, avec renvoi à la section 30.1.
  - Traitement : Dans l'antipatron 1 de 30.7, « la spécification de sécurité de MCP interdit cette pratique » est remplacé par l'interdiction telle que l'exposé la formule (un serveur n'accepte ni ne relaie un jeton non émis pour lui, section 30.1), plus la règle de la section 30.2 pour la chaîne d'agents (un sous-agent ne reçoit jamais le jeton de son parent).

Ce qui reste, selon l'agent d'alignement : Contrôle « conforme » (6466 à 6551 mots); 8 passages modifiés, tous dans le volet. Contradictions internes laissées, l'exposé ne tranchant pas : transfert sous 72 heures ou suspension du renouvellement (30.8) contre révocation instantanée du ClusterSPIFFEID (tableau du cycle de vie), et renouvellement du SVID « à mi-vie » contre « aux 15 min ». Non touchés, hors relevé : « antipatrons observés lors de la vague 2024–2025 » et « approches observées dans l'industrie » (30.7), énoncés d'usage sans source que l'exposé ne confirme pas non plus; à décider par le relecteur.

## Chapitre 31 — Menaces

### Volet « Modélisation des menaces multi-agents (OWASP ASI01–ASI10) et sécurité MCP »

- **Nom de l’instance qui publie le référentiel ASI** — *corrigé*
  - Exposé : Section 31.2 : publié par le projet OWASP GenAI Security, le 9 décembre 2025.
  - Volet, avant alignement : Le volet parle de l’OWASP Agentic Security Initiative (ASI); l’ADR-019 conserve cette formule dans sa condition de révision (bulletins de menaces de l’OWASP Agentic Security Initiative).
  - Traitement : Dans la condition de révision de l'ADR-019 (corps, pas le titre), « l'OWASP Agentic Security Initiative » devient « le projet OWASP GenAI Security (section 31.2) », nom que donne l'exposé.
- **Intitulés de deux catégories ASI** — *corrigé*
  - Exposé : Section 31.2 : ASI02 « Tool Misuse » et ASI05 « Unexpected Code Execution ».
  - Volet, avant alignement : ASI02 « Tool Misuse & Exploitation » et ASI05 « Unexpected Code Execution (RCE) » dans le tableau de 31.9.
  - Traitement : Dans le tableau de 31.9, « Tool Misuse & Exploitation » devient « Tool Misuse » et « Unexpected Code Execution (RCE) » devient « Unexpected Code Execution », intitulés de la section 31.2; les gloses françaises sont inchangées.
- **Serveur local et transport stdio** — *nuance*
  - Exposé : Sections 31.5 et grille de décision : liste d’autorisation, affichage de la commande et bac à sable (recommandé, non exigé); poste de développement isolé sans secrets : exception admise.
  - Volet, avant alignement : Encadré sectoriel (défense, infrastructures critiques) : aucun transport stdio sur les postes et serveurs de production, seul Streamable HTTP avec mTLS par passerelle. Prescription plus stricte, limitée à ces secteurs.
  - Traitement : La règle sectorielle (aucun stdio en production) est conservée; une phrase ajoutée à la fin de son point 2 dit qu'elle va au-delà de l'exposé, qui retient liste d'autorisation, affichage de la commande et bac à sable (recommandé, non exigé), avec exception pour un poste de développement isolé sans secrets (section 31.5 et grille de décision).
- **Force des garanties contre l’injection** — *corrigé*
  - Exposé : Section 31.4 : aucune source lue n’établit de parade fiable au niveau du modèle; CaMeL donne une sécurité prouvable au prix de 77 % de tâches résolues contre 84 % sans défense (chapitre 45); aucun taux d’attaque en production n’est cité.
  - Volet, avant alignement : Le volet affirme une neutralisation structurelle, un confinement prouvable (ADR-019) et, au fil rouge, 0,00 % d’action illégitime sur 2 500 variantes, sans mention du coût en utilité.
  - Traitement : Dans l'ADR-019, « neutralisation structurelle » et « confinement prouvable » sont remplacés par une limitation de ce que peut faire un agent détourné (31.4, 31.5), avec le constat qu'aucune source lue n'établit de parade fiable au niveau du modèle; dans l'encadré CaMeL, « l'état de l'art 2027 applique » devient « on peut recourir à » et une phrase donne le coût en utilité (77 % contre 84 %, chapitre 45, section 31.4). Le 0,00 % sur 2 500 variantes du fil rouge est laissé tel quel (fiction).
- **Attaque de type rug pull : contre-mesure** — *relevé inexact*
  - Exposé : Section 31.5 : épinglage de version, vérification d’une empreinte des définitions, nouvelle approbation à tout changement.
  - Volet, avant alignement : Blocage par défaut de tout changement dynamique en production et promotion CI/CD à chaque mise à jour légitime d’un schéma (ADR-019). Même direction, pas de nouvelle approbation individuelle mentionnée.
  - Traitement : Rien modifié : le volet ne contredit pas l'exposé. L'épinglage de l'empreinte SHA-256 des définitions et le blocage de tout changement sont équivalents à l'épinglage et à la vérification d'empreinte; la promotion CI/CD signée (Sigstore) à chaque mise à jour légitime, avec un lockfile approuvé par SecOps, tient lieu de nouvelle approbation à tout changement.

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (94 %). Aucun changement dans les blocs de code, figures, formules, titres d'extraits ni titres d'ADR. Contradictions internes du relevé (révision « semestrielle » contre « trimestrielle » dans l'ADR-019) laissées telles quelles : l'exposé ne tranche pas. Éléments du volet sans équivalent dans l'exposé, non traités faute d'avoir été relevés comme contradictoires : date et gravité du CVE-2025-54136 (section 31.5 de l'exposé ne le mentionne pas), « Linux Foundation AAIF », la description P-LLM/Q-LLM de CaMeL (le texte complet de [8] n'a pas été lu), et la cible ASR_action à 0,00 % de la liste de contrôle, que le relecteur voudra peut-être nuancer par un renvoi à la section 31.4.

## Chapitre 32 — Assurance

### Volet « Défense en profondeur : bacs à sable, garde-fous neuro-symboliques et coupe-circuits »

- **Portée de la preuve formelle et de l'application hors du modèle** — *corrigé*
  - Exposé : 32.5 : l'application hors bande est un signal, non une preuve (un seul point de mesure, petit modèle, hypothèse non établie). 32.2 : l'assurance de trajectoire est un programme de recherche; les invariants sont écrits à la main et leur complétude n'est pas démontrée.
  - Volet, avant alignement : 32.7 : l'enseignement des incidents de 2024–2025 est « sans appel » (un système probabiliste ne se sécurise pas avec un second). Fil rouge : « preuve mathématique » qu'aucune hallucination ne viole les plafonds. ADR-020 : « garanties mathématiques opposables aux régulateurs ». J'ai gardé ces énoncés et ajouté deux renvois neutres aux sections 32.5 et 32.2.
  - Traitement : Dans la section 32.7, « Les incidents de 2024–2025 enseignent » est devenu « Ce volet part de l'hypothèse », et le renvoi à la section 32.5 dit qu'elle ne l'établit pas (un signal, non une preuve, sur un seul point de mesure); dans l'ADR-020 (conséquences positives), « Garanties mathématiques opposables aux régulateurs » est ramené à une vérification hors du modèle, relativement aux invariants écrits, avec renvois aux sections 32.5 et 32.2; la « preuve mathématique » exigée par le comité dans le fil rouge est laissée, car elle relève de la fiction du Groupe Boréal.
- **Numéro du chapitre** — *sans objet*
  - Exposé : Le chapitre est le chapitre 32 (titre et sections 32.1 à 32.5).
  - Volet, avant alignement : 32.6 parle de « ce vingtième chapitre ». J'ai retiré l'expression.
  - Traitement : L'expression « ce vingtième chapitre » ne figure plus dans le volet (déjà retirée à la section 32.6), et les renvois internes restent cohérents avec le chapitre 32; rien n'a été modifié.

Ce qui reste, selon l'agent d'alignement : Seul le fichier du volet a été modifié, par deux éditions. Le contrôle répond « conforme ». Les affirmations d'adoption ou de maturité signalées dans le relevé (Cedar, OpenSandbox « standard d'entreprise », moteurs « dominants en 2027 », « immunité du cluster hôte », « arrêt d'urgence quasi instantané ») ne faisaient pas partie des deux divergences. Je les ai laissées telles quelles. Le relecteur pourrait les reprendre dans un passage distinct, car l'exposé n'en dit rien. De même, la phrase de la section 32.7 qui voit l'appel à `update_vendor_bank_account` échouer sur l'évaluation déterministe n'a pas été nuancée.

## Chapitre 33 — Observabilité et évaluation

### Volet « Observabilité distribuée de bout en bout avec OpenTelemetry GenAI »

- **Statut des conventions GenAI et décision de les imposer** — *corrigé*
  - Exposé : Section 33.2 : tous les documents lus sont au statut « Development », le dépôt n'a publié aucune version; l'exposé recommande un schéma interne, une normalisation au collecteur et l'épinglage d'une version.
  - Volet, avant alignement : Sections 33.8 et 33.13 : « l'industrie s'est alignée fin 2026 » sur les conventions, « standard ouvert CNCF »; l'ADR impose `gen_ai.*` à tout orchestrateur, agent, passerelle et serveur MCP, sans schéma interne ni épinglage.
  - Traitement : Section 33.8 : « l'industrie s'est alignée fin 2026 … de la CNCF … agentgateway » remplacé par OpenTelemetry comme format d'échange à retenir, conventions toutes « Development », aucune version publiée, schéma interne, normalisation au collecteur et épinglage (section 33.2); ADR-021 : « Standard ouvert CNCF » ramené au même constat, condition de révision « suivant les versions » devenue « suivant l'évolution … aucune version publiée », et phrase de nuance dans la Décision (imposer `gen_ai.*` va au-delà de la section 33.2); phrase équivalente ajoutée à la synthèse exécutive.
- **Échantillonnage des traces et piste d'audit** — *nuance*
  - Exposé : Sections 33.1 et 33.6 : une trace peut être échantillonnée, la piste d'audit est distincte et jamais échantillonnée; nom de l'agent, opération et modèle sont posés à la création du span pour servir aux décisions d'échantillonnage.
  - Volet, avant alignement : Section 33.9 : l'échantillonnage aléatoire en tête est une erreur, on échantillonne en queue; les transactions mutatives sont conservées à 100 % dans l'index de traces, sans piste d'audit séparée (hors encadré Merkle/WORM).
  - Traitement : Après les quatre règles de la section 33.9, deux phrases disent que l'échantillonnage en queue et la rétention à 100 % vont au-delà de l'exposé (trace échantillonnable, attributs posés à la création du span, section 33.6) et que la piste d'audit, distincte et jamais échantillonnée (section 33.1), n'est pas remplacée par l'index de traces; règles et encadré Merkle/WORM inchangés.
- **Bagages (baggage) propagés vers le serveur MCP** — *avertissement*
  - Exposé : Section 33.4 : les bagages propagés avec le contexte de trace voyagent jusque chez le tiers appelé; ils comptent parmi les fuites latérales.
  - Volet, avant alignement : Extrait 33.1 : le code place `saga.id` et le budget restant (`finops.remaining_cad`) dans le baggage envoyé au serveur MCP.
  - Traitement : Phrase ajoutée dans le texte d'introduction de l'Extrait 33.1, avant le bloc de code laissé intact : l'extrait place `saga.id` et le budget restant dans le baggage, alors que l'exposé range les bagages parmi les fuites latérales car ils voyagent chez le tiers appelé (section 33.4).
- **Message d'exception dans le span** — *avertissement*
  - Exposé : Section 33.4 : le message d'une exception est signalé comme sensible.
  - Volet, avant alignement : Extrait 33.1 : le code enregistre l'exception et copie son message dans le statut du span.
  - Traitement : Même phrase d'avertissement avant l'Extrait 33.1 : le code copie le message de l'exception dans le statut du span, alors que l'exposé le signale comme sensible (section 33.4).
- **Accès au contenu pour l'évaluation** — *nuance*
  - Exposé : Section 33.4 : les évaluateurs, humains ou automatiques, et la boucle d'exemples d'entraînement travaillent dans une zone de contenu sous accès restreint.
  - Volet, avant alignement : Section 33.10 : le contenu complet n'existe que dans la voûte forensique (erreurs et actes L3/L4, 14 à 30 jours, mandat d'incident doublement approuvé); le couloir opérationnel n'en contient pas. Aucun accès prévu pour l'évaluation.
  - Traitement : Paragraphe ajouté après la liste des deux couloirs de la section 33.10 : le dispositif ne prévoit aucun accès au contenu pour l'évaluation, ce qui va au-delà de la section 33.4, où une zone de contenu sous accès restreint sert aux évaluateurs (humains ou automatiques) et à la boucle d'exemples d'entraînement, après masquage.
- **Propagation du contexte de trace sur A2A** — *avertissement*
  - Exposé : Section 33.3 : la convention ne décrit pas comment le contexte de trace passe du client au serveur A2A, ni comment le span client se rattache au span interne de l'agent appelé.
  - Volet, avant alignement : Sections 33.9, 33.11 et liste de contrôle : la propagation W3C est tenue pour acquise sur chaque saut A2A, avec un objectif de continuité causale de 99,8 % sur les flux L3.
  - Traitement : Trois ajouts brefs signalent que les conventions lues ne décrivent ni le passage du contexte de trace client-serveur A2A ni le rattachement du span client au span interne (section 33.3) : fin de la strate 2 (section 33.9, avec `a2a.task.id` et l'identifiant d'affaires retenus par l'exposé), phrase sous le tableau des SLI (cible de 99,8 %) et point 1 de la liste de contrôle; cible, tableau et nombre de points inchangés.

Ce qui reste, selon l'agent d'alignement : Contrôle automatique « conforme » (4113 à 4501 mots). Les six divergences étaient exactes; seul le fichier du volet a été modifié. Laissé tel quel : l'incohérence « couloir opérationnel à 100 % du flux » contre 5 à 10 % des interactions L1 à l'index de traces, que l'exposé ne tranche pas. Aussi non touchés, faute d'être au relevé : les attributs `cache_read_input_tokens`, `cache_creation_input_tokens` et `reasoning_tokens` (le tableau de la section 33.9 les donne en attributs distincts, alors que l'exposé range ces jetons dans les totaux d'entrée et de sortie, section 33.1) et le « couple CLIENT / SERVER » de la strate 2 (l'exposé n'en parle pas); à trancher par le relecteur.

## Chapitre 34 — Exploitation

### Volet « Cycle de vie ADLC, CI/CD probabiliste, simulation (τ-bench) et ingénierie du chaos »

- **Seuil de la barrière de rejeu** — *nuance*
  - Exposé : Section 34.2 : la barrière est un seuil sur pass^k; l'exemple illustratif de l'article est 90 % sur quatre tentatives.
  - Volet, avant alignement : Section 34.9 et ADR : pass^5 ≥ 0,95 sur le corpus critique (manifeste : 0,95 critique, 0,88 global), cinq trajectoires par scénario.
  - Traitement : Relevé exact : la section 34.2 retient un seuil sur pass^k (exemple illustratif : 90 % sur quatre tentatives); j'ai gardé pass^5 ≥ 0,95 et les valeurs du manifeste, et ajouté en fin de paragraphe de la section 34.9 une phrase disant qu'ils vont au-delà de ce que retient la section 34.2.
- **Unités de changement d'un agent** — *corrigé*
  - Exposé : Sections 34.1 et 34.2 : le changement s'étend du code au prompt, au modèle, aux outils et à la mémoire.
  - Volet, avant alignement : Section 34.8 : six couches (code d'orchestration, modèle, prompt système et AGENTS.md, Agent Skills, schémas MCP, politiques Cedar/OPA); le tableau y substitue le contrat A2A et le code d'infrastructure. La mémoire n'y figure pas.
  - Traitement : Relevé exact : j'ai ajouté en fin du paragraphe des six couches (section 34.8) une phrase d'après les sections 34.1 et 34.2 (la mémoire est une unité de changement et le manifeste regroupe les politiques de garde-fous et de mémoire), précisant que ces six couches ne la nomment pas; énumération, tableau et manifeste inchangés.
- **Échelle des niveaux d'autonomie** — *corrigé*
  - Exposé : Section 34.4 : L0 arrêté, L1 assistance, L2 supervisé, L3 autonome (quatre niveaux).
  - Volet, avant alignement : L0/L1 pour les extracteurs, L2/L3 pour les spécialistes, et L2 à L4 pour les livraisons soumises au manifeste : un niveau L4 que l'exposé ne définit pas.
  - Traitement : Relevé exact : le niveau L4 n'existe pas dans la section 34.4 (L0 à L3); j'ai ramené « L2 à L4 » à « L2 ou L3 (niveaux de la section 34.4) » après le manifeste, « L3/L4 » à « L3 » dans le tableau des référentiels, et « L2–L4 » à « L2–L3 » dans le périmètre et la décision de l'ADR-022 (titre de l'ADR intact).

Ce qui reste, selon l'agent d'alignement : Pour la divergence 3, j'ai supprimé L4 plutôt que de l'avertir, car l'exposé définit une échelle fermée à quatre niveaux; si L4 correspond à une échelle propre au Compendium (p. ex. un autre chapitre), il faudra choisir entre l'avertissement et la correction. Non touchés, faute d'arbitrage par l'exposé : l'incohérence entre les six couches du texte et les six lignes du tableau, « Révision : Semestrielle » face à la révision annuelle des seuils de l'ADR, et l'attribution de L0/L1 aux extracteurs et de L2/L3 aux spécialistes (dans l'exposé, les niveaux se règlent par la consommation du budget d'erreur, non par classe d'agent). Les 0,45 par résultat et 0,55 par saga restent tels quels (unités différentes, l'exposé ne tranche pas).

## Chapitre 38 — Canada et Québec

### Volet « Conformité réglementaire internationale et canadienne, et droit B2B inter-agents »

- **Champ d'application de la ligne directrice E-23** — *corrigé*
  - Exposé : 38.3 : le texte ne contient ni « agentic » ni « agent »; la définition du modèle est large et la cote de risque des usages d'IA générative est laissée au jugement de chaque institution.
  - Volet, avant alignement : 38.9 : E-23 étend la gestion du risque de modèle à tout système analytique, génératif ou agentique éclairant une décision d'affaires ou financière, avec une cote de risque supérieure pour un graphe L3 qu'un copilote L1 et des paliers 1, 2 et 3 (TIER_2_MATERIAL dans le manifeste).
  - Traitement : Dans « Canada fédéral », la phrase qui étendait E-23 à tout système « agentique éclairant une décision » est remplacée par ce que dit la section 38.3 (le texte ne nomme pas les agents, sa définition large du modèle s'y applique sans peine); la cellule « Déclencheur » du tableau est alignée, et avant l'extrait 38.1 une phrase précise que le palier TIER_2_MATERIAL est un choix de l'entreprise puisque E-23 laisse la cote de risque des usages d'IA générative au jugement de chaque institution (section 38.3).
- **Force de E-23 et validation de 2e ligne** — *corrigé*
  - Exposé : 38.7 : « attentes du régulateur au 1er mai 2027 »; 38.3 : la ligne directrice prend effet à cette date. Aucune validation indépendante de 2e ligne n'y est décrite.
  - Volet, avant alignement : 38.9 : E-23 est « opposable le 1er mai 2027 » et impose une validation indépendante de 2e ligne, une surveillance continue et un plan de repli testé.
  - Traitement : La cellule « Statut » du tableau passe de « Opposable le 1er mai 2027 » à « Attentes du régulateur au 1er mai 2027 (section 38.7) », et « Trois obligations » devient « Trois exigences », avec une phrase disant que validation indépendante, surveillance continue et plan de repli vont au-delà de ce que retient la section 38.3 (inventaire, cote de risque inhérent, cote des modèles de tiers selon B-10, approbation avant tout changement).
- **Seuil de l'article 12.1 de la Loi 25** — *corrigé*
  - Exposé : 38.4 : l'article 12.1 vise toute décision fondée exclusivement sur un traitement automatisé, sans seuil d'effet; la condition « effets juridiques ou incidence importante » est celle du projet de loi C-36 (art. 63).
  - Volet, avant alignement : 38.9 : l'article 12.1 s'applique lorsqu'un agent L3 ou L4 tranche seul une décision produisant des effets juridiques ou significatifs sur une personne.
  - Traitement : Dans la puce « Décisions exclusivement automatisées (art. 12.1) », la condition « effets juridiques ou significatifs » est retirée et remplacée par une précision : « effets juridiques ou incidence importante » est la condition du projet de loi C-36 (art. 63; section 38.1), non de l'article 12.1.
- **Durée de conservation des traces** — *nuance*
  - Exposé : 38.4 et grille de décision : durée fixée par finalité, puis destruction ou anonymisation, sauf délai légal de conservation (art. 23).
  - Volet, avant alignement : 38.8 à 38.12 : archivage WORM septennal (wormDecisionLogRetentionYears: 7) des fiches de décision, renseignements personnels utilisés compris, pour rejouer les décisions lors d'une inspection E-23 sur sept ans.
  - Traitement : La durée de sept ans (bloc YAML, ADR et encadré) est conservée; une phrase avant l'extrait 38.1 dit qu'elle est un choix de l'entreprise et rappelle ce que retient la section 38.4 (durée fixée par finalité, puis destruction ou anonymisation, sauf délai légal, art. 23), et dans l'encadré « l'inspection BSIF E-23 porte sur sept ans » devient « l'entreprise veut rejouer sur sept ans une décision soumise à l'inspection ».
- **Sanctions de la Loi 25** — *relevé inexact*
  - Exposé : 38.4 : sanction administrative pécuniaire plafonnée à 10 millions de dollars ou 2 % du chiffre d'affaires mondial; aucun plafond pénal indiqué.
  - Volet, avant alignement : 38.9 : mêmes plafonds administratifs, plus un plafond pénal de 25 M$ CAD ou 4 % (art. 90.12 et 91 LPRPSP). Complément, non contradiction; non vérifiable dans l'exposé.
  - Traitement : Aucun changement : l'exposé n'indique aucun plafond pénal sans le nier, donc le volet ne le contredit pas (le relevé le reconnaît lui-même), et je ne peux rien ajouter qui ne vienne pas de l'exposé.

Ce qui reste, selon l'agent d'alignement : Les plafonds pénaux de 25 M$ CAD ou 4 % (art. 90.12 et 91 LPRPSP) restent dans le volet et ne sont pas vérifiables dans l'exposé : à confronter à la source [9] du chapitre. Je n'ai pas touché au reste du tableau comparatif (cellules E-23 « Séparation des tâches & plan de contingence », « suivi de dérive », « IA non déclarée »), à la liste de contrôle (point 3, « validation indépendante de 2e ligne ») ni à l'encadré « Triage de matérialité », qui présentent comme pratiques de l'entreprise des éléments que l'exposé ne décrit pas pour E-23; la phrase de nuance de la section 38.9 les couvre en partie. Les incohérences internes du volet (9 semaines dans l'ADR contre 9,5 dans le fil rouge, révision « Semestrielle » de l'ADR) restent, l'exposé ne les tranchant pas.

## Chapitre 40 — FinOps agentique

### Volet « FinOps agentique : gouvernance économique et Cost-per-Outcome »

- **Refacturation interne** — *nuance*
  - Exposé : Section 40.2 et grille de décision : afficher d'abord les coûts sans les refacturer, ne refacturer qu'une fois la clé d'imputation fiable.
  - Volet, avant alignement : Refacturation réelle aux centres de coûts métiers, qui responsabilise immédiatement les divisions, et obligatoire pour tout flux L2–L4 (ADR-023).
  - Traitement : Divergence confirmée (la section 40.10 et l'ADR-023 imposent la refacturation réelle à tout flux L2–L4, alors que l'exposé recommande d'afficher d'abord les coûts); une phrase ajoutée à la fin du premier paragraphe de 40.10 dit que cette règle va au-delà de ce que retient l'exposé et rappelle sa recommandation (section 40.2 et grille de décision), sans toucher à l'ADR ni à l'extrait.
- **Portée d'un plafond budgétaire** — *corrigé*
  - Exposé : Section 40.3 : un quota est un frein, pas un mur (dépassement constaté après coup, requêtes concurrentes qui excèdent le plafond, comptage imparfait).
  - Volet, avant alignement : Le disjoncteur par saga empêche la récidive d'un emballement nocturne, et l'ADR-023 annonce un risque d'emballement financier nul.
  - Traitement : Dans l'ADR-023, « Risque d'emballement financier nul » devient « freiné, non exclu (un plafond est un frein, pas un mur : section 40.3) », et une phrase est ajoutée à la fin du premier paragraphe de 40.9 : l'exposé tient un quota à la passerelle pour un frein, non pour un mur (dépassement constaté après coup, requêtes concurrentes); « Zéro récidive » du fil rouge est laissé (fiction).
- **Remise du cache de préfixe** — *corrigé*
  - Exposé : Section 40.6 : lecture à 0,1 fois le prix d'entrée sur la plupart des modèles (soit 90 % de remise), 0,05 ou 0,025 fois sur certains récents.
  - Volet, avant alignement : Remise de 75 à 90 % sur les préfixes en mémoire GPU, et remise de 80 % dans la démonstration arithmétique.
  - Traitement : Le « -75 à -90 % » du tableau de 40.7 et le « 75 à 90 % de remise … en mémoire GPU » du levier 1 de 40.9 sont remplacés par les prix de l'exposé (lecture à 0,1 fois le prix d'entrée sur la plupart des modèles, 0,05 ou 0,025 fois sur certains récents, section 40.6), et une phrase placée avant la démonstration arithmétique signale que la remise de 80 % est une hypothèse de calcul, sans modifier ses chiffres.
- **Effet du routage vers un petit modèle sur la qualité** — *laissé*
  - Exposé : Section 40.6 : le routage à deux niveaux coûte 1,7 point de F1, tout confier à un modèle léger fait tomber le F1 à 0,843; la perte de précision est à mesurer.
  - Volet, avant alignement : La cascade vers les SLM absorbe 76 % des appels chez Groupe Boréal sans dégrader le score pass^5.
  - Traitement : Le passage visé (76 % des appels absorbés par les SLM chez Groupe Boréal sans dégrader pass^5, section 40.11) relève du cas fictif : aucun changement.

Ce qui reste, selon l'agent d'alignement : Contrôle automatique : « conforme » (3967 à 4128 mots). Les trois contradictions internes signalées (révision semestrielle ou trimestrielle de l'ADR-023, zone de 95 à 100 % non décrite, 50 à 75 % de réduction du numérateur contre une facture divisée par plus de onze) sont laissées : l'exposé ne tranche aucune d'elles. À examiner par le relecteur : la phrase de 40.9 « à constance pass^5 égale » (quatre leviers, dont la cascade SLM) est une affirmation générale que l'exposé nuance (routage à deux niveaux : -1,7 point de F1, perte de précision à mesurer); elle n'était pas dans le relevé, je n'y ai pas touché. Le « 80 % » de la démonstration peut se lire comme une remise effective sur l'ensemble de l'entrée, d'où la formulation prudente « hypothèse »; l'exposé précise aussi que les plafonds budgétaires d'agentgateway n'ont pas été lus.

## Chapitre 41 — Modèle opérationnel

### Volet « Modèle opérationnel cible, facteur humain (HOTL) et prospective 2028–2030 »

- **Portée de l'obligation de maîtrise de l'IA (EU AI Act, art. 4)** — *corrigé*
  - Exposé : 41.5 : l'obligation européenne de maîtrise de l'IA a été allégée par le Digital Omnibus (chapitre 35).
  - Volet, avant alignement : 41.8 : « conformément à l'article 4 de l'EU AI Act », aucun superviseur HOTL ne reçoit ses droits d'approbation CIBA sans validation pratique d'un parcours sur les biais d'automatisation. Texte conservé tel quel.
  - Traitement : Dans la section 41.8 (« Certification de littératie IA »), j'ai retiré « conformément à l'article 4 de l'EU AI Act », gardé la règle sur les droits CIBA et ajouté qu'elle va au-delà de ce que retient l'exposé, l'obligation européenne de maîtrise de l'IA (article 4) ayant été allégée par le Digital Omnibus (section 41.5, chapitre 35).
- **Raison d'être et efficacité de la supervision humaine** — *nuance*
  - Exposé : 41.2 et 41.3 : un point d'approbation se justifie par l'imputabilité, non par la performance; l'ajout d'un humain décideur tend à dégrader le résultat quand l'agent est meilleur.
  - Volet, avant alignement : 41.9 et ADR-025 : le HOTL est le dernier recours; les canaris visent à mesurer et prouver l'effectivité réelle du contrôle humain (« filet humain effectif », « preuve empirique d'effectivité »). Texte conservé tel quel.
  - Traitement : Dans l'introduction de la section 41.9, j'ai ajouté une phrase : selon l'exposé, le point d'approbation se justifie par l'imputabilité, non par la performance (section 41.2); l'effectivité visée par les règles et les canaris est celle d'un examen réellement exercé, non d'une meilleure décision moyenne. « Filet humain effectif » et « preuve empirique d'effectivité » sont intacts (ADR-025 aussi).
- **Dimensionnement de la charge de supervision** — *nuance*
  - Exposé : 41.4 et grille de décision : aucune norme ni ratio publié pour la charge d'un superviseur; elle se règle sur la charge mesurée d'exceptions et d'approbations.
  - Volet, avant alignement : 41.9, règle 3 : plafond calculé de 33 dossiers complexes par quart (360 min, coefficient 0,65, 7 min par examen); fil rouge : 24 superviseurs HOTL pour 28 agents et 11 sagas. Tension plutôt que contradiction, texte conservé tel quel.
  - Traitement : À la fin du paragraphe de la règle 3 (section 41.9), j'ai ajouté que le plafond calculé va au-delà de ce que retient l'exposé : aucune norme publiée ne fixe la charge d'un superviseur, et la supervision se dimensionne selon la charge mesurée d'exceptions et d'approbations (section 41.4). Formule, paramètres et 33 dossiers par quart sont conservés; les 24 superviseurs du fil rouge sont laissés (fiction).

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (4156 à 4071 mots). Pour la divergence 2, le volet n'affirme pas explicitement que l'humain améliore la décision; la tension vient de « filet » et de « preuve d'effectivité ». Je l'ai donc traitée par une nuance courte plutôt que par une correction, et le relecteur peut juger qu'un « relevé inexact » aurait suffi. Je n'ai pas touché au renvoi « chapitre 38 » (relations B2B), à l'assimilation propriétaire métier nominatif / propriétaire de l'agent ni aux 90 % et 95 % : l'exposé ne tranche pas ces points.

## Chapitre 43 — Maturité et prospective

### Volet « Modèle de maturité de l'entreprise agentique (niveaux 1 à 5) et antipatterns »

- **Modèle de maturité** — *corrigé*
  - Exposé : Section 43.1 : cinq stades numérotés de 0 à 4 (Essais, Agent borné, Parc gouverné, Composition, Autonomie réglée), mesurés par domaine d'affaires, avec une preuve de sortie par stade et le stade du critère le plus faible.
  - Volet, avant alignement : Section 43.6 : cinq niveaux N1 à N5 (ad hoc, départemental, gouverné, orchestré, fédéré B2B) sur six dimensions, avec un niveau cible par processus et un score de maturité par division. Les deux échelles ne sont pas reliées et leurs niveaux ne se correspondent pas (N5 = fédération B2B). J'ai écrit « niveau » pour N1 à N5 afin de ne pas les confondre avec les « stades » de l'exposé.
  - Traitement : Section 43.6 : « Le modèle de référence 2027 » devient « Cette grille », et deux phrases précisent qu'elle se distingue des cinq stades de 0 à 4 de la section 43.1 (mesurés par domaine d'affaires), que les deux échelles ne se correspondent pas et que, comme les stades, elle est une proposition sans validation empirique.
- **Découpage de la feuille de route** — *corrigé*
  - Exposé : Section 43.2 : jalons franchis sur preuve, non en trimestres; jalon 2 (noyau de gouvernance) avant tout deuxième agent.
  - Volet, avant alignement : Section 43.9 : quatre vagues calendaires dites « trimestrielles » (semaines 1–6, mois 2–4, mois 5–8, mois 9–12+) rattachées aux portes G1 à G4.
  - Traitement : Section 43.9 : « trimestrielles » est retiré; les vagues sont dites « aux durées indicatives », avec renvoi à la section 43.2, qui découpe la feuille de route en jalons franchis sur preuve, non en trimestres.
- **Portée des constats sur le marché** — *corrigé*
  - Exposé : Sections 43.1 et « Limites » : aucune source lue ne répartit les entreprises par stade; le stade 3 n'a pas d'exemple publié; aucun cas documenté de MCP, A2A ou multi-agents en production (chapitre 42).
  - Volet, avant alignement : Synthèse exécutive et 43.7 : « la plupart des grandes entreprises » subissent une prolifération d'agents fantômes; un « audit des programmes en difficulté entre 2025 et 2027 » ramène presque tous les échecs à sept antipatterns; 85 % des flux internes se situent aux niveaux N3 et N4. Aucune source n'est donnée.
  - Traitement : Synthèse exécutive : « la plupart des grandes entreprises » devient « une entreprise peut… », avec la précision qu'aucune source lue ne répartit les entreprises par stade (section 43.1); encadré « Important » : le chiffre de 85 % est remplacé par « le niveau visé dépend du risque (section 43.1) »; section 43.7 : l'« audit des programmes en difficulté entre 2025 et 2027 » est retiré.
- **Catégories d'échec** — *corrigé*
  - Exposé : Section 43.3 : la taxonomie MAST recense quatorze modes d'échec, surtout de conception et de coordination.
  - Volet, avant alignement : Section 43.7 : sept antipatterns structurels expliquent presque tous les échecs industriels. Ce sont deux inventaires distincts, sans correspondance établie.
  - Traitement : Section 43.7 : « les échecs industriels découlent presque toujours de sept antipatterns » devient une liste présentée comme proposition non validée, sans correspondance établie avec la taxonomie MAST (quatorze modes d'échec, surtout de conception et de coordination, section 43.3).

Ce qui reste, selon l'agent d'alignement : Le relevé prête au volet que 85 % des flux « se situent » en N3 et N4 : le volet les donnait comme optimum de ces niveaux; le chiffre n'a de source nulle part et a été retiré. Les incohérences internes signalées (amnistie de 30 jours contre trois semaines, DECOMMISSION du fil rouge) sont laissées, l'exposé ne tranchant pas. Hors relevé, l'encadré sectoriel M&A garde deux chiffres généraux sans source dans l'exposé (« trois à cinq ans », « huit semaines »); je ne les ai pas touchés.

## Chapitre 44 — Plan de données d'inférence et routage cognitif

### Volet « Plan de données AI-natif, passerelles et routage cognitif hybride »

- **Nature du troisième palier** — *corrigé*
  - Exposé : Section 44.3 : l'échelle à trois paliers est une cible de conception, non un schéma établi; le calcul au moment de l'inférence est un second axe (l'effort), non un échelon au-dessus du grand modèle, et il ne rattrape pas un problème hors de portée du modèle.
  - Volet, avant alignement : Le palier 3 est une catégorie de modèles à calcul au moment de l'inférence, échelon supérieur d'une escalade SLM, LLM, calcul au moment de l'inférence (formule du palier minimal sur {1,2,3}, tableau des paliers, code du routeur).
  - Traitement : Le texte courant ne présente plus le palier 3 comme une catégorie de modèles ni comme un échelon : synthèse (cible de conception, « calcul au moment de l'inférence »), intro et puce du palier 3 de la section 44.8 (second axe, l'effort, qui ne rattrape pas un problème hors de portée du modèle), et phrase d'avertissement avant la formule, le tableau et l'Extrait 44.2, qui restent intacts (section 44.3).
- **Activation du routage et palier par défaut** — *corrigé*
  - Exposé : Sections 44.3 et grille de décision : le routage s'active par classe de tâche, avec une règle explicite par défaut; une classe inconnue va au palier supérieur.
  - Volet, avant alignement : Le routage repose sur un score de complexité et un nombre d'outils (code : SLM si complexité inférieure à 0.42 et au plus 4 outils), et l'ADR-014 fait du palier 1 (SLM) la cible par défaut de tout flux.
  - Traitement : La décision de l'ADR-014 (« cible par défaut le palier 1 SLM ») devient un routage par classe de tâche, palier 1 là où une règle explicite l'établit et palier supérieur pour toute classe inconnue (section 44.3); une phrase avant l'Extrait 44.2 signale que le code arbitre sur un score de complexité et un nombre d'outils, alors que l'exposé active le routage par classe de tâche.
- **Rôle et nom d'Agent Router** — *corrigé*
  - Exposé : Section 44.2 : Agent Router est le nouveau nom d'Envoy AI Gateway, une passerelle d'IA de l'AAIF bâtie sur Envoy, distincte d'agentgateway.
  - Volet, avant alignement : Envoy AI Gateway est cité comme passerelle distincte (synthèse, 44.7), et « Agent Router » désigne un module de routage cognitif multicritère de la passerelle (44.8, tableau comparatif, ADR).
  - Traitement : Agent Router est rétabli comme nouveau nom d'Envoy AI Gateway, passerelle de l'AAIF distincte d'agentgateway (synthèse et section 44.7, avec renvoi à la section 44.2); le « module Agent Router » devient « routeur cognitif » dans l'intro de 44.8, la ligne « Routage intelligent » du tableau comparatif et l'option 3 de l'ADR; le titre de l'ADR est inchangé.
- **Version d'API de l'extension d'inférence** — *avertissement*
  - Exposé : Section 44.2 : le site de l'extension publie une référence d'API v1 à côté de v1alpha1; le statut de v1 n'est pas précisé.
  - Volet, avant alignement : L'Extrait 44.3 utilise inference.networking.x-k8s.io/v1alpha2 pour InferencePool et InferenceModel.
  - Traitement : Le manifeste de l'Extrait 44.3 est inchangé; la phrase d'introduction signale qu'il utilise v1alpha2, alors que le site de l'extension publie une référence d'API v1 à côté de v1alpha1, sans préciser le statut de v1 (section 44.2).
- **Grandeurs de latence mesurées** — *nuance*
  - Exposé : Section 44.6 : TTFT, débit et taux de succès du cache se mesurent par classe de tâche, à la médiane et au 99e centile.
  - Volet, avant alignement : Le TTFT est exprimé au p95 (indicateurs de la synthèse, tableau des paliers, fil rouge).
  - Traitement : Le p95 est conservé (synthèse, tableau des paliers, fil rouge), avec une mention en synthèse et une phrase avant le tableau précisant que l'exposé retient la médiane et le 99e centile, par classe de tâche (section 44.6); les chiffres du fil rouge ne sont pas touchés.
- **Niveau de preuve des gains du cache KV** — *corrigé*
  - Exposé : Section 44.5 : les gains chiffrés de l'ordonnancement conscient du cache et de la désagrégation viennent de llm-d et de ses contributeurs, avec le tourniquet comme base la plus faible; aucune évaluation indépendante n'a été trouvée.
  - Volet, avant alignement : Le volet avance sans source des chiffres comme jusqu'à 80 % des FLOPS gaspillés et une latence triplée en tourniquet, un rechargement de huit à douze fois plus rapide que le recalcul, et un succès du cache de 19 % à 88 % (cas Boréal).
  - Traitement : Section 44.9 : « 80 % des FLOPS gaspillés, latence triple » est remplacé par les chiffres de l'exposé (débit de sortie triplé, TTFT deux fois plus court, Tesla et Red Hat, tourniquet comme base la plus faible, aucune évaluation indépendante; section 44.5); le « huit à douze fois plus rapide » du délestage est retiré, l'exposé n'en rapportant aucun gain; le 94 % de l'encadré télécoms devient une annonce sans évaluation indépendante; le 19 % à 88 % du cas Boréal est laissé (fiction).
- **Origine de l'Endpoint Picker** — *avertissement*
  - Exposé : Section 44.5 : le site de l'extension réserve son EPP léger aux tests de conformité et renvoie la production vers un EPP existant, tel celui de llm-d.
  - Volet, avant alignement : L'Extrait 44.3 déclare un EPP propre au Groupe Boréal (boreal-kv-aware-epp) avec ses poids de notation et ses seuils de saturation.
  - Traitement : Le manifeste de l'Extrait 44.3 est inchangé; la phrase d'introduction signale que boreal-kv-aware-epp est propre au Groupe Boréal, alors que le site de l'extension réserve son EPP léger aux tests de conformité et renvoie la production vers un EPP existant, tel celui de llm-d (section 44.5).

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme » (3970 à 4336 mots, 109 %); seul le volet a été modifié, 15 lignes touchées, sans toucher au code, aux figures, aux formules, aux titres d'extraits ni à la syntaxe des encadrés. Les contradictions internes du relevé (70 à 80 % contre 70 à 78 %, 150 ms contre 45 à 160 ms, L2 contre L3/L4, 4096 contre 6000 jetons, « trois problèmes » pour quatre puces) sont laissées, l'exposé ne tranchant pas. Hors relevé et non traités : « écrits en Rust », « ont émergé en 2026 » (44.7), « En production, 70 à 80 % » et « 3 à 7 % » (44.8), que l'exposé ne confirme pas.

## Chapitre 45 — Réseaux B2B fédérés et négociation entre agents

### Volet « Maillages B2B inter-entreprises, espaces de données et négociation multi-parties »

- **Rôle du justificatif OOR pour un agent** — *corrigé*
  - Exposé : 45.3 : le justificatif OOR atteste qu'une personne occupe une fonction officielle et n'est prévu pour aucun agent logiciel; l'agent porte une délégation distincte, bornée et révocable (le justificatif ECR en est le support le plus proche); l'extension aux agents est une orientation de la GLEIF; l'acceptation du vLEI par un espace de données n'est pas vérifiée.
  - Volet, avant alignement : Le justificatif OOR, couplé au vLEI, établit qu'un agent précis agit au nom de l'entreprise dans les limites d'une délégation (strate 1 de 45.8; `OOR:VP_SUPPLY_CHAIN_DELEGATE` dans l'Extrait 45.2; point 1 de la liste de contrôle). La décision (a) de l'ADR-026 exige le vLEI sur tout canal B2B mutatif.
  - Traitement : Dans la strate 1 de 45.8, le texte dit désormais que le justificatif d'entité établit la contrepartie, que l'OOR établit le dirigeant qui peut l'engager et que l'agent agit sous une délégation distincte, bornée et révocable, avec la précision que rien ne prévoit l'émission d'un OOR à un agent et que l'acceptation du vLEI n'est pas vérifiée (section 45.3). Le point 1 de la liste de contrôle est reformulé dans le même sens. Une phrase d'avertissement précède l'Extrait 45.2, dont le champ `OOR:VP_SUPPLY_CHAIN_DELEGATE` reste intact. La décision (a) de l'ADR-026 est gardée, avec une phrase de nuance avant l'encadré : elle va au-delà du vLEI « si le réseau l'accepte » que retient l'exposé.
- **Application des politiques ODRL** — *corrigé*
  - Exposé : 45.2 : ODRL exprime et n'applique rien; retirer un accord n'efface pas une copie des données; le respect de l'accord dépend du consommateur et du contrat.
  - Volet, avant alignement : La politique ODRL « interdit techniquement » l'ingestion pour l'entraînement, la rétention et la retransmission; le tableau de 45.8 parle d'un contrat ODRL « appliqué par le connecteur EDC »; la synthèse parle de politiques d'usage « exécutables ».
  - Traitement : « Interdit techniquement » devient « exprime l'interdiction », suivi d'une phrase (section 45.2) : ODRL n'applique rien, retirer un accord n'efface pas une copie, le respect dépend du consommateur et du contrat. « Exécutables » est retiré de la synthèse et remplacé par une mention que ODRL exprime sans appliquer. Dans le tableau de 45.8, « appliqué par le connecteur EDC » devient « négocié et surveillé par le connecteur EDC; le respect dépend du consommateur et du contrat ».
- **Moment d'émission du mandat AP2** — *corrigé*
  - Exposé : 45.7 : le mandat de paiement ne s'émet qu'après un rapprochement à trois voies réussi.
  - Volet, avant alignement : 45.10 : le `CartMandate` AP2 est émis à l'issue de la négociation, comme séquestre logique, et crée le bon de commande; seule la libération du paiement attend le rapprochement.
  - Traitement : À l'étape 1 de 45.10, le `CartMandate` devient un mandat contractuel (sans l'étiquette AP2), qui crée le bon de commande sans émettre de mandat de paiement AP2, et le texte renvoie à la section 45.7 : le mandat de paiement ne s'émet qu'après un rapprochement réussi. L'étape 4 place l'émission du mandat de paiement AP2 après la concordance, juste avant la libération de l'ordre de paiement.
- **Traitement du micropaiement x402** — *corrigé*
  - Exposé : 45.7 : le micropaiement x402, où le service est rendu dans la réponse qui suit le paiement, échappe au rapprochement préalable; on le traite par un portefeuille dédié et plafonné et un rapprochement a posteriori.
  - Volet, avant alignement : 45.10 et point 7 de la liste de contrôle : le règlement x402 (en-tête, ou jeton sur compte pré-provisionné) est subordonné au rapprochement à trois voies avant sa libération.
  - Traitement : À l'étape 3 de 45.10, le x402 sort de la liste des demandes soumises au rapprochement préalable, et une phrase dit que le micropaiement x402 échappe à ce rapprochement et passe par un portefeuille dédié et plafonné avec rapprochement a posteriori (section 45.7). La mention x402 est retirée de l'étape 4, la synthèse (décision 3) et le point 7 de la liste de contrôle sont alignés, et une phrase de nuance avant l'ADR dit que la décision (c) et l'option retenue valent hors micropaiement x402.
- **Portée des protections annoncées** — *corrigé*
  - Exposé : 45.4 : la scission Diplomate / Évaluateur interne est une cible de conception, sans source, qui ne suffit pas (les concessions révèlent le prix de réserve). 45.6 : aucune défense éprouvée contre la collusion; les mesures sont des précautions. 45.7 : un paiement indu se traite par compensation.
  - Volet, avant alignement : Le fil rouge rapporte 0 % de fuite; l'ADR-026 promet une protection du secret d'affaires et l'élimination de la fraude à la facturation autonome; l'encadré sectoriel présentait deux règles comme suffisantes pour un maillage « irréprochable » (formulation neutralisée dans la réécriture, la portée du propos étant inchangée).
  - Traitement : Dans les conséquences de l'ADR-026, « élimination de la fraude à la facturation autonome » devient une réduction du risque de paiement indu, que le rapprochement ne supprime pas (compensation, section 45.7), et la protection du secret d'affaires est limitée à la divulgation directe, les concessions révélant encore le prix de réserve (section 45.4). Les 0 % de fuite du fil rouge sont laissés (fiction). L'encadré sectoriel ne parle plus d'« irréprochable » : sans objet.

Ce qui reste, selon l'agent d'alignement : Seul `Master/fusion/reecrit/chapitre-45-volet-a.md` est modifié; le contrôle répond « conforme » (102 %). Deux points à relire. Le renommage du `CartMandate` en mandat contractuel interprète le volet : l'exposé ne définit pas cet objet, et le tableau et le code (`MandateTerms`, « mandat signé ») gardent le mot « mandat » pour la première voie. Deux autres affirmations d'adoption, hors du relevé, n'ont pas été traitées : « déployé ... en 2027 » dans l'introduction des quatre strates de 45.8, et « vLEI et rôle OOR vérifiables instantanément » dans le tableau. Les contradictions internes signalées (Groupe Boréal Synergie Inc. contre Groupe Boréal Inc.) sont laissées, l'exposé ne tranchant pas.

## Chapitre 46 — Inférence confidentielle, résilience et IA physique

### Volet « Souveraineté cognitive, portabilité multi-cloud et reprise après sinistre cognitif »

- **Décompte et contenu des « six substrats d'état »** — *corrigé*
  - Exposé : Section 46.1 : la grille compte six états (modèle et configuration, contexte en cours d'inférence, mémoire persistante, état d'exécution durable, traces et journaux d'audit, secrets). La section « Limites » précise que « six substrats d'état » n'a été retrouvé nulle part et que la grille est une proposition sans source.
  - Volet, avant alignement : Six couches différentes (journal du moteur durable, mémoire, KV-cache, files d'événements, observabilité, journaux du fournisseur de modèle), reprises comme un décompte établi dans l'ADR (« 6 couches ») et la liste de contrôle (« 6 substrats »).
  - Traitement : Dans l'introduction de 46.9, le volet dit maintenant que la grille de la section 46.1 est une proposition sans source qui compte six états autrement composés, que les six couches listées sont un inventaire proposé et non un décompte établi, et que « six substrats d'état » ne se retrouve dans aucune source; l'ADR (option 3) et le premier point de la liste de contrôle renvoient désormais à l'inventaire proposé de la section 46.9.
- **Portée des TEE et résistance à une injonction extraterritoriale** — *corrigé*
  - Exposé : Sections 46.1 et 46.2 : géorepérage, clés détenues et TEE réduisent ce qu'un exploitant peut remettre sans constituer une réponse juridique. Un TEE élève le coût de l'accès sans le rendre impossible (TEE.fail : attestations forgées, rapports GPU relayables, sécurité physique seule parade).
  - Volet, avant alignement : Tableau des modèles de clés : résistance « Maximale (isolation matérielle prouvée) » et visibilité « Nulle » pour HYOK avec enclave TEE. Synthèse : l'exploitant ne peut inspecter ni consignes, ni poids, ni tenseurs. ADR : conformité « démontrable ». Section 46.10 : une réquisition adressée à l'hébergeur de l'orchestrateur n'obtient que des blocs opaques.
  - Traitement : Synthèse (décision 2) : seuls les logiciels et les administrateurs de l'exploitant sont retirés de la base de confiance, et le TEE élève le coût de l'accès sans le rendre impossible (section 46.2); tableau des modèles de clés : visibilité « nulle pour les logiciels et les administrateurs de l'hébergeur » et résistance « la plus élevée du tableau, non absolue » au lieu de « Maximale (isolation matérielle prouvée) »; section 46.10 : la réquisition n'obtient « que ces blocs » devient ce que l'hébergeur peut remettre, avec rappel que les clés détenues ne sont pas une réponse juridique (section 46.1); ADR : « Conformité souveraine démontrable » remplacée par une réduction de ce que l'exploitant peut remettre, sans valoir réponse juridique.
- **Rôle de HYOK** — *nuance*
  - Exposé : Section 46.3 : HYOK est un levier de révocation, pas une barrière pendant le traitement. Pour la plupart des charges, le risque pour la disponibilité dépasse le bénéfice. Grille de décision : HYOK réservé aux classes de données qui l'exigent.
  - Volet, avant alignement : Tableau : visibilité de l'hébergeur « Nulle sur les PII » attribuée à « HYOK + pseudonymisation amont », sans mention du coût de disponibilité. L'ADR exige HYOK pour les classes C2 et C3, ce qui reste compatible avec la grille.
  - Traitement : Paragraphe ajouté avant le tableau des modèles de clés en 46.10 : la visibilité nulle sur les PII vient de la pseudonymisation en amont, HYOK seul est un levier de révocation et non une barrière pendant le traitement, et selon AWS le risque pour la disponibilité dépasse le bénéfice pour la plupart des charges (section 46.3); la grille de décision réserve HYOK aux classes qui l'exigent, ce qui reste compatible avec l'exigence de l'ADR-027 pour C2 et C3.
- **Seuil RTO de 15 minutes** — *corrigé*
  - Exposé : Section 46.4 : le seuil n'a pas de source. Il n'est plausible que pour le reroutage vers un modèle déjà qualifié. C'est une cible de conception à fixer par classe de tâche et à valider par exercice.
  - Volet, avant alignement : Le seuil est présenté comme exigé en résilience prudentielle (BSIF E-23), bloquant en CI/CD (ADR) et mesuré à 11 minutes et 14 secondes lors de l'exercice, sans distinction du reroutage et de la requalification.
  - Traitement : Synthèse : libellé « Exigée en résilience prudentielle » remplacé par « Cible de conception en résilience prudentielle », « bascule » devient « vise une bascule » et une phrase dit que le seuil n'a pas de source et se fixe par classe de tâche puis se valide par exercice (section 46.4); avertissement ajouté avant la formule de RTO_cog (plausible seulement pour le reroutage vers un modèle déjà qualifié, la requalification étant une seconde horloge); l'ADR (option 3) et le point 8 de la liste de contrôle présentent le seuil comme cible à mesurer; la formule, le fil rouge (11 min 14 s) et le code sont intacts.
- **Emplacement du modèle de secours** — *nuance*
  - Exposé : Section 46.4 : modèle de secours chez un autre exploitant, par classe de tâche, et autohébergé pour les classes critiques.
  - Volet, avant alignement : Le secours est toujours une grappe souveraine à poids ouverts (synthèse, piliers, ADR), sans option chez un autre exploitant.
  - Traitement : Phrase ajoutée à la fin de l'introduction de 46.11 : le secours toujours souverain à poids ouverts va au-delà de la section 46.4, qui retient un modèle de secours par classe de tâche, chez un autre exploitant, et autohébergé pour les classes critiques; synthèse, piliers et ADR sont laissés tels quels.

Ce qui reste, selon l'agent d'alignement : Contrôle « conforme » (4421 à 4655 mots). Non traités, hors relevé : la phrase de 46.10 sur le calcul confidentiel GPU « arrivé à maturité » sur Hopper et Blackwell, que l'exposé ne confirme pas (il n'a lu que la vue d'ensemble de NVIDIA), et le rapport d'attestation « signé par sa racine silicium », que TEE.fail met en cause (section 46.2). Les incohérences internes (pass^5 à 0,94 contre plancher de 0,90 dans le code, exercice « annuel » de l'encadré sectoriel contre trimestriel ailleurs, 96,4 % du fil rouge) sont laissées : l'exposé ne les tranche pas. L'ADR et le premier point de la liste de contrôle ont reçu un court renvoi à la section 46.9 pour ne plus présenter « 6 » comme un décompte établi.

### Volet « Orchestration en périphérie, opérations déconnectées et passerelles vers l'IA physique »

- **Seuil de 72 heures d'autonomie** — *corrigé*
  - Exposé : Section 46.5 et « Limites de ce chapitre » : le seuil de 72 h n'a pas de source; la durée de survie se déduit du plus court de plusieurs délais (jetons, certificats, journal local, quotas) et se calcule par site.
  - Volet, avant alignement : Synthèse, tableau, paliers 0-24 h, 24-72 h et au-delà de 72 h, ADR (a) et liste de contrôle : 72 h garanties comme minimum exigé pour tout site critique, avec repli automatique en L1 au-delà.
  - Traitement : Dans la synthèse, « autonomie garantie ≥ 72 h » devient une durée de survie calculée par site et vérifiée par essai, avec 72 h comme cible sans source (section 46.5); même reformulation pour le point 1 de la liste de contrôle; phrases d'avertissement (section 46.5) avant la figure, le tableau des profils de nœud, les paliers de gradation et l'extrait 46.6; l'ADR-028 (a) est gardé, avec une nuance disant qu'il va au-delà de la section 46.5; fil rouge laissé tel quel.
- **Simplex, certification et conformité aux normes** — *corrigé*
  - Exposé : Section 46.7 : Simplex est un patron d'architecture, non une voie de certification; rien n'établit qu'il confère la conformité à l'ISO 10218 ou à l'IEC 61508.
  - Volet, avant alignement : Parle d'un « pont certifiable », d'un contrôleur de repli certifié (SIL 3 / PL d), d'une architecture « sous normes » ISO 10218, ISO 3691-4 et IEC 61508, et d'une sûreté des personnes garantie (ADR, conséquences).
  - Traitement : « Certifié » et « certifiable » deviennent « vérifié » (synthèse, pont de la section 46.15, contrôleur de repli, ADR-028 (c)); « SIL 3 / PL d » est présenté comme niveau visé; une phrase (section 46.7) rappelle que Simplex est un patron d'architecture, non une voie de certification, dans la synthèse et avant le tableau des couches; dans l'ADR-028, « sûreté des personnes garantie » est ramenée à un contrôleur vérifié et isolé, et « non-conformité aux normes » à l'absence d'enveloppe vérifiée (section 46.7).
- **Édition de l'ISO 10218** — *corrigé*
  - Exposé : Section 46.7 : seule l'ISO 10218-1:2025 (troisième édition, février 2025) est connue; l'intégration relève de l'ISO 10218-2.
  - Volet, avant alignement : Cite « ISO 10218-1/2:2025 » pour la cellule articulée, donc une édition 2025 de la partie 2 aussi.
  - Traitement : « ISO 10218-1/2:2025 » devient « ISO 10218-1:2025; l'intégration relève de l'ISO 10218-2, section 46.7 » dans la couche 3 de la section 46.15; l'intitulé gras de cette couche passe de « ISO 10218:2025 » à « ISO 10218-1:2025 ».
- **Retour arrière d'une mise à jour** — *relevé inexact*
  - Exposé : Section 46.8 : le client refuse toute métadonnée de version inférieure; un retour arrière se livre comme une nouvelle version au contenu ancien.
  - Volet, avant alignement : Activation A/B : en cas d'échec, le chien de garde matériel rebascule automatiquement sur la partition A précédente, sans livraison d'une nouvelle version.
  - Traitement : Rien n'a changé : la règle de l'exposé (section 46.8) porte sur les métadonnées TUF, que le client refuse si leur version est inférieure, alors que le volet décrit un rebasculement local du chien de garde sur la partition A déjà installée, mécanisme que l'exposé n'aborde pas; le volet ne dit nulle part « sans livraison d'une nouvelle version ».

Ce qui reste, selon l'agent d'alignement : Le contrôle répond « conforme »; seul chapitre-46-volet-b.md est modifié. Le relevé ne citait ni la figure ni l'extrait 46.6 pour le seuil de 72 h, ni l'option 2 de l'ADR-028 pour la « non-conformité aux normes »; je les ai traités par cohérence avec le même sujet. Le rejet du point 4 est un jugement : un relecteur qui juge ambigu l'intitulé « retour arrière automatique » pourrait ajouter une phrase renvoyant à la section 46.8. Laissés faute d'arbitrage par l'exposé : les écarts de watts, L1 contre L1/L2, la limite de 24 h, les « rôles » de signature du volet comparés aux rôles TUF de la section 46.8, et les dates 2027 du fil rouge.

## Chapitre 47 — Ingénierie agentique interne et distillation

### Volet « Usine logicielle agentique (Agentic SDLC) et modernisation assistée du patrimoine »

- **Seuil de mutation** — *corrigé*
  - Exposé : 47.3 : le seuil « score de mutation ≥ 85 % » n'a pas de source; un score global est le mauvais objet (mutants équivalents). Il faut le calculer sur le code modifié, le calibrer par module et exclure les mutants équivalents reconnus. Grille de décision : « Jamais un seuil global unique ».
  - Volet, avant alignement : Seuil unique d'au moins 85 % de mutants tués sur tout code généré, repris dans la synthèse, le portier, le tableau des garde-fous, l'ADR et la liste de contrôle. Le volet reprend deux des trois conditions (code modifié, élagage des mutants équivalents), pas la calibration par module.
  - Traitement : Le seuil de 85 % est signalé comme sans source et ramené aux trois conditions de la section 47.3 (code modifié, calibré par module à partir du score observé avant les agents, mutants équivalents exclus), dans la synthèse, le portier, le tableau des garde-fous, l'option 3 de l'ADR et le point 4 de la liste de contrôle.
- **Fenêtre et critère de l'exécution en miroir** — *corrigé*
  - Exposé : 47.4 : « 30 jours à 0,00 $ d'écart » n'a pas de source. La forme (écart nul) se défend, la durée se discute : la fenêtre doit couvrir au moins un cycle d'affaires complet, clôture périodique comprise; trente jours couvrent une fin de mois, pas une fin d'exercice. Chaque écart ignoré est une décision signée.
  - Volet, avant alignement : Trente jours, au moins un cycle mensuel complet (fin de mois incluse), au moins 100 000 transactions, écart nul. Présenté comme standard de référence du compendium, avec 0,00 $ « prouvé sur 30 j »; aucune mention de la fin d'exercice ni des écarts ignorés signés.
  - Traitement : Le « cycle mensuel » devient un cycle d'affaires complet, clôture périodique comprise; 30 jours et 0,00 $ sont donnés comme cibles de conception sans source (trente jours couvrent une fin de mois, pas une fin d'exercice) et chaque écart ignoré est une décision signée (section 47.4); « 0,00 $ constaté sur 30 j » devient une cible au tableau, et la synthèse et le point 7 de la liste de contrôle sont ajustés.
- **Exécution en miroir et écritures** — *nuance*
  - Exposé : 47.4 (Scientist) : la technique n'est sûre que pour du code qui ne modifie pas de données; pour les écritures, double écriture puis comparaison à la lecture. Sur un traitement par lots, exécution parallèle sur le même fichier d'entrée, sorties rapprochées enregistrement par enregistrement.
  - Volet, avant alignement : Le nouveau service s'exécute sur le trafic réel en parallèle du programme IBM i, « sans commettre ses écritures »; le comparateur compare l'intention d'écriture transactionnelle dans un mode d'essai à blanc isolé. Aucune double écriture avec comparaison à la lecture avant le passage en maître.
  - Traitement : Dans la section 47.11, après la description du comparateur en essai à blanc, deux phrases rappellent la limite de la section 47.4 (sûre seulement sans modification de données; double écriture puis comparaison à la lecture; exécution parallèle sur le même fichier d'entrée pour les lots) et disent que l'essai à blanc est une variante propre au volet.
- **Index SCIP pour le patrimoine** — *corrigé*
  - Exposé : 47.2 : la liste d'indexeurs SCIP lue ne contient ni COBOL ni RPG; pour ces langages, l'index vient de l'outillage de l'éditeur ou n'existe pas. 47.4 : aucune source lue ne traite RPG.
  - Volet, avant alignement : L'analyse d'impact et la modernisation du patrimoine RPG, COBOL et PL/SQL reposent sur un graphe AST / SCIP (synthèse, liste de contrôle, conséquences de l'ADR). Le découpage par domaine passe par un parseur ANTLR / Tree-sitter spécialisé RPG/COBOL, sans lien établi avec un indexeur SCIP.
  - Traitement : Dans la synthèse, la liste de contrôle et les conséquences de l'ADR, SCIP ne vaut que là où un indexeur existe; la section 47.10 ajoute que, pour COBOL et RPG, l'index vient de l'outillage de l'éditeur ou n'existe pas (section 47.2) et que RPG n'est traité par aucune source lue (section 47.4).
- **Statut de la séparation des rôles** — *corrigé*
  - Exposé : 47.1 : la séparation en deux rôles (spécificateur, bâtisseur) à droits distincts est une extrapolation à valider; le spécificateur lit le besoin et le code; le passage de l'un à l'autre est un point d'approbation humaine.
  - Volet, avant alignement : Quatre rôles cloisonnés (spécificateur et auteur d'oracle, bâtisseur, portier, critique), ADR-029 « Acceptée »; le spécificateur ne voit jamais le code d'implémentation candidat; la signature humaine intervient à la fusion, pas entre spécification et construction.
  - Traitement : La section 47.9 présente la séparation en deux rôles comme une extrapolation à valider avec approbation humaine entre les deux (section 47.1, chapitre 22), dit que les quatre rôles et la signature à la fusion vont au-delà de l'exposé, et le statut de l'ADR devient « Acceptée (… extrapolation à valider; section 47.1) »; la règle « le spécificateur ne voit jamais le code candidat » est laissée, car compatible avec les sections 47.1 et 47.3.

Ce qui reste, selon l'agent d'alignement : Seul Master/fusion/reecrit/chapitre-47-volet-a.md est modifié (16 lignes); code, figures, formules, titres d'extraits et titre de l'ADR sont intacts, et le contrôle répond « conforme » (104 % de l'original). Laissés faute d'arbitrage par l'exposé : 85 % dans le texte contre minMutationKillScore 0.88 dans l'Extrait 47.2, 100 000 transactions et 10 000 à 100 000 cas (sans source dans l'exposé), 50 000 contre 60 000 cas, 1,5 contre 1,4 million de lignes, et les chiffres « ×5 », « échec > 70 % », « 8 % », « 250 lignes ». Je n'ai pas touché non plus au verdict « Standard de référence du compendium », à l'amorce ANTLR / Tree-sitter de l'étape 1, ni à PL/SQL (que l'exposé ne nomme pas parmi les langages sans indexeur SCIP).

### Volet « Agentic DataOps, contrats de données auto-réparateurs et SRE autonome »

- **Version d'ODCS** — *avertissement*
  - Exposé : 47.5 : la version est 3.2.0 selon le chapitre 15, une 4.0.0 étant annoncée.
  - Volet, avant alignement : L'Extrait 47.4 (code repris à l'identique) déclare apiVersion odcs.bitol.io/v3.0.1; le texte parle d'« ODCS v3 ».
  - Traitement : Le bloc de l'Extrait 47.4 reste intact (il déclare la v3.0.1); une phrase ajoutée juste avant le bloc signale que l'exposé retient la version 3.2.0 selon le chapitre 15, une 4.0.0 étant annoncée (section 47.5); le texte « ODCS v3 » est laissé, car compatible avec la 3.2.0.
- **Isolement d'une rupture de schéma par la branche** — *avertissement*
  - Exposé : 47.5 : le schéma de la table vaut pour toutes les branches; une branche n'isole pas un changement de schéma.
  - Volet, avant alignement : Traite la rupture de schéma sur la branche d'audit : le contrat prévoit driftOrSchemaBreak = FREEZE_BRANCH_AND_SIGNAL_STALE, ce qui suppose que la rupture reste isolée.
  - Traitement : Le champ driftOrSchemaBreak du YAML reste intact; une phrase ajoutée avant l'Extrait 47.4 précise que, selon l'exposé, le schéma de la table vaut pour toutes les branches et qu'une branche n'isole pas un changement de schéma (section 47.5).
- **Balisage des champs libres des journaux** — *corrigé*
  - Exposé : 47.6 : une consigne de ne rien exécuter laisse un modèle exécuter dans 30 % des essais; il ne faut pas compter sur le filtre, les garde-fous de contenu étant contournés ou inadaptés; seules tiennent les mesures architecturales.
  - Volet, avant alignement : Les champs libres sont encapsulés dans des balises `<untrusted_external_input>` qui « interdisent toute interprétation prescriptive », et trois verrous (dont ce balisage) « neutralisent » l'attaque.
  - Traitement : Dans la section 47.15, « neutralisent » devient « encadrent », et les balises <untrusted_external_input> ne « interdisent » plus l'interprétation : elles signalent un contenu non fiable, avec le rappel de l'exposé (consigne de ne rien exécuter : un modèle exécute encore dans 30 % des essais; ne pas compter sur le filtre; seules tiennent les mesures architecturales, section 47.6).

Ce qui reste, selon l'agent d'alignement : Seul le volet réécrit a été modifié; le contrôle répond « conforme » (102 % du volume d'origine). Dans le troisième point, j'assimile le balisage à une consigne pour le rattacher au résultat de 30 % de l'exposé : c'est une inférence que le relecteur peut vouloir confirmer. Les contradictions internes signalées dans les remarques du relevé (PSI 0,25 contre 0,20, 88 % contre le 85 % hors volet, paliers R1, « trois à quatre » sous-agents, 1,3 % gelé au fil rouge) sont laissées, l'exposé ne les tranchant pas; le fil rouge, qui parle d'un changement de format JSON intercepté sur la branche, relève de la fiction et reste inchangé.

### Volet « Volants d'inertie cognitifs, compilation de consignes et distillation LLM → SLM »

- **Chargement des adaptateurs en production** — *relevé inexact*
  - Exposé : 47.8 : un adaptateur se charge au démarrage plutôt qu'à chaud; le chargement à chaud de vLLM est déconseillé en production hors environnement isolé.
  - Volet, avant alignement : La promotion par déploiement canari (10 % puis 100 %) conserve l'adaptateur N-1 en VRAM pour un retour arrière en moins de 5 s, et les adaptateurs périmés sont décommissionnés automatiquement; cela suppose des chargements et déchargements à l'exécution, sans que le volet dise s'il s'agit du chargement à chaud.
  - Traitement : Rien modifié : le volet ne parle jamais de chargement à chaud; conserver l'adaptateur N-1 en VRAM, router le canari de 10 % à 100 % et décommissionner « au profit du palier supérieur » (repli vers l'enseignant) ne suppose aucun chargement à l'exécution et reste compatible avec le chargement au démarrage de la section 47.8.
- **Référence de mesure de l'élève** — *nuance*
  - Exposé : 47.8 : l'élève se mesure sur le banc interne du chapitre 33, pas contre l'enseignant.
  - Volet, avant alignement : La porte de promotion exige un ratio de constance pass^5 de l'élève sur celle de l'enseignant d'au moins 0,99, et l'échantillon sentinelle de 2 % mesure le taux d'accord de l'élève avec l'enseignant en production.
  - Traitement : Une phrase ajoutée à la fin du point « Échantillonnage sentinelle » de 47.20 : le ratio de la porte de promotion et le taux d'accord situent l'élève par rapport à l'enseignant, ce qui va au-delà de la section 47.8, où l'élève se mesure sur le banc interne du chapitre 33, pas contre l'enseignant, dont il hérite les erreurs.
- **Statut de la recette Multi-LoRA (SFT + DPO)** — *avertissement*
  - Exposé : 47.8 et Limites : composition de briques sourcées séparément, cible de conception à valider; aucune mesure lue sur un élève distillé par cette recette.
  - Volet, avant alignement : La recette est tenue pour décidée (ADR-031 acceptée), avec des volumes et des résultats chiffrés (parité 97,2 % contre 97,4 %, baisse de 68 % du coût par résultat), présentés comme vérifiés.
  - Traitement : Deux phrases ajoutées dans le texte courant : avant le tableau comparatif de 47.20 (chiffres présentés comme illustration d'une cible de conception, recette à valider, aucune mesure lue sur un élève distillé, section 47.8) et après la phrase d'ouverture de 47.22 devant l'ADR-031 (recette qui reste une cible de conception à valider); le statut « Acceptée », le titre de l'ADR et les chiffres du fil rouge (« vérifié ») sont laissés, car relevant de la décision et de la fiction du Groupe Boréal.
- **Protocole d'exposition des canaris** — *nuance*
  - Exposé : 47.7 et Limites : le résumé lu de l'article de Carlini ne décrit ni les canaris ni la métrique d'exposition; la description vient de la connaissance générale.
  - Volet, avant alignement : Le volet prescrit un protocole précis (K = 200 canaris, 10 000 témoins, comparaison des rangs de vraisemblance, seuil d'exposition, décodage glouton) attribué à la méthode d'exposition de Carlini.
  - Traitement : Une phrase ajoutée à la fin du deuxième paragraphe de « Test d'exposition des canaris » : le protocole détaillé va au-delà de la section 47.7 (canari = séquence artificielle unique glissée dans le jeu d'entraînement, exposition mesurée dans le modèle, publication bloquée s'il ressort), le résumé lu de Carlini ne décrivant ni les canaris ni la métrique, et le nombre de canaris et de témoins, le seuil et le décodage n'étant décrits dans aucune source lue.

Ce qui reste, selon l'agent d'alignement : Contrôle conforme (96 %), quatre lignes touchées dans le seul volet, rien d'autre. Sur la divergence 2, je n'ai pas touché au code ni aux libellés de la porte pass^5 : la parité compare deux scores mesurés sur le jeu de réserve scellé, mais l'exposé ne mentionne ni τ-bench ni pass^k, et rien ne dit que ce jeu est le « banc interne du chapitre 33 » (déduction, non vérifiée). Non traités, hors relevé : « un élève 8B distillé peut y égaler ou surpasser un modèle géant » (47.20) n'est pas confirmé par l'exposé, et les contradictions internes signalées par le relevé (200 contre 500 canaris, seuils de latence, 82/85/86 %) sont laissées, l'exposé ne les tranchant pas.

## Ouverture et annexes F à H

Ces quatre textes n'ont pas d'exposé jumeau. Ils ont été réécrits dans le ton des exposés. L'ouverture a en plus été alignée sur les exposés des chapitres 1, 4 et 11; le glossaire de l'annexe H renvoie à l'annexe A pour les termes qui y sont déjà définis.

### Ouverture

Changements principaux :

- Ton ramené à celui de l'exposé : phrases courtes, emphase et métaphores retirées (« fracture brutale », « sans concession », « silos cognitifs bavards », « volant d'inertie », « archipel », « boussole »), formule d'annonce finale remplacée par une phrase affirmative.
- Termes français à la place des termes anglais (systèmes d'enregistrement, confiance zéro, coût par résultat, humain dans la boucle / sur la boucle, agents fantômes, ingénierie du contexte, coût de sortie, passerelles natives de l'IA); les noms de spécifications et de produits restent.
- Titres des sections 0.1 à 0.6 et des sous-sections ramenés à la forme sobre; numéros et ordre des sections inchangés, titre du chapitre et titres d'encadrés intacts.
- Gras limité aux amorces (listes, paragraphes, première cellule des lignes de tableau); amorces rédigées comme au chapitre 1.
- Les 36 lignes de tableau, les six parcours (séquences exactes de chapitres et d'annexes), la formule de Lusser, la figure et l'encadré fil rouge (tous les faits et chiffres) sont conservés; cellules resserrées, en-tête « Standard de production » devenu « Cible de production ».
- Alignement sur les chapitres 1, 4 et 11 : 17 corrections, nuances ou avertissements avec renvois de section; en 0.1, l'adoption est ramenée aux chiffres de la section 4.1 et au portrait de MAP (section 4.2).

Divergences traitées :

- **Statut de la thèse d'ouverture** — *corrigé*
  - Texte d'appui : Section 1.5 : la thèse est un argument, pas un constat; les deux conditions sont nécessaires par raisonnement, non démontrées par la mesure.
  - Texte, avant alignement : L'encadré d'ouverture présentait en « Constat fondamental » que la performance ne dépend plus du modèle mais du tissu conjonctif.
  - Traitement : Amorce « Point de départ »; l'affirmation devient « l'ouvrage soutient » et une phrase renvoie à la section 1.5 (argument, non constat).
- **Adoption des agents en 2026 et capacités des systèmes déployés** — *corrigé*
  - Texte d'appui : Section 4.1 : 40 % des organisations d'au moins 1 G$ US ont mis des agents à l'échelle dans au moins une fonction (27 % un an plus tôt), 22 % des plus petites, chiffres déclaratifs connus par un compte rendu de presse. Section 4.2 : agents en production étroits (68 % moins de dix étapes avant intervention humaine, 16 cas sur 20 en workflow prédéfini; collecte de 2025). Chapitre 4 : ce qui sépare pilote et production est la fiabilité, l'évaluation et les contrôles.
  - Texte, avant alignement : Disait que le centre de gravité avait basculé en 2026, que les organisations avaient franchi la frontière vers l'exécution autonome, que les systèmes déployés délèguent et maintiennent un état sur plusieurs jours, et qu'une « fracture brutale » était apparue au passage à l'échelle.
  - Traitement : Paragraphe réécrit : une partie des organisations a commencé à passer à l'action; chiffres de 4.1 et de 4.2 avec renvois; la cause pilote-production est celle du chapitre 4; l'état sur plusieurs jours est retiré.
- **Effectif de l'AAIF** — *avertissement*
  - Texte d'appui : Section 11.2 : huit membres platine; un décompte approximatif de logos donne une cinquantaine de membres or et environ deux cents membres argent; aucun total de plus de 300.
  - Texte, avant alignement : L'AAIF fédérerait « plus de 300 organisations membres fin 2026 ».
  - Traitement : Chiffre gardé au conditionnel; une phrase dit que le chapitre 11 ne le confirme pas et donne son propre décompte (section 11.2).
- **Consolidation des standards ouverts** — *corrigé*
  - Texte d'appui : Section 11.8 : convergence réelle à la couche des protocoles, absente à celle de l'identité (trois modèles de confiance, section 11.7). Section 4.4 : le socle MCP et A2A existe, mais registre MCP en préversion, identité sans profil adopté, conventions OpenTelemetry au statut « Development ». Section 11.2 : l'AAIF est un foyer neutre pour des projets, pas un organisme de normalisation.
  - Texte, avant alignement : Parlait d'une « consolidation historique » et d'une « séparation architecturale claire » des rôles, sans limite, sous une « gouvernance neutre » liée au W3C et à l'IETF « en synergie ».
  - Traitement : Séparation des rôles limitée à la couche des protocoles; ajout que la convergence est absente pour l'identité (11.7 et 11.8) et que le reste du socle est en chantier (4.4); AAIF décrite comme foyer neutre pour des projets, « aux côtés de » AGNTCY, ASF, W3C, IETF et FIDO.
- **Dix projets « initiaux » de l'AAIF** — *corrigé*
  - Texte d'appui : Section 11.2 : trois projets fondateurs au 9 décembre 2025; dix projets au 11 novembre 2026 (A2A admis à l'été 2026, Agent Skills le 22 octobre 2026).
  - Texte, avant alignement : Citait « les dix projets initiaux de l'AAIF ».
  - Traitement : « les dix projets hébergés par l'AAIF au 11 novembre 2026, contre trois à sa création (section 11.2) ».
- **Statut « vérifié » des socles d'architecture** — *corrigé*
  - Texte d'appui : Section 1.5 : aucun cas documenté ne montre MCP, A2A ou un système multi-agents en production (chapitre 42). Section 4.4 : OpenTelemetry au statut « Development », registre MCP en préversion, identité des agents sans profil adopté.
  - Texte, avant alignement : MCP, A2A, OpenTelemetry gen_ai.* et les autres socles « correspondent à des réalités techniques vérifiées et documentées fin 2026 ».
  - Traitement : « existent et sont documentés fin 2026 »; phrase ajoutée : cela ne vaut pas preuve d'usage (section 1.5, chapitre 42); les trois socles encore en chantier sont nommés (section 4.4).
- **Cibles de production 2027 présentées comme standards** — *corrigé*
  - Texte d'appui : Section 4.2 : les agents en production sont étroits, construits sur mesure; les protocoles répondent à une étape que la plupart des équipes n'ont pas franchie. Section 1.5 : aucun cas documenté de MCP, A2A ou multi-agents en production.
  - Texte, avant alignement : Le tableau des sept ruptures opposait les prototypes 2024-2025 aux « standards de production d'entreprise (2027) », et la phrase d'introduction parlait de « standards de production 2027 ».
  - Traitement : En-tête de colonne et phrase d'introduction : « cible de production »; phrase ajoutée disant que ces cibles ne décrivent pas l'état général de la pratique (4.2, 1.5, chapitre 42).
- **Les modèles seraient devenus interchangeables** — *corrigé*
  - Texte d'appui : Section 4.2 : 17 cas sur 20 utilisent un modèle propriétaire; la perte d'un fournisseur de modèles se prépare (chapitre 46).
  - Texte, avant alignement : Postulat : les modèles fondationnels « sont devenus des composants interchangeables ».
  - Traitement : Reformulé en posture (« doivent être traités comme des composants remplaçables ») avec une phrase : ce n'est pas l'état de la pratique, 17 cas sur 20 de MAP dépendent d'un modèle propriétaire (section 4.2).
- **Calendrier réglementaire « simultané »** — *corrigé*
  - Texte d'appui : Section 4.4 : le règlement (UE) 2026/1744 (Digital Omnibus) a reculé le calendrier; annexe III au 2 décembre 2027, annexe I au 2 août 2028. Section 4.5 et points à retenir : le report donne du temps, pas une dispense.
  - Texte, avant alignement : Parlait d'une « entrée en vigueur simultanée » et d'une année 2027 qui « ferme définitivement la parenthèse de tolérance expérimentale ».
  - Traitement : Échéances « échelonnées de 2026 à 2028 »; ajout du Digital Omnibus, des deux dates de l'AI Act et de la phrase « ce report donne du temps, non une dispense » (section 4.4); les dates du texte (E-23, article 50, Loi 25) sont gardées.
- **Source des échéances européennes** — *corrigé*
  - Texte d'appui : Section 4.4 et limites du chapitre 4 : le Digital Omnibus a été lu sur une reproduction non officielle; le chapitre 35 en confirme le report par les considérants publiés sur EUR-Lex.
  - Texte, avant alignement : Les échéances juridiques « reposent sur les textes officiels en vigueur ».
  - Traitement : Phrase ajoutée en 0.4 : la date de décembre 2027 est connue par une reproduction non officielle du règlement (UE) 2026/1744, dont le chapitre 35 confirme le report.
- **Échelle L0 à L4 et « taxonomies purement cognitives »** — *corrigé*
  - Texte d'appui : Section 1.3 : trois échelles publiées (Feng et coll. L1 à L5, Singapour à quatre niveaux, CSA de 0 à 5), définies d'après le rôle de l'humain ou, pour Singapour, selon deux axes; elles ne se recouvrent qu'approximativement.
  - Texte, avant alignement : Opposait l'échelle L0 à L4 à des « taxonomies purement cognitives », sans la situer par rapport aux échelles publiées.
  - Traitement : Opposition retirée; l'échelle est dite propre à l'ouvrage.
- **Numéros des niveaux L0 à L4** — *avertissement*
  - Texte d'appui : Section 1.3 : le L3 de Feng et coll. est « consultant », le niveau 3 de la CSA « conditionnelle ».
  - Texte, avant alignement : Présentait L0 à L4 comme échelle unique du compendium, sans dire que ses numéros diffèrent de ceux des échelles publiées.
  - Traitement : Échelle laissée telle quelle; phrase ajoutée : ses numéros ne se transposent pas aux trois échelles de la section 1.3, avec l'exemple de L3 et du niveau 3.
- **Règle du maillon le plus élevé** — *nuance*
  - Texte d'appui : Section 1.3 : le niveau d'autonomie se fixe par agent et par classe d'action; l'approbation est réservée à l'irréversible et au fort enjeu.
  - Texte, avant alignement : Impose à toute la chaîne le niveau d'exigence du maillon dont l'empreinte d'action est la plus élevée.
  - Traitement : Règle gardée; phrase ajoutée dans l'encadré : elle va au-delà de ce que retient le chapitre 1 (section 1.3).
- **Identité décentralisée et justificatifs (DID, VCs) dans le tableau des standards** — *avertissement*
  - Texte d'appui : Sections 11.4 et 11.10 : aucun RFC propre aux agents; identité décentralisée, confiance et réputation : posture « attendre ».
  - Texte, avant alignement : Les lignes « Identité et sécurité » (SPIFFE/DID) et « SPIFFE / SPIRE & W3C DIDs / VCs » présentent DID comme brique d'identité de la cible 2027.
  - Traitement : Lignes gardées; paragraphe ajouté après le tableau 0.6 : aucun RFC propre aux agents, DID en posture « attendre » (sections 11.4 et 11.10).
- **ISO/IEC 42001 et NIST AI RMF comme référentiels « d'agents »** — *corrigé*
  - Texte d'appui : Sections 11.5 et 11.6 : aucune norme ISO/IEC propre aux agents repérée; l'initiative du NIST n'a produit aucun livrable normatif.
  - Texte, avant alignement : La cellule disait « référentiels de maîtrise des risques d'agents ».
  - Traitement : « d'agents » retiré de la cellule; phrase ajoutée après le tableau 0.6 (sections 11.5 et 11.6).
- **Maturité des projets de l'AAIF listés au tableau 0.6** — *avertissement*
  - Texte d'appui : Section 11.2 : trois niveaux (Sandbox, Growth, Impact); seul le niveau d'A2A (Growth) est établi; l'étiquette « projet de l'AAIF » ne dit rien de la maturité.
  - Texte, avant alignement : Le tableau liste les projets AAIF comme standards sans indiquer leur niveau.
  - Traitement : Phrase ajoutée après le tableau 0.6 sur les trois niveaux et sur A2A au niveau Growth (section 11.2).
- **Neutralité de la gouvernance par fondation (critère 1)** — *avertissement*
  - Texte d'appui : Section 11.2 : conseil et comité technique réglés par la cotisation; la gouvernance technique varie d'un projet à l'autre.
  - Texte, avant alignement : Le critère 1 oppose la « fondation ouverte multi-acteurs » à l'éditeur unique, sans nuance.
  - Traitement : Question gardée; phrase ajoutée : au sein de l'AAIF, la gouvernance technique varie d'un projet à l'autre (section 11.2).

Ce qui reste, selon l'agent : Le contrôle répond « conforme » (5027 → 5518 mots, 110 %, donc près du plafond de 110 %). Les 36 lignes de tableau, la formule, la figure, les encadrés et les séquences des six parcours sont conservés; seul fichier écrit : Master/fusion/reecrit/ouverture.md. Je n'ai pas pu vérifier contre les trois exposés le contenu de E-23 et de la Loi 25 (article 12.1, sanctions), l'article 50 de l'AI Act, ISO/IEC 42001 dans les appels d'offres, la formule de Forrester, l'architecture à six couches ni l'attribution des sujets aux chapitres 12 à 47 dans les parcours et le tableau 0.6 : ces éléments sont laissés tels quels. J'ai écrit « fictive mais réaliste » pour le Groupe Boréal (« fictive » vient de la consigne, non du texte d'origine).

### Annexe F — Décisions d'architecture (ADR) et arbres de choix

Changements principaux :

- Introduction, paragraphe de F.1 et textes d'introduction de F.2, F.3 et F.4 resserrés : retrait de « non négociable », « maître », « formels », « parfaitement », « insurmontable », « doctrine », « numéro un ».
- Titres : « consolidé » retiré de F.1, « sélection » remplacé par « choix » en F.2, « arbitrage entre » par « choix entre » en F.3, « normatif » retiré en F.4; numéros de sections inchangés.
- Cas limites de F.2 : amorces en gras alignées sur le patron « **Amorce.** texte »; « Edge » retiré de l'amorce 4, redondant avec « en périphérie »; « systématiquement » devient « toujours ».
- Colonne de l'invariant : « Zéro » devient « Aucune » ou « aucun »; « egress », « ACL-aware », « pré/post-action », « décommissionnement », « 3-Way Match » et « Open-Weights » remplacés par un terme français; formules $\tau$, $\ge 85\,\%$ et pass^5 conservées telles quelles.
- Phrase finale de F.4 reformulée en condition (« Si toutes les fiches suivent ce descripteur… ») au lieu de « l'adoption systématique »; blocs de code, figures, séparateur de tableau, colonnes « Code », « Chap. » et « Intitulé normatif » et renvois inchangés.

Ce qui reste, selon l'agent : Aucun texte d'appui n'est défini pour l'annexe F; aucune divergence à comparer, et le contrôle répond conforme (33 lignes de tableau conservées, colonnes 1 à 3 identiques selon un diff). À relire : « mille embranchements » est une hyperbole conservée parce que le chiffre est protégé, et « fréquente, observée en 2025–2026 » reste une affirmation sans source dans l'original. Les rapprochements « à trois voies » et « poids ouverts » reprennent le vocabulaire des chapitres 45 et 32 ou 46, que je n'ai lu que par recherche de termes, non par relecture des passages.

### Annexe G — Listes de contrôle d'homologation

Changements principaux :

- Introduction et encadré resserrés : « Règle d'homologation » devient une amorce sobre, « Go / No-Go » et l'expansion de PRR (sigle conservé) sont retirés.
- Termes anglais remplacés par le français lorsqu'il existe : mode fantôme, déploiement canari, équipe rouge, confiance zéro, retour arrière, systèmes d'enregistrement, gigue, multilocataire, périphérie, reprise cognitive, poids ouverts, exécution miroir, coût par résultat, usine logicielle agentique, SRE autonome, agents d'utilisation d'interface graphique (CUA), géorepérage, jeu de réserve.
- Intensifs et gloses anglaises retirés (strict, complet, transparente, Scope Attenuation, Segregation of Duties, Named Business Owner, Deployment Footprint, Kill Switch, PIA); « zéro » devient « aucun »; « staging » devient « pré-production ».
- Titres des grilles en minuscules sauf le premier mot et les noms propres; en-tête de la 4e colonne : « Artefact de preuve exigé à la revue d'homologation ».
- Les 75 points, leurs identifiants, criticités et mentions [BLOQUANT] sont inchangés (vérifié par comparaison des colonnes 1 et 3); séparateurs de tableau, formules et symboles (≥, ≤, →, ↔︎) repris à l'identique.

Ce qui reste, selon l'agent : Annexe sans texte d'appui (UNITES.annexe-G : liste vide), donc aucune divergence à comparer avec un exposé; les renvois externes (RFC, ISO, EU AI Act, Loi 25, E-23) sont repris tels quels, sans vérification contre une source. Choix de vocabulaire à valider : « équipe rouge », « mode fantôme » et « exécution miroir » suivent les chapitres 6, 34 et 47; « verrouillages actifs » (O-06) suit le chapitre 33. « Séparation des devoirs » (F-11) et « séparation des tâches » (S-15) sont laissées telles quelles, comme dans l'original. « Write-Audit-Publish », « rug pull », « On-Behalf-Of » et « Saga » restent en l'état (patron ou attaque nommés, objet de spécification).

### Annexe H — Glossaire normatif et index des standards

Changements principaux :

- Entrées renvoyées à l'annexe A (19) : Agent Card (A.2), Agent Registry (A.2), Bac à sable d'exécution (A.5), Chorégraphie agentique (A.1), Confidential Clean Room / GPU TEE (A.5 et A.7), Context Engineering (A.3), Couche sémantique (A.3), Data Contract (A.3), Dataspace (A.7), Distillation LLM → SLM (A.6), Exécution durable (A.1), Human-in-the-Loop (A.1), Human-on-the-Loop (A.1), MCP Tool Poisoning (A.5), Ontologie d'entreprise (A.3), Patron Saga (A.1), Policy Decision Point / Policy Enforcement Point (A.4), Shadow Mirroring (A.6), Simplex cyber-physique (A.5). Chacune garde son intitulé, ne dit que ce que l'annexe A n'a pas (technologies, normes, mécanisme, portée) et se termine par « (voir annexe A, section A.k) ». Aucune ne se réduit au seul renvoi : toutes ajoutent quelque chose.
- 35 entrées absentes de l'annexe A gardent leur définition, resserrée : emphase retirée (« massivement », « strictement », « physiquement », « maîtresse »), métaphores remplacées (« sas », « maison neutre »), anglicismes francisés (« prompts », « nœud Edge », « B2B », « stateful », « Open Source », « pub/sub », « Physical AI », « Systems of Record »).
- Introduction réécrite : plus de formule d'annonce ni de « mobilise simultanément »; elle dit la relation à l'annexe A (renvoi des entrées déjà définies, définitions qui fixent l'usage et non une norme).
- Tableau H.2 : 27 lignes et séparateur conservés; en-têtes en minuscules, catégories corrigées (« Identité corporative » devient « Identité d'entreprise », « Bancs d'évaluation » devient « Bancs d'essai »), « LLM » devient « modèle de langage », « déc. 2027 » devient « décembre 2027 ».
- Titres, ligne de séparation du tableau, formules $…$, 54 puces et 29 lignes de tableau conservés à l'identique ou en nombre; apostrophes typographiques de l'original gardées, comme dans les volets déjà réécrits.

Divergences traitées :

- **Terme français de human-on-the-loop** — *corrigé*
  - Texte d'appui : Annexe A, section A.1 : « humain sur la boucle » (human-on-the-loop)
  - Texte, avant alignement : H.1 : « Humain en supervision — Niveau L3 »
  - Traitement : Intitulé aligné sur l'annexe A : « HOTL / Humain sur la boucle — Niveau L3 ». C'est le seul intitulé de H.1 dont le français change avec le suivant.
- **Terme français de l'exécution en miroir** — *corrigé*
  - Texte d'appui : Annexe A, section A.6 : « exécution en miroir » (le figuier étrangleur y est défini à part)
  - Texte, avant alignement : H.1 : « Shadow Mirroring (Double exécution en ombre) », patron « Strangler Fig »
  - Traitement : Intitulé « Shadow Mirroring (Exécution en miroir) »; « Strangler Fig » devient « figuier étrangleur ». L'identité des deux notions est une déduction (mêmes entrées, seul l'ancien chemin sert), non une lecture du chapitre 47.
- **Benchmark** — *corrigé*
  - Texte d'appui : Annexe A, section A.6 : « banc d'essai » (benchmark)
  - Texte, avant alignement : H.2 : catégorie « Bancs d'évaluation » pour Tau-bench
  - Traitement : « Bancs d'essai »
- **Système d'enregistrement** — *corrigé*
  - Texte d'appui : Annexe A, section A.3 : « système d'enregistrement » (system of record)
  - Texte, avant alignement : H.1, System of Action : « Systems of Record » en anglais
  - Traitement : « systèmes d'enregistrement »
- **Fenêtre de contexte** — *corrigé*
  - Texte d'appui : Annexe A, section A.3 : « fenêtre de contexte »
  - Texte, avant alignement : H.1, Context Engineering : « fenêtre d'attention d'un agent »
  - Traitement : Le membre de phrase disparaît dans le renvoi à A.3; Context Rot emploie « fenêtre de contexte ».
- **Portée du mot « normatif »** — *nuance*
  - Texte d'appui : Annexe A, en tête : chaque définition fixe l'usage du mot dans l'ouvrage, « pas une norme »
  - Texte, avant alignement : Titre « Glossaire normatif » et introduction « vocabulaire normatif »
  - Traitement : Introduction : « chaque définition fixe l'usage du mot dans l'ouvrage, non une norme ». Le titre reste, la première ligne étant imposée.
- **Protection d'un environnement d'exécution de confiance** — *nuance*
  - Texte d'appui : Annexe A, section A.5 : protège des logiciels et des opérateurs de l'exploitant, « guère d'un accès physique »
  - Texte, avant alignement : H.1 : données non exposées « à l'hébergeur ni à la contrepartie », sans réserve
  - Traitement : Phrase ajoutée à l'entrée Confidential Clean Room / GPU TEE : la protection vaut contre les logiciels et les opérateurs de l'exploitant, guère contre un accès physique.
- **Sigle ACP** — *avertissement*
  - Texte d'appui : Annexe A, section A.8 : ACP désigne trois protocoles selon le chapitre (6, 7 ou 10)
  - Texte, avant alignement : H.2, A2A : « unifiant l'initiative ACP », sans dire lequel
  - Traitement : Texte laissé. L'annexe A ne dit pas lequel des trois ACP A2A a unifié; le chapitre 6 le dit sans doute.

Ce qui reste, selon l'agent : Le texte est plus long que l'original (106 %), parce que chaque renvoi ajoute une dizaine de mots; le gain tient à la sobriété, non à la longueur. Quatre entrées ont été gardées entières bien qu'elles touchent une notion de l'annexe A, faute d'avoir le même terme : Clé d'idempotence (A.1), Dérive sémantique (A.6), KV-Cache Sharing (A.6) et HYOK (A.8, simple développement du sigle); à trancher par le relecteur. Les niveaux « L2 » et « L3 » des entrées HITL et HOTL n'ont pas pu être confrontés au chapitre 22, qui n'est pas un texte d'appui; le contenu de H.2 (dates, autorités, articles) est repris de l'original sans vérification externe.
