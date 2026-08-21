# Lot L-14 — L-14

| Champ | Valeur |
|---|---|
| Lot | **L-14** — phase **P2**, jalon J-3 |
| Débloque | **ch. 24, 26** |
| Date d'instruction | **21 juillet 2026** |
| Résultat | **9 affirmations** — 0 en [A], 0 écartée(s) par le vote. **3 échecs de source** consignés |
| Vote | **2 affirmation(s)** portant à elles seules une thèse de chapitre soumises au vote à trois juges, conformément au seuil déclaré (PRD §A.4). Les autres sont en **[B] par extraction citée** |
| Contrôle de bornage | **3 correction(s)** — contrôle systématique introduit en P2 sur constat de la relecture P1.4 |
| Statut | ☑ **CLOS** |

---

## A. Affirmations retenues (9)

| # | Niveau | Degré | Affirmation |
|---|---|---|---|
| `L14-A1` | **[B]** | 0 | Les conventions sémantiques GenAI d'OpenTelemetry ont quitté le dépôt principal `open-telemetry/semantic-conventions` pour le dépôt dédié `https://github.com/open-telemetry/semantic-conventions-genai`, par une rupture déclarée dans la version v1.42.0 du dépôt principal, publiée le 12 juin 2026 (published_at 2026-06-12T21:03:17Z). |
| `L14-A2` | **[B]** ⚖ | 1 | Au 21 juillet 2026, le dépôt dédié `open-telemetry/semantic-conventions-genai` ne porte aucune version publiée : l'API GitHub renvoie une liste de releases vide et une liste d'étiquettes (tags) vide, et la section « Schema URL » du fichier README.md du dépôt contient le seul mot « TODO ». Les conventions agentiques ne sont donc, à cette date, identifiables par aucun numéro de version ni aucune URL de schéma propres au dépôt dé… |
| `L14-A3` | **[B]** | 0 | L'échelle de maturité applicable aux groupes de conventions sémantiques d'OpenTelemetry compte cinq échelons — `development`, `alpha`, `beta`, `release_candidate`, `stable` — et non trois ; en l'absence de niveau déclaré, le niveau `development` est présumé. |
| `L14-A4` | **[B]** ⚖ | 0 | Les documents agentiques du dépôt dédié portent, au 21 juillet 2026, le statut de document « Development » : le fichier `docs/gen-ai/README.md` et le fichier `docs/gen-ai/gen-ai-agent-spans.md` affichent l'un et l'autre en tête la ligne « **Status**: [Development][DocumentStatus] », soit le premier échelon de l'échelle des groupes de conventions sémantiques. |
| `L14-A5` | **[B]** | 0 | Le fichier `model/gen-ai/registry.yaml` du dépôt dédié définit quatre attributs d'agent — `gen_ai.agent.id`, `gen_ai.agent.name`, `gen_ai.agent.description`, `gen_ai.agent.version` — et deux attributs de conversation — `gen_ai.conversation.id`, `gen_ai.conversation.compacted` — chacun portant la valeur `stability: development`. |
| `L14-A6` | **[B]** | 0 | Le document `docs/gen-ai/gen-ai-spans.md` du dépôt dédié définit un segment (span) d'appel d'outil dont il prescrit le nom sous la forme « execute_tool {gen_ai.tool.name} », et le registre d'attributs déclare au niveau `development` les sept attributs d'outil `gen_ai.tool.name`, `gen_ai.tool.call.id`, `gen_ai.tool.description`, `gen_ai.tool.type`, `gen_ai.tool.call.arguments`, `gen_ai.tool.call.result` et `gen_ai.tool.definiti… |
| `L14-A7` | **[B]** | 0 | L'évaluation d'un agent est couverte par un événement nommé `gen_ai.evaluation.result`, défini dans `docs/gen-ai/gen-ai-events.md`, dont les attributs `gen_ai.evaluation.name`, `gen_ai.evaluation.score.value`, `gen_ai.evaluation.score.label` et `gen_ai.evaluation.explanation` portent tous la valeur `stability: development` au registre. |
| `L14-A8` | **[B]** | 0 | La documentation de Datadog énonce sa conformité par référence à un millésime du dépôt PRINCIPAL des conventions sémantiques — « OpenTelemetry 1.37+ semantic conventions for generative AI » —, millésime publié le 25 août 2025, donc antérieur au déplacement des conventions GenAI vers le dépôt dédié (v1.42.0, 12 juin 2026) ; la même page prescrit en outre la variable d'environnement `OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_e… |
| `L14-A9` | **[B]** | 0 | Microsoft documente, pour le traçage d'agents de Microsoft Foundry, un statut scindé et daté : « Tracing is generally available for prompt and hosted agents. Workflow and external agents are in preview », la préversion étant fournie sans engagement de niveau de service et déconseillée par l'éditeur pour les charges de production. |

