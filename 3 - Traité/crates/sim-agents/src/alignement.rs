//! **Algorithme 1 du ch. 1** — alignement par règle de plus proche voisin
//! (EX-A02), sous les hypothèses exactes du traité.
//!
//! Hypothèses, affichées en permanence parce qu'elles sont l'inverse de celles
//! du reste du produit : **synchrone**, **bruit nul**, famille finie de graphes
//! de voisinage, voisinage connu au tour courant.
//!
//! Ce que ce mécanisme sert : l'accord de fait **sans protocole d'accord**.
//! Ce qu'il ne fournit pas, et qu'aucun affichage ne doit suggérer (PD5) : ni
//! paramètre d'ordre, ni transition de phase. Le traité écrit que le bruit nul
//! retire précisément la transition de phase ; Φ, η_c et β ≈ 0,45 appartiennent
//! au modèle de Vicsek **avec bruit** (§1.2, p. 12), qu'aucun mécanisme du
//! périmètre actuel ne fournit.

use sim_core::alea::Alea;
use sim_core::oracle::{Oracle, Registre};
use sim_core::temps::Instant;

/// Nom de l'oracle du critère local (PD10).
pub const ACCORD_LOCAL: &str = "EX-A02 — écart aux voisins ≤ ε pendant R tours";

/// Signature du mécanisme, affichée sans repli possible (EX-V07, PD8).
pub const SIGNATURE: &[(&str, &str)] = &[
    ("modèle de panne", "aucun — le mécanisme n'en tolère pas"),
    ("synchronisme", "synchrone, tours globaux"),
    ("bruit", "nul — et c'est le bruit nul qui retire la transition de phase"),
    ("coût", "Θ(n·d) messages par tour, 1 tour par mise à jour"),
    ("condition d'arrêt", "aucune — la règle s'applique indéfiniment"),
];

/// L'essaim aligné.
pub struct Alignement {
    /// Caps, en radians dans (−π, π].
    pub caps: Vec<f64>,
    /// Graphe de voisinage du tour courant : `voisins[i]` liste les voisins.
    voisins: Vec<Vec<usize>>,
    /// Cardinal du voisinage — borné, donc conforme à la définition d'essaim.
    pub degre: usize,
    /// Vrai quand la connexité conjointe est rompue par construction.
    pub scinde: bool,
    /// Tours écoulés.
    pub tours: u64,
}

impl Alignement {
    /// `n` agents de cap tiré uniformément dans (−π, π].
    pub fn nouveau(n: usize, degre: usize, alea: &mut Alea) -> Alignement {
        let caps = (0..n)
            .map(|_| alea.uniforme() * 2.0 * std::f64::consts::PI - std::f64::consts::PI)
            .collect();
        Alignement {
            caps,
            voisins: vec![Vec::new(); n],
            degre,
            scinde: false,
            tours: 0,
        }
    }

    /// Arme le critère d'accord — **local**, donc porteur de son
    /// contre-exemple et du réglage qui le met en défaut (PD10).
    pub fn armer_oracles(&self, registre: &mut Registre) {
        // PD10 — le critère est **local** : il porte son contre-exemple et le
        // réglage qui le met en défaut, et il ne s'affiche jamais « convergé ».
        registre.armer(Oracle::surete(ACCORD_LOCAL, "§1.1").local(
            "sur perte de connexité conjointe, chaque composante converge vers sa propre limite \
             et aucun agent ne peut le détecter",
            "activer la scission — `scinder(true)`",
        ));
    }

    /// Rompt (ou rétablit) la connexité conjointe. C'est le mode de défaillance
    /// nommé du mécanisme, provocable par un réglage (EX-A10, O2).
    pub fn scinder(&mut self, scinde: bool) {
        self.scinde = scinde;
    }

    /// Tire le graphe de voisinage du tour dans une **famille finie** : chaque
    /// agent reçoit `degre` voisins tirés parmi ceux de sa moitié quand
    /// l'essaim est scindé, parmi tous sinon.
    fn tirer_voisinage(&mut self, alea: &mut Alea) {
        let n = self.caps.len();
        let moitie = n / 2;
        for i in 0..n {
            let (debut, fin) = if !self.scinde {
                (0, n)
            } else if i < moitie {
                (0, moitie)
            } else {
                (moitie, n)
            };
            let etendue = (fin - debut) as u64;
            self.voisins[i].clear();
            for _ in 0..self.degre.min(etendue as usize) {
                let v = debut + alea.entier(etendue) as usize;
                if v != i && !self.voisins[i].contains(&v) {
                    self.voisins[i].push(v);
                }
            }
        }
    }

