//! `sim-core` — moteur déterministe à événements discrets.
//!
//! Le §3.3 du traité décrit, comme algorithme numéroté, la campagne de
//! simulation que ce crate implante : horloge logique, processus unique, aucune
//! concurrence multifil, réseau et temps et aléa abstraits derrière une
//! interface, graine journalisée, rejeu à l'identique du contre-exemple.
//!
//! Ce que ce crate **ne** connaît **pas**, et ne doit pas apprendre (§5.1 du PRD) : le
//! journal partitionné, les agents, l'interface.
//!
//! ## Règles tenues ici
//!
//! - **PD1** — un seul fil, aucune horloge système, un seul générateur semé,
//!   aucune itération sur table de hachage dans un chemin d'ordonnancement.
//! - **PD2** — un oracle est une sûreté ou une vivacité bornée, jamais autre
//!   chose ([`oracle`]).
//! - **PD6** — le modèle de faute est un objet de première classe, affiché,
//!   versionné, et il nomme ce qu'il ne sait pas produire ([`faute`]).
//! - **PD12** — un détecteur soupçonne, il ne prouve pas ([`detecteur`]).
//! - **DT1** — flottant partout, transcendantes par `libm` : mesuré au banc
//!   `bancs/dt1-flottant`.
//!
//! ## Documentation du dépôt
//!
//! La spécification est `docs/PRD.md`, et tout code d'exigence cité ici —
//! `EX-C01`, `PD1`, `NF-02` — s'y trouve en toutes lettres. `docs/README.md`
//! indexe le reste.

// Un item public sans documentation est refusé : rustdoc est la documentation
// d'interface de ce dépôt, et une interface à demi documentée ne dit pas
// laquelle des deux moitiés manque.
#![deny(missing_docs)]
#![deny(rustdoc::broken_intra_doc_links)]

pub mod alea;
pub mod couverture;
pub mod detecteur;
pub mod famille;
pub mod faute;
pub mod graphe;
pub mod horloge;
pub mod moteur;
pub mod oracle;
pub mod registre;
pub mod service;
pub mod temps;
pub mod verification;

use serde::{Deserialize, Serialize};

/// Version du crate, écrite dans tout export (NF-03).
pub const VERSION: &str = env!("CARGO_PKG_VERSION");

/// Constante de départ de FNV-1a 64 bits.
///
/// L'empreinte du produit ne vient pas du traité : c'est un choix, retenu parce
/// qu'il n'a besoin d'aucune dépendance et se réimplante à l'identique sur toute
/// cible (NF-02). Les deux bancs de `bancs/` la réécrivent, et c'est délibéré —
/// le banc DT1 ne doit dépendre de rien, c'est sa méthode.
pub(crate) const FNV_DEPART: u64 = 0xcbf2_9ce4_8422_2325;
/// Nombre premier de FNV-1a 64 bits.
pub(crate) const FNV_PREMIER: u64 = 0x0000_0100_0000_01b3;

/// Absorbe des octets dans un hachage FNV-1a.
///
/// Les deux empreintes de cette crate passent par ici : [`Config::hachage`],
/// qui avale la sérialisation JSON, et [`moteur::Trace::absorber`], qui avale
/// les huit octets de poids faible d'un `u64`. ⚠ *Le commentaire de `hachage`
/// affirmait le contraire — « les réunir changerait toutes les empreintes de
/// NF-03 » — et c'est faux : les deux absorbaient déjà **octet par octet**,
/// `(x >> 8i) & 0xff` étant exactement `x.to_le_bytes()[i]`. Ce qui les
/// distingue est ce qu'elles donnent à manger, jamais la façon de manger.*
/// Mesuré : les six empreintes du banc de parité sont inchangées.
pub(crate) fn absorber_octets(mut h: u64, octets: &[u8]) -> u64 {
    for octet in octets {
        h ^= u64::from(*octet);
        h = h.wrapping_mul(FNV_PREMIER);
    }
    h
}

/// Identifiant d'un acteur. Un acteur est ce que le moteur sait dater ; il peut
/// être un agent, une partition, ou le milieu lui-même — `sim-core` ne tranche
/// pas, puisqu'il ne les connaît pas.
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Debug, Default, Serialize, Deserialize)]
pub struct ActeurId(pub u32);

/// Configuration d'une exécution, journalisée dès l'étape 1 de l'algorithme 3.3
/// du §3.3 : avec la graine, elle suffit au rejeu à l'identique.
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Config {
    /// Graine du générateur unique. Avec le reste de cette structure, elle
    /// suffit au rejeu bit à bit (NF-01).
    pub graine: u64,
    /// Unité du temps logique (DT10).
    pub granularite: temps::Granularite,
    /// Modèle de faute actif. Deux exécutions de même graine sous deux modèles
    /// différents ne mesurent pas la même chose, et le hachage le montre.
    pub fautes: faute::ModeleFaute,
    /// Plafond d'événements de l'exécution.
    pub evenements_max: u64,
    /// Plafond de temps de calcul, en secondes-cœur. `None` : aucun.
    pub secondes_coeur_max: Option<f64>,
    /// Nom du scénario. DT10 : la granularité étant réglée par scénario, deux
    /// exécutions de scénarios différents ne se comparent pas — le hachage le
    /// rend visible plutôt que de l'interdire séparément.
    pub scenario: String,
}

