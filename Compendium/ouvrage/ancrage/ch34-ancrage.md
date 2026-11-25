# Journal d'ancrage atomique Wyvern G2 — Chapitre 34 (`ch34`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/12 - Partie XII/Chapitre 34.md` (`4 223` mots de prose selon `verifie_manuscrit`, `4 480` selon `parser_plan`, plage `[3 901, 4 579]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch34-sources.md` (`[1]`–`[9]` en statut `L+`, `3` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`) et spécifications `Compendium/prd.md` (`EXIG-HOM-01..06`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b5-5`
- **Passe G2 initiale (supportés)** : 14
- **Rectifications appliquées lors de la passe G2 :** 14
- **Verdict final — supportés :** 28 / 28 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 34.md`

Toutes les formulations divergentes ou insuffisamment délimitées relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 34.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/12%20-%20Partie%20XII/Chapitre%2034.md), sans altérer le bloc scellé `G0-EX-CH04-03`, les invariants `CA-01`–`CA-22`, les `owned_concepts` (`exigences-cre-ia-305`, `dix-interdictions-exig-gov-17`, `portee-et-force-normative-cre-ia`, `homologation-prr-75-points`, `referentiel-annexes-protocoles-chronologie`, `grille-homologation-et-fiche-agent`), l'ensemble des renvois `[1]`–`[9]` ni le calibrage (`4 223` / `4 480` mots dans `[3 901, 4 579]`) :

1. **Portée exacte des renvois `[1]`–`[9]` et attribution de la Loi 25 (`L7`, `L15`, `L19`, `L22`, `L64`, `L70`, `L156`, `L178`) :** retrait du renvoi `[8]` (`AIBanks.ca` `SRC-071.txt`, qui ne traite pas de la Loi 25) sur l'article `12.1` de `LQ 2021, c. 25` (`RLRQ, c. P-39.1`), réancré sur le registre `L+` du traité (`SRC-063` dans `ancres-chronologiques.json` et `← Chapitre 25`) avec scission en deux phrases conformes à `CA-05` ; retrait des renvois `[6, 7]` hors sujet sur `OPA/Rego` et `journal signé` à `L15` (rattachés à `G0` et `[1]`) ; distinction claire de la portée propre de `[1]` (`JSON Schema Draft 2020-12`), `[2]` (`OWASP ASI01–ASI10`), `[9]` (`RFC 2119`) et de la fenêtre `PQC` `2030–2035` (`← Chapitre 18`).
2. **Rectification de fond sur `EXIG-CON-28`, `Annexe A/B` et le corpus `Tome 3` (`L28`, `L74`, `L82`, `L88`, `L90`–`L92`) :** correction de l'objet erroné attribué à `EXIG-CON-28` (« secteur des assurances » remplacé par la véracité des déclarations et l'interdiction de l'« AI washing » sous `ACVM 11-348` selon `Tome 2 § 12.10`) ; qualification de la Note `AMF IA` (`CRE-IA-2026-01-QC`, `31 octobre 2026`) face au `statut F` de `lautorite.qc.ca` `[8]` ; distinction entre `EXIG-GOV-07` (`Annexe B`, fiche d'agent) et `EXIG-GOV-11` (`Annexe A`, grille d'homologation), et entre les `57` points bruts de `Tome 2 Annexe A` et leur regroupement en `41` rubriques avec `POR` dans `Tome 5 Annexe C.1` ; qualification du glossaire du `Tome 3 Annexe A` comme glossaire d'usage non normatif (le glossaire normatif siégeant en `Tome 2 Annexe E`), et précision que seuls `agentproto` et `dawn` ont été créés en octobre 2026 (contrairement aux livrables et révisions `OAuth 2.1` et `WIMSE`).
3. **Rectification factuelle du `Tableau 34.2` (`PRR-75` bloquants) et du schéma `Adr2027B001` (`L104`, `L108`, `L156`) :** correction de `S-15` (remplacement d'« approbation `P3` » — qui relève de `S-10` conditionnel — par « séparation des tâches `SoD` » conforme à `matrice-exig-prr-c40.json` et `Tome 3 Annexe G`), de `F-14` (remplacement d'« couverture et tests `C01–C40` / `SBB` » par « confinement du SRE autonome sous `Cedar`/`OPA` »), et de `F-04` (résidence juridictionnelle des couches d'état) ; distinction entre le champ `minimum_eval_gate` du schéma `Adr2027B001` et la convention `pass^5`.

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C34-01` à `C34-28`)

