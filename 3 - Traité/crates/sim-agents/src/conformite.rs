//! **Φ_c**, la conformité empirique d'une population (EX-A56, §8.1 du traité).
//!
//! > la conformité empirique Φ_c d'une population sur une décision d : la
//! > probabilité que deux agents tirés au hasard produisent la même valeur,
//! > moins la valeur qu'aurait cette probabilité si les décisions étaient
//! > indépendantes de même loi marginale. (§8.1 du traité)
//!
//! Φ_c vaut 0 pour des tirages indépendants et 1 pour une population qui décide
//! comme un seul agent.
//!
//! **Provenance.** C'est une **proposition de l'ouvrage**, mesurée par aucune
//! source : le traité l'écrit lui-même. Elle ne figure donc jamais parmi les
//! chiffres du traité à retrouver (NF-15), et son affichage porte l'étiquette des
//! grandeurs dérivées (F2).
//!
//! **Il n'y a pas de seuil.** Le §8.1 du traité dit n'en avoir aucune mesure et juger
//! probable qu'il n'y en ait pas un seul. Rien ici ne rend un booléen
//! « conforme », aucune zone n'est colorée, et [`SEUIL`] est une constante de
//! module qui rend le libellé plutôt qu'un nombre (PD5).
//!
//! **Coût** : une lecture du sujet où les décisions sont déposées, et **aucun
//! message supplémentaire** — les décisions y sont déjà écrites. C'est ce qui
//! distingue Φ_c de l'estimateur que le troisième reste de la conclusion déclare
//! introuvable : il ne demande aucune vue globale.

use sim_milieu::journal::Enregistrement;
use std::collections::BTreeMap;

/// Refus opposé à qui demande Φ_c sur plusieurs partitions (DT14).
pub const REFUS_MULTIPARTITION: &str =
    "Φ_c se mesure sur une partition unique : comparer deux décisions déposées sur deux \
     partitions suppose une relation d'ordre que M2 ne fournit pas (EX-A56, DT14)";

/// Ce qui est affiché à la place d'un seuil, et qui n'est pas une valeur (PD5).
pub const SEUIL: &str =
    "seuil inconnu — le traité n'en a aucune mesure et juge probable qu'il n'y en ait pas un \
     seul, la conformité pouvant être ruineuse pour un mécanisme et sans effet sur un autre";

/// **Constat de mesure : Φ_c ne distingue pas la conformité de la coordination.**
///
/// NF-15 impose de consigner l'écart à l'endroit où il se constate, et celui-ci
/// contredit ce que le PRD écrivait avant la mesure.
///
/// Ce que le PRD annonçait : le curseur de familles (EX-C19) devait faire passer
/// Φ_c de ≈ 0 à ≈ 1 sans qu'aucun paramètre de mécanisme ne bouge, et c'était le
/// critère de sortie de la phase 6.
///
/// Ce que la mesure donne, sur le scénario B à n = 24, m = 6, graine 7
/// (`cargo run -p sim-agents --example diagnostic_conformite --release`) :
///
/// | part de conformité | 0 | 0,25 | 0,5 | 0,75 | 1 |
/// |---|---|---|---|---|---|
/// | Φ_c | 0,173 | 0,180 | 0,181 | 0,228 | 0,186 |
///
/// Précision ± 0,003 sur ≈ 10⁵ paires. Trois faits, et aucun n'était prévu.
///
/// 1. **Φ_c vaut déjà 0,17 à conformité nulle**, avec un tirage par agent. La
///    cause n'est pas un défaut de l'estimateur : les agents lisent tous la même
///    trace, donc leurs décisions **sont** corrélées. C'est la thèse de l'ouvrage
///    — la coordination par le milieu — mesurée par la grandeur que le ch. 8
///    propose pour mesurer autre chose.
/// 2. **Le curseur ne déplace Φ_c que de 0,055**, de 0,173 à 0,228, soit
///    dix-huit fois sa précision et un dix-huitième de l'amplitude annoncée.
///    L'amplitude est prise max − min sur le curseur, qui est ce que calcule
///    `le_curseur_controle_le_partage_des_tirages_et_non_lamplitude_de_phi_c`.
///    La conformité du tirage est un contributeur **minoritaire** devant celle
///    du milieu.
/// 3. **La relation n'est pas monotone** : 0,75 rend plus que 1,0. Partager un
///    uniforme entre agents dont les vues de φ diffèrent ne force pas le même
///    choix — `Alea::pondere_avec` appliqué à des poids différents rend des
///    indices différents.
///
/// Conséquence pour l'ouvrage, et elle porte : Φ_c mesure la corrélation des
/// décisions, sans distinguer celle qui vient de la **fonction de décision** de
/// celle qui vient du **milieu partagé**. Sur un essaim stigmergique, les deux
/// coexistent et la seconde domine. Le §8.1 du traité propose Φ_c comme paramètre d'ordre
/// de la conformité d'une population ; ce qu'il mesure ici est la somme des deux,
/// et rien dans la grandeur ne les sépare.
///
/// Conséquence pour le produit : le critère de sortie de la phase 6 est **à
/// refaire sur la mesure**, comme DT1 et NF-05 l'ont été. Ce que le scénario M
/// établit n'est pas un passage de 0 à 1, c'est que **l'hypothèse d'indépendance
/// des sept énoncés du tableau 21 est déjà violée dans le code livré**, à curseur
/// au repos — ce qui est plus fort que ce que le PRD annonçait, et moins
/// spectaculaire.
pub const CONSTAT_DE_MESURE: &str =
    "constat de mesure (NF-15) — Φ_c ne distingue pas la conformité de la coordination : il vaut \
     déjà ≈ 0,17 à curseur au repos, parce que les agents lisent tous la même trace, et le \
     curseur de familles ne le déplace que de ≈ 0,055, soit un dix-huitième de l'amplitude \
     annoncée. La grandeur mesure la somme de la corrélation due à la fonction de décision et \
     de celle due au milieu partagé, sans les séparer. Le critère de sortie de la phase 6 est \
     à refaire sur la mesure.";

