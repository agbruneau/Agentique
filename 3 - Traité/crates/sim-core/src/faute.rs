//! Le modèle de faute, objet de première classe (PD6).
//!
//! > Les fautes qu'il sait produire sont exactement les fautes que la campagne
//! > pourra trouver. (§3.3, p. 50, 3ᵉ éd.)
//!
//! Conséquence tenue ici : le modèle s'affiche (EX-C06), se versionne, et
//! nomme ce qu'il ne sait pas produire. Un mécanisme absent du modèle a, dans
//! tout résultat, une probabilité de faute nulle — le mode (b) de l'algorithme
//! 2 du §3.2 du traité, c'est-à-dire un mensonge silencieux.

use crate::alea::Alea;
use crate::temps::{Duree, Instant};
use crate::ActeurId;
use serde::{Deserialize, Serialize};

/// Version du modèle de faute, écrite dans tout export (PD6, NF-03). Une
/// campagne rejouée sous un modèle différent ne compare pas la même chose.
pub const VERSION_MODELE: u32 = 1;

/// Les trois échelles de panne matérielle du §3.3. Elles ne sont pas
/// interchangeables : une baie emporte plusieurs machines, un centre emporte
/// plusieurs baies, et c'est cette imbrication qui produit la corrélation que
/// les bornes probabilistes du traité supposent absente (§8.3 du PRD).
#[derive(Clone, Copy, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub enum Niveau {
    /// Une machine tombe seule.
    Machine,
    /// Une baie tombe, et emporte toutes ses machines.
    Baie,
    /// Un centre tombe, et emporte toutes ses baies.
    Centre,
}

/// Position d'un acteur dans la hiérarchie matérielle.
#[derive(Clone, Copy, PartialEq, Eq, Debug, Default, Serialize, Deserialize)]
pub struct Domaine {
    /// Machine hôte.
    pub machine: u32,
    /// Baie qui contient la machine.
    pub baie: u32,
    /// Centre qui contient la baie.
    pub centre: u32,
}

/// Une panne tirée : qui tombe, à quelle échelle, et si elle redémarre.
///
/// `redemarrage` à `None` est un crash-arrêt franc ; `Some(d)` est un
/// arrêt-reprise, c'est-à-dire le cas que le §4.3 oppose au robot mort qui
/// reste mort — un agent qui revient avec son état d'avant et écrit.
#[derive(Clone, Copy, Debug)]
pub struct Panne {
    /// L'acteur qui tombe.
    pub acteur: ActeurId,
    /// L'échelle à laquelle la panne s'est produite.
    pub niveau: Niveau,
    /// Délai de retour, ou `None` pour un crash-arrêt franc.
    pub redemarrage: Option<Duree>,
}

/// La partition réseau, **processus à deux états** et non tirage par message.
///
/// §3.2 du traité, algorithme 2 : le PRD (EX-C05) écrit « faute de quoi elle n'est jamais
/// tirée ». Un tirage indépendant par message produit des pertes éparses, pas
/// une coupure durable : la scission silencieuse et la décision divisée que les
/// scénarios doivent provoquer ne surviennent jamais sous ce modèle-là.
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Partition {
    /// Probabilité d'entrer en partition à chaque pas d'évaluation.
    pub p_entree: f64,
    /// Probabilité d'en sortir à chaque pas d'évaluation.
    pub p_sortie: f64,
    /// Période d'évaluation du processus.
    pub pas: Duree,
    /// Côté de chaque acteur pendant une partition. Vide hors partition.
    #[serde(skip)]
    cotes: Vec<bool>,
    #[serde(skip)]
    prochaine_evaluation: Instant,
}

impl Partition {
    /// Processus à deux états, réglé par ses deux probabilités et sa période.
    pub fn nouvelle(p_entree: f64, p_sortie: f64, pas: Duree) -> Self {
        Partition {
            p_entree,
            p_sortie,
            pas,
            cotes: Vec::new(),
            prochaine_evaluation: Instant(0),
        }
    }

    /// Aucune partition possible. C'est un réglage, pas un défaut : les
    /// scénarios A et B tournent sous ce régime.
    pub fn aucune() -> Self {
        Partition::nouvelle(0.0, 0.0, Duree(1))
    }

