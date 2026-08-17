//! Surcoût de format (EX-M11) et idempotence du producteur (EX-M12).
//!
//! Les tailles sont des **valeurs de documentation produit**, donc périssables
//! au sens de l'annexe B. Ce qui n'est pas périssable, c'est leur *forme* : un
//! coût fixe par lot plus un coût marginal par message, et c'est elle qui rend
//! le levier du lot visible (EX-M16).

use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;

/// Surcoût de format d'un lot.
///
/// > 60 octets pour un message seul (contre 34 dans l'ancien format), 753
/// > octets pour un lot de 100 (contre 3 400), soit ≈ 7 octets marginaux par
/// > message additionnel en lot. (§1.3, §2.1 et §7.1 du traité)
///
/// Les trois chiffres sont cohérents entre eux et le modèle les reproduit
/// exactement : 53 + 7 × 1 = 60, et 53 + 7 × 100 = 753.
#[derive(Clone, Copy, Debug, Serialize, Deserialize)]
pub struct Format {
    /// Coût fixe d'un lot, en octets.
    pub entete_lot: u64,
    /// Coût marginal par message additionnel, en octets.
    pub marginal: u64,
    /// Coût par message de l'ancien format, sans mise en lot.
    pub ancien_par_message: u64,
}

impl Default for Format {
    fn default() -> Self {
        Format {
            entete_lot: 53,
            marginal: 7,
            ancien_par_message: 34,
        }
    }
}

impl Format {
    /// Taille d'un lot de `b` messages.
    pub fn octets_lot(&self, b: u64) -> u64 {
        self.entete_lot + self.marginal * b
    }

    /// Taille du même contenu dans l'ancien format, sans mise en lot.
    pub fn octets_ancien(&self, b: u64) -> u64 {
        self.ancien_par_message * b
    }

    /// Taille amortie par message. C'est elle qui décide du levier du lot.
    pub fn octets_par_message(&self, b: u64) -> f64 {
        if b == 0 {
            return 0.0;
        }
        self.octets_lot(b) as f64 / b as f64
    }

    /// Provenance à afficher (F1, F2) : ces valeurs viennent de la
    /// documentation d'un produit, pas d'une mesure du simulateur.
    pub const SOURCE: &'static str =
        "§1.3, §2.1 et §7.1 du traité — valeur de documentation produit, périssable (annexe B)";
}

/// Coût d'écriture d'un lot (EX-M16).
///
/// Le chemin en six étapes — envoi, ajout local, réponse aux k − 1 requêtes de
/// récupération en attente, requêtes suivantes portant le décalage de fin de
/// journal, avancée de la borne de visibilité, accusé — coûte **2k messages par
/// lot et 2 tours en série**.
///
/// Le compteur affiche le coût **par enregistrement**, parce que c'est là que
/// le levier du lot devient visible : à b = 500 et k = 3, 0,012 message par
/// enregistrement. Sans cette division, le compte n'a pas de sens.
#[derive(Clone, Copy, Debug)]
pub struct CoutLot {
    /// Facteur de réplication.
    pub k: u32,
    /// Taille du lot, en enregistrements.
    pub b: u64,
}

impl CoutLot {
    /// Coût d'un lot de `b` enregistrements sur `k` répliques.
    pub fn nouveau(k: u32, b: u64) -> CoutLot {
        CoutLot { k, b }
    }

    /// 2k messages par lot, quelle que soit sa taille.
    pub fn messages(&self) -> u64 {
        2 * self.k as u64
    }

    /// Deux tours **en série** : le lot ne les parallélise pas.
    pub fn tours(&self) -> u64 {
        2
    }

    /// Coût par enregistrement — la seule forme qui rende le levier lisible.
    pub fn messages_par_enregistrement(&self) -> f64 {
        if self.b == 0 {
            return 0.0;
        }
        self.messages() as f64 / self.b as f64
    }
}

/// Livraison idempotente du producteur (EX-M12).
///
/// **La portée est affichée, parce qu'elle est le piège** : l'idempotence vaut
/// à l'intérieur d'une session et d'une partition, et nulle part ailleurs. Un
/// producteur qui redémarre ouvre une nouvelle session, et le dédoublonnage ne
/// traverse pas cette frontière.
#[derive(Clone, Debug, Default)]
pub struct Producteur {
    /// Identifiant de producteur, renouvelé à chaque session.
    pub id_session: u64,
    /// Dernier numéro de séquence accepté, **par partition**.
    sequences: BTreeMap<u32, u64>,
    /// Doublons rejetés **dans** la portée de l'idempotence.
    pub doublons_rejetes: u64,
    /// Doublons acceptés parce qu'ils venaient d'une autre session : c'est le
    /// piège de la portée, et il se compte plutôt que de se taire.
    pub doublons_admis_hors_portee: u64,
}

impl Producteur {
    /// Nouveau producteur. Changer d'`id_session` revient à redémarrer, et
    /// ouvre une portée d'idempotence neuve.
    pub fn nouveau(id_session: u64) -> Producteur {
        Producteur {
            id_session,
            ..Default::default()
        }
    }

