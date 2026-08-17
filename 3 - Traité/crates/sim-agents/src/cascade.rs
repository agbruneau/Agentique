//! Scénario J — la cascade de l'agent saturé, et AUTO-GUÉRIR (EX-A36, EX-V16).
//!
//! > Aucun agent n'est tombé, et l'essaim s'effondre. (§6.1, figure 6.1, p. 91)
//!
//! **Aucune faute n'est injectée : c'est la condition de démonstration.** La
//! charge franchit la capacité de service, la file de chaque agent croît, sa
//! latence de réponse — **sortie** du modèle (EX-C15) — dépasse
//! `timeoutSeconds`, trois sondes consécutives échouent, l'agent est redémarré
//! bien qu'il soit vivant, ses partitions sont rééquilibrées, la charge se
//! reporte sur les survivants, et la génération suivante commence.

use crate::Bloc;
use sim_core::alea::Alea;
use sim_core::temps::Duree;

/// Le bloc de trois du **scénario J** — la cascade de l'agent saturé (PD8).
pub const BLOC_J: Bloc = Bloc {
    en_clair:
        "Une surveillance automatique redémarre les agents qui ne répondent plus assez vite. Sous \
         forte charge, un agent en bonne santé répond lentement — il est donc déclaré mort et \
         redémarré ; sa charge se reporte sur les autres, qui ralentissent à leur tour. Personne \
         n'est tombé en panne, et la population s'écroule quand même, par l'action du dispositif \
         censé la protéger.",
    these: "Aucun agent n'est tombé, et l'essaim s'effondre.",
    source: "§6.1, p. 90 (3ᵉ éd.) — figure 6.1, p. 91 ; §4.3 tableau 13 ; §7.3 ; §2.3",
    mecanisme_visible:
        "la charge offerte franchit la capacité de service ; la file de chaque agent croît, sa \
         latence de réponse dépasse timeoutSeconds, trois sondes consécutives échouent, l'agent \
         est redémarré bien qu'il soit vivant, ses partitions sont rééquilibrées, la charge se \
         reporte sur les survivants, et la génération suivante commence.",
    ne_demontre_pas:
        "le comportement d'un client de courtier réel ni la performance d'un autoscaleur réel. Le \
         simulateur transpose des valeurs par défaut documentées et périssables ; un déploiement \
         dont les défauts diffèrent produira une autre cascade, pas l'absence de cascade. Qu'une \
         troisième voie existe : le simulateur n'offre que les deux issues du traité et refuse la \
         configuration « détecteur exact ».",
};

/// Débit utile de l'état absorbant, en requêtes par seconde (§2.3 :
/// 280 → 560 → 150). Le système ne remonte jamais au-dessus.
pub const DEBIT_ABSORBANT: f64 = 150.0;

/// Ce que la sonde de vivacité teste.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum SondeVivacite {
    /// Elle mesure la **capacité à répondre dans le délai**, donc la charge.
    /// C'est le réglage qui produit la cascade.
    LatenceDeReponse,
    /// **Le remède du traité** : elle ne teste qu'un blocage constatable sans
    /// travailler — un fil qui n'a pas avancé son décalage. Le scénario montre
    /// que cette bascule supprime la cascade **sans changer la charge**.
    DecalageSeulement,
}

/// Les quatre étapes du bandeau EX-V16.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Etape {
    /// Un agent sature : sa file s'allonge, sa latence de réponse croît.
    Saturation,
    /// La sonde échoue assez de fois : l'agent est **déclaré** mort. Il ne
    /// l'est pas.
    MortDeclaree,
    /// Le rééquilibrage redistribue ses partitions.
    Reequilibrage,
    /// Sa charge tombe sur les survivants, qui saturent à leur tour.
    ReportDeCharge,
}

/// Paramètres du volet 1.
#[derive(Clone, Copy, Debug)]
pub struct Params {
    /// Taille de l'essaim.
    pub n: u32,
    /// Charge offerte, en requêtes par seconde.
    pub charge_par_s: f64,
    /// Temps de service par requête, en millisecondes. Fixe la capacité.
    pub temps_service_ms: f64,
    /// `timeoutSeconds` de la sonde — la borne connue la plus serrée.
    pub timeout_s: f64,
    /// `periodSeconds`.
    pub periode_s: f64,
    /// `failureThreshold`.
    pub seuil_echec: u32,
    /// Durée de reconstruction d'état — ce qui reporte la charge sur les
    /// survivants.
    pub reconstruction_s: f64,
    /// Ce que la sonde de vivacité mesure réellement.
    pub sonde: SondeVivacite,
    /// Régime métastable du §2.3 : 280 → 560 → 150 req/s.
    pub metastable: bool,
}

