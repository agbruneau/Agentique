//! NF-01 à NF-04 — déterminisme et reproductibilité.
//!
//! > NF-04 : un test d'intégration exécute 100 graines et vérifie l'égalité des
//! > traces entre deux exécutions consécutives.
//!
//! C'est la propriété fondatrice (PD1) : si elle tombe, aucune figure produite
//! n'est rejouable et O4 s'effondre avec elle.

use sim_agents::scenario_b;
use sim_agents::stigmergie::Params;

/// Budget court : ce qui est vérifié ici est l'égalité de deux traces, pas le
/// régime atteint. Cent graines à budget long ne diraient rien de plus.
const BUDGET: u64 = 6_000;

fn params() -> Params {
    Params {
        n: 16,
        ..Params::scenario_b()
    }
}

/// NF-04 — cent graines, deux exécutions chacune, traces identiques.
#[test]
fn nf04_cent_graines_se_rejouent_a_lidentique() {
    for graine in 0..100u64 {
        let a = scenario_b(params(), graine, BUDGET).unwrap();
        let b = scenario_b(params(), graine, BUDGET).unwrap();
        assert_eq!(
            a.trace, b.trace,
            "graine {graine} : traces différentes entre deux exécutions consécutives"
        );
        assert_eq!(a.mesures.effort, b.mesures.effort, "graine {graine}");
        assert_eq!(a.mesures.cycles, b.mesures.cycles, "graine {graine}");
        assert_eq!(a.temps_logique, b.temps_logique, "graine {graine}");
    }
}

/// Cent graines distinctes doivent produire cent traces distinctes — sans quoi
/// le test précédent serait satisfait par un simulateur qui ignore sa graine.
#[test]
fn cent_graines_produisent_cent_traces_distinctes() {
    let mut traces: Vec<u64> = (0..100u64)
        .map(|g| scenario_b(params(), g, BUDGET).unwrap().trace)
        .collect();
    traces.sort_unstable();
    let avant = traces.len();
    traces.dedup();
    assert_eq!(avant, traces.len(), "des graines distinctes ont produit la même trace");
}

/// Le modèle de faute fait partie de l'identité d'une exécution (PD6) : deux
/// exécutions de même graine sous deux réglages différents ne doivent pas
/// produire la même trace, sans quoi le réglage ne réglerait rien.
#[test]
fn un_reglage_different_produit_une_trace_differente() {
    let nominal = scenario_b(params(), 1, BUDGET).unwrap();
    for (nom, p) in [
        ("verrouillage", Params { n: 16, ..Params::verrouillage() }),
        ("essaim aveugle", Params { n: 16, ..Params::essaim_aveugle() }),
        ("rejeu", Params { n: 16, ..Params::rejeu() }),
        ("incomparabilité M2", Params { n: 16, ..Params::incomparabilite_m2() }),
    ] {
        let autre = scenario_b(p, 1, BUDGET).unwrap();
        assert_ne!(
            nominal.trace, autre.trace,
            "le préréglage « {nom} » produit la même trace que le nominal"
        );
    }
}

/// NF-03 — l'en-tête d'export porte la version, la graine et le hachage de
/// configuration ; deux configurations différentes ont deux hachages différents.
#[test]
fn nf03_lentete_identifie_lexecution() {
    let a = scenario_b(params(), 1, BUDGET).unwrap();
    let b = scenario_b(params(), 2, BUDGET).unwrap();
    assert!(a.entete.contains("sim-core"));
    assert!(a.entete.contains("graine 1"));
    assert!(b.entete.contains("graine 2"));
    assert_ne!(a.entete, b.entete);
}
