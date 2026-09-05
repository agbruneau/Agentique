# Audit du code Rust de `3 - Traité` — optimisation et refactorisation, et plan d'exécution

*Audit conduit le 4 septembre 2026 sur l'arbre de travail (branche `main`, commit `a7df123`). Périmètre : le code Rust du simulateur `stigmergie-lab` — quatre crates (`sim-core`, `sim-milieu`, `sim-agents`, `sim-viz`), deux bancs (`dt1-flottant`, `parite-wasm`), un binaire (`campagne`), quatre exemples, sept fichiers de tests d'intégration — soit **78 fichiers `.rs` et 29 690 lignes** (`find crates bancs -name '*.rs' | xargs wc -l`). Chaque fichier a été lu en entier. Les documents (`docs/`, `VERDICT.md`, `README.md`, `CLAUDE.md`) ont été lus pour ce qu'ils contraignent, non audités pour eux-mêmes : c'était l'objet de l'audit du 2 septembre.*

---

## 1. Résumé

**Le code tient ce qu'il déclare, et la mesure de départ est verte sur toute la ligne.** Rien dans ce plan ne corrige un défaut de comportement ; tout y est vitesse, allocation, code mort, duplication ou couplage déjà nommé au registre des décisions.

| Ce que le dossier déclare | Ce que la mesure rend le 4 septembre 2026 | Verdict |
|---|---|---|
| 467 tests, 0 échec — 254 / 96 / 68 / 6 unitaires, 43 d'intégration | `cargo test --workspace --release` : **467 passés, 0 échec**, ventilation identique, 12 s | ☑ |
| `clippy` 0, `cargo doc` 0 | sorties **0** et **0** (7,9 s et 7,1 s) | ☑ |
| NF-05 : 15,2 puis 13,2 s simulées/s-cœur à n = 1 000 (verdict de phase 5) | banc `nf05` : **12,9 puis 11,9** — même ordre, colonnes reproductibles (`s simulées` 5,13 / 25,65 ; `retard max` 71 546 / 356 061) identiques | ☑ |
| — *(rien n'est déclaré)* | `cargo fmt --all --check` : **60 fichiers, 225 différences** de mise en forme | ⚠ voir T-01 |

Ce que l'audit trouve est de quatre ordres :

1. **Le chemin chaud du scénario B paie chaque cycle des allocations et des copies qu'il n'a pas besoin de faire** (P-01 à P-07). Deux copies intégrales de l'intervalle lu (jusqu'à 256 × 64 octets), quatre `Vec` alloués puis libérés, deux `libm::log` et deux `libm::pow` recalculés sur des paramètres figés. Le gain attendu est un **facteur constant — de l'ordre de 20 à 35 % du temps par cycle, à confirmer au profil** —, et **il ne changera pas le verdict NF-05**, dont l'écart est structurel (Θ(n²), un facteur 80). Tout ce que la phase 2 touche se fait **bit pour bit identique** : mêmes tirages, mêmes flottants, mêmes traces.
2. **L'écran du scénario A recalcule quarante-neuf exécutions par image**, y compris quand aucun curseur n'a bougé (V-01) — c'est le seul poste qui pèse sur NF-07 (30 images/s en WASM), et un cache sur les entrées suffit.
3. **Du code mort ponctuel et quatre paramètres fantômes** (D-01 à D-08), dont un mode de défaillance du scénario H que **rien ne peut produire** : la branche « époque » de `PushPull` est inatteignable, parce que les époques ne divergent jamais (D-05).
4. **Des refactorisations que le registre des décisions nomme déjà comme « le correctif de fond »** — vainqueur en temps lu dans une chaîne, provenance des bornes recopiée, sept paramètres positionnels du scénario A — et qui n'attendent qu'un arbitrage (R-01 à R-05), plus trois duplications à résorber sans arbitrage (R-06 à R-08).

Et une incohérence documentaire que le code révèle : **le verdict NF-05 attribue à la rétention un gain qu'elle ne peut pas produire**, `Milieu::appliquer_retention` n'ayant aucun appelant hors test (T-03).

**Le plan est en cinq phases**, dont trois bit-identiques (0 à 2), une qui touche l'interface et impose le réempaquetage (3), une de refactorisations d'API (4), et une de documents (5). Aucune ne touche `Traité.md`, aucune n'affaiblit un critère de sortie de phase. **Les six décisions qu'il ouvrait sont analysées et tranchées au §4.8** — `rustfmt` appliqué, les trois paramètres fantômes retirés, le mode « époque » déclaré non provocable, `Option<f64>` adopté, les trois `completude` factorisées, la phase facultative retirée. Ce sont des choix proposés : ils tiennent tant que l'auteur ne les infirme pas avant la phase 0.

---

## 2. Méthode

