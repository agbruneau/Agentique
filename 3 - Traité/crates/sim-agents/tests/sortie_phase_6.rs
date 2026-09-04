//! Critère de sortie de la phase 6 — **Le second axe**.
//!
//! Le §9 du PRD écrivait ce critère avant la mesure :
//!
//! > Φ_c mesuré passe de ≈ 0 à ≈ 1 par le seul curseur de structure des
//! > familles, sans qu'aucun paramètre de mécanisme ne bouge. Les quatre bornes
//! > que le produit sait mesurer s'effacent — plancher d'exploration, redondance
//! > k, avantage de d = 2, corroboration r parmi n — et aucun oracle de sûreté
//! > armé ne se déclenche pendant cet effacement.
//!
//! **La première phrase est contredite par la mesure**, et ces tests énoncent ce
//! qui est vrai. Φ_c vaut déjà ≈ 0,17 à curseur au repos, parce que les agents
//! lisent tous la même trace ; le curseur ne le déplace que de ≈ 0,055 — de 0,173
//! à 0,228 —, et pas monotonement. Le constat est consigné dans
//! [`sim_agents::conformite::CONSTAT_DE_MESURE`], conformément à NF-15 — un écart
//! est un défaut du simulateur **ou** une erreur de ce qui l'annonçait, et les
//! deux se consignent.
//!
//! Ce que la phase 6 établit est donc plus fort et moins spectaculaire que ce
//! qu'elle annonçait : **l'hypothèse d'indépendance des sept énoncés du tableau
//! 21 est déjà violée dans le code livré**, et rien avant EX-A58 ne le disait.

use sim_agents::arbitrage::{FileDarbitrage, Motif};
use sim_agents::conformite;
use sim_agents::deliberation::{DepotAveugle, FaitPrive, Mode};
use sim_agents::dettes::{self, EtatDeBorne};
use sim_agents::scenario_m::scenario_m;
use sim_agents::stigmergie::Params;
use sim_core::famille::{Familles, TirageDeDecision};
use sim_core::temps::{Duree, Instant};
use sim_core::{alea::Alea, ActeurId};
use sim_milieu::historique::{Historique, Issue};
use sim_milieu::journal::Identite;
use sim_milieu::quota::{Politique, Quotas, Verdict};

fn params() -> Params {
    let mut p = Params::scenario_b();
    p.n = 24;
    p.m = 6;
    p.p = 1;
    p.intervalle_lecture = 128;
    p
}

/// **Point 1 du critère, reformulé sur la mesure.** Le curseur contrôle le
/// partage des tirages, de façon monotone et vérifiable ; il ne contrôle pas Φ_c
/// de 0 à 1, et le critère d'origine était faux.
#[test]
fn le_curseur_controle_le_partage_des_tirages_et_non_lamplitude_de_phi_c() {
    let mesures: Vec<(f64, u64, f64)> = [0.0, 0.25, 0.5, 0.75, 1.0]
        .iter()
        .map(|part| {
            let r = scenario_m(params(), *part, 7, 20_000).expect("scénario M");
            (*part, r.tirages_partages, r.conformite.phi_c)
        })
        .collect();

    // Ce qui est monotone : le partage.
    assert!(
        mesures.windows(2).all(|w| w[0].1 <= w[1].1),
        "partages non croissants : {mesures:?}"
    );
    assert_eq!(mesures[0].1, 0, "aucun partage à curseur au repos");

    // Ce qui ne l'est pas : Φ_c. L'amplitude reste très inférieure à ce que le
    // PRD annonçait, et ce test fixe le constat pour qu'un changement soit un
    // événement plutôt qu'un glissement silencieux.
    let phi: Vec<f64> = mesures.iter().map(|m| m.2).collect();
    let amplitude =
        phi.iter().cloned().fold(f64::MIN, f64::max) - phi.iter().cloned().fold(f64::MAX, f64::min);
    assert!(
        amplitude < 0.2,
        "l'amplitude de Φ_c sous le curseur vaut {amplitude:.3} : le constat de mesure a changé"
    );
    assert!(
        phi[0] > 0.10,
        "Φ_c = {:.3} à curseur au repos : le constat de mesure a changé",
        phi[0]
    );
}

