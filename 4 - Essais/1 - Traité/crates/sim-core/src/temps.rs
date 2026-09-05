//! Horloge logique. Elle n'avance que par consommation d'événements (PD1) et
//! ne consulte jamais l'horloge du système.

use serde::{Deserialize, Serialize};
use std::ops::{Add, Sub};

/// EX-C04 — la granularité est un **paramètre du modèle**, pas une constante :
/// elle décide de ce qui compte comme simultané, donc de ce que le départage de
/// la file (EX-C03) a à départager.
///
/// DT10 tranche « une granularité par scénario », journalisée et affichée. La
/// conséquence dure y est écrite : deux exécutions de granularités différentes
/// ne se comparent pas. Le hachage de configuration porte la granularité, ce qui
/// rend la comparaison impossible sans qu'on ait à l'interdire séparément.
#[derive(Clone, Copy, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub enum Granularite {
    /// Un tic vaut 1 µs. Résolution de l'aller-retour du §4.3 ; le scénario D
    /// l'exige.
    Micro,
    /// Un tic vaut 1 ms. Le scénario J couvre des minutes et ne tiendrait pas
    /// en microsecondes à un coût de campagne acceptable.
    Milli,
}

impl Granularite {
    /// Nombre de nanosecondes que vaut un tic. Sert l'affichage seul : aucune
    /// décision d'ordonnancement ne passe par cette conversion.
    pub fn nanosecondes(self) -> u64 {
        match self {
            Granularite::Micro => 1_000,
            Granularite::Milli => 1_000_000,
        }
    }

    /// Libellé affiché (EX-C04, F1 : toute grandeur porte son unité).
    pub fn unite(self) -> &'static str {
        match self {
            Granularite::Micro => "µs",
            Granularite::Milli => "ms",
        }
    }

    /// Convertit une durée exprimée en millisecondes réelles vers des tics.
    /// Arrondi au tic supérieur : une latence de 20 ms ne doit jamais devenir
    /// nulle parce que la granularité est grossière.
    ///
    /// # Panics
    ///
    /// Si `ms` n'est pas un nombre fini positif ou nul. Le cast `as u64` de Rust
    /// est saturant : sans cette garde, un NaN — produit par une division par
    /// zéro en amont — devient `Duree(0)`, c'est-à-dire « immédiat », soit
    /// exactement le cas que la règle d'arrondi ci-dessus existe pour empêcher.
    /// Un infini devient `u64::MAX`, qui ramène ensuite l'événement à l'instant
    /// courant par saturation. Les deux se taisent ; il vaut mieux qu'ils
    /// parlent.
    pub fn tics_depuis_ms(self, ms: f64) -> Duree {
        assert!(
            ms.is_finite() && ms >= 0.0,
            "durée non convertible en tics : {ms} ms"
        );
        let par_ms = 1_000_000.0 / self.nanosecondes() as f64;
        let tics = (ms * par_ms).ceil();
        // Le cast `as u64` sature en silence : sans cette garde, 1e30 ms rend
        // `u64::MAX`, et l'horloge poussée là ne redescend plus — la boucle
        // d'évaluation des fautes tourne alors sans fin, parce que
        // `prochaine_evaluation + pas` sature à son tour.
        assert!(
            tics < u64::MAX as f64,
            "durée hors domaine : {ms} ms vaut {tics} tics à cette granularité"
        );
        Duree(tics as u64)
    }

    /// Réciproque, pour l'affichage.
    pub fn ms_depuis_tics(self, d: Duree) -> f64 {
        d.0 as f64 * self.nanosecondes() as f64 / 1_000_000.0
    }
}

/// Date en temps logique, comptée en tics de la granularité courante.
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Debug, Default, Serialize, Deserialize)]
pub struct Instant(pub u64);

/// Durée en tics.
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Debug, Default, Serialize, Deserialize)]
pub struct Duree(pub u64);

impl Add<Duree> for Instant {
    type Output = Instant;
    /// Saturant, comme la soustraction. Un enroulement ferait **reculer**
    /// l'horloge, ce que `Moteur::maintenant` déclare impossible ; et le profil
    /// release du dépôt ne pose pas `overflow-checks`, donc il serait silencieux.
    fn add(self, d: Duree) -> Instant {
        Instant(self.0.saturating_add(d.0))
    }
}

impl Sub for Instant {
    type Output = Duree;
    /// Écart entre deux dates. Saturant : une date antérieure rend une durée
    /// nulle plutôt qu'un débordement silencieux.
    fn sub(self, autre: Instant) -> Duree {
        Duree(self.0.saturating_sub(autre.0))
    }
}

impl Add for Duree {
    type Output = Duree;
    /// Saturant, même motif : une somme de délais enroulée rendrait un délai
    /// nul, donc un événement immédiat.
    fn add(self, autre: Duree) -> Duree {
        Duree(self.0.saturating_add(autre.0))
    }
}
