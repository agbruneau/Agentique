# Chapitre 4 — Interopérabilité verticale agent-outil : Model Context Protocol (MCP), passerelles et intégration du patrimoine

La Partie I a montré qu’un agent d’entreprise fiable repose sur un noyau déterministe — l’`Agent Harness` — bornant l’inférence probabiliste derrière des contrats typés. Isolé dans son environnement d’exécution (`SHADI`, `gVisor` ou `Firecracker`), ce noyau demeure toutefois inopérant sans accès gouverné aux données et transactions du système d’information. La Partie II adresse donc le Plan 3 d’interopérabilité défini au chapitre 2. Ce chapitre 4 traite exclusivement de l’**interopérabilité verticale agent-outil** : la découverte, l’ergonomie sémantique, la médiation en passerelle et l’encapsulation patrimoniale permettant à un agent d’invoquer des capacités déterministes. La coopération horizontale inter-agents relève du chapitre 5 (`A2A` et `AGNTCY`), l’ingénierie des mémoires du chapitre 6, et la chaîne cryptographique d’identité (`SPIFFE`, `OAuth OBO`, `OPA` /`Cedar`) du chapitre 10.

Pour l’architecte d’entreprise (`EA`), l’enjeu consiste à éliminer les connecteurs point-à-point tout en maîtrisant les coûts `FinOps` et la protection des `Systems of Record` (`ERP`, `CRM`, mainframes). Pour l’architecte de solutions (`SA`), il s’agit de concevoir des interfaces adaptées à un consommateur probabiliste, de bâtir des `MCP Gateways` multiprotocoles (`REST`, `gRPC`, `GraphQL`) et d’isoler le patrimoine par des couches anti-corruption.

## 4.1 Du couplage M × N au standard MCP : architecture sans état, primitives et négociation

### 4.1.1 Du couplage quadratique M × N à la gouvernance ouverte sous l’AAIF

Avant l’émergence d’un protocole vertical unifié, relier M environnements d’agents à N systèmes d’entreprise imposait autant de connecteurs dédiés [55]. Ce couplage quadratique `M × N` dupliquait le code d’authentification, fragilisait les déploiements à chaque évolution d’`API` et fragmentait l’auditabilité [55] [56]. Introduit par Anthropic en novembre 2024, le `Model Context Protocol` (`MCP`) ramène cette intégration à une complexité additive `M + N` : l’hôte implémente un client unique tandis que chaque domaine expose un serveur conforme au même contrat filaire [57] [55].

Pour garantir une pérennité indépendante des fournisseurs d’inférence, la Linux Foundation a lancé le 9 décembre 2025 l’`Agentic AI Foundation` (`AAIF`), portée par les contributions fondatrices d’Anthropic (`MCP`), de Block (`goose`) et d’OpenAI (`AGENTS.md`), avec comme membres Platine AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft et OpenAI [57]. Cette gouvernance neutre protège les architectures d’entreprise contre tout enfermement propriétaire.

Sur le plan structurel, `MCP` sépare trois rôles sur une enveloppe `JSON-RPC 2.0` [58] [59] :

1. **L’Hôte (**`MCP Host`**)** héberge l’`Agent Harness`, orchestre le modèle de langage, gère les consentements et agrège les contextes [58] [60].
2. **Le Client (**`MCP Client`**)** maintient au sein de l’hôte une liaison dédiée `1:1` avec un serveur donné, attache les métadonnées protocolaires à chaque requête et isole les domaines de confiance [58].
3. **Le Serveur (**`MCP Server`**)** expose de manière autonome outils, ressources et gabarits devant un système métier ou un gisement de données [58].

L’enveloppe `JSON-RPC 2.0` (`jsonrpc`, `method`, `params`, `id`, `result` ou `error`) découple le contrat applicatif du transport [58] [59]. En exécution locale confinée, le transport `stdio` communique sur l’entrée et la sortie standard du sous-processus (réservant `stderr` aux journaux), tandis qu’en réseau distribué d’entreprise, `Streamable HTTP` devient l’unique standard actif, reléguant l’ancien transport `HTTP + SSE` (`2024-11-05`) au statut déprécié [58] [60].

### 4.1.2 Le virage sans état de la révision 2026-07-28 et le transport Streamable HTTP

Jusqu’à la révision `2025-11-25`, `MCP` reposait sur un cycle à état de session : une poignée de main obligatoire (`initialize` puis `notifications/initialized`) émettait un identifiant `Mcp-Session-Id` conservé en mémoire serveur, accompagné d’un point d’accès `HTTP GET` permanent et de la reprise `SSE` par `Last-Event-ID` [58]. En production distribuée, cette affinité de session compliquait le passage à l’échelle derrière les répartiteurs de charge L7 et les environnements sans serveur (*serverless*) [58].

La spécification `2026-07-28` résout cette limitation en adoptant une architecture **strictement sans état** (*stateless*) [58] :

- **Suppression de la session et du handshake** : `Mcp-Session-Id` et l’échange `initialize` disparaissent du modèle moderne; les réponses de découverte (`tools/list`, `resources/list`, `prompts/list`) ne varient plus par connexion ni par effet de bord d’autres appels sur la connexion, tout en pouvant être filtrées selon les droits d’autorisation présentés sur la requête [58].
- **Négociation par requête via** `_meta` **et** `server/discover` : chaque appel transporte dans `_meta` la version protocolaire (`io.modelcontextprotocol/protocolVersion`), les capacités (`io.modelcontextprotocol/clientCapabilities`) et l’identité (`io.modelcontextprotocol/clientInfo`), doublés sur `HTTP` par l’en-tête `MCP-Protocol-Version` [58]. En cas d’écart, le serveur retourne `UnsupportedProtocolVersionError` (`-32022`) listant les versions `supported` pour permettre un réessai immédiat [58]. Tout serveur doit en parallèle implémenter `server/discover`, offrant aux clients et passerelles une inspection en un appel des versions et capacités supportées (ainsi qu’une sonde de rétrocompatibilité sur `stdio`) [58].
- **Point de terminaison** `POST` **unique en** `Streamable HTTP` : le serveur n’expose qu’une route `POST` (par exemple `/mcp`); il répond par un document JSON (`200 OK`, `application/json`) ou ouvre un flux `text/event-stream` (`SSE`) strictement borné à la requête courante (avec `X-Accel-Buffering: no` contre la mise en tampon des mandataires) pour émettre des `notifications/progress` avant la réponse finale [58]. Les notifications reçoivent un `202 Accepted`, et toute coupure réseau impose de réémettre la requête avec un nouvel `id` [58].

