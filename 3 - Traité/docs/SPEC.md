# SPEC — le contrat d'implantation

## 0. Ce que ce document est, et ce qu'il n'est pas

Trois documents décrivent le même logiciel sous trois angles, et les confondre
fait perdre du temps :

| Document | Répond à | Autorité |
|---|---|---|
| [`PRD.md`](PRD.md) | **Qu'est-ce qui est exigé, et pourquoi ?** | Le traité. Chaque exigence porte un code et une citation |
| [`architecture.md`](architecture.md) | **Où est quoi, et que refuse de savoir chaque couche ?** | Le §5 du PRD |
| **`SPEC.md`** (ici) | **Que garantit le code effectivement compilé ?** | Le code. Chaque énoncé de ce document est vérifiable par lecture d'une signature ou exécution d'un test |

La différence n'est pas de style. Le PRD dit *le milieu doit garantir M3* ; ce
document dit *`Milieu::lire` ne rend que des enregistrements durables, et
`Milieu::ecrire` rend un `delai_durabilite` que l'appelant planifie lui-même*. Le
premier est une exigence, le second est un contrat opposable : si le code
change, ce document devient faux, et c'est ce qui le rend utile.

**Règle de rédaction.** Aucun énoncé de ce document ne vient du PRD. Chacun est
tiré du code ou d'une exécution, et porte le chemin qui permet de le vérifier.
Là où le code ne tient pas ce que le PRD exige, ce document dit **ce que le code
fait**, avec un renvoi vers la réserve correspondante du §0 du PRD — jamais
l'exigence à la place de la réalité.

**État mesuré au 17 août 2026, 09 h 49** : **465 tests**, `cargo test --workspace --release`,
exit 0 ; clippy et rustdoc à 0, `cargo clippy --workspace --all-targets --release`
et `cargo doc --workspace --no-deps` à 09 h 50. Le §0
du PRD enregistre 348 à la clôture de la phase 5 ; la phase 6 a porté le compte à
419, l'audit du 13 août à 428, et celui du 17 août à 447 puis 465 — des tests
ajoutés pour fermer des trous que ces révisions ont ouverts, aucun affaibli.
**Ce compte est une mesure, pas une constante** : il ne se cite pas, il se refait
par la ligne ci-dessus — 428 à 08 h 10, 447 à 08 h 32 et 465 à 09 h 49 le même
jour, cinq agents écrivant en parallèle.

**Règle de lecture des blocs de code.** Les blocs `rust` de ce document sont des
**esquisses de signature** : ils donnent les items dont un énoncé dépend, jamais
la surface publique complète. Un item absent d'un bloc n'est pas un item absent
du code. En revanche, un item **présent** dans un bloc est présent tel quel dans
le code, paramètres compris — c'est ce qui rend le document opposable.

---

## 1. Le contrat de déterminisme

C'est le contrat fondateur : tous les autres reposent sur lui (PD1, NF-01 à
NF-04).

### 1.1 Ce qui suffit à rejouer

```rust
// sim-core/src/lib.rs
pub struct Config {
    pub graine: u64,
    pub granularite: temps::Granularite,
    pub fautes: faute::ModeleFaute,
    pub evenements_max: u64,
    pub secondes_coeur_max: Option<f64>,
    pub scenario: String,
}
```

`Config` **est** l'entrée complète d'une exécution : rien d'autre n'influence sa
trace. Trois méthodes en font un contrat plutôt qu'une structure de commodité :

| Méthode | Garantie |
|---|---|
| `Config::hachage() -> u64` | Empreinte de la configuration entière, modèle de faute compris. Deux configurations qui diffèrent d'un seul champ ont deux hachages |
| `Config::entete() -> String` | La ligne écrite en tête de tout export : version du binaire et hachage (NF-03) |
| `Config::verifier_rejeu(version_export, hachage_export) -> Result<(), String>` | **Refuse** le rejeu sur une version différente, au lieu de le tenter. Le refus est une `Err`, pas un avertissement |

Le champ `scenario` est dans le hachage pour une raison de conception, non de
traçabilité : DT10 règle la granularité par scénario, donc deux exécutions de
scénarios différents ne se comparent pas. Le hachage rend l'incomparabilité
visible plutôt que de l'interdire par un contrôle séparé.

### 1.2 La source unique d'aléa

```rust
// sim-core/src/alea.rs
pub struct Alea { /* ChaCha8Rng semé */ }
impl Alea {
    pub fn nouveau(graine: u64) -> Self;
    pub fn graine(&self) -> u64;
    pub fn tirages(&self) -> u64;      // compteur de tirages consommés
    pub fn bits(&mut self) -> u64;
    pub fn uniforme(&mut self) -> f64;
    pub fn entier(&mut self, n: u64) -> u64;
    pub fn bernoulli(&mut self, p: f64) -> bool;
    pub fn exponentielle(&mut self, moyenne: f64) -> f64;
    pub fn pondere(&mut self, poids: &[f64]) -> Option<usize>;
    pub fn pondere_avec(poids: &[f64], u: f64) -> Option<usize>;
}
```

Contrat : **il n'existe aucun autre générateur d'aléa que `ChaCha8Rng` semé, et
aucune graine qui ne descende de `Config::graine`.** Aucun `thread_rng`, aucune
horloge, aucune adresse mémoire n'entre dans un tirage.

**Ce que le contrat ne dit pas, et qu'il faut lire.** Il n'y a pas *une* instance
d'`Alea` par exécution. Le scénario A en sème une (`scenario.rs`,
`Alea::nouveau(graine)`) et le scénario B en sème une seconde pour l'amorçage,
`Alea::nouveau(graine ^ 0x5eed)`, à côté de celle que porte le moteur. PD1 tient
— les deux descendent de la même graine, le rejeu est exact, et cent graines
distinctes rendent cent traces distinctes. Ce qui ne tient pas est la portée du
compteur : `Alea::tirages()` ne compte que les tirages de **son** instance, donc
une divergence de chemin survenue pendant l'amorçage ne s'y verrait pas.

Conséquence pour tout code nouveau : une fonction qui a besoin d'aléa prend
`&mut Alea` en paramètre. Elle ne le crée pas, ne le stocke pas, ne le clone pas.

### 1.3 Ce que le lint fait respecter

`clippy.toml` porte des interdictions structurelles, pas du style, et chacune
est un contrat :

| Interdit | Raison mesurée | Remplacement |
|---|---|---|
| `f64::ln`, `exp`, `powf`, `sin`, `cos`, `atan2` | Divergent entre natif et `wasm32-unknown-unknown` : elles viennent de la bibliothèque mathématique de la plateforme, que IEEE-754 ne normalise pas | `libm::log`, `libm::exp`, `libm::pow`, `libm::sin`, `libm::cos`, `libm::atan2` |
| `f64::mul_add` | Mesurée **identique**, et interdite quand même : son verdict a changé entre deux passages du banc, après installation de mingw. Dépendre de la machine de construction est pire que diverger | `a * b + c`, ou `libm::fma` si l'arrondi unique est voulu |
| `std::collections::HashMap`, `HashSet` | Itération non ordonnée : tout chemin d'ordonnancement en dépendrait silencieusement | `BTreeMap`, `BTreeSet`, `IndexMap` |

