# Bibliographie — Chapitre 3 : L'interopérabilité agentique

*Bibliographie du chapitre 3 (interopérabilité agentique : entre agents, outils, modèles, cadriciels et organisations), arrêtée à juin 2026.*

**Convention de citation.** Auteurs/Organisme (Année). *Titre*. Support/venue. Identifiant stable (arXiv / DOI / RFC / révision datée de spec / URL). Six catégories ; ordre alphabétique par auteur/organisme (par identifiant/date pour les specs et RFC).

**Méthode.** Recherche en éventail sur 12 sous-domaines, puis vérification adverse de chaque citation sur le web (existence, auteurs, année, arXiv id, RFC, révision datée de spec), enfin dédoublonnage. Bilan : **194 références vérifiées → 165 entrées ; 170 confirmées, 24 corrigées, 0 non vérifiable.** Détail du compte : après fusion des doublons, 163 entrées ; le quasi-doublon South et al. / whitepaper OpenID AIIM (même arXiv:2510.25819) a été fusionné en une entrée unique (−1) ; puis trois entrées de veille ont été ajoutées (+3) — CSA *MCP Security Crisis* (4 mai 2026), divulgation OX Security stdio (avril 2026), IETF draft-klrc-aiagent-auth-02 (1ᵉʳ juin 2026) —, **non re-vérifiées en adverse dans cette passe** (à confirmer sur le web avant publication ; marquées ⚠). Pièges du domaine traités : révisions datées de MCP citées à leur date ; sigle « ACP » distingué (Agent Communication Protocol IBM/BeeAI vs Agentic Commerce Protocol OpenAI/Stripe) ; A2A v1.0.0 (12 mars 2026), courant v1.0.1 (28 mai 2026) ; AP2 gouverné par la FIDO Alliance (pas la Linux Foundation) ; x402 annoncé le 23 sept. 2025, x402 Foundation constituée sous la Linux Foundation le 2 avril 2026 ; MPP réglé on-chain via Tempo (x402 = flux compatible, pas le rail).

**Marqueur ⚠ — abondant ici, et c'est normal.** L'interopérabilité agentique est un domaine de frontière : la majorité des sources sont des *ressources vivantes* (specs versionnées par date, drafts IETF/W3C en cours, prépublications arXiv 2025-2026, docs produit). Le ⚠ signale qu'il faut fixer la version/révision/statut exact au moment de citer.

**Réserve de forme.** Les renvois « référence → section » de la sortie brute (étiquettes thématiques) ne sont pas reportés ici pour la lisibilité ; un index thématique alignable sur la TOC peut être régénéré sur demande.

---

## 1. Ouvrages et articles fondateurs (communication d'agents, interopérabilité, avant l'ère LLM)

- Austin, John L. (1962). *How to Do Things with Words* (eds. J. O. Urmson & M. Sbisà). Oxford : Clarendon Press / Oxford University Press (William James Lectures, Harvard 1955). ISBN 978-0198245537 (2e éd. 1975).
- Clark, Herbert H. & Brennan, Susan E. (1991). *Grounding in Communication*. In L. B. Resnick, J. M. Levine & S. D. Teasley (Eds.), *Perspectives on Socially Shared Cognition*, pp. 127-149. Washington DC : American Psychological Association. DOI 10.1037/10096-006.
- Finin, Tim ; Fritzson, Richard ; McKay, Don ; McEntire, Robin (1994). *KQML as an Agent Communication Language*. Proceedings of CIKM '94, ACM, pp. 456-463. DOI 10.1145/191246.191322.
- FIPA (2002). *FIPA ACL Message Structure Specification*. FIPA Standard (2002-12-03), repris par l'IEEE Computer Society (2005). FIPA SC00061G. ⚠
- FIPA (2002). *FIPA Communicative Act Library Specification*. FIPA Standard (2002-12-03). FIPA SC00037J. ⚠
- FIPA (2002). *FIPA Contract Net Interaction Protocol Specification*. FIPA Standard (2002-12-03). FIPA SC00029H. ⚠
- FIPA (2002). *FIPA SL Content Language Specification*. FIPA Standard (2002-12). FIPA SC00008I. ⚠
- Grice, H. Paul (1975). *Logic and Conversation*. In P. Cole & J. L. Morgan (Eds.), *Syntax and Semantics, Vol. 3 : Speech Acts*, pp. 41-58. New York : Academic Press. DOI 10.1163/9789004368811_003 (édition Brill).
- Labrou, Yannis & Finin, Tim (1994). *A Semantics Approach for KQML*. Proceedings of CIKM '94, ACM, pp. 447-455. DOI 10.1145/191246.191320.
- Labrou, Yannis & Finin, Timothy (1997). *Semantics and Conversations for an Agent Communication Language*. Proceedings of IJCAI-97, Nagoya, pp. 584-591. arXiv:cs/9809034.
- Rao, Anand S. & Georgeff, Michael P. (1995). *BDI Agents : From Theory to Practice*. Proceedings of ICMAS-95, AAAI Press, pp. 312-319. cdn.aaai.org/ICMAS/1995/ICMAS95-042.pdf.
- Searle, John R. (1969). *Speech Acts : An Essay in the Philosophy of Language*. Cambridge University Press. ISBN 978-0521096263 ; DOI 10.1017/CBO9781139173438.
- Singh, Munindar P. (1998). *Agent Communication Languages : Rethinking the Principles*. IEEE Computer, vol. 31, no. 12, pp. 40-47. DOI 10.1109/2.735849.
- Singh, Munindar P. (2000). *A Social Semantics for Agent Communication Languages*. In *Issues in Agent Communication*, LNAI vol. 1916, Springer, pp. 31-45. DOI 10.1007/10722777_3.
- Smith, Reid G. (1980). *The Contract Net Protocol : High-Level Communication and Control in a Distributed Problem Solver*. IEEE Transactions on Computers, vol. C-29, no. 12, pp. 1104-1113. DOI 10.1109/TC.1980.1675516.
- Sperber, Dan & Wilson, Deirdre (1995). *Relevance : Communication and Cognition* (2e éd.). Oxford : Blackwell (1re éd. 1986). ISBN 978-0631198789.
- Tolk, Andreas & Muguira, James A. (2003). *The Levels of Conceptual Interoperability Model (LCIM)*. Fall Simulation Interoperability Workshop, SISO. Paper 03F-SIW-007.
- Wang, Wenguang ; Tolk, Andreas ; Wang, Weiping (2009). *The Levels of Conceptual Interoperability Model : Applying Systems Engineering Principles to Modeling and Simulation*. SpringSim '09, Article 168. arXiv:0908.0191.
- Wegner, Peter (1996). *Interoperability*. ACM Computing Surveys, vol. 28, no. 1, pp. 285-287. DOI 10.1145/234313.234424.
- Yolum, Pinar & Singh, Munindar P. (2002). *Flexible Protocol Specification and Execution : Applying Event Calculus Planning Using Commitments*. Proceedings of AAMAS '02, ACM, pp. 527-534. DOI 10.1145/544862.544867.

