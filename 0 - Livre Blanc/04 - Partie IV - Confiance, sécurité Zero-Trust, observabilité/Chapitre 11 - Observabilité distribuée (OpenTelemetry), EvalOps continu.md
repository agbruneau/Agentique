# Chapitre 11 — Observabilité distribuée (OpenTelemetry), EvalOps continu et fiabilité (SRE agentique)

Une architecture agentique dotée d’identités `Zero-Trust` (chapitre 10) et d’un moteur d’exécution durable (chapitre 09) reste aveugle en production si l’entreprise ne peut ni corréler ses trajectoires cognitives, ni prouver statistiquement leur qualité avant déploiement, ni couper une boucle pathologique en temps réel. Là où un service déterministe échoue par un code `HTTP 500` net, un `System of Agency` peut réussir techniquement chaque requête réseau tout en dérivant sémantiquement, en épuisant des quotas d’inférence ou en propageant une erreur en cascade sur plusieurs domaines [237] [238] [239].

Ce chapitre pose le socle d’observabilité, d’évaluation continue (`EvalOps`) et de fiabilité (`SRE`) de la Partie IV. Côté `SA`, l’enjeu est d’unifier la télémétrie `OpenTelemetry` sur `MCP`, `A2A` et l’inférence, d’automatiser des bancs de trajectoires hermétiques, de piloter des `SLI` /`SLO` comportementaux et d’armer des coupe-circuits cognitifs à repli déterministe [240] [241] [242] [243]. Côté `EA`, il s’agit de garantir l’auditabilité des délégations humaines et machines, d’interdire la fuite de données personnelles en télémétrie et de protéger les `Systems of Record` (`SoR`) [244] [245] [246] [247]. Par frontière d’étanchéité, la gouvernance économique `FinOps` relève du chapitre 12 et le déploiement `GitOps` de l’`AI Gateway` du chapitre 13.

## 11.1 Instrumentation unifiée `OpenTelemetry GenAI` : corrélation traces, identités `SPIFFE` /`OBO` et coûts

### 11.1.1 Convergence vers les conventions sémantiques `OpenTelemetry GenAI`

Les traceurs propriétaires fragmentaient jusqu’ici l’observabilité des invites, appels d’outils et graphes de décision, enfermant chaque équipe dans des formats incompatibles [248]. Le groupe de travail `OpenTelemetry GenAI SIG` maintient désormais un référentiel dédié (`open-telemetry/semantic-conventions-genai`) qui normalise de façon agnostique les spans, événements d’exception et métriques pour modèles, bases vectorielles et agents autonomes [240] [248].

La hiérarchie normative d’une exécution agentique s’articule autour de trois familles de spans [240] [249] [250] :

1. **Spans de cycle de vie et d’orchestration** (`create_agent`, `invoke_agent` client ou interne, et `plan`) : encadrent l’invocation globale, corrélée par `gen_ai.conversation.id` et qualifiée par un nom d’agent de faible cardinalité (`gen_ai.agent.name`) et sa version (`gen_ai.agent.version`), en émettant `gen_ai.invoke_agent.exception` lors d’un arrêt anormal [240]. Les attributs d’aiguillage (`gen_ai.agent.name`, `gen_ai.operation.name`) doivent être fournis dès la création du span afin de guider l’échantillonnage [240].
2. **Spans d’opérations de modèle** (`inference`, `embeddings`, `retrieval`, `fetch_response`) : tracent chaque passe cognitive, le modèle effectif (`gen_ai.response.model`), les compteurs de jetons (y compris `cache_read.input_tokens` et ventilations par modalité) ainsi que la raison d’arrêt (`gen_ai.response.finish_reasons`) [240] [250].

3. **Spans d’exécution d’outils** (`gen_ai.execute_tool`) : capturent chaque appel vers une capacité externe et l’événement `gen_ai.execute_tool.exception`, avec des raffinements spécialisés pour les agents exposés comme outils, le chargement de compétences (*Agent Skills*) et l’exécution de commandes [249].

Cette grammaire unifiée permet à tout backend conforme à `OTLP` de reconstituer l’arbre causal multi-tours sans couplage à un cadriciel ni à un fournisseur d’inférence unique [248].

### 11.1.2 Propagation du contexte sur `MCP` (`SEP-414`), `A2A` et `W3C Trace Context`

Dès qu’un agent franchit une frontière réseau vers une `MCP Gateway` (chapitre 04) ou un pair `Agent-to-Agent` (`A2A`, chapitre 05), la continuité causale repose sur la propagation distribuée. Sur transport `HTTP` classique, les en-têtes normalisés `traceparent` et `tracestate` du standard `W3C Trace Context` relient les spans inter-services [251]. En revanche, `MCP` véhicule des messages `JSON-RPC` multiplexés sur `stdio` ou `Streamable HTTP` où plusieurs requêtes et notifications circulent au sein d’un même flux persistant [252].

Les conventions `OpenTelemetry` pour `MCP` adoptent donc la proposition `SEP-414` : l’appelant injecte les clés `traceparent`, `tracestate` et `baggage` **sans préfixe DNS** directement dans le dictionnaire `params._meta` de chaque requête ou notification, et le serveur `MCP` en extrait le contexte pour l’attacher comme parent distant tout en mesurant `mcp.client.operation.duration`, `mcp.server.operation.duration` et les durées de session [252]. Côté délégation horizontale, les conventions `A2A` normalisent les spans `a2a.client` et `a2a.server` (sur `HTTP` et `gRPC`) en enregistrant le nom de méthode (`SendMessage`, `SendStreamingMessage`), le locataire (`tenant`) et l’identifiant `contextId`, tout en maintenant une séparation nette entre transport inter-agents et spans cognitifs de niveau supérieur [253].