impl Default for Params {
    fn default() -> Self {
        Params {
            n: 16,
            // Capacité de l'essaim intact : 16 × 1 000 / 5 = 3 200 req/s. La
            // charge par défaut la franchit — c'est la condition du scénario.
            charge_par_s: 3_400.0,
            temps_service_ms: 5.0,
            timeout_s: 1.0,
            periode_s: 10.0,
            seuil_echec: 3,
            reconstruction_s: 10.0,
            sonde: SondeVivacite::LatenceDeReponse,
            metastable: false,
        }
    }
}

impl Params {
    /// Capacité de service de l'essaim, en requêtes par seconde.
    pub fn capacite(&self, agents_actifs: u32) -> f64 {
        agents_actifs as f64 * 1_000.0 / self.temps_service_ms
    }

    /// Sous le seuil de saturation : la charge tient dans la capacité.
    pub fn sous_le_seuil() -> Params {
        Params {
            charge_par_s: 1_600.0,
            ..Params::default()
        }
    }

    /// Le remède du traité, **à charge inchangée**.
    pub fn decalage_seulement() -> Params {
        Params {
            sonde: SondeVivacite::DecalageSeulement,
            ..Params::default()
        }
    }
}

/// L'état d'un agent.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum EtatAgent {
    Actif,
    /// En redémarrage : il ne sert plus, et sa charge est reportée.
    EnRedemarrage(u32),
}

/// La cascade.
pub struct Cascade {
    /// Préréglage en vigueur.
    pub params: Params,
    etats: Vec<EtatAgent>,
    echecs_consecutifs: Vec<u32>,
    /// **Compteur de pannes réelles.** Il reste à zéro : c'est tout le point.
    ///
    /// Aucun code ne l'incrémente, et c'est **structurel** : `Cascade` n'injecte
    /// aucune faute, et le modèle de faute de `sim-core` n'est branché sur aucun
    /// scénario. Les assertions `pannes_reelles == 0` ne peuvent donc pas
    /// échouer — ce qu'elles établissent est la lecture du code, pas une mesure.
    /// Ce qui se mesure vraiment est le contraste : `redemarrages > 0` avec
    /// celui-ci à zéro.
    pub pannes_reelles: u32,
    /// Redémarrages déclarés — des morts qui n'en sont pas.
    pub redemarrages: u32,
    /// Générations de la cascade : une vague de redémarrages en est une.
    pub generations: u32,
    /// Étapes du bandeau EX-V16 déjà allumées.
    pub etapes: Vec<Etape>,
    /// Débit servi à chaque pas.
    pub debit_servi: Vec<f64>,
    /// Latence de réponse au 99ᵉ centile, par pas.
    pub l99_reponse_s: Vec<f64>,
    /// Messages de rééquilibrage cumulés.
    pub messages_reequilibrage: u64,
    pas: u32,
}

impl Cascade {
    /// Prépare la population. Les sondes reçoivent ici leur **décalage de
    /// phase**, sans lequel la cascade n'aurait pas de générations.
    pub fn nouvelle(params: Params) -> Cascade {
        // Les sondes ne démarrent pas toutes au même instant : chaque agent a
        // sa phase. Sans ce décalage, toute la population atteindrait le seuil
        // d'échecs au même pas et tomberait d'un bloc — il n'y aurait pas de
        // **générations**, et donc rien de ce que le scénario doit montrer.
        let phases = (0..params.n)
            .map(|i| i % params.seuil_echec.max(1))
            .collect();
        Cascade {
            etats: vec![EtatAgent::Actif; params.n as usize],
            echecs_consecutifs: phases,
            params,
            pannes_reelles: 0,
            redemarrages: 0,
            generations: 0,
            etapes: Vec::new(),
            debit_servi: Vec::new(),
            l99_reponse_s: Vec::new(),
            messages_reequilibrage: 0,
            pas: 0,
        }
    }

