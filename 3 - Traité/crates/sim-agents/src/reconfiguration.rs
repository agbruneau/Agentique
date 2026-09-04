//! Déclencheur de reconfiguration (EX-A44) et régimes de clé (EX-A45).
//!
//! Deux décisions que le §4.1 exige de rendre explicites, parce que les
//! confondre coûte cher et que rien dans le code ne le signale autrement.

/// EX-A44 — **le déclencheur de reconfiguration est déclaré** : charge offerte
/// ou appartenance.
///
/// Les deux classes d'événements appellent des réponses **opposées** : ajouter
/// des agents dans un cas ; réaffecter le travail du disparu sans ajouter
/// personne dans l'autre, puisque le débit total n'a pas manqué — il a été
/// redistribué.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Declencheur {
    /// ρ = λ/µ franchit un seuil : il manque de la capacité.
    ChargeOfferte,
    /// Un agent s'est arrêté, ou une partition réseau est apparue. La capacité
    /// totale n'a pas changé de besoin ; c'est sa répartition qui a changé.
    Appartenance,
}

/// Réponse apportée.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Reponse {
    /// Ajouter des agents.
    MonterEnCharge,
    /// Réaffecter le travail du disparu, sans ajouter personne.
    Reaffecter,
}

/// Coût net d'une reconfiguration.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub struct CoutNet {
    /// Agents ajoutés en réponse au déclencheur.
    pub agents_injectes: u32,
    /// Rééquilibrages supplémentaires provoqués par l'injection.
    pub reequilibrages_supplementaires: u32,
    /// Vrai si la réponse ne correspond pas au déclencheur.
    pub confusion: bool,
}

/// Le simulateur **permet la confusion** — répondre à une panne partielle par
/// une montée en charge — et en compte le prix. L'interdire priverait le
/// scénario de ce qu'il doit montrer.
pub fn reconfigurer(d: Declencheur, r: Reponse, n: u32) -> CoutNet {
    match (d, r) {
        (Declencheur::ChargeOfferte, Reponse::MonterEnCharge) => CoutNet {
            agents_injectes: (n / 4).max(1),
            reequilibrages_supplementaires: 1,
            confusion: false,
        },
        (Declencheur::Appartenance, Reponse::Reaffecter) => CoutNet {
            agents_injectes: 0,
            reequilibrages_supplementaires: 1,
            confusion: false,
        },
        (Declencheur::Appartenance, Reponse::MonterEnCharge) => CoutNet {
            // Des agents injectés dans un système **en train de se réparer**,
            // et le rééquilibrage supplémentaire qu'ils provoquent.
            agents_injectes: (n / 4).max(1),
            reequilibrages_supplementaires: 2,
            confusion: true,
        },
        (Declencheur::ChargeOfferte, Reponse::Reaffecter) => CoutNet {
            agents_injectes: 0,
            // Réaffecter ne crée pas la capacité qui manque : il faudra
            // recommencer.
            reequilibrages_supplementaires: 2,
            confusion: true,
        },
    }
}

/// EX-A45 — **les deux régimes de clé, et la partition chaude qu'ils
/// décident.**
///
/// L'unité de regroupement n'est pas choisie par l'essaim mais par le
/// producteur : dans le milieu événementiel, c'est la partition du sujet. Le
/// simulateur expose les régimes et leurs conséquences opposées, **jamais un
/// seul**, et exige qu'un régime soit choisi explicitement — il n'y a pas de
/// défaut silencieux.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum RegimeDeCle {
    /// Répartition uniforme sur les p partitions, au prix de **toute la
    /// localité** : deux événements du même client tombent dans deux
    /// partitions distinctes et perdent leur ordre relatif — c'est M2, pas un
    /// défaut.
    HachageDeLaCle,
    /// Conserve la localité, donc l'ordre relatif par client, mais **importe la
    /// dissymétrie du domaine**. Mode de défaillance dominant : la **partition
    /// chaude**.
    CleSemantique,
    /// Rend l'affectation stable : l'arrivée ou le départ d'un agent ne déplace
    /// qu'environ 1/n des clés au lieu de la totalité. Atténue le coût du
    /// premier régime, **ne le supprime pas**.
    HachageCoherent,
}