    /// Vrai pendant une coupure. Les côtés sont alors fixés et ne bougent plus
    /// jusqu'à la sortie.
    pub fn en_cours(&self) -> bool {
        !self.cotes.is_empty()
    }

    /// Fait avancer le processus jusqu'à `maintenant`. À appeler depuis la
    /// boucle du moteur : l'évaluation est cadencée par le temps logique, donc
    /// reproductible.
    ///
    /// Un pas nul suspend l'évaluation au lieu de boucler : `pas` est un champ
    /// public désérialisé, donc `Duree(0)` est atteignable depuis une
    /// configuration, et la boucle ne progresserait jamais.
    pub fn avancer(&mut self, maintenant: Instant, nb_acteurs: usize, alea: &mut Alea) {
        if self.pas.0 == 0 {
            return;
        }
        while self.prochaine_evaluation <= maintenant {
            let suivante = self.prochaine_evaluation + self.pas;
            // `Instant + Duree` sature : arrivée à `u64::MAX`, la condition
            // resterait vraie à jamais et la boucle ne rendrait plus la main.
            if suivante == self.prochaine_evaluation {
                self.prochaine_evaluation = Instant(u64::MAX);
                break;
            }
            self.prochaine_evaluation = suivante;
            if self.en_cours() {
                if alea.bernoulli(self.p_sortie) {
                    self.cotes.clear();
                }
            } else if alea.bernoulli(self.p_entree) {
                // Les côtés sont tirés une fois, à l'entrée : pendant toute la
                // partition, la coupure reste la même. C'est ce qui la rend
                // durable, et donc observable.
                self.cotes = (0..nb_acteurs).map(|_| alea.bernoulli(0.5)).collect();
            }
        }
    }

    /// Vrai si le lien entre ces deux acteurs est coupé.
    pub fn coupe(&self, de: ActeurId, vers: ActeurId) -> bool {
        match (self.cotes.get(de.0 as usize), self.cotes.get(vers.0 as usize)) {
            (Some(a), Some(b)) => a != b,
            _ => false,
        }
    }
}

/// Un point d'injection de haut niveau (EX-C07).
#[derive(Clone, Debug, Serialize, Deserialize)]
pub enum Injection {
    /// Faire échouer une opération d'ordinaire réussie.
    Echec {
        /// Nom de l'opération visée.
        operation: String,
        /// Probabilité d'échec à chaque appel.
        probabilite: f64,
    },
    /// Retarder une opération d'ordinaire rapide.
    Retard {
        /// Nom de l'opération visée.
        operation: String,
        /// Retard ajouté, en millisecondes.
        ajout_ms: f64,
        /// Probabilité que le retard s'applique.
        probabilite: f64,
    },
    /// Choisir une valeur inhabituelle de paramètre.
    Valeur {
        /// Nom du paramètre visé.
        parametre: String,
        /// Valeur imposée.
        valeur: f64,
    },
}

/// Le modèle de faute complet (EX-C05).
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct ModeleFaute {
    /// Probabilité qu'un message soit perdu sur le chemin.
    pub omission: f64,
    /// Retard additionnel moyen d'un message, en millisecondes.
    pub retard_moyen_ms: f64,
    /// Partition réseau, processus à deux états.
    pub partition: Partition,
    /// Probabilité de crash par machine et par pas d'évaluation.
    pub crash_machine: f64,
    /// Idem par baie — emporte toutes les machines de la baie.
    pub crash_baie: f64,
    /// Idem par centre.
    pub crash_centre: f64,
    /// Période d'évaluation des crashs.
    pub pas_crash: Duree,
    /// Fraction des pannes qui sont des arrêt-reprise plutôt que des
    /// crash-arrêt francs, et le délai de retour.
    pub part_redemarrage: f64,
    /// Délai avant qu'un acteur en arrêt-reprise revienne.
    pub delai_redemarrage: Duree,
    /// Probabilité qu'une écriture non synchronisée soit corrompue au
    /// redémarrage.
    pub corruption_au_redemarrage: f64,
    /// Amplitude de la randomisation des dates d'événements, en tics. Zéro
    /// désactive.
    pub gigue_de_date: u64,
    /// Points d'injection de haut niveau.
    pub injections: Vec<Injection>,
    #[serde(skip)]
    prochaine_evaluation_crash: Instant,
}

