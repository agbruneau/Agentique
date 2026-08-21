# M2 — `crates/sim-milieu`, audit du 17 août 2026

Dix-neuf anomalies relevées, seize corrigées, trois consignées sans correctif.

> **État de ce document.** Les chiffres et les sorties de §A à §C sont ceux du
> **tour 1**. Les `fichier:ligne` ont en revanche été repris pour désigner le
> **code livré**, et non l'état trouvé. Le tour 2, à la fin, porte les correctifs
> du jugement du critique et les sorties de l'arbre livré — **68 tests**.

La suite de la crate passe de **56** à **61** tests : deux couvrent un oracle qui
n'en avait aucun, un couvre une violation que la fréquence de sondage fabriquait,
un fixe l'unité de tour d'EX-M22, un fixe l'exception du seuil de concentration.

Les trois commandes, lancées dans un `CARGO_TARGET_DIR` privé — cinq agents
écrivaient dans `target/` en parallèle, et l'éditeur de liens y perdait des
objets en cours de lien :

```
$ cargo clippy -p sim-milieu --all-targets --release
    Finished `release` profile [optimized] target(s) in 0.14s

$ cargo test -p sim-milieu --release
running 61 tests
test result: ok. 61 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

$ cargo doc -p sim-milieu --no-deps
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.13s
   Generated .../doc/sim_milieu/index.html
```

`cargo check -p sim-agents --all-targets --release` passe après les deux
changements de signature (§A6, §A11) : aucun appelant hors crate.

---

## A. Corrigées

### A1 — `groupe.rs:92` — `Protocole::tours()` rendait des aller-retours

**Preuve.** EX-M22 : « **L'unité de tour est celle de l'annexe B.1** ». L'annexe
B.1 du PRD fixe la convention de référence : « §6.1 : deux envois indépendants
comptent pour un tour, deux envois enchaînés en comptent deux — **un aller-retour
vaut 2 tours** ; c'est la convention de référence du PRD ». L'annexe B chiffre en
conséquence : « Rééquilibrage, protocole d'origine […] 4n messages et 2
aller-retours = **4 tours** (voir B.1) » et « Rééquilibrage coopératif […] 4
aller-retours = **8 tours** sous la convention retenue en B.1 ».

