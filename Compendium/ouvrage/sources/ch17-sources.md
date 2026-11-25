# Base documentaire fermée — Chapitre 17 — Chaîne de mandat OBO à deux sauts, approbation cryptographique CIBA, KYA tiers et asymétrie de révocation

**Protocole :** `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0,0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

---

### [1] SRC-041 — RFC 8693: OAuth 2.0 Token Exchange

- **Auteurs / Émetteur :** Michael B. Jones, Anthony Nadalin, Brian Campbell, John Bradley, Chuck Mortimore
- **Date de publication :** `2020-01`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC8693`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-041.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8693.txt
- **Empreinte SHA-256 (LF) :** `22f271006669060ee5142350371ee70ed30bba6db93a9d8b43d897d462586a6f` (`56867` octets, `7815` mots)
- **Synthèse factuelle vérifiée :** RFC 8693 Standards Track (OAuth 2.0 Token Exchange) définissant l'échange de jetons, la revendication immuable sub et l'imbrication explicite des acteurs délégués act.

### [2] SRC-009 — RFC 8707: Resource Indicators for OAuth 2.0

- **Auteurs / Émetteur :** Brian Campbell, John Bradley, Hannes Tschofenig
- **Date de publication :** `2020-02`
- **Organisme / Revue :** IETF Standards Track
- **Identifiant :** `RFC 8707`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-009.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8707.txt
- **Empreinte SHA-256 (LF) :** `7fb70d66034ad271cda08ff66a791627b774e81a121be798165c0ea70ec81b01` (`23316` octets, `3145` mots)
- **Synthèse factuelle vérifiée :** Extension OAuth 2.0 Resource Indicators (parameter resource) imposant une liaison stricte d'audience (aud) lors des demandes et échanges de jetons ; fonde le rejet du token passthrough (EXIG-MCP-11).

### [3] SRC-042 — RFC 9396: OAuth 2.0 Rich Authorization Requests (RAR)

- **Auteurs / Émetteur :** Torsten Lodderstedt, Justin Richer, Brian Campbell
- **Date de publication :** `2023-05`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC9396`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-042.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9396.txt
- **Empreinte SHA-256 (LF) :** `e334d06f14081317caf9d457dcbffeae877c5e5009f2452d2f11adcd47d68f6b` (`55352` octets, `7380` mots)
- **Synthèse factuelle vérifiée :** RFC 9396 Standards Track (Rich Authorization Requests) permettant d'exprimer des autorisations structurées fines via authorization_details (types d'action, montants, cibles).

### [4] SRC-043 — RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)

- **Auteurs / Émetteur :** Daniel Fett, Brian Campbell, John Bradley, Torsten Lodderstedt et al.
- **Date de publication :** `2023-09`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC9449`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-043.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9449.txt
- **Empreinte SHA-256 (LF) :** `5e0267f9b8801cc882ec1dcb1d1d220cbe8cb38bbe428362cd1c8a2b33ef30e0` (`83632` octets, `12014` mots)
- **Synthèse factuelle vérifiée :** RFC 9449 Standards Track (OAuth 2.0 DPoP) liant cryptographiquement les jetons d'accès à une clé éphémère du client via l'en-tête dpop+jwt (htm, htu, ath, jti) et la revendication cnf.

### [5] SRC-045 — OpenID Connect Client-Initiated Backchannel Authentication Flow — Core 1.0

- **Auteurs / Émetteur :** Gonzalo Fernandez, Axel Nennker, Dave Tonge et al. (OpenID Foundation)
- **Date de publication :** `2021-09-01`
- **Organisme / Revue :** OpenID Foundation
- **Identifiant :** `OIDC-CIBA-1.0`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-045.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html
- **Empreinte SHA-256 (LF) :** `fb983307e736a3747a1dfa27f4e698f41cd45f4854f129c7cfc3c4a24c3d8020` (`70895` octets, `9881` mots)
- **Synthèse factuelle vérifiée :** Spécification OpenID Connect CIBA Core 1.0 encadrant les flux d'authentification et d'approbation hors bande asynchrones (auth_req_id) dissociés du canal d'exécution de l'agent.

### [6] SRC-004 — RFC 7493: The I-JSON Message Format