**Ces interdictions sont opposables, et elles ne l'étaient pas.**
`disallowed_methods` et `disallowed_types` appartiennent au groupe `style` de
clippy, donc à `warn` par défaut : `cargo clippy --workspace --all-targets
--release` sortait **0 sur du code qui appelle `f64::ln` et construit un
`HashMap`**. Le `[workspace.lints.clippy]` du `Cargo.toml` racine les passe en
`deny`, et les six membres l'héritent par `[lints] workspace = true`. Vérifié :
un `x.ln()` introduit dans `sim-core` fait sortir clippy en 101.

Le profil `release` du workspace ne réintroduit aucune option d'arithmétique
relâchée : Rust ne contracte pas les expressions flottantes et n'active jamais
`fast-math`.

**Un trou connu, et il n'est pas linté.** `std::time::Instant` **panique** sur
`wasm32-unknown-unknown` ; le correctif est `web_time::Instant`. Aucun lint ne
l'attrape, parce que sur cible native `web_time::Instant` *est*
`std::time::Instant` par réexport et clippy résout le chemin canonique — le lint
frappait le correctif en même temps que le défaut. La construction WASM ne le
voit pas non plus : le type compile pour cette cible et ne panique qu'à
l'exécution. Voir [`decisions.md`](decisions.md).

---

## 2. Le contrat du moteur

```rust
// sim-core/src/moteur.rs
pub struct Evenement<C> { /* date: Instant, seq: u64, cible: ActeurId, charge: C */ }
pub struct Moteur<C> {
    pub granularite: Granularite, pub alea: Alea, pub fautes: ModeleFaute,
    pub oracles: Registre, pub couverture: Couverture, pub budget: Budget,
    pub hypotheses: RegistreHypotheses, /* file, horloge, sequence, trace, arret : privés */
}
impl<C> Moteur<C> {
    pub fn nouveau(graine: u64, granularite: Granularite, budget: Budget) -> Moteur<C>;
    pub fn pousser(&mut self, delai: Duree, cible: ActeurId, charge: C);
    pub fn pousser_a(&mut self, date: Instant, cible: ActeurId, charge: C);
    pub fn suivant(&mut self) -> Option<Evenement<C>>;
    pub fn maintenant(&self) -> Instant;
    pub fn trace(&self) -> Trace;
    pub fn arret(&self) -> Option<&Arret>;
}
```

### 2.1 Le moteur est passif, et c'est un interdit

`suivant()` rend l'événement de date minimale et avance l'horloge. **Il n'appelle
aucun gestionnaire.** L'appelant exécute le traitement, puis réinjecte par
`pousser`. Il n'existe pas de trait « gestionnaire », et il ne doit pas y en
avoir : un trait à une seule implantation est le cadriciel que RQ3 surveille.

### 2.2 L'ordre est total et ne dépend d'aucun conteneur

```rust
impl<C> Ord for Evenement<C> {
    fn cmp(&self, autre: &Self) -> Ordering {
        autre.date.cmp(&self.date).then_with(|| autre.seq.cmp(&self.seq))
    }
}
```

Tas binaire inversé : minimum en tête. Les égalités de date sont départagées par
`seq`, compteur monotone attribué à l'insertion — **jamais** par l'ordre
d'itération d'un conteneur (EX-C03). C'est la clause qui rend `BinaryHeap`
admissible malgré son instabilité : deux événements de même `(date, seq)`
n'existent pas.

### 2.3 L'ordre des contrôles dans `suivant()` est un contrat, pas un détail

L'ordre exact, tel qu'implanté :

1. arrêt déjà posé → `None` ;
2. arrêt demandé → `Arret::Demande` ;
3. budget de secondes-cœur épuisé → `Arret::BudgetTemps` ;
4. **violation de sûreté du tour précédent** → arrêt (EX-C09) ;
5. budget d'événements épuisé → `Arret::BudgetEvenements` ;
6. file vide → `Arret::FileVide` ;
7. **échéance des vivacités bornées, éprouvée contre la date du *prochain*
   événement** → arrêt si elle tombe ;
8. extraction, avance de l'horloge **sans aucune attente réelle**, absorption
   dans la trace.

Deux de ces positions sont contre-intuitives et délibérées. La violation de
sûreté est testée **avant** le budget : une exécution qui viole au dernier
événement de son budget doit rapporter la violation, pas l'épuisement — les deux
motifs sont vrais, un seul est un défaut. Et l'échéance des vivacités est
éprouvée contre la date du prochain événement plutôt qu'après l'avoir extrait :
sinon une échéance enjambée par un saut de temps ne se verrait pas, et l'état
final se retrouverait au-delà de l'instant de la violation.

### 2.4 La trace de rejeu

```rust
pub struct Trace(u64);
```

`suivant()` absorbe `date`, `seq` et `cible` de chaque événement. `Trace::valeur()`
est l'empreinte comparée par NF-04 : deux exécutions de même graine rendent la
même valeur, cent graines distinctes en rendent cent distinctes. Elle ne porte
**pas** les charges — c'est un condensé d'ordonnancement, pas de contenu.

### 2.5 Le temps est logique, jamais mural

```rust
// sim-core/src/temps.rs
pub enum Granularite { /* … */ }
pub struct Instant(pub u64);
pub struct Duree(pub u64);
impl Granularite {
    pub fn nanosecondes(self) -> u64;
    pub fn unite(self) -> &'static str;
    pub fn tics_depuis_ms(self, ms: f64) -> Duree;
    pub fn ms_depuis_tics(self, d: Duree) -> f64;
}
```

`Instant` et `Duree` sont des compteurs de tics, sans rapport avec l'horloge de
la machine. Aucune conversion vers un temps mural n'existe dans `sim-core`.

**Deux horloges murales existent dans le dépôt, et une seule est sur un chemin de
simulation.** Celle de `sim-viz` sert l'affichage d'EX-V07 et passe par
`web_time` (`scenario_a.rs`, `scenario_b.rs`) — c'est la seule que NF-02 et NF-12
concernent. La seconde est dans `crates/sim-agents/examples/banc_nf05.rs`, en
`std::time::Instant`, et elle **est l'objet du banc** : NF-05 se mesure en
secondes-cœur, donc en temps mural. Aucun test ne l'exerce (NF-12 tenue).

---

## 3. Le contrat des oracles

