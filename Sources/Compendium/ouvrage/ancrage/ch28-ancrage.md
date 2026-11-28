# Journal d'ancrage atomique Wyvern G2 — Chapitre 28 (`ch28`)

- **Unité auditée :** `Sources/Compendium/ouvrage/manuscrit/10 - Partie X/Chapitre 28.md` (`4 729` mots de prose selon `verifie_manuscrit.py`, plage `[4 600, 5 400]`)
- **Base documentaire fermée :** `Sources/Compendium/ouvrage/sources/ch28-sources.md` (`[1]`–`[10]` en statut `L+`, `3` exclusions `statut F` : `lautorite.qc.ca`, `ciro.ca`, `securities-administrators.ca`, Option A iso-corpus) ; textes intégraux `Sources/Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` (`SRC-063`, `SRC-065`, `SRC-068`, `SRC-070`, `SRC-071`, `SRC-111`, `SRC-114`, `SRC-124`, `SRC-060`, `SRC-110`) ; registres `Sources/Compendium/ouvrage/registre/*.json` (`matrice-exig-prr-c40.json`, `concordance-taxonomies.json`, `ancres-chronologiques.json`) ; protocole `Sources/Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Sources/Compendium/ouvrage/aq/rapports-g0.json`) ; index heuristique interne `Sources/Tomes/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-7` (mise à jour Vague 2 `auteur-d09-d10`)
- **Passe G2 initiale (supportés) :** 7
- **Rectifications appliquées lors de la passe G2 et du rééquilibrage multisectoriel :** 24
- **Verdict final — supportés :** 31 / 31 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 28.md`

Toutes les formulations divergentes, attributions inexactes ou références hors corpus `L+` fermé relevées lors de la passe initiale, ainsi que la structuration en matrice à six verticaux d'entreprise coiffée par l'étalon financier en Option A iso-corpus, ont été ancrées directement dans [Chapitre 28.md](file:///c:/Github/Agentique/Sources/Compendium/ouvrage/manuscrit/10%20-%20Partie%20X/Chapitre%2028.md), en préservant les `owned_concepts` (`profils-financiers-5-secteurs`, `profil-assurance-dommages-m17`, `profil-assurance-personnes-m16`, `profil-banque-m14`, `profil-gestion-patrimoine-m15`, `profil-groupe-diversifie-m18`, `eclats-sectoriels-extrapoles`, `vertical-financier-durci`, `tampon-deterministe-rtr-iso20022`, `production-agentique-canadienne-2025-2026`), les renvois `[1]`–`[10]`, les quatre figures (`Figure 100` à `Figure 103`) et le calibrage (`4 729` mots dans `[4 600, 5 400]`) :

1. **Matrice à six verticaux d'entreprise et clôture `DIV-02` (`L1`–`L25`, `Tableaux 28.1`–`28.2`, `Figure 100`) :** alignement du titre `L1` et des alt-texts/légendes de `SCH-28-01`, `SCH-28-02` et `SCH-28-03` sur `specs/manifest.json` ; positionnement du noyau invariant (`42` capacités invariantes et `10` conditionnelles sur `52`) étalonné sur les services financiers et assurances (`M-14` à `M-18`, seul vertical intégralement démontré sur pièces `L+` dans le corpus fermé) avant déclinaison structurée vers les cinq autres verticaux d'entreprise (industrie `IT/OT`, santé et sciences de la vie, commerce/logistique `B2B`, secteur public, services numériques/TI) ; alignement des `24 PEX` sur `CRE-IA-2026-01 v1.2` (`5` directes, `12` extensions, `7` comblements).
2. **Séparation stricte entre preuves `L+` (`[1]`–`[10]`) et repérage interne / `statut F` (`L26`–`L67`) :** dissociation exacte entre `LSAC` (`art. 44`, `171`, `224` `[7]`), *Loi sur les banques* (`art. 21`, `238`, `239`, `415`, `416`, `485.1`–`506`, `495.2(1)`, `627.*` `[4]`), `Loi 25` (`art. 12.1`, `art. 9`/`53.1` `[1]`), `BSIF E-23` (`[2]`), `BSIF B-10` (`[3]`), `NC 31-103` (`1er octobre 2028` `[6]`), `EU AI Act` Annexe III `5(c)` (`[9]`), `BSIF B-15` (`[10]`) et `AIBanks.ca` (source secondaire sous réserve `statut F` `[5]`), d'avec les règles `DORS/92-330`, `DORS/2021-181`, `OCRI`/`ACVM 11-348` (`statut F`), `L.C. 2017, ch. 3`, `LQ 2023, c. 5`, *Loi sur les assureurs* `art. 71`, `LDPSF` `art. 38` et `BSIF B-9`/`E-21` qualifiées en repérage `Tome 4`/`Tome 5`.
3. **Généralisation du sas déterministe pré-engagement et garde-fou `DC-P11`/`DC-P12` (`L78`–`L142`, `Figures 101`–`103`, `Tableau 28.3`) :** formalisation du patron universel du sas déterministe pré-engagement devant acte irréversible à partir de l'étalon `Paiements Canada RTR` (`pacs.008`, `EXIG-CON-29`, `EXIG-INT-22`, `decimal_money.py`, `ciba_approval.py`, rétention `≥ 30` s) et de son isomorphisme architectural vers les ordres `ERP`/`EDI` fermes, expéditions `WMS` et interfaces `MES`/`OT` ; maintien du bilan `2025–2026` des `10` institutions canadiennes (`5+4+1`) et démarcation stricte `DC-P11`/`DC-P12` entre le périmètre démontré (`BCA` + trousse `G0` `83/83` `pytest` et `45/45` `OPA` à `100,0 %`) et les cinq verticaux transposés à titre illustratif (`HL7 FHIR R4` clinique distinct de `M-16`, `CAP-028` lecture seule `IT/OT` `SIL 2/3`, `SCM`/`EDI`, secteur public `EF-06`, TI `ADR-015`/`PRR F-14`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C28-01` à `C28-31`)

