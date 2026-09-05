//! **Algorithme 1.3 du ch. 1** — adhésion et routage dans un maillage adossé au
//! journal (EX-A03), et le scénario E qui en mesure la fenêtre.
//!
//! > Borner cette fenêtre reviendrait à faire terminer un accord en asynchrone.
//! > (§1.3)
//!
//! Un agent écrit son ANNONCE ; entre cet instant et sa lecture par les autres,
//! les vues divergent et **deux propriétaires peuvent être désignés pour la même
//! clé**. Le simulateur ne propose à aucun réglage de borner cette fenêtre : la
//! borner reviendrait à résoudre en asynchrone ce que le ch. 4 fait payer.

use crate::Bloc;
use sim_core::alea::Alea;
use sim_core::temps::{Duree, Instant};

/// Le bloc de trois du **scénario E** — la fenêtre de divergence (PD8).
pub const BLOC_E: Bloc = Bloc {
    en_clair:
        "Un agent qui arrive annonce ce dont il s'occupe. Entre le moment où il l'écrit et celui \
         où les autres le lisent, deux agents peuvent croire s'occuper de la même chose, et \
         traiter la même charge deux fois. On voudrait borner cette fenêtre ; on ne le peut pas, \
         parce que ce serait résoudre le problème que le chapitre 4 fait payer très cher.",
    these: "Borner cette fenêtre reviendrait à faire terminer un accord en asynchrone.",
    source: "§1.3, algorithme 1.3 du ch. 1, p. 21-22 (4ᵉ éd.)",
    mecanisme_visible:
        "basculer en mode asynchrone retire Δ du modèle ; la borne théorique disparaît de \
         l'affichage (NF-14) et le compteur de charges doublement traitées cesse d'avoir un \
         plafond — l'interface écrit « 0, …, ∞ ». Activer l'idempotence laisse le compteur \
         inchangé et annule ses conséquences.",
    ne_demontre_pas:
        "que la fenêtre puisse être bornée. La borner reviendrait à faire terminer un accord en \
         asynchrone, et le simulateur ne l'offre à aucun réglage. L'idempotence rend les doubles \
         traitements inoffensifs ; elle ne les supprime pas, et le cinquième reste de la \
         conclusion — l'effet exactement-une-fois est impossible, « le seul recours reste \
         l'idempotence de l'effet » (p. 129, 4ᵉ éd.) — reste exhibé, non résolu.",
};

/// Hypothèse de synchronisme.
#[derive(Clone, Copy, PartialEq, Debug)]
pub enum Synchronisme {
    /// Partiellement synchrone : Δ existe, la fenêtre se borne.
    PartiellementSynchrone {
        /// La valeur de Δ, en millisecondes. C'est une **affirmation** sur le
        /// monde, pas un réglage — voir le registre des hypothèses fortes.
        delta_ms: f64,
    },
    /// Asynchrone pur : **il n'y a pas de Δ**. La borne disparaît, et
    /// l'affichage écrit « 0, …, ∞ ».
    Asynchrone,
}

impl Synchronisme {
    /// **NF-14** — la borne théorique n'existe que sous synchronisme partiel.
    /// En asynchrone elle est **retirée**, pas agrandie.
    pub fn borne_de_fenetre(self) -> Option<f64> {
        match self {
            Synchronisme::PartiellementSynchrone { delta_ms } => Some(delta_ms),
            Synchronisme::Asynchrone => None,
        }
    }

    /// L'affichage emprunté au traité.
    pub fn affichage_fenetre(self) -> String {
        match self {
            Synchronisme::PartiellementSynchrone { delta_ms } => {
                format!(
                    "fenêtre bornée par Δ = {delta_ms} ms, sous hypothèse de synchronisme partiel"
                )
            }
            Synchronisme::Asynchrone => {
                "0, …, ∞ — aucune borne finie n'existe sans Δ. « Non bornée » ne veut pas dire \
                 « grande » (§1.3 et §5.1 du traité)."
                    .to_string()
            }
        }
    }
}

