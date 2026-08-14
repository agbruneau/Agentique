//! Horloges locales à dérive (EX-C13) et domaines de panne partagés (EX-C14).
//!
//! Deux mécanismes qui n'existent que pour rendre **fausses** des hypothèses que
//! le reste du produit prend pour acquises. Sans eux, le bail serait sûr par
//! construction et la corroboration améliorerait toujours la détection ; avec
//! eux, les deux cessent de tenir, et c'est ce que les scénarios J et L doivent
//! montrer.

use crate::alea::Alea;
use crate::temps::{Duree, Instant};
use crate::ActeurId;
use std::collections::BTreeSet;

/// Horloges locales à dérive (EX-C13).
///
/// Chaque agent possède une horloge dont le facteur de dérive est **tiré de la
/// graine**, borné par un `ε_vrai` de configuration. L'horloge reste logique :
/// PD1 tient, la dérive est déterministe et rejouable.
///
/// **`ε_vrai` est distinct de l'`ε` supposé par les mécanismes de bail**
/// (EX-A33). C'est tout l'objet : quand la dérive réelle dépasse celle que le
/// mécanisme suppose, le détenteur croit son bail vivant alors que le quorum
/// l'a réattribué — et **aucun agent ne l'observe**.
#[derive(Clone, Debug)]
pub struct Horloges {
    /// Facteur de dérive de chaque agent, autour de 1,0.
    facteurs: Vec<f64>,
    /// Borne de dérive relative **réelle**, celle du monde simulé.
    pub epsilon_vrai: f64,
}

impl Horloges {
    /// Construit les horloges. `epsilon_vrai` est la dérive relative maximale :
    /// à 1e-2, une horloge peut avancer ou retarder de 1 % du temps écoulé.
    pub fn nouvelles(n: u32, epsilon_vrai: f64, alea: &mut Alea) -> Horloges {
        Horloges {
            facteurs: (0..n)
                .map(|_| 1.0 + epsilon_vrai * (alea.uniforme() * 2.0 - 1.0))
                .collect(),
            epsilon_vrai,
        }
    }

    /// Horloges parfaites — utile pour isoler un autre effet. Ce n'est pas le
    /// défaut : une horloge parfaite est une hypothèse, pas une observation.
    pub fn parfaites(n: u32) -> Horloges {
        Horloges {
            facteurs: vec![1.0; n as usize],
            epsilon_vrai: 0.0,
        }
    }

    /// Facteur de dérive d'un agent.
    pub fn facteur(&self, agent: ActeurId) -> f64 {
        self.facteurs
            .get(agent.0 as usize)
            .copied()
            .unwrap_or(1.0)
    }

    /// L'instant tel que **cet agent** le perçoit, à partir du temps de
    /// référence de l'observateur.
    pub fn percu(&self, agent: ActeurId, reference: Instant) -> Instant {
        Instant((reference.0 as f64 * self.facteur(agent)) as u64)
    }

    /// Écart maximal entre deux horloges après une durée donnée.
    ///
    /// C'est cette grandeur que le mécanisme de bail suppose bornée par son
    /// `ε`. Quand elle le dépasse, la sûreté du bail tombe **sans qu'aucun
    /// compteur du protocole ne bouge**.
    pub fn ecart_maximal(&self, ecoule: Duree) -> Duree {
        let max = self.facteurs.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
        let min = self.facteurs.iter().cloned().fold(f64::INFINITY, f64::min);
        Duree(((max - min) * ecoule.0 as f64) as u64)
    }

    /// Dérive relative **effectivement tirée** : `max |facteur − 1|`.
    ///
    /// Distincte d'`epsilon_vrai`, qui n'en est que la borne de configuration.
    /// Sur un petit `n`, le tirage peut rester loin sous sa borne.
    pub fn derive_tiree(&self) -> f64 {
        self.facteurs
            .iter()
            .map(|f| (f - 1.0).abs())
            .fold(0.0, f64::max)
    }

    /// Vrai si la dérive réelle dépasse celle qu'un mécanisme suppose.
    ///
    /// **C'est le troisième mode d'EX-A33, et il est invisible** : ni la
    /// latence ni le taux d'erreur ne le signalent. Seul l'oracle externe le
    /// voit.
    ///
    /// La comparaison porte sur la dérive **tirée**, pas sur `epsilon_vrai` :
    /// signaler le mode sur la borne de configuration le signalerait quand
    /// aucune horloge ne dérive assez pour le produire — une hypothèse affichée
    /// comme une mesure.
    pub fn depasse(&self, epsilon_suppose: f64) -> bool {
        self.derive_tiree() > epsilon_suppose
    }

    /// Libellé permanent (EX-C13, §7.3), **destiné** à l'affichage en gris avec
    /// sa source. Aucun appelant à ce jour : `sim-viz` ne le lit pas.
    pub const PROVENANCE_EPSILON: &'static str =
        "une infrastructure de temps à références GPS et horloges atomiques maintient \
         l'incertitude généralement sous 10 ms — repère externe (annexe B). Un déploiement \
         hybride sans cette infrastructure ne mesure pas sa dérive ; **il la suppose**.";
}

