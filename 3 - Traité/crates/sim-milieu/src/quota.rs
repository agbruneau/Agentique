//! Quota et prix croissant par ressource — le seul levier structurel contre la
//! conformité (EX-M26, §8.1 du traité).
//!
//! Le §8.1 du traité recense trois leviers de diversification qui se paient — diversifier
//! les modèles, les invites et les contextes, ou le tirage —, dont le troisième
//! seul est presque gratuit et « n'agit que sur la marge de la distribution, non
//! sur son mode ; c'est précisément le mode qui est en cause ». Puis :
//!
//! > Le seul levier structurel appartient au milieu : rendre coûteuse la
//! > décision majoritaire plutôt qu'espérer sa dispersion — quota par ressource,
//! > prix croissant avec le nombre de preneurs, refus d'écriture au-delà d'un
//! > seuil de concentration. (§8.1 du traité)
//!
//! **Ce qui distingue ce levier de ceux du §5.3 du traité, et c'est tout son intérêt** :
//! les leviers de gouvernance bornent un agent **qui accepte de l'être** et
//! s'appliquent dans le processus même dont le §8.3 du traité suppose qu'il agit contre le
//! système. Celui-ci borne une **ressource**, ce qui ne demande le consentement
//! de personne.
//!
//! Coût : **0 message**, un compteur par clé dans le milieu.

use crate::journal::Cle;
use std::collections::BTreeMap;

/// Politique de concentration appliquée à l'écriture.
#[derive(Clone, Copy, PartialEq, Debug)]
pub enum Politique {
    /// Aucune. C'est le défaut : une politique qu'on n'a pas demandée ne borne
    /// rien.
    Aucune,
    /// Quota dur : au-delà de `plafond` preneurs distincts sur une clé,
    /// l'écriture est refusée.
    QuotaDur {
        /// Nombre maximal de preneurs distincts admis sur une même clé.
        plafond: u32,
    },
    /// Prix croissant avec le nombre de preneurs : l'écriture est acceptée, et
    /// son coût déclaré est multiplié. Ne refuse rien — c'est une taxe, pas une
    /// barrière, et l'affichage doit le dire.
    PrixCroissant {
        /// Facteur ajouté au prix par preneur au-delà du premier. Le k-ième
        /// preneur distinct d'une clé paie `1 + pente × (k − 1)` : le premier
        /// paie le prix nominal, le **deuxième paie déjà la pente**. Compté sur
        /// l'état d'avant, le deuxième aurait encore payé le nominal, et le prix
        /// n'aurait pas crû « avec le nombre de preneurs » (§8.1 du traité).
        pente: f64,
    },
    /// Refus au-delà d'un seuil de **concentration** : la part d'une clé dans le
    /// total des écritures ne peut pas dépasser `part_max`.
    ///
    /// **Une exception, et elle est structurelle** : la toute première écriture
    /// est acceptée quel que soit `part_max`, sa part valant nécessairement 1.
    /// La borne ne tient donc qu'à partir de la deuxième — sans quoi aucune clé
    /// ne pourrait jamais commencer, et la politique refuserait tout.
    SeuilDeConcentration {
        /// Part maximale d'une clé dans le total, dans (0, 1].
        part_max: f64,
    },
}

/// Ce qu'une politique répond à une demande d'écriture.
#[derive(Clone, Copy, PartialEq, Debug)]
pub enum Verdict {
    /// Acceptée, au prix indiqué. `1.0` est le prix nominal.
    Acceptee {
        /// Multiplicateur de prix appliqué.
        prix: f64,
    },
    /// Refusée, avec le motif à afficher.
    Refusee {
        /// Motif du refus, tel qu'affiché.
        motif: &'static str,
    },
}

/// Compteur par clé, et la politique qui s'y applique (EX-M26).
#[derive(Clone, Debug)]
pub struct Quotas {
    politique: Politique,
    /// `clé -> nombre d'écritures`. `BTreeMap` : itération ordonnée (PD1).
    ecritures: BTreeMap<Cle, u64>,
    /// `clé -> preneurs distincts`. Un preneur est un agent, et il **devrait**
    /// venir de l'identité apposée par le milieu (EX-M24) plutôt que d'une
    /// déclaration de l'écrivain. Ici il est celui que l'appelant présente :
    /// aucun chemin ne relie ce compteur à [`crate::journal::Enregistrement`],
    /// et aucun scénario ne l'instancie (`crate::hors_perimetre()`).
    preneurs: BTreeMap<Cle, std::collections::BTreeSet<u32>>,
    total: u64,
    refus: u64,
    prix_cumule: f64,
}

impl Quotas {
    /// Installe une politique. `Politique::Aucune` est le défaut du milieu.
    pub fn nouveau(politique: Politique) -> Quotas {
        Quotas {
            politique,
            ecritures: BTreeMap::new(),
            preneurs: BTreeMap::new(),
            total: 0,
            refus: 0,
            prix_cumule: 0.0,
        }
    }