impl RegimeDeCle {
    /// Ce que ce régime **achète**. Aucun n'est gratuit ; voir
    /// [`RegimeDeCle::coute`] pour le prix.
    pub fn achete(self) -> &'static str {
        match self {
            RegimeDeCle::HachageDeLaCle => "répartition uniforme sur les p partitions",
            RegimeDeCle::CleSemantique => "la localité, donc l'ordre relatif par client",
            RegimeDeCle::HachageCoherent => {
                "la stabilité de l'affectation : environ 1/n des clés déplacées au lieu de toutes"
            }
        }
    }

    /// Ce que ce régime **coûte**, affiché au même rang que ce qu'il achète.
    pub fn coute(self) -> &'static str {
        match self {
            RegimeDeCle::HachageDeLaCle => {
                "détruit TOUTE localité : deux événements du même client tombent dans deux \
                 partitions distinctes et perdent leur ordre relatif — c'est M2, pas un défaut"
            }
            RegimeDeCle::CleSemantique => {
                "importe la dissymétrie du domaine ; mode de défaillance dominant : la partition \
                 chaude"
            }
            RegimeDeCle::HachageCoherent => {
                "atténue le coût du hachage simple, ne le supprime pas ; conçu pour des réseaux \
                 où aucun serveur ne peut connaître l'état complet"
            }
        }
    }

    /// Fraction des clés déplacées quand la population passe de n à n + 1.
    pub fn cles_deplacees(self, n: u32) -> f64 {
        match self {
            // Le hachage modulo p redistribue tout dès que p change.
            RegimeDeCle::HachageDeLaCle => 1.0,
            RegimeDeCle::CleSemantique => 1.0,
            RegimeDeCle::HachageCoherent => 1.0 / (n.max(1) as f64),
        }
    }
}

/// Affectation des clés aux partitions selon le régime.
pub struct Affectation {
    /// Régime de clé en vigueur — obligatoire, sans défaut silencieux.
    pub regime: RegimeDeCle,
    /// Nombre de partitions.
    pub p: u32,
    /// Poids de chaque clé — la dissymétrie du domaine, quand elle existe.
    pub poids: Vec<u64>,
}

impl Affectation {
    /// Construit l'affectation. Le régime est **obligatoire** : il n'y a pas de
    /// constructeur par défaut, parce qu'il n'y a pas de défaut silencieux.
    pub fn nouvelle(regime: RegimeDeCle, p: u32, poids: Vec<u64>) -> Affectation {
        Affectation { regime, p, poids }
    }

    /// La partition d'une clé sous le régime en vigueur.
    pub fn partition_de(&self, cle: u64) -> u32 {
        match self.regime {
            RegimeDeCle::HachageDeLaCle | RegimeDeCle::HachageCoherent => {
                ((cle.wrapping_mul(0x9e37_79b9_7f4a_7c15) >> 32) % self.p.max(1) as u64) as u32
            }
            // La clé sémantique regroupe : les clés voisines vont ensemble, ce
            // qui conserve la localité et importe la dissymétrie.
            RegimeDeCle::CleSemantique => {
                let groupes = self.poids.len().max(1) as u64;
                let par_partition = (groupes / self.p.max(1) as u64).max(1);
                ((cle / par_partition) % self.p.max(1) as u64) as u32
            }
        }
    }

    /// Charge de chaque partition.
    ///
    /// Au moins une case : `partition_de` ramène tout à 0 quand `p` vaut 0
    /// (`p.max(1)`), et un vecteur vide sortirait des bornes juste après.
    pub fn charge(&self) -> Vec<u64> {
        let mut c = vec![0u64; (self.p.max(1)) as usize];
        for (cle, poids) in self.poids.iter().enumerate() {
            c[self.partition_de(cle as u64) as usize] += poids;
        }
        c
    }

