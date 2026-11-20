# Chapitre M-20 — Palier 1, 2028-2029

*Question directrice : Que faut-il avoir bâti avant d’accorder de l’autonomie?*

> **État de référence (16 novembre 2026) :** Ce chapitre définit le premier palier d’exécution de la feuille de route (`2028-2029`), ses quinze initiatives (`INI-001` à `INI-015`) et ses quatre portes de passage (`POR-001` à `POR-004`), en conformité avec `Master/registre/prescriptions.json` et l’échelle des domaines `D1` à `D8` et des classes de décision `Classe 1` à `Classe 6`.

## 20.1 Objectif, jalon et stade de sortie

Le **Palier 1 (**`2028-2029` **— Fonder)** répond à une exigence non négociable : mettre fin à la dispersion des pilotes isolés hérités de 2026-2027 et installer l’intégralité du plan de contrôle possédé avant d’élargir le périmètre d’action des agents. Sur le plan réglementaire, l’ouverture de ce palier s’effectue alors que la ligne directrice E-23 révisée du BSIF sur la gestion du risque lié aux modèles est pleinement en vigueur depuis le 1er mai 2027 D [1], que les obligations relatives aux systèmes à haut risque de l’Annexe III du règlement européen sur l’IA (solvabilité bancaire, assurance-vie et santé) s’appliquent depuis le 2 décembre 2027 aux groupes ayant une empreinte dans l’Union — distinctes des délais ultérieurs accordés aux administrations publiques — D [19], que l’interdiction des rétrofacturations de commissions en valeurs mobilières prend effet le 1er octobre 2028 D [20], que la divulgation climatique de portée 3 devient obligatoire dès la clôture de l’exercice 2028 D [18] et que la durée maximale des certificats TLS publics tombe à 47 jours le 15 mars 2029 D [16].

> **[Figure]**
> - Feuille de route 2028–2035 — Trois paliers franchis sur preuve et portes (15 portes POR définies) Règle d’ordre (C27) : le contrôle précède l’autonomie · Dates de paliers indicatives, franchissement sur preuves vérifiables
> - 2027 2028 2029 2030 2031 2032 2033 2034 2035
> - Paliers & stades cibles
> - Pont 2027
> - Socle C27
> - Stades 0–1
> - Palier 1 — Fonder
> - 2028–2029 · Sans regret
> - Sortie : Stade 2
> - Palier 2 — Étendre
> - 2030–2032 · Fédération & PQC
> - Sortie : Stade 3
> - Palier 3 — Élargir
> - 2033–2035 · Sous plafond légal
> - Sortie : Stade 3–4*
> - Initiatives structurantes
> - Prérequis
> - fin 2027
> - Registre E-23, NHI & TLS 47 j
> - Passerelle 5 contrôles & sas
> - Sagas & Loi 25 art. 12.1
> - Coût complet & clauses B-10
> - Sémantique & mémoire bi-temp.
> - PQC ML-DSA/SLH-DSA (CAP-040)
> - Lecture ouverte 99,5 % (CAP-026)
> - Fédération multi-plateformes
> - Mandats externes (CAP-014/041)
> - Espaces fédérés & enclave
> - Alignement lois fin. post-2033
> - Achèvement PQC de bout en bout
> - Portes sur preuve (POR)
> - POR-001..003 NHI, TLS 47 j, Loi 25, 10 s
> - POR-004 (Sortie P1) CPO, tiers B-10, fin CUA
> - POR-005..008 (PQC) ML-DSA/SLH-DSA, API 99,5 %
> - POR-009 (Sortie P2) Stade 3 & reprise humaine
> - POR-011..014 (Sortie P3) Mandats B2B & PQC 100 %
> - Échéances externes
> - [D] 2027-05 BSIF E-23
> - [D] 2027-12 AI Act Ann. III
> - [D] 2028 ACVM 31-103 & B-15
> - [D] 2029-03 TLS 47 j
> - [A] 2030–32 Fenêtre PQC G7
> - [D] 2033-06 Lois fin. fédérales
> - [D/A] 2035 Fin transition PQC
> - * Au Palier 3, les domaines soumis à un plafond légal ou à l’irréversibilité (Classes 4 et 5 critiques) demeurent aux Stades 2 ou 3.

*Fig. 6. – Frise 2028-2035 des trois paliers, de leurs portes et des échéances réglementaires*