impl Default for ModeleFaute {
    /// Le modèle par défaut est **sans faute**. Motif : une faute qu'on n'a pas
    /// demandée est aussi trompeuse qu'une faute qu'on ne peut pas produire.
    /// Les scénarios déclarent ce qu'ils injectent.
    fn default() -> Self {
        ModeleFaute {
            omission: 0.0,
            retard_moyen_ms: 0.0,
            partition: Partition::aucune(),
            crash_machine: 0.0,
            crash_baie: 0.0,
            crash_centre: 0.0,
            pas_crash: Duree(1_000),
            part_redemarrage: 0.0,
            delai_redemarrage: Duree(0),
            corruption_au_redemarrage: 0.0,
            gigue_de_date: 0,
            injections: Vec::new(),
            prochaine_evaluation_crash: Instant(0),
        }
    }
}

impl ModeleFaute {
    /// Vrai si le message est perdu — par omission tirée ou par partition.
    ///
    /// Les deux causes sont distinctes et le restent : la partition est une
    /// coupure durable et corrélée, l'omission un aléa indépendant. Les
    /// confondre reviendrait à rendre la partition inobservable.
    pub fn message_perdu(&self, de: ActeurId, vers: ActeurId, alea: &mut Alea) -> bool {
        self.partition.coupe(de, vers) || alea.bernoulli(self.omission)
    }

    /// Retard additionnel d'un message, en millisecondes.
    pub fn retard_message(&self, alea: &mut Alea) -> f64 {
        if self.retard_moyen_ms <= 0.0 {
            0.0
        } else {
            alea.exponentielle(self.retard_moyen_ms)
        }
    }

    /// Randomisation de la date d'un événement (EX-C05, dernière entrée de la
    /// liste du §3.3). Rend un décalage en tics, jamais négatif : un événement
    /// ne remonte pas le temps logique.
    pub fn gigue(&self, alea: &mut Alea) -> Duree {
        if self.gigue_de_date == 0 {
            Duree(0)
        } else {
            Duree(alea.entier(self.gigue_de_date + 1))
        }
    }

    /// Vrai si une écriture non synchronisée est corrompue au redémarrage.
    pub fn ecriture_corrompue(&self, alea: &mut Alea) -> bool {
        alea.bernoulli(self.corruption_au_redemarrage)
    }