/// Estimation de Φ_c sur un jeu de décisions déposées.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Conformite {
    /// Valeur estimée, dans [−1, 1] par construction.
    ///
    /// **Le signe est rendu tel quel.** Une valeur négative n'est pas une erreur
    /// d'estimation : c'est une population qui s'accorde **moins** que le hasard,
    /// donc anti-conforme, et l'écraser à zéro la rendrait indiscernable d'une
    /// population indépendante. C'est ce que faisait un `clamp(0, 1)` posé ici, et
    /// il rendait vrai par construction le test censé montrer qu'une population
    /// décorrélée vaut zéro — dont le jeu de données valait en réalité −0,2.
    pub phi_c: f64,
    /// Probabilité observée que deux agents distincts s'accordent.
    pub accord_observe: f64,
    /// Ce que cette probabilité vaudrait sous indépendance, à loi marginale
    /// égale : Σ p_v². C'est le terme que Φ_c retranche, et l'afficher évite de
    /// lire une conformité là où il n'y a qu'un espace de décision étroit.
    pub accord_sous_independance: f64,
    /// Paires observées, k. La précision suit celle de toute proportion, en
    /// 1/√k.
    pub paires: u64,
    /// Nombre d'agents distincts ayant déposé une décision.
    pub agents: u32,
}

impl Conformite {
    /// Demi-largeur de l'intervalle, en 1/√k. `None` quand aucune paire n'a été
    /// observée — une valeur sans précision serait un nombre sans provenance.
    pub fn precision(&self) -> Option<f64> {
        if self.paires == 0 {
            return None;
        }
        Some(1.0 / (self.paires as f64).sqrt())
    }

    /// Φ_c dépasse-t-il la précision de son estimation ?
    ///
    /// C'est la seule question à laquelle ce module répond par un booléen, et ce
    /// n'est **pas** un seuil de conformité : c'est le point où la mesure cesse
    /// d'être indistinguable de zéro.
    ///
    /// **Ce n'est plus la question d'EX-A58, et c'est le résultat de la
    /// phase 6.** L'effacement d'une borne suit le **réglage** — la structure des
    /// familles, qui viole démontrablement l'indépendance des tirages —, jamais
    /// Φ_c mesuré, qui ne sépare pas la conformité de la coordination
    /// (`CONSTAT_DE_MESURE`). Effacer sur cette base afficherait comme une preuve
    /// une fausse alarme que PD12 interdit. Le chemin de l'effacement est
    /// [`crate::dettes::verdicts`], qui prend une `&Familles`.
    pub fn depasse_sa_precision(&self) -> bool {
        match self.precision() {
            Some(e) => self.phi_c > e,
            None => false,
        }
    }

