//! Oracles — et la séparation que PD2 refuse de laisser s'effacer.
//!
//! > Un cahier des charges qui mêle S1 et L1 sans les nommer produit des
//! > exigences dont la moitié est non testable. (§3.2)
//!
//! Un oracle est donc **soit** une sûreté, réfutable par une trace finie,
//! **soit** une vivacité **bornée**, qui ne s'énonce jamais sans sa condition.
//! Il n'y a pas de troisième cas, et la vivacité non bornée n'est pas
//! représentable : EX-C11 la refuse à la construction.

use crate::temps::{Duree, Instant};
use std::collections::BTreeMap;

/// Classe d'un oracle (PD2).
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Classe {
    /// **`[S]`** — réfutable par une trace finie ; le moniteur lève l'alerte à
    /// l'instant de la violation.
    Surete,
    /// **`[L]`** — vivacité **bornée**. L'horizon est la condition sans laquelle
    /// l'énoncé n'est pas testable ; il n'existe pas de constructeur qui
    /// l'omette.
    VivaciteBornee {
        /// Délai au-delà duquel l'attente est une violation.
        horizon: Duree,
    },
}

/// Portée d'évaluation (PD10).
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Portee {
    /// Évalué **hors du monde perçu par les agents**. C'est un privilège de
    /// l'observateur, et l'interface doit dire qu'aucun agent ne dispose de
    /// cette information (§8.3, EX-A51).
    Globale,
    /// Évalué sur la perception d'un seul agent. PD10 : un tel prédicat n'est
    /// **jamais** présenté comme un état de l'essaim, et il porte son
    /// contre-exemple.
    Locale {
        /// Ce que le prédicat *paraît* dire, et qui est faux.
        contre_exemple: &'static str,
        /// Le réglage qui le met en défaut — livré, pas décrit (EX-A39).
        reglage_fautif: &'static str,
    },
}

/// Un oracle déclaré.
#[derive(Clone, Debug)]
pub struct Oracle {
    /// Nom stable, qui sert de clé dans le registre et s'affiche tel quel.
    pub nom: &'static str,
    /// Sûreté ou vivacité bornée — il n'y a pas de troisième cas (PD2).
    pub classe: Classe,
    /// Globale ou locale. Une portée locale ne certifie jamais l'essaim (PD10).
    pub portee: Portee,
    /// Référence de section **et de page** dans le traité (F2). Une grandeur
    /// sans provenance est traitée comme une faute de rédaction.
    pub source: &'static str,
}

impl Oracle {
    /// Oracle de sûreté à portée globale.
    pub fn surete(nom: &'static str, source: &'static str) -> Oracle {
        Oracle {
            nom,
            classe: Classe::Surete,
            portee: Portee::Globale,
            source,
        }
    }

    /// Oracle de vivacité **bornée**. L'horizon est obligatoire par signature :
    /// c'est la moitié « refusé à la compilation » d'EX-C11.
    pub fn vivacite_bornee(nom: &'static str, horizon: Duree, source: &'static str) -> Oracle {
        Oracle {
            nom,
            classe: Classe::VivaciteBornee { horizon },
            portee: Portee::Globale,
            source,
        }
    }

    /// Marque l'oracle comme évalué sur la perception d'un seul agent (PD10).
    pub fn local(mut self, contre_exemple: &'static str, reglage_fautif: &'static str) -> Oracle {
        self.portee = Portee::Locale {
            contre_exemple,
            reglage_fautif,
        };
        self
    }

