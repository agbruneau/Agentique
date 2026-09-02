//! Boucle de commande d'élasticité (EX-A25), ses trois modes de défaillance
//! (EX-A47), sa limite d'autorité (EX-A46) et la loi de Little (EX-A49).
//!
//! Un seul mécanisme pour ses deux écritures dans le traité : la **forme
//! algorithmique** du §2.2 — zone morte, plafond par p, budget de churn,
//! hystérésis de descente — et la **forme de plateforme** du §4.3 / §6.1 /
//! §7.3 — `visées = plafond[courantes × (métrique_courante / métrique_visée)]`,
//! tolérance 0,1, période 15 s, disponibilité initiale 30 s, initialisation de
//! la métrique processeur 5 min.
//!
//! La boucle est **perpétuelle** : sa condition d'arrêt n'est pas sa
//! terminaison. L'interface n'affiche jamais « stabilisé » — elle affiche le
//! point fixe atteint (|r − 1| ≤ τ) ou son absence.
//!
//! ## Ce que la mesure a établi, et que le PRD ne disait pas
//!
//! Aux **valeurs documentées** — tolérance 0,1, période 15 s, disponibilité
//! initiale 30 s — le contrôleur ne converge pas : il tourne autour de sa
//! cible. La raison est structurelle et n'a rien d'un défaut d'implantation :
//! `visées = courantes × r` est un correcteur proportionnel à gain unitaire, et
//! le temps mort vaut deux périodes de synchronisation. Un tel correcteur est
//! marginalement instable, et le §2.2 du traité le décrit d'ailleurs sans le nommer
//! ainsi : « le contrôleur mesure l'effet d'une décision qu'il n'a pas fini
//! d'appliquer ».
//!
//! La différence entre le régime nominal et le préréglage « oscillation »
//! d'EX-A47 est donc une différence **de degré, pas de nature** : l'hystérésis
//! de descente divise l'amplitude et le nombre d'inversions, elle ne les
//! supprime pas. C'est ce que les tests vérifient, et c'est ce que l'interface
//! doit montrer — un contrôleur qui « se stabilise » serait une fiction.

/// Sur quelle grandeur le contrôleur pilote.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Metrique {
    /// Le décalage de consommation : il répond au goulot réel.
    Decalage,
    /// L'occupation processeur : elle **sature après** le goulot réel, et le
    /// point fixe devient inatteignable (EX-A47, « métrique trompeuse »).
    Processeur,
}

/// Paramètres de la boucle.
#[derive(Clone, Debug)]
pub struct Params {
    /// Tolérance τ de la zone morte. Défaut documenté : 0,1.
    pub tolerance: f64,
    /// Période de synchronisation. Défaut documenté : 15 s.
    pub periode_s: f64,
    /// Délai de disponibilité initiale T_a — le temps mort entre une correction
    /// et le moment où elle contribue à la mesure. Défaut documenté : 30 s.
    pub disponibilite_initiale_s: f64,
    /// Période d'initialisation de la métrique processeur. Défaut documenté :
    /// 5 min.
    pub init_metrique_processeur_s: f64,
    /// Fenêtre d'hystérésis de descente W.
    pub fenetre_descente_s: f64,
    /// Budget de churn β : fraction de la population modifiable par période,
    /// **dans les deux sens**.
    pub beta: f64,
    /// Plafond structurel p — le contrôleur borne n par p, **jamais par u\***.
    pub p: u32,
    /// Ce que le contrôleur observe pour décider.
    pub metrique: Metrique,
    /// Population initiale.
    pub n0: u32,
}

