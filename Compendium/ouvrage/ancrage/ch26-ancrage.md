# Journal d'ancrage atomique Wyvern G2 — Chapitre 26 (`ch26`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/09 - Partie IX/Chapitre 26.md` (`4 513` mots de prose selon `verifie_manuscrit.py`, `4 726` mots selon `parser_plan.py`, plage `[4 251, 4 989]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch26-sources.md` (`[1]`–`[7]` en statut `L+`, `3` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-{052,060,061,062,067,069,109}.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-5`
- **Passe G2 initiale (supportés) :** 9
- **Rectifications appliquées lors de la passe G2 :** 22
- **Verdict final — supportés :** 31 / 31 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 26.md`

Toutes les formulations divergentes, sur-attribuées ou relevant du repérage antérieur hors corpus `L+` fermé de ce chapitre relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 26.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/09%20-%20Partie%20IX/Chapitre%2026.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant les `owned_concepts` (`eu-ai-act`, `systeme-qualite-en-18286-dora-cra`, `maillage-reglementaire-international`, `iso-iec-42001-nist`, `souverainete-espaces-donnees-tee-hyok`, `cadres-internationaux-imda-aica-g7`, `classes-risque-agents-et-plafonds`, `incidents-agentiques-et-notification-multiregime`), l'ensemble des renvois `[1]`–`[7]` et le calibrage (`4 513` / `4 726` mots dans `[4 251, 4 989]`) :

1. **Portes `PRR G-03` vs `PRR G-02` et `G-07`/`G-08` (`L13`, `L73`, `L112`, `L122`–`L123`) :** correction de l'alignement sur `registre/matrice-exig-prr-c40.json` (`prr_75` et `grille_unifiee_t5_annexe_c1` `A.2.3`) en remplaçant `PRR G-02` (qui vise l'inscription au SMIA `ISO/IEC 42001`) par `PRR G-03` (qualification réglementaire de l'empreinte de déploiement, porte `[BLOQUANT]` liée à `EXIG-CON-01..02`), et rattachement exact de `PRR G-07` à l'article `50` (`2 août 2026`) et de `PRR G-08` à l'Annexe III (`2 décembre 2027`) sans confusion avec l'Annexe I (`2 août 2028`).
2. **DORA `19` CTI, `CRA`, Directive `(UE) 2024/2853` et autres actes européens (`L15`–`L17`, `L45`–`L47`, `L53`, `L57`–`L59`, `L122`) :** retrait du faux renvoi `[3]` (`SRC-062.txt`, 2022) sur la désignation de novembre 2025 de `19` prestataires tiers critiques (rattachée au repérage historique `Tome 1 § 30.2.2`) ; rattachement du `CRA` `(UE) 2024/2847` à sa citation dans `[2]` (`SRC-061.txt`) et à l'ancre `ANC-008` (`11 décembre 2027`) ; retrait de `[1, 3]` et `[1, 7]` sur la Directive `(UE) 2024/2853` (`ANC-002`), `(UE) 2024/903`, `eIDAS 2.0` (`(UE) 2024/1183`), `PSD2`, `NIS 2` (`ANC-006`), `MiFID II`, `AMLR` (sous réserve documentaire `Tome 1`), `US SR 26-2` / `OCC 2026-13` et `UK PRA SS1/23`, qualifiés comme issus du repérage antérieur (`Tome 1` / `Tome 3 § 36`) hors base `L+` de ce chapitre ; recalage de l'apport de Bostan (`[7]`, `SRC-109.txt`) sur la propagation systémique des risques dans les chaînes numériques transfrontalières.
3. **Référentiels `NIST`, `ISO/IEC`, `IMDA`, `AICA`/`IAIS`, `G7 CEG` et délais d'incident (`L19`, `L67`–`L71`, `L83`–`L85`, `L111`–`L113`, `L123`) :** retrait du renvoi erroné `[6]` (`G7 CEG PQC`) de la riposte aux incidents `S1`–`S4`, en le réservant exclusivement à la feuille de route `G7 CEG` du `14 janvier 2026` ; qualification explicite de `NIST AI RMF 1.0`, `NIST AI 600-1`, `CAISI`, `COSIS`, `IMDA v1.5`, `AICA`/`IAIS` et de la famille payante `ISO/IEC JTC 1/SC 42` (`ISO/IEC 42001:2023` en `statut F`, `42005`, `22989`, `23894`, `FDIS 24970`, `DIS 42102–42105`) comme issus du repérage antérieur (`Tome 2`, `Tome 3`, `Tome 4`) hors `L+` fermé de ce chapitre ; renvoi vers `← Chapitre 25` et `Tome 2` pour `Loi 25`, `BSIF E-23`, `LPRPDE`, `RGPD art. 33–34` et la loi `C-8` (en veille `Tome 2 § 12.3`).
4. **Souveraineté matérielle, `SEAL`, `Data Act` et `ADR-027` (`L21`, `L91`–`L97`, `L107`, `L114`, `L124`) :** qualification explicite de `U.S. CLOUD Act`, `Data Act` (`art. 32`), `SEAL-0..4`, `Gaia-X` (niveau 3 auto-déclaratif), `SecNumCloud 3.2` et `COM(2026) 502` comme repérage `Tome 3 § 37` hors `L+` de ce chapitre ; qualification d'`ADR-027` (« acceptée sous réserve »), des `six couches d'état`, des boucliers `C2` (`HMAC-FPE`/`HYOK`) / `C3` (`CPU/GPU TEE`) et des cibles `RTO < 15 min` / `RPO = 0` comme choix et cibles de conception internes (`Tome 3 § 46`) sans invulnérabilité absolue ni valeur de réponse juridique ; ajout de `G-03`, `G-07` et `F-04` dans la trace de synchronisation `G0` (`prr_validators.py`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C26-01` à `C26-30`)

