//! **Scénario M — Le second axe** (§8.1, §8.2 et §8.3 du traité).
//!
//! > Un milieu qui rend la coordination bon marché rend du même geste bon marché
//! > ce que le concepteur ne veut pas — la conformité, puisque tous lisent la
//! > même trace ; la collusion, puisqu'un tableau public suffit à s'aligner au
//! > sou près ; la tromperie, puisque déposer coûte le même prix qu'on dise vrai
//! > ou faux.
//!
//! **Cette phrase est une épissure, et elle ne se lit à aucune page.** Sa
//! proposition principale — jusqu'à « ce que le concepteur ne veut pas » — est
//! reprise mot pour mot de l'**introduction, p. 5** ; l'énumération des trois est
//! celle du **§8.3 du traité, p. 127**, où la proposition, elle, s'écrit « la mesure ajoute
//! qu'il rend tout aussi bon marché ». Troisième édition dans les deux cas. Le
//! §9 du PRD portait la même épissure sous la seule mention « §8.3, p. 94 » —
//! deux provenances pour une, et la page d'une édition antérieure ; le banc du
//! 17 août 2026 l'y a démontée en même temps qu'ici.
//!
//! **Ce scénario ne montre rien de neuf, et c'est sa forme.** Il rejoue le
//! scénario B en poussant un curseur qu'aucun scénario livré n'avait, et il
//! mesure ce que la conformité fait à des bornes **déjà mesurées ici**. Le ch. 8
//! ne réfute aucun mécanisme de l'ouvrage : il déplace le domaine de validité de
//! sept énoncés, ce qui est plus difficile à voir et se corrige moins bien,
//! puisque le mécanisme continue de tourner pendant que sa borne cesse de tenir.
//!
//! **La circularité est réelle et elle est nommée** (RQ13). La conformité est
//! **injectée** : le simulateur n'exécute aucun modèle de langage et n'a aucun
//! moyen de faire émerger la variance nulle, il la pose. Ce que le scénario
//! établit n'est donc pas que des agents se conforment — le traité le mesure, le
//! produit ne le peut pas — mais **quels résultats déjà livrés ici cessent de
//! tenir quand ils le font**, et lesquels ne le savent pas.

use crate::conformite::{self, Conformite};
use crate::dettes::{self, EtatDeBorne, Verdict};

use crate::scenario::Bloc;
use crate::stigmergie::{Evt, Fourragement, Params};
use sim_core::alea::Alea;
use sim_core::moteur::{Budget, Moteur};
use sim_core::temps::Granularite;

/// Bloc de trois du scénario M (PD8).
pub const BLOC_M: Bloc = Bloc {
    en_clair: "Quand tous les agents décident de la même façon, le simulateur continue de \
               tourner exactement comme avant — mais les garanties chiffrées qu'il affichait \
               ne valent plus, et rien dans le mécanisme ne s'en aperçoit.",
    these: "Un milieu qui rend la coordination bon marché rend du même geste bon marché ce que \
            le concepteur ne veut pas — la conformité, puisque tous lisent la même trace ; la \
            collusion, puisqu'un tableau public suffit à s'aligner au sou près ; la tromperie, \
            puisque déposer coûte le même prix qu'on dise vrai ou faux.",
    source: "épissure de deux endroits, et c'est la thèse (4ᵉ éd.) : la proposition principale — \
             jusqu'à « ce que le concepteur ne veut pas » — est celle de l'introduction, p. 5, mot \
             pour mot ; l'énumération des trois est celle du §8.3, p. 127, où la proposition, \
             elle, s'écrit « la mesure ajoute qu'il rend tout aussi bon marché »",
    mecanisme_visible: "porter la part de conformité de 0 à 1 fait consommer aux n agents le \
                        même tirage pour la même décision (EX-C19) ; Φ_c mesuré sur les \
                        décisions déposées passe de ≈ 0 à > 0 (EX-A56), et les sept bornes du \
                        tableau 21 sont effacées de l'affichage (EX-A58, NF-14) — pendant que \
                        les oracles de sûreté armés ne se déclenchent pas, parce qu'ils \
                        vérifient des propriétés qui restent vraies.",
    ne_demontre_pas: "que la conformité mesurée par le traité soit reproduite : elle est \
                      INJECTÉE. Le simulateur n'exécute aucun modèle de langage. Il ne démontre \
                      pas non plus qu'il existe un seuil — le traité n'en a aucune mesure —, ni \
                      que les mécanismes du §8.2 fonctionnent, aucun n'étant mesuré par une \
                      source, ni que l'escalade du §8.3 soit empêchable, le monde clos n'ayant \
                      ni système d'exploitation ni droits (T3).",
};