⚖ = soumise au vote adversarial à trois juges.

## C. Contrôle de bornage — 3 correction(s)

*Contrôle de forme, non de contenu : il ne juge pas la vérité du fait, il retire l'excès de l'énoncé.*

| # | Faute | Reformulation retenue |
|---|---|---|
| `L14-A2` | **degré injustifié** | Relevé du 21 juillet 2026 sur le dépôt `open-telemetry/semantic-conventions-genai` : l'interrogation de l'API GitHub renvoie une liste de releases vide et une liste d'étiquettes (tags) vide, et la section « Schema URL » du `README.md` du dépôt porte la seule mention « TODO ». Aucun numéro de version ni aucune URL de schéma propres au dépôt dédié n'est donc documenté à cette date — fait négatif ÉTABLI (degré 2), fondé… |
| `L14-A3` | **verbe excessif** | Selon la section de la spécification des conventions sémantiques d'OpenTelemetry qui définit la maturité des groupes (fichier et section à nommer au registre du lot), l'échelle compte cinq échelons — `development`, `alpha`, `beta`, `release_candidate`, `stable` — et le texte pose qu'en l'absence de niveau déclaré, `development` s'applique. Le relevé ne soutient pas l'existence d'une échelle à trois échelons. |
| `L14-A4` | **clause d'exclusivité** | Au 21 juillet 2026, deux documents agentiques du dépôt dédié ont été relevés — `docs/gen-ai/README.md` et `docs/gen-ai/gen-ai-agent-spans.md` — et affichent l'un et l'autre en tête la ligne « **Status**: [Development][DocumentStatus] ». Le relevé porte sur ces deux fichiers ; il ne documente pas le statut des autres documents agentiques du dépôt. |

## D. Échecs de source consignés (3)

| Ce qui n'a pas pu être ouvert | Motif |
|---|---|
| Document d'évaluation supposé du dépôt dédié | HTTP 404. Le fichier n'existe pas : la liste du répertoire docs/gen-ai, ouverte ensuite, ne comprend aucun fichier d'évaluation. L'objet a été retrouvé dans docs/gen-ai/gen-ai-events.md (événement gen_ai.evaluation.result) — l'échec a servi… |
| Outils web (WebFetch, WebSearch, Bash) indisponibles en début de lot | Indisponibilité temporaire du classificateur de sécurité de la session (« claude-sonnet-5[1m] is temporarily unavailable »), sur environ six tentatives successives. Aucune source n'a été perdue : toutes ont été rouvertes après rétablissemen… |
| Accès direct par curl à l'API GitHub | Permission refusée par la politique d'exécution de la session. Contourné sans perte : les mêmes ressources d'API ont été ouvertes par l'outil de récupération web. |

## E. Ce que le lot déclare n'avoir pas couvert

