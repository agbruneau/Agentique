# M1 · `sim-core` — jugement du critique, tour 1

Rendu par un agent en contexte neuf, sans connaissance de ce que le bâtisseur
avait tenté. Comparaison à l'aveugle contre `bancs/dt1-flottant/VERDICT.md`,
partie 1 écrite avant ouverture du dépôt.

## Verdict : **A** — le rapport d'audit

> A porte la provenance sur chaque affirmation prise une par une — `fichier:ligne`,
> la commande, la sortie brute, la citation de source avec son numéro de ligne, un
> chiffre avant/après — et range huit choses non établies au même rang que les douze
> établies, en disant pour chacune ce qui trancherait. B raconte bien sa mesure et
> en tire une conséquence qui contrarie son attente (`mul_add`), mais l'essentiel de
> ce qu'il affirme est un tableau de verdicts.

## L'écart retenu — sur le perdant (le verdict DT1)

> Le tableau de parité est le cœur du document, et il ne publie qu'un seul des
> chiffres qui le fondent : `f4ec27f3f92a91ac`, pour une comparaison sur les quatorze
> et plus qu'il annonce. Les mentions « identique » et « divergent » y sont des
> étiquettes sans le hachage qui les soutient, et « Même constat pour les six autres »
> étend une donnée montrée à six données non montrées — le lecteur ne peut ni vérifier
> ligne à ligne ni repérer laquelle des lignes serait fausse ; il ne peut que refaire
> le banc en entier ou croire.

## Ce qui a tenu à la vérification

Les cinq tests neufs rejoués contre `HEAD` : les quatre sorties citées se
reproduisent **au caractère près** (`baie 1 au pas 0 : 18 machines sur 20`,
`left: 0.4678368592575487 / right: 0.4678368592575487`, `left: 7049 / right: 49999`).
Le tableau 400/400 → 204/400 se retrouve exactement, graine 11, mêmes paramètres.
86 `#[test]` avant, 91 après, aucun retiré, le seul test existant modifié est
renforcé. Citations du traité textuelles ; « 10 ms » bien absent ; les trois
lignes de PRD citées exactes. Aucune régression en aval.

## Affirmations prises en défaut

1. **A5, parenthèse sur `sim-viz`.** « `sim-viz` n'importe de `sim-core` que
   `ModeleFaute::hors_modele` et `Agregat::mention_obligatoire` » est **faux** :
   `crates/sim-viz/src/scenario_a.rs:49` porte `use sim_core::temps::Granularite;`,
   à `HEAD` comme aujourd'hui. La conclusion visée — `LIBELLE_L99` sans appelant —
   tient malgré tout.

2. **A2, « la liste redevient exacte ».** L'énumération refaite de `hors_modele()`
   (`faute.rs:473-476`) en oublie deux : `ModeleFaute::message_perdu` (`faute.rs:238`)
   et `ModeleFaute::avertissements` (`faute.rs:436`) n'ont d'appelant nulle part,
   `bancs/` compris. D'autant plus visible qu'A2 cite EX-C05 « **omission** et retard
   de message » pour justifier l'ajout de `retard_message`, et laisse dehors la
   fonction qui implante l'omission.

## Ce que le bâtisseur n'a pas vu

### C1 — `detecteur.rs:59-61` : la doc affirme une garantie de type que le type ne donne pas (PD12)

Le commentaire dit que `#[non_exhaustive]` « tient PD12 **par le type** : hors de
cette crate, la structure ne se construit pas par littéral, donc personne ne peut
fabriquer une exactitude que nul sondage ne porte ». `#[non_exhaustive]` interdit
le littéral, **pas l'affectation de champ** ; `Proprietes` est `Copy` avec quatre
champs `pub`, et `Detecteur::proprietes()` (`:191`) en rend un exemplaire par valeur.
Depuis une crate externe :

```
(a) mesuré   : suspicions=1       fausses=1 exactitude=Some(1.0) complétude=Duree(21)..Duree(31)
(a) fabriqué : suspicions=1000000 fausses=0 exactitude=Some(0.0) complétude=Duree(1)..Duree(2)
```

