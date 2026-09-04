//! Scénario G — agrégat fenêtré et **sous-compte silencieux** (EX-A06).
//!
//! > Une réponse fausse d'une quantité inconnue, que rien dans le résultat ne
//! > trahit. (§7.1)
//!
//! L'esquisse HyperLogLog fusionnable **est** un treillis à jonction monotone :
//! la fusion registre à registre par maximum est idempotente, commutative,
//! associative. C'est la famille « état » d'EX-A21, implantée là où elle gagne
//! sa place.
//!
//! Le manifeste ne supprime pas le problème : il **convertit une erreur
//! silencieuse en erreur nommée**, et le traité interdit d'en revendiquer
//! davantage.

use crate::Bloc;

/// Le bloc de trois du **scénario G** — agrégat fenêtré et sous-compte
/// silencieux (PD8).
pub const BLOC_G: Bloc = Bloc {
    en_clair:
        "On compte quelque chose sur une fenêtre de temps, en fusionnant les comptes partiels de \
         chaque partition. Si l'une d'elles se tait, le total publié reste étiqueté « complet » : \
         il manque une part qu'aucun chiffre du résultat ne révèle. Tenir la liste des \
         contributeurs attendus ne rend pas la réponse juste — cela rend seulement son erreur \
         visible.",
    these: "Une réponse fausse d'une quantité inconnue, que rien dans le résultat ne trahit.",
    source: "§7.1, p. 104 (4ᵉ éd.) — esquisses fusionnables, filigrane, volets, manifeste",
    mecanisme_visible:
        "désactiver le manifeste ; une partition muette cesse de contribuer, le volet publié \
         reste étiqueté « complet », et l'erreur d'estimation affichée ne bouge pas — parce \
         qu'elle mesure l'esquisse, pas l'absence.",
    ne_demontre_pas:
        "que le manifeste supprime le problème. Il convertit une erreur silencieuse en erreur \
         nommée, et le traité interdit d'en revendiquer davantage.",
};

/// Nombre de registres. `m = 2 048`.
pub const M: usize = 2_048;
/// Bits par registre.
pub const BITS_PAR_REGISTRE: usize = 5;

/// Erreur type de l'esquisse : `1,04/√m`.
pub fn erreur_type() -> f64 {
    1.04 / (M as f64).sqrt()
}

/// Taille d'une esquisse, en octets.
pub fn octets_par_esquisse() -> usize {
    M * BITS_PAR_REGISTRE / 8
}

/// splitmix64 — mélangeur à avalanche complète, déterministe et portable (DT1 :
/// entier pur, aucune transcendante).
fn melange(x: u64) -> u64 {
    let mut z = x.wrapping_add(0x9e37_79b9_7f4a_7c15);
    z = (z ^ (z >> 30)).wrapping_mul(0xbf58_476d_1ce4_e5b9);
    z = (z ^ (z >> 27)).wrapping_mul(0x94d0_49bb_1331_11eb);
    z ^ (z >> 31)
}

/// Une esquisse HyperLogLog fusionnable.
#[derive(Clone, Debug)]
pub struct Esquisse {
    registres: Vec<u8>,
}

impl Default for Esquisse {
    fn default() -> Self {
        Esquisse::nouvelle()
    }
}

impl Esquisse {
    /// Esquisse vide : cardinalité estimée nulle.
    pub fn nouvelle() -> Esquisse {
        Esquisse {
            registres: vec![0; M],
        }
    }

    /// Ajoute un élément.
    ///
    /// Le mélangeur est splitmix64 et non une simple multiplication : HLL
    /// dépend de l'uniformité **bit à bit** du haché, et un produit par une
    /// constante laisse des corrélations qui font sous-estimer les rangs — donc
    /// la cardinalité, d'un facteur mesuré à cinq avant correction.
    pub fn ajouter(&mut self, valeur: u64) {
        let h = melange(valeur);
        let index = (h >> (64 - 11)) as usize % M;
        // Nombre de zéros de tête du reste, plus un.
        let reste = h << 11;
        let rang = (reste.leading_zeros() + 1).min(31) as u8;
        if rang > self.registres[index] {
            self.registres[index] = rang;
        }
    }

    /// **La fusion est le sup registre à registre** : idempotente, commutative,
    /// associative. C'est ce qui en fait un treillis à jonction monotone.
    pub fn fusionner(&mut self, autre: &Esquisse) {
        for (a, b) in self.registres.iter_mut().zip(&autre.registres) {
            if *b > *a {
                *a = *b;
            }
        }
    }

    /// Cardinalité estimée.
    pub fn estimer(&self) -> f64 {
        let m = M as f64;
        let alpha = 0.7213 / (1.0 + 1.079 / m);
        let somme: f64 = self
            .registres
            .iter()
            .map(|r| libm::pow(2.0, -(*r as f64)))
            .sum();
        let brut = alpha * m * m / somme;
        // Correction des petites cardinalités.
        let vides = self.registres.iter().filter(|r| **r == 0).count();
        if brut <= 2.5 * m && vides > 0 {
            m * libm::log(m / vides as f64)
        } else {
            brut
        }
    }
}

