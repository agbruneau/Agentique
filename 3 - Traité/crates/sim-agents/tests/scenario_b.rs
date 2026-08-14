//! Critères d'acceptation du scénario B, tels qu'écrits au §7 du PRD.
//!
//! > (1) avec γ < 1 et écrêtage, l'essaim suit la bascule d'utilité ;
//! > (2) avec γ = 1, il reste verrouillé sur la ressource devenue mauvaise ;
//! > (3) la fraction d'effort mesurée hors dominante ne descend **jamais** sous
//! > la borne calculée (oracle EX-A11b) — un écart serait un défaut
//! > d'implantation ou une erreur du traité, et les deux méritent d'être
//! > trouvés.
//!
//! S'y ajoutent le critère de sortie de la phase 1 — rejeu à l'identique par
//! graine — et NF-10 : chaque mode de défaillance nommé a un test qui le
//! **provoque** et vérifie qu'il se produit.

use sim_agents::stigmergie::{MomentTrace, Params};
use sim_agents::scenario_b;

/// Budget de référence du scénario B.
///
/// Le désapprentissage a un temps caractéristique de τ/ln(1/γ) ≈ 9,5 s simulées
/// avec les défauts, et la fenêtre post-bascule doit en contenir plusieurs :
/// vérifié au diagnostic (`examples/diagnostic_b.rs`) avant de fixer la valeur.
///
/// Ce qui compte est le **temps simulé**, pas le nombre d'agents : le dépôt
/// étant calibré sur n, un essaim de 16 atteint le même régime qu'un essaim de
/// 64 au même instant simulé, pour quatre fois moins d'événements. Les tests
/// tournent donc à n = 16 — ce n'est pas un test au rabais, c'est le même temps
/// simulé pour un quart du coût.
const BUDGET: u64 = 150_000;

/// Population des tests. Voir [`BUDGET`].
const N_TEST: u32 = 16;

fn params() -> Params {
    Params {
        n: N_TEST,
        ..Params::scenario_b()
    }
}

fn params_verrouillage() -> Params {
    Params {
        n: N_TEST,
        // Le dépôt suit la population, comme en nominal : seul γ change.
        depot_unitaire: Some(params().depot()),
        ..Params::verrouillage()
    }
}

/// Critère (1) — avec γ < 1 et écrêtage, l'essaim **suit** la bascule.
#[test]
fn avec_oubli_lessaim_suit_la_bascule_dutilite() {
    let r = scenario_b(params(), 1, BUDGET).unwrap();
    assert!(r.bascule_faite, "la bascule n'a pas eu lieu dans le budget");
    assert!(
        r.suit_la_bascule(),
        "l'essaim n'a pas suivi : {:.1} % de l'effort final sur la moitié devenue la plus utile \
         (dernière tranche : {:?})",
        r.part_effort_finale_sur_la_moitie_haute() * 100.0,
        r.mesures.effort_par_tranche.last().unwrap()
    );

    // Il a bien **quitté** l'ancienne dominante, qui est devenue la pire.
    let finale = r.mesures.effort_par_tranche.last().unwrap();
    let total: u64 = finale.iter().sum();
    let part_ancienne = finale[0] as f64 / total as f64;
    assert!(
        part_ancienne < 0.1,
        "l'essaim sert encore l'ancienne dominante à {:.1} %",
        part_ancienne * 100.0
    );

    // Et il **campe** à distance de l'optimum : il ne s'y concentre pas. La
    // négation de la thèse serait aussi fausse que l'immobilité.
    assert!(
        r.part_effort_finale_sur_la_meilleure() < 0.95,
        "l'essaim a atteint l'optimum, ce que le traité dit qu'il ne fait pas"
    );
}

/// Critère (2) — avec γ = 1, l'essaim reste **verrouillé** sur la ressource
/// devenue mauvaise. EX-A11a : γ = 1 supprime l'oubli.
#[test]
fn sans_oubli_lessaim_reste_verrouille() {
    let r = scenario_b(params_verrouillage(), 1, BUDGET).unwrap();
    assert!(r.bascule_faite);
    assert!(
        !r.suit_la_bascule(),
        "γ = 1 devrait verrouiller, or {:.1} % de l'effort final est passé du bon côté",
        r.part_effort_finale_sur_la_moitie_haute() * 100.0
    );
    // Le verrouillage est un attachement au passé, pas une dispersion :
    // l'effort reste du côté des ressources devenues mauvaises.
    let servie = r.ressource_la_plus_servie_en_fin();
    assert!(
        servie < r.meilleure_ressource / 2,
        "l'essaim sert la ressource {servie} : ce n'est pas l'ancienne dominante"
    );

    // NF-14 — l'hypothèse violée **efface** la borne, elle ne la grise pas.
    let e = r.bornes.unwrap_err();
    assert!(e.contains("borne effacée"), "{e}");
    assert!(e.contains("NF-14"), "{e}");
}