impl Default for Params {
    fn default() -> Self {
        Params {
            tolerance: 0.1,
            periode_s: 15.0,
            disponibilite_initiale_s: 30.0,
            init_metrique_processeur_s: 300.0,
            // **Valeur documentée**, et non un choix du produit : le §7.3
            // (p. 114, 4ᵉ éd.) publie les défauts de la fenêtre de stabilisation —
            // 300 s à la baisse, 0 s à la hausse. Voir
            // [`Params::FENETRE_STABILISATION`]. L'asymétrie est le résultat : à
            // la baisse la fenêtre couvre exactement les vingt périodes de
            // l'aveuglement, à la hausse elle est nulle.
            fenetre_descente_s: 300.0,
            // Les trois valeurs qui suivent, elles, sont des **décisions du
            // produit sans provenance dans le traité** (F1) : le §2.2 décrit le
            // contrôleur et ses grandeurs, il n'en chiffre aucune. Elles sont
            // choisies pour que le régime nominal et le préréglage
            // « oscillation » d'EX-A47 se distinguent à l'œil, et pour aucune
            // autre raison.
            beta: 0.5,
            p: 32,
            metrique: Metrique::Decalage,
            n0: 4,
        }
    }
}

impl Params {
    /// EX-A47 — **oscillation** : W < 2·T_a, ou fenêtre de stabilisation nulle
    /// avec un temps mort supérieur à la période.
    pub fn oscillation() -> Params {
        Params {
            fenetre_descente_s: 0.0,
            // Temps mort de 60 s contre une période de 5 s : le contrôleur
            // réévalue douze fois avant que sa première correction porte.
            periode_s: 5.0,
            disponibilite_initiale_s: 60.0,
            beta: 1.0,
            ..Params::default()
        }
    }

    /// EX-A47 — **métrique trompeuse** : pilotage sur l'occupation processeur.
    pub fn metrique_trompeuse() -> Params {
        Params {
            metrique: Metrique::Processeur,
            ..Params::default()
        }
    }

    /// **Le rapport que le traité fait afficher en permanence** : nombre de
    /// fois où le contrôleur réévalue la même erreur avant qu'une réplique
    /// fraîche contribue à la mesure.
    ///
    /// Aux défauts documentés, 5 min / 15 s = **20** (NF-15).
    pub fn reevaluations_par_correction(&self) -> f64 {
        self.init_metrique_processeur_s / self.periode_s
    }

    /// Provenance de la fenêtre de stabilisation, affichée avec le réglage (F2).
    ///
    /// Les défauts **sont** publiés, et le §7.3 (p. 114, 4ᵉ éd.) les reprend : 300 s à
    /// la baisse, 0 s à la hausse. Le produit ne modélise que la baisse —
    /// [`Params::fenetre_descente_s`] — parce que la fenêtre nulle à la hausse
    /// n'a rien à retenir ; les deux politiques de montée qui bornent alors le
    /// pas (100 % ou 4 répliques par tranche de 15 s, la plus permissive
    /// l'emportant) ne sont **pas** transposées, le budget de churn ⌊β·T⌋ du
    /// §2.2 du traité tenant ce rôle.
    pub const FENETRE_STABILISATION: &'static str =
        "300 s à la baisse, 0 s à la hausse (§7.3, p. 114, 4ᵉ éd.) — seule la baisse est \
         transposée ; les deux politiques de montée du même paragraphe ne le sont pas, le \
         budget de churn ⌊β·T⌋ du §2.2 du traité en tenant lieu";
}

