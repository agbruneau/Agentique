# Chapitre M-10 — Carte des capacités cibles

*Question directrice : Que doit savoir faire l’entreprise en 2035?*

> **État de référence (16 novembre 2026) :** Ce chapitre définit les cinquante-deux capacités cibles (`CAP-001` à `CAP-052`) constituant le référentiel consolidé de l’architecture 2028-2035, en parité stricte avec `Master/registre/capacites.json` et l’Annexe B. Chaque fiche est formulée en rôle fonctionnel sans aucun nom de produit commercial; les textes fermés non lus figurent dans les Limites.

Le modèle de référence du chapitre M-9 fixe l’ossature des responsabilités; la **carte des capacités cibles** précise, emplacement par emplacement, ce que l’institution financière doit savoir accomplir, mesurer et prouver sur la période 2028-2035. Elle réunit **cinquante-deux capacités (**`CAP-001` **à** `CAP-052`**)** découplées des produits du marché et dimensionnées sans quota arbitraire [1] [3] [5] (C27, § 23.1).

> **[Figure]**
> - Carte des capacités cibles 2035 (52 capacités : 42 invariantes, 10 conditionnelles)
> - Invariante (A, B, C) Conditionnelle (scénarios nommés) Paliers : P1 (2028–29) · P2 (2030–32) · P3 (2033–35)
> - Couche 1 — Interaction (6)
> - P1 001 Interfaces déclaratives bornées P1 002 Supervision humaine liée P1 003 Transparence et révision (Loi 25)
> - P2·AB 004 Voix et multimodal temps réel P1 005 Archivage communications P3·AB 006 Encadrement agents externes
> - Couche 2 — Agents et orchestration (8)
> - P1 007 Séquencement déterministe P1 008 Exécution durable et réveil P1 009 Idempotence et sagas
> - P2 010 Topologies et revue hétérogène P2 011 Dorsale événementielle audit P2 012 Délégation et garde anti-boucle
> - P2·BC 013 Fédération gravité données P3·AB 014 Négociation inter-organisations
> - Couche 3 — Contexte et connaissance (7)
> - P2 015 Couche sémantique gouvernée P2 016 Médiation standards sectoriels P1 017 Contexte compilé et ACL amont
> - P1 018 Compétences signées portables P2 019 Mémoire bi-temporelle et oubli P2 020 Contrats qualité et quarantaine
> - P1 021 Cloisonnement entités et Loi 25
> - Couche 4 — Accès (7)
> - P1 022 Passerelle à cinq contrôles P1 023 Outils métier et schémas signés P1 024 Encapsulation patrimoniale
> - P1·BC 025 Harnais dérogatoire CUA (12 m) P2 026 Passerelles bancaires ouvertes P3·AC 027 Connecteurs espaces fédérés
> - P2·BC 028 Sas télématique/OT hors ligne
> - Couche 5 — Modèles (6)
> - P1 029 Routage d'inférence à 3 paliers P1 030 Confinement sans réseau sortant P2 031 Continuité cognitive bimodèle
> - P1 032 Résidence des 6 substrats d'état P2·BC 033 Inférence confidentielle enclave P2·BC 034 Distillation sous sas anti-PII
> - Plan de contrôle transversal possédé par l’institution (Volets A, B et C)
> - Volet A — Identité & sécurité (7)
> - P1 035 NHI sans secret & TLS 47 j
> - P1 036 Délégation atténuée par saut
> - P1 037 Décision politique hors modèle
> - P1 038 Défense injections et menaces
> - P1 039 Coupe-circuit hiérarchisé
> - P2 040 Agilité CBOM & PQC ML-DSA
> - P3·AC 041 Identité légale et mandats tiers
> - Volet B — Observabilité & FinOps (5)
> - P1 042 Traces causales et couloir PII
> - P1 043 Simulation, chaos et canari
> - P2 044 Surveillance dérive et budgets
> - P1 045 Coût par résultat et disjoncteur
> - P2 046 Empreinte énergie et Scope 3
> - Volet C — Gouvernance & registre (6)
> - P1 047 Registre central et cote E-23
> - P1 048 Matrice D1–D8 × Classes 1–6
> - P1 049 Qualification et preuve légale
> - P1 050 Validation 2e et 3e lignes
> - P1 051 Gouvernance tiers et sortie
> - P2 052 Usine logicielle et SRE borné

*Fig. 3. – Carte des capacités cibles par couche et par volet du plan de contrôle*

Chaque capacité est définie une seule fois par une **fiche à dix champs** : identifiant et nom, emplacement, description, statut (**quarante-deux invariantes** sous A, B et C; **dix conditionnelles** détaillées en M-11), palier d’atteinte (`P1` en 2028-2029, `P2` en 2030-2032, `P3` en 2033-2035 C : tous ; SIG-003 ), motif sourcé, preuve d’atteinte vérifiable, dépendances, renvois exacts au Compendium 2027, aux ADR et au Cadre 2026, et signal de révision (`SIG-nnn`).

| Emplacement (chapitre M-9) | Plage | Total | Invariantes | Conditionnelles | P1 | P2 | P3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `interaction` | `CAP-001`–`CAP-006` | 6 | 4 | 2 | 4 | 1 | 1 |
| `agents-orchestration` | `CAP-007`–`CAP-014` | 8 | 6 | 2 | 3 | 4 | 1 |
| `contexte-connaissance` | `CAP-015`–`CAP-021` | 7 | 7 | 0 | 3 | 4 | 0 |
| `acces` | `CAP-022`–`CAP-028` | 7 | 4 | 3 | 4 | 2 | 1 |
| `modeles` | `CAP-029`–`CAP-034` | 6 | 4 | 2 | 3 | 3 | 0 |
| `controle-identite-securite` | `CAP-035`–`CAP-041` | 7 | 6 | 1 | 5 | 1 | 1 |
| `controle-observabilite-finops` | `CAP-042`–`CAP-046` | 5 | 5 | 0 | 3 | 2 | 0 |
| `controle-gouvernance-registre` | `CAP-047`–`CAP-052` | 6 | 6 | 0 | 5 | 1 | 0 |
| **Total** | `CAP-001`**–**`CAP-052` | **52** | **42** | **10** | **30** | **18** | **4** |

## 10.1 Couche 1 — Interaction (`CAP-001` à `CAP-006`)

Surface d’exposition directe aux clients, épargnants, assurés et réviseurs internes, cette couche garantit le rendu sans script arbitraire, l’effectivité de la révision humaine [1], l’avis et le recours de l’article 12.1 de la Loi 25 [15], l’archivage supervisé des communications [12] [16] et le filtrage des agents externes [9].

### CAP-001 — Rendu d’interfaces génératives sur catalogues déclaratifs bornés

P : CAP-001

- **Identifiant et nom :** `CAP-001` — Rendu d’interfaces génératives sur catalogues déclaratifs bornés
- **Emplacement :** `interaction`
- **Description :** Sépare l’intention d’affichage produite par l’agent et le rendu visuel au poste client ou conseiller via un catalogue fermé de composants homologués, sans exécution de scripts arbitraires.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Confinement des injections et exfiltrations côté client sur canaux numériques (C27, § 7.1, § 31.4).
- **Preuve d’atteinte :** Rejet de 100 % des composants hors catalogue signé lors des tests d’intrusion automatisés.
- **Dépendances :** `CAP-037`
- **Renvois :** C27, § 7.1, § 10.1, § 31.4; ADR-007; Cadre 2026, Plan A

- **Signal de révision :** `SIG-004` — Convergence ou fragmentation des protocoles d’interaction agent-utilisateur et inter-domaines.

### CAP-002 — Postes de supervision humaine instrumentés et approbation liée aux paramètres

P : CAP-002