    /// Construction depuis une déclaration chargée — l'autre moitié d'EX-C11,
    /// celle qui refuse « au chargement, avec un message citant §3.2 ».
    pub fn depuis_declaration(
        nom: &'static str,
        classe: &str,
        horizon: Option<Duree>,
        source: &'static str,
    ) -> Result<Oracle, String> {
        match (classe, horizon) {
            ("surete", None) => Ok(Oracle::surete(nom, source)),
            // Une sûreté assortie d'un horizon mêle S1 et L1 — précisément ce
            // que PD2 refuse. L'accepter en jetant l'horizon en silence fait
            // pire : `attendre()` sur cet oracle deviendrait un non-événement.
            ("surete", Some(h)) => Err(format!(
                "oracle « {nom} » refusé : une sûreté ne porte pas d'horizon, et celui-ci en \
                 déclare un ({} tics). §3.2 — un énoncé qui mêle S1 et L1 est à moitié non \
                 testable. Déclarez « vivacite » avec cet horizon, ou retirez-le.",
                h.0
            )),
            ("vivacite", Some(h)) => Ok(Oracle::vivacite_bornee(nom, h, source)),
            ("vivacite", None) => Err(format!(
                "oracle « {nom} » refusé : une vivacité sans horizon n'est réfutable par aucune \
                 exécution finie. §3.2 — une vivacité ne s'énonce jamais sans sa condition, \
                 détecteur de défaillance ou borne Δ. Déclarez un horizon, ou déclarez une sûreté."
            )),
            (autre, _) => Err(format!(
                "oracle « {nom} » refusé : classe « {autre} » inconnue. §3.2 impose de nommer S1 \
                 ou L1 ; une exigence qui les mêle est à moitié non testable."
            )),
        }
    }

    /// Nom affiché. PD10 : un prédicat local ne s'affiche jamais sous le nom
    /// de la propriété globale qu'il approche.
    pub fn nom_affiche(&self) -> String {
        match self.portee {
            Portee::Globale => self.nom.to_string(),
            Portee::Locale { .. } => format!("{} — critère local (heuristique)", self.nom),
        }
    }
}

/// Une violation constatée.
#[derive(Clone, Debug)]
pub struct Violation {
    /// Nom de l'oracle violé.
    pub oracle: &'static str,
    /// Instant **exact** de la violation (EX-C09), et non celui de sa détection.
    pub date: Instant,
    /// Ce qui a été constaté, en clair.
    pub details: String,
}

/// Une vivacité bornée en attente de satisfaction.
#[derive(Clone, Debug)]
struct Attente {
    oracle: &'static str,
    echeance: Instant,
    details: String,
}

/// Le registre des oracles armés d'une exécution.
///
/// Les oracles sont **évalués par l'appelant** et rapportés ici : `sim-core`
/// ne connaît ni les agents ni le milieu (§5.1), il ne peut donc pas évaluer
/// un prédicat sur eux. Ce qu'il tient, c'est la déclaration, la classe, le
/// délai d'une vivacité et l'instant exact d'une violation.
#[derive(Default)]
pub struct Registre {
    oracles: Vec<Oracle>,
    attentes: Vec<Attente>,
    violations: Vec<Violation>,
}

impl Registre {
    /// Registre vide : aucun oracle armé.
    pub fn nouveau() -> Self {
        Registre::default()
    }

    /// Arme un oracle pour la durée de l'exécution. NF-11 veut les invariants
    /// du milieu armés en permanence dans les tests — coûteux, mais exacts.
    pub fn armer(&mut self, oracle: Oracle) {
        self.oracles.push(oracle);
    }

    /// Les oracles armés, dans l'ordre d'armement.
    pub fn oracles(&self) -> &[Oracle] {
        &self.oracles
    }

    /// Les violations constatées. Vide ne veut pas dire « aucune violation
    /// possible » : cela veut dire qu'aucune n'a été **vue** (§8.4).
    pub fn violations(&self) -> &[Violation] {
        &self.violations
    }

    fn classe(&self, nom: &str) -> Option<Classe> {
        self.oracles.iter().find(|o| o.nom == nom).map(|o| o.classe)
    }

