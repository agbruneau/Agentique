# Annexe B — Fiches protocoles

> **Version 2 — 12 novembre 2026.** État de référence : 11 novembre 2026. Chaque fiche condense le chapitre indiqué, complété par les chapitres 8 (registres) et 11 (gouvernance), et n'ajoute aucune source; les réserves de ces chapitres s'appliquent. « Non réglé » désigne ce que le protocole laisse à l'entreprise. Annexe auditée et révisée le 12 novembre 2026.

## B.1 Vue d'ensemble

| Protocole | Relation couverte | Porteur | État | Chapitre |
|---|---|---|---|---|
| MCP | Agent et outils | AAIF; série de LF Projects | Révision `2026-07-28` | 5 |
| A2A | Agent et agent | AAIF, stade « Growth » | Version 1.0, correctif 1.0.1 | 6 |
| AG-UI | Agent et interface | CopilotKit et partenaires, hors fondation | Antérieur à la 1.0, par déduction | 7 |
| ANP | Agents sans tiers commun | Communauté ANP, hors fondation | Jeu de spécifications 1.2, en partie en brouillon | 7 |
| AGNTCY | Annuaire, schémas, messagerie | Linux Foundation, hors AAIF | Annuaire 1.0; messagerie en brouillon | 7 |
| AP2 | Preuve d'autorisation d'achat | Google | Version 0.2, non datée | 10 |
| x402 | Paiement dans l'échange HTTP | x402 Foundation, né chez Coinbase | Version non établie; SDK visant des chaînes de blocs | 10 |

Deux protocoles forment le socle, MCP et A2A. Les cinq autres s'adoptent besoin par besoin, derrière un adaptateur.

## B.2 MCP — Model Context Protocol

