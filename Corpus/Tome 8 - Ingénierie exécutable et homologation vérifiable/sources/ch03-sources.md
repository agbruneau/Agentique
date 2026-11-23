# Base documentaire fermée — Chapitre 3 — Politiques OPA/Rego hors modèle, CaMeL, confinement sans KVM et Sagas compensables

**Protocole :** `MLR-PRISMA-SCR-MANUEL-VOL8-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

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

### [2] SRC-059 — OWASP Agentic AI Top 10 Crosswalk (GitHub Pages miroir ouvert CC BY-SA 4.0)

- **Auteurs / Émetteur :** OWASP GenAI Security Project
- **Date de publication :** `2026`
- **Organisme / Revue :** OWASP GenAI Security Project (genai-security-project.github.io)
- **Identifiant :** `OWASP-AGENTIC-CROSSWALK`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-059.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://genai-security-project.github.io/crosswalk/agentic-ai-top10/
- **Empreinte SHA-256 (LF) :** `e5a50552cb527f49da00bcd4ea206348db3331b41c6f4fa2dd7e7dc5904cf17d` (`3616` octets, `506` mots)
- **Synthèse factuelle vérifiée :** Tableau de correspondance ouvert OWASP Agentic AI Top 10 Crosswalk reliant les catégories ASI01–ASI10 aux mécanismes de défense techniques vérifiables.

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

### [5] SRC-007 — Defeating Prompt Injections by Design (CaMeL)

- **Auteurs / Émetteur :** Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes et al.
- **Date de publication :** `2025-06-24`
- **Organisme / Revue :** arXiv (prépublication)
- **Identifiant :** `arXiv:2503.18813v2`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-007.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2503.18813
- **Empreinte SHA-256 (LF) :** `7a9735abcbdcbea1569be50b290f7e8198648a57f378a27bdb796e0f38cb3d2b` (`361916` octets, `50342` mots)
- **Synthèse factuelle vérifiée :** Architecture CaMeL (Capability-based ML Security) isolant le flux de contrôle fiable du flux de données non fiables ; résout 77 % des tâches AgentDojo avec garantie structurelle contre 84 % sans défense.

### [6] SRC-056 — Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks

- **Auteurs / Émetteur :** James Peters-Gill, Avi Semler, Henning Bartsch, Ilia Shumailov et al.
- **Date de publication :** `2026-10-05`
- **Organisme / Revue :** arXiv
- **Identifiant :** `arXiv:2610.05640`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-056.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2610.05640
- **Empreinte SHA-256 (LF) :** `490ff7dc6d6914d59acfb56fab33ebb48ae61dd5ef1bfd181cb69d04c68ee9f5` (`97586` octets, `14394` mots)
- **Synthèse factuelle vérifiée :** Étude Peters-Gill et al. (octobre 2026, Can CaMeLs Talk?) démontrant que les garanties CaMeL mono-agent ne se composent pas en multi-agents (0,2 % ASR résiduelle contre 12,9 % sans défense), sauf propagation stricte multi-CaMeL (0,0 % ASR).

### [7] SRC-002 — Design Patterns for Securing LLM Agents against Prompt Injections

- **Auteurs / Émetteur :** Luca Beurer-Kellner, Beat Buesser, Ana-Maria Creţu, Edoardo Debenedetti et al.
- **Date de publication :** `2025-06-27`
- **Organisme / Revue :** arXiv (IBM / ETH Zurich / EPFL / Google DeepMind)
- **Identifiant :** `arXiv:2506.08837v3`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-002.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2506.08837
- **Empreinte SHA-256 (LF) :** `b3e1ed3304dd7a8c4a96cc21c515d50b2b1ebf00c5764a4844179bdce76b72d1` (`80916` octets, `12285` mots)
- **Synthèse factuelle vérifiée :** Taxonomie de 6 patrons architecturaux de sécurisation contre l'injection indirecte (action-selector, plan-then-execute, map-reduce LLM, dual-LLM, code-then-execute, context-minimization) prouvant que la défense doit résider dans le graphe de contrôle hors du modèle.

### [8] SRC-003 — Towards a Science of Scaling Agent Systems

- **Auteurs / Émetteur :** Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park et al.
- **Date de publication :** `2025-12-09`
- **Organisme / Revue :** arXiv
- **Identifiant :** `arXiv:2512.08296`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-003.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2512.08296
- **Empreinte SHA-256 (LF) :** `991148d77ecdcd5a7ba19a0f6ce1ff3c5d8f54c8abea67debf7182a1296a559f` (`145288` octets, `18743` mots)
- **Synthèse factuelle vérifiée :** Étude empirique de mise à l'échelle des systèmes multi-agents démontrant qu'ajouter des agents dégrade la performance dès que la surcharge de coordination ou la séquentialité des outils excède les gains de parallélisme.

### [9] SRC-031 — Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

- **Auteurs / Émetteur :** Dat Tran, Douwe Kiela
- **Date de publication :** `2026-04-11`
- **Organisme / Revue :** arXiv
- **Identifiant :** `arXiv:2604.02460v2`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-031.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2604.02460
- **Empreinte SHA-256 (LF) :** `80b064f92eb145f5ff0977ee03fb95543bb95599007e69ded99c08927edac0e9` (`74996` octets, `11295` mots)
- **Synthèse factuelle vérifiée :** Analyse empirique montrant que des agents uniques bien outillés surpassent souvent les architectures multi-agents sur le raisonnement multi-sauts lorsque le protocole inter-agents fragmente le contexte.

### [10] SRC-032 — The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size

- **Auteurs / Émetteur :** Blaž Bertalanič, Carolina Fortuna
- **Date de publication :** `2026-05-31`
- **Organisme / Revue :** arXiv
- **Identifiant :** `arXiv:2606.02646`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-032.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2606.02646
- **Empreinte SHA-256 (LF) :** `dd138f578d07f36f25b962fc8a5c346c1461587184ab85121087e8731feaee72` (`135378` octets, `20794` mots)
- **Synthèse factuelle vérifiée :** Étude mettant en évidence l'effet Ringelmann dans les essaims d'agents LLM : dilution de la contribution utile et dérive de coordination à mesure que la taille du groupe augmente.

### [11] SRC-033 — Sagas

- **Auteurs / Émetteur :** Hector Garcia-Molina, Kenneth Salem
- **Date de publication :** `1987-05`
- **Organisme / Revue :** ACM SIGMOD 1987 (Princeton Dept. CS OA)
- **Identifiant :** `ACM-SIGMOD-1987-SAGAS`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-033.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf
- **Empreinte SHA-256 (LF) :** `61c64fc7900604a34fcae13f7907df581d97c48ff19ec0d7db579a3bd1bd332e` (`46158` octets, `7817` mots)
- **Synthèse factuelle vérifiée :** Article fondateur de Garcia-Molina et Salem (1987) formalisant les Sagas à transactions atomiques et actions compensatrices jusqu'au point de non-retour (point pivot).

### [12] SRC-006 — SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning

- **Auteurs / Émetteur :** Edward Y. Chang, Longling Geng
- **Date de publication :** `2025-07-09`
- **Organisme / Revue :** arXiv (prépublication, gabarit PVLDB)
- **Identifiant :** `arXiv:2503.11951v3`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-006.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2503.11951
- **Empreinte SHA-256 (LF) :** `c2565e8391cc57e98ad4c7f26cac6b52dd76360de5a461152d2a94765e64e694` (`73051` octets, `9679` mots)
- **Synthèse factuelle vérifiée :** Cadre SagaLLM combinant gestion contextuelle par points de contrôle, validation indépendante de contraintes et exécution transactionnelle compensable pour empêcher les dérives d'état multi-étapes.

### [13] SRC-034 — Temporal SDKs — Durable Execution, Event History and Deterministic Replay

- **Auteurs / Émetteur :** Temporal Technologies
- **Date de publication :** `2026`
- **Organisme / Revue :** Temporal Documentation
- **Identifiant :** `TEMPORAL-SDKS-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-034.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://docs.temporal.io/encyclopedia/temporal-sdks
- **Empreinte SHA-256 (LF) :** `95aa625eecff574cd1e55188823cb0b0e10a7c36a2f78b415913ca3bf1fcf35b` (`15387` octets, `2327` mots)
- **Synthèse factuelle vérifiée :** Documentation technique Temporal SDKs décrivant l'exécution durable basée sur l'historique d'événements rejouable de façon déterministe, la gestion des délais et les signaux humains.

