# Dossier fermé de sources L+ — Chapitre 09 — Observer, prouver et compter au coût complet du résultat conforme

- **Unité du livre** : `ch09` (`sources/ch09-sources.md`)
- **Axes de recherche couverts** : `RQ3, RQ5`
- **Date de gel des faits** : 2 décembre 2026
- **Protocole** : `MLR-PRISMA-SCR-LIVRE-2027-V1.2` (`metadata_only_pct = 0.0 %`, règle stricte `AO-01` sans contournement)
- **Nombre de sources probantes incluses** : 22 sources intégrales `L+`

> Ce dossier fermé recense exclusivement les sources primaires et travaux ouverts dont le texte intégral UTF-8 a été extrait, conservé sous `recherche/corpus_l_plus/` et authentifié par empreinte `SHA-256`. Aucune source en `statut F` ni copie locale non ouverte n'entre dans l'argumentation probante.

Note AO-01 (statut F) : le manuel STPA MIT hébergé sur scripts.mit.edu (erreur TLS/réseau) est exclu en statut F dans `recherche/registre-statut-f.json` ; la méthode STPA/STAMP est documentée en L+ via Barrett et al. (`SRC-058`).

---

### [1] SRC-007 — Defeating Prompt Injections by Design (CaMeL)

- **Auteurs / Émetteur** : Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes et al. (2025, 2025-06-24)
- **Revue / Organisme / Dépôt** : arXiv (prépublication) — Identifiant : `arXiv:2503.18813v2`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.18813
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-007.txt` (50342 mots, 361916 octets)
- **Empreinte SHA-256** : `7a9735abcbdcbea1569be50b290f7e8198648a57f378a27bdb796e0f38cb3d2b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Système d'exécution sécurisé et évaluation sur banc AgentDojo (`arXiv:2503.18813v2`) | Axes : `RQ5`
- **Synthèse factuelle** : Debenedetti et al. présentent CaMeL, une couche système de sécurité inspirée des langages à capacités et du patron Dual-LLM qui isole par construction le graphe d'appels d'outils du traitement de données externes non fiables. Un modèle planificateur traduit la requête approuvée en un sous-ensemble restreint de Python dont l'arbre syntaxique est interprété sous politiques de flux de données et de capacités, tandis qu'un modèle confiné sans accès aux outils privilégiés résume les données brutes. Sur le banc AgentDojo, CaMeL résout 77 % des tâches avec une garantie structurelle contre l'injection de prompt indirecte, contre 84 % pour un agent sans défense. Cette source valide l'arbitrage sécurité-utilité et le principe de séparation contrôle-données en ingénierie.

### [2] SRC-023 — FinOps Open Cost and Usage Specification (FOCUS) v1.4 — Spécification normative complète