- **Identifiant et nom :** `CAP-002` — Postes de supervision humaine instrumentés et approbation liée aux paramètres
- **Emplacement :** `interaction`
- **Description :** Affiche aux réviseurs une vue différentielle des pièces et de l’impact métier, plafonne la cadence par quart, lie la signature d’approbation au condensat des paramètres et injecte des dossiers témoins.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Prévention de la complaisance d’approbation et supervision effective sous BSIF E-23 D [1] (C27, § 22.5, § 30.4).
- **Preuve d’atteinte :** Rejet technique de tout jeton dont les paramètres ont varié après attente et mesure trimestrielle sur dossiers témoins.
- **Dépendances :** `CAP-008`, `CAP-036`
- **Renvois :** C27, § 18.5, § 22.4, § 22.5, § 30.4, § 41.4; ADR-018, ADR-025; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-106` — Interprétation administrative ou judiciaire qualifiant d’exclusivement automatisée une révision humaine purement formelle.

### CAP-003 — Transparence client, avis contemporain et canal de révision humaine effective

P : CAP-003

- **Identifiant et nom :** `CAP-003` — Transparence client, avis contemporain et canal de révision humaine effective
- **Emplacement :** `interaction`
- **Description :** Informe la personne lorsqu’elle interagit avec un agent ou subit une décision automatisée, expose sur demande les facteurs principaux et ouvre un recours direct devant un professionnel habilité.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Obligations de transparence et de réexamen de l’article 12.1 de la Loi 25 et traitement équitable des clients [7] [13] [15].
- **Preuve d’atteinte :** Présence vérifiée de l’explication des facteurs et du canal de révision sur 100 % des décisions de classe 5.
- **Dépendances :** `CAP-049`
- **Renvois :** C27, § 22.6, § 38.3, § 38.4; ADR-024; Cadre 2026, Plan C
- **Signal de révision :** `SIG-107` — Adoption d’une réforme fédérale instaurant un régime pancanadien des décisions automatisées dans le secteur privé.

### CAP-004 — Interaction vocale et multimodale en temps réel avec gestion d’interruption

P : CAP-004

- **Identifiant et nom :** `CAP-004` — Interaction vocale et multimodale en temps réel avec gestion d’interruption
- **Emplacement :** `interaction`
- **Description :** Gère les échanges vocaux et visuels à basse latence pour l’accueil ou la déclaration de sinistre, avec interruption immédiate par l’usager, consentement explicite et transcription caviardée.
- **Statut :** Conditionnelle (scénarios A, B)
- **Palier d’atteinte :** P2
- **Motif :** Absorption des pointes d’appels et pièces visuelles lorsque la pile multimodale respecte le cadre juridictionnel (C27, § 7.1, § 22.5).
- **Preuve d’atteinte :** Transfert sans perte de contexte vers un préposé en moins de deux secondes lors des essais de charge.
- **Dépendances :** `CAP-001`, `CAP-032`, `CAP-042`
- **Renvois :** C27, § 7.1, § 22.5, § 33.4; ADR-007; Cadre 2026, Plan A, Plan B
- **Signal de révision :** `SIG-102` — Encadrement québécois accru de l’offre et de la collecte numériques sans représentant certifié.

### CAP-005 — Contrôle préalable et archivage supervisé des communications externes assistées

P : CAP-005

- **Identifiant et nom :** `CAP-005` — Contrôle préalable et archivage supervisé des communications externes assistées
- **Emplacement :** `interaction`
- **Description :** Filtre avant envoi les correspondances et synthèses rédigées avec un agent selon les règles sectorielles, bloque tout conseil non autorisé et archive chaque échange dans le dossier de surveillance.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Surveillance des communications et tenue de dossiers des courtiers et distributeurs d’assurance [12] [16] (C27, § 38.3).
- **Preuve d’atteinte :** Couverture à 100 % des messages assistés par l’archive supervisée et blocage prouvé des recommandations hors mandat.
- **Dépendances :** `CAP-037`, `CAP-049`
- **Renvois :** C27, § 38.3, § 39.5, § 39.6; ADR-024; Cadre 2026, Plan C
- **Signal de révision :** `SIG-105` — Adoption de règles contraignantes des autorités en valeurs mobilières sur les outils conversationnels et la convenance.

### CAP-006 — Authentification et encadrement des agents externes sur les canaux numériques

P : CAP-006

- **Identifiant et nom :** `CAP-006` — Authentification et encadrement des agents externes sur les canaux numériques

- **Emplacement :** `interaction`
- **Description :** Identifie cryptographiquement les agents mandatés par des clients ou tiers sur les portails publics, bloque l’extraction d’écran prohibée et applique des quotas ainsi que des parcours dédiés.
- **Statut :** Conditionnelle (scénarios A, B)
- **Palier d’atteinte :** P3
- **Motif :** Accueil encadré d’agents consommateurs conjugué à l’interdiction légale du grattage d’écran bancaire [9] (C27, § 9.4, § 9.6).
- **Preuve d’atteinte :** Rejet de toute requête d’agent externe sans signature d’origine ni preuve de mandat valide lors d’audits publics.
- **Dépendances :** `CAP-026`, `CAP-041`
- **Renvois :** C27, § 9.1, § 9.2, § 9.4, § 9.6; ADR-005, ADR-026; Cadre 2026, Plan A
- **Signal de révision :** `SIG-103` — Prise des décrets interdisant le grattage d’écran et ouvrant l’initiation d’opérations bancaires par tiers accrédités.

## 10.2 Couche 2 — Agents et orchestration (`CAP-007` à `CAP-014`)

Cœur de la coordination multi-étapes exposé aux quatorze modes d’échec documentés en production [37] (C27, ch. 16 à 21), cette couche impose dès `P1` l’enveloppe déterministe, l’exécution durable et les sagas à compensation [4] [11], puis encadre topologies, événements, délégation anti-boucle [22], fédération multi-plateformes et négociation externe.

### CAP-007 — Enveloppe de séquencement déterministe autour des cellules agentiques bornées

P : CAP-007

- **Identifiant et nom :** `CAP-007` — Enveloppe de séquencement déterministe autour des cellules agentiques bornées
- **Emplacement :** `agents-orchestration`
- **Description :** Confie l’enchaînement maître des processus critiques, les portes de conformité et l’arrêt à du code ou une machine à états déterministe encapsulant des cellules agentiques typées et bornées.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Fiabilité observée des séquences courtes sous contrôle logiciel et auditabilité exigée sous BSIF E-23 D [1] [37] (C27, § 4.2, § 17.6).
- **Preuve d’atteinte :** Absence vérifiée en revue d’architecture de tout routage maître non déterministe sur les classes de décision 3 à 5.
- **Dépendances :** `CAP-037`
- **Renvois :** C27, § 4.2, § 17.1, § 17.2, § 17.6, § 17.7; ADR-001, ADR-002; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-013` — Publication d’un banc indépendant démontrant plus de 95 % de réussite holistique sur des tâches longues non algorithmiques.

### CAP-008 — Exécution durable, journalisation déterministe et revalidation au réveil

P : CAP-008

- **Identifiant et nom :** `CAP-008` — Exécution durable, journalisation déterministe et revalidation au réveil
- **Emplacement :** `agents-orchestration`
- **Description :** Journalise de façon chiffrée les étapes des flux longs, reprend après panne sans répéter les appels accomplis et revalide les préconditions métiers ainsi que les droits au sortir de mise en veille.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Protection contre les pertes d’état, écritures dupliquées et écarts post-attente lors d’approbations différées [4] (C27, § 18.1, § 18.5).
- **Preuve d’atteinte :** Survie de 100 % des flux longs lors d’interruptions brutales de nœuds sans double appel externe ni corruption.
- **Dépendances :** `CAP-032`
- **Renvois :** C27, § 18.1, § 18.2, § 18.5, § 18.6; ADR-012; Cadre 2026, Plan B
- **Signal de révision :** `SIG-014` — Persistance d’un taux élevé d’échec de bout en bout sur les chaînes multi-agents malgré la persistance d’état.

### CAP-009 — Idempotence transactionnelle de bout en bout, sagas à compensation et tampon d’irréversibilité

P : CAP-009

- **Identifiant et nom :** `CAP-009` — Idempotence transactionnelle de bout en bout, sagas à compensation et tampon d’irréversibilité
- **Emplacement :** `agents-orchestration`
- **Description :** Attache une clé d’idempotence déterministe à chaque mutation, ordonne les transactions multi-systèmes autour d’un point pivot avec compensations pré-enregistrées et retient les sorties irréversibles.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Intégrité comptable face aux pannes partielles et à l’irrévocabilité des rails de paiement en temps réel [11] (C27, § 18.3, § 18.4, § 18.7).
- **Preuve d’atteinte :** Zéro écriture orpheline ou doublon comptable lors d’injections de pannes réseau à mi-parcours transactionnel.
- **Dépendances :** `CAP-008`, `CAP-022`
- **Renvois :** C27, § 18.3, § 18.4, § 18.7, § 19.7; ADR-012, ADR-013; Cadre 2026, Plan A, Plan B
- **Signal de révision :** `SIG-104` — Mise en production générale du règlement interbancaire en temps réel irrévocable.

### CAP-010 — Catalogue homologué de topologies multi-agents et revue contradictoire hétérogène

P : CAP-010

- **Identifiant et nom :** `CAP-010` — Catalogue homologué de topologies multi-agents et revue contradictoire hétérogène

- **Emplacement :** `agents-orchestration`
- **Description :** Privilégie l’agent unique lorsqu’il suffit, interdit les cycles conversationnels libres et plafonne toute boucle producteur-critique avec détection de stagnation et deux familles distinctes de modèles.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Contention des quatorze modes d’échec multi-agents et de la dérive quadratique des coûts [37] (C27, § 16.6, § 16.7, § 21.1).
- **Preuve d’atteinte :** Blocage en intégration continue des graphes cycliques libres ou couplant la même famille de modèles en exécution et revue.
- **Dépendances :** `CAP-007`, `CAP-029`
- **Renvois :** C27, § 16.1, § 16.4, § 16.6, § 16.7, § 21.1, § 21.5; ADR-011; Cadre 2026, Plan B, Plan C
- **Signal de révision :** `SIG-014` — Évolution mesurée des taux d’échec de coordination lors du chaînage de plus de trois agents spécialisés.

### CAP-011 — Dorsale événementielle asynchrone et rejouabilité d’audit

P : CAP-011

- **Identifiant et nom :** `CAP-011` — Dorsale événementielle asynchrone et rejouabilité d’audit
- **Emplacement :** `agents-orchestration`
- **Description :** Découple par événements immuables typés les flux multi-consommateurs ou soumis à pointes extrêmes, assure la publication atomique avec l’état métier et permet la relecture contrôlée d’audit.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Absorption des pointes climatiques ou boursières et résilience opérationnelle sous BSIF E-21 [4] [20] (C27, § 19.1, § 19.4, § 19.7).
- **Preuve d’atteinte :** Zéro perte de message sous débit décuplé et reconstitution fidèle d’une séquence passée sur banc isolé.
- **Dépendances :** `CAP-009`, `CAP-015`
- **Renvois :** C27, § 19.1, § 19.3, § 19.4, § 19.7; ADR-013; Cadre 2026, Plan B
- **Signal de révision :** `SIG-109` — Renforcement des exigences prudentielles de gestion des événements climatiques et des flux de capteurs.

### CAP-012 — Protocole normalisé de délégation inter-agents interne et garde anti-boucle

P : CAP-012

- **Identifiant et nom :** `CAP-012` — Protocole normalisé de délégation inter-agents interne et garde anti-boucle
- **Emplacement :** `agents-orchestration`
- **Description :** Normalise les délégations asynchrones entre domaines par fiches d’agents signées, états de cycle de vie, artefacts typés et compteur de sauts coupant immédiatement toute boucle inter-plateformes.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2

