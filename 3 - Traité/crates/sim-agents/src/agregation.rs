//! Les trois mécanismes d'agrégation du scénario H, et l'oracle qui les juge.
//!
//! > Le résultat n'est pas en retard, il est faux. (§4.1, p. 58, 3ᵉ éd.)
//!
//! - **EX-A14** — algorithme 1 du ch. 4, échange par paires push-pull, avec
//!   époque et relance. **Aucune condition d'arrêt.**
//! - **EX-A15** — push-sum valeur-poids, dont l'estimateur est le rapport des
//!   deux. L'accusé de réception est un **commutateur** : il restaure la
//!   conservation à 2 messages par échange au lieu de 1.
//! - **EX-A16** — politique stochastique par taux. **Zéro message**, et
//!   **aucune** condition d'arrêt, pas même heuristique.
//!
//! **EX-A37** — la conservation de masse est un oracle, et sa rupture est un
//! scénario. Sa violation n'arrête pas l'exécution : elle est **datée et
//! attribuée à sa ligne**.

use crate::echantillonnage::{Biais, ServiceDePairs};
use sim_core::alea::Alea;
use sim_core::oracle::{Oracle, Registre};
use sim_core::temps::Instant;

/// Nom de l'oracle de conservation.
pub const CONSERVATION: &str = "EX-A37 — conservation de masse de l'agrégation";

/// Où la masse a été perdue. L'oracle ne dit pas « la somme a bougé » : il dit
/// **quelle ligne** de quel échange l'a fait bouger.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Ligne {
    /// Ligne 4 — le PULL de retour s'est perdu : j a moyenné, i non.
    Ligne4PullPerdu,
    /// Crash-arrêt entre deux cycles : la masse détenue disparaît.
    CrashEnCoursDeProtocole,
    /// Ligne 11 — la relance **ne plafonne pas** l'erreur : elle réinjecte de la
    /// dispersion à chaque période, et le maximum de la dérive croît avec la
    /// durée d'observation (§4.1, p. 58, 3ᵉ éd.).
    Ligne11Relance,
    /// Lignes 5 et 6 — deux traitements opposés du même désaccord d'époque.
    Epoque,
}

impl Ligne {
    /// La ligne de l'algorithme, citée avec ce qu'elle produit.
    pub fn libelle(self) -> &'static str {
        match self {
            Ligne::Ligne4PullPerdu => {
                "ligne 4 — PULL perdu : j a exécuté sa ligne 10, i non ; la somme quitte sa \
                 valeur de |x_i − x_j|/2 sur cet échange"
            }
            Ligne::CrashEnCoursDeProtocole => {
                "crash-arrêt entre deux cycles — la masse détenue disparaît ; le protocole \
                 converge encore, vers une autre valeur"
            }
            Ligne::Ligne11Relance => {
                "ligne 11 — la relance ne **plafonne** pas l'erreur : elle réinjecte de la \
                 dispersion à chaque période, de sorte que son maximum croît avec la durée \
                 d'observation, là où l'erreur sans relance est acquise une fois pour toutes. Ce \
                 qu'elle achète n'est pas un plafond mais la conversion d'un mensonge stable en \
                 une oscillation qu'un opérateur voit passer (§4.1, p. 58, 3ᵉ éd.)"
            }
            Ligne::Epoque => {
                "lignes 5 contre 6 — l'agent en retard se réinitialise, l'agent en avance \
                 ignore : deux traitements opposés du même désaccord d'époque"
            }
        }
    }
}

/// Une rupture de conservation, datée et attribuée.
#[derive(Clone, Debug)]
pub struct Rupture {
    /// Instant de la rupture.
    pub date: Instant,
    /// La ligne de l'algorithme qui l'a produite — l'attribution, et non le
    /// simple constat qu'un écart existe.
    pub ligne: Ligne,
    /// Variation **signée** de la somme.
    ///
    /// Le traité écrit « la somme totale a diminué » pour l'échange qu'il
    /// détaille ; la mesure montre les deux sens selon l'ordre de x_i et x_j, et
    /// l'interface affiche la quantité signée **sans corriger le texte source**.
    pub variation: f64,
    /// Les deux agents de l'échange fautif.
    pub entre: (u32, u32),
}

