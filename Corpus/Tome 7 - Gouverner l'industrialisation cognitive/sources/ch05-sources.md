# Dossier fermé de sources L+ — Chapitre 05 — Connecter sans s'enfermer : protocoles ouverts, dette sémantique et patrimoine

- **Unité du livre** : `ch05` (`sources/ch05-sources.md`)
- **Axes de recherche couverts** : `RQ2, RQ3`
- **Date de gel des faits** : 2 décembre 2026
- **Protocole** : `MLR-PRISMA-SCR-LIVRE-2027-V1.2` (`metadata_only_pct = 0.0 %`, règle stricte `AO-01` sans contournement)
- **Nombre de sources probantes incluses** : 15 sources intégrales `L+`

> Ce dossier fermé recense exclusivement les sources primaires et travaux ouverts dont le texte intégral UTF-8 a été extrait, conservé sous `recherche/corpus_l_plus/` et authentifié par empreinte `SHA-256`. Aucune source en `statut F` ni copie locale non ouverte n'entre dans l'argumentation probante.

---

### [1] SRC-004 — The Coasean Singularity? Demand, Supply, and Market Design with AI Agents

- **Auteurs / Émetteur** : Peyman Shahidi, Gili Rusak, Benjamin S. Manning, Andrey Fradkin, John J. Horton (2025, 2025-11)
- **Revue / Organisme / Dépôt** : NBER Working Paper 34468 — Identifiant : `NBER-w34468`
- **URL ouverte vérifiée** : https://www.nber.org/system/files/working_papers/w34468/w34468.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-004.txt` (9028 mots, 64339 octets)
- **Empreinte SHA-256** : `45b9200d9e59c5eff7cb6ee35688c38f65ee372e0d547be0596409c1b2810292`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Document de travail économique (NBER Working Paper 34468) | Axes : `RQ1`
- **Synthèse factuelle** : Shahidi, Rusak, Manning, Fradkin et Horton examinent l'effet des agents IA sur les marchés numériques à travers le prisme coasien de l'effondrement des coûts de recherche, de négociation et de vérification. Du côté de la demande, les utilisateurs arbitrent entre qualité décisionnelle et réduction d'effort selon le contexte et la capacité de l'agent. Du côté de l'offre, les plateformes arbitrent entre intégration verticale fermée et interopérabilité ouverte entre domaines, ce qui conditionne l'allocation de la valeur économique. Ce papier remplace en L+ les éditions commerciales bloquées de la théorie des coûts de transaction pour ancrer la réflexion sur les frontières de la firme.

### [2] SRC-006 — SagaLLM: Context Management, Validation, and Transaction Guarantees for Multi-Agent LLM Planning

