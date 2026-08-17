//! Diffusion pair à pair adressée, avec entretien de la vue d'appartenance par
//! sondage (EX-A04) — le terme de comparaison du scénario A.
//!
//! Le traité tient trois comptes séparés (§1.3, tableau 3 ; §1.2), et
//! l'interface ne les mélange jamais :
//!
//! 1. **une diffusion** — n − 1 messages en 1 tour ;
//! 2. **l'entretien de la vue** — Θ(n²) messages par période de sondage, sans
//!    équivalent côté journal, le producteur n'ayant pas de destinataire à
//!    connaître ;
//! 3. **un cycle où toute la population dépose** — Θ(n·d) messages.
//!
//! L'entretien de vue est un **détecteur de défaillance** : c'est le premier
//! des cinq exemplaires comptés par PD7, et il utilise l'objet paramétré de
//! `sim-core` plutôt qu'une écriture propre.

use sim_core::alea::Alea;
use sim_core::detecteur::{Detecteur, Etat};
use sim_core::temps::{Duree, Granularite};
use sim_core::ActeurId;

/// Comptes de la maille. Chaque compte a son unité et son énoncé ; il n'existe
/// pas d'accesseur qui les additionne (§1.1, convention de comptage).
#[derive(Clone, Copy, Debug, Default)]
pub struct Comptes {
    /// Messages d'une diffusion : l'émetteur nomme chaque destinataire.
    pub messages_diffusion: u64,
    /// Messages d'entretien de la vue d'appartenance.
    pub messages_entretien: u64,
    /// Messages d'un cycle où toute la population dépose.
    pub messages_depot: u64,
    /// Tours d'une diffusion. Un aller simple suffit : c'est l'avantage de la
    /// maille, et le scénario A doit le montrer avant de montrer son prix.
    pub tours_diffusion: u64,
    /// Périodes de sondage écoulées.
    pub periodes_sondage: u64,
    /// Messages perdus par omission.
    pub messages_perdus: u64,
}

/// La maille pair à pair.
pub struct Maille {
    /// Taille de la population.
    pub n: u32,
    /// Degré de dépôt d — nombre de destinataires nommés par un agent qui
    /// dépose.
    pub degre_depot: u32,
    /// Délai d'un aller simple, en millisecondes.
    pub aller_simple_ms: f64,
    /// Probabilité qu'un message soit perdu.
    pub taux_omission: f64,
    /// Détecteur d'appartenance — l'entretien de vue **est** un détecteur
    /// (PD6, PD12).
    pub detecteur: Detecteur,
    /// Compteurs de messages et de sondages.
    pub comptes: Comptes,
    granularite: Granularite,
}

impl Maille {
    /// Maille neuve, avec son détecteur d'appartenance déjà armé.
    ///
    /// Une période de sondage nulle est **refusée ici**, et non laissée filer
    /// jusqu'à `sim-core` : `Detecteur::nouveau` la refuse à raison au titre du
    /// §4.3 du traité — deux sondes se chevaucheraient et le compte d'échecs
    /// consécutifs ne voudrait plus rien dire —, mais un refus rendu à deux
    /// couches de distance ne dit plus quel réglage le déclenche. Le plancher est
    /// de **deux** tics : l'expiration doit rester strictement plus courte que la
    /// période, et à un seul tic il ne resterait aucune valeur admissible.
    ///
    /// L'écrêtage local rend donc le refus de `sim-core` inatteignable, et le
    /// `expect` ci-dessous documente cet invariant au lieu de propager un
    /// `Result` que rien ne pourrait produire.
    pub fn nouvelle(
        n: u32,
        degre_depot: u32,
        aller_simple_ms: f64,
        taux_omission: f64,
        periode_sondage_ms: f64,
        granularite: Granularite,
    ) -> Maille {
        let periode = Duree(granularite.tics_depuis_ms(periode_sondage_ms).0.max(2));
        let expiration = granularite.tics_depuis_ms(aller_simple_ms * 4.0);
        Maille {
            n,
            degre_depot,
            aller_simple_ms,
            taux_omission,
            detecteur: Detecteur::nouveau(periode, expiration.min(Duree(periode.0 - 1)), 3)
                .expect("période plancher à 2 tics et expiration écrêtée sous la période"),
            comptes: Comptes::default(),
            granularite,
        }
    }

    /// Une diffusion : l'émetteur nomme chacun des n − 1 autres.
    ///
    /// Rend le **temps** au bout duquel toute la population est informée : un
    /// aller simple. C'est la partie que le traité refuse d'escamoter, et le
    /// scénario A l'affiche à côté des deux tours de journal.
    pub fn diffuser(&mut self, alea: &mut Alea) -> Duree {
        let destinataires = self.n.saturating_sub(1) as u64;
        self.comptes.messages_diffusion += destinataires;
        self.comptes.tours_diffusion += 1;
        for _ in 0..destinataires {
            if alea.bernoulli(self.taux_omission) {
                self.comptes.messages_perdus += 1;
            }
        }
        self.granularite.tics_depuis_ms(self.aller_simple_ms)
    }

