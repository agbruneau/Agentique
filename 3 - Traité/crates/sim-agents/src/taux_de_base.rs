//! Scénario L — le taux de base (EX-A31, EX-A32, EX-A34, EX-A35, DT8).
//!
//! > Une sonde presque parfaite produit des alarmes presque toutes fausses.
//! > (§7.2)
//!
//! **P(I) n'est jamais saisi directement** : il est dérivé des trois grandeurs
//! qui le produisent, pour que l'utilisateur voie d'où vient 2 × 10⁻⁵.

use crate::Bloc;
use sim_core::horloge::Domaines;

/// Le bloc de trois du **scénario L** — le taux de base (PD8).
pub const BLOC_L: Bloc = Bloc {
    en_clair:
        "Un détecteur qui se trompe une fois sur cent mille paraît excellent. Mais s'il surveille \
         un flux où les vrais incidents sont mille fois plus rares que ses erreurs, presque toutes \
         ses alarmes seront fausses. Ce n'est pas un défaut du détecteur : c'est l'effet de la \
         rareté de ce qu'il cherche, et aucune amélioration de sa précision ne l'annule.",
    these: "Une sonde presque parfaite produit des alarmes presque toutes fausses.",
    source: "§7.2, figure 7.2 p. 107, tableau 19 p. 110 (4ᵉ éd.)",
    mecanisme_visible:
        "glisser le curseur de structure des domaines de « disjoints » vers « domaine unique » \
         fait passer les détecteurs d'entrées indépendantes à des entrées corrélées ; le taux de \
         fausses alarmes conjoint P(A|¬I)ʳ remonte vers P(A|¬I) pendant que la détection \
         conjointe reste clouée à P(A|I)ʳ. P(I|A) s'effondre sans qu'aucun indicateur interne du \
         mécanisme ne bouge.",
    ne_demontre_pas:
        "que la corroboration améliore la détection. Elle **échange de la détection contre de la \
         précision**, et rien dans le mécanisme ne mesure où l'on se situe entre les deux \
         extrêmes — ce qui interdit au simulateur d'afficher un P(I|A) unique.",
};

/// Les trois grandeurs qui **produisent** P(I). Il n'est jamais saisi.
#[derive(Clone, Copy, Debug)]
pub struct TauxDeBase {
    /// Enregistrements d'audit par jour.
    pub enregistrements_par_jour: f64,
    /// Tentatives d'intrusion par jour.
    pub intrusions_par_jour: f64,
    /// Enregistrements affectés par intrusion.
    pub enregistrements_par_intrusion: f64,
}

impl Default for TauxDeBase {
    fn default() -> Self {
        TauxDeBase {
            enregistrements_par_jour: 1e6,
            intrusions_par_jour: 2.0,
            enregistrements_par_intrusion: 10.0,
        }
    }
}

impl TauxDeBase {
    /// P(I) — **dérivé**, jamais saisi. Aux défauts : 2 × 10 / 10⁶ = 2 × 10⁻⁵.
    pub fn p_i(&self) -> f64 {
        self.intrusions_par_jour * self.enregistrements_par_intrusion
            / self.enregistrements_par_jour
    }

    /// Affichage : la dérivation est montrée, pour que l'utilisateur voie d'où
    /// vient le chiffre.
    pub fn affichage(&self) -> String {
        format!(
            "P(I) = {} intrusions/jour × {} enregistrements/intrusion ÷ {} enregistrements/jour \
             = {:.1e} — **dérivé, jamais saisi**",
            self.intrusions_par_jour,
            self.enregistrements_par_intrusion,
            self.enregistrements_par_jour,
            self.p_i()
        )
    }
}

/// **EX-A31** — corroboration `r` parmi `n`.
///
/// Modèle repris entier : crash-arrêt et omission, partiellement synchrone avec
/// Δ inconnue, **aucune horloge synchronisée, aucun agent menteur**.
#[derive(Clone, Copy, Debug)]
pub struct Corroboration {
    /// Seuil : `r = 1` désactive la corroboration.
    pub r: u32,
    /// Taux de détection d'une sonde.
    pub p_a_sachant_i: f64,
    /// Taux de fausses alarmes d'une sonde.
    pub p_a_sachant_non_i: f64,
}