    /// Libellé complet, précision et absence de seuil comprises (EX-V22).
    pub fn affichage(&self) -> String {
        match self.precision() {
            Some(e) => format!(
                "Φ_c = {:.4} ± {:.4} sur {} paires ({} agents) — accord observé {:.4}, \
                 attendu sous indépendance {:.4} — {}",
                self.phi_c, e, self.paires, self.agents, self.accord_observe,
                self.accord_sous_independance, SEUIL
            ),
            None => "Φ_c — jamais observé : aucune paire de décisions déposées".to_string(),
        }
    }
}

/// Estime Φ_c sur les décisions lues dans **une** partition.
///
/// **Pourquoi l'estimation aligne les décisions par rang, et non par date.** Une
/// seule décision par agent ne suffit pas : la loi marginale devrait alors être
/// estimée sur la même coupe transversale que l'accord observé, et les deux
/// termes seraient **identiquement égaux** — Φ_c vaudrait 0 quelle que soit la
/// population. C'était le premier estimateur écrit ici, et il était nul par
/// construction ; le test `la_conformite_se_lit_sur_un_espace_de_decision_large`
/// est ce qui l'a montré.
///
/// La loi marginale d'un agent s'estime donc sur **sa propre suite** de décisions,
/// et l'accord s'observe entre agents **au même rang** de leurs suites. C'est le
/// pendant exact du partage d'EX-C19, qui porte sur le tour et non sur l'instant :
/// les cycles étant décalés, aucun agent ne décide à la même date qu'un autre.
///
/// Rend `Err(REFUS_MULTIPARTITION)` si les enregistrements viennent de plusieurs
/// partitions (DT14) — refus, pas approximation.
pub fn estimer(decisions: &[Enregistrement]) -> Result<Conformite, &'static str> {
    let mut partitions = decisions.iter().map(|e| e.partition);
    if let Some(p0) = partitions.next() {
        if partitions.any(|p| p != p0) {
            return Err(REFUS_MULTIPARTITION);
        }
    }

    // Suite de décisions par agent, dans l'ordre de la partition (M1). L'auteur
    // vient du champ apposé par le milieu (EX-M24) : une conformité calculée sur
    // un auteur déclaré par l'écrivain mesurerait ce que les agents *disent*
    // avoir décidé.
    let mut suites: BTreeMap<u32, Vec<u64>> = BTreeMap::new();
    let mut ordonne: Vec<&Enregistrement> = decisions.iter().collect();
    ordonne.sort_by_key(|e| e.decalage);
    for e in ordonne {
        // La clé de regroupement est la représentation binaire de la valeur :
        // exacte, sans tolérance. Deux agents qui « décident la même chose »
        // décident le même bit à bit — sinon c'est une décision voisine, et non
        // la même.
        suites.entry(e.auteur.agent.0).or_default().push(e.valeur.to_bits());
    }
    let agents: Vec<&Vec<u64>> = suites.values().collect();
    let nb_agents = agents.len();

    // Rangs communs à toutes les suites : au-delà, l'accord porterait sur des
    // agents dont l'un n'a pas encore décidé, ce qui n'est pas un désaccord.
    let rangs = agents.iter().map(|s| s.len()).min().unwrap_or(0);
    if nb_agents < 2 || rangs == 0 {
        return Ok(Conformite {
            phi_c: 0.0,
            accord_observe: 0.0,
            accord_sous_independance: 0.0,
            paires: 0,
            agents: nb_agents as u32,
        });
    }

    // Lois marginales, une par agent, sur sa propre suite.
    let marginales: Vec<BTreeMap<u64, f64>> = agents
        .iter()
        .map(|s| {
            let mut m: BTreeMap<u64, f64> = BTreeMap::new();
            for v in s.iter() {
                *m.entry(*v).or_insert(0.0) += 1.0;
            }
            let total = s.len() as f64;
            for p in m.values_mut() {
                *p /= total;
            }
            m
        })
        .collect();

    let mut accords = 0u64;
    let mut paires = 0u64;
    let mut somme_independance = 0.0;
    let mut nb_paires_agents = 0u64;
    for i in 0..nb_agents {
        for j in (i + 1)..nb_agents {
            let accords_de_la_paire = agents[i][..rangs]
                .iter()
                .zip(&agents[j][..rangs])
                .filter(|(a, b)| a == b)
                .count() as u64;
            paires += rangs as u64;
            accords += accords_de_la_paire;
            // Σ_v p_i(v) · p_j(v) : l'accord qu'aurait cette paire si chacun
            // tirait dans sa propre loi, indépendamment de l'autre.
            somme_independance += marginales[i]
                .iter()
                .map(|(v, pi)| pi * marginales[j].get(v).copied().unwrap_or(0.0))
                .sum::<f64>();
            nb_paires_agents += 1;
        }
    }

    let accord_observe = accords as f64 / paires as f64;
    let sous_independance = somme_independance / nb_paires_agents as f64;

    Ok(Conformite {
        phi_c: accord_observe - sous_independance,
        accord_observe,
        accord_sous_independance: sous_independance,
        paires,
        agents: nb_agents as u32,
    })
}

