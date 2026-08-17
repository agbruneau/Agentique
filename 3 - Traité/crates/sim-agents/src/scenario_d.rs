//! Scénario D — La chute de R1.
//!
//! Rejeu **pas à pas**, contrôlé par l'utilisateur, du déroulé du §2.1 du traité à k = 3
//! et m = 2. Ce n'est pas une animation : chaque instant est un pas explicite,
//! parce que la thèse tient à l'ordre exact des événements et qu'un déroulé
//! automatique la rendrait inobservable.
//!
//! Ce que le scénario établit : le nombre de disparitions auquel un
//! enregistrement survit est **m − 1**, jamais k − 1.

use crate::Bloc;
use sim_core::oracle::Registre;
use sim_core::registre::RegistreHypotheses;
use sim_core::temps::{Duree, Instant};
use sim_milieu::replication::{Isr, Refus};

/// Le bloc de trois du **scénario D** — la chute de R1 (PD8).
pub const BLOC_D: Bloc = Bloc {
    en_clair:
        "Une donnée est recopiée sur trois machines pour survivre à des pannes. On croit donc \
         qu'elle survit à deux disparitions. Elle n'en supporte qu'une : ce qui compte n'est pas \
         le nombre de copies demandées, mais le nombre de copies effectivement à jour au moment \
         où l'écriture a été acceptée. Et rien, nulle part, ne signale l'écart.",
    these: "Le nombre de disparitions auquel r₂ survit n'est pas k − 1 = 2, il est m − 1 = 1.",
    source: "§2.1, p. 26 (3ᵉ éd.) — figure 2.1c, p. 28 ; §6.1 pour l'ISR, R2 et le temporisateur",
    mecanisme_visible:
        "porter m à 1 active le préréglage « ISR muet ». L'ISR se réduit au seul meneur sous \
         charge, les producteurs continuent de recevoir leurs accusés, la largeur d'accusé \
         affichée tombe à 1 — et aucune erreur n'est émise. C'est le seul endroit du produit où \
         l'affichage vaut mieux que le protocole.",
    ne_demontre_pas:
        "que la documentation du courtier se contredise. Elle conditionne sa garantie à ce qu'au \
         moins une réplique reste synchronisée, et à t₄ aucune ne l'est. Il ne démontre rien non \
         plus sur un courtier déployé : le simulateur transpose la documentation, pas \
         l'implantation, et un écart entre les deux est invisible d'ici (§2.3 du PRD).",
};

/// Les instants du déroulé, tels que le tableau du §2.1 du traité les écrit.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Etape {
    /// Avant tout : trois répliques synchronisées.
    Depart,
    /// t₀ — r₁ accusé, largeur 3.
    T0,
    /// t₁ — C retiré pour retard. **Aucune panne**, compteur à zéro.
    T1,
    /// t₂ — r₂ accusé, largeur 2 ; C ne le détient pas.
    T2,
    /// t₃ — B s'arrête ; sous m, la partition cesse d'accuser.
    T3,
    /// t₄ — A s'arrête ; seul C vit, et il ne détient pas r₂.
    T4,
    /// Le choix : attendre le retour d'un membre, ou élire C.
    Choix,
}

impl Etape {
    /// L'étape suivante. `Choix` est absorbante : le scénario s'y arrête.
    pub fn suivante(self) -> Etape {
        match self {
            Etape::Depart => Etape::T0,
            Etape::T0 => Etape::T1,
            Etape::T1 => Etape::T2,
            Etape::T2 => Etape::T3,
            Etape::T3 => Etape::T4,
            Etape::T4 | Etape::Choix => Etape::Choix,
        }
    }

    /// Le libellé du pas, avec ce qu'il faut observer à cet instant.
    pub fn libelle(self) -> &'static str {
        match self {
            Etape::Depart => "départ — {A, B, C} synchronisées",
            Etape::T0 => "t₀ — r₁ accusé, largeur 3",
            Etape::T1 => "t₁ — C retiré pour retard : aucune panne, compteur à zéro",
            Etape::T2 => "t₂ — r₂ accusé, largeur 2 ; C ne le détient pas",
            Etape::T3 => "t₃ — B s'arrête ; sous m, la partition cesse d'accuser",
            Etape::T4 => "t₄ — A s'arrête ; seul C vit, et il ne détient pas r₂",
            Etape::Choix => "le choix : attendre un membre, ou élire C",
        }
    }
}

