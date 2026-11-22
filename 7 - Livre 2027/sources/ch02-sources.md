# Dossier fermé de sources L+ — Chapitre 02 — L'épreuve des mesures : investissements géants, bancs biaisés et productivité réelle

- **Unité du livre** : `ch02` (`sources/ch02-sources.md`)
- **Axes de recherche couverts** : `RQ1, RQ2`
- **Date de gel des faits** : 31 décembre 2026
- **Protocole** : `MLR-PRISMA-SCR-LIVRE-2027-V1.2` (`metadata_only_pct = 0.0 %`, règle stricte `AO-01` sans contournement)
- **Nombre de sources probantes incluses** : 18 sources intégrales `L+`

> Ce dossier fermé recense exclusivement les sources primaires et travaux ouverts dont le texte intégral UTF-8 a été extrait, conservé sous `recherche/corpus_l_plus/` et authentifié par empreinte `SHA-256`. Aucune source en `statut F` ni copie locale non ouverte n'entre dans l'argumentation probante.

Note AO-01 (statut F) : le communiqué primaire de Gartner (25 juin 2025, HTTP 403), sa reprise Reuters (HTTP 401), l'article HTML Statistique Canada 11-621-m (HTTP 403) ainsi que les études commerciales Polaris, Fortune Business Insights et IDC sont consignés en statut F dans `recherche/registre-statut-f.json` et exclus des preuves directes.

---

### [1] SRC-001 — From AGI to ASI

- **Auteurs / Émetteur** : Tim Genewein, Matija Franklin, Alexander Lerchner, Laurent Orseau et al. (2026, 2026-06-10)
- **Revue / Organisme / Dépôt** : arXiv (Google DeepMind) — Identifiant : `arXiv:2606.12683`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2606.12683
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-001.txt` (35148 mots, 241842 octets)
- **Empreinte SHA-256** : `edd192381975a8159249a6bb7db581577959d30f2cf408869dfb67786ac8b8cf`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Essai prospectif théorique et quantitatif (Google DeepMind) | Axes : `RQ1, RQ2`
- **Synthèse factuelle** : Cette étude de Google DeepMind analyse les trajectoires technologiques menant de l'intelligence artificielle générale aux systèmes superintelligents et chiffre la croissance historique du stock mondial de calcul effectif. Les auteurs montrent (note 2, p. 4) qu'un gain matériel annuel de ~1,5×, combiné à ~3× d'efficacité algorithmique et ~2,5× de croissance des dépenses matérielles, produit un facteur composé de 11,25× arrondi prudemment à au moins 10× par an sur la dernière décennie. Ils formalisent également le problème de la « barrière d'abstraction » (§ 5.5), expliquant pourquoi des modèles numériques à bande passante élevée risquent de produire des abstractions incompatibles avec la supervision humaine. Pour l'ouvrage, ce document ancre l'origine matérielle et algorithmique de l'industrialisation cognitive et la nécessité d'un contrôle institutionnel continu.

### [2] SRC-003 — Towards a Science of Scaling Agent Systems

- **Auteurs / Émetteur** : Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park et al. (2025, 2025-12-09)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2512.08296`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.08296
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-003.txt` (18743 mots, 145288 octets)
- **Empreinte SHA-256** : `991148d77ecdcd5a7ba19a0f6ce1ff3c5d8f54c8abea67debf7182a1296a559f`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Étude empirique expérimentale sur lois d'échelle multi-agents | Axes : `RQ2`
- **Synthèse factuelle** : Kim et al. évaluent systématiquement comment la performance d'agents à base de modèles de langage évolue lorsqu'on augmente le nombre d'agents coordonnés sur des tâches séquentielles ou parallélisables. Leurs courbes (figure 5, p. 22) démontrent que les systèmes multi-agents centralisés et décentralisés plafonnent rapidement et se dégradent selon la capacité du modèle sous-jacent (Gemini 2.0 Flash vs 2.5 Pro) et la nature de la tâche. Les auteurs identifient trois mécanismes majeurs de dégradation : les erreurs de logique sur les prémisses, la dérive numérique cumulée dépassant 5 % d'écart et l'omission progressive du contexte partagé. Ce travail contredit l'heuristique naïvement additive voulant que multiplier les agents améliore automatiquement la fiabilité.

### [3] SRC-008 — Artificial Intelligence Index Report 2026

- **Auteurs / Émetteur** : Sha Sajadieh, Loredana Fattorini, Raymond Perrault, Yolanda Gil et al. (2026, 2026-04-14)
- **Revue / Organisme / Dépôt** : Stanford HAI / arXiv — Identifiant : `arXiv:2606.15708`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2606.15708
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-008.txt` (132584 mots, 880133 octets)
- **Empreinte SHA-256** : `11f49f977f4ddb87ba28743c0f4edb3b6e2a440be766df60207661655de38363`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Rapport statistique et bibliométrique annuel (Stanford HAI 2026) | Axes : `RQ1, RQ6`
- **Synthèse factuelle** : L'édition 2026 de l'AI Index Report de Stanford HAI compile les tendances mondiales de recherche, de performance technique, d'économie du travail et de réglementation de l'IA. Dans son analyse économique des métiers exposés, le rapport montre qu'aux États-Unis l'emploi des développeurs logiciels âgés de 22 à 25 ans a reculé de près de 20 % depuis 2024, alors que les effectifs des développeurs plus expérimentés poursuivent leur croissance. Il documente également l'expansion continue du volume de publications scientifiques (environ 258 000 articles en 2024, soit 40,9 % de la recherche informatique dans OpenAlex) et l'accélération des investissements d'infrastructure. Ce jeu de données sert de repère quantitatif principal pour la crise de l'apprentissage junior et la gouvernance des compétences.

