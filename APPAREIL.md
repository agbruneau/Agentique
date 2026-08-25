# L'appareil du dépôt — refaire, ou vérifier

*Ce fichier est l'annexe technique du [`README.md`](README.md), sortie de la page parce qu'elle ne
sert à personne qui vient **lire** les huit documents : tout y est déjà rendu en PDF. Elle sert à les
**refaire**, ou à vérifier qu'ils tiennent encore.* ✎ *Ce fichier s'est dit « non versionné », comme
le `README.md` : c'était faux dans les deux cas — `git ls-files` les rend tous les deux.*

## Les onze contrôles

**Onze contrôles, onze à 0.** *Trois sortaient 1 jusqu'au 21 août 2026 ; la note ⚠ de leur ligne
ci-dessous dit ce que chacun avait trouvé et ce qui a été fait.* Rien
n'est câblé en intégration continue — pas de `.github/` —, et chacun se lance seul, depuis le dossier
indiqué. *Relevé du 21 août 2026 ; toutes les commandes ci-dessous ont été rejouées pour ce relevé,
sauf mention contraire.*

**a. « Ce document tient-il ? » — un contrôle par livrable**

| Commande | Depuis | Verdict |
|---|---|---|
| `python Python/check-veille.py` | `4 - Veille/` | ☑ **0** — 94 sections, 342 entrées, appariement cité ↔ défini clos dans les deux sens |
| `python Python/check-revue.py` | `4 - Veille/` | ☑ **0** — 192 définies, 8 tableaux, 12 attestées / 32 auto-déclarées / 145 sans revue sur 189 arXiv |
| `python Python/check-traite.py` | `3 - Traité/` | ☑ **0** — 143 pages, recomptées à **deux sources du PDF qui doivent concorder** ; 123 notices citées nommément ; 72 110 mots |
| `python PRD/check-compendium.py` | `2 - Compendium/` | ☑ **0** — les 50 pièces tiennent (P1-P8), 3 rapports déclaratifs |
| `python PRD/check-toc.py` · `PRD/check-sieges.py` | `2 - Compendium/` | ☑ **0** — C1-C15 ; 26 sièges sur 50 pièces (S1-S5) |
| `python "4 - Veille/Python/check-resume.py" <fichier.pdf>` | racine | ☑ **0 sur les neuf rendus livrés**, essayés un par un pour ce relevé — il mesure la **géométrie** de la page de titre : le gabarit compose le résumé dans un bloc qui ne se scinde pas, donc un résumé trop long se fait rogner sous la marge basse sans que Pandoc sorte autre chose que 0. ☑ *Il est désormais **enchaîné** aux chaînes de rendu de `4 - Veille/` et `5 - Recension/`, qui échouent s'il échoue* |
| `bash PRD/decompte.sh --verifier` | `2 - Compendium/` | ☑ **0** — les quatre points d'ancrage tenus : Vol. I 225 258 / 233 257, Vol. II **93 239**, Vol. III 160 890. ⚠ *L'ancre du Vol. II a été **redatée** de 93 242 à 93 239 le 21 août 2026 : trois jetons étaient tombés du corps le 8 août avec le renommage du volume, et le script avait raison de le dire — le motif est en tête de son bloc d'attendus* |
| ⚠ *Le Vol. I n'a aucun contrôle propre.* | | |

**b. « Les contrôles tiennent-ils ? » — validation par mutation**

Chaque harnais copie le corpus dans un dossier temporaire, y injecte des fautes connues et exige que
le contrôle les attrape. À lancer après toute retouche du contrôle correspondant.

| Commande | Depuis | Verdict |
|---|---|---|
| `python PRD/check-sieges-mutations.py` | `2 - Compendium/` | ☑ **0** — attrape les **108** mutations |
| `python PRD/check-toc-mutations.py` | `2 - Compendium/` | ☑ **0** — **23 sur 23**. ⚠ *M14 échappait à C14 jusqu'au 21 août 2026, et le harnais ne pouvait pas le dire : son ancre visait une entrée d'**historique** de la rangée `\| Source \|` du conspectus, quand C14 ne lit que la version de tête. Réancrée sur le préfixe de rangée — une ancre qui vise ce que le contrôle ne regarde pas cesse de tester sans que rien le signale* |
| `python PRD/check-compendium-mutations.py` | `2 - Compendium/` | ☑ **0** — ligne de base tenue, **17 mutations sur 17**. ⚠ *Il s'arrêtait en `AssertionError` à M6 jusqu'au 21 août 2026 — ancre littérale « \| 11 000 \| 10 724 \| » périmée quand le ch. 1 s'est re-mesuré à 10 859 mots —, et **les huit mutations suivantes ne tournaient pas**. Réancrée sur la **colonne** du registre, non sur la valeur qui l'occupe* |

