# M2 · `sim-milieu` — jugement du critique, tour 1

Agent en contexte neuf. Comparaison à l'aveugle contre `bancs/dt1-flottant/VERDICT.md`,
partie 1 écrite avant ouverture du dépôt.

## Verdict : **A** — le rapport d'audit

> Le document A fait porter à chaque affirmation soit un `fichier:ligne` avec la
> citation adverse en regard, soit une commande et sa sortie, et il pousse jusqu'à la
> contre-épreuve — retirer le correctif, montrer le test qui tombe —, seule forme qui
> établit qu'un test garde quelque chose.

## L'écart retenu — sur le perdant (le verdict DT1)

> Le fait pivot du document — `f64::mul_add` divergeait au premier passage du banc et
> coïncide au second — est le seul dont aucune sortie n'est reproduite : les hachages
> du premier passage ne figurent nulle part, et la commande de rejeu ne peut par
> construction reproduire que l'état courant. L'interdiction la mieux argumentée du
> document repose donc sur la mesure la moins vérifiable.

## Ce qui a tenu

Trois commandes rejouées (61 tests verts, clippy `deny` propre, `cargo doc` propre).
Contre-épreuve de §A3 reproduite à l'identique. Les cinq pages de §B1 reproduites par
`pypdf` : **14, 26, 26, 65, 96** contre 13, 22, 21, 49, 71 annoncés dans le code ;
PDF à 143 pages, page de titre « 15 août 2026 — troisième édition ». Citations du
§8.1 et de M4 retrouvées mot pour mot. Passage de 56 à 61 tests confirmé par
`git show HEAD`. Aucune assertion retirée du diff ; deux ajoutées.

## Affirmations prises en défaut

1. **« Les dix entrées existantes sont toutes exactes » (§A4).** Il y en avait **neuf**.
   `git show HEAD:…/lib.rs` donne neuf chaînes ; la liste livrée en compte treize
   (neuf + quatre ajoutées). Les neuf sont bien exactes — reprises une à une contre
   les appelants réels — mais le document se trompe sur le cardinal d'une liste dont
   il dit l'avoir parcourue entrée par entrée.

2. **Le bloc de sortie collé en §A3 ne se rejoue pas tel quel.** Sur l'arbre livré,
   filtrer sur `m10` donne `1 passed; 1 failed; … 59 filtered out` (2 + 59 = 61), non 57.
   Les deux lignes de verdict par test sont exactes au caractère près ; le bloc décrit
   un arbre à 59 tests, antérieur à celui dont le même paragraphe dit « les 61 tests
   passent ».

## Ce que le bâtisseur n'a pas vu

### D1 — `groupe.rs:358` : l'oracle de sûreté d'EX-M23 a un prédicat inatteignable, et rien ne le dit

`verifier_surete` cherche un propriétaire qui aurait quitté le groupe. Mais `attribution`
et `membres` sont privés, et leurs seuls scripteurs sont `attribuer` (`:252`, qui n'assigne
que des membres courants) et `retirer_membre` (`:345`, qui met `None` sur les partitions
du partant). **Aucune suite d'appels publics ne peut laisser un non-membre propriétaire** :
la branche `registre.violer(UN_SEUL_PROPRIETAIRE, …)` est morte.

C'est la situation que la crate nomme explicitement ailleurs — pour M2/M3 (`journal.rs:694-708`)
et R2 (`replication.rs:173-179`) : « l'oracle reste armé pour que sa ligne figure au
catalogue, non pour qu'il se déclenche ». Ici la doc affirme au contraire que l'oracle
« vérifie **en outre** qu'aucun propriétaire n'est un non-membre », et le test
`une_partition_na_quun_proprietaire` (`:546`) **passerait avec un corps vide** : il ne
fait jamais partir personne. Contre NF-10.

### D2 — `historique.rs:75` : le refus « non négociable » du régime `NonVerifiable` se contourne par une seconde voie publique