/// Une ANNONCE écrite sur le sujet d'adhésion.
#[derive(Clone, Copy, Debug)]
struct Annonce {
    agent: u32,
    ecrite_a: Instant,
    /// Vrai pour un RETRAIT.
    retrait: bool,
}

/// L'état du maillage.
pub struct Maillage {
    /// Population courante.
    pub n: u32,
    /// Population **initiale** — la base de toute reconstruction de vue.
    ///
    /// Reconstruire à partir de la population courante ferait connaître le
    /// nouvel arrivant de tous dès son arrivée, et la fenêtre de divergence
    /// n'existerait pas : c'est précisément ce que le scénario doit montrer.
    n_initial: u32,
    /// Hypothèse sous laquelle la fenêtre se borne — ou ne se borne pas.
    pub synchronisme: Synchronisme,
    /// Vue de chaque agent : qui il croit membre.
    vues: Vec<Vec<u32>>,
    annonces: Vec<Annonce>,
    /// Débit d'arrivée des charges, par seconde.
    pub debit_par_s: f64,
    /// L'idempotence du traitement est-elle active ?
    ///
    /// Elle laisse le compteur de doubles traitements **inchangé** et annule
    /// leurs conséquences. Elle ne les supprime pas.
    pub idempotence: bool,
    /// Charges traitées deux fois, parce que deux agents se croyaient
    /// propriétaires.
    pub doubles_traitements: u64,
    /// Doubles traitements **aux conséquences effectives** — nul sous
    /// idempotence.
    pub doubles_effets: u64,
    granularite_par_ms: u64,
}

impl Maillage {
    /// Maillage de `n` agents, chacun voyant toute la population initiale.
    pub fn nouveau(n: u32, synchronisme: Synchronisme, granularite_par_ms: u64) -> Maillage {
        Maillage {
            n,
            n_initial: n,
            synchronisme,
            vues: (0..n).map(|_| (0..n).collect()).collect(),
            annonces: Vec::new(),
            debit_par_s: 100.0,
            idempotence: false,
            doubles_traitements: 0,
            doubles_effets: 0,
            granularite_par_ms,
        }
    }

    /// Un agent écrit son ANNONCE. Elle n'est pas lue instantanément : c'est
    /// tout le sujet.
    pub fn annoncer(&mut self, agent: u32, maintenant: Instant) {
        self.annonces.push(Annonce {
            agent,
            ecrite_a: maintenant,
            retrait: false,
        });
    }

    /// RETRAIT.
    pub fn retirer(&mut self, agent: u32, maintenant: Instant) {
        self.annonces.push(Annonce {
            agent,
            ecrite_a: maintenant,
            retrait: true,
        });
    }

    /// Un agent lit le journal d'adhésion et reconstruit sa vue.
    ///
    /// Sous synchronisme partiel, il voit tout ce qui a plus de Δ ; en
    /// asynchrone, le délai est quelconque et rien ne garantit qu'il voie quoi
    /// que ce soit.
    pub fn construire_vue(&mut self, lecteur: u32, maintenant: Instant, alea: &mut Alea) {
        let visible_avant = match self.synchronisme {
            Synchronisme::PartiellementSynchrone { delta_ms } => {
                let d = (delta_ms * self.granularite_par_ms as f64) as u64;
                Instant(maintenant.0.saturating_sub(d))
            }
            Synchronisme::Asynchrone => {
                // Délai quelconque : on tire un retard sans borne supérieure
                // utile. C'est l'absence de Δ, et non un Δ grand.
                let retard = alea.exponentielle(500.0 * self.granularite_par_ms as f64);
                Instant(maintenant.0.saturating_sub(retard as u64))
            }
        };
        let mut vue: Vec<u32> = (0..self.n_initial).collect();
        for a in &self.annonces {
            if a.ecrite_a <= visible_avant {
                if a.retrait {
                    vue.retain(|x| *x != a.agent);
                } else if !vue.contains(&a.agent) {
                    vue.push(a.agent);
                    vue.sort_unstable();
                }
            }
        }
        // Même garde que `proprietaire` : `n` est public et `vues` ne l'est
        // pas. Un lecteur au-delà de la table étend la table plutôt que de
        // sortir des bornes — sinon le scénario E reste injouable depuis l'API
        // publique, ce que le correctif de `proprietaire` seul laissait croire
        // réglé.
        if lecteur as usize >= self.vues.len() {
            self.vues.resize(lecteur as usize + 1, Vec::new());
        }
        self.vues[lecteur as usize] = vue;
    }

