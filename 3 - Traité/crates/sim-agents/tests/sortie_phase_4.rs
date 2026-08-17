//! Critère de sortie de la phase 4, tel qu'écrit au §9 du PRD.
//!
//! > Le tableau 15 se remplit par la mesure. Le scénario J reproduit la cascade
//! > en **trois générations** sans qu'aucun agent ne soit tombé, la bascule
//! > « décalage seulement » la supprime à charge inchangée, S1w tient sous faux
//! > soupçon avec arbitrage d'époque et tombe à l'instant exact du retour de
//! > l'agent soupçonné sans lui, et la durée de double détention est affichée
//! > sans jamais être présentée comme S1. Le scénario K affiche, pour chaque
//! > levier, la durée pendant laquelle l'invariant peut être faux — et affiche
//! > « non bornée » là où le traité l'écrit, jamais une moyenne plausible.

use sim_agents::allocation::{tableau_15, Mecanisme};
use sim_agents::cascade::{Cascade, Params, SondeVivacite};
use sim_agents::gouvernance::Levier;
use sim_agents::soupcon::{ArbitrageDepoque, Reconfiguration};
use sim_core::alea::Alea;
use sim_core::temps::{Duree, Instant};
use sim_core::ActeurId;

fn derouler(params: Params, pas: u32) -> Cascade {
    let mut c = Cascade::nouvelle(params);
    let mut alea = Alea::nouveau(1);
    for _ in 0..pas {
        c.pas(&mut alea);
    }
    c
}

/// **(1)** Le tableau 15 se remplit **par la mesure**, avec les repères du
/// traité en regard.
#[test]
fn critere_1_le_tableau_15_se_remplit_par_la_mesure() {
    let t = tableau_15(64, 0.9, 0.01, &mut Alea::nouveau(1));
    assert_eq!(t.len(), 6, "les six mécanismes d'EX-A05");
    for l in &t {
        assert!(!l.repere_du_traite.is_empty(), "{:?}", l.mecanisme);
        assert!(!l.condition_darret.is_empty());
    }
    // Le sixième mécanisme coûte zéro et n'a aucune condition d'arrêt.
    let stochastique = t
        .iter()
        .find(|l| l.mecanisme == Mecanisme::PolitiqueStochastique)
        .unwrap();
    assert_eq!((stochastique.messages, stochastique.tours), (0, 0));
    assert!(stochastique.condition_darret.contains("AUCUNE"));
}

/// **(2)** La cascade est complète en **trois générations** sans qu'aucun agent
/// ne soit tombé.
///
/// **`pannes_reelles == 0` ne peut pas échouer**, et `cascade::Cascade` le dit
/// dans sa propre documentation : aucun code n'incrémente ce compteur, la cascade
/// n'injectant aucune faute. Ce qui se mesure ici est le contraste — des
/// redémarrages et des générations avec ce compteur à zéro —, et le critère (3)
/// le complète en montrant qu'un seul réglage les supprime à charge inchangée.
#[test]
fn critere_2_la_cascade_en_trois_generations_sans_aucune_panne() {
    let c = derouler(Params::default(), 60);
    assert!(c.generations >= 3, "{} générations", c.generations);
    assert_eq!(c.pannes_reelles, 0, "aucun agent n'est tombé");
    assert!(c.redemarrages > 0);
    assert!(c.bandeau().contains("pannes réelles : 0"));
}

/// **(3)** La bascule « décalage seulement » supprime la cascade **à charge
/// inchangée**.
#[test]
fn critere_3_le_decalage_seulement_supprime_la_cascade() {
    let avec = derouler(Params::default(), 60);
    let sans = derouler(Params::decalage_seulement(), 60);
    assert_eq!(avec.params.charge_par_s, sans.params.charge_par_s);
    assert_eq!(sans.params.sonde, SondeVivacite::DecalageSeulement);
    assert!(avec.redemarrages > 0);
    assert_eq!(sans.redemarrages, 0);
}

/// **(4)** S1w tient sous faux soupçon avec arbitrage d'époque, tombe à
/// l'instant exact du retour sans lui, et la durée de double détention est
/// affichée **sans jamais être présentée comme S1**.
#[test]
fn critere_4_s1w_tient_et_s1_ne_tient_pas() {
    let m = ActeurId(1);

    // Avec arbitrage : S1w tient.
    let mut avec = Reconfiguration::nouvelle(4, ArbitrageDepoque::LeMilieuArbitre);
    avec.reconfigurer(0, m, Instant(0));
    let epoque_de_m = avec.epoque(0);
    avec.reconfigurer(0, ActeurId(2), Instant(100));
    assert!(!avec.ecrire(0, m, epoque_de_m, Instant(300)));
    assert!(avec.s1w_tient());

    // Sans arbitrage : S1w tombe **exactement** au retour de m, pas avant.
    let mut sans = Reconfiguration::nouvelle(4, ArbitrageDepoque::LeMilieuNarbitrePas);
    sans.reconfigurer(0, m, Instant(0));
    let e = sans.epoque(0);
    sans.reconfigurer(0, ActeurId(2), Instant(100));
    assert!(sans.s1w_tient(), "rien avant le retour");
    assert!(sans.ecrire(0, m, e, Instant(300)));
    assert!(!sans.s1w_tient(), "et elle tombe à l'instant du retour");

    // La durée de double détention est affichée, et **jamais** comme S1.
    let affichage = avec.affichage_s1(true);
    let ligne_s1 = affichage.iter().find(|(k, _)| k.starts_with("S1 (")).unwrap();
    assert!(ligne_s1.1.contains("non rétabli"));
    assert!(ligne_s1.1.contains("non bornée en asynchrone"));
    assert!(!affichage.iter().any(|(_, v)| v.contains("S1 tient")));
}

/// **(5)** Le scénario K affiche, pour chaque levier, la durée pendant laquelle
/// l'invariant peut être faux — et **« non bornée »** là où le traité l'écrit,
/// jamais une moyenne plausible.
#[test]
fn critere_5_chaque_levier_affiche_sa_fenetre_de_violation() {
    let leviers = [
        Levier::ClassesDeCriticite,
        Levier::QuotaSurengage,
        Levier::BudgetDeReprise,
        Levier::EtranglementAdaptatif,
        Levier::BudgetDePerturbation,
        Levier::DimensionnementAutomatique,
    ];

    // Chaque levier dit ce qu'il ne borne pas.
    for l in leviers {
        assert!(!l.ne_borne_pas().is_empty(), "{}", l.nom());
    }

    // En asynchrone, toutes les fenêtres sont non bornées, sans exception et
    // sans valeur chiffrée.
    for l in leviers {
        let a = l.affichage_fenetre(true, Duree(120));
        assert_eq!(a, "**non bornée**", "{}", l.nom());
    }

    // Sous synchronisme partiel, celles qui restent non bornées le disent
    // toujours — jamais une moyenne plausible.
    let non_bornes = [
        Levier::ClassesDeCriticite,
        Levier::QuotaSurengage,
        Levier::BudgetDePerturbation,
        Levier::DimensionnementAutomatique,
    ];
    for l in non_bornes {
        assert_eq!(
            l.affichage_fenetre(false, Duree(120)),
            "**non bornée**",
            "{}",
            l.nom()
        );
    }
    assert!(Levier::EtranglementAdaptatif
        .affichage_fenetre(false, Duree(120))
        .contains("120"));
}