CE QUE LE LOT ÉTABLIT ET CE QU'IL NE PEUT PAS ÉTABLIR.  1. **Le triplet minimal exigé par le lot (version + date + statut) n'est pas satisfiable comme il était posé, et c'est là le résultat principal.** Le dépôt dédié n'a ni release ni étiquette et porte « TODO » à la place de son URL de schéma (L14-A2). Le lot rend donc : dépôt = `open-telemetry/semantic-conventions-genai` ; statut = `Development` (L14-A4) ; version = **inexistante à ce jour**, la seule ancre temporelle disponible étant la date de consultation (21 juillet 2026) et la date de la rupture qui a créé le dépôt (12 juin 2026, L14-A1). ⚠ Conséquence de rédaction pour le ch. 24 : la formule « conventions OTel version X du [date] » est **inécrivable**. La seule formule fidèle est du type « les conventions sémantiques GenAI d'OpenTelemetry, telles que portées par le dépôt `semantic-conventions-genai` au 21 juillet 2026, à l'état *Development* et sans version publiée ». Le PRDPlan §5.5, qui pose que « conventions OTel sans version est une affirmation vide », doit être amendé : l'affirmation reste vide, mais c'est faute de version **existante**, pas faute de recherche.  2. **Correction d'une erreur du cadrage amont, à ne pas propager.** Le CLAUDE.md du volume (l. 122) et le PRD §8.3 portent une échelle à trois échelons (« Development → Release Candidate → Stable »). L14-A3 montre qu'il y en a **cinq** pour les groupes de conventions sémantiques, et que la confusion vient probablement d'une seconde échelle, distincte, applicable aux **signaux des bibliothèques clientes**. Corriger en nommant l'échelle visée, sinon la correction reproduit la faute.  3. **Périmètre non couvert, et pourquoi.** (a) Les **métriques** GenAI (`docs/gen-ai/gen-ai-metrics.md`, `model/gen-ai/metrics.yaml`) n'ont pas été ouvertes : le ch. 26 (indicateurs AgentOps) en dépend directement et cela reste à instruire. (b) Le document **`mcp.md`** du dépôt dédié n'a pas été ouvert, alors que la revalidation du 21 juillet 2026 (§2.5 et le brouillon MCP) le désigne comme la pièce de jonction pour le §24.4 — corrélation trace ↔ chaîne de mandat, propagation `traceparent`/`tracestate`/`baggage` dans `_meta`. **C'est la lacune la plus coûteuse du lot.** (c) Neuf des onze fichiers Markdown de `docs/gen-ai` n'ont pas été ouverts un à un : aucun constat de ce lot ne vaut pour l'ensemble du répertoire. (d) Les fichiers `spans.yaml`, `events.yaml` et `metrics.yaml` du modèle n'ont pas été balayés : le relevé d'attributs (L14-A5 à A7) provient de `registry.yaml` et des documents cités, et **ne prétend pas à l'exhaustivité**.  4. **Aucune clause d'exclusivité n'est revendiquée nulle part.** Ni « les seuls attributs d'agent », ni « le premier éditeur conforme », ni « tous les documents en Development ». Chaque constat est borné au fichier ou à la ressource ouverts.  5. **Panorama des plateformes : deux occurrences, pas un état du marché.** Seuls Microsoft Foundry (L14-A9) et Datadog (L14-A8) ont été instruits sur source primaire d'éditeur. **Langfuse** a été ouvert mais n'est pas promu en affirmation, faute de place : sa documentation porte le verbatim « Langfuse aims to be compliant with the OpenTelemetry GenAI semantic conventions and support major LLM instrumentation frameworks » (https://langfuse.com/docs/opentelemetry/get-started, consulté le 21 juillet 2026) — une **formulation d'intention**, non de conformité constatée, et la page cite des attributs `gen_ai.prompt` / `gen_ai.completion` dont la correspondance avec le registre courant n'a **pas** été vérifiée. Non instruits : Arize Phoenix, LangSmith, W&B Weave, Traceloop, Grafana, Elastic, AWS. **Le relevé ne soutient donc aucun énoncé sur « l'état du marché »** : il documente trois cas. Toute métrique d'adoption reste à traiter comme auto-déclarée.  6. **Réserve de méthode sur les citations.** Les verbatim ont été obtenus par un outil de récupération qui convertit la page puis en extrait le texte ; les fichiers de spécification ont été lus en **brut** (raw.githubusercontent.com) pour limiter ce risque, mais la typographie exacte (gras, liens de référence) mériterait une seconde constatation sur pièce avant toute citation verbatim revendiquée mot pour mot dans un chapitre — au sens de CA-05 et CA-14, ce rapport est une constatation datée, pas une attestation de verbatim.  7. **Ce que le lot ne clôt pas.** Il ne clôt pas L-14 : les métriques (ch. 26) et le document MCP (§24.4) manquent. Il n'ouvre aucune entrée de socle par lui-même — la promotion en F-xx relève de la clôture du lot, après le vote adverse sur L14-A2 et L14-A4.