## 2. Articles de recherche sur l'interopérabilité agentique (2023-2026)

- Anbiaee, Zeynab ; Rabbani, Mahdi ; Mirani, Mansur ; et al. (2026). *Security Threat Modeling for Emerging AI-Agent Protocols : A Comparative Analysis of MCP, A2A, Agora, and ANP*. arXiv:2602.11327.
- Balija, Sree Bhargavi ; Singal, Rekha ; Singh, Abhishek ; et al. (2025). *The Trust Fabric : Decentralized Interoperability and Economic Coordination for the Agentic Web*. arXiv:2507.07901.
- Bhardwaj, Varun Pratap (2026). *Agent Behavioral Contracts : Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents*. arXiv:2602.22302.
- Cemri, Mert ; Pan, Melissa Z. ; Yang, Shuyi ; et al. (2025). *Why Do Multi-Agent LLM Systems Fail?* (taxonomie MAST). arXiv:2503.13657 (NeurIPS 2025 Datasets & Benchmarks).
- Chen, Weize ; You, Ziming ; Li, Ran ; et al. (2024). *Internet of Agents : Weaving a Web of Heterogeneous Agents for Collaborative Intelligence*. arXiv:2407.07061.
- Debi, Tanusree ; Zhu, Wentian ; Sen Gupta, Pranjol (2026). *Whispers of Wealth : Red-Teaming Google's Agent Payments Protocol via Prompt Injection*. arXiv:2601.22569.
- Du, Chenguang ; Wang, Chuyi ; Chao, Yihan ; Xie, Xiaohui ; Cui, Yong (2025). *AI Agent Communication from Internet Architecture Perspective : Challenges and Opportunities*. arXiv:2509.02317.
- Du, Hongyi ; Su, Jiaqi ; Li, Jisen ; et al. (2025). *Which LLM Multi-Agent Protocol to Choose?* (benchmark ProtocolBench). arXiv:2510.17149.
- Ehtesham, Abul ; Singh, Aditi ; Gupta, Gaurav Kumar ; Kumar, Saket (2025). *A survey of agent interoperability protocols : MCP, ACP, A2A, and ANP*. arXiv:2505.02279v2 (v2, 23 mai 2025 ; antérieur à la révision MCP 2025-11-25, donc pré-*Tasks* asynchrones). ⚠
- Fleming, Charles ; Muscariello, Luca ; Pandey, Vijoy ; Kompella, Ramana (2025). *A Layered Protocol Architecture for the Internet of Agents*. arXiv:2511.19699.
- Gupta, Aayush (2026). *ReliabilityBench : Evaluating LLM Agent Reliability Under Production-Like Stress Conditions*. arXiv:2601.06112.
- Hou, Xinyi ; Zhao, Yanjie ; Wang, Shenao ; Wang, Haoyu (2025). *Model Context Protocol (MCP) : Landscape, Security Threats, and Future Research Directions*. arXiv:2503.23278.
- Huang, Ken ; Narajala, Vineeth Sai ; Habler, Idan ; Sheriff, Akram (2025). *Agent Name Service (ANS) : A Universal Directory for Secure AI Agent Discovery and Interoperability*. arXiv:2505.10609 (endossé OWASP GenAI/ASI).
- Huang, Ken ; Narajala, Vineeth Sai ; Yeoh, Jerry ; et al. (2025). *A Novel Zero-Trust Identity Framework for Agentic AI : Decentralized Authentication and Fine-Grained Access Control*. arXiv:2505.19301.
- Ioannides, Georgios ; Constantinou, Christos ; Jain, Vinija ; Chadha, Aman ; Elkins, Aaron (2025). *MOD-X : A Modular Open Decentralized eXchange Framework for Heterogeneous Interoperable AI Agents*. arXiv:2507.04376.
- Jamshidi, Saeid ; Moradi Dakhel, Arghavan ; Nafi, Kawser Wazed ; Khomh, Foutse (2026). *Hallucination Cascade : Analyzing Error Propagation in Multi-Agent LLM Systems*. arXiv:2606.07937.
- Kong, Dezhang ; Lin, Shi ; Xu, Zhenhua ; et al. (Zhang, Ningyu ; Han, Meng) (2025). *A Survey of LLM-Driven AI Agent Communication : Protocols, Security Risks, and Defense Countermeasures*. arXiv:2506.19676.
- Kotte, Varun (2026). *PromptPort : A Reliability Layer for Cross-Model Structured Extraction*. arXiv:2601.06151.
- Lee, Wilson Y. (2026). *Capable but Unreliable : Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks*. arXiv:2602.19008.
- Lin, Bohan ; Yang, Kuo ; Tan, Zelin ; et al. (2025). *AgentAsk : Multi-Agent Systems Need to Ask*. arXiv:2510.07593.
- Louck, Yedidel ; Stulman, Ariel ; Dvir, Amit (2025). *Security Analysis of Agentic AI Communication Protocols : A Comparative Evaluation*. arXiv:2511.03841 ; ACM Transactions on AI Security and Privacy (en ligne 25 mars 2026), DOI 10.1145/3803431.
- Maloyan, Narek & Namiot, Dmitry (2026). *Breaking the Protocol : Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents*. arXiv:2601.17549. *(contexte non cité)*
- Muscariello, Luca ; Pandey, Vijoy ; Polic, Ramiz (2025). *The AGNTCY Agent Directory Service : Architecture and Implementation*. arXiv:2509.18787.
- Patel, Khush ; Surendira, Siva ; George, Jithin ; Kapale, Shreyas (2026). *The Six Sigma Agent : Achieving Enterprise-Grade Reliability in LLM Systems Through Consensus-Driven Decomposed Execution*. arXiv:2601.22290.
- Petrova, Tatiana ; Bliznioukov, Boris ; Puzikov, Aleksandr ; State, Radu (2025). *From Semantic Web and MAS to Agentic AI : A Unified Narrative of the Web of Agents*. arXiv:2507.10644.
- Qiang, Zhangcheng ; Wang, Weiqing ; Taylor, Kerry (2024). *Agent-OM : Leveraging LLM Agents for Ontology Matching*. PVLDB, vol. 18, no. 3, pp. 516-529. arXiv:2312.00326.
- Rabanser, Stephan ; Kapoor, Sayash ; Kirgis, Peter ; et al. (2026). *Towards a Science of AI Agent Reliability*. arXiv:2602.16666 (accepté à ICML 2026).
- Raskar, Ramesh ; Chari, Pradyumna ; Zinky, John ; et al. (2025). *Beyond DNS : Unlocking the Internet of AI Agents via the NANDA Index and Verified AgentFacts*. arXiv:2507.14263 (MIT Media Lab / Project NANDA).
- Sarkar, Anjana & Sarkar, Soumyendu (2025). *Survey of LLM Agent Communication with MCP : A Software Design Pattern Centric Review*. arXiv:2506.05364.
- Sharma, Rishi ; de Vos, Martijn ; Chari, Pradyumna ; Raskar, Ramesh ; Kermarrec, Anne-Marie (2025). *Collaborative Agentic AI Needs Interoperability Across Ecosystems* (position paper, EPFL/MIT). arXiv:2505.21550.
- Singh, Aditi ; Ehtesham, Abul ; Lambe, Mahesh ; et al. (2025). *Evolution of AI Agent Registry Solutions : Centralized, Enterprise, and Distributed Approaches*. arXiv:2508.03095.
- South, Tobin ; Cecchetti, S. ; Fletcher, G. ; et al. (OpenID Foundation, AIIM Community Group) (2025). *Identity Management for Agentic AI: The new frontier of authorization, authentication, and security for an AI agent world*. OpenID Foundation (whitepaper, 7 oct. 2025) ; arXiv:2510.25819. [Whitepaper OpenID et sa prépublication arXiv sont le même document ; entrée unique, cf. cat. 4 fusionnée ici.]
- Tuan, Thanh Luong & Sanyal, Abhijit (2026). *Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems : A Neurosymbolic Architecture for Domain-Grounded AI Agents*. arXiv:2604.00555.
- Wang, Yaxuan ; Liu, Quan ; Wang, Zhenting ; et al. (2025). *PromptBridge : Cross-Model Prompt Transfer for Large Language Models*. arXiv:2512.01420.
- Xie, Yizhe ; Zhu, Congcong ; Zhang, Xinyue ; et al. (2026). *From Spark to Fire : Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration*. arXiv:2603.04474.
- Xu, Wenxin ; Wang, Taotao ; Xia, Yihan ; Zhang, Shengli ; Liew, Soung Chang (2026). *Agent-OSI : A Layered Protocol Stack Toward a Decentralized Internet of Agents*. arXiv:2602.13795.
- Yang, Yingxuan ; Chai, Huacan ; Song, Yuanyi ; et al. (Zhang, Weinan) (2025). *A Survey of AI Agent Protocols* (Shanghai Jiao Tong University). arXiv:2504.16736.
- Yang, Yingxuan ; Ma, Mulei ; Huang, Yuxuan ; et al. (Zhang, Weinan ; Wang, Jun) (2025). *Agentic Web : Weaving the Next Web with AI Agents*. arXiv:2507.21206.
- Yuan, Dun ; Lyu, Fuyuan ; Yuan, Ye ; et al. (Liu, Xue) (2026). *Beyond Message Passing : A Semantic View of Agent Communication Protocols*. arXiv:2604.02369. [Prépublication ⚠ : fixer le numéro de version arXiv au moment de citer.] ⚠
- Zheng, Lifan ; Chen, Jiawei ; Yin, Qinghong ; et al. (2025). *Rethinking the Reliability of Multi-agent System : A Perspective from Byzantine Fault Tolerance*. arXiv:2511.10400.
- Zhu, Kunlun ; Liu, Zijia ; Li, Bingxuan ; et al. (You, Jiaxuan) (2025). *Where LLM Agents Fail and How They can Learn From Failures*. arXiv:2509.25370.