```rust
// sim-core/src/oracle.rs
pub enum Classe {
    Surete,
    VivaciteBornee { horizon: Duree },
}
pub enum Portee {
    Globale,
    Locale { contre_exemple: &'static str, reglage_fautif: &'static str },
}
impl Oracle {
    pub fn surete(nom: &'static str, source: &'static str) -> Oracle;
    pub fn vivacite_bornee(nom: &'static str, horizon: Duree, source: &'static str) -> Oracle;
    pub fn local(self, contre_exemple: &'static str, reglage_fautif: &'static str) -> Oracle;
    pub fn depuis_declaration(nom, classe: &str, horizon: Option<Duree>, source)
        -> Result<Oracle, String>;
}
```

### 3.1 La vivacité non bornée n'est pas représentable

Il n'existe **aucun** constructeur qui produise une vivacité sans horizon : c'est
PD2 tenu par le type et non par la revue. `depuis_declaration` — le constructeur
prévu pour un chargement de configuration, **aujourd'hui sans appelant** : les
quinze oracles armés le sont par littéral — rend une `Err` si la classe déclarée
est une vivacité et que l'horizon manque (EX-C11).

### 3.2 Un prédicat local porte son contre-exemple ou n'existe pas

`Portee::Locale` a deux champs obligatoires : ce que le prédicat *paraît* dire,
et le réglage qui le met en défaut. Un `Portee::Locale` sans ces deux champs ne se
construit pas.

**Mais rien ne les affiche.** `Registre::criteres_locaux()` les rend, et n'a aucun
appelant hors d'un test de `sim-core` ; `sim-viz` ne connaît ni la méthode, ni le
mot « critère local ». Le seul oracle `Portee::Locale` du produit, `ACCORD_LOCAL`,
n'est de surcroît armé par aucune exécution. La donnée que PD10 exige de livrer
existe, est remplie, et n'est lue par personne :
`sim_agents::hors_perimetre()` le déclare.

### 3.3 Le catalogue des oracles nommés

Ce sont les seuls oracles armés par un mécanisme du produit, avec leur crate
d'origine. Un oracle qui n'est pas dans cette liste n'est pas armé.

| Nom de constante | Classe | Crate · module | Ce qu'il refuse |
|---|---|---|---|
| `M1` | `[S]` | `sim-milieu::journal` | Ordre total dans une partition |
| `M2` | `[S]` | `sim-milieu::journal` | Aucun ordre entre partitions |
| `M3` | `[S]` | `sim-milieu::journal` | Un enregistrement lu est durable |
| `M4` | `[S]` | `sim-milieu::journal` | Le compactage ne réordonne pas |
| `M10` | `[S]` | `sim-milieu::journal` | Le compactage préserve l'état final lisible |
| `R1` | `[S]` | `sim-milieu::replication` | Tout enregistrement accusé est présent chez tout meneur ultérieur |
| `R2` | `[S]` | `sim-milieu::replication` | Un enregistrement lisible a été répliqué à tout l'ISR |
| `UN_SEUL_PROPRIETAIRE` | `[S]` | `sim-milieu::groupe` | Chaque partition est affectée à au plus un membre |
| `TOUTE_PARTITION_A_UN_PROPRIETAIRE` | `[L]` | `sim-milieu::groupe` | Vivacité **conditionnelle** : après expiration du délai de session |
| `PLANCHER` | `[S]` | `sim-agents::stigmergie` | Le plancher d'exploration calculé n'est jamais franchi |
| `HORS_DOMINANTE` | `[S]` | `sim-agents::stigmergie` | La fraction d'effort hors dominante ne descend pas sous sa borne |
| `CONSERVATION` | `[S]` | `sim-agents::agregation` | Conservation de masse de l'agrégation |
| `ACCORD_LOCAL` | `[S]` | `sim-agents::alignement` | Écart aux voisins ≤ ε pendant R tours — **critère local** |
| `D1` | `[S]` | `sim-agents::directive` | Aucune directive d'époque inférieure appliquée après une supérieure |
| `D2` | `[L]` | `sim-agents::directive` | Toute directive finit par être accusée par les agents vivants |

**Armé n'est pas évalué, et dix lignes de ce tableau sont dans ce cas.**
`CONSERVATION`, `ACCORD_LOCAL`, `D1`, `D2`, `UN_SEUL_PROPRIETAIRE` et
`TOUTE_PARTITION_A_UN_PROPRIETAIRE` sont déclarés et leurs `armer_oracles` n'ont
d'appelant que dans leurs propres tests : **six** oracles qu'aucune exécution
n'arme. Les neuf autres le sont — `PLANCHER` et `HORS_DOMINANTE` par le
scénario B, M1 à M4 et M10 par le journal, R1 et R2 par le scénario D. `R2` est armé à chaque exécution mais **n'a aucun prédicat** — il
tient par construction d'`avancer_visibilite`, comme M2 et M3 tiennent par
construction du journal. Et les prédicats de M1, M4 et M10, eux armés, ne sont
appelés par aucune exécution : `Milieu::verifier` n'a d'appelant que dans un test.
Les deux `hors_perimetre()` le déclarent, entrée par entrée.

Aucun oracle n'a été ajouté par la phase 6, et c'est un fait à lire : le ch. 8 ne
produit aucune propriété réfutable par une trace finie. Ce qu'il produit est un
**paramètre d'ordre** (Φ_c, une mesure), des **refus au chargement** (Φ_c
multipartition, pondération sur issues non vérifiables) et un **effacement de
borne** (NF-14). Le catalogue reste donc à quinze.

**Un manque, et il est au registre.** Les trois mécanismes d'accord du §5.1 **du traité**
portent des prédicats *ad hoc*, hors du registre de `sim-core` et donc hors de
ses garanties PD2. `sim_agents::hors_perimetre()` le déclare. Un oracle du §5.1 **du traité**
ajouté doit passer par `Registre::armer`, pas par un booléen local.

### 3.4 Une violation est datée, une attente échoit

| Appel | Effet |
|---|---|
| `Registre::violer(nom, date, details)` | Consigne une violation de sûreté à l'instant exact. Le moteur s'arrête au tour suivant (EX-C09) |
| `Registre::attendre(nom, maintenant, details)` | Ouvre une attente de vivacité bornée |
| `Registre::satisfaire(nom)` | Ferme l'attente |
| `Registre::echoir(maintenant)` | Convertit en violation toute attente dont l'horizon est dépassé |

La conséquence pratique : une vivacité bornée qui ne se réalise pas **expire** au
lieu d'échouer, ce qui distingue « pas encore » de « jamais » — et c'est
exactement la distinction que PD2 protège.

---

## 4. Le contrat du modèle de faute et du détecteur

### 4.1 Le modèle de faute est versionné