    fn actifs(&self) -> u32 {
        self.etats.iter().filter(|e| **e == EtatAgent::Actif).count() as u32
    }

    fn allumer(&mut self, e: Etape) {
        if !self.etapes.contains(&e) {
            self.etapes.push(e);
        }
    }

    /// Un pas de sonde, de durée `periode_s`.
    pub fn pas(&mut self, _alea: &mut Alea) {
        self.pas += 1;
        let actifs = self.actifs();

        let charge = self.params.charge_par_s;
        let capacite = self.params.capacite(actifs);

        // **Régime métastable (§2.3).** Une fois la bascule franchie, le débit
        // utile s'effondre sous sa valeur d'avant et **y reste**, même si la
        // charge offerte redescend : la capacité libérée est consommée par le
        // travail réémis. C'est un état **absorbant**, et non un creux dont le
        // système remonte — 280 avant, 560 au pic, 150 après.
        let servi = if self.params.metastable && self.generations >= 1 {
            DEBIT_ABSORBANT.min(capacite)
        } else {
            charge.min(capacite)
        };
        self.debit_servi.push(servi);

        // La latence croît avec l'utilisation, et diverge sous saturation.
        //
        // Ce n'est **pas** EX-C15 : c'est une formule fermée M/M/1 sur des
        // agrégats — une seule valeur pour toute la population, sans file par
        // agent ni arriéré. EX-C15 (`sim_core::service`) demande que la latence
        // émerge de la file de chaque agent, et n'est branchée nulle part ; le
        // manque est consigné dans `hors_perimetre()`. Conséquence directe : les
        // générations de la cascade viennent du décalage de phase posé au
        // constructeur, pas de la saturation.
        let utilisation = if capacite > 0.0 { charge / capacite } else { f64::INFINITY };
        let l99 = if utilisation < 1.0 {
            // File M/M/1 : la latence explose en 1/(1 − ρ).
            self.params.temps_service_ms / 1_000.0 / (1.0 - utilisation)
        } else {
            f64::INFINITY
        };
        self.l99_reponse_s.push(l99);
        if utilisation >= 1.0 {
            self.allumer(Etape::Saturation);
        }

        // Les sondes.
        let mut morts_declarees = Vec::new();
        for i in 0..self.params.n as usize {
            match self.etats[i] {
                EtatAgent::EnRedemarrage(reste) => {
                    self.etats[i] = if reste <= 1 {
                        EtatAgent::Actif
                    } else {
                        EtatAgent::EnRedemarrage(reste - 1)
                    };
                    continue;
                }
                EtatAgent::Actif => {}
            }

            let echec = match self.params.sonde {
                // La sonde mesure la charge : un agent saturé mais **vivant**
                // est classé mort.
                SondeVivacite::LatenceDeReponse => l99 > self.params.timeout_s,
                // Le remède : elle ne teste qu'un blocage constatable sans
                // travailler. Un agent lent qui avance n'échoue jamais.
                SondeVivacite::DecalageSeulement => false,
            };

            if echec {
                self.echecs_consecutifs[i] += 1;
                if self.echecs_consecutifs[i] >= self.params.seuil_echec {
                    morts_declarees.push(i);
                }
            } else {
                self.echecs_consecutifs[i] = 0;
            }
        }

        if !morts_declarees.is_empty() {
            self.generations += 1;
            self.allumer(Etape::MortDeclaree);
            self.allumer(Etape::Reequilibrage);
            self.allumer(Etape::ReportDeCharge);
            let pas_de_reconstruction =
                (self.params.reconstruction_s / self.params.periode_s).ceil() as u32;
            for i in morts_declarees {
                self.redemarrages += 1;
                self.echecs_consecutifs[i] = 0;
                self.etats[i] = EtatAgent::EnRedemarrage(pas_de_reconstruction.max(1));
                // Chaque mort déclarée coûte un rééquilibrage.
                self.messages_reequilibrage += 8 * self.params.n as u64;
            }
        }
    }

    /// L'essaim sert-il encore quelque chose ?
    pub fn sert_encore(&self) -> bool {
        self.actifs() > 0
    }

