# Base documentaire fermée — Chapitre 4 — EvalOps hermétiques, Wilson >= 3/p, tests métamorphiques, PRR 24 et conformité

**Protocole :** `MLR-PRISMA-SCR-MANUEL-VOL8-2027-V1.0` (`AO-01` / `AO-02` stricts)
**Date de gel :** 2 décembre 2026 (`2026-12-02`)
**Portée :** Sources primaires intégrales vérifiées en statut `L+` (`0 % METADATA_ONLY`) — clause `non-avis` (`AO-05`) applicable aux sections juridiques et réglementaires.

---

### [1] SRC-029 — τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

- **Auteurs / Émetteur :** Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan
- **Date de publication :** `2024-06-17`
- **Organisme / Revue :** arXiv (Princeton)
- **Identifiant :** `arXiv:2406.12045`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-029.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://arxiv.org/pdf/2406.12045
- **Empreinte SHA-256 (LF) :** `659469b4a86d64eab21b613c1754164de732af170d5954a26ac7a69d06cab7d9` (`130060` octets, `17795` mots)
- **Synthèse factuelle vérifiée :** Banc d'essai tau-bench (Yao et al., 2024) introduisant la métrique de constance pass^k (réussite sur k exécutions répétées indépendantes) plutôt que pass@k pour mesurer la fiabilité en entreprise.

### [2] SRC-022 — NIST/SEMATECH e-Handbook of Statistical Methods — Section 7.2.4.1 Confidence Intervals for a Binomial Proportion (Wilson / Exact)

- **Auteurs / Émetteur :** NIST / SEMATECH
- **Date de publication :** `2012-04`
- **Organisme / Revue :** NIST Engineering Statistics Handbook
- **Identifiant :** `NIST-HANDBOOK-7.2.4.1`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-022.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
- **Empreinte SHA-256 (LF) :** `7cd7f651da8a13015902f782f324ad3d2a038446bb9079e6e99f294e32d1442a` (`10050` octets, `1406` mots)
- **Synthèse factuelle vérifiée :** Section 7.2.4.1 du manuel statistique NIST/SEMATECH formulant l'intervalle de confiance de Wilson et d'Agresti-Coull pour une proportion binomiale, socle du dimensionnement à zéro échec.

### [3] SRC-094 — Binomial confidence intervals for rare events: importance of defining margin of error relative to magnitude of proportion

- **Auteurs / Émetteur :** Owen McGrath, Kevin Burke
- **Date de publication :** `2024-01-15`
- **Organisme / Revue :** arXiv (University of Limerick)
- **Identifiant :** `arXiv:2109.02516`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-094.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2109.02516
- **Empreinte SHA-256 (LF) :** `5389504543994bb1ff65414eb1edcf4ccda10b0d880e50ece38618bd82346151` (`70404` octets, `12083` mots)
- **Synthèse factuelle vérifiée :** Analyse statistique de McGrath et Burke (arXiv:2109.02516) comparant les estimateurs de Wilson, Clopper-Pearson, Wald et Agresti-Coull pour les probabilités d'événements rares et leur marge d'erreur relative.

### [4] SRC-091 — Testing Chatbots Using Metamorphic Relations

- **Auteurs / Émetteur :** Josip Bozic, Franz Wotawa
- **Date de publication :** `2020-03-31`
- **Organisme / Revue :** 31th IFIP ICTSS / HAL Id hal-02526355v1
- **Identifiant :** `hal-02526355`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-091.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://inria.hal.science/hal-02526355v1/document
- **Empreinte SHA-256 (LF) :** `069cee64fd680ec43c71269994ed3945bc99f8e0bd4d9b737d1917a26e8ba39d` (`42745` octets, `6801` mots)
- **Synthèse factuelle vérifiée :** Article de Bozic et Wotawa (ICTSS / hal-02526355v1) appliquant les relations métamorphiques (citées depuis Chen et al. 2018) au test de systèmes conversationnels sans oracle explicite.

### [5] SRC-092 — MORTAR: Multi-turn Metamorphic Testing for LLM-based Dialogue Systems

