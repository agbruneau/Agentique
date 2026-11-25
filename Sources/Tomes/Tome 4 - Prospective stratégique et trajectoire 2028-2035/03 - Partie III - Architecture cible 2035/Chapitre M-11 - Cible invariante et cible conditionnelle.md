# Chapitre M-11 — Cible invariante et cible conditionnelle

*Question directrice : Que bâtir quoi qu’il arrive, et que différer?*

> **État de référence (16 novembre 2026) :** La partition entre noyau invariant et options conditionnelles s’appuie sur les cinquante-deux capacités définies au chapitre M-10 (`capacites.json`), sur les scénarios A, B et C prolongés au chapitre M-8 à partir du Compendium 2027, sur la méthode des parcours adaptatifs sous incertitude profonde vérifiée sur texte primaire, ainsi que sur les échéances réglementaires et normatives arrêtées au 16 novembre 2026.

## 11.1 Décider sous incertitude profonde : coûts de transfert, noyau sans regret et options réelles

Le chapitre M-10 a recensé cinquante-deux capacités cibles (`CAP-001` à `CAP-052`) nécessaires pour exploiter des systèmes agentiques dans une institution financière canadienne ou québécoise sur la période 2028-2035. Or l’institution ignore lequel des trois scénarios du chapitre M-8 prévaudra : convergence ouverte des couches d’identité, de découverte et de télémétrie (**scénario A — Socle étendu**), coexistence durable de suites progicielles et infonuagiques enfermant chacune leur gouvernance (**scénario B — Archipel**), ou fragmentation marquée des régimes juridictionnels, cryptographiques et énergétiques (**scénario C — Blocs**) (C27, § 43.3). Dans les termes de la décision sous incertitude profonde (*Dynamic Adaptive Policy Pathways*), ces trois trajectoires ne reçoivent aucune distribution de probabilité fiable [1]; figer le plan directeur autour d’un seul scénario expose soit au surinvestissement prématuré, soit à un verrouillage dont les **coûts de transfert** (*transfer costs*) deviennent prohibitifs au moment de bifurquer [1].

Deux asymétries factuelles permettent toutefois de trancher dès maintenant. D’une part, la quasi-totalité des jalons réglementaires et techniques déjà **datés** entre 2027 et 2033 — entrée en vigueur de E-23 du BSIF le 1er mai 2027 D [2], application de l’Annexe III du règlement européen sur l’IA pour les institutions et administrations visées le 2 décembre 2027 D [3], suppression européenne des frais de changement d’infonuagique au 12 janvier 2027 D [4], divulgations climatiques de portée 3 dès l’exercice 2028 D [5], abaissement des certificats TLS publics à 100 puis 47 jours d’ici mars 2029 D [6], et temporisation des lois bancaires et d’assurances fédérales au 30 juin 2033 D [7] [21] — portent sur **la preuve, l’inventaire, l’imputabilité, la sécurité et la réversibilité**, jamais sur une obligation d’accroître l’autonomie. D’autre part, céder son registre d’agents, son identité ou sa piste d’audit au studio d’un fournisseur unique oblige à payer deux fois lors d’un changement de cap : réécrire les connecteurs métiers et reconstituer les preuves sous contrôle prudentiel [8] (C27, § 27.4, § 27.5).

L’architecture cible sépare donc **quarante-deux capacités invariantes** (`statut: "invariante"` dans `capacites.json`), qui forment l’investissement sans regret valide sous A, B et C, et **dix capacités conditionnelles** (`statut: "conditionnelle"`), préparées par des interfaces d’accueil légères mais déployées en capital uniquement lorsqu’un signal (`SIG-nnn`) franchit son seuil compte tenu du délai de mise en œuvre (*lead time*) [1].