    /// **EX-V16** — le bandeau, avec son titre et le compteur de pannes réelles.
    pub fn bandeau(&self) -> String {
        format!(
            "**aucun agent n'est tombé, et l'essaim s'effondre** — étapes allumées : {} ; \
             pannes réelles : {} ; générations : {} ; redémarrages : {}",
            self.etapes.len(),
            self.pannes_reelles,
            self.generations,
            self.redemarrages
        )
    }
}

// ---------------------------------------------------------------------------
// EX-A36 — AUTO-GUÉRIR
// ---------------------------------------------------------------------------

/// **EX-A36** — dix lignes, signature complète.
///
/// Modèle : crash-arrêt et omission ; partiellement synchrone, Δ inconnue ;
/// **détecteur incomplet ET inexact** ; budget de perturbation `B` tenu derrière
/// un quorum de taille `q`, **lu au moment de l'action et non au moment du
/// soupçon**.
pub struct AutoGuerir {
    /// Taille du sous-groupe de sondage indirect.
    pub s: u8,
    /// Taille du quorum du budget.
    pub q: u32,
    /// Délai de refroidissement : empêche la boucle de se réamorcer sur son
    /// propre effet.
    pub t_froid: Duree,
    /// Durée réelle d'un redémarrage.
    pub duree_redemarrage: Duree,
    /// L'agent est-il du côté minoritaire d'une partition ?
    pub cote_minoritaire: bool,
    /// Réparations effectivement engagées.
    pub reparations: u32,
    /// Réparations refusées faute de budget — le quorum a dit non.
    pub budgets_refuses: u32,
    /// Vrai si la boucle s'est réamorcée sur son propre effet.
    pub boucle_auto_entretenue: bool,
    dernier_declenchement: Option<sim_core::temps::Instant>,
}

impl AutoGuerir {
    /// Boucle d'auto-guérison. `t_froid` trop court laisse la boucle se
    /// réamorcer sur son propre effet, et c'est un mode de défaillance nommé.
    pub fn nouveau(s: u8, q: u32, t_froid: Duree, duree_redemarrage: Duree) -> AutoGuerir {
        AutoGuerir {
            s,
            q,
            t_froid,
            duree_redemarrage,
            cote_minoritaire: false,
            reparations: 0,
            budgets_refuses: 0,
            boucle_auto_entretenue: false,
            dernier_declenchement: None,
        }
    }

    /// Coût d'un soupçon confirmé : **2 + 4s + 2q messages et 4 tours**, dont un
    /// seul — l'acquisition du budget — bloque sur un quorum.
    pub fn cout_soupcon_confirme(&self) -> (u64, u64) {
        (2 + 4 * self.s as u64 + 2 * self.q as u64, 4)
    }

    /// Tente une réparation.
    ///
    /// Le budget est **lu au moment de l'action**, pas au moment du soupçon :
    /// c'est la ligne 7, et c'est elle qui fait échouer la réparation du côté
    /// minoritaire d'une partition.
    pub fn reparer(&mut self, maintenant: sim_core::temps::Instant) -> Result<(), String> {
        // Refroidissement : la boucle ne se réamorce pas sur son propre effet.
        if let Some(dernier) = self.dernier_declenchement {
            if maintenant.0 < dernier.0 + self.t_froid.0 {
                return Err("en refroidissement".to_string());
            }
            // Si T_froid est plus court que le redémarrage, un soupçon repasse
            // sur un agent en cours de démarrage : la boucle ne termine pas.
            if self.t_froid < self.duree_redemarrage {
                self.boucle_auto_entretenue = true;
            }
        }

        if self.cote_minoritaire {
            self.budgets_refuses += 1;
            return Err(
                "acquisition du budget échouée : la ligne 7 s'applique, **aucun redémarrage n'a \
                 lieu**. L'auto-guérison perd sa vivacité exactement dans la circonstance qui la \
                 motive — c'est le **prix assumé de sa sûreté**, pas un défaut (§7.3)."
                    .to_string(),
            );
        }

        self.dernier_declenchement = Some(maintenant);
        self.reparations += 1;
        Ok(())
    }

    /// Condition d'arrêt : le succès de la sonde de démarrage.
    pub const CONDITION_DARRET: &'static str =
        "le succès de la sonde de démarrage — et rien d'autre (§7.3, EX-A36)";
}