Lorsqu’un traitement métier exige un suivi multi-étapes (panier, session de navigation), le serveur délivre un **jeton d’état explicite** opaque et entropique passé comme argument ordinaire des appels ultérieurs, en validant l’autorisation à chaque invocation et en documentant son expiration [58]. Sur `Streamable HTTP`, les en-têtes obligatoires `Mcp-Method` et `Mcp-Name`, complétés par la projection `x-mcp-header` (`Mcp-Param-{name}` sur paramètres primitifs non sensibles, à l’exclusion stricte des secrets et `PII`), permettent aux équipements L7 d’aiguiller ou de limiter les requêtes sans désérialiser le JSON-RPC [58]. La figure 4.1 et le tableau 4.1 synthétisent cette mécanique.

> **[Figure]**
> - Hôte & Client MCP
> - (Agent Harness)
> - Passerelle / Serveur MCP (Point POST /mcp unique)
> - Système aval (API / Données)
> - Hôte & Client MCP
> - (Agent Harness)
> - Passerelle / Serveur MCP (Point POST /mcp unique)
> - Système aval (API / Données)
> - 1. Découverte sans état et cache (ttlMs)
> - 1 POST server/discover (_meta.protocolVersion: "2026-07-28", MCP-Protocol-Version)
> - 2 200 OK (supportedVersions, capabilities, ttlMs, cacheScope: "public")
> - 3 POST tools/list (cursor optionnel)
> - 4 200 OK (tools[], nextCursor, ttlMs, cacheScope)
> - 2. Invocation, MRTR et flux SSE par requête
> - 5 POST tools/call (Mcp-Method, Mcp-Name, Mcp-Param-\*)
> - alt [Information complémentaire requise (MRTR)]
> - 6 200 OK (resultType: "input_required", inputRequests, requestState)
> - 7 Collecte inputResponses (saisie ou approbation)
> - 8 POST tools/call (nouvel id, inputResponses + requestState)
> - 9 Appel métier normalisé (idempotent)
> - 10 Réponse aval
> - 1 1
> - 200 OK (text/event-stream SSE : notifications/progress -> resultType: "complete", structuredContent)
> - 3. Notifications sur abonnement explicite
> - 12 POST subscriptions/listen (toolsListChanged: true)
> - 13 Flux SSE ouvert (notifications/subscriptions/acknowledged)
> - 14 SSE : notifications/tools/list_changed

*Fig. 13. – Séquence protocolaire MCP 2026-07-28 : découverte sans état, transport Streamable HTTP, reprise MRTR et cache ttlMs*

| Dimension | Révision `2025-11-25` (avec session) | Révision `2026-07-28` (sans état) | Impact architectural `SA` |
| --- | --- | --- | --- |
| État et négociation | Handshake `initialize` et `Mcp-Session-Id` | Sans état; `_meta` par requête et `server/discover` | Répartition `L7` et mise à l’échelle horizontale sans affinité [58] |
| Transport `HTTP` | `POST` + `GET` SSE et reprise `Last-Event-ID` | Point `POST` unique; `SSE` borné à la requête; `subscriptions/listen` | Traversée simplifiée des pare-feux; réessai idempotent sur coupure [58] |
| Retours vers le client | Appels inverses (`sampling`, `elicitation`, `roots`) | `MRTR` (`resultType: "input_required"` + `requestState`) | Supprime les RPC inverses asymétriques derrière passerelle [58] |
| Cache de découverte | Heuristiques locales ou `listChanged` seul | Champs requis `ttlMs` et `cacheScope` (`"public"` /`"private"`) | Réduit la charge de découverte sur passerelles et `SoR` [58] |
| Tâches longues | Expérimentales dans le cœur (`tasks/result`) | Extension `tasks` (`tasks/get`, `tasks/update`) | Isole les workflows asynchrones longs du cœur synchrone [58] |
| Routage L7 | Lecture obligatoire du corps `JSON-RPC` | En-têtes `MCP-Protocol-Version`, `Mcp-Method`, `Mcp-Name`, `Mcp-Param-*` | Filtrage et routage régional à la vitesse du plan réseau [58] |

*Tableau 4.1 — Évolution structurante entre les révisions* `2025-11-25` *et* `2026-07-28` *du protocole* `MCP`*.*

### 4.1.3 Primitives serveur, modèle MRTR, schémas de sortie et cache natif

`MCP` classe les capacités serveur selon l’acteur qui en garde l’initiative [58] :

- **Outils (**`Tools`**, contrôlés par le modèle)** : opérations découvertes par `tools/list` et exécutées par `tools/call` [58]. Chaque outil spécifie un nom (1 à 128 caractères ASCII `A-Z`, `a-z`, `0-9`, `_`, `-`, `.`), une description, un `inputSchema` (`JSON Schema 2020-12` par défaut), un `outputSchema` optionnel et des `ToolAnnotations` (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) [58]. Fait déterminant pour les coûts d’inférence, `tools/list` doit retourner les outils dans un **ordre déterministe** afin de préserver les taux de succès du cache de prompt côté modèle [58].
- **Ressources (**`Resources`**, contrôlées par l’hôte)** : données adressables par `URI` (`resources/list`, `resources/read`, `resources/templates/list`) munies d’annotations de priorité et de fraîcheur [58].
- **Gabarits (**`Prompts`**, contrôlés par l’utilisateur)** : modèles paramétrables (`prompts/list`, `prompts/get`) exposés comme raccourcis structurés dans l’interface hôte [58].

