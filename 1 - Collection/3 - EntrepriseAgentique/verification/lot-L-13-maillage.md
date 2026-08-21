# Lot L-13 — L-13

| Champ | Valeur |
|---|---|
| Lot | **L-13** — phase **P2**, jalon J-3 |
| Débloque | **ch. 22, 23** |
| Date d'instruction | **21 juillet 2026** |
| Résultat | **9 affirmations** — 0 en [A], 0 écartée(s) par le vote. **7 échecs de source** consignés |
| Vote | **1 affirmation(s)** portant à elles seules une thèse de chapitre soumises au vote à trois juges, conformément au seuil déclaré (PRD §A.4). Les autres sont en **[B] par extraction citée** |
| Contrôle de bornage | **2 correction(s)** — contrôle systématique introduit en P2 sur constat de la relecture P1.4 |
| Statut | ☑ **CLOS** |

---

## A. Affirmations retenues (9)

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L13-A1` | **[B]** | 0 | La documentation officielle de Docker décrit MCP Gateway comme une solution ouverte d'orchestration de serveurs MCP agissant en mandataire centralisé entre clients et serveurs, et déclare que sa fourniture au titre de « Docker AI Governance » est réservée sur invitation (invite-only) — soit une disponibilité restreinte, distincte d'une disponibilité générale. |
| `L13-A2` | **[B]** | 0 | AWS a déclaré Amazon Bedrock AgentCore — dont AgentCore Gateway et AgentCore Identity — généralement disponible le 13 octobre 2025, dans neuf régions AWS nommées ; AgentCore Gateway y est documenté comme convertissant des API, des fonctions Lambda et des services existants en outils compatibles MCP. |
| `L13-A3` | **[B]** | 0 | agentgateway, mandataire ouvert annoncé pour MCP et A2A, se déclare projet de la Linux Foundation ; au 21 juillet 2026, la version publiée marquée « Latest » sur son dépôt est v1.4.0-alpha.2 (21 juillet 2026), signalée comme pré-version, la publication la plus récente non marquée pré-version étant v1.3.1 (22 juin 2026). |
| `L13-A4` | **[B]** | 0 | La documentation d'agentgateway spécifie une politique d'autorisation propre à MCP, écrite en Common Expression Language, évaluée dans le contexte d'une requête MCP contre des invocations de méthodes telles que list_tools et call_tools, exposant les champs mcp.tool.name, mcp.tool.target, mcp.prompt.name, mcp.resource.name, jwt.sub et jwt.<claim>, et filtrant des réponses de liste toute ressource non autorisée. |
| `L13-A5` | **[B]** | 0 | SLIM (Secure Low-Latency Interactive Messaging) est décrit par un Internet-Draft de soumission individuelle, draft-mpsb-agntcy-slim-02, dont la fiche du Datatracker de l'IETF porte une expiration au 8 janvier 2027 ; le document s'y présente comme couche de transport pour les protocoles d'agents — A2A et MCP nommément — combinant gRPC sur HTTP/2 et HTTP/3 avec chiffrement de bout en bout par MLS. |
| `L13-A6` | **[C]** | 1 | La sous-section 8.2 « Discovery Mechanisms » de la spécification A2A version 1.0.0 énumère trois mécanismes de découverte — URI bien connu https://{server_domain}/.well-known/agent-card.json, interrogation de catalogues d'agents curés, et configuration directe d'URL ou de contenu de carte d'agent — et n'assortit la mention des catalogues d'aucun protocole de registre ou de courtage spécifié dans cette sous-section. |
| `L13-A7` | **[B]** | 0 | NIST SP 800-207 « Zero Trust Architecture », publié en août 2020, pose que l'authentification et l'autorisation — du sujet comme de l'appareil — sont des fonctions discrètes exécutées avant l'établissement d'une session vers une ressource d'entreprise, et que la protection porte sur les ressources et non sur les segments de réseau. |
| `L13-A8` | **[B]** | 0 | Le document du NIST consacré à l'identité et à l'autorisation des agents logiciels et d'IA — « [Concept Paper] Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization », publié le 5 février 2026 par le NCCoE — est un concept paper au stade de projet public initial (Initial Public Draft) appelant des commentaires jusqu'au 2 avril 2026 : un document pré-normatif de cadrage de projet, ni… |
| `L13-A9` | **[B]** ⚖ | 0 | Le terme « agent mesh » désigne deux objets techniquement distincts chez deux fournisseurs consultés : chez Solo.io, une couche de connectivité posée par analogie avec le service mesh pour traiter sécurité, observabilité, cloisonnement et garde-fous (communiqué du 24 avril 2025) ; chez Solace, un cadriciel applicatif multi-agents bâti sur le Solace AI Connector, le Google Agent Development Kit et le protocole A2A (dépôt Solace… |

⚖ = soumise au vote adversarial à trois juges.

## C. Contrôle de bornage — 2 correction(s)

*Contrôle de forme, non de contenu : il ne juge pas la vérité du fait, il retire l'excès de l'énoncé.*

| # | Faute | Reformulation retenue |
|---|---|---|
| `L13-A4` | **clause d'exclusivité** | La documentation d'agentgateway spécifie une politique d'autorisation propre à MCP, écrite en Common Expression Language, évaluée dans le contexte d'une requête MCP contre des invocations de méthodes telles que list_tools et call_tools ; elle y documente notamment les champs mcp.tool.name, mcp.tool.target, mcp.prompt.name, mcp.resource.name, jwt.sub et jwt.<claim>, et décrit un filtrage des réponses de liste qui en r… |
| `L13-A9` | **promesse non démontrée** | Le terme « agent mesh » recouvre deux objets techniquement distincts chez les deux fournisseurs consultés : Solo.io le présente dans son communiqué du 24 avril 2025 comme une couche de connectivité posée par analogie avec le service mesh, à laquelle ce communiqué assigne la sécurité, l'observabilité, le cloisonnement et les garde-fous — objectifs annoncés par le fournisseur, non des propriétés démontrées ; chez Solac… |

## D. Échecs de source consignés (7)

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Page produit « Agent Mesh » de Solo.io — définition et statut de disponibilité de l'offre | HTTP 404. Repli sur le communiqué de presse du 24 avril 2025, qui est une source de fournisseur et non une documentation de produit : le statut de disponibilité de l'Agent Mesh reste donc non établi. |
| Annonce AWS de disponibilité générale d'AgentCore (URL supposée) | HTTP 404 — URL construite par déduction, invalide. L'annonce réelle a été retrouvée et ouverte à https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/ |
| Vue d'ensemble de l'Agent Directory Service d'AGNTCY (composant de découverte/courtage) | La page ne renvoie qu'un message de redirection vers https://dir.agntcy.org/latest/dir/dir-overview/ ; le contenu n'a pas été récupéré. Le courtage/annuaire d'AGNTCY reste donc non instruit dans ce lot. |
| Section 8 de la spécification A2A sur le site officiel (ancre directe) | Contenu tronqué avant la section 8 : seuls les intitulés de sous-sections étaient présents. Repli sur le fichier source docs/specification.md du dépôt a2aproject/A2A (branche main). |
| Racine de la documentation agentgateway (mécanismes de politique) | Page de navigation uniquement, aucun contenu de politique. Repli sur la page de documentation dédiée /docs/standalone/main/mcp/mcp-authz/ |
| Documentation Solo Enterprise for agentgateway — autorisation externe par OPA/Rego | Non ouverte : URL rencontrée en résultat de moteur de recherche seulement, faute de budget de requêtes. Le volet OPA/Rego de l'offre commerciale n'est donc pas instruit ; rien n'en est affirmé. |
| Accès réseau direct (curl) pour contourner l'indisponibilité temporaire des outils web | Permission refusée par le bac à sable. En début de session, WebSearch et WebFetch ont par ailleurs été indisponibles environ cinq minutes (classificateur de sûreté hors service), ce qui a réduit le nombre de requêtes menées. |

## E. Ce que le lot déclare n'avoir pas couvert

CE QUE LE LOT N'A PAS COUVERT, ET POURQUOI.  1) Plafond de neuf affirmations. Deux passerelles MCP ont été ouvertes et citées mais n'ont pas obtenu de créneau ; leurs relevés sont reproduits ici pour reprise ultérieure, sans statut d'affirmation du socle :  - Azure API Management (https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview, ms.date 2025-11-13, mise à jour 2026-07-01). Disponibilité déclarée : « Classic tiers: Developer, Basic, Standard, Premium ; v2 tiers: Basic v2, Standard v2, Premium v2 ». Réserve explicite de la source (fait négatif ÉTABLI, degré 2) : « API Management currently supports MCP server tools, but doesn't support MCP resources or prompts » et « API Management MCP server capabilities currently aren't supported in workspaces ». La page distingue en outre un canal de préversion (« AI Gateway release channel […] before they're generally available »).  - IBM ContextForge / MCP Gateway (https://github.com/IBM/mcp-context-forge, Apache-2.0, v1.0.5 du 7 juillet 2026) : « An open source registry and proxy that federates tools, agents, and APIs into one clean endpoint for your AI clients. » Le README consulté ne porte aucune déclaration explicite de maturité ou de préparation à la production.  2) Le tri demandé ANNONCE / GA DOCUMENTÉE / PRODUCTION reste incomplet sur son troisième degré. Aucune offre de ce lot n'a produit de preuve de déploiement en production documentée par un tiers indépendant. C'est un degré 3 (absence de documentation dans le corpus consulté), non un fait négatif : la colonne PRODUCTION est vide faute de recherche dédiée, pas parce qu'elle serait établie vide. Répartition constatée : GA documentée par le fournisseur = AWS AgentCore (13 oct. 2025) et Azure API Management (paliers nommés) ; disponibilité restreinte = Docker MCP Gateway au titre de Docker AI Governance (invite-only) ; pré-version = agentgateway (dernière publication marquée pré-version, v1.4.0-alpha.2) et SLIM (Internet-Draft + étiquettes alpha) ; ANNONCE seule = Solo.io Agent Mesh (communiqué, page produit en 404).  3) Non instruit, faute de budget de requêtes : le courtage/annuaire d'AGNTCY (Agent Directory Service, redirection non suivie) ; le volet OPA/Rego de Solo Enterprise for agentgateway ; les passerelles MCP de Kong, Cloudflare, Obot, MintMCP et autres éditeurs, dont aucune n'a été ouverte — l'énumération de passerelles produite par ce lot n'est donc ni exhaustive ni présentée comme telle ; l'emploi du terme « agent mesh » par des analystes (Gartner et autres) et par Microsoft ; Entra Agent ID, hors périmètre de L-13.  4) Point (c) — moteurs de politique pour l'autorisation par arête : une seule affirmation retenue (CEL dans agentgateway), documentaire et non démontrée. Open Policy Agent a été vérifié comme projet CNCF de niveau « Graduated » depuis le 29 janvier 2021 (https://www.cncf.io/projects/open-policy-agent-opa/, consulté le 21 juillet 2026) mais n'a pas obtenu de créneau ; aucun lien documentaire entre OPA et une passerelle MCP n'a été ouvert dans ce lot, donc rien n'en est affirmé.  5) Le terme « maillage d'agents » en français n'a fait l'objet d'aucune recherche distincte : le relevé (e) porte sur l'anglais « agent mesh » chez deux fournisseurs. Aucune définition normative n'a été rencontrée ; le terme reste à traiter comme terme de marché sans siège normatif, conformément à R-03.

## F. Sources et citations

### `L13-A1` — [B]

La documentation officielle de Docker décrit MCP Gateway comme une solution ouverte d'orchestration de serveurs MCP agissant en mandataire centralisé entre clients et serveurs, et déclare que sa fourniture au titre de « Docker AI Governance » est réservée sur invitation (invite-only) — soit une disponibilité restreinte, distincte d'une disponibilité générale.

- **primaire** — MCP Gateway — page consultée sans numéro de version affiché, consultée le 2026-07-21 — <https://docs.docker.com/ai/mcp-gateway/>
  > The MCP Gateway is Docker's open source solution for orchestrating Model Context Protocol (MCP) servers. […] MCP Gateway as part of Docker AI Governance is an invite-only feature. […] It acts as a centralized proxy between clients and servers, managing configuration, credentials, and access control.
- **primaire** — docker/mcp-gateway (dépôt source) — branche par défaut, consultée le 21 juillet 2026 ; licence MIT, consultée le 2026-07-21 — <https://github.com/docker/mcp-gateway>
  > The MCP Toolkit, in Docker Desktop, allows developers to configure and consume MCP servers from the Docker MCP Catalog. Underneath, the Toolkit is powered by a docker CLI plugin: `docker-mcp`.

**Réserve** — L'énoncé porte sur ce que la page de documentation déclare, non sur une capacité constatée. La page consultée ne comporte aucune mention de vérification de signature ni de gestion de secrets ; ce constat vaut pour cette seule page et ne dit rien du reste de la documentation Docker (degré 3 hors de la page).

### `L13-A2` — [B]

AWS a déclaré Amazon Bedrock AgentCore — dont AgentCore Gateway et AgentCore Identity — généralement disponible le 13 octobre 2025, dans neuf régions AWS nommées ; AgentCore Gateway y est documenté comme convertissant des API, des fonctions Lambda et des services existants en outils compatibles MCP.

- **primaire** — Amazon Bedrock AgentCore is now generally available — Posté le 13 octobre 2025, consultée le 2026-07-21 — <https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/>
  > Amazon Bedrock AgentCore is available in nine AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (Ireland).
- **primaire** — Amazon Bedrock AgentCore Gateway: A secure AI gateway for agents, tools, and models — guide « latest », consulté le 21 juillet 2026, consultée le 2026-07-21 — <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html>
  > it converts APIs, Lambda functions, and existing services into Model Context Protocol (MCP)-compatible tools; fronts other agents and HTTP services through passthrough targets (including Agent-to-Agent (A2A) traffic); and routes inference requests across multiple model providers through a unified, model-based routing endpoint.

**Réserve** — Métrique et qualification auto-déclarées par AWS. La page produit porte en outre une clause d'exclusivité auto-déclarée — « is the only solution that provides both comprehensive ingress authentication and egress authentication in a fully managed service » — qui n'est pas reprise ici et qu'aucun balayage ne permet d'établir. « GA documentée » signifie ici : annonce de disponibilité générale par le fournisseur, non déploiement en production constaté par un tiers.

### `L13-A3` — [B]

agentgateway, mandataire ouvert annoncé pour MCP et A2A, se déclare projet de la Linux Foundation ; au 21 juillet 2026, la version publiée marquée « Latest » sur son dépôt est v1.4.0-alpha.2 (21 juillet 2026), signalée comme pré-version, la publication la plus récente non marquée pré-version étant v1.3.1 (22 juin 2026).

- **primaire** — agentgateway/agentgateway (README) — branche par défaut, consultée le 21 juillet 2026 ; licence Apache-2.0, consultée le 2026-07-21 — <https://github.com/agentgateway/agentgateway>
  > Agentgateway is a Linux Foundation project. […] an open source proxy built on AI-native protocols […] that provides drop-in security, observability, and governance for agent-to-LLM, agent-to-tool, and agent-to-agent communication.
- **primaire** — Releases — agentgateway/agentgateway — état au 21 juillet 2026, consultée le 2026-07-21 — <https://github.com/agentgateway/agentgateway/releases>
  > v1.4.0-alpha.2 (July 21, 2026) — Latest / Pre-release ; v1.4.0-alpha.1 (July 6, 2026) — Pre-release ; v1.3.1 (June 22, 2026) ; v1.3.0 (June 18, 2026)

**Réserve** — Le README ouvre par une clause d'exclusivité auto-déclarée (« The first complete connectivity solution for Agentic AI ») : elle est attribuée à son auteur et non reprise comme fait. Le relevé de versions est daté du 21 juillet 2026 et se périme à chaque publication.

### `L13-A4` — [B]

La documentation d'agentgateway spécifie une politique d'autorisation propre à MCP, écrite en Common Expression Language, évaluée dans le contexte d'une requête MCP contre des invocations de méthodes telles que list_tools et call_tools, exposant les champs mcp.tool.name, mcp.tool.target, mcp.prompt.name, mcp.resource.name, jwt.sub et jwt.<claim>, et filtrant des réponses de liste toute ressource non autorisée.

- **primaire** — MCP authorization — agentgateway — documentation « main (in dev) », consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://agentgateway.dev/docs/standalone/main/mcp/mcp-authz/>
  > The MCP authorization policy works similarly to HTTP authorization, but runs in the context of an MCP request. Authorization rules are written as CEL expressions that evaluate against specific MCP method invocations, such as list_tools and call_tools, to control which tools, prompts, and resources clients can access. […] If a tool or other resource is not allowed, agentgateway automatically filters the resource from list responses so that unauthorized clients never see it.

**Réserve** — R-02 : il s'agit de ce que la documentation décrit, non d'un comportement démontré ni évalué indépendamment. CEL est ici un langage d'expression évalué dans le mandataire ; l'énoncé ne dit rien du moteur OPA/Rego, dont l'existence dans l'offre Solo Enterprise apparaît en résultats de recherche mais dont la page n'a pas été ouverte lors de ce lot.

### `L13-A5` — [B]

SLIM (Secure Low-Latency Interactive Messaging) est décrit par un Internet-Draft de soumission individuelle, draft-mpsb-agntcy-slim-02, dont la fiche du Datatracker de l'IETF porte une expiration au 8 janvier 2027 ; le document s'y présente comme couche de transport pour les protocoles d'agents — A2A et MCP nommément — combinant gRPC sur HTTP/2 et HTTP/3 avec chiffrement de bout en bout par MLS.

- **primaire** — Secure Low-Latency Interactive Messaging (SLIM) — draft-mpsb-agntcy-slim-02 — révision -02 ; expiration au 8 janvier 2027, consultée le 2026-07-21 — <https://datatracker.ietf.org/doc/draft-mpsb-agntcy-slim/>
  > This document specifies the Secure Low-Latency Interactive Messaging (SLIM), a protocol designed to support real-time interactive AI applications at scale. SLIM provides the transport layer for agent protocols (for example, A2A and MCP), combining gRPC over HTTP/2 and HTTP/3 with secure messaging, group communication, and native RPC semantics.
- **primaire** — agntcy/slim (README) — étiquette la plus récente : slimctl v2.0.0-alpha.7, 20 juillet 2026 ;…, consultée le 2026-07-21 — <https://github.com/agntcy/slim>
  > SLIM (Secure Low-Latency Interactive Messaging) is a next-generation communication framework that provides the secure, scalable transport layer for AI agent protocols […] Handles reliable delivery, end-to-end MLS encryption, and group membership management

**Réserve** — Statut pré-normatif : Internet-Draft de soumission individuelle, ni RFC, ni document adopté par un groupe de travail ; il expire le 8 janvier 2027 sauf révision. R-02 : le chiffrement MLS est ce que la spécification décrit, non une propriété démontrée par le relevé. Le dépôt d'implémentation ne publie à ce jour que des étiquettes de pré-version (slimctl v2.0.0-alpha.7, 20 juillet 2026).

### `L13-A6` — [C]

La sous-section 8.2 « Discovery Mechanisms » de la spécification A2A version 1.0.0 énumère trois mécanismes de découverte — URI bien connu https://{server_domain}/.well-known/agent-card.json, interrogation de catalogues d'agents curés, et configuration directe d'URL ou de contenu de carte d'agent — et n'assortit la mention des catalogues d'aucun protocole de registre ou de courtage spécifié dans cette sous-section.

**Balayage (degré 1)** — Balayage de la sous-section 8.2 du fichier docs/specification.md du dépôt a2aproject/A2A, branche main, consulté le 21 juillet 2026 (l'ancre HTML #8-agent-discovery-the-agent-card du site a2a-protocol.org renvoyait un contenu tronqué, voir failures). Chaînes cherchées dans la sous-section : « registry », « registries », « catalog », « broker ». Résultat : l'énumération comporte exactement trois entrées (Well-Known URI, Registries/Catalogs, Direct Configuration) et aucune n'est accompagnée d'un mécanisme normatif de registre. Le balayage porte sur cette seule sous-section : il ne dit rien du reste de la spécification, notamment de la section 7 (Authentication and Authorization) ni de la sous-section 8.4 (Agent Card Signing).

- **primaire** — Agent2Agent (A2A) Protocol Specification — §8.2 Discovery Mechanisms — Latest Released Version 1.0.0 ; branche main consultée le 21 juillet 2…, consultée le 2026-07-21 — <https://raw.githubusercontent.com/a2aproject/A2A/main/docs/specification.md>
  > Well-Known URI: Accessing `https://{server_domain}/.well-known/agent-card.json` […] Registries/Catalogs: Querying curated catalogs of agents […] Direct Configuration: Pre-configured Agent Card URLs or content

