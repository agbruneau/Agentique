# Journal d'ancrage atomique Wyvern G2 — Chapitre 26 (`ch26`)

- **Unité auditée :** `Sources/Compendium/ouvrage/manuscrit/09 - Partie IX/Chapitre 26.md` (`4 570` mots de prose selon `verifie_manuscrit.py`, plage `[4 251, 4 989]`)
- **Base documentaire fermée :** `Sources/Compendium/ouvrage/sources/ch26-sources.md` (`[1]`–`[7]` en statut `L+`, `3` exclusions `statut F`, Option A iso-corpus) ; textes intégraux `Sources/Compendium/ouvrage/recherche/corpus_l_plus/SRC-{052,060,061,062,067,069,109}.txt` ; registres `Sources/Compendium/ouvrage/registre/*.json` ; protocole `Sources/Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Sources/Compendium/ouvrage/aq/rapports-g0.json`) ; index heuristique interne `Sources/Tomes/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-5` (mise à jour Vague 2 `auteur-d09-d10`)
- **Passe G2 initiale (supportés) :** 9
- **Rectifications appliquées lors de la passe G2 et du rééquilibrage multisectoriel :** 24
- **Verdict final — supportés :** 33 / 33 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 26.md`

Toutes les formulations divergentes, sur-attribuées ou relevant du repérage antérieur hors corpus `L+` fermé relevées lors de la passe initiale, ainsi que le rééquilibrage multisectoriel vers l'ensemble des systèmes d'entreprise en Option A iso-corpus, ont été ancrés directement dans [Chapitre 26.md](file:///c:/Github/Agentique/Sources/Compendium/ouvrage/manuscrit/09%20-%20Partie%20IX/Chapitre%2026.md), sans altérer `CA-01`..`CA-22`, en préservant les `owned_concepts` (`eu-ai-act`, `systeme-qualite-en-18286-dora-cra`, `maillage-reglementaire-international`, `iso-iec-42001-nist`, `souverainete-espaces-donnees-tee-hyok`, `cadres-internationaux-imda-aica-g7`, `classes-risque-agents-et-plafonds`, `incidents-agentiques-et-notification-multiregime`), les renvois `[1]`–`[7]` et le calibrage (`4 570` mots dans `[4 251, 4 989]`) :

1. **Qualification européenne transversale des systèmes d'entreprise (`L1`–`L17`, `L25`–`L63`, `Tableau 26.1`, `Figure 94`) :** alignement du titre `L1` sur `specs/manifest.json` et de l'alt-text/légende de `SCH-26-01` (`Figure 94`) ; mise en avant du spectre multisectoriel de l'`EU AI Act` (`Annexe I` machines industrielles et dispositifs médicaux au `2 août 2028` `ANC-010`, `Annexe III` infrastructures critiques point `2`, recrutement/`SIRH` point `4`, services publics point `5(a)`, crédit `5(b)` et assurance vie/santé `5(c)` au `2 décembre 2027` `ANC-007` `[1, 2]`), du risque de requalification fournisseur d'une DSI sur un `ERP`, `SIRH` ou `MES` (`article 25(1)` `[1, 2]`), de la cyberrésilience multisectorielle `NIS 2` (`ANC-006`, repérage `Tome 1`) aux côtés de l'étalon financier `DORA` (`[3]`), et du socle européen d'interopérabilité (`CRA` `SBOM` cité en `[2]` `ANC-008`, `(UE) 2024/903` `EIF`, `eIDAS 2.0`, `PSD2`, `Data Act` `ANC-003`).
2. **Portes `PRR G-03`, `G-07` et `G-08` (`L13`, `L73`, `Tableau 26.3`, `L128`) :** alignement strict sur `registre/matrice-exig-prr-c40.json` (`PRR G-03` pour la qualification réglementaire et le plafonnement par pire cas `EXIG-CON-01..02`, `PRR G-07` pour l'article `50` au `2 août 2026`, `PRR G-08` pour l'Annexe III au `2 décembre 2027`).
3. **Séparation stricte entre preuves `L+` (`[1]`–`[7]`), `statut F` et repérage interne (`L15`–`L21`, `L53`–`L71`, `L97`–`L103`) :** attribution exacte d'`EN 18286:2026` (`(UE) 2026/2274` `[4]` et DG CNECT `[5]`) comme preuve ouverte `L+` remplaçant `ISO/IEC 42001:2023` (`statut F` sur `iso.org`) ; qualification des `19` CTI de novembre 2025, `US SR 26-2` / `OCC 2026-13`, `UK PRA SS1/23`, `MiFID II`, `AMLR`, Directive `(UE) 2024/2853` (`ANC-002`), `NIST AI RMF 1.0` / `600-1`, `IMDA v1.5` et `AICA`/`IAIS` comme issus du repérage des `Tomes 1` à `4` hors corpus `L+` fermé de ce chapitre, en réservant `[6]` à la feuille de route PQC du `G7 CEG` (`14 janvier 2026`) et `[7]` (Bostan) à la propagation systémique dans les chaînes logistiques numériques.
4. **Souveraineté matérielle des six substrats d'état (`L21`, `L97`–`L107`, `Figure 96`) :** qualification d'`ADR-027` (« acceptée sous réserve », `PRR F-04..F-06`), de la grille `SEAL-0..4`, des boucliers `Classe-S2` (`HYOK` `HMAC-FPE`, `RTT ≤ 35 ms` en mode fermé *fail-closed*) et `Classe-S3` (`CPU`/`GPU TEE` `CAP-033`, `SIG-016`, limite `DDR5` `TEE.fail` `< 1 000 $ US`) ainsi que des cibles `RTO < 15 min` / `RPO = 0` comme choix et cibles de conception internes (`Tome 3 § 37, § 46`, `Tome 5 § 9.2`) sans simulation `GPU TEE` locale en barrière `G0`.

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C26-01` à `C26-33`)

