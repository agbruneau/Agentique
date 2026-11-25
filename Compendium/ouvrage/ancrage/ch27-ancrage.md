# Journal d'ancrage atomique Wyvern G2 — Chapitre 27 (`ch27`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/09 - Partie IX/Chapitre 27.md` (`4 010` mots de prose selon `verifie_manuscrit.py`, `4 273` mots selon `parser_plan.py`, plage `[3 726, 4 374]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch27-sources.md` (`[1]`–`[6]` en statut `L+`, `2` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json` et `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/tests/test_third_party_vectors.py`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-6`
- **Passe G2 initiale (supportés)** : 6
- **Rectifications appliquées lors de la passe G2 :** 26
- **Verdict final — supportés :** 32 / 32 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 27.md`

Toutes les formulations divergentes, sur-attribuées à des renvois `[n]` ou issues du repérage antérieur hors socle `L+` fermé relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 27.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/09%20-%20Partie%20IX/Chapitre%2027.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant les cinq `owned_concepts`, les renvois `[1]`–`[6]`, les trois figures `SCH-27-01`..`03`, les trois tableaux et le calibrage (`4 010` / `4 273` mots dans `[3 726, 4 374]`) :

1. **Réattribution stricte des renvois `[1]`–`[6]` (`L7`, `L11`–`L15`, `L21`, `L28`–`L39`, `L51`–`L59`, `Tableau 27.2`, `L82`–`L84`, `Tableau 27.3`, `L120`–`L122`) :** retrait des renvois hors portée vers `[2]` (`SRC-068` `BSIF B-10`) sur les exigences purement internes (`EXIG-APP-04`, `Tableau 54`, `RFC 8693`, `CAEP`, `EXIG-IAM-20`, préavis `90` j, révocation `NHI` `24` h), vers `[4]` (`SRC-060` `EU AI Act`) sur la réversibilité pilote, les assurances, `AB-316`, *Moffatt c. Air Canada* et la Directive `(UE) 2024/2853`, et vers `[5, 6]` sur la fenêtre `12` mois de `POR-016` ; ancrage exact de `[5]` (`SRC-070`, art. 239 de la *Loi sur les banques* sur les livres au Canada) et de `[6]` (`SRC-114`, ouverture bancaire et sécurité des accès au Canada).
2. **Correction de l'incohérence `Performance mesurée` (`L30`) et de l'attribution `PRR G-14` (`L15`, `L94`–`L99`, `Tableau 27.3`, `L122`) :** alignement de `L30` sur `Tome 2 § 13.4` (`Tableau 54`) en excluant `Performance mesurée` (`5 %`) des critères éliminatoires malgré son essai reproductible `EXIG-APP-04` ; réaffectation de `PRR G-14` depuis les exclusions d'assurance vers les garde-fous anti-collusion algorithmique conformément à `registre/matrice-exig-prr-c40.json` ; qualification de `PRR O-15` comme protocole de décommissionnement rattaché à la rubrique `A.8.6`.
3. **Séparation des lois `L+`, cibles du cadre et repérage doctrinal (`L5`, `L13`–`L15`, `L53`–`L59`, `L82`–`L95`, `L105`) :** distinction entre l'article `18.3` de la Loi 25 (`[1]`, limitation au mandat et non-conservation) et son extension contractuelle `EXIG-APP-10` proscrivant l'entraînement ; qualification des délais cibles du cadre (`10` j, `90` j, `24` h / `4` h, `6` mois, `12` mois, `24` h `NHI`) ; rattachement du *Data Act* (`12 janvier 2027`) à `ANC-003` et des éléments `AAIF`, `Tableau 53`, `AB-316`, *Moffatt* (`statut F`), `(UE) 2024/2853` (`ANC-002`), `LCCJTI`/`LUCE`/`CNUDCI-2024` et `CG 40 47`/`40 48`/`35 08` (`statut F`) au repérage antérieur des *Tomes 2 et 3* ; précision de l'exécution `G0` des `5` fichiers `a2a_tck` dans `test_third_party_vectors.py` (`[3]`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C27-01` à `C27-32`)

### Section introductive — Titre, question directrice et cadrage (`L1–L7`)