impl Default for Corroboration {
    fn default() -> Self {
        Corroboration {
            r: 3,
            p_a_sachant_i: 0.70,
            p_a_sachant_non_i: 1e-3,
        }
    }
}

/// Les deux régimes, **et jamais un seul chiffre**.
#[derive(Clone, Copy, Debug)]
pub struct DeuxRegimes {
    /// P(I|A) sous indépendance des fautes.
    pub sous_independance: f64,
    /// P(I|A) à corrélation parfaite.
    pub a_correlation_parfaite: f64,
}

impl Corroboration {
    /// Coût : **1 message et 0 tour** pour lever une alarme ; Θ(n) messages par
    /// fenêtre dans le pire cas pour corroborer, **0 tour**.
    pub fn cout_par_alarme(&self) -> (u64, u64) {
        (1, 0)
    }
    /// Coût par fenêtre : `n` messages, **0 tour**. La corroboration ne
    /// synchronise personne.
    pub fn cout_par_fenetre(&self, n: u32) -> (u64, u64) {
        (n as u64, 0)
    }

    /// Détection conjointe : `P(A|I)ʳ`. Elle **reste clouée là** quelle que soit
    /// la corrélation — c'est le point.
    pub fn detection_conjointe(&self) -> f64 {
        libm::pow(self.p_a_sachant_i, self.r as f64)
    }

    /// Taux de fausses alarmes conjoint, en fonction de la corrélation `rho`.
    ///
    /// Sous indépendance il vaut `P(A|¬I)ʳ` ; à corrélation parfaite il
    /// **redevient** `P(A|¬I)`. Entre les deux, l'interpolation est celle du
    /// modèle, et le mécanisme ne sait pas où il se situe.
    pub fn fausses_conjointes(&self, rho: f64) -> f64 {
        let independant = libm::pow(self.p_a_sachant_non_i, self.r as f64);
        let correle = self.p_a_sachant_non_i;
        independant + rho.clamp(0.0, 1.0) * (correle - independant)
    }

    /// P(I|A) par Bayes, à corrélation donnée.
    pub fn p_i_sachant_a(&self, base: &TauxDeBase, rho: f64) -> f64 {
        let p_i = base.p_i();
        let vrais = self.detection_conjointe() * p_i;
        let faux = self.fausses_conjointes(rho) * (1.0 - p_i);
        if vrais + faux <= 0.0 {
            return 0.0;
        }
        vrais / (vrais + faux)
    }

    /// **Les deux bornes, affichées ensemble et jamais une valeur unique**
    /// (EX-V14, EX-A31).
    pub fn deux_regimes(&self, base: &TauxDeBase) -> DeuxRegimes {
        DeuxRegimes {
            sous_independance: self.p_i_sachant_a(base, 0.0),
            a_correlation_parfaite: self.p_i_sachant_a(base, 1.0),
        }
    }

    /// Le libellé obligatoire.
    pub const LIBELLE: &'static str =
        "la corroboration n'améliore pas la détection, elle **échange de la détection contre de \
         la précision** — et rien dans le mécanisme ne mesure où l'on se situe entre les deux \
         extrêmes, ce qui interdit d'afficher un P(I|A) unique (§7.2)";

    /// Débit de fausses alarmes : `n · λ · P(A|¬I)`.
    pub fn fausses_alarmes_par_s(&self, n: u32, lambda: f64) -> f64 {
        n as f64 * lambda * self.p_a_sachant_non_i
    }
}