```rust
// sim-core/src/faute.rs
pub const VERSION_MODELE: u32 = 1;
pub struct ModeleFaute;
impl ModeleFaute {
    pub fn resume(&self) -> Vec<(&'static str, String)>;
    pub fn avertissements(&self) -> Vec<String>;
    pub fn hors_modele() -> &'static [&'static str];
}
```

`VERSION_MODELE` entre dans le résumé affiché : un résultat produit sous un
modèle de faute est illisible sans savoir lequel (PD6). `avertissements()` porte
la mise en garde d'EX-C06 — un taux de fautes excessif réduit l'exploration au
lieu de l'augmenter.

Ce que le modèle sait produire : omissions et retards de message, partition
réseau comme **processus à deux états** (`Partition::nouvelle(p_entree, p_sortie, pas)`),
crashs par niveau (`Niveau`, `Domaine`, `Panne`), gigue, corruption d'écriture non
synchronisée, et trois points d'injection (`Injection`) — échec d'une opération
d'ordinaire réussie, retard d'une opération d'ordinaire rapide, valeur inhabituelle
d'un paramètre.

**Ce qu'il ne produit pas est déclaré par `hors_modele()`, et la première entrée
est la plus lourde** : aucun scénario livré ne règle `Config.fautes`. Ni la
partition à deux états, ni les crashs par niveau, ni les points d'injection ne
sont jamais tirés. Les omissions du scénario A viennent d'un taux propre à
`sim-agents::pair_a_pair` — deux mécanismes pour la même faute, dont un seul est
versionné avec la configuration.

### 4.2 Le détecteur soupçonne, et son exactitude est calculée

```rust
// sim-core/src/detecteur.rs
pub enum Etat { /* Sain | Suspect | Retire */ }
pub struct Proprietes { /* complétude, exactitude */ }
impl Detecteur {
    pub fn nouveau(periode: Duree, expiration: Duree, seuil: u8) -> Detecteur;
    pub fn defauts_documentes(tics_par_seconde: u64) -> Detecteur;
    pub fn completude(&self) -> (Duree, Duree);
    pub fn proprietes(&self) -> Proprietes;
    pub fn etat(&self, cible: ActeurId) -> Etat;
    pub fn sonder(&mut self, cible, vivant: bool, latence: Duree, maintenant: Instant) -> Etat;
    pub fn retirer(&mut self, cible, action: &str, autorisation: &str) -> String;
}
impl Proprietes {
    pub fn exactitude(&self) -> Option<f64>;   // None tant que rien n'a été sondé
}
```

Quatre clauses tenues par les types, non par la convention (PD12) :

- **`Etat` n'a pas de variante `Mort`.** L'état d'un agent aux yeux d'un autre
  est *sain*, *suspect* ou *retiré*. « Mort » n'est pas une observation, c'est
  une action — d'où `retirer(cible, action, autorisation)`, qui exige de nommer
  l'action et son autorisation, et rend la phrase affichée.
- **L'exactitude est un `Option<f64>` calculé**, jamais un paramètre : elle vient
  du rapport entre fausses suspicions et **suspicions portées** — non entre
  fausses suspicions et sondages, qui ne donnent pas le même nombre. Le
  dénominateur ne s'incrémente qu'au franchissement du seuil, donc l'exactitude
  vaut `None` **tant qu'aucune suspicion n'a été portée**, et pas seulement avant
  le premier sondage : un détecteur qui a sondé mille fois sans jamais suspecter
  rend encore `None`. `Proprietes` est `#[non_exhaustive]`, ce qui interdit de la
  construire par littéral hors de `sim-core` — sans quoi la clause serait tenue
  par la convention et non par le type.
- **La complétude est une paire de bornes** (`completude() -> (Duree, Duree)`),
  pas un scalaire — c'est l'intervalle 21–31 s aux défauts documentés, dont le
  30 s du traité est l'arrondi.
- `defauts_documentes` construit le détecteur aux valeurs de plateforme
  (période 10 s, expiration 1 s, seuil 3) et prend la granularité en argument :
  une constante de temps ne se code pas en tics. **Aucun appelant de production**
  ne l'emploie : le seul détecteur armé du produit est celui de
  `sim-agents::pair_a_pair`, dont l'expiration est dérivée de l'aller simple. Le
  `timeoutSeconds = 1 s` qu'EX-C12 nomme en exemple n'est donc pas armé, et
  l'intervalle 21–31 s ci-dessus est celui d'un détecteur que seuls des tests
  construisent.

**DT6 n'est pas tenue, et le contrat le dit.** L'objet est unique dans
`sim-core`, mais il n'a **qu'un** consommateur, `sim-agents::pair_a_pair` ;
`sim-milieu` n'en instancie aucun (il tient `delai_session` et le seuil de retard
en propre) et le sondage indirect est un second objet,
`sim-agents::soupcon::DetecteurInfectieux`, avec ses propres compteurs.

---

## 5. Le contrat du milieu

### 5.1 Le milieu ne planifie rien

```rust
// sim-milieu/src/journal.rs
impl Milieu {
    pub fn ecrire(&mut self, partition: u32, cle: Cle, valeur: f64,
                  date_evenement: Instant, identite: Identite,
                  alea: &mut Alea) -> Ecriture;
    pub fn valider(&mut self, e: Ecriture) -> bool;
    pub fn lire(&mut self, partition: u32, depuis: u64, max: usize) -> Vec<Enregistrement>;
    pub fn lire_multi(&mut self, curseurs: &[(u32, u64)], budget_total: usize,
                      alea: &mut Alea) -> Vec<Enregistrement>;
    pub fn compacter(&mut self, partition: u32) -> Vec<Enregistrement>;
    pub fn appliquer_retention(&mut self, partition: u32, maintenant: Instant, r: Duree) -> u64;
}
```

`ecrire` rend une `Ecriture` portant un `delai_durabilite` ; **c'est l'appelant
qui en fait un événement.** Sans cette clause, `sim-milieu` devrait connaître le
type de charge du moteur, et la couche remonterait d'un cran. C'est l'interdit
symétrique de la passivité du moteur, et les deux se lisent sur le même tour de
boucle du diagramme de [`architecture.md`](architecture.md).

### 5.2 Ce que `lire` garantit

- **M1** — les enregistrements sortent dans l'ordre des décalages croissants.
- **M3** — `lire` ne rend **que** des enregistrements durables. Un enregistrement
  écrit et non encore validé n'est pas lisible, et ce n'est pas un filtre de
  commodité : sauter les non-durables au lieu de s'arrêter au premier casserait
  M1 côté lecture. Le code emploie donc un `take_while`, pas un `filter`.
