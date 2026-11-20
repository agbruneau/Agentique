# Annexe B — Gabarit d’Architecture Decision Record (ADR) et liste de contrôle EA/SA (40 critères)

Cette annexe réunit deux instruments d’homologation pour le comité d’architecture (`ARB`) : un gabarit d’`ADR` agentique et une grille bloquante de quarante critères.

## B.1 Gabarit d’Architecture Decision Record (ADR) agentique

Toute création ou évolution majeure d’un agent soumet ce dossier reliant l’imputabilité métier (`EA`) aux garanties techniques (`SA`).

| Rubrique ADR | Contenu normatif attendu en comité ARB |
| --- | --- |
| **1. Identification** | `ADR-YYYY-NNN`, titre, statut (*Proposé / Homologué / Déprécié*), `Agent Owner`, centre de coûts, palier `R1` –`R4`, autonomie `L0` –`L4`. |
| **2. Capacité métier** | Chaîne de valeur `BIZBOK` /`TOGAF`, rejet d’un flux `L0` seul, stéréotypes `ArchiMate 3.2` (`«Cognitive Actor»`, `«Intent Contract»`). |
| **3. Portefeuille** | Choix *Acheter / Assembler / Construire*, coexistence `BPMN` /`iPaaS` /`RPA` et stade *Strangler Fig* (`1` à `4`). |
| **4. Partition 80/20** | Part déterministe/cognitive, patron retenu (agent unique, graphe ou hybride `Event Mesh`) et schémas `JSON`. |
| **5. Protocoles et données** | Serveurs `MCP` (`ACI`), pairs `A2A` /`OASF`, `Data Contracts` (`ODCS`), `ACL` /`CQRS`, mémoire `CoALA` et isolation. |
| **6. Durabilité** | Moteur (`Temporal`, `Restate`, `Dapr`), classification `Saga`, `Idempotency-Key`, portes `HOTL` sous `SLA` et repli `L0`. |
| **7. Sécurité et lois** | Menaces `ASI01` –`ASI10`, `SPIFFE` /`NHI`, `OAuth OBO`, `OPA` /`Cedar`, confinement et `Loi 25` /`EU AI Act` /`ISO 42001`. |
| **8. EvalOps et FinOps** | Traces `OTel GenAI`, seuils `pass^k`, coupe-circuits, coût par résultat (`p50` /`p90` /`p99`), `AI Gateway` et réversibilité. |
| **9. Révision** | Risques résiduels acceptés, date de revue `3LoD`, conditions de révocation et plan de retrait. |

*Tableau B.1 — Gabarit d’Architecture Decision Record (*`ADR`*) agentique pour comité d’architecture.*

## B.2 Liste de contrôle d’homologation EA / SA (40 critères)

Les quarante critères `C01` à `C40` répartis en cinq domaines forment la grille bloquante d’accès à l’action bornée et à l’autonomie sous contrat.