/// **DT8** — le point d'injection « agent menteur », **désactivé par défaut**.
///
/// Dès qu'il est activé, l'interface affiche la borne `3f + 1` et la phrase de
/// la figure 5.1.
#[derive(Clone, Copy, Debug, Default)]
pub struct AgentMenteur {
    /// Faux par défaut, et activable dans les scénarios I et L seulement.
    pub actif: bool,
    /// Nombre de menteurs `f`. Nommé `f` et non `m` : le glossaire réserve `m`
    /// au minimum de répliques synchronisées d'ISR(k, m), et les deux graphies
    /// coexistaient dans le dépôt sans que rien ne tranche.
    pub f: u32,
}

impl AgentMenteur {
    /// Participants minimaux pour tolérer `f` déviants : **3f + 1**.
    ///
    /// `f`, et non `m` : le glossaire du PRD réserve `m` au minimum de répliques
    /// synchronisées d'ISR(k, m), et les deux graphies coexistaient dans le
    /// dépôt sans que rien ne tranche.
    pub fn participants_minimaux(&self) -> u32 {
        3 * self.f + 1
    }

    /// Affichage imposé dès l'activation.
    pub fn affichage(&self, participants: u32) -> Option<String> {
        if !self.actif {
            return None;
        }
        Some(format!(
            "agent menteur actif ({} menteur(s)) : la borne est **3f + 1**, donc **aucune \
             solution à moins de {} participants ne tolère {} déviants**, et ce modèle tue les \
             trois premières lignes de la figure 5.1 (p. 73, 4ᵉ éd.). Participants présents : \
             {}. Tout verdict rendu sur ces mécanismes est **conditionnel au modèle P**. La \
             cryptographie ne relâche pas la borne, elle la change.",
            self.f,
            self.participants_minimaux(),
            self.f,
            participants
        ))
    }

    /// À trois participants, **aucune solution ne résiste à un seul traître**.
    pub fn resiste(&self, participants: u32) -> bool {
        !self.actif || participants >= self.participants_minimaux()
    }
}

/// **EX-A34** — classification des prédicats : stable ou instable.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Predicat {
    /// Une fois vrai, il le reste.
    Stable,
    /// Il peut redevenir faux — aucun instantané ne l'établit.
    Instable,
}

/// Classe un prédicat d'après sa formulation. **Elle ne le vérifie pas** : le
/// classement est lexical — la présence de « présentement » ou « en cours » —,
/// et rien ici n'évalue le prédicat sur un état du monde.
pub fn classer(enonce: &str) -> Predicat {
    // « Le système est présentement attaqué » n'est PAS stable : la session se
    // termine et l'attaquant efface. « Un événement correspondant à la
    // signature S s'est produit dans l'intervalle [t₁, t₂] » EST stable dès
    // lors que le milieu est en ajout seul.
    if enonce.contains("présentement") || enonce.contains("en cours") {
        Predicat::Instable
    } else {
        Predicat::Stable
    }
}

/// Ce que le journal achète : il **transforme un prédicat instable en prédicat
/// stable**, pour Θ(1) message par observation et 0 tour.
pub const APPORT_DU_JOURNAL: &str =
    "le journal transforme un prédicat instable en prédicat stable, pour Θ(1) message par \
     observation et **0 tour** : c'est la raison technique pour laquelle la détection distribuée \
     s'adosse au journal plutôt qu'à un état partagé. Le prix est la rétention, bornée par R \
     (§7.2, EX-M20)";

/// **EX-A35** — échantillonnage de traces.
#[derive(Clone, Copy, Debug)]
pub struct Echantillonnage {
    /// Taux, par exemple 1/1024.
    pub taux: f64,
    /// Cohérent par trace plutôt que par enregistrement : rompt l'hypothèse
    /// d'indépendance des tirages au sein d'une intrusion.
    pub coherent_par_trace: bool,
}

impl Echantillonnage {
    /// Probabilité d'échantillonner **au moins une fois** une intrusion qui se
    /// manifeste dans `k` enregistrements.
    ///
    /// Sous tirage indépendant : `1 − (1 − p)^k`. À p = 1/1024 et k = 10, cela
    /// donne ≈ **0,97 %** (NF-15).
    pub fn probabilite_de_voir(&self, k: u32) -> f64 {
        if self.coherent_par_trace {
            // La trace entière est prise ou laissée : la probabilité remonte au
            // taux lui-même, et **c'est alors la couverture des traces, non
            // celle des enregistrements, qui borne la détection**.
            self.taux
        } else {
            1.0 - libm::pow(1.0 - self.taux, k as f64)
        }
    }

