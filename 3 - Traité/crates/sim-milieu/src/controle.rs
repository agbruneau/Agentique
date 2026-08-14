//! Plan de contrôle — **modèle de coût**, jamais protocole (EX-M21, DT7).
//!
//! > Le plan de données évite l'accord ; le plan de contrôle le paie pour tout
//! > le monde. (§4.2, p. 49)
//!
//! DT7 tranche : implanter Raft ferait du produit un simulateur de protocole
//! d'accord, ce que le traité refuse d'être. Ce qui est simulé, c'est le
//! **prix** : Ω(n) messages par décision, une fenêtre d'indisponibilité après
//! l'arrêt du meneur, et un quorum accessible ou non.
//!
//! Les compteurs de ce plan ne sont **jamais** additionnés à ceux du plan de
//! données (§5.1b). L'affichage dit « modèle de coût du plan de contrôle »,
//! jamais « consensus ».

use sim_core::alea::Alea;
use sim_core::temps::Duree;

/// Libellé imposé à tout affichage de ce plan (DT7).
pub const LIBELLE: &str = "modèle de coût du plan de contrôle — pas un protocole d'accord (DT7)";

/// Coût et état du quorum de métadonnées.
#[derive(Clone, Debug)]
pub struct PlanDeControle {
    /// k = 2f + 1.
    pub k: u32,
    /// Membres vivants du quorum.
    vivants: u32,
    /// Temps de diffusion, tiré dans 0,5 – 20 ms selon la technologie de
    /// stockage (§6.1, tableau 17).
    pub diffusion_min_ms: f64,
    /// Borne haute du temps de diffusion, en millisecondes.
    pub diffusion_max_ms: f64,
    /// Délai d'élection, tiré uniformément dans un intervalle fixe —
    /// 150 – 300 ms par défaut (§4.2, §4.3, §6.1).
    pub election_min_ms: f64,
    /// Borne haute du délai d'élection, en millisecondes (§4.2, §4.3, §6.1).
    pub election_max_ms: f64,
    /// Temps moyen entre pannes, en millisecondes.
    ///
    /// **Provenance absente (F1)** : le traité n'écrit que le symbole
    /// « ≪ MTBF » dans la condition du §4.2 et n'en chiffre aucune valeur. Une
    /// heure est une **décision du produit**, choisie pour que la condition soit
    /// franchement tenue au régime nominal, et `violations_de_la_condition`
    /// l'affiche telle quelle.
    pub mtbf_ms: f64,

    /// Messages du plan de contrôle. **Jamais additionnés** à ceux du plan de
    /// données.
    pub messages: u64,
    /// Décisions prises, chacune ayant coûté Ω(k) messages.
    pub decisions: u64,
    /// Élections de meneur.
    pub elections: u64,
    /// Indisponibilité cumulée après arrêt du meneur.
    pub indisponibilite: Duree,
    /// Élections déclenchées alors qu'une élection était en cours : c'est le
    /// mode de défaillance nommé.
    pub elections_perpetuelles: u64,
}

impl PlanDeControle {
    /// Construit le plan. `f` est le nombre de défaillances tolérées ; k = 2f+1.
    pub fn nouveau(f: u32) -> PlanDeControle {
        let k = 2 * f + 1;
        PlanDeControle {
            k,
            vivants: k,
            diffusion_min_ms: 0.5,
            diffusion_max_ms: 20.0,
            election_min_ms: 150.0,
            election_max_ms: 300.0,
            mtbf_ms: 3_600_000.0,
            messages: 0,
            decisions: 0,
            elections: 0,
            indisponibilite: Duree(0),
            elections_perpetuelles: 0,
        }
    }

    /// Le quorum est-il accessible ? Il faut une **majorité** de membres
    /// vivants : c'est ce que le détecteur fortement exact à terme exige, et
    /// c'est prouvé nécessaire (§4.2).
    pub fn quorum_accessible(&self) -> bool {
        self.vivants > self.k / 2
    }

