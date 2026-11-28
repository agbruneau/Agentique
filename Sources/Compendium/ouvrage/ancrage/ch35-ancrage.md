# Journal d'ancrage atomique Wyvern G2 — Chapitre 35 (`ch35`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/12 - Partie XII/Chapitre 35.md` (`4 210` mots de prose `verifie_manuscrit` / `4 499` mots `parser_plan`, plage `[3 726, 4 374]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch35-sources.md` (`[1]`–`[11]` en statut `L+`, `2` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) et code de la trousse `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/` ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b5-6`
- **Passe G2 initiale (supportés)** : 15
- **Rectifications appliquées lors de la passe G2 :** 20
- **Verdict final — supportés :** 35 / 35 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 35.md`

Toutes les formulations divergentes, attributions erronées ou confusions de périmètre relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 35.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/12%20-%20Partie%20XII/Chapitre%2035.md), sans altérer le bloc scellé `CA-G0-SYNC` `G0-EX-CH04-01` (`L82–L112`), en préservant les invariants `CA-01`..`CA-22`, les `owned_concepts` (`barriere-logicielle-g0-execute-g0`, `trousse-executable-tome-8`, `cinq-blocs-sbb-tableau-12`, `calibration-feds-ema`, `contrats-types-executes-ci-annexe-c`), l'ensemble des renvois `[1]`–`[11]` et le calibrage (`4 210` / `4 499` mots dans `[3 726, 4 374]`) :

1. **Verrous `G0`, `requirements.lock`, `schemas_checked` et paquet `slh-dsa` (`L11`, `L13`, `L34`, `Tableau 35.1`, `Tableau 35.3`, `L163`) :** correction du décompte de `requirements.lock` (`17` paquets verrouillés `--require-hashes` contre `18` distributions Python inspectées dans `.venv` dont `pip`) ; séparation dans les `21` validations de `aq/rapports-g0.json` entre les `13` schémas `JSON Schema Draft 2020-12` (`[1]`) et les `8` contrôles de registres de gouvernance ; précision du chemin réel sur disque (`Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/`) ; dissociation de l'exclusion du paquet PyPI `slh-dsa` (`LGPL-3.0-or-later`, spécification interne `G0` hors corpus `L+`) d'avec le renvoi `[4]` (`NIST FIPS 205`, qui fonde `slh_dsa_fips205.py`).
2. **Chemins, symboles et comportement des `5 SBB` du `Tableau 12` (`L5`, `L60`, `Tableau 35.2`, `Tableau 35.3`) :** correction du chemin erroné `policies_opa/opa_runner.py` en `policy_saga/opa_runner.py` (couplé aux paquets `.rego` `rule_of_two.rego` et `camel_taint.rego`) ; reformulation du rôle de `validate_obo_delegation` (`obo_dpop.py`, liaison `DPoP`/`cnf` éliminant les secrets statiques et rejetant `passthrough`, `> 2` sauts ou absence de preuve `DPoP`) ; ajout des symboles exacts `compute_action_hash_h` (`ciba_approval.py`), `build_scitt_merkle_tree` et `seal_merkle_root` (`audit_scitt_focus.py`, `SLH-DSA-SHA2-128s`), ainsi que `audit_scitt_focus.py (compute_cpo_and_focus)` aux côtés de `decimal_money.py` (`TypeError` sur `float`/`bool`) ; précision que les `5 SBB` étaient « sans exemple retenu » au `Tableau 12` (`Corpus/Tome 2`).
3. **Simulation synthétique `FEDS`/`EMA` sous `DC-P12` (`L120`, `L123`, `L124`, `L126`, `L128`) :** qualification du terme impropre `seuil empirique X34 ≥ 0,386` en `seuil simulé X34 ≥ 0,386` (cohérence stricte avec `DC-P12`) ; précision que `99,921 %` (`99,50 %`) et `99,812 %` (`99,08 %`) sont des médianes simulées `p50` ; ajout de `p99 = 11 034,19 ms` sur la traîne `POR-003` ; dissociation de `[4]` (`FIPS 205` pour `SLH-DSA-128s`) d'avec le volume simulé `22,48 Mo` ; alignement des profils patrimoniaux (`plafond L2 sur le conseil`) et groupe diversifié (`52/52` capacités) sur le Chapitre 28 et le Tome 4.
4. **Contrats `C.1`–`C.8` et calendrier réglementaire (`L15`, `L130`–`L139`, `Figure 3`, `Tableau 35.3`, `L165`) :** distinction entre les six contrats `[Exécuté en CI]` (`C.1`–`C.4`, `C.7`, `C.8`) et les deux contrats `[Schéma conceptuel]` (`C.5`, `C.6`, `DC-P11`) ; restriction du scénario d'achat de `12 480 \$` (`agt-achats-indirects@1.2.0`, `N3`, seuil `5 000 \$`) aux cinq contrats concernés (`C.1`, `C.2`, `C.6`, `C.7`, `C.8`) ; mention de `RFC 7493` pour `I-JSON` et scission de `L130` selon `CA-05` ; rectification de l'échéance de l'Annexe III de l'`EU AI Act` en **`à partir du 2 décembre 2027`** (`SRC-061.txt`) et rattachement des ancres réglementaires au registre `SSOT` (`ancres-chronologiques.json`) en réservant `[3, 4]` à la fenêtre post-quantique `G7` `2030–2035`.
5. **Adaptation éditoriale au titre directeur *Interopérabilité et automatisation agentique des systèmes d'entreprise* (`L1`, `L3`, `L5`, `L17`–`L22`, `L124`–`L126`, `L151`) :** synchronisation exacte de `L1` sur `specs/manifest.json` (`ch35`), regroupement explicite des `4` paquets `MIT` selon le diptyque **médiation d'interopérabilité vérifiable** (`harness_proto/`, `authz_pqc_audit/`) et **confinement déterministe de l'automatisation** (`policy_saga/` + `policies_opa/`, `evalops_prr/`), maintien intact à l'octet près de `G0-EX-CH04-01` (`L78–L108`, `wilson_bounds.py`), et mise en valeur de la portée multisectorielle des `8` contrats `C.1–C.8` (scénario d'achat indirect *Source-to-Pay* de `12 480 $` sous double visa `C.6`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C35-01` à `C35-35`)