**c. « La chaîne se refait-elle ? » — graver, assembler, composer**

Ordre réel de fabrication : **graver les figures → assembler la source → composer le PDF.**
☑ **Les trois étapes ont été rejouées le 21 août 2026, et les neuf PDF livrés se refont désormais
tous par un script versionné** — ils n'étaient que quatre à le pouvoir.

| Commande | Depuis | Verdict |
|---|---|---|
| `python figures/contenu.py` | `3 - Traité/` | ☑ **19 SVG du traité regravés, identiques à l'octet** (`dessine.py` n'est pas un point d'entrée : il porte les primitives). ⚠ *Se lançait depuis la **racine du dépôt** jusqu'au 21 août 2026, les planches y étant restées quand le traité est entré — elles sont chez lui depuis* |
| `python figures/dessine.py` | `5 - Recension/` | ☑ **5 SVG regravés, identiques à l'octet** |
| `python figures/genere.py [--verifier]` | `2 - Compendium/` | ☑ **0** — **115 figures regravées** sur 49 pièces, identiques à l'octet ; insertion idempotente, aucune pièce touchée. ☑ *Depuis le 21 août 2026 il annonce **118** et non 115 : le registre `ANTERIEURES` compte les **trois figures antérieures au programme** et les gèle à l'empreinte SHA-256. Elles ne se regravent toujours pas — aucune primitive ne les rend —, mais elles ne peuvent plus bouger sans que le contrôle sorte 1* |
| `python build/assemble.py` | `1 - Collection/2 -…/` et `/3 -…/` | ☑ **reproduit le `Monographie.md` livré à l'octet près**, sur les deux volumes |
| `python build/assemble.py <sortie.md>` | `2 - Compendium/` | ☑ 50 chapitres, 5 livres, 2 annexes → 31 028 l. / 2,72 Mo |
| `bash build/build-pdf.sh` | Vol. I, II, III, Compendium | **Non rejoué ici.** Prérequis déclarés dans les scripts : Pandoc ≥ 3.1.7, Typst ≥ 0.12, `python3` + `pypdf`, polices nommées ; Node ≥ 18 + `mermaid-cli` pour les 28 diagrammes du Vol. I |
| `bash build/build-pdf.sh` | `3 - Traité/` | ☑ **143 pages**, pagination inchangée. ⚠ *Chaîne **écrite** le 21 août 2026 : sa commande n'était nulle part au dépôt, et il a fallu la reconstituer. Elle se lance de ce dossier depuis que les figures y sont* |
| `bash build/build-pdf.sh [veille\|revue]` | `4 - Veille/` | ☑ **144 et 59 pages**, pagination inchangée après le changement de titre. *Inscrit au dépôt les deux commandes qui n'y vivaient qu'en prose ; enchaîne `check-resume.py`* |
| `bash build/build-pdf.sh [etat\|planche]` | `5 - Recension/` | ☑ **185 et 7 pages**, pagination inchangée. ⚠ *Il ne couvre PAS les deux `.html`, et le dit : leur commande prend `--css <feuille>`, et aucune feuille de style n'est versionnée* |
| `cargo test --workspace --release` · `cargo clippy --workspace --all-targets --release` · `cargo doc --workspace --no-deps` | `3 - Traité/` | ☑ **0 aux trois** — **467 tests, 0 échec, 0 ignoré**, aucun `#[ignore]` au code ; clippy 0 sur les six membres et toutes les cibles ; rustdoc 0. *Ce sont les trois commandes d'avant-commit de `docs/DEVELOPPEMENT.md`, et la troisième existe parce que les deux premières sont restées vertes pendant que rustdoc sortait 101.* ⚠⚠ *L'ensemble sortait **101 à l'instant** jusqu'au 21 août 2026 : deux membres du workspace manquaient au disque* |
| `bancs/dt1-flottant/banc.mjs` · `bancs/parite-wasm/banc.mjs` | `3 - Traité/` | ☑ **0 aux deux**, sous Node 24. **DT1** : NF-02 tenue sur 8 groupes à parité exigée, 10⁶ itérations chacun — *les 6 divergences de la bibliothèque de plateforme sont le **résultat** du banc, non une régression, et `mul_add` coïncide sur cette machine*. **EX-V12** : 6 cas identiques natif/WASM |
| `cargo run -p sim-agents --example …` (×4) · `--bin campagne` | `3 - Traité/` | ☑ **0 aux cinq**. *`banc_nf05` affiche ✗ NF-05 et sort 0 : la cible de 10³ s simulées/s-cœur n'est pas atteinte — c'est un écart consigné au registre, pas un échec de banc.* `diagnostic_conformite` reproduit le constat qui a réfuté le premier point du critère de sortie de la phase 6 |
| `wasm-bindgen --target web` sur `sim_viz.wasm` | `3 - Traité/` | ☑ **reproduit `web/sim_viz.js` et `web/sim_viz_bg.wasm` à l'octet** — 68 213 et 3 669 337 octets, et 1 447 624 en `gzip -9`. *Les deux chiffres du `README.md` du dossier, datés du 17 août 2026, sont donc encore valides ; ils ne l'étaient que jusqu'à la prochaine édition de `crates/sim-viz/`* |

