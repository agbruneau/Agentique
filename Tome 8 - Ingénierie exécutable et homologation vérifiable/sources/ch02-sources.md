# Base documentaire fermée — Chapitre 2 — Identité NHI, délégation OBO, choc PQC HTTP 431 et double couloir probatoire

**Protocole :** `MLR-PRISMA-SCR-MANUEL-VOL8-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

---

### [1] SRC-046 — SPIFFE Concepts — Workload Identity, SPIFFE ID and SVID

- **Auteurs / Émetteur :** SPIFFE / Cloud Native Computing Foundation
- **Date de publication :** `2026`
- **Organisme / Revue :** CNCF SPIFFE
- **Identifiant :** `SPIFFE-CONCEPTS-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-046.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
- **Empreinte SHA-256 (LF) :** `d85539da6604e026266545f74198661e718d6fd2d7316178cab87565f44c9851` (`6860` octets, `1080` mots)
- **Synthèse factuelle vérifiée :** Spécification SPIFFE décrivant les identités de charge de travail cryptographiques (SPIFFE ID URI) et les documents SVID X.509/JWT à courte durée de vie sans secret statique.

### [2] SRC-047 — Workload Identity Practices (draft-ietf-wimse-workload-identity-practices-08)

- **Auteurs / Émetteur :** IETF WIMSE Working Group
- **Date de publication :** `2026-10-30`
- **Organisme / Revue :** IETF Datatracker
- **Identifiant :** `IETF-WIMSE-WIP-08`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-047.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://www.ietf.org/archive/id/draft-ietf-wimse-workload-identity-practices-08.txt
- **Empreinte SHA-256 (LF) :** `863cee96178b93722999cbceee5ff74cb7b6203356af2ae571e289c6e72b408b` (`57958` octets, `8930` mots)
- **Synthèse factuelle vérifiée :** Brouillon IETF WIMSE (draft-ietf-wimse-workload-identity-practices-08) détaillant l'atténuation de portée et l'isolation de réseaux de métadonnées pour les charges de travail distribuées.

### [3] SRC-048 — AI Identity Management System (draft-ietf-wimse-aims-01)

- **Auteurs / Émetteur :** IETF WIMSE Working Group
- **Date de publication :** `2026-11-02`
- **Organisme / Revue :** IETF Datatracker
- **Identifiant :** `IETF-WIMSE-AIMS-01`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-048.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://www.ietf.org/archive/id/draft-ietf-wimse-aims-01.txt
- **Empreinte SHA-256 (LF) :** `ab53c74913dd1337f6183a03825d985dc1f39bc613721a54e9a3d3092231045e` (`69988` octets, `10027` mots)
- **Synthèse factuelle vérifiée :** Brouillon IETF WIMSE AIMS (draft-ietf-wimse-aims-01) proposant une architecture de gestion des identités et délégations propres aux systèmes d'agents IA.

### [4] SRC-041 — RFC 8693: OAuth 2.0 Token Exchange

