# Dossier fermé de sources L+ — Chapitre 03 — Les nouvelles frontières de la firme : Coase chez les agents autonomes

- **Unité du livre** : `ch03` (`sources/ch03-sources.md`)
- **Axes de recherche couverts** : `RQ1`
- **Date de gel des faits** : 31 décembre 2026
- **Protocole** : `MLR-PRISMA-SCR-LIVRE-2027-V1.2` (`metadata_only_pct = 0.0 %`, règle stricte `AO-01` sans contournement)
- **Nombre de sources probantes incluses** : 14 sources intégrales `L+`

> Ce dossier fermé recense exclusivement les sources primaires et travaux ouverts dont le texte intégral UTF-8 a été extrait, conservé sous `recherche/corpus_l_plus/` et authentifié par empreinte `SHA-256`. Aucune source en `statut F` ni copie locale non ouverte n'entre dans l'argumentation probante.

---

### [1] SRC-003 — Towards a Science of Scaling Agent Systems

- **Auteurs / Émetteur** : Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park et al. (2025, 2025-12-09)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2512.08296`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.08296
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-003.txt` (18743 mots, 145288 octets)
- **Empreinte SHA-256** : `991148d77ecdcd5a7ba19a0f6ce1ff3c5d8f54c8abea67debf7182a1296a559f`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Étude empirique expérimentale sur lois d'échelle multi-agents | Axes : `RQ2`
- **Synthèse factuelle** : Kim et al. évaluent systématiquement comment la performance d'agents à base de modèles de langage évolue lorsqu'on augmente le nombre d'agents coordonnés sur des tâches séquentielles ou parallélisables. Leurs courbes (figure 5, p. 22) démontrent que les systèmes multi-agents centralisés et décentralisés plafonnent rapidement et se dégradent selon la capacité du modèle sous-jacent (Gemini 2.0 Flash vs 2.5 Pro) et la nature de la tâche. Les auteurs identifient trois mécanismes majeurs de dégradation : les erreurs de logique sur les prémisses, la dérive numérique cumulée dépassant 5 % d'écart et l'omission progressive du contexte partagé. Ce travail contredit l'heuristique naïvement additive voulant que multiplier les agents améliore automatiquement la fiabilité.

### [2] SRC-006 — SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning

- **Auteurs / Émetteur** : Edward Y. Chang, Longling Geng (2025, 2025-03-15)
- **Revue / Organisme / Dépôt** : arXiv / VLDB — Identifiant : `arXiv:2503.11951`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.11951
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-006.txt` (9679 mots, 73051 octets)
- **Empreinte SHA-256** : `c2565e8391cc57e98ad4c7f26cac6b52dd76360de5a461152d2a94765e64e694`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Architecture transactionnelle et validation expérimentale (SagaLLM) | Axes : `RQ3`
- **Synthèse factuelle** : Chang et Geng documentent quatre défauts structurels des planificateurs multi-agents à base de LLM : l'auto-validation peu fiable, la perte de contexte sur horizons longs, l'absence de garanties transactionnelles et la coordination fragile entre agents distribués. Pour y remédier, SagaLLM adapte le patron des sagas compensatoires de Garcia-Molina en combinant mémoire persistante externe, validation indépendante par des agents tiers et journalisation explicite des états avant et après chaque action. L'architecture permet d'annuler ou de compenser les effets partiels d'un flux distribué lorsqu'une contrainte aval échoue sans immobiliser les ressources par verrou distribué ACID. Elle forme la référence directe de l'ouvrage pour les sagas à point pivot et l'exécution durable.

### [3] SRC-007 — Defeating Prompt Injections by Design (CaMeL)

- **Auteurs / Émetteur** : Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes et al. (2025, 2025-03-24)
- **Revue / Organisme / Dépôt** : arXiv / IEEE SaTML — Identifiant : `arXiv:2503.18813`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.18813
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-007.txt` (50342 mots, 361916 octets)
- **Empreinte SHA-256** : `49dbe34fe4cd657f9d22e5dfc3a6088dbce5935172937af6374bafdbf2bc188b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Système d'exécution sécurisé et évaluation sur banc AgentDojo (peer-reviewed) | Axes : `RQ5`
- **Synthèse factuelle** : Debenedetti et al. présentent CaMeL, une couche système de sécurité inspirée des langages à capacités et du patron Dual-LLM qui isole par construction le graphe d'appels d'outils du traitement de données externes non fiables. Un modèle planificateur traduit la requête approuvée en un sous-ensemble restreint de Python dont l'arbre syntaxique est interprété sous politiques de flux de données et de capacités, tandis qu'un modèle confiné sans accès aux outils privilégies résume les données brutes. Sur le banc AgentDojo, CaMeL résout 77 % des tâches avec une garantie structurelle contre l'injection de prompt indirecte, contre 84 % pour un agent sans défense. Cette source valide l'arbitrage sécurité-utilité et le principe de séparation contrôle-données en ingénierie.

### [4] SRC-011 — Agentic AI orchestration: TMT Predictions 2026

- **Auteurs / Émetteur** : Deloitte Insights (2025, 2025-11-18)
- **Revue / Organisme / Dépôt** : Deloitte Center for Technology, Media & Telecommunications — Identifiant : `DELOITTE-TMT-2026-AGENTS`
- **URL ouverte vérifiée** : https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/ai-agent-orchestration.html
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-011.txt` (6070 mots, 46734 octets)
- **Empreinte SHA-256** : `8f00ca31f3414401a18347cc57b42eecf993f9a88d115454db7d8f76082111a2`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `9.5/12` | Devis : Rapport sectoriel de veille technologique (Deloitte TMT Predictions 2026) | Axes : `RQ1, RQ2`
- **Synthèse factuelle** : Publié le 18 novembre 2025, ce rapport analyse le passage des assistants isolés à l'orchestration multi-agents en entreprise et détaille les couches requises : plan de contexte et mémoire, sélection adaptative de modèles, télémétrie et expérience utilisateur. Deloitte rapporte que les estimations de marché placent les agents autonomes à 8,5 G\$ US en 2026 et 35 G\$ US en 2030, voire jusqu'à 45 G\$ US si les entreprises résolvent les goulots d'orchestration. Surtout, le document reprend l'estimation de Gartner (juin 2025, dont le communiqué primaire et Reuters sont en statut F) selon laquelle plus de 40 % des projets agentiques actuels risquent d'être annulés d'ici 2027 faute de maîtrise des coûts, de complexité d'échelle ou de gestion des risques.

### [5] SRC-024 — NIST/SEMATECH e-Handbook of Statistical Methods — Section 8.1.8.1 Series Model (Lusser Reliability Law)