Rapporté aux jalons du Compendium 2027 (C27, § 43.1, § 43.2), ce premier palier accomplit les **Jalons 1 et 2** (recensement intégral, identité distincte, médiation d’outils et homologation répétée) afin d’amener l’ensemble des domaines d’affaires prioritaires (`D1` à `D8`) du stade `1` vers un **Stade 2 solide (Usage encadré)** à la sortie de 2029 C : tous ; SIG-101. Durant ces vingt-quatre mois, l’autonomie en production est volontairement circonscrite : les tâches de lecture et de synthèse (`Classe 1`) se généralisent; les actions internes réversibles à faible matérialité (`Classe 2`) s’ouvrent sous compensation éprouvée sur `D4`, `D6` et `D8`; en revanche, toute décision matérielle (`Classe 3`), irréversible (`Classe 4`) ou visant une personne (`Classe 5`) sur `D2`, `D3` et `D5` demeure strictement subordonnée à une approbation humaine synchrone liée aux paramètres (`CAP-002`), la `Classe 6` restant techniquement interdite (`CAP-037`).

## 20.2 Architecture de transition à la sortie du palier

À la clôture du Palier 1, vingt-neuf des cinquante-deux capacités cibles sont en service actif sous tous les scénarios (trente sous les scénarios B et C avec la dérogation transitoire `CAP-025`)

et forment une architecture de transition cohérente à travers les huit emplacements du modèle de référence :

- **Couche 1 — Interaction (**`CAP-001`**,** `CAP-002`**,** `CAP-003`**,** `CAP-005`**).** Tous les canaux internes et clients reposent sur un rendu déclaratif sans exécution de scripts générés (`CAP-001`). Les files d’approbation humaine présentent une vue différentielle et lient la validation au condensat des paramètres (`CAP-002`). Toute décision de `Classe 5` émet l’avis contemporain, les facteurs principaux et le recours humain requis par la Loi 25 (`CAP-003`) [6], tandis que les correspondances assistées des courtiers et distributeurs traversent le sas de pré-approbation et d’archivage supervisé (`CAP-005`) [10] [12].
- **Couche 2 — Agents et orchestration (**`CAP-007`**,** `CAP-008`**,** `CAP-009`**).** L’orchestration demeure mono-domaine : chaque flux critique est enveloppé dans une machine à états déterministe (`CAP-007`), exécuté sur un moteur durable revalidant les conditions au sortir d’attente (`CAP-008`) et muni de clés d’idempotence, de compensations pré-enregistrées et d’un tampon de retenue devant les virements irrévocables ou envois externes (`CAP-009`) [4] [9].
- **Couche 3 — Contexte et connaissance (**`CAP-017`**,** `CAP-018`**,** `CAP-021`**).** Sans attendre l’unification ontologique complète du Palier 2, la récupération documentaire filtre les listes d’accès du mandant en amont (`CAP-017`), les procédures métiers sont livrées en paquets déclaratifs signés (`CAP-018`), et l’étiquetage à l’ingestion verrouille dès le premier jour les murailles inter-filiales, le secret anti-blanchiment et le rejet absolu des résultats génétiques (`CAP-021`) [6] [7] [11].
- **Couche 4 — Accès aux outils et systèmes (**`CAP-022`**,** `CAP-023`**,** `CAP-024`**, et conditionnellement** `CAP-025`**).** Aucun agent n’appelle un système métier hors de la passerelle aux cinq contrôles (`CAP-022`) ni d’un fichier de verrouillage signé des schémas d’outils (`CAP-023`). Les programmes centraux sollicités sur `D3`, `D4` et `D5` sont encapsulés en arithmétique décimale exacte (`CAP-024`); les rares écrans patrimoniaux sans API sont confinés dans le harnais dérogatoire à retrait programmé sous douze mois (`CAP-025`).
- **Couche 5 — Modèles et exécution (**`CAP-029`**,** `CAP-030`**,** `CAP-032`**).** Le plan de données d’inférence route les requêtes sur trois paliers avec affinité de cache (`CAP-029`), isole tout calcul généré en bac à sable sans réseau sortant (`CAP-030`) et localise les six substrats d’état sous clés matérielles détenues par l’institution (`CAP-032`) [2] [3] [6].
- **Plan de contrôle — Volets 1, 2 et 3 (**`CAP-035` **à** `039`**,** `CAP-042`**,** `043`**,** `045`**,** `CAP-047` **à** `051`**).** Les trois volets atteignent leur régime opérationnel de base : identités non humaines parrainées sans secret statique (`CAP-035`), échange de jetons atténués par saut (`CAP-036`), décision de politique déterministe hors modèle (`CAP-037`), décontamination des pièces externes (`CAP-038`), coupe-circuit opérationnel sous dix secondes (`CAP-039`), télémétrie normalisée au collecteur à double couloir (`CAP-042`), qualification pré-production répétée (`CAP-043`), affichage du coût complet par résultat conforme (`CAP-045`), registre central bloquant (`CAP-047`), matrice des plafonds `D1`–`D8` × `Classes 1`–`6` (`CAP-048`), qualification juridictionnelle (`CAP-049`), revue indépendante de deuxième ligne (`CAP-050`) et clauses contractuelles de sortie des tiers (`CAP-051`) [1] [2] [5] [21].

