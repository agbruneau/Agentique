# M4 · scénarios & preuves de `sim-agents` — jugement du critique, tour 1

Agent en contexte neuf. Comparaison à l'aveugle contre `bancs/dt1-flottant/VERDICT.md`,
partie 1 écrite avant ouverture du dépôt. Le rapport d'audit était le document **B**.

## Verdict : **B** — le rapport d'audit

> B porte chaque affirmation avec sa preuve exécutable — sortie de test citée, sortie de
> `grep` citée, `fichier:ligne`, et un script de remesure que le lecteur peut relancer —,
> il tire la conséquence contre ses propres documents normatifs (`CLAUDE.md`, le PRD), et
> il range à part ce qu'il n'a pas corrigé avec le motif du non-correctif.

## L'écart retenu — sur le perdant (le verdict DT1)

> La pièce qui décide de la solution est donnée par **un seul** couple de bits, et les six
> autres opérations sont portées par « Même constat pour les six autres » ; et le
> retournement de `mul_add`, qui est l'argument central, ne cite aucun artefact d'aucun des
> deux passages.

**Quatrième critique consécutif à désigner le même défaut**, en contextes séparés et sans
concertation possible. C'est un constat sur la barre, pas sur le produit ; consigné, non
actionné — le mandat porte sur le code.

## Contre-épreuves : les cinq tests renforcés sont réfutables

| mécanisme cassé | test | résultat |
|---|---|---|
| `partage.rs:44` `{x}` → `{x:.9}` | `le_depot_unitaire_pose_traverse_le_lien_sans_perte` | **FAILED** — `left: Some(8.2313e-5) / right: Some(8.231290285767679e-5)`. Le garde d'origine ne voyait rien. |
| `conformite.rs:261` `.clamp(0,1)` réintroduit | `une_population_qui_ne_saccorde_jamais_rend_un_phi_c_negatif` | **FAILED** — Φ_c = 0 au lieu de −0,2 |
| `elasticite.rs` `default()` = `oscillation()` | `critere_5_loscillation_diverge_sans_aucune_panne` | **FAILED** au volet ajouté. `pannes == 0`, `amplitude ≥ 8`, `inversions ≥ 4` passent encore : **l'ancien test aurait laissé passer** |
| `gouvernance.rs:192` agrégat plafonné à 110 | `critere_1_le_budget_borne_le_client_et_pas_lagregat` | **FAILED** — l'ancienne assertion `110 > 55` passait sous ce plafond |
| `scenario_m.rs:120` graine `^ 1` | `a_curseur_au_repos_le_scenario_m_rejoue_le_scenario_b` | **FAILED** — `phi_c 0,2139 ≠ 0,1727` |

**Nuance sur le dernier.** Une première contre-épreuve — amorce `graine ^ 0x5eed` → `0x5eee` —
**n'a pas fait échouer** le test. Ce n'est pas un défaut : `stigmergie.rs:582-584` documente
que l'amorce ne sert plus qu'à `let _ = alea.bits()`. Mais la conséquence annoncée — « un
écart de câblage entre les deux chemins ne pourra plus se lire comme un effet de la
conformité » — est **plus large que ce qui est établi** : le test compare trois scalaires
agrégés, pas l'entrelacement.

## Pages : quatorze points réétalonnés indépendamment, aucun faux

`pymupdf`, 143 pages, numérotation imprimée = index PDF. Thèse A p. 25 ✓, tableau 3 p. 18 ✓,
figure 0 p. 4 ✓, thèse B p. 16 ✓, algorithme 2 p. 14 ✓, thèse D p. 26 ✓, figure 2.1c p. 28 ✓,
tableau 16 p. 84 ✓, §8.3 du traité = « Buts incompatibles » p. 124-127 ✓, glossaire p. 14 / 18 /
129 ✓, blocs E,F,G,J,L : algo 3 p. 21, fig. 5.2 p. 80, tabl. 15 p. 81, fig. 6.1 p. 91,
tabl. 13 p. 72, fig. 7.2 p. 107, tabl. 19 p. 110 ✓. Table des matières exacte sur les huit
sections annoncées.

### F0 — une provenance reste imprécise, et c'est celle qu'il vient de certifier

`scenario_m.rs:41` porte « §8.3, p. 127 (3ᵉ éd.) ; l'incise "du même geste" est reprise de la
p. 5 ». Mesuré : p. 127 lit « …la mesure **ajoute** qu'il rend tout aussi bon marché… », alors
que la formule citée dans `these` — « rend **du même geste** bon marché » — est celle de la
**p. 5** *en entier*. Ce qui vient de la p. 5 n'est pas une incise, c'est toute la proposition
principale. **L'aveu sous-déclare l'épissure.**

## Ce que le bâtisseur n'a pas vu

### F1 — `scenario.rs:468` et `:532-535` : le test ajouté contre les provenances fausses se compare à lui-même

`const BLOCS_VERIFIES: [&str; 5] = ["A","B","D","K","M"]`, et la boucle de
`les_blocs_verifies_nomment_leur_edition` itère sur les cinq mêmes littéraux ;
`assert!(BLOCS_VERIFIES.contains(&nom))` est vrai par juxtaposition et **ne peut pas échouer**.
La seule clause réfutable est `b.source.contains("3ᵉ éd.")` : **une page fausse portant la
bonne mention d'édition passe** — exactement le défaut que le test existe pour empêcher.

### F2 — `tests/sortie_phase_6.rs:136-139` : le repli « réfutable » est vide

Le test dit vérifier « que la **mesure**, elle, survit à l'effacement de la borne », par
`assert!(r.hors_dominante.0.is_finite())`. Contre-épreuve — `scenario_m.rs:144` remplacé par
`let hors_dominante_mesuree = 0.0;`, la mesure détruite :

```
running 1 test
test aucun_oracle_de_surete_ne_tombe_pendant_leffacement ... ok
```

L'audit a lu ce test, a jugé « l'aveu à sa place » et l'a laissé tel quel, sans remarquer que
le repli est vide.

### F3 — `gouvernance.rs:492` : `assert_eq!(Criticite::TOUTES.len(), 4)` sur `[Criticite; 4]`

La longueur est fixée par le type : vérité de compilation.

### F4 — `essaim.rs:88-103` et `:146` : la correction de doc n'a pas de test

La doc réécrite promet une unité par branche ; aucun test n'appelle `intervalle_max()` sur
`Perception::Voisinage`, et le seul appel assère `32` sur une valeur posée sept lignes plus haut.

## Ce qui tient

**`hors_perimetre()`, les deux sens — rien à reprocher.** Chaque entrée recoupée :
`allocation.rs:235` `let _ = alea;`, `scenario.rs:187` `let _ = p;`, `accord.rs:12` « aucun
`Registre::armer` », les trois colonnes du tableau 14 bien des `String`, `dettes` importé par
aucun fichier de `sim-viz`, aucun des six mécanismes des phases 1-5 sans chemin
`crate::<module>` hors de son fichier. Le seul manque est `cycle_de_vie`, et l'audit l'avait vu.

**NF-12 tenue.** Aucun `sleep` dans `sim-agents` ; la seule horloge murale est
`examples/banc_nf05.rs:15,38`, un banc de débit, pas un test.

**Dépôt restauré.** Les cinq mécanismes cassés pour les contre-épreuves ont été remis à
l'octet près, vérifié deux fois par égalité de l'empreinte SHA-256 du `git diff` avec la ligne
de base — une vérification qui a rattrapé un premier restaure incomplet.
