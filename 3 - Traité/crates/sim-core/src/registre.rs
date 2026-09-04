//! Registre des hypothèses fortes (EX-C12, PD12).
//!
//! > Toute hypothèse plus forte que « Δ finie mais inconnue » est nommée à
//! > l'endroit où elle est prise. (§6.1 du traité)
//!
//! Le §6.1 du traité en fait sa règle d'ouverture : c'est cette hypothèse **qui casse en
//! premier sous charge**. Un temporisateur à borne connue n'est pas un réglage,
//! c'est une **affirmation** — « un suiveur sain rattrape le meneur en moins de
//! 30 s », « un agent sain répond en moins d'une seconde » — et le registre
//! compte le nombre de fois où elle a été fausse dans l'exécution en cours.
//!
//! Ce compteur est la seule chose qui distingue un modèle honnête d'un modèle
//! qui suppose ce qu'il devrait mesurer.

use crate::temps::Duree;
use std::collections::BTreeMap;

/// Une hypothèse forte déclarée.
#[derive(Clone, Debug)]
pub struct Hypothese {
    /// Nom du réglage qui l'encode, tel qu'il apparaît dans la documentation
    /// d'origine.
    pub reglage: &'static str,
    /// Valeur du temporisateur.
    pub valeur: Duree,
    /// Section du traité (F1, F2 : jamais un nombre sans provenance).
    pub source: &'static str,
    /// Ce que le réglage **affirme**, en toutes lettres.
    pub affirmation: &'static str,
    /// Nombre de fois où l'affirmation a été fausse dans l'exécution en cours.
    pub dementis: u64,
    /// Nombre de fois où elle a été mise à l'épreuve.
    pub epreuves: u64,
}

impl Hypothese {
    /// Fraction des épreuves où l'affirmation était fausse. `None` tant qu'elle
    /// n'a pas été éprouvée : F1 impose d'afficher l'absence, pas un zéro.
    pub fn taux_de_dementi(&self) -> Option<f64> {
        if self.epreuves == 0 {
            None
        } else {
            Some(self.dementis as f64 / self.epreuves as f64)
        }
    }
}

/// Le registre.
#[derive(Default, Debug, Clone)]
pub struct RegistreHypotheses {
    hypotheses: BTreeMap<&'static str, Hypothese>,
}

impl RegistreHypotheses {
    /// Registre vide.
    pub fn nouveau() -> Self {
        RegistreHypotheses::default()
    }

    /// Déclare une hypothèse. Un temporisateur à borne connue qui n'est pas
    /// déclaré ici est un réglage enfoui, et RQ7 dit ce qu'il coûte.
    pub fn declarer(
        &mut self,
        reglage: &'static str,
        valeur: Duree,
        source: &'static str,
        affirmation: &'static str,
    ) {
        self.hypotheses.insert(
            reglage,
            Hypothese {
                reglage,
                valeur,
                source,
                affirmation,
                dementis: 0,
                epreuves: 0,
            },
        );
    }

    /// Met l'affirmation à l'épreuve. `tenue` dit si elle s'est vérifiée.
    ///
    /// # Panics
    ///
    /// Si `reglage` n'a pas été déclaré. `assert!` et non `debug_assert!` : la
    /// suite de tests tourne en `--release`, où ce dernier disparaît. Un nom mal
    /// saisi laissait alors `dementis` et `epreuves` à zéro **sans rien dire** —
    /// c'est-à-dire un modèle qui suppose, affiché comme un modèle éprouvé,
    /// exactement ce que ce registre existe pour empêcher (EX-C12).
    pub fn eprouver(&mut self, reglage: &str, tenue: bool) {
        let h = self
            .hypotheses
            .get_mut(reglage)
            .unwrap_or_else(|| panic!("hypothèse « {reglage} » éprouvée sans être déclarée"));
        h.epreuves += 1;
        if !tenue {
            h.dementis += 1;
        }
    }

    /// Une hypothèse par le nom du réglage qui l'encode.
    pub fn get(&self, reglage: &str) -> Option<&Hypothese> {
        self.hypotheses.get(reglage)
    }

    /// Toutes les hypothèses déclarées, dans l'ordre des noms de réglage.
    /// L'ordre est stable — un `BTreeMap`, pas une table de hachage (PD1).
    pub fn toutes(&self) -> impl Iterator<Item = &Hypothese> {
        self.hypotheses.values()
    }

    /// Les hypothèses démenties au moins une fois. Ce sont celles qui ont
    /// cassé sous charge, et NF-16 exige qu'un test les rende fausses
    /// délibérément.
    pub fn dementies(&self) -> Vec<&Hypothese> {
        self.hypotheses
            .values()
            .filter(|h| h.dementis > 0)
            .collect()
    }

    /// Affichage (EX-C12 : le registre est affiché, chaque entrée avec son
    /// compteur).
    pub fn resume(&self, unite: &str) -> Vec<String> {
        self.hypotheses
            .values()
            .map(|h| {
                let compteur = match h.taux_de_dementi() {
                    Some(t) => format!(
                        "fausse {} fois sur {} ({:.1} %)",
                        h.dementis,
                        h.epreuves,
                        t * 100.0
                    ),
                    None => "jamais éprouvée".to_string(),
                };
                format!(
                    "{} = {} {unite} — « {} » ({}) : {compteur}",
                    h.reglage, h.valeur.0, h.affirmation, h.source
                )
            })
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn registre() -> RegistreHypotheses {
        let mut r = RegistreHypotheses::nouveau();
        r.declarer(
            "replica.lag.time.max.ms",
            Duree(30_000),
            "§6.1",
            "un suiveur sain rattrape le meneur en moins de 30 s",
        );
        r
    }

    /// EX-C12 — l'entrée porte sa valeur, sa source et l'affirmation qu'elle
    /// encode. Un temporisateur sans affirmation ne se déclare pas.
    #[test]
    fn une_hypothese_porte_son_affirmation_et_sa_source() {
        let r = registre();
        let h = r.get("replica.lag.time.max.ms").unwrap();
        assert_eq!(h.valeur, Duree(30_000));
        assert!(h.affirmation.contains("30 s"));
        assert_eq!(h.source, "§6.1");
    }

    /// F1 — tant qu'elle n'a pas été éprouvée, l'absence de mesure s'affiche.
    #[test]
    fn une_hypothese_non_eprouvee_na_pas_de_taux() {
        assert_eq!(
            registre()
                .get("replica.lag.time.max.ms")
                .unwrap()
                .taux_de_dementi(),
            None
        );
        assert!(registre().resume("ms")[0].contains("jamais éprouvée"));
    }

    /// Le compteur de démentis est ce qui rend l'hypothèse vérifiable au lieu
    /// d'être supposée.
    #[test]
    fn le_compteur_de_dementis_compte() {
        let mut r = registre();
        for tenue in [true, true, false, true, false] {
            r.eprouver("replica.lag.time.max.ms", tenue);
        }
        let h = r.get("replica.lag.time.max.ms").unwrap();
        assert_eq!(h.epreuves, 5);
        assert_eq!(h.dementis, 2);
        assert_eq!(h.taux_de_dementi(), Some(0.4));
        assert_eq!(r.dementies().len(), 1);
    }

    #[test]
    fn une_hypothese_toujours_tenue_nest_pas_dementie() {
        let mut r = registre();
        r.eprouver("replica.lag.time.max.ms", true);
        assert!(r.dementies().is_empty());
    }
}
