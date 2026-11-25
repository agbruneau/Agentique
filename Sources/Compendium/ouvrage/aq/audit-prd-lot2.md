# Audit indépendant `REV-03` (Lot 2/4) — Fidélité à `prd.md`, cohérence, schémas et édition (`CH-10` à `CH-18`)

> **Auditeur** : `audit-prd-lot2` (`REV-03`, Lot 2/4) · **Date** : `2026-11-25` · **Régime** : Production (audit seul, zéro modification de manuscrit ou de schéma)  
> **Périmètre** : Partie IV (`D04` : `CH-10`, `CH-11`, `CH-12`), Partie V (`D05` : `CH-13`, `CH-14`, `CH-15`), Partie VI (`D06` : `CH-16`, `CH-17`, `CH-18`) et leurs `27` schémas (`SCH-10-01` à `SCH-18-03`).  
> **Références confrontées** : `Compendium/prd.md` (L2074–L3579), `aq/rapports-g0.json`, extraits `CA-G0-SYNC` (`Tome 8/trousse/`), `sources/ch10..18-sources.md`, `ancrage/ch10..18-ancrage.md`, `registre/` et `schemas/SCH-10-01`..`SCH-18-03` (+ `rendus/`).

---

## 1. Synthèse exécutive

L'audit indépendant des `9` chapitres (`CH-10`–`CH-18`) et de leurs `27` schémas relève un socle technique globalement dense, bien sourcé (`100 %` des renvois `[1]..[N]` résolus dans `sources/chXX-sources.md`, `4/4` blocs `CA-G0-SYNC` conformes octet pour octet au rapport `G0`, `27/27` liens de rendus valides), mais identifie **`23` constats ouverts** : **`2` BLOQUANTS**, **`11` MAJEURS** et **`10` MINEURS**.

| Gravité | Nombre | Identifiants |
|---|---:|---|
| **BLOQUANT** | `2` | `PRD-L2-001` (`ch13`), `PRD-L2-002` (`ch18`) |
| **MAJEUR** | `11` | `PRD-L2-003` (`ch10`), `PRD-L2-004` (`ch14`), `PRD-L2-005` (`ch15`), `PRD-L2-006` (`ch15`), `PRD-L2-007` (`ch17`), `PRD-L2-008` (`ch13`), `PRD-L2-009` (`ch14`), `PRD-L2-010` (`ch18`), `PRD-L2-011` (`ch17`), `PRD-L2-012` (`ch16`), `PRD-L2-013` (`ch11`) |
| **MINEUR** | `10` | `PRD-L2-014` (`ch10`), `PRD-L2-015` (`ch12`), `PRD-L2-016` (`ch11`), `PRD-L2-017` (`ch13`), `PRD-L2-018` (`ch10`), `PRD-L2-019` (`ch18`), `PRD-L2-020` (`ch17`), `PRD-L2-021` (`ch13`), `PRD-L2-022` (`ch14`), `PRD-L2-023` (`ch16`) |
| **Total** | **`23`** | **Axes** : `schemas` (`8`), `couverture_prd` (`6`), `coherence` (`5`), `edition` (`4`) |

Les deux constats **bloquants** exigent une correction avant publication :
1. **`PRD-L2-001` (`ch13`)** : `Chapitre 13.md` donne deux définitions mutuellement contradictoires d'`OO1–OO4` dans la même section `13.2.1` (L17/L132 + `SCH-13-01` assimilent `OO1`/`OO2` au code déterministe pur et au graphe fixe, tandis que L9/L31 et le Tableau 13.1 les définissent comme des régimes émergents pilotés par l'agent et proscrits par `C26 § 29.4.1`).
2. **`PRD-L2-002` (`ch18`)** : `SCH-18-03.mmd` attribue explicitement à `pqc_http431.py` des tailles d'en-tête atteignant `165 Ko` à `5` sauts, ce qui contredit frontalement le Tableau 18.1 (`97 403` octets maximum mesurés par `pqc_http431.py`).

---

## 2. Vérification `CA-G0-SYNC`, trousse `G0` et intégrité des liens

