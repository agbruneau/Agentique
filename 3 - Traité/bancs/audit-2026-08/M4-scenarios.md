# M4 — scénarios, gouvernance et preuves : constats

Périmètre audité : `crates/sim-agents/` — `essaim.rs`, `scenario.rs`,
`scenario_d.rs`, `scenario_m.rs`, `gouvernance.rs`, `conformite.rs`, `dettes.rs`,
`partage.rs`, `glossaire.rs`, `lib.rs`, `bin/campagne.rs`, tout `examples/`, tout
`tests/`. Les modules de mécanismes sont hors périmètre ; ce qu'ils portent
n'apparaît ici que lorsqu'une affirmation du périmètre porte sur eux.

Suite exécutée dans un `CARGO_TARGET_DIR` isolé : le `target/` du dépôt a été
vidé sous l'éditeur de liens en cours de compilation par une exécution
concurrente (`cannot find …symbols.o`), ce qui n'est pas un défaut du code.

```
cargo clippy -p sim-agents --all-targets --release   → Finished, 0 diagnostic
cargo test   -p sim-agents --release                 → 290 tests, 290 ok, 0 échec
cargo doc    -p sim-agents --no-deps                 → Finished, 0 lien cassé
cargo check  -p sim-viz    --release                 → Finished (le consommateur compile)
```

Avant correctifs : 282 tests. Huit ajoutés, aucun retiré, aucun relâché.

---

## 1. `partage.rs:33` — l'encodage à neuf décimales détruit le dépôt unitaire (EX-V09, NF-03)

**Constat.** `fn f(x: f64) -> String { format!("{x:.9}") }` arrondissait tous les
flottants du lien. `Params::verrouillage()` **calcule** son dépôt unitaire —
φ_max·(−ln γ)/(n·τ/T) — et n'a donc pas la forme d'un cran de curseur.

**Preuve.** Test écrit avant le correctif, exécuté sur le code d'origine :

```
---- partage::tests::le_depot_unitaire_pose_traverse_le_lien_sans_perte ----
assertion `left == right` failed: le dépôt unitaire a changé de valeur en traversant le lien
  left: Some(8.2313e-5)
 right: Some(8.231290285767679e-5)
```

et, sur les autres flottants du lien :

```
---- partage::tests::aucun_champ_flottant_nest_arrondi_par_lencodage ----
 left: gamma: 0.9523809523809523, phi_min: 0.0003333333333333333, eta_min: 0.3333333333333333,
       periode_cycle_ms: 50.333333333333336
right: gamma: 0.952380952,        phi_min: 0.000333333,           eta_min: 0.333333333,
       periode_cycle_ms: 50.333333333
```

Le texte du PRD qu'EX-V09 transpose : *« Toute exécution est partageable par une
URL encodant graine + configuration ; le destinataire voit exactement la même
chose. »* Cinq chiffres significatifs sur dix-sept ne sont pas « exactement la
même chose », et NF-03 ne rattrape rien puisque la version, elle, est la bonne :
la figure change sans le moindre refus. C'est la panne que le commentaire du
champ `q` décrit lui-même — *« C'est le critère de sortie (4) de la phase 2 qui
tombait »* — revenue par la précision au lieu de l'omission.

Le test qui gardait ce critère, `sortie_phase_2::critere_4_un_lien_partage_reproduit_la_figure`,
ne pouvait pas le voir : il n'exerce que `Params::scenario_b()`, dont
`depot_unitaire` vaut `None` et s'encode `q=auto`.

**Changé.** `format!("{x}")` — la plus courte écriture décimale qui se relit à
l'identique. Deux tests ajoutés (`partage.rs`), l'un sur le préréglage
« verrouillage » avec comparaison de trace, l'autre sur les quatre autres
flottants.

**Conséquence.** Un lien de préréglage reproduit la figure. Les liens produits
par une version antérieure du binaire restent refusés par NF-03, donc aucun lien
existant n'est réinterprété.

---

## 2. Cinq blocs PD8 sur dix citent une page qui ne résout pas dans le traité livré (F2)

**Constat.** `Traité.pdf` du dépôt est la **troisième** édition, 15 août 2026,
**143 pages** (mesuré : `pymupdf.open("Traité.pdf").page_count`). Sa table des
matières donne §1.2 p. 12-16, §1.3 p. 17-22, §2.1 p. 23-29, §4.2 p. 61-66,
§5.3 p. 82-86, §6.2 p. 91-95, §8.3 p. 124-127, conclusion p. 128-129.

Recherche du texte cité, verbatim, page par page :

| bloc | fichier | citait | ce qui s'y trouve | mesuré |
|---|---|---|---|---|
| A | `scenario.rs:58` | §1.3, p. 21 | §1.3, mais pas la thèse | thèse §2.1 **p. 25** ; tableau 3 p. 18 ; figure 0 p. 4 |
| B | `scenario.rs:218` | §1.2, p. 13 | §1.2, ni la thèse ni l'algorithme 2 | thèse **p. 16** ; algorithme 2 **p. 14** |
| D | `scenario_d.rs:25` | §2.1, p. 22 | **§1.3** — hors de la section citée | thèse **p. 26** ; figure 2.1c **p. 28** |
| K | `gouvernance.rs:23` | §5.3, p. 63 | **§4.2** — hors de la section citée | tableau 16 **p. 84** |
| M | `scenario_m.rs:41` | §8.3, p. 94 | **§6.2** — hors de la section citée | thèse **p. 127** |