### Section introductive et Section 26.1 — Résumé exécutif (`L1–L21`)

- **C26-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice posant l'unification sous index probatoire unique, interfaces interopérables et souveraineté matérielle des six substrats d'état des obligations européennes (`EU AI Act`, `DORA`, `CRA`, `NIS 2`, `Data Act`) et des référentiels internationaux applicables aux systèmes d'entreprise.
  - **Appui vérifié :** `specs/manifest.json` (`ch26`, `D09`, `SUB_D09_02`, `owned_concepts`), `registre/mindmap-complet.json`.
  - **Verdict : supporté**

- **C26-02 (`L5`, `L7`)** — *Affirmation :* Cadrage de la deuxième section de `D09` au gel du `2 décembre 2026` pour toute entreprise opérant à l'international, clause `non-avis` (`AO-05`), interdiction de transposition mécanique avec le droit canadien/québécois (`↔ ch25`), preuve primaire `L+` `[1]`–`[7]` et consignation en `statut F` (`AO-01`) d'`iso.org` (`HTTP 403`), `standards.cencenelec.eu` (`HTTP 500`) et `eur-lex.europa.eu` (`AWS WAF`), substitués par EUR-Lex Cellar et `EN 18286:2026` `[4, 5]`.
  - **Appui vérifié :** `sources/ch26-sources.md`, `recherche/registre-statut-f.json`, `SRC-067.txt`, `SRC-069.txt`, `SRC-109.txt`.
  - **Verdict : supporté**

- **C26-03 (`L11`)** — *Affirmation :* Pilier 1 — Le Règlement `(UE) 2024/1689` (*EU AI Act* ou RIA) saisit tout fournisseur ou déployeur établi dans un pays tiers dès que les sorties sont utilisées dans l'Union (`article 2(1)`) ; interdictions `article 5` applicables depuis le `2 février 2025` et règles `GPAI` depuis le `2 août 2025` (échéance `2 août 2027` pour modèles préexistants) `[1]`.
  - **Appui vérifié :** `SRC-060.txt` (`art. 2(1)(c)`, `art. 111 § 3`, `art. 113 a)-b)`).
  - **Verdict : supporté**