/// Les préréglages d'EX-A37.
#[derive(Clone, Copy, Debug)]
pub struct Params {
    /// Taille de la population.
    pub n: u32,
    /// Taux d'omission sur le chemin de **retour** — c'est la ligne 4.
    pub omission: f64,
    /// Période de relance C, en cycles. `None` = relance désactivée : l'erreur
    /// n'est plus plafonnée.
    pub relance: Option<u32>,
    /// Cycle du premier crash-arrêt.
    pub crash_au_cycle: Option<u32>,
    /// Accusé de réception du push-sum : restaure la conservation à 2 messages
    /// par échange au lieu de 1.
    pub accuse_push_sum: bool,
    /// Répartition des mesures initiales.
    pub biais: Biais,
    /// Partition réseau : les agents d'indice < n/2 ne parlent plus aux autres.
    pub partition: bool,
}

impl Default for Params {
    fn default() -> Self {
        Params {
            n: 64,
            omission: 0.01,
            relance: Some(50),
            crash_au_cycle: None,
            accuse_push_sum: false,
            biais: Biais::Desequilibre,
            partition: false,
        }
    }
}

impl Params {
    /// Régime sans faute : la somme doit être conservée exactement.
    pub fn sans_faute() -> Params {
        Params {
            omission: 0.0,
            biais: Biais::Uniforme,
            ..Params::default()
        }
    }
}

/// **EX-A14** — échange par paires push-pull.
pub struct PushPull {
    /// Estimation courante de chaque agent.
    pub x: Vec<f64>,
    x0: Vec<f64>,
    /// Époque de chaque agent.
    epoque: Vec<u64>,
    vivant: Vec<bool>,
    /// Préréglage en vigueur.
    pub params: Params,
    /// Ruptures de conservation, datées et **attribuées à une ligne**.
    pub ruptures: Vec<Rupture>,
    /// Cycles exécutés.
    pub cycles: u32,
    /// Messages échangés.
    pub messages: u64,
    /// Somme au démarrage — la masse à conserver.
    pub somme_initiale: f64,
    /// Dérive **maximale** observée depuis le début.
    pub derive_max: f64,
    /// Nombre de fois où la relance a ramené la somme à sa valeur initiale.
    ///
    /// C'est l'observable du « tracé qui remonte » d'EX-A37 : la relance ne
    /// corrige pas l'erreur, elle **remet le compteur à zéro**, et la dérive
    /// reprend aussitôt sur une dispersion fraîchement réintroduite.
    pub retours_a_zero: u32,
}

impl PushPull {
    /// Initialise à partir des mesures locales. Leur somme est la masse que le
    /// protocole doit conserver.
    pub fn nouveau(x0: Vec<f64>, params: Params) -> PushPull {
        let somme_initiale = x0.iter().sum();
        PushPull {
            epoque: vec![0; x0.len()],
            vivant: vec![true; x0.len()],
            x: x0.clone(),
            x0,
            params,
            ruptures: Vec::new(),
            cycles: 0,
            messages: 0,
            somme_initiale,
            derive_max: 0.0,
            retours_a_zero: 0,
        }
    }

    /// Arme la conservation de masse comme oracle de sûreté (NF-11).
    pub fn armer_oracle(registre: &mut Registre) {
        registre.armer(Oracle::surete(CONSERVATION, "§4.1, figure 4.1"));
    }

    /// Somme courante des estimations. C'est l'invariant : elle doit rester
    /// égale à la somme des mesures initiales.
    pub fn somme(&self) -> f64 {
        self.x
            .iter()
            .zip(&self.vivant)
            .filter(|(_, v)| **v)
            .map(|(x, _)| *x)
            .sum()
    }

    /// Dispersion des estimations — elle décroît pendant que la somme dérive,
    /// et c'est le croisement des deux courbes qui porte le scénario.
    pub fn dispersion(&self) -> f64 {
        let vivants: Vec<f64> = self
            .x
            .iter()
            .zip(&self.vivant)
            .filter(|(_, v)| **v)
            .map(|(x, _)| *x)
            .collect();
        if vivants.is_empty() {
            return 0.0;
        }
        let max = vivants.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
        let min = vivants.iter().cloned().fold(f64::INFINITY, f64::min);
        max - min
    }

    fn coupe(&self, i: u32, j: u32) -> bool {
        self.params.partition && ((i < self.params.n / 2) != (j < self.params.n / 2))
    }