    /// Soumet un enregistrement portant `(id_session, partition, sequence)`.
    /// Rend `true` si l'écriture doit avoir lieu, `false` si c'est un doublon
    /// reconnu.
    pub fn accepter(&mut self, id_session: u64, partition: u32, sequence: u64) -> bool {
        if id_session != self.id_session {
            // Hors portée : session différente. Le doublon passe, et le
            // compteur le dit — c'est exactement la limite qu'EX-M12 exige
            // d'afficher plutôt que de laisser croire à une garantie générale.
            self.doublons_admis_hors_portee += 1;
            return true;
        }
        let dernier = self.sequences.get(&partition).copied();
        match dernier {
            Some(d) if sequence <= d => {
                self.doublons_rejetes += 1;
                false
            }
            _ => {
                self.sequences.insert(partition, sequence);
                true
            }
        }
    }

    /// Libellé de portée, affiché avec le commutateur (EX-M12).
    pub const PORTEE: &'static str =
        "idempotence à l'intérieur d'une session et d'une partition (§1.3, §7.1) — un producteur \
         qui redémarre ouvre une session neuve, et le dédoublonnage ne la traverse pas";
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-M11, NF-15 — les trois chiffres du traité doivent être **retrouvés**
    /// par le modèle, pas cités à côté de lui.
    #[test]
    fn le_format_retrouve_les_chiffres_du_traite() {
        let f = Format::default();
        assert_eq!(f.octets_lot(1), 60, "un message seul");
        assert_eq!(f.octets_lot(100), 753, "un lot de 100");
        assert_eq!(f.octets_ancien(100), 3_400, "ancien format, 100 messages");
        assert_eq!(f.marginal, 7, "≈ 7 octets marginaux par message additionnel");
    }

    /// Le levier du lot : le coût amorti par message s'effondre avec b.
    #[test]
    fn le_lot_amortit_son_entete() {
        let f = Format::default();
        assert!((f.octets_par_message(1) - 60.0).abs() < 1e-9);
        assert!((f.octets_par_message(100) - 7.53).abs() < 1e-9);
        assert!(f.octets_par_message(500) < f.octets_par_message(100));
    }

    /// EX-M16, NF-15 — le chiffre du traité est **retrouvé** : 0,012 message
    /// par enregistrement à b = 500 et k = 3.
    #[test]
    fn le_cout_du_lot_retrouve_le_chiffre_du_traite() {
        let c = CoutLot::nouveau(3, 500);
        assert_eq!(c.messages(), 6, "2k messages par lot");
        assert_eq!(c.tours(), 2, "deux tours en série");
        assert!(
            (c.messages_par_enregistrement() - 0.012).abs() < 1e-9,
            "{}",
            c.messages_par_enregistrement()
        );
    }

    /// Le levier du lot : sans mise en lot, chaque enregistrement paie les 2k
    /// messages en entier.
    #[test]
    fn sans_lot_chaque_enregistrement_paie_le_plein_tarif() {
        assert_eq!(CoutLot::nouveau(3, 1).messages_par_enregistrement(), 6.0);
        assert!(CoutLot::nouveau(3, 500).messages_par_enregistrement() < 0.02);
    }

    /// EX-M12 — le dédoublonnage marche à l'intérieur d'une session et d'une
    /// partition.
    #[test]
    fn lidempotence_rejette_un_doublon_dans_la_portee() {
        let mut p = Producteur::nouveau(7);
        assert!(p.accepter(7, 0, 1));
        assert!(p.accepter(7, 0, 2));
        assert!(!p.accepter(7, 0, 2), "même séquence, même partition : doublon");
        assert!(!p.accepter(7, 0, 1), "séquence antérieure : doublon");
        assert_eq!(p.doublons_rejetes, 2);
    }

    /// … et **pas** en dehors. C'est la limite, et elle est comptée plutôt que
    /// tue.
    #[test]
    fn lidempotence_ne_traverse_pas_la_session() {
        let mut p = Producteur::nouveau(7);
        assert!(p.accepter(7, 0, 1));
        assert!(
            p.accepter(8, 0, 1),
            "session différente : le doublon passe, et c'est la portée d'EX-M12"
        );
        assert_eq!(p.doublons_admis_hors_portee, 1);
        assert_eq!(p.doublons_rejetes, 0);
    }

    /// Deux partitions ont deux suites de séquences indépendantes.
    #[test]
    fn lidempotence_est_par_partition() {
        let mut p = Producteur::nouveau(1);
        assert!(p.accepter(1, 0, 5));
        assert!(p.accepter(1, 1, 5), "autre partition, autre suite");
        assert!(!p.accepter(1, 0, 5));
    }

    #[test]
    fn la_portee_est_affichee() {
        assert!(Producteur::PORTEE.contains("session"));
        assert!(Producteur::PORTEE.contains("partition"));
    }
}
