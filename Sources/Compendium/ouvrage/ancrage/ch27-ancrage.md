# Journal d'ancrage atomique Wyvern G2 — Chapitre 27 (`ch27`)

- **Unité auditée :** `Sources/Compendium/ouvrage/manuscrit/09 - Partie IX/Chapitre 27.md` (`4 231` mots de prose selon `verifie_manuscrit.py`, plage `[3 726, 4 374]`)
- **Base documentaire fermée :** `Sources/Compendium/ouvrage/sources/ch27-sources.md` (`[1]`–`[6]` en statut `L+`, `2` exclusions `statut F`, Option A iso-corpus) ; textes intégraux `Sources/Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Sources/Compendium/ouvrage/registre/*.json` ; protocole `Sources/Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Sources/Compendium/ouvrage/aq/rapports-g0.json` et `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/tests/test_third_party_vectors.py`) ; index heuristique interne `Sources/Tomes/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-6` (mise à jour Vague 2 `auteur-d09-d10`)
- **Passe G2 initiale (supportés) :** 6
- **Rectifications appliquées lors de la passe G2 et du rééquilibrage multisectoriel :** 27
- **Verdict final — supportés :** 33 / 33 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 27.md`

Toutes les formulations divergentes, sur-attribuées à des renvois `[n]` ou issues du repérage antérieur hors socle `L+` fermé relevées lors de la passe initiale, ainsi que l'élargissement transversal aux suites applicatives d'entreprise et à l'automatisation `B2B` en Option A iso-corpus, ont été ancrés directement dans [Chapitre 27.md](file:///c:/Github/Agentique/Sources/Compendium/ouvrage/manuscrit/09%20-%20Partie%20IX/Chapitre%2027.md), sans altérer `CA-01`..`CA-22`, en préservant les cinq `owned_concepts`, les renvois `[1]`–`[6]`, les trois figures `SCH-27-01`..`03` (`Figure 97`..`Figure 99`), les trois tableaux et le calibrage (`4 231` mots dans `[3 726, 4 374]`) :

1. **Approvisionnement réversible sur l'ensemble du parc applicatif (`L1`–`L49`, `Tableau 27.1`, `Figure 97`) :** alignement du titre `L1` sur `specs/manifest.json` ; couverture explicite tant des plateformes dédiées (modèles, orchestrateurs, passerelles, serveurs `MCP`) que de l'activation d'extensions agentiques dans les suites d'entreprise (`ERP`, `CRM`, `ITSM`, `SIRH`, `iPaaS`) ; maintien intégral de la pondération du `Tableau 27.1` (`20 % + 15 % + 15 % + 15 % + 15 % + 10 % + 5 % + 5 % = 100 %`, `7` critères éliminatoires sur `8`, `Performance mesurée` à `5 %` non éliminatoire bien que testée sous `EXIG-APP-04`, `PRR O-15` en `A.8.6`).
2. **Distinction exacte `EXIG-APP-13` vs `EXIG-APP-14` et réattribution stricte `[1]`–`[6]` (`L13`, `L51`–`L78`, `Tableau 27.2`, `Figure 98`) :** distinction nette entre la Clause 7 (`EXIG-APP-13` : droit d'audit tiers selon l'étalon `BSIF B-10` `[2]`, rapports d'équipe rouge *OWASP Top 10 for Agentic Applications* `2026`, inventaire des modèles/serveurs `MCP`, préavis cible `≥ 90` j avant retrait ou modification de modèle même sous alias et maintien sous enquête) et la Clause 8 (`EXIG-APP-14` : restitution intégrale en formats ouverts sans sémantique captive de l'état `CoALA`/graphes/cartes/politiques/traces/index/jeux, sortie sans frais sous `Data Act` au `12 janvier 2027` `ANC-003`, assistance cible `6` mois et destruction écrite attestée `[1, 2]`), éprouvée annuellement à `POR-016` ; ancrage exact de `[1]` (`Loi 25` art. 3.5, 11, 12.1, 17, 18.3, 23, 32), `[2]` (`BSIF B-10`), `[3]` (`a2a-tck 1.0.0.alpha3`), `[4]` (`EU AI Act` art. 25(4), 53), `[5]` (*Loi sur les banques* art. 239) et `[6]` (`LSAC` ouverture sécurisée canadienne).
3. **Mandat apparent et automatisation contractuelle `B2B` (`L15`, `L80`–`L99`, `Figure 99`) :** cadrage des flux externes (`CRM`, achats *Source-to-Pay* `ERP`, logistique `SCM`, places de marché) ; qualification en repérage doctrinal (`Tome 3 § 36, § 38.10`, hors `L+`) d'`AB-316` (`art. 1714.46`), *Moffatt c. Air Canada* (`statut F`), Directive `(UE) 2024/2853` (`ANC-002`), `LCCJTI`/`LUCE`/`E-SIGN`/`UETA`/`CNUDCI-2024` et formulaires `ISO`/`Verisk` (`CG 40 47`, `40 48`, `35 08`, `statut F`) ; rattachement exact de `PRR G-14` aux verrous anti-collusion algorithmique (`matrice-exig-prr-c40.json`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C27-01` à `C27-33`)

