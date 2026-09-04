//! Banc d'essai DT1 / RQ1 — divergence flottante natif contre WASM.
//!
//! Question posée par le PRD (§11, DT1 ; §10, RQ1 ; NF-02) : l'arithmétique du
//! cœur peut-elle rester en flottant, ou faut-il des points fixes sur tout
//! chemin qui influence l'ordonnancement ?
//!
//! Méthode : chaque groupe exécute N itérations d'**une seule** opération et
//! accumule un hachage FNV-1a des bits IEEE de chaque résultat. Un seul bit qui
//! diffère entre les deux cibles change le hachage. Un groupe par opération, et
//! non un groupe fourre-tout : le hachage doit nommer l'opération fautive, pas
//! seulement signaler qu'il y en a une.
//!
//! Les entrées sont produites par un générateur congruentiel **entier**. Aucune
//! entrée ne dépend d'un calcul flottant : les deux cibles reçoivent donc les
//! mêmes bits, et tout écart mesuré est imputable à l'opération testée seule.

// `clippy.toml` interdit ces méthodes dans tout le dépôt, sur la foi de ce que
// ce banc a mesuré. Le banc est le seul endroit qui doit continuer de les
// appeler : il les compare à leurs homologues portables, et l'interdiction
// s'appliquerait à sa propre preuve.
#![allow(clippy::disallowed_methods)]

use std::f64::consts::{PI, TAU};

/// Constante de départ FNV-1a, 64 bits.
const FNV_DEPART: u64 = 0xcbf2_9ce4_8422_2325;
/// Nombre premier FNV-1a, 64 bits.
const FNV_PREMIER: u64 = 0x0000_0100_0000_01b3;

/// Absorbe les 8 octets de la représentation IEEE-754 de `x`.
///
/// On hache `to_bits()` et non la valeur : deux NaN de charges utiles
/// différentes, ou un +0,0 contre un −0,0, doivent compter comme un écart.
#[inline]
fn melange(h: &mut u64, x: f64) {
    let bits = x.to_bits();
    for i in 0..8 {
        *h ^= (bits >> (i * 8)) & 0xff;
        *h = h.wrapping_mul(FNV_PREMIER);
    }
}

/// Générateur d'entrées, entier pur (LCG de Knuth). Rend un f64 dans [0, 1)
/// construit par assemblage de bits, jamais par division : la valeur produite
/// est identique bit à bit sur toute cible avant que l'opération testée ne
/// s'applique.
#[inline]
fn suivant(etat: &mut u64) -> f64 {
    *etat = etat
        .wrapping_mul(6_364_136_223_846_793_005)
        .wrapping_add(1_442_695_040_888_963_407);
    // Mantisse à 52 bits dans l'exposant de [1, 2), puis translation.
    f64::from_bits(0x3ff0_0000_0000_0000 | (*etat >> 12)) - 1.0
}

/// Les opérations mesurées. L'ordre est stable : le rapport y renvoie par
/// numéro, et le chargeur Node itère sur cette plage.
#[derive(Clone, Copy)]
pub enum Groupe {
    /// Addition, soustraction, multiplication, division, racine carrée,
    /// arrondis, comparaisons, conversion f64 → u64. IEEE-754 impose le
    /// résultat exact de chacune : l'attente est zéro écart.
    Base = 0,
    /// Logarithme népérien — tirage d'une latence exponentielle, −ln(u)/λ.
    Ln = 1,
    /// Exponentielle — décroissance γ de la trace stigmergique (§1.2).
    Exp = 2,
    /// Puissance réelle — plancher d'exploration (φ_min/φ_max)^α (EX-A11c).
    Powf = 3,
    /// Sinus — cap d'un agent dans l'alignement du ch. 1 (EX-A02).
    Sin = 4,
    /// Cosinus — idem.
    Cos = 5,
    /// Arc-tangente à deux arguments — moyenne de caps (EX-A02).
    Atan2 = 6,
    /// Multiplication-addition fusionnée — dépend de la présence matérielle
    /// d'un FMA ; WASM ne l'expose pas comme instruction.
    MulAdd = 7,