    /// Soumet une écriture. **0 message** : le verdict est local au milieu.
    ///
    /// L'ordre des contrôles est un contrat : les **refus** sont prononcés sur
    /// l'état **avant** cette écriture, puis les compteurs avancent seulement si
    /// elle est acceptée. Sans quoi le premier preneur d'une clé serait déjà
    /// compté contre son propre plafond.
    ///
    /// Le **prix**, lui, inclut le soumissionnaire : une taxe ne refuse rien, et
    /// facturer sur l'état d'avant faisait payer le prix nominal au deuxième
    /// preneur distinct. Refus et prix ne se règlent donc pas sur le même état,
    /// et c'est délibéré.
    pub fn soumettre(&mut self, cle: Cle, preneur: u32) -> Verdict {
        let verdict = self.verdict(cle, preneur);
        match verdict {
            Verdict::Acceptee { prix } => {
                *self.ecritures.entry(cle).or_insert(0) += 1;
                self.preneurs.entry(cle).or_default().insert(preneur);
                self.total += 1;
                self.prix_cumule += prix;
            }
            Verdict::Refusee { .. } => self.refus += 1,
        }
        verdict
    }

    fn verdict(&self, cle: Cle, preneur: u32) -> Verdict {
        let deja_preneur = self
            .preneurs
            .get(&cle)
            .is_some_and(|s| s.contains(&preneur));
        let preneurs = self.preneurs.get(&cle).map_or(0, |s| s.len()) as u32;
        match self.politique {
            Politique::Aucune => Verdict::Acceptee { prix: 1.0 },
            Politique::QuotaDur { plafond } => {
                if !deja_preneur && preneurs >= plafond {
                    Verdict::Refusee {
                        motif: "quota par ressource atteint — la décision majoritaire est \
                                bornée par le milieu, non par l'agent (EX-M26)",
                    }
                } else {
                    Verdict::Acceptee { prix: 1.0 }
                }
            }
            // Le soumissionnaire compte : `preneurs` est l'état d'avant, et le
            // k-ième preneur distinct doit payer `1 + pente × (k − 1)`.
            Politique::PrixCroissant { pente } => Verdict::Acceptee {
                prix: 1.0
                    + pente * f64::from((preneurs + u32::from(!deja_preneur)).saturating_sub(1)),
            },
            Politique::SeuilDeConcentration { part_max } => {
                if self.total == 0 {
                    return Verdict::Acceptee { prix: 1.0 };
                }
                let part = (self.ecritures.get(&cle).copied().unwrap_or(0) + 1) as f64
                    / (self.total + 1) as f64;
                if part > part_max {
                    Verdict::Refusee {
                        motif: "seuil de concentration franchi — au-delà, le milieu refuse \
                                l'écriture (EX-M26)",
                    }
                } else {
                    Verdict::Acceptee { prix: 1.0 }
                }
            }
        }
    }

    /// Part de la clé la plus prise dans le total des écritures acceptées.
    ///
    /// C'est la grandeur que la politique de concentration borne, et elle
    /// s'affiche même quand la politique est `Aucune` : une concentration
    /// mesurée et non bornée est une information, pas un défaut.
    pub fn concentration_max(&self) -> f64 {
        if self.total == 0 {
            return 0.0;
        }
        self.ecritures
            .values()
            .copied()
            .max()
            .map_or(0.0, |m| m as f64 / self.total as f64)
    }

    /// Preneurs distincts sur cette clé.
    pub fn preneurs(&self, cle: Cle) -> u32 {
        self.preneurs.get(&cle).map_or(0, |s| s.len()) as u32
    }

    /// Écritures refusées par la politique.
    pub fn refus(&self) -> u64 {
        self.refus
    }

    /// Prix cumulé des écritures acceptées. Vaut le nombre d'écritures sous une
    /// politique sans prix : le surcoût se lit par différence.
    pub fn prix_cumule(&self) -> f64 {
        self.prix_cumule
    }

    /// Ce que le mécanisme ne traite pas (tableau 22, EX-V21).
    pub fn ne_traite_pas() -> &'static str {
        "une population qui converge sur une ressource non médiée par le milieu — le compteur \
         ne voit que ce qui passe par une clé (§8.1 du traité)"
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-M26 — sans politique, rien n'est borné : la concentration est **mesurée**,
    /// jamais contrainte.
    #[test]
    fn sans_politique_rien_nest_borne() {
        let mut q = Quotas::nouveau(Politique::Aucune);
        for a in 0..10 {
            assert_eq!(q.soumettre(7, a), Verdict::Acceptee { prix: 1.0 });
        }
        assert_eq!(q.refus(), 0);
        assert_eq!(q.concentration_max(), 1.0, "mesurée, et non bornée");
    }

