//! Critère de sortie de la phase 3, tel qu'écrit au §9 du PRD.
//!
//! > Le scénario H produit une valeur **unanime et fausse** sur perte d'un seul
//! > PULL, l'oracle de conservation de masse l'attribue à la ligne 4 de
//! > l'échange en cause, et l'interface ne dit jamais « convergé ». Le scénario
//! > I remplit les tableaux 7, 11, 12 et 14 et les figures 4.2 et 5.1 par la
//! > mesure, colonnes « modèle de panne », « synchronisme » et « propriété
//! > abandonnée » comprises, les lignes non livrées restant en gris. La
//! > fraction résiduelle de susceptibles ne décroît pas quand le budget de
//! > simulation s'allonge. La case « accord » du seuil de quorum bascule sous
//! > partition.

use sim_agents::accord::{grille, Case, Mecanisme, MoyenneLocale, SeuilDeQuorum};
use sim_agents::agregation::{Ligne, Params, PushPull};
use sim_agents::echantillonnage::{Biais, ServiceDePairs};
use sim_agents::propagation::{FamilleCrdt, Rumeur};
use sim_core::alea::Alea;
use sim_core::temps::Instant;

/// **(1)** Le scénario H produit une valeur **unanime et fausse**, attribuée à
/// la **ligne 4**, et rien n'affiche « convergé ».
#[test]
fn critere_1_une_valeur_unanime_et_fausse_attribuee_a_la_ligne_4() {
    let params = Params {
        omission: 0.05,
        relance: None,
        biais: Biais::Uniforme,
        ..Params::default()
    };
    let mut p = PushPull::nouveau((0..64).map(|i| i as f64 * 1.5).collect(), params);
    let mut s = ServiceDePairs::nouveau(64, params.biais);
    let mut alea = Alea::nouveau(101);
    let dispersion_initiale = p.dispersion();

    for c in 0..400 {
        p.cycle(&mut s, &mut alea, Instant(c));
    }

    // Unanime : la dispersion s'est effondrée.
    assert!(
        p.dispersion() < dispersion_initiale / 100.0,
        "dispersion finale {}",
        p.dispersion()
    );
    // Fausse : la somme a quitté sa valeur, donc la valeur commune n'est la
    // moyenne de rien.
    assert!((p.somme() - p.somme_initiale).abs() > 1.0);

    // Attribuée à la ligne 4 de l'échange en cause.
    let premiere = p
        .ruptures
        .iter()
        .find(|r| r.ligne == Ligne::Ligne4PullPerdu)
        .expect("au moins une perte de PULL");
    assert!(premiere.ligne.libelle().contains("ligne 4"));
    let rapport = p.rapporter().unwrap();
    assert!(rapport.contains("ligne 4"), "{rapport}");

    // Et rien n'affiche « convergé ».
    let (_, etiquette) = p.critere_local_heuristique(1e-6);
    assert!(!etiquette.contains("convergé"), "{etiquette}");
    assert!(etiquette.contains("heuristique"), "{etiquette}");
    assert!(!rapport.contains("convergé"), "{rapport}");
}

/// **(2)** La grille du scénario I est remplie **par la mesure**, ses colonnes
/// de signature ne sont jamais vides, et les lignes non livrées restent en gris.
#[test]
fn critere_2_la_grille_est_remplie_par_la_mesure() {
    let mut alea = Alea::nouveau(102);
    let q = SeuilDeQuorum::nouveau(128, vec![0.9, 0.85], 0.10, 3, true, &mut alea).unwrap();
    let m = MoyenneLocale::nouvelle((0..64).map(|i| i as f64).collect());
    let g = grille(&q, &m, FamilleCrdt::Etat);

    // Colonnes « modèle de panne », « synchronisme » et « propriété
    // abandonnée » : jamais vides, sur aucune ligne.
    for l in &g {
        assert!(!l.modele_de_panne.is_empty());
        assert!(!l.synchronisme.is_empty());
        assert!(!l.propriete_abandonnee.is_empty());
    }

    // Les trois mécanismes livrés sont mesurés ; le consensus reste en gris
    // avec la valeur du traité (DT7).
    assert!(g[0].mesuree() && g[1].mesuree() && g[2].mesuree());
    assert!(!g[3].mesuree(), "le consensus n'est jamais mesuré");
    assert_eq!(g[3].accord, Case::NonLivree);
    assert!(g[3].valeur_du_traite.contains("repère cité"));

    // Chaque mécanisme déclare ce qu'il abandonne et l'oracle qui le mesure.
    for mecanisme in [
        Mecanisme::SeuilDeQuorum,
        Mecanisme::MoyenneAlignement,
        Mecanisme::FusionCrdt,
    ] {
        assert!(!mecanisme.propriete_abandonnee().is_empty());
        assert!(!mecanisme.oracle_arme().is_empty());
    }
}

