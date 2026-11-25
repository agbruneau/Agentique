# Dossier fermé de sources L+ — Chapitre 07 — Qui agit et au nom de qui ? Identité non humaine et chaîne de mandat

- **Unité du livre** : `ch07` (`sources/ch07-sources.md`)
- **Axes de recherche couverts** : `RQ4`
- **Date de gel des faits** : 2 décembre 2026
- **Protocole** : `MLR-PRISMA-SCR-LIVRE-2027-V1.2` (`metadata_only_pct = 0.0 %`, règle stricte `AO-01` sans contournement)
- **Nombre de sources probantes incluses** : 18 sources intégrales `L+`

> Ce dossier fermé recense exclusivement les sources primaires et travaux ouverts dont le texte intégral UTF-8 a été extrait, conservé sous `recherche/corpus_l_plus/` et authentifié par empreinte `SHA-256`. Aucune source en `statut F` ni copie locale non ouverte n'entre dans l'argumentation probante.

Note AO-01 (statut F) : la sous-page directe `gleif.org/.../vlei-ecosystem-governance-framework/` retourne HTTP 404 et reste exclue en `statut F` (`F#24` dans `recherche/registre-statut-f.json`) ; l'écosystème vLEI est exclusivement documenté par les sources ouvertes vérifiées regroupées dans `SRC-079`.

---

### [1] SRC-002 — Virtual Agent Economies

- **Auteurs / Émetteur** : Nenad Tomašev, Matija Franklin, Joel Z. Leibo, Julian Jacobs et al. (2025, 2025-09-12)
- **Revue / Organisme / Dépôt** : arXiv (Google DeepMind) — Identifiant : `arXiv:2509.10147`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2509.10147
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-002.txt` (23147 mots, 153510 octets)
- **Empreinte SHA-256** : `f475a70c3b55b02a344241b1e1e6e1634cd904922b191f8bed2b89c1ca5d1554`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Cadre d'analyse socio-économique et de design institutionnel | Axes : `RQ1`
- **Synthèse factuelle** : Tomašev et al. caractérisent l'émergence spontanée d'« économies d'agents virtuels » où des agents autonomes négocient, vérifient des états et exécutent des transactions à des fréquences dépassant la supervision humaine directe. Ils proposent la typologie de l'« économie bac à sable » selon deux axes orthogonaux : son origine (émergente ou intentionnelle) et son degré de perméabilité envers l'économie humaine établie. Le texte étudie les mécanismes d'enchères équitables, d'attestation vérifiable des échanges et de prévention des avantages asymétriques liés aux écarts de capacité entre modèles. Il fournit le soubassement conceptuel des chapitres sur la frontière de l'entreprise, les marchés d'agents et l'imputabilité financière.

### [2] SRC-005 — An Economy of AI Agents

- **Auteurs / Émetteur** : Gillian K. Hadfield, Andrew Koh (2025, 2025-09-01)
- **Revue / Organisme / Dépôt** : arXiv / Schwartz Reisman Institute — Identifiant : `arXiv:2509.01063`
- **URL ouverte vérifiée** : https://arxiv.org/pdf/2509.01063
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-005.txt` (11074 mots, 74078 octets)
- **Empreinte SHA-256** : `c87fd1c3cd815ba6ae355c6b34203dd83f75b20406e1eded6fbac6787e0eb0e9`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Analyse microéconomique et institutionnelle (NBER Handbook chapter) | Axes : `RQ1, RQ4`
- **Synthèse factuelle** : Hadfield et Koh modélisent une économie peuplée d'agents IA capables de planifier et d'exécuter sur des horizons longs avec une supervision humaine intermittente. Les auteurs montrent que le bon fonctionnement de ces marchés exige de nouvelles infrastructures institutionnelles : identités vérifiables des mandataires, régimes de responsabilité civile, mémoire corrélée des engagements et mécanismes de sanction contre la collusion ou la défection. Ils soulignent le risque que des agents optimisateurs exploitent les failles contractuelles ou expérimentales des environnements numériques plus vite que les régulateurs humains. Ce cadre éclaire la jonction entre délégation économique, droit des obligations et identité cryptographique.

### [3] SRC-039 — Agent2Agent (A2A) Protocol Specification