Le §12 A du PRD et le §7 posent que *« Les pages citées sont celles de la
deuxième édition du traité (F2) »*, et F2 ajoute : *« une page sans édition n'est
pas une provenance imprécise, c'est une provenance fausse »*. `CLAUDE.md`, qui
prévaut, dit que la pagination est celle de la troisième édition. Sous l'une ou
l'autre lecture, un lecteur qui ouvre le seul traité présent dans le dépôt à la
page citée ne trouve pas la phrase citée.

Trois recoupements internes confirment le sens de la correction plutôt que le
sens inverse : `stigmergie.rs:639-640` arme déjà `PLANCHER` et `HORS_DOMINANTE`
sur « §1.2, **p. 16** », `sim-viz/src/scenario_b.rs:67` pose
`SOURCE_BORNES = "§1.2, p. 16"`, et le commentaire de `sim-viz/src/scenario_b.rs:61`
enregistre qu'un panneau *« annonçait « p. 13 » sous une légende qui disait
« p. 16 » »*. Le dépôt avait donc déjà corrigé cette page ailleurs ; les blocs ne
l'avaient pas suivie.

**Changé.** Les cinq `source` portent la page mesurée **et nomment leur édition**
(`3ᵉ éd.`). Idem pour `Comparaison::diametres()` (`scenario.rs:146`), l'en-tête de
module de `scenario_m.rs`, et l'assertion de `scenario_d.rs:392` qui vérifiait
`contains("p. 22")`. Test ajouté :
`scenario::tests::les_blocs_verifies_nomment_leur_edition`, dont la
documentation porte le tableau de mesure ci-dessus.

**Conséquence.** Les cinq citations résolvent. Les cinq autres blocs — E, F, G,
J, L — **résolvent déjà** dans la troisième édition (mesuré : algorithme 3 p. 21,
figure 5.2 p. 80, tableau 15 p. 81, §7.1 p. 104, figure 6.1 p. 91, tableau 13
p. 72, figure 7.2 p. 107, tableau 19 p. 110) ; il leur manque seulement la
mention d'édition, et leurs fichiers sont hors périmètre.

---

## 3. `glossaire.rs` — sept provenances de page fausses, et un renvoi §8.3 ambigu lu du mauvais côté

**Constat (a).** Les entrées du glossaire portaient « §1.3, p. 21 » (×3),
« §1.2, p. 13 » (×8) et « conclusion p. 94 ». Mesuré dans le traité livré :
tableau 3 p. 18, figure 0 p. 4, « 2 en permanence » p. 18, algorithme 2 p. 14,
γ ∈ (0,1) p. 14, les deux bornes p. 16, idempotence en conclusion p. 129 —
p. 94 étant dans le §6.2.

**Constat (b), `glossaire.rs:226`.** L'entrée « ℓ₉₉ » portait `provenance: "§8.3"`.
Le champ est défini comme *« section du traité, nomenclature du produit, ou
réglage de l'interface »*, donc « §8.3 » s'y lit comme une section du **traité**.
Or le §8.3 du traité est *« Buts incompatibles : escalade, force, trêve »*
(p. 124-127) et ne parle pas de latence ; la séparation des deux ℓ₉₉ — entrée du
milieu contre sortie de réponse — est le §8.3 du **PRD**. C'est exactement le
piège que `CLAUDE.md` signale : *« Un renvoi qui peut se lire des deux côtés se
qualifie. »*

**Changé.** Les pages, une par une, avec l'édition. La provenance de ℓ₉₉ devient
« nomenclature du produit — §8.3 du PRD ; la grandeur, elle, est du §6.1 ».

**Conséquence.** Le glossaire cesse d'attribuer au traité une règle du produit, et
d'envoyer le lecteur sur des pages qui ne portent pas ce qu'il cherche.

---

## 4. `conformite.rs:261` — un `clamp(0.0, 1.0)` rendait vrai par construction le test qui devait établir le zéro de Φ_c

**Constat.** `estimer` rendait `phi_c: (accord_observe - sous_independance).clamp(0.0, 1.0)`
alors que le champ se documente *« dans [−1, 1] par construction »*
(`conformite.rs:105`) : la doc affirmait un domaine que le code ne tenait pas.

L'effet portait sur une preuve. Le test
`une_population_decorrelee_vaut_environ_zero` construisait cinq agents parcourant
les cinq mêmes valeurs dans cinq ordres décalés, puis asserte `phi_c == 0.0`.
Mesuré sur ce jeu : `accord_observe = 0.0`, `accord_sous_independance = 0.2`,
donc **Φ_c brut = −0,2**. L'assertion passait par l'écrêtage, pas par
l'estimateur. Et le jeu de données n'était pas décorrélé : une population qui
n'atteint **jamais** l'accord de rang est anti-conforme — cinq tirages
indépendants n'y parviendraient qu'avec une probabilité de 5⁻¹⁰⁰. Le zéro de
l'échelle n'était donc établi par rien.

**Changé.** Écrêtage retiré. Le test devient
`une_population_qui_ne_saccorde_jamais_rend_un_phi_c_negatif` et asserte
Φ_c = −0,2 à 10⁻⁹ ; un second test,
`une_population_reellement_decorrelee_reste_dans_sa_precision`, tire douze agents
indépendamment dans la même loi et exige |Φ_c| ≤ 1/√k.

**Conséquence.** Une population anti-conforme cesse d'être indiscernable d'une
population indépendante. Aucune mesure livrée ne bouge : les Φ_c du scénario M
sont positifs (≈ 0,17 à 0,23), `depasse_sa_precision()` rendait déjà `false` sur
un négatif écrêté, et les onze tests de `sortie_phase_6` passent inchangés.

---

## 5. `lib.rs` — trois défauts de la liste `hors_perimetre()` (PD6)