### 11.1.3 Corrélation des identités `SPIFFE` /`OBO` et télémétrie des coûts d’exécution

Relier la consommation de jetons et la latence d’outils à une responsabilité juridique exige d’unir télémétrie et sécurité (chapitre 10). L’architecture associe l’identité cryptographique de la charge de travail — `SPIFFE ID` et `SVID` éphémères (`X.509` ou `JWT`) délivrés par l’API locale [245] — à la délégation humaine `OAuth 2.0 Token Exchange` (`RFC 8693`), où la revendication `sub` désigne le sujet mandant tandis que l’objet JSON imbriqué `act` identifie l’acteur immédiat au niveau externe et préserve les intermédiaires amont dans les niveaux internes [244].

Les conventions `OpenTelemetry GenAI` ne normalisant pas encore nativement ces champs d’identité, l’architecte définit un contrat d’extension explicite d’entreprise :

1. **Provenance** `OTLP` **par** `SPIFFE` : les collecteurs et SDK s’authentifient mutuellement (`mTLS`) par `SVID` éphémères, éliminant les clés API statiques de télémétrie et attestant la provenance de chaque span [245].
2. **Attributs d’extension sur traces** : chaque span critique (`invoke_agent`, `execute_tool`, `a2a.server`) enregistre `spiffe.workload.id`, l’acteur courant `auth.obo.actor` extrait du `act` externe et un condensat cryptographique irréversible du `sub` humain afin de préserver la traçabilité sans exposer d’identifiant nominatif [244] [245] [254].
3. **Propagation légère par** `W3C Baggage` : seuls des attributs de routage non sensibles (code de centre de coûts, classe de criticité métier) circulent via `OpenTelemetry Baggage` (y compris dans `params._meta` sous `MCP`), en proscrivant toute donnée personnelle ou charge volumineuse répliquée sur chaque saut réseau [252] [255].

Pour la mesure technique des coûts et volumes d’exécution, `OpenTelemetry` sépare strictement deux familles métriques [256] [257]. Les **compteurs monotones** (`gen_ai.client.inference.usage.input_tokens`, `output_tokens`, `cache_read.input_tokens`, `cache_write.input_tokens` et `reasoning.output_tokens`), ventilés par `gen_ai.token.modality`, alimentent le calcul des rythmes de dépense transmis au pilotage `FinOps` du chapitre 12 [256]. À l’inverse, les **histogrammes par opération** (`gen_ai.client.inference.operation.input_tokens` et `output_tokens`) suivent la distribution par appel et omettent délibérément la modalité afin que les quantiles `p95` /`p99` restent mathématiquement exacts — car sommer des percentiles par modalité fausserait l’estimation du coût unitaire réel [256]. Côté agent, `gen_ai.invoke_agent.inference_calls` comptabilise chaque invocation logique de modèle indépendamment des reprises réseau sous-jacentes, `gen_ai.invoke_agent.tool_calls` dénombre les appels d’outils par exécution et `gen_ai.invoke_agent.duration` adopte des bornes d’histogramme étendues de `0,1 s` à `86 400 s` (`24 h`) pour couvrir les boucles durables [257]. Enfin, `gen_ai.agent.name` doit demeurer de faible cardinalité (jamais un nom de classe générique tel `"StateGraph"` ni un identifiant de session) pour protéger la base `TSDB` [240] [257].

> **[Figure]**
> - Plan d'exécution
> - agentique
> - [system]
> - Pipeline Collecteur OTel
> - (Enclave)
> - [system]
> - Puits Observabilité &
> - Audit [system]
> - «container» Agent Harness [invoke_agent / chat]
> - Émet spans OTel GenAI, SVID SPIFFE & jeton OBO
> - «container» MCP Gateway [execute_tool / mcp]
> - Extrait traceparent & baggage via params._meta
> - «container» Pair A2A / Inférence
> - [a2a.client / model]
> - Propage contextId, usage.\* & TTFT/TPOT
> - «container» Collector Edge [redactionprocessor + OTTL]
> - Allowlist clés, hache sub,
> - masque PII (contenu=0)
> - «container» Collector Tail-Sampling
> - [tailsamplingprocessor]
> - Retient 100 % erreurs, route métriques usage.\*
> - «container» Backend Traces
> - [OTLP / Phoenix]
> - Traces liées trace_id,
> - act & SPIFFE ID
> - «container» TSDB Métriques SRE
> - [Prometheus]
> - Compteurs jetons & histogrammes latence
> - «container» Journal Audit WORM
> - [SIEM Immuable]
> - Chaîne OBO sub -> act
> - sans payload brut
> - tools/call + _meta traceparent
> - SendMessage /
> - inférence
> - Export OTLP (mTLS SPIFFE)
> - Spans MCP + attributs OBO
> - Spans assainis
> - sans PII
> - Traces anomalie
> - & échantillon
> - Métriques gen_ai.\*
> - faible cardinalité
> - Piste identités
> - SPIFFE / OBO

*Fig. 41. – Topologie d’instrumentation unifiée OpenTelemetry GenAI, corrélation SPIFFE/OBO et pipeline collecteur assaini*

### 11.1.4 Assainissement des charges utiles et échantillonnage tardif (*Tail Sampling*)