- **Auteurs / Émetteur** : Linux Foundation / A2A Project (2026, 2026-05-28)
- **Revue / Organisme / Dépôt** : a2a-protocol.org — Identifiant : `A2A-SPEC-2026`
- **URL ouverte vérifiée** : https://a2a-protocol.org/latest/specification/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-039.txt` (24333 mots, 179807 octets)
- **Empreinte SHA-256** : `fb9823ce13380143b0509c404cc5098c945ba2ec21f0dda779ddf90f4a351727`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Spécification ouverte d'interopérabilité inter-agents (Linux Foundation A2A, v1.0.1) | Axes : `RQ3, RQ5`
- **Synthèse factuelle** : La spécification Agent2Agent (A2A) propose une architecture à trois couches — modèle de données canonique, opérations abstraites et liaisons protocolaires JSON-RPC, gRPC et HTTP/REST — permettant à des agents opaques de domaines ou d'organisations distincts de se découvrir et de collaborer sur des tâches asynchrones de longue durée. Le protocole encadre la découverte par Agent Cards, les flux multi-tours, l'architecture d'extensions typées et la sécurité multi-locataires. A2A représente dans l'ouvrage le protocole horizontal complémentaire de MCP pour les échanges inter-entreprises.

### [4] SRC-041 — RFC 8693: OAuth 2.0 Token Exchange

- **Auteurs / Émetteur** : Michael B. Jones, Anthony Nadalin, Brian Campbell, John Bradley, Chuck Mortimore (2020, 2020-01)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC8693`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc8693.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-041.txt` (7815 mots, 56867 octets)
- **Empreinte SHA-256** : `22f271006669060ee5142350371ee70ed30bba6db93a9d8b43d897d462586a6f`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 8693, évalué par les pairs) | Axes : `RQ4`
- **Synthèse factuelle** : La RFC 8693 spécifie un protocole de Security Token Service fondé sur HTTP et JSON permettant d'échanger un jeton de sécurité OAuth 2.0 existant pour obtenir un nouveau jeton dans un contexte d'emprunt d'identité (impersonation) ou de délégation explicite. Elle définit notamment la revendication JWT « act » (actor) qui chaîne cryptographiquement l'identité du mandataire agissant tout en conservant le sujet initial « sub » du mandant humain, ainsi que « may_act » pour restreindre les acteurs autorisés. Ce mécanisme constitue le fondement normalisé des chaînes de délégation au nom du mandant (OBO) pour agents.

### [5] SRC-042 — RFC 9396: OAuth 2.0 Rich Authorization Requests (RAR)

- **Auteurs / Émetteur** : Torsten Lodderstedt, Justin Richer, Brian Campbell (2023, 2023-05)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9396`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9396.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-042.txt` (7380 mots, 55352 octets)
- **Empreinte SHA-256** : `e334d06f14081317caf9d457dcbffeae877c5e5009f2452d2f11adcd47d68f6b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9396, évalué par les pairs) | Axes : `RQ4`
- **Synthèse factuelle** : La RFC 9396 introduit le paramètre JSON « authorization_details » dans les requêtes et réponses de jetons OAuth 2.0 afin de décrire des autorisations granulaires fortement typées (montants plafonnés, comptes bénéficiaires, actions précises) là où les simples chaînes « scope » restent trop grossières. Elle précise la validation sémantique entre client, serveur d'autorisation et serveur de ressources ainsi que l'usage de schémas lisibles par machine. Appliqué aux agents financiers, RAR contraint cryptographiquement chaque appel d'outil au mandat exact approuvé par le client ou la politique.

### [6] SRC-043 — RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)

- **Auteurs / Émetteur** : Daniel Fett, Brian Campbell, John Bradley, Torsten Lodderstedt et al. (2023, 2023-09)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9449`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9449.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-043.txt` (12014 mots, 83632 octets)
- **Empreinte SHA-256** : `5e0267f9b8801cc882ec1dcb1d1d220cbe8cb38bbe428362cd1c8a2b33ef30e0`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9449, évalué par les pairs) | Axes : `RQ4`
- **Synthèse factuelle** : La RFC 9449 définit OAuth 2.0 Demonstrating Proof of Possession (DPoP), un mécanisme applicatif permettant de lier cryptographiquement un jeton d'accès ou d'actualisation à une paire de clés asymétriques détenue par le client grâce à un en-tête JWT signé et une confirmation par empreinte JWK (« cnf/jkt »). Contrairement aux jetons porteurs classiques, un jeton lié par DPoP volé dans une mémoire tampon ou un journal est inutilisable sans la clé privée associée, avec possibilité de nonce anti-rejeu. Ce standard sécurise les échanges entre passerelles, agents et serveurs de ressources face aux risques d'exfiltration.

### [7] SRC-044 — RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains (SCITT)

- **Auteurs / Émetteur** : Henk Birkholz, Antoine Delignat-Lavaud, Cedric Fournet, Yogesh Deshpande, Steve Lasker (2026, 2026-06)
- **Revue / Organisme / Dépôt** : IETF RFC Editor — Identifiant : `RFC9943`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc9943.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-044.txt` (9449 mots, 65473 octets)
- **Empreinte SHA-256** : `1ed0ffb4007b7986d5d3ff4da1a0489d5b9d71c5eae4cd89a7f48ae650a19fef`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Standard IETF Internet Standards Track (RFC 9943, juin 2026) | Axes : `RQ4, RQ5`
- **Synthèse factuelle** : La RFC 9943 normalise l'architecture SCITT (Supply Chain Integrity, Transparency, and Trust) pour l'enregistrement et l'audit d'énoncés signés par un émetteur unique dans des journaux transparents fondés sur des structures de données vérifiables (arbres de Merkle anti-équivocation). Elle permet à toute partie vérifiante d'obtenir la preuve cryptographique qu'un manifeste logiciel, une attestation de modèle ou un serveur d'outils a bien été enregistré et validé à un instant donné. SCITT offre une réponse normalisée aux attaques sur la chaîne d'approvisionnement d'outils agentiques et aux exigences de traçabilité d'audit.

