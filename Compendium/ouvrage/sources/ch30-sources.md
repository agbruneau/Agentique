# Base documentaire fermée — Chapitre 30 — Usine logicielle GitOps et anti-patrons agentiques

**Protocole :** `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0,0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

---

### [1] SRC-055 — OWASP Top 10 for Agentic Applications 2026 (v1.0, December 2025 — document complet CC BY-SA 4.0)

- **Auteurs / Émetteur :** OWASP GenAI Security Project
- **Date de publication :** `2025-12`
- **Organisme / Revue :** OWASP GenAI Security Project (Agentic Security Initiative — GenAI-Security-Corpus)
- **Identifiant :** `OWASP-AGENTIC-TOP10-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-055.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/genai-security-project/GenAI-Security-Corpus/main/corpus/agentic-top10/2026-final/OWASP-Top-10-for-Agentic-Applications-2026-v1.0.pdf
- **Empreinte SHA-256 (LF) :** `4d9f1c9f067fc284f01e8a904b172bbaceb97dd5a259a4d73c7d80f1482c22f3` (`100680` octets, `13820` mots)
- **Synthèse factuelle vérifiée :** Référentiel OWASP Top 10 for Agentic Applications 2026 (v1.0, CC BY-SA 4.0) recensant ASI01 à ASI10 avec mention explicite non-avis juridique (document primaire en statut L+ hors genai.owasp.org).

### [2] SRC-086 — A2A Technology Compatibility Kit (a2a-tck) v1.0.0.alpha3 — AgentCard Requirements (tck/requirements/agent_card.py)

- **Auteurs / Émetteur :** A2A Project TCK Maintainers
- **Date de publication :** `2026-10-20`
- **Organisme / Revue :** GitHub a2aproject/a2a-tck@1.0.0.alpha3 (5daf0144)
- **Identifiant :** `A2A-TCK-1.0.0.alpha3`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-086.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/a2aproject/a2a-tck/5daf0144b4a4adbdefb62180739b13c5bd7d8196/tck/requirements/agent_card.py
- **Empreinte SHA-256 (LF) :** `4889ec96433ae5f2a09c0332d9e1ff96bf3533bcd6ff41fc35a5106ffd59e44d` (`8648` octets, `672` mots)
- **Synthèse factuelle vérifiée :** Suite de conformité a2a-tck au tag 1.0.0.alpha3 (commit 5daf0144) : les exigences CARD-SIGN-001 à CARD-SIGN-004 y sont marquées NOT_AUTOMATABLE et le répertoire conformance-vectors/a2a-jcs-v01 y est absent.

### [3] SRC-087 — Open Policy Agent (OPA) v1.22.4 — Rego Policy Language Reference (policy-language.md)

- **Auteurs / Émetteur :** Open Policy Agent / CNCF Maintainers
- **Date de publication :** `2026-11-12`
- **Organisme / Revue :** GitHub open-policy-agent/opa@v1.22.4 (ba39415d)
- **Identifiant :** `OPA-v1.22.4-LANG`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-087.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-policy-agent/opa/ba39415db4b3c90cd68942a74b3cc2223ec2b23c/docs/docs/policy-language.md
- **Empreinte SHA-256 (LF) :** `4b242f9eee53ae85cdb9e073e8fd8addfe60177b0d33c7de371a0c0f2cbbb7fc` (`118657` octets, `16566` mots)
- **Synthèse factuelle vérifiée :** Référence du langage Rego d'Open Policy Agent (OPA v1.22.4, tag ba39415d) spécifiant la sémantique Datalog, l'évaluation indéfinie et l'usage impératif de default allow := false en tête de paquet.

### [4] SRC-088 — Open Policy Agent (OPA) v1.22.4 — Policy Testing & Coverage (policy-testing.md)

