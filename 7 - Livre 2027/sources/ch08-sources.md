# Dossier fermé de sources L+ — Chapitre 08 — Sécurité par construction : pourquoi un modèle plus capable n'est pas plus sûr

- **Unité du livre** : `ch08` (`sources/ch08-sources.md`)
- **Axes de recherche couverts** : `RQ5`
- **Date de gel des faits** : 31 décembre 2026
- **Protocole** : `MLR-PRISMA-SCR-LIVRE-2027-V1.2` (`metadata_only_pct = 0.0 %`, règle stricte `AO-01` sans contournement)
- **Nombre de sources probantes incluses** : 13 sources intégrales `L+`

> Ce dossier fermé recense exclusivement les sources primaires et travaux ouverts dont le texte intégral UTF-8 a été extrait, conservé sous `recherche/corpus_l_plus/` et authentifié par empreinte `SHA-256`. Aucune source en `statut F` ni copie locale non ouverte n'entre dans l'argumentation probante.

Note AO-01 (statut F) : le portail PDF principal genai.owasp.org (HTTP 403) et le portail IEEE Xplore (HTTP 202 WAF) sont exclus en statut F dans `recherche/registre-statut-f.json`; seul le crosswalk ouvert vérifié (`SRC-055`) fait foi.

---

### [1] SRC-007 — Defeating Prompt Injections by Design (CaMeL)

- **Auteurs / Émetteur** : Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes et al. (2025, 2025-03-24)
- **Revue / Organisme / Dépôt** : arXiv / IEEE SaTML — Identifiant : `arXiv:2503.18813`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.18813
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-007.txt` (50342 mots, 361916 octets)
- **Empreinte SHA-256** : `49dbe34fe4cd657f9d22e5dfc3a6088dbce5935172937af6374bafdbf2bc188b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Système d'exécution sécurisé et évaluation sur banc AgentDojo (peer-reviewed) | Axes : `RQ5`
- **Synthèse factuelle** : Debenedetti et al. présentent CaMeL, une couche système de sécurité inspirée des langages à capacités et du patron Dual-LLM qui isole par construction le graphe d'appels d'outils du traitement de données externes non fiables. Un modèle planificateur traduit la requête approuvée en un sous-ensemble restreint de Python dont l'arbre syntaxique est interprété sous politiques de flux de données et de capacités, tandis qu'un modèle confiné sans accès aux outils privilégies résume les données brutes. Sur le banc AgentDojo, CaMeL résout 77 % des tâches avec une garantie structurelle contre l'injection de prompt indirecte, contre 84 % pour un agent sans défense. Cette source valide l'arbitrage sécurité-utilité et le principe de séparation contrôle-données en ingénierie.

### [2] SRC-038 — Model Context Protocol (MCP) Specification — Revision 2025-11-25

- **Auteurs / Émetteur** : Model Context Protocol Maintainers (2025, 2025-11-25)
- **Revue / Organisme / Dépôt** : modelcontextprotocol.io — Identifiant : `MCP-SPEC-2025-11-25`
- **URL ouverte vérifiée** : https://modelcontextprotocol.io/specification/2025-11-25
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-038.txt` (658 mots, 4720 octets)
- **Empreinte SHA-256** : `4c51bbc2f467fee7c2e5a4a61a05dac44533734db74af5244320f32be7ec46da`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Spécification protocolaire ouverte de connectivité (MCP 2025-11-25) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : La spécification du Model Context Protocol (révision du 25 novembre 2025) définit un protocole standardisé fondé sur JSON-RPC 2.0 inspiré du Language Server Protocol pour relier des applications hôtes LLM, des clients connecteurs et des serveurs exposant outils, ressources et gabarits. Le texte encadre le cycle de vie des sessions, les mécanismes de consentement utilisateur et les considérations de sûreté liées à l'exposition d'outils locaux ou distants. Dans l'ouvrage, MCP incarne l'axe vertical d'interopérabilité agent-outil tout en exigeant des contrôles supplémentaires d'authentification et de sémantique métier.

### [3] SRC-039 — Agent2Agent (A2A) Protocol Specification

- **Auteurs / Émetteur** : Linux Foundation / A2A Project (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : a2a-protocol.org — Identifiant : `A2A-SPEC-2026`
- **URL ouverte vérifiée** : https://a2a-protocol.org/latest/specification/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-039.txt` (24333 mots, 179807 octets)
- **Empreinte SHA-256** : `fb9823ce13380143b0509c404cc5098c945ba2ec21f0dda779ddf90f4a351727`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Spécification ouverte d'interopérabilité inter-agents (Linux Foundation A2A) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : La spécification Agent2Agent (A2A) propose une architecture à trois couches — modèle de données canonique, opérations abstraites et liaisons protocolaires JSON-RPC, gRPC et HTTP/REST — permettant à des agents opaques de domaines ou d'organisations distincts de se découvrir et de collaborer sur des tâches asynchrones de longue durée. Le protocole encadre la découverte par Agent Cards, les flux multi-tours, l'architecture d'extensions typées et la sécurité multi-locataires. A2A représente dans l'ouvrage le protocole horizontal complémentaire de MCP pour les échanges inter-entreprises.