### [8] SRC-045 — OpenID Connect Client-Initiated Backchannel Authentication Flow — Core 1.0

- **Auteurs / Émetteur** : Gonzalo Fernandez, Axel Nennker, Dave Tonge et al. (OpenID Foundation) (2021, 2021-09-01)
- **Revue / Organisme / Dépôt** : OpenID Foundation — Identifiant : `OIDC-CIBA-1.0`
- **URL ouverte vérifiée** : https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-045.txt` (9881 mots, 70895 octets)
- **Empreinte SHA-256** : `fb983307e736a3747a1dfa27f4e698f41cd45f4854f129c7cfc3c4a24c3d8020`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Spécification finale OpenID Foundation (CIBA Core 1.0) | Axes : `RQ4, RQ6`
- **Synthèse factuelle** : La norme OpenID Connect Client-Initiated Backchannel Authentication (CIBA) dissocie le dispositif de consommation où la requête démarre (un agent autonome ou un guichet) du dispositif d'authentification personnel où le mandant humain authentifie son identité et consent de manière asynchrone hors bande (push, ping ou poll). Elle élimine les redirections navigateur et prend en charge les demandes signées ainsi qu'un code utilisateur de liaison contextuelle. Dans une architecture de confiance zéro pour agents, CIBA incarne le mécanisme d'escalade humaine asynchrone pour toute transaction pivot irréversible.

### [9] SRC-046 — SPIFFE Concepts — Workload Identity, SPIFFE ID and SVID

- **Auteurs / Émetteur** : SPIFFE / Cloud Native Computing Foundation (2026)
- **Revue / Organisme / Dépôt** : CNCF SPIFFE — Identifiant : `SPIFFE-CONCEPTS-2026`
- **URL ouverte vérifiée** : https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-046.txt` (1080 mots, 6860 octets)
- **Empreinte SHA-256** : `d85539da6604e026266545f74198661e718d6fd2d7316178cab87565f44c9851`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Spécification ouverte d'identité de charge de travail (CNCF SPIFFE) | Axes : `RQ4`
- **Synthèse factuelle** : La documentation conceptuelle de SPIFFE définit comment chaque charge de travail logicielle ou instance d'agent reçoit une identité cryptographique vérifiable (SPIFFE ID sous forme d'URI de domaine de confiance) attestée par un document éphémère SVID (certificat X.509 ou jeton JWT à rotation rapide). L'attribution repose sur l'attestation dynamique de l'environnement d'exécution (nœud, conteneur, plateforme cloud) plutôt que sur des clés API statiques partagées ou des secrets durables. SPIFFE constitue la brique de base pour distinguer rigoureusement chaque agent dans les journaux et les passerelles de politiques.

### [10] SRC-047 — Workload Identity Practices (draft-ietf-wimse-workload-identity-practices-08)