## 20.3 Initiatives sans regret et initiatives conditionnelles

Quatorze initiatives **sans regret** — indispensables sous les trois scénarios A, B et C — et une initiative **conditionnelle** composent le portefeuille du Palier 1 :

### Initiatives sans regret (`INI-001` à `INI-014`)

- **INI-001 — Déploiement du registre central d’inventaire, de cote de risque inhérent et de blocage réseau.** P : INI-001 Met en place le répertoire unique d’entreprise rattachant chaque agent à son propriétaire métier, à sa cote de risque E-23 et à un contrôle d’admission réseau bloquant les déploiements non inscrits (`CAP-047`, `CAP-048`; seuil de bascule : coexistence d’agents dans plus d’une direction ou audit E-23; signal `SIG-101`) D [1] (C27, § 8.7, § 39.1).
- **INI-002 — Mise en service des identités non humaines parrainées, de l’automatisation TLS à 47 jours et de l’échange de jetons à portée atténuée.** P : INI-002 Élimine les clés d’API statiques et sessions humaines relayées au profit d’attestations courtes couplées au système RH, automatise à 100 % le renouvellement des certificats TLS sous le plafond de 47 jours avant le 15 mars 2029 (`ANC-030`) et déploie les échanges de jetons réduisant l’audience à chaque saut (`CAP-035`, `CAP-036`; signal `SIG-003`, `SIG-012`) [3] [5] [15] [16] (C27, § 29.2, § 30.2).
- **INI-003 — Interposition de la passerelle d’outils aux cinq contrôles et épinglage cryptographique des schémas.** P : INI-003 Impose l’authentification mutuelle, l’autorisation par opération, la validation de schéma, le quota budgétaire et la vérification de signature des descripteurs sur tout serveur d’outils (`CAP-022`, `CAP-023`; signal `SIG-005`) [3] [14] (C27, § 24.2, § 31.5, § 49.7).
- **INI-004 — Externalisation du point de décision de politique déterministe, décontamination et coupe-circuit.** P : INI-004 Déploie le moteur déclaratif hors modèle vérifié formellement, l’extracteur isolé pour documents externes non fiables et le coupe-circuit relié au centre de sécurité (`CAP-037`, `CAP-038`, `CAP-039`; signal `SIG-101`) D [1] [3] [4] (C27, § 30.6, § 31.4, § 34.6).
- **INI-005 — Instrumentation de la télémétrie causale normalisée au collecteur et de la voûte forensique régionale.** P : INI-005 Déploie la corrélation distribuée de bout en bout, l’isolation d’un schéma interne face aux conventions externes en chantier et le masquage des renseignements personnels avant indexation générale (`CAP-042`; signal `SIG-006`) [6] [17] (C27, § 33.2, § 33.4).
- **INI-006 — Cartographie juridictionnelle des six substrats d’état et mise sous clés souveraines.** P : INI-006 Localise journaux, mémoires, caches, traces, files et sauvegardes sous clés matérielles détenues par l’institution et active les étiquettes d’exclusion légale, y compris pour les renseignements génétiques protégés au Canada (`CAP-021`, `CAP-032`; signal `SIG-107`) [6] [7] [11] [26] (C27, § 38.6, § 46.1).
- **INI-007 — Mise en place du plan de données d’inférence tri-palier et des bacs à sable d’exécution sans réseau.** P : INI-007 Centralise le routage cognitif frugal avec affinité de préfixe et confine tout code ou calcul généré en environnement jetable isolé (`CAP-029`, `CAP-030`; signal `SIG-015`) [3] [22] (C27, § 32.3, § 44.3).
- **INI-008 — Standardisation de l’enveloppe déterministe, de l’exécution durable et des sagas à compensation.** P : INI-008 Fournit aux équipes les gabarits d’orchestration
  déterministe, de reprise sans double appel, de revalidation post-attente et de tampon sur actions irréversibles (`CAP-007`, `CAP-008`, `CAP-009`; signal `SIG-014`) [4] [9] (C27, § 17.6, § 18.3, § 18.5).