**Réserve** — Niveau C assumé : la sous-section a été lue au travers d'un outil d'extraction et non par lecture intégrale du fichier ; le balayage est borné à 8.2. Le relevé ne soutient pas l'énoncé plus large « A2A ne prévoit pas de courtage » — il ne le réfute pas davantage.

### `L13-A7` — [B]

NIST SP 800-207 « Zero Trust Architecture », publié en août 2020, pose que l'authentification et l'autorisation — du sujet comme de l'appareil — sont des fonctions discrètes exécutées avant l'établissement d'une session vers une ressource d'entreprise, et que la protection porte sur les ressources et non sur les segments de réseau.

- **primaire** — NIST Special Publication 800-207, Zero Trust Architecture — version finale, août 2020, consultée le 2026-07-21 — <https://csrc.nist.gov/pubs/sp/800/207/final>
  > Authentication and authorization (both subject and device) are discrete functions performed before a session to an enterprise resource is established. […] Zero trust focuses on protecting resources (assets, services, workflows, network accounts, etc.), not network segments, as the network location is no longer seen as the prime component to the security posture of the resource.

**Réserve** — Le document est de 2020 et ne traite pas des agents logiciels autonomes ; toute transposition agentique est une construction d'auteur à marquer comme telle, non un contenu de SP 800-207.