- **Auteurs / Émetteur** : Edward Y. Chang, Longling Geng (2025, 2025-07-09)
- **Revue / Organisme / Dépôt** : arXiv (prépublication, gabarit PVLDB) — Identifiant : `arXiv:2503.11951v3`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.11951
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-006.txt` (9679 mots, 73051 octets)
- **Empreinte SHA-256** : `c2565e8391cc57e98ad4c7f26cac6b52dd76360de5a461152d2a94765e64e694`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (prépublication arXiv sous gabarit PVLDB non finalisé) | Score AACODS : `10.5/12` | Devis : Architecture transactionnelle et validation expérimentale (SagaLLM) | Axes : `RQ3`
- **Synthèse factuelle** : Chang et Geng documentent quatre défauts structurels des planificateurs multi-agents à base de LLM : l'auto-validation peu fiable, la perte de contexte sur horizons longs, l'absence de garanties transactionnelles et la coordination fragile entre agents distribués. Pour y remédier, SagaLLM adapte le patron des sagas compensatoires de Garcia-Molina en combinant mémoire persistante externe, validation indépendante par des agents tiers et journalisation explicite des états avant et après chaque action. L'architecture permet d'annuler ou de compenser les effets partiels d'un flux distribué lorsqu'une contrainte aval échoue sans immobiliser les ressources par verrou distribué ACID. Elle forme la référence directe de l'ouvrage pour les sagas à point pivot et l'exécution durable.

### [3] SRC-007 — Defeating Prompt Injections by Design (CaMeL)

- **Auteurs / Émetteur** : Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes et al. (2025, 2025-06-24)
- **Revue / Organisme / Dépôt** : arXiv (prépublication) — Identifiant : `arXiv:2503.18813v2`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2503.18813
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-007.txt` (50342 mots, 361916 octets)
- **Empreinte SHA-256** : `7a9735abcbdcbea1569be50b290f7e8198648a57f378a27bdb796e0f38cb3d2b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (prépublication arXiv v2) | Score AACODS : `11.5/12` | Devis : Système d'exécution sécurisé et évaluation sur banc AgentDojo (prépublication arXiv) | Axes : `RQ5`
- **Synthèse factuelle** : Debenedetti et al. présentent CaMeL, une couche système de sécurité inspirée des langages à capacités et du patron Dual-LLM qui isole par construction le graphe d'appels d'outils du traitement de données externes non fiables. Un modèle planificateur traduit la requête approuvée en un sous-ensemble restreint de Python dont l'arbre syntaxique est interprété sous politiques de flux de données et de capacités, tandis qu'un modèle confiné sans accès aux outils privilégiés résume les données brutes. Sur le banc AgentDojo, CaMeL résout 77 % des tâches avec une garantie structurelle contre l'injection de consignes indirecte, contre 84 % pour un agent sans défense. Cette source valide l'arbitrage sécurité-utilité et le principe de séparation contrôle-données en ingénierie.

### [4] SRC-026 — Cognitive Architectures for Language Agents (CoALA)

- **Auteurs / Émetteur** : Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, Thomas L. Griffiths (2024, 2024-03-15)
- **Revue / Organisme / Dépôt** : TMLR / arXiv — Identifiant : `arXiv:2309.02427`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2309.02427
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-026.txt` (18434 mots, 123231 octets)
- **Empreinte SHA-256** : `831e99a3f99a9f1e2cdc1c2940b3a2046ca2973226130c16ebf5d58b2acb3dde`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Article de synthèse architecturale évalué par les pairs (TMLR 2024) | Axes : `RQ2, RQ3`
- **Synthèse factuelle** : Sumers, Yao, Narasimhan et Griffiths transposent les sciences cognitives et les architectures symboliques classiques (SOAR, ACT-R) dans le cadre CoALA (Cognitive Architectures for Language Agents). Ils structurent tout agent autour d'une boucle décisionnelle itérative reliant une mémoire de travail et trois mémoires à long terme (épisodique, sémantique et procédurale) à un espace d'actions internes et d'appels d'outils externes. CoALA montre que le modèle de langage n'est qu'un composant statistique au sein d'un programme de flux de contrôle explicite, appuyant la séparation architecturale entre noyau déterministe et inférence.

### [5] SRC-033 — Sagas

- **Auteurs / Émetteur** : Hector Garcia-Molina, Kenneth Salem (1987, 1987-05)
- **Revue / Organisme / Dépôt** : ACM SIGMOD 1987 (Princeton Dept. CS OA) — Identifiant : `ACM-SIGMOD-1987-SAGAS`
- **URL ouverte vérifiée** : https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-033.txt` (7817 mots, 46158 octets)
- **Empreinte SHA-256** : `61c64fc7900604a34fcae13f7907df581d97c48ff19ec0d7db579a3bd1bd332e`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Article fondateur d'informatique distribuée évalué par les pairs (ACM SIGMOD 1987) | Axes : `RQ3`
- **Synthèse factuelle** : Garcia-Molina et Salem introduisent le concept de « saga » pour traiter les transactions de longue durée (LLT) sans maintenir de verrous exclusifs bloquants sur les bases de données critiques. Une saga décompose une LLT en une séquence de transactions locales indépendantes T_1..T_n dotées de transactions compensatoires C_1..C_{n-1} capables d'annuler sémantiquement l'effet des étapes achevées si une étape ultérieure échoue et impose une reprise arrière. Cette formalisation des garanties « tout ou compensation » sans verrouillage distribué demeure la pierre angulaire de l'orchestration d'agents reliés à des systèmes d'enregistrement patrimoniaux.

### [6] SRC-036 — The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header)

- **Auteurs / Émetteur** : Jayadeba Jena, Sanjay Dalal, Dmitrii Tishkin (IETF HTTPAPI WG) (2026, 2026-11-21)
- **Revue / Organisme / Dépôt** : IETF Datatracker — Identifiant : `IETF-DRAFT-IDEMPOTENCY-KEY-09`
- **URL ouverte vérifiée** : https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-036.txt` (3668 mots, 24607 octets)
- **Empreinte SHA-256** : `d737453f458f71e135b6bee31e4bdda076f6bca90f264add649fd738b75714cb`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Spécification technique en cours de normalisation IETF (HTTPAPI WG, version -09) | Axes : `RQ3`
- **Synthèse factuelle** : Le brouillon normatif de l'IETF HTTPAPI (version -09) définit l'en-tête HTTP « Idempotency-Key » destiné à rendre les méthodes mutantes non idempotentes telles que POST et PATCH tolérantes aux pannes et aux réessais réseau. Il recommande côté client l'emploi d'un UUID ou d'une chaîne aléatoire imprévisible avec durée de validité documentée, et décrit côté ressource la construction d'une clé composite de cache ainsi que le calcul d'une empreinte de charge utile afin de rejeter en HTTP 422 (SHOULD) les divergences et en HTTP 409 (SHOULD) les requêtes concurrentes en cours.

