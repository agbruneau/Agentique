# Bibliographie — L'ingénierie des systèmes agentiques

*Bibliographie du chapitre sur l'IA agentique (angle dominant : ingénierie des systèmes agentiques), arrêtée à juin 2026.*

**Convention de citation.** Auteurs/Organisme (Année). *Titre*. Support/venue. Identifiant stable (arXiv / DOI / RFC / ISO / URL).
Six catégories ; ordre alphabétique par auteur/organisme à l'intérieur de chaque catégorie (par identifiant pour les normes IETF/ISO).

**Méthode de constitution.** Recherche en éventail sur 12 sous-domaines, puis vérification adverse de chaque citation sur le web (existence, auteurs, année, arXiv id, venue, numéro de norme/RFC), enfin dédoublonnage. Bilan : **246 références vérifiées → 208 entrées retenues (comptées) ; 229 confirmées, 17 corrigées, 0 non vérifiable.** *Révision v2 (2026-06-24) : +1 référence IBM vérifiée (portefeuille AIOps/observabilité). Finalisation (2026-07) : +1 entrée EchoLeak (Aim Security, CVE-2025-32711) ; lettrage des homonymies auteur-année (Anthropic 2025a-e, OpenAI 2024a-b et 2025a-f, Willison 2025a-b) reporté dans le corps ; répartition finale par catégorie : 17 + 111 + 17 + 16 + 2 + 45.* Pièges spécifiques au domaine traités à la vérification : surnom de papier (ReAct, Reflexion, Toolformer…) rattaché au bon arXiv id, distinction année arXiv vs année de conférence, distinction des deux « CRAG » (Corrective RAG 2401.15884 vs benchmark 2406.04744).

**Marqueur ⚠.** Signale une *ressource vivante* (doc produit/framework, spécification versionnée par date, prépublication non encore en actes, document en statut draft/proposition, version de paquet) dont le numéro/l'ancre/le statut doit être fixé au moment de citer.

**Deux réserves de forme.** (1) Les renvois « référence → section » ne sont pas reportés ici (étiquettes thématiques hétérogènes selon les agents) — un index thématique alignable sur la TOC peut être régénéré sur demande. (2) Les accents de quelques mots français dans les chaînes de citation ne sont pas normalisés (citations préservées verbatim pour ne pas altérer les métadonnées).

---

## 1. Ouvrages et articles fondateurs (avant l'ère des agents LLM)

- Anderson, J. R.; Bothell, D.; Byrne, M. D.; Douglass, S.; Lebiere, C.; Qin, Y. (2004). *An Integrated Theory of the Mind*. Psychological Review, vol. 111, no. 4, pp. 1036-1060. DOI:10.1037/0033-295X.111.4.1036.
- Bellman, R. (1957). *A Markovian Decision Process*. Journal of Mathematics and Mechanics (Indiana Univ. Math. J.), vol. 6, no. 5, pp. 679-684. https://www.jstor.org/stable/24900506 (également RAND P-1066).
- Bratman, M. E. (1987). *Intention, Plans, and Practical Reason*. Harvard University Press, Cambridge MA. ISBN 9780674458185.
- Brooks, R. A. (1991). *Intelligence without Representation*. Artificial Intelligence, vol. 47, no. 1-3, pp. 139-159. DOI:10.1016/0004-3702(91)90053-M.
- Jennings, N. R.; Sycara, K.; Wooldridge, M. (1998). *A Roadmap of Agent Research and Development*. Autonomous Agents and Multi-Agent Systems, vol. 1, no. 1, pp. 7-38. DOI:10.1023/A:1010090405266.
- Kaelbling, L. P.; Littman, M. L.; Cassandra, A. R. (1998). *Planning and Acting in Partially Observable Stochastic Domains*. Artificial Intelligence, vol. 101, no. 1-2, pp. 99-134. DOI:10.1016/S0004-3702(98)00023-X.
- Laird, J. E.; Newell, A.; Rosenbloom, P. S. (1987). *SOAR: An Architecture for General Intelligence*. Artificial Intelligence, vol. 33, pp. 1-64. DOI:10.1016/0004-3702(87)90050-6.
- Puterman, M. L. (1994). *Markov Decision Processes: Discrete Stochastic Dynamic Programming*. John Wiley & Sons (Wiley Series in Probability and Statistics). DOI:10.1002/9780470316887 (ISBN imprimé 9780471619772).
- Rao, A. S. (1996). *AgentSpeak(L): BDI Agents Speak Out in a Logical Computable Language*. MAAMAW 1996, LNCS (LNAI) vol. 1038, Springer, pp. 42-55. DOI:10.1007/BFb0031845.
- Rao, A. S.; Georgeff, M. P. (1995). *BDI Agents: From Theory to Practice*. First International Conference on Multi-Agent Systems (ICMAS-95), San Francisco, pp. 312-319. https://cdn.aaai.org/ICMAS/1995/ICMAS95-042.pdf.
- Russell, S. J.; Norvig, P. (2020/2021). *Artificial Intelligence: A Modern Approach (4th Edition)*. Pearson. ISBN 9780134610993.
- Russell, S. J.; Subramanian, D. (1995). *Provably Bounded-Optimal Agents*. Journal of Artificial Intelligence Research (JAIR), vol. 2, pp. 575-609. DOI:10.1613/jair.133 (arXiv:cs/9505103).
- Shoham, Y.; Leyton-Brown, K. (2009). *Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations*. Cambridge University Press. ISBN 9780521899437.
- Smith, R. G. (1980). *The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver*. IEEE Transactions on Computers, vol. C-29, no. 12, pp. 1104-1113. DOI:10.1109/TC.1980.1675516.
- Sutton, R. S.; Barto, A. G. (2018). *Reinforcement Learning: An Introduction (2nd Edition)*. MIT Press, Cambridge MA. ISBN 9780262039246.
- Wooldridge, M. (2009). *An Introduction to MultiAgent Systems (2nd Edition)*. John Wiley & Sons. ISBN 9780470519462.
- Wooldridge, M.; Jennings, N. R. (1995). *Intelligent Agents: Theory and Practice*. The Knowledge Engineering Review (Cambridge University Press), vol. 10, no. 2, pp. 115-152. DOI:10.1017/S0269888900008122.

## 2. Articles de recherche sur les agents LLM et le raisonnement (2022-2026)