- **Auteurs / Émetteur** : FinOps Foundation (2026, 2026-06-04)
- **Revue / Organisme / Dépôt** : Linux Foundation / FinOps Foundation (GitHub release v1.4) — Identifiant : `FINOPS-FOCUS-1.4`
- **URL ouverte vérifiée** : https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/releases/download/v1.4/FOCUS_spec-v1_4.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-023.txt` (92764 mots, 698569 octets)
- **Empreinte SHA-256** : `67f651d7a5b0bd9103b5cffaa3617edaec6fb7f1aa9ebd2b7d3f122a422a5f5e`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Spécification ouverte de normalisation comptable cloud (FinOps FOCUS v1.4) | Axes : `RQ1, RQ3`
- **Synthèse factuelle** : La spécification FinOps Open Cost and Usage Specification (FOCUS v1.4, Linux Foundation) normalise le schéma des données de facturation et d'utilisation des ressources infonuagiques entre fournisseurs. Elle définit des colonnes et conventions terminologiques unifiées permettant aux équipes d'ingénierie et de finance d'exécuter de manière homogène la rétrofacturation interne (chargeback), l'imputation des coûts par produit ou agent, la budgétisation et la prévision. Dans l'ouvrage, FOCUS sert de standard pivot pour relier la consommation de jetons et de calcul au coût complet par résultat conforme (CPO).

### [3] SRC-028 — Why Do Multi-Agent LLM Systems Fail? (MAST)

- **Auteurs / Émetteur** : Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal et al. (2025, 2025-10-26)
- **Revue / Organisme / Dépôt** : NeurIPS 2025 / arXiv — Identifiant : `arXiv:2503.13657v3`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.13657
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-028.txt` (19765 mots, 136729 octets)
- **Empreinte SHA-256** : `7eeb1c6dfd098f1f6507ab979bdae4a7a2eacc1888efc0d599aca663f6577933`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Taxonomie empirique et jeu de données annoté (NeurIPS 2025 / MAST-Data) | Axes : `RQ2`
- **Synthèse factuelle** : Cemri et al. analysent plus de 1 600 traces (1 642 traces dans MAST-Data) issues de sept cadriciels multi-agents open source populaires (dont AutoGen, CrewAI, ChatDev, MetaGPT et Manus) et construisent la taxonomie MAST à 14 modes de défaillance regroupés en 3 catégories : conception système, désalignement inter-agents et vérification/terminaison. Les taux d'échec observés sur les systèmes évalués varient de 41 % à 86,7 %, mettant en évidence que la plupart des défaillances proviennent de la coordination, de l'oubli de spécifications ou d'absences de garde-fous de vérification plutôt que des capacités intrinsèques du LLM. Ces mesures fondent l'exigence de tests structurels et de contrôle déterministe.

### [4] SRC-035 — CloudEvents Specification — Version 1.0.2

- **Auteurs / Émetteur** : CNCF Serverless Working Group (2022, 2022-04)
- **Revue / Organisme / Dépôt** : Cloud Native Computing Foundation (CNCF) — Identifiant : `CLOUDEVENTS-1.0.2`
- **URL ouverte vérifiée** : https://raw.githubusercontent.com/cloudevents/spec/v1.0.2/cloudevents/spec.md
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-035.txt` (3651 mots, 25147 octets)
- **Empreinte SHA-256** : `8f4d59dd27f8807741321b3145c5c9c2f22bba5bf9a9299b0c2020d769dc92ae`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Spécification ouverte CNCF de format d'événement (CloudEvents v1.0.2) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : Publiée par le groupe Serverless de la Cloud Native Computing Foundation, la spécification CloudEvents v1.0.2 standardise une enveloppe neutre de métadonnées contextuelles (identifiant id, source, type, specversion, datacontenttype, heure) pour décrire les événements traversant des routeurs, bus de messages et systèmes de traçage hétérogènes. Cette séparation nette entre attributs de contexte routables par les intermédiaires et charge utile métier facilite la mise en place de files d'attente, de journaux de reprise et de politiques de sécurité indépendantes du protocole de transport. Elle appuie l'orchestration événementielle et les canaux de compensation dédiés aux chapitres 3 et 4.

### [5] SRC-037 — OpenTelemetry Semantic Conventions for Generative AI Agent & Execute Tool Spans (gen_ai.operation.name)

- **Auteurs / Émetteur** : OpenTelemetry GenAI SIG (2026, 2026-11-05)
- **Revue / Organisme / Dépôt** : CNCF / OpenTelemetry Semantic Conventions (GenAI SIG — agent-spans, execute-tool & registry.yaml) — Identifiant : `OTEL-GENAI-AGENT-TOOL-SPANS`
- **URL ouverte vérifiée** : https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-agent-spans.md
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-037.txt` (13159 mots, 125111 octets)
- **Empreinte SHA-256** : `1b2526202e8aef9b15819b89cd1c34eefd8d10be3dac7b05f714597c34d5549c`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Conventions sémantiques d'observabilité ouverte (OpenTelemetry GenAI Agent & Execute Tool Spans) | Axes : `RQ3, RQ6`
- **Synthèse factuelle** : Cette spécification du groupe d'intérêt spécial GenAI d'OpenTelemetry normalise les attributs, événements et métriques des traces distribuées (« spans ») pour la création d'agents (`create_agent`), leur invocation client ou interne (`invoke_agent`) et l'exécution d'outils (`execute_tool`, définie dans `execute-tool.md` et `registry.yaml`). Elle précise les champs obligatoires et conditionnels couvrant l'identifiant stable de l'agent (`gen_ai.agent.id`), l'appel d'outil (`gen_ai.tool.name`, `gen_ai.tool.call.id`), la version, le modèle et les captures optionnelles (« Opt-In ») des instructions et paramètres sans exposer par défaut les données sensibles. Ces conventions soutiennent directement l'instrumentation télémétrique à double couloir des chapitres 4, 6 et 9.