#[cfg(test)]
mod tests {
    use super::*;

    fn derouler(params: Params, pas: u32) -> Cascade {
        let mut c = Cascade::nouvelle(params);
        let mut alea = Alea::nouveau(1);
        for _ in 0..pas {
            c.pas(&mut alea);
        }
        c
    }

    /// **Critère (1) du scénario J** — sous le seuil de saturation, **zéro
    /// redémarrage** sur toute la durée.
    #[test]
    fn critere_1a_sous_le_seuil_aucun_redemarrage() {
        let c = derouler(Params::sous_le_seuil(), 60);
        assert_eq!(c.redemarrages, 0);
        assert_eq!(c.generations, 0);
        assert_eq!(c.pannes_reelles, 0);
    }

    /// **Critère (1)** — au-dessus, la cascade est **complète en trois
    /// générations**, sans qu'aucune faute ait été injectée, et le compteur de
    /// pannes affiche **0**.
    #[test]
    fn critere_1b_la_cascade_est_complete_en_trois_generations_sans_aucune_panne() {
        let c = derouler(Params::default(), 60);
        assert!(
            c.generations >= 3,
            "la cascade doit atteindre trois générations, or {}",
            c.generations
        );
        assert_eq!(c.pannes_reelles, 0, "AUCUNE faute n'a été injectée");
        assert!(c.redemarrages > 0, "et pourtant des agents ont été redémarrés");
        assert_eq!(c.etapes.len(), 4, "les quatre étapes du bandeau sont allumées");
        assert!(c.bandeau().contains("pannes réelles : 0"));
    }

    /// **Critère (2)** — la bascule « décalage seulement » supprime la cascade
    /// **à charge inchangée**.
    #[test]
    fn critere_2a_le_decalage_seulement_supprime_la_cascade_a_charge_inchangee() {
        let avec = derouler(Params::default(), 60);
        let sans = derouler(Params::decalage_seulement(), 60);
        assert_eq!(
            avec.params.charge_par_s, sans.params.charge_par_s,
            "la charge est identique — c'est le point"
        );
        assert!(avec.redemarrages > 0);
        assert_eq!(sans.redemarrages, 0, "le remède supprime la cascade");
        assert_eq!(sans.generations, 0);
    }

    /// **Critère (2)** — … et un `timeoutSeconds` plus généreux **ne la
    /// supprime pas**. C'est le critère qui compte : le remède n'est pas un
    /// réglage plus généreux.
    ///
    /// Il ne la retarde même pas, et il faut le dire : sous saturation, la
    /// latence de la file M/M/1 **diverge**, de sorte qu'aucune valeur finie de
    /// `timeoutSeconds` n'est franchie plus tard qu'une autre. La cascade est
    /// bit pour bit la même. Ce que l'expiration allonge est ailleurs — dans la
    /// détection **vraie** d'un agent réellement arrêté, dont la complétude
    /// croît avec elle (§7.3, p. 112) —, et c'est exactement le mauvais échange :
    /// on paie en détection sans rien acheter en fausses suspicions.
    #[test]
    fn critere_2b_un_timeout_plus_genereux_ne_supprime_pas_la_cascade() {
        let serre = derouler(Params::default(), 60);
        let genereux = derouler(
            Params {
                timeout_s: 30.0,
                ..Params::default()
            },
            60,
        );
        assert!(
            genereux.redemarrages > 0,
            "un timeout plus généreux ne supprime pas la cascade"
        );
        assert_eq!(
            (genereux.redemarrages, genereux.generations),
            (serre.redemarrages, serre.generations),
            "sous saturation la latence diverge : le réglage ne retarde rien du tout"
        );
        // Et il allonge la détection vraie : la complétude du détecteur croît
        // avec l'expiration.
        let (min_serre, _) =
            crate::soupcon::DetecteurInfectieux::completude(10, 1, 3).expect("réglage documenté");
        let (min_genereux, _) =
            crate::soupcon::DetecteurInfectieux::completude(10, 30, 3).expect("réglage documenté");
        assert!(min_genereux > min_serre, "la détection vraie s'allonge");
    }