/// Un domaine de panne nommé (EX-C14).
///
/// La corrélation s'injecte **par domaine**, et non par un scalaire global :
/// même image, même lien, même plan de contrôle. Un agent appartient à zéro ou
/// plusieurs domaines.
#[derive(Clone, Debug)]
pub struct Domaine {
    /// Ce que le domaine partage — « même image », « même baie », « même plan
    /// de contrôle ». Le nom est ce qui rend la corrélation lisible.
    pub nom: &'static str,
    /// Membres, ordonnés (PD1).
    pub membres: Vec<u32>,
    /// Probabilité que le domaine entier tombe à un pas d'évaluation.
    pub probabilite: f64,
}

/// La structure des domaines. **Les scénarios pilotent la structure, jamais ρ.**
#[derive(Clone, Debug, Default)]
pub struct Domaines {
    /// Les domaines déclarés. Un agent peut n'appartenir à aucun.
    pub domaines: Vec<Domaine>,
    /// Taille de la population, dénominateur du calcul de ρ.
    pub n: u32,
}

impl Domaines {
    /// Population de `n` agents, sans aucun domaine : ρ = 0.
    pub fn nouveau(n: u32) -> Domaines {
        Domaines {
            domaines: Vec::new(),
            n,
        }
    }

    /// Domaines **disjoints** : chaque agent dans le sien. C'est le régime où
    /// les fautes sont indépendantes, et où toutes les bornes probabilistes du
    /// traité s'appliquent.
    pub fn disjoints(n: u32, probabilite: f64) -> Domaines {
        Domaines {
            domaines: (0..n)
                .map(|i| Domaine {
                    nom: "hôte propre",
                    membres: vec![i],
                    probabilite,
                })
                .collect(),
            n,
        }
    }

    /// Domaine **unique partagé** : tous les agents derrière la même dépendance.
    /// Les fautes deviennent parfaitement corrélées.
    pub fn unique(n: u32, probabilite: f64) -> Domaines {
        Domaines {
            domaines: vec![Domaine {
                nom: "dépendance partagée",
                membres: (0..n).collect(),
                probabilite,
            }],
            n,
        }
    }

    /// Interpolation entre disjoints et unique : `part` ∈ [0, 1] fixe la
    /// fraction de la population réunie dans un domaine commun.
    ///
    /// C'est le **curseur du scénario L**, et ρ en est dérivé.
    pub fn interpole(n: u32, part: f64, probabilite: f64) -> Domaines {
        let groupes = ((1.0 - part.clamp(0.0, 1.0)) * (n as f64 - 1.0) + 1.0).round().max(1.0) as u32;
        let taille = n.div_ceil(groupes);
        let mut domaines = Vec::new();
        let mut debut = 0;
        while debut < n {
            let fin = (debut + taille).min(n);
            domaines.push(Domaine {
                nom: "domaine",
                membres: (debut..fin).collect(),
                probabilite,
            });
            debut = fin;
        }
        Domaines { domaines, n }
    }

    /// **ρ est dérivé de la structure, jamais saisi** (EX-C14).
    ///
    /// Il vaut la probabilité que deux agents tirés au hasard tombent ensemble
    /// plutôt qu'indépendamment : 0 sous domaines disjoints, 1 sous domaine
    /// unique.
    /// Les paires **distinctes** sont comptées une fois, quel que soit le
    /// nombre de domaines qui les portent. Sommer `C(|d|, 2)` sur les domaines
    /// double-compterait tout recouvrement — et le recouvrement est le cas
    /// nommé par EX-C14 : « même image, **même lien**, même plan de contrôle »
    /// est trois domaines sur les mêmes agents. Un `.min(1,0)` masquerait le
    /// dépassement au lieu de le corriger.
    pub fn rho(&self) -> f64 {
        if self.n < 2 {
            return 0.0;
        }
        let mut paires: BTreeSet<(u32, u32)> = BTreeSet::new();
        for d in &self.domaines {
            let mut m: Vec<u32> = d.membres.to_vec();
            m.sort_unstable();
            m.dedup();
            for (i, a) in m.iter().enumerate() {
                for b in &m[i + 1..] {
                    paires.insert((*a, *b));
                }
            }
        }
        let paires_totales = (self.n as f64) * (self.n as f64 - 1.0) / 2.0;
        paires.len() as f64 / paires_totales
    }

    /// Tire les agents frappés à ce pas. Une faute de domaine frappe **tous ses
    /// membres au même instant logique**.
    pub fn tirer(&self, alea: &mut Alea) -> Vec<u32> {
        let mut frappes = Vec::new();
        for d in &self.domaines {
            if alea.bernoulli(d.probabilite) {
                for m in &d.membres {
                    if !frappes.contains(m) {
                        frappes.push(*m);
                    }
                }
            }
        }
        frappes.sort_unstable();
        frappes
    }