    /// Nombre de membres vivants du quorum.
    pub fn vivants(&self) -> u32 {
        self.vivants
    }

    /// Arrête un membre. Sous la majorité, plus aucune décision n'est prise.
    pub fn arreter_un_membre(&mut self) {
        self.vivants = self.vivants.saturating_sub(1);
    }

    /// Ramène un membre, sans jamais dépasser `k`.
    pub fn redemarrer_un_membre(&mut self) {
        self.vivants = (self.vivants + 1).min(self.k);
    }

    /// Une décision du plan de contrôle : **Ω(n) messages**, où n est la taille
    /// du quorum. Rend `None` si le quorum n'est pas accessible — auquel cas
    /// rien n'est décidé, et c'est la bonne réponse plutôt qu'une décision
    /// unilatérale.
    pub fn decider(&mut self, n_essaim: u32) -> Option<u64> {
        if !self.quorum_accessible() {
            return None;
        }
        // Ω(n) par décision : le plan de contrôle paie pour tout le monde.
        let cout = self.k as u64 + n_essaim as u64;
        self.messages += cout;
        self.decisions += 1;
        Some(cout)
    }

    /// La condition `broadcastTime ≪ electionTimeout ≪ MTBF`, vérifiée en
    /// continu (§6.1, tableau 17).
    ///
    /// Rend la liste des inégalités violées. La **violation de gauche** est
    /// celle qui compte : quand le temps de diffusion approche le délai
    /// d'élection, une élection démarre avant que la précédente ait pu se
    /// conclure.
    pub fn violations_de_la_condition(&self) -> Vec<String> {
        let mut v = Vec::new();
        // « ≪ » n'est pas « < » : on exige un ordre de grandeur.
        if self.diffusion_max_ms * 10.0 >= self.election_min_ms {
            v.push(format!(
                "violation de gauche : temps de diffusion jusqu'à {:.1} ms contre un délai \
                 d'élection dès {:.1} ms — l'inégalité broadcastTime ≪ electionTimeout ne tient \
                 plus, et le mode de défaillance est **élections perpétuelles** : une panne née \
                 de la charge, manifestée comme panne d'accord (§6.1).",
                self.diffusion_max_ms, self.election_min_ms
            ));
        }
        if self.election_max_ms * 10.0 >= self.mtbf_ms {
            v.push(format!(
                "violation de droite : délai d'élection jusqu'à {:.1} ms contre un MTBF de \
                 {:.0} ms — le système retombe en panne avant d'avoir fini d'élire.",
                self.election_max_ms, self.mtbf_ms
            ));
        }
        v
    }

    /// Arrêt du meneur : une élection s'ouvre, et la partition est indisponible
    /// pendant sa durée.
    ///
    /// Si la condition de gauche est violée, l'élection n'aboutit pas et une
    /// autre s'ouvre : ce sont les **élections perpétuelles**.
    pub fn arret_du_meneur(&mut self, alea: &mut Alea, granularite_par_ms: u64) -> Duree {
        self.elections += 1;
        let duree_ms =
            self.election_min_ms + alea.uniforme() * (self.election_max_ms - self.election_min_ms);
        let diffusion_ms =
            self.diffusion_min_ms + alea.uniforme() * (self.diffusion_max_ms - self.diffusion_min_ms);

        // L'élection n'aboutit que si la diffusion tient dans son délai.
        if diffusion_ms >= duree_ms {
            self.elections_perpetuelles += 1;
        }
        let d = Duree((duree_ms * granularite_par_ms as f64) as u64);
        self.indisponibilite = self.indisponibilite + d;
        d
    }