- **Auteurs / Émetteur :** Michael B. Jones, Anthony Nadalin, Brian Campbell, John Bradley, Chuck Mortimore
- **Date de publication :** `2020-01`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC8693`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-041.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8693.txt
- **Empreinte SHA-256 (LF) :** `22f271006669060ee5142350371ee70ed30bba6db93a9d8b43d897d462586a6f` (`56867` octets, `7815` mots)
- **Synthèse factuelle vérifiée :** RFC 8693 Standards Track (OAuth 2.0 Token Exchange) définissant l'échange de jetons, la revendication immuable sub et l'imbrication explicite des acteurs délégués act.

### [5] SRC-009 — RFC 8707: Resource Indicators for OAuth 2.0

- **Auteurs / Émetteur :** Brian Campbell, John Bradley, Hannes Tschofenig
- **Date de publication :** `2020-02`
- **Organisme / Revue :** IETF Standards Track
- **Identifiant :** `RFC 8707`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-009.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8707.txt
- **Empreinte SHA-256 (LF) :** `7fb70d66034ad271cda08ff66a791627b774e81a121be798165c0ea70ec81b01` (`23316` octets, `3145` mots)
- **Synthèse factuelle vérifiée :** Extension OAuth 2.0 Resource Indicators (parameter resource) imposant une liaison stricte d'audience (aud) lors des demandes et échanges de jetons ; fonde le rejet du token passthrough (EXIG-MCP-11).

### [6] SRC-043 — RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)

- **Auteurs / Émetteur :** Daniel Fett, Brian Campbell, John Bradley, Torsten Lodderstedt et al.
- **Date de publication :** `2023-09`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC9449`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-043.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9449.txt
- **Empreinte SHA-256 (LF) :** `5e0267f9b8801cc882ec1dcb1d1d220cbe8cb38bbe428362cd1c8a2b33ef30e0` (`83632` octets, `12014` mots)
- **Synthèse factuelle vérifiée :** RFC 9449 Standards Track (OAuth 2.0 DPoP) liant cryptographiquement les jetons d'accès à une clé éphémère du client via l'en-tête dpop+jwt (htm, htu, ath, jti) et la revendication cnf.

### [7] SRC-042 — RFC 9396: OAuth 2.0 Rich Authorization Requests (RAR)

- **Auteurs / Émetteur :** Torsten Lodderstedt, Justin Richer, Brian Campbell
- **Date de publication :** `2023-05`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC9396`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-042.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9396.txt
- **Empreinte SHA-256 (LF) :** `e334d06f14081317caf9d457dcbffeae877c5e5009f2452d2f11adcd47d68f6b` (`55352` octets, `7380` mots)
- **Synthèse factuelle vérifiée :** RFC 9396 Standards Track (Rich Authorization Requests) permettant d'exprimer des autorisations structurées fines via authorization_details (types d'action, montants, cibles).

### [8] SRC-045 — OpenID Connect Client-Initiated Backchannel Authentication Flow — Core 1.0

- **Auteurs / Émetteur :** Gonzalo Fernandez, Axel Nennker, Dave Tonge et al. (OpenID Foundation)
- **Date de publication :** `2021-09-01`
- **Organisme / Revue :** OpenID Foundation
- **Identifiant :** `OIDC-CIBA-1.0`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-045.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html
- **Empreinte SHA-256 (LF) :** `fb983307e736a3747a1dfa27f4e698f41cd45f4854f129c7cfc3c4a24c3d8020` (`70895` octets, `9881` mots)
- **Synthèse factuelle vérifiée :** Spécification OpenID Connect CIBA Core 1.0 encadrant les flux d'authentification et d'approbation hors bande asynchrones (auth_req_id) dissociés du canal d'exécution de l'agent.

### [9] SRC-004 — RFC 7493: The I-JSON Message Format

- **Auteurs / Émetteur :** Tim Bray (Ed.)
- **Date de publication :** `2015-03`
- **Organisme / Revue :** IETF Standards Track
- **Identifiant :** `RFC 7493`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-004.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc7493.txt
- **Empreinte SHA-256 (LF) :** `79cf90d87551d63e750c72b383876c2617311a31fb5a9e0f72dc69f3dcb9600e` (`11483` octets, `1941` mots)
- **Synthèse factuelle vérifiée :** Profil I-JSON (Internet JSON) Standards Track interdisant les clés dupliquées, les valeurs NaN/Infinity, les surrogates UTF-8 isolés et les ambiguïtés de précision numérique : socle normatif des montants entiers et du condensat C.6.

### [10] SRC-019 — OpenID Shared Signals Framework Specification 1.0

- **Auteurs / Émetteur :** Atul Tulshibagwale, Tim Cappalli, Apoorva Deshpande et al.
- **Date de publication :** `2025-08-29`
- **Organisme / Revue :** OpenID Foundation Shared Signals Working Group
- **Identifiant :** `OpenID SSF 1.0`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-019.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://openid.net/specs/openid-sharedsignals-framework-1_0.html
- **Empreinte SHA-256 (LF) :** `68263a1cbe315de9ae3519ff2321053aa92ca72096ae3f0872b289d0d046c6a7` (`87785` octets, `12202` mots)
- **Synthèse factuelle vérifiée :** Spécification OpenID Shared Signals Framework (SSF 1.0) normalisant la diffusion asynchrone d'événements de sécurité (SET) entre émetteurs et récepteurs pour la suspension rapide de sessions.

### [11] SRC-020 — OpenID Continuous Access Evaluation Profile (CAEP) 1.0

- **Auteurs / Émetteur :** Tim Cappalli, Atul Tulshibagwale
- **Date de publication :** `2025-08-29`
- **Organisme / Revue :** OpenID Foundation Shared Signals Working Group
- **Identifiant :** `OpenID CAEP 1.0`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-020.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://openid.net/specs/openid-caep-1_0.html
- **Empreinte SHA-256 (LF) :** `f3114cfa038f095958641996c432193e843cb2395a2b0cd3ba13ca31f8a2345f` (`29497` octets, `3733` mots)
- **Synthèse factuelle vérifiée :** Profil OpenID Continuous Access Evaluation Profile (CAEP 1.0) définissant les types d'événements de changement d'état d'session, d'assurance et de révocation d'identifiants temps réel.

### [12] SRC-017 — OAuth 2.0 Agent Authorization Explicit Revocation (Internet-Draft draft-chen-oauth-agent-revocation-01 — brouillon individuel)

- **Auteurs / Émetteur :** Meiling Chen, Li Su
- **Date de publication :** `2026-10-30`
- **Organisme / Revue :** IETF Internet-Draft (Individual Submission)
- **Identifiant :** `draft-chen-oauth-agent-revocation-01`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-017.txt`, score AACODS `9.5/12`)
- **URL d'origine :** https://www.ietf.org/archive/id/draft-chen-oauth-agent-revocation-01.txt
- **Empreinte SHA-256 (LF) :** `25d9788ca0cb574ff0c4bbc3215ad4094bb8f9cde660e2e15a184c7a81bd9a22` (`14051` octets, `1968` mots)
- **Synthèse factuelle vérifiée :** Brouillon individuel IETF (draft-chen-oauth-agent-revocation-01, non adopté par un WG au 2026-12-02) proposant une révocation explicite, en lot et en cascade pour les délégations d'agents OAuth 2.0.