- **Lecture intégrale** des 78 fichiers, avec la ligne de chaque constat.
- **Rejeu de l'appareil** avec `CARGO_TARGET_DIR` hors de OneDrive et le `PATH` de `DEVELOPPEMENT.md` : `cargo test`, `cargo clippy`, `cargo doc`, `cargo fmt --check`, `banc_nf05`. Les sorties sont dans le tableau du §1.
- **Micro-banc `libm`** sur la machine de mesure (cible `x86_64-pc-windows-gnu`, `opt-level = 3`, 25,6 M d'appels) : `exp` **4,0 ns**, `log` **3,4 ns**, `pow` **20,5 ns**, `pow(2, −r)` **19,2 ns**. Vérifié au passage : `libm::pow(2.0, −r)` et `f64::from_bits((1023 − r) << 52)` rendent les **mêmes bits** pour `0 ≤ r < 32` — ce qui autorise O-04.
- **Recherche des appelants** par `grep` pour chaque item soupçonné mort ou sans consommateur ; ce qui est cité comme « sans appelant » l'est au sens *aucune occurrence hors de son module et de ses tests*.
- **Non fait, et c'est déclaré** : aucun profil échantillonné — la ventilation du temps par cycle du §3.1 est une **estimation** tirée du micro-banc et du compte d'opérations, et la phase 0 la remplace par une mesure. Les bancs WASM (`dt1`, `parite-wasm`) ne sont pas rejoués ; leurs verdicts sont lus.

---

## 3. Constats

Sévérité : **M** majeur (un coût mesurable, ou une règle du dossier violée) · **m** mineur · **info**. Chaque constat porte un marqueur de préservation : **[B]** le correctif est **bit-identique** (mêmes tirages, mêmes flottants, mêmes traces et empreintes) ; **[Δ]** il peut changer des bits ; **[API]** il change une signature publique.

### 3.1 Le chemin chaud du scénario B

Le budget mesuré : 200 000 événements en 0,40 s à n = 1 000, soit **2 µs par événement**, c'est-à-dire ≈ 4 µs pour la paire *cycle d'agent + accusé de durabilité*. Ventilation **estimée** d'un cycle qui lit ses 256 enregistrements : ≈ 1,0 µs de `libm::exp` (256 × 4 ns, incompressible sans changer les bits), ≈ 1 µs de copies mémoire (deux fois 16 ko — `size_of::<Enregistrement>()` vaut 64), ≈ 2 µs de file, de tirages, de mémo de familles, d'allocations et de boucle sur φ. **Aucun de ces postes n'est le Θ(n²)** : celui-ci est le nombre de cycles par unité de temps simulé, et il ne se déplace pas.

| # | Sév. | Constat | Où |
|---|---|---|---|
| P-01 | M **[B][API]** | **L'intervalle lu est copié deux fois par cycle.** `Milieu::lire` rend un `Vec<Enregistrement>` cloné du journal, `lire_multi` le recopie dans `sortie`, et `actualiser_phi` ne fait qu'itérer dessus. Un enregistrement fait 64 octets ; à 256 par cycle c'est 32 ko de `memcpy` et deux allocations pour rien. Le correctif est une fonction qui rend des **plages** — `Vec<(u32, Range<usize>)>`, une par partition dans l'ordre mélangé — et un appelant qui itère les tranches du journal en place ; `lire` et `lire_multi` deviennent des enveloppes de cette fonction, pour que les tests et l'API existants tiennent. Même ordre de lecture, mêmes tirages de Fisher-Yates, mêmes compteurs. | `crates/sim-milieu/src/journal.rs:501-514`, `:540-563` ; `crates/sim-agents/src/stigmergie.rs:741-750`, `:851-891` |
| P-02 | M **[B]** | **`Params::bornes_applicables()` est recalculée à chaque cycle**, dans `verifier_bornes` : deux `libm::pow` (≈ 40 ns) et, dès que la borne est effacée — préréglage « verrouillage », toute part de conformité non nulle —, **un `format!` d'une phrase de 300 caractères par cycle**, jeté aussitôt. Les paramètres sont figés à la construction : calculer une fois dans `Fourragement::nouveau` et garder le `Result<Bornes, String>`. | `crates/sim-agents/src/stigmergie.rs:917-944` |
| P-03 | m **[B]** | **`Params::depot()` — un `libm::log` — est recalculé à chaque dépôt** ; même motif, même correctif : une valeur calculée une fois à la construction. | `crates/sim-agents/src/stigmergie.rs:1045-1046`, `:255-271` |
| P-04 | m **[B]** | **`Granularite::tics_depuis_ms` — avec ses deux `assert!` et un `ceil` — est rappelée à chaque cycle** pour la période, pour τ, et à chaque action pour la fenêtre ℓ₉₉ (`periode()`, `actualiser_phi`, `agir`, `compter_incomparabilite`) ; `actualiser_phi` refait aussi `ln γ` (un `libm::log`) à chaque cycle, et `compter_incomparabilite` un `libm::pow` pour son seuil. Six constantes de l'exécution, à calculer une fois. | `crates/sim-agents/src/stigmergie.rs:710-712`, `:852-860`, `:993-999`, `:1019` |
| P-05 | m **[B]** | **Trois `Vec` de travail alloués et libérés à chaque cycle** — `curseurs` (p entrées), `poids` (m entrées) — et, dans `compter_incomparabilite` en multipartition, `classes` trié en entier pour n'en lire que deux. Deux tampons réutilisés dans `Fourragement` suffisent aux deux premiers ; le troisième se remplace par une recherche des deux plus grands **avec le même départage** que le tri stable descendant (plus petit indice à poids égal), ou se laisse tel quel — il ne tourne qu'en mode « incomparabilité M2 ». | `crates/sim-agents/src/stigmergie.rs:742-747`, `:899-911`, `:981-989` |
| P-06 | m **[B]** | **`agir` recalcule le maximum des utilités à chaque action** (`fold` sur m ressources) pour `utilite_optimale` ; ce maximum ne change qu'à la bascule. Le tenir à jour dans `appliquer_bascule`. | `crates/sim-agents/src/stigmergie.rs:1035-1039`, `:1103-1118` |
| P-07 | m **[B]** | **`durabilite` clone `curseurs` à chaque accusé** (`curseurs_valides = curseurs.clone()`, et l'inverse au rejeu) : une allocation par événement de durabilité, soit la moitié des événements. `clone_from` réutilise le tampon ; les deux vecteurs ont toujours la même longueur p. | `crates/sim-agents/src/stigmergie.rs:1088`, `:1093` |
| P-08 | info | **`libm::exp` n'est pas le goulot**, contrairement à ce que sa position dans la boucle laisse croire : 4 ns par appel, 256 appels par cycle, ≈ 1 µs sur 4. Les formes qui l'éviteraient — factorisation incrémentale de `exp(k·Δt)`, table — changent les bits et sont écartées (NF-02, EX-V12). Il n'y a **pas d'optimisation bit-identique de ce poste**. | `crates/sim-agents/src/stigmergie.rs:861-885` |
| P-09 | info | **NF-05 reste hors d'atteinte quelle que soit la phase 2**, et le plan ne promet pas le contraire. À n = 1 000 et T = 50 ms, une seconde simulée vaut 20 000 cycles ; la cible de 10³ s simulées/s-cœur exige 50 ns par cycle, contre ≈ 4 µs mesurés. Un facteur 80, dont ce plan reprend au mieux un tiers. Le verdict du banc le dit déjà ; l'audit le confirme par la mesure et par le micro-banc. | `bancs/nf05-debit/VERDICT.md` |

### 3.2 L'interface

| # | Sév. | Constat | Où |
|---|---|---|---|
| V-01 | M **[B]** | **Le scénario A exécute cinquante `scenario_a` par image** — une pour le bandeau et les quatre actes, quarante-neuf pour la courbe du croisement — **sans regarder si une entrée a changé**. Chaque appel fait une `diffuser` (n tirages de Bernoulli) et une `entretenir_vue` (n sondes du `Detecteur`, n tirages exponentiels, n conversions en tics) : à n = 2 000, de l'ordre de 10 ms par image en natif — estimé du micro-banc, non profilé —, davantage en WASM, pendant tout glissement de curseur. Or les cinquante résultats sont des fonctions pures de six entrées et d'une graine figée. Un cache — clé = les six entrées, valeur = la `Comparaison`, les deux courbes et l'abscisse de bascule — recalculé **au changement d'entrée seulement** rend le même écran et laisse l'image au repos à zéro calcul. Le texte « il se recalcule à chaque image » (`comment_cet_ecran_sexecute`) et le libellé du temps mural (« celui de ce seul recalcul ») sont à reformuler : *à chaque changement de réglage*. La vue continue de **lire** la simulation et de ne rien trancher (§5.1 du PRD). | `crates/sim-viz/src/scenario_a.rs:125-144`, `:343-370`, `:684-706` |
| V-02 | m **[B]** | **Le §5 du scénario B refait, par image, six préréglages et douze `differences`** — soit 6 constructeurs `Params` et 156 `format!` de chaînes qui ne dépendent d'aucun état de la vue. Négligeable en temps (≈ 20 µs), mais c'est du travail par image pour une table constante : à calculer une fois dans `VueB::default`. À faire seulement si `scenario_b.rs` est touché par ailleurs. | `crates/sim-viz/src/scenario_b.rs:794-822`, `:977-984` |
| V-03 | info | L'onglet « Repères » minuscule chaque terme et chaque définition à chaque image pour filtrer (≈ 70 allocations par image). Sans effet perceptible ; laissé tel quel. | `crates/sim-viz/src/lib.rs:762-770` |

### 3.3 Code mort et paramètres fantômes

| # | Sév. | Constat | Où |
|---|---|---|---|
| D-01 | m **[B]** | **`Vue::derniere_sonde` est écrit à chaque sonde et jamais lu** : le champ, son écriture, et l'`Instant` passé pour lui à `sonder` ne servent à rien. Le paramètre `maintenant` de `Detecteur::sonder` n'a alors plus d'usage — le retirer touche onze appels dans trois fichiers, dont un seul en production (`pair_a_pair`) ; le garder documenté est le moindre diff. | `crates/sim-core/src/detecteur.rs:111`, `:276` |
| D-02 | m **[B]** | **`Iteration::dernier_ecart` n'est lu que pour se mettre à jour** : un minimum tenu que rien ne consulte. | `crates/sim-agents/src/consensus_lineaire.rs:117`, `:134`, `:173-176` |
| D-03 | m **[B][API]** | **`Partition::durables()` n'a aucun appelant**, pas même un test. | `crates/sim-milieu/src/journal.rs:282-285` |
| D-04 | m **[API]** | **Trois paramètres fantômes** : `Cascade::pas(&mut self, _alea)` ne tire rien ; `allocation::tableau_15(…, alea)` fait `let _ = alea` — et `hors_perimetre()` le déclare (« la graine est ignorée ») ; `Reconfiguration::ecrire(…, auteur, …)` fait `let _ = auteur`. Un paramètre reçu et ignoré est une promesse d'affordance que le code ne tient pas. Le quatrième, `scenario_a(…, p, …)`, est **délibéré et déclaré** (curseur muet de l'écran, entrée de `hors_perimetre()`) et n'est pas touché. Tranché au §4.8. | `crates/sim-agents/src/cascade.rs:209` ; `allocation.rs:234-235` ; `soupcon.rs:530-568` ; `scenario.rs:166-187` |
| D-05 | M *(décision)* | **La branche « époque » de `PushPull::cycle` est inatteignable.** Les époques ne bougent qu'en deux endroits : la relance, qui incrémente **toutes** les entrées d'un bloc, et la branche elle-même, qui aligne le retardataire sur l'avancé. Aucun chemin — ni crash, ni partition, ni omission — ne fait diverger deux époques, donc `Ligne::Epoque` n'est jamais produite, alors que le module l'annonce comme un mode de défaillance (« lignes 5 contre 6 — deux traitements opposés du même désaccord »), et que NF-10 veut chaque mode nommé **provocable**. Ce n'est pas un défaut de vitesse : c'est un mode déclaré que rien ne peut montrer. Deux issues, toutes deux des décisions de produit : donner un chemin de divergence (une relance qui se propage par bavardage au lieu d'être globale), ou déclarer le mode non provocable dans `hors_perimetre()`. Tranché au §4.8. | `crates/sim-agents/src/agregation.rs:246-248`, `:282-301` |
| D-06 | m **[B]** | **Un test attrape une panique qui n'existe plus** : `le_detecteur_refuse_une_expiration_plus_longue_que_sa_periode` enveloppe dans `catch_unwind` un `expect` sur un `Result` — c'est la trace du temps où `Detecteur::nouveau` assertait. Le test vérifie bien un refus, mais par le mauvais chemin ; `assert!(….is_err())` dit ce qu'il vérifie. | `crates/sim-core/src/detecteur.rs:442-446` |
| D-07 | info | `Service`, `CoutAgent`, `Retention`, `verifier_horizon`, `compacter`, `appliquer_retention`, `Agregat`, `Generateur`, `composantes`, `fortement_connexe`, et six mécanismes de `sim-agents` n'ont **aucun appelant en production**. Ce n'est pas du code mort au sens de cet audit : chacun est déclaré comme tel par l'une des trois listes d'absences (PD6), et son retrait est une décision de périmètre, pas de nettoyage. Ils sont listés ici pour que le §3.5 dise ce que leur optimisation vaut : **rien**, sur un résultat affiché. | `sim_agents::hors_perimetre()`, `sim_milieu::hors_perimetre()`, `ModeleFaute::hors_modele()` |
| D-08 | m **[B]** | **`scenario_m` clone la partition entière pour l'estimer** (`.to_vec()`), là où `scenario_b`, deux lignes plus haut dans un autre fichier, passe la tranche telle quelle à `conformite::estimer`. | `crates/sim-agents/src/scenario_m.rs:149-150` ; `scenario.rs:434` |