    /// Une période d'entretien de la vue : chaque agent sonde chacun des
    /// autres. **Θ(n²) messages**, et c'est le terme qui explose (§1.3).
    ///
    /// `vivant` dit, pour chaque agent, s'il répond — le détecteur, lui, ne
    /// voit qu'un délai.
    pub fn entretenir_vue(&mut self, vivants: &[bool], alea: &mut Alea) -> u64 {
        let maintenant = sim_core::temps::Instant(self.comptes.periodes_sondage * self.detecteur.periode.0);
        let mut messages = 0u64;
        for cible in 0..self.n {
            let repond = vivants.get(cible as usize).copied().unwrap_or(true);
            // La latence de réponse est tirée autour de l'aller-retour ; c'est
            // elle, confrontée à l'expiration, qui produit les fausses
            // suspicions (PD12).
            let latence = self
                .granularite
                .tics_depuis_ms(alea.exponentielle(self.aller_simple_ms * 2.0));
            // Chaque sondeur émet : le détecteur compte 2 messages par sonde,
            // et il y a n − 1 sondeurs par cible.
            self.detecteur
                .sonder(ActeurId(cible), repond, latence, maintenant);
            messages += 2 * self.n.saturating_sub(1) as u64;
        }
        self.comptes.messages_entretien += messages;
        self.comptes.periodes_sondage += 1;
        messages
    }

    /// Un cycle où toute la population dépose : **Θ(n·d) messages** (§1.2).
    pub fn cycle_de_depot(&mut self) -> u64 {
        let messages = self.n as u64 * self.degre_depot as u64;
        self.comptes.messages_depot += messages;
        messages
    }

    /// Agents actuellement suspects ou retirés aux yeux du détecteur.
    pub fn suspects(&self) -> u32 {
        (0..self.n)
            .filter(|i| self.detecteur.etat(ActeurId(*i)) != Etat::Sain)
            .count() as u32
    }

    /// Ce que le traité **ne** donne **pas** pour la maille, et que l'interface
    /// n'invente donc pas (scénario A, F1).
    pub const DIAMETRE: &'static str =
        "provenance absente — le traité donne le diamètre du journal (2 en permanence, §1.3) et \
         n'en donne aucun pour la maille";
}

#[cfg(test)]
mod tests {
    use super::*;

    /// SPEC §7, clause 4 — une période de sondage nulle faisait déborder
    /// `periode.0 - 1`, puis échouer l'assertion du §4.3 dans `sim-core`. Elle
    /// est ramenée au plus petit réglage qui garde son sens.
    #[test]
    fn une_periode_de_sondage_nulle_ne_panique_pas() {
        for ms in [0.0, 1e-9, 0.4, 1000.0] {
            let m = Maille::nouvelle(8, 2, 5.0, 0.0, ms, Granularite::Milli);
            assert_eq!(m.n, 8, "période de {ms} ms");
        }
    }

    /// Tableau 3, §1.3 — une diffusion coûte n − 1 messages et **un** tour.
    #[test]
    fn une_diffusion_coute_n_moins_un_messages_en_un_tour() {
        let mut alea = Alea::nouveau(1);
        let mut m = Maille::nouvelle(64, 3, 2.0, 0.0, 1_000.0, Granularite::Micro);
        m.diffuser(&mut alea);
        assert_eq!(m.comptes.messages_diffusion, 63);
        assert_eq!(m.comptes.tours_diffusion, 1);
    }

    /// §1.3 — l'entretien de la vue est en Θ(n²) par période. C'est le compte
    /// qui rend la maille intenable à grand n, et il n'a **aucun équivalent**
    /// côté journal.
    #[test]
    fn lentretien_de_vue_est_quadratique() {
        let mut alea = Alea::nouveau(2);
        let vivants = vec![true; 100];
        let mut petite = Maille::nouvelle(10, 3, 2.0, 0.0, 1_000.0, Granularite::Micro);
        let mut grande = Maille::nouvelle(100, 3, 2.0, 0.0, 1_000.0, Granularite::Micro);
        let a = petite.entretenir_vue(&vivants[..10], &mut alea);
        let b = grande.entretenir_vue(&vivants, &mut alea);
        assert_eq!(a, 10 * 2 * 9);
        assert_eq!(b, 100 * 2 * 99);
        // Population multipliée par 10, coût multiplié par ~100.
        assert!((b as f64 / a as f64) > 90.0);
    }

    /// §1.2 — un cycle où toute la population dépose coûte Θ(n·d).
    #[test]
    fn un_cycle_de_depot_coute_n_fois_d() {
        let mut m = Maille::nouvelle(50, 4, 2.0, 0.0, 1_000.0, Granularite::Micro);
        assert_eq!(m.cycle_de_depot(), 200);
    }

    /// Le temps d'une diffusion est un aller simple — l'avantage de la maille.
    #[test]
    fn le_temps_dune_diffusion_est_un_aller_simple() {
        let mut alea = Alea::nouveau(3);
        let mut m = Maille::nouvelle(64, 3, 2.0, 0.0, 1_000.0, Granularite::Micro);
        assert_eq!(m.diffuser(&mut alea), Duree(2_000));
    }

    /// PD12 — sous charge, l'entretien de vue suspecte des agents vivants. Le
    /// taux n'est pas saisi : il sort de la latence.
    #[test]
    fn sous_charge_lentretien_suspecte_des_agents_vivants() {
        let mut alea = Alea::nouveau(4);
        // Aller simple de 20 ms : l'aller-retour moyen dépasse largement
        // l'expiration, qui vaut 4 allers simples mais est plafonnée par la
        // période.
        let mut m = Maille::nouvelle(20, 3, 20.0, 0.0, 30.0, Granularite::Micro);
        let vivants = vec![true; 20];
        for _ in 0..10 {
            m.entretenir_vue(&vivants, &mut alea);
        }
        let p = m.detecteur.proprietes();
        assert!(p.suspicions > 0, "aucune suspicion portée");
        assert_eq!(
            p.fausses_suspicions, p.suspicions,
            "tous les agents étaient vivants : toutes les suspicions sont fausses"
        );
    }

    /// F1 — l'absence de provenance s'affiche.
    #[test]
    fn le_diametre_de_la_maille_est_declare_absent() {
        assert!(Maille::DIAMETRE.contains("provenance absente"));
    }
}