/// **Point 2 du critère, première moitié, corrigée par la mesure.** Les sept
/// bornes du tableau 21
/// s'effacent d'après le **réglage** — dès que deux agents partagent une famille,
/// leurs tirages ne sont démontrablement plus indépendants — et non d'après Φ_c
/// mesuré, qui ne sépare pas la conformité de la coordination.
#[test]
fn les_sept_bornes_seffacent_sur_le_reglage_et_la_borne_effacee_nest_pas_grisee() {
    // À curseur au repos : tirages indépendants, bornes affichées, et Φ_c
    // pourtant non nul — c'est très exactement la fausse alarme que PD12
    // interdit d'afficher comme une preuve.
    let repos = scenario_m(params(), 0.0, 11, 20_000).expect("scénario M");
    assert_eq!(repos.bornes_effacees(), 0);
    assert!(repos.hors_dominante.1.is_some());
    assert!(repos.conformite.phi_c > 0.10);
    assert!(dettes::verdicts(&Familles::une_par_agent(24))
        .iter()
        .all(|v| v.etat == EtatDeBorne::Affichee));

    // Dès que le curseur bouge : sept bornes effacées, et la borne est absente,
    // non pointillée — `None`, pas un drapeau.
    let conforme = scenario_m(params(), 1.0, 11, 20_000).expect("scénario M");
    assert_eq!(conforme.bornes_effacees(), 7);
    assert!(conforme.hors_dominante.1.is_none());
    // Et la mesure, elle, reste : effacer la borne n'efface pas ce qui a été
    // mesuré. `is_finite()` ne l'établissait pas — une constante l'est aussi ;
    // ce qui l'établit est que la grandeur soit une **fraction d'effort**, dans
    // l'intervalle qu'un minimum de 1 − p_max peut atteindre sur m ressources.
    let mesure = conforme.hors_dominante.0;
    assert!(
        mesure > 0.0 && mesure <= 1.0 - 1.0 / f64::from(params().m),
        "fraction hors dominante {mesure} : ce n'est pas une fraction d'effort mesurée"
    );
}

/// **Point 2 du critère, seconde moitié, et c'est elle qui porte la thèse.**
/// Aucun oracle de
/// sûreté armé ne se déclenche pendant que les bornes s'effacent : le mécanisme
/// continue de tourner, les oracles restent muets, et ce qui cesse de tenir est
/// une borne que rien dans le protocole ne surveille.
///
/// **Ce que ce test prouve exactement, et il faut le dire.** À part nulle, les
/// oracles `PLANCHER` et `HORS_DOMINANTE` sont **évalués** à chaque cycle et
/// restent muets : c'est une mesure. Dès que la part est non nulle, NF-14 efface
/// la borne, donc `verifier_bornes` sort avant de les évaluer — leur silence est
/// alors tenu **par construction** et non par la mesure. Le test l'assume et
/// vérifie à la place ce qui reste réfutable sous effacement : que l'exécution va
/// à son terme, que les sept bornes sont bien retirées, et que la **mesure**, elle,
/// survit à l'effacement de la borne. Le §0.1 du PRD le consigne.
///
/// **Ce que « la mesure survit » veut dire ici, et comment il se réfute.**
/// `is_finite()` ne l'établissait pas : remplacer `hors_dominante_observee` par
/// la constante `0.0` laissait ce test passer. Deux clauses le tiennent
/// maintenant, et la seconde est celle qui mord.
///
/// 1. La grandeur est une **fraction d'effort** : strictement positive, et au
///    plus 1 − 1/m, puisqu'elle est un minimum de 1 − p_max sur m ressources.
/// 2. Elle **dépend de l'exécution** : à part fixée, trois graines rendent trois
///    valeurs distinctes. Mesuré, à m = 6 — part 0 : 0,3325 / 0,3452 / 0,2882 ;
///    part 0,5 : 0,4401 / 0,2985 / 0,2952 ; part 1 : 0,3149 / 0,1074 / 0,2649.
///    **Toute** substitution par une constante tombe sur cette clause, quelle
///    que soit la constante choisie.
///
/// La clause 2 ne dit rien du *sens* de la variation, et c'est délibéré : la
/// mesure n'est pas monotone en la part — à graine 3, elle **monte** de 0,3325 à
/// 0,4401 entre part 0 et part 0,5. Une assertion de monotonie serait fausse.
#[test]
fn aucun_oracle_de_surete_ne_tombe_pendant_leffacement() {
    let plafond = 1.0 - 1.0 / f64::from(params().m);
    for part in [0.0, 0.5, 1.0] {
        let graines = [3u64, 11, 47];
        let mut mesures = Vec::new();
        for graine in graines {
            let r = scenario_m(params(), part, graine, 20_000).expect("scénario M");
            assert_eq!(
                r.violations_de_surete, 0,
                "part = {part}, graine = {graine} : un oracle est tombé, \
                 le scénario prouverait autre chose que ce qu'il annonce"
            );
            // Effacer une borne n'efface pas une mesure — clause 1.
            let mesure = r.hors_dominante.0;
            assert!(
                mesure > 0.0 && mesure <= plafond,
                "part = {part}, graine = {graine} : fraction hors dominante {mesure}, \
                 hors de ]0 ; {plafond}] — ce n'est pas une fraction d'effort mesurée"
            );
            mesures.push(mesure);

            let effacees = r.bornes_effacees();
            if part == 0.0 {
                assert_eq!(effacees, 0, "à curseur au repos, aucune borne ne s'efface");
                assert!(
                    r.hors_dominante.1.is_some(),
                    "et la borne reste affichée, donc les oracles sont bien évalués"
                );
            } else {
                assert_eq!(effacees, 7, "part = {part} : les sept bornes du tableau 21");
                assert!(r.hors_dominante.1.is_none(), "absente, pas grisée");
            }
        }

        // Clause 2 — la mesure dépend de l'exécution, donc trois graines ne
        // rendent pas la même valeur. C'est ce qui distingue une mesure d'une
        // constante, et l'effacement de la borne n'y change rien.
        for (i, a) in mesures.iter().enumerate() {
            for (j, b) in mesures.iter().enumerate().skip(i + 1) {
                assert!(
                    a != b,
                    "part = {part} : les graines {} et {} rendent la même fraction \
                     hors dominante {a} — la mesure ne dépend plus de l'exécution",
                    graines[i],
                    graines[j]
                );
            }
        }
    }
}