- **Auteurs / Émetteur** : National Institute of Standards and Technology (NIST) / SEMATECH (2012, 2012-04-01)
- **Revue / Organisme / Dépôt** : NIST Information Technology Laboratory — Identifiant : `NIST-HANDBOOK-8.1.8.1`
- **URL ouverte vérifiée** : https://www.itl.nist.gov/div898/handbook/apr/section1/apr181.htm
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-024.txt` (467 mots, 3049 octets)
- **Empreinte SHA-256** : `8734d2a7119029ec0a3459f4c9f33332967e14e2742b40938f3c53a2e94c01da`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Manuel statistique normatif de fiabilité industrielle (NIST/SEMATECH § 8.1.8.1) | Axes : `RQ2`
- **Synthèse factuelle** : La section 8.1.8.1 du manuel NIST/SEMATECH formalise le modèle des risques concurrents (système en série ou loi multiplicative de Lusser) lorsque les modes de défaillance de composants enchaînés sont indépendants et que la première défaillance fait échouer l'ensemble. La fiabilité globale du système s'écrit comme le produit des fiabilités individuelles des composants, tandis que les taux de défaillance s'additionnent. Appliquée à une chaîne de 10 étapes autonomes indépendantes fiables chacune à 94 %, cette loi donne une réussite sans erreur de 0,94^10 = 53,86 % (53,9 %), fondant la critique des enchaînements probabilistes longs.

### [6] SRC-026 — Cognitive Architectures for Language Agents (CoALA)

- **Auteurs / Émetteur** : Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, Thomas L. Griffiths (2024, 2024-03-15)
- **Revue / Organisme / Dépôt** : TMLR / arXiv — Identifiant : `arXiv:2309.02427`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2309.02427
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-026.txt` (18434 mots, 123231 octets)
- **Empreinte SHA-256** : `831e99a3f99a9f1e2cdc1c2940b3a2046ca2973226130c16ebf5d58b2acb3dde`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Article de synthèse architecturale évalué par les pairs (TMLR 2024) | Axes : `RQ2, RQ3`
- **Synthèse factuelle** : Sumers, Yao, Narasimhan et Griffiths transposent les sciences cognitives et les architectures symboliques classiques (SOAR, ACT-R) dans le cadre CoALA (Cognitive Architectures for Language Agents). Ils structurent tout agent autour d'une boucle décisionnelle itérative reliant une mémoire de travail et trois mémoires à long terme (épisodique, sémantique et procédurale) à un espace d'actions internes et d'appels d'outils externes. CoALA montre que le modèle de langage n'est qu'un composant statistique au sein d'un programme de flux de contrôle explicite, appuyant la séparation architecturale entre noyau déterministe et inférence.

### [7] SRC-027 — Measuring Agents in Production (MAP)

- **Auteurs / Émetteur** : Melissa Z. Pan, Negar Arabzadeh, Riccardo Cogo, Yuxuan Zhu et al. (2025, 2025-12-02)
- **Revue / Organisme / Dépôt** : arXiv (UC Berkeley) — Identifiant : `arXiv:2512.04123`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.04123
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-027.txt` (22684 mots, 160353 octets)
- **Empreinte SHA-256** : `3f8f34adaeb523b3cdc740f8df9d4c97b621f9ac7f955c10d94e3fbc97dcc2e1`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Étude mixte terrain (20 études de cas et enquête sur 306 répondants / 86 systèmes) | Axes : `RQ2, RQ6`
- **Synthèse factuelle** : L'étude Measuring Agents in Production (MAP) de Pan et al. documente comment les praticiens conçoivent réellement les agents en exploitation à travers 20 entrevues approfondies et 306 réponses d'enquête couvrant 26 domaines (86 praticiens en production). Contre le mythe de l'autonomie ouverte, 68 % des systèmes déployés exécutent au plus 10 étapes avant intervention humaine, 80 % des études de cas (16 sur 20) utilisent des flux de travail structurés fixes, 70 % conservent des modèles commerciaux sans réentraînement des poids et 79 % rédigent les invites manuellement. Les organisations sacrifient délibérément l'autonomie ouverte au profit de la prévisibilité et de la maîtrise du risque.

### [8] SRC-028 — Why Do Multi-Agent LLM Systems Fail? (MAST)

- **Auteurs / Émetteur** : Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal et al. (2025, 2025-03-17)
- **Revue / Organisme / Dépôt** : NeurIPS 2025 / arXiv — Identifiant : `arXiv:2503.13657`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.13657
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-028.txt` (19765 mots, 136729 octets)
- **Empreinte SHA-256** : `7eeb1c6dfd098f1f6507ab979bdae4a7a2eacc1888efc0d599aca663f6577933`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Taxonomie empirique et jeu de données annoté (NeurIPS 2025 / MAST-Data) | Axes : `RQ2`
- **Synthèse factuelle** : Cemri et al. analysent plus de 1 600 traces (1 642 traces dans MAST-Data) issues de sept cadriciels multi-agents open source populaires (dont AutoGen, CrewAI, ChatDev, MetaGPT et Manus) et construisent la taxonomie MAST à 14 modes de défaillance regroupés en 3 catégories : conception système, désalignement inter-agents et vérification/terminaison. Les taux d'échec observés sur les systèmes évalués varient de 41 % à 86,7 %, mettant en évidence que la plupart des défaillances proviennent de la coordination, de l'oubli de spécifications ou d'absences de garde-fous de vérification plutôt que des capacités intrinsèques du LLM. Ces mesures fondent l'exigence de tests structurels et de contrôle déterministe.

