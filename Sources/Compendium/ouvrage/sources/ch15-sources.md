# Base documentaire fermée — Chapitre 15 — Automatisation durable hors processus, idempotence JCS inter-systèmes et sagas compensables à canal isolé

**Protocole :** `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0,0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

---

### [1] SRC-033 — Sagas

- **Auteurs / Émetteur :** Hector Garcia-Molina, Kenneth Salem
- **Date de publication :** `1987-05`
- **Organisme / Revue :** ACM SIGMOD 1987 (Princeton Dept. CS OA)
- **Identifiant :** `ACM-SIGMOD-1987-SAGAS`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-033.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf
- **Empreinte SHA-256 (LF) :** `61c64fc7900604a34fcae13f7907df581d97c48ff19ec0d7db579a3bd1bd332e` (`46158` octets, `7817` mots)
- **Synthèse factuelle vérifiée :** Article fondateur de Garcia-Molina et Salem (1987) formalisant les Sagas à transactions atomiques et actions compensatrices jusqu'au point de non-retour (point pivot).

### [2] SRC-034 — Temporal SDKs — Durable Execution, Event History and Deterministic Replay

- **Auteurs / Émetteur :** Temporal Technologies
- **Date de publication :** `2026`
- **Organisme / Revue :** Temporal Documentation
- **Identifiant :** `TEMPORAL-SDKS-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-034.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://docs.temporal.io/encyclopedia/architecture/temporal-sdks
- **Empreinte SHA-256 (LF) :** `95aa625eecff574cd1e55188823cb0b0e10a7c36a2f78b415913ca3bf1fcf35b` (`15387` octets, `2327` mots)
- **Synthèse factuelle vérifiée :** Documentation technique Temporal SDKs décrivant l'exécution durable basée sur l'historique d'événements rejouable de façon déterministe, la gestion des délais et les signaux humains.

### [3] SRC-006 — SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning

- **Auteurs / Émetteur :** Edward Y. Chang, Longling Geng
- **Date de publication :** `2025-07-09`
- **Organisme / Revue :** arXiv (prépublication, gabarit PVLDB)
- **Identifiant :** `arXiv:2503.11951v3`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-006.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2503.11951
- **Empreinte SHA-256 (LF) :** `c2565e8391cc57e98ad4c7f26cac6b52dd76360de5a461152d2a94765e64e694` (`73051` octets, `9679` mots)
- **Synthèse factuelle vérifiée :** Cadre SagaLLM combinant gestion contextuelle par points de contrôle, validation indépendante de contraintes et exécution transactionnelle compensable pour empêcher les dérives d'état multi-étapes.

### [4] SRC-036 — The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header)

- **Auteurs / Émetteur :** Jayadeba Jena, Sanjay Dalal, Dmitrii Tishkin
- **Date de publication :** `2026-11-21`
- **Organisme / Revue :** IETF Datatracker
- **Identifiant :** `IETF-DRAFT-IDEMPOTENCY-KEY-09`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-036.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
- **Empreinte SHA-256 (LF) :** `d737453f458f71e135b6bee31e4bdda076f6bca90f264add649fd738b75714cb` (`24607` octets, `3668` mots)
- **Synthèse factuelle vérifiée :** Brouillon IETF HTTPAPI (draft-ietf-httpapi-idempotency-key-header-09) spécifiant l'en-tête Idempotency-Key et les rejets HTTP 409 (requête en cours) et 422 (réutilisation avec charge différente).

### [5] SRC-077 — RFC 8785: JSON Canonicalization Scheme (JCS)

- **Auteurs / Émetteur :** Anders Rundgren, Bret Jordan, Samuel Erdtman
- **Date de publication :** `2020-06`
- **Organisme / Revue :** IETF RFC Editor (Independent Submission)
- **Identifiant :** `RFC 8785`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-077.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc8785.txt
- **Empreinte SHA-256 (LF) :** `be00e8aeddaf91fcf40b1c5ecaa33f2d627dac1e3c338e80a1eb0445e31af642` (`36840` octets, `5011` mots)
- **Synthèse factuelle vérifiée :** RFC 8785 (Independent Submission, statut Informational — JSON Canonicalization Scheme, JCS) fixant la canonisation déterministe (ordre UTF-16 des clés, formatage ECMAScript des nombres) préalable à tout hachage SHA-256.

### [6] SRC-132 — RFC 9562: Universally Unique IDentifiers (UUIDs)

- **Auteurs / Émetteur :** Kyzer Davis, Brad Peabody, Pierre Leach
- **Date de publication :** `2024-05`
- **Organisme / Revue :** IETF RFC Editor
- **Identifiant :** `RFC 9562`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-132.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.rfc-editor.org/rfc/rfc9562.txt
- **Empreinte SHA-256 (LF) :** `a3d609ca981cd5c9f4bf0acf6a8a3a446ed79f5cc4c0ae2d9287349feaab70c1` (`99366` octets, `14594` mots)
- **Synthèse factuelle vérifiée :** Standard IETF RFC 9562 (Davis, Peabody et Leach, mai 2024) définissant les formats UUID modernes dont UUIDv7 ordonné chronologiquement pour la corrélation distribuée.

---

## Exclusions en statut F (`AO-01` — hors preuve)

- `https://dl.acm.org/doi/10.1145/3143561` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 / mur payant ACM Digital Library (1 tentative AO-01) ; compensé en L+ par Bozic & Wotawa (hal-02526355, SRC-091), MORTAR co-signé par T.Y. Chen (arXiv:2412.15557, SRC-092) et Chen et al. (arXiv:2608.07076, SRC-093).