    /// Fait avancer le tirage des pannes jusqu'à `maintenant` et rend celles
    /// survenues. L'itération suit l'ordre du vecteur de domaines — jamais
    /// celui d'une table de hachage (PD1).
    pub fn tirer_pannes(
        &mut self,
        maintenant: Instant,
        domaines: &[Domaine],
        alea: &mut Alea,
    ) -> Vec<Panne> {
        let mut pannes = Vec::new();
        // Même garde que `Partition::avancer` : `pas_crash` est public et
        // désérialisé, et un pas nul ferait boucler l'évaluation sans fin.
        if self.pas_crash.0 == 0 {
            return pannes;
        }
        while self.prochaine_evaluation_crash <= maintenant {
            let suivante = self.prochaine_evaluation_crash + self.pas_crash;
            // Même garde que `Partition::avancer` : la saturation ferme
            // l'enroulement et ouvrirait un blocage si on ne la voyait pas.
            if suivante == self.prochaine_evaluation_crash {
                self.prochaine_evaluation_crash = Instant(u64::MAX);
                break;
            }
            self.prochaine_evaluation_crash = suivante;

            // **Un tirage par niveau, avant la boucle des acteurs.** Le niveau
            // est l'unité de la panne : `crash_baie` est la probabilité qu'une
            // baie tombe à ce pas, pas celle qu'une de ses machines la fasse
            // tomber. Tirer par membre, comme ce code le faisait, donnait deux
            // résultats faux à la fois — une baie de m machines tombait avec la
            // probabilité 1 − (1 − p)^m, donc l'injection dépendait de la taille
            // de la population ; et la baie n'emportait que les membres
            // **postérieurs** au tirage réussi, alors que « emporte toutes les
            // machines de la baie » est la définition du niveau.
            //
            // Les listes sont triées et dédupliquées : l'ordre des tirages ne
            // dépend que de la structure, jamais de son parcours (PD1). Le
            // tirage d'une baie a lieu même si son centre est déjà tombé, pour
            // que le nombre de tirages consommés reste fonction de la seule
            // structure ; le centre l'emporte ensuite au classement.
            let mut cles_centres: Vec<u32> = domaines.iter().map(|d| d.centre).collect();
            cles_centres.sort_unstable();
            cles_centres.dedup();
            let centres_tombes: Vec<u32> = cles_centres
                .into_iter()
                .filter(|_| alea.bernoulli(self.crash_centre))
                .collect();

            let mut cles_baies: Vec<(u32, u32)> =
                domaines.iter().map(|d| (d.centre, d.baie)).collect();
            cles_baies.sort_unstable();
            cles_baies.dedup();
            let baies_tombees: Vec<(u32, u32)> = cles_baies
                .into_iter()
                .filter(|_| alea.bernoulli(self.crash_baie))
                .collect();

            // Les échelles se cumulent : un centre qui tombe emporte ses baies,
            // une baie ses machines, indépendamment de leur propre tirage. C'est
            // la corrélation que le §8.3 du PRD déclare non mesurable et seulement
            // injectable.
            for (i, d) in domaines.iter().enumerate() {
                let acteur = ActeurId(i as u32);
                if centres_tombes.contains(&d.centre) {
                    pannes.push(self.panne(acteur, Niveau::Centre, alea));
                } else if baies_tombees.contains(&(d.centre, d.baie)) {
                    pannes.push(self.panne(acteur, Niveau::Baie, alea));
                } else if alea.bernoulli(self.crash_machine) {
                    pannes.push(self.panne(acteur, Niveau::Machine, alea));
                }
            }
        }
        pannes
    }

    fn panne(&self, acteur: ActeurId, niveau: Niveau, alea: &mut Alea) -> Panne {
        let redemarrage = if alea.bernoulli(self.part_redemarrage) {
            Some(self.delai_redemarrage)
        } else {
            None
        };
        Panne {
            acteur,
            niveau,
            redemarrage,
        }
    }

    /// EX-C07 — l'opération nommée échoue-t-elle ?
    pub fn injection_echec(&self, operation: &str, alea: &mut Alea) -> bool {
        self.injections.iter().any(|i| match i {
            Injection::Echec {
                operation: o,
                probabilite,
            } => o == operation && alea.bernoulli(*probabilite),
            _ => false,
        })
    }

    /// EX-C07 — retard additionnel injecté sur l'opération nommée, en ms.
    pub fn injection_retard(&self, operation: &str, alea: &mut Alea) -> f64 {
        let mut total = 0.0;
        for i in &self.injections {
            if let Injection::Retard {
                operation: o,
                ajout_ms,
                probabilite,
            } = i
            {
                if o == operation && alea.bernoulli(*probabilite) {
                    total += ajout_ms;
                }
            }
        }
        total
    }

    /// EX-C07 — valeur inhabituelle imposée à un paramètre, s'il y en a une.
    pub fn injection_valeur(&self, parametre: &str) -> Option<f64> {
        self.injections.iter().find_map(|i| match i {
            Injection::Valeur {
                parametre: p,
                valeur,
            } if p == parametre => Some(*valeur),
            _ => None,
        })
    }