### [13] SRC-050 — NIST FIPS 204: Module-Lattice-Based Digital Signature Standard (ML-DSA)

- **Auteurs / Émetteur :** National Institute of Standards and Technology (NIST)
- **Date de publication :** `2024-08-13`
- **Organisme / Revue :** NIST Computer Security Resource Center
- **Identifiant :** `NIST-FIPS-204`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-050.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf
- **Empreinte SHA-256 (LF) :** `14b6c1706d2c4a1645a7c285e37e9e7e33dd98348302c84c11db9613c0f1d267` (`150660` octets, `25028` mots)
- **Synthèse factuelle vérifiée :** Norme NIST FIPS 204 (ML-DSA) normalisant la signature numérique post-quantique basée sur réseaux et fixant les tailles exactes de clés et signatures (ML-DSA-65 : 3 309 o ; ML-DSA-87 : 4 627 o).

### [14] SRC-012 — RFC 9964: ML-DSA for JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE)

- **Auteurs / Émetteur :** Mike Prorock, Orie Steele
- **Date de publication :** `2026-05`
- **Organisme / Revue :** IETF Standards Track
- **Identifiant :** `RFC 9964`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-012.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9964.txt
- **Empreinte SHA-256 (LF) :** `a7c42dac175c3a9c95d2e36fe43afaddc35c7586d16cfe15e71ff67f47479c8b` (`178023` octets, `4971` mots)
- **Synthèse factuelle vérifiée :** RFC 9964 Standards Track spécifiant les sérialisations JOSE et COSE pour ML-DSA (FIPS 204) : ML-DSA-44 (sig. 2 420 octets), ML-DSA-65 (3 309 octets) et ML-DSA-87 (4 627 octets), créant un risque de dépassement HTTP 431 (8 192 octets) sur les chaînes OBO multi-sauts.