### [6] SRC-044 — RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT)

- **Auteurs / Émetteur** : Henk Birkholz, Antoine Delignat-Lavaud, Cedric Fournet, Yogesh Deshpande, Steve Lasker (2026, 2026-06)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9943`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9943.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-044.txt` (9449 mots, 65473 octets)
- **Empreinte SHA-256** : `1ed0ffb4007b7986d5d3ff4da1a0489d5b9d71c5eae4cd89a7f48ae650a19fef`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9943, juin 2026) | Axes : `RQ4, RQ5`
- **Synthèse factuelle** : La RFC 9943 normalise l'architecture SCITT (Supply Chain Integrity, Transparency, and Trust) pour l'enregistrement et l'audit d'énoncés signés par un émetteur unique dans des journaux transparents fondés sur des structures de données vérifiables (arbres de Merkle anti-équivocation). Elle permet à toute partie vérifiante d'obtenir la preuve cryptographique qu'un manifeste logiciel, une attestation de modèle ou un serveur d'outils a bien été enregistré et validé à un instant donné. SCITT offre une réponse normalisée aux attaques sur la chaîne d'approvisionnement d'outils agentiques et aux exigences de traçabilité d'audit.

### [7] SRC-054 — NIST AI 100-2e2025: Adversarial Machine Learning — A Taxonomy and Terminology of Attacks and Mitigations

- **Auteurs / Émetteur** : Alina Oprea, Apostol Vassilev et al. (NIST) (2025, 2025-03-20)
- **Revue / Organisme / Dépôt** : NIST — Identifiant : `NIST-AI-100-2E2025`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-054.txt` (48743 mots, 347771 octets)
- **Empreinte SHA-256** : `1f113bf38b90261c6372c5b9a8d77a4355c7e4fa0ccf11b4d179930a9a0dfa7f`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Taxonomie normative officielle (NIST AI 100-2e2025) | Axes : `RQ5`
- **Synthèse factuelle** : Ce rapport du NIST établit une taxonomie et une terminologie de référence en apprentissage automatique antagoniste (Adversarial Machine Learning) couvrant aussi bien l'IA prédictive que l'IA générative. Il classe systématiquement les attaques selon le stade du cycle de vie, les objectifs (compromission d'intégrité, disponibilité, vie privée), les capacités et la connaissance de l'attaquant, puis associe les mesures d'atténuation disponibles et leurs limites persistantes. Ce cadre permet aux chapitres 5, 8 et 9 de distinguer empoisonnement, évasion et détournement de contexte.

### [8] SRC-057 — Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem

- **Auteurs / Émetteur** : Obada Kraishan (2026, 2026-09-15)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2609.14119`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2609.14119
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-057.txt` (7412 mots, 49308 octets)
- **Empreinte SHA-256** : `cae21acac54fea61a6270540a888a090731fac9d0de3ae0f121f3d51d59ed7e9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Recensement empirique de sécurité sur registre public (21 643 serveurs MCP, 2026) | Axes : `RQ5`
- **Synthèse factuelle** : Kraishan réalise en août–septembre 2026 le premier recensement complet du registre public MCP en collectant 21 643 serveurs (72 606 versions) et en analysant le code source de 14 353 d'entre eux à l'aide d'un analyseur à huit classes de menaces calibré sur 414 cas vérifiés manuellement. L'étude observe une prévalence élevée d'exposition réseau sans authentification (9,57 % des serveurs analysés) ainsi que des phénomènes de « dérive silencieuse » où un même nom de serveur change discrètement de comportement ou d'implémentation. Ce constat empirique justifie les sas d'assainissement et le registre d'outils signé SCITT aux chapitres 4, 8 et 9.