### [4] SRC-011 — Agentic AI orchestration: TMT Predictions 2026

- **Auteurs / Émetteur** : Deloitte Insights (2025, 2025-11-18)
- **Revue / Organisme / Dépôt** : Deloitte Center for Technology, Media & Telecommunications — Identifiant : `DELOITTE-TMT-2026-AGENTS`
- **URL ouverte vérifiée** : https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/ai-agent-orchestration.html
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-011.txt` (6070 mots, 46734 octets)
- **Empreinte SHA-256** : `8f00ca31f3414401a18347cc57b42eecf993f9a88d115454db7d8f76082111a2`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `9.5/12` | Devis : Rapport sectoriel de veille technologique (Deloitte TMT Predictions 2026) | Axes : `RQ1, RQ2`
- **Synthèse factuelle** : Publié le 18 novembre 2025, ce rapport analyse le passage des assistants isolés à l'orchestration multi-agents en entreprise et détaille les couches requises : plan de contexte et mémoire, sélection adaptative de modèles, télémétrie et expérience utilisateur. Deloitte rapporte que les estimations de marché placent les agents autonomes à 8,5 G\$ US en 2026 et 35 G\$ US en 2030, voire jusqu'à 45 G\$ US si les entreprises résolvent les goulots d'orchestration. Surtout, le document reprend l'estimation de Gartner (juin 2025, dont le communiqué primaire et Reuters sont en statut F) selon laquelle plus de 40 % des projets agentiques actuels risquent d'être annulés d'ici 2027 faute de maîtrise des coûts, de complexité d'échelle ou de gestion des risques.

### [5] SRC-012 — Agentic AI Market Size & Share Analysis — Growth Trends and Forecast

- **Auteurs / Émetteur** : Mordor Intelligence (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : Mordor Intelligence — Identifiant : `MORDOR-AGENTIC-AI-2026`
- **URL ouverte vérifiée** : https://www.mordorintelligence.com/industry-reports/agentic-ai-market
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-012.txt` (6584 mots, 47538 octets)
- **Empreinte SHA-256** : `d36ecb1c274ce55607835b6e3c6c5b4e02d1868265e37f73a79173ace448bef6`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `9.0/12` | Devis : Étude de marché sectorielle en accès ouvert (Mordor Intelligence 2026) | Axes : `RQ1`
- **Synthèse factuelle** : Cette analyse ouverte du marché de l'IA agentique évalue la taille mondiale à 9,89 G\$ US en 2026 et à 14,06 G\$ US en 2027, avec une projection atteignant 82,27 G\$ US en 2032 au taux de croissance annuel composé de 42,38 % sur la période 2027–2032 (soit environ 40,6 G\$ US par interpolation à l'horizon 2030). Le rapport identifie les services financiers et bancaires (BFSI) et l'automatisation de processus comme moteurs principaux en Amérique du Nord, tout en soulignant la hausse des coûts de calcul d'orchestration, le manque d'interopérabilité et le verrouillage fournisseur comme freins majeurs. Utilisée conjointement avec Deloitte et Grand View, elle borne la fourchette haute ouverte du marché 2026–2030.

