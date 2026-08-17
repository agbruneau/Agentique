//! **Algorithme 8.1 — dépôt aveugle sur sujet de délibération** (EX-A57, §8.2 du traité).
//!
//! ⚠ **Mécanisme proposé par l'ouvrage. Aucune source ne le mesure** ; ce qui
//! suit est un raisonnement de conception sur des garanties existantes, et
//! l'affichage doit le dire au même rang que le résultat.
//!
//! Modèle de panne : **P** (crash-arrêt, omission).
//! Hypothèse de synchronisme : **asynchrone pour la sûreté** ; partiellement
//! synchrone, borne Δ, pour toute borne de temps.
//! Hypothèses sur le milieu : **M1, M3, M4 sur une partition unique** du sujet de
//! délibération, plus l'identité apposée par le courtier (EX-M24).
//!
//! Le mécanisme est direct : chaque agent écrit ce qu'il détient en propre
//! **avant** de pouvoir lire ce que les autres ont écrit, la lecture n'étant
//! autorisée qu'au-delà de son propre décalage d'écriture. Le milieu n'a rien à
//! évaluer, il n'a qu'à ordonner — c'est M1 employée comme **contrainte de
//! protocole** et non comme garantie de lecture.
//!
//! **Coût** : 1 écriture et 1 lecture par agent et par tour, soit Θ(n) messages
//! par tour, contre Θ(n) également pour une délibération libre. Le mécanisme ne
//! coûte pas en messages, il coûte en **latence** : un tour de journal de plus.
//!
//! **Condition d'arrêt** : un budget de tours fixé d'avance et écrit dans le
//! sujet. Aucune stabilité ne sert de condition — c'est la stabilité prématurée
//! que le mécanisme combat, et un critère d'arrêt sur stabilité serait ici le
//! défaut et non l'optimisation (EX-A38).

use sim_core::ActeurId;
use std::collections::BTreeMap;

/// Provenance à afficher avec tout résultat de ce mécanisme (F2).
pub const PROVENANCE: &str =
    "mécanisme proposé par l'ouvrage (§8.2 du traité, algorithme 8.1) — aucune source ne le \
     mesure ; raisonnement de conception sur des garanties existantes";

/// Ce que le mécanisme ne protège pas (tableau 22, EX-V21).
pub const NE_PROTEGE_PAS: &str =
    "la réception : rien n'oblige un lecteur à peser une pièce unique plus qu'un chœur — c'est \
     l'objet de l'historique par identité (EX-M25)";

/// Refus opposé à qui voudrait arrêter la délibération sur une stabilité.
pub const REFUS_ARRET_SUR_STABILITE: &str =
    "aucune stabilité ne sert de condition d'arrêt : c'est la stabilité prématurée que le \
     mécanisme combat. Le budget de tours est fixé d'avance et écrit dans le sujet (EX-A57)";

/// Ce qu'un agent détient en propre au premier tour.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct FaitPrive {
    /// L'agent qui le détient.
    pub agent: ActeurId,
    /// La valeur détenue. `None` : l'agent ne détient **rien** en propre et écrit
    /// un fait vide — la fraction d'enregistrements vides est le signal à
    /// surveiller (mode (b)).
    pub valeur: Option<f64>,
}

/// Un enregistrement du sujet de délibération.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Depot {
    /// Auteur, apposé (EX-M24).
    pub agent: ActeurId,
    /// Tour de délibération.
    pub tour: u32,
    /// Ce qui a été déposé. `None` est un fait vide, et il est **écrit**, pas omis :
    /// un agent qui n'écrit rien serait indistinguable d'un agent lent.
    pub valeur: Option<f64>,
}

/// Mode de défaillance provocable (NF-10).
#[derive(Clone, Copy, Debug, PartialEq, Eq, Default)]
pub enum Mode {
    /// Nominal : la fenêtre est bornée par le temps, un absent n'est pas attendu.
    #[default]
    Nominal,
    /// Mode (a) — l'étape 3 attend la présence de **tous**. Un agent lent retarde
    /// alors toute la population, et c'est ce qu'il ne faut pas exiger.
    AttendreTousLesEcrivains,
}

/// Ce que le mécanisme rapporte d'un tour de délibération.
#[derive(Clone, Debug, PartialEq)]
pub struct Tour {
    /// Numéro du tour.
    pub numero: u32,
    /// Les dépôts lus, dans l'ordre de la partition (M1).
    pub depots: Vec<Depot>,
    /// Décision agrégée du tour : moyenne des valeurs non vides.
    ///
    /// `None` quand aucun agent ne détient de fait : le mécanisme n'invente pas
    /// de décision, et c'est ce que le mode (b) rend visible.
    pub decision: Option<f64>,
    /// Fraction d'enregistrements vides — **le signal du mode (b)**. Sous
    /// conformité forte, tous écrivent la même chose au tour 1, ce que le
    /// mécanisme rend visible sans le corriger.
    pub fraction_vide: f64,
    /// Vrai si un agent lent a fait attendre la population (mode (a)).
    pub bloque_par_un_lent: bool,
}

