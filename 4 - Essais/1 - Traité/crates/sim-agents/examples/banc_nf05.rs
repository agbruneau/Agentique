//! Banc NF-05 — débit de simulation, en **secondes simulées par seconde-cœur**.
//!
//! C'est l'unité du traité, et non le nombre d'exécutions. La cible est
//! ≥ 10³ s simulées/s-cœur à n = 1 000, p = 16.
//!
//! Le temps mural est lu **ici**, dans le banc, et jamais dans les crates de
//! simulation : PD1 interdit l'horloge du système au cœur, et la mesure de
//! performance est par nature hors du monde clos.
//!
//! NF-05 est une cible d'ingénierie, pas une mesure du traité (§8.2 du PRD, note de
//! méthode).

use sim_agents::scenario_b;
use sim_agents::stigmergie::Params;
use std::time::Instant;

fn main() {
    println!("banc NF-05 — cible : ≥ 1000 s simulées / s-cœur à n = 1000, p = 16\n");
    println!(
        "     n     p    événements   s simulées   s-cœur   débit (s sim./s-cœur)  retard max"
    );

    for (n, p, budget) in [
        (64u32, 8u32, 200_000u64),
        (256, 16, 200_000),
        (1_000, 16, 200_000),
        (1_000, 16, 1_000_000),
    ] {
        // L'intervalle de lecture reste **constant** : EX-A12 exige un
        // intervalle borné du milieu, et une borne qui suivrait n ne serait
        // plus une borne. Le retard de consommation qui en résulte à grand n
        // est le phénomène, pas un artefact — il est mesuré et rapporté.
        let params = Params {
            n,
            p,
            ..Params::scenario_b()
        };
        let periode_ms = params.periode_cycle_ms;

        let depart = Instant::now();
        let r = scenario_b(params, 1, budget).unwrap();
        let secondes_coeur = depart.elapsed().as_secs_f64();

        // Temps simulé : chaque agent exécute un cycle par période, et le
        // nombre total de cycles est mesuré.
        let simule_s = r.mesures.cycles as f64 / n as f64 * periode_ms / 1_000.0;
        let debit = simule_s / secondes_coeur;

        println!(
            "{n:6} {p:5} {budget:13} {simule_s:12.2} {secondes_coeur:8.2} {debit:16.1} {:11}{}",
            r.mesures.retard_consommation_max,
            if n == 1_000 && debit >= 1_000.0 {
                "  ✓ NF-05"
            } else if n == 1_000 {
                "  ✗ NF-05"
            } else {
                ""
            }
        );
    }
}
