# Audit indépendant PRD — Lot 4 (`REV-03`, Parties X–XII, Annexes A–E, Schémas et Livrables)

- **Auditeur** : `audit-prd-lot4` (`REV-03`, Lot 4/4, mode audit uniquement)
- **Référentiel** : `Compendium/prd.md` (Parties X–XII, Annexes A–E), registres SSOT `Compendium/ouvrage/registre/*.json`, `Compendium/ouvrage/specs/manifest.json`, `Compendium/ouvrage/aq/rapports-g0.json`
- **Périmètre audité** :
  - **14 unités** : `CH-28` à `CH-36` (Parties X `D10`, XI `D11`, XII `D12`) et `Annexes A` à `E`
  - **28 schémas du lot** (`SCH-28-01` à `SCH-36-04`) + contrôle d'homogénéité des **115 schémas** de l'ouvrage
  - **3 livrables assemblés** : `Compendium.md` (`7 204` lignes, `205 115` mots), `Compendium.html` (`10,03 Mo`, `115` images embarquées, `0` ancre cassée), `Compendium.pdf` (`711` pages, `354` signets, `0` débordement de marge, `0` lien GOTO cassé)

## 1. Verdict synthétique

| Gravité | Effectif | Répartition principale |
|---|---:|---|
| **BLOQUANT** | **8** | Citations `[1]`–`[19]` orphelines (`1 302`/`1 303`), numérotation des `115` figures cassée (`84` anomalies), troncatures massives des Annexes `A`, `B`, `C`, `D`, `E` par `_select_sections_for_budget()`, chemin inexistant `policies_opa/opa_runner.py` |
| **MAJEUR** | **12** | Chaînes corrompues `//[É]/` et `[N]//[É]/[S]` en PDF/HTML/MD, `106` `\$` littéraux en MD, italiques brisés (`SCH-30-01`/`30-03`), reset figures Partie XII, `EXIG-EXEC-02/03` omis en `CH-35`, sur-extension `DISC-02` en `CH-36`, fuites `prd.md` et chemins d'atelier, `Cible (mots)` en Annexe A, doublons `BIBLIOGRAPHIE_BRUTE`, fuites Tome 8 et juridictions dupliquées en Annexe C, identifiants PRD manquants (`CH-31`/`32`/`34`), typographie `fr-CA` cassée (`353` `:` sans espace) dans les 5 Annexes |
| **MINEUR** | **8** | Placement/numérotation des `114` tableaux, titres `H2` Partie XII, faute d'accord `CH-32`, absence TdM dans `Compendium.md` + `pass^k` TdM PDF, renvois croisés `CH-28`–`30` / `CH-31` / `CH-33`, noms d'outils internes dans `SCH-35-01` et `SCH-36-03` |
| **Total** | **28** | **Verdict : NON PRÊT À PUBLICATION en l'état** (8 bloquants à lever avant gel final) |

### Points forts vérifiés
- **Couverture thématique MindMap de `CH-28`–`CH-36`** : `100 %` des thèmes MindMap assignés aux chapitres `28` à `36` (`75` thèmes) sont traités sur le fond avec rigueur technique, ancrage réglementaire daté (`2 décembre 2026`), clause `non-avis` (`65` occurrences) et fermeture `DIV-02` (`56` occurrences) / `DISC-01`–`DISC-05` présentes.
- **Intégrité des 115 schémas (`SCH-00-01`..`SCH-36-04`)** : `115/115` sources et rendus présents, valides en XML/PNG, tous embarqués en base64 dans `Compendium.html` (`0` image manquante), `28/28` schémas du Lot 4 strictement conformes aux notations prescrites dans `prd.md` Annexe E (`11` `.puml`, `9` `.svg`, `8` `.mmd`).
- **Intégrité structurelle et visuelle de base des livrables** : `0` saut de niveau de titre (`H1`–`H5`), `0` titre dupliqué, `0` ancre interne cassée sur `395` liens dans `Compendium.html`, `0` lien GOTO cassé et `0` débordement de marge sur les `711` pages de `Compendium.pdf`, `0` `\$` littéral ni LaTeX brut `\(...\)` dans `HTML` et `PDF` (les `88` formules MathML / Typst sont correctement rendues), et comptages G2 `674 -> 1 390` exacts sur les `37` journaux `ancrage/*.md`.

---

## 2. Cause racine systémique des défauts des Annexes A–E