L’observabilité brute entre en conflit direct avec la protection des renseignements personnels. Par défaut, `OpenTelemetry GenAI` impose un mode `Opt-In` strict (`OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT`) avant de capturer instructions système, invites ou complétions (`gen_ai.input.messages`, `gen_ai.output.messages`), et prévoit même l’externalisation vers un dépôt chiffré hors bande (`OTEL_INSTRUMENTATION_GENAI_CONTENT_HOOK`, format configurable via `OTEL_INSTRUMENTATION_GENAI_UPLOAD_FORMAT`) ne laissant que des références `*_ref` sur les spans [248] [250]. En production courante, l’observabilité partagée respecte l’invariant `payload bytes = 0` posé sur la `MCP Gateway` au chapitre 04.

Comme l’illustre la figure 11.1, cet invariant est appliqué en enclave par un `OpenTelemetry Collector` combinant filtrage déterministe et sélection tardive :

- **Assainissement (**`redactionprocessor` **et** `transformprocessor`**)** : le `redactionprocessor` supprime d’abord tout attribut absent de sa liste blanche (`allowed_keys`), puis masque les motifs interdits (`blocked_values`) [246]. En parallèle, le `transformprocessor` (`OTTL`) hache les identifiants sujets et réécrit tout attribut résiduel avant exportation vers les puits partagés [254].
- **Échantillonnage tardif (**`tailsamplingprocessor`**)** : plutôt qu’un échantillonnage aveugle en tête qui perdrait les défaillances rares, le collecteur tamponne les spans jusqu’à achèvement de la trace complète pour retenir **100 %** des erreurs, dépassements de latence ou déclenchements de garde-fous, tout en sous-échantillonnant les trajectoires nominales [258]. Cette topologie exige un équilibrage de charge conscient du `trace_id` entre instances de collecteur [258].

| Signal / Attribut | Référence normative | Rôle `SA` | Exigence `EA` |
| --- | --- | --- | --- |
| `invoke_agent`, `inference`, `execute_tool` | `OTel GenAI` [240] [249] [250] | Reconstituer l’arbre causal multi-tours et les versions | Attribut `gen_ai.agent.name` à faible cardinalité [240] |
| `params._meta` (`traceparent`, `baggage`) | `W3C` & `SEP-414` (`MCP`) [252] [251] | Corréler le trafic `JSON-RPC` multiplexé | Zéro PII ou charge lourde dans `baggage` [255] |
| `a2a.client` / `a2a.server` (`contextId`) | `OTel A2A` [253] | Suivre la délégation asynchrone inter-agents | Cloisonnement locataire et séparation transport/cognition [253] |
| Compteurs `usage.*` vs histogrammes `operation.*` | `OTel Token Metrics` [256] | Calculer débits de jetons et quantiles `p95` /`p99` | Agrégats propres transmis au suivi `FinOps` (ch. 12) [256] |
| `SPIFFE SVID` + claims `sub` / `act` | `SPIFFE` & `RFC 8693` [244] [245] | Relier spans critiques aux identités machine/mandant | Piste WORM hachant `sub` ; transport `OTLP` en `mTLS` [244] [245] [254] |
| `redactionprocessor`, `OTTL`, `tailsampling` | `OTel Collector` [246] [258] [254] | Retenir 100 % des anomalies sans fuite de données | Politique `Opt-In` stricte ; `payload bytes = 0` par défaut [248] [250] |

