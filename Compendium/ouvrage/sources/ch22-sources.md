# Base documentaire fermée — Chapitre 22 — Observabilité OpenTelemetry GenAI, double couloir PII et scellage probatoire JCS/SCITT + SLH-DSA

**Protocole :** `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0,0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

---

### [1] SRC-037 — OpenTelemetry Semantic Conventions for Generative AI Agent & Execute Tool Spans (gen_ai.operation.name)

- **Auteurs / Émetteur :** OpenTelemetry GenAI SIG
- **Date de publication :** `2026-11-05`
- **Organisme / Revue :** CNCF / OpenTelemetry Semantic Conventions (GenAI SIG — agent-spans, execute-tool & registry.yaml)
- **Identifiant :** `OTEL-GENAI-AGENT-TOOL-SPANS`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-037.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-agent-spans.md
- **Empreinte SHA-256 (LF) :** `1b2526202e8aef9b15819b89cd1c34eefd8d10be3dac7b05f714597c34d5549c` (`125111` octets, `13159` mots)
- **Synthèse factuelle vérifiée :** Conventions sémantiques OpenTelemetry GenAI Agent & Framework Spans (gen-ai-agent-spans.md, statut Development) décrivant les spans create_agent, invoke_agent et execute_tool.

### [2] SRC-089 — OpenTelemetry Semantic Conventions v1.41.0 — GenAI Attribute Registry (gen-ai.md)

- **Auteurs / Émetteur :** OpenTelemetry Semantic Conventions Maintainers
- **Date de publication :** `2026-04-28`
- **Organisme / Revue :** GitHub open-telemetry/semantic-conventions@v1.41.0 (e018fe6f)
- **Identifiant :** `OTEL-v1.41.0-GENAI`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-089.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-telemetry/semantic-conventions/e018fe6f91862f5ed63c082f87697cddac596784/docs/registry/attributes/gen-ai.md
- **Empreinte SHA-256 (LF) :** `74e99ecc4e35c6c7c7541dd310d1bd2f9e9c24f26e35338a332901cce43993da` (`39330` octets, `3715` mots)
- **Synthèse factuelle vérifiée :** Registre v1.41.0 des conventions sémantiques OpenTelemetry GenAI (60 attributs recensés dont 50 en statut Development, 10 en statut Deprecated et aucun Stable, incluant gen_ai.usage.cache_creation.input_tokens et cache_read).

### [3] SRC-090 — OpenTelemetry semantic-conventions-genai (commit 244465e9 — 85 attributs Development incluant cache_write)

- **Auteurs / Émetteur :** OpenTelemetry GenAI SIG Maintainers
- **Date de publication :** `2026-10-31`
- **Organisme / Revue :** GitHub open-telemetry/semantic-conventions-genai@244465e9
- **Identifiant :** `OTEL-GENAI-DEV-85`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-090.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/244465e94b9d7167fa5ed5c31a4b2b49ab6ddee5/docs/registry/attributes/gen-ai.md
- **Empreinte SHA-256 (LF) :** `b05fc94233aa5bf1dea4d7d5b60abf65b0255f49443f08ce9502a6bea7a18c75` (`62752` octets, `6234` mots)
- **Synthèse factuelle vérifiée :** Registre OpenTelemetry semantic-conventions-genai (commit 244465e9, 31 octobre 2026) exposant 85 attributs en statut Development et renommant l'écriture de cache en gen_ai.usage.cache_write.input_tokens.

### [4] SRC-077 — RFC 8785: JSON Canonicalization Scheme (JCS)

- **Auteurs / Émetteur :** Anders Rundgren, Bret Jordan, Samuel Erdtman
- **Date de publication :** `2020-06`
- **Organisme / Revue :** IETF RFC Editor (Independent Submission)
- **Identifiant :** `RFC8785`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-077.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8785.txt
- **Empreinte SHA-256 (LF) :** `be00e8aeddaf91fcf40b1c5ecaa33f2d627dac1e3c338e80a1eb0445e31af642` (`36840` octets, `5011` mots)
- **Synthèse factuelle vérifiée :** RFC 8785 (Independent Submission, statut Informational — JSON Canonicalization Scheme, JCS) fixant la canonisation déterministe (ordre UTF-16 des clés, formatage ECMAScript des nombres) préalable à tout hachage SHA-256.

### [5] SRC-044 — RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT)

- **Auteurs / Émetteur :** Henk Birkholz, Antoine Delignat-Lavaud, Cedric Fournet, Yogesh Deshpande, Steve Lasker
- **Date de publication :** `2026-06`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC9943`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-044.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9943.txt
- **Empreinte SHA-256 (LF) :** `1ed0ffb4007b7986d5d3ff4da1a0489d5b9d71c5eae4cd89a7f48ae650a19fef` (`65473` octets, `9449` mots)
- **Synthèse factuelle vérifiée :** RFC 9943 Standards Track (SCITT Architecture) spécifiant l'enregistrement transparent de déclarations signées dans un journal à append-only basé sur arbre de Merkle et reçu vérifiable.

