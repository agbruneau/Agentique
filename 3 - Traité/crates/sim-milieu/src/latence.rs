//! Latence du chemin écriture → accusé de durabilité → lecture (EX-M09).
//!
//! **Un seul segment de ce chemin est tiré** : écriture → accusé. C'est lui qui
//! décide de l'instant où l'enregistrement devient lisible, et le reste du
//! chemin ne coûte aucun tic — [`crate::journal::Milieu::lire`] rend
//! immédiatement, à la date logique de l'appelant. Le ℓ₉₉ affiché est donc celui
//! de la durabilité, pas celui d'un aller-retour de lecture.
//!
//! Deux règles du PRD tiennent ici, et elles se distinguent :
//!
//! - **EX-M09** — la latence est tirée d'une distribution paramétrable, et
//!   **ℓ₉₉ en est extrait et affiché, jamais la moyenne seule**.
//! - **§8.3 du PRD** — ce ℓ₉₉ est une **entrée** du modèle, pas une sortie. Le
//!   ℓ₉₉ de réponse d'un agent, lui, **est** une sortie, produite par la file et
//!   le temps de service : `sim_core::service::Service::l99_de_reponse`. Les deux
//!   portent des libellés distincts dans toute l'interface, et un affichage qui
//!   les mêlerait est un défaut bloquant.

use sim_core::alea::Alea;
use sim_core::temps::{Duree, Granularite};
use serde::{Deserialize, Serialize};

/// Le quantile à 99 % d'une exponentielle vaut sa moyenne fois ln(100).
/// `libm::log` et non `f64::ln` : le banc DT1 mesure que la seconde diverge
/// entre natif et WASM.
fn facteur_l99() -> f64 {
    libm::log(100.0)
}

/// Distribution de la latence du milieu, **paramétrée par son ℓ₉₉**.
///
/// Régler la moyenne serait exposer la grandeur que le traité refuse d'afficher
/// seule ; régler ℓ₉₉ met le percentile au premier plan, là où le §2.3 et le
/// §6.2 du traité le placent.
#[derive(Clone, Copy, Debug, Serialize, Deserialize)]
pub struct Latence {
    /// ℓ₉₉ visé, en millisecondes. **Entrée du modèle** (§8.3 du PRD).
    pub l99_ms: f64,
    /// Plancher incompressible, en millisecondes.
    pub plancher_ms: f64,
}

impl Latence {
    /// Distribution exponentielle de ℓ₉₉ donné, sans plancher.
    pub fn depuis_l99(l99_ms: f64) -> Latence {
        Latence {
            l99_ms,
            plancher_ms: 0.0,
        }
    }

    /// Latence déterministe — utile aux scénarios qui veulent isoler une autre
    /// cause. Ce n'est pas un défaut : c'est un régime, et il est nommé.
    pub fn fixe(ms: f64) -> Latence {
        Latence {
            l99_ms: ms,
            plancher_ms: ms,
        }
    }

    fn moyenne_ms(&self) -> f64 {
        ((self.l99_ms - self.plancher_ms) / facteur_l99()).max(0.0)
    }

    /// Tire une latence, en tics de la granularité courante.
    ///
    /// # Panics
    ///
    /// Si le tirage ne donne pas un nombre de millisecondes fini et positif —
    /// `Granularite::tics_depuis_ms` l'exige et le dit. Le cas se produit sur un
    /// réglage négatif ou non fini, que la désérialisation d'un scénario peut
    /// livrer sans passer par [`Latence::depuis_l99`] ni [`Latence::fixe`]. Le
    /// silence serait pire : un NaN converti donnerait `Duree(0)`, donc un
    /// accusé de durabilité **immédiat**, et M3 cesserait d'avoir un prix.
    pub fn tirer(&self, alea: &mut Alea, g: Granularite) -> Duree {
        let m = self.moyenne_ms();
        let ms = if m <= 0.0 {
            self.plancher_ms
        } else {
            self.plancher_ms + alea.exponentielle(m)
        };
        g.tics_depuis_ms(ms)
    }
}

/// Accumulateur de latences mesurées, pour extraire les percentiles.
///
// ponytail: vecteur trié à la demande, O(n log n) par lecture de percentile et
// O(n) en mémoire. À n = 10⁶ mesures c'est 8 Mo et quelques millisecondes, donc
// sans objet ici. Passer à un t-digest ou à un histogramme à godets
// logarithmiques si une campagne veut garder toutes les latences de toutes les
// exécutions.
#[derive(Clone, Debug, Default)]
pub struct Mesures {
    valeurs: Vec<u64>,
}