    /// EX-C06 — le modèle s'affiche, avec ses unités (F1).
    pub fn resume(&self) -> Vec<(&'static str, String)> {
        vec![
            ("omission", format!("{:.4} (probabilité par message)", self.omission)),
            ("retard moyen", format!("{:.3} ms", self.retard_moyen_ms)),
            (
                "partition",
                format!(
                    "entrée {:.5} / sortie {:.5} par pas de {} tics",
                    self.partition.p_entree, self.partition.p_sortie, self.partition.pas.0
                ),
            ),
            (
                "crash",
                format!(
                    "machine {:.6} / baie {:.6} / centre {:.6} par pas de {} tics",
                    self.crash_machine, self.crash_baie, self.crash_centre, self.pas_crash.0
                ),
            ),
            (
                "arrêt-reprise",
                format!(
                    "{:.2} des pannes, retour après {} tics",
                    self.part_redemarrage, self.delai_redemarrage.0
                ),
            ),
            (
                "corruption au redémarrage",
                format!("{:.4} (probabilité par écriture non synchronisée)", self.corruption_au_redemarrage),
            ),
            ("gigue de date", format!("{} tics", self.gigue_de_date)),
            ("points d'injection", format!("{}", self.injections.len())),
            ("version du modèle", format!("{VERSION_MODELE}")),
        ]
    }

    /// EX-C06 — l'interface avertit qu'un taux de fautes excessif **réduit**
    /// l'exploration au lieu de l'augmenter.
    ///
    /// > éviter de pousser le système dans un espace d'états restreint par un
    /// > taux de fautes excessif (§3.3)
    pub fn avertissements(&self) -> Vec<String> {
        let mut a = Vec::new();
        if self.omission > 0.5 {
            a.push(format!(
                "omission à {:.2} : plus d'un message sur deux est perdu ; l'exploration se \
                 restreint aux états d'échec au lieu de s'élargir (§3.3)",
                self.omission
            ));
        }
        if self.partition.p_entree > 0.0 && self.partition.p_sortie == 0.0 {
            a.push(
                "partition sans probabilité de sortie : une fois entrée, l'exécution reste \
                 partitionnée jusqu'à la fin — c'est un régime, pas une faute intermittente"
                    .to_string(),
            );
        }
        // Ce que ce seuil mesure, et qu'A1 n'a pas déplacé : la probabilité
        // qu'un acteur **donné** tombe à un pas. Chaque acteur appartient à
        // exactement une machine, une baie et un centre, donc la somme des trois
        // taux majore cette probabilité par union — avant A1 comme après.
        // Mesuré à 10 000 pas sur vingt acteurs : 0,0928 par acteur et par pas
        // pour `crash_centre = 0,09`, 0,0905 pour `crash_machine = 0,09`. Le
        // seuil reste donc calibré sur la bonne grandeur.
        if self.crash_machine + self.crash_baie + self.crash_centre > 0.1 {
            a.push(
                "taux de crash cumulé supérieur à 0,1 par pas et par acteur : la population se \
                 vide avant d'avoir exploré son espace d'états (§3.3)"
                    .to_string(),
            );
        }
        // Ce qu'A1 a réellement changé, et qu'aucun taux n'exprime : la
        // corrélation. Depuis le tirage par niveau, une baie ou un centre tombe
        // **en entier** avec la probabilité déclarée, alors qu'un tirage par
        // membre laissait sortir une partie du domaine. À taux par acteur
        // identique, la même mesure donne 928 vidages complets sur 10 000 pas à
        // `crash_centre = 0,09` contre **zéro** à `crash_machine = 0,09` :
        // l'espace d'états visité est celui d'une population vidée d'un coup.
        // C'est un régime, comme la partition sans probabilité de sortie, donc
        // il se signale sans seuil.
        if self.crash_baie > 0.0 || self.crash_centre > 0.0 {
            a.push(format!(
                "crash corrélé : une baie tombe en entier avec la probabilité {:.6} par pas, \
                 un centre avec {:.6} — la population se vide d'un coup au lieu de perdre \
                 quelques membres, et aucun taux par acteur ne distingue les deux régimes \
                 (§3.3 du traité, §8.3 du PRD)",
                self.crash_baie, self.crash_centre
            ));
        }
        a
    }

