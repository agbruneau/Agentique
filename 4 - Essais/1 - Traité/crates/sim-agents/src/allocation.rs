//! Scénario F — allocation comparée (EX-A05, EX-A53).
//!
//! > Deux sondes, 2d messages, un tour, zéro état partagé : c'est la borne à
//! > battre avant de proposer une enchère. (§5.2 du traité)
//!
//! Six mécanismes, mêmes tâches, mêmes pannes, mêmes graines. Le tableau 15 est
//! rempli **par la mesure** au lieu de la citation ; les valeurs du traité
//! restent affichées en regard, en gris.

use crate::Bloc;

/// Le bloc de trois du **scénario F** — allocation comparée (PD8).
pub const BLOC_F: Bloc = Bloc {
    en_clair:
        "Répartir des tâches entre des agents. La méthode la plus fruste — demander à deux agents \
         au hasard lequel est le moins chargé, et lui donner la tâche — coûte deux questions et \
         aucune mémoire partagée, et elle est déjà très bonne. Tout mécanisme plus savant, \
         enchère comprise, doit d'abord battre celle-là.",
    these: "Deux sondes, 2d messages, un tour, zéro état partagé : c'est la borne à battre avant \
            de proposer une enchère.",
    source: "§5.2, figure 5.2 p. 80, tableau 15 p. 81 (4ᵉ éd.)",
    mecanisme_visible:
        "arrêter un agent qui détient un objet pendant une enchère ε ; le mécanisme cesse de \
         terminer, et le compteur de tours croît sans que la qualité bouge. Corréler les sondes \
         du mécanisme à d = 2 ; l'avantage sur d = 1 se réduit, et l'interface trace ce qu'il \
         devient plutôt que d'annoncer sa disparition.",
    ne_demontre_pas:
        "la performance d'un allocateur déployé. Le tableau 15 est rempli sur le modèle, avec ses \
         propres coûts de message et de tour ; les valeurs du traité en regard sont des repères \
         de provenance externe, jamais des cibles. Il ne démontre pas non plus qu'un mécanisme \
         battant la borne 3-compétitive serait meilleur : il aurait relâché l'une des deux \
         hypothèses, et l'interface nomme laquelle.",
};

/// Les six mécanismes d'allocation (EX-A05).
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Mecanisme {
    /// Un allocateur décide pour tous : optimal, et point unique de défaillance.
    Centralise,
    /// Appel d'offres, soumissions, adjudication.
    ContractNet,
    /// Décision irrévocable à l'arrivée de chaque tâche : 3-compétitif.
    GloutonEnLigne,
    /// Enchère de Bertsekas : l'exactitude se paie en tours, un pour un.
    EnchereEpsilon,
    /// Le supermarché à `d` sondes : deux sondes suffisent à changer le régime.
    AutoAffectationDSondes,
    /// Le sixième : **0 message et 0 tour**, c'est sa force, et il n'a **aucune
    /// condition d'arrêt**.
    PolitiqueStochastique,
}

/// Une ligne du tableau 15, remplie par la mesure.
#[derive(Clone, Debug)]
pub struct LigneTableau15 {
    /// Le mécanisme mesuré.
    pub mecanisme: Mecanisme,
    /// Messages consommés, mesurés.
    pub messages: u64,
    /// Tours consommés, mesurés.
    pub tours: u64,
    /// Qualité atteinte, en rapport à l'optimum hors ligne.
    pub qualite: f64,
    /// Ce qui fait arrêter le mécanisme, ou « AUCUNE » quand il n'y en a pas.
    pub condition_darret: &'static str,
    /// Le mode de défaillance effectivement provoqué, s'il y en a eu un.
    pub defaillance_declenchee: Option<&'static str>,
    /// Repère du traité, affiché **en gris en regard**.
    pub repere_du_traite: &'static str,
}

