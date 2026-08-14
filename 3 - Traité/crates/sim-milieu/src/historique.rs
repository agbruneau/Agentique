//! Historique vérifié par identité — la réputation comme projection du journal
//! (EX-M25, §8.2).
//!
//! > la réputation est une fonction de l'historique, et l'historique est
//! > exactement ce que le milieu conserve déjà. (§8.2)
//!
//! Ce module n'est **pas** un composant nouveau : c'est le mécanisme du sujet
//! compacté (EX-M10) appliqué à un autre objet. Pour chaque identité, la suite
//! de ses assertions et, **quand elle existe**, l'issue vérifiée de chacune.
//!
//! Coût : 1 écriture par vérification, 1 lecture compactée par consultation.
//!
//! **La condition d'échec est sérieuse et ce module la fait respecter.** Là où
//! l'issue n'est pas vérifiable — la plupart des jugements de conception —,
//! l'historique n'enregistre que la concordance avec la majorité, c'est-à-dire
//! qu'il récompense la conformité du §8.1 et **aggrave le mal qu'il devait
//! corriger**. [`Historique::poids`] refuse donc de rendre un poids dans ce
//! régime, au lieu de le rendre dégradé.

use crate::journal::Identite;
use std::collections::BTreeMap;

/// Ce que devient une assertion déposée.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Issue {
    /// Vérifiée et confirmée par un tiers : la vulnérabilité soumise était
    /// nouvelle et valide, la route annoncée rapide l'était, l'utilité déclarée
    /// s'est réalisée.
    Confirmee,
    /// Vérifiée et démentie.
    Dementie,
    /// **Non vérifiable.** Ce n'est pas « pas encore vérifiée » : c'est une
    /// assertion dont aucun tiers ne peut établir l'issue, et sa présence
    /// disqualifie tout poids calculé sur cette identité.
    NonVerifiable,
}

/// Ce que le régime des issues autorise à calculer.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Regime {
    /// Toutes les issues consultées sont vérifiables : un poids par source est
    /// légitime.
    Verifiable,
    /// Au moins une issue n'est pas vérifiable. Aucun poids n'est rendu.
    NonVerifiable,
}

/// Refus opposé à qui demande un poids sur des issues non vérifiables.
pub const REFUS_NON_VERIFIABLE: &str =
    "là où l'issue n'est pas vérifiable, l'historique n'enregistre que la concordance avec la \
     majorité, c'est-à-dire qu'il récompense la conformité du §8.1 et aggrave le mal qu'il \
     devait corriger — aucun poids n'est rendu (EX-M25)";

/// Le compte d'une identité.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub struct Compte {
    /// Assertions déposées par cette identité.
    pub assertions: u64,
    /// Issues confirmées.
    pub confirmees: u64,
    /// Issues démenties.
    pub dementies: u64,
    /// Assertions dont l'issue a été déclarée non vérifiable.
    pub non_verifiables: u64,
}

impl Compte {
    /// Fiabilité constatée : part des issues **vérifiées** qui ont été
    /// confirmées. `None` tant qu'aucune issue vérifiée n'existe — une fiabilité
    /// sans vérification serait un nombre sans provenance (F1).
    pub fn fiabilite(&self) -> Option<f64> {
        let verifiees = self.confirmees + self.dementies;
        if verifiees == 0 {
            return None;
        }
        Some(self.confirmees as f64 / verifiees as f64)
    }
}

/// Projection du journal par identité (EX-M25).
#[derive(Clone, Debug, Default)]
pub struct Historique {
    comptes: BTreeMap<Identite, Compte>,
    ecritures: u64,
    consultations: u64,
}

impl Historique {
    /// Historique vide.
    pub fn nouveau() -> Historique {
        Historique::default()
    }

    /// Enregistre une assertion déposée par cette identité. Aucune issue n'est
    /// connue à ce stade — c'est le point du §8.2 : ce qu'un agent dépose est ce
    /// qu'il **déclare** avoir fait.
    pub fn asserter(&mut self, qui: Identite) {
        self.comptes.entry(qui).or_default().assertions += 1;
    }

    /// Enregistre l'issue **vérifiée par un tiers** d'une assertion.
    ///
    /// Coût : 1 écriture. Le tiers n'est pas modélisé ici — c'est l'agent arbitre
    /// du §7.2, et le milieu ne fait que consigner ce qu'il rend.
    pub fn verifier(&mut self, qui: Identite, issue: Issue) {
        let c = self.comptes.entry(qui).or_default();
        match issue {
            Issue::Confirmee => c.confirmees += 1,
            Issue::Dementie => c.dementies += 1,
            Issue::NonVerifiable => c.non_verifiables += 1,
        }
        self.ecritures += 1;
    }

    /// Le compte d'une identité, sans consommer de consultation.
    pub fn compte(&self, qui: Identite) -> Compte {
        self.comptes.get(&qui).copied().unwrap_or_default()
    }

    /// Régime de cette identité : peut-on pondérer sur elle ?
    pub fn regime(&self, qui: Identite) -> Regime {
        if self.compte(qui).non_verifiables > 0 {
            Regime::NonVerifiable
        } else {
            Regime::Verifiable
        }
    }