*Tableau 11.1 — Convention de mappage* `OpenTelemetry GenAI` *: corrélation traces, identités* `SPIFFE` */*`OBO` *et assainissement.*

> **Arbitrage EA / SA** — Imposer `OpenTelemetry GenAI` (`invoke_agent`, `execute_tool`, `MCP` `SEP-414` et `A2A`) comme contrat télémétrique unique tout en maintenant la capture brute `Opt-In` désactivée par défaut en production [240] [252] [253] [250]. Le `SA` mappe les extensions d’entreprise `spiffe.workload.id`, `auth.obo.actor` (`act`) et `sub` haché par `OTTL`, sépare compteurs `usage.*` et histogrammes `operation.*`, et chaîne `redactionprocessor`, `transformprocessor` et `tailsamplingprocessor` derrière un routage par `trace_id` [256] [244] [246] [258] [254]. L’`EA` exige le `mTLS` `SPIFFE` sur le pipeline `OTLP` et proscrit toute PII dans `W3C Baggage` ou les dimensions métriques [257] [255] [245].

## 11.2 Pipeline `EvalOps` industriel : `golden datasets` de trajectoires, `mock MCP servers` et juges calibrés

### 11.2.1 Trajectoire et état final : la divergence entre `pass@k` et `pass^k`

Un agent autonome modifie un environnement au fil de plusieurs tours probabilistes, exposant les tests naïfs à deux erreurs symétriques [241]. Ne noter que le texte final masque les *défaillances silencieuses* : un agent peut annoncer une réservation confirmée sans avoir muté la base de données ou obtenir le bon résultat par un appel erroné [241] [259]. À l’inverse, figer une séquence rigide sans inspecter l’état final pénalise un modèle plus capable qui atteint légitimement l’objectif par un chemin plus court ou contourne une ambiguïté de règle [241].

Une ingénierie `EvalOps` rigoureuse sépare clairement chaque **tâche** (*task*), chaque **essai** (*trial*), la **trajectoire complète** (*transcript* incluant pensées, appels d’outils et traces) et l’**état final vérifié** (*outcome*, tel l’état exact d’une base SQL) [241] [237]. Elle distingue également l’**infrastructure d’évaluation** (*eval harness*) de l’**échafaudage applicatif** (*agent harness*) évalué conjointement avec le modèle [241]. Répéter `k` essais met alors en évidence une divergence décisive formalisée par `tau-bench` et Anthropic [241] [237] :

- **La métrique** `pass@k` mesure la probabilité d’obtenir au moins une réussite en `k` tentatives et converge vers `100 %` lorsque `k` augmente, convenant aux tâches exploratoires filtrables par tests unitaires déterministes [241].
- **La métrique** `pass^k` mesure la probabilité que **les** `k` **tentatives réussissent toutes** sans exception [237]. Avec un succès unitaire de `75 %`, `pass^3` chute déjà à `(0,75)³ ≈ 42 %` [241]. Sur `tau-bench`, même des agents avancés réussissent moins de `50 %` des tâches et tombent sous `25 %` à `pass^8` dans le commerce de détail [237].

Pour les processus autonomes exposés aux clients ou aux `SoR`, le `pass^k` devient l’indicateur contractuel de constance exigé en homologation plutôt qu’un score `pass@1` flatteur [241] [237].

### 11.2.2 `Golden datasets` de trajectoires et suites capacité / non-régression

Contrairement à une idée reçue exigeant des centaines de cas initiaux, Anthropic montre qu’un amorçage de `20` à `50` tâches simples tirées d’échecs réels suffit au démarrage pour détecter des écarts significatifs à forte taille d’effet, car attendre trop longtemps oblige ensuite à rétro-concevoir les critères de succès à partir d’un système déjà en production [241]. Ce patrimoine se structure ensuite en deux batteries complémentaires unifiées dans des plateformes telles que `Langfuse` [241] [260] :

1. **Suites de capacité** (*capability evals*) : ciblent les tâches difficiles ou capacités émergentes à taux de réussite initial bas pour guider l’amélioration itérative des invites, outils `ACI` et cascades [241].
2. **Suites de non-régression** (*regression evals*) : constituent la porte bloquante d’intégration continue (`CI`) avec un taux cible proche de `100 %` [241] [260]. Tout cas de capacité stabilisé gradue vers la suite de non-régression, elle-même alimentée en boucle fermée par la conversion des traces de production annotées ou en échec en jeux d’essais versionnés [241] [260].

Pour noter les séquences d’outils sans rigidité excessive, le critère `tool_trajectory_avg_score` de `Google ADK` définit trois régimes [259] : `EXACT` (ordre, outils et arguments strictement identiques), `IN_ORDER` (ordre relatif respecté malgré des lectures intermédiaires) et `ANY_ORDER` (présence de tous les appels attendus sans contrainte d’ordre) [259]. Des critères d’efficience purement informatifs (`tool_call_count_v1`, `inference_call_count_v1`, `token_usage_v1`, `invocation_duration_v1`) suivent les dérives d’amplification sans jamais déclencher de faux échecs fonctionnels [259].

### 11.2.3 Bancs hermétiques : `mock MCP servers`, simulation d’environnement et bacs à sable

Tester des trajectoires en `CI` contre des `SoR` réels provoque effets de bord destructeurs, coûts externes et variabilité réseau [261] [262]. L’architecture `EvalOps` isole donc les tests derrière trois mécanismes complémentaires :

1. **Vérification contractuelle par** `MCP Inspector` : la commande automatisée `npx @modelcontextprotocol/inspector --cli` interroge `tools/list`, vérifie la conformité des schémas `JSON-RPC` sur transports `stdio` ou `Streamable HTTP` et valide les réponses de serveurs simulés dès l’étape `CI` [263].
2. **Simulation d’environnement et injection de fautes** : selon le patron `Environment Simulation` de `Google ADK` (branché via `before_tool_callback` ou greffon dédié sans modifier le code de l’agent), une couche d’interception applique d’abord un **mode d’injection déterministe** (réponses figées ou codes d’erreur `HTTP 503` paramétrés par arguments et graine aléatoire) pour vérifier les chemins de repli, puis recourt à défaut à un **mode de simulation par modèle** (*mock strategy*) contraint par le schéma de l’outil et l’état de session [261].
3. **Confinement conteneurisé par essai (**`Inspect AI`**)** : lorsque l’agent manipule fichiers, terminaux ou bases locales, chaque échantillon tourne dans un bac à sable `Docker` dédié exposant une interface normalisée (`exec`, `read_file`, `write_file`) avec nettoyage automatique et plafonds de ressources afin d’empêcher toute interférence lors de campagnes parallèles [262].

> **[Figure]**
> - 1. Déclencheurs & Référentiel 2. Banc Hermétique CI/CD
> - 3. Évaluateurs Étagés
> - 4. Porte & Rétroaction
> - PR Git (Code / Prompt / MCP)
> - Golden Dataset (Trajectoires & cas prod)
> - Harnais EvalOps (Essais k : pass@k / pass^k)
> - Simulateur MCP / Env (Injection 503 & Mock)
> - Tier 1 : Code Graders (Exact / In-Order / État DB)
> - Tier 2 : Juge LLM Calibré (Swap + rubrique G-Eval)
> - Tier 3 : Calibration SME (Accord κ validé)
> - Porte CI/CD (Bloque si régression)
> - Traces Production (Échantillons échecs)
> - Déclenche suite
> - Injecte tâches
> - Mock outils
> - Transcripts &
> - états finaux
> - Cas conformes
> - au juge
> - Corrige biais &
> - criteria drift
> - Verdict T1
> - Verdict T2
> - Échecs annotés
> - Promeut cas

*Fig. 42. – Pipeline EvalOps continu : portes CI/CD, simulation hermétique et calibration des juges*

### 11.2.4 Juges `LLM` calibrés, biais métriques et *criteria drift*

Lorsque les assertions déterministes ne suffisent plus pour apprécier nuance politique ou qualité rédactionnelle — là où les métriques lexicales comme `BLEU` ou `ROUGE` corrèlent mal avec le jugement humain — l’approche *LLM-as-a-Judge* formalisée par `G-Eval` (chaîne de pensée et grille structurée, atteignant une corrélation de Spearman de `0,514` sur le résumé) et `MT-Bench` apporte le passage à l’échelle [264] [265]. Elle introduit toutefois trois vulnérabilités documentées :

- **Biais du juge probabiliste** : Zheng et al. caractérisent les biais de **position** en comparaison par paires, de **verbosité** (favorisant les réponses longues) et d’**auto-favoritisme** envers les sorties issues de la même famille de modèles [264].
- **Illusion du taux d’accord brut** : Thakur et al. montrent sur treize modèles juges qu’un accord brut élevé en pourcentage masque des écarts pouvant atteindre cinq points sur les barèmes humains ainsi qu’une tendance à l’indulgence et une sensibilité à la complexité des invites, rendant indispensable l’usage de métriques corrigées du hasard telles que le **kappa de Cohen (**`κ`**)** [266].
- **Dérive des critères (*criteria drift*)** : Shankar et al. (`EvalGen`) démontrent que les experts métier découvrent et affinent leurs exigences réelles en annotant des traces concrètes plutôt qu’en rédigeant des grilles figées *a priori* [267].

La figure 11.2 synthétise l’étagement retenu : les évaluateurs en code (Tier 1) filtrent d’abord contrats et état final à coût quasi nul ; seuls les cas conformes passent devant un juge `LLM` dé-biaisé par permutation symétrique des paires et rubriques `G-Eval` (Tier 2) ; enfin, des experts métier (Tier 3) révisent un échantillon stratifié pour corriger le *criteria drift* et vérifier un accord `κ` élevé (avec une cible d’ingénierie recommandée `κ ≥ 0,75` avant de rendre un juge bloquant en `CI/CD`) [241] [264] [267] [266] [260] [265].

| Dimension | Code déterministe (Tier 1) | Trajectoire & Mock `MCP` | Juge `LLM` calibré (Tier 2) | Revue humaine `SME` (Tier 3) |
| --- | --- | --- | --- | --- |
| Cible | Contrats `JSON`, état `DB` [241] | Outils (`EXACT` /`IN_ORDER` /`ANY_ORDER`) et fautes `503` [259] [261] | Nuance sémantique, hallucinations (`G-Eval`) [259] [265] | Vérité terrain et *criteria drift* [241] [267] |
| Fiabilité et biais | Déterministe ; rigide hors schéma [241] | Reproductible si injection amorcée [261] | Biais position, verbosité, indulgence [264] [266] | Accord inter-humains variable [267] |
| Rôle `CI/CD` | Bloquant à chaque *commit* [241] | Bloquant sur PR et contrats `MCP` [261] [263] | Bloquant après Tier 1 si validé par `κ` [266] [260] | Échantillonnage hebdomadaire et post-incident [241] [267] |
| Coût et latence | Millisecondes [241] | Faible (bac à sable isolé) [261] [262] | Modéré (permutations et rubriques) [264] [265] | Élevé (expertise rare) [241] |

*Tableau 11.2 — Matrice comparative des évaluateurs étagés et stratégies de simulation en* `EvalOps`*.*

> **Arbitrage EA / SA** — Imposer l’évaluation conjointe trajectoire + état final en banc hermétique (`mock MCP servers`, injection amorcée ou conteneurs isolés) avant toute mise en production, en interdisant les tests automatisés sur `SoR` réels [241] [261] [262]. Le `SA` exécute Tier 1 avant Tier 2, applique la permutation symétrique et calibre chaque juge par kappa de Cohen (`κ`) [241] [264] [266]. L’`EA` fixe des seuils contractuels `pass^k` sur les flux critiques et maintient une recalibration experte continue contre le *criteria drift* [237] [267].

## 11.3 `SRE` agentique : `SLI` /`SLO` comportementaux, détection de dérive sémantique et rejeu forensique

### 11.3.1 Extension des `SLI` /`SLO` aux comportements cognitifs

Un agent peut maintenir `99,9 %` de disponibilité réseau tout en rendant un service inutilisable par boucles répétitives ou appels d’outils invalides [237] [242]. Le `SRE` agentique complète donc les indicateurs d’infrastructure par des `SLI` comportementaux reliés à un **budget d’erreur** commun :

1. `SLI` **d’infrastructure et d’inférence** : latence au premier jeton (`gen_ai.server.time_to_first_token`, `TTFT`), temps par jeton de sortie (`gen_ai.server.time_per_output_token`, `TPOT`), durée globale (`gen_ai.invoke_agent.duration`) et taux d’erreurs (`error.type`) [240] [257].
2. `SLI` **comportementaux et de trajectoire** : conformité `JSON Schema` au premier essai, proportion d’exécutions sans déclenchement de garde-fou, distribution de `gen_ai.invoke_agent.tool_calls` et `inference_calls`, et score `EvalOps` en ligne sur traces échantillonnées [257] [259] [260].

Toute dégradation de validité ou d’outillage consomme ce budget d’erreur et déclenche un gel des évolutions de prompts ou de modèles (articulé avec le cycle `GitOps` du chapitre 13) [260] [242].

### 11.3.2 Alertes multi-fenêtres sur taux d’épuisement (*Multiwindow, Multi-Burn-Rate*)

Le *Google SRE Workbook* montre que la conception d’alertes arbitre quatre paramètres : **précision**, **rappel**, **temps de détection** et **temps de réinitialisation** [242]. Les seuils instantanés provoquent du bruit sur micro-rafales, tandis qu’une fenêtre longue isolée maintient l’alerte active longtemps après résolution de l’incident [242]. Les équipes `SRE` alertent donc sur la vitesse d’épuisement du budget d’erreur (*burn rate*) via deux fenêtres couplées : une fenêtre longue mesurant l’impact cumulé sur `30 jours` et une fenêtre courte au douzième (`1/12`) garantissant que le défaut est encore actif et s’éteint en quelques minutes après reprise [242].

Pour un `SLO` de `99,9 %` (`0,1 %` de budget mensuel), la configuration de référence prescrit [242] :

- **Pagination immédiate (**`Page`**)** à `14,4×` sur `1 h` / `5 min` (`2 %` du budget consommé, extinction en cinq minutes après retour à la normale) ou `6×` sur `6 h` / `30 min` (`5 %` du budget) [242].
- **Billet asynchrone (**`Ticket`**)** à `1×` sur `3 jours` / `6 h` (`10 %` du budget), idéal pour signaler une dérive sémantique progressive sans réveiller l’astreinte [242].

### 11.3.3 Détection de dérive sémantique en absence de vérité terrain

En exploitation, l’annotation humaine arrive avec retard ou reste absente sur les grands volumes [268]. Le cadre `NIST AI RMF 1.0` (`NIST AI 100-1`) — structuré autour des fonctions continues *Govern*, *Map*, *Measure* et *Manage* — impose pourtant sous *Measure* et *Manage* une surveillance continue des dérives de données, de modèles et de concepts assortie de seuils déclencheurs de recalibration, de réentraînement ou de retrait [247]. En outre, les dérives proviennent autant des entrées métier externes (évolution saisonnière ou lexicale) que des mises à jour silencieuses des fournisseurs d’inférence ou des descriptions d’outils `MCP` [268] [247]. Faute d’étiquettes immédiates, l’étude comparative d’Evidently AI formalise cinq détecteurs sur les vecteurs d’enchâssement (*embeddings*) face à une fenêtre de référence validée [268] :

1. **Distance euclidienne entre centroïdes** : écart linéaire entre vecteurs moyens de référence et courants [268].
2. **Distance cosinus entre centroïdes** : écart angulaire entre centroïdes ; comme la distance euclidienne, ces approches agrégées peuvent toutefois masquer des déformations multimodales internes lorsque la moyenne globale reste stable [268].
3. **Classifieur binaire de domaine** : discrimine référence et flux courant via l’aire sous courbe (`ROC AUC`) ; retenu par Evidently comme défaut pragmatique pour détecter les glissements textuels [268].
4. **Part de composantes dérivantes** : applique des tests univariés dimension par dimension pour quantifier la proportion de coordonnées modifiées [268].
5. **Écart maximal moyen (**`MMD`**)** : test à noyau non paramétrique comparant les distributions multivariées complètes au-delà de leurs centroïdes [268].

La corrélation de ces signaux avec `gen_ai.response.model` et `gen_ai.agent.version` permet de distinguer immédiatement un glissement de la clientèle métier d’une mise à jour silencieuse d’un modèle amont [240] [268] [250].

> **[Figure]**
> - Sources Télémétrie & État
> - Détection & Alertes SRE
> - Rejeu Forensique & Remédiation Spans & Métriques OTLP (TTFT, TPOT, tool_calls)
> - Vecteurs Embeddings (Entrées & Sorties)
> - Journal Durable /Checkpoints
> - Moteur SLI/SLO Burn Rate (14.4x / 6x -> Page 1 x -> Ticket)
> - Détecteur Dérive Sémantique (Classifieur + Cosinus + MMD)
> - Escalade Astreinte & Promotion EvalOps
> - Replayer Déterministe (Temporal History JSON)
> - Banc Fork & Sandbox (LangGraph / Inspect AI)
> - Fenêtres longues &
> - courtes (1/12)
> - Compare référence
> - vs flux courant
> - Alerte burn rate /dépassement SLO
> - Signal dérive sans vérité terrain
> - Diagnostic d'orchestration
> - Reproduit branche
> - cognitive
> - Historique immuable
> - Snapshot super-étape

*Fig. 43. – Chaîne SRE agentique : calcul multi-fenêtres burn rate, détection de dérive sémantique et rejeu forensique*

### 11.3.4 Rejeu forensique : rejeu déterministe contre bifurcation en bac à sable

Face à un incident non déterministe, relancer la requête initiale ne reproduit pas la même trajectoire [241] [269]. La figure 11.3 sépare deux mécanismes forensiques complémentaires [270] [269] :

1. **Rejeu déterministe d’orchestration (**`Temporal Replayer`**)** : extrait l’historique immuable de production (`WorkflowHistory.from_json`) et restitue au code d’orchestration les résultats enregistrés dans les `Activities` sans ré-appeler modèles ni outils [270]. Exécuté en lot avec l’option `fail_fast=false` sur les historiques d’une `TaskQueue`, il valide en intégration continue qu’une mise à jour du graphe de workflow ne provoque aucune erreur de non-déterminisme sur les cas passés [270].
2. **Bifurcation cognitive en bac à sable (**`LangGraph Time Travel`**)** : inspecte les points de reprise (`get_state_history`) pour rejouer (`replay`) ou modifier l’état (`fork`) et tester un correctif de prompt [269]. Parce que les nœuds en aval sont **ré-exécutés**, tout `fork` doit impérativement tourner en enclave `EvalOps` devant des `mock MCP servers`, jamais sur des `SoR` réels [261] [262] [269].

| Dimension `SRE` | Indicateurs et outils | Règle de déclenchement | Réponse opérationnelle |
| --- | --- | --- | --- |
| Latence et erreurs d’inférence | `TTFT`, `TPOT`, durée agent, ratio `429` /`5xx` [257] | Multi-fenêtres `14,4×` (`1 h/5 min`) et `6×` (`6 h/30 min`) [242] | Pagination `SA` et bascule `AI Gateway` [242] |
| Qualité comportementale | Validité `JSON`, `pass^1` en ligne, `tool_calls` [257] [259] | `Burn rate` `1×` (`3 j/6 h`, `10 %` budget) [260] [242] | Billet d’analyse et gel des prompts [242] |
| Dérive sémantique | Classifieur domaine, cosinus, `MMD` [268] | Seuil `AUC` ou `MMD` vs référence [268] [247] | Recalibration `EvalOps` / alerte *Manage* [267] [247] |
| Rejeu d’orchestration | `Temporal Replayer` (`WorkflowHistory`) [270] | Erreur de non-déterminisme ou bogue flux [270] | Replay exact à coût nul sans `LLM` ni `MCP` [270] |
| Bifurcation cognitive | `LangGraph` `get_state_history` + `fork` [269] | Incident de raisonnement ou ajout au dataset [260] [269] | Exécution confinée sur `mock MCP` uniquement [261] [269] |

*Tableau 11.3 — Référentiel des* `SLI` */*`SLO` *comportementaux, politiques de* `burn rate` *et rejeu forensique.*

