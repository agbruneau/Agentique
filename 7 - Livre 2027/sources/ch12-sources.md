# Dossier fermé de sources L+ — Chapitre 12 — Décider sous incertitude profonde : des 90 premiers jours à l'ère post-quantique

- **Unité du livre** : `ch12` (`sources/ch12-sources.md`)
- **Axes de recherche couverts** : `RQ4, RQ6`
- **Date de gel des faits** : 31 décembre 2026
- **Protocole** : `MLR-PRISMA-SCR-LIVRE-2027-V1.2` (`metadata_only_pct = 0.0 %`, règle stricte `AO-01` sans contournement)
- **Nombre de sources probantes incluses** : 18 sources intégrales `L+`

> Ce dossier fermé recense exclusivement les sources primaires et travaux ouverts dont le texte intégral UTF-8 a été extrait, conservé sous `recherche/corpus_l_plus/` et authentifié par empreinte `SHA-256`. Aucune source en `statut F` ni copie locale non ouverte n'entre dans l'argumentation probante.

Note AO-01 (statut F) : `lautorite.qc.ca` demeure en statut F (HTTP 403 WAF), explicitement signalé avec la trace secondaire ouverte `SRC-071` en complément des textes fédéraux L+ (`BSIF E-23`, `B-15`, `OSC NI 31-103`, `Loi sur les banques`).

---

### [1] SRC-008 — Artificial Intelligence Index Report 2026

- **Auteurs / Émetteur** : Sha Sajadieh, Loredana Fattorini, Raymond Perrault, Yolanda Gil et al. (2026, 2026-04-14)
- **Revue / Organisme / Dépôt** : Stanford HAI / arXiv — Identifiant : `arXiv:2606.15708`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2606.15708
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-008.txt` (132584 mots, 880133 octets)
- **Empreinte SHA-256** : `11f49f977f4ddb87ba28743c0f4edb3b6e2a440be766df60207661655de38363`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Rapport statistique et bibliométrique annuel (Stanford HAI 2026) | Axes : `RQ1, RQ6`
- **Synthèse factuelle** : L'édition 2026 de l'AI Index Report de Stanford HAI compile les tendances mondiales de recherche, de performance technique, d'économie du travail et de réglementation de l'IA. Dans son analyse économique des métiers exposés, le rapport montre qu'aux États-Unis l'emploi des développeurs logiciels âgés de 22 à 25 ans a reculé de près de 20 % depuis 2024, alors que les effectifs des développeurs plus expérimentés poursuivent leur croissance. Il documente également l'expansion continue du volume de publications scientifiques (environ 258 000 articles en 2024, soit 40,9 % de la recherche informatique dans OpenAlex) et l'accélération des investissements d'infrastructure. Ce jeu de données sert de repère quantitatif principal pour la crise de l'apprentissage junior et la gouvernance des compétences.

### [2] SRC-040 — From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI

- **Auteurs / Émetteur** : Margaret-Anne Storey (2026, 2026-03-23)
- **Revue / Organisme / Dépôt** : arXiv (University of Victoria) — Identifiant : `arXiv:2603.22106`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2603.22106
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-040.txt` (4902 mots, 32784 octets)
- **Empreinte SHA-256** : `ea4b2e2a02be74d9ea58c479f65fd32ca0dd95a60fab65538792e41a844dd052`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Analyse conceptuelle en génie logiciel (Université de Victoria, arXiv 2026) | Axes : `RQ3, RQ6`
- **Synthèse factuelle** : Margaret-Anne Storey montre que l'accélération fulgurante du codage assisté par IA générative déplace la dette technique classique vers deux passifs plus insidieux : la dette cognitive (perte de compréhension partagée par les équipes du fonctionnement du logiciel produit) et la dette d'intention (oubli des hypothèses métier et contraintes pour lesquelles le système a été conçu). Même lorsque les tests unitaires réussissent, les équipes deviennent incapables de faire évoluer ou de corriger le code en toute confiance face à des effets de bord inattendus. Cette thèse éclaire l'érosion de la maîtrise d'ouvrage technologique aux chapitres 3, 5, 11 et 12.