| Chapitre | Extrait `CA-G0-SYNC` | Fichier source (`Tome 8/trousse/`) | Lignes | Concordance texte | Concordance SHA-256 (`aq/rapports-g0.json`) |
|---|---|---|---|---|---|
| `CH-15` | `G0-EX-CH03-03` | `policy_saga/saga_orchestrator.py` | `107-140` | `OK` (exact) | `OK` (`a2aac944...`) |
| `CH-17` | `G0-EX-CH02-01` | `authz_pqc_audit/obo_dpop.py` | `85-114` | `OK` (exact) | `OK` (`d3c2d0ce...`) |
| `CH-17` | `G0-EX-CH02-02` | `authz_pqc_audit/ciba_approval.py` | `106-117` | `OK` (exact) | `OK` (`423ebd61...`) |
| `CH-18` | `G0-EX-CH02-03` | `authz_pqc_audit/pqc_http431.py` | `149-177` | `OK` (exact) | `OK` (`c5c72e27...`) |

- **Symboles `trousse/` vérifiés** : `StepStatus.ESCALADED` (`CH-10`, conforme à `harness_proto/pipeline.py`), `MoneyAmount` / `ALLOWED_CURRENCIES` (`CH-12`, conforme à `policy_saga/decimal_money.py`), `SagaStatus` et `11/11` tests `test_saga_10_faults.py` (`CH-15`), `assert_active` (`CH-17`, `revocation_fsm.py`), `ML_DSA_SPECS` `3 309` / `4 627` o (`CH-18`, `pqc_http431.py`).
- **Liens schémas et sources** : `27/27` images `../../schemas/rendus/SCH-1X-0Y.{svg,png}` existent et sont non vides ; `100 %` des sources `[1]..[N]` concordent avec `sources/ch10-sources.md`..`ch18-sources.md` ; `100 %` des SVG sources (`SCH-12-03`, `SCH-13-01/02`, `SCH-14-01`, `SCH-15-01`, `SCH-16-01/02`, `SCH-17-03`, `SCH-18-02`) sont identiques à leur copie dans `schemas/rendus/`.

---

## 3. Bilan chapitre par chapitre (`CH-10` à `CH-18`)