### [9] SRC-031 — Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

- **Auteurs / Émetteur** : Dat Tran, Douwe Kiela (2026, 2026-04-02)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2604.02460`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2604.02460
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-031.txt` (11295 mots, 74996 octets)
- **Empreinte SHA-256** : `80b064f92eb145f5ff0977ee03fb95543bb95599007e69ded99c08927edac0e9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Analyse théorique et expérimentale à budget de calcul constant (Stanford) | Axes : `RQ2`
- **Synthèse factuelle** : Tran et Kiela établissent, à partir de l'inégalité de traitement des données, qu'à budget égal de jetons de raisonnement et sous utilisation efficace du contexte, un agent unique est théoriquement plus efficace en information qu'un système multi-agents sur le raisonnement à sauts multiples. Leurs expériences montrent que les gains publiés en faveur des systèmes multi-agents proviennent souvent d'un biais de confusion lié à l'augmentation cachée du calcul en phase d'inférence. Lorsque le budget est normalisé, l'agent unique égale ou surpasse la plupart des architectures multi-agents, ces dernières ne redevenant compétitives que lorsque le contexte individuel sature.

### [10] SRC-032 — The Ringelmann Effect in Multi-Agent LLM Systems: A Scaling Law for Effective Team Size

- **Auteurs / Émetteur** : Blaž Bertalanič, Carolina Fortuna (2026, 2026-05-31)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2606.02646`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2606.02646
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-032.txt` (20794 mots, 135378 octets)
- **Empreinte SHA-256** : `4fa498f378d078f8995d9071474601709754aef7ceb408149ee8bbeb2f146ae9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Modélisation mathématique et validation multi-modèles (Jozef Stefan Institute) | Axes : `RQ2, RQ6`
- **Synthèse factuelle** : Bertalanič et Fortuna transposent l'effet Ringelmann aux systèmes multi-agents et dérivent une loi d'échelle à deux paramètres mesurant la taille effective d'une équipe N_eff/N = 1/(1 + c(N−1)N^−β) à travers 44 cellules expérimentales. Leurs résultats montrent que dans de nombreuses configurations de débat et de vote majoritaire sur Qwen, Llama et autres familles ouvertes, N_eff plafonne rapidement près de 1,1 à 1,8 agent effectif même à N = 30 agents nominaux, tandis que les coûts en jetons explosent à plus de 64 000–101 000 jetons par question. L'article offre aux architectes un test pilote frugal pour décider si l'ajout d'agents reste économiquement rentable.

### [11] SRC-033 — Sagas