**(a) `lib.rs:114` — deux `\n` littéraux dans une chaîne affichée.** L'entrée sur
les oracles était écrite `"… aucune exécution — \n         \`CONSERVATION\`…"`,
c'est-à-dire avec des sauts de ligne et neuf espaces **dans la donnée**, là où les
dix-neuf autres entrées utilisent la continuation `\`. `sim-viz/src/lib.rs:882`
passe cette liste telle quelle à `section()`, qui la rend en puces. Corrigé en
continuation.

**(b) `lib.rs:114` — l'entrée affirmait un appelant qui n'existe pas.** Elle
disait des six oracles non armés que *« leurs `armer_oracles` n'ont d'appelant que
dans leurs propres tests »*. Mesuré :

```
$ grep -rn "armer_oracles(\|armer_oracle(" crates --include=*.rs | grep -v "fn armer"
crates/sim-agents/src/directive.rs:295,305,324   (mod tests)
crates/sim-agents/src/scenario.rs:403            (production)
crates/sim-agents/src/scenario_d.rs:115          (production)
crates/sim-agents/src/scenario_m.rs:127          (production)
crates/sim-agents/src/stigmergie.rs:641          (production)
crates/sim-milieu/src/groupe.rs:483,498          (mod tests)
crates/sim-milieu/src/journal.rs:777,874,894     (mod tests)
crates/sim-milieu/src/replication.rs:506         (mod tests)
```

`Alignement::armer_oracles` (`alignement.rs:62`) et `PushPull::armer_oracle`
(`agregation.rs:181`) n'y figurent pas : ils n'ont **aucun** appelant, pas même un
test. `ACCORD_LOCAL` et `CONSERVATION` ne sont donc inscrits à aucun registre, où
que ce soit — un cran plus fort que ce que l'entrée déclarait. Le compte de
quinze et de neuf, lui, est exact : catalogue = `PLANCHER`, `HORS_DOMINANTE`,
`CONSERVATION`, `ACCORD_LOCAL`, `D1`, `D2`, `UN_SEUL_PROPRIETAIRE`,
`TOUTE_PARTITION_A_UN_PROPRIETAIRE`, M1-M4, M10, R1, R2 ; armés en production =
les deux du fourragement, les cinq du journal, les deux de la réplication.

L'entrée voisine sur PD10 (`lib.rs:124`) disait qu'*« aucun affichage ne les lit »* ;
elle dit maintenant aussi qu'aucun registre ne les porte à l'exécution.

**(c) `lib.rs:79` — un curseur de l'interface qui ne règle rien, non déclaré.**
`scenario_a(n, p, …)` fait `let _ = p;` (`scenario.rs:187`) : aucun des comptes du
tableau 3 n'en dépend. `sim-viz/src/scenario_a.rs:439-440` expose pourtant
`poignee(ui, "p — partitions", …)` avec un `Slider::new(&mut self.p, 1..=64)`, et
`scenario_a.rs:124` le passe à la fonction. Le curseur bouge, aucun chiffre ne
bouge, et rien à côté ne le dit. Entrée ajoutée à `hors_perimetre()`, et la
documentation de `scenario_a` le nomme.

**Vérification de la liste dans l'autre sens.** Les autres entrées ont été
recoupées contre le code : `tableau_15` fait bien `let _ = alea;`
(`allocation.rs:235`) ; `Mode::Retard` n'est utilisé que pour un libellé
(`consensus_lineaire.rs:70`) ; `PrixDeLanarchie::rapport_mesure` n'a aucun
producteur ; `Agregat::absorber` et `faibles` n'ont d'appelant que dans
`couverture.rs` (tests) ; `Registre::criteres_locaux` de même ; `sim-viz` n'importe
que `BLOC_A`, `BLOC_B`, `glossaire` et `conformite`, jamais `dettes`. Le compte de
dix mécanismes sans appelant tient : six des phases 1-5 (`adhesion`, `alignement`,
`causalite`, `consensus_lineaire`, `directive`, `reconfiguration` — aucune
référence hors de leur propre fichier), deux du ch. 8 dans `sim-agents`
(`deliberation`, `arbitrage` — référencés par le seul `sortie_phase_6.rs`), et
deux dans `sim-milieu` (EX-M25, EX-M26).

---

## 6. `tests/sortie_phase_2.rs:130` — le critère de sortie (5) reposait sur une assertion qui ne peut pas échouer

**Constat.** Le §9 du PRD écrit : *« Le préréglage « oscillation » diverge avec un
compteur de pannes strictement nul. »* Le test l'établissait par
`assert_eq!(c.pannes, 0)`. Or `elasticite::Controleur::pannes` est posé à 0 à la
construction (`elasticite.rs:207`) et **aucun chemin ne l'incrémente** — les trois
seules autres occurrences du champ sont des assertions de test. L'assertion est
donc vraie par construction du type ; elle ne mesure rien.

Le même défaut existe pour `cascade::pannes_reelles` dans `sortie_phase_4.rs`, à
ceci près que `cascade.rs:152` le documente déjà : *« Les assertions
`pannes_reelles == 0` ne peuvent donc pas échouer. »*

**Changé.** Les deux tests disent désormais ce qu'ils prouvent. Celui de la phase
2 gagne le volet réfutable qui manquait : le réglage nominal, sur la même charge
et le même nombre de périodes, doit rester dans une bande au moins trois fois plus
étroite. Sans lui, un contrôleur qui oscillerait dans les deux réglages passait le
critère.

**Ce que la mesure a rendu au passage, et qui n'était pas prévu.** La première
version du volet réfutable comparait aussi les inversions. Elle a échoué :

```
---- critere_5_loscillation_diverge_sans_aucune_panne ----
nominal 14 inversions contre oscillation 14
…
 left: (9, 14, 11, 31, 14, 32)   (amplitude, inversions, population finale — nominal puis oscillation)