- Asai, A.; Wu, Z.; Wang, Y.; Sil, A.; Hajishirzi, H. (2023). *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*. arXiv:2310.11511 (ICLR 2024, oral).
- Barnett, S.; Kurniawan, S.; Thudumu, S.; Brannelly, Z.; Abdelrazek, M. (2024). *Seven Failure Points When Engineering a Retrieval Augmented Generation System*. CAIN 2024 (IEEE/ACM). arXiv:2401.05856.
- Belcak, P.; Heinrich, G.; Diao, S.; Fu, Y.; Dong, X.; Muralidharan, S.; Lin, Y. C.; Molchanov, P. (2025). *Small Language Models are the Future of Agentic AI*. arXiv:2506.02153 (NVIDIA Research ; prise de position). ⚠
- Besta, M.; Blach, N.; Kubicek, A.; Gerstenberger, R.; Podstawski, M.; Gianinazzi, L.; et al. (2024). *Graph of Thoughts: Solving Elaborate Problems with Large Language Models*. arXiv:2308.09687 (AAAI 2024, vol. 38, no. 16, pp. 17682-17690, DOI:10.1609/aaai.v38i16.29720).
- Cemri, M.; Pan, M. Z.; Yang, S.; Agrawal, L. A.; Chopra, B.; Tiwari, R.; Keutzer, K.; Parameswaran, A.; Klein, D.; Ramchandran, K.; Zaharia, M.; Gonzalez, J. E.; Stoica, I. (2025). *Why Do Multi-Agent LLM Systems Fail?* arXiv:2503.13657 (NeurIPS 2025 Datasets & Benchmarks ; taxonomie MAST). ⚠
- Chan, C.-M.; Chen, W.; Su, Y.; Yu, J.; Xue, W.; Zhang, S.; Fu, J.; Liu, Z. (2023). *ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate*. arXiv:2308.07201 (ICLR 2024).
- Chen, W.; Su, Y.; Zuo, J.; Yang, C.; Yuan, C.; Chan, C.-M.; Yu, H.; Lu, Y.; Hung, Y.-H.; Qian, C.; Qin, Y.; Cong, X.; Xie, R.; Liu, Z.; Sun, M.; Zhou, J. (2023). *AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors*. arXiv:2308.10848 (ICLR 2024). *(contexte non cité)*
- Chhikara, P.; Khant, D.; Aryan, S.; Singh, T.; Yadav, D. (2025). *Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory*. arXiv:2504.19413.
- Chiang, W.-L.; Zheng, L.; Sheng, Y.; Angelopoulos, A. N.; Li, T.; Li, D.; Zhang, H.; Zhu, B.; Jordan, M.; Gonzalez, J. E.; Stoica, I. (2024). *Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference*. arXiv:2403.04132 (ICML 2024, PMLR 235:8359-8388).
- Debenedetti, E.; Zhang, J.; Balunović, M.; Beurer-Kellner, L.; Fischer, M.; Tramèr, F. (2024). *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*. arXiv:2406.13352 (NeurIPS 2024 Datasets & Benchmarks).
- Debenedetti, E.; Shumailov, I.; Fan, T.; Hayes, J.; Carlini, N.; Fabian, D.; Kern, C.; Shi, C.; Terzis, A.; Tramèr, F. (2025). *Defeating Prompt Injections by Design (CaMeL)*. arXiv:2503.18813.
- DeepSeek-AI (Guo, D.; et al.) (2025). *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. arXiv:2501.12948 (également Nature vol. 645, pp. 633-638, 2025, DOI:10.1038/s41586-025-09422-z).
- Deng, X.; Gu, Y.; Zheng, B.; Chen, S.; Stevens, S.; Wang, B.; Sun, H.; Su, Y. (2023). *Mind2Web: Towards a Generalist Agent for the Web*. arXiv:2306.06070 (NeurIPS 2023 Datasets & Benchmarks, Spotlight).
- Du, Y.; Li, S.; Torralba, A.; Tenenbaum, J. B.; Mordatch, I. (2023). *Improving Factuality and Reasoning in Language Models through Multiagent Debate*. arXiv:2305.14325 (ICML 2024).
- Edge, D.; Trinh, H.; Cheng, N.; Bradley, J.; Chao, A.; Mody, A.; Truitt, S.; Metropolitansky, D.; Ness, R. O.; Larson, J. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. arXiv:2404.16130 (Microsoft Research, GraphRAG).
- Ehtesham, A.; Singh, A.; Gupta, G. K.; Kumar, S. (2025). *A survey of agent interoperability protocols: MCP, ACP, A2A, and ANP*. arXiv:2505.02279 (v2, 23 mai 2025).
- Es, S.; James, J.; Espinosa-Anke, L.; Schockaert, S. (2023). *Ragas: Automated Evaluation of Retrieval Augmented Generation*. arXiv:2309.15217 (EACL 2024, demo).
- Gao, L.; Ma, X.; Lin, J.; Callan, J. (2023). *Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE)*. arXiv:2212.10496 (ACL 2023).
- Gao, Y.; Xiong, Y.; Gao, X.; Jia, K.; Pan, J.; Bi, Y.; Dai, Y.; Sun, J.; Wang, M.; Wang, H. (2024). *Retrieval-Augmented Generation for Large Language Models: A Survey*. arXiv:2312.10997.
- Greenblatt, R.; Denison, C.; Wright, B.; Roger, F.; MacDiarmid, M.; Marks, S.; Treutlein, J.; et al. (2024). *Alignment faking in large language models*. arXiv:2412.14093 (Anthropic, Redwood Research).
- Greshake, K.; Abdelnabi, S.; Mishra, S.; Endres, C.; Holz, T.; Fritz, M. (2023). *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. AISec '23. arXiv:2302.12173.
- Guo, T.; Chen, X.; Wang, Y.; Chang, R.; Pei, S.; Chawla, N. V.; Wiest, O.; Zhang, X. (2024). *Large Language Model based Multi-Agents: A Survey of Progress and Challenges*. arXiv:2402.01680 (IJCAI 2024, pp. 8048-8057).
- Hong, S.; Zheng, X.; Chen, J.; Cheng, Y.; Wang, J.; Zhang, C.; Wang, Z.; Yau, S. K. S.; Lin, Z.; Zhou, L.; Ran, C.; Xiao, L.; Wu, C.; Schmidhuber, J. (2023). *MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework*. arXiv:2308.00352 (ICLR 2024).
- Hu, Y.; Wang, Y.; McAuley, J. (2025). *Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions (MemoryAgentBench)*. arXiv:2507.05257.
- Izacard, G.; Caron, M.; Hosseini, L.; Riedel, S.; Bojanowski, P.; Joulin, A.; Grave, E. (2022). *Unsupervised Dense Information Retrieval with Contrastive Learning (Contriever)*. arXiv:2112.09118 (TMLR 2022).
- Izacard, G.; Grave, E. (2021). *Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering (FiD)*. arXiv:2007.01282 (EACL 2021). *(contexte non cité)*
- Jiang, Z.; Xu, F. F.; Gao, L.; Sun, Z.; Liu, Q.; Dwivedi-Yu, J.; Yang, Y.; Callan, J.; Neubig, G. (2023). *Active Retrieval Augmented Generation (FLARE)*. arXiv:2305.06983 (EMNLP 2023).
- Jimenez, C. E.; Yang, J.; Wettig, A.; Yao, S.; Pei, K.; Press, O.; Narasimhan, K. (2023). *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* arXiv:2310.06770 (ICLR 2024).
- Jimenez Gutierrez, B.; Shu, Y.; Gu, Y.; Yasunaga, M.; Su, Y. (2024). *HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models*. arXiv:2405.14831 (NeurIPS 2024).
- Jin, B.; Zeng, H.; Yue, Z.; Wang, D.; Zamani, H.; Han, J. (2025). *Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning*. arXiv:2503.09516.
- Kambhampati, S.; Valmeekam, K.; Guan, L.; Stechly, K.; Verma, M.; Bhambri, S.; Saldyt, L.; Murthy, A. (2024). *LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks*. arXiv:2402.01817 (ICML 2024, spotlight).
- Kapoor, S.; Stroebl, B.; Siegel, Z. S.; Nadgir, N.; Narayanan, A. (2024). *AI Agents That Matter*. arXiv:2407.01502.
- Kapoor, S.; Stroebl, B.; Narayanan, A.; et al. (Princeton PLI) (2025). *Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation*. arXiv:2510.11977 (accepté à ICLR 2026 ; plateforme HAL). ⚠
- Karpukhin, V.; Oğuz, B.; Min, S.; Lewis, P.; Wu, L.; Edunov, S.; Chen, D.; Yih, W. (2020). *Dense Passage Retrieval for Open-Domain Question Answering (DPR)*. arXiv:2004.04906 (EMNLP 2020).
- Khattab, O.; Zaharia, M. (2020). *ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT*. arXiv:2004.12832 (SIGIR 2020).
- Koh, J. Y.; Lo, R.; Jang, L.; Duvvur, V.; Lim, M. C.; Huang, P.-Y.; Neubig, G.; Zhou, S.; Salakhutdinov, R.; Fried, D. (2024). *VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks*. arXiv:2401.13649 (ACL 2024).
- Kojima, T.; Gu, S. S.; Reid, M.; Matsuo, Y.; Iwasawa, Y. (2022). *Large Language Models are Zero-Shot Reasoners*. arXiv:2205.11916 (NeurIPS 2022 ; Zero-shot-CoT).
- Lei, F.; Chen, J.; Ye, Y.; Cao, R.; Shin, D.; Su, H.; Yu, T.; et al. (2025). *Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows*. arXiv:2411.07763 (ICLR 2025, oral).
- Lewis, P.; Perez, E.; Piktus, A.; Petroni, F.; Karpukhin, V.; Goyal, N.; Küttler, H.; Lewis, M.; Yih, W.; Rocktäschel, T.; Riedel, S.; Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. arXiv:2005.11401 (NeurIPS 2020 ; article fondateur du terme RAG).
- Li, G.; Hammoud, H.; Itani, H.; Khizbullin, D.; Ghanem, B. (2023). *CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society*. arXiv:2303.17760 (NeurIPS 2023).
- Li, J.; Hui, B.; Qu, G.; Yang, J.; et al. (2023). *Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs (BIRD)*. arXiv:2305.03111 (NeurIPS 2023).
- Li, M.; Zhao, Y.; Yu, B.; Song, F.; Li, H.; Yu, H.; Li, Z.; Huang, F.; Li, Y. (2023). *API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs*. arXiv:2304.08244 (EMNLP 2023). *(contexte non cité)*
- Lightman, H.; Kosaraju, V.; Burda, Y.; Edwards, H.; Baker, B.; Lee, T.; Leike, J.; Schulman, J.; Sutskever, I.; Cobbe, K. (2023). *Let's Verify Step by Step*. arXiv:2305.20050 (ICLR 2024).
- Liu, N. F.; Lin, K.; Hewitt, J.; Paranjape, A.; Bevilacqua, M.; Petroni, F.; Liang, P. (2023). *Lost in the Middle: How Language Models Use Long Contexts*. arXiv:2307.03172 (TACL vol. 12, 2024, pp. 157-173, DOI:10.1162/tacl_a_00638).
- Liu, X.; Yu, H.; Zhang, H.; Xu, Y.; Lei, X.; Lai, H.; Gu, Y.; et al. (2023). *AgentBench: Evaluating LLMs as Agents*. arXiv:2308.03688 (ICLR 2024).
- Liu, Y.; Iter, D.; Xu, Y.; Wang, S.; Xu, R.; Zhu, C. (2023). *G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*. arXiv:2303.16634 (EMNLP 2023).
- Liu, Y.; Jia, Y.; Geng, R.; Jia, J.; Gong, N. Z. (2024). *Formalizing and Benchmarking Prompt Injection Attacks and Defenses*. arXiv:2310.12815 (USENIX Security '24).
- Madaan, A.; Tandon, N.; Gupta, P.; Hallinan, S.; Gao, L.; Wiegreffe, S.; et al. (2023). *Self-Refine: Iterative Refinement with Self-Feedback*. arXiv:2303.17651 (NeurIPS 2023).
- Maharana, A.; Lee, D.-H.; Tulyakov, S.; Bansal, M.; Barbieri, F.; Fang, Y. (2024). *Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo)*. arXiv:2402.17753 (ACL 2024, Long Papers).
- Masterman, T.; Besen, S.; Sawtell, M.; Chao, A. (2024). *The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey*. arXiv:2404.11584.
- Mei, L.; Yao, J.; Ge, Y.; Wang, Y.; Bi, B.; Cai, Y.; Liu, J.; Li, M.; et al. (2025). *A Survey of Context Engineering for Large Language Models*. arXiv:2507.13334.
- Meinke, A.; Schoen, B.; Scheurer, J.; Balesni, M.; Shah, R.; Hobbhahn, M. (2024). *Frontier Models are Capable of In-context Scheming*. arXiv:2412.04984 (Apollo Research).
- Mialon, G.; Fourrier, C.; Swift, C.; Wolf, T.; LeCun, Y.; Scialom, T. (2023). *GAIA: a benchmark for General AI Assistants*. arXiv:2311.12983 (ICLR 2024).
- Muennighoff, N.; Tazi, N.; Magne, L.; Reimers, N. (2023). *MTEB: Massive Text Embedding Benchmark*. arXiv:2210.07316 (EACL 2023).
- Muennighoff, N.; Yang, Z.; Shi, W.; Li, X. L.; Fei-Fei, L.; Hajishirzi, H.; Zettlemoyer, L.; Liang, P.; Candès, E.; Hashimoto, T. (2025). *s1: Simple Test-Time Scaling*. arXiv:2501.19393 (EMNLP 2025, pp. 20275-20321).
- Packer, C.; Wooders, S.; Lin, K.; Fang, V.; Patil, S. G.; Stoica, I.; Gonzalez, J. E. (2023). *MemGPT: Towards LLMs as Operating Systems*. arXiv:2310.08560.
- Park, J. S.; O'Brien, J. C.; Cai, C. J.; Morris, M. R.; Liang, P.; Bernstein, M. S. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*. arXiv:2304.03442 (UIST 2023).
- Patil, S. G.; Zhang, T.; Wang, X.; Gonzalez, J. E. (2023). *Gorilla: Large Language Model Connected with Massive APIs*. arXiv:2305.15334 (NeurIPS 2024).
- Patil, S. G.; Mao, H.; Yan, F.; Ji, C. C.-J.; Suresh, V.; Stoica, I.; Gonzalez, J. E. (2025). *The Berkeley Function-Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models*. ICML 2025, PMLR vol. 267, pp. 48371-48392. https://proceedings.mlr.press/v267/patil25a.html.
- Phan, L.; et al. (Center for AI Safety ; Scale AI) (2025). *Humanity's Last Exam*. arXiv:2501.14249 (version ultérieure parue dans *Nature*, vol. 649, pp. 1139-1146, 2026, sous le titre « A benchmark of expert-level academic questions to assess AI capabilities », DOI:10.1038/s41586-025-09962-4). ⚠
- Press, O.; Zhang, M.; Min, S.; Schmidt, L.; Smith, N. A.; Lewis, M. (2023). *Measuring and Narrowing the Compositionality Gap in Language Models (Self-Ask)*. arXiv:2210.03350 (Findings of EMNLP 2023).
- Qian, C.; Liu, W.; Liu, H.; Chen, N.; Dang, Y.; Li, J.; Yang, C.; Chen, W.; Su, Y.; Cong, X.; Xu, J.; Li, D.; Liu, Z.; Sun, M. (2023). *ChatDev: Communicative Agents for Software Development*. arXiv:2307.07924 (ACL 2024, pp. 15174-15186).
- Qin, Y.; Liang, S.; Ye, Y.; Zhu, K.; Yan, L.; Lu, Y.; Lin, Y.; Cong, X.; Tang, X.; Qian, B.; Zhao, S.; Hong, L.; Tian, R.; Xie, R.; Zhou, J.; Gerstein, M.; Li, D.; Liu, Z.; Sun, M. (2023). *ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs*. arXiv:2307.16789 (ICLR 2024, spotlight).
- Qin, Y.; Ye, Y.; Fang, J.; Wang, H.; Liang, S.; Tian, S.; Zhang, J.; et al. (ByteDance Seed) (2025). *UI-TARS: Pioneering Automated GUI Interaction with Native Agents*. arXiv:2501.12326. ⚠
- Rasmussen, P.; Paliychuk, P.; Beauvais, T.; Ryan, J.; Chalef, D. (2025). *Zep: A Temporal Knowledge Graph Architecture for Agent Memory*. arXiv:2501.13956 (moteur Graphiti).
- Rein, D.; Hou, B. L.; Stickland, A. C.; Petty, J.; Pang, R. Y.; Dirani, J.; Michael, J.; Bowman, S. R. (2023). *GPQA: A Graduate-Level Google-Proof Q&A Benchmark*. arXiv:2311.12022 (COLM 2024).
- Saad-Falcon, J.; Khattab, O.; Potts, C.; Zaharia, M. (2024). *ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems*. arXiv:2311.09476 (NAACL 2024).
- Sapkota, R.; Roumeliotis, K. I.; Karkee, M. (2025). *AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges*. arXiv:2505.10468 (Information Fusion, Elsevier, DOI:10.1016/j.inffus.2025.103599).
- Sarthi, P.; Abdullah, S.; Tuli, A.; Khanna, S.; Goldie, A.; Manning, C. D. (2024). *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*. arXiv:2401.18059 (ICLR 2024).
- Schick, T.; Dwivedi-Yu, J.; Dessì, R.; Raileanu, R.; Lomeli, M.; Zettlemoyer, L.; Cancedda, N.; Scialom, T. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. arXiv:2302.04761 (NeurIPS 2023).
- Schoen, B.; Nitishinskaya, E.; Balesni, M.; Hobbhahn, M.; et al. (OpenAI & Apollo Research) (2025). *Stress Testing Deliberative Alignment for Anti-Scheming Training*. arXiv:2509.15541.
- Shao, Z.; Wang, P.; Zhu, Q.; Xu, R.; Song, J.; et al. (DeepSeek-AI) (2024). *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models*. arXiv:2402.03300 (introduit GRPO).
- Shinn, N.; Cassano, F.; Berman, E.; Gopinath, A.; Narasimhan, K.; Yao, S. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*. arXiv:2303.11366 (NeurIPS 2023).
- Singh, A.; Ehtesham, A.; Kumar, S.; Khoei, T. T. (2025). *Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG*. arXiv:2501.09136.
- Snell, C.; Lee, J.; Xu, K.; Kumar, A. (2024). *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*. arXiv:2408.03314.
- Sumers, T. R.; Yao, S.; Narasimhan, K.; Griffiths, T. L. (2023). *Cognitive Architectures for Language Agents (CoALA)*. arXiv:2309.02427 (TMLR, 2024).
- Thakur, N.; Reimers, N.; Rücklé, A.; Srivastava, A.; Gurevych, I. (2021). *BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models*. arXiv:2104.08663 (NeurIPS 2021 Datasets & Benchmarks).
- Trivedi, H.; Balasubramanian, N.; Khot, T.; Sabharwal, A. (2023). *Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions (IRCoT)*. arXiv:2212.10509 (ACL 2023).
- Valmeekam, K.; Marquez, M.; Olmo, A.; Sreedharan, S.; Kambhampati, S. (2023). *PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change*. arXiv:2206.10498 (NeurIPS 2023 Datasets & Benchmarks).
- Valmeekam, K.; Marquez, M.; Sreedharan, S.; Kambhampati, S. (2023). *On the Planning Abilities of Large Language Models: A Critical Investigation*. arXiv:2305.15771 (NeurIPS 2023).
- Wang, L.; Xu, W.; Lan, Y.; Hu, Z.; Lan, Y.; Lee, R. K.-W.; Lim, E.-P. (2023). *Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models*. arXiv:2305.04091 (ACL 2023).
- Wang, L.; Ma, C.; Feng, X.; Zhang, Z.; Yang, H.; Zhang, J.; Chen, Z.; Tang, J.; Chen, X.; Lin, Y.; Zhao, W. X.; Wei, Z.; Wen, J.-R. (2024). *A Survey on Large Language Model based Autonomous Agents*. arXiv:2308.11432 (Frontiers of Computer Science, vol. 18, no. 6, DOI:10.1007/s11704-024-40231-1).
- Wang, X.; Chen, Y.; Yuan, L.; Zhang, Y.; Li, Y.; Peng, H.; Ji, H. (2024). *Executable Code Actions Elicit Better LLM Agents (CodeAct)*. arXiv:2402.01030 (ICML 2024).
- Wang, X.; Wei, J.; Schuurmans, D.; Le, Q.; Chi, E.; Narang, S.; Chowdhery, A.; Zhou, D. (2022). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. arXiv:2203.11171 (ICLR 2023).
- Wang, Y.; Chen, X. (2025). *MIRIX: Multi-Agent Memory System for LLM-Based Agents*. arXiv:2507.07957.
- Wei, J.; Wang, X.; Schuurmans, D.; Bosma, M.; Ichter, B.; Xia, F.; Chi, E.; Le, Q.; Zhou, D. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. arXiv:2201.11903 (NeurIPS 2022).
- Wu, D.; Wang, H.; Yu, W.; Zhang, Y.; Chang, K.-W.; Yu, D. (2024). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. arXiv:2410.10813 (ICLR 2025).
- Wu, Q.; Bansal, G.; Zhang, J.; Wu, Y.; Zhang, S.; Zhu, E.; Li, B.; Jiang, L.; Zhang, X.; Wang, C. (2023). *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework*. arXiv:2308.08155 (COLM 2024).
- Wu, Y.; Liang, S.; Zhang, C.; Wang, Y.; Zhang, Y.; Guo, H.; Tang, R.; Liu, Y. (2025). *From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs*. arXiv:2504.15965.
- Xi, Z.; Chen, W.; Guo, X.; He, W.; Ding, Y.; Hong, B.; Zhang, M.; et al.; Gui, T. (2023). *The Rise and Potential of Large Language Model Based Agents: A Survey*. arXiv:2309.07864.
- Xie, T.; Zhang, D.; Chen, J.; Li, X.; Zhao, S.; Cao, R.; Hua, T. J.; Cheng, Z.; Shin, D.; Lei, F.; Liu, Y.; Xu, Y.; Zhou, S.; Savarese, S.; Xiong, C.; Zhong, V.; Yu, T. (2024). *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*. arXiv:2404.07972 (NeurIPS 2024).
- Xu, B.; Peng, Z.; Lei, B.; Mukherjee, S.; Liu, Y.; Xu, D. (2023). *ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models*. arXiv:2305.18323.
- Xu, W.; Liang, Z.; Mei, K.; Gao, H.; Tan, J.; Zhang, Y. (2025). *A-MEM: Agentic Memory for LLM Agents*. arXiv:2502.12110 (NeurIPS 2025 ; méthode Zettelkasten). ⚠
- Yan, S.-Q.; Gu, J.-C.; Zhu, Y.; Ling, Z.-H. (2024). *Corrective Retrieval Augmented Generation (CRAG)*. arXiv:2401.15884.
- Yang, J.; Jimenez, C. E.; Wettig, A.; Lieret, K.; Yao, S.; Narasimhan, K.; Press, O. (2024). *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*. arXiv:2405.15793 (NeurIPS 2024).
- Yang, X.; Sun, K.; et al. (2024). *CRAG — Comprehensive RAG Benchmark*. arXiv:2406.04744 (NeurIPS 2024 Datasets & Benchmarks ; Meta, distinct de Corrective RAG 2401.15884).
- Yang, Y.; Chai, H.; Song, Y.; Qi, S.; Wen, M.; Li, N.; Liao, J.; Hu, H.; Lin, J.; Chang, G.; Liu, W.; Wen, Y.; Yu, Y.; Zhang, W. (2025). *A Survey of AI Agent Protocols*. arXiv:2504.16736.
- Yang, Y.; Ma, M.; Huang, Y.; Chai, H.; Gong, C.; Geng, H.; Zhou, Y.; Wen, Y.; Fang, M.; Chen, M.; Gu, S.; Jin, M.; Spanos, C.; Yang, Y.; Abbeel, P.; Song, D.; Zhang, W.; Wang, J. (2025). *Agentic Web: Weaving the Next Web with AI Agents*. arXiv:2507.21206.
- Yang, Z.; Qi, P.; Zhang, S.; Bengio, Y.; Cohen, W.; Salakhutdinov, R.; Manning, C. D. (2018). *HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering*. arXiv:1809.09600 (EMNLP 2018).
- Yao, S.; Shinn, N.; Razavi, P.; Narasimhan, K. (2024). *tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*. arXiv:2406.12045 (métrique pass^k ; Sierra Research).
- Yao, S.; Yu, D.; Zhao, J.; Shafran, I.; Griffiths, T. L.; Cao, Y.; Narasimhan, K. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. arXiv:2305.10601 (NeurIPS 2023).
- Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.; Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv:2210.03629 (ICLR 2023).
- Yehudai, A.; Eden, L.; Li, A.; Uziel, G.; Zhao, Y.; Bar-Haim, R.; Cohan, A.; Shmueli-Scheuer, M. (2025). *Survey on Evaluation of LLM-based Agents*. arXiv:2503.16416.
- Yu, T.; Zhang, R.; Yang, K.; Yasunaga, M.; Wang, D.; et al. (2018). *Spider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task*. arXiv:1809.08887 (EMNLP 2018).
- Zelikman, E.; Wu, Y.; Mu, J.; Goodman, N. D. (2022). *STaR: Bootstrapping Reasoning With Reasoning*. arXiv:2203.14465 (NeurIPS 2022).
- Zhan, Q.; Liang, Z.; Ying, Z.; Kang, D. (2024). *InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents*. arXiv:2403.02691 (Findings of ACL 2024).
- Zhang, Z.; Bo, X.; Ma, C.; Li, R.; Chen, X.; Dai, Q.; Zhu, J.; Dong, Z.; Wen, J.-R. (2024). *A Survey on the Memory Mechanism of Large Language Model based Agents*. arXiv:2404.13501 (ACM TOIS, DOI:10.1145/3748302).
- Zheng, L.; Chiang, W.-L.; Sheng, Y.; Zhuang, S.; Wu, Z.; Zhuang, Y.; Lin, Z.; Li, Z.; Li, D.; Xing, E. P.; Zhang, H.; Gonzalez, J. E.; Stoica, I. (2023). *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*. arXiv:2306.05685 (NeurIPS 2023 Datasets & Benchmarks).
- Zhong, W.; Guo, L.; Gao, Q.; Ye, H.; Wang, Y. (2024). *MemoryBank: Enhancing Large Language Models with Long-Term Memory*. arXiv:2305.10250 (AAAI 2024, vol. 38, no. 17, pp. 19724-19731, DOI:10.1609/aaai.v38i17.29946). *(contexte non cité)*
- Zhou, A.; Yan, K.; Shlapentokh-Rothman, M.; Wang, H.; Wang, Y.-X. (2023). *Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models (LATS)*. arXiv:2310.04406 (ICML 2024).
- Zhou, S.; Xu, F. F.; Zhu, H.; Zhou, X.; Lo, R.; Sridhar, A.; Cheng, X.; Ou, T.; Bisk, Y.; Fried, D.; Alon, U.; Neubig, G. (2023). *WebArena: A Realistic Web Environment for Building Autonomous Agents*. arXiv:2307.13854 (ICLR 2024).