/// Un volet publié pour une fenêtre.
#[derive(Clone, Debug)]
pub struct Volet {
    /// Numéro de la fenêtre publiée.
    pub fenetre: u64,
    /// Cardinalité estimée sur les contributions **reçues**.
    pub estimation: f64,
    /// Erreur d'estimation de l'esquisse. Elle mesure **l'esquisse**, pas
    /// l'absence — et c'est tout le piège.
    pub erreur_esquisse: f64,
    /// Étiquette du volet.
    pub etiquette: Etiquette,
    /// Révisions successives : un volet est révisable.
    pub revision: u32,
}

/// Ce que le volet déclare de lui-même.
#[derive(Clone, Debug, PartialEq)]
pub enum Etiquette {
    /// Toutes les partitions attendues ont contribué.
    Complet,
    /// Certaines manquent, et elles sont **nommées**.
    Partiel {
        /// Les partitions attendues qui n'ont pas contribué.
        manquants: Vec<u32>,
    },
}

impl Etiquette {
    /// Le libellé affiché avec le volet. C'est le seul endroit où l'absence
    /// devient visible : l'erreur d'estimation, elle, ne bouge pas.
    pub fn libelle(&self) -> String {
        match self {
            Etiquette::Complet => "complet".to_string(),
            Etiquette::Partiel { manquants } => {
                format!("partiel, manquants = {manquants:?}")
            }
        }
    }
}

/// L'agrégat fenêtré coopératif.
pub struct AgregatFenetre {
    /// **Manifeste M** : les partitions attendues. Sans lui, l'absence est
    /// indétectable.
    pub manifeste: Option<Vec<u32>>,
    /// Contributions reçues pour la fenêtre courante.
    contributions: Vec<(u32, Esquisse)>,
    /// Volets publiés, dans l'ordre des fenêtres.
    pub volets: Vec<Volet>,
    /// Filigrane heuristique : au-delà, la fenêtre est déclenchée.
    pub filigrane: u64,
}

impl AgregatFenetre {
    /// Agrégat neuf. `manifeste` à `None` est le préréglage du scénario G :
    /// tout volet se déclarera « complet », y compris quand il ne l'est pas.
    pub fn nouveau(manifeste: Option<Vec<u32>>) -> AgregatFenetre {
        AgregatFenetre {
            manifeste,
            contributions: Vec::new(),
            volets: Vec::new(),
            filigrane: 0,
        }
    }

    /// Une partition contribue.
    pub fn contribuer(&mut self, partition: u32, esquisse: Esquisse) {
        self.contributions.push((partition, esquisse));
    }

    /// Déclenche la fenêtre et publie un volet.
    ///
    /// **Avec manifeste**, l'absence est nommée. **Sans**, le volet se déclare
    /// complet — et il est faux, d'une quantité que rien ne trahit.
    pub fn declencher(&mut self, fenetre: u64) -> Volet {
        let mut fusion = Esquisse::nouvelle();
        for (_, e) in &self.contributions {
            fusion.fusionner(e);
        }

        let etiquette = match &self.manifeste {
            Some(attendues) => {
                let manquants: Vec<u32> = attendues
                    .iter()
                    .filter(|p| !self.contributions.iter().any(|(q, _)| q == *p))
                    .copied()
                    .collect();
                if manquants.is_empty() {
                    Etiquette::Complet
                } else {
                    Etiquette::Partiel { manquants }
                }
            }
            // Sans manifeste, rien ne distingue une partition muette d'une
            // partition vide.
            None => Etiquette::Complet,
        };

        let revision = self.volets.iter().filter(|v| v.fenetre == fenetre).count() as u32;
        let volet = Volet {
            fenetre,
            estimation: fusion.estimer(),
            // **L'erreur affichée mesure l'esquisse, pas l'absence.** Elle ne
            // bouge pas quand une partition se tait, et c'est le piège.
            erreur_esquisse: erreur_type(),
            etiquette,
            revision,
        };
        self.volets.push(volet.clone());
        self.contributions.clear();
        volet
    }

    /// Convention de comptage des tours (§7.1, tableau 18) : sous la convention
    /// de l'aller-retour bloquant, l'essaim stigmergique à esquisses coûte
    /// **0 tour**.
    pub const TOURS: u64 = 0;
}

#[cfg(test)]
mod tests {
    use super::*;

    fn esquisse_de(debut: u64, fin: u64) -> Esquisse {
        let mut e = Esquisse::nouvelle();
        for v in debut..fin {
            e.ajouter(v);
        }
        e
    }

    /// EX-A06 — les paramètres de l'esquisse sont ceux du traité.
    #[test]
    fn les_parametres_de_lesquisse_sont_ceux_du_traite() {
        assert_eq!(M, 2_048);
        assert_eq!(BITS_PAR_REGISTRE, 5);
        // Erreur type ≈ 1,04/√2048 ≈ 2,3 %.
        assert!((erreur_type() - 0.0230).abs() < 1e-4, "{}", erreur_type());
        // ≈ 1,3 ko par esquisse — le traité annonce « ≈ 1,5 ko ».
        assert_eq!(octets_par_esquisse(), 1_280);
        assert_eq!(
            AgregatFenetre::TOURS,
            0,
            "0 tour sous la convention du §7.1"
        );
    }

