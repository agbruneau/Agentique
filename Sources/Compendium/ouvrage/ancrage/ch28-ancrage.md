# Journal d'ancrage atomique Wyvern G2 — Chapitre 28 (`ch28`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/10 - Partie X/Chapitre 28.md` (`4 876` mots de prose `verifie_manuscrit` / `5 124` mots `parser_plan`, plage `[4 600, 5 400]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch28-sources.md` (`[1]`–`[8]` en statut `L+`, `3` exclusions `statut F` : `lautorite.qc.ca`, `ciro.ca`, `securities-administrators.ca`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` (`SRC-063`, `SRC-065`, `SRC-068`, `SRC-070`, `SRC-071`, `SRC-111`, `SRC-114`, `SRC-124`, ainsi que `SRC-060` et `SRC-110`) ; registres `Compendium/ouvrage/registre/*.json` (`matrice-exig-prr-c40.json`, `concordance-taxonomies.json`, `ancres-chronologiques.json`) ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-7`
- **Passe G2 initiale (supportés)** : 7
- **Rectifications appliquées lors de la passe G2 :** 22
- **Verdict final — supportés :** 29 / 29 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 28.md`

Toutes les formulations divergentes, attributions inexactes ou références issues de documents hors corpus `L+` fermé relevées lors de la passe initiale ont été réancrées ou qualifiées directement dans [Chapitre 28.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/10%20-%20Partie%20X/Chapitre%2028.md), en préservant les `owned_concepts` (`profils-financiers-5-secteurs`, `profil-assurance-dommages-m17`, `profil-assurance-personnes-m16`, `profil-banque-m14`, `profil-gestion-patrimoine-m15`, `profil-groupe-diversifie-m18`, `eclats-sectoriels-extrapoles`, `vertical-financier-durci`, `tampon-deterministe-rtr-iso20022`, `production-agentique-canadienne-2025-2026`), l'ensemble des renvois `[1]`–`[8]` et le calibrage dans `[4 600, 5 400]` :

1. **Clôture `DIV-02` (`v1.2`) et socle `42/52` capacités (`L13`, `L15`, `L21`–`L29`, `L40`–`L60`, `Tableaux 28.1`–`28.2`) :** précision du socle cible (`52` capacités dont `42` invariantes du noyau possédé et `10` conditionnelles) ; alignement des décomptes `PEX` sur la matrice synchronisée `CRE-IA-2026-01 v1.2` de `registre/matrice-exig-prr-c40.json` (`5` couvertures directes, `12` extensions et `7` comblements de lacunes 2026 — soit `M-14` `1/2/2`, `M-15` `2/1/2`, `M-16` `2/2/1`, `M-17` `0/3/2`, `M-18` `0/4/0` — résorbant l'ancien décompte `13` / `11` hérité de `v1.1` dans `concordance-taxonomies.json`, et levant l'incohérence interne de `M-15`).
2. **Séparation stricte entre textes vérifiés en `L+` et repérage `Tome 4` / `Tome 5` / `statut F` (`L21`–`L54`) :** dissociation de `LSAC` (`art. 44`, `171`, `224` dans `SRC-114.txt` `[7]`) d'avec l'objectif `99,5 %` et le délai `5` ans des consentements ouverts (projet de règlement, `Tome 4`, hors `L+`) ; dissociation de la *Loi sur les banques* (`art. 238`, `239`, `415`, `416`, `485.1`–`506`, `495.2(1)`, `627.08`, `627.13`, `627.43(2)`, `627.44`, `21` dans `SRC-070.txt` `[4]`) d'avec `DORS/92-330` et `DORS/2021-181` (`56` jours, `Tome 4`, hors `L+`) ; qualification explicite en repérage interne hors `L+` des règles `OCRI` / `ACVM 11-348` (`statut F` sur `ciro.ca` et `securities-administrators.ca`), des frais quotidiens `NC 31-103` au `1er janvier 2026` (`ANC-101` / `Tome 4`), ainsi que de `L.C. 2017, ch. 3`, `L.Q. 2023, c. 5`, `Loi sur les assureurs` `art. 71`, `LDPSF` `art. 38`, `BSIF B-9` et `E-21` ; précision de la base exacte de `BSIF B-10` (`SRC-068.txt` `[3]` incluant affiliées et sociétés mères dans les accords avec des tiers) et de la *Loi 25* (`art. 9` modifiant `art. 53.1` dans `SRC-063.txt` `[1]`).
3. **Six facteurs, étude Milsom `[8]` et tampon `RTR` (`L79`–`L94`) :** qualification des travaux `FSB`/`BoE`/`ESRB`, de *Moffatt v. Air Canada* (`650,88 $ CA`, régime `[C]`) et de `FINOS AIGF v2.0` comme repérage `Tome 1` hors `L+` ; correction grammaticale (`simultanée`) ; réancrage fidèle de `SRC-124.txt` (`[8]`, fiabilité de bout en bout des flux plutôt que calcul arithmétique et dérive d'autonomie) ; qualification du `9 novembre 2026` et des messages `ISO 20022` `RTR` (`Tome 2`/`Tome 4`, hors `L+`) ; distinction entre les fonctions exécutées dans la trousse du Tome 8 (`decimal_money.py` et `ciba_approval.py`) et les prescriptions de `EXIG-CON-29` (schéma `ISO 20022` et rétention minimale de `30` s).
4. **Terrain canadien `5+4+1`, erreur de renvoi `Desjardins [7]` et périmètre `Borealis-Bench` (`L17`, `L106`–`L142`, `Tableau 28.3`) :** rattachement du classement `5+4+1` au recensement `Tome 1 ch35` complété en `L+` par `AIBanks.ca` `[5]` (`SRC-071.txt`, notant `Banque Nationale` à `69/100`) ; suppression du renvoi fautif `[7]` sur la ligne `Desjardins` du `Tableau 28.3` ; retrait de l'allégation d'exécution locale de `Borealis-Bench` (absent du disque au `Tome 8`) au profit de la trousse exécutable vérifiée en `G0` (`83/83` tests `pytest` et `45/45` tests `OPA` à `100,0 %`, `aq/rapports-g0.json`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C28-01` à `C28-29`)

