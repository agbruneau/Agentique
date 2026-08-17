//! Service d'échantillonnage de pairs (EX-A17) et tri de vue (EX-A18).
//!
//! > Aucun mécanisme n'accède à la liste des vivants autrement que par ce
//! > service. (EX-A17)
//!
//! ## Pourquoi le défaut n'est pas l'uniforme parfait
//!
//! RQ10 nomme le pire mode de rupture du produit : le service descend du même
//! générateur semé que le reste du monde clos, il est donc aussi uniforme qu'on
//! le lui demande. Or le résultat expérimental du traité est que les
//! implantations réelles fournissent un flux **localement** uniforme dont les
//! propriétés d'aléa ne tiennent pas globalement (§4.1). Retrouver une borne de
//! convergence sous un échantillonneur parfait, c'est la retrouver sous
//! l'hypothèse la plus favorable — et aucun compteur ne le signalerait.
//!
//! Le défaut est donc **déséquilibré**, et le biais est un objet de première
//! classe qu'on injecte, jamais une propriété qu'on mesure.

use sim_core::alea::Alea;

/// Biais de l'échantillonneur.
#[derive(Clone, Copy, PartialEq, Debug, Default)]
pub enum Biais {
    /// Tirage uniforme. **Ce n'est pas le défaut** : c'est l'hypothèse la plus
    /// favorable, et le §8.3 exige qu'on le dise.
    Uniforme,
    /// Certains pairs sont tirés bien plus souvent que d'autres. C'est le
    /// régime par défaut (RQ10).
    #[default]
    Desequilibre,
    /// Les pairs d'un même hôte se tirent entre eux : le graphe d'échange se
    /// referme par grappes, et le régime de cycles quitte Θ(log n).
    GroupeParHote {
        /// Nombre d'agents par hôte.
        taille_hote: u32,
        /// Probabilité de rester dans son hôte.
        p_local: f64,
    },
    /// Dégénéré : tous les appels rendent le même pair.
    Degenere,
}

impl Biais {
    /// Nom affiché du biais. L'uniforme porte sa mise en garde : c'est
    /// l'hypothèse la plus favorable, et jamais le préréglage par défaut.
    pub fn nom(self) -> &'static str {
        match self {
            Biais::Uniforme => "uniforme — hypothèse la plus favorable, jamais le défaut (RQ10)",
            Biais::Desequilibre => "déséquilibré — le défaut",
            Biais::GroupeParHote { .. } => "groupé par hôte",
            Biais::Degenere => "dégénéré",
        }
    }

    /// EX-A42, NF-14 — les bornes qui supposent un tirage uniforme sont
    /// **effacées** dès que le biais en sort. Pas grisées, pas pointillées :
    /// retirées, y compris quand la mesure est meilleure que la borne effacée.
    pub fn bornes_applicables(self) -> Result<(), String> {
        match self {
            Biais::Uniforme => Ok(()),
            autre => Err(format!(
                "borne effacée : Θ(log n) cycles pour l'agrégation et O(log n) tours pour la \
                 rumeur supposent un **tirage uniforme** du service de pairs, or le biais est « \
                 {} ». Les implantations donnent un flux localement uniforme, mais les hypothèses \
                 usuelles sur l'aléa ne tiennent pas globalement (§4.1). La borne est retirée de \
                 l'affichage, y compris si la mesure est meilleure (NF-14).",
                autre.nom()
            )),
        }
    }
}

/// Le service d'échantillonnage.
pub struct ServiceDePairs {
    /// Taille de la population échantillonnable.
    pub n: u32,
    /// Biais du tirage — un **paramètre à injecter**, jamais une propriété
    /// mesurée sur un système réel (§8.3).
    pub biais: Biais,
    /// Nombre de fois où chaque pair a été rendu. C'est la seule façon de
    /// **constater** le biais ; le service ne le mesure pas pour lui-même.
    tirages: Vec<u64>,
    /// Nombre total d'appels au service.
    pub appels: u64,
}

impl ServiceDePairs {
    /// Service neuf sur `n` agents.
    pub fn nouveau(n: u32, biais: Biais) -> ServiceDePairs {
        ServiceDePairs {
            n,
            biais,
            tirages: vec![0; n as usize],
            appels: 0,
        }
    }

