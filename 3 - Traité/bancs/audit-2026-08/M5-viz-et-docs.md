# M5 — l'interface et la concordance des documents : anomalies mesurées

Périmètre : `crates/sim-viz/` en totalité, et les six documents qui affirment
quelque chose de vérifiable sur le dépôt — `README.md`, `docs/README.md`,
`docs/DEVELOPPEMENT.md`, `docs/architecture.md`, `docs/SPEC.md`, `CLAUDE.md`.

Toutes les mesures sont du **17 août 2026**, entre 08 h 09 et 08 h 34, heure
portée sur chacune. Quatre autres agents modifiaient `sim-core`, `sim-milieu` et
`sim-agents` pendant ce temps : les comptes qui dépendent de ces crates sont
donc horodatés, et deux d'entre eux ont bougé sous la mesure — le fait est
consigné plutôt que lissé (§ *Ce que ces mesures ne démontrent pas*).

Le `target/` du dépôt s'est trouvé incohérent à 08 h 26 — un `cargo clean`
concurrent avait retiré les `.rlib` sans invalider les empreintes, et l'éditeur
de liens échouait sur trente-six fichiers absents. Les mesures qui suivent
passent donc par un `CARGO_TARGET_DIR` propre à cet audit. Ce n'est pas un
défaut du dépôt ; c'est une condition de mesure, et elle est nommée.

---

## Table

| # | Où | Nature | Corrigée |
|---|---|---|---|
| 1 | `crates/sim-viz/src/lib.rs:931` | EX-V23 absente de la liste d'absences — PD6, et le §0 du PRD affirme le contraire | oui |
| 2 | `crates/sim-viz/src/scenario_b.rs:74,587,593` | `« §1.2, p. 13 »` en dur, contredit par `Bornes::LEGENDE` (`p. 16`) dans le **même cadre** | oui |
| 3 | `crates/sim-viz/src/scenario_b.rs:29-32` vs `:150` | Le `//!` dit ne jamais choisir une valeur ; `VueB::default` en choisit une | oui |
| 4 | `crates/sim-viz/src/lib.rs:927` | Accents graves rendus littéralement, contre le commentaire posé douze lignes plus haut | oui |
| 5 | `crates/sim-viz/src/lib.rs:854` · `scenario_b.rs:744,1332` | Renvois `§8.3` / `§5.1` non qualifiés — le cas que `CLAUDE.md` nomme | oui |
| 6 | `CLAUDE.md:8,18` | `docs/Traité.pdf` : le fichier est à la racine | oui |
| 7 | `CLAUDE.md:21` | « 116 pages » — le PDF du dépôt en a 143 | oui |
| 8 | `README.md:108-111` | NF-08 : 1 445 293 / 3 663 058 octets ne sont plus ce que la mesure rend | oui |
| 9 | `README.md:289` | « aucun point d'appel **dans la vue** » rend le compte de seize faux | oui |
| 10 | `docs/README.md:28,73` | Traité donné pour la 2ᵉ édition du 13 août ; c'est la 3ᵉ du 15 août | oui |
| 11 | `docs/README.md:14` · `README.md:11` | « le renvoi de `CLAUDE.md` n'est pas corrigé » — il l'est désormais | oui |
| 12 | `docs/architecture.md:238` | « dix-huit énoncés en dur » — dix-neuf après le correctif 1 | oui |
| 13 | `docs/SPEC.md:644-651` | « page de la deuxième édition » : le code n'en tient pas une seule | oui |
| 14 | `docs/SPEC.md:682` | « zéro texte du traité » — faux tant que `SOURCE_BORNES` existe | oui |
| 15 | 4 documents | 428 tests / 385 unitaires / 4 dans `sim-viz` — la mesure rend 447 / 404 / 5 | oui |
| 16 | `clippy.toml:8-10` | Le motif d'interdiction de `mul_add` contredit `bancs/dt1-flottant/VERDICT.md` | **non** |
| 17 | `docs/README.md:145` | « le journal … retiré du dépôt » — une pièce homonyme est à la racine | **non** |
| 18 | `crates/sim-agents`, `crates/sim-milieu` | Quatre pages différentes pour le seul §1.2 | **non** |

---

## 1 — EX-V23 n'était déclarée nulle part, et le PRD écrivait qu'elle l'était

`crates/sim-viz/src/lib.rs:846-990`, fonction `limites()` ; l'entrée ajoutée est
à la ligne 931.

**Preuve.** Le §0 du PRD, ligne 166 :

> | **EX-V23 n'a rien à afficher** | […] Le panneau n'est donc pas câblé dans
> `sim-viz`, et l'onglet « Limites » **le déclare** |

Il ne le déclarait pas.

```
$ grep -oE "EX-V[0-9]+" crates/sim-viz/src/*.rs | cut -d: -f2 | sort -u | tr '\n' ' '
EX-V01 EX-V02 EX-V03 EX-V04 EX-V05 EX-V06 EX-V07 EX-V08 EX-V09 EX-V11 EX-V12
EX-V13 EX-V18 EX-V19 EX-V20 EX-V21 EX-V22
```

Aucun `EX-V23`. Le §0 du PRD (ligne 151) énumère les seize exigences `EX-V*`
sans point d'appel : `V02`, `V03/V04/V19`, `V05`, `V06`, `V09`, `V13` à `V18`,
`V20/V21`, **`V23`**. L'onglet en déclarait quinze. Une absence non déclarée est
exactement le mensonge symétrique que PD6 vise, et il portait sur le seul
mécanisme du ch. 8 dont le §0 promettait qu'il était affiché.

**Changé.** Une entrée ajoutée à la liste, `lib.rs:931`, qui dit ce qui manque —
l'émetteur, pas le panneau :

> « EX-V23 — la file de demandes d'arbitrage. Le panneau est spécifié et
> « FileDarbitrage::affichage » rend son libellé complet ; ce qui manque est
> l'émetteur. Faute de régime du §8.3 du traité dans le monde clos, la file est
> vide en permanence, et un panneau perpétuellement vide se lirait « rien à
> arbitrer » là où il faut lire « rien ne peut y entrer ». »

`FileDarbitrage::affichage` existe bien : `crates/sim-agents/src/arbitrage.rs:167`.

**Conséquence.** L'onglet déclare maintenant les seize `EX-V*` que le PRD compte,
et le compte affiché à l'écran suit — il est calculé (`lignes.len()`), pas écrit.
Le §0 du PRD redevient vrai sans qu'on ait touché au PRD.

---