## 3. Spécifications, protocoles et normes techniques

*Organismes et projets par ordre alphabétique ; normes IETF (RFC) et ISO/IEC regroupées par numéro croissant.*

- Agent2Agent Protocol Project (Linux Foundation ; contribué par Google) (2025). *Agent2Agent (A2A) Protocol Specification, v1.0.0* (taguée 12 mars 2026 ; v1.0.1 le 28 mai 2026). Licence Apache 2.0. https://a2a-protocol.org/latest/specification/. ⚠
- Anthropic (2024c). *Introducing the Model Context Protocol*. Annonce officielle (25 nov. 2024). https://www.anthropic.com/news/model-context-protocol.
- Anthropic / communauté Model Context Protocol (2025). *Model Context Protocol Specification, version 2025-11-25* (révision complète : autorisation renforcée et Tasks asynchrones pour les opérations de longue durée, en sus des primitives tools/resources/prompts). https://modelcontextprotocol.io/specification/2025-11-25.
- FIPA / IEEE Computer Society (2002). *FIPA ACL Message Structure Specification (SC00061G)* et *FIPA Communicative Act Library Specification (SC00037J)*. Standard FIPA (2002-12-03), hérité par l'IEEE Computer Society (2005). http://www.fipa.org/specs/fipa00061/.
- Google (2025). *Agent Payments Protocol (AP2)*. Spécification ouverte (annoncée 16 sept. 2025 ; mandats Intent/Cart/Payment portés comme W3C Verifiable Credentials). https://ap2-protocol.org/. ⚠
- IBM Research / BeeAI (2025). *Agent Communication Protocol (ACP — sigle « ACP » pour communication agent-agent ; à distinguer de l'Agentic Commerce Protocol homonyme)*. Protocole HTTP-natif (lancé mars 2025), donné à la Linux Foundation ; fusionné dans A2A, dépôt archivé le 27 août 2025. https://github.com/i-am-bee/acp. ⚠
- Sakimura, N.; Bradley, J.; Agarwal, N. (2015). *Proof Key for Code Exchange by OAuth Public Clients (PKCE)*. IETF RFC 7636 (Standards Track), septembre 2015. DOI:10.17487/RFC7636.
- Jones, M.; Nadalin, A.; Campbell, B. (ed.); Bradley, J.; Mortimore, C. (2020). *OAuth 2.0 Token Exchange*. IETF RFC 8693 (Standards Track), janvier 2020. DOI:10.17487/RFC8693.
- Campbell, B.; Bradley, J.; Tschofenig, H. (2020). *Resource Indicators for OAuth 2.0*. IETF RFC 8707 (Standards Track), février 2020.
- Jones, M. B.; Hunt, P.; Parecki, A. (2025). *OAuth 2.0 Protected Resource Metadata*. IETF RFC 9728 (Proposed Standard), avril 2025. DOI:10.17487/RFC9728.
- Hardt, D. (ed.); Parecki, A.; Lodderstedt, T. (2026). *The OAuth 2.1 Authorization Framework*. IETF Internet-Draft (Standards Track, en cours), draft-ietf-oauth-v2-1-15 (2 mars 2026) ; obsolète RFC 6749/6750 ; non encore publié comme RFC. ⚠
- ISO/IEC JTC 1/SC 42 (2023). *Information technology — Artificial intelligence — Management system*. ISO/IEC 42001:2023 (première norme certifiable de système de management de l'IA, AIMS, décembre 2023).
- ISO/IEC JTC 1/SC 42 (2025). *Information technology — Artificial intelligence (AI) — AI system impact assessment*. ISO/IEC 42005:2025 (mai 2025 ; companion de ISO/IEC 42001).
- Model Context Protocol (Anthropic et contributeurs) (2024). *Model Context Protocol Specification, version 2024-11-05*. https://modelcontextprotocol.io/specification/2024-11-05.
- Model Context Protocol (2025). *Model Context Protocol Specification, version 2025-06-18* (primitives tools/resources/prompts, sorties structurées, elicitation, couche d'autorisation par découverte OAuth/OIDC avec indication de ressource RFC 8707). https://modelcontextprotocol.io/specification/2025-06-18.
- OpenAI ; Stripe (2025). *Agentic Commerce Protocol (ACP — sigle « ACP » pour le paiement/commerce agentique ; à distinguer de l'Agent Communication Protocol homonyme)*. Spécification ouverte, licence Apache 2.0 (beta). https://github.com/agentic-commerce-protocol/agentic-commerce-protocol. ⚠
- OpenTelemetry Authors (CNCF) (2025-2026). *Semantic Conventions for Generative AI (GenAI spans, agent/framework spans, metrics, events)*. Statut Development. https://github.com/open-telemetry/semantic-conventions-genai. ⚠

## 4. Référentiels de sécurité et de gouvernance

- Aim Security / Aim Labs (2025). *EchoLeak: A Zero-Click AI Vulnerability in Microsoft 365 Copilot (CVE-2025-32711)*. Avis de sécurité (11 juin 2025 ; exfiltration *zero-click* par injection d'invite indirecte). https://www.aim.security/lp/aim-labs-echoleak-blogpost. ⚠
- Andriushchenko, M.; Souly, A.; Dziemian, M.; Duenas, D.; Lin, M.; Wang, J.; Hendrycks, D.; Zou, A.; Kolter, Z.; Fredrikson, M.; Winsor, E.; Wynne, J.; Gal, Y.; Davies, X. (2024). *AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents*. arXiv:2410.09024 (ICLR 2025).
- Anthropic (Lynch, A.; et al.) (2025a). *Agentic Misalignment: How LLMs could be insider threats*. Anthropic Research (juin 2025). https://www.anthropic.com/research/agentic-misalignment. ⚠
- Beurer-Kellner, L.; Buesser, B.; Creţu, A.-M.; Debenedetti, E.; Dobos, D.; Fabian, D.; Fischer, M.; Froelicher, D.; Grosse, K.; Naeff, D.; Ozoani, E.; Paverd, A.; Tramèr, F.; Volhejn, V. (2025). *Design Patterns for Securing LLM Agents against Prompt Injections*. arXiv:2506.08837.
- Cloud Security Alliance (CSA) (2026). *NIST AI Risk Management Framework: Agentic Profile*. White paper (DRAFT, 2026-03-27 ; architecture AAGATE, AI Controls Matrix v1.0). https://labs.cloudsecurityalliance.org/agentic/agentic-nist-ai-rmf-profile-v1/. ⚠
- Meta AI (Security team) (2025). *Agents Rule of Two: A Practical Approach to AI Agent Security*. Meta AI Blog (31 oct. 2025). https://ai.meta.com/blog/practical-ai-agent-security/.
- METR (Model Evaluation & Threat Research) (2025). *Recent Frontier Models Are Reward Hacking*. METR (5 juin 2025). https://metr.org/blog/2025-06-05-recent-reward-hacking/.
- MITRE Corporation (2021 ; base vivante). *MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)*. Origine 2020 (Adversarial ML Threat Matrix) ; version courante v2026.05 (27 mai 2026). https://atlas.mitre.org/. ⚠
- NIST (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1 (26 jan. 2023 ; fonctions Govern/Map/Measure/Manage). DOI:10.6028/NIST.AI.100-1.
- NIST (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. NIST AI 600-1 (26 juil. 2024 ; 12 catégories de risque GenAI). DOI:10.6028/NIST.AI.600-1.
- OWASP Gen AI Security Project (2025). *OWASP Top 10 for LLM Applications 2025*. OWASP Foundation (LLM01 Prompt Injection, LLM06 Excessive Agency). https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/.
- OWASP GenAI Security Project / Agentic Security Initiative (2025). *OWASP Top 10 for Agentic Applications (for 2026)*. OWASP Foundation (publié 9 déc. 2025 ; ASI01 Agent Goal Hijack … ASI10 Rogue Agents). https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/. ⚠
- OWASP GenAI Security Project / Agentic Security Initiative (2025). *Agentic AI — Threats and Mitigations*. OWASP Foundation (taxonomie, cadre MAESTRO). https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/.
- OWASP Non-Human Identities Top 10 Project (2025). *OWASP Non-Human Identities Top 10 — 2025*. OWASP Foundation (NHI1 Improper Offboarding, NHI2 Secret Leakage, NHI5 Overprivileged NHI…). https://owasp.org/www-project-non-human-identities-top-10/2025/.
- Willison, S. (2023). *The Dual LLM pattern for building AI assistants that can resist prompt injection*. Simon Willison's Weblog (25 avril 2023). https://simonwillison.net/2023/Apr/25/dual-llm-pattern/.
- Willison, S. (2025b). *The lethal trifecta for AI agents: private data, untrusted content, and external communication*. Simon Willison's Weblog (16 juin 2025). https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/.

## 5. Réglementation

- Commission européenne (2025). *Digital Omnibus on AI — simplification ciblée de la législation sur l'IA*. Proposition législative (19 nov. 2025) ; report adopté dans la fenêtre du socle (accord en trilogue le 7 mai 2026, vote du Parlement européen le 16 juin, feu vert du Conseil le 29 juin 2026 ; Annexe III → 2 déc. 2027, Annexe I → 2 août 2028), publication au JOUE à suivre. https://digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal. ⚠
- Parlement européen et Conseil de l'UE (2024). *Règlement (UE) 2024/1689 du 13 juin 2024 établissant des règles harmonisées concernant l'intelligence artificielle (AI Act)*. JO de l'UE (OJ L, 2024/1689, 12.7.2024 ; en vigueur le 1er août 2024). http://data.europa.eu/eli/reg/2024/1689/oj.

## 6. Ressources praticiennes (frameworks, blogs d'ingénierie, modèles, bancs d'essai, rapports)

- AGNTCY Project (initié par Cisco) / Linux Foundation (2025). *AGNTCY documentation (Internet of Agents interoperability)*. Ouvert par Cisco (mars 2025), donné à la Linux Foundation (juil. 2025) ; interopérable avec A2A et MCP. https://docs.agntcy.org/. ⚠
- Anthropic (2024a). *Building Effective Agents*. Anthropic Engineering (19 déc. 2024 ; définition « systems where LLMs dynamically direct their own processes and tool usage » ; distinction workflows/agents). https://www.anthropic.com/engineering/building-effective-agents.
- Anthropic (2024b). *Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku*. Annonce officielle (22 oct. 2024 ; première capacité « computer use » en beta publique). https://www.anthropic.com/news/3-5-models-and-computer-use.
- Anthropic (2025b). *Donating the Model Context Protocol and establishing the Agentic AI Foundation*. Annonce (9 déc. 2025). https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation.
- Anthropic (2025c). *Effective context engineering for AI agents*. Anthropic Engineering (sept. 2025). https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents.
- Anthropic (2025d). *How we built our multi-agent research system*. Anthropic Engineering (13 juin 2025 ; architecture orchestrateur-travailleurs). https://www.anthropic.com/engineering/multi-agent-research-system.
- Anthropic (2025e). *Memory tool* et *Context management / context editing* (compaction, beta context-management-2025-06-27). Documentation produit. https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool. ⚠
- Anthropic (Appel, R.; Tamkin, A.; et al.) (2026). *The Anthropic Economic Index report: Economic primitives*. Rapport de recherche (15 jan. 2026). https://www.anthropic.com/research/anthropic-economic-index-january-2026-report. ⚠
- Arize AI et communauté open source (2026). *Arize Phoenix: Open-Source AI Observability & Evaluation (avec OpenInference)*. Bâti sur OpenTelemetry. https://github.com/Arize-ai/phoenix. ⚠
- CrewAI Inc. (2025). *CrewAI documentation: Flows (et Crews)*. Documentation officielle (Flows event-driven + Crews role-based). https://docs.crewai.com/en/concepts/flows. ⚠
- DBOS, Inc. (2025). *DBOS Transact: durable workflows on Postgres*. Documentation officielle (checkpoint d'état, reprise, queues durables ; Python/TS/Go/Java/Kotlin). https://docs.dbos.dev/. ⚠
- Google (Google Cloud) (2025). *Agent Development Kit (ADK) documentation*. Toolkit code-first multi-agents (Python, Java, Go, TypeScript, Kotlin ; support MCP). https://adk.dev/. ⚠
- Google Developers (2025). *Agent Development Kit: Making it easy to build multi-agent applications*. Google Developers Blog (Google Cloud NEXT 2025, avril 2025). https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/.
- Guo, Z.; Cheng, S.; Wang, H.; Liang, S.; Qin, Y.; Li, P.; Liu, Z.; Sun, M.; Liu, Y. (2024). *StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models*. arXiv:2403.07714 (Findings of ACL 2024). *(contexte non cité)*
- IBM (2024-2026). *Portefeuille AIOps et observabilité* — IBM Concert (et Concert Resilience), IBM Instana Observability, IBM Turbonomic (Application Resource Management), IBM SevOne, IBM Cloud Pak for AIOps (anc. Cloud Pak for Watson AIOps). Plateformes d'opérations agentiques, observabilité full-stack et optimisation de ressources ; la catégorie « AIOps » a été nommée par Gartner vers 2017. https://www.ibm.com/products/instana. ⚠
- LangChain (The LangChain Team) ; version originale : Martin, L. (2025). *Context Engineering (LangChain) / Context Engineering for Agents* (taxonomie write/select/compress/isolate). https://www.langchain.com/blog/context-engineering-for-agents ; https://rlancemartin.github.io/2025/06/23/context_engineering/.
- LangChain, Inc. (2025). *LangGraph 1.0 is now generally available*. Changelog/Blog (22 oct. 2025). https://changelog.langchain.com/announcements/langgraph-1-0-is-now-generally-available.
- LangChain, Inc. (2025). *Durable execution (LangGraph documentation)* (checkpointer, persistence, human-in-the-loop). https://docs.langchain.com/oss/python/langgraph/durable-execution. ⚠
- LangChain, Inc. (2026). *langgraph (PyPI package, versions datées)*. PyPI (à la vérification : 1.2.7, 30 juin 2026, MIT, Python 3.10+). https://pypi.org/project/langgraph/. ⚠
- LangChain, Inc. (2026). *LangSmith: AI Agent & LLM Observability and Evaluation Platform* (agnostique au framework). https://docs.langchain.com/langsmith/observability. ⚠
- Langfuse (Langfuse GmbH) (2026). *Langfuse: Open Source LLM Engineering Platform — Observability & Tracing* (evals, observabilité, gestion de prompts, datasets ; intégration OpenTelemetry). https://langfuse.com/docs. ⚠
- Letta (anciennement MemGPT) (2024). *MemGPT Is Now Part of Letta*. Letta Blog (23 sept. 2024 ; mémoire trois niveaux core/archival/recall, ADE). https://www.letta.com/blog/memgpt-and-letta.
- Linux Foundation (Anthropic/MCP, Block/goose, OpenAI/AGENTS.md) (2025). *Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF)…*. Communiqué (9 déc. 2025). https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation.
- Linux Foundation ; Google (2026). *A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year*. Communiqué (9 avril 2026, premier anniversaire d'A2A). https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year. ⚠
- LlamaIndex (2025). *Announcing Workflows 1.0: a lightweight framework for agentic systems*. LlamaIndex Blog (event-driven step/event ; Python et TypeScript). https://www.llamaindex.ai/blog/announcing-workflows-1-0-a-lightweight-framework-for-agentic-systems.
- LlamaIndex (2025). *Workflows (documentation officielle)*. https://developers.llamaindex.ai/python/llamaagents/workflows/. ⚠
- Microsoft (2025). *Introducing Microsoft Agent Framework (public preview)*. Microsoft Learn / Azure Blog (1 oct. 2025 ; convergence AutoGen + Semantic Kernel ; support MCP/A2A ; Python et .NET). https://learn.microsoft.com/en-us/agent-framework/overview/.
- Microsoft (2025). *Introduction to Semantic Kernel*. Microsoft Learn (kernel, plugins, planners ; C#, Python, Java). https://learn.microsoft.com/en-us/semantic-kernel/overview/.
- Microsoft (2026). *Microsoft Agent Framework Version 1.0*. Microsoft DevBlogs/Learn (version production-ready publiée le 3 avril 2026 pour Python et .NET). https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/. ⚠
- OpenAI (2023). *Function calling and other API updates*. OpenAI Blog/changelog (13 juin 2023). https://openai.com/index/function-calling-and-other-api-updates/.
- OpenAI (Preparedness ; avec les auteurs de SWE-bench) (2024a). *Introducing SWE-bench Verified*. OpenAI (13 août 2024 ; sous-ensemble humain-validé de 500 tâches). https://openai.com/index/introducing-swe-bench-verified/.
- OpenAI (2024b). *OpenAI o1 System Card*. OpenAI (5 déc. 2024 ; alignement délibératif). arXiv:2412.16720.
- OpenAI (2025a). *A Practical Guide to Building Agents*. Guide PDF (17 avril 2025, 34 pages). https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf.
- OpenAI (2025b). *Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol*. Annonce produit (sept. 2025 ; co-développé avec Stripe). https://openai.com/index/buy-it-in-chatgpt/.
- OpenAI (2025c). *Computer-Using Agent (CUA) / Introducing Operator*. Annonce (23 jan. 2025 ; boucle screenshot → raisonnement → action). https://openai.com/index/computer-using-agent/.
- OpenAI (2025d). *New tools for building agents (Responses API, Agents SDK)*. Annonce produit (11 mars 2025). https://openai.com/index/new-tools-for-building-agents/.
- OpenAI (2025e). *OpenAI Agents SDK (documentation officielle)*. Framework Python léger (agents, handoffs, agents-as-tools, guardrails, tracing ; successeur de Swarm). https://openai.github.io/openai-agents-python/. ⚠
- OpenAI (2025f). *OpenAI co-founds the Agentic AI Foundation under the Linux Foundation*. Annonce (déc. 2025 ; donation d'AGENTS.md). https://openai.com/index/agentic-ai-foundation/.
- Patil, S. G.; et al. (Gorilla LLM / UC Berkeley Sky Computing Lab) (2024). *Berkeley Function-Calling Leaderboard (BFCL)*. Blog + leaderboard + dépôt (évaluation AST, appels séries/parallèles, multi-langage). https://gorilla.cs.berkeley.edu/leaderboard.html. ⚠
- Pydantic (Pydantic Services Inc.) (2025). *Durable Execution — Temporal (Pydantic AI documentation)* (TemporalAgent, activities, retries, intégration Logfire). https://pydantic.dev/docs/ai/integrations/durable_execution/temporal/. ⚠
- Stanford Institute for Human-Centered AI (HAI) (2025). *The 2025 AI Index Report*. Rapport annuel (avril 2025). https://hai.stanford.edu/ai-index/2025-ai-index-report.
- Temporal Technologies (2025). *Temporal documentation: Durable Execution et Temporal for AI*. Documentation officielle (workflows déterministes + activities, event history, replay ; intégration OpenAI Agents SDK). https://docs.temporal.io/. ⚠
- Visa ; Mastercard (2025). *Visa and Mastercard both launch new agentic AI payments tools (Visa Trusted Agent Protocol / Mastercard Agent Pay)*. Couverture Digital Commerce 360 (16 oct. 2025 ; sources primaires : Visa Trusted Agent Protocol 14 oct. 2025, Mastercard Agent Pay 29 avril 2025). https://www.digitalcommerce360.com/2025/10/16/visa-mastercard-both-launch-agentic-ai-payments-tools/. ⚠
- Willison, S. (2025a). *I think « agent » may finally have a widely enough agreed upon definition to be useful jargon now*. Simon Willison's Weblog/Newsletter (18 sept. 2025 ; définition « an LLM agent runs tools in a loop to achieve a goal »). https://simonwillison.net/2025/Sep/18/agents/.
- Yan, W. (Cognition) (2025). *Don't Build Multi-Agents*. Cognition AI Blog (juin 2025 ; single writer / continuous context). https://cognition.ai/blog/dont-build-multi-agents.

---

### Annexe — vérification

La passe de vérification adverse a **confirmé 229 références** et **corrigé 17** (aucune écartée comme non vérifiable). Corrections types intégrées : rattachement d'un surnom de papier au bon arXiv id, distinction année arXiv vs année de conférence, séparation des deux « CRAG » (Corrective RAG `2401.15884` vs benchmark `2406.04744`), métadonnées d'auteurs/venue rectifiées. Doublons fusionnés : ReAct (4 occurrences), Generative Agents (3), Toolformer (3), Russell & Norvig (3), Wooldridge & Jennings (3), etc.

*Les entrées marquées ⚠ sont des ressources vivantes (doc produit/framework, spec versionnée par date, prépublication, draft, version de paquet) : fixer la version/l'ancre/le statut exact au moment de citer.*