- **Auteurs / Émetteur :** Tim Bray (Ed.)
- **Date de publication :** `2015-03`
- **Organisme / Revue :** IETF Standards Track
- **Identifiant :** `RFC 7493`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-004.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc7493.txt
- **Empreinte SHA-256 (LF) :** `79cf90d87551d63e750c72b383876c2617311a31fb5a9e0f72dc69f3dcb9600e` (`11483` octets, `1941` mots)
- **Synthèse factuelle vérifiée :** Profil I-JSON (Internet JSON) Standards Track interdisant les clés dupliquées, les valeurs NaN/Infinity, les surrogates UTF-8 isolés et les ambiguïtés de précision numérique : socle normatif des montants entiers et du condensat C.6.

### [7] SRC-013 — Transaction Tokens (Internet-Draft draft-ietf-oauth-transaction-tokens-11 — brouillon IETF WG)

- **Auteurs / Émetteur :** Atul Tulshibagwale, George Fletcher, Pieter Kasselman
- **Date de publication :** `2026-07-30`
- **Organisme / Revue :** IETF OAuth Working Group (Internet-Draft)
- **Identifiant :** `draft-ietf-oauth-transaction-tokens-11`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-013.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://www.ietf.org/archive/id/draft-ietf-oauth-transaction-tokens-11.txt
- **Empreinte SHA-256 (LF) :** `64447dddda3a5d9fe7440a2f9ff84b5c14c9e55c23f936963f98e37fad483f9c` (`70155` octets, `10658` mots)
- **Synthèse factuelle vérifiée :** Brouillon IETF OAuth Working Group (draft-ietf-oauth-transaction-tokens-11, non encore RFC au gel) définissant des jetons de transaction compacts à taille constante O(1) pour propager sujet, charge de travail et contexte de requête entre microservices.

### [8] SRC-017 — OAuth 2.0 Agent Authorization Explicit Revocation (Internet-Draft draft-chen-oauth-agent-revocation-01 — brouillon individuel)

- **Auteurs / Émetteur :** Meiling Chen, Li Su
- **Date de publication :** `2026-10-30`
- **Organisme / Revue :** IETF Internet-Draft (Individual Submission)
- **Identifiant :** `draft-chen-oauth-agent-revocation-01`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-017.txt`, score AACODS `9.5/12`)
- **URL d'origine :** https://www.ietf.org/archive/id/draft-chen-oauth-agent-revocation-01.txt
- **Empreinte SHA-256 (LF) :** `25d9788ca0cb574ff0c4bbc3215ad4094bb8f9cde660e2e15a184c7a81bd9a22` (`14051` octets, `1968` mots)
- **Synthèse factuelle vérifiée :** Brouillon individuel IETF (draft-chen-oauth-agent-revocation-01, non adopté par un WG au 2026-12-02) proposant une révocation explicite, en lot et en cascade pour les délégations d'agents OAuth 2.0.

### [9] SRC-019 — OpenID Shared Signals Framework Specification 1.0

- **Auteurs / Émetteur :** Atul Tulshibagwale, Tim Cappalli, Apoorva Deshpande et al.
- **Date de publication :** `2025-08-29`
- **Organisme / Revue :** OpenID Foundation Shared Signals Working Group
- **Identifiant :** `OpenID SSF 1.0`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-019.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://openid.net/specs/openid-sharedsignals-framework-1_0.html
- **Empreinte SHA-256 (LF) :** `68263a1cbe315de9ae3519ff2321053aa92ca72096ae3f0872b289d0d046c6a7` (`87785` octets, `12202` mots)
- **Synthèse factuelle vérifiée :** Spécification OpenID Shared Signals Framework (SSF 1.0) normalisant la diffusion asynchrone d'événements de sécurité (SET) entre émetteurs et récepteurs pour la suspension rapide de sessions.

### [10] SRC-020 — OpenID Continuous Access Evaluation Profile (CAEP) 1.0

- **Auteurs / Émetteur :** Tim Cappalli, Atul Tulshibagwale
- **Date de publication :** `2025-08-29`
- **Organisme / Revue :** OpenID Foundation Shared Signals Working Group
- **Identifiant :** `OpenID CAEP 1.0`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-020.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://openid.net/specs/openid-caep-1_0.html
- **Empreinte SHA-256 (LF) :** `f3114cfa038f095958641996c432193e843cb2395a2b0cd3ba13ca31f8a2345f` (`29497` octets, `3733` mots)
- **Synthèse factuelle vérifiée :** Profil OpenID Continuous Access Evaluation Profile (CAEP 1.0) définissant les types d'événements de changement d'état d'session, d'assurance et de révocation d'identifiants temps réel.

### [11] SRC-128 — RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens

- **Auteurs / Émetteur :** Brian Campbell, John Bradley, Nat Sakimura, Torsten Lodderstedt
- **Date de publication :** `2020-02`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC 8705`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-128.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8705.txt
- **Empreinte SHA-256 (LF) :** `f3a8ff8dc00c2bdbc0059fb52300945b33d7f0dbfa5ded5a494b13f99ddfc6c8` (`54252` octets, `7366` mots)
- **Synthèse factuelle vérifiée :** Standard IETF RFC 8705 (Campbell et al., fév. 2020) régissant l'authentification mutuelle TLS (mTLS) et la liaison cryptographique des jetons OAuth 2.0 au certificat client.