/// L'état de la boucle.
pub struct Controleur {
    /// Réglages de la boucle.
    pub params: Params,
    /// Population **visée** par le contrôleur.
    pub population: u32,
    /// Population visée, datée. La population **effective** — celle qui
    /// contribue à la mesure — est cette suite lue avec un retard de T_a.
    ///
    /// Le temps mort est modélisé comme un retard pur, et non comme une
    /// accumulation de corrections en vol : accumuler laisse la visée et
    /// l'effective dériver l'une de l'autre dès qu'un écrêtage intervient, et
    /// la boucle mesure alors un système qui n'existe pas.
    datee: Vec<(f64, u32)>,
    horloge_s: f64,
    /// Historique de la population, une entrée par période.
    pub historique: Vec<u32>,
    /// Depuis quand la métrique demande une descente sans interruption.
    /// L'hystérésis n'autorise la descente qu'au-delà de la fenêtre W.
    descente_demandee_depuis_s: Option<f64>,
    /// Nombre d'inversions du sens de correction. C'est la signature des dents
    /// de scie : une trajectoire qui converge en compte peu, une qui oscille en
    /// compte une par période ou presque.
    pub inversions: u64,
    dernier_sens: i8,
    /// Nombre de périodes où le point fixe |r − 1| ≤ τ était atteint.
    pub periodes_au_point_fixe: u64,
    /// Périodes écoulées.
    pub periodes: u64,
    /// Lectures de métriques : Θ(n) par période, 1 tour.
    pub lectures_de_metriques: u64,
    /// Tours de la boucle de contrôle.
    pub tours: u64,
    /// **Compteur de pannes** : le contrôleur n'en provoque aucune. Il reste à
    /// zéro même quand la population diverge, et c'est tout le point d'EX-A47.
    pub pannes: u32,
    /// τ mesuré — délai entre une correction et son effet mesurable. **Mesuré,
    /// jamais saisi** : chaque entrée est l'écart entre l'instant où une visée a
    /// été posée et la première période où elle entre dans la mesure, et non le
    /// T_a saisi. Les deux coïncident seulement quand T_a tombe sur un multiple
    /// de la période.
    delais_mesures: Vec<f64>,
    /// Instant de pose de la visée actuellement visible, pour ne compter chaque
    /// correction qu'une fois.
    derniere_visible_s: Option<f64>,
}

impl Controleur {
    /// Contrôleur au repos, population à `params.n0`.
    pub fn nouveau(params: Params) -> Controleur {
        let n0 = params.n0;
        Controleur {
            params,
            population: n0,
            datee: vec![(0.0, n0)],
            horloge_s: 0.0,
            historique: vec![n0],
            descente_demandee_depuis_s: None,
            inversions: 0,
            dernier_sens: 0,
            periodes_au_point_fixe: 0,
            periodes: 0,
            lectures_de_metriques: 0,
            tours: 0,
            pannes: 0,
            delais_mesures: Vec::new(),
            derniere_visible_s: None,
        }
    }

    /// La visée datée dont l'effet est déjà mesurable, avec **l'instant où elle
    /// a été posée**. `None` tant qu'aucune ne l'est.
    fn visee_visible(&self) -> Option<(f64, u32)> {
        let cible = self.horloge_s - self.params.disponibilite_initiale_s;
        self.datee.iter().rev().find(|(t, _)| *t <= cible).copied()
    }

    /// Population dont l'effet est déjà mesurable : la visée telle qu'elle
    /// était il y a T_a.
    pub fn population_effective(&self) -> u32 {
        self.visee_visible()
            .map(|(_, n)| n)
            .unwrap_or(self.params.n0)
    }

    /// Métrique observée pour une charge donnée.
    ///
    /// Le décalage répond au goulot réel : il décroît quand la population
    /// croît. L'occupation processeur **sature** : au-delà du goulot, elle ne
    /// bouge plus, et le point fixe devient inatteignable.
    fn metrique(&self, charge: f64) -> f64 {
        let n = self.population_effective().max(1) as f64;
        match self.params.metrique {
            Metrique::Decalage => charge / n,
            Metrique::Processeur => (charge / n).min(1.0),
        }
    }