### [9] SRC-058 — STAMP/STPA Informed Characterization of Factors Leading to Loss of Control in AI Systems

- **Auteurs / Émetteur** : Steve Barrett, Anna Bruvere, Sean P. Fillingham, Catherine Rhodes, Stefano Vergani (2026, 2026-02-03)
- **Revue / Organisme / Dépôt** : arXiv (Centre for the Study of Existential Risk) — Identifiant : `arXiv:2512.17600v2`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.17600
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-058.txt` (17212 mots, 112088 octets)
- **Empreinte SHA-256** : `78b03417f4de11b0132a9afce95e493bec8b9028715ec9b9139aa504d4599ecb`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Cadre d'analyse de sûreté système (Barrett et al., STAMP/STPA, v2 fév. 2026) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Barrett, Bruvere, Fillingham, Rhodes et Vergani (Arcadia Impact / CSER / King's College London) appliquent la méthodologie d'ingénierie de la sûreté STAMP/STPA pour caractériser systématiquement les facteurs causaux menant à une perte de contrôle dans les systèmes sociotechniques intégrant l'IA. Plutôt que de traiter uniquement les défaillances isolées de composants, l'approche modélise les boucles de contrôle, les actions de contrôle dangereuses et les défauts de rétroaction entre concepteurs, opérateurs humains et composants autonomes. Elle fonde en L+ les analyses de boucles de contrainte et de gouvernance opérationnelle des chapitres 8, 9, 11 et 12.

### [10] SRC-059 — System level governance of generative AI risks in cross border e-commerce supply chains

- **Auteurs / Émetteur** : Ionel Bostan (2026, 2026-08-27)
- **Revue / Organisme / Dépôt** : Discover Computing (Springer OA) — Identifiant : `DOI:10.1007/s10791-026-10509-y`
- **URL ouverte vérifiée** : https://link.springer.com/article/10.1007/s10791-026-10509-y
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-059.txt` (10451 mots, 81859 octets)
- **Empreinte SHA-256** : `ccfeca2f7bdcb50bee94cc157151c33f01246c54aaae878846a63ea2b864dd5c`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `10.5/12` | Devis : Article de recherche évalué par les pairs (Discover Computing, Springer OA 2026) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Publié en août 2026 dans Discover Computing, cet article d'Ionel Bostan conceptualise le « risque systémique » (system-level risk) engendré par le déploiement d'IA générative à travers des pipelines de données, architectures de modèles et chaînes d'approvisionnement numériques transfrontalières. Il montre que les risques éthiques, réglementaires et de durabilité se propagent au-delà de l'algorithme individuel le long des dépendances organisationnelles et juridictionnelles des plateformes. L'article étaye la gouvernance multi-couches et le contrôle des chaînes de sous-traitance aux chapitres 9 et 10.

### [11] SRC-060 — Règlement (UE) 2024/1689 (EU AI Act)