- **Motif :** Standardisation du protocole inter-agents et prévention des emballements croisés entre progiciels [22] (C27, § 6.2, § 6.4, § 27.1).
- **Preuve d’atteinte :** Coupure instantanée de 100 % des cycles simulés entre trois environnements distincts et vérification des signatures.
- **Dépendances :** `CAP-022`, `CAP-036`, `CAP-047`
- **Renvois :** C27, § 6.2, § 6.4, § 6.6, § 27.1, § 31.7; ADR-006, ADR-015; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-004` — Soumission ou report des spécifications IETF de découverte et de protocole de session inter-agents.

### CAP-013 — Fédération d’orchestration multi-plateformes selon la gravité des données

P : CAP-013

- **Identifiant et nom :** `CAP-013` — Fédération d’orchestration multi-plateformes selon la gravité des données
- **Emplacement :** `agents-orchestration`
- **Description :** Maintient l’exécution mono-domaine au sein des agents natifs proches des données métiers, mais rapatrie sur l’orchestrateur durable neutre toute transaction coordonnant au moins deux silos.
- **Statut :** Conditionnelle (scénarios B, C)
- **Palier d’atteinte :** P2
- **Motif :** Coexistence durable de plans de contrôle éditeurs fragmentés et maîtrise des frais à l’acte (C27, § 26.9, § 27.2, § 27.4).
- **Preuve d’atteinte :** Zéro appel direct non médiatisé entre deux suites applicatives dans les traces réseau et suivi du coût par saga.
- **Dépendances :** `CAP-008`, `CAP-012`, `CAP-022`
- **Renvois :** C27, § 26.9, § 27.1, § 27.2, § 27.4; ADR-015; Cadre 2026, Plan B, Plan C
- **Signal de révision :** `SIG-002` — Durcissement réglementaire sur les prestataires tiers critiques d’orchestration et d’infonuagique.

### CAP-014 — Négociation et exécution inter-organisations à séparation négociateur-évaluateur

P : CAP-014

- **Identifiant et nom :** `CAP-014` — Négociation et exécution inter-organisations à séparation négociateur-évaluateur
- **Emplacement :** `agents-orchestration`
- **Description :** Sépare physiquement l’agent négociateur externe de l’évaluateur interne détenant marges, réserves et règles antifraude, et exige un rapprochement tripartite déterministe hors modèle avant paiement.
- **Statut :** Conditionnelle (scénarios A, B)
- **Palier d’atteinte :** P3
- **Motif :** Protection du secret commercial, anti-collusion et sûreté des règlements au stade 4 (C27, § 45.4, § 45.6, § 45.7).
- **Preuve d’atteinte :** Absence prouvée des prix de réserve dans le contexte du négociateur sous attaque adverse et blocage de tout écart tripartite.
- **Dépendances :** `CAP-009`, `CAP-012`, `CAP-041`

- **Renvois :** C27, § 36.3, § 45.1, § 45.4, § 45.6, § 45.7; ADR-026; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-007` — Reconnaissance prudentielle ou interbancaire de justificatifs cryptographiques de mandat organisationnel.

## 10.3 Couche 3 — Contexte et connaissance (`CAP-015` à `CAP-021`)

Sept capacités invariantes empêchent les agents d’agir sur des définitions erronées, des pièces hors habilitations ou des faits périmés [1] [15] (C27, ch. 12 à 15), tout en appliquant dès l’ingestion les murailles de groupe, le secret anti-blanchiment et l’exclusion génétique [6] [8] [18] [19].

### CAP-015 — Couche sémantique gouvernée et contrats ontologiques métiers versionnés

P : CAP-015

- **Identifiant et nom :** `CAP-015` — Couche sémantique gouvernée et contrats ontologiques métiers versionnés
- **Emplacement :** `contexte-connaissance`
- **Description :** Centralise dans un référentiel versionné les définitions d’indicateurs financiers, règles d’admissibilité et entités métiers, interdisant aux agents de recalculer librement des agrégats par requêtes brutes.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Gouvernance des définitions de données de modèles et fiabilité des rapports de gestion et prudentiels exigées par BSIF E-23 dès le 1er mai 2027 D [1], conjuguées à la cohérence sémantique inter-agents (C27, § 12.1, § 12.2, § 12.7).
- **Preuve d’atteinte :** 100 % des requêtes d’indicateurs prudentiels résolues par vues sémantiques homologuées sans requête ad hoc directe.
- **Dépendances :** `CAP-022`
- **Renvois :** C27, § 3.3, § 12.1, § 12.2, § 12.3, § 12.7; ADR-009; Cadre 2026, Plan C
- **Signal de révision :** `SIG-110` — Publication d’extensions sémantiques dédiées aux agents par les organismes sectoriels de normalisation.

### CAP-016 — Médiation sémantique canonique vers les standards de données financiers et d’assurance

P : CAP-016

- **Identifiant et nom :** `CAP-016` — Médiation sémantique canonique vers les standards de données financiers et d’assurance
- **Emplacement :** `contexte-connaissance`
- **Description :** Traduit de manière déterministe et traçable les codifications internes patrimoniales vers les standards sectoriels de paiement, de partage bancaire, de valeurs mobilières, d’assurance et de santé.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2

- **Motif :** Interopérabilité exigée par ISO 20022, le cadre bancaire ouvert et les réseaux courtiers [10] [11] [14] (C27, § 12.5, § 25.4).
- **Preuve d’atteinte :** Validation de schéma à 100 % et zéro perte de précision sur les essais d’aller-retour avec les formats cibles.
- **Dépendances :** `CAP-015`, `CAP-024`
- **Renvois :** C27, § 3.2, § 3.3, § 12.5, § 25.4; ADR-009, ADR-016; Cadre 2026, Plan C
- **Signal de révision :** `SIG-104` — Entrée en service opérationnel du rail de paiement en temps réel et évolution de ses guides compagnons.

### CAP-017 — Compilation déterministe du contexte, filtrage d’accès en amont et passage par référence

P : CAP-017

- **Identifiant et nom :** `CAP-017` — Compilation déterministe du contexte, filtrage d’accès en amont et passage par référence
- **Emplacement :** `contexte-connaissance`
- **Description :** Ordonne les segments de contexte pour préserver les préfixes de cache, applique les droits d’accès du mandant avant toute recherche et transmet les pièces lourdes entre agents par jeton de référence.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Moindre privilège sur les documents et maîtrise de la dérive cognitive et tarifaire en long contexte (C27, § 13.5, § 15.3, § 15.6).
- **Preuve d’atteinte :** Zéro fragment hors habilitations retourné lors des tests d’accès croisés et suivi du taux de réutilisation de préfixe.
- **Dépendances :** `CAP-036`
- **Renvois :** C27, § 13.2, § 13.5, § 13.6, § 15.3, § 15.6; ADR-008; Cadre 2026, Plan A, Plan B
- **Signal de révision :** `SIG-015` — Hausse du coût complet par résultat réussi liée à l’inflation de la taille des contextes multi-tours.

### CAP-018 — Bibliothèque gouvernée, versionnée et signée de compétences procédurales portables

P : CAP-018

- **Identifiant et nom :** `CAP-018` — Bibliothèque gouvernée, versionnée et signée de compétences procédurales portables
- **Emplacement :** `contexte-connaissance`
- **Description :** Encapsule les procédures métiers et barèmes sous forme de paquets déclaratifs portables entre modèles, chargés progressivement à la demande et signés cryptographiquement en chaîne de livraison.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Portabilité procédurale et intégrité des consignes métiers sous BSIF E-23 D [1] (C27, § 13.3, § 27.3, § 34.2).
- **Preuve d’atteinte :** Exécution conforme d’un même paquet sur deux familles de modèles et rejet automatique de tout paquet non signé.
- **Dépendances :** `CAP-047`

- **Renvois :** C27, § 13.3, § 13.5, § 27.3, § 34.2; ADR-005, ADR-022; Cadre 2026, Plan C
- **Signal de révision :** `SIG-005` — Évolution des formats normalisés d’exposition de compétences et de ressources contextuelles.

### CAP-019 — Mémoire persistante bi-temporelle auditable à date, garde anti-empoisonnement et oubli sélectif

P : CAP-019

- **Identifiant et nom :** `CAP-019` — Mémoire persistante bi-temporelle auditable à date, garde anti-empoisonnement et oubli sélectif
- **Emplacement :** `contexte-connaissance`
- **Description :** Réserve la mémoire inter-sessions aux besoins prouvés, horodate validité métier et ingestion sans écrasement, filtre l’empoisonnement persistant et exécute l’effacement sélectif vérifiable.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Preuve à date devant le superviseur et obligation légale de destruction de l’article 23 de la Loi 25 D [1] [15] (C27, § 14.5, § 14.6).
- **Preuve d’atteinte :** Restitution exacte de l’état mémoriel actif à une date passée et preuve d’effacement d’un dossier purgé.
- **Dépendances :** `CAP-017`, `CAP-032`, `CAP-038`
- **Renvois :** C27, § 14.1, § 14.2, § 14.5, § 14.6, § 31.6; ADR-010; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-106` — Précisions réglementaires sur la conservation et l’explicabilité des éléments contextuels ayant servi à une décision.

### CAP-020 — Contrats formels de qualité des données et sas de quarantaine avant exposition

P : CAP-020

- **Identifiant et nom :** `CAP-020` — Contrats formels de qualité des données et sas de quarantaine avant exposition
- **Emplacement :** `contexte-connaissance`
- **Description :** Soumet chaque table ou flux alimentant un agent décisionnel à un contrat vérifiant fraîcheur, bornes et dérive dans un sas isolé avant publication, mettant en quarantaine tout lot non conforme.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Blocage en amont des données corrompues et fiabilité des divulgations prudentielles et climatiques D [1] [21] (C27, § 15.1, § 47.5).
- **Preuve d’atteinte :** Mise en quarantaine en moins d’une minute d’un lot injecté hors bornes sans exposition aux agents aval.
- **Dépendances :** `CAP-015`
- **Renvois :** C27, § 15.1, § 15.2, § 47.5; ADR-030; Cadre 2026, Plan B, Plan C
- **Signal de révision :** `SIG-109` — Entrée en vigueur de nouvelles exigences prudentielles sur la qualité des données climatiques et de capteurs.

### CAP-021 — Cloisonnement contextuel par entité juridique, finalité de consentement et données prohibées

P : CAP-021

- **Identifiant et nom :** `CAP-021` — Cloisonnement contextuel par entité juridique, finalité de consentement et données prohibées
- **Emplacement :** `contexte-connaissance`
- **Description :** Étiquette chaque document, vecteur et fait selon l’entité juridique, le consentement exprès et la classe légale pour imposer les murailles de groupe, le secret anti-blanchiment et l’exclusion génétique.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Cloisonnement banque-assurance-courtage, secret CANAFE et Loi sur la non-discrimination génétique [6] [8] [15] [18] [19].
- **Preuve d’atteinte :** Zéro fuite inter-filiales ni restitution d’indice génétique ou de déclaration douteuse sur tests contradictoires.
- **Dépendances :** `CAP-017`, `CAP-037`
- **Renvois :** C27, § 14.3, § 15.3, § 38.3, § 38.4; ADR-008, ADR-010; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-108` — Révision législative fédérale précédant l’échéance de temporisation des lois bancaires et d’assurances.