/// Ce que le scénario M rapporte.
#[derive(Clone, Debug)]
pub struct ResultatM {
    /// Part de conformité posée en entrée (EX-C19).
    pub part_conforme: f64,
    /// Affichage de la structure des familles.
    pub structure: String,
    /// Φ_c mesuré sur les décisions déposées (EX-A56).
    pub conformite: Conformite,
    /// L'état des sept bornes du tableau 21 (EX-A58).
    pub verdicts: Vec<Verdict>,
    /// Tirages rediffusés au lieu d'être consommés — la mesure directe de
    /// l'effet de la structure.
    pub tirages_partages: u64,
    /// Violations d'oracle de sûreté pendant l'exécution.
    ///
    /// **C'est le critère qui porte la thèse** : il doit rester à zéro pendant
    /// que les bornes s'effacent. Un scénario qui ferait tomber un oracle
    /// prouverait autre chose que ce qu'il annonce.
    pub violations_de_surete: usize,
    /// Sessions vues avec plusieurs agents distincts — condition d'échec
    /// d'EX-M24, constatée et non supposée.
    pub sessions_partagees: usize,
    /// Fraction d'effort mesurée hors ressource dominante, et sa borne.
    ///
    /// La seconde est **effacée** — `None`, pas un drapeau — dès que la structure
    /// des familles viole l'indépendance des tirages, c'est-à-dire d'après le
    /// **réglage** et jamais d'après Φ_c mesuré (`dettes::verdicts`, §0.1 du PRD).
    /// La première, elle, reste : effacer une borne n'efface pas une mesure.
    pub hors_dominante: (f64, Option<f64>),
}

impl ResultatM {
    /// Les bornes effacées, sur les sept.
    pub fn bornes_effacees(&self) -> usize {
        self.verdicts
            .iter()
            .filter(|v| v.etat == EtatDeBorne::Effacee)
            .count()
    }

    /// Libellé permanent du scénario, qui dit ce que le milieu ne voit pas (T3).
    pub fn libelle_permanent() -> &'static str {
        "ici, le milieu voit ce qu'on lui a fait écrire ; le régime mesuré, lui, contourne le \
         milieu — et la conformité est une entrée du modèle, comme la corrélation des fautes : \
         ce que le scénario mesure est son effet, jamais sa valeur"
    }
}

