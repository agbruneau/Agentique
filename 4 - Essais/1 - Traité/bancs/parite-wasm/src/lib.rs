//! Banc EX-V12 — parité de sortie entre le rendu natif et le rendu WASM.
//!
//! > Le rendu WASM et le rendu natif produisent des chiffres identiques pour la
//! > même graine ; toute divergence est un **défaut bloquant**. (EX-V12)
//!
//! Ce que le banc compare n'est pas l'image mais les **chiffres** qui la
//! produisent : la trace d'exécution du scénario, son effort par ressource et
//! ses compteurs. Deux rendus qui partent des mêmes nombres montrent la même
//! figure ; deux rendus qui partent de nombres différents ne peuvent pas être
//! rapprochés par une comparaison de pixels.
//!
//! Le banc DT1 vérifiait les opérations ; celui-ci vérifie qu'un mécanisme
//! entier, avec ses milliers d'appels enchaînés, ne diverge pas non plus.

#![deny(missing_docs)]

use sim_agents::scenario_b;
use sim_agents::stigmergie::Params;

/// Les scénarios mesurés. L'ordre est stable : le chargeur itère sur la plage.
pub const NB_CAS: u32 = 6;

/// Nom du cas, pour le rapport.
pub fn nom_du_cas(cas: u32) -> &'static str {
    match cas {
        0 => "B nominal",
        1 => "B verrouillage (γ = 1)",
        2 => "B essaim aveugle (T < ℓ₉₉)",
        3 => "B rejeu",
        4 => "B incomparabilité M2",
        5 => "B trace optimiste",
        _ => "inconnu",
    }
}

fn params(cas: u32) -> Params {
    let base = match cas {
        1 => Params::verrouillage(),
        2 => Params::essaim_aveugle(),
        3 => Params::rejeu(),
        4 => Params::incomparabilite_m2(),
        5 => Params::trace_optimiste(),
        _ => Params::scenario_b(),
    };
    Params { n: 16, ..base }
}

/// Exécute un cas et rend une **empreinte** de tout ce qui alimente la figure.
///
/// Absorber la seule trace du moteur ne suffirait pas : deux exécutions
/// pourraient partager leur entrelacement et différer sur les valeurs
/// calculées, qui sont ce que l'écran montre.
pub fn empreinte(cas: u32, graine: u64, budget: u64) -> u64 {
    // Paniquer plutôt que rendre 0 : un échec **symétrique** sur les deux
    // cibles rendrait deux fois `0000000000000000`, le comparateur conclurait
    // « identique » et le banc afficherait « EX-V12 : tenue sur 6 cas » sans
    // qu'aucun scénario n'ait tourné. Un verdict de parité doit distinguer
    // « mêmes chiffres » de « aucun chiffre ».
    let r = scenario_b(params(cas), graine, budget)
        .unwrap_or_else(|motif| panic!("cas {cas} refusé : {motif}"));
    let mut h: u64 = 0xcbf2_9ce4_8422_2325;
    let mut absorber = |x: u64| {
        for i in 0..8 {
            h ^= (x >> (i * 8)) & 0xff;
            h = h.wrapping_mul(0x0000_0100_0000_01b3);
        }
    };
    absorber(r.trace);
    absorber(r.mesures.cycles);
    absorber(r.mesures.effets_dupliques);
    absorber(r.mesures.decisions_non_fiables);
    absorber(r.mesures.cycles_sans_retroaction);
    absorber(r.mesures.depots_sans_effet);
    absorber(r.mesures.reattaques);
    absorber(r.mesures.retard_consommation_max);
    for e in &r.mesures.effort {
        absorber(*e);
    }
    for tranche in &r.mesures.effort_par_tranche {
        for e in tranche {
            absorber(*e);
        }
    }
    // Les grandeurs flottantes affichées, prises sur leurs bits : c'est bien
    // l'égalité **exacte** qu'EX-V12 exige, pas un voisinage.
    for phi in &r.phi_moyen {
        absorber(phi.to_bits());
    }
    absorber(r.mesures.utilite_recoltee.to_bits());
    // Les deux grandeurs sont des `Option<f64>` depuis le 4 septembre 2026.
    // L'absence retrouve ici la sentinelle qu'elles portaient avant, pour que
    // les six empreintes de NF-03 ne bougent pas d'un bit sur ce changement de
    // type — le banc mesure la parité natif/WASM, pas la forme de l'API.
    absorber(
        r.mesures
            .plancher_observe
            .unwrap_or(f64::INFINITY)
            .to_bits(),
    );
    absorber(
        r.mesures
            .hors_dominante_observee
            .unwrap_or(f64::INFINITY)
            .to_bits(),
    );
    h
}

/// Point d'entrée appelable depuis WebAssembly.
///
/// # Safety
/// Aucune : la fonction ne déréférence rien. `extern "C"` fige l'ABI pour
/// l'export.
#[no_mangle]
pub extern "C" fn banc_parite(cas: u32, graine: u64, budget: u64) -> u64 {
    empreinte(cas, graine, budget)
}

/// Nombre de cas du banc, lu par le chargeur Node.
///
/// # Safety
/// Aucune : la fonction ne déréférence rien.
#[no_mangle]
pub extern "C" fn banc_parite_nb_cas() -> u32 {
    NB_CAS
}