### `L13-A8` — [B]

Le document du NIST consacré à l'identité et à l'autorisation des agents logiciels et d'IA — « [Concept Paper] Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization », publié le 5 février 2026 par le NCCoE — est un concept paper au stade de projet public initial (Initial Public Draft) appelant des commentaires jusqu'au 2 avril 2026 : un document pré-normatif de cadrage de projet, ni norme, ni révision de SP 800-207.

- **primaire** — [Concept Paper] Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authoriza… — Other (Initial Public Draft), 5 février 2026 ; commentaires jusqu'au 2…, consultée le 2026-07-21 — <https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd>
  > AI agents—software systems that use data and algorithms to autonomously perform tasks—offer the promise of improved productivity, efficiency, and decision-making in complex scenarios.
- **primaire** — NIST CSRC — recherche de publications, mot-clé « agentic » — requête exécutée le 21 juillet 2026, consultée le 2026-07-21 — <https://csrc.nist.gov/publications/search?keywords-lg=agentic>
  > [Concept Paper] Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization — Draft — 2/05/2026 ; CSWP 53 (Initial Public Draft) Charting the Course for NIST OSCAL — Draft — 12/02/2025

**Réserve** — Prospective PROJETÉ : le document annonce l'intention de lancer un projet de démonstration au NCCoE, sans engagement daté de livraison constaté. Les normes d'identité candidates (OAuth 2.0, OpenID Connect, SPIFFE/SPIRE) circulent dans des analyses secondaires ; la fiche CSRC consultée ne les nomme pas et le PDF du NCCoE n'a pas été ouvert lors de ce lot — l'énoncé ne les reprend donc pas. L'absence d'une déclinaison agentique publiée de SP 800-207 relève du degré 3 : la recherche par mot-clé « agentic » dans le moteur de publications du NIST ne retourne que deux entrées, et une requête par chaîne n'établit aucune absence.

