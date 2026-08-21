# M5 · `sim-viz` + concordance documentaire — jugement du critique, tour 1

Agent en contexte neuf. Comparaison à l'aveugle contre `bancs/dt1-flottant/VERDICT.md`,
partie 1 écrite avant ouverture du dépôt. Ordre inversé par rapport aux tours M1 et M2 :
ici le rapport d'audit était le document **B**.

## Verdict : **B** — le rapport d'audit

> B fait porter à chaque affirmation la commande qui la produit et sa sortie, avec
> `fichier:ligne`, horodatage, et la distinction explicite entre mesure et déduction.
> A raisonne juste et tire bien ses conséquences, mais il livre un tableau de verdicts
> là où B livre des sorties : le lecteur de A doit relancer le banc entier pour vérifier
> quoi que ce soit.

## L'écart retenu — sur le perdant (le verdict DT1)

> L'affirmation la plus lourde du document — celle qui justifie la septième interdiction —
> est la seule qui ne s'appuie sur aucune donnée montrée. […] Le document qui exige
> ailleurs qu'une grandeur porte sa provenance imprime ici sa déduction dans la même
> typographie que ses mesures.

Troisième critique consécutif à désigner le même défaut du verdict DT1, sans concertation
possible : les trois ont couru en parallèle, en contextes séparés.

## Ce qui se reproduit exactement

**447 = 404 unitaires + 43 d'intégration**, répartis **247 / 91 / 61 / 5** — chiffre pour
chiffre. `gzip -9 -c web/sim_viz_bg.wasm | wc -c` → **1 445 512**, `stat -c%s` →
**3 663 250**, à l'octet près. `pymupdf` → **143 pages** ; §1.2 ouvre p. 12, l'énoncé des
bornes p. 16, « Buts incompatibles » p. 124, le chapitre 8 p. 117. Sur `Traité.md` :
`h2=11 h3=24`, 22 tableaux, 10 algorithmes, 18 légendes de figure, **123 notices**,
3ᵉ édition du 15 août. 31 modules, 32 termes de glossaire, 14 DT, 19 SVG, 19 énoncés en
dur, 16 `EX-V*`, 15 littéraux de plage. Les **17 filtres** des 13 lignes du `README`
rendent tous exactement les comptes annoncés. Clippy et rustdoc à 0 sur `sim-viz`. Aucun
lien relatif cassé dans les six documents.

## Affirmations prises en défaut

### E1 — une correction déclarée faite sur deux occurrences n'en a touché qu'une

L'anomalie 8 est portée « corrigée : oui » sur *les deux chiffres*.

```
CLAUDE.md:245:  est fait et NF-08 est tenue : **1 445 293 octets compressés**
```

`README.md:109` est passé à 1 445 512 ; **`CLAUDE.md:245` porte encore le chiffre que le
rapport lui-même déclare périmé**, dans un des six documents de son mandat, un fichier
qu'il a édité trois fois par ailleurs.

### E2 — le chiffre installé est déjà périmé, par les propres correctifs de l'auteur

Reconstruit hors du dépôt (`cargo build -p sim-viz --release --lib --target
wasm32-unknown-unknown` puis `wasm-bindgen`) : **brut = 3 666 603, gz9 = 1 446 247**,
contre 3 663 250 / 1 445 512 au `README`. Motif : la construction est de 08 h 13, `lib.rs`
a été édité à 08 h 25 et `scenario_b.rs` à 08 h 26. C'est exactement le défaut diagnostiqué
— « l'empaquetage était vieux de deux révisions de l'interface » — **reproduit à une
révision**.

### E3 — les numéros de ligne sont ceux de l'état trouvé, pas de l'état laissé

Cohérent partout, mais non signalé : `docs/SPEC.md:703-705` sont aujourd'hui **719-721**,
`SPEC.md:666` est **682**, `scenario_b.rs:706` et `:1294` sont **735** et **1323**,
`docs/README.md:144` est **145**. Un lecteur qui suit les renvois de la section « vérifié
et tenait » atterrit dans la table de nomenclature. *(Vaut pour les cinq rapports.)*