```

À 200 périodes, charge 80, service 10 : le réglage **nominal inverse exactement
autant** que le réglage « oscillation », quatorze fois l'un comme l'autre. Seule
l'amplitude sépare les deux — 9 contre 31, population finale 11 contre 32.
C'est la réserve du §0 sur le contrôleur d'élasticité, mesurée ici sur le
compteur d'inversions ; l'assertion finale porte donc sur l'amplitude, et le
commentaire du test porte les chiffres.

---

## 7. `gouvernance.rs:349` — « l'agrégat n'est borné par rien » établi par une conséquence arithmétique

**Constat.** Le critère (1) du scénario K asserte d'abord
`amplification_par_client(true) == 1,1` et `amplification_agregee(100, true) == 110`,
puis ajoute `assert!(agregee(100) > par_client * 50.0)` avec le message *« l'agrégat
n'est borné par rien »*. 110 > 55 est impliqué par les deux lignes précédentes :
l'assertion ne peut pas échouer si elles passent, et elle n'établit rien sur
l'absence de plafond.

**Changé.** Remplacée par la propriété réfutable : l'agrégat vaut 1,1 × clients et
croît strictement, vérifié sur 1, 10, 10³, 10⁵ et 10⁷ clients.

---

## 8. `essaim.rs:96` — la doc d'`intervalle_max` affirme une unité que la moitié du code ne rend pas

**Constat.** La doc disait *« Nombre d'enregistrements que ce membre a le droit de
lire par cycle »*, alors que la branche `Perception::Voisinage` rend
`cardinal_max`, un nombre de **voisins**. Le PRD §8.3 et `CLAUDE.md` font de la
confusion de deux grandeurs homonymes un défaut bloquant ; ici les deux ne sont
même pas homonymes, elles sont fondues dans une seule signature.

**Changé.** La doc nomme l'unité de chaque branche et dit que les deux ne
s'additionnent pas. Un seul appelant en production (`stigmergie.rs:687`), sur la
branche `IntervalleMilieu`.

---

## 9. `scenario_m.rs` — une affirmation de la documentation que rien ne vérifiait

**Constat.** La doc de `scenario_m` porte : *« À 0, la population est décorrélée et
le résultat doit être identique à celui du scénario B — c'est ce qui rend le
scénario honnête : le curseur au repos ne change rien. »* Les deux fonctions
construisent pourtant leur moteur séparément — `scenario_b` déclare un modèle de
faute et trois conditions de couverture que `scenario_m` ne déclare pas — et aucun
test ne comparait les deux chemins.

**Changé.** Test ajouté,
`a_curseur_au_repos_le_scenario_m_rejoue_le_scenario_b` : à mêmes réglages et même
graine, Φ_c et la fraction hors dominante doivent être **égaux bit à bit** entre
les deux chemins. Il passe — l'affirmation était vraie, elle n'était pas établie.

**Conséquence.** Un écart de câblage entre les deux chemins ne pourra plus se lire
comme un effet de la conformité.

---

# Anomalies identifiées et **non** corrigées

## A. `dettes.rs:186` — `verdicts` efface sept bornes là où le réglage n'en invalide que quatre

Le critère d'effacement est `familles.diversite_effective() < familles.n()`,
c'est-à-dire une violation démontrable de l'indépendance des **tirages**. Trois
des sept dettes supposent l'indépendance d'autre chose : la deuxième celle des
*défaillances* de répliques (§2.1), la troisième celle des *délais* de gigue
(§2.3), la cinquième celle des *épisodes* échantillonnés (§3.3). Un curseur de
familles ne touche à aucune des trois, et leurs bornes sont effacées avec les
quatre autres. NF-14 dit *« une hypothèse violée efface la borne »* ; effacer une
borne dont l'hypothèse tient est l'erreur symétrique, et le §9 du PRD écrivait
d'ailleurs *« Les **quatre** bornes que le produit sait mesurer s'effacent »*.

**Motif du non-correctif.** Le corriger change le critère de sortie de la phase 6,
qui compte sept effacements dans `sortie_phase_6.rs:103,148` et dans
`scenario_m.rs:241`, et qui est consigné au §0.1 du PRD — document que je n'ai pas
le droit de modifier. La documentation de `verdicts` nomme désormais l'écart ;
la décision appartient au produit.

## B. `tests/sortie_phase_6.rs:125` — un point du critère de sortie non réfutable au-delà de `part = 0`

`aucun_oracle_de_surete_ne_tombe_pendant_leffacement` asserte
`violations_de_surete == 0` pour `part ∈ {0 ; 0,5 ; 1}`. Vérifié :
`Params::bornes_applicables()` rend `Err` dès `part_conforme > 0`
(`stigmergie.rs:351`), et `verifier_bornes` sort avant d'évaluer les oracles
(`stigmergie.rs:883-886`). Le silence des oracles est donc tenu par construction
pour les deux dernières valeurs. **Le test le dit déjà lui-même** et vérifie à la
place ce qui reste réfutable ; laissé tel quel, l'aveu étant à sa place et le
§0.1 du PRD le consignant.

## C. `scenario.rs:547` — `chaque_scenario_porte_son_bloc_de_trois` est entièrement subsumé

Il vérifie sur A et B ce que `les_dix_blocs_portent_leur_section_et_leur_page`
vérifie sur les dix. Il ne peut pas échouer seul. Redondant plutôt que
tautologique ; retirer un test est une décision d'inventaire, pas un correctif.

## D. `bin/campagne.rs:156-158` — JSON assemblé sans échappement

`entete` et `LIBELLE` sont interpolés dans des chaînes JSON sans échappement, et
`args.sigma` / `args.kappa` sont écrits en flottants bruts. Aucune des deux
constantes ne contient de guillemet ni de contre-oblique aujourd'hui, donc le
rapport produit est valide ; `--sigma nan` écrirait `"sigma": NaN`, qui ne l'est
pas, mais l'ajustement échoue et sort en code 1 avant l'écriture. Latent, non
atteignable par le chemin livré ; signalé plutôt que corrigé.

## E. `cycle_de_vie.rs` — module sans appelant, non déclaré

Sa seule référence hors de son fichier est `gouvernance.rs:332`, dans `mod tests`.
Il n'est pas dans `hors_perimetre()`. Il est couvert transitivement par l'entrée
« huit des dix blocs livrés … n'ont aucun point d'affichage », qui inclut K —
l'ajouter nommément est un jugement sur la granularité de la liste, et le fichier
du mécanisme est hors périmètre.

---

# Écarts qui obligent à corriger un document normatif

Je n'ai modifié ni `docs/PRD.md`, ni `docs/decisions.md`, ni `gauntlet-log.md`.

1. **`docs/PRD.md:11` et `:346` et `:1083` — l'édition normative.** Le PRD désigne
   la *« deuxième édition, revue et augmentée, 13 août 2026 »* et pose que les
   pages citées sont les siennes. Le seul traité présent dans le dépôt est la
   **troisième**, 15 août 2026 (`Traité.md:6`, `date:`), et son PDF fait 143 pages.
   La clause d'édition de F2 doit passer à la troisième, faute de quoi la règle
   renvoie à un document que le dépôt ne contient pas.

2. **`CLAUDE.md` — « troisième édition […] 116 pages ».** Mesuré : 143 pages
   (`pymupdf`, `page_count`), numérotation imprimée de 2 à 143. Le PDF a été
   régénéré après la rédaction de `CLAUDE.md` (`Traité.pdf` du 15 août 17 h 36,
   `CLAUDE.md` du 15 août 12 h 44). Le nombre de pages est à reprendre.

3. **`CLAUDE.md` — « Quatre des quinze oracles du catalogue ne sont donc armés par
   aucune exécution ».** Mesuré : **six** — `CONSERVATION`, `ACCORD_LOCAL`, `D1`,
   `D2`, `UN_SEUL_PROPRIETAIRE`, `TOUTE_PARTITION_A_UN_PROPRIETAIRE`. C'est déjà ce
   que `sim_agents::hors_perimetre()` déclarait ; les deux documents divergent.

---

# Renvois de page hors périmètre, mesurés au passage

Ceux-ci tombent hors de la section qu'ils citent, dans le traité livré. Ils ne
sont pas dans mes fichiers ; les valeurs sont fournies pour la reprise.

| fichier:ligne | cite | la page citée est dans |
|---|---|---|
| `sim-milieu/src/replication.rs:7` | §2.1, p. 22 | §1.3 (§2.1 commence p. 23) |
| `sim-milieu/src/replication.rs:181` | §2.1, p. 21 | §1.3 |
| `sim-milieu/src/journal.rs:682-685` | §1.2, p. 13 | §1.2, mais M1-M4 sont énoncés p. 14 |
| `sim-milieu/src/journal.rs:82` | §6.2, p. 71 | §4.3 (§6.2 = p. 91-95) |
| `sim-milieu/src/controle.rs:4` | §4.2, p. 49 | §3.2 (§4.2 = p. 61-66) |
| `sim-core/src/faute.rs:4` | §3.3, p. 41 | §3.1 (§3.3 = p. 50-55) |
| `sim-agents/src/usl.rs:3` | conclusion, p. 130 | Références (conclusion = p. 128-129) |

Et les cinq blocs E, F, G, J, L (`adhesion.rs:24`, `allocation.rs:22`,
`agregat_fenetre.rs:27`, `cascade.rs:25`, `taux_de_base.rs:20`) : pages
**correctes**, édition **non nommée**.

---

# Rejouer

```powershell
$env:PATH = "$env:USERPROFILE\.cargo\bin;$env:LOCALAPPDATA\Microsoft\WinGet\Packages\BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe\mingw64\bin;$env:PATH"
cargo clippy -p sim-agents --all-targets --release
cargo test   -p sim-agents --release
cargo doc    -p sim-agents --no-deps
```

Les pages du traité se remesurent ainsi :

```python
import pymupdf, re
d = pymupdf.open("Traité.pdf")
pages = [re.sub(r"\s+", " ", p.get_text()) for p in d]
def page_de(citation):
    c = re.sub(r"\s+", " ", citation)
    return [i + 1 for i, t in enumerate(pages) if c in t]