### `L13-A9` — [B]

Le terme « agent mesh » désigne deux objets techniquement distincts chez deux fournisseurs consultés : chez Solo.io, une couche de connectivité posée par analogie avec le service mesh pour traiter sécurité, observabilité, cloisonnement et garde-fous (communiqué du 24 avril 2025) ; chez Solace, un cadriciel applicatif multi-agents bâti sur le Solace AI Connector, le Google Agent Development Kit et le protocole A2A (dépôt SolaceLabs/solace-agent-mesh, version 1.28.4 du 29 juin 2026).

- **primaire** — Solo.io Launches Agent Gateway and Introduces Agent Mesh for Unified AI Connectivity — 24 avril 2025, consultée le 2026-07-21 — <https://www.solo.io/press-releases/solo-io-launches-agent-gateway-and-introduces-agent-mesh>
  > Just like microservices created the need for a service mesh to address cross-cutting concerns at the connectivity layer, agents require an Agent Mesh to solve common security, observability, tenancy, and guardrail concerns.
- **primaire** — SolaceLabs/solace-agent-mesh (README) — version 1.28.4, 29 juin 2026 ; licence Apache-2.0, consultée le 2026-07-21 — <https://github.com/SolaceLabs/solace-agent-mesh>
  > Solace Agent Mesh is a framework that supports building AI applications where multiple specialized AI agents work together to solve complex problems. […] SAM is built on top of the Solace AI Connector (SAC) which allows Solace Platform Event Brokers to connect to AI models and services and Google's Agent Development Kit (ADK) for AI logic and tool integrations. […] Agents can discover and delegate tasks to each other seamlessly using the Agent2Agent (A2A) Protocol.

**Réserve** — Le relevé porte sur deux fournisseurs seulement : il ne dresse pas la liste des emplois du terme et n'autorise aucune clause d'exclusivité. Aucune définition normative de « agent mesh » n'a été rencontrée dans un texte de norme ouvert au cours de ce lot — degré 3 (absence de documentation dans le corpus consulté), non un fait négatif. Le communiqué Solo.io ne comporte aucun énoncé de disponibilité pour l'Agent Mesh lui-même : sur l'échelle demandée, il relève de l'ANNONCE.

