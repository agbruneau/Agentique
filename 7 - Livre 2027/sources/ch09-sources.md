# Dossier fermé de sources L+ — Chapitre 09 — Observer, prouver et compter au coût complet du résultat conforme

- **Unité du livre** : `ch09` (`sources/ch09-sources.md`)
- **Axes de recherche couverts** : `RQ3, RQ5`
- **Date de gel des faits** : 31 décembre 2026
- **Protocole** : `MLR-PRISMA-SCR-LIVRE-2027-V1.2` (`metadata_only_pct = 0.0 %`, règle stricte `AO-01` sans contournement)
- **Nombre de sources probantes incluses** : 17 sources intégrales `L+`

> Ce dossier fermé recense exclusivement les sources primaires et travaux ouverts dont le texte intégral UTF-8 a été extrait, conservé sous `recherche/corpus_l_plus/` et authentifié par empreinte `SHA-256`. Aucune source en `statut F` ni copie locale non ouverte n'entre dans l'argumentation probante.

Note AO-01 (statut F) : le manuel STPA MIT hébergé sur scripts.mit.edu (erreur TLS/réseau) est exclu en statut F dans `recherche/registre-statut-f.json`; la méthode STPA/STAMP est documentée en L+ via Barrett et al. (`SRC-058`).

---

### [1] SRC-007 — Defeating Prompt Injections by Design (CaMeL)

- **Auteurs / Émetteur** : Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes et al. (2025, 2025-03-24)
- **Revue / Organisme / Dépôt** : arXiv / IEEE SaTML — Identifiant : `arXiv:2503.18813`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.18813
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-007.txt` (50342 mots, 361916 octets)
- **Empreinte SHA-256** : `49dbe34fe4cd657f9d22e5dfc3a6088dbce5935172937af6374bafdbf2bc188b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Système d'exécution sécurisé et évaluation sur banc AgentDojo (peer-reviewed) | Axes : `RQ5`
- **Synthèse factuelle** : Debenedetti et al. présentent CaMeL, une couche système de sécurité inspirée des langages à capacités et du patron Dual-LLM qui isole par construction le graphe d'appels d'outils du traitement de données externes non fiables. Un modèle planificateur traduit la requête approuvée en un sous-ensemble restreint de Python dont l'arbre syntaxique est interprété sous politiques de flux de données et de capacités, tandis qu'un modèle confiné sans accès aux outils privilégies résume les données brutes. Sur le banc AgentDojo, CaMeL résout 77 % des tâches avec une garantie structurelle contre l'injection de prompt indirecte, contre 84 % pour un agent sans défense. Cette source valide l'arbitrage sécurité-utilité et le principe de séparation contrôle-données en ingénierie.

### [2] SRC-023 — FinOps Open Cost and Usage Specification (FOCUS) v1.4