Afin d’éliminer les requêtes RPC inverses du serveur vers le client, la révision `2026-07-28` déprécie `Roots`, `Sampling` et `Logging` (`SEP-2577`) et généralise le mécanisme **Multi Round-Trip Requests (**`MRTR`**)** [58].

Tout résultat porte `resultType` (`"complete"` ou `"input_required"`): lorsqu’une approbation ou saisie complémentaire est requise, le serveur retourne un `InputRequiredResult` (`inputRequests` et `requestState`), permettant au client de soumettre à nouveau `tools/call` muni de `inputResponses` et d’un nouvel `id` [58].

La robustesse des contrats s’appuie en outre sur `outputSchema` et `structuredContent` (validant la charge produite par le serveur, distincte des *Structured Outputs* du modèle vus au chapitre 3, et doublée en texte sérialisé pour compatibilité), ainsi que sur la distinction entre fautes protocolaires (`-32602` pour outil inconnu ou schéma invalide) et erreurs métier (`isError: true`) fournissant des indices d’auto-correction à l’agent [58]. Les résultats complets (`resultType: "complete"`) de découverte et lecture (`server/discover`, `tools/list`, `resources/list`, `resources/read`, `prompts/list`) incluent obligatoirement `ttlMs` (durée de fraîcheur en millisecondes vérifiée par `now < t_received + ttlMs`, sans déclencher de scrutin automatique) et `cacheScope` (`"public"` pour les intermédiaires partagés ou `"private"` par client), tandis que les réponses `input_required` et les requêtes portant `inputResponses` ou `requestState` ne doivent jamais être mises en cache [58]. En parallèle, `_meta` standardise la propagation `OpenTelemetry` (`traceparent`, `tracestate`, `baggage`) et `logLevel` par requête [58].

### 4.1.4 Double lecture EA / SA

Pour l’`EA`, `MCP` sous gouvernance `AAIF` unifie le Plan 3 en supprimant le couplage fournisseur, mais exige de rappeler que les `ToolAnnotations` demeurent **des indications non fiables** sur tout serveur non certifié et ne sauraient fonder une décision de sécurité [58] [57]. Pour le `SA`, le passage au protocole sans état `2026-07-28` impose de gérer la persistance applicative hors connexion (jetons explicites ou moteur durable du chapitre 9) et d’exploiter `ttlMs` ainsi que les en-têtes `Mcp-Method` /`Mcp-Param-*` dès la frontière réseau [58].

> **Arbitrage EA / SA** — Adopter la spécification `MCP` (`Streamable HTTP` sans état, révision `2026-07-28` avec repli documenté si requis) comme contrat vertical unique entre l’`Agent Harness` et les systèmes d’outils, en écartant `HTTP + SSE` sur tout nouveau projet [58] [57]. L’`EA` interdit d’accorder une confiance de sécurité aux seules `ToolAnnotations` et impose l’audit des serveurs autorisés; le `SA` exploite `server/discover`, le tri déterministe de `tools/list`, les en-têtes `Mcp-Method` /`Mcp-Name` /`Mcp-Param-*` et les bornes `ttlMs` /`cacheScope` pour bâtir une couche verticale sans affinité de session [58].

## 4.2 Ergonomie sémantique des outils (Agent-Computer Interface) contre l’anti-patron Swagger-to-MCP

### 4.2.1 Principes de l’Agent-Computer Interface (ACI)

Un transport standardisé ne garantit ni la justesse de sélection ni l’efficacité d’un outil. Dans *SWE-agent*, Yang et al. ont établi le concept d’`Agent-Computer Interface` **(**`ACI`**)** en montrant que les agents de langage forment une classe d’utilisateurs distincte des humains et des programmes déterministes [61]. En dotant le modèle d’une interface sur mesure — intégrant un visualiseur et un éditeur de fichiers dédiés, des commandes de recherche et de navigation dans les dépôts ainsi que l’exécution de tests — `SWE-agent` a atteint `12,5 %` de réussite `pass@1` sur `SWE-bench` et `87,7 %` sur `HumanEvalFix` [61].

Anthropic transpose ce principe à l’ingénierie des serveurs `MCP` : un outil incarne un contrat entre un système déterministe et un consommateur non déterministe [62]. Ses noms, descriptions, paramètres et retours appartiennent de plein droit à l’ingénierie du contexte : l’interface la plus claire pour l’agent se révèle du même coup la plus lisible pour les équipes d’exploitation [62].

### 4.2.2 L’anti-patron Swagger-to-MCP : saturation, confusion et double transit

Face à des centaines d’`API` existantes, la tentation répandue consiste à générer automatiquement un serveur `MCP` en traduisant chaque route `OpenAPI` /`Swagger` (`GET`, `POST`, `PATCH`, `DELETE`) en un outil individuel. Cet **anti-patron** `Swagger-to-MCP` engendre quatre défaillances critiques en production [62] [55] [63] :