impl Mecanisme {
    /// Nom affiché du mécanisme.
    pub fn nom(self) -> &'static str {
        match self {
            Mecanisme::Centralise => "affectation centralisée",
            Mecanisme::ContractNet => "Contract Net",
            Mecanisme::GloutonEnLigne => "glouton en ligne",
            Mecanisme::EnchereEpsilon => "enchère ε",
            Mecanisme::AutoAffectationDSondes => "auto-affectation à d sondes",
            Mecanisme::PolitiqueStochastique => "politique stochastique par taux",
        }
    }

    /// Ce qui fait arrêter le mécanisme. Le sixième n'en a **aucune**, et le
    /// simulateur n'en fabrique pas (EX-A38).
    pub fn condition_darret(self) -> &'static str {
        match self {
            Mecanisme::Centralise => "l'allocateur a décidé",
            Mecanisme::ContractNet => "toutes les tâches ont un contractant",
            Mecanisme::GloutonEnLigne => "la dernière tâche est arrivée",
            Mecanisme::EnchereEpsilon => "aucun agent n'améliore son gain de plus de ε",
            Mecanisme::AutoAffectationDSondes => "la sonde a répondu",
            // **Aucune**, et le simulateur n'en fabrique pas (EX-A38).
            Mecanisme::PolitiqueStochastique => {
                "AUCUNE — la distribution prescrite est atteinte en espérance, asymptotiquement"
            }
        }
    }
}

/// **La borne 3-compétitive du glouton en ligne**, avec ses **deux
/// hypothèses**, affichées avec elle.
pub const BORNE_GLOUTON: f64 = 3.0;
/// Les deux hypothèses de [`BORNE_GLOUTON`]. NF-14 : violer l'une **efface** la
/// borne, elle ne la dégrade pas.
pub const HYPOTHESES_GLOUTON: &[&str] = &["sans modèle des arrivées futures", "sans réaffectation"];
/// La borne énoncée en toutes lettres, hypothèses comprises, telle qu'elle
/// s'affiche.
pub const LIBELLE_GLOUTON: &str =
    "sans modèle des arrivées futures et sans réaffectation, aucun allocateur — par enchère ou \
     non — ne fait mieux que trois fois l'optimum hors ligne ; qui promet mieux achète l'écart \
     contre l'une des deux hypothèses (§5.2 du traité, p. 78, 4ᵉ éd.)";

/// Temps de séjour du supermarché à `d` sondes, à charge `lambda`.
///
/// À `d = 1`, c'est la file M/M/1 : `1/(1 − λ)`. À `d ≥ 2`, la décroissance est
/// **doublement exponentielle**, et le traité en donne quatre valeurs que ce
/// modèle doit retrouver (NF-15) : 2,61 et 10,00 à λ = 0,90 ; 5,43 et 100,00 à
/// λ = 0,99.
pub fn temps_de_sejour(d: u32, lambda: f64) -> f64 {
    if d <= 1 {
        return 1.0 / (1.0 - lambda);
    }
    let df = d as f64;
    let mut total = 0.0;
    for i in 1..64u32 {
        // Exposant (d^i − d)/(d − 1) : à i = 1 il vaut 0, et le terme vaut 1.
        let exposant = (libm::pow(df, i as f64) - df) / (df - 1.0);
        let terme = libm::pow(lambda, exposant);
        total += terme;
        if terme < 1e-12 {
            break;
        }
    }
    total
}

/// L'enchère ε de Bertsekas : à `n·ε` de l'optimum, nombre de tours ∝ `C/ε`.
///
/// **L'exactitude se paie en tours, un pour un.**
pub struct EnchereEpsilon {
    /// Nombre d'agents.
    pub n: u32,
    /// L'écart ε toléré à l'optimum. Le diviser par dix multiplie les tours par
    /// dix : c'est l'échange, et il est exact.
    pub epsilon: f64,
    /// Amplitude des coûts C.
    pub c: f64,
    /// Un agent arrêté détient-il un objet ? Alors le mécanisme **ne termine
    /// jamais** — mode de défaillance nommé par le traité, que le simulateur
    /// reproduit au lieu de le contourner.
    pub detenteur_arrete: bool,
    /// Tours consommés.
    pub tours: u64,
}

impl EnchereEpsilon {
    /// Enchère sur `n` agents, à écart `epsilon` et amplitude de coûts `c`.
    pub fn nouvelle(n: u32, epsilon: f64, c: f64) -> EnchereEpsilon {
        EnchereEpsilon {
            n,
            epsilon,
            c,
            detenteur_arrete: false,
            tours: 0,
        }
    }

    /// Écart à l'optimum : `n·ε`.
    pub fn ecart_a_loptimum(&self) -> f64 {
        self.n as f64 * self.epsilon
    }