## 3. Spécifications et protocoles (MCP / A2A / ANP / ACP / AP2 / x402 + RFC et standards Web)

- A2A Project / Linux Foundation (2026). *Agent2Agent (A2A) Protocol Specification, v1.0.0* (Agent Card, Signed Agent Cards via JWS+JCS, bindings JSON-RPC 2.0 / gRPC / HTTP+JSON). a2a-protocol.org/latest/specification/. ⚠
- Agent Network Protocol Community (2025). *AgentNetworkProtocol (ANP) — specifications* (dont did:wba Method Design Specification). GitHub agent-network-protocol/AgentNetworkProtocol. ⚠
- Agent Network Protocol (2025). *did:wba Method Specification (Web-Based Agent DID Method), v0.2* (auth HTTP via RFC 9421 et RFC 9530). agent-network-protocol.com/specs/did-method.html. ⚠
- Anthropic / MCP maintainers (2024). *Model Context Protocol Specification — Revision 2024-11-05* (release initiale). modelcontextprotocol.io/specification/2024-11-05. ⚠
- Anthropic / MCP maintainers (2025). *MCP Specification — Revision 2025-03-26* (cadre d'autorisation OAuth, transport Streamable HTTP). modelcontextprotocol.io/specification/2025-03-26. ⚠
- Anthropic / MCP maintainers (2025). *MCP Specification — Revision 2025-06-18* (Elicitation, Roots, sorties structurées, OAuth Resource Server). modelcontextprotocol.io/specification/2025-06-18. ⚠
- MCP maintainers (Anthropic, OpenAI, GitHub, Block, communauté) (2025). *MCP Specification — Revision 2025-11-25* (OIDC Discovery, tasks expérimentaux SEP-1686, URL-mode elicitation SEP-1036, OAuth CIMD SEP-991, JSON Schema 2020-12 SEP-1613, gouvernance SEP-932, tiering SDK SEP-1730). modelcontextprotocol.io/specification/2025-11-25/changelog. ⚠
- MCP Core Maintainers (OpenAI, Anthropic) avec le UI Community Working Group (créateurs MCP-UI) (2025). *MCP Apps : Extending servers with interactive user interfaces* (SEP-1865 ; schéma ui:// et iframes sandboxées). blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/. ⚠
- IBM Research / BeeAI (i-am-bee), Linux Foundation (2025). *Agent Communication Protocol (ACP) — projet BeeAI* (REST/HTTP, découverte hors-ligne, messages multipart MIME). agentcommunicationprotocol.dev. [ACP-agent IBM/BeeAI, fusionné dans A2A août 2025 ; distinct de l'ACP-commerce OpenAI/Stripe.] ⚠
- Chang, Gaowei ; et al. (Agent Network Protocol) (2025). *Agent Network Protocol (ANP) Technical White Paper* (architecture 3 couches : DID W3C, méta-protocole de négociation, protocole applicatif, JSON-LD). arXiv:2508.00007.
- W3C AI Agent Protocol Community Group (2025). *Agent Network Protocol White Paper*. W3C CG Draft Report, w3c-cg.github.io/ai-agent-protocol/. ⚠
- OpenAI, Stripe (2025-2026). *Agentic Commerce Protocol (ACP) — Specification* (Checkout API, Delegate Payment ; versions datées : 2025-09-29 initiale, 2025-12-12, 2026-01-16, 2026-01-30, 2026-04-17). GitHub agentic-commerce-protocol. [ACP-commerce, distinct de l'ACP-agent IBM/BeeAI.] ⚠
- Google (gouvernance transférée à la FIDO Alliance) (2025-2026). *Agent Payments Protocol (AP2) — Specification* (mandats Intent/Cart/Payment comme Verifiable Credentials W3C ; v0.2 le 2026-04-28, support Human-Not-Present). GitHub google-agentic-commerce/AP2 ; ap2-protocol.org. [Gouvernance FIDO Alliance, PAS Linux Foundation.] ⚠
- Coinbase ; x402 Foundation (sous Linux Foundation, avec Cloudflare et Stripe) (2025-2026). *x402 — A payments protocol for the internet, built on HTTP* (HTTP 402 ; « x402 V2 »). GitHub coinbase/x402 ; x402.org (annonce conjointe Cloudflare + Coinbase le 2025-09-23 ; constitution formelle de la x402 Foundation sous la Linux Foundation le 2026-04-02). ⚠
- Stripe, Tempo (2026). *Machine Payments Protocol (MPP) — open standard for billing AI agents over HTTP* (HTTP 402 ; stablecoins via Tempo on-chain, cartes/BNPL via Shared Payment Tokens). mpp.dev (lancement 2026-03-18). ⚠
- Google (avec Shopify, Etsy, Wayfair, Target, Walmart) (2026). *Universal Commerce Protocol (UCP)* (transports API/A2A/MCP ; découverte/panier/achat/suivi ; compatible AP2). ucp.dev (annonce 2026-01-11, NRF Big Show). ⚠
- Visa (avec Cloudflare) (2025). *Trusted Agent Protocol (TAP)* (signe l'identité de l'agent dans des en-têtes HTTP via RFC 9421 / Web Bot Auth ; Ed25519). GitHub visa/trusted-agent-protocol (annonce 2025-10-14). ⚠
- OpenAI (puis Agentic AI Foundation / Linux Foundation) (2025). *AGENTS.md — format ouvert et tool-agnostique d'instructions de projet* (publié août 2025 ; contribution fondatrice à l'AAIF, 9 déc. 2025). agents.md. ⚠
- CopilotKit (et communauté AG-UI) (2025). *AG-UI (Agent-User Interaction Protocol)* (HTTP POST + SSE, protobuf optionnel) entre front-end et backend agentique. copilotkit.ai/ag-ui ; GitHub ag-ui-protocol/ag-ui. ⚠
- OpenAI (2025). *Responses API* (interface unifiée à primitives agentiques ; Assistants API dépréciée 2025-08-26, sunset 2026-08-26). developers.openai.com/api/reference/responses/. ⚠
- Anthropic (2024). *Messages API* (API stateless de référence pour Claude ; format de fait émulé par des passerelles). docs.anthropic.com/en/api/messages. ⚠
- A2A Project / a2aproject (2025-2026). *A2A Technology Compatibility Kit (a2a-tck)* (suite de conformance pytest, 3 transports, filtrage RFC 2119). GitHub a2aproject/a2a-tck. ⚠
- Model Context Protocol organization (2025-2026). *MCP Conformance — framework for testing MCP client and server implementations* (cible les révisions datées). GitHub modelcontextprotocol/conformance. ⚠
- modelcontextprotocol (2024-2026). *MCP Inspector — Visual testing tool for MCP servers* (transports stdio/SSE/streamable-http). GitHub modelcontextprotocol/inspector. ⚠
- OpenTelemetry Authors (CNCF) (2025-2026). *Semantic Conventions for GenAI agent and framework spans* (statut Development/Experimental). opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/. ⚠
- Christensen, Erik ; Curbera, Francisco ; Meredith, Greg ; Weerawarana, Sanjiva (W3C) (2001). *Web Services Description Language (WSDL) 1.1*. W3C Note, 15 mars 2001.
- OASIS UDDI Specification TC (2004). *UDDI Version 3.0.2* (ratifié OASIS Standard fév. 2005). oasis-open.org/committees/uddi-spec/doc/spec/v3/uddi-v3.0.2-20041019.htm.
- Hardt, D. (Ed.) (2012). *The OAuth 2.0 Authorization Framework*. IETF RFC 6749.
- Richer, J. (Ed.) ; Jones, M. ; Bradley, J. ; Machulak, M. ; Hunt, P. (2015). *OAuth 2.0 Dynamic Client Registration Protocol*. IETF RFC 7591.
- Nottingham, M. (2019). *Well-Known Uniform Resource Identifiers (URIs)*. IETF RFC 8615 (obsolète RFC 5785).
- Jones, M. ; Nadalin, A. ; Campbell, B. (Ed.) ; Bradley, J. ; Mortimore, C. (2020). *OAuth 2.0 Token Exchange*. IETF RFC 8693.
- Campbell, B. ; Bradley, J. ; Tschofenig, H. (2020). *Resource Indicators for OAuth 2.0*. IETF RFC 8707. [Référencé par l'autorisation MCP 2025-06-18 pour confiner l'audience des jetons.]
- Backman, A. (Ed.) ; Richer, J. (Ed.) ; Sporny, M. (2024). *HTTP Message Signatures*. IETF RFC 9421.
- Jones, M. ; Hunt, P. ; Parecki, A. (2025). *OAuth 2.0 Protected Resource Metadata*. IETF RFC 9728. [Adoptée par l'autorisation MCP pour la découverte via .well-known.]
- Hardt, D. ; Parecki, A. ; Lodderstedt, T. (Eds.) (2026). *The OAuth 2.1 Authorization Framework*. IETF Internet-Draft, draft-ietf-oauth-v2-1-15 (mars 2026). ⚠
- Narajala, Vineeth Sai ; Huang, Ken ; Habler, Idan ; Sheriff, Akram (2025). *Agent Name Service (ANS)*. IETF Internet-Draft, draft-narajala-ans-00 (remplacé par ANS v2). ⚠
- Courtney, S. (GoDaddy) ; Narajala, V. S. ; Huang, K. ; Habler, I. ; Sheriff, A. (2026). *Agent Name Service v2 (ANS) : A Domain-Anchored Trust Layer for Autonomous AI Agent Identity*. IETF Internet-Draft, draft-narajala-courtney-ansv2-01 (2026-04-13). ⚠
- Mozley, Jim ; Williams, Nic ; Sarikaya, Behcet ; Schott, Roland ; Damick, Jeffrey (2026). *DNS for AI Discovery (DNS-AID)*. IETF Internet-Draft (dnsop), draft-mozleywilliams-dnsop-dnsaid-02 (2026-05-27). ⚠
- Mozley, Jim ; Williams, Nic ; Sarikaya, Behcet ; Schott, Roland (2025). *Brokered Agent Network for DNS AI Discovery (BANDAID)*. IETF Internet-Draft (dnsop), draft-mozleywilliams-dnsop-bandaid-00. ⚠
- W3C DID Working Group (Sporny, M. ; Guy, A. ; Sabadello, M. ; Reed, D., Eds.) (2022). *Decentralized Identifiers (DIDs) v1.0*. W3C Recommendation, 19 juillet 2022.
- W3C VC Working Group (Sporny, M. ; Thibodeau Jr, T. ; Herman, I. ; Cohen, G. ; Jones, M. B., Eds.) (2025). *Verifiable Credentials Data Model v2.0*. W3C Recommendation, 15 mai 2025.
- W3C Distributed Tracing Working Group (2021). *Trace Context (Level 1)*. W3C Recommendation, 23 novembre 2021.
- W3C Distributed Tracing Working Group (2024). *Trace Context Level 2*. W3C Candidate Recommendation Draft, 28 mars 2024. ⚠

## 4. Référentiels de sécurité, d'identité et de gouvernance

- Aim Labs / Aim Security (équipe EchoLeak) (2025). *EchoLeak : The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System*. arXiv:2509.10540 ; avis Microsoft MSRC CVE-2025-32711 (M365 Copilot, CVSS 9.3).
- Bhatt, Manish ; Narajala, Vineeth Sai ; Habler, Idan (2025). *ETDI : Mitigating Tool Squatting and Rug Pull Attacks in MCP by using OAuth-Enhanced Tool Definitions and Policy-Based Access Control*. arXiv:2506.01333.
- Cloud Security Alliance (Huang, K. ; Narajala, V. S. ; Yeoh, J. ; et al.) (2025). *Agentic AI Identity and Access Management : A New Approach*. CSA (artefact de recherche). cloudsecurityalliance.org/artifacts/agentic-ai-identity-and-access-management-a-new-approach. *(contexte non cité)*
- Cloud Security Alliance (Huang, Ken) (2025). *Agentic AI Threat Modeling Framework : MAESTRO* (7 couches). CSA blog (6 fév. 2025) + GitHub CloudSecurityAlliance/MAESTRO.
- Cloud Security Alliance (Huang, Ken ; Habler, Idan) (2025). *Threat Modeling Google's A2A Protocol with the MAESTRO Framework*. CSA blog (30 avril 2025). cloudsecurityalliance.org/blog/2025/04/30/threat-modeling-google-s-a2a-protocol-with-the-maestro-framework.
- Cloud Security Alliance (2026). *The MCP Security Crisis* (synthèse ≥ 7 CVE haute/critique sur des plateformes intégrant MCP ; recommandation zéro confiance à la couche outil). CSA / labs.cloudsecurityalliance.org (4 mai 2026). ⚠
- Debenedetti, Edoardo ; Zhang, Jie ; Balunović, Mislav ; et al. (2024). *AgentDojo : A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*. NeurIPS 2024 (Datasets & Benchmarks). arXiv:2406.13352.
- Debenedetti, Edoardo ; Shumailov, Ilia ; Fan, Tianqi ; et al. (2025). *Defeating Prompt Injections by Design (CaMeL)*. arXiv:2503.18813.
- FIDO Alliance (2026). *FIDO Alliance to Develop Standards for Trusted AI Agent Interactions* (Agentic Authentication TWG, Payments TWG ; bâtis sur AP2 et le framework Verifiable Intent). Communiqué (avril 2026). fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/.
- Gaire, Shiva ; Gyawali, Srijan ; Mishra, Saroj ; et al. (2025). *Systematization of Knowledge : Security and Safety in the Model Context Protocol Ecosystem*. arXiv:2512.08290.
- Guo, Yongjian ; Liu, Puzhuo ; Ma, Wanlun ; et al. (2025). *MCPXKIT : The Unified Toolkit for Analyzing Model Context Protocol Security*. arXiv:2508.12538 (accepté IEEE TDSC).
- IETF (Kasselman, P., Defakto Security ; Lombardo, J., AWS ; Rosomakho, Y., Zscaler ; Campbell, B., Ping Identity ; Steele, N., OpenAI ; Parecki, A., Okta) (2026). *AI Agent Authentication and Authorization*. IETF Internet-Draft individuel, draft-klrc-aiagent-auth-02 (1ᵉʳ juin 2026). datatracker.ietf.org/doc/draft-klrc-aiagent-auth/. ⚠
- IETF WIMSE Working Group (Salowey, J. ; Rosomakho, Y. ; Tschofenig, H., Eds.) (2026). *Workload Identity in a Multi System Environment (WIMSE) Architecture*. IETF Internet-Draft, draft-ietf-wimse-arch-07 (2 mars 2026). ⚠
- JFrog Security Research / NVD-MITRE (2025). *CVE-2025-6514 — mcp-remote OS command injection* (RCE client, CVSS 9.6 ; corrigé en 0.1.16). GHSA-6xpm-ggf7-wc3p (9 juil. 2025).
- Meunier, T. (Cloudflare) ; Major, S. (Google) (2026). *HTTP Message Signatures for automated traffic Architecture (Web Bot Auth)*. IETF Internet-Draft individuel, draft-meunier-web-bot-auth-architecture-05 (2 mars 2026). ⚠
- Oligo Security / NVD-MITRE (2025). *CVE-2025-49596 — MCP Inspector : absence d'authentification client-proxy* (RCE, CVSS 9.4 ; corrigé v0.14.1 le 13 juin 2025).
- OpenID Foundation (2025). *Artificial Intelligence Identity Management (AIIM) Community Group*. openid.net/cg/artificial-intelligence-identity-management-community-group/. [Le whitepaper AIIM *Identity Management for Agentic AI* (arXiv:2510.25819) est listé sous South et al. (2025), cat. 2, pour éviter le doublon.] ⚠
- OWASP GenAI Security Project (2024). *OWASP Top 10 for Large Language Model Applications 2025* (v2.0, LLM01:2025-LLM10:2025). Publié 18 nov. 2024. genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/. *(contexte non cité)*
- OWASP GenAI Security Project — Agentic Security Initiative (2025). *OWASP Top 10 for Agentic Applications for 2026* (ASI01-ASI10 ; dont ASI07 Insecure Inter-Agent Communication, ASI08 Cascading Failures). Annoncé 9 déc. 2025. genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/.
- OWASP GenAI Security Project — Agentic Security Initiative (2025). *Agentic AI — Threats and Mitigations (v1.0)* (guide threat-model). genai.owasp.org. *(contexte non cité)*
- OWASP MCP Top 10 Project (lead : Vandana Verma Sehgal) (2025). *OWASP MCP Top 10* (MCP01-MCP10 ; statut beta). owasp.org/www-project-mcp-top-10/. ⚠
- OX Security (2026). *Divulgation — comportement stdio par défaut de serveurs MCP* (≈ 200 000 instances estimées exposées ; qualification « défaut de conception » contestée, Anthropic la tenant pour un comportement intentionnel documenté). OX Security ; relais VentureBeat (avril 2026). ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/. ⚠
- SPIFFE project (CNCF) (2025). *SPIFFE specification & SPIRE runtime* (identité de charge via SVID X.509/JWT ; projet gradué). spiffe.io. ⚠
- Trulioo (et PayOS) (2025). *Know Your Agent (KYA) : An Identity Framework for Trusted Agentic Commerce + Digital Agent Passport (DAP)*. Trulioo (livre blanc d'industrie). trulioo.com/resources/white-papers/know-your-agent-an-identity-framework-for-trusted-agentic-commerce. ⚠
- W3C Agent Identity Registry Protocol Community Group (2026). *Call for Participation / charte* (CG proposée 2026-04-22, appel à participation 2026-04-24 ; attestations vérifiables liant l'agent à son organisation). w3.org/community/agent-identity/. ⚠
- Wang, Bin ; Liu, Zexin ; Yu, Hao ; et al. (2025). *MCPGuard : Automatically Detecting Vulnerabilities in MCP Servers*. arXiv:2510.23673.
- Wang, Zhiqiang ; Gao, Yichao ; Wang, Yanting ; et al. (2025). *MCPTox : A Benchmark for Tool Poisoning Attack on Real-World MCP Servers* (45 serveurs, 353 outils, 1312 cas). arXiv:2508.14925.

## 5. Réglementation

- Parlement européen et Conseil de l'UE (2024). *Règlement (UE) 2024/1689 établissant des règles harmonisées concernant l'intelligence artificielle (AI Act)*. JO de l'UE (13 juin 2024 ; entrée en vigueur 1er août 2024 ; application échelonnée jusqu'au 2 août 2027). ELI : data.europa.eu/eli/reg/2024/1689/oj.

## 6. Ressources praticiennes (blogs d'ingénierie, fondations, registres, frameworks)

- AGNTCY / Outshift by Cisco (Linux Foundation) (2025). *Agent Directory Service (ADS) — documentation et spécification, sur OASF* (annuaire distribué capability-centric ; content-addressed, registre OCI/ORAS, signature Sigstore). docs.agntcy.org/oasf/. ⚠
- Anthropic (2024). *Introducing the Model Context Protocol*. anthropic.com/news/model-context-protocol (25 nov. 2024).
- Anthropic (Applied AI / Engineering) (2025). *Code execution with MCP : Building more efficient agents*. anthropic.com/engineering/code-execution-with-mcp (4 nov. 2025). *(contexte non cité)*
- BerriAI (LiteLLM) (2026). *LiteLLM — SDK Python et Proxy/AI Gateway pour appeler 100+ API LLM au format OpenAI* (coût, garde-fous, répartition de charge). GitHub BerriAI/litellm ; docs.litellm.ai. ⚠
- Beurer-Kellner, Luca ; Fischer, Marc (Invariant Labs) (2025). *MCP Security Notification : Tool Poisoning Attacks*. invariantlabs.ai (1er avril 2025).
- Blair, Kate (IBM Research) / LF AI & Data (2025). *ACP Joins Forces with A2A Under the Linux Foundation's LF AI and Data*. Blog communautaire LF AI & Data (29 août 2025). lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/.
- Cloudflare ; Coinbase (2025). *Launching the x402 Foundation with Coinbase, and support for x402 transactions*. blog.cloudflare.com/x402/ (2025-09-23).
- Coinbase (2025). *Introducing x402 : a new standard for internet-native payments*. Coinbase Developer Platform Blog (mai 2025). coinbase.com/developer-platform/discover/launches/x402.
- Eclipse Foundation (Eclipse LMOS) (2025). *Eclipse LMOS Redefines Agentic AI with Industry's First Open Agent Definition Language (ADL) for Enterprises* (ADL model-neutral ; déploiement Deutsche Telekom). Eclipse Newsroom (28 oct. 2025). newsroom.eclipse.org/news/announcements/eclipse-lmos-redefines-agentic-ai-industry%E2%80%99s-first-open-agent-definition. ⚠
- GitHub (Padilla, Toby ; et al.) (2025). *Meet the GitHub MCP Registry*. The GitHub Blog (16 sept. 2025).
- Google Cloud (2025). *Announcing Agent Payments Protocol (AP2)*. cloud.google.com/blog (2025-09-16).
- Google (blog.google) / FIDO Alliance (2026). *Google donates Agent Payments Protocol to FIDO Alliance* (2026-04-28 ; v0.2, Human-Not-Present, standard Verifiable Intent co-développé avec Mastercard).
- Janix-ai (2025). *mcp-validator — Test suite for validating MCP server implementations* (supporte la révision 2025-06-18 ; STDIO et HTTP). GitHub Janix-ai/mcp-validator. ⚠
- Kong Inc. (2026). *Kong AI Gateway — plan de contrôle multi-fournisseurs* (AI Proxy / AI Proxy Advanced, API normalisée provider-agnostique). developer.konghq.com/ai-gateway/. ⚠
- Linux Foundation (2026). *A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year*. Communiqué (9 avril 2026). linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year.
- Linux Foundation / Agentic AI Foundation (2025). *Formation of the Agentic AI Foundation (AAIF) — donations MCP, goose, AGENTS.md*. Communiqué (9 déc. 2025).
- Mastercard (2025). *Mastercard Agent Pay et Mastercard Agentic Tokens* (extension de MDES liant credential tokenisé + scope marchand + consentement). Newsroom (2025-04-29). mastercard.com/global/en/news-and-trends/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai.html.
- Microsoft (2025). *Microsoft Agent Framework — convergence d'AutoGen et Semantic Kernel* (support natif MCP, A2A, OpenAPI ; aperçu oct. 2025 ; GA 1.0 le 3 avril 2026). devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/.
- Model Context Protocol Project / Anthropic (Soria Parra, D. ; Jones, A. ; Antanavicius, T. ; Padilla, T. ; Chu, T.) (2025). *Introducing the MCP Registry* (preview 2025-09-08). blog.modelcontextprotocol.io.
- Model Context Protocol Project (2025). *modelcontextprotocol/registry — dépôt de référence du registre MCP officiel* (API gelée v0.1, oct. 2025). GitHub. ⚠
- OpenAI (2025). *Buy it in ChatGPT : Instant Checkout and the Agentic Commerce Protocol* (lancement + open-sourcing de l'ACP, 2025-09-29). openai.com/index/buy-it-in-chatgpt/.
- OpenRouter (2026). *OpenRouter — interface unifiée compatible OpenAI vers de nombreux modèles* (routage, fallback, facturation unifiée). openrouter.ai/docs. ⚠
- Portkey AI (2026). *Portkey AI Gateway — passerelle unifiée vers de nombreux LLM* (garde-fous, observabilité, gestion de prompts ; drop-in SDK OpenAI). GitHub Portkey-AI/gateway. ⚠
- Responsible AI Collaborative — AI Incident Database (2025). *Incident 1152 : LLM-Driven Replit Agent Reportedly Executed Unauthorized Destructive Commands During Code Freeze, Leading to Loss of Production Data* (18 juillet 2025). incidentdatabase.ai/cite/1152/.
- Skan AI (2026). *Agentic Ontology of Work (AOW), Version 1.0* (Agents, Skills, Intents, Contexts, Policies, Memory, Confidence, Outcomes). Whitepaper (lancement 10 fév. 2026). skan.ai/whitepapers/agentic-ontology-of-work. ⚠
- Snowflake et partenaires — Open Semantic Interchange (OSI) (2026). *Open Semantic Interchange (OSI) — spécification v1.0* (modèle sémantique standardisé, couche analytics/BI/AI ; Apache 2.0). open-semantic-interchange.org (annonce 23 sept. 2025 ; v1.0 le 27 janvier 2026). ⚠
- Soria Parra, David (MCP, lead core maintainer) (2025). *MCP joins the Agentic AI Foundation*. blog.modelcontextprotocol.io (9 déc. 2025).
- Stripe (2025). *Developing an open standard for agentic commerce* (co-annonce de l'ACP avec OpenAI ; Shared Payment Token, 2025-09-29). Stripe Newsroom. stripe.com/blog/developing-an-open-standard-for-agentic-commerce.
- Unit 42 (Palo Alto Networks) (2025). *New Prompt Injection Attack Vectors Through MCP Sampling*. unit42.paloaltonetworks.com.
- vLLM (2026). *vLLM — serveur d'inférence exposant un serveur compatible OpenAI (et Anthropic Messages API)*. docs.vllm.ai. ⚠
- W3C AI Agent Protocol Community Group (proposée par Gaowei Chang et al.) (2025). *AI Agent Protocol Community Group (mission et charte)* (proposée 8 mai 2025 ; 1re réunion 18 juin 2025). w3.org/community/agentprotocol/. ⚠
- W3C Autonomous Agents on the Web Community Group (proposée par Fabien Gandon) (2023). *Autonomous Agents on the Web (WebAgents) Community Group — Charter* (Hypermedia MAS / Linked Data). w3.org/community/webagents/. ⚠
- Willison, Simon (2025). *The lethal trifecta for AI agents : private data, untrusted content, and external communication*. simonwillison.net (16 juin 2025).

---

### Annexe — vérification et fusion

La passe de vérification adverse a **confirmé 170 références** et **corrigé 24** (aucune écartée comme non vérifiable). Corrections types : ordre/complétude des listes d'auteurs (Beyond Message Passing, MAST, ANS, AGNTCY ADS, MCP Registry), distinction des deux « ACP », gouvernance AP2 (FIDO, pas LF), DOI PVLDB non confirmé d'Agent-OM remplacé par arXiv. Doublons fusionnés notables : KQML (4×), Contract Net (3×), *Beyond Message Passing* (4×), specs FIPA décomposées par numéro, A2A v1.0 (2×), MCP Conformance (2×), whitepaper OpenID AIIM / South et al. (2×, même arXiv:2510.25819). Ajouts de veille juillet 2026 (non re-vérifiés en adverse, marqués ⚠) : CSA *MCP Security Crisis*, OX Security stdio, IETF draft-klrc-aiagent-auth-02.

*Le marqueur ⚠ est volontairement fréquent : sur ce sujet de frontière, la plupart des protocoles, registres et frameworks sont des ressources vivantes versionnées par date ou des drafts IETF/W3C — re-confirmer la version/le statut au moment de citer.*