L'inspection de `Compendium/ouvrage/outils/genere_annexes.py` révèle **trois défauts logiciels** qui expliquent la quasi-totalité des constats bloquants et majeurs des cinq annexes :
1. **`_select_sections_for_budget()` (éviction gloutonne par budget de mots)** : lorsqu'un bloc normatif dépasse le plafond de mots résiduel, la fonction le saute silencieusement et tente d'insérer un bloc ultérieur plus court. Conséquences vérifiées :
   - **Annexe A** : `§4` saute de `ch07` à `ch14` (`28/36` chapitres perdus) et `§5` (Statut F) disparaît entièrement.
   - **Annexe B** : `§6` s'arrête après `24/81` `attenuation_risque`, perdant `100 %` des `dependance_technique` (`93`) et `amplification_synergie` (`63`) ; seules `86/616` relations `REL_xxxx` y apparaissent (`132/616` dans tout l'ouvrage).
   - **Annexe C** : `§5` coupe après `8/13` jalons (dernier : `2025-12-03`), évince intégralement les `73` échéances `2027–2035` en prose, évince `§6`, `§8`, `§9` et laisse un paragraphe orphelin `Liaison REL_0058` sans titre en L95.
   - **Annexe D** : `§8` coupe à `24/57` specs `L+`, `§10` n'affiche que `10/82` `encadrement_normatif` et `0/132` `operationnalisation`.
   - **Annexe E** : `§3` évince intégralement la **Partie XII (`D12`, `10` schémas `SCH-34-01`..`SCH-36-04`)** du catalogue analytique.
2. **`_RAW_MARKER_RE` et `_sanitize_fr_ca()`** : la regex supprime les jetons légitimes `[N]`, `[M]`, `[S]` de la notation de quadruple preuve `([N]/[M]/[É]/[S])` (produisant `//[É]/` en Annexe A L132 et `[N]//[É]/[S]` en Annexe E L36/L165, imprimés tels quels dans le PDF p. 601, 689, 703), tandis que `re.sub(r" +([,.;:!?])", r"\1", cleaned)` efface l'espace `fr-CA` avant les deux-points (`353` violations dans les 5 annexes).
3. **Comparaison lexicographique de dates dans `Annexe C` (L670)** : `str(date) <= "2026-12-02"` classe le jalon futur `18 mois — J3 : Industrialisation` (`DAPP-T5-03`) en tête des « jalons établis jusqu'au gel du 2 décembre 2026 » (car `'18 mois' < '2026-12-02'`), faussant également le décompte (`13` vs `73` au lieu de `12` vs `74`).

---

## 3. Audit détaillé par unité

### 3.1 Partie X (`D10`) — `CH-28`, `CH-29`, `CH-30`

| Unité | Mots | Thèmes MindMap | Schémas (`prd.md` vs disque) | Constats relevés |
|---|---:|---:|---|---|
| **CH-28** | 5 313 | 10/10 | `SCH-28-01` (`.svg`), `28-02` (`.puml`), `28-03` (`.svg`) — 3/3 OK | `PRD-L4-010` (`\$` dans backticks L25, 81, 114–118), `PRD-L4-025` (`SIG-103..105`, `DISC-01/05` non repris). Note : la réconciliation PEX `13/11` v1.1 → `5/12/7` v1.2 est bien explicitée en L15. |
| **CH-29** | 4 985 | 8/8 | `SCH-29-01` (`.puml`), `29-02` (`.mmd`), `29-03` (`.svg`) — 3/3 OK | `PRD-L4-010` (`\$` dans backticks L83, 137, 143), `PRD-L4-015` (mentions `aq/rapports-g0.json` L19/137), `PRD-L4-025` (`ADR-018`, `ADR-031`, `INI-047`, `DIV-02` absents). Note : `policy_saga/opa_runner.py` (L17/26) est exact sur disque. |
| **CH-30** | 4 520 | 6/6 | `SCH-30-01` (`.puml`), `30-02` (`.mmd`), `30-03` (`.svg`) — 3/3 OK | **`PRD-L4-011` (MAJEUR)** : italiques imbriqués brisés dans `*Figure 94 — SCH-30-01 ... *Golden Paths* ...*` (L49, confirmé visuellement PDF p. 486 avec `*` littéraux) et `*Figure 96 — SCH-30-03 ... *Strangler Fig* ...*` (L128) ; `PRD-L4-025` (`POR-016`, `ADR-009`, `DEC-001` absents). |