### [6] SRC-018 — NIST FIPS 205: Stateless Hash-Based Digital Signature Standard (SLH-DSA)

- **Auteurs / Émetteur :** National Institute of Standards and Technology (NIST)
- **Date de publication :** `2024-08-13`
- **Organisme / Revue :** NIST Federal Information Processing Standards
- **Identifiant :** `NIST FIPS 205`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-018.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf
- **Empreinte SHA-256 (LF) :** `c27445a0f736858615b4625c234e30c8a222b2ea61cd5bfef18b7e45e53aad37` (`137225` octets, `21924` mots)
- **Synthèse factuelle vérifiée :** Norme FIPS 205 (SLH-DSA) du NIST normalisant les signatures post-quantiques sans état basées sur des arbres de hachage (variantes SHA2-128s/f), utilisée pour le scellement d'archives probatoires à long terme.

### [7] SRC-063 — Loi modernisant des dispositions législatives en matière de protection des renseignements personnels (Loi 25 / LQ 2021, c. 25, art. 12.1)

- **Auteurs / Émetteur :** Assemblée nationale du Québec
- **Date de publication :** `2021-09-22`
- **Organisme / Revue :** Publications du Québec
- **Identifiant :** `LQ-2021-C25`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-063.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://www.publicationsduquebec.gouv.qc.ca/fileadmin/Fichiers_client/lois_et_reglements/LoisAnnuelles/fr/2021/2021C25F.PDF
- **Empreinte SHA-256 (LF) :** `829e67f777ca0645b5b51a2ec4d8ec94739232c5a33ef76b7944d2bb81b61d87` (`143588` octets, `21658` mots)
- **Synthèse factuelle vérifiée :** Loi québécoise LQ 2021, c. 25 (Loi 25) sanctionnée en texte intégral : article 12.1 en vigueur depuis le 22 septembre 2023 (décisions automatisées : information, explication, observation, révision humaine), ÉFVP, sanctions administratives jusqu'à 10 M\$ CA (2 %) et amendes pénales jusqu'à 25 M\$ CA (4 %).

### [8] SRC-055 — OWASP Top 10 for Agentic Applications 2026 (v1.0, December 2025 — document complet CC BY-SA 4.0)

- **Auteurs / Émetteur :** OWASP GenAI Security Project
- **Date de publication :** `2025-12`
- **Organisme / Revue :** OWASP GenAI Security Project (Agentic Security Initiative — GenAI-Security-Corpus)
- **Identifiant :** `OWASP-AGENTIC-TOP10-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-055.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/genai-security-project/GenAI-Security-Corpus/main/corpus/agentic-top10/2026-final/OWASP-Top-10-for-Agentic-Applications-2026-v1.0.pdf
- **Empreinte SHA-256 (LF) :** `4d9f1c9f067fc284f01e8a904b172bbaceb97dd5a259a4d73c7d80f1482c22f3` (`100680` octets, `13820` mots)
- **Synthèse factuelle vérifiée :** Référentiel OWASP Top 10 for Agentic Applications 2026 (v1.0, CC BY-SA 4.0) recensant ASI01 à ASI10 avec mention explicite non-avis juridique (document primaire en statut L+ hors genai.owasp.org).

---

## Exclusions en statut F (`AO-01` — hors preuve)

- `https://www.legisquebec.gouv.qc.ca/fr/document/lc/P-39.1` — `HTTP_403` (`included_in_evidence: false`). Portail consolidé bloqué HTTP 403 (1 tentative AO-01) ; compensé en L+ par LQ 2021, c. 25 sanctionnée (SRC-063) et Rapport quinquennal CAI 2026 (SRC-064).
- `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 sur genai.owasp.org; compensé intégralement par le PDF officiel CC BY-SA 4.0 v1.0 archivé sur github.com/genai-security-project/GenAI-Security-Corpus (SRC-055, L+).
