# M1 — `crates/sim-core` : audit

Portée : les quatorze fichiers de `crates/sim-core/src`. Rien hors de ce
répertoire n'est modifié. Douze anomalies corrigées, huit relevées sans
correctif — le motif est donné pour chacune.

> **Renvois.** Les `fichier:ligne` de ce rapport ont été repris au tour 2 pour
> désigner **le code livré**, et non l'état trouvé. Les renvois hors de
> `crates/sim-core/` sont donnés par symbole et non par ligne : quatre autres
> agents éditent ces crates en parallèle, et toute ligne qu'on y citerait serait
> périmée avant d'être lue. Deux affirmations de ce tour 1 ont été prises en
> défaut par le critique ; elles sont **marquées sur place** et traitées au
> [tour 2](#tour-2).

## État après correctifs (tour 1)

L'état **livré** est celui du [tour 2](#tour-2) ; ce qui suit est l'état à la
clôture du tour 1.

```
$ cargo clippy -p sim-core --all-targets --release
    Checking sim-core v0.1.0 (…\crates\sim-core)
    Finished `release` profile [optimized] target(s) in 4.13s

$ cargo test -p sim-core --release
running 91 tests
test result: ok. 91 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
   Doc-tests sim_core
test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

$ cargo doc -p sim-core --no-deps
 Documenting sim-core v0.1.0 (…\crates\sim-core)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 6.01s

$ cargo check -p sim-milieu -p sim-agents --release
    Finished `release` profile [optimized] target(s) in 1.61s
```

86 tests avant, 91 après : cinq ajoutés, aucun retiré, aucun affaibli. Les cinq
sont exécutés ci-dessous **contre le code d'avant correctif** ; quatre échouent,
et l'échec est la preuve.

Note d'environnement, sans rapport avec le code : `cargo test` échoue à
l'édition de liens dans le `target/` du dépôt, `ld.exe` de mingw 16.1.0 ne
retrouvant aucun des `.o` qu'il vient de produire — le chemin du dépôt porte un
« é » (`3 - Traité`) et l'éditeur de liens lit son `argv` dans la page de codes
ANSI. Toutes les mesures de ce rapport sont prises avec
`CARGO_TARGET_DIR` pointé sur un chemin ASCII ; rien d'autre n'est changé. ✎ *Motif faux, corrigé le
22 août 2026 : ce n'est pas l'accent du chemin mais la **synchronisation OneDrive** du
`target/` qui casse l'édition de liens — un workspace d'essai sous `…/3 - Traité/`, même
accent et même espace, s'édite sans un mot hors de OneDrive. Le déroutement reste le bon
remède ; seul son motif était mal attribué. Mesure à l'appui à
[`docs/DEVELOPPEMENT.md`](../../docs/DEVELOPPEMENT.md).*

---

## A1 — `faute.rs:292` (avant correctif : `faute.rs:296-322`) — invariant faux

**Le défaut.** `ModeleFaute::tirer_pannes` tirait `crash_baie` et `crash_centre`
**par acteur**, dans la boucle des domaines, jusqu'à ce qu'un tirage réussisse.

**Ce que la spécification dit.** EX-C05 (PRD §6.1, l. 751) : « Le modèle de faute
couvre : crash-arrêt et redémarrage de machine, **de baie et de centre** ». Les
champs de `ModeleFaute` le déclarent en toutes lettres :

```rust
/// Probabilité de crash par machine et par pas d'évaluation.
pub crash_machine: f64,
/// Idem par baie — emporte toutes les machines de la baie.
pub crash_baie: f64,
```

et `Niveau::Baie` : « Une baie tombe, et **emporte toutes ses machines** ».

**La preuve.** Le nouveau test `une_baie_tombe_en_entier_et_a_sa_propre_probabilite`
exécuté contre le `faute.rs` de `HEAD` (deux baies de vingt machines,
`crash_baie = 0,5`, 200 pas) :

```
thread '…::une_baie_tombe_en_entier_et_a_sa_propre_probabilite' panicked at src\faute.rs:592:17:
baie 1 au pas 0 : 18 machines sur 20
```

(Sortie brute d'alors ; dans le code livré, cette assertion est `faute.rs:645`.)

Dix-huit sur vingt : les deux machines rencontrées **avant** le tirage réussi
sortent indemnes d'une baie tombée. Second effet, mesuré en remplaçant
l'assertion par un compteur, même graine, mêmes paramètres :

| code | chutes de baie constatées | probabilité déclarée |
|---|---|---|
| avant | **400 sur 400** tirages | 0,5 |
| après | **204 sur 400** tirages | 0,5 |

Une baie de *m* machines tombait avec la probabilité 1 − (1 − p)^m : l'injection
de corrélation dépendait de la taille de la population, ce qu'aucun réglage ne
disait.

**Ce que j'ai changé.** Un tirage par niveau, avant la boucle des acteurs, sur
les clés de centre puis de baie triées et dédupliquées (l'ordre des tirages ne
dépend donc que de la structure — PD1). Le classement par acteur suit :
centre, puis baie, puis machine. La fermeture `centre_tombe` et son paramètre
mort `let _ = c;` disparaissent ; le corps est plus court qu'avant.

**Conséquence.** `crash_baie` et `crash_centre` valent maintenant ce qu'ils
déclarent, et un niveau emporte tous ses membres. La suite de tirages consommés
sur `Alea` change — sans effet ailleurs : `tirer_pannes` n'a **aucun appelant**
hors de `sim-core` (vérifié par balayage des trois autres crates).

Deux tests ajoutés : celui ci-dessus, et `un_centre_emporte_toutes_ses_baies`
(garde de non-régression sur la préséance du niveau ; il passait déjà avant,
`crash_centre = 1,0` faisant réussir le premier tirage).

---

## A2 — `faute.rs:489` — liste `hors_modele()` périmée (PD6)

**Le défaut.** L'entrée ouvrait sur :

> « **ce modèle-ci**, dans les scénarios livrés : **aucun d'eux ne règle
> `Config.fautes`**, donc […] ni les points d'injection ne sont jamais tirés »

**La preuve.** `crates/sim-agents/src/scenario.rs` (fonction `scenario_b`) règle `Config.fautes`,
et son propre commentaire le dit :

```rust
let mut fautes = sim_core::faute::ModeleFaute::default();
fautes.injections = vec![
    sim_core::faute::Injection::Echec { operation: "action de l'agent".to_string(), … },
    sim_core::faute::Injection::Echec { operation: "crash avant validation".to_string(), … },
];
let config = Config { …, fautes: fautes.clone(), … };
```

La conclusion (« les points d'injection ne sont jamais tirés ») reste vraie, mais
le motif énoncé est faux, et le vrai motif est ailleurs : `Moteur::installer_fautes`
n'a **aucun appelant** dans tout le dépôt — balayage `grep -rn installer_fautes
crates/` : une définition, zéro appel. Toute exécution tourne donc sur
`ModeleFaute::default()` quelle que soit la `Config` chargée. C'est le mensonge
symétrique que PD6 vise : une liste d'absences qui se trompe sur ce qui est
absent.

Même balayage, mécanismes d'ici sans aucun appelant hors `sim-core` :
`tirer_pannes`, `Moteur::avancer_partition`, `injection_echec`,
`injection_retard`, `injection_valeur`, `retard_message`, `ecriture_corrompue`.
Les trois derniers ne figuraient nulle part dans la liste, alors qu'EX-C05 les
énumère (« omission et retard de message ; […] corruption des écritures non
synchronisées au redémarrage »). **Ce balayage en oubliait deux — voir D2 au
tour 2 : ils sont neuf.**

**Ce que j'ai changé.** L'entrée dit maintenant que le moteur ne reçoit jamais le
modèle configuré, que le scénario B **règle** bien `Config.fautes` mais que cette
déclaration ne sert qu'à l'affichage, au hachage et au versionnement, et elle
nomme les mécanismes sans appelant — sept alors, **neuf** dans le code livré,
voir D2. `gigue` — le seul que la boucle appelle — est nommé aussi, avec son
amplitude nulle au défaut.

**Conséquence.** La liste redevient exacte. Elle est plus longue, et c'est le
résultat. — **Faux : elle restait incomplète de deux entrées. Pris en défaut
par le critique, corrigé en D2 au tour 2.**

---

## A3 — `horloge.rs:113` — grandeur sans provenance (F2, NF-15)

**Le défaut.** `Horloges::PROVENANCE_EPSILON` affirmait :

> « une infrastructure de temps à références GPS et horloges atomiques maintient
> l'incertitude **généralement sous 10 ms** — repère externe (annexe B) »

**Ce que la source dit.** `Traité.md`, §7.3 : TrueTime tient l'incertitude « sous
la forme d'une dent de scie de **1 à 7 ms** entre deux interrogations des maîtres
de temps, avec des **excursions au-delà** lorsqu'un maître devient indisponible
ou qu'une machine est surchargée — mesure de 2012 ». Et la phrase suivante :
« Un ε annoncé **sans percentile** est inutilisable ici : ce qui viole
l'invariant n'est pas la valeur courante, c'est **la queue**. »

Le « 10 ms » n'est nulle part dans le traité. Le libellé faisait donc deux fois
ce que la source interdit : un chiffre attribué à une source qui n'en porte pas
d'approchant, et un majorant lissé sans percentile — c'est-à-dire l'ε que la
phrase suivante déclare inutilisable, sur un mécanisme dont le mode de
défaillance est précisément la queue.

(À ne pas confondre avec `docs/PRD.md` l. 1445, « ε_vrai de l'horloge simulée
(EX-C13) | 0 – 60 s | **10 ms** » : c'est le défaut d'un curseur de scénario, pas
un repère externe.)

**Ce que j'ai changé.** Le libellé porte la dent de scie de 1 à 7 ms, les
excursions, la date de la mesure, la raison pour laquelle un majorant ne vaut
rien, et il conserve « il la suppose ». Test ajouté :
`le_repere_depsilon_porte_le_chiffre_de_la_source_et_sa_queue`, qui épingle les
quatre fragments.

**Conséquence.** L'affichage prévu — il n'existe pas encore, voir R3 — dirait le
chiffre de la source au lieu d'un chiffre inventé.

---

## A4 — `verification.rs:246` — doc qui affirme ce que le code ne tient pas

**Le défaut.** `Campagne::REFUS` était documentée « **Affiché en permanence** ».

**La preuve.** Balayage du dépôt : `Campagne::REFUS` n'apparaît que dans sa
définition et dans son propre test. `sim-viz` ne la lit pas ; aucun export ne
l'écrit.

**Ce que j'ai changé.** La doc dit ce qui est : formulation arrêtée, aucun
appelant, prête pour l'affichage et non affichée — et elle renvoie à
`Issue::libelle`, qui porte les mêmes trois refus et **est** appelé. Forme
reprise de `PROVENANCE_EPSILON`, qui déclarait déjà honnêtement son absence
d'appelant.

**Conséquence.** Une exigence [U] déclarée tenue redevient une exigence déclarée
non câblée.

---

## A5 — `service.rs:15` — même classe, même correctif

**Le défaut.** Le `//!` du module affirmait que les deux ℓ₉₉ « portent des
libellés distincts **dans toute l'interface** ».

**La preuve.** `Service::LIBELLE_L99` n'a aucun appelant hors de son test ;
`sim-viz` n'importe de `sim-core` que `ModeleFaute::hors_modele` et
`Agregat::mention_obligatoire`. — **Faux : `crates/sim-viz/src/scenario_a.rs`
importe aussi `sim_core::temps::Granularite`. Pris en défaut par le critique,
corrigé en D1 au tour 2 ; la conclusion visée — `LIBELLE_L99` sans appelant —
tient malgré tout.**

**Ce que j'ai changé.** Le module dit que la séparation du §8.3 est tenue par le
nom des deux fonctions, pas par un affichage, et que le libellé n'a pas
d'appelant.

---

## A6 — `famille.rs:256` — corrélation fabriquée, contre EX-C19

**Le défaut.** `Familles::famille` rend `u32::MAX` pour un agent hors bornes, et
sa doc disait pourquoi : « un appelant qui interroge un agent inexistant ne doit
pas recevoir une corrélation ». `Familles::partagent` respectait la règle.
`TirageDeDecision::uniforme`, non : il clavait le mémo sur cette sentinelle,
réunissant **tous** les agents inexistants dans une famille commune.

**Ce que la spécification dit.** EX-C19 (PRD l. 766) : « Un agent appartient à
**exactement une** famille ; deux agents d'une même famille consomment le
**même tirage** ». Un agent qui n'existe pas n'appartient à aucune.

**La preuve.** Le nouveau test `deux_agents_hors_bornes_ne_partagent_pas_leur_tirage`
contre le `famille.rs` de `HEAD` :

```
assertion `left != right` failed: aucune famille, donc aucun partage
  left: 0.4678368592575487
 right: 0.4678368592575487
```

Deux agents distincts, hors bornes, même tirage — une corrélation que le curseur
de familles ne pilote pas, sur la grandeur même que la phase 6 mesure.

**Ce que j'ai changé.** La sentinelle devient une constante nommée,
`Familles::SANS_FAMILLE` (`famille.rs:111`), et `uniforme` la traite comme une
absence : tirage direct, aucune mémoïsation, `partages` inchangé.

---

## A7 — `famille.rs:100` — débordement silencieux à n ≥ 65 536

**Le défaut.** `appartenance: (0..n).map(|i| i * nb / n)` en `u32`. Le profil
release du dépôt (`Cargo.toml` racine) ne pose pas `overflow-checks` : le produit
s'enroule sans un mot.

**La preuve.** Le nouveau test `la_repartition_ne_deborde_pas_sur_une_grande_population`
contre `HEAD`, à n = 100 000 et `interpole(n, 0.5)` :

```
assertion `left == right` failed
  left: 7049
 right: 49999
```

Le dernier agent était rangé dans la famille 7049 au lieu de 49999 : un
enroulement replie les agents tardifs sur les familles de tête, donc fabrique de
la conformité que `diversite_effective()` continue de nier.

**Ce que j'ai changé.** Le produit passe par `u64`. Une ligne.

**Conséquence.** Hors de portée des scénarios livrés (NF-05 plafonne à
n = 1 000), mais `Familles::interpole` est publique et sa borne n'était écrite
nulle part.

---

## A8 — `lib.rs:141` — message d'erreur incomparable

`verifier_rejeu` écrivait le hachage attendu en hexadécimal (`{:016x}`) et le
hachage fourni en **décimal** (`{hachage_export}`), dans la même phrase. Deux
nombres qu'aucun lecteur ne peut rapprocher, sur le chemin d'erreur de NF-03.
Corrigé : `{hachage_export:016x}`. Le test `le_rejeu_dune_autre_configuration_est_refuse`
épingle désormais les deux formes au lieu de se contenter d'`is_err()`.

---

## A9 — `lib.rs:95` — chemin de panique non documenté

`Config::hachage` fait `serde_json::to_string(self).expect("configuration
sérialisable")`. JSON n'a ni `NaN` ni infini et `serde_json` refuse de les
écrire ; or `Config` porte `secondes_coeur_max: Option<f64>` et un `ModeleFaute`
entièrement fait de `f64`. Une `Config` construite en mémoire avec un taux `NaN`
fait donc paniquer `hachage()`, et par contrecoup `entete()` et
`verifier_rejeu()`. Section `# Panics` ajoutée, qui note aussi qu'une `Config`
lue d'un fichier ne peut pas être dans cet état.

---

## A10 — `detecteur.rs:158` — deux `assert!` non documentés

`Detecteur::nouveau` panique sur `seuil == 0` et sur `expiration >= periode`.
`oracle.rs`, `registre.rs`, `temps.rs` et `graphe.rs` documentent tous les leurs ;
celui-ci, non, alors qu'un test l'exerce (`le_detecteur_refuse_une_expiration_plus_longue_que_sa_periode`).
Section `# Panics` ajoutée.

---

## A11 — `oracle.rs:236` — doc qui contredit le corps

`Registre::attendre` : « la condition doit devenir vraie **avant**
`maintenant + horizon` ». `Registre::echoir` compare avec `<`, donc l'échéance
elle-même n'est pas une violation — le test
`une_vivacite_non_satisfaite_viole_juste_apres_son_horizon` l'établit et son nom
le dit. « avant » remplacé par « au plus tard à », avec le renvoi à `echoir`.

---

## A12 — `couverture.rs:178` — nom de test qui promet plus que le corps

Le test s'appelait `aucune_fonction_ne_rend_un_pourcentage_de_couverture` et
n'assertait que le contenu de `Agregat::mention_obligatoire()`. La propriété du
nom est tenue par le type, non par une assertion, et ne peut pas l'être de
l'intérieur. Renommé `la_mention_obligatoire_refuse_le_critere_de_completude` ;
le corps est inchangé et l'intention d'origine passe en doc.

---

## Relevé sans correctif

**R1 — `horloge.rs:191` : `.round()` hors du périmètre mesuré par DT1.**
`Domaines::interpole` appelle `f64::round`, qui n'est ni dans le groupe à parité
exigée du banc (`+ − × ÷`, `sqrt`, `floor`, `ceil`, comparaisons, `f64 → u64`),
ni dans les sept méthodes interdites. Le verdict DT1 est explicite sur ce que le
banc ne démontre pas ; une opération non mesurée sur un chemin qui décide de la
structure des domaines est une lacune de couverture. Non corrigée pour deux
raisons : le dépôt compte trois appels de `.round()`, dont deux hors de mon
périmètre (`sim-agents/src/allocation.rs` et `sim-agents/src/usl.rs`), et
le remède propre est d'ajouter le groupe au banc, pas de réécrire un site sur
trois.

**R2 — `sim-core` n'a pas de `hors_perimetre()`.** `CLAUDE.md` en nomme deux,
pour `sim-milieu` et `sim-agents`, plus `ModeleFaute::hors_modele()`. Le cœur n'a
donc pas de liste où déclarer ses propres mécanismes sans appelant, et A2 a dû
en loger sept dans une liste dont l'objet est le modèle de faute. Balayage des
trois autres crates — implantés, testés unitairement, **aucun appelant** :
`Agregat::faibles` (EX-C08, « signalent celles à compte nul ou faible » :
la moitié « signalent » n'est exécutée par personne), `Oracle::depuis_declaration`
et `Oracle::nom_affiche` (le refus au chargement d'EX-C11 et la règle
d'affichage de PD10), `RegistreHypotheses::dementies` (NF-16),
`Config::hachage` et `Config::verifier_rejeu` (NF-03), `CoutAgent` (EX-C17, déjà
déclaré par `hors_modele`), `Service::derniere_latence`,
`Graphe::fortement_connexe`, `Graphe::composantes`,
`Generateur::connexite_conjointe`, `Horloges::ecart_maximal`,
`Horloges::derive_tiree`, `Familles::part_structurelle`, `Alea::pondere`.
Ouvrir `sim_core::hors_perimetre()` est une décision d'interface qui touche
`docs/PRD.md` et `CLAUDE.md`, que la consigne me ferme.

**R3 — EX-C06 : le modèle affiché n'est pas le modèle actif.**
`crates/sim-agents/src/scenario.rs` affiche `fautes.resume()`, c'est-à-dire
le modèle de la `Config` ; le moteur, lui, tourne sur `ModeleFaute::default()`
puisque `installer_fautes` n'est jamais appelé. `Moteur::fautes()` existe
justement pour que « le bandeau montre le modèle **actif** » et n'est pas
utilisé. Le défaut est dans `sim-agents` : hors périmètre. A2 le consigne du
côté `sim-core`.

**R4 — `detecteur.rs:111` : `Vue::derniere_sonde` est écrit et jamais lu.**
Champ privé, alimenté à chaque `sonder`, qu'aucune lecture n'utilise. Clippy ne
l'attrape pas (il est écrit). Non retiré : rien dans le PRD ne tranche s'il est
un reliquat ou l'amorce du calcul de complétude par cible, et supprimer de l'état
sans base normative est du remue-ménage.

**R5 — `moteur.rs:326` : l'ordre budget / échéance de vivacité.** `suivant()`
place `arreter_sur_violation()` avant le contrôle de budget — un commentaire
justifie explicitement ce choix — mais `oracles.echoir(date)` vient **après**.
Une échéance de vivacité qui tombe au moment même où le budget d'événements
s'épuise est donc rapportée `BudgetEvenements`, pas `Violation`. Non corrigée :
une fois le budget épuisé l'horloge n'avance plus, il n'existe donc pas de date à
laquelle faire échoir, et le raisonnement inverse est défendable. À trancher par
le PRD, pas par moi.

**R6 — `horloge.rs:72` : `ecart_maximal` sur une population vide.** `fold` sur
`NEG_INFINITY` / `INFINITY` donne `-inf`, puis `NaN` si `ecoule` vaut zéro ; les
deux se convertissent en `Duree(0)`, qui est la bonne réponse. Aucune panique,
aucun résultat faux : rien à corriger, relevé pour que le prochain lecteur ne
reparte pas dessus.

**R7 — `graphe.rs:224` : « tous les liens qui le traversent ».** Le `//!` du
module et la doc de `Courtier` annoncent qu'un courtier saturé supprime « tous
les liens qui le traversent » ; le code ne coupe un lien que si un courtier
saturé porte ses **deux** extrémités. L'écart est réel, mais il est déjà nommé
dans le test `deux_courtiers_disjoints_laissent_passer_les_liens_croises`, qui
en tire la conséquence de conception (« le modèle de courtier ne sait donc pas
exprimer deux moitiés internement connexes et mutuellement isolées »). Changer le
prédicat changerait EX-C16 ; c'est une décision de spécification.

**R8 — `verification.rs:47` : `executions_necessaires` à ε ou δ nuls.**
`ln(2/0)/(2·0²)` donne `inf`, converti en `u64::MAX` par saturation. Aucune
panique, et `Campagne::conclure` rapporte alors une absence de verdict — c'est le
comportement voulu par EX-C18. Relevé pour mémoire. **R8 n'a regardé qu'un bout
du domaine ; l'autre est C2, corrigé au tour 2, et il rend cette entrée sans
objet : ε = 0 et δ = 0 sont désormais refusés par `Parametres::refus`.**

---

# Tour 2

Réponse au jugement [`M1-critique.md`](M1-critique.md) : les deux affirmations
prises en défaut (D1, D2) et les six anomalies (C1 à C6). Chaque preuve a été
**reproduite avant correctif** depuis une crate **externe** à l'arbre —
`sim-core` en dépendance par chemin, `CARGO_TARGET_DIR` hors du chemin
accentué — de sorte que ce qui est mesuré est bien ce qu'un consommateur de la
crate voit. Rien hors de `crates/sim-core/` n'est modifié.
✎ *Motif faux — voir la note du 22 août 2026 en tête de rapport.*

## État livré

```
$ cargo clippy -p sim-core --all-targets --release
    Finished `release` profile [optimized] target(s) in 0.11s

$ cargo test -p sim-core --release
running 96 tests
test result: ok. 96 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
   Doc-tests sim_core
test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

$ cargo doc -p sim-core --no-deps
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.12s
   Generated …\doc\sim_core\index.html

$ cargo check -p sim-milieu -p sim-agents --release
    Checking sim-milieu v0.1.0 (…\crates\sim-milieu)
    Checking sim-agents v0.1.0 (…\crates\sim-agents)
    Finished `release` profile [optimized] target(s) in 1.08s
```

91 tests à la clôture du tour 1, **96** après : cinq ajoutés, aucun retiré,
aucun affaibli. Un test est renommé (`le_cout_dun_agent_retrouve_les_chiffres_du_traite`
→ `le_cout_dun_agent_retrouve_lordre_de_grandeur_du_traite`) et son corps
**gagne** six assertions ; voir C5.

---

## D1 — la parenthèse d'A5 sur `sim-viz` : affirmation fausse

**Reproduction.** Balayage des importations de `sim_core` dans `sim-viz`, à
l'état livré :

```
$ grep -rn "sim_core::" crates/sim-viz/src/
crates/sim-viz/src/lib.rs:…       sim_core::faute::ModeleFaute::hors_modele(),
crates/sim-viz/src/lib.rs:…       sim_core::couverture::Agregat::mention_obligatoire()
crates/sim-viz/src/scenario_a.rs:49:  use sim_core::temps::Granularite;
```

Trois importations, non deux. Le critique a raison.

**Ce que j'ai changé.** La phrase d'A5 est corrigée sur place et porte la marque
du défaut. Les deux renvois `crates/sim-viz/src/lib.rs:894` et `:928` sont
retirés plutôt que renumérotés : ils désignaient déjà `:906` et `:983` au moment
où j'écris, `sim-viz` étant édité en parallèle. Tout renvoi hors
`crates/sim-core/` de ce rapport est désormais donné par symbole.

**Portée du défaut.** La conclusion visée par A5 tient : `Service::LIBELLE_L99`
n'a toujours aucun appelant, ce que le `//!` de `service.rs:15-20` déclare. Le
défaut était dans la preuve, pas dans le verdict.

---

## D2 — A2, « la liste redevient exacte » : elle ne l'était pas

**Reproduction.** Balayage des deux fonctions que le critique nomme, `bancs/`
compris :

```
$ grep -rn "message_perdu\|avertissements" crates/ bancs/ --include=*.rs
crates/sim-core/src/faute.rs:238:    pub fn message_perdu(…)          ← définition
crates/sim-core/src/faute.rs:436:    pub fn avertissements(…)          ← définition
crates/sim-core/src/faute.rs:…:      (deux appels, dans ses propres tests)
crates/sim-agents/src/stigmergie.rs:176:  pub fn avertissements(…)     ← autre type
crates/sim-agents/src/scenario.rs:…:      f.params.avertissements()    ← Params, pas ModeleFaute
crates/sim-viz/src/scenario_b.rs:…:       self.params.avertissements() ← idem
```

`ModeleFaute::message_perdu` et `ModeleFaute::avertissements` n'ont aucun
appelant. Les deux appels visibles portent sur
`sim_agents::stigmergie::Params::avertissements`, homonyme sans rapport — c'est
précisément ce qui rend l'oubli facile, et c'est aussi ce qui le rend grave :
l'homonymie donne l'impression que la moitié `[U]` d'EX-C06 est câblée.

**Ce que j'ai changé.** `faute.rs:497` — la liste `hors_modele()` nomme
désormais **neuf** mécanismes sans appelant au lieu de sept :
`message_perdu` y entre avec sa mention de l'omission d'EX-C05 (le reproche du
critique porte : A2 citait « **omission** et retard de message » pour justifier
l'ajout de `retard_message` et laissait dehors la fonction qui implante
l'omission), et `avertissements` y entre avec la note sur l'homonyme, pour que
la liste ne se refasse pas prendre au même piège.

**Preuve que c'est parti.** Le texte livré, `faute.rs:497-504` :

> Sans appelant non plus, **neuf** : `tirer_pannes` (crashs par niveau),
> `Moteur::avancer_partition` (partition à deux états), `message_perdu`
> (l'omission d'EX-C05, et la coupure de partition avec elle), `injection_echec`,
> `injection_retard`, `injection_valeur`, `retard_message`, `ecriture_corrompue`,
> et `avertissements` — la moitié [U] d'EX-C06 : les avertissements affichés par
> `sim-agents` et `sim-viz` viennent de
> `sim_agents::stigmergie::Params::avertissements`, homonyme et sans rapport,
> jamais de ceux-ci.

Le balayage ci-dessus ne rend plus aucun mécanisme sans appelant qui ne soit
déclaré.

---

## C1 — `detecteur.rs:59` : la doc affirmait une garantie de type que le type ne donne pas

**Reproduction, depuis une crate externe.** `#[non_exhaustive]` interdit le
littéral, la mise à jour fonctionnelle et le filtrage exhaustif ; il n'interdit
pas l'affectation de champ, et `Proprietes` est `Copy` avec quatre champs `pub`
qu'un exemplaire rendu par `Detecteur::proprietes()` livre par valeur :

```
== C1 — Proprietes fabriquee hors de la crate malgre #[non_exhaustive]
(a) mesure   : suspicions=1       fausses=1 exactitude=Some(1.0) completude=Duree(21)..Duree(31)
(a) fabrique : suspicions=1000000 fausses=0 exactitude=Some(0.0) completude=Duree(1)..Duree(2)
```

Chiffre pour chiffre la sortie du critique. Le défaut est établi.

**Ce que j'ai changé — et ce que je n'ai pas pu changer.** Le correctif est
**documentaire**, et c'est une contrainte de périmètre, pas un choix de confort :
tenir PD12 *par le type* demande des champs privés et quatre accesseurs, ce qui
casse `crates/sim-agents/src/pair_a_pair.rs`, qui lit `p.suspicions` et
`p.fausses_suspicions`. C'est un changement d'interface hors du périmètre de cet
audit, et je le consigne comme tel plus bas.

`detecteur.rs:59-78` dit maintenant trois choses : ce que `#[non_exhaustive]`
donne réellement (l'ajout d'un champ reste non cassant), ce qu'il ne donne pas —
avec la sortie mesurée ci-dessus en bloc `text` dans la doc —, et **ce que PD12
tient quand même**, qui est plus étroit qu'annoncé : le détecteur ne prend ces
nombres que de `sonder`, une copie falsifiée ne remonte pas dans l'objet, donc
elle ne trompe qu'un affichage. La note nomme l'appelant qui bloque le correctif
par le type.

**Preuve que c'est parti.** La fabrication reste possible et le rapport ci-dessus
le montre ; ce qui disparaît est l'affirmation. `cargo doc -p sim-core --no-deps`
passe, et la doc rendue porte la mesure. Aucun test n'est ajouté : établir par
un test qu'un littéral externe ne compile pas demanderait `trybuild`, c'est-à-dire
une dépendance de développement pour une propriété que le compilateur tient déjà
et qui n'est **pas** celle qui était fausse.

---

## C2 — `verification.rs:47`, `:64`, `:206` : un verdict EX-C18 complet rendu sur zéro exécution

**Reproduction.** Le cast `as u64` de Rust est saturant. À δ ≥ 2, δ = NaN, ε = NaN
ou δ < 0, `libm::log(2/δ)` est nul, négatif ou NaN, `N` sature à 0, et
`Campagne::conclure()` traverse ses deux gardes :

```
(c) delta=2   -> N=0 ; conclut=false ; **aucune violation observée en 0 exécutions** — et non
                 « aucune violation ». […] **il n'est pas vu** (§8.4).
(c) delta=NaN -> N=0 ; idem
(c) epsilon=NaN -> N=0 ; idem
(c) delta=-1  -> N=0 ; idem
(c) avant lancement : ε = 1e-2, δ = 2e0 → **N = 0 exécutions**. Un chiffre significatif de
                 plus — ε = 1e-3 à la même confiance — en demanderait 0 , soit **cent fois plus**
```

La dernière ligne est le second défaut, que le critique ne relève pas :
l'affichage d'avant lancement, que le §8.4 rend obligatoire, annonçait un budget
nul **et** promettait « cent fois plus » de zéro.

**Ce que j'ai changé.** Une garde unique, à la source, plutôt qu'un `if n == 0`
au point de sortie : `Parametres::refus()` (`verification.rs:64`) tient le
domaine de la borne du §3.2 — `0 < ε ≤ 1` et `0 < δ < 1` — et rend la raison en
clair. `Campagne::conclure` l'interroge en premier (`:206`) et rend
`Issue::AbsenceDeVerdict` ; `affichage_avant_lancement` l'interroge aussi
(`:79`) et refuse d'afficher un N. Les comparaisons rejettent `NaN`, qui n'est
vrai pour aucune d'elles. Le domaine et non `n == 0`, parce que `δ ≥ 1` rend la
borne **vide** sans rendre N nul : ε = 10⁹ donnait `N = 1` et un verdict sur une
seule exécution, ce que le seuil sur N aurait laissé passer.

**Preuve que c'est parti.** Même binaire, même crate externe :

```
(c) delta=2     -> N=0 ; conclut=false ; **absence de verdict** : ε = 0.01 et δ = 2 sont hors du
                   domaine de la borne du §3.2, qui suppose 0 < ε ≤ 1 et 0 < δ < 1 : aucun N ne
                   s'en déduit. […] (§5.3, EX-C18).
(c) delta=NaN   -> idem      (c) epsilon=NaN -> idem      (c) delta=-1 -> idem
(c) epsilon=1e9 -> N=1 ; conclut=false ; **absence de verdict** : … hors du domaine …
(c) avant lancement : **aucune campagne à lancer** : … Le N affiché serait zéro, et une campagne
                   de zéro exécution ne mesure rien (§8.4).
```

Test ajouté, `verification.rs:342`,
`des_parametres_hors_domaine_ne_rendent_aucun_verdict` : sept réglages hors
domaine, dont il exige à chaque fois l'absence de verdict, l'absence de la phrase
« aucune violation observée », et un affichage d'avant lancement qui ne promet
rien ; plus deux réglages valides — le défaut du §8.4 et le bord `ε = 1, δ = 0,999`
— dont il exige que la garde les laisse passer. Le domaine ne se referme donc pas
sur les réglages du traité.

---

## C3 — `moteur.rs:277` : la préséance annoncée n'était tenue que sur un des trois arrêts

**Reproduction.** `arreter_sur_violation()` était placé avant
`Arret::BudgetEvenements`, mais après `Arret::Demande` et `Arret::BudgetTemps`.
Une violation **déjà au registre** était donc enterrée par les deux autres :

```
(d)     arret rapporte : Some(BudgetTemps) (violations enregistrees : 1)
(d bis) arret rapporte : Some(Demande)
(d ter) temoin sans autre motif : Some(Violation("m1"))
```

Le témoin est là pour écarter l'explication paresseuse : le mécanisme
fonctionne, c'est son rang qui est faux.

**Ce que j'ai changé.** Le contrôle remonte immédiatement après le court-circuit
`arret.is_some()`, donc **avant les trois** motifs. Le motif est une question de
date, pas de préférence : une violation enregistrée a eu lieu au tour précédent,
tandis que la demande d'arrêt et le budget de temps sont **rapportés de
l'extérieur** — `Budget::demander_arret` et `Budget::consommer_temps` — donc
postérieurs par construction. EX-C09 veut l'arrêt à l'instant de la violation ;
les trois motifs sont vrais ensemble, un seul est un défaut. Le commentaire de
`suivant()` porte la mesure ci-dessus.

**Preuve que c'est parti.**

```
(d)     arret rapporte : Some(Violation("m1")) (violations enregistrees : 1)
(d bis) arret rapporte : Some(Violation("m1"))
(d ter) temoin sans autre motif : Some(Violation("m1"))
```

Test ajouté, `moteur.rs:523`,
`une_violation_enregistree_lemporte_sur_les_autres_arrets` : les trois cas —
budget de temps, arrêt demandé, budget d'événements — chacun armé au même tour
qu'une violation enregistrée. Les deux tests existants qui exercent
`BudgetTemps` et `BudgetEvenements` sans violation passent inchangés : la
préséance ne s'applique qu'en présence d'une violation, elle ne masque pas les
autres motifs.

**Ce que ce correctif ne fait pas.** R5 reste ouvert : `oracles.echoir(date)`
vient toujours après le contrôle de budget (`moteur.rs:326`), donc une échéance
de vivacité qui *tomberait* au moment où le budget s'épuise est toujours
rapportée `BudgetEvenements`. C3 et R5 ne sont pas le même défaut — le critique
le dit lui-même : en R5 la violation n'existe pas encore, ici elle est au
registre. R5 demande de trancher si une échéance peut échoir à une date que
l'horloge n'atteindra jamais ; c'est une décision de spécification, et elle reste
au PRD.

---

## C4 — `faute.rs:436` : l'arbitrage, et sur quoi je tranche

**Reproduction.** Vingt acteurs répartis en quatre baies d'un centre, 10 000 pas,
même graine, trois réglages :

```
(e) crash_centre  = 0,09 : 928 vidages complets sur 10000 pas ; taux par acteur et par pas = 0.0928 ; avertissements() = []
(e) crash_machine = 0,09 :   0 vidages complets sur 10000 pas ; taux par acteur et par pas = 0.0905 ; avertissements() = []
(e) crash_baie    = 0,09 :   1 vidage  complet  sur 10000 pas ; taux par acteur et par pas = 0.0903 ; avertissements() = []
```

Le cas du critique est reproduit : un centre unique à 0,09 vide toute la
population 9,3 % des pas, et rien n'est dit.

**Sur quoi je tranche.** La mesure contredit le diagnostic du critique, et
confirme le défaut.

Le diagnostic était : « avant A1, les trois taux avaient de fait le même
dénominateur ; depuis, la somme additionne des probabilités de dénominateurs
différents, donc le seuil sous-avertit ». C'est faux, et la deuxième colonne le
montre : **le taux par acteur est le même dans les trois lignes** — 0,0928,
0,0905, 0,0903 pour un réglage de 0,09. Il ne pouvait pas en aller autrement.
Chaque acteur appartient à exactement une machine, une baie et un centre ; sa
probabilité de tomber à un pas est `1 − (1−p_m)(1−p_b)(1−p_c)`, dont la somme des
trois taux est le majorant par union — **avant A1 comme après**. A1 a changé le
nombre de tirages consommés et la corrélation entre acteurs, pas l'espérance par
acteur. Le seuil n'a donc jamais cessé de mesurer la grandeur qu'il mesurait.

Ce qu'A1 a réellement changé est dans la **première** colonne, et aucun des trois
taux ne l'exprime : à espérance par acteur identique, `crash_centre` produit 928
vidages complets et `crash_machine` **zéro**. C'est la différence entre une
population qui s'érode et une population qui disparaît d'un coup, et c'est
exactement ce que le §3.3 vise — « éviter de pousser le système dans un espace
d'états restreint ». Un essaim vidé en bloc n'explore pas ; il n'existe pas.

Je tranche donc sur la **grandeur**, mais pas dans la direction demandée :

1. **Le seuil de 0,1 reste, et sa formulation nomme enfin ce qu'il mesure** — « par
   pas **et par acteur** ». Le corriger aurait été corriger une grandeur juste.
2. **J'ajoute l'avertissement qu'A1 rend nécessaire**, sur la corrélation, qui est
   un **régime** et non un taux. Il se signale donc **sans seuil**, exactement
   comme « partition sans probabilité de sortie » — l'autre avertissement de
   régime du même corps, qui ne porte lui non plus aucune constante. C'est aussi
   la seule forme qui ne fabrique pas un chiffre sans provenance : ni le §3.3 ni
   le PRD ne donnent de seuil pour une panne corrélée, et le 0,1 existant n'en a
   déjà pas.

**Preuve que c'est parti.**

```
(e) crash_centre  = 0,09 : 928 vidages … ; avertissements() = ["crash corrélé : une baie tombe en
    entier avec la probabilité 0.000000 par pas, un centre avec 0.090000 — la population se vide
    d'un coup au lieu de perdre quelques membres, et aucun taux par acteur ne distingue les deux
    régimes (§3.3, §8.3)"]
(e) crash_machine = 0,09 :   0 vidages … ; avertissements() = []
(e) crash_baie    = 0,09 :   1 vidage  … ; avertissements() = ["crash corrélé : une baie tombe en
    entier avec la probabilité 0.090000 par pas, un centre avec 0.000000 — …"]
```

Le cas grave du critique déclenche ; le cas décorrélé de même espérance ne
déclenche pas. Test ajouté, `faute.rs:742`,
`un_crash_correle_est_signale_meme_sous_le_seuil_cumule`, qui vérifie d'abord
que le cas est bien **sous** le seuil cumulé — sans quoi il ne prouverait rien.
`le_modele_par_defaut_ne_produit_aucune_faute` passe inchangé : les deux taux de
niveau valent zéro au défaut, donc le régime ne se signale pas.

**Réserve, et elle est réelle.** `ModeleFaute::avertissements` n'a **aucun
appelant** (voir D2) : cet avertissement est calculé et affiché par personne.
Sur un résultat, cela a l'effet d'un avertissement absent. Il est déclaré comme
tel dans `hors_modele()`.

---

## C5 — `service.rs:27`, `:83`, `:203` : l'arbitrage, et sur quoi je tranche

**Reproduction.** Le §2.2 (`Traité.md:582`) donne, textuellement : « de l'ordre
de trois cents mots, soit **quelques milliers d'octets** sur une architecture
64 bits, dont **233 mots** de zone de tas, pile comprise : la documentation
d'OTP 29.0.5 annonce **327** mots à son guide d'efficacité, sur une transcription
qui affiche OTP 27, et **338** à sa page de mémoire ; l'écart est explicable, et
**il reste la meilleure raison de ne rien gager sur le chiffre exact** », puis
« le plancher mémoire d'un million d'agents de ce type est donc de l'ordre de
**2,6 Go** avant tout état applicatif ».

État trouvé :

```
(f) octets() = 2616 ; source = « §2.2 — valeur de documentation, périssable (annexe B) »
$ grep -c "2 616\|2616" Traité.md
0
```

Le code retenait 327, laissait tomber 338 **et** la mise en garde, et épinglait
le produit par `assert_eq!(c.octets(), 2_616)` sous le nom
`le_cout_dun_agent_retrouve_les_chiffres_du_traite`. Le critique a raison sur les
trois points : le chiffre est absent de la source, la source refuse
explicitement de le donner, et le nom du test affirme le contraire.

**Sur quoi je tranche.** Non pas entre « garder » et « retirer » l'assertion,
mais sur **ce dont elle est la preuve**. Deux choses étaient confondues sous un
seul nom :

- `327` est un **réglage** — il faut un nombre pour calculer, la source en donne
  deux et refuse d'arbitrer. Un réglage se documente et se garde contre la
  dérive ; il ne se présente pas comme une mesure.
- `2 616` est l'**arithmétique** de ce réglage — `327 × 8`. Elle est exacte, et
  elle ne dit rien du traité.
- Ce que le traité permet de **retrouver**, au sens de NF-15, est un ordre de
  grandeur : 233 mots de tas, « quelques milliers d'octets », « de l'ordre de
  2,6 Go » pour un million. C'est cela, et cela seul, qui répond à NF-15.

Je garde donc les deux assertions arithmétiques — les retirer affaiblirait le
test, et la consigne l'interdit à juste titre : une garde de non-régression sur
un défaut public est utile — mais elles cessent d'être présentées comme des
chiffres du traité, et le test gagne les assertions qui, elles, retrouvent la
source. **NF-15 est ainsi tenue au sens strict : on retrouve ce que le traité
donne, on ne fabrique pas ce qu'il refuse.**

**Ce que j'ai changé.**

- `service.rs:27-42` — la doc de `CoutAgent` porte les deux chiffres, le refus
  d'arbitrer, l'ordre de grandeur dérivé, et dit en toutes lettres que « 2 616
  octets » n'est pas dans le traité.
- `service.rs:83` — `CoutAgent::SOURCE` ne dit plus « §2.2 — valeur de
  documentation, périssable » mais porte la citation, les deux chiffres, la mise
  en garde et la phrase « le défaut retient 327 : réglage, non arbitrage ».
  C'est la constante que F1/F2 destinent à l'affichage : afficher « 327 mots »
  seul ferait passer un réglage pour une mesure.
- `service.rs:203` — le test devient
  `le_cout_dun_agent_retrouve_lordre_de_grandeur_du_traite` et passe de trois à
  neuf assertions : 233 mots de tas ; le défaut compris entre les deux chiffres
  de la source ; « quelques milliers d'octets » ; « de l'ordre de 2,6 Go » à
  ±10 % pour un million ; la provenance qui porte 327, 338 et la mise en garde ;
  puis, sous un commentaire qui dit ce qu'elles sont, les deux assertions
  arithmétiques d'origine.

**Preuve que c'est parti.**

```
(f) octets() = 2616 ; source = « §2.2 — « de l'ordre de trois cents mots, soit quelques milliers
    d'octets […] dont 233 mots de zone de tas, pile comprise » ; OTP 29.0.5 annonce 327 mots à son
    guide d'efficacité et 338 à sa page de mémoire, « et il reste la meilleure raison de ne rien
    gager sur le chiffre exact ». Le défaut retient 327 : réglage, non arbitrage. Valeur périssable
    (annexe B) »
```

L'ordre de grandeur du traité tient pour **les deux** chiffres qu'il donne :
327 × 8 × 10⁶ = 2,616 Go et 338 × 8 × 10⁶ = 2,704 Go, tous deux « de l'ordre de
2,6 Go ». Le test passerait donc si le réglage basculait sur 338, et c'est le
comportement voulu : la source ne tranche pas, le test non plus.

---

## C6 — `detecteur.rs:205`, `service.rs:69` et `:75` : multiplications nues sur champs publics

**Reproduction.** Profil release du dépôt, sans `overflow-checks` :

```
(g) periode = 2^63, seuil = 3 -> completude = 1..9223372036854775809 tics
(g) 2305843009213693952 mots x 8 -> octets() = 0
(g) octets() = 8796093022208 ; plancher(u32::MAX) = 18446735277616529408
```

La première ligne est la plus mauvaise des trois : le détecteur **le plus lent
représentable** annonçait une détection en **1 tic**. Un enroulement qui rend un
grand nombre se remarque ; un enroulement qui rend « instantané » se croit.

**Ce que j'ai changé.** Trois `saturating_mul`, et rien d'autre — c'est la
convention déjà tenue par `Instant + Duree`, `Instant − Instant`, `Duree + Duree`
(`temps.rs:88-114`) et par les deux gardes de saturation de `faute.rs`. Chacune
porte en doc l'unité et le cas d'enroulement qu'elle ferme.

**Preuve que c'est parti.**

```
(g) periode = 2^63, seuil = 3 -> completude = 18446744073709551615..18446744073709551615 tics
(g) 2305843009213693952 mots x 8 -> octets() = 18446744073709551615
(g) octets() = 8796093022208 ; plancher(u32::MAX) = 18446744073709551615
```

Deux tests ajoutés : `detecteur.rs:357`
(`la_completude_sature_au_lieu_de_senrouler`) et `service.rs:241`
(`le_cout_sature_au_lieu_de_senrouler`).

---

## Ce qui reste ouvert, et qui n'est pas dans mon périmètre

Ces trois points demandent une décision hors `crates/sim-core/` ; ils sont
consignés ici et **rien n'a été édité** dans `docs/PRD.md` ni
`docs/decisions.md`.

1. **C1 ne se ferme pas par le type sans changer une interface.** Rendre les
   quatre champs de `Proprietes` privés derrière des accesseurs tiendrait PD12
   *par le type*, et casserait `crates/sim-agents/src/pair_a_pair.rs`. Décision
   d'interface : à prendre à la consolidation, pas dans un audit de crate.
2. **`ModeleFaute::avertissements` n'a aucun appelant** (D2, C4). La moitié `[U]`
   d'EX-C06 — « l'interface avertit » — n'est donc tenue par personne, et
   l'avertissement ajouté en C4 hérite de cette réserve. Le §0 du PRD devrait la
   porter : elle est de la même famille que les dix mécanismes sans appelant
   qu'il énumère déjà.
3. **R2 reste entier** : `sim-core` n'a pas de `hors_perimetre()`, et la liste
   d'absences du cœur continue de loger dans `ModeleFaute::hors_modele()`, dont
   ce n'est pas l'objet. Neuf entrées y tiennent maintenant au lieu de sept.
   Ouvrir `sim_core::hors_perimetre()` touche `docs/PRD.md` et `CLAUDE.md`.

*Mesures du tour 2 prises depuis une crate hors arbre dépendant de `sim-core` par
chemin, `CARGO_TARGET_DIR` sur un chemin ASCII. Aucun fichier hors de
`crates/sim-core/` et de ce rapport n'est modifié.*
✎ *Motif faux — voir la note du 22 août 2026 en tête de rapport.*
