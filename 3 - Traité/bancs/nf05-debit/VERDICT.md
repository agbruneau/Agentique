# NF-05 — Débit de simulation : mesure et verdict

**NF-05 n'est pas atteinte, et l'écart n'est pas un défaut d'optimisation : il
est structurel au mécanisme mesuré.** La cible est ≥ 10³ secondes simulées par
seconde-cœur à n = 1 000, p = 16. Le mesuré est **de l'ordre de 10 à 15 selon la
charge de la machine**, soit presque deux ordres de grandeur en dessous.

**Les deux colonnes reproductibles sont `s simulées` et `retard max`** : elles ne
dépendent que de la graine et du budget, et se retrouvent au chiffre près à tout
rejeu. Le débit, lui, se divise par une durée murale ; il varie d'un passage à
l'autre sur la même machine, et le verdict ne repose pas dessus. Un rejeu de
l'audit a rendu 12,9 et 10,8 là où le tableau ci-dessous porte 15,2 et 13,2, avec
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

## La seconde cause, elle, est corrigeable — et elle est en phase 2

En phase 1, le débit chutait d'un facteur 10 entre 200 000 et 1 000 000
d'événements à n constant. La raison était visible dans la colonne « retard
max » : **le journal croissait sans borne**, faute de rétention.

**C'est corrigé, et la mesure le montre** : la chute vaut maintenant un facteur
**1,1** (15,2 → 13,2). Le retard maximal, lui, reste du même ordre — la
rétention borne le journal, elle ne fait pas rattraper les agents.

Ce qui n'a pas changé, et ne changera pas, c'est l'ordre de grandeur :
Θ(n²) reste Θ(n²). C'est ce qui sépare les deux causes.

## Ce que la mesure établit quand même

**Les scénarios tournent confortablement.** À n = 64 — le défaut des scénarios
A et B — le débit est de **599** s simulées par seconde-cœur, et une exécution
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
