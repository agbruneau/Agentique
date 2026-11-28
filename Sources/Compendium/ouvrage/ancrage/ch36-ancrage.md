# Journal d'ancrage atomique Wyvern G2 — Chapitre 36 (`ch36`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/12 - Partie XII/Chapitre 36.md` (`6 065` mots `verifie_manuscrit` / `6 351` mots `parser_plan`, plage `[5 300, 6 220]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch36-sources.md` (`[1]`–`[12]` en statut `L+`, `4` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` (`concordance-taxonomies.json`, `matrice-exig-prr-c40.json`, `ancres-chronologiques.json`, `faits-empiriques.json`, `glossaire-termes.json`, `specifications-lplus.json`) ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) ; spécifications `Compendium/prd.md` ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`) et usine `gabarit-pdf/`
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b5-7`
- **Passe G2 initiale (supportés) :** 27
- **Rectifications appliquées lors de la passe G2 :** 14
- **Verdict final — supportés :** 41 / 41 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 36.md`

Toutes les formulations divergentes ou insuffisamment qualifiées relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 36.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/12%20-%20Partie%20XII/Chapitre%2036.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant la notice opposable `non-avis`, les marqueurs taxonomiques autorisés (`[A]`/`[B]`/`[C]`/`[N]`/`[M]`/`[É]`/`[S]`/`[D]`/`[L+]`), les `14` `owned_concepts` (`concordance-inter-tomes-div02`..`registre-sources-tracees-annexe-b`), l'ensemble des renvois `[1]`–`[12]` et le calibrage (`6 065` mots `verifie_manuscrit` / `6 351` mots `parser_plan` dans `[5 300, 6 220]`) :

