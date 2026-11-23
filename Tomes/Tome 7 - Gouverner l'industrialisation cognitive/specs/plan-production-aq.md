# Usine de Production et d'AQ du 7 - Livre — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task **uniquement lorsque l'utilisateur donnera le feu vert de lancement après validation de `specs/`**. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produire, illustrer, vérifier par cinq barrières indépendantes et assembler en PDF/HTML l'ouvrage complet *Gouverner l'industrialisation cognitive* (~74 000 mots, liminaire architectural + 12 chapitres, 23 figures) à partir du dossier normatif `7 - Livre/specs/`.

**Architecture:** Pipeline séquentiel en cinq étages découplés par fichiers versionnés : (1) outillage déterministe de validation et d'échantillonnage, (2) collecte scientifique ouverte `L+` hachée `SHA-256`, réancrage des registres et indexation du corpus local sans contournement, (3) génération compilée des 23 figures (`Fig-00` à `Fig-22`) et rédaction cloisonnée des 13 unités narratives sur base de sources fermée, (4) exécution étanche de `G1`, `G2`, `G3` passe 1 et `G4`, puis (5) lissage transversal `G5`, recollation finale à froid `G3` passe 2, génération déterministe des annexes et inspection visuelle `Pandoc`/`Typst`.

**Tech Stack:** Python 3.12+ (`pytest`, `hashlib`, `json`, `re`), `PlantUML` (`.svg`), `Mermaid CLI` (`.png` 300 DPI), `Pandoc` (`-f markdown-tex_math_dollars+tex_math_single_backslash`), `Typst`, orchestration multi-agents isolée via `invoke_subagent`.

**Spec:** `7 - Livre/specs/prd.md`, `7 - Livre/specs/toc.md`, `7 - Livre/specs/manifest.json`, `7 - Livre/specs/charte-editoriale.md`, `7 - Livre/specs/protocole-mlr-2027.json`, `7 - Livre/specs/contrat-aq.md`.

## Global Constraints

- Zéro contournement d'accès (`AO-01`) : tout `HTTP 403`, `429`, WAF, CAPTCHA, Anubis ou mur payant stoppe net la requête et classe la notice en `statut F` (interdite en preuve, `0 %` de `METADATA_ONLY`).
- Plage stricte de volume (`CA-01`) : `68 080` à `79 920` mots au total, et tolérance ± 8 % sur chacune des 16 unités de `manifest.json`.
- Zéro jargon matriciel (`CA-02`) ni auto-plagiat de 12 mots consécutifs ou plus face à `Corpus/` hors citations entre guillemets (`CA-03`).
- Tous les montants en dollars littéraux sont échappés en `\$` dans les fichiers `.md`, toute formule est écrite en `\(...\)` (`CA-06`), et `Pandoc` est invoqué avec `-f markdown-tex_math_dollars+tex_math_single_backslash`.
- Les volumes `1` à `6` du dépôt sont une carte de repérage, jamais une preuve (`AO-02`) : tout fait qui en provient est réancré sur la source primaire qu'ils citent.
- Ordre des barrières imposé par `contrat-aq.md` : `G1` → `G2` → `G3` passe 1 → `G4` → `G5` lissage → `G3` passe 2 sur le texte final → `G5` rendu.
- Calendrier (`prd.md` § 1) : production et AQ en novembre–décembre 2026, date de gel des faits arrêtée par l'auteur au **2 décembre 2026** (`2026-12-02`), publication en janvier 2027; les dates de 2027 et au-delà sont rédigées comme des échéances à venir.
- Étanchéité stricte d'AQ (`contrat-aq.md`) : aucun sous-agent rédacteur n'exécute `G2`, `G3`, `G4` (rôle critique) ou `G5` sur son propre texte; `gauntlet-loop` n'utilise jamais un tableau de messages partagé public.

## Review Focus