### Section introductive et Section 27.1 — Résumé exécutif (`L1–L15`)

- **C27-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice posant la conversion de l'interopérabilité protocolaire ouverte et des exigences multi-juridictions en critères éliminatoires d'approvisionnement pour les systèmes d'entreprise, en dix clauses de réversibilité et en garde-fous `B2B`.
  - **Appui vérifié :** `specs/manifest.json` (`ch27`, `D09`, `SUB_D09_03`, `owned_concepts`), `registre/matrice-exig-prr-c40.json` (`CAP-051`, `EXIG-APP-01..17`).
  - **Verdict : supporté**

- **C27-02 (`L5`)** — *Affirmation :* Risque de réintroduction par contrat de l'opacité, du réentraînement ou de la captivité lors de l'activation d'extensions agentiques sur les suites (`ERP`, `CRM`, `ITSM`, `SIRH`, `iPaaS`) ou d'achats dédiés ; selon le repérage du cadre (*Tome 2*, 27 octobre 2026, hors socle `L+`), le transfert de `MCP` et d'`A2A` vers `AAIF` a déplacé le verrouillage vers cinq foyers (`Tableau 53`).
  - **Appui vérifié :** `Tome 2 § 13.1` (`Tableau 53`), `Tome 3` (`ADR-004`).
  - **Verdict : supporté**

- **C27-03 (`L7`)** — *Affirmation :* Clôture de `D09` au gel du `2 décembre 2026` sous clause `non-avis` (`AO-05`) ; appuis `L+` `[1]`–`[6]` distincts des règles internes (`CRE-IA-2026-01`), avec exclusions `statut F` (`iso.org` pour `ISO/IEC 42001`, `legisquebec.gouv.qc.ca`, formulaires *ISO/Verisk* et décisions non ouvertes).
  - **Appui vérifié :** `sources/ch27-sources.md`, `specs/protocole-mlr-compendium.json` (`AO-01`, `AO-05`).
  - **Verdict : supporté**

