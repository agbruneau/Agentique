//! Scénario K — la fenêtre de violation (EX-A09, EX-A30, EX-A54, EX-V20,
//! EX-V21).
//!
//! > Le budget est un plafond, pas une garantie. (§5.3)
//!
//! **PD11** — la gouvernance ne produit rien, elle interdit. Aucun levier n'est
//! présenté comme un invariant : chacun affiche **la durée pendant laquelle
//! l'invariant qu'il protège peut être faux**, et « non bornée » s'affiche « non
//! bornée », jamais « grande ».

use crate::Bloc;
use sim_core::temps::Duree;

/// Le bloc de trois du **scénario K** — la fenêtre de violation (PD8).
pub const BLOC_K: Bloc = Bloc {
    en_clair:
        "On donne à chaque agent un quota, pour que la somme de leurs demandes reste tenable. \
         Chaque agent respecte le sien, et le total dépasse quand même ce que le système peut \
         servir : aucune règle locale ne voit la somme. Sans autorité centrale, tout garde-fou \
         réparti a une durée pendant laquelle la règle qu'il protège est fausse — l'honnêteté \
         consiste à borner cette durée, pas à prétendre qu'elle n'existe pas.",
    these: "Le budget est un plafond, pas une garantie.",
    source: "§5.3, tableau 16, p. 84 (3ᵉ éd.)",
    mecanisme_visible:
        "activer le budget de reprise borne l'amplification par client à 1,1 fois la charge \
         nominale ; la dépendance saturée reçoit alors 1,1 × la charge nominale de chacun des \
         clients conformes, et aucune règle locale ne voit l'agrégat. Basculer en asynchrone \
         retire Δ, et toutes les fenêtres chiffrées deviennent « non bornées ».",
    ne_demontre_pas:
        "les valeurs de 23 % contre 46 %, le facteur 10 sur les incidents d'épuisement mémoire et \
         la couverture de plus de 48 % de la flotte : ce sont des mesures d'une flotte réelle, \
         affichées comme repère de provenance externe et jamais comme cible. Ce que le scénario \
         mesure est le **signe** de l'écart et son mécanisme causal — un agent autonome qui \
         estime lui-même son besoin le surestime, parce que le coût d'une sous-estimation lui est \
         imputé alors que le coût d'une surestimation est mutualisé. C'est une externalité, et \
         aucune règle locale ne la corrige : seule une politique imposée le fait, c'est-à-dire une \
         autorité (PD11). Ni l'émergence, faute de paramètre d'ordre (PD5).",
};

/// Les leviers du tableau 16 (EX-A30).
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Levier {
    /// Classes de criticité : elles ne bornent **rien** tant qu'un délesteur
    /// ne les lit pas.
    ClassesDeCriticite,
    /// Quota délibérément surengagé.
    QuotaSurengage,
    /// Budget de reprise : il borne un client, jamais l'agrégat de tous.
    BudgetDeReprise,
    /// Étranglement adaptatif : il ne borne pas la fenêtre déjà écoulée.
    EtranglementAdaptatif,
    /// Budget de perturbation : il ne borne pas les perturbations
    /// involontaires, qui le consomment sans pouvoir être empêchées.
    BudgetDePerturbation,
    /// Dimensionnement automatique : il ne borne pas un agent qui surestime
    /// son besoin.
    DimensionnementAutomatique,
}

/// Les quatre classes de criticité, comme taxonomie explicite.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Criticite {
    /// La plus haute : jamais délestée.
    CriticalPlus,
    /// Critique.
    Critical,
    /// Délestable en dernier recours.
    SheddablePlus,
    /// Délestable la première.
    Sheddable,
}

impl Criticite {
    /// Les quatre classes, de la plus haute à la plus délestable.
    pub const TOUTES: [Criticite; 4] = [
        Criticite::CriticalPlus,
        Criticite::Critical,
        Criticite::SheddablePlus,
        Criticite::Sheddable,
    ];

    /// Le nom de la classe, tel qu'il apparaît dans la source.
    pub fn nom(self) -> &'static str {
        match self {
            Criticite::CriticalPlus => "CRITICAL_PLUS",
            Criticite::Critical => "CRITICAL",
            Criticite::SheddablePlus => "SHEDDABLE_PLUS",
            Criticite::Sheddable => "SHEDDABLE",
        }
    }
}