- **Auteurs / Émetteur** : IETF WIMSE Working Group (2026, 2026-10-30)
- **Revue / Organisme / Dépôt** : IETF Datatracker — Identifiant : `IETF-WIMSE-WIP-08`
- **URL ouverte vérifiée** : https://www.ietf.org/archive/id/draft-ietf-wimse-workload-identity-practices-08.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-047.txt` (8930 mots, 57958 octets)
- **Empreinte SHA-256** : `863cee96178b93722999cbceee5ff74cb7b6203356af2ae571e289c6e72b408b`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Brouillon normatif de groupe de travail IETF (WIMSE WIP-08, oct. 2026) | Axes : `RQ4`
- **Synthèse factuelle** : Rédigé par Schwenkschuster et Rosomakho pour le groupe de travail IETF WIMSE (Workload Identity in Multi-System Environments), ce document recense les pratiques industrielles d'attribution d'identités éphémères sans secrets persistants aux charges de travail dans Kubernetes, SPIFFE, les fournisseurs infonuagiques et l'intégration continue. Il analyse trois patrons de livraison des justificatifs (système de fichiers, API locale et variables d'environnement) et leurs surfaces d'exposition respectives. Il ancre l'état de l'art opérationnel pour supprimer les jetons statiques longue durée dans les flottes d'agents.

### [11] SRC-048 — AI Identity Management System (draft-ietf-wimse-aims-01)

- **Auteurs / Émetteur** : IETF WIMSE Working Group (2026, 2026-11-02)
- **Revue / Organisme / Dépôt** : IETF Datatracker — Identifiant : `IETF-WIMSE-AIMS-01`
- **URL ouverte vérifiée** : https://www.ietf.org/archive/id/draft-ietf-wimse-aims-01.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-048.txt` (10027 mots, 69988 octets)
- **Empreinte SHA-256** : `ab53c74913dd1337f6183a03825d985dc1f39bc613721a54e9a3d3092231045e`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `10.5/12` | Devis : Brouillon normatif IETF spécifique aux agents IA (WIMSE AIMS-01, nov. 2026) | Axes : `RQ4`
- **Synthèse factuelle** : Le document AI Identity Management System (draft-ietf-wimse-aims-01, novembre 2026) rédigé par des auteurs de Defakto, AWS, Zscaler, Ping Identity, OpenAI et Okta applique l'architecture WIMSE et OAuth 2.0 à l'authentification et à l'autorisation des agents IA. Partant du principe que les agents sont des charges de travail exécutées dans des environnements complexes, il spécifie l'identification des agents, le cycle de provisionnement des justificatifs et les limites de l'authentification uniquement transport par rapport aux preuves applicatives. Cette source récente démontre la convergence de la normalisation industrielle fin 2026.

### [12] SRC-049 — NIST FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM)

- **Auteurs / Émetteur** : National Institute of Standards and Technology (NIST) (2024, 2024-08-13)
- **Revue / Organisme / Dépôt** : NIST Computer Security Resource Center — Identifiant : `NIST-FIPS-203`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-049.txt` (19224 mots, 125529 octets)
- **Empreinte SHA-256** : `bb840af1e6a3e1df10862cf3a8f26e435cbdc7502248a809ba1caba205a3574c`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Norme fédérale cryptographique officielle (NIST FIPS 203, août 2024) | Axes : `RQ4`
- **Synthèse factuelle** : La norme NIST FIPS 203 formalise le mécanisme d'encapsulation de clés post-quantique ML-KEM (issu de CRYSTALS-Kyber), dont la sûreté repose sur la difficulté du problème Module Learning with Errors face à un adversaire quantique. Elle définit trois jeux de paramètres selon les catégories de sécurité et régit la génération de clés, l'encapsulation et la décapsulation pour établir des clés symétriques partagées sur canaux publics. Dans le chapitre 7 et le chapitre 12, FIPS 203 fonde l'échange de clés hybride ou post-quantique pour contrer la menace « capter maintenant, déchiffrer plus tard ».

### [13] SRC-050 — NIST FIPS 204: Module-Lattice-Based Digital Signature Standard (ML-DSA)

- **Auteurs / Émetteur** : National Institute of Standards and Technology (NIST) (2024, 2024-08-13)
- **Revue / Organisme / Dépôt** : NIST Computer Security Resource Center — Identifiant : `NIST-FIPS-204`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-050.txt` (25028 mots, 150660 octets)
- **Empreinte SHA-256** : `14b6c1706d2c4a1645a7c285e37e9e7e33dd98348302c84c11db9613c0f1d267`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Norme fédérale cryptographique officielle (NIST FIPS 204, août 2024) | Axes : `RQ4`
- **Synthèse factuelle** : La norme NIST FIPS 204 normalise l'algorithme de signature numérique post-quantique sur réseaux euclidiens ML-DSA (issu de CRYSTALS-Dilithium) pour garantir l'authenticité, l'intégrité et la non-répudiation des données signées face aux ordinateurs quantiques à grande échelle. Le tableau officiel des tailles de clés et de signatures (Table 2, p. 16) établit exactement 2 420 octets pour ML-DSA-44, 3 309 octets pour ML-DSA-65 et 4 627 octets pour ML-DSA-87 (sans traiter la taille des signatures elliptiques classiques, documentée pour Ed25519 dans RFC 8032 / SRC-076). Ces ordres de grandeur pèsent directement sur les en-têtes HTTP, les chaînes de jetons OAuth et la latence des passerelles agentiques.