1. **Saturation de la fenêtre de contexte** : un portefeuille applicatif ou `SaaS` compte aisément plusieurs centaines d’opérations [64] [63]. L’injection statique de tous les schémas d’entrée dans le contexte consomme des centaines de milliers de jetons avant même le traitement de la requête utilisateur, gonflant les coûts et la latence [55] [63].
2. **Confusion d’outils (**`tool confusion`**)** : devant des grappes d’opérations granulaires quasi synonymes (`get_user`, `list_users`, `get_user_details`), le modèle sélectionne la mauvaise route ou hallucine des clés étrangères manquantes [62] [63].
3. **Double traversée des charges intermédiaires** : en invocation directe, toute donnée lue d’un outil transite par la fenêtre de contexte du `LLM` pour être recopiée vers l’outil suivant [55] [64]. Anthropic montre qu’un transfert de transcription d’une réunion de deux heures entre `Google Drive` et `Salesforce` injecte environ `50 000` jetons supplémentaires dans la boucle, tout en augmentant le risque d’erreur de copie [55].
4. **Rejet technique des schémas** `OpenAPI` **complexes** : les spécifications destinées aux développeurs abondent en constructions polymorphiques (`oneOf`, `anyOf`, `allOf`) et en sérialiseurs complexes d’en-têtes ou de *cookies*. Comme le précise la documentation d’`Amazon Bedrock AgentCore Gateway`, ces mots-clés combinatoires, les contrats `Swagger 2.0` et ces sérialiseurs sont incompatibles avec la conversion vers les `ToolSpec` des modèles [65].

La figure 4.2 met en contraste l’empilement `Swagger-to-MCP` naïf et l’architecture `ACI` consolidée.

> **[Figure]**
> - Anti-patron : Wrapper
> - Swagger-to-MCP 1:1
> - Architecture cible : Façade ACI et
> - découverte dynamique
> - Harnais LLM (Contexte saturé)
> - Catalogue brut 200+ outils CRUD Endpoints fins GET / POST / PATCH
> - Sélection erratique & double transit de jetons
> - Harnais LLM (Contexte épuré)
> - Tool Search ou Code Mode isolé
> - Outils ACI consolidés (Intention métier)
> - Orchestrateur aval (REST / OData agrégé)
> - Charge tous les schémas d'entrée
> - Appels séquentiels
> - sans agrégation
> - Payloads bruts renvoyés au LLM
> - Charge à la demande
> - (schémas pertinents)
> - Contrats sémantiques
> - & outputSchema
> - Enchaîne et filtre avant retour concis

*Fig. 14. – Comparaison structurelle entre l’anti-patron Swagger-to-MCP 1:1 et l’architecture ACI consolidée*

### 4.2.3 Remédiations : façades d’intention, Dynamic Toolsets, Code Mode et intégrité OWASP

Quatre leviers permettent d’éradiquer l’anti-patron `Swagger-to-MCP` tout en sécurisant la surface sémantique des outils.

**Façades consolidées par intention métier.** Plutôt que d’exposer des primitives `CRUD` fragmentaires, il faut assembler des outils orientés workflow (`schedule_event`, `get_expenses_by_date_range`) qui exécutent de façon déterministe la séquence d’appels aval [62]. Anthropic recommande un espace de nommage strict par domaine (`slack_search`), le retour d’identifiants sémantiques lisibles plutôt que d’`UUID` opaques, un paramètre `response_format` (`"concise"` ou `"detailed"`) régulant la verbosité, la pagination bornée et une boucle d’évaluation automatisée mesurant l’impact de chaque révision de schéma [58] [62].

**Découverte progressive (**`Dynamic Toolsets` **contre** `tool search` **natif).** Pour les vastes catalogues, Speakeasy a évalué sur des ensembles de 40 à 400 outils le patron `Dynamic Toolsets` articulé autour de trois méta-outils : `search_tools` (recherche sémantique par plongements avec aperçu des catégories et filtres d’étiquettes), `describe_tools` (chargement différé du schéma d’entrée) et `execute_tool` [63]. Sur ces bancs de test, cette approche a réduit la consommation jusqu’à `160×` (en moyenne `96 %` des jetons d’entrée et `90 %` au total) tout en préservant `100 %` de succès [63]. Toutefois, Speakeasy souligne que les harnais clients modernes intégrant nativement un `tool search` différé au niveau de l’inférence, embarquer une seconde couche de recherche à l’intérieur d’un serveur `MCP` unitaire entre en concurrence avec le modèle et dégrade la découvrabilité [66]. La recherche dynamique appartient donc au harnais ou à la passerelle fédérée, non à chaque serveur isolé [66].

**Exécution programmatique (**`Code Mode`**).** Formalisée par Anthropic et Cloudflare (Kenton Varda et Sunil Pai), l’architecture `Code Mode` projette les outils `MCP` sous forme d’`API TypeScript` typées [55] [64]. Parce que les `LLM` ont assimilé un volume massif de code `TypeScript` réel comparativement aux jetons synthétiques d’appel de fonction, le modèle rédige un script court qui enchaîne, filtre et agrège plusieurs appels sans repasser les résultats intermédiaires par le contexte [55] [64]. Chez Cloudflare, ce script s’exécute dans un isolat `V8 Dynamic Worker` privé d’accès Internet direct et raccordé uniquement par liaisons internes aux serveurs `MCP` autorisés, maintenant les clés d’`API` hors de portée du code généré [64] [66].

**Défense sémantique contre les menaces** `OWASP`**.** Puisque toutes les descriptions et valeurs de retour cohabitent dans la même fenêtre contextuelle du modèle, l’`OWASP MCP Top 10` et l’`OWASP MCP Security Cheat Sheet` identifient trois risques critiques au niveau `ACI` : le `Tool Poisoning` (instructions cachées dans les descriptions ou retours), les `Rug Pull Attacks` (altération malveillante d’un outil après approbation initiale) et le `Tool Shadowing` (détournement inter-serveurs au sein du même hôte) [67] [60]. La validation stricte des schémas et la vérification d’empreinte des définitions approuvées deviennent ainsi des exigences d’ingénierie de base [60]. Le tableau 4.2 résume ces arbitrages.