- **Auteurs / Émetteur** : Parlement européen et Conseil de l'Union européenne (2024, 2024-07-12)
- **Revue / Organisme / Dépôt** : Journal officiel de l'Union européenne — Identifiant : `CELEX:32024R1689`
- **URL ouverte vérifiée** : https://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0009.01/DOC_1
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-060.txt` (102754 mots, 711317 octets)
- **Empreinte SHA-256** : `e0a79e4f278c88177206c60458fad1f06c74fc80d6b23e404ef523c290346477`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Acte législatif européen officiel (Règlement UE 2024/1689, JOUE) | Axes : `RQ6`
- **Synthèse factuelle** : Le texte intégral français officiel du Règlement (UE) 2024/1689 (EU AI Act, adopté le 13 juin 2024 et publié le 12 juillet 2024) fixe le cadre harmonisé par niveaux de risque dans l'Union européenne. L'article 113 prévoit une application échelonnée incluant les pratiques interdites (février 2025), les obligations de transparence de l'article 50 et la date générale d'application du 2 août 2026, ainsi que les régimes des systèmes à haut risque des annexes III et I. Il sert de texte juridique socle avant prise en compte des ajustements calendaires adoptés en juillet 2026.

### [12] SRC-062 — Règlement (UE) 2022/2554 sur la résilience opérationnelle numérique du secteur financier (DORA)

- **Auteurs / Émetteur** : Parlement européen et Conseil de l'Union européenne (2022, 2022-12-27)
- **Revue / Organisme / Dépôt** : Journal officiel de l'Union européenne — Identifiant : `CELEX:32022R2554`
- **URL ouverte vérifiée** : https://publications.europa.eu/resource/cellar/0caf473a-85bd-11ed-9887-01aa75ed71a1.0009.01/DOC_1
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-062.txt` (52268 mots, 364364 octets)
- **Empreinte SHA-256** : `6e4b138de7f05c440c3b1c3b590545dc0cd3f1c793e4c12c733f8736a2ecfb9e`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Acte législatif européen officiel financier (Règlement UE 2022/2554 DORA, JOUE) | Axes : `RQ6`
- **Synthèse factuelle** : Le Règlement (UE) 2022/2554 sur la résilience opérationnelle numérique du secteur financier (DORA) impose aux entités financières européennes des exigences contraignantes de gestion du risque lié aux TIC, de déclaration des incidents majeurs, de tests de résilience avancés et d'encadrement strict des prestataires tiers critiques de services TIC. Il oblige notamment l'organe de direction à superviser l'exposition contractuelle aux fournisseurs cloud et d'IA externes et à maintenir les compétences nécessaires pour évaluer ces risques. Dans l'ouvrage, DORA offre le parallèle européen direct aux attentes prudentielles du BSIF.

### [13] SRC-065 — Ligne directrice E-23 — Gestion du risque de modélisation à l'échelle de l'entreprise (édition 2027)