- **INI-009 — Déploiement des interfaces déclaratives bornées, des postes de supervision liée et du canal de recours client.** P : INI-009 Équipe les postes clients, conseillers et réviseurs du catalogue visuel fermé, de l’approbation liée aux paramètres, des avis Loi 25, des avis et recours de protection des consommateurs financiers et de l’archivage supervisé (`CAP-001`, `CAP-002`, `CAP-003`, `CAP-005`; signal `SIG-106`) [6] [10] [13] [27] (C27, § 22.5, § 38.4).
- **INI-010 — Industrialisation de la compilation déterministe du contexte et de la bibliothèque signée de compétences.** P : INI-010 Remplace les invites artisanales par l’assemblage filtré selon les droits en amont et des paquets procéduraux signés portables (`CAP-017`, `CAP-018`; signal `SIG-005`) D [1] (C27, § 13.3, § 13.6, § 15.3).
- **INI-011 — Encapsulation déterministe en décimal exact des programmes centraux bancaires et actuariels prioritaires.** P : INI-011 Construit les premiers adaptateurs typés protégeant l’exactitude comptable et le débit des systèmes d’enregistrement sur `D3`, `D4` et `D5` (`CAP-024`; signal `SIG-015`) [4] (C27, § 25.1, § 25.4).
- **INI-012 — Mise en service des bancs internes de qualification multi-essais et de l’outillage indépendant des deuxième et troisième lignes.** P : INI-012 Constitue les jeux de simulation métiers scellés mesurant la constance répétée et ouvre le portail d’audit indépendant de la gestion des risques de modèles (`CAP-043`, `CAP-050`; signal `SIG-013`) D [1] [23] [24] (C27, § 33.7, § 39.6).
- **INI-013 — Automatisation de la qualification par empreinte juridictionnelle et de la comptabilité au coût par résultat.** P : INI-013 Intègre aux pipelines le contrôle bloquant des pièces requises sous BSIF E-23 dès le 1er mai 2027 D [1], sous la Loi 25 [6] et sous le règlement européen 2026/1744 applicable le 2 décembre 2027 aux institutions financières visées — distinct du butoir du 2 août 2030 propre aux administrations publiques — D [19], et publie mensuellement le coût complet par résultat conforme (`CAP-045`, `CAP-049`; signal `SIG-001`) [22] (C27, § 38.7, § 40.5).
- **INI-014 — Renégociation des clauses contractuelles de notification, de non-réemploi et de sortie des tiers.** P : INI-014 Aligne systématiquement les renouvellements fournisseurs sur les exigences de transparence agentique, d’interdiction d’entraînement et d’exportation sans frais (`CAP-051`; signal `SIG-002`) D [2] [5] [21] (C27, § 27.5).

### Initiative conditionnelle (`INI-015`)

- **INI-015 — Encadrement dérogatoire confiné et plan d’extinction à douze mois des agents d’interface graphique résiduels.** P : INI-015 Activée uniquement sous les **scénarios B et C** lorsqu’un progiciel patrimonial critique dépourvu d’API retarderait une chaîne prioritaire : enferme la session dans un harnais à masquage de données personnelles, double validation visuelle et budget obligatoire de retrait sous douze mois (`CAP-025`; signal `SIG-103`; C27, § 25.4, § 25.5; `ADR-016`).

### Ordonnancement interne sur vingt-quatre mois

L’exécution du portefeuille 2028-2029 obéit à un chemin critique en quatre vagues semestrielles afin d’éviter qu’une équipe métier ne développe sur des fondations mouvantes :

