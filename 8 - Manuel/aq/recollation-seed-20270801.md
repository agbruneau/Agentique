# Rapport de recollation G3 — Passe 1 (`seed=20270801`)

- **Barrière :** `G3` (`CA-13`, `specs/contrat-aq.md` § 2.3)
- **Graine déterministe :** `20270801` ([`recollation-seed-20270801.json`](recollation-seed-20270801.json))
- **Effectif tiré :** `60` énoncés sources stratifiés (`15` × `4` catégories : `empirique`, `spec_technique`, `juridique`, `assertions_g0` ; `12` × `5` unités narratives : `00-liminaire`, `ch01`..`ch04`)
- **Auditeur indépendant :** sous-agent isolé `Recollateur G3 Passe 1` (`DeepInvestigator`, `a58bb8c0`)
- **Score initial avant correction :** **`57/60`** (`95,0 %` `CONFORME`, `3` `ECART`)
- **Score final après correction et contre-vérification :** **`60/60`** (`100,0 %` `CONFORME`, `0` `ECART` résiduel)

## Synthèse des écarts initiaux et rectifications appliquées

| Item | Localisation | Nature de l'écart initial | Action correctrice et preuve vérifiée | Verdict final |
| :---: | --- | --- | --- | :---: |
| `26` | `ch02:P022:S01` (`Chapitre 02.md#L89`) | Attribuait à tort l'exigence `EXIG-SEC-25` à `ciba_approval.py` (`C.6`), alors que `registre/matrice-exig-prr-c40.json` (`L594–603`) l'affecte à `ch03 / policies_opa / OpaPolicyEngine.run_coverage`. | Retrait d'`EXIG-SEC-25` en `Chapitre 02.md#L89` (remplacé par `bloc SBB-SIGNED-HUMAN-APPROVAL`), mise à jour de `ch02-ancrage.md` (`C29`), rattachement explicite d'`EXIG-SEC-25` à `OpaPolicyEngine.run_coverage` en `Chapitre 03.md#L51` et `ch03-ancrage.md` (`CH03-033`, plage corrigée `L137–196`). | **CONFORME** |
| `31` | `ch02:P047:S01` (`Chapitre 02.md#L223`) | Mentionnait un retrait après `v1.41.0` et un ciblage `v1.44+` via le *Cadre de Référence* sans source `L+` archivée couvrant `v1.44+`. | Reformulation en `Chapitre 02.md#L223` et `ch02-ancrage.md` (`C55`) strictement ancrée sur les trois instantanés `L+` archivés : `SRC-089` (`[17]`, `v1.41.0` du `28 avril 2026`), `SRC-090` (`[18]`, `semantic-conventions-genai@244465e9` du `31 octobre 2026`) et `SRC-037` (`[19]`, renvoyant à `v1.45.0` pour les attributs généraux d'erreur). | **CONFORME** |
| `58` | `ch04:P056:S02` (`Chapitre 04.md#L219`) | Citait uniquement `[21]` (`SRC-067`) pour la présomption de conformité à l'art. `17`, alors que `SRC-067` vise expressément l'art. `40` (le lien à l'art. `17` figure dans `SRC-060` `[15]` et `SRC-069` `[23]`). | Précision en `Chapitre 04.md#L219` de l'art. `40` pour la présomption QMS visant l'art. `17` avec triplet `[15, 21, 23]`, correction de `ch04-sources.md#L238` et mise à jour de `ch04-ancrage.md` (`C04-189`, plages `SRC-060 L3953–3965, L4706–4713`). | **CONFORME** |

## Rectifications hors échantillon et suivis consignés

- **Contresens critique hors échantillon (`00-liminaire:P007:S01`, `00 - Liminaire.md#L17`) :** la phrase affirmait « sans représentativité populationnelle ni firmes de moins de 20 employés `[7]` », contredisant `SRC-016.txt` (`L104–108`) selon lequel les firmes de moins de `20` employés sont *surreprésentées* par rapport à leur part du PIB. Rectifié en `00 - Liminaire.md#L17` et consigné en `ch00-ancrage.md` (`CH00-012`).
- **Dérive mineure de version (`SRC-036`) :** `draft-ietf-httpapi-idempotency-key-header-07` corrigé en `-09` dans `sources/ch03-sources.md` (`L172`, `L190`) et `registre/specifications-lplus.json` (`L481`).
- **Nettoyages annexes appliqués :** `sources/ch02-sources.md#L194` (`Registre v1.41.0` au lieu de `Registre stable`, car `0` attribut `Stable` dans `SRC-089`) et `L293` (`RFC 8785` `Independent Submission` / `Informational` au lieu de `Standards Track`).
- **Points consignés pour la suite du pipeline :**
  1. Coquille grammaticale mineure sur `Item 15` (`Chapitre 01.md#L21` : « Pan et ses coauteurs examine ») à corriger en phase de lissage `G5`.
  2. Mention résiduelle d'`EXIG-SEC-25` sous `ASI03`/`ASI09` dans `8 - Trousse/vectors/owasp_src055/{asi01_asi10_catalog.json,asi01_asi10_crosswalk.md}` (condensats scellés dans `vectors-manifest.json`, laissés intacts hors périmètre manuscrit conformément à la matrice SSOT `matrice-exig-prr-c40.json`) ainsi que dans l'archive en lecture seule `specs-volume-8/`.

## Contre-vérification et barrières déterministes

- Les `57` items non modifiés de `recollation-seed-20270801.json` ont également été contre-vérifiés directement par le recollateur contre `corpus_l_plus/*.txt`, `8 - Trousse/`, `aq/rapports-g0.json` et `registre/`.
- Barrières exécutées après rectification : `G0` (`execute_g0.py --verify-sync-manifest`) -> `exit 0` (`83/83` `pytest`, `45/45` `OPA` à `100,0 %`, `14/14` extraits `CA-G0-SYNC`) ; `G1` (`verifie_manuscrit.py --strict`) -> `exit 0` (`0` erreur).
- **Verdict consolidé `G3` Passe 1 :** **`60/60`** (`CONFORME`).