/// **(3)** La fraction résiduelle de susceptibles **ne décroît pas** quand le
/// budget de simulation s'allonge. Une décroissance serait un défaut
/// d'implantation du retrait.
#[test]
fn critere_3_la_fraction_residuelle_ne_decroit_pas_avec_le_budget() {
    let mesurer = |tours: u32| {
        let mut r = Rumeur::nouvelle(4_000, Some(3));
        let mut s = ServiceDePairs::nouveau(4_000, Biais::Uniforme);
        let mut alea = Alea::nouveau(103);
        for _ in 0..tours {
            r.tour(&mut s, &mut alea);
        }
        r.fraction_residuelle()
    };
    let a = mesurer(60);
    let b = mesurer(240);
    let c = mesurer(960);
    assert!(a > 0.0, "la fraction résiduelle doit être non nulle");
    assert!(
        (b - a).abs() < 1e-12 && (c - b).abs() < 1e-12,
        "elle ne doit pas décroître : {a}, {b}, {c}"
    );
}

/// **(4)** La case « accord » du seuil de quorum **bascule sous partition** :
/// deux quorums locaux se forment de part et d'autre, et aucun agent ne le
/// détecte — seul l'oracle armé le compte.
/// La division n'est pas certaine à chaque exécution — les deux composantes
/// peuvent converger sur la même option par hasard. Ce que le scénario
/// établit, et qui suffit à faire tomber l'accord, c'est qu'elle est
/// **possible sous partition et impossible sans**. Un accord qui ne tient que
/// si le hasard coopère n'est pas un accord.
#[test]
fn critere_4_la_case_accord_bascule_sous_partition() {
    let executer = |graine: u64, partition: bool| {
        let mut alea = Alea::nouveau(graine);
        // Deux options de qualité égale : chaque composante choisit alors sans
        // qu'une préférence commune ne les réaligne.
        let mut q = SeuilDeQuorum::nouveau(256, vec![0.9, 0.9], 0.10, 3, true, &mut alea).unwrap();
        q.partition = partition;
        let mut s = ServiceDePairs::nouveau(256, Biais::Uniforme);
        for _ in 0..250 {
            q.tour(&mut s, &mut alea);
        }
        (q.case_accord(), q.engagements_incompatibles())
    };

    let divisions_avec = (0..12u64)
        .filter(|g| executer(*g, true).0 == Case::Abandonnee)
        .count();
    let divisions_sans = (0..12u64)
        .filter(|g| executer(*g, false).0 == Case::Abandonnee)
        .count();

    assert!(
        divisions_avec > 0,
        "sous partition, la décision divisée doit survenir au moins une fois sur douze"
    );
    assert_eq!(
        divisions_sans, 0,
        "sans partition, l'accord doit tenir à toutes les graines"
    );

    // Et quand elle survient, c'est bien l'oracle armé qui la compte — aucun
    // agent ne la détecte.
    let graine_divisee = (0..12u64)
        .find(|g| executer(*g, true).0 == Case::Abandonnee)
        .unwrap();
    assert!(executer(graine_divisee, true).1 > 0);
}