- **C27-04 (`L11`)** — *Affirmation :* Premier verrou (`CAP-051`, `INI-014`, `POR-004`, `POR-016`) : rejet des allégations non mesurées (`EXIG-APP-04`) en appui à la diligence tiers `[2]`, qualification sur le `Tableau 27.1` (`Tableau 54` du Tome 2 : interopérabilité à `20 %` en tête, `7` critères éliminatoires sur `8`, refus `DOIT` bloquant pour `EXIG-APP-01..06`, `17`, retrait `PRR O-15` en `A.8.6`) et consignation des lacunes `a2a-tck 1.0.0.alpha3` (`CARD-SIGN-001`..`004` `NOT_AUTOMATABLE` sans `a2a-jcs-v01` `[3]`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json`, `SRC-068.txt` `[2]`, `SRC-086.txt` `[3]`, `Tome 2 § 13.2, § 13.4`.
  - **Verdict : supporté**

- **C27-05 (`L13`)** — *Affirmation :* Deuxième verrou : dix clauses minimales (`EXIG-APP-07` à `EXIG-APP-16`) appuyées sur `[1, 2, 4]`, testées chaque année à `POR-016` et verrouillées contre `EXIG-GOV-17`, distinguant obligations légales (`1` an art. 11 `[1]`, art. 18.3 `[1]`, art. 17 `[1]`, livres bancaires `[5]`, art. 3.5/18.3 `[1]`, attentes BSIF `[2]`, *Data Act* `12 janvier 2027` `ANC-003`, art. 25(4) RIA `[4]`) et cibles du cadre (`10` j, `90` j, `24` h / `4` h, `6` mois, `24` h `NHI`), ainsi qu'`EXIG-APP-13` vs `EXIG-APP-14`.
  - **Appui vérifié :** `SRC-063.txt` `[1]`, `SRC-068.txt` `[2]`, `SRC-060.txt` `[4]`, `SRC-070.txt` `[5]`, `ancres-chronologiques.json` (`ANC-003`), `matrice-exig-prr-c40.json` (`POR-016`), `Tome 2 § 13.3`.
  - **Verdict : supporté**

- **C27-06 (`L15`)** — *Affirmation :* Troisième verrou : absence de personnalité juridique (`AB-316` art. `1714.46`, Directive `(UE) 2024/2853`, *Moffatt c. Air Canada* en `statut F`, repérage `Tome 3`), responsabilité sur l'écart autorité réelle ↔ apparente (`CRM`, `ERP`, places de marché), avenants `B2B` (`LCCJTI`, `LUCE`, `CNUDCI-2024`), mandats `AP2` plafonnés, verrous anti-collusion (`PRR G-14`) et audit annuel d'assurance.
  - **Appui vérifié :** `Tome 3 § 36.1–36.5, § 38.10`, `matrice-exig-prr-c40.json` (`PRR G-14`), `ancres-chronologiques.json` (`ANC-002`).
  - **Verdict : supporté**

### Section 27.2.1 — Banc d'essai, `Tableau 27.1` et clauses `EXIG-APP-07..16` (`L19–L78`, Tableaux 27.1–27.2, Figures 97–98)

- **C27-07 (`L21`)** — *Affirmation :* Analyse préalable de réversibilité (`EXIG-APP-01`) en appui aux plans de sortie `[2]`, interdiction d'extension propriétaire hors catalogue (`EXIG-APP-02`) et neutralisation des cinq foyers de verrouillage du repérage (*Tome 2*, Tableau 53).
  - **Appui vérifié :** `SRC-068.txt` `[2]`, `Tome 2` (`L6285–6313`).
  - **Verdict : supporté**

- **C27-08 (`L23`)** — *Affirmation :* `EXIG-APP-04` interdit de retenir comme critère une allégation fournisseur non mesurée et impose quatre vérifications reproductibles (`EXIG-APP-03` à `EXIG-APP-06`).
  - **Appui vérifié :** `Tome 2 § 13.2`.
  - **Verdict : supporté**

- **C27-09 (`L25`)** — *Affirmation :* `EXIG-APP-03` exige scénarios `MCP 2026-07-28` et suite `a2a-tck` sans échec `MUST` `[3]`, avec consignation des lacunes de `1.0.0.alpha3` (`CARD-SIGN-001`..`004` `NOT_AUTOMATABLE` et absence de `conformance-vectors/a2a-jcs-v01` `[3]`) compensées par `a2a_card.py`.
  - **Appui vérifié :** `SRC-086.txt` `[3]`, `specifications-lplus.json` (`SPEC-A2A-TCK-ALPHA3`), `Tome 8/trousse/harness_proto/a2a_card.py`.
  - **Verdict : supporté**

- **C27-10 (`L26`)** — *Affirmation :* `EXIG-APP-04` mesure `P50` et `P99` avec politiques `OPA` (ou `Cedar` en choix d'architecture), caviardage, traçage et journalisation actifs, en archivant données brutes, matériel et profil de trafic.
  - **Appui vérifié :** `Tome 2` (`L6343–6347`), `Tome 3` (`ADR-020`).
  - **Verdict : supporté**

- **C27-11 (`L27`)** — *Affirmation :* `EXIG-APP-05` vérifie l'export `OTLP`, `OpenTelemetry GenAI` (`OTEL_SEMCONV_STABILITY_OPT_IN`), `W3C Trace Context` sur tous les sauts maîtrisés et la facturation `FOCUS 1.4+` traduisant les crédits propriétaires en jetons vers l'`ITFM`/`ERP`.
  - **Appui vérifié :** `Tome 2` (`L6351–6357`), `specifications-lplus.json` (`SPEC-FOCUS-V1-4`, `SPEC-OTEL-*`).
  - **Verdict : supporté**

- **C27-12 (`L28`)** — *Affirmation :* `EXIG-APP-06` impose une `NHI` distincte fédérable sans secret statique et la démonstration chronométrée de révocation via `SSF`/`CAEP` sous `EXIG-IAM-20` (`≤ 15` min incluant `EXIG-IAM-15`, distincte de `EXIG-APP-16` sous `24` h), en complément des tests substitutifs à `CARD-SIGN-004` `[3]`.
  - **Appui vérifié :** `Tome 2` (`EXIG-APP-06`, `EXIG-IAM-15/20`, `EXIG-APP-16`), `SRC-086.txt` `[3]`.
  - **Verdict : supporté**

- **C27-13 (`L30`, `L32`)** — *Affirmation :* Règles de cotation du `Tableau 27.1` (`Tableau 54` du Tome 2, `EXIG-APP-17`) : notes `0` à `3`, plafond à `1` sans essai interne, `< 3` éliminatoire sur `Interopérabilité`, `Identité` et `Observabilité`, `< 2` sur les quatre autres critères éliminatoires (note `2` provisoire confirmée `≥ 2` au 1er pilote pour `Réversibilité` et `Coûts`), `Performance mesurée` (`5 %`) non éliminatoire, marge `± 5` points et plancher `5 %`.
  - **Appui vérifié :** `Tome 2 § 13.4` (`L6459–6479`).
  - **Verdict : supporté**

- **C27-14 (`L34–L45`, `Tableau 27.1`)** — *Affirmation :* Le `Tableau 27.1` reprend les huit critères et poids (`20 %`, `15 %`, `15 %`, `15 %`, `15 %`, `10 %`, `5 %`, `5 %`), preuves (`[1, 2, 3]`) et statuts (`7` éliminatoires, `1` non éliminatoire) de `EXIG-APP-17`.
  - **Appui vérifié :** `Tome 2` (`Tableau 54`), `SRC-063.txt` `[1]`, `SRC-068.txt` `[2]`, `SRC-086.txt` `[3]`.
  - **Verdict : supporté**

- **C27-15 (`L47–L49`, `Figure 97`)** — *Affirmation :* `Figure 97` (`SCH-27-01.png`) représentant l'arbre de qualification éliminatoire en trois sas.
  - **Appui vérifié :** `specs/manifest.json` (`SCH-27-01`), `schemas/SCH-27-01.mmd`.
  - **Verdict : supporté**

- **C27-16 (`L51`)** — *Affirmation :* Incorporation obligatoire des dix clauses `EXIG-APP-07..16` appuyées sur `[1, 2, 4]`, sans dérogation sur les obligations légales impératives (Loi 25 art. 17 et 18.3 `[1]`) ni sur `EXIG-GOV-17`.
  - **Appui vérifié :** `Tome 2` (`L6369`, `L6455`), `SRC-063.txt` `[1]`.
  - **Verdict : supporté**

- **C27-17 (`L53`)** — *Affirmation :* Clause 1 (`EXIG-APP-07` : `A2A v1.0.1` natif, `a2a-tck` `[3]`, maintien `≥ 12` mois cible cadre) et Clause 2 (`EXIG-APP-08` : `MCP 2026-07-28`, `RFC 8707`, zéro relais de jeton, `RFC 8693` `act`).
  - **Appui vérifié :** `SRC-086.txt` `[3]`, `Tome 2` (`L6375–6389`).
  - **Verdict : supporté**

- **C27-18 (`L54`)** — *Affirmation :* Clause 3 (`EXIG-APP-09` : accès continu aux traces, restitution `≤ 10` j cible pour art. 12.1 et art. 32 `30` j, conservation `≥ 1` an art. 11 `[1]`) et Clause 4 (`EXIG-APP-10` : art. 18.3 `[1]` étendu contractuellement en interdiction d'entraînement et rétention nulle ou bornée).
  - **Appui vérifié :** `SRC-063.txt` `[1]`, `Tome 2` (`L6391–6405`).
  - **Verdict : supporté**

- **C27-19 (`L55`)** — *Affirmation :* Clause 5 (`EXIG-APP-11` : lieux de traitement, préavis cible `90` j, entente art. 17 `[1]`, chaînes `NIS 2` `← ch26`, livres bancaires art. 239 `[5]`, `CLOUD Act` et `HYOK`) et Clause 6 (`EXIG-APP-12` : avis sans délai art. 18.3 `[1]`, cibles `24` h / `4` h IFF `[2]`, gel `EXIG-CON-23`).
  - **Appui vérifié :** `SRC-063.txt` `[1]`, `SRC-068.txt` `[2]`, `SRC-070.txt` `[5]`, `Tome 2` (`L6407–6421`).
  - **Verdict : supporté**

- **C27-20 (`L56`)** — *Affirmation :* Distinction stricte entre Clause 7 (`EXIG-APP-13` : droit d'audit tiers selon l'étalon `BSIF B-10` `[2]`, équipe rouge *OWASP Top 10 for Agentic Applications* `2026`, inventaire modèles/serveurs `MCP`, préavis cible `≥ 90` j avant retrait/changement de modèle même sous alias, maintien sous enquête) et Clause 8 (`EXIG-APP-14` : restitution ouverte intégrale sans sémantique captive, assistance cible `6` mois et destruction attestée `[1, 2]`).
  - **Appui vérifié :** `SRC-068.txt` (`Principe 8`, `§ 2.3.5`) `[2]`, `SRC-063.txt` (`art. 18.3, 23`) `[1]`, `Tome 2` (`L6423–6437`).
  - **Verdict : supporté**

- **C27-21 (`L57`)** — *Affirmation :* Clause 9 (`EXIG-APP-15` : accord écrit art. `25(4)` ou doc. art. `53` de l'*EU AI Act* `[4]`) et Clause 10 (`EXIG-APP-16` : coupure immédiate `CAEP` et révocation écrite `NHI` sous cible `24` h).
  - **Appui vérifié :** `SRC-060.txt` `[4]`, `Tome 2` (`L6439–6453`).
  - **Verdict : supporté**

- **C27-22 (`L59`)** — *Affirmation :* Anti-concentration `SaaS` et `hyperscalers` : interdiction des frais de changement dès le `12 janvier 2027` (*Data Act* `(UE) 2023/2854` art. `29 § 1`, `ANC-003`), couplée à `EXIG-APP-14` et `EXIG-APP-07..08` (`A2A` `[3]` / `MCP`), plans de sortie `DORA`/`NIS 2` (`← ch26`) et `BSIF B-10` `[2]`, ouverture sécurisée canadienne `[6]`, et test annuel réel `POR-016` (dépréciation cible `12` mois).
  - **Appui vérifié :** `ancres-chronologiques.json` (`ANC-003`), `SRC-068.txt` `[2]`, `SRC-086.txt` `[3]`, `SRC-114.txt` `[6]`, `matrice-exig-prr-c40.json` (`POR-016`).
  - **Verdict : supporté**

- **C27-23 (`L61–L74`, `Tableau 27.2`)** — *Affirmation :* Le `Tableau 27.2` synthétise l'ancrage juridique/prudentiel et les seuils exécutables des dix clauses `EXIG-APP-07` à `EXIG-APP-16`.
  - **Appui vérifié :** `SRC-063.txt` `[1]`, `SRC-068.txt` `[2]`, `SRC-086.txt` `[3]`, `SRC-060.txt` `[4]`, `SRC-070.txt` `[5]`, `ancres-chronologiques.json` (`ANC-003`, `ANC-007`, `ANC-010`), `Tome 2 § 13.3`.
  - **Verdict : supporté**

- **C27-24 (`L76–L78`, `Figure 98`)** — *Affirmation :* `Figure 98` (`SCH-27-02.svg`) opposant un contrat captif au bouclier des dix clauses `EXIG-APP-07..16` et à `POR-016`.
  - **Appui vérifié :** `specs/manifest.json` (`SCH-27-02`), `schemas/SCH-27-02.svg`.
  - **Verdict : supporté**

### Section 27.2.2 — Mandat apparent et responsabilité B2B (`L80–L99`, Figure 99)

- **C27-25 (`L82`, `L84`)** — *Affirmation :* Absence de personnalité juridique des agents (`AB-316` art. `1714.46` en vigueur le `1er janvier 2026` selon suivi législatif au *Tome 3* § 36.1) ; imputation canadienne *Moffatt c. Air Canada* (`2024 BCCRT 149`, connue par doctrine, décision primaire en `statut F`) ; Directive `(UE) 2024/2853` (`9 décembre 2026`, `ANC-002`, `AILD` retirée en 2025 selon `CSA` en `statut F`, *Tome 3* § 36.4).
  - **Appui vérifié :** `Tome 3 § 36.1, § 36.4`, `ancres-chronologiques.json` (`ANC-002`).
  - **Verdict : supporté**

- **C27-26 (`L86`)** — *Affirmation :* Modélisation par déduction architecturale (*Tome 3* § 36.2) de l'écart entre autorité réelle configurée (`OAuth`, `OPA`/`Cedar`, mandats devant `ERP`/`CRM`) et autorité apparente perçue par les clients ou fournisseurs.
  - **Appui vérifié :** `Tome 3 § 36.2`.
  - **Verdict : supporté**

- **C27-27 (`L88`)** — *Affirmation :* Cadre des contrats électroniques `B2B` (*Tome 3* § 36.3, § 38.10) : `LCCJTI` (`LQ 2001, c. 32`, `RLRQ, c. C-1.1` en `statut F`), `LUCE` (*common law* hors Québec), `E-SIGN`, `UETA` (art. 14 en `statut F`), loi type `CNUDCI-2024` (`11 juillet 2024`) et exclusion du règlement des litiges dans `AP2` (`← ch08`).
  - **Appui vérifié :** `Tome 3 § 36.3, § 38.10`.
  - **Verdict : supporté**

- **C27-28 (`L90–L95`)** — *Affirmation :* Quatre garde-fous d'automatisation `B2B` : (1) avenants bilatéraux (`LCCJTI`/`LUCE`), mandats `AP2` plafonnés, *Diplomate / Évaluateur* et rapprochement tripartite `Cedar` (`← ch13`) ; (2) publication des limites, `CIBA` et `non-avis` (`EXIG-AMF-12`, `EXIG-CON-19`) ; (3) verrous anti-collusion (`PRR G-14`) face à *Loi sur la concurrence*, *Sherman Act* et art. `101 TFUE` (*Tome 3* § 38.10) ; (4) audit annuel des assurances face aux formulaires `ISO`/`Verisk` (`CG 40 47`, `40 48`, `35 08`, presse spécialisée *Tome 3* § 36.5, `statut F`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`PRR G-14`), `Tome 2` (`EXIG-CON-19`), `Tome 3 § 36.5, § 38.10`, `Tome 5` (`EXIG-AMF-12`).
  - **Verdict : supporté**

- **C27-29 (`L97–L99`, `Figure 99`)** — *Affirmation :* `Figure 99` (`SCH-27-03.svg`) illustrant l'écart autorité réelle ↔ apparente et les quatre garde-fous `B2B`.
  - **Appui vérifié :** `specs/manifest.json` (`SCH-27-03`), `schemas/SCH-27-03.puml`.
  - **Verdict : supporté**

### Section 27.3 — Synthèse, livrables et invariants (`L101–L122`, Tableau 27.3)

- **C27-30 (`L103`, `L105`)** — *Affirmation :* Interfaces amont (`ch08`, `09`, `13`, `25`, `26`) et aval (`ch29`, `ch34` `PRR O-15`) ; en `G0`, exécution de `5` fichiers de vecteurs `a2a_tck` et cas négatifs locaux dérivés de `1.0.0.alpha3` (`114` `MUST`, `a2a_jcs_v01` absent `[3]`) dans `test_third_party_vectors.py`.
  - **Appui vérifié :** `Tome 8/trousse/tests/test_third_party_vectors.py`, `aq/rapports-g0.json`, `SRC-086.txt` `[3]`.
  - **Verdict : supporté**

- **C27-31 (`L107–L114`, `Tableau 27.3`)** — *Affirmation :* Quatre livrables auditables (`Tableau 27.1`, annexe des `10` clauses distinguant `EXIG-APP-13` et `EXIG-APP-14`, plan de réversibilité et test annuel `POR-016`, avenant `B2B` + anti-collusion `PRR G-14` + revue assurances) et leurs critères d'acceptation.
  - **Appui vérifié :** `matrice-exig-prr-c40.json`, `SRC-063.txt` `[1]`, `SRC-068.txt` `[2]`, `SRC-086.txt` `[3]`, `SRC-060.txt` `[4]`.
  - **Verdict : supporté**

- **C27-32 (`L116–L122`)** — *Affirmation :* Transition vers la Partie X (`→ Chapitre 28`, matrice à six verticaux coiffée par l'étalon `M-14..M-18`) et trois invariants exécutables du Chapitre 27 (banc éliminatoire `7/8`, dix clauses non dérogeables distinguant `EXIG-APP-13` et `EXIG-APP-14` / `POR-016`, maîtrise de l'écart réel ↔ apparent en `B2B` avec `PRR G-14` et audit d'assurance).
  - **Appui vérifié :** `specs/manifest.json` (`ch27`, `ch28`), `SRC-063.txt`..`SRC-114.txt` `[1..6]`.
  - **Verdict : supporté**

- **C27-33 (`CA-10` — bijection bibliographique Option A)** — *Affirmation :* Bijection stricte `100 %` entre les renvois `[1]`–`[6]` du corps narratif et `sources/ch27-sources.md` (`L1` alignée sur `manifest.json`, entrées `[1]`–`[6]` intactes).
  - **Appui vérifié :** `sources/ch27-sources.md`, `outils/verifie_manuscrit.py` (`CA-10`).
  - **Verdict : supporté**