## F. Sources et citations

### `L14-A1` — [B]

Les conventions sémantiques GenAI d'OpenTelemetry ont quitté le dépôt principal `open-telemetry/semantic-conventions` pour le dépôt dédié `https://github.com/open-telemetry/semantic-conventions-genai`, par une rupture déclarée dans la version v1.42.0 du dépôt principal, publiée le 12 juin 2026 (published_at 2026-06-12T21:03:17Z).

**Balayage (degré 0)** — CHANGELOG.md du dépôt principal, section v1.42.0 « Breaking Changes », ouvert en brut le 21 juillet 2026 ; page opentelemetry.io/docs/specs/semconv/gen-ai/ ouverte le même jour, réduite à un avis de déplacement ; date de publication lue au champ published_at de l'API GitHub des releases (tag v1.42.0).

- **primaire** — CHANGELOG.md — open-telemetry/semantic-conventions, entrée v1.42.0 — v1.42.0, consultée le 2026-07-21 — <https://raw.githubusercontent.com/open-telemetry/semantic-conventions/main/CHANGELOG.md>
  > All `gen_ai.*` attributes, metrics, events, and spans previously defined under `model/gen-ai/`, `model/openai/`, and `model/mcp/` (and documented under `docs/gen-ai/`) are deprecated in this repository and have moved to the [OpenTelemetry GenAI semantic conventions repository](https://github.com/open-telemetry/semantic-conventions-genai).
- **primaire** — API GitHub — release v1.42.0 de open-telemetry/semantic-conventions — 2026-06-12, consultée le 2026-07-21 — <https://api.github.com/repos/open-telemetry/semantic-conventions/releases/tags/v1.42.0>
  > tag_name: v1.42.0 — published_at: 2026-06-12T21:03:17Z
- **primaire** — Semantic conventions for generative AI systems (page historique) — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://opentelemetry.io/docs/specs/semconv/gen-ai/>
  > GenAI semantic conventions have moved to the OpenTelemetry GenAI semantic conventions repository. This page has moved and is no longer maintained in this repository.

### `L14-A2` — [B]

Au 21 juillet 2026, le dépôt dédié `open-telemetry/semantic-conventions-genai` ne porte aucune version publiée : l'API GitHub renvoie une liste de releases vide et une liste d'étiquettes (tags) vide, et la section « Schema URL » du fichier README.md du dépôt contient le seul mot « TODO ». Les conventions agentiques ne sont donc, à cette date, identifiables par aucun numéro de version ni aucune URL de schéma propres au dépôt dédié.

**Balayage (degré 1)** — Deux constats bornés, tous deux sur des ressources ouvertes le 21 juillet 2026 : (1) https://api.github.com/repos/open-telemetry/semantic-conventions-genai/releases et .../tags renvoient chacune le corps `[]` — il s'agit des ressources d'énumération complète du dépôt lui-même, non d'une requête par mot-clé ; (2) le fichier README.md brut du dépôt, lu intégralement, contient la section « ## Schema URL » suivie de la seule ligne « TODO ». Chaînes cherchées dans le README : « Schema URL », « version », « stability », « release ».

- **primaire** — API GitHub — releases de open-telemetry/semantic-conventions-genai — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://api.github.com/repos/open-telemetry/semantic-conventions-genai/releases>
  > []
- **primaire** — API GitHub — tags de open-telemetry/semantic-conventions-genai — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://api.github.com/repos/open-telemetry/semantic-conventions-genai/tags>
  > []
- **primaire** — README.md — OpenTelemetry GenAI Semantic Conventions — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/README.md>
  > ## Schema URL  TODO

**Réserve** — Portée bornée à ces deux ressources et à cette date. L'absence de release GitHub n'établit pas que le projet n'ait aucun mécanisme de versionnage ailleurs (une numérotation par instantané de dépôt, par URL de schéma générée à la construction, ou par les millésimes du dépôt principal dont il dépend via Weaver reste possible et n'a pas été balayée). Ne pas en tirer « les conventions agentiques ne sont pas versionnées » au sens absolu.