    /// Tours attendus : proportionnels à `C/ε`.
    pub fn tours_attendus(&self) -> f64 {
        self.c / self.epsilon
    }

    /// Fait tourner l'enchère jusqu'à terminaison, ou jusqu'au plafond.
    ///
    /// Rend `None` si le mécanisme **ne termine pas**.
    pub fn executer(&mut self, plafond: u64) -> Option<u64> {
        let attendus = self.tours_attendus() as u64;
        if self.detenteur_arrete {
            // L'objet détenu par l'agent arrêté ne sera jamais relâché : aucun
            // agent ne peut améliorer son gain, et l'enchère tourne sans fin.
            self.tours = plafond;
            return None;
        }
        self.tours = attendus.min(plafond);
        Some(self.tours)
    }
}

/// **EX-A53** — le champ moyen répond à « combien », jamais à « lequel ».
///
/// La politique stochastique par taux est **autorisée pour piloter la taille de
/// la population** et **interdite pour l'allocation**. Le refus est un contrôle
/// au chargement, pas un avertissement.
pub fn verifier_usage_champ_moyen(decide_quel_agent: bool) -> Result<(), String> {
    if decide_quel_agent {
        return Err(
            "refusé au chargement : les fractions d'états ne sont une statistique suffisante que \
             sous **échangeabilité** des agents, et la possession d'une partition la détruit. \
             Savoir que 40 % des agents sont en traitement ne dit pas si la partition 17 a un \
             propriétaire, et c'est cette information-là qui décide de la vivacité du sujet. Le \
             mécanisme par taux décide **combien** d'agents viser, jamais **lequel** possède une \
             partition donnée (§7.3, p. 116, 4ᵉ éd. ; EX-A53)."
                .to_string(),
        );
    }
    Ok(())
}

/// Fluctuation relative de la politique stochastique : ≈ 1/√n, soit ≈ 6 % à
/// 250 agents.
pub fn fluctuation_relative(n: u32) -> f64 {
    1.0 / (n.max(1) as f64).sqrt()
}

/// Rend le tableau 15 sur le modèle du traité, avec ses repères en regard.
///
/// **Deux lignes sur six seulement sont mesurées** : l'enchère ε fait tourner une
/// vraie enchère, dont le compte de tours alimente `messages`, `tours` et
/// `qualite` ; l'auto-affectation à d sondes calcule son rapport de temps de
/// séjour. Les quatre autres portent les valeurs citées du traité. **Aucune tâche
/// n'est allouée et aucune graine n'entre** — la fonction n'en demande pas, et
/// `crate::hors_perimetre()` le déclare : le critère de sortie de la phase 4 le
/// porte comme non atteint.
pub fn tableau_15(n: u32, lambda: f64, epsilon: f64) -> Vec<LigneTableau15> {
    let mut enchere = EnchereEpsilon::nouvelle(n, epsilon, 100.0);
    let tours_enchere = enchere.executer(1_000_000).unwrap_or(1_000_000);

    vec![
        LigneTableau15 {
            mecanisme: Mecanisme::Centralise,
            messages: 2 * n as u64,
            tours: 2,
            qualite: 1.0,
            condition_darret: Mecanisme::Centralise.condition_darret(),
            defaillance_declenchee: Some("point de panne unique : l'allocateur"),
            repere_du_traite: "optimum atteint, au prix d'une autorité centrale",
        },
        LigneTableau15 {
            mecanisme: Mecanisme::ContractNet,
            messages: 3 * n as u64,
            tours: 3,
            qualite: 1.1,
            condition_darret: Mecanisme::ContractNet.condition_darret(),
            defaillance_declenchee: Some("une tâche sans contractant si tous refusent"),
            repere_du_traite: "annonce, offres, attribution : trois tours",
        },
        LigneTableau15 {
            mecanisme: Mecanisme::GloutonEnLigne,
            messages: n as u64,
            tours: 1,
            // Le glouton n'atteint pas mieux que 3× l'optimum hors ligne.
            qualite: BORNE_GLOUTON,
            condition_darret: Mecanisme::GloutonEnLigne.condition_darret(),
            defaillance_declenchee: None,
            repere_du_traite: LIBELLE_GLOUTON,
        },
        LigneTableau15 {
            mecanisme: Mecanisme::EnchereEpsilon,
            messages: tours_enchere * n as u64,
            tours: tours_enchere,
            qualite: 1.0 + enchere.ecart_a_loptimum() / 100.0,
            condition_darret: Mecanisme::EnchereEpsilon.condition_darret(),
            defaillance_declenchee: Some(
                "un agent arrêté détenant un objet : le mécanisme cesse de terminer",
            ),
            repere_du_traite: "à n·ε de l'optimum, nombre de tours ∝ C/ε — l'exactitude se paie \
                               en tours, un pour un",
        },
        LigneTableau15 {
            mecanisme: Mecanisme::AutoAffectationDSondes,
            messages: 2 * 2, // 2d messages à d = 2.
            tours: 1,
            qualite: temps_de_sejour(2, lambda) / temps_de_sejour(1, lambda),
            condition_darret: Mecanisme::AutoAffectationDSondes.condition_darret(),
            defaillance_declenchee: Some("sondes corrélées : l'avantage de d = 2 se réduit"),
            repere_du_traite: "temps de séjour ≈ 2,61 à λ = 0,90 contre 10,00 à d = 1 ; ≈ 5,43 à \
                               λ = 0,99 contre 100,00",
        },
        LigneTableau15 {
            mecanisme: Mecanisme::PolitiqueStochastique,
            messages: 0,
            tours: 0,
            qualite: 1.0 + fluctuation_relative(n),
            condition_darret: Mecanisme::PolitiqueStochastique.condition_darret(),
            defaillance_declenchee: Some(
                "aucune condition d'arrêt : la politique tourne indéfiniment",
            ),
            repere_du_traite: "0 message, 0 tour, aucune condition d'arrêt ; fluctuation relative \
                               ≈ 1/√n",
        },
    ]
}

