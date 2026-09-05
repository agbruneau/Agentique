//! Familles de décision — la variance d'une population est un composant
//! (EX-C19, PD13).
//!
//! Le §1.1 de la deuxième édition du traité pose la convention que ce module
//! transpose :
//!
//! > le vecteur de paramètres qui distingue δᵢ de δ n'est pas un raffinement de
//! > notation, c'est la seule source de variance de la population, et un essaim
//! > qui ne l'instancie pas n'a pas n agents mais un agent exécuté n fois.
//!
//! En robotique, la variance est **fournie par le monde** — position, usure,
//! bruit de capteur. En logiciel, elle ne l'est pas : deux agents portant le
//! même modèle, la même invite et le même contexte ne diffèrent par rien. Ce
//! module rend la propriété réglable au lieu de la supposer.
//!
//! **Le décalque est délibéré.** [`Familles`] est à la décision ce que
//! [`crate::horloge::Domaines`] est à la panne : une structure nommée dont la
//! grandeur agrégée se **dérive**, jamais ne se saisit. Le motif est le même,
//! et la raison aussi — un scalaire posé n'est pas réfutable.
//!
//! **Ce module ne mesure pas Φ_c.** La conformité empirique est une statistique
//! des décisions **déposées dans le milieu**, donc elle se lit dans
//! `sim-agents` (EX-A56). Ce qui est ici est la cause, pas la mesure.

use crate::alea::Alea;
use crate::ActeurId;
use std::collections::BTreeMap;

/// Partition de la population en familles de décision.
///
/// Un agent appartient à **exactement une** famille. Deux agents d'une même
/// famille consomment le même tirage pour une même décision **au même tour de
/// leur boucle** : c'est la transposition littérale de « même modèle, même
/// invite, même contexte ». Le partage porte sur le rang de la décision, jamais
/// sur la date — voir [`TirageDeDecision`], qui dit pourquoi.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Familles {
    /// Famille de chaque agent, indexée par `ActeurId.0`.
    appartenance: Vec<u32>,
    /// Nombre de familles distinctes. **Total**, non par partition du milieu.
    nb: u32,
}

impl Familles {
    /// Une famille par agent : la population **décorrélée**.
    ///
    /// C'est le défaut, et c'est l'hypothèse **la plus favorable** — celle sous
    /// laquelle toutes les bornes probabilistes du produit ont été mesurées. Elle
    /// s'affiche comme un réglage à sa valeur extrême, jamais comme la nature des
    /// choses (PD13).
    pub fn une_par_agent(n: u32) -> Familles {
        Familles {
            appartenance: (0..n).collect(),
            nb: n,
        }
    }

    /// Une famille unique : la population **conforme**, qui décide comme un seul
    /// agent.
    pub fn unique(n: u32) -> Familles {
        Familles {
            appartenance: vec![0; n as usize],
            nb: if n == 0 { 0 } else { 1 },
        }
    }

    /// Position intermédiaire : `part` ∈ [0, 1] interpole entre une famille par
    /// agent (`part = 0`) et une famille unique (`part = 1`).
    ///
    /// **Aucune provenance dans le traité.** La source mesure les deux extrêmes
    /// et note qu'en déploiement réel la variance est plus grande qu'en
    /// laboratoire tout en restant très inférieure à celle d'une population
    /// humaine ; elle ne donne aucune loi entre les deux. Toute mesure prise à
    /// une position intermédiaire est donc une **interpolation du produit** et
    /// s'étiquette comme telle (F1, incertitude 7 du PRD).
    pub fn interpole(n: u32, part: f64) -> Familles {
        let part = part.clamp(0.0, 1.0);
        if n == 0 {
            return Familles {
                appartenance: Vec::new(),
                nb: 0,
            };
        }
        // De n familles à 1, linéairement. `ceil` plutôt que `round` : à part
        // strictement inférieure à 1, il reste au moins deux familles, donc la
        // population n'est jamais déclarée conforme par un arrondi.
        let nb = if part >= 1.0 {
            1
        } else {
            let brut = f64::from(n) * (1.0 - part);
            (brut.ceil() as u32).clamp(2.min(n), n)
        };
        Familles {
            // Répartition par tranches contiguës : déterministe, sans tirage. Le
            // produit passe par `u64` : `i * nb` déborde `u32` dès n ≈ 65 536, et
            // le profil release du dépôt ne pose pas `overflow-checks`, donc
            // l'enroulement replierait des agents éloignés dans une même famille
            // sans un mot.
            appartenance: (0..n)
                .map(|i| (u64::from(i) * u64::from(nb) / u64::from(n)) as u32)
                .collect(),
            nb,
        }
    }

