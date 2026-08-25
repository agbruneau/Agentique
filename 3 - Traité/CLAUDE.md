# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Ce qu'est ce dépôt

**stigmergie-lab** — simulateur déterministe d'essaims d'agents logiciels. Le
dépôt transpose un traité (`Traité.pdf`, **troisième édition du 15 août
2026 — 8 chapitres, 24 sections, 123 notices**) en logiciel exécutable. **Toute la
documentation vit dans [`docs/`](docs/)**, dont
[`docs/README.md`](docs/README.md) est l'index ; ce fichier et le `README.md`
restent à la racine par convention d'outil, et **`Traité.md` / `Traité.pdf` y
sont aussi** depuis l'entrée du dossier dans le dépôt Agentique, le 14 août 2026
— ce n'est pas un choix, c'est là que la fusion les a posés.

Deux documents font autorité, dans cet ordre :

1. **`Traité.pdf`** — source normative, à la racine du dossier et non sous
   `docs/`. Les algorithmes, les hypothèses et
   les chiffres viennent de là, et de nulle part ailleurs. **La pagination est
   celle de la troisième édition — 143 pages**, mesurées sur le PDF du dépôt le
   17 août 2026 : le format ferme de cent pages a
   été levé le 15 août 2026, de sorte qu'elle ne coïncide ni avec la deuxième
   édition ni avec aucun renvoi antérieur à la révision 3.0 du PRD, et qu'une
   page citée sans son édition est une provenance fausse, pas imprécise (F2).
   **La migration des renvois n'est pas finie, et elle se mesure** :

   ```bash
   grep -rhoE '§[0-9]+(\.[0-9]+)?, p\. [0-9]+' crates/ | sort | uniq -c | sort -rn
   ```

   Au 17 août 2026 à 08 h 32, cette ligne rend quatre pages différentes pour le
   seul §1.2 — `p. 16` dix fois, `p. 13` quatre fois, `p. 14` deux fois, `p. 12`
   une fois —, et le compte bouge d'une heure à l'autre pendant la migration.
   Dans la troisième édition, le §1.2 ouvre à la page 12 et l'énoncé des bornes
   est à la page 16. Chaque `p. N` est donc à revérifier contre le PDF avant
   d'être cru, et un renvoi qui porte son édition (`(3ᵉ éd.)`) est le seul qui
   se relise sans le refaire.
2. **`docs/PRD.md`** — la spécification, environ 2 340 lignes. Toute exigence porte un
   code (`EX-C01`, `EX-M09`, `EX-A31`, `EX-V12`, `NF-02`, `PD1`, `DT1`, `RQ3`…)
   que le code cite en commentaire. Chercher le code dans `docs/PRD.md` donne la
   lettre de l'exigence ; le §12 A donne la correspondance traité → implantation.