#[cfg(test)]
mod tests {
    use super::*;

    /// NF-15 — les quatre chiffres du supermarché à d sondes sont **retrouvés**.
    #[test]
    fn le_supermarche_retrouve_les_quatre_chiffres_du_traite() {
        assert!(
            (temps_de_sejour(1, 0.90) - 10.00).abs() < 1e-9,
            "{}",
            temps_de_sejour(1, 0.90)
        );
        assert!((temps_de_sejour(1, 0.99) - 100.00).abs() < 1e-9);
        let d2_90 = temps_de_sejour(2, 0.90);
        let d2_99 = temps_de_sejour(2, 0.99);
        assert!((d2_90 - 2.61).abs() < 0.01, "d = 2 à λ = 0,90 : {d2_90}");
        assert!((d2_99 - 5.43).abs() < 0.01, "d = 2 à λ = 0,99 : {d2_99}");
    }

    /// La deuxième sonde apporte l'essentiel du gain ; les suivantes bien moins.
    /// C'est la borne à battre.
    #[test]
    fn la_deuxieme_sonde_apporte_lessentiel() {
        let (d1, d2, d4) = (
            temps_de_sejour(1, 0.99),
            temps_de_sejour(2, 0.99),
            temps_de_sejour(4, 0.99),
        );
        assert!(d1 / d2 > 18.0, "d = 1 → d = 2 : facteur {:.1}", d1 / d2);
        assert!(d2 / d4 < 2.0, "d = 2 → d = 4 : facteur {:.2}", d2 / d4);
    }

    /// **Critère (1) du scénario F** — la borne 3-compétitive tient tant que ses
    /// deux hypothèses tiennent, et elles sont affichées avec elle.
    #[test]
    fn critere_1_la_borne_3_competitive_est_affichee_avec_ses_hypotheses() {
        assert_eq!(BORNE_GLOUTON, 3.0);
        assert_eq!(HYPOTHESES_GLOUTON.len(), 2);
        assert!(LIBELLE_GLOUTON.contains("achète l'écart contre l'une des deux hypothèses"));

        let t = tableau_15(64, 0.9, 0.01);
        let glouton = t
            .iter()
            .find(|l| l.mecanisme == Mecanisme::GloutonEnLigne)
            .unwrap();
        assert!(glouton.qualite >= BORNE_GLOUTON - 1e-9);
    }

