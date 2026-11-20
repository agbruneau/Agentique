# Chapitre 9 — Plan d’inférence, six substrats d’état, confidentialité matérielle, résilience et réseaux B2B

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 47, 50]` · `[CAD26 ch. 5, 6, 9, 11–13 | EXIG-ARC-08, EXIG-ARC-09, EXIG-INT-22, EXIG-SEC-10, EXIG-SEC-20, EXIG-CON-05, EXIG-APP-10..14]` · `[C27 ch. 37, 44–46 | ADR-014, ADR-026..028]` · `[PD28 M-11, M-13 | PRI-011 | CAP-014, CAP-027..029, CAP-031..033, CAP-041 | DEC-006, DEC-008, DEC-012 | POR-002, POR-006, POR-013]`.

*Question directrice : Où résident réellement les six états d’un agent, comment en assurer la continuité cognitive et la souveraineté juridictionnelle, et comment encadrer les interactions B2B fédérées ?*

**Thèse du chapitre :** Souveraineté, résilience et ouverture inter-entreprises se jouent dans le plan d’inférence, les substrats d’état et les frontières B2B P : PRI-011 . L’institution interpose une passerelle de modèles (alias logique `DEVRAIT`) dissociant routage à trois paliers, affinité `KV-cache` et cinq horloges de versionnage P : CAP-029 P : DEC-006 E : EXIG-ARC-08 E : EXIG-ARC-09 . Elle chiffre sous clés maîtrisées chacun des six substrats d’état sans confondre résidence physique et contrôle juridictionnel. Elle intègre ainsi les limites des enclaves matérielles et la continuité cognitive bimodèle P : CAP-031 P : CAP-032 P : CAP-033 P : POR-002 P : POR-006 E : EXIG-CON-05 E : EXIG-APP-11 . Enfin, elle subordonne tout échange B2B au Palier 3 à `vLEI`, à la scission Diplomate / Évaluateur et au rapprochement à trois voies avant règlement P : CAP-014 P : CAP-027 P : CAP-041 P : DEC-012 P : POR-013 E : EXIG-INT-22 .

## 9.1 Plan de données d’inférence, séparation modèle / réplique et cinq horloges de versionnage

Dans les six couches de `CAD26 § 5.2`, la **passerelle de modèles** siège en Couche 3 (*Agents et exécution cognitive*) : tout appel d’inférence la traverse E : EXIG-ARC-08 , désigné par **alias logique** (`DEVRAIT`) et jamais par identifiant fournisseur en dur (`ADR-014`) P : CAP-029 P : DEC-006 E : EXIG-ARC-09 . Le plan de données (`C27 ch. 44 § 44.1–44.5`, pp. 866–871) sépare deux décisions orthogonales :

1. **Choix du modèle (routage à trois paliers).** Le trafic se partage entre petit modèle frugal sur tâches bornées qualifiées en `E2`, modèle frontière par défaut sur intention complexe, et calcul accru à l’inférence sur arbitrage ardu (`EXIG-FIN-06`). `C27 § 44.3` (pp. 868–869, échelle à trois paliers posée en cible `[S]`) rappelle toutefois que les routeurs automatiques restent sensibles aux reformulations et fragiles sur requêtes difficiles, excluant tout routage non qualifié en `E2`.
2. **Choix de la réplique (affinité** `KV-cache`**).** Sur parc dédié, un rond-robin détruit la localité des préfixes d’invites et d’outils. Un ordonnanceur conscient du cache pondère charge des files GPU et préfixes chauds en VRAM pour abaisser délai du premier jeton (`TTFT`), coût de relecture et empreinte énergétique (`C27 § 44.4–44.5`, `EXIG-FIN-07`).

Alors qu’un condensat binaire suffit à promouvoir un logiciel classique (`C26 § 47.10`), un agent suit **cinq horloges de versionnage asynchrones** (`C26 ch. 47 § 47.8`, p. 542 `[S]`) :

| Horloge | Composant | Angle mort (`C26 ch. 47`) | Parade AE / AS |
| --- | --- | --- | --- |
| **1. Modèle** | Millésime réel servi (`gen_ai.response.model`) | Mutation silencieuse derrière un alias fournisseur (`§ 47.10`). | Tracer le millésime en audit (`EXIG-OBS-12`), préavis écrit (`EXIG-APP-13`) et rejeu `E2` (`EXIG-GOV-12`). |
| **2. Invites** | Consignes système et gabarits | Modification déclarative hors compilation (`§ 47.7`). | Gestion comme du code et condensat `SHA-256` inscrit en audit (`EXIG-ARC-24`, `EXIG-OBS-12`). |
| **3. Outils** | Schémas et serveurs `MCP` | Retournement après approbation (*rug-pull*, `§ 47.4`). | Épinglage cryptographique au catalogue interne (`EXIG-MCP-20`, `EXIG-SEC-18`). |
| **4. Politiques** | Règles `PDP` et plafonds | Décalage entre code promu et règles actives (`§ 47.8`). | Politiques versionnées hors modèle (`CAP-037`) et version tracée en audit (`EXIG-OBS-12`). |
| **5. Harnais** | Cadriciel (compaction, ordre des règles) | Cinquième horloge hors socle (`§ 47.8.1`), altérant le comportement à invite constante. | Épinglage strict dans l’image immuable et qualification `E2`. |

Deux conséquences s’imposent à l’AS. D’abord, `CycloneDX 1.7` et `SPDX 3.0` (`EXIG-SEC-20`, requis par le *Cyber Resilience Act* au 11 décembre 2027 D `ANC-008`) inventorient modèles et bibliothèques. Toutefois, ils **n’incluent aucun champ pour les invites ni les politiques** (`C26 Tableau 47.3` p. 538), et les extensions déclaratives JSON manquent de révocation (`C26 § 47.7`, degré 3). Ensuite, **un retour arrière (*rollback*) d’artefact ne restaure ni la mémoire accumulée, ni les délégations actives**, ni les effets externes déjà commis (`C26 § 47.11`, pp. 543–544).

## 9.2 Souveraineté juridictionnelle, six substrats d’état, `TEE` / `HYOK` et continuité cognitive

Selon `C27 ch. 37` (`§ 37.1`, p. 743), **la résidence physique des données n’équivaut jamais au contrôle juridictionnel**. Héberger à Montréal ou Toronto chez un opérateur soumis à une loi extraterritoriale (*CLOUD Act*) n’offre aucune immunité. Aucun schéma européen `EUCS` unifié n’est adopté mi-2026 hors qualifications nationales tel *SecNumCloud* (`C27 § 37.5`). Sous `Loi 25 art. 17`, l’institution qualifie l’exploitant et maîtrise les clés E : EXIG-CON-05 E : EXIG-APP-11 sur les **six substrats d’état** (`C27 § 46.1` `[S]`, `ADR-027`) P : PRI-011 P : CAP-032 P : POR-002 :

| Substrat (`C27 § 46.1` `[S]`) | Contenu | Risque dominant | Contrôle cible (`POR-002`) |
| --- | --- | --- | --- |
| **1. Modèle et configuration** | Poids, adaptateurs, invites, catalogue | Fuite de propriété intellectuelle ou altération. | Artefacts signés, registre interne et repli à poids ouverts (`CAP-031`). |
| **2. Contexte volatil d’inférence** | Fenêtre active, `KV-cache` GPU, sorties d’outils | Exposition en clair sur GPU mutualisés ; rétention fournisseur. | Clause zéro rétention / zéro entraînement (`EXIG-APP-10`), enclave `TEE` sélective (`CAP-033`). |
| **3. Mémoire longue persistante** | Épisodes, index vectoriels, graphes bi-temporels | Profilage massif et entrave au droit à l’oubli. | Isolation par entité/mandant (`EXIG-ARC-23`), clés souveraines et purge `Loi 25`. |
| **4. État d’exécution durable** | Points de contrôle, attentes (`awakeable`), journaux Saga | Sérialisation accidentelle de paramètres sensibles ou jetons. | Magasin externe chiffré au repos (`EXIG-ORC-11`, `EXIG-ORC-13`) et zéro jeton stocké (`EXIG-IAM-06`). |
| **5. Traces et journaux d’audit** | Métadonnées `OTel`, voûte forensique, audit `JCS` | Injonction étrangère ou altération interne des preuves. | Double couloir PII (`≤ 14 j`), audit `JCS` et ancrage horaire externe (`EXIG-OBS-07..13`). |
| **6. Secrets et clés** | Clés racines de gestionnaire de clés (*Key Management Service*, `KMS`) / module matériel de sécurité (*Hardware Security Module*, `HSM`), autorités `SPIFFE` | Perte immédiate de souveraineté sur compromission. | Garde exclusive par l’institution (`HYOK` / `HSM`) pour déchiquetage instantané. |

Sur accélérateurs mutualisés — en sus de `CAD26 EXIG-SEC-10` (`IOMMU` et remise à zéro mémoire) —, les **enclaves matérielles (**`TEE`**) CPU/GPU** (`C27 § 46.2, 46.10`) restent conditionnelles aux scénarios `B` et `C` sous `SIG-016` P : CAP-033 P : INI-027 . Deux réserves s’imposent (`C27 § 46.2–46.3, 46.10`). D’abord, l’attaque `TEE.fail` sur bus `DDR5` **coûterait moins de** `1 000 $ US` **selon les auteurs** (page non recoupée, `C27 § 46.2`) pour extraire des clés CPU et relayer des attestations GPU, sans dispenser de sécurité physique. Ensuite, le séquestre externe de clés (`HYOK`) garantit une révocation immédiate (`POR-002`) sous `RTT ≤ 35 ms` **conseillé**, sans portabilité native des chiffrés.

En **continuité cognitive (*Cognitive DR*)**, basculer d’API prend quelques secondes, mais réaligner invites, outils et seuils sur une autre famille exige des semaines à froid (`C27 § 46.4`). Tout flux critique (`Classes 3 à 5`) pré-qualifie donc en `E2` un **second profil indépendant à poids ouverts exercé chaque trimestre** P : CAP-031 P : DEC-006 P : POR-006 E : EXIG-APP-14 . Les seuils de reprise `< 15 min` `[S]` (`C27 § 46.11`) et d’autonomie déconnectée `72 h` `[S]` (`C27 § 46.17`) restent des **cibles de conception sans appui empirique (**`[S]`**)**. Hors réseau (sinistres terrain, `PEX-031`), l’agent opère en *Local-First* sur **quotas en séquestre** réconciliés par `CRDT` (`C27 § 46.5, 46.14`). À la marge du cœur financier, si un groupe expose un équipement physique ou télématique (`CAP-028`, `ADR-028`), toute commande (`ROS 2`/`DDS`) franchit un **arbitre matériel déterministe** `Simplex` (`ISO 10218-1:2025` / `IEC 61508`) sous mises à jour signées `TUF`, sans certifier le contrôleur neuronal P : CAP-028 P : DEC-008 .

## 9.3 Réseaux B2B fédérés conditionnels (`P3`) : `vLEI`, `Dataspace`, Diplomate / Évaluateur et rapprochement 3 voies

L’échange inter-organisations (`Stade 4`) reste proscrit en conseil (`D2`, `Stades 2–3`) et sur les enquêtes de conformité (`D6`, `Stade 3` interne en `PD28 M-12` p. 171, hors inventaires techniques de `M-18`). Ailleurs, il demeure conditionnel au Palier 3 (`2033–2035` C : A, C ; SIG-007, SIG-110 ) sous quatre verrous (`C27 ch. 45`, `ADR-026`) P : CAP-014 P : CAP-027 P : CAP-041 P : DEC-012 P : POR-013 :

1. **Identité légale vérifiable (**`vLEI`**).** Tout agent tiers présente ses justificatifs `GLEIF vLEI` et de rôle organisationnel officiel (*Official Organizational Role*, `OOR`, `SIG-007`) liés à la personne morale et aux plafonds de son mandat (`CAP-041`).
2. **Connecteurs** `Dataspace` **et** `ODRL 2.2`**.** Les flux B2B (co-assurance, réassurance, portée 3) traversent des connecteurs exécutant `ODRL 2.2` (`CAP-027`), qui gouverne l’usage sans empêcher techniquement la copie post-livraison hors salle blanche (`C27 § 45.2, 45.5`).
3. **Scission** `Diplomate / Évaluateur` **et anti-collusion.** Le **Diplomate** externe ne détient aucun secret ; l’**Évaluateur** interne vérifie les offres contre tables de réserve, marges et fraude sous rondes bornées (`C27 § 45.4`, `CAP-014`), avec surveillance statistique de la **collusion algorithmique** (`C27 § 45.6`).

4. **Rapprochement à trois voies avant règlement (**`AP2` **/** `x402`**).** Tout mandat de paiement (`AP2` — transfert FIDO non matérialisé au 1er nov. 2026 `C26 S-091` — ou `x402`) est classé `P3` E : EXIG-INT-22 sous **rapprochement déterministe à trois voies** hors modèle (contrat signé, preuve d’exécution, facture conforme, `C27 § 45.7`, `POR-013`).

Correspondance `ABB → SBB` de l’inférence, des substrats et du B2B (état au 28 oct.–14 nov. 2026) :

| Domaine | ABB (bloc neutre) | SBB substituables (état au 28 oct.–14 nov. 2026) |
| --- | --- | --- |
| Passerelle et ordonnancement d’inférence | Médiateur d’alias à 3 paliers et affinité `KV-cache` | agentgateway, Envoy AI Gateway, LiteLLM, Portkey, Bifrost ; `Gateway API Inference Extension` (`EPP`) et `llm-d` sur vLLM, SGLang, TensorRT-LLM (RouteLLM avec réserve) |
| Confidentialité matérielle et clés | Enclaves matérielles CPU/GPU attestées et séquestre externe | `Intel TDX`, `AMD SEV-SNP`, `NVIDIA Confidential Computing` ; `HSM` internes et `HYOK` (`RTT ≤ 35 ms` conseillé) |
| Échange B2B fédéré | Identité légale et connecteur d’espace de données | `GLEIF vLEI` (`KERI`/`ACDC`), Eclipse Dataspace Components (`EDC`) + `ODRL 2.2` |

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. Imposer la matrice juridictionnelle des six substrats d’état (`[S]`) en séparant résidence physique et contrôle juridictionnel extraterritorial P : PRI-011 P : CAP-032 P : POR-002 E : EXIG-CON-05 E : EXIG-APP-11 .
2. Exiger sur les flux critiques (`Classes 3 à 5`) une continuité cognitive bimodèle incluant un profil indépendant à poids ouverts testé chaque trimestre P : CAP-031 P : DEC-006 P : POR-006 E : EXIG-APP-14 , et réserver les enclaves `TEE` sur signal `SIG-016` P : CAP-033 .
3. Subordonner tout `Stade 4` B2B en `P3` (`2033–2035` C : A, C ; SIG-007, SIG-110 ) à `vLEI`, à la scission Diplomate / Évaluateur, à l’anti-collusion et au rapprochement tripartite avant paiement P : CAP-014 P : CAP-027 P : CAP-041 P : DEC-012 P : POR-013 E : EXIG-INT-22 .

Spécifications AS

1. Opérer tout modèle derrière la passerelle par alias logique (`DEVRAIT`) E : EXIG-ARC-08 E : EXIG-ARC-09 , dissocier routage prudent à 3 paliers et affinité `KV-cache`, et gouverner les cinq horloges (`C26 § 47.8`) au-delà de `CycloneDX 1.7` / `SPDX 3.0` E : EXIG-SEC-20 .
2. Chiffrer les substrats sous clés souveraines (`HYOK` avec `RTT ≤ 35 ms` conseillé), intégrer le risque physique `TEE.fail` (qui coûterait moins de `1 000 $ US` selon les auteurs), et encadrer le mode déconnecté par quotas en séquestre `CRDT` et arbitre `Simplex` (cibles sans appui empirique : RTO `< 15 min` `[S]` et autonomie `72 h` `[S]`) P : CAP-028 P : DEC-008 .
3. Cloisonner réseau et mémoire entre Diplomate externe et Évaluateur interne, attacher `ODRL 2.2` aux connecteurs `Dataspace`, et bloquer tout règlement `AP2`/`x402` (`P3`) derrière un rapprochement déterministe à trois voies.

## 9.4 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Invocation des modèles et répliques | Passerelle unique et alias logiques (`DEVRAIT`), routage à 3 paliers et affinité `KV-cache` P : CAP-029 P : DEC-006 E : EXIG-ARC-08 E : EXIG-ARC-09 | Jamais d’appel direct vers une API externe hors bac d’essai local sans données réelles | `[M]` `C27` ch. 44 § 44.3–44.5 ; `CAD26` § 5.2 |
| Souveraineté des états d’un agent | Matrice juridictionnelle et clés maîtrisées par l’institution sur les six substrats P : CAP-032 P : POR-002 E : EXIG-CON-05 | Données strictement publiques `P0` sans renseignement personnel ni secret d’affaires | `[N]` `Loi 25` art. 17 (`EXIG-APP-11`) ; `C27` § 37.1, § 46.1 `[S]` |
| Enclaves d’inférence confidentielle (`TEE`) | Activation sélective (`SIG-016`) pour secrets critiques sur accélérateurs mutualisés P : CAP-033 | Grappe dédiée sous contrôle physique complet, ou latence `HYOK` excédant le seuil conseillé de `35 ms` `RTT` | `[M]` `[É]` Attaque `TEE.fail` (coûterait `< 1 000 $ US` selon les auteurs, `C27` § 46.2–46.3) |
| Continuité face à la défaillance d’un modèle | Second profil indépendant à poids ouverts pré-qualifié en `E2` et exercé chaque trimestre P : CAP-031 P : POR-006 | Assistants internes non critiques `Classe 1` tolérant une suspension temporaire | `[N]` `BSIF` E-21 / B-10 ; `CAD26` `EXIG-APP-14` |
| Résilience terrain hors réseau et actionneurs | Quotas en séquestre bornés (`CRDT`) et arbitre matériel déterministe `Simplex` P : CAP-028 P : DEC-008 | Actes irréversibles ou refus `Classe 4`, retenus jusqu’au retour du canal humain | `[S]` `C27` § 46.4–46.8, § 46.11, § 46.17 (`< 15 min` `[S]`, `72 h` `[S]`) |
| Transaction inter-entreprises (`Stade 4`) | Identité `vLEI`, scission Diplomate / Évaluateur, anti-collusion et rapprochement 3 voies avant `P3` P : CAP-014 P : CAP-041 P : DEC-012 P : POR-013 E : EXIG-INT-22 | Proscrit en conseil (`D2`) et sur les enquêtes/décisions de conformité (`D6`, `Stade 3` interne en `PD28 M-12`) | `[M]` Collusion (`C27` § 45.6) ; `C26` `S-091` |

## 9.5 Limites et renvois

**Limites et réserves.** Les cinq horloges (`C26 § 47.8`, dont la cinquième sans socle primaire en `§ 47.8.1`) et les six substrats (`C27 § 46.1`) sont des constructions d’auteur (`[S]`). Tout chiffrage fictif du *Groupe Boréal Inc.* (`C27 § 46.17`) est exclu comme preuve, et les seuils `< 15 min` `[S]` et `72 h` `[S]` demeurent des cibles de conception non mesurées, tout comme les prototypes OT (`C27 § 28.5`). Au 17 novembre 2026, ni `EUCS` (`C27 § 37.5`) ni le transfert d’`AP2` (`C26 S-091`) ne sont aboutis.

**Renvois aux volumes sources :** `C26` ch. 47 (pp. 534–544 ; § 47.2.1, § 47.7–47.11), ch. 50 (`S-091` p. 585) ; `CAD26` § 5.2–5.3 (`EXIG-ARC-08, 09`), `EXIG-INT-22`, `EXIG-SEC-10, 20`, `EXIG-CON-05`, `EXIG-APP-10..14` ; `C27` ch. 37 (pp. 747–754), ch. 44 (`ADR-014` pp. 874–893), ch. 45 (`ADR-026` pp. 894–915), ch. 46 (`ADR-027, 028` pp. 916–949) ; `PD28` `M-11`, `M-13`, `PRI-011`, `CAP-014`, `CAP-027..029`, `CAP-031..033`, `CAP-041`, `DEC-006`, `DEC-008`, `DEC-012`, `POR-002`, `POR-006`, `POR-013`, `SIG-007`, `SIG-009`, `SIG-015`, `SIG-016`, `SIG-103`, `SIG-109`, `SIG-110`.