    /// **Poids par source**, pour pondérer φ par la fiabilité constatée plutôt
    /// que par la seule quantité déposée.
    ///
    /// Coût : 1 lecture compactée par consultation.
    ///
    /// Deux refus, et ils ne sont pas négociables (EX-M25) :
    ///
    /// - `Err(REFUS_NON_VERIFIABLE)` dès qu'une issue non vérifiable figure au
    ///   compte de cette identité. Le mécanisme n'est pas dégradé, il est refusé.
    /// - `Ok(None)` quand aucune issue vérifiée n'existe encore : il n'y a rien à
    ///   pondérer, et rendre 1,0 par défaut ferait passer une absence de mesure
    ///   pour une fiabilité parfaite.
    pub fn poids(&mut self, qui: Identite) -> Result<Option<f64>, &'static str> {
        self.consultations += 1;
        if self.regime(qui) == Regime::NonVerifiable {
            return Err(REFUS_NON_VERIFIABLE);
        }
        Ok(self.compte(qui).fiabilite())
    }

    /// Écritures de vérification effectuées — le coût du mécanisme, à afficher.
    pub fn ecritures(&self) -> u64 {
        self.ecritures
    }

    /// Consultations effectuées, poids refusés compris.
    pub fn consultations(&self) -> u64 {
        self.consultations
    }

    /// Identités connues, dans l'ordre.
    pub fn identites(&self) -> impl Iterator<Item = (&Identite, &Compte)> {
        self.comptes.iter()
    }

    /// Ce que le mécanisme ne traite pas, à afficher au même rang que ce qu'il
    /// achète (EX-V21, tableau 22).
    pub fn ne_traite_pas() -> &'static str {
        "les jugements dont l'issue n'est pas vérifiable — l'historique y récompenserait la \
         conformité ; et la crédulité d'un lecteur, que l'attribution ne corrige pas (§8.2)"
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use sim_core::ActeurId;

    fn qui(n: u32) -> Identite {
        Identite::propre(ActeurId(n))
    }

    /// EX-M25 — une assertion sans issue vérifiée ne donne **aucun** poids. Un
    /// poids par défaut de 1,0 serait une pondération sur une issue inconnue.
    #[test]
    fn une_assertion_sans_issue_ne_donne_aucun_poids() {
        let mut h = Historique::nouveau();
        h.asserter(qui(0));
        h.asserter(qui(0));
        assert_eq!(h.compte(qui(0)).assertions, 2);
        assert_eq!(
            h.poids(qui(0)).expect("régime vérifiable"),
            None,
            "aucune issue vérifiée : rien à pondérer, et surtout pas 1,0"
        );
    }

    /// EX-M25 — la fiabilité est la part des issues **confirmées**, et rien d'autre.
    #[test]
    fn la_fiabilite_est_la_part_des_issues_confirmees() {
        let mut h = Historique::nouveau();
        for _ in 0..3 {
            h.verifier(qui(1), Issue::Confirmee);
        }
        h.verifier(qui(1), Issue::Dementie);
        assert_eq!(h.poids(qui(1)).unwrap(), Some(0.75));
        assert_eq!(h.ecritures(), 4, "1 écriture par vérification");
    }

    /// EX-M25 — une issue non vérifiable fait **refuser** le poids, et non rendre
    /// un poids dégradé : pondérer sur une issue qu'on ne sait pas juger est pire
    /// que ne pas pondérer.
    #[test]
    fn une_issue_non_verifiable_fait_refuser_le_poids() {
        let mut h = Historique::nouveau();
        h.verifier(qui(2), Issue::Confirmee);
        h.verifier(qui(2), Issue::NonVerifiable);
        let e = h.poids(qui(2)).expect_err("le poids doit être refusé");
        assert!(e.contains("récompense la conformité"));
        assert_eq!(h.regime(qui(2)), Regime::NonVerifiable);
    }

    /// EX-M25 — le refus ne dépend pas de l'ordre des issues : une seule issue non
    /// vérifiable suffit, quelle que soit sa position.
    #[test]
    fn le_refus_ne_depend_pas_de_lordre_des_issues() {
        let mut h = Historique::nouveau();
        h.verifier(qui(3), Issue::NonVerifiable);
        h.verifier(qui(3), Issue::Confirmee);
        assert!(h.poids(qui(3)).is_err());
    }

    /// PD1 — les identités sont rendues dans l'ordre, jamais dans celui d'une table
    /// de hachage.
    #[test]
    fn les_identites_sont_rendues_dans_lordre() {
        let mut h = Historique::nouveau();
        h.asserter(qui(5));
        h.asserter(qui(1));
        h.asserter(qui(3));
        let ids: Vec<u32> = h.identites().map(|(i, _)| i.agent.0).collect();
        assert_eq!(ids, vec![1, 3, 5], "BTreeMap : itération ordonnée (PD1)");
    }

    /// EX-M25 — la consultation est comptée **même quand elle est refusée** : son
    /// prix est payé par le consultant, que la réponse lui serve ou non.
    #[test]
    fn la_consultation_est_comptee_meme_quand_elle_est_refusee() {
        let mut h = Historique::nouveau();
        h.verifier(qui(4), Issue::NonVerifiable);
        let _ = h.poids(qui(4));
        let _ = h.poids(qui(4));
        assert_eq!(h.consultations(), 2);
    }
}