## 10.4 Couche 4 — Accès aux outils et aux systèmes (`CAP-022` à `CAP-028`)

En réponse aux cent deux vulnérabilités de serveurs d’outils relevées en 2026 (C27, § 31.3, § 49.7) [3] [5], cette couche verrouille la passerelle aux cinq contrôles, l’épinglage de schémas, l’encapsulation décimale exacte et le retrait des agents d’écran, avant d’ouvrir les interfaces réglementées [9] [10], les espaces fédérés et le sas hors réseau [20].

### CAP-022 — Passerelle unifiée de médiation et des cinq contrôles par invocation d’outil

P : CAP-022

- **Identifiant et nom :** `CAP-022` — Passerelle unifiée de médiation et des cinq contrôles par invocation d’outil
- **Emplacement :** `acces`
- **Description :** Impose un point de passage unique entre agents et outils ou systèmes centraux appliquant authentification mutuelle, autorisation par opération, validation de schéma, quota budgétaire et trace.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Protection du cœur transactionnel et gestion du cyberrisque selon BSIF B-13 [3] [5] (C27, § 24.1, § 24.2).
- **Preuve d’atteinte :** Blocage réseau de tout appel direct vers une API métier hors passerelle et vérification des cinq contrôles.
- **Dépendances :** `CAP-035`, `CAP-037`, `CAP-042`
- **Renvois :** C27, § 5.1, § 24.1, § 24.2, § 24.5; ADR-005, ADR-014; Cadre 2026, Plan A, Plan B

- **Signal de révision :** `SIG-005` — Révision majeure du transport ou du modèle d’autorisation du protocole d’accès aux outils.

### CAP-023 — Conception d’outils orientés intention métier et épinglage cryptographique des schémas

P : CAP-023

- **Identifiant et nom :** `CAP-023` — Conception d’outils orientés intention métier et épinglage cryptographique des schémas
- **Emplacement :** `acces`
- **Description :** Expose des outils alignés sur des intentions d’affaires bornées, vérifie la signature et le condensat des schémas avant ouverture et bloque toute mutation dynamique non ré-homologuée des descripteurs.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Parade aux cent deux vulnérabilités de serveurs d’outils recensées en 2026 et aux substitutions post-approbation (C27, § 5.8, § 31.3, § 49.7).
- **Preuve d’atteinte :** Rejet immédiat de tout serveur d’outils dont l’empreinte diverge du fichier de verrouillage signé en production.
- **Dépendances :** `CAP-022`, `CAP-047`
- **Renvois :** C27, § 5.2, § 5.8, § 31.3, § 31.5, § 49.7; ADR-005, ADR-019; Cadre 2026, Plan A
- **Signal de révision :** `SIG-101` — Conversion des observations du BSIF sur la sécurité des outils d’agents en attentes prudentielles opposables.

### CAP-024 — Encapsulation déterministe des systèmes centraux patrimoniaux en arithmétique décimale exacte

P : CAP-024

- **Identifiant et nom :** `CAP-024` — Encapsulation déterministe des systèmes centraux patrimoniaux en arithmétique décimale exacte
- **Emplacement :** `acces`
- **Description :** Encapsule les programmes centraux bancaires et actuariels derrière des adaptateurs déterministes préservant l’arithmétique décimale exacte, lissant la charge et interdisant les trames brutes par modèle.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Exactitude comptable au centime et disponibilité des systèmes d’enregistrement centraux [4] (C27, § 25.1, § 25.4, § 25.5).
- **Preuve d’atteinte :** Zéro écart d’arrondi sur cent mille opérations de test et maintien des temps de réponse centraux sous quota actif.
- **Dépendances :** `CAP-022`
- **Renvois :** C27, § 25.1, § 25.2, § 25.4, § 25.5; ADR-001, ADR-016; Cadre 2026, Plan A, Plan B
- **Signal de révision :** `SIG-015` — Évolution du ratio économique entre encapsulation progressive et modernisation directe des modules centraux.

### CAP-025 — Harnais dérogatoire sous double validation et extinction programmée des agents d’interface graphique

P : CAP-025

- **Identifiant et nom :** `CAP-025` — Harnais dérogatoire sous double validation et extinction programmée des agents d’interface graphique
- **Emplacement :** `acces`
- **Description :** Restreint les agents manipulant l’écran aux seuls écrans patrimoniaux sans API prouvée, sous caviardage de données personnelles, zones interdites, double contrôle visuel et retrait budgété à douze mois.
- **Statut :** Conditionnelle (scénarios B, C)
- **Palier d’atteinte :** P1
- **Motif :** Encadrement transitoire des progiciels fermés face aux risques d’injection visuelle et de fragilité (C27, § 25.4, § 25.5, § 31.4).
- **Preuve d’atteinte :** Chaque dérogation active possède un budget d’extinction à douze mois et tourne en session virtuelle jetable vérifiée.
- **Dépendances :** `CAP-024`, `CAP-030`, `CAP-049`
- **Renvois :** C27, § 25.4, § 25.5, § 31.4; ADR-016; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-103` — Entrée en vigueur des interdictions légales de grattage d’écran et généralisation d’interfaces normalisées.

### CAP-026 — Passerelles d’interfaces réglementées pour le partage financier ouvert et les tiers accrédités

P : CAP-026

- **Identifiant et nom :** `CAP-026` — Passerelles d’interfaces réglementées pour le partage financier ouvert et les tiers accrédités
- **Emplacement :** `acces`
- **Description :** Opère les interfaces normalisées à haute disponibilité pour les tiers accrédités du cadre bancaire ouvert et les réseaux externes, vérifie l’accréditation en temps réel et tient le registre des consentements.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Disponibilité de 99,5 % et registre quinquennal de consentement du cadre bancaire ouvert canadien A [9] [10].
- **Preuve d’atteinte :** Disponibilité mensuelle d’au moins 99,5 % en pré-production et révocation immédiate d’un consentement sur les jetons actifs.
- **Dépendances :** `CAP-016`, `CAP-022`, `CAP-036`
- **Renvois :** C27, § 24.3, § 29.8, § 38.3, § 45.2; ADR-024, ADR-026; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-103` — Désignation officielle de la norme technique unique et ouverture réglementaire de l’accès en écriture.

### CAP-027 — Connecteurs d’espaces de données fédérés sous politiques d’usage exécutables

P : CAP-027

- **Identifiant et nom :** `CAP-027` — Connecteurs d’espaces de données fédérés sous politiques d’usage exécutables
- **Emplacement :** `acces`