    /// Rend un pair pour l'agent `de`. Jamais lui-même.
    pub fn tirer(&mut self, de: u32, alea: &mut Alea) -> Option<u32> {
        if self.n < 2 {
            return None;
        }
        self.appels += 1;
        let p = match self.biais {
            Biais::Uniforme => {
                let mut j = alea.entier(self.n as u64) as u32;
                if j == de {
                    j = (j + 1) % self.n;
                }
                j
            }
            Biais::Desequilibre => {
                // Loi de puissance grossière : le carré d'un uniforme concentre
                // les tirages sur les premiers indices.
                let u = alea.uniforme();
                let mut j = ((u * u) * self.n as f64) as u32 % self.n;
                if j == de {
                    j = (j + 1) % self.n;
                }
                j
            }
            Biais::GroupeParHote {
                taille_hote,
                p_local,
            } => {
                let hote = de / taille_hote.max(1);
                if alea.bernoulli(p_local) {
                    let base = hote * taille_hote;
                    let etendue = taille_hote.min(self.n.saturating_sub(base)).max(1);
                    let mut j = base + alea.entier(etendue as u64) as u32;
                    if j == de {
                        j = base + (j + 1 - base) % etendue;
                    }
                    j.min(self.n - 1)
                } else {
                    let mut j = alea.entier(self.n as u64) as u32;
                    if j == de {
                        j = (j + 1) % self.n;
                    }
                    j
                }
            }
            Biais::Degenere => {
                if de == 0 {
                    1
                } else {
                    0
                }
            }
        };
        self.tirages[p as usize] += 1;
        Some(p)
    }

    /// Constat du déséquilibre : rapport entre le pair le plus tiré et le
    /// moins tiré. Vaut 1 pour un tirage parfaitement plat.
    ///
    /// C'est une **mesure de l'observateur**, pas une information dont un agent
    /// dispose (§8.3).
    pub fn desequilibre_constate(&self) -> Option<f64> {
        if self.appels == 0 {
            return None;
        }
        let max = *self.tirages.iter().max()? as f64;
        let min = *self.tirages.iter().min()? as f64;
        Some(if min > 0.0 { max / min } else { f64::INFINITY })
    }
}

/// Tri de vue par distance (EX-A18).
///
/// Vue de `c` descripteurs, échange par cycle, conservation des `c` qui
/// minimisent une distance sur un attribut — version de code, zone de
/// déploiement, spécialisation déclarée.
///
/// Mode de défaillance porté par ce mécanisme : la **scission silencieuse**.
/// Deux moitiés cessent de s'échantillonner mutuellement et chacune croit être
/// l'essaim entier, sans qu'aucun agent puisse le détecter.
pub struct TriDeVue {
    /// Taille de la vue conservée par agent.
    pub c: usize,
    /// Attribut de chaque agent — c'est sur lui que porte la distance.
    ///
    /// Lecture seule par [`TriDeVue::attribut`] : il **dimensionne** la table
    /// des vues, et le redimensionner de l'extérieur la laissait derrière lui.
    attribut: Vec<f64>,
    /// Vue de chaque agent.
    vues: Vec<Vec<u32>>,
}

impl TriDeVue {
    /// Vues vides sur une population portant ces attributs.
    pub fn nouveau(attribut: Vec<f64>, c: usize) -> TriDeVue {
        let n = attribut.len();
        TriDeVue {
            c,
            attribut,
            vues: vec![Vec::new(); n],
        }
    }

    /// L'attribut de chaque agent, en lecture seule.
    pub fn attribut(&self) -> &[f64] {
        &self.attribut
    }

    /// La vue de l'agent `i` — ce qu'il croit être son voisinage.
    ///
    /// Rend `None` hors population : un agent qui n'existe pas n'a pas de vue
    /// (SPEC §7, clause 4).
    pub fn vue(&self, i: u32) -> Option<&[u32]> {
        self.vues.get(i as usize).map(|v| v.as_slice())
    }

    fn distance(&self, i: u32, j: u32) -> f64 {
        (self.attribut[i as usize] - self.attribut[j as usize]).abs()
    }