> **[Figure]**
> - Matrice des capacités par scénario — Noyau sans regret (42) et options conditionnelles (10) Partie haute : bilan complet par emplacement · Partie basse : profil d’activation des capacités conditionnelles
> - Couche / Volet Invariantes Cond. Total A Total B Total C
> - Couche 1 — Interaction 4 2 6 6 4
> - Couche 2 — Agents et orchestration 6 2 7 8 7
> - Couche 3 — Contexte et connaissance 7 0 7 7 7
> - Couche 4 — Accès 4 3 5 6 7
> - Couche 5 — Modèles 4 2 4 6 6
> - Volet A — Identité et sécurité 6 1 7 6 7
> - Volet B — Observabilité et FinOps 5 0 5 5 5
> - Volet C — Gouvernance et registre 6 0 6 6 6
> - Total (52 capacités · P1 : 29 inv. / 1 cond.) 42 10 47 50 49
> - Détail des 10 capacités conditionnelles par scénario et signal de révision
> - ID Capacité conditionnelle Palier Scén. A Scén. B Scén. C Signal
> - CAP-004 Voix et multimodal temps réel P2 Requise Requise —SIG-102
> - CAP-006 Encadrement agents externes P3 Requise Requise —SIG-103
> - CAP-013 Fédération gravité données P2 —Requise Requise SIG-002
> - CAP-014 Négociation inter-organisations P3 Requise Requise —SIG-007
> - CAP-025 Harnais dérogatoire CUA (12 m) P1 —Requise Requise SIG-103
> - CAP-027 Connecteurs espaces fédérés P3 Requise —Requise SIG-110
> - CAP-028 Sas télématique/OT hors ligne P2 —Requise Requise SIG-109
> - CAP-033 Inférence confidentielle enclave P2 —Requise Requise SIG-016
> - CAP-034 Distillation sous sas anti-PII P2 —Requise Requise SIG-015
> - CAP-041 Identité légale et mandats tiers P3 Requise —Requise SIG-007
> - Scénarios : A = Socle étendu · B = Archipel · C = Blocs (29 des 30 capacités du Palier 1 appartiennent au noyau invariant).

*Fig. 4. – Matrice des capacités invariantes et conditionnelles selon les scénarios A, B et C.*

## 11.2 La cible invariante : les 42 capacités sans regret et la frontière de ce que l’institution possède

Parmi les quarante-deux capacités invariantes, toutes n’appellent pas le même mode d’appropriation. Prolongeant l’exposé sourcé du Compendium 2027 (C27, § 27.4) et le principe `PRI-015`, l’institution distingue trois régimes : **posséder en propre** le noyau de contrôle et de médiation garantissant son indépendance prudentielle; **consommer de façon interchangeable** les commodités cognitives et d’infrastructure derrière des contrats ouverts; et **fédérer** l’exécution locale près des systèmes métiers.

### Le noyau possédé en propre : plan de contrôle transversal et points de coupure

Un composant relève du noyau possédé dès lors que son enfermement chez un tiers compromettrait la conformité à E-23 [2], B-10 [8], B-13 [9], E-21 [10] ou la Loi 25 [11]. Ce noyau réunit les **dix-sept capacités invariantes du plan de contrôle** et les **vingt-cinq coupures déterministes des couches opérationnelles** :