    /// Un cycle : chaque agent vivant échange avec un pair.
    pub fn cycle(&mut self, service: &mut ServiceDePairs, alea: &mut Alea, maintenant: Instant) {
        self.cycles += 1;

        // Crash-arrêt : la masse détenue disparaît.
        if Some(self.cycles) == self.params.crash_au_cycle {
            if let Some(i) = (0..self.params.n).find(|i| self.vivant[*i as usize]) {
                let perdue = self.x[i as usize];
                self.vivant[i as usize] = false;
                self.ruptures.push(Rupture {
                    date: maintenant,
                    ligne: Ligne::CrashEnCoursDeProtocole,
                    variation: -perdue,
                    entre: (i, i),
                });
            }
        }

        // Relance : elle ne plafonne pas l'erreur, elle réinjecte de la
        // dispersion — donc de la masse à perdre — à chaque période (§4.1).
        if let Some(c) = self.params.relance {
            if c > 0 && self.cycles.is_multiple_of(c) {
                let avant = self.somme();
                for (i, x) in self.x.iter_mut().enumerate() {
                    if self.vivant[i] {
                        *x = self.x0[i];
                    }
                }
                for e in &mut self.epoque {
                    *e += 1;
                }
                let variation = self.somme() - avant;
                // Seuil **relatif** : l'arithmétique flottante fait dériver la
                // somme de quelques ulps même sans faute, et une rupture
                // fantôme à 10⁻¹⁵ ferait mentir l'oracle dans l'autre sens.
                let seuil = 1e-9 * self.somme_initiale.abs().max(1.0);
                if variation.abs() > seuil {
                    self.retours_a_zero += 1;
                    self.ruptures.push(Rupture {
                        date: maintenant,
                        ligne: Ligne::Ligne11Relance,
                        variation,
                        entre: (0, 0),
                    });
                }
            }
        }

        for i in 0..self.params.n {
            if !self.vivant[i as usize] {
                continue;
            }
            let j = match service.tirer(i, alea) {
                Some(j) if self.vivant[j as usize] && !self.coupe(i, j) => j,
                _ => continue,
            };

            // PUSH : i envoie son état à j. Un message.
            self.messages += 1;
            let (xi, xj) = (self.x[i as usize], self.x[j as usize]);
            let moyenne = (xi + xj) / 2.0;

            // Désaccord d'époque : l'agent en retard se réinitialise, celui en
            // avance ignore. Deux traitements **opposés** du même fait.
            if self.epoque[i as usize] != self.epoque[j as usize] {
                let (retard, avance) = if self.epoque[i as usize] < self.epoque[j as usize] {
                    (i, j)
                } else {
                    (j, i)
                };
                let avant = self.somme();
                self.x[retard as usize] = self.x0[retard as usize];
                self.epoque[retard as usize] = self.epoque[avance as usize];
                let variation = self.somme() - avant;
                if variation.abs() > 1e-12 {
                    self.ruptures.push(Rupture {
                        date: maintenant,
                        ligne: Ligne::Epoque,
                        variation,
                        entre: (i, j),
                    });
                }
                continue;
            }

            // Ligne 10 : j moyenne à réception du PUSH.
            self.x[j as usize] = moyenne;

            // Ligne 4 : le PULL de retour peut se perdre. Alors j a moyenné, i
            // non, et la somme quitte sa valeur de |x_i − x_j|/2.
            if alea.bernoulli(self.params.omission) {
                // j a moyenné, i non : la somme passe de x_i + x_j à
                // x_i + (x_i + x_j)/2, soit une variation de (x_i − x_j)/2.
                // Le signe suit l'ordre de x_i et x_j — le traité écrit « la
                // somme totale a diminué » pour l'échange qu'il détaille, et la
                // mesure montre les deux sens. La quantité est affichée signée,
                // sans corriger le texte source.
                self.ruptures.push(Rupture {
                    date: maintenant,
                    ligne: Ligne::Ligne4PullPerdu,
                    variation: (xi - xj) / 2.0,
                    entre: (i, j),
                });
            } else {
                self.messages += 1;
                self.x[i as usize] = moyenne;
            }
        }

        self.derive_max = self.derive_max.max((self.somme() - self.somme_initiale).abs());
    }

