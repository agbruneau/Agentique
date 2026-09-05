//! Côté natif du banc DT1. Écrit une ligne par groupe, au format que le
//! comparateur Node relit : `numéro<TAB>hachage hexadécimal<TAB>nom`.

use banc_dt1::noyau::{self, Groupe};

fn main() {
    let n: u32 = std::env::args()
        .nth(1)
        .and_then(|a| a.parse().ok())
        .unwrap_or(1_000_000);

    println!("# banc DT1 — natif — {} itérations par groupe", n);
    println!("# colonnes : numéro, hachage, parité exigée (NF-02), nom");
    for g in 0..banc_dt1::NB_GROUPES {
        let groupe = Groupe::depuis_u32(g).expect("numéro de groupe hors plage");
        println!(
            "{}\t{:016x}\t{}\t{}",
            g,
            noyau::banc(groupe, n),
            if groupe.exige_parite() {
                "exigée"
            } else {
                "constat"
            },
            groupe.nom(),
        );
    }
}