    /// EX-M26 — le quota dur **refuse** au-delà du plafond ; le refus est le signal,
    /// et il est rendu à l'écrivain.
    #[test]
    fn le_quota_dur_refuse_le_preneur_au_dela_du_plafond() {
        let mut q = Quotas::nouveau(Politique::QuotaDur { plafond: 3 });
        for a in 0..3 {
            assert!(matches!(q.soumettre(1, a), Verdict::Acceptee { .. }));
        }
        assert!(
            matches!(q.soumettre(1, 3), Verdict::Refusee { .. }),
            "le quatrième preneur distinct est refusé"
        );
        assert!(
            matches!(q.soumettre(1, 0), Verdict::Acceptee { .. }),
            "un preneur déjà compté n'est pas refusé une seconde fois"
        );
        assert_eq!(q.preneurs(1), 3);
    }

    /// EX-M26 — le prix croissant **taxe sans jamais refuser** : c'est l'autre
    /// politique, et elle ne borne rien.
    #[test]
    fn le_prix_croissant_taxe_sans_refuser() {
        let mut q = Quotas::nouveau(Politique::PrixCroissant { pente: 1.0 });
        for a in 0..4 {
            assert!(matches!(q.soumettre(2, a), Verdict::Acceptee { .. }));
        }
        assert_eq!(
            q.refus(),
            0,
            "une taxe ne refuse rien, et l'affichage le dit"
        );
        // Prix 1, 2, 3, 4 : le k-ième preneur distinct paie 1 + pente × (k − 1),
        // le soumissionnaire compris. Facturé sur l'état d'avant, le deuxième
        // preneur payait encore le nominal et le cumul valait 7.
        assert_eq!(q.prix_cumule(), 10.0);
    }

    /// EX-M26 — « prix croissant **avec le nombre de preneurs** » (§8.1 du traité) : le
    /// deuxième preneur distinct paie déjà la pente. Un preneur déjà compté ne
    /// fait pas monter le prix, puisqu'il ne fait pas monter leur nombre.
    #[test]
    fn le_prix_monte_des_le_deuxieme_preneur() {
        let mut q = Quotas::nouveau(Politique::PrixCroissant { pente: 1.0 });
        assert_eq!(q.soumettre(2, 0), Verdict::Acceptee { prix: 1.0 });
        assert_eq!(
            q.soumettre(2, 1),
            Verdict::Acceptee { prix: 2.0 },
            "un facteur ajouté par preneur au-delà du premier"
        );
        assert_eq!(
            q.soumettre(2, 0),
            Verdict::Acceptee { prix: 2.0 },
            "un preneur déjà compté ne fait pas monter leur nombre"
        );
    }

    /// EX-M26 — le seuil de concentration borne la part qu'une seule clé peut
    /// prendre, ce que ni le quota dur ni le prix ne font.
    #[test]
    fn le_seuil_de_concentration_borne_la_part_dune_cle() {
        let mut q = Quotas::nouveau(Politique::SeuilDeConcentration { part_max: 0.5 });
        assert!(matches!(q.soumettre(1, 0), Verdict::Acceptee { .. }));
        assert!(matches!(q.soumettre(2, 1), Verdict::Acceptee { .. }));
        // La clé 1 passerait à 2/3 > 0,5.
        assert!(matches!(q.soumettre(1, 0), Verdict::Refusee { .. }));
        assert!(q.concentration_max() <= 0.5 + 1e-9);
    }

    /// EX-M26 — la première écriture échappe au seuil de concentration, et c'est
    /// structurel : sa part vaut 1 quelle que soit la politique. La borne
    /// s'applique à partir de la deuxième, et l'affichage ne doit pas promettre
    /// autre chose.
    #[test]
    fn la_premiere_ecriture_echappe_au_seuil_de_concentration() {
        let mut q = Quotas::nouveau(Politique::SeuilDeConcentration { part_max: 0.1 });
        assert!(
            matches!(q.soumettre(1, 0), Verdict::Acceptee { .. }),
            "sinon aucune clé ne pourrait commencer"
        );
        assert_eq!(
            q.concentration_max(),
            1.0,
            "au-dessus du seuil, et mesurée telle quelle"
        );
        assert!(
            matches!(q.soumettre(1, 0), Verdict::Refusee { .. }),
            "la borne tient ensuite"
        );
    }

    /// EX-M26 — le verdict porte sur l'état **d'avant** l'écriture : un quota qui se
    /// jugerait après coup aurait déjà laissé passer ce qu'il devait borner.
    #[test]
    fn le_verdict_porte_sur_letat_davant_lecriture() {
        // Sinon le premier preneur d'une clé serait compté contre son propre
        // plafond, et un quota de 1 refuserait tout.
        let mut q = Quotas::nouveau(Politique::QuotaDur { plafond: 1 });
        assert!(matches!(q.soumettre(9, 0), Verdict::Acceptee { .. }));
        assert!(matches!(q.soumettre(9, 1), Verdict::Refusee { .. }));
    }
}