### [15] SRC-076 — RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)

- **Auteurs / Émetteur :** Simon Josefsson, Ilari Liusvaara
- **Date de publication :** `2017-01`
- **Organisme / Revue :** IRTF / IETF RFC Editor
- **Identifiant :** `RFC8032`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-076.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8032.txt
- **Empreinte SHA-256 (LF) :** `29c43d9f68a78933e16355eba485ce654fb7256858b69f8d1f02af9ea40e25cc` (`87266` octets, `12059` mots)
- **Synthèse factuelle vérifiée :** RFC 8032 Standards Track (EdDSA) spécifiant Ed25519 avec signatures fixes de 64 octets, utilisé comme référence de comparaison de taille face aux signatures post-quantiques ML-DSA.

### [16] SRC-013 — Transaction Tokens (Internet-Draft draft-ietf-oauth-transaction-tokens-11 — brouillon IETF WG)

- **Auteurs / Émetteur :** Atul Tulshibagwale, George Fletcher, Pieter Kasselman
- **Date de publication :** `2026-07-30`
- **Organisme / Revue :** IETF OAuth Working Group (Internet-Draft)
- **Identifiant :** `draft-ietf-oauth-transaction-tokens-11`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-013.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://www.ietf.org/archive/id/draft-ietf-oauth-transaction-tokens-11.txt
- **Empreinte SHA-256 (LF) :** `64447dddda3a5d9fe7440a2f9ff84b5c14c9e55c23f936963f98e37fad483f9c` (`70155` octets, `10658` mots)
- **Synthèse factuelle vérifiée :** Brouillon IETF OAuth Working Group (draft-ietf-oauth-transaction-tokens-11, non encore RFC au gel) définissant des jetons de transaction compacts à taille constante O(1) pour propager sujet, charge de travail et contexte de requête entre microservices.

### [17] SRC-089 — OpenTelemetry Semantic Conventions v1.41.0 — GenAI Attribute Registry (gen-ai.md)

- **Auteurs / Émetteur :** OpenTelemetry Semantic Conventions Maintainers
- **Date de publication :** `2026-04-28`
- **Organisme / Revue :** GitHub open-telemetry/semantic-conventions@v1.41.0 (e018fe6f)
- **Identifiant :** `OTEL-v1.41.0-GENAI`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-089.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-telemetry/semantic-conventions/e018fe6f91862f5ed63c082f87697cddac596784/docs/registry/attributes/gen-ai.md
- **Empreinte SHA-256 (LF) :** `74e99ecc4e35c6c7c7541dd310d1bd2f9e9c24f26e35338a332901cce43993da` (`39330` octets, `3715` mots)
- **Synthèse factuelle vérifiée :** Registre v1.41.0 des conventions sémantiques OpenTelemetry GenAI (60 attributs recensés dont 50 en statut Development, 10 en statut Deprecated et aucun Stable, incluant gen_ai.usage.cache_creation.input_tokens et cache_read).

### [18] SRC-090 — OpenTelemetry semantic-conventions-genai (commit 244465e9 — 85 attributs Development incluant cache_write)

- **Auteurs / Émetteur :** OpenTelemetry GenAI SIG Maintainers
- **Date de publication :** `2026-10-31`
- **Organisme / Revue :** GitHub open-telemetry/semantic-conventions-genai@244465e9
- **Identifiant :** `OTEL-GENAI-DEV-85`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-090.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/244465e94b9d7167fa5ed5c31a4b2b49ab6ddee5/docs/registry/attributes/gen-ai.md
- **Empreinte SHA-256 (LF) :** `b05fc94233aa5bf1dea4d7d5b60abf65b0255f49443f08ce9502a6bea7a18c75` (`62752` octets, `6234` mots)
- **Synthèse factuelle vérifiée :** Registre OpenTelemetry semantic-conventions-genai (commit 244465e9, 31 octobre 2026) exposant 85 attributs en statut Development et renommant l'écriture de cache en gen_ai.usage.cache_write.input_tokens.

