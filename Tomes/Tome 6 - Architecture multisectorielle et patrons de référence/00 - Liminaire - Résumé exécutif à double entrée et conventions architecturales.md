# Liminaire — Résumé exécutif à double entrée et conventions architecturales

L’insertion d’agents autonomes (`LLM`, `SLM`) entre les interfaces (`Systems of Engagement`, `SoE`) et les systèmes d’autorité (`Systems of Record`, `SoR`) rompt trente ans de déterminisme applicatif sans rendre les bases transactionnelles caduques.

Au fil des quinze chapitres, une thèse s’impose : **la fiabilité de l’entreprise agentique tient à l’ingénierie des frontières plutôt qu’à la puissance des modèles**. Maintenir environ `80 %` du contrôle, des règles impératives, des identités et des mutations en logique déterministe, tout en confinant les `20 %` cognitifs sous contrats typés, télémétrie et réversibilité, transforme l’agentique en capacité industrielle auditable.

## 0.1 Colophon d’ingénierie 100 % IA et protocole de vérifiabilité Wyvern

Cet ouvrage a été conçu, rédigé, schématisé, validé et assemblé sans rédaction humaine par la **cellule d’architecture automatisée — Pipeline Gemini / Wyvern** (`Novembre 2026`), selon une chaîne pilotée par `manifest.json`, `glossaire-registre.md` et un assemblage `Pandoc` /`Typst`.

La traçabilité des chapitres `01` à `15` (Parties I à V) repose sur quatre verrous :

1. **Cloisonnement unitaire** : périmètre borné sans redite. Les unités `01` à `15` totalisent **79 522 mots** et **225 pages** avant l’ajout du liminaire et des annexes (cible globale : **250 ± 8 pages** sur 17 unités).
2. **Base de sources fermée** : aucune citation de mémoire. Chaque chapitre s’appuie sur un registre (`sources/ch<NN>-sources.md`) réunissant spécifications ouvertes (`AAIF`, `IETF`, `CNCF`, `W3C`), référentiels (`OWASP`, `NIST`, `ISO/IEC`, `CSA`, `BSIF` /`OSFI`), textes légaux et études vérifiés en ligne, soit **394 sources primaires distinctes** consolidées à l’**Annexe C**.
3. **Ancrage atomique Wyvern** : audit phrase par phrase face aux sources (`ancrage/ch<NN>-ancrage.md`). Sur **1 002 affirmations atomiques** vérifiées, **883** (`88,1 %`) étaient supportées dès le premier jet et **119** (`11,9 %`) rectifiées ou retirées (bilan à l’**Annexe D**).
4. **Validation et inspection PDF** : contrôles `validate.ts`, compilation stricte de **59 figures** (`56` schémas `PlantUML` `.svg` via `-failfast2` et `3` arbres `Mermaid` `.png`) et **52 tableaux**, suivis d’une inspection visuelle complète.

> **Périmètre de validité** — Synthèse des standards et retours vérifiés à **novembre 2026**; aucun protocole inédit n’est formulé et les revues internes (`ÉFVP`, `AIA`, `3LoD`) demeurent requises.

## 0.2 Résumé exécutif — Direction de l’architecture d’entreprise (EA)

Selon `RAND`, plus de `80 %` des projets d’IA échouent faute de cadrage métier et d’infrastructure; seuls `21 %` des dirigeants possèdent une gouvernance mature et `40 %` des projets agentiques risquent l’abandon d’ici 2027 (chapitre 15). L’`EA` urbanise donc les `Systems of Agency` sans exposer les `SoR`.

