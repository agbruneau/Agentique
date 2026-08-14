//! Vérification statistique bornée (§8.4, EX-C18).
//!
//! Le mode vérification implante l'algorithme 2 du §3.2 :
//!
//! ```text
//! N = ⌈ ln(2/δ) / (2ε²) ⌉
//! ```
//!
//! **N est affiché avant de lancer**, avec ses repères — parce que le coût est
//! l'information, et qu'un utilisateur qui découvre après coup qu'il lui fallait
//! cent fois plus d'exécutions pour un chiffre significatif de plus n'a pas été
//! informé.
//!
//! La sortie est `p̂ ± ε` avec `Pr(|p̂ − p| > ε) < δ`, **jamais une valeur nue**.

use serde::{Deserialize, Serialize};

/// Paramètres d'une campagne de vérification.
#[derive(Clone, Copy, Debug, Serialize, Deserialize)]
pub struct Parametres {
    /// Demi-largeur de l'intervalle.
    pub epsilon: f64,
    /// Risque de dépassement.
    pub delta: f64,
}

impl Default for Parametres {
    fn default() -> Self {
        Parametres {
            epsilon: 1e-2,
            delta: 1e-2,
        }
    }
}

impl Parametres {
    /// `N = ⌈ ln(2/δ) / (2ε²) ⌉`.
    pub fn executions_necessaires(&self) -> u64 {
        (libm::log(2.0 / self.delta) / (2.0 * self.epsilon * self.epsilon)).ceil() as u64
    }

    /// **Affiché avant de lancer**, avec les repères du §8.4.
    pub fn affichage_avant_lancement(&self) -> String {
        let n = self.executions_necessaires();
        let dix_fois_plus_fin = Parametres {
            epsilon: self.epsilon / 10.0,
            delta: self.delta,
        };
        format!(
            "ε = {:.0e}, δ = {:.0e} → **N = {} exécutions**. Un chiffre significatif de plus — \
             ε = {:.0e} à la même confiance — en demanderait {} , soit **cent fois plus** (§8.4).",
            self.epsilon,
            self.delta,
            n,
            dix_fois_plus_fin.epsilon,
            dix_fois_plus_fin.executions_necessaires()
        )
    }
}

/// Comment une campagne s'est terminée.
#[derive(Clone, Debug, PartialEq)]
pub enum Issue {
    /// Le budget a été consommé, et une estimation est disponible.
    Estimation {
        /// L'estimation, jamais rendue sans ses deux bornes.
        p_chapeau: f64,
        /// Demi-largeur de l'intervalle.
        epsilon: f64,
        /// Probabilité que la vraie valeur soit hors de l'intervalle.
        delta: f64,
    },
    /// Le budget a été épuisé **sans aucune violation observée**.
    ///
    /// Ce n'est **pas** « aucune violation » : c'est « aucune violation
    /// observée en N exécutions ».
    AucuneViolationObservee {
        /// Nombre d'exécutions effectuées, sans lequel la phrase ne veut rien
        /// dire.
        n: u64,
    },
    /// La vérification **n'a pas terminé** dans son budget.
    ///
    /// C'est une **absence de verdict**, jamais une absence de problème — le
    /// piège que le §5.3 nomme à propos du model checking exhaustif.
    AbsenceDeVerdict {
        /// Pourquoi la campagne n'a pas pu conclure.
        raison: String,
    },
}

impl Issue {
    /// Le libellé affiché. Aucune de ces formulations n'est une valeur nue.
    pub fn libelle(&self) -> String {
        match self {
            Issue::Estimation {
                p_chapeau,
                epsilon,
                delta,
            } => format!(
                "p̂ = {p_chapeau:.6} ± {epsilon:.0e}, avec Pr(|p̂ − p| > {epsilon:.0e}) < {delta:.0e}"
            ),
            Issue::AucuneViolationObservee { n } => format!(
                "**aucune violation observée en {n} exécutions** — et non « aucune violation ». \
                 Un comportement dont la probabilité est inférieure au seuil d'échantillonnage \
                 n'est pas déclaré absent : **il n'est pas vu** (§8.4)."
            ),
            Issue::AbsenceDeVerdict { raison } => format!(
                "**absence de verdict** : {raison}. Passé une taille d'essaim, le vérificateur ne \
                 termine pas, et l'ingénieur reçoit un silence qu'il est tenté de lire comme une \
                 absence de problème (§5.3, EX-C18)."
            ),
        }
    }

    /// Vrai si l'issue conclut quelque chose sur la propriété.
    pub fn conclut(&self) -> bool {
        matches!(self, Issue::Estimation { .. })
    }
}

/// Une campagne de vérification statistique.
pub struct Campagne {
    /// ε et δ visés, qui fixent N.
    pub params: Parametres,
    executions: u64,
    violations: u64,
    /// Budget d'exécutions réellement accordé. S'il est inférieur à N, la
    /// campagne ne peut pas conclure.
    pub budget: u64,
}

impl Campagne {
    /// Campagne neuve. Un `budget` inférieur à
    /// [`Parametres::executions_necessaires`] mène à une absence de verdict, et
    /// c'est délibéré : mieux vaut le dire que rendre un chiffre sous-alimenté.
    pub fn nouvelle(params: Parametres, budget: u64) -> Campagne {
        Campagne {
            params,
            executions: 0,
            violations: 0,
            budget,
        }
    }

    /// Rapporte le résultat d'une exécution.
    pub fn observer(&mut self, violation: bool) {
        self.executions += 1;
        if violation {
            self.violations += 1;
        }
    }

    /// Nombre d'exécutions observées jusqu'ici.
    pub fn executions(&self) -> u64 {
        self.executions
    }