- **C27-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice posant la traduction de la neutralité protocolaire et des obligations multi-juridictions en critères éliminatoires d'appel d'offres, en dix clauses non dérogeables et en garde-fous sur le mandat `B2B`.
  - **Appui vérifié :** `Compendium/ouvrage/specs/manifest.json` (`ch27`, `D09`, `SUB_D09_03`, `owned_concepts`), `registre/matrice-exig-prr-c40.json` (`CAP-051`, `EXIG-APP-01..17`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C27-02 (`L5`)** — *Affirmation :* Sans clauses contraignantes, les stipulations privées rétabliraient opacité, réentraînement et captivité ; selon le repérage du cadre (*Tome 2*, 27 octobre 2026, hors socle `L+`), le transfert de `MCP` et d'`A2A` vers `AAIF` déplace le verrouillage vers extensions propriétaires, couverture partielle, plafonds d'orchestration, identités fermées et crédits propriétaires.
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 13.1`, `L6279–6293`, `Tableau 53`), `Corpus/Tome 3` (`ADR-004`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement le transfert `AAIF` et les cinq foyers de verrouillage comme constats du repérage *Tome 2* (27 octobre 2026) hors socle `L+` fermé · **Verdict : supporté**

- **C27-03 (`L7`)** — *Affirmation :* Clôture de `D09` au gel du `2 décembre 2026` sous clause `non-avis` (`AO-05`) ; appuis légaux et techniques `L+` `[1]`–`[6]` et registres consolidés distincts des règles internes (`CRE-IA-2026-01`), avec exclusions `statut F` (`iso.org` pour `ISO/IEC 42001`, `legisquebec.gouv.qc.ca`, formulaires *ISO/Verisk* et décisions non ouvertes).
  - **Appui vérifié :** `sources/ch27-sources.md` (`L1–80`), `registre/glossaire-termes.json` (`Clause non-avis`, `Statut F`), `specs/protocole-mlr-compendium.json` (`AO-01`, `AO-05`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé l'amalgame entre l'exclusion `iso.org` (`ISO/IEC 42001` en `ch27-sources.md`) et les formulaires assurantiels *ISO/Verisk*, et séparé les sources `L+` `[1]`–`[6]` des règles internes du cadre · **Verdict : supporté**

### Section 27.1 — Résumé exécutif (`L9–L15`)

- **C27-04 (`L11`)** — *Affirmation :* Premier verrou (`CAP-051`, `INI-014`, `POR-004`, `POR-016`) : rejet des allégations non mesurées (`EXIG-APP-04`) en appui à la diligence tiers `[2]`, qualification sur le `Tableau 54` (`7` critères éliminatoires sur `8`, refus `DOIT` bloquant pour `EXIG-APP-01..06`, `17`, complétées par `PRR O-15` en `A.8.6`) et consignation des lacunes `a2a-tck 1.0.0.alpha3` (`CARD-SIGN-001`..`004` `NOT_AUTOMATABLE`, sans `a2a-jcs-v01` `[3]`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`CAP-051`, `INI-014`, `POR-004`, `POR-016`, `PRR O-15`, rubrique `A.8.6`), `SRC-068.txt` (`[2]` Principe 4 `L289`), `SRC-086.txt` (`[3]` `L133–184`), `registre/specifications-lplus.json` (`SPEC-A2A-TCK-ALPHA3`), `Corpus/Tome 2` (`§ 13.2`, `§ 13.4`).
  - **Passe initiale :** écart rectifié · **Action :** retiré `[2]` et `[3]` de `EXIG-APP-04` / `Tableau 54`, précisé le rôle de `PRR O-15` en `A.8.6` et maintenu `[3]` sur `a2a-tck` · **Verdict : supporté**

- **C27-05 (`L13`)** — *Affirmation :* Deuxième verrou : dix clauses minimales (`EXIG-APP-07` à `EXIG-APP-16`) appuyées sur `[1, 2, 4]`, testées annuellement à `POR-016`, verrouillées contre `EXIG-GOV-17` ; distinction entre dispositions légales (`1` an art. 11 `[1]`, mandat art. 18.3 `[1]`, entente art. 17 `[1]`, livres bancaires `[5]`, art. 3.5/18.3 `[1]`, attentes BSIF `[2]`, *Data Act* `12 janvier 2027`, art. 25(4) RIA `[4]`) et cibles du cadre (`10` j, `90` j, `24` h / `4` h, `6` mois, `24` h `NHI`).
  - **Appui vérifié :** `SRC-063.txt` (`[1]` art. 3.5, 11, 17, 18.3), `SRC-068.txt` (`[2]` § 2.3.3, § 2.3.5), `SRC-060.txt` (`[4]` art. 25(4)), `SRC-070.txt` (`[5]` art. 239), `registre/ancres-chronologiques.json` (`ANC-003`), `registre/matrice-exig-prr-c40.json` (`POR-016`), `Corpus/Tome 2` (`§ 13.3`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé l'exercice à blanc par le test réel `POR-016`, dissocié obligations légales et cibles internes, et réaligné `[1, 2, 4, 5]` · **Verdict : supporté**

- **C27-06 (`L15`)** — *Affirmation :* Troisième verrou : absence de personnalité juridique (`AB-316` art. `1714.46`, Directive `(UE) 2024/2853`, *Moffatt c. Air Canada* en `statut F` selon repérage *Tome 3*), modélisation de l'écart autorité réelle ↔ apparente, avenants `B2B` (`LCCJTI`, `LUCE`, `CNUDCI-2024`), mandats `AP2`, verrous anti-collusion (`PRR G-14`) et revue annuelle des exclusions IA en assurance.
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 36.1–36.5`, `§ 38.10`), `registre/matrice-exig-prr-c40.json` (`PRR G-14`), `registre/ancres-chronologiques.json` (`ANC-002`).
  - **Passe initiale :** écart rectifié · **Action :** retiré le renvoi hors portée `[4]`, qualifié le repérage *Tome 3* et réaffecté `PRR G-14` aux verrous anti-collusion · **Verdict : supporté**