### Section 28.1 — Titre, ouverture, clôture `DIV-02` et cinq profils financiers (`L1–L73`, Tableaux 28.1–28.2, Figure 88)

- **C28-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant la déclinaison d'un noyau invariant sur cinq sous-secteurs financiers sans re-dérivation ni dépassement d'irréversibilité, et traçant la frontière entre preuves financières et extrapolations sectorielles.
  - **Appui vérifié :** `specs/manifest.json` (`ch28`, `D10`, `SUB_D10_01`), structure `§ 28.1`–`§ 28.3`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C28-02 (`L5`, `L7`)** — *Affirmation :* Épreuve du droit positif financier sur `5` sous-secteurs sous clause `non-avis` (`AO-05`), annoncée en trois sections (`M-14`–`M-18` et `24 PEX` / `DIV-02` ; `6` facteurs, `EXIG-CON-29` et bilan `2025–2026` ; frontière probante santé/`IT/OT`).
  - **Appui vérifié :** `specs/protocole-mlr-compendium.json`, `sources/ch28-sources.md` (`L5`), `Chapitre 28.md` (`L9–L142`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C28-03 (`L13`)** — *Affirmation :* Portabilité sans re-dérivation sur `M-14`–`M-18` du socle cible de `52` capacités (`CAP-001` à `CAP-052`, dont `42` invariantes du noyau possédé et `10` conditionnelles), avec branchement sémantique par domaine (`MISMO`, `ACORD`, `HL7 FHIR`, `CDM`).
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`bilan_chiffre` : `52`, `42`, `10`), `registre/matrice-exig-prr-c40.json` (`cap_52`).
  - **Passe initiale :** écart rectifié · **Action :** distingué les `42` capacités invariantes du noyau possédé et les `10` conditionnelles au sein des `52` capacités cibles · **Verdict : supporté**