### [7] SRC-038 — Model Context Protocol (MCP) Specification — Revision 2025-11-25 (corpus normatif complet)

- **Auteurs / Émetteur** : Model Context Protocol Maintainers (2025, 2025-11-25)
- **Revue / Organisme / Dépôt** : Model Context Protocol (GitHub modelcontextprotocol/modelcontextprotocol — spec 2025-11-25) — Identifiant : `MCP-SPEC-2025-11-25`
- **URL ouverte vérifiée** : https://github.com/modelcontextprotocol/modelcontextprotocol/tree/main/docs/specification/2025-11-25
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-038.txt` (62231 mots, 757889 octets)
- **Empreinte SHA-256** : `938fca60c06c92e10cd6448f31d90fbb81d03adcb1952a21915d219f685e96a9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Corpus normatif complet de connectivité ouverte (MCP 2025-11-25) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : Le corpus normatif complet du Model Context Protocol (révision du 25 novembre 2025) définit un protocole standardisé fondé sur JSON-RPC 2.0 inspiré du Language Server Protocol pour relier hôtes LLM, clients connecteurs et serveurs exposant outils, ressources et gabarits. Il spécifie l'architecture, les transports, l'autorisation OAuth, les tâches et les meilleures pratiques de sécurité, en avertissant que les outils constituent des vecteurs d'exécution arbitraire, que leurs descriptions demeurent non fiables sans serveur approuvé et que le protocole ne garantit pas seul le consentement ni le contrôle d'accès.

### [8] SRC-039 — Agent2Agent (A2A) Protocol Specification

- **Auteurs / Émetteur** : Linux Foundation / A2A Project (2026, 2026-05-28)
- **Revue / Organisme / Dépôt** : a2a-protocol.org (release v1.0.1) — Identifiant : `A2A-SPEC-2026`
- **URL ouverte vérifiée** : https://a2a-protocol.org/latest/specification/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-039.txt` (24333 mots, 179807 octets)
- **Empreinte SHA-256** : `fb9823ce13380143b0509c404cc5098c945ba2ec21f0dda779ddf90f4a351727`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Spécification ouverte d'interopérabilité inter-agents (Linux Foundation A2A) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : La spécification Agent2Agent (A2A) propose une architecture à trois couches — modèle de données canonique, opérations abstraites et liaisons protocolaires JSON-RPC, gRPC et HTTP/REST — permettant à des agents opaques de domaines ou d'organisations distincts de se découvrir et de collaborer sur des tâches asynchrones de longue durée. Le protocole encadre la découverte par Agent Cards, les flux multi-tours, l'architecture d'extensions typées et la sécurité multi-locataires. A2A représente dans l'ouvrage le protocole horizontal complémentaire de MCP pour les échanges inter-entreprises.

### [9] SRC-040 — From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI

- **Auteurs / Émetteur** : Margaret-Anne Storey (2026, 2026-03-23)
- **Revue / Organisme / Dépôt** : arXiv (University of Victoria) — Identifiant : `arXiv:2603.22106`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2603.22106
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-040.txt` (4902 mots, 32784 octets)
- **Empreinte SHA-256** : `ea4b2e2a02be74d9ea58c479f65fd32ca0dd95a60fab65538792e41a844dd052`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Analyse conceptuelle en génie logiciel (Université de Victoria, arXiv 2026) | Axes : `RQ3, RQ6`
- **Synthèse factuelle** : Margaret-Anne Storey montre que l'accélération fulgurante du codage assisté par IA générative déplace la dette technique classique vers deux passifs plus insidieux : la dette cognitive (perte de compréhension partagée par les équipes du fonctionnement du logiciel produit) et la dette d'intention (oubli des hypothèses métier et contraintes pour lesquelles le système a été conçu). Même lorsque les tests unitaires réussissent, les équipes deviennent incapables de faire évoluer ou de corriger le code en toute confiance face à des effets de bord inattendus. Cette thèse éclaire l'érosion de la maîtrise d'ouvrage technologique aux chapitres 3, 4, 5, 11 et 12.

### [10] SRC-042 — RFC 9396: OAuth 2.0 Rich Authorization Requests (RAR)

- **Auteurs / Émetteur** : Torsten Lodderstedt, Justin Richer, Brian Campbell (2023, 2023-05)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9396`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9396.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-042.txt` (7380 mots, 55352 octets)
- **Empreinte SHA-256** : `e334d06f14081317caf9d457dcbffeae877c5e5009f2452d2f11adcd47d68f6b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9396, évalué par les pairs) | Axes : `RQ4`
- **Synthèse factuelle** : La RFC 9396 introduit le paramètre JSON « authorization_details » dans les requêtes et réponses de jetons OAuth 2.0 afin de décrire des autorisations granulaires fortement typées (montants plafonnés, comptes bénéficiaires, actions précises) là où les simples chaînes « scope » restent trop grossières. Elle précise la validation sémantique entre client, serveur d'autorisation et serveur de ressources ainsi que l'usage de schémas lisibles par machine. Appliqué aux agents financiers, RAR contraint cryptographiquement chaque appel d'outil au mandat exact approuvé par le client ou la politique.

### [11] SRC-054 — NIST AI 100-2e2025: Adversarial Machine Learning — A Taxonomy and Terminology of Attacks and Mitigations

