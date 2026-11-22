# Dossier fermé de sources L+ — Chapitre 08 — Sécurité par construction : pourquoi un modèle plus capable n'est pas plus sûr

- **Unité du livre** : `ch08` (`sources/ch08-sources.md`)
- **Axes de recherche couverts** : `RQ5`
- **Date de gel des faits** : 2 décembre 2026
- **Protocole** : `MLR-PRISMA-SCR-LIVRE-2027-V1.2` (`metadata_only_pct = 0.0 %`, règle stricte `AO-01` sans contournement)
- **Nombre de sources probantes incluses** : 13 sources intégrales `L+`

> Ce dossier fermé recense exclusivement les sources primaires et travaux ouverts dont le texte intégral UTF-8 a été extrait, conservé sous `recherche/corpus_l_plus/` et authentifié par empreinte `SHA-256`. Aucune source en `statut F` ni copie locale non ouverte n'entre dans l'argumentation probante.

Note AO-01 (statut F) : le portail principal `genai.owasp.org` (HTTP 403, `F#03`) et le portail `ieeexplore.ieee.org` (HTTP 202 WAF, `F#04`) restent exclus en `statut F` dans `recherche/registre-statut-f.json` ; le référentiel OWASP est documenté par la copie officielle complète CC BY-SA 4.0 v1.0 archivée dans le dépôt officiel `GenAI-Security-Corpus` (`SRC-055`).

---

### [1] SRC-007 — Defeating Prompt Injections by Design (CaMeL)

- **Auteurs / Émetteur** : Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes et al. (2025, 2025-06-24)
- **Revue / Organisme / Dépôt** : arXiv (prépublication) — Identifiant : `arXiv:2503.18813v2`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.18813
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-007.txt` (50342 mots, 361916 octets)
- **Empreinte SHA-256** : `7a9735abcbdcbea1569be50b290f7e8198648a57f378a27bdb796e0f38cb3d2b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (prépublication arXiv) | Score AACODS : `11.5/12` | Devis : Prépublication décrivant un système d'exécution sécurisé et évaluation sur banc AgentDojo | Axes : `RQ5`
- **Synthèse factuelle** : Debenedetti et al. présentent CaMeL, une couche système de sécurité inspirée des langages à capacités et du patron Dual-LLM qui isole par construction le graphe d'appels d'outils du traitement de données externes non fiables. Un modèle planificateur traduit la requête approuvée en un sous-ensemble restreint de Python dont l'arbre syntaxique est interprété sous politiques de flux de données et de capacités, tandis qu'un modèle confiné sans accès aux outils privilégiés résume les données brutes. Sur le banc AgentDojo, CaMeL résout 77 % des tâches avec une garantie structurelle contre l'injection de consignes indirecte, contre 84 % pour un agent sans défense. Cette source valide l'arbitrage sécurité-utilité et le principe de séparation contrôle-données en ingénierie.

### [2] SRC-038 — Model Context Protocol (MCP) Specification — Revision 2025-11-25 (corpus normatif complet)

- **Auteurs / Émetteur** : Model Context Protocol Maintainers (2025, 2025-11-25)
- **Revue / Organisme / Dépôt** : Model Context Protocol (GitHub modelcontextprotocol/modelcontextprotocol — spec 2025-11-25) — Identifiant : `MCP-SPEC-2025-11-25`
- **URL ouverte vérifiée** : https://github.com/modelcontextprotocol/modelcontextprotocol/tree/main/docs/specification/2025-11-25
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-038.txt` (62231 mots, 757889 octets)
- **Empreinte SHA-256** : `938fca60c06c92e10cd6448f31d90fbb81d03adcb1952a21915d219f685e96a9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Corpus normatif complet de spécification protocolaire ouverte (MCP 2025-11-25 : 22 chapitres et tutoriels sécurité/autorisation) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : Le corpus normatif intégral du Model Context Protocol (révision du 25 novembre 2025 : architecture, protocole de base, autorisation OAuth, transports, tâches, client/serveur/outils, schéma et bonnes pratiques de sécurité) définit un protocole JSON-RPC 2.0 inspiré du Language Server Protocol pour relier hôtes LLM, clients et serveurs d'outils. La spécification avertit que les outils constituent une exécution de code arbitraire, que leurs descriptions et annotations sont non fiables hors serveur de confiance et que les serveurs mandataires doivent prévenir le problème du « délégué confus » et le transfert direct de jetons (*token passthrough*).

