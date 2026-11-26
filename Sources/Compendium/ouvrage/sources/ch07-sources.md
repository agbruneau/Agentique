# Base documentaire fermée — Chapitre 07 — Protocoles verticaux outil-modèle : épinglage MCP 2026-07-28, façades d'intention et intégrité SHA-256

**Protocole :** `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0,0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

---

### [1] SRC-072 — Model Context Protocol (MCP) Revision 2026-07-28 — Server Tools (tools.mdx)

- **Auteurs / Émetteur :** Model Context Protocol Maintainers
- **Date de publication :** `2026-07-28`
- **Organisme / Revue :** GitHub modelcontextprotocol/modelcontextprotocol@5f5440bb
- **Identifiant :** `MCP-2026-07-28-TOOLS`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-072.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/5f5440bb26a62e2cf3440b92da5a667efa03b267/docs/specification/2026-07-28/server/tools.mdx
- **Empreinte SHA-256 (LF) :** `ed550806a58eb7744b858fb9f26001aa5e55dac9e2babe88317cc81d9d4c490d` (`23788` octets, `2925` mots)
- **Synthèse factuelle vérifiée :** Section Server Tools de la spécification MCP 2026-07-28 (commit épinglé 5f5440bb) définissant tools/list, schémas JSON d'entrée/sortie et caractère non fiable des annotations d'outils.

### [2] SRC-074 — Model Context Protocol (MCP) Revision 2026-07-28 — Streamable HTTP Transport (streamable-http.mdx)

- **Auteurs / Émetteur :** Model Context Protocol Maintainers
- **Date de publication :** `2026-07-28`
- **Organisme / Revue :** GitHub modelcontextprotocol/modelcontextprotocol@5f5440bb
- **Identifiant :** `MCP-2026-07-28-HTTP`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-074.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/5f5440bb26a62e2cf3440b92da5a667efa03b267/docs/specification/2026-07-28/basic/transports/streamable-http.mdx
- **Empreinte SHA-256 (LF) :** `22574bf11e004068493787203ce92be1162107cad717bcb805a15780d4fa69c9` (`31155` octets, `3746` mots)
- **Synthèse factuelle vérifiée :** Spécification du transport Streamable HTTP de MCP 2026-07-28 (commit 5f5440bb) établissant le mode stateless par défaut, le retrait du flux GET et la validation stricte des en-têtes MCP-Protocol-Version, Mcp-Method et Mcp-Name.

### [3] SRC-078 — Model Context Protocol (MCP) Revision 2026-07-28 — Authorization Security Considerations (security-considerations.mdx)

- **Auteurs / Émetteur :** Model Context Protocol Maintainers
- **Date de publication :** `2026-07-28`
- **Organisme / Revue :** GitHub modelcontextprotocol/modelcontextprotocol@5f5440bb
- **Identifiant :** `MCP-2026-07-28-SEC`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-078.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/5f5440bb26a62e2cf3440b92da5a667efa03b267/docs/specification/2026-07-28/basic/authorization/security-considerations.mdx
- **Empreinte SHA-256 (LF) :** `71dd5f0f236cfa26fb33a3cebf6fc71d4797f1225a06c9cae85bdda54ae50bf8` (`9939` octets, `1104` mots)
- **Synthèse factuelle vérifiée :** Section Security Considerations de MCP 2026-07-28 (commit 5f5440bb) interdisant le passage de jeton (token passthrough), imposant RFC 8707 et protégeant les en-têtes contre l'exfiltration de secrets ou PII.

### [4] SRC-080 — Model Context Protocol (MCP) Revision 2026-07-28 — TypeScript Schema (schema.ts)

- **Auteurs / Émetteur :** Model Context Protocol Maintainers
- **Date de publication :** `2026-07-28`
- **Organisme / Revue :** GitHub modelcontextprotocol/modelcontextprotocol@5f5440bb
- **Identifiant :** `MCP-2026-07-28-SCHEMA-TS`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-080.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/5f5440bb26a62e2cf3440b92da5a667efa03b267/schema/2026-07-28/schema.ts
- **Empreinte SHA-256 (LF) :** `742750af0bb8c716e7030c4977c992b55d1adc4407e9e66997db5846baedc2cd` (`98426` octets, `12890` mots)
- **Synthèse factuelle vérifiée :** Schéma TypeScript normatif schema.ts de MCP 2026-07-28 (commit 5f5440bb) fixant exactement les types JSON-RPC, métadonnées _meta réservées et structures de résultats d'outils.

### [5] SRC-081 — MCP SEP-2596: Specification Feature Lifecycle and Deprecation Policy (Status: Final)

- **Auteurs / Émetteur :** Den Delimarsky (@localden)
- **Date de publication :** `2026-11-22`
- **Organisme / Revue :** GitHub modelcontextprotocol/modelcontextprotocol@862397ce
- **Identifiant :** `MCP-SEP-2596`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-081.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/862397cec702e8f828713071da501cf56158e8fc/seps/2596-spec-feature-lifecycle-and-deprecation.md
- **Empreinte SHA-256 (LF) :** `6608969be1213cafd12edc27269519be54b3fadb0443ff0f1b5fc76f75752de4` (`26389` octets, `3378` mots)
- **Synthèse factuelle vérifiée :** Proposition SEP-2596 (Statut : Final) formalisant le cycle de vie des fonctionnalités MCP (Active, Deprecated, Removed) avec une fenêtre minimale de 12 mois entre dépréciation et retrait (soit jusqu'au 2027-07-28 pour 2026-07-28).

### [6] SRC-082 — MCP SEP-3398: Release Cycle Updates (Status: Accepted)

- **Auteurs / Émetteur :** Kurtis Van Gent (@kurtisvg)
- **Date de publication :** `2026-10-14`
- **Organisme / Revue :** GitHub modelcontextprotocol/modelcontextprotocol@862397ce
- **Identifiant :** `MCP-SEP-3398`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-082.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/862397cec702e8f828713071da501cf56158e8fc/seps/3398-release-cycle-updates.md
- **Empreinte SHA-256 (LF) :** `64aee02f2717dc1b290c079a012c470baccd53f6299103b6713a545ccae03be5` (`27669` octets, `3795` mots)
- **Synthèse factuelle vérifiée :** Proposition SEP-3398 (Statut : Accepted) instaurant un cycle semestriel prévisible (dernier mardi de mars et de septembre) et reportant l'échéance de publication de la spécification MCP initialement prévue en décembre 2026 au 30 mars 2027.

### [7] SRC-038 — Model Context Protocol (MCP) Specification — Revision 2025-11-25 (corpus normatif complet)

- **Auteurs / Émetteur :** Model Context Protocol Maintainers
- **Date de publication :** `2025-11-25`
- **Organisme / Revue :** Model Context Protocol (GitHub modelcontextprotocol/modelcontextprotocol — spec 2025-11-25)
- **Identifiant :** `MCP-SPEC-2025-11-25`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-038.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://github.com/modelcontextprotocol/modelcontextprotocol/tree/main/docs/specification/2025-11-25
- **Empreinte SHA-256 (LF) :** `938fca60c06c92e10cd6448f31d90fbb81d03adcb1952a21915d219f685e96a9` (`757889` octets, `62231` mots)
- **Synthèse factuelle vérifiée :** Archive normative de la révision MCP 2025-11-25 conservée exclusivement comme témoin de la discordance DISC-05 face à la révision épinglée 2026-07-28.

### [8] SRC-057 — Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem

- **Auteurs / Émetteur :** Obada Kraishan
- **Date de publication :** `2026-09-15`
- **Organisme / Revue :** arXiv
- **Identifiant :** `arXiv:2609.14119`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-057.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2609.14119
- **Empreinte SHA-256 (LF) :** `cae21acac54fea61a6270540a888a090731fac9d0de3ae0f121f3d51d59ed7e9` (`49308` octets, `7412` mots)
- **Synthèse factuelle vérifiée :** Recensement empirique d'Obada Kraishan (septembre 2026) sur 21 643 serveurs MCP et 72 606 versions : parmi 8 900 serveurs multi-versions, 51,09 % changent entre versions, 40,58 % présentent une dérive sémantique silencieuse et 4,16 % redirigent vers un autre hôte (OR = 2,96).

### [9] SRC-009 — RFC 8707: Resource Indicators for OAuth 2.0

- **Auteurs / Émetteur :** Brian Campbell, John Bradley, Hannes Tschofenig
- **Date de publication :** `2020-02`
- **Organisme / Revue :** IETF Standards Track
- **Identifiant :** `RFC 8707`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-009.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8707.txt
- **Empreinte SHA-256 (LF) :** `7fb70d66034ad271cda08ff66a791627b774e81a121be798165c0ea70ec81b01` (`23316` octets, `3145` mots)
- **Synthèse factuelle vérifiée :** Extension OAuth 2.0 Resource Indicators (parameter resource) imposant une liaison stricte d'audience (aud) lors des demandes et échanges de jetons ; fonde le rejet du token passthrough (EXIG-MCP-11).

### [10] SRC-077 — RFC 8785: JSON Canonicalization Scheme (JCS)

- **Auteurs / Émetteur :** Anders Rundgren, Bret Jordan, Samuel Erdtman
- **Date de publication :** `2020-06`
- **Organisme / Revue :** IETF RFC Editor (Independent Submission)
- **Identifiant :** `RFC 8785`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-077.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8785.txt
- **Empreinte SHA-256 (LF) :** `be00e8aeddaf91fcf40b1c5ecaa33f2d627dac1e3c338e80a1eb0445e31af642` (`36840` octets, `5011` mots)
- **Synthèse factuelle vérifiée :** RFC 8785 (Independent Submission, statut Informational — JSON Canonicalization Scheme, JCS) fixant la canonisation déterministe (ordre UTF-16 des clés, formatage ECMAScript des nombres) préalable à tout hachage SHA-256.

### [11] SRC-129 — RFC 9207: OAuth 2.0 Authorization Server Issuer Identification

- **Auteurs / Émetteur :** Karsten Meyer zu Selhausen, Daniel Fett
- **Date de publication :** `2022-03`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC 9207`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-129.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9207.txt
- **Empreinte SHA-256 (LF) :** `033ca79b0d49be0aa32623798e18b209dd2c63ec52e48838ed3c479b849a7d66` (`18611` octets, `2522` mots)
- **Synthèse factuelle vérifiée :** Standard IETF RFC 9207 (Meyer zu Selhausen et Fett, mars 2022) imposant le paramètre iss dans les réponses d'autorisation OAuth 2.0 pour prévenir les attaques par confusion d'émetteur.

### [12] SRC-134 — RFC 9728: OAuth 2.0 Protected Resource Metadata

- **Auteurs / Émetteur :** Michael B. Jones, Phil Hunt, Aaron Parecki
- **Date de publication :** `2025-04`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC 9728`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-134.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9728.txt
- **Empreinte SHA-256 (LF) :** `148d22364f63c78ae696363667ab074246c1fadf07c9d5eaab814296333953c0` (`53311` octets, `7435` mots)
- **Synthèse factuelle vérifiée :** Standard IETF RFC 9728 (Jones, Hunt et Parecki, avril 2025) définissant les métadonnées de ressources protégées OAuth 2.0 adoptées pour la découverte d'autorisation MCP.

### [13] SRC-055 — OWASP Top 10 for Agentic Applications 2026 (v1.0, December 2025 — document complet CC BY-SA 4.0)

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

- `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 sur genai.owasp.org; compensé intégralement par le PDF officiel CC BY-SA 4.0 v1.0 archivé sur github.com/genai-security-project/GenAI-Security-Corpus (SRC-055, L+).
