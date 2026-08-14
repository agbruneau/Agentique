//! Critère de sortie de la phase 2, tel qu'écrit au §9 du PRD.
//!
//! > Le scénario C retrouve des σ et κ injectés par construction, à l'intérieur
//! > de son intervalle de confiance. R1 tombe exactement à t₄, jamais avant. Le
//! > préréglage `min.insync.replicas = 1` fait tomber la tolérance de f à 0
//! > **sans qu'aucune erreur ne soit émise**, et l'interface le nomme. Un lien
//! > partagé reproduit la figure exactement chez le destinataire. Le préréglage
//! > « oscillation » diverge avec un compteur de pannes strictement nul.
//!
//! Les cinq points sont ici, chacun dans un test qui échoue si le point tombe.

use sim_agents::elasticite::{Controleur, Params as ParamsElasticite};
use sim_agents::partage::Lien;
use sim_agents::scenario_d::{Choix, Etape, ScenarioD};
use sim_agents::stigmergie::Params;
use sim_agents::usl::{ajuster_avec_ic, Charge};
use sim_agents::scenario_b;
use sim_core::alea::Alea;

/// **(1)** Le scénario C retrouve σ et κ injectés, dans son intervalle de
/// confiance. C'est la validation croisée qui autorise à faire confiance à
/// l'estimation là où la vérité n'est pas connue.
#[test]
fn critere_1_le_scenario_c_retrouve_les_parametres_injectes() {
    // Trois jeux de paramètres : la validation ne doit pas tenir par accident
    // sur un seul point de l'espace.
    for (sigma, kappa) in [(0.02, 0.0001), (0.005, 0.00002), (0.1, 0.0005)] {
        let charge = Charge::nouvelle(sigma, kappa, 4_096);
        let mut alea = Alea::nouveau(1);
        let points = charge.campagne(2, 512, 16, 30, &mut alea);
        let a = ajuster_avec_ic(&points, 400, &mut alea).unwrap();
        assert!(
            a.ic_sigma.contient(sigma),
            "σ = {sigma} hors de [{:.6}, {:.6}]",
            a.ic_sigma.bas,
            a.ic_sigma.haut
        );
        assert!(
            a.ic_kappa.contient(kappa),
            "κ = {kappa} hors de [{:.8}, {:.8}]",
            a.ic_kappa.bas,
            a.ic_kappa.haut
        );
    }
}

/// **(2)** R1 tombe **exactement** au choix d'élire hors ISR, et jamais avant.
/// Le compteur de pannes affiche 2 à cet instant : k ≥ f + 1 est respecté à
/// l'égalité, et l'enregistrement est perdu quand même.
#[test]
fn critere_2_r1_tombe_exactement_a_t4_et_jamais_avant() {
    let mut d = ScenarioD::defaut();
    while d.etape != Etape::T4 {
        d.pas();
        assert!(d.violation_r1().is_none(), "R1 violée avant t₄");
    }
    assert_eq!(d.isr.pannes, 2);
    d.choisir(Choix::ElireHorsIsr);
    assert!(d.violation_r1().is_some(), "R1 doit tomber à l'élection hors ISR");

    // Et jamais si l'on attend : le prix payé est l'indisponibilité.
    let mut attente = ScenarioD::defaut();
    attente.derouler(Choix::AttendreUnMembre);
    assert!(attente.violation_r1().is_none());
}

/// **(3)** `min.insync.replicas = 1` fait tomber la tolérance à 0 **sans
/// qu'aucune erreur ne soit émise**, et l'interface le nomme.
#[test]
fn critere_3_lisr_muet_ne_leve_aucune_erreur_et_linterface_le_nomme() {
    let mut d = ScenarioD::isr_muet();
    for _ in 0..4 {
        d.pas();
    }
    // Le producteur écrit encore, et reçoit son accusé.
    let decalage = d.isr.ecrire().expect("avec m = 1, la partition accuse encore");
    for id in d.isr.isr().to_vec() {
        d.isr.repliquer(id, decalage + 1, sim_core::temps::Instant(99));
    }
    assert_eq!(d.isr.derniere_largeur(), Some(1));
    assert_eq!(d.isr.tolerances().0, Some(0), "tolérance tombée à 0");

    let avis = d.isr.perte_muette().expect("l'interface doit le nommer");
    assert!(avis.contains("aucune erreur n'est émise"), "{avis}");

    // L'affichage EX-V15 montre les trois grandeurs sans jamais les additionner.
    let v15 = d.isr.affichage_v15();
    assert!(v15.iter().any(|(k, _)| *k == "|ISR| courant"));
    assert!(v15.iter().any(|(k, _)| *k == "largeur d'accusé du dernier validé"));
    assert!(v15.iter().any(|(k, v)| *k == "marge d'accusé |ISR| − m"
        && v.contains("grandeur dérivée du produit")));
}

/// **(4)** Un lien partagé reproduit la figure **exactement** chez le
/// destinataire — trace, effort et série temporelle comprises.
#[test]
fn critere_4_un_lien_partage_reproduit_la_figure() {
    for graine in [1u64, 7, 99] {
        let emetteur = Lien {
            version: sim_core::VERSION.to_string(),
            scenario: "B".to_string(),
            graine,
            budget: 20_000,
            params: Params {
                n: 16,
                ..Params::scenario_b()
            },
        };
        let recu = Lien::decoder(&emetteur.encoder(), sim_core::VERSION).unwrap();
        let a = scenario_b(emetteur.params.clone(), emetteur.graine, emetteur.budget).unwrap();
        let b = scenario_b(recu.params.clone(), recu.graine, recu.budget).unwrap();
        assert_eq!(a.trace, b.trace, "graine {graine}");
        assert_eq!(a.mesures.effort_par_tranche, b.mesures.effort_par_tranche);
        assert_eq!(a.phi_moyen, b.phi_moyen);
    }
}

/// **(5)** Le préréglage « oscillation » diverge avec un **compteur de pannes
/// strictement nul**. Rien n'est tombé, et le système est inutilisable : c'est
/// ce qui le rend pédagogique.
#[test]
fn critere_5_loscillation_diverge_sans_aucune_panne() {
    let mut c = Controleur::nouveau(ParamsElasticite::oscillation());
    for _ in 0..200 {
        c.periode(80.0, 10.0);
    }
    assert_eq!(c.pannes, 0, "compteur de pannes strictement nul");
    assert!(c.amplitude_totale() >= 8, "amplitude {}", c.amplitude_totale());
    assert!(c.inversions >= 4, "{} inversions", c.inversions);
    assert!(
        !c.affichage_point_fixe().contains("stabilis"),
        "l'interface n'affiche jamais « stabilisé »"
    );
}