- Faux positifs de l'analyseur `12-grammes` (`CA-03`) sur les intitulés officiels de lois longues (p. ex. *Loi sur la protection des renseignements personnels dans le secteur privé*) : exclure uniquement les segments entre guillemets français `« … »` dûment suivis d'une référence `[n]`.
- Dérive de comptage de mots entre code source Markdown et prose réelle : exclure les blocs de code clôturés, le front matter YAML et les URLs des liens avant de vérifier `[min_words, max_words]`.
- Corruption silencieuse de deux montants en dollars dans un même paragraphe lors des retouches stylistiques de `G4` : réexécuter obligatoirement `verifie_manuscrit.py` après chaque tour de `gauntlet-loop`.
- Contradiction entre un chiffre cité en prose et `registre/faits-empiriques.json` ou `ancres-chronologiques.json` : injecter ces deux JSON en lecture obligatoire à chaque agent rédacteur et auditeur.
- Régression factuelle introduite par l'agent de lissage transversal (`G5`) : restreindre ses modifications aux paragraphes de transition et soumettre son `git diff` à une passe différentielle Wyvern.

---

### Task 1: Outillage déterministe de contrôle (`G1`), d'échantillonnage (`G3`) et d'annexes

**Files:**
- Create: `7 - Livre/outils/verifie_manuscrit.py`
- Create: `7 - Livre/outils/echantillon_aq.py`
- Create: `7 - Livre/outils/genere_annexes.py`
- Test: `7 - Livre/outils/test_outillage_aq.py`

**Interfaces:**
- Consumes: `specs/manifest.json`, `specs/protocole-mlr-2027.json`, `registre/*.json`
- Produces:
  - `verifie_manuscrit.check_manuscrit(root: Path, strict: bool = True) -> list[str]` (retourne la liste vide si `CA-01`..`CA-11` et `CA-17` passent)
  - `echantillon_aq.draw_stratified_sample(root: Path, seed: int, exclude_ids: set[str]) -> list[dict]` (`60` items : `25` empiriques, `20` juridiques, `15` prospectifs/techniques; au moins `2` par unité narrative)
  - `genere_annexes.build_annexes(root: Path) -> list[Path]` (écrit les Annexes `A`, `B`, `C` dans `manuscrit/05 - Annexes/`)

- [ ] **Step 1: Écrire les tests unitaires échouants couvrant les 5 cas limites de `Review Focus`**

```python
def test_forbidden_codes_and_unescaped_dollars_detected(tmp_book):
    errors = check_manuscrit(tmp_book, strict=True)
    assert any("CA-02" in e for e in errors)
    assert any("CA-06" in e for e in errors)

def test_12gram_ignores_quoted_statute_titles_only(tmp_book):
    errors = check_manuscrit(tmp_book, strict=True)
    assert not any("Loi sur la protection" in e for e in errors)

def test_two_seeds_produce_disjoint_60_item_samples(populated_book):
    s1 = draw_stratified_sample(populated_book, seed=202701, exclude_ids=set())
    s2 = draw_stratified_sample(populated_book, seed=202702, exclude_ids={x["claim_loc"] for x in s1})
    assert len(s1) == 60 and len(s2) == 60
    assert {x["claim_loc"] for x in s1}.isdisjoint({x["claim_loc"] for x in s2})
    assert all(sum(1 for x in s1 if x["unit"] == u) >= 2 for u in UNITS_NARRATIVES)

def test_dollar_math_rejected_and_backslash_math_accepted(tmp_book):
    errors = check_manuscrit(tmp_book, strict=True)
    assert any("CA-06" in e and "$0{,}94" in e for e in errors)
    assert not any("CA-06" in e and "\\(0{,}94" in e for e in errors)
```

- [ ] **Step 2: Exécuter `pytest` pour vérifier l'échec initial**

Run: `pytest "7 - Livre/outils/test_outillage_aq.py" -v`
Expected: FAIL (`ModuleNotFoundError` sur `verifie_manuscrit`)

- [ ] **Step 3: Implémenter `verifie_manuscrit.py`, `echantillon_aq.py` et `genere_annexes.py`**

Comptage de mots hors YAML/blocs de code/URLs; indexation par hachage glissant des `12-grammes` de `Corpus/`; stratification déterministe `random.Random(seed)`.

- [ ] **Step 4: Exécuter `pytest` et `verifie_specs.py`**

Run: `pytest "7 - Livre/outils/test_outillage_aq.py" -v; python "7 - Livre/outils/verifie_specs.py"`
Expected: PASS (`0` erreur)

- [ ] **Step 5: Commit de l'outillage**