### [3] SRC-039 — Agent2Agent (A2A) Protocol Specification

- **Auteurs / Émetteur** : Linux Foundation / A2A Project (2026, 2026-05-28)
- **Revue / Organisme / Dépôt** : a2a-protocol.org — Identifiant : `A2A-SPEC-2026`
- **URL ouverte vérifiée** : https://a2a-protocol.org/latest/specification/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-039.txt` (24333 mots, 179807 octets)
- **Empreinte SHA-256** : `fb9823ce13380143b0509c404cc5098c945ba2ec21f0dda779ddf90f4a351727`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Spécification ouverte d'interopérabilité inter-agents (Linux Foundation A2A, v1.0.1) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : La spécification Agent2Agent (A2A) propose une architecture à trois couches — modèle de données canonique, opérations abstraites et liaisons protocolaires JSON-RPC, gRPC et HTTP/REST — permettant à des agents opaques de domaines ou d'organisations distincts de se découvrir et de collaborer sur des tâches asynchrones de longue durée. Le protocole encadre la découverte par Agent Cards, les flux multi-tours, l'architecture d'extensions typées et la sécurité multi-locataires. A2A représente dans l'ouvrage le protocole horizontal complémentaire de MCP pour les échanges inter-entreprises.

### [4] SRC-042 — RFC 9396: OAuth 2.0 Rich Authorization Requests (RAR)