### Section 34.0 & 34.1 — Titre, ouverture et résumé exécutif (`L1–L22`)

- **C34-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice unifiant `305` exigences `CRE-IA-2026-01`, `10` interdictions `EXIG-GOV-17` et la grille `PRR-75`.
  - **Appui vérifié :** `specs/manifest.json` (`ch34`, `D12`, `SUB_D12_01`), `registre/matrice-exig-prr-c40.json` (`exig_cre_ia_v1_2`, `prr_75`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-02 (`L5`)** — *Affirmation :* Ouverture de la Partie XII (`D12`) soudant norme prescrite, preuve logicielle hors ligne et traçabilité éditoriale pour tout composant doté d'une capacité d'action (interne, acquis sur étagère ou tiers).
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 1.2`, `L426`), `Compendium/prd.md` (`EXIG-HOM-01`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-03 (`L7`)** — *Affirmation :* Au gel du `2 décembre 2026`, `CRE-IA-2026-01 v1.2` consolide dans `exigences.json` `305` exigences vérifiables (suivant `RFC 2119` `[9]`), `10` interdictions `EXIG-GOV-17`, `PRR-75` (`24` bloquants sur `75`) et `ADR 2027-B001` validé `JSON Schema Draft 2020-12` `[1]` avec couverture `OWASP ASI01–ASI10` `[2]`, sous clause consultative `non-avis` `[3, 4, 5, 8]`.
  - **Appui vérifié :** `SRC-021.txt` (`[1]`), `SRC-055.txt` (`[2]`), `SRC-125.txt` (`[9]`), `SRC-060/061/065/071.txt` (`[3, 4, 5, 8]`), `registre/matrice-exig-prr-c40.json` (`L4`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié les artefacts internes du traité des renvois externes `[1, 2, 9]` · **Verdict : supporté**

- **C34-04 (`L11`)** — *Affirmation :* Pilier 1 — `CRE-IA-2026-01 v1.2` arrêté le `19 novembre 2026` (`DC-P08`), fédérant `305` exigences sous `16` préfixes (`EXIG-ARC` à `EXIG-APP`), avec verbes `RFC 2119` (`DOIT`, `NE DOIT PAS`, `DEVRAIT`) `[9]` et règle du doute.
  - **Appui vérifié :** `SRC-125.txt` (`[9]`, `L30–L40`), `Corpus/Tome 2` (`L44`, `L426`, `L458–L493`), `registre/matrice-exig-prr-c40.json` (`familles`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-05 (`L13`)** — *Affirmation :* Pilier 2 — dix interdictions absolues (`EXIG-GOV-17`) réconciliées avec les `46 ND` (zéro dérogation : `NX`, `P3` sans `CIBA` lié, usurpation, relais de jeton, Règle de deux, absence de fiche ou de journal chaîné, violation des lois `[2, 3, 5]`).
  - **Appui vérifié :** `Corpus/Tome 5` (`L182`, `Annexe C.2`, `L1926`), `registre/matrice-exig-prr-c40.json` (`dix_interdictions_sans_derogation_gov_17`), `SRC-055/060/065.txt` (`[2, 3, 5]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-06 (`L15`)** — *Affirmation :* Pilier 3 — `PRR-75` pour `L2`–`L4` en `5` domaines de `15` points (`S/R/O/G/F`) avec `24` Portes PRR bloquantes appuyées sur artefacts automatisés (`journal signé`, `OPA/Rego` vérifié en `G0`, `JSON Schema Draft 2020-12` `[1]`), fiche d'agent (`Annexe B`, `Tableau 63`) et `ADR 2027-B001`.
  - **Appui vérifié :** `SRC-021.txt` (`[1]`), `aq/rapports-g0.json` (`opa_check`), `Corpus/Tome 3` (`Annexe G`), `Corpus/Tome 2` (`Tableau 63`).
  - **Passe initiale :** écart rectifié · **Action :** supprimé `[6, 7]` hors sujet et rattaché `OPA/Rego` à `G0` · **Verdict : supporté**

- **C34-07 (`L17–L19`)** — *Affirmation :* Pilier 4 (volet Québec Loi 25) — article `12.1` inséré par `LQ 2021, c. 25` dans la *Loi sur le secteur privé* (`RLRQ, c. P-39.1`, en vigueur le `22 septembre 2023`, ancré `L+` `SRC-063` et `← Chapitre 25`), avis, facteurs, observations, révision humaine, sanctions jusqu'à `10 M\$ CA` (`2 %`) et `25 M\$ CA` (`4 %`).
  - **Appui vérifié :** `registre/ancres-chronologiques.json` (`2026-LOI25-ART12-1`, `SRC-063`), `Chapitre 25.md`.
  - **Passe initiale :** écart rectifié · **Action :** supprimé le renvoi erroné `[8]` (`AIBanks.ca`), précisé `RLRQ, c. P-39.1` et scindé en deux phrases conformes à `CA-05` · **Verdict : supporté**

- **C34-08 (`L20–L21`)** — *Affirmation :* Pilier 4 (volets BSIF et AMF) — `BSIF E-23` révisée le `11 septembre 2025` avec entrée en vigueur le `1er mai 2027` `[5]`, et repère attendu du `1er mai 2027` pour la ligne directrice IA de l'AMF rapporté sous réserve via `AIBanks.ca` `[8]` (portail direct en `statut F`).
  - **Appui vérifié :** `SRC-065.txt` (`[5]`, `L15`, `L31`), `SRC-071.txt` (`[8]`, `L271–L275`), `sources/ch34-sources.md` (`L112`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-09 (`L22`)** — *Affirmation :* Pilier 4 (volets UE et PQC) — `EU AI Act` art. `50` applicable dès le `2 août 2026` `[3]`, `(UE) 2026/1744` fixant au plus tard au `2 décembre 2027` l'Annexe III et au `2 août 2028` l'Annexe I `[4]`, art. `17` soutenu par `EN 18286:2026` via `(UE) 2026/2274` `[6, 7]`, et fenêtre `PQC` `2030–2035` (`G7`/NIST) issue du registre (`← Chapitre 18`).
  - **Appui vérifié :** `SRC-060.txt` (`[3]`, `Art. 50`, `Art. 113`), `SRC-061.txt` (`[4]`), `SRC-067.txt` (`[6]`), `SRC-069.txt` (`[7]`), `ancres-chronologiques.json` (`2030-2035-G7-PQC-FINANCE`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement la fenêtre `2030–2035` au calendrier du registre (`← Chapitre 18`) · **Verdict : supporté**

### Section 34.2.1 — Socle `CRE-IA-2026-01 v1.2`, dix interdictions `GOV-17` et principes (`L24–L78`, Tableau 34.1, Figure 1)

- **C34-10 (`L28`)** — *Affirmation :* Passage de `287` (`v1.1`) à `305` exigences (`v1.2`, `DC-P08`, `19 novembre 2026`) : `+12` `EXIG-AMF-01..12` (transposant `41` attentes de la Note interne `AMF IA` `CRE-IA-2026-01-QC` du `31 octobre 2026`, portail `statut F` `[8]`), `+2` `PQC` (`EXIG-SEC-27..28`), `ACVM 11-348` convenance (`EXIG-CON-27`) et véracité/anti-« AI washing » (`EXIG-CON-28`), `RTR` (`EXIG-CON-29`) et `EN 18286:2026` (`EXIG-CON-30` `[6, 7]`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L44`, `§ 12.10`, `L6133–L6263`, `L8751`), `SRC-067/069.txt` (`[6, 7]`), `SRC-071.txt` (`[8]`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé l'objet d'`EXIG-CON-28` en véracité et anti-« AI washing » `ACVM 11-348` (au lieu de « secteur des assurances ») et qualifié la Note interne `AMF IA` avec `[8]` · **Verdict : supporté**

- **C34-11 (`L30–L51`, Tableau 34.1)** — *Affirmation :* Ventilation quantitative des `305` exigences (`255 DOIT`, `34 NE DOIT PAS`, `16 DEVRAIT` `[9]`) sous `16` préfixes (`25+23+22+15+10+30+23+21+28+13+6+10+20+30+12+17 = 305`) et croisement avec `75 PRR`, `15 POR`, `31 ADR` et `41` rubriques.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`repartition_force`, `familles_comptes`, `grille_unifiee_t5_annexe_c1`), `SRC-125.txt` (`[9]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-12 (`L53–L63`)** — *Affirmation :* Noyau non dérogeable `EXIG-GOV-17` (interdictions `1` à `9` alignées sur `46 ND` : `EXIG-AUT-03`, `09`, `12`, `13`, `EXIG-IAM-08`, `09`, `12`, `EXIG-MCP-11`, `EXIG-GOV-01..15`, `EXIG-AUT-01`, `02`, `EXIG-CON-02`, `EXIG-AUT-07`, `EXIG-SEC-06`, `EXIG-OBS-11`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`dix_interdictions_sans_derogation_gov_17`), `Corpus/Tome 5` (`Annexe C.2`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-13 (`L64`)** — *Affirmation :* Interdiction `10` d'`EXIG-GOV-17` — conformité impérative aux lois applicables (`EXIG-AUT-22..23`, `EXIG-CON-04..22`), dont Loi 25 art. `12.1` (`← Chapitre 25`), ÉFVP, livres bancaires et `EU AI Act` `[3]`.
  - **Appui vérifié :** `Corpus/Tome 5` (`L1987`), `SRC-060.txt` (`[3]`), `Chapitre 25.md`.
  - **Passe initiale :** écart rectifié · **Action :** retiré le renvoi `[8]` sur Loi 25 et le tiret conditionnel `U+00AD` dans `impérativement` · **Verdict : supporté**

- **C34-14 (`L66–L68`)** — *Affirmation :* Principes d'interprétation (`CRE-IA-2026-01 § 1`) : portée fonctionnelle et règle du doute, force `RFC 2119` `[9]` (`DOIT`/`NE DOIT PAS` bloquants vs `DEVRAIT` sur équivalence signée) et indicatif présent des blocs logiciels.
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 1.2`, `§ 1.4`, `L426–L480`), `SRC-125.txt` (`[9]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-15 (`L70–L72`)** — *Affirmation :* Séparation entre obligations légales externes (Loi 25 `← Chapitre 25`, BSIF `[5]`, repère AMF sous réserve `[8]`, règlements UE `[3, 4]`, `EN 18286:2026` `[6, 7]` publiée le `12 octobre 2026` et explicitée le `21 octobre 2026` pour l'art. `17`, échéance Annexe III `2 décembre 2027` `[4]`) et seuils d'ingénierie internes (`pass^5`, rétention).
  - **Appui vérifié :** `Corpus/Tome 2` (`L483`), `SRC-060/061/065/067/069/071.txt` (`[3, 4, 5, 6, 7, 8]`).
  - **Passe initiale :** écart rectifié · **Action :** retiré `[8]` de Loi 25 et rattaché `[8]` au repère AMF sous réserve · **Verdict : supporté**

- **C34-16 (`L74–L78`, Figure 1)** — *Affirmation :* Parcours de lecture par rôle au `Tableau 2` du Tome 2 (direction TI, architectes, plateforme, sécurité, risques/conformité/RP, responsables métier, approvisionnement, audit interne) complété par le découpage `AE`/`AS`/`RSSI`/`SRE`, et `Figure 1` (`SCH-34-01.svg`).
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 2`, `L432–L446`), `schemas/SCH-34-01.puml`, `schemas/rendus/SCH-34-01.svg`.
  - **Passe initiale :** écart rectifié · **Action :** aligné la liste des rôles sur `Tableau 2` de Tome 2 tout en conservant la synthèse `AE`/`AS`/`RSSI`/`SRE` · **Verdict : supporté**

### Section 34.2.2 — Grille `PRR-75`, `24` portes bloquantes, fiche d'agent et `ADR 2027-B001` (`L80–L156`, Tableau 34.2, Figures 2–3, `G0-EX-CH04-03`)

- **C34-17 (`L82–L86`)** — *Affirmation :* Fiche d'agent (`Annexe B`, `Tableau 63`) dont le contenu est exigé par `EXIG-GOV-07` (en complément de la grille `EXIG-GOV-11`), suivie aux trois jalons `Proposition`, `Conception` et `Pilote`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L473`, `Annexe B`, `L6895–L6938`, `Tableau 63`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié `EXIG-GOV-07` (fiche d'agent) d'`EXIG-GOV-11` (grille d'homologation) · **Verdict : supporté**

- **C34-18 (`L88`)** — *Affirmation :* Grille d'applicabilité et d'homologation (`Tome 2 Annexe A`, `A.1` à `A.8`, `57` points dont `28` universels et `29` conditionnels incluant `11` règles non dérogeables, consolidés en `41` rubriques `A.2.1` à `A.8.7` dans `Tome 5 Annexe C.1`), projection déterministe de `A.1` (`EXIG-GOV-16`) filtrant les `305` exigences `EXIG-*`, marquage `EXIG-GOV-17` et liaison `POR` (maintenant `L0–L1` hors périmètre `PRR-75`).
  - **Appui vérifié :** `Corpus/Tome 2` (`Annexe A`, `L6788–6892`), `Corpus/Tome 5` (`Annexe C.1`, `L1920–1973`), `registre/matrice-exig-prr-c40.json`.
  - **Passe initiale :** écart rectifié · **Action :** intégrée la ventilation `28`/`29`/`11` et `A.2.1`–`A.8.7` (`post-G4`) · **Verdict : supporté**

- **C34-19 (`L90–L96`, Figure 2)** — *Affirmation :* Corpus synoptique du Tome 3 (`Annexes A, B, C, D, H`) : glossaire bilingue d'usage en `8` rubriques `A.1`–`A.8` (glossaire normatif au `Tome 2 Annexe E`), `7` fiches protocoles (`MCP`, `A2A`, `AG-UI`, `ANP`, `AGNTCY`, `AP2`, `x402`), `3` grilles probatoires, chronologie `2024–2028` (création en octobre 2026 de `agentproto` et `dawn`, livrables/révisions `OAuth 2.1` et `WIMSE` d'octobre–novembre 2026), index de `27` fondations/standards, et `Figure 2` (`SCH-34-02.png`).
  - **Appui vérifié :** `Corpus/Tome 3` (`Annexes A–D, H`, `L27612–L28594`), `schemas/SCH-34-02.mmd`, `schemas/rendus/SCH-34-02.png`, `SRC-125.txt` (`[9]`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié le glossaire du Tome 3 de glossaire d'usage et distingué la création d'`agentproto`/`dawn` en octobre 2026 des révisions `OAuth 2.1`/`WIMSE` · **Verdict : supporté**

- **C34-20 (`L98–L100`)** — *Affirmation :* Grille pré-production `PRR-75` (`Tome 3 Annexe G`, `Tome 8 Annexe B`) : `75` points en `5 × 15` (`S/R/O/G/F`), quatre niveaux de force probatoire (`normative`, `mesurée`, `éditeur`, `synthèse`), répartition `24` bloquants conditionnant l'ouverture en production aux niveaux actifs (`L2–L4`), `26` conditionnels (`S:4, R:4, O:3, G:4, F:11` activés selon périmètre technique, palier `L3–L4` `O-05`/`F-07` ou assujettissement `[3, 5]`) et `25` élevée/moyenne.
  - **Appui vérifié :** `Corpus/Tome 3` (`Annexe G`, `L28452–28559`), `registre/matrice-exig-prr-c40.json` (`prr_75`), `SRC-060.txt` `[3]`, `SRC-065.txt` `[5]`.
  - **Passe initiale :** conforme · **Action :** ajoutée la ventilation exacte des `26` conditionnels (`S:4, R:4, O:3, G:4, F:11`) (`post-G4`), et harmonisé `L2–L4` sur les `24` portes bloquantes (lissage G5) · **Verdict : supporté**

- **C34-21 (`L102–L110`, Tableau 34.2)** — *Affirmation :* Tableau `34.2` détaillant les `24` portes bloquantes par domaine (`S:8`, `R:5`, `O:2`, `G:7`, `F:2`) avec leurs identifiants et objets exacts (`S-15` séparation des tâches `SoD`, `F-04` résidence juridictionnelle des couches d'état, `F-14` confinement du SRE autonome sous `Cedar`/`OPA`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`prr_75.items`), `Corpus/Tome 3` (`Annexe G`), `Corpus/Tome 8` (`L1446`, `L3020–L3036`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé `S-15` (séparation des tâches `SoD`), `F-04` (résidence juridictionnelle des couches d'état) et `F-14` (confinement du SRE autonome sous `Cedar`/`OPA`) · **Verdict : supporté**

- **C34-22 (`L112–L116`, Figure 3)** — *Affirmation :* Gabarit `ADR 2027-B001` validé par `schemas/adr_2027_b001.schema.json` (`JSON Schema Draft 2020-12` `[1]`), traversée des `24` verrous dans `evalops_prr`, présence des `5 SBB` et des niveaux probatoires, validation `C01–C40` à `exit 0`, illustrés à la `Figure 3` (`SCH-34-03.png`).
  - **Appui vérifié :** `SRC-021.txt` (`[1]`), `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/evalops_prr/prr_validators.py`, `schemas/SCH-34-03.mmd`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-23 (`L118–L154`)** — *Affirmation :* Extrait normatif `G0-EX-CH04-03` synchronisé octet pour octet avec `adr_2027_b001.schema.json` (`lines="1-32"`, `sha256="4f0a41e7280851ce1413efeb6accb3632bb3ee6a0bfefc4fa7d92338156e36ae"`).
  - **Appui vérifié :** `aq/rapports-g0.json` (`L169–L175`), `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/schemas/adr_2027_b001.schema.json`, `verifie_manuscrit.py` (`CA-20`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-24 (`L156`)** — *Affirmation :* Cinq garde-fous de `Adr2027B001` (`additionalProperties: false` `[1]`, `owners` sous `EXIG-GOV-01`, `risk_and_autonomy` `L0`–`L4` / `OWASP ASI01–ASI10` `[2]` / `bsif_e23_materiality` `[5]` / `quebec_law25_automated_decision` `← Chapitre 25` / `eu_ai_act_tier` `[3, 4]`, `technical_invariants` dont `max_cost_per_outcome_cad > 0` et `minimum_eval_gate` tel `pass^5`, `fallback_and_killswitch` et `review_trigger`).
  - **Appui vérifié :** `adr_2027_b001.schema.json`, `SRC-021/055/060/061/065.txt` (`[1, 2, 3, 4, 5]`), `Compendium/prd.md` (`EXIG-HOM-04`).
  - **Passe initiale :** écart rectifié · **Action :** retiré `[8]` sur `quebec_law25_automated_decision` et distingué le nom de champ `minimum_eval_gate` de la convention `pass^5` · **Verdict : supporté**

### Section 34.3 — Synthèse transversale, livrables et invariants (`L158–L178`, Tableau 34.3)

- **C34-25 (`L160`)** — *Affirmation :* Convergence amont (`PRIN-01..12` et `31 ADR` `← ch06`, `OWASP ASI01–10` `← ch19` `[2]`, coupe-circuit `< 10 s` / `≤ 15 min` et purge `≤ 14 j` vs `14–30 j` `← ch21, ch22`, cadres QC/CA/UE `← ch25, ch26` `[3..8]`, trousse `← ch35`) et projections aval (`→ ch20, ch23, ch32, ch36`).
  - **Appui vérifié :** `Chapitre 21.md`, `Chapitre 22.md` (`L74`), `Chapitre 25.md`, `Chapitre 26.md`, `Chapitre 35.md`, `SRC-055/060/061/065/067/069/071.txt` (`[2..8]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-26 (`L162`)** — *Affirmation :* Règle `AO-01` (`L+` haché `SHA-256` vs `statut F` hors preuve : `lautorite.qc.ca` `HTTP 403` sous réserve via `AIBanks.ca` `[8]`, `iso.org` `ISO/IEC 42001` `HTTP 403`, `CEN/CENELEC` `HTTP 500` compensé par `[6, 7]`).
  - **Appui vérifié :** `sources/ch34-sources.md` (`L110–L114`), `recherche/registre-statut-f.json`, `SRC-067/069/071.txt` (`[6, 7, 8]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C34-27 (`L164–L172`, Tableau 34.3)** — *Affirmation :* Tableau `34.3` des cinq livrables opposables (`exigences.json v1.2` sous `EXIG-HOM-01/02` `[9]`, fiche `Tableau 63` + grille `A.1–A.8`, `PRR-75`, `ADR 2027-B001` `[1, 2]`, appareil synoptique `7` protocoles / `27` standards et mention `non-avis` `[3, 5, 8]`).
  - **Appui vérifié :** `Compendium/prd.md` (`EXIG-HOM-01..06`), `registre/matrice-exig-prr-c40.json`, `SRC-021/055/060/065/071/125.txt` (`[1, 2, 3, 5, 8, 9]`).
  - **Passe initiale :** conforme · **Action :** ajouté `EXIG-HOM-02` (`post-G4`) · **Verdict : supporté**

- **C34-28 (`L170–L174`)** — *Affirmation :* Trois invariants exécutables du Chapitre 34 : (1) soumission universelle à `exigences.json v1.2` (`305` règles) et zéro tolérance `EXIG-GOV-17` (`46 ND`) ; (2) verrouillage `PRR-75` (`100 %` des `24` contrôles `[BLOQUANT]` `S:8/R:5/O:2/G:7/F:2`) ; (3) contrat mécanique `ADR 2027-B001` (`adr_2027_b001.schema.json` `[1]`, `ASI01–ASI10` `[2]`, `Loi 25` `← Chapitre 25`, `BSIF E-23` `[5]`, `AMF` sous réserve via source secondaire `AIBanks.ca` `[8]`, `EU AI Act` `[3, 4]`) sans valeur d'avis juridique.
  - **Appui vérifié :** `SRC-021/055/060/061/065/071.txt` (`[1, 2, 3, 4, 5, 8]`), `registre/matrice-exig-prr-c40.json` (`POR-003`, `CAP-046`, `EXIG-AMF-11`, `EXIG-EVA-03`, `EXIG-MCP-03`, `EXIG-OBS-06`, `EXIG-ORC-18`), `adr_2027_b001.schema.json`.
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement `[1, 2, 3, 4, 5, 8]` et `← Chapitre 25` au 3e invariant ; révision `REV-04` : renumérotation continue `Figure 106` à `Figure 108` (`PRD-L4-012`), retrait de `\$` dans les backticks (`PRD-L4-010`), harmonisation `H2` (`34.1`/`34.2`/`34.3`, `PRD-L4-022`), intégration explicite de `POR-003`, `DC-P11`, `CAP-046` et des `5` `EXIG-*` clés (`PRD-L4-019`) et nuance explicite de source secondaire `AIBanks.ca` sur `[8]` (`REF-003`), en préservant intégralement le bloc `G0-EX-CH04-03` · **Verdict : supporté**