- **Auteurs / Émetteur :** Aaron Guoxiang Guo, Aldeida Aleti, Neelofar Neelofar, Chakkrit Tantithamthavorn, Yuanyuan Qi, Tsong Yueh Chen
- **Date de publication :** `2024-12-20`
- **Organisme / Revue :** arXiv
- **Identifiant :** `arXiv:2412.15557`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-092.txt`, score AACODS `10.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2412.15557
- **Empreinte SHA-256 (LF) :** `0e9939c49f50f444cac355418f0db09d566aef8d16f240d7c65a6a9efbe8acc8` (`112972` octets, `17197` mots)
- **Synthèse factuelle vérifiée :** Cadre MORTAR (Guo, Aleti, Chen et al., arXiv:2412.15557) étendant le test métamorphique aux dialogues LLM multi-tours par perturbations d'entrées préservant l'invariance relationnelle sans oracle.

### [6] SRC-093 — Explanation-Guided Metamorphic Testing of Specialized Language Models: An Empirical Study

- **Auteurs / Émetteur :** Xingcheng Chen, Mehmet Besenk, Andrea Stocco
- **Date de publication :** `2026-08-07`
- **Organisme / Revue :** arXiv (TU Munich / fortiss)
- **Identifiant :** `arXiv:2608.07076`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-093.txt`, score AACODS `10.0/12`)
- **URL d'origine :** https://arxiv.org/pdf/2608.07076
- **Empreinte SHA-256 (LF) :** `619e05baae21e839f905977dba7044e689b91a4678be105edc031a6307593af2` (`71983` octets, `9506` mots)
- **Synthèse factuelle vérifiée :** Étude empirique récente (août 2026, arXiv:2608.07076) combinant tests métamorphiques et signaux d'explication pour détecter les défaillances silencieuses de modèles spécialisés sans oracle.

### [7] SRC-028 — Why Do Multi-Agent LLM Systems Fail? (MAST)

- **Auteurs / Émetteur :** Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal et al.
- **Date de publication :** `2025-10-26`
- **Organisme / Revue :** NeurIPS 2025 / arXiv
- **Identifiant :** `arXiv:2503.13657v3`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-028.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://arxiv.org/pdf/2503.13657
- **Empreinte SHA-256 (LF) :** `7eeb1c6dfd098f1f6507ab979bdae4a7a2eacc1888efc0d599aca663f6577933` (`136729` octets, `19765` mots)
- **Synthèse factuelle vérifiée :** Taxonomie MAST (Cemri et al., 2025) analysant 1 642 traces de systèmes multi-agents sur 7 cadriciels et 14 modes de défaillance, avec des taux d'échec compris entre 41 % et 86,7 %.

### [8] SRC-030 — Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation (HAL)

- **Auteurs / Émetteur :** Sayash Kapoor, Benedikt Stroebl, Peter Kirgis, Nitya Nadgir et al.
- **Date de publication :** `2025-10-13`
- **Organisme / Revue :** arXiv (Princeton)
- **Identifiant :** `arXiv:2510.11977`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-030.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://arxiv.org/pdf/2510.11977
- **Empreinte SHA-256 (LF) :** `4f1e326b6b314f5856566ce21a588bd934508fc767159859376315a94fcb2dfd` (`173603` octets, `25986` mots)
- **Synthèse factuelle vérifiée :** Holistic Agent Leaderboard (Kapoor et al., 2025) mettant en évidence l'impact du coût d'inférence, de la reproductibilité et du harnais d'évaluation sur les scores comparatifs des agents.

### [9] SRC-011 — Agentic AI orchestration: TMT Predictions 2026

- **Auteurs / Émetteur :** Deloitte Insights
- **Date de publication :** `2025-11-18`
- **Organisme / Revue :** Deloitte Center for Technology, Media & Telecommunications
- **Identifiant :** `DELOITTE-TMT-2026-AGENTS`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-011.txt`, score AACODS `9.5/12`)
- **URL d'origine :** https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/ai-agent-orchestration.html
- **Empreinte SHA-256 (LF) :** `e7d41d25e64a998140f9d6510c553c62821273c598d9de5f92be40839362271b` (`39392` octets, `5425` mots)
- **Synthèse factuelle vérifiée :** Rapport TMT Predictions 2026 documentant la hausse de l'adoption de l'orchestration agentique et citant l'estimation Gartner selon laquelle plus de 40 % des projets agentiques risquent l'abandon d'ici fin 2027 faute de ROI et de gouvernance (communiqué primaire Gartner consigné en statut F).

### [10] SRC-040 — From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI

- **Auteurs / Émetteur :** Margaret-Anne Storey
- **Date de publication :** `2026-03-23`
- **Organisme / Revue :** arXiv (University of Victoria)
- **Identifiant :** `arXiv:2603.22106`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-040.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://arxiv.org/pdf/2603.22106
- **Empreinte SHA-256 (LF) :** `ea4b2e2a02be74d9ea58c479f65fd32ca0dd95a60fab65538792e41a844dd052` (`32784` octets, `4902` mots)
- **Synthèse factuelle vérifiée :** Article de M.-A. Storey et coll. (2026) conceptualisant la dette cognitive et d'intention lorsque des systèmes générés ou orchestrés par IA perdent leur traçabilité humaine.

### [11] SRC-051 — NIST IR 8547: Transition to Post-Quantum Cryptography Standards (Final, October 2026)

- **Auteurs / Émetteur :** Dustin Moody, Ray Perlner, Andrew Regenscheid, Angela Robinson, David Cooper
- **Date de publication :** `2026-10-21`
- **Organisme / Revue :** NIST (NIST IR 8547 Final)
- **Identifiant :** `NIST-IR-8547`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-051.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf
- **Empreinte SHA-256 (LF) :** `80e6a458907c3d2e5829db8eef5b8efbbb89a25b2dbe1153bcc7129a1a4a2599` (`78365` octets, `10327` mots)
- **Synthèse factuelle vérifiée :** Rapport NIST IR 8547 (octobre 2026) fixant la trajectoire de dépréciation de la cryptographie asymétrique classique (RSA/ECC) et de transition PQC vers l'horizon 2030–2035.

### [12] SRC-052 — Advancing a Coordinated Roadmap for the Transition to Post-Quantum Cryptography in the Financial Sector

- **Auteurs / Émetteur :** G7 Cyber Expert Group (CEG)
- **Date de publication :** `2026-01-14`
- **Organisme / Revue :** G7 Cyber Expert Group / UK HM Treasury & Bank of England
- **Identifiant :** `G7-CEG-PQC-ROADMAP-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-052.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://assets.publishing.service.gov.uk/media/6966149d8d599f4c09e1ffab/G7-CEG-Quantum-Roadmap.pdf
- **Empreinte SHA-256 (LF) :** `cab48e350b2941891ec38ed7545d2b276b5815804d690187650c232424c945e3` (`16420` octets, `2175` mots)
- **Synthèse factuelle vérifiée :** Feuille de route du G7 Cyber Expert Group (janvier 2026) coordonnant la migration post-quantique du secteur financier sur l'horizon 2030–2035.

### [13] SRC-055 — OWASP Top 10 for Agentic Applications 2026 (v1.0, December 2025 — document complet CC BY-SA 4.0)

- **Auteurs / Émetteur :** OWASP GenAI Security Project
- **Date de publication :** `2025-12`
- **Organisme / Revue :** OWASP GenAI Security Project (Agentic Security Initiative — GenAI-Security-Corpus)
- **Identifiant :** `OWASP-AGENTIC-TOP10-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-055.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://raw.githubusercontent.com/genai-security-project/GenAI-Security-Corpus/main/corpus/agentic-top10/2026-final/OWASP-Top-10-for-Agentic-Applications-2026-v1.0.pdf
- **Empreinte SHA-256 (LF) :** `4d9f1c9f067fc284f01e8a904b172bbaceb97dd5a259a4d73c7d80f1482c22f3` (`100680` octets, `13820` mots)
- **Synthèse factuelle vérifiée :** Référentiel OWASP Top 10 for Agentic Applications 2026 (v1.0, CC BY-SA 4.0) recensant ASI01 à ASI10 avec mention explicite non-avis juridique (document primaire en statut L+ hors genai.owasp.org).

### [14] SRC-058 — STAMP/STPA Informed Characterization of Factors Leading to Loss of Control in AI Systems

- **Auteurs / Émetteur :** Steve Barrett, Anna Bruvere, Sean P. Fillingham, Catherine Rhodes, Stefano Vergani
- **Date de publication :** `2026-02-03`
- **Organisme / Revue :** arXiv (Centre for the Study of Existential Risk)
- **Identifiant :** `arXiv:2512.17600v2`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-058.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://arxiv.org/pdf/2512.17600
- **Empreinte SHA-256 (LF) :** `78b03417f4de11b0132a9afce95e493bec8b9028715ec9b9139aa504d4599ecb` (`112088` octets, `17212` mots)
- **Synthèse factuelle vérifiée :** Application de l'analyse systémique STAMP/STPA aux agents autonomes pour modéliser les pertes de contrôle dans les boucles de rétroaction sociotechniques.