- **Auteurs / Émetteur** : Torsten Lodderstedt, Justin Richer, Brian Campbell (2023, 2023-05)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9396`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9396.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-042.txt` (7380 mots, 55352 octets)
- **Empreinte SHA-256** : `e334d06f14081317caf9d457dcbffeae877c5e5009f2452d2f11adcd47d68f6b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9396, évalué par les pairs) | Axes : `RQ4`
- **Synthèse factuelle** : La RFC 9396 introduit le paramètre JSON « authorization_details » dans les requêtes et réponses de jetons OAuth 2.0 afin de décrire des autorisations granulaires fortement typées (montants plafonnés, comptes bénéficiaires, actions précises) là où les simples chaînes « scope » restent trop grossières. Elle précise la validation sémantique entre client, serveur d'autorisation et serveur de ressources ainsi que l'usage de schémas lisibles par machine. Appliqué aux agents financiers, RAR contraint cryptographiquement chaque appel d'outil au mandat exact approuvé par le client ou la politique.

### [5] SRC-043 — RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)

- **Auteurs / Émetteur** : Daniel Fett, Brian Campbell, John Bradley, Torsten Lodderstedt et al. (2023, 2023-09)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9449`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9449.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-043.txt` (12014 mots, 83632 octets)
- **Empreinte SHA-256** : `5e0267f9b8801cc882ec1dcb1d1d220cbe8cb38bbe428362cd1c8a2b33ef30e0`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9449, évalué par les pairs) | Axes : `RQ4`
- **Synthèse factuelle** : La RFC 9449 définit OAuth 2.0 Demonstrating Proof of Possession (DPoP), un mécanisme applicatif permettant de lier cryptographiquement un jeton d'accès ou d'actualisation à une paire de clés asymétriques détenue par le client grâce à un en-tête JWT signé et une confirmation par empreinte JWK (« cnf/jkt »). Contrairement aux jetons porteurs classiques, un jeton lié par DPoP volé dans une mémoire tampon ou un journal est inutilisable sans la clé privée associée, avec possibilité de nonce anti-rejeu. Ce standard sécurise les échanges entre passerelles, agents et serveurs de ressources face aux risques d'exfiltration.

### [6] SRC-044 — RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT)

- **Auteurs / Émetteur** : Henk Birkholz, Antoine Delignat-Lavaud, Cedric Fournet, Yogesh Deshpande, Steve Lasker (2026, 2026-06)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9943`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9943.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-044.txt` (9449 mots, 65473 octets)
- **Empreinte SHA-256** : `1ed0ffb4007b7986d5d3ff4da1a0489d5b9d71c5eae4cd89a7f48ae650a19fef`
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

- **Auteurs / Émetteur** : Alina Oprea, Apostol Vassilev et al. (NIST) (2025, 2025-03-20)
- **Revue / Organisme / Dépôt** : NIST — Identifiant : `NIST-AI-100-2E2025`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-054.txt` (48743 mots, 347771 octets)
- **Empreinte SHA-256** : `1f113bf38b90261c6372c5b9a8d77a4355c7e4fa0ccf11b4d179930a9a0dfa7f`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Taxonomie normative officielle (NIST AI 100-2e2025) | Axes : `RQ5`
- **Synthèse factuelle** : Ce rapport du NIST établit une taxonomie et une terminologie de référence en apprentissage automatique antagoniste (Adversarial Machine Learning) couvrant aussi bien l'IA prédictive que l'IA générative. Il classe systématiquement les attaques selon le stade du cycle de vie, les objectifs (compromission d'intégrité, disponibilité, vie privée), les capacités et la connaissance de l'attaquant, puis associe les mesures d'atténuation disponibles et leurs limites persistantes. Ce cadre permet aux chapitres 5, 8 et 9 de distinguer empoisonnement, évasion et détournement de contexte.

### [9] SRC-055 — OWASP Top 10 for Agentic Applications 2026 (v1.0, December 2025 — document complet CC BY-SA 4.0)

- **Auteurs / Émetteur** : OWASP GenAI Security Project (2025, 2025-12)
- **Revue / Organisme / Dépôt** : OWASP GenAI Security Project (Agentic Security Initiative — GenAI-Security-Corpus) — Identifiant : `OWASP-AGENTIC-TOP10-2026`
- **URL ouverte vérifiée** : https://raw.githubusercontent.com/genai-security-project/GenAI-Security-Corpus/main/corpus/agentic-top10/2026-final/OWASP-Top-10-for-Agentic-Applications-2026-v1.0.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-055.txt` (13820 mots, 100680 octets)
- **Empreinte SHA-256** : `4d9f1c9f067fc284f01e8a904b172bbaceb97dd5a259a4d73c7d80f1482c22f3`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Référentiel industriel ouvert complet de risques (OWASP Top 10 for Agentic Applications 2026 v1.0, déc. 2025) | Axes : `RQ5`
- **Synthèse factuelle** : Document complet officiel CC BY-SA 4.0 (56 pages, décembre 2025) de l'initiative *Agentic Security* d'OWASP, couvrant les dix risques critiques `ASI01` à `ASI10` (détournement d'objectif, mésusage d'outils, abus d'identité, chaîne d'approvisionnement, exécution de code inattendue, empoisonnement de mémoire, communication inter-agents, défaillances en cascade, exploitation de la confiance humain-agent et agents dévoyés), complété par la matrice de correspondance réglementaire/normative (Annexe A) et le registre d'incidents documentés en production dont les attaques MCP de 2025 (Annexe D).

### [10] SRC-056 — Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks

- **Auteurs / Émetteur** : James Peters-Gill, Avi Semler, Henning Bartsch, Ilia Shumailov et al. (2026, 2026-10-05)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2610.05640`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2610.05640
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-056.txt` (14394 mots, 97586 octets)
- **Empreinte SHA-256** : `490ff7dc6d6914d59acfb56fab33ebb48ae61dd5ef1bfd181cb69d04c68ee9f5`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Évaluation cryptographique/sécuritaire multi-agents (Oxford / MATS, arXiv 2026) | Axes : `RQ5`
- **Synthèse factuelle** : Peters-Gill, Semler, Bartsch, Shumailov et Schroeder de Witt testent la composabilité des garanties de sécurité de CaMeL lorsque plusieurs agents équipés chacun de CaMeL s'invoquent mutuellement comme outils dans une architecture hiérarchique. Leurs résultats montrent de manière critique que les garanties de CaMeL ne se composent pas automatiquement d'un agent à l'autre : une attaque concrète par injection indirecte réussit en exploitant la réinterprétation de données non fiables transitant entre sous-agents privilégiés et planificateurs. Cette limite démontre l'importance de la « règle du maillon le plus élevé » et du confinement aux frontières inter-agents.

### [11] SRC-057 — Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem

- **Auteurs / Émetteur** : Obada Kraishan (2026, 2026-09-15)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2609.14119`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2609.14119
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-057.txt` (7412 mots, 49308 octets)
- **Empreinte SHA-256** : `cae21acac54fea61a6270540a888a090731fac9d0de3ae0f121f3d51d59ed7e9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Recensement empirique de sécurité sur registre public (21 643 serveurs MCP, 2026) | Axes : `RQ5`
- **Synthèse factuelle** : Kraishan réalise en août–septembre 2026 le premier recensement complet du registre public MCP en collectant 21 643 serveurs (72 606 versions) et en analysant le code source de 14 353 d'entre eux à l'aide d'un analyseur à huit classes de menaces calibré sur 414 cas vérifiés manuellement. L'étude observe une prévalence élevée d'exposition réseau sans authentification (9,57 % des serveurs analysés) ainsi que des phénomènes de « dérive silencieuse » où un même nom de serveur change discrètement de comportement ou d'implémentation. Ce constat empirique justifie les sas d'assainissement et le registre d'outils signé SCITT aux chapitres 4, 8 et 9.

### [12] SRC-058 — STAMP/STPA Informed Characterization of Factors Leading to Loss of Control in AI Systems

- **Auteurs / Émetteur** : Steve Barrett, Anna Bruvere, Sean P. Fillingham, Catherine Rhodes, Stefano Vergani (2026, 2026-02-03)
- **Revue / Organisme / Dépôt** : arXiv (Centre for the Study of Existential Risk) — Identifiant : `arXiv:2512.17600v2`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.17600
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-058.txt` (17212 mots, 112088 octets)
- **Empreinte SHA-256** : `78b03417f4de11b0132a9afce95e493bec8b9028715ec9b9139aa504d4599ecb`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Cadre d'analyse de sûreté système (Barrett et al., STAMP/STPA, v2 fév. 2026) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Barrett, Bruvere, Fillingham, Rhodes et Vergani (Arcadia Impact / CSER / King's College London) appliquent la méthodologie d'ingénierie de la sûreté STAMP/STPA pour caractériser systématiquement les facteurs causaux menant à une perte de contrôle dans les systèmes sociotechniques intégrant l'IA. Plutôt que de traiter uniquement les défaillances isolées de composants, l'approche modélise les boucles de contrôle, les actions de contrôle dangereuses et les défauts de rétroaction entre concepteurs, opérateurs humains et composants autonomes. Elle fonde en L+ les analyses de boucles de contrainte et de gouvernance opérationnelle des chapitres 8, 9, 11 et 12.