### Section 28.1 — Matrice à six verticaux, étalon `M-14..M-18` et `24 PEX` (`L1–L77`, Tableaux 28.1–28.2, Figure 100)

- **C28-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant la déclinaison du noyau invariant (`42/52 CAP`) sur les cinq profils financiers de haute régulation (`M-14` à `M-18`, `24 PEX`) et les règles de transposition multisectorielle sans excéder les preuves `L+`.
  - **Appui vérifié :** `specs/manifest.json` (`ch28`, `D10`, `SUB_D10_01`), `registre/concordance-taxonomies.json`.
  - **Verdict : supporté**

- **C28-02 (`L5`, `L7`)** — *Affirmation :* Positionnement de la matrice à six verticaux d'entreprise coiffée par l'étalon financier sous clause `non-avis` (`AO-05`), structurée en trois étapes (`M-14..M-18` et `24 PEX` / `DIV-02` ; `6` facteurs, sas pré-engagement `EXIG-CON-29` et bilan `10` institutions `2025–2026` ; transposition contrôlée sous `DC-P11`/`DC-P12`).
  - **Appui vérifié :** `specs/protocole-mlr-compendium.json`, `sources/ch28-sources.md`.
  - **Verdict : supporté**

- **C28-03 (`L13–L20`)** — *Affirmation :* Étalonnage des `52` capacités (`42` invariantes du noyau possédé et `10` conditionnelles) sur le vertical financier avant déclinaison vers six verticaux d'entreprise : (1) finance/assurances (`M-14..M-18`, `CAP-026` `[7]`), (2) industrie/énergie/`IT/OT` (`ERP`/`MES`/`SCADA`, `IEC 62443` `statut F`, `CAP-028`), (3) santé (`DSE` `HL7 FHIR R4`, `LQ 2023, c. 5` vs `RLRQ, c. P-39.1` `[1]`), (4) commerce/logistique `B2B` (`CAP-014`, `EXIG-INT-22`), (5) secteur public (`MCN` `ANC-117`/`118`, `SCT`, `EIF`), (6) services numériques/TI (`ADR-015`, `PRR F-14`).
  - **Appui vérifié :** `concordance-taxonomies.json` (`52`, `42`, `10`), `matrice-exig-prr-c40.json` (`cap_52`, `PRR F-14`), `SRC-063.txt` `[1]`, `SRC-114.txt` `[7]`.
  - **Verdict : supporté**