    /// Le commutateur change **le libellé de la grandeur affichée**, pas
    /// seulement sa valeur.
    pub fn libelle_grandeur(&self) -> &'static str {
        if self.coherent_par_trace {
            "couverture des **traces** — c'est elle qui borne la détection"
        } else {
            "couverture des **enregistrements**, sous hypothèse d'indépendance des tirages"
        }
    }
}

/// **EX-A32** — AGRÉGER-ÉPIDÉMIQUE : facteurs de convergence et cycles.
pub mod agreger_epidemique {
    /// Provenance des trois facteurs de convergence ci-dessous, portée ici
    /// plutôt que répétée sur chacun (F2).
    pub const SOURCE: &str = "§7.2 — facteurs de réduction de variance par cycle d'agrégation";

    /// Couplage parfait — **témoin non implantable** : exige une connaissance
    /// globale.
    pub const COUPLAGE_PARFAIT: f64 = 0.25;
    /// Tirage uniforme, implanté.
    pub const TIRAGE_UNIFORME: f64 = 0.367_879_441_171_442_33; // e⁻¹
    /// Tirage distribué du protocole — **le défaut**.
    pub const TIRAGE_DISTRIBUE: f64 = 0.303;

    /// Cycles nécessaires pour réduire la variance d'un facteur `cible`.
    ///
    /// À 10⁻⁶ et facteur 0,303 : `ln(10⁻⁶)/ln(0,303) ≈ 11,6`, soit **12 cycles,
    /// quelle que soit la taille de l'essaim** (NF-15).
    pub fn cycles_pour(cible: f64, facteur: f64) -> u32 {
        (libm::log(cible) / libm::log(facteur)).ceil() as u32
    }

    /// Une époque coûte **24n messages et 12 tours** à δ = 1 s.
    pub fn cout_epoque(n: u32) -> (u64, u64) {
        (24 * n as u64, 12)
    }

    /// La variance reste bornée **si et seulement si** le facteur de
    /// convergence est inférieur à `1 − π`, soit π < ≈ 69,7 % à 0,303.
    pub fn variance_bornee(pi: f64, facteur: f64) -> bool {
        facteur < 1.0 - pi
    }

    /// Seuil d'emballement pour un facteur donné.
    pub fn seuil_demballement(facteur: f64) -> f64 {
        1.0 - facteur
    }

    /// Contrôle à la construction : un agrégat épidémique **ne peut pas
    /// alimenter une décision de sécurité**.
    pub fn verifier_branchement(vers_confinement: bool) -> Result<(), String> {
        if vers_confinement {
            return Err(
                "branchement refusé : l'agrégation épidémique est **admissible pour estimer une \
                 charge, inadmissible pour établir un fait de sécurité** (§7.2). Le branchement \
                 sur le rééquilibrage de charge est exactement l'usage prévu."
                    .to_string(),
            );
        }
        Ok(())
    }
}

/// Le scénario L : P(I|A) en fonction du curseur de structure des domaines.
pub fn scenario_l(
    base: &TauxDeBase,
    corroboration: &Corroboration,
    n: u32,
    part_domaine_commun: f64,
) -> (f64, f64) {
    let domaines = Domaines::interpole(n, part_domaine_commun, 0.0);
    let rho = domaines.rho();
    (rho, corroboration.p_i_sachant_a(base, rho))
}

#[cfg(test)]
mod tests {
    use super::*;

    /// **P(I) est dérivé** des trois grandeurs, et vaut 2 × 10⁻⁵ aux défauts.
    #[test]
    fn p_i_est_derive_et_vaut_deux_dix_moins_cinq() {
        let b = TauxDeBase::default();
        assert!((b.p_i() - 2e-5).abs() < 1e-12, "{}", b.p_i());
        assert!(b.affichage().contains("dérivé, jamais saisi"));
    }