- **C26-04 (`L13`)** — *Affirmation :* Transparence `article 50` applicable depuis le `2 août 2026` avec transition au `2 décembre 2026` (`article 50 § 2`) et nouvelles interdictions (`article 5`, `b bis` et `b ter`) `[1, 2]` ; Règlement `(UE) 2026/1744` du `8 juillet 2026` (*Digital Omnibus*, publié le `24 juillet 2026`, en vigueur le `27 juillet 2026`) reportant l'`Annexe III` (`SIRH`, infrastructures critiques, services publics, crédit, assurance vie/santé) au `2 décembre 2027` (`PRR G-08`) et l'`Annexe I` (machines industrielles, dispositifs médicaux) au `2 août 2028`, cadencant `EXIG-CON-13..16`, `PRR G-03` et `PRR G-07` `[1, 2]`.
  - **Appui vérifié :** `SRC-060.txt`, `SRC-061.txt`, `registre/matrice-exig-prr-c40.json` (`G-03`, `G-07`, `G-08`).
  - **Verdict : supporté**

- **C26-05 (`L15`, `L17`)** — *Affirmation :* Pilier 2 — Triple qualification simultanée `[1, 3]` : modèle décisionnel (`RIA` `[1]`, `US SR 26-2` hors IA générative/agentique et `UK SS1/23` au repérage `Tome 1`) ; TIC, cyber et interopérabilité (`NIS 2` `ANC-006` pour industrie/énergie/santé/transport/numérique, étalon `DORA` depuis le `17 janvier 2025` `[3]`, `CRA` `(UE) 2024/2847` cité en `[2]`, `11 décembre 2027`, `ANC-008`) ; produits, chaînes logistiques et marchés (Directive `(UE) 2024/2853` après `9 décembre 2026` `ANC-002`, propagation systémique éclairée par Bostan `[7]`, `MiFID II` et `AMLR` sous réserve `Tome 1`) ; `SMQ` (`article 17`) couvert par `EN 18286:2026` (`(UE) 2026/2274` du `12 octobre 2026`, `EXIG-CON-30`) remplaçant `ISO/IEC 42001:2023` (`statut F`) `[4, 5]`.
  - **Appui vérifié :** `SRC-060.txt` `[1]`, `SRC-061.txt` `[2]`, `SRC-062.txt` `[3]`, `SRC-067.txt` `[4]`, `SRC-069.txt` `[5]`, `SRC-109.txt` `[7]`, `ancres-chronologiques.json` (`ANC-002`, `ANC-006`, `ANC-008`), `Tome 1 § 30.2`.
  - **Verdict : supporté**

- **C26-06 (`L19`)** — *Affirmation :* Pilier 3 — Référentiels volontaires (`NIST AI RMF 1.0`, `NIST AI 600-1`, `ISO/IEC 42005:2025`, `IMDA Agentic AI v1.5`, `AICA`/`IAIS`, repérage `Tome 2`/`3`/`4`), feuille de route PQC du `G7 CEG` (`14 janvier 2026` `[6]`), plafonds `EXIG-CON-02`, `EXIG-CON-18`, `EXIG-CON-26` et riposte `S1`–`S4` cumulant `24 h` BSIF (`← ch25`), `72 h` cible RGPD/CAI/LPRPDE (`Tome 2`) et `2`/`10`/`15` jours RIA `art. 73` `[1]`.
  - **Appui vérifié :** `SRC-052.txt` `[6]`, `SRC-060.txt` `[1]`, `Tome 2` (`EXIG-CON-02`, `18`, `23..26`).
  - **Verdict : supporté**

- **C26-07 (`L21`)** — *Affirmation :* Pilier 4 — Insuffisance de l'hébergement géographique face au `CLOUD Act` (repérage `Tome 3`) ; architecture cible `ADR-027` (`SEAL-0..4`, `F-04`..`F-06`) étendant par choix interne le géorepérage aux six couches d'état des systèmes d'entreprise (`HMAC-FPE` sous `HSM HYOK` en `classe de souveraineté C2`, enclaves `CPU`/`GPU TEE` en `classe de souveraineté C3`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`ADR-027`, `F-04..F-06`), `Tome 3 § 37.1, § 46.9–46.13`.
  - **Verdict : supporté**