| Critère | `Swagger-to-MCP` 1:1 | Façade `ACI` d’intention | `Dynamic Toolsets` / `Tool Search` | `Code Mode` en isolat |
| --- | --- | --- | --- | --- |
| Granularité | Routes `CRUD` brutes | Outils métier consolidés | Indexation et chargement paresseux | Modules `TypeScript` en bac à sable |
| Empreinte contextuelle | Massive (saturation rapide) [55] [63] | Faible par domaine [62] | Réduite jusqu’à `160×` (`90 %` total) [63] | Minimale (synthèse seule retournée) [55] [64] |
| Données intermédiaires | Double traversée par le `LLM` [55] | Filtrées en sortie (format concis) [62] | Transitent à l’appel d’exécution | Agrégées dans l’isolat sans repasser par le `LLM` [55] [64] |
| Précision du modèle | Dégradée (`tool confusion`) [62] | Élevée si validée par évaluations [62] | `100 %` sur bancs 40–400 outils [63] | Très élevée sur enchaînements complexes [64] |
| Contraintes d’adoption | Schémas `oneOf` / `allOf` rejetés [65] | Coût de conception de façade [62] | Éviter la redondance avec le harnais [66] | Nécessite isolat `V8` ou microVM sans réseau [64] [66] |

*Tableau 4.2 — Comparaison des approches d’ergonomie sémantique et de passage à l’échelle des outils* `MCP`*.*

### 4.2.4 Double lecture EA / SA

Pour l’`EA`, proscrire la conversion mécanique `Swagger-to-MCP` protège les budgets `FinOps` contre le gonflement des jetons d’entrée et assure que les agents n’interagissent qu’avec des capacités métier homologuées [62] [55]. Pour le `SA`, l’ergonomie `ACI` impose de tester empiriquement chaque outil sur des cas complexes, d’aplatir les contrats JSON, de prévoir la troncature des sorties et de verrouiller cryptographiquement les définitions entre déploiements contre le `Rug Pull` [62] [60] [65].

> **Arbitrage EA / SA** — Interdire en revue d’architecture (`ARB`) la mise en production de convertisseurs `Swagger-to-MCP` exposant directement les routes `CRUD` sans curation [62] [63] [65]. Le `SA` conçoit des façades `ACI` orientées intention dotées de paramètres de pagination/`response_format`, d’`outputSchema` et d’erreurs `isError: true` correctives, tout en confiant le chargement différé au `tool search` client ou à un `Code Mode` confiné à la passerelle [58] [62] [66]. L’`EA` impose le contrôle d’intégrité des descriptions et schémas en intégration continue contre le `Tool Poisoning` et le `Rug Pull` [67] [60].

## 4.3 Architecture des MCP Gateways d’entreprise : médiation REST/gRPC/GraphQL, cache et découverte dynamique

### 4.3.1 Convergence vers la MCP Gateway d’entreprise

Brancher chaque `Agent Harness` directement sur des dizaines de serveurs hétérogènes (`stdio` locaux, services distants, connecteurs tiers) multiplie les angles morts de sécurité et favorise l’apparition de `Shadow MCP Servers` non inventoriés dénoncés par l’`OWASP` [67] [60]. La `MCP Gateway` centralise cette couche verticale du Plan 3 autour de deux familles complémentaires :

- **Les plans de données nativement agentiques (**`AAIF`**)** : écrit en `Rust`, `Agentgateway` fédère dans un unique proxy le routage `HTTP` /`gRPC`, l’aiguillage `LLM` et la médiation `MCP` (`stdio`, `HTTP`, `SSE`, `Streamable HTTP`, traduction `OpenAPI`), avec moteur de politiques `CEL` par outil, limitation de débit et traces `OpenTelemetry` [68] (son versant `A2A` relevant du chapitre 5). De son côté, `Agent Router` (anciennement `Envoy AI Gateway`) s’appuie sur `Envoy` et `Envoy Gateway` via des ressources déclaratives (`AIGatewayRoute`, `AIServiceBackend`) et `ExtProc` sur `gRPC` pour multiplexer les serveurs `MCP` et appliquer des règles `CEL` granulaires [69].
- **Les passerelles d’**`API Management` **et iPaaS étendues** : `Azure API Management` (`APIM`) projette sélectivement des opérations `REST` gérées ou encapsule des serveurs `MCP` externes derrière ses produits et politiques [70]; `Amazon Bedrock AgentCore Gateway` traduit des contrats `OpenAPI 3.0` /`3.1` en outils gouvernés [65]; et `MuleSoft Agent Fabric` (`Omni Gateway` / `MCP Bridge`) expose les actifs `API-led` existants sans réécriture applicative [56].

### 4.3.2 Médiation multiprotocole : REST/OpenAPI, gRPC et GraphQL

La valeur opérationnelle d’une `MCP Gateway` tient à sa capacité de médier les protocoles déjà en place sans imposer de réécrire chaque microservice :

- **Médiation** `REST / OpenAPI` : l’importation déclarative de contrats `OpenAPI 3.0` /`3.1` exige une sélection rigoureuse des opérations, des `operationId` explicites devenant les noms d’outils, des schémas aplatis sans `oneOf` /`anyOf` /`allOf` ni sérialiseurs complexes (`AgentCore`) et le respect du périmètre fonctionnel (`APIM` ne supportant par exemple que les `Tools`, sans `Resources` ni `Prompts`) [70] [65]. Microsoft avertit également d’un écueil d’exploitation critique dans `APIM` : désactiver globalement la journalisation des corps de réponse (`Number of payload bytes to log = 0`), sans quoi les échanges `MCP` peuvent être altérés ou exposés [70].
- **Médiation** `gRPC` : s’appuyant sur des ressources Kubernetes natives telles que `GRPCRoute` dans `Agentgateway`, la passerelle achemine le trafic par nom de service et de méthode `Protobuf` et propage les statuts `grpc-status` [68]. Pour exposer ces services en `MCP`, une couche adaptatrice sur la passerelle projette les contrats sélectionnés vers `JSON Schema 2020-12`, applique des *deadlines* strictes et convertit les traitements progressifs en notifications `notifications/progress` sur `SSE` borné [58].
- **Médiation** `GraphQL` **par requêtes persistées** : exposer l’introspection `GraphQL` ouverte à un `LLM` l’autoriserait à émettre des requêtes imbriquées coûteuses (`N+1`) et à extraire des sous-graphes massifs. L’architecture recommandée par `Apollo GraphQL` (`Apollo MCP Server`) proscrit l’introspection en production et n’expose que des **requêtes persistées** approuvées via un manifeste (`persisted-query-manifest.json`) ou `GraphOS Uplink`, garantissant des sélections de champs strictement minimales et une liste blanche déterministe [71].