⚠ **Points d'entrée qui n'ont pas été rejoués** : `2 - Compendium/build/assemble-bibliographie.py`,
`build/echantillon.py` (maquette Springer, avec `echantillon.template` et `springer.template`), les
trois `build/inject-pagination.py` des volumes du corpus, et les quatre `build-pdf.sh` des Vol. I, II,
III et du Compendium.

**d. « Les renvois tiennent-ils ? » — mesuré ici, non tenu là-bas**

⚠ **1 879 renvois relatifs résolus dans les 227 `.md` du dépôt, et DEUX ROMPUS**, au 22 août 2026 —
*ils étaient 243 à viser le vide avant la passe du 21, zéro après elle, et deux le lendemain.*
⚠⚠ **Les deux morts avaient la même cause, une suppression du 22 août** : un journal de boucle est
sorti de l'index, et deux `README.md` de `3 - Traité/` le citaient encore en lien — celui du dossier
en tête d'une rangée de tableau, celui de `docs/` au corps, où il l'opposait au journal de la revue
par les pairs. ☑ **La décision d'auteur que ce relevé laissait ouverte est prise le 25 août 2026** :
les deux renvois sont retirés, la pièce n'est pas restaurée, et son nom est effacé du dépôt entier —
*ce qu'elle a produit de durable est au §0.2 du PRD du traité et à son registre, non dans le journal — le dossier de banc qui en portait les dix rapports est lui-même sorti du dépôt le 25 août 2026.* ⚠ **Aucun contrôle du dépôt ne résout un lien markdown** : c'est
une mesure faite pour ce relevé, pas une garantie que le dépôt tient. La commande est une résolution
de chaque cible relative contre le système de fichiers, blocs et *spans* de code exclus — un
`` `[…](cible)` `` cité en prose n'est pas un lien.

## D'où viennent les chiffres du `README.md`

Relevés le **21 août 2026** sur l'arbre de travail, par ces commandes et par elles seules — ⚠ *trois
exceptés, redatés du **22 août 2026** et marqués comme tels au fil du texte : les titres et auteurs,
le décompte d'octets avec deux de ses cardinaux, et les renvois du point d ci-dessus.*

- **Pages** — `pypdf`, `len(PdfReader(f).pages)` sur les 10 PDF versionnés. Aucun nombre de pages
  n'est repris d'un autre `README.md`.
- **Titres et auteurs** — champs `/Title` et `/Author` des PDF, et en-têtes YAML des sources.
  *Les six PDF de tête portent six `/Title` distincts depuis l'échange titre ↔ sous-titre du
  21 août 2026 ; ils n'en portaient que quatre.* ⚠ **Le champ ne vaut pas la source, et l'écart se
  mesure des deux côtés — relevé du 22 août 2026.** *(a)* `/Title` : le PDF d'état de l'art lit
  `État de lart en services financiers`, **apostrophe tombée à la composition Typst du 21 août**,
  quand sa source YAML l'écrit bien. *(b)* `/Author` : **le nom est sur les neuf, la mention
  « M.Sc. IT » sur six seulement** — les Vol. I, II et III portent `André-Guy Bruneau` seul. *Citer
  l'en-tête YAML pour le champ du PDF, ou l'inverse, est le piège de cette ligne.*