| Unité | Familles / Thèmes PRD | Couverture substantielle | Schémas (`SCH-XX-01..03`) | Constats ouverts |
|---|---|---|---|---|
| **`CH-10`** | `2` / `7` | Très solide : `DEC-003`/`ADR-009`, `FIBO`/`SHACL`/`OWL 2`, `ODCS v3.2.0`/`WAP`, `Lynx`/`RTR`/`DORS/2026-133`, `KV-cache`, `RAG` hybride, `Agent Skills`. Réancrage pertinent de la coexistence `60 j` sur `EXIG-INT-14` (`SIG-110` omis). | `SCH-10-02.puml` attribue à tort `DORS/2026-133` à `Lynx` au lieu de `RTR` ; `§45.12` brut. | `PRD-L2-003` (M), `PRD-L2-014` (m), `PRD-L2-018` (m) |
| **`CH-11`** | `2` / `5` | Très solide : `CoALA` 4 compartiments, `PRIN-11`/`DEC-004`, `EXIG-ARC-22..25`, `HMAC`/`CaMeL` (`taint_camel.py`, `camel_taint.rego`), bi-temporalité `Graphiti`/`Letta`, `Crypto-Shredding` Loi 25 art. 23, `OpenFGA`/`RLS`, `Silo`/`Bridge`/`Pool`, `Recall@K` vs `RAGAS`/`ARES`. `MemGPT`/`Zep` omis. | `SCH-11-01` omet écriture validée et purge sur `Z3` (sémantique) ; `SCH-11-03` affiche `EXIG` tronqué et `Pool` non relié à `N7` ; `§39.5` brut dans `SCH-11-02`. | `PRD-L2-013` (M), `PRD-L2-016` (m) |
| **`CH-12`** | `2` / `7` | Très solide : `EBCDIC CP037/CP1147`, `COMP-3` → `Decimal` (`decimal_money.py`, `PEX-015`), `CQRS`/`CDC`, `QSYS2.SET_CLIENT_INFO`, `Strangler Fig` 4 stades, `ADR-016` (`≥ 92 % MCP` / `≤ 8 % CUA` / `12 mois` / `POR-008`), `LSAC` art. 171, `Purdue`/`IDMZ`/`Simplex`/`FMI 3.0`, `Edge CRDT 72 h`, `6 substrats` + `HYOK` + `prr_validators.py`. Manquent `CAP-033` en prose, `Cedar` en Edge et `IEEE P3945.1`. | Cohérents ; `SCH-12-03.svg` cite `CAP-033` (absent de la prose). | `PRD-L2-015` (m) |
| **`CH-13`** | `2` / `10` | Couverture riche (`Kim`, `Tran/Kiela`, `Ringelmann`, `ReAct`/`ReWOO`, `APM`, 8 patrons `ADR-011` + débat, 10 anti-patrons `EXIG-ORC-29`, `EXIG-ORC-23..25`, `Diplomate DMZ`/`Évaluateur TEE`, `MAST v3` 14 modes, 7 modes frontaliers), mais **contradiction interne bloquante sur `OO1–OO4`** et forte désynchronisation avec ses 3 schémas (`FM-2 32,3 %` vs `32,4 %`, `3×–15×`, `24,7 %` bogues SDK, `fromAi 10 appels`, `Replit #1152`). | `SCH-13-01` hérite l'amalgame `OO1/OO2` déterministes proscrits par `C26 § 29.4.1` ; `SCH-13-02` et `SCH-13-03` désynchronisés de la prose `G5`. | `PRD-L2-001` (**B**), `PRD-L2-008` (M), `PRD-L2-017` (m), `PRD-L2-021` (m) |
| **`CH-14`** | `2` / `3` | Bon traitement de la dorsale `CloudEvents v1.0.2` / `AsyncAPI 3.x`, `EXIG-EVT-01..10`, `Outbox + CDC`, pathologies réactives (`STPA`/`ASI08`/`ASI10`), `DLQ`, `backpressure`, `FORCED_OPEN`, passerelle `MCP ↔ ROS 2/DDS`, `LOTO`, `Simplex` (`≤ 1 ms`) et `TUF`/`Sigstore`. Omet `DEC-007`, `ADR-015`, `PRR R-04`, `PRR R-05`. | `SCH-14-02.mmd` teste `xagenthopcount > 4` contre `≥ 4` dans la prose ; `SCH-14-03.puml` dit « conforme IEC 61508 / ISO 10218-1 » contre le désaveu L91. | `PRD-L2-004` (M), `PRD-L2-009` (M), `PRD-L2-022` (m) |
| **`CH-15`** | `2` / `7` | Exemplaire en prose (`0` ID `prd.md` manquant) : `Temporal`/`Restate`/`Dapr`/`Step Functions`, `TOCTOU`, `PRIN-12` (`5` plafonds, `9` capacités POC), `LAP v0.1`, `Saga` à point pivot, `Outbox`, `EXIG-ORC-28` (`G0-EX-CH03-03`), `10` fautes `test_saga_10_faults.py`, `idem-v1` `JCS`, `UETR` `RFC 9562`. | Deux défauts majeurs de schémas : étapes Saga/compensation incohérentes dans `SCH-15-02.puml` ; `Lecture (L0–L1)` et câblage `Engagement → LAP` uniquement dans `SCH-15-03.mmd`. | `PRD-L2-005` (M), `PRD-L2-006` (M) |
| **`CH-16`** | `2` / `8` | Très bon traitement de `NHI`, `Blueprint`/`Instance`, parrainage SIRH `< 72 h`, `Q-A..Q-E`, `BCP 240`/`RFC 9700`, `Entra`/`GCP`/`AWS`, `3` modèles de registres, `AgentCard` `JWS`/`JCS` (`a2a_card.py`), `SPIFFE`/`SPIRE`/`RATS`/`WIMSE`, passeport `4+1` pièces, `GLEIF vLEI` (`ISO 17442-3`). Écart `0/15` (`3×5` vs `15` mécanismes `prd.md`), verdict passeport `1/4` omis, `EXIG-IAM-09`/`16`, `NIST SP 800-207`, `ANC-022`, `SIG-003` absents. | `SCH-16-01` affirme `Socle OAuth 2.1` (brouillon selon L48) ; `SCH-16-02` affiche `A2A v1.0.0` vs `v1.0.1` en Tableau 16.1. | `PRD-L2-012` (M), `PRD-L2-023` (m) |
| **`CH-17`** | `2` / `7` | Très rigoureux sur le noyau exécutable (`G0-EX-CH02-01/02`, `revocation_fsm.py`, `RFC 8693/8707/9396/9449/8705/9700`, `Txn-Token -11`, `CIBA`+`FIDO2`+`I-JSON`/`JCS` `C.6`, `KYA 0/9`, `SSF 1.0`/`CAEP 1.0`). Omet la veille `agentproto`/`dawn`/`ID-JAG`/`Macaroons`/`Biscuit`/`RFC 9635` et plusieurs cotes `ADR-*`/`EXIG-AUT-10`/`EXIG-ORC-04`/`PRR S-04`. | `SCH-17-01.puml` place à tort `PKCE S256` et `iss RFC 9207` sur la flèche d'échange arrière-plan `OBO RFC 8693`. | `PRD-L2-007` (M), `PRD-L2-011` (M), `PRD-L2-020` (m) |
| **`CH-18`** | `2` / `4` | Très clair sur `SC-081v3` (`100 j` / `47 j` / `10 j`), `ACME`, `FIPS 203/204/205`, `NIST IR 8547`, `Mosca`, `CBOM`, `3` conditions crypto-agilité, `SCITT`+`SLH-DSA`, `G0-EX-CH02-03` et `Tableau 18.1`. Date `NIST IR 8547` divergente de `prd.md` (`21 oct.` vs `27 oct. 2026`), `ANC-023/030/040/043`, `DEC-012`, `SIG-010/011` absents de la prose. | **Bloquant** : `SCH-18-03.mmd` impute `165 Ko` à `pqc_http431.py` (contre `97,4 Ko` max au Tab. 18.1). `SCH-18-01` contient « automation » ; `SCH-18-02` affiche `T21.3` brut ; faute « son neutralisation » (L122). | `PRD-L2-002` (**B**), `PRD-L2-010` (M), `PRD-L2-019` (m) |