> **Arbitrage EA / SA** — Subordonner l’exploitation des agents à des `SLO` comportementaux couplés à des alertes `burn rate` multi-fenêtres (`14,4×`, `6×`, `1×`) [257] [242]. Le `SA` corrèle la dérive sémantique (classifieur ou `MMD`) avec `gen_ai.response.model`, réserve `Temporal Replayer` au diagnostic d’orchestration et confine tout `fork` cognitif sur `mock MCP servers` [268] [270] [269] [250]. L’`EA` exige la traçabilité `MEASURE` /`MANAGE` (`NIST AI 100-1`) et la rétention d’historiques auditables [247] [270].

## 11.4 Coupe-circuits cognitifs, plafonds de profondeur et repli automatique vers flux déterministe

### 11.4.1 Pathologies d’emballement : `LLM10`, `ASI08` et `ASI10`

La résilience réseau classique ne protège pas contre un agent sain techniquement mais bloqué dans une dérive cognitive coûteuse [238] [239]. Le référentiel `OWASP` distingue trois menaces majeures : la **consommation non bornée (**`LLM10:2025`**)** générant déni de service (`DoS`) sur les GPU et *Denial of Wallet* (`DoW`) par boucles récursives ou flux de longueur non bornée [239] ; les **défaillances en cascade (**`ASI08`**)** où une hallucination ou une rupture de schéma se propage et s’amplifie entre agents sans contrôle intermédiaire [238] ; et les **agents hors mandat (**`ASI10`**)** opérant en boucle auto-entretenue [238]. Un agent ne doit donc jamais arbitrer seul la poursuite de sa boucle : les verrous appartiennent au code déterministe du harnais et des passerelles [238] [239].

