//! La définition d'essaim, et sa garde (EX-A12).
//!
//! > La perception d'un agent se factorise par un voisinage de cardinal borné
//! > ou par un intervalle borné du milieu. (§1.1)
//!
//! Un agent dont la perception prendrait la configuration entière n'est pas un
//! membre de l'essaim : c'est un coordonnateur. Le simulateur le refuse **à la
//! construction**, et non à l'exécution — une perception globale ne se corrige
//! pas en cours de route, elle invalide tout ce que l'exécution mesure.
//!
//! Le refus n'interdit pas les coordonnateurs. Il interdit qu'un coordonnateur
//! soit compté comme membre de l'essaim : le scénario F l'instancie
//! explicitement et séparément, le coordonnateur de groupe (T1) et l'autorité
//! d'admission (PD11) suivent la même règle.

/// Ce qu'un agent perçoit.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Perception {
    /// Voisinage de cardinal borné — la forme du ch. 1 (alignement) et du ch. 5.
    Voisinage {
        /// Nombre maximal de voisins. La borne doit être **indépendante de n**,
        /// sinon ce n'est plus un essaim — condition que
        /// [`Membre::nouveau`] ne peut pas vérifier sur un appel isolé, et qui
        /// se tient donc à la lecture des scénarios.
        cardinal_max: u32,
    },
    /// Intervalle borné du milieu — la forme stigmergique : l'agent lit au plus
    /// `enregistrements_max` enregistrements par cycle.
    IntervalleMilieu {
        /// Plafond de lecture par cycle, **total** et non par partition.
        enregistrements_max: u32,
    },
}

/// Un membre validé de l'essaim. Le type ne se construit que par
/// [`Membre::nouveau`], donc l'existence d'une valeur atteste du contrôle.
#[derive(Clone, Copy, Debug)]
pub struct Membre {
    /// La perception validée de ce membre.
    pub perception: Perception,
}

/// Message de refus, repris mot pour mot d'EX-A12.
pub const REFUS: &str = "ce n'est pas un membre de l'essaim, c'est un coordonnateur";

impl Membre {
    /// Construit un membre, ou refuse.
    ///
    /// `population` est la taille de l'essaim ; `enregistrements_totaux` la
    /// taille du milieu visible, **`None` quand elle n'est pas bornée**. Une
    /// perception qui atteint l'une ou l'autre n'est plus bornée relativement à
    /// la configuration : c'est la vue globale.
    ///
    /// **Ce que cette garde n'établit pas.** Elle voit un appel, pas une
    /// famille d'appels : elle refuse un cardinal qui atteint `population`, mais
    /// pas un cardinal réglé à `population − 1`, qui croît pourtant avec n et
    /// n'est donc pas davantage une perception d'essaim. Et sur un milieu non
    /// borné (`None`), elle ne peut rien dire du tout — c'est le cas du scénario
    /// B. L'invariant « la borne est indépendante de n » se tient à la lecture
    /// des scénarios, pas ici.
    pub fn nouveau(
        perception: Perception,
        population: u32,
        enregistrements_totaux: Option<u64>,
    ) -> Result<Membre, String> {
        match (perception, enregistrements_totaux) {
            (Perception::Voisinage { cardinal_max }, _)
                if u64::from(cardinal_max) >= u64::from(population) =>
            {
                Err(format!(
                    "{REFUS} — voisinage de {cardinal_max} sur une population de {population} \
                     (§1.1)"
                ))
            }
            (
                Perception::IntervalleMilieu {
                    enregistrements_max,
                },
                Some(totaux),
            ) if u64::from(enregistrements_max) >= totaux && totaux > 0 => Err(format!(
                "{REFUS} — intervalle de {enregistrements_max} sur un milieu de \
                 {totaux} enregistrements (§1.1)"
            )),
            _ => Ok(Membre { perception }),
        }
    }

    /// Nombre d'enregistrements que ce membre a le droit de lire par cycle.
    pub fn intervalle_max(&self) -> usize {
        match self.perception {
            Perception::IntervalleMilieu {
                enregistrements_max,
            } => enregistrements_max as usize,
            Perception::Voisinage { cardinal_max } => cardinal_max as usize,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn un_voisinage_borne_est_un_membre() {
        assert!(Membre::nouveau(Perception::Voisinage { cardinal_max: 8 }, 64, None).is_ok());
    }

    /// EX-A12 — la vue globale est refusée, avec le message du traité.
    #[test]
    fn un_voisinage_qui_couvre_la_population_est_refuse() {
        let e = Membre::nouveau(Perception::Voisinage { cardinal_max: 64 }, 64, None).unwrap_err();
        assert!(e.contains("coordonnateur"), "{e}");
        assert!(e.contains("§1.1"), "{e}");
    }

    #[test]
    fn un_intervalle_qui_couvre_le_milieu_est_refuse() {
        let e = Membre::nouveau(
            Perception::IntervalleMilieu {
                enregistrements_max: 1_000,
            },
            64,
            Some(1_000),
        )
        .unwrap_err();
        assert!(e.contains("coordonnateur"), "{e}");
    }

    #[test]
    fn un_intervalle_borne_est_un_membre() {
        let m = Membre::nouveau(
            Perception::IntervalleMilieu {
                enregistrements_max: 32,
            },
            64,
            Some(1_000),
        )
        .unwrap();
        assert_eq!(m.intervalle_max(), 32);
    }
}