- **Auteurs / Émetteur** : Bureau du surintendant des institutions financières (BSIF / OSFI) (2025, 2025-09-11)
- **Revue / Organisme / Dépôt** : BSIF Canada — Identifiant : `BSIF-E23-2027`
- **URL ouverte vérifiée** : https://www.osfi-bsif.gc.ca/fr/consignes/repertoire-consignes/ligne-directrice-e-23-gestion-du-risque-modelisation-2027
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-065.txt` (6372 mots, 44778 octets)
- **Empreinte SHA-256** : `60ef80b531aaa0ac26d2180a14bd1c295297dabe7ddf8c4260f37c90b2ecda3e`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Ligne directrice prudentielle fédérale officielle (BSIF E-23, édition 2027) | Axes : `RQ6`
- **Synthèse factuelle** : La ligne directrice E-23 révisée du Bureau du surintendant des institutions financières sur la gestion du risque de modélisation à l'échelle de l'entreprise affiche explicitement une date d'entrée en vigueur fixée « Le 1 mai 2027 ». Elle étend formellement le champ du risque de modélisation au-delà des modèles statistiques classiques pour englober les modèles d'intelligence artificielle et d'apprentissage automatique à travers tout leur cycle de vie (inventaire, validation indépendante, surveillance continue et gouvernance des compétences). Elle constitue l'ancre prudentielle canadienne structurante de la troisième et quatrième partie.

### [14] SRC-066 — Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security and Operational Risk

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2026, 2026-07-13)
- **Revue / Organisme / Dépôt** : OSFI Technology Risk Bulletin — Identifiant : `OSFI-BULLETIN-AGENTIC-2026`
- **URL ouverte vérifiée** : http://www.osfi-bsif.gc.ca/en/risks/technology-cyber-risk-management/technology-risk-bulletin/generative-agentic-artificial-intelligence-implications-technology-cyber-security-operational
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-066.txt` (1971 mots, 14425 octets)
- **Empreinte SHA-256** : `5a1b1a2e004b17fdfdbef1e2da35981654e689878fe0727cf26d9aba27e00f2b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Bulletin officiel de risque technologique et cyber (OSFI/BSIF, juillet 2026) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Publié en juillet 2026, ce bulletin du BSIF analyse spécifiquement les risques technologiques, cybernétiques et opérationnels introduits par l'IA générative et l'IA agentique (définie par le raisonnement et l'exécution autonomes) dans les institutions financières fédérales. Le régulateur avertit que ces technologies élargissent les surfaces d'attaque, accélèrent la propagation des défaillances et mettent à l'épreuve les contrôles existants sous les lignes directrices B-13, B-10 et E-21. Il recommande une gouvernance renforcée de l'autonomie, une journalisation et surveillance accrues ainsi que des plans de continuité adaptés aux collectifs d'agents.

### [15] SRC-067 — Guideline B-15: Climate Risk Management

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2025, 2025-03-07)
- **Revue / Organisme / Dépôt** : OSFI Canada — Identifiant : `OSFI-B15`
- **URL ouverte vérifiée** : https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/climate-risk-management
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-067.txt` (6901 mots, 48790 octets)
- **Empreinte SHA-256** : `8136e1e002181ca17e41c4492105da441a3b316d8fccb6289665c35ed11d8946`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Ligne directrice prudentielle climatique officielle (OSFI/BSIF B-15) | Axes : `RQ6`
- **Synthèse factuelle** : La ligne directrice B-15 du BSIF fixe les attentes de divulgation financière liée au climat pour les institutions financières fédérales en s'appuyant sur le GHG Protocol et la norme PCAF pour la comptabilisation des émissions financées et assurées. Dans le tableau récapitulatif de l'annexe 2-2 (élément b) ii), la date d'exercice financier attendue pour la divulgation des émissions absolues brutes de portée 3 — incluant obligatoirement la catégorie 15 des prêts, investissements et portefeuilles d'assurance — est arrêtée à 2028 (tandis que le volet b) iii visant les actifs sous gestion demeure marqué TBD). Ce texte officialise le jalon de fin 2028 exploité aux chapitres 9 et 12.

### [16] SRC-068 — Guideline B-10: Third-Party Risk Management

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2023, 2023-04-30)
- **Revue / Organisme / Dépôt** : OSFI Canada — Identifiant : `OSFI-B10`
- **URL ouverte vérifiée** : https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/third-party-risk-management-guideline
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-068.txt` (7859 mots, 55115 octets)
- **Empreinte SHA-256** : `db7ccc401ea3b392f22b42c75b63d657eb95cd1c6ab5ccf2d55551bf9be01625`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Ligne directrice prudentielle officielle sur les tiers (OSFI/BSIF B-10) | Axes : `RQ6`
- **Synthèse factuelle** : La ligne directrice B-10 du BSIF encadre la gestion des risques liés aux accords avec des tiers pour toutes les banques, sociétés d'assurances et succursales étrangères sous réglementation fédérale canadienne. Elle exige une diligence raisonnable continue, l'évaluation du risque de concentration, la maîtrise des chaînes de sous-traitance de niveau n (« fourth parties ») et des plans de sortie et de réversibilité robustes pour les services technologiques critiques. Elle appuie l'exigence de substituabilité des modèles et d'encadrement des serveurs d'outils externes dans l'ouvrage.

### [17] SRC-075 — Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents

- **Auteurs / Émetteur** : Shipi Dhanorkar, Samir Passi, Mihaela Vorvoreanu (2026, 2026-06-03)
- **Revue / Organisme / Dépôt** : arXiv (Microsoft Research) — Identifiant : `arXiv:2606.05391`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2606.05391
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-075.txt` (17178 mots, 122290 octets)
- **Empreinte SHA-256** : `a0b7c487a5e089136bbd97d1f4d9dc54ce8376634f6f270ea425689f31dd179c`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Étude empirique qualitative auprès de développeurs (Microsoft Research, arXiv 2026) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Dhanorkar, Passi et Vorvoreanu observent directement comment des développeurs exercent concrètement la supervision humaine d'agents logiciels autonomes au quotidien, depuis la co-planification jusqu'à l'inspection des résultats. L'étude documente les dilemmes de granularité des instructions — où les agents prennent des décisions fragiles faute d'exigences implicites de sécurité ou de maintenabilité — ainsi que les heuristiques improvisées de vérification face à la fatigue cognitive. Elle ancre empiriquement les exigences concrètes d'ergonomie cognitive et de « révision humaine effective » aux chapitres 9, 11 et 12.

