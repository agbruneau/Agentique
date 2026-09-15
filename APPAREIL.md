# L'appareil du dépôt — refaire, ou vérifier

*Annexe technique du [`README.md`](README.md). Elle ne sert pas à lire le corpus — les documents
sont rendus en PDF —, mais à les refaire, ou à vérifier qu'ils tiennent encore : chaque point
d'entrée, le dossier d'où il se lance, et ce qu'il rend.*

**Relevé du 15 septembre 2026.** Chaque chiffre de cette page est la sortie d'une commande rejouée
ce jour-là, entre 8 h 43 et 9 h 20 (heure de l'Est), sur le poste de l'auteur : Windows 11,
Python 3.14.7, cargo et rustc 1.98.0, Typst 0.15.1, Pandoc 3.11, Node 24.19.0,
wasm-bindgen 0.2.127, pymupdf 1.28.2 ; `PYTHONUTF8=1` sauf mention ; `CARGO_TARGET_DIR` hors du
dépôt. **L'arbre rejoué** est le commit `e1b1b9e` plus les corrections non commitées que le
[plan d'exécution](<Plan%20d%27ex%C3%A9cution%20%E2%80%94%20%C3%A9valuation%20acad%C3%A9mique.md>)
y posait le même jour ; le [§ 9](#9-larbre-rejoué) dit lesquelles. Les graveurs et les assembleurs
ont tourné dans une copie de leur dossier, ramenée aux octets de l'index : rien n'a été écrit dans
l'arbre.

*La page précédente — relevés du 21 août au 5 septembre 2026 — se relit par
`git show e1b1b9e:APPAREIL.md`, et ses chiffres y restent à leur date. Le
[§ 7](#7-ce-que-ce-relevé-change-à-la-page-précédente) dit ce que ce relevé y change.*

## 1. Verdict d'ensemble

| Famille | Points d'entrée rejoués | Sortie 0 | Autre sortie, et pourquoi |
|---|---|---|---|
| Contrôles de document, renvois compris ([§ 3](#3-contrôles-de-document)) | 16 | 14 | `check-empaquetage.py` sort 1 sans `CARGO_TARGET_DIR` — « INDÉTERMINÉ », par construction — et 0 avec ; `check-resume.py` sort 0 sur les dix rendus qu'il sait lire, 1 sur l'article et sur le mémoire de 1997, où il est inapplicable ([§ 6](#6-alertes-que-la-mesure-porte-et-quaucun-contrôle-ne-bloque)) |
| Harnais de mutation ([§ 4](#4-validation-par-mutation)) | 6 | 6 | — |
| Fabrication : graveurs, assembleurs, composition ([§ 5](#5-fabrication-et-simulateur)) | 7 | 7 | — ; les cinq graveurs et assembleurs rendent des fichiers identiques à l'octet à l'index |
| Simulateur : cargo, bancs, exemples ([§ 5](#5-fabrication-et-simulateur)) | 11 | 11 | `banc_nf05` affiche ✗ NF-05 et sort 0 : écart consigné au registre du simulateur |

**Non rejoué** : les sept chaînes Pandoc → Typst des PDF livrés, `inject-pagination.py`, `echantillon.py` et les deux `.html` de `5 - Recension/`, nommés au
[§ 8](#8-ce-qui-na-pas-été-rejoué-le-15-septembre-2026).

## 2. Intégration continue

[![appareil](https://github.com/agbruneau/Agentique/actions/workflows/appareil.yml/badge.svg)](https://github.com/agbruneau/Agentique/actions/workflows/appareil.yml)

Le flux [`.github/workflows/appareil.yml`](.github/workflows/appareil.yml) rejoue l'appareil à
chaque poussée sur `main`, à chaque demande de tirage et à la demande, en trois tâches, chacune sur
`ubuntu-latest` et sur `windows-latest`. Chaque étape est une commande de cette page, lancée du même
dossier.

| Tâche | Ce qu'elle rejoue |
|---|---|
| Documents | les contrôles de document du § 3, sauf `check-empaquetage.py` et `check-renvois.py`, qui a sa tâche ; `check-resume.py` sur les dix rendus qu'il sait lire ; `genere.py --verifier` une seconde fois sans mode UTF-8, sous Windows ; les cinq harnais de mutation de document du § 4 ; puis, **dans l'arbre**, les cinq graveurs et assembleurs du § 5 avec `assemble-bibliographie.py` et — sous Linux seulement — `reporter-volumetrie.py` en mode écriture, suivis de deux gardes — `git status --porcelain` vide, aucun fichier en CRLF — ; et une garde qui refuse tout script portant ⚠ ou ☑ sans `sys.stdout.reconfigure` |
| Renvois | `Python/check-renvois.py` et son harnais |
| Simulateur | `cargo fmt --all --check`, `cargo clippy`, `cargo test`, avec un plancher de 470 tests |

**Ce que le flux ne rejoue pas encore** :

- les sept `build/build-pdf.sh` — la chaîne Pandoc → Typst des PDF livrés, dont les polices sont
  celles du poste de l'auteur ;
- la parité de `Traité.pdf`, pour la même raison : sans Pandoc dans le `PATH`, `check-traite.py` la
  déclare « NON MESURÉ » ;
- la construction WASM et `check-empaquetage.py` ;
- les deux bancs Node, les quatre exemples et `campagne` ;
- `cargo doc` ;
- l'assembleur du compendium, `build/assemble.py`, dont la sortie n'a pas de pendant versionné ;
- `check-resume.py` sur l'article et sur le mémoire, où il est inapplicable.

**Deux défauts de plateforme, contournés dans le flux et non corrigés dans les scripts**, relevés le 15 septembre 2026 sous Ubuntu 24.04 (WSL) ; le troisième, les polices du poste que `Traité.pdf` embarque, est à la liste ci-dessus :

- `decompte.sh --verifier` dépend de la locale : son ancre `wc -w` du Vol. I, 233 257, est celle du `wc` de Git pour Windows ; le `wc` GNU en locale UTF-8 compte les espaces insécables comme séparateurs et rend 241 260. Le flux lance `decompte.sh` et `reporter-volumetrie.py` en `LC_ALL=C`, où les deux `wc` rendent 233 257 ;
- `reporter-volumetrie.py` lance `bash` par `subprocess`, que Windows résout en `C:\Windows\System32\bash.exe` — le lanceur WSL, non le bash de Git : le flux ne le rejoue que sous Linux.

La tâche Simulateur prend la chaîne `stable` de l'hôte — `msvc` sous Windows, `gnu` sous Linux —, quand le § 5 a tourné sur la chaîne `stable-x86_64-pc-windows-gnu` que fixe `rust-toolchain.toml` : ni l'une ni l'autre n'est encore éprouvée par le flux (tâche T1.1 du plan).

**Au 15 septembre 2026, le flux n'a jamais tourné** : aucun commit qui le porte n'est poussé, le
badge n'a pas de verdict à rendre, et chaque sortie de cette page est celle du poste de l'auteur.

## 3. Contrôles de document

*Ce document tient-il ?*

| Commande | Depuis | Sortie | Ce qu'elle rend |
|---|---|---|---|
| `python Python/check-veille.py` | `3 - Veille/` | **0** | 94 sections, 24 tableaux, 25 questions ouvertes ; 342 entrées, 306 titres (3 homonymies arbitrées) ; 342 définies, 342 citées |
| `python Python/check-revue.py` | `3 - Veille/` | **0** | 192 définies ; 142 sur 142 neuves citées nommément, 23 sur 50 du socle discutées ; 8 tableaux, 8 légendes ; 12 attestées, 32 autodéclarées, 145 sans revue sur 189 arXiv |
| `python Python/check-traite.py` | `4 - Essais/1 - Traité/` | **0** | 143 pages ; 72 511 mots, 19 figures ; 123 notices, 123 citées nommément ; parité du PDF, 1 551 326 octets hors horodatage, refait à l'identique |
| `python Python/check-empaquetage.py` | `4 - Essais/1 - Traité/` | **0** avec `CARGO_TARGET_DIR`, **1** sans | avec : module WASM refait dans un dossier jetable, 3 670 027 octets identiques à l'octet à celui de `web/`, glu 68 213 octets ; sans : « INDÉTERMINÉ », la construction irait dans le `target/` du dépôt |
| `python PRD/check-compendium.py` | `2 - Compendium/` | **0** | 50 pièces, **P1-P10** ; **5 rapports déclaratifs** |
| `python PRD/check-toc.py` | `2 - Compendium/` | **0** | **C1-C16** |
| `python PRD/check-sieges.py` | `2 - Compendium/` | **0** | 26 sièges sur 50 pièces, S1-S5 |
| `bash PRD/decompte.sh --verifier` | `2 - Compendium/` | **0** | Vol. I 225 258 mots (commande de référence) et 233 257 (`wc -w`) ; Vol. II 93 239, 29 pièces ; Vol. III 160 890, 34 pièces ; agrégat 479 387 ; hors du `wc` de Git pour Windows, en `LC_ALL=C` (§ 2) |
| `python PRD/reporter-volumetrie.py --verifier` | `2 - Compendium/` | **0** | 333 416 mots de corps ; les trois sites qui publient la mesure concordent ; sur ce poste, le `bash` qu'il lance est celui de WSL (§ 2) |
| `python build/verifier-piece.py` | `2 - Compendium/` | **0** | les 50 rendus `.html` sont ceux que les `.md` produisent : parité stricte, purge de l'appareil, figures. Il re-rend chaque pièce par Pandoc : sans Pandoc dans le `PATH`, il sort 1 sur `FileNotFoundError` |
| `python build/assemble-bibliographie.py --verifier` | `2 - Compendium/` | **0** | 1 154 entrées uniques, 109 doublons fondus |
| `python figures/genere.py --verifier` | `2 - Compendium/` | **0**, et **0 sans `PYTHONUTF8`** | 118 figures : 115 gravées sur 49 pièces, 3 antérieures au programme vérifiées à l'empreinte, calculée sur les octets ramenés en LF. *À 8 h 44 le même jour, sur `e1b1b9e` sans correction, il sortait 1 — trois empreintes gelées sur des octets CRLF — et, sans `PYTHONUTF8`, `UnicodeEncodeError` sur le premier ⚠ : la condition B3 de l'évaluation, que les tâches T0.2 et T0.3 du plan lèvent* |
| `python rejeu-politique.py` | `4 - Essais/2 - Article/` | **0** | déroulés A et B, sensibilité, table de transitions totale — 36 cases sur 36 renseignées —, gardes de `hors_service` ; RÉF-6 non déclenchée. **Réserve** : 35 cases sont rejouées entières, la case (étalonnage, E2) à moitié — la branche « sinon → G » n'est exercée par aucune assertion, ce que le script déclare en commentaire |
| `python check-article.py` | `4 - Essais/2 - Article/` | **0** | 77 entrées définies, 77 citées ; parité du PDF, 751 989 octets hors horodatage ; 165 renvois « § » vers 42 cibles ; 10 cardinaux du `README` ; 8 scores |
| `python "3 - Veille/Python/check-resume.py" <fichier.pdf>` | racine | **0** sur dix, **1** sur deux | dégagement sous la marge basse de 72 pt : Vol. I +236,8 ; Vol. II +170,2 ; Vol. III +206,9 ; `Compendium.pdf` **+1,7, « LIMITE »** ; note SDLC +154,8 ; revue +151,2 ; veille +99,2 ; traité +122,3 ; planche *Cinq schémas* **+0,3, « LIMITE »** ; état de l'art +12,6. Sort 1 sur l'article (« déborde de 27.7 pt ») et sur le mémoire de 1997 (« page de titre illisible ») — [§ 6](#6-alertes-que-la-mesure-porte-et-quaucun-contrôle-ne-bloque) |
| `python Python/check-renvois.py` | racine | **0** | 225 `.md` suivis ou non ignorés, 2 079 renvois relatifs dont 75 à fragment ; 0 mort, 1 toléré — une ancre de citation verbatim de la spécification A2A, déclarée au script |
| *Le Vol. I n'a aucun contrôle propre.* | | | |

## 4. Validation par mutation

*Les contrôles tiennent-ils ?*

Chaque harnais copie son corpus dans un dossier temporaire, vérifie que le corpus intact passe, y
injecte des fautes connues, et exige que le contrôle les voie — et, pour certaines, qu'une matière
légitime ne déclenche rien.

| Commande | Depuis | Sortie | Ce qu'elle rend |
|---|---|---|---|
| `python PRD/check-sieges-mutations.py` | `2 - Compendium/` | **0** | passage intact ; **114** mutations attrapées |
| `python PRD/check-toc-mutations.py` | `2 - Compendium/` | **0** | passage intact ; **24** mutations détectées, M1 à M16b, chacune par le contrôle attendu |
| `python PRD/check-compendium-mutations.py` | `2 - Compendium/` | **0** | ligne de base tenue ; **23** mutations au verdict attendu, dont 6 matières légitimes qui ne doivent rien déclencher |
| `python build/verifier-piece-mutations.py` | `2 - Compendium/` | **0** | ligne de base à zéro ; **6** mutations au verdict attendu |
| `python check-article-mutations.py` | `4 - Essais/2 - Article/` | **0** | dossier intact tenu ; **7** mutations au verdict attendu |
| `python Python/check-renvois-mutations.py` | racine | **0** | corpus propre et corpus réel passent ; **16** mutations, M0 à M15, au verdict attendu, dont 5 renvois à ignorer ou à tolérer |

## 5. Fabrication et simulateur

*La chaîne se refait-elle ?*

Ordre réel de fabrication : graver les figures, assembler la source, composer le PDF. Un graveur ou
un assembleur est jugé sur ce qu'il écrit, comparé au blob de l'index.

| Commande | Depuis | Sortie | Ce qu'elle rend |
|---|---|---|---|
| `python figures/contenu.py` | `4 - Essais/1 - Traité/` | **0** | 19 SVG regravés, identiques à l'octet |
| `python figures/dessine.py` | `5 - Recension/` | **0** | 5 SVG regravés, identiques à l'octet |
| `python figures/genere.py` | `2 - Compendium/` | **0** | 118 figures, dont 115 regravées sur 49 pièces ; les 118 SVG et les 55 `.md` des cinq Livres identiques à l'octet — insertion idempotente |
| `python build/assemble.py` | `1 - Collection/2 - OrchestrationAgentique/` | **0** | 38 blocs, 850 Ko ; `Monographie.md` identique à l'octet |
| `python build/assemble.py` | `1 - Collection/3 - EntrepriseAgentique/` | **0** | 34 pièces, 1 094 Ko ; `Monographie.md` identique à l'octet |
| `python build/assemble.py <sortie.md>` | `2 - Compendium/` | **0** | 50 chapitres, 5 livres, 2 annexes, 23 renvois à la note de statut marqués ; 31 095 lignes, 2 698 050 octets, sans pendant versionné |
| `typst compile article-hpc-qpu.typ <sortie.pdf>` | `4 - Essais/2 - Article/` | **0** | 752 159 octets, la taille du PDF versionné ; la parité hors horodatage est celle de `check-article.py` |
| `cargo test --workspace --release` | `4 - Essais/1 - Traité/` | **0** | **470 tests réussis, 0 échec, 0 ignoré** — 17 binaires de test, 6 cibles de doctest |
| `cargo clippy --workspace --all-targets --release` | `4 - Essais/1 - Traité/` | **0** | aucun avertissement sur les six membres du workspace |
| `cargo fmt --all --check` | `4 - Essais/1 - Traité/` | **0** | aucune ligne |
| `cargo doc --workspace --no-deps` | `4 - Essais/1 - Traité/` | **0** | aucun avertissement |
| banc DT1 : `dt1-natif 1000000 > <natif.tsv>`, puis `node bancs/dt1-flottant/banc.mjs <banc_dt1.wasm> <natif.tsv> 1000000` | `4 - Essais/1 - Traité/` | **0** | NF-02 tenue sur 8 groupes à parité exigée, 10⁶ itérations chacun ; 6 opérations de la bibliothèque de plateforme divergent — ln, exp, powf, sin, cos, atan2 —, ce qui est le résultat du banc et non une régression |
| banc EX-V12 : `parite-natif 1 20000 > <natif.tsv>`, puis `node bancs/parite-wasm/banc.mjs <banc_parite.wasm> <natif.tsv> 1 20000` | `4 - Essais/1 - Traité/` | **0** | 6 cas sur 6 identiques natif / WASM |
| `cargo run -p sim-agents --example banc_nf05 --release` | `4 - Essais/1 - Traité/` | **0** | ✗ NF-05 : 29,0 s simulées par s-cœur à n = 1 000, p = 16, sur 200 000 événements, et 23,1 sur 1 000 000, pour une cible de 1 000 — écart consigné, non échec du banc |
| `cargo run -p sim-agents --release --example` `diagnostic_b`, `diagnostic_elasticite`, `diagnostic_conformite` | `4 - Essais/1 - Traité/` | **0** aux trois | `diagnostic_conformite` rend Φ_c = 0,1727 ± 0,0030 à curseur au repos : la mesure ne distingue pas la conformité de la coordination |
| `cargo run -p sim-agents --bin campagne --release -- --sortie <dossier>` | `4 - Essais/1 - Traité/` | **0** | σ̂ = 0,019945, κ̂ = 0,00010018, û* = 98,9 agents ; les paramètres injectés sont dans l'intervalle de confiance |

Les bancs, les exemples et `campagne` ont écrit leurs sorties (`natif.tsv`, `rapports/`) hors du
dépôt.

## 6. Alertes que la mesure porte, et qu'aucun contrôle ne bloque

| Alerte | Mesure | Ce qu'elle veut dire |
|---|---|---|
| Résumé de `Compendium.pdf` | `check-resume.py` sort 0 et écrit « LIMITE : 1.7 pt de dégagement seulement » | la moindre reprise du résumé le fait rogner sous la marge basse, sans que Pandoc ni Typst le signalent ; la tâche T4.5 du plan le condense |
| Résumé de la planche *Cinq schémas* | « LIMITE : 0.3 pt » | même risque, plus serré |
| Rejeu de l'article | 35,5 cases exercées sur 36 : 35 entières, la case (étalonnage, E2) à moitié | « 36/36 » dit que la table est totale, non que chaque branche est exercée ; la tâche T6.7 donne au rejeu un verdict d'étalonnage en entrée |
| `check-resume.py` sur `article-hpc-qpu.pdf` | sort 1, « le résumé déborde de 27.7 pt » | **verdict faux, contrôle inapplicable** : le gabarit arXiv pose un folio en pied de la page de titre, sous la marge par construction, et compose le résumé dans un bloc que Typst reporte à la page suivante au lieu de le rogner — le risque surveillé n'existe pas dans ce gabarit |
| `check-resume.py` sur le mémoire de 1997 | sort 1, « page de titre illisible — contrôle inapplicable » | PDF produit par Acrobat 6.02, qui n'est pas un document composé ici |
| `/Creator` de `1 - Collection/1 - InteroperabiliteAgentique/Monographie.pdf` | `Typst 0.15.0` ; les dix autres PDF composés portent `Typst 0.15.1` | la chaîne du Vol. I n'a pas été rejouée depuis la montée de version (tâche T6.6) |
| `/Title` de `5 - Recension/État de l'art — services financiers.pdf` | `État de lart en services financiers` | apostrophe tombée à la composition ; la source YAML l'écrit bien (tâche T6.1) |

## 7. Ce que ce relevé change à la page précédente

La colonne du milieu se lit par `git show e1b1b9e:APPAREIL.md` ; celle de droite est la sortie du
15 septembre 2026. Les cinq premières lignes sont les écarts que l'évaluation académique relève à
son § 8.4.

| Objet | Écrit au commit `e1b1b9e` | Rejoué le 15 septembre 2026 |
|---|---|---|
| `check-compendium.py` | P1-P8, 3 rapports déclaratifs | P1-P10, 5 rapports déclaratifs |
| `check-toc.py` | C1-C15 | C1-C16 |
| `check-sieges-mutations.py` | 108 mutations | 114 |
| `check-compendium-mutations.py` | 17 sur 17 | 23 |
| `cargo test` | 467 tests | 470 |
| `check-toc-mutations.py` | 23 sur 23 | 24, M1 à M16b |
| `check-traite.py` | 72 110 mots | 72 511 |
| `genere.py --verifier` | 0 | 1 à 8 h 44 sur `e1b1b9e` ; 0 après les tâches T0.2 et T0.3 |
| graveurs et assembleurs | « identiques à l'octet » | à 8 h 50, sur des scripts qui écrivaient en mode texte, 19 SVG du traité et les deux `Monographie.md` ne l'étaient que modulo fins de ligne ; identiques à l'octet après la tâche T0.4 |
| `rejeu-politique.py` | table 36/36, sans réserve | 36 cases renseignées, 35 rejouées entières |
| `check-resume.py` | 0 sur les neuf rendus livrés | 0 sur les neuf, et sur la note ; deux « LIMITE » (§ 6) |
| `typst compile` de l'article | 750 902 octets | 752 159 |
| renvois Markdown | 220 `.md`, 1 992 liens relatifs, 4 morts, par une mesure qu'aucun contrôle versionné ne portait | 225 `.md`, 2 079 renvois relatifs, 0 mort, par `check-renvois.py`, qui vérifie aussi les ancres |
| points d'entrée absents des tableaux | sept : `check-article.py`, `check-article-mutations.py`, `check-empaquetage.py`, `verifier-piece.py`, `verifier-piece-mutations.py`, `rendre-piece.py`, `reporter-volumetrie.py` | aucun ; `rendre-piece.py` est rejoué au travers de `verifier-piece.py` |
| intégration continue | « rien n'est câblé » | flux écrit, jamais exécuté (§ 2) |

## 8. Ce qui n'a pas été rejoué le 15 septembre 2026

- Les sept `build/build-pdf.sh` — Vol. I, II, III, compendium, traité, `3 - Veille/`,
  `5 - Recension/` — et les trois `build/inject-pagination.py` qu'ils appellent : les PDF livrés ne
  sont jugés ici que sur leurs sorties versionnées — pages, métadonnées, géométrie de la page de
  titre, et parité là où `check-traite.py` et `check-article.py` la mesurent.
- `2 - Compendium/build/echantillon.py`, maquette de gabarit qui écrit deux PDF à la racine du
  volume.
- Les deux `.html` de `5 - Recension/` : leur commande prend une feuille de style que le dépôt ne
  versionne pas (tâche T6.4).

## 9. L'arbre rejoué

- **Commit** : `e1b1b9e`, « plan », 15 septembre 2026 à 7 h 23.
- **Premier passage, de 8 h 43 à 8 h 55**, sur ce commit, les corrections du plan arrivant pendant
  qu'il tournait : les bancs, les exemples, `campagne`, `check-empaquetage.py` avec cible et
  `typst compile` de l'article viennent de lui ; `cargo test`, `clippy`, `fmt` et `doc` ont rendu
  la même sortie aux deux passages. Ce qu'il rend autrement que le passage final est au § 7.
- **Passage final, de 9 h 06 à 9 h 20** : tout le reste, sur l'arbre qui portait, non commitées,
  les empreintes de `genere.py` réancrées sur les octets LF (T0.2), `sys.stdout.reconfigure` dans
  les scripts qui impriment ⚠ ou ☑ (T0.3), les écritures en `newline="\n"` des graveurs et des
  assembleurs (T0.4), les trois PDF de travail de `5 - Recension/` sortis de l'index (T0.5), le
  `repository` du `Cargo.toml` et les deux `README` du traité (T0.9), la décision D-17 (T0.1), les
  renvois vers `2 - Compendium/audit.md` repointés (T0.8), `Python/check-renvois.py`, son harnais
  et le flux d'intégration continue (T1.1 à T1.4), `ARCHIVES.md` (T2.3) ; `check-renvois.py` a été
  rejoué en dernier, après l'entrée de `CONTRIBUTIONS.md` (T2.1) et les éditions de cette page.
- **Les scripts n'ont pas bougé pendant le passage final** :
  `git diff -- '*.py' '*.sh' '*.toml' | sha256sum` rend `ae59606d11c0…` avant et après.

## 10. D'où viennent les chiffres du `README.md`

Chaque commande se lance de la racine du dépôt ; la sortie est celle du 15 septembre 2026.

| Chiffre | Commande | Sortie |
|---|---|---|
| pages des PDF | `pymupdf.open(f).page_count` sur chaque `*.pdf` de `git ls-files` | 569, 387, 427, 1 000, 143, 144, 59, 186 et 7 pour les neuf rendus des huit livrables — **2 922** ; 49 pour la note SDLC et 38 pour l'article — **3 009** sur onze PDF composés ; 146 pour le mémoire de 1997 |
| fichiers et octets au commit | `git ls-tree -r -l e1b1b9e \| awk '{s+=$4} END {print NR, s}'` | 589 fichiers, 79 704 921 octets |
| fichiers par extension | `git -c core.quotepath=off ls-tree -r --name-only e1b1b9e` | 222 `.md`, 142 `.svg`, 76 `.rs`, 54 `.html`, 39 `.py`, 15 `.pdf`, 9 `.toml`, 8 `.sh`, 7 `.template`, 4 `.gitignore`, 3 `.typ`, 2 `.mjs`, 2 `LICENSE`, 1 `.txt`, 1 `.lua`, 1 `Cargo.lock`, 1 `.json`, 1 `.bib`, 1 `.gitattributes` |
| lignes de Rust | `git ls-files -z '*.rs' \| xargs -0 cat \| wc -l` | 30 939 lignes dans 76 fichiers ; 30 488 dans les 71 de `crates/` |
| lignes des sources | `wc -l` | Vol. I 7 257 ; Vol. II 3 306 ; Vol. III 3 275 ; traité 1 889 ; veille 1 932 ; revue 1 052 ; état de l'art 1 986 ; note SDLC 1 070 ; article, `.typ`, 1 979 |
| diagrammes Mermaid | `grep -c` sur la ligne d'ouverture de bloc `mermaid` | 28 dans le Vol. I, 64 dans les `.md` versionnés |
| diapositives de `NiveauMaturité.html` | `grep -c '<section class="slide"'` | 7 |
| `README.md` versionnés | `git ls-files '*README.md' \| wc -l` | 18 |
| historique | `git log --format=%an \| sort \| uniq -c` ; `git log --merges` ; `git tag` | 328 commits du 24 juin au 15 septembre 2026 — 306 André-Guy Bruneau, 20 `Claude`, 2 `agbruneau` ; 4 fusions ; une étiquette, `mono-v1.0` |
| renvois Markdown | `python Python/check-renvois.py` | 225 `.md` suivis ou non ignorés, 2 079 renvois relatifs dont 75 à fragment ; 0 mort, 1 toléré — une ancre de citation verbatim de la spécification A2A, déclarée au script |