| Semestre | Priorité d’ingénierie et de gouvernance | Initiatives livrées | Verrou levé |
| --- | --- | --- | --- |
| **S1 2028** | Visibilité complète, identité parrainée, résidence souveraine et clauses contractuelles | `INI-001`, `INI-002`, `INI-006`, `INI-014` | Fin des déploiements clandestins, des clés statiques et des transferts hors juridiction non maîtrisés [1] [2] [3] [6]. |
| **S2 2028** | Médiation technique obligatoire des outils, politique hors modèle et télémétrie causale | `INI-003`, `INI-004`, `INI-005`, `INI-007` | Passage par `POR-001` et `POR-002`; interdiction technique de tout appel direct d’outil ou d’inférence hors passerelle [3] [14] [17]. |
| **S1 2029** | Industrialisation de l’exécution durable, du contexte filtré, des postes supervisés et de la 2e ligne | `INI-008`, `INI-009`, `INI-010`, `INI-012` | Franchissement de `POR-003`; homologation indépendante des premiers flux `D1`, `D4`, `D6` et `D8` en Stade 2 [1] [4] [10] [13]. |
| **S2 2029** | Encapsulation décimale des systèmes centraux, affichage économique complet et cantonnement d’écran | `INI-011`, `INI-013`, et conditionnellement `INI-015` | Franchissement de `POR-004`; sortie ordonnée du Palier 1 avec coût complet par résultat publié [4] [22]. |

## 20.4 Portes et preuves de sortie

Aucun domaine d’affaires n’est autorisé à franchir le Palier 1 sur simple constat calendaire : quatre portes séquentielles exigent des preuves matérielles vérifiables par la deuxième ligne de défense.

- **POR-001 — Étanchéité de l’inventaire central, des identités non humaines, des certificats TLS 47 jours, des bacs à sable et de la passerelle d’outils.** P : POR-001 Subordonne l’ouverture d’outils opérationnels en production (`CAP-018`, `CAP-022`, `CAP-023`, `CAP-030`, `CAP-035`, `CAP-036`, `CAP-047`) à deux preuves : (1) 100 % des agents actifs rattachés à une fiche d’inventaire munie d’une cote de risque E-23 et d’un parrain RH actif, avec rejet réseau démontré d’un agent non inscrit et confinement sans trafic réseau sortant des bacs à sable (`CAP-030`); (2) zéro clé statique ou session humaine partagée en audit de configuration, renouvellement automatisé à 100 % des certificats TLS sous 47 jours avant le 15 mars 2029 (`ANC-030`), et rejet automatique d’un schéma d’outil ou d’un paquet de compétence procédurale altéré sans signature (`CAP-018`, `CAP-023`) D [1] [3] [5] [16] (C27, § 8.7, § 29.2, § 30.2, § 32.3).
- **POR-002 — Conformité juridique des six substrats d’état, du double couloir de traces et des recours clients.** P : POR-002 Subordonne le traitement de données personnelles ou sectorielles protégées (`CAP-001`, `CAP-003`, `CAP-005`, `CAP-017`, `CAP-021`, `CAP-032`, `CAP-042`, `CAP-049`) à deux preuves : (1) inventaire vérifié des six substrats par juridiction, test de révocation de clé cliente rendant les états illisibles, zéro renseignement personnel en clair dans l’index général de traces et zéro fragment hors habilitations retourné par le filtrage ACL amont (`CAP-017`); (2) vérification sur échantillon réel du rendu déclaratif sans script généré (`CAP-001`), de l’avis contemporain, de l’explication des facteurs et du recours
  humain (Loi 25, art. 12.1) ainsi que rejet prouvé d’indices génétiques et de déclarations anti-blanchiment [6] [7] [10] [11] [26] (C27, § 33.4, § 38.4, § 46.1).
- **POR-003 — Qualification indépendante de deuxième ligne, résilience d’exécution durable et coupe-circuit.** P : POR-003 Subordonne toute mise en service sur les `Classes 2 à 5` (`CAP-002`, `CAP-007`, `CAP-008`, `CAP-009`, `CAP-037`, `CAP-038`, `CAP-039`, `CAP-043`, `CAP-050`) à deux preuves : (1) certificat de revue indépendante signé par la deuxième ligne sur banc de simulation interne répété incluant zéro invocation mutative non autorisée sur corpus d’injections indirectes (`CAP-038`); (2) exercice chronométré prouvant l’arrêt des mutations par le coupe-circuit en moins de dix secondes et la reprise sans doublon d’une transaction interrompue pendant une attente humaine D [1] [4] [23] (C27, § 18.5, § 33.7, § 34.6, § 39.6).
- **POR-004 — Sortie du Palier 1 (Stade 2 atteint) : coût complet affiché, clauses de réversibilité et retrait planifié des dérogations d’écran.** P : POR-004 Autorise l’entrée d’un domaine au Palier 2 (`CAP-024`, `CAP-025`, `CAP-029`, `CAP-045`, `CAP-048`, `CAP-051`) sur constat conjoint : (1) publication mensuelle du coût complet par résultat conforme non rouvert comparé à sa base non agentique préalable; (2) présence des clauses de notification et de sortie dans les contrats renouvelés et budget d’extinction à douze mois sur toute dérogation résiduelle d’interface graphique D [2] [21] [22] (C27, § 25.4, § 27.5, § 40.5, § 43.1).