- **Description :** Encadre le partage inter-institutionnel (co-assurance, réassurance, antifraude, climat) par des connecteurs vérifiant l’identité légale partenaire et attachant des règles exécutables de non-réemploi.
- **Statut :** Conditionnelle (scénarios A, C)
- **Palier d’atteinte :** P3
- **Motif :** Partage régulé de données sensibles sans perte de gouvernance entre institutions partenaires D [21] (C27, § 37.2, § 37.3, § 45.2).
- **Preuve d’atteinte :** Application technique prouvée d’une clause d’expiration et de non-entraînement lors d’un échange bilatéral simulé.
- **Dépendances :** `CAP-021`, `CAP-026`, `CAP-041`
- **Renvois :** C27, § 37.2, § 37.3, § 37.4, § 45.2; ADR-026; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-110` — Adoption de contrats d’usage machine-lisibles dans les consortiums sectoriels d’assurance et de finance.

### CAP-028 — Sas déterministe pour flux physiques ou télématiques et continuité locale hors réseau

P : CAP-028

- **Identifiant et nom :** `CAP-028` — Sas déterministe pour flux physiques ou télématiques et continuité locale hors réseau
- **Emplacement :** `acces`
- **Description :** Lit les capteurs et flux télématiques sur réplica isolé sans écriture directe vers les automates, et permet aux équipes terrain en zone sinistrée d’opérer hors réseau sur quotas réconciliables.
- **Statut :** Conditionnelle (scénarios B, C)
- **Palier d’atteinte :** P2
- **Motif :** Continuité d’indemnisation lors de catastrophes majeures et sûreté des interfaces physiques [4] [20] (C27, § 28.4, § 46.5).
- **Preuve d’atteinte :** Exercice hors réseau réussi avec réconciliation sans double paiement au retour de liaison et zéro canal d’écriture physique.
- **Dépendances :** `CAP-009`, `CAP-022`
- **Renvois :** C27, § 28.1, § 28.4, § 46.5, § 46.8; ADR-017, ADR-028; Cadre 2026, Plan A, Plan B
- **Signal de révision :** `SIG-109` — Publication de directives actualisées sur la télématique d’assurance et la résilience aux catastrophes.

## 10.5 Couche 5 — Modèles et exécution (`CAP-029` à `CAP-034`)

Pour contrer simultanément la dérive des coûts [36], le risque de fournisseur unique [2] [4] et la fuite d’état hors juridiction [15] (C27, ch. 44, ch. 46), ces six capacités instituent routage tri-palier, bacs à sable étanches, maîtrise des six substrats d’état, repli vers poids ouverts, enclaves attestées et distillation purifiée [34].

### CAP-029 — Plan de données d’inférence, routage cognitif à trois paliers et affinité de cache

P : CAP-029

- **Identifiant et nom :** `CAP-029` — Plan de données d’inférence, routage cognitif à trois paliers et affinité de cache
- **Emplacement :** `modeles`
- **Description :** Unifie l’accès aux modèles derrière un plan de données qui route les classes qualifiées vers de petits modèles, réserve les grands modèles aux cas complexes et ordonnance par affinité de préfixe.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Maîtrise de la latence, du coût par résultat et du risque de fournisseur unique [2] [36] (C27, § 40.6, § 44.1, § 44.3).
- **Preuve d’atteinte :** Bascule de modèle par simple configuration sans retouche du code d’agent et suivi du gain de cache.
- **Dépendances :** `CAP-017`, `CAP-042`
- **Renvois :** C27, § 40.6, § 44.1, § 44.3, § 44.4, § 44.5; ADR-014; Cadre 2026, Plan B
- **Signal de révision :** `SIG-015` — Hausse sur deux trimestres du coût complet par résultat réussi malgré la baisse du prix facial du jeton.

### CAP-030 — Confinement d’exécution en bac à sable isolé matériellement sans réseau sortant

P : CAP-030

- **Identifiant et nom :** `CAP-030` — Confinement d’exécution en bac à sable isolé matériellement sans réseau sortant
- **Emplacement :** `modeles`
- **Description :** Exécute tout code généré, calcul ad hoc ou analyse de fichier externe dans un bac à sable éphémère isolé matériellement ou par capacités mémoire, sans réseau sortant et détruit après usage.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Blocage des évasions de confinement et exécutions arbitraires observées en 2026 [3] (C27, § 31.2, § 32.3, § 49.7).
- **Preuve d’atteinte :** Échec à 100 % des tentatives de sortie réseau, de persistance locale et de lecture de secrets hôtes en test d’intrusion.
- **Dépendances :** `CAP-022`
- **Renvois :** C27, § 31.2, § 32.1, § 32.3, § 49.7; ADR-020; Cadre 2026, Plan A
- **Signal de révision :** `SIG-101` — Renforcement des contrôles techniques exigés par le BSIF sur l’exécution de code par des agents.

### CAP-031 — Continuité cognitive bimodèle et bascule éprouvée vers un profil à poids ouverts

P : CAP-031

- **Identifiant et nom :** `CAP-031` — Continuité cognitive bimodèle et bascule éprouvée vers un profil à poids ouverts
- **Emplacement :** `modeles`
- **Description :** Homologue pour chaque processus critique de classe 3 à 5 au moins deux familles indépendantes de modèles, dont un profil souverain à poids ouverts testé trimestriellement en bascule réelle.

- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Continuité des opérations critiques et maîtrise du risque de concentration sous BSIF E-21 et B-10 [2] [4] (C27, § 27.5, § 46.4).
- **Preuve d’atteinte :** Exercice trimestriel de bascule complète vers le profil de repli dans le délai homologué au seuil de constance requis.
- **Dépendances :** `CAP-018`, `CAP-029`, `CAP-043`, `CAP-051`
- **Renvois :** C27, § 27.5, § 44.6, § 46.4; ADR-027; Cadre 2026, Plan B, Plan C
- **Signal de révision :** `SIG-002` — Nouvelles obligations réglementaires sur la concentration des fournisseurs critiques de modèles.

### CAP-032 — Cloisonnement juridictionnel des six substrats d’état et maîtrise souveraine des clés

P : CAP-032

- **Identifiant et nom :** `CAP-032` — Cloisonnement juridictionnel des six substrats d’état et maîtrise souveraine des clés
- **Emplacement :** `modeles`
- **Description :** Localise par juridiction les six substrats d’état d’un agent (journaux, mémoires, caches, traces, files, sauvegardes) sous clés détenues en module matériel par l’institution et pseudonymisation amont.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Conformité des transferts selon l’article 17 de la Loi 25 et protection face aux lois extraterritoriales [2] [3] [15] (C27, § 38.6, § 46.1).
- **Preuve d’atteinte :** Inventaire automatisé des six substrats par flux et illisibilité prouvée des états après révocation de la clé cliente.
- **Dépendances :** `CAP-021`
- **Renvois :** C27, § 37.1, § 37.5, § 38.6, § 46.1, § 46.3; ADR-027; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-107` — Évolution des règles canadiennes et québécoises de transfert transfrontalier de renseignements personnels.

### CAP-033 — Inférence confidentielle en enclave matérielle attestée sur processeurs et accélérateurs

P : CAP-033

- **Identifiant et nom :** `CAP-033` — Inférence confidentielle en enclave matérielle attestée sur processeurs et accélérateurs
- **Emplacement :** `modeles`
- **Description :** Exécute l’inférence des charges les plus sensibles dans des enclaves matérielles chiffrant mémoire vive et bus d’accélérateurs, avec libération des clés conditionnée à l’attestation silicium.
- **Statut :** Conditionnelle (scénarios B, C)
- **Palier d’atteinte :** P2
- **Motif :** Isolation matérielle face à l’opérateur d’hébergement sur dossiers médicaux, actuariels ou stratégiques (C27, § 45.5, § 46.2).
- **Preuve d’atteinte :** Vérification cryptographique de l’attestation matérielle avant déchiffrement et tenue du budget de latence.

- **Dépendances :** `CAP-029`, `CAP-032`
- **Renvois :** C27, § 37.5, § 45.5, § 46.2, § 46.3; ADR-027; Cadre 2026, Plan A
- **Signal de révision :** `SIG-016` — Disponibilité régionale et coût énergétique des grappes d’accélérateurs dotées d’enclaves confidentielles.

### CAP-034 — Compilation déclarative des consignes et distillation contrôlée sous sas anti-renseignements personnels

P : CAP-034

- **Identifiant et nom :** `CAP-034` — Compilation déclarative des consignes et distillation contrôlée sous sas anti-renseignements personnels
- **Emplacement :** `modeles`
- **Description :** Gère des consignes compilables et encadre toute distillation vers petits modèles par un sas irréversible de purge des renseignements personnels, une porte de parité multi-essais et une sentinelle continue.
- **Statut :** Conditionnelle (scénarios B, C)
- **Palier d’atteinte :** P2
- **Motif :** Sobriété économique et électrique sur forts volumes répétitifs dans le respect de la Loi 25 [15] [34] [36] (C27, § 47.7, § 47.8).
- **Preuve d’atteinte :** Audit confirmant zéro renseignement personnel dans les jeux d’affinage et parité maintenue face au modèle de référence.
- **Dépendances :** `CAP-018`, `CAP-029`, `CAP-043`
- **Renvois :** C27, § 40.6, § 47.7, § 47.8; ADR-031; Cadre 2026, Plan B, Plan C
- **Signal de révision :** `SIG-015` — Écart économique observé entre le coût d’entretien d’une filière de distillation et le prix des petits modèles standards.

## 10.6 Plan de contrôle, volet 1 — Identité et sécurité (`CAP-035` à `CAP-041`)

Aligné sur le Plan A du Cadre 2026, ce volet déploie la confiance zéro non humaine [3] [5] (C27, ch. 29 à 32) : identités parrainées sans secret statique, délégation atténuée [25] [26], politiques déterministes hors modèle, décontamination d’entrées, coupe-circuit [4], agilité post-quantique [29] [30] [31] et mandats externes [27] [32].

### CAP-035 — Identités non humaines uniques par classe d’agent, parrainage nominatif et attestations éphémères

P : CAP-035

- **Identifiant et nom :** `CAP-035` — Identités non humaines uniques par classe d’agent, parrainage nominatif et attestations éphémères
- **Emplacement :** `controle-identite-securite`
- **Description :** Délivre à chaque classe d’agent une identité cryptographique distincte rattachée dans le système RH à un parrain métier actif, authentifiée uniquement par attestations courtes sans secret statique, et automatise à 100 % le renouvellement des certificats TLS et d’identités machines sous la limite de 47 jours.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1

- **Motif :** Imputabilité des modèles autonomes sous BSIF E-23 dès le 1er mai 2027 D [1], gestion des comptes système et de service sous BSIF B-13 (§ 3.2.7) [3] et identités non humaines recommandées par le bulletin du BSIF de juillet 2026 [5] (C27, § 29.2, § 29.4).
- **Preuve d’atteinte :** Zéro secret statique ou compte partagé en production, suspension automatique vérifiée sur vacance de parrainage et renouvellement automatisé à 100 % des certificats TLS sous cycle maximal de 47 jours avant le 15 mars 2029 (`ANC-030`).
- **Dépendances :** `CAP-047`
- **Renvois :** C27, § 29.1, § 29.2, § 29.3, § 29.4, § 39.3; ADR-018, ADR-025; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-101` — Formalisation prudentielle d’exigences dédiées aux identités non humaines d’agents par le BSIF.

### CAP-036 — Délégation cryptographique à portée atténuée par saut et preuve de possession

P : CAP-036

- **Identifiant et nom :** `CAP-036` — Délégation cryptographique à portée atténuée par saut et preuve de possession
- **Emplacement :** `controle-identite-securite`
- **Description :** Impose à chaque saut entre usager, orchestrateur, sous-agent et outil un échange de jeton qui conserve l’initiateur, empile les mandataires, réduit l’audience et lie l’usage au canal chiffré.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Prévention du délégué confus et de l’escalade transitive de droits dans les chaînes d’agents [25] [26] (C27, § 29.5, § 30.2, § 30.3).
- **Preuve d’atteinte :** Rejet à 100 % des tentatives de rejeu sur audience tierce ou d’élargissement de portée en test d’intrusion.
- **Dépendances :** `CAP-035`
- **Renvois :** C27, § 29.5, § 30.1, § 30.2, § 30.3; ADR-018; Cadre 2026, Plan A
- **Signal de révision :** `SIG-003` — Passage en norme officielle IETF des profils d’assertion d’identité et de jetons de transaction pour agents.

### CAP-037 — Point de décision de politique déterministe hors modèle et preuve formelle d’invariants

P : CAP-037

- **Identifiant et nom :** `CAP-037` — Point de décision de politique déterministe hors modèle et preuve formelle d’invariants
- **Emplacement :** `controle-identite-securite`
- **Description :** Évalue hors modèle chaque appel mutatif, accès sensible ou délégation dans un moteur de politiques déclaratif versionné dont les interdictions cardinales sont prouvées formellement avant livraison.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Nécessité de contrôles déterministes inviolables par invite adverse sous BSIF E-23 et B-13 D [1] [3] (C27, § 22.4, § 30.6, § 32.1).

- **Preuve d’atteinte :** Vérification formelle automatisée des clauses d’interdiction en chaîne de livraison et décision sous la milliseconde.
- **Dépendances :** Aucune (socle autonome du plan de contrôle)
- **Renvois :** C27, § 22.4, § 30.5, § 30.6, § 32.1, § 32.2; ADR-020; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-008` — Publication de contrôles certifiables dédiés aux garde-fous déterministes d’agents dans les normes internationales.