    /// Un cycle : chaque agent échange sa vue avec un pair, puis conserve les
    /// `c` descripteurs les plus proches au sens de l'attribut.
    ///
    /// Le service de pairs a **sa propre** population : un identifiant qu'il
    /// rend au-delà de celle-ci désigne un agent sans attribut ni vue, et il est
    /// écarté comme un tirage sans réponse (SPEC §7, clause 4). C'est ce qui
    /// garantit que toute entrée de `vues` reste un agent de la population, donc
    /// que [`TriDeVue::scission_silencieuse`] peut l'indexer sans garde.
    pub fn cycle(&mut self, service: &mut ServiceDePairs, alea: &mut Alea) {
        let n = self.attribut.len() as u32;
        for i in 0..n {
            let pair = match service.tirer(i, alea).filter(|p| *p < n) {
                Some(p) => p,
                None => continue,
            };
            let mut candidats: Vec<u32> = self.vues[i as usize].clone();
            candidats.push(pair);
            candidats.extend_from_slice(&self.vues[pair as usize]);
            candidats.retain(|j| *j != i);
            candidats.sort_unstable();
            candidats.dedup();
            candidats.sort_by(|a, b| {
                // `total_cmp` et non `partial_cmp(…).unwrap_or(Equal)` : sur un
                // `NaN`, ce dernier rend un ordre **non transitif**, donc un
                // résultat de tri qui dépend du parcours de l'algorithme — la
                // définition même de ce que PD1 interdit.
                self.distance(i, *a)
                    .total_cmp(&self.distance(i, *b))
                    // Départage stable par identifiant : sans lui, l'ordre
                    // dépendrait de l'algorithme de tri (PD1).
                    .then(a.cmp(b))
            });
            candidats.truncate(self.c);
            self.vues[i as usize] = candidats;
        }
    }

