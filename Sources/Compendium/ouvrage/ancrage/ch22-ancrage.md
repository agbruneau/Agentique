# Journal d'ancrage atomique Wyvern G2 — Chapitre 22 (`ch22`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/08 - Partie VIII/Chapitre 22.md` (`4 799` mots de prose selon `verifie_manuscrit.count_prose_words()`, plage `[4 251, 4 989]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch22-sources.md` (`[1]`–`[8]` en statut `L+`, `2` exclusions `statut F` sur `legisquebec.gouv.qc.ca` et `genai.owasp.org`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` (`SRC-037`, `SRC-089`, `SRC-090`, `SRC-077`, `SRC-044`, `SRC-018`, `SRC-063`, `SRC-055`) ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`, `authz_pqc_audit/{otel_pii_mapper.py,audit_scitt_focus.py,slh_dsa_fips205.py}`, `tests/test_authz_pqc_audit.py`) ; repérage interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-1`
- **Passe G2 initiale (supportés)** : 13
- **Rectifications appliquées lors de la passe G2 :** 20
- **Verdict final — supportés :** 35 / 35 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 22.md`

Toutes les formulations divergentes, sur-attribuées à une source `[k]` ou issues de spécifications et bancs hors corpus `L+` fermé relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 22.md](file:///c:/Github/Agentique/Sources/Compendium/ouvrage/manuscrit/08%20-%20Partie%20VIII/Chapitre%2022.md), sans modifier le bloc scellé `CA-G0-SYNC` (`G0-EX-CH02-04`, lignes `88–121`), en préservant les invariants `CA-01`..`CA-22`, le fait `FACT-OTEL-GENAI-ATTRS`, les ancres chronologiques rattachées à `ch22`, les vedettes de glossaire (`Double couloir probatoire`, `télémétrie à double couloir`), les `owned_concepts`, les renvois `[1]`–`[8]` et le calibrage (`4 799` mots dans `[4 251, 4 989]`) :

1. **Conventions `OpenTelemetry GenAI`, `W3C Trace Context` et `NO_CONTENT` (`L11`, `L21`, `L23`, `L25`, `L29–L39`, `Tableau 22.1`) :** distinction entre le statut réel dans `SRC-089.txt` (`[2]`, `v1.41.0` : `50` `Development`, `10` `Deprecated`, `0` `Stable`) et `SRC-090.txt` (`[3]`, `85` `Development`) ; retrait des renvois `[1]` / `[1, 2]` erronés sur `W3C Trace Context` (`55` car., `ff`, `32` membres), `SEP-414` (`params._meta`), *span link*, `OTEL_SEMCONV_STABILITY_OPT_IN`, `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT=NO_CONTENT` et `{mcp.method.name}` (rattachés au cadre `EXIG-OBS-01..05`, `EXIG-OBS-10`, `Tome 2 § 10.1–10.2` et aux chapitres `07`/`14`) ; rattachement exact de `create_agent`, `invoke_agent`, `invoke_workflow` et `execute_tool` à `[1]` (`SRC-037.txt`) et du statut `Opt-In` par défaut à `[1, 2, 3]` ; qualification de `gen_ai.client.token.usage` comme métrique issue du `Tome 2 § 10.1` intégrée dans `otel_pii_mapper.py`.
2. **Provenance `AIBOM` `5+1` horloges et référentiels externes (`L13`, `L64`) :** qualification explicite du modèle à `5+1` horloges et de l'inspection des cinq référentiels (`CycloneDX 1.7`, `SPDX 3.0.1`, `in-toto`, `SLSA v1.2`, `NIST SP 800-218A`) comme relevant du relevé comparatif du traité (`Tome 1 § 47.1–47.2`, hors base `L+` fermée de ce chapitre, `[5]` mentionnant les quatre premiers à titre illustratif).
3. **Loi 25 (`LQ 2021, c. 25`), trois magasins et référence `SEC Rule 17a-4` (`L13`, `L70`–`L76`, `L133`) :** reformulation exacte des plafonds pénaux et administratifs (`10 M\$ CA` ou `2 %`, et `15 000 \$ CA` à `25 M\$ CA` ou `4 %` du chiffre d'affaires mondial précédent) selon `SRC-063.txt` (`[7]`) ; rattachement des prescriptions de rétention (`13` mois au `Tome 5 § 8.1`, `≤ 14` jours sous `EXIG-OBS-08`, `≥ 1` an sous `EXIG-CON-09`) au cadre répondant à `[7]` ; qualification explicite de `SEC Rule 17a-4` comme analogie issue des `Tome 1` et `Tome 6` hors base `L+` du chapitre.
4. **Scellage `JCS` (`RFC 8785`), `SCITT` (`RFC 9943`), `Borealis-Bench` et `SLH-DSA` (`L15`, `L137`, `L141`–`L145`, `Tableau 22.3`) :** dissociation de `RFC 8785` (`[4]`) et de l'exigence `MUST` d'`A2A` / `JWS` (`RFC 7515`) ; alignement du titre exact de `RFC 9943` (*An Architecture for Trustworthy and Transparent Digital Supply Chains*, `[5]`) et séparation entre `VDS`/`COSE` (`RFC 9942` `[5]`) et le profil Merkle binaire `0x00`/`0x01` horaire du cadre (`EXIG-OBS-12`, `audit_scitt_focus.py`) ; remplacement de l'allégation de mesure locale dans `Borealis-Bench` (dépôt absent du disque en `G0`) par le calcul arithmétique vérifié (`7 856 / 10 000 = 0,7856 ≈ 0,786` o/év.) en regard de l'ordre de grandeur rapporté au `Tome 3 § 49.5` ; rattachement de l'anonymisation `RPRP` à `EXIG-OBS-13` / `[7]` et des durées sectorielles (`24` mois, `5–7` ans `OCRI` art. `3803`, `20–40` ans) au cadre (`Tome 2 § 10.3`, `Tome 5 § 8.2`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C22-01` à `C22-35`)