/// Ce que l'utilisateur choisit à la fin, et il n'y a pas de troisième option.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Choix {
    /// R1 préservée, indisponibilité **non bornée** — jamais « grande ».
    AttendreUnMembre,
    /// r₂ détruit chez ses deux détenteurs par troncature.
    ElireHorsIsr,
}

/// L'état du scénario.
pub struct ScenarioD {
    /// La partition répliquée, avec son ISR et son seuil `m`.
    pub isr: Isr,
    /// R1 et R2, armés dès le départ.
    pub oracles: Registre,
    /// Le temporisateur d'appartenance, déclaré comme hypothèse forte.
    pub hypotheses: RegistreHypotheses,
    /// Le pas courant.
    pub etape: Etape,
    /// Récit des pas franchis, avec ce qui a été observé à chacun.
    pub recit: Vec<String>,
    /// Instant logique du pas courant, en secondes.
    horloge: Instant,
}

impl ScenarioD {
    /// Construit le scénario. `m = 1` active le préréglage « ISR muet ».
    pub fn nouveau(k: u32, m: u32, temporisateur_s: u64) -> ScenarioD {
        let isr = Isr::nouvelle(k, m, Duree(temporisateur_s));
        let mut oracles = Registre::nouveau();
        let mut hypotheses = RegistreHypotheses::nouveau();
        isr.armer_oracles(&mut oracles);
        isr.declarer_hypotheses(&mut hypotheses);
        ScenarioD {
            isr,
            oracles,
            hypotheses,
            etape: Etape::Depart,
            recit: Vec::new(),
            horloge: Instant(0),
        }
    }

    /// Les défauts du scénario : k = 3, m = 2, temporisateur 30 s.
    pub fn defaut() -> ScenarioD {
        ScenarioD::nouveau(3, 2, 30)
    }

    /// Le préréglage « ISR muet » : m = 1.
    pub fn isr_muet() -> ScenarioD {
        ScenarioD::nouveau(3, 1, 30)
    }

    fn noter(&mut self, ligne: String) {
        self.recit.push(ligne);
    }

    /// Réplique un enregistrement chez les membres courants de l'ISR.
    fn repliquer_isr(&mut self) {
        let fin = self.isr.fin_meneur;
        for id in self.isr.isr().to_vec() {
            self.isr.repliquer(id, fin, self.horloge);
        }
    }

    /// Franchit un pas. Rend le libellé de l'étape atteinte.
    pub fn pas(&mut self) -> String {
        self.horloge = Instant(self.horloge.0 + 1);
        self.etape = self.etape.suivante();
        match self.etape {
            Etape::T0 => {
                match self.isr.ecrire() {
                    Ok(d) => {
                        self.repliquer_isr();
                        let l = self.isr.derniere_largeur().unwrap_or(0);
                        self.noter(format!("r₁ écrit au décalage {d}, accusé à largeur {l}"));
                    }
                    Err(e) => self.noter(format!("r₁ refusé : {e:?}")),
                }
            }
            Etape::T1 => {
                // Retrait pour retard : le compteur de pannes ne bouge pas.
                self.isr.retirer_pour_retard(2);
                self.noter(format!(
                    "C retiré de l'ISR pour retard ; pannes = {}, retraits pour retard = {}",
                    self.isr.pannes, self.isr.retraits_pour_retard
                ));
            }
            Etape::T2 => {
                match self.isr.ecrire() {
                    Ok(d) => {
                        self.repliquer_isr();
                        let l = self.isr.derniere_largeur().unwrap_or(0);
                        self.noter(format!(
                            "r₂ écrit au décalage {d}, accusé à largeur {l} — C ne le détient pas"
                        ));
                    }
                    Err(Refus::SousLeSeuil { isr, m }) => self.noter(format!(
                        "r₂ refusé : |ISR| = {isr} sous m = {m}"
                    )),
                    Err(e) => self.noter(format!("r₂ refusé : {e:?}")),
                }
            }
            Etape::T3 => {
                self.isr.arreter(1);
                let refus = self.isr.ecrire();
                self.noter(format!(
                    "B arrêté ; pannes = {} ; nouvelle écriture : {}",
                    self.isr.pannes,
                    match refus {
                        Err(Refus::SousLeSeuil { isr, m }) =>
                            format!("refusée, |ISR| = {isr} sous m = {m}"),
                        Err(e) => format!("refusée, {e:?}"),
                        Ok(_) => "acceptée — la partition accuse encore".to_string(),
                    }
                ));
            }
            Etape::T4 => {
                self.isr.arreter(0);
                self.noter(format!(
                    "A arrêté ; pannes = {} ; seul C vit, et sa fin de journal est {}",
                    self.isr.pannes,
                    self.isr.repliques.iter().find(|r| r.id == 2).map(|r| r.fin).unwrap_or(0)
                ));
            }
            _ => {}
        }
        self.isr.verifier_r1(&mut self.oracles, self.horloge);
        self.etape.libelle().to_string()
    }