    /// Signale la violation d'une sûreté. EX-C09 : l'exécution s'arrête, et la
    /// graine plus la configuration suffisent au rejeu.
    ///
    /// EX-A37 (phase 3) demandera une exception pour la conservation de masse,
    /// dont la violation se date et s'attribue sans arrêter. Elle n'est pas
    /// anticipée ici : PD7 compte les exemplaires avant de factoriser, et il
    /// n'y en a qu'un.
    ///
    /// # Panics
    ///
    /// Si `nom` n'a pas été armé. `assert!` et non `debug_assert!` : la suite de
    /// tests du dépôt tourne en `--release`, où un `debug_assert!` disparaît —
    /// le garde-fou n'existait donc que dans le mode que personne n'exécute.
    pub fn violer(&mut self, nom: &'static str, date: Instant, details: impl Into<String>) {
        // Garde symétrique de celui d'`attendre` : une vivacité bornée ne se
        // viole pas directement, elle échoit. La violer à la main court-circuite
        // l'horizon, c'est-à-dire la seule chose qui la rende testable (PD2).
        match self.classe(nom) {
            Some(Classe::Surete) => {}
            Some(Classe::VivaciteBornee { .. }) => panic!(
                "« {nom} » est armé comme vivacité bornée : on ne le viole pas, il échoit"
            ),
            None => panic!("oracle « {nom} » violé sans avoir été armé"),
        }
        self.violations.push(Violation {
            oracle: nom,
            date,
            details: details.into(),
        });
    }

    /// Arme l'attente d'une vivacité bornée : la condition doit devenir vraie
    /// avant `maintenant + horizon`.
    ///
    /// # Panics
    ///
    /// Si `nom` n'est pas une vivacité bornée armée. C'est le garde-fou qui
    /// compte le plus, et il était le plus inerte : sous `debug_assert!`, une
    /// vivacité surveillée sous un nom mal classé n'était jamais armée, jamais
    /// échue, et l'exécution rapportait « aucune violation » — indiscernable
    /// d'une surveillance satisfaite.
    pub fn attendre(&mut self, nom: &'static str, maintenant: Instant, details: impl Into<String>) {
        let horizon = match self.classe(nom) {
            Some(Classe::VivaciteBornee { horizon }) => horizon,
            Some(Classe::Surete) => {
                panic!("« {nom} » est armé comme sûreté : on ne l'attend pas, on le viole")
            }
            None => panic!("« {nom} » n'est pas un oracle armé"),
        };
        // `Instant + Duree` sature : un horizon assez grand pour saturer rendrait
        // l'attente inatteignable, donc une vivacité déclarée **bornée** se
        // comporterait en non bornée — ce que PD2 refuse de rendre représentable.
        let echeance = maintenant + horizon;
        assert!(
            echeance.0 != u64::MAX,
            "« {nom} » : l'échéance sature, l'attente ne pourrait jamais échoir"
        );
        self.attentes.push(Attente {
            oracle: nom,
            echeance,
            details: details.into(),
        });
    }

    /// La condition attendue est survenue. Retire la plus ancienne attente de
    /// cet oracle.
    pub fn satisfaire(&mut self, nom: &str) {
        if let Some(i) = self.attentes.iter().position(|a| a.oracle == nom) {
            self.attentes.remove(i);
        }
    }

    /// Transforme en violations les attentes dont l'échéance est dépassée.
    /// Appelé par la boucle à chaque avance de l'horloge.
    pub fn echoir(&mut self, maintenant: Instant) {
        let mut i = 0;
        while i < self.attentes.len() {
            if self.attentes[i].echeance < maintenant {
                let a = self.attentes.remove(i);
                self.violations.push(Violation {
                    // L'échéance, pas `maintenant` : l'horloge saute d'événement
                    // en événement (EX-C01), donc l'instant de détection peut
                    // être arbitrairement postérieur à celui de la violation.
                    // C'est ce que le champ `date` promet de ne pas être.
                    date: a.echeance,
                    oracle: a.oracle,
                    details: format!(
                        "horizon dépassé à {} — {} (constaté à {})",
                        a.echeance.0, a.details, maintenant.0
                    ),
                });
            } else {
                i += 1;
            }
        }
    }

    /// Nombre d'attentes encore ouvertes. À la fin d'une exécution, une attente
    /// ouverte n'est **pas** une violation : elle n'a simplement pas conclu, et
    /// c'est exactement ce qu'une trace finie sait dire d'une vivacité (§8.3).
    pub fn attentes_ouvertes(&self) -> usize {
        self.attentes.len()
    }