### [19] SRC-037 — OpenTelemetry Semantic Conventions for Generative AI Agent & Execute Tool Spans (gen_ai.operation.name)

- **Auteurs / Émetteur :** OpenTelemetry GenAI SIG
- **Date de publication :** `2026-11-05`
- **Organisme / Revue :** CNCF / OpenTelemetry Semantic Conventions (GenAI SIG — agent-spans, execute-tool & registry.yaml)
- **Identifiant :** `OTEL-GENAI-AGENT-TOOL-SPANS`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-037.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-agent-spans.md
- **Empreinte SHA-256 (LF) :** `1b2526202e8aef9b15819b89cd1c34eefd8d10be3dac7b05f714597c34d5549c` (`125111` octets, `13159` mots)
- **Synthèse factuelle vérifiée :** Conventions sémantiques OpenTelemetry GenAI Agent & Framework Spans (gen-ai-agent-spans.md, statut Development) décrivant les spans create_agent, invoke_agent et execute_tool.

### [20] SRC-044 — RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT)

- **Auteurs / Émetteur :** Henk Birkholz, Antoine Delignat-Lavaud, Cedric Fournet, Yogesh Deshpande, Steve Lasker
- **Date de publication :** `2026-06`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC9943`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-044.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9943.txt
- **Empreinte SHA-256 (LF) :** `1ed0ffb4007b7986d5d3ff4da1a0489d5b9d71c5eae4cd89a7f48ae650a19fef` (`65473` octets, `9449` mots)
- **Synthèse factuelle vérifiée :** RFC 9943 Standards Track (SCITT Architecture) spécifiant l'enregistrement transparent de déclarations signées dans un journal à append-only basé sur arbre de Merkle et reçu vérifiable.

### [21] SRC-018 — NIST FIPS 205: Stateless Hash-Based Digital Signature Standard (SLH-DSA)

- **Auteurs / Émetteur :** National Institute of Standards and Technology (NIST)
- **Date de publication :** `2024-08-13`
- **Organisme / Revue :** NIST Federal Information Processing Standards
- **Identifiant :** `NIST FIPS 205`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-018.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf
- **Empreinte SHA-256 (LF) :** `c27445a0f736858615b4625c234e30c8a222b2ea61cd5bfef18b7e45e53aad37` (`137225` octets, `21924` mots)
- **Synthèse factuelle vérifiée :** Norme FIPS 205 (SLH-DSA) du NIST normalisant les signatures post-quantiques sans état basées sur des arbres de hachage (variantes SHA2-128s/f), utilisée pour le scellement d'archives probatoires à long terme.

### [22] SRC-023 — FinOps Open Cost and Usage Specification (FOCUS) v1.4 — Spécification normative complète

- **Auteurs / Émetteur :** FinOps Foundation
- **Date de publication :** `2026-06-04`
- **Organisme / Revue :** Linux Foundation / FinOps Foundation (GitHub release v1.4)
- **Identifiant :** `FINOPS-FOCUS-1.4`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-023.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/releases/download/v1.4/FOCUS_spec-v1_4.pdf
- **Empreinte SHA-256 (LF) :** `67f651d7a5b0bd9103b5cffaa3617edaec6fb7f1aa9ebd2b7d3f122a422a5f5e` (`698569` octets, `92764` mots)
- **Synthèse factuelle vérifiée :** Spécification FinOps FOCUS v1.4 normalisant les colonnes de facturation et d'usage (BilledCost, EffectiveCost, ConsumedQuantity, ChargePeriodStart) et permettant les champs d'extension carbone/énergie (CAP-046).

### [23] SRC-010 — RFC 9334: Remote ATtestation procedureS (RATS) Architecture

- **Auteurs / Émetteur :** Henk Birkholz, Dave Thaler, Michael Richardson, Ned Smith, Wei Pan
- **Date de publication :** `2023-01`
- **Organisme / Revue :** IETF Informational RFC
- **Identifiant :** `RFC 9334`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-010.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9334.txt
- **Empreinte SHA-256 (LF) :** `9cf8aa2510befad61a50b4808a031e37e6ac1658b0d3efd7df940a07770325b1` (`102376` octets, `15421` mots)
- **Synthèse factuelle vérifiée :** Architecture RATS (Remote ATtestation procedureS) publiée en catégorie IETF Informational (et non Standards Track) définissant les rôles conceptuels Attester, Verifier et Relying Party sans imposer de format de fil unique.

### [24] SRC-053 — Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates (incl. Ballot SC-081v3)

- **Auteurs / Émetteur :** CA/Browser Forum Server Certificate Working Group
- **Date de publication :** `2026-10-04`
- **Organisme / Revue :** CA/Browser Forum
- **Identifiant :** `CABF-BR-SC081V3`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-053.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md
- **Empreinte SHA-256 (LF) :** `8d44ae9b57d6bc8b4bc90896c0edff9f2217d7e7468d3b19ac285454e31016c2` (`337172` octets, `47637` mots)
- **Synthèse factuelle vérifiée :** Exigences de base du CA/B Forum réduisant progressivement la durée maximale de validité des certificats TLS publics à 100 jours au 15 mars 2027 puis à 47 jours au 15 mars 2029.

### [25] SRC-063 — Loi modernisant des dispositions législatives en matière de protection des renseignements personnels (Loi 25 / LQ 2021, c. 25, art. 12.1)

- **Auteurs / Émetteur :** Assemblée nationale du Québec
- **Date de publication :** `2021-09-22`
- **Organisme / Revue :** Publications du Québec
- **Identifiant :** `LQ-2021-C25`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-063.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://www.publicationsduquebec.gouv.qc.ca/fileadmin/Fichiers_client/lois_et_reglements/LoisAnnuelles/fr/2021/2021C25F.PDF
- **Empreinte SHA-256 (LF) :** `829e67f777ca0645b5b51a2ec4d8ec94739232c5a33ef76b7944d2bb81b61d87` (`143588` octets, `21658` mots)
- **Synthèse factuelle vérifiée :** Loi québécoise LQ 2021, c. 25 (Loi 25) sanctionnée en texte intégral : article 12.1 en vigueur depuis le 22 septembre 2023 (décisions automatisées : information, explication, observation, révision humaine), ÉFVP, sanctions administratives jusqu'à 10 M\$ CA (2 %) et amendes pénales jusqu'à 25 M\$ CA (4 %).

### [26] SRC-077 — RFC 8785: JSON Canonicalization Scheme (JCS)

- **Auteurs / Émetteur :** Anders Rundgren, Bret Jordan, Samuel Erdtman
- **Date de publication :** `2020-06`
- **Organisme / Revue :** IETF RFC Editor (Independent Submission)
- **Identifiant :** `RFC8785`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-077.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8785.txt
- **Empreinte SHA-256 (LF) :** `be00e8aeddaf91fcf40b1c5ecaa33f2d627dac1e3c338e80a1eb0445e31af642` (`36840` octets, `5011` mots)
- **Synthèse factuelle vérifiée :** RFC 8785 (Independent Submission, statut Informational — JSON Canonicalization Scheme, JCS) fixant la canonisation déterministe (ordre UTF-16 des clés, formatage ECMAScript des nombres) préalable à tout hachage SHA-256.

---

## Exclusions documentaires et statut F (`AO-01`)

- `draft-ietf-oauth-transaction-tokens-11` (`SRC-013`), `draft-chen-oauth-agent-revocation-01` (`SRC-017`), `draft-ietf-wimse-*` (`SRC-047`, `SRC-048`) et `semantic-conventions-genai` (`SRC-090`) ne sont pas des RFC ou normes finales au 2 décembre 2026 et sont qualifiés explicitement comme tels.
- `RFC 9334` (`SRC-010`) relève de la catégorie `Informational`.