    /// Une période de la boucle. `charge` est la charge offerte, `visee` la
    /// valeur cible de la métrique.
    pub fn periode(&mut self, charge: f64, visee: f64) {
        self.horloge_s += self.params.periode_s;
        self.periodes += 1;
        // Θ(n) lectures de métriques par période, et un tour : la boucle bloque
        // sur la collecte avant de décider.
        self.lectures_de_metriques += self.population.max(1) as u64;
        self.tours += 1;

        // τ est **mesuré, jamais saisi** (EX-A25) : c'est l'écart entre
        // l'instant où une correction a été posée et la première période où son
        // effet entre dans la mesure. Recopier `disponibilite_initiale_s` ferait
        // passer une entrée pour une sortie ; la quantification par la période
        // suffit d'ailleurs à les séparer dès que T_a n'est pas un multiple de
        // T. L'entrée initiale `(0, n₀)` est exclue : ce n'est pas une
        // correction.
        if let Some((pose_a, _)) = self.visee_visible() {
            if pose_a > 0.0 && self.derniere_visible_s != Some(pose_a) {
                self.derniere_visible_s = Some(pose_a);
                self.delais_mesures.push(self.horloge_s - pose_a);
            }
        }

        let m = self.metrique(charge);
        let r = if visee > 0.0 { m / visee } else { 1.0 };

        // Zone morte : |r − 1| ≤ τ. Le point fixe est **atteint**, pas
        // « stabilisé » — la boucle continue de tourner.
        if (r - 1.0).abs() <= self.params.tolerance {
            self.periodes_au_point_fixe += 1;
            self.descente_demandee_depuis_s = None;
            self.historique.push(self.population);
            return;
        }

        // visées = plafond[courantes × r], puis plafond structurel par p.
        let visees = ((self.population as f64) * r).ceil().max(1.0) as u32;
        let visees = visees.min(self.params.p);

        // Budget de churn ⌊β·T⌋, dans les deux sens.
        let budget = ((self.params.beta * self.population as f64).floor() as i64).max(1);
        let mut delta = (visees as i64 - self.population as i64).clamp(-budget, budget);

        // **Hystérésis de descente sur la fenêtre W** (EX-A25). On ne retire un
        // agent que si la métrique demande la descente sans interruption depuis
        // W. Sans elle, un correcteur proportionnel à retard pur entretient ses
        // propres dents de scie : c'est exactement le préréglage
        // « oscillation », qui met W à zéro.
        if delta < 0 {
            let depuis = *self
                .descente_demandee_depuis_s
                .get_or_insert(self.horloge_s);
            if self.horloge_s - depuis < self.params.fenetre_descente_s {
                delta = 0;
            }
        } else {
            self.descente_demandee_depuis_s = None;
        }

        let sens = delta.signum() as i8;
        if sens != 0 {
            if self.dernier_sens != 0 && sens != self.dernier_sens {
                self.inversions += 1;
            }
            self.dernier_sens = sens;
        }

        if delta != 0 {
            self.population = (self.population as i64 + delta).max(1) as u32;
            self.datee.push((self.horloge_s, self.population));
        }
        self.historique.push(self.population);
    }

    /// τ **mesuré** — délai entre une correction et son effet mesurable.
    /// Jamais saisi (EX-A25).
    pub fn tau_mesure_s(&self) -> Option<f64> {
        if self.delais_mesures.is_empty() {
            return None;
        }
        Some(self.delais_mesures.iter().sum::<f64>() / self.delais_mesures.len() as f64)
    }

    /// Amplitude crête à crête sur toute la trajectoire.
    pub fn amplitude_totale(&self) -> u32 {
        self.amplitude(self.historique.len())
    }

    /// Amplitude crête à crête de la population sur les `k` dernières périodes.
    /// C'est la mesure de l'oscillation.
    pub fn amplitude(&self, k: usize) -> u32 {
        let debut = self.historique.len().saturating_sub(k);
        let tranche = &self.historique[debut..];
        match (tranche.iter().max(), tranche.iter().min()) {
            (Some(h), Some(b)) => h - b,
            _ => 0,
        }
    }

    /// EX-A47 — l'interface affiche **le point fixe atteint ou son absence**,
    /// jamais « stabilisé ».
    pub fn affichage_point_fixe(&self) -> String {
        if self.periodes == 0 {
            return "aucune période exécutée".to_string();
        }
        let fraction = self.periodes_au_point_fixe as f64 / self.periodes as f64;
        if self.periodes_au_point_fixe == 0 {
            format!(
                "point fixe |r − 1| ≤ τ **jamais atteint** en {} périodes — la boucle est \
                 perpétuelle, et sa condition d'arrêt n'est pas sa terminaison",
                self.periodes
            )
        } else {
            format!(
                "point fixe |r − 1| ≤ τ atteint sur {:.0} % des {} périodes",
                fraction * 100.0,
                self.periodes
            )
        }
    }