### 11.4.2 Plafonds de profondeur et insuffisance des bornes génériques

Les cadriciels exposent des garde-fous mécaniques aux sémantiques distinctes [271] [272]. `OpenAI Agents SDK` compte les **tours** d’inférence (chaque invocation modèle et ses appels d’outils associés) et lève `MaxTurnsExceeded` au dépassement de `max_turns` — réglage qu’il est impératif de ne pas désactiver via `max_turns=None` en production —, complété par des déclencheurs rapides `input_guardrails` et `output_guardrails` (`TripwireTriggered`) exécutés en contrôle amont ou aval [271]. `LangGraph` borne les **super-étapes** (*super-steps*) via `recursion_limit` (`GraphRecursionError`), dont la valeur par défaut dans les versions `1.0.6` à `1.1.3` atteint `10 000` **étapes** [272]. Conserver ce réglage par défaut en production est irresponsable : il faut abaisser explicitement `recursion_limit` (en clé de configuration de haut niveau, hors sous-objet `configurable`, ou via `LANGGRAPH_DEFAULT_RECURSION_LIMIT`) par cas d’usage et exploiter `RemainingSteps` pour sortir proprement avant l’exception [272]. Toutefois, un plafond statique reste tardif face à un agent répétant en boucle le même appel erroné [271] [272].

