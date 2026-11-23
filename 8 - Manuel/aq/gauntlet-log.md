# Journal de comparaison critique à l'aveugle G4 (`gauntlet-loop`, CA-15)

- **Barrière :** `G4` (`CA-15`, `specs/contrat-aq.md` § 2.4 et protocole `gauntlet-loop`)
- **Étalons de référence :** extraits anonymisés de `3 - Compendium 2027/` (`00 - Ouverture` § `0.1–0.2` et `Chapitre 48 - Revue de littérature` § `48.2–48.10`), comparés en français canadien sur quatre critères : (1) précision technique et densité analytique, (2) rigueur argumentative et démarcation faits/limites/conjectures, (3) clarté, rythme et qualité du français technique, (4) utilité concrète pour un architecte principal ou responsable fiabilité.
- **Étanchéité :** critiques `DeepInvestigator` isolés en contexte neuf, lisant exclusivement `Extrait-A.md` et `Extrait-B.md` anonymisés, avec alternance et inversion des emplacements `A`/`B` entre unités et entre tours, et plafond strict de deux tours de correction par unité.
- **Bilan global :** **`4 / 5` unités victorieuses** (`00-liminaire`, `ch02`, `ch03`, `ch04`), **`1` unité clôturée au plafond de 2 tours de correction** (`ch01`, en raison de l'asymétrie de genre entre spécification d'un extracteur mono-appel borné et revue transversale multi-agents, tout en ayant corrigé l'intégralité des défauts internes relevés au fil des trois tours).

---

## Tableau récapitulatif des évaluations A/B

| Unité | Tour | Slot candidat | Étalon anonymisé | Verdict binaire | Vainqueur | Action appliquée |
| :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| `00-liminaire` | 1 | `A` | `Compendium 2027` § `0.1–0.2` | `A > B` | **Candidat (`00-liminaire`)** | Victoire directe ; suivi d'allègement lexical consigné pour `G5`. |
| `ch01` | 1 | `B` | `Chapitre 48` § `48.3–48.4` | `A > B` | Étalon | Retouche 1 (`Chapitre 01.md`) : reformulation Partition `80/20`, distinction `_walk_strict_rules` / mots-clés racine, précision sur `categorie_sinistre` et `_check_grounding`, rôle distinct de `_INPUT_SCHEMA` vs `HarnessExtraction`, légende `Tableau 1.1`. |
| `ch01` | 2 | `A` | `Chapitre 48` § `48.3–48.5` | `B > A` | Étalon | Retouche 2 (`Chapitre 01.md`) : correction `step_trace` (`8` jalons logiques) vs boucle `while` à `max_repair_retries = 2` (`3x` appels pire cas), distinction `output_sha256` (non signé) vs `JWS`, limites de `_check_grounding`, retrait des backticks superflus sur les nombres en prose. |
| `ch01` | 3 | `B` | `Chapitre 48` § `48.3–48.5` | `A > B` | Étalon (plafond atteint) | Arrêt au plafond de `2` tours de correction ; prise en compte finale immédiate de 4 retouches ponctuelles signalées (`examine` singulier à `L21`, retrait du pléonasme `~20 %` et du ratio `7/8`, attribution `JWS` au `§ 1.4` vs condensats `§ 1.1–1.2`, retrait du terme impropre « horodatage »). |
| `ch02` | 1 | `A` | `Chapitre 48` § `48.5–48.6` | `B > A` | Étalon | Retouche 1 (`Chapitre 02.md`) : tranche initiale trop courte ; suppression des lourdeurs méta-éditoriales (`L21`, `L27`) et explicitation du périmètre de `validate_obo_delegation` en aval de la validation JWS/schéma et d'un cache distribué anti-rejeu `jti`. |
| `ch02` | 2 | `B` | `Chapitre 48` § `48.4–48.9` | `B > A` | **Candidat (`ch02`)** | Victoire sur tranche complète `§ 2.1` inversée en `B` ; suivi des précisions `RFC 7493` (*surrogates* isolés hors UTF-8) et statut OpenID *Final* (`Tableau 2.1`) consigné pour `G5`. |
| `ch03` | 1 | `B` | `Chapitre 48` § `48.8–48.10` | `B > A` | **Candidat (`ch03`)** | Victoire directe ; coquille `modèle privilège` et cadrage symétrique OPA/Cedar + couverture de lignes consignés pour `G5`. |
| `ch04` | 1 | `A` | `Chapitre 48` § `48.2` | `A > B` | **Candidat (`ch04`)** | Victoire directe ; vérifié sur disque qu'aucune coquille de chemin n'existait dans `Chapitre 04.md#L225` (artéfact du script de masquage de `scratch/`) ; piste de table synthétique juridique consignée pour `G5`. |

---

## Détail des écarts majeurs relevés et résolution par unité

1. **`00-liminaire` (Tour 1 — Gagné en `A` face à `B`)**
   - Critique `02882b5a` (`DeepInvestigator`). Force du candidat : précision empirique datée (`2 décembre 2026`, Banque du Canada avec limites d'échantillonnage, `MAP`, `MAST`, Kraishan avec `OR = 2,96` sans lien causal, exclusion Gartner) et arbitrages exécutables `DISC-01..05`. Point noté pour `G5` : alléger les renvois éditoriaux denses de l'ouverture tout en maintenant le volume sous `3 780` mots (`3 774` actuellement).
2. **`ch01` (Tours 1, 2, 3 — Plafonné à 2 tours de correction)**
   - Tour 1 (`e6e76a38`, candidat en `B`) : relevait une confusion autour de la Partition 80/20 (laissant croire à 20 % d'incohérence syntaxique), une tension entre les règles récursives de `strict: true` et l'interdiction racine d'`allOf`/`if`/`then`/`else`, l'obligation non nulle sur `categorie_sinistre`, et l'assimilation entre `_INPUT_SCHEMA` et `HarnessExtraction`. Corrigé dans `Chapitre 01.md` par alignement exact sur `harness_proto/pipeline.py`.
   - Tour 2 (`022a0483`, candidat en `A`, tranche étendue à `L13–105`) : relevait l'incohérence entre un flux linéaire en `8` étapes (`1/8`) et la boucle `while` (`max_repair_retries = 2`, jusqu'à `3x` appels modèle), ainsi que l'absence de signature `JWS` dans `8_seal`. Corrigé dans `Chapitre 01.md` (`L80–102` et `Tableau 1.1`).
   - Tour 3 (`2e8b28b2`, candidat en `B`) : a validé l'amélioration de fond mais maintenu `VAINQUEUR: A` sur l'étalon bibliographique transversal (`Chapitre 48`), tout en signalant quatre défauts précis corrigés immédiatement dans `Chapitre 01.md` (retrait du pléonasme `environ ~20 %` et du pseudo-ratio `7/8` à `L25`, rattachement explicite de `RFC 7515` `JWS` au `§ 1.4` à `L31`, suppression du mot impropre « horodatage » pour `output_sha256` à `L85`, et vérification du singulier `l'étude ... examine` à `L21`). Arrêt conforme au plafond de 2 retouches de `contrat-aq.md` / `gauntlet-loop`.
3. **`ch02` (Tour 1 perdu en `A`, Tour 2 gagné en `B`)**
   - Tour 1 (`f126c109`, candidat en `A`) : la tranche initiale coupait `G0-EX-CH02-01` avant SSF/CAEP et CIBA, et soulignait la lourdeur d'auto-justification interne ainsi que le besoin de situer les responsabilités amont (`JWS`, schéma complet à `L29`, cache distribué `jti`) vis-à-vis de `validate_obo_delegation`. Corrigé en `Chapitre 02.md` (`L21`, `L27`, `L29`, `L71–75`).
   - Tour 2 (`b0f4bdfc`, candidat en `B`, section `2.1` complète) : victoire de `ch02` grâce à la densité exécutable (`RFC 8693/8707/9449/9396`, `Ballot SC-081v3`, `SSF/CAEP` irréversible, `CIBA I-JSON/JCS`). Points techniques mineurs (`RFC 7493` *lone surrogates* hors UTF-8 à `L89`, distinction *Final* OpenID Foundation au `Tableau 2.1`) planifiés pour le lissage `G5`.
4. **`ch03` (Tour 1 — Gagné en `B` face à `A`)**
   - Critique `8e075ec8`. Victoire nette sur l'instrumentation déterministe hors modèle (`NISTAML.015/013`, `ASI01/02/06`, piège `undefined` Rego, `verify_rego_default_deny`, `OpaPolicyEngine.evaluate`/`run_coverage`). Coquille `le modèle privilège` (`L17`), cadrage transparent du choix `OPA / Rego` (`L23–41`) et précision « couverture de lignes à `100 %` » consignés pour le lissage `G5`.
5. **`ch04` (Tour 1 — Gagné en `A` face à `B`)**
   - Critique `35bfb9bc`. Victoire nette sur les relations métamorphiques sans oracle et le schéma `2027-B001` ; vérification sur disque confirmant l'intégrité du chemin `8 - Trousse/schemas/adr_2027_b001.schema.json` à `L225`.

---

## Contrôle post-G4 (`G2` différentiel, `G0` et `G1`)

Toutes les modifications apportées en `G4` dans `Chapitre 01` et `Chapitre 02` font l'objet d'un contre-audit `G2` différentiel indépendant (`Auditeur G2 Diff Post-G4`), consigné dans `ancrage/ch01-ancrage.md` et `ancrage/ch02-ancrage.md`, suivi de la ré-exécution complète des barrières `G0` (`execute_g0.py --verify-sync-manifest`), de la régénération des Annexes (`genere_annexes.py`) et de `G1` (`verifie_manuscrit.py --strict`).