Le **§0 de `docs/PRD.md`** est le tableau de suivi : **six phases**, toutes
terminées — les cinq premières en vingt-neuf bancs, la sixième livrée avec son
critère de sortie atteint sur trois points et **refait sur la mesure** pour le
quatrième (§0.1). Il enregistre aussi
les **verdicts de banc**, les **réserves** et les **écarts au traité relevés par
la mesure**. Il se met à jour à la fin de chaque banc, pas en cours de route. Son
**§0.0** dit ce que la deuxième édition du traité a changé, et c'est ce qu'il faut
lire avant de toucher à un mécanisme existant — **mais c'est de l'histoire, et sa
pagination est celle de la deuxième**. Son **§0.2** enregistre le banc de vérification du
17 août 2026 : l'état mesuré du dépôt avec la ligne qui refait chaque compte, ce
que la troisième édition change (deux écarts qu'elle absorbe, un qu'elle
retourne, trois citations qu'elle retire), et ce que la campagne laisse ouvert.

**Attention aux renvois `§X.Y` ambigus.** Ils ne sont **pas** deux, comme ce
fichier l'a longtemps écrit : **quatorze** numéros de sous-section existent des
deux côtés — §2.1, §2.2, §2.3, §3.1, §3.2, §5.1, §5.2, §5.3, §6.1, §6.2, §6.3,
§8.1, §8.2, §8.3 — et aucun ne désigne la même chose dans les deux documents.
Les deux qui trompent le plus : le §8.3 du **PRD** est « ce que le produit ne
mesure pas », celui du **traité** « buts incompatibles » (ch. 8) ; le §5.1 du
**PRD** est le découpage en crates, celui du **traité** « mécanismes de
consensus ». Un renvoi qui peut se lire des deux côtés se qualifie — le banc du
17 août a qualifié les 219 sites nus du code, dont 33 visaient le PRD.

## Commandes

`cargo` n'est pas dans le `PATH` des shells de cet environnement. Préfixer :

```powershell
$env:PATH = "$env:USERPROFILE\.cargo\bin;$env:LOCALAPPDATA\Microsoft\WinGet\Packages\BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe\mingw64\bin;$env:PATH"
```

Le second chemin est mingw-w64 : `dlltool.exe` en vient, et `sim-viz` ne compile
pas sans lui (les trois autres crates n'en ont pas besoin).

Suite complète — **467 tests, 0 échec**, mesurés le 17 août 2026 à 11 h 14, exit 0
— 424 unitaires (254 `sim-agents`, 96 `sim-core`, 68 `sim-milieu`, 6 `sim-viz`) et
43 d'intégration. Le §0 du PRD enregistre 348 à la clôture de la phase 5 ; la
phase 6 a porté le compte à 419, le banc du 13 août à 428, celui du 17 août à 447,
puis 465, 466, 467. **Ce compte est une mesure, pas une constante** : il ne se cite
pas, il se refait par la ligne ci-dessous. Il a bougé **cinq** fois en trois
heures le 17 août, plusieurs agents écrivant en parallèle. **Le `target/` du dépôt ne convient
pas à la mesure** — l'édition de liens y échoue, et il faut dérouter
`$env:CARGO_TARGET_DIR` **hors de OneDrive** avant toute commande `cargo`.
✎ *Ce fichier attribuait l'échec à l'accent du chemin — « le chemin contient un
« é » », donc « un chemin ASCII » suffirait — jusqu'au 22 août 2026, et c'est
faux : un workspace d'essai sous `…/3 - Traité/`, même accent et même espace,
s'édite sans un mot hors de OneDrive. La seule variable qui change le verdict
est la synchronisation ; l'accent, le cache vieilli et la longueur du chemin ont
été éprouvés puis écartés le 21 août 2026, mesure à l'appui, à
[`docs/DEVELOPPEMENT.md`](docs/DEVELOPPEMENT.md).*

```bash
cargo test --workspace --release
```

Un seul test, ou un module :

```bash
cargo test -p sim-agents --release critere_2_le_seul_curseur
```

Lint — `clippy.toml` porte des interdictions structurelles, pas du style, et le
`[workspace.lints.clippy]` du `Cargo.toml` racine les passe en `deny` :

```bash
cargo clippy --workspace --all-targets --release
```

Documentation — troisième commande d'avant commit, et non facultative : les
quatre crates déclarent `#![deny(rustdoc::broken_intra_doc_links)]`, et rien
d'autre n'attrape un renvoi cassé.

```bash
cargo doc --workspace --no-deps
```

Interface native, campagne sans interface, bancs et diagnostics : voir
[docs/DEVELOPPEMENT.md](docs/DEVELOPPEMENT.md), qui donne la ligne exacte de chacun.

## Architecture

Quatre crates en **chaîne linéaire sans cycle**, plus deux bancs de mesure :

```
sim-core  ◄──── sim-milieu  ◄──── sim-agents  ◄──── sim-viz
```

| Crate | Fait | Ne fait pas |
|---|---|---|
| `sim-core` | Boucle à événements discrets, horloge logique, RNG semé, modèle de faute, détecteur, registre des hypothèses fortes, oracles, vérification statistique, **familles de décision** (EX-C19) | Ne connaît **ni** le journal partitionné, **ni** les agents |
| `sim-milieu` | Journal partitionné M1–M4, réplication ISR(k, m), rétention, latences, groupe de consommation, plan de contrôle facturé à part, **identité apposée, historique par identité, quota par ressource** (EX-M24 à M26) | N'implante **aucun** algorithme d'agent, **aucun** protocole d'accord ; n'**évalue jamais** le contenu d'un enregistrement (PD14) |
| `sim-agents` | Les mécanismes du traité, les oracles de propriétés, les paramètres d'ordre, **et les scénarios comme données** (paramètres, plages, critères d'acceptation) | Ne dessine **rien** |
| `sim-viz` | egui/eframe, tracés, onglets « Limites » et « Repères », échelle typographique, schémas figés | Contient **zéro** logique de simulation, **zéro** définition de scénario et **zéro** texte du traité — le glossaire vient de `sim_agents::glossaire`, les reformulations de `Bloc::en_clair` —, **à trois exceptions nommées, toutes déclarées à l'écran dans l'onglet « Limites »** (PD6) : le découpage du budget en tranches réimplanté par `situe_la_tranche`, les neuf valeurs d'ouverture de `VueA::default` et `VueB::default` (défauts du §7 du PRD, transcrits faute d'accesseur), et `SOURCE_BORNES`. **Ni export, ni parcours « le fil »** : O6 n'est pas livré |