```powershell
git add "7 - Livre/outils"
git commit -m "Ajouter l'outillage deterministe G1, G3 et generateur d'annexes du 7 - Livre"
```

---

### Task 2: Collecte scientifique ouverte `L+` (`MLR 2027`) et indexation du corpus local

**Files:**
- Create: `7 - Livre/outils/collecte_mlr_ouverte.py`
- Create: `7 - Livre/recherche/manifeste-sources-sha256.json`
- Create: `7 - Livre/recherche/registre-statut-f.json`
- Create: `7 - Livre/sources/ch00-sources.md` .. `ch12-sources.md`
- Test: `7 - Livre/outils/test_collecte_mlr.py`

**Interfaces:**
- Consumes: `specs/protocole-mlr-2027.json`, `sources-locales/*` (dont la copie locale non versionnée de l'essai DeepMind), `Corpus/*`
- Produces: `recherche/corpus_l_plus/*.txt` (UTF-8 intégraux hachés `SHA-256`), `recherche/manifeste-sources-sha256.json` et les `13` bases fermées `sources/ch00-sources.md` à `sources/ch12-sources.md`

- [ ] **Step 1: Écrire le test garantissant l'arrêt sans contournement sur `403`/`429` (`AO-01`) et le hachage `SHA-256`**

```python
def test_blocked_response_logged_as_status_f_without_retry_bypass(mock_http_403):
    entry = fetch_open_source("https://example.org/restricted.pdf", client=mock_http_403)
    assert entry["status"] == "F"
    assert entry["included_in_evidence"] is False
```

- [ ] **Step 2: Vérifier l'échec du test, puis implémenter `collecte_mlr_ouverte.py` et exécuter la collecte sur `RQ1`–`RQ6`**

Interroger uniquement les API ouvertes de `protocole-mlr-2027.json`, extraire en `.txt` UTF-8 les textes intégraux libres et les PDF de `sources-locales/` (l'essai DeepMind n'y sert que d'inspiration; la preuve passe par `arXiv:2606.12683`), calculer les `SHA-256`, noter `AACODS`, réancrer sur source primaire chaque entrée de `registre/` dont le `statut_preuve` vaut `a_reancrer`, consigner la date de gel des faits arrêtée au **2 décembre 2026** (`2026-12-02`; aucune source postérieure) et constituer les 13 dossiers fermés `sources/ch00-sources.md` à `sources/ch12-sources.md` (résumé factuel de 3–5 phrases lu sur texte complet par référence).

- [ ] **Step 3: Vérifier la couverture `CA-09`, `CA-10`, `CA-11`**

Run: `pytest "7 - Livre/outils/test_collecte_mlr.py" -v; python "7 - Livre/outils/verifie_manuscrit.py" --sources-only`
Expected: PASS (seuil `min_included_studies` atteint pour chaque axe `RQ1`–`RQ6`, `0 %` de `METADATA_ONLY`, `0` entrée de registre restée `a_reancrer`)

- [ ] **Step 4: Commit de la base documentaire `L+`**

```powershell
git add "7 - Livre/outils/collecte_mlr_ouverte.py" "7 - Livre/outils/test_collecte_mlr.py" "7 - Livre/recherche" "7 - Livre/sources"
git commit -m "Constituer le corpus ouvert L+ hache SHA-256 et les 13 bases de sources fermees"
```

---

### Task 3: Conception et compilation stricte des 23 figures vectorielles (`Fig-00` à `Fig-22`)

**Files:**
- Create: `7 - Livre/diagrammes/Fig-00.puml` .. `Fig-22.mmd` (selon `manifest.json`)
- Create: `7 - Livre/outils/compile_figures.py`

**Interfaces:**
- Consumes: `specs/manifest.json` (`figures`), `specs/charte-editoriale.md` (§ 4.3 : `10–14` nœuds max, distinction trait plein déterministe / pointillé probabiliste)
- Produces: `7 - Livre/diagrammes/rendus/Fig-00.svg` .. `Fig-22.png`

- [ ] **Step 1: Rédiger les 23 sources `PlantUML` et `Mermaid` et `compile_figures.py`**

Appliquer `-failfast2` pour `PlantUML` et résolution `300 DPI` pour les 3 arbres `Mermaid` (`Fig-06`, `Fig-11`, `Fig-22`).

- [ ] **Step 2: Compiler et vérifier `CA-08`**

Run: `python "7 - Livre/outils/compile_figures.py" --strict`
Expected: PASS (`23/23` figures générées sans avertissement, chacune $\le 14$ nœuds)

- [ ] **Step 3: Commit des figures**

```powershell
git add "7 - Livre/diagrammes" "7 - Livre/outils/compile_figures.py"
git commit -m "Produire et compiler les 23 figures vectorielles du 7 - Livre"
```

---

### Task 4: Rédaction cloisonnée du Liminaire et des Chapitres 01 à 12

**Files:**
- Create: `7 - Livre/manuscrit/00 - Liminaire.md`
- Create: `7 - Livre/manuscrit/01 - Partie I/Chapitre 01 ... .md` à `04 - Partie IV/Chapitre 12 ... .md` (chemins exacts de `manifest.json`)

**Interfaces:**
- Consumes: `specs/prd.md`, `specs/toc.md`, `specs/charte-editoriale.md`, `specs/manifest.json`, `registre/*.json`, `sources/ch00..ch12-sources.md`, `diagrammes/rendus/*`
- Produces: les `13` fichiers Markdown narratifs totalisant `70 000 mots ± 8 %`

- [ ] **Step 1: Rédiger les 4 parties par lots cloisonnés en parallèle (`invoke_subagent`, `TypeName: "self"`, `Workspace: "share"` ou écriture sur fichiers disjoints)**

Chaque agent rédacteur reçoit exclusivement : son contrat d'unité dans `toc.md` et `manifest.json` (`owned_concepts` vs renvois), `charte-editoriale.md`, `registre/*.json` et sa base fermée `sources/chNN-sources.md`.

- [ ] **Step 2: Générer une première version des Annexes `A`–`C` et passer la barrière déterministe `G1`**

Run: `python "7 - Livre/outils/genere_annexes.py"; python "7 - Livre/outils/verifie_manuscrit.py" --strict`
Expected: PASS sur `CA-01` à `CA-11` (`0` code banni, `0` collision `12-grammes`, budgets de mots conformes, `\$` échappés)

- [ ] **Step 3: Commit du premier jet complet conforme `G1`**

```powershell
git add "7 - Livre/manuscrit"
git commit -m "Livrer le manuscrit initial complet (Liminaire, Ch. 01-12, Annexes) conforme G1"
```

---

### Task 5: Exécution étanche des barrières d'AQ `G2` (Wyvern), `G3` passe 1 et `G4` (`gauntlet-loop`)

**Files:**
- Create: `7 - Livre/ancrage/ch00-ancrage.md` .. `ch12-ancrage.md`
- Create: `7 - Livre/aq/recollation-seed-202701.json` et `aq/recollation-seed-202701.md`
- Create: `7 - Livre/aq/gauntlet-log.md`
- Modify: `7 - Livre/manuscrit/**` (rectifications d'ancrage, de recollation et d'écriture)

**Interfaces:**
- Consumes: `specs/contrat-aq.md`, `manuscrit/**`, `sources/**`, `recherche/corpus_l_plus/**`
- Produces: journaux de preuve `ancrage/` et `aq/`, manuscrit vérifié à `100 %` sur `CA-12`, `CA-13` et `CA-15`

- [ ] **Step 1: Exécuter `G2` — Ancrage atomique Wyvern par 13 sous-agents d'audit neufs (`00` à `12`)**

Chaque agent décompose chaque paragraphe en *claims* atomiques, vérifie contre `sources/chNN-sources.md` (`00` à `12`) et `corpus_l_plus/`, rectifie les `imprécis`, retire/réancre les `non supportés` et écrit `ancrage/chNN-ancrage.md`.

- [ ] **Step 2: Exécuter `G3` passe 1 (`seed=202701`)**

Run: `python "7 - Livre/outils/echantillon_aq.py" --seed 202701 -o "7 - Livre/aq/recollation-seed-202701.json"`
Dépêcher un agent `recollateur-1` neuf sur les `.txt` bruts et rectifier jusqu'à `60/60` (`CA-13`). La passe 2 à froid est exécutée à la Tâche 6, sur le texte final.

- [ ] **Step 3: Exécuter `G4` — Boucle `gauntlet-loop` A/B à l'aveugle sur le liminaire et les 12 chapitres**

Présenter en aveugle (`Texte A` / `Texte B`, ordre alterné) chaque unité face aux extraits étalons en français de `manifest.json` à des sous-agents critiques neufs jusqu'à victoire A/B, gains marginaux sur 2 tours ou plafond de budget; consigner chaque tour dans `aq/gauntlet-log.md` et repasser `G1` + différentiel `G2` sur tout paragraphe retouché.

- [ ] **Step 4: Revalider `G1` intégralement et commiter les preuves `G2`, `G3` passe 1 et `G4`**

Run: `python "7 - Livre/outils/verifie_manuscrit.py" --strict`
Expected: PASS (`0` erreur)

```powershell
git add "7 - Livre/manuscrit" "7 - Livre/ancrage" "7 - Livre/aq"
git commit -m "Valider les barrieres d'AQ agentiques G2 (Wyvern), G3 passe 1 et G4 (gauntlet)"
```

---

### Task 6: Lissage transversal, recollation finale à froid, assemblage `Pandoc`/`Typst` et inspection visuelle (`G5`, `G3` passe 2)

**Files:**
- Create: `7 - Livre/outils/assemble_livre.py`
- Create: `7 - Livre/outils/gabarit-livre.typ`
- Create: `7 - Livre/aq/rapport-lissage-et-visuel.md`
- Create: `7 - Livre/aq/recollation-seed-202702.json` et `aq/recollation-seed-202702.md`
- Create: `Corpus/7 - Livre.md`, `Corpus/7 - Livre.pdf` et `7 - Livre/livrables/7 - Livre.html`

**Interfaces:**
- Consumes: `manuscrit/**`, `registre/**`, `ancrage/**`, `aq/**`, `diagrammes/rendus/**`
- Produces: éditions intégrales `.md`, `.html` autonome et `.pdf` inspectées visuellement (`CA-14`, `CA-16` à `CA-18`)

- [ ] **Step 1: Dépêcher un agent `lisseur-editorial` neuf sur l'assemblage complet (`CA-16`)**

Harmoniser les transitions inter-unités et éliminer toute redite résiduelle sans altérer les affirmations sourcées (contrôle différentiel Wyvern sur le `git diff`).

- [ ] **Step 2: Exécuter `G3` passe 2 à froid sur le texte final (`seed=202702`, `CA-14`)**

Run: `python "7 - Livre/outils/echantillon_aq.py" --seed 202702 --exclude "7 - Livre/aq/recollation-seed-202701.json" -o "7 - Livre/aq/recollation-seed-202702.json"`
Dépêcher un agent `recollateur-2` neuf, distinct de `recollateur-1`.
Expected: $\ge 57/60$ (`95 %`) avant correction et `60/60` (`100 %`) après; sinon retour des unités fautives en `G2` puis nouveau tirage disjoint à graine `202703`.

- [ ] **Step 3: Régénérer les Annexes `A`–`C` (`CA-17`) et compiler les éditions `.md`, `.html` et `.pdf`**

Run: `python "7 - Livre/outils/genere_annexes.py"; python "7 - Livre/outils/assemble_livre.py" --all`
Expected: Génération sans erreur de `Corpus/7 - Livre.md`, `7 - Livre/livrables/7 - Livre.html` (`-f markdown-tex_math_dollars+tex_math_single_backslash --embed-resources`) et `Corpus/7 - Livre.pdf` (`Typst`).

- [ ] **Step 4: Inspecter visuellement 100 % des pages rendues et exécuter la vérification finale stricte (`CA-18`)**

Convertir le PDF en images de pages, inspecter chaque page (tableaux, figures, formules, montants `\$`, coupures) dans `aq/rapport-lissage-et-visuel.md`, corriger tout défaut de mise en page, puis relancer `verifie_manuscrit.py --strict`.

Run: `python "7 - Livre/outils/verifie_manuscrit.py" --strict --check-deliverables`
Expected: PASS (`CA-01` à `CA-18` conformes à `100 %`)

- [ ] **Step 5: Commit final du livre assemblé**

```powershell
git add "7 - Livre"
git commit -m "Livrer l'edition integrale verifiee (MD, HTML, PDF) du 7 - Livre"
```