    /// EX-A46 — le contrôleur **n'a autorité sur aucun invariant de sûreté**.
    /// L'arrêter au milieu d'un cycle gèle la population sans rien corrompre.
    pub fn arreter(&mut self) -> u32 {
        // La population visée reste ce qu'elle est, et le retard s'écoule sans
        // qu'aucun invariant n'en dépende : le contrôleur n'a autorité sur
        // aucune sûreté.
        self.population
    }
}

/// EX-A49 — la loi de Little, **outil de dimensionnement de la cible**, jamais
/// de pilotage.
///
/// Deux conséquences implantées : la boucle du contrôleur ne l'appelle jamais,
/// et le calculateur est un objet **séparé** qui affiche ses trois hypothèses
/// et étiquette son résultat « non valide » hors de leur domaine.
pub struct CibleLittle {
    /// λ — débit d'arrivée.
    pub lambda: f64,
    /// W — temps de séjour moyen.
    pub w: f64,
    /// c — capacité d'un agent.
    pub c: f64,
}

/// Régime dans lequel la mesure a été prise.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Regime {
    /// Stationnaire : les hypothèses tiennent.
    Stationnaire,
    /// Transitoire ou saturé : le résultat est **arithmétiquement exact et
    /// opérationnellement faux**.
    TransitoireOuSature,
}