- **Lignes, octets, cardinaux de fichiers** — `wc -l` / `wc -c` / `git ls-files`. *Les tailles sont
  décimales : 1 Mo = 10⁶ octets.* ⚠⚠ **Le décompte d'octets s'est périmé DEUX FOIS le 22 août
  2026** : remesuré à 75 116 966 en début de passe, il est retombé le jour même avec la suppression
  d'un journal de boucle de `3 - Traité/`, et il vaut **75 096 625** au dernier relevé — *trois passes
  concordantes, `cat | wc -c` deux fois et la somme des `stat` une fois.* ⚠ **Deux cardinaux de la
  même ligne sont tombés avec la pièce** — le total, **575 → 574**, et les `.md`, **228 → 227** ;
  *les quinze autres extensions tiennent tels quels.* *Il était déjà faux avant, et sa fausseté a
  survécu à deux causes distinctes : la suppression puis la restauration d'`APPAREIL.md` — 11 306
  octets qui sortent et rentrent —, et les éditions du 22 août à `3 - Traité/README.md`,
  `CLAUDE.md` et `docs/DEVELOPPEMENT.md`. **Ce nombre se périme à chaque commit**, y compris celui
  qui l'écrit : il est auto-référentiel, le `README.md` étant lui-même compté. Le remesurer par la
  ligne ci-dessous, et ne le corriger qu'en gardant le même nombre de chiffres — sans quoi
  l'édition déplace le total qu'elle prétend fixer.*

  ```bash
  git ls-files -z | xargs -0 cat | wc -c
  ```

  ⚠⚠ **Un relevé unique ne se vérifie pas, et cette commande ne signale rien quand il est faux.**
  Le 22 août 2026, un relevé pris juste après cinq éditions a rendu **75 116 696** — *270 octets de
  moins* que les trois passes concordantes prises ensuite, et que la somme des tailles fichier par
  fichier, qui donnent toutes **75 116 966**. La commande sort 0 dans les deux cas et les deux
  nombres sont plausibles : rien ne distingue le bon du mauvais sans une seconde mesure.
  ⚠ **La cause de ces 270 octets n'est pas établie**, et elle n'a pas été cherchée — *une piste
  OneDrive a été écrite ici puis retirée le jour même, faute de mesure : le dossier est synchronisé,
  ce qui suffit à casser l'édition de liens dans `target/`
  ([`docs/DEVELOPPEMENT.md`](<3 - Traité/docs/DEVELOPPEMENT.md>)), mais rien ne montre que ce soit
  ce qui s'est passé ici.* Ce qui est établi est la règle, pas le mécanisme : **mesurer par deux
  passes qui doivent concorder**, la seconde méthode servant de contrôle croisé puisqu'elle n'ouvre
  pas les fichiers en flux.

  ```bash
  git ls-files -z | xargs -0 stat -c%s | awk '{s+=$1} END {print s}'
  ```

  ☑ *Ce que la règle a effectivement attrapé, le même jour* : un écart de **23 538** octets entre
  deux relevés, qui n'était pas une erreur de mesure du tout — un journal de boucle de
  `3 - Traité/`, 24 566 octets au disque, avait été supprimé par un commit entre les deux. Une mesure qui ne
  concorde pas est d'abord une question sur l'arbre, pas sur la commande.
- **Historique** — `git log --format='%an'`, `git log --merges` (quatre fusions, et
  `git log --all --grep='#4'` ne rend rien), `git tag`, `git branch -r`, et
  `git log --all --diff-filter=A --name-only` pour ce que l'arbre ne porte plus. *C'est cette
  dernière commande qui a rendu les 55 fichiers restaurés le 21 août 2026.*
- **Références, sections, tableaux, mots** — sortie des contrôles du dépôt eux-mêmes
  (`check-veille.py`, `check-revue.py`, `check-traite.py`, `decompte.sh`), rejoués ici ; les 312
  notices de l'état de l'art recomptées à part sur sa bibliographie.
- **Reproductibilité des chaînes** — assembleurs et graveurs relancés sur une copie de sauvegarde,
  puis comparés fichier à fichier avec `cmp` ; l'arbre a été remis en état après chaque essai. *Les
  cinq PDF nouvellement scriptés ont été composés vers une sortie d'essai (`OUT_PDF=`, `SUFFIXE=`)
  avant de l'être en place.*
- **Renvois morts** — résolution de chaque cible relative de **tous les `.md` versionnés**, et non
  des seuls `README.md` : c'est ce qui a fait passer le compte de 35 à 243.
- **Diagrammes Mermaid** — `grep -cFx` sur la ligne d'ouverture de bloc `mermaid` : 28 dans le
  Vol. I, 64 dans tout le dépôt.