### C2 — `verification.rs:38-40` et `:160-187` : un verdict EX-C18 complet rendu sur zéro exécution

R8 examine ε = 0 et δ = 0, où `N` sature à `u64::MAX`. L'autre bout n'est pas
regardé. `Parametres` n'a aucune garde, ses deux champs sont `pub` et `Deserialize`.
À δ ≥ 2 — ou δ = NaN —, `libm::log(2/δ) ≤ 0`, le cast sature à 0, et
`Campagne::conclure()` traverse ses deux gardes :

```
(c) δ=2 → N=0 ; conclut sans exécution : « aucune violation observée en 0 exécutions »
```

C'est la formulation arrêtée d'EX-C18, avec son autorité, sur un budget de zéro.
Ailleurs dans la même crate, un champ public désérialisé est gardé pour moins que
ça — `Partition::avancer`, `tirer_pannes`, `Granularite::tics_depuis_ms`,
`Detecteur::nouveau`.

### C3 — `moteur.rs:281-304` : la préséance annoncée n'est tenue que sur un budget des trois

Le commentaire de `suivant()` écrit : « Et avant le budget : une exécution qui viole
au dernier événement de son budget doit rapporter la violation, pas l'épuisement. »
`arreter_sur_violation()` est bien placé avant `BudgetEvenements` (`:301`), mais
**après** `Arret::Demande` (`:281`) et `Arret::BudgetTemps` (`:285`). Une violation
**déjà enregistrée** est donc enterrée par les deux autres :

```
(d)     arrêt rapporté : Some(BudgetTemps) (violations enregistrées : 1)
(d bis) arrêt rapporté : Some(Demande)
```

Plus dur que R5, que le rapport relève : là, la violation n'existe pas encore ; ici
elle est au registre et l'arrêt la tait. EX-C09 veut l'arrêt à l'instant de la violation.

### C4 — `faute.rs:452-458` : le correctif A1 change le sens de deux grandeurs et laisse le seuil calibré sur l'ancien

`avertissements()` teste `crash_machine + crash_baie + crash_centre > 0.1`. Avant A1,
les trois taux avaient de fait le même dénominateur — la machine. Depuis A1,
`crash_baie` est par baie et `crash_centre` par centre : la somme additionne des
probabilités de dénominateurs différents. Le seuil **sous-avertit dans le sens
grave** — un centre unique à `crash_centre = 0,09` vide toute la population à 9 %
des pas sans rien déclencher. C'est la moitié `[U]` d'EX-C06, rendue fausse par la
correction elle-même.

### C5 — `service.rs:25-29`, `:62`, `:171-176` : la faute de provenance d'A3, un fichier plus loin

Le §2.2 du traité (`Traité.md:582`) dit « de l'ordre de trois cents mots, soit
**quelques milliers d'octets** […] OTP 29.0.5 annonce **327** mots à son guide
d'efficacité […] et **338** à sa page de mémoire ; l'écart est explicable, et **il
reste la meilleure raison de ne rien gager sur le chiffre exact** ». Le code retient
327, laisse tomber 338 et la mise en garde, et en dérive « 2 616 octets » — chiffre
**absent du traité** (0 occurrence). Le test `le_cout_dun_agent_retrouve_les_chiffres_du_traite`
épingle `assert_eq!(c.octets(), 2_616)` : il fixe une précision que la source refuse
explicitement de donner, sous un nom qui affirme le contraire (F2, NF-15).

### C6 — multiplications nues sur champs publics

`detecteur.rs:184` (`periode.0 * (seuil − 1)`), `service.rs:53` et `:58`
(`mots * octets_par_mot` puis `× n`), dans une crate qui note deux fois
(`temps.rs:90-92`, `famille.rs:96-98`) que le profil release ne pose pas
`overflow-checks` et qui sature partout ailleurs délibérément.

---

*Le critique n'a rien modifié dans le dépôt : mesures faites sur copies sous
`%TEMP%`, `CARGO_TARGET_DIR` hors du chemin accentué.*