### Section 26.2.1 — Droit de l'Union européenne (`L25–L65`, Tableau 26.1, Figure 94)

- **C26-08 (`L27`)** — *Affirmation :* Portée extraterritoriale `article 2(1)` et définition fonctionnelle `article 3(1)` couvrant toute automatisation agentique `[1]` ; inscription à la fiche (`EXIG-CON-13`) et classement d'office **Élevée** (`EXIG-CON-01`) dans un domaine de l'`Annexe III` par choix interne écartant l'article `6(3)` `[1]`.
  - **Appui vérifié :** `SRC-060.txt` (`L3039–3040`, `L3108–3112`), `Tome 2` (`EXIG-CON-01`, `EXIG-CON-13`).
  - **Verdict : supporté**

- **C26-09 (`L29`, `L31`)** — *Affirmation :* Calendrier réorganisé sans moratoire par `(UE) 2026/1744` (`8 juill. 2026`, pub. `24 juill. 2026`, vigueur `27 juill. 2026`) : interdictions `article 5` (`2 février 2025` et `2 décembre 2026` points `b bis`/`b ter`, `EXIG-CON-14`), `GPAI` (`2 août 2025` / `2 août 2027` `art. 111 § 3`), transparence `article 50 §§ 1–3` depuis le `2 août 2026` et transition `art. 50 § 2` au `2 décembre 2026` (`ANC-001`), étendue par `EXIG-CON-19..20` `[1, 2]`.
  - **Appui vérifié :** `SRC-060.txt`, `SRC-061.txt`, `ancres-chronologiques.json` (`ANC-001`), `Tome 2`.
  - **Verdict : supporté**

- **C26-10 (`L33`, `L35`)** — *Affirmation :* Haut risque reporté au `2 décembre 2027` (`Annexe III`, `ANC-007`) et au `2 août 2028` (`Annexe I` : machines industrielles, jouets, ascenseurs, équipements radio, dispositifs médicaux, `ANC-010`) ; bac à sable au `2 août 2027` ; orientations `art. 72 § 3` au `2 septembre 2027` ; délais `2 août 2030` (`art. 111 § 2`) et `fin 2030` (`art. 111 § 1`) ; réexamens de `2028` à `2033` (`art. 112 §§ 2–3`) ; spectre multisectoriel de l'`Annexe III` (`point 2` infrastructures critiques, `point 4` `SIRH`/emploi, `point 5(a)` services publics, `5(b)` crédit hors fraude, `5(c)` assurance vie/maladie hors dommages) `[1, 2]`.
  - **Appui vérifié :** `SRC-060.txt`, `SRC-061.txt`, `ancres-chronologiques.json` (`ANC-005`, `ANC-007`, `ANC-010`, `ANC-011`, `ANC-013`, `ANC-014`, `ANC-018..021`).
  - **Verdict : supporté**

- **C26-11 (`L37`)** — *Affirmation :* Requalification fournisseur d'une DSI selon l'`article 25(1)` lors d'une modification substantielle ou réaffectation d'un agent ou modèle `GPAI` sur un `ERP`, `SIRH` ou `MES` vers une finalité de l'`Annexe III`, emportant les devoirs des `articles 11, 16, 17, 43, 47–49, 72, 73`, `EXIG-CON-15` et accord écrit `article 25(4)` (`→ ch27`) `[1, 2]`.
  - **Appui vérifié :** `SRC-060.txt` (`L3930–3952`, `L4197–4232`), `SRC-061.txt` (`L1094`), `Tome 2` (`EXIG-CON-15`).
  - **Verdict : supporté**

- **C26-12 (`L39`)** — *Affirmation :* Obligations déployeur sous `article 26` (`EXIG-CON-16`) : supervision compétente dotée d'arrêt sûr (`article 14`), pertinence des entrées, journaux `≥ 6` mois (`art. 26(6)`, étendus à `24` mois par `EXIG-OBS-13`), information des travailleurs, `AIDF` (`art. 27` reliée à l'`AIPD` RGPD sous `(UE) 2026/1744`) et droit à explication (`article 86` hors point `2`) `[1, 2]`.
  - **Appui vérifié :** `SRC-060.txt`, `SRC-061.txt`, `Tome 2` (`EXIG-CON-16`, `EXIG-OBS-13`).
  - **Verdict : supporté**