    /// Applique le choix final. Il n'y a pas de troisième option.
    pub fn choisir(&mut self, choix: Choix) -> String {
        self.horloge = Instant(self.horloge.0 + 1);
        self.etape = Etape::Choix;
        let message = match choix {
            Choix::AttendreUnMembre => {
                self.isr.election_hors_isr = false;
                match self.isr.elire() {
                    Some(id) => format!("meneur {id} élu dans l'ISR"),
                    None => "aucun membre de l'ISR n'est vivant : la partition attend. R1 est \
                             préservée, et l'indisponibilité est **non bornée** — pas « grande », \
                             non bornée."
                        .to_string(),
                }
            }
            Choix::ElireHorsIsr => {
                self.isr.election_hors_isr = true;
                match self.isr.elire() {
                    Some(id) => format!(
                        "meneur {id} élu **hors ISR** ; {} enregistrement(s) détruit(s) par \
                         troncature chez leurs détenteurs",
                        self.isr.tronques
                    ),
                    None => "aucune réplique vivante".to_string(),
                }
            }
        };
        self.noter(message.clone());
        self.isr.verifier_r1(&mut self.oracles, self.horloge);
        message
    }

    /// Déroule tout le scénario jusqu'au choix.
    pub fn derouler(&mut self, choix: Choix) {
        while self.etape != Etape::T4 {
            self.pas();
        }
        self.choisir(choix);
    }