### Section 27.2.1 — Banc d'essai et grille `Tableau 54` (`L19–L47`)

- **C27-07 (`L21`)** — *Affirmation :* Analyse préalable de réversibilité (`EXIG-APP-01`) en appui aux plans de sortie `[2]`, interdiction de dépendance à une extension non cataloguée (`EXIG-APP-02`, `URI` versionné, repli, jamais `required` sans dérogation) et réponse aux cinq foyers de verrouillage du repérage (*Tome 2*, Tableau 53).
  - **Appui vérifié :** `SRC-068.txt` (`[2]` § 2.3.5 `L443–461`, § 3.1 `L559`), `Corpus/Tome 2` (`L6285–6313`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché `[2]` aux plans de sortie et qualifié les cinq foyers comme repérage du *Tome 2* (Tableau 53) · **Verdict : supporté**

- **C27-08 (`L23`)** — *Affirmation :* `EXIG-APP-04` interdit de retenir comme critère ou exigence une latence, un débit ou une allégation publiés par un fournisseur, imposant quatre vérifications reproductibles (`EXIG-APP-03` à `EXIG-APP-06`).
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 13.2`, `L6335–6365`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C27-09 (`L25`)** — *Affirmation :* `EXIG-APP-03` exige scénarios `MCP 2026-07-28` et suite `a2a-tck` sans échec `MUST` (tests stables sur deux versions tant qu'en préversion `1.0.0.alpha3`), avec consignation des lacunes (`CARD-SIGN-001` à `CARD-SIGN-004` `NOT_AUTOMATABLE` — canonisation `JCS`, exclusion `signatures`, en-tête `JWS` et rejet des clés révoquées — et absence de `conformance-vectors/a2a-jcs-v01` `[3]`), compensées par les tests internes substitutifs `a2a_card.py`.
  - **Appui vérifié :** `SRC-086.txt` (`[3]` `L133–184`), `registre/specifications-lplus.json` (`SPEC-A2A-TCK-ALPHA3`), `harness_proto/a2a_card.py`, `Corpus/Tome 2` (`L6339`).
  - **Passe initiale :** Conforme · **Action :** précisés le détail `CARD-SIGN-001`..`004` et la compensation par `a2a_card.py` (`post-G4`) · **Verdict : supporté**

- **C27-10 (`L26`)** — *Affirmation :* `EXIG-APP-04` mesure `P50` et `P99` avec politiques `OPA` (ou `Cedar` en choix d'architecture), caviardage, traçage et journalisation actifs, en archivant données brutes, matériel et trafic.
  - **Appui vérifié :** `Corpus/Tome 2` (`L6343–6347`), `Corpus/Tome 3` (`ADR-020` `Cedar`).
  - **Passe initiale :** écart rectifié · **Action :** précisé le statut de choix d'architecture pour `Cedar` face à `OPA` vérifié en `G0` · **Verdict : supporté**

- **C27-11 (`L27`)** — *Affirmation :* `EXIG-APP-05` vérifie l'export `OTLP`, la version figée `OpenTelemetry GenAI` (`OTEL_SEMCONV_STABILITY_OPT_IN`), la propagation `W3C Trace Context` sur chaque saut maîtrisé (serveurs `MCP` hébergés inclus) et la facturation `FOCUS 1.4` ou ultérieur traduisant les unités propres en jetons.
  - **Appui vérifié :** `Corpus/Tome 2` (`L6351–6357`), `registre/specifications-lplus.json` (`SPEC-FOCUS-V1-4` `SRC-023`, `SPEC-OTEL-*` `SRC-037`, `SRC-089`, `SRC-090`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C27-12 (`L28`)** — *Affirmation :* `EXIG-APP-06` impose une `NHI` distincte fédérable sans secret statique partagé et la démonstration chronométrée de révocation (via `SSF`/`CAEP`, les tests substitutifs à `CARD-SIGN-004` `[3]` ne couvrant que la signature au catalogue `EXIG-A2A-03`) sous la borne `EXIG-IAM-20` (cible proposée `≤ 15` min incluant la durée résiduelle bornée par `EXIG-IAM-15`, distincte de la révocation `NHI` sous `24` h en `EXIG-APP-16`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L6359–6365`, `EXIG-IAM-15`, `EXIG-IAM-20`, `EXIG-APP-16`), `SRC-086.txt` (`[3]`), `registre/specifications-lplus.json` (`SPEC-OPENID-CAEP-1-0` `SRC-020`).
  - **Passe initiale :** écart rectifié · **Action :** retiré le renvoi hors portée `[2]` (`BSIF B-10`) et distinguée la borne `EXIG-IAM-20`/`15` de `EXIG-APP-16` (`24` h) (`post-G4`) · **Verdict : supporté**