impl Levier {
    /// Nom affiché du levier.
    pub fn nom(self) -> &'static str {
        match self {
            Levier::ClassesDeCriticite => "classes de criticité",
            Levier::QuotaSurengage => "quota délibérément surengagé",
            Levier::BudgetDeReprise => "budget de reprise",
            Levier::EtranglementAdaptatif => "étranglement adaptatif",
            Levier::BudgetDePerturbation => "budget de perturbation",
            Levier::DimensionnementAutomatique => "dimensionnement automatique par mesure",
        }
    }

    /// **EX-V21, EX-A30** — ce que le levier **ne borne pas**. Cette colonne est
    /// testée, jamais citée.
    pub fn ne_borne_pas(self) -> &'static str {
        match self {
            Levier::ClassesDeCriticite => "rien, tant qu'un délesteur ne les lit pas",
            Levier::QuotaSurengage => "la somme des quotas, qui dépasse délibérément la capacité",
            Levier::BudgetDeReprise => "l'agrégat de tous les clients",
            Levier::EtranglementAdaptatif => "la fenêtre de deux minutes déjà écoulée",
            Levier::BudgetDePerturbation => {
                "les perturbations involontaires, qui le consomment sans pouvoir être empêchées"
            }
            Levier::DimensionnementAutomatique => "un agent qui surestime son besoin",
        }
    }

    /// **EX-V21** — la durée pendant laquelle l'invariant protégé peut être
    /// faux. `None` signifie **non bornée** — et l'affichage l'écrit ainsi,
    /// jamais « grande ».
    pub fn fenetre_de_violation(self, asynchrone: bool, fenetre_etranglement: Duree) -> Option<Duree> {
        if asynchrone {
            // Sans Δ, aucune fenêtre n'est bornée (RQ8).
            return None;
        }
        match self {
            Levier::EtranglementAdaptatif => Some(fenetre_etranglement),
            Levier::BudgetDeReprise => Some(Duree(0)),
            Levier::ClassesDeCriticite => None,
            Levier::QuotaSurengage => None,
            Levier::BudgetDePerturbation => None,
            Levier::DimensionnementAutomatique => None,
        }
    }

    /// Affichage de la fenêtre (EX-V21, RQ8).
    pub fn affichage_fenetre(self, asynchrone: bool, fenetre_etranglement: Duree) -> String {
        match self.fenetre_de_violation(asynchrone, fenetre_etranglement) {
            Some(d) => format!("{} tics", d.0),
            None => "**non bornée**".to_string(),
        }
    }
}

/// **EX-A09** — étranglement adaptatif et délestage par criticité.
///
/// `K = 2`, fenêtre de 120 s, au plus 3 tentatives, plafond de 10 % du volume
/// client.
#[derive(Clone, Copy, Debug)]
pub struct BudgetDeReprise {
    /// Facteur K de l'étranglement adaptatif.
    pub k: f64,
    /// Fenêtre glissante.
    pub fenetre: Duree,
    /// Nombre maximal de tentatives.
    pub tentatives_max: u32,
    /// Plafond de reprises, en fraction du volume client.
    pub plafond: f64,
}

impl Default for BudgetDeReprise {
    fn default() -> Self {
        BudgetDeReprise {
            k: 2.0,
            fenetre: Duree(120),
            tentatives_max: 3,
            plafond: 0.10,
        }
    }
}

impl BudgetDeReprise {
    /// Amplification **par client** : la charge nominale plus les reprises,
    /// plafonnées.
    pub fn amplification_par_client(&self, actif: bool) -> f64 {
        if actif {
            1.0 + self.plafond
        } else {
            // Sans budget, chaque échec est réessayé jusqu'au maximum.
            self.tentatives_max as f64
        }
    }

    /// Amplification **agrégée** sur `clients` tous conformes.
    ///
    /// C'est ce que le budget **ne borne pas** : chaque client respecte son
    /// plafond, et la dépendance saturée reçoit la somme.
    pub fn amplification_agregee(&self, clients: u32, actif: bool) -> f64 {
        self.amplification_par_client(actif) * clients as f64
    }
}

/// **EX-A54** — le prix de l'anarchie, **mesuré et non postulé**.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum ClasseDeLatence {
    /// Borne 4/3.
    Lineaire,
    /// Borne p + 1.
    Polynomiale(u32),
    /// Fonctions générales continues non décroissantes : la seule borne
    /// disponible est que la latence à l'équilibre n'excède pas celle d'un
    /// optimum contraint d'acheminer **deux fois** le trafic.
    Generale,
}

impl ClasseDeLatence {
    /// La borne du prix de l'anarchie pour cette classe. `INFINITY` pour le cas
    /// général, où il n'existe **aucun rapport borné** — et non un rapport
    /// grand.
    pub fn borne(self) -> f64 {
        match self {
            ClasseDeLatence::Lineaire => 4.0 / 3.0,
            ClasseDeLatence::Polynomiale(p) => p as f64 + 1.0,
            // Pas un rapport : un énoncé sur un optimum contraint.
            ClasseDeLatence::Generale => f64::INFINITY,
        }
    }

