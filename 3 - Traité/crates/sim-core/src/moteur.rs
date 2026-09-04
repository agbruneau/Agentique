//! La boucle à événements discrets (EX-C01), et ce qui la rend rejouable.
//!
//! Le moteur est **passif** : il rend l'événement de date minimale, avance
//! l'horloge, et laisse l'appelant exécuter le gestionnaire puis réinjecter ce
//! qu'il produit. Ce choix évite un trait « gestionnaire » à une seule
//! implantation (PD7) et garde `sim-core` ignorant des agents comme du journal
//! partitionné (§5.1 du PRD).
//!
//! Il n'y a pas d'attente réelle : l'horloge saute à la date de l'événement
//! suivant. Aucun appel à l'horloge du système n'existe dans ce fichier — c'est
//! la lettre de PD1.

use crate::alea::Alea;
use crate::couverture::Couverture;
use crate::faute::ModeleFaute;
use crate::oracle::Registre;
use crate::temps::{Duree, Granularite, Instant};
use crate::ActeurId;
use std::cmp::Ordering;
use std::collections::BinaryHeap;

/// Un événement daté en temps logique.
///
/// `seq` est le compteur monotone d'EX-C03 : il départage les égalités de date.
/// Sans lui, l'ordre de deux événements simultanés dépendrait de l'ordre
/// d'insertion dans le tas, qui n'est pas spécifié.
#[derive(Clone, Copy, Debug)]
pub struct Evenement<C> {
    /// Date d'échéance, en temps **logique**. Jamais un temps mural.
    pub date: Instant,
    /// Rang d'insertion. Départage deux événements de même date, et c'est ce
    /// qui rend l'ordre total et reproductible.
    pub seq: u64,
    /// Acteur à qui l'événement est destiné.
    pub cible: ActeurId,
    /// Charge utile, dont le moteur ne connaît rien : il ne l'inspecte pas et
    /// ne l'ordonne pas.
    pub charge: C,
}

// Ordre implanté à la main, et non dérivé : `C` n'a pas à être ordonnable, et
// seuls (date, seq) décident. L'ordre est inversé parce que `BinaryHeap` est un
// tas max et que la boucle veut la date **minimale**.
impl<C> Ord for Evenement<C> {
    fn cmp(&self, autre: &Self) -> Ordering {
        autre
            .date
            .cmp(&self.date)
            .then_with(|| autre.seq.cmp(&self.seq))
    }
}
impl<C> PartialOrd for Evenement<C> {
    fn partial_cmp(&self, autre: &Self) -> Option<Ordering> {
        Some(self.cmp(autre))
    }
}
impl<C> PartialEq for Evenement<C> {
    fn eq(&self, autre: &Self) -> bool {
        self.date == autre.date && self.seq == autre.seq
    }
}
impl<C> Eq for Evenement<C> {}

