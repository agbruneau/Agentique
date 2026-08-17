//! Loi d'échelle universelle : mesure de σ et κ (scénario C).
//!
//! > L'ouvrage n'a pas dit comment. (conclusion, p. 130)
//!
//! C'est la contribution du projet au traité : le §2.1 pose
//! `C(n) = n / (1 + σ(n − 1) + κn(n − 1))` et `u* = √((1 − σ)/κ)`, mais ne
//! fournit **aucun protocole de mesure**. Ce module en fournit un, et le valide
//! par croisement — on injecte σ et κ, on **applique la formule** pour produire
//! les points, on y ajoute un bruit, et on vérifie que l'ajustement retrouve les
//! valeurs injectées.
//!
//! **Ce que cette validation croisée établit, et ce qu'elle n'établit pas.** Elle
//! établit que l'estimateur est correct : la régression retrouve ce qu'on a
//! injecté. Elle n'établit **rien** sur un débit émergent, parce qu'il n'y a sous
//! ces points ni milieu, ni latence, ni boucle à événements — la régression
//! inverse la formule qui a produit les points. `crate::hors_perimetre()` le
//! déclare (F2).
//!
//! **Ce que σ̂ et κ̂ caractérisent** : le milieu **simulé**, jamais un courtier
//! de production. Ce que la campagne valide, c'est le protocole. Le libellé est
//! obligatoire et permanent (voir [`LIBELLE`]).
//!
//! La régression est un moindres carrés à deux paramètres écrit à la main —
//! PD7 : une dépendance d'optimisation pour résoudre un système 2 × 2 serait
//! exactement la dérive que RQ3 surveille.

use sim_core::alea::Alea;

/// Libellé permanent du scénario C (F2). Il ne se replie pas.
pub const LIBELLE: &str =
    "paramètres du milieu simulé — le protocole est transposable, la valeur ne l'est pas";

/// Les deux paramètres de l'USL.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Parametres {
    /// σ — contention, la part sérialisée.
    pub sigma: f64,
    /// κ — cohérence, le coût quadratique de coordination.
    pub kappa: f64,
}

impl Parametres {
    /// Débit relatif à n agents : `C(n) = n / (1 + σ(n − 1) + κn(n − 1))`.
    pub fn debit(&self, n: f64) -> f64 {
        n / (1.0 + self.sigma * (n - 1.0) + self.kappa * n * (n - 1.0))
    }

    /// `u* = √((1 − σ)/κ)` — le maximum, au-delà duquel la courbe devient
    /// rétrograde.
    ///
    /// Rend `None` quand κ = 0 : il n'y a alors pas de maximum, et le
    /// simulateur ne fabrique pas un nombre pour combler (F1).
    pub fn u_etoile(&self) -> Option<f64> {
        if self.kappa <= 0.0 || self.sigma >= 1.0 {
            return None;
        }
        Some(((1.0 - self.sigma) / self.kappa).sqrt())
    }
}

/// Un point de mesure : une taille et le débit mesuré.
#[derive(Clone, Copy, Debug)]
pub struct Point {
    /// Taille de l'essaim mesuré.
    pub n: f64,
    /// Débit **relatif** à celui d'un agent seul.
    pub debit_relatif: f64,
}

/// Ajuste σ et κ par moindres carrés.
///
/// Linéarisation exacte, sans approximation : de
/// `C(n) = n / (1 + σ(n−1) + κn(n−1))` on tire
/// `n/C(n) − 1 = σ(n−1) + κn(n−1)`, qui est **linéaire** en (σ, κ) et sans
/// terme constant. Le système normal est donc 2 × 2, et se résout par Cramer.
///
/// Rend `None` si le système est dégénéré — moins de deux tailles distinctes,
/// ou déterminant nul. Un ajustement impossible se déclare ; il ne se comble
/// pas par une valeur arbitraire.
pub fn ajuster(points: &[Point]) -> Option<Parametres> {
    let (mut s11, mut s12, mut s22, mut s1y, mut s2y) = (0.0, 0.0, 0.0, 0.0, 0.0);
    for p in points {
        if p.n <= 1.0 || p.debit_relatif <= 0.0 {
            continue;
        }
        let x1 = p.n - 1.0;
        let x2 = p.n * (p.n - 1.0);
        let y = p.n / p.debit_relatif - 1.0;
        s11 += x1 * x1;
        s12 += x1 * x2;
        s22 += x2 * x2;
        s1y += x1 * y;
        s2y += x2 * y;
    }
    let det = s11 * s22 - s12 * s12;
    if det.abs() < 1e-12 {
        return None;
    }
    Some(Parametres {
        sigma: (s1y * s22 - s2y * s12) / det,
        kappa: (s11 * s2y - s12 * s1y) / det,
    })
}