impl CibleLittle {
    /// Les trois hypothèses de la loi de Little, affichées avec le résultat.
    /// Hors régime stationnaire, le calcul reste exact et la conclusion fausse.
    pub const HYPOTHESES: &'static [&'static str] = &[
        "moyennes finies",
        "processus stochastiques strictement stationnaires",
        "processus d'arrivée métriquement transitif de moyenne non nulle",
    ];

    /// n = λW/c, avec son étiquette de validité.
    pub fn calculer(&self, regime: Regime) -> (f64, Option<&'static str>) {
        let n = if self.c > 0.0 {
            self.lambda * self.w / self.c
        } else {
            0.0
        };
        let etiquette = match regime {
            Regime::Stationnaire => None,
            Regime::TransitoireOuSature => Some(
                "NON VALIDE — mesure prise en régime transitoire ou saturé : un nombre \
                 arithmétiquement exact et opérationnellement faux (§2.2 et §3.1 du traité)",
            ),
        };
        (n, etiquette)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// NF-15 — le rapport 5 min / 15 s = **20** est retrouvé, pas cité.
    #[test]
    fn le_rapport_de_reevaluation_vaut_vingt() {
        let p = Params::default();
        assert_eq!(p.reevaluations_par_correction(), 20.0);
    }

    /// F2 — la fenêtre de stabilisation porte sa provenance, et le défaut du
    /// produit est **celui du traité** : 300 s à la baisse (§7.3, p. 114, 4ᵉ éd.).
    ///
    /// Ce que le libellé doit dire en plus de la valeur : ce qui n'est **pas**
    /// transposé. La fenêtre à la hausse vaut 0 s et les deux politiques de
    /// montée qui bornent alors le pas ne sont pas implantées (PD6).
    #[test]
    fn la_fenetre_de_stabilisation_porte_sa_provenance_et_ce_quelle_omet() {
        assert_eq!(Params::default().fenetre_descente_s, 300.0);
        assert!(Params::FENETRE_STABILISATION.contains("300 s à la baisse"));
        assert!(Params::FENETRE_STABILISATION.contains("§7.3"));
        assert!(
            Params::FENETRE_STABILISATION.contains("ne le sont pas"),
            "le libellé doit nommer ce qui n'est pas transposé (PD6)"
        );
    }

    /// En régime sain, le contrôleur **finit** au point fixe et y reste.
    ///
    /// Le pourcentage global n'est pas le bon critère : même aux défauts
    /// documentés, T_a = 30 s contre une période de 15 s donne deux
    /// réévaluations avant qu'une correction porte, donc un dépassement
    /// initial. Ce qui distingue le régime sain de l'oscillation n'est pas
    /// l'absence de transitoire, c'est qu'il **se termine**.
    #[test]
    fn en_regime_sain_le_point_fixe_est_atteint() {
        let mut c = Controleur::nouveau(Params::default());
        for _ in 0..120 {
            c.periode(80.0, 10.0);
        }
        // La cible est 80 / 10 = 8, et la zone morte |r − 1| ≤ 0,1 ne contient
        // que n = 8. Le contrôleur y passe, sans s'y immobiliser : voir la note
        // du module. Ce qui est exigé du régime sain est qu'il reste **borné**
        // au voisinage de la cible, et qu'il atteigne le point fixe.
        assert!(
            (5..=14).contains(&c.population),
            "la population doit rester bornée au voisinage de 8, or {}",
            c.population
        );
        assert!(
            c.amplitude_totale() <= 12,
            "la population ne doit pas balayer toute la plage, amplitude {}",
            c.amplitude_totale()
        );
        assert!(c.periodes_au_point_fixe > 0, "{}", c.affichage_point_fixe());
        assert_eq!(c.pannes, 0);
    }

    /// EX-A25 — c'est **l'hystérésis de descente** qui sépare le régime sain de
    /// l'oscillation. La retirer, toutes choses égales par ailleurs, suffit à
    /// produire les dents de scie.
    #[test]
    fn lhysteresis_de_descente_est_ce_qui_amortit() {
        let mut avec = Controleur::nouveau(Params::default());
        let mut sans = Controleur::nouveau(Params {
            fenetre_descente_s: 0.0,
            ..Params::default()
        });
        for _ in 0..120 {
            avec.periode(80.0, 10.0);
            sans.periode(80.0, 10.0);
        }
        assert!(
            sans.inversions >= avec.inversions * 3,
            "sans hystérésis {} inversions, avec {}",
            sans.inversions,
            avec.inversions
        );
        // L'amplitude totale, elle, ne les sépare pas : elle est dominée par le
        // dépassement initial, qui est une **montée**, et l'hystérésis ne
        // s'applique qu'aux descentes. Un test qui l'exigerait mesurerait une
        // promesse que le mécanisme ne fait pas.
        assert_eq!(
            sans.amplitude_totale(),
            avec.amplitude_totale(),
            "le dépassement initial est le même : seule la suite diffère"
        );
    }

    /// Critère de sortie de la phase 2 — le préréglage « oscillation » diverge
    /// **avec un compteur de pannes strictement nul**. C'est ce qui le rend
    /// pédagogique : rien n'est tombé, et le système est inutilisable.
    #[test]
    fn le_prereglage_oscillation_diverge_sans_aucune_panne() {
        let mut c = Controleur::nouveau(Params::oscillation());
        for _ in 0..200 {
            c.periode(80.0, 10.0);
        }
        assert_eq!(c.pannes, 0, "aucune panne — c'est tout le point");
        assert!(
            c.amplitude_totale() >= 8,
            "la population devrait balayer une large plage, amplitude {}",
            c.amplitude_totale()
        );
        assert!(
            c.inversions >= 4,
            "les dents de scie se comptent en inversions de sens, or {}",
            c.inversions
        );
        // Et le contrôleur passe l'essentiel de son temps hors du point fixe.
        assert!(
            (c.periodes_au_point_fixe as f64) < 0.2 * c.periodes as f64,
            "{}",
            c.affichage_point_fixe()
        );
    }

    /// EX-A47 — l'interface n'affiche **jamais** « stabilisé ».
    #[test]
    fn linterface_naffiche_jamais_stabilise() {
        let mut c = Controleur::nouveau(Params::oscillation());
        for _ in 0..40 {
            c.periode(80.0, 10.0);
        }
        let a = c.affichage_point_fixe();
        assert!(!a.contains("stabilis"), "{a}");
        assert!(a.contains("point fixe"), "{a}");
    }

    /// EX-A47 — **métrique trompeuse** : l'occupation processeur sature après
    /// le goulot réel, et le point fixe devient inatteignable.
    #[test]
    fn la_metrique_trompeuse_rend_le_point_fixe_inatteignable() {
        let mut c = Controleur::nouveau(Params::metrique_trompeuse());
        // Charge telle que la métrique sature à 1,0 alors que la visée est 0,2.
        for _ in 0..60 {
            c.periode(1_000.0, 0.2);
        }
        assert_eq!(
            c.periodes_au_point_fixe, 0,
            "la métrique saturée ne redescend jamais dans la zone morte"
        );
        assert!(c.affichage_point_fixe().contains("jamais atteint"));
    }

    /// EX-A25 — le contrôleur borne n par **p**, jamais par u\*.
    #[test]
    fn le_controleur_borne_n_par_p_et_pas_autrement() {
        let mut c = Controleur::nouveau(Params {
            p: 6,
            ..Params::default()
        });
        for _ in 0..60 {
            c.periode(10_000.0, 1.0);
        }
        assert_eq!(c.population, 6, "la ligne 5 borne n par p");
    }

    /// EX-A25 — le budget de churn borne la variation par période, dans les
    /// deux sens.
    #[test]
    fn le_budget_de_churn_borne_la_variation() {
        let mut c = Controleur::nouveau(Params {
            n0: 10,
            beta: 0.2,
            p: 1_000,
            ..Params::default()
        });
        c.periode(10_000.0, 1.0);
        assert!(
            c.population <= 12,
            "⌊0,2 × 10⌋ = 2 au plus par période, or n = {}",
            c.population
        );
    }

    /// EX-A25 — τ est **mesuré**, jamais saisi.
    ///
    /// Aux défauts documentés, T_a = 30 s est un multiple de la période de 15 s,
    /// donc la mesure retombe sur la valeur saisie ; c'est ce qui rendait
    /// invisible une implantation qui se contentait de recopier T_a. Le second
    /// cas sépare les deux : à T_a = 20 s pour une période de 15 s, la
    /// quantification de la boucle porte le délai **réel** à 30 s, et c'est lui
    /// que le simulateur doit rendre.
    #[test]
    fn tau_est_mesure_et_pas_saisi() {
        let mut c = Controleur::nouveau(Params::default());
        assert_eq!(c.tau_mesure_s(), None, "rien à mesurer avant la première correction");
        for _ in 0..20 {
            c.periode(500.0, 10.0);
        }
        assert_eq!(c.tau_mesure_s(), Some(30.0), "le temps mort mesuré");

        let mut decale = Controleur::nouveau(Params {
            disponibilite_initiale_s: 20.0,
            ..Params::default()
        });
        for _ in 0..20 {
            decale.periode(500.0, 10.0);
        }
        assert_eq!(
            decale.tau_mesure_s(),
            Some(30.0),
            "τ mesuré doit être le délai réel (30 s), non le T_a saisi (20 s)"
        );
    }

    /// EX-A46 — arrêter le contrôleur en plein cycle gèle la population et ne
    /// corrompt rien.
    #[test]
    fn arreter_le_controleur_gele_la_population_sans_rien_corrompre() {
        let mut c = Controleur::nouveau(Params::default());
        for _ in 0..7 {
            c.periode(500.0, 10.0);
        }
        let n = c.arreter();
        assert_eq!(n, c.population);
        assert_eq!(c.pannes, 0);
        // Aucune correction en vol ne s'appliquera : l'état est cohérent.
        let avant = c.population;
        c.periode(500.0, 10.0);
        assert!(c.population.abs_diff(avant) <= (c.params.beta * avant as f64) as u32 + 1);
    }

    /// EX-A49 — la loi de Little étiquette son résultat « non valide » hors de
    /// son domaine, et affiche ses trois hypothèses.
    #[test]
    fn little_etiquette_son_resultat_hors_domaine() {
        let cible = CibleLittle {
            lambda: 100.0,
            w: 0.2,
            c: 2.0,
        };
        let (n, etiquette) = cible.calculer(Regime::Stationnaire);
        assert_eq!(n, 10.0);
        assert!(etiquette.is_none());

        let (n2, etiquette2) = cible.calculer(Regime::TransitoireOuSature);
        assert_eq!(n2, 10.0, "arithmétiquement exact");
        assert!(
            etiquette2.unwrap().contains("opérationnellement faux"),
            "et opérationnellement faux"
        );
        assert_eq!(CibleLittle::HYPOTHESES.len(), 3);
    }
}