#[cfg(test)]
mod tests {
    use super::*;
    use sim_core::temps::Instant;
    use sim_core::ActeurId;
    use sim_milieu::journal::Identite;

    /// Une population dont chaque agent dépose la suite `valeurs[agent]`, dans
    /// l'ordre des rangs. Les décalages sont attribués rang par rang, comme le
    /// ferait un journal où les agents déposent à tour de rôle.
    fn journal(valeurs: &[Vec<f64>]) -> Vec<Enregistrement> {
        let rangs = valeurs.iter().map(Vec::len).max().unwrap_or(0);
        let mut out = Vec::new();
        let mut decalage = 0u64;
        for r in 0..rangs {
            for (a, suite) in valeurs.iter().enumerate() {
                if let Some(v) = suite.get(r) {
                    out.push(Enregistrement {
                        partition: 0,
                        decalage,
                        cle: 0,
                        valeur: *v,
                        octets: 32,
                        date_evenement: Instant(r as u64),
                        durable: true,
                        auteur: Identite::propre(ActeurId(a as u32)),
                    });
                    decalage += 1;
                }
            }
        }
        out
    }

    /// n agents décidant tous la même chose à chaque rang, la valeur variant
    /// d'un rang à l'autre : c'est la conformité au sens du traité.
    fn conforme(n: usize, rangs: usize) -> Vec<Vec<f64>> {
        (0..n)
            .map(|_| (0..rangs).map(|r| (r % 5) as f64).collect())
            .collect()
    }

    #[test]
    fn une_population_conforme_approche_un() {
        let c = estimer(&journal(&conforme(10, 20))).unwrap();
        assert_eq!(c.accord_observe, 1.0, "tous décident la même chose à chaque rang");
        // Sous indépendance, chacun tirant dans sa propre loi uniforme sur cinq
        // valeurs, l'accord vaudrait 1/5.
        assert!((c.accord_sous_independance - 0.2).abs() < 1e-9);
        assert!((c.phi_c - 0.8).abs() < 1e-9, "Φ_c = {}", c.phi_c);
        assert!(c.depasse_sa_precision());
    }

    /// Une population qui ne s'accorde **jamais** n'est pas décorrélée, elle est
    /// anti-conforme, et Φ_c doit le dire par son signe.
    ///
    /// Chaque agent parcourt les cinq valeurs dans un ordre décalé du sien :
    /// mêmes lois marginales, et un accord de rang systématiquement nul, ce que
    /// cinq tirages indépendants ne produiraient qu'avec une probabilité de
    /// 5⁻¹⁰⁰. Sous indépendance l'accord vaudrait 1/5 ; il vaut 0, donc
    /// Φ_c = −0,2. C'est cette valeur-là que le `clamp(0, 1)` retiré rendait
    /// indiscernable de zéro.
    #[test]
    fn une_population_qui_ne_saccorde_jamais_rend_un_phi_c_negatif() {
        let n = 5;
        let v: Vec<Vec<f64>> = (0..n)
            .map(|a| (0..20).map(|r| ((r + a) % 5) as f64).collect())
            .collect();
        let c = estimer(&journal(&v)).unwrap();
        assert_eq!(c.accord_observe, 0.0);
        assert!((c.accord_sous_independance - 0.2).abs() < 1e-9);
        assert!((c.phi_c + 0.2).abs() < 1e-9, "Φ_c = {}", c.phi_c);
        assert!(!c.depasse_sa_precision());
    }