1. **Gouvernance, inventaire et trois lignes de défense (`controle-gouvernance-registre` — 6 invariantes sur 6) :** registre central d’inventaire, de cote de risque et de blocage réseau (`CAP-047`), gouvernance dynamique des plafonds `D1`–`D8` × `Classe 1`–`Classe 6` et maintien des compétences humaines (`CAP-048`), qualification juridictionnelle et archivage probatoire intègre (`CAP-049`), outillage d’accès indépendant des 2e et 3e lignes (`CAP-050`), clauses contractuelles de notification et de sortie testée des tiers (`CAP-051`) [8] [12], et usine d’ingénierie logicielle et de modernisation patrimoniale à séparation des tâches (`CAP-052`) [9].
2. **Identité non humaine, politiques hors modèle et agilité cryptographique (`controle-identite-securite` — 6 invariantes sur 7) :** identités non humaines parrainées à attestations éphémères (`CAP-035`) [12], échange de jetons à portée atténuée par saut (`CAP-036`), point de décision déterministe hors modèle vérifié (`CAP-037`), décontamination des entrées externes (`CAP-038`), coupe-circuit opérationnel hiérarchisé (`CAP-039`), et agilité cryptographique préparant les certificats à 47 jours de 2029 D [6] ainsi que la migration post-quantique recommandée par le G7 financier sur 2030-2032 vers 2035 A [13] (`CAP-040`).
3. **Observabilité causale, qualification interne et pilotage économique (`controle-observabilite-finops` — 5 invariantes sur 5) :** télémétrie distribuée normalisée au collecteur avec double couloir protégeant les renseignements personnels (`CAP-042`) [11] [14], bancs métiers internes multi-essais et de chaos (`CAP-043`), surveillance continue de dérive liée aux budgets d’erreur (`CAP-044`), calcul du coût complet par résultat conforme avec disjoncteurs (`CAP-045`) (C27, § 40.5, § 50.7), et comptabilisation énergétique et carbone de l’inférence (`CAP-046`) [5] [15].
4. **Points de coupure invariants dans les cinq couches horizontales (25 capacités invariantes) :**
  - *Interaction (`CAP-001`, `CAP-002`, `CAP-003`, `CAP-005`)* : catalogues déclaratifs sans code libre, postes de supervision liés aux paramètres, avis contemporain et recours humain de l’article 12.1 de la Loi 25 [11], et archivage supervisé des communications réglementées [16];
  - *Agents et orchestration (`CAP-007`, `CAP-008`, `CAP-009`, `CAP-010`, `CAP-011`, `CAP-012`)* : enveloppe déterministe maître, exécution durable à revalidation post-attente, sagas à compensation et tampon d’irréversibilité, catalogue fermé de topologies, dorsale événementielle pour relecture ou pointes, et délégation interne munie d’une garde anti-boucle [17];
  - *Contexte et connaissance (`CAP-015`, `CAP-016`, `CAP-017`, `CAP-018`, `CAP-019`, `CAP-020`, `CAP-021`)* : couche sémantique gouvernée, médiation vers les formats financiers et d’assurance, compilation déterministe filtrée par droits en amont, compétences procédurales signées, mémoire bi-temporelle à oubli sélectif, quarantaine de qualité des données, et cloisonnement par personne morale, consentement et données prohibées [7] [11] [18];
  - *Accès (`CAP-022`, `CAP-023`, `CAP-024`, `CAP-026`)* : passerelle unifiée des cinq contrôles par appel, outils orientés intention à schémas épinglés, encapsulation décimale exacte du patrimoine, et passerelles réglementées à 99,5 % de disponibilité pour le partage ouvert accrédité [19];
  - *Modèles et exécution (`CAP-029`, `CAP-030`, `CAP-031`, `CAP-032`)* : plan de données d’inférence à routage frugal trois paliers, bac à sable matériel sans sortie réseau, continuité cognitive bimodèle vers des poids ouverts, et cloisonnement juridictionnel des six substrats d’état sous clés souveraines.

Posséder ce noyau n’implique pas de recoder des infrastructures basses : l’institution assemble des briques ouvertes ou commerciales derrière ses propres schémas canoniques, ses clés et ses politiques versionnées, afin qu’aucun fournisseur ne détienne ni le registre maître (`CAP-047`), ni les journaux probatoires (`CAP-049`), ni la grammaire des politiques (`CAP-037`) (C27, § 27.2, § 27.4). À l’inverse, les modèles frontières, le calcul banalisé et les agents internes à un progiciel métier sont **consommés comme ressources remplaçables** derrière `CAP-022` et `CAP-029`.