Au plan réseau, la passerelle exploite les en-têtes `Mcp-Method`, `Mcp-Name`, `MCP-Protocol-Version` et `Mcp-Param-*` (`x-mcp-header`) pour appliquer routage et quotas avant désérialisation JSON-RPC, tout en relayant `traceparent` dans `_meta` vers `OpenTelemetry` [58] [68] [69]. La figure 4.3 illustre cette topologie C4.

> **[Figure]**
> - MCP Gateway d'entreprise
> - (Agentgateway / Agent
> - Router / APIM)
> - [system]
> - «container» Terminaison Streamable
> - HTTP [POST /mcp + SSE]
> - Routage Mcp-Method,
> - Mcp-Name, en-têtes x-mcp-header
> - «container» Politiques & garde-fous
> - [CEL / Schémas]
> - RBAC par outil, quotas,
> - anti-poisoning
> - «container» Catalogue dynamique
> - [Registry / server.json]
> - Filtrage par portées et
> - ordre déterministe
> - «container» Cache & Code Mode
> - [ttlMs / Isolat V8]
> - Cache lectures et scripts multi-serveurs sans réseau
> - «container» Adaptateurs protocolaires
> - [Médiation aval]
> - OpenAPI 3.x curé, gRPC,
> - Persisted Queries
> - «container» Agent Harness
> - [Client MCP]
> - Tool Search et appels JSON-RPC
> - 2.0
> - «external_system» API REST / OpenAPI
> - Microservices JSON
> - «external_system» Services gRPC
> - Protobuf / GRPCRoute
> - «external_system» Graphe GraphQL
> - GraphOS Persisted Queries
> - «external_system» Télémétrie OTel (ch. 11)
> - Traces _meta.traceparent
> - Valide contrat
> - et droits
> - Résout outils
> - autorisés
> - Médiation si défaut cache
> - Appels MCP [Streamable HTTP]
> - Vérifie cache
> - ou exécute
> - Émet spans
> - OTel
> - Projette [HTTP / JSON]
> - Achemine [gRPC / Protobuf]
> - Exécute [Liste blanche]

*Fig. 15. – Topologie C4 d’une MCP Gateway d’entreprise assurant la médiation REST, gRPC et GraphQL*

### 4.3.3 Découverte dynamique, cache et placement de Code Mode

La passerelle orchestre trois mécanismes transversaux essentiels à l’échelle de l’entreprise. Premièrement, la **découverte dynamique** s’appuie sur le schéma normalisé `server.json` et les espaces de nommage vérifiés par `DNS` du `MCP Registry` officiel [72]. En adossant la passerelle à un sous-registre interne approuvé selon ce format, l’organisation bloque les paquets communautaires non audités (risque de chaîne d’approvisionnement `OWASP`) [72] [67] [60], préfixe automatiquement les noms d’outils pour prévenir les collisions entre serveurs (`search`) [58], filtre `tools/list` selon les droits de la requête et maintient un ordonnancement déterministe favorable au cache de prompt [58].

Deuxièmement, la **mise en cache** combine les indices protocolaires `ttlMs` et `cacheScope` (`"public"` ou `"private"`, exigés sur `server/discover`, `tools/list`, `resources/read` et `prompts/list`, à l’exclusion stricte des états `input_required` et reprises `MRTR`) [58] avec une politique de cache applicatif côté passerelle sur les appels `tools/call` ciblant des outils idempotents annotés `readOnlyHint: true`, amortissant les réessais répétés des boucles d’agents. La clé de cache respecte toujours la méthode et les paramètres discriminants (`uri` sur `resources/read`, `cursor` sur les listes paginées) afin d’éviter toute fuite inter-requêtes [58]. Troisièmement, comme le démontre Speakeasy, la passerelle constitue le point d’ancrage idéal pour `Code Mode` lorsqu’il s’agit de composer des données issues de multiples serveurs `MCP` hétérogènes dans un isolat `V8` sans accès réseau libre : les liaisons typées y agrègent les réponses en mémoire locale sans réintroduire de logique de recherche redondante dans chaque serveur unitaire [64] [66].

### 4.3.4 Double lecture EA / SA

Pour l’`EA`, la `MCP Gateway` met fin aux `Shadow MCP Servers`, impose un catalogue vérifié `server.json` et centralise le contrôle d’accès et la facturation avant même l’intégration complète `OAuth OBO` /`SPIFFE` du chapitre 10 [72] [67] [68]. Pour le `SA`, la discipline consiste à éviter la dérive vers un `ESB` monolithique : la passerelle gère exclusivement transport `Streamable HTTP`, médiation protocolaire, validation de schéma, cache et télémétrie, sans héberger d’orchestration métier complexe [58] [68] [71].

