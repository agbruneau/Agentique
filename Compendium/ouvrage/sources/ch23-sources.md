# Base documentaire fermée — Chapitre 23 — Banc EvalOps hermétique (E1–E3), bornes de Wilson, tests métamorphiques FR/EN et distillation contrôlée

**Protocole :** `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0,0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

---

### [1] SRC-022 — NIST/SEMATECH e-Handbook of Statistical Methods — Section 7.2.4.1 Confidence Intervals for a Binomial Proportion (Wilson / Exact)

- **Auteurs / Émetteur :** NIST / SEMATECH
- **Date de publication :** `2012-04`
- **Organisme / Revue :** NIST Engineering Statistics Handbook
- **Identifiant :** `NIST-HANDBOOK-7.2.4.1`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-022.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
- **Empreinte SHA-256 (LF) :** `7cd7f651da8a13015902f782f324ad3d2a038446bb9079e6e99f294e32d1442a` (`10050` octets, `1406` mots)
- **Synthèse factuelle vérifiée :** Section 7.2.4.1 du manuel statistique NIST/SEMATECH formulant l'intervalle de confiance de Wilson et d'Agresti-Coull pour une proportion binomiale, socle du dimensionnement à zéro échec.

### [2] SRC-094 — Binomial confidence intervals for rare events: importance of defining margin of error relative to magnitude of proportion

- **Auteurs / Émetteur :** Owen McGrath, Kevin Burke
- **Date de publication :** `2024-01-15`
- **Organisme / Revue :** arXiv (University of Limerick)
- **Identifiant :** `arXiv:2109.02516`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-094.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2109.02516
- **Empreinte SHA-256 (LF) :** `5389504543994bb1ff65414eb1edcf4ccda10b0d880e50ece38618bd82346151` (`70404` octets, `12083` mots)
- **Synthèse factuelle vérifiée :** Analyse statistique de McGrath et Burke (arXiv:2109.02516) comparant les estimateurs de Wilson, Clopper-Pearson, Wald et Agresti-Coull pour les probabilités d'événements rares et leur marge d'erreur relative.

### [3] SRC-029 — τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

- **Auteurs / Émetteur :** Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan
- **Date de publication :** `2024-06-17`
- **Organisme / Revue :** arXiv (Princeton)
- **Identifiant :** `arXiv:2406.12045`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-029.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://arxiv.org/pdf/2406.12045
- **Empreinte SHA-256 (LF) :** `659469b4a86d64eab21b613c1754164de732af170d5954a26ac7a69d06cab7d9` (`130060` octets, `17795` mots)
- **Synthèse factuelle vérifiée :** Banc d'essai tau-bench (Yao et al., 2024) introduisant la métrique de constance pass^k (réussite sur k exécutions répétées indépendantes) plutôt que pass@k pour mesurer la fiabilité en entreprise.

### [4] SRC-030 — Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation (HAL)

- **Auteurs / Émetteur :** Sayash Kapoor, Benedikt Stroebl, Peter Kirgis, Nitya Nadgir et al.
- **Date de publication :** `2025-10-13`
- **Organisme / Revue :** arXiv (Princeton)
- **Identifiant :** `arXiv:2510.11977`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-030.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://arxiv.org/pdf/2510.11977
- **Empreinte SHA-256 (LF) :** `4f1e326b6b314f5856566ce21a588bd934508fc767159859376315a94fcb2dfd` (`173603` octets, `25986` mots)
- **Synthèse factuelle vérifiée :** Holistic Agent Leaderboard (Kapoor et al., 2025) mettant en évidence l'impact du coût d'inférence, de la reproductibilité et du harnais d'évaluation sur les scores comparatifs des agents.

### [5] SRC-091 — Testing Chatbots Using Metamorphic Relations

- **Auteurs / Émetteur :** Josip Bozic, Franz Wotawa
- **Date de publication :** `2020-03-31`
- **Organisme / Revue :** 31th IFIP ICTSS / HAL Id hal-02526355v1
- **Identifiant :** `hal-02526355`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-091.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://inria.hal.science/hal-02526355v1/document
- **Empreinte SHA-256 (LF) :** `069cee64fd680ec43c71269994ed3945bc99f8e0bd4d9b737d1917a26e8ba39d` (`42745` octets, `6801` mots)
- **Synthèse factuelle vérifiée :** Article de Bozic et Wotawa (ICTSS / hal-02526355v1) appliquant les relations métamorphiques (citées depuis Chen et al. 2018) au test de systèmes conversationnels sans oracle explicite.
- **Audit d'accès réseau (`2026-11-25`) :** Sondage direct filtré par défi Proof-of-Work Anubis sur HAL (non contourné selon `AO-01`). Texte intégral CC BY 4.0 archivé avant filtrage et vérifié par empreinte `SHA-256` locale (`069cee64fd680ec43c71269994ed3945bc99f8e0bd4d9b737d1917a26e8ba39d`) ; notice HAL canonique `https://inria.hal.science/hal-02526355v1` et DOI éditeur IFIP ICTSS 2019 : `https://doi.org/10.1007/978-3-030-31280-0_3`.

### [6] SRC-092 — MORTAR: Multi-turn Metamorphic Testing for LLM-based Dialogue Systems

- **Auteurs / Émetteur :** Aaron Guoxiang Guo, Aldeida Aleti, Neelofar Neelofar, Chakkrit Tantithamthavorn, Yuanyuan Qi, Tsong Yueh Chen
- **Date de publication :** `2024-12-20`
- **Organisme / Revue :** arXiv
- **Identifiant :** `arXiv:2412.15557`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-092.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2412.15557
- **Empreinte SHA-256 (LF) :** `0e9939c49f50f444cac355418f0db09d566aef8d16f240d7c65a6a9efbe8acc8` (`112972` octets, `17197` mots)
- **Synthèse factuelle vérifiée :** Cadre MORTAR (Guo, Aleti, Chen et al., arXiv:2412.15557) étendant le test métamorphique aux dialogues LLM multi-tours par perturbations d'entrées préservant l'invariance relationnelle sans oracle.

### [7] SRC-093 — Explanation-Guided Metamorphic Testing of Specialized Language Models: An Empirical Study

- **Auteurs / Émetteur :** Xingcheng Chen, Mehmet Besenk, Andrea Stocco
- **Date de publication :** `2026-08-07`
- **Organisme / Revue :** arXiv (TU Munich / fortiss)
- **Identifiant :** `arXiv:2608.07076`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-093.txt`, score AACODS `10.0/12`)
- **URL d'origine :** https://arxiv.org/pdf/2608.07076
- **Empreinte SHA-256 (LF) :** `619e05baae21e839f905977dba7044e689b91a4678be105edc031a6307593af2` (`71983` octets, `9506` mots)
- **Synthèse factuelle vérifiée :** Étude empirique récente (août 2026, arXiv:2608.07076) combinant tests métamorphiques et signaux d'explication pour détecter les défaillances silencieuses de modèles spécialisés sans oracle.

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

- `https://dl.acm.org/doi/10.1145/3143561` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 / mur payant ACM Digital Library (1 tentative AO-01) ; compensé en L+ par Bozic & Wotawa (hal-02526355, SRC-091), MORTAR co-signé par T.Y. Chen (arXiv:2412.15557, SRC-092) et Chen et al. (arXiv:2608.07076, SRC-093).
- `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/` — `HTTP_403` (`included_in_evidence: false`). HTTP 403 sur genai.owasp.org; compensé intégralement par le PDF officiel CC BY-SA 4.0 v1.0 archivé sur github.com/genai-security-project/GenAI-Security-Corpus (SRC-055, L+).