### [3] SRC-044 — RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT)

- **Auteurs / Émetteur** : Henk Birkholz, Antoine Delignat-Lavaud, Cedric Fournet, Yogesh Deshpande, Steve Lasker (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9943`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9943.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-044.txt` (9450 mots, 65476 octets)
- **Empreinte SHA-256** : `3ae677b4a295a3ee3eb793d39daf3d2a1139b041ff019fc5317bfe24a3fa3ae6`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9943, juin 2026) | Axes : `RQ4, RQ5`
- **Synthèse factuelle** : La RFC 9943 normalise l'architecture SCITT (Supply Chain Integrity, Transparency, and Trust) pour l'enregistrement et l'audit d'énoncés signés par un émetteur unique dans des journaux transparents fondés sur des structures de données vérifiables (arbres de Merkle anti-équivocation). Elle permet à toute partie vérifiante d'obtenir la preuve cryptographique qu'un manifeste logiciel, une attestation de modèle ou un serveur d'outils a bien été enregistré et validé à un instant donné. SCITT offre une réponse normalisée aux attaques sur la chaîne d'approvisionnement d'outils agentiques et aux exigences de traçabilité d'audit.

### [4] SRC-049 — NIST FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM)

- **Auteurs / Émetteur** : National Institute of Standards and Technology (NIST) (2024, 2024-08-13)
- **Revue / Organisme / Dépôt** : NIST Computer Security Resource Center — Identifiant : `NIST-FIPS-203`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-049.txt` (19224 mots, 125529 octets)
- **Empreinte SHA-256** : `bb840af1e6a3e1df10862cf3a8f26e435cbdc7502248a809ba1caba205a3574c`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Norme fédérale cryptographique officielle (NIST FIPS 203, août 2024) | Axes : `RQ4`
- **Synthèse factuelle** : La norme NIST FIPS 203 formalise le mécanisme d'encapsulation de clés post-quantique ML-KEM (issu de CRYSTALS-Kyber), dont la sûreté repose sur la difficulté du problème Module Learning with Errors face à un adversaire quantique. Elle définit trois jeux de paramètres selon les catégories de sécurité et régit la génération de clés, l'encapsulation et la décapsulation pour établir des clés symétriques partagées sur canaux publics. Dans le chapitre 7 et le chapitre 12, FIPS 203 fonde l'échange de clés hybride ou post-quantique pour contrer la menace « capter maintenant, déchiffrer plus tard ».

### [5] SRC-050 — NIST FIPS 204: Module-Lattice-Based Digital Signature Standard (ML-DSA)

- **Auteurs / Émetteur** : National Institute of Standards and Technology (NIST) (2024, 2024-08-13)
- **Revue / Organisme / Dépôt** : NIST Computer Security Resource Center — Identifiant : `NIST-FIPS-204`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-050.txt` (25028 mots, 150660 octets)
- **Empreinte SHA-256** : `14b6c1706d2c4a1645a7c285e37e9e7e33dd98348302c84c11db9613c0f1d267`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Norme fédérale cryptographique officielle (NIST FIPS 204, août 2024) | Axes : `RQ4`
- **Synthèse factuelle** : La norme NIST FIPS 204 normalise l'algorithme de signature numérique post-quantique sur réseaux euclidiens ML-DSA (issu de CRYSTALS-Dilithium) pour garantir l'authenticité, l'intégrité et la non-répudiation des données signées face aux ordinateurs quantiques à grande échelle. Le tableau officiel des tailles de clés et de signatures (p. 16) établit exactement 3 309 octets pour ML-DSA-65 et 4 627 octets pour ML-DSA-87 (contre 2 420 octets pour ML-DSA-44 et 64 octets pour une signature elliptique ECDSA/Ed25519 classique). Ces facteurs d'expansion (~52× et ~72×) pèsent directement sur les en-têtes HTTP, les chaînes de jetons OAuth et la latence des passerelles agentiques.