### [18] SRC-027 — Measuring Agents in Production (MAP)

- **Auteurs / Émetteur** : Melissa Z. Pan, Negar Arabzadeh, Riccardo Cogo, Yuxuan Zhu et al. (2025, 2025-12-02)
- **Revue / Organisme / Dépôt** : arXiv (UC Berkeley) — Identifiant : `arXiv:2512.04123`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.04123
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-027.txt` (22684 mots, 160353 octets)
- **Empreinte SHA-256** : `3f8f34adaeb523b3cdc740f8df9d4c97b621f9ac7f955c10d94e3fbc97dcc2e1`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Étude mixte terrain (20 études de cas et enquête sur 306 répondants / 86 systèmes) | Axes : `RQ2, RQ6`
- **Synthèse factuelle** : L'étude Measuring Agents in Production (MAP) de Pan et al. documente comment les praticiens conçoivent réellement les agents en exploitation à travers 20 entrevues approfondies et 306 réponses d'enquête couvrant 26 domaines (86 praticiens en production). Contre le mythe de l'autonomie ouverte, 68 % des systèmes déployés exécutent au plus 10 étapes avant intervention humaine, 80 % des études de cas (16 sur 20) utilisent des flux de travail structurés fixes, 70 % conservent des modèles commerciaux sans réentraînement des poids et 79 % rédigent les invites manuellement. Les organisations sacrifient délibérément l'autonomie ouverte au profit de la prévisibilité et de la maîtrise du risque.

### [19] SRC-029 — τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

- **Auteurs / Émetteur** : Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan (2024, 2024-06-17)
- **Revue / Organisme / Dépôt** : arXiv (Princeton) — Identifiant : `arXiv:2406.12045`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2406.12045
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-029.txt` (17795 mots, 130060 octets)
- **Empreinte SHA-256** : `659469b4a86d64eab21b613c1754164de732af170d5954a26ac7a69d06cab7d9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Banc d'essai conversationnel à état de base de données (arXiv Princeton / Sierra) | Axes : `RQ2`
- **Synthèse factuelle** : Yao, Shinn, Razavi et Narasimhan conçoivent τ-bench pour évaluer des agents confrontés simultanément à des usagers simulés, à des outils d'API réels et à des politiques métier strictes (secteurs aérien et commerce de détail), en comparant l'état final exact de la base de données avec l'état cible. Ils introduisent la métrique pass^k, mesurant la probabilité qu'un agent réussisse sans défaillance les k répétitions d'une même tâche, révélant qu'un agent appelant des outils à 50 % sur un essai chute rapidement sous pass^8. L'article démontre que les scores moyens à essai unique surestiment gravement l'aptitude à la production.

### [20] SRC-030 — Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation (HAL)

- **Auteurs / Émetteur** : Sayash Kapoor, Benedikt Stroebl, Peter Kirgis, Nitya Nadgir et al. (2025, 2025-10-13)
- **Revue / Organisme / Dépôt** : arXiv (Princeton) — Identifiant : `arXiv:2510.11977`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2510.11977
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-030.txt` (25986 mots, 173603 octets)
- **Empreinte SHA-256** : `4f1e326b6b314f5856566ce21a588bd934508fc767159859376315a94fcb2dfd`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Infrastructure normalisée d'évaluation et méta-analyse (21 730 exécutions, Princeton) | Axes : `RQ2`
- **Synthèse factuelle** : Kapoor et al. mettent au point le Holistic Agent Leaderboard (HAL), un harnais d'évaluation standardisé exécuté sur machines virtuelles isolées qui orchestre 21 730 exécutions à travers 9 modèles et 9 bancs d'essai afin d'éliminer les biais d'implémentation des harnais ad hoc. Leur analyse tridimensionnelle (modèle × harnais × banc) révèle que le coût en jetons varie d'un ordre de grandeur entre architectures pour des gains parfois marginaux et recense des défaillances silencieuses de contournement ou de devinette face aux blocages d'outils. HAL fournit la justification méthodologique de la chaîne d'ingénierie et d'évaluation sur les protocoles d'évaluation Pareto coût-constance.