    /// NF-15 — la détection conjointe à r = 3 vaut **0,343**.
    #[test]
    fn la_detection_conjointe_vaut_0343() {
        let c = Corroboration::default();
        assert!((c.detection_conjointe() - 0.343).abs() < 1e-9, "{}", c.detection_conjointe());
    }

    /// **EX-A31** — les deux régimes, et **jamais un seul chiffre**. Sous
    /// indépendance P(I|A) ≈ 99,99 % ; à corrélation parfaite, il s'effondre.
    #[test]
    fn les_deux_regimes_sont_affiches_ensemble() {
        let b = TauxDeBase::default();
        let c = Corroboration::default();
        let d = c.deux_regimes(&b);
        assert!(
            d.sous_independance > 0.999,
            "sous indépendance : {:.6}",
            d.sous_independance
        );
        assert!(
            d.a_correlation_parfaite < 0.02,
            "à corrélation parfaite : {:.6}",
            d.a_correlation_parfaite
        );
        assert!(Corroboration::LIBELLE.contains("échange de la détection contre de la précision"));
    }

    /// **Le curseur du scénario L** — glisser la structure des domaines de
    /// « disjoints » vers « unique » fait s'effondrer P(I|A) **sans qu'aucun
    /// indicateur interne du mécanisme ne bouge**.
    #[test]
    fn le_curseur_de_structure_effondre_p_i_sachant_a() {
        let b = TauxDeBase::default();
        let c = Corroboration::default();

        let (rho_disjoint, p_disjoint) = scenario_l(&b, &c, 64, 0.0);
        let (rho_unique, p_unique) = scenario_l(&b, &c, 64, 1.0);

        assert!((rho_disjoint - 0.0).abs() < 1e-9);
        assert!((rho_unique - 1.0).abs() < 1e-9);
        assert!(p_disjoint > 0.999, "≈ 99,99 % : {p_disjoint:.6}");
        assert!(p_unique < 0.02, "moins de 2 % : {p_unique:.6}");

        // **Aucun indicateur interne ne bouge** : la détection conjointe reste
        // clouée à 0,343 des deux côtés.
        assert!((c.detection_conjointe() - 0.343).abs() < 1e-9);

        // Et le glissement est monotone.
        let mut precedent = 1.0;
        for k in 0..=10 {
            let (_, p) = scenario_l(&b, &c, 64, k as f64 / 10.0);
            assert!(p <= precedent + 1e-9, "P(I|A) doit décroître : {precedent} puis {p}");
            precedent = p;
        }
    }

    /// **EX-A31** — le coût : 1 message et 0 tour par alarme, Θ(n) messages et
    /// **0 tour** par fenêtre.
    #[test]
    fn les_couts_de_la_corroboration_sont_ceux_du_traite() {
        let c = Corroboration::default();
        assert_eq!(c.cout_par_alarme(), (1, 0));
        assert_eq!(c.cout_par_fenetre(128), (128, 0));
        // Débit de fausses alarmes : n · λ · P(A|¬I).
        assert!((c.fausses_alarmes_par_s(64, 12.0) - 0.768).abs() < 1e-9);
    }

    /// **DT8** — l'agent menteur est désactivé par défaut ; son activation
    /// affiche la borne 3f + 1.
    #[test]
    fn dt8_lagent_menteur_affiche_la_borne_3f_plus_1() {
        let inactif = AgentMenteur::default();
        assert!(!inactif.actif);
        assert!(inactif.affichage(64).is_none());

        let actif = AgentMenteur { actif: true, f: 1 };
        assert_eq!(actif.participants_minimaux(), 4);
        let a = actif.affichage(3).unwrap();
        // Une seule graphie fait foi. Accepter les deux, comme le faisait
        // cette assertion, laissait vivre `3m + 1` — où `m` désigne déjà le
        // minimum de répliques synchronisées d'ISR(k, m).
        assert!(a.contains("3f + 1"), "{a}");
        assert!(a.contains("conditionnel au modèle P"), "{a}");
        assert!(a.contains("La cryptographie ne relâche pas la borne"), "{a}");
        // À trois participants, aucune solution ne résiste à un seul traître.
        assert!(!actif.resiste(3));
        assert!(actif.resiste(4));
    }