---

## 4. Registre détaillé des constats (`PRD-L2-001` à `PRD-L2-023`)

### Constats BLOQUANTS

- **`PRD-L2-001`** (`BLOQUANT` · `coherence` · `ch13`) — **Contradiction interne sur `OO1–OO4` dans `Chapitre 13.md` et `SCH-13-01.svg`**.
  - *Faits vérifiés* : `Chapitre 13.md` L17 et L132 (et `SCH-13-01.svg` L13–L27, L68–L84) assimilent `OO1` au code déterministe pur (`N0`/`DMN`), `OO2` au graphe fixe, `OO3` à l'agent unique et `OO4` au multi-agents, tout en écrivant que `OO2` (« Flux prévisible sans boucle libre ») est « Proscrit si test C26 § 29.4.1 positif ». Or, `Chapitre 13.md` L9, L31 et le **Tableau 13.1** (L33–L38) définissent au contraire `OO1` et `OO2` comme des régimes pilotés par l'agent sans artefact exécutoire (expérimentation / assistance consultative), et `OO3`/`OO4` comme des régimes à épine dorsale déterministe (conformes à `Tome 1 § 22.1 / Figure 22.1`).
  - *Résolution* : Séparer nettement l'**arbre de sobriété en 4 paliers** (`N0/code → flux structuré → agent unique → multi-agents`, `EXIG-ORC-01/02`) de la **grille `OO1–OO4` d'autorité de commandement** (`Tome 1 § 22.1`), corriger `CH-13` L17/L132 et refondre `SCH-13-01.svg` en conséquence.

