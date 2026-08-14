//! Diagnostic de la boucle d'élasticité : trajectoire de la population.

use sim_agents::elasticite::{Controleur, Params};

fn main() {
    for (nom, p) in [
        ("nominal", Params::default()),
        ("oscillation", Params::oscillation()),
    ] {
        let mut c = Controleur::nouveau(p);
        println!("\n=== {nom} ===");
        for i in 0..40 {
            let eff = c.population_effective();
            c.periode(80.0, 10.0);
            if i < 24 {
                println!(
                    "t{:02} pop={:3} eff={:3} m={:6.2}",
                    i,
                    c.population,
                    eff,
                    80.0 / eff.max(1) as f64
                );
            }
        }
        println!(
            "final pop={} amplitude(10)={} {}",
            c.population,
            c.amplitude(10),
            c.affichage_point_fixe()
        );
    }
}