### [15] SRC-060 — Règlement (UE) 2024/1689 (EU AI Act)

- **Auteurs / Émetteur :** Parlement européen et Conseil de l'Union européenne
- **Date de publication :** `2024-07-12`
- **Organisme / Revue :** Journal officiel de l'Union européenne
- **Identifiant :** `CELEX:32024R1689`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-060.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0009.01/DOC_1
- **Empreinte SHA-256 (LF) :** `e0a79e4f278c88177206c60458fad1f06c74fc80d6b23e404ef523c290346477` (`711317` octets, `102754` mots)
- **Synthèse factuelle vérifiée :** Règlement (UE) 2024/1689 (EU AI Act) publié au JOUE fixant les obligations de transparence (art. 50), de gouvernance humaine (art. 14), de QMS (art. 17) et le calendrier d'application (art. 113).

### [16] SRC-061 — Règlement (UE) 2026/1744 du 8 juillet 2026 modifiant le règlement (UE) 2024/1689 (simplification / échéances IA)

- **Auteurs / Émetteur :** Parlement européen et Conseil de l'Union européenne
- **Date de publication :** `2026-07-24`
- **Organisme / Revue :** Journal officiel de l'Union européenne (JO L 24.7.2026)
- **Identifiant :** `CELEX:32026R1744`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-061.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0009.01/DOC_1
- **Empreinte SHA-256 (LF) :** `cafaf35193ed2bdb4c97f5219deef5a6c9310aa5ceae48484d36485b3211d712` (`175654` octets, `26235` mots)
- **Synthèse factuelle vérifiée :** Règlement (UE) 2026/1744 modifiant le règlement (UE) 2024/1689, ajustant les délais transitoires (art. 111) et fixant au plus tard au 2 décembre 2027 l'application de l'Annexe III.

### [17] SRC-062 — Règlement (UE) 2022/2554 sur la résilience opérationnelle numérique du secteur financier (DORA)

- **Auteurs / Émetteur :** Parlement européen et Conseil de l'Union européenne
- **Date de publication :** `2022-12-27`
- **Organisme / Revue :** Journal officiel de l'Union européenne
- **Identifiant :** `CELEX:32022R2554`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-062.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://publications.europa.eu/resource/cellar/0caf473a-85bd-11ed-9887-01aa75ed71a1.0009.01/DOC_1
- **Empreinte SHA-256 (LF) :** `6e4b138de7f05c440c3b1c3b590545dc0cd3f1c793e4c12c733f8736a2ecfb9e` (`364364` octets, `52268` mots)
- **Synthèse factuelle vérifiée :** Règlement (UE) 2022/2554 (DORA) imposant au secteur financier européen la gestion des risques TIC, les tests de résilience opérationnelle et l'encadrement des prestataires tiers critiques.

### [18] SRC-063 — Loi modernisant des dispositions législatives en matière de protection des renseignements personnels (Loi 25 / LQ 2021, c. 25, art. 12.1)

- **Auteurs / Émetteur :** Assemblée nationale du Québec
- **Date de publication :** `2021-09-22`
- **Organisme / Revue :** Publications du Québec
- **Identifiant :** `LQ-2021-C25`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-063.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://www.publicationsduquebec.gouv.qc.ca/fileadmin/Fichiers_client/lois_et_reglements/LoisAnnuelles/fr/2021/2021C25F.PDF
- **Empreinte SHA-256 (LF) :** `829e67f777ca0645b5b51a2ec4d8ec94739232c5a33ef76b7944d2bb81b61d87` (`143588` octets, `21658` mots)
- **Synthèse factuelle vérifiée :** Loi québécoise LQ 2021, c. 25 (Loi 25) sanctionnée en texte intégral : article 12.1 en vigueur depuis le 22 septembre 2023 (décisions automatisées : information, explication, observation, révision humaine), ÉFVP, sanctions administratives jusqu'à 10 M\$ CA (2 %) et amendes pénales jusqu'à 25 M\$ CA (4 %).