    /// Les prédicats locaux armés, avec ce qui les met en défaut (PD10, EX-A39).
    pub fn criteres_locaux(&self) -> BTreeMap<&'static str, (&'static str, &'static str)> {
        self.oracles
            .iter()
            .filter_map(|o| match o.portee {
                Portee::Locale {
                    contre_exemple,
                    reglage_fautif,
                } => Some((o.nom, (contre_exemple, reglage_fautif))),
                Portee::Globale => None,
            })
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-C11 — le refus au chargement, avec son message.
    #[test]
    fn une_vivacite_sans_horizon_est_refusee() {
        let e = Oracle::depuis_declaration("couverture", "vivacite", None, "§4.2")
            .expect_err("une vivacité sans horizon doit être refusée");
        assert!(e.contains("§3.2"), "le message doit citer §3.2 : {e}");
        assert!(Oracle::depuis_declaration("couverture", "vivacite", Some(Duree(10)), "§4.2").is_ok());
        assert!(Oracle::depuis_declaration("r1", "surete", None, "§2.1").is_ok());
    }

    #[test]
    fn une_classe_inconnue_est_refusee() {
        assert!(Oracle::depuis_declaration("x", "peut-etre", None, "§1").is_err());
    }

    /// EX-C09 — la violation porte l'instant exact.
    #[test]
    fn la_violation_porte_sa_date() {
        let mut r = Registre::nouveau();
        r.armer(Oracle::surete("m1", "§1.2"));
        r.violer("m1", Instant(1_234), "décalage 7 avant décalage 5");
        assert_eq!(r.violations().len(), 1);
        assert_eq!(r.violations()[0].date, Instant(1_234));
    }

    #[test]
    fn une_vivacite_satisfaite_avant_son_horizon_ne_viole_pas() {
        let mut r = Registre::nouveau();
        r.armer(Oracle::vivacite_bornee("proprietaire", Duree(100), "§2.2"));
        r.attendre("proprietaire", Instant(0), "partition 3");
        r.echoir(Instant(50));
        r.satisfaire("proprietaire");
        r.echoir(Instant(500));
        assert!(r.violations().is_empty());
        assert_eq!(r.attentes_ouvertes(), 0);
    }

    /// L'échéance elle-même n'est **pas** dépassée : `echoir` compare avec `<`,
    /// donc la violation tombe au premier instant strictement postérieur. Le nom
    /// le dit maintenant — l'ancien annonçait « à son horizon » et le corps
    /// établissait le contraire.
    #[test]
    fn une_vivacite_non_satisfaite_viole_juste_apres_son_horizon() {
        let mut r = Registre::nouveau();
        r.armer(Oracle::vivacite_bornee("proprietaire", Duree(100), "§2.2"));
        r.attendre("proprietaire", Instant(0), "partition 3");
        r.echoir(Instant(100));
        assert!(r.violations().is_empty(), "l'échéance elle-même n'est pas dépassée");
        r.echoir(Instant(101));
        assert_eq!(r.violations().len(), 1);
    }

    /// PD10 — un prédicat local ne s'affiche jamais comme un état de l'essaim.
    #[test]
    fn un_predicat_local_ne_dit_jamais_converge() {
        let o = Oracle::surete("accord", "§3.1").local(
            "l'agent mort cesse de publier, ses voisins lisent un état figé",
            "crash-arrêt d'un agent pendant la fenêtre R",
        );
        let affiche = o.nom_affiche();
        assert!(affiche.contains("critère local"), "{affiche}");
        assert!(!affiche.contains("convergé"));
    }

    #[test]
    fn les_criteres_locaux_portent_leur_reglage_fautif() {
        let mut r = Registre::nouveau();
        r.armer(Oracle::surete("accord", "§3.1").local("état figé", "crash-arrêt"));
        r.armer(Oracle::surete("m1", "§1.2"));
        let locaux = r.criteres_locaux();
        assert_eq!(locaux.len(), 1);
        assert_eq!(locaux["accord"], ("état figé", "crash-arrêt"));
    }
}