### [6] SRC-013 — Enterprise Agentic AI Market Size, Share & Trends Analysis Report

- **Auteurs / Émetteur** : Grand View Research (2025, 2025-10-01)
- **Revue / Organisme / Dépôt** : Grand View Research — Identifiant : `GVR-ENT-AGENTIC-AI-2025`
- **URL ouverte vérifiée** : https://www.grandviewresearch.com/industry-analysis/enterprise-agentic-ai-market-report
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-013.txt` (3783 mots, 30757 octets)
- **Empreinte SHA-256** : `1ad2496d415a6facb36d9ed8f9c889e9eaa08f962d54fb8f1de9ae6221c33cab`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `9.0/12` | Devis : Étude de marché segment entreprise (Grand View Research) | Axes : `RQ1`
- **Synthèse factuelle** : Le rapport de Grand View Research centré sur le segment « entreprise » de l'IA agentique chiffre le marché mondial à 2,6 G\$ US en 2024, l'estime à 5,3 G\$ US en 2026 et le projette à 24,5 G\$ US en 2030 selon un taux de croissance annuel composé de 46,2 % sur 2025–2030 (soit environ 7,75 G\$ US en 2027). L'Amérique du Nord représente plus de 39 % des revenus initiaux, portée par le basculement progressif d'agents simples vers des systèmes multi-agents d'entreprise. Ce périmètre restrictif axé entreprise fournit la borne basse de la fourchette L+ pour l'enveloppe de marché 2026–2030 face aux séries commerciales exclues en statut F.

### [7] SRC-017 — Alphabet Inc. Form 8-K Exhibit 99.1 — Q3 2026 Financial Results

- **Auteurs / Émetteur** : Alphabet Inc. (2026, 2026-10-28)
- **Revue / Organisme / Dépôt** : U.S. SEC EDGAR — Identifiant : `SEC-GOOG-8K-2026Q3`
- **URL ouverte vérifiée** : https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-017.txt` (3730 mots, 25461 octets)
- **Empreinte SHA-256** : `ebfea816ab26e93d4f4b837fbbeea00d626ed26b9f023a76c4ae7db25d6d48e7`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Dépôt réglementaire financier officiel (SEC Form 8-K Ex. 99.1, Q3 2026) | Axes : `RQ1`
- **Synthèse factuelle** : Le communiqué financier officiel d'Alphabet Inc. pour le troisième trimestre clos le 30 septembre 2026 (déposé le 28 octobre 2026) fait état d'un chiffre d'affaires trimestriel consolidé de 127,6 G\$ US (+25 %) et détaille le tableau des flux de trésorerie. Sur les neuf premiers mois calendaires de 2026, les acquisitions d'immobilisations corporelles en trésorerie (« Purchases of property and equipment ») atteignent 131 953 M\$ US (dont 51 355 M\$ au seul T3 2026, portant le flux de trésorerie disponible trimestriel à -9 065 M\$), soit 159 804 M\$ US sur douze mois glissants contre 63 596 M\$ US sur 9M 2025. Ce document constitue l'une des quatre pièces comptables primaires mesurant l'ampleur historique de l'effort d'infrastructure IA.