- **C26-13 (`L41–L49`, Tableau 26.1)** — *Affirmation :* Le `Tableau 26.1` consolide `EU AI Act` `[1, 2]`, `EN 18286:2026` `[4, 5]`, `DORA` `[3]` & `NIS 2` (`ANC-006`, repérage `Tome 1`), `CRA` `(UE) 2024/2847` (cité `[2]`, `ANC-008`) & Directive `(UE) 2024/2853` (`ANC-002`), ainsi que `(UE) 2024/903`, `eIDAS 2.0`, `PSD2` et `Data Act` (`ANC-003`).
  - **Appui vérifié :** `SRC-060.txt`, `SRC-061.txt`, `SRC-062.txt`, `SRC-067.txt`, `SRC-069.txt`, `ancres-chronologiques.json` (`ANC-002..017`), `Tome 1`/`3`.
  - **Verdict : supporté**

- **C26-14 (`L51`, `L53`)** — *Affirmation :* Décision `(UE) 2026/2274` (`12 oct. 2026`) publiant `EN 18286:2026` sous l'article `40` `[4]`, communiqué DG CNECT (`21 oct. 2026`) `[5]`, `EXIG-CON-30` (`J2a` `1er nov. 2027`, `E1`–`E3` au `Tome 2 § 12.10`), et socle européen d'interopérabilité (`CRA` `SBOM` `[2]` `11 déc. 2027` `ANC-008`, `(UE) 2024/903` `12 janv. 2025` `EIF`, `eIDAS 2.0` `24 déc. 2026`, `PSD2`, `EDC`/`ODRL` + `Data Act`).
  - **Appui vérifié :** `SRC-067.txt` `[4]`, `SRC-069.txt` `[5]`, `SRC-061.txt` `[2]`, `Tome 1`, `Tome 2`, `ANC-008`.
  - **Verdict : supporté**