### [21] SRC-063 — Loi modernisant des dispositions législatives en matière de protection des renseignements personnels (Loi 25 / LQ 2021, c. 25, art. 12.1)

- **Auteurs / Émetteur** : Assemblée nationale du Québec (2021, 2021-09-22)
- **Revue / Organisme / Dépôt** : Publications du Québec — Identifiant : `LQ-2021-C25`
- **URL ouverte vérifiée** : https://www.publicationsduquebec.gouv.qc.ca/fileadmin/Fichiers_client/lois_et_reglements/LoisAnnuelles/fr/2021/2021C25F.PDF
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-063.txt` (21658 mots, 143588 octets)
- **Empreinte SHA-256** : `829e67f777ca0645b5b51a2ec4d8ec94739232c5a33ef76b7944d2bb81b61d87`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Texte législatif officiel sanctionné du Québec (Loi 25 / LQ 2021, c. 25) | Axes : `RQ6`
- **Synthèse factuelle** : La Loi modernisant des dispositions législatives en matière de protection des renseignements personnels (LQ 2021, c. 25, sanctionnée le 22 septembre 2021) insère l'article 12.1 dans la Loi sur le privé encadrant toute décision rendue fondée exclusivement sur un traitement automatisé (information de la personne concernée, communication sur demande des renseignements, facteurs et paramètres utilisés, correction et droit de présenter ses observations devant un membre du personnel). Elle instaure des sanctions administratives pécuniaires pouvant atteindre 10 000 000 \$ CA ou 2 % du chiffre d'affaires mondial (art. 90.12) et des amendes pénales allant jusqu'à 25 000 000 \$ CA ou 4 % du chiffre d'affaires mondial (art. 91). Ce texte sanctionné fournit la preuve L+ face au blocage HTTP 403 de LégisQuébec (statut F).

### [22] SRC-077 — RFC 8785: JSON Canonicalization Scheme (JCS)

- **Auteurs / Émetteur** : Anders Rundgren, Bret Jordan, Samuel Erdtman (2020, 2020-06)
- **Revue / Organisme / Dépôt** : IETF RFC Editor (Independent Submission) — Identifiant : `RFC8785`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc8785.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-077.txt` (5011 mots, 36840 octets)
- **Empreinte SHA-256** : `be00e8aeddaf91fcf40b1c5ecaa33f2d627dac1e3c338e80a1eb0445e31af642`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.0/12` | Devis : Spécification IETF (JSON Canonicalization Scheme, RFC 8785) | Axes : `RQ3, RQ4, RQ5`
- **Synthèse factuelle** : La RFC 8785 définit le schéma de canonisation JSON (JSON Canonicalization Scheme, JCS) permettant de produire une représentation binaire UTF-8 déterministe de toute structure JSON afin d'en calculer le condensat ou la signature cryptographique directement sur le document lisible sans encodage Base64 intermédiaire. Elle impose la sérialisation déterministe des nombres selon ECMAScript, la suppression des espaces superflus et le tri lexicographique récursif des noms de propriétés par unités de code UTF-16. Dans les chapitres 7 à 9, JCS fonde l'empreinte canonique des événements de preuve et des journaux scellés d'audit.