1. **Clause `non-avis`, portée des catégories `A`/`B` et sigle `EFVP` (`L5`, `L9`, `L15`, `L75`, `L87`) :** explicitation complète « avis juridique, médical, financier ou réglementaire » dans l'encadré `non-avis`, correction de « système d'exploitation réel (`SoR`) » en « système en exploitation réelle ou sur ses systèmes d'enregistrement (`SoR`) », précision que la catégorie `A` est requise au Tome 2 pour fonder une exigence (contrairement à `B`), alignement du renvoi aux `121` références et `449` sources de l'Annexe G du Tome 2, et notation exacte `EFVP` (`ÉFVP`) conforme au `Tableau 65`.
2. **Pont `DIV-02`, cinq lacunes `CAP` et numérotation `PEX` (`L27`, `L37`) :** rectification de quatre des cinq libellés des capacités sans exigence `CAD26` directe d'après `concordance-taxonomies.json` et `matrice-exig-prr-c40.json` (`CAP-025` sas dérogatoire et extinction `CUA`, `CAP-028` sas `OT` et continuité déconnectée `72` h, `CAP-033` inférence en enclave attestée, `CAP-046` comptabilisation énergétique et carbone `B-15`, `CAP-052` ingénierie assistée ségrégée) ; séparation entre la ventilation `13` / `11` du Tome 5 avant `v1.2` et les `7` entrées restant au statut `Lacune 2026` dans `matrice-exig-prr-c40.json` ; précision de la numérotation non contiguë `PEX-001`–`044` et remplacement de `Tableau A.1` par `section A.1` du Tome 5.
3. **Discordance `DISC-05` et fenêtres `SEP-2596` / `SEP-3398` (`Tableau 36.1`, `L67`) :** dissociation entre le verrouillage de `StreamableHttpAdapter` sur `Mcp-Method`/`Mcp-Name` (`SRC-074.txt` `[3]`) et l'isolation par `McpTransportAdapter` de l'échéance `SEP-3398` (`30 mars 2027` `[5]`) et de la fenêtre `SEP-2596` (`12` mois pour toute nouvelle dépréciation jusqu'au `28 juillet 2027`, contre `3` mois de grâce transitoire pour `HTTP+SSE` déjà déprécié, archivé au commit du `22 novembre 2026` `[4]`).
4. **Audit Tome 2 (`302/427`, `448` → `449`), lot `W3.2` et Annexe H (`L89`, `L102`–`L104`, `L125`) :** remplacement de `71 %` par le décompte exact `302` sur `427` (`70,7 %`), dissociation chronologique entre les `448` sources distinctes du `19 novembre 2026` (après fusion de `25` doublons sur `473` entrées) et l'ajout de `[474]` (`RFC 7515`) portant l'Annexe G à `449` sources en `v1.1` avant `[475]`–`[498]` ; précision des `5` API productives sur `9` et des `1 101` occurrences d'URLs du lot `W3.2` ; distinction dans l'Annexe H entre le relevé du `1er novembre 2026` (`22/24` directes, `2/24` partielles) et le contrôle déterministe `24/24` plus protocole stratifié `n ≥ 8/24` instauré le `19 novembre` pour les réouvertures ultérieures.
5. **Usine `gabarit-pdf/`, `compile_schemas_compendium.py`, figures `base64` et `Tableau 36.3` (`L145`–`L147`, `L165`–`L169`) :** séparation entre `compile_diagrams.py` (`319` diagrammes des `8` tomes : `253` `.svg` et `66` `.png` au facteur `3`) et `compile_schemas_compendium.py` (`139` schémas du traité : `58` `PlantUML` `.svg` sous `-failfast2`, `23` `Mermaid` `.png` et `58` `SVG`) ; ventilation exacte des figures encodées en `base64` dans les éditions `HTML` autonomes (`23` pour le Tome 7, `9` pour le Tome 8, `139` pour `Compendium.html`) ; rattachement d'`EXIG-CONC-01..06` au plan directeur du traité et scission conforme à `CA-05`.
6. **Adaptation éditoriale au titre directeur *Interopérabilité et automatisation agentique des systèmes d'entreprise* (`L1`, `L3`, `L5`, `L43`–`L47`, `L149`, `Tableau 36.3`) :** synchronisation exacte de `L1` sur `specs/manifest.json` (`ch36`), consignation explicite sous `AO-02` en `§ 36.1.2` (`L45`) des vrais titres historiques publiés des `Tomes 1–8` (`specs/manifest.json:L72–79`, `4 542` pages) face au titre unifié du traité, élargissement de la démarcation `EF-06` aux `L5` et `L149` à toutes les « *entreprises privées (industrielles, commerciales, numériques ou financières)* » en incluant l'`Arrêté 2025-02` et le *Guide IA agentique* du `MCN` conformément à `ANC-117`/`ANC-118`, et maintien de la vedette `CA-07` `Statut F`.

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C36-01` à `C36-41`)

### Section 36.0 & 36.1 — En-tête, clause non-avis et résumé exécutif (`L1–L17`)

- **C36-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice cadrant la concordance structurelle, taxonomique et éditoriale des huit volumes antérieurs dans ce traité des systèmes d'entreprise (`DIV-02`, `DISC-01`–`DISC-05`), la chaîne probatoire indépendante (`Wyvern G0–G5`, `L+`/`Statut F`) et la clause opposable de `non-avis`.
  - **Appui vérifié :** `specs/manifest.json` (`ch36`, `D12`, `SUB_D12_03`), `Compendium/prd.md` (`L6488–6508`).
  - **Passe initiale :** conforme · **Action :** aligné sur `manifest.json` (Vague 2) · **Verdict : supporté**

- **C36-02 (`L5`)** — *Affirmation :* Notice opposable `non-avis` (`AO-05`, `DC-P01`, `DC-P12`, gel `2 décembre 2026`) précisant que le traité, ses schémas et sa trousse ne constituent ni un avis juridique, médical, financier ou réglementaire, ni une opinion actuarielle ni une certification d'audit, et ne remplacent pas l'homologation sur système réel ou `SoR` au sens de la Loi 25 `[7]`, BSIF `E-23` `[8]`, `AMF` `[12]` et `EU AI Act` (visé via `(UE) 2026/2274` `[9]` et le Chapitre 26), avec démarcation `EF-06` (`Arrêté 2025-02` et *Guide IA agentique* du `MCN`, `AMOPS`, `EO 14412`, `OMB M-26-15`, `SCT` sans effet de plein droit sur les entreprises privées industrielles, commerciales, numériques ou financières) et licences `CC BY 4.0` / `MIT`.
  - **Appui vérifié :** `SRC-055.txt` (`non-avis` juridique), `SRC-063.txt` (`Loi 25` `[7]`), `SRC-065.txt` (`BSIF E-23` `[8]`), `SRC-067.txt` (`[9]`), `SRC-071.txt` (`[12]`), `registre/ancres-chronologiques.json` (`ANC-117`, `ANC-118`), `specs/manifest.json` (`L10–14`), `gabarit-pdf/volumes.json` (`DC-P01`, `DC-P12`, `AO-05`).
  - **Passe initiale :** écart rectifié · **Action :** élargi `EF-06` à l'ensemble des entreprises privées et inclus les textes `MCN` (`ANC-117`, `ANC-118`) en Vague 2 · **Verdict : supporté**

- **C36-03 (`L7`, `L9`)** — *Affirmation :* Chapitre terminal clôturant la collection de `8` tomes, `4 542` pages composées en `Typst` et `319` diagrammes, dans la continuité des chapitres `34` (`305` `EXIG-* v1.2`, `EXIG-GOV-17`, `PRR-75`) et `35` (`exit 0`, `G0`, `5 SBB`), et annonçant `DIV-02`, Tome 1, `DISC-01`–`05`, glossaire, `Wyvern G0–G5`, `CA-16`, `L+`/`Statut F`, `[A]`/`[B]`/`[C]` et `3` degrés d'absence, audit des `121` références et `449` sources de l'Annexe G du Tome 2, veille `30` j, `Typst` et `non-avis`.
  - **Appui vérifié :** `Corpus/README.md` (`L29`), `registre/matrice-exig-prr-c40.json`, `Corpus/Tome 2` (`F.1`–`F.2`, `L7945–7983`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement l'audit des `449` sources aux `121` références initiales et à l'Annexe G du Tome 2 · **Verdict : supporté**

- **C36-04 (`L13`)** — *Affirmation :* Résumé du verrou de concordance : `DIV-02` soude `52` capacités (`42` inv. + `10` cond.) et `24 PEX` aux `305 EXIG-* v1.2` (`DC-P07`) et corrige trois suppositions héritées ; `DISC-01`–`05` (`concordance-taxonomies.json`) résout les conflits d'échelles, relie les `4` paquets aux Plans `A`/`B`/`C`, garantit la neutralité `ArchiMate` et épingle `MCP 2026-07-28` (`5f5440bb`) `[2, 3]` face à `SEP-2596` `[4]` et `SEP-3398` `[5]`.
  - **Appui vérifié :** `registre/concordance-taxonomies.json`, `SRC-072.txt` `[2]`, `SRC-074.txt` `[3]`, `SRC-081.txt` `[4]`, `SRC-082.txt` `[5]`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-05 (`L15`)** — *Affirmation :* Résumé du régime `Wyvern G0–G5` : règle anti-contournement `AO-01` (`A4`) écartant après une tentative toute URL bloquée (`HTTP 401/403/429/451`, `WAF`, mur payant) en **Statut F** (`lautorite.qc.ca` `[12]`, `legisquebec.gouv.qc.ca`, `genai.owasp.org` `[6]`, `iso.org` `[9]`) ; appui sur textes intégraux `L+` `SHA-256` de catégorie `A` ou `B` (`A` requise au Tome 2 pour fonder une exigence) ; séparation `G0`–`G5`, `CA-16`/`G3`, `gauntlet-loop` `G4`, `[A]`/`[B]`/`[C]`, `3` degrés d'absence et réserve `F-01`.
  - **Appui vérifié :** `specs/protocole-mlr-compendium.json` (`AO-01`), `recherche/registre-statut-f.json`, `ch36-sources.md` (`[6, 7, 9, 12]`), `Corpus/Tome 2` (`Tableau 66`, `L7951–7953`).
  - **Passe initiale :** écart rectifié · **Action :** précisé la portée distincte des catégories `A` et `B` au Tome 2 · **Verdict : supporté**

- **C36-06 (`L17`)** — *Affirmation :* Résumé de la traçabilité éditoriale et du bouclier juridique : `v1.2` (`Annexe H`), péremption `30` j (`Annexe N`), registres (`159` entrées `S-001`–`S-159` Annexe B, `999` notices Annexe I), chaîne `gabarit-pdf/` (`Markdown`, `HTML`, `PDF Typst` `6,14 × 9,21 po`, `4 542` p., `319` diagrammes), `100,0 %` inspection `G5`, `non-avis`, `EF-06` et licences `CC BY 4.0` / `MIT`.
  - **Appui vérifié :** `Corpus/README.md` (`L5`, `L29`), `gabarit-pdf/gabarit-collection.typ`, `Corpus/Tome 1` (`L11500–11712`), `Corpus/Tome 2` (`L8751`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 36.2.1 — Concordance inter-tomes (`DIV-02`), `DISC-01` à `DISC-05`, Tome 1 et glossaire (`L19–L79`)

- **C36-07 (`L25`)** — *Affirmation :* Fermeture de `DIV-02` (`corpus_2026_absent`) consignée au Tome 4 entre le modèle à cinq couches (`C1`–`C5`) + 3 volets et `CAD26` (`CRE-IA-2026-01`, `6` couches et `3` plans), réalisée au Tome 5 par inspection de `CAD26 v1.2` et des `49` pages de la `Note AMF IA`.
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`L4–8`), `Corpus/Tome 5` (`L29`, `L162`, `L265`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-08 (`L27`)** — *Affirmation :* Pont `DC-P07` reliant `52 CAP` (`42` inv. + `10` cond.), `24 PEX` (numérotées de façon non contiguë de `PEX-001` à `PEX-044`) et `305 EXIG-* v1.2` par trois relations (`couverture_directe`, `ancrage_extension` `13` avant `v1.2`, `comble_lacune_2026` `11` dont `7` subsistent en `Lacune 2026` dans `matrice-exig-prr-c40.json`), avec cinq `CAP` sans exigence `CAD26` directe (`CAP-025` sas dérogatoire et extinction `CUA`, `CAP-028` sas `OT` et continuité `72` h, `CAP-033` inférence en enclave attestée, `CAP-046` comptabilisation carbone `B-15`, `CAP-052` ingénierie assistée ségrégée).
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`L20–35`), `registre/matrice-exig-prr-c40.json` (`cap_52`, `pex_24`), `Corpus/Tome 5` (`L277`, `L331`, `L1724`, `L1776–1832`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé les descriptions erronées de `CAP-025`, `CAP-028`, `CAP-033` et `CAP-052`, séparé la ventilation `13`/`11` (avant `v1.2`) des `7` `Lacune 2026` de `matrice-exig-prr-c40.json` et précisé la numérotation non contiguë des `24 PEX` · **Verdict : supporté**

- **C36-09 (`L29–L33`)** — *Affirmation :* Correction de trois suppositions de l'Annexe E.1 du Tome 4 : `Rectification 1` (modèles et confinement en Couche 3 `CAD26` = `C5` *modeles*, non Couche 6) ; `Rectification 2` (aucune Couche 3 « Connaissance » dans `CAD26 § 5.2`, `C3` couvrant Couches 2, 3 et 5) ; `Rectification 3` (`SoR` en Couche 6 `CAD26`, non Couche 5, sous `C4` via `ACL`).
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`L9–13`), `Corpus/Tome 5` (`L271–275`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-10 (`L35`)** — *Affirmation :* Quatre coquilles `CAD26 v1.1` rectifiées (`EXIG-APP-18` p. 32 ; `EXIG-APP-12`->`EXIG-APP-17` sous `EXIG-APP-16` p. 233 ; `EXIG-MEM-01`->`EXIG-ARC-22` p. 258 et 342 ; 6 occurrences `EXIG-ARC-02`->`EXIG-ARC-21` p. 195–257) et consignation de la dissonance résiduelle `M-12` (plafond interne `N3` sans ouverture inter-organisations) par rapport aux cibles fédérées envisagées en `M-15`/`M-18` (`→ Chapitre 28`).
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`L14–19`, `L132`, `DISC-02`).
  - **Passe initiale :** conforme · **Action :** retiré `Stade 3` au lissage G5 sous `DISC-02` · **Verdict : supporté**

- **C36-11 (`L37–L39`)** — *Affirmation :* Table d'arrimage issue du Tome 5 (`section A.1` reprise dans `concordance-taxonomies.json`) reliant terme à terme `C1`..`C5` (`C1` interaction `CAP-001..006` → `Couche 1` ; `C2` agents-orchestration `CAP-007..014` → `Couche 2` + volet agents `Couche 3` ; `C3` contexte-connaissance `CAP-015..021` → travail `Couche 2`, procédurale `Couche 3`, recherche `Couche 5` ; `C4` accès `CAP-022..028` → `Couches 4/5/6` homologue `C6` côté données ; `C5` modèles `CAP-029..034` → `Couche 3`) et les trois volets transversaux (`Plans A`, `B`, `C`, couvrant `C6 Gouvernance`) aux six couches (`Couches 1`–`6`, répondant aux `6` couches `C1`–`C6` des repères sectoriels) et trois plans de `CAD26 § 5.2–5.3`.
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`L37–102`), `Corpus/Tome 5` (`L1711–1724`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé l'intitulé inexistant `Tableau A.1` par `section A.1` et explicité l'arrimage complet `C3`, `C5` et `C6` (`post-G4`) · **Verdict : supporté**

- **C36-12 (`L45`, `L47`)** — *Affirmation :* Concordance titulaire sous `AO-02` préservant les huit titres historiques publiés des Tomes `1` à `8` (`4 542` pages dans `specs/manifest.json:L72–79`) subsumés sous *Interopérabilité et automatisation agentique des systèmes d'entreprise* ; Tome 1 gelé au `27 juillet 2026` avec revalidations jusqu'au `1er novembre 2026`, organisé en `5` Livres et `50` chapitres, uni par `5` exigences de gouvernance transversales adossées à l'invariant à `4` termes (`§ 1.0.2` : découplage, contrat, évolution, exploitation) et aux Annexes `B` (`S-001`–`S-159`), `I` (`999` notices) et `N`.
  - **Appui vérifié :** `specs/manifest.json` (`L4`, `L72–79`), `Corpus/Tome 1` (`L13–33`, `L131–143`), `Tomes/Tome 1.../00 - Présentation des cinq livres.md` (`L1–15`).
  - **Passe initiale :** conforme · **Action :** acté la concordance titulaire des `8` Tomes publiés sous `AO-02` (Vague 2) · **Verdict : supporté**

- **C36-13 (`L43`, `L45`)** — *Affirmation :* Réconciliation interne des Volumes I, II et III au ch. 43 du Tome 1 : `Tableau 43.1` (fusion 4+3 -> 6 couches alignées sur `CAD26`), `Tableau 43.3` (équivalence des 3 échelles homonymes avec retrait du continuum `0–5` et `L0–L3` Boréalis), `§ 37.0` (homonymies fabrique d'identité/agents et *AgentMesh* Solace/Solo.io), `§ 50.4` (registre de gel) et `Tableau 49.1` (`§ 49.12`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L8746`, `L9863–9865`, `L9982–9988`, `L11297`, `L11482`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-14 (`L47`, `L49`)** — *Affirmation :* Insertion et légende de la Figure 1 (`SCH-36-01.svg`) illustrant le pont structurel `DIV-02`, la réconciliation interne du Tome 1 et le glossaire `Tableau 65`.
  - **Appui vérifié :** `specs/manifest.json` (`ch36`, `SCH-36-01`), `schemas/SCH-36-01.puml`, `schemas/rendus/SCH-36-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-15 (`L53–L56`)** — *Affirmation :* Contexte des cinq discordances transversales (`DISC-01` à `DISC-05`) tranchées au Tome 8 (`§ 0.2`) et dans `concordance-taxonomies.json`, avec renvoi consolidé vers le calendrier `2023–2035` en `→ Annexe C`.
  - **Appui vérifié :** `Corpus/Tome 8` (`L40–48`), `registre/concordance-taxonomies.json` (`L186–292`).
  - **Passe initiale :** conforme · **Action :** ajouté renvoi `→ Annexe C` (lissage G5) · **Verdict : supporté**

- **C36-16 (`L57`, Tableau 36.1 `DISC-01`)** — *Affirmation :* Arbitrage `DISC-01` conservant `L0–L4` pour les droits de mutation/sortie externe avec tri amont isolant tout flux sans modèle avant d'appliquer `L0–L1` en lecture seule (`policies_opa`, ch. 05).
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`L188–205`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-17 (`L56`, Tableau 36.1 `DISC-02`)** — *Affirmation :* Arbitrage `DISC-02` (`AO-03`) proscrivant dans la prose et le code du Tome 8 `Classe 1–6`, `Stade 0–4` et `Palier 1–3` au profit exclusif de `BLOQUANT`, `OBLIGATOIRE`, `RECOMMANDE` et des paliers d'outils `P0–P3` avec table de correspondance inter-tomes (`→ Annexe C`).
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`L207–229`), `Compendium/prd.md` (`L6901`).
  - **Passe initiale :** conforme · **Action :** révision `REV-04` (`PRD-L4-014`) : recadrage exact de la portée de `DISC-02` sur la prose et le code du Tome 8 avec table de correspondance inter-tomes · **Verdict : supporté**

- **C36-18 (`L59`, Tableau 36.1 `DISC-03`)** — *Affirmation :* Arbitrage `DISC-03` raccordant les modules Python/`OPA` du Tome 8 aux Plans `A`, `B` et `C` du cadre `CAD26` (`5 SBB`).
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`L231–253`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-19 (`L60`, Tableau 36.1 `DISC-04`)** — *Affirmation :* Arbitrage `DISC-04` posant la neutralité `ArchiMate 3.2` / `4.0 C260` (`27 avril 2026`) sans artefact propriétaire requis en `G0`.
  - **Appui vérifié :** `registre/concordance-taxonomies.json` (`L255–272`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-20 (`L61`, Tableau 36.1 `DISC-05`)** — *Affirmation :* Arbitrage `DISC-05` épinglant `MCP 2026-07-28` (`5f5440bb`) en `Streamable HTTP` sans état face au témoin `2025-11-25` `[1]`, verrouillant `StreamableHttpAdapter` sur `Mcp-Method`/`Mcp-Name` `[2, 3]` et isolant via `McpTransportAdapter` l'échéance `SEP-3398` (`30 mars 2027` `[5]`) et la fenêtre `SEP-2596` (`2027-07-28` `[4]`).
  - **Appui vérifié :** `SRC-038.txt` `[1]`, `SRC-072.txt` `[2]`, `SRC-074.txt` (`L288–293` `[3]`), `SRC-081.txt` `[4]`, `SRC-082.txt` `[5]`, `registre/concordance-taxonomies.json` (`L274–291`).
  - **Passe initiale :** écart rectifié · **Action :** distingué le verrouillage des en-têtes sur `StreamableHttpAdapter` de l'isolation par `McpTransportAdapter` des jalons `SEP-3398`/`SEP-2596` · **Verdict : supporté**

- **C36-21 (`L65`, `L67`)** — *Affirmation :* Rôle du témoin `MCP 2025-11-25` `[1]`, rejet de `HTTP+SSE` au profit de `Streamable HTTP` sans état `2026-07-28` (`5f5440bb`) `[2, 3]`, et protection par `McpTransportAdapter` contre `SEP-2596` (statut `Final`, archivée au commit du `22 novembre 2026`, `12` mois minimum pour toute nouvelle dépréciation soit jusqu'au `28 juillet 2027` pour `2026-07-28`, avec grâce transitoire de `3` mois pour les fonctions déjà dépréciées telles qu'`HTTP+SSE` `[4]`) et `SEP-3398` (`Accepted` `14 octobre 2026`, dernier mardi de mars/septembre, report déc. 2026 -> `30 mars 2027` `[5]`).
  - **Appui vérifié :** `SRC-038.txt` `[1]`, `SRC-072.txt` `[2]`, `SRC-074.txt` (`L16–21` `[3]`), `SRC-081.txt` (`L106–111`, `L216–234` `[4]`), `SRC-082.txt` (`L3–17`, `L203` `[5]`).
  - **Passe initiale :** écart rectifié · **Action :** distingué la fenêtre de `12` mois des nouvelles dépréciations de la grâce transitoire de `3` mois pour `HTTP+SSE` sous `SEP-2596`, précisé la date de commit d'archive du `22 novembre 2026` et scindé en deux paragraphes (`CA-05`) · **Verdict : supporté**

- **C36-22 (`L69`, `L71`)** — *Affirmation :* Insertion et légende de la Figure 2 (`SCH-36-02.svg`) visualisant les convertisseurs canoniques `DISC-01`–`DISC-05`.
  - **Appui vérifié :** `specs/manifest.json` (`ch36`, `SCH-36-02`), `schemas/SCH-36-02.svg`, `schemas/rendus/SCH-36-02.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-23 (`L75`)** — *Affirmation :* Glossaire bilingue normatif `fr-CA`/`en` (`Tableau 65`, Annexe E du Tome 2) unifiant les définitions de `A2A`, `AAIF`, `CIBA`, `EIF`, `EFVP` (`ÉFVP`), `FinOps`, `MCP`, `NHI`, `OBO`, `ODD`, `PEP`, `RIA`, `SVID` et `SMIA`.
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 65`, `L7815–7934`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la graphie sur l'entrée exacte `EFVP` du `Tableau 65` tout en conservant `ÉFVP` · **Verdict : supporté**

- **C36-24 (`L77`)** — *Affirmation :* Transposition française `RFC 2119` (`MUST` -> `DOIT`, `MUST NOT` -> `NE DOIT PAS`, `SHOULD` -> `DEVRAIT` `[11]`) et règle de préséance du texte normatif du corps et du `Tableau 7` sur le `Tableau 65`.
  - **Appui vérifié :** `SRC-125.txt` (`L30–40` `[11]`), `Corpus/Tome 2` (`L717`, `L7813`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-25 (`L79`)** — *Affirmation :* Table de correspondance des trois blueprints du ch. 14 du Tome 6 vers `matrice-exig-prr-c40.json` (`bp1_assistant_interne`, `bp2_rag_entreprise_acl`, `bp3_orchestration_multi_agents_b2b`) pour `C01`–`C40`.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`c01_c40_blueprints`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 36.2.2 — Chaîne probatoire `Wyvern`, `G0–G5`, `Statut F` / `L+`, `gabarit-pdf/` et `non-avis` (`L81–L141`)

- **C36-26 (`L85`)** — *Affirmation :* Politique anti-contournement `AO-01` (`A4` en `W2.1`/`W3.2` du Tome 3) proscrivant le contournement de `HTTP 401/403/429/451`, `WAF`, `CAPTCHA`/`Anubis` ou mur payant, avec arrêt après au plus une requête infructueuse et consignation en **Statut F** (`included_in_evidence: false`).
  - **Appui vérifié :** `specs/protocole-mlr-compendium.json` (`L5–21`), `recherche/registre-statut-f.json` (`L4`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-27 (`L87`)** — *Affirmation :* Exigence de textes intégraux ouverts `[L+]` hachés `SHA-256` après normalisation `LF`, notés `>= 9,0/12` sur `AACODS`, et classement Tome 2 en catégorie `A` ou `B` (`B` insuffisante seule pour une exigence, `C` exclue en appui).
  - **Appui vérifié :** `specs/protocole-mlr-compendium.json` (`L19–20`, `L40–43`), `recherche/manifeste-sources-sha256.json` (`L4`), `Corpus/Tome 2` (`Tableau 66`, `L7951–7953`).
  - **Passe initiale :** écart rectifié · **Action :** précisé que la catégorie `B` est insuffisante seule pour fonder une exigence · **Verdict : supporté**

- **C36-28 (`L89–L94`)** — *Affirmation :* Bilan quantitatif `W3.2` Tome 3 (`582` notices brutes de `5` API scientifiques ouvertes productives sur `9` interrogées dont `3` `Statut F`, `453` dédupliquées, `κ = 0,7935`, `223` textes intégraux `SHA-256`, `160` études `L+`, `83` résumés remplacés, `0,0 %` sur résumé seul, `1 101` occurrences d'URLs ; `95` `L+` Tome 8, `79` `L+` Tome 7) et quatre exclusions `Statut F` (`lautorite.qc.ca` `[12]`, `legisquebec.gouv.qc.ca` `[7]`, `genai.owasp.org` `[6]`, `iso.org` `[9]`).
  - **Appui vérifié :** `Corpus/Tome 3` (`L26081`, `L26446–26472`, `L28244`), `Corpus/README.md` (`L27–28`), `ch36-sources.md` (`L143–148`), `recherche/registre-statut-f.json`.
  - **Passe initiale :** écart rectifié · **Action :** précisé « productives (sur neuf interrogées, dont trois consignées en Statut F) » et « occurrences d'URLs » · **Verdict : supporté**

- **C36-29 (`L96`)** — *Affirmation :* Appareil critique du Tome 1 (`[A]`, `[B]`, `[C]`, avec interdiction d'appuyer un fait central sur `[C]`) et marqueurs d'ingénierie de preuves (`[N]`, `[M]`, `[É]`, `[S]`, `[D]`, `[L+]`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L11504–11506`), `Compendium/prd.md` (`L6490–6508`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-30 (`L98`)** — *Affirmation :* Qualification des négations selon les **trois degrés d'absence** (`degré 1`, `degré 2`, `degré 3`), réserve cryptographique `F-01` et refus de lissage (`Tableau 11.5`, distinction « démontre » / « promet », exemple `S-090` / `S-091` `28 avril 2026`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L2684–2692`, `L3226`, `L11504`, `L11606–11607`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-31 (`L102`, `L104`)** — *Affirmation :* Audit en trois passes du Tome 2 (`27–28 octobre 2026`, déduplication `19 novembre 2026`) : `121` références (`108` accessibles), `427` liens, correction/remplacement/retrait de `302` sur `427` (`70,7 %`, plus de sept sur dix), `32` corrections au `Tableau 68`, `11` vérifications thématiques, `1 409` affirmations sur `428` références -> `473` entrées Annexe G -> `448` sources distinctes le `19 novembre 2026` (`25` doublons fusionnés) -> `449` en `v1.1` par ajout de `[474]` (`RFC 7515`), classées `A`, `B` (Gartner reclassé) et `C` (proscrite en appui), avant `[475]`–`[498]` en Annexe H.
  - **Appui vérifié :** `Corpus/Tome 2` (`L7941–7997`, `L8750`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé `71 %` par `302 sur 427 (70,7 %)`, distingué `448` (`19 novembre`) de `449` (`v1.1` `[474]`) avant `[475]`–`[498]` et scindé en deux paragraphes selon `CA-05` · **Verdict : supporté**

- **C36-32 (`L106–L117`, Tableau 36.2)** — *Affirmation :* Pipeline `Wyvern G0–G5` fondé sur `CA-19`, canonisation `RFC 8785` (`JCS`) `[10]` préalable à `SHA-256`, et synthèse des six barrières (`G0` `execute_g0.py` : `83/83` `pytest`, `45/45` `OPA` à `100,0 %`, `4/4` vecteurs `50` fichiers, `SPDX MIT`, `14/14` `CA-G0-SYNC` à `exit 0` ; `G1` `verifie_manuscrit.py --strict` ; `G2` `1 087` T7, `577` T8, `356` corr. et `1 614` compl. T3 ; `G3`/`CA-16` `60/60` T4 [`120`]/T7/T8, `40/40` T5, `148` Compendium ; `G4` `gauntlet-loop` ; `G5` `genere_annexes.py`, `assemble_livre.py`, `5` annexes, `100 %`).
  - **Appui vérifié :** `SRC-077.txt` `[10]`, `aq/rapports-g0.json` (`L11–176`), `outils/verifie_manuscrit.py` (`L1404`), `Corpus/README.md` (`L27–28`), `Corpus/Tome 3` (`L34`), `Corpus/Tome 4` (`L58`), `Corpus/Tome 5` (`L52`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-33 (`L119`, `L121`)** — *Affirmation :* Insertion et légende de la Figure 3 (`SCH-36-03.svg`) reliant collecte `L+`/`Statut F`, degrés d'absence/`F-01`, pipeline `G0–G5` et double recollation `CA-16`.
  - **Appui vérifié :** `specs/manifest.json` (`ch36`, `SCH-36-03`), `schemas/SCH-36-03.puml`, `schemas/rendus/SCH-36-03.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-34 (`L125`)** — *Affirmation :* Actualisation novembre 2026 (`Annexe H` Tome 2) : réexamen le `1er novembre 2026` des `24` dépendances datées (`22/24` directes, `2/24` partielles sous réserve `HTTP 403`/résumé Web), remédiation du `19 novembre` ajoutant un contrôle déterministe `24/24` et un protocole stratifié `n ≥ 8/24` pour les réouvertures ultérieures ; `Tableau 72` (`9` sièges `A2A`, `SEP-3398` `[5]`, erratum `RTR` `9 novembre 2026`) ; unification `DC-P08` (`19 novembre 2026`, `287` -> `305` `EXIG-* v1.2` avec `12 EXIG-AMF` et `6` ajouts `PQC`, `ACVM`, `RTR`, `EN 18286:2026` `[9]`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L8657`, `L8724–8751`), `SRC-082.txt` `[5]`, `SRC-067.txt` `[9]`.
  - **Passe initiale :** écart rectifié · **Action :** distingué l'état du `1er novembre` (`22/24` directes + `2/24` partielles) du contrôle déterministe `24/24` et du protocole stratifié prospectif `n ≥ 8/24` du `19 novembre` · **Verdict : supporté**

- **C36-35 (`L127`, `L129`)** — *Affirmation :* Protocole de péremption du ch. 50 Tome 1 (`§ 50.3`, seuil `30` j, `14` événements `Tableau 50.1` en trois états types) et exécution à l'Annexe N au `1er novembre 2026` (`[AN-1]`–`[AN-27]`, `N.1`–`N.4`, `SEP-3398` `[5]`, `NIST IR 8547 Final` `2030`/`2035` `← ch18`, calendrier `EU AI Act` `← ch26`, `EN 18286:2026` `[9]`, Note AMF `N.3`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L11443–11474`, `L12871–13017`), `SRC-051.txt` (`2030`/`2035`, `← ch18`), `SRC-082.txt` `[5]`, `SRC-067.txt` `[9]`.
  - **Passe initiale :** conforme · **Action :** en recollation `G3` (`seed=20270901`), dissocié `EN 18286:2026` `[9]` du calendrier `EU AI Act` (`← ch26`) et ajouté le renvoi `← ch18` sur `NIST IR 8547 Final` · **Verdict : supporté**

- **C36-36 (`L131`)** — *Affirmation :* Indexation dans les deux registres consolidés du Tome 1 : Annexe B (`159` entrées `S-001`–`S-159` : `S-001`–`S-046` Vol. II, `S-047`–`S-142` Vol. III, `S-143`–`S-159` Vol. I) et Annexe I (`1 263` notices dédupliquées en `999` entrées uniques `§ I.1`, `§ I.2`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L11496–11506`, `L11701–11713`, `L12853`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-37 (`L145`, `L147`)** — *Affirmation :* Chaîne unifiée `gabarit-pdf/` (`volumes.json`, `compile_diagrams.py`, `compile_pdf.py`) compilant les `319` diagrammes des tomes (`253` `PlantUML` `.svg` et `66` `Mermaid` `.png` au facteur `3`) et les `8` volumes `Typst` (`6,14 × 9,21 po`, corps `10,6` pt, `4 542` pages PDF, ~`72,81` Mo, plus `2` `HTML` Tomes 7 et 8) ; compilation des `139` schémas du traité par `compile_schemas_compendium.py` (`58` `PlantUML` `.svg` `-failfast2`, `23` `Mermaid` `.png`, `58` `SVG`) ; synchronisation `LF` et embarquement `base64` (`23` T7, `9` T8, `139` `Compendium.html`) ; contrôle visuel `100 %` en `G5`.
  - **Appui vérifié :** `gabarit-pdf/volumes.json`, `gabarit-pdf/gabarit-collection.typ`, `gabarit-pdf/compile_diagrams.py` (`L38`, `L374–384`), `outils/compile_schemas_compendium.py`, `outils/verifie_manuscrit.py`, `specs/manifest.json` (`139` figures), HTML Tomes 7–8 (`23`/`9` `base64`).
  - **Passe initiale :** écart rectifié · **Action :** aligné le décompte sur les `139` schémas du traité (`58` + `23` + `58`) · **Verdict : supporté**

- **C36-38 (`L149`, `L151`, `L153`)** — *Affirmation :* Bouclier juridique opposable (`DC-P01`, `AO-05`, `EF-06` `MCN Arrêté 2025-02`/`Guide IA agentique`/`AMOPS`/`EO 14412`/`OMB M-26-15`/`SCT` sans extension aux entreprises privées industrielles, commerciales, numériques ou financières, `DC-P12`, `CC BY 4.0`/`MIT`) et Figure 136 (`SCH-36-04.png`).
  - **Appui vérifié :** `registre/ancres-chronologiques.json` (`ANC-117`, `ANC-118`), `gabarit-pdf/volumes.json`, `specs/manifest.json` (`ch36`, `SCH-36-04`), `schemas/SCH-36-04.mmd`, `schemas/rendus/SCH-36-04.png`.
  - **Passe initiale :** conforme · **Action :** élargi `EF-06` aux entreprises privées (Vague 2) · **Verdict : supporté**

### Section 36.3 — Synthèse transversale, livrables et invariants (`L143–L165`)

- **C36-39 (`L145`, `L147`)** — *Affirmation :* Articulation amont (`ch05` `[2]`, `ch25`–`26` `[7, 8, 9, 12]`, `ch29`, `ch34`, `ch35`) et aval (`ch01`, `ch03`, `ch07`, `ch08`, `ch18`, `ch19`, `ch28`, `ch30`, `ch34`, `ch35`) conforme à la partition `CA-21`.
  - **Appui vérifié :** `specs/manifest.json` (`ch36`, `owned_concepts`), `outils/verifie_manuscrit.py` (`CA-21`), `Compendium/plan.md` (`L1705`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C36-40 (`L161–L171`, Tableau 36.3)** — *Affirmation :* Génération mécanique sans retouche des `5` Annexes (`CA-17`, dont les réconciliations inter-tomes en `→ Annexe C`) et récapitulatif des cinq livrables de concordance (`EXIG-CONC-01..06` du plan directeur du traité, `DC-P07`, `AO-01`/`A4`, `CA-09..18`, `DC-P08`, `AO-05`, `EF-06`) avec renvois `[2, 3, 4, 5, 6, 7, 9, 10, 12]`.
  - **Appui vérifié :** `Compendium/prd.md` (`L6502–6507`), `outils/genere_annexes.py`, `outils/verifie_manuscrit.py` (`CA-17`), `ch36-sources.md` (`[2..7, 9, 10, 12]`).
  - **Passe initiale :** écart rectifié · **Action :** aligné les décomptes des rangées `4` et `5` (`24` dépendances / `n ≥ 8/24`, `319` + `139` schémas, `HTML` `23`/`9`/`139`), remplacé `(plan directeur du Compendium)` par `(plan directeur du traité)` et ajouté le renvoi `→ Annexe C` · **Verdict : supporté**

- **C36-41 (`L159–L163`)** — *Affirmation :* Trois invariants exécutables du Chapitre 36 (`EXIG-CONC-01` concordance `DIV-02` et `DISC-01`–`05` bornant la proscription `DISC-02` à la prose et au code du Tome 8 ; `AO-01`/`CA-16`/`CA-17` intégrité `L+`/`Statut F` et `Wyvern G0–G5` ; `DC-P01`/`AO-05`/`EF-06` fraîcheur `30` j, `gabarit-pdf/` et clause `non-avis`).
  - **Appui vérifié :** `Compendium/prd.md` (`L6502–6507`, `L6563`, `L6901`), `registre/concordance-taxonomies.json`, `outils/verifie_manuscrit.py`, `schemas/SCH-36-03.puml`.
  - **Passe initiale :** conforme · **Action :** révision `REV-04` : renumérotation continue `Figure 112` à `Figure 115` (`PRD-L4-012`), recadrage `DISC-02` + explicitation `EXIG-AMF-01..12`, `EXIG-CON-27..30`, `EXIG-SEC-27..28` (`PRD-L4-014`), suppression des `5` mentions `prd.md` au `Tableau 36.3` et de `gauntlet-loop` (`PRD-L4-015`, `SCH-36-03.puml` `PRD-L4-027`), harmonisation `H2`/`H3` (`PRD-L4-022`) et nuance explicite de source secondaire `AIBanks.ca` sur `[12]` (`REF-003`) · **Verdict : supporté**