    /// L'énoncé complet de la borne, tel qu'il s'affiche.
    pub fn libelle(self) -> String {
        match self {
            ClasseDeLatence::Lineaire => "4/3 — latence linéaire en la congestion".to_string(),
            ClasseDeLatence::Polynomiale(p) => {
                format!("{} — polynôme de degré {p} à coefficients positifs", p + 1)
            }
            ClasseDeLatence::Generale => {
                "aucun rapport borné : la latence à l'équilibre n'excède pas celle d'un optimum \
                 contraint d'acheminer DEUX FOIS le trafic"
                    .to_string()
            }
        }
    }
}

/// Mesure du prix de l'anarchie, **toujours accompagnée** de la fraction de
/// charge portée par le plus gros agent.
///
/// **Une borne affichée sans cette fraction est un défaut bloquant** (EX-A54) :
/// la borne suppose un nombre infini d'agents infinitésimaux, et un essaim de
/// n = 40 agents portant 2,5 % chacun ne la satisfait pas.
#[derive(Clone, Copy, Debug)]
pub struct PrixDeLanarchie {
    /// Le rapport **mesuré** entre l'équilibre et l'optimum.
    pub rapport_mesure: f64,
    /// La classe de latence, qui décide de la borne applicable.
    pub classe: ClasseDeLatence,
    /// Fraction de charge portée par le plus gros agent.
    pub fraction_du_plus_gros: f64,
}

impl PrixDeLanarchie {
    /// L'hypothèse d'atomicité tient-elle ? Elle exige que chaque agent porte
    /// une fraction négligeable.
    pub fn agents_infinitesimaux(&self) -> bool {
        self.fraction_du_plus_gros < 0.01
    }

    /// La borne est-elle respectée ?
    pub fn dans_la_borne(&self) -> bool {
        self.rapport_mesure <= self.classe.borne()
    }

    /// **EX-A54** — l'affichage, qui ne se fait jamais sans la fraction.
    pub fn affichage(&self) -> String {
        format!(
            "rapport équilibre/optimum mesuré {:.4} contre la borne {} ; **fraction de charge du \
             plus gros agent : {:.3}** — la borne suppose un nombre infini d'agents \
             infinitésimaux, et {} (EX-A54).",
            self.rapport_mesure,
            self.classe.libelle(),
            self.fraction_du_plus_gros,
            if self.agents_infinitesimaux() {
                "l'hypothèse tient ici"
            } else {
                "elle NE TIENT PAS ici : la borne ne s'applique pas"
            }
        )
    }
}

/// Estimation du besoin en ressources.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Estimation {
    /// L'agent déclare lui-même son besoin. Il le **surestime**, parce que le
    /// coût d'une sous-estimation lui est imputé alors que le coût d'une
    /// surestimation est mutualisé. C'est une externalité.
    AutoDeclaree,
    /// Le besoin est mesuré.
    Mesuree,
}

impl Estimation {
    /// Part de ressources réservées **non utilisées**.
    pub fn part_non_utilisee(self) -> f64 {
        match self {
            Estimation::AutoDeclaree => 0.46,
            Estimation::Mesuree => 0.23,
        }
    }

    /// Provenance des deux chiffres, affichée avec eux (F1, F2).
    pub const PROVENANCE: &'static str =
        "23 % contre 46 % : mesures d'une flotte réelle, **repère de provenance externe** (F2), \
         jamais une cible du simulateur. Ce que le scénario mesure est le SENS de l'écart et son \
         mécanisme causal.";

    /// L'externalité en toutes lettres : aucune règle **locale** ne la corrige.
    pub const EXTERNALITE: &'static str =
        "un agent autonome qui estime lui-même son besoin le surestime : le coût d'une \
         sous-estimation lui est imputé, celui d'une surestimation est mutualisé. Aucune règle \
         locale ne corrige cette externalité — seule une politique imposée le fait, c'est-à-dire \
         une autorité (PD11).";
}