La ligne de coupe est **le niveau de la boucle, pas le thème**. Un découpage
thématique (`sim-consensus`, `sim-gouvernance`) est explicitement interdit par
le §5.1 **du PRD** : il produirait le cadriciel que RQ3 surveille.

**Règle d'ouverture d'une cinquième crate** : les **deux** conditions à la fois
— plus d'une crate consommatrice, **et** une dépendance que les autres ne
doivent pas hériter. Réévaluée à la sortie de la phase 3 : aucun candidat, règle
reconduite. `sim-agents` fait trente et un modules et ce n'est pas un motif.

Le moteur est **passif** : il rend l'événement de date minimale, avance
l'horloge, et laisse l'appelant exécuter le gestionnaire puis réinjecter ce
qu'il produit. Pas de trait « gestionnaire » à une seule implantation.

## Contraintes non négociables

Elles ne sont pas des préférences de style. Chacune est mesurée ou lintée, et la
violer casse un critère de sortie déjà atteint.

- **PD1 — déterminisme.** Un seul fil, aucune horloge système dans le cœur, un
  unique `ChaCha8Rng` semé (`sim_core::alea::Alea`), aucune itération sur table
  de hachage dans un chemin qui influence l'ordonnancement. `clippy.toml`
  interdit `HashMap` et `HashSet` — utiliser `BTreeMap` / `BTreeSet`.
- **NF-02 — parité natif/WASM.** `clippy.toml` interdit **sept méthodes de
  `f64`** — `ln`, `exp`, `powf`, `sin`, `cos`, `atan2`, `mul_add`. Six sont
  mesurées **divergentes** entre cibles au banc DT1 ; la septième, `mul_add`,
  y est mesurée *identique* et reste interdite parce que son verdict **a changé
  entre deux passages du banc**, après installation de mingw — dépendre de la
  machine de construction est pire que diverger. Le fichier portait l'inverse en
  commentaire jusqu'au 17 août 2026 ; il porte désormais les deux motifs
  séparément, et le `reason` de `mul_add` avec. Passer par `libm::log`, `libm::exp`,
  `libm::pow`… Le verdict est
  [`bancs/dt1-flottant/VERDICT.md`](bancs/dt1-flottant/VERDICT.md) : **flottant
  partout, aucun point fixe**, contrairement à ce que le PRD recommandait avant
  la mesure. Aucune option d'arithmétique relâchée dans les profils.
- **PD2 — un oracle est une sûreté `[S]` ou une vivacité *bornée* `[L]`, jamais
  autre chose.** La vivacité non bornée n'est pas représentable : le
  constructeur qui l'omettrait n'existe pas (EX-C11).
- **PD10 — un prédicat local ne certifie jamais une propriété globale.** Un
  oracle à portée `Locale` porte son contre-exemple **et** le réglage qui le met
  en défaut, livrés, pas décrits.
- **PD12 — un détecteur soupçonne, il ne prouve pas.** Le taux de fausses
  suspicions est **calculé**, jamais paramétré.
- **PD6 — ce qui est absent s'affiche au même rang que ce qui est présent.**
  D'où les fonctions `hors_perimetre()` de `sim-milieu` et `sim-agents`, et
  `ModeleFaute::hors_modele()`. **Elles se tiennent à jour à chaque fin de
  phase** : une liste périmée déclare absent ce qui est livré, ce qui est le
  mensonge symétrique — et celui qui s'installe le plus facilement. Un module
  écrit mais qu'aucun scénario n'appelle y figure : il a le même effet sur un
  résultat qu'un module inexistant.
- **NF-12 — aucun test ne dépend de l'horloge murale ni d'un `sleep`.**
- **NF-14 — une hypothèse violée *efface* la borne.** Ni grisée, ni pointillée,
  ni astérisquée — y compris quand la mesure est meilleure que la borne effacée.
