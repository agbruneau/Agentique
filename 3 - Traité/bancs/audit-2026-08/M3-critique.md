# M3 · mécanismes de `sim-agents` — jugement du critique, tour 1

Agent en contexte neuf. Comparaison à l'aveugle contre `bancs/dt1-flottant/VERDICT.md`,
partie 1 écrite avant ouverture du dépôt. Le rapport d'audit était le document **B**.

## Verdict : **B** — le rapport d'audit

> Chaque affirmation de B est réduite à un atome que le lecteur peut ouvrir seul —
> `fichier:ligne`, page, citation verbatim, sortie de commande collée —, et le document
> soumet sa propre méthode à un étalonnage (le folio imprimé confronté à l'index physique)
> avant de s'en servir.

## L'écart retenu — sur le perdant (le verdict DT1)

> Le tableau de parité est le résultat du document, et il ne livre pas ce qu'il a mesuré :
> « identique », « divergent » sont des jugements déjà rendus, pas des données. […]
> L'inférence qui décide de toute la solution repose sur un point de mesure divulgué sur sept.

**Cinquième critique consécutif à désigner le même défaut**, en contextes séparés.

## Ce qui tient

Le protocole de provenance est bon : le folio imprimé coïncide avec l'index physique —
vérifié sur 15 pages (2, 3, 4, 5, 11, 16, 59, 78, 80, 104, 107, 112, 114, 130, 143). PDF à
143 pages, à la racine. **Les 14 relocalisations sont toutes justes**, dont huit revérifiées
par ancre textuelle : `stigmergie.rs` §1.2 → 16 ✓, `agregation.rs` §4.1 → 58/59 ✓,
`usl.rs` → 130 ✓, `adhesion.rs:24` → 21/22 ✓, `adhesion.rs:35` → 129 ✓ (la variante « est »
est bien p. 95 — la distinction est correcte), `allocation.rs:117` → 78 ✓, `cascade.rs:3`
→ 91 ✓, `taux_de_base.rs:20` → 107/110 ✓. **290 tests, 0 échec**, clippy muet, `cargo doc`
propre.

## Affirmations prises en défaut

### G-a — « Dernière notice de la bibliographie : 120 » est faux

La bibliographie va jusqu'à **123** (`Traité.pdf` p. 143 : « 123. Commission européenne… »),
sans trou. Le chiffre figure au tableau *Mesure* du banc de provenance, donc revendiqué comme
mesuré, dans la section même qui reproche à `CLAUDE.md` ses chiffres faux — **et `CLAUDE.md`,
qui dit 123 notices, a raison.**

### G-b — la page de la contre-preuve d'A6 est fausse

B écrit « le §4.3 (**p. 71-72**) ne donne que le majorant », puis cite « leurs valeurs par
défaut, période 10 s, expiration 1 s, seuil d'échec 3, fixent à 30 s le délai… ». Cette phrase
est **p. 70**. La page portée dans le code (§7.3, p. 112) est juste ; **c'est la page qui sert
à l'invalider qui ne l'est pas** — le défaut corrigé reparaît dans le paragraphe qui le corrige.

### G-c — « Cinq tests ajoutés, un par chemin » est faux, et le document se contredit

**Trois** tests ajoutés (`soupcon.rs:605`, `cycle_de_vie.rs:343`, `echantillonnage.rs:394`) —
ce que la section « Commandes exécutées » dit 200 lignes plus loin. `git diff -U0 HEAD --
crates/sim-agents/src/accord.rs` ne contient **aucun `#[test]` ajouté** : le chemin
`accord.rs:370/378/419` est corrigé sans test. C'est précisément celui dont la correction est
incomplète.

### G-d — trois des cinq chemins ne sont corrigés que dans un sens ; la cause reste

Les correctifs couvrent l'*agrandissement* d'un champ public, pas le *rétrécissement*.
Mesuré par exécution (crate hors dépôt, `catch_unwind`) :

```
[PANIQUE] TriDeVue::attribut rétréci    → echantillonnage.rs:228  len 4, index 14
[PANIQUE] scission après rétrécissement → echantillonnage.rs:264  len 4, index 23
[PANIQUE] MoyenneLocale::x rétréci      → accord.rs:393           len 2, index 19
```

`Vec::resize` tronque `vues` mais ne purge pas les identifiants obsolètes qu'elles
contiennent ; et dans `MoyenneLocale::tour`, les `resize` traitent les tables auxiliaires
pendant que la cause reste — `anciens[j as usize]` où `j` est borné par la population du
**service**, jamais par `x.len()`.

### G-e — la clause invoquée n'est pas celle qui est appliquée

`docs/SPEC.md:668` : « `Result` plutôt que `panic!` : une configuration invalide est un refus
rendu à l'appelant, jamais un abandon ». Les correctifs des deux seuils sont des
`saturating_sub(1)` : une **coercition silencieuse**. `completude(10, 1, 0)` rend `(1, 11)`
sans rien signaler. Documenté dans le `///`, donc pas caché — mais ce n'est pas « un refus
rendu à l'appelant », et le document présente les deux comme la même chose.

### G-f — N5 est sous-décrit, et son motif de non-correction ne tient qu'à moitié

« Hors du domaine (0, 1), la calibration retombe silencieusement sur γ = 0,999 999 » n'est
vrai que pour γ ≥ 1 : `self.gamma.min(0.999_999)` ne borne **que par le haut**. Mesuré sur
`Params::scenario_b()` :

```
gamma =   0.9 -> depot() = 8.2313e-5
gamma =   1.0 -> depot() = 7.8125e-10      (écrêté, comme annoncé)
gamma =   0.0 -> depot() = inf
gamma =  -0.5 -> depot() = NaN
```

`Params::avertissements()` ne signale que `gamma >= 1.0`. La moitié basse du domaine exclu ne
produit ni écrêtage, ni avertissement, ni refus — **et un `depot()` NaN se propage dans les
comparaisons `partial_cmp().unwrap_or(Equal)` du tri des traces, où il détruit l'ordre
déterministe (PD1).**

### G-g — mineur

Le périmètre fait **10 846** lignes (`wc -l`), non 10 611 ; comptage antérieur aux
corrections, mais présenté comme courant.

## Ce que le bâtisseur n'a pas vu

### G1 — `accord.rs:272` : `SeuilDeQuorum::n` est public, et `tour()` indexe des tables dimensionnées à la construction

```
panicked at accord.rs:272: index out of bounds: the len is 16 but the index is 63
```

Reproduit par `q.n = 64` sur `SeuilDeQuorum::nouveau(16, …)` suivi d'un `tour()`. C'est le
motif **exact** que le rapport corrige ailleurs, dans le même fichier, **120 lignes au-dessus
du site corrigé**. `opinion`, `unanimites` et `engage` restent à 16.

### G2 — `accord.rs:272` : `SeuilDeQuorum::qualites` est public et indexé par l'opinion

```
panicked at accord.rs:272: index out of bounds: the len is 0 but the index is 0
```

Reproduit par `q.qualites.clear()` puis `tour()`.

### G3 — `propagation.rs:113` : `Rumeur::n` est public, `etat` et `compteur` sont privés et dimensionnés à la construction

```
panicked at propagation.rs:113: index out of bounds: the len is 8 but the index is 25
```

Reproduit par `r.n = 64` sur `Rumeur::nouvelle(8, Some(3))`. Le module documente pourtant
`SPEC §7, clause 4` au constructeur (`:59`, « ne jamais abandonner sur un indice hors
bornes ») — **la garde est au constructeur, pas sur le champ qui la contourne.**

### G4 — `accord.rs:412` : `ecart_a_la_validite()` rend `NaN` sur population vide

`0.0/0.0` sur `x0.len()`. C'est l'oracle armé d'EX-A51 : il rend une valeur, pas un refus, et
`NaN` comparé à un seuil est faux dans les deux sens.

### G5-G7 — les trois paniques par rétrécissement de G-d

`echantillonnage.rs:228`, `echantillonnage.rs:264`, `accord.rs:393` restent atteignables
depuis un champ public après la correction.

## Contraintes structurelles

Rien à signaler : aucune des sept méthodes de `f64` interdites, aucun `HashMap`/`HashSet` dans
le périmètre ; clippy est muet et le seul `HashSet` du dépôt est dans un commentaire de
`sim-milieu`.

*Aucun fichier du dépôt modifié : le banc de reproduction est un crate séparé sous le
scratchpad, `CARGO_TARGET_DIR` dérouté.*