### [13] SRC-066 — Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security and Operational Risk

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2026, 2026-07-13)
- **Revue / Organisme / Dépôt** : OSFI Technology Risk Bulletin — Identifiant : `OSFI-BULLETIN-AGENTIC-2026`
- **URL ouverte vérifiée** : http://www.osfi-bsif.gc.ca/en/risks/technology-cyber-risk-management/technology-risk-bulletin/generative-agentic-artificial-intelligence-implications-technology-cyber-security-operational
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-066.txt` (1971 mots, 14425 octets)
- **Empreinte SHA-256** : `5a1b1a2e004b17fdfdbef1e2da35981654e689878fe0727cf26d9aba27e00f2b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Bulletin officiel de risque technologique et cyber (OSFI/BSIF, juillet 2026) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Publié en juillet 2026, ce bulletin du BSIF analyse spécifiquement les risques technologiques, cybernétiques et opérationnels introduits par l'IA générative et l'IA agentique (définie par le raisonnement et l'exécution autonomes) dans les institutions financières fédérales. Le régulateur avertit que ces technologies élargissent les surfaces d'attaque, accélèrent la propagation des défaillances et mettent à l'épreuve les contrôles existants sous les lignes directrices B-13, B-10 et E-21. Il recommande une gouvernance renforcée de l'autonomie, une journalisation et surveillance accrues ainsi que des plans de continuité adaptés aux collectifs d'agents.