### CAP-038 — Décontamination des entrées externes non fiables et défense contre les menaces agentiques

P : CAP-038

- **Identifiant et nom :** `CAP-038` — Décontamination des entrées externes non fiables et défense contre les menaces agentiques
- **Emplacement :** `controle-identite-securite`
- **Description :** Maintient la modélisation des dix menaces agentiques, isole la lecture des pièces externes dans un extracteur sans outils mutatifs, marque leur provenance non fiable et exécute des tests adverses continus.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Défense contre le détournement d’objectif par injection indirecte dans les pièces clients ou sinistres [3] (C27, § 31.2, § 31.4, § 32.5).
- **Preuve d’atteinte :** Zéro invocation mutative non autorisée sur corpus d’injections documentaires rejoué à chaque déploiement.
- **Dépendances :** `CAP-022`, `CAP-037`
- **Renvois :** C27, § 31.1, § 31.2, § 31.4, § 31.6, § 31.8, § 32.5; ADR-019; Cadre 2026, Plan A
- **Signal de révision :** `SIG-101` — Évolution des attentes de tests adverses continus formulées par les superviseurs financiers.

### CAP-039 — Coupe-circuit opérationnel hiérarchisé et révocation instantanée des sessions et jetons

P : CAP-039

- **Identifiant et nom :** `CAP-039` — Coupe-circuit opérationnel hiérarchisé et révocation instantanée des sessions et jetons
- **Emplacement :** `controle-identite-securite`
- **Description :** Relie orchestrateurs, passerelles et identités au centre de sécurité pour permettre en quelques secondes le passage en lecture seule, la révocation en cascade des jetons ou le repli manuel d’un domaine.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Arrêt d’urgence des défaillances en cascade et résilience sous BSIF E-21 et E-23 D [1] [4] (C27, § 32.3, § 34.6).
- **Preuve d’atteinte :** Exercice trimestriel chronométré prouvant l’arrêt des mutations et la révocation des jetons en moins de dix secondes.
- **Dépendances :** `CAP-008`, `CAP-022`, `CAP-036`
- **Renvois :** C27, § 32.3, § 34.6; ADR-020; Cadre 2026, Plan A, Plan B

- **Signal de révision :** `SIG-014` — Détection d’incidents de propagation rapide d’erreurs sur des chaînes d’orchestration.

### CAP-040 — Agilité cryptographique, inventaire CBOM et transition post-quantique (ML-DSA et SLH-DSA)

P : CAP-040

- **Identifiant et nom :** `CAP-040` — Agilité cryptographique, inventaire CBOM et transition post-quantique (ML-DSA et SLH-DSA)
- **Emplacement :** `controle-identite-securite`
- **Description :** Inventorie toutes les primitives cryptographiques (`CBOM`) des identités, jetons et journaux d’agents et orchestre, sur le socle PKI automatisé à 47 jours établi en Palier 1 (`CAP-035`), la bascule hybride puis post-quantique native vers `ML-DSA` et `SLH-DSA`.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Certificats courts dès 2027-2029 et feuille de route post-quantique financière du G7 sur 2030-2032 vers 2035 D A [29] [30] [31] (C27, § 49.5).
- **Preuve d’atteinte :** Inventaire cryptographique automatisé (`CBOM`) complet, essai concluant de jetons délégués et certificats hybrides `ML-DSA` et double scellement `SLH-DSA` des archives longues.
- **Dépendances :** `CAP-035`, `CAP-036`
- **Renvois :** C27, § 29.4, § 29.5, § 49.5; ADR-006, ADR-018; Cadre 2026, Plan A
- **Signal de révision :** `SIG-009` — Transformation de la feuille de route post-quantique financière du G7 en exigence prudentielle contraignante au Canada.

### CAP-041 — Identité légale d’organisation vérifiable et justificatifs cryptographiques de mandat externe

P : CAP-041