L’évaluation de chaque porte obéit à une séparation stricte des rôles conforme à la gouvernance prudentielle des trois lignes de défense [1] [4] : la première ligne (ingénierie de plateforme et propriétaire métier du domaine `D1` à `D8`) produit les journaux d’essais horodatés; la deuxième ligne (gestion du risque de modèles, sécurité et conformité juridique) rejoue un sous-ensemble contradictoire sur son outillage indépendant (`INI-012`) et dispose d’un droit de veto suspensif; la troisième ligne (audit interne) vérifie annuellement l’absence de contournement dérogatoire. Lorsqu’un domaine échoue à une preuve de `POR-003` ou `POR-004`, ses agents existants ne sont pas arrêtés s’ils respectent `POR-001` et `POR-002`, mais ils demeurent gelés en mode de préparation pure (`Classe 1`) jusqu’à levée matérielle de la réserve, sans retarder la progression des autres directions métiers déjà qualifiées.

## 20.5 Dépendances externes et signaux de bascule

Trois dépendances externes rythment l’exécution de 2028-2029 et gouvernent d’éventuels ajustements de trajectoire :

1. **Normalisation de l’identité d’agent, de l’interopérabilité et de la télémétrie (**`SIG-003`**,** `SIG-004`**,** `SIG-005`**,** `SIG-006`**).** À l’IETF, le groupe `WIMSE` travaille sur l’identité de charge de travail (`SIG-003`) [15] tandis que les groupes `DAWN` et `AGENTPROTO` fixent leurs jalons IESG entre la fin de 2027 et mars 2028 (`SIG-004`) A [25]; la révision `MCP` du 28 juillet 2026 appelle également le cadrage de l’identité d’agent (`SIG-005`) [14], et les conventions OpenTelemetry pour agents demeurent en statut de développement (`SIG-006`) [17]. L’architecture du Palier 1 isole donc ces formats derrière la passerelle (`INI-003`) et le collecteur (`INI-005`) afin d’adopter les normes stabilisées sans réécrire les agents métiers.

2. **Abaissement à 47 jours de la validité des certificats TLS le 15 mars 2029 (**`ANC-030`**,** `SIG-012`**).** Ce jalon daté D [16] impose dès le Palier 1 (`CAP-035`, `INI-002`) et sous contrôle bloquant de `POR-001` d’éliminer tout renouvellement manuel de certificat sur les points de terminaison d’agents et de serveurs d’outils, préparant directement la bascule post-quantique `ML-DSA`/`SLH-DSA` du Palier 2 (`CAP-040`, `INI-019`, `POR-007`).
3. **Évolutions prudentielles fédérales et québécoises (**`SIG-101`**,** `SIG-102`**,** `SIG-103`**,** `SIG-105`**,** `SIG-106`**).** Toute transformation du bulletin BSIF de juillet 2026 en ligne directrice opposable [5], toute publication ouverte des lignes directrices québécoises de l’AMF ou toute prise des décrets d’application des services bancaires ouverts [8] déclenche le relèvement immédiat des contrôles d’empreinte dans `INI-013`.

## 20.6 Ce que le palier ne fait pas

Pour concentrer les ressources d’ingénierie et de deuxième ligne sur l’étanchéité des fondations, le Palier 1 **exclut explicitement cinq chantiers**, dont toute activation anticipée constituerait une dérive hors plan :