    /// Valeur rendue par [`Familles::famille`] pour un agent hors bornes.
    ///
    /// Elle marque l'**absence** de famille, et aucun mécanisme ne la traite
    /// comme un numéro : EX-C19 pose qu'un agent appartient à exactement une
    /// famille, et un agent qui n'existe pas n'en a aucune.
    pub const SANS_FAMILLE: u32 = u32::MAX;

    /// Nombre d'agents.
    pub fn n(&self) -> u32 {
        self.appartenance.len() as u32
    }

    /// Famille de cet agent, ou [`Familles::SANS_FAMILLE`] hors bornes — un
    /// appelant qui interroge un agent inexistant ne doit pas recevoir une
    /// corrélation. La sentinelle n'est **pas** un numéro de famille : elle ne
    /// partage rien, ni ici ni au [`TirageDeDecision`].
    pub fn famille(&self, agent: ActeurId) -> u32 {
        self.appartenance
            .get(agent.0 as usize)
            .copied()
            .unwrap_or(Familles::SANS_FAMILLE)
    }

    /// Ces deux agents partagent-ils leur tirage de décision ?
    pub fn partagent(&self, a: ActeurId, b: ActeurId) -> bool {
        let (fa, fb) = (self.famille(a), self.famille(b));
        fa != Familles::SANS_FAMILLE && fa == fb
    }

    /// **Diversité effective** : le paramètre de contrôle de Φ_c (§8.1 du traité).
    ///
    /// C'est le nombre de familles distinctes, et rien de plus — le traité
    /// énumère aussi le nombre d'invites et l'entropie de la température de
    /// tirage, qui n'ont aucun objet dans un monde clos où δ est un programme.
    pub fn diversite_effective(&self) -> u32 {
        self.nb
    }

    /// Part de conformité **structurelle**, dans [0, 1] : 0 quand chaque agent
    /// est seul, 1 quand tous partagent une famille.
    ///
    /// **Ce n'est pas Φ_c.** C'est la grandeur d'entrée dont Φ_c est l'effet
    /// mesuré, et les deux ne s'affichent jamais dans le même champ : celle-ci
    /// est posée, celle-là se lit sur les décisions déposées (EX-A56). Le rapport
    /// entre les deux est ce que le scénario M mesure ; le supposer serait
    /// fabriquer la conclusion.
    pub fn part_structurelle(&self) -> f64 {
        let n = self.n();
        if n <= 1 {
            return 0.0;
        }
        1.0 - (f64::from(self.nb) - 1.0) / (f64::from(n) - 1.0)
    }

    /// Affichage de la structure, à côté de Φ_c et jamais à sa place (EX-V22).
    pub fn affichage(&self) -> String {
        let n = self.n();
        if self.nb == n {
            format!("{n} familles pour {n} agents — population décorrélée (défaut, hypothèse la plus favorable)")
        } else if self.nb <= 1 {
            format!("1 famille pour {n} agents — population conforme")
        } else {
            format!(
                "{} familles pour {n} agents — interpolation du produit, sans provenance dans le traité",
                self.nb
            )
        }
    }
}