- **EX-A12** — `lire_multi` applique son budget **total**, pas par partition.
  L'ordre des curseurs est mélangé par Fisher-Yates tiré de l'unique `Alea`
  (M2 : aucun ordre entre partitions n'est promis, et le mélange fait payer
  l'agent qui en supposerait un).

### 5.3 La réplication, et la perte muette

```rust
// sim-milieu/src/replication.rs
pub const REGLAGE_LAG: &str = "replica.lag.time.max.ms";
impl Isr {
    pub fn nouvelle(k: u32, m: u32, temporisateur: Duree) -> Isr;
    pub fn ecrire(&mut self) -> Result<u64, Refus>;
    pub fn tolerances(&self) -> (Option<u32>, u32);
    pub fn marge_daccuse(&self) -> i64;
    pub fn affichage_v15(&self) -> Vec<(&'static str, String)>;
    pub fn perte_muette(&self) -> Option<String>;
    pub fn declarer_hypotheses(&self, registre: &mut RegistreHypotheses);
}
```

Trois clauses de contrat :

- `ecrire` rend `Err(Refus::SousLeSeuil)` quand la taille de l'ISR tombe sous
  `m`. **C'est le seul signal que le producteur reçoive** — à `m = 1` il n'y a
  plus de seuil à franchir, donc plus aucun refus, et la tolérance passe de `f` à
  0 sans qu'aucune erreur ne soit émise. `perte_muette()` est ce qui rend le
  phénomène affichable ; c'est le seul endroit du produit où l'affichage vaut
  mieux que le protocole.
- `tolerances()` rend **deux** grandeurs de provenance différente : `w − 1` pour
  un enregistrement accusé à largeur `w` (§2.1 du traité), et `|ISR| − 1` pour R1
  (§6.1 du traité). Elles ne s'additionnent pas. `marge_daccuse()` en rend une
  troisième,
  `|ISR| − m`, **dérivée du produit** — le traité ne l'écrit pas, et l'affichage
  l'étiquette comme telle.
- `declarer_hypotheses` inscrit `replica.lag.time.max.ms` au registre EX-C12 avec
  l'affirmation qu'il encode — *un suiveur sain rattrape le meneur en moins du
  temporisateur* — et le compteur des fois où elle a été fausse. Les 30 s sont la
  **valeur par défaut** d'EX-M14, non le texte du registre.

**Une asymétrie assumée, et une exception qu'il faut dire** : le temporisateur ne
décide que du **retrait**, et aucune réplique retirée pour retard ne revient.
`|ISR|` est donc monotone décroissante **hors élection hors ISR** — mais `elire`
en régime hors ISR réaffecte `self.isr = vec![meneur]`, ce qui la fait remonter de
0 à 1. Ce n'est pas un cas de laboratoire : c'est la trajectoire du scénario D,
`Etape::T3` puis `T4` vidant l'ISR avant `Choix::ElireHorsIsr`, à l'instant même
où R1 tombe. `sim_milieu::hors_perimetre()` le déclare ainsi.

### 5.4 Le groupe et le plan de contrôle

`Groupe` porte les trois protocoles de rééquilibrage (`Protocole`), le
parallélisme utile `min(n, p)`, et les quatre lignes de coût d'un changement de
population (`CoutChangement`). `Protocole::messages(n)`, `phases()`, `tours()` et
`pose_une_barriere()` sont les quatre grandeurs comptées séparément — le compte de
**phases** n'entre jamais dans la même colonne que le compte de **tours**
(annexe B.1 du PRD).

`PlanDeControle` est un **modèle de coût**, jamais un protocole (DT7). Sa
constante `LIBELLE` est littéralement *« modèle de coût du plan de contrôle — pas
un protocole d'accord »*, et `violations_de_la_condition()` rend les ruptures de
`broadcastTime ≪ electionTimeout ≪ MTBF`. Ses compteurs ne sont jamais additionnés
à ceux du plan de données.

---

## 6. Le contrat de l'essaim

```rust
// sim-agents/src/essaim.rs
pub enum Perception {
    Voisinage { cardinal_max: u32 },
    IntervalleMilieu { enregistrements_max: u32 },
}
pub struct Membre { pub perception: Perception }
pub const REFUS: &str = "ce n'est pas un membre de l'essaim, c'est un coordonnateur";
```

`Membre::nouveau` **rejette à la construction** une perception non factorisée,
avec le message `REFUS`. C'est EX-A12 tenu par le constructeur, pas par la revue.

**Ce que le constructeur vérifie, et la frontière exacte** : il refuse
`cardinal_max >= population`, et un test nommé le fixe
(`un_voisinage_qui_couvre_la_population_est_refuse`). Un `cardinal_max` **égal à
`n` est donc refusé**.

**Ce qu'il ne peut pas vérifier, et qui se tient à la lecture** : un
`cardinal_max` réglé à `population − 1` passe, et une borne qui suit `n` d'un cran
n'est pas une borne indépendante de `n`. La doc du champ le dit ; aucun code ne le
rattrape.

Le plafond de `IntervalleMilieu` est **total**, non par partition — c'est la même
clause que `lire_multi`, vue du côté de l'agent.

---

## 7. Le contrat des mécanismes

Trente et un modules dans `sim-agents`. **« Un par mécanisme du traité » est une
approximation**, et quatre modules la démentent : `glossaire` est une donnée,
`partage` implante un lien d'URL (EX-V09, EX-V12) auquel aucune section du traité
ne correspond, et `scenario` et `scenario_d` sont des jeux de données de scénario.
`conformite`, `dettes` et `scenario_m` nomment bien une section — le §8.1 du
traité — et ne sont donc pas des exceptions.
Le contrat commun, tenu par convention de module et vérifié par la présence des
tests :

1. **Le module ouvre sur un `//!`** qui dit quelle section du traité il implante
   et quelle règle il tient, souvent avec la citation en bloc.
2. **La signature complète est publique** : modèle de panne, hypothèse de
   synchronisme, hypothèses sur le milieu, condition d'arrêt, modes de
   défaillance. Plusieurs modules l'exposent comme une constante — par exemple
   `alignement::SIGNATURE: &[(&str, &str)]` et
   `consensus_lineaire::SIGNATURE`.
3. **Les modes de défaillance sont des variantes d'énumération**, donc
   provocables, jamais des commentaires : `agregation::Ligne`,
   `consensus_lineaire::Mode`, `cascade::Etape`, `cycle_de_vie::OrdreDeChute`,
   `soupcon::PolitiqueExpiration`, `stigmergie::MomentTrace`.
4. **Les refus sont des constantes ou des `Result`**, pas des `panic!` :
   `essaim::REFUS`, `soupcon::REFUS_TROISIEME_VOIE`,
   `agregation::PolitiqueStochastique::REFUS_DARRET`,
   `consensus_lineaire::Iteration::REFUS_PROGRESSION`,
   `allocation::verifier_usage_champ_moyen(..) -> Result<(), String>`. Les deux
   constructeurs qui abandonnaient sur un réglage de bord **et qui rendaient déjà
   un `Result`** — `p = 0` du scénario B, `k = 0` du seuil de quorum — refusent
   désormais ; `Rumeur::nouvelle`, qui n'en rend pas, **écrête** à `n.max(1)` et le
   dit dans son `///`. Un test par module le fixe.
5. **Une constante numérique porte sa provenance** dans un champ ou une constante
   voisine — `agreger_epidemique::SOURCE` dans `sim-agents`, et
   `elasticite::Params::FENETRE_STABILISATION`, qui déclare l'**absence** de
   provenance du défaut : F1 appliqué à un trou. Les crates voisines tiennent la
   même clause (`sim_milieu::format::SOURCE`, `sim_core::service::SOURCE`).
6. **Les tests unitaires vivent dans le module**, en `#[cfg(test)] mod tests`,
   nommés en phrase française.

**Une politique sans condition d'arrêt n'en reçoit pas une.**
`agregation::REFUS_DARRET` est le libellé affiché à la place :
*« aucune condition d'arrêt locale, pas même heuristique »* (EX-A38). De même,
`consensus_lineaire::REFUS_PROGRESSION` refuse la barre de progression, sauf sur
digraphe équilibré fortement connexe, où la minoration existe.

---

## 8. Le contrat des scénarios comme données

```rust
// sim-agents/src/scenario.rs
pub struct Bloc {
    pub en_clair: &'static str,          // reformulation du produit — jamais citée
    pub these: &'static str,             // une phrase, citée du traité
    pub source: &'static str,            // section ET page (F2)
    pub mecanisme_visible: &'static str,  // quel réglage, quel effet, par quel chemin
    pub ne_demontre_pas: &'static str,    // la négation, au même rang que la thèse
}
```

C'est PD8 tenu par une structure : un scénario sans ces cinq champs ne se
construit pas. Le champ `en_clair` est le seul écrit par le produit, et
l'interface le désigne comme une reformulation — une paraphrase présentée au rang
d'une citation serait la confusion de provenance qu'EX-V11 refuse.

**Les dix blocs livrés** : `BLOC_A`, `BLOC_B` (`scenario.rs`), `BLOC_D`
(`scenario_d.rs`), `BLOC_E` (`adhesion.rs`), `BLOC_F` (`allocation.rs`),
`BLOC_G` (`agregat_fenetre.rs`), `BLOC_J` (`cascade.rs`), `BLOC_K`
(`gouvernance.rs`), `BLOC_L` (`taux_de_base.rs`), `BLOC_M` (`scenario_m.rs`).
**Les scénarios C, H et I n'ont pas de bloc**, et `sim_agents::hors_perimetre()`
le déclare.

Les dix portent une `source` avec **section et page**, ce
que fixe `les_dix_blocs_portent_leur_section_et_leur_page`. **De quelle édition,
le code ne le dit qu'en partie, et il n'en dit pas la même chose partout.**
Mesuré le 17 août 2026 à 08 h 32 par

```bash
grep -rhoE '§[0-9]+(\.[0-9]+)?, p\. [0-9]+' crates/ | sort | uniq -c | sort -rn
```

les 43 renvois `§X.Y, p. N` des quatre crates donnent **quatre** pages
différentes pour le seul §1.2 — `p. 16` dix fois, `p. 13` quatre fois, `p. 14`
deux fois, `p. 12` une fois. **L'édition de référence est tranchée depuis le
17 août 2026** — c'est la **troisième**, 143 pages, la seule que le dépôt
contienne, et F2 comme DT5 portent la clause. Ce que le constat ci-dessus établit
n'est donc plus une ambiguïté d'édition mais une **migration inachevée** : le
`Traité.pdf` du dépôt ouvre le §1.2 à la page 12 avec l'énoncé des bornes à la
page 16, `p. 13` ne correspond à ni l'un ni l'autre, et le compte ci-dessus a
bougé d'une heure à l'autre pendant la campagne. Le code n'en tient pas une seule,
ce que F2 qualifie de provenance fausse et non d'imprécision, et seuls les renvois
portant `(3ᵉ éd.)` se relisent sans refaire la vérification. **Huit d'entre eux — D, E,
F, G, J, K, L, M — n'ont aucun point d'affichage** : `sim-viz` ne lit que `BLOC_A`
et `BLOC_B`, et le réexport de `BLOC_D` et `BLOC_M` par `lib.rs` n'en est pas un.
La liste d'absences le dit, et l'onglet « Limites » affiche le même compte.

Les points d'entrée exécutables sont des fonctions pures de leurs paramètres et
de leur graine :

```rust
pub fn scenario_a(/* … */) -> Comparaison;
pub fn scenario_b(params: Params, graine: u64, budget_evenements: u64)
    -> Result<ResultatB, String>;
pub fn scenario_l(/* … */);
```

`Result` plutôt que `panic!` : une configuration invalide est un refus rendu à
l'appelant, jamais un abandon (EX-C11, EX-A52, EX-A53).

---

## 9. Le contrat de l'interface

`sim-viz` est la seule crate qui dessine, et son contrat est presque entièrement
négatif :

| Elle contient | Elle ne contient pas |
|---|---|
| `Application`, les deux points d'entrée `lancer_natif` et `lancer_web`, l'échelle typographique `poser_le_style` posée à l'identique sur les deux cibles | **Zéro** logique de simulation, à **une** exception nommée : `scenario_b.rs::situe_la_tranche` réimplante l'hypothèse que le budget d'événements est découpé en tranches de largeur égale — c'est ce que fait `Fourragement::traiter`, mais `sim-agents` ne rend pas la tranche de bascule, et le jour où le découpage cesserait d'être uniforme l'étiquette « avant / après la bascule » mentirait sans erreur de compilation. Déclarée dans son rustdoc **et** dans l'onglet « Limites » depuis l'audit du 17 août 2026 |
| `scenario_a.rs`, `scenario_b.rs` — les deux vues livrées | **Zéro** définition de scénario, à **deux** exceptions nommées : les critères d'acceptation viennent tous de `sim-agents`, mais **les valeurs d'ouverture des deux vues sont écrites ici** — six dans `VueA::default` (n, p, ℓ₉₉, aller simple, degré de dépôt, taux d'omission) et trois dans `VueB::default` (n, budget, graine). Ce sont les défauts des tableaux du §7 du PRD, transcrits faute d'accesseur : `sim_agents::scenario_a` est une fonction à sept paramètres sans constructeur de défaut, et `Params::scenario_b()` pose n = 64 là où la vue ouvre à 16 (Θ(n²)). Rien ne tient ces transcriptions en accord avec le PRD. **Les plages de curseur, elles aussi, sont écrites ici** — quinze littéraux dans les deux vues, dont quatre qu'aucun tableau du §7 du PRD ne fixe. Les neuf valeurs d'ouverture sont déclarées dans l'onglet « Limites » depuis l'audit du 17 août 2026 |
| Les onglets « Limites » et « Repères » | **Zéro** texte du traité, à **une** exception nommée : le glossaire vient de `sim_agents::glossaire`, les reformulations de `Bloc::en_clair`, trois des **six** listes de l'onglet venant des `hors_perimetre()` — mais la provenance des deux bornes est recopiée dans `scenario_b.rs::SOURCE_BORNES`, faute d'accesseur dans `sim-agents`. La copie a déjà divergé de `Bornes::LEGENDE`, affichée quatre lignes plus bas dans le même cadre ; depuis l'audit du 17 août 2026 le test `la_provenance_des_bornes_suit_encore_sim_agents` échoue à la place de l'écran |
| Trois rangs de cadre — `cadre` découpe une section numérotée, `encart` accompagne sans découper, `bloc_pd8` pose le sien | Ni export CSV, ni parcours « le fil » : **O6 n'est pas livré** |

`main.rs` fait seize lignes, dont **six de code** : deux `fn main` gardés par
`#[cfg]`, l'un pour la cible native, l'autre vide pour `wasm32`. Aucune logique.
**Les deux cibles traversent le même code** : c'est la condition d'EX-V12, dont
la parité de sortie est mesurée par
[`bancs/parite-wasm`](../bancs/parite-wasm/VERDICT.md) — six cas du scénario B,
empreintes identiques, bits des flottants compris.

---

## 10. Le contrat de nomenclature

Quatre paires de grandeurs se ressemblent et ne se mêlent jamais. Les confondre
est un défaut bloquant, pas une imprécision.

| Grandeur | Statut | Où | Ne pas confondre avec |
|---|---|---|---|
| **ℓ₉₉ du milieu** | **Entrée** — paramètre tiré d'une distribution | `sim-milieu::latence::Latence::depuis_l99` | **ℓ₉₉ de réponse d'un agent** — **sortie**, produite par la file et le temps de service : `sim-core::service::Service::l99_de_reponse`, dont la constante `LIBELLE_L99` porte l'avertissement |
| **ρ** | **Dérivé** de la structure des domaines de panne | `sim-core::horloge::Domaines::rho()` | **Φ_c** — corrèle les *décisions*, pas les *pannes*. Livré : `sim-agents::conformite::estimer` (EX-A56), dérivé de `sim-core::famille::Familles` (EX-C19). Ce qu'il mesure réellement est au §13 |
| **Tour** | Trois conventions coexistantes | Glossaire §12 C du PRD, annexe B.1 | **Aller-retour** : sous la convention de référence, il vaut deux tours. `Protocole::tours()` et `phases()` sont deux colonnes |
| **Largeur d'accusé `w`** | Du traité (§2.1) | `Isr::derniere_largeur()` | **Marge d'accusé \|ISR\| − m** : `Isr::marge_daccuse()`, **grandeur dérivée du produit**, étiquetée comme telle |

Règle générale : toute grandeur qui ne vient pas du traité porte l'étiquette
« dérivée du produit » ou « simulé » à l'endroit où elle s'affiche (F2). Le code
la porte dans une constante voisine, jamais dans un commentaire.

---

## 11. Ce que le contrat ne couvre pas

Trois fonctions du code sont la liste vivante des absences, et elles sont un
**livrable**, pas un commentaire (PD6) :

| Fonction | Ce qu'elle énumère |
|---|---|
| `sim_agents::hors_perimetre()` | **20 entrées** — dont le tableau 15 rendu par citation, le débit « émergent » du scénario C qui inverse la formule qui a produit ses points, trois des **sept** colonnes du tableau 14, six mécanismes des phases 1 à 5 sans appelant, **six** oracles du catalogue jamais armés, et les deux mécanismes du ch. 8 qu'aucun scénario n'exécute — `awk '/pub fn hors_perimetre/,/^}/' crates/sim-agents/src/lib.rs \| grep -cE '^\s*"'`, 17 août 2026 |
| `sim_milieu::hors_perimetre()` | **13 entrées** — dont l'absence d'arbitrage d'époque, la monotonie de \|ISR\| **hors élection hors ISR**, l'historique par identité (EX-M25) et le quota par ressource (EX-M26) que nul scénario n'instancie, les prédicats d'oracle jamais évalués, la fonction de clé du milieu sans appelant, et le fait que rétention, compactage, groupe et plan de contrôle sont **implantés, testés, et appelés par aucun scénario** — même ligne sur `crates/sim-milieu/src/lib.rs`, 17 août 2026 |
| `ModeleFaute::hors_modele()` | **5 entrées** — dont la première, aucun scénario ne règle `Config.fautes`, et la cinquième, l'adversité endogène du §8.3 du traité (EX-C20). La première **énumère à elle seule neuf mécanismes sans appelant**, dont six sans rapport avec le modèle de faute pris comme modèle : c'est la conséquence de l'absence de `sim_core::hors_perimetre()`, décision ouverte au [registre](decisions.md) |

**La distinction qui gouverne ces listes n'est pas « écrit / pas écrit » mais
« branché / pas branché ».** Un module que personne n'appelle a exactement le
même effet sur un résultat qu'un module qui n'existe pas. Une entrée ne se retire
d'ici que parce que le mécanisme est **branché**, jamais parce qu'il est écrit
quelque part.

Les réserves du §0 du PRD reprennent ces listes avec leur conséquence sur les
critères de sortie ; ce document ne les recopie pas.

---

## 12. Comment vérifier ce contrat

| Ce qu'on vérifie | Commande |
|---|---|
| Le contrat entier — **465 tests** au 17 août 2026, 09 h 49 ; le compte se remesure, il ne se cite pas | `cargo test --workspace --release` |
| Le critère de sortie de la phase 6 | `cargo test -p sim-agents --release --test sortie_phase_6` |
| Le constat de mesure sur Φ_c | `cargo run -p sim-agents --example diagnostic_conformite --release` |
| Les interdictions structurelles — **sortie 101 si l'une tombe** | `cargo clippy --workspace --all-targets --release` |
| La parité flottante natif/WASM (NF-02) | Banc DT1 — voir [`DEVELOPPEMENT.md`](DEVELOPPEMENT.md) |
| La parité de sortie d'un mécanisme complet (EX-V12) | Banc `parite-wasm` — idem |
| La documentation d'interface — **sortie 101 sur un renvoi cassé** | `cargo doc --workspace --no-deps` — les quatre crates déclarent `#![deny(missing_docs)]` et `#![deny(rustdoc::broken_intra_doc_links)]` |

**Les critères de sortie de phase sont des tests d'intégration**, et ce sont eux
qui tiennent le contrat au niveau du système :

| Fichier | Tests | Ce qu'il prouve |
|---|---|---|
| `crates/sim-agents/tests/determinisme.rs` | 4 | NF-01 et NF-04 : 100 graines, deux exécutions chacune, traces égales ; 100 graines distinctes, 100 traces distinctes |
| `crates/sim-agents/tests/scenario_b.rs` | 11 | Le critère de sortie de la phase 1 |
| `crates/sim-agents/tests/sortie_phase_2.rs` | 5 | |
| `crates/sim-agents/tests/sortie_phase_3.rs` | 4 | |
| `crates/sim-agents/tests/sortie_phase_4.rs` | 5 | |
| `crates/sim-agents/tests/sortie_phase_5.rs` | 3 | |
| `crates/sim-agents/tests/sortie_phase_6.rs` | 11 | Le second axe — dont le point 1 **reformulé sur la mesure**, le §9 du PRD ayant annoncé un résultat que la mesure réfute |

Il n'y a pas de `sortie_phase_1.rs` : les critères de la phase 1 sont dans
`determinisme.rs` et `scenario_b.rs`. **Ne pas affaiblir ces tests** — ce sont les
preuves du tableau du §0. Les 43 tests d'intégration se complètent de **422** tests
unitaires (253 `sim-agents`, 96 `sim-core`, 68 `sim-milieu`, 5 `sim-viz`), soit
**465** au 17 août 2026 à 09 h 49. **C'est la répartition, non le total, qui dit
où le filet est lâche** : 43 tests d'intégration pour 422 unitaires, et cinq
seulement sur toute l'interface.

**Les trois commandes à passer avant de committer**, et non deux : `cargo test`,
`cargo clippy` et `cargo doc`. La troisième manquait à la procédure, et c'est
elle qui a laissé passer les deux renvois rustdoc cassés que l'audit a trouvés —
la procédure était structurellement incapable de voir le seul défaut mécanique
que le dépôt portait en cours.

**Il n'y a pas d'intégration continue.** NF-13 et NF-16 nomment un mécanisme
d'application que le dépôt ne contient pas : ce que ces exigences obtiennent vient
de `cargo test --workspace` lancé à la main.

---

## 13. Ce que la phase 6 a ajouté au contrat

La phase 6 est **livrée**. Quatre clauses de ce document ont changé, une
cinquième a été ajoutée par la mesure plutôt que par la spécification, et une
sixième par l'audit du dépôt.

| Clause d'avant | Ce qu'elle est devenue |
|---|---|
| L'aléa de décision vient du `Alea` unique, un tirage par agent | `famille::TirageDeDecision` : deux agents d'une même famille consomment le **même** tirage pour une même décision **au même tour de leur boucle**. Le déterminisme tient — le tirage partagé descend du même générateur semé, et le rejeu est vérifié par `le_partage_de_tirage_ne_casse_pas_le_rejeu` |
| `Enregistrement` n'avait pas d'auteur | `Enregistrement::auteur: Identite`, **apposé par le milieu** à la réception. `Milieu::ecrire` prend l'identité en paramètre ; la charge utile est un `f64`, donc il n'y a structurellement aucune place pour un auteur déclaré. `Milieu::sessions_partagees()` **constate** la condition d'échec sans pouvoir l'empêcher |
| `ModeleFaute::hors_modele()` avait 4 entrées | Cinq : l'adversité endogène du §8.3 **du traité**, avec la distinction explicite d'avec DT8 — l'agent menteur est *injecté*, ce régime-ci est *produit* |
| Trois hypothèses nommées conditionnaient les bornes | Six. `Params::bornes_applicables` rend une `Err` portant son motif sur γ, sur le couple φ, sur le couple η, sur `m = 0`, sur un exposant négatif, et dès que la part de conformité est non nulle : la borne est **absente**, pas grisée. L'audit a trouvé que seul le couple φ était gardé, de sorte que le portail rendait `Ok` sur des planchers de probabilité valant `NaN`, `inf` ou `−0,00125` |
| *(clause nouvelle)* | **L'effacement d'une borne suit le réglage, jamais la mesure.** `dettes::verdicts` prend une `&Familles`, non une `&Conformite` |
| *(clause nouvelle, relevée par l'audit)* | **Effacer une borne n'efface pas une mesure.** `Fourragement::verifier_bornes` relève `plancher_observe` et `hors_dominante_observee` **avant** de consulter le portail, et non à l'intérieur de la branche qui s'arrête quand la borne est effacée. L'ordre inverse faisait disparaître la mesure au moment précis où elle devenait la seule chose à regarder |
| *(clause nouvelle, relevée par l'audit du 17 août 2026)* | **`Politique::PrixCroissant` facture le k-ième preneur distinct `1 + pente × (k − 1)`, le soumissionnaire compris.** Le **deuxième** preneur distinct paie donc déjà la pente. Le code facturait sur l'état *d'avant* la soumission, de sorte que le deuxième payait encore le prix nominal et que le prix ne croissait pas « avec le nombre de preneurs » (§8.1) : la documentation du champ avait raison contre le code, et c'est le code qui a été corrigé. Le PRD ne chiffre pas cette grandeur — il exige « prix croissant avec le nombre de preneurs » (EX-M26) —, donc la formule est ici et nulle part ailleurs, tenue par `le_prix_monte_des_le_deuxieme_preneur` : à pente 1 et quatre preneurs distincts, le prix cumulé vaut **10**, non 7 |

**Pourquoi la clause nouvelle, et c'est le résultat le plus important de la
phase.** Le premier point du critère de sortie annonçait un Φ_c passant de ≈ 0 à
≈ 1 sous le curseur de familles. Mesuré, Φ_c vaut **déjà ≈ 0,17 à curseur au
repos** — les agents lisent tous la même trace, donc leurs décisions sont
corrélées — et le curseur ne le déplace que de ≈ 0,055, de 0,173 à 0,228, non
monotonement : dix-huit fois sa précision, un dix-huitième de l'amplitude
annoncée. Φ_c
mesure donc la **somme** de la corrélation due à la fonction de décision et de
celle due au milieu partagé, sans les séparer.

Effacer une borne sur cette base aurait affirmé que l'indépendance des **tirages**
est violée alors que ce qui est mesuré est la **coordination** : une fausse alarme,
que la discipline de PD12 interdit. NF-14 parle d'un *réglage* qui viole une
hypothèse, et le réglage — la structure des familles — est connu. Φ_c reste
affiché comme une mesure, à côté et jamais à la place.

Le constat est dans `sim_agents::conformite::CONSTAT_DE_MESURE`, se reproduit par
`cargo run -p sim-agents --example diagnostic_conformite --release`, et le §0.1 du
PRD le consigne comme cinquième écart au sens de NF-15.

**Ce que la phase établit** est plus fort et moins spectaculaire que ce qu'elle
annonçait : l'hypothèse d'indépendance des sept énoncés du tableau 21 était déjà
portée sans être dite par le code des phases 1 à 5, et rien avant EX-A58 ne le
signalait.