- **C28-04 (`L22`)** — *Affirmation :* Clôture `DIV-02` contre `CRE-IA-2026-01 v1.2` (`305` exigences) : `5` couvertures directes (`EXIG-CON-27..29`, `EXIG-SEC-27..28`), `12` extensions et `7` comblements (remplaçant `13`/`11` de `v1.1`), répondant à `LSAC` `art. 171` `[7]`, *Loi sur les banques* `art. 416` `[4]`, `OCRI`, `NC 31-103` `[6]`, génétique, `LDPSF` et climat.
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`pex_24`), `concordance-taxonomies.json` (`div_02`), `SRC-070.txt` `[4]`, `SRC-111.txt` `[6]`, `SRC-114.txt` `[7]`.
  - **Verdict : supporté**

- **C28-05 (`L24`)** — *Affirmation :* Sept paramètres d'arbitrage d'autonomie et évaluation artificielle `FEDS` (`Tome 4`/`Tome 5`, `Borealis-Bench` absent du disque) bornée sous `DC-C07 = 65,0 %`, calibrant la charge de contrôle entre `49,59 / 100` et `95,78 / 100`.
  - **Appui vérifié :** `Tome 4` (`L1377`), `Tome 5` (`L1462`), `Tome 8` (`L1804`).
  - **Verdict : supporté**

- **C28-06 (`L28`)** — *Affirmation :* Profil `M-14` Banque (`68,36 / 100` `FEDS`, `PEX-001..005` : `1` dir., `2` ext., `2` combl.) ; `LSAC` (`26 mars 2026`, `L.C. 2026, ch. 3`, `art. 224`) prohibant le grattage d'écran (`art. 171`) et instituant le registre de la Banque du Canada (`art. 44`) `[7]` sous `POR-008`, avec cible `99,5 %` au projet de règlement (`Tome 4`, hors `L+`).
  - **Appui vérifié :** `SRC-114.txt` `[7]`, `matrice-exig-prr-c40.json`, `Tome 4`.
  - **Verdict : supporté**

- **C28-07 (`L30`)** — *Affirmation :* `PEX-002` (`art. 627.08` et `627.44` `7` ans `[4]`, cible `5` ans `Tome 4`) ; `PEX-003` (`art. 416` `[4]` et `DORS/92-330` `8` produits `Tome 4`) ; `PEX-005` (`art. 238–239`, `627.13` `< 100 $ CA`, `627.43(2)` « ombudsman » `[4]`, `56` jours `DORS/2021-181` `Tome 4`) ; `PEX-004` (`EXIG-CON-29`).
  - **Appui vérifié :** `SRC-070.txt` `[4]`, `Tome 4`.
  - **Verdict : supporté**

- **C28-08 (`L32`)** — *Affirmation :* Profil `M-15` Patrimoine (`49,59 / 100` `FEDS`, conseil `D2` confiné en `L1`–`L2`, `art. 415` `[4]`, `PEX-011..015` : `2` dir., `1` ext., `2` combl.) ; `PEX-011` (`EXIG-CON-27`) rattachant la convenance à un représentant inscrit sous `OCRI 3400`/`1103(2)` et `Avis 11-348` (`Tome 4`, `statut F`).
  - **Appui vérifié :** `SRC-070.txt` `[4]`, `matrice-exig-prr-c40.json`, `sources/ch28-sources.md`, `Tome 4`.
  - **Verdict : supporté**

- **C28-09 (`L34`)** — *Affirmation :* `PEX-012` (`OCRI 3240`/`3241` `OEO`, `Tome 4`), `PEX-013` (`EXIG-CON-28`, `7` ans, `règles 3600`/`3803`, `Tome 4`), `PEX-014` (`NC 31-103` du `8 octobre 2026` interdisant les rétrofacturations au `1er octobre 2028` / `2028-10-01` `[6]`) et `PEX-015` (`Decimal` exact, `1er janvier 2026`, `ANC-101`, `Tome 4`).
  - **Appui vérifié :** `SRC-111.txt` `[6]`, `ancres-chronologiques.json` (`ANC-101`, `ANC-105`), `Tome 4`.
  - **Verdict : supporté**