### [8] SRC-018 — Amazon.com, Inc. Form 8-K Exhibit 99.1 — Q3 2026 Financial Results and 2026 CapEx Guidance

- **Auteurs / Émetteur** : Amazon.com, Inc. (2026, 2026-10-29)
- **Revue / Organisme / Dépôt** : U.S. SEC EDGAR — Identifiant : `SEC-AMZN-8K-2026Q3`
- **URL ouverte vérifiée** : https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20260930xex991.htm
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-018.txt` (5981 mots, 39402 octets)
- **Empreinte SHA-256** : `8da73deea031eeb68c1ff6501b08f4eb681248b18dde64cf2d68a8dd65d608a9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Dépôt réglementaire financier officiel (SEC Form 8-K Ex. 99.1, Q3 2026) | Axes : `RQ1`
- **Synthèse factuelle** : Le dépôt Form 8-K d'Amazon.com, Inc. pour le T3 2026 (29 octobre 2026) rapporte des ventes AWS en hausse de 39,3 % (rythme annualisé de 184 G\$ US) ainsi que le lancement du service Bedrock Managed Agents et du harnais Strands. Au tableau des flux de trésorerie, les achats d'immobilisations corporelles s'élèvent à 175 670 M\$ US sur neuf mois 2026 (contre 92 297 M\$ US en 9M 2025), creusant le flux de trésorerie disponible sur douze mois glissants à -42,4 G\$ US. Surtout, la prévision financière officielle pour l'exercice 2026 maintient explicitement une cible d'environ 220 G\$ US en dépenses d'investissement en trésorerie.

### [9] SRC-019 — Meta Platforms, Inc. Form 8-K Exhibit 99.1 — Q3 2026 Results and 2026 CapEx Guidance