/// **EX-V20** — toute borne de distribution s'affiche avec le compteur d'agents
/// **individuellement non conformes** à côté d'elle.
pub fn affichage_borne_de_distribution(borne: f64, non_conformes: u32, n: u32) -> String {
    format!(
        "borne de distribution {borne:.4} — elle **ne dit rien d'un agent particulier**. Agents \
         individuellement non conformes : {non_conformes} sur {n}. Un essaim conforme en \
         distribution peut contenir un agent qui viole toutes les contraintes qu'on croyait \
         garanties (EX-V20, RQ11)."
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::cycle_de_vie::{BudgetPerturbation, Perturbation};

    /// **Critère (1) du scénario K** — avec budget de reprise, l'amplification
    /// **par client** est bornée à 1,1 ; l'**agrégat** de clients tous
    /// conformes ne l'est pas.
    #[test]
    fn critere_1_le_budget_borne_le_client_et_pas_lagregat() {
        let b = BudgetDeReprise::default();
        assert!((b.amplification_par_client(true) - 1.1).abs() < 1e-9);
        // Cent clients tous conformes : la dépendance reçoit 110 fois la charge
        // nominale d'un client, et aucune règle locale ne voit cet agrégat.
        assert!((b.amplification_agregee(100, true) - 110.0).abs() < 1e-9);
        // « L'agrégat n'est borné par rien » : il croît proportionnellement au
        // nombre de clients, sans plafond. Comparer l'agrégat de cent clients à
        // cinquante fois l'amplification d'un seul serait une conséquence
        // arithmétique des deux lignes ci-dessus, donc une assertion qui ne peut
        // pas échouer ; ce qui se réfute est la **croissance sans plafond**.
        let mut precedent = 0.0;
        for clients in [1u32, 10, 1_000, 100_000, 10_000_000] {
            let a = b.amplification_agregee(clients, true);
            assert!(
                (a - 1.1 * f64::from(clients)).abs() < 1e-6 * a.max(1.0),
                "{clients} clients : agrégat {a}, attendu 1,1 × {clients}"
            );
            assert!(a > precedent, "l'agrégat a cessé de croître à {clients} clients");
            precedent = a;
        }
        assert_eq!(
            Levier::BudgetDeReprise.ne_borne_pas(),
            "l'agrégat de tous les clients"
        );
    }

    /// Sans budget, chaque client réessaie jusqu'au maximum.
    #[test]
    fn sans_budget_lamplification_par_client_atteint_le_maximum() {
        let b = BudgetDeReprise::default();
        assert!((b.amplification_par_client(false) - 3.0).abs() < 1e-9);
        assert_eq!(b.k, 2.0);
        assert_eq!(b.fenetre, Duree(120));
    }

    /// **Critère (2)** — les perturbations involontaires **consomment** le
    /// budget jusqu'à épuisement sans qu'aucune ne soit empêchée, et une
    /// suppression directe le contourne entièrement.
    #[test]
    fn critere_2_les_involontaires_consomment_sans_etre_empechees() {
        let mut b = BudgetPerturbation::nouveau(2);
        for _ in 0..5 {
            assert!(
                b.soumettre(Perturbation::Involontaire),
                "aucune involontaire n'est empêchée"
            );
        }
        assert_eq!(b.consommees(), 5, "elles ont consommé au-delà du plafond");
        assert!(!b.soumettre(Perturbation::Volontaire), "et le volontaire est refusé");
        assert!(b.soumettre(Perturbation::SuppressionDirecte), "qui contourne");
    }

    /// **Critère (3)** — le rapport reste sous 4/3 en latence linéaire tant que
    /// la fraction du plus gros agent est négligeable, et **sort de la borne**
    /// quand n est petit. C'est ce dernier point que le scénario existe pour
    /// montrer.
    #[test]
    fn critere_3_la_borne_sort_de_son_domaine_quand_n_est_petit() {
        // Essaim nombreux, agents infinitésimaux : la borne s'applique.
        let grand = PrixDeLanarchie {
            rapport_mesure: 1.25,
            classe: ClasseDeLatence::Lineaire,
            fraction_du_plus_gros: 0.001,
        };
        assert!(grand.agents_infinitesimaux());
        assert!(grand.dans_la_borne());
        assert!(grand.affichage().contains("l'hypothèse tient ici"));

        // n = 40 agents portant 2,5 % chacun : elle ne s'applique plus.
        let petit = PrixDeLanarchie {
            rapport_mesure: 1.25,
            classe: ClasseDeLatence::Lineaire,
            fraction_du_plus_gros: 0.025,
        };
        assert!(!petit.agents_infinitesimaux());
        assert!(petit.affichage().contains("NE TIENT PAS"));
    }

    /// **Critère (3)** — en latence polynomiale de degré 3, la borne applicable
    /// est **4**, non 4/3.
    #[test]
    fn critere_3b_la_borne_depend_de_la_classe_de_latence() {
        assert!((ClasseDeLatence::Lineaire.borne() - 4.0 / 3.0).abs() < 1e-9);
        assert!((ClasseDeLatence::Polynomiale(3).borne() - 4.0).abs() < 1e-9);
        assert!(ClasseDeLatence::Generale.borne().is_infinite());
        assert!(ClasseDeLatence::Generale.libelle().contains("DEUX FOIS le trafic"));
    }

    /// **EX-A54** — une borne affichée sans la fraction du plus gros agent est
    /// un défaut bloquant : l'affichage la porte toujours.
    #[test]
    fn ex_a54_la_borne_ne_sannonce_jamais_sans_la_fraction() {
        let p = PrixDeLanarchie {
            rapport_mesure: 1.1,
            classe: ClasseDeLatence::Lineaire,
            fraction_du_plus_gros: 0.02,
        };
        assert!(p.affichage().contains("fraction de charge du plus gros agent"));
    }

    /// **Critère (4)** — le passage de l'estimation auto-déclarée à mesurée
    /// réduit la part réservée non utilisée, dans le **sens** annoncé. Les
    /// valeurs, elles, sont des repères externes.
    #[test]
    fn critere_4_lestimation_mesuree_reduit_la_part_non_utilisee() {
        assert!(Estimation::Mesuree.part_non_utilisee() < Estimation::AutoDeclaree.part_non_utilisee());
        assert!(Estimation::PROVENANCE.contains("repère de provenance externe"));
        assert!(Estimation::EXTERNALITE.contains("Aucune règle locale"));
        assert!(Estimation::EXTERNALITE.contains("autorité"));
    }

    /// **Critère (5)** — en mode asynchrone, **chaque** levier affiche
    /// « fenêtre non bornée » et aucune valeur chiffrée n'apparaît.
    #[test]
    fn critere_5_en_asynchrone_toutes_les_fenetres_sont_non_bornees() {
        let leviers = [
            Levier::ClassesDeCriticite,
            Levier::QuotaSurengage,
            Levier::BudgetDeReprise,
            Levier::EtranglementAdaptatif,
            Levier::BudgetDePerturbation,
            Levier::DimensionnementAutomatique,
        ];
        for l in leviers {
            let a = l.affichage_fenetre(true, Duree(120));
            assert_eq!(a, "**non bornée**", "{}", l.nom());
            assert!(!a.contains("tics"), "aucune valeur chiffrée");
        }
        // Sous synchronisme partiel, seuls certains leviers ont une fenêtre
        // chiffrée ; les autres restent non bornés, et le disent.
        assert!(Levier::EtranglementAdaptatif
            .affichage_fenetre(false, Duree(120))
            .contains("120"));
        assert_eq!(
            Levier::DimensionnementAutomatique.affichage_fenetre(false, Duree(120)),
            "**non bornée**"
        );
    }

    /// **EX-A30** — chaque levier porte sa colonne « ce qu'il ne borne pas »,
    /// et les quatre classes de criticité sont une taxonomie explicite.
    #[test]
    fn ex_a30_chaque_levier_dit_ce_quil_ne_borne_pas() {
        for l in [
            Levier::ClassesDeCriticite,
            Levier::QuotaSurengage,
            Levier::BudgetDeReprise,
            Levier::EtranglementAdaptatif,
            Levier::BudgetDePerturbation,
            Levier::DimensionnementAutomatique,
        ] {
            assert!(!l.ne_borne_pas().is_empty(), "{}", l.nom());
        }
        // `TOUTES.len() == 4` était une vérité de compilation — le type est
        // `[Criticite; 4]` —, donc une assertion qui ne peut pas échouer. Ce que
        // la taxonomie promet et qui se réfute : les quatre entrées sont les
        // quatre classes de la source, chacune une fois, de la plus haute à la
        // plus délestable. Un doublon, un oubli ou une inversion tombe ici.
        assert_eq!(
            Criticite::TOUTES.map(Criticite::nom),
            ["CRITICAL_PLUS", "CRITICAL", "SHEDDABLE_PLUS", "SHEDDABLE"]
        );
    }

    /// **EX-V20** — toute borne de distribution s'affiche avec le compteur
    /// d'agents individuellement non conformes.
    #[test]
    fn ex_v20_la_borne_de_distribution_porte_son_compteur() {
        let a = affichage_borne_de_distribution(0.95, 3, 40);
        assert!(a.contains("ne dit rien d'un agent particulier"));
        assert!(a.contains("3 sur 40"));
    }

    /// PD8 — le bloc de trois.
    #[test]
    fn le_scenario_porte_son_bloc_de_trois() {
        assert!(BLOC_K.these.contains("plafond, pas une garantie"));
        assert!(BLOC_K.ne_demontre_pas.contains("externalité"));
    }
}