/// **Point 3 du critère.** Le contraste avec et sans identité apposée est lisible
/// sans explication : la même chaîne, l'une attribuable, l'autre non — et la
/// condition d'échec est constatée après coup, jamais empêchée.
#[test]
fn lidentite_apposee_est_constatee_et_sa_condition_dechec_est_provocable() {
    let sain = scenario_m(params(), 0.0, 5, 20_000).expect("scénario M");
    assert_eq!(sain.sessions_partagees, 0);

    let mut p = params();
    p.identite_partagee = true;
    let partage = scenario_m(p, 0.0, 5, 20_000).expect("scénario M");
    assert_eq!(
        partage.sessions_partagees, 1,
        "le milieu appose fidèlement une identité fausse : il ne peut que le constater"
    );
}

/// **Point 4 du critère.** Le dépôt aveugle coûte exactement un tour de journal
/// de plus par tour de délibération, et **ne change pas** le compte de messages.
#[test]
fn le_depot_aveugle_coute_en_latence_et_non_en_messages() {
    let mut d = DepotAveugle::nouveau(4, Mode::Nominal);
    let faits: Vec<FaitPrive> = (0..6)
        .map(|a| FaitPrive {
            agent: ActeurId(a),
            valeur: Some(f64::from(a)),
        })
        .collect();
    for _ in 0..4 {
        d.tour(&faits, &[]).expect("dans le budget");
    }
    // Θ(n) messages par tour : 6 écritures + 6 lectures, quatre tours.
    assert_eq!(d.messages(), 48);
    // Deux tours de journal par tour de délibération : c'est le surcoût, et il
    // est compté à part.
    assert_eq!(d.tours_de_journal(), 8);
    assert!(d.surcout().contains("il coûte en latence"));
    // Le budget est la seule condition d'arrêt.
    assert!(d.tour(&faits, &[]).is_none());
}

/// **Livrable 4 de la phase 6, hors critère de sortie** (§9 du PRD : « EX-M25
/// (historique vérifié) »). L'historique refuse de pondérer sur des issues non
/// vérifiables, au lieu de rendre un poids dégradé.
#[test]
fn lhistorique_refuse_la_ponderation_sur_des_issues_non_verifiables() {
    let mut h = Historique::nouveau();
    let a = Identite::propre(ActeurId(1));
    h.verifier(a, Issue::Confirmee);
    h.verifier(a, Issue::Confirmee);
    assert_eq!(h.poids(a).expect("issues vérifiables"), Some(1.0));

    h.verifier(a, Issue::NonVerifiable);
    let e = h.poids(a).expect_err("le poids doit être refusé");
    assert!(e.contains("récompense la conformité"));
}

