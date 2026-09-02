# Verdict — parité de sortie natif / WASM (EX-V12)

**Question posée.** Deux cibles, un seul code : le destinataire d'un lien de
partage voit-il **exactement** la même figure que son émetteur ?

**Réponse.** Oui, sur les six cas du scénario B, bits des flottants compris.

☑ **Rejoué le 2 septembre 2026** sur un module reconstruit, et **tenu** : six cas, six paires d'empreintes identiques, sortie 0. *Le module reconstruit est lui-même identique à l'octet à celui du 17 août 2026* — la construction WASM est reproductible, ce que ce banc n'avait pas eu à mesurer jusqu'ici. ⚠ **Ce rejeu ne périme pas la mesure d'origine, il la reconduit** : *un verdict de parité vaut pour la construction sur laquelle il a été pris, et celle-ci est la même.*

## Le montage

Le banc calcule une empreinte de `ResultatB` — mesures, trace d'entrelacement,
bornes, φ moyen — pour six configurations nommées, à graine 1 et budget 20 000 :

| Cas | Ce qu'il exerce |
|---|---|
| nominal | Le régime de référence |
| verrouillage (γ = 1) | Le mode de défaillance EX-A11a |
| essaim aveugle (T < ℓ₉₉) | Le cycle plus court que la durabilité |
| rejeu | Les effets dupliqués |
| incomparabilité M2 | L'entrelacement randomisé |
| trace optimiste | Le dépôt avant l'action |

Les deux côtés sont **régénérés à chaque exécution** : le natif écrit
`natif.tsv`, que le comparateur Node relit avant de faire tourner le module
WASM. Ce fichier est dans `.gitignore`, et c'est délibéré — le versionner
ferait croire à une référence stable là où il n'y en a pas.

La ligne exacte est dans
[`docs/DEVELOPPEMENT.md`](../../docs/DEVELOPPEMENT.md) ; en résumé :

```bash
cargo build --release --bin parite-natif && cargo build --release -p banc-parite --lib --target wasm32-unknown-unknown && ./target/release/parite-natif 1 20000 > bancs/parite-wasm/natif.tsv && node bancs/parite-wasm/banc.mjs target/wasm32-unknown-unknown/release/banc_parite.wasm bancs/parite-wasm/natif.tsv 1 20000
```

## Ce qui est mesuré, et ce qui ne l'est pas

**Mesuré** : l'égalité des empreintes. Aucune ligne « constat » — contrairement
au banc DT1, toute divergence est ici un **défaut bloquant**, parce qu'EX-V12
est une sûreté `[S]`.

**Non mesuré** : la performance, le rendu, et l'égalité de *toutes* les
grandeurs — l'empreinte est un hachage, donc elle détecte une divergence sans
dire laquelle. C'est suffisant pour un verdict de sûreté, insuffisant pour un
diagnostic.

**Non versionné** : aucune des deux sorties. La conclusion n'est donc
redémontrable que par recompilation, et c'est assumé — figer un hachage
reviendrait à figer une version de `rustc` et de `wasm-bindgen` dans un fichier
que rien ne met à jour, et le banc DT1 a déjà montré ce que valent les verdicts
qui dépendent de la machine de construction.

## Un défaut trouvé par le banc, et corrigé

Le banc rendait `0` quand `scenario_b` échouait. Un échec **symétrique** — un
paramètre refusé sur les deux cibles — produisait donc deux fois
`0000000000000000`, le comparateur concluait « identique », et le banc
affichait « EX-V12 : tenue sur 6 cas » sans qu'aucun scénario n'ait tourné. Un
verdict de parité doit distinguer « mêmes chiffres » de « aucun chiffre » : le
banc panique maintenant, avec le motif du refus.

## Conséquence

`sim-viz` expose une bibliothèque que les deux cibles partagent, et `main.rs`
fait seize lignes dont six de code, sans aucune logique : deux `fn main` gardés
par cible. C'est cette structure qui rend EX-V12 mesurable : deux
binaires distincts la rendraient invérifiable par construction.