/// Exécute le scénario M : le scénario B, sous une part de conformité donnée.
///
/// `part_conforme` ∈ [0, 1]. À 0, la population est décorrélée et le résultat doit
/// être identique à celui du scénario B — c'est ce qui rend le scénario honnête :
/// le curseur au repos ne change rien.
pub fn scenario_m(
    mut params: Params,
    part_conforme: f64,
    graine: u64,
    budget_evenements: u64,
) -> Result<ResultatM, String> {
    params.part_conforme = part_conforme;

    let g = Granularite::Micro;
    let mut moteur: Moteur<Evt> = Moteur::nouveau(graine, g, Budget::evenements(budget_evenements));
    // Même amorce que le scénario B : à `part_conforme = 0`, les deux exécutions
    // doivent être **identiques**, ce qui interdit de semer autrement ici.
    let mut f = {
        let mut amorce = Alea::nouveau(graine ^ 0x5eed);
        Fourragement::nouveau(params, g, &mut amorce)?
    };
    f.armer_oracles(&mut moteur.oracles);
    f.amorcer(&mut moteur);
    while let Some(ev) = moteur.suivant() {
        f.traiter(&mut moteur, ev.cible, ev.charge);
    }

    // Φ_c se lit sur les décisions déposées, dans **une** partition : c'est M2
    // qui l'impose, et DT14 qui tranche le lieu. Le scénario B range toutes ses
    // ressources sur la partition 0 par défaut ; si l'appelant les a réparties,
    // l'estimation refuse, et c'est le bon comportement.
    let conformite =
        conformite::estimer(f.milieu.partition(0).enregistrements()).map_err(str::to_string)?;
    // NF-14 s'applique au **réglage**, non à la mesure : c'est la structure des
    // familles qui viole démontrablement l'indépendance des tirages. Φ_c ne le
    // ferait pas, faute de séparer ses deux causes (CONSTAT_DE_MESURE).
    let verdicts = dettes::verdicts(f.tirage.familles());

    let hors_dominante_mesuree = f.mesures.hors_dominante_observee;
    let borne = f.params.bornes().fraction_hors_dominante;
    // La borne est **effacée**, pas grisée : `None` et non un drapeau.
    let borne_affichee = if verdicts
        .iter()
        .any(|v| v.etat == dettes::EtatDeBorne::Effacee)
    {
        None
    } else {
        Some(borne)
    };

    Ok(ResultatM {
        part_conforme,
        structure: f.tirage.familles().affichage(),
        conformite,
        verdicts,
        tirages_partages: f.tirage.partages(),
        violations_de_surete: moteur.oracles.violations().len(),
        sessions_partagees: f.milieu.sessions_partagees().len(),
        hors_dominante: (hors_dominante_mesuree, borne_affichee),
    })
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::conformite::CONSTAT_DE_MESURE;

    fn params() -> Params {
        let mut p = Params::scenario_b();
        p.n = 24;
        p.m = 6;
        p.p = 1;
        p.ressources_sur_une_partition = true;
        p.intervalle_lecture = 128;
        p
    }

    /// Le curseur au repos ne change **rien** : à `part_conforme = 0`, le
    /// scénario M rejoue le scénario B, mêmes réglages et même graine.
    ///
    /// C'est ce que la documentation de [`scenario_m`] affirme, et c'est ce qui
    /// rend le scénario honnête — un curseur dont la position de repos déplacerait
    /// déjà la mesure ferait passer un écart de câblage pour un effet de la
    /// conformité. Rien ne le vérifiait.
    #[test]
    fn a_curseur_au_repos_le_scenario_m_rejoue_le_scenario_b() {
        let b = crate::scenario_b(params(), 7, 20_000).unwrap();
        let m = scenario_m(params(), 0.0, 7, 20_000).unwrap();
        assert_eq!(
            m.conformite,
            b.conformite.unwrap(),
            "Φ_c diffère : les deux chemins n'exécutent pas la même chose"
        );
        assert_eq!(
            m.hors_dominante.0, b.mesures.hors_dominante_observee,
            "la fraction hors dominante diffère"
        );
        assert_eq!(m.tirages_partages, 0);
    }

    #[test]
    fn le_curseur_au_repos_ne_partage_aucun_tirage() {
        let r = scenario_m(params(), 0.0, 7, 20_000).unwrap();
        assert_eq!(
            r.tirages_partages, 0,
            "une famille par agent : aucun partage"
        );
        assert!(r.structure.contains("décorrélée"));
    }

    #[test]
    fn la_famille_unique_fait_partager_les_tirages() {
        let r = scenario_m(params(), 1.0, 7, 20_000).unwrap();
        assert!(
            r.tirages_partages > 0,
            "une famille unique rediffuse ses tirages"
        );
        assert!(r.structure.contains("conforme"));
    }

    #[test]
    fn le_partage_croit_avec_la_part_de_conformite() {
        // C'est ce que le curseur contrôle réellement, et la seule grandeur qui
        // en dépende de façon monotone — Φ_c, lui, ne l'est pas (voir
        // `CONSTAT_DE_MESURE`).
        let p: Vec<u64> = [0.0, 0.25, 0.5, 0.75, 1.0]
            .iter()
            .map(|part| {
                scenario_m(params(), *part, 7, 20_000)
                    .unwrap()
                    .tirages_partages
            })
            .collect();
        assert!(
            p.windows(2).all(|w| w[0] <= w[1]),
            "partages non croissants : {p:?}"
        );
        assert_eq!(p[0], 0);
    }

    #[test]
    fn phi_c_est_deja_non_nul_a_curseur_au_repos() {
        // **Constat de mesure**, et il contredit ce que le PRD annonçait : les
        // agents lisent tous la même trace, donc leurs décisions sont corrélées
        // avant qu'aucun tirage ne soit partagé. Ce test fixe le constat pour que
        // sa disparition soit un événement, non un glissement.
        let r = scenario_m(params(), 0.0, 7, 20_000).unwrap();
        assert!(
            r.conformite.phi_c > 0.10,
            "Φ_c = {} à curseur au repos — le constat de mesure a changé",
            r.conformite.phi_c
        );
        assert!(r.conformite.depasse_sa_precision());
        assert!(CONSTAT_DE_MESURE.contains("ne distingue pas"));
    }

    #[test]
    fn leffacement_des_bornes_suit_le_curseur_et_non_la_mesure() {
        // NF-14 porte sur un réglage : à curseur au repos, les tirages sont
        // indépendants et les bornes restent affichées — même si Φ_c mesuré est
        // non nul, parce qu'il mesure alors la coordination et non le tirage.
        let repos = scenario_m(params(), 0.0, 11, 20_000).unwrap();
        assert_eq!(repos.bornes_effacees(), 0);
        assert!(repos.hors_dominante.1.is_some());
        assert!(repos.conformite.phi_c > 0.10, "et Φ_c est pourtant non nul");

        for part in [0.25, 0.5, 1.0] {
            let r = scenario_m(params(), part, 11, 20_000).unwrap();
            assert_eq!(r.bornes_effacees(), 7, "part = {part}");
            assert!(r.hors_dominante.1.is_none(), "borne effacée, non grisée");
        }
    }

    #[test]
    fn aucun_oracle_de_surete_ne_tombe_pendant_que_les_bornes_seffacent() {
        // C'est le critère qui porte la thèse : le mécanisme continue de tourner,
        // les oracles restent muets, et ce qui cesse de tenir est une borne que
        // rien dans le protocole ne surveille.
        for part in [0.0, 0.5, 1.0] {
            let r = scenario_m(params(), part, 11, 20_000).unwrap();
            assert_eq!(
                r.violations_de_surete, 0,
                "part = {part} : un oracle est tombé, le scénario prouverait autre chose"
            );
        }
    }

    #[test]
    fn le_scenario_se_rejoue_a_lidentique_par_graine() {
        let a = scenario_m(params(), 0.7, 99, 20_000).unwrap();
        let b = scenario_m(params(), 0.7, 99, 20_000).unwrap();
        assert_eq!(a.conformite, b.conformite);
        assert_eq!(a.tirages_partages, b.tirages_partages);
        assert_eq!(a.hors_dominante, b.hors_dominante);
    }

    #[test]
    fn lidentite_partagee_est_constatee_apres_coup() {
        let mut p = params();
        p.identite_partagee = true;
        let r = scenario_m(p, 0.0, 5, 20_000).unwrap();
        assert_eq!(
            r.sessions_partagees, 1,
            "une session vue avec plusieurs agents : le zombie du §2.1 du traité par la porte \
             de l'identité"
        );
        let r2 = scenario_m(params(), 0.0, 5, 20_000).unwrap();
        assert_eq!(r2.sessions_partagees, 0);
    }

    #[test]
    fn le_bloc_de_trois_nomme_linjection() {
        assert!(BLOC_M.ne_demontre_pas.contains("INJECTÉE"));
        assert!(ResultatM::libelle_permanent().contains("entrée du modèle"));
    }
}