### `L14-A3` — [B]

L'échelle de maturité applicable aux groupes de conventions sémantiques d'OpenTelemetry compte cinq échelons — `development`, `alpha`, `beta`, `release_candidate`, `stable` — et non trois ; en l'absence de niveau déclaré, le niveau `development` est présumé.

**Balayage (degré 0)** — Page normative « Semantic convention groups » d'opentelemetry.io ouverte le 21 juillet 2026 ; l'énumération et la règle de défaut y sont citées mot pour mot.

- **primaire** — Semantic convention groups — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://opentelemetry.io/docs/specs/semconv/general/semantic-convention-groups/>
  > Semantic Convention groups can have the following [stability levels][MaturityLevel]: `development`, `alpha`, `beta`, `release_candidate`, and `stable`. […] If stability level is not specified, it's assumed to be `development`. […] Group stability MUST NOT change from `stable` to any other level.
- **primaire** — Versioning and stability for OpenTelemetry clients — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://opentelemetry.io/docs/specs/otel/versioning-and-stability/>
  > Signals start in **Development** status as defined by OTEP 0232. While signals are in development, breaking changes and performance issues MAY occur.

**Réserve** — ⚠ Deux échelles distinctes coexistent et ne se confondent pas. Celle-ci régit les GROUPES DE CONVENTIONS SÉMANTIQUES (cinq échelons). La page « Versioning and stability for OpenTelemetry clients » régit les SIGNAUX des bibliothèques clientes et énumère, elle, Development / Stable / Deprecated / Removed, en précisant que « Development » s'appelait auparavant « Experimental ». C'est vraisemblablement la confusion de ces deux échelles qui a produit le « Development → Release Candidate → Stable » à trois échelons porté par le CLAUDE.md (l. 122) et le PRD §8.3 : cette formulation est à corriger, mais en nommant l'échelle visée, sans quoi la correction reproduira la faute.

### `L14-A4` — [B]

Les documents agentiques du dépôt dédié portent, au 21 juillet 2026, le statut de document « Development » : le fichier `docs/gen-ai/README.md` et le fichier `docs/gen-ai/gen-ai-agent-spans.md` affichent l'un et l'autre en tête la ligne « **Status**: [Development][DocumentStatus] », soit le premier échelon de l'échelle des groupes de conventions sémantiques.

**Balayage (degré 0)** — Les deux fichiers ont été ouverts en brut le 21 juillet 2026 sur la branche main du dépôt dédié ; la ligne de statut est identique dans les deux. Constat borné à ces deux fichiers, non étendu aux onze fichiers du répertoire.

- **primaire** — Semantic Conventions for Generative AI Systems — docs/gen-ai/README.md — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/README.md>
  > **Status**: [Development][DocumentStatus]
- **primaire** — Semantic Conventions for GenAI agent spans — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-agent-spans.md>
  > **Status**: [Development][DocumentStatus]

**Réserve** — Borné aux deux fichiers ouverts. Ne pas écrire « tous les documents du dépôt sont en Development » : les neuf autres fichiers Markdown du répertoire docs/gen-ai n'ont pas été ouverts un à un. Le statut « Development » d'un DOCUMENT et la valeur `stability: development` d'un ATTRIBUT sont deux marquages distincts, à ne pas fusionner.

### `L14-A5` — [B]

Le fichier `model/gen-ai/registry.yaml` du dépôt dédié définit quatre attributs d'agent — `gen_ai.agent.id`, `gen_ai.agent.name`, `gen_ai.agent.description`, `gen_ai.agent.version` — et deux attributs de conversation — `gen_ai.conversation.id`, `gen_ai.conversation.compacted` — chacun portant la valeur `stability: development`.

**Balayage (degré 0)** — Fichier registry.yaml ouvert en brut le 21 juillet 2026 ; relevé ciblé des identifiants préfixés `gen_ai.agent` et `gen_ai.conversation` avec leur champ `stability` adjacent.