    /// R1 a-t-elle été violée, et à quel instant ?
    pub fn violation_r1(&self) -> Option<(u64, &str)> {
        self.oracles
            .violations()
            .iter()
            .find(|v| v.oracle == sim_milieu::R1)
            .map(|v| (v.date.0, v.details.as_str()))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Critère d'acceptation (1) — R1 est violée **exactement** au choix
    /// d'élire hors ISR, et le compteur de pannes affiche 2 à cet instant :
    /// k ≥ f + 1 est respecté à l'égalité, et pourtant l'enregistrement est
    /// perdu. C'est toute la thèse.
    #[test]
    fn r1_tombe_avec_election_hors_isr_et_pas_avant() {
        let mut d = ScenarioD::defaut();
        // Aucun pas du déroulé ne viole R1 : la perte se joue au choix.
        while d.etape != Etape::T4 {
            d.pas();
            assert!(
                d.violation_r1().is_none(),
                "R1 violée trop tôt, à l'étape {:?}",
                d.etape
            );
        }
        assert_eq!(d.isr.pannes, 2, "deux arrêts : B puis A");
        assert_eq!(d.isr.retraits_pour_retard, 1, "C retiré sans être tombé");

        d.choisir(Choix::ElireHorsIsr);
        let (_, details) = d.violation_r1().expect("R1 doit tomber à l'élection hors ISR");
        assert!(details.contains("largeur 2"), "{details}");
        assert!(d.isr.tronques > 0, "la troncature doit détruire r₂");
    }

    /// … et **jamais** avec l'attente. Le prix payé est l'indisponibilité, qui
    /// est non bornée et affichée comme telle.
    #[test]
    fn r1_tient_si_lon_attend_un_membre() {
        let mut d = ScenarioD::defaut();
        d.derouler(Choix::AttendreUnMembre);
        assert!(d.violation_r1().is_none(), "{:?}", d.oracles.violations());
        assert_eq!(d.isr.tronques, 0);
        assert!(
            d.recit.last().unwrap().contains("non bornée"),
            "{}",
            d.recit.last().unwrap()
        );
    }

    /// §2.1 du traité — r₂ est accusé à largeur 2, donc il survit à **m − 1 = 1**
    /// disparition, et non à k − 1 = 2. Le chiffre se lit dans la mesure.
    #[test]
    fn la_largeur_daccuse_de_r2_vaut_deux_et_non_trois() {
        let mut d = ScenarioD::defaut();
        d.pas(); // t₀
        assert_eq!(d.isr.derniere_largeur(), Some(3), "r₁ accusé à largeur 3");
        d.pas(); // t₁ : C retiré
        d.pas(); // t₂
        assert_eq!(d.isr.derniere_largeur(), Some(2), "r₂ accusé à largeur 2");
        let (survie, _) = d.isr.tolerances();
        assert_eq!(survie, Some(1), "largeur 2 → survit à 1 disparition, pas 2");
    }

    /// EX-M07 — un retrait pour retard n'incrémente **jamais** le compteur de
    /// pannes. Les confondre rendrait la chute de R1 inexplicable.
    #[test]
    fn un_retrait_pour_retard_nest_pas_une_panne() {
        let mut d = ScenarioD::defaut();
        d.pas();
        d.pas(); // t₁ : C retiré pour retard
        assert_eq!(d.isr.pannes, 0);
        assert_eq!(d.isr.retraits_pour_retard, 1);
        assert_eq!(d.isr.taille_isr(), 2);
    }

    /// Critère d'acceptation (2) — le préréglage `min.insync.replicas = 1` fait
    /// tomber la tolérance à 0 **sans qu'aucune erreur ne soit émise**, et
    /// l'interface le nomme.
    #[test]
    fn le_prereglage_isr_muet_ne_leve_aucune_erreur() {
        let mut d = ScenarioD::isr_muet();
        d.pas(); // t₀
        d.pas(); // t₁ : C retiré
        d.pas(); // t₂
        d.pas(); // t₃ : B s'arrête — |ISR| = 1, mais m = 1 : on accuse encore

        // Le producteur ne reçoit aucun refus : c'est cela, la perte muette.
        assert!(
            d.isr.ecrire().is_ok(),
            "avec m = 1 la partition continue d'accuser, c'est le point"
        );
        // Et l'enregistrement qu'il vient d'écrire est accusé à largeur 1,
        // donc il ne survit à **aucune** disparition. La tolérance mesurée
        // porte sur le dernier enregistrement validé, pas sur les précédents :
        // r₂ avait été accusé à largeur 2 et garde sa tolérance de 1.
        let fin = d.isr.fin_meneur;
        for id in d.isr.isr().to_vec() {
            d.isr.repliquer(id, fin, Instant(10));
        }
        assert_eq!(d.isr.derniere_largeur(), Some(1));
        let (survie, _) = d.isr.tolerances();
        assert_eq!(survie, Some(0), "la tolérance est tombée à 0 disparition");

        // Rien dans le protocole ne le dit ; seul l'affichage le trahit.
        let avertissement = d.isr.perte_muette().expect("l'interface doit le nommer");
        assert!(avertissement.contains("aucune erreur n'est émise"), "{avertissement}");
        assert!(avertissement.contains("EX-M15"), "{avertissement}");
    }

    /// Le même déroulé sous m = 2 refuse l'écriture : le seuil est la **seule**
    /// information que le producteur reçoit.
    #[test]
    fn sous_le_seuil_lecriture_est_refusee() {
        let mut d = ScenarioD::defaut();
        d.pas();
        d.pas();
        d.pas();
        d.pas(); // t₃ : |ISR| = 1 < m = 2
        assert_eq!(
            d.isr.ecrire(),
            Err(Refus::SousLeSeuil { isr: 1, m: 2 })
        );
        assert!(d.isr.perte_muette().is_none(), "avec m = 2, la perte n'est pas muette");
    }

    /// F2 — **la page exacte du bloc D**, seule chose que les tests de
    /// `scenario` ne tiennent pas sur lui.
    ///
    /// Les trois assertions voisines ont été retirées comme doublons, chacune
    /// contre un test strictement plus fort de `crate::scenario` :
    /// `les_dix_blocs_portent_leur_section_et_leur_page` refuse les champs vides
    /// des dix blocs — après `trim`, là où celles-ci ne testaient que la chaîne
    /// vide — et `les_dix_blocs_nomment_leur_edition` tient la clause d'édition
    /// pour les dix. Ce qui reste ici ne l'est pas : la vérification par le
    /// traité ramène la page à l'intervalle du §2.1, mesuré de la p. 23 à la
    /// p. 30, et n'exige donc pas la p. 26. « p. 22 » tombait hors de cet
    /// intervalle ; « p. 25 » y tomberait.
    #[test]
    fn le_bloc_d_cite_la_page_ou_la_these_se_lit() {
        assert!(BLOC_D.source.contains("p. 26"), "{}", BLOC_D.source);
    }
}