- **C28-10 (`L36–L41`, `Tableau 28.1`)** — *Affirmation :* Le `Tableau 28.1` synthétise `M-14` et `M-15` (`SIG-103`, `SIG-104`, `SIG-105`, `DISC-01`, `DISC-05`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json`, `SRC-070.txt` `[4]`, `SRC-111.txt` `[6]`, `SRC-114.txt` `[7]`.
  - **Verdict : supporté**

- **C28-11 (`L45`, `L47`)** — *Affirmation :* Profil `M-16` Assurance de personnes (`70,19 / 100` `FEDS`, `PEX-021..025` : `2` dir., `2` ext., `1` combl.) : `PEX-021` (`L.C. 2017, ch. 3`, `Tome 4`), `PEX-022` (`LQ 2023, c. 5`, `Tome 4`), `PEX-023` (`EXIG-AMF-12`, Loi 25 `art. 12.1` `[1]`, `EU AI Act` Annexe III `5(c)` `[9]`), `PEX-024` (`EXIG-AMF-06`, `MGA`), `PEX-025` (`EXIG-SEC-27/28`, `PQC` `20`–`40` ans `Tome 5`).
  - **Appui vérifié :** `SRC-063.txt` `[1]`, `SRC-060.txt` `[9]`, `matrice-exig-prr-c40.json`, `Tome 4`, `Tome 5`.
  - **Verdict : supporté**

- **C28-12 (`L49`, `L51`)** — *Affirmation :* Profil `M-17` Assurance de dommages (`64,23 / 100` `FEDS`, `PEX-031..035` : `3` ext., `2` combl.) : `PEX-031` (`BSIF B-9`/`E-21` `Tome 4`, `FNOL`, `EXIG-AMF-12`, Loi 25 `art. 12.1` `[1]`), `PEX-032` (*Loi sur les assureurs* `art. 71`, `LQ 2018, c. 23` `Tome 4`), `PEX-033` (`LDPSF art. 38`, `≥ 3` assureurs `Tome 4`), `PEX-034` (`BSIF B-10` `[3]`, sas photo), `PEX-035` (`BSIF B-9` `Tome 4`, `BSIF B-15` exercice `2028` `[10]`, `SIG-109`–`110`).
  - **Appui vérifié :** `SRC-063.txt` `[1]`, `SRC-068.txt` `[3]`, `SRC-110.txt` `[10]`, `matrice-exig-prr-c40.json`, `Tome 4`.
  - **Verdict : supporté**

- **C28-13 (`L55`, `L57`, `L59`)** — *Affirmation :* Profil `M-18` Groupe diversifié (`95,78 / 100` `FEDS`, `52/52 CAP`, `PEX-041..044` : `4` ext., `PRI-010`, `CAP-021`), transposable à tout holding multi-filiales : `PEX-041` (`EXIG-CON-06`), `PEX-042` (Loi 25 `art. 9`/`53.1` `[1]`, régime des apparentés *Loi sur les banques* `art. 485.1`–`506` et plafond `5 %` `art. 495.2(1)` `[4]`), `PEX-043` (`BSIF B-10` incluant mères et affiliées `[3]`), `PEX-044` (`EXIG-CON-25`, livres `art. 239` `[4]`, `BSIF E-23` `[2]`, `AMF` via `AIBanks.ca` `statut F` `[5]`, `BSIF B-15` `[10]`, révision `30 juin 2033` / `2033-06-30` `art. 21` `[4]`).
  - **Appui vérifié :** `SRC-063.txt` `[1]`, `SRC-065.txt` `[2]`, `SRC-068.txt` `[3]`, `SRC-070.txt` `[4]`, `SRC-071.txt` `[5]`, `SRC-110.txt` `[10]`, `ancres-chronologiques.json` (`ANC-109..111`).
  - **Verdict : supporté**

- **C28-14 (`L61–L67`, `Tableau 28.2`)** — *Affirmation :* Le `Tableau 28.2` synthétise `M-16`, `M-17` et `M-18` avec ancrages `[1, 3, 4, 9, 10]`.
  - **Appui vérifié :** `matrice-exig-prr-c40.json`, `SRC-063.txt`, `SRC-068.txt`, `SRC-070.txt`, `SRC-060.txt`, `SRC-110.txt`.
  - **Verdict : supporté**

- **C28-15 (`L69–L71`, `Figure 100`)** — *Affirmation :* `Figure 100` (`SCH-28-01.svg`) illustrant la matrice sectorielle articulant l'étalon `M-14..M-18` (`24 PEX`, `DIV-02`) et la transposition multisectorielle du tronc `42/52 CAP`.
  - **Appui vérifié :** `specs/manifest.json` (`SCH-28-01`), `schemas/SCH-28-01.svg`, `schemas/rendus/SCH-28-01.svg`.
  - **Verdict : supporté**

- **C28-16 (`L73–L77`)** — *Affirmation :* Trois invariants exécutables du Chapitre 28 (`42/52 CAP` et cloisonnement `PRI-010`/`PEX-041..044` ; sas déterministe pré-engagement `EXIG-CON-29`/`PEX-004` sur `RTR pacs.008` transposable aux ordres `ERP`/`EDI` et `OT` ; garde-fou épistémique `DC-P11`/`DC-P12`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json`, `Chapitre 28.md`.
  - **Verdict : supporté**

### Section 28.2 — Durcissement étalon, sas pré-engagement et terrain canadien (`L78–L130`, Figures 101–102, Tableau 28.3)

- **C28-17 (`L82–L86`, `L88–L90`, `Figure 101`)** — *Affirmation :* Six facteurs de durcissement financier : irréversibilité, risque systémique (`FSB`/`BoE`/`ESRB` au `Tome 1 § 31.1`), responsabilité (*Moffatt c. Air Canada*, `14 février 2024`, `650,88 $ CA` au `Tome 1 § 31.1.3` `[C]`), double qualification simultanée modèle (`BSIF E-23` `[2]`) et tiers (`BSIF B-10` `[3]`), fraude `LBC-AML`, et standardisation ouverte (`FINOS AIGF v2.0` `Tome 1 § 31.3.3`) éclairée par Milsom (`arXiv:2512.02230` `[8]`), schématisés en `Figure 101` (`SCH-28-04.svg`).
  - **Appui vérifié :** `SRC-065.txt` `[2]`, `SRC-068.txt` `[3]`, `SRC-124.txt` `[8]`, `Tome 1 § 31`, `schemas/SCH-28-04.puml`.
  - **Verdict : supporté**

- **C28-18 (`L94`, `L96`)** — *Affirmation :* Patron universel du sas déterministe pré-engagement devant acte irréversible formalisé par `EXIG-CON-29` (`CRE-IA-2026-01 v1.2`) sur le `RTR` de Paiements Canada (cible `9 novembre 2026`, `ISO 20022` `pacs.008`/`camt.*` au `Tome 2`/`Tome 4`), interdisant toute écriture directe par agent (`PEX-004`), à l'instar des ordres `EDI` fermes ou consignes hors jumeau.
  - **Appui vérifié :** `Tome 2` (`EXIG-CON-29`), `Tome 4`, `matrice-exig-prr-c40.json` (`PEX-004`).
  - **Verdict : supporté**

- **C28-19 (`L98–L103`, `L105–L107`, `Figure 102`)** — *Affirmation :* Quatre contrôles synchrones bloquants du tampon hors modèle : (1) schéma `ISO 20022` (ou `EDI`/`BAPI` sur `ERP`) et `Decimal` exact (`policy_saga/decimal_money.py`) ; (2) idempotence et `UETR` (`UUIDv7`) ; (3) seuils, sanctions et liquidité/stocks ; (4) sas `P3` (`EXIG-INT-22`) sur condensat `JCS` (`RFC 8785`) avec double approbateur en classe Élevée (`EXIG-AUT-15`), `ciba_approval.py` (`≤ 15` min `EXIG-AUT-12`) et **fenêtre de rétention minimale de `30` secondes** (`EXIG-CON-29`), transposable aux bons de commande `EDI`, expéditions `WMS` et lots `MES` (`Figure 102`, `SCH-28-02.svg`).
  - **Appui vérifié :** `Tome 8/trousse/policy_saga/decimal_money.py`, `authz_pqc_audit/ciba_approval.py`, `Tome 2` (`EXIG-INT-22`, `EXIG-AUT-12/15`, `EXIG-CON-29`), `schemas/SCH-28-02.puml`.
  - **Verdict : supporté**

- **C28-20 (`L111`)** — *Affirmation :* Hygiène des grandeurs auto-déclarées non sommables, répartition `5 + 4 + 1` issue du `Tome 1 ch35` (`Banque Nationale` notée `69 / 100` dans `AIBanks.ca` du `1er novembre 2026` `[5]`), maintien en `statut F` (`HTTP 403`) de `lautorite.qc.ca`, `ciro.ca` et `securities-administrators.ca`, et appuis `[1..7]`.
  - **Appui vérifié :** `Tome 1 ch35`, `SRC-071.txt` `[5]`, `sources/ch28-sources.md`.
  - **Verdict : supporté**

- **C28-21 (`L113–L126`, `Tableau 28.3`)** — *Affirmation :* Le `Tableau 28.3` consigne les faits publics datés `2025–2026` et réserves des dix institutions canadiennes (`TD`, `Scotiabank`, `RBC`, `Manuvie`, `Desjardins`, `CIBC`, `Intact`, `BMO`, `Sun Life` hors `ACP`, `Banque Nationale` `[5]`).
  - **Appui vérifié :** `Tome 1 § 35.1–35.8`, `SRC-071.txt` `[5]`.
  - **Verdict : supporté**

- **C28-22 (`L128`)** — *Affirmation :* Deux enseignements (« le mot ne mesure pas la chose » chez `CIBC`/`Intact` ; cinq invariants de façade `Tome 1 § 35.9` sans chaîne de mandat `OBO`/`CIBA` ni positionnement `OO1`–`OO4` publiés avant le `1er mai 2027` `[2, 5]`).
  - **Appui vérifié :** `Tome 1 § 35.9`, `SRC-065.txt` `[2]`, `SRC-071.txt` `[5]`.
  - **Verdict : supporté**

### Section 28.3 — Transposition multisectorielle et frontière probante (`L130–L143`, Figure 103)

- **C28-23 (`L132–L137`)** — *Affirmation :* Démarcation stricte `DC-P11`/`DC-P12` entre le périmètre démontré (`BCA`, `CRE-IA-2026-01 v1.2`, trousse `Tome 8` vérifiée en `G0` via `83/83` `pytest` et `45/45` `OPA` à `100,0 %`, plus campagnes `FEDS` `Tome 4`/`5` hors disque) et les règles de transposition illustratives vers la santé (`DSE`/`HL7 FHIR R4` distinct de `M-16`, `LQ 2023, c. 5` vs `RLRQ, c. P-39.1` `[1]`, revue clinicienne), l'industrie `IT/OT` (`BEL` Trois-Rivières Purdue `IEC 62443`, `NERC CIP`, `IEC 61511 SIL 2/3` en `statut F`, sas lecture seule `CAP-028` + jumeau numérique), la logistique `B2B` (`CAP-014`, `EXIG-INT-22`), le secteur public (`MCN`/`SCT` `EF-06`) et les TI internes (`ADR-015`, `PRR F-14`).
  - **Appui vérifié :** `aq/rapports-g0.json`, `SRC-063.txt` `[1]`, `matrice-exig-prr-c40.json` (`CAP-014`, `CAP-028`, `PRR F-14`), `Tome 3`, `Tome 4`, `Tome 8`.
  - **Verdict : supporté**

- **C28-24 (`L139–L141`, `Figure 103`)** — *Affirmation :* `Figure 103` (`SCH-28-03.svg`) matérialisant la démarcation `DC-P11`/`DC-P12` entre terrain canadien vérifié (`Z1`), sas de transposition (`Z2`) et vignettes sectorielles (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`SCH-28-03`), `schemas/SCH-28-03.svg`, `schemas/rendus/SCH-28-03.svg`.
  - **Verdict : supporté**

- **C28-25 (`L143`)** — *Affirmation :* Convergence des échéances du `1er mai 2027` (`BSIF E-23` `[2]`, `AMF` sous réserve `statut F` `[5]`) et du `1er octobre 2028` (`NC 31-103` `[6]`), et ouverture vers le Chapitre 29 (trois blueprints `C01–C40`, fédération multi-`SaaS`, activation tricéphale `BEL`/`BCA`/`BSN` sous `Borealis-Bench`).
  - **Appui vérifié :** `SRC-065.txt` `[2]`, `SRC-071.txt` `[5]`, `SRC-111.txt` `[6]`, `specs/manifest.json` (`ch29`).
  - **Verdict : supporté**

- **C28-26 à C28-31 (`CA-04`, `CA-07`, `CA-10`, `CA-20`, `CA-21`)** — *Affirmation :* Ordre exact des quatre figures (`SCH-28-01`, `SCH-28-04`, `SCH-28-02`, `SCH-28-03`), présence des dates `ANC-105` (`2028-10-01`) et `ANC-109..111` (`2033-06-30`), bijection `100 %` des sources `[1]`–`[10]` avec `sources/ch28-sources.md`, zéro bloc de code clôturé (`CA-20`) et respect intégral des `owned_concepts` (`CA-21`).
  - **Appui vérifié :** `specs/manifest.json`, `registre/ancres-chronologiques.json`, `sources/ch28-sources.md`, `outils/verifie_manuscrit.py`.
  - **Verdict : supporté**