- **primaire** — model/gen-ai/registry.yaml — registre d'attributs GenAI — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/model/gen-ai/registry.yaml>
  > key: gen_ai.agent.id / stability: development — key: gen_ai.agent.name / stability: development — key: gen_ai.agent.description / stability: development — key: gen_ai.agent.version / stability: development — key: gen_ai.conversation.id / stability: development — key: gen_ai.conversation.compacted / stability: development

**Réserve** — Le relevé porte sur les préfixes demandés dans ce fichier. Il n'établit pas que ce soient les seuls attributs d'agent du corpus OpenTelemetry : les attributs d'un agent peuvent aussi être portés par d'autres fichiers du dépôt (spans.yaml, metrics.yaml, events.yaml), non balayés ici. Aucune clause d'exclusivité n'est revendiquée.

### `L14-A6` — [B]

Le document `docs/gen-ai/gen-ai-spans.md` du dépôt dédié définit un segment (span) d'appel d'outil dont il prescrit le nom sous la forme « execute_tool {gen_ai.tool.name} », et le registre d'attributs déclare au niveau `development` les sept attributs d'outil `gen_ai.tool.name`, `gen_ai.tool.call.id`, `gen_ai.tool.description`, `gen_ai.tool.type`, `gen_ai.tool.call.arguments`, `gen_ai.tool.call.result` et `gen_ai.tool.definitions`.

**Balayage (degré 0)** — Section « Execute Tool Span » de gen-ai-spans.md et fichier registry.yaml ouverts le 21 juillet 2026. Dans le tableau d'attributs de ce segment, `gen_ai.operation.name` et `gen_ai.tool.name` sont marqués « Required », `error.type` (Stable) et `gen_ai.agent.name` « Conditionally Required », `gen_ai.tool.call.arguments` et `gen_ai.tool.call.result` « Opt-In ».

- **primaire** — Semantic Conventions for GenAI spans — section « Execute Tool Span » — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md>
  > **Span name** SHOULD be `execute_tool {gen_ai.tool.name}`.
- **primaire** — model/gen-ai/registry.yaml — attributs d'outil — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/model/gen-ai/registry.yaml>
  > key: gen_ai.tool.name / stability: development — key: gen_ai.tool.call.id / stability: development — key: gen_ai.tool.description / stability: development — key: gen_ai.tool.type / stability: development — key: gen_ai.tool.call.arguments / stability: development — key: gen_ai.tool.call.result / stability: development — key: gen_ai.tool.definitions / stability: development

**Réserve** — Le verbe prescriptif de la spécification est « SHOULD », non « MUST » : le nom de segment est recommandé, non imposé. Les deux attributs qui portent le contenu réel de l'appel (`call.arguments`, `call.result`) sont en « Opt-In », c'est-à-dire hors émission par défaut — point à ne pas passer sous silence dans un chapitre qui traite de journalisation probatoire.

### `L14-A7` — [B]

L'évaluation d'un agent est couverte par un événement nommé `gen_ai.evaluation.result`, défini dans `docs/gen-ai/gen-ai-events.md`, dont les attributs `gen_ai.evaluation.name`, `gen_ai.evaluation.score.value`, `gen_ai.evaluation.score.label` et `gen_ai.evaluation.explanation` portent tous la valeur `stability: development` au registre.

**Balayage (degré 0)** — Fichier gen-ai-events.md ouvert en brut le 21 juillet 2026 (statut de document « **Status**: [Development][DocumentStatus] ») ; identifiants et valeurs de stabilité relevés dans registry.yaml. À noter : l'événement porte aussi `error.type`, seul attribut de l'ensemble marqué « Stable », et `gen_ai.response.id`.

- **primaire** — Semantic Conventions for GenAI events — événement d'évaluation — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-events.md>
  > gen_ai.evaluation.result
- **primaire** — model/gen-ai/registry.yaml — attributs d'évaluation — branche main, consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/model/gen-ai/registry.yaml>
  > key: gen_ai.evaluation.name / stability: development — key: gen_ai.evaluation.score.value / stability: development — key: gen_ai.evaluation.score.label / stability: development — key: gen_ai.evaluation.explanation / stability: development

