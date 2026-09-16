# stigmergie-lab — le traité et sa transposition

Le dossier porte deux choses. Le *Traité sur les systèmes multiagents en essaim*, [`Traité.pdf`](Trait%C3%A9.pdf) — quatrième édition du
2 septembre 2026, 143 p. numérotées et une page « Abstract » : la coordination par le milieu, ce qu'un essaim gagne à ne pas s'accorder et ce qu'il le paie. Et
`stigmergie-lab`, simulateur déterministe en Rust qui le transpose sous une règle : tout chiffre affiché doit être retrouvé par la
mesure, ou l'écart consigné. Cinq écarts le sont, dont deux portent contre le traité depuis le reclassement du 17 août 2026 — trois avant lui, compte que cite la troisième édition —, au [registre des décisions](docs/decisions.md).

**Statut :** le traité est livrable (Vol. V) — fixé le 15 septembre 2026 par la décision [D-18](../../2%20-%20Compendium/PRD/PRD.md#d-18) ;
le simulateur, sa transposition, est hors compte. Dépôt rouvert le même jour par [D-17](../../2%20-%20Compendium/PRD/PRD.md#d-17), re-clos le 16 septembre 2026 par [D-19](../../2%20-%20Compendium/PRD/PRD.md#d-19).

**Par où entrer :** le traité ; puis [`docs/README.md`](docs/README.md), l'index de la documentation — [`PRD.md`](docs/PRD.md) dit ce qui
est exigé, [`SPEC.md`](docs/SPEC.md) ce que le code garantit — et [`CLAUDE.md`](CLAUDE.md) pour qui reprend le code.

**Prérequis :** Rust stable, cible fixée par `rust-toolchain.toml` ; mingw-w64 pour l'interface ; et `CARGO_TARGET_DIR` hors de OneDrive
avant toute commande `cargo`, faute de quoi l'édition de liens échoue ([`DEVELOPPEMENT.md`](docs/DEVELOPPEMENT.md)).

**Refaire :** depuis ce dossier.

1. L'interface, scénarios A et B : `cargo run -p sim-viz --release`.
2. L'interface web, même code et mêmes chiffres, servie ensuite par `python -m http.server 8777 --directory web` :

   ```bash
   cargo build -p sim-viz --release --lib --target wasm32-unknown-unknown \
     && wasm-bindgen --target web --no-typescript --out-dir web \
        "$CARGO_TARGET_DIR/wasm32-unknown-unknown/release/sim_viz.wasm"
   ```

3. La campagne sans interface, scénario C : `cargo run -p sim-agents --bin campagne --release -- --sortie rapports/`.
4. Les tests — chaque critère d'acceptation en est un : `cargo test --workspace --release`.

`bash build/build-pdf.sh` recompose le traité ; `python Python/check-traite.py` en vérifie pagination, notices et parité du rendu, et
`python Python/check-empaquetage.py` que le module WASM est celui que les sources produisent. L'intégration continue
([`appareil.yml`](../../.github/workflows/appareil.yml)) rejoue `cargo fmt`, `clippy` et `test`, plancher de 470 tests, sous Linux et
Windows ; ni `cargo doc`, ni les bancs, ni l'empaquetage WASM.

**Réserves :** la cible de débit NF-05 n'est pas atteinte, par un écart structurel en Θ(n²) ; NF-07 n'est pas mesurée ; l'interface
s'arrête aux scénarios A et B. La liste complète est au §0 du [PRD](docs/PRD.md) et à l'onglet « Limites » de l'interface.

**Journal :** [`JOURNAL.md`](JOURNAL.md) — entrée du dossier au dépôt, figures et chaîne de rendu, mesures datées de l'empaquetage et des
tests, et l'index de la documentation tel qu'il était écrit au 15 septembre 2026.