/// Intervalle de confiance d'un paramètre.
#[derive(Clone, Copy, Debug)]
pub struct Intervalle {
    /// Borne basse.
    pub bas: f64,
    /// Borne haute.
    pub haut: f64,
}

impl Intervalle {
    /// Vrai si `x` tombe dans l'intervalle, bornes comprises. C'est le test de
    /// la validation croisée : le paramètre injecté doit s'y retrouver.
    pub fn contient(&self, x: f64) -> bool {
        x >= self.bas && x <= self.haut
    }
}

/// Résultat d'un ajustement avec ses intervalles de confiance.
#[derive(Clone, Debug)]
pub struct Ajustement {
    /// σ̂ et κ̂ estimés sur les points de mesure.
    pub estimation: Parametres,
    /// Intervalle de confiance de σ̂, par rééchantillonnage.
    pub ic_sigma: Intervalle,
    /// Intervalle de confiance de κ̂.
    pub ic_kappa: Intervalle,
    /// Intervalle de confiance de u\* — `None` quand κ̂ ≤ 0, auquel cas le
    /// maximum n'existe pas et rien n'est affiché à sa place.
    pub ic_u_etoile: Option<Intervalle>,
    /// Résidus relatifs, pour le tracé.
    pub residus: Vec<f64>,
    /// Nombre de rééchantillonnages ayant abouti.
    pub reechantillonnages: usize,
}

/// Ajuste avec intervalles de confiance **par rééchantillonnage**.
///
/// Le rééchantillonnage tire les points avec remise ; c'est la seule méthode
/// qui ne suppose rien de la loi des résidus, et le §2.1 ne fournit aucune loi.
pub fn ajuster_avec_ic(points: &[Point], tirages: usize, alea: &mut Alea) -> Option<Ajustement> {
    let estimation = ajuster(points)?;

    let mut sigmas = Vec::with_capacity(tirages);
    let mut kappas = Vec::with_capacity(tirages);
    let mut us = Vec::with_capacity(tirages);
    let mut echantillon = Vec::with_capacity(points.len());
    for _ in 0..tirages {
        echantillon.clear();
        for _ in 0..points.len() {
            echantillon.push(points[alea.entier(points.len() as u64) as usize]);
        }
        if let Some(p) = ajuster(&echantillon) {
            sigmas.push(p.sigma);
            kappas.push(p.kappa);
            if let Some(u) = p.u_etoile() {
                us.push(u);
            }
        }
    }
    if sigmas.len() < 10 {
        return None;
    }

    let residus = points
        .iter()
        .map(|p| {
            let attendu = estimation.debit(p.n);
            if attendu > 0.0 {
                (p.debit_relatif - attendu) / attendu
            } else {
                0.0
            }
        })
        .collect();

    Some(Ajustement {
        reechantillonnages: sigmas.len(),
        ic_sigma: percentiles(&mut sigmas),
        ic_kappa: percentiles(&mut kappas),
        ic_u_etoile: if us.len() >= 10 {
            Some(percentiles(&mut us))
        } else {
            None
        },
        estimation,
        residus,
    })
}

/// Intervalle à 95 % par percentiles empiriques.
fn percentiles(v: &mut [f64]) -> Intervalle {
    // `total_cmp` et non `partial_cmp(…).unwrap_or(Equal)` : ce dernier rend un
    // ordre **non transitif** dès qu'un `NaN` entre dans l'échantillon — un
    // rééchantillonnage dégénéré suffit —, et le résultat du tri dépend alors du
    // parcours de l'algorithme, ce que PD1 interdit.
    v.sort_by(|a, b| a.total_cmp(b));
    let bas = v[((0.025 * v.len() as f64) as usize).min(v.len() - 1)];
    let haut = v[((0.975 * v.len() as f64) as usize).min(v.len() - 1)];
    Intervalle { bas, haut }
}