    // Les mêmes opérations, prises dans `libm` : une implantation en Rust pur
    // qui n'utilise que le groupe `Base`. Si le groupe `Base` est identique
    // entre les cibles, celles-ci doivent l'être aussi — le banc le vérifie au
    // lieu de le supposer.
    /// `libm::log` — l'homologue portable de `f64::ln`.
    LibmLn = 8,
    /// `libm::exp`.
    LibmExp = 9,
    /// `libm::pow`.
    LibmPow = 10,
    /// `libm::sin`.
    LibmSin = 11,
    /// `libm::cos`.
    LibmCos = 12,
    /// `libm::atan2`.
    LibmAtan2 = 13,
    /// `libm::fma` — arrondi unique, obtenu par le calcul et non par le
    /// matériel.
    LibmFma = 14,
}

/// Nombre de groupes. Le chargeur Node en dépend.
pub const NB_GROUPES: u32 = 15;

impl Groupe {
    /// Décode un numéro de groupe. `None` au-delà de [`NB_GROUPES`].
    pub fn depuis_u32(g: u32) -> Option<Groupe> {
        Some(match g {
            0 => Groupe::Base,
            1 => Groupe::Ln,
            2 => Groupe::Exp,
            3 => Groupe::Powf,
            4 => Groupe::Sin,
            5 => Groupe::Cos,
            6 => Groupe::Atan2,
            7 => Groupe::MulAdd,
            8 => Groupe::LibmLn,
            9 => Groupe::LibmExp,
            10 => Groupe::LibmPow,
            11 => Groupe::LibmSin,
            12 => Groupe::LibmCos,
            13 => Groupe::LibmAtan2,
            14 => Groupe::LibmFma,
            _ => return None,
        })
    }

    /// Nom du groupe tel qu'il apparaît dans la sortie du banc.
    pub fn nom(self) -> &'static str {
        match self {
            Groupe::Base => "base (+ - * / sqrt, arrondis, conversions)",
            Groupe::Ln => "ln",
            Groupe::Exp => "exp",
            Groupe::Powf => "powf",
            Groupe::Sin => "sin",
            Groupe::Cos => "cos",
            Groupe::Atan2 => "atan2",
            Groupe::MulAdd => "mul_add (FMA)",
            Groupe::LibmLn => "libm::log",
            Groupe::LibmExp => "libm::exp",
            Groupe::LibmPow => "libm::pow",
            Groupe::LibmSin => "libm::sin",
            Groupe::LibmCos => "libm::cos",
            Groupe::LibmAtan2 => "libm::atan2",
            Groupe::LibmFma => "libm::fma",
        }
    }

    /// Vrai si la parité natif/WASM de ce groupe est **exigée** par NF-02.
    ///
    /// Les opérations `std` transcendantes ne le sont pas : le banc les mesure
    /// pour établir le constat qui motive DT1, et leur divergence est le
    /// résultat attendu. Faire échouer le banc sur elles reviendrait à faire
    /// échouer la mesure sur ce qu'elle a mesuré.
    pub fn exige_parite(self) -> bool {
        !matches!(
            self,
            Groupe::Ln
                | Groupe::Exp
                | Groupe::Powf
                | Groupe::Sin
                | Groupe::Cos
                | Groupe::Atan2
                | Groupe::MulAdd
        )
    }

    /// Ce que le groupe conditionne dans le produit, pour le rapport.
    pub fn usage(self) -> &'static str {
        match self {
            Groupe::Base => "dates d'événements, comparaisons de la file, compteurs",
            Groupe::Ln => "tirage exponentiel des latences du milieu (EX-M09)",
            Groupe::Exp => "décroissance γ de la trace (EX-A01)",
            Groupe::Powf => "plancher d'exploration et fraction d'effort (EX-A11c)",
            Groupe::Sin => "alignement de caps (EX-A02)",
            Groupe::Cos => "alignement de caps (EX-A02)",
            Groupe::Atan2 => "moyenne de caps (EX-A02)",
            Groupe::MulAdd => "accumulation de φ (EX-A01)",
            Groupe::LibmLn => "candidat portable pour ln",
            Groupe::LibmExp => "candidat portable pour exp",
            Groupe::LibmPow => "candidat portable pour powf",
            Groupe::LibmSin => "candidat portable pour sin",
            Groupe::LibmCos => "candidat portable pour cos",
            Groupe::LibmAtan2 => "candidat portable pour atan2",
            Groupe::LibmFma => "candidat portable pour mul_add",
        }
    }
}