print(d.page_count, d.get_toc())
print(page_de("elle le déplace dans le milieu"))   # → [25]
```

---

# Tour 2 — les cinq entrées de `M4-critique.md`

Cinq entrées portées par le jugement : **F0** (provenance sous-déclarée) et **F1**
à **F4**. Toutes les cinq sont des anomalies ; aucune n'est écartée. Chacune est
reproduite sur le code trouvé, puis corrigée, puis établie par contre-épreuve sur
le code livré — mécanisme cassé, test qui tombe, sortie citée, restauration
vérifiée.

```
$env:CARGO_TARGET_DIR = "C:\Users\agbru\AppData\Local\Temp\cargo-t2-m4"
cargo clippy -p sim-agents --all-targets --release  → Finished, 0 diagnostic
cargo test   -p sim-agents --release                → 296 tests, 296 ok, 0 échec
cargo doc    -p sim-agents --no-deps                → Finished, 0 lien cassé
```

Le compte détaillé : 253 (lib) + 4 + 11 + 5 + 4 + 5 + 3 + 11 (intégration). Un
test ajouté ici, un renommé, **aucun retiré, aucun relâché** ; l'écart de 290 à
296 comprend les tests d'un chantier parallèle sur les modules de mécanismes, qui
tourne dans la même crate.

---

## F0 — `scenario_m.rs:49` : l'aveu sous-déclarait l'épissure

**Reproduction.** Mesuré dans le traité livré — `pymupdf` sur `Traité.pdf`,
143 pages, et recherche verbatim page par page :

```python
q('rend du même geste bon marché ce que le concepteur ne veut pas')  → [5]
q('la conformité, puisque tous lisent la même trace')                → [127]
```

La p. 127 (§8.3) écrit : « La première édition soutenait que le milieu rend la
coordination bon marché ; **la mesure ajoute qu'il rend tout aussi bon marché** ce
que le concepteur ne veut pas — la conformité… ». La proposition principale du
champ `these` — « un milieu qui rend la coordination bon marché rend **du même
geste** bon marché ce que le concepteur ne veut pas » — est celle de
l'**introduction, p. 5**, mot pour mot, et non une incise. L'ancien aveu,
« l'incise « du même geste » est reprise de la p. 5 », déclarait un mot là où
c'est toute la proposition principale.

**Changé.** `scenario_m.rs:49` déclare les deux provenances, chacune avec ce
qu'elle porte, et dit comment le §8.3 écrit la proposition ; l'en-tête de module
(`scenario_m.rs:9-15`) porte le même aveu sous le bloc cité, qui ne s'attribue
plus à une page unique.

**Preuve que c'est parti.** L'aveu du tour 1 remis en place, le test de F1 tombe
sur le fragment qui vient de l'introduction :

```
thread 'scenario::tests::la_these_de_chaque_bloc_verifie_est_a_la_page_citee'
panicked at crates\sim-agents\src\scenario.rs:718:17:
bloc M : « un milieu qui rend la coordination bon marché rend du même » est dans
l'introduction du traité, que `source` ne nomme pas — §8.3, p. 127 (3ᵉ éd.) ;
l'incise « du même geste » est reprise de la p. 5
```

L'épissure n'est donc plus déclarée par une phrase, elle est **vérifiée**.

---

## F1 — `scenario.rs` : le test contre les provenances fausses se comparait à lui-même

**Reproduction.** Sur le code trouvé, `BLOC_A.source` passé de « p. 25 » à
« p. 21 » — une page fausse portant la bonne mention d'édition :

```
running 1 test
test scenario::tests::les_blocs_verifies_nomment_leur_edition ... ok
```

Le test existait contre exactement ce cas et ne le voyait pas. `BLOCS_VERIFIES` et
la boucle itéraient sur les mêmes cinq littéraux ; la seule clause qui pouvait
échouer était `contains("3ᵉ éd.")`.

**Changé.** `BLOCS_VERIFIES` est **supprimé** — une liste comparée à elle-même
n'établit rien —, remplacé par `blocs_verifies()` (`scenario.rs:492`), la seule
liste des cinq blocs. `les_blocs_verifies_nomment_leur_edition`
(`scenario.rs:639`) ne garde que la clause de forme et dit dans sa doc qu'elle ne
vaut que par le test suivant. Le test qui manquait est
`la_these_de_chaque_bloc_verifie_est_a_la_page_citee` (`scenario.rs:681`), et il
interroge le traité :

1. la thèse est **retrouvée mot pour mot** dans `Traité.md`, en un ou plusieurs
   morceaux contigus (casse et ponctuation finale exceptées) ;
2. **chaque** morceau tombe sous une section que `source` nomme — c'est le défaut
   mesuré au tour 1 sur A, D, K et M, dont la page citée tombait hors de la
   section citée ;
3. chaque page citée à côté d'un marqueur de section tombe dans l'intervalle
   mesuré de cette section (`PAGES_DES_SECTIONS`, `scenario.rs:477`, relevé par
   `pymupdf.open("Traité.pdf").get_toc()`).

**Pourquoi `Traité.md` et non un dépouillement du PDF.** Le juge laissait le choix
et demandait le motif. `Traité.md` est la **source** Pandoc/Typst dont le PDF est
le rendu : vérifier contre elle, c'est vérifier contre l'original. Un
dépouillement page à page du PDF donnerait la page exacte, mais au prix d'une
seconde copie du traité dans le dépôt, dérivée, que rien n'oblige à régénérer et
qui peut diverger de la première sans le dire — la panne même dont ce lot de
constats est fait. La table des matières mesurée donne le compromis : elle
rattache une page à sa section sans recopier le texte.

**Ce qui reste hors de portée, et c'est dit dans la doc du test.** `Traité.md` ne
porte aucune pagination — elle naît du rendu. Une page fausse **à l'intérieur** de
la bonne section passe encore : c'était le cas du bloc B au tour 1, qui citait la
p. 13 pour une thèse qui est p. 16, l'une et l'autre dans le §1.2. L'intervalle de
section ramène la latitude de 143 pages à cinq ou six ; le reste est tenu par la
relecture.

**Contre-épreuves — trois, une par clause.**

Page fausse dans une section nommée correctement (`BLOC_A` : p. 25 → p. 21) :

```
panicked at crates\sim-agents\src\scenario.rs:747:17:
bloc A : 2.1 occupe les pages 23 à 30 du traité livré, et le bloc cite la p. 21
— §2.1, p. 21 (3ᵉ éd.) — comptes comparés : tableau 3, p. 18, et figure 0, p. 4
```

Section fausse avec une page qui y résout (`BLOC_A` : §2.1 p. 25 → §1.2 p. 16) —
le cas que l'intervalle de pages, seul, laisserait passer :

```
panicked at crates\sim-agents\src\scenario.rs:718:17:
bloc A : « elle ne détruit pas le point partagé, elle le déplace dan » est dans
§2.1 du traité, que `source` ne nomme pas — §1.2, p. 16 (3ᵉ éd.) — comptes
comparés : tableau 3, p. 18, et figure 0, p. 4
```

Épissure sous-déclarée (`BLOC_M`, aveu du tour 1) : la sortie est citée en F0.

Restauration vérifiée par `git diff` : aucune des trois falsifications ne subsiste.

---

## F2 — `tests/sortie_phase_6.rs:148` : le repli « réfutable » était vide

**Reproduction.** `scenario_m.rs` — la mesure remplacée par la constante `0.0` :

```
running 1 test
test aucun_oracle_de_surete_ne_tombe_pendant_leffacement ... ok
```

`assert!(r.hors_dominante.0.is_finite())` ne dit rien d'autre que « ce n'est ni
NaN ni l'infini ». Il n'était pas *entièrement* creux — `hors_dominante_observee`
est initialisé à `f64::INFINITY` et n'est un minimum courant que si
`verifier_bornes` s'exécute —, mais toute constante finie le satisfait, et c'est
la substitution qu'un défaut réel produirait.

**Une assertion réfutable est possible à cet endroit, et il y en a deux.** Le
point du critère annonce que « la mesure survit à l'effacement de la borne ».
Mesuré, à m = 6 ressources, trois graines par valeur du curseur :

| part | graine 3 | graine 11 | graine 47 |
|---|---|---|---|
| 0 | 0,332517 | 0,345230 | 0,288217 |
| 0,5 | 0,440145 | 0,298514 | 0,295159 |
| 1 | 0,314852 | 0,107437 | 0,264941 |

De quoi tirer deux clauses, et **la mesure en a écarté une troisième** : la
grandeur n'est **pas** monotone en la part — à graine 3 elle *monte* de 0,3325 à
0,4401 entre part 0 et part 0,5. Une assertion de monotonie aurait été fausse.

**Changé.** `tests/sortie_phase_6.rs:148` remplace le repli par :

1. la grandeur est une **fraction d'effort** — strictement positive et au plus
   1 − 1/m, puisqu'elle est un minimum de 1 − p_max sur m ressources
   (`sortie_phase_6.rs:162`) ;
2. elle **dépend de l'exécution** — à part fixée, trois graines rendent trois
   valeurs distinctes (`sortie_phase_6.rs:187`). **Toute** substitution par une
   constante tombe sur cette clause, quelle que soit la constante.

La même assertion creuse existait au point voisin,
`les_sept_bornes_seffacent_…` (`sortie_phase_6.rs:110`) : même correctif,
clause 1. La doc du test porte les chiffres mesurés et dit pourquoi la monotonie
n'y est pas.

**Contre-épreuves — une par clause, plus la voisine.**

Mesure remplacée par `0.0` :

```
panicked at crates\sim-agents\tests\sortie_phase_6.rs:162:13:
part = 0, graine = 3 : fraction hors dominante 0, hors de ]0 ; 0.8333333333333334]
— ce n'est pas une fraction d'effort mesurée
```

Mesure remplacée par la constante **plausible** `0.3`, que la clause 1 laisse
passer :

```
panicked at crates\sim-agents\tests\sortie_phase_6.rs:187:17:
part = 0 : les graines 3 et 11 rendent la même fraction hors dominante 0.3
— la mesure ne dépend plus de l'exécution
```

Le point voisin, sous `0.0` :

```
panicked at crates\sim-agents\tests\sortie_phase_6.rs:110:5:
fraction hors dominante 0 : ce n'est pas une fraction d'effort mesurée
```

Le critère de sortie est **renforcé** : deux points du §9 qui passaient sous une
mesure détruite tombent maintenant. Rien n'y est retiré ni affaibli — la clause
`violations_de_surete == 0` et l'aveu du tour 1 sur ce qu'elle tient par
construction au-delà de `part = 0` sont conservés mot pour mot.

---

## F3 — `gouvernance.rs:497` : `TOUTES.len() == 4` sur `[Criticite; 4]`

**Reproduction.** L'assertion est une vérité de compilation ; un doublon la
satisfait. `TOUTES` avec `CriticalPlus` deux fois :

```
running 1 test
test gouvernance::tests::ex_a30_chaque_levier_dit_ce_quil_ne_borne_pas ... ok
```

**Changé.** Ce que la taxonomie promet — quatre classes, chacune une fois, de la
plus haute à la plus délestable — est asserté sur les **noms de la source** :

```rust
assert_eq!(
    Criticite::TOUTES.map(Criticite::nom),
    ["CRITICAL_PLUS", "CRITICAL", "SHEDDABLE_PLUS", "SHEDDABLE"]
);
```

Un doublon, un oubli ou une inversion tombe ici. L'ancienne
`assert_eq!(Criticite::CriticalPlus.nom(), "CRITICAL_PLUS")` est subsumée et
retirée : elle est le premier élément du tableau.

**Contre-épreuve.** Le même doublon :

```
assertion `left == right` failed
  left: ["CRITICAL_PLUS", "CRITICAL_PLUS", "SHEDDABLE_PLUS", "SHEDDABLE"]
 right: ["CRITICAL_PLUS", "CRITICAL", "SHEDDABLE_PLUS", "SHEDDABLE"]