Le `//!` (l. 13-18) dit que `poids` « refuse de rendre un poids dans ce régime, au lieu
de le rendre dégradé ». Mais `Historique::compte` (l. 126) rend un `Compte` par valeur et
`Compte::fiabilite` (l. 75) est publique : même rapport, sans refus, **et sans compter la
consultation** que la doc dit « payée par le consultant, que la réponse lui serve ou non ».
`Historique::identites` (l. 170) offre la même voie sur toute la population.

```
h.poids(qui(2))              -> Err(REFUS_NON_VERIFIABLE)
h.compte(qui(2)).fiabilite() -> Some(1.0)
h.consultations()            -> 1        // la voie détournée ne paie rien
```

### D3 — `lib.rs:94-96` : des astérisques d'emphase deux entrées sous le commentaire qui les interdit

Le commentaire `lib.rs:77-78` dit : « Sans astérisques d'emphase […] : egui n'a pas
d'analyseur Markdown et rendrait les deux littéralement. » L'entrée écrit « plan de
contrôle `**en exécution**` ». Elle est affichée par `sim-viz/src/lib.rs:889` via
`section` → `puce`, qui pose un `egui::RichText` sans analyse Markdown : l'onglet
« Limites » affiche les astérisques.

### D4 — `journal.rs:752` : `verifier_m10` compare les charges utiles par `==` sur `f64`, et fabrique une violation sur NaN

`Milieu::ecrire` (l. 402) accepte n'importe quel `f64` sans garde. Sans aucun compactage,
sur un journal identique à lui-même :

```
partition 0 : la clé 1 lisait NaN avant le compactage et lit NaN après
```

Latent aujourd'hui — `verifier_m10` n'a aucun appelant, ce que la liste déclare — mais
c'est précisément la borne que le correctif du compactage devait garder.

### D5 — `groupe.rs:161` : `duree_orpheline` ne compte pas l'orphelinat initial, alors que l'oracle le voit

Le champ est documenté « durée cumulée pendant laquelle des partitions ont été sans
propriétaire » et `nouveau` (l. 176) dit « toutes orphelines », mais laisse
`orphelines_depuis` à `None` : de la création au premier `entrer`, rien n'est cumulé.
Mesuré : `suivre_vivacite` ouvre une attente à `Instant(0)`, l'entrée d'un membre à
`Instant(500)` la satisfait, et `duree_orpheline` vaut `Duree(0)`. **Deux mesures du même
fait se contredisent.**

## Constats mineurs, non filtrés

- `quota.rs:140` — `PrixCroissant` facture `1 + pente × (preneurs − 1)` sur l'état
  *d'avant* : le deuxième preneur distinct paie le prix nominal, alors que la doc annonce
  « facteur ajouté au prix par preneur au-delà du premier ». Le commentaire du test
  (`:244`) documente le code, pas la doc.
- `journal.rs:457` — `Milieu::valider` appelé deux fois sur la même `Ecriture` rend `true`
  les deux fois, facture deux `tours_journal` et pousse un doublon dans
  `latences_durabilite` : **biaise le ℓ₉₉ d'EX-M09**. Aucune garde, aucune mention.
- `groupe.rs:143` — `Groupe::p` est un champ public alors que `attribution` et
  `orphelines_depuis` sont dimensionnés depuis `p` à la construction : le modifier après
  coup désaccorde `parallelisme_utile` de `debit_instantane`, aucun invariant ne le rattrape.

## Contraintes structurelles — rien à signaler

Aucun `HashMap`/`HashSet`, aucune des sept méthodes interdites de `f64` (clippy en `deny`
le confirme), le mélange de `lire_multi` tire de l'unique `Alea` semé, et PD14 tient — le
seul lecteur de `Enregistrement::valeur` est `verifier_m10`, qui compare une préservation.
C'est aussi là que loge D4.