    /// Un tour : chaque agent prend la moyenne des caps de son voisinage,
    /// lui-même compris.
    ///
    /// La moyenne est circulaire — `atan2(Σ sin, Σ cos)` — parce qu'un cap est
    /// un angle : la moyenne arithmétique de −179° et +179° donnerait 0°, soit
    /// la direction exactement opposée. `libm` et non `f64` : DT1.
    pub fn tour(&mut self, alea: &mut Alea) {
        self.tirer_voisinage(alea);
        let anciens = self.caps.clone();
        for i in 0..self.caps.len() {
            let mut sx = libm::sin(anciens[i]);
            let mut cx = libm::cos(anciens[i]);
            for v in &self.voisins[i] {
                sx += libm::sin(anciens[*v]);
                cx += libm::cos(anciens[*v]);
            }
            self.caps[i] = libm::atan2(sx, cx);
        }
        self.tours += 1;
    }

    /// Dispersion des caps : écart circulaire moyen à la direction moyenne.
    /// Zéro quand tous les caps coïncident.
    ///
    /// **Ce n'est pas un paramètre d'ordre** au sens de PD5 : il n'y a ni
    /// paramètre de contrôle, ni seuil, ni exposant, parce qu'il n'y a pas de
    /// bruit. L'appeler Φ serait revendiquer une émergence que le mécanisme ne
    /// démontre pas.
    pub fn dispersion(&self) -> f64 {
        let n = self.caps.len() as f64;
        let sx: f64 = self.caps.iter().map(|c| libm::sin(*c)).sum();
        let cx: f64 = self.caps.iter().map(|c| libm::cos(*c)).sum();
        1.0 - (sx * sx + cx * cx).sqrt() / n
    }

    /// Dispersion à l'intérieur d'une moitié. Sert à montrer que sous scission
    /// chaque composante s'accorde — sur une valeur différente.
    pub fn dispersion_moitie(&self, seconde: bool) -> f64 {
        let n = self.caps.len();
        let plage = if seconde { n / 2..n } else { 0..n / 2 };
        let k = plage.len() as f64;
        let sx: f64 = plage.clone().map(|i| libm::sin(self.caps[i])).sum();
        let cx: f64 = plage.map(|i| libm::cos(self.caps[i])).sum();
        1.0 - (sx * sx + cx * cx).sqrt() / k
    }

    /// Cap moyen d'une moitié.
    pub fn cap_moyen_moitie(&self, seconde: bool) -> f64 {
        let n = self.caps.len();
        let plage = if seconde { n / 2..n } else { 0..n / 2 };
        let sx: f64 = plage.clone().map(|i| libm::sin(self.caps[i])).sum();
        let cx: f64 = plage.map(|i| libm::cos(self.caps[i])).sum();
        libm::atan2(sx, cx)
    }

    /// Évalue le critère **local** de l'agent `i` : son écart aux voisins
    /// est-il sous ε ?
    ///
    /// PD10 : ce que ce prédicat paraît dire — « le consensus est atteint » —
    /// est faux sous scission. Le simulateur le nomme « critère local
    /// (heuristique) » et livre le réglage qui le met en défaut.
    pub fn critere_local(&self, i: usize, epsilon: f64) -> bool {
        self.voisins[i]
            .iter()
            .all(|v| ecart_circulaire(self.caps[i], self.caps[*v]).abs() <= epsilon)
    }

    /// L'observateur, lui, voit les deux limites. Aucun agent n'y a accès
    /// (§8.3), et l'interface doit le dire.
    pub fn ecart_entre_moities(&self) -> f64 {
        ecart_circulaire(self.cap_moyen_moitie(false), self.cap_moyen_moitie(true)).abs()
    }

    /// Signale au registre qu'un critère local satisfait ne vaut pas accord —
    /// non comme violation, mais comme constat à afficher (EX-A39).
    pub fn critere_local_trompeur(&self, epsilon: f64, maintenant: Instant) -> Option<String> {
        let tous_satisfaits = (0..self.caps.len()).all(|i| self.critere_local(i, epsilon));
        if tous_satisfaits && self.scinde && self.ecart_entre_moities() > epsilon {
            Some(format!(
                "à {} : tous les critères locaux sont satisfaits, et les deux composantes \
                 s'accordent sur des caps distants de {:.3} rad. Aucun agent ne peut le détecter \
                 (§1.1).",
                maintenant.0,
                self.ecart_entre_moities()
            ))
        } else {
            None
        }
    }
}