### [6] SRC-051 — NIST IR 8547 (ipd): Transition to Post-Quantum Cryptography Standards

- **Auteurs / Émetteur** : Dustin Moody, Lily Chen, David Cooper, Quynh Dang et al. (NIST) (2024, 2024-11-12)
- **Revue / Organisme / Dépôt** : NIST — Identifiant : `NIST-IR-8547`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-051.txt` (9445 mots, 68680 octets)
- **Empreinte SHA-256** : `a58a28d341936c0ea456eb1b601930334323b8b9f87a017fafaaf991ef6c7cd6`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Rapport technique officiel NIST de transition (NIST IR 8547 ipd) | Axes : `RQ4`
- **Synthèse factuelle** : Le rapport NIST IR 8547 planifie la transition des algorithmes asymétriques vulnérables (RSA, ECDSA, EdDSA, ECDH) vers les normes post-quantiques FIPS 203, 204 et 205 tout en classant les cinq catégories de sécurité post-quantique. Il recense les familles normalisées à abandonner ou à remplacer et sert de guide technique de synchronisation pour les organismes de normalisation et les industries critiques. Note documentaire vérifiée dans le document : le brouillon initial ipd de novembre 2024 analysé ici porte un avis d'actualisation mentionnant la parution de la version finale en octobre 2026 (tous deux antérieurs au gel du 31 décembre 2026).

### [7] SRC-052 — Advancing a Coordinated Roadmap for the Transition to Post-Quantum Cryptography in the Financial Sector

- **Auteurs / Émetteur** : G7 Cyber Expert Group (CEG) (2026, 2026-01-14)
- **Revue / Organisme / Dépôt** : G7 Cyber Expert Group / UK HM Treasury & Bank of England — Identifiant : `G7-CEG-PQC-ROADMAP-2026`
- **URL ouverte vérifiée** : https://assets.publishing.service.gov.uk/media/6966149d8d599f4c09e1ffab/G7-CEG-Quantum-Roadmap.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-052.txt` (2175 mots, 16420 octets)
- **Empreinte SHA-256** : `cab48e350b2941891ec38ed7545d2b276b5815804d690187650c232424c945e3`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Feuille de route multilatérale officielle (G7 Cyber Expert Group, janv. 2026) | Axes : `RQ4, RQ6`
- **Synthèse factuelle** : Publiée en janvier 2026 par le G7 Cyber Expert Group, cette feuille de route coordonnée non contraignante conseille les ministères des Finances, banques centrales et institutions financières sur la migration vers la cryptographie résistante au quantique et l'agilité cryptographique. Le document relève que les orientations des juridictions pointent vers 2035 comme horizon cible global tout en recommandant une approche duale fondée sur les risques priorisant les systèmes critiques dans la fenêtre indicative 2030–2032. Il insiste sur la gouvernance de la direction, la cartographie des dépendances envers les fournisseurs tiers et le risque « capter maintenant, déchiffrer plus tard ».

### [8] SRC-053 — Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates (incl. Ballot SC-081v3)

