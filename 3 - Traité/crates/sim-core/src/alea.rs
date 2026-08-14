//! Source d'aléa unique et semée (PD1).
//!
//! Toute valeur aléatoire du monde clos sort d'ici. Il n'y a qu'un générateur
//! par exécution : l'ordre des tirages est donc l'ordre de consommation des
//! événements, et le rejeu à graine égale redonne la même suite.
//!
//! Les transcendantes passent par `libm` et non par les méthodes de `f64`
//! (DT1, banc `bancs/dt1-flottant`) : sans cela, une latence exponentielle
//! tirée en natif et en WASM diffère dès le premier tirage.

use rand_chacha::ChaCha8Rng;
use rand_core::{RngCore, SeedableRng};

/// Le générateur du monde clos.
pub struct Alea {
    rng: ChaCha8Rng,
    graine: u64,
    /// Nombre de tirages consommés. Affiché avec la trace : deux exécutions
    /// qui divergent le font souvent d'abord sur ce compteur.
    tirages: u64,
}

impl Alea {
    /// Générateur semé. `ChaCha8Rng` est spécifié bit à bit : la même graine
    /// donne la même suite en natif et en WASM, ce qui est la condition de
    /// NF-02 sur les chemins qui consomment de l'aléa.
    pub fn nouveau(graine: u64) -> Self {
        Alea {
            rng: ChaCha8Rng::seed_from_u64(graine),
            graine,
            tirages: 0,
        }
    }

    /// La graine, à journaliser avec la configuration (§3.3, étape 1).
    pub fn graine(&self) -> u64 {
        self.graine
    }

    /// Nombre de tirages consommés. Deux exécutions qui divergent le font
    /// souvent d'abord sur ce compteur, ce qui en fait un point de comparaison
    /// plus utile que la trace elle-même.
    pub fn tirages(&self) -> u64 {
        self.tirages
    }

    /// 64 bits bruts.
    pub fn bits(&mut self) -> u64 {
        self.tirages += 1;
        self.rng.next_u64()
    }

    /// Uniforme sur [0, 1).
    ///
    /// 53 bits de mantisse, mis à l'échelle par une puissance de deux : la
    /// multiplication est exacte en IEEE-754, donc identique sur les deux
    /// cibles (groupe « base » du banc DT1).
    pub fn uniforme(&mut self) -> f64 {
        (self.bits() >> 11) as f64 * (1.0 / (1u64 << 53) as f64)
    }

    /// Entier uniforme sur [0, n). Rend 0 si n vaut 0.
    ///
    /// Méthode de Lemire : un produit large, sans boucle de rejet ni modulo.
    /// Le biais résiduel est de l'ordre de 2⁻⁶⁴ et ne dépend pas de la cible.
    pub fn entier(&mut self, n: u64) -> u64 {
        if n == 0 {
            return 0;
        }
        ((self.bits() as u128 * n as u128) >> 64) as u64
    }

    /// Tire vrai avec la probabilité `p`. Hors de [0, 1], `p` est ramené aux
    /// bornes : un taux mal saisi ne doit pas produire un comportement inversé.
    pub fn bernoulli(&mut self, p: f64) -> bool {
        self.uniforme() < p.clamp(0.0, 1.0)
    }

    /// Loi exponentielle de moyenne `moyenne`, en unités de l'appelant.
    ///
    /// `1 − u` est dans (0, 1] : le logarithme n'est jamais pris en zéro.
    pub fn exponentielle(&mut self, moyenne: f64) -> f64 {
        -libm::log(1.0 - self.uniforme()) * moyenne
    }

    /// Tirage pondéré sur un vecteur de poids positifs. Rend l'indice tiré, ou
    /// `None` si tous les poids sont nuls — cas que l'appelant doit traiter et
    /// non masquer : c'est le régime où la trace stigmergique s'est effondrée.
    ///
    /// L'ordre du vecteur est significatif : c'est lui qui rend le tirage
    /// reproductible, et il ne doit jamais venir d'une table de hachage (PD1).
    pub fn pondere(&mut self, poids: &[f64]) -> Option<usize> {
        let u = self.uniforme();
        Self::pondere_avec(poids, u)
    }

    /// Même tirage pondéré, à partir d'un uniforme **déjà tiré**.
    ///
    /// Existe pour EX-C19 : les membres d'une même famille de décision
    /// partagent leur uniforme, et le partage se fait dans
    /// [`crate::famille::TirageDeDecision`], pas ici. `Alea` reste la source
    /// unique — cette fonction n'en est pas une, elle ne tire rien.
    pub fn pondere_avec(poids: &[f64], u: f64) -> Option<usize> {
        let total: f64 = poids.iter().sum();
        // La négation est délibérée et ne se remplace pas par `total <= 0.0` :
        // elle attrape aussi le NaN, qu'un poids mal calculé peut produire. Un
        // NaN qui passerait le contrôle ferait échouer tous les tests de la
        // boucle de tirage et rendrait `None` par la porte de sortie, ce qui
        // masquerait la cause.
        #[allow(clippy::neg_cmp_op_on_partial_ord)]
        if !(total > 0.0) {
            return None;
        }
        let seuil = u * total;
        let mut cumul = 0.0;
        for (i, p) in poids.iter().enumerate() {
            cumul += p;
            if seuil < cumul {
                return Some(i);
            }
        }
        // Atteignable seulement par arrondi quand `seuil` frôle `total`.
        Some(poids.len() - 1)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-C02 : même graine, même suite. C'est la propriété qui porte tout le
    /// reste ; si elle tombe, aucun rejeu ne tient.
    #[test]
    fn meme_graine_meme_suite() {
        let mut a = Alea::nouveau(42);
        let mut b = Alea::nouveau(42);
        for _ in 0..1_000 {
            assert_eq!(a.bits(), b.bits());
        }
        assert_eq!(a.tirages(), b.tirages());
    }

    #[test]
    fn graines_distinctes_suites_distinctes() {
        let mut a = Alea::nouveau(1);
        let mut b = Alea::nouveau(2);
        assert_ne!(a.bits(), b.bits());
    }

    #[test]
    fn uniforme_reste_dans_son_intervalle() {
        let mut a = Alea::nouveau(7);
        for _ in 0..10_000 {
            let u = a.uniforme();
            assert!((0.0..1.0).contains(&u), "u = {u}");
        }
    }

    #[test]
    fn entier_reste_dans_sa_borne() {
        let mut a = Alea::nouveau(9);
        for _ in 0..10_000 {
            assert!(a.entier(7) < 7);
        }
        assert_eq!(a.entier(0), 0);
    }

    #[test]
    fn pondere_refuse_les_poids_nuls() {
        let mut a = Alea::nouveau(3);
        assert_eq!(a.pondere(&[0.0, 0.0]), None);
        assert_eq!(a.pondere(&[0.0, 1.0]), Some(1));
    }

    /// Le tirage pondéré doit suivre les poids : sans cela le scénario B
    /// mesurerait un plancher d'exploration qui ne vient pas de la trace.
    #[test]
    fn pondere_suit_les_poids() {
        let mut a = Alea::nouveau(11);
        let mut comptes = [0u32; 3];
        for _ in 0..30_000 {
            comptes[a.pondere(&[1.0, 2.0, 7.0]).unwrap()] += 1;
        }
        assert!((2_500..3_500).contains(&comptes[0]), "{comptes:?}");
        assert!((5_500..6_500).contains(&comptes[1]), "{comptes:?}");
        assert!((20_000..22_000).contains(&comptes[2]), "{comptes:?}");
    }
}