    /// Affichage (EX-M21, EX-V17). Le mot « consensus » n'y figure pas.
    pub fn resume(&self) -> Vec<(&'static str, String)> {
        vec![
            ("nature", LIBELLE.to_string()),
            ("k = 2f + 1", format!("{} membres, {} vivants", self.k, self.vivants)),
            (
                "quorum",
                if self.quorum_accessible() {
                    "accessible".to_string()
                } else {
                    "inaccessible — aucune décision n'est prise, et c'est la bonne réponse"
                        .to_string()
                },
            ),
            (
                "messages du plan de contrôle",
                format!("{} — jamais additionnés à ceux du plan de données", self.messages),
            ),
            ("décisions", format!("{}", self.decisions)),
            (
                "indisponibilité cumulée",
                format!("{} tics après arrêt du meneur", self.indisponibilite.0),
            ),
            (
                "élections perpétuelles",
                format!("{} — panne née de la charge, manifestée comme panne d'accord", self.elections_perpetuelles),
            ),
        ]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-M21 — la majorité est nécessaire, et sous quorum inaccessible rien
    /// n'est décidé.
    #[test]
    fn sans_majorite_rien_nest_decide() {
        let mut p = PlanDeControle::nouveau(1); // k = 3
        assert_eq!(p.k, 3);
        assert!(p.quorum_accessible());
        assert!(p.decider(100).is_some());

        p.arreter_un_membre();
        assert!(p.quorum_accessible(), "2 sur 3 : majorité");
        p.arreter_un_membre();
        assert!(!p.quorum_accessible(), "1 sur 3 : plus de majorité");
        assert!(p.decider(100).is_none(), "aucune décision unilatérale");
    }

    /// Ω(n) messages par décision — le plan de contrôle paie pour tout le monde.
    #[test]
    fn une_decision_coute_omega_n() {
        let mut p = PlanDeControle::nouveau(1);
        let petit = p.decider(10).unwrap();
        let grand = p.decider(1_000).unwrap();
        assert!(grand > petit * 10);
    }

    /// La condition tient aux valeurs par défaut… sauf la gauche, parce que la
    /// plage de diffusion monte à 20 ms contre un délai d'élection dès 150 ms :
    /// un seul ordre de grandeur, pas deux. Le simulateur le dit au lieu de le
    /// supposer.
    #[test]
    fn la_condition_est_verifiee_en_continu() {
        let p = PlanDeControle::nouveau(1);
        let v = p.violations_de_la_condition();
        assert_eq!(v.len(), 1, "{v:?}");
        assert!(v[0].contains("violation de gauche"));
        assert!(v[0].contains("élections perpétuelles"));
    }

    /// EX-M21 — la violation de gauche est **provocable**, et le mode de
    /// défaillance annoncé se produit (NF-10, NF-16).
    #[test]
    fn nf10_la_violation_de_gauche_produit_des_elections_perpetuelles() {
        let mut p = PlanDeControle::nouveau(1);
        // Un stockage lent : la diffusion dépasse le délai d'élection.
        p.diffusion_min_ms = 200.0;
        p.diffusion_max_ms = 400.0;
        assert!(!p.violations_de_la_condition().is_empty());

        let mut alea = Alea::nouveau(1);
        for _ in 0..50 {
            p.arret_du_meneur(&mut alea, 1_000);
        }
        assert!(
            p.elections_perpetuelles > 0,
            "la violation de gauche doit produire des élections qui n'aboutissent pas"
        );
        assert!(p.indisponibilite.0 > 0);
    }

    /// Aux valeurs saines, l'élection aboutit.
    #[test]
    fn sous_condition_tenue_les_elections_aboutissent() {
        let mut p = PlanDeControle::nouveau(1);
        p.diffusion_max_ms = 5.0;
        let mut alea = Alea::nouveau(2);
        for _ in 0..50 {
            p.arret_du_meneur(&mut alea, 1_000);
        }
        assert_eq!(p.elections_perpetuelles, 0);
    }

    /// DT7 — l'affichage ne dit jamais « consensus ».
    #[test]
    fn laffichage_ne_dit_jamais_consensus() {
        let p = PlanDeControle::nouveau(2);
        for (_, v) in p.resume() {
            assert!(!v.to_lowercase().contains("consensus"), "{v}");
        }
        assert!(LIBELLE.contains("pas un protocole d'accord"));
    }
}