**Réserve** — L'évaluation n'a pas de fichier de documentation dédié : le répertoire docs/gen-ai, dont la liste a été ouverte le 21 juillet 2026, comprend onze fichiers Markdown (README, anthropic, aws-bedrock, azure-ai-inference, gen-ai-agent-spans, gen-ai-events, gen-ai-exceptions, gen-ai-metrics, gen-ai-spans, mcp, openai) et un sous-répertoire non-normative, sans fichier d'évaluation ; l'objet est logé dans le document des événements. Constat borné à cette liste de répertoire.

### `L14-A8` — [B]

La documentation de Datadog énonce sa conformité par référence à un millésime du dépôt PRINCIPAL des conventions sémantiques — « OpenTelemetry 1.37+ semantic conventions for generative AI » —, millésime publié le 25 août 2025, donc antérieur au déplacement des conventions GenAI vers le dépôt dédié (v1.42.0, 12 juin 2026) ; la même page prescrit en outre la variable d'environnement `OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental`, dont l'intitulé qualifie ces conventions d'expérimentales.

**Balayage (degré 0)** — Page de documentation produit de Datadog ouverte le 21 juillet 2026 ; date de v1.37.0 lue au champ published_at de l'API GitHub des releases du dépôt principal (2025-08-25T23:38:36Z).

- **primaire** — OpenTelemetry Instrumentation — Datadog Agent Observability — consultée le 21 juillet 2026, consultée le 2026-07-21 — <https://docs.datadoghq.com/llm_observability/instrumentation/otel_instrumentation/>
  > OpenTelemetry 1.37+ semantic conventions for generative AI […] OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental
- **primaire** — API GitHub — release v1.37.0 de open-telemetry/semantic-conventions — 2025-08-25, consultée le 2026-07-21 — <https://api.github.com/repos/open-telemetry/semantic-conventions/releases/tags/v1.37.0>
  > tag_name: v1.37.0 — published_at: 2025-08-25T23:38:36Z

**Réserve** — ⚠ Constat borné à Datadog : AUCUNE généralisation à l'ensemble des éditeurs n'est soutenue par ce relevé, qui n'a examiné qu'un fournisseur. L'énoncé porte sur ce que Datadog DOCUMENTE, non sur ce que son produit fait ; la conformité annoncée est auto-déclarée par l'éditeur et doit être attribuée à Datadog à chaque occurrence. Le relevé ne soutient pas — et ne réfute pas — la thèse plus large d'une discontinuité générale de numérotation entre le dépôt dédié et les implémentations d'éditeurs : il en fournit une occurrence, pas une mesure.

### `L14-A9` — [B]

Microsoft documente, pour le traçage d'agents de Microsoft Foundry, un statut scindé et daté : « Tracing is generally available for prompt and hosted agents. Workflow and external agents are in preview », la préversion étant fournie sans engagement de niveau de service et déconseillée par l'éditeur pour les charges de production.

**Balayage (degré 0)** — Page Microsoft Learn « Agent tracing in Microsoft Foundry (preview) » ouverte le 21 juillet 2026 ; métadonnées de la page : ms.date 2026-03-27, updated_at 2026-05-18. Le titre de la page porte lui-même la mention « (preview) ».

- **primaire** — Agent tracing in Microsoft Foundry (preview) — ms.date 2026-03-27 ; mise à jour 2026-05-18, consultée le 2026-07-21 — <https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept>
  > Tracing is generally available for prompt and hosted agents. Workflow and external agents are in preview. […] Items marked (preview) in this article are currently in public preview. This preview is provided without a service-level agreement, and we don't recommend it for production workloads.

**Réserve** — ⚠ Quatre choses distinctes à ne pas fusionner sur cette seule page : la DISPONIBILITÉ GÉNÉRALE vaut pour deux catégories d'agents (prompt, hosted), la PRÉVERSION pour deux autres (workflow, external) — un chapitre qui écrirait « le traçage d'agents de Foundry est GA » serait faux pour la moitié du périmètre. Statut auto-déclaré par Microsoft, à lui attribuer à chaque occurrence. Par ailleurs, cette page renvoie encore, pour les conventions sémantiques, vers opentelemetry.io/docs/specs/semconv/gen-ai/ — la page que le dépôt principal déclare déplacée et non maintenue (voir L14-A1).

