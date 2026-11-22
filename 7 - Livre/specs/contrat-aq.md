# Contrat d'assurance qualité 100 % agentique — Livre 2027 (v1.2)

Ce contrat définit le protocole de contrôle indépendant auquel est soumis l'intégralité du manuscrit avant publication. **Principe d'étanchéité cardinal** : aucun agent ayant rédigé une unité, généré une figure ou assemblé une bibliographie n'est autorisé à auditer, recoller ou noter son propre livrable.

**Ordre d'exécution.** Les barrières sont numérotées par nature, non par ordre chronologique. L'ordre imposé est : `G1` → `G2` → `G3` passe 1 → `G4` (avec repassage `G1` et `G2` différentiel) → `G5` lissage (avec repassage `G1` et `G2` différentiel) → `G3` passe 2 à froid sur le texte final → `G5` rendu et inspection visuelle. La passe 2 de `G3` mesure ainsi la fiabilité résiduelle du texte réellement publié.

---

## 1. Vue d'ensemble des cinq barrières (`G1` à `G5`)

| Barrière | Rôle d'agent | Entrées inspectées | Critères couverts | Condition de sortie |
|---|---|---|---|---|
| **`G1` — Garde déterministe** | Script `outils/verifie_manuscrit.py` | Fichiers Markdown, `manifest.json`, `registre/*.json`, sources `L+`, figures `.svg`/`.png` | `CA-01` à `CA-11`, `CA-17` | Code de retour `0` sur l'ensemble des contrôles de la section 2.1 |
| **`G2` — Ancrage atomique Wyvern** | Agents `auditeur-wyvern` (contexte neuf, `1` par unité narrative `00`–`12`) | `00 - Liminaire.md` / `Chapitre NN.md`, `sources/ch00..ch12-sources.md`, textes bruts `corpus_l_plus/` | `CA-10`, `CA-12` | `100 %` des affirmations atomiques au verdict `supporté` après rectification ou retrait consigné dans `ancrage/ch00..ch12-ancrage.md` |
| **`G3` — Double recollation à l'aveugle** | Deux agents `recollateur` distincts et indépendants | Deux échantillons stratifiés disjoints de `60` énoncés chacun face aux `.txt` primaires | `CA-07`, `CA-13`, `CA-14` | Passe 1 (`seed=202701`) ramenée à `60/60`; passe 2 à froid (`seed=202702`, `0` chevauchement, texte final) $\ge 95\ \%$ avant correction et `60/60` après |
| **`G4` — Critique éditoriale à l'aveugle (`gauntlet-loop`)** | Paires `batisseur` / `critique` en contextes isolés (`invoke_subagent`, jamais `swarm`) | Unité anonymisée vs extrait étalon anonymisé (ordre `A`/`B` alterné) | `CA-15` | Victoire à l'aveugle, gains marginaux sur `2` tours consécutifs ou plafond budgétaire atteint, suivi d'un repassage `G1` + `G2` différentiel sur les passages retouchés |
| **`G5` — Lissage transversal et inspection visuelle** | Agent `lisseur-editorial` neuf + agent d'inspection visuelle sur rendu | Manuscrit complet assemblé, Annexes `A`–`C`, sorties `.pdf` (`Typst`) et `.html` (`Pandoc`) | `CA-16`, `CA-17`, `CA-18` | `0` redite inter-unités majeure, `0` couture cassée, `100 %` des pages inspectées visuellement sans défaut de rendu |

---

## 2. Spécification détaillée des contrôles

