# DT1 — Arithmétique du cœur : verdict

**Décision : le flottant reste, sur toute la simulation. Aucun point fixe.**
Les transcendantes passent par `libm`, jamais par les méthodes de `f64`.

Tranchée sur mesure le 12 août 2026, conformément au §11 (« attendre le banc
d'essai RQ1 ») et au §9 (« DT1 est tranchée sur mesure et non par défaut »).

## Mesure

10⁶ itérations par groupe, une opération par groupe, hachage FNV-1a des bits
IEEE-754 de chaque résultat intermédiaire. Entrées produites par un générateur
congruentiel entier : les deux cibles reçoivent les mêmes bits.

| Cible | Détail |
|---|---|
| Native | `x86_64-pc-windows-gnu`, rustc 1.97.1, profil `release`, `opt-level = 3` |
| WASM | `wasm32-unknown-unknown`, même rustc, exécuté sous Node v24.19.0 (V8) |

| Opération | Parité | Résultat |
|---|---|---|
| `+ − × ÷`, `sqrt`, `floor`, `ceil`, comparaisons, conversion `f64 → u64` | exigée | **identique** |
| `f64::ln`, `exp`, `powf`, `sin`, `cos`, `atan2` | constat | **divergent** |
| `f64::mul_add` | constat | **instable — voir ci-dessous** |
| `libm::log`, `exp`, `pow`, `sin`, `cos`, `atan2`, `fma` | exigée | **identique** |

### `mul_add` : le cas le plus instructif du banc

Au premier passage, `f64::mul_add` divergeait entre natif et WASM. Au second —
après l'installation de mingw-w64 sur la machine de construction, qui n'a rien
à voir avec ce calcul — il **coïncide**. Rien du code n'avait changé.

Ce n'est pas une mesure contradictoire, c'est le résultat : `f64::mul_add`
délègue à la bibliothèque mathématique que l'éditeur de liens trouve, et ce
qu'il trouve dépend de ce qui est installé. Une opération dont le résultat
dépend de l'outillage présent sur la machine de build est exactement ce que
NF-02 ne peut pas tolérer — une exécution rejouée sur un poste différemment
équipé donnerait d'autres bits, sans qu'aucun changement de code ne le signale.

L'interdiction de `f64::mul_add` en sort renforcée, pas affaiblie. `libm::fma`,
lui, est resté identique aux deux passages et sur les deux cibles.

## Lecture

**Le groupe de base est exact des deux côtés.** IEEE-754 impose le résultat de
l'addition, de la soustraction, de la multiplication, de la division et de la
racine carrée ; les deux cibles le rendent bit à bit. L'hypothèse pessimiste du
§11 — points fixes sur tout chemin influençant l'ordonnancement — n'a pas lieu
d'être : l'horloge logique, le départage de la file, les compteurs et les dates
d'événements tiennent en flottant sans risque.

**La divergence vient entièrement de la bibliothèque mathématique de la
plateforme.** Les transcendantes ne sont pas normées par IEEE-754 : chaque
plateforme livre son approximation. Le natif appelle la libm du système, le WASM
embarque la sienne.

**Détail qui décide de la solution.** Le hachage de `libm::log` **en natif**
(`f4ec27f3f92a91ac`) est exactement celui de `f64::ln` **en WASM**. La cible
WASM route donc déjà ses transcendantes vers `libm` ; adopter `libm`
explicitement ne déplace que le natif, et le fait converger vers le WASM. Même
constat pour les six autres.

**`mul_add` est un piège distinct**, et le seul dont le résultat a bougé d'un
passage à l'autre du banc. Écrire `a * b + c` donne un résultat portable ;
`libm::fma` donne l'arrondi unique, portablement. Les deux sont admissibles,
`f64::mul_add` ne l'est pas — non parce qu'il diverge toujours, mais parce
qu'on ne peut pas savoir quand il divergera.

## Conséquences appliquées

1. **Aucun point fixe.** Le PRD §11 les donnait « par défaut » ; la mesure les
   écarte. Le coût évité est celui d'une arithmétique d'échelle sur tout le
   moteur.
2. **`libm` entre dans les dépendances** (§5.2). Elle n'est pas ajoutée par un
   mécanisme — le critère de dérive du §5.2 tient — mais par NF-02, exigence
   antérieure au découpage en mécanismes.
3. **Sept méthodes de `f64` sont interdites** dans les crates de simulation, et
   l'interdiction est vérifiée par `clippy.toml` plutôt que par convention :
   `ln`, `exp`, `powf`, `sin`, `cos`, `atan2`, `mul_add`.
4. **Le banc devient un test permanent de NF-02.** Il échoue si un groupe à
   parité exigée diverge ; la divergence des six opérations de plateforme est
   son résultat, pas une régression, et ne le fait pas échouer.

## Ce que ce banc ne démontre pas

- **Rien sur les autres cibles.** Le verdict porte sur `x86_64-pc-windows-gnu`
  contre `wasm32-unknown-unknown` sous V8. Une cible ARM, un autre moteur WASM
  ou une autre version de rustc demandent de relancer le banc — c'est
  précisément à quoi il sert. Le cas `mul_add` montre que même une autre
  **machine de construction** suffit à changer un résultat.
- **Rien sur l'ordre des opérations.** Le banc mesure des opérations isolées.
  Une somme dont l'ordre des termes dépend d'un `HashMap` divergerait malgré un
  flottant parfaitement portable ; c'est PD1 qui couvre ce cas, pas DT1.
- **Rien sur la précision.** Deux résultats identiques peuvent être également
  faux. La parité est une propriété de reproductibilité, pas d'exactitude.

## Rejouer

```bash
cargo build --release --bin dt1-natif && cargo build --release --lib --target wasm32-unknown-unknown && ./target/release/dt1-natif 1000000 > bancs/dt1-flottant/natif.tsv && node bancs/dt1-flottant/banc.mjs target/wasm32-unknown-unknown/release/banc_dt1.wasm bancs/dt1-flottant/natif.tsv 1000000
```
