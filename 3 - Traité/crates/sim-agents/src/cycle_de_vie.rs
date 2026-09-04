//! Cycle de vie et sondes (EX-A26), ordre de chute au retrait (EX-A48), budget
//! de perturbation (EX-A27).
//!
//! **Trois sondes aux effets disjoints et non substituables** — c'est ce que le
//! §2.2 du traité impose, et les confondre est le défaut que le scénario J exploitera :
//! la sonde de démarrage bloque les deux autres, celle de vivacité **redémarre
//! le conteneur**, celle de disponibilité **retire des points d'accès sans
//! redémarrer**.

use sim_core::temps::Duree;

/// Les cinq états du cycle de vie (EX-A26).
#[derive(Clone, Copy, PartialEq, Eq, Debug, Default)]
pub enum Etat {
    /// L'agent démarre : il ne sert pas encore.
    #[default]
    Demarrage,
    /// Prêt à recevoir du travail.
    Pret,
    /// En train de traiter.
    EnTraitement,
    /// En vidange : il finit son travail en cours et n'en accepte plus.
    EnVidange,
    /// Arrêté.
    Arrete,
}

impl Etat {
    /// Libellé affiché de l'état.
    pub fn libelle(self) -> &'static str {
        match self {
            Etat::Demarrage => "démarrage",
            Etat::Pret => "prêt",
            Etat::EnTraitement => "en traitement",
            Etat::EnVidange => "en vidange",
            Etat::Arrete => "arrêté",
        }
    }
}

/// Les trois sondes. Leurs effets sont **disjoints** : aucune ne remplace une
/// autre.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Sonde {
    /// Bloque les deux autres jusqu'à son succès.
    Demarrage,
    /// Échec répété → **redémarrage du conteneur**.
    Vivacite,
    /// Échec répété → **retrait des points d'accès**, sans redémarrer.
    Disponibilite,
}

impl Sonde {
    /// L'effet **propre** de cette sonde. Deux sondes n'ont jamais le même, et
    /// confondre les deux dernières est le défaut que le scénario J exploite.
    pub fn effet(self) -> &'static str {
        match self {
            Sonde::Demarrage => "bloque les deux autres sondes jusqu'à son succès",
            Sonde::Vivacite => "redémarre le conteneur",
            Sonde::Disponibilite => "retire des points d'accès, sans redémarrer",
        }
    }
}

/// Réglages documentés d'une sonde : `initialDelaySeconds 0`, `periodSeconds
/// 10`, `timeoutSeconds 1`, `successThreshold 1`, `failureThreshold 3`.
#[derive(Clone, Copy, Debug)]
pub struct ReglagesSonde {
    /// `initialDelaySeconds` — attente avant la première sonde.
    pub delai_initial_s: u64,
    /// `periodSeconds` — intervalle entre deux sondes.
    pub periode_s: u64,
    /// `timeoutSeconds` — **la borne connue la plus serrée**, et donc une
    /// hypothèse forte : « un agent sain répond en moins de tant ».
    pub expiration_s: u64,
    /// `successThreshold` — succès consécutifs pour redevenir sain.
    pub seuil_succes: u8,
    /// `failureThreshold` — échecs consécutifs avant l'action.
    pub seuil_echec: u8,
}

impl Default for ReglagesSonde {
    fn default() -> Self {
        ReglagesSonde {
            delai_initial_s: 0,
            periode_s: 10,
            expiration_s: 1,
            seuil_succes: 1,
            seuil_echec: 3,
        }
    }
}

impl ReglagesSonde {
    /// Coût : 1 aller-retour par agent et par période, soit **2 messages**, et
    /// Θ(n) messages par période pour l'essaim.
    pub fn messages_par_periode(&self, n: u32) -> u64 {
        2 * n as u64
    }

    /// Ce que la sonde de disponibilité **ne peut pas faire**, affiché en
    /// toutes lettres à côté du réglage (EX-A26).
    pub const LIMITE_DISPONIBILITE: &'static str =
        "la sonde de disponibilité n'a AUCUN effet sur l'allocation de partitions d'un \
         consommateur : son travail n'arrive pas par un point d'accès, mais par sa propre lecture \
         du journal (§6.1 du traité)";

    /// La contre-mesure du traité est une **bascule**, pas un conseil : la
    /// sonde de vivacité ne teste qu'un blocage constatable sans travailler —
    /// un fil qui n'a pas avancé son décalage — jamais la capacité à répondre
    /// dans le délai, qui mesure la charge.
    pub const BASCULE_VIVACITE: &'static str =
        "vivacité sur « décalage seulement » : teste un blocage constatable sans travailler, et \
         non la capacité à répondre dans le délai. Le scénario J montre que cette bascule supprime \
         la cascade SANS changer la charge (§6.1 du traité)";
}