### [14] SRC-051 — NIST IR 8547: Transition to Post-Quantum Cryptography Standards (Final, October 2026)

- **Auteurs / Émetteur** : Dustin Moody, Ray Perlner, Andrew Regenscheid, Angela Robinson, David Cooper (2026, 2026-10-21)
- **Revue / Organisme / Dépôt** : NIST (NIST IR 8547 Final) — Identifiant : `NIST-IR-8547`
- **URL ouverte vérifiée** : https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-051.txt` (10327 mots, 78365 octets)
- **Empreinte SHA-256** : `80e6a458907c3d2e5829db8eef5b8efbbb89a25b2dbe1153bcc7129a1a4a2599`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `12.0/12` | Devis : Rapport technique officiel NIST final de transition (NIST IR 8547, oct. 2026, approuvé ERB le 21 octobre 2026) | Axes : `RQ4`
- **Synthèse factuelle** : Le rapport final NIST IR 8547 d'octobre 2026 planifie la transition des algorithmes asymétriques vulnérables (RSA, ECDSA, EdDSA, ECDH) vers les normes post-quantiques FIPS 203, 204 et 205. Il fixe la dépréciation des schémas asymétriques classiques (>= 112 bits) après 2030 et leur interdiction après 2035 (avec jalons fédéraux pour les actifs à haute valeur : 31 décembre 2030 pour l'établissement de clés et 31 décembre 2031 pour les signatures), tout en prévoyant l'interdiction des algorithmes symétriques 112 bits et de SHA-1 en 2030.

### [15] SRC-052 — Advancing a Coordinated Roadmap for the Transition to Post-Quantum Cryptography in the Financial Sector

- **Auteurs / Émetteur** : G7 Cyber Expert Group (CEG) (2026, 2026-01-14)
- **Revue / Organisme / Dépôt** : G7 Cyber Expert Group / UK HM Treasury & Bank of England — Identifiant : `G7-CEG-PQC-ROADMAP-2026`
- **URL ouverte vérifiée** : https://assets.publishing.service.gov.uk/media/6966149d8d599f4c09e1ffab/G7-CEG-Quantum-Roadmap.pdf
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-052.txt` (2175 mots, 16420 octets)
- **Empreinte SHA-256** : `cab48e350b2941891ec38ed7545d2b276b5815804d690187650c232424c945e3`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Feuille de route multilatérale officielle (G7 Cyber Expert Group, janv. 2026) | Axes : `RQ4, RQ6`
- **Synthèse factuelle** : Publiée en janvier 2026 par le G7 Cyber Expert Group, cette feuille de route coordonnée non contraignante conseille les ministères des Finances, banques centrales et institutions financières sur la migration vers la cryptographie résistante au quantique et l'agilité cryptographique. Le document relève que les orientations des juridictions pointent vers 2035 comme horizon cible global tout en recommandant une approche duale fondée sur les risques priorisant les systèmes critiques dans la fenêtre indicative 2030–2032. Il insiste sur la gouvernance de la direction, la cartographie des dépendances envers les fournisseurs tiers et le risque « capter maintenant, déchiffrer plus tard ».

### [16] SRC-053 — Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates (incl. Ballot SC-081v3)

