//! **§6.2** — reconstruction causale hors ligne (EX-A08, EX-M20).
//!
//! `ANCÊTRES(e, H)` remonte la chaîne des causes d'un événement dans un horizon
//! `H`. Ce que le mécanisme doit dire, et que la plupart des implantations
//! taisent : **quand la chaîne a été coupée**.
//!
//! L'horizon réel n'est pas celui qu'on demande — c'est la rétention `R` du
//! milieu (EX-M20). Au-delà, la propriété redevient invérifiable, et le drapeau
//! de troncature est la seule chose honnête à afficher.

use sim_core::temps::{Duree, Instant};

/// Un événement du journal, avec ses causes directes.
#[derive(Clone, Debug)]
pub struct Evenement {
    /// Identifiant de l'événement.
    pub id: u64,
    /// Date d'écriture dans le journal.
    pub date: Instant,
    /// Causes directes, par identifiant.
    pub causes: Vec<u64>,
}

/// Le résultat d'une reconstruction.
#[derive(Clone, Debug)]
pub struct Ancetres {
    /// Identifiants trouvés, ordonnés.
    pub trouves: Vec<u64>,
    /// **Drapeau de troncature** : vrai si la chaîne a été coupée, soit par
    /// l'horizon demandé, soit par la rétention.
    pub tronque: bool,
    /// Ce qui a coupé la chaîne. `None` si elle est complète.
    pub cause_de_troncature: Option<&'static str>,
    /// Taux d'échantillonnage qui a produit le journal, quand il y en a un.
    ///
    /// Composé avec EX-A35 : une chaîne reconstruite depuis un journal
    /// échantillonné porte le drapeau **et** le taux.
    pub taux_dechantillonnage: Option<f64>,
}

impl Ancetres {
    /// Affichage (EX-A08). Un résultat tronqué le dit ; il ne se présente
    /// jamais comme complet.
    pub fn affichage(&self) -> String {
        let base = format!("{} ancêtre(s) reconstruit(s)", self.trouves.len());
        match (self.tronque, self.taux_dechantillonnage) {
            (false, None) => format!("{base} — chaîne complète"),
            (false, Some(t)) => format!(
                "{base} — chaîne complète **dans le journal échantillonné au taux 1/{:.0}**",
                1.0 / t
            ),
            (true, None) => format!(
                "{base} — **TRONQUÉE** : {}",
                self.cause_de_troncature.unwrap_or("cause inconnue")
            ),
            (true, Some(t)) => format!(
                "{base} — **TRONQUÉE** : {} ; journal échantillonné au taux 1/{:.0}, ce qui \
                 compose deux causes d'incomplétude",
                self.cause_de_troncature.unwrap_or("cause inconnue"),
                1.0 / t
            ),
        }
    }
}

/// `ANCÊTRES(e, H)` — remonte la chaîne des causes.
///
/// `retention` borne l'horizon **réel** : au-delà, les événements ont disparu du
/// milieu, quelle que soit la profondeur demandée.
pub fn ancetres(
    journal: &[Evenement],
    depart: u64,
    horizon: Duree,
    maintenant: Instant,
    retention: Option<Duree>,
    taux_dechantillonnage: Option<f64>,
) -> Ancetres {
    let limite_horizon = Instant(maintenant.0.saturating_sub(horizon.0));
    let limite_retention = retention.map(|r| Instant(maintenant.0.saturating_sub(r.0)));

    let mut trouves = Vec::new();
    let mut pile = vec![depart];
    let mut tronque = false;
    let mut cause: Option<&'static str> = None;

    while let Some(id) = pile.pop() {
        let e = match journal.iter().find(|e| e.id == id) {
            Some(e) => e,
            None => {
                // L'événement n'est plus dans le journal : la rétention l'a
                // évaporé.
                tronque = true;
                cause = Some(
                    "l'événement a quitté le journal : au-delà de R, la propriété redevient \
                     invérifiable ; R, non la sensibilité du détecteur, est l'horizon réel \
                     (§6.1, §7.2, EX-M20)",
                );
                continue;
            }
        };
        if let Some(limite) = limite_retention {
            if e.date < limite {
                tronque = true;
                cause = Some("horizon de rétention R atteint");
                continue;
            }
        }
        if e.date < limite_horizon {
            tronque = true;
            cause = Some("horizon H demandé atteint");
            continue;
        }
        if !trouves.contains(&id) {
            trouves.push(id);
            for c in &e.causes {
                pile.push(*c);
            }
        }
    }
    trouves.sort_unstable();

    Ancetres {
        trouves,
        tronque,
        cause_de_troncature: cause,
        taux_dechantillonnage,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn journal() -> Vec<Evenement> {
        // Chaîne e0 ← e1 ← e2 ← e3, espacée de 100 tics.
        (0..4u64)
            .map(|i| Evenement {
                id: i,
                date: Instant(i * 100),
                causes: if i == 0 { vec![] } else { vec![i - 1] },
            })
            .collect()
    }

    /// EX-A08 — une chaîne complète le dit, et son drapeau reste baissé.
    #[test]
    fn une_chaine_complete_ne_porte_pas_le_drapeau() {
        let a = ancetres(&journal(), 3, Duree(1_000), Instant(300), None, None);
        assert_eq!(a.trouves, vec![0, 1, 2, 3]);
        assert!(!a.tronque);
        assert!(a.affichage().contains("complète"));
    }

    /// EX-A08 — l'horizon demandé coupe la chaîne, et le drapeau se lève.
    #[test]
    fn lhorizon_demande_tronque_et_le_drapeau_se_leve() {
        let a = ancetres(&journal(), 3, Duree(150), Instant(300), None, None);
        assert!(a.tronque);
        assert!(a.trouves.len() < 4);
        assert!(a.affichage().contains("TRONQUÉE"));
        assert!(a.cause_de_troncature.unwrap().contains("horizon H"));
    }

    /// **EX-M20** — la rétention borne l'horizon **réel**, quelle que soit la
    /// profondeur demandée. C'est R, non la sensibilité du détecteur, qui
    /// décide.
    #[test]
    fn la_retention_borne_lhorizon_reel() {
        // On demande tout l'historique, mais R ne remonte que 150 tics.
        let a = ancetres(
            &journal(),
            3,
            Duree(100_000),
            Instant(300),
            Some(Duree(150)),
            None,
        );
        assert!(a.tronque, "la rétention coupe malgré l'horizon demandé");
        assert!(a.cause_de_troncature.unwrap().contains("rétention"));
    }

    /// Composé avec EX-A35 : la chaîne porte le drapeau **et** le taux
    /// d'échantillonnage qui l'a produite.
    #[test]
    fn une_chaine_echantillonnee_porte_son_taux() {
        let a = ancetres(
            &journal(),
            3,
            Duree(1_000),
            Instant(300),
            None,
            Some(1.0 / 1024.0),
        );
        assert!(a.affichage().contains("1/1024"), "{}", a.affichage());

        let tronquee = ancetres(
            &journal(),
            3,
            Duree(150),
            Instant(300),
            None,
            Some(1.0 / 1024.0),
        );
        assert!(tronquee.affichage().contains("deux causes d'incomplétude"));
    }

    /// Un événement absent du journal est une troncature, pas un silence.
    #[test]
    fn un_evenement_evapore_est_une_troncature() {
        let partiel = vec![Evenement {
            id: 3,
            date: Instant(300),
            causes: vec![2],
        }];
        let a = ancetres(&partiel, 3, Duree(100_000), Instant(300), None, None);
        assert!(a.tronque);
        assert!(a.cause_de_troncature.unwrap().contains("invérifiable"));
    }
}