/// Une délibération sur un sujet dédié à une partition unique.
#[derive(Clone, Debug)]
pub struct DepotAveugle {
    /// Budget de tours, **fixé d'avance**.
    budget_tours: u32,
    mode: Mode,
    /// Décalage d'écriture de chaque agent au tour courant. La lecture n'est
    /// autorisée qu'au-delà : c'est la contrainte de protocole.
    decalage_ecriture: BTreeMap<ActeurId, u64>,
    journal: Vec<Depot>,
    tours_faits: u32,
    ecritures: u64,
    lectures: u64,
    tours_de_journal: u64,
}

impl DepotAveugle {
    /// Ouvre une délibération. Le budget est écrit ici et ne change plus.
    pub fn nouveau(budget_tours: u32, mode: Mode) -> DepotAveugle {
        DepotAveugle {
            budget_tours,
            mode,
            decalage_ecriture: BTreeMap::new(),
            journal: Vec::new(),
            tours_faits: 0,
            ecritures: 0,
            lectures: 0,
            tours_de_journal: 0,
        }
    }

    /// Exécute un tour, sur les faits privés de la population.
    ///
    /// L'ordre des étapes est le contrat, et il n'est pas réarrangeable :
    /// **tous** écrivent (étapes 1 et 2), **puis** chacun lit (étape 3). Une
    /// implantation qui laisserait un agent lire avant d'avoir écrit rendrait le
    /// mécanisme inopérant sans qu'aucun test de sortie ne le voie — d'où le
    /// contrôle explicite de [`DepotAveugle::a_ecrit_avant_de_lire`].
    ///
    /// `lents` : les agents qui n'ont pas encore écrit à l'ouverture de la
    /// fenêtre de lecture. Sous [`Mode::Nominal`] ils ne sont **pas attendus**.
    pub fn tour(&mut self, faits: &[FaitPrive], lents: &[ActeurId]) -> Option<Tour> {
        if self.tours_faits >= self.budget_tours {
            return None;
        }
        let numero = self.tours_faits + 1;

        // Étapes 1 et 2 — écrire, puis attendre l'accusé de durabilité (M3).
        // Un agent lent n'écrit pas dans la fenêtre.
        let debut = self.journal.len() as u64;
        for f in faits {
            if lents.contains(&f.agent) {
                continue;
            }
            self.journal.push(Depot {
                agent: f.agent,
                tour: numero,
                valeur: f.valeur,
            });
            self.decalage_ecriture
                .insert(f.agent, self.journal.len() as u64);
            self.ecritures += 1;
        }
        // Le tour de journal supplémentaire est ici, et il est compté à part du
        // compte de messages, qui ne bouge pas.
        self.tours_de_journal += 1;

        let bloque = !lents.is_empty() && self.mode == Mode::AttendreTousLesEcrivains;

        // Étape 3 — lire l'intervalle du tour, jamais avant l'étape 2.
        let depots: Vec<Depot> = self.journal[debut as usize..].to_vec();
        self.lectures += depots.len() as u64;
        self.tours_de_journal += 1;

        let valeurs: Vec<f64> = depots.iter().filter_map(|d| d.valeur).collect();
        let fraction_vide = if depots.is_empty() {
            1.0
        } else {
            1.0 - valeurs.len() as f64 / depots.len() as f64
        };
        let decision = if valeurs.is_empty() {
            None
        } else {
            Some(valeurs.iter().sum::<f64>() / valeurs.len() as f64)
        };

        self.tours_faits = numero;
        Some(Tour {
            numero,
            depots,
            decision,
            fraction_vide,
            bloque_par_un_lent: bloque,
        })
    }

    /// Cet agent a-t-il écrit avant que la lecture lui soit ouverte ?
    ///
    /// C'est la contrainte de protocole elle-même, exposée pour être testable :
    /// la lecture n'est autorisée qu'au-delà du décalage d'écriture de l'agent.
    pub fn a_ecrit_avant_de_lire(&self, agent: ActeurId) -> bool {
        self.decalage_ecriture.contains_key(&agent)
    }

    /// Budget de tours, tel qu'écrit dans le sujet.
    pub fn budget_tours(&self) -> u32 {
        self.budget_tours
    }

    /// Tours effectués.
    pub fn tours_faits(&self) -> u32 {
        self.tours_faits
    }

    /// Messages : 1 écriture et 1 lecture par agent et par tour, soit Θ(n) par
    /// tour — **autant** qu'une délibération libre.
    pub fn messages(&self) -> u64 {
        self.ecritures + self.lectures
    }