| Régime d’appropriation | Composants couverts | Capacités invariantes associées | Justification économique et prudentielle |
| --- | --- | --- | --- |
| **Possédé en propre** (schémas, clés et coupures) | Registre d’agents, identité NHI, moteur de politiques, collecteur et voûte d’audit, bancs internes, passerelles d’outils et d’inférence, couche sémantique et cloisonnement juridique. | Les 42 capacités invariantes de la carte `M-10`. | Préserve l’imputabilité sous E-23 [2] et B-10 [8], réduit le coût de transfert entre scénarios [1] et garantit l’opposabilité des preuves [11] [16]. |
| **Consommé de façon interchangeable** | Modèles commerciaux ou à poids ouverts, calcul GPU infonuagique, moteurs de persistance et connecteurs techniques banalisés. | Encapsulés derrière `CAP-018`, `CAP-022`, `CAP-029`, `CAP-031`, `CAP-051`. | Capte la baisse du coût unitaire des modèles sans verrouillage contractuel ni interruption lors du retrait d’une API (C27, § 46.4). |
| **Fédéré près des données** | Agents spécialistes internes aux progiciels CRM, ITSM, ERP, sinistres ou portefeuille pour les actes strictement mono-silo. | Encadrés par `CAP-012`, `CAP-022`, `CAP-036`, `CAP-042` (et `CAP-013` sous B et C). | Respecte les invariants transactionnels natifs des progiciels tout en interdisant les maillages latéraux opaques entre éditeurs (C27, § 27.4). |

## 11.3 La cible conditionnelle : les 10 capacités modulées par les scénarios A, B et C

Les dix capacités conditionnelles de `capacites.json` répondent aux bifurcations externes de la période 2028-2035. Selon la méthode des parcours adaptatifs [1], chacune sépare une **action préparatoire légère** (intégrée sans regret aux interfaces du noyau) et un **investissement complet**, déclenché uniquement sur signal vérifié :

| Famille stratégique | Capacité conditionnelle (`capacites.json`) | Scénarios | Palier | Action préparatoire dès P1–P2 (faible coût) | Seuil et signal déclenchant le déploiement complet |
| --- | --- | --- | --- | --- | --- |
| **1. Ouverture externe et multimodalité synchrone** | `CAP-004` — Interaction vocale et multimodale temps réel avec gestion d’interruption | **A, B** | P2 | Prévoir le consentement d’enregistrement et le caviardage audio/vidéo dans `CAP-042`. | Maturité latence/coût et stabilité des règles québécoises sur la collecte sans représentant (`SIG-102`). |
|  | `CAP-006` — Authentification et encadrement des agents externes sur les canaux numériques | **A, B** | P3 | Bloquer le grattage d’écran et séparer le routage API accrédité (`CAP-026`) [19]. | Décrets d’interdiction du grattage d’écran et ouverture réglementaire au-delà de la lecture seule (`SIG-103`) C : A, B ; SIG-103. |
|  | `CAP-014` — Négociation et exécution inter-organisations à séparation négociateur-évaluateur | **A, B** | P3 | Isoler dès P2 les tables de marges, de fraude et de prix de réserve hors des contextes d’agents (`CAP-021`). | Reconnaissance sectorielle ou prudentielle de justificatifs de mandat d’organisation en 2032-2035 (`SIG-007`) C : A, B ; SIG-007. |
| **2. Défense d’archipel multi-plateformes et souveraineté durcie** | `CAP-013` — Fédération d’orchestration multi-plateformes selon la gravité des données | **B, C** | P2 | Maintenir des contrats d’événements et d’états neutres (`CAP-008`, `CAP-012`). | Persistance de plans de contrôle éditeurs incompatibles ou surtaxation des appels croisés (`SIG-002`, `SIG-004`). |
|  | `CAP-025` — Harnais dérogatoire sous double validation et extinction des agents d’interface graphique | **B, C** | P1 | Exiger la preuve préalable d’absence d’interface binaire ou fichier (`CAP-024`). | Retard avéré d’ouverture d’API sur un progiciel fermé critique, avec budget obligatoire d’extinction à 12 mois (`SIG-103`). |
|  | `CAP-028` — Sas déterministe pour flux physiques/télématiques et continuité locale hors réseau | **B, C** | P2 | Définir les quotas d’indemnisation d’urgence dans les plans de continuité E-21 et B-9 [10]. | Déploiement terrain en zones à connectivité vulnérable lors de sinistres climatiques majeurs (`SIG-109`). |
|  | `CAP-033` — Inférence confidentielle en enclave matérielle attestée sur accélérateurs | **B, C** | P2 | Chiffrer les états et pseudonymiser les identifiants sous clés détenues par l’institution (`CAP-032`). | Tensions extraterritoriales accrues ou disponibilité régionale à coût maîtrisé de grappes GPU attestées (`SIG-002`, `SIG-016`). |
|  | `CAP-034` — Compilation déclarative des consignes et distillation sous sas anti-PII | **B, C** | P2 | Structurer dès P1 les compétences de façon déclarative (`CAP-018`) et les jeux d’essai (`CAP-043`). | Hausse durable du coût par résultat ou rationnement énergétique rendant rentable l’affinage de petits modèles (`SIG-015`, `SIG-016`). |
| **3. Confiance légale inter-institutionnelle formelle** | `CAP-027` — Connecteurs d’espaces de données fédérés sous politiques d’usage exécutables | **A, C** | P3 | Étiqueter finalités, entités et clauses de non-réentraînement sur tous les jeux internes (`CAP-021`). | Adoption de contrats d’usage exécutables par les consortiums d’assurance, de réassurance ou de finance (`SIG-110`) C : A, C ; SIG-110. |
|  | `CAP-041` — Identité légale d’organisation vérifiable et justificatifs de mandat externe | **A, C** | P3 | Structurer les mandats internes avec agilité cryptographique post-quantique (`CAP-036`, `CAP-040`). | Reconnaissance par un réseau de paiement ou un superviseur du G7 d’un profil normatif de mandat vérifiable (`SIG-007`) C : A, C ; SIG-007. |