### [14] SRC-035 — CloudEvents Specification — Version 1.0.2

- **Auteurs / Émetteur :** CNCF Serverless Working Group
- **Date de publication :** `2022-04`
- **Organisme / Revue :** Cloud Native Computing Foundation (CNCF)
- **Identifiant :** `CLOUDEVENTS-1.0.2`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-035.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/cloudevents/spec/v1.0.2/cloudevents/spec.md
- **Empreinte SHA-256 (LF) :** `8f4d59dd27f8807741321b3145c5c9c2f22bba5bf9a9299b0c2020d769dc92ae` (`25147` octets, `3651` mots)
- **Synthèse factuelle vérifiée :** Spécification CloudEvents v1.0.2 normalisant l'enveloppe de métadonnées événementielles (id, source, type, datacontenttype) et la corrélation inter-services.

### [15] SRC-036 — The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header)

- **Auteurs / Émetteur :** Jayadeba Jena, Sanjay Dalal, Dmitrii Tishkin
- **Date de publication :** `2026-11-21`
- **Organisme / Revue :** IETF Datatracker
- **Identifiant :** `IETF-DRAFT-IDEMPOTENCY-KEY-09`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-036.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
- **Empreinte SHA-256 (LF) :** `d737453f458f71e135b6bee31e4bdda076f6bca90f264add649fd738b75714cb` (`24607` octets, `3668` mots)
- **Synthèse factuelle vérifiée :** Brouillon IETF HTTPAPI (draft-ietf-httpapi-idempotency-key-header-09) spécifiant l'en-tête Idempotency-Key et les rejets HTTP 409 (requête en cours) et 422 (réutilisation avec charge différente).

### [16] SRC-054 — NIST AI 100-2e2025: Adversarial Machine Learning — A Taxonomy and Terminology of Attacks and Mitigations

- **Auteurs / Émetteur :** Alina Oprea, Apostol Vassilev et al. (NIST)
- **Date de publication :** `2025-03-20`
- **Organisme / Revue :** NIST
- **Identifiant :** `NIST-AI-100-2E2025`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-054.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf
- **Empreinte SHA-256 (LF) :** `1f113bf38b90261c6372c5b9a8d77a4355c7e4fa0ccf11b4d179930a9a0dfa7f` (`347771` octets, `48743` mots)
- **Synthèse factuelle vérifiée :** Publication NIST AI 100-2e2025 classifiant les attaques adverses en apprentissage automatique et systèmes LLM (évasion, empoisonnement, extraction) et leurs mesures d'atténuation.

---

## Exclusions documentaires et statut F (`AO-01`)

- `https://genai.owasp.org/` (`HTTP 403`) — compensé par l'archive officielle CC BY-SA 4.0 `SRC-055` et le Crosswalk ouvert `SRC-059`.
- `draft-ietf-httpapi-idempotency-key-header-09` (`SRC-036`) est un brouillon IETF en cours de normalisation.