- **Auteurs / Émetteur** : Meta Platforms, Inc. (2026, 2026-10-21)
- **Revue / Organisme / Dépôt** : U.S. SEC EDGAR — Identifiant : `SEC-META-8K-2026Q3`
- **URL ouverte vérifiée** : https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-09302026xexhibit991.htm
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-019.txt` (3681 mots, 25225 octets)
- **Empreinte SHA-256** : `bb4724559067335d931adf053587027a7f013b526abe9cd6cd3c8609908289e0`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Dépôt réglementaire financier officiel (SEC Form 8-K Ex. 99.1, Q3 2026) | Axes : `RQ1`
- **Synthèse factuelle** : Le communiqué Q3 2026 de Meta Platforms, Inc. (21 octobre 2026) consigne des achats d'immobilisations corporelles de 83 055 M\$ US sur neuf mois 2026 (contre 48 308 M\$ US en 9M 2025) et un CapEx trimestriel de 34,91 G\$ US en incluant les paiements en principal des contrats de location-financement (flux de trésorerie disponible du T3 négatif à -2,12 G\$). Dans les prévisions de direction (« CFO Outlook Commentary »), Meta resserre sa fourchette annuelle 2026 de dépenses d'investissement — incluant les contrats de location-financement — entre 135 G\$ US et 145 G\$ US. Ce périmètre comptable distinct explique la nécessité de documenter explicitement l'hétérogénéité des définitions de CapEx entre hyperscalers.

### [10] SRC-020 — Microsoft Corporation Form 10-Q — Quarter Ended September 30, 2026 (Q1 FY2027)

- **Auteurs / Émetteur** : Microsoft Corporation (2026, 2026-10-28)
- **Revue / Organisme / Dépôt** : U.S. SEC EDGAR — Identifiant : `SEC-MSFT-10Q-2026Q3`
- **URL ouverte vérifiée** : https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-020.txt` (30230 mots, 226244 octets)
- **Empreinte SHA-256** : `8277bdc9e23911388238a7748ae4a3e116e56d3c7aab84c3fbaae2ca6028942b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Dépôt réglementaire financier officiel (SEC Form 10-Q Q1 FY2027) | Axes : `RQ1`
- **Synthèse factuelle** : Le rapport trimestriel Form 10-Q de Microsoft Corporation pour le trimestre clos le 30 septembre 2026 (déposé le 28 octobre 2026) présente des revenus de 92 279 M\$ US (+19 %) et un résultat d'exploitation de 45 915 M\$ US. Aux flux de trésorerie d'investissement, les additions aux immobilisations corporelles en trésorerie (« Additions to property and equipment ») atteignent 39 367 M\$ US pour le trimestre juillet–septembre 2026, soit plus du double des 19 394 M\$ US de la période correspondante de 2025, hors engagements additionnels de location-financement de centres de données (note 12). Ce trimestre forme le troisième tiers des dépenses calendaires de trésorerie 2026 de Microsoft.

### [11] SRC-021 — Microsoft Corporation Form 10-K — Fiscal Year Ended June 30, 2026

- **Auteurs / Émetteur** : Microsoft Corporation (2026, 2026-07-29)
- **Revue / Organisme / Dépôt** : U.S. SEC EDGAR — Identifiant : `SEC-MSFT-10K-FY2026`
- **URL ouverte vérifiée** : https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-021.txt` (48983 mots, 362449 octets)
- **Empreinte SHA-256** : `ff8124e94093e324235983f12e8c74b1f4f16db9d3733d6e393028a65861682c`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Dépôt réglementaire financier officiel (SEC Form 10-K FY2026) | Axes : `RQ1`
- **Synthèse factuelle** : Le rapport annuel Form 10-K de Microsoft Corporation pour l'exercice fiscal clos le 30 juin 2026 (déposé le 29 juillet 2026) atteste d'additions en trésorerie aux immobilisations corporelles de 115 948 M\$ US sur douze mois (contre 64 551 M\$ US en FY2025 et 44 477 M\$ US en FY2024). Le rapport détaille également les engagements pluriannuels hors bilan liés aux contrats de location-financement et d'exploitation d'infrastructures informatiques et de centres de données (443 506 M\$ US au total). Combiné aux deux rapports 10-Q encadrants, ce dépôt permet le calcul exact des décaissements de janvier à septembre 2026.

### [12] SRC-022 — Microsoft Corporation Form 10-Q — Six Months Ended December 31, 2025 (Q2 FY2026)

- **Auteurs / Émetteur** : Microsoft Corporation (2026, 2026-01-28)
- **Revue / Organisme / Dépôt** : U.S. SEC EDGAR — Identifiant : `SEC-MSFT-10Q-2025Q4`
- **URL ouverte vérifiée** : https://www.sec.gov/Archives/edgar/data/789019/000119312526027207/msft-20251231.htm
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-022.txt` (31330 mots, 237215 octets)
- **Empreinte SHA-256** : `1dc9127a22fb2e5e535616c7f1a37cb9fc31593d1a1cfbab7ba5526ed5ac5ac4`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Dépôt réglementaire financier officiel (SEC Form 10-Q Q2 FY2026) | Axes : `RQ1`
- **Synthèse factuelle** : Le rapport Form 10-Q de Microsoft Corporation pour le semestre clos le 31 décembre 2025 (déposé le 28 janvier 2026) enregistre 49 270 M\$ US d'additions en trésorerie aux immobilisations corporelles entre juillet et décembre 2025. Par différence exacte avec le 10-K FY2026 (115 948 M\$ US), Microsoft a décaissé 66 678 M\$ US de janvier à juin 2026, puis 39 367 M\$ US au trimestre suivant, soit exactement 106 045 M\$ US (106,0 G\$ US) sur les neuf premiers mois calendaires de 2026. Additionnée à Alphabet, Amazon et Meta, la somme vérifiée en trésorerie sur neuf mois s'élève à 496 723 M\$ US (496,7 G\$ US).

### [13] SRC-023 — FinOps Open Cost and Usage Specification (FOCUS) v1.4

- **Auteurs / Émetteur** : FinOps Foundation (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : Linux Foundation / FinOps Foundation — Identifiant : `FINOPS-FOCUS-1.4`
- **URL ouverte vérifiée** : https://focus.finops.org/focus-specification/v1-4/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-023.txt` (408 mots, 2805 octets)
- **Empreinte SHA-256** : `e6f6f27c0a5402244bc16e3e0bedfe7fad2c0556f915584599670289526e8fea`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Spécification ouverte de normalisation comptable cloud (FinOps FOCUS v1.4) | Axes : `RQ1, RQ3`
- **Synthèse factuelle** : La spécification FinOps Open Cost and Usage Specification (FOCUS v1.4, Linux Foundation) normalise le schéma des données de facturation et d'utilisation des ressources infonuagiques entre fournisseurs. Elle définit des colonnes et conventions terminologiques unifiées permettant aux équipes d'ingénierie et de finance d'exécuter de manière homogène la rétrofacturation interne (chargeback), l'imputation des coûts par produit ou agent, la budgétisation et la prévision. Dans l'ouvrage, FOCUS sert de standard pivot pour relier la consommation de jetons et de calcul au coût complet par résultat conforme (CPO).