- **C27-13 (`L30`)** — *Affirmation :* Règles de cotation du `Tableau 54` (`EXIG-APP-17`, *Tome 2*) : notes `0` à `3`, plafond à `1` sans essai interne, note `< 3` éliminatoire sur `Interopérabilité`, `Identité` et `Observabilité`, `< 2` sur les quatre autres critères éliminatoires (note provisoire `2` tolérée pour `Réversibilité` et `Coûts`), `Performance mesurée` (`5 %`) non éliminatoire bien que testée (`EXIG-APP-04`), rééquilibrage maximal de `± 5` points et plancher de `5 %` par critère éliminatoire.
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 13.4`, `L6459–6479`).
  - **Passe initiale :** écart rectifié · **Action :** retiré les renvois `[2]` et corrigé l'énoncé qui incluait à tort `Performance` dans les seuils d'exclusion automatique · **Verdict : supporté**

- **C27-14 (`L32–L43`, `Tableau 27.1`)** — *Affirmation :* Le `Tableau 27.1` reprend les huit critères, poids indicatifs (`20 %`, `15 %`, `15 %`, `15 %`, `15 %`, `10 %`, `5 %`, `5 %`), preuves exigées et statuts (`7` éliminatoires, `1` non éliminatoire) du `Tableau 54` (`EXIG-APP-17`), incluant la mention explicite `note 2 provisoire confirmée au 1er pilote` sur `Réversibilité et sortie` et `Coûts et FinOps`.
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 54`, `L6463–6477`), `SRC-086.txt` (`[3]`), `SRC-068.txt` (`[2]`), `SRC-063.txt` (`[1]`).
  - **Passe initiale :** écart rectifié · **Action :** retiré `[2]` de `Identité et délégation` (`L35`) et `[4]` de `Réversibilité et sortie` (`L39`) en y rattachant `[2]` aux stratégies de sortie `B-10`, et harmonisé au lissage G5 le libellé `note 2 provisoire confirmée au 1er pilote` · **Verdict : supporté**