/// Le groupe de consommation est un **troisième détecteur à seuil fixe**, avec
/// ses propres constantes (EX-A26).
#[derive(Clone, Copy, Debug)]
pub struct SeuilsGroupe {
    /// `session.timeout.ms` — un agent mort soupçonné.
    pub session_ms: u64,
    /// `max.poll.interval.ms` — un agent bloqué dans son traitement.
    pub max_poll_ms: u64,
}

impl Default for SeuilsGroupe {
    fn default() -> Self {
        SeuilsGroupe {
            session_ms: 45_000,
            max_poll_ms: 300_000,
        }
    }
}

/// EX-A48 — au retrait d'un agent, **la disponibilité chute avant la vivacité**.
///
/// Aux valeurs par défaut, un agent en vidange qui échoue à trois sondes de
/// vivacité consécutives est tué en une trentaine de secondes, en pleine
/// validation de décalage. L'ordre inverse est provocable, et ce qu'il produit
/// est mesuré : chaque retrait « propre » engendre au moins un redémarrage, et
/// chaque redémarrage rouvre un rééquilibrage.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum OrdreDeChute {
    /// Nominal : disponibilité d'abord, la vidange se termine proprement.
    DisponibiliteDabord,
    /// Provoqué : la vivacité tue l'agent en pleine vidange.
    VivaciteDabord,
}

/// Résultat d'un retrait.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub struct Retrait {
    /// Redémarrages engendrés par ce retrait.
    pub redemarrages: u32,
    /// Rééquilibrages rouverts par ces redémarrages.
    pub reequilibrages_rouverts: u32,
    /// Vrai si la validation de décalage a pu se terminer avant la mise à mort.
    pub validation_de_decalage_achevee: bool,
    /// Délai entre le début des échecs et la mise à mort effective.
    pub duree_avant_mise_a_mort: Duree,
}

/// Simule le retrait d'un agent selon l'ordre de chute.
///
/// `seuil_echec = 0` est **refusé**, et non écrêté : les champs de
/// [`ReglagesSonde`] sont publics, `seuil_echec − 1` sur un entier non signé
/// abandonnait, et l'écrêter rendait une durée de mise à mort d'allure
/// plausible sous un réglage qui ne décrit aucune politique de sonde — zéro
/// échec toléré n'est pas un seuil serré, c'est l'absence de seuil. « Une
/// configuration invalide est un refus rendu à l'appelant, jamais un abandon »
/// (SPEC §7, clause 4) — même arbitrage que `sim_core::detecteur::Detecteur` et
/// que [`crate::soupcon::DetecteurInfectieux::completude`], qui dérivent le même
/// encadrement de 21 à 31 s.
///
/// La durée **sature**, pour la même raison que dans les deux autres : les
/// champs de [`ReglagesSonde`] sont publics et le profil release du dépôt ne
/// pose pas `overflow-checks`, de sorte qu'une période proche de 2⁶⁴ rendait une
/// mise à mort enroulée, donc annoncée immédiate là où elle est la plus lente.
pub fn retirer(ordre: OrdreDeChute, r: ReglagesSonde) -> Result<Retrait, String> {
    if r.seuil_echec == 0 {
        return Err(
            "seuil d'échec nul refusé : la mise à mort suit `seuil_echec` échecs consécutifs, et \
             à zéro échec il n'y a pas de politique de sonde à simuler — la durée rendue serait \
             une valeur d'allure plausible sans réglage derrière (§6.1 du traité)."
                .to_string(),
        );
    }
    Ok(match ordre {
        OrdreDeChute::DisponibiliteDabord => Retrait {
            validation_de_decalage_achevee: true,
            ..Default::default()
        },
        OrdreDeChute::VivaciteDabord => Retrait {
            // Trois échecs consécutifs à `periode_s` d'intervalle, plus
            // l'expiration du dernier : une trentaine de secondes.
            duree_avant_mise_a_mort: Duree(
                r.periode_s
                    .saturating_mul(u64::from(r.seuil_echec - 1))
                    .saturating_add(r.expiration_s)
                    .saturating_add(r.periode_s),
            ),
            redemarrages: 1,
            reequilibrages_rouverts: 1,
            validation_de_decalage_achevee: false,
        },
    })
}

