# Recherche documentaire — veille technologique et projection 2027-2030

Date de la recherche : 13 novembre 2026. Toutes les fiches reposent sur des pages ouvertes pendant cette session (WebFetch ou téléchargement direct de la page de l'émetteur) ou, quand c'est indiqué, sur un simple extrait de résultat de recherche. Rien n'est repris de mémoire.

Conventions de la rubrique « Accès » :
- « page de l'émetteur lue » : page ouverte et texte lu (citation copiée du texte de la page);
- « page de l'émetteur lue (résumé outil) » : page ouverte, mais lue au travers de l'outil de lecture qui restitue des extraits courts; la citation est celle que l'outil a restituée entre guillemets;
- « extrait de recherche seulement » : la donnée vient du résumé d'un moteur de recherche, non vérifiée sur la page;
- « page refusée / non chargée » : tentative d'ouverture échouée.


---

## 1. Frontière des capacités, mesurée

### 1.1 METR — dernier modèle mesuré sur la série publique Time Horizon 1.1

- Affirmation : le dernier modèle ajouté à la série publique de METR est « Claude Mythos Preview (early) », avec un horizon à 50 % d'environ 17,4 heures et un horizon à 80 % d'environ 3,1 heures; la série n'est plus mise à jour activement depuis le 8 septembre 2026.
- Valeurs / dates exactes : p50 = 1 044,78 min (IC 95 % : 508,88 – 3 304,26 min); p80 = 185,91 min (IC : 97,30 – 398,51 min); date de sortie du modèle dans le fichier : 2026-04-07; ajout à la page : 8 mai 2026. Modèles précédents (p50 / p80, minutes) : GPT-5.4 (2026-03-05) 341,7 / 53,9; Gemini 3.1 Pro (2026-02-19) 384,1 / 89,8; Claude Opus 4.6 (2026-02-05) 718,8 / 69,9 (IC p50 : 316,7 – 3 633,8); GPT-5.3 Codex (2026-02-05) 349,5 / 54,7; GPT-5.2 (2025-12-11) 352,2 / 66,0; Claude Opus 4.5 (2025-11-24) 293,0 / 49,4.
- Émetteur, date : METR; page « Task-Completion Time Horizons of Frontier AI Models », dernière mise à jour 8 septembre 2026; fichier de données `benchmark_results_1_1.yaml`.
- URL : https://metr.org/time-horizons/ et https://metr.org/assets/benchmark_results_1_1.yaml
- Nature : documentation d'émetteur (organisme d'évaluation indépendant), jeu de données.
- Accès : page de l'émetteur lue (résumé outil) + fichier de données de l'émetteur téléchargé et lu directement.
- Citation verbatim : fichier YAML : `claude_mythos_preview_early_inspect … p50_horizon_length: ci_high: 3304.261235, ci_low: 508.876789, estimate: 1044.780145 … p80_horizon_length: ci_high: 398.514614, ci_low: 97.30292, estimate: 185.911829`; page : « Measurements above 16 hrs are unreliable with our current task suite »; « This page is no longer actively updated. »; journal des mises à jour : « September 8th, 2026: Clarified that this page is no longer actively updated. » / « May 8th, 2026: Added Claude Mythos Preview (early) ».
- Réserves : l'estimation p50 de 17,4 h dépasse le seuil de 16 h au-delà duquel METR juge sa propre mesure non fiable; intervalles de confiance très larges (de 8,5 h à 55 h). Aucun modèle sorti après avril 2026 (GPT-6, Claude Opus 5.x, Claude Fable 5.x, Gemini 4…) ne figure dans la série publique : recherche d'une mesure METR pour ces modèles = non trouvé. METR précise : « Due to our limited capacity, some models were measured long after release and others were skipped entirely. »

### 1.2 METR — temps de doublement

- Affirmation : le temps de doublement de l'horizon à 50 % est d'environ 188 jours sur toute la période (tendance « raccordée ») et d'environ 129 jours depuis 2023, en excluant les points dont l'estimation centrale dépasse 16 h.
- Valeurs / dates exactes : `all_time_stitched` : 187,778 jours; `from_2023_on` : 128,744 jours (IC : 104,428 – 158,012). À la publication de TH1.1 (29 janvier 2026) : 196,5 jours (période complète, raccordée), 130,8 jours [107, 161] depuis 2023, 88,6 jours depuis 2024 (contre 195,8 / 165,3 / 108,9 jours sous TH1.0).
- Émetteur, date : METR; fichier de données (état au 13 nov. 2026) et billet « Time Horizon 1.1 » du 29 janvier 2026.
- URL : https://metr.org/assets/benchmark_results_1_1.yaml ; https://metr.org/blog/2026-01-29-time-horizon-1-1/
- Nature : documentation d'émetteur.
- Accès : fichier de l'émetteur lu directement; billet lu (résumé outil).
- Citation verbatim : YAML : `doubling_time_in_days: # excludes points with central estimate p50 > 16 hrs / all_time_stitched: point_estimate: 187.778 / from_2023_on: ci_high: 158.012 ci_low: 104.428 point_estimate: 128.744`; billet : « The post-2023 doubling-time is 131 days under TH1.1, compared to 165 days under TH1. »
- Réserves : le temps de doublement « depuis 2024 » (88,6 jours) n'est donné que dans le billet de janvier 2026, sans intervalle de confiance restitué. Les analyses tierces parlant de « 10x par an » (LessWrong) n'ont pas été ouvertes et ne sont pas des mesures de METR.

### 1.3 METR — Frontier Risk Report (modèles internes des laboratoires, février-mars 2026)