### 2.1 Barrière `G1` — Vérificateur mécanique (`verifie_manuscrit.py`)
Le script s'exécute sans appel de modèle et bloque immédiatement la chaîne si l'une des règles suivantes échoue :
1. **Calibrage (`CA-01`)** : compte de mots de chaque unité (hors front matter `YAML`, blocs de code et `URL`) dans sa plage `[min_words, max_words]` de `manifest.json` et total dans `[68 080, 79 920]`.
2. **Propreté lexicale (`CA-02`)** : aucune correspondance aux expressions régulières de `forbidden_prose_regexes` hors blocs de code ou citations documentées.
3. **Anti-auto-plagiat (`CA-03`)** : extraction des `12-grammes` normalisés du manuscrit (hors citations entre guillemets français `« … »` suivies d'un renvoi `[n]`) comparée aux six fichiers de `../0 - PDF-MD/`; toute collision échoue avec indication du fichier et de la ligne.
4. **Conformité structurelle (`CA-04`, `CA-05`)** : présence de `*Question directrice :*`, des sous-sections prescrites (`0.1`–`0.6` au liminaire, `X.1`–`X.4` dans les chapitres), des encadrés prescrits (`> **Cinq critères permanents` au liminaire, `> **Trois arbitrages sans regret` dans les chapitres), exactement `1` tableau au liminaire, au plus `2` par chapitre et au plus `18 %` de lignes de listes à puces par unité.
5. **Sûreté typographique (`CA-06`)** : aucun caractère `$` non échappé; toute formule écrite en `\(...\)` ou `\[...\]`.
6. **Intégrité documentaire et cryptographique (`CA-08` à `CA-11`)** : existence et hachage `SHA-256` valide de chaque source `L+`, `0` référence vers une notice `METADATA_ONLY`, `statut F` ou un volume du dépôt non réancré, `0` renvoi `[n]` orphelin, couverture minimale par axe selon `min_included_studies` de `protocole-mlr-2027.json`, et compilation sans erreur des `23` figures (`Fig-00` à `Fig-22`).
7. **Concordance des registres (`CA-07`)** : toute date ou valeur chiffrée qui correspond à une clé de `registre/ancres-chronologiques.json` ou `registre/faits-empiriques.json` y est reproduite à l'identique.
8. **Annexes régénérées (`CA-17`)** : le contenu des Annexes `A`–`C` est identique à la sortie de `genere_annexes.py`.

### 2.2 Barrière `G2` — Protocole d'ancrage atomique Wyvern (`CA-12`)
Pour chacune des `13` unités narratives (`00` à `12`), un agent `auditeur-wyvern` neuf reçoit uniquement l'unité, sa liste `sources/chNN-sources.md` (`00` à `12`) et l'accès en lecture aux textes intégraux `corpus_l_plus/` :
1. Segmentation paragraphe par paragraphe et décomposition en **affirmations atomiques vérifiables** (une seule proposition factuelle, chiffrée, historique ou juridique par entrée).
2. Vérification en deux temps : contre la fiche de lecture vérifiée, puis directement dans le texte intégral `L+` en cas d'ambiguïté. Un fait appuyé sur un volume du dépôt (`1` à `6`) est remonté jusqu'à la source primaire que ce volume cite; à défaut, il est `non supporté` (`AO-02`).
3. Attribution d'un verdict strict :
   - `supporté` : correspondance exacte de sens, de périmètre et d'ordre de grandeur;
   - `imprécis` : nuance, condition expérimentale ou juridiction omise $\rightarrow$ reformulation immédiate calquée sur la source;
   - `non supporté` : affirmation absente de la source citée $\rightarrow$ suppression pure et simple, ou réattribution vers une autre source `L+` vérifiée de la base fermée.
4. Production obligatoire du journal `ancrage/chNN-ancrage.md` synthétisé mécaniquement à l'**Annexe C**.

### 2.3 Barrière `G3` — Double recollation stratifiée à l'aveugle (`CA-13`, `CA-14`)
Un script déterministe `echantillon_aq.py` tire **60 affirmations sourcées** à travers le liminaire et les 12 chapitres, avec **au moins 2 énoncés par unité narrative** :
- `25` affirmations empiriques ou quantitatives (marché, bancs d'essai, lois d'échelle, sécurité);
- `20` énoncés réglementaires ou juridiques (`Loi 25`, `BSIF`, `AMF`, `OCRI`, `EU AI Act`);
- `15` énoncés prospectifs ou techniques datés (`PKI`, post-quantique, spécifications `IETF`/`NIST`/`MCP`/`A2A`).

Les éléments listés au § 7 de `prd.md` (points de vigilance probatoire) sont inclus d'office dans la passe 1 lorsqu'ils figurent dans le manuscrit.

Deux passes sont conduites par deux agents neufs distincts :
1. **Passe 1 (`seed=202701`)**, après `G2` : recollation mot à mot contre les fichiers `.txt` bruts; tout écart est rectifié dans le manuscrit et revérifié jusqu'à `60 / 60` (`100 %`).
2. **Passe 2 à froid (`seed=202702`, exclusion totale des paragraphes de la passe 1)**, sur le texte final après `G4` et le lissage `G5` : mesure la fiabilité résiduelle réelle du livre. Si le score avant correction est `< 57 / 60` (`95 %`), les unités fautives retournent en barrière `G2` complète, puis un nouveau tirage disjoint est effectué à graine incrémentée (`202703`, `202704`, …).

### 2.4 Barrière `G4` — Boucle critique de tenue littéraire (`gauntlet-loop`, `CA-15`)
Pour garantir que l'ouvrage se lit comme un essai de direction de premier plan et non comme une compilation technique :
1. **Étanchéité** : invocation par `invoke_subagent` (jamais sur tableau partagé public) d'un agent `critique` neuf à chaque tour, ignorant tout des consignes de génération et de l'identité de l'extrait évalué.
2. **Barre nommée, récupérable et comparable** : extraits en français de longueur équivalente, exempts de codes internes, tirés des passages étalons déclarés dans `manifest.json` (`Ouverture` du *Compendium 2027*, sections `0.1`–`0.2`; `Chapitre 48`, sections `48.4` et `48.8`). Aucun texte en anglais n'entre dans la comparaison, pour préserver l'aveugle.
3. **Verdict binaire forcé** : présentation anonymisée `Texte A` / `Texte B` (ordre inversé à chaque tour), sans note sur 10. Le critique désigne le gagnant sur la clarté argumentative, la densité d'idées, le rythme de lecture et la rigueur épistémique, puis énonce **un seul écart majeur actionnable**.
4. **Garde-fou d'intégrité factuelle** : toute réécriture effectuée par le bâtisseur durant `G4` repasse obligatoirement par `G1` et par un contrôle différentiel `G2` afin qu'aucune amélioration stylistique n'introduise d'affirmation non sourcée.
5. **Arrêt et traçabilité** : consignation dans `aq/gauntlet-log.md` (plafond budgétaire fixé au lancement avant le tour 1).

### 2.5 Barrière `G5` — Lissage transversal et inspection visuelle (`CA-16` à `CA-18`)
1. **Lissage des coutures** : un agent `lisseur-editorial` neuf parcourt le liminaire et les 12 chapitres dans l'ordre de lecture continu pour harmoniser les transitions, unifier le registre et purger toute explication dupliquée en violation des contrats `owned_concepts` de `manifest.json`. Ses modifications se limitent aux transitions et aux redites; son `git diff` passe un contrôle `G2` différentiel.
2. **Régénération des annexes** : exécution automatique de `genere_annexes.py` depuis `registre/` et `ancrage/`.
3. **Rendu et inspection visuelle** : compilation du PDF (`Typst`) et du HTML autonome (`Pandoc` avec `-f markdown-tex_math_dollars+tex_math_single_backslash --embed-resources`), conversion en captures page par page et inspection visuelle complète par agent dédié (détection de débordements de tableaux, veuves et orphelines critiques, caractères cassés, formules non rendues ou montants `\$` altérés).