- **Auteurs / Émetteur** : CA/Browser Forum Server Certificate Working Group (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : CA/Browser Forum — Identifiant : `CABF-BR-SC081V3`
- **URL ouverte vérifiée** : https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-053.txt` (47637 mots, 337172 octets)
- **Empreinte SHA-256** : `8d44ae9b57d6bc8b4bc90896c0edff9f2217d7e7468d3b19ac285454e31016c2`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Standard PKI public en vigueur (CA/Browser Forum BR v2.3.1, Ballot SC081) | Axes : `RQ4`
- **Synthèse factuelle** : Les Baseline Requirements v2.3.1 (4 octobre 2026) du CA/Browser Forum intègrent formellement le calendrier contraignant du Ballot SC081 réduisant par paliers la durée maximale de validité et de réutilisation des validations de certificats TLS publics. Après l'étape à 200 jours (15 mars 2026), la validité maximale et le réemploi des preuves de domaine/IP chutent à 100 jours le 15 mars 2027, puis à 47 jours (avec réutilisation limitée à 10 jours) le 15 mars 2029 (§ 4.2.1 et § 6.3.2). Ce resserrement impose l'automatisation intégrale ACME et la crypto-agilité sur toutes les passerelles d'agents exposées.

### [9] SRC-058 — STAMP/STPA Informed Characterization of Factors Leading to Loss of Control in AI Systems

- **Auteurs / Émetteur** : Steve Barrett, Anna Bruvere, Sean P. Fillingham, Catherine Rhodes (2025, 2025-12-19)
- **Revue / Organisme / Dépôt** : arXiv (Centre for the Study of Existential Risk) — Identifiant : `arXiv:2512.17600`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2512.17600
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-058.txt` (17212 mots, 112088 octets)
- **Empreinte SHA-256** : `78b03417f4de11b0132a9afce95e493bec8b9028715ec9b9139aa504d4599ecb`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Cadre d'analyse de sûreté système (Barrett et al., STAMP/STPA, déc. 2025) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Barrett, Bruvere, Fillingham, Rhodes et Vergani (Arcadia Impact / CSER / King's College London) appliquent la méthodologie d'ingénierie de la sûreté STAMP/STPA pour caractériser systématiquement les facteurs causaux menant à une perte de contrôle dans les systèmes sociotechniques intégrant l'IA. Plutôt que de traiter uniquement les défaillances isolées de composants, l'approche modélise les boucles de contrôle, les actions de contrôle dangereuses et les défauts de rétroaction entre concepteurs, opérateurs humains et composants autonomes. Elle fonde en L+ les analyses de boucles de contrainte et de gouvernance opérationnelle des chapitres 8, 9, 11 et 12.

### [10] SRC-060 — Règlement (UE) 2024/1689 (EU AI Act)

- **Auteurs / Émetteur** : Parlement européen et Conseil de l'Union européenne (2024, 2024-07-12)
- **Revue / Organisme / Dépôt** : Journal officiel de l'Union européenne — Identifiant : `CELEX:32024R1689`
- **URL ouverte vérifiée** : https://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0009.01/DOC_1
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-060.txt` (102754 mots, 711317 octets)
- **Empreinte SHA-256** : `e0a79e4f278c88177206c60458fad1f06c74fc80d6b23e404ef523c290346477`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Acte législatif européen officiel (Règlement UE 2024/1689, JOUE) | Axes : `RQ6`
- **Synthèse factuelle** : Le texte intégral français officiel du Règlement (UE) 2024/1689 (EU AI Act, adopté le 13 juin 2024 et publié le 12 juillet 2024) fixe le cadre harmonisé par niveaux de risque dans l'Union européenne. L'article 113 prévoit une application échelonnée incluant les pratiques interdites (février 2025), les obligations de transparence de l'article 50 et la date générale d'application du 2 août 2026, ainsi que les régimes des systèmes à haut risque des annexes III et I. Il sert de texte juridique socle avant prise en compte des ajustements calendaires adoptés en juillet 2026.

### [11] SRC-061 — Règlement (UE) 2026/1744 du 8 juillet 2026 modifiant le règlement (UE) 2024/1689 (simplification / échéances IA)

- **Auteurs / Émetteur** : Parlement européen et Conseil de l'Union européenne (2026, 2026-07-24)
- **Revue / Organisme / Dépôt** : Journal officiel de l'Union européenne (JO L 24.7.2026) — Identifiant : `CELEX:32026R1744`
- **URL ouverte vérifiée** : https://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0009.01/DOC_1
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-061.txt` (26235 mots, 175654 octets)
- **Empreinte SHA-256** : `cafaf35193ed2bdb4c97f5219deef5a6c9310aa5ceae48484d36485b3211d712`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Acte législatif européen officiel modificatif (Règlement UE 2026/1744, JOUE 24.7.2026) | Axes : `RQ6`
- **Synthèse factuelle** : Le Règlement (UE) 2026/1744 du 8 juillet 2026 (publié au JOUE le 24 juillet 2026, train de mesures omnibus numérique sur l'IA) modifie directement l'article 113 et l'article 111 du règlement (UE) 2024/1689 en raison des retards d'adoption des normes techniques harmonisées. En vertu du point c) révisé de l'article 113, les exigences des sections 1, 2 et 3 du chapitre III s'appliquent à partir du 2 décembre 2027 pour les systèmes à haut risque de l'annexe III et à partir du 2 août 2028 pour ceux de l'annexe I, tandis que les systèmes déjà mis sur le marché disposent jusqu'au 2 décembre 2026 pour les obligations visées à l'article 50, paragraphe 2. Cette vérification textuelle écarte toute ambiguïté sur le calendrier européen exact au gel de décembre 2026.