    /// Tours de journal consommés — c'est **ici** qu'est le prix : deux par tour
    /// de délibération, contre un pour une délibération libre.
    pub fn tours_de_journal(&self) -> u64 {
        self.tours_de_journal
    }

    /// Le surcoût, dans l'unité où il se paie.
    pub fn surcout(&self) -> String {
        format!(
            "{} messages et {} tours de journal pour {} tours de délibération — le mécanisme ne \
             coûte pas en messages, il coûte en latence : un tour de journal de plus par tour",
            self.messages(),
            self.tours_de_journal(),
            self.tours_faits
        )
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn faits(n: u32, valeurs: &[Option<f64>]) -> Vec<FaitPrive> {
        (0..n)
            .map(|a| FaitPrive {
                agent: ActeurId(a),
                valeur: valeurs[a as usize],
            })
            .collect()
    }

    #[test]
    fn chacun_ecrit_avant_de_pouvoir_lire() {
        let mut d = DepotAveugle::nouveau(1, Mode::Nominal);
        let f = faits(4, &[Some(1.0), Some(2.0), Some(3.0), Some(4.0)]);
        let t = d.tour(&f, &[]).expect("un tour dans le budget");
        assert_eq!(t.depots.len(), 4);
        for a in 0..4 {
            assert!(d.a_ecrit_avant_de_lire(ActeurId(a)));
        }
        assert_eq!(t.decision, Some(2.5));
    }

    #[test]
    fn le_prix_est_en_latence_et_non_en_messages() {
        let mut d = DepotAveugle::nouveau(3, Mode::Nominal);
        let f = faits(2, &[Some(1.0), Some(1.0)]);
        for _ in 0..3 {
            d.tour(&f, &[]).unwrap();
        }
        // 2 écritures + 2 lectures par tour, sur 3 tours.
        assert_eq!(d.messages(), 12);
        // 2 tours de journal par tour de délibération : c'est le surcoût.
        assert_eq!(d.tours_de_journal(), 6);
        assert!(d.surcout().contains("il coûte en latence"));
    }

    #[test]
    fn le_budget_de_tours_est_la_seule_condition_darret() {
        let mut d = DepotAveugle::nouveau(2, Mode::Nominal);
        let f = faits(2, &[Some(5.0), Some(5.0)]);
        assert!(d.tour(&f, &[]).is_some());
        assert!(d.tour(&f, &[]).is_some());
        assert!(
            d.tour(&f, &[]).is_none(),
            "au-delà du budget, plus de tour — et jamais d'arrêt sur stabilité"
        );
        assert_eq!(d.tours_faits(), 2);
        assert_eq!(d.budget_tours(), 2);
    }

    #[test]
    fn mode_b_la_fraction_vide_est_le_signal_et_nest_pas_corrigee() {
        let mut d = DepotAveugle::nouveau(1, Mode::Nominal);
        let f = faits(4, &[None, None, None, Some(9.0)]);
        let t = d.tour(&f, &[]).unwrap();
        assert_eq!(t.fraction_vide, 0.75);
        // Le mécanisme rend la décision du seul agent qui détient un fait : il
        // rend le vide **visible**, il ne le comble pas.
        assert_eq!(t.decision, Some(9.0));
    }

    #[test]
    fn mode_b_aucun_fait_prive_ne_produit_aucune_decision() {
        let mut d = DepotAveugle::nouveau(1, Mode::Nominal);
        let f = faits(3, &[None, None, None]);
        let t = d.tour(&f, &[]).unwrap();
        assert_eq!(t.fraction_vide, 1.0);
        assert_eq!(t.decision, None, "aucune décision n'est inventée");
    }

    #[test]
    fn mode_a_un_agent_lent_nest_pas_attendu_en_nominal() {
        let f = faits(3, &[Some(1.0), Some(2.0), Some(3.0)]);

        let mut nominal = DepotAveugle::nouveau(1, Mode::Nominal);
        let t = nominal.tour(&f, &[ActeurId(2)]).unwrap();
        assert!(!t.bloque_par_un_lent);
        assert_eq!(t.depots.len(), 2, "l'absent n'est pas attendu");

        let mut attend = DepotAveugle::nouveau(1, Mode::AttendreTousLesEcrivains);
        let t = attend.tour(&f, &[ActeurId(2)]).unwrap();
        assert!(
            t.bloque_par_un_lent,
            "le mode (a) fait retarder toute la population par un seul lent"
        );
    }

    #[test]
    fn la_provenance_dit_quaucune_source_ne_mesure_le_mecanisme() {
        assert!(PROVENANCE.contains("aucune source ne le mesure"));
        assert!(NE_PROTEGE_PAS.contains("réception"));
        assert!(REFUS_ARRET_SUR_STABILITE.contains("stabilité prématurée"));
    }
}
