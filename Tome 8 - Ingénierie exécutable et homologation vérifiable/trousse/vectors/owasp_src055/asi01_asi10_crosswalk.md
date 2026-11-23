# OWASP Top 10 for Agentic Applications (`ASI01`–`ASI10`) — Cartographie hors ligne `SRC-055`

- **Licence amont :** `CC BY-SA 4.0` (OWASP GenAI Security Project — Agentic Security Initiative)
- **Sources ouvertes (`L+`) :** [`genai-security-project.github.io/crosswalk/agentic-ai-top10/`](https://genai-security-project.github.io/crosswalk/agentic-ai-top10/) (`SHA-256`: `e5a50552cb527f49da00bcd4ea206348db3331b41c6f4fa2dd7e7dc5904cf17d`), dépôt [`genai-security-project/crosswalk`](https://github.com/genai-security-project/crosswalk) (`b0b85c5b725be135248869e642efe5e4eca6ea17`), et `SRC-055` [`genai-security-project/GenAI-Security-Corpus`](https://github.com/genai-security-project/GenAI-Security-Corpus) (`b234defdc90833d12c6f9fedb3161600b6f77abb`, texte UTF-8 `SHA-256`: `4d9f1c9f067fc284f01e8a904b172bbaceb97dd5a259a4d73c7d80f1482c22f3`).
- **Clause `AO-01` :** Accès strictement interdit à `genai.owasp.org` (`HTTP 403`, `statut F`).

| ID | Menace (`SRC-055`) | Sévérité Web / `2026-Q3` | Score `AIVSS` | Mappages Crosswalk | Couverture `8 - Manuel/trousse/` |
|---|---|---:|---:|---:|---|
| `ASI01` | Agent Goal Hijack | Critical / Critical | 9.8 | 101 | `harness_proto/pipeline.py`, `policies_opa/camel_taint.rego`, `evalops_prr/metamorphic.py` |
| `ASI02` | Tool Misuse and Exploitation | Critical / Critical | 9.6 | 99 | `policies_opa/rule_of_two.rego`, `harness_proto/mcp_pinning.py`, `policy_saga/saga_orchestrator.py` |
| `ASI03` | Identity and Privilege Abuse | Critical / Critical | 9.3 | 109 | `authz_pqc_audit/obo_dpop.py`, `authz_pqc_audit/revocation_fsm.py`, `authz_pqc_audit/ciba_approval.py` |
| `ASI04` | Agentic Supply Chain Vulnerabilities | High / High | 8.4 | 99 | `harness_proto/mcp_pinning.py`, `harness_proto/a2a_card.py`, `execute_g0.py` |
| `ASI05` | Unexpected Code Execution (RCE) | Critical / Critical | 9.9 | 98 | `policy_saga/sandbox_manifest.py`, `policies_opa/sandbox_confinement.rego`, `harness_proto/pipeline.py` |
| `ASI06` | Memory & Context Poisoning | High / High | 8.7 | 97 | `policy_saga/taint_camel.py`, `policies_opa/camel_taint.rego`, `harness_proto/pipeline.py` |
| `ASI07` | Insecure Inter-Agent Communication | High / High | 8.2 | 97 | `harness_proto/a2a_card.py`, `harness_proto/mcp_pinning.py`, `authz_pqc_audit/pqc_http431.py` |
| `ASI08` | Cascading Failures | High / Critical | 9.1 | 97 | `policy_saga/saga_orchestrator.py`, `evalops_prr/wilson_bounds.py`, `evalops_prr/prr_validators.py` |
| `ASI09` | Human-Agent Trust Exploitation | Medium / High | 7.3 | 95 | `authz_pqc_audit/ciba_approval.py`, `harness_proto/pipeline.py`, `authz_pqc_audit/audit_scitt_focus.py` |
| `ASI10` | Rogue Agents | Critical / Critical | 9.7 | 101 | `authz_pqc_audit/revocation_fsm.py`, `evalops_prr/prr_validators.py`, `authz_pqc_audit/audit_scitt_focus.py` |

## `ASI01` — Agent Goal Hijack

- **Sévérité :** `Critical` (portail crosswalk) · `Critical` (`AIVSS 9.8`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Attackers redirect an agent's objectives or decision logic through direct or indirect prompt injection, poisoned content, malicious documents, or crafted tool outputs. The agent continues operating normally from the outside while serving the attacker's intent.
- **Contrôles `8 - Manuel/trousse/` :** 8-step schema boundary, CaMeL control/data isolation, BILINGUAL_FR_EN_INJECTION_INVARIANCE (`EXIG-MCP-19, EXIG-SEC-24, S-03, S-06`)
- **Mesures d'atténuation `SRC-055` (9):** Treat all natural-language inputs (e.g., user-provided text, uploaded documents, retrieved content) as untrusted. Route them through the same input-validation and prompt-injection safeguards defined in LLM01:2025 before they can influence goal selection, planning, or tool calls.

## `ASI02` — Tool Misuse and Exploitation

- **Sévérité :** `Critical` (portail crosswalk) · `Critical` (`AIVSS 9.6`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Agents misuse legitimate tools due to prompt manipulation, goal hijack, misalignment, or unsafe delegation — calling tools with destructive parameters, chaining tools in unexpected sequences, or operating tools far beyond their intended scope.
- **Contrôles `8 - Manuel/trousse/` :** Rule of Two default allow := false, JCS SHA-256 tool pinning, Idempotency & budget ceiling (`EXIG-SEC-06, EXIG-MCP-20, S-01, S-08`)
- **Mesures d'atténuation `SRC-055` (9):** Note: ASI02 builds on the mitigations of LLM06:2025 (Excessive Agency) by extending them to multi-step agentic workflows and tool orchestration. While LLM06 focuses on model-level autonomy, ASI02 addresses misuse of legitimate tools within agentic plans and delegation chains.

## `ASI03` — Identity and Privilege Abuse

- **Sévérité :** `Critical` (portail crosswalk) · `Critical` (`AIVSS 9.3`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Agents inherit human or system credentials — session tokens, API keys, SSH keys, delegated permissions — and attackers exploit weak privilege boundaries to use those credentials beyond their intended scope, enabling lateral movement.
- **Contrôles `8 - Manuel/trousse/` :** OBO <= 2 hops + DPoP RFC 9449 + passthrough rejection, SSF/CAEP FSM, CIBA I-JSON/JCS action_sha256 (`EXIG-MCP-11, EXIG-SEC-25, S-09, S-11`)
- **Mesures d'atténuation `SRC-055` (9):** Enforce Task-Scoped, Time-Bound Permissions: Issue short-lived, narrowly scoped tokens per task and cap rights with permission boundaries - using per-agent identities and short-lived credentials (e.g., mTLS certificates or scoped tokens) - to limit blast radius, block delegated-abuse and maintenance-window attacks, and mitigate un-scoped inheritance, orphaned privileges, and reflection-loop elevation.

## `ASI04` — Agentic Supply Chain Vulnerabilities

- **Sévérité :** `High` (portail crosswalk) · `High` (`AIVSS 8.4`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Malicious or compromised tools, MCP servers, prompt templates, model files, or agent personas introduced into the runtime supply chain alter agent behaviour or expose data — often fetched dynamically at runtime with no static review.
- **Contrôles `8 - Manuel/trousse/` :** Rug-pull SHA-256 digest suspension, AgentCard JWS+JCS & pinned jku, requirements.lock --require-hashes + SPDX (`EXIG-MCP-20, EXIG-A2A-03, G-01, S-14`)
- **Mesures d'atténuation `SRC-055` (9):** Provenance and SBOMs, AIBOMs: Sign and attest manifests, prompts, and tool definitions; require and operationalize SBOMs, AIBOMs with periodic attestations; maintain inventory of AI components; use curated registries and block untrusted sources.

## `ASI05` — Unexpected Code Execution (RCE)

- **Sévérité :** `Critical` (portail crosswalk) · `Critical` (`AIVSS 9.9`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Agents that generate or execute code — for workflow automation, scripting, data processing — become remote code execution gateways when crafted prompts or poisoned inputs cause them to run attacker-controlled logic.
- **Contrôles `8 - Manuel/trousse/` :** network:none / IMDS block / read_only_root, No eval/shell tool forwarding, Strict Draft 2020-12 typing (`EXIG-SEC-12, EXIG-SEC-13, EXIG-SEC-14, EXIG-SEC-15, S-15`)
- **Mesures d'atténuation `SRC-055` (7):** Follow the mitigations of LLM05:2025 Improper Output Handling with input validation and output encoding to sanitize agent-generated code

## `ASI06` — Memory & Context Poisoning

- **Sévérité :** `High` (portail crosswalk) · `High` (`AIVSS 8.7`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Persistent corruption of agent memory, RAG stores, embeddings, or contextual knowledge — unlike prompt injection, the effect persists across sessions, slowly shifting agent behaviour or leaking secrets over time.
- **Contrôles `8 - Manuel/trousse/` :** SessionTaintTracker propagation, Grounding verification against SoR records, Tenant/task context isolation (`S-06, R-03, EXIG-SEC-24`)
- **Mesures d'atténuation `SRC-055` (9):** Baseline data protection: Encryption in transit and at rest combined with least-privilege access

## `ASI07` — Insecure Inter-Agent Communication

- **Sévérité :** `High` (portail crosswalk) · `High` (`AIVSS 8.2`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Agent-to-agent (A2A) communication channels lacking strong authentication, encryption, or schema validation enable spoofing, replay attacks, protocol downgrade, and agent-in-the-middle attacks that misdirect entire multi-agent workflows.
- **Contrôles `8 - Manuel/trousse/` :** AgentCard JWS ES256/JCS RFC 8785, MCP HeaderMismatch (-32020) & Streamable HTTP, ML-DSA Transaction Tokens O(1) (`EXIG-A2A-03, EXIG-MCP-15, EXIG-MCP-16, R-06`)
- **Mesures d'atténuation `SRC-055` (9):** Secure agent channels: Use end-to-end encryption with per-agent credentials and mutual authentication. Enforce PKI certificate pinning, forward secrecy, and regular protocol reviews to prevent interception or spoofing.

## `ASI08` — Cascading Failures

- **Sévérité :** `High` (portail crosswalk) · `Critical` (`AIVSS 9.1`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Single-point faults — a poisoned memory entry, a bad plan, a compromised tool — propagate through multi-agent workflows and amplify into system-wide incidents. Especially critical in OT environments.
- **Contrôles `8 - Manuel/trousse/` :** Saga 10 fault scenarios + isolated CompensationChannel, Circuit-breaker & human escalation, 24 blocking PRR & 2027-B001 (`EXIG-ORC-18, EXIG-ORC-20, EXIG-ORC-28, R-01, R-14`)
- **Mesures d'atténuation `SRC-055` (10):** Zero-trust model in application design: design system with fault tolerance that assumes availability failure of LLM:2025, agentic function components and external sources.

## `ASI09` — Human-Agent Trust Exploitation

- **Sévérité :** `Medium` (portail crosswalk) · `High` (`AIVSS 7.3`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Users anthropomorphise agents — trusting their fluency, apparent expertise, and persuasive outputs — enabling hijacked agents to manipulate humans into approving malicious commands, sharing sensitive data, or performing harmful actions.
- **Contrôles `8 - Manuel/trousse/` :** Distinct approver_sub != principal_sub bound to JCS hash h, AMBIGU_ESCALADE gate, SCITT RFC 9943 + SLH-DSA audit (`EXIG-SEC-25, G-05, G-06, O-02`)
- **Mesures d'atténuation `SRC-055` (9):** Explicit confirmations: Require multi-step approval or “human in the loop” before accessing extra sensitive data or performing risky actions.

## `ASI10` — Rogue Agents

- **Sévérité :** `Critical` (portail crosswalk) · `Critical` (`AIVSS 9.7`, jeu `2026-Q3`)
- **Synthèse crosswalk :** Malicious or compromised agents that appear compliant on the surface but pursue hidden goals, hijack workflows, or systematically deviate from their intended purpose — often the end-state of a successful ASI01 or ASI06 attack.
- **Contrôles `8 - Manuel/trousse/` :** soc_killswitch_id in 2027-B001 + REVOKED terminal FSM, pass^k & Wilson 95% behavioral gates, Tamper-evident SCITT ledger (`EXIG-EVA-03, G-07, G-10, G-15, F-04, F-14`)
- **Mesures d'atténuation `SRC-055` (7):** Governance & Logging: Maintain comprehensive, immutable and signed audit logs of all agent actions, tool calls, and inter-agent communication to review for stealth infiltration or unapproved delegation.