### [14] SRC-024 — NIST/SEMATECH e-Handbook of Statistical Methods — Section 8.1.8.1 Series Model (Lusser Reliability Law)

- **Auteurs / Émetteur** : National Institute of Standards and Technology (NIST) / SEMATECH (2012, 2012-04-01)
- **Revue / Organisme / Dépôt** : NIST Information Technology Laboratory — Identifiant : `NIST-HANDBOOK-8.1.8.1`
- **URL ouverte vérifiée** : https://www.itl.nist.gov/div898/handbook/apr/section1/apr181.htm
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-024.txt` (467 mots, 3049 octets)
- **Empreinte SHA-256** : `8734d2a7119029ec0a3459f4c9f33332967e14e2742b40938f3c53a2e94c01da`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Manuel statistique normatif de fiabilité industrielle (NIST/SEMATECH § 8.1.8.1) | Axes : `RQ2`
- **Synthèse factuelle** : La section 8.1.8.1 du manuel NIST/SEMATECH formalise le modèle des risques concurrents (système en série ou loi multiplicative de Lusser) lorsque les modes de défaillance de composants enchaînés sont indépendants et que la première défaillance fait échouer l'ensemble. La fiabilité globale du système s'écrit comme le produit des fiabilités individuelles des composants, tandis que les taux de défaillance s'additionnent. Appliquée à une chaîne de 10 étapes autonomes indépendantes fiables chacune à 94 %, cette loi donne une réussite sans erreur de 0,94^10 = 53,86 % (53,9 %), fondant la critique des enchaînements probabilistes longs.

### [15] SRC-025 — Measuring AI Ability to Complete Long Tasks

- **Auteurs / Émetteur** : METR Research (2025, 2025-03-19)
- **Revue / Organisme / Dépôt** : METR — Identifiant : `METR-HORIZON-2025`
- **URL ouverte vérifiée** : https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-025.txt` (2347 mots, 14806 octets)
- **Empreinte SHA-256** : `ebd5b0ac94c9de5f82557e59df11222b7df40c35457f20517f7b240bcb40f05d`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Étude empirique longitudinale sur banc d'essai temporel (METR 2025) | Axes : `RQ2`
- **Synthèse factuelle** : METR propose d'évaluer la capacité des agents autonomes non par un score ponctuel abstrait mais par la durée humaine des tâches logicielles qu'ils parviennent à achever avec un seuil de fiabilité fixé (50 % ou 80 %). Sur six ans d'historique empirique, l'horizon temporel des tâches complétées à 50 % de fiabilité par les meilleurs agents a doublé approximativement tous les sept mois. L'étude met toutefois en évidence l'écart critique entre la réussite à 50 % (tolérable en expérimentation interactive) et la constance élevée exigée en production réglementée.

### [16] SRC-027 — Measuring Agents in Production (MAP)