### 3.4 Duplications et refactorisations

Les cinq premières sont **nommées par `docs/decisions.md` comme « le correctif de fond »** de choix pris dans la vue faute de mieux, ou comme décisions ouvertes. L'audit ne les rouvre pas ; il les chiffre.

| # | Sév. | Constat | Où |
|---|---|---|---|
| R-01 | M **[B][API]** | **Le vainqueur en temps du scénario A est lu par `contains("la maille gagne")`** dans une phrase française de `sim-agents`, et un test de `sim-viz` garde le couplage. Le registre demande `qui_gagne_en_temps() -> Vainqueur` dans `sim-agents`, dont `verdict_temps` compose sa phrase : une énumération à deux variantes, une méthode, et `VAINQUEUR_MAILLE` disparaît avec son test de garde. | `crates/sim-viz/src/scenario_a.rs:80-88`, `:365`, `:790-806` ; `crates/sim-agents/src/scenario.rs:128-140` ; `docs/decisions.md` (« Le vainqueur en temps est lu dans une chaîne ») |
| R-02 | M **[B][API]** | **La provenance des deux bornes est recopiée dans la vue** (`SOURCE_BORNES = "§1.2, p. 16, 4ᵉ éd."`), avec un test qui vérifie qu'elle reste contenue dans `Bornes::LEGENDE`. Une constante `Bornes::SOURCE` dans `sim-agents`, dont `LEGENDE` se sert, supprime la copie et son test. | `crates/sim-viz/src/scenario_b.rs:61-74`, `:1397-1403` ; `crates/sim-agents/src/stigmergie.rs:422-432` |
| R-03 | M **[B][API]** | **`scenario_a` est une fonction nue à sept paramètres positionnels**, sans défaut, et `VueA::default` transcrit six valeurs du §7 du PRD que rien ne tient en accord. Une structure `ParamsA` avec un `Default` portant les défauts du PRD, comme `Params::scenario_b()` le fait déjà pour B, ferme l'exception « zéro définition de scénario **à deux exceptions nommées** » de `sim-viz` pour A. Les trois valeurs de `VueB::default` (n = 16, budget, graine) restent : n = 16 est un choix de coût d'ouverture, pas un défaut de scénario. | `crates/sim-agents/src/scenario.rs:166-202` ; `crates/sim-viz/src/scenario_a.rs:103-121` ; `docs/decisions.md` (« Remonter dans `sim-agents` les neuf valeurs ») |
| R-04 | m **[API]** | **`Mesures::plancher_observe` et `hors_dominante_observee` portent `+∞` comme sentinelle**, et la vue la traduit (`jamais_vu`). Le registre nomme `Option<f64>` comme le bon correctif ; il change une signature publique et deux tests d'intégration qui comparent ces champs. Tranché au §4.8. | `crates/sim-agents/src/stigmergie.rs:502-505`, `:669-671` ; `crates/sim-viz/src/scenario_b.rs:1094-1110` |
| R-05 | info *(décision)* | **La dérivation 21–31 s existe en trois exemplaires** (`Detecteur::completude`, `DetecteurInfectieux::completude`, `cycle_de_vie::retirer`), alignés par le banc du 17 août et **délibérément non factorisés** : `SPEC.md` §8 le dit, PD7 est ouverte. Les trois portent la même saturation et le même refus du seuil nul, donc une seule fonction `sim_core::detecteur::encadrement_de_detection(periode, expiration, seuil) -> Result<(Duree, Duree), String>` les remplace à l'identique. Tranché au §4.8 : la règle du comptage de PD7 est satisfaite par trois exemplaires écrits dans le traité, la factorisation est due. | `crates/sim-core/src/detecteur.rs:224-233` ; `crates/sim-agents/src/soupcon.rs:209-228` ; `cycle_de_vie.rs:181-209` |
| R-06 | m **[B]** | **FNV-1a est écrit quatre fois** : `Config::hachage` (octets), `Trace::absorber` (u64 par octets), `bancs/parite-wasm` (idem) et `bancs/dt1-flottant` (bits d'un f64). Les deux de `sim-core` partagent déjà les constantes en commentaire ; une fonction `pub(crate) fn absorber_octets(h: &mut u64, octets: &[u8])` les sert toutes deux à l'identique — `(x >> 8i) & 0xff` **est** `x.to_le_bytes()[i]`. Les deux bancs restent autonomes : `dt1` ne doit dépendre de rien (c'est sa méthode), et `parite` mesure une empreinte, pas une bibliothèque. | `crates/sim-core/src/lib.rs:96-113` ; `moteur.rs:143-166` |
| R-07 | m **[B]** | **`Mesures::moyenne_et_queue` trie deux fois le même vecteur** (deux appels à `percentile`, chacun clonant et triant). Un tri, deux rangs. Sans appelant en production ; corrigé au passage si le fichier est ouvert. | `crates/sim-milieu/src/latence.rs:116-125`, `:147-153` |
| R-08 | m **[B]** | **`Registre::echoir` retire par `remove(i)` dans une boucle** — quadratique dans le pire cas, pour une liste qui compte rarement plus d'une attente. `retain` avec un emprunt disjoint sur `violations` rend la même liste dans le même ordre. | `crates/sim-core/src/oracle.rs:271-292` |

### 3.5 Mécanismes sans appelant — optimisations facultatives

Aucun de ces postes ne touche un résultat affiché ni un banc (D-07). Ils sont listés parce qu'ils sont vrais et parce qu'un jour un scénario les branchera ; **aucun n'est dans le chemin critique du plan**.

| # | Sév. | Constat | Où |
|---|---|---|---|
| O-01 | m **[B]** | **`Graphe::composantes` et `fortement_connexe` recherchent les arcs entrants en balayant tous les sommets** à chaque visite — Θ(n · Σ deg) au lieu de Θ(n + arcs) —, et `Generateur::tour` refait à chaque tour l'union de la fenêtre (avec un tri par `ajouter`) puis un test de forte connexité, soit deux balayages quadratiques par tour. Une adjacence inverse construite une fois par appel, une union par tri-dédoublonnage par sommet, et une `VecDeque` pour l'historique (`remove(0)` est linéaire). | `crates/sim-core/src/graphe.rs:59-64`, `:91-119`, `:138-163`, `:234-238`, `:247-257` |
| O-02 | m **[B]** | **`Domaines::tirer` dédoublonne par `contains`** : quadratique sur un domaine unique de n membres. Un `BTreeSet<u32>` rend la même liste triée, avec les mêmes tirages. | `crates/sim-core/src/horloge.rs:239-252` |
| O-03 | m **[B]** | **`Alignement::tour` calcule `sin` et `cos` de chaque cap `1 + d` fois** — une fois pour lui-même, une par voisin qui le lit. Deux vecteurs précalculés par tour : n × 2 transcendantes au lieu de n × 2(1 + d), mêmes bits. | `crates/sim-agents/src/alignement.rs:109-122` |
| O-04 | m **[B]** | **`Esquisse::estimer` appelle `libm::pow(2, −r)` 2 048 fois par estimation** (≈ 40 µs) là où 2⁻ʳ se construit par `f64::from_bits((1023 − r) << 52)` — **mesuré identique aux bits** pour `r < 32`, et `rang` est écrêté à 31. | `crates/sim-agents/src/agregat_fenetre.rs:109-125` |
| O-05 | m **[B]** | **`ancetres` cherche chaque événement par balayage** (`journal.iter().find`) et teste `trouves.contains` : Θ(N · k). Un index `BTreeMap<u64, &Evenement>` et un `BTreeSet` de visités ; la liste finale est triée de toute façon. | `crates/sim-agents/src/causalite.rs:86-119` |
| O-06 | info | `PushPull::cycle` calcule `somme()` — Θ(n) — deux fois par relance, `Rumeur::tour` et `Iteration::tour` clonent leur état par tour, `SeuilDeQuorum::tour` alloue deux `Vec` par agent et par tour, `Service::l99_de_reponse` clone et trie ses latences à chaque lecture. Tous à n ≤ 4 000 dans les tests, tous sous la seconde. Laissés tels quels. | `agregation.rs:238-264` ; `propagation.rs:120` ; `consensus_lineaire.rs:152` ; `accord.rs:293-322` ; `sim-core/src/service.rs:168-176` |

### 3.6 Tests et appareil

| # | Sév. | Constat | Où |
|---|---|---|---|
| T-01 | m *(décision)* | **Le dépôt n'a jamais passé `rustfmt`** : 60 fichiers, 225 différences, toutes de mise en page (`rustfmt` ne touche ni les chaînes ni les commentaires). Ce n'est pas une règle du dossier — `DEVELOPPEMENT.md` en nomme cinq, pas celle-là. Deux issues : appliquer une fois, en un commit isolé **avant** toute autre phase pour que les diffs qui suivent restent lisibles, et ajouter `cargo fmt --all --check` aux commandes d'avant commit ; ou décider que le dossier ne suit pas `rustfmt` et l'écrire. Deux conséquences mesurées de la première : la table d'histoire de `scenario.rs` descend de dix lignes (626 → 636, `rustfmt --emit stdout`), et `SPEC.md` l. 674 la cite par numéro ; et les lignes de panique embarquées dans tout binaire changent, ce qui touche le module WASM — le jour où il existe. Tranché au §4.8. | `cargo fmt --all --check` |
| T-02 | m | **Aucun test ne fige les empreintes d'exécution d'une révision à l'autre** : NF-04 vérifie qu'une graine rejoue **dans le même binaire**, jamais qu'un changement de code a laissé les traces intactes. Or six des sept phases de ce plan promettent l'identité bit à bit. Le banc de parité, côté natif seul (`parite-natif 1 20000`), rend six empreintes en une seconde sans Node ni WASM ; enregistrées **avant** la phase 1 dans le scratch de travail, elles sont la preuve de chaque commit « [B] ». À reproduire avec `banc_nf05` pour les colonnes `s simulées` et `retard max`, qui sont reproductibles. | `bancs/parite-wasm/src/main.rs` ; `crates/sim-agents/examples/banc_nf05.rs` |
| T-03 | M *(documentaire)* | **Le verdict NF-05 attribue à la rétention un gain que le code ne peut pas produire.** Il écrit que la chute de débit entre 200 000 et 1 000 000 d'événements « est corrigée » parce que « le journal croissait sans borne, faute de rétention » ; le PRD (l. 298) reprend « la part corrigeable — l'absence de rétention ». Or `Milieu::appliquer_retention` **n'a aucun appelant hors test** — `sim_milieu::hors_perimetre()` le déclare —, et le journal du scénario B croît toujours sans borne (`retard max` 356 061 à un million d'événements le confirme). Ce qui a réellement supprimé le facteur 10 est la **recherche binaire** de `Partition::valider` et de `Milieu::lire`, que le commentaire du journal date et chiffre (« 64 ms, 316 ms puis 1 405 ms pour n = 20 k, 40 k, 80 k validations »). Le verdict est juste sur le fait et faux sur la cause ; F2 le traite comme une provenance fausse. | `bancs/nf05-debit/VERDICT.md:48-56` ; `docs/PRD.md:298` ; `crates/sim-milieu/src/journal.rs:256-259`, `:489-493` |
| T-04 | info | **Le test `la_these_de_chaque_bloc_verifie_est_a_la_page_citee` embarque `Traité.md` entier** (`include_str!`, 5 256 lignes) dans le binaire de test de `sim-agents`. C'est délibéré et bon — la provenance se vérifie contre la source — ; noté pour que personne ne le prenne pour une fuite. | `crates/sim-agents/src/scenario.rs:468` |
| T-05 | info | Les tests d'intégration tournent en 12 s ; le plus long est `scenario_b.rs` (1,1 s). Rien à optimiser côté tests. | `cargo test --workspace --release` |

### 3.7 Ce que l'audit a écarté, et pourquoi le dire

- **Changer la file d'événements** (DT3) : `BinaryHeap` coûte log(2n) par opération, ≈ 100 ns ici. Le registre a déjà tranché — « la file calendaire ne se justifie que si NF-05 échoue », et NF-05 échoue pour une autre raison. Écarté.
- **Une exponentielle plus rapide** que `libm::exp` : elle change les bits, donc la parité natif/WASM mesurée par `parite-wasm`, et le verdict DT1 avec. Écarté (P-08).
- **Monter `eframe`/`egui` de 0.29** : hors du périmètre — rien dans le code n'en souffre, et un changement de rendu obligerait à remesurer l'empaquetage pour rien.
- **`clippy::pedantic` ou d'autres lints** : le dossier tient ses interdictions structurelles (neuf, en `deny`) ; le reste serait du style.
- **`HashMap`, `unsafe`, `thread`, `Instant` hors `sim-viz` et banc** : aucun dans les crates. Rien à écarter.

---

## 4. Plan d'exécution

### 4.1 Cadre

- **Un commit par phase**, chacun clos par les cinq commandes d'avant commit de `DEVELOPPEMENT.md` en sortie 0, plus `cargo fmt --all --check` si T-01 est adopté.
- **Toute phase marquée [B] prouve son identité bit à bit** par les six empreintes de `parite-natif` et les colonnes reproductibles de `banc_nf05`, comparées à celles enregistrées en phase 0. Une empreinte qui bouge sur une phase [B] est un défaut de la phase, pas une mesure à consigner.
- **Toute phase qui touche `crates/sim-viz/` refait l'empaquetage web, rejoue `bancs/parite-wasm` et `python Python/check-empaquetage.py`, et met à jour le couple d'octets NF-08** du `README.md` et de `CLAUDE.md`, l'ancien gardé à côté et daté — c'est la règle du dossier ; les phases 3 et 4 la déclenchent. ⚠ **Ce que la règle ne dit pas, et que l'audit a mesuré** : le module embarque les trois crates basses — un binaire release porte les chemins et les lignes de panique de `stigmergie.rs`, `journal.rs`, `oracle.rs`… —, donc **toute édition d'une des quatre crates, mise en forme comprise, change les octets du module**, et le mode « contenu » de `check-empaquetage.py` le verrait. Il ne le voit pas aujourd'hui : `web/sim_viz_bg.wasm` est **absent du disque** de la machine de mesure (`web/` ne contient qu'`index.html`), et le contrôle sort 0 en le disant. Le plan s'y conforme sans le contourner : **aucune construction avant la phase 3** — les phases 0 à 2 ne changent aucun octet d'un module qui n'existe pas —, puis une construction à la fin de chacune des phases 3 et 4, après quoi plus aucune crate n'est éditée. La chaîne est présente (`wasm-bindgen` 0.2.127, Node 24, cible `wasm32-unknown-unknown`).
- **Les numéros de ligne de cet audit sont ceux du commit `a7df123`.** La phase 0 les décale ; à partir d'elle, un constat se retrouve par son symbole, jamais par sa ligne.
- **Aucune phase n'affaiblit un test d'intégration** ; les tests qui changent le font parce qu'une signature change (phases 1 et 4), et le changement est nommé dans le commit.
- **Aucune phase ne touche `Traité.md` ni `Traité.pdf`.** Les listes d'absences ne perdent aucune entrée ; la phase 1 en **ajoute** une (D-05) et en reformule une (D-04), et les comptes qui en dépendent sont remesurés en phase 5.
- Les gains sont **mesurés, jamais annoncés** : chaque phase de vitesse rejoue `banc_nf05` et écrit le débit obtenu dans le journal d'exécution du §7, avec l'ancien.