/// Modèle de charge à contention **connue par construction**.
///
/// C'est ce qui rend la validation croisée possible : le temps de service d'un
/// agent croît selon `t(n) = t₀ (1 + σ(n − 1) + κn(n − 1))`, de sorte que le
/// débit total vaut exactement `n/t(n)`, soit l'USL. On mesure ensuite ce débit
/// par simulation, avec le bruit que les latences y ajoutent, et on vérifie que
/// l'ajustement retrouve les paramètres injectés.
#[derive(Clone, Copy, Debug)]
pub struct Charge {
    /// σ et κ **injectés** dans le milieu simulé. Ce sont eux que
    /// l'ajustement doit retrouver.
    pub injectes: Parametres,
    /// Temps de service d'un agent seul, en millisecondes.
    pub t0_ms: f64,
    /// Bruit relatif sur chaque mesure de temps de service.
    pub bruit: f64,
    /// Plafond structurel : au-delà de p, les agents supplémentaires ne
    /// travaillent pas (EX-M19).
    pub p: u32,
}

impl Charge {
    /// Milieu simulé aux paramètres injectés, avec 5 % de bruit relatif.
    pub fn nouvelle(sigma: f64, kappa: f64, p: u32) -> Charge {
        Charge {
            injectes: Parametres { sigma, kappa },
            t0_ms: 1.0,
            bruit: 0.05,
            p,
        }
    }

    /// Rend le débit relatif à n agents, **par application de la formule du
    /// §2.1**, avec un bruit multiplicatif — ce n'est pas une mesure.
    ///
    /// Aucun agent ne tire de temps de service ici, aucun achèvement n'est
    /// compté : `t_nominal` est calculé une fois, hors boucle, et la boucle ne
    /// fait qu'y appliquer le bruit. Le nom du scénario C parle de débit
    /// « émergent » ; ce qui émerge est le bruit, pas la loi
    /// (`crate::hors_perimetre()`, F2).
    ///
    /// Le plafond min(n, p) s'applique — les agents au-delà de p n'entrent pas
    /// au numérateur (EX-M19).
    pub fn mesurer(&self, n: u32, cycles: u32, alea: &mut Alea) -> f64 {
        let actifs = n.min(self.p) as f64;
        let nf = n as f64;
        let t_nominal = self.t0_ms * (1.0 + self.injectes.sigma * (nf - 1.0)
            + self.injectes.kappa * nf * (nf - 1.0));
        let mut total = 0.0;
        for _ in 0..cycles {
            // Bruit multiplicatif centré : la mesure n'est jamais exacte, et
            // c'est ce qui donne son sens à l'intervalle de confiance.
            let facteur = 1.0 + self.bruit * (alea.uniforme() * 2.0 - 1.0);
            total += t_nominal * facteur;
        }
        let t_moyen = total / cycles as f64;
        // Débit relatif à celui d'un agent seul (t₀).
        actifs * self.t0_ms / t_moyen
    }