    /// Vrai si ces agents partagent au moins un domaine — donc si leurs fautes
    /// sont corrélées.
    ///
    /// C'est la condition que le sondage indirect d'EX-A23 **ne vérifie pas** et
    /// qu'EX-C14 rend fausse à volonté.
    pub fn partagent(&self, agents: &[u32]) -> bool {
        self.domaines.iter().any(|d| {
            agents.iter().filter(|a| d.membres.contains(a)).count() >= 2
        })
    }

    /// Affichage (EX-C14) : ρ porte l'étiquette « dérivé ».
    pub fn affichage(&self) -> String {
        format!(
            "{} domaine(s) nommé(s) ; ρ = {:.4} — **grandeur dérivée de la structure**, jamais \
             saisie (EX-C14). Les scénarios pilotent la structure, pas ρ.",
            self.domaines.len(),
            self.rho()
        )
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-C13 — la dérive est déterministe et rejouable : PD1 tient.
    #[test]
    fn la_derive_est_deterministe_et_rejouable() {
        let a = Horloges::nouvelles(64, 1e-2, &mut Alea::nouveau(1));
        let b = Horloges::nouvelles(64, 1e-2, &mut Alea::nouveau(1));
        for i in 0..64u32 {
            assert_eq!(a.facteur(ActeurId(i)), b.facteur(ActeurId(i)));
        }
        let c = Horloges::nouvelles(64, 1e-2, &mut Alea::nouveau(2));
        assert_ne!(a.facteur(ActeurId(0)), c.facteur(ActeurId(0)));
    }

    /// L'écart entre horloges croît avec le temps écoulé — c'est ce qui rend le
    /// bail dangereux sur une longue durée.
    #[test]
    fn lecart_croit_avec_le_temps() {
        let h = Horloges::nouvelles(64, 1e-2, &mut Alea::nouveau(3));
        let court = h.ecart_maximal(Duree(1_000));
        let long = h.ecart_maximal(Duree(100_000));
        assert!(long.0 > court.0 * 50, "{} contre {}", long.0, court.0);
    }

    /// EX-C13 — `ε_vrai` et l'`ε` supposé sont **distincts**, et c'est leur
    /// écart qui produit le troisième mode d'EX-A33.
    #[test]
    fn epsilon_vrai_est_distinct_de_lepsilon_suppose() {
        let h = Horloges::nouvelles(8, 1e-1, &mut Alea::nouveau(4));
        assert!(h.depasse(1e-2), "la dérive réelle dépasse celle supposée");
        assert!(!h.depasse(1.0), "et pas une hypothèse plus large");
        assert!(Horloges::PROVENANCE_EPSILON.contains("il la suppose"));
    }

    #[test]
    fn des_horloges_parfaites_ne_derivent_pas() {
        let h = Horloges::parfaites(16);
        assert_eq!(h.ecart_maximal(Duree(u32::MAX as u64)), Duree(0));
        assert!(!h.depasse(0.0));
    }

    /// EX-C14 — ρ est **dérivé** : 0 sous domaines disjoints, 1 sous domaine
    /// unique, et il parcourt l'intervalle quand le curseur bouge.
    #[test]
    fn rho_est_derive_de_la_structure() {
        assert_eq!(Domaines::disjoints(64, 0.01).rho(), 0.0);
        assert_eq!(Domaines::unique(64, 0.01).rho(), 1.0);

        let mut precedent = 0.0;
        for k in 0..=10 {
            let r = Domaines::interpole(64, k as f64 / 10.0, 0.01).rho();
            assert!(r >= precedent - 1e-9, "ρ doit croître : {precedent} puis {r}");
            precedent = r;
        }
        assert!(Domaines::disjoints(4, 0.0).affichage().contains("dérivée"));
    }

    /// EX-C14 — une faute de domaine frappe **tous ses membres au même instant
    /// logique**.
    #[test]
    fn une_faute_de_domaine_frappe_tous_ses_membres() {
        let d = Domaines::unique(32, 1.0);
        let frappes = d.tirer(&mut Alea::nouveau(5));
        assert_eq!(frappes.len(), 32, "le domaine entier tombe d'un coup");

        let disjoints = Domaines::disjoints(32, 1.0);
        assert_eq!(disjoints.tirer(&mut Alea::nouveau(5)).len(), 32);
        // Mais à faible probabilité, les disjoints tombent séparément.
        let rares = Domaines::disjoints(1_000, 0.01);
        let f = rares.tirer(&mut Alea::nouveau(6));
        assert!(f.len() < 100, "{} agents frappés sur 1 000", f.len());
    }

    /// La condition que le sondage indirect ne vérifie pas : les s pairs
    /// partagent-ils le lien fautif ?
    #[test]
    fn le_partage_de_domaine_se_constate() {
        let unique = Domaines::unique(16, 0.0);
        assert!(unique.partagent(&[0, 5, 9]));
        let disjoints = Domaines::disjoints(16, 0.0);
        assert!(!disjoints.partagent(&[0, 5, 9]));
    }
}