/// Le contraste entre les deux régimes est la démonstration du scénario : la
/// même graine, le même budget, un seul réglage qui change.
/// Le contraste doit tenir **à toute graine**. Un critère d'acceptation qui ne
/// vaudrait que pour certains tirages ne serait pas un critère : c'est ce que
/// vérifie la répétition ci-dessous.
#[test]
fn le_contraste_entre_gamma_inferieur_a_un_et_gamma_egal_a_un_est_net() {
    for graine in 1..=8u64 {
        let avec = scenario_b(params(), graine, BUDGET).unwrap();
        let sans = scenario_b(params_verrouillage(), graine, BUDGET).unwrap();
        assert!(
            avec.suit_la_bascule(),
            "graine {graine} : avec oubli, l'essaim doit suivre (dernière tranche {:?})",
            avec.mesures.effort_par_tranche.last().unwrap()
        );
        assert!(
            !sans.suit_la_bascule(),
            "graine {graine} : sans oubli, l'essaim doit rester verrouillé (dernière tranche {:?})",
            sans.mesures.effort_par_tranche.last().unwrap()
        );
        assert!(
            avec.part_effort_finale_sur_la_moitie_haute()
                > sans.part_effort_finale_sur_la_moitie_haute() * 2.0,
            "graine {graine} : contraste insuffisant, {:.3} avec oubli contre {:.3} sans",
            avec.part_effort_finale_sur_la_moitie_haute(),
            sans.part_effort_finale_sur_la_moitie_haute()
        );
    }
}

/// Critère (3) — l'oracle EX-A11b ne se déclenche jamais en régime nominal.
/// Une violation signalerait soit un défaut d'implantation, soit une erreur du
/// traité.
#[test]
fn la_borne_dexploration_tient() {
    for graine in 1..=20u64 {
        let r = scenario_b(params(), graine, 20_000).unwrap();
        assert!(
            r.borne_tenue(),
            "graine {graine} : {:?}",
            r.violations
        );
        let b = r.bornes.as_ref().unwrap();
        assert!(
            r.mesures.plancher_observe >= b.plancher_tirage * (1.0 - 1e-12),
            "graine {graine} : plancher observé {:.9} sous la borne {:.9}",
            r.mesures.plancher_observe,
            b.plancher_tirage
        );
        assert!(
            r.mesures.hors_dominante_observee >= b.fraction_hors_dominante * (1.0 - 1e-12),
            "graine {graine} : fraction hors dominante {:.9} sous la borne {:.9}",
            r.mesures.hors_dominante_observee,
            b.fraction_hors_dominante
        );
    }
}

/// Critère de sortie de la phase 1 — le scénario B se rejoue à l'identique par
/// graine, entrelacement compris (NF-01, EX-C02).
#[test]
fn le_scenario_b_se_rejoue_a_lidentique() {
    for graine in [1u64, 42, 1_000] {
        let a = scenario_b(params(), graine, 20_000).unwrap();
        let b = scenario_b(params(), graine, 20_000).unwrap();
        assert_eq!(a.trace, b.trace, "graine {graine} : traces différentes");
        assert_eq!(a.mesures.effort, b.mesures.effort);
        assert_eq!(a.mesures.cycles, b.mesures.cycles);
    }
}

/// Deux graines distinctes ne doivent pas produire la même trace — sans quoi le
/// test précédent ne prouverait rien.
#[test]
fn deux_graines_distinctes_produisent_des_traces_distinctes() {
    let a = scenario_b(params(), 1, 20_000).unwrap();
    let b = scenario_b(params(), 2, 20_000).unwrap();
    assert_ne!(a.trace, b.trace);
}

/// NF-10 — mode « essaim aveugle » : T < ℓ₉₉. L'agent redécide avant que sa
/// trace précédente soit durable ; la rétroaction disparaît.
#[test]
fn nf10_essaim_aveugle() {
    let aveugle = scenario_b(Params { n: N_TEST, ..Params::essaim_aveugle() }, 3, 20_000).unwrap();
    let nominal = scenario_b(params(), 3, 20_000).unwrap();
    let part_aveugle =
        aveugle.mesures.cycles_sans_retroaction as f64 / aveugle.mesures.cycles.max(1) as f64;
    let part_nominal =
        nominal.mesures.cycles_sans_retroaction as f64 / nominal.mesures.cycles.max(1) as f64;
    assert!(
        part_aveugle > 0.9,
        "T < ℓ₉₉ devrait rendre presque tous les cycles aveugles, or {:.2}",
        part_aveugle
    );
    assert!(
        part_nominal < 0.5,
        "en nominal T > ℓ₉₉, la rétroaction doit revenir : {:.2}",
        part_nominal
    );
}