    /// L'estimation est correcte à l'erreur type près.
    #[test]
    fn lestimation_est_correcte_a_lerreur_type_pres() {
        let e = esquisse_de(0, 100_000);
        let estime = e.estimer();
        let erreur = (estime - 100_000.0).abs() / 100_000.0;
        assert!(erreur < 4.0 * erreur_type(), "erreur relative {erreur:.4}");
    }

    /// **EX-A21** — la fusion est idempotente, commutative et associative :
    /// c'est un treillis à jonction monotone.
    #[test]
    fn la_fusion_est_un_treillis_a_jonction_monotone() {
        let a = esquisse_de(0, 1_000);
        let b = esquisse_de(500, 1_500);
        let c = esquisse_de(1_000, 2_000);

        // Idempotence : fusionner deux fois ne change rien.
        let mut x = a.clone();
        x.fusionner(&b);
        let avant = x.estimer();
        x.fusionner(&b);
        assert_eq!(x.estimer(), avant);

        // Commutativité.
        let mut ab = a.clone();
        ab.fusionner(&b);
        let mut ba = b.clone();
        ba.fusionner(&a);
        assert_eq!(ab.estimer(), ba.estimer());

        // Associativité.
        let mut gauche = a.clone();
        gauche.fusionner(&b);
        gauche.fusionner(&c);
        let mut droite = b.clone();
        droite.fusionner(&c);
        let mut a2 = a.clone();
        a2.fusionner(&droite);
        assert_eq!(gauche.estimer(), a2.estimer());
    }

    /// **Critère d'acceptation du scénario G** — avec manifeste, une partition
    /// muette produit un volet **« partiel, manquants = … »**.
    #[test]
    fn avec_manifeste_une_partition_muette_est_nommee() {
        let mut a = AgregatFenetre::nouveau(Some(vec![0, 1, 2, 3]));
        a.contribuer(0, esquisse_de(0, 1_000));
        a.contribuer(1, esquisse_de(1_000, 2_000));
        // La partition 2 se tait.
        a.contribuer(3, esquisse_de(3_000, 4_000));
        let v = a.declencher(1);
        assert_eq!(v.etiquette, Etiquette::Partiel { manquants: vec![2] });
        assert!(v.etiquette.libelle().contains("manquants = [2]"));
    }

    /// … et **sans manifeste**, elle produit un volet **« complet » qui est
    /// faux**. Le contraste est le livrable pédagogique.
    #[test]
    fn sans_manifeste_le_volet_se_declare_complet_et_il_est_faux() {
        let complet = {
            let mut a = AgregatFenetre::nouveau(None);
            for p in 0..4u32 {
                a.contribuer(p, esquisse_de(p as u64 * 1_000, (p as u64 + 1) * 1_000));
            }
            a.declencher(1)
        };
        let ampute = {
            let mut a = AgregatFenetre::nouveau(None);
            for p in [0u32, 1, 3] {
                a.contribuer(p, esquisse_de(p as u64 * 1_000, (p as u64 + 1) * 1_000));
            }
            a.declencher(1)
        };

        // Les deux se déclarent complets.
        assert_eq!(ampute.etiquette, Etiquette::Complet);
        assert_eq!(complet.etiquette, Etiquette::Complet);

        // L'estimation est fausse — d'une quantité inconnue.
        assert!(
            ampute.estimation < complet.estimation * 0.9,
            "{} contre {}",
            ampute.estimation,
            complet.estimation
        );

        // **Et l'erreur affichée ne bouge pas** : elle mesure l'esquisse, pas
        // l'absence. C'est le sous-compte silencieux.
        assert_eq!(ampute.erreur_esquisse, complet.erreur_esquisse);
    }

    /// Le volet est **révisable** : un déclenchement ultérieur sur la même
    /// fenêtre porte un numéro de révision.
    #[test]
    fn un_volet_est_revisable() {
        let mut a = AgregatFenetre::nouveau(Some(vec![0, 1]));
        a.contribuer(0, esquisse_de(0, 500));
        let premier = a.declencher(1);
        assert_eq!(premier.revision, 0);
        assert!(matches!(premier.etiquette, Etiquette::Partiel { .. }));

        // La partition retardataire arrive : le volet est révisé.
        a.contribuer(0, esquisse_de(0, 500));
        a.contribuer(1, esquisse_de(500, 1_000));
        let second = a.declencher(1);
        assert_eq!(second.revision, 1);
        assert_eq!(second.etiquette, Etiquette::Complet);
        assert!(second.estimation > premier.estimation);
    }

    /// PD8 — le bloc de trois.
    #[test]
    fn le_scenario_porte_son_bloc_de_trois() {
        assert!(BLOC_G.these.contains("quantité inconnue"));
        assert!(BLOC_G.ne_demontre_pas.contains("erreur nommée"));
    }
}