    /// §2.3 — le régime **métastable** : le débit s'effondre sous sa valeur
    /// d'avant et **y reste**. C'est l'état absorbant.
    #[test]
    fn le_regime_metastable_a_un_etat_absorbant() {
        let c = derouler(
            Params {
                metastable: true,
                ..Params::default()
            },
            60,
        );
        let debut = c.debit_servi.first().copied().unwrap_or(0.0);
        // Le régime absorbant se lit sur la fin de la trajectoire, pas sur un
        // pas isolé : le dernier pas peut tomber pendant une vague de
        // redémarrages, où la capacité est nulle pour une autre raison.
        let n = c.debit_servi.len();
        let fin: f64 = c.debit_servi[n - 10..].iter().sum::<f64>() / 10.0;
        assert!(
            fin < debut,
            "le débit doit rester sous sa valeur d'avant : {debut} puis {fin}"
        );
        assert!(
            fin <= 150.0,
            "l'état absorbant plafonne à 150 req/s, or {fin}"
        );
        // Et il ne remonte jamais : c'est ce qui le rend absorbant.
        assert!(
            c.debit_servi[n - 10..].iter().all(|d| *d <= 150.0),
            "aucun pas de la fin ne doit repasser au-dessus"
        );
    }

    /// **EX-A36** — le coût d'un soupçon confirmé : 2 + 4s + 2q messages et 4
    /// tours.
    #[test]
    fn le_cout_dauto_guerir_est_celui_du_traite() {
        let a = AutoGuerir::nouveau(3, 5, Duree(120), Duree(60));
        assert_eq!(a.cout_soupcon_confirme(), (2 + 12 + 10, 4));
        assert!(AutoGuerir::CONDITION_DARRET.contains("sonde de démarrage"));
    }

    /// **Critère (13)** — sous partition isolant une minorité, l'acquisition du
    /// budget échoue et **aucun redémarrage n'a lieu** du côté minoritaire.
    #[test]
    fn critere_13a_le_cote_minoritaire_ne_se_repare_plus() {
        let mut majoritaire = AutoGuerir::nouveau(3, 5, Duree(120), Duree(60));
        let mut minoritaire = AutoGuerir::nouveau(3, 5, Duree(120), Duree(60));
        minoritaire.cote_minoritaire = true;

        assert!(majoritaire.reparer(sim_core::temps::Instant(0)).is_ok());
        let e = minoritaire.reparer(sim_core::temps::Instant(0)).unwrap_err();
        assert!(e.contains("aucun redémarrage n'a lieu"), "{e}");
        assert!(e.contains("prix assumé de sa sûreté"), "{e}");
        assert_eq!(minoritaire.reparations, 0);
        assert_eq!(majoritaire.reparations, 1);
    }

    /// **Critère (13)** — avec `T_froid` plus court que la durée de
    /// redémarrage, la boucle **ne termine pas**.
    #[test]
    fn critere_13b_t_froid_trop_court_produit_une_boucle_auto_entretenue() {
        let mut a = AutoGuerir::nouveau(3, 5, Duree(10), Duree(60));
        a.reparer(sim_core::temps::Instant(0)).unwrap();
        a.reparer(sim_core::temps::Instant(100)).unwrap();
        assert!(a.boucle_auto_entretenue, "T_froid < redémarrage : la boucle se réamorce");

        let mut sain = AutoGuerir::nouveau(3, 5, Duree(120), Duree(60));
        sain.reparer(sim_core::temps::Instant(0)).unwrap();
        sain.reparer(sim_core::temps::Instant(200)).unwrap();
        assert!(!sain.boucle_auto_entretenue);
    }

    /// Le refroidissement empêche un second déclenchement trop rapproché.
    #[test]
    fn le_refroidissement_empeche_un_second_declenchement() {
        let mut a = AutoGuerir::nouveau(3, 5, Duree(120), Duree(60));
        a.reparer(sim_core::temps::Instant(0)).unwrap();
        assert!(a.reparer(sim_core::temps::Instant(50)).is_err());
        assert!(a.reparer(sim_core::temps::Instant(200)).is_ok());
    }

    /// PD8 — le bloc de trois.
    #[test]
    fn le_scenario_porte_son_bloc_de_trois() {
        assert!(BLOC_J.these.contains("ucun agent n'est tombé"));
        assert!(BLOC_J.ne_demontre_pas.contains("troisième voie"));
    }
}
