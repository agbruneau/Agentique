# Construire et rejouer

Ce document donne la ligne de commande exacte de chaque opération. Ce que ces
commandes **garantissent** est dans [`SPEC.md`](SPEC.md) ; pourquoi elles
existent est dans le [PRD](PRD.md).

## Chaîne d'outils

| Outil | Version employée | Pourquoi |
|---|---|---|
| Rust | stable — 1.97.1 au moment de la mesure — cible `x86_64-pc-windows-gnu` | Le linker MSVC exige le toolset C++ de Visual Studio, absent de la machine de développement. `rust-toolchain.toml` fixe le **canal et la cible** ; il ne fixe pas la version. |
| Cible WASM | `wasm32-unknown-unknown` | Cible du produit (O5). Le banc DT1 la compare au natif. |
| mingw-w64 | WinLibs POSIX/UCRT | `dlltool.exe`, exigé par les crates qui lient des DLL Windows (`eframe` et ses dépendances). |
| Node | 24 | Exécute le module WASM du banc DT1 sur le même moteur que le navigateur visé. |
| `wasm-bindgen-cli` | 0.2.127, épinglée sur `Cargo.lock` | Produit la glu JavaScript de l'interface web. Une version différente de celle de la bibliothèque est refusée à l'exécution. |

`dlltool.exe` doit être dans le `PATH` pour compiler `sim-viz` :

```bash
export PATH="$LOCALAPPDATA/Microsoft/WinGet/Packages/BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe/mingw64/bin:$PATH"
```

Les autres crates — `sim-core`, `sim-milieu`, `sim-agents` — n'en ont pas besoin.

## Commandes

Suite de tests complète — **467 tests** au 17 août 2026, 11 h 14, exit 0 :

```bash
cargo test --workspace --release
```

Le compte se répartit en 424 tests unitaires dans les modules — 254 dans
`sim-agents`, 96 dans `sim-core`, 68 dans `sim-milieu`, 6 dans `sim-viz` — et 43
tests d'intégration, qui sont les critères de sortie de phase. Le §0 du PRD
enregistre 348 à la clôture de la phase 5 ; la phase 6 a porté le compte à 419,
l'audit du 13 août à 428, et celui du 17 août à 447, puis 465, 466, 467 — des
tests ajoutés pour fermer des trous que la révision a ouverts, aucun affaibli.
**Le compte est une mesure et se refait ; c'est la répartition, elle, qui dit où
le filet est lâche** — 43 tests d'intégration pour 424 unitaires, et six seulement
sur toute l'interface. Le total a bougé **cinq** fois en trois heures le 17 août
— 428 à 08 h 10, 447 à 08 h 32, 465 à 09 h 49, 466 à 10 h 26, 467 à 11 h 14 —,
plusieurs agents écrivant en parallèle : un compte gravé dans un document se
périme sans que rien ne le signale, la ligne de commande ne se périme pas.

⚠ **`cargo` n'est pas dans le `PATH`, et l'édition de liens échoue dans le
`target/` du dépôt** parce que le chemin contient un « é ». Les mesures
ci-dessus ont été prises ainsi :

```powershell
$env:PATH = "$env:USERPROFILE\.cargo\bin;$env:LOCALAPPDATA\Microsoft\WinGet\Packages\BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe\mingw64\bin;$env:PATH"
$env:CARGO_TARGET_DIR = "C:\Users\agbru\AppData\Local\Temp\cargo-conso"
```

Un seul test, ou un module :

```bash
cargo test -p sim-agents --release critere_2_le_seul_curseur
```

Documentation d'interface — les quatre crates déclarent `#![deny(missing_docs)]`,
donc un item public sans `///` ne compile pas :

```bash
cargo doc --workspace --no-deps --open
```

Interface native — le binaire s'appelle `stigmergie-lab` :

```bash
cargo run -p sim-viz --release
```

Interface web — construction, puis service local (DT4 : pages statiques) :

```bash
cargo build -p sim-viz --release --lib --target wasm32-unknown-unknown && wasm-bindgen --target web --no-typescript --out-dir web target/wasm32-unknown-unknown/release/sim_viz.wasm
```

```bash
python -m http.server 8777 --directory web
```

Le `.wasm` doit être servi en `application/wasm` ; `file://` ne fonctionne pas,
les modules ES l'interdisent.

**Rien n'attrape aujourd'hui une horloge système réintroduite dans `sim-viz`.**
Reconstruire pour `wasm32-unknown-unknown` ne suffit pas : `std::time::Instant`
compile sans un mot pour cette cible et ne panique qu'à l'exécution, dans un
navigateur. Ce qui marcherait est `cargo clippy --target wasm32-unknown-unknown`
avec le type interdit — sur cette cible, `web_time::Instant` n'est **pas**
`std::time::Instant`, donc le lint frapperait le défaut sans frapper le
correctif. Non câblé ; voir `clippy.toml`.

Banc DT1 — parité flottante natif/WASM, test permanent de NF-02 :

```bash
cargo build --release --bin dt1-natif && cargo build --release --lib --target wasm32-unknown-unknown && ./target/release/dt1-natif 1000000 > bancs/dt1-flottant/natif.tsv && node bancs/dt1-flottant/banc.mjs target/wasm32-unknown-unknown/release/banc_dt1.wasm bancs/dt1-flottant/natif.tsv 1000000
```