| Code | Domaine | Critère vérifiable et preuve exigée en comité ARB | Ch. |
| --- | --- | --- | --- |
| `C01` | EA | Arrimage `BIZBOK` /`TOGAF` et tri `L0` –`L4` écartant les flux déterministes. | 01, 02 |
| `C02` | EA | Vue `ArchiMate 3.2` typant l’agent en `«Cognitive Actor»` lié à `«Human-on-the-Loop»` et `«Guardrail Policy»`. | 02 |
| `C03` | EA | Répartition entre quatre plans découplés sans contournement des Plans 3 et 4. | 02, 14 |
| `C04` | EA | Arbitrage *Acheter / Assembler / Construire* justifié avec clauses de réversibilité. | 02, 12 |
| `C05` | EA | Inscription au registre (`Agent Registry`) avec `Agent Owner` nominatif et palier `R1` –`R4`. | 12, 15 |
| `C06` | EA | Séparation `3LoD` / `OSFI E-23` avec revue indépendante (`2LoD`) exigée dès `R3`. | 12 |
| `C07` | EA | Coexistence `BPMN` / `iPaaS`, gel/sortie `RPA` et rejet des anti-patrons `AP-01` –`AP-03`. | 15 |
| `C08` | EA | Trajectoire *Strangler Fig* en quatre stades avec *baseline* chiffrée et accord `Agent Owner`. | 15 |
| `C09` | SA / Protocoles | Partition `80/20` vérifiée : règles impératives et écritures `SoR` hors prompt. | 01, 03 |
| `C10` | SA / Protocoles | Contrats `JSON Schema` (`additionalProperties: false`, `strict: true`) et validation sémantique. | 03 |
| `C11` | SA / Protocoles | Outils `MCP` (`Streamable HTTP`) orientés `ACI` via `MCP Gateway` (zéro `Swagger-to-MCP`). | 04, 15 |
| `C12` | SA / Protocoles | Encapsulation `SoR` par couche `ACL` et projections `CQRS` /`CDC` en lecture. | 04, 14 |
| `C13` | SA / Protocoles | Opacité `A2A v1.0` (`AgentCard` `JWS` /`RFC 8785`, `Tasks` asynchrones, `CancelTask`). | 05, 14 |
| `C14` | SA / Protocoles | Taxonomie `OASF` (`AGNTCY`) et `SLIM` /`MLS` pour fédération B2B sans exposition entrante. | 05, 14 |
| `C15` | SA / Protocoles | Mémoires `CoALA` sous compaction et `Agentic RAG` arrimé à `ODCS` et BI/`MDM`. | 06 |
| `C16` | SA / Protocoles | Propagation `ACL` à la requête (`OpenFGA` /`RLS`), isolation `Silo` et défense `ASI06`. | 06, 14, 15 |
| `C17` | Orchestration | Justification du multi-agents face à l’agent unique (`Skills` /`ReWOO`, `45 %`, `~15×`). | 07 |
| `C18` | Orchestration | Bornage des topologies (`max_iterations`, stagnation, quorum, *Group Chat* ≤ 3). | 07 |
| `C19` | Orchestration | Passage par référence (`Claim-Check` / `Artifact URI`, `TTL` /`ACL`) et `Goal Pinning`. | 07, 14 |
| `C20` | Orchestration | Enveloppes `CloudEvents v1.0.2` et `AsyncAPI 3.0.0` (`ce_correlationid`, `ce_ttl`, ségrégation). | 08 |
| `C21` | Orchestration | Patron hybride inter-domaines, `Retry` /`DLQ` non bloquants et *backpressure* `TPM`. | 08, 14 |
| `C22` | Orchestration | Moteur durable (`Temporal`, `Restate`, `Dapr`) pour boucles longues, `SoR` ou `HOTL`. | 09, 14, 15 |
| `C23` | Orchestration | Idempotence trois états (`Idempotency-Key`), `Transactional Outbox` et Sagas autour du pivot. | 09 |
| `C24` | Orchestration | Suspensions `HOTL` sous `SLA` (`Signals` /`Awakeables`) exposant le différentiel `SoR`. | 01, 09 |
| `C25` | Zero-Trust / OTel | Analyse `OWASP ASI01` –`ASI10` et séparation contrôle/données (`CaMeL`), zéro sécurité en prompt. | 10, 15 |
| `C26` | Zero-Trust / OTel | Identités `NHI` éphémères (`SPIFFE` /`SPIRE` `SVID`, `WIMSE`) par rôle, zéro secret statique. | 10, 13, 14 |
| `C27` | Zero-Trust / OTel | Délégation `OAuth 2.0 OBO` (`RFC 8693`), `RFC 8707`, `DPoP` (`RFC 9449`) et `Txn-Tokens`. | 10, 14 |
| `C28` | Zero-Trust / OTel | `Intent Gates` déterministes (`OPA` /`Cedar`) et mandats fins `RFC 9396` (`RAR`). | 10, 14 |
| `C29` | Zero-Trust / OTel | Confinement (`Firecracker`, `gVisor`, `Wasmtime`, `SHADI`; zéro `runc`), `PII` et `AISPM` /`AIDR`. | 03, 10, 14 |
| `C30` | Zero-Trust / OTel | Traces `OpenTelemetry GenAI` (`SEP-414`, `A2A`) corrélant `SPIFFE` et `OBO` sous `OTTL`. | 11 |
| `C31` | Zero-Trust / OTel | Pipeline `EvalOps` bloquant en CI sur *mock MCP servers* (`pass^k`, juges `κ`). | 11, 13, 15 |
| `C32` | Zero-Trust / OTel | `SLI` /`SLO` comportementaux sous alertes *burn rate* (`14,4×`, `6×`, `1×`) et repli `L0` testé. | 11, 15 |
| `C33` | Plateforme / FinOps | Provisionnement via *Golden Paths* (`Backstage`, `Kratix`, `Crossplane`) hors logique métier. | 13 |
| `C34` | Plateforme / FinOps | Routage unique par `AI Gateway` (`GAIE` /`LiteLLM`) gérant quotas `TPM` et `vLLM` /`NIM`. | 13, 14 |
| `C35` | Plateforme / FinOps | `GitOps` cognitif co-versionnant code, prompts, `OASF` /`MCP`, `OPA` et `EvalOps` (`SLSA`). | 13 |
| `C36` | Plateforme / FinOps | Livraison progressive (`Shadow`, `Canary`) et épinglage durable (`Worker Versioning`). | 13, 14 |
| `C37` | Plateforme / FinOps | Socle `ISO/IEC 42001` et `NIST AI RMF` prouvant `Loi 25` (`ÉFVP`), `LPRPDE` et `EU AI Act`. | 12 |
| `C38` | Plateforme / FinOps | Archivage immuable (`WORM` / *Object Lock*) des décisions, `(sub, act[])` et `HITL`. | 12, 14 |
| `C39` | Plateforme / FinOps | Coût unitaire `FinOps` par résultat réussi (`p50` /`p90` /`p99`), cache `KV` /`SLM` et `FOCUS`. | 03, 12 |
| `C40` | Plateforme / FinOps | `Showback` avant `Chargeback`, `TCO` /`ROI` ajusté du risque et tests de portabilité. | 12, 15 |

*Tableau B.2 — Liste de contrôle d’homologation EA / SA en quarante critères (*`C01` *à* `C40`*) pour comité d’architecture.*
