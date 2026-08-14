//! Binaire natif. Tout est dans la bibliothèque, que la cible web partage.
//!
//! Les deux `main` sont gardés, parce que la cible `[[bin]]` ne l'est pas :
//! `cargo clippy -p sim-viz --target wasm32-unknown-unknown` la vérifie aussi,
//! et `lancer_natif` n'existe pas sur cette cible. Sans la garde, la ligne de
//! preuve du protocole ne passe qu'avec `--lib`.

#[cfg(not(target_arch = "wasm32"))]
fn main() -> eframe::Result<()> {
    sim_viz::lancer_natif()
}

/// La cible web n'a pas de binaire : tout passe par `lancer_web`, appelé par le
/// module JavaScript au chargement.
#[cfg(target_arch = "wasm32")]
fn main() {}