/// **Livrable 5 de la phase 6, hors critère de sortie** (§9 du PRD : « EX-M26
/// (quota par ressource) »). Le quota borne une **ressource** — donc sans le
/// consentement de l'agent — et le prix croissant ne refuse rien, ce que
/// l'affichage doit dire.
#[test]
fn le_quota_borne_une_ressource_et_le_prix_ne_refuse_rien() {
    let mut dur = Quotas::nouveau(Politique::QuotaDur { plafond: 2 });
    assert!(matches!(dur.soumettre(1, 0), Verdict::Acceptee { .. }));
    assert!(matches!(dur.soumettre(1, 1), Verdict::Acceptee { .. }));
    assert!(matches!(dur.soumettre(1, 2), Verdict::Refusee { .. }));
    assert_eq!(dur.refus(), 1);

    let mut prix = Quotas::nouveau(Politique::PrixCroissant { pente: 0.5 });
    for a in 0..5 {
        assert!(matches!(prix.soumettre(1, a), Verdict::Acceptee { .. }));
    }
    assert_eq!(prix.refus(), 0, "une taxe ne refuse rien");
    assert!(prix.prix_cumule() > 5.0, "et elle se paie");
}

/// **Livrable 5 de la phase 6, hors critère de sortie** (§9 du PRD : « EX-A59 et
/// EX-V23 (demandes d'arbitrage) »). La file affiche l'âge de la plus ancienne
/// attente avec son compte, et déclare hors du système le délai qu'elle ne borne
/// pas.
#[test]
fn la_file_darbitrage_affiche_lage_avec_le_compte() {
    let mut f = FileDarbitrage::nouvelle(Duree(100));
    f.demander(
        Identite::propre(ActeurId(2)),
        3,
        Motif::MandatsContradictoires,
        Instant(10),
    );
    let a = f.affichage(Instant(200), "µs");
    assert!(a.contains("1 en attente"));
    assert!(a.contains("plus ancienne attente 190"));
    assert!(a.contains("DÉPASSÉ"));
    assert!(a.contains("pas dans le système"));
}

/// **Contrat de déterminisme, non négociable** (PD1) : le partage de tirage ne
/// casse pas le rejeu. Deux exécutions de même graine et de même structure
/// rendent la même mesure, partages compris.
#[test]
fn le_partage_de_tirage_ne_casse_pas_le_rejeu() {
    for part in [0.0, 0.5, 1.0] {
        let a = scenario_m(params(), part, 123, 20_000).expect("scénario M");
        let b = scenario_m(params(), part, 123, 20_000).expect("scénario M");
        assert_eq!(a.conformite, b.conformite, "part = {part}");
        assert_eq!(a.tirages_partages, b.tirages_partages, "part = {part}");
        assert_eq!(a.hors_dominante, b.hors_dominante, "part = {part}");
    }

    // Et deux graines distinctes ne rendent pas la même chose, sans quoi
    // l'égalité ci-dessus ne prouverait rien.
    let a = scenario_m(params(), 0.5, 1, 20_000).expect("scénario M");
    let b = scenario_m(params(), 0.5, 2, 20_000).expect("scénario M");
    assert_ne!(a.conformite.phi_c, b.conformite.phi_c);
}

/// Le partage porte sur le **tour** et non sur l'instant, et c'est vérifiable
/// hors du scénario : les cycles étant décalés, une clé par instant rendrait
/// EX-C19 inerte.
#[test]
fn le_partage_porte_sur_le_tour_et_non_sur_linstant() {
    let mut alea = Alea::nouveau(9);
    let mut t = TirageDeDecision::nouveau(Familles::unique(3));
    // Trois agents atteignant le tour 4 à trois moments quelconques.
    let a = t.uniforme(ActeurId(0), "choix", 4, &mut alea);
    let b = t.uniforme(ActeurId(1), "choix", 4, &mut alea);
    let c = t.uniforme(ActeurId(2), "choix", 4, &mut alea);
    assert_eq!(a, b);
    assert_eq!(b, c);
    assert_eq!(t.tires(), 1);
    assert_eq!(t.partages(), 2);
}

/// Le constat de mesure est exposé, et il dit ce qu'il faut refaire (NF-15).
#[test]
fn le_constat_de_mesure_est_expose_et_nomme_ce_qui_est_a_refaire() {
    let c = conformite::CONSTAT_DE_MESURE;
    assert!(c.contains("ne distingue pas la conformité de la coordination"));
    assert!(c.contains("à refaire sur la mesure"));
    // Trois dettes sur sept ne sont pas mesurables ici, et le produit le dit.
    assert_eq!(dettes::partage_mesurable(), (4, 3));
}
