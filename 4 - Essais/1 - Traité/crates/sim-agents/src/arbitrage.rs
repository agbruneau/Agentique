//! **File de demandes d'arbitrage** — l'essaim écrit vers l'opérateur
//! (EX-A59, §8.3 du traité).
//!
//! Symétrique exact de la directive d'EX-A07 : là où PD4 fait écrire la console
//! vers l'essaim, ce module fait écrire l'essaim vers l'opérateur. Un agent
//! bloqué, en conflit de mandat, ou constatant une ambiguïté qu'il n'a pas
//! autorité à trancher, écrit un enregistrement de demande sur un sujet dédié —
//! époque, auteur **apposé** (EX-M24), décalage — traité exactement comme une
//! directive.
//!
//! **Fondement mesuré.** Dans les épisodes du §8.3 du traité qui se règlent par une trêve,
//! les agents reconnaissent dans la conduite des autres l'exécution de directives
//! contradictoires plutôt qu'une hostilité, sortent de la boucle d'escalade,
//! nettoient le code malveillant qu'ils avaient déposé, écrivent des comptes
//! rendus, et **demandent l'intervention d'un humain**. La demande d'arbitrage
//! est un enregistrement comme un autre.
//!
//! **Coût** : 1 écriture par demande.
//!
//! **Ce qu'elle ne borne pas, et qui s'affiche avec elle** : le délai d'arrivée
//! de l'humain, qui n'est pas dans le système.

use sim_core::temps::{Duree, Instant};
use sim_milieu::journal::Identite;

/// Ce que le mécanisme ne borne pas (tableau 22, EX-V21).
pub const NE_BORNE_PAS: &str =
    "le délai d'arrivée de l'humain, qui n'est pas dans le système — la file borne l'attente \
     mesurée, jamais la réponse (EX-A59)";

/// Pourquoi un agent remonte une décision plutôt que de la prendre.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Motif {
    /// Mandats contradictoires constatés entre agents — le régime du §8.3 du traité.
    MandatsContradictoires,
    /// Blocage que l'agent ne peut pas dénouer dans son périmètre.
    Blocage,
    /// Ambiguïté de mandat : l'agent pourrait agir, et n'a pas autorité pour
    /// trancher. C'est le cas que la source relève comme le plus vertueux, et le
    /// plus facile à ne pas implanter.
    AmbiguiteDeMandat,
}

impl Motif {
    /// Libellé affiché.
    pub fn libelle(self) -> &'static str {
        match self {
            Motif::MandatsContradictoires => {
                "mandats contradictoires entre agents (§8.3 du \
                                              traité)"
            }
            Motif::Blocage => "blocage hors du périmètre de l'agent",
            Motif::AmbiguiteDeMandat => "ambiguïté de mandat — l'agent n'a pas autorité",
        }
    }
}

/// Une demande écrite par un agent.
#[derive(Clone, Debug, PartialEq)]
pub struct Demande {
    /// Auteur, apposé par le milieu (EX-M24) — jamais déclaré par l'agent.
    pub auteur: Identite,
    /// Époque de la vue de l'agent au moment de la demande, comme une directive.
    pub epoque: u64,
    /// Décalage attribué sur le sujet d'arbitrage.
    pub decalage: u64,
    /// Pourquoi.
    pub motif: Motif,
    /// Date d'écriture, en temps logique.
    pub ecrite_a: Instant,
    /// Date de traitement par l'opérateur, si elle a eu lieu.
    pub traitee_a: Option<Instant>,
}

/// Le sujet d'arbitrage, et son budget de latence propre.
#[derive(Clone, Debug)]
pub struct FileDarbitrage {
    demandes: Vec<Demande>,
    /// Budget de latence **propre** à ce sujet, distinct de celui des directives.
    budget_latence: Duree,
    ecritures: u64,
}

impl FileDarbitrage {
    /// Ouvre la file avec son budget de latence.
    pub fn nouvelle(budget_latence: Duree) -> FileDarbitrage {
        FileDarbitrage {
            demandes: Vec::new(),
            budget_latence,
            ecritures: 0,
        }
    }

    /// Un agent écrit sa demande. Coût : 1 écriture.
    pub fn demander(
        &mut self,
        auteur: Identite,
        epoque: u64,
        motif: Motif,
        maintenant: Instant,
    ) -> u64 {
        let decalage = self.demandes.len() as u64;
        self.demandes.push(Demande {
            auteur,
            epoque,
            decalage,
            motif,
            ecrite_a: maintenant,
            traitee_a: None,
        });
        self.ecritures += 1;
        decalage
    }

    /// L'opérateur traite la demande la plus ancienne non traitée.
    ///
    /// Rend `None` quand il n'y a rien à traiter. Le traitement est **hors du
    /// système** : ce module ne modélise pas la décision de l'humain, seulement
    /// l'instant où elle arrive.
    pub fn traiter_la_plus_ancienne(&mut self, maintenant: Instant) -> Option<u64> {
        let d = self.demandes.iter_mut().find(|d| d.traitee_a.is_none())?;
        d.traitee_a = Some(maintenant);
        Some(d.decalage)
    }

