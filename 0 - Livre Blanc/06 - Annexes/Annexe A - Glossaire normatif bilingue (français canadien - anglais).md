# Annexe A — Glossaire normatif bilingue (français canadien / anglais)

Ce glossaire consolide la terminologie des quinze chapitres selon les conventions du français canadien (`fr-CA`) et les identifiants techniques normalisés.

| Terme fr-CA | Terme anglais | Définition normative | Ch. |
| --- | --- | --- | --- |
| Acteur cognitif | `«Cognitive Actor»` | Stéréotype `ArchiMate 3.2` (`Application Component`) lié à `«Human-on-the-Loop»` et `«Guardrail Policy»`. | 02 |
| Agent-Computer Interface | *Agent-Computer Interface (ACI)* | Ergonomie d’outils `MCP` par intention, pagination et erreurs correctives contre `Swagger-to-MCP`. | 04, 15 |
| Agentic RAG fédéré | *Federated Agentic RAG* | Recherche hybride (`BM25`, vectoriel, `RRF`, `Text-to-SQL`, `GraphRAG`) sous `CRAG` et `ACL`. | 06, 14 |
| Ancrage d’objectif | *Goal Pinning* | Maintien du mandat aux extrémités du contexte, hors historique mutable, contre le *Goal Drift*. | 07 |
| Annuaire fédéré | `Agent Directory Service (ADS)` | Registre `AGNTCY` indexant des fiches `OASF` signées (`Sigstore`) sur `OCI` /`ORAS` et `Kademlia DHT`. | 05, 14 |
| Architecte d’entreprise (EA) | *Enterprise Architect (EA)* | Responsable d’urbanisation, capacités, portefeuille, conformité et `FinOps`. | 01, 02, 12 |
| Architecte de solutions (SA) | *Solution Architect (SA)* | Concepteur bout-en-bout : protocoles, état, résilience, sécurité et observabilité. | 01, 03, 14 |
| Boîte d’envoi transactionnelle | *Transactional Outbox* | Patron garantissant l’atomicité mutation en base / événement sans `2PC`. | 09 |
| Carte d’agent signée | `Agent Card (JWS)` | Descripteur JSON canonisé (`RFC 8785`) et signé (`JWS`) sous `.well-known/agent-card.json`. | 05, 13, 14 |
| Cascade d’inférence | *Inference Cascade* | Routage gradué vers `SLM` ou modèles prédictifs avant escalade vers un `frontier LLM`. | 03, 12 |
| Chemin pavé | *Golden Path* | Gabarit exécutable (`IAP`, `Backstage`, `Kratix`, `Crossplane`) pré-câblant identité, `OTel` et garde-fous. | 13, 15 |
| Contrat de données | `Data Contract (ODCS)` | Spécification `ODCS v3` gouvernant schéma, qualité, fraîcheur (`SLA`) et confidentialité. | 06 |
| Couche anti-corruption | *Anti-Corruption Layer (ACL)* | Façade sémantique (`CQRS` /`CDC`) isolant les `SoR` patrimoniaux des rafales et schémas hérités. | 04, 14, 15 |
| Coupe-circuit cognitif | *Cognitive Circuit Breaker* | Automate (`max_turns`, hachage, cinq états) repliant un agent déviant vers `L0` ou `HOTL`. | 09, 11, 15 |
| Délégation au nom de | `On-Behalf-Of (OBO)` | Échange `OAuth 2.0 (RFC 8693)` à *downscoping* propageant `(sub, act[])`. | 10, 14 |
| Dette cognitive / d’intention | *Cognitive & Intent Debt* | Cascades de rustines (`CACE`) et perte de traçabilité en prompts. | 01 |
| Économie unitaire | `FinOps` (*Cost per Outcome*) | Coût (`p50` /`p90` /`p99`) par résultat réussi, pertes incluses, rapproché `OTel` /`FOCUS`. | 12 |
| Entreprise agentique | *Agentic Enterprise* | Organisation intégrant des agents gouvernés aux systèmes et aux humains. | 01, 02, 15 |
| Étalement agentique | *Agent Sprawl* | Prolifération d’agents fantômes sans `Agent Owner`, hors registre et sur-privilégiés (`AP-02`). | 12, 15 |
| Évaluation continue | `EvalOps` | Pipeline automatisé sur *golden datasets*, *mock MCP servers* et juges calibrés (`pass^k`, `κ`). | 11, 13, 15 |
| Exécution durable | `Durable Execution` | Moteur (`Temporal`, `Restate`, `Dapr`) assurant `checkpointing` et `replay` déterministe sur panne. | 09, 13, 14 |
| GitOps cognitif | *Cognitive GitOps* | Co-versionnement Git, CI et signature (`SLSA`, `Sigstore`) du quintette comportemental. | 13 |
| Idempotence à trois états | `Idempotency-Key` | Contrôle d’empreinte et d’état empêchant toute double mutation `SoR` sur réessai. | 04, 09 |
| Identité non humaine | `Non-Human Identity (NHI)` | Identité machine attestée (`SPIFFE` /`SPIRE`, `SVID`, `WIMSE`), sans secret statique. | 10, 13, 14 |
| Maillage événementiel | `Event Mesh` | Bus asynchrone (`Kafka`, `Solace`, `NATS`) routant `CloudEvents` sous `AsyncAPI 3.0` et `ce_ttl`. | 08, 14 |
| Mémoire distribuée (`CoALA`) | *Distributed Agent Memory* | Stratification travail, épisodique, sémantique et procédurale distincte du journal durable. | 06 |
| Noyau d’exécution | `Agent Harness` | Boucle déterministe encadrant modèles, outils, compaction et garde-fous. | 03, 07 |
| Passage par référence | *Claim-Check / Artifact URI* | Pointeur (`Artifact URI`, `TTL`, `ACL`) évitant la copie de charges en contexte. | 07, 14 |
| Passerelle d’inférence | `AI Gateway` | Accès unifié (`GAIE`, `LiteLLM`) vers nuages et enclaves (`vLLM` /`NIM`), quotas `TPM`. | 13, 14 |
| Passerelle d’outils | `MCP Gateway` | Médiateur `MCP` (`Streamable HTTP`) assurant découverte, cache `ttlMs` et audit. | 04, 14 |
| Plateforme interne | `Internal Agentic Platform (IAP)` | Socle produit interne (`TVP`) offrant *Golden Paths*, passerelles, télémétrie et `GitOps`. | 02, 13, 14 |
| Porte d’intention | `Intent Gate` | Contrôle déterministe *Policy-as-Code* (`OPA` /`Rego`, `Cedar`) vérifiant mandat et seuils. | 10, 14, 15 |
| Propriétaire d’agent | `Agent Owner` | Responsable nominatif du mandat, palier `R1` –`R4`, budget et retrait. | 12, 15 |
| Protocole inter-agents | `Agent-to-Agent (A2A)` | Délégation asynchrone `Tasks` (`SSE`, `Artifacts`) entre pairs opaques et `SLIM` /`MLS`. | 05, 14 |
| Règle hybride 80/20 | *80/20 Hybrid Rule* | Partition ~80 % code déterministe et ~20 % nœuds cognitifs typés. | 03, 07, 15 |
| Saga compensatoire | *Compensating Saga* | Séquence classant étapes (compensable, pivot, réessayable) pour cohérence métier. | 09, 14 |
| Strangler Fig agentique | *Agentic Strangler Fig* | Migration en quatre stades (ombre, recommandation, action bornée, autonomie) devant `BPM` /`RPA`. | 15 |
| Systèmes du SI | `SoR` / `SoE` / `SoA` | Stratification entre autorité (`Record`), interface (`Engagement`) et planification (`Agency`). | 01, 02 |
| Télémétrie GenAI | `OpenTelemetry GenAI` | Spans corrélés d’agent, `MCP` (`SEP-414`), `A2A`, `SPIFFE` /`OBO` et coûts (`OTTL`). | 11, 12 |

*Tableau A.1 — Glossaire normatif bilingue de référence couvrant les chapitres 01 à 15.*