- **Auteurs / Émetteur** : CA/Browser Forum Server Certificate Working Group (2026, 2026-10-04)
- **Revue / Organisme / Dépôt** : CA/Browser Forum — Identifiant : `CABF-BR-SC081V3`
- **URL ouverte vérifiée** : https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-053.txt` (47637 mots, 337172 octets)
- **Empreinte SHA-256** : `8d44ae9b57d6bc8b4bc90896c0edff9f2217d7e7468d3b19ac285454e31016c2`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.5/12` | Devis : Standard PKI public en vigueur (CA/Browser Forum BR v2.3.1, Ballot SC081) | Axes : `RQ4`
- **Synthèse factuelle** : Les Baseline Requirements v2.3.1 (4 octobre 2026) du CA/Browser Forum intègrent formellement le calendrier contraignant du Ballot SC081 (référencé `2.1.5 | SC081` dans `SRC-053.txt` L151, correspondant au scrutin SC-081v3) réduisant par paliers la durée maximale de validité et de réutilisation des validations de certificats TLS publics. Après l'étape à 200 jours (15 mars 2026), la validité maximale et le réemploi des preuves de domaine/IP chutent à 100 jours le 15 mars 2027, puis à 47 jours (avec réutilisation limitée à 10 jours) le 15 mars 2029 (§ 4.2.1 et § 6.3.2). Ce resserrement impose l'automatisation intégrale ACME et la crypto-agilité sur toutes les passerelles d'agents exposées.

### [17] SRC-076 — RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)

- **Auteurs / Émetteur** : Simon Josefsson, Ilari Liusvaara (2017, 2017-01)
- **Revue / Organisme / Dépôt** : IRTF / IETF RFC Editor — Identifiant : `RFC8032`
- **URL ouverte vérifiée** : https://www.rfc-editor.org/rfc/rfc8032.txt
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-076.txt` (12059 mots, 87266 octets)
- **Empreinte SHA-256** : `29c43d9f68a78933e16355eba485ce654fb7256858b69f8d1f02af9ea40e25cc`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Oui | Score AACODS : `11.5/12` | Devis : Spécification IRTF/IETF RFC 8032 (EdDSA : Ed25519 et Ed448) | Axes : `RQ4`
- **Synthèse factuelle** : La RFC 8032 spécifie l'algorithme de signature numérique sur courbes d'Edwards EdDSA pour les instances Ed25519 et Ed448 (§ 3.3 et § 5.1.6). Elle établit notamment que les clés privées et publiques Ed25519 mesurent 32 octets et que toute signature Ed25519 (y compris Ed25519ctx et Ed25519ph) pèse exactement 64 octets (§ 7), contre 114 octets pour Ed448. Cette spécification fonde rigoureusement le repère comparatif de 64 octets face aux signatures post-quantiques ML-DSA.

### [18] SRC-079 — GLEIF verifiable LEI (vLEI) Trust Chain & WebOfTrust vLEI KERI/ACDC Ecosystem Specifications (ISO 17442-3)

- **Auteurs / Émetteur** : Global Legal Entity Identifier Foundation (GLEIF) / WebOfTrust vLEI (2026, 2026-10-15)
- **Revue / Organisme / Dépôt** : GLEIF & GitHub (GLEIF-IT/vlei-egf, WebOfTrust/vLEI) — Identifiant : `GLEIF-VLEI-ISO17442-3`
- **URL ouverte vérifiée** : https://www.gleif.org/organizational-identity/lei-vlei/the-verifiable-lei-vlei/
- **Texte intégral L+** : `recherche/corpus_l_plus/SRC-079.txt` (5350 mots, 39987 octets)
- **Empreinte SHA-256** : `2ccc0f09f7c8475c0236605ba2b3f07537945e72e998df4db363f641a6166bd5`
- **Évaluation et devis** : Statut `L+` (`metadata_only: false`) | Évalué par les pairs : Non (document officiel, norme ou prépublication ouverte) | Score AACODS : `11.0/12` | Devis : Documentation officielle GLEIF et spécifications KERI/ACDC WebOfTrust vLEI (ISO 17442-3) | Axes : `RQ4`
- **Synthèse factuelle** : Ce corpus ouvert regroupe la présentation officielle GLEIF du vLEI (normalisé ISO 17442-3 en 2024), l'index documentaire du dépôt officiel `GLEIF-IT/vlei-egf` et les spécifications techniques KERI/ACDC du dépôt `WebOfTrust/vLEI`. Il documente GLEIF comme racine de confiance numérique reliée au Global LEI Index et les six schémas hiérarchiques de justificatifs vérifiables (QVI, LE, OOR_AUTH, OOR, ECR_AUTH avec clause de confidentialité IPEX/ACDC, et ECR) fondés sur les identifiants auto-adressants SAID et les journaux d'événements transactionnels.