- **Identifiant et nom :** `CAP-041` — Identité légale d’organisation vérifiable et justificatifs cryptographiques de mandat externe
- **Emplacement :** `controle-identite-securite`
- **Description :** Émet, vérifie et révoque des justificatifs cryptographiques reliant un agent externe à l’identité légale vérifiée de son entreprise, au signataire habilité et aux plafonds exacts de son mandat.
- **Statut :** Conditionnelle (scénarios A, C)
- **Palier d’atteinte :** P3
- **Motif :** Sécurisation juridique du mandat lors d’échanges inter-entreprises avec courtiers, banques et prestataires [27] [32] (C27, § 29.8, § 36.2, § 45.3).
- **Preuve d’atteinte :** Vérification hors ligne de la chaîne entité légale — signataire — agent et rejet immédiat de tout mandat hors bornes.
- **Dépendances :** `CAP-036`, `CAP-040`
- **Renvois :** C27, § 10.2, § 29.8, § 36.2, § 45.3; ADR-024, ADR-026; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-007` — Adoption d’un profil normatif de mandat d’agent vérifiable par un réseau de paiement ou un superviseur du G7.

## 10.7 Plan de contrôle, volet 2 — Observabilité, évaluation et FinOps (`CAP-042` à `CAP-046`)

Aligné sur le Plan B du Cadre 2026, ce volet rend les flottes auditables et économiquement gouvernables (C27, ch. 33, ch. 34, ch. 40) : traces causales à double couloir [15] [28], qualification multi-essais face à la saturation des bancs publics [1] [35], budgets d’erreur, coût complet par résultat [36] et empreinte carbone de portée 3 [21] [34].

### CAP-042 — Télémétrie causale distribuée normalisée au collecteur et double couloir de confidentialité

P : CAP-042

- **Identifiant et nom :** `CAP-042` — Télémétrie causale distribuée normalisée au collecteur et double couloir de confidentialité
- **Emplacement :** `controle-observabilite-finops`
- **Description :** Propage l’identifiant de trace à travers agents et outils, normalise au collecteur vers un schéma interne stable et sépare la télémétrie assainie sans données personnelles de la voûte forensique chiffrée.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Auditabilité de bout en bout sans fuite de renseignements personnels sous Loi 25 [15] [28] (C27, § 33.2, § 33.3, § 33.4).
- **Preuve d’atteinte :** Graphe causal complet reconstitué par transaction et zéro renseignement personnel en clair dans l’index général.
- **Dépendances :** `CAP-032`
- **Renvois :** C27, § 33.1, § 33.2, § 33.3, § 33.4; ADR-021; Cadre 2026, Plan B
- **Signal de révision :** `SIG-006` — Passage au statut stable des conventions sémantiques d’observabilité dédiées aux agents et aux protocoles d’outils.

### CAP-043 — Qualification pré-production par simulation multi-tours répétée, chaos et déploiement progressif

P : CAP-043

- **Identifiant et nom :** `CAP-043` — Qualification pré-production par simulation multi-tours répétée, chaos et déploiement progressif
- **Emplacement :** `controle-observabilite-finops`
- **Description :** Conditionne toute mise en service à un seuil de constance multi-essais sur banc de simulation métier interne, à l’injection de pannes, puis à un mode fantôme sans mutation suivi d’un canari.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Saturation des bancs publics et exigence de qualification pré-production sous BSIF E-23 D [1] [35] (C27, § 33.7, § 34.2, § 49.2).
- **Preuve d’atteinte :** Blocage automatique en livraison de tout candidat sous le seuil de constance multi-essais ou de survie aux pannes.
- **Dépendances :** `CAP-018`, `CAP-042`
- **Renvois :** C27, § 33.5, § 33.6, § 33.7, § 34.2, § 48.5, § 49.2; ADR-022; Cadre 2026, Plan B, Plan C

- **Signal de révision :** `SIG-013` — Apparition de nouvelles méthodes homologuées d’évaluation de fiabilité sur longues trajectoires métiers.

### CAP-044 — Surveillance continue en production, détection de dérive et pilotage par budgets d’erreur

P : CAP-044

- **Identifiant et nom :** `CAP-044` — Surveillance continue en production, détection de dérive et pilotage par budgets d’erreur
- **Emplacement :** `controle-observabilite-finops`
- **Description :** Suit en continu les indicateurs de résultat métier réel (réouvertures, infirmations humaines, dérive sémantique) et relie la consommation du budget d’erreur au maintien ou au retrait d’autonomie.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Surveillance continue de la performance et de la dérive des systèmes autonomes sous BSIF E-23 D [1] (C27, § 34.3, § 34.4, § 34.7).
- **Preuve d’atteinte :** Abaissement automatique de classe d’autonomie déclenché lors d’une dégradation simulée du taux de dossiers conformes.
- **Dépendances :** `CAP-042`, `CAP-048`
- **Renvois :** C27, § 34.3, § 34.4, § 34.5, § 34.7; ADR-021, ADR-022; Cadre 2026, Plan B, Plan C
- **Signal de révision :** `SIG-101` — Durcissement des indicateurs continus de surveillance opérationnelle attendus par les superviseurs.

### CAP-045 — Pilotage économique par le coût complet du résultat conforme et disjoncteurs budgétaires

P : CAP-045

- **Identifiant et nom :** `CAP-045` — Pilotage économique par le coût complet du résultat conforme et disjoncteurs budgétaires
- **Emplacement :** `controle-observabilite-finops`
- **Description :** Mesure par processus le coût complet par résultat conforme non rouvert face à une base non agentique, arme des disjoncteurs par transaction, affiche puis refacture les coûts et déclasse les flux déficitaires.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Multiplication des coûts réels en multi-agents malgré la baisse du prix facial du jeton [36] (C27, § 40.2, § 40.5, § 50.7).
- **Preuve d’atteinte :** Imputation mensuelle de 100 % des coûts complets aux clôtures validées et coupure prouvée sur dépassement d’enveloppe.
- **Dépendances :** `CAP-022`, `CAP-029`, `CAP-042`
- **Renvois :** C27, § 40.1, § 40.2, § 40.3, § 40.5, § 50.7; ADR-023; Cadre 2026, Plan B
- **Signal de révision :** `SIG-015` — Divergence persistante entre le prix facial au million de jetons et le coût complet par dossier résolu.

### CAP-046 — Comptabilisation énergétique et carbone des charges d’inférence et des fournisseurs

P : CAP-046

- **Identifiant et nom :** `CAP-046` — Comptabilisation énergétique et carbone des charges d’inférence et des fournisseurs
- **Emplacement :** `controle-observabilite-finops`
- **Description :** Mesure la consommation électrique et l’intensité carbone des charges d’inférence internes et tierces par domaine, intègre ce critère au routage et alimente la reddition climatique annuelle.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P2
- **Motif :** Tension électrique projetée par l’AIE et divulgation des émissions de portée 3 dès l’exercice 2028 sous BSIF B-15 D [21] [34] (C27, § 40.1).
- **Preuve d’atteinte :** Consolidation auditable des émissions liées aux plateformes d’IA dans le rapport climatique réglementaire annuel.
- **Dépendances :** `CAP-029`, `CAP-045`
- **Renvois :** C27, § 40.1, § 40.2, § 44.3; ADR-023; Cadre 2026, Plan B, Plan C
- **Signal de révision :** `SIG-016` — Apparition de contraintes régionales de raccordement électrique ou de surtarification énergétique de l’inférence.

## 10.8 Plan de contrôle, volet 3 — Gouvernance et registre (`CAP-047` à `CAP-052`)

Aligné sur le Plan C du Cadre 2026, ce volet outille les trois lignes de défense [1] [17] : inventaire central et blocage réseau, plafonds d’autonomie et maintien des compétences [33], qualification juridictionnelle distinguant institutions privées et administrations publiques [12] [15] [23], revue indépendante, réversibilité des tiers [2] [24] et ingénierie à séparation des tâches.

### CAP-047 — Registre central d’inventaire, de cote de risque inhérent et de blocage des agents non homologués

P : CAP-047

- **Identifiant et nom :** `CAP-047` — Registre central d’inventaire, de cote de risque inhérent et de blocage des agents non homologués
- **Emplacement :** `controle-gouvernance-registre`
- **Description :** Maintient l’inventaire d’entreprise unique des agents, modèles, outils et compétences, calcule leur cote de risque inhérent selon l’autonomie, fige leurs manifestes et bloque tout agent non inscrit.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Inventaire exhaustif et classification du risque intégrant l’autonomie exigés par BSIF E-23 au 1er mai 2027 D [1] (C27, § 8.7, § 39.1).
- **Preuve d’atteinte :** 100 % des flux d’agents sur le réseau rattachés à une fiche active dotée d’un propriétaire et d’une cote validée.
- **Dépendances :** Aucune (registre fondateur du plan de contrôle)
- **Renvois :** C27, § 8.6, § 8.7, § 23.4, § 39.1, § 39.2, § 43.2; ADR-003; Cadre 2026, Plan C
- **Signal de révision :** `SIG-008` — Publication d’un référentiel normatif international d’inventaire et de certification des systèmes agentiques.

### CAP-048 — Gouvernance dynamique de l’autonomie par domaine et par classe de décision avec maintien des compétences humaines

P : CAP-048

- **Identifiant et nom :** `CAP-048` — Gouvernance dynamique de l’autonomie par domaine et par classe de décision avec maintien des compétences humaines
- **Emplacement :** `controle-gouvernance-registre`
- **Description :** Applique pour chaque couple domaine (D1 à D8) et classe de décision (1 à 6) le plafond d’autonomie et de rétrogradation, subordonné au maintien vérifié de la compétence humaine de contre-expertise.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Autonomie méritée et prévention de l’atrophie des compétences internes de reprise D [1] [33] (C27, § 22.3, § 22.4, § 41.5, § 43.1).
- **Preuve d’atteinte :** Application technique de la matrice des plafonds et réussite d’un exercice annuel de reprise manuelle sans agent.
- **Dépendances :** `CAP-037`, `CAP-047`
- **Renvois :** C27, § 22.3, § 22.4, § 39.3, § 41.5, § 43.1; ADR-025; Cadre 2026, Plan C
- **Signal de révision :** `SIG-017` — Contraction de la relève qualifiée compromettant la capacité réelle de contre-expertise et de reprise humaine.

### CAP-049 — Qualification réglementaire par empreinte juridictionnelle et archivage probatoire intègre

P : CAP-049

- **Identifiant et nom :** `CAP-049` — Qualification réglementaire par empreinte juridictionnelle et archivage probatoire intègre
- **Emplacement :** `controle-gouvernance-registre`
- **Description :** Calcule en livraison l’empreinte juridictionnelle selon le maillon le plus strict, vérifie l’ÉFVP requise et archive sur support non réinscriptible les preuves d’explicabilité, de consentement et d’audit.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Cumul des obligations fédérales, québécoises et européennes visant les institutions privées, distinctes des échéances propres aux administrations D A [1] [10] [12] [15] [23].
- **Preuve d’atteinte :** Blocage de tout déploiement sans pièces réglementaires requises et restitution d’un dossier probatoire en moins de quatre heures.
- **Dépendances :** `CAP-042`, `CAP-047`
- **Renvois :** C27, § 17.7, § 35.1, § 35.4, § 38.3, § 38.4, § 38.7; ADR-024; Cadre 2026, Plan C
- **Signal de révision :** `SIG-001` — Extension des cas d’usage financiers classés à haut risque par la réglementation européenne ou canadienne.

### CAP-050 — Validation indépendante de deuxième ligne et assurance d’audit interne des trois lignes

P : CAP-050

- **Identifiant et nom :** `CAP-050` — Validation indépendante de deuxième ligne et assurance d’audit interne des trois lignes

- **Emplacement :** `controle-gouvernance-registre`
- **Description :** Donne à la deuxième ligne de risque de modèles et à l’audit interne un accès autonome en lecture aux registres, bancs scellés et traces forensiques, interdisant toute auto-homologation par les concepteurs.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Revue indépendante et gouvernance des trois lignes de défense sous BSIF E-23 et principes AICA D [1] [17] (C27, § 38.3, § 39.6).
- **Preuve d’atteinte :** Certificat de validation indépendante de deuxième ligne présent pour 100 % des agents de risque élevé ou de classes 3 à 5.
- **Dépendances :** `CAP-043`, `CAP-047`, `CAP-049`
- **Renvois :** C27, § 38.3, § 39.4, § 39.6; ADR-022, ADR-024; Cadre 2026, Plan C
- **Signal de révision :** `SIG-102` — Publication ou durcissement des attentes québécoises de gouvernance et de validation indépendante des modèles.

### CAP-051 — Gouvernance des tiers, clauses contractuelles de sortie, notification et réversibilité éprouvée

P : CAP-051

- **Identifiant et nom :** `CAP-051` — Gouvernance des tiers, clauses contractuelles de sortie, notification et réversibilité éprouvée
- **Emplacement :** `controle-gouvernance-registre`
- **Description :** Impose aux contrats de plateformes et de modèles la notification des fonctions autonomes, l’interdiction d’entraînement sur données clientes, l’exportation sans frais prohibitifs et des essais de sortie.
- **Statut :** Invariante (scénarios A, B, C)
- **Palier d’atteinte :** P1
- **Motif :** Gestion des tiers sous BSIF B-10, notification relevée en juillet 2026 et suppression européenne des frais de bascule D [2] [5] [24] (C27, § 27.5).
- **Preuve d’atteinte :** Clauses de notification et de réversibilité dans 100 % des contrats renouvelés et essai annuel documenté d’extraction.
- **Dépendances :** `CAP-018`, `CAP-047`
- **Renvois :** C27, § 27.3, § 27.5, § 36.5, § 36.6; ADR-004, ADR-027; Cadre 2026, Plan C
- **Signal de révision :** `SIG-002` — Renforcement de la supervision directe des fournisseurs tiers critiques de modèles et de plateformes.

### CAP-052 — Ingénierie logicielle, modernisation patrimoniale et exploitation assistées à séparation des tâches

P : CAP-052

- **Identifiant et nom :** `CAP-052` — Ingénierie logicielle, modernisation patrimoniale et exploitation assistées à séparation des tâches
- **Emplacement :** `controle-gouvernance-registre`
- **Description :** Sépare techniquement les droits de l’agent d’oracle de test et de l’agent codeur, exige tests de mutation et parité en miroir sans écart en modernisation patrimoniale, et proscrit tout shell libre en production.
- **Statut :** Invariante (scénarios A, B, C)

- **Palier d’atteinte :** P2
- **Motif :** Modernisation sûre des systèmes centraux et parade à l’auto-approbation ou aux incidents d’exploitation [3] [4] (C27, § 25.3, § 47.1, § 47.4, § 47.6).
- **Preuve d’atteinte :** Impossibilité technique pour l’agent bâtisseur de modifier les tests d’acceptation ou d’ouvrir un shell, et rapport miroir à zéro écart.
- **Dépendances :** `CAP-024`, `CAP-030`, `CAP-037`
- **Renvois :** C27, § 25.3, § 47.1, § 47.3, § 47.4, § 47.6; ADR-029, ADR-030; Cadre 2026, Plan A, Plan C
- **Signal de révision :** `SIG-017` — Évolution de la disponibilité d’experts humains capables de qualifier les migrations de systèmes patrimoniaux.

## 10.9 Articulation transversale des capacités d’échange entre organisations

Dans le modèle de maturité retenu (C27, § 43.1), l’ouverture au **Stade 4 (Échange entre organisations)** résulte de l’assemblage indissociable de six capacités réparties sur quatre couches et volets :

1. **Authentification des agents externes sur portails publics (**`CAP-006`**)**, distinguant un mandataire légitime du grattage d’écran interdit par le cadre bancaire ouvert [9] (C27, § 9.4).
2. **Passerelles d’interfaces réglementées à haute disponibilité (**`CAP-026`**)**, assurant dès `P2` la disponibilité de 99,5 %, le contrôle d’accréditation et le registre quinquennal des consentements [9] [10], ainsi que les flux avec les réseaux de courtage [13] [16].
3. **Identité légale d’organisation vérifiable et justificatifs de mandat (**`CAP-041`**)**, reliant l’agent externe à l’entité morale mandante et aux plafonds autorisés [27] [32] (C27, § 29.8, § 45.3).
4. **Connecteurs d’espaces de données fédérés (**`CAP-027`**)**, attachant des règles d’usage et de non-réentraînement en co-assurance, réassurance, antifraude ou données climatiques [21] (C27, § 37.3, § 45.2).
5. **Sas à séparation diplomate externe / évaluateur interne (**`CAP-014`**)**, isolant les prix de réserve et soumettant tout décaissement à un rapprochement tripartite hors modèle (C27, § 45.4, § 45.7).
6. **Agilité cryptographique post-quantique (**`CAP-040`**) et archivage probatoire (**`CAP-049`**)**, préservant sur longue durée la valeur juridique des engagements et consentements inter-entreprises [12] [29] [31].

## Limites

1. **Clôture sectorielle et grilles analytiques.** L’épreuve des cinq profils sectoriels (`M-14` à `M-18`, synthétisée au chapitre `M-19`) a confirmé que ces cinquante-deux fiches couvrent l’ensemble des exigences sans capacité manquante; par ailleurs, le découpage en six substrats d’état repris dans `CAP-032` (`C27, § 46.1`) demeure une grille analytique d’inventaire propre à l’ouvrage 2027.

2. **Absence du répertoire** `../2026/`**.** Le champ *Renvois* pointe vers les plans transversaux attestés (`Plan A`, `Plan B`, `Plan C`) sans identifiant individuel `EXIG-…`.
3. **Référentiels sous adhésion et PDF fermés.** Les schémas complets `FDX`, `ACORD` et `CSIO` (à la différence des métadonnées `FIBO` [14]), l’avis télématique québécois de 2015 (`N-03`) ainsi que les cinq lignes directrices en PDF de l’AMF (`T-01` sur l’IA, `T-02` sur les modèles, `T-14` et `T-15` sur les technologies et la continuité, `T-13` sur la conduite commerciale) restent classés fermés (`F`) sans appuyer aucune obligation `[N]`.

## Sources

1. BSIF, *Ligne directrice E-23 — Gestion du risque lié aux modèles (2027)*, 2025-09-11, lu le 2026-11-16, lu en entier, statut L+, texte : T-05.txt.
2. BSIF, *Ligne directrice B-10 — Gestion du risque lié aux tiers*, 2023-04-30, lu le 2026-11-16, lu en entier, statut L+, texte : T-06.txt.
3. BSIF, *Ligne directrice B-13 — Gestion du risque lié aux technologies et au cyberrisque*, 2022-07-31, lu le 2026-11-16, lu en entier, statut L+, texte : T-07.txt.
4. BSIF, *Ligne directrice E-21 — Gestion du risque opérationnel et résilience opérationnelle*, 2024-08-22, lu le 2026-11-16, lu en entier, statut L+, texte : T-08.txt.
5. BSIF, *Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security, and Operational Resilience — Technology Risk Bulletin*, juillet 2026 (modifié le 2026-07-13), lu le 2026-11-16, lu en entier, statut L+, texte : T-09.txt.
6. Parlement du Canada, *Loi sur le recyclage des produits de la criminalité et le financement des activités terroristes* (*L.C. 2000, ch. 17*), à jour 2026-10-29, lu le 2026-11-16, lu par passages, statut L+, texte : T-10.txt.
7. ACFC, *The Financial Consumer Protection Framework: enhanced protection for bank customers*, 2025-10-16, lu le 2026-11-16, lu en entier, statut L+, texte : T-12.txt.
8. Gouverneur général en conseil, *Règlement sur le commerce de l’assurance — banques et sociétés de portefeuille bancaires* (*DORS/92-330*), à jour 2026-10-29, lu le 2026-11-16, lu en entier, statut L+, texte : T-17.txt.
9. Parlement du Canada, *Loi sur les services bancaires axés sur les consommateurs* (*L.C. 2026, ch. 3*), 2026-03-26 (à jour 2026-10-29), lu le 2026-11-16, lu en entier, statut L+, texte : T-19.txt.
10. Ministère des Finances du Canada, *Projet de Règlement sur les services bancaires axés sur les consommateurs*, 2026-06-27, lu le 2026-11-16, lu en entier, statut L+, texte : T-20.txt.
11. Paiements Canada, *Système RTR — Spécifications ISO 20022 v1.4*, 2025-05-30, lu le 2026-11-16, lu en entier, statut L+, texte : T-21.txt.
12. OCRI, *Règles visant les courtiers en placement (règles 3100 à 3900)*, 2026-08-11, lu le 2026-11-16, lu par passages, statut L+, texte : T-23.txt.
13. CCRRA et OCRA, *Conduite des activités d’assurance et traitement équitable des clients*, en vigueur (référence novembre 2017), lu le 2026-11-16, lu en entier, statut L+, texte : T-27.txt.
14. EDM Council, *FIBO Metadata Specification*, lu le 2026-11-16, lu en entier, statut L+, texte : T-32.txt.
15. Parlement du Québec, *Loi 25 — L.Q. 2021, c. 25 modifiant RLRQ, c. P-39.1*, 2021-09-22, lu le 2026-11-16, lu par passages, statut L+, texte : QC-01.txt.
16. Parlement du Québec, *Loi sur les assureurs et LDPSF — L.Q. 2018, c. 23*, sanctionnée le 2018-06-13, lu le 2026-11-16, lu par passages, statut L+, texte : QC-03.txt.

17. AICA / IAIS, *Application Paper on the Supervision of Artificial Intelligence*, 2025-07-02, lu le 2026-11-16, lu en entier, statut L+, texte : CAN-02.txt.
18. Cour suprême du Canada, *Renvoi relatif à la Loi sur la non-discrimination génétique*, 2020 CSC 17, 2020-07-10, lu le 2026-11-16, lu par passages, statut L+, texte : CAN-03.txt.
19. Parlement du Canada, *Loi sur la non-discrimination génétique* (*L.C. 2017, ch. 3*), à jour 2026-10-29, lu le 2026-11-16, lu en entier, statut L+, texte : N-01.txt.
20. BSIF, *Ligne directrice B-9 — Exposition au risque de tremblement de terre*, 2013-02-28 (modifié le 2013-07-31), lu le 2026-11-16, lu en entier, statut L+, texte : N-04.txt.
21. BSIF, *Ligne directrice B-15 — Gestion des risques climatiques*, 2025-03-07 (mis à jour le 2026-01-08), lu le 2026-11-16, lu en entier, statut L+, texte : N-05.txt.
22. Projet A2A, *Agent2Agent Protocol Specification v1.0.0*, 2026, lu le 2026-11-16, lu en entier, statut L+, texte : N-09.txt.
23. Union européenne, *Règlement (UE) 2026/1744 du 8 juillet 2026 modifiant les échéances de l’AI Act*, JOUE du 2026-07-24, lu le 2026-11-16, lu en entier, statut L+, texte : P-02.txt.
24. Union européenne, *Règlement (UE) 2023/2854 (Data Act, art. 29)*, du 13 décembre 2023 (JOUE du 2023-12-22), lu le 2026-11-16, lu par passages, statut L+, texte : P-08.txt.
25. IETF WIMSE, *Charter & draft-ietf-wimse-aims-01*, révision 2026-11-02, lu le 2026-11-16, lu en entier, statut L+, texte : P-12.txt.
26. IETF OAuth, *ID-JAG-06 et profils d’échange de jetons (*`RFC 8693`*,* `RFC 9449`*)*, 2026-10-31, lu le 2026-11-16, lu en entier, statut L+, texte : P-13.txt.
27. W3C, *Verifiable Credentials Data Model v2.0*, 2025-05-15, lu le 2026-11-16, lu par passages, statut L+, texte : P-17.txt.
28. OpenTelemetry, *GenAI & Agentic Semantic Conventions (Status: Development)*, lu le 2026-11-16, lu par passages, statut L+, texte : P-19.txt.
29. G7 Cyber Expert Group, *Post-Quantum Cryptography Roadmap in the Financial Sector*, janvier 2026, lu le 2026-11-16, lu en entier, statut L+, texte : P-24.txt.
30. CA/Browser Forum, *Ballot SC-081v3 (TLS Certificate Validity)*, adoption du Ballot SC-081v3 le 2025-04-11, lu le 2026-11-16, lu par passages, statut L+, texte : P-26.txt.
31. IETF, *RFC 9964, RFC 10024 et RFC 10073 (PQC JOSE/COSE/X.509, publications mai à novembre 2026) et brouillon* `draft-uppalapati-wimse-pq-agent-identity`, 2026-10-27, lu le 2026-11-16, lu par passages, statut L+, texte : P-27.txt.
32. GLEIF, *Agentic AI in Payments: Establishing Interoperable Trust and Control* v1.0 (vLEI), 2026-08-13, lu le 2026-11-16, lu en entier, statut L+, texte : P-28.txt.
33. Statistique Canada, *Enquête sur l’IA en entreprise et programme TechStat*, 2026-06-11, lu le 2026-11-16, lu en entier, statut L+, texte : P-29.txt.
34. AIE, *Energy and AI Special Report*, avril 2025, lu le 2026-11-16, lu par passages, statut L+, texte : P-33.txt.
35. METR, *Measuring AI Ability to Complete Long Tasks (arrêt série initiale)*, 2026-09-08, lu le 2026-11-16, lu en entier, statut L+, texte : P-34.txt.
36. Stanford HAI, *AI Index Report*, 2026, lu le 2026-11-16, lu par passages, statut L+, texte : P-36.txt.
37. M. Pan et al., *Measuring Agents in Production (MAP)* (`arXiv:2512.04123`), et M. Cemri et al., *Why Do Multi-Agent LLM Systems Fail? (MAST)* (NeurIPS 2025), 2025-2026, lu le 2026-11-16, lu par passages, statut L+, texte : P-38.txt.