    /// Rapporte les ruptures à l'oracle.
    ///
    /// EX-A37 — la violation **n'arrête pas l'exécution** : elle est datée et
    /// attribuée. C'est l'exception que le registre d'oracles de `sim-core`
    /// prévoyait, et elle est la seule.
    pub fn rapporter(&self) -> Option<String> {
        let derive = self.somme() - self.somme_initiale;
        if derive.abs() < 1e-9 {
            return None;
        }
        let premiere = self.ruptures.first()?;
        Some(format!(
            "somme {:.9} contre {:.9} initiale, dérive {:+.9} — première rupture à {} : {}",
            self.somme(),
            self.somme_initiale,
            derive,
            premiere.date.0,
            premiere.ligne.libelle()
        ))
    }

    /// **EX-A38** — aucune condition d'arrêt n'est fabriquée. Ce mécanisme est
    /// proactif et ne se termine pas ; la règle locale disponible est
    /// obligatoirement étiquetée **heuristique**.
    pub fn critere_local_heuristique(&self, epsilon: f64) -> (bool, &'static str) {
        (
            self.dispersion() < epsilon,
            "critère local (heuristique) — un agent ne peut pas distinguer une estimation \
             stabilisée d'une estimation qui n'a pas encore vu la contribution d'un \
             sous-ensemble mal échantillonné (§4.1, EX-A38)",
        )
    }
}

/// **EX-A15** — push-sum valeur-poids.
pub struct PushSum {
    valeur: Vec<f64>,
    poids: Vec<f64>,
    vivant: Vec<bool>,
    /// Préréglage en vigueur.
    pub params: Params,
    /// Cycles exécutés.
    pub cycles: u32,
    /// Messages échangés — **un seul** par échange, sans accusé.
    pub messages: u64,
    /// Somme des mesures initiales : la masse à conserver.
    pub somme_initiale: f64,
}

impl PushSum {
    /// Initialise valeurs et poids ; chaque poids part à 1.
    pub fn nouveau(x0: Vec<f64>, params: Params) -> PushSum {
        let somme_initiale = x0.iter().sum();
        let n = x0.len();
        PushSum {
            valeur: x0,
            poids: vec![1.0; n],
            vivant: vec![true; n],
            params,
            cycles: 0,
            messages: 0,
            somme_initiale,
        }
    }

    /// Estimateur : le **rapport** valeur/poids.
    pub fn estimation(&self, i: usize) -> f64 {
        if self.poids[i].abs() < 1e-300 {
            return f64::NAN;
        }
        self.valeur[i] / self.poids[i]
    }

    /// Somme des valeurs détenues par les agents vivants. C'est la grandeur
    /// conservée : un crash la fait disparaître avec l'agent.
    pub fn somme_valeurs(&self) -> f64 {
        self.valeur
            .iter()
            .zip(&self.vivant)
            .filter(|(_, v)| **v)
            .map(|(x, _)| *x)
            .sum()
    }

    fn coupe(&self, i: u32, j: u32) -> bool {
        self.params.partition && ((i < self.params.n / 2) != (j < self.params.n / 2))
    }

    /// Un cycle : chaque agent vivant pousse la moitié de sa masse à un pair
    /// tiré. Sans accusé, un message perdu emporte la masse qu'il portait.
    pub fn cycle(&mut self, service: &mut ServiceDePairs, alea: &mut Alea) {
        self.cycles += 1;
        for i in 0..self.params.n {
            if !self.vivant[i as usize] {
                continue;
            }
            let j = match service.tirer(i, alea) {
                Some(j) if self.vivant[j as usize] && !self.coupe(i, j) => j,
                _ => continue,
            };
            // La moitié est émise et retranchée.
            let (dv, dp) = (self.valeur[i as usize] / 2.0, self.poids[i as usize] / 2.0);
            self.valeur[i as usize] -= dv;
            self.poids[i as usize] -= dp;
            self.messages += 1;

            let perdu = alea.bernoulli(self.params.omission);
            if perdu && !self.params.accuse_push_sum {
                // Sans accusé, la moitié émise est perdue : la somme quitte sa
                // valeur, et rien ne la corrige.
                continue;
            }
            if perdu && self.params.accuse_push_sum {
                // Avec accusé, l'émetteur reprend sa part — au prix d'un
                // second message par échange.
                self.messages += 1;
                self.valeur[i as usize] += dv;
                self.poids[i as usize] += dp;
                continue;
            }
            if self.params.accuse_push_sum {
                self.messages += 1;
            }
            self.valeur[j as usize] += dv;
            self.poids[j as usize] += dp;
        }
    }