### Section introductive et Section 26.1 — Résumé exécutif (`L1–L21`)

- **C26-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice posant l'unification sous index probatoire unique et souveraineté matérielle vérifiable des obligations de l'Union européenne (`EU AI Act`, `Digital Omnibus`, `EN 18286:2026`, `DORA`, `CRA`) et des référentiels internationaux (`NIST AI RMF`, `IMDA v1.5`, `AICA`, `G7`) sans analogie mécanique avec le droit canadien.
  - **Appui vérifié :** `specs/manifest.json` (`ch26`, `D09`, `SUB_D09_02`, `owned_concepts`), `registre/mindmap-complet.json`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C26-02 (`L5`, `L7`)** — *Affirmation :* Cadrage de la deuxième section de `D09` au gel du `2 décembre 2026`, clause `non-avis` (`AO-05`), interdiction de transposition mécanique entre droit européen et droit canadien/québécois (`↔ ch25`), preuve primaire exclusivement `L+` `[1]`–`[7]`, et consignation en `statut F` (`AO-01`) d'`iso.org` (`HTTP 403`), `standards.cencenelec.eu` (`HTTP 500`) et `eur-lex.europa.eu` (`AWS WAF`), substitués par EUR-Lex Cellar et `EN 18286:2026` `[4, 5]`.
  - **Appui vérifié :** `sources/ch26-sources.md` (`L1–92`), `recherche/registre-statut-f.json` (`L29–38`, `L117–126`, `L216–225`), `SRC-067.txt`, `SRC-069.txt`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C26-03 (`L11`)** — *Affirmation :* Pilier 1 — Le Règlement `(UE) 2024/1689` (*EU AI Act* ou RIA) s'applique aux fournisseurs et déployeurs de pays tiers dès que les sorties sont utilisées dans l'Union (`article 2(1)`) ; interdictions de l'article `5` applicables depuis le `2 février 2025`, et règles `GPAI` depuis le `2 août 2025` (échéance au `2 août 2027` pour modèles préexistants) `[1]`.
  - **Appui vérifié :** `SRC-060.txt` (`L3039–3040` `art. 2(1)(c)`, `L7336–7337` `art. 113 a)-b)`, `L7241–7242` `art. 111 § 3`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C26-04 (`L13`)** — *Affirmation :* Transparence de l'article `50` applicable depuis le `2 août 2026` avec transition au `2 décembre 2026` pour le marquage des systèmes préexistants (`article 50 § 2`) et nouvelles interdictions (`article 5`, `b bis` et `b ter`) `[1, 2]` ; Règlement `(UE) 2026/1744` du `8 juillet 2026` (*Digital Omnibus*, publié le `24 juillet 2026`, en vigueur le `27 juillet 2026`) reportant l'Annexe III au `2 décembre 2027` (`PRR G-08`) et l'Annexe I au `2 août 2028`, cadencant `EXIG-CON-13..16`, `PRR G-03` et `PRR G-07` (`article 50`) `[2]`.
  - **Appui vérifié :** `SRC-060.txt` (`L5049–5078`, `L7334`), `SRC-061.txt` (`L2`, `L38`, `L984–1010`, `L1843–1856`, `L2069–2071`), `registre/matrice-exig-prr-c40.json` (`prr_75` : `G-03`, `G-07`, `G-08`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché exactement `G-07` à l'article `50` et `G-08` à l'Annexe III, ajouté `PRR G-03` et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C26-05 (`L15`, `L17`)** — *Affirmation :* Pilier 2 — Triple qualification simultanée `[1, 3]` : modèle décisionnel (`RIA` `[1]`, `US SR 26-2` d'avril 2026 excluant l'IA générative/agentique et `UK SS1/23` du repérage `Tome 1`) ; TIC critiques (`DORA` depuis le `17 janvier 2025` `[3]` et `CRA` `(UE) 2024/2847` cité en `[2]`, `11 décembre 2027`, `ANC-008`) ; marché et produits (`MiFID II`, `AMLR` juillet 2027 sous réserve `Tome 1`, Directive `(UE) 2024/2853` après `9 décembre 2026`, `ANC-002`, éclairés par Bostan `[7]`) ; et `SMQ` (`article 17`) couvert par `EN 18286:2026` (`(UE) 2026/2274` du `12 octobre 2026`, présomption `article 40`, `EXIG-CON-30`) remplaçant `ISO/IEC 42001:2023` (`statut F`) `[4, 5]`.
  - **Appui vérifié :** `SRC-060.txt` `[1]`, `SRC-061.txt` (`L391–424` `[2]`), `SRC-062.txt` (`L4290` `[3]`), `SRC-067.txt` (`L1–40` `[4]`), `SRC-069.txt` (`L1–10` `[5]`), `SRC-109.txt` (`[7]`), `ancres-chronologiques.json` (`ANC-002`, `ANC-008`), `Corpus/Tome 1` (`§ 30.2`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié les textes `L+` `[1..5, 7]` des repères antérieurs `Tome 1`/`3`, rattaché `CRA` à `[2]`/`ANC-008` et `2024/2853` à `ANC-002`, et scindé le paragraphe (`CA-05`) · **Verdict : supporté**

- **C26-06 (`L19`)** — *Affirmation :* Pilier 3 — Référentiels volontaires du repérage `Tome 2`/`3`/`4` (`NIST AI RMF 1.0`, `NIST AI 600-1`, `ISO/IEC 42005:2025`, `IMDA Agentic AI v1.5`, `AICA`/`IAIS`, hors `L+` ici), feuille de route PQC du `G7 CEG` (`14 janvier 2026` `[6]`), et trois contrôles internes (`EXIG-CON-02` plafonds `Élevée ≤ N2`, `Modérée ≤ N3`, `Faible ≤ N3`/`N4` comité ; `EXIG-CON-18` ; `EXIG-CON-26` ; riposte `S1`–`S4` cumulant `24 h` BSIF, `72 h` CAI/RGPD via `← ch25`/`Tome 2`, et `2/10/15 j` RIA `art. 73` `[1]`).
  - **Appui vérifié :** `SRC-052.txt` (`L6` `[6]`), `SRC-060.txt` (`L6154–6167` `[1]`), `Corpus/Tome 2` (`EXIG-CON-02`, `EXIG-CON-18`, `EXIG-CON-23..26`).
  - **Passe initiale :** écart rectifié · **Action :** retiré le renvoi hors portée `[6]` de la riposte `S1`–`S4` et qualifié les référentiels volontaires hors base `L+` de ce chapitre · **Verdict : supporté**

- **C26-07 (`L21`)** — *Affirmation :* Pilier 4 — Insuffisance de l'hébergement géographique face au `CLOUD Act` (repérage `Tome 3`) ; architecture cible `ADR-027` (`SEAL-0..4` repérage `Tome 3`, `F-04`..`F-06`) étendant par choix interne le géorepérage à six couches d'état (`HMAC-FPE` sous `HSM` `HYOK` en `C2` ; `CPU`/`GPU TEE` `AMD SEV-SNP`, `Intel TDX`, `NVIDIA H100` en `C3`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`adr_31_sort` `ADR-027`, `prr_75` `F-04..F-06`), `Corpus/Tome 3` (`§ 37.1`, `§ 46.9–46.13`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `CLOUD Act`, `SEAL-0..4`, `ADR-027` et les six couches comme repérage `Tome 3` et choix/cible de conception interne · **Verdict : supporté**

### Section 26.2.1 — Droit de l'Union européenne (`L25–L63`, Tableau 26.1, Figure 1)

- **C26-08 (`L27`)** — *Affirmation :* Portée extraterritoriale `article 2(1)` (sorties utilisées dans l'Union) et définition `article 3(1)` (système automatisé à divers degrés d'autonomie, pouvant s'adapter après déploiement et déduisant des entrées comment générer des sorties) `[1]` ; inscription à la fiche (`EXIG-CON-13`) et classement d'office **Élevée** (`EXIG-CON-01`) dans un domaine de l'Annexe III par choix interne écartant la dérogation de l'article `6(3)` `[1]`.
  - **Appui vérifié :** `SRC-060.txt` (`L3039–3040`, `L3108–3112`), `Corpus/Tome 2` (`EXIG-CON-01`, `EXIG-CON-13`, `Tableau 49`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté la capacité d'adaptation après déploiement à l'article `3(1)` et qualifié l'exclusion de l'article `6(3)` comme choix normatif du cadre · **Verdict : supporté**

- **C26-09 (`L29`, `L31`)** — *Affirmation :* Calendrier réorganisé sans moratoire par `(UE) 2026/1744` (`8 juill. 2026`, pub. `24 juill. 2026`, vigueur `27 juill. 2026`) : interdictions `article 5` dès le `2 février 2025` complétées le `2 décembre 2026` par les points `b bis` et `b ter` (`EXIG-CON-14`) ; `GPAI` dès le `2 août 2025` avec échéance `2 août 2027` (`art. 111 § 3`) ; transparence `article 50 §§ 1–3` depuis le `2 août 2026` avec transition `article 50 § 2` au `2 décembre 2026` (`ANC-001`), étendue par `EXIG-CON-19` et `EXIG-CON-20` `[1, 2]`.
  - **Appui vérifié :** `SRC-060.txt` (`L5049–5078`, `L7241–7242`, `L7334–7337`), `SRC-061.txt` (`L984–1010`, `L1843–1848`, `L2069–2071`), `ancres-chronologiques.json` (`ANC-001`), `Corpus/Tome 2` (`EXIG-CON-14`, `EXIG-CON-19`, `EXIG-CON-20`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C26-10 (`L33`, `L35`)** — *Affirmation :* Haut risque reporté au `2 décembre 2027` (`Annexe III`, `ANC-007`) et au `2 août 2028` (`Annexe I`, `ANC-010`) ; bac à sable national au `2 août 2027` ; orientations `art. 72 § 3` au `2 septembre 2027` ; délais préexistants autorités publiques (`2 août 2030`, `art. 111 § 2`) et `Annexe X` (`fin 2030`, `art. 111 § 1`) ; réexamens quadriennaux à partir du `2 août 2028` et du `2 août 2029`, s'échelonnant de `2028` à `2033` (`art. 112 §§ 2–3`) ; `Annexe III` points `5(b)` (crédit/solvabilité, fraude financière exclue) et `5(c)` (assurance-vie/maladie, dommages exclus) `[1, 2]`.
  - **Appui vérifié :** `SRC-060.txt` (`L7226–7239`, `L7258–7271`, `L7515–7518`), `SRC-061.txt` (`L1248`, `L1402–1407`, `L1838`, `L1850–1854`), `ancres-chronologiques.json` (`ANC-007`, `ANC-010`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la référence exacte aux réexamens de l'article `112 §§ 2–3` à partir du `2 août 2028` et du `2 août 2029` · **Verdict : supporté**

- **C26-11 (`L37`)** — *Affirmation :* Requalification fournisseur selon l'`article 25(1)` (marque, modification substantielle, réaffectation d'un agent ou `GPAI` vers `Annexe III`), emportant les obligations des `articles 11, 16, 17, 43, 47–49, 72, 73`, `EXIG-CON-15` et accord écrit `article 25(4)` (`→ ch27`) `[1, 2]`.
  - **Appui vérifié :** `SRC-060.txt` (`L3930–3952`, `L4197–4232`), `SRC-061.txt` (`L1094`), `Corpus/Tome 2` (`EXIG-CON-15`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C26-12 (`L39`)** — *Affirmation :* Obligations déployeur sous `article 26` (`EXIG-CON-16`) : supervision compétente, consciente du biais d'automatisation et dotée d'interruption vers un état sûr (`article 14`), pertinence des entrées, journaux `≥ 6` mois (`article 26(6)`, étendus à `24` mois par `EXIG-OBS-13`), information des travailleurs (`article 26(7)`), `AIDF` (`article 27` relié à l'`AIPD` `art. 35` RGPD sous `(UE) 2026/1744`), et droit à explication (`article 86`) pour l'Annexe III hors point `2`, notamment en crédit et en assurance `[1, 2]`.
  - **Appui vérifié :** `SRC-060.txt` (`L3842–3880`, `L4242–4290`, `L4342–4382`, `L6638–6646`), `SRC-061.txt` (`L1095–1103`), `Corpus/Tome 2` (`EXIG-CON-16`, `EXIG-OBS-13`).
  - **Passe initiale :** écart rectifié · **Action :** précisé la modification `art. 27(4)` sous `(UE) 2026/1744` et l'étendue exacte de l'article `86` (Annexe III hors point `2`, notamment crédit et assurance) · **Verdict : supporté**

- **C26-13 (`L41–L49`, Tableau 26.1)** — *Affirmation :* Tableau 26.1 consolidant le `RIA` `[1, 2]`, `EN 18286:2026` `[4, 5]`, `DORA` `[3]` (et `19` CTI `nov. 2025` du repérage `Tome 1`), `CRA` `(UE) 2024/2847` (cité `[2]`, `ANC-008`) & Directive `(UE) 2024/2853` (`ANC-002`, repérage `Tome 1`/`3`), ainsi que `(UE) 2024/903`, `eIDAS 2.0`, `PSD2` et `NIS 2` (repérage `Tome 1` & `ANC-006`).
  - **Appui vérifié :** `SRC-060.txt` `[1]`, `SRC-061.txt` `[2]`, `SRC-062.txt` `[3]`, `SRC-067.txt` `[4]`, `SRC-069.txt` `[5]`, `ancres-chronologiques.json` (`ANC-002`, `ANC-006`, `ANC-008`), `Corpus/Tome 1`.
  - **Passe initiale :** écart rectifié · **Action :** retiré les faux renvois `[3]` sur les `19` CTI de `nov. 2025` et `[1, 3]` sur `CRA`/`2024/2853`/`2024/903`/`eIDAS`/`PSD2`/`NIS 2`, remplacés par l'attribution exacte (`[2]`, ancres et repérage `Tome 1`/`3`) · **Verdict : supporté**

- **C26-14 (`L51`, `L53`)** — *Affirmation :* Décision `(UE) 2026/2274` (`12 oct. 2026`) publiant `EN 18286:2026` pour présomption de conformité `article 40` `[4]` ; communiqué DG CNECT (`21 oct. 2026`) sur l'articulation avec `article 17` et les SMQ sectoriels `[5]` ; `EXIG-CON-30` (`J2a` `1er nov. 2027`, traçabilité versions, `E1`–`E3` selon `Tome 2 § 12.10`) ; compléments du repérage `Tome 1` et ancres (`CRA` `[2]` `11 déc. 2027` `ANC-008`, `2024/903` `12 janv. 2025`, `eIDAS 2.0` `24 déc. 2026` `← ch17`, `PSD2` `← ch22`).
  - **Appui vérifié :** `SRC-067.txt` (`L15–82` `[4]`), `SRC-069.txt` (`L1–11` `[5]`), `SRC-061.txt` (`L391–424` `[2]`), `Corpus/Tome 2` (`L6157–6163`), `Corpus/Tome 1` (`L282`, `L835`), `ancres-chronologiques.json` (`ANC-008`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché `J2a`/`E1`–`E3` au référentiel interne `Tome 2 § 12.10` et attribué les actes complémentaires au repérage `Tome 1`, à `[2]` et à `ANC-008` · **Verdict : supporté**

- **C26-15 (`L55`)** — *Affirmation :* Axe 1 (*Risque de modèle*) de la triple qualification `[1, 3]` : selon le repérage comparatif `Tome 1 § 30.2` (hors `L+` de ce chapitre), `PRA SS1/23` au Royaume-Uni (`mai 2024`, `5` principes) et `BSIF E-23` au Canada (`← ch25`) couvrent l'IA, tandis que `US SR 26-2` / `OCC 2026-13` (`17 avril 2026`) exclut l'IA générative et agentique du risque de modèle tout en maintenant le crédit équitable.
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 30.2.4`, `L6926–6938`), `SRC-060.txt` `[1]`, `SRC-062.txt` `[3]`.
  - **Passe initiale :** écart rectifié · **Action :** qualifié `PRA SS1/23` et `US SR 26-2` / `OCC 2026-13` comme issus du repérage comparatif `Tome 1 § 30.2` hors `L+` fermé de ce chapitre, et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C26-16 (`L57`, `L59`)** — *Affirmation :* Axe 2 (`DORA` `(UE) 2022/2554` depuis `17 janv. 2025`, registre des tiers TIC, plans de sortie, `TLPT` `art. 24–26` `[3]` ; désignation `nov. 2025` de `19` CTI au repérage `Tome 1 § 30.2.2`, propagation systémique transfrontalière éclairée par Bostan `[7]`) et Axe 3 (`MiFID II`, `AMLR` `juill. 2027` sous réserve `Tome 1` / `AMLA`, Directive `(UE) 2024/2853` `9 déc. 2026` `ANC-002` `Tome 3 § 36`).
  - **Appui vérifié :** `SRC-062.txt` (`L2499–2560`, `L4290` `[3]`), `SRC-109.txt` (`L16–36`, `L107–125` `[7]`), `Corpus/Tome 1` (`§ 30.2.2` `L6908`, `§ 30.2.5–30.2.6` `L6946–6954`), `Corpus/Tome 3` (`L19390`), `ancres-chronologiques.json` (`ANC-002`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié `DORA` `[3]` du repérage `Tome 1` sur les `19` CTI, recalé l'apport de `[7]`, qualifié `MiFID II`/`AMLR`/`2024/2853` hors `L+` ici, retiré `[1, 7]` sur `2024/2853`, et scindé en deux paragraphes (`CA-05`) · **Verdict : supporté**

- **C26-17 (`L61–L63`, Figure 1)** — *Affirmation :* Figure 1 (`SCH-26-01.svg`) matérialisant la triple qualification croisée avec le *Digital Omnibus* `(UE) 2026/1744` et le socle ouvert `EN 18286:2026`.
  - **Appui vérifié :** `specs/manifest.json` (`ch26`, `SCH-26-01`), `schemas/SCH-26-01.svg`, `schemas/rendus/SCH-26-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 26.2.2 — Référentiels internationaux et souveraineté cognitive (`L65–L101`, Tableau 26.2, Figures 2–3)

- **C26-18 (`L67`)** — *Affirmation :* Cadres américains issus du repérage `Tome 2 § 12.5` (hors textes intégraux `L+` dans ce chapitre) : `NIST AI RMF 1.0` (`NIST AI 100-1`, janv. 2023, `72` sous-catégories, examen au plus tard en `2028`), `NIST AI 600-1` (juill. 2024 ; `GOVERN 6.1–6.2`, `MAP 3.5`, `MEASURE 2.4, 2.7, 3.1`, `MANAGE 2.4`, `GOVERN 1.7`), `CAISI` (fév. 2026) et projets `COSIS` (`SP 800-53`).
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 12.5`, `L5923–5941`), `SRC-054.txt` (`L4266–4272`, mention secondaire de `AI 100-1`/`600-1`), `SRC-109.txt` (`L151`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement ces cadres NIST/CAISI/COSIS comme issus du repérage normatif antérieur `Tome 2 § 12.5` hors textes intégraux `L+` dans ce chapitre · **Verdict : supporté**

- **C26-19 (`L69`)** — *Affirmation :* Famille `ISO/IEC JTC 1/SC 42` au repérage `Tome 2 § 12.5` / `Tome 3 § 35` (`ISO/IEC 42001:2023` `38` mesures annexe A, `42005:2025`, `22989:2022`, `23894:2023`, `FDIS 24970`, `DIS 42102–42105`) ; normes payantes d'`iso.org` demeurant en `statut F` (`AO-01`, `HTTP 403`) sans texte intégral ouvert en `L+`, basculant l'ancrage probatoire ouvert sur `EN 18286:2026` `[4, 5]`.
  - **Appui vérifié :** `recherche/registre-statut-f.json` (`L216–225`), `sources/ch26-sources.md` (`L90`), `SRC-067.txt` `[4]`, `SRC-069.txt` `[5]`, `Corpus/Tome 2` (`L5935–5937`), `Corpus/Tome 3` (`L19379`).
  - **Passe initiale :** écart rectifié · **Action :** étendu l'explication `statut F` / repérage `Tome 2`/`3` à l'ensemble de la famille payante `ISO/IEC` · **Verdict : supporté**

- **C26-20 (`L71`)** — *Affirmation :* `IMDA Agentic AI v1.5` (juin 2026, repérage `Tome 3 § 35.3` hors base `L+` ici), principes `AICA`/`IAIS` (repérage `Tome 4`) et feuille de route post-quantique du `G7 CEG` (`14 janvier 2026`, `2030–2035`, priorité critique `2030–2032`) `[6]` (`↔ ch18`).
  - **Appui vérifié :** `SRC-052.txt` (`L6`, `L189–198`, `L216–218` `[6]`), `ancres-chronologiques.json` (`2030-2035-G7-PQC-FINANCE`), `Corpus/Tome 3` (`§ 35.3`, `L19210–19235`), `Corpus/Tome 4` (`L572`, `L3492`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `IMDA v1.5` et `AICA`/`IAIS` comme issus du repérage antérieur des tomes hors base `L+` de ce chapitre, en réservant `[6]` au `G7 CEG` · **Verdict : supporté**

- **C26-21 (`L73`, `L75–L81`, Tableau 26.2)** — *Affirmation :* Attribution de classe de risque par critère maximal unique sans moyenne compensatoire (`EXIG-CON-01`, `EXIG-CON-02`, `PRR G-03`), plafonds exclusifs (`Élevée ≤ N2`, `Modérée ≤ N3`, `Faible ≤ N3` ou `N4` sur comité, `NX` proscrit), réévaluation sur dérive (`EXIG-GOV-12`, `EXIG-CON-03`), et synthèse au `Tableau 26.2` (`Annexe III` `[1, 2]`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`prr_75` `G-03`, `grille_unifiee_t5_annexe_c1` `A.2.3`), `Corpus/Tome 2` (`Tableau 46`, `EXIG-CON-01..03`, `L5633–5668`), `SRC-060.txt` `[1]`, `SRC-061.txt` `[2]`.
  - **Passe initiale :** écart rectifié · **Action :** corrigé `PRR G-02` → `PRR G-03` conformément au registre SSOT `matrice-exig-prr-c40.json` · **Verdict : supporté**

- **C26-22 (`L83`)** — *Affirmation :* Déclaration annuelle de tolérance au risque (`EXIG-CON-17`), évaluation d'impact unifiée (`EXIG-CON-26` : ÉFVP `Loi 25` `← ch25`, AIDF `RIA art. 27` / AIPD `RGPD art. 35` `[1, 2]`, impact algorithmique, `ISO/IEC 42005` `Tome 2 § 12.9`), et index unique des preuves (`EXIG-CON-18` reliant `EXIG-*`, `NIST AI RMF` `Tome 2 § 12.5`, `EN 18286:2026` `[4]`, `Loi 25`/`BSIF E-23` `← ch25` et `DORA` `[3]`).
  - **Appui vérifié :** `SRC-060.txt` (`L4299`, `L4379` `[1]`), `SRC-061.txt` (`L1098–1103` `[2]`), `SRC-062.txt` `[3]`, `SRC-067.txt` `[4]`, `Corpus/Tome 2` (`EXIG-CON-17..18`, `EXIG-CON-26`, `Tableau 50`, `Tableau 52`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement `Loi 25`/`BSIF E-23` au `← ch25` et `NIST`/`ISO 42005` au `Tome 2` · **Verdict : supporté**

- **C26-23 (`L85`)** — *Affirmation :* Riposte aux incidents `S1`–`S4` en cinq temps (`EXIG-CON-23..25`) : (1) Contenir (`EXIG-IAM-20`, `→ ch21`, canal de compensation ouvert, bacs conservés) ; (2) Préserver (`art. 73(6)` RIA `[1]`) ; (3) Évaluer et aviser par cumul strict (`24 h` BSIF, `2/10/15 j` RIA `art. 73` `[1]`, `72 h` cible CAI et plafond RGPD `art. 33–34`, Loi 25, LPRPDE via `← ch25`/`Tome 2 § 12.8`, loi `C-8` en veille `Tome 2 § 12.3`, registre `5 ans`) ; (4) Corriger et compenser ; (5) Apprendre (`E1`–`E3`).
  - **Appui vérifié :** `SRC-060.txt` (`L6154–6178` `art. 73(2)–(6)` `[1]`), `Corpus/Tome 2` (`Tableau 51`, `EXIG-CON-23..25`, `L5826`, `L6053–6098`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché les délais canadiens/québécois et `RGPD` au `← ch25` et `Tome 2 § 12.8` (et `C-8` à la veille `Tome 2 § 12.3`), et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C26-24 (`L87–L89`, Figure 2)** — *Affirmation :* Figure 2 (`SCH-26-02.png`) couplant régime nominal (`EXIG-CON-02`, `EN 18286:2026`, `EXIG-CON-18`) et boucle d'urgence `S1`–`S4` en 5 temps.
  - **Appui vérifié :** `specs/manifest.json` (`ch26`, `SCH-26-02`), `schemas/SCH-26-02.mmd`, `schemas/rendus/SCH-26-02.png`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C26-25 (`L91`, `L93`)** — *Affirmation :* Repères de souveraineté du `Tome 3 § 37` (hors corpus `L+` fermé de ce chapitre) : distinction résidence vs contrôle juridictionnel sous `U.S. CLOUD Act` (`18 U.S.C. § 2713`) et `Data Act` (`(UE) 2023/2854`, `article 32`, sept. 2025) ; grille `SEAL-0..4` ; labels `Gaia-X` (niveau 3 encore auto-déclaratif) ; `SecNumCloud 3.2` (arrêté `12 août 2026` rapporté par commentaires secondaires, `EUCS` bloqué) ; proposition non adoptée `COM(2026) 502` (`3 juin 2026`).
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 37.1–37.2`, `L19615–19668`, `L19744–19773`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié l'ensemble de ces instruments comme issus du repérage `Tome 3 § 37` hors `L+` fermé ici et rappelé le statut déclaratif de `Gaia-X` niveau 3 et secondaire de `SecNumCloud` · **Verdict : supporté**

- **C26-26 (`L95`, `L97`, `L98–L100`, Figure 3)** — *Affirmation :* Architecture cible `ADR-027` (statut « acceptée sous réserve », `PRR F-04..F-06`, `Tome 3 § 46.9–46.13`) : géorepérage sur six couches d'état ; boucliers `C2` (`HMAC-FPE`/`FF1` sous `HSM HYOK`) et `C3` (`CPU/GPU TEE` `AMD SEV-SNP`, `Intel TDX`, `NVIDIA H100/B200`, `PCIe` chiffré `SPDM`/`CMA`, libération sur registres `PCR`) élevant le coût d'interception sans invulnérabilité absolue ni valeur juridique, avec bascule visant les cibles internes `RTO < 15 min` et `RPO = 0` (`SCH-26-03.svg`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`adr_31_sort` `ADR-027`, `prr_75` `F-04..F-06`), `Corpus/Tome 3` (`L24272–24499`), `schemas/SCH-26-03.puml`, `schemas/rendus/SCH-26-03.svg`.
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement `ADR-027`, les 6 substrats et `RTO < 15 min` / `RPO = 0` comme choix et cibles de conception internes (`Tome 3 § 46`) et explicité les limites de garantie du `TEE` · **Verdict : supporté**

- **C26-31 (`L98–L99`, § 26.2.3 — ajout post-G4 et raccord G5)** — *Affirmation :* Sous `ADR-027` (`Tome 3 § 46.2–46.3, § 46.5, § 46.10`, `Tome 5 § 9.2`, hors socle `L+`), la bascule **FinOps et latence** entre `C2 (HYOK)` (`ZDR`, révocation cryptographique, cible `RTT ≤ 35 ms` repérée d'`AWS XKS`) et `C3 (TEE)` (`CAP-033`, signal `SIG-016`, limite `DDR5` `TEE.fail` `< 1 000 \$ US` `← ch21`) échoue en mode fermé (*fail-closed*) si le gestionnaire `HSM` devient injoignable ou dépasse `> 35 ms` (suspendant l'accès aux données protégées avant bascule vers `C3`), et bascule vers `C3` dès que les données ne sont pas pseudonymisables, relèvent de `BSIF E-23` élevé ou excèdent durablement `RTT ≤ 35 ms` ; la vérification distante des `PCR` confronte les empreintes signées (microcode, noyau, `vLLM`/`SGLang`, poids) sur cible homologuée sans simulation `GPU TEE` en tests automatisés `G0`.
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 46.2–46.3, § 46.5, § 46.10`, `L23948–23991`, `L24264`), `Corpus/Tome 5` (`§ 9.2`, `L1352`), `registre/matrice-exig-prr-c40.json` (`CAP-033`, `SIG-016`).
  - **Passe initiale :** ajout post-G4 · **Action :** vérification différentielle `G2` et raccord `G5` (`fail-closed` sur `HSM` injoignable ou `> 35 ms`) · **Verdict : supporté**

### Section 26.3 — Synthèse architecturale, livrables et portes de contrôle (`L103–L124`)

- **C26-27 (`L105`, `L107`)** — *Affirmation :* Interfaces amont (`ch05`, `08`, `09`, `17`, `21`, `22`, `23`, `24`, `25`) et aval (`ch27`, `28`, `31` `SIG-001/002/008`, `ch34` `305` exigences) ; validation `G0` via `sandbox_confinement.rego`, `audit_scitt_focus.py` et `prr_validators.py` (incluant `G-03`, `G-07`, `F-04`) tout en documentant l'absence de simulation matérielle `GPU TEE` réelle dans les tests automatisés locaux.
  - **Appui vérifié :** `specs/manifest.json`, `registre/matrice-exig-prr-c40.json` (`dapp_sig_27`, `exig_cre_ia_v1_2`, `mappings` `G-03`, `G-07`, `F-04`), `Tomes/Tome 8/.../evalops_prr/prr_validators.py` (`L12–37`), `policies_opa/sandbox_confinement.rego`, `authz_pqc_audit/audit_scitt_focus.py`, `aq/rapports-g0.json`.
  - **Passe initiale :** écart rectifié · **Action :** précisé les identifiants vérifiés (`G-03`, `G-07`, `F-04`) dans `prr_validators.py` · **Verdict : supporté**

- **C26-28 (`L109–L116`, Tableau 26.3)** — *Affirmation :* Quatre livrables obligatoires et critères d'acceptation exécutables (`EXIG-CON-13..18, 26, 30`, `PRR G-03, G-07, G-08`, `EXIG-CON-01..03`, `EXIG-GOV-12`, `EXIG-CON-23..25`, `EXIG-IAM-20`, `SIG-001/002/008`, `ADR-027`, `F-04..F-06`, `G7 CEG` `[6]`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json`, `SRC-060.txt` `[1]`, `SRC-062.txt` `[3]`, `SRC-067.txt` `[4]`, `SRC-069.txt` `[5]`, `SRC-052.txt` `[6]`, `Corpus/Tome 2`, `Corpus/Tome 3`.
  - **Passe initiale :** écart rectifié · **Action :** corrigé `PRR G-02` → `PRR G-03`, qualifié les sources `Tome 2`/`Tome 3`/`← ch25` dans la colonne exécutable et retiré `[3]` des alertes `24 h`/`72 h` · **Verdict : supporté**

- **C26-29 (`L118`)** — *Affirmation :* Transition vers le Chapitre 27 convertissant les obligations de fond (`art. 25(4)` RIA, `HYOK`, sortie sans frais *Data Act*) en clauses contractuelles et bancs d'essai éliminatoires.
  - **Appui vérifié :** `SRC-060.txt` (`L4227–4232` `art. 25(4)`), `specs/manifest.json` (`ch26` → `ch27`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C26-30 (`L120–L124`)** — *Affirmation :* Trois invariants exécutables du Chapitre 26 : (1) triple qualification et ancrage `EN 18286:2026` (`EXIG-CON-13..18`, `EXIG-CON-30`, `PRR G-03`, `G-07`, `G-08`) sans dépendance `ISO/IEC 42001` (`statut F`) `[1, 2, 3, 4, 5]` ; (2) plafonds par pire cas et riposte `S1`–`S4` sans destruction forensique (`EXIG-CON-02`, `EXIG-CON-23..25`, `PRR G-03`) avec cumul `24 h` (`← ch25`), `2/10/15 j` (`[1]`) et `72 h` (`Tome 2`) ; (3) souveraineté matérielle cible sur six substrats (`ADR-027`, `SEAL-0..4`, `F-04..F-06`, `C2 HYOK`, `C3 CPU/GPU TEE`, `ZDR`, `RTO < 15 min` / `RPO = 0`).
  - **Appui vérifié :** `SRC-060.txt` `[1]`, `SRC-061.txt` `[2]`, `SRC-062.txt` `[3]`, `SRC-067.txt` `[4]`, `SRC-069.txt` `[5]`, `registre/matrice-exig-prr-c40.json`, `Corpus/Tome 2`, `Corpus/Tome 3`.
  - **Passe initiale :** écart rectifié · **Action :** corrigé `PRR G-02` → `PRR G-03`, qualifié les éléments `Tome 1`/`Tome 2`/`Tome 3`/`← ch25` et les cibles internes, et scindé les phrases (`CA-05`) · **Verdict : supporté**

- **C26-32 (`REV-04`, `PRD-L3-018/019/020`, `PRD-L4-002`)** — *Affirmation :* Reclassement de `SMQ EN 18286:2026` en Colonne 1 (`Z1`) et nuance `US SR 26-2 (hors IA gén./ag.)` dans `SCH-26-01.svg` ; enrichissement de `SCH-26-02.mmd` (`AICA`, `G7 CEG`, `EXIG-CON-17/26`) et `SCH-26-03.puml` (`RTT ≤ 35 ms`, `limite TEE.fail`) ; mise en liste numérotée de la riposte `S1`–`S4` en cinq temps, articulation avec `EXIG-CON-21`/`22` (`← ch25`), nettoyage de `\$` dans backticks (`< 1 000 $ US`) et numérotation `Figure 82`..`Figure 84`.
  - **Appui vérifié :** `schemas/SCH-26-01.svg`, `schemas/SCH-26-02.mmd`, `schemas/SCH-26-03.puml`, `SRC-060.txt`, `SRC-067.txt`, `Compendium/prd.md` (`L4978–4998`).
  - **Passe REV-04 :** intégré et vérifié · **Verdict : supporté**