## 2 — Deux pages pour une seule source, dans un seul cadre

`crates/sim-viz/src/scenario_b.rs:549` et `:555` **à l'état trouvé** ; le code
livré porte la constante à `:74` et ses deux emplois à `:587` et `:593`, panneau
« Ce que le traité démontre ».

**Preuve.** À 08 h 21 :

```
$ grep -rn '§1.2, p. 1[36]' crates/sim-viz/src crates/sim-agents/src/stigmergie.rs
crates/sim-agents/src/stigmergie.rs:377:  … à corriger (§1.2, p. 16)";     ← Bornes::LEGENDE
crates/sim-viz/src/scenario_b.rs:549:     "§1.2, p. 13",
crates/sim-viz/src/scenario_b.rs:555:     "§1.2, p. 13",
```

`Bornes::LEGENDE` est affichée par ce même panneau, quatre lignes sous les deux
`du_traite` (`scenario_b.rs:577-582` dans le code livré). L'écran annonçait donc **p. 13** au-dessus
et **p. 16** au-dessous, pour la même section du même traité. Vérifié contre le
PDF du dépôt :

```
$ python -c "…"   # pymupdf, recherche plein texte
'n’atteint pas l’optimum'  -> page 16
'campe à distance bornée'  -> page 16
'plancher d’exploration'   -> page 16
```

`p. 13` était donc faux, et pas seulement divergent. La divergence s'est
d'ailleurs produite **pendant cet audit** : à 08 h 07, `stigmergie.rs:377`
portait encore `p. 13`.

`CLAUDE.md`, `docs/architecture.md` et `docs/SPEC.md` affirment tous trois que
`sim-viz` contient « **zéro** texte du traité ». Une référence de section et de
page en est un — c'est ce que F2 appelle une provenance, et le PRD en fait la
condition d'affichage de toute grandeur du traité.

**Changé.** `scenario_b.rs:74`, constante `SOURCE_BORNES`, alignée sur
`sim-agents` et **tenue par un test** — `la_provenance_des_bornes_suit_encore_sim_agents`,
`scenario_b.rs:1397`, qui échoue si `Bornes::LEGENDE` cesse de contenir la
chaîne. C'est le motif déjà employé dans cette crate pour `VAINQUEUR_MAILLE`
(`scenario_a.rs:88`), et pour la même raison : un couplage par chaîne qu'aucune
erreur de compilation n'attrape se paie par un test, pas par une convention.

```
$ cargo test -p sim-viz --release
test scenario_b::tests::la_provenance_des_bornes_suit_encore_sim_agents ... ok
test result: ok. 5 passed; 0 failed; …
```

**Conséquence.** Le cadre ne montre plus qu'une page. Une repagination du traité
fait désormais échouer `cargo test` au lieu de laisser l'écran citer une page qui
n'existe pas. Le correctif de fond — un accesseur de provenance dans `sim-agents`,
qui supprimerait la copie — est hors de la portée de ce morceau et reste ouvert.

---

## 3 — Le fichier déclare ne jamais choisir une valeur, et en choisit une