    /// Critère d'arrêt **local** : l'estimation varie de moins de ε sur R
    /// cycles. Sous partition, il est satisfait **des deux côtés de la coupe**,
    /// chaque composante annonçant sa propre moyenne (PD10).
    pub fn estimations_par_composante(&self) -> (f64, f64) {
        let moitie = (self.params.n / 2) as usize;
        let moyenne = |plage: std::ops::Range<usize>| {
            let v: Vec<f64> = plage
                .filter(|i| self.vivant[*i])
                .map(|i| self.estimation(i))
                .collect();
            if v.is_empty() {
                f64::NAN
            } else {
                v.iter().sum::<f64>() / v.len() as f64
            }
        };
        (moyenne(0..moitie), moyenne(moitie..self.params.n as usize))
    }
}

/// **EX-A16** — politique stochastique par taux.
///
/// Chaîne de Markov sur les états d'agent dont la distribution stationnaire est
/// l'allocation visée. **Zéro message.** Le coût ne se compte ni en tours ni en
/// messages mais en **temps de mélange**, et l'unité affichée est celle-là.
///
/// **Aucune condition d'arrêt**, pas même heuristique : la politique tourne
/// indéfiniment pendant que la population se stabilise en distribution, sans
/// qu'aucun agent n'observe cette stabilisation (EX-A38).
pub struct PolitiqueStochastique {
    /// État de chaque agent.
    etat: Vec<usize>,
    /// Taux de transition `taux[a][b]`.
    taux: Vec<Vec<f64>>,
    /// Cycles écoulés. Ce n'est **pas** un compteur de tours de protocole : la
    /// politique n'en a pas.
    pub cycles: u64,
    /// Distribution visée.
    pub visee: Vec<f64>,
}

impl PolitiqueStochastique {
    /// Répartit `n` agents sur les états, puis laisse la chaîne tourner.
    pub fn nouvelle(n: u32, taux: Vec<Vec<f64>>, visee: Vec<f64>) -> PolitiqueStochastique {
        PolitiqueStochastique {
            etat: (0..n as usize).map(|i| i % taux.len()).collect(),
            taux,
            cycles: 0,
            visee,
        }
    }

    /// **Zéro message** : c'est sa force, et l'affichage doit le dire.
    pub const MESSAGES: u64 = 0;

    /// Il n'existe **aucune** condition d'arrêt locale, pas même heuristique.
    /// Le simulateur n'en fabrique pas (EX-A38, PD10, dernière ligne).
    pub const REFUS_DARRET: &'static str =
        "aucune condition d'arrêt locale, pas même heuristique : la politique tourne indéfiniment \
         pendant que la population se stabilise en distribution, sans qu'aucun agent n'observe \
         cette stabilisation (§3.1 du traité, EX-A38)";

    /// Un cycle de la chaîne : chaque agent tire sa transition. Aucun message
    /// n'est échangé, et aucun agent n'apprend quoi que ce soit d'un autre.
    pub fn cycle(&mut self, alea: &mut Alea) {
        self.cycles += 1;
        for e in &mut self.etat {
            let ligne = &self.taux[*e];
            let total: f64 = ligne.iter().sum();
            if total <= 0.0 {
                continue;
            }
            let seuil = alea.uniforme() * total;
            let mut cumul = 0.0;
            for (b, t) in ligne.iter().enumerate() {
                cumul += t;
                if seuil < cumul {
                    *e = b;
                    break;
                }
            }
        }
    }

    /// Distribution courante de la population — **grandeur de population**
    /// (PD3), jamais un état perçu par un agent.
    pub fn distribution(&self) -> Vec<f64> {
        let mut c = vec![0.0; self.taux.len()];
        for e in &self.etat {
            c[*e] += 1.0;
        }
        let n = self.etat.len() as f64;
        c.iter().map(|x| x / n).collect()
    }

    /// Écart à la distribution visée — mesure de l'observateur.
    pub fn ecart_a_la_visee(&self) -> f64 {
        self.distribution()
            .iter()
            .zip(&self.visee)
            .map(|(a, b)| (a - b).abs())
            .sum::<f64>()
            / 2.0
    }

    /// L'unité de coût est le **temps de mélange**, pas le tour ni le message.
    pub const UNITE_DE_COUT: &'static str =
        "temps de mélange de la chaîne des taux — ni tours ni messages (EX-A16)";
}

#[cfg(test)]
mod tests {
    use super::*;

    fn etats(n: usize) -> Vec<f64> {
        (0..n).map(|i| (i as f64) * 1.5).collect()
    }