/// Budget de perturbation (EX-A27).
///
/// > Il empêche l'essaim de s'auto-mutiler, il n'empêche pas le monde de le
/// > mutiler.
#[derive(Clone, Debug)]
pub struct BudgetPerturbation {
    /// Plafond de perturbations simultanées.
    pub plafond: u32,
    /// Perturbations en cours.
    consommees: u32,
    /// Perturbations volontaires que le budget a refusées.
    pub volontaires_refusees: u32,
    /// Perturbations involontaires subies : elles **consomment** le budget sans
    /// pouvoir être empêchées.
    pub involontaires_subies: u32,
    /// Suppressions directes qui ont **contourné** le budget.
    pub contournements_par_suppression_directe: u32,
}

/// Nature d'une perturbation.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Perturbation {
    /// Passe par l'interface d'éviction : le budget **peut la refuser**.
    Volontaire,
    /// Panne matérielle, panique du noyau, partition réseau, éviction pour
    /// manque de ressources : elle **compte contre le budget sans pouvoir être
    /// empêchée**.
    Involontaire,
    /// Suppression directe d'un membre : elle **contourne** le budget. C'est
    /// une action offerte par le simulateur, pas un oubli d'implantation.
    SuppressionDirecte,
    /// Mise à jour progressive : le budget ne la limite pas non plus.
    MiseAJourProgressive,
}

impl BudgetPerturbation {
    /// Budget neuf, à `plafond` perturbations simultanées.
    pub fn nouveau(plafond: u32) -> BudgetPerturbation {
        BudgetPerturbation {
            plafond,
            consommees: 0,
            volontaires_refusees: 0,
            involontaires_subies: 0,
            contournements_par_suppression_directe: 0,
        }
    }

    /// Perturbations en cours, toutes natures confondues.
    pub fn consommees(&self) -> u32 {
        self.consommees
    }

    /// Soumet une perturbation. Rend `true` si elle a lieu.
    pub fn soumettre(&mut self, p: Perturbation) -> bool {
        match p {
            Perturbation::Volontaire => {
                if self.consommees >= self.plafond {
                    self.volontaires_refusees += 1;
                    false
                } else {
                    self.consommees += 1;
                    true
                }
            }
            Perturbation::Involontaire => {
                self.consommees += 1;
                self.involontaires_subies += 1;
                true
            }
            Perturbation::SuppressionDirecte => {
                self.contournements_par_suppression_directe += 1;
                true
            }
            Perturbation::MiseAJourProgressive => true,
        }
    }

    /// Libellé affiché (EX-A27).
    pub const LIBELLE: &'static str =
        "il empêche l'essaim de s'auto-mutiler, il n'empêche pas le monde de le mutiler";
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-A26 — les trois sondes ont trois effets **disjoints**. Aucune ne
    /// remplace une autre.
    #[test]
    fn les_trois_sondes_ont_des_effets_disjoints() {
        let effets: Vec<&str> = [Sonde::Demarrage, Sonde::Vivacite, Sonde::Disponibilite]
            .iter()
            .map(|s| s.effet())
            .collect();
        assert_eq!(effets.len(), 3);
        assert!(effets[1].contains("redémarre"));
        assert!(effets[2].contains("sans redémarrer"));
        assert_ne!(effets[1], effets[2]);
    }

    /// Les défauts documentés sont exposés tels quels, et le coût est Θ(n) par
    /// période.
    #[test]
    fn les_defauts_documentes_et_le_cout_des_sondes() {
        let r = ReglagesSonde::default();
        assert_eq!(
            (
                r.delai_initial_s,
                r.periode_s,
                r.expiration_s,
                r.seuil_succes,
                r.seuil_echec
            ),
            (0, 10, 1, 1, 3),
            "0/10/1/1/3"
        );
        assert_eq!(r.messages_par_periode(100), 200, "2 messages par agent");
    }

    /// EX-A26 — ce que la sonde de disponibilité ne peut pas faire est affiché
    /// en toutes lettres.
    #[test]
    fn la_limite_de_la_sonde_de_disponibilite_est_affichee() {
        assert!(ReglagesSonde::LIMITE_DISPONIBILITE.contains("AUCUN effet"));
        assert!(ReglagesSonde::LIMITE_DISPONIBILITE.contains("sa propre lecture"));
        assert!(ReglagesSonde::BASCULE_VIVACITE.contains("SANS changer la charge"));
    }

    /// EX-A26 — le groupe est un troisième détecteur, avec ses propres
    /// constantes.
    #[test]
    fn le_groupe_est_un_troisieme_detecteur() {
        let s = SeuilsGroupe::default();
        assert_eq!(s.session_ms, 45_000, "agent mort soupçonné");
        assert_eq!(s.max_poll_ms, 300_000, "agent bloqué dans son traitement");
        assert!(s.max_poll_ms > s.session_ms, "deux seuils, deux objets");
    }