    /// Produit les points de mesure d'une campagne, tailles réparties en
    /// progression géométrique.
    pub fn campagne(
        &self,
        n_min: u32,
        n_max: u32,
        tailles: usize,
        repetitions: u32,
        alea: &mut Alea,
    ) -> Vec<Point> {
        let mut points = Vec::new();
        for i in 0..tailles {
            let f = i as f64 / (tailles.max(2) - 1) as f64;
            // `libm::pow` et non `f64::powf` : la répartition des tailles
            // décide des points mesurés, donc du résultat de la campagne. DT1.
            let n = (n_min as f64 * libm::pow(n_max as f64 / n_min as f64, f)).round() as u32;
            for _ in 0..repetitions {
                points.push(Point {
                    n: n as f64,
                    debit_relatif: self.mesurer(n, 32, alea),
                });
            }
        }
        points
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// La formule du §2.1 est reproduite exactement, et C(1) = 1.
    #[test]
    fn la_formule_usl_est_celle_du_traite() {
        let p = Parametres {
            sigma: 0.02,
            kappa: 0.0001,
        };
        assert!((p.debit(1.0) - 1.0).abs() < 1e-12);
        // C(n) < n dès qu'il y a de la contention.
        assert!(p.debit(10.0) < 10.0);
        // Et la courbe devient rétrograde au-delà de u*.
        let u = p.u_etoile().unwrap();
        assert!(p.debit(u * 2.0) < p.debit(u));
    }

    /// F1 — sans κ, il n'y a pas de maximum, et le simulateur n'en fabrique pas.
    #[test]
    fn sans_kappa_il_ny_a_pas_de_maximum() {
        let p = Parametres {
            sigma: 0.1,
            kappa: 0.0,
        };
        assert_eq!(p.u_etoile(), None);
    }

    /// L'ajustement retrouve exactement des paramètres sur des données sans
    /// bruit : c'est le contrôle de la mécanique avant celui de la mesure.
    #[test]
    fn lajustement_est_exact_sans_bruit() {
        let vrais = Parametres {
            sigma: 0.03,
            kappa: 0.0002,
        };
        let points: Vec<Point> = [2u32, 4, 8, 16, 32, 64, 128]
            .iter()
            .map(|n| Point {
                n: *n as f64,
                debit_relatif: vrais.debit(*n as f64),
            })
            .collect();
        let e = ajuster(&points).unwrap();
        assert!((e.sigma - vrais.sigma).abs() < 1e-9, "σ̂ = {}", e.sigma);
        assert!((e.kappa - vrais.kappa).abs() < 1e-12, "κ̂ = {}", e.kappa);
    }

    #[test]
    fn un_systeme_degenere_est_refuse() {
        assert!(ajuster(&[]).is_none());
        assert!(ajuster(&[Point { n: 1.0, debit_relatif: 1.0 }]).is_none());
    }

    /// **Critère d'acceptation (1) du scénario C** — sur un milieu à contention
    /// connue par construction, l'estimation retrouve les paramètres injectés à
    /// l'intérieur de son intervalle de confiance.
    ///
    /// C'est cette validation croisée qui autorise à faire confiance à
    /// l'estimation là où la vérité n'est pas connue.
    #[test]
    fn la_validation_croisee_retrouve_les_parametres_injectes() {
        let charge = Charge::nouvelle(0.02, 0.0001, 4_096);
        let mut alea = Alea::nouveau(1);
        let points = charge.campagne(2, 512, 16, 30, &mut alea);
        let a = ajuster_avec_ic(&points, 400, &mut alea).unwrap();

        assert!(
            a.ic_sigma.contient(charge.injectes.sigma),
            "σ injecté {} hors de [{:.6}, {:.6}]",
            charge.injectes.sigma,
            a.ic_sigma.bas,
            a.ic_sigma.haut
        );
        assert!(
            a.ic_kappa.contient(charge.injectes.kappa),
            "κ injecté {} hors de [{:.8}, {:.8}]",
            charge.injectes.kappa,
            a.ic_kappa.bas,
            a.ic_kappa.haut
        );
        assert!(a.reechantillonnages > 300);
    }

    /// … et u\* est reproductible à la graine près (O3).
    #[test]
    fn u_etoile_est_reproductible_a_la_graine_pres() {
        let charge = Charge::nouvelle(0.02, 0.0001, 4_096);
        let ajuster_avec = |graine| {
            let mut alea = Alea::nouveau(graine);
            let points = charge.campagne(2, 512, 16, 30, &mut alea);
            ajuster_avec_ic(&points, 200, &mut alea)
                .unwrap()
                .estimation
                .u_etoile()
                .unwrap()
        };
        assert_eq!(ajuster_avec(7), ajuster_avec(7));

        // Et l'estimation encadre la vraie valeur.
        let vrai = charge.injectes.u_etoile().unwrap();
        let estime = ajuster_avec(7);
        assert!(
            (estime - vrai).abs() / vrai < 0.2,
            "û* = {estime:.1} contre u* = {vrai:.1}"
        );
    }

    /// **Critère d'acceptation (2)** — au-delà de n = p, le débit cesse de
    /// croître.
    #[test]
    fn au_dela_de_p_le_debit_cesse_de_croitre() {
        let charge = Charge::nouvelle(0.001, 0.0, 16);
        let mut alea = Alea::nouveau(2);
        let a_p = charge.mesurer(16, 64, &mut alea);
        let a_deux_p = charge.mesurer(32, 64, &mut alea);
        assert!(
            a_deux_p <= a_p * 1.05,
            "le débit ne doit pas croître au-delà de p : {a_p:.2} puis {a_deux_p:.2}"
        );
    }

    /// F2 — le libellé permanent dit ce que les paramètres caractérisent.
    #[test]
    fn le_libelle_dit_ce_que_les_parametres_caracterisent() {
        assert!(LIBELLE.contains("milieu simulé"));
        assert!(LIBELLE.contains("la valeur ne l'est pas"));
    }
}