/// Exécute `n` itérations du groupe `g` et rend le hachage de tous les
/// résultats intermédiaires produits.
pub fn banc(g: Groupe, n: u32) -> u64 {
    let mut h = FNV_DEPART;
    let mut etat = 0x2545_f491_4f6c_dd1d;
    let mut acc = 0.0f64;

    for _ in 0..n {
        let a = suivant(&mut etat);
        let b = suivant(&mut etat);

        match g {
            Groupe::Base => {
                // Accumulation en série : c'est la forme qu'a l'avance de
                // l'horloge logique et le cumul de φ.
                acc = (acc + a) * 0.5;
                melange(&mut h, acc);
                melange(&mut h, a - b);
                melange(&mut h, a * b);
                // b + 1 ∈ [1, 2) : jamais de division par une valeur voisine de zéro.
                melange(&mut h, a / (b + 1.0));
                melange(&mut h, (a * a + b * b).sqrt());
                melange(&mut h, (a * 1e9).floor());
                melange(&mut h, (b * 1e9).ceil());
                // Conversion vers l'entier : c'est elle qui date un événement.
                melange(&mut h, ((a * 1e9) as u64) as f64);
                // Comparaison : le départage de la file de priorité en dépend.
                melange(&mut h, if a < b { a } else { b });
            }
            // b + 1 ∈ [1, 2) : argument strictement positif, jamais un ln(0).
            Groupe::Ln => melange(&mut h, (b + 1.0).ln()),
            // −a ∈ (−1, 0] : plage de la décroissance, jamais un débordement.
            Groupe::Exp => melange(&mut h, (-a).exp()),
            // Base ∈ [1, 2), exposant ∈ [0, 5) : la plage d'α du scénario B.
            Groupe::Powf => melange(&mut h, (b + 1.0).powf(a * 5.0)),
            // Un cap parcourt [−π, π].
            Groupe::Sin => melange(&mut h, (a * TAU - PI).sin()),
            Groupe::Cos => melange(&mut h, (a * TAU - PI).cos()),
            Groupe::Atan2 => melange(&mut h, (a - 0.5).atan2(b - 0.5)),
            Groupe::MulAdd => {
                acc = a.mul_add(b, acc);
                melange(&mut h, acc);
            }

            // Mêmes arguments, aux mêmes bits près, que leurs homologues std.
            Groupe::LibmLn => melange(&mut h, libm::log(b + 1.0)),
            Groupe::LibmExp => melange(&mut h, libm::exp(-a)),
            Groupe::LibmPow => melange(&mut h, libm::pow(b + 1.0, a * 5.0)),
            Groupe::LibmSin => melange(&mut h, libm::sin(a * TAU - PI)),
            Groupe::LibmCos => melange(&mut h, libm::cos(a * TAU - PI)),
            Groupe::LibmAtan2 => melange(&mut h, libm::atan2(a - 0.5, b - 0.5)),
            Groupe::LibmFma => {
                acc = libm::fma(a, b, acc);
                melange(&mut h, acc);
            }
        }
    }
    h
}