- **`PRD-L2-002`** (`BLOQUANT` · `schemas` · `ch18`) — **Contradiction chiffrée entre `SCH-18-03.mmd` (`165 Ko` attribué à `pqc_http431.py`) et le Tableau 18.1 (`97 403 o` max)**.
  - *Faits vérifiés* : `SCH-18-03.mmd` L6 affiche `Chaîne à 2 sauts : 20–35 Ko / 5 sauts : jusqu'à 165 Ko (pqc_http431.py)`. Or, `Chapitre 18.md` L103 et le Tableau 18.1 rapportent les sorties exactes de `pqc_http431.py`, dont le maximum à 5 sauts est `97 403` octets (`JWT_X5C_CHAIN`, `ML-DSA-87`) et `24 468`–`33 258` octets en `JWT_KID_REF` (tandis que `165 Ko` provenait de l'estimation `Borealis-Bench` non présente sur disque).
  - *Résolution* : Remplacer les valeurs dans `SCH-18-03.mmd` par les mesures vérifiées de `pqc_http431.py` (Tableau 18.1 : `9,6–38,8 Ko` à 2 sauts ; `24,5–97,4 Ko` à 5 sauts) et regénérer `rendus/SCH-18-03.png`.

### Constats MAJEURS

- **`PRD-L2-003`** (`MAJEUR` · `schemas` · `ch10`) — **`Règlement n° 10 DORS/2026-133` placé dans le bloc `Rail Lynx` de `SCH-10-02.puml`**.
  - *Faits vérifiés* : `SCH-10-02.puml` L44 (`N5`) place `Règlement n° 10 DORS/2026-133` dans `Rail Lynx`, alors que `prd.md` L2125 et `Chapitre 10.md` L62 établissent que ce règlement (en vigueur le 24 août 2026) constitue le socle juridique du rail temps réel **`RTR`** (`N6`).
  - *Résolution* : Déplacer `Règlement n° 10 DORS/2026-133` de `N5` vers `N6` dans `SCH-10-02.puml` et regénérer `SCH-10-02.svg`.

- **`PRD-L2-004`** (`MAJEUR` · `schemas` · `ch14`) — **Écart de borne `≥ 4` (`CH-14`) contre `> 4` (`SCH-14-02.mmd`) sur `xagenthopcount`**.
  - *Faits vérifiés* : `Chapitre 14.md` (Tableau 14.1 L34, Tableau 14.2 L51, L62, L103, L114) coupe à `xagenthopcount >= xagentmaxhops = 4` (conforme à Tome 2 Figure 10), alors que `SCH-14-02.mmd` L14 (calqué sur `prd.md` L2796/L2861) teste `xagenthopcount > 4` (écart d'un saut).
  - *Résolution* : Harmoniser `SCH-14-02.mmd` L14 en `xagenthopcount ≥ 4` (et regénérer `SCH-14-02.png`).

- **`PRD-L2-005`** (`MAJEUR` · `schemas` · `ch15`) — **Séquence Saga et compensations incohérentes dans `SCH-15-02.puml`**.
  - *Faits vérifiés* : `SCH-15-02.puml` L35–L43 enchaîne `T1 → T2`, `faute T2`, `Point pivot P3`, `Finalisation T3` et `Compensations inverses C2 → C1`. Si `T2` échoue sans effet, seul `C1` s'exécute (comme dans `test_saga_10_faults.py` scénario 1 et Tableau 15.2, où `T3` est le pivot et `T4` la finalisation post-pivot).
  - *Résolution* : Corriger `SCH-15-02.puml` pour aligner les étapes et compensations sur `saga_orchestrator.py` / Tableau 15.2 (`T1`, `T2` pré-pivot, `T3` pivot, `T4` post-pivot ; faute `T2` → `C1`, ou faute pré-pivot `T3` → `C2 → C1` avant pivot `T4`) et regénérer `SCH-15-02.svg`.

- **`PRD-L2-006`** (`MAJEUR` · `schemas` · `ch15`) — **Confusion `L0–L1` / `P0–P1` et câblage erroné `Engagement irréversible → LAP` dans `SCH-15-03.mmd`**.
  - *Faits vérifiés* : `SCH-15-03.mmd` L6 étiquette `Lecture (L0–L1)` (confondant niveau d'autonomie et palier d'outil `P0–P1`, contre Tableau 15.3). Aux lignes 29–31, `N4` (`Engagement irréversible`) n'est relié qu'à `N7` (`Z3 · Patron LAP`) sans lien vers `Z2` (`idem-v1` + `UETR`), laissant entendre que tout engagement irréversible (y compris bancaire) transite par `LAP`.
  - *Résolution* : Remplacer `(L0–L1)` par `(P0–P1)` en `N2`, relier `N4` à `Z2` (`idem-v1` + `UETR`) et réserver la branche `Z3` (`LAP`) aux actifs physiques/exclusifs.

- **`PRD-L2-007`** (`MAJEUR` · `schemas` · `ch17`) — **`PKCE S256` et `iss RFC 9207` attribués à tort à l'échange `OBO RFC 8693` dans `SCH-17-01.puml`**.
  - *Faits vérifiés* : `SCH-17-01.puml` L20 annote l'appel arrière-plan `N2 -> N3` (`Échange OBO RFC 8693`) avec `(PKCE S256, iss RFC 9207)`. Ces deux mécanismes s'appliquent au flux d'autorisation frontal (`Authorization Code`, `RFC 9700`), pas au `grant_type=token-exchange` (`RFC 8693`).
  - *Résolution* : Déplacer `PKCE S256` et `iss RFC 9207` sur l'obtention initiale du jeton mandant (`RFC 9700`) et ne conserver que `subject_token`, `actor_token` (`SVID`), `aud` (`RFC 8707`) et `RAR` (`RFC 9396`) sur la flèche `OBO`.

- **`PRD-L2-008`** (`MAJEUR` · `coherence` · `ch13`) — **Désynchronisation entre `CH-13` (prose révisée `G5`) et `SCH-13-01`/`SCH-13-02`/`SCH-13-03`**.
  - *Faits vérifiés* : `FM-2` vaut `32,3 %` dans `CH-13` L92/Tab. 13.3 contre `32,4 %` dans `SCH-13-03.puml` L31 ; le surcoût multi-agents vaut `1,6×–6,2×` / `10×–45×` en prose contre `3×–15×` dans `SCH-13-01.svg` L70/L84 ; `24,7 % de bogues d'intégration SDK` (`SCH-13-02.svg` L25), `BPMN fromAi` / `10 appels` (`SCH-13-01.svg` L32/L44) et `Replit #1152` (`SCH-13-03.puml` L32) figurent dans les schémas mais disparaissent de la prose (qui omet aussi `Camunda 8.11`, `UiPath Maestro`, `Routine` `41,1 % → 96,3 %` et les dates `GA` de `prd.md` L2596/L2633).
  - *Résolution* : Synchroniser les 3 schémas de `CH-13` sur les chiffres vérifiés de la prose (`FM-2 = 32,3 %`, fourchettes de jetons cohérentes) et réconcilier les éléments de `prd.md` affichés dans les figures.

- **`PRD-L2-009`** (`MAJEUR` · `couverture_prd` · `ch14`) — **Omission de `DEC-007`, `ADR-015`, `PRR R-04` et `PRR R-05` dans `CH-14` et sur-affirmation normative dans `SCH-14-03.puml`**.
  - *Faits vérifiés* : `DEC-007` (présent dans `SCH-14-01.svg` L83), `ADR-015`, `PRR R-04` et `PRR R-05` (portes `EXIG-EVT-01..10` dans `matrice-exig-prr-c40.json` et `prd.md` L2777) sont absents de `Chapitre 14.md`. En outre, `SCH-14-03.puml` L55 qualifie `Simplex` de « conforme IEC 61508 et ISO 10218-1 », contredisant la réserve explicite de `Chapitre 14.md` L91 (normes `statut F`, patron préparatoire non certifiant).
  - *Résolution* : Ajouter `DEC-007`, `ADR-015`, `PRR R-04` et `PRR R-05` en section `14.3` et remplacer « conforme » par « préparatoire à » dans `SCH-14-03.puml`.

- **`PRD-L2-010`** (`MAJEUR` · `coherence` · `ch18`) — **Date divergente de `NIST IR 8547 Final` (`21 oct.` vs `27 oct. 2026`) et omissions d'identifiants `prd.md` dans `CH-18`**.
  - *Faits vérifiés* : `Chapitre 18.md` L41 (et `ch18-ancrage.md` `C18-13`) date `NIST IR 8547 Final` au `21 octobre 2026`, contre `27 octobre 2026` dans `prd.md` (L3439, L3467, L3501, L3544). De plus, `ANC-023` et `ANC-030` (présents dans `SCH-18-01.mmd` L6–L7), `ANC-040`, `ANC-043`, `DEC-012`, `SIG-010`, `SIG-011`, `SP 800-131A Rev. 3`, `Public Law 117-260` et `Europol/QSFF` manquent dans la prose de `CH-18`.
  - *Résolution* : Unifier la date exacte de `NIST IR 8547 Final` entre `prd.md`, `CH-18` et `Annexe C/N`, et consigner `ANC-023/030/040/043`, `DEC-012` et `SIG-010/011` dans `CH-18`.

- **`PRD-L2-011`** (`MAJEUR` · `couverture_prd` · `ch17`) — **Omissions de veille délégation et d'identifiants `prd.md` dans `CH-17`**.
  - *Faits vérifiés* : `Chapitre 17.md` omet les pistes de veille prescrites par `prd.md` L3278–L3305 (`agentproto`, `dawn`, `ID-JAG`, `Macaroons`, `Biscuit`, `RFC 9635` GNAP, `RFC 7523`, `arXiv 2605.30169`) ainsi que plusieurs cotes normatives (`ADR-005`, `ADR-012`, `ADR-015`, `ADR-018`, `EXIG-AUT-10`, `EXIG-AUT-16`, `EXIG-ORC-04`, `PRR S-04` isolé, `PRR S-14`, `PRR S-15`).
  - *Résolution* : Ajouter une sous-synthèse sur ces travaux de veille délégation en `17.2.1` et compléter le Tableau 17.3 avec les cotes `EXIG-AUT-10`, `EXIG-ORC-04`, `ADR-018` et `PRR S-04`.

- **`PRD-L2-012`** (`MAJEUR` · `coherence` · `ch16`) — **Divergence de sens sur `0/15`, omissions `prd.md` et qualification `OAuth 2.1` dans `SCH-16-01.svg`**.
  - *Faits vérifiés* : `Chapitre 16.md` L15/L40 interprète `0/15` comme `3 mécanismes × 5 questions` (`Tome 1 Tableau 14.2`, lissage `G5`) et omet le verdict du passeport virtuel (`1` pleine / `4` partielles), alors que `prd.md` L3097 parle de « 15 mécanismes audités ». Manquent aussi `EXIG-IAM-09`, `EXIG-IAM-16`, `NIST SP 800-207`, `ANC-022`, `SIG-003` et `arXiv:2509.01063`. Enfin, `SCH-16-01.svg` L49 affiche « Socle OAuth 2.1 / BCP 240 », alors que `CH-16` L48 rappelle qu'`OAuth 2.1` reste un brouillon au gel.
  - *Résolution* : Expliciter la réconciliation `0/15` et le bilan `1/4` du passeport, intégrer les cotes manquantes (`EXIG-IAM-09`, `NIST SP 800-207`, `ANC-022`, `SIG-003`) et corriger `OAuth 2.1` en `OAuth 2.0 (BCP 240 / RFC 9700)` dans `SCH-16-01.svg`.

- **`PRD-L2-013`** (`MAJEUR` · `schemas` · `ch11`) — **Flèches manquantes sur la mémoire sémantique (`SCH-11-01.puml`) et cote tronquée `EXIG` (`SCH-11-03.puml`)**.
  - *Faits vérifiés* : Dans `SCH-11-01.puml` (L49–L50), l'écriture validée `HMAC` (`N2 --> N4`) et la purge légale (`N8 --> N4`) visent uniquement `Z2` (épisodique), omettant `Z3` (sémantique, `N5`) contrairement à `prd.md` L2346 et `Chapitre 11.md` L47/L64/L114. Dans `SCH-11-03.puml` L30, le titre de `Z1` comporte `EXIG` sans numéro (`EXIG-ARC-16 / EXIG-ARC-23`) et `N6` (`Pool`) n'a pas de flèche vers `N7`.
  - *Résolution* : Ajouter `N2 --> N5` et `N8 --> N5` dans `SCH-11-01.puml`, compléter `EXIG-ARC-16 / EXIG-ARC-23` et `N6 --> N7` dans `SCH-11-03.puml`, puis regénérer les SVG.

### Constats MINEURS

- **`PRD-L2-014`** (`MINEUR` · `couverture_prd` · `ch10`) — Mentionner `SIG-110` comme signal de révision de `CAP-015` (distinct de la coexistence `60 j` d'`EXIG-INT-14`), indiquer la dépendance `← CH-29` (plongements ouverts pour `Cognitive DR`) au Tableau 10.3 et clarifier la source exacte de la mesure `27,9 %` (`Yuan et coll., 2026` dans `prd.md` vs « auteur unique » en L19).
- **`PRD-L2-015`** (`MINEUR` · `couverture_prd` · `ch12`) — Reporter `CAP-033` (présent dans `SCH-12-03.svg` L26) dans la prose et les Tableaux 12.2/12.3 de `CH-12`, préciser `Cedar` pour les politiques embarquées de la cellule Edge (L69) et mentionner `IEEE P3945.1` (`prd.md` L2425).
- **`PRD-L2-016`** (`MINEUR` · `couverture_prd` · `ch11`) — Mentionner les lignées `MemGPT` (pour `Letta`) et `Zep` (pour `Graphiti`) en `CH-11` L55 pour la traçabilité avec `prd.md` L2274.
- **`PRD-L2-017`** (`MINEUR` · `couverture_prd` · `ch13`) — Inscrire explicitement les cotes `AP-07` et `AP-09` (`prd.md` L2610) lors de l'énumération des anti-patrons en `CH-13` L60.
- **`PRD-L2-018`** (`MINEUR` · `schemas` · `ch10`) — Qualifier les références brutes aux Tomes dans quatre schémas : `§45.12` (`SCH-10-02.puml` L46), `§39.5` (`SCH-11-02.puml` L36), `§ 22.10` (`SCH-13-01.svg` L49) et `T21.3` (`SCH-18-02.svg` L45).
- **`PRD-L2-019`** (`MINEUR` · `edition` · `ch18`) — Corriger la faute d'accord *« et **son** neutralisation »* → *« **sa** neutralisation »* (`Chapitre 18.md` L122) et remplacer l'anglicisme `automation` par `automatisation` dans `SCH-18-01.mmd` L32.
- **`PRD-L2-020`** (`MINEUR` · `edition` · `ch17`) — Remplacer les anglicismes isolés dans le lot : `antipattern` (`CH-17` L5 → `anti-patron`), `workflows` (`CH-13` L80 → `flux`), `playbooks` (`CH-16` L125 → `procédures de réponse` / `manuels opératoires`).
- **`PRD-L2-021`** (`MINEUR` · `edition` · `ch13`) — Harmoniser le gabarit entre Partie IV (`CH-10–12`), Partie V (`CH-13–15`) et Partie VI (`CH-16–18`) : encadré `> **Clause non-avis (`AO-05`)**` absent dans `CH-13–18`, titres `X.1` hétérogènes, et renvois de plomberie interne (`hors socle L+`, `aq/rapports-g0.json`, `sources/chXX-sources.md`, `AO-01`, `AO-08`) trop présents dans le corps pédagogique de `CH-13–16`.
- **`PRD-L2-022`** (`MINEUR` · `edition` · `ch14`) — Harmoniser la notation mathématique : `CH-13` (`7`), `CH-14` (`10` inline + `1` bloc `\[...\]`), `CH-15` (`4`), `CH-17` (`4`) et `CH-18` (`11`) emploient des délimiteurs LaTeX `\(...\)` / `\[...\]`, alors que `CH-10–12` et `CH-16` n'en contiennent aucun ; vérifier le rendu final ou convertir les notations simples en Unicode (`O(1)`, `O(n²)`, `κ = 0,88`).
- **`PRD-L2-023`** (`MINEUR` · `coherence` · `ch16`) — Aligner `SCH-16-02.svg` L13 (`A2A v1.0.0`) sur `A2A v1.0.0 / v1.0.1` (`CH-16` L69 / Tableau 16.1) et documenter en Annexe C la mise à jour `draft-ietf-oauth-transaction-tokens-09` (`prd.md` L3279) → `-11` (`CH-17`/`CH-18`).