- **Auteurs / Émetteur** : Melissa Z. Pan, Negar Arabzadeh, Riccardo Cogo, Yuxuan Zhu et al. (2025, 2025-12-02)
- **Revue / Organisme / Dépôt** : arXiv (UC Berkeley) — Identifiant : `arXiv:2512.04123`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.04123
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-027.txt` (22684 mots, 160353 octets)
- **Empreinte SHA-256** : `3f8f34adaeb523b3cdc740f8df9d4c97b621f9ac7f955c10d94e3fbc97dcc2e1`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Étude mixte terrain (20 études de cas et enquête sur 306 répondants / 86 systèmes) | Axes : `RQ2, RQ6`
- **Synthèse factuelle** : L'étude Measuring Agents in Production (MAP) de Pan et al. documente comment les praticiens conçoivent réellement les agents en exploitation à travers 20 entrevues approfondies et 306 réponses d'enquête couvrant 26 domaines (86 praticiens en production). Contre le mythe de l'autonomie ouverte, 68 % des systèmes déployés exécutent au plus 10 étapes avant intervention humaine, 80 % des études de cas (16 sur 20) utilisent des flux de travail structurés fixes, 70 % conservent des modèles commerciaux sans réentraînement des poids et 79 % rédigent les invites manuellement. Les organisations sacrifient délibérément l'autonomie ouverte au profit de la prévisibilité et de la maîtrise du risque.

### [17] SRC-028 — Why Do Multi-Agent LLM Systems Fail? (MAST)

- **Auteurs / Émetteur** : Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal et al. (2025, 2025-03-17)
- **Revue / Organisme / Dépôt** : NeurIPS 2025 / arXiv — Identifiant : `arXiv:2503.13657`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.13657
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-028.txt` (19765 mots, 136729 octets)
- **Empreinte SHA-256** : `7eeb1c6dfd098f1f6507ab979bdae4a7a2eacc1888efc0d599aca663f6577933`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Taxonomie empirique et jeu de données annoté (NeurIPS 2025 / MAST-Data) | Axes : `RQ2`
- **Synthèse factuelle** : Cemri et al. analysent plus de 1 600 traces (1 642 traces dans MAST-Data) issues de sept cadriciels multi-agents open source populaires (dont AutoGen, CrewAI, ChatDev, MetaGPT et Manus) et construisent la taxonomie MAST à 14 modes de défaillance regroupés en 3 catégories : conception système, désalignement inter-agents et vérification/terminaison. Les taux d'échec observés sur les systèmes évalués varient de 41 % à 86,7 %, mettant en évidence que la plupart des défaillances proviennent de la coordination, de l'oubli de spécifications ou d'absences de garde-fous de vérification plutôt que des capacités intrinsèques du LLM. Ces mesures fondent l'exigence de tests structurels et de contrôle déterministe.

### [18] SRC-031 — Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

- **Auteurs / Émetteur** : Dat Tran, Douwe Kiela (2026, 2026-04-02)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2604.02460`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2604.02460
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-031.txt` (11295 mots, 74996 octets)
- **Empreinte SHA-256** : `80b064f92eb145f5ff0977ee03fb95543bb95599007e69ded99c08927edac0e9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Analyse théorique et expérimentale à budget de calcul constant (Stanford) | Axes : `RQ2`
- **Synthèse factuelle** : Tran et Kiela établissent, à partir de l'inégalité de traitement des données, qu'à budget égal de jetons de raisonnement et sous utilisation efficace du contexte, un agent unique est théoriquement plus efficace en information qu'un système multi-agents sur le raisonnement à sauts multiples. Leurs expériences montrent que les gains publiés en faveur des systèmes multi-agents proviennent souvent d'un biais de confusion lié à l'augmentation cachée du calcul en phase d'inférence. Lorsque le budget est normalisé, l'agent unique égale ou surpasse la plupart des architectures multi-agents, ces dernières ne redevenant compétitives que lorsque le contexte individuel sature.
