# NF-05 — Débit de simulation : mesure et verdict

**NF-05 n'est pas atteinte, et l'écart n'est pas un défaut d'optimisation : il
est structurel au mécanisme mesuré.** La cible est ≥ 10³ secondes simulées par
seconde-cœur à n = 1 000, p = 16. Le mesuré est **de l'ordre de 20 à 25 selon la
charge de la machine** — 10 à 15 avant la phase 2 de [`audit.md`](../../audit.md),
remesuré ci-dessous —, soit un ordre et demi de grandeur en dessous.

**Les deux colonnes reproductibles sont `s simulées` et `retard max`** : elles ne
dépendent que de la graine et du budget, et se retrouvent au chiffre près à tout
rejeu. Le débit, lui, se divise par une durée murale ; il varie d'un passage à
l'autre sur la même machine, et le verdict ne repose pas dessus. Un rejeu de
le banc a rendu 12,9 et 10,8 là où le tableau ci-dessous porte 15,2 et 13,2, avec
`s simulées` et `retard max` identiques — c'est exactement la distinction que le
verdict DT1 impose pour un chiffre qui dépend de la machine de construction.

Remesuré à la clôture de la phase 5, sur le scénario B,
`x86_64-pc-windows-gnu`, profil `release`. Banc :
`crates/sim-agents/examples/banc_nf05.rs`.

| n | p | événements | s simulées | s-cœur | débit | retard max |
|---|---|---|---|---|---|---|
| 64 | 8 | 200 000 | 80,17 | 0,13 | **599** | 121 |
| 256 | 16 | 200 000 | 20,03 | 0,33 | **61** | 490 |
| 1 000 | 16 | 200 000 | 5,13 | 0,34 | **15,2** | 71 546 |
| 1 000 | 16 | 1 000 000 | 25,65 | 1,94 | **13,2** | 356 061 |

**La mesure de la phase 1 est périmée d'un facteur cinquante**, et elle a été
citée telle quelle dans cinq fichiers pendant quatre phases. Elle donnait
0,2 à 2,0, et 29,6 à n = 64. Ce qui a changé n'est pas le mécanisme — il est
toujours en Θ(n²) — mais la seconde cause diagnostiquée ci-dessous, qui a été
corrigée entre-temps. Un verdict de banc se remesure quand le code qu'il mesure
change ; ne pas l'avoir fait est le défaut, pas le chiffre.

## Remesure du 4 septembre 2026, après la phase 2 de `audit.md`

Le chemin chaud du cycle d'agent a été réécrit (commit `3548faa`) : le journal
se lit **par plages** au lieu d'être copié enregistrement par enregistrement, et
les sept grandeurs dérivées des paramètres sont calculées une fois à la
construction au lieu d'une fois par cycle. Même machine, même profil, même banc,
même graine.

| n | p | événements | s simulées | s-cœur | débit | retard max |
|---|---|---|---|---|---|---|
| 64 | 8 | 200 000 | 80,17 | 0,09 | **865** | 121 |
| 256 | 16 | 200 000 | 20,03 | 0,17 | **115** | 490 |
| 1 000 | 16 | 200 000 | 5,13 | 0,21 | **25,0** | 71 546 |
| 1 000 | 16 | 1 000 000 | 25,65 | 1,28 | **20,1** | 356 061 |

**Les deux colonnes reproductibles sont identiques au tableau précédent**, `s
simulées` et `retard max`, au chiffre près et sur les quatre lignes. C'est ce
qui autorise à lire la colonne `s-cœur` comme un gain et non comme du bruit : le
travail simulé est **le même**, et il coûte à peu près deux fois moins.

**Le verdict ne change pas.** Un facteur 1,9 sur une cible manquée d'un facteur
soixante-dix ne la rapproche pas : il faudrait encore quarante fois mieux, et le
Θ(n²) est intact. Ce que la remesure établit est plus étroit, et vaut d'être
écrit : la part du débit qui tenait à l'**implantation** était de moitié, et le
profil de la phase 0 l'a localisée — 2 940 ns par cycle passés à copier des
enregistrements du journal vers un tampon d'agent, soit 96 % du coût de lecture.
⚠ *L'audit avait estimé cette copie à environ 1 µs par cycle et le gain à 20 à
35 % ; la mesure l'a corrigé dans les deux sens. Une estimation d'audit n'est
pas une mesure, et c'est le profil qui tranche.*

## Pourquoi la cible est hors d'atteinte pour ce mécanisme

Le calcul se fait sans profileur. À n = 1 000 et T = 50 ms, une seconde simulée
contient 20 000 cycles d'agent. Atteindre 10³ s simulées/s-cœur exigerait donc
**2 × 10⁷ cycles par seconde-cœur**, soit 50 ns par cycle — pour un cycle qui
comprend une lecture d'intervalle, la mise à jour de φ sur m ressources, un
tirage pondéré, une écriture et deux événements de file. Aucune implantation ne
tient cela ; ce n'est pas une question de constante.