### [4] SRC-042 — RFC 9396: OAuth 2.0 Rich Authorization Requests (RAR)

- **Auteurs / Émetteur** : Torsten Lodderstedt, Justin Richer, Brian Campbell (2023, 2023-05-01)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9396`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9396.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-042.txt` (7381 mots, 55355 octets)
- **Empreinte SHA-256** : `4dd9cae1706ae4f417e220c8f702b70e7cdc646aa4ea74c63ef224337a508ce0`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9396, évalué par les pairs) | Axes : `RQ4`
- **Synthèse factuelle** : La RFC 9396 introduit le paramètre JSON « authorization_details » dans les requêtes et réponses de jetons OAuth 2.0 afin de décrire des autorisations granulaires fortement typées (montants plafonnés, comptes bénéficiaires, actions précises) là où les simples chaînes « scope » restent trop grossières. Elle précise la validation sémantique entre client, serveur d'autorisation et serveur de ressources ainsi que l'usage de schémas lisibles par machine. Appliqué aux agents financiers, RAR contraint cryptographiquement chaque appel d'outil au mandat exact approuvé par le client ou la politique.

### [5] SRC-043 — RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)

- **Auteurs / Émetteur** : Daniel Fett, Brian Campbell, John Bradley, Torsten Lodderstedt et al. (2023, 2023-09-01)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9449`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9449.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-043.txt` (12015 mots, 83635 octets)
- **Empreinte SHA-256** : `a2292338693a203b2b769edea593c8fc55e39a391c0f9c82f3093d9bed35667d`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9449, évalué par les pairs) | Axes : `RQ4`
- **Synthèse factuelle** : La RFC 9449 définit OAuth 2.0 Demonstrating Proof of Possession (DPoP), un mécanisme applicatif permettant de lier cryptographiquement un jeton d'accès ou d'actualisation à une paire de clés asymétriques détenue par le client grâce à un en-tête JWT signé et une confirmation par empreinte JWK (« cnf/jkt »). Contrairement aux jetons porteurs classiques, un jeton lié par DPoP volé dans une mémoire tampon ou un journal est inutilisable sans la clé privée associée, avec possibilité de nonce anti-rejeu. Ce standard sécurise les échanges entre passerelles, agents et serveurs de ressources face aux risques d'exfiltration.

### [6] SRC-044 — RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT)

- **Auteurs / Émetteur** : Henk Birkholz, Antoine Delignat-Lavaud, Cedric Fournet, Yogesh Deshpande, Steve Lasker (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9943`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9943.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-044.txt` (9450 mots, 65476 octets)
- **Empreinte SHA-256** : `3ae677b4a295a3ee3eb793d39daf3d2a1139b041ff019fc5317bfe24a3fa3ae6`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9943, juin 2026) | Axes : `RQ4, RQ5`
- **Synthèse factuelle** : La RFC 9943 normalise l'architecture SCITT (Supply Chain Integrity, Transparency, and Trust) pour l'enregistrement et l'audit d'énoncés signés par un émetteur unique dans des journaux transparents fondés sur des structures de données vérifiables (arbres de Merkle anti-équivocation). Elle permet à toute partie vérifiante d'obtenir la preuve cryptographique qu'un manifeste logiciel, une attestation de modèle ou un serveur d'outils a bien été enregistré et validé à un instant donné. SCITT offre une réponse normalisée aux attaques sur la chaîne d'approvisionnement d'outils agentiques et aux exigences de traçabilité d'audit.

### [7] SRC-048 — AI Identity Management System (draft-ietf-wimse-aims-01)