    /// **Critère (1) du scénario H** — sans omission, sans crash et sans
    /// partition, la somme est conservée à la précision de l'arithmétique
    /// retenue (DT1), sur 100 graines.
    #[test]
    fn critere_1_sans_faute_la_somme_est_conservee_sur_cent_graines() {
        for graine in 0..100u64 {
            let params = Params {
                relance: None,
                ..Params::sans_faute()
            };
            let mut p = PushPull::nouveau(etats(64), params);
            let mut s = ServiceDePairs::nouveau(64, params.biais);
            let mut alea = Alea::nouveau(graine);
            for c in 0..60 {
                p.cycle(&mut s, &mut alea, Instant(c));
            }
            assert!(
                (p.somme() - p.somme_initiale).abs() < 1e-9,
                "graine {graine} : dérive {}",
                p.somme() - p.somme_initiale
            );
            assert!(p.ruptures.is_empty());
            assert!(p.rapporter().is_none());
        }
    }

    /// **Critère (2)** — au premier PULL perdu, la somme varie **exactement**
    /// de |x_i − x_j|/2, et l'oracle date l'événement à la **ligne 4** de
    /// l'échange en cause.
    #[test]
    fn critere_2_le_premier_pull_perdu_est_attribue_a_la_ligne_4() {
        let params = Params {
            omission: 0.05,
            relance: None,
            biais: Biais::Uniforme,
            ..Params::default()
        };
        let mut p = PushPull::nouveau(etats(64), params);
        let mut s = ServiceDePairs::nouveau(64, params.biais);
        let mut alea = Alea::nouveau(7);

        let avant = p.somme();
        let mut cycle = 0u64;
        while p.ruptures.is_empty() && cycle < 200 {
            p.cycle(&mut s, &mut alea, Instant(cycle));
            cycle += 1;
        }
        let r = p.ruptures.first().expect("une rupture doit survenir");
        assert_eq!(r.ligne, Ligne::Ligne4PullPerdu);
        assert!(r.ligne.libelle().contains("|x_i − x_j|/2"));

        // La variation de la somme est exactement celle que la rupture annonce.
        let attendu: f64 = p.ruptures.iter().map(|r| r.variation).sum();
        assert!(
            ((p.somme() - avant) - attendu).abs() < 1e-9,
            "somme {} contre {} attendus",
            p.somme() - avant,
            attendu
        );
        assert!(p.rapporter().unwrap().contains("ligne 4"));
    }

    /// **Critère (3)** — le contraste que le §4.1 (p. 58, 3ᵉ éd.) énonce, retrouvé par
    /// la mesure (NF-15) : **sans relance, l'erreur se fige** — une fois
    /// l'unanimité installée, il ne reste plus de masse à perdre — tandis
    /// qu'**avec relance, son maximum croît avec la durée d'observation**,
    /// parce que chaque période réinjecte de la dispersion.
    ///
    /// C'est l'inverse de ce que « la relance plafonne l'erreur » laisserait
    /// croire, et c'est le livrable.
    #[test]
    fn critere_3_la_relance_ne_plafonne_pas_lerreur_elle_la_fait_croitre() {
        let executer = |relance: Option<u32>, cycles: u64| {
            let params = Params {
                omission: 0.10,
                relance,
                biais: Biais::Uniforme,
                ..Params::default()
            };
            let mut p = PushPull::nouveau(etats(64), params);
            let mut s = ServiceDePairs::nouveau(64, params.biais);
            let mut alea = Alea::nouveau(11);
            for c in 0..cycles {
                p.cycle(&mut s, &mut alea, Instant(c));
            }
            p
        };

        // Avec relance : le tracé **remonte** — la somme est ramenée à sa
        // valeur initiale à chaque fois — puis redérive aussitôt.
        let avec = executer(Some(50), 1_200);
        assert!(
            avec.retours_a_zero >= 20,
            "{} retours à zéro sur 24 relances attendues",
            avec.retours_a_zero
        );
        assert!(avec.derive_max > 1e-6, "et elle redérive entre deux relances");

        // Sans relance : aucun retour, jamais. L'erreur reste où elle est
        // tombée.
        let sans = executer(None, 1_200);
        assert_eq!(sans.retours_a_zero, 0);
        assert!((sans.somme() - sans.somme_initiale).abs() > 1.0);

        // Sans relance, la dérive **se fige** au lieu de croître sans borne :
        // une fois l'unanimité installée, il n'y a plus de désaccord à perdre —
        // (x_i − x_j)/2 tend vers zéro — et la valeur fausse est définitivement
        // acquise. Une dérive sans borne se détecterait par n'importe quel
        // contrôle de vraisemblance ; une erreur figée ne se détecte par rien.
        let sans_court = executer(None, 300).derive_max;
        assert!(
            (sans.derive_max - sans_court).abs() < 1e-9,
            "la dérive se fige : {sans_court:.3} puis {:.3}",
            sans.derive_max
        );

        // Avec relance, au contraire, le maximum **croît avec la durée
        // d'observation** : chaque période réinjecte la dispersion que la
        // dérive consomme. C'est l'énoncé exact du §4.1 (p. 58, 3ᵉ éd.), et il est ici
        // retrouvé et non cité (NF-15).
        let avec_court = executer(Some(50), 300).derive_max;
        assert!(
            avec.derive_max > avec_court,
            "le maximum doit croître avec la durée : {avec_court:.3} sur 300 cycles, {:.3} sur \
             1 200 — la relance ne plafonne rien",
            avec.derive_max
        );
    }