Banc EX-V12 — parité de sortie natif/WASM d'un mécanisme complet :

```bash
cargo build --release --bin parite-natif && cargo build --release -p banc-parite --lib --target wasm32-unknown-unknown && ./target/release/parite-natif 1 20000 > bancs/parite-wasm/natif.tsv && node bancs/parite-wasm/banc.mjs target/wasm32-unknown-unknown/release/banc_parite.wasm bancs/parite-wasm/natif.tsv 1 20000
```

Campagne sans interface — scénario C, CSV et rapport JSON :

```bash
cargo run -p sim-agents --bin campagne --release -- --sortie rapports/
```

Banc NF-05 — débit de simulation :

```bash
cargo run -p sim-agents --example banc_nf05 --release
```

Diagnostic du scénario B — effort par tranche de temps :

```bash
cargo run -p sim-agents --example diagnostic_b --release
```

Diagnostic du contrôleur d'élasticité — l'oscillation structurelle du §0 du PRD,
celle que l'hystérésis de descente divise par cinq sans la supprimer :

```bash
cargo run -p sim-agents --example diagnostic_elasticite --release
```

Diagnostic de conformité — Φ_c en fonction de la part de conformité. C'est ce
diagnostic qui a réfuté le premier point du critère de sortie de la phase 6, et il
existe pour que le constat se reproduise plutôt que se cite :

```bash
cargo run -p sim-agents --example diagnostic_conformite --release
```

## Avant de committer

Il n'y a pas d'intégration continue dans ce dépôt — NF-13 et NF-16 nomment un
mécanisme d'application qu'il ne contient pas. Ce que ces exigences obtiennent
vient donc de ces **trois** commandes, lancées à la main, dans cet ordre :

```bash
cargo test --workspace --release
```

```bash
cargo clippy --workspace --all-targets --release
```

```bash
cargo doc --workspace --no-deps
```

**La troisième manquait, et son absence a coûté.** `cargo test` et `cargo clippy`
sont restés verts pendant que `cargo doc` sortait en 101 sur deux renvois
rustdoc cassés : la procédure d'avant commit était structurellement incapable de
voir le seul défaut mécanique que le dépôt portait en cours. Les trois sortent
non nulles à la première violation.

Si le changement touche `sim-viz` ou une transcendante, ajouter le banc de parité
correspondant ci-dessus. Si le changement touche un critère de sortie de phase,
la règle est dans [`SPEC.md`](SPEC.md) et elle est courte : **ne pas affaiblir
ces tests** — ce sont les preuves du tableau du §0 du PRD.

## Règles que le dépôt fait respecter mécaniquement

- `clippy.toml` interdit sept méthodes de `f64` : **six** mesurées divergentes
  entre natif et WASM (NF-02, verdict DT1), et `mul_add`, mesurée *identique* au
  second passage du banc mais dont le verdict **a changé** après l'installation
  de mingw-w64 sans qu'une ligne de code bouge — elle dépend de la machine de
  construction, ce qui est pire que diverger. Le fichier porte les deux motifs
  séparément depuis le 17 août 2026. Sont interdits aussi `HashMap` et `HashSet`,
  dont l'itération n'est pas ordonnée (PD1). **Ces neuf interdictions sont `deny`**, par le
  `[workspace.lints.clippy]` du `Cargo.toml` racine que les six membres héritent
  — sans quoi elles restent au niveau `warn` de leur groupe `style` et `cargo
  clippy` sort **0 sur du code interdit**, ce qui était le cas jusqu'à l'audit.
- Le banc DT1 échoue si une opération à parité exigée diverge. La divergence des
  transcendantes de plateforme est son **résultat**, pas une régression, et ne
  le fait pas échouer.
- `#![deny(missing_docs)]` sur les quatre crates : un item public sans `///` ne
  compile pas.
- `#![deny(rustdoc::broken_intra_doc_links)]` : un renvoi rustdoc cassé ne
  compile pas non plus. C'est ce qui garde les liens entre modules vrais quand un
  type est renommé.
- Le profil `release` du workspace n'active **aucune** option d'arithmétique
  relâchée, et `lto` reste désactivé sur le banc DT1 : la mesure porte sur les
  opérations, pas sur ce que l'optimiseur en fait.

Ce que **rien** ne fait respecter, et qu'il faut donc tenir à la lecture : les
listes d'absences. `sim_agents::hors_perimetre()`,
`sim_milieu::hors_perimetre()` et `ModeleFaute::hors_modele()` sont des
livrables (PD6), et la règle est *branché / pas branché*, non *écrit / pas
écrit* — une entrée ne se retire que lorsqu'un scénario appelle effectivement le
mécanisme.

## Verdicts de banc

| Banc | Verdict |
|---|---|
| DT1 — arithmétique | [`bancs/dt1-flottant/VERDICT.md`](../bancs/dt1-flottant/VERDICT.md) |
| NF-05 — débit | [`bancs/nf05-debit/VERDICT.md`](../bancs/nf05-debit/VERDICT.md) |
| EX-V12 — parité natif/WASM | [`bancs/parite-wasm/VERDICT.md`](../bancs/parite-wasm/VERDICT.md) |