`crates/sim-viz/src/scenario_b.rs`, `//!` de tête (lignes 29-32) contre
`VueB::default` (ligne 150 dans le code livré, 123 à l'état trouvé).

**Preuve.** L'énoncé :

> Rien ici ne calcule un résultat : […] les six préréglages des constructeurs de
> [`Params`] (§5.1). Ce fichier choisit **où** poser ces valeurs, jamais ce
> qu'elles valent.

Le code :

```rust
params: Params { n: 16, ..Params::scenario_b() },
```

et `crates/sim-agents/src/stigmergie.rs:142` : `n: 64`. La vue s'ouvrait donc sur
un réglage qui n'est aucun des six préréglages, sur une valeur qu'elle avait
choisie elle-même, sans un mot.

**Changé.** L'énoncé du `//!` dit maintenant l'exception, la nomme unique et
donne son motif — l'exécution est en Θ(n²), et n = 64 fait payer seize fois le
premier tracé —, plus un commentaire au point de décision (`:153-160` dans le
code livré). *(Tour 2 : l'énoncé disait « une exception, et une seule » alors que
`VueB::default` en pose trois — voir E6 ci-dessous.)*

**Conséquence.** Le lecteur qui compte les six préréglages ne cherche plus
pourquoi aucun n'est marqué « chargé » à l'ouverture. Le comportement n'a pas
changé : passer à n = 64 aurait rendu le premier tracé seize fois plus cher, ce
qui est un coût réel pour le persona P1 du PRD.

---

## 4 — Des accents graves rendus littéralement, contre le commentaire du dessus

`crates/sim-viz/src/lib.rs:927` dans le code livré, `:915` à l'état trouvé.

**Preuve.** Le commentaire posé douze lignes plus haut, `lib.rs:915-916` dans le code livré :

> // Sans astérisques d'emphase : egui n'a pas d'analyseur
> // Markdown et les rendrait littéralement.

et la ligne d'EX-V09, dans la même liste :

```rust
"EX-V09 — le partage par fragment d'URL (encodé et décodé par \
 `sim-agents::partage`, jamais lu ici)",
```

Les accents graves ne sont pas plus analysés que les astérisques : `egui` n'a
aucun analyseur Markdown. L'écran rendait donc `` `sim-agents::partage` `` avec
ses deux accents. La ligne voisine (`:928`) emploie déjà des guillemets pour le
même besoin — la règle existait, elle n'était pas tenue partout.

**Changé.** Guillemets, comme la ligne voisine. **Conséquence** : la liste
d'absences est homogène, et le seul endroit de l'écran qui nomme un module ne
porte plus de ponctuation de balisage.

---

## 5 — Trois renvois `§X.Y` que `CLAUDE.md` demande de qualifier

`crates/sim-viz/src/lib.rs:854`, `scenario_b.rs:744` et `scenario_b.rs:1332`
dans le code livré (`:843`, `:706`, `:1294` à l'état trouvé) — chaînes
affichées, pas des commentaires. *(Tour 2 : la restriction aux chaînes affichées
est elle-même le défaut E4-E5 ; voir plus bas.)*

**Preuve.** `CLAUDE.md` :

> **Attention aux renvois `§X.Y` ambigus.** Le PRD et le traité ont tous deux un
> §8.3, et ils ne parlent pas de la même chose : celui du **PRD** est « ce que le
> produit ne mesure pas », celui du **traité** est « buts incompatibles » (ch. 8).
> Un renvoi qui peut se lire des deux côtés se qualifie.

Les trois chaînes portaient `(§8.3)`, `(§8.3)` et `(PD6, §5.1)` sans
qualification, dans une interface dont toute la grammaire d'EX-V11 désigne le
traité quand elle écrit `§`. Les trois visent le PRD : « ce que le produit ne
mesure pas », les deux ℓ₉₉, et le découpage en crates. Le §8.3 du traité, lui,
est bien « Buts incompatibles » — vérifié sur la table des matières du PDF,
p. 124.

**Changé.** `(§8.3 du PRD — celui du traité porte sur les buts incompatibles)`,
`(§8.3 du PRD)`, `(§5.1 du PRD)`.

**Conséquence.** Un lecteur qui suit le renvoi tombe sur le bon document. Les
autres `§` affichés par l'interface (`§1.1`, `§4.1`, `§1.2`) désignent le traité
et sont exacts ; ils n'ont pas été touchés.

---

## 6 et 7 — `CLAUDE.md` : un chemin faux et un compte de pages faux

**Chemin.** `CLAUDE.md:8` et `:16` visaient `docs/Traité.pdf` ; les deux énoncés
corrigés sont aux lignes 8 et 18 du fichier livré.

```
$ ls docs/
DEVELOPPEMENT.md  PRD.md  README.md  SPEC.md  architecture.md  decisions.md
$ ls Traité.*
Traité.md  Traité.pdf
```

Le `README.md` et le `docs/README.md` signalaient tous deux l'erreur en la
laissant en place (« `CLAUDE.md` porte encore l'ancien chemin »). Corrigé, et les
deux signalements mis à jour en conséquence (anomalie 11).

**Pages.** `CLAUDE.md:18` à l'état trouvé, `:21` dans le fichier livré :
« **La pagination est celle de la troisième édition — 116 pages** ».

```
$ python -c "import pymupdf; print(pymupdf.open('Traité.pdf').page_count)"
143
```

Le folio de la dernière page est 143, la table des matières donne les
« Références » à la page 130 et le chapitre 8 à la page 117 — un chapitre entier
tombe au-delà des 116 annoncées. Le PDF a été écrit le 15 août à 17 h 36,
`CLAUDE.md` le même jour à 12 h 44 : le compte datait d'avant le tirage qu'il
décrit.

**Changé.** 143 pages, avec la date de mesure. Et la clause qui suit est passée
d'une affirmation à une commande, parce que la migration des renvois est en
cours et que le compte bouge d'une heure à l'autre :

```
$ grep -rhoE '§[0-9]+(\.[0-9]+)?, p\. [0-9]+' crates/ | sort | uniq -c | sort -rn
```

À 08 h 32, quatre pages pour le seul §1.2 : `p. 16` dix fois, `p. 13` quatre
fois, `p. 14` deux fois, `p. 12` une fois. À 08 h 21, la même ligne rendait
`p. 13` quinze fois et `p. 16` cinq fois. Un compte gravé dans un document se
serait périmé en onze minutes ; la ligne de commande, elle, ne se périme pas.

---

## 8 — NF-08 : l'empaquetage mesuré n'était plus celui qui est écrit

`README.md:108-111` dans le fichier livré (`:109-111` à l'état trouvé).

**Preuve.** L'énoncé : « Module compressé : **1 445 293 octets** […] sur
3 663 058 octets bruts. Remesuré à chaque révision de l'interface. »

État trouvé à 08 h 11 :

```
$ stat -c '%n %s' web/*
web/index.html 4410
web/sim_viz.js 68213
web/sim_viz_bg.wasm 3613854      ← ni 3 663 058, ni rien de ce qui est écrit
```

Le module livré datait du 13 août 07 h 41, alors que `lib.rs` et `scenario_b.rs`
avaient été écrits le 14 août à 00 h 02 et 00 h 18. L'empaquetage était donc
vieux de deux révisions de l'interface, et la phrase « remesuré à chaque
révision » était fausse au moment même où elle le promettait.

Reconstruit à 08 h 13 par la commande du `README` :

```
$ cargo build -p sim-viz --release --lib --target wasm32-unknown-unknown \
  && wasm-bindgen --target web --no-typescript --out-dir web \
     target/wasm32-unknown-unknown/release/sim_viz.wasm
$ printf "brut=%s gz9=%s\n" "$(stat -c%s web/sim_viz_bg.wasm)" \
                            "$(gzip -9 -c web/sim_viz_bg.wasm | wc -c)"
brut=3663250 gz9=1445512
```

1 445 512 octets, soit 1,378 Mio ou 1,45 Mo SI, contre une cible de 8 Mo : NF-08
reste tenue d'un facteur 5,5. Les deux chiffres écrits étaient donc justes à
219 et 192 octets près — mais sur un module qui n'était pas celui du dépôt.

**Changé.** Les deux chiffres, avec l'heure de mesure, et un avertissement qui
remplace la promesse : `web/sim_viz.js` et `web/sim_viz_bg.wasm` sont dans
`.gitignore`, ils ne se remesurent que si l'on relance la commande.

**Conséquence.** La cible NF-08 reste tenue ; ce qui ne l'était pas était la
prétention à un remesurage automatique, que rien dans le dépôt ne produit.
Reconstruire le paquet n'altère aucun fichier suivi.

---

## 9 — « aucun point d'appel *dans la vue* » fausse le compte de seize

`README.md:287-292` dans le fichier livré (`:266-269` à l'état trouvé).

**Preuve.** Le §0 du PRD compte seize `EX-V*` **sans point d'appel** et sept qui
en ont un : `V01, V07, V08, V10, V11, V12, V22`. Or EX-V10 est le binaire
`campagne` (PRD, ligne 1064), qui n'est pas la vue. « Seize […] et aucun point
d'appel **dans la vue** » comptait donc dix-sept exigences sous une étiquette de
seize.

**Changé.** La qualification retirée, EX-V23 nommée, et la place d'EX-V10 dite
explicitement.

---

## 10 et 11 — `docs/README.md` décrit la deuxième édition du traité

`docs/README.md:28` (nœud mermaid) et `:73` (tableau des documents) dans le
fichier livré (`:27` et `:72` à l'état trouvé).

**Preuve.** Le document donnait « SOURCE NORMATIVE — 2ᵉ édition » et « deuxième
édition du 13 août 2026 ». L'en-tête du traité livré :

```
$ head -6 Traité.md
date: "15 août 2026 — troisième édition, revue sur sa propre mesure"
```

`README.md` et `CLAUDE.md` disent tous deux « troisième édition du 15 août 2026 ».
`docs/README.md` était le seul des trois à décrire un tirage antérieur.

Les autres comptes de cette entrée ont été vérifiés et sont **exacts** ; ils
n'ont pas été touchés :

```
$ printf "h2=%s h3=%s\n" "$(grep -c '^## ' Traité.md)" "$(grep -c '^### ' Traité.md)"
h2=11 h3=24                        # 8 chapitres numérotés + intro/conclusion/références
$ grep -cE "^(Table:|: )" Traité.md
22                                 # 22 tableaux
$ grep -nE '^Algorithme [0-9]' Traité.md | wc -l
10                                 # 10 blocs légendés, dont l'algorithme 8.1
$ grep -oiE "figure [0-9]+\.[0-9]+[a-c]?" Traité.md | sort -u | wc -l
18                                 # 18 légendes, 16 numéros (2.1 se décline en a/b/c)
$ awk 'NR>1749' Traité.md | grep -cE '^[0-9]+\. '
123                                # 123 notices
```

**Changé.** Troisième édition, 15 août 2026, 143 pages, 123 notices, et un
avertissement sur la pagination — le PRD reste figé à la deuxième, ce que ce
document n'a pas le droit de trancher mais a le devoir de signaler.

---

## 12, 13, 14 — trois énoncés que le correctif ou la mesure a rendus faux

**`docs/architecture.md:238`** — « dix-huit énoncés en dur ». Compté avant
correctif : 8 dans « Hors de portée de la mesure » + 10 dans « Ce que cette
interface n'affiche pas » = 18 ✓. Après l'ajout d'EX-V23 : 19. Corrigé, et le
motif du manque écrit à côté du compte.

**`docs/SPEC.md:644-651`** (`:636` à l'état trouvé) — « une `source` avec section et page de la deuxième
édition ». Le code n'en tient pas une seule : voir la mesure du § 6-7. Réécrit
pour dire ce que le code fait — la règle de rédaction que ce document se donne
lui-même —, avec la ligne de commande qui refait le constat.

**`docs/SPEC.md:682`** (`:666` à l'état trouvé) — « **Zéro** texte du traité ». Faux tant que
`SOURCE_BORNES` existe. L'exception est maintenant nommée, avec son test.

---

## 15 — Les comptes de tests

**Preuve.** Deux mesures, la première avant toute modification :

```
$ cargo test --workspace --release        # 2026-08-17 08:10:27
TOTAL PASSED = 428    0 failed
```

428 exactement — la valeur des quatre documents était juste à 08 h 10. Après les
correctifs de ce morceau et le travail concurrent des quatre autres agents :

```
$ cargo test --workspace --release        # 2026-08-17 08:32:09
TOTAL = 447  exit=0
… 247 passed (sim-agents lib) … 91 (sim-core) … 61 (sim-milieu) … 5 (sim-viz)
… 4 + 11 + 5 + 4 + 5 + 3 + 11 = 43 (intégration)
```

447 = 404 unitaires + 43 d'intégration. La répartition écrite dans
`docs/DEVELOPPEMENT.md` et `docs/SPEC.md` (239 / 86 / 56 / 4, et 385 unitaires)
ne correspond plus.

**Changé.** 447 / 404 / 247 / 91 / 61 / 5 dans `CLAUDE.md`, `README.md` (deux
endroits), `docs/DEVELOPPEMENT.md` et `docs/SPEC.md` (trois endroits), chaque
fois avec l'heure. Les mentions historiques de 428 sont conservées comme
historique, pas comme état.

**Conséquence, et c'est la limite de ce correctif.** Ce compte est le seul de ce
rapport qui ne se stabilise pas : quatre agents ajoutaient des tests pendant la
mesure, et 428 → 447 est en partie leur ouvrage. Un seul de ces dix-neuf tests
est de ce morceau — `la_provenance_des_bornes_suit_encore_sim_agents`. C'est
pourquoi les trois documents disent désormais que le compte **est une mesure**
et donnent la ligne qui la refait.

---

## Anomalies identifiées et **non** corrigées

### 16 — `clippy.toml:8-10` contredit le verdict DT1

```
# `mul_add` diverge pour une autre raison — arrondi unique matériel contre
# double arrondi en WASM — et se remplace soit par `a * b + c`, soit par
# `libm::fma` si l'arrondi unique est voulu.
```

`bancs/dt1-flottant/VERDICT.md`, lignes 24 et 29-31, mesure l'inverse :

> | `f64::mul_add` | constat | **instable — voir ci-dessous** |
> Au premier passage, `f64::mul_add` divergeait entre natif et WASM. Au second —
> après l'installation de mingw-w64 […] il **coïncide**.

`mul_add` n'est pas interdite parce qu'elle diverge ; elle est interdite parce
que son verdict **a changé entre deux passages**, ce qui la rend dépendante de la
machine de construction. `docs/DEVELOPPEMENT.md` et `docs/SPEC.md` portent tous
deux le motif exact ; seul `clippy.toml` porte l'ancien.

**Motif du non-correctif** : `clippy.toml` n'est ni dans `crates/`, ni dans les
six documents attribués à ce morceau. Le changement est d'un commentaire de trois
lignes, sans effet sur le lint.

### 17 — `docs/README.md:145` déclare disparu un fichier présent

> **Ce qui a existé et n'existe plus** : le journal de la revue adversariale qui
> avait produit la version 2.0 du PRD, retiré du dépôt.

L'historique git donne ce retrait au commit `4dfc0dc`, et `git status` donne à la
racine une pièce homonyme non suivie, dont la première ligne l'annonce comme le
journal de la boucle de l'audit complet du code. L'énoncé est donc vrai de
l'histoire git et faux du répertoire : la pièce présente est le journal **de cet
audit-ci**, non suivi, homonyme. ⚠ *Les trois commandes reproduites ici la
nommaient : elles sont retirées le 25 août 2026, avec son nom, sur instruction
d'auteur — la pièce est sortie du dépôt le 22 août.*

**Motif du non-correctif** : le fichier est nommé document normatif dans le
mandat de ce morceau, donc hors d'atteinte ; et décrire dans un index permanent
un artefact de session serait la faire vieillir plus vite que l'énoncé qu'elle
remplace. À trancher à la passe de consolidation, quand on saura si ce journal
reste.

### 18 — Quatre pages pour le §1.2 dans `sim-agents` et `sim-milieu`

Mesure à 08 h 32 (§ 6-7). Restent notamment
`crates/sim-milieu/src/journal.rs:633-636` — les quatre oracles M1 à M4 armés
sur `« §1.2, p. 13 »` — et huit entrées de
`crates/sim-agents/src/glossaire.rs`, alors que `Bornes::LEGENDE` et `BLOC_B`
sont déjà passés à `p. 16 (3ᵉ éd.)`. La mesure sur le PDF donne l'ouverture du
§1.2 à la page 12 et l'énoncé des bornes à la page 16 ; `p. 13` ne correspond à
ni l'un ni l'autre.

**Motif du non-correctif** : les trois crates sont le morceau d'autres agents, et
la migration y était en cours pendant la mesure — quatre occurrences ont changé
d'elles-mêmes entre 08 h 07 et 08 h 32. Le côté `sim-viz`, lui, est corrigé et
tenu par un test.

---

## Ce qui a été vérifié et tenait

Ces énoncés ont été éprouvés et n'ont pas été touchés. Ils comptent autant que
les défauts : sans eux, la liste ci-dessus ne dit pas ce qu'elle a couvert.

- **NF-14 — la borne est effacée, pas grisée.** `scenario_b.rs:578-604` : la
  branche `Err` de `bornes_applicables()` n'affiche que le motif, aucune valeur,
  aucun pointillé. Un **seul** lecteur des bornes dans tout l'écran, sur les
  paramètres vivants ; `effort_a_la_tranche` n'en lit aucune (`:1244-1336`), donc
  aucune figure ne peut redessiner un plancher que le panneau vient d'effacer.
  Les mesures, elles, restent affichées — `Fourragement::verifier_bornes` les
  relève avant le portail, ce que `jamais_vu` documente.
- **PD3 — Θ(1) par rapport à n.** Aucun widget de `sim-viz` n'est indexé sur la
  population : les deux figures posent une barre par **ressource**
  (`r.phi_moyen`, `courante`), le schéma du scénario A est figé à six agents.
- **F3 — le mot « convergé ».** `grep -rn "converg" crates/sim-viz/src/` ne rend
  que la ligne de `lib.rs:28` qui énonce la règle.
- **L'échelle typographique.** Les sept `.size(` de la crate emploient les trois
  constantes `THESE`, `TITRE_SECTION`, `MESURE` ; aucune taille n'est retapée au
  point d'appel, comme le `//!` l'affirme.
- **Chemins de panique.** Les deux `expect` de `lancer_web` sont gardés par
  `#[cfg(target_arch = "wasm32")]` et documentés. Les trois indexations directes
  — `series[*tranche]`, `part(courante, vedette)`,
  `r.partition_des_ressources[j]` — sont sûres : `*tranche` est écrêté à
  `derniere` (`:1249`), et `meilleure_ressource`, `phi_moyen`,
  `partition_des_ressources` et chaque tranche de `effort_par_tranche` dérivent
  tous de `ressources`, de longueur `m`
  (`stigmergie.rs:620`, `:1079`, `scenario.rs:431-432`).
- **Les quinze littéraux de plage de curseur** annoncés par `docs/SPEC.md:681` :
  comptés, six au scénario A et neuf au scénario B.
- **Les dix-sept filtres de test des treize lignes du tableau du `README`**
  rendent tous un ensemble
  non vide (`scenario::` 7, `usl::` 8, `scenario_d::` 7, `adhesion::` 5,
  `allocation::` 10, `gouvernance::` 11, `taux_de_base::` 13, `agregat_fenetre::`
  7, `agregation::` 10, `cascade::` 10, `soupcon::` 16, `elasticite::` 12,
  `propagation::` 12, `accord::` 9, `consensus_lineaire::` 8), et
  `--test scenario_b` / `--test sortie_phase_6` en donnent onze chacun.
- **La commande d'exemple de `CLAUDE.md` et de `docs/DEVELOPPEMENT.md`**,
  `cargo test -p sim-agents --release critere_2_le_seul_curseur`, sélectionne
  bien un test et un seul —
  `critere_2_le_seul_curseur_de_structure_fait_seffondrer_p_i_sachant_a`, dans
  `tests/sortie_phase_5.rs`.
- **Les comptes des trois listes d'absences** de `docs/SPEC.md:719-721` : 19, 9
  et 5, retrouvés dans le code.
- **`sim-agents` fait bien trente et un modules** (32 fichiers moins `lib.rs`),
  **le glossaire trente-deux termes**, **`main.rs` seize lignes dont six de
  code**, **les DT du PRD quatorze**, **les figures du traité dix-neuf fichiers
  sous `../figures/`**, **les noms de paquet des deux bancs** `banc-dt1` et
  `banc-parite` et leurs binaires `dt1-natif` et `parite-natif`.

---

## Preuves finales

```
$ date                                    2026-08-17 08:34:05
$ cargo clippy -p sim-viz --all-targets --release
    Finished `release` profile [optimized] target(s) in 1.60s
exit=0
$ cargo doc -p sim-viz --no-deps
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 2.47s
   Generated …/doc/sim_viz/index.html and 1 other file
exit=0
$ cargo test -p sim-viz --release
test scenario_a::tests::le_vainqueur_se_lit_encore_dans_la_phrase_de_verdict ... ok
test scenario_b::tests::la_tranche_se_situe_de_part_et_dautre_de_la_bascule ... ok
test scenario_b::tests::la_ligne_de_differences_nomme_ce_que_le_prereglage_deplace ... ok
test scenario_b::tests::la_provenance_des_bornes_suit_encore_sim_agents ... ok
test scenario_b::tests::chaque_prereglage_dit_ou_regarder ... ok
test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
exit=0
$ cargo test --workspace --release        # 08:32:09
TOTAL = 447  exit=0
```

Aucun avertissement sur les trois commandes. Zéro test affaibli ou retiré ; un
ajouté.

---

## Ce que cet audit ne démontre pas

- **Rien sur le rendu.** Aucune des corrections d'affichage — accents graves,
  qualification des renvois, ligne EX-V23 — n'a été vue à l'écran. `sim-viz` ne
  s'éprouve que par lecture et par `cargo`, l'interface n'ayant aucun test de
  rendu et NF-07 n'étant pas mesurée. Les trois défauts sont établis par le
  code et par la règle qu'ils violent, pas par une capture.
- **Rien sur le compte de tests dans une heure.** 447 est un instantané pris à
  08 h 32, pendant que quatre agents modifiaient trois crates. La suite entière
  a été verte à ce moment ; elle avait un test en échec à 08 h 30, dans
  `sim-agents`, chez un autre morceau, et verte de nouveau à 08 h 31 sans que
  rien de ce morceau n'y touche.
- **Rien sur les pages du traité hors du §1.2.** Quatre renvois ont été vérifiés
  contre le PDF — l'ouverture du §1.2, l'énoncé des bornes, le §8.3 et le
  chapitre 8. Les trente-neuf autres `p. N` du dépôt ne l'ont pas été, et la
  mesure du § 6-7 ne dit pas qu'ils sont faux : elle dit que le dépôt en donne
  plusieurs pour une même section, ce qui suffit à établir qu'au moins un l'est.
- **Rien sur les documents non attribués.** `docs/PRD.md`, `docs/decisions.md` et le
  journal de boucle n'ont pas été audités et n'ont pas été touchés. Deux
  affirmations du PRD ont servi de preuve contre le code (§0, lignes 151 et 166) ;
  c'est le code qui a été mis en accord, jamais l'inverse.

---

## Tour 2

Réponse au jugement `bancs/audit-2026-08/M5-critique.md`. Mesures du **17 août
2026, entre 09 h 08 et 09 h 14**, même périmètre et mêmes conditions qu'au tour 1
— `CARGO_TARGET_DIR` propre à l'audit, quatre autres agents écrivant dans
`sim-core`, `sim-milieu` et `sim-agents` pendant ce temps. Le fait s'est
manifesté : à **09 h 10 min 11 s**, `cargo clippy -p sim-viz` a échoué sur une
erreur de `sim-agents` (`E0615`, `self.n` au lieu de `self.n()`) qui n'existait
plus à 09 h 11 min 04 s. Aucune des deux minutes n'est de ce morceau ; l'échec
est consigné parce qu'il conditionne les preuves finales.

### E1 et E2 — le chiffre d'empaquetage, et le fait qu'il bouge

**Avant.** Les deux occurrences étaient incohérentes entre elles, et toutes deux
périmées :

```
$ grep -rn '445 293\|445 512' README.md CLAUDE.md          # 09 h 05
README.md:109:**1 445 512 octets** …
CLAUDE.md:245:  … NF-08 est tenue : **1 445 293 octets compressés** …
```

`CLAUDE.md:245` portait encore le chiffre que le tour 1 déclarait périmé — la
correction annoncée sur deux occurrences n'en avait touché qu'une. Et le chiffre
installé au `README` sortait d'une construction de 08 h 13, alors que `lib.rs` et
`scenario_b.rs` ont été édités à 08 h 25 et 08 h 26 : périmé d'une révision au
moment même où il était écrit.

**Changé.** Une construction unique, faite **après** les correctifs de code de ce
tour, et les deux occurrences alignées sur elle :

```
$ cargo build -p sim-viz --release --lib --target wasm32-unknown-unknown
                                            # 09:08:40 → Finished in 32.36s
$ wasm-bindgen --target web --no-typescript --out-dir web \
    $CARGO_TARGET_DIR/wasm32-unknown-unknown/release/sim_viz.wasm    # 09:09:21
$ printf "brut=%s gz9=%s\n" "$(stat -c%s web/sim_viz_bg.wasm)" \
                            "$(gzip -9 -c web/sim_viz_bg.wasm | wc -c)"
brut=3668599 gz9=1447267                                             # 09:09:29
$ stat -c '%n %y' web/sim_viz_bg.wasm
web/sim_viz_bg.wasm 2026-08-17 09:09:21.036829300 -0400
```

`README.md:107-131` porte désormais les deux chiffres, **la ligne de commande
exacte qui les produit**, l'heure de la construction dont ils sortent, et la
conséquence : « ce qui se cite d'ici est la ligne de commande, jamais le
nombre ». `CLAUDE.md:243-250` renvoie à cette commande au lieu de recopier une
mesure.

**Preuve que c'est parti.**

```
$ grep -rn '445 293\|445 512\|663 250\|663 058' README.md docs/*.md CLAUDE.md
(aucune sortie)                                                      # 09 h 13
$ grep -rn '447 267\|668 599' README.md CLAUDE.md
README.md:109:**1 447 267 octets** — 1,380 Mio, ou 1,45 Mo en unités SI …
README.md:110:8 Mo (NF-08), sur **3 668 599 octets bruts**. …
CLAUDE.md:245:  … NF-08 est tenue : **1 447 267 octets compressés** — 1,380 Mio, ou
CLAUDE.md:246:  1,45 Mo en unités SI — sur 3 668 599 octets bruts, contre une cible de 8 Mo.
```

**Ce que ce correctif ne fait pas, et le dit.** Il ne stabilise pas le chiffre. Le
module a été construit à 09 h 09, et les quatre autres agents écrivaient encore —
`sim-agents` a changé au moins deux fois entre 09 h 08 et 09 h 11, sous la mesure.
**La mesure finale de NF-08 reste à refaire quand les crates auront cessé de
bouger**, par les deux lignes du `README`. Ce qui est acquis n'est pas
`1 447 267` : c'est que les deux occurrences sortent de la **même** construction,
datée, et qu'elles portent la commande qui les refait.

### E3 — les numéros de ligne désignent maintenant le code livré

**Avant.** `docs/SPEC.md:703-705`, `SPEC.md:666`, `scenario_b.rs:706` et `:1294`,
`docs/README.md:144` désignaient l'état trouvé. Un lecteur de la section « ce qui
a été vérifié et tenait » atterrissait dans la table de nomenclature.

**Changé.** Tous les renvois du tour 1 ont été repris, selon deux règles :

- un renvoi qui désigne du code ou du texte **encore présent** porte le numéro du
  **fichier livré**, mesuré à 09 h 13 ;
- un renvoi qui désigne une ligne **supprimée ou remplacée** garde son numéro et
  porte la mention « à l'état trouvé », suivie de l'emplacement livré — la preuve
  d'un défaut est le texte qu'on a trouvé, et le renuméroter le ferait
  disparaître.

Notamment : table `| 1 |` → `lib.rs:931` ; `| 5 |` → `lib.rs:854` ·
`scenario_b.rs:744,1332` ; `| 8 |` → `README.md:108-111` ; `| 9 |` →
`README.md:289` ; `| 13 |` → `docs/SPEC.md:644-651` ; `| 14 |` → `:682` ;
`| 17 |` → `docs/README.md:145` ; et, dans « vérifié et tenait »,
`scenario_b.rs:578-604`, `:1244-1336`, `:1249`, `docs/SPEC.md:681` et `:719-721`,
`lib.rs:28`, `scenario_a.rs:88`.

**Ce que ce correctif ne fait pas.** Les renvois qui pointent dans `sim-core`,
`sim-milieu` et `sim-agents` — `arbitrage.rs:167`, `stigmergie.rs:377`, `:620`,
`:1079`, `scenario.rs:166-174`, `:431-432`, `journal.rs:633-636`, `glossaire.rs`
— **n'ont pas été repris** : ces trois crates sont éditées par d'autres agents à
cet instant même, et un numéro relevé ici serait périmé avant d'être lu. Ils
restent horodatés à leur mesure du tour 1. C'est la règle de NF-08 appliquée aux
renvois : quand un repère bouge, on écrit d'où il vient.

### E4 et E5 — les renvois `§8.3` et `§5.1` dans les commentaires publiés

**Avant.** Le tour 1 avait restreint son propre périmètre aux chaînes affichées.
`CLAUDE.md` ne pose pas cette restriction, et `cargo doc --workspace --no-deps`
publie les commentaires :

```
$ grep -rn '§8\.3\|§5\.1' crates/sim-viz/src/ | grep -v 'du PRD\|du traité'
crates/sim-viz/src/lib.rs:4://! scénario** (§5.1). Il affiche ce que `sim-agents`…
crates/sim-viz/src/lib.rs:722:/// même titre que les scénarios (§5.1). Le filtre…
crates/sim-viz/src/lib.rs:827:/// §8.3 — ce que le produit ne mesure pas, affiché…
crates/sim-viz/src/scenario_a.rs:16://! …ne tranche aucun verdict (§5.1). L'abscisse…
crates/sim-viz/src/scenario_b.rs:20://!   vue (§5.1).
```

Cinq renvois nus, dont celui du rustdoc de `limites()` — la fonction même dont le
tour 1 avait qualifié la chaîne affichée seize lignes plus bas. Les deux sections
se lisent des deux côtés : au traité, §5.1 est « Mécanismes de consensus »
(`Traité.md:1140`) et §8.3 « Buts incompatibles » (`:1702`) ; au PRD, §5.1 est
« Vue d'ensemble » (`docs/PRD.md:615`) et §8.3 « Ce que le produit ne mesure
pas » (`:1627`).

**Changé.** Les cinq qualifiés. Le rustdoc de `limites()` (`lib.rs:834-838`)
porte en plus la raison, pour que la règle ne se reperde pas :

> `/// §8.3 **du PRD** — ce que le produit ne mesure pas, affiché en permanence.`
> `///`
> `/// Le §8.3 **du traité** est « Buts incompatibles » (ch. 8) : le renvoi se`
> `/// lit des deux côtés et se qualifie donc partout, y compris dans ce`
> `/// commentaire, que cargo doc --workspace --no-deps publie.`

**Preuve que c'est parti** — la règle appliquée à **toute** la crate, commentaires
compris :

```
$ grep -rn '§8\.3\|§5\.1' crates/sim-viz/src/ | grep -v 'du PRD\|du traité'
(aucune sortie, exit=1)                                              # 09 h 13
```

**Balayage des autres renvois, pour ne pas refaire l'erreur de périmètre.** Les
treize formes de la crate ont été triées :

```
$ grep -rhoE '§[0-9]+(\.[0-9]+)?' crates/sim-viz/src/ | sort | uniq -c | sort -rn
6 §5.1  5 §5  5 §3  4 §8.3  2 §7  2 §4  2 §2  2 §1.2  2 §1.1  2 §1  1 §6  1 §4.1  1 §1.3
```

`§1` à `§6` **nus** sont les numéros de section **de l'écran du scénario B**
(« le bouton nominal du §5 », « la figure du §3 ») : aucune lecture documentaire
n'est possible. `§7` porte déjà « PRD » (`scenario_a.rs:59` et `:62`). `§1.1`,
`§1.2`, `§1.3` et `§4.1` ne sont **pas** ambigus : le PRD n'a aucune sous-section
de ce numéro — son §1 « Contexte » (`docs/PRD.md:290`) n'en a pas, et son §4
« Principes directeurs » (`:461-612`) numérote les siennes `PD1`…`PD14`. Le seul
couple ambigu de la crate était donc `§5.1` / `§8.3`, et il est traité.

### E6 — « zéro définition de scénario » était faux

**Avant.** `docs/SPEC.md:681`, dont la seule exception nommée était les plages de
curseur :

> **Zéro** définition de scénario : les paramètres et les critères d'acceptation
> viennent de `sim-agents`. **Les plages de curseur, elles, sont écrites ici** …

```
$ sed -n '104,112p' crates/sim-viz/src/scenario_a.rs        # état trouvé
n: 64, p: 8, l99_ms: 20.0, aller_simple_ms: 2.0, degre_depot: 3, taux_omission: 0.01
$ sed -n '152,157p' crates/sim-viz/src/scenario_b.rs        # état trouvé
params: Params { n: 16, ..Params::scenario_b() }, budget: 150_000, graine: 1
$ grep -rn '150_000' crates/sim-agents/src/                 # 09 h 12
(aucune sortie)
```

Neuf valeurs, aucune lue dans `sim-agents`.

**Une précision qui change la rédaction du correctif.** Le jugement écrit que ces
valeurs « ne viennent d'aucun `sim-agents` », ce qui est exact, mais elles ne
sont pas pour autant sans provenance : ce sont **les défauts des tableaux du §7
du PRD** — `docs/PRD.md:1095-1100` pour A (n 64, p 8, ℓ₉₉ 20 ms, aller simple
2 ms, taux d'omission 1 %, d 3) et `:1132` et `:1134` pour B (n 16, budget
150 000). La graine, elle, ne figure dans aucun tableau. Le document devait donc
dire non pas « la vue invente », mais « la vue **transcrit** le PRD faute
d'accesseur, et rien ne tient la transcription en accord » — ce qui est le défaut
réel, et exactement celui de `SOURCE_BORNES`.

**Changé.** Trois documents, parce que trois documents portaient l'énoncé — c'est
la faute d'E1 qu'il fallait ne pas refaire :

- `docs/SPEC.md:681` — « à **deux** exceptions nommées », les neuf valeurs
  détaillées vue par vue, leur provenance PRD §7, et le fait que rien ne les
  tient ;
- `docs/architecture.md:63` et `CLAUDE.md:116` — la même exception, en une ligne ;
- `crates/sim-viz/src/scenario_b.rs:34-47` — le `//!` disait « une exception, et
  une seule : le `n` d'ouverture », alors que `VueB::default` en pose trois. Il en
  déclare trois, plus la quatrième d'E7 ; le commentaire du point de décision
  (`:153-160`) suit ;
- `crates/sim-viz/src/scenario_a.rs:103-109` — `VueA::default` n'avait aucun
  rustdoc ; il en a un qui nomme la transcription et son absence de garde-fou.

**Preuve.**

```
$ grep -rn 'éro\*\* définition' docs/SPEC.md docs/architecture.md CLAUDE.md \
    | grep -c 'exception'
3
```

**La décision de conception qui reste à trancher, et qui n'est pas un oubli.**
Deux remèdes se défendaient : corriger le document, ou **remonter les neuf
valeurs dans `sim-agents`** — un défaut nommé pour `VueB` et un constructeur de
défaut pour `scenario_a` —, de sorte que la phrase « zéro définition de
scénario » redevienne vraie au lieu d'être amendée. Le second est **hors du
périmètre de ce morceau** : `sim-agents` appartient à un autre agent, et l'API de
`sim_agents::scenario_a` — fonction nue à sept paramètres — devrait changer. Il
est consigné ici comme **décision de conception ouverte**, à trancher à la passe
de consolidation. Tant qu'elle ne l'est pas, le contrat de la crate porte une
exception au lieu d'un absolu : c'est vrai, et plus faible.

### E7 — « zéro logique de simulation » était contredit par le code

**Avant.** `docs/SPEC.md:680` écrivait l'absolu, et
`crates/sim-viz/src/scenario_b.rs:1340-1353` le contredisait dans son propre
rustdoc :

> **Hypothèse réimplantée dans la vue, et nommée ici : le budget d'événements est
> découpé en tranches de largeur égale.**

Déclarée dans le code, absente des trois documents, et **absente de l'écran**.
PD6 tranche : ce qui est absent s'affiche au même rang que ce qui est présent, et
la réciproque vaut — ce que la vue tient et qu'elle affirme ailleurs ne pas tenir
doit s'afficher au même rang aussi.

**Changé — le document *et* la déclaration.**

- `docs/SPEC.md:680`, `docs/architecture.md:63`, `CLAUDE.md:116` : l'exception est
  nommée avec ce qu'elle coûte — `sim-agents` ne rend pas la tranche de bascule,
  donc un découpage non uniforme ferait mentir l'étiquette « avant / après la
  bascule » sans qu'aucune erreur de compilation ne le signale ;
- `crates/sim-viz/src/lib.rs:944-979` : une **sixième section** dans l'onglet
  « Limites », « Ce que cette interface décide à la place de « sim-agents » »,
  trois énoncés — l'hypothèse de découpage, les trois valeurs d'ouverture du
  scénario B, les six du scénario A. Son compte affiché est calculé
  (`lignes.len()`, `lib.rs:965`), jamais écrit ;
- `docs/architecture.md:237-244` : l'onglet tire « trois de ses **six** listes »
  des `hors_perimetre` et **écrit les trois autres**, vingt-deux énoncés en dur ;
- `crates/sim-viz/src/lib.rs:3-10` : le `//!` de la crate ne dit plus « aucune
  logique de simulation » tout court — il renvoie aux exceptions et à l'endroit
  où elles s'affichent.

**Preuve.**

```
$ grep -n 'Ce que cette interface décide' crates/sim-viz/src/lib.rs
950:                    "Ce que cette interface décide à la place de « sim-agents »",
$ grep -rn 'éro\*\* logique' docs/SPEC.md docs/architecture.md CLAUDE.md \
    | grep -c 'exception'
3
```

**Ce que ce correctif ne fait pas.** Aucun test ne tient la nouvelle liste : elle
est en dur, comme les deux autres, et `docs/architecture.md:238` le dit
maintenant. Un test qui comparerait les trois valeurs annoncées à
`VueB::default()` serait tautologique — il vérifierait qu'une constante vaut
elle-même. Le seul garde-fou réel serait l'accesseur dans `sim-agents`,
c'est-à-dire la décision laissée ouverte en E6.

### Ce qui n'a pas été corrigé, et pourquoi

Rien du jugement : les sept entrées E1 à E7 sont traitées. Les trois anomalies du
tour 1 restées ouvertes — `clippy.toml`, `docs/README.md:145`, les pages du §1.2
dans les trois autres crates — le restent pour les motifs déjà écrits, qui n'ont
pas changé : hors périmètre attribué, ou morceau d'un autre agent.

### Preuves finales du tour 2

```
$ date                                            2026-08-17 09:11:04
$ cargo clippy -p sim-viz --all-targets --release
    Checking sim-viz v0.1.0 (…/crates/sim-viz)
    Finished `release` profile [optimized] target(s) in 2.60s
clippy exit=0

$ date                                            2026-08-17 09:11:17
$ cargo doc -p sim-viz --no-deps
 Documenting sim-viz v0.1.0 (…/crates/sim-viz)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 11.53s
   Generated …/doc/sim_viz/index.html and 1 other file
doc exit=0

$ cargo test -p sim-viz --release --lib
test scenario_b::tests::la_provenance_des_bornes_suit_encore_sim_agents ... ok
test scenario_a::tests::le_vainqueur_se_lit_encore_dans_la_phrase_de_verdict ... ok
test scenario_b::tests::la_ligne_de_differences_nomme_ce_que_le_prereglage_deplace ... ok
test scenario_b::tests::la_tranche_se_situe_de_part_et_dautre_de_la_bascule ... ok
test scenario_b::tests::chaque_prereglage_dit_ou_regarder ... ok
test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
test exit=0
```

Aucun avertissement sur les trois commandes. Zéro test affaibli, retiré ou ajouté
à ce tour. Aucun fichier de `sim-core`, `sim-milieu` ou `sim-agents` touché ; ni
`docs/PRD.md`, ni `docs/decisions.md`.

### Ce que le tour 2 ne démontre pas

- **Rien sur le rendu, toujours.** La sixième section de l'onglet « Limites » n'a
  pas été vue à l'écran, pas plus que les correctifs du tour 1. Elle est établie
  par le code, par `cargo test` et par la règle qu'elle sert, pas par une capture.
- **Rien sur NF-08 après 09 h 09.** Voir E1-E2 : la mesure est à refaire.
- **Rien sur la durée de justesse des neuf valeurs d'ouverture.** Le correctif
  d'E6 établit qu'elles **coïncident** avec les tableaux du §7 du PRD au 17 août
  2026 ; il n'établit pas qu'elles y resteront, puisque rien ne les tient.