- **Auteurs / Émetteur** : IETF WIMSE Working Group (2026, 2026-11-02)
- **Revue / Organisme / Dépôt** : IETF Datatracker — Identifiant : `IETF-WIMSE-AIMS-01`
- **URL ouverte vérifiée** : https://www.ietf.org/archive/id/draft-ietf-wimse-aims-01.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-048.txt` (10027 mots, 69988 octets)
- **Empreinte SHA-256** : `ab53c74913dd1337f6183a03825d985dc1f39bc613721a54e9a3d3092231045e`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Brouillon normatif IETF spécifique aux agents IA (WIMSE AIMS-01, nov. 2026) | Axes : `RQ4`
- **Synthèse factuelle** : Le document AI Identity Management System (draft-ietf-wimse-aims-01, novembre 2026) rédigé par des auteurs de Defakto, AWS, Zscaler, Ping Identity, OpenAI et Okta applique l'architecture WIMSE et OAuth 2.0 à l'authentification et à l'autorisation des agents IA. Partant du principe que les agents sont des charges de travail exécutées dans des environnements complexes, il spécifie l'identification des agents, le cycle de provisionnement des justificatifs et les limites de l'authentification uniquement transport par rapport aux preuves applicatives. Cette source récente démontre la convergence de la normalisation industrielle fin 2026.

### [8] SRC-054 — NIST AI 100-2e2025: Adversarial Machine Learning — A Taxonomy and Terminology of Attacks and Mitigations

- **Auteurs / Émetteur** : Alina Oprea, Apostol Vassilev et al. (NIST) (2025, 2025-03-01)
- **Revue / Organisme / Dépôt** : NIST — Identifiant : `NIST-AI-100-2E2025`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-054.txt` (48743 mots, 347771 octets)
- **Empreinte SHA-256** : `1f113bf38b90261c6372c5b9a8d77a4355c7e4fa0ccf11b4d179930a9a0dfa7f`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Taxonomie normative officielle (NIST AI 100-2e2025) | Axes : `RQ5`
- **Synthèse factuelle** : Ce rapport du NIST établit une taxonomie et une terminologie de référence en apprentissage automatique antagoniste (Adversarial Machine Learning) couvrant aussi bien l'IA prédictive que l'IA générative. Il classe systématiquement les attaques selon le stade du cycle de vie, les objectifs (compromission d'intégrité, disponibilité, vie privée), les capacités et la connaissance de l'attaquant, puis associe les mesures d'atténuation disponibles et leurs limites persistantes. Ce cadre permet aux chapitres 5, 8 et 9 de distinguer empoisonnement, évasion et détournement de contexte.

### [9] SRC-055 — OWASP Top 10 for Agentic Applications (2026) — Threat Crosswalk

- **Auteurs / Émetteur** : OWASP GenAI Security Project (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : OWASP GenAI Security Project (GitHub Open Pages) — Identifiant : `OWASP-AGENTIC-TOP10-2026`
- **URL ouverte vérifiée** : https://genai-security-project.github.io/crosswalk/agentic-ai-top10/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-055.txt` (506 mots, 3616 octets)
- **Empreinte SHA-256** : `e5a50552cb527f49da00bcd4ea206348db3331b41c6f4fa2dd7e7dc5904cf17d`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Référentiel industriel ouvert de risques (OWASP Agentic AI Top 10 Crosswalk 2026) | Axes : `RQ5`
- **Synthèse factuelle** : Alors que le portail PDF principal genai.owasp.org bloque l'accès automatisé (HTTP 403, statut F), le Crosswalk officiel hébergé en accès ouvert sur github.io répertorie l'ensemble des 10 catégories de risques critiques de l'OWASP Top 10 pour applications agentiques 2026 (ASI01 à ASI10, incluant le détournement d'objectif par injection indirecte). Chaque catégorie est notée par criticité, ventilée en mesures de base, de durcissement et avancées, et mise en correspondance contrôle par contrôle avec 26 référentiels dont NIST AI RMF, ISO/IEC 42001, MITRE ATLAS et l'EU AI Act.

### [10] SRC-056 — Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks

- **Auteurs / Émetteur** : James Peters-Gill, Avi Semler, Henning Bartsch, Ilia Shumailov et al. (2026, 2026-10-05)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2610.05640`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2610.05640
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-056.txt` (14394 mots, 97586 octets)
- **Empreinte SHA-256** : `490ff7dc6d6914d59acfb56fab33ebb48ae61dd5ef1bfd181cb69d04c68ee9f5`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Évaluation cryptographique/sécuritaire multi-agents (Oxford / MATS, arXiv 2026) | Axes : `RQ5`
- **Synthèse factuelle** : Peters-Gill, Semler, Bartsch, Shumailov et Schroeder de Witt testent la composabilité des garanties de sécurité de CaMeL lorsque plusieurs agents équipés chacun de CaMeL s'invoquent mutuellement comme outils dans une architecture hiérarchique. Leurs résultats montrent de manière critique que les garanties de CaMeL ne se composent pas automatiquement d'un agent à l'autre : une attaque concrète par injection indirecte réussit en exploitant la réinterprétation de données non fiables transitant entre sous-agents privilégiés et planificateurs. Cette limite démontre l'importance de la « règle du maillon le plus élevé » et du confinement aux frontières inter-agents.