    /// Conclut la campagne.
    pub fn conclure(&self) -> Issue {
        let n = self.params.executions_necessaires();
        if self.executions < n.min(self.budget) {
            return Issue::AbsenceDeVerdict {
                raison: format!(
                    "{} exécutions sur les {n} nécessaires ; budget {}",
                    self.executions, self.budget
                ),
            };
        }
        if self.budget < n {
            return Issue::AbsenceDeVerdict {
                raison: format!(
                    "budget de {} exécutions insuffisant pour ε = {:.0e} et δ = {:.0e}, qui en \
                     demandent {n}",
                    self.budget, self.params.epsilon, self.params.delta
                ),
            };
        }
        if self.violations == 0 {
            return Issue::AucuneViolationObservee { n: self.executions };
        }
        Issue::Estimation {
            p_chapeau: self.violations as f64 / self.executions as f64,
            epsilon: self.params.epsilon,
            delta: self.params.delta,
        }
    }

    /// **Ce que la vérification ne dit pas** (§8.3, §8.4). Affiché en
    /// permanence.
    pub const REFUS: &'static [&'static str] = &[
        "un comportement dont la probabilité est inférieure au seuil d'échantillonnage n'est pas \
         déclaré absent — il n'est pas vu",
        "une campagne qui épuise son budget sans violation affiche « aucune violation observée en \
         N exécutions », jamais « aucune violation »",
        "une vérification qui ne termine pas dans son budget est rapportée comme absence de \
         verdict, jamais comme absence de problème",
    ];
}

#[cfg(test)]
mod tests {
    use super::*;

    /// §8.4 — les repères du traité sont **retrouvés** : ε = 10⁻², δ = 10⁻²
    /// donnent N ≈ 26 492 ; ε = 10⁻³ à la même confiance en demande ≈ 2,65 × 10⁶.
    #[test]
    fn les_reperes_du_traite_sont_retrouves() {
        let p = Parametres::default();
        assert_eq!(p.executions_necessaires(), 26_492);

        let fin = Parametres {
            epsilon: 1e-3,
            delta: 1e-2,
        };
        let n = fin.executions_necessaires();
        assert!(
            (n as f64 - 2.65e6).abs() / 2.65e6 < 0.01,
            "N = {n} pour ε = 10⁻³"
        );
        // Cent fois plus pour un chiffre significatif de plus.
        assert!((n as f64 / p.executions_necessaires() as f64 - 100.0).abs() < 1.0);
    }

    /// **N est affiché avant de lancer**, avec son repère.
    #[test]
    fn n_est_affiche_avant_de_lancer() {
        let a = Parametres::default().affichage_avant_lancement();
        assert!(a.contains("26492"), "{a}");
        assert!(a.contains("cent fois plus"), "{a}");
    }

    /// La sortie est `p̂ ± ε` avec sa confiance, **jamais une valeur nue**.
    #[test]
    fn la_sortie_porte_toujours_son_intervalle() {
        let p = Parametres::default();
        let mut c = Campagne::nouvelle(p, 30_000);
        for i in 0..p.executions_necessaires() {
            c.observer(i % 100 == 0);
        }
        let issue = c.conclure();
        assert!(issue.conclut());
        let l = issue.libelle();
        assert!(l.contains("p̂"), "{l}");
        assert!(l.contains("±"), "{l}");
        assert!(l.contains("Pr("), "{l}");
    }

    /// **EX-C18** — une campagne sans violation affiche « aucune violation
    /// **observée** en N exécutions », jamais « aucune violation ».
    #[test]
    fn ex_c18_aucune_violation_observee_nest_pas_aucune_violation() {
        let p = Parametres::default();
        let mut c = Campagne::nouvelle(p, 30_000);
        for _ in 0..p.executions_necessaires() {
            c.observer(false);
        }
        let l = c.conclure().libelle();
        assert!(l.contains("aucune violation observée"), "{l}");
        assert!(l.contains("il n'est pas vu"), "{l}");
        assert!(!l.contains("aucune violation en"), "{l}");
    }

    /// **EX-C18** — une vérification qui ne termine pas est une **absence de
    /// verdict**, jamais une absence de problème.
    #[test]
    fn ex_c18_une_verification_inachevee_est_une_absence_de_verdict() {
        let p = Parametres::default();
        // Budget très inférieur à N.
        let mut c = Campagne::nouvelle(p, 100);
        for _ in 0..100 {
            c.observer(false);
        }
        let issue = c.conclure();
        assert!(!issue.conclut());
        let l = issue.libelle();
        assert!(l.contains("absence de verdict"), "{l}");
        assert!(l.contains("absence de problème"), "{l}");
    }

    /// Les trois refus d'affichage sont énoncés.
    #[test]
    fn les_trois_refus_daffichage_sont_enonces() {
        assert_eq!(Campagne::REFUS.len(), 3);
        assert!(Campagne::REFUS[0].contains("il n'est pas vu"));
        assert!(Campagne::REFUS[1].contains("jamais « aucune violation »"));
        assert!(Campagne::REFUS[2].contains("jamais comme absence de problème"));
    }

    /// Le coût croît en 1/ε² : c'est ce qui rend le mode utilisable ou non.
    #[test]
    fn le_cout_croit_en_inverse_du_carre_de_epsilon() {
        let grossier = Parametres {
            epsilon: 1e-1,
            delta: 1e-2,
        };
        let fin = Parametres {
            epsilon: 1e-2,
            delta: 1e-2,
        };
        let rapport =
            fin.executions_necessaires() as f64 / grossier.executions_necessaires() as f64;
        assert!((rapport - 100.0).abs() < 1.0, "{rapport}");
    }
}