/// Le tirage de décision d'une population, partagé à l'intérieur d'une famille.
///
/// **Le partage porte sur le tour de l'agent, non sur l'instant logique**, et ce
/// choix est le cœur de la transposition. Les cycles d'agents sont décalés d'un
/// tirage dans la période — sans quoi la population tomberait d'un bloc, et
/// DT13 du registre `docs/decisions.md` enregistre ce décalage comme une
/// correction imposée par la mesure en phase 4.
/// Deux agents ne partagent donc **jamais** une date. Ce qu'ils partagent est le
/// **rang de la décision dans leur boucle** : le fait mesuré par le traité est
/// que dix-huit agents sur trente ouvrent une branche du même nom, pas qu'ils
/// l'ouvrent à la même microseconde. Une clé par instant rendrait ce module
/// inerte dans les scénarios livrés, ce qui est pire qu'absent (PD6).
///
/// Contrat de déterminisme : le tirage vient du `Alea` **unique** et semé, et le
/// mémo ne fait que le rediffuser. Deux exécutions de même graine et de même
/// structure consomment le même nombre de tirages et rendent la même trace
/// (PD1, EX-C02). Le nombre de tirages consommés dépend de la structure — une
/// famille unique en consomme n fois moins qu'une famille par agent —, ce qui est
/// une différence de configuration et non de déterminisme.
#[derive(Debug, Clone)]
pub struct TirageDeDecision {
    familles: Familles,
    /// `(famille, décision, tour) -> valeur`.
    memo: BTreeMap<(u32, &'static str, u64), f64>,
    /// Tour le plus avancé rencontré. Sert uniquement à élaguer : le mémo d'un
    /// tour révolu ne peut plus servir, la boucle d'un agent ne revenant pas en
    /// arrière.
    tour_max: u64,
    partages: u64,
    tires: u64,
}

/// Tours de retard conservés au mémo avant élagage.
///
/// Deux : un agent en retard d'un tour sur le plus avancé de sa famille doit
/// encore pouvoir rediffuser. Au-delà, l'entrée ne servira plus, et la garder
/// ferait croître le mémo avec la durée de l'exécution.
const TOURS_CONSERVES: u64 = 2;

impl TirageDeDecision {
    /// Installe une structure de familles.
    pub fn nouveau(familles: Familles) -> TirageDeDecision {
        TirageDeDecision {
            familles,
            memo: BTreeMap::new(),
            tour_max: 0,
            partages: 0,
            tires: 0,
        }
    }

    /// La structure installée.
    pub fn familles(&self) -> &Familles {
        &self.familles
    }

    /// Tirage uniforme pour `decision` au `tour` de cet agent, partagé par les
    /// membres de sa famille qui atteignent le même tour.
    ///
    /// Le premier membre de la famille à atteindre ce tour consomme un tirage du
    /// générateur ; les suivants reçoivent le même nombre sans en consommer.
    pub fn uniforme(
        &mut self,
        agent: ActeurId,
        decision: &'static str,
        tour: u64,
        alea: &mut Alea,
    ) -> f64 {
        if tour > self.tour_max {
            self.tour_max = tour;
            let plancher = self.tour_max.saturating_sub(TOURS_CONSERVES);
            self.memo.retain(|(_, _, t), _| *t >= plancher);
        }
        let famille = self.familles.famille(agent);
        // Un agent hors bornes n'a pas de famille, il en a l'**absence**. La
        // mémoïser reviendrait à réunir tous les agents inexistants dans une
        // famille commune : deux d'entre eux recevraient le même tirage, alors
        // que `Familles::partagent` répond déjà que non. Une corrélation que le
        // curseur de familles ne pilote pas est exactement ce qu'EX-C19 interdit
        // de fabriquer.
        if famille == Familles::SANS_FAMILLE {
            self.tires += 1;
            return alea.uniforme();
        }
        let cle = (famille, decision, tour);
        if let Some(u) = self.memo.get(&cle) {
            self.partages += 1;
            return *u;
        }
        let u = alea.uniforme();
        self.tires += 1;
        self.memo.insert(cle, u);
        u
    }

