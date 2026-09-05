//! Surface d'appel du banc DT1. Le même code sert les deux cibles :
//! `cdylib` chargée par Node pour wasm32-unknown-unknown, `rlib` liée au
//! binaire natif.

#![deny(missing_docs)]

pub mod noyau;

pub use noyau::{Groupe, NB_GROUPES};

/// Point d'entrée unique, appelable depuis WebAssembly.
///
/// Rend le hachage du groupe, ou 0 si le numéro de groupe n'existe pas — le
/// chargeur traite 0 comme une erreur, aucun groupe valide ne le produisant.
///
/// # Safety
/// Aucune : la fonction ne déréférence rien. `extern "C"` sert seulement à
/// figer l'ABI pour l'export WASM.
#[no_mangle]
pub extern "C" fn banc_dt1(groupe: u32, n: u32) -> u64 {
    match Groupe::depuis_u32(groupe) {
        Some(g) => noyau::banc(g, n),
        None => 0,
    }
}

/// Nombre de groupes, lu par le chargeur pour ne pas dupliquer la constante.
#[no_mangle]
pub extern "C" fn banc_dt1_nb_groupes() -> u32 {
    NB_GROUPES
}