    /// Âge de la plus ancienne demande non traitée.
    ///
    /// **C'est la grandeur qui s'affiche avec le compte**, jamais le compte seul :
    /// c'est la règle de dérivée d'EX-V05 appliquée à une autre file — un compte
    /// de demandes traitées sans l'âge de la plus ancienne en attente ne dit rien.
    pub fn age_de_la_plus_ancienne(&self, maintenant: Instant) -> Option<Duree> {
        self.demandes
            .iter()
            .filter(|d| d.traitee_a.is_none())
            .map(|d| Duree(maintenant.0.saturating_sub(d.ecrite_a.0)))
            .max()
    }

    /// Le budget de latence est-il dépassé par la plus ancienne attente ?
    pub fn budget_depasse(&self, maintenant: Instant) -> bool {
        self.age_de_la_plus_ancienne(maintenant)
            .is_some_and(|a| a > self.budget_latence)
    }

    /// Demandes en attente.
    pub fn en_attente(&self) -> usize {
        self.demandes
            .iter()
            .filter(|d| d.traitee_a.is_none())
            .count()
    }

    /// Demandes traitées.
    pub fn traitees(&self) -> usize {
        self.demandes
            .iter()
            .filter(|d| d.traitee_a.is_some())
            .count()
    }

    /// Écritures effectuées — le coût du mécanisme.
    pub fn ecritures(&self) -> u64 {
        self.ecritures
    }

    /// Toutes les demandes, dans l'ordre du sujet (M1).
    pub fn demandes(&self) -> &[Demande] {
        &self.demandes
    }

    /// Affichage du panneau (EX-V23) : le compte **et** l'âge, jamais l'un sans
    /// l'autre, et le délai de l'humain déclaré hors du système.
    pub fn affichage(&self, maintenant: Instant, unite: &str) -> String {
        let age = match self.age_de_la_plus_ancienne(maintenant) {
            Some(a) => format!("{} {unite}", a.0),
            None => "—".to_string(),
        };
        format!(
            "{} en attente, {} traitées ; plus ancienne attente {age} ; budget {} {unite}{} — {}",
            self.en_attente(),
            self.traitees(),
            self.budget_latence.0,
            if self.budget_depasse(maintenant) {
                " (DÉPASSÉ)"
            } else {
                ""
            },
            NE_BORNE_PAS
        )
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use sim_core::ActeurId;

    fn qui(n: u32) -> Identite {
        Identite::propre(ActeurId(n))
    }

    #[test]
    fn une_demande_coute_une_ecriture_et_porte_son_auteur_appose() {
        let mut f = FileDarbitrage::nouvelle(Duree(100));
        let d = f.demander(qui(3), 7, Motif::Blocage, Instant(10));
        assert_eq!(d, 0);
        assert_eq!(f.ecritures(), 1);
        assert_eq!(f.demandes()[0].auteur, qui(3));
        assert_eq!(f.demandes()[0].epoque, 7);
    }

    #[test]
    fn lage_de_la_plus_ancienne_saffiche_avec_le_compte() {
        let mut f = FileDarbitrage::nouvelle(Duree(100));
        f.demander(qui(0), 1, Motif::Blocage, Instant(10));
        f.demander(qui(1), 1, Motif::AmbiguiteDeMandat, Instant(50));
        assert_eq!(f.age_de_la_plus_ancienne(Instant(60)), Some(Duree(50)));
        let a = f.affichage(Instant(60), "µs");
        assert!(a.contains("2 en attente"));
        assert!(a.contains("plus ancienne attente 50"));
        assert!(a.contains("pas dans le système"));
    }

    #[test]
    fn le_traitement_prend_la_plus_ancienne() {
        let mut f = FileDarbitrage::nouvelle(Duree(100));
        f.demander(qui(0), 1, Motif::Blocage, Instant(10));
        f.demander(qui(1), 1, Motif::Blocage, Instant(20));
        assert_eq!(f.traiter_la_plus_ancienne(Instant(30)), Some(0));
        assert_eq!(f.en_attente(), 1);
        assert_eq!(f.traitees(), 1);
        assert_eq!(f.age_de_la_plus_ancienne(Instant(30)), Some(Duree(10)));
    }

    #[test]
    fn une_file_vide_na_ni_age_ni_depassement() {
        let f = FileDarbitrage::nouvelle(Duree(10));
        assert_eq!(f.age_de_la_plus_ancienne(Instant(1_000)), None);
        assert!(!f.budget_depasse(Instant(1_000)));
        assert!(f.affichage(Instant(1_000), "µs").contains("—"));
    }

    #[test]
    fn le_budget_de_latence_est_propre_a_ce_sujet() {
        let mut f = FileDarbitrage::nouvelle(Duree(5));
        f.demander(qui(0), 1, Motif::MandatsContradictoires, Instant(0));
        assert!(!f.budget_depasse(Instant(5)));
        assert!(f.budget_depasse(Instant(6)));
        assert!(f.affichage(Instant(6), "µs").contains("DÉPASSÉ"));
    }

    #[test]
    fn traiter_une_file_vide_ne_rend_rien() {
        let mut f = FileDarbitrage::nouvelle(Duree(1));
        assert_eq!(f.traiter_la_plus_ancienne(Instant(0)), None);
    }
}