    /// **Scission silencieuse** — les vues se sont-elles refermées sur des
    /// groupes disjoints ?
    ///
    /// C'est un privilège de l'observateur : aucun agent ne peut le constater,
    /// et l'interface doit le dire (PD10, §8.3).
    pub fn scission_silencieuse(&self) -> Option<String> {
        let n = self.attribut.len();
        // Sans population, il n'y a pas de médiane à prendre : `tri[n/2]`
        // sortait des bornes. Aucune scission n'est constatable non plus.
        if n == 0 {
            return None;
        }
        // Deux moitiés par l'attribut : la scission se lit si aucune vue ne
        // traverse la frontière.
        let mediane = {
            let mut tri = self.attribut.clone();
            // Ordre **total** : voir [`TriDeVue::cycle`] (PD1).
            tri.sort_by(|a, b| a.total_cmp(b));
            tri[n / 2]
        };
        let cote = |i: usize| self.attribut[i] >= mediane;
        let traversees = (0..n)
            .flat_map(|i| self.vues[i].iter().map(move |j| (i, *j as usize)))
            .filter(|(i, j)| cote(*i) != cote(*j))
            .count();
        if traversees == 0 && self.vues.iter().any(|v| !v.is_empty()) {
            Some(
                "scission silencieuse : aucune vue ne traverse la frontière d'attribut. Chaque \
                 moitié croit être l'essaim entier, et **aucun agent ne peut le détecter** — seul \
                 l'observateur le voit (§4.1, PD10)."
                    .to_string(),
            )
        } else {
            None
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// RQ10 — le défaut **n'est pas** l'uniforme parfait.
    #[test]
    fn le_defaut_nest_pas_luniforme_parfait() {
        assert_eq!(Biais::default(), Biais::Desequilibre);
        assert!(Biais::Uniforme.nom().contains("jamais le défaut"));
    }

    /// EX-A17 — le biais déséquilibré se constate : certains pairs sont tirés
    /// bien plus souvent que d'autres.
    #[test]
    fn le_biais_desequilibre_se_constate() {
        let mut alea = Alea::nouveau(1);
        let mut uniforme = ServiceDePairs::nouveau(64, Biais::Uniforme);
        let mut desequilibre = ServiceDePairs::nouveau(64, Biais::Desequilibre);
        // On tire depuis tous les agents : sinon le tireur lui-même n'est jamais
        // rendu, son compte reste à zéro, et le rapport est infini pour une
        // raison qui n'a rien à voir avec le biais.
        for k in 0..20_000u32 {
            let de = k % 64;
            uniforme.tirer(de, &mut alea);
            desequilibre.tirer(de, &mut alea);
        }
        let u = uniforme.desequilibre_constate().unwrap();
        let d = desequilibre.desequilibre_constate().unwrap();
        assert!(u < 2.0, "l'uniforme doit être plat, rapport {u}");
        assert!(d > 5.0, "le déséquilibré doit concentrer, rapport {d}");
    }

    /// EX-A42, NF-14 — dès que le biais quitte l'uniforme, les bornes sont
    /// **effacées**, pas atténuées.
    #[test]
    fn hors_uniforme_les_bornes_sont_effacees() {
        assert!(Biais::Uniforme.bornes_applicables().is_ok());
        let e = Biais::Desequilibre.bornes_applicables().unwrap_err();
        assert!(e.contains("borne effacée"), "{e}");
        assert!(e.contains("NF-14"), "{e}");
        assert!(e.contains("y compris si la mesure est meilleure"), "{e}");
    }

    /// Un agent ne se tire jamais lui-même.
    #[test]
    fn un_agent_ne_se_tire_jamais_lui_meme() {
        let mut alea = Alea::nouveau(2);
        for biais in [
            Biais::Uniforme,
            Biais::Desequilibre,
            Biais::GroupeParHote {
                taille_hote: 8,
                p_local: 0.9,
            },
            Biais::Degenere,
        ] {
            let mut s = ServiceDePairs::nouveau(32, biais);
            for de in 0..32u32 {
                for _ in 0..50 {
                    assert_ne!(s.tirer(de, &mut alea), Some(de), "biais {biais:?}");
                }
            }
        }
    }

    /// EX-A17 — le groupement par hôte referme le graphe d'échange sur des
    /// grappes.
    #[test]
    fn le_groupement_par_hote_referme_le_graphe() {
        let mut alea = Alea::nouveau(3);
        let mut s = ServiceDePairs::nouveau(
            64,
            Biais::GroupeParHote {
                taille_hote: 8,
                p_local: 0.95,
            },
        );
        let mut locaux = 0;
        for _ in 0..5_000 {
            if let Some(p) = s.tirer(3, &mut alea) {
                if p < 8 {
                    locaux += 1;
                }
            }
        }
        assert!(locaux > 4_000, "{locaux} tirages dans l'hôte sur 5 000");
    }

    /// EX-A18 — le tri de vue conserve les c plus proches, et il est
    /// déterministe.
    #[test]
    fn le_tri_de_vue_conserve_les_c_plus_proches() {
        let attribut: Vec<f64> = (0..32).map(|i| i as f64).collect();
        let mut t = TriDeVue::nouveau(attribut, 4);
        let mut s = ServiceDePairs::nouveau(32, Biais::Uniforme);
        let mut alea = Alea::nouveau(4);
        for _ in 0..60 {
            t.cycle(&mut s, &mut alea);
        }
        // La vue de l'agent 16 doit être peuplée de ses voisins d'attribut.
        let vue = t.vue(16).expect("l'agent 16 est dans la population");
        assert!(!vue.is_empty());
        assert!(vue.len() <= 4);
        let ecart_max = vue.iter().map(|j| (*j as i64 - 16).abs()).max().unwrap();
        assert!(ecart_max <= 6, "vue {vue:?} trop éloignée");
        assert_eq!(t.vue(32), None, "hors population, aucune vue");
    }

    /// SPEC §7, clause 4 — une population vide faisait sortir
    /// `scission_silencieuse` des bornes de sa médiane, et un **service de pairs
    /// plus grand** que la population fait entrer dans les vues des agents qui
    /// n'existent pas ici. `attribut` n'est plus public : le désaligner de la
    /// table des vues n'est plus exprimable.
    #[test]
    fn une_population_vide_ou_plus_petite_que_le_service_ne_panique_pas() {
        let vide = TriDeVue::nouveau(Vec::new(), 3);
        assert_eq!(vide.scission_silencieuse(), None);
        assert_eq!(vide.vue(0), None);

        let mut t = TriDeVue::nouveau(vec![0.0, 1.0, 2.0], 3);
        let mut s = ServiceDePairs::nouveau(64, Biais::Uniforme);
        let mut alea = Alea::nouveau(6);
        for _ in 0..20 {
            t.cycle(&mut s, &mut alea);
        }
        assert_eq!(t.attribut().len(), 3, "la population reste celle du mécanisme");
        assert_eq!(t.vue(3), None, "hors population, aucune vue");
        // Aucune vue ne porte un agent que la population n'a pas : c'est
        // l'invariant qui rend `scission_silencieuse` indexable sans garde.
        for i in 0..3u32 {
            for j in t.vue(i).unwrap() {
                assert!((*j as usize) < t.attribut().len(), "vue hors population : {j}");
            }
        }
        let _ = t.scission_silencieuse();
    }

    /// EX-A18, PD10 — la **scission silencieuse** est provocable, et seul
    /// l'observateur la voit.
    #[test]
    fn le_tri_de_vue_produit_une_scission_silencieuse() {
        // Deux groupes d'attributs très éloignés : le tri les sépare.
        let attribut: Vec<f64> = (0..32)
            .map(|i| if i < 16 { i as f64 } else { 1_000.0 + i as f64 })
            .collect();
        let mut t = TriDeVue::nouveau(attribut, 3);
        let mut s = ServiceDePairs::nouveau(32, Biais::Uniforme);
        let mut alea = Alea::nouveau(5);
        for _ in 0..100 {
            t.cycle(&mut s, &mut alea);
        }
        let avis = t.scission_silencieuse().expect("les vues doivent s'être refermées");
        assert!(avis.contains("aucun agent ne peut le détecter"), "{avis}");
    }
}