### 11.4.3 Anatomie du coupe-circuit cognitif à états étendus

Pour interrompre précocement ces boucles, l’architecture adapte l’automate *Circuit Breaker* de Martin Fowler (`CLOSED`, `OPEN`, `HALF_OPEN`) [273] et ses extensions `Resilience4j` (`METRICS_ONLY`, `DISABLED`, `FORCED_OPEN`, fenêtres glissantes à complexité `O(1)` par *Subtract-on-Evict* sur `RingBitBuffer` et `slow-call rate`) [243] au contrôle cognitif :

1. **Empreinte répétitive d’outils** : le harnais calcule un hachage canonique `(tool_name, sorted_arguments)` à chaque tour et coupe la boucle si la même empreinte ou le même état se répète `N` fois consécutivement (par exemple `2` ou `3`) sans progression.
2. **Taux d’erreurs de schéma et de lenteur** : sur fenêtre glissante par décompte ou par temps maintenue en `O(1)` sans balayage coûteux [243], une hausse des rejets `JSON Schema`, erreurs `isError: true`, déclenchements `guardrails` ou appels lents (`slow-call rate`) bascule le circuit vers `OPEN` [243] [271].
3. **Calibration et arrêt d’urgence** : `METRICS_ONLY` observe les franchissements sans bloquer lors de la mise au point des seuils en mode ombre, tandis que `FORCED_OPEN` procure au `SOC` /`SRE` un interrupteur d’arrêt immédiat (*kill-switch*) contre un agent `ASI10` [238] [243].