### 4.2 Phase 0 — mise en forme et empreintes de référence (un commit, plus une mesure hors commit)

| Tâche | Constats | Geste |
|---|---|---|
| 0.1 | T-01 | `cargo fmt --all`, commit isolé « mise en forme rustfmt, aucun changement de code », et `cargo fmt --all --check` ajouté comme sixième commande d'avant commit dans `DEVELOPPEMENT.md`. **Dans le même commit**, parce qu'il en est la cause : le renvoi `scenario.rs (l. 617-634)` de `SPEC.md` (l. 674) passe à **l. 627-644** — mesuré par `rustfmt --emit stdout`, la table d'histoire descend de dix lignes — ou, mieux, devient un renvoi au symbole (« la table du rustdoc de `les_dix_blocs_nomment_leur_edition` »), qui ne se périme pas. Facultatif : le SHA du commit dans un `.git-blame-ignore-revs` à la racine du dépôt. |
| 0.2 | T-02 | Enregistrer dans le scratch de travail : `parite-natif 1 20000` (six empreintes), `parite-natif 7 150000` (les réglages de l'écran B, à n = 16), et `banc_nf05` (colonnes `s simulées` et `retard max`). Ce sont les références des phases 1, 2, 4 et 5. |
| 0.3 | P-08, P-09 | **Un profil échantillonné** de `banc_nf05` à n = 1 000 (par exemple `samply` ou l'outil que la machine a), pour remplacer la ventilation estimée du §3.1 par une mesure avant d'engager la phase 2. Si le profil contredit l'estimation — si les copies ne pèsent pas —, la phase 2 se réduit à P-02, P-03 et P-07, qui coûtent trois lignes chacune. |

Critère de sortie : `cargo fmt --all --check` en sortie 0 ; 467 tests verts et empreintes identiques — la mise en forme ne change aucun résultat, et c'est la première chose que les références de 0.2 prouvent ; une ventilation mesurée du cycle.

### 4.3 Phase 1 — code mort, tests et paramètres fantômes (un commit) [B]

| Tâche | Constats | Geste |
|---|---|---|
| 1.1 | D-01 | Retirer `Vue::derniere_sonde` et son écriture. Garder `maintenant` dans la signature de `sonder`, avec une ligne de doc disant qu'il n'est plus consommé — le retirer coûterait huit tests et un appelant pour rien. |
| 1.2 | D-02 | Retirer `Iteration::dernier_ecart`, son initialisation et le bloc de fin de `tour`. |
| 1.3 | D-03 | Retirer `Partition::durables`. |
| 1.4 | D-06 | `assert!(Detecteur::nouveau(Duree(1), Duree(10), 3).is_err())` à la place du `catch_unwind`. |
| 1.5 | D-08 | `conformite::estimer(f.milieu.partition(0).enregistrements())` dans `scenario_m`, sans `to_vec`. |
| 1.6 | D-04 | Retirer `_alea` de `Cascade::pas` (deux appels : le `derouler` des tests du module et celui de `sortie_phase_4.rs`), `alea` de `tableau_15` (quatre appels, trois dans le module et un dans `sortie_phase_4.rs` ; l'entrée « la graine est ignorée » de `hors_perimetre()` reste vraie et reste), et `auteur` de `Reconfiguration::ecrire` (six appels, quatre dans le module et deux dans `sortie_phase_4.rs`). L'entrée de `hors_perimetre()` sur le tableau 15 passe de « la graine est ignorée » à « aucune graine n'entre : rien n'est tiré » — une reformulation, pas un retrait. Choix retenu au §4.8. |
| 1.7 | R-06, R-07, R-08 | `absorber_octets` dans `sim-core` servant `Config::hachage` et `Trace::absorber` ; un seul tri dans `moyenne_et_queue` ; `retain` dans `Registre::echoir`. |
| 1.8 | D-05 | Le mode « époque » reste écrit et **est déclaré non provocable** : une entrée de `sim_agents::hors_perimetre()` — « mode « époque » du push-pull (lignes 5 et 6 de l'algorithme 4.1) : la relance est modélisée comme une remise à zéro instantanée et globale, donc deux époques ne divergent jamais et « Ligne::Epoque » n'est produite par aucune exécution ni aucun test » —, un commentaire sur la branche qui renvoie à l'entrée, et **un test qui fixe le constat** : après relances, crash et partition, toutes les époques sont égales et aucune rupture `Epoque` n'existe. Le jour où la relance devient un bavardage (§4.8), ce test tombe, et c'est ce qu'il est fait pour. Choix retenu au §4.8. |

Critère de sortie : 467 tests + 1, tous verts (1.6 renomme des appels, n'en retire aucun) ; **empreintes de 0.2 identiques** ; clippy et doc à 0 ; le compte de `hors_perimetre()` de `sim-agents` passe à **21**, et `CLAUDE.md`, `SPEC.md` §11 et le §0 du PRD le disent (phase 5).

### 4.4 Phase 2 — le chemin chaud du scénario B (un commit) [B]

Dans l'ordre du gain estimé, chaque geste rejouant les empreintes avant le suivant.

| Tâche | Constats | Geste |
|---|---|---|
| 2.1 | P-01 | Dans `sim-milieu` : `Milieu::plage_lisible(&self, partition, depuis, max) -> Range<usize>` (le calcul de `debut` et de la longueur, sans copie) et `Milieu::lire_multi_plages(&mut self, curseurs, budget_total, alea, sortie: &mut Vec<(u32, Range<usize>)>)` qui fait le mélange, borne le budget et facture `couts` exactement comme `lire_multi`. `lire` et `lire_multi` deviennent des enveloppes (`to_vec` de la plage) : leurs tests et leur doc ne bougent pas. **Un test neuf** : sur un journal de trois partitions et une graine, `lire_multi` et `lire_multi_plages` rendent les mêmes enregistrements dans le même ordre, et les mêmes `couts`. Dans `stigmergie` : un tampon `plages: Vec<(u32, Range<usize>)>` dans `Fourragement`, pris par `mem::take` le temps du cycle ; `actualiser_phi` prend les plages et lit `self.milieu.partition(p).enregistrements()[plage]` en place — emprunts disjoints sur `self.milieu` et `self.agents`. |
| 2.2 | P-02, P-03, P-04 | `Fourragement` gagne six champs privés calculés dans `nouveau` : `bornes: Result<Bornes, String>`, `depot: f64`, `periode: Duree`, `tau_tics: f64`, `ln_gamma: f64`, `fenetre_l99: Duree` (et le seuil de `compter_incomparabilite`, si ce mode est gardé tel quel). `params` passe de `pub` à privé avec `pub fn params(&self) -> &Params` — trois lectures à adapter (`scenario.rs:442`, `:447`, `scenario_m.rs:157`) —, sans quoi un paramètre modifié après construction désaccorderait le cache sans qu'aucun test le voie. `verifier_bornes` lit `self.bornes` ; `deposer` lit `self.depot` ; `periode()` disparaît. |
| 2.3 | P-05 | Deux tampons `curseurs: Vec<(u32, u64)>` et `poids: Vec<f64>` dans `Fourragement`, vidés et remplis par cycle. `compter_incomparabilite` : laissé tel quel — il ne tourne qu'en mode M2, et la recherche des deux premiers avec départage identique vaut plus de lignes qu'elle n'en économise. |
| 2.4 | P-06 | `utilite_max: f64` tenu à jour dans `nouveau` et `appliquer_bascule` ; `agir` l'additionne. Le paramètre `i` de `agir`, ignoré, est retiré. |
| 2.5 | P-07 | `clone_from` aux deux sites de `durabilite`. |
| 2.6 | — | Rejouer `banc_nf05` et consigner les quatre lignes avec celles de la phase 0 dans le journal du §7. Le débit est la seule colonne qui doit bouger ; `s simulées` et `retard max` doivent être **identiques**. |

Critère de sortie : empreintes de 0.2 identiques aux six cas et aux deux réglages ; `s simulées` et `retard max` identiques ; 467 + 1 tests verts ; débit consigné.

### 4.5 Phase 3 — l'interface (un commit, et le réempaquetage dans le même) [B]

| Tâche | Constats | Geste |
|---|---|---|
| 3.1 | V-01 | `VueA` gagne un champ `cache: Option<(CleA, Comparaison, Vec<[f64; 2]>, Vec<[f64; 2]>, Option<f64>)>` où `CleA` est le sextuplet des entrées (flottants comparés par `to_bits`). `afficher` recalcule tout — l'appel de tête et le balayage — **quand la clé change**, et sinon relit le cache ; `duree_ms` devient le temps mural du dernier recalcul. Reformuler `comment_cet_ecran_sexecute` (« se recalcule à chaque changement de réglage ; le balayage y est compris ») et la note du bandeau. Aucune sortie ne change : mêmes appels, mêmes valeurs. |
| 3.2 | V-02 | Facultatif, seulement parce que le fichier voisin est ouvert : ne rien faire dans `scenario_b.rs` si 3.1 suffit à la phase. |
| 3.3 | règle du dossier | `cargo build -p sim-viz --release --lib --target wasm32-unknown-unknown && wasm-bindgen …`, `python Python/check-empaquetage.py`, banc `parite-wasm` (six cas), puis les deux octets NF-08 dans `README.md` et `CLAUDE.md`, l'ancien couple gardé et daté. |

Critère de sortie : `check-empaquetage.py` en sortie 0 sur le module refait ; six empreintes natif/WASM identiques ; les six tests de `sim-viz` verts ; NF-08 remesurée et écrite.

### 4.6 Phase 4 — les refactorisations nommées au registre (un commit) [B][API]

Chacune est « le correctif de fond » que `docs/decisions.md` nomme pour un choix pris dans la vue. Elles changent des signatures publiques de `sim-agents`, donc elles touchent `sim-viz` — et la phase rejoue donc le §4.5, tâche 3.3, une seconde fois.

| Tâche | Constats | Geste |
|---|---|---|
| 4.1 | R-01 | `pub enum Vainqueur { Maille, Journal }` et `Comparaison::qui_gagne_en_temps(&self) -> Vainqueur` dans `scenario.rs` ; `verdict_temps` s'en sert. `scenario_a.rs` lit l'énumération ; `VAINQUEUR_MAILLE` et `le_vainqueur_se_lit_encore_dans_la_phrase_de_verdict` disparaissent, remplacés par un test de `scenario.rs` sur les deux régimes. `decisions.md` : la ligne « Le vainqueur en temps » passe de **[R]** à *fermée*, avec la date. |
| 4.2 | R-02 | `pub const SOURCE: &str = "§1.2, p. 16, 4ᵉ éd."` à côté de `Bornes::LEGENDE`, qui garde sa page en toutes lettres, et un test dans `sim-agents` que `LEGENDE.contains(SOURCE)` — la garde change de crate, elle ne disparaît pas. `scenario_b.rs` lit `Bornes::SOURCE` ; `SOURCE_BORNES` et son test disparaissent. |
| 4.3 | R-03 | `pub struct ParamsA { n, p, l99_ms, aller_simple_ms, degre_depot, taux_omission, graine }` avec `impl Default` portant les défauts du §7 du PRD et leur provenance en doc ; `scenario_a(&ParamsA) -> Comparaison`. `VueA` garde un `ParamsA` et cesse de transcrire ; `hors_perimetre()` (entrée « nombre de partitions du scénario A ») et l'onglet « Limites » (section « Ce que cette interface décide ») sont à reformuler : six valeurs de moins, il n'en reste trois, celles de `VueB`. `decisions.md` : la ligne « Remonter dans `sim-agents` les neuf valeurs » devient « les trois de `VueB` ». |
| 4.4 | R-04 | `plancher_observe: Option<f64>` et `hors_dominante_observee: Option<f64>` dans `Mesures` (le `Default` dérivé donne `None`, les deux `f64::INFINITY` de `nouveau` disparaissent) ; `verifier_bornes` met à jour par `Some(courant.map_or(x, \|m\| m.min(x)))` ; `ResultatM::hors_dominante` devient `(Option<f64>, Option<f64>)` ; `scenario_b.rs::jamais_vu` disparaît au profit d'un `match` ; les tests de `scenario_b.rs`, `scenario_m.rs` et `sortie_phase_6.rs` déballent par `expect("mesuré : au moins un cycle")`. **Le banc de parité absorbe `map_or(f64::INFINITY, \|v\| v).to_bits()`**, pour que les six empreintes ne bougent pas. Une douzaine de sites dans six fichiers, diff net négatif. Choix retenu au §4.8 ; c'est la première tâche à retirer si la phase doit raccourcir. |
| 4.5 | R-05 | `pub fn encadrement_de_detection(periode: Duree, expiration: Duree, seuil: u32) -> Result<(Duree, Duree), String>` dans `sim_core::detecteur` — le refus du seuil nul avec le motif « zéro échec », les deux bornes saturantes, et rien d'autre. `Detecteur::completude` l'appelle (son seuil est garanti non nul par le constructeur : `expect` documenté) ; `DetecteurInfectieux::completude` devient la conversion secondes → `Duree` autour de l'appel ; `cycle_de_vie::retirer` prend la borne haute. Les trois tests « 21 à 31 s » et les trois tests de saturation restent tels quels : le chiffre est toujours **retrouvé** par le calcul, jamais recopié (NF-15). Entiers saturants : bit-identique. `SPEC.md` §8 réécrit son paragraphe « les trois copies n'ont pas été factorisées » ; `decisions.md` reçoit la ligne qui applique la règle du comptage de PD7 à cet exemplaire (phase 5). Choix retenu au §4.8. |

Critère de sortie : empreintes identiques ; tests verts (le compte change : moins deux tests de garde dans `sim-viz`, plus un ou deux dans `sim-agents`) ; `check-empaquetage.py` et `parite-wasm` rejoués ; `decisions.md` et l'onglet « Limites » à jour.

### 4.7 Phase 5 — les documents (un commit)

| Tâche | Constats | Geste |
|---|---|---|
| 5.1 | T-03 | `bancs/nf05-debit/VERDICT.md` : la section « La seconde cause » attribue le facteur 1,1 à la **recherche binaire de `valider` et de `lire`**, cite la ligne de `journal.rs` qui la date, et écrit que la rétention **n'est branchée sur aucun scénario** (`hors_perimetre()`), l'ancienne attribution gardée et datée. `docs/PRD.md:298` : même correction, une phrase. |
| 5.2 | phases 2 et 3 | Le même `VERDICT.md` reçoit le tableau remesuré après la phase 2, avec la date et le commit, l'ancien tableau gardé. `SPEC.md` §12 et `DEVELOPPEMENT.md` : le compte de tests, refait par la ligne, jamais recopié d'ici. |
| 5.3 | phases 1 et 4 | `docs/decisions.md` : les quatre lignes fermées (R-01, R-02, R-03, R-04), une ligne neuve pour R-05 — « règle du comptage de PD7 appliquée à l'encadrement de détection : trois exemplaires écrits dans le traité (§4.3, §6.1, §7.3), une fonction ; DT6, qui porte sur l'**objet** détecteur, reste posée et non tenue » —, et une pour D-05. `docs/SPEC.md` : §8, le paragraphe des trois copies ; §9, le contrat de `sim-viz` passe de « à deux exceptions nommées » à « à une » ; §11, `hors_perimetre()` de `sim-agents` à 21 entrées. `CLAUDE.md` et le §0 du PRD : le même compte de 21, par la ligne `awk` qui le mesure. |
| 5.4 | T-01 | `DEVELOPPEMENT.md` : la sixième commande d'avant commit, et la phrase sur le mode « contenu » de `check-empaquetage.py` — il mord sur toute édition des quatre crates, pas seulement de `sim-viz`. |

**La phase facultative des mécanismes sans appelant (O-01 à O-05) est retirée du plan** — voir §4.8. Le §3.5 reste ce qu'il est : une réserve datée, à exécuter le jour où un scénario branche l'un de ces mécanismes, chaque geste y étant bit-identique et couvert par les tests existants du module.

### 4.8 Les six décisions — analyse et choix retenus

Chaque décision est instruite contre le code lu et contre les règles que le dossier se donne ; le choix retenu est celui que l'audit **propose**, et il vaut tant que l'auteur ne l'infirme pas avant la phase 0. Aucun des six ne rouvre une décision du registre ; deux en ferment.

#### T-01 — `rustfmt` : appliquer, en phase 0, et en faire un garde-fou

*Ce que le code montre.* 60 fichiers, 225 différences, **toutes de mise en page** — `rustfmt` ne touche ni les chaînes, ni les commentaires, ni les rustdoc (`wrap_comments` et `normalize_comments` sont désactivés par défaut), et le dépôt n'a aucun `rustfmt.toml`. Le dossier est écrit dans un style proche de `rustfmt` ; les 225 écarts sont des chaînes d'appels et des littéraux de struct pliés à la main.

*Ce que chaque option coûte.* **Appliquer** : un commit de 60 fichiers, du bruit dans `git blame` (neutralisable par `.git-blame-ignore-revs`), et deux conséquences mesurées — le renvoi de ligne de `SPEC.md` l. 674 se décale de dix lignes (0.1 le corrige dans le même commit), et les lignes de panique embarquées dans les binaires changent, ce qui **ne** touche aucun module tant qu'aucun n'est construit (§4.1). **Ne pas appliquer** : chaque phase de fond traînerait dans son diff les replis de mise en page des lignes qu'elle touche, ou les laisserait, et le dépôt continuerait de n'avoir aucune règle de forme écrite. **Appliquer seulement aux fichiers touchés** : la pire des trois — deux styles dans le même dépôt, et des diffs de fond qui mêlent les deux.

*Choix retenu.* **Appliquer, en phase 0, avant tout autre geste**, et ajouter `cargo fmt --all --check` comme sixième commande d'avant commit. Motif : le dossier fait respecter ses règles mécaniquement (neuf interdictions en `deny`, `missing_docs`, liens rustdoc) et celle-ci est la seule qui coûte zéro à tenir une fois posée ; et un audit qui cite 225 gestes de fond ne peut pas les livrer dans des diffs illisibles.

#### D-04 — les trois paramètres fantômes : retirer

*Ce que le code montre.* `Cascade::pas(&mut self, _alea)` ne tire rien — la cascade n'injecte aucune faute, son rustdoc le dit, et le seul aléa que le scénario J pourrait vouloir un jour est celui de la file par agent d'EX-C15, déclarée non branchée. `tableau_15(…, alea)` fait `let _ = alea` et `hors_perimetre()` déclare que « la graine est ignorée ». `Reconfiguration::ecrire(…, auteur, …)` fait `let _ = auteur` : S1w se décide sur l'époque, pas sur l'auteur, et aucun compteur du module ne distingue l'ancien propriétaire d'un tiers — ce que la sémantique d'EX-A41 n'exige pas.

*Ce que chaque option coûte.* **Retirer** : douze appels, tous dans des tests (`cascade.rs`, `allocation.rs`, `soupcon.rs`, `sortie_phase_4.rs`), une reformulation d'une entrée de `hors_perimetre()`, zéro effet sur un résultat. **Garder** : trois signatures qui promettent un aléa ou une attribution que le code ne consomme pas — c'est le mensonge d'affordance que PD6 interdit à l'écran, transporté dans l'API —, et, le jour où EX-C15 ou une vraie allocation se branchera, le paramètre reviendra de toute façon avec la sémantique qu'il aura alors, qui n'est pas forcément celle-ci (une `&mut Alea` pour une file par agent, ou un `TirageDeDecision` ?).

*Choix retenu.* **Retirer les trois** (tâche 1.6). C'est YAGNI appliqué à des signatures : un paramètre se rajoute en une ligne le jour où il sert ; un paramètre ignoré coûte à chaque lecture.

#### D-05 — la branche « époque » de `PushPull` : déclarer non provocable, et fixer le constat

*Ce que le code montre.* Les époques ne bougent qu'à la relance (`for e in &mut self.epoque { *e += 1 }`, **toutes** les entrées, vivantes ou non) et dans la branche elle-même. Ni le crash-arrêt, ni la partition, ni l'omission n'en désaccordent deux. `Ligne::Epoque` — « lignes 5 contre 6 » — est donc un mode de défaillance **déclaré**, avec son libellé et sa place dans l'énumération, **qu'aucune exécution ni aucun test ne produit** : NF-10 est déjà violée pour lui, silencieusement, depuis la phase 3.

*Ce que chaque option coûte.* **(a) Rendre le mode provocable** : la seule façon fidèle est de modéliser la relance comme ce qu'elle est dans l'algorithme 4.1 — un **bavardage** qui part d'un initiateur et se propage par les échanges, la ligne 5 faisant adopter l'époque nouvelle au retardataire. C'est un changement de modèle du scénario H, qui déplace le moment où la somme revient à zéro (progressif au lieu d'instantané), donc les grandeurs que le critère (3) de la phase 3 mesure (`retours_a_zero`, `derive_max`) et l'énoncé du traité que ce critère **retrouve** (« la relance ne plafonne pas l'erreur »). Ce n'est pas une optimisation, c'est une décision de produit à prendre avec le PRD, et le plan n'en prend aucune. **(b) Déclarer** : une entrée de `hors_perimetre()`, un commentaire, un test qui fixe le constat. **(c) Supprimer la branche** : vingt lignes de moins, mais un variant public `Ligne::Epoque` qui ne serait plus construit nulle part et un libellé orphelin — la discipline du dossier pour un mécanisme écrit et non branché n'est pas la suppression, c'est la liste d'absences (six mécanismes y sont déjà dans ce cas).

*Choix retenu.* **(b)**, en tâche 1.8 : la branche reste, l'entrée de `hors_perimetre()` dit pourquoi elle est inerte, et un test tombe le jour où quelqu'un rend les époques divergentes — c'est exactement ce que le dossier fait pour ses autres constats de mesure. L'option (a) est nommée au registre comme ce qu'il faudrait pour lever l'entrée.

#### R-04 — `Option<f64>` pour les deux minimums observés : faire, en dernier de la phase 4

*Ce que le code montre.* `plancher_observe` et `hors_dominante_observee` sont initialisés à `f64::INFINITY` et abaissés par `min` à chaque cycle ; la vue traduit l'infini en « jamais observé » (`jamais_vu`). Le registre a mesuré que la sentinelle ne survit qu'à une exécution **sans aucun cycle**, et nomme `Option<f64>` comme « le bon correctif » — c'est déjà la forme d'`ecart_a_loptimum()` deux lignes plus bas, et de `Proprietes::exactitude()` dans `sim-core`.

*Ce que chaque option coûte.* **Faire** : une douzaine de sites dans six fichiers (le mécanisme, le résultat M, trois fichiers de tests, la vue, le banc de parité), un diff net **négatif** — `jamais_vu` et ses dix lignes de rustdoc disparaissent, les deux `INFINITY` aussi — et une précaution au banc pour que les empreintes restent identiques. **Laisser** : une valeur magique dans une structure publique, une traduction dans la vue, et une ligne ouverte au registre, pour un cas que rien ne produit.

*Choix retenu.* **Faire** (tâche 4.4), parce que la phase 4 ouvre déjà ces fichiers, que le type dit alors ce que F1 exige — l'absence se déclare, elle ne se comble pas —, et que le résultat est moins de code. C'est la première tâche à retirer si la phase 4 doit raccourcir : elle ne change rien à ce qui s'affiche.

#### R-05 — les trois `completude` : factoriser, parce que la règle du comptage l'impose

*Ce que le code montre.* Trois fonctions calculent `période × (seuil − 1) + expiration` et sa borne haute `+ période`, avec la même saturation et le même refus du seuil nul — alignées **à la main** par le banc du 17 août, qui a corrigé trois fois le même défaut. `SPEC.md` §8 tient qu'elles ne sont pas factorisées « parce que PD7 est une décision ouverte » et que NF-15 veut le chiffre « retrouvé par une mesure, pas recopié d'un appel ».

*Ce que la règle dit vraiment.* PD7, tel que le PRD l'amende (§ « la règle du comptage »), n'interdit pas la factorisation : il exige que les exemplaires soient **comptés dans le traité** avant d'écrire, et fixe le seuil à trois — c'est le raisonnement même du rustdoc de `detecteur.rs` (« cinq exemplaires : le seuil de trois est franchi, la factorisation est due »). Ici le compte est fait par le dossier lui-même : §4.3, §6.1 et §7.3, trois exemplaires écrits dans la source, et la même dérivation. La règle est donc **satisfaite, pas suspendue**. Quant à NF-15 : une fonction partagée **calcule** 21 et 31 à partir de 10, 1 et 3, elle ne les recopie pas ; les trois tests qui les retrouvent restent inchangés, et ce sont eux qui tiennent l'exigence, pas le nombre de copies de la formule. Ce que la factorisation ne fait **pas** : elle ne touche pas à DT6, qui porte sur l'unicité de l'**objet** détecteur et reste « posée et non tenue ».

*Ce que chaque option coûte.* **Factoriser** : une fonction de dix lignes dans `sim-core`, trois appelants, ≈ 25 lignes de moins, entiers saturants donc bit-identique, deux paragraphes de documents. **Tenir ouvert** : trois copies à réaligner à chaque défaut trouvé sur l'une — le banc du 17 août l'a fait une fois ; il n'y a aucune raison que ce soit la dernière.

*Choix retenu.* **Factoriser** (tâche 4.5), et écrire au registre que c'est la règle du comptage de PD7 appliquée à cet exemplaire — non une réouverture de PD7 ni un arbitrage de DT6.

#### Phase facultative (O-01 à O-05) : retirer du plan

*Ce que le code montre.* Cinq optimisations bit-identiques, justes, sur des mécanismes **qu'aucun scénario n'appelle** — leurs seuls exécutants sont leurs tests, qui tiennent en une fraction de seconde, et l'ensemble de la suite en douze.

*Ce que chaque option coûte.* **Exécuter** : ≈ 60 lignes, un commit, zéro effet sur un résultat affiché, un banc ou une durée de test perceptible. **Retirer** : rien, puisque le §3.5 garde le constat avec sa ligne et son geste.

*Choix retenu.* **Retirer**, et laisser le §3.5 comme réserve datée : c'est la définition d'une optimisation spéculative, et RQ3 la surveille de la même façon qu'une abstraction spéculative.

### 4.9 Séquence et effort

| Phase | Commits | Fichiers touchés | Taille du diff | Risque | Gain |
|---|---|---|---|---|---|
| 0 | 1 (+ mesures) | 60 + `SPEC.md`, `DEVELOPPEMENT.md` | mise en page seule, plus deux lignes de prose | nul — empreintes et tests le prouvent | lisibilité des phases suivantes ; références ; une règle de forme tenue |
| 1 | 1 | 10 + `lib.rs` (liste d'absences) | ≈ −70 / +50 lignes | nul — bit-identique, tests existants + 1 | code mort retiré, trois signatures honnêtes, un mode déclaré |
| 2 | 1 | 3 (`journal.rs`, `stigmergie.rs`, `scenario.rs`) + `scenario_m.rs` | ≈ +90 / −40 lignes | faible — bit-identique, empreintes de garde | **20 à 35 % du temps par cycle**, à mesurer |
| 3 | 1 | 1 (`scenario_a.rs`) + `README.md`, `CLAUDE.md` | ≈ +40 / −10 lignes | faible — sorties identiques ; première construction du module | zéro calcul par image au repos sur l'écran A |
| 4 | 1 | 8 + `decisions.md`, `SPEC.md`, `lib.rs` (Limites) | ≈ +110 / −110 lignes | moyen — signatures publiques, trois crates, deux tests de garde retirés | quatre lignes du registre fermées, une formule au lieu de trois |
| 5 | 1 | 6 documents | prose | nul | une provenance fausse corrigée ; comptes remesurés |

L'ordre est contraint deux fois : la phase 0 précède tout (mise en forme et références), et la phase 4 suit la phase 3, parce que les deux touchent `sim-viz` et que la seconde rejoue le réempaquetage de la première. Les phases 1 et 2 sont indépendantes l'une de l'autre. Cinq commits, plus les mesures hors commit de la phase 0.

---

## 5. Limites de cet audit

- **La ventilation du temps par cycle est estimée, pas profilée** — la phase 0 le corrige avant la phase 2, et la phase 2 peut se réduire d'autant.
- **Les bancs WASM ne sont pas rejoués, et le module n'est pas sur le disque** de la machine de mesure ; l'identité bit à bit des phases [B] est prouvée côté natif par `parite-natif`, ce qui suffit à montrer que le code n'a pas changé de résultat, mais pas à remesurer la parité — la phase 3 construit le module et le fait.
- **Le micro-banc `libm` est celui de cette machine** (`x86_64-pc-windows-gnu`) ; en WASM, les rapports entre `exp`, copies et allocations peuvent différer, et la conclusion « `exp` n'est pas le goulot » y est à revérifier si NF-07 devient une cible.
- **Les listes d'absences n'ont pas été recomptées** ; elles l'ont été le 2 septembre, et rien de ce plan n'en retire une entrée, sauf D-05 et R-03 sur décision.
- **Aucun constat de comportement** : les 467 tests passent, et l'audit n'a pas cherché de défaut fonctionnel hors D-05, trouvé en lisant.

---

## 6. Commandes de rejeu

Depuis `3 - Traité/`, avec les deux lignes d'environnement de `DEVELOPPEMENT.md` posées (`PATH` et `CARGO_TARGET_DIR` hors de OneDrive).

```bash
cargo test --workspace --release
```

```bash
cargo clippy --workspace --all-targets --release
```

```bash
cargo doc --workspace --no-deps
```

```bash
cargo fmt --all --check
```

```bash
cargo run -p sim-agents --example banc_nf05 --release
```

Empreintes de référence — six cas du scénario B, côté natif, sans WASM ni Node :

```bash
cargo run --release --bin parite-natif -- 1 20000
```

Le banc de parité complet, le réempaquetage et son contrôle, après toute édition de `crates/sim-viz/` : les lignes de `DEVELOPPEMENT.md`, § « Commandes », et `python Python/check-empaquetage.py`.

Micro-banc `libm` de cet audit — un crate jetable de vingt lignes, `libm = "0.2"`, `opt-level = 3`, cible `x86_64-pc-windows-gnu` — dont les quatre chiffres du §2 sont la sortie ; il n'est pas versé au dépôt, et ce qui se cite d'ici est le protocole, pas le nombre.

---

## 7. Journal d'exécution — 4 septembre 2026

*Écrit après coup, comme un verdict de banc : cette section dit ce que
l'exécution a trouvé, y compris là où elle a démenti l'audit qui la planifiait.*

**Les six phases sont exécutées**, en six commits : `063d8dc` (rustfmt),
`b9b1879` (phase 1), `3548faa` (phase 2), `310c900` (phase 3), `367b602`
(phase 4) et celui qui porte cette section (phase 5).

### 7.1 Ce que la mesure a démenti dans cet audit

| Ce que l'audit écrivait | Ce que l'exécution a mesuré |
|---|---|
| La copie du journal coûte « environ 1 µs par cycle », et la phase 2 rendra 20 à 35 % | Le profil de la phase 0 mesure **2 940 ns par cycle**, soit 96 % du coût de lecture, et la phase 2 rend **×1,9**. L'estimation était basse d'un facteur trois dans les deux sens. C'est la raison d'être de la phase 0, et elle a servi |
| R-08 — `Registre::echoir` gagnerait à filtrer par `retain` | **Retiré sur mesure.** `retain` allouerait à chaque événement pour une liste presque toujours vide ; la boucle indicée existante n'alloue pas, et le pire cas quadratique qu'elle porte n'est atteint par aucun scénario. L'audit proposait un changement qui aurait coûté |
| R-04 — `scenario_b.rs::jamais_vu` disparaît au profit d'un `match` | **Gardée**, retypée en `Option<f64>`. Deux sites d'appel, et son rustdoc porte la raison F2 qu'un `match` en ligne aurait perdue : trois lignes de moins ne valent pas la perte du motif |
| Le couple NF-08 se périme « à la première édition de `crates/sim-viz/` » | Le module embarque **les quatre crates**, lignes de panique comprises : les phases 2 et 4 n'ont touché ni `sim-viz` ni son interface directe, et il a changé de taille deux fois. Corrigé au `README`, dans `CLAUDE.md` et dans `DEVELOPPEMENT.md` |
| La phase 5 corrige l'attribution fausse du gain NF-05 dans deux fichiers | **Trois** : `docs/decisions.md` portait la même erreur — « périmée depuis que la rétention existe » — et le plan ne l'avait pas vue |
| La phase 5 remesure le compte de tests dans `SPEC.md` et `DEVELOPPEMENT.md` | **Cinq fichiers** : `README.md`, `CLAUDE.md` et le §0 du PRD le portaient aussi. En laisser trois à 467 pendant que deux disent 470 aurait produit exactement le défaut que la règle du dépôt condamne |

### 7.2 Ce qui a été prouvé, et comment

**Identité bit à bit.** Les six empreintes de `parite-natif` sur deux réglages —
`1 20000` et `7 150000` — sont **identiques** avant et après les cinq phases, y
compris après `rustfmt`, après la refonte de la lecture du journal et après les
cinq refactorisations d'interface. Les colonnes reproductibles du banc NF-05,
`s simulées` et `retard max`, le sont aussi sur les quatre lignes. Le banc
`parite-wasm` rend les **six mêmes empreintes** natif et WASM, inchangées depuis
la phase 0.

**Le seul changement de comportement observable** est le nombre de fois que
l'écran A appelle `scenario_a` : cinquante par image, contre cinquante par
changement de réglage. L'image elle-même est identique au pixel près.

### 7.3 Un défaut de l'appareil, pas du code

`Python/check-empaquetage.py` **plante après avoir rendu son verdict** :
`UnicodeEncodeError` sur un `\u26a0` écrit vers une console `cp1252`. La sortie
utile est déjà imprimée, et le code de sortie reste 0, donc la porte ne ment
pas ; mais un contrôle d'avant commit qui trace une pile est un contrôle qu'on
apprend à ignorer. Contourné ici par `PYTHONIOENCODING=utf-8`. **Non corrigé** :
l'appareil Python n'est pas le périmètre de cet audit, et le corriger sans
l'avoir lu en entier serait le geste que cet audit reproche ailleurs.