### Section 35.0 — Titre, question directrice et ouverture (`L1–L7`)

- **C35-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant la matérialisation des invariants d'interopérabilité protocolaire (`MCP`, `A2A`, `JCS`, `OBO`) et d'automatisation déterministe (`Harnais 80/20`, `OPA/Rego`, `Saga`, `CIBA`, `EvalOps`) en une trousse Python/OPA portable exécutant les `5 SBB`, les vecteurs tiers, la barrière `G0` et les contrats `C.1–C.8`.
  - **Appui vérifié :** `specs/manifest.json` (`ch35`, `D12`, `SUB_D12_02`), `registre/matrice-exig-prr-c40.json` (`cinq_sbb`, `EXIG-EXEC-01`..`06`).
  - **Passe initiale :** conforme · **Action :** aligné sur `manifest.json` (Vague 2) · **Verdict : supporté**

- **C35-02 (`L5`)** — *Affirmation :* Dans les sept premiers tomes, la validation des harnais, les cinq blocs du `Tableau 12` demeurés sans exemple retenu et `Borealis-Bench` (consigné au Corpus hors dépôt local, ← Chapitre 29) ne disposaient pas d'implémentation exécutable sur disque ; la trousse `MIT` du Tome 8 convertit ces invariants en tests portables.
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 12`, `L1360–L1361`), `Tomes/Tome 8 .../manuscrit/00 - Liminaire.md` (`L7–L9`), `Tomes/Tome 8 .../trousse/LICENSE` (`MIT`), `Chapitre 29.md` (`L135`).
  - **Passe initiale :** écart rectifié · **Action :** précisé « sans exemple retenu au `Tableau 12` » et rappelé que `Borealis-Bench` est consigné au Corpus hors dépôt local · **Verdict : supporté**

- **C35-03 (`L7`)** — *Affirmation :* Sous démarcation `DC-01` et `DC-P12`, la trousse et le banc s'exécutent hors ligne sur doublures hermétiques (*mock MCP servers*) sans réseau, modèle payant, essai humain ni `SoR` réel ; résultats arrêtés au gel du `2 décembre 2026` sous clause `non-avis` (`AO-05`).
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/README.md` (`L5–L7`), `specs/protocole-mlr-compendium.json`, `sources/ch35-sources.md` (`L4–L5`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 35.1 — Résumé exécutif : architecture bicéphale et barrière `G0` (`L9–L15`)

- **C35-04 (`L11`)** — *Affirmation :* Architecture bicéphale séparant la tête éditoriale `CC BY 4.0` (extraits `≤ 40` lignes) du corps `MIT` `8 - Manuel/trousse/` (archivé dans `Tomes/Tome 8 .../trousse/`) en `Python 3.12+` et `OPA/Rego v1.22.4` `[9, 10]` avec `JSON Schema Draft 2020-12` `[1]`, reliés par `CA-G0-SYNC` (`14` extraits vérifiés octet pour octet en `SHA-256` contre `aq/rapports-g0.json`).
  - **Appui vérifié :** `SRC-021.txt` `[1]`, `SRC-087.txt` `[9]`, `SRC-088.txt` `[10]`, `Tomes/Tome 8 .../trousse/pyproject.toml`, `aq/rapports-g0.json` (`L77–L175`).
  - **Passe initiale :** écart rectifié · **Action :** précisé le chemin réel d'archivage `Tomes/Tome 8 .../trousse/` dans le dépôt · **Verdict : supporté**

- **C35-05 (`L13`)** — *Affirmation :* `execute_g0.py` (`Windows`/`Linux`, `exit 0` sans privilège hôte) exclut `Rust`, `Go`, `Firecracker`/`KVM`, `Postgres`, `OpenFGA` et `Cedar`, et atteste au `2 décembre 2026` : `83/83` `pytest` (`0` échec, `0` ignoré), `45/45` `OPA/Rego` (`100,0 %`, `default allow := false` `[9, 10]`), `13` schémas `Draft 2020-12` `[1]` et `8` validations de registres (`21` contrôles sans violation), `17` paquets `SHA-256` dans `requirements.lock`, `SPDX MIT` sur `50` fichiers et `18` distributions Python inspectées avec rejet `LGPL`.
  - **Appui vérifié :** `aq/rapports-g0.json` (`L11–L50`), `Tomes/Tome 8 .../trousse/requirements.lock` (`17` paquets), `spdx-allowlist.json`, `SRC-021.txt` `[1]`, `SRC-087.txt` `[9]`, `SRC-088.txt` `[10]`.
  - **Passe initiale :** écart rectifié · **Action :** corrigé `18` en `17` paquets verrouillés dans `requirements.lock` face aux `18` distributions inspectées dans `.venv`, et dissocié les `13` schémas des `8` validations de registres composant les `21` contrôles · **Verdict : supporté**

- **C35-06 (`L15`)** — *Affirmation :* Contre-épreuve sur `50` fichiers de `4` suites tierces (`RFC 8785` `[7]`, `NIST ACVP` `FIPS 204` `[3]` / `FIPS 205` `[4]`, `a2a-tck 1.0.0.alpha3` `[8]`, `OWASP` `[5]`), implémentation des `5 SBB` du `Tableau 12`, banc `feds-ema/` (`DC-P12`, `C07 = 65,0 %`) et examen des `8` contrats `C.1`–`C.8` de l'Annexe C (`6` `[Exécuté en CI]` + `2` `[Schéma conceptuel]` à chaîne canonique vérifiée `[1, 3, 6, 7, 8]`).
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/vectors/vectors-manifest.json`, `SRC-021.txt` `[1]`, `SRC-050.txt` `[3]`, `SRC-018.txt` `[4]`, `SRC-055.txt` `[5]`, `SRC-072.txt` `[6]`, `SRC-077.txt` `[7]`, `SRC-086.txt` `[8]`, `Corpus/Tome 2` (`L7012`).
  - **Passe initiale :** écart rectifié · **Action :** précisé la répartition `6 [Exécuté en CI]` / `2 [Schéma conceptuel]` et ajouté le renvoi `[8]` pour `C.3` · **Verdict : supporté**

### Section 35.2.1 — Trousse `MIT`, `4` paquets, vecteurs tiers et `5 SBB` (`L19–L76`, Tableaux 35.1–35.2, Figures 1–2)

- **C35-07 (`L21`, `L23`)** — *Affirmation :* Quatre paquets `MIT` ; `harness_proto/` implémente la partition `80/20` et le harnais en `8` étapes (`pipeline.py`), `JSON Schema Draft 2020-12` `[1]`, l'épinglage `JCS SHA-256` et en-têtes `MCP 2026-07-28` (`mcp_pinning.py` `[6, 7]`), et l'enveloppe signée `AgentCard` sous `A2A v1.0.1` (`a2a_card.py` `[8]`).
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/harness_proto/` (`pipeline.py`, `mcp_pinning.py`, `a2a_card.py`), `SRC-021.txt` `[1]`, `SRC-072.txt` `[6]`, `SRC-077.txt` `[7]`, `SRC-086.txt` `[8]`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-08 (`L24`)** — *Affirmation :* `authz_pqc_audit/` implémente `OBO` `≤ 2` sauts sans relais (`obo_dpop.py`), `CIBA` liée au hachage d'action (`ciba_approval.py`), le banc `HTTP 431` (`pqc_http431.py`) avec tailles `FIPS 204` (`ML-DSA-65` `3 309` o, `ML-DSA-87` `4 627` o `[3]`) opposant la croissance `O(sauts)` (`JWT_EMBEDDED_JWK` `8 298` o, `JWT_X5C_CHAIN` `14 139` o dès `1` saut en `ML-DSA-65` ; `JWT_KID_REF` `9 624` o, `CBOR_COSE_CWT` `9 413` o dès `2` sauts en `ML-DSA-65`, et `13 140`/`12 928` o en `ML-DSA-87`) aux `Transaction Tokens` invariants `O(1)` (`4 778`/`4 757` o `ML-DSA-65` ; `6 536`/`6 514` o `ML-DSA-87`, `HTTP 200` face au plafond `8 192` o `[3, 7]`), le caviardage `OTel`/`PII` (`otel_pii_mapper.py`) et `JCS` + `SCITT` rescellé `SLH-DSA` (`audit_scitt_focus.py` `[4, 7]`).
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/authz_pqc_audit/` (`obo_dpop.py`, `ciba_approval.py`, `pqc_http431.py` exécuté dans `.venv`, `audit_scitt_focus.py`), `SRC-050.txt` (`L1317`, `L1321`, `[3]`), `SRC-018.txt` `[4]`, `SRC-077.txt` `[7]`.
  - **Passe initiale :** conforme · **Action :** ajoutées les mesures exactes `pqc_http431.py` de `1` à `5` sauts (`post-G4`) · **Verdict : supporté**

- **C35-09 (`L25`, `L26`)** — *Affirmation :* `policy_saga/` & `policies_opa/` hébergent `rule_of_two.rego`, `camel_taint.rego` et le confinement sous `OPA v1.22.4` `[9, 10]`, `OpaPolicyEngine`, `decimal_money.py` et `saga_orchestrator.py` ; `evalops_prr/` regroupe `mock_mcp_harness.py`, `wilson_bounds.py` `[2, 11]`, `metamorphic.py` (`4` relations FR/EN) et `prr_validators.py` (`24` portes bloquantes `PRR-75`, `ADR 2027-B001`, `C01–C40`).
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/{policy_saga,policies_opa,evalops_prr}/`, `SRC-022.txt` `[2]`, `SRC-087.txt` `[9]`, `SRC-088.txt` `[10]`, `SRC-094.txt` `[11]`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-10 (`L28`)** — *Affirmation :* `policy_saga/saga_orchestrator.py` persiste une machine à états sous `SQLite WAL` avec `CompensationChannel` isolé et passe `10` scénarios déterministes d'injection de fautes dans `tests/test_saga_10_faults.py`.
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/policy_saga/saga_orchestrator.py` (`L87`, `PRAGMA journal_mode = WAL`), `tests/test_saga_10_faults.py`, `aq/rapports-g0.json` (`L47`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-11 (`L30`)** — *Affirmation :* `rule_of_two.rego` et `camel_taint.rego` appliquent la sémantique Datalog d'`OPA v1.22.4` `[9]` et sont éprouvés par tests négatifs sous `opa test --coverage --format=json` `[10]` pour garantir un rejet fermé plutôt qu'une évaluation indéfinie.
  - **Appui vérifié :** `policies_opa/{rule_of_two,camel_taint}.rego`, `SRC-087.txt` (`L80–99`, `L2072–2103`, `[9]`), `SRC-088.txt` `[10]`, `aq/rapports-g0.json` (`L31–37`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-12 (`L32`)** — *Affirmation :* `metamorphic.py` vérifie `4` relations métamorphiques FR/EN sans oracle externe et `prr_validators.py` contrôle `24` portes bloquantes `PRR-75`, `5 SBB`, le schéma `Adr2027B001` `[1]` et les `40` critères `C01–C40`.
  - **Appui vérifié :** `evalops_prr/{metamorphic,prr_validators}.py`, `schemas/adr_2027_b001.schema.json`, `SRC-021.txt` `[1]`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-13 (`L34`)** — *Affirmation :* Vérification `--require-hashes` des `17` paquets verrouillés dans `requirements.lock`, audit `SPDX` sur les `18` distributions Python inspectées dans `.venv` et `50` fichiers sources, rejet `GPL`/`AGPL`/`LGPL`/`SSPL`, et proscription du paquet tiers `slh-dsa` (`LGPL-3.0-or-later`, spécification interne `G0` hors `L+`) au profit de `authz_pqc_audit/slh_dsa_fips205.py` (`MIT`) conforme à `FIPS 205` `[4]`.
  - **Appui vérifié :** `requirements.lock` (`17` paquets), `.venv` (`18` distributions dont `pip`), `spdx-allowlist.json`, `Tomes/Tome 8 .../specs/architecture-trousse-g0.md` (`L110`), `slh_dsa_fips205.py`, `SRC-018.txt` `[4]`.
  - **Passe initiale :** écart rectifié · **Action :** corrigé `18` -> `17` paquets dans `requirements.lock` face aux `18` distributions `SPDX`, et dissocié le renvoi `[4]` (`FIPS 205`) de l'exclusion PyPI `slh-dsa` · **Verdict : supporté**

- **C35-14 (`L36`–`L40`, `Figure 1`)** — *Affirmation :* `CA-G0-SYNC` scelle `14` extraits (`G0-EX-CH01-01` à `G0-EX-CH04-03`, `≤ 40` L, `SHA-256` `LF`) contre `aq/rapports-g0.json` ; la `Figure 1` (`SCH-35-01.svg`) synthétise l'architecture bicéphale.
  - **Appui vérifié :** `aq/rapports-g0.json` (`L77–175`), `schemas/SCH-35-01.puml`, `schemas/rendus/SCH-35-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-15 (`L42`–`L47`)** — *Affirmation :* `4` suites tierces (`vectors-manifest.json`, `50` fichiers) : `rfc8785` (`20`, UTF-16/ECMAScript `[7]`), `nist_acvp` (`12`, `FIPS 204`/`205` du `13 août 2024` `[3, 4]`), `a2a_tck` (`5`, `a2a-tck v1.0.0.alpha3` du `20 octobre 2026`, `5daf0144`, `CARD-SIGN-001`..`004` `NOT_AUTOMATABLE` et `conformance-vectors/a2a-jcs-v01` absent dans `tck/requirements/agent_card.py` `[8]`), `owasp_src055` (`13`, `ASI01`–`ASI10`, *OWASP Top 10 for Agentic Applications 2026* `Version 2026`, déc. 2025 `[5]`, `genai.owasp.org` en statut `F` `HTTP 403`).
  - **Appui vérifié :** `vectors-manifest.json`, `SRC-077.txt` `[7]`, `SRC-050.txt` `[3]`, `SRC-018.txt` `[4]`, `SRC-086.txt` (`L133–184`, `[8]`), `SRC-055.txt` (`L1–120`, `[5]`), `registre-statut-f.json` (`L40–48`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-16 (`L49`–`L58`, `Tableau 35.1`)** — *Affirmation :* Le `Tableau 35.1` consigne le bilan `G0` (`83/83` `pytest` sur `6` modules, `45/45` `OPA 100,0 %` sur `3` `.rego` `[9, 10]`, `13` schémas `[1]` + `8` contrôles de registres = `21` validations, `50` fichiers `SPDX MIT` + `17` paquets verrouillés / `18` distributions, `50/50` vecteurs tiers `[3, 4, 5, 7, 8]` dont `CARD-SIGN-001..004` `NOT_AUTOMATABLE` compensés par `a2a_card.py`, `14/14` `CA-G0-SYNC`).
  - **Appui vérifié :** `aq/rapports-g0.json` (`L11–76`), `requirements.lock`, `harness_proto/a2a_card.py`, `vectors/a2a_tck/a2a_tck_must_requirements.json`, `SRC-021.txt`, `SRC-050.txt`, `SRC-018.txt`, `SRC-055.txt`, `SRC-077.txt`, `SRC-086.txt`, `SRC-087.txt`, `SRC-088.txt`.
  - **Passe initiale :** écart rectifié · **Action :** ajouté `8 contrôles de registres`, aligné `17` paquets épinglés / `18` distributions inspectées et rappelé au `Tableau 35.1` la limite `NOT_AUTOMATABLE` compensée par `a2a_card.py` (lissage G5) · **Verdict : supporté**

- **C35-17 (`L60`–`L66`, `Figure 2`)** — *Affirmation :* Résolution de la lacune des `5 SBB` demeurés sans exemple retenu au `Tableau 12` (`Plan A` `3`, `Plan B` `2`), illustrée en `Figure 2` (`SCH-35-02.svg`) ; rejet `TypeError` sur `float`/`bool` et neutralisation de l'évaluation indéfinie `Rego` via `default allow := false` et couverture `100,0 %` (`opa test --coverage --format=json` `[9, 10]`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L1360–L1361`), `schemas/SCH-35-02.puml`, `decimal_money.py` (`L24–27`), `SRC-087.txt` `[9]`, `SRC-088.txt` `[10]`.
  - **Passe initiale :** écart rectifié · **Action :** précisé « sans exemple retenu ni code compagnon exécutable » · **Verdict : supporté**

- **C35-18 (`L68`–`L76`, `Tableau 35.2`)** — *Affirmation :* Le `Tableau 35.2` relie les `5 SBB` à leurs modules et symboles exacts : `obo_dpop.py` (`validate_obo_delegation`), `policy_saga/opa_runner.py` (`OpaPolicyEngine`) + `policies_opa/{rule_of_two,camel_taint}.rego` `[9, 10]`, `ciba_approval.py` (`compute_action_hash_h`, `verify_ciba_approval_tokens` `[7]`), `audit_scitt_focus.py` (`AuditChainLedger`, `build_scitt_merkle_tree`, `seal_merkle_root`, `SLH-DSA-SHA2-128s` `[4, 7]`), `decimal_money.py` + `audit_scitt_focus.py` (`compute_cpo_and_focus`, `TypeError` `float`/`bool`).
  - **Appui vérifié :** `obo_dpop.py`, `policy_saga/opa_runner.py`, `policies_opa/*.rego`, `ciba_approval.py`, `audit_scitt_focus.py`, `decimal_money.py`, `registre/matrice-exig-prr-c40.json` (`cinq_sbb`), `SRC-018.txt` `[4]`, `SRC-077.txt` `[7]`, `SRC-087.txt` `[9]`, `SRC-088.txt` `[10]`.
  - **Passe initiale :** écart rectifié · **Action :** corrigé le chemin erroné `policies_opa/opa_runner.py` en `policy_saga/opa_runner.py`, précisé la liaison `DPoP`/`cnf` sur `obo_dpop.py` et complété les symboles de `ciba_approval.py`, `audit_scitt_focus.py` et `compute_cpo_and_focus` · **Verdict : supporté**

### Section 35.2.2 — Wilson (`G0-EX-CH04-01`), `FEDS`/`EMA` (`DC-P12`) et `C.1`–`C.8` (`L78–L145`, Figure 3)

- **C35-19 (`L80`–`L112`, `G0-EX-CH04-01`)** — *Affirmation :* `EXIG-EVA-03` et l'extrait scellé `G0-EX-CH04-01` (`evalops_prr/wilson_bounds.py` `L43–70`, `SHA-256` `3e685cbef8...`) mettent en œuvre la borne supérieure unilatérale de Wilson à `95 %` (`z = 1,644854`) formulée dans NIST `§ 7.2.4.1` `[2]` et analysée pour les événements rares par McGrath et Burke `[11]`.
  - **Appui vérifié :** `evalops_prr/wilson_bounds.py` (`L13`, `L43–70`), `aq/rapports-g0.json` (`L155–160`), `SRC-022.txt` `[2]`, `SRC-094.txt` `[11]`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-20 (`L114`)** — *Affirmation :* `evaluate_wilson_gate` impose \(n \ge \lceil 3/p \rceil\) (`300` scénarios distincts sans échec donnant `0,8938 % < 1 %` en unilatéral `95 %`, contre `1,2643 %` et `~381` essais en bilatéral `z = 1,96`) et interdit toute répétition via `len(set(scenario_ids)) != len(outs)` `[2, 11]`.
  - **Appui vérifié :** `wilson_bounds.py` (`L63–69`), `tests/test_evalops_prr.py` (`L173–223`), `faits-empiriques.json` (`FACT-WILSON-3P`), `SRC-022.txt` `[2]`, `SRC-094.txt` `[11]`, vérification Python exacte.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-21 (`L116`)** — *Affirmation :* Les simulations quantitatives du banc reproductible `feds-ema/` (`seed=20261119`, remplaçant les estimations fictives Groupe Boréal au profit de `Borealis-Bench`, ← Chapitre 29) portent l'étiquette `DC-P12` matérialisant le plafond épistémique `C07 = 65,0 %` avec zéro étude humaine et zéro donnée de production.
  - **Appui vérifié :** `Corpus/Tome 4` (`L1241`, `L1377`, `L4877`), `Chapitre 29.md` (`L135`), `Chapitre 31.md` (`L40`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-22 (`L118`–`L122`)** — *Affirmation :* Campagne `FEDS` (`4 000` tirages/seuil) : `POR-003 < 10 s` (`99,95 %`, `p99 = 3 732,68 ms`, traîne `p99 = 11 034,19 ms` en partition, bail `TTL ≤ 5 s`) ; enveloppe d'outils (`63,85 %` conformes à `≤ 15` pour risque `≤ 2 %`, `≤ 15` `L1`–`L2` et `≤ 10–12` `L3`–`L4`) ; `CIBA < 60 s` (`< 5 s` technique `96,78 %`, alerte `60 s`, `TTL` `120–180 s`, `p95` `66,72 s`).
  - **Appui vérifié :** `Corpus/Tome 4` (`L1241`, `L4877`).
  - **Passe initiale :** écart rectifié · **Action :** précisé `p99 = 11 034,19 ms` sur la traîne de partition réseau · **Verdict : supporté**

- **C35-23 (`L123`)** — *Affirmation :* Rétention chaude : le plancher `30` j atteint `97,17 %` nominal (`p95 = 24,69` j) et `89,10 %` sous panne sévère, justifiant la cible `45` j en banque et assurance pour un surcoût simulé `SCITT` + `SLH-DSA-128s` (variante `FIPS 205` `[4]`) de `22,48 Mo` par `3` millions d'événements.
  - **Appui vérifié :** `Corpus/Tome 4` (`L1377`, `L4877`), `SRC-018.txt` (`L2481`, `[4]`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement `[4]` (`FIPS 205`) à la variante `SLH-DSA-128s` plutôt qu'au surcoût simulé `FEDS` · **Verdict : supporté**

- **C35-24 (`L124`)** — *Affirmation :* Constance `pass^5 ≥ 99 %` : médiane simulée `p50 = 99,921 %` (`99,50 %` conformité) sur le plan de contrôle et `p50 = 99,812 %` (`99,08 %` conformité) en défense multicouche (`≥ 99 %` en `L3`–`L4`), contre `≥ 95 %` pour le cœur génératif `L1`–`L2`.
  - **Appui vérifié :** `Corpus/Tome 4` (`L1241`, `L4877`).
  - **Passe initiale :** écart rectifié · **Action :** précisé `médiane simulée p50` et les taux de conformité associés (`99,50 %` et `99,08 %`) · **Verdict : supporté**

- **C35-25 (`L126`)** — *Affirmation :* Analyse `EMA` (`3 000` réplications `LHS`) : `Scénario A` (`TCO 1,233`, regret `p95 = 13,858`) contre `Scénario B` (`92,53 %` satisfaction conjointe, `95,70 %` futurs gagnés, regret `p95 = 0,000`), avec activation conditionnelle de `CAP-027`, `033`, `034`, `041` au seuil simulé `X34 ≥ 0,386`.
  - **Appui vérifié :** `Chapitre 31.md` (`L32`, `L40–42`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé l'appellation contradictoire `seuil empirique` par `seuil simulé` conforme à `DC-P12` · **Verdict : supporté**

- **C35-26 (`L128`)** — *Affirmation :* Analyse sectorielle `Borealis-Bench/feds-ema` (`CRE-IA v1.2` `305` exigences, `52` capacités, `15` `POR`, `41` attentes AMF / `12 EXIG-AMF`) : `49,59 / 100` gestion de patrimoine (plafond `L2` sur le conseil, ← Chapitre 28), `64,23` dommages, `68,36` banque, `70,19` personnes, `95,78` groupe diversifié (`52/52` capacités), moyenne `69,63 / 100`, adéquation algorithmique moyenne `81,10 / 100`.
  - **Appui vérifié :** `Corpus/Tome 4` (`L1377`), `Chapitre 28.md` (`L27`, `L50`, `Tableaux 28.1`–`28.2`).
  - **Passe initiale :** écart rectifié · **Action :** retiré l'étiquette non sourcée `(L4)` sur groupe diversifié et précisé le rattachement du plafond `L2` au conseil en patrimoine · **Verdict : supporté**

- **C35-27 (`L130`–`L135`)** — *Affirmation :* Validation des `8` contrats `C.1`–`C.8` de l'Annexe C (`DC-P11`) : `C.1`, `C.2`, `C.6`, `C.7`, `C.8` partagent le scénario d'achat de `12 480 \$` (`agt-achats-indirects@1.2.0`, classe modérée, `N3`, seuil `5 000 \$`), tandis que `C.3` (`AgentCard`), `C.4` (`CloudEvents`) et `C.5` (`OBO`) illustrent les protocoles associés (`6 [Exécuté en CI]`, `2 [Schéma conceptuel]`) ; `C.6` calcule `action_sha256` `h` (`RFC 8785` `[7]`, `apb-5e19c2` / `apb-91d4e8`, `I-JSON` `RFC 7493`) ; `C.7`–`C.8` bouclent la piste sous schémas `Draft 2020-12` `[1]` acceptant `ES256`, `ML-DSA-65` et `ML-DSA-87` `[3]`.
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 64`, `L7011–7460`), `Tomes/Tome 8 .../trousse/schemas/audit_record_c8.schema.json`, `SRC-021.txt` `[1]`, `SRC-050.txt` `[3]`, `SRC-072.txt` `[6]`, `SRC-077.txt` `[7]`.
  - **Passe initiale :** écart rectifié · **Action :** restreint le scénario `12 480 \$` aux contrats `C.1`, `C.2`, `C.6`, `C.7`, `C.8`, ajouté `RFC 7493` pour `I-JSON` et scindé la phrase d'ouverture selon `CA-05` · **Verdict : supporté**

- **C35-28 (`L137`)** — *Affirmation :* Alignement sur le calendrier du registre chronologique `SSOT` (← Chapitres 25, 26 et 34) : Loi 25 art. `12.1` (`22 septembre 2023`), `BSIF E-23` et repère attendu AMF (sous réserve documentaire) au `1er mai 2027`, `EU AI Act` art. `50` dès `août 2026` (`2 août 2026`), Annexe III **à partir du `2 décembre 2027`**, Annexe I le `2 août 2028`, et transition post-quantique `G7` `2030–2035` fondée sur `FIPS 204` et `FIPS 205` `[3, 4]`.
  - **Appui vérifié :** `registre/ancres-chronologiques.json` (`L8–188`), `SRC-061.txt` (`L1850–1854`), `SRC-050.txt` `[3]`, `SRC-018.txt` `[4]`.
  - **Passe initiale :** écart rectifié · **Action :** corrigé « au plus tard le 2 décembre 2027 » en « à partir du 2 décembre 2027 » selon `SRC-061.txt`, et rattaché les jalons légaux au registre `SSOT` tout en réservant `[3, 4]` à `G7` `2030–2035` · **Verdict : supporté**

- **C35-29 (`L134`, `L139`)** — *Affirmation :* Précision du badge `[Schéma conceptuel]` pour `C.5`/`C.6` à l'Annexe C du Tome 2 (charges utiles composites multi-blocs hors exécution `CI` autonome) dont les schémas (`delegated_token_claims`, `approval_token_c6`) et le calcul canonique `action_sha256` (`RFC 8785`) deviennent exécutables en `G0` dans `obo_dpop.py` et `ciba_approval.py` ; trois propriétés démontrées par `C.1`–`C.8` : calcul du condensat `action_sha256` et écran d'approbation par la passerelle, séparation du `typ` d'approbation d'avec `at+jwt`, et transition `ES256` → `ML-DSA-65`/`87` sans rupture du schéma `Draft 2020-12` ni du chaînage `C.8` `[1, 3, 7]`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L7374`, `L7430–7470`), `obo_dpop.py`, `ciba_approval.py` (`L73–74`, `L106–117`), `audit_record_c8.schema.json`, `SRC-021.txt` `[1]`, `SRC-050.txt` `[3]`, `SRC-077.txt` `[7]`.
  - **Passe initiale :** écart rectifié · **Action :** ajoutée l'explicitation `G0` des contrats conceptuels `C.5`/`C.6` (`post-G4`) · **Verdict : supporté**

- **C35-30 (`L141`–`L145`, `Figure 3`)** — *Affirmation :* `Figure 3` (`SCH-35-03.svg`) confrontant `feds-ema/` (`seed=20261119`, `DC-P12`, `C07 = 65,0 %`, `0` étude humaine) et la chaîne `C.1–C.8` (scénario d'achat `12 480 \$` sur `C.1`, `C.2`, `C.6–C.8`) sous `ES256` / `ML-DSA-65` / `ML-DSA-87`.
  - **Appui vérifié :** `schemas/SCH-35-03.svg`, `Corpus/Tome 2` (`L7011–7025`).
  - **Passe initiale :** écart rectifié · **Action :** précisé en légende le périmètre `C.1`, `C.2`, `C.6–C.8` du scénario `12 480 \$` · **Verdict : supporté**

### Section 35.3 — Synthèse transversale, livrables et invariants (`L147–L165`, Tableau 35.3)

- **C35-31 (`L149`)** — *Affirmation :* Interfaces amont (`ch29`, `ch34`) et aval (`ch04`, `ch15`, `ch18`, `ch20`, `ch22`, `ch23`, `ch31`, `ch36`) respectant la partition bijective `CA-21`.
  - **Appui vérifié :** `specs/manifest.json` (`ch01`–`ch36`), `verifie_manuscrit.py` (`CA-21`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-32 (`L151`–`L159`, `Tableau 35.3`)** — *Affirmation :* Le `Tableau 35.3` synthétise les `5` livrables exécutables (`8 - Manuel/trousse/` avec `17` paquets verrouillés / `18` distributions `[1, 9, 10]`, `4/4` suites tierces et `14/14` `CA-G0-SYNC` `[3, 4, 5, 7, 8]`, `5 SBB` incluant `policy_saga/opa_runner` + validation `24` portes PRR bloquantes et `C01–C40` `[1, 4, 7, 9, 10]`, `feds-ema/` + Wilson `[2, 11]`, et `C.1–C.8` `[1, 3, 6, 7]`).
  - **Appui vérifié :** `aq/rapports-g0.json`, `requirements.lock`, `prr_validators.py`, `Corpus/Tome 2`, `Corpus/Tome 4`, `SRC-021`, `022`, `050`, `018`, `055`, `072`, `077`, `086`, `087`, `088`, `094`.
  - **Passe initiale :** écart rectifié · **Action :** harmonisé `17` paquets / `18` distributions, `policy_saga/opa_runner`, `24 portes PRR bloquantes`, le scénario `12 480 \$` sur `C.1`, `C.2`, `C.6–C.8` et les badges `DC-P11` · **Verdict : supporté**

- **C35-33 (`L163`, Invariant 1)** — *Affirmation :* Barrière `execute_g0.py` à `exit 0` prouvant `83/83` `pytest`, `45/45` `OPA` à `100,0 %` sous `default allow := false`, `13` schémas `Draft 2020-12` stricts (`21` contrôles avec registres), `SPDX MIT` sur `50` fichiers, `17` paquets `SHA-256` (`18` distributions), `4/4` suites tierces (`50` fichiers) et `14/14` `CA-G0-SYNC`.
  - **Appui vérifié :** `aq/rapports-g0.json`, `requirements.lock`.
  - **Passe initiale :** écart rectifié · **Action :** aligné `13` schémas / `21` contrôles et `17` paquets / `18` distributions · **Verdict : supporté**

- **C35-34 (`L164`, Invariant 2)** — *Affirmation :* Exécution testable des `5 SBB` du `Tableau 12` (dont arithmétique `Decimal` stricte) et validation par `evaluate_wilson_gate` (`G0-EX-CH04-01`, `EXIG-EVA-03`) imposant \(n \ge \lceil 3/p \rceil\) sans répétition (`300` essais distincts à `0` échec donnant `0,8938 % < 1 %`).
  - **Appui vérifié :** `evalops_prr/wilson_bounds.py`, `tests/test_evalops_prr.py`, `policy_saga/decimal_money.py`, `audit_scitt_focus.py`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C35-35 (`L161`, Invariant 3)** — *Affirmation :* Bornage `DC-P12` (`FEDS` `4 000` tirages, `EMA` `3 000` `LHS`, plafond `C07 = 65,0 %` sans étude humaine ni `SoR` réel) et continuité `JCS SHA-256` d'`ES256` vers `ML-DSA-65/87` sur les contrats `C.1–C.8` (scénario `12 480 $` sur `C.1`, `C.2`, `C.6–C.8`).
  - **Appui vérifié :** `Corpus/Tome 2` (`L7011–7025`), `Corpus/Tome 4` (`L1241`, `L4877`), `audit_record_c8.schema.json`, `Compendium/prd.md` (`EXIG-EXEC-01`..`06`).
  - **Passe initiale :** écart rectifié · **Action :** précisé le périmètre `C.1`, `C.2`, `C.6–C.8` du scénario `12 480 $` ; révision `REV-04` : renumérotation continue `Figure 109` à `Figure 111` (`PRD-L4-012`), retrait de `\$` dans les backticks (`PRD-L4-010`), intégration explicite de `EXIG-EXEC-02` et `EXIG-EXEC-03` en prose, `Tableau 35.3` et Invariant 1 (`PRD-L4-013`), remplacement des chemins internes `aq/rapports-g0.json` par `rapport scellé G0` (`PRD-L4-015` et `SCH-35-01.puml` `PRD-L4-027`) et harmonisation `H2` (`35.1`/`35.2`/`35.3`, `PRD-L4-022`), en préservant intégralement le bloc `G0-EX-CH04-01` · **Verdict : supporté**
