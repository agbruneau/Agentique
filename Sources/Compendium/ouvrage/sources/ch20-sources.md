# Base documentaire fermée — Chapitre 20 — Interopérabilité des politiques hors modèle (OPA/Rego, Cedar, AuthZEN), Règle de deux et séparation contrôle/données CaMeL

**Protocole :** `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0,0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

---

### [1] SRC-087 — Open Policy Agent (OPA) v1.22.4 — Rego Policy Language Reference (policy-language.md)

- **Auteurs / Émetteur :** Open Policy Agent / CNCF Maintainers
- **Date de publication :** `2026-11-12`
- **Organisme / Revue :** GitHub open-policy-agent/opa@v1.22.4 (ba39415d)
- **Identifiant :** `OPA-v1.22.4-LANG`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-087.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-policy-agent/opa/ba39415db4b3c90cd68942a74b3cc2223ec2b23c/docs/docs/policy-language.md
- **Empreinte SHA-256 (LF) :** `4b242f9eee53ae85cdb9e073e8fd8addfe60177b0d33c7de371a0c0f2cbbb7fc` (`118657` octets, `16566` mots)
- **Synthèse factuelle vérifiée :** Référence du langage Rego d'Open Policy Agent (OPA v1.22.4, tag ba39415d) spécifiant la sémantique Datalog, l'évaluation indéfinie et l'usage impératif de default allow := false en tête de paquet.

### [2] SRC-088 — Open Policy Agent (OPA) v1.22.4 — Policy Testing & Coverage (policy-testing.md)

- **Auteurs / Émetteur :** Open Policy Agent / CNCF Maintainers
- **Date de publication :** `2026-11-12`
- **Organisme / Revue :** GitHub open-policy-agent/opa@v1.22.4 (ba39415d)
- **Identifiant :** `OPA-v1.22.4-TEST`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-088.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-policy-agent/opa/ba39415db4b3c90cd68942a74b3cc2223ec2b23c/docs/docs/policy-testing.md
- **Empreinte SHA-256 (LF) :** `4e566ce11e03cf89bba835e3ab35a54b21b980d5b1661951d8b82278c4fab291` (`18696` octets, `2247` mots)
- **Synthèse factuelle vérifiée :** Documentation Policy Testing d'OPA v1.22.4 (tag ba39415d) décrivant opa test --coverage --format=json afin de garantir une couverture à 100 % des branches d'autorisation et de déni.

### [3] SRC-007 — Defeating Prompt Injections by Design (CaMeL)

- **Auteurs / Émetteur :** Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes et al.
- **Date de publication :** `2025-06-24`
- **Organisme / Revue :** arXiv (prépublication)
- **Identifiant :** `arXiv:2503.18813v2`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-007.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2503.18813
- **Empreinte SHA-256 (LF) :** `7a9735abcbdcbea1569be50b290f7e8198648a57f378a27bdb796e0f38cb3d2b` (`361916` octets, `50342` mots)
- **Synthèse factuelle vérifiée :** Architecture CaMeL (Capability-based ML Security) isolant le flux de contrôle fiable du flux de données non fiables ; résout 77 % des tâches AgentDojo avec garantie structurelle contre 84 % sans défense.

### [4] SRC-056 — Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks

- **Auteurs / Émetteur :** James Peters-Gill, Avi Semler, Henning Bartsch, Ilia Shumailov et al.
- **Date de publication :** `2026-10-05`
- **Organisme / Revue :** arXiv
- **Identifiant :** `arXiv:2610.05640`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-056.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2610.05640
- **Empreinte SHA-256 (LF) :** `490ff7dc6d6914d59acfb56fab33ebb48ae61dd5ef1bfd181cb69d04c68ee9f5` (`97586` octets, `14394` mots)
- **Synthèse factuelle vérifiée :** Étude Peters-Gill et al. (octobre 2026, Can CaMeLs Talk?) démontrant que les garanties CaMeL mono-agent ne se composent pas en multi-agents (0,2 % ASR résiduelle contre 12,9 % sans défense), sauf propagation stricte multi-CaMeL (0,0 % ASR).

### [5] SRC-055 — OWASP Top 10 for Agentic Applications 2026 (v1.0, December 2025 — document complet CC BY-SA 4.0)

- **Auteurs / Émetteur :** OWASP GenAI Security Project
- **Date de publication :** `2025-12`
- **Organisme / Revue :** OWASP GenAI Security Project (Agentic Security Initiative — GenAI-Security-Corpus)
- **Identifiant :** `OWASP-AGENTIC-TOP10-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-055.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/genai-security-project/GenAI-Security-Corpus/main/corpus/agentic-top10/2026-final/OWASP-Top-10-for-Agentic-Applications-2026-v1.0.pdf
- **Empreinte SHA-256 (LF) :** `4d9f1c9f067fc284f01e8a904b172bbaceb97dd5a259a4d73c7d80f1482c22f3` (`100680` octets, `13820` mots)
- **Synthèse factuelle vérifiée :** Référentiel OWASP Top 10 for Agentic Applications 2026 (v1.0, CC BY-SA 4.0) recensant ASI01 à ASI10 avec mention explicite non-avis juridique (document primaire en statut L+ hors genai.owasp.org).

### [6] SRC-059 — OWASP Agentic AI Top 10 Crosswalk (GitHub Pages miroir ouvert CC BY-SA 4.0)

- **Auteurs / Émetteur :** OWASP GenAI Security Project
- **Date de publication :** `2026`
- **Organisme / Revue :** OWASP GenAI Security Project (genai-security-project.github.io)
- **Identifiant :** `OWASP-AGENTIC-CROSSWALK`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-059.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://genai-security-project.github.io/crosswalk/agentic-ai-top10/
- **Empreinte SHA-256 (LF) :** `e5a50552cb527f49da00bcd4ea206348db3331b41c6f4fa2dd7e7dc5904cf17d` (`3616` octets, `506` mots)
- **Synthèse factuelle vérifiée :** Tableau de correspondance ouvert OWASP Agentic AI Top 10 Crosswalk reliant les catégories ASI01–ASI10 aux mécanismes de défense techniques vérifiables.

### [7] SRC-002 — Design Patterns for Securing LLM Agents against Prompt Injections

- **Auteurs / Émetteur :** Luca Beurer-Kellner, Beat Buesser, Ana-Maria Creţu, Edoardo Debenedetti et al.
- **Date de publication :** `2025-06-27`
- **Organisme / Revue :** arXiv (IBM / ETH Zurich / EPFL / Google DeepMind)
- **Identifiant :** `arXiv:2506.08837v3`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-002.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2506.08837
- **Empreinte SHA-256 (LF) :** `b3e1ed3304dd7a8c4a96cc21c515d50b2b1ebf00c5764a4844179bdce76b72d1` (`80916` octets, `12285` mots)
- **Synthèse factuelle vérifiée :** Taxonomie de 6 patrons architecturaux de sécurisation contre l'injection indirecte (action-selector, plan-then-execute, map-reduce LLM, dual-LLM, code-then-execute, context-minimization) prouvant que la défense doit résider dans le graphe de contrôle hors du modèle.

---

## Exclusions en statut F (`AO-01` — hors preuve)

- `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 sur genai.owasp.org; compensé intégralement par le PDF officiel CC BY-SA 4.0 v1.0 archivé sur github.com/genai-security-project/GenAI-Security-Corpus (SRC-055, L+).
