# Rapport de recollation G3 — Passe 2 à froid (`seed=20270802`)

- **Barrière :** `G3` passe 2 à froid (`CA-14`, `specs/contrat-aq.md` § 2.3)
- **Graine déterministe :** `20270802` ([`recollation-seed-20270802.json`](recollation-seed-20270802.json))
- **Disjointivité vérifiée face à la passe 1 (`seed=20270801`) :** `0` chevauchement sur `claim_loc` et `0` chevauchement sur `paragraph_loc` (`60` énoncés répartis en `4 × 15` strates : `empirique`, `spec_technique`, `juridique`, `assertions_g0`, avec `>= 8` par unité narrative : `00-liminaire`: `10`, `ch01`: `11`, `ch02`: `13`, `ch03`: `11`, `ch04`: `15`)
- **Auditeur indépendant :** sous-agent isolé `Recollateur G3 Passe 2` (`DeepInvestigator`, `7180a9a4`)
- **Score initial avant correction :** **`59/60`** (`98,3 %` `CONFORME`, seuil bloquant `>= 57/60` atteint ; `1` `ECART`)
- **Score final après correction et contre-vérification :** **`60/60`** (`100,0 %` `CONFORME`, `0` `ECART` résiduel)

## Synthèse de l'écart initial et de la rectification appliquée

| Item | Localisation | Nature de l'écart initial | Action correctrice et preuve vérifiée | Verdict final |
| :---: | --- | --- | --- | :---: |
| `7` | `00-liminaire:P026:S01` (`00 - Liminaire.md#L76`) | La phrase mentionnait « la publication semestrielle de `SEP-3398` est attendue le 30 mars 2027 » sous `[10]` (`SRC-072`), alors que `SEP-3398` (`SRC-082`) porte déjà le statut `Accepted` (`2026-10-14`) et fixe la cadence semestrielle des publications de la **spécification MCP**, dont la prochaine parution vise le `30 mars 2027`. | Reformulation en `00 - Liminaire.md#L76` (*« Pour le protocole MCP 2026-07-28 [10], la prochaine publication semestrielle de la spécification (instaurée par `SEP-3398`, statut `Accepted`) est attendue le 30 mars 2027 (Chapitre 01) [16]. »*), ajout de `[16] SRC-082` dans `sources/ch00-sources.md` (`SHA-256` vérifié `64aee02f...`), mise à jour de `ancrage/ch00-ancrage.md` (`CH00-060`) et contre-vérification indépendante par `7180a9a4`. | **CONFORME** |

## Synthèse de contrôle des 60 items et stabilité du tirage

- **Contre-vérification des `59` autres items (`Items 1–6`, `8–60`) :** tous vérifiés **`CONFORME`** dès la passe à froid contre `recherche/corpus_l_plus/SRC-*.txt`, `sources/ch00..ch04-sources.md`, `8 - Trousse/**`, `registre/*.json` et `aq/rapports-g0.json`. La stabilité du tirage `draw_stratified_sample(..., seed=20270802)` après retouche de l'Item `7` a été confirmée (`59/60` items identiques champ pour champ ; seul l'Item `7` inclut désormais `[10, 16]` → `["SRC-072", "SRC-082"]`).
- **Observations annexes consignées hors statut d'écart :**
  1. En `00 - Liminaire.md#L41` (`Tableau 0.1` / commentaire), le paragraphe `00-liminaire:P014` reste non retouché car exclu par la passe 1 (`seed=20270801`).
  2. Sur `Item 58` (`ch04:P059:S01`), `SRC-067` (`[21]`) vise l'art. `40` pour les QMS tandis que le rattachement explicite à l'art. `17` provient de `SRC-060` (`[15]`) et de `SRC-069` (`[23]`, déjà cité au paragraphe `L219`).
  3. Sur `Item 31` (`ch02:P057:S01`), l'énoncé reflète fidèlement les plafonds des articles `90.12` et `91` de `LQ 2021, c. 25` (`SRC-063 L2283–2333`), sans reprendre la règle annexe de récidive de l'article `92.1`.

## Revalidation déterministe post-rectification

- **Barrière `G0` (`execute_g0.py --verify-sync-manifest`) :** `exit 0` (`PASS` : `83/83` `pytest`, `45/45` `OPA` à `100,0 %` sur `3` paquets `.rego`, `21` validations `JSON Schema 2020-12`, `4/4` suites de vecteurs tiers `50/50`, `requirements.lock` `17` paquets `SHA-256`, `50` fichiers / `18` distributions `.venv` compatibles `MIT`, `14/14` extraits `CA-G0-SYNC`).
- **Barrières `CA-17` & `G1` (`genere_annexes.py` puis `verifie_manuscrit.py --strict`) :** `exit 0` (`0` erreur, `0` collision `12-grammes`, `00 - Liminaire.md` à `3 774` mots dans `[3 220, 3 780]`).
- **Verdict consolidé `G3` Passe 2 (`CA-14`) :** **`60/60`** (`CONFORME`).