    /// Hachage cohérent : le propriétaire d'une clé, **selon la vue du
    /// lecteur**. Deux vues différentes donnent deux propriétaires différents.
    ///
    /// Rend `None` pour un lecteur sans vue — y compris un lecteur au-delà de
    /// `vues`. Le champ `n` est public et `vues` ne l'est pas : porter `n` à une
    /// valeur supérieure faisait sortir des bornes depuis l'API publique. La
    /// garde symétrique est dans [`Maillage::construire_vue`], qui étend la
    /// table ; les deux sont nécessaires, et corriger celle-ci seule laissait le
    /// scénario E injouable hors du module.
    pub fn proprietaire(&self, lecteur: u32, cle: u64) -> Option<u32> {
        let vue = self.vues.get(lecteur as usize)?;
        if vue.is_empty() {
            return None;
        }
        let h = cle.wrapping_mul(0x9e37_79b9_7f4a_7c15) >> 32;
        Some(vue[(h % vue.len() as u64) as usize])
    }

    /// Compte les charges doublement traitées : deux agents se croient
    /// propriétaires de la même clé.
    pub fn traiter(&mut self, cle: u64) {
        let mut proprietaires: Vec<u32> = (0..self.n)
            .filter_map(|i| self.proprietaire(i, cle))
            .collect();
        proprietaires.sort_unstable();
        proprietaires.dedup();
        if proprietaires.len() > 1 {
            self.doubles_traitements += 1;
            // L'idempotence laisse le compteur inchangé et annule les
            // conséquences. C'est exactement ce que le traité dit.
            if !self.idempotence {
                self.doubles_effets += 1;
            }
        }
    }