- **C28-04 (`L15`)** — *Affirmation :* Clôture `DIV-02` contre `CRE-IA-2026-01 v1.2` (`305` exigences) selon la matrice synchronisée : `5` couvertures directes (après ajout d'`EXIG-CON-27` à `29` et `EXIG-SEC-27` à `28`), `12` extensions et `7` comblements (remplaçant `13`/`11` de `v1.1`), répondant notamment à la `LSAC` (`art. 171` `[7]`), *Loi sur les banques* (`art. 416` `[4]`), `OCRI`, `NC 31-103` `[6]`, génétique, `LDPSF` et climat.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`pex_24` : `5` Directe, `12` Extension, `7` Lacune 2026), `registre/concordance-taxonomies.json` (`div_02`), `SRC-114.txt` (`[7]`), `SRC-070.txt` (`[4]`), `SRC-111.txt` (`[6]`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la ventilation sur `matrice-exig-prr-c40.json` (`v1.2`), expliqué la résorption de l'ancien décompte `v1.1` et raccourci le syntagme pour supprimer la collision `CA-03` · **Verdict : supporté**

- **C28-05 (`L17`)** — *Affirmation :* Sept questions structurantes et évaluation artificielle `FEDS` issue du corpus interne (`Tome 4`/`Tome 5`, banc `Borealis-Bench` absent du disque), bornée sous plafond `C07 = 65,0 %`, donnant des charges de contrôle de `49,59 / 100` à `95,78 / 100`.
  - **Appui vérifié :** `Corpus/Tome 4` (`L1377`), `Corpus/Tome 5` (`L1462`), `Corpus/Tome 8` (`L1804`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement les cotes `FEDS` au corpus interne (`Tome 4`/`Tome 5`) et signalé l'absence de `Borealis-Bench` sur disque · **Verdict : supporté**

- **C28-06 (`L21`)** — *Affirmation :* Profil `M-14` Banque (`68,36 / 100` `FEDS`, `PEX-001`–`005` : `1` directe, `2` extensions, `2` comblements en `v1.2`) ; `LSAC` promulguée le `26 mars 2026` (`L.C. 2026, ch. 3`, `art. 224`) prohibant le grattage d'écran (`art. 171`, entrée en vigueur par décret) et instituant le registre de la Banque du Canada (`art. 44`) `[7]`, sous `POR-008`, avec cible ouverte de `99,5 %` issue du projet de règlement (`Tome 4`, hors `L+`).
  - **Appui vérifié :** `SRC-114.txt` (`art. 44`, `171`, `224`), `registre/matrice-exig-prr-c40.json` (`pex_24`, `dapp_por_15`), `Corpus/Tome 4` (`L3234`, `L5452`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la ventilation `1/2/2` sur `v1.2`, vérifié `art. 44` en `[7]` et dissocié la cible `99,5 %` du projet de règlement (`Tome 4`) hors `[7]` · **Verdict : supporté**

- **C28-07 (`L23`, `L25`)** — *Affirmation :* `PEX-002` (consentement exprès par produit `art. 627.08` `[4]`, `7` ans pour dossiers de plainte `art. 627.44` `[4]`, cible `5` ans pour consentements ouverts au projet de règlement `Tome 4`) ; `PEX-003` (muraille bancassurance `art. 416` `[4]` et `DORS/92-330` `8` produits permis, `Tome 4`) ; `PEX-005` (livres au Canada `art. 238–239`, alertes `< 100 $ CA` `art. 627.13`, interdiction d'« ombudsman » `art. 627.43(2)` `[4]`, délai `56` jours `DORS/2021-181` `Tome 4`) ; `PEX-004` (`EXIG-CON-29`).
  - **Appui vérifié :** `SRC-070.txt` (`art. 238`, `239`, `416`, `627.08`, `627.13`, `627.43(2)`, `627.44`), `Corpus/Tome 4` (`L5453–5456`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié les articles vérifiés dans `[4]` des dispositions `DORS/92-330`, `DORS/2021-181` (`56` j) et du projet de règlement (`5` ans) issues du `Tome 4` hors `L+`, et scindé le paragraphe (`CA-05`) · **Verdict : supporté**

- **C28-08 (`L27`)** — *Affirmation :* Profil `M-15` Patrimoine (`49,59 / 100` `FEDS`, plafond `D2` verrouillé en exploitation bornée `L1`–`L2` sans autonomie fédérée inter-organisations, interdiction bancaire des valeurs mobilières `art. 415` `[4]`, `PEX-011`–`015` : `2` directes, `1` extension, `2` comblements) ; `PEX-011` (`EXIG-CON-27`) rattachant la convenance à une personne physique inscrite sous `OCRI 3400`/`1103(2)` et `ACVM 11-348` (`Tome 4`, hors `L+`, `ciro.ca` et `securities-administrators.ca` en `statut F`).
  - **Appui vérifié :** `SRC-070.txt` (`art. 415`), `registre/matrice-exig-prr-c40.json` (`PEX-011`..`015`), `registre/concordance-taxonomies.json` (`DISC-02`, `L132`), `sources/ch28-sources.md` (`L102–103`), `Corpus/Tome 4` (`L5457–5461`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé le décompte `2/1/2` (levant la contradiction interne), qualifié `OCRI` / `ACVM 11-348` comme repérage `Tome 4` hors `L+` face au `statut F` et retiré `stades 2–3` au lissage G5 (`DISC-02`) · **Verdict : supporté**

- **C28-09 (`L29`)** — *Affirmation :* `PEX-012` (`OCRI 3240`/`3241` `OEO`, `Tome 4`), `PEX-013` (`EXIG-CON-28`, `OCRI 3600`/`3803`, `7` ans, `Tome 4`), `PEX-014` (`NC 31-103` amendements du `8 octobre 2026` interdisant les rétrofacturations au `1er octobre 2028` `[6]`), et `PEX-015` (calcul quotidien en `Decimal` exact des frais entrés en vigueur le `1er janvier 2026`, `Tome 4`, ancre `ANC-101`).
  - **Appui vérifié :** `SRC-111.txt` (`[6]`, `8 oct. 2026`, `1er oct. 2028`), `registre/ancres-chronologiques.json` (`ANC-101`, `2028-10-01-GESTION-PATRIMOINE-RETROFACTURATION`), `Corpus/Tome 4` (`L5458–5461`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié les amendements vérifiés en `[6]` des règles `OCRI` et des amendements du `1er janvier 2026` issus du repérage `Tome 4` / `ANC-101`, et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C28-10 (`L31–L36`, `Tableau 28.1`)** — *Affirmation :* Le `Tableau 28.1` synthétise `M-14` (`1` dir., `2` ext., `2` combl.) et `M-15` (`2` dir., `1` ext., `2` combl.) avec ancrages vérifiés et mentions de repérage/`statut F`.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json`, `SRC-070.txt`, `SRC-111.txt`, `SRC-114.txt`.
  - **Passe initiale :** écart rectifié · **Action :** aligné les comptes `v1.2`, ajouté `art. 44` et `627.*`, et qualifié `DORS/92-330` et `OCRI` · **Verdict : supporté**

- **C28-11 (`L40`)** — *Affirmation :* Profil `M-16` Assurance de personnes (`70,19 / 100` `FEDS`, `PEX-021`–`025` : `2` directes, `2` extensions, `1` comblement en `v1.2`) ; `PEX-021` (caviardage déterministe pré-`CoALA` sous *Loi sur la non-discrimination génétique* `L.C. 2017, ch. 3`, `Tome 4`) et `PEX-022` (consentement exprès distinct borné dans le temps sous `L.Q. 2023, c. 5`, `Tome 4`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`PEX-021`..`025`), `Corpus/Tome 4` (`L3543–3560`, `L5462–5463`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la ventilation `2/2/1` et qualifié `L.C. 2017, ch. 3` et `L.Q. 2023, c. 5` en repérage `Tome 4` hors `L+` · **Verdict : supporté**

- **C28-12 (`L42`)** — *Affirmation :* `PEX-023` (`EXIG-AMF-12` et *Loi 25* `art. 12.1` `[1]`, en convergence avec l'Annexe III point `5(c)` du règlement européen sur l'IA `SRC-060`), `PEX-024` (`EXIG-AMF-06`, sociétés mandataires `MGA`) et `PEX-025` (`EXIG-SEC-27/28`, conservation bi-temporelle `PQC` sur cible longue `20` à `40` ans documentée au `Tome 5`).
  - **Appui vérifié :** `SRC-063.txt` (`art. 12.1`), `SRC-060.txt` (Annexe III `5(c)`), `registre/ancres-chronologiques.json` (`ANC-007`), `Corpus/Tome 5` (`L1417–1418`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché l'Annexe III `5(c)` à `SRC-060` et attribué la plage `20` à `40` ans à la cible du `Tome 5` · **Verdict : supporté**

- **C28-13 (`L44`, `L46`)** — *Affirmation :* Profil `M-17` Assurance de dommages (`64,23 / 100` `FEDS`, `PEX-031`–`035` : `0` directe, `3` extensions, `2` comblements en `v1.2`) : `PEX-031` (`BSIF B-9`/`E-21` `Tome 4`, `FNOL`, `EXIG-AMF-12`, `Loi 25` `art. 12.1` `[1]`), `PEX-032` (*Loi sur les assureurs* `art. 71`, `L.Q. 2018, c. 23`, `Tome 4`), `PEX-033` (`LDPSF art. 38`, `≥ 3` assureurs hors groupe, `Tome 4`), `PEX-034` (`BSIF B-10` `[3]`, sas multimodal) et `PEX-035` (`BSIF B-9` `Tome 4`, `BSIF B-15` `SRC-110` exercice `2028`, `SIG-109`–`110`).
  - **Appui vérifié :** `SRC-063.txt` (`[1]`), `SRC-068.txt` (`[3]`), `SRC-110.txt` (`BSIF B-15`), `registre/matrice-exig-prr-c40.json` (`PEX-031`..`035`), `Corpus/Tome 4` (`L5467–5471`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la ventilation `0/3/2` et qualifié les sources `Tome 4` hors `L+` ainsi que `SRC-110` pour `BSIF B-15` · **Verdict : supporté**

- **C28-14 (`L50`)** — *Affirmation :* Profil `M-18` Groupe financier diversifié (`95,78 / 100` `FEDS`, `52/52` capacités cibles, `PEX-041`–`044` : `4` extensions en `v1.2`, `PRI-010`, `CAP-021`), imposant de mutualiser une fois l'infrastructure technique sans données tout en maintenant des cloisons juridiques hermétiques par personne morale.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`PEX-041`..`044`, `PRI-010`, `CAP-021`), `Corpus/Tome 4` (`L5472–5475`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié les quatre propositions d'extensions en `v1.2` · **Verdict : supporté**

- **C28-15 (`L52`, `L54`)** — *Affirmation :* `PEX-041` (`EXIG-CON-06`, étiquette immuable d'entité), `PEX-042` (jeton de consentement manifeste, libre, éclairé, spécifique et présenté distinctement sous *Loi 25* `art. 9` modifiant `art. 53.1` `[1]`), Partie XI *Loi sur les banques* (`art. 485.1`–`506`, plafond `5 %` du capital réglementaire envers un apparenté non institutionnel à l'`art. 495.2(1)` `[4]`), `PEX-043` (`BSIF B-10` `[3]` incluant entités affiliées et sociétés mères dans les accords avec des tiers et exigeant des plans de sortie proportionnels), et `PEX-044` (`EXIG-CON-25`, livres `art. 239` `[4]`, `BSIF E-23` `[2]`, `AMF` `[5]`, `BSIF B-15` `SRC-110`, révision `30 juin 2033` `art. 21` `[4]`).
  - **Appui vérifié :** `SRC-063.txt` (`art. 9` / `53.1`), `SRC-070.txt` (`art. 21`, `239`, `485.1`–`506`, `495.2(1)`), `SRC-068.txt` (`affiliates`, `exit plans`), `SRC-065.txt` (`[2]`), `SRC-071.txt` (`[5]`), `SRC-110.txt` (`B-15`).
  - **Passe initiale :** écart rectifié · **Action :** précisé `art. 9` / `53.1` `[1]`, `art. 495.2(1)` `[4]`, `art. 21` / `239` `[4]`, `SRC-110` et reformulé fidèlement `BSIF B-10` `[3]` · **Verdict : supporté**

- **C28-16 (`L56–L62`, `Tableau 28.2`)** — *Affirmation :* Le `Tableau 28.2` synthétise `M-16` (`2` dir., `2` ext., `1` combl.), `M-17` (`0` dir., `3` ext., `2` combl.) et `M-18` (`0` dir., `4` ext., `0` combl.) avec ancrages exacts.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json`, `SRC-063.txt`, `SRC-068.txt`, `SRC-070.txt`.
  - **Passe initiale :** écart rectifié · **Action :** aligné les comptes `v1.2`, ajouté `art. 495.2` et qualifié les textes issus du repérage `Tome 4` · **Verdict : supporté**

- **C28-17 (`L64–L68`, `Figure 88`)** — *Affirmation :* La Figure 88 (`SCH-28-01.svg`) illustre les cinq ailes (`M-14`–`M-18`), leurs cotes `FEDS` et l'exécution des `24` verrous `PEX` autour du noyau mutualisé (`52/52 CAP`, `DIV-02`).
  - **Appui vérifié :** `specs/manifest.json` (`SCH-28-01`), `schemas/SCH-28-01.svg`, `schemas/rendus/SCH-28-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C28-18 (`L70–L73`)** — *Affirmation :* Trois invariants exécutables du Chapitre 28 : (1) cloisonnement juridique `PRI-010` / `PEX-041`–`044` sous `BSIF B-10`; (2) tampon déterministe hors modèle `EXIG-CON-29` / `PEX-004` avant `RTR` (`pacs.008`) avec `ISO 20022`, `Decimal`, `UETR`, antifraude et `P3` sur `JCS` (`≥ 30` s); (3) attribution datée, statuts bloqués sans contournement et frontière probante `HL7 FHIR R4` / `SIL 2/3`.
  - **Appui vérifié :** `Chapitre 28.md` (`L50–L54`, `L87–L96`, `L106–L138`), `registre/matrice-exig-prr-c40.json`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 28.2 — Durcissement financier, rail `RTR` et terrain canadien 2025–2026 (`L75–L125`, Tableau 28.3, Figure 89)

- **C28-19 (`L79`, `L81`, `L83`)** — *Affirmation :* Six facteurs de durcissement financier : irréversibilité, risque systémique (`FSB`/`BoE`/`ESRB` relevés au `Tome 1 § 31.1`), responsabilité (*Moffatt v. Air Canada*, `14 février 2024`, `650,88 $ CA`, repérage `Tome 1 § 31.1.3` `[C]`), double qualification simultanée modèle (`BSIF E-23` `[2]`) et tiers (`BSIF B-10` `[3]`), fraude `LBC-AML`, `FINOS AIGF v2.0` (`Tome 1 § 31.3.3`) et étude Milsom (`arXiv:2512.02230` `[8]`, limitée moins par le raisonnement arithmétique que par la fiabilité de bout en bout des flux et la dérive d'autonomie).
  - **Appui vérifié :** `SRC-065.txt` (`[2]`), `SRC-068.txt` (`[3]`), `SRC-124.txt` (`[8]`, `L17–24`, `abstract`), `Corpus/Tome 1` (`L7139`, `L7307`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `FSB`/`BoE`/`ESRB`, *Moffatt* (`[C]`) et `FINOS` comme repérage `Tome 1` hors `L+`, corrigé `simultanée` et aligné l'énoncé sur les conclusions exactes de `SRC-124.txt` (`[8]`) · **Verdict : supporté**

- **C28-20 (`L87`, `L89`)** — *Affirmation :* `EXIG-CON-29` (`CRE-IA-2026-01 v1.2`, nov. `2026`) encadrant le `RTR` de Paiements Canada (cible `9 novembre 2026` et spécification `ISO 20022` `pacs.008`/`camt.*` issues du repérage `Tome 2`/`Tome 4`, hors `L+`), dont l'irrévocabilité immédiate annule la compensation Saga et proscrit toute soumission directe par agent probabiliste (`PEX-004`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L6149–6155`), `Corpus/Tome 4` (`L3235`, `L5455`), `registre/matrice-exig-prr-c40.json` (`PEX-004`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié la cible `9 novembre 2026` et la spécification `ISO 20022` `RTR` comme repérage interne `Tome 2`/`Tome 4` hors `L+` · **Verdict : supporté**

- **C28-21 (`L91–L96`)** — *Affirmation :* Quatre contrôles synchrones bloquants du tampon hors modèle avant émission `RTR` : (1) contrôle `ISO 20022` (`EXIG-CON-29`) et conversion monétaire `Decimal` exacte sans flottant `IEEE-754` (`trousse/policy_saga/decimal_money.py`) ; (2) idempotence et `UETR` ; (3) antifraude et liquidité ; (4) en vertu d'`EXIG-INT-22` (tout paiement par agent relève de `P3` à zéro paiement automatisé sans l'utilisateur), signature humaine `P3` sur condensat `RFC 8785` (`JCS`) sur le rail `RTR` (`EXIG-CON-29`, double approbateur en classe Élevée sous `EXIG-AUT-15`), contrôle du jeton `CIBA`, de l'unicité `jti` et de l'expiration (`≤ 15` min selon `EXIG-AUT-12`, `trousse/authz_pqc_audit/ciba_approval.py`), avec dissociation temporelle complémentaire entre les contrôles synchrones (`ms` `PEP` `Tome 5`) et la **fenêtre de rétention minimale de `30` secondes** ajoutée par `EXIG-CON-29` sur `RTR` (`pacs.008`) en complément du mandat `P3` d'`EXIG-INT-22` (rejet propre à zéro sortie sur échec, refus ou `exp ≤ now_ts`).
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/policy_saga/decimal_money.py` (`L1–39`), `Tomes/Tome 8 .../trousse/authz_pqc_audit/ciba_approval.py` (`L58–118`), `Corpus/Tome 2` (`EXIG-INT-22` `L2706`, `EXIG-AUT-12/15`, `EXIG-CON-29` `L6149–6155`), `Corpus/Tome 5`.
  - **Passe initiale :** écart rectifié · **Action :** dissocié les fonctions des deux modules Python de la trousse d'avec `EXIG-INT-22`, `EXIG-AUT-12/15`, `EXIG-CON-29` (`30` s) et la fenêtre synchrone `PEP` (`post-G4`), et explicité au lissage G5 la complémentarité `EXIG-INT-22` (`P3`) / `EXIG-CON-29` (`RTR`, `≥ 30 s`) · **Verdict : supporté**

- **C28-22 (`L98–L100`, `Figure 89`)** — *Affirmation :* La Figure 89 (`SCH-28-02.svg`) sépare la zone probabiliste (`Z1`), le tampon déterministe `EXIG-CON-29` (`Z2`) et le sas `P3` sur `JCS` avec rétention `≥ 30` s avant l'émission `pacs.008` (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`SCH-28-02`), `schemas/SCH-28-02.puml`, `schemas/rendus/SCH-28-02.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C28-23 (`L104–L108`)** — *Affirmation :* Hygiène des métriques auto-déclarées (non vérifiées indépendamment, non sommables si unités distinctes), classement d'accès `5 + 4 + 1` issu du `Tome 1 ch35` (avec mention en `L+` de `Banque Nationale` notée `69 / 100` par `AIBanks.ca` `[5]`), maintien en statut bloqué `HTTP 403` de `lautorite.qc.ca`, `ciro.ca` et `securities-administrators.ca`, et appuis `L+` `[1]`–`[7]`.
  - **Appui vérifié :** `Corpus/Tome 1` (`L8256`, `L8445`), `SRC-071.txt` (`[5]`, `National Bank 69`), `sources/ch28-sources.md` (`L101–103`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché la grille `5+4+1` au recensement `Tome 1 ch35` hors `L+`, intégré la notation `AIBanks.ca` `[5]` et scindé le paragraphe (`CA-05`) · **Verdict : supporté**

- **C28-24 (`L110–L123`, `Tableau 28.3`)** — *Affirmation :* Le `Tableau 28.3` rapporte les faits publics datés `2025–2026` et réserves de dix institutions (`TD`, `Scotiabank`, `RBC`, `Manuvie`, `Desjardins`, `CIBC`, `Intact`, `BMO`, `Sun Life` sans lien `ACP`, `Banque Nationale`) selon le repérage `Tome 1 § 35` et `[5]`.
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 35.1`–`§ 35.8`, `L8258–8450`), `SRC-071.txt` (`[5]`).
  - **Passe initiale :** écart rectifié · **Action :** supprimé le renvoi erroné `[7]` (`LSAC`) de la ligne `Desjardins`, attribué la source au `Tome 1 § 35` et ajouté l'indice `AIBanks.ca` `[5]` sur `Banque Nationale` · **Verdict : supporté**

- **C28-25 (`L125`)** — *Affirmation :* Deux enseignements (« le mot ne mesure pas la chose » chez `CIBC` et `Intact` ; cinq invariants de façade `Tome 1 § 35.9` sans preuve publique de chaîne de mandat cryptographique ni de positionnement `OO1`–`OO4`), justifiant la préparation au `1er mai 2027` (`BSIF E-23` `[2, 5]`, `AMF` sous réserve `[5]`).
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 35.9`), `SRC-065.txt` (`[2]`), `SRC-071.txt` (`[5]`).
  - **Passe initiale :** écart rectifié · **Action :** attribué explicitement les cinq invariants au `Tome 1 § 35.9` · **Verdict : supporté**

### Section 28.3 — Frontière probante et transition (`L127–L142`, Figure 90)

- **C28-26 (`L129–L134`)** — *Affirmation :* Frontière méthodologique stricte séparant le périmètre démontré (`BCA`, `CRE-IA-2026-01 v1.2`, `AMF IA`, trousse Tome 8 vérifiée en `G0` via `83/83` tests `pytest` et `45/45` tests `OPA` à `100,0 %`, plus campagnes synthétiques `FEDS` documentées aux `Tome 4`/`Tome 5`, `Borealis-Bench` absent du disque au `Tome 8`) des extrapolations illustratives (`HL7 FHIR R4`, usine `BEL` Trois-Rivières `IEC 62443`, `NERC CIP`, `IEC 61511 SIL 2/3`) soumises à revue clinique intégrale ou sas `OPC UA` / `MQTT Sparkplug` en lecture seule.
  - **Appui vérifié :** `aq/rapports-g0.json` (`L11–49` : `83` pytest, `45` OPA à `100,0 %`), `Corpus/Tome 8` (`L1804`), `Corpus/Tome 3` (`BEL` Trois-Rivières, `SIL 2/3`), `Corpus/Tome 4` (`W4.2`).
  - **Passe initiale :** écart rectifié · **Action :** retiré l'allégation d'exécution locale de `Borealis-Bench` et inscrit les métriques exactes vérifiées en `G0` sur la trousse du Tome 8 · **Verdict : supporté**

- **C28-27 (`L136–L138`, `Figure 90`)** — *Affirmation :* La Figure 90 (`SCH-28-03.svg`) matérialise la démarcation entre terrain canadien (`Z1`), sas de non-importation (`Z2`) et extrapolations `HL7 FHIR R4` / `IT/OT SIL 2/3` en lecture seule (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`SCH-28-03`), `schemas/SCH-28-03.svg`, `schemas/rendus/SCH-28-03.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C28-28 (`L140`)** — *Affirmation :* Convergence des échéances du `1er mai 2027` (`BSIF E-23` `[2]` et `AMF` attendu sous réserve via source secondaire `AIBanks.ca`, portail en statut `F` `[5]`) et du `1er octobre 2028` (`NC 31-103` `[6]`), et valeur de l'alignement des `24 PEX` sur `CRE-IA-2026-01 v1.2`.
  - **Appui vérifié :** `SRC-065.txt` (`[2]`), `SRC-071.txt` (`[5]`), `SRC-111.txt` (`[6]`), `registre/ancres-chronologiques.json`.
  - **Passe initiale :** conforme · **Action :** révision `REV-04` : ajout de la nuance explicite de source secondaire `AIBanks.ca` (`statut F` AMF) sur les renvois `[5]` (`REF-003`), retrait des échappements `\$` dans les backticks (`PRD-L4-010`) et ajout des renvois `SIG-103`, `SIG-104`, `SIG-105`, `DISC-01`, `DISC-05` au `Tableau 28.1` (`PRD-L4-025`) · **Verdict : supporté**

- **C28-29 (`L142`)** — *Affirmation :* Ouverture vers le Chapitre 29 (assemblage en trois blueprints `C01–C40`, fédération multi-SaaS, continuité cognitive et séparation entre le fil rouge du Groupe Boréal et les preuves exécutables de la trousse logicielle).
  - **Appui vérifié :** `specs/manifest.json` (`ch29`), `Corpus/Tome 8` (`L1804`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé la mention finale de `Borealis-Bench` par celle de la trousse logicielle exécutable · **Verdict : supporté**