**Urbanisation et portefeuille (Partie I).** Face aux queues de latence, erreurs sous `200 OK` et mutations irréversibles, le **chapitre 1** gradue l’autonomie (`L0` –`L4`), proscrit la validation mécanique et contient la **quadruple dette** (technique, cognitive, d’intention, couplage `CACE`) en écartant les règles métier des prompts. Le **chapitre 2** étend `TOGAF ADM` et `ArchiMate 3.2` : tout agent est un `«Cognitive Actor»` (`Application Component`, jamais `Business Actor`), relié à `«Human-on-the-Loop»` et `«Guardrail Policy»`. Il découpe le SI en **quatre plans** (Expérience, Orchestration, Interopérabilité/Contexte, Confiance/Observabilité) et arbitre **Acheter (**`SaaS`**) vs Assembler (**`MCP` **/**`A2A`**, défaut) vs Construire**. Le **chapitre 3** impose la **règle 80/20** devant l’`ARB`.

**Souveraineté, conformité et FinOps (Parties II à V).** Les chapitres **04 à 06** préviennent l’enfermement via `MCP` devant couches anti-corruption (`ERP` /mainframes), `A2A` /`AGNTCY` (`OASF`) pour l’opacité B2B, et arrimage `ODCS`, `BI`, `MDM` et `OWL 2` /`SHACL`. Les chapitres **07 à 09** justifient le multi-agents face au facteur `~15×`, imposent une orchestration macro-réglementaire inter-domaines et sécurisent les transactions par exécution durable.

Appuyé sur le `Zero-Trust` (chapitre 10) et `OpenTelemetry` /`EvalOps` (chapitre 11), le **chapitre 12** impose un **registre central** avec `Agent Owner`, paliers `R1` **–**`R4` et **Trois Lignes de Défense (**`3LoD`**)** alignées sur `OSFI E-23` (1er mai 2027). Un socle `ISO/IEC 42001:2023` **+** `NIST AI RMF / AI 600-1` satisfait **Loi 25** (`RPRP`, `ÉFVP`, `art. 12.1`), **LPRPDE** (projet `C-27` caduc le 6 janvier 2025), **Directive** `SCT` (`AIA`) et `EU AI Act` (`art. 50` août 2026, `Annexe III` décembre 2027). Côté `FinOps` (`98 %` des équipes gèrent l’IA, `43 %` peinent à prouver le `ROI`), l’`EA` pilote le **coût par résultat réussi** (`p50` /`p90` /`p99`), rapproche `OTel GenAI` et `FOCUS` (*Showback* puis *Chargeback*), suit le `TCO` à cinq postes (`PTU` + `PAYG`) et garantit la réversibilité (`Data Act`). Les chapitres **13 à 15** déploient l’`IAP`, comparent trois blueprints, cohabitent avec `BPMN` /`iPaaS`, résorbent le `RPA`, bloquent **12 anti-patrons (**`AP-01` **–**`AP-12`**)** et cadencent la maturité sur **90 / 180 / 360 jours** (`M1` –`M5`).

> **Arbitrage EA / SA** — Bloquer tout déploiement `R3` –`R4` ou fédération `A2A` avant consolidation du socle `J90–J180` : registre avec `Agent Owner`, passerelles `AI` /`MCP`, identités `NHI`, `EvalOps` bloquant et moteur durable.

## 0.3 Résumé exécutif — Architecture de solutions et ingénierie de plateforme (SA)

Le `SA` et l’ingénierie plateforme enferment chaque nœud probabiliste dans un exosquelette déterministe, observable, idempotent et remplaçable.

**Harnais et interopérabilité (Parties I et II).** Le **chapitre 3** confine l’`Agent Harness` sous `SHADI` local ou `gVisor` /`Firecracker` /`Kata` via `SandboxWarmPool` (zéro `runc` nu). La règle **80/20** oriente vers des `SLM` (`RouteLLM`, `FrugalGPT`) et scelle chaque nœud par `JSON Schema Draft 2020-12` (`CFG` /`XGrammar`, `strict: true`) et validation sémantique. La Partie II normalise trois axes :

- **Vertical (**`Agent → Outil`**, chap. 04)** : `MCP` sans état (`Streamable HTTP`, `2026-07-28`), façades `ACI` (bannissant *Swagger-to-MCP*) derrière `MCP Gateway` (`server.json`, `ttlMs`, `Code Mode`), et couches `ACL` /`CQRS` /`CDC` (`Debezium`) devant les `SoR`.
- **Horizontal (**`Agent ↔ Agent`**, chap. 05)** : délégation opaque `A2A v1.0` (`AgentCard` `JWS` /`RFC 8785`, `Tasks`, `SSE`, webhooks anti-`SSRF`) et fédération `AGNTCY` (`OASF`, `ADS` `OCI` /`Kademlia` /`Sigstore`, `SLIM` /`MLS`).
- **Mémoire (chap. 06)** : quatre mémoires séparées (procédurale sous `Git`), `Agentic RAG` hybride (`RRF` + `Cross-Encoder`), `Text-to-SQL` sémantique, `GraphRAG` et propagation `ACL` (`OpenFGA`, `PostgreSQL RLS`, mode `Silo`).

**Coordination, durable et confiance (Parties III à V).** Le **chapitre 7** privilégie l’agent unique ou les graphes dirigés (`Séquentiel`, `Routeur`, `Supervisor`, `DAG`), borne les boucles (`Handoff`, `Scatter-Gather`, `Generator-Verifier`, `Group Chat` ≤ 3 agents), transfère par `Artifact URI` et ancre l’objectif (`Goal Pinning`). Le **chapitre 8** déploie l’`Event Mesh` (`CloudEvents v1.0.2`, `AsyncAPI 3.0.0` sur `Kafka`, `Solace`, `NATS JetStream`) verrouillé par `ce_ttl`, `DLQ` et quotas `TPM`. Le **chapitre 9** confie l’état long à un moteur durable (`Temporal`, `Restate`, `Dapr Workflow`) isolant le `LLM` en `Activities` /`ctx.run()`, remplace `2PC` par `Idempotency-Key`, `Outbox` et **Sagas compensatoires**, et gère l’attente `HOTL` via `Signals` /`Awakeables` sous `SLA`.

En sécurité, le **chapitre 10** unit `OWASP ASI01–10` /`MAESTRO`, `CaMeL`, `SPIFFE` **/**`SPIRE`, `OAuth 2.0 OBO` (`RFC 8693` /`8707`, `DPoP`, `RFC 9396`, `Transaction Tokens`), `Intent Gates` (`OPA` /`Cedar`), confinement `Firecracker` /`gVisor` /`Wasmtime`, filtrage `PII` et `AISPM` /`AIDR`. Le **chapitre 11** corrèle `OTel GenAI` (`SEP-414`), verrouille les promotions par `EvalOps` (`mock MCP`, `κ`, `pass^k`) et arme des **coupe-circuits à cinq états** (`METRICS_ONLY` → `CLOSED` → `OPEN` → `HALF_OPEN` → `FORCED_OPEN`) vers `L0`. Le **chapitre 13** bâtit l’`IAP` (`Backstage`, `Kratix`, `Crossplane`), l’`AI Gateway` (`GAIE` /`LiteLLM`, `EPP` /`llm-d`, `vLLM` /`NIM`), le `GitOps` du quintette (`SLSA v1.2` /`Sigstore`) et le `Worker Versioning Pinned`; le **chapitre 14** instancie **trois blueprints** (`Temporal` + `WORM`, B2B `A2A` /`Event Mesh`, Souverain `CoCo` /`microVM`); le **chapitre 15** encadre la migration *Strangler Fig* en quatre stades.

## 0.4 Parcours de lecture par rôle et conventions graphiques (ArchiMate, C4, séquences)

La double lecture `EA` /`SA` oriente chaque profil vers les chapitres et contrôles correspondant à son mandat (**Tableau 0.1**).

| Profil | Priorité décisionnelle | Parcours recommandé | Livrables et contrôles |
| --- | --- | --- | --- |
| **EA (Architecture d’entreprise)** | Urbanisation 4 plans, portefeuille, conformité, trajectoire | 01, 02, 06 (6.3), 12, 14 (14.4), 15, Annexes A–B | Cartographie `ArchiMate`, dossier `ARB`, feuille de route 360 j |
| **SA (Solutions et intégration)** | Contrats `80/20`, `MCP` /`A2A`, exécution durable, blueprints | 01, 03, 04–09, 10, 11, 13, 14 | `Agent Harness`, passerelles, `Sagas`, `ADR`, topologies |
| **CISO et sécurité (**`NHI`**)** | `ASI01–10` /`MAESTRO`, `SPIFFE`, `OBO`, confinement, `ACL` | 03 (3.1), 04–06, 10, 14 (14.1, 14.3), Annexe B | `Intent Gates` `OPA` /`Cedar`, `SVID`, `microVM`, `AISPM` /`AIDR` |
| **Plateforme (**`IAP`**) et** `SRE` | *Golden Paths*, `AI Gateway`, `GitOps`, `OTel`, `EvalOps` | 03, 08, 09, 11, 13, 14, 15 (15.2–15.4) | `EvalOps` bloquant, `Worker Versioning`, `SLO`, coupe-circuits |
| `FinOps` **et Agent Owner** | Coût par résultat, dérive `O(T²)` /`15×`, `FOCUS`, `ROI` | 01 (1.3), 02, 03, 07 (7.1), 12, 14 (14.4), 15 | Registre `R1–R4`, `PTU` /`PAYG`, `TCO` 5 postes, *Showback* |
| **Conformité,** `RPRP`**, audit** | `OSFI E-23`, `Loi 25`, `LPRPDE` /`SCT`, `EU AI Act`, `ISO 42001` | 01 (1.3), 02 (2.2), 06, 11, 12 (12.1–12.2), 15, Annexes B–D | `ÉFVP`, fiche `AIA`, traces `OTel` /`WORM`, audit Wyvern |

*Tableau 0.1 — Parcours de lecture ciblés selon le profil décisionnel.*

Pour rester lisibles sur papier Lettre, les schémas comptent 12–16 éléments : `PlantUML` (`.puml` → `.svg`) couvre `56` des `59` figures des chapitres `01` –`15`, et `Mermaid` (`.mmd` → `.png` 300 DPI) les `3` arbres décisionnels (`02-04`, `03-03`, `05-02`). Le **Tableau 0.2** codifie ces notations et la frontière déterministe/probabiliste.

| Notation et moteur | Usage et volume (01–15) | Éléments et relations clés | Frontière déterministe vs probabiliste |
| --- | --- | --- | --- |
| `ArchiMate 3.2` (`PlantUML`, `.svg`) | Urbanisation `EA`, capacités, feuille de route (`7` fig.) | `«Cognitive Actor»`, `«Intent Contract»`, `«Guardrail Policy»`, `«Human-on-the-Loop»` | Strates `SoE` /`SoA` /`SoR` séparées; l’agent reste un composant applicatif borné |
| `C4` (`PlantUML`, `.svg`) | Architecture `SA`, 4 plans et blueprints (`21` fig.) | `System_Boundary`, `Container`, `ContainerDb`, flux `MCP` /`A2A` /`OBO` /`OTLP` | Enceintes déterministes (`Harness`, `80/20`, `MCP Gateway`, `ACL`, `OPA`, durable) isolant les `LLM` |
| **Séquences** (`PlantUML`, `.svg`) | Protocoles `MCP` /`A2A`, `OBO`, `Sagas` et rejeu (`14` fig.) | Participants, `autonumber`, `alt` /`loop`, appels (`->`) et retours `SSE` (`-->`) | Le harnais ou moteur durable garde le contrôle; l’inférence reste une invocation bornée |
| **États et UML** (`PlantUML`, `.svg`) | Automates `L0–L4`, coupe-circuits (`2` fig.) et flux (`12` fig.) | États initiaux, transitions gardées, losanges, paquets gauche-droite | Seuils, plafonds `max_turns` et replis `OPEN` /`FORCED_OPEN` (`L0`) tracés en verrous explicites |
| **Arbres** (`Mermaid`, `.png`) | Logigrammes de tri (`3` fig.) | Losanges à branches étiquetées et feuilles prescriptives | Chaque arbre écarte d’abord les flux déterministes (`L0`, API fixe) avant toute branche cognitive |

*Tableau 0.2 — Conventions graphiques et codification visuelle de la frontière déterministe / probabiliste.*
