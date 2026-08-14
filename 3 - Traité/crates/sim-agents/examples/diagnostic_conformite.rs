//! Φ_c du scénario B en fonction de la part de conformité (EX-A56, EX-C19).
//!
//! Ce diagnostic existe parce que sa **mesure contredit ce que le PRD annonçait**
//! avant elle : le curseur de familles était censé faire passer Φ_c de ≈ 0 à ≈ 1,
//! et il ne le fait pas. Voir [`sim_agents::conformite::CONSTAT_DE_MESURE`].

use sim_agents::scenario_m::scenario_m;
use sim_agents::stigmergie::Params;

fn main() {
    let mut p = Params::scenario_b();
    p.n = 24;
    p.m = 6;
    p.p = 1;
    p.intervalle_lecture = 128;
    println!("part  Φ_c      ±        accord   indép.   paires   partages  bornes effacées");
    for part in [0.0, 0.25, 0.5, 0.75, 1.0] {
        let r = scenario_m(p.clone(), part, 7, 20_000).expect("scénario M");
        println!(
            "{part:<5} {:.4}   {:.4}   {:.4}   {:.4}   {:<8} {:<9} {}",
            r.conformite.phi_c,
            r.conformite.precision().unwrap_or(f64::NAN),
            r.conformite.accord_observe,
            r.conformite.accord_sous_independance,
            r.conformite.paires,
            r.tirages_partages,
            r.bornes_effacees()
        );
    }
    println!("\n{}", sim_agents::conformite::CONSTAT_DE_MESURE);
}