Le code rendait 2 et 4 — les aller-retours —, et son propre commentaire l'écrivait
(« /// Aller-retours en série »), sous un nom qui dit *tours*. Le compte affiché
était donc la moitié du compte imposé pour les deux protocoles à barrière, et il
alimentait `CoutChangement::tours` et `Groupe::tours`, tous deux documentés
« aller-retours » alors qu'EX-M22 exige des tours.

**Changement.** `Protocole::aller_retours()` rend 2 / 4 / 0 ; `Protocole::tours()`
rend 4 / 8 / 1, avec la provenance de la conversion. Les deux champs cumulés sont
redocumentés. Test ajouté :
`les_tours_sont_comptes_dans_la_convention_de_lannexe_b1`, plus une assertion de
tours dans `lentree_dans_un_groupe_coute_theta_n`.

**Conséquence.** Le coût de coordination d'EX-M17 et d'EX-M22 est enfin dans
l'unité que le PRD impose, et les tours ne peuvent plus être confondus avec les
phases — le test l'assertit pour les trois protocoles.

### A2 — `groupe.rs:420` — `suivre_vivacite` empilait une attente par sondage

**Preuve.** `sim_core::oracle::Registre::attendre` pousse une attente à chaque
appel, et `satisfaire` « retire la plus ancienne attente de cet oracle » — une
seule. `suivre_vivacite` appelait `attendre` à chaque invocation tant qu'une
partition était orpheline. Dix sondages pendant une même période d'orphelinat
ouvraient dix attentes ; le retour d'un propriétaire en refermait une, et les neuf
autres échoyaient plus tard en violations de `TOUTE_PARTITION_A_UN_PROPRIETAIRE`,
à une date où la condition était remplie. Le nombre de violations d'EX-M23 `[L]`
dépendait donc de la fréquence du sondage, pas de la trajectoire.

**Changement.** Drapeau privé `Groupe::attente_ouverte` ; la méthode passe à
`&mut self` et devient idempotente. Doc corrigée : elle disait « arme l'attente
pour **chaque partition orpheline** » alors qu'elle en armait une par *appel*.
Test ajouté : `sonder_la_vivacite_a_repetition_nempile_pas_les_attentes`, qui
sonde dix fois, satisfait, puis appelle `echoir(Instant(1_000_000))` et exige zéro
violation.

**Conséquence.** L'oracle de vivacité d'EX-M23 mesure une propriété et non un
rythme d'appel. Sans correctif, câbler `groupe` dans un scénario aurait produit
des violations fabriquées.

### A3 — `journal.rs` — l'oracle EX-M10 n'avait aucun test

**Preuve.** La doc de la constante `M10` écrit : « C'est la seule propriété qu'un
compactage puisse réellement casser […] Elle ne l'était pas : elle n'existait que
comme chaîne d'affichage, et **un défaut mesuré sur 36,5 % des compactages tirés
au sort laissait la suite de tests verte**. » L'oracle a été écrit pour couvrir ce
défaut ; aucun test de la crate n'appelait `Milieu::verifier_m10`. Rien ne gardait
donc la borne de durabilité de `compacter`, c'est-à-dire le correctif lui-même.

**Changement.** Deux tests. `m10_le_compactage_preserve_letat_final_lisible`
construit le cas exact — deux clés durables, un trou non durable, un successeur
durable derrière le trou — et exige M4 **et** M10 sans violation.
`m10_detecte_la_perte_dun_etat_final_lisible` fabrique le journal qu'un compactage
non borné produirait, constate que **M4 ne voit rien** et que M10 lève deux
violations.

**Contre-épreuve exécutée.** Frontière retirée (`let frontiere = p.journal.len();`),
rejouée sur **l'arbre livré** — le bloc collé ici au tour 1 décrivait un arbre
antérieur à 59 tests, alors que le même paragraphe en annonçait 61 :

```
$ cargo test -p sim-milieu --release -- m10
test journal::tests::m10_ne_fabrique_pas_de_violation_sur_une_charge_utile_nan ... ok
test journal::tests::m10_detecte_la_perte_dun_etat_final_lisible ... ok
test journal::tests::m10_le_compactage_preserve_letat_final_lisible ... FAILED
test result: FAILED. 2 passed; 1 failed; 0 ignored; 0 measured; 65 filtered out; finished in 0.00s
```

2 + 1 + 65 = 68, le compte de l'arbre livré (voir Tour 2). Frontière remise : les
68 tests passent.

**Conséquence.** Le seul correctif de la crate dont la doc dit qu'il a été trouvé
par la mesure est désormais tenu par un test qui échoue si on le retire.

### A4 — `lib.rs:55` — `hors_perimetre()` déclarait absent moins que ce qui l'est

PD6 : « une liste périmée déclare absent ce qui est livré, ce qui est le mensonge
symétrique ». Vérification faite dans les deux sens, par recherche des appelants
hors crate. Les **neuf** entrées existantes sont **toutes exactes**. Quatre manquaient, ce qui
porte la liste livrée à treize :

1. **Le module `format` en entier.** `Producteur` (EX-M12) et `CoutLot` (EX-M16)
   n'ont aucun appelant : aucun doublon n'est rejeté et aucun coût par
   enregistrement n'est facturé dans un résultat. L'entrée existante ne couvrait
   que le surcoût d'octets (EX-M11).
2. **`Milieu::partition_de`.** Aucun appelant hors test : `ecrire` range
   l'enregistrement dans la partition que l'écrivain nomme (`stigmergie.rs:1050`
   passe `self.ressources[j].partition`). La fonction de clé h du §1.2 ne décide
   de rien, et la concentration observée vient du réglage du scénario.
3. **Le refus d'oracle d'EX-M20.** EX-M20 : « tout oracle dont l'horizon dépasse R
   est **refusé au chargement** ». `Milieu::verifier_horizon` et la structure
   `Retention` n'ont aucun appelant ; `appliquer_retention` reçoit sa fenêtre en
   paramètre. R n'existe donc dans aucune exécution comme la « grandeur unique à
   trois rôles » qu'EX-M20 décrit, et aucun chargement ne refuse quoi que ce soit.
4. **Le temporisateur d'ISR en exécution (EX-M14).** `Isr::avancer` n'a d'appelant
   que ses tests : `scenario_d.rs:166` appelle `retirer_pour_retard(2)` à la main.
   Or `hypotheses.eprouver(REGLAGE_LAG, …)` ne vit que dans `avancer`, tandis que
   `scenario_d.rs:116` appelle `declarer_hypotheses`. L'hypothèse forte du
   registre EX-C12 est donc **déclarée sans jamais être éprouvée**, quelle que
   soit la trajectoire ; le démenti qu'EX-M14 annonce — « sous saturation,
   l'exclusion frappe des suiveurs vivants » — n'est produit que par un test
   unitaire.

**Conséquence.** L'onglet « Limites » de `sim-viz` (`lib.rs:900`) affiche cette
liste telle quelle. Les quatre mécanismes y figurent maintenant au même rang que
ceux qui tournent.

### A5 — `quota.rs:9` — citation du §8.1 réécrite et présentée comme citation

**Preuve.** Le bloc `> ` du module portait : « Le seul levier structurel, et il
appartient au milieu, consiste à rendre coûteuse la décision majoritaire plutôt
qu'à espérer sa dispersion : quota par ressource… ». Le traité, §8.1, écrit :
« Le seul levier structurel appartient au milieu : rendre coûteuse la décision
majoritaire plutôt qu'espérer sa dispersion — quota par ressource, prix croissant
avec le nombre de preneurs, refus d'écriture au-delà d'un seuil de
concentration. » La phrase avait été reformulée dans un bloc de citation.

La ligne qui l'introduisait était fausse en outre : elle prêtait aux **trois**
leviers de diversification ce que le traité dit du **troisième** seul (« n'agit
que sur la marge de la distribution, non sur son mode »), alors qu'il écrit du
premier qu'il « supprime la cause principale ».

**Changement.** Citation restituée mot pour mot avec sa section ; la phrase
d'introduction nomme les trois leviers et attribue la restriction au bon.

### A6 — `controle.rs:169` — conversion de temps ad hoc, tronquante et non gardée

**Preuve.** `Duree((duree_ms * granularite_par_ms as f64) as u64)` double la
conversion que `sim_core::temps::Granularite::tics_depuis_ms` porte, en perdant
ses deux garanties, que sa propre doc énonce : l'arrondi **au tic supérieur** et
l'assertion sur `is_finite() && >= 0.0`, motivée ainsi — « sans cette garde, un
NaN […] devient `Duree(0)`, c'est-à-dire “immédiat” […]. Les deux se taisent ; il
vaut mieux qu'ils parlent. » Un délai d'élection de 150,9 ms devenait 150 tics ;
un réglage non fini, une indisponibilité nulle et muette.

**Changement.** La méthode prend une `Granularite` et appelle `tics_depuis_ms`.
Le test `sous_condition_tenue_les_elections_aboutissent` vérifie désormais que la
fenêtre rendue tient dans 150–300 ms (§4.2), au lieu de ne rien dire de sa valeur.

### A7 — `groupe.rs:228` — `Duree(delai_session.0 * 2)` hors de l'arithmétique saturante

**Preuve.** `Cargo.toml` racine ne pose pas `overflow-checks` sur le profil
release, et `sim_core::temps` documente pourquoi ses opérateurs saturent : « un
enroulement ferait **reculer** l'horloge […] et il serait silencieux ». Le produit
brut sur `u64` enroulé aurait rendu une borne de vivacité **plus courte** que le
délai de session, donc une violation d'EX-M23 `[L]` fabriquée par l'arithmétique.

**Changement.** `self.delai_session + self.delai_session`, qui passe par
l'addition saturante de `Duree`.

### A8 — `controle.rs:63` — le champ `elections_perpetuelles` documentait autre chose que son calcul

**Preuve.** Doc : « Élections déclenchées alors qu'une élection était **en
cours** ». Le code incrémente sur `diffusion_ms >= duree_ms`, et rien dans
`PlanDeControle` ne représente une élection « en cours ». Deux définitions
distinctes pour un même compteur.

**Changement.** La doc dit ce qui est compté — une élection dont la diffusion n'a
pas tenu dans son délai —, et dit aussi que rien ne relance : c'est l'appelant qui
rouvre, et aucun scénario ne le fait.

### A9 — `controle.rs:115` — `decider` documentait un Ω(n) sur la mauvaise population

**Preuve.** Doc : « **Ω(n) messages**, où n est la taille du quorum ». Le code
facture `self.k + n_essaim`. DT7 et le §4.2 chiffrent Ω(n) sur l'**essaim** —
c'est la thèse même du chapitre : « le plan de contrôle le paie pour tout le
monde ». Le test `une_decision_coute_omega_n` (`grand > petit * 10`) ne passe que
grâce au terme d'essaim, celui que la doc niait.

**Changement.** La doc nomme l'essaim, donne le coût rendu (`k + n`) et sa
provenance.

### A10 — `journal.rs:59` et `journal.rs:68` — deux champs documentaient ce que le code ne tient pas

**Preuve.** (a) `Enregistrement::cle` : « Elle décide de la partition ». Faux :
`Milieu::ecrire` prend la partition en paramètre et ne consulte jamais
`partition_de`. (b) `Enregistrement::octets` : « Ce qui est compté **ici** est la
taille annoncée par l'écrivain ». Faux : aucun chemin ne permet d'annoncer une
taille, `ecrire` passe `OCTETS_DEFAUT` et c'est le seul appelant de
`Partition::ajouter`.

**Changement.** Les deux docs disent l'état livré, avec renvoi à
`hors_perimetre()`. Le paramètre `octets` de `Partition::ajouter` est supprimé :
il ne recevait qu'une constante, et sa présence laissait croire que le surcoût de
format d'EX-M11 pouvait être facturé là.

### A11 — chemins de panique non documentés

**Preuve.** `Milieu::partition` portait une section `# Panics` ; les six autres
entrées indexant `self.partitions[…]` n'en avaient pas — `ecrire`, `valider`,
`lire`, `lire_multi`, `compacter`, `appliquer_retention`. `Isr::nouvelle` assertit
`k ≥ 1` et `1 ≤ m ≤ k` sans le dire. `Latence::tirer` panique dans
`tics_depuis_ms` sur un réglage négatif ou non fini, atteignable par
désérialisation d'un scénario : `Latence` dérive `Deserialize` et ses champs sont
publics, donc les constructeurs ne sont pas un passage obligé.

**Changement.** Sections `# Panics` sur les huit, chacune disant pourquoi
l'arrêt vaut mieux que le silence. Aucun comportement modifié.

### A12 — `journal.rs:6` — la citation de M4 était tronquée de sa première moitié

**Preuve.** Traité, §1.2 : « **M4** : l'ordre est maintenu en toute circonstance
**et** le compactage ne réordonne jamais, il ne fait que supprimer ». Le bloc
`> ` du module ne portait que la seconde moitié — l'abrégé d'EX-M04, cité comme
s'il venait du traité. La moitié perdue est celle que `appliquer_retention` doit
tenir autant que `compacter`.

**Changement.** Citation complète, avec la note qui dit que le PRD l'abrège.

### A13 — provenances internes fausses ou incomplètes

- `replication.rs:1` déclarait implanter **EX-M23**. EX-M23 porte sur la
  propriété d'une partition dans un groupe de consommation : c'est `groupe.rs`.
  Corrigé, avec le renvoi.
- `lib.rs:12` rangeait **EX-M16** (coût d'écriture d'un lot) dans le groupe de
  consommation ; il vit dans `format`. Corrigé.
- `journal.rs:1` énumérait ce qui vit **ailleurs** sans dire que la rétention
  (EX-M10, EX-M20), les coûts (EX-M13) et l'identité apposée (EX-M24) vivent
  **là**. Complété.
- `journal.rs:695` (`armer_oracles`) affirmait que l'oracle M2 « vérifie que le
  simulateur randomise effectivement ». Il ne vérifie rien : la doc de
  `Milieu::verifier`, dix lignes plus bas, dit le contraire et a raison. Aligné.
- `journal.rs:728` (`verifier`) ouvrait sur « Une violation arrête l'exécution
  (EX-C09) », alors que la même doc conclut que la méthode n'a aucun appelant.
  Mis au conditionnel, avec le renvoi à `hors_perimetre()`.

### A14 — `quota.rs:55` — le seuil de concentration promettait une borne qu'il ne tient pas au premier coup

**Preuve.** `Politique::SeuilDeConcentration` : « la part d'une clé dans le total
des écritures ne peut pas dépasser `part_max` ». `Quotas::verdict` accepte
inconditionnellement quand `total == 0`, et la part de cette écriture vaut 1. Le
test existant ne le voyait pas : ses deux premières écritures portaient sur deux
clés distinctes.

**Changement.** L'exception est documentée comme structurelle — sans elle, aucune
clé ne pourrait commencer — et fixée par un test :
`la_premiere_ecriture_echappe_au_seuil_de_concentration`, à `part_max = 0,1`.

### A15 — `quota.rs:82` — le preneur documenté comme apposé par le milieu ne l'est pas

**Preuve.** Doc du champ `preneurs` : « le milieu le connaît parce qu'il **appose
l'identité** (EX-M24), et non parce qu'un agent le déclare ». `soumettre` reçoit
un `u32` de l'appelant ; aucun chemin ne relie `Quotas` à
`Enregistrement::auteur`. La signature n'est pas changée — elle est appelée depuis
`sim-agents/tests/sortie_phase_6.rs`, hors de ce morceau.

**Changement.** La doc distingue ce que le mécanisme **devrait** prendre de ce
qu'il prend, et renvoie à `hors_perimetre()`.

### A16 — `historique.rs` — deux compteurs présentés comme deux suites appariées

**Preuve.** EX-M25 : « pour chaque identité, **la suite de ses assertions et,
quand elle existe, l'issue vérifiée de chacune** ». `Historique` tient
`assertions` et `confirmees/dementies/non_verifiables` comme compteurs
indépendants : `verifier` n'exige aucun `asserter` préalable et ne dit pas quelle
assertion l'issue tranche, si bien que `confirmees` peut dépasser `assertions` —
c'est le cas dans les tests de la crate et dans `sortie_phase_6.rs`.
Deuxième point : EX-M25 exige qu'un historique « ne soit jamais affiché comme une
mesure de véracité », et `Compte::fiabilite` ne portait pas cette contrainte.

**Changement.** Les deux docs le disent : l'appariement n'est pas livré, et la
fiabilité mesure une concordance constatée, jamais une véracité (PD14).
L'appariement lui-même n'est **pas** implanté — voir B3.

---

## B. Identifiées, non corrigées

### B1 — Toutes les pages du traité citées dans la crate sont fausses par rapport au PDF du dépôt

**Mesure.** `Traité.pdf` du dépôt est bien la troisième édition (page de titre :
« 15 août 2026 — troisième édition, revue sur sa propre mesure ») et compte **143
pages**, folio imprimé égal à l'index de page. Extraction par `pypdf`, phrase par
phrase :

| Citation dans le code | Phrase | Page mesurée |
|---|---|---|
| `journal.rs:696-699` — « §1.2, p. 13 » | « M1 : l'ordre est total… » | **14** |
| `replication.rs:7` — « §2.1, p. 22 » | « Le nombre de disparitions auquel r₂ survit… » | **26** |
| `replication.rs:181` — « §2.1, p. 21 » | « tout enregistrement accusé… » (R1) | **26** |
| `controle.rs:3` — « §4.2, p. 49 » | « Le plan de données évite l'accord… » | **65** |
| `journal.rs:82` — « §6.2, p. 71 » | « la traçabilité distribuée répond… » | **96** |

Les cinq sections, elles, sont exactes ; les cinq pages ne le sont pas, et l'écart
croît avec la position dans l'ouvrage (+1, +4, +5, +16, +25), ce qui est la
signature d'un rendu de géométrie différente, non d'un décalage constant.

**Pourquoi non corrigé.** `CLAUDE.md` fixe la pagination normative à « **116
pages** » et pose que « une page citée sans son édition est une provenance fausse,
pas imprécise (F2) ». Aucun rendu à 116 pages n'existe dans le dépôt, et le seul
qui s'y trouve en fait 143 : les pages du code ne correspondent donc **ni** à la
référence déclarée, **ni** au fichier livré. Renuméroter sur le PDF du dépôt
mettrait `sim-milieu` en désaccord avec les quatre autres crates, qui portent la
même pagination, et prendrait à la place du dépôt une décision documentaire —
quel rendu fait foi — que les consignes de cette passe réservent explicitement.
`CLAUDE.md` et les autres crates sont hors de ce morceau.

À trancher en amont : soit `docs/Traité.pdf` (116 pages) est restauré et les
citations sont justes, soit `Traité.pdf` (143 pages) fait foi et les cinq
citations de cette crate — plus leurs homologues dans les trois autres — se
renumérotent en une passe.

### B2 — EX-M09 : le ℓ₉₉ de durabilité est mesuré et n'est lu par personne

`Milieu::latences_durabilite` n'a aucun lecteur hors des tests de la crate
(recherche sur tout `crates/`). EX-M09 est étiquetée `[M]` et exige que ℓ₉₉ « en
soit extrait **et affiché** ». `sim-viz` déclare de son côté ne pas afficher
« EX-V06 — la distribution du chemin de durabilité ».

**Pourquoi non corrigé.** Le milieu produit la mesure ; c'est l'affichage qui
manque, et il est déclaré du côté qui le doit. Ajouter une entrée à
`hors_perimetre()` du milieu déclarerait absent ce que le milieu livre
effectivement — la faute symétrique de PD6, dans l'autre sens.
Ce que la doc du module `latence` dit maintenant, et qui manquait : un seul
segment du chemin est tiré. La lecture ne coûte aucun tic, et `Milieu::lire` le
dit désormais.

### B3 — EX-M25 : l'appariement assertion → issue n'est pas implanté

Voir A16 pour la preuve. Le livrer suppose un identifiant d'assertion porté par
`Historique::asserter` et repris par `verifier`, donc un changement de signature
d'une API appelée depuis `sim-agents/tests/sortie_phase_6.rs` — hors de ce
morceau, et sans appelant de scénario qui en tirerait quoi que ce soit
(EX-M25 est déjà déclaré non branché). Consigné ; le correctif appartient à la
passe qui câblera le mécanisme.

---

## C. Vérifié, conforme

Relevé ici parce qu'un audit qui ne dit que ce qui cloche laisse croire que le
reste n'a pas été regardé.

- **PD14 — le milieu n'évalue jamais le contenu.** Aucun chemin de la crate ne
  lit `Enregistrement::valeur` pour en tirer une décision. Le seul lecteur est
  `verifier_m10`, qui compare l'état lisible d'avant et d'après un compactage :
  il vérifie une préservation, il ne juge pas un témoignage.
- **EX-M11, EX-M16 — les chiffres du traité sont retrouvés** : 53 + 7 × 1 = 60,
  53 + 7 × 100 = 753, 34 × 100 = 3 400 ; 2k/b = 0,012 message par enregistrement
  à b = 500 et k = 3. Tests existants, conservés.
- **NF-02** — `libm::log` dans `latence.rs`, aucune des sept méthodes interdites
  de `f64` ; clippy le confirme en `deny`.
- **PD1** — aucun `HashMap`/`HashSet` ; le mélange de `lire_multi` est un
  Fisher-Yates tiré de l'unique `Alea` semé, et `Alea::entier(n)` rend bien
  `[0, n)`.
- **Les neuf entrées préexistantes de `hors_perimetre()`** ont été vérifiées une à
  une contre les appelants réels : toutes exactes, y compris la non-monotonie de
  |ISR| sous élection hors ISR, la barrière posée et levée dans le même appel, et
  l'absence de différenciation de révocation entre les trois protocoles.

---

## Tour 2

Jugement du critique : `M2-critique.md`. Deux affirmations prises en défaut, cinq
anomalies D1 à D5, trois constats mineurs. **Tout est corrigé**, aucune entrée
n'a été écartée comme non-anomalie.

Les quatre commandes, dans un `CARGO_TARGET_DIR` privé :

```
$ cargo clippy -p sim-milieu --all-targets --release
    Finished `release` profile [optimized] target(s) in 1.49s

$ cargo test -p sim-milieu --release
running 68 tests
test result: ok. 68 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

$ cargo doc -p sim-milieu --no-deps
 Documenting sim-milieu v0.1.0
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 1.62s
   Generated .../doc/sim_milieu/index.html

$ cargo check -p sim-agents --release
    Finished `release` profile [optimized] target(s) in 1.46s
```

**61 → 68 tests.** Sept ajoutés, aucun retiré, aucune assertion affaiblie.

Les sept binaires d'intégration de `sim-agents` passent contre ce `sim-milieu` —
`scenario_b` 11, `determinisme` 4, `sortie_phase_2` 5, `sortie_phase_3` 4,
`sortie_phase_4` 5, `sortie_phase_5` 3, `sortie_phase_6` 11. Les tests
**unitaires** de `sim-agents` ne compilent pas au moment de cette passe, pour des
raisons étrangères à ce morceau (`cycle_de_vie.rs:359`, `soupcon.rs:498` — trois
erreurs E0308/E0609 dans du code en cours d'édition par un autre agent).

---

### Défaut 1 — le cardinal de `hors_perimetre()`

**Reproduction.** `git show HEAD:./crates/sim-milieu/src/lib.rs` rend **neuf**
chaînes, non dix. §A4 et §C disaient dix.

**Correctif.** §A4 dit maintenant « les **neuf** entrées existantes », et ajoute
que quatre entrées portent la liste livrée à treize. Le §C est corrigé de même.
Les neuf restent exactes : le critique l'a revérifié.

### Défaut 2 — le bloc de sortie de §A3

**Reproduction.** Le bloc collé au tour 1 annonçait `57 filtered out`, soit un
arbre à 59 tests, dans un paragraphe qui conclut « les 61 tests passent ».

**Correctif.** Contre-épreuve rejouée sur l'arbre livré, frontière retirée de
`Milieu::compacter` puis remise. Le bloc de §A3 porte la sortie réelle —
`2 passed; 1 failed; 65 filtered out`, soit 68 — et le dit.

---

### D1 — `groupe.rs:397` — prédicat inatteignable d'EX-M23 `[S]`

**Arbitrage : déclarer, et livrer le contre-exemple.** Rendre la branche
atteignable demanderait un état de zombie — un membre retiré de `membres` mais
gardant ses partitions —, c'est-à-dire un **mécanisme** que ni le traité ni le
PRD ne demandent au milieu, et qu'aucun scénario n'exécuterait (`hors_perimetre()`
déclare déjà le groupe non branché). La crate sait nommer ce cas : `journal.rs`
pour M2/M3, `replication.rs:173-179` pour R2. Le prédicat est **conservé** pour
la raison que `Partition` donne déjà de M1 — « un invariant vrai par construction
cesse de l'être à la première modification » —, et sa doc dit désormais qu'aucune
suite d'appels publics ne l'atteint, avec le nom des deux seuls scripteurs de
`attribution`.

**Reproduction.** Corps de `verifier_surete` vidé :

```
$ cargo test -p sim-milieu --release -- une_partition_na_quun_proprietaire
test groupe::tests::une_partition_na_quun_proprietaire ... ok
test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 66 filtered out
```

**Changement.** Le test (`groupe.rs:622`) construit le contre-exemple depuis
l'intérieur du module — le seul endroit d'où l'état est constructible — en
écrivant `g.attribution[2] = Some(77)`, puis exige une violation et vérifie son
libellé.

**Preuve que ça a disparu.** Même contre-épreuve, sur le test corrigé :

```
test groupe::tests::une_partition_na_quun_proprietaire ... FAILED
thread ... panicked at crates\sim-milieu\src\groupe.rs:640:9:
assertion `left == right` failed: []
  left: 0
 right: 1
test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 67 filtered out
```

Corps remis : les 68 tests passent. NF-10 est tenue.

### D2 — `historique.rs` — le refus « non négociable » contourné

**Arbitrage : fermer la voie.** La doc du module qualifie le refus de non
négociable, et le §8.1 dit pourquoi — un poids calculé sur des issues non
vérifiables récompense la conformité. Requalifier la doc reviendrait à écrire que
le mécanisme rend le nombre qu'il déclare refuser. La voie est donc fermée, et
**à la racine** : le refus n'appartient plus à `Historique::poids` mais au
**compte**, par où passent les trois voies publiques.

**Reproduction.**

```
h.poids(qui(6))              -> Err("là où l'issue n'est pas vérifiable, … (EX-M25)")
h.compte(qui(6)).fiabilite() -> Some(1.0)
h.consultations()            -> 1
h.identites()                -> [(6, Some(1.0))]
```

**Changement.** `Compte::regime()` (`historique.rs:77`) porte la règle, seul.
`Compte::fiabilite()` (`:101`) rend `Result<Option<f64>, &'static str>` — même
forme que `poids`, déjà dans la crate — et les deux réponses négatives restent
**distinctes** : `Err` = régime interdit, `Ok(None)` = aucune issue vérifiée. Les
confondre en un seul `None` aurait été la faute que ce dépôt traque ailleurs (les
deux ℓ₉₉, les deux corrélations). `Historique::regime` (`:170`) et
`Historique::poids` (`:180`) y renvoient ; `poids` n'ajoute plus que la
consultation, et sa duplication du test de régime disparaît.

La seconde moitié du constat — la voie détournée ne paie pas la consultation —
est **requalifiée** plutôt que fermée : `Historique::compte` (`:161`) est un
accesseur des quatre compteurs, pas la consultation facturée, et sa doc le dit
désormais explicitement, en renvoyant le coût d'EX-M25 à `poids` seul. Facturer
`compte` facturerait aussi `identites`, donc l'affichage de la population, ce que
le tableau 22 ne demande pas. Rien n'est contourné pour autant : le refus ne
dépend plus de la voie.

**Preuve que ça a disparu.** `le_refus_ne_se_contourne_par_aucune_voie_publique`
(`historique.rs:222`) exige `is_err()` sur les trois voies — `poids`, `compte`,
`identites`. Vidé du garde-fou de `fiabilite`, il tombe sur la deuxième assertion.

### D3 — `lib.rs:94` — astérisques d'emphase

**Reproduction.** `git show HEAD:.../lib.rs` : l'entrée « plan de contrôle
`**en exécution**` » figure deux entrées sous le commentaire (`lib.rs:77-78`) qui
interdit les astérisques, parce que `sim-viz` (`lib.rs:900` → `section` → `puce`,
`:1026`) pose un `egui::RichText` sans analyseur Markdown.

**Changement.** Astérisques retirées. Et parce que la règle a été violée une fois
alors qu'elle était écrite juste au-dessus, elle est désormais **tenue par un
test** : `aucune_entree_ne_porte_de_balisage_markdown` (`lib.rs:108`) refuse tout
astérisque et tout retour à la ligne dans les treize entrées.

**Preuve que ça a disparu.** Le test passe sur l'arbre livré ; réintroduire les
deux astérisques le fait tomber avec le texte fautif en message.

### D4 — `journal.rs:780` — `verifier_m10` comparait les `f64` par `==`

**Reproduction.** Sans aucun compactage, sur un journal identique à lui-même :

```
$ cargo test -p sim-milieu --release -- repro_d4 --nocapture
thread '...repro_d4_m10_ne_fabrique_pas_de_violation_sur_nan' panicked at journal.rs:829:9:
[Violation { oracle: "EX-M10 — le compactage préserve l'état final lisible",
  date: Instant(1),
  details: "partition 0 : la clé 1 lisait NaN avant le compactage et lit NaN après" }]
```

**Changement.** La comparaison porte sur les **bits** : `v.to_bits() ==
valeur.to_bits()`. L'oracle demande si le compactage a conservé le même
enregistrement, non si deux nombres sont numériquement égaux ; le compactage
recopie l'enregistrement tel quel (`Copy`), donc les bits sont préservés
exactement quand l'état l'est. La comparaison est **plus stricte** — elle sépare
+0,0 de −0,0 —, ce qui est le bon sens pour une préservation, et un oracle plus
strict ne peut pas laisser passer ce que l'ancien attrapait. PD14 tient : comparer
deux états n'est pas juger un contenu.

Aucune garde n'a été posée sur `Milieu::ecrire` : refuser un `f64` non fini
changerait le modèle pour réparer un oracle, et le défaut est dans l'oracle.

**Preuve que ça a disparu.**
`m10_ne_fabrique_pas_de_violation_sur_une_charge_utile_nan` (`journal.rs:851`)
passe. Les deux tests de §A3 — dont celui qui **exige** deux violations sur une
perte réelle — passent inchangés : la borne n'a pas été relâchée.

### D5 — `groupe.rs:168` — `duree_orpheline` ignorait l'orphelinat initial

**Reproduction.**

```
assertion `left == right` failed: 2 partitions × 500 tics depuis la création
  left: Duree(0)
 right: Duree(1000)
```

`suivre_vivacite` ouvre pourtant une attente à `Instant(0)`, que l'entrée d'un
membre à `Instant(500)` satisfait : deux mesures du même fait se contredisaient.

**Changement.** `Groupe::nouveau` (`:188`) prend la **date de création** et
renseigne `orphelines_depuis` avec elle. Le paramètre n'est pas `Instant(0)`
supposé : un groupe créé en cours d'exécution ne doit pas cumuler l'orphelinat
antérieur à lui-même. Aucun appelant hors crate (`Groupe` n'est instancié nulle
part ailleurs) ; `cargo check -p sim-agents --release` passe. La doc de
`duree_orpheline` dit en outre ce que son nom ne dit pas : la durée est cumulée
**sur les partitions**, p × d et non d.

**Preuve que ça a disparu.** `lorphelinat_initial_est_compte_comme_les_autres`
(`groupe.rs:489`) exige `Duree(1_000)` et la concordance avec l'attente de
l'oracle ; `un_groupe_cree_en_cours_dexecution_ne_cumule_pas_davant` (`:508`)
exige `Duree(400)` pour un groupe créé à `Instant(700)` — et non `Duree(1_800)`.

---

### Mineur — `quota.rs:151` — `PrixCroissant` en retard d'un preneur

**Reproduction.**

```
assertion `left == right` failed: un facteur ajouté par preneur au-delà du premier
  left: Acceptee { prix: 1.0 }
 right: Acceptee { prix: 2.0 }
```

Le deuxième preneur distinct payait le prix nominal.

**Changement.** Le **prix** inclut le soumissionnaire :
`1 + pente × ((preneurs + !déjà_preneur) − 1)`. C'est la doc qui avait raison
contre le code, et le §8.1 avec elle — « prix croissant **avec le nombre de
preneurs** » : un prix qui ne bouge pas quand un deuxième preneur arrive ne croît
pas avec leur nombre. Les **refus**, eux, restent prononcés sur l'état d'avant,
sans quoi un quota de 1 refuserait tout ; les deux états sont désormais
distingués dans la doc de `soumettre`, parce qu'ils diffèrent.

**Preuve que ça a disparu.** `le_prix_monte_des_le_deuxieme_preneur`
(`quota.rs:269`) exige 1,0 puis 2,0, et 2,0 encore pour un preneur déjà compté —
qui ne fait pas monter leur nombre. `le_prix_croissant_taxe_sans_refuser` passe
de 7,0 à **10,0** attendus : l'assertion reste exacte, et le commentaire dit ce
que valait l'ancien compte et pourquoi. Le test aval
`le_quota_borne_une_ressource_et_le_prix_ne_refuse_rien`
(`sortie_phase_6.rs:217`) passe : son cumul monte de 8,0 à 10,0, au-dessus du
seuil de 5,0 qu'il vérifie.

### Mineur — `journal.rs:265` — `valider` rejoué facturait deux fois

**Reproduction.**

```
thread '...repro_journal457_un_accuse_ne_se_rejoue_pas' panicked at journal.rs:839:9:
le second accusé n'accuse rien
```

`Milieu::valider` rendait `true` deux fois sur la même `Ecriture`, comptait deux
`tours_journal` et poussait un doublon dans `latences_durabilite`, donc biaisait
le ℓ₉₉ d'EX-M09.

**Changement.** Correctif à la racine, dans `Partition::valider` (`:265`) et non
chez l'appelant : `Ok(i) if !self.journal[i].durable`. Un accusé de durabilité est
un événement unique ; le rejouer n'accuse rien, et `false` est déjà la réponse
« rien n'a eu lieu ». Les docs de `Partition::valider` et de `Milieu::valider`
(`:471`) énumèrent maintenant les **deux** cas de `false` — décalage inconnu, et
enregistrement déjà durable.

**Portée mesurée, et c'est un résultat en soi.** Une sonde temporaire posée dans
`Milieu::valider`, qui panique sur toute re-validation ou tout décalage absent, a
été passée sur les sept binaires d'intégration de `sim-agents` — dont
`sortie_phase_6`, qui exécute le scénario M et le scénario B onze fois. **Elle
n'a jamais déclenché** : aucun chemin exécuté ne valide deux fois. Le biais du
ℓ₉₉ était donc latent, non actif, et le correctif ne déplace aucune mesure
publiée. Sonde retirée.

**Preuve que ça a disparu.** `un_accuse_de_durabilite_ne_se_rejoue_pas`
(`journal.rs:868`) exige `true` puis `false`, `tours_journal == 1` et
`latences_durabilite.compte() == 1`.

### Mineur — `groupe.rs:212` — `Groupe::p` public désaccordait deux mesures

**Reproduction.** Le champ était public alors que `attribution` et
`orphelines_depuis` sont dimensionnés depuis `p` à la construction :

```rust
g.p = 100;
assert_eq!(g.parallelisme_utile(), 1, "désaccordé de debit_instantane = 4");  // passe
```

**Changement.** Le champ est **supprimé** — pas rendu privé avec un accesseur qui
le recopierait. `Groupe::p()` (`:212`) le dérive de `attribution.len()`, la table
même que `debit_instantane` parcourt : les deux mesures lisent désormais la même
source, et le désaccord n'est plus représentable. Aucun appelant hors crate.

**Preuve que ça a disparu.** La reproduction **ne compile plus** : `no field 'p'
on type 'Groupe'`. C'est la forme la plus forte de disparition — un test qui la
garderait supposerait que l'état fautif reste constructible.

---

## Ce qui reste ouvert après le tour 2

- **B1 — les pages du traité** restent fausses par rapport au PDF du dépôt, pour
  le motif donné au tour 1 : l'arbitrage « quel rendu fait foi » est en amont de
  ce morceau et engage les quatre crates.
- **B2, B3** inchangés.
- **La liste de `hors_perimetre()` n'a pas bougé au tour 2.** Rien de ce qui a été
  corrigé ici ne branche ni ne débranche un mécanisme : les treize entrées restent
  exactes.
- **À porter hors de ce morceau** : le compte de tests du dépôt (`CLAUDE.md`
  annonce 428) monte de sept ; et EX-M26, si le PRD chiffre le prix croissant,
  doit lire `1 + pente × (k − 1)` pour le k-ième preneur distinct,
  soumissionnaire compris.