Comme le montre la figure 11.4, à l’échéance du délai de refroidissement, `HALF_OPEN` n’autorise que des sondes canari bornées validées par vérificateurs Tier 1 avant de refermer le circuit [273] [243]. En exécution durable (chapitre 09), l’évaluation et l’état du circuit résident dans l’`Activity` et sont journalisés afin de préserver le rejeu `Temporal Replayer` [270].

> **[Figure]**
> - METRICS_ONLY (Calibration silencieuse)
> - CLOSED (Exécution nominale sous max_turns / recursion_limit)
> - OPEN (Coupure cognitive immédiate : repli déterministe L0 / HITL)
> - HALF_OPEN (Sondes canari bornées validées par Tier 1)
> - FORCED_OPEN (Arrêt d'urgence opérateur ou alerte ASI10)
> - Déploiement mode ombre
> - Seuils validés (promotion prod)
> - Répétition hachage >= N ou budget / dérive / erreurs >= seuil
> - Expiration délai refroidissement Échec ou lenteur
> - d'une sonde
> - Sondes saines (succès Tier 1)
> - Kill-switch manuel ou mandat violé (ASI10)
> - Escalade incident systémique (ASI08)
> - Réarmement autorisé
> - après correctif

*Fig. 44. – Automate coupe-circuit cognitif à états étendus, plafonds de profondeur et repli déterministe*

### 11.4.4 Repli automatique vers un flux déterministe (`L0`)

En état `OPEN` ou `FORCED_OPEN`, le système bascule sans appeler le modèle vers un mode dégradé prévu par la partition `80/20` (chapitre 03) et l’échelle `L0` –`L4` (chapitre 01) :

1. **Workflow déterministe** `L0` : exécution directe d’un arbre de règles (`OPA`/code) ou d’un formulaire guidé dans le `SoE` pour les processus structurés, garantissant la continuité de service sans inférence [238] [273].
2. **Réponse documentaire non générative** : restitution directe des extraits issus de la recherche lexicale/hybride en lecture seule (`readOnlyHint: true`) sans étape de synthèse générative risquée.
3. **Escalation** `Human-on-the-Loop` **(**`HOTL`**)** : suspension durable du dossier avec trace `OpenTelemetry`, identifiant d’acteur `SPIFFE` /`OBO` et motif exact de coupure pour revue humaine auditée, ou compensation de la Saga à l’expiration du `SLA` [244] [270] [238].

| Déclencheur | Détection déterministe | Action `SA` | Exigence `EA` |
| --- | --- | --- | --- |
| Boucle d’outil répétitive | Hachage `(tool_name, args)` sur fenêtre glissante | Coupure locale `OPEN` immédiate [273] | Aucun auto-arbitrage par le `LLM` [238] |
| Plafond de profondeur | `max_turns`, `recursion_limit`, `RemainingSteps` [271] [272] | Sortie ordonnée vers repli `L0` [272] | Seuil strict par cas (`10 000` proscrit) [272] |
| Erreurs schémas / lenteur | Fenêtre `Resilience4j` (`failureRate` + `slowCallRate`) [243] | `OPEN` -> flux `L0` ; sondage `HALF_OPEN` [273] [243] | Continuité métier sans inférence critique |
| Dérive `ASI08` / `ASI10` | `traceparent` + profondeur + `tripwires` [251] [238] [271] | Bascule `FORCED_OPEN` et escalade `HOTL` [238] [243] | Révocation `SVID` /`OBO` ; audit WORM [244] [245] |
| Emballement `LLM10` | Compteurs `usage.*` + `burn rate` [256] [242] [239] | Quotas par locataire et mode non génératif [239] | Liaison aux plafonds `FinOps` (ch. 12) |

*Tableau 11.4 — Matrice de décision des coupe-circuits cognitifs, plafonds et replis déterministes.*

> **Arbitrage EA / SA** — Proscrire les plafonds par défaut permissifs (`recursion_limit = 10 000`, `max_turns=None`) et toute auto-limitation confiée au `LLM` [238] [271] [272]. Le `SA` combine `max_turns`, `RemainingSteps`, hachage d’arguments et coupe-circuit à cinq états (`METRICS_ONLY`, `CLOSED`, `OPEN`, `HALF_OPEN`, `FORCED_OPEN`) routant vers un flux `L0` ou `HOTL` [273] [243] [271] [272]. L’`EA` exige des tests périodiques de ce repli sans inférence et un arrêt d’urgence `FORCED_OPEN` face aux risques `LLM10`, `ASI08` et `ASI10` [238] [239] [243].

## Synthèse et transition vers le chapitre 12

En unifiant la télémétrie `OpenTelemetry GenAI`, `MCP` (`SEP-414`) et `A2A` avec les identités `SPIFFE` /`OBO` sous assainissement strict [240] [252] [244] [246], en industrialisant `EvalOps` sur bancs hermétiques et juges calibrés au kappa de Cohen [241] [261] [266], et en couplant alertes `burn rate`, détection de dérive, rejeu forensique et coupe-circuits cognitifs à repli déterministe [242] [268] [270] [243], l’entreprise rend ses agents auditables et fiables. Les métriques d’usage (`usage.*`), attributs `Baggage` et journaux `NIST AI RMF` ainsi produits alimentent directement la conformité et le pilotage `FinOps` du chapitre 12.