- **C27-15 (`L45–L47`, `Figure 1`)** — *Affirmation :* `SCH-27-01.png` représente l'arbre de qualification en trois sas (refus `DOIT`/allégations `EXIG-APP-04`, banc d'essai `MCP`/`a2a-tck`/`P50`–`P99`/`OTLP`/`FOCUS 1.4+`, grille `Tableau 54` à `7` critères éliminatoires sur `8`).
  - **Appui vérifié :** `Compendium/ouvrage/schemas/SCH-27-01.mmd` (`L1–30`), `specs/manifest.json` (`SCH-27-01`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

### Section 27.2.2 — Clauses contractuelles et réversibilité (`L49–L78`)

- **C27-16 (`L51`)** — *Affirmation :* Incorporation obligatoire des dix clauses du cadre (`EXIG-APP-07..16`) appuyées sur `[1, 2, 4]`, avec écart contractuel interdit sur les obligations légales impératives (Loi 25 art. 17 et 18.3 `[1]`) et sur `EXIG-GOV-17` (`P3` sans approbation).
  - **Appui vérifié :** `Corpus/Tome 2` (`L6369`, `L6455`), `SRC-063.txt` (`[1]` art. 17, 18.3).
  - **Passe initiale :** écart rectifié · **Action :** rattaché `[1, 2, 4]` aux assises légales et prudentielles sous-jacentes plutôt qu'à la nomenclature interne `EXIG-APP-07..16` / `EXIG-GOV-17` · **Verdict : supporté**

- **C27-17 (`L53`)** — *Affirmation :* Clause 1 (`EXIG-APP-07`) : `A2A 1.0` natif (`a2a.proto`, `/.well-known/agent-card.json`, zéro extension obligatoire, vérifié par `a2a-tck` `[3]`, maintien `≥ 12` mois cible cadre) ; Clause 2 (`EXIG-APP-08`) : `MCP 2026-07-28`, `resource` `RFC 8707`, zéro relais de jeton et `RFC 8693` (`act`, intersection `sub ∩ act`).
  - **Appui vérifié :** `SRC-086.txt` (`[3]`), `SRC-083.txt` (`L1826`, `L1978`), `SRC-041.txt` (`RFC 8693`), `SRC-009.txt` (`RFC 8707`), `SRC-078.txt` (`L22–23`, `L124`), `Corpus/Tome 2` (`L6375–6389`).
  - **Passe initiale :** écart rectifié · **Action :** retiré `[2]` (`BSIF B-10`) sur `MCP`/`RFC 8693` et qualifié `12` mois comme cible du cadre à défaut de délai spécifique · **Verdict : supporté**

- **C27-18 (`L54`)** — *Affirmation :* Clause 3 (`EXIG-APP-09`) : accès continu aux traces, restitution sous `10` j (cible cadre) pour l'art. `12.1` et art. `32` (`30` j), conservation `≥ 1` an (art. `11` `[1]`) ; Clause 4 (`EXIG-APP-10`) : contrat écrit, usage limité au mandat et non-conservation (art. `18.3` `[1]`), étendus contractuellement pour interdire l'entraînement ou l'évaluation sur données/vecteurs avec rétention nulle ou bornée.
  - **Appui vérifié :** `SRC-063.txt` (`[1]` art. 11 `L1502–1503`, art. 12.1 `L1542–1555`, art. 18.3 `L1630–1655`, art. 32 `L1869–1871`), `Corpus/Tome 2` (`L6391–6405`).
  - **Passe initiale :** écart rectifié · **Action :** explicité que `10` j est cible du cadre et que l'interdiction d'entraînement est une extension contractuelle de la limitation au mandat de l'art. `18.3` `[1]` · **Verdict : supporté**

- **C27-19 (`L55`)** — *Affirmation :* Clause 5 (`EXIG-APP-11`) : déclaration des lieux, préavis cible `90` j, entente écrite après ÉFVP pour transfert hors Québec (art. `17` `[1]`), maintien au Canada des livres bancaires (art. `239` `[5]`), documentation `CLOUD Act` et `HYOK` ; Clause 6 (`EXIG-APP-12`) : avis sans délai au RPRP (art. `18.3` `[1]`), cibles cadre `24` h (`4` h IFF pour tenir le signalement BSIF `[2]`) et gel des preuves (`EXIG-CON-23`).
  - **Appui vérifié :** `SRC-063.txt` (`[1]` art. 17 `L1581–1605`, art. 18.3 `L1645–1655`), `SRC-070.txt` (`[5]` art. 239 `L7646`), `SRC-068.txt` (`[2]` § 2.3.3.2, § 3.1 `L491`, `L581`, `L625`), `Corpus/Tome 2` (`L6407–6421`).
  - **Passe initiale :** écart rectifié · **Action :** scindé la phrase pour respecter `CA-05`, rattaché `[5]` à l'art. `239` de la *Loi sur les banques*, et qualifié `90` j / `24` h / `4` h comme cibles du cadre · **Verdict : supporté**

- **C27-20 (`L56`)** — *Affirmation :* Clause 7 (`EXIG-APP-13`) : droit d'audit `BSIF B-10` `[2]`, équipe rouge *OWASP Top 10 for Agentic Applications* (`2026`), inventaire des composants, préavis cible `≥ 90` j avant retrait/changement de modèle et accès sous enquête ; Clause 8 (`EXIG-APP-14`) : restitution formats ouverts (`CoALA`, graphes, traces, jeux), assistance cible `6` mois et destruction écrite attestée `[1, 2]`.
  - **Appui vérifié :** `SRC-068.txt` (`[2]` Principe 8 `L411–415`, § 2.3.5 `L445–461`), `SRC-063.txt` (`[1]` art. `18.3`), `SRC-055.txt` (`L1–5`), `Corpus/Tome 2` (`L6423–6437`).
  - **Passe initiale :** écart rectifié · **Action :** rétabli le titre exact *OWASP Top 10 for Agentic Applications* (`2026`) et qualifié `90` j et `6` mois comme cibles du cadre · **Verdict : supporté**

- **C27-21 (`L57`)** — *Affirmation :* Clause 9 (`EXIG-APP-15`) : accord écrit art. `25(4)` de l'*EU AI Act* (ou documentation art. `53` pour `GPAI`) lors d'une fourniture ou requalification art. `25(1)` `[4]` ; Clause 10 (`EXIG-APP-16`) : invalidation immédiate (`CAEP`) à la suspension et révocation écrite `NHI` sous la cible de `24` h.
  - **Appui vérifié :** `SRC-060.txt` (`[4]` art. 25 `L4197–4237`, art. 53 `L5218`), `Corpus/Tome 2` (`L6439–6453`).
  - **Passe initiale :** écart rectifié · **Action :** retiré le renvoi `[2]` en fin de Clause 10 et qualifié `24` h comme cible interne · **Verdict : supporté**

- **C27-22 (`L59`)** — *Affirmation :* Stratégie anti-concentration `hyperscalers` : interdiction des frais de changement dès le `12 janvier 2027` (`Data Act` `(UE) 2023/2854` art. `29 § 1`, ancre `ANC-003`), plans de sortie `DORA` (`← Ch. 26`) et `BSIF B-10` `[2]`, ouverture bancaire et sécurité des accès au Canada `[6]`, et test annuel réel `POR-016` avec fenêtre cible de dépréciation de `12` mois.
  - **Appui vérifié :** `registre/ancres-chronologiques.json` (`ANC-003` `L483–497`), `SRC-068.txt` (`[2]` § 2.3.5, § 3.1), `SRC-114.txt` (`[6]` `L.C. 2026, ch. 3, art. 224`), `registre/matrice-exig-prr-c40.json` (`POR-016`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché le *Data Act* à `ANC-003` (hors texte intégral dans `[4]`), `DORA` au chapitre 26, `[6]` à l'ouverture bancaire canadienne et retiré `[5, 6]` de la cible `12` mois de `POR-016` · **Verdict : supporté**

- **C27-23 (`L61–L74`, `Tableau 27.2`)** — *Affirmation :* Le `Tableau 27.2` synthétise l'ancrage juridique/prudentiel et les seuils ou cibles exécutables des dix clauses `EXIG-APP-07` à `EXIG-APP-16`.
  - **Appui vérifié :** `SRC-063.txt` `[1]`, `SRC-068.txt` `[2]`, `SRC-086.txt` `[3]`, `SRC-060.txt` `[4]`, `SRC-070.txt` `[5]`, `registre/ancres-chronologiques.json` (`ANC-003`, `ANC-007`, `ANC-010`), `SRC-055.txt` (`NHI1` 2025), `Corpus/Tome 2` (`§ 13.3`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté mentions `(cible)` / `ANC-003` / `[1]` / `[2]` / `[5]` / `OWASP NHI1 (2025)` et aligné `EXIG-APP-07` sur `a2a-tck` `[3]` · **Verdict : supporté**

- **C27-24 (`L76–L78`, `Figure 2`)** — *Affirmation :* `SCH-27-02.svg` oppose un contrat infonuagique captif aux deux piliers des dix clauses `EXIG-APP-07..16` et à la porte `POR-016`.
  - **Appui vérifié :** `Compendium/ouvrage/schemas/SCH-27-02.svg` (`L1–94`), `specs/manifest.json` (`SCH-27-02`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

### Section 27.2.3 — Mandat apparent, contrats B2B et risques juridiques (`L80–L99`)

- **C27-25 (`L82–L84`)** — *Affirmation :* Absence de personnalité juridique des agents (`AB-316` art. `1714.46` du Code civil californien, en vigueur le 1er janvier 2026 selon suivi législatif et reproduction hors portail officiel dans *Tome 3* § 36.1) ; imputation canadienne *Moffatt c. Air Canada* (`2024 BCCRT 149`, connue via analyses doctrinales, source primaire en `statut F`) ; Directive `(UE) 2024/2853` (transposable au `9 décembre 2026`, `ANC-002`, proposition `AILD` retirée en 2025 selon `CSA` en `statut F`) qualifiant le logiciel de produit tout en excluant les pertes commerciales `B2B`.
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 36.1` `L19394–19406`, `§ 36.4` `L19483–19495`, limites `L19598–19608`), `registre/ancres-chronologiques.json` (`ANC-002` `L403–417`).
  - **Passe initiale :** écart rectifié · **Action :** retiré les trois faux renvois `[4]` et explicité la provenance (`Tome 3`, `ANC-002`, `statut F`) · **Verdict : supporté**

- **C27-26 (`L86`)** — *Affirmation :* Modélisation par déduction architecturale (*Tome 3*, § 36.2) de l'écart entre autorité réelle configurée (`OAuth`, `OPA`/`Cedar`, mandats) et autorité apparente perçue par les tiers (canal, marque, `AgentCard` sans borne).
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 36.2`, `L19420–19430` : « Ce qui suit est une déduction »).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement cette traduction architecturale de modélisation par déduction du *Tome 3* (`§ 36.2`) · **Verdict : supporté**

- **C27-27 (`L88`)** — *Affirmation :* Cadre des contrats électroniques relevé au *Tome 3* (`§ 36.3`, `§ 38.10`) : `LCCJTI` (`L.Q. 2001, c. 32`, `RLRQ, c. C-1.1` en `statut F`) sans mention d'« agent » ni d'« automatisé » ; loi modèle `LUCE` de *common law* non applicable au Québec ; `E-SIGN`, `UETA` (art. `14` en `statut F`) et loi type `CNUDCI-2024` (11 juillet 2024, texte modèle non contraignant) ; insuffisance face à l'erreur unilatérale probabiliste et exclusion du règlement des litiges dans `AP2` (`← Ch. 08`).
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 36.3` `L19463–19477`, `§ 38.10` `L20057–20058`, `L20300`).
  - **Passe initiale :** écart rectifié · **Action :** apporté les réserves exactes du *Tome 3* sur `LCCJTI`, `LUCE`, `UETA` et `CNUDCI-2024` · **Verdict : supporté**

- **C27-28 (`L90–L95`)** — *Affirmation :* Quatre garde-fous `B2B` : (1) avenants bilatéraux (`LCCJTI`/`LUCE`), mandats `AP2` plafonnés, *Diplomate / Évaluateur* et `Cedar` (`← Ch. 13`) ; (2) publication des limites, `CIBA` et `non-avis` (`EXIG-AMF-12`, `EXIG-CON-19`) ; (3) verrous hors modèle anti-collusion (`PRR G-14`) face à *Loi sur la concurrence*, *Sherman Act* et art. `101 TFUE` (*Tome 3* `§ 38.10`) ; (4) revue annuelle des assurances face aux formulaires `ISO`/`Verisk` (`CG 40 47`, `CG 40 48`, `CG 35 08`, connus par presse spécialisée en *Tome 3* `§ 36.5`, textes en `statut F`) et solvabilité fournisseur.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`PRR G-14`), `Corpus/Tome 2` (`EXIG-CON-19`), `Corpus/Tome 3` (`§ 36.5` `L19505–19519`, `§ 38.10` `L20306`), `Corpus/Tome 5` (`EXIG-AMF-12`).
  - **Passe initiale :** écart rectifié · **Action :** déplacé `PRR G-14` vers le verrou 3 anti-collusion, scindé la phrase de `L95` selon `CA-05` et qualifié la source secondaire des formulaires `Verisk` · **Verdict : supporté**

- **C27-29 (`L97–L99`, `Figure 3`)** — *Affirmation :* `SCH-27-03.svg` illustre l'écart autorité réelle ↔ apparente (*Moffatt*, `AB-316`) et les quatre garde-fous `B2B` (avenants `LCCJTI`/`LUCE`, mandats `AP2`, anti-collusion `PRR G-14` et audit d'assurance).
  - **Appui vérifié :** `Compendium/ouvrage/schemas/SCH-27-03.puml` (`L61–89`), `specs/manifest.json` (`SCH-27-03`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la légende `L99` pour associer `PRR G-14` à l'anti-collusion · **Verdict : supporté**

### Section 27.3 — Synthèse, livrables, clôture et invariants (`L101–L122`)

- **C27-30 (`L103–L105`)** — *Affirmation :* Interfaces amont (`ch08`, `ch09`, `ch13`, `ch25`, `ch26`) et aval (`ch29`, `ch34` `PRR O-15`) ; en `G0`, `test_third_party_vectors.py` (`Tome 8/trousse/`) exécute `5` fichiers de vecteurs `a2a_tck` et cas négatifs locaux dérivés de `1.0.0.alpha3` (`114` `MUST`, `a2a_jcs_v01` absent `[3]`).
  - **Appui vérifié :** `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/tests/test_third_party_vectors.py` (`L294–356`), `aq/rapports-g0.json` (`L64–68`), `SRC-086.txt` `[3]`.
  - **Passe initiale :** écart rectifié · **Action :** scindé le paragraphe selon `CA-05` et précisé la portée exacte des `5` fichiers `a2a_tck` et `114` `MUST` en `G0` · **Verdict : supporté**

- **C27-31 (`L107–L114`, `Tableau 27.3`)** — *Affirmation :* Quatre livrables (`Tableau 54`, annexe des `10` clauses sans contradiction avec `EXIG-GOV-17`, plan de réversibilité et test annuel `POR-016`, avenant `B2B` + anti-collusion `PRR G-14` + revue assurances) et leurs critères d'acceptation.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`EXIG-APP-*`, `CAP-051`, `INI-014`, `POR-004`, `POR-016`, `PRR O-15`, `PRR G-14`), `SRC-063.txt` `[1]`, `SRC-068.txt` `[2]`, `SRC-086.txt` `[3]`, `SRC-060.txt` `[4]`.
  - **Passe initiale :** écart rectifié · **Action :** retiré `[2]` du banc d'essai (`L109`) et `[4]` des assurances (`L112`), aligné test réel `POR-016`, `ANC-003` et `PRR G-14` · **Verdict : supporté**

- **C27-32 (`L116–L122`)** — *Affirmation :* Transition vers la Partie X (`→ Chapitre 28`) et trois invariants exécutables du Chapitre 27 (banc éliminatoire `7/8`, dix clauses non dérogeables et sortie `POR-016`, maîtrise de l'écart réel ↔ apparent en `B2B` avec `PRR G-14` et audit d'assurance).
  - **Appui vérifié :** `specs/manifest.json` (`ch27`, `ch28`), `SRC-063.txt` `[1]`, `SRC-068.txt` `[2]`, `SRC-086.txt` `[3]`, `SRC-060.txt` `[4]`, `SRC-070.txt` `[5]`, `SRC-114.txt` `[6]`.
  - **Passe initiale :** écart rectifié · **Action :** retiré `[2, 3]` de la fin du premier invariant et `[4]` de la fin du troisième, ajouté l'ancrage exact `[5, 6]` et `PRR G-14` · **Verdict : supporté**