- **Auteurs / Émetteur :** Open Policy Agent / CNCF Maintainers
- **Date de publication :** `2026-11-12`
- **Organisme / Revue :** GitHub open-policy-agent/opa@v1.22.4 (ba39415d)
- **Identifiant :** `OPA-v1.22.4-TEST`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-088.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-policy-agent/opa/ba39415db4b3c90cd68942a74b3cc2223ec2b23c/docs/docs/policy-testing.md
- **Empreinte SHA-256 (LF) :** `4e566ce11e03cf89bba835e3ab35a54b21b980d5b1661951d8b82278c4fab291` (`18696` octets, `2247` mots)
- **Synthèse factuelle vérifiée :** Documentation Policy Testing d'OPA v1.22.4 (tag ba39415d) décrivant opa test --coverage --format=json afin de garantir une couverture à 100 % des branches d'autorisation et de déni.

### [5] SRC-021 — JSON Schema: A Media Type for Describing JSON Documents (Draft 2020-12 Core, draft-bhutton-json-schema-01)

- **Auteurs / Émetteur :** Austin Wright, Henry Andrews, Ben Hutton, Greg Dennis
- **Date de publication :** `2022-06-16`
- **Organisme / Revue :** JSON Schema / IETF Internet-Draft 2020-12
- **Identifiant :** `JSON Schema Draft 2020-12 Core`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-021.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://json-schema.org/draft/2020-12/json-schema-core
- **Empreinte SHA-256 (LF) :** `ece40a12059837b62bc4867673924eafd5845d73223d3f04ff3b99254b6c9875` (`135644` octets, `19552` mots)
- **Synthèse factuelle vérifiée :** Spécification JSON Schema Draft 2020-12 Core (draft-bhutton-json-schema-01) encadrant la validation structurelle stricte (additionalProperties: false, required, types explicites) des contrats MCP et schémas de la trousse.

### [6] SRC-057 — Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem

- **Auteurs / Émetteur :** Obada Kraishan
- **Date de publication :** `2026-09-15`
- **Organisme / Revue :** arXiv
- **Identifiant :** `arXiv:2609.14119`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-057.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2609.14119
- **Empreinte SHA-256 (LF) :** `cae21acac54fea61a6270540a888a090731fac9d0de3ae0f121f3d51d59ed7e9` (`49308` octets, `7412` mots)
- **Synthèse factuelle vérifiée :** Recensement empirique d'Obada Kraishan (septembre 2026) sur 21 643 serveurs MCP et 72 606 versions : parmi 8 900 serveurs multi-versions, 51,09 % changent entre versions, 40,58 % présentent une dérive sémantique silencieuse et 4,16 % redirigent vers un autre hôte (OR = 2,96).

### [7] SRC-011 — Agentic AI orchestration: TMT Predictions 2026

- **Auteurs / Émetteur :** Deloitte Insights
- **Date de publication :** `2025-11-18`
- **Organisme / Revue :** Deloitte Center for Technology, Media & Telecommunications
- **Identifiant :** `DELOITTE-TMT-2026-AGENTS`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-011.txt`, score AACODS `9.5/12`)
- **URL d'origine :** https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/ai-agent-orchestration.html
- **Empreinte SHA-256 (LF) :** `e7d41d25e64a998140f9d6510c553c62821273c598d9de5f92be40839362271b` (`39392` octets, `5425` mots)
- **Synthèse factuelle vérifiée :** Rapport TMT Predictions 2026 documentant la hausse de l'adoption de l'orchestration agentique et citant l'estimation Gartner selon laquelle plus de 40 % des projets agentiques risquent l'abandon d'ici fin 2027 faute de ROI et de gouvernance (communiqué primaire Gartner consigné en statut F).

---

## Exclusions en statut F (`AO-01` — hors preuve)

- `https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 sur gartner.com; documenté secondairement dans Deloitte TMT 2026 (SRC-011, L+) avec mention explicite du statut F du communiqué primaire.
- `https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai` — `NETWORK_ERROR:TimeoutError` (`included_in_evidence: false`). Expiration réseau / blocage Akamai sur mckinsey.com.
- `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 sur genai.owasp.org; compensé intégralement par le PDF officiel CC BY-SA 4.0 v1.0 archivé sur github.com/genai-security-project/GenAI-Security-Corpus (SRC-055, L+).
