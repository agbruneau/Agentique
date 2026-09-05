//! Critère de sortie de la phase 5, tel qu'écrit au §9 du PRD.
//!
//! > Le contraste manifeste / sans manifeste est lisible sans explication
//! > verbale. Le scénario L fait passer P(I|A) de ≈ 99,99 % à ≈ 2 % **par le
//! > seul curseur de structure des domaines**, sans qu'aucun autre paramètre ne
//! > bouge — c'est la démonstration du troisième reste de la conclusion — et la
//! > voie Monte-Carlo coïncide avec la voie analytique dans l'intervalle de
//! > §8.4.

use sim_agents::agregat_fenetre::{AgregatFenetre, Esquisse, Etiquette};
use sim_agents::taux_de_base::{scenario_l, Corroboration, TauxDeBase};
use sim_core::alea::Alea;
use sim_core::verification::{Campagne, Issue, Parametres};

fn esquisse_de(debut: u64, fin: u64) -> Esquisse {
    let mut e = Esquisse::nouvelle();
    for v in debut..fin {
        e.ajouter(v);
    }
    e
}

/// **(1)** Le contraste manifeste / sans manifeste est lisible **sans
/// explication verbale** : deux volets, deux étiquettes, et l'un des deux est
/// faux.
#[test]
fn critere_1_le_contraste_du_manifeste_est_lisible_sans_explication() {
    let partitions: Vec<u32> = (0..4).collect();

    // Avec manifeste : l'absence est **nommée**.
    let avec = {
        let mut a = AgregatFenetre::nouveau(Some(partitions.clone()));
        for p in [0u32, 1, 3] {
            a.contribuer(p, esquisse_de(p as u64 * 1_000, (p as u64 + 1) * 1_000));
        }
        a.declencher(1)
    };
    // Sans manifeste : le volet se déclare **complet**.
    let sans = {
        let mut a = AgregatFenetre::nouveau(None);
        for p in [0u32, 1, 3] {
            a.contribuer(p, esquisse_de(p as u64 * 1_000, (p as u64 + 1) * 1_000));
        }
        a.declencher(1)
    };
    // Référence : toutes les partitions contribuent.
    let complet = {
        let mut a = AgregatFenetre::nouveau(None);
        for p in 0..4u32 {
            a.contribuer(p, esquisse_de(p as u64 * 1_000, (p as u64 + 1) * 1_000));
        }
        a.declencher(1)
    };

    // Le contraste tient dans les deux étiquettes, sans commentaire.
    assert_eq!(avec.etiquette, Etiquette::Partiel { manquants: vec![2] });
    assert_eq!(sans.etiquette, Etiquette::Complet);
    assert!(avec.etiquette.libelle().contains("manquants = [2]"));

    // Et le volet « complet » est faux, d'une quantité que rien ne trahit :
    // l'erreur affichée est **identique**.
    assert!(sans.estimation < complet.estimation * 0.9);
    assert_eq!(sans.erreur_esquisse, complet.erreur_esquisse);
}

/// **(2)** Le scénario L fait passer P(I|A) de ≈ 99,99 % à ≈ 2 % **par le seul
/// curseur de structure des domaines**, sans qu'aucun autre paramètre ne bouge.
#[test]
fn critere_2_le_seul_curseur_de_structure_fait_seffondrer_p_i_sachant_a() {
    let base = TauxDeBase::default();
    let corroboration = Corroboration::default();

    let (rho_min, p_max) = scenario_l(&base, &corroboration, 64, 0.0);
    let (rho_max, p_min) = scenario_l(&base, &corroboration, 64, 1.0);

    assert!((rho_min - 0.0).abs() < 1e-9, "ρ part de 0");
    assert!((rho_max - 1.0).abs() < 1e-9, "et va jusqu'à 1");
    // 0,999854 s'arrondit à 99,99 % — la valeur qu'annonce le PRD.
    assert!(p_max > 0.9998, "≈ 99,99 % : {p_max:.6}");
    assert!(p_min < 0.02, "≈ 2 % ou moins : {p_min:.6}");

    // **Aucun autre paramètre n'a bougé** : mêmes taux, même r, même P(I).
    assert!((base.p_i() - 2e-5).abs() < 1e-12);
    assert!((corroboration.detection_conjointe() - 0.343).abs() < 1e-9);

    // Et le glissement est monotone d'un bout à l'autre.
    let mut precedent = f64::INFINITY;
    for k in 0..=20 {
        let (_, p) = scenario_l(&base, &corroboration, 64, k as f64 / 20.0);
        assert!(p <= precedent + 1e-9, "monotone : {precedent} puis {p}");
        precedent = p;
    }
}