> **Arbitrage EA / SA** — Imposer le passage de tout flux vertical `Agent → Outil` par une `MCP Gateway` gouvernée (`Agentgateway`, `Agent Router`, `APIM` ou équivalent) raccordée à un registre interne calqué sur `server.json` [72] [67] [68] [69] [70]. L’`EA` interdit les connexions directes non inventoriées et impose le blocage de journalisation brute des corps de réponse (`payload bytes = 0`) sur les flux `MCP` [67] [70]. Le `SA` confine la passerelle aux rôles de médiation (`OpenAPI 3.x` curé, `GRPCRoute`, requêtes persistées `GraphQL`), de cache `ttlMs` et d’isolation `Code Mode` multi-serveurs sans logique métier imbriquée [58] [66] [65] [71].

## 4.4 Encapsulation du SI patrimonial : couches anti-corruption devant ERP, CRM et mainframes

### 4.4.1 Vulnérabilité des Systems of Record face aux rafales agentiques

Raccorder des agents autonomes aux systèmes patrimoniaux — progiciels `ERP` (`SAP`, `Oracle`), `CRM` (`Salesforce`) et mainframes `IBM Z` (`CICS`, `IMS`, `Db2`) — soumet ces actifs critiques à trois vulnérabilités structurelles :

1. **Dérive des coûts** `MIPS` **/**`MSU` **et saturation des quotas** : les boucles exploratoires et parallélisations d’agents génèrent des rafales de lectures imprévisibles susceptibles d’épuiser les plafonds journaliers d’`API` `SaaS` ou d’envoler la facturation processeur sur mainframe.

2. **Fuite sémantique des modèles hérités** : exposer directement des schémas alambiqués, des `API` obsolètes ou des interfaces transactionnelles héritées (telles que les transactions `CICS` /`IMS` et schémas `ERP` /`CRM` à centaines d’attributs techniques) contamine la fenêtre contextuelle de l’agent et multiplie les erreurs d’arguments [62] [73] [74] [56].
3. **Connectivité native sans amortisseur transactionnel** : des éditeurs intègrent désormais `MCP` directement dans leurs couches d’accès patrimoniales, à l’image d’`IBM z/OS Connect 3.0.98` (octobre 2025, `APAR PH68103` sur `z/OS 3.2`, `CICS 6.3` et `IMS TMRA` pour `POSIX(OFF)`), qui permet de publier des opérations `API` sur `z/OS` comme outils `MCP` [74]. Or exposer ces points d’accès bruts sans couche tampon priverait le mainframe de protection contre les boucles répétitives et la complexité des modèles hérités [73] [56].

### 4.4.2 Couche anti-corruption (ACL) et déplacement incrémental

La réponse architecturale canonique repose sur le patron `Anti-Corruption Layer` **(**`ACL`**)** défini en *Domain-Driven Design* et documenté par Microsoft [73]. Interposée entre la `MCP Gateway` et chaque `SoR`, l’`ACL` prend la forme d’une **façade** ou d’un **adaptateur** embarquant la logique de traduction bidirectionnelle sans altérer le système patrimonial; son adoption implique néanmoins un surcroît de latence, l’exploitation d’un service supplémentaire, un assainissement strict des entrées aux frontières de confiance et une journalisation structurée corrélée par identifiants de trace [73] :

- **Traduction bidirectionnelle de domaine** : l’`ACL` présente vers `MCP` des outils métier épurés et normalisés, puis convertit en aval vers `SAP` /`ERP`, `Salesforce` (`CRM`), `MuleSoft Omni Gateway` ou les `API` exposées par `IBM z/OS Connect` [73] [74] [56].
- **Traduction des fautes techniques en erreurs** `MCP` **actionnables** : les codes de retour cryptiques ou incidents `SoR` sont interceptés et reformulés en réponses `isError: true` intelligibles par l’agent sans divulguer la topologie interne du patrimoine [58] [73].
- **Coutures de modernisation incrémentale** : suivant les patrons de Martin Fowler (*Patterns of Legacy Displacement*), notamment `Legacy Mimic` et `Event Interception`, l’`ACL` exploite des coutures techniques existantes (files de messages, déclencheurs de base de données, interfaces intermédiaires) pour isoler puis déplacer progressivement les fonctions hors du monolithe sans réécriture risquée [75].

### 4.4.3 Découplage lecture/écriture par CDC (Debezium) et projections CQRS

Pour neutraliser l’impact de charge sur les `SoR`, l’`ACL` applique une séparation stricte de type `CQRS` entre consultations et mutations.

Côté **lectures**, un pipeline de capture par journaux de transactions (`Change Data Capture` **—** `CDC`) tel que `Debezium` (déployé sur `Kafka Connect`, en `Debezium Server` ou opérateur `Kubernetes`) capte en quasi-temps réel les insertions, mises à jour et suppressions directement depuis les journaux des bases supportées (`Db2`, `Oracle`, `PostgreSQL`, `SQL Server`) sans scrutation `SQL` intrusive [75] [76]. Ces flux événementiels (`CloudEvents`, patron `Outbox`) alimentent des **projections de lecture** `CQRS` modernes (indexation rapide, cache distribué à invalidation automatique) dédiées aux outils `readOnlyHint: true` [58] [76]. Les requêtes répétitives des agents n’atteignent plus ni les moteurs transactionnels `ERP` ni les `MIPS` du mainframe.

Côté **écritures**, toute mutation traverse la passerelle bornée de l’`ACL` vers les interfaces transactionnelles officielles (`z/OS Connect`, `MuleSoft`, `ERP`), soumise à trois verrous déterministes : validation des invariants métier en code applicatif, vérification d’une **clé d’idempotence** contre les doubles exécutions lors des réessais `Streamable HTTP`, et lissage de débit protégeant le `SoR`, avec recours à `MRTR` (`input_required`) pour toute opération irréversible exigeant une confirmation [58] [73] [56]. La figure 4.4 et le tableau 4.3 synthétisent ces patrons.

> **[Figure]**
> - Couche Anti-Corruption (ACL) & découplage CQRS
> - [system]
> - «container» Façade sémantique ACL
> - [Traducteur DDD]
> - Convertit modèles, clés
> - et erreurs isError
> - «container» Réplicat de lecture
> - [PostgreSQL / Redis]
> - Absorbe rafales
> - d'exploration
> - «container» Passerelle d'écriture
> - [Idempotence / Limiteur]
> - Lisse les mutations
> - vers les SoR
> - «container» Pipeline CDC asynchrone
> - [Debezium / Kafka]
> - Capture journaux sans scrutation SQL
> - «container» MCP Gateway
> - [Streamable HTTP]
> - Outils métier idempotents
> - «external_system» CRM (Salesforce)
> - System of Record — API / Flows
> - «external_system» ERP (SAP / Oracle)
> - System of Record —
> - Connecteurs / API
> - «external_system» Mainframe IBM Z
> - System of Record — z/OS
> - Connect / CICS / Db2
> - Lectures rapides
> - (readOnlyHint)
> - Appelle outil [JSON-RPC 2.0]
> - Écritures bornées (clé d'idempotence)
> - Mute [API CRM]
> - Mute [REST / iPaaS]
> - Déclenche [z/OS Connect]
> - Journaux Oracle / SQL
> - [CDC]
> - Journaux
> - Db2 [CDC]
> - Projette état quasi-temps réel

*Fig. 16. – Topologie C4 d’encapsulation du SI patrimonial par couche anti-corruption, CDC Debezium et séparation CQRS*

| Système cible | Médiation `MCP` | Maîtrise du contexte et coûts | Régime lectures / écritures | Contre-mesures prioritaires |
| --- | --- | --- | --- | --- |
| `REST / OpenAPI` | `MCP Gateway` (`APIM`, `AgentCore`, `Agentgateway`) [68] [70] [65] | Curation d’`operationId`; schémas sans `oneOf` /`allOf` [65] | Cache `ttlMs` + clés d’idempotence [58] | Proscription `Swagger-to-MCP`; logs payload à `0` [70] |
| Services `gRPC` | `GRPCRoute` et traduction `Protobuf` [68] | Pagination et conversion vers `progress` [58] [68] | Synchrones à *deadlines* strictes | Bornage des flux continus à la passerelle [68] |
| Graphes `GraphQL` | **Requêtes persistées** (`Apollo MCP Server`) [71] | Sélection minimale des champs; zéro introspection [71] | Liste blanche figée au *build* / `GraphOS` [71] | Blocage des requêtes profondes `N+1` [71] |
| `ERP / CRM` (`SAP`, `Salesforce`) | `ACL` + iPaaS (`MuleSoft Omni Gateway`) [73] [56] | Outils métier consolidés masquant schémas `ERP` /`CRM` [62] [73] | Consultations sur réplicat `CDC`; écritures lissées [56] [76] | Protection des quotas API `SaaS` et modèle `DDD` [73] |
| Mainframes `IBM Z` | `z/OS Connect` derrière `MCP Gateway` + `ACL` [73] [74] | Abstraction schémas hérités; retours synthétiques [62] [73] | Lectures `Db2` via `Debezium` `CDC` + `CQRS`; mutations bornées [74] [76] | Maîtrise `MIPS` /`MSU` et zéro branchement direct [73] [76] |

*Tableau 4.3 — Matrice décisionnelle de médiation* `MCP` *et d’encapsulation par famille de système cible.*

### 4.4.4 Double lecture EA / SA

Pour l’`EA`, l’association `ACL + CDC` ouvre le patrimoine aux agents sans compromettre la trajectoire de modernisation par *Legacy Displacement* ni exposer les budgets `MIPS` /`SaaS` aux rafales stochastiques [73] [75]. Pour le `SA`, aucun connecteur natif (`z/OS Connect`, `OData`) ne doit être exposé directement au modèle sans façade traductrice, réplicat de lecture `Debezium` et verrou d’idempotence [73] [74] [76].

> **Arbitrage EA / SA** — Imposer une **Couche Anti-Corruption (**`ACL`**)** et une **séparation** `CQRS` **alimentée par** `CDC` devant tout `ERP`, `CRM` ou mainframe raccordé à la `MCP Gateway` [73] [74] [76]. L’`EA` proscrit les lectures et écritures directes non amorties sur les `SoR` afin de protéger coûts `MIPS` /licences et intégrité comptable [73] [75]. Le `SA` route les outils `readOnlyHint: true` vers des projections `Debezium` à faible latence et encadre chaque mutation par idempotence, lissage de débit et validation `MRTR` lorsque le risque transactionnel l’exige [58] [76].

## Synthèse architecturale du chapitre

L’interopérabilité verticale agent-outil repose sur quatre invariants complémentaires : l’adoption du standard ouvert `MCP` **(**`2026-07-28`**)** sans état sur `Streamable HTTP` et métadonnées `_meta` [58] [57]; la conception d’interfaces `ACI` orientées intention métier, affranchies de l’anti-patron `Swagger-to-MCP` et protégées contre le `Tool Poisoning` [61] [62] [60]; la médiation centralisée via `MCP Gateway` couvrant `OpenAPI`, `gRPC`, requêtes persistées `GraphQL`, registre `server.json`, cache `ttlMs` et `Code Mode` isolé [72] [66] [68] [71]; et l’encapsulation des `SoR` patrimoniaux par `ACL`, `CQRS` et `CDC` **(**`Debezium`**)** [73] [74] [76]. Le chapitre 5 étend désormais cette couche vers la coopération horizontale inter-agents (`A2A` et `AGNTCY`), avant que le chapitre 6 n’organise la mémoire sémantique et que le chapitre 10 ne complète la gouvernance cryptographique des identités (`SPIFFE`, `OAuth OBO`) et des politiques (`OPA` /`Cedar`).