/// Pourquoi une exécution s'est arrêtée. Aucune de ces raisons n'est
/// « terminée » : le §3.3 ne fournit aucun critère de complétude (EX-C10b).
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Arret {
    /// Plus aucun événement en attente.
    FileVide,
    /// Budget d'événements épuisé.
    BudgetEvenements,
    /// Budget de temps de calcul épuisé, rapporté par l'appelant.
    BudgetTemps,
    /// Violation d'oracle : l'exécution s'arrête à l'instant de la violation
    /// (EX-C09, §3.3 étape 5).
    Violation(&'static str),
    /// Arrêt demandé de l'extérieur.
    Demande,
}

/// Budget d'une exécution (EX-C10a).
///
/// Le budget en secondes-cœur ne peut pas être mesuré ici : lire l'horloge du
/// système dans le cœur violerait PD1 et rendrait l'exécution non rejouable.
/// L'appelant — binaire de campagne ou interface — mesure et appelle
/// `consommer_temps`. Le budget en événements, lui, est déterministe et suffit
/// à borner une exécution isolée.
#[derive(Clone, Debug)]
pub struct Budget {
    /// Nombre d'événements au-delà duquel l'exécution s'arrête. Déterministe,
    /// donc reproductible.
    pub evenements_max: u64,
    /// Plafond de temps de calcul, en secondes-cœur. `None` signifie « aucun
    /// plafond » : il n'est pas mesuré ici, mais rapporté par l'appelant via
    /// [`Budget::consommer_temps`].
    pub secondes_coeur_max: Option<f64>,
    secondes_consommees: f64,
    arret_demande: bool,
}

impl Budget {
    /// Budget borné par le seul nombre d'événements.
    pub fn evenements(evenements_max: u64) -> Budget {
        Budget {
            evenements_max,
            secondes_coeur_max: None,
            secondes_consommees: 0.0,
            arret_demande: false,
        }
    }

    /// Ajoute un plafond de temps de calcul, en secondes-cœur.
    pub fn avec_secondes_coeur(mut self, s: f64) -> Budget {
        self.secondes_coeur_max = Some(s);
        self
    }

    /// Rapporte du temps de calcul consommé, mesuré **hors du monde clos**.
    pub fn consommer_temps(&mut self, secondes: f64) {
        self.secondes_consommees += secondes;
    }

    /// Demande l'arrêt à la prochaine extraction d'événement. L'arrêt est
    /// rapporté comme [`Arret::Demande`], et non comme une fin de file.
    pub fn demander_arret(&mut self) {
        self.arret_demande = true;
    }

    /// Temps de calcul rapporté jusqu'ici, en secondes-cœur.
    pub fn secondes_consommees(&self) -> f64 {
        self.secondes_consommees
    }
}

/// Hachage cumulatif de la trace (EX-C02, NF-01, NF-04).
///
/// Deux exécutions de même graine et même configuration doivent produire la
/// même suite de (date, seq, cible) — c'est l'entrelacement. L'appelant peut
/// ajouter ses propres marques pour couvrir aussi les valeurs calculées.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct Trace(u64);

impl Trace {
    const DEPART: u64 = 0xcbf2_9ce4_8422_2325;
    const PREMIER: u64 = 0x0000_0100_0000_01b3;

    /// Trace vide, avant tout événement.
    pub fn nouvelle() -> Trace {
        Trace(Trace::DEPART)
    }

    /// Absorbe une valeur dans le hachage. L'ordre des appels compte : deux
    /// exécutions qui absorbent les mêmes valeurs dans un ordre différent
    /// donnent des traces différentes, et c'est le comportement voulu.
    pub fn absorber(&mut self, x: u64) {
        for i in 0..8 {
            self.0 ^= (x >> (i * 8)) & 0xff;
            self.0 = self.0.wrapping_mul(Trace::PREMIER);
        }
    }

    /// Le hachage courant, tel qu'il s'écrit dans un export (NF-01, NF-04).
    pub fn valeur(self) -> u64 {
        self.0
    }
}

/// Le moteur.
pub struct Moteur<C> {
    file: BinaryHeap<Evenement<C>>,
    horloge: Instant,
    sequence: u64,
    evenements_consommes: u64,

    /// Unité du temps logique, réglée par scénario (DT10, EX-C04). Deux
    /// exécutions de granularités différentes ne se comparent pas.
    pub granularite: Granularite,
    /// La source d'aléa **unique** du monde clos (PD1).
    pub alea: Alea,
    /// Modèle de faute actif, affiché et versionné (PD6).
    pub fautes: ModeleFaute,
    /// Oracles armés. Une violation arrête l'exécution à son instant (EX-C09).
    pub oracles: Registre,
    /// Compteur de conditions atteintes (EX-C08, NF-13).
    pub couverture: Couverture,
    /// Ce qui borne l'exécution (EX-C10a).
    pub budget: Budget,
    /// EX-C12 — les hypothèses plus fortes que « Δ finie mais inconnue »,
    /// nommées là où elles sont prises, avec le compteur de leurs démentis.
    pub hypotheses: crate::registre::RegistreHypotheses,

    trace: Trace,
    arret: Option<Arret>,
}

impl<C> Moteur<C> {
    /// Moteur neuf : file vide, horloge à zéro, générateur semé par `graine`.
    ///
    /// La graine et la granularité font partie de l'identité de l'exécution :
    /// avec la configuration, elles suffisent au rejeu à l'identique (§3.3).
    pub fn nouveau(graine: u64, granularite: Granularite, budget: Budget) -> Moteur<C> {
        Moteur {
            file: BinaryHeap::new(),
            horloge: Instant(0),
            sequence: 0,
            evenements_consommes: 0,
            granularite,
            alea: Alea::nouveau(graine),
            fautes: ModeleFaute::default(),
            oracles: Registre::nouveau(),
            couverture: Couverture::nouvelle(),
            budget,
            hypotheses: crate::registre::RegistreHypotheses::nouveau(),
            trace: Trace::nouvelle(),
            arret: None,
        }
    }

    /// L'instant logique courant. Il ne recule jamais.
    pub fn maintenant(&self) -> Instant {
        self.horloge
    }

    /// Le hachage de l'entrelacement produit jusqu'ici.
    pub fn trace(&self) -> Trace {
        self.trace
    }

    /// Nombre d'événements extraits, à comparer à `budget.evenements_max`.
    pub fn evenements_consommes(&self) -> u64 {
        self.evenements_consommes
    }

    /// Nombre d'événements planifiés et non encore extraits.
    pub fn en_attente(&self) -> usize {
        self.file.len()
    }

    /// Raison de l'arrêt, si l'exécution s'est arrêtée.
    pub fn arret(&self) -> Option<&Arret> {
        self.arret.as_ref()
    }

    /// Planifie un événement dans `delai` à partir de maintenant.
    ///
    /// La gigue de date du modèle de faute s'applique ici (EX-C05, dernière
    /// entrée de la liste du §3.3) : elle ne peut qu'ajouter du retard, un
    /// événement ne remontant jamais le temps logique.
    pub fn pousser(&mut self, delai: Duree, cible: ActeurId, charge: C) {
        let gigue = self.fautes.gigue(&mut self.alea);
        let date = self.horloge + delai + gigue;
        self.pousser_a(date, cible, charge);
    }

    /// Planifie un événement à une date absolue. Une date passée est ramenée à
    /// l'instant courant : le temps logique ne recule pas.
    pub fn pousser_a(&mut self, date: Instant, cible: ActeurId, charge: C) {
        let date = date.max(self.horloge);
        self.sequence += 1;
        self.file.push(Evenement {
            date,
            seq: self.sequence,
            cible,
            charge,
        });
    }

    /// Ajoute une marque à la trace — pour couvrir les valeurs calculées, que
    /// le moteur ne connaît pas.
    pub fn marquer(&mut self, x: u64) {
        self.trace.absorber(x);
    }

    /// Extrait l'événement de date minimale et avance l'horloge à cette date
    /// (EX-C01). Rend `None` quand l'exécution s'arrête, et `arret()` dit
    /// pourquoi.
    pub fn suivant(&mut self) -> Option<Evenement<C>> {
        if self.arret.is_some() {
            return None;
        }
        // EX-C09 — première moitié : une sûreté violée par le gestionnaire du
        // tour précédent arrête ici, **avant** d'extraire quoi que ce soit.
        //
        // Et avant **les trois** motifs d'arrêt, non pas le seul budget
        // d'événements : une violation déjà enregistrée a eu lieu au tour
        // précédent, donc avant l'épuisement du budget de temps comme avant la
        // demande d'arrêt, qui sont tous deux rapportés de l'extérieur et donc
        // postérieurs. Les motifs sont vrais ensemble ; un seul est un défaut,
        // et c'est celui-là qu'il faut rapporter. Placé après l'un d'eux, le
        // contrôle enterrait une violation au registre sous une raison
        // administrative — mesuré : `Some(BudgetTemps)` et `Some(Demande)` avec
        // une violation enregistrée.
        if self.arreter_sur_violation() {
            return None;
        }
        if self.budget.arret_demande {
            self.arret = Some(Arret::Demande);
            return None;
        }
        if let Some(max) = self.budget.secondes_coeur_max {
            if self.budget.secondes_consommees >= max {
                self.arret = Some(Arret::BudgetTemps);
                return None;
            }
        }

        if self.evenements_consommes >= self.budget.evenements_max {
            self.arret = Some(Arret::BudgetEvenements);
            return None;
        }

        let date = match self.file.peek() {
            Some(ev) => ev.date,
            None => {
                self.arret = Some(Arret::FileVide);
                return None;
            }
        };

        // EX-C09 — seconde moitié : les vivacités bornées échoient à l'horloge,
        // jamais à l'événement, sinon une échéance enjambée par un saut de temps
        // ne se verrait pas. L'échéance est donc éprouvée contre la date du
        // **prochain** événement, et si elle tombe, l'horloge n'avance pas
        // jusque-là : s'arrêter après le saut placerait l'état final au-delà de
        // l'instant de la violation, et l'événement extrait serait perdu.
        self.oracles.echoir(date);
        if self.arreter_sur_violation() {
            return None;
        }

        let ev = self.file.pop().expect("la file vient d'être sondée");

        // Avance sans attente réelle (EX-C01).
        self.horloge = ev.date;
        self.evenements_consommes += 1;

        self.trace.absorber(ev.date.0);
        self.trace.absorber(ev.seq);
        self.trace.absorber(ev.cible.0 as u64);

        Some(ev)
    }

    /// Arme `Arret::Violation` si une violation est enregistrée, et dit si
    /// l'exécution doit s'arrêter.
    ///
    /// Nomme la violation de **date minimale** — pas la première enregistrée :
    /// un gestionnaire peut en signaler plusieurs dans le même tour, et c'est la
    /// plus ancienne qui a arrêté l'exécution (EX-C09). L'ordre d'insertion
    /// départage, comme partout ailleurs dans le moteur.
    fn arreter_sur_violation(&mut self) -> bool {
        let plus_ancienne = self
            .oracles
            .violations()
            .iter()
            .enumerate()
            .min_by_key(|(i, v)| (v.date, *i))
            .map(|(_, v)| v.oracle);
        match plus_ancienne {
            Some(nom) => {
                self.arret = Some(Arret::Violation(nom));
                true
            }
            None => false,
        }
    }

    /// Fait avancer le processus de partition à deux états. À appeler par la
    /// boucle de l'appelant, qui seul connaît la population.
    ///
    /// **Ne tire pas les pannes** : `ModeleFaute::tirer_pannes` demande la liste
    /// des domaines, que le moteur ne détient pas, et l'appelant l'invoque
    /// lui-même. La partition, elle, ne dépend que du temps, donc elle est
    /// cadencée ici.
    pub fn avancer_partition(&mut self, nb_acteurs: usize) {
        let maintenant = self.horloge;
        self.fautes
            .partition
            .avancer(maintenant, nb_acteurs, &mut self.alea);
        if self.fautes.partition.en_cours() {
            self.couverture.atteindre("partition en cours");
        }
    }

    /// Installe le modèle de faute de la configuration.
    ///
    /// Sans cet appel, le moteur garde `ModeleFaute::default()`, c'est-à-dire
    /// **aucune faute** : la partition ne se déclenche jamais et le taux
    /// d'omission reste nul, quelle que soit la `Config` chargée. Le constat
    /// figure dans `ModeleFaute::hors_modele()` tant qu'aucun scénario livré ne
    /// s'en sert.
    pub fn installer_fautes(&mut self, fautes: ModeleFaute) {
        self.fautes = fautes;
    }

    /// Le modèle de faute en vigueur, pour l'affichage d'EX-C06 et d'EX-V07 :
    /// le bandeau doit montrer le modèle **actif**, pas une phrase constante.
    pub fn fautes(&self) -> &ModeleFaute {
        &self.fautes
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn moteur() -> Moteur<u32> {
        Moteur::nouveau(1, Granularite::Milli, Budget::evenements(10_000))
    }

    /// EX-C01 — l'ordre de sortie est celui des dates, pas celui d'insertion.
    #[test]
    fn la_file_rend_la_date_minimale() {
        let mut m = moteur();
        m.pousser_a(Instant(30), ActeurId(0), 30);
        m.pousser_a(Instant(10), ActeurId(0), 10);
        m.pousser_a(Instant(20), ActeurId(0), 20);
        let dates: Vec<u64> = std::iter::from_fn(|| m.suivant())
            .map(|e| e.date.0)
            .collect();
        assert_eq!(dates, vec![10, 20, 30]);
    }

    /// EX-C03 — à date égale, le départage suit le compteur d'insertion, et
    /// jamais l'ordre interne du tas.
    #[test]
    fn les_egalites_sont_departagees_par_la_sequence() {
        let mut m = moteur();
        for i in 0..64u32 {
            m.pousser_a(Instant(5), ActeurId(i), i);
        }
        let charges: Vec<u32> = std::iter::from_fn(|| m.suivant())
            .map(|e| e.charge)
            .collect();
        assert_eq!(charges, (0..64).collect::<Vec<u32>>());
    }

    /// EX-C01 — l'horloge saute à la date de l'événement, sans attente.
    #[test]
    fn lhorloge_saute_a_la_date() {
        let mut m = moteur();
        m.pousser_a(Instant(1_000_000), ActeurId(0), 0);
        assert_eq!(m.maintenant(), Instant(0));
        m.suivant().unwrap();
        assert_eq!(m.maintenant(), Instant(1_000_000));
    }

    #[test]
    fn le_temps_logique_ne_recule_pas() {
        let mut m = moteur();
        m.pousser_a(Instant(100), ActeurId(0), 0);
        m.suivant().unwrap();
        m.pousser_a(Instant(50), ActeurId(0), 1);
        let ev = m.suivant().unwrap();
        assert_eq!(ev.date, Instant(100));
    }

    /// EX-C02 — même graine, même configuration, même trace.
    #[test]
    fn deux_executions_de_meme_graine_ont_la_meme_trace() {
        fn executer(graine: u64) -> u64 {
            let mut m: Moteur<u32> =
                Moteur::nouveau(graine, Granularite::Milli, Budget::evenements(5_000));
            for i in 0..50u32 {
                m.pousser(Duree(i as u64 % 7), ActeurId(i % 5), i);
            }
            while let Some(ev) = m.suivant() {
                if ev.charge % 3 == 0 {
                    let d = Duree((m.alea.uniforme() * 10.0) as u64);
                    m.pousser(d, ActeurId(ev.charge % 5), ev.charge + 1);
                }
                m.marquer(ev.charge as u64);
            }
            m.trace().valeur()
        }
        assert_eq!(executer(7), executer(7));
        assert_ne!(executer(7), executer(8));
    }

    #[test]
    fn le_budget_devenements_arrete_lexecution() {
        let mut m: Moteur<u32> = Moteur::nouveau(1, Granularite::Milli, Budget::evenements(3));
        for i in 0..10u32 {
            m.pousser_a(Instant(i as u64), ActeurId(0), i);
        }
        let n = std::iter::from_fn(|| m.suivant()).count();
        assert_eq!(n, 3);
        assert_eq!(m.arret(), Some(&Arret::BudgetEvenements));
    }

    #[test]
    fn le_budget_de_temps_est_rapporte_de_lexterieur() {
        let mut m: Moteur<u32> = Moteur::nouveau(
            1,
            Granularite::Milli,
            Budget::evenements(1_000).avec_secondes_coeur(1.0),
        );
        m.pousser_a(Instant(1), ActeurId(0), 0);
        m.pousser_a(Instant(2), ActeurId(0), 1);
        assert!(m.suivant().is_some());
        m.budget.consommer_temps(1.5);
        assert!(m.suivant().is_none());
        assert_eq!(m.arret(), Some(&Arret::BudgetTemps));
    }

    /// EX-C09 — l'exécution s'arrête à la violation.
    #[test]
    fn une_violation_arrete_lexecution() {
        use crate::oracle::Oracle;
        let mut m = moteur();
        m.oracles.armer(Oracle::surete("m1", "§1.2"));
        for i in 0..10u32 {
            m.pousser_a(Instant(i as u64), ActeurId(0), i);
        }
        m.suivant().unwrap();
        m.oracles.violer("m1", m.maintenant(), "ordre rompu");
        assert!(m.suivant().is_none());
        assert_eq!(m.arret(), Some(&Arret::Violation("m1")));
    }

    /// EX-C09 — une violation **déjà enregistrée** l'emporte sur les trois
    /// autres motifs d'arrêt, et non sur le seul budget d'événements. L'arrêt
    /// demandé et le budget de temps sont rapportés de l'extérieur, donc
    /// postérieurs à la violation : les rapporter à sa place enterre le seul
    /// motif qui soit un défaut sous une raison administrative.
    #[test]
    fn une_violation_enregistree_lemporte_sur_les_autres_arrets() {
        use crate::oracle::Oracle;

        // (a) budget de temps épuisé au même tour.
        let mut m: Moteur<u32> = Moteur::nouveau(
            1,
            Granularite::Milli,
            Budget::evenements(1_000).avec_secondes_coeur(1.0),
        );
        m.oracles.armer(Oracle::surete("m1", "§1.2"));
        m.pousser_a(Instant(1), ActeurId(0), 0);
        m.pousser_a(Instant(2), ActeurId(0), 1);
        m.suivant().unwrap();
        m.oracles.violer("m1", m.maintenant(), "ordre rompu");
        m.budget.consommer_temps(1.5);
        assert!(m.suivant().is_none());
        assert_eq!(m.arret(), Some(&Arret::Violation("m1")));

        // (b) arrêt demandé au même tour.
        let mut m: Moteur<u32> = Moteur::nouveau(1, Granularite::Milli, Budget::evenements(1_000));
        m.oracles.armer(Oracle::surete("m2", "§1.2"));
        m.pousser_a(Instant(1), ActeurId(0), 0);
        m.suivant().unwrap();
        m.oracles.violer("m2", m.maintenant(), "ordre rompu");
        m.budget.demander_arret();
        assert!(m.suivant().is_none());
        assert_eq!(m.arret(), Some(&Arret::Violation("m2")));

        // (c) budget d'événements épuisé au même tour — déjà tenu avant.
        let mut m: Moteur<u32> = Moteur::nouveau(1, Granularite::Milli, Budget::evenements(1));
        m.oracles.armer(Oracle::surete("m3", "§1.2"));
        m.pousser_a(Instant(1), ActeurId(0), 0);
        m.pousser_a(Instant(2), ActeurId(0), 1);
        m.suivant().unwrap();
        m.oracles.violer("m3", m.maintenant(), "ordre rompu");
        assert!(m.suivant().is_none());
        assert_eq!(m.arret(), Some(&Arret::Violation("m3")));
    }

    /// La file vide n'est pas une terminaison : c'est l'épuisement des
    /// événements, et EX-C10b interdit de le présenter comme une complétude.
    #[test]
    fn la_file_vide_est_un_arret_nomme() {
        let mut m = moteur();
        m.pousser_a(Instant(1), ActeurId(0), 0);
        m.suivant().unwrap();
        assert!(m.suivant().is_none());
        assert_eq!(m.arret(), Some(&Arret::FileVide));
    }
}