    /// Nombre de fois qu'un tirage a été **rediffusé** au lieu d'être consommé.
    ///
    /// C'est la mesure directe de l'effet de la structure, et elle est nulle sur
    /// une population décorrélée. Elle ne remplace pas Φ_c : elle compte des
    /// tirages, pas des décisions égales.
    pub fn partages(&self) -> u64 {
        self.partages
    }

    /// Nombre de tirages effectivement consommés du générateur.
    pub fn tires(&self) -> u64 {
        self.tires
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn une_famille_par_agent_est_le_defaut_et_ne_partage_rien() {
        let f = Familles::une_par_agent(8);
        assert_eq!(f.diversite_effective(), 8);
        assert!(!f.partagent(ActeurId(0), ActeurId(1)));
        assert_eq!(f.part_structurelle(), 0.0);
        assert!(f.affichage().contains("décorrélée"));
    }

    #[test]
    fn la_famille_unique_fait_decider_toute_la_population_ensemble() {
        let f = Familles::unique(8);
        assert_eq!(f.diversite_effective(), 1);
        assert!(f.partagent(ActeurId(0), ActeurId(7)));
        assert_eq!(f.part_structurelle(), 1.0);
    }

    #[test]
    fn linterpolation_ne_declare_jamais_la_conformite_par_un_arrondi() {
        // À part < 1, il reste au moins deux familles : la population n'est
        // jamais dite conforme sans que le curseur soit au bout.
        for part in [0.5, 0.9, 0.99, 0.999] {
            let f = Familles::interpole(64, part);
            assert!(
                f.diversite_effective() >= 2,
                "part = {part} rend {} familles",
                f.diversite_effective()
            );
        }
        assert_eq!(Familles::interpole(64, 1.0).diversite_effective(), 1);
    }

    #[test]
    fn le_tirage_est_partage_dans_la_famille_et_pas_entre_familles() {
        let mut alea = Alea::nouveau(7);
        let mut t = TirageDeDecision::nouveau(Familles::interpole(4, 1.0));
        let tous: Vec<f64> = (0..4)
            .map(|a| t.uniforme(ActeurId(a), "choix", 10, &mut alea))
            .collect();
        assert!(
            tous.windows(2).all(|w| w[0] == w[1]),
            "même famille, même instant, même décision : {tous:?}"
        );
        assert_eq!(t.tires(), 1, "un seul tirage consommé pour quatre agents");
        assert_eq!(t.partages(), 3, "les trois suivants le rediffusent");

        let mut t2 = TirageDeDecision::nouveau(Familles::une_par_agent(4));
        let mut alea2 = Alea::nouveau(7);
        let c = t2.uniforme(ActeurId(0), "choix", 10, &mut alea2);
        let d = t2.uniforme(ActeurId(3), "choix", 10, &mut alea2);
        assert_ne!(c, d, "familles distinctes : aucun partage");
        assert_eq!(t2.partages(), 0);
    }

    #[test]
    fn le_memo_ne_franchit_pas_un_tour() {
        let mut alea = Alea::nouveau(1);
        let mut t = TirageDeDecision::nouveau(Familles::unique(2));
        let a = t.uniforme(ActeurId(0), "choix", 10, &mut alea);
        let b = t.uniforme(ActeurId(0), "choix", 11, &mut alea);
        assert_ne!(a, b, "deux tours, deux tirages");
        assert_eq!(t.tires(), 2);
    }

    #[test]
    fn un_agent_en_retard_dun_tour_partage_encore() {
        // Les cycles sont décalés : les membres d'une famille n'atteignent pas
        // le même tour au même instant. Sans cette tolérance, le partage ne
        // prendrait jamais dans les scénarios livrés.
        let mut alea = Alea::nouveau(4);
        let mut t = TirageDeDecision::nouveau(Familles::unique(3));
        let a = t.uniforme(ActeurId(0), "choix", 5, &mut alea);
        // L'agent 1 avance d'un tour avant que l'agent 2 n'atteigne le tour 5.
        t.uniforme(ActeurId(1), "choix", 6, &mut alea);
        let c = t.uniforme(ActeurId(2), "choix", 5, &mut alea);
        assert_eq!(a, c, "le retardataire rediffuse le tirage de son tour");
    }

    #[test]
    fn le_memo_ne_croit_pas_avec_la_duree_de_lexecution() {
        let mut alea = Alea::nouveau(6);
        let mut t = TirageDeDecision::nouveau(Familles::unique(4));
        for tour in 0..500u64 {
            for a in 0..4u32 {
                t.uniforme(ActeurId(a), "choix", tour, &mut alea);
            }
        }
        assert!(t.memo.len() <= 3, "mémo élagué : {} entrées", t.memo.len());
        assert_eq!(t.tires(), 500, "un tirage par tour, pour quatre agents");
    }

    /// EX-C19 — un agent hors bornes n'appartient à aucune famille, donc il ne
    /// partage avec personne. Le mémo était clé sur la sentinelle : deux agents
    /// inexistants recevaient le même tirage, ce que `partagent` niait déjà.
    #[test]
    fn deux_agents_hors_bornes_ne_partagent_pas_leur_tirage() {
        let f = Familles::une_par_agent(2);
        assert_eq!(f.famille(ActeurId(7)), Familles::SANS_FAMILLE);
        assert!(!f.partagent(ActeurId(7), ActeurId(8)));

        let mut alea = Alea::nouveau(21);
        let mut t = TirageDeDecision::nouveau(f);
        let a = t.uniforme(ActeurId(7), "choix", 3, &mut alea);
        let b = t.uniforme(ActeurId(8), "choix", 3, &mut alea);
        assert_ne!(a, b, "aucune famille, donc aucun partage");
        assert_eq!(t.partages(), 0);
        assert_eq!(t.tires(), 2);
    }

    /// La répartition par tranches reste exacte au-delà de 2¹⁶ agents : le
    /// produit `i × nb` déborde `u32`, et le profil release ne le signalerait
    /// pas.
    #[test]
    fn la_repartition_ne_deborde_pas_sur_une_grande_population() {
        let n = 100_000u32;
        let f = Familles::interpole(n, 0.5);
        let nb = f.diversite_effective();
        assert_eq!(nb, 50_000);
        assert_eq!(f.famille(ActeurId(0)), 0);
        assert_eq!(f.famille(ActeurId(n - 1)), nb - 1);
        // Croissance monotone : un enroulement replierait un agent tardif sur
        // une famille de tête.
        assert!((1..n).all(|i| f.famille(ActeurId(i)) >= f.famille(ActeurId(i - 1))));
    }

    #[test]
    fn deux_decisions_distinctes_ne_partagent_pas_leur_tirage() {
        let mut alea = Alea::nouveau(3);
        let mut t = TirageDeDecision::nouveau(Familles::unique(2));
        let a = t.uniforme(ActeurId(0), "choix", 5, &mut alea);
        let b = t.uniforme(ActeurId(0), "nom", 5, &mut alea);
        assert_ne!(a, b);
    }

    #[test]
    fn le_partage_ne_casse_pas_le_rejeu() {
        // PD1 : deux exécutions de même graine et même structure rendent la
        // même suite, partages compris.
        let suite = |graine: u64| {
            let mut alea = Alea::nouveau(graine);
            let mut t = TirageDeDecision::nouveau(Familles::interpole(6, 0.5));
            let mut v = Vec::new();
            for tour in 0..5u64 {
                for a in 0..6u32 {
                    v.push(t.uniforme(ActeurId(a), "choix", tour, &mut alea));
                }
            }
            (v, t.tires(), t.partages())
        };
        assert_eq!(suite(42), suite(42));
        assert_ne!(suite(42).0, suite(43).0);
    }
}