- **NF-15 — les chiffres du traité doivent être *retrouvés* par la mesure.** Un
  écart est un défaut du simulateur **ou** une erreur du traité, et les deux se
  consignent. **Cinq** sont consignés, tous au registre
  [`docs/decisions.md`](docs/decisions.md), et la conclusion de la troisième
  édition confirme le compte en citant ce dépôt (notice 120). **Leur classement a
  été refait le 17 août 2026 contre l'édition livrée** ; ne pas reprendre
  l'ancien :
  - **Deux sont absorbés par la source.** Le §3.1 de la 3ᵉ édition écrit
    7,933 × 10⁻³ et qualifie l'arrondi 7,9 × 10⁻³ d'énoncé faux ; le §4.1 écrit
    « elle se fige » et « la relance ne plafonne donc pas l'erreur ». Les deux
    mesures des phases 3 et 4 y sont désormais écrites. Ils restent des écarts
    contre la 2ᵉ édition et contre le texte du PRD.
  - **Deux portent contre le traité livré.** Φ_c, qui ne sépare pas la
    conformité de la coordination (§8.1) ; et le contrôleur d'élasticité, qui
    **contredit le §7.3 de la 3ᵉ édition** — celle-ci conclut à « un dépassement
    en escalier suivi d'une descente filtrée » et non à une oscillation. Ce
    second-là **n'est pas tranché** : le produit ne transpose ni la fenêtre nulle
    à la hausse ni les deux politiques de montée que la même page publie.
  - **Un ne porte pas sur le traité** : `mul_add`, qui porte sur la machine de
    construction.
- **PRD §8.3 — ce que le produit ne mesure pas.** Deux paires de grandeurs y
  sont tenues séparées, et mêler l'une ou l'autre est un défaut bloquant. Les
  deux **ℓ₉₉** : celle du milieu est une **entrée**, celle de réponse d'un agent
  est une **sortie**. Les deux **corrélations** : **ρ** corrèle les *pannes* et
  se dérive des domaines (EX-C14, livré) ; **Φ_c** corrèle les *décisions* et se
  dérive des familles (EX-C19, EX-A56 — **livré** en phase 6 ; ce qu'il mesure
  réellement est au §0.1 du PRD). Confondre les deux ferait
  passer une décision de conception pour un accident de plateforme.

## Conventions de code

- **Tout est en français** : noms de modules, de types, de champs, de fonctions,
  commentaires. `Enregistrement`, `Perception`, `temps_de_sejour`, `alea.rs`.
  Les termes techniques établis restent en anglais (`offset`, `push-sum`, ISR).
- **Tout item public porte un `///`, et le lint le fait respecter** : les quatre
  crates déclarent `#![deny(missing_docs)]`. Une doc utile donne l'unité,
  l'invariant ou la provenance — pas la paraphrase du nom. Sur un champ dont le
  nom dit déjà tout, écrire ce que le nom **ne** dit **pas** : « jamais un temps
  mural », « **total** et non par partition », « calculé, jamais paramétré ».
- **Chaque module ouvre sur un `//!` qui dit quelle section du traité il
  implante et quelle règle il tient**, souvent avec la citation en bloc `> `.
  Une grandeur sans provenance est traitée comme une faute de rédaction (F2) :
  les constantes portent leur `source: &'static str`.
- **Les tests unitaires vivent dans le module**, en `#[cfg(test)] mod tests`,
  nommés en phrase française : `le_rejeu_inter_versions_est_refuse`.
- **Les critères de sortie de phase sont des tests d'intégration** —
  `crates/sim-agents/tests/sortie_phase_N.rs` pour N ≥ 2. Ceux de la phase 1
  sont dans `determinisme.rs` et `scenario_b.rs` : il n'y a pas de
  `sortie_phase_1.rs`. Chaque test porte en doc le
  point du §9 qu'il vérifie, cité sans modification. Ne pas les affaiblir : ce
  sont les preuves du tableau du §0.
- Les décisions tranchées par la mesure plutôt que par le raisonnement
  s'écrivent dans un `VERDICT.md` sous `bancs/`, se résument au §0 du PRD, et
  entrent au registre [`docs/decisions.md`](docs/decisions.md).

## Réserves ouvertes

**Les principales.** La liste complète — **vingt-deux entrées** au 17 août 2026,
quatre ajoutées par le banc — est au §0 du PRD, et
la liste vivante est dans le code : `sim_agents::hors_perimetre()` (**20**
entrées), `sim_milieu::hors_perimetre()` (**13**), `ModeleFaute::hors_modele()`
(**5**, dont la première en énumère neuf). Ces trois comptes se remesurent :