impl Config {
    /// Hachage de la configuration (NF-03). Calculé sur la sérialisation JSON,
    /// dont l'ordre des champs suit la déclaration et non une table de hachage.
    ///
    /// # Panics
    ///
    /// Si la configuration porte un flottant non fini. JSON n'a ni `NaN` ni
    /// infini, et `serde_json` refuse de les écrire : une `Config` construite en
    /// mémoire avec `secondes_coeur_max: Some(f64::INFINITY)` ou un taux de
    /// faute `NaN` fait donc paniquer ici, et par contrecoup dans
    /// [`Config::entete`] et [`Config::verifier_rejeu`]. Une configuration lue
    /// d'un fichier ne peut pas être dans cet état, la même règle JSON valant à
    /// la lecture.
    pub fn hachage(&self) -> u64 {
        let json = serde_json::to_string(self).expect("configuration sérialisable");
        absorber_octets(FNV_DEPART, json.as_bytes())
    }

    /// En-tête écrit dans tout export (NF-03).
    pub fn entete(&self) -> String {
        format!(
            "sim-core {VERSION} | modèle de faute v{} | graine {} | configuration {:016x} | \
             granularité {} | scénario {}",
            faute::VERSION_MODELE,
            self.graine,
            self.hachage(),
            self.granularite.unite(),
            self.scenario,
        )
    }

    /// NF-03 — un rejeu sur une version différente est **refusé**, pas tenté.
    pub fn verifier_rejeu(&self, version_export: &str, hachage_export: u64) -> Result<(), String> {
        if version_export != VERSION {
            return Err(format!(
                "rejeu refusé : export produit par sim-core {version_export}, binaire courant \
                 {VERSION}. NF-03 refuse le rejeu inter-versions au lieu de le tenter — un \
                 entrelacement identique n'est garanti que sur la même version du binaire."
            ));
        }
        if hachage_export != self.hachage() {
            return Err(format!(
                // Les deux hachages dans la même base : l'attendu s'écrivait en
                // hexadécimal et le fourni en décimal, de sorte que le message
                // donnait deux nombres qu'aucun lecteur ne pouvait comparer.
                "rejeu refusé : hachage de configuration {:016x} attendu, {hachage_export:016x} \
                 fourni. La graine seule ne suffit pas : le §3.3 journalise la graine **et** la \
                 configuration complète.",
                self.hachage()
            ));
        }
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use temps::Granularite;

    fn config() -> Config {
        Config {
            graine: 42,
            granularite: Granularite::Milli,
            fautes: faute::ModeleFaute::default(),
            evenements_max: 1_000,
            secondes_coeur_max: None,
            scenario: "B".to_string(),
        }
    }

    #[test]
    fn le_hachage_change_avec_la_configuration() {
        let a = config();
        let mut b = config();
        b.graine = 43;
        assert_ne!(a.hachage(), b.hachage());

        // DT10 : la granularité fait partie de l'identité de l'exécution.
        let mut c = config();
        c.granularite = Granularite::Micro;
        assert_ne!(a.hachage(), c.hachage());

        // PD6 : le modèle de faute aussi. Deux exécutions de même graine sous
        // deux modèles différents ne mesurent pas la même chose.
        let mut d = config();
        d.fautes.omission = 0.01;
        assert_ne!(a.hachage(), d.hachage());
    }

    #[test]
    fn le_hachage_est_stable() {
        assert_eq!(config().hachage(), config().hachage());
    }

    /// NF-03 — le rejeu inter-versions est refusé, et le message dit pourquoi.
    #[test]
    fn le_rejeu_inter_versions_est_refuse() {
        let c = config();
        let h = c.hachage();
        assert!(c.verifier_rejeu(VERSION, h).is_ok());
        let e = c.verifier_rejeu("0.0.0", h).unwrap_err();
        assert!(e.contains("NF-03"), "{e}");
    }

    #[test]
    fn le_rejeu_dune_autre_configuration_est_refuse() {
        let c = config();
        let e = c.verifier_rejeu(VERSION, 0).unwrap_err();
        // Les deux hachages du message se comparent : même base, même largeur.
        assert!(e.contains(&format!("{:016x} attendu", c.hachage())), "{e}");
        assert!(e.contains("0000000000000000 fourni"), "{e}");
    }

    #[test]
    fn lentete_porte_version_graine_et_hachage() {
        let e = config().entete();
        assert!(e.contains(VERSION));
        assert!(e.contains("graine 42"));
        assert!(e.contains("modèle de faute v1"));
    }
}