La cause de fond est le mécanisme lui-même, pas le code : **chaque agent lit ce
que toute la population écrit**. Le coût par unité de temps simulé est donc en
Θ(n²), et c'est une propriété de la stigmergie sur journal partagé, exactement
celle que le scénario C mesure sous la forme du terme σ de l'USL.

## La seconde cause, elle, était corrigeable — et elle l'a été

En phase 1, le débit chutait d'un facteur 10 entre 200 000 et 1 000 000
d'événements à n constant. **C'est corrigé, et la mesure le montre** : la chute
vaut un facteur **1,1** (15,2 → 13,2, et 25,0 → 20,1 à la remesure).

**Ce qui l'a corrigé n'est pas la rétention.** ⚠ *Du 17 août au 4 septembre 2026,
cette section a attribué le gain à la rétention — « le journal croissait sans
borne, faute de rétention » — et le §0.1 du PRD l'a repris. C'était faux, et le
code le disait.* `Milieu::appliquer_retention` **n'a aucun appelant hors test** :
`sim_milieu::hors_perimetre()` le déclare — « rétention, compactage, groupe et
plan de contrôle sont implantés, testés, et appelés par aucun scénario » —, et le
journal du scénario B croît toujours sans borne, ce que la colonne « retard max »
confirme à 356 061 sur un million d'événements. Une rétention qui ne tourne pas
ne borne rien.

Ce qui a réellement supprimé le facteur 10 est la **recherche binaire** de
`Partition::valider` et de `Milieu::lire`, entrée au dépôt le 14 août 2026
(`6ac7170`), et le rustdoc de `journal.rs` la date et la chiffre : « un balayage
linéaire rendrait le coût d'une exécution quadratique en le nombre d'écritures,
ce que NF-06 interdit — et c'était le cas ici, mesuré à 64 ms, 316 ms puis
1 405 ms pour n = 20 k, 40 k, 80 k validations ». Le journal croît toujours ; ce
qui a cessé de croître est le **coût d'un accès** à ce journal.

Le verdict était juste sur le fait et faux sur la cause, et F2 traite cela comme
une provenance fausse plutôt que comme une imprécision : l'attribution désignait
un mécanisme **hors périmètre** comme la preuve d'un gain réellement mesuré.

Le retard maximal, lui, reste du même ordre : rien ici ne fait rattraper les
agents. Et ce qui n'a pas changé, ni ne changera, c'est l'ordre de grandeur —
Θ(n²) reste Θ(n²). C'est ce qui sépare les deux causes.

## Ce que la mesure établit quand même

**Les scénarios tournent confortablement.** À n = 64 — le défaut des scénarios
A et B — le débit est de **865** s simulées par seconde-cœur — 599 avant la
phase 2 —, et une exécution
complète du scénario B prend une fraction de seconde. Rien dans la phase
1 n'est bloqué par ce constat.

**Ce qui est bloqué est l'usage à n = 12 500**, celui que le traité prend pour
exemple d'exploitation. L'incertitude 3 du §10 le prévoyait : *« Le régime de n
où la simulation reste interactive […] il n'est pas acquis qu'une visualisation
à 30 images/s tienne à cette échelle. »* La réponse mesurée est non, et elle
arrive plus tôt que prévu : c'est le **moteur**, pas le rendu, qui plafonne.

## Ce qu'il faudrait pour changer le verdict

Trois leviers, par ordre d'effet décroissant, et aucun n'est un travail
d'optimisation :

1. **Réviser la cible.** NF-05 est étiquetée [M] et déclarée « cible
   d'ingénierie, pas une mesure du traité » (§8.2, note de méthode). Une cible
   posée sans mesure préalable, que la mesure contredit de quatre ordres de
   grandeur, est une cible à refaire — sur la mesure, comme DT1.
2. **Le mode champ moyen** (RQ5), qui est l'échappatoire que le traité fournit
   lui-même, et dont la portée est bornée par le §10 : admissible pour
   dimensionner la population, interdit dès que l'unicité d'un propriétaire est
   en jeu.
3. **La rétention** (phase 2), qui supprime la dégradation en fonction de la
   durée sans toucher à celle en fonction de n.

## Ce que ce banc ne mesure pas

- **NF-07**, l'interactivité du rendu à 30 images/s. Ce banc ne porte que sur le
  moteur ; NF-07 demande un navigateur en avant-plan avec une horloge d'images,
  et reste non mesurée.
- **Le débit d'un autre scénario.** Le scénario A ne simule pas de population à
  chaque pas ; sa comparaison est analytique et son coût sans rapport.
- **Le temps mural d'un système réel.** Le temps simulé n'est pas le temps
  mesuré, et aucun chiffre de ce banc ne prédit la latence d'un déploiement
  (§8.3).

## Rejouer

```bash
cargo run -p sim-agents --example banc_nf05 --release
```