### [19] SRC-064 — Rapport quinquennal 2026 sur l'application de la Loi sur la protection des renseignements personnels dans le secteur privé

- **Auteurs / Émetteur :** Commission d'accès à l'information du Québec (CAI)
- **Date de publication :** `2026-05`
- **Organisme / Revue :** Commission d'accès à l'information du Québec
- **Identifiant :** `CAI-RQ-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-064.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://www.cai.gouv.qc.ca/uploads/pdfs/CAI_RQ_2026.pdf
- **Empreinte SHA-256 (LF) :** `db8153ade9d57151bd7427e5ed3c4157447efdc17a4d35d8727427edd7589e7c` (`1206095` octets, `167678` mots)
- **Synthèse factuelle vérifiée :** Rapport quinquennal 2026 de la Commission d'accès à l'information (CAI) dressant le bilan d'application de la Loi sur le secteur privé modernisée et de l'article 12.1.

### [20] SRC-065 — Ligne directrice E-23 — Gestion du risque de modélisation à l'échelle de l'entreprise (édition 2027)

- **Auteurs / Émetteur :** Bureau du surintendant des institutions financières (BSIF / OSFI)
- **Date de publication :** `2025-09-11`
- **Organisme / Revue :** BSIF Canada
- **Identifiant :** `BSIF-E23-2027`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-065.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://www.osfi-bsif.gc.ca/fr/consignes/repertoire-consignes/ligne-directrice-e-23-gestion-du-risque-modelisation-2027
- **Empreinte SHA-256 (LF) :** `60ef80b531aaa0ac26d2180a14bd1c295297dabe7ddf8c4260f37c90b2ecda3e` (`44778` octets, `6372` mots)
- **Synthèse factuelle vérifiée :** Ligne directrice E-23 du BSIF (révisée en septembre 2025) régissant la gestion du risque de modélisation à l'échelle de l'entreprise (incluant l'IA), à compter du 1er mai 2027.

### [21] SRC-067 — Décision d'exécution (UE) 2026/2274 de la Commission du 12 octobre 2026 concernant les normes harmonisées relatives aux systèmes d'IA à haut risque (EN 18286:2026)

- **Auteurs / Émetteur :** Commission européenne
- **Date de publication :** `2026-10-12`
- **Organisme / Revue :** Journal officiel de l'Union européenne (EUR-Lex Cellar)
- **Identifiant :** `UE-2026-2274-EN18286`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-067.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://publications.europa.eu/resource/cellar/05805dc1-c76c-11f1-a77b-01aa75ed71a1.0010.01/DOC_1
- **Empreinte SHA-256 (LF) :** `3d1dcffce8aeb8fa2cf340feb94c21e084800bf21c7249940c0fa51000b37f33` (`5154` octets, `733` mots)
- **Synthèse factuelle vérifiée :** Décision d'exécution (UE) 2026/2274 du 12 octobre 2026 publiant au JOUE la référence de la norme harmonisée EN 18286:2026 relative aux systèmes de gestion de la qualité pour le règlement (UE) 2024/1689 (présomption de conformité au titre de l'article 40 ; portée sur l'article 17 explicitée dans SRC-069).

### [22] SRC-068 — Guideline B-10: Third-Party Risk Management

- **Auteurs / Émetteur :** Office of the Superintendent of Financial Institutions (OSFI / BSIF)
- **Date de publication :** `2023-04-30`
- **Organisme / Revue :** OSFI Canada
- **Identifiant :** `OSFI-B10`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-068.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/third-party-risk-management-guideline
- **Empreinte SHA-256 (LF) :** `db7ccc401ea3b392f22b42c75b63d657eb95cd1c6ab5ccf2d55551bf9be01625` (`55115` octets, `7859` mots)
- **Synthèse factuelle vérifiée :** Ligne directrice B-10 du BSIF (2023) sur la gestion des risques liés aux tiers imposant inventaire des sous-traitants, continuité d'activité et clauses de réversibilité.

### [23] SRC-069 — First harmonised standard supporting the AI Act published in the Official Journal (EN 18286:2026)

- **Auteurs / Émetteur :** Commission européenne (DG CNECT)
- **Date de publication :** `2026-10-21`
- **Organisme / Revue :** European Commission Digital Strategy
- **Identifiant :** `EC-DIGITAL-EN18286-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-069.txt`, score AACODS `11.5/12`)
- **URL d'origine :** https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal
- **Empreinte SHA-256 (LF) :** `647fbb09b0ec2399cfae5add020126b9b9b65b26dee84e381b204afcc21aa291` (`1876` octets, `295` mots)
- **Synthèse factuelle vérifiée :** Communiqué officiel de la Commission européenne (21 octobre 2026) précisant la portée opérationnelle d'EN 18286:2026 et son intégration dans les systèmes QMS sectoriels existants.

### [24] SRC-070 — Loi sur les banques (L.C. 1991, ch. 46 — révision statutaire au 30 juin 2033)

- **Auteurs / Émetteur :** Parlement du Canada / Ministère de la Justice
- **Date de publication :** `2026-10-29`
- **Organisme / Revue :** Justice Canada (Lois codifiées)
- **Identifiant :** `LC-1991-C46`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-070.txt`, score AACODS `12.0/12`)
- **URL d'origine :** https://laws-lois.justice.gc.ca/fra/lois/b-1.01/TexteComplet.html
- **Empreinte SHA-256 (LF) :** `0e1fc93237931022566f8436015964c426c7f7a70f22fe5ab8af69396717bd1f` (`1767391` octets, `266067` mots)
- **Synthèse factuelle vérifiée :** Loi sur les banques (L.C. 1991, ch. 46) régissant notamment le maintien et la localisation au Canada des registres et archives comptables ou clients (art. 239 et suivants).