- **Auteurs / Émetteur** : FinOps Foundation (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : Linux Foundation / FinOps Foundation — Identifiant : `FINOPS-FOCUS-1.4`
- **URL ouverte vérifiée** : https://focus.finops.org/focus-specification/v1-4/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-023.txt` (408 mots, 2805 octets)
- **Empreinte SHA-256** : `e6f6f27c0a5402244bc16e3e0bedfe7fad2c0556f915584599670289526e8fea`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Spécification ouverte de normalisation comptable cloud (FinOps FOCUS v1.4) | Axes : `RQ1, RQ3`
- **Synthèse factuelle** : La spécification FinOps Open Cost and Usage Specification (FOCUS v1.4, Linux Foundation) normalise le schéma des données de facturation et d'utilisation des ressources infonuagiques entre fournisseurs. Elle définit des colonnes et conventions terminologiques unifiées permettant aux équipes d'ingénierie et de finance d'exécuter de manière homogène la rétrofacturation interne (chargeback), l'imputation des coûts par produit ou agent, la budgétisation et la prévision. Dans l'ouvrage, FOCUS sert de standard pivot pour relier la consommation de jetons et de calcul au coût complet par résultat conforme (CPO).

### [3] SRC-028 — Why Do Multi-Agent LLM Systems Fail? (MAST)

- **Auteurs / Émetteur** : Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal et al. (2025, 2025-03-17)
- **Revue / Organisme / Dépôt** : NeurIPS 2025 / arXiv — Identifiant : `arXiv:2503.13657`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.13657
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-028.txt` (19765 mots, 136729 octets)
- **Empreinte SHA-256** : `7eeb1c6dfd098f1f6507ab979bdae4a7a2eacc1888efc0d599aca663f6577933`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Taxonomie empirique et jeu de données annoté (NeurIPS 2025 / MAST-Data) | Axes : `RQ2`
- **Synthèse factuelle** : Cemri et al. analysent plus de 1 600 traces (1 642 traces dans MAST-Data) issues de sept cadriciels multi-agents open source populaires (dont AutoGen, CrewAI, ChatDev, MetaGPT et Manus) et construisent la taxonomie MAST à 14 modes de défaillance regroupés en 3 catégories : conception système, désalignement inter-agents et vérification/terminaison. Les taux d'échec observés sur les systèmes évalués varient de 41 % à 86,7 %, mettant en évidence que la plupart des défaillances proviennent de la coordination, de l'oubli de spécifications ou d'absences de garde-fous de vérification plutôt que des capacités intrinsèques du LLM. Ces mesures fondent l'exigence de tests structurels et de contrôle déterministe.

### [4] SRC-035 — CloudEvents Specification — Version 1.0.2

- **Auteurs / Émetteur** : CNCF Serverless Working Group (2022, 2022-04-01)
- **Revue / Organisme / Dépôt** : Cloud Native Computing Foundation (CNCF) — Identifiant : `CLOUDEVENTS-1.0.2`
- **URL ouverte vérifiée** : https://raw.githubusercontent.com/cloudevents/spec/v1.0.2/cloudevents/spec.md
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-035.txt` (3651 mots, 25147 octets)
- **Empreinte SHA-256** : `8f4d59dd27f8807741321b3145c5c9c2f22bba5bf9a9299b0c2020d769dc92ae`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Spécification ouverte CNCF de format d'événement (CloudEvents v1.0.2) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : Publiée par le groupe Serverless de la Cloud Native Computing Foundation, la spécification CloudEvents v1.0.2 standardise une enveloppe neutre de métadonnées contextuelles (identifiant id, source, type, specversion, datacontenttype, heure) pour décrire les événements traversant des routeurs, bus de messages et systèmes de traçage hétérogènes. Cette séparation nette entre attributs de contexte routables par les intermédiaires et charge utile métier facilite la mise en place de files d'attente, de journaux de reprise et de politiques de sécurité indépendantes du protocole de transport. Elle appuie l'orchestration événementielle et les canaux de compensation dédiés aux chapitres 3 et 4.

### [5] SRC-037 — OpenTelemetry Semantic Conventions for Generative AI Agents (gen-ai-agent-spans)

- **Auteurs / Émetteur** : OpenTelemetry GenAI SIG (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : CNCF / OpenTelemetry — Identifiant : `OTEL-GENAI-AGENT-SPANS`
- **URL ouverte vérifiée** : https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-agent-spans.md
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-037.txt` (5295 mots, 51753 octets)
- **Empreinte SHA-256** : `0816fd88102bcd7382db933bf8606ebb5fd6e1d9a513685489e1b0ee7b9e58c1`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Conventions sémantiques d'observabilité ouverte (OpenTelemetry GenAI Agent Spans) | Axes : `RQ3, RQ6`
- **Synthèse factuelle** : Cette spécification du groupe d'intérêt spécial GenAI d'OpenTelemetry normalise les attributs, événements et métriques des traces distribuées (« spans ») pour la création d'agents (create_agent), leur invocation client ou interne (invoke_agent), la planification (plan) et l'exécution d'outils (execute_tool). Elle précise les champs obligatoires et conditionnels couvrant l'identifiant stable de l'agent (gen_ai.agent.id), la version, le modèle et les captures optionnelles (« Opt-In ») des instructions système sans exposer par défaut les données sensibles. Ces conventions soutiennent directement l'instrumentation télémétrique à double couloir des chapitres 4, 6 et 9.

### [6] SRC-044 — RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT)

- **Auteurs / Émetteur** : Henk Birkholz, Antoine Delignat-Lavaud, Cedric Fournet, Yogesh Deshpande, Steve Lasker (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9943`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9943.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-044.txt` (9450 mots, 65476 octets)
- **Empreinte SHA-256** : `3ae677b4a295a3ee3eb793d39daf3d2a1139b041ff019fc5317bfe24a3fa3ae6`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9943, juin 2026) | Axes : `RQ4, RQ5`
- **Synthèse factuelle** : La RFC 9943 normalise l'architecture SCITT (Supply Chain Integrity, Transparency, and Trust) pour l'enregistrement et l'audit d'énoncés signés par un émetteur unique dans des journaux transparents fondés sur des structures de données vérifiables (arbres de Merkle anti-équivocation). Elle permet à toute partie vérifiante d'obtenir la preuve cryptographique qu'un manifeste logiciel, une attestation de modèle ou un serveur d'outils a bien été enregistré et validé à un instant donné. SCITT offre une réponse normalisée aux attaques sur la chaîne d'approvisionnement d'outils agentiques et aux exigences de traçabilité d'audit.

### [7] SRC-054 — NIST AI 100-2e2025: Adversarial Machine Learning — A Taxonomy and Terminology of Attacks and Mitigations

- **Auteurs / Émetteur** : Alina Oprea, Apostol Vassilev et al. (NIST) (2025, 2025-03-01)
- **Revue / Organisme / Dépôt** : NIST — Identifiant : `NIST-AI-100-2E2025`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-054.txt` (48743 mots, 347771 octets)
- **Empreinte SHA-256** : `1f113bf38b90261c6372c5b9a8d77a4355c7e4fa0ccf11b4d179930a9a0dfa7f`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Taxonomie normative officielle (NIST AI 100-2e2025) | Axes : `RQ5`
- **Synthèse factuelle** : Ce rapport du NIST établit une taxonomie et une terminologie de référence en apprentissage automatique antagoniste (Adversarial Machine Learning) couvrant aussi bien l'IA prédictive que l'IA générative. Il classe systématiquement les attaques selon le stade du cycle de vie, les objectifs (compromission d'intégrité, disponibilité, vie privée), les capacités et la connaissance de l'attaquant, puis associe les mesures d'atténuation disponibles et leurs limites persistantes. Ce cadre permet aux chapitres 5, 8 et 9 de distinguer empoisonnement, évasion et détournement de contexte.

### [8] SRC-057 — Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem

- **Auteurs / Émetteur** : Obada Kraishan (2026, 2026-09-12)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2609.14119`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2609.14119
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-057.txt` (7412 mots, 49308 octets)
- **Empreinte SHA-256** : `cae21acac54fea61a6270540a888a090731fac9d0de3ae0f121f3d51d59ed7e9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Recensement empirique de sécurité sur registre public (21 643 serveurs MCP, 2026) | Axes : `RQ5`
- **Synthèse factuelle** : Kraishan réalise en août–septembre 2026 le premier recensement complet du registre public MCP en collectant 21 643 serveurs (72 606 versions) et en analysant le code source de 14 353 d'entre eux à l'aide d'un analyseur à huit classes de menaces calibré sur 414 cas vérifiés manuellement. L'étude observe une prévalence élevée d'exposition réseau sans authentification (9,57 % des serveurs analysés) ainsi que des phénomènes de « dérive silencieuse » où un même nom de serveur change discrètement de comportement ou d'implémentation. Ce constat empirique justifie les sas d'assainissement et le registre d'outils signé SCITT aux chapitres 4, 8 et 9.

### [9] SRC-058 — STAMP/STPA Informed Characterization of Factors Leading to Loss of Control in AI Systems

- **Auteurs / Émetteur** : Steve Barrett, Anna Bruvere, Sean P. Fillingham, Catherine Rhodes (2025, 2025-12-19)
- **Revue / Organisme / Dépôt** : arXiv (Centre for the Study of Existential Risk) — Identifiant : `arXiv:2512.17600`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.17600
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-058.txt` (17212 mots, 112088 octets)
- **Empreinte SHA-256** : `78b03417f4de11b0132a9afce95e493bec8b9028715ec9b9139aa504d4599ecb`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Cadre d'analyse de sûreté système (Barrett et al., STAMP/STPA, déc. 2025) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Barrett, Bruvere, Fillingham, Rhodes et Vergani (Arcadia Impact / CSER / King's College London) appliquent la méthodologie d'ingénierie de la sûreté STAMP/STPA pour caractériser systématiquement les facteurs causaux menant à une perte de contrôle dans les systèmes sociotechniques intégrant l'IA. Plutôt que de traiter uniquement les défaillances isolées de composants, l'approche modélise les boucles de contrôle, les actions de contrôle dangereuses et les défauts de rétroaction entre concepteurs, opérateurs humains et composants autonomes. Elle fonde en L+ les analyses de boucles de contrainte et de gouvernance opérationnelle des chapitres 8, 9, 11 et 12.

### [10] SRC-059 — System level governance of generative AI risks in cross border e-commerce supply chains

- **Auteurs / Émetteur** : Ionel Bostan (2026, 2026-08-27)
- **Revue / Organisme / Dépôt** : Discover Computing (Springer OA) — Identifiant : `DOI:10.1007/s10791-026-10509-y`
- **URL ouverte vérifiée** : https://link.springer.com/article/10.1007/s10791-026-10509-y
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-059.txt` (10544 mots, 82590 octets)
- **Empreinte SHA-256** : `dd42130bd7b9ad14912eff39a8ea5234d48eb8f80a2f1f6cc0b325da4d106fa9`
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
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-065.txt` (7675 mots, 64813 octets)
- **Empreinte SHA-256** : `886e1d96170f5def8a72bc30a2d8d68ef49d2fc2728e79cf97b3d7dbedd19322`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Ligne directrice prudentielle fédérale officielle (BSIF E-23, édition 2027) | Axes : `RQ6`
- **Synthèse factuelle** : La ligne directrice E-23 révisée du Bureau du surintendant des institutions financières sur la gestion du risque de modélisation à l'échelle de l'entreprise affiche explicitement une date d'entrée en vigueur fixée « Le 1 mai 2027 ». Elle étend formellement le champ du risque de modélisation au-delà des modèles statistiques classiques pour englober les modèles d'intelligence artificielle et d'apprentissage automatique à travers tout leur cycle de vie (inventaire, validation indépendante, surveillance continue et gouvernance des compétences). Elle constitue l'ancre prudentielle canadienne structurante de la troisième et quatrième partie.

### [14] SRC-066 — Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security and Operational Risk

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2026, 2026-07-01)
- **Revue / Organisme / Dépôt** : OSFI Technology Risk Bulletin — Identifiant : `OSFI-BULLETIN-AGENTIC-2026`
- **URL ouverte vérifiée** : http://www.osfi-bsif.gc.ca/en/risks/technology-cyber-risk-management/technology-risk-bulletin/generative-agentic-artificial-intelligence-implications-technology-cyber-security-operational
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-066.txt` (4194 mots, 49330 octets)
- **Empreinte SHA-256** : `362c9639e348264a5fb303562725378b726185cd4d26914724182736c0c07d69`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Bulletin officiel de risque technologique et cyber (OSFI/BSIF, juillet 2026) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Publié en juillet 2026, ce bulletin du BSIF analyse spécifiquement les risques technologiques, cybernétiques et opérationnels introduits par l'IA générative et l'IA agentique (définie par le raisonnement et l'exécution autonomes) dans les institutions financières fédérales. Le régulateur avertit que ces technologies élargissent les surfaces d'attaque, accélèrent la propagation des défaillances et mettent à l'épreuve les contrôles existants sous les lignes directrices B-13, B-10 et E-21. Il recommande une gouvernance renforcée de l'autonomie, une journalisation et surveillance accrues ainsi que des plans de continuité adaptés aux collectifs d'agents.

### [15] SRC-067 — Guideline B-15: Climate Risk Management

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2025, 2025-03-07)
- **Revue / Organisme / Dépôt** : OSFI Canada — Identifiant : `OSFI-B15`
- **URL ouverte vérifiée** : https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/climate-risk-management
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-067.txt` (8175 mots, 68377 octets)
- **Empreinte SHA-256** : `cd686b65d8f7a6abd08c9acfe8b09f6f6c68e0900e51f2d1dcc04aa3963d7079`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Ligne directrice prudentielle climatique officielle (OSFI/BSIF B-15) | Axes : `RQ6`
- **Synthèse factuelle** : La ligne directrice B-15 du BSIF fixe les attentes de divulgation financière liée au climat pour les institutions financières fédérales en s'appuyant sur le GHG Protocol et la norme PCAF pour la comptabilisation des émissions financées et assurées. Dans le tableau récapitulatif de l'annexe 2-2 (élément b) ii), la date d'exercice financier attendue pour la divulgation des émissions absolues brutes de portée 3 — incluant obligatoirement la catégorie 15 des prêts, investissements et portefeuilles d'assurance — est arrêtée à 2028 (tandis que le volet b) iii visant les actifs sous gestion demeure marqué TBD). Ce texte officialise le jalon de fin 2028 exploité aux chapitres 9 et 12.

### [16] SRC-068 — Guideline B-10: Third-Party Risk Management

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2023, 2023-04-24)
- **Revue / Organisme / Dépôt** : OSFI Canada — Identifiant : `OSFI-B10`
- **URL ouverte vérifiée** : https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/third-party-risk-management-guideline
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-068.txt` (9964 mots, 88262 octets)
- **Empreinte SHA-256** : `596393b79ecc10a1f5b9a3e1b38e9932ccc9fa4c2303afb5c3756947fae9ce4f`
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