- **Auteurs / Émetteur** : Hector Garcia-Molina, Kenneth Salem (1987, 1987-05-01)
- **Revue / Organisme / Dépôt** : ACM SIGMOD 1987 (Princeton Dept. CS OA) — Identifiant : `ACM-SIGMOD-1987-SAGAS`
- **URL ouverte vérifiée** : https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-033.txt` (7817 mots, 46158 octets)
- **Empreinte SHA-256** : `61c64fc7900604a34fcae13f7907df581d97c48ff19ec0d7db579a3bd1bd332e`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Article fondateur d'informatique distribuée évalué par les pairs (ACM SIGMOD 1987) | Axes : `RQ3`
- **Synthèse factuelle** : Garcia-Molina et Salem introduisent le concept de « saga » pour traiter les transactions de longue durée (LLT) sans maintenir de verrous exclusifs bloquants sur les bases de données critiques. Une saga décompose une LLT en une séquence de transactions locales indépendantes T_1..T_n accompagnées chacune d'une transaction compensatoire C_i capable d'annuler sémantiquement son effet si une étape ultérieure échoue et doit revenir en arrière. Cette formalisation des garanties « tout ou compensation » sans verrouillage distribué demeure la pierre angulaire de l'orchestration d'agents reliés à des systèmes d'enregistrement patrimoniaux.

### [12] SRC-034 — Temporal SDKs — Durable Execution, Event History and Deterministic Replay

- **Auteurs / Émetteur** : Temporal Technologies (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : Temporal Documentation — Identifiant : `TEMPORAL-SDKS-2026`
- **URL ouverte vérifiée** : https://docs.temporal.io/encyclopedia/temporal-sdks
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-034.txt` (2327 mots, 15387 octets)
- **Empreinte SHA-256** : `95aa625eecff574cd1e55188823cb0b0e10a7c36a2f78b415913ca3bf1fcf35b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Documentation d'architecture d'exécution durable (Temporal Technologies) | Axes : `RQ3`
- **Synthèse factuelle** : Cette spécification architecturale des SDK Temporal décrit comment les workflows persistants enregistrent chaque étape, minuterie et réponse d'activité dans un journal d'événements immuable (Event History) géré par le service d'orchestration. En cas de redémarrage, d'expiration ou de panne de processus, le moteur rejoue le code déterministe du workflow en récupérant les résultats déjà mémorisés dans le journal sans réexécuter les effets de bord externes déjà validés. Ce modèle impose une frontière stricte entre la logique déterministe du workflow et les appels non déterministes (LLM, API externes) confinés dans des activités idempotentes.

### [13] SRC-035 — CloudEvents Specification — Version 1.0.2

- **Auteurs / Émetteur** : CNCF Serverless Working Group (2022, 2022-04-01)
- **Revue / Organisme / Dépôt** : Cloud Native Computing Foundation (CNCF) — Identifiant : `CLOUDEVENTS-1.0.2`
- **URL ouverte vérifiée** : https://raw.githubusercontent.com/cloudevents/spec/v1.0.2/cloudevents/spec.md
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-035.txt` (3651 mots, 25147 octets)
- **Empreinte SHA-256** : `8f4d59dd27f8807741321b3145c5c9c2f22bba5bf9a9299b0c2020d769dc92ae`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Spécification ouverte CNCF de format d'événement (CloudEvents v1.0.2) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : Publiée par le groupe Serverless de la Cloud Native Computing Foundation, la spécification CloudEvents v1.0.2 standardise une enveloppe neutre de métadonnées contextuelles (identifiant id, source, type, specversion, datacontenttype, heure) pour décrire les événements traversant des routeurs, bus de messages et systèmes de traçage hétérogènes. Cette séparation nette entre attributs de contexte routables par les intermédiaires et charge utile métier facilite la mise en place de files d'attente, de journaux de reprise et de politiques de sécurité indépendantes du protocole de transport. Elle appuie l'orchestration événementielle et les canaux de compensation dédiés aux chapitres 3 et 4.

### [14] SRC-036 — The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header)

- **Auteurs / Émetteur** : Sanjay Dalal, Jae-Hoon Lee (IETF HTTPAPI WG) (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : IETF Datatracker — Identifiant : `IETF-DRAFT-IDEMPOTENCY-KEY`
- **URL ouverte vérifiée** : https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-036.txt` (3668 mots, 24607 octets)
- **Empreinte SHA-256** : `d737453f458f71e135b6bee31e4bdda076f6bca90f264add649fd738b75714cb`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Spécification technique en cours de normalisation IETF (HTTPAPI WG) | Axes : `RQ3`
- **Synthèse factuelle** : Le brouillon normatif de l'IETF HTTPAPI définit l'en-tête HTTP « Idempotency-Key » destiné à rendre les méthodes mutantes non idempotentes telles que POST et PATCH tolérantes aux pannes et aux réessais réseau. Il formalise les obligations du client (unicité et durée de validité de la clé) et celles de la ressource (calcul d'empreinte de requête, détection de conflit en cas de réutilisation avec une charge utile différente et restitution déterministe de la réponse mise en cache). En orchestration agentique, ce mécanisme empêche qu'un agent relancé après délai d'attente ne déclenche deux paiements ou écritures comptables.