Cette matrice module l’épaisseur du noyau interne selon la trajectoire qui se matérialise à partir de 2030 :

- **Scénario A (Socle étendu — 42 invariantes + 5 conditionnelles `CAP-004`, `006`, `014`, `027`, `041`) :** la traduction multi-éditeurs s’allège puisque les suites adoptent les standards d’identité et de trace; le capital du Palier 3 finance l’interopérabilité externe encadrée (partage financier ouvert étendu, soumissions courtiers automatisées, espaces de co-assurance) C : A ; SIG-003, SIG-007, SIG-110.
- **Scénario B (Archipel — 42 invariantes + 8 conditionnelles `CAP-004`, `006`, `013`, `014`, `025`, `028`, `033`, `034`) :** l’institution durcit sa médiation interne; `CAP-013` interdit les appels latéraux coûteux entre progiciels SaaS, `CAP-025` absorbe transitoirement les écrans fermés, et `CAP-034` contient la rente facturée par les fournisseurs de modèles C : B ; SIG-004, SIG-015.
- **Scénario C (Blocs — 42 invariantes + 7 conditionnelles `CAP-013`, `025`, `027`, `028`, `033`, `034`, `041`) :** l’exposition aux agents consommateurs sur le Web (`CAP-006`) et la négociation ouverte (`CAP-014`) sont gelées au profit d’échanges bilatéraux ou intra-bloc sous identité légale vérifiable (`CAP-027`, `CAP-041`), d’enclaves matérielles (`CAP-033`), d’autonomie déconnectée (`CAP-028`) et de petits modèles souverains (`CAP-034`) C : C ; SIG-001, SIG-002, SIG-016.

## 11.4 Règles d’arbitrage temporel entre investissement immédiat et option différée

Quatre règles opératoires tirées des parcours adaptatifs [1] cadrent l’allocation de capital :