    /// PD6 — ce que le modèle **ne sait pas** produire, à afficher au même rang
    /// que ce qu'il sait produire. Un mécanisme absent a une probabilité de
    /// faute nulle dans tout résultat, et c'est un mensonge silencieux.
    ///
    /// **Sans balisage Markdown dans les entrées** : `sim-viz` les affiche
    /// telles quelles par un `egui::RichText`, qui n'a pas d'analyseur — des
    /// astérisques d'emphase et des accents graves s'y liraient littéralement,
    /// et un retour à la ligne couperait la puce. Un nom de module ou d'item se
    /// marque donc par des guillemets. La règle vaut pour les trois listes
    /// d'absences que l'onglet « Limites » réunit, et `sim-viz` la tient par un
    /// test.
    pub fn hors_modele() -> &'static [&'static str] {
        &[
            "ce modèle-ci, dans les scénarios livrés : le moteur n'en reçoit jamais \
             d'exemplaire. « Moteur::installer_fautes » n'a aucun appelant, donc toute \
             exécution tourne sur « ModeleFaute::default() », c'est-à-dire sans faute, quelle \
             que soit la « Config » chargée. Le scénario B, lui, règle bien « Config.fautes » — \
             deux points d'injection déclarés — mais cette déclaration ne sert qu'à \
             l'affichage, au hachage et au versionnement : elle ne pilote aucun tirage. \
             Sans appelant non plus, neuf : « tirer_pannes » (crashs par niveau), \
             « Moteur::avancer_partition » (partition à deux états), « message_perdu » \
             (l'omission d'EX-C05, et la coupure de partition avec elle), \
             « injection_echec », « injection_retard », « injection_valeur », « retard_message », \
             « ecriture_corrompue », et « avertissements » — la moitié [U] d'EX-C06 : les \
             avertissements affichés par « sim-agents » et « sim-viz » viennent de \
             « sim_agents::stigmergie::Params::avertissements », homonyme et sans rapport, \
             jamais de ceux-ci. « gigue » est le seul mécanisme d'ici que la boucle \
             appelle, et son amplitude vaut zéro au défaut. Les fautes que les scénarios \
             produisent réellement — omission du scénario A, échec d'action et crash avant \
             validation du scénario B — sont tirées par les mécanismes de « sim-agents », pas \
             ici : deux mécanismes pour la même faute, dont un seul est réglable depuis la \
             configuration et versionné avec elle",
            "le plancher mémoire de la population (EX-C17) : « sim_core::service::CoutAgent » \
             le calcule et retrouve les chiffres du traité, mais aucun affichage ne le lit",
            "faute byzantine — hors modèle P. Le point d'injection existe (DT8, \
             « sim-agents::taux_de_base »), désactivé par défaut et limité aux scénarios I et L",
            "toute dépendance hors du monde clos : bibliothèque tierce, système \
             d'exploitation, courtier réel (§3.3 du traité, §2.3 du PRD)",
            // EX-C20 — §8.3 du traité de la deuxième édition. À ne pas confondre avec
            // l'entrée « faute byzantine » ci-dessus : là, l'adversité est
            // **injectée** par un point d'injection désactivé par défaut (DT8) ;
            // ici, elle est **produite** par une population dont chaque membre
            // suit fidèlement sa consigne.
            "adversité endogène (§8.3 du traité — celui du PRD porte sur ce que le produit ne \
             mesure pas) — des agents qui ne s'arrêtent pas, ne se taisent pas, \
             n'émettent aucune valeur arbitraire, et dont l'effet est pourtant byzantin, sans \
             qu'aucun ait été programmé pour nuire. Le seuil f < n/3 n'y a pas de sens : le \
             nombre d'agents adverses n'est pas borné par l'hypothèse, il vaut n. Le modèle P \
             la manque par construction, et le monde clos ne peut pas la produire — les moyens \
             observés (révocation de comptes, terminaison de processus, contrôle de santé \
             falsifié) sont hors du milieu, donc hors de ce simulateur (T3)",
        ]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-C05 : la partition doit **durer**. Un tirage indépendant par message
    /// ne la produirait jamais, et c'est la raison pour laquelle le PRD impose
    /// le processus à deux états.
    #[test]
    fn la_partition_dure() {
        let mut p = Partition::nouvelle(0.5, 0.01, Duree(10));
        let mut alea = Alea::nouveau(1);
        let mut tics_partitionnes = 0;
        let mut entrees = 0;
        let mut etait = false;
        for t in 0..10_000 {
            p.avancer(Instant(t), 8, &mut alea);
            if p.en_cours() {
                tics_partitionnes += 1;
                if !etait {
                    entrees += 1;
                }
            }
            etait = p.en_cours();
        }
        assert!(tics_partitionnes > 5_000, "partitionné {tics_partitionnes} tics");
        // Peu d'entrées, longues durées : c'est la signature d'un processus à
        // deux états, par opposition à un scintillement.
        assert!(entrees < 50, "{entrees} entrées en partition");
    }

    #[test]
    fn la_partition_coupe_les_deux_cotes_et_pas_le_reste() {
        let mut p = Partition::nouvelle(1.0, 0.0, Duree(1));
        let mut alea = Alea::nouveau(2);
        p.avancer(Instant(0), 4, &mut alea);
        assert!(p.en_cours());
        // Un acteur n'est jamais coupé de lui-même.
        for i in 0..4u32 {
            assert!(!p.coupe(ActeurId(i), ActeurId(i)));
        }
        // La relation est symétrique.
        for i in 0..4u32 {
            for j in 0..4u32 {
                assert_eq!(p.coupe(ActeurId(i), ActeurId(j)), p.coupe(ActeurId(j), ActeurId(i)));
            }
        }
    }

    #[test]
    fn aucune_partition_ne_coupe_rien() {
        let mut p = Partition::aucune();
        let mut alea = Alea::nouveau(3);
        p.avancer(Instant(1_000), 4, &mut alea);
        assert!(!p.en_cours());
        assert!(!p.coupe(ActeurId(0), ActeurId(3)));
    }

    /// Une panne de baie emporte toutes ses machines : c'est la corrélation que
    /// le §8.3 du PRD déclare injectable et non mesurable.
    #[test]
    fn la_panne_de_baie_emporte_ses_machines() {
        let mut m = ModeleFaute {
            crash_baie: 1.0,
            pas_crash: Duree(1),
            ..Default::default()
        };
        let domaines: Vec<Domaine> = (0..6)
            .map(|i| Domaine {
                machine: i,
                baie: i / 3,
                centre: 0,
            })
            .collect();
        let mut alea = Alea::nouveau(4);
        let pannes = m.tirer_pannes(Instant(0), &domaines, &mut alea);
        assert_eq!(pannes.len(), 6);
        assert!(pannes.iter().all(|p| p.niveau == Niveau::Baie));
    }

    /// EX-C05 — « idem par baie : emporte toutes les machines de la baie », et
    /// `crash_baie` est une probabilité **par baie et par pas**.
    ///
    /// À probabilité intermédiaire, le tirage par membre manquait les deux :
    /// il laissait sortir indemnes les machines rencontrées avant le tirage
    /// réussi, et donnait à une baie de vingt machines une chance de tomber de
    /// 1 − 0,5²⁰ ≈ 1, c'est-à-dire une injection qui croît avec la population.
    #[test]
    fn une_baie_tombe_en_entier_et_a_sa_propre_probabilite() {
        const PAS: u64 = 200;
        const PAR_BAIE: u32 = 20;
        let mut m = ModeleFaute {
            crash_baie: 0.5,
            pas_crash: Duree(1),
            ..Default::default()
        };
        let domaines: Vec<Domaine> = (0..2 * PAR_BAIE)
            .map(|i| Domaine {
                machine: i,
                baie: i / PAR_BAIE,
                centre: 0,
            })
            .collect();
        let mut alea = Alea::nouveau(11);
        let mut chutes = 0u64;
        for t in 0..PAS {
            let pannes = m.tirer_pannes(Instant(t), &domaines, &mut alea);
            for baie in 0..2u32 {
                let frappees = pannes
                    .iter()
                    .filter(|p| p.acteur.0 / PAR_BAIE == baie && p.niveau == Niveau::Baie)
                    .count() as u32;
                assert!(
                    frappees == 0 || frappees == PAR_BAIE,
                    "baie {baie} au pas {t} : {frappees} machines sur {PAR_BAIE}"
                );
                if frappees == PAR_BAIE {
                    chutes += 1;
                }
            }
        }
        // 400 tirages de baie à p = 0,5 : ≈ 200 chutes, et non ≈ 400 comme le
        // donnerait un tirage par machine.
        assert!(
            (160..240).contains(&chutes),
            "{chutes} chutes de baie sur {} tirages à p = 0,5",
            2 * PAS
        );
    }

    /// EX-C05 — même règle un cran plus haut : un centre emporte **toutes** ses
    /// baies, et le niveau rapporté est celui du centre, pas celui de la baie.
    #[test]
    fn un_centre_emporte_toutes_ses_baies() {
        let mut m = ModeleFaute {
            crash_centre: 1.0,
            crash_baie: 0.5,
            crash_machine: 0.5,
            pas_crash: Duree(1),
            ..Default::default()
        };
        let domaines: Vec<Domaine> = (0..12)
            .map(|i| Domaine {
                machine: i,
                baie: i / 4,
                centre: 0,
            })
            .collect();
        let pannes = m.tirer_pannes(Instant(0), &domaines, &mut Alea::nouveau(12));
        assert_eq!(pannes.len(), 12);
        assert!(pannes.iter().all(|p| p.niveau == Niveau::Centre));
    }

    #[test]
    fn le_modele_par_defaut_ne_produit_aucune_faute() {
        let mut m = ModeleFaute::default();
        let mut alea = Alea::nouveau(5);
        assert!(!m.message_perdu(ActeurId(0), ActeurId(1), &mut alea));
        assert_eq!(m.retard_message(&mut alea), 0.0);
        assert_eq!(m.gigue(&mut alea), Duree(0));
        let domaines = vec![Domaine::default(); 4];
        assert!(m.tirer_pannes(Instant(10_000), &domaines, &mut alea).is_empty());
        assert!(m.avertissements().is_empty());
    }

    #[test]
    fn les_points_dinjection_repondent_par_nom() {
        let m = ModeleFaute {
            injections: vec![
                Injection::Echec {
                    operation: "ecriture".into(),
                    probabilite: 1.0,
                },
                Injection::Retard {
                    operation: "lecture".into(),
                    ajout_ms: 5.0,
                    probabilite: 1.0,
                },
                Injection::Valeur {
                    parametre: "gamma".into(),
                    valeur: 1.0,
                },
            ],
            ..Default::default()
        };
        let mut alea = Alea::nouveau(6);
        assert!(m.injection_echec("ecriture", &mut alea));
        assert!(!m.injection_echec("lecture", &mut alea));
        assert_eq!(m.injection_retard("lecture", &mut alea), 5.0);
        assert_eq!(m.injection_retard("ecriture", &mut alea), 0.0);
        assert_eq!(m.injection_valeur("gamma"), Some(1.0));
        assert_eq!(m.injection_valeur("alpha"), None);
    }

    #[test]
    fn un_taux_excessif_est_signale() {
        let m = ModeleFaute {
            omission: 0.9,
            ..Default::default()
        };
        assert!(!m.avertissements().is_empty());
    }

    /// EX-C06, moitié [U] — depuis le tirage par niveau, un crash de baie ou de
    /// centre est **corrélé** : le domaine tombe en entier. Le seuil cumulé de
    /// 0,1 mesure la probabilité par acteur, que la corrélation ne déplace pas
    /// (0,0928 mesuré pour `crash_centre = 0,09`, 0,0905 pour
    /// `crash_machine = 0,09`) ; il ne peut donc pas voir le régime, et un
    /// centre unique à 0,09 vidait toute la population 9 % des pas sans qu'un
    /// mot soit dit.
    #[test]
    fn un_crash_correle_est_signale_meme_sous_le_seuil_cumule() {
        let correle = ModeleFaute {
            crash_centre: 0.09,
            ..Default::default()
        };
        assert!(
            correle.crash_machine + correle.crash_baie + correle.crash_centre <= 0.1,
            "le cas est bien sous le seuil cumulé"
        );
        let a = correle.avertissements();
        assert_eq!(a.len(), 1, "{a:?}");
        assert!(a[0].contains("crash corrélé"), "{}", a[0]);

        // Même taux par acteur, sans corrélation : rien à signaler.
        let decorrele = ModeleFaute {
            crash_machine: 0.09,
            ..Default::default()
        };
        assert!(decorrele.avertissements().is_empty(), "aucun niveau n'est réglé");
    }
}