    /// **EX-A34** — « présentement attaqué » n'est pas stable ; « un événement
    /// s'est produit dans [t₁, t₂] » l'est.
    #[test]
    fn ex_a34_classe_les_predicats() {
        assert_eq!(classer("le système est présentement attaqué"), Predicat::Instable);
        assert_eq!(
            classer("un événement de signature S s'est produit dans [t1, t2]"),
            Predicat::Stable
        );
        assert!(APPORT_DU_JOURNAL.contains("0 tour"));
        assert!(APPORT_DU_JOURNAL.contains("bornée par R"));
    }

    /// **EX-A35, NF-15** — à 1/1024 et 10 enregistrements, la probabilité de
    /// voir l'intrusion vaut ≈ **0,97 %**.
    #[test]
    fn ex_a35_retrouve_les_097_pourcent() {
        let e = Echantillonnage {
            taux: 1.0 / 1024.0,
            coherent_par_trace: false,
        };
        let p = e.probabilite_de_voir(10);
        assert!((p - 0.00973).abs() < 1e-4, "{p}");
        assert!(e.libelle_grandeur().contains("enregistrements"));
    }

    /// … et le commutateur cohérent par trace **change le libellé de la
    /// grandeur**, pas seulement sa valeur.
    #[test]
    fn ex_a35_le_commutateur_change_le_libelle() {
        let par_trace = Echantillonnage {
            taux: 1.0 / 1024.0,
            coherent_par_trace: true,
        };
        assert!(par_trace.libelle_grandeur().contains("traces"));
        assert!(par_trace.libelle_grandeur().contains("borne la détection"));
    }

    /// **EX-A32, NF-15** — réduire la variance d'un facteur 10⁻⁶ demande
    /// **12 cycles**, quelle que soit la taille de l'essaim.
    #[test]
    fn ex_a32_retrouve_les_douze_cycles() {
        use agreger_epidemique::*;
        assert_eq!(cycles_pour(1e-6, TIRAGE_DISTRIBUE), 12);
        assert_eq!(cout_epoque(100), (2_400, 12));
        assert!((COUPLAGE_PARFAIT - 0.25).abs() < 1e-12);
        assert!((TIRAGE_UNIFORME - 0.3679).abs() < 1e-4);
    }

    /// **EX-A32** — la variance reste bornée **si et seulement si** le facteur
    /// est inférieur à 1 − π, soit π < ≈ 69,7 % à 0,303.
    #[test]
    fn ex_a32_le_seuil_demballement_vaut_697_pourcent() {
        use agreger_epidemique::*;
        let seuil = seuil_demballement(TIRAGE_DISTRIBUE);
        assert!((seuil - 0.697).abs() < 1e-3, "{seuil}");
        assert!(variance_bornee(0.60, TIRAGE_DISTRIBUE));
        assert!(!variance_bornee(0.75, TIRAGE_DISTRIBUE));
    }

    /// **EX-A32** — un agrégat épidémique **ne peut pas** alimenter une décision
    /// de sécurité, et le chargement est refusé.
    #[test]
    fn ex_a32_refuse_le_branchement_sur_le_confinement() {
        use agreger_epidemique::*;
        assert!(verifier_branchement(false).is_ok());
        let e = verifier_branchement(true).unwrap_err();
        assert!(e.contains("inadmissible pour établir un fait de sécurité"), "{e}");
    }

    /// PD8 — le bloc de trois.
    #[test]
    fn le_scenario_porte_son_bloc_de_trois() {
        assert!(BLOC_L.these.contains("presque toutes fausses"));
        assert!(BLOC_L.ne_demontre_pas.contains("un P(I|A) unique"));
    }
}