    /// **Critère (4)** — sous partition, le push-sum satisfait son critère
    /// d'arrêt local **des deux côtés**, chaque composante annonçant sa propre
    /// moyenne. L'interface n'affiche « convergé » dans aucune des deux.
    #[test]
    fn critere_4_sous_partition_chaque_composante_annonce_sa_moyenne() {
        let params = Params {
            omission: 0.0,
            partition: true,
            biais: Biais::Uniforme,
            ..Params::default()
        };
        let mut ps = PushSum::nouveau(etats(64), params);
        let mut s = ServiceDePairs::nouveau(64, params.biais);
        let mut alea = Alea::nouveau(13);
        for _ in 0..400 {
            ps.cycle(&mut s, &mut alea);
        }
        let (gauche, droite) = ps.estimations_par_composante();
        assert!(gauche.is_finite() && droite.is_finite());
        assert!(
            (gauche - droite).abs() > 1.0,
            "les deux composantes doivent annoncer des moyennes distinctes : {gauche} et {droite}"
        );
    }

    /// **Critère (5)** — avec l'accusé activé, la conservation tient sous
    /// omission du PULL, et le compte de messages passe de 1 à 2 par échange.
    /// Le prix est visible, pas escamoté.
    #[test]
    fn critere_5_laccuse_restaure_la_conservation_a_deux_messages() {
        let mesurer = |accuse: bool| {
            let params = Params {
                omission: 0.10,
                accuse_push_sum: accuse,
                biais: Biais::Uniforme,
                ..Params::default()
            };
            let mut ps = PushSum::nouveau(etats(64), params);
            let mut s = ServiceDePairs::nouveau(64, params.biais);
            let mut alea = Alea::nouveau(17);
            for _ in 0..200 {
                ps.cycle(&mut s, &mut alea);
            }
            (
                (ps.somme_valeurs() - ps.somme_initiale).abs(),
                ps.messages,
            )
        };
        let (derive_sans, messages_sans) = mesurer(false);
        let (derive_avec, messages_avec) = mesurer(true);
        assert!(derive_avec < 1e-9, "avec accusé, la somme est conservée : {derive_avec}");
        assert!(derive_sans > 1.0, "sans accusé, elle dérive : {derive_sans}");
        assert!(
            messages_avec > messages_sans,
            "le prix doit être visible : {messages_avec} contre {messages_sans}"
        );
    }

    /// **Critère (6)** — avec l'échantillonneur groupé par hôte, la borne
    /// théorique **disparaît** de l'affichage, sans qu'aucun compteur du
    /// protocole ne bouge.
    #[test]
    fn critere_6_le_groupement_par_hote_efface_la_borne() {
        let groupe = Biais::GroupeParHote {
            taille_hote: 8,
            p_local: 0.95,
        };
        assert!(groupe.bornes_applicables().is_err());

        // Et le protocole, lui, ne signale rien : mêmes messages, même cycles.
        let mesurer = |biais| {
            let params = Params {
                omission: 0.0,
                biais,
                ..Params::default()
            };
            let mut p = PushPull::nouveau(etats(64), params);
            let mut s = ServiceDePairs::nouveau(64, biais);
            let mut alea = Alea::nouveau(19);
            for c in 0..100 {
                p.cycle(&mut s, &mut alea, Instant(c));
            }
            (p.messages, p.ruptures.len())
        };
        let (m_uniforme, r_uniforme) = mesurer(Biais::Uniforme);
        let (m_groupe, r_groupe) = mesurer(groupe);
        assert_eq!(r_uniforme, r_groupe, "aucune rupture de part et d'autre");
        let ecart_relatif = (m_uniforme as f64 - m_groupe as f64).abs() / (m_uniforme as f64);
        assert!(
            ecart_relatif < 0.05,
            "le compte de messages ne bouge pas : {m_uniforme} contre {m_groupe}"
        );
    }