### [11] SRC-057 — Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem

- **Auteurs / Émetteur** : Obada Kraishan (2026, 2026-09-12)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2609.14119`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2609.14119
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-057.txt` (7412 mots, 49308 octets)
- **Empreinte SHA-256** : `cae21acac54fea61a6270540a888a090731fac9d0de3ae0f121f3d51d59ed7e9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Recensement empirique de sécurité sur registre public (21 643 serveurs MCP, 2026) | Axes : `RQ5`
- **Synthèse factuelle** : Kraishan réalise en août–septembre 2026 le premier recensement complet du registre public MCP en collectant 21 643 serveurs (72 606 versions) et en analysant le code source de 14 353 d'entre eux à l'aide d'un analyseur à huit classes de menaces calibré sur 414 cas vérifiés manuellement. L'étude observe une prévalence élevée d'exposition réseau sans authentification (9,57 % des serveurs analysés) ainsi que des phénomènes de « dérive silencieuse » où un même nom de serveur change discrètement de comportement ou d'implémentation. Ce constat empirique justifie les sas d'assainissement et le registre d'outils signé SCITT aux chapitres 4, 8 et 9.

### [12] SRC-058 — STAMP/STPA Informed Characterization of Factors Leading to Loss of Control in AI Systems

- **Auteurs / Émetteur** : Steve Barrett, Anna Bruvere, Sean P. Fillingham, Catherine Rhodes (2025, 2025-12-19)
- **Revue / Organisme / Dépôt** : arXiv (Centre for the Study of Existential Risk) — Identifiant : `arXiv:2512.17600`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.17600
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-058.txt` (17212 mots, 112088 octets)
- **Empreinte SHA-256** : `78b03417f4de11b0132a9afce95e493bec8b9028715ec9b9139aa504d4599ecb`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Cadre d'analyse de sûreté système (Barrett et al., STAMP/STPA, déc. 2025) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Barrett, Bruvere, Fillingham, Rhodes et Vergani (Arcadia Impact / CSER / King's College London) appliquent la méthodologie d'ingénierie de la sûreté STAMP/STPA pour caractériser systématiquement les facteurs causaux menant à une perte de contrôle dans les systèmes sociotechniques intégrant l'IA. Plutôt que de traiter uniquement les défaillances isolées de composants, l'approche modélise les boucles de contrôle, les actions de contrôle dangereuses et les défauts de rétroaction entre concepteurs, opérateurs humains et composants autonomes. Elle fonde en L+ les analyses de boucles de contrainte et de gouvernance opérationnelle des chapitres 8, 9, 11 et 12.

### [13] SRC-066 — Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security and Operational Risk

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2026, 2026-07-01)
- **Revue / Organisme / Dépôt** : OSFI Technology Risk Bulletin — Identifiant : `OSFI-BULLETIN-AGENTIC-2026`
- **URL ouverte vérifiée** : http://www.osfi-bsif.gc.ca/en/risks/technology-cyber-risk-management/technology-risk-bulletin/generative-agentic-artificial-intelligence-implications-technology-cyber-security-operational
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-066.txt` (4194 mots, 49330 octets)
- **Empreinte SHA-256** : `362c9639e348264a5fb303562725378b726185cd4d26914724182736c0c07d69`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Bulletin officiel de risque technologique et cyber (OSFI/BSIF, juillet 2026) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Publié en juillet 2026, ce bulletin du BSIF analyse spécifiquement les risques technologiques, cybernétiques et opérationnels introduits par l'IA générative et l'IA agentique (définie par le raisonnement et l'exécution autonomes) dans les institutions financières fédérales. Le régulateur avertit que ces technologies élargissent les surfaces d'attaque, accélèrent la propagation des défaillances et mettent à l'épreuve les contrôles existants sous les lignes directrices B-13, B-10 et E-21. Il recommande une gouvernance renforcée de l'autonomie, une journalisation et surveillance accrues ainsi que des plans de continuité adaptés aux collectifs d'agents.