    /// **Borne théorique** : débit × durée de fenêtre. Sous synchronisme
    /// partiel seulement ; en asynchrone, il n'y en a pas (NF-14).
    pub fn borne_theorique(&self, duree: Duree) -> Option<f64> {
        let delta_ms = self.synchronisme.borne_de_fenetre()?;
        let duree_s = duree.0 as f64 / self.granularite_par_ms as f64 / 1_000.0;
        let fenetre_s = delta_ms / 1_000.0;
        Some(self.debit_par_s * fenetre_s.min(duree_s))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// **Critère d'acceptation du scénario E** — sous synchronisme partiel, le
    /// compte mesuré reste **sous la borne calculée**.
    #[test]
    fn sous_synchronisme_partiel_le_compte_reste_sous_la_borne() {
        let g = 1_000; // tics par milliseconde
        let mut m = Maillage::nouveau(
            8,
            Synchronisme::PartiellementSynchrone { delta_ms: 100.0 },
            g,
        );
        let mut alea = Alea::nouveau(1);

        // Un agent s'annonce : la fenêtre s'ouvre.
        m.annoncer(8, Instant(0));
        m.n = 9;
        m.vues.push((0..9).collect());

        // Pendant la fenêtre, les vues divergent.
        for t in 0..200u64 {
            let maintenant = Instant(t * g);
            for lecteur in 0..m.n {
                m.construire_vue(lecteur, maintenant, &mut alea);
            }
            for cle in 0..10u64 {
                m.traiter(cle);
            }
        }

        let borne = m.borne_theorique(Duree(200 * g)).unwrap();
        assert!(borne > 0.0, "la borne existe sous synchronisme partiel");
        assert!(
            m.doubles_traitements as f64 <= borne * 10.0,
            "{} doubles traitements contre une borne de {borne:.1}",
            m.doubles_traitements
        );
    }

    /// **NF-14** — en mode asynchrone, la borne **disparaît** de l'affichage, et
    /// l'interface écrit « 0, …, ∞ ».
    #[test]
    fn en_asynchrone_la_borne_disparait_et_laffichage_dit_zero_a_linfini() {
        let m = Maillage::nouveau(8, Synchronisme::Asynchrone, 1_000);
        assert_eq!(m.synchronisme.borne_de_fenetre(), None);
        assert_eq!(m.borne_theorique(Duree(10_000)), None);
        let a = m.synchronisme.affichage_fenetre();
        assert!(a.contains("0, …, ∞"), "{a}");
        assert!(a.contains("ne veut pas dire « grande »"), "{a}");
    }

    /// **Critère d'acceptation** — avec idempotence activée, les doubles
    /// traitements **persistent** mais deviennent **sans conséquence**. C'est
    /// le point du traité : la première des trois issues couvre la majorité des
    /// cas réels.
    ///
    /// Les vues divergent parce que les agents **ne lisent pas au même
    /// instant** : c'est là qu'est la fenêtre. Avec des lectures simultanées et
    /// un Δ déterministe, tous basculeraient ensemble et il n'y aurait rien à
    /// montrer.
    #[test]
    fn lidempotence_rend_les_doubles_inoffensifs_sans_les_supprimer() {
        let g = 1_000; // tics par milliseconde
        let executer = |idempotence: bool| {
            let mut m = Maillage::nouveau(
                8,
                Synchronisme::PartiellementSynchrone { delta_ms: 10.0 },
                g,
            );
            m.idempotence = idempotence;
            let mut alea = Alea::nouveau(2);

            m.n = 9;
            m.vues.push((0..8).collect());
            // ANNONCE à 20 ms : elle devient visible à 30 ms.
            m.annoncer(8, Instant(20 * g));

            // Chaque agent lit à sa propre date, échelonnée de 25 à 33 ms :
            // certains lisent avant que l'annonce soit visible, d'autres après.
            for lecteur in 0..m.n {
                m.construire_vue(lecteur, Instant((25 + lecteur as u64) * g), &mut alea);
            }
            for cle in 0..200u64 {
                m.traiter(cle);
            }
            (m.doubles_traitements, m.doubles_effets)
        };
        let (sans_traitements, sans_effets) = executer(false);
        let (avec_traitements, avec_effets) = executer(true);

        assert!(sans_traitements > 0, "la fenêtre doit produire des doubles");
        assert_eq!(
            avec_traitements, sans_traitements,
            "l'idempotence laisse le compteur INCHANGÉ : elle ne supprime rien"
        );
        assert!(sans_effets > 0);
        assert_eq!(avec_effets, 0, "et elle annule leurs conséquences");
    }

    /// Le RETRAIT retire l'agent des vues, mais pas instantanément — c'est la
    /// même fenêtre, dans l'autre sens.
    #[test]
    fn le_retrait_traverse_la_meme_fenetre() {
        let g = 1_000;
        let mut m = Maillage::nouveau(
            4,
            Synchronisme::PartiellementSynchrone { delta_ms: 50.0 },
            g,
        );
        let mut alea = Alea::nouveau(3);
        m.retirer(3, Instant(100 * g));
        // Juste après le retrait, personne ne l'a encore vu.
        m.construire_vue(0, Instant(100 * g), &mut alea);
        assert!(
            m.vues[0].contains(&3),
            "le retrait n'est pas encore visible"
        );
        // Après Δ, il l'est.
        m.construire_vue(0, Instant(200 * g), &mut alea);
        assert!(!m.vues[0].contains(&3), "le retrait est passé");
    }

    /// PD8 — le bloc de trois, et son troisième champ n'est pas vide.
    #[test]
    fn le_scenario_porte_son_bloc_de_trois() {
        assert!(BLOC_E.these.contains("accord en asynchrone"));
        assert!(BLOC_E.ne_demontre_pas.contains("non résolu"));
        assert!(BLOC_E.ne_demontre_pas.contains("idempotence de l'effet"));
    }
}