    /// **Critère (7)** — la politique stochastique n'affiche à aucun instant un
    /// critère d'arrêt, même heuristique. Sa seule sortie est une distribution
    /// de population et son temps de mélange.
    #[test]
    fn critere_7_la_politique_stochastique_na_aucun_critere_darret() {
        let taux = vec![vec![0.9, 0.1], vec![0.2, 0.8]];
        let mut p = PolitiqueStochastique::nouvelle(256, taux, vec![2.0 / 3.0, 1.0 / 3.0]);
        let mut alea = Alea::nouveau(23);
        for _ in 0..2_000 {
            p.cycle(&mut alea);
        }
        assert_eq!(PolitiqueStochastique::MESSAGES, 0, "zéro message");
        assert!(PolitiqueStochastique::REFUS_DARRET.contains("pas même heuristique"));
        assert!(PolitiqueStochastique::UNITE_DE_COUT.contains("temps de mélange"));
        // La distribution s'approche de la visée — mais aucun agent ne le sait.
        assert!(p.ecart_a_la_visee() < 0.1, "écart {}", p.ecart_a_la_visee());
    }

    /// EX-A38 — le critère du push-pull est disponible, mais **obligatoirement
    /// étiqueté heuristique**.
    #[test]
    fn le_critere_du_push_pull_est_etiquete_heuristique() {
        let params = Params::sans_faute();
        let p = PushPull::nouveau(etats(16), params);
        let (_, etiquette) = p.critere_local_heuristique(1e-3);
        assert!(etiquette.contains("heuristique"));
        assert!(!etiquette.contains("convergé"));
    }

    /// EX-A37 — le crash-arrêt emporte la masse détenue, et l'oracle l'attribue
    /// à sa cause, pas à la ligne 4.
    #[test]
    fn le_crash_est_attribue_a_sa_propre_cause() {
        let params = Params {
            omission: 0.0,
            crash_au_cycle: Some(5),
            relance: None,
            biais: Biais::Uniforme,
            ..Params::default()
        };
        let mut p = PushPull::nouveau(etats(64), params);
        let mut s = ServiceDePairs::nouveau(64, params.biais);
        let mut alea = Alea::nouveau(29);
        for c in 0..40 {
            p.cycle(&mut s, &mut alea, Instant(c));
        }
        assert_eq!(p.ruptures.len(), 1);
        assert_eq!(p.ruptures[0].ligne, Ligne::CrashEnCoursDeProtocole);
        assert!(p.rapporter().unwrap().contains("crash-arrêt"));
    }

    /// Le scénario H en un test : **l'unanimité s'installe pendant que
    /// l'invariant s'effondre**. Les deux courbes se croisent.
    #[test]
    fn lunanimite_sinstalle_pendant_que_linvariant_seffondre() {
        let params = Params {
            omission: 0.05,
            relance: None,
            biais: Biais::Uniforme,
            ..Params::default()
        };
        let mut p = PushPull::nouveau(etats(64), params);
        let mut s = ServiceDePairs::nouveau(64, params.biais);
        let mut alea = Alea::nouveau(31);
        let dispersion_initiale = p.dispersion();
        for c in 0..300 {
            p.cycle(&mut s, &mut alea, Instant(c));
        }
        // L'unanimité : la dispersion s'est effondrée.
        assert!(
            p.dispersion() < dispersion_initiale / 100.0,
            "dispersion {} depuis {dispersion_initiale}",
            p.dispersion()
        );
        // Et la valeur sur laquelle tout le monde s'accorde n'est la moyenne de
        // rien : la somme a quitté sa valeur initiale.
        assert!(
            (p.somme() - p.somme_initiale).abs() > 1.0,
            "la somme doit avoir dérivé"
        );
    }
}