| Rubrique | Contenu |
|---|---|
| Objet | Standardise la manière dont une application d'IA découvre et appelle des outils. Laisse l'orchestration à l'hôte et la délégation entre agents à A2A. |
| Gouvernance | Lancé par Anthropic à la fin de 2024, donné à l'AAIF à sa création, le 9 décembre 2025. Série de LF Projects, LLC, qui approuve tout changement de gouvernance; licence Apache 2.0. Les sièges de mainteneurs appartiennent à des personnes, deux mainteneurs en chef tranchent; toute modification passe par une SEP. |
| Modèle | Trois rôles : hôte, client, serveur, sur JSON-RPC. Un serveur expose des outils, des ressources et des prompts. Transports : Streamable HTTP pour le distant, stdio pour le local; HTTP+SSE, déprécié depuis `2025-03-26`, peut être retiré dans une révision future. |
| Révision `2026-07-28` | Protocole sans état : plus de poignée de main ni de session; capacités jointes à chaque requête; méthode `server/discover` obligatoire; un serveur qui manque d'une information renvoie `input_required`, et le client réémet la requête. En-têtes `Mcp-Method` et `Mcp-Name` pour les intermédiaires; tout serveur qui lit le corps rejette une discordance (400, `HeaderMismatch`). Échantillonnage, racines et journalisation sont dépréciés. |
| Extensions | Stables : OAuth Client Credentials, Enterprise-Managed Authorization, MCP Apps. Bêta : Tasks (destinée au cœur, avec ses propres notifications d'état), Skills over MCP, Server Cards. Toujours désactivées par défaut. |
| Sécurité | Autorisation facultative; sur HTTP, elle suit un profil d'OAuth 2.1. Un serveur n'accepte qu'un jeton émis pour lui et ne le relaie pas en aval. Un serveur HTTP valide l'en-tête `Origin`. Les annotations d'un outil sont non fiables, sauf si le serveur est de confiance. |
| Non réglé | Identité de l'agent, comportement des passerelles, piste d'audit, validation humaine (simple « devrait »), approbation des serveurs, vérification du code. Le registre officiel, en préversion, n'authentifie que l'éditeur et exclut les serveurs privés. |
| Appuis pour planifier | Fenêtre de dépréciation d'au moins douze mois; SDK classés en trois niveaux; feuille de route du 22 août 2026 en cinq priorités, sans engagement ferme. |
| Usage en entreprise | Protocole par défaut entre agent et outil. Autorisation obligatoire sur tout serveur distant, Enterprise-Managed Authorization si le fournisseur d'identité et les clients la prennent en charge, registre interne, passerelle sur le chemin, outils idempotents ou compensables. |

## B.3 A2A — Agent2Agent Protocol

| Rubrique | Contenu |
|---|---|
| Objet | Standardise la délégation d'un objectif à un agent opaque : le client ne voit ni ses outils, ni sa mémoire, ni son raisonnement. |
| Gouvernance | Lancé par Google en avril 2025; donné à la Linux Foundation le 23 juin 2025; fusion d'ACP, le protocole d'IBM, annoncée le 29 août 2025; entrée à l'AAIF annoncée le 27 août 2026, date d'approbation inconnue. Comité de pilotage technique de huit entreprises en août 2025; composition actuelle non vérifiée. |
| État | Version 1.0 du 12 mars 2026, première spécification stable, en rupture avec la version 0.3; correctif 1.0.1 du 28 mai 2026. La page de la spécification affiche encore 1.0.0. |
| Modèle | Agent Card, tâche, message et artefact. Huit états de tâche, préfixés `TASK_STATE_` en 1.0, dont `REJECTED` et `AUTH_REQUIRED`. Onze opérations. Trois liaisons équivalentes : JSON-RPC, gRPC, HTTP+JSON; le fichier Protocol Buffers est normatif. |
| Modes | Requête-réponse, flux, notifications poussées vers un webhook, doublons possibles. |
| Sécurité | Authentification à la couche HTTP, selon les mécanismes déclarés dans la carte. Signature des cartes possible, non obligatoire; elle atteste l'origine, pas la fiabilité. Le serveur doit autoriser chaque opération. En état `AUTH_REQUIRED`, les justificatifs s'obtiennent hors protocole, sauf mécanisme négocié. |
| Non réglé | API de registre, obtention des identifiants, portée d'une approbation donnée en cours de tâche, justesse du résultat, responsabilité entre organisations. |
| Adoption | Plus de 150 organisations déclarent leur soutien en avril 2026; intégrations dans Azure AI Foundry, Copilot Studio et Amazon Bedrock AgentCore Runtime. Des déploiements en production sont affirmés, sans qu'aucune organisation soit nommée. |
| Usage en entreprise | Protocole par défaut entre agents d'équipes ou d'organisations distinctes. Version 1.0 avec son correctif 1.0.1 pour tout nouvel agent, cartes signées, exposition derrière une passerelle, contrôle de ce que rend un agent tiers. |

## B.4 AG-UI — Agent-User Interaction Protocol

| Rubrique | Contenu |
|---|---|
| Objet | Normalise le flux d'événements entre le service qui exécute un agent et l'application que l'utilisateur a sous les yeux. |
| Gouvernance | Né d'un partenariat de CopilotKit avec LangChain et CrewAI. Aucune fondation; absent des projets de l'AAIF. |
| État | La documentation annonce le retrait des événements `THINKING_*` « à la version 1.0.0 » et liste des événements en brouillon; le dépôt n'affiche aucune version publiée. Le protocole n'aurait donc pas atteint sa version 1.0 : c'est une déduction. |
| Modèle | Le client envoie une entrée d'exécution par HTTP POST; le service répond par un flux d'événements, en SSE ou en format binaire, sans transport imposé. État partagé par instantané, puis deltas JSON Patch. L'interface peut déclarer des outils que l'agent appelle. |
| Voisins | A2UI et MCP Apps décrivent le rendu; AG-UI le transporte. |
| Sécurité | La page d'architecture ne dit rien de l'authentification ni de l'autorisation. Une approbation recueillie par un outil frontal ne fait pas preuve (chapitre 30). |
| Adoption | Intégrations documentées avec Microsoft Agent Framework, Google ADK, AWS Strands Agents, LangChain, CrewAI, Pydantic AI et LlamaIndex. |
| Usage en entreprise | À placer derrière la couche d'identité interne. Épingler le SDK et isoler les types d'événements dans un module. |

## B.5 ANP — Agent Network Protocol

| Rubrique | Contenu |
|---|---|
| Objet | Identifier et trouver un agent sur l'internet ouvert, entre organisations sans relation préalable ni tiers commun. |
| Gouvernance | Porté par une « communauté ANP », sous licence Apache 2.0, sans fondation. Le livre blanc figure parmi les brouillons du groupe communautaire W3C AI Agent Protocol, sans portée normative; aucun travail de normalisation formelle n'a été repéré. |
| État | Jeu de spécifications 1.2. Publiés : authentification par DID, méthode `did:wba` et son espace de noms, description, découverte, catalogue de messagerie de bout en bout. En brouillon : autorisation (version 0.7), méta-protocole, adaptation au paiement AP2. Candidat : profil de groupe MLS. |
| Modèle | Trois couches. Identité : un DID hébergé sous un nom de domaine, qui publie les clés de l'agent. Méta-protocole : deux agents négocient leur format d'échange et génèrent le code correspondant. Application : description en JSON-LD, découverte par `/.well-known/agent-descriptions` ou par des services de recherche. |
| Sécurité | La confiance s'ancre dans le DNS et TLS. L'autorisation, pièce maîtresse pour une entreprise, reste en brouillon. |
| Réserve | Un format négocié à l'exécution et du code généré à la volée se concilient mal avec la gestion du changement et la piste d'audit. C'est une analyse du chapitre 7. |
| Usage en entreprise | Sans objet à l'interne, où un fournisseur d'identité et un registre existent. À la frontière, `did:wba` à l'essai, en comparaison avec vLEI (chapitre 45); méta-protocole exclu de la production. |

## B.6 AGNTCY

| Rubrique | Contenu |
|---|---|
| Objet | Infrastructure ouverte pour que des agents se découvrent, vérifient leurs capacités et communiquent. Complète MCP et A2A, ne les remplace pas. |
| Gouvernance | Ouvert par Cisco en mars 2025, confié à la Linux Foundation le 29 juillet 2025 avec Dell Technologies, Google Cloud, Oracle et Red Hat. Distinct de l'AAIF. |
| OASF | Schéma qui décrit un agent par compétences et domaines; extensible, appelé à évoluer. |
| Agent Directory | Annuaire distribué, sans opérateur central, en version 1.0 depuis le 19 février 2026. Fiches adressées par leur contenu, signature possible. L'adressage garantit l'intégrité d'une fiche, pas son auteur ni sa qualité. |
| SLIM | Messagerie point à point, de groupe et par appel de procédure, sur gRPC en flux (HTTP/2 ou WebSocket), sans courtier central, chiffrée de bout en bout par MLS. Brouillon IETF individuel, informatif, non adopté par un groupe de travail; révision 03 du 2 novembre 2026, qui expire le 6 mai 2027. |
| Identity | Identifiant d'agent adossé à un justificatif vérifiable, l'Agent Badge. |
| Réserve | L'empreinte d'un seul fournisseur reste forte : auteurs du brouillon, serveur de schémas, instance publique de l'annuaire. |
| Usage en entreprise | Composants adoptés séparément. Annuaire et OASF pour fédérer plusieurs registres; SLIM, à l'essai, pour des groupes chiffrés entre domaines de confiance. |

## B.7 AP2 — Agent Payments Protocol

| Rubrique | Contenu |
|---|---|
| Objet | Prouver ce qu'un utilisateur a autorisé pour un achat. Ne décrit ni catalogue ni panier : c'est une fonction de sécurité logée dans un protocole de commerce. |
| Gouvernance | Publié par Google; conçu pour être compatible avec UCP. |
| État | Version 0.2, non datée. |
| Modèle | Deux mandats signés, liés par hachage à l'objet de caisse du marchand : Checkout Mandate pour le contenu, Payment Mandate pour le paiement. Un mandat ouvert exprime des contraintes et porte la clé publique de l'agent; un mandat fermé décrit une transaction. Format SD-JWT. |
| Garanties | La surface où l'utilisateur approuve ne doit pas être agentique. La validation des mandats s'exécute dans du code déterministe. |
| Parcours | Avec présence humaine : l'utilisateur approuve le panier fermé. Sans présence humaine : il approuve des contraintes, et l'agent signe les mandats fermés. |
| Non réglé | Façon dont l'agent arrête le contenu des mandats, litiges, conservation des preuves, délégation d'un mandat entre agents, langage de requête des mandats, répartition de la responsabilité. |
| Voisin | Verifiable Intent, brouillon 0.1 attribué par l'AAIF à Mastercard avec Google, reprend le format et ajoute un justificatif d'identité en tête de chaîne. |
| Usage en entreprise | Présence humaine par défaut. Mandat ouvert pour des achats répétitifs de faible valeur, avec contraintes étroites et expiration courte. Mandats et reçus versés à la piste d'audit. |

## B.8 x402

| Rubrique | Contenu |
|---|---|
| Objet | Placer le paiement dans l'échange HTTP, au moyen du code d'état 402 Payment Required. |
| Gouvernance | Né chez Coinbase, transféré sous une x402 Foundation : le dépôt canonique est `x402-foundation/x402`, celui de Coinbase n'est plus qu'une copie de développement. Licence Apache 2.0; statuts de la fondation non établis. |
| Modèle | Trois en-têtes : `PAYMENT-REQUIRED` dans la réponse 402, `PAYMENT-SIGNATURE` dans la requête réémise, `PAYMENT-RESPONSE` avec la ressource. Un facilitateur peut vérifier (`/verify`) et régler (`/settle`) pour le serveur. Trois schémas : `exact`, `upto`, `batch-settlement` (chaînes EVM seulement). |
| Portée | Ambition déclarée de couvrir tous les réseaux; les SDK listés visent des chaînes de blocs, et le règlement se fait en cryptomonnaies stables selon l'AAIF. |
| Sécurité | Un seul principe : ni le facilitateur ni le serveur ne doivent pouvoir déplacer des fonds au-delà de l'intention du client. |
| Non réglé | Autorisation distincte du paiement, plafond de dépense, remboursement, litige, identité du payeur. |
| Voisin | MPP, corédigé par Tempo et Stripe, emploie le même code 402 avec une autre grammaire. Aucun pont entre les deux dans les pages lues. |
| Usage en entreprise | Micropaiements de services découverts en cours de tâche, depuis un portefeuille dédié et plafonné hors de l'agent. Un mandat AP2 peut porter l'autorisation, et x402 le règlement. |

## B.9 Lire une fiche

Trois lignes comptent plus que les autres. La gouvernance dit qui peut changer le protocole, et à quel rythme. L'état dit ce qui est stable, donc ce qu'on peut épingler. La ligne « non réglé » donne la liste des décisions qui reviennent à l'entreprise : c'est elle qui dimensionne le projet.

Pour tout protocole absent de cette annexe, les sept questions du chapitre 7 s'appliquent : besoin hors de portée de MCP et d'A2A, composition avec l'existant, gouvernance, stabilité promise, mises en œuvre indépendantes, sécurité spécifiée, possibilité d'en sortir.