1. **Aucune délégation transactionnelle directe entre organisations externes (Stade 4 interdit en** `P1`**).** Ni l’initiation d’opérations par agents tiers externes (`CAP-006`, `CAP-014`), ni les espaces de données fédérés (`CAP-027`), ni les mandats inter-entreprises (`CAP-041`) ne sont ouverts en production en 2028-2029.
2. **Aucun essaim multi-agents inter-domaines en production.** La coopération entre directions métiers distinctes attend la couche sémantique gouvernée (`CAP-015`) et la garde anti-boucle inter-plateformes (`CAP-012`) du Palier 2.
3. **Aucune mémoire sémantique persistante inter-sessions sur dossiers clients.** Tant que le graphe bi-temporel et l’effacement sélectif vérifiable (`CAP-019`) ne sont pas homologués en `P2`, les agents fonctionnent sur état de session borné et lecture filtrée à la volée (`CAP-017`).
4. **Aucune refacturation comptable punitive avant stabilisation de la mesure.** Conformément à l’exposé du Compendium 2027 (C27, § 40.2), le Palier 1 affiche le coût complet par résultat (`showback` via `INI-013`) et réserve la refacturation interne obligatoire (`chargeback`) au Palier 2.
5. **Aucune suppression des équipes métiers de révision et de contre-expertise.** Sur `D2`, `D3` et `D5`, l’objectif de `P1` est d’instrumenter la qualité et la célérité de la décision humaine, jamais de démanteler la capacité de reprise manuelle exigée par BSIF E-21 et E-23 [1] [4].

## Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Ouverture d’un outil mutatif en production durant `P1` | Bloquer techniquement tant que `POR-001`, `POR-002` et `POR-003` ne sont pas franchies par le domaine | Jamais en production; seuls des bacs à sable sur données synthétiques sont admis avant `POR-003` | [N] [1] |
| Mode d’authentification d’un agent vers un système métier | Identité non humaine parrainée et jeton éphémère atténué par saut (`INI-002`) | Jamais d’emprunt de session humaine ni de clé d’API partagée en production | [N] [3] |
| Gestion des conventions externes instables (télémétrie, jetons) | Encapsuler derrière le collecteur normalisateur (`INI-005`) et la passerelle (`INI-003`) | Bascule directe vers le standard externe dès son passage officiel au statut stable (`SIG-003`, `SIG-006`) | [É] |
| Imputation économique des coûts d’agents en 2028-2029 | Afficher mensuellement le coût complet par résultat conforme sans refacturation comptable interne | Avancer la refacturation dès fin 2029 uniquement si la clé de corrélation par clôture métier est auditée sans écart | [M] |
| Demande d’automatisation par écran sur progiciel ancien | Refuser par défaut et prioriser un adaptateur décimal déterministe (`INI-011`) | Dérogation `INI-015` de 12 mois maximum si l’absence d’interface binaire/fichier est prouvée et le retrait financé | [S] |

## Limites

1. **Rythme d’absorption de la deuxième ligne de défense.** Le passage de `POR-003` sur l’ensemble des flux des `Classes 3 à 5` dépend de la capacité réelle des équipes indépendantes de validation des modèles; en cas de goulot d’étranglement, le périmètre de sortie de `P1` se restreint aux domaines les plus critiques sans jamais abaisser le niveau d’exigence des preuves.
2. **Décrets fédéraux et textes québécois fermés.** Le calendrier exact des décrets d’entrée en vigueur du cadre bancaire ouvert (`T-20`) demeure annoncé `[A]` [8], et les cinq documents PDF fermés de l’AMF québécoise (`T-13` à `T-15`, `T-01` et `T-02`) restent au statut fermé (`F`).

## Sources

1. BSIF, *Ligne directrice E-23 — Gestion du risque lié aux modèles (2027)*, 2025-09-11, lu le 2026-11-16, lu en entier, statut L+, texte : T-05.txt.
2. BSIF, *Ligne directrice B-10 — Gestion du risque lié aux tiers*, 2023-04-30, lu le 2026-11-16, lu en entier, statut L+, texte : T-06.txt.
3. BSIF, *Ligne directrice B-13 — Gestion du risque lié aux technologies et au cyberrisque*, 2022-07-31 (en vigueur le 2024-01-01), lu le 2026-11-16, lu en entier, statut L+, texte : T-07.txt.
4. BSIF, *Ligne directrice E-21 — Gestion du risque opérationnel et résilience opérationnelle*, 2024-08-22, lu le 2026-11-16, lu en entier, statut L+, texte : T-08.txt.
5. BSIF, *Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security, and Operational Resilience — Bulletin sur le risque technologique*, 2026-07-13, lu le 2026-11-16, lu en entier, statut L+, texte : T-09.txt.
6. Parlement du Québec, *Loi 25 — L.Q. 2021, c. 25 modifiant RLRQ, c. P-39.1*, 2021-09-22, lu le 2026-11-16, lu par passages, statut L+, texte : QC-01.txt.