### [12] SRC-129 — RFC 9207: OAuth 2.0 Authorization Server Issuer Identification

- **Auteurs / Émetteur :** Karsten Meyer zu Selhausen, Daniel Fett
- **Date de publication :** `2022-03`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC 9207`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-129.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9207.txt
- **Empreinte SHA-256 (LF) :** `033ca79b0d49be0aa32623798e18b209dd2c63ec52e48838ed3c479b849a7d66` (`18611` octets, `2522` mots)
- **Synthèse factuelle vérifiée :** Standard IETF RFC 9207 (Meyer zu Selhausen et Fett, mars 2022) imposant le paramètre iss dans les réponses d'autorisation OAuth 2.0 pour prévenir les attaques par confusion d'émetteur.

### [13] SRC-133 — RFC 9700: Best Current Practice for OAuth 2.0 Security (BCP 240)

- **Auteurs / Émetteur :** Torsten Lodderstedt, John Bradley, Andrey Labunets, Daniel Fett
- **Date de publication :** `2025-01`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC 9700`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-133.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9700.txt
- **Empreinte SHA-256 (LF) :** `7ffb6c499888b7d9a9cdbbb9eb2d4cc156d775e5df46bc288175b60d0910d63b` (`113847` octets, `16604` mots)
- **Synthèse factuelle vérifiée :** Standard IETF BCP 240 / RFC 9700 (Lodderstedt et al., janv. 2025) consolidant les meilleures pratiques de sécurité OAuth 2.0 (interdiction des flux implicite et mot de passe, PKCE et épinglage).

### [14] SRC-134 — RFC 9728: OAuth 2.0 Protected Resource Metadata

- **Auteurs / Émetteur :** Michael B. Jones, Phil Hunt, Aaron Parecki
- **Date de publication :** `2025-04`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC 9728`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-134.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9728.txt
- **Empreinte SHA-256 (LF) :** `148d22364f63c78ae696363667ab074246c1fadf07c9d5eaab814296333953c0` (`53311` octets, `7435` mots)
- **Synthèse factuelle vérifiée :** Standard IETF RFC 9728 (Jones, Hunt et Parecki, avril 2025) définissant les métadonnées de ressources protégées OAuth 2.0 adoptées pour la découverte d'autorisation MCP.

### [15] SRC-071 — AIBanks.ca — The Canadian Bank AI Index (2026 Q4 edition, agrégateur tiers indépendant)

- **Auteurs / Émetteur :** AIBanks.ca
- **Date de publication :** `2026-11-01`
- **Organisme / Revue :** AIBanks.ca (agrégateur tiers indépendant — index public de preuves)
- **Identifiant :** `AIBANKS-CA-AMF-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-071.txt`, score AACODS `9.0/12`)
- **URL d'origine :** https://www.aibanks.ca/
- **Empreinte SHA-256 (LF) :** `2d39751c5fed55ad19aebd3cc238f8a1a26d6b266bb8bc3f7ee1e0e37a796e8b` (`12404` octets, `1985` mots)
- **Synthèse factuelle vérifiée :** Agrégateur canadien ouvert AIBanks.ca (édition T4 au 1er novembre 2026) confirmant l'échéance du 1er mai 2027 pour BSIF E-23 et signalant l'échéance attendue du 1er mai 2027 de la ligne directrice IA de l'AMF (rapportée sous réserve car le portail lautorite.qc.ca est en statut F).

---

## Exclusions en statut F (`AO-01` — hors preuve)

- `https://lautorite.qc.ca/` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 Cloudflare WAF sur lautorite.qc.ca (1 tentative AO-01) et absence de l'archive locale 2026/documents/Note AMF IA.pdf ; date attendue du 1er mai 2027 corroborée sous réserve explicite via AIBanks.ca (SRC-071, L+).
- `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 sur genai.owasp.org; compensé intégralement par le PDF officiel CC BY-SA 4.0 v1.0 archivé sur github.com/genai-security-project/GenAI-Security-Corpus (SRC-055, L+).