### Dérive concurrente, qui n'est pas une faute de l'auteur

`sim_agents::hors_perimetre()` = **20** entrées et `sim_milieu::hors_perimetre()` = **13**
aujourd'hui, contre 19 / 9 à `HEAD` — les valeurs du rapport. Les autres agents écrivaient
jusqu'à 08 h 53, après la dernière mesure de 08 h 34. Le rapport l'avait annoncé en donnant
la ligne de commande plutôt qu'un compte gravé. Le compte de tests n'a pas bougé d'une unité.

## Ce que le bâtisseur n'a pas vu

### E4 — `sim-viz/src/lib.rs:827` : le renvoi §8.3 ambigu, dans le rustdoc de la fonction qu'il venait de corriger

`/// §8.3 — ce que le produit ne mesure pas`. Il a qualifié la chaîne **affichée** seize
lignes plus bas (`:843`) et laissé le renvoi ambigu dans le commentaire que
`cargo doc --workspace --no-deps` publie. `grep -n '^### 8.3' Traité.md` → « Buts
incompatibles ». Le rapport a lui-même restreint son périmètre à « chaînes affichées, pas
des commentaires » ; `CLAUDE.md` ne pose pas cette restriction.

### E5 — `§5.1` nu quatre fois contre deux fois qualifié, dans les mêmes fichiers

`lib.rs:4`, `lib.rs:722`, `scenario_b.rs:20`, `scenario_a.rs:16` portent `(§5.1)` nu,
tandis que `scenario_b.rs:31` et `:1323` disent « du PRD ». `grep -n '^### 5.1' Traité.md`
→ « Mécanismes de consensus » : dans un simulateur d'essaims, le renvoi se lit des deux
côtés au moins aussi facilement que §8.3. `scenario_b.rs:20` est **onze lignes au-dessus**
de celui qui a été qualifié.

### E6 — `docs/SPEC.md:681` : « zéro définition de scénario » est faux

La seule exception nommée est les plages de curseur. Or `scenario_b.rs:152-157` pose
`n: 16`, `budget: 150_000`, `graine: 1`, et `scenario_a.rs:104-112` pose **six** valeurs de
paramètre — `n: 64, p: 8, l99_ms: 20.0, aller_simple_ms: 2.0, degre_depot: 3,
taux_omission: 0.01` — qui ne viennent d'aucun `sim-agents` : `pub fn scenario_a`
(`sim-agents/src/scenario.rs:166-174`) est une fonction nue à sept paramètres sans
constructeur de défaut, et `grep -rn '150_000' crates/sim-agents/src/` ne rend rien.

Il a amendé la ligne **voisine** de la même table (`:682`) et laissé celle-ci.

### E7 — `docs/SPEC.md:680` : « zéro logique de simulation » est contredit par le code lui-même

`sim-viz/src/scenario_b.rs:1340-1353`, dont le rustdoc le déclare en propres termes :
« **Hypothèse réimplantée dans la vue, et nommée ici : le budget d'événements est découpé
en tranches de largeur égale.** » Déclarée dans le code, absente des trois documents qui
écrivent « zéro », et **absente de l'onglet « Limites »** — le même mensonge symétrique, à
l'autre bout de la même table, que celui qu'il a corrigé pour `SOURCE_BORNES`.

## Ce qui tient, vérifié ligne par ligne

NF-14 : `bornes_applicables()` n'a qu'un seul lecteur dans toute la crate
(`scenario_b.rs:569`), la branche `Err` (`:590-594`) n'imprime que le motif — aucune valeur,
aucun pointillé, aucun gris — et aucun second lecteur n'existe. F3 : `grep -rn "converg"`
ne rend que `lib.rs:22`. Les sept `.size(` passent tous par `THESE`, `TITRE_SECTION` ou
`MESURE`.