    /// **Partition chaude** — rapport entre la partition la plus chargée et la
    /// charge moyenne. Au-delà de 2, le régime a importé une dissymétrie que
    /// l'essaim ne peut pas corriger.
    pub fn partition_chaude(&self) -> f64 {
        let c = self.charge();
        let total: u64 = c.iter().sum();
        if total == 0 {
            return 1.0;
        }
        let moyenne = total as f64 / c.len() as f64;
        *c.iter().max().unwrap() as f64 / moyenne
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-A44 — les deux déclencheurs appellent des réponses **opposées**, et
    /// répondre correctement ne coûte pas la même chose que se tromper.
    #[test]
    fn les_deux_declencheurs_appellent_des_reponses_opposees() {
        let bon_charge = reconfigurer(Declencheur::ChargeOfferte, Reponse::MonterEnCharge, 64);
        let bon_appartenance = reconfigurer(Declencheur::Appartenance, Reponse::Reaffecter, 64);
        assert!(!bon_charge.confusion);
        assert!(!bon_appartenance.confusion);
        assert!(bon_charge.agents_injectes > 0, "il manque de la capacité");
        assert_eq!(
            bon_appartenance.agents_injectes, 0,
            "le débit total n'a pas manqué, il a été redistribué"
        );
    }

    /// EX-A44 — le simulateur **permet la confusion** et en compte le prix :
    /// des agents injectés dans un système en train de se réparer, et le
    /// rééquilibrage supplémentaire qu'ils provoquent.
    #[test]
    fn la_confusion_est_permise_et_son_prix_est_compte() {
        let confus = reconfigurer(Declencheur::Appartenance, Reponse::MonterEnCharge, 64);
        assert!(confus.confusion);
        assert!(confus.agents_injectes > 0);
        let correct = reconfigurer(Declencheur::Appartenance, Reponse::Reaffecter, 64);
        assert!(
            confus.reequilibrages_supplementaires > correct.reequilibrages_supplementaires,
            "le prix de la confusion doit être visible"
        );
    }

    /// EX-A45 — chaque régime expose ce qu'il achète **et** ce qu'il coûte,
    /// jamais l'un sans l'autre.
    #[test]
    fn chaque_regime_expose_ce_quil_achete_et_ce_quil_coute() {
        for r in [
            RegimeDeCle::HachageDeLaCle,
            RegimeDeCle::CleSemantique,
            RegimeDeCle::HachageCoherent,
        ] {
            assert!(!r.achete().is_empty());
            assert!(!r.coute().is_empty());
        }
        assert!(RegimeDeCle::HachageDeLaCle
            .coute()
            .contains("c'est M2, pas un défaut"));
        assert!(RegimeDeCle::CleSemantique
            .coute()
            .contains("partition chaude"));
        assert!(RegimeDeCle::HachageCoherent
            .coute()
            .contains("ne le supprime pas"));
    }

    /// EX-A45 — la clé sémantique **importe la dissymétrie du domaine** : sous
    /// une charge inégale, elle produit une partition chaude que le hachage
    /// évite.
    #[test]
    fn la_cle_semantique_produit_la_partition_chaude() {
        // Un domaine dissymétrique : les premières clés portent l'essentiel du
        // trafic, comme un gros client parmi de petits.
        let poids: Vec<u64> = (0..256u64)
            .map(|i| if i < 16 { 1_000 } else { 1 })
            .collect();

        let semantique = Affectation::nouvelle(RegimeDeCle::CleSemantique, 8, poids.clone());
        let hachage = Affectation::nouvelle(RegimeDeCle::HachageDeLaCle, 8, poids);

        assert!(
            semantique.partition_chaude() > 4.0,
            "la clé sémantique doit concentrer, rapport {:.2}",
            semantique.partition_chaude()
        );
        assert!(
            hachage.partition_chaude() < 2.5,
            "le hachage doit répartir, rapport {:.2}",
            hachage.partition_chaude()
        );
    }

    /// EX-A45 — le hachage cohérent ne déplace qu'environ 1/n des clés, là où
    /// le hachage simple les déplace toutes.
    #[test]
    fn le_hachage_coherent_stabilise_laffectation() {
        assert_eq!(RegimeDeCle::HachageDeLaCle.cles_deplacees(100), 1.0);
        let coherent = RegimeDeCle::HachageCoherent.cles_deplacees(100);
        assert!((coherent - 0.01).abs() < 1e-9, "{coherent}");
    }
}