- **C26-15 (`L55`)** — *Affirmation :* Axe 1 (*Risque de modèle et IA*) de la triple qualification `[1, 3]` : `RIA` `[1]`, et repérage comparatif `Tome 1 § 30.2` opposant `PRA SS1/23` (`mai 2024`) et `BSIF E-23` (`← ch25`) à `US SR 26-2` / `OCC 2026-13` (`17 avril 2026`, excluant l'IA générative et agentique du risque de modèle).
  - **Appui vérifié :** `SRC-060.txt` `[1]`, `SRC-062.txt` `[3]`, `Tome 1 § 30.2.4`.
  - **Verdict : supporté**

- **C26-16 (`L57`, `L59`)** — *Affirmation :* Axe 2 (`NIS 2` `(UE) 2022/2555` réexamen `17 oct. 2027` `ANC-006` pour industrie/énergie/santé/transport/numérique ; étalon `DORA` `(UE) 2022/2554` depuis `17 janv. 2025`, registre tiers TIC, plans de sortie, `TLPT` `art. 24–26` `[3]`, `19` CTI `nov. 2025` `Tome 1 § 30.2.2`, propagation systémique transfrontalière démontrée par Bostan `[7]`) et Axe 3 (Directive `(UE) 2024/2853` `9 déc. 2026` `ANC-002` `Tome 3 § 36` ; `MiFID II` et `AMLR` `juill. 2027` sous réserve `Tome 1`).
  - **Appui vérifié :** `SRC-062.txt` `[3]`, `SRC-109.txt` `[7]`, `ancres-chronologiques.json` (`ANC-002`, `ANC-006`, `ANC-009`, `ANC-015`, `ANC-016`), `Tome 1`, `Tome 3`.
  - **Verdict : supporté**

- **C26-17 (`L61–L63`, Figure 94)** — *Affirmation :* `Figure 94` (`SCH-26-01.svg`) illustrant la triple qualification européenne d'un système d'entreprise automatisé (`EN 18286:2026`, `DORA`/`NIS 2`, `CRA`, `eIDAS 2.0`, `Digital Omnibus 2026/1744`).
  - **Appui vérifié :** `specs/manifest.json` (`ch26`, `SCH-26-01`), `schemas/SCH-26-01.svg`, `schemas/rendus/SCH-26-01.svg`.
  - **Verdict : supporté**

### Section 26.2.2 — Référentiels internationaux et souveraineté des substrats d'état (`L65–L107`, Tableau 26.2, Figures 95–96)

- **C26-18 (`L67`)** — *Affirmation :* `NIST AI RMF 1.0` (`NIST AI 100-1`, janv. 2023, `72` sous-catégories, réexamen au plus tard en `2028`), `NIST AI 600-1` (juill. 2024), `CAISI` (fév. 2026) et projets `COSIS` (`SP 800-53`) qualifiés comme repérage `Tome 2 § 12.5` hors textes `L+` ici.
  - **Appui vérifié :** `Tome 2 § 12.5`, `SRC-109.txt`.
  - **Verdict : supporté**

- **C26-19 (`L69`)** — *Affirmation :* Famille `ISO/IEC JTC 1/SC 42` (`ISO/IEC 42001:2023` `38` mesures, `42005:2025`, `22989:2022`, `23894:2023`, `FDIS 24970`, `DIS 42102–42105`) consignée en `statut F` (`iso.org` `HTTP 403`, `AO-01`), basculant la preuve ouverte sur `EN 18286:2026` `[4, 5]`.
  - **Appui vérifié :** `recherche/registre-statut-f.json`, `sources/ch26-sources.md`, `SRC-067.txt` `[4]`, `SRC-069.txt` `[5]`, `Tome 2`, `Tome 3`.
  - **Verdict : supporté**

- **C26-20 (`L71`)** — *Affirmation :* `IMDA Agentic AI v1.5` (juin 2026, `Tome 3 § 35.3`), principes `AICA`/`IAIS` (`Tome 4`) et feuille de route PQC du `G7 CEG` (`14 janvier 2026`, `2030–2035`, priorité `2030`–`2032`) `[6]` (`↔ ch18`).
  - **Appui vérifié :** `SRC-052.txt` `[6]`, `ancres-chronologiques.json` (`ANC-040`, `ANC-043`, `2030-2035-G7-PQC-FINANCE`), `Tome 3`, `Tome 4`.
  - **Verdict : supporté**

- **C26-21 (`L73–L81`, Tableau 26.2)** — *Affirmation :* Classe de risque par critère maximal unique sans moyenne compensatoire (`EXIG-CON-01..02`, `PRR G-03`), plafonds exclusifs (`Élevée ≤ N2`, `Modérée ≤ N3`, `Faible ≤ N3` ou `N4` sur comité, `NX` proscrit), réévaluation sur dérive (`EXIG-GOV-12`, `EXIG-CON-03`) et `Tableau 26.2` couvrant les déclencheurs multisectoriels (`SIRH`, infra critique, crédit, assurance vie/santé Ann. III `[1, 2]`, `SoR`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`G-03`), `Tome 2` (`Tableau 46`, `EXIG-CON-01..03`), `SRC-060.txt` `[1]`, `SRC-061.txt` `[2]`.
  - **Verdict : supporté**

- **C26-22 (`L83`)** — *Affirmation :* Tolérance annuelle au risque (`EXIG-CON-17`), évaluation d'impact unifiée (`EXIG-CON-26` : ÉFVP `← ch25`, AIDF `RIA art. 27` / AIPD `RGPD art. 35` `[1, 2]`, impact algorithmique, `ISO/IEC 42005` `Tome 2 § 12.9`) et index unique des preuves (`EXIG-CON-18`) `[1, 3, 4]`.
  - **Appui vérifié :** `SRC-060.txt` `[1]`, `SRC-061.txt` `[2]`, `SRC-062.txt` `[3]`, `SRC-067.txt` `[4]`, `Tome 2`.
  - **Verdict : supporté**

- **C26-23 (`L85–L91`)** — *Affirmation :* Riposte `S1`–`S4` en cinq temps (`EXIG-CON-23..25`) : Contenir (`EXIG-IAM-20`, `← ch21`), Préserver (`art. 73(6)` RIA `[1]`), Évaluer et aviser par cumul strict (`24 h` BSIF `← ch25`, `2`/`10`/`15 j` RIA `art. 73` `[1]`, `72 h` cible RGPD/CAI/LPRPDE `Tome 2 § 12.8`, veille `C-8`, registre `5` ans), Corriger et compenser sur `SoR`, Apprendre (`E1`–`E3`).
  - **Appui vérifié :** `SRC-060.txt` (`art. 73`) `[1]`, `Tome 2 § 12.8`.
  - **Verdict : supporté**

- **C26-24 (`L93–L95`, Figure 95)** — *Affirmation :* `Figure 95` (`SCH-26-02.png`) couplant régime nominal (`EXIG-CON-02`, `EN 18286:2026`, `EXIG-CON-18`) et boucle d'urgence `S1`–`S4`.
  - **Appui vérifié :** `specs/manifest.json` (`SCH-26-02`), `schemas/SCH-26-02.mmd`, `schemas/rendus/SCH-26-02.png`.
  - **Verdict : supporté**

- **C26-25 (`L97`)** — *Affirmation :* Repères de souveraineté (`Tome 3 § 37.1–37.2`, hors `L+` ici) : résidence vs contrôle juridictionnel sous `U.S. CLOUD Act` (`18 U.S.C. § 2713`), `Data Act` (`(UE) 2023/2854`, `art. 32`, sept. 2025), grille `SEAL-0..4`, `Gaia-X` niveau 3 auto-déclaratif, `SecNumCloud 3.2` (`12 août 2026` secondaire, `EUCS` bloqué) et `COM(2026) 502` (`3 juin 2026`).
  - **Appui vérifié :** `Tome 3 § 37.1–37.2`.
  - **Verdict : supporté**

- **C26-26 (`L99`, `L101`, `L105–L107`, Figure 96)** — *Affirmation :* Architecture cible `ADR-027` (« acceptée sous réserve », `PRR F-04..F-06`, `Tome 3 § 46.9–46.13`) couvrant les six substrats d'état reliant l'automatisation aux systèmes d'entreprise (`ERP`, `CRM`, `SIRH`, `MES`, `SoR`), protégés par `Classe-S2` (`C2`, `HMAC-FPE` sous `HSM HYOK`) et `Classe-S3` (`C3`, `CPU`/`GPU TEE` avec attestation distante `PCR`), visant `RTO < 15 min` et `RPO = 0` (`Figure 96`, `SCH-26-03.svg`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`ADR-027`, `F-04..F-06`), `Tome 3 § 46.9–46.13`, `schemas/rendus/SCH-26-03.svg`.
  - **Verdict : supporté**

- **C26-27 (`L103`)** — *Affirmation :* Arbitrage FinOps et latence sous `ADR-027` (`Tome 3 § 46.2–46.3, § 46.10`, `Tome 5 § 9.2`) : `Classe-S2 (HYOK)` sous contrat `ZDR` et cible `RTT ≤ 35 ms` en mode fermé (*fail-closed*) ; bascule vers `Classe-S3` (`CAP-033`, `SIG-016`) pour secrets industriels, dossiers cliniques, `BSIF E-23` élevé ou `RTT > 35 ms`, arbitrant la limite `DDR5` (`TEE.fail`, `< 1 000 $ US` `← ch21`) sans simulation `GPU TEE` locale en `G0` (`Tome 8`).
  - **Appui vérifié :** `Tome 3 § 46`, `Tome 5 § 9.2`, `matrice-exig-prr-c40.json` (`CAP-033`, `SIG-016`).
  - **Verdict : supporté**

### Section 26.3 — Synthèse architecturale, livrables et portes de contrôle (`L109–L130`, Tableau 26.3)

- **C26-28 (`L111`, `L113`)** — *Affirmation :* Interfaces amont (`ch05`, `08`, `09`, `17`, `21`, `22`, `23`, `24`, `25`) et aval (`ch27`, `28`, `31` `SIG-001/002/008`, `ch34` `305` exigences) ; synchronisation `G0` via `sandbox_confinement.rego`, `audit_scitt_focus.py` et `prr_validators.py` (`G-03`, `G-07`, `F-04`).
  - **Appui vérifié :** `specs/manifest.json`, `aq/rapports-g0.json`, `Tome 8/trousse/`.
  - **Verdict : supporté**

- **C26-29 (`L115–L122`, Tableau 26.3)** — *Affirmation :* Quatre livrables auditables et critères d'acceptation exécutables (`EXIG-CON-13..18, 26, 30`, `PRR G-03, G-07, G-08`, `EXIG-CON-01..03`, `EXIG-GOV-12`, `EXIG-CON-23..25`, `EXIG-IAM-20`, `SIG-001/002/008`, `ADR-027`, `F-04..F-06`, `G7 CEG` `[6]`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json`, `SRC-060.txt` `[1]`, `SRC-062.txt` `[3]`, `SRC-067.txt` `[4]`, `SRC-069.txt` `[5]`, `SRC-052.txt` `[6]`.
  - **Verdict : supporté**

- **C26-30 (`L124`)** — *Affirmation :* Transition vers le Chapitre 27 convertissant `art. 25(4)` RIA, `HYOK` et la sortie sans frais du *Data Act* en clauses contractuelles et bancs d'essai éliminatoires sur les suites `SaaS`, fournisseurs infonuagiques et partenaires `B2B`.
  - **Appui vérifié :** `SRC-060.txt` (`art. 25(4)`), `specs/manifest.json` (`ch26` → `ch27`).
  - **Verdict : supporté**

- **C26-31 (`L126–L130`)** — *Affirmation :* Trois invariants exécutables du Chapitre 26 : (1) qualification cumulative (`Modèle IA`, `DORA` ou `NIS 2` et `CRA` `[2, 3]`, `Produits et marché`) et preuve ouverte `EN 18286:2026` sans dépendance `ISO/IEC 42001` (`statut F`) `[1, 2, 3, 4, 5]` ; (2) plafonds par pire cas (`EXIG-CON-02`, `PRR G-03`) et riposte `S1`–`S4` sans destruction forensique ; (3) souveraineté matérielle sur six substrats d'état (`ADR-027`, `SEAL-0..4`, `F-04..F-06`, `Classe-S2 HYOK`, `Classe-S3 TEE`, `ZDR`, `RTO < 15 min` / `RPO = 0`).
  - **Appui vérifié :** `SRC-060.txt`..`SRC-069.txt` `[1..5]`, `matrice-exig-prr-c40.json`, `Tome 2`, `Tome 3`.
  - **Verdict : supporté**

- **C26-32 (`CA-07` — ancres chronologiques rattachées à `ch26`)** — *Affirmation :* Présence exacte et concordante des dates du registre `ancres-chronologiques.json` (`2 août 2026`, `2 décembre 2026`, `9 décembre 2026`, `12 octobre 2026`, `21 octobre 2026`, `14 janvier 2026`, `2 août 2027`, `2 septembre 2027`, `17 octobre 2027`, `2 décembre 2027`, `11 décembre 2027`, `17 janvier 2028`, `2 août 2028`, `2 août 2029`, `2 août 2030`, `2030–2035`).
  - **Appui vérifié :** `registre/ancres-chronologiques.json`, `outils/verifie_manuscrit.py` (`CA-07`).
  - **Verdict : supporté**

- **C26-33 (`CA-10` — bijection bibliographique Option A)** — *Affirmation :* Bijection stricte `100 %` entre les renvois `[1]`–`[7]` du corps narratif et `sources/ch26-sources.md` (`L1` alignée sur `manifest.json`, entrées `[1]`–`[7]` intactes).
  - **Appui vérifié :** `sources/ch26-sources.md`, `outils/verifie_manuscrit.py` (`CA-10`).
  - **Verdict : supporté**