    /// Une population réellement **décorrélée** — chaque agent tire dans la même
    /// loi, indépendamment des autres — rend un Φ_c indiscernable de zéro, à la
    /// précision de l'estimation près.
    ///
    /// C'est le cas que le test précédent ne couvrait pas, et le seul qui fixe le
    /// zéro de l'échelle : sans lui, rien n'établit que Φ_c mesure autre chose
    /// que « les suites diffèrent ».
    #[test]
    fn une_population_reellement_decorrelee_reste_dans_sa_precision() {
        let mut alea = sim_core::alea::Alea::nouveau(4);
        let v: Vec<Vec<f64>> = (0..12)
            .map(|_| (0..400).map(|_| (alea.uniforme() * 5.0).floor()).collect())
            .collect();
        let c = estimer(&journal(&v)).unwrap();
        assert!(
            c.phi_c.abs() <= c.precision().unwrap(),
            "Φ_c = {} pour une précision de {}",
            c.phi_c,
            c.precision().unwrap()
        );
        assert!(!c.depasse_sa_precision());
    }

    #[test]
    fn un_espace_de_decision_a_une_seule_valeur_nest_pas_de_la_conformite() {
        // C'est le piège que la soustraction évite : tous décident pareil, mais
        // il n'y avait rien d'autre à décider.
        let v: Vec<Vec<f64>> = (0..8).map(|_| vec![7.0; 15]).collect();
        let c = estimer(&journal(&v)).unwrap();
        assert_eq!(c.accord_observe, 1.0);
        assert_eq!(c.accord_sous_independance, 1.0);
        assert_eq!(c.phi_c, 0.0);
    }

    #[test]
    fn la_conformite_partielle_se_lit_entre_les_deux() {
        // Six agents conformes, quatre décorrélés.
        let mut v = conforme(6, 20);
        for a in 0..4 {
            v.push((0..20).map(|r| ((r + a + 1) % 5) as f64).collect());
        }
        let c = estimer(&journal(&v)).unwrap();
        assert!(c.phi_c > 0.0 && c.phi_c < 0.8, "Φ_c = {}", c.phi_c);
    }

    #[test]
    fn le_multipartition_est_refuse_et_non_approxime() {
        let mut d = journal(&conforme(2, 4));
        d[1].partition = 1;
        let e = estimer(&d).expect_err("M2 ne fournit aucun ordre entre partitions");
        assert!(e.contains("M2"));
    }

    #[test]
    fn la_precision_suit_la_racine_du_nombre_de_paires() {
        let c = estimer(&journal(&conforme(4, 10))).unwrap();
        // Six paires d'agents, dix rangs.
        assert_eq!(c.paires, 60);
        let e = c.precision().unwrap();
        assert!((e - 1.0 / 60.0f64.sqrt()).abs() < 1e-12);
    }

    #[test]
    fn moins_de_deux_agents_ne_donne_aucune_paire_et_aucun_seuil() {
        let c = estimer(&journal(&[vec![1.0, 2.0]])).unwrap();
        assert_eq!(c.paires, 0);
        assert_eq!(c.precision(), None);
        assert!(c.affichage().contains("jamais observé"));
        assert!(!c.depasse_sa_precision());
    }

    #[test]
    fn seuls_les_rangs_communs_a_tous_sont_compares() {
        // L'agent 1 n'a décidé qu'une fois : le rang 2 de l'agent 0 n'a pas de
        // vis-à-vis, et son absence n'est pas un désaccord.
        let d = journal(&[vec![1.0, 1.0, 1.0], vec![1.0]]);
        let c = estimer(&d).unwrap();
        assert_eq!(c.paires, 1, "un seul rang commun");
        assert_eq!(c.accord_observe, 1.0);
    }

    #[test]
    fn laffichage_ne_contient_jamais_de_verdict_de_conformite() {
        let a = estimer(&journal(&conforme(8, 12))).unwrap().affichage();
        assert!(a.contains("seuil inconnu"));
        for mot in ["conforme", "élevé", "faible", "critique"] {
            assert!(!a.contains(mot), "l'affichage porte un jugement : « {mot} »");
        }
    }
}