```

---

## F4 — `essaim.rs:116` : la branche `Voisinage` d'`intervalle_max` n'avait pas de test

**Reproduction.** Le seul appel de la méthode, en production comme en test, passe
par l'autre branche :

```
$ grep -rn "intervalle_max" crates/
crates/sim-agents/src/essaim.rs:96      (définition)
crates/sim-agents/src/essaim.rs:146     (test — branche IntervalleMilieu)
crates/sim-agents/src/stigmergie.rs:736 (production — branche IntervalleMilieu)
```

La doc corrigée au tour 1 promet une unité par branche — des enregistrements d'un
côté, des voisins de l'autre — et une seule était exercée.

**Changé.** `un_voisinage_borne_est_un_membre` devient
`un_voisinage_borne_est_un_membre_et_sa_borne_se_compte_en_voisins`
(`essaim.rs:116`) : le membre est construit sur `Perception::Voisinage`, et
`intervalle_max()` est lu. Le test qui ne vérifiait que `is_ok()` vérifie
maintenant ce que la doc promet.

**Contre-épreuve.** Branche `Voisinage` rendant `0` :

```
 right: 8
failures:
    essaim::tests::un_voisinage_borne_est_un_membre_et_sa_borne_se_compte_en_voisins
```

**Ce que ce test ne peut pas faire, et il faut le dire.** Un accesseur rend son
champ ; l'assertion porte sur une valeur posée quelques lignes plus haut, et c'est
irréductible. Ce qu'elle attrape est le seul défaut possible ici : la branche qui
cesse de rendre son cardinal.

---

# Écarts qui obligent à corriger un document normatif — tour 2

Je n'ai modifié ni `docs/PRD.md`, ni `docs/decisions.md`. Un écart s'ajoute aux
trois du tour 1.

4. **`docs/PRD.md:1539` — l'épissure de F0 vient du PRD, pas du produit.** Le §9
   cite la thèse du scénario M sous la seule mention « (§8.3, p. 94) », et c'est
   la même phrase épissée : sa proposition principale est de l'introduction p. 5,
   son énumération du §8.3 p. 127. Deux défauts en un — une provenance pour deux,
   et une page qui n'est celle d'aucune des deux dans le traité livré.
   `docs/PRD.md:401` porte la même citation avec la même page. `BLOC_M` déclare
   désormais les deux provenances ; le PRD ne les déclare pas, et c'est lui qu'un
   relecteur lit d'abord.

---

# Reprise des `fichier:ligne` du tour 1

Le juge a relevé que les numéros de ligne des cinq rapports désignent l'état
trouvé. Voici, mesurés sur le code livré, ceux qui ont bougé ; les autres —
`partage.rs:33`, `scenario.rs:58`, `:187`, `:218`, `scenario_d.rs:25`, `:392`,
`gouvernance.rs:23`, `:332`, `glossaire.rs:226`, `conformite.rs:105`, `:261`,
`lib.rs:79`, `:114`, `dettes.rs:186`, `tests/sortie_phase_2.rs:130`,
`sortie_phase_6.rs:103`, `bin/campagne.rs:156-158` — sont inchangés.

| tour 1 | code livré | ce que la ligne désigne |
|---|---|---|
| `scenario.rs:146` | `scenario.rs:144` | `Comparaison::diametres()` |
| `scenario.rs:547` | `scenario.rs:760` | `chaque_scenario_porte_son_bloc_de_trois` (constat C) |
| `scenario_m.rs:41` | `scenario_m.rs:49` | le champ `source` de `BLOC_M` |
| `scenario_m.rs:241` | `scenario_m.rs:275` | l'assertion des sept effacements |
| `gouvernance.rs:349` | `gouvernance.rs:349-358` | la propriété réfutable qui a remplacé `110 > 55` |
| `lib.rs:124` | `lib.rs:122` | l'entrée PD10 de `hors_perimetre()` |
| `sortie_phase_6.rs:125` | `sortie_phase_6.rs:148` | `aucun_oracle_de_surete_ne_tombe_pendant_leffacement` (constat B) |
| `sortie_phase_6.rs:148` | `sortie_phase_6.rs:177` | le second des sept effacements (constat A) |

**Hors périmètre, mesurés le 17 août et volatils.** Un chantier parallèle édite
les modules de mécanismes pendant que ceci s'écrit ; ces lignes bougent encore.

| tour 1 | mesuré le 17 août |
|---|---|
| `stigmergie.rs:639-640` | `stigmergie.rs:688-689` |
| `stigmergie.rs:687` | `stigmergie.rs:736` |
| `stigmergie.rs:351` | `stigmergie.rs:359` |
| `stigmergie.rs:883-886` | `stigmergie.rs:929` |
| `elasticite.rs:207` | `elasticite.rs:178` |
| `sim-viz/src/scenario_b.rs:61` / `:67` | `:68` / `:74` |
| `sim-viz/src/scenario_a.rs:124` / `:439-440` | `:131` / `:446` |
| `sim-milieu/src/journal.rs:682-685` | `journal.rs:696-697` |

Inchangés hors périmètre : `cascade.rs:152`, `allocation.rs:235`,
`consensus_lineaire.rs:70`, `replication.rs:7`, `:181`, `journal.rs:82`,
`controle.rs:4`, `faute.rs:4`, `usl.rs:3`.

---

# Rejouer le tour 2

```powershell
$env:PATH = "$env:USERPROFILE\.cargo\bin;$env:LOCALAPPDATA\Microsoft\WinGet\Packages\BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe\mingw64\bin;$env:PATH"
$env:CARGO_TARGET_DIR = "C:\Users\agbru\AppData\Local\Temp\cargo-t2-m4"
cargo clippy -p sim-agents --all-targets --release
cargo test   -p sim-agents --release
cargo doc    -p sim-agents --no-deps
```

Les intervalles de `PAGES_DES_SECTIONS` se remesurent ainsi :

```python
import pymupdf
d = pymupdf.open("Traité.pdf")
print(d.page_count, [(t, p) for _, t, p in d.get_toc()])
```