impl Mesures {
    /// Accumulateur vide.
    pub fn nouvelle() -> Mesures {
        Mesures::default()
    }

    /// Enregistre une mesure.
    pub fn ajouter(&mut self, d: Duree) {
        self.valeurs.push(d.0);
    }

    /// Nombre de mesures accumulées — le dénominateur de tout percentile.
    pub fn compte(&self) -> usize {
        self.valeurs.len()
    }

    /// Percentile mesuré, en tics. `None` s'il n'y a rien à mesurer : F1
    /// impose d'**afficher l'absence** plutôt que de combler par un zéro.
    pub fn percentile(&self, p: f64) -> Option<Duree> {
        if self.valeurs.is_empty() {
            return None;
        }
        let mut tri = self.valeurs.clone();
        tri.sort_unstable();
        // Rang par la méthode du plus proche, borné au dernier indice.
        let rang = ((p * tri.len() as f64).ceil() as usize).saturating_sub(1);
        Some(Duree(tri[rang.min(tri.len() - 1)]))
    }

    /// ℓ₉₉ mesuré. Selon l'objet mesuré, c'est une **entrée** du modèle (chemin
    /// de durabilité du milieu) ou une **sortie** (réponse d'un agent) — et les
    /// deux ne portent jamais le même libellé (§8.3 du PRD).
    pub fn l99(&self) -> Option<Duree> {
        self.percentile(0.99)
    }

    /// Moyenne mesurée. **Privée d'accès direct** : EX-M09 interdit d'afficher
    /// la moyenne seule, et EX-V06 exige qu'elle soit accompagnée de sa queue.
    /// Le seul chemin public est [`Mesures::moyenne_et_queue`].
    fn moyenne(&self) -> Option<f64> {
        if self.valeurs.is_empty() {
            return None;
        }
        Some(self.valeurs.iter().sum::<u64>() as f64 / self.valeurs.len() as f64)
    }

    /// Moyenne **avec** sa queue (EX-M09, EX-V06). Il n'existe pas d'accesseur
    /// qui rende la moyenne seule : la règle est tenue par le type, pas par la
    /// discipline de l'appelant.
    pub fn moyenne_et_queue(&self) -> Option<(f64, Duree, Duree)> {
        Some((
            self.moyenne()?,
            self.percentile(0.99)?,
            self.percentile(0.999)?,
        ))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-M09 — le ℓ₉₉ mesuré doit retrouver le ℓ₉₉ demandé. Sans cela, le
    /// paramètre affiché ne serait pas celui que le modèle applique.
    #[test]
    fn le_l99_mesure_retrouve_le_l99_demande() {
        let l = Latence::depuis_l99(20.0);
        let mut alea = Alea::nouveau(1);
        let mut m = Mesures::nouvelle();
        for _ in 0..200_000 {
            m.ajouter(l.tirer(&mut alea, Granularite::Micro));
        }
        let mesure_ms = Granularite::Micro.ms_depuis_tics(m.l99().unwrap());
        assert!(
            (mesure_ms - 20.0).abs() < 1.0,
            "ℓ₉₉ mesuré {mesure_ms:.2} ms pour 20 ms demandées"
        );
    }

    #[test]
    fn une_latence_fixe_ne_varie_pas() {
        let l = Latence::fixe(5.0);
        let mut alea = Alea::nouveau(2);
        let a = l.tirer(&mut alea, Granularite::Micro);
        let b = l.tirer(&mut alea, Granularite::Micro);
        assert_eq!(a, b);
        assert_eq!(a, Duree(5_000));
    }

    /// F1 — l'absence de mesure s'affiche, elle ne se comble pas.
    #[test]
    fn sans_mesure_il_ny_a_pas_de_percentile() {
        let m = Mesures::nouvelle();
        assert_eq!(m.l99(), None);
        assert_eq!(m.moyenne_et_queue(), None);
    }

    #[test]
    fn la_moyenne_ne_sobtient_quaccompagnee_de_sa_queue() {
        let mut m = Mesures::nouvelle();
        for i in 1..=100u64 {
            m.ajouter(Duree(i));
        }
        let (moyenne, l99, l999) = m.moyenne_et_queue().unwrap();
        assert!((moyenne - 50.5).abs() < 0.01);
        assert_eq!(l99, Duree(99));
        assert_eq!(l999, Duree(100));
    }
}