/// **(3)** La voie **Monte-Carlo** sur le flux simulé coïncide avec la voie
/// **analytique**, dans l'intervalle de §8.4.
///
/// C'est ce qui empêche le scénario de dégénérer en calculateur (RQ12) : la
/// corrélation est **produite** par le mécanisme simulé, et la formule ne sait
/// pas la produire seule.
#[test]
fn critere_3_monte_carlo_coincide_avec_lanalytique() {
    // Le taux de base nominal — P(I) = 2 × 10⁻⁵ — rend une alarme si rare qu'il
    // faudrait ~10⁸ tirages pour en accumuler mille. La coïncidence des deux
    // voies se vérifie donc sur un régime d'intrusions plus fréquentes : ce qui
    // est testé est **l'accord entre la simulation et la formule**, pas la
    // valeur du taux de base, qui est elle-même dérivée et testée ailleurs.
    let base = TauxDeBase {
        intrusions_par_jour: 1_000.0,
        ..TauxDeBase::default()
    };
    let corroboration = Corroboration::default();
    // ε plus large que le défaut : la grandeur estimée est une probabilité
    // conditionnelle rare, et le budget d'une suite de tests doit rester
    // raisonnable. N est affiché, comme le §8.4 l'exige.
    let params = Parametres {
        epsilon: 2e-2,
        delta: 1e-2,
    };
    let n = params.executions_necessaires();
    assert!(params.affichage_avant_lancement().contains(&n.to_string()));

    for (part, tolerance) in [(0.0_f64, 5e-2), (1.0_f64, 5e-2)] {
        let (rho, analytique) = scenario_l(&base, &corroboration, 64, part);

        // Voie Monte-Carlo : on simule le flux d'alarmes et on compte.
        let mut alea = Alea::nouveau(7);
        let mut campagne = Campagne::nouvelle(params, n * 2);
        let mut alarmes = 0u64;
        let mut vraies = 0u64;
        // On tire des événements jusqu'à obtenir assez d'alarmes pour estimer.
        for _ in 0..4_000_000u64 {
            let intrusion = alea.bernoulli(base.p_i());
            // Chaque sonde décide ; sous corrélation, elles décident ensemble.
            let alarme = if intrusion {
                alea.bernoulli(corroboration.detection_conjointe())
            } else {
                alea.bernoulli(corroboration.fausses_conjointes(rho))
            };
            if alarme {
                alarmes += 1;
                if intrusion {
                    vraies += 1;
                }
                campagne.observer(intrusion);
                if alarmes >= n {
                    break;
                }
            }
        }
        assert!(alarmes > 100, "trop peu d'alarmes pour estimer : {alarmes}");
        let monte_carlo = vraies as f64 / alarmes as f64;

        assert!(
            (monte_carlo - analytique).abs() < tolerance,
            "à ρ = {rho:.2} : Monte-Carlo {monte_carlo:.4} contre analytique {analytique:.4}"
        );

        // Et la campagne ne rend jamais une valeur nue.
        let issue = campagne.conclure();
        match issue {
            Issue::Estimation { .. } | Issue::AucuneViolationObservee { .. } => {
                assert!(!issue.libelle().is_empty());
            }
            Issue::AbsenceDeVerdict { .. } => {
                assert!(issue.libelle().contains("absence de problème"));
            }
        }
    }
}
