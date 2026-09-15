# Documentation de stigmergie-lab

Tout ce qui documente le simulateur vit ici, sauf ce qu'un outil ou une mesure attend ailleurs : le [`README.md`](../README.md) et
[`CLAUDE.md`](../CLAUDE.md) à la racine du dossier, les `VERDICT.md` sous [`bancs/`](../bancs/), à côté de la mesure qui les produit, et la
source normative elle-même, [`Traité.pdf`](../Traité.pdf), à la racine du dossier.

Deux documents seulement sont des sources : le traité pour ce qui est exigé, le code pour ce qui est garanti. Le PRD tire son autorité du
traité, `SPEC.md` du code ; là où les deux divergent, le PRD garde l'exigence et `SPEC.md` dit ce que le code fait.

**Statut :** documentation de la transposition du traité, livrable (Vol. V) par la décision
[D-18](../../../2%20-%20Compendium/PRD/PRD.md#d-18) du 15 septembre 2026 ; le simulateur est hors compte.

| Document | Ce qu'il contient | Quand le lire |
|---|---|---|
| [`PRD.md`](PRD.md) | ce qui est exigé, sous des codes que le code source cite ; le §0 suit l'avancement, le §12 A mène du traité à l'implantation | pour la lettre d'une exigence ou l'état du projet |
| [`SPEC.md`](SPEC.md) | ce que le code garantit : déterminisme, moteur, catalogue des oracles, milieu, et ce que le contrat ne couvre pas | avant d'écrire du code |
| [`architecture.md`](architecture.md) | les quatre crates, ce que chaque couche refuse de savoir, la carte des modules | pour savoir où va un changement |
| [`decisions.md`](decisions.md) | le registre : décisions techniques, verdicts de banc, décisions ouvertes, écarts au traité | avant de refaire un choix tranché |
| [`DEVELOPPEMENT.md`](DEVELOPPEMENT.md) | chaîne d'outils, commande exacte de chaque banc, commandes d'avant commit | pour construire ou rejouer |

Verdicts de banc : [DT1, arithmétique](../bancs/dt1-flottant/VERDICT.md) · [NF-05, débit](../bancs/nf05-debit/VERDICT.md) ·
[EX-V12, parité natif et WASM](../bancs/parite-wasm/VERDICT.md).

**Par où entrer :** l'état et les réserves au §0 du PRD ; ce que le produit ne mesure pas, au §8.3 du PRD et à l'onglet « Limites » de
l'interface ; un code cité dans le code — `EX-C01`, `PD1`, `NF-02` — se cherche tel quel dans le PRD.

**Documentation d'interface :** dans le code, en rustdoc, par `cargo doc --workspace --no-deps --open` ; les quatre crates déclarent
`#![deny(missing_docs)]` et `#![deny(rustdoc::broken_intra_doc_links)]`.

**Journal :** cet index tel qu'il était écrit au 15 septembre 2026 — le graphe de qui dérive de qui, ce qui n'existe pas et pourquoi — est
à la [page du journal du dossier](../JOURNAL.md#page-docs).