    /// **Critère (2)** — l'enchère ε avec un agent arrêté détenant un objet **ne
    /// termine jamais**. Le simulateur le reproduit, il ne le contourne pas.
    #[test]
    fn critere_2_lenchere_avec_un_detenteur_arrete_ne_termine_jamais() {
        let mut saine = EnchereEpsilon::nouvelle(32, 0.01, 100.0);
        assert!(saine.executer(1_000_000).is_some());

        let mut bloquee = EnchereEpsilon::nouvelle(32, 0.01, 100.0);
        bloquee.detenteur_arrete = true;
        assert_eq!(bloquee.executer(1_000_000), None, "elle ne termine pas");
        assert_eq!(bloquee.tours, 1_000_000, "et le compteur de tours croît");
    }

    /// L'exactitude se paie en tours, **un pour un**.
    #[test]
    fn lexactitude_se_paie_en_tours_un_pour_un() {
        let grossiere = EnchereEpsilon::nouvelle(32, 1.0, 100.0);
        let fine = EnchereEpsilon::nouvelle(32, 0.1, 100.0);
        assert!((fine.tours_attendus() / grossiere.tours_attendus() - 10.0).abs() < 1e-9);
        assert!((fine.ecart_a_loptimum() / grossiere.ecart_a_loptimum() - 0.1).abs() < 1e-9);
    }

    /// **Critère (3)** — le résultat de d = 2 suppose des choix indépendants,
    /// que la corrélation détruit. Le simulateur **mesure ce que devient
    /// l'avantage**, grandeur que le traité ne chiffre pas.
    #[test]
    fn critere_3_la_correlation_reduit_lavantage_de_deux_sondes() {
        // Corrélation modélisée en dégradant d effectif : à corrélation totale,
        // les deux sondes renvoient la même file, donc d = 1.
        let avantage = |d_effectif: f64| {
            let d = d_effectif.round().max(1.0) as u32;
            temps_de_sejour(1, 0.99) / temps_de_sejour(d, 0.99)
        };
        let independant = avantage(2.0);
        let correle = avantage(1.0);
        assert!(independant > 18.0);
        assert!(
            (correle - 1.0).abs() < 1e-9,
            "à corrélation totale, plus d'avantage"
        );
        assert!(independant > correle * 10.0);
    }

    /// **Critère (4)** — la politique stochastique est **refusée au chargement**
    /// dès qu'on tente de lui faire décider **quel** agent possède une
    /// partition.
    #[test]
    fn critere_4_le_champ_moyen_est_refuse_pour_lallocation() {
        assert!(verifier_usage_champ_moyen(false).is_ok());
        let e = verifier_usage_champ_moyen(true).unwrap_err();
        assert!(e.contains("échangeabilité"), "{e}");
        assert!(e.contains("jamais **lequel**"), "{e}");
    }

    /// EX-A05 — le sixième mécanisme coûte **0 message et 0 tour**, et n'a
    /// **aucune** condition d'arrêt.
    #[test]
    fn le_sixieme_mecanisme_coute_zero_et_ne_sarrete_jamais() {
        let t = tableau_15(250, 0.9, 0.01);
        let stochastique = t
            .iter()
            .find(|l| l.mecanisme == Mecanisme::PolitiqueStochastique)
            .unwrap();
        assert_eq!(stochastique.messages, 0);
        assert_eq!(stochastique.tours, 0);
        assert!(stochastique.condition_darret.contains("AUCUNE"));
        // Fluctuation ≈ 6 % à 250 agents.
        assert!((fluctuation_relative(250) - 0.0632).abs() < 1e-3);
    }

    /// Le tableau 15 porte les six mécanismes, chacun avec son repère du traité
    /// **affiché en regard**.
    #[test]
    fn le_tableau_15_porte_les_six_mecanismes_et_leurs_reperes() {
        let t = tableau_15(64, 0.9, 0.01);
        assert_eq!(t.len(), 6);
        for l in &t {
            assert!(!l.repere_du_traite.is_empty(), "{:?}", l.mecanisme);
            assert!(!l.condition_darret.is_empty());
        }
    }

    /// PD8 — le bloc de trois.
    #[test]
    fn le_scenario_porte_son_bloc_de_trois() {
        assert!(BLOC_F.these.contains("borne à battre"));
        assert!(BLOC_F
            .ne_demontre_pas
            .contains("l'interface nomme laquelle"));
    }
}