1. **Primauté réglementaire et de contrôle (P1).** Toute capacité nécessaire à la conformité aux échéances datées de 2027-2029 (notamment `CAP-001` à `003`, `005`, `007` à `009`, `017`, `018`, `021` à `024`, `029`, `030`, `032`, `035` à `039`, `042`, `043`, `045`, `047` à `051`) est financée au Palier 1 avant toute extension d’autonomie.
2. **Délai de préparation (*lead time*) face aux seuils de bascule.** Lorsqu’une transition exige plusieurs années d’inventaire et de migration — certificats à 47 jours de mars 2029 D [6] et migration post-quantique recommandée sur 2030-2032 vers 2035 A [13] —, ses fondations d’agilité (`CAP-040`) sont engagées dès P1-P2 avant même toute contrainte prudentielle locale (`SIG-009`).
3. **Réservation d’interface sans immobilisation prématurée.** Pour les capacités conditionnelles de Palier 3 (`CAP-014`, `CAP-027`, `CAP-041`), l’institution n’acquiert aucun intergiciel dédié en 2028; elle vérifie seulement que ses schémas de mandat (`CAP-036`) et de cloisonnement (`CAP-021`) pourront accueillir une attestation externe sans refonte.
4. **Extinction budgétée des palliatifs.** Tout palliatif transitoire — en particulier le harnais d’agents d’interface graphique (`CAP-025`) — reçoit dès son octroi une date d’extinction financée afin de ne jamais devenir permanent (C27, § 25.4).

## 11.5 Ce que l’architecture cible exclut délibérément

Définir une cible sur sept ans impose enfin de proscrire cinq impasses, quel que soit le scénario :

- **Aucun pré-entraînement interne de grand modèle fondationnel généraliste.** Le coût en capital et en puissance électrique — jusqu’à 154 MW de pointe relevés par l’AIE pour un grand modèle frontalier [15] — est disproportionné face au routage frugal (`CAP-029`) et à la distillation ciblée (`CAP-034`) (C27, § 47.8).
- **Aucun « orchestrateur dieu » monolithique gouvernant l’intérieur de tous les progiciels.** Recoder dans un graphe central unique la logique interne du cœur bancaire, des sinistres, du CRM et du portefeuille bloque les livraisons et crée un point unique de défaillance (C27, § 16.7, § 23.9, § 27.4).
- **Aucune mémoire d’agent unifiée à l’échelle d’un groupe financier diversifié.** Fusionner dans un même index les données bancaires, les dossiers d’assurance et les profils de courtage enfreindrait la restriction bancaire de commercialisation d’assurance posée à l’article 416 (*Loi sur les banques*) [7], le principe de finalité de la Loi 25 [11] et l’encadrement des conflits d’intérêts [16].
- **Aucun essaim conversationnel cyclique non borné sur un processus soumis à audit.** Les dialogues libres entre pairs sans machine à états maîtresse ni plafond d’itérations ruinent la reproductibilité exigée par E-23 [2] et multiplient les défaillances MAST [20] (C27, § 16.5, § 21.1).
- **Aucun grattage d’écran externe sous identifiants clients, ni aucune auto-modification du cadre.** La réutilisation automatisée des mots de passe consommateurs est vouée à l’interdiction par l’article 171 de la *Loi sur les services bancaires axés sur les consommateurs* [19], et toute écriture d’un agent sur ses permissions, politiques ou journaux (`Classe 6`) reste bloquée techniquement [9] [12].

## Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Arbitrage entre posséder et consommer un composant agentique | Posséder en propre le noyau de contrôle (`CAP-047`, `CAP-035`, `CAP-037`, `CAP-042`/`049`, `CAP-022`/`029`); consommer modèles et calcul comme commodités remplaçables [8]. | Déléguer l’hébergement physique à un infonuagique qualifié uniquement si schémas, clés racines (`CAP-032`) et portabilité testée (`CAP-051`) demeurent sous maîtrise exclusive de l’institution [4] [8]. | [N] [4] [8] |
| Financement initial d’une capacité conditionnelle (`CAP-004`, `006`, `013`, `014`, `025`, `027`, `028`, `033`, `034`, `041`) | Ne financer en P1 que la réservation d’interface dans le noyau invariant; différer le déploiement complet jusqu’au franchissement vérifié du signal `SIG-nnn` associé [1]. | Activer en P1 le harnais dérogatoire `CAP-025` sur seule preuve formelle d’absence d’interface programmable sur un système critique, avec budget d’extinction à 12 mois. | [M] [1] |
| Coordination d’un processus traversant plusieurs suites SaaS d’éditeurs distincts | Laisser chaque acte mono-domaine dans l’agent du progiciel, mais imposer `CAP-022` et, dès deux silos mutés sous B ou C, le moteur durable neutre (`CAP-008`, `CAP-013`) (C27, § 27.4). | Flux purement analytique en lecture seule sans renseignement personnel sensible et couvert par un connecteur unidirectionnel audité. | [É] [12] |
| Spécialisation des modèles sur le vocabulaire et les règles internes | Privilégier l’ingénierie déterministe du contexte (`CAP-017`), les compétences signées (`CAP-018`) et le routage à trois paliers (`CAP-029`) sans modifier les poids [20]. | Activer la distillation sous sas anti-PII (`CAP-034`) en P2 sous B ou C si le volume stabilisé et la dérive du coût par résultat (`SIG-015`) en prouvent le gain net [15]. | [M] [20] |
| Ouverture des canaux numériques aux agents mandatés par les clients ou courtiers | Refuser tout accès par capture d’écran; canaliser vers les interfaces accréditées (`CAP-026`) [19], puis activer `CAP-006`, `CAP-014` et `CAP-041` sur signal réglementaire et normatif. | Jamais sur l’interdiction du contournement d’écran ni sur la vérification cryptographique du mandat et de l’accréditation [12] [19]. | [N] [12] [19] |

## Limites

Trois limites encadrent cette partition :

1. **Frontière évolutive entre invariant et conditionnel.** Le classement de dix capacités en statut conditionnel reflète l’état des normes et du marché au 16 novembre 2026; l’épreuve des profils sectoriels (`M-14` à `M-18`, clôturée au chapitre `M-19`) a confirmé cette partition initiale de dix capacités conditionnelles, et les revues du chapitre M-25 promouvront une capacité conditionnelle dès réalisation vérifiée de son signal.
2. **Corpus externes absents ou fermés.** L’absence sur disque du répertoire `../2026/` interdit de citer des exigences individuelles `EXIG-…`; de même, les lignes directrices `T-01`, `T-02`, `T-13`, `T-14` et `T-15` de l’AMF ainsi que `SecNumCloud v3.2` (`T-33`) et `TOGAF`, fermés (`F`) lors de la collecte sans contournement, ne soutiennent aucune preuve `[N]`.
3. **Absence de chiffrage budgétaire universel.** Conformément à `EF-13`, aucun budget fictif en dollars n’est prêté au noyau invariant : son dimensionnement dépend des entités juridiques, du patrimoine et des volumes propres à chaque institution, suivis par le coût par résultat conforme (`CAP-045`).

## Sources