### [12] SRC-065 — Ligne directrice E-23 — Gestion du risque de modélisation à l'échelle de l'entreprise (édition 2027)

- **Auteurs / Émetteur** : Bureau du surintendant des institutions financières (BSIF / OSFI) (2025, 2025-09-11)
- **Revue / Organisme / Dépôt** : BSIF Canada — Identifiant : `BSIF-E23-2027`
- **URL ouverte vérifiée** : https://www.osfi-bsif.gc.ca/fr/consignes/repertoire-consignes/ligne-directrice-e-23-gestion-du-risque-modelisation-2027
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-065.txt` (7675 mots, 64813 octets)
- **Empreinte SHA-256** : `886e1d96170f5def8a72bc30a2d8d68ef49d2fc2728e79cf97b3d7dbedd19322`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Ligne directrice prudentielle fédérale officielle (BSIF E-23, édition 2027) | Axes : `RQ6`
- **Synthèse factuelle** : La ligne directrice E-23 révisée du Bureau du surintendant des institutions financières sur la gestion du risque de modélisation à l'échelle de l'entreprise affiche explicitement une date d'entrée en vigueur fixée « Le 1 mai 2027 ». Elle étend formellement le champ du risque de modélisation au-delà des modèles statistiques classiques pour englober les modèles d'intelligence artificielle et d'apprentissage automatique à travers tout leur cycle de vie (inventaire, validation indépendante, surveillance continue et gouvernance des compétences). Elle constitue l'ancre prudentielle canadienne structurante de la troisième et quatrième partie.

### [13] SRC-066 — Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security and Operational Risk

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2026, 2026-07-01)
- **Revue / Organisme / Dépôt** : OSFI Technology Risk Bulletin — Identifiant : `OSFI-BULLETIN-AGENTIC-2026`
- **URL ouverte vérifiée** : http://www.osfi-bsif.gc.ca/en/risks/technology-cyber-risk-management/technology-risk-bulletin/generative-agentic-artificial-intelligence-implications-technology-cyber-security-operational
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-066.txt` (4194 mots, 49330 octets)
- **Empreinte SHA-256** : `362c9639e348264a5fb303562725378b726185cd4d26914724182736c0c07d69`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Bulletin officiel de risque technologique et cyber (OSFI/BSIF, juillet 2026) | Axes : `RQ5, RQ6`
- **Synthèse factuelle** : Publié en juillet 2026, ce bulletin du BSIF analyse spécifiquement les risques technologiques, cybernétiques et opérationnels introduits par l'IA générative et l'IA agentique (définie par le raisonnement et l'exécution autonomes) dans les institutions financières fédérales. Le régulateur avertit que ces technologies élargissent les surfaces d'attaque, accélèrent la propagation des défaillances et mettent à l'épreuve les contrôles existants sous les lignes directrices B-13, B-10 et E-21. Il recommande une gouvernance renforcée de l'autonomie, une journalisation et surveillance accrues ainsi que des plans de continuité adaptés aux collectifs d'agents.

### [14] SRC-067 — Guideline B-15: Climate Risk Management

- **Auteurs / Émetteur** : Office of the Superintendent of Financial Institutions (OSFI / BSIF) (2025, 2025-03-07)
- **Revue / Organisme / Dépôt** : OSFI Canada — Identifiant : `OSFI-B15`
- **URL ouverte vérifiée** : https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/climate-risk-management
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-067.txt` (8175 mots, 68377 octets)
- **Empreinte SHA-256** : `cd686b65d8f7a6abd08c9acfe8b09f6f6c68e0900e51f2d1dcc04aa3963d7079`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Ligne directrice prudentielle climatique officielle (OSFI/BSIF B-15) | Axes : `RQ6`
- **Synthèse factuelle** : La ligne directrice B-15 du BSIF fixe les attentes de divulgation financière liée au climat pour les institutions financières fédérales en s'appuyant sur le GHG Protocol et la norme PCAF pour la comptabilisation des émissions financées et assurées. Dans le tableau récapitulatif de l'annexe 2-2 (élément b) ii), la date d'exercice financier attendue pour la divulgation des émissions absolues brutes de portée 3 — incluant obligatoirement la catégorie 15 des prêts, investissements et portefeuilles d'assurance — est arrêtée à 2028 (tandis que le volet b) iii visant les actifs sous gestion demeure marqué TBD). Ce texte officialise le jalon de fin 2028 exploité aux chapitres 9 et 12.

### [15] SRC-069 — CSA / OSC Notice of Amendments to National Instrument 31-103 — Prohibition of Chargebacks

- **Auteurs / Émetteur** : Autorités canadiennes en valeurs mobilières / Ontario Securities Commission (2026, 2026-10-08)
- **Revue / Organisme / Dépôt** : Commission des valeurs mobilières de l'Ontario (OSC) — Identifiant : `CSA-NI31-103-2026-10-08`
- **URL ouverte vérifiée** : https://www.osc.ca/sites/default/files/2026-10/csa_20261008_31-103_amendments-investment-fund-securities.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-069.txt` (4993 mots, 33492 octets)
- **Empreinte SHA-256** : `70b2dbd2b698650079e67404dc9b1037de32fb620a42f1013224514b48ae0922`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Avis d'adoption réglementaire officiel en valeurs mobilières (ACVM / OSC, 8 oct. 2026) | Axes : `RQ6`
- **Synthèse factuelle** : L'avis publié le 8 octobre 2026 par les Autorités canadiennes en valeurs mobilières dans le Bulletin de la CVMO (49 OSCB 8511) adopte les modifications à la Norme canadienne 31-103 interdisant les rétrofacturations (chargebacks) liées à la distribution de titres de fonds d'investissement assujettis. Le texte définitif fixe formellement l'entrée en vigueur au 1er octobre 2028 (« This Instrument comes into force on October 1, 2028 », sauf droit transitoire sur titres acquis avant cette date et avis différé de la Colombie-Britannique). Ce document lève l'incertitude signalée dans prd.md § 7 en ancrant exactement le périmètre et l'échéance d'octobre 2028.

### [16] SRC-070 — Loi sur les banques (L.C. 1991, ch. 46 — révision statutaire au 30 juin 2033)

- **Auteurs / Émetteur** : Parlement du Canada / Ministère de la Justice (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : Justice Canada (Lois codifiées) — Identifiant : `LC-1991-C46`
- **URL ouverte vérifiée** : https://laws-lois.justice.gc.ca/fra/lois/b-1.01/TexteComplet.html
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-070.txt` (266067 mots, 1767391 octets)
- **Empreinte SHA-256** : `0e1fc93237931022566f8436015964c426c7f7a70f22fe5ab8af69396717bd1f`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Loi fédérale codifiée officielle du Canada (Justice Canada, à jour oct. 2026) | Axes : `RQ6`
- **Synthèse factuelle** : La codification officielle de la Loi sur les banques (L.C. 1991, ch. 46, à jour le 29 octobre 2026) fixe à l'article 21 la clause statutaire de temporisation (« sunset clause ») disposant que les banques et banques étrangères autorisées ne peuvent exercer leurs activités au Canada après le 30 juin 2033 sauf prorogation ou révision parlementaire. Cette échéance quinquennale encadre l'agenda législatif de modernisation financière du Canada à moyen terme. Elle ancre directement les horizons juridiques longs des chapitres 10 et 12.

### [17] SRC-071 — AIBanks.ca — Suivi réglementaire canadien ouvert (BSIF E-23 et Ligne directrice IA de l'AMF)

- **Auteurs / Émetteur** : AIBanks.ca (2026, 2026-06-01)
- **Revue / Organisme / Dépôt** : AIBanks.ca — Identifiant : `AIBANKS-CA-AMF-2026`
- **URL ouverte vérifiée** : https://www.aibanks.ca/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-071.txt` (1985 mots, 12404 octets)
- **Empreinte SHA-256** : `2d39751c5fed55ad19aebd3cc238f8a1a26d6b266bb8bc3f7ee1e0e37a796e8b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `9.0/12` | Devis : Registre secondaire ouvert daté (AIBanks.ca, édition T4 nov. 2026) | Axes : `RQ6`
- **Synthèse factuelle** : Édition du 1er novembre 2026 du Canadian Bank AI Index recensant 210 déploiements publics d'IA auprès de 35 banques, coopératives et fintechs canadiennes tout en suivant l'état d'avancement des régimes prudentiels. Alors que le site officiel de l'AMF (lautorite.qc.ca) oppose un blocage HTTP 403 WAF (statut F) et ne peut être cité comme preuve primaire directe, cette base ouverte documente la concordance de mise en application entre la ligne directrice E-23 du BSIF et l'échéance du 1er mai 2027. Son utilisation est strictement explicitée comme référence secondaire ouverte en complément des textes fédéraux L+.

### [18] SRC-072 — Dynamic Adaptive Policy Pathways (DAPP)

- **Auteurs / Émetteur** : Marjolijn Haasnoot, Andrew Warren, Jan H. Kwakkel (2019, 2019-03-01)
- **Revue / Organisme / Dépôt** : Decision Making under Deep Uncertainty (Springer OA) — Identifiant : `DOI:10.1007/978-3-030-05252-2_4`
- **URL ouverte vérifiée** : https://link.springer.com/chapter/10.1007/978-3-030-05252-2_4
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-072.txt` (8402 mots, 56644 octets)
- **Empreinte SHA-256** : `7977e2b1fb07500ea09003968e6a53a737e5d4630117dbbfcbd5f7b9da65b29c`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Chapitre méthodologique évalué par les pairs (Springer OA DMDU 2019) | Axes : `RQ6`
- **Synthèse factuelle** : Marjolijn Haasnoot, Andrew Warren et Jan H. Kwakkel exposent la méthode des Dynamic Adaptive Policy Pathways (DAPP) pour la prise de décision stratégique et d'investissement sous incertitude profonde. Plutôt que de figer un plan statique unique, DAPP cartographie des trajectoires alternatives et identifie les points de bascule (« adaptation tipping points ») et signaux avancés déclenchant des transferts anticipés vers d'autres options avant obsolescence ou verrouillage de trajectoire. Cette méthode fournit le cadre décisionnel du chapitre 12 pour articuler signaux économiques, seuils cryptographiques et bascules réglementaires jusqu'en 2035.