/// Écart angulaire ramené dans (−π, π].
fn ecart_circulaire(a: f64, b: f64) -> f64 {
    let mut d = a - b;
    while d > std::f64::consts::PI {
        d -= 2.0 * std::f64::consts::PI;
    }
    while d <= -std::f64::consts::PI {
        d += 2.0 * std::f64::consts::PI;
    }
    d
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-A02 — sous connexité, l'essaim s'aligne sans protocole d'accord.
    /// NF-09 : le test vérifie une propriété **citée** du traité — l'accord de
    /// fait, §1.1.
    #[test]
    fn sous_connexite_lessaim_saligne() {
        let mut alea = Alea::nouveau(1);
        let mut a = Alignement::nouveau(64, 6, &mut alea);
        let depart = a.dispersion();
        for _ in 0..200 {
            a.tour(&mut alea);
        }
        assert!(depart > 0.3, "dispersion de départ {depart:.4}");
        assert!(a.dispersion() < 1e-6, "dispersion finale {:.9}", a.dispersion());
    }

    /// NF-10 — le mode de défaillance nommé se **provoque**, et se produit :
    /// chaque composante converge vers sa propre limite.
    #[test]
    fn sous_scission_chaque_composante_a_sa_limite() {
        let mut alea = Alea::nouveau(2);
        let mut a = Alignement::nouveau(64, 6, &mut alea);
        a.scinder(true);
        for _ in 0..300 {
            a.tour(&mut alea);
        }
        assert!(a.dispersion_moitie(false) < 1e-6, "moitié 1 non alignée");
        assert!(a.dispersion_moitie(true) < 1e-6, "moitié 2 non alignée");
        assert!(
            a.ecart_entre_moities() > 0.1,
            "les deux limites coïncident par hasard : écart {:.6}",
            a.ecart_entre_moities()
        );
    }

    /// PD10 — le critère local est satisfait alors que l'essaim est scindé.
    /// C'est le cœur du principe : un test local ne certifie pas une propriété
    /// globale.
    #[test]
    fn le_critere_local_est_satisfait_alors_que_lessaim_est_scinde() {
        let mut alea = Alea::nouveau(3);
        let mut a = Alignement::nouveau(64, 6, &mut alea);
        a.scinder(true);
        for _ in 0..300 {
            a.tour(&mut alea);
        }
        assert!((0..64).all(|i| a.critere_local(i, 1e-3)));
        let message = a.critere_local_trompeur(1e-3, Instant(300)).unwrap();
        assert!(message.contains("Aucun agent ne peut le détecter"), "{message}");
    }

    /// La moyenne des caps est circulaire : deux caps opposés autour de ±π
    /// doivent s'accorder sur π, jamais sur 0.
    #[test]
    fn la_moyenne_des_caps_est_circulaire() {
        let mut alea = Alea::nouveau(4);
        let mut a = Alignement::nouveau(2, 1, &mut alea);
        a.caps = vec![3.10, -3.10];
        for _ in 0..50 {
            a.tour(&mut alea);
        }
        let m = a.caps[0].abs();
        assert!(
            (m - std::f64::consts::PI).abs() < 0.1,
            "les caps se sont accordés sur {m:.4} au lieu de ±π"
        );
    }

    /// PD5 — le mécanisme ne fournit pas de paramètre d'ordre, et la signature
    /// le rattache à sa cause : c'est le **bruit nul** qui retire la transition
    /// de phase, non un manque d'implantation.
    ///
    /// Ce que ce test ne vérifie pas, et qu'il ne prétend plus vérifier : qu'il
    /// n'existe nulle part de méthode nommée `phi` ni de seuil rendu. Un test
    /// unitaire ne peut pas contrôler une absence de nom dans le module ; la
    /// discipline tient par la revue et par le `//!` du module.
    #[test]
    fn aucun_parametre_dordre_nest_revendique() {
        let bruit = SIGNATURE.iter().find(|(k, _)| *k == "bruit").expect("signature du bruit");
        assert!(bruit.1.contains("nul"));
        assert!(
            bruit.1.contains("transition de phase"),
            "la signature doit nommer ce que le bruit nul retire : {}",
            bruit.1
        );
        // Et la dispersion n'est jamais présentée comme un paramètre d'ordre :
        // aucun seuil, aucun paramètre de contrôle ne l'accompagne.
        assert!(
            !SIGNATURE.iter().any(|(k, _)| k.contains("paramètre d'ordre") || k.contains("seuil")),
            "aucune ligne de signature ne revendique un paramètre d'ordre"
        );
    }
}