1. V. A. W. J. Marchau, W. E. Walker, P. J. T. M. Bloemen et S. W. Popper (dir.), *Decision Making under Deep Uncertainty: From Theory to Practice* (ch. 1 et ch. 4, *Dynamic Adaptive Policy Pathways*), Springer Open Access, 2019, lu le 2026-11-16, lu en entier, statut L+, texte : N-10.txt.
2. BSIF, *Guideline E-23 – Model Risk Management (2027)*, publication 2025-09-11 (en vigueur le 1er mai 2027), lu le 2026-11-16, lu en entier, statut L+, texte : T-05.txt.
3. Parlement européen et Conseil, *Règlement (UE) 2026/1744 du 8 juillet 2026 modifiant le règlement (UE) 2024/1689 (omnibus numérique sur l’IA, reportant l’Annexe III au 2 décembre 2027)*, JOUE du 2026-07-24, lu le 2026-11-16, lu en entier, statut L+, texte : P-02.txt.
4. Parlement européen et Conseil, *Règlement (UE) 2023/2854 du 13 décembre 2023 sur les données (Data Act, art. 29 supprimant les frais de changement au 12 janvier 2027)*, JOUE du 2023-12-22, lu le 2026-11-16, lu par passages, statut L+, texte : P-08.txt.
5. BSIF, *Guideline B-15 – Climate Risk Management* (émissions de portée 3 dès l’exercice 2028), 2025-03-07 (mis à jour le 2026-01-08), lu le 2026-11-16, lu en entier, statut L+, texte : N-05.txt.
6. CA/Browser Forum, *TLS Baseline Requirements* v2.3.1 (adoption du Ballot SC-081v3 le 2025-04-11 abaissant la validité des certificats TLS à 100 jours en mars 2027 et 47 jours au 15 mars 2029), lu le 2026-11-16, lu par passages, statut L+, texte : P-26.txt.
7. Parlement du Canada, *Loi sur les banques* (*L.C. 1991, ch. 46*, art. 21 temporisation au 30 juin 2033 et art. 416 assurance, à jour 2026-10-29, dernière modification 2026-10-16), lu le 2026-11-16, lu par passages, statut L+, texte : T-16.txt.
8. BSIF, *Guideline B-10 – Third-Party Risk Management Guideline*, 2023-04-30, lu le 2026-11-16, lu en entier, statut L+, texte : T-06.txt.
9. BSIF, *Guideline B-13 – Technology and Cyber Risk Management*, 2022-07-31, lu le 2026-11-16, lu en entier, statut L+, texte : T-07.txt.
10. BSIF, *Guideline E-21 – Operational Risk Management and Resilience*, 2024-08-22, lu le 2026-11-16, lu en entier, statut L+, texte : T-08.txt.
11. Parlement du Québec, *Loi modernisant des dispositions législatives en matière de protection des renseignements personnels* (*L.Q. 2021, c. 25* — Loi 25, art. 3.3, 12–14, 12.1, 17 et 23), sanctionnée le 2021-09-22, lu le 2026-11-16, lu par passages, statut L+, texte : QC-01.txt.
12. BSIF, *Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security, and Operational Resilience* (Technology Risk Bulletin), juillet 2026 (modifié le 2026-07-13), lu le 2026-11-16, lu en entier, statut L+, texte : T-09.txt.
13. G7 Cyber Expert Group, *Advancing a Coordinated Roadmap for the Transition to Post-Quantum Cryptography in the Financial Sector*, janvier 2026, lu le 2026-11-16, lu en entier, statut L+, texte : P-24.txt.
14. OpenTelemetry, *Semantic Conventions for Generative AI Systems and Agentic Protocols (Status: Development)*, lu le 2026-11-16, lu par passages, statut L+, texte : P-19.txt.

15. Agence internationale de l’énergie (AIE), *Energy and AI*, avril 2025, lu le 2026-11-16, lu par passages, statut L+, texte : P-33.txt.
16. OCRI (CIRO), *Investment Dealer and Partially Consolidated Rules* (art. 1103, Règles 3100, 3400, 3600 et 3800), 2026-08-11, lu le 2026-11-16, lu par passages, statut L+, texte : T-23.txt.
17. Linux Foundation / Projet A2A, *Agent2Agent (A2A) Protocol Specification* v1.0.0, 2026, lu le 2026-11-16, lu en entier, statut L+, texte : N-09.txt.
18. Parlement du Canada, *Loi sur la non-discrimination génétique* (*L.C. 2017, ch. 3*, art. 1–7), à jour 2026-10-29, lu le 2026-11-16, lu en entier, statut L+, texte : N-01.txt.
19. Parlement du Canada, *Loi sur les services bancaires axés sur les consommateurs* (*L.C. 2026, ch. 3, art. 224*, art. 15–44, 125 et 171), sanctionnée le 2026-03-26 (à jour 2026-10-29), lu le 2026-11-16, lu en entier, statut L+, texte : T-19.txt.
20. M. Pan et al., *Measuring Agents in Production (MAP)* (`arXiv:2512.04123`), et M. Cemri et al., *Why Do Multi-Agent LLM Systems Fail? (MAST)* (NeurIPS 2025), 2025-2026, lu le 2026-11-16, lu par passages, statut L+, texte : P-38.txt.
21. Parlement du Canada, *Loi sur les sociétés d’assurances* (*L.C. 1991, ch. 47*, art. 21(1) temporisation au 30 juin 2033, à jour 2026-10-29), lu le 2026-11-16, lu par passages, statut L+, texte : CAN-01.txt.