### [25] SRC-071 — AIBanks.ca — The Canadian Bank AI Index (2026 Q4 edition, agrégateur tiers indépendant)

- **Auteurs / Émetteur :** AIBanks.ca
- **Date de publication :** `2026-11-01`
- **Organisme / Revue :** AIBanks.ca (agrégateur tiers indépendant — index public de preuves)
- **Identifiant :** `AIBANKS-CA-AMF-2026`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-071.txt`, score AACODS `9.0/12`)
- **URL d'origine :** https://www.aibanks.ca/
- **Empreinte SHA-256 (LF) :** `2d39751c5fed55ad19aebd3cc238f8a1a26d6b266bb8bc3f7ee1e0e37a796e8b` (`12404` octets, `1985` mots)
- **Synthèse factuelle vérifiée :** Agrégateur canadien ouvert AIBanks.ca (édition T4 au 1er novembre 2026) confirmant l'échéance du 1er mai 2027 pour BSIF E-23 et signalant l'échéance attendue du 1er mai 2027 de la ligne directrice IA de l'AMF (rapportée sous réserve car le portail lautorite.qc.ca est en statut F).

### [26] SRC-075 — Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents

- **Auteurs / Émetteur :** Shipi Dhanorkar, Samir Passi, Mihaela Vorvoreanu
- **Date de publication :** `2026-06-03`
- **Organisme / Revue :** arXiv (Microsoft Research)
- **Identifiant :** `arXiv:2606.05391`
- **Statut de vérification :** `L+` (texte intégral archivé dans `recherche/corpus_l_plus/SRC-075.txt`, score AACODS `11.0/12`)
- **URL d'origine :** https://arxiv.org/pdf/2606.05391
- **Empreinte SHA-256 (LF) :** `a0b7c487a5e089136bbd97d1f4d9dc54ce8376634f6f270ea425689f31dd179c` (`122290` octets, `17178` mots)
- **Synthèse factuelle vérifiée :** Étude arXiv:2606.05391 analysant les limites pratiques de la supervision humaine face aux systèmes agentiques et l'exigence de preuves d'approbation actionnables.

---

## Exclusions documentaires et statut F (`AO-01`)

- `https://dl.acm.org/doi/10.1145/3143561` (Chen et al. 2018, paywall `HTTP 403`), `https://standards.cencenelec.eu/dyn/www/f?p=CEN:110:0::::FSP_PROJECT:82555` (`HTTP 500`), `https://www.iso.org/standard/81230.html` (`HTTP 403`) et `https://lautorite.qc.ca/` (`HTTP 403`) sont consignés en statut F selon `AO-01` et remplacés par les substituts primaires ouverts `L+` (`SRC-091`, `SRC-092`, `SRC-093`, `SRC-067`, `SRC-069`, `SRC-071`).