### 3.2 Partie XI (`D11`) — `CH-31`, `CH-32`, `CH-33`

| Unité | Mots | Thèmes MindMap | Schémas (`prd.md` vs disque) | Constats relevés |
|---|---:|---:|---|---|
| **CH-31** | 5 453 | 11/11 | `SCH-31-01` (`.svg`), `31-02` (`.mmd`), `31-03` (`.puml`) — 3/3 OK | `PRD-L4-015` (fuites `ch31-sources.md` L7, `registre/matrice-exig-prr-c40.json` L46/54, `registre/concordance-taxonomies.json` L73), `PRD-L4-019` (`EXIG-CON-30` absent), `PRD-L4-028` (`25` `INI-*` et `POR-006/012/013` agrégés sans table exhaustive correspondante en annexe). |
| **CH-32** | 4 963 | 8/8 | `SCH-32-01` (`.puml`), `32-02` (`.mmd`), `32-03` (`.svg`) — 3/3 OK | **`PRD-L4-019` (MAJEUR)** : `EXIG-GOV-19` (`prd.md` L5933), `EXIG-CON-12` (L5938), `CAP-047`, `CAP-050`, `PRR-75` non cités ; `PRD-L4-023` (faute d'accord L7 : `un cadre technique pédagogique arrêtée`). |
| **CH-33** | 3 912 | 3/3 | `SCH-33-01` (`.puml`), `33-02` (`.svg`), `33-03` (`.mmd`) — 3/3 OK | `PRD-L4-010` (`\$` dans backticks L52), `PRD-L4-026` (`CAP-002`, `CAP-031`, `CAP-039`, `ADR-025`, `PRI-007`, `PRR-75` non cités). Note : `\(\psi \ge 0,75\)` (L46) est correctement rendu en MathML/Typst. |

### 3.3 Partie XII (`D12`) — `CH-34`, `CH-35`, `CH-36`

| Unité | Mots | Thèmes MindMap | Schémas (`prd.md` vs disque) | Constats relevés |
|---|---:|---:|---|---|
| **CH-34** | 4 558 | 6/6 | `SCH-34-01` (`.puml`), `34-02` (`.mmd`), `34-03` (`.mmd`) — 3/3 OK | **`PRD-L4-012` (MAJEUR)** : réinitialisation `Figure 1–3` au lieu de `Figure 106–108` (confirmé PDF p. 548) ; `PRD-L4-010` (`\$` L19) ; `PRD-L4-019` (`POR-003`, `DC-P11`, `CAP-046` et 5 `EXIG-*` clés omis) ; `PRD-L4-022` (structure `H2` divergente `## 34.1 Résumé exécutif`). |
| **CH-35** | 4 532 | 5/5 | `SCH-35-01` (`.puml`), `35-02` (`.puml`), `35-03` (`.svg`) — 3/3 OK | **`PRD-L4-013` (MAJEUR)** : codes `EXIG-EXEC-02` et `EXIG-EXEC-03` (`prd.md` L6359–6360) omis partout (y compris Tableau 35.3), et écart `17` paquets verrouillés dans `requirements.lock` (vérifié sur disque) vs `18` dans `prd.md`/`rapports-g0.json` non tracé en Annexe D ; `PRD-L4-012` (`Figure 1–3` au lieu de `109–111`) ; `PRD-L4-010` (`\$` L130, 134, 145, 157, 165) ; `PRD-L4-015` (`aq/rapports-g0.json` répété) ; `PRD-L4-027` (`rapports-g0.json` dans `SCH-35-01.puml` L74) ; `PRD-L4-022`. |
| **CH-36** | 6 011 | 14/14 | `SCH-36-01` (`.puml`), `36-02` (`.svg`), `36-03` (`.puml`), `36-04` (`.mmd`) — 4/4 OK | **`PRD-L4-014` (MAJEUR)** : `DISC-02` formulé en L60/165 comme proscription générale en prose technique (contredite par `CH-28`–`32` et `Annexe C` L18 qui la cantonnent au Volume 8), et omission des `14` événements de péremption Annexe N et des codes `EXIG-AMF/CON/SEC` de la réouverture `v1.2` ; **`PRD-L4-015` (MAJEUR)** : `prd.md` imprimé 5 fois dans le Tableau 36.3 (PDF p. 590) ; `PRD-L4-012` (`Figure 1–4` au lieu de `112–115`) ; `PRD-L4-027` (`gauntlet-loop` dans `SCH-36-03.puml` L72) ; `PRD-L4-022`. |

### 3.4 Annexes `A` à `E` — Contrôle de conformité SSOT vs `prd.md`

| Annexe | Comptage SSOT attendu | Restitution effective | Constats majeurs / bloquants |
|---|---|---|---|
| **Annexe A** | `12` domaines, `36` chapitres, `71` familles (`FAM_*`), `260` thèmes, `Statut F` (`§5`), `674 -> 1 390` G2 | Table 2 (`36` chapitres OK mais colonne interne `Cible (mots)`), `§4` limité à **`8/36` chapitres** (`ch01`–`07`, `ch14`), `47/260` titres de thèmes, `0/260` slugs, `0/71` `FAM_*`, **`§5` absent**, `674 -> 1 390` exact | `PRD-L4-003` (BLOQUANT), `PRD-L4-009` (`//[É]/` L132, PDF p. 601), `PRD-L4-016` (`Cible (mots)` + colonnes PRD manquantes), `PRD-L4-015` (`specs/manifest.json`, `verifie_manuscrit.py`), `PRD-L4-020` (typographie `:`) |
| **Annexe B** | `616` interrelations (`8` types), `25` nœuds carrefours, `62` tensions, `81` atténuations, `93` dépendances, `63` synergies | **`## 2.` manquant** (`## 1.` → `## 3.`), **`86/616` `REL_xxxx`** (`62` tensions + `24/81` atténuations, `0/93` dépendances, `0/63` synergies), doublon verbatim des `62` tensions dans `BIBLIOGRAPHIE_BRUTE` | `PRD-L4-004` (BLOQUANT), `PRD-L4-017` (doublon `BIBLIOGRAPHIE_BRUTE`), `PRD-L4-020` (typographie `:`) |
| **Annexe C** | `DIV-02`, `DISC-01`–`05`, `86` jalons vérifiés `2023–2035` (`12` pré-gel + `74` post-gel), grandeurs empiriques (`§6`), `§7–§9` | `18 mois — J3` classé « établi pré-gel » (`13/73` faux), **`8/13` établis** (coupe à `2025-12-03`), **`0/73` jalons `2027–2035`** en prose, **`§6, §8, §9` évincés**, `Liaison REL_0058` orpheline (L95) | `PRD-L4-005` (BLOQUANT), `PRD-L4-018` (`Section: 0.2`, `Volume 8`, juridictions dupliquées), `PRD-L4-010` (`\$` L89/103/197–198), `PRD-L4-020` (`13` `..` + `:`) |
| **Annexe D** | `305 EXIG-*`, `52 CAP`, `24 PEX` (`PEX-001`..`044`), `75 PRR` (`24` bloquants), `C01–C40` (`18/15/7`), `5 SBB`, `57` specs `L+`, `95` mappings G0, matrice `237` entrées | `0/52` CAP listées, titre erroné **`PEX-001–PEX-024`** (PDF p. 668), **`24/57` specs `L+`** en `§8`, **`10/82` encadrement + `0/132` opérationnalisation** en `§10`, `C01–C40` `18/15/7` et `51` PRR non bloquants absents, chemin faux **`policies_opa/opa_runner.py`** | `PRD-L4-006` (BLOQUANT), `PRD-L4-008` (BLOQUANT — `opa_runner.py`), `PRD-L4-015` (`Compendium/ouvrage/outils/`), `PRD-L4-020` (`(1 liaisons)` L192/196/198 + `:`) |
| **Annexe E** | `115` schémas (`4` panoramiques + `111` de chapitres sur Parties I–XII), `319` figures du corpus (`267` liées / `52` non liées = `83,70 %`), répartition par 8 archétypes et publics | **`Partie XII — D12` (`10` schémas `SCH-34-01`..`36-04`) entièrement évincée de `§3`** (`101/111` en `§3`), tableaux archétypes/publics/couverture `267/319` absents | `PRD-L4-007` (BLOQUANT), `PRD-L4-009` (`[N]//[É]/[S]` L36 & L165, PDF p. 689 & 703), `PRD-L4-017` (redondance `BIBLIOGRAPHIE_BRUTE`), `PRD-L4-020` (typographie `:`) |

---

## 4. Audit de cohérence d'ensemble des 3 livrables (`MD`, `HTML`, `PDF`)

| Critère global | `Compendium.md` | `Compendium.html` | `Compendium.pdf` (`711 p.`) | Statut |
|---|---|---|---|---|
| Hiérarchie des titres (`H1`–`H5`), doublons | `354` titres, `0` saut, `0` doublon | `355` titres (`+title`), `0` id dupliqué | `354` signets cohérents | **OK** (sauf `## 2.` manquant en Annexe B) |
| Table des matières & ancres internes | **Aucune TdM générée** (`PRD-L4-024`) | `<nav id="TOC">` (`60` liens), `395/395` `#ancres` valides (`0` cassée) | TdM `p. 3–6` propre, `62` liens, `0` GOTO cassé (`pass^k` brut p. 3) | **MINEUR** (`PRD-L4-024`) |
| Citations `[1]`..`[19]` & bibliographie | **`1 302` appels orphelins**, 0 section Références | **`1 302` appels orphelins** | **`1 303` appels orphelins sur `388` pages** | **BLOQUANT** (`PRD-L4-001`) |
| Numérotation des `115` figures | **`84` anomalies** (`Figure 1` × `28`, saut `3 -> 88 -> 105 -> 1`) | Identique (`84` anomalies) | Identique (`84` anomalies, vérifié p. 548) | **BLOQUANT** (`PRD-L4-002`) |
| Homogénéité des `114` tableaux | `100` légendes dessous, `9` dessus (`CH-10..12`), `5` sans légende (Annexes) | Identique (`114` `<table>`) | Identique, `0` débordement de marge | **MINEUR** (`PRD-L4-021`) |
| Images / schémas embarqués | `115/115` liens relatifs valides (`0` manquant) | `115/115` `data:image/` embarquées (`0` cassée) | `115/115` rendus (`92` SVG + `23` PNG) | **OK** |
| Échappements `\$`, LaTeX `\(...\)`, italiques | **`106` `\$` bruts** (`94` en backticks), `3` légendes `*...*` cassées | `0` `\$`, `0` `\(`, `88` `<math>`, **`3` légendes cassées** | `0` `\$`, `0` `\(`, **`3` légendes cassées** (vérifié p. 486 : `Golden Paths*`) | **MAJEUR** (`PRD-L4-010`, `011`) |
| Artefacts de production & corruptions | `10` `BIBLIOGRAPHIE_BRUTE`, `5` `prd.md`, `3` `//[É]/` ou `[N]//`, `353` `:` sans espace | `10` commentaires `BIBLIOGRAPHIE_BRUTE`, `5` `prd.md`, `3` corruptions | `5` `prd.md` (p. 590), `3` corruptions (p. 601, 689, 703), `353` `:` sans espace | **MAJEUR** (`PRD-L4-009`, `015`, `017`, `020`) |
| Exhaustivité SSOT globale | `115/115` schémas, `260/260` slugs (dans Annexe B), **`0/71` `FAM_*`**, **`132/616` `REL_xxxx`**, `DIV-02`/`DISC-01..05`/`non-avis` présents | Identique | Identique | **BLOQUANT** (`PRD-L4-003` à `007`) |

---

## 5. Registre consolidé des 28 constats (`PRD-L4-001` à `PRD-L4-028`)

Les 28 constats détaillés, avec leur sévérité, axe, unité et résolution prescrite, sont consignés au format machine exploitable dans [`Compendium/ouvrage/aq/findings-prd-lot4.json`](file:///c:/Github/Agentique/Compendium/ouvrage/aq/findings-prd-lot4.json).

### Ordre de remédiation recommandé
1. **Correction prioritaire de `genere_annexes.py` + `registre/matrice-exig-prr-c40.json` + `registre/ancres-chronologiques.json`** : lève d'un seul coup les 6 bloquants des Annexes (`PRD-L4-003` à `008`) et 5 majeurs (`PRD-L4-009`, `016`, `017`, `018`, `020`).
2. **Correction d'`assemble_livre.py` et harmonisation globale des figures + références de chapitres** : lève les 2 bloquants transversaux (`PRD-L4-001`, `PRD-L4-002`) ainsi que `PRD-L4-010`, `PRD-L4-012`, `PRD-L4-024`.
3. **Retouches ciblées sur `CH-28`–`CH-36` et `SCH-35-01`/`SCH-36-03`** : lève les constats majeurs et mineurs restants (`PRD-L4-011`, `013`, `014`, `015`, `019`, `021`–`023`, `025`–`028`).