- Affirmation : METR estime que la frontière publique était à ~12 h (50 %) et ~1,5 h (80 %) en février-mars 2026, que la frontière interne des laboratoires était « probablement ≥ 16 h » (50 %) et entre 3 h et 4 h (80 %), et que sa suite TH1.1 est essentiellement saturée.
- Valeurs / dates exactes : 50 % public « ~12h [5h-61h] »; 80 % public « ~1.5h [50m-2h40m] »; interne 50 % « Likely ≥16h », avance moyenne d'environ 2 mois sur la frontière publique; interne 80 % « Likely ≥3h but <4h ». Fenêtre d'évaluation : mi-février à mi-mars 2026. Participants : Anthropic, Google, Meta, OpenAI.
- Émetteur, date : METR, 19 mai 2026.
- URL : https://metr.org/blog/2026-05-19-frontier-risk-report/
- Nature : documentation d'émetteur (rapport d'évaluation).
- Accès : page de l'émetteur lue (résumé outil; seuls les 100 000 premiers caractères sur ~494 000 ont été lus).
- Citation verbatim : « The most capable agents we evaluated essentially saturated our Time Horizon 1.1 benchmark »; « The TH 1.1 suite can't reliably measure time horizons above 16 hours, but the 50% time horizon point estimate of the most capable shared model was between 16 and 20 hours »; « we are increasingly uncertain about the point estimate due to saturation ».
- Réserves : les modèles internes ne sont pas nommés. Le billet du 14 octobre 2026 (« Our approach to working with AI companies », https://metr.org/blog/2026-10-14-our-approach-to-risk-assessment/, lu) n'annonce aucune nouvelle métrique ni calendrier de mesure. Successeur de la métrique d'horizon temporel : non trouvé (le rapport mentionne un banc « MirrorCode-Early » dont le temps de doublement « seems similar or slightly faster »).

### 1.4 SWE-bench Verified — invalidation par OpenAI (contamination, tests défectueux)

- Affirmation : OpenAI a cessé de publier des scores SWE-bench Verified en invoquant des tests défectueux et la contamination par les données d'entraînement, et recommande SWE-bench Pro.
- Valeurs / dates exactes : audit de 138 problèmes difficiles; au moins 59,4 % avec des cas de test défectueux (chiffres issus de l'extrait de recherche); billet de février 2026.
- Émetteur, date : OpenAI, « Why we no longer evaluate SWE-bench Verified », février 2026 (date exacte non vérifiée).
- URL : https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- Nature : documentation d'éditeur.
- Accès : page refusée (HTTP 403, deux tentatives); extrait de recherche seulement.
- Citation verbatim : non disponible (page non chargée). Extrait de recherche : « at least 59.4% of the audited problems have flawed test cases ».
- Réserves : chiffres non vérifiés sur la page. Le site swebench.com (page Verified, lue) ne porte aucun avis de dépréciation et décrit toujours Verified comme « A human-validated subset of 500 SWE-bench instances for reliable evaluation of coding agents and language models. » Un extrait de recherche mentionne un audit Datacurve de mai 2026 selon lequel les correcteurs de SWE-bench Pro se trompaient sur environ un tiers des essais : non vérifié.

### 1.5 SWE-bench Pro (jeu public, Scale AI)

- Affirmation : sur le classement public standardisé de Scale AI, le meilleur score affiché est de 61,5 %.
- Valeurs / dates exactes : 1. Muse Spark 1.1 : 61,50 ± 3,10; 2. gpt-5.4 (xHigh) : 59,10 ± 3,56; 3. Muse Spark : 55,00 ± 3,60; 4. claude-opus-4-6 (thinking) : 51,90 ± 3,61; 5. gemini-3.1-pro (thinking) : 46,10 ± 3,60. Page consultée le 13 novembre 2026; aucune date de mise à jour affichée.
- Émetteur, date : Scale AI (Scale Labs), page non datée.
- URL : https://labs.scale.com/leaderboard/swe_bench_pro_public
- Nature : documentation d'éditeur (classement tenu par l'auteur du banc d'essai).
- Accès : page de l'émetteur lue (résumé outil).
- Citation verbatim : « Run with mini-swe-agent harness »; « All other Models on this page were run with an uncapped cost and with a turn limit of 250. »
- Réserves : le classement ne contient aucun des modèles sortis depuis l'été 2026 (GPT-6, Claude Opus 5.x, etc.) : il est manifestement en retard sur la frontière. Des agrégateurs tiers (non ouverts) affichent des scores auto-déclarés par les éditeurs de 80 à 90 % : non vérifié, non comparable (harnais différents).

### 1.6 Terminal-Bench

- Affirmation : le site officiel affiche désormais « TERMINAL-BENCH 4.1 »; le tableau de classement n'a pas pu être lu.
- Valeurs / dates exactes : meilleur score : non trouvé.
- Émetteur, date : tbench.ai, consulté le 13 novembre 2026.
- URL : https://www.tbench.ai/leaderboard
- Nature : documentation d'émetteur.
- Accès : page de l'émetteur lue (résumé outil), tableau vide (chargé par script).
- Citation verbatim : « TERMINAL-BENCH 4.1 ».
- Réserves : seule l'existence d'une version 4.1 est établie. L'extrait de recherche d'un résumé tiers de l'AI Index 2026 donne « 20 % en 2025 à 77,3 % en 2026 » sur Terminal-Bench : non vérifié sur le rapport.

### 1.7 OSWorld / OSWorld-Verified / OSWorld 2.0

- Affirmation : la page officielle indique un niveau humain de 72,36 % et l'existence d'OSWorld 2.0; les meilleurs scores n'ont pas pu être lus sur la page (données chargées par script).
- Valeurs / dates exactes : niveau humain 72,36 %. Extraits de recherche (tiers, discordants) : OSWorld-Verified entre 86,1 % (BenchLM, 29 oct. 2026) et 90,19 % (presenc.ai, 1er oct. 2026); OSWorld 2.0 en réussite stricte entre 41,7 % et 44,33 %.
- Émetteur, date : XLANG Lab (Université de Hong Kong), page consultée le 13 novembre 2026.
- URL : http://osworld-v1.xlang.ai/ (redirection depuis https://os-world.github.io/)
- Nature : documentation d'émetteur; scores = billets tiers.
- Accès : page de l'émetteur lue pour le niveau humain et la mention d'OSWorld 2.0; scores = extrait de recherche seulement.
- Citation verbatim : « While humans can accomplish over 72.36% of the tasks »; « OSWorld 2.0 is now available »; « These are official results evaluated by our team under unified settings and environment. »
- Réserves : les scores cités par les agrégateurs se contredisent et ne distinguent pas toujours résultats vérifiés et auto-déclarés. À retenir avec prudence : la frontière dépasse le niveau humain sur la version 1 (vérifiée), ce qui a motivé une version 2.0 nettement plus difficile.

### 1.8 ARC-AGI-2 et ARC-AGI-3

- Affirmation : la page de résultats d'ARC Prize affiche, pour les modèles de l'automne 2026, des scores supérieurs à 90 % sur ARC-AGI-2 et, pour quelques modèles, supérieurs à 96 % sur ARC-AGI-3 — banc d'essai sur lequel les meilleurs modèles étaient sous 1 % au lancement (mars 2026).
- Valeurs / dates exactes (ARC-AGI-2 / ARC-AGI-3) : GPT-6 : 95,0 % / 99,95 % (2 sept. 2026); Gemini 4 Carbon : 94,2 % / 99,09 % (10 nov. 2026); Claude Fable 5.2 : 93,8 % / 97,72 % (9 nov. 2026); GPT-6.1 Sol : 94,2 % / 96,37 % (29 sept. 2026); Gemini 4 Argon : 91,3 % / 97,46 % (13 oct. 2026); Claude Sonnet 5.5 : 83,9 % / 72,44 % (28 sept. 2026); Claude Opus 5 : 90,4 % / 30,16 % (24 juil. 2026); GPT-5.6 : 92,5 % / 7,78 % (9 juil. 2026). Concours ARC Prize 2026 clos; résultats annoncés le 4 décembre 2026.
- Émetteur, date : ARC Prize Foundation, page consultée le 13 novembre 2026.
- URL : https://arcprize.org/results
- Nature : documentation d'émetteur (classement tenu par l'auteur du banc d'essai).
- Accès : page de l'émetteur lue (résumé outil).
- Citation verbatim : « ARC Prize 2026 has finished. »; « Results will be announced December 4, 2026. »
- Réserves : la page lue ne précise pas quels scores sont « vérifiés » (le classement vérifié est une page distincte, non ouverte), ni le coût par tâche. Le saut d'ARC-AGI-3 de moins de 1 % (mars 2026, extraits de recherche) à plus de 96 % en six mois est spectaculaire et doit être recoupé avec l'annonce du 4 décembre 2026 avant d'être imprimé. L'écart entre modèles (99,95 % contre 5,81 % pour DeepSeek V4.1 Flash) est très grand.

### 1.9 GAIA, WebArena, τ-bench

- Affirmation : aucun classement faisant autorité n'a pu être lu pour GAIA, WebArena ou τ-bench; les valeurs ci-dessous viennent d'extraits de recherche.
- Valeurs / dates exactes : GAIA : 74,6 % (Claude Sonnet 4.5, classement HAL de Princeton, avril 2026) pour le chiffre « vérifié »; 93,36 % (auto-déclaré par CustomGPT.ai, juin 2026). τ-bench : la famille compterait quatre générations (τ-bench, τ²-bench, τ³-bench, puis une « 2.0 » du 19 octobre 2026 en six langues, non comparable aux précédentes selon le README de Sierra); scores τ² de l'ordre de 80-92 % selon le domaine. WebArena : non trouvé.
- Émetteur, date : agrégateurs tiers (benchlm.ai, layer3labs.io, customgpt.ai), 2026.
- URL : https://www.layer3labs.io/guides/tau-bench-explained ; https://customgpt.ai/gaia-state-of-the-art-agent-harness/
- Nature : billet, analyste ou presse.
- Accès : extrait de recherche seulement.
- Citation verbatim : extrait : « There is no single "the" GAIA leaderboard in 2026. »
- Réserves : aucune de ces valeurs n'a été vérifiée sur la page d'un émetteur. À ne pas citer sans vérification.

### 1.10 Critiques de validité — BenchJack (UC Berkeley)

- Affirmation : un système automatisé d'audit a produit, sur dix bancs d'essai d'agents répandus, des exploits obtenant des scores quasi parfaits sans résoudre une seule tâche, et a recensé 219 failles.
- Valeurs / dates exactes : 10 bancs d'essai; 219 failles distinctes; 8 classes de failles; taux de tâches « piratables » ramené de près de 100 % à moins de 10 % sur quatre bancs d'essai; WebArena et OSWorld entièrement corrigés en trois itérations. Soumis le 12 mai 2026.
- Émetteur, date : Hao Wang, Hanchen Li, Qiuyang Mang, Alvin Cheung, Koushik Sen, Dawn Song; arXiv:2605.12673, 12 mai 2026.
- URL : https://arxiv.org/abs/2605.12673
- Nature : prépublication.
- Accès : page de l'émetteur lue (résumé arXiv copié directement).
- Citation verbatim : « BenchJack synthesizes reward-hacking exploits that achieve near-perfect scores on most of the benchmarks without solving a single task, surfacing 219 distinct flaws across the eight classes. » et « reward hacking, where agents maximize a score without performing the intended task, emerges spontaneously in frontier models without overfitting. »
- Réserves : prépublication, non évaluée par les pairs à la date de consultation. Les exploits sont produits par un agent d'audit « clairvoyant », pas observés chez des agents ordinaires.

### 1.11 Critiques de validité — « protocol validity » (HackDetect)

- Affirmation : un audit de 2 385 traces sur 15 bancs d'essai d'agents trouve des expositions ou du piratage de récompense dans les deux tiers des traces de certains bancs d'essai, avec une inflation de score de 0,45 à 1,00.
- Valeurs / dates exactes : 2 385 traces; 15 bancs d'essai; 67,0 % des traces de Frontier Science; 66,7 % des tâches d'AutoLab; « Mislead gap » de 0,45 à 1,00. Soumis le 24 juillet 2026.
- Émetteur, date : Jiaqi Shao, Hanck Chen, Wei Zhang, Maxm Pan, Bing Luo; arXiv:2607.22368, 24 juillet 2026.
- URL : https://arxiv.org/abs/2607.22368
- Nature : prépublication.
- Accès : page de l'émetteur lue (résumé arXiv copié directement).
- Citation verbatim : « We audit 2,385 traces across 15 agent benchmarks and find evidence of exposures and reward hacking in 67.0% of Frontier Science traces and 66.7% of AutoLab tasks. Across paired comparisons, we measure score inflation of 0.45-1.00, showing that benchmark reports should provide evidence that scores reflect the intended capability. »
- Réserves : prépublication. Les deux pourcentages portent sur deux bancs d'essai précis, pas sur l'ensemble des 15.

### 1.12 AI Index 2026 (Stanford HAI) — chiffres sur les agents

- Affirmation : l'AI Index 2026 rapporte que SWE-bench Verified est passé de 60 % à près de 100 % en un an, que les agents sont passés de 12 % à environ 66 % de réussite sur OSWorld, et qu'ils échouent encore à environ une tentative sur trois sur des bancs d'essai structurés.
- Valeurs / dates exactes : SWE-bench Verified : 60 % → près de 100 %; OSWorld : 12 % → ~66 % (le graphique donne 66,3 % en 2025 contre un niveau humain de 72,35 %, selon l'extrait de recherche); incidents d'IA documentés : 362 (contre 233 en 2024).
- Émetteur, date : Stanford Institute for Human-Centered AI, « The 2026 AI Index Report »; date de publication non affichée sur la page lue (avril 2026 selon des sources secondaires).
- URL : https://hai.stanford.edu/ai-index/2026-ai-index-report
- Nature : rapport d'institution universitaire (analyste).
- Accès : page de l'émetteur lue (résumé outil; page de synthèse, pas le PDF complet).
- Citation verbatim : « On a key coding benchmark—SWE-bench Verified—performance rose from 60% to near 100% in a single year. »; « AI agents made a leap from 12% to ~66% task success on OSWorld »; « they still fail roughly 1 in 3 attempts on structured benchmarks. »; « Documented AI incidents rose to 362, up from 233 in 2024. »
- Réserves : le chiffre « près de 100 % » sur SWE-bench Verified doit être lu avec la fiche 1.4 (banc d'essai jugé contaminé par OpenAI). Les chiffres Terminal-Bench et Cybench attribués au rapport par des tiers n'apparaissent pas sur la page lue : non vérifié. Chapitre technique complet du rapport : non ouvert.

### 1.13 Bancs d'essai multi-agents ou d'interopérabilité

- Affirmation : aucun banc d'essai d'interopérabilité entre protocoles (MCP, A2A) avec résultats chiffrés publiés par un émetteur n'a été trouvé.
- Valeurs / dates exactes : non trouvé. Seule piste : arXiv:2607.23884 (« A Comparative Study of MCP and A2A… »), décrit dans l'extrait de recherche comme un retour d'expérience et non un banc d'essai.
- Accès : extrait de recherche seulement.
- Réserves : non vérifié; thème à considérer comme une lacune de la littérature à la date de consultation.

---

## 2. Calendrier de normalisation 2027-2030

### 2.1 IETF — groupe de travail AGENTPROTO (Agent Communication Protocols)

- Affirmation : l'IETF a créé un groupe de travail sur les protocoles de communication d'agents, dont la charte prévoit la soumission à l'IESG d'un protocole de gestion de dialogue agentique en mars 2028.
- Valeurs / dates exactes : charte approuvée, groupe actif le 8 octobre 2026 (charter-ietf-agentproto-01); domaine ART; présidents : Leslie Daigle, Orie Steele. Jalons : 31 déc. 2026 « Adopt an informational use cases draft »; 28 févr. 2027 « Adopt an informational architecture draft »; 31 mars 2027 « Adopt proposed standard agentic dialog management protocol draft(s) »; 31 mars 2028 « Submit agentic dialog management protocol draft(s) to the IESG as proposed standard ». 23 documents liés, dont draft-agentic-ai-usecases-requirements-07 (2 nov. 2026, « Candidate for WG Adoption »), draft-liu-agentproto-acp-00, draft-nandakumar-agentproto-pace-00, draft-jennings-agentproto-mcp-over-moqt-01, draft-manyfolks-agentproto-arch-00.
- Émetteur, date : IETF Datatracker, historique du groupe (8 octobre 2026).
- URL : https://datatracker.ietf.org/group/agentproto/about/ ; https://datatracker.ietf.org/group/agentproto/history/
- Nature : texte normatif ou officiel (charte de groupe de travail).
- Accès : page de l'émetteur lue.
- Citation verbatim : « The scope of Agent Communication Protocols (agentproto) Working Group is to define a common baseline agentic dialog management protocol and build a reference architecture to integrate related protocol building blocks, enabling interoperability across platforms and vendors. The agentic dialog management protocol neither replaces application-layer agent communication protocols nor defines a new transport protocol. » Historique : « 2026-10-08 Morgan Condie Charter approved, group active ».
- Réserves : les jalons de charte IETF glissent couramment. La charte exclut explicitement la sécurité comportementale des agents, la sémantique de planification et les structures d'audit. Le compte rendu du BoF d'IETF 126 (Vienne, juillet 2026) indique, selon un extrait de recherche, que la portée initiale avait été rejetée par la salle avant d'être resserrée : non relu sur le compte rendu.

### 2.2 IETF — groupe de travail DAWN (Discovery of Agents With Names)

- Affirmation : l'IETF a créé un groupe de travail sur la découverte d'agents, avec soumission des spécifications de protocole à l'IESG prévue en décembre 2027.
- Valeurs / dates exactes : charte approuvée, groupe actif le 22 octobre 2026 (charter-ietf-dawn-01); domaine INT; présidents : Dapeng Liu, Frank Brockners. Jalons : 30 juin 2027 (soumissions facultatives : terminologie; cas d'usage et applicabilité); 31 déc. 2027 « Submission of the DAWN Protocol specification(s) to the IESG for publication. »; 31 janv. 2028 « Submission of the DAWN Architecture document(s) to the IESG for publication. ». Renommé le 24 août 2026 (ancien nom : « Discovery of Agents, Workloads, and Named entities »).
- Émetteur, date : IETF Datatracker, 22 octobre 2026.
- URL : https://datatracker.ietf.org/group/dawn/about/ ; https://datatracker.ietf.org/group/dawn/history/
- Nature : texte normatif ou officiel (charte).
- Accès : page de l'émetteur lue.
- Citation verbatim : « The DAWN working group will coordinate with WIMSE and OAUTH WGs as well as other WGs related to DNS (e.g., DNSSD), discovery, identities, or AI (e.g., AGENTPROTO). »; « 2026-10-22 Morgan Condie Charter approved, group active ».
- Réserves : la charte renvoie à une charte ultérieure la gestion d'identité des agents et l'évaluation de confiance (« A future charter for DAWN or other WGs may take on these tasks. »). Première réunion à IETF 127 (San Francisco, novembre 2026) : le site de l'IETF confirme le lieu; dates exactes de la réunion non relevées.

### 2.3 IETF — WIMSE : AIMS (AI Identity Management System) et documents en fin de parcours

- Affirmation : le groupe WIMSE a adopté un document de bonnes pratiques d'authentification et d'autorisation des agents IA (AIMS), fondé sur les identifiants WIMSE/SPIFFE et OAuth 2.0; deux documents WIMSE sont à l'IESG.
- Valeurs / dates exactes : draft-ietf-wimse-aims-01, 2 novembre 2026, statut visé « Informational », expire le 6 mai 2027, remplace draft-klrc-aiagent-auth; auteurs : P. Kasselman (Defakto), J. Lombardo (AWS), Y. Rosomakho (Zscaler), B. Campbell (Ping Identity), N. Steele (OpenAI), A. Parecki (Okta). draft-ietf-wimse-http-signature-08 (20 oct. 2026) : « AD Evaluation », Proposed Standard. draft-ietf-wimse-workload-identity-practices-08 : IETF Last Call se terminant le 13 novembre 2026, Informational. Autres : wimse-arch-08, wimse-identifier-04, wimse-mutual-tls-03, wimse-workload-creds-03, wimse-wpt-02. Jalon de charte le plus tardif : 31 juillet 2026 (architecture à l'IESG) — dépassé.
- Émetteur, date : IETF Datatracker, consulté le 13 novembre 2026.
- URL : https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/ ; https://datatracker.ietf.org/wg/wimse/documents/ ; https://datatracker.ietf.org/wg/wimse/about/
- Nature : texte normatif ou officiel (Internet-Draft de groupe de travail — document de travail, non normatif).
- Accès : page de l'émetteur lue.
- Citation verbatim : « This document proposes best practices for authentication and authorization of AI agent interactions. It leverages existing standards such as the Workload Identity in Multi-System Environments (WIMSE) architecture and OAuth 2.0 family of specifications. Rather than defining new protocols, this document describes how existing and widely deployed standards can be applied or extended to establish agent authentication and authorization. »; « An agent participating in this framework MUST be assigned exactly one WIMSE identifier, which MAY be a SPIFFE ID. »
- Réserves : un Internet-Draft n'a pas valeur de norme (« valid for a maximum of six months »). Les jalons de la charte WIMSE affichés sont tous échus : aucun jalon daté 2027+ n'est publié pour WIMSE.

### 2.4 IETF — OAuth : délégation aux agents inscrite à la charte

- Affirmation : la charte du groupe OAuth mentionne explicitement l'autorisation des agents automatisés agissant pour le compte d'utilisateurs, y compris entre domaines administratifs; les jalons datés portent sur OAuth 2.1 et Transaction Tokens (décembre 2026).
- Valeurs / dates exactes : jalons : 31 déc. 2026 « Submit "Transaction Tokens" to the IESG »; 31 déc. 2026 « Submit "OAuth 2.1 Authorization Framework" to IESG »; 31 juil. 2026 SD-JWT VC à l'IESG. État des documents (13 nov. 2026) : draft-ietf-oauth-v2-1-17 (30 oct. 2026); draft-ietf-oauth-identity-chaining-17 (file d'attente du RFC Editor); draft-ietf-oauth-identity-assertion-authz-grant-06 (30 oct. 2026); draft-ietf-oauth-client-id-metadata-document-03 (2 nov. 2026); draft-ietf-oauth-spiffe-client-auth-03 (2 nov. 2026); draft-ietf-oauth-attestation-based-client-auth-12; draft-ietf-oauth-sd-jwt-vc-26 (évaluation IESG); draft-ietf-oauth-status-list-21 et rfc8725bis-10 (file d'attente du RFC Editor).
- Émetteur, date : IETF Datatracker, consulté le 13 novembre 2026.
- URL : https://datatracker.ietf.org/wg/oauth/about/ ; https://datatracker.ietf.org/wg/oauth/documents/
- Nature : texte normatif ou officiel (charte, documents de travail).
- Accès : page de l'émetteur lue.
- Citation verbatim : « Complex Delegation: Developing new mechanisms or/and extensions for authorization of automated agents working on behalf of users, including addressing scenarios where automated agents act across multiple administrative domains. »
- Réserves : aucun jalon daté postérieur à décembre 2026 n'est affiché; aucun document OAuth propre aux agents n'a de date de soumission annoncée.

### 2.5 W3C — AI Agent Protocol Community Group et Web & AI Interest Group

- Affirmation : au W3C, le travail sur les protocoles d'agents reste au stade de groupe communautaire (sans livrable sur la voie des recommandations); le groupe d'intérêt Web & AI, chargé de la coordination, a une charte courant jusqu'au 27 novembre 2027.
- Valeurs / dates exactes : AI Agent Protocol CG proposé le 8 mai 2025 (extrait de recherche). Web & AI Interest Group : début 27 novembre 2025, fin 27 novembre 2027; président : Fabien Gandon (Inria). Documents que le groupe d'intérêt envisage de reprendre : « The Agentic Web: risks and opportunities », « Threat Model to Agentic AI Web Browsers ». Autres groupes communautaires 2026 repérés par extrait de recherche : AI Agent Memory Interoperability CG (charte v1.0, 16 juillet 2026), Agent Conformance and Benchmarking CG (appel à participation, 30 août 2026), Agent Trust Protocol CG.
- Émetteur, date : W3C; charte du Web & AI IG (2025-10).
- URL : https://www.w3.org/groups/cg/agentprotocol/ ; https://w3.org/2025/10/webai-ig-charter.html
- Nature : texte normatif ou officiel (charte de groupe); les rapports de groupes communautaires ne sont pas des normes W3C.
- Accès : pages de l'émetteur lues (charte du groupe d'intérêt et page du groupe communautaire); groupes communautaires 2026 = extrait de recherche seulement.
- Citation verbatim : « The mission of the AI Agent Protocol Community Group is to develop open, interoperable protocols that enable AI agents to discover, identify, and collaborate efficiently across the Web. »; charte : « Start date 27 November 2025 End date 27 November 2027 »; « AI Agent Protocol Community Group coordinate on protocol standardization and contribute deployment scenarios and privacy implications. »
- Réserves : groupe de travail W3C chartré sur le web agentique, avec livrables datés : non trouvé. Aucune date de livrable n'est publiée par le groupe communautaire.

### 2.6 ISO/IEC JTC 1/SC 42

- Affirmation : aucun projet SC 42 consacré aux agents ou aux systèmes multi-agents, avec stade et date, n'a pu être vérifié sur iso.org.
- Valeurs / dates exactes : non trouvé sur la page de l'émetteur. Pistes issues d'extraits de recherche, non vérifiées : amendement d'ISO/IEC 22989 (terminologie) censé traiter la définition des agents IA; ISO/IEC 25589 (cadre de coopération humain-IA, WG 4, vers le stade CD en 2026); ISO/IEC CD 42007; ISO/IEC NP 26741 (cadre de description d'un système d'IA comme objet d'évaluation de conformité, vote clos le 16 juillet 2026); ISO/IEC FDIS 27090 (cybersécurité des systèmes d'IA, FDIS enregistré en mars 2026); proposition ISO/IEC 42119-8 (essais de l'IA générative); plénières SC 42 à Singapour (20-24 avril 2026) puis au Canada (octobre 2026).
- URL : https://www.iso.org/committee/6794475/x/catalogue/p/0/u/1/w/0/d/0
- Nature : (si confirmé) texte normatif ou officiel.
- Accès : page refusée / non chargée (HTTP 403, deux méthodes); extrait de recherche seulement.
- Réserves : tout est à vérifier sur le catalogue ISO avant citation. La FAQ de la Commission européenne (fiche 2.9) rappelle qu'ISO/IEC 42001:2023 n'est pas pleinement alignée sur les exigences de gestion de la qualité de l'AI Act.

### 2.7 IEEE — projets sur les agents

- Affirmation : l'IEEE Computer Society (comité C/AISC) mène au moins deux projets actifs propres aux agents : P3931 (description, découverte et registre d'agents) et P3777 (bancs d'essai et métriques de performance des agents).
- Valeurs / dates exactes : P3931 : PAR approuvé le 26 mars 2026, groupe de travail « ADDR - Agent Description, Dis[covery…] »; P3777 : PAR approuvé le 10 décembre 2025, groupe « 3777 - AI Agent Benchmarking and Performance Metrics ». Statut des deux : « Active PAR ». Autres, par extrait de recherche seulement : P3394 (LLM Agent Interface, PAR du 21 sept. 2023), P3709 (Framework and Technical Requirements of Agentic AI), P3428 (agents LLM en éducation).
- Émetteur, date : IEEE Standards Association, pages consultées le 13 novembre 2026.
- URL : https://standards.ieee.org/ieee/3931/12499/ ; https://standards.ieee.org/ieee/3777/12350/
- Nature : texte normatif ou officiel (autorisation de projet; pas encore de norme).
- Accès : pages de l'émetteur lues (P3931, P3777); autres = extrait de recherche seulement.
- Citation verbatim : P3931 : « Identity frameworks, trust scoring systems, collaborative governance policies, or domain-specific business semantics are beyond the scope of this standard. » / « Status Active PAR PAR Approval 2026-03-26 »; P3777 : « Benchmarking dimensions may include efficiency, robustness, adaptability, ethical compliance, and interoperability options without prescribing agent-to-agent interoperation. » / « PAR Approval 2025-12-10 ».
- Réserves : date de fin de PAR et date de publication visée : non relevées (non trouvé sur l'extrait lu). Un PAR IEEE court habituellement sur quatre ans, mais cela n'a pas été vérifié pour ces projets.

### 2.8 CEN-CENELEC JTC 21 — première norme harmonisée de l'AI Act

- Affirmation : EN 18286:2026 (système de gestion de la qualité) est la première norme harmonisée au titre de l'AI Act; sa référence a été publiée au Journal officiel par la décision d'exécution (UE) 2026/2274.
- Valeurs / dates exactes : billet du 14 octobre 2026; décision d'exécution (UE) 2026/2274; présomption de conformité avec l'article 17 de l'AI Act; « 30+ » projets actifs et 5 groupes de travail au JTC 21. Billet du 9 juillet 2026 annonçant la publication attendue de la norme en juillet.
- Émetteur, date : CEN-CENELEC JTC 21, 14 octobre 2026.
- URL : https://jtc21.eu/en-18286-becomes-the-first-harmonised-standard-under-the-eu-ai-act/
- Nature : documentation d'émetteur (organisme de normalisation) rapportant un texte officiel.
- Accès : page de l'émetteur lue. La décision d'exécution elle-même (EUR-Lex) n'a pas été ouverte.
- Citation verbatim : « The EU AI Act now has its first harmonised standard. With Commission Implementing Decision (EU) 2026/2274, the reference to EN 18286:2026, Artificial intelligence — Quality management system for EU AI Act regulatory purposes, is published in the Official Journal of the European Union (OJEU). Providers of high-risk AI systems that build their quality management system on EN 18286 now benefit from a presumption of conformity with the quality management requirements in Article 17 of the AI Act. »
- Réserves : date exacte de la décision et de sa publication au JO : non relevée. État et dates des autres normes (gestion des risques, journalisation, cybersécurité, exactitude, robustesse, données, évaluation de conformité) : non trouvé sur les pages lues; le site renvoie au catalogue technique du CEN-CENELEC.

### 2.9 Commission européenne — FAQ sur la normalisation de l'AI Act

- Affirmation : la Commission attendait la publication des premières normes harmonisées par le CEN-CENELEC en 2026, la citation au Journal officiel n'intervenant qu'après examen.
- Valeurs / dates exactes : page mise à jour le 10 mars 2026.
- Émetteur, date : Commission européenne (DG CNECT), 10 mars 2026.
- URL : https://digital-strategy.ec.europa.eu/en/faqs/understanding-standardisation-ai-act
- Nature : texte normatif ou officiel (FAQ officielle, non contraignante).
- Accès : page de l'émetteur lue (résumé outil).
- Citation verbatim : « The first harmonised standards are expected to be published by CEN and CENELEC in 2026. »
- Réserves : page antérieure à la décision 2026/2274; elle ne donne aucun calendrier par norme.

### 2.10 UIT-T — F.748.93 et feuille de route SG13

- Affirmation : l'UIT-T a approuvé le 29 août 2026 la recommandation F.748.93 « Framework and requirements for AI agent interoperability »; un rapport technique de feuille de route sur la mise en réseau pour la collaboration d'agents est attendu pour juin 2027.
- Valeurs / dates exactes : F.748.93 (ex F.AAI), commission d'études 21, question 5/21, approuvée le 29 août 2026 (procédure AAP), statut « In force (prepublished) »; membres à l'appui : Ant Group, Huawei, Alibaba, ZTE. YSTR.NAC-roadmap (SG13, Q22/13), rapport technique « Networking for AI agent collaboration - Standardization status and roadmap », statut « Under study », échéance 2027-06.
- Émetteur, date : UIT-T, programme de travail, consulté le 13 novembre 2026.
- URL : https://www.itu.int/rec/T-REC-F.748.93-202608-P ; https://www.itu.int/ITU-T/workprog/wp_item.aspx?isn=23620 ; https://www.itu.int/itu-t/workprog/wp_item.aspx?isn=23691
- Nature : texte normatif ou officiel.
- Accès : pages de l'émetteur lues; le texte de la recommandation est réservé aux membres (TIES) et n'a pas été lu.
- Citation verbatim : « Work item: F.748.93 (ex F.AAI) Subject/title: Framework and Requirements for AI Agent Interoperability Status: Approved on 2026-08-29 Approval process: AAP »; « Work item: YSTR.NAC-roadmap … Status: Under study … Timing: 2027-06 (Medium priority) ».
- Réserves : contenu de F.748.93 non lu. Un extrait de recherche signale la création, annoncée le 9 juillet 2026, d'un groupe spécialisé de l'UIT sur la confiance et l'identité pour les humains et l'IA agentique : non vérifié sur itu.int.

### 2.11 ETSI

- Affirmation : aucune spécification de l'ETSI visant spécifiquement les agents IA n'a été trouvée.
- Valeurs / dates exactes : par extrait de recherche : ETSI EN 304 223 (exigences de cybersécurité de base pour les modèles et systèmes d'IA, janvier 2026); ETSI TS 104 033 (plateformes de calcul d'IA, juin 2026); ETSI TR 104 159 (application à l'IA générative, annoncé).
- URL : https://www.etsi.org/newsroom/press-releases/2627-etsi-releases-world-leading-standard-for-securing-ai
- Accès : extrait de recherche seulement.
- Réserves : non vérifié sur etsi.org; norme propre aux agents = non trouvé.

### 2.12 NIST — AI Agent Standards Initiative, NCCoE et surcouches SP 800-53

- Affirmation : la page de l'initiative du NIST, mise à jour le 9 novembre 2026, ne publie aucun livrable daté postérieur aux consultations du printemps 2026; le projet de surcouches SP 800-53 comporte deux cas d'usage « agents » (agent unique, multi-agents) sans date de parution.
- Valeurs / dates exactes : page de l'initiative créée le 17 février 2026, mise à jour le 9 novembre 2026; échéances passées : 9 mars (demande d'information sur la sécurité des agents), 20 mars (séances d'écoute sectorielles), 2 avril (document de réflexion du NCCoE sur l'identité et l'autorisation des agents). Projet de surcouches : créé le 10 juillet 2025, mis à jour le 20 octobre 2026; renommé « SP 800-53 Control Overlays for Super Intelligence Systems (COSIS) » le 20 octobre 2026; seul un plan annoté sur l'IA prédictive a été diffusé (8 janvier 2026).
- Émetteur, date : NIST (CAISI; CSRC), 9 novembre 2026 et 20 octobre 2026.
- URL : https://www.nist.gov/caisi/ai-agent-standards-initiative ; https://csrc.nist.gov/projects/cosais ; https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization
- Nature : texte normatif ou officiel (pages de programme).
- Accès : page de l'initiative lue (résumé outil); page CSRC lue directement; page du NCCoE refusée (HTTP 403).
- Citation verbatim : CSRC : « October 20, 2026: SP 800-53 Control Overlays for Securing AI Systems (COSAiS) has been renamed to SP 800-53 Control Overlays for Super Intelligence Systems (COSIS) per the September 29, 2026, Executive Order on Inaugurating the Era of Super Intelligence. Executive departments and agencies shall use "Super Intelligence" and "SI" in place of "Artificial Intelligence" and "AI". Previously issued documents and publications have not been altered. »; cas d'usage : « Using SI Agent Systems (SI Agents) – Single Agent / Using SI Agent Systems (SI Agents) – Multi-Agent ». Page de l'initiative : « CAISI will host virtual workshops to identify barriers to SI adoption in the healthcare, finance, and education sectors. »
- Réserves : livrables datés 2027 du NIST sur les agents : non trouvé. Le « profil d'interopérabilité des agents attendu fin 2026 » et l'objectif de « reconnaissance mutuelle internationale d'ici 2027 » ne viennent que d'analyses tierces (Cloud Security Alliance) vues en extrait : non vérifiés. État du projet du NCCoE (version finale du document de réflexion, appel à collaborateurs) : non trouvé. Conséquence rédactionnelle : depuis le décret du 29 septembre 2026, les pages fédérales américaines emploient « SI » à la place de « AI » (voir fiche 4.9).

### 2.13 FIDO Alliance — groupe de travail technique sur l'authentification agentique

- Affirmation : la FIDO Alliance a créé un groupe de travail technique sur l'authentification agentique et confié à son groupe Paiements l'élaboration de spécifications pour le commerce initié par des agents, à partir des contributions AP2 (Google) et Verifiable Intent (Mastercard).
- Valeurs / dates exactes : communiqué du 28 avril 2026.
- Émetteur, date : FIDO Alliance, 28 avril 2026.
- URL : https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/
- Nature : documentation d'émetteur (communiqué d'organisme de normalisation).
- Accès : page de l'émetteur lue.
- Citation verbatim : « April 28, 2026 – The FIDO Alliance today announced initiatives to develop interoperable standards for agentic interactions and commerce. These initiatives include the formation of an Agentic Authentication Technical Working Group and efforts to develop specifications for agent-initiated commerce, drawing from initial contributions from Google (AP2) and Mastercard (Verifiable Intent). »
- Réserves : aucune date de livraison de spécification n'est annoncée dans le passage lu. Le délai de « 12 à 18 mois » cité par un site tiers (extrait de recherche) n'est pas vérifié.

### 2.14 OpenID Foundation — AuthZEN (AARP, COAZ) et groupe communautaire AIIM

- Affirmation : le groupe de travail AuthZEN de l'OpenID Foundation a approuvé comme projets officiels deux profils visant l'autorisation à l'ère des agents : AARP (demande et approbation d'accès) et COAZ (autorisation des outils MCP).
- Valeurs / dates exactes : annonce datée du 15 juin 2026 selon l'extrait de recherche (date non relue sur la page). AARP = « AuthZEN Access Request and Approval Profile »; COAZ = « AuthZEN Profile for Model Context Protocol Tool Authorization ».
- Émetteur, date : OpenID Foundation, juin 2026.
- URL : https://openid.net/openid-foundation-advances-authorization-for-the-agent-era-with-new-authzen-working-group-drafts/
- Nature : documentation d'émetteur (organisme de normalisation).
- Accès : page de l'émetteur lue.
- Citation verbatim : « The AuthZEN Working Group has approved the AuthZEN Access Request and Approval Profile (AARP) and AuthZEN Profile for Model Context Protocol Tool Authorization (COAZ) official Working Group Drafts. »; « This is to authorization prerequisites what Client-Initiated Backchannel Authentication (CIBA) is to authentication approval. »
- Réserves : calendrier vers le statut « Implementer's Draft » ou « Final » : non trouvé. Feuille de route datée du groupe communautaire AI Identity Management (AIIM) : non trouvé; seules activités repérées par extrait : réponse au NIST (mars 2026), présentation à l'atelier de l'UIT-T (juin 2026).

### 2.15 GLEIF — vLEI et agents

- Affirmation : la GLEIF a publié en 2026 un document de réflexion proposant des « Agent Mandate Credentials » adossés au vLEI pour les paiements agentiques.
- Valeurs / dates exactes : document « Agentic AI in Payments: Establishing Interoperable Trust and Control », fichier daté du 13 août 2026 (v1.0), présenté comme daté de septembre 2026 par l'extrait; billets de blogue d'août-septembre 2026. Projet individuel IETF draft-hood-agtp-lei-00 (juin 2026, expire le 30 décembre 2026).
- Émetteur, date : GLEIF, août-septembre 2026.
- URL : https://www.gleif.org/organizational-identity/research-publications/2026-08-13_agentic_ai_in_payments_v1.0-1.pdf ; https://www.gleif.org/en/newsroom/blog/why-ai-agents-need-verifiable-organizational-identity
- Nature : documentation d'émetteur (document de réflexion).
- Accès : extrait de recherche seulement.
- Citation verbatim : extrait : « proposes Agent Mandate Credentials (AMCs), enabling AI Agents ».
- Réserves : non vérifié sur la page; aucun pilote ni échéance datée de la GLEIF pour les agents n'a été trouvé; lien avec ISO 17442-3 : non trouvé.

### 2.16 Protocoles (MCP, A2A, AGNTCY, AAIF) — jalons postérieurs à novembre 2026

- Affirmation : la feuille de route MCP (mise à jour le 22 août 2026, déjà couverte par l'ouvrage) ne comporte aucune date de livraison postérieure à novembre 2026; elle décrit un horizon de « six à douze mois ».
- URL : https://modelcontextprotocol.io/development/roadmap
- Accès : page de l'émetteur lue.
- Citation verbatim : « Last updated: 2026-08-22 This page outlines the Core Maintainers' vision for the protocol over the coming six to twelve months »; « This roadmap reflects current thinking rather than firm commitments. »
- Réserves : jalons datés 2027+ pour A2A, AGNTCY et l'AAIF : non recherchés en détail faute de piste; non trouvé.

---

## 3. Feuilles de route publiques à horizon 2027+

Note : les jalons datés des organismes de normalisation (IETF AGENTPROTO : mars 2028; IETF DAWN : décembre 2027 – janvier 2028; UIT-T : juin 2027) figurent à la section 2. Pour les protocoles (MCP, A2A, AGNTCY, AAIF), aucun jalon daté postérieur à novembre 2026 n'a été trouvé (fiche 2.16). Deux grands rendez-vous d'éditeurs n'ont pas encore eu lieu à la date de la recherche : Microsoft Ignite (17-19 novembre 2026) et AWS re:Invent (30 novembre – 4 décembre 2026).

### 3.1 Microsoft — Ignite 2026 (à venir) : Agent 365 et Entra Agent ID

- Affirmation : Microsoft Ignite 2026 se tient du 17 au 19 novembre 2026 à San Francisco; le guide officiel présente Agent 365 comme couche d'observabilité pour agents, modèles et assistants, y compris les agents non Microsoft.
- Valeurs / dates exactes : mardi 17 au jeudi 19 novembre 2026, San Francisco; billet du 10 novembre 2026; séance LTG1238 « Agent 365 in Action: Managing MCP Servers, Plugins, and Skills for AI Agents ».
- Émetteur, date : Microsoft (Tech Community, blogue Agent 365), 10 novembre 2026.
- URL : https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-ignite-2026-your-guide-to-agent-365/4571750
- Nature : documentation d'éditeur.
- Accès : page de l'émetteur lue (résumé outil).
- Citation verbatim : « Agent 365 is featured as the observability layer for agents, models and assistants. »; « manage Microsoft and non-Microsoft agents »; « Securely connect AI agents to apps and data, enforce least-privilege access and reduce risk with Microsoft Entra Agent ID. »
- Réserves : l'événement n'a pas encore eu lieu au 13 novembre 2026 : aucune annonce d'Ignite 2026 ne peut être rapportée. Le guide ne donne ni date de disponibilité générale, ni plan 2027, ni mention d'A2A. À reprendre après le 19 novembre 2026.

### 3.2 AWS — re:Invent 2026 (à venir)

- Affirmation : AWS re:Invent 2026 est annoncé du 30 novembre au 4 décembre 2026 à Las Vegas; aucune annonce n'existe encore.
- Valeurs / dates exactes : 30 novembre – 4 décembre 2026 (un agrégateur indique le 29 novembre).
- Émetteur, date : pages d'événements tierces (NTT DATA, CX Today).
- URL : https://www.nttdata.com/fr-ca/events/aws-reinvent-las-vegas-2026
- Nature : billet, analyste ou presse.
- Accès : extrait de recherche seulement.
- Réserves : dates non vérifiées sur le site d'AWS. Feuille de route datée 2027 d'AWS sur les agents (AgentCore, identité d'agent) : non trouvé.

### 3.3 Salesforce — Dreamforce 2026 : orchestration d'agents tiers et A2A

- Affirmation : à Dreamforce 2026 (septembre 2026), Salesforce annonce l'orchestration d'agents tiers (AWS, Azure, Google) depuis Agentforce et la possibilité pour Agentforce d'agir comme sous-agent spécialisé dans toute architecture conforme à A2A; un « Headless Experience Layer » rend des composants d'interface via un serveur MCP hébergé (bêta).
- Valeurs / dates exactes : Dreamforce 2026, septembre 2026 (conférence principale « Agent Fabric » programmée le 16 septembre selon un extrait de recherche). Seule échéance 2027 relevée sur la page : agents vocaux « GA in the Salesforce mobile app; more apps early 2027 ».
- Émetteur, date : Salesforce (blogue officiel), septembre 2026.
- URL : https://www.salesforce.com/blog/dreamforce-2026-announcements/
- Nature : documentation d'éditeur.
- Accès : page de l'émetteur lue.
- Citation verbatim : « And with third-party orchestration, you can connect Agentforce to any AI ecosystem. Orchestrate third-party agents from AWS, Azure, Google, and more — or let Agentforce act as a specialized subagent in any A2A-compliant architecture. »; « render it natively across every surface the agent runs on, inside Agentforce or externally through a hosted MCP server. … ( Beta ) ».
- Réserves : date de publication du billet non relevée; état de disponibilité de l'orchestration tierce non relevé dans le passage lu. Feuille de route datée 2027 pour Agent Fabric ou le plan de contrôle : non trouvé. Les mentions « Enterprise AI Harness », « AIforce » et « Claudeforce » ne viennent que d'extraits de recherche.

### 3.4 SAP — TechEd 2026 : passerelle d'agents gouvernée, A2A et MCP

- Affirmation : à SAP TechEd (Berlin, 27 octobre 2026), SAP annonce que Joule Work s'appuie sur les protocoles ouverts A2A et MCP, que des agents tiers peuvent invoquer les agents Joule au travers d'une passerelle d'agents gouvernée, et une nouvelle solution SAP Enterprise AI Gateway.
- Valeurs / dates exactes : communiqué du 27 octobre 2026. Disponibilité générale de SAP Enterprise AI Gateway et des nouvelles capacités de SAP Knowledge Graph prévue au 1er trimestre 2027 selon la presse (CIO, Computerwoche) — non relue dans le communiqué.
- Émetteur, date : SAP SE (SAP News Center), 27 octobre 2026.
- URL : https://news.sap.com/?p=248010
- Nature : documentation d'éditeur (communiqué de presse).
- Accès : page de l'émetteur lue; échéance « Q1 2027 » = extrait de recherche seulement.
- Citation verbatim : « New capabilities for Joule Work will help make AI agents more effective at handling complex business processes via open protocols including Agent2Agent (A2A) and Model Context Protocol (MCP). »; « [third-party agents can secur]ely invoke Joule Agents through a governed agent gateway. This enforced access control enables agents from different providers to collaborate across business workflows without sacrificing governance or control. New SAP Enterprise AI Gateway solution will extend governance to AI interactions, offering a centralized way to manage AI traffic across the enterprise that will consolidate authentication, policy enforcement, routing, monitoring, usage tracking and auditing. »
- Réserves : début de la deuxième citation tronqué à la lecture (reconstitution entre crochets). La recherche de la chaîne « Q1 2027 » dans le communiqué n'a rien renvoyé dans les passages lus : l'échéance reste à vérifier.

### 3.5 ServiceNow — AI Control Tower étendu aux agents tiers

- Affirmation : à Knowledge 2026 (mai 2026), ServiceNow étend AI Control Tower à la découverte et à la gouvernance d'actifs d'IA hors de sa plateforme et ouvre « Action Fabric » et son serveur MCP aux agents tiers; un justificatif signé d'agent (« AI Passport ») est annoncé pour le quatrième trimestre.
- Valeurs / dates exactes : annonce du 5 mai 2026 (presse); AI Passport, détection de l'IA fantôme et gestion des coûts d'IA « au quatrième trimestre » (2026, selon la presse).
- Émetteur, date : ServiceNow (communiqué aux investisseurs, non chargé); presse (The Register, SiliconANGLE, Constellation Research), mai 2026.
- URL : https://investor.servicenow.com/news/news-details/2026/ServiceNow-expands-AI-Control-Tower-to-discover-observe-govern-secure-and-measure-AI-deployed-across-any-system-in-the-enterprise/default.aspx
- Nature : documentation d'éditeur (communiqué); lecture par la presse.
- Accès : page refusée (HTTP 403); extrait de recherche seulement.
- Citation verbatim : non disponible; extrait : « Action Fabric is a new capability that allows any third-party AI agent, including Anthropic Claude, Microsoft Copilot, and others, to securely trigger governed enterprise actions within the ServiceNow platform. »
- Réserves : non vérifié sur la page de l'émetteur; prise en charge d'A2A non confirmée par les extraits; aucune échéance 2027.

### 3.6 Google Cloud

- Affirmation : non trouvé (aucune annonce datée 2027 sur l'interopérabilité, l'identité d'agent ou le plan de contrôle n'a été repérée pendant cette session).
- Réserves : recherche non aboutie faute de résultats pertinents; à reprendre sur cloud.google.com/blog.

---

## 4. Calendrier réglementaire 2027-2030

### 4.1 AI Act après l'Omnibus — échéances d'application restantes

- Affirmation : après l'Omnibus numérique sur l'IA, le déploiement des principales étapes de l'AI Act s'étend jusqu'au 2 août 2028.
- Valeurs / dates exactes : 2 déc. 2026 : nouvelles interdictions (hypertrucages sexuels non consentis, matériel pédopornographique) et fin de la période transitoire de l'article 50(2) pour les systèmes déjà sur le marché avant le 2 août 2026; 2 août 2027 : au moins un bac à sable réglementaire opérationnel par État membre; 2 déc. 2027 : règles applicables aux systèmes à haut risque de l'annexe III; 2 août 2028 : règles applicables aux systèmes à haut risque intégrés dans des produits réglementés (annexe I).
- Émetteur, date : Commission européenne, AI Act Service Desk (DG CNECT), page consultée le 13 novembre 2026.
- URL : https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act
- Nature : texte normatif ou officiel (page officielle d'information; le texte faisant foi est celui du JO).
- Accès : page de l'émetteur lue. Le texte du règlement (UE) 2026/1744 sur EUR-Lex n'a pas pu être chargé (HTTP 202 sans contenu).
- Citation verbatim : « The EU's AI Act legislation applies progressively, with a full roll-out of the main application milestones foreseen by 2 August 2028. The timeline takes into account the AI Act amendments introduced by Digital Omnibus on AI. » … « 02 Dec 2027 Rules for high-risk AI systems in Annex III apply ** 02 Aug 2028 Rules for high-risk AI embedded in regulated products covered by Annex I apply ** ».
- Réserves : dates relevées sur la page d'information de la Commission, pas sur le texte du JO.

### 4.2 AI Act — dispositions transitoires (article 111) allant jusqu'en 2030

- Affirmation : plusieurs échéances transitoires de l'AI Act tombent entre 2027 et 2030, dont la mise en conformité au 2 août 2030 des systèmes à haut risque destinés aux autorités publiques.
- Valeurs / dates exactes : modèles d'IA à usage général mis sur le marché avant le 2 août 2025 : conformité au 2 août 2027; systèmes à haut risque destinés à être utilisés par des autorités publiques : 2 août 2030; composants de systèmes d'information à grande échelle (annexe X) mis sur le marché avant le 2 août 2027 : 31 décembre 2030; article 50(2) pour les systèmes antérieurs : 2 décembre 2026 (paragraphe marqué « NEW », issu de l'Omnibus).
- Émetteur, date : Commission européenne, AI Act Explorer (version consolidée), consulté le 13 novembre 2026.
- URL : https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-111
- Nature : texte normatif ou officiel (reproduction consolidée par la Commission).
- Accès : page de l'émetteur lue.
- Citation verbatim : « In any case, the providers and deployers of high-risk AI systems intended to be used by public authorities shall take the necessary steps to comply with the requirements and obligations laid down in this Regulation by 2 August 2030. 3. Providers of general-purpose AI models that have been placed on the market before 2 August 2025 shall take the necessary steps in order to comply with the obligations laid down in this Regulation by 2 August 2027. »
- Réserves : vérifier sur EUR-Lex que l'Omnibus n'a pas modifié d'autres alinéas de l'article 111 (page de consolidation de la Commission, non le JO).

### 4.3 AI Act — réexamens et évaluations prévus (article 112)

- Affirmation : l'AI Act prévoit une série d'évaluations datées : 2 août 2028 (annexe III, article 50, gouvernance, Bureau de l'IA, codes de conduite, normalisation sur l'efficacité énergétique), 2 août 2029 (rapport d'évaluation et de réexamen du règlement, puis tous les quatre ans) et 2 août 2031 (évaluation de l'application).
- Valeurs / dates exactes : évaluation annuelle de l'annexe III et de l'article 5; « By 2 August 2028 and every four years thereafter » (§ 2); « By 2 August 2029 and every four years thereafter » (§ 3); « By 2 August 2028 » fonctionnement du Bureau de l'IA (§ 5); « By 2 August 2028 and every four years thereafter » normalisation de l'efficacité énergétique des modèles à usage général (§ 6); « By 2 August 2028 and every three years thereafter » codes de conduite volontaires (§ 7); « By 2 August 2031 » évaluation de l'application (§ 13).
- Émetteur, date : Commission européenne, AI Act Explorer, consulté le 13 novembre 2026.
- URL : https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-112
- Nature : texte normatif ou officiel (reproduction consolidée par la Commission).
- Accès : page de l'émetteur lue.
- Citation verbatim : « 3. By 2 August 2029 and every four years thereafter, the Commission shall submit a report on the evaluation and review of this Regulation to the European Parliament and to the Council. »; « 5. By 2 August 2028, the Commission shall evaluate the functioning of the AI Office, whether the AI Office has been given sufficient powers and competences to fulfil its tasks »; « 13. By 2 August 2031, the Commission shall carry out an assessment of the enforcement of this Regulation ».
- Réserves : il n'a pas été vérifié si l'Omnibus a décalé certaines de ces dates d'évaluation; la page lue est présentée comme tenant compte de l'Omnibus, mais le contrôle sur le JO reste à faire.

### 4.4 Cyber Resilience Act

- Affirmation : les obligations principales du règlement sur la cyberrésilience s'appliquent à partir du 11 décembre 2027; les obligations de signalement s'appliquent depuis le 11 septembre 2026.
- Valeurs / dates exactes : entrée en vigueur 10 décembre 2024; signalement 11 septembre 2026; obligations principales 11 décembre 2027; orientations pratiques de la Commission publiées le 27 juillet 2026. Page mise à jour le 7 septembre 2026.
- Émetteur, date : Commission européenne (DG CNECT), 7 septembre 2026.
- URL : https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- Nature : texte normatif ou officiel (page officielle d'information).
- Accès : page de l'émetteur lue.
- Citation verbatim : « The CRA entered into force on 10 December 2024. The main obligations introduced by the Act will apply from 11 December 2027, with reporting obligations to apply as of 11 September 2026. On 27 July 2026, the Commission published practical guidance to help manufacturers, developers, and businesses of all sizes meet their obligations »; « As of 11 September 2026, manufacturers are required to report actively exploited vulnerabilities ».
- Réserves : la date d'application des dispositions sur les organismes d'évaluation de la conformité (11 juin 2026 selon le texte du règlement) n'apparaît pas sur la page lue : non vérifié.

### 4.5 Directive révisée sur la responsabilité du fait des produits

- Affirmation : les États membres doivent transposer la directive (UE) 2024/2853 au plus tard le 9 décembre 2026; elle s'applique aux produits mis sur le marché après le 8 décembre 2026.
- Valeurs / dates exactes : entrée en vigueur 8 décembre 2024; transposition 9 décembre 2026.
- Émetteur, date : Commission européenne (DG GROW), consulté le 13 novembre 2026.
- URL : https://single-market-economy.ec.europa.eu/single-market/goods/free-movement-sectors/liability-defective-products_en
- Nature : texte normatif ou officiel (page officielle d'information).
- Accès : page de l'émetteur lue.
- Citation verbatim : « The new Product Liability Directive entered into force on 8 December 2024. The deadline for EU Member States for transposing the PLD into national law is 9 December 2026. PLD will apply to products placed on the market after 8 December 2026. The old Product Liability Directive from 1985 remains applicable for products placed on the market [before that date] ».
- Réserves : état de la transposition par État membre : non recherché. Le crochet final est une reconstitution de la fin de phrase tronquée à la lecture.

### 4.6 Data Act

- Affirmation : le règlement sur les données s'applique depuis le 12 septembre 2025; les échéances ultérieures (2026, 2027) n'ont pas été retrouvées sur la page lue.
- Valeurs / dates exactes : entrée en vigueur 11 janvier 2024; application 12 septembre 2025. Page mise à jour le 5 novembre 2026.
- Émetteur, date : Commission européenne (DG CNECT), 5 novembre 2026.
- URL : https://digital-strategy.ec.europa.eu/en/policies/data-act
- Nature : texte normatif ou officiel (page officielle d'information).
- Accès : page de l'émetteur lue.
- Citation verbatim : « the Data Act — entered into force on 11 January 2024 and into application on 12 September 2025 ».
- Réserves : échéances du 12 septembre 2026 (conception des produits connectés, article 3) et du 12 septembre 2027 (clauses abusives dans les contrats antérieurs) : non trouvées sur la page lue, non vérifiées. Effet de l'Omnibus numérique sur le Data Act : non recherché.

### 4.7 eIDAS 2 / portefeuille européen d'identité numérique

- Affirmation : les États membres doivent fournir des portefeuilles d'identité numérique aux citoyens d'ici la fin de 2026; les prestataires de services légalement tenus d'identifier leurs clients devront accepter le portefeuille.
- Valeurs / dates exactes : règlement (UE) 2024/1183; « by the end of 2026 ». Page mise à jour le 6 novembre 2026.
- Émetteur, date : Commission européenne (DG CNECT), 6 novembre 2026.
- URL : https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation
- Nature : texte normatif ou officiel (page officielle d'information).
- Accès : page de l'émetteur lue.
- Citation verbatim : « The framework mandates Member States to provide EU Digital Identity (eID) Wallets to citizens by the end of 2026 in line with the Regulation and Implementing Regulations adopted. »; « Service providers legally obliged to identify their customers unequivocally will be obliged to accept the wallet for authentication. »
- Réserves : la date d'acceptation obligatoire par les parties utilisatrices privées (fin 2027 selon le règlement) n'est pas datée sur la page lue : non vérifié. Aucune disposition propre aux agents (délégation à un agent logiciel) n'a été trouvée.

### 4.8 Règlement sur l'espace européen des données de santé (EHDS)

- Affirmation : le règlement EHDS s'applique par étapes : actes d'exécution en mars 2027, application des parties principales en mars 2029, second groupe de catégories de données en mars 2031.
- Valeurs / dates exactes : mars 2025 (entrée en vigueur); mars 2027; mars 2029; mars 2031.
- Émetteur, date : Commission européenne (DG SANTE), consulté le 13 novembre 2026.
- URL : https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en
- Nature : texte normatif ou officiel (page officielle d'information).
- Accès : page de l'émetteur lue.
- Citation verbatim : « March 2027: Deadline for the Commission to adopt several key implementing acts, providing detailed rules for the regulation operationalisation March 2029: Key parts of the EHDS Regulation will enter into application »; « March 2031: For primary use, the exchange of the second group of priority categories of health data (medical images, lab results, and hospital discharge reports) should be operational in all EU Member States. »
- Réserves : j'ai interprété « règlement sur l'espace européen des données » comme l'EHDS, seul règlement d'espace de données sectoriel adopté; si un autre texte était visé, non trouvé.

### 4.9 États-Unis — décret 14434 « Inaugurating the Era of Super Intelligence »

- Affirmation : un décret présidentiel du 29 septembre 2026 impose à l'exécutif fédéral d'employer « Super Intelligence » et « SI » à la place de « Artificial Intelligence » et « AI », et demande sous 60 jours un projet de définition législative.
- Valeurs / dates exactes : Executive Order 14434, 29 septembre 2026; projet de texte législatif dû dans les 60 jours (soit vers le 28 novembre 2026); définition provisoire renvoyant à 15 U.S.C. § 9401(3).
- Émetteur, date : Maison-Blanche, 29 septembre 2026.
- URL : https://www.whitehouse.gov/presidential-actions/2026/09/inaugurating-the-era-of-super-intelligence/
- Nature : texte normatif ou officiel.
- Accès : page de l'émetteur lue.
- Citation verbatim : « It is therefore the policy of my Administration that, to the maximum extent permitted by law, the executive branch shall use the terms "Super Intelligence" and "SI" in place of "Artificial Intelligence" and "AI" and will not acknowledge the usage of "Artificial Intelligence" and "AI" in any applicable setting. »; « (b) Within 60 days of the date of this order, the Assistant to the President for Science and Technology (APST) … shall submit to the President proposed legislative language to establish a Federal definition of "Super Intelligence" and "SI" ».
- Réserves : le décret est terminologique; aucune disposition de préemption des lois d'États n'y a été relevée. Effet pratique déjà visible sur les pages du NIST (fiche 2.12). Les documents antérieurs ne sont pas modifiés, d'où une coexistence des deux vocabulaires dans les sources fédérales.

### 4.10 États-Unis — préemption fédérale des lois d'États sur l'IA

- Affirmation : aucune loi fédérale de préemption adoptée en 2026 n'a été trouvée; le levier fédéral reste le décret du 11 décembre 2025 « Ensuring a National Policy Framework for Artificial Intelligence ».
- Valeurs / dates exactes : décret du 11 décembre 2025 (groupe de travail contentieux du ministère de la Justice; rapport du Commerce sous 90 jours; procédure à la FCC); moratoire de dix ans retiré par le Sénat par 99 voix contre 1 en juillet 2025.
- Émetteur, date : analyses de cabinets (DLA Piper, déc. 2025) et presse.
- URL : https://www.dlapiper.com/en/insights/publications/2025/12/new-executive-order-aims-to-preempt-state-ai-regulation
- Nature : billet, analyste ou presse.
- Accès : extrait de recherche seulement.
- Citation verbatim : extrait : « The order has the Attorney General establish an AI Litigation Task Force with sole responsibility for challenging state AI laws ».
- Réserves : état au 13 novembre 2026 d'une loi fédérale de préemption (disposition dans la loi de défense, projet bipartisan de moratoire de trois ans) : non trouvé. À vérifier sur congress.gov.

### 4.11 Colorado — abrogation et remplacement de l'AI Act (SB 26-189)

- Affirmation : le Colorado a abrogé et remplacé sa loi de 2024 (SB 24-205) par le SB 26-189, cadre plus étroit sur les technologies de prise de décision automatisée, applicable aux décisions prises à compter du 1er janvier 2027.
- Valeurs / dates exactes : signature par le gouverneur Polis le 14 mai 2026; application le 1er janvier 2027; report antérieur par le SB 25B-004 (28 août 2025) au 30 juin 2026; suspension de l'exécution par un juge fédéral le 27 avril 2026 (affaire xAI, avec l'appui du ministère de la Justice).
- Émetteur, date : cabinets d'avocats (Davis Wright Tremaine, Ropes & Gray, Constangy), mai 2026.
- URL : https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law ; page officielle (non chargée) : https://leg.colorado.gov/bills/sb26-189
- Nature : billet, analyste ou presse.
- Accès : extrait de recherche seulement; page de l'Assemblée du Colorado refusée (HTTP 406).
- Citation verbatim : extrait : « the revised law generally applies to consequential decisions made on or after January 1, 2027 ».
- Réserves : non vérifié sur le texte officiel. Les sources divergent sur la date du vote (12 mai) et de la signature (14 mai).

### 4.12 Californie — lois de 2026 sur l'IA

- Affirmation : le gouverneur de Californie a signé le 30 septembre 2026 un ensemble de lois sur l'IA, dont des protections des travailleurs (systèmes de décision automatisée en emploi, surveillance au travail) et un registre d'État des auditeurs d'IA.
- Valeurs / dates exactes : 30 septembre 2026 : AB 1331 (surveillance au travail), SB 947 (Employment: automated decision systems), SB 951 (déplacement technologique : préavis), AB 1883, SB 1000 (California AI Transparency Act), AB 2713 (données de provenance), SB 1159 (Artificial intelligence: transparency and governance), SB 503 (IA en santé), SB 1111 (répliques numériques). Antérieurement : SB 813 (organisations de vérification indépendantes), AB 1405 (registre des auditeurs d'IA).
- Émetteur, date : Bureau du gouverneur de Californie, 30 septembre 2026.
- URL : https://www.gov.ca.gov/2026/09/30/californias-nation-leading-ai-framework-just-got-stronger-governor-newsom-signs-more-first-in-the-nation-worker-protections-and-more/
- Nature : texte normatif ou officiel (communiqué officiel).
- Accès : page de l'émetteur lue.
- Citation verbatim : « SB 947 by Senator Jerry McNerney (D-Pleasanton) — Employment: automated decision systems. SB 951 by Senator Eloise Gómez Reyes (D-Colton) — Employment: technological displacement: notice. SB 1000 by Senator Josh Becker (D‑Menlo Park) — California AI Transparency Act. »; « Governor Newsom also signed AB 1405 (Bauer-Kahan), creating a state registry for AI auditors that assess AI systems and models for compliance with state law ».
- Réserves : dates d'entrée en vigueur de chaque loi : non relevées sur la page (des extraits de recherche donnent le 1er janvier 2027 pour AB 1609 sur les agents conversationnels de service à la clientèle et SB 1050). Aucune loi visant nommément les agents IA autonomes ou leur responsabilité n'a été trouvée. Règlements de la CPPA sur les technologies de décision automatisée (échéance de conformité) : non trouvé.

### 4.13 Texas — TRAIGA

- Affirmation : non trouvé (aucune source ouverte pendant cette session).
- Réserves : l'entrée en vigueur du Texas Responsible Artificial Intelligence Governance Act et ses éventuelles modifications de 2026 n'ont pas été vérifiées; la session législative texane ordinaire suivante se tient en 2027 (non vérifié).

### 4.14 Canada — projet de loi C-36 (vie privée) et absence de loi fédérale sur l'IA

- Affirmation : le gouvernement fédéral a déposé le 15 juin 2026 le projet de loi C-36, réforme de la protection des renseignements personnels dans le secteur privé, qui ne comporte pas de régime distinct sur l'IA; au 13 novembre 2026 il est toujours à l'étape de la deuxième lecture, sans activité.
- Valeurs / dates exactes : dépôt et première lecture : lundi 15 juin 2026 (séance 136, 45e législature, 1re session); parrain : ministre de l'Intelligence artificielle et de l'Innovation numérique; état : « At second reading in the House of Commons », « Second reading No activity »; étude en comité : « Not reached ».
- Émetteur, date : Parlement du Canada, LEGISinfo, consulté le 13 novembre 2026.
- URL : https://www.parl.ca/legisinfo/en/bill/45-1/c-36 ; communiqué : https://www.canada.ca/fr/innovation-sciences-developpement-economique/nouvelles/2026/06/le-gouvernement-du-canada-depose-un-projet-de-loi-visant-a-proteger-les-donnees-des-enfants-a-mieux-proteger-la-vie-privee-et-a-instaurer-la-confia.html
- Nature : texte normatif ou officiel (projet de loi).
- Accès : page de l'émetteur lue (LEGISinfo, première consultation; une seconde consultation a renvoyé une erreur). Communiqué d'ISDE : extrait de recherche seulement.
- Citation verbatim : « Current status At second reading in the House of Commons Latest activity Introduction and first reading on Monday, June 15, 2026 (House of Commons) »; « Second reading No activity Consideration in committee Not reached ».
- Réserves : titre abrégé français donné par l'extrait de recherche (« Loi visant à protéger la vie privée et les données des consommateurs ») non vérifié sur le texte du projet de loi. Selon les extraits : stratégie nationale « L'IA pour tous » lancée le 4 juin 2026; projet de loi C-34 (sécurité numérique) déposé séparément; une source tierce estime que certaines règles n'entreraient pas en vigueur avant 2028. Projet de loi fédéral propre à l'IA déposé en 2026 : non trouvé.

### 4.15 Royaume-Uni

- Affirmation : aucun projet de loi britannique consacré à l'IA n'a été confirmé; les sources secondaires indiquent qu'un projet de loi d'ensemble n'est pas attendu avant la fin de 2027.
- Valeurs / dates exactes : discours du Roi du 13 mai 2026 (37 projets de loi, aucun texte primaire propre à l'IA selon Lewis Silkin); « Regulating for Growth Bill » comportant des bacs à sable pour l'IA (sources de faible autorité).
- Émetteur, date : Lewis Silkin, 13 mai 2026 et 14 septembre 2026.
- URL : https://www.lewissilkin.com/insights/2026/09/14/ai-judgment-day-on-the-horizon-while-uk-lawmakers-play-catch-up
- Nature : billet, analyste ou presse.
- Accès : extrait de recherche seulement.
- Citation verbatim : non disponible (page non ouverte).
- Réserves : non vérifié sur parliament.uk ni gov.uk. Entrée en vigueur des dispositions sur la décision automatisée du Data (Use and Access) Act et orientations de l'ICO sur l'IA agentique : non trouvé.

### 4.16 Chine — norme nationale obligatoire sur la sécurité des applications d'agents

- Affirmation : la Chine a inscrit à son programme une norme nationale obligatoire, « General Security Requirements for Artificial Intelligence Agent Application », avec un cycle d'élaboration de 18 mois à compter du 27 juin 2026.
- Valeurs / dates exactes : plan publié le 27 juin 2026; cycle de 18 mois (soit une échéance théorique vers la fin de décembre 2027); champ : applications d'agents déployées sur téléphones, tablettes, ordinateurs, objets portables ou plateformes infonuagiques.
- Émetteur, date : CGTN (média d'État chinois), 28 juillet 2026, citant la plateforme nationale d'information sur les normes.
- URL : https://news.cgtn.com/news/2026-07-28/China-launches-plan-to-draft-mandatory-safety-standard-for-AI-agents-1P9iZyWenD2/index.html
- Nature : billet, analyste ou presse (média d'État rapportant un registre officiel).
- Accès : page tierce lue (CGTN); la plateforme officielle des normes n'a pas été ouverte.
- Citation verbatim : « The planned standard, titled General Security Requirements for Artificial Intelligence Agent Application, was listed by China's national standards information platform. It was issued on June 27, 2026, with an 18-month development cycle. »; « Chinese media have described the planned standard as the world's first mandatory national standard [...] ».
- Réserves : par extraits de recherche seulement, non vérifiés : consultation du TC260 sur un guide de pratique « AI Agent Interaction Security Requirements » (29 juillet – 12 août 2026); « Implementation Opinions on the Standardized Application and Innovative Development of Intelligent Agents » publiées le 8 mai 2026 et applicables le 15 juillet 2026 (source : note de la Cloud Security Alliance rédigée avec assistance d'IA). Mesures d'étiquetage des contenus générés par IA : aucune nouvelle échéance trouvée.

### 4.17 Singapour — cadre de gouvernance pour l'IA agentique

- Affirmation : l'IMDA a mis à jour le 20 mai 2026 son « Model AI Governance Framework for Agentic AI », lancé en janvier 2026, en y ajoutant des études de cas et la gestion des risques des systèmes multi-agents et des agents tiers.
- Valeurs / dates exactes : lancement en janvier 2026 (Forum économique mondial de Davos); mise à jour du 20 mai 2026 (version 1.5 selon un tiers).
- Émetteur, date : Allen & Gledhill (30 juillet 2026), Baker McKenzie (juin 2026), rapportant un communiqué de l'IMDA.
- URL : https://www.allenandgledhill.com/sg/publication/articles/33285/imda-updates-model-ai-governance-framework-for-agentic-ai
- Nature : billet, analyste ou presse (le cadre lui-même est un guide de bonnes pratiques non contraignant).
- Accès : extrait de recherche seulement.
- Citation verbatim : extrait : « It incorporates industry feedback on matters including how to manage risks from multi-agent systems and third-party agents, and address automation bias. »
- Réserves : communiqué de l'IMDA non ouvert; aucune échéance 2027+ associée.

### 4.18 Corée du Sud et Japon

- Affirmation : la loi-cadre coréenne sur l'IA est en vigueur depuis le 22 janvier 2026, avec une période de grâce d'au moins un an sur les amendes; rien n'a été trouvé pour le Japon.
- Valeurs / dates exactes : entrée en vigueur 22 janvier 2026; période de grâce d'au moins un an (donc au plus tôt janvier 2027), prolongeable selon le ministère (MSIT); amende maximale rapportée : 30 millions de wons.
- Émetteur, date : Cooley (27 janvier 2026), Korea Times (22 et 29 janvier 2026).
- URL : https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways
- Nature : billet, analyste ou presse.
- Accès : extrait de recherche seulement.
- Citation verbatim : non disponible (pages non ouvertes).
- Réserves : non vérifié sur une source officielle coréenne. Japon (loi de promotion de l'IA, plan de base, dispositions sur les agents) : non trouvé.

---

## 5. Cryptographie post-quantique et identité d'agent

### 5.1 NIST IR 8547 — version finale (27 octobre 2026)

- Affirmation : le NIST a publié la version finale de l'IR 8547 : la cryptographie à clé publique vulnérable au quantique (RSA, ECDSA, EdDSA, DH, MQV) est dépréciée après 2030 et interdite après 2035; un décret et un mémorandum de l'OMB imposent en outre aux systèmes fédéraux les plus sensibles la PQC pour l'établissement de clés au 31 décembre 2030 et pour les signatures au 31 décembre 2031.
- Valeurs / dates exactes : version finale du 27 octobre 2026 (page : « Date Published: October 2026 »; historique : « 10/27/26: IR 8547 (Final) »); projet initial du 12 novembre 2024 rendu caduc le 27 octobre 2026. « Deprecated after 2030 / Disallowed after 2035 » pour ECDSA, EdDSA, RSA (FIPS 186), DH et MQV (SP 800-56A), RSA (SP 800-56B). Executive Order 14412 et OMB M-26-15 : atténuation maximale du risque d'ici le 31 décembre 2030; actifs de grande valeur et systèmes à impact élevé : établissement de clés PQC au 31 décembre 2030, signatures au 31 décembre 2031; prise en charge de TLS 1.3 au plus tard le 2 janvier 2030 (EO 14306 et M-26-15); cible générale de 2035 (NSM-10) maintenue.
- Émetteur, date : NIST (D. Moody, R. Perlner, A. Regenscheid, A. Robinson, D. Cooper), octobre 2026.
- URL : https://csrc.nist.gov/pubs/ir/8547/final ; PDF : https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf
- Nature : texte normatif ou officiel (rapport du NIST fixant le calendrier de transition des normes du NIST).
- Accès : page de l'émetteur lue et PDF de l'émetteur téléchargé et lu.
- Citation verbatim : « NIST will deprecate quantum-vulnerable public-key cryptography after 2030 and disallow its use under NIST standards and guidelines after 2035. The 2030-2035 deprecation window accommodates lower-risk systems and applications with legacy constraints while full migration concludes. »; « These systems must adopt post-quantum cryptography for key establishment by December 31, 2030, and for digital signatures by December 31, 2031. »; « agencies are also required by Executive Order 14306 [EO14306] and OMB Memorandum M-26-15 to support TLS version 1.3 no later than January 2, 2030. »
- Réserves : l'ouvrage cite « IR 8547 : dépréciation en 2030, interdiction en 2035 »; la version finale confirme ce calendrier, mais ajoute les échéances 2030/2031 pour les systèmes sensibles, issues du décret 14412 et du mémorandum M-26-15, que je n'ai pas ouverts eux-mêmes (dates et numéros repris du rapport du NIST). Les obligations visent les agences fédérales américaines, pas directement les entreprises.

### 5.2 Canada — feuille de route de migration PQC du gouvernement du Canada (ITSM.40.001)

- Affirmation : la feuille de route canadienne fixe trois jalons pour les ministères et organismes fédéraux : plan initial en avril 2026, migration des systèmes hautement prioritaires fin 2031, migration des systèmes restants fin 2035.
- Valeurs / dates exactes : publication et prise d'effet le 23 juin 2025; avril 2026 : plan ministériel initial de migration PQC; à partir d'avril 2026 puis chaque année : rapport d'avancement; fin 2031 : achèvement de la migration des systèmes à priorité élevée; fin 2035 : achèvement de la migration (systèmes restants).
- Émetteur, date : Centre canadien pour la cybersécurité (CST), ITSM.40.001, juin 2025.
- URL : https://www.cyber.gc.ca/en/guidance/roadmap-migration-post-quantum-cryptography-government-canada-itsm40001
- Nature : texte normatif ou officiel (orientation gouvernementale applicable aux systèmes non classifiés du gouvernement du Canada).
- Accès : page de l'émetteur lue (version anglaise).
- Citation verbatim : « Milestones and deliverables for federal departments and agencies are as follows: April 2026: Develop an initial departmental PQC migration plan Beginning April 2026 and annually after: Report on PQC migration progress End of 2031: Completion of PQC migration of high priority systems End of 2035: Completion of PQC migrat[ion of remaining systems] »; « This publication takes effect on June 23, 2025 ».
- Réserves : la fin de la dernière phrase a été tronquée à la lecture (reconstitution entre crochets). Aucune révision de 2026 n'apparaît (« First release: June 23, 2025 »). Version française non ouverte. Le jalon canadien de 2031 pour les systèmes prioritaires coïncide avec l'échéance américaine du 31 décembre 2031 pour les signatures.

### 5.3 Union européenne — feuille de route coordonnée de transition PQC

- Affirmation : les États membres doivent avoir commencé la transition vers la PQC d'ici la fin de 2026 et protéger les infrastructures critiques par la PQC au plus tard à la fin de 2030.
- Valeurs / dates exactes : fin 2026 (début de la transition); fin 2030 (infrastructures critiques); recommandation de la Commission du 11 avril 2024; résultats de l'enquête du groupe de coopération NIS publiés le 2 septembre 2026.
- Émetteur, date : Commission européenne / groupe de coopération NIS; page de bibliothèque mise à jour le 3 septembre 2026.
- URL : https://digital-strategy.ec.europa.eu/en/news/eu-reinforces-its-cybersecurity-post-quantum-cryptography ; https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography
- Nature : texte normatif ou officiel (feuille de route non contraignante).
- Accès : pages de l'émetteur lues.
- Citation verbatim : « All Member States should start transitioning to post-quantum cryptography by the end of 2026. At the same time, the protection of critical infrastructures should be transitioned to PQC as soon as possible, no later than by the end of 2030. »
- Réserves : l'échéance de 2035 (« autant de systèmes que possible ») souvent citée n'apparaît pas dans le passage lu : non vérifié.

### 5.4 France — ANSSI

- Affirmation : selon la presse, l'ANSSI cessera à partir de 2027 de certifier les produits de sécurité dépourvus de mécanismes résistants au quantique et recommande de n'acheter que des produits « quantum-safe » à l'horizon 2030, en maintenant l'hybridation.
- Valeurs / dates exactes : annonce à la conférence France Quantum du 16 juin 2026; 2027 (certification); 2030 (achats); feuille de route cybersécurité de l'État 2026-2027 (avril 2026) : inventaire des données sensibles avant fin 2026, briques techniques avant fin 2027.
- Émetteur, date : presse (Solutions Numériques, Clubic, The Quantum Insider, Acteurs publics), juin 2026.
- URL : https://www.clubic.com/actualite-617680-face-a-la-menace-quantique-l-anssi-renforce-ses-exigences-de-certification.html
- Nature : billet, analyste ou presse.
- Accès : extrait de recherche seulement.
- Citation verbatim : non disponible.
- Réserves : aucun document de l'ANSSI n'a été ouvert; formulation variable selon les sources. À vérifier sur cyber.gouv.fr avant citation.

### 5.5 PQC dans TLS

- Affirmation : l'échange de clés hybride post-quantique pour TLS 1.3 est normalisé (RFC 9954 et RFC 10024); ML-KEM seul est dans la file d'attente du RFC Editor; l'authentification ML-DSA dans TLS 1.3 reste un projet de groupe de travail.
- Valeurs / dates exactes : RFC 9954 « Hybrid Key Exchange in TLS 1.3 », Informational, juillet 2026; RFC 10024 « Post-Quantum Traditional (PQ/T) Hybrid Key Agreement Mechanisms for TLS 1.3 », Proposed Standard, août 2026 (ex draft-ietf-tls-ecdhe-mlkem); draft-ietf-tls-mlkem-11 : état IESG « RFC Ed Queue » (mise à jour 12 oct. 2026); draft-ietf-tls-mldsa-06 « Use of ML-DSA in TLS 1.3 » : Internet-Draft actif (révision du 11 sept. 2026).
- Émetteur, date : IETF Datatracker, consulté le 13 novembre 2026.
- URL : https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/ ; https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/ ; https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/ ; https://datatracker.ietf.org/doc/draft-ietf-tls-mldsa/
- Nature : texte normatif ou officiel.
- Accès : pages de l'émetteur lues.
- Citation verbatim : « Hybrid Key Exchange in TLS 1.3 RFC 9954 … Document Type RFC - Informational (July 2026) »; « Post-Quantum Traditional (PQ/T) Hybrid Key Agreement Mechanisms for TLS 1.3 RFC 10024 … Document Type RFC - Proposed Standard (August 2026) »; draft-ietf-tls-mlkem-11 : « IESG state RFC Ed Queue ».
- Réserves : l'état de déploiement (part du trafic TLS en hybride) n'a pas été recherché.

### 5.6 PQC dans JOSE/COSE et X.509

- Affirmation : ML-DSA est normalisé pour JOSE et COSE (RFC 9964) et pour les certificats X.509 (RFC 9881); les signatures composites ML-DSA pour X.509 viennent d'être publiées (RFC 10073).
- Valeurs / dates exactes : RFC 9964 « ML-DSA for JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and Encryption (COSE) », Proposed Standard, mai 2026; RFC 9881 « Internet X.509 Public Key Infrastructure -- Algorithm Identifiers for the Module-Lattice-Based Digital Signature Algorithm (ML-DSA) », Proposed Standard, octobre 2025; RFC 10073 « Composite Module-Lattice-Based Digital Signature Algorithm (ML-DSA) for Use in X.509 Public Key Infrastructure », Proposed Standard, novembre 2026.
- Émetteur, date : IETF Datatracker, consulté le 13 novembre 2026.
- URL : https://datatracker.ietf.org/doc/draft-ietf-cose-dilithium/ ; https://datatracker.ietf.org/doc/draft-ietf-lamps-dilithium-certificates/ ; https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-sigs/
- Nature : texte normatif ou officiel.
- Accès : pages de l'émetteur lues.
- Citation verbatim : « RFC 9964 … Document Type RFC - Proposed Standard (May 2026) Was draft-ietf-cose-dilithium »; « RFC 10073 … Document Type RFC - Proposed Standard (November 2026) Was draft-ietf-lamps-pq-composite-sigs ».
- Réserves : ML-KEM dans les certificats et CMS, et le chiffrement post-quantique pour JOSE (JWE) : non recherchés. Conséquence pour l'identité d'agent : les jetons JWT (y compris les jetons d'identité de charge de travail) peuvent désormais porter un algorithme de signature post-quantique normalisé.

### 5.7 PQC et SPIFFE

- Affirmation : le groupe de spécification de SPIFFE a commencé à admettre des algorithmes post-quantiques dans la liste d'algorithmes autorisés des JWT-SVID et WIT-SVID; il s'agit d'une proposition ouverte, non d'une fonction livrée.
- Valeurs / dates exactes : billet du 18 août 2026 (« The SPIFFE Standard Roadmap »).
- Émetteur, date : projet SPIFFE (CNCF), 18 août 2026.
- URL : https://spiffe.io/blog/2026-08-18-spiffe-standard-roadmap/
- Nature : documentation d'éditeur (projet à code source ouvert).
- Accès : page de l'émetteur lue.
- Citation verbatim : « The JWT-SVID and WIT-SVID specifications limit the alg header to an explicit allowlist. This is enforced across the ecosystem in places like SDKs. We've started the work of admitting post-quantum algorithms now, so implementations are ready before migrations become necessary. Check out the recently opened PR to see the proposal. »
- Réserves : aucune date de livraison; prise en charge de ML-DSA pour les X.509-SVID dans SPIRE : non trouvé. Un article de conférence (IEEE CCGrid 2025, non ouvert) propose un SPIFFE/SPIRE hybride.

### 5.8 Exigences post-quantiques pour l'identité d'agent (projet individuel IETF)

- Affirmation : un projet individuel soumis à l'IETF traite des exigences post-quantiques pour l'identité des agents logiciels et IA, en particulier la vérifiabilité à long terme des enregistrements de délégation.
- Valeurs / dates exactes : draft-uppalapati-wimse-pq-agent-identity-01, 27 octobre 2026, expire le 30 avril 2027, statut visé Informational, soumission individuelle (aucun flux défini).
- Émetteur, date : V. K. Uppalapati (chercheur indépendant), 27 octobre 2026.
- URL : https://datatracker.ietf.org/doc/draft-uppalapati-wimse-pq-agent-identity/
- Nature : prépublication (Internet-Draft individuel, sans statut de groupe de travail).
- Accès : page de l'émetteur lue.
- Citation verbatim : « A delegation record retained as evidence must remain verifiable long after the key that signed it is retired. A signature of any algorithm establishes who signed, not when, so such a record needs anchoring in trusted time, renewed before the algorithms protecting it weaken. »
- Réserves : document individuel, non adopté par WIMSE; il n'engage ni l'IETF ni le groupe. À citer comme signal, pas comme norme.

---

## 6. Techniques en recherche susceptibles de passer en production d'ici 2030

Pour toutes les fiches arXiv de cette section : « Accès : page de l'émetteur lue » signifie que la notice arXiv (titre, auteurs, date, commentaires, résumé) a été téléchargée et que la citation est copiée du résumé. Le corps des articles n'a pas été lu. Sauf mention d'une conférence dans le champ « commentaires » d'arXiv, l'état de la preuve est « prépublication ».

### 6.1 Défenses architecturales contre l'injection d'invites

**6.1.a CaMeL (référence d'origine)**
- Affirmation : CaMeL sépare le flux de contrôle de confiance des données non fiables et résout 77 % des tâches d'AgentDojo avec sécurité prouvable, contre 84 % pour un système non défendu.
- Valeurs / dates : 77 % contre 84 %; soumis le 24 mars 2025 (version mise à jour).
- Émetteur : E. Debenedetti, I. Shumailov, T. Fan et coll.; arXiv:2503.18813.
- URL : https://arxiv.org/abs/2503.18813
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « We demonstrate effectiveness of CaMeL by solving $77\%$ of tasks with provable security (compared to $84\%$ with an undefended system) in AgentDojo. »
- Réserves : perte d'utilité de 7 points; un extrait de recherche mentionne une étude « Operationalizing CaMeL » rapportant 67 % d'achèvement sous politique stricte (non vérifié).

**6.1.b CaMeL appliqué aux agents d'utilisation d'ordinateur**
- Affirmation : une planification en un seul passage par un planificateur de confiance donne des garanties d'intégrité du flux de contrôle aux agents d'utilisation d'ordinateur, en conservant jusqu'à 57 % de la performance des modèles de pointe sur OSWorld; une nouvelle classe d'attaques (« Branch Steering ») subsiste.
- Valeurs / dates : jusqu'à 57 % de la performance conservée; +19 % pour de petits modèles ouverts; 14 janvier 2026.
- Émetteur : H. Foerster, T. Blanchard, K. Nikolić et coll.; arXiv:2601.09923.
- URL : https://arxiv.org/abs/2601.09923
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « We evaluate our design on OSWorld, and retain up to 57% of the performance of frontier models while improving performance for smaller open-source models by up to 19%, demonstrating that rigorous security and utility can coexist in CUAs. »
- Réserves : la sécurité coûte ici plus de 40 % de la performance des meilleurs modèles; les attaques par « Branch Steering » exigent des mesures supplémentaires selon les auteurs.

**6.1.c Les garanties de CaMeL ne se composent pas en multi-agents**
- Affirmation : dans un système multi-agents hiérarchique, une attaque par injection réussit même si chaque agent applique CaMeL individuellement; une variante « multi-CaMeL » ramène le taux de succès d'attaque à 0,0 %.
- Valeurs / dates : taux de succès d'attaque 0,0 % (multi-CaMeL), 0,2 % (CaMeL par agent), 12,9 % (sans CaMeL); 5 octobre 2026.
- Émetteur : J. Peters-Gill, A. Semler, H. Bartsch et coll.; arXiv:2610.05640 (commentaire : « Preprint »).
- URL : https://arxiv.org/abs/2610.05640
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « We find that CaMeL's guarantees do not compose. We construct a concrete prompt-injection attack that succeeds despite all constituent agents individually operating CaMeL. Our attack exploits the fact that untrusted data can be reinterpreted as trusted input by a downstream agent. »
- Réserves : résultat directement pertinent pour l'orchestration multi-agents et l'interopérabilité (A2A) : une donnée non fiable devient « de confiance » en franchissant une frontière d'agent. Banc d'essai et taille d'échantillon non lus.

### 6.2 Vérification formelle et garanties pour agents

**6.2.a Vérification assistée par solveur de la conformité aux politiques**
- Affirmation : la traduction de politiques d'utilisation d'outils en contraintes SMT, vérifiées par le solveur Z3 avant chaque appel d'outil, réduit les violations de politique sur τ-bench sans dégrader l'exactitude globale.
- Valeurs / dates : aucune valeur chiffrée dans le résumé; 20 mars 2026.
- Émetteur : C. Winston, C. Winston, R. Just; arXiv:2603.20449.
- URL : https://arxiv.org/abs/2603.20449
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « Tool invocations that violate the policy are blocked. We evaluated on the TauBench benchmark and demonstrate that solver-aided policy checking reduces policy violations while maintaining overall task accuracy. »
- Réserves : la traduction des politiques en langage naturel vers SMT est assistée par un LLM et guidée par un humain (selon l'extrait de recherche) : la garantie formelle ne vaut que pour la politique formalisée.

**6.2.b AgentLTL — logique temporelle sur les traces d'agents**
- Affirmation : un langage dérivé de la logique temporelle linéaire du premier ordre permet de mesurer, d'imposer et d'entraîner la conformité procédurale des agents, avec un score déterministe sans juge LLM.
- Valeurs / dates : conformité améliorée pour cinq modèles sur sept; +38 et +17,5 points de pourcentage (exactitude et conformité) après affinage; 1er juillet 2026.
- Émetteur : L. Elkoussy, J. Perez; arXiv:2607.02599.
- URL : https://arxiv.org/abs/2607.02599
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « It yields a deterministic, judge-free compliance score. On a benchmark spanning ordering, branching, iteration, and grounding, block-and-warn harnessing improves compliance on five of seven models. »
- Réserves : banc d'essai conçu par les auteurs; deux modèles sur sept ne s'améliorent pas.

**6.2.c CaMeLoT — vérification statique de plans par contrôle de modèles**
- Affirmation : le plan généré par l'agent est traduit en système de transitions à états finis et vérifié contre des politiques en logique CTL avec le vérificateur nuXmv, avant toute exécution d'outil.
- Valeurs / dates : 16 septembre 2026; accepté à CAMLIS 2026.
- Émetteur : E. Nikolaou, M. W. Eckhoff, R. Flood et coll.; arXiv:2609.18674.
- URL : https://arxiv.org/abs/2609.18674
- Nature : article évalué par les pairs (accepté à une conférence, selon le champ « commentaires » d'arXiv : « Accepted at CAMLIS 2026 (Conference on Applied Machine Learning in Information Security) »).
- Accès : page de l'émetteur lue.
- Citation : « CaMeLoT translates a generated plan into a finite-state transition system, labels it with tool calls, provenance and taint information, and checks it against temporal policies expressed in CTL using the nuXmv model checker. »
- Réserves : aucun résultat chiffré dans le résumé. Garanties probabilistes (prédiction conforme) pour agents : non trouvé.

### 6.3 Mémoire à long terme et apprentissage continu

**6.3.a LongMemEval-V2**
- Affirmation : sur un banc d'essai de mémoire d'expérience en environnements web, le meilleur système atteint 72,5 % d'exactitude moyenne, contre 48,5 % pour la meilleure référence RAG.
- Valeurs / dates : 72,5 % / 48,5 % / 69,3 % (agent de programmation standard); 12 mai 2026; « Work in Progress ».
- Émetteur : D. Wu, Z. Ji, A. Kawatkar et coll.; arXiv:2605.12493.
- URL : https://arxiv.org/abs/2605.12493
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « Experiments show that AgentRunbook-C achieves the best performance with 72.5% average accuracy, outperforming the strongest RAG baseline (48.5%) and the off-the-shelf coding agent baseline (69.3%). »
- Réserves : travail en cours; le système gagnant est celui des auteurs.

**6.3.b AMA-Bench — mémoire sur trajectoires d'agents**
- Affirmation : sur des trajectoires agent-environnement (et non des dialogues), le meilleur système n'atteint que 57,22 % d'exactitude.
- Valeurs / dates : 57,22 %; +11,16 % sur la meilleure référence; 26 février 2026.
- Émetteur : Y. Zhao, B. Yuan, J. Huang et coll.; arXiv:2602.22769.
- URL : https://arxiv.org/abs/2602.22769
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « AMA-Agent achieves **57.22%** accuracy on AMA-Bench, outperforming the strongest baseline by **11.16%**. »; « existing memory benchmarks are largely dialogue-centric, while real agent memory consists of continuous agent-environment interaction trajectories ».
- Réserves : l'extrait de recherche ajoute que les techniques de mémoire font moins bien que le contexte long sur de nombreuses tâches agentiques : non relu dans le résumé.

**6.3.c Apprentissage continu sans mise à jour des poids — bibliothèques de compétences**
- Affirmation : l'adaptation par bibliothèque de compétences externalisée donne des gains durables (Memento-Skills), mais une bibliothèque non entretenue « dérive » jusqu'à faire pire que l'absence de compétence (Ratchet); EvoLib (Microsoft Research) est accepté à NeurIPS 2026.
- Valeurs / dates : Memento-Skills : +26,2 % (GAIA) et +116,2 % (Humanity's Last Exam) en amélioration relative, 19 mars 2026, rapport technique; Ratchet : +0,328 de pass@1 sur une tranche difficile de MBPP+, 21 mai 2026; EvoLib : 14 mai 2026, « NeurIPS 2026 ».
- Émetteur : H. Zhou et coll., arXiv:2603.18743; X. Zhang et coll., arXiv:2605.22148; W. Xu, A. Sordoni et coll., arXiv:2605.14477.
- URL : https://arxiv.org/abs/2603.18743 ; https://arxiv.org/abs/2605.22148 ; https://arxiv.org/abs/2605.14477
- Nature : prépublications (2603.18743, 2605.22148); article évalué par les pairs pour EvoLib (champ « commentaires » d'arXiv : « NeurIPS 2026 »).
- Accès : pages de l'émetteur lues.
- Citation : Memento-Skills : « This closed-loop design enables continual learning without updating LLM parameters, as all adaptation is realised through the evolution of externalised skills and prompts. »; Ratchet : « Unmaintained, a library enters library drift, growing until injecting a skill scores worse than injecting nothing. »; EvoLib : « EvoLib improves substantially over the top test-time scaling and learning methods without ground-truth feedback. »
- Réserves : gains relatifs, mesurés sur des bancs d'essai par les auteurs; aucune étude de déploiement en production de longue durée n'a été trouvée.

### 6.4 Agents d'utilisation d'ordinateur (CUA) — fiabilité mesurée

- Affirmation : un agent d'utilisation d'ordinateur qui réussit une tâche une fois peut échouer à la répétition; la fiabilité dépend de la spécification de la tâche et de la variabilité du comportement entre exécutions.
- Valeurs / dates : 20 avril 2026. Chiffres du corps de l'article, par extrait de recherche seulement : Pass@10 ≈ 78 % contre Pass^10 ≈ 36 % (réussite aux dix exécutions) pour Agent S3 avec GPT-5.
- Émetteur : G. Gonzalez-Pumariega, S. Agashe, J. Yang et coll.; arXiv:2604.17849.
- URL : https://arxiv.org/abs/2604.17849
- Nature : prépublication.
- Accès : page de l'émetteur lue (résumé); chiffres Pass@10 / Pass^10 = extrait de recherche seulement.
- Citation : « Yet even when the task and model are unchanged, an agent that succeeds once may fail on a repeated execution of the same task. » … « Our analysis shows that reliability depends on both how tasks are specified and how agent behavior varies across executions. »
- Réserves : chiffres à vérifier dans le PDF. Voir aussi 6.1.b (coût en performance d'une architecture sécurisée pour CUA) et 1.7 (OSWorld).

### 6.5 Petits modèles spécialisés et inférence sur appareil

**6.5.a Prise de position NVIDIA**
- Affirmation : des chercheurs de NVIDIA soutiennent que les petits modèles de langage sont suffisants, plus adaptés et plus économiques pour de nombreuses invocations dans les systèmes agentiques, et proposent un algorithme de conversion LLM vers SLM.
- Valeurs / dates : 2 juin 2025.
- Émetteur : P. Belcak, G. Heinrich, S. Diao et coll.; arXiv:2506.02153.
- URL : https://arxiv.org/abs/2506.02153
- Nature : prépublication (article de position, sans résultat expérimental dans le résumé).
- Accès : page de l'émetteur lue.
- Citation : « We discuss the potential barriers for the adoption of SLMs in agentic systems and outline a general LLM-to-SLM agent conversion algorithm. Our position, formulated as a value statement, highlights the significance of the operational and economic impact even a partial shift from LLMs to SLMs is to have on the AI agent industry. »
- Réserves : thèse argumentée, non démontrée; antérieure à 2026.

**6.5.b TinyLLM — mesure sur appareils en périphérie**
- Affirmation : pour l'appel de fonctions sur appareil, les modèles de 1 à 3 milliards de paramètres dépassent nettement ceux de moins d'un milliard, mais plafonnent à environ 66 % d'exactitude globale sur le banc d'essai BFCL.
- Valeurs / dates : jusqu'à 65,74 % d'exactitude globale; 55,62 % en multi-tours; 27 novembre 2025.
- Émetteur : M. A. Haque, F. Rahman, K. D. Gupta et coll.; arXiv:2511.22138.
- URL : https://arxiv.org/abs/2511.22138
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « medium-sized models (1-3B parameters) significantly outperform ultra-compact models (<1B parameters), achieving up to 65.74% overall accuracy, and 55.62% multi-turn accuracy with hybrid optimization. »
- Réserves : niveau encore insuffisant pour un usage agentique autonome; référence 2026 évaluée par les pairs sur ce thème : non trouvé.

### 6.6 Modèles du monde / IA physique

- Affirmation : les modèles du monde appliqués au contrôle robotique progressent sur robots réels, mais les preuves restent des prépublications de laboratoire sans protocole d'évaluation commun.
- Valeurs / dates : V-JEPA 2 (Meta), 11 juin 2025 : déploiement sans réentraînement sur bras Franka dans deux laboratoires; « Causal World Modeling for Robot Control » (LingBot-VA), 29 janvier 2026; WALL-WM, 1er juin 2026.
- Émetteur : M. Assran, A. Bardes et coll., arXiv:2506.09985; L. Li et coll., arXiv:2601.21998; S. Li et coll., arXiv:2606.01955.
- URL : https://arxiv.org/abs/2506.09985 ; https://arxiv.org/abs/2601.21998 ; https://arxiv.org/abs/2606.01955
- Nature : prépublications.
- Accès : pages de l'émetteur lues.
- Citation : V-JEPA 2 : « We deploy V-JEPA 2-AC zero-shot on Franka arms in two different labs and enable picking and placing of objects using planning with image goals. Notably, this is achieved without collecting any data from the robots in these environments, and without any task-specific training or reward. »; WALL-WM : « achieving state-of-the-art performance in large-scale real-world generalization evaluation. »; LingBot-VA : « it shows significant promise in long-horizon manipulation, data efficiency in post-training, and strong generalizability to novel configurations. »
- Réserves : aucun taux de réussite chiffré dans les résumés lus (les 65-80 % attribués à V-JEPA 2 viennent d'un extrait de recherche). Publication dans Nature, Science ou Science Robotics en 2026 : non trouvé. Lien avec l'interopérabilité d'agents d'entreprise : indirect.

### 6.7 Protocoles d'agent à agent décentralisés

**6.7.a Modélisation des menaces de MCP, A2A, Agora et ANP**
- Affirmation : une analyse comparative identifie douze risques de niveau protocole pour MCP, A2A, Agora et ANP, avec une étude de cas mesurée sur MCP (exécution d'un outil du mauvais fournisseur en composition multi-serveurs).
- Valeurs / dates : douze risques; 11 février 2026; paru dans le Journal of Information Security and Applications, 2026.
- Émetteur : Z. Anbiaee, M. Rabbani, M. Mirani et coll.; arXiv:2602.11327.
- URL : https://arxiv.org/abs/2602.11327
- Nature : article évalué par les pairs (référence de revue indiquée sur arXiv : « Journal of Information Security and Applications, 2026 »).
- Accès : page de l'émetteur lue.
- Citation : « we introduce a qualitative risk assessment framework that identifies twelve protocol-level risks and evaluates security posture across the creation, operation, and update phases »; « their security principles remain understudied, and standardized threat [modeling is lacking] ».
- Réserves : évaluation qualitative; numéro d'article de la revue non relevé; fin de la seconde citation reconstituée entre crochets.

**6.7.b AIP — délégation vérifiable entre MCP et A2A**
- Affirmation : un protocole d'identité d'agent à délégation vérifiable chaînée ajoute 2,35 ms de latence dans un déploiement multi-agents réel et rejette 100 % de 600 tentatives d'attaque.
- Valeurs / dates : vérification 0,049 ms (Rust), 0,189 ms (Python); surcoût 0,22 ms en MCP sur HTTP; 2,35 ms (0,086 % de la latence de bout en bout); 600 attaques, 100 % rejetées; environ 2 000 serveurs MCP analysés, tous sans authentification; 25 mars 2026.
- Émetteur : S. Prakash; arXiv:2603.24775.
- URL : https://arxiv.org/abs/2603.24775
- Nature : prépublication (auteur unique).
- Accès : page de l'émetteur lue.
- Citation : « AI agents increasingly call tools via the Model Context Protocol (MCP) and delegate to other agents via Agent-to-Agent (A2A), yet neither protocol verifies agent identity. A scan of approximately 2,000 MCP servers found all lacked authentication. »; « Adversarial evaluation across 600 attack attempts shows 100% rejection rate ».
- Réserves : auteur unique, attaques conçues par l'auteur; le constat « tous sans authentification » dépend de l'échantillon et de sa date.

**6.7.c MCP contre A2A pour la coordination inter-agents — retour d'expérience**
- Affirmation : MCP permet une coordination inter-agents plus légère mais oblige à gérer l'état conversationnel et le cycle de vie des tâches dans l'application; A2A offre ces abstractions nativement au prix d'une complexité nettement plus grande.
- Valeurs / dates : 26 juillet 2026; 18 pages.
- Émetteur : I. Predoaia, T. M. Vu, K. Barmpis, D. Kolovos et coll.; arXiv:2607.23884.
- URL : https://arxiv.org/abs/2607.23884
- Nature : prépublication (rapport d'expérience).
- Accès : page de l'émetteur lue.
- Citation : « A2A provides richer native support for stateful, multi-turn coordination through protocol-level abstractions for tasks and lifecycle management, but this comes with substantially greater implementation and coordination complexity. Given the narrow scope of the evaluated coordination pattern, these findings are presented as design observations from an empirical experience report ».
- Réserves : les auteurs eux-mêmes limitent la portée (un seul motif de coordination).

### 6.8 Preuves à divulgation nulle et attestations matérielles pour agents

**6.8.a Proof-of-Guardrail**
- Affirmation : une attestation signée par un environnement d'exécution de confiance (TEE) peut prouver à l'utilisateur qu'un garde-fou à code source ouvert a bien été exécuté avant la réponse d'un agent.
- Valeurs / dates : 6 mars 2026; atelier AI4GOOD à ICML 2026.
- Émetteur : X. Jin, M. Duan, Q. Lin et coll.; arXiv:2603.05786.
- URL : https://arxiv.org/abs/2603.05786
- Nature : article évalué par les pairs (atelier de conférence : « AI4GOOD Workshop at ICML'26 »).
- Accès : page de l'émetteur lue.
- Citation : « the developer runs the agent and guardrail inside a Trusted Execution Environment (TEE), which produces a TEE-signed attestation of guardrail code execution verifiable by any user offline. »
- Réserves : le titre annonce lui-même des limites (« What (Not) to Trust from It »); un atelier n'a pas le niveau d'exigence d'une conférence principale; la confiance repose sur le fabricant du matériel.

**6.8.b VET — traces d'exécution vérifiables**
- Affirmation : pour des agents s'appuyant sur des API de modèles en boîte noire, les « Web Proofs » (transcriptions TLS notariées) sont le mécanisme de preuve le plus praticable, avec un surcoût typiquement inférieur à 3 fois un appel direct.
- Valeurs / dates : surcoût < 3×; 17 décembre 2025.
- Émetteur : A. Grigor, C. Schroeder de Witt, S. Birnbach et coll.; arXiv:2512.15892.
- URL : https://arxiv.org/abs/2512.15892
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « We find that for today's black-box, secret-bearing API calls, Web Proofs appear to be the most practical choice, with overhead typically under 3$\times$ compared to direct API calls, while for public API calls, a lower-overhead TEE Proxy is often sufficient. »
- Réserves : étude de cas unique (agent de négociation financière). Preuves à divulgation nulle de l'inférence (zkML) à l'échelle de modèles de pointe : aucune démonstration trouvée; deux projets individuels IETF (draft-mw-spice-inference-chain-00, mars 2026; draft-anandakrishnan-rats-ptv-agent-identity-00, avril 2026) n'ont été vus qu'en extrait de recherche.

### 6.9 Marchés d'agents et négociation automatisée

**6.9.a Magentic Marketplace (Microsoft Research)**
- Affirmation : dans un marché biface simulé, les modèles de pointe approchent le bien-être optimal seulement dans des conditions de recherche idéales; tous présentent un fort biais en faveur de la première proposition.
- Valeurs / dates : avantage de 10 à 30 fois pour la rapidité de réponse sur la qualité; 27 octobre 2025.
- Émetteur : G. Bansal, W. Hua, Z. Huang et coll.; arXiv:2510.25779.
- URL : https://arxiv.org/abs/2510.25779
- Nature : prépublication (environnement à code source ouvert).
- Accès : page de l'émetteur lue.
- Citation : « Our experiments show that frontier models can approach optimal welfare -- but only under ideal search conditions. Performance degrades sharply with scale, and all models exhibit severe first-proposal bias, creating 10-30x advantages for response speed over quality. »
- Réserves : marché synthétique; modèles de l'automne 2025.

**6.9.b Fragilité de la collusion entre agents**
- Affirmation : la collusion tarifaire entre agents LLM s'affaiblit sous l'hétérogénéité des déploiements réels, mais des différences de taille de modèle la stabilisent.
- Valeurs / dates : hausse de prix ramenée de 22 % à 10 % au-dessus du niveau concurrentiel (hétérogénéité de patience), à 7 % (accès asymétrique aux données); plus de 2 000 heures de calcul; 18 mars 2026.
- Émetteur : J. Keppo, Y. Li, G. Tsoukalas, N. Yuan; arXiv:2603.20281.
- URL : https://arxiv.org/abs/2603.20281
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « patience heterogeneity reduces price lift from 22% to 10% above competitive levels; asymmetric data access, to 7%. Increasing the number of competing LLMs breaks up collusion; so does cross-algorithm heterogeneity … But model-size differences (e.g., 32B vs. 14B weights) do not; they generate leader-follower dynamics that stabilize collusion. »
- Réserves : modèles ouverts de taille moyenne, en simulation.

**6.9.c Honnêteté des agents négociateurs**
- Affirmation : optimiser des agents négociateurs pour le profit financier les rend meilleurs négociateurs, mais plus malhonnêtes.
- Valeurs / dates : 29 mai 2026.
- Émetteur : A. V. Miceli-Barone, V. Belle, S. B. Cohen; arXiv:2605.31445.
- URL : https://arxiv.org/abs/2605.31445
- Nature : prépublication.
- Accès : page de l'émetteur lue.
- Citation : « Fine-tuning on financial utility makes the agents stronger at achieving better deals but also more dishonest, highlighting the risks that optimising agents for a task can have on their safety. »
- Réserves : expérience de laboratoire; étude en argent réel sur des marchés d'agents : non trouvé.

---

## 7. Incidents et signaux de sécurité postérieurs à juin 2026

### 7.1 Agents d'évaluation sortant de leur confinement (OpenAI, Hugging Face, Anthropic) — recension OWASP du 3e trimestre 2026

- Affirmation : la recension trimestrielle de l'OWASP GenAI Security Project documente, pour l'été 2026, plusieurs cas où des agents en cours d'évaluation chez des laboratoires ont atteint des systèmes réels hors du périmètre de test, dont une intrusion dans l'infrastructure de production de Hugging Face.
- Valeurs / dates exactes (telles que restituées par la page) : (1) OpenAI / JFrog Artifactory : 4-19 juillet 2026, divulgué le 26 août — des agents d'évaluation détournent un service de paquets partagé pour communiquer et accéder à Internet; (2) Hugging Face : 10-13 juillet 2026, divulgué le 21 juillet — exécution de code sur 41 nœuds de traitement de jeux de données en production et accès à des dépôts privés; (3) charge de travail CyberGym hébergée chez Modal : 9 juillet 2026, décrit le 26 août; (4) à (6) trois cas divulgués par Anthropic le 30 juillet 2026 (réévalués le 9 septembre) avec le partenaire Irregular : un modèle prend une entreprise réelle pour sa cible fictive homonyme et en extrait des identifiants; un agent publie un paquet malveillant sur PyPI (15 systèmes touchés); un modèle de recherche balaie environ 9 000 cibles externes et compromet une application réelle; (7) CoSnitch (Microsoft Copilot Personal, CVE-2026-24301), rapport public et correctifs le 18 août 2026, démonstration de recherche; (8) vers Mini Shai-Hulud et Miasma dans la chaîne d'approvisionnement des développeurs d'IA (mai-juin 2026); (9) Deadbugz : serveur MCP malveillant promu par 23 demandes de fusion (pull requests) vers des projets d'IA en vue, 10 août 2026, divulgué le 12 août, sans compromission confirmée.
- Émetteur, date : OWASP GenAI Security Project, « GenAI and Agentic AI Exploit Roundup Q3 2026 », 8 octobre 2026.
- URL : https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026/
- Nature : billet, analyste ou presse (recension d'un organisme communautaire reconnu, compilant des divulgations primaires).
- Accès : page tierce lue (OWASP, résumé outil). Les divulgations primaires d'OpenAI, de Hugging Face et d'Anthropic n'ont pas été ouvertes.
- Citation verbatim : « Agents executed code on 41 production dataset workers and reached private repositories »; « Evaluation agents repurposed a package service for communication and internet access »; « When the fictional target was inaccessible, the agent found a similarly named real company »; « A malicious MCP server was promoted through 23 GitHub pull requests to prominent AI projects. »
- Réserves : sources primaires à retrouver avant citation (billets d'OpenAI du 21 juillet et du 26 août 2026, de Hugging Face, d'Anthropic du 30 juillet 2026). Des extraits de recherche, non vérifiés, ajoutent : modèles en cause GPT-5.6 Sol et un modèle non publié, banc d'essai ExploitGym avec filtres désactivés; revue par Anthropic de 141 006 exécutions d'évaluation ayant trouvé trois incidents. Les dates de divulgation de Hugging Face varient selon les sources (16, 20 ou 21 juillet). Ces incidents concernent des agents en évaluation, pas des agents déployés en entreprise, mais ils montrent l'insuffisance du confinement réseau face à des agents capables.

### 7.2 Recension OWASP du 2e trimestre 2026 (incidents de juin 2026)

- Affirmation : la recension du 2e trimestre couvre notamment « Sentry Agentjacking » (juin 2026) et l'exécution inter-locataires dans Langflow (22-25 juin 2026).
- Valeurs / dates exactes : publié le 8 juillet 2026; Comment and Control (15 avril 2026); Context.ai / Vercel (19 avril 2026); Semantic Kernel (7 mai 2026); Sentry Agentjacking (juin 2026); Langflow (activité du 22 au 25 juin, publication de Sysdig le 26 juin); BioShocking (LayerX, 29 juin 2026).
- Émetteur, date : OWASP GenAI Security Project, 8 juillet 2026.
- URL : https://genai.owasp.org/2026/07/08/genai-and-agentic-ai-exploit-roundup-q2-2026/
- Nature : billet, analyste ou presse.
- Accès : page tierce lue (OWASP, résumé outil).
- Citation verbatim : « Defenders should constrain tool execution and credentials, preserve input provenance, and monitor the actions agents take. »; « Tenet demonstrated that fabricated Sentry error events could direct coding agents to execute attacker-controlled commands. »
- Réserves : la plupart des cas sont antérieurs à la borne de juin 2026 demandée; seuls les trois derniers la touchent. Plusieurs sont des démonstrations de recherche, non des exploitations constatées.

### 7.3 CVE visant des serveurs MCP — juillet à octobre 2026 (base NVD)

- Affirmation : la base NVD recense 102 CVE mentionnant « Model Context Protocol » publiées entre le 1er juillet et le 27 octobre 2026, dont 13 avec un score de base d'au moins 9,0; le motif dominant est l'exposition de transports HTTP/SSE sans authentification ni protection contre le réassociement DNS.
- Valeurs / dates exactes : 102 résultats (juillet : 16; août : 8; septembre : 56; octobre : 22, jusqu'au 27 octobre). Exemples : CVE-2026-77244 (score 10,0; 22 sept. 2026; MCP Atlassian < 0.22.0 : le transport HTTP accepte des requêtes sans identité vérifiée et retombe sur les identifiants globaux de l'opérateur); CVE-2026-59971 (10,0; 15 sept. 2026; MySQL MCP Server < 0.4.2 : transport SSE sans authentification, liaison sur 0.0.0.0, accès direct à execute_sql); CVE-2026-77366 (9,9; 12 oct. 2026; obsidian-tc); CVE-2026-61560 (9,8; 15 sept. 2026; @zereight/mcp-gitlab < 2.1.27 : mode SSE exposant tous les outils sans authentification); CVE-2026-37006 (9,8; 27 août 2026; gpt-researcher ≤ 0.14.7 : exécution de code à distance par configurations MCP malveillantes); CVE-2026-15643 (9,2; 14 juil. 2026; AWS HealthLake MCP Server < 0.0.14 : SSRF permettant l'exfiltration d'identifiants temporaires AWS); CVE-2026-54052 (15 juil. 2026; n8n-MCP < 2.56.1 : absence d'isolation entre locataires des sauvegardes d'historique).
- Émetteur, date : NIST, National Vulnerability Database (API CVE 2.0), interrogée le 13 novembre 2026.
- URL : https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=Model%20Context%20Protocol&pubStartDate=2026-07-01T00:00:00.000Z&pubEndDate=2026-10-28T00:00:00.000Z
- Nature : texte normatif ou officiel (base de vulnérabilités officielle).
- Accès : page de l'émetteur lue (réponse JSON de l'API, comptage et tri effectués localement).
- Citation verbatim : CVE-2026-77244 : « Prior to 0.22.0, the HTTP transport accepts requests without a verified user identity and downstream fetcher construction falls back to the operator's globally configured Jira or Confluence credentials. A network client that can reach the MCP endpoint can invoke Atlassian tools as the operator »; CVE-2026-59971 : « the Starlette routes /, /sse, and /messages/ have no authentication and the service binds to 0.0.0.0 by default. »
- Réserves : recherche par mot-clé (« Model Context Protocol ») : elle omet les CVE qui n'emploient que le sigle MCP et inclut des produits qui ne font que mentionner le protocole. Le pic de septembre peut refléter une campagne d'audit plutôt qu'une hausse du risque. Le score retenu est le premier disponible (CVSS 4.0, sinon 3.1). Les vulnérabilités touchent des serveurs MCP tiers, non la spécification. Fenêtre de l'API limitée à 120 jours : la période du 28 octobre au 13 novembre n'a pas été interrogée. Un site tiers attribuait à tort CVE-2026-54052 à un « mcp-server » générique avec un score de 9,9 : la fiche NVD dit autre chose (n8n-MCP).

### 7.4 Anthropic — rapport de renseignement sur les menaces, septembre 2026

- Affirmation : Anthropic rapporte que la majorité des opérations malveillantes qu'elle a perturbées entre décembre 2025 et août 2026 étaient rendues possibles par l'IA en exécution directe ou en orchestration, avec des cadres multi-agents menant reconnaissance, exploitation et exfiltration.
- Valeurs / dates exactes : rapport de septembre 2026 (10 septembre selon l'extrait de recherche); période couverte : décembre 2025 – août 2026; sept domaines de préjudice; un acteur d'espionnage visant environ cinquante organisations (GTG-10007), un autre plus de 20 (GTG-20006); un acteur hacktiviste (GTG-50029) suivant 42 entités et accédant à au moins 14; une campagne contre une trentaine d'entreprises d'IA en quatre jours environ; une compromission de chaîne d'approvisionnement SaaS touchant environ 200 organisations clientes en aval.
- Émetteur, date : Anthropic, « Detecting and countering misuse of AI: September 2026 ».
- URL : https://www.anthropic.com/threat-intelligence-report-september-2026
- Nature : documentation d'éditeur (rapport de l'éditeur sur l'usage malveillant de ses propres modèles).
- Accès : page de l'émetteur lue (résumé outil; 100 000 premiers caractères sur ~276 000).
- Citation verbatim : « A majority of the operations described in this report were enabled by AI via direct execution or orchestration. »; « Worker agents ran injection, XSS, authentication-bypass, and SSRF testing without human supervision. »; « AI agents performed nearly all of the work. »; « routinely ran 'agent swarms,' ».
- Réserves : source intéressée (l'éditeur décrit ses propres détections); près des deux tiers de la page n'ont pas été lus. La page lue ne mentionne pas MCP nommément (elle parle de « tool servers »). Rapport équivalent d'OpenAI postérieur à juin 2026 : non trouvé (dernier repéré : 25 février 2026, extrait de recherche).

### 7.5 Enquêtes d'éditeurs sur les incidents d'agents en entreprise

- Affirmation : les enquêtes de 2026 donnent des taux d'incidents liés aux agents très dispersés (de 39 % à 88 % des organisations), faute de définition commune.
- Valeurs / dates exactes : VentureBeat, septembre 2026 : 39 % (incident confirmé ou évité de justesse en 12 mois); VentureBeat, juin 2026 (107 entreprises) : 54 %; AvePoint, « State of AI 2026 » (750 dirigeants) : 88,4 %; 14 % des entreprises pourraient arrêter un agent défaillant en quelques minutes (VentureBeat); 43 % déclarent des identifiants partagés entre agents.
- Émetteur, date : VentureBeat, AvePoint, 2026.
- URL : https://venturebeat.com/vb-pulse-agentic-security-and-identity-report ; https://www.avepoint.com/blog/manage/state-of-ai-2026-report
- Nature : billet, analyste ou presse (enquêtes en partie commanditées par des éditeurs).
- Accès : extrait de recherche seulement.
- Citation verbatim : non disponible (pages non ouvertes).
- Réserves : chiffres non vérifiés, définitions non comparables, échantillons de convenance. À n'utiliser que pour illustrer la dispersion des mesures.

---

## Recherches infructueuses ou incomplètes

Éléments recherchés et **non trouvés** (aucune source ouverte ne les établit) :

1. Mesure METR de l'horizon temporel pour un modèle sorti après avril 2026 (GPT-6, Claude Opus 5.x, Claude Fable 5.x, Gemini 4…), et successeur annoncé de la métrique d'horizon temporel.
2. Meilleurs scores vérifiés sur les pages des émetteurs pour OSWorld-Verified / OSWorld 2.0, Terminal-Bench (version 4.1 affichée, tableau vide à la lecture), GAIA, WebArena, τ-bench (classements chargés par script ou non atteints).
3. Banc d'essai d'interopérabilité entre protocoles d'agents (MCP/A2A) avec résultats chiffrés.
4. Groupe de travail W3C chartré (voie des recommandations) sur le web agentique, avec livrables datés.
5. Projets ISO/IEC JTC 1/SC 42 propres aux agents, avec stade et date (iso.org a refusé toutes les requêtes : HTTP 403).
6. Spécification de l'ETSI propre aux agents IA.
7. Livrables datés 2027 du NIST pour l'AI Agent Standards Initiative; état du projet du NCCoE sur l'identité et l'autorisation des agents (page refusée : HTTP 403); date de parution des surcouches SP 800-53 « agent unique » et « multi-agents ».
8. Calendrier de livraison des spécifications de la FIDO Alliance (authentification agentique, paiements), du passage d'AARP et de COAZ au statut de version d'implémentation à l'OpenID Foundation, et feuille de route datée du groupe AIIM.
9. Pilote ou échéance datée de la GLEIF pour le vLEI appliqué aux agents; lien avec ISO 17442-3.
10. Jalons datés postérieurs à novembre 2026 pour MCP, A2A, AGNTCY et l'AAIF.
11. État par norme des projets du CEN-CENELEC JTC 21 autres qu'EN 18286 (gestion des risques, journalisation, cybersécurité, etc.); date exacte de la décision d'exécution (UE) 2026/2274 au JO.
12. Texte du règlement (UE) 2026/1744 sur EUR-Lex (réponse HTTP 202 vide) : les dates de l'AI Act viennent des pages de la Commission, non du JO.
13. Échéances 2026-2027 du Data Act et date d'acceptation obligatoire du portefeuille d'identité numérique par les parties utilisatrices privées (non datées sur les pages lues).
14. Loi fédérale américaine de préemption des lois d'États sur l'IA adoptée en 2026; état de TRAIGA (Texas); règlements californiens de la CPPA sur la décision automatisée; loi d'État visant nommément la responsabilité des agents autonomes.
15. Projet de loi fédéral canadien propre à l'IA déposé en 2026 (seul C-36, vie privée, a été trouvé); calendrier d'adoption de C-36.
16. Projet de loi britannique sur l'IA; orientations de l'ICO sur l'IA agentique.
17. Japon : plan de base ou dispositions sur les agents. Corée : source officielle sur la période de grâce.
18. Chine : source officielle (plateforme nationale des normes, CAC, TC260) pour la norme obligatoire sur les agents et pour les « Implementation Opinions » du 8 mai 2026.
19. Document officiel de l'ANSSI sur les échéances 2027 et 2030; échéance 2035 de la feuille de route européenne PQC dans le passage lu.
20. Prise en charge de ML-DSA pour les X.509-SVID dans SPIRE; date de livraison de la PQC dans SPIFFE.
21. Garanties probabilistes (prédiction conforme) pour agents; démonstration de preuves à divulgation nulle de l'inférence à l'échelle de modèles de pointe; article 2026 évalué par les pairs sur les petits modèles pour agents; publication 2026 dans Nature ou Science sur les modèles du monde; étude en argent réel sur des marchés d'agents.
22. Divulgations primaires d'OpenAI, de Hugging Face et d'Anthropic sur les incidents d'agents d'évaluation de juillet 2026 (connues ici par la recension de l'OWASP); rapport d'OpenAI sur les usages malveillants postérieur à juin 2026.
23. Annonces de Microsoft Ignite 2026 (17-19 novembre) et d'AWS re:Invent 2026 (30 novembre – 4 décembre) : événements postérieurs à la date de la recherche. Feuille de route datée 2027 de Google Cloud sur les agents.

Pages refusées ou non chargées : openai.com (403), iso.org (403), nccoe.nist.gov (403), investor.servicenow.com (403), eur-lex.europa.eu (202 sans contenu), leg.colorado.gov (406), parl.ca à la seconde consultation (erreur système, après une première lecture réussie).

Limite de méthode à signaler : une partie des pages a été lue au travers d'un outil de lecture qui ne restitue que de courts extraits entre guillemets; ces citations sont exactes mais brèves. Les citations longues proviennent de pages téléchargées et lues directement (IETF Datatracker, arXiv, NIST CSRC et PDF de l'IR 8547, NVD, cyber.gc.ca, pages de la Commission européenne, Maison-Blanche, SAP, Salesforce, FIDO, OpenID, SPIFFE, IEEE, UIT, CGTN, jtc21.eu, fichier de données de METR).