```bash
awk '/pub fn hors_perimetre/,/^}/' crates/sim-agents/src/lib.rs | grep -cE '^\s*"'
```

- **Φ_c ne sépare pas la conformité de la coordination** — c'est le résultat de
  la phase 6, et il porte contre le traité autant que contre le PRD. La grandeur
  que le §8.1 **du traité** propose pour mesurer la conformité d'une population
  vaut **déjà ≈ 0,17** sur le scénario B avec un tirage par agent, parce que les
  agents lisent tous la même trace ; le curseur de familles ne la déplace que de
  ≈ 0,055 — de 0,173 à 0,228 —, non monotonement. Conséquence de conception
  appliquée : **l'effacement d'une borne suit le réglage, jamais Φ_c mesuré** —
  `dettes::verdicts` prend une `&Familles`.
  Le constat est dans `sim_agents::conformite::CONSTAT_DE_MESURE` et au §0.1 du
  PRD.
- **Quatre mécanismes du chapitre 8 n'ont aucun appelant** — le dépôt aveugle
  (EX-A57), l'historique par identité (EX-M25), le **quota par ressource**
  (EX-M26) et la file d'arbitrage (EX-A59) sont implantés et testés unitairement,
  et aucun scénario ne les exécute : sur un résultat, cela a exactement l'effet
  d'un mécanisme absent (PD6). La file d'arbitrage n'a même pas d'émetteur, faute
  de régime du §8.3 **du traité** dans le monde clos (T3).
- **Six mécanismes des phases 1 à 5 n'ont aucun appelant non plus** — adhésion,
  alignement, causalité, consensus linéaire, directive et reconfiguration.
  **Six** des quinze oracles du catalogue ne sont donc armés par aucune exécution
  — `CONSERVATION`, `ACCORD_LOCAL`, `D1`, `D2`, `UN_SEUL_PROPRIETAIRE` et
  `TOUTE_PARTITION_A_UN_PROPRIETAIRE` —, dont deux ne le sont nulle part, pas même
  par un test ; neuf tournent. Et les prédicats de M1, M4 et M10 ne sont évalués
  par personne. Les deux `hors_perimetre()` et le §3.3 de `docs/SPEC.md` le
  déclarent ; *ce fichier annonçait quatre jusqu'au 17 août 2026, et c'est le compte
  du code qui avait raison.*
- **`sim-core` n'a pas de `hors_perimetre()`, et c'est une décision ouverte.**
  `grep -rn 'fn hors_perimetre' crates/` n'en rend que deux. Les absences du cœur
  logent dans `ModeleFaute::hors_modele()`, dont ce n'est pas l'objet : sa première
  entrée énumère à elle seule **neuf** mécanismes sans appelant, dont
  `ModeleFaute::avertissements` — la moitié `[U]` d'EX-C06, tenue par personne.
  Trancher touche quatre documents et l'onglet « Limites » ; **ne pas créer la
  fonction sans la décision**, qui est au registre.
- **NF-05 n'est pas atteinte** — de l'ordre de 10 à 15 secondes simulées par
  seconde-cœur à n = 1 000, contre une cible de 10³. L'écart est structurel : chaque agent lit ce que toute la
  population écrit, donc Θ(n²). Voir
  [`bancs/nf05-debit/VERDICT.md`](bancs/nf05-debit/VERDICT.md). La cible est à
  refaire sur la mesure, comme DT1 l'a été.
- **NF-07 n'est pas mesurée** — 30 images/s à n ≤ 2 000 en WASM demande un
  navigateur en avant-plan avec une horloge d'images. L'empaquetage web, lui,
  est fait et NF-08 est tenue : **1 447 624 octets compressés** — 1,381 Mio, ou
  1,45 Mo en unités SI — sur 3 669 337 octets bruts, contre une cible de 8 Mo.
  **Ce couple est une mesure d'une construction précise, pas une constante** :
  celle du 17 août 2026 à 11 h 14, et il se périme à la première édition de
  `crates/sim-viz/`. Il se refait par les deux lignes du `README.md` (§ « 2.
  L'interface web »), qui sont ce qui se cite ici, jamais le nombre.
- **EX-V09 n'est pas câblée dans l'interface** — `sim_agents::partage` encode et
  décode le lien avec ses tests, mais `sim-viz` ne lit pas le fragment d'URL.
- **Le contrôleur d'élasticité ne converge pas** aux valeurs documentées, pour
  une raison structurelle qui ne contredit pas le traité (§2.2 du traité).