- **Auteurs / Émetteur** : Alina Oprea, Apostol Vassilev et al. (NIST) (2025, 2025-03-20)
- **Revue / Organisme / Dépôt** : NIST — Identifiant : `NIST-AI-100-2E2025`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-054.txt` (48743 mots, 347771 octets)
- **Empreinte SHA-256** : `1f113bf38b90261c6372c5b9a8d77a4355c7e4fa0ccf11b4d179930a9a0dfa7f`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Taxonomie normative officielle (NIST AI 100-2e2025) | Axes : `RQ5`
- **Synthèse factuelle** : Ce rapport du NIST établit une taxonomie et une terminologie de référence en apprentissage automatique antagoniste (Adversarial Machine Learning) couvrant aussi bien l'IA prédictive que l'IA générative. Il classe systématiquement les attaques selon le stade du cycle de vie, les objectifs (compromission d'intégrité, disponibilité, vie privée), les capacités et la connaissance de l'attaquant, puis associe les mesures d'atténuation disponibles et leurs limites persistantes. Ce cadre permet aux chapitres 5, 8 et 9 de distinguer empoisonnement, évasion et détournement de contexte.

### [12] SRC-056 — Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks

- **Auteurs / Émetteur** : James Peters-Gill, Avi Semler, Henning Bartsch, Ilia Shumailov et al. (2026, 2026-10-05)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2610.05640`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2610.05640
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-056.txt` (14394 mots, 97586 octets)
- **Empreinte SHA-256** : `490ff7dc6d6914d59acfb56fab33ebb48ae61dd5ef1bfd181cb69d04c68ee9f5`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Évaluation cryptographique/sécuritaire multi-agents (Oxford / MATS, arXiv 2026) | Axes : `RQ5`
- **Synthèse factuelle** : Peters-Gill, Semler, Bartsch, Shumailov et Schroeder de Witt testent la composabilité des garanties de sécurité de CaMeL lorsque plusieurs agents équipés chacun de CaMeL s'invoquent mutuellement comme outils dans une architecture hiérarchique. Leurs résultats montrent de manière critique que les garanties de CaMeL ne se composent pas automatiquement d'un agent à l'autre : une attaque concrète par injection indirecte réussit en exploitant la réinterprétation de données non fiables transitant entre sous-agents privilégiés et planificateurs. Cette limite démontre l'importance de la « règle du maillon le plus élevé » et du confinement aux frontières inter-agents.

### [13] SRC-057 — Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem

- **Auteurs / Émetteur** : Obada Kraishan (2026, 2026-09-15)
- **Revue / Organisme / Dépôt** : arXiv — Identifiant : `arXiv:2609.14119`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2609.14119
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-057.txt` (7412 mots, 49308 octets)
- **Empreinte SHA-256** : `cae21acac54fea61a6270540a888a090731fac9d0de3ae0f121f3d51d59ed7e9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Recensement empirique de sécurité sur registre public (21 643 serveurs MCP, 2026) | Axes : `RQ5`
- **Synthèse factuelle** : Kraishan réalise en août–septembre 2026 le premier recensement complet du registre public MCP en collectant 21 643 serveurs (72 606 versions) et en analysant le code source de 14 353 d'entre eux à l'aide d'un analyseur à huit classes de menaces calibré sur 414 cas vérifiés manuellement. L'étude observe une prévalence élevée d'exposition réseau sans authentification (9,57 % des serveurs analysés) ainsi que des phénomènes de « dérive silencieuse » où un même nom de serveur change discrètement de comportement ou d'implémentation. Ce constat empirique justifie les sas d'assainissement et le registre d'outils signé aux chapitres 4, 8 et 9.

### [14] SRC-063 — Loi modernisant des dispositions législatives en matière de protection des renseignements personnels (Loi 25 / LQ 2021, c. 25, art. 12.1)

- **Auteurs / Émetteur** : Assemblée nationale du Québec (2021, 2021-09-22)
- **Revue / Organisme / Dépôt** : Publications du Québec — Identifiant : `LQ-2021-C25`
- **URL ouverte vérifiée** : https://www.publicationsduquebec.gouv.qc.ca/fileadmin/Fichiers_client/lois_et_reglements/LoisAnnuelles/fr/2021/2021C25F.PDF
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-063.txt` (21658 mots, 143588 octets)
- **Empreinte SHA-256** : `829e67f777ca0645b5b51a2ec4d8ec94739232c5a33ef76b7944d2bb81b61d87`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Texte législatif officiel sanctionné du Québec (Loi 25 / LQ 2021, c. 25) | Axes : `RQ6`
- **Synthèse factuelle** : La Loi modernisant des dispositions législatives en matière de protection des renseignements personnels (LQ 2021, c. 25, sanctionnée le 22 septembre 2021) insère l'article 12.1 dans la Loi sur le privé — entré en vigueur le 22 septembre 2023 (art. 175), tandis que le droit à la portabilité a pris effet le 22 septembre 2024 — encadrant toute décision rendue fondée exclusivement sur un traitement automatisé (information, communication sur demande des renseignements, facteurs et paramètres utilisés, correction et droit de présenter ses observations devant un membre du personnel). Elle instaure des sanctions administratives pécuniaires pouvant atteindre 10 000 000 \$ CA ou 2 % du chiffre d'affaires mondial (art. 90.12) et des amendes pénales allant jusqu'à 25 000 000 \$ CA ou 4 % du chiffre d'affaires mondial (art. 91). Ce texte sanctionné fournit la preuve L+ face au blocage de LégisQuébec (RLRQ, c. P-39.1, statut F).

### [15] SRC-035 — CloudEvents Specification — Version 1.0.2

- **Auteurs / Émetteur** : CNCF Serverless Working Group (2022, 2022-04)
- **Revue / Organisme / Dépôt** : Cloud Native Computing Foundation (CNCF) — Identifiant : `CLOUDEVENTS-1.0.2`
- **URL ouverte vérifiée** : https://raw.githubusercontent.com/cloudevents/spec/v1.0.2/cloudevents/spec.md
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-035.txt` (3651 mots, 25147 octets)
- **Empreinte SHA-256** : `8f4d59dd27f8807741321b3145c5c9c2f22bba5bf9a9299b0c2020d769dc92ae`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Spécification ouverte CNCF de format d'événement (CloudEvents v1.0.2) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : Publiée par le groupe Serverless de la Cloud Native Computing Foundation, la spécification CloudEvents v1.0.2 standardise une enveloppe neutre de métadonnées contextuelles (identifiant id, source, type, specversion, datacontenttype, heure) pour décrire les événements traversant des routeurs, bus de messages et systèmes de traçage hétérogènes. Cette séparation nette entre attributs de contexte routables par les intermédiaires et charge utile métier facilite la mise en place de files d'attente, de journaux de reprise et de politiques de sécurité indépendantes du protocole de transport. Elle appuie l'orchestration événementielle et les canaux de compensation dédiés dans l'architecture et la gouvernance de l'ouvrage.
