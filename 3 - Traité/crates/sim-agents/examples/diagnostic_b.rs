//! Diagnostic du scénario B : effort par tranche, pour lire la dynamique du
//! désapprentissage au lieu de la déduire d'un cumul.

use sim_agents::scenario_b;
use sim_agents::stigmergie::Params;

fn main() {
    for (nom, params, budget) in [
        ("nominal 200k", Params::scenario_b(), 200_000u64),
        ("nominal 600k", Params::scenario_b(), 600_000),
        ("verrouillage 600k", Params::verrouillage(), 600_000),
    ] {
        let r = scenario_b(params, 1, budget).unwrap();
        println!(
            "\n=== {nom} — meilleure après bascule : {} ===",
            r.meilleure_ressource
        );
        for (t, tranche) in r.mesures.effort_par_tranche.iter().enumerate() {
            let total: u64 = tranche.iter().sum();
            if total == 0 {
                continue;
            }
            let parts: Vec<String> = tranche
                .iter()
                .map(|n| format!("{:3.0}", *n as f64 * 100.0 / total as f64))
                .collect();
            println!("t{t:02} | {}", parts.join(" "));
        }
        println!(
            "final sur la meilleure : {:.3} | suit : {} | retard max : {}",
            r.part_effort_finale_sur_la_meilleure(),
            r.suit_la_bascule(),
            r.mesures.retard_consommation_max
        );
    }
}