    /// EX-A48 — l'ordre inverse est provocable, et chaque retrait « propre »
    /// engendre alors un redémarrage, qui rouvre un rééquilibrage.
    #[test]
    fn lordre_inverse_tue_lagent_en_pleine_vidange() {
        let r = ReglagesSonde::default();
        let nominal = retirer(OrdreDeChute::DisponibiliteDabord, r).expect("réglages documentés");
        assert!(nominal.validation_de_decalage_achevee);
        assert_eq!(nominal.redemarrages, 0);

        let inverse = retirer(OrdreDeChute::VivaciteDabord, r).expect("réglages documentés");
        assert!(!inverse.validation_de_decalage_achevee);
        assert_eq!(inverse.redemarrages, 1);
        assert_eq!(inverse.reequilibrages_rouverts, 1);
        // « une trentaine de secondes » : 10 × 2 + 1 + 10 = 31 s.
        assert_eq!(inverse.duree_avant_mise_a_mort, Duree(31));
    }

    /// SPEC §7, clause 4 — `seuil_echec = 0` faisait déborder `seuil_echec − 1`
    /// sur un entier non signé. Les champs de `ReglagesSonde` sont publics. Il
    /// est désormais **refusé**, et non écrêté : l'écrêtage rendait une mise à
    /// mort en 11 s sous un réglage qui ne décrit aucune politique de sonde.
    #[test]
    fn un_seuil_dechec_nul_est_refuse_au_lieu_detre_ecrete() {
        let r = ReglagesSonde {
            seuil_echec: 0,
            ..ReglagesSonde::default()
        };
        for ordre in [
            OrdreDeChute::VivaciteDabord,
            OrdreDeChute::DisponibiliteDabord,
        ] {
            let motif = retirer(ordre, r).expect_err("seuil nul : refus attendu, pas une durée");
            assert!(motif.contains("zéro échec"), "{motif}");
        }
        // Le réglage voisin passe : la garde ne mange pas le domaine utile.
        let un = ReglagesSonde {
            seuil_echec: 1,
            ..ReglagesSonde::default()
        };
        let inverse = retirer(OrdreDeChute::VivaciteDabord, un).expect("un échec suffit");
        assert_eq!(inverse.duree_avant_mise_a_mort, Duree(11));
    }

    /// Même arbitrage que `sim_core::detecteur` et que
    /// [`crate::soupcon::DetecteurInfectieux::completude`] : la durée
    /// **sature**. Sans cela, une période proche de 2⁶⁴ rendait une mise à mort
    /// enroulée, donc annoncée quasi immédiate là où elle est la plus lente.
    #[test]
    fn la_duree_avant_mise_a_mort_sature_au_lieu_de_senrouler() {
        let r = ReglagesSonde {
            periode_s: 1u64 << 63,
            ..ReglagesSonde::default()
        };
        let inverse = retirer(OrdreDeChute::VivaciteDabord, r).expect("seuil valide");
        assert_eq!(inverse.duree_avant_mise_a_mort, Duree(u64::MAX));
    }

    /// EX-A27 — le budget refuse les volontaires et **subit** les
    /// involontaires.
    #[test]
    fn le_budget_refuse_les_volontaires_et_subit_les_involontaires() {
        let mut b = BudgetPerturbation::nouveau(1);
        assert!(b.soumettre(Perturbation::Volontaire));
        assert!(!b.soumettre(Perturbation::Volontaire), "plafond atteint");
        assert_eq!(b.volontaires_refusees, 1);

        // Une panne matérielle consomme le budget sans pouvoir être empêchée.
        assert!(b.soumettre(Perturbation::Involontaire));
        assert_eq!(b.involontaires_subies, 1);
        assert_eq!(
            b.consommees(),
            2,
            "au-delà du plafond, et rien ne l'empêche"
        );
    }

    /// EX-A27 — la suppression directe **contourne** le budget, et c'est une
    /// action offerte, pas un oubli.
    #[test]
    fn la_suppression_directe_contourne_le_budget() {
        let mut b = BudgetPerturbation::nouveau(0);
        assert!(!b.soumettre(Perturbation::Volontaire));
        assert!(b.soumettre(Perturbation::SuppressionDirecte));
        assert_eq!(b.contournements_par_suppression_directe, 1);
        assert!(
            b.soumettre(Perturbation::MiseAJourProgressive),
            "non limitée non plus"
        );
        assert!(BudgetPerturbation::LIBELLE.contains("il n'empêche pas le monde"));
    }
}
