//! Côté natif du banc EX-V12. Écrit une ligne par cas, au format que le
//! comparateur Node relit : `numéro<TAB>empreinte<TAB>nom`.

use banc_parite::{empreinte, nom_du_cas, NB_CAS};

fn main() {
    let mut args = std::env::args().skip(1);
    let graine: u64 = args.next().and_then(|a| a.parse().ok()).unwrap_or(1);
    let budget: u64 = args.next().and_then(|a| a.parse().ok()).unwrap_or(20_000);

    println!("# banc EX-V12 — natif — graine {graine}, budget {budget}");
    for cas in 0..NB_CAS {
        println!(
            "{cas}\t{:016x}\t{}",
            empreinte(cas, graine, budget),
            nom_du_cas(cas)
        );
    }
}