/// NF-10 — mode « rejeu » : crash entre l'action et la validation de décalage.
/// φ reste inchangé — le dépôt est idempotent par M1 + M4 — mais l'effet de
/// l'action est **dupliqué** si l'action ne l'est pas. Le produit exhibe le
/// cinquième reste de la conclusion ; il ne le supprime pas.
#[test]
fn nf10_rejeu_produit_des_effets_dupliques() {
    let r = scenario_b(Params { n: N_TEST, ..Params::rejeu() }, 4, 20_000).unwrap();
    assert!(
        r.mesures.effets_dupliques > 0,
        "le mode rejeu n'a produit aucun effet dupliqué"
    );
    // Et l'oracle du plancher tient malgré tout : le rejeu n'altère pas φ.
    assert!(r.borne_tenue(), "{:?}", r.violations);

    // Sans le mode, aucun effet dupliqué.
    let nominal = scenario_b(params(), 4, 20_000).unwrap();
    assert_eq!(nominal.mesures.effets_dupliques, 0);
}

/// NF-10 — mode « incomparabilité M2 » : les ressources comparées sont placées
/// sur deux partitions. En deçà du seuil de fiabilité, l'ordre relatif de φ est
/// **sans objet**, et le simulateur le compte au lieu de le masquer.
#[test]
fn nf10_incomparabilite_m2() {
    let r = scenario_b(Params { n: N_TEST, ..Params::incomparabilite_m2() }, 5, 20_000).unwrap();
    assert!(
        r.mesures.decisions_non_fiables > 0,
        "aucune décision inter-partitions n'a été comptée comme non fiable"
    );
    let nominal = scenario_b(params(), 5, 20_000).unwrap();
    assert_eq!(
        nominal.mesures.decisions_non_fiables, 0,
        "sur une seule partition, M2 n'a pas d'objet"
    );
}

/// NF-10 — mode « trace optimiste » : écriture **avant** l'action. Les deux
/// positions sont des réglages déclarés, sans valeur par défaut, et chacune a
/// son mode de défaillance.
#[test]
fn nf10_trace_optimiste_et_pessimiste_sont_deux_reglages() {
    let optimiste = scenario_b(Params { n: N_TEST, ..Params::trace_optimiste() }, 6, 20_000).unwrap();
    let pessimiste = scenario_b(params(), 6, 20_000).unwrap();
    assert_eq!(Params::trace_optimiste().moment_trace, MomentTrace::Avant);
    assert_eq!(Params::scenario_b().moment_trace, MomentTrace::Apres);

    // Optimiste : la trace est déposée même quand l'action échoue. Elle
    // surestime, et rien dans le milieu ne le trahit.
    assert!(
        optimiste.mesures.depots_sans_effet > 0,
        "aucun dépôt sans effet : la trace optimiste n'a pas son mode de défaillance"
    );
    assert_eq!(
        pessimiste.mesures.depots_sans_effet, 0,
        "en pessimiste, un échec d'action ne dépose pas"
    );

    // Pessimiste : entre l'action et l'écriture, un autre agent réattaque une
    // ressource déjà traitée. Les deux positions ont bien leur prix.
    assert!(
        pessimiste.mesures.reattaques > 0,
        "aucune réattaque mesurée : la trace pessimiste n'a pas son mode de défaillance"
    );
}

/// F3 — l'interface n'affiche jamais « convergé ». Le résultat ne porte aucun
/// champ qui l'affirmerait, et l'écart à l'optimum est une **mesure seule**,
/// sans borne, parce que le traité ne chiffre pas cette distance.
#[test]
fn aucun_resultat_ne_pretend_a_la_convergence() {
    let r = scenario_b(params(), 8, 20_000).unwrap();
    let ecart = r.mesures.ecart_a_loptimum().unwrap();
    assert!(
        (0.0..1.0).contains(&ecart),
        "écart à l'optimum hors plage : {ecart}"
    );
    assert!(r.entete.contains("sim-core"), "{}", r.entete);
    assert!(r.entete.contains("graine 8"), "{}", r.entete);
}