7. Parlement du Canada, *Loi sur le recyclage des produits de la criminalité et le financement des activités terroristes* (*L.C. 2000, ch. 17*), 2026-10-29, lu le 2026-11-16, lu par passages, statut L+, texte : T-10.txt.
8. Ministère des Finances du Canada, *Projet de Règlement sur les services bancaires axés sur les consommateurs*, 2026-06-27, lu le 2026-11-16, lu en entier, statut L+, texte : T-20.txt.
9. Paiements Canada, *Système RTR — Spécifications ISO 20022 v1.4*, 2025-05-30, lu le 2026-11-16, lu par passages, statut L+, texte : T-21.txt.
10. OCRI, *Règles visant les courtiers en placement — règles 3100 à 3900*, 2026-08-11, lu le 2026-11-16, lu par passages, statut L+, texte : T-23.txt.
11. Parlement du Canada, *Loi sur la non-discrimination génétique — L.C. 2017, ch. 3*, 2026-10-29, lu le 2026-11-16, lu en entier, statut L+, texte : N-01.txt.
12. Parlement du Québec, *Loi sur les assureurs et LDPSF — L.Q. 2018, c. 23*, 2018-06-13, lu le 2026-11-16, lu par passages, statut L+, texte : QC-03.txt.
13. CCRRA et OCRA, *Conduite des activités d’assurance et traitement équitable des clients*, novembre 2017, lu le 2026-11-16, lu en entier, statut L+, texte : T-27.txt.
14. Model Context Protocol (MCP), *Specification*, 2026-07-28, lu le 2026-11-16, lu en entier, statut L+, texte : P-10.txt.
15. IETF WIMSE, *Charter & draft-ietf-wimse-aims-01*, 2026-11-02, lu le 2026-11-16, lu en entier, statut L+, texte : P-12.txt.
16. CA/Browser Forum, *Ballot SC-081v3 (TLS Certificate Validity)*, 2025-04-11, lu le 2026-11-16, lu par passages, statut L+, texte : P-26.txt.
17. OpenTelemetry, *GenAI & Agentic Semantic Conventions (Development)*, lu le 2026-11-16, lu par passages, statut L+, texte : P-19.txt.
18. BSIF, *Ligne directrice B-15 — Gestion des risques climatiques*, 2025-03-07 (mis à jour le 2026-01-08), lu le 2026-11-16, lu en entier, statut L+, texte : N-05.txt.
19. Union européenne, *Règlement (UE) 2026/1744 du 8 juillet 2026 modifiant les échéances de l’AI Act*, JOUE du 2026-07-24, lu le 2026-11-16, lu en entier, statut L+, texte : P-02.txt.
20. Autorités canadiennes en valeurs mobilières (ACVM), *Modifications au Règlement 31-103 interdisant les rétrofacturations (chargebacks)*, 2026-10-08, lu le 2026-11-16, lu en entier, statut L+, texte : CAN-08.txt.
21. Union européenne, *Règlement (UE) 2023/2854 du 13 décembre 2023 (Data Act, art. 29)*, JOUE du 2023-12-22, lu le 2026-11-16, lu par passages, statut L+, texte : P-08.txt.
22. Stanford HAI, *AI Index Report*, 2026, lu le 2026-11-16, lu par passages, statut L+, texte : P-36.txt.
23. AICA / IAIS, *Application Paper on the Supervision of Artificial Intelligence*, 2025-07-02, lu le 2026-11-16, lu en entier, statut L+, texte : CAN-02.txt.
24. METR, *Measuring AI Ability to Complete Long Tasks (arrêt série initiale)*, 2026-09-08, lu le 2026-11-16, lu en entier, statut L+, texte : P-34.txt.
25. IETF DAWN & AGENTPROTO, *Charters and Milestones*, 2026-10-23, lu le 2026-11-16, lu en entier, statut L+, texte : P-16.txt.
26. Cour suprême du Canada, *Renvoi relatif à la Loi sur la non-discrimination génétique* (*2020 CSC 17*, *[2020] 2 R.C.S. 283*), 2020-07-10, lu le 2026-11-16, lu par passages, statut L+, texte : CAN-03.txt.
27. Agence de la consommation en matière financière du Canada (ACFC), *The Financial Consumer Protection Framework: Enhanced Protection for Bank Customers*, 2025-10-16, lu le 2026-11-16, lu en entier, statut L+, texte : T-12.txt.