### Ouverture et Section 22.1 — Titre, question directrice, introduction et résumé exécutif (`L1–L15`)

- **C22-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant l'interopérabilité télémétrique `OpenTelemetry GenAI` vers les chaînes `APM`, `SIEM` et d'audit d'entreprise malgré son instabilité, le caviardage opérationnel bilingue (`Loi 25`) et le scellage probatoire décennal `JCS`/`SCITT` + `SLH-DSA`.
  - **Appui vérifié :** `specs/manifest.json` (`ch22`, `D08`, `SUB_D08_01`), structure `§ 22.1`–`§ 22.3`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-02 (`L5`)** — *Affirmation :* Distinction entre sondes HTTP traditionnelles et défaillances silencieuses des processus d'entreprise automatisés par agents (`MCP` vers `ERP` ou `CRM`, contexte obsolète) ; risque de fuite de `RP` dans les collecteurs `APM` et `SIEM` partagés et de sanctions sévères sous la Loi 25 `[7]`.
  - **Appui vérifié :** `SRC-063.txt` (`L1542–1555`, `L2283–2333`), `Corpus/Tome 5` (`L1195`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-03 (`L7`)** — *Affirmation :* Ouverture de `D08` au gel du `2 décembre 2026`, appui amont sur `ch07`, `ch14`, `ch16` et `ch17`, intégration de `G0-EX-CH02-04` (`otel_pii_mapper.py`, barrière `G0`) et clause `non-avis` (`AO-05`) `[7, 8]`.
  - **Appui vérifié :** `specs/manifest.json` (`freeze_date: 2026-12-02`), `aq/rapports-g0.json` (`L127–133`), `SRC-055.txt` (`L13`), `SRC-063.txt`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-04 (`L11` phrases 1–2)** — *Affirmation :* Verrou 1 (`EXIG-OBS-01..13`, `PRI-013`, `CAP-042`, `CAP-049`, `ADR-021`) : aucune clé `gen_ai.*` au statut `Stable` et absence de champs de mandat (`lacune 21` du référentiel) `[1, 2, 3]`, justifiant l'émission `OTLP` vers un collecteur `v1.41.0` épinglé derrière un adaptateur bidirectionnel et quatre clés de jointure trace ↔ mandat (`EXIG-OBS-01`, `otel_pii_mapper.py`).
  - **Appui vérifié :** `SRC-089.txt` (`L16–67`, `50` `Development`, `10` `Deprecated`, `0` `Stable`), `SRC-090.txt` (`85` `Development`), `SRC-037.txt`, `otel_pii_mapper.py` (`L114–138`), `Corpus/Tome 2` (`L4740–4745`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé la formule « intégralement au statut `Development` » par l'absence de statut `Stable` et rattaché `lacune 21`, `OTLP` et l'adaptateur au cadre · **Verdict : supporté**

- **C22-05 (`L11` phrase 3)** — *Affirmation :* Selon le cadre (`EXIG-OBS-02`, `EXIG-OBS-05`, `EXIG-OBS-10`), `W3C Trace Context` emprunte `_meta` sur `MCP`, les en-têtes `A2A` et les extensions `CloudEvents`, sans `RP` dans `baggage`, avec échantillonnage en queue retenant `100,0 %` des anomalies.
  - **Appui vérifié :** `Corpus/Tome 2` (`L4760–4766`, `L4859`, `L4907–4911`), `SRC-074.txt` (`L259`), `SRC-080.txt` (`L35`).
  - **Passe initiale :** écart rectifié · **Action :** retiré le renvoi `[1]` (`SRC-037.txt` ne traitant ni de `W3C Trace Context` ni de `_meta`) et rattaché explicitement aux exigences `EXIG-OBS-02/05/10` · **Verdict : supporté**

- **C22-06 (`L13` phrases 1–2)** — *Affirmation :* Verrou 2 : modèle `AIBOM` construit dans le traité (`Tome 1 § 47.1–47.2`) en `5` constituants livrés plus une `6e` horloge de harnais, appuyé sur cinq référentiels externes (`CycloneDX 1.7`, `SPDX 3.0.1`, `in-toto`, `SLSA v1.2`, `NIST SP 800-218A`, dont les quatre premiers sont cités à titre indicatif dans `[5]`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L10732–10766`), `SRC-044.txt` (`L858–864`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié le modèle comme construction du traité et précisé le statut externe des cinq référentiels avec mention illustrative de quatre d'entre eux dans `[5]` · **Verdict : supporté**

- **C22-07 (`L13` phrase 3)** — *Affirmation :* Verrou 3 : **télémétrie à double couloir** (**Double couloir probatoire**) séparant physiquement trois magasins (`EXIG-OBS-07..09`, `EXIG-CON-09`) : couloir opérationnel `100,0 %` métadonnées caviardées `FR`/`EN` (voûte « bris de glace » purgée au plus tard à `J+14`), grand livre d'audit et dossier individuel sous clé `DEK` client répondant à la Loi 25 `[7]`.
  - **Appui vérifié :** `glossaire-termes.json` (`L103–108`), `Corpus/Tome 2` (`L4883–4972`), `SRC-063.txt` (`[7]`).
  - **Passe initiale :** écart rectifié · **Action :** explicité l'ancrage normatif du cadre (`EXIG-OBS-07..09`, `EXIG-CON-09`) en réponse à la Loi 25 `[7]` · **Verdict : supporté**

- **C22-08 (`L15`)** — *Affirmation :* Verrou 4 : grand livre `C.8` (`EXIG-OBS-11`, `EXIG-OBS-12`) à `5` éléments avant tout relais `P2`/`P3` en échec fermé, canonisés `JCS` (`RFC 8785` `[4]`) et chaînés `precedent_sha256`, ancrés au moins chaque heure hors domaine selon le profil `SCITT` (`RFC 9943`, `VDS` et reçus `COSE` `[5]`) puis rescellés tous les `≤ 5` ans en `SLH-DSA` (`NIST FIPS 205` `[6]`) sur `24` mois à `40` ans (`EXIG-OBS-13`, `EXIG-SEC-28`).
  - **Appui vérifié :** `SRC-077.txt` (`[4]`), `SRC-044.txt` (`L492–558`, `[5]`), `SRC-018.txt` (`[6]`), `audit_scitt_focus.py`, `Corpus/Tome 2` (`L4948–4970`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié les apports respectifs de `[4]`, `[5]` et `[6]` des prescriptions de périodicité et de durée propres au cadre · **Verdict : supporté**

### Section 22.2.1 — Observabilité `OpenTelemetry GenAI` et provenance `AIBOM` (`L19–L64`, Tableau 22.1, Figure 1)

- **C22-09 (`L21`)** — *Affirmation :* Volatilité `gen_ai.*` au gel du `2 décembre 2026` `[1, 2, 3]` : `v1.41.0` (`28 avril 2026`, correctif `v1.41.1` relevé au `Tome 2 § 10.1` sans modification de `gen_ai.*`) compte `60` attributs (`50` `Development`, `10` `Deprecated`, `0` `Stable`) `[2]` ; révision `244465e9` (`31 octobre 2026`) expose `85` attributs tous `Development`, renommant `cache_creation` en `cache_write` et `token.type` en `token.modality` tout en retirant notamment `gen_ai.system`, `prompt_tokens` et `completion_tokens` `[2, 3]` ; fiches spans du `5 novembre 2026` formalisant `create_agent`, `invoke_agent`, `invoke_workflow` et `execute_tool` en `Development` `[1]`.
  - **Appui vérifié :** `SRC-089.txt` (`50` Dev, `10` Depr, `0` Stable), `SRC-090.txt` (`85` Dev), `SRC-037.txt` (`L43`, `L188`, `L194`, `L668`), `faits-empiriques.json` (`FACT-OTEL-GENAI-ATTRS`), `Corpus/Tome 2` (`L4738–4744`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché `v1.41.1` au `Tome 2 § 10.1`, nuancé « notamment » pour les clés dépréciées retirées et ajouté `invoke_workflow` de `[1]` · **Verdict : supporté**

- **C22-10 (`L23`)** — *Affirmation :* Face à l'instabilité `[1, 2, 3]`, `EXIG-OBS-01`, `PRI-013`, `CAP-042`, `ADR-021` et `PRR O-01` imposent `OTLP`, consignation de version et `OTEL_SEMCONV_STABILITY_OPT_IN`, et collecteur épinglé `v1.41.0` `[2]` derrière un adaptateur bidirectionnel traduisant les `6` renommages clés (`OTEL_V141_TO_GENAI_DEV_MAP`, couvrant les attributs `[2, 3]` et la métrique `gen_ai.client.token.usage` du `Tome 2 § 10.1`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L4738–4745`, `L4853`), `otel_pii_mapper.py` (`L123–138`), `SRC-089.txt`, `SRC-090.txt`.
  - **Passe initiale :** écart rectifié · **Action :** retiré `[1, 2]` de l'exigence `EXIG-OBS-01` et explicité l'origine de la métrique client dans le `Tome 2 § 10.1` · **Verdict : supporté**

- **C22-11 (`L25`, `L27`)** — *Affirmation :* Recommandation externe `W3C Trace Context` reprise par le cadre (`EXIG-OBS-02`, `03`, `10`, `Tome 2 § 10.1`) : `traceparent` (`55` car. `v00`, rejet nul/`ff`), `tracestate` (`≤ 32`), injection dans `params._meta` sur `MCP 2026-07-28` (`SEP-414` indexé au traité) et en-têtes `A2A`/`CloudEvents`, nouveau span + *span link* aux frontières externes, identifiants `ca.entreprise.task_id` / `a2a.*` distincts de l'idempotence, et interdiction de `RP` ou secrets dans `baggage` et `tracestate`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L4750–4776`, `L4907–4913`), `SRC-074.txt` (`L259`), `SRC-080.txt` (`L35`).
  - **Passe initiale :** écart rectifié · **Action :** supprimé les trois renvois `[1]` erronés et qualifié les spécifications externes et prescriptions `Tome 2 § 10.1` · **Verdict : supporté**

- **C22-12 (`L29`–`L35`)** — *Affirmation :* Hiérarchie uniforme des spans (`EXIG-OBS-04`, `05`, `Tome 2 § 10.1`) appuyée sur `[1, 2, 3]` : `invoke_workflow` (`INTERNAL`), `invoke_agent` (`CLIENT`/`INTERNAL` `[1]` avec `gen_ai.agent.id`/`.version` `[2, 3]`), `{gen_ai.operation.name} {gen_ai.request.model}` (`response.model`, jetons, `finish_reasons` `[1, 2, 3]`), `execute_tool` (`INTERNAL` `[1]`), `{mcp.method.name} {cible}` (`CLIENT`, `Tome 2 § 10.1`), et attente `CIBA` en deux événements.
  - **Appui vérifié :** `SRC-037.txt` (`L164–259`, `L657–713`), `SRC-089.txt`, `SRC-090.txt`, `Corpus/Tome 2` (`L4780–4826`).
  - **Passe initiale :** écart rectifié · **Action :** distingué les conventions `SRC-037`/`089`/`090` des adaptations et ajouts du cadre (`Tome 2 § 10.1`) · **Verdict : supporté**

- **C22-13 (`L37`)** — *Affirmation :* Manque structurel **lacune 21** (`C30`) dans `OpenTelemetry GenAI` sans lien natif trace ↔ autorité `[1, 2, 3]` ; comblement sous `EXIG-OBS-06` (proscrivant `enterprise.` et `otel.`) via quatre clés `REQUIRED_MANDATE_JOIN_ATTRS` (`ca.entreprise.task_id`, `autonomy_level`, `approval.jti`, `cost_center`).
  - **Appui vérifié :** `SRC-037.txt`, `SRC-089.txt`, `SRC-090.txt`, `otel_pii_mapper.py` (`L96–99`, `L114–121`), `test_authz_pqc_audit.py` (`L725–742`), `Corpus/Tome 1` (`L10962`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté `[2]` avec `[1, 3]` pour le silence natif et précisé que `lacune 21` est la désignation du référentiel · **Verdict : supporté**

- **C22-14 (`L39`)** — *Affirmation :* Cinq `SLI` cognitifs du cadre (`TCR`, `TER`, tours, amplification, `HOTL`), détecteur *livelock*, *tail sampling* `100,0 %` sur erreurs/relances/plafonds/refus (`EXIG-OBS-05`), statut `Opt-In` sans capture par défaut dans `[1, 2, 3]` et réglage `OTEL_INSTRUMENTATION_GENAI_CAPTURE_CONTENT=NO_CONTENT` du `Tome 2 § 10.2`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L4859`, `L4875`), `Corpus/Tome 3` (`L18063–18070`, `L18310`), `SRC-089.txt` (`L82–108`), `SRC-090.txt` (`L160–172`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié le comportement `Opt-In` par défaut de `[1, 2, 3]` de la variable `NO_CONTENT` issue du `Tome 2 § 10.2` · **Verdict : supporté**

- **C22-15 (`L41`–`L43`, Figure 1)** — *Affirmation :* Figure 1 (`SCH-22-01.svg`) illustrant propagation `_meta` sans `RP` (`Z1`), collecteur épinglé `v1.41.0` à jointure `4` clés (`Z2`) et `AIBOM` `5+1` horloges (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch22`, `SCH-22-01`), `schemas/SCH-22-01.puml` (`L61–85`), `schemas/rendus/SCH-22-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-16 (`L45`–`L52`)** — *Affirmation :* Décomposition de l'agent en cinq constituants livrés à horloges indépendantes (poids, serveurs `MCP`, bibliothèques, invites/compétences, politiques `OPA`/`Cedar`) plus la sixième horloge propre au harnais (`5+1` horloges).
  - **Appui vérifié :** `Corpus/Tome 1` (`L10732–10746`, `L10844–10848`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-17 (`L54`–`L62`, Tableau 22.1)** — *Affirmation :* Tableau 22.1 synthétisant `OTel v1.41.0` (`60` entrées `[2]`), `semantic-conventions-genai@244465e9` (`85` attr. `[3]`), renommages, métrique client (`Tome 2 § 10.1`) incluse dans `DEFAULT_ALLOWED_ATTRS` (`G0`) et `4` clés `lacune 21`.
  - **Appui vérifié :** `SRC-089.txt` (`[2]`), `SRC-090.txt` (`[3]`), `otel_pii_mapper.py` (`L123–144`), `Corpus/Tome 2` (`L4853`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement la ligne de métrique d'usage client comme relevant du `Tome 2 § 10.1` en alias `G0` · **Verdict : supporté**

- **C22-18 (`L64`)** — *Affirmation :* Examen comparatif du traité (`Tome 1 § 47.2`, hors base `L+` fermée de ce chapitre) de `CycloneDX 1.7` (`ECMA-424` 2e éd., oct. 2025 ; `machine-learning-model`, `data`), `SPDX 3.0.1` (`AIPackage` à `15` prop. propres, `DatasetPackage` à `13` prop.), `in-toto`, `SLSA v1.2` et `NIST SP 800-218A` (quatre premiers cités dans `[5]`) ; absence native de champs d'invites/politiques/extensions déclaratives et extension `AIBOM` par attestations `SHA-256` liées à `C.8`.
  - **Appui vérifié :** `Corpus/Tome 1` (`L10754–10788`), `SRC-044.txt` (`L858–864`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement le relevé de ces spécifications au `Tome 1 § 47.2` hors base `L+` fermée, avec renvoi aux mentions illustratives de `[5]` · **Verdict : supporté**

### Section 22.2.2 — Double couloir `PII`, caviardage `FR`/`EN` et scellage `JCS`/`SCITT` + `SLH-DSA` (`L66–L151`, Tableaux 22.2, Figures 2–3, `G0-EX-CH02-04`)

- **C22-19 (`L68`–`L70`)** — *Affirmation :* Preuve directe `AO-01` sur `LQ 2021, c. 25` (`Loi 25` `[7]`), exclusion `statut F` (`HTTP 403`) de `legisquebec.gouv.qc.ca` et `genai.owasp.org` (compensée par `[8]`) ; article `12.1` en vigueur depuis le `22 septembre 2023` (avis, divulgation, rectification, révision humaine) et sanctions (art. `90.12` : jusqu'à `10 M\$ CA` ou `2 %` du chiffre d'affaires mondial antérieur ; art. `91` : `15 000 \$ CA` jusqu'à `25 M\$ CA` ou `4 %`) `[7]`.
  - **Appui vérifié :** `SRC-063.txt` (`L1542–1555`, `L2283–2333`, `L2485`), `SRC-055.txt` (`[8]`), `recherche/registre-statut-f.json` (`L40–48`, `L227–235`), `ancres-chronologiques.json` (`2026-LOI25-ART12-1`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté le plancher pénal `15 000 \$ CA` et la référence à l'exercice antérieur conformément à `SRC-063.txt` `[7]` · **Verdict : supporté**

- **C22-20 (`L72`–`L76`)** — *Affirmation :* Séparation physique en trois magasins (`EXIG-OBS-07..13`, `EXIG-CON-09`, `PRR O-02`) en réponse à `[7]` : (1) couloir `1` sans texte brut (`EXIG-OBS-07`), `HMAC-SHA256`, rétention indicative `13` mois (`Tome 5 § 8.1`) et voûte « bris de glace » sous double accord purgée à `≤ 14` jours (`EXIG-OBS-08`, tranchant `14–30` j de `C27`) ; (2) grand livre `WORM` `C.8` en échec fermé (`EXIG-OBS-11`) ; (3) dossier `art. 12.1` `≥ 1` an sous clé `DEK` client effaçable (`EXIG-CON-09` `[7]`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L4883–4972`), `Corpus/Tome 5` (`L1201–1212`), `SRC-063.txt` (`[7]`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché la rétention indicative `13` mois au `Tome 5 § 8.1` et l'exigence de dossier individuel à `[7]` · **Verdict : supporté**

- **C22-21 (`L78`–`L80`, Figure 2)** — *Affirmation :* Figure 2 (`SCH-22-02.svg`) montrant couloir `1` caviardé `FR`/`EN` (`Z1`), voûte « bris de glace » à purge `J+14` (`Z2`) et dossier `art. 12.1` sous clé `DEK` effaçable (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch22`, `SCH-22-02`), `schemas/SCH-22-02.svg` (`L1–94`), `schemas/rendus/SCH-22-02.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-22 (`L82`–`L84`)** — *Affirmation :* Double barrière déterministe (`EXIG-OBS-09`) : `map_span_attributes` applique `DEFAULT_ALLOWED_ATTRS`, rejette `enterprise.`/`otel.`, exige les `4` clés `lacune 21`, supprime `approver`/`approbateur` et purge `9` attributs bruts ; `redact_pii_bilingual` applique `7` regex ordonnées (`BEARER_JWT`, `IBAN`, `PAYMENT_CARD`, `EMAIL`, `RAMQ`, `PHONE`, `NAS_SIN`) produisant `[CATEGORIE:hex12]` via `HMAC-SHA256`.
  - **Appui vérifié :** `otel_pii_mapper.py` (`L90–175`), `test_authz_pqc_audit.py` (`L703–816`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-23 (`L86`–`L123`, `G0-EX-CH02-04`)** — *Affirmation :* Extrait scellé `CA-G0-SYNC` `G0-EX-CH02-04` (`otel_pii_mapper.py`, lignes `235–265`, `sha256="60bd160c1a507c6df31fd1dfc3811c866a6f17e8b623e961b2511c00c7e41889"`) vérifié en `G0`, et complémentarité avec l'exclusion de base `EXIG-OBS-07`.
  - **Appui vérifié :** `aq/rapports-g0.json` (`L127–133`), `otel_pii_mapper.py` (`L234–266`), `verifie_manuscrit.py` (`CA-20` exit 0).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-24 (`L125`–`L131`, Tableau 22.2)** — *Affirmation :* Tableau 22.2 synthétisant les trois magasins réglementés (rôles, protections et durées de rétention/purge).
  - **Appui vérifié :** `Corpus/Tome 2` (`L4883–4972`), `Corpus/Tome 5` (`L1208–1212`), `SRC-063.txt` (`[7]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-25 (`L133`–`L135`)** — *Affirmation :* Interdiction de l'auto-journalisation face à l'injection indirecte (`OWASP ASI01` `[8]`, analogie `SEC Rule 17a-4` issue des `Tome 1` et `Tome 6`), écriture `C.8` par la `PEP` en échec fermé (`EXIG-OBS-11`), et `5` éléments obligatoires (`EXIG-OBS-12`) + `sequence`, `flux`, `horodatage`, `precedent_sha256` (`64` zéros initiaux) et corrélation `trace_id`/`span_id`/`UETR`/idempotence.
  - **Appui vérifié :** `SRC-055.txt` (`L50`, `ASI01`), `audit_scitt_focus.py` (`L15`, `L56–79`), `test_authz_pqc_audit.py` (`L819–877`), `Corpus/Tome 1` (`L7299`), `Corpus/Tome 2` (`L4921–4960`), `Corpus/Tome 6` (`L4394`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement l'analogie `SEC Rule 17a-4` aux `Tome 1` et `Tome 6` hors base `L+` de ce chapitre · **Verdict : supporté**

- **C22-26 (`L137`–`L139`)** — *Affirmation :* Canonisation `JCS` (`RFC 8785`, juin 2020 `[4]` : tri `UTF-16`, suppression des espaces, sérialisation ECMAScript des nombres sans `NaN`/`Infinity`, `I-JSON`), emploi sur `MCP`/`Saga`/`C.6` et soutien à l'exigence `MUST` d'`A2A` + `JWS` (`RFC 7515`, `← ch08, ch16`), ainsi que détection locale `broken_sequence` via `AuditChainLedger.verify_chain`.
  - **Appui vérifié :** `SRC-077.txt` (`L3–9`, `L180–360`), `SRC-083.txt` (`L2008`), `audit_scitt_focus.py` (`L81–133`), `test_authz_pqc_audit.py` (`L934–991`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié `RFC 8785` `[4]` de l'exigence `MUST` d'`A2A` / `RFC 7515` · **Verdict : supporté**

- **C22-27 (`L141`–`L143`)** — *Affirmation :* Couche de transparence **SCITT** (`RFC 9943`, *Standards Track*, juin 2026, « An Architecture for Trustworthy and Transparent Digital Supply Chains » `[5]`, `VDS` en ajout seul et reçus `COSE` `RFC 9942`) ; profil du cadre (`EXIG-OBS-12`, `audit_scitt_focus.py`) à arbre binaire de Merkle horaire (`0x00`/`0x01`), preuve logarithmique \(O(\log N)\), amortissement arithmétique `7 856 / 10 000 = 0,7856 ≈ 0,786` o/év. (ordre de grandeur rapporté pour `Borealis-Bench` au `Tome 3 § 49.5`, absent du disque en `G0`) et anonymisation par suppression dans la table `RPRP` (`EXIG-OBS-13`, Loi 25 `[7]`).
  - **Appui vérifié :** `SRC-044.txt` (`L3–38`, `L492–558`, `L586–606`), `audit_scitt_focus.py` (`L136–226`), `SRC-018.txt` (`L2491`), `Corpus/Tome 3` (`L26901`), `Corpus/Tome 2` (`L4968`), `SRC-063.txt` (`[7]`).
  - **Passe initiale :** écart rectifié · **Action :** rectifié le titre exact de `RFC 9943`, séparé `VDS`/`COSE` `[5]` du profil Merkle `0x00`/`0x01`, remplacé l'allégation de mesure locale dans `Borealis-Bench` par l'amortissement arithmétique et son statut absent du disque, et rattaché l'anonymisation `RPRP` à `EXIG-OBS-13` / `[7]` · **Verdict : supporté**

- **C22-28 (`L145`)** — *Affirmation :* Rétentions sectorielles du traité (`Tome 2 § 10.3`, `Tome 5 § 8.2`) : `24` mois min (`EXIG-OBS-13`), `5–7` ans bancaire/`OCRI` art. `3803`, `20–40` ans vie/rentes ; croisement avec cycles `TLS` (`15 mars 2027`, `15 mars 2029`) et feuille de route `G7` `2030–2035` (`← ch18`), et rescellement `≤ 5` ans (`EXIG-SEC-28`, `PRR G-15`) en **SLH-DSA** (`NIST FIPS 205`, `13 août 2024` `[6]`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L4720`, `L4968`), `Corpus/Tome 5` (`L105`, `L1211`), `ancres-chronologiques.json`, `SRC-018.txt` (`L12`, `L28–39`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché les durées sectorielles au traité et scindé la phrase pour respecter le plafond `≤ 70` mots de `CA-05` · **Verdict : supporté**

- **C22-29 (`L147`)** — *Affirmation :* Choix de `SLH-DSA-SHA2-128s` (`7 856` o, clé publique `32` o) contre `128f` (`17 088` o) `[6]`, implémentation Python pur sous licence `MIT` (`slh_dsa_fips205.py`) et validation `G0` sur `20` vecteurs `rfc8785` et `12` vecteurs `NIST FIPS 205 ACVP` `[4, 6]`.
  - **Appui vérifié :** `SRC-018.txt` (`L2481–2501`), `slh_dsa_fips205.py` (`L1–40`), `aq/rapports-g0.json` (`L13–18`, `L51–63`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-30 (`L149`–`L151`, Figure 3)** — *Affirmation :* Figure 3 (`SCH-22-03.png`) représentant l'enregistrement `C.8` et la canonisation `JCS` (`Z1`), le chaînage `WORM` + ancrage `SCITT` horaire (`Z2`) et le rescellement `SLH-DSA` tous les `≤ 5` ans (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch22`, `SCH-22-03`), `schemas/SCH-22-03.mmd` (`L1–21`), `schemas/rendus/SCH-22-03.png`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 22.3 — Synthèse architecturale, livrables, interfaces et invariants (`L153–L169`, Tableau 22.3, Encadré)

- **C22-31 (`L155`)** — *Affirmation :* Interfaces amont (`ch07`, `ch14`, `ch15`, `ch16`, `ch17`, `ch18`) et aval (`ch19`, `ch23`, `ch24`, `ch25`, `ch26`, `ch34`, `ch35`) respectant la partition bijective `CA-21` du domaine `D08`.
  - **Appui vérifié :** `specs/manifest.json` (`ch22.owned_concepts`), `verifie_manuscrit.py` (`CA-21`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-32 (`L157`–`L163`, Tableau 22.3)** — *Affirmation :* Tableau 22.3 des trois livrables d'ingénierie, exigences normatives et critères exécutables `G0`–`G1` (`otel_pii_mapper.py`, `audit_scitt_focus.py` + `slh_dsa_fips205.py` avec amortissement théorique `0,786` o/év. sur `10 000` év., et inventaire `AIBOM` / purge `≤ 14` j / `DEK` `≥ 1` an `[1–7]`).
  - **Appui vérifié :** `aq/rapports-g0.json`, `otel_pii_mapper.py`, `audit_scitt_focus.py`, `slh_dsa_fips205.py`, `SRC-089/090/037/077/044/018/063`.
  - **Passe initiale :** écart rectifié · **Action :** qualifié l'amortissement `0,786` o/év. de théorique sur `10 000` événements en ligne 2 · **Verdict : supporté**

- **C22-33 (`L165`–`L169`, Trois invariants)** — *Affirmation :* Encadré final des trois invariants exécutables du Chapitre 22 (`OTel v1.41.0` + `4` clés `ca.entreprise.*`, double couloir `PII` `FR`/`EN` + purge `≤ 14` j + dossier `DEK` `art. 12.1`, et grand livre `C.8` `JCS` `RFC 8785` + `SCITT` `RFC 9943` + `SLH-DSA` `FIPS 205` `≤ 5` ans).
  - **Appui vérifié :** `verifie_manuscrit.py` (`CA-04` exit 0), `otel_pii_mapper.py`, `audit_scitt_focus.py`, `slh_dsa_fips205.py`, `SRC-077`, `SRC-044`, `SRC-018`, `SRC-063`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C22-34 (`REV-04`, `PRD-L3-009/010`, `PRD-L4-002`)** — *Affirmation :* Intégration des repères secondaires PRD (`PRIN-06`, lacune flotte `F-96`, `FINOS AI Governance v2.0` et `watsonx.governance` qualifiés hors base `L+` du chapitre, `PRR R-07` sur `JCS`), correction `SCH-22-02.svg` (`Rend`) et `SCH-22-01.puml` (`60 ↔ 85 attr. gen_ai.*`, `horloge harnais`), nettoyage `\$` dans backticks (`10 M$ CA`, `15 000 $ CA`, `25 M$ CA`) et numérotation `Figure 70`..`Figure 72`.
  - **Appui vérifié :** `Compendium/prd.md` (`L4134–4168`), `schemas/SCH-22-01.puml`, `schemas/SCH-22-02.svg`, `SRC-063.txt`, `SRC-077.txt`.
  - **Passe REV-04 :** intégré et vérifié · **Verdict : supporté**

- **C22-35 (`L1–L13`, `L17`, `L27`, `L37`, `L60`, `L72`, `L128`, `L145`, `L155–L157`)** — *Affirmation :* Interopérabilité télémétrique de bout en bout (`W3C Trace Context` reliant portail métier, agent, `PEP`, `MCP` et requêtes `REST`/`SQL` sur `ERP`, `CRM`, `ITSM` ; quatre clés `ca.entreprise.*` de `G0-EX-CH02-04` préservé à l'octet) vers les collecteurs `APM` (`Datadog`, `Dynatrace`, `Grafana Tempo`, `Elastic` qualifiés hors `L+`), les corrélateurs `SIEM` (`Sentinel`, `Splunk` hors `L+`), l'`ITSM` et les outils `ITFM`/`ERP` (`cost_center`) ; séparation des droits entre exploitants `SRE`/`APM`/`SIEM` et auditeurs habilités (`Loi 25` art. `12.1` `[7]`, clé `DEK` sous `KMS`) ; et élargissement multisectoriel des durées probatoires `WORM` (`6–7` ans fiscal `ERP`, `5–7` ans `OCRI`, `10–25` ans clinique/pharma, `10–30` ans industriel, `20–40` ans vie/rentes) articulé avec l'échéance `fin 2028` et `SLH-DSA` `[6]`.
  - **Appui vérifié :** `specs/manifest.json` (`ch22.title`), `otel_pii_mapper.py`, `ancres-chronologiques.json` (`fin 2028`), `SRC-089.txt` `[2]`, `SRC-090.txt` `[3]`, `SRC-018.txt` `[6]`, `SRC-063.txt` `[7]`, `Corpus/Tome 2` (`§ 10.1–10.3`), `Corpus/Tome 5` (`§ 8.1–8.2`).
  - **Adaptation interopérabilité et automatisation d'entreprise :** intégré et vérifié · **Verdict : supporté**
