//! Graphe de communication (EX-C16).
//!
//! > Le graphe de communication est un **objet du modèle** : orienté et
//! > asymétrique par défaut, à voisinage variable d'un tour à l'autre. (§5.1 du traité)
//!
//! Trois décisions que ce module tient, et dont chacune contredit une commodité
//! répandue :
//!
//! - **Orienté et asymétrique par défaut.** Un graphe non orienté est un cas
//!   particulier, pas le cas normal : que i voie j n'oblige pas j à voir i.
//! - **Le retrait d'arêtes est corrélé.** La saturation d'un courtier supprime
//!   d'un coup tous les liens qui le traversent. Retirer les arêtes
//!   indépendamment produirait une avarie que rien ne produit en pratique.
//! - **La connexité conjointe est vérifiée *a posteriori*** sur une fenêtre
//!   glissante, et rapportée comme **constat d'exécution** — jamais comme
//!   hypothèse satisfaite par construction. Un graphe conjointement connexe en
//!   espérance peut être déconnecté dans la réalisation, et la preuve ne s'en
//!   aperçoit pas (§4.2).

use crate::alea::Alea;
use std::collections::BTreeSet;

/// Le graphe d'un tour.
#[derive(Clone, Debug)]
pub struct Graphe {
    n: u32,
    /// `arcs[i]` = successeurs de i. Ordonnés (PD1).
    arcs: Vec<Vec<u32>>,
}

impl Graphe {
    /// Graphe à `n` sommets et aucun arc.
    pub fn vide(n: u32) -> Graphe {
        Graphe {
            n,
            arcs: vec![Vec::new(); n as usize],
        }
    }

    /// Nombre de sommets.
    pub fn n(&self) -> u32 {
        self.n
    }

    /// Successeurs de `i`, triés. L'ordre est stable d'une exécution à l'autre.
    ///
    /// # Panics
    ///
    /// Si `i >= n`.
    pub fn voisins(&self, i: u32) -> &[u32] {
        &self.arcs[i as usize]
    }

    /// Ajoute l'arc `de → vers`. Les boucles et les doublons sont ignorés.
    ///
    /// # Panics
    ///
    /// Si `de >= n`.
    pub fn ajouter(&mut self, de: u32, vers: u32) {
        if de != vers && !self.arcs[de as usize].contains(&vers) {
            self.arcs[de as usize].push(vers);
            self.arcs[de as usize].sort_unstable();
        }
    }

    /// Degré **sortant** maximal Δ(G). C'est lui qui borne le pas α de
    /// l'itération linéaire (EX-A13) : dans `x_i ← x_i + α Σ_{j ∈ voisins(i)}
    /// (x_j − x_i)`, la somme court sur les successeurs de `i`, donc c'est leur
    /// nombre qui borne α.
    pub fn degre_max(&self) -> u32 {
        (0..self.n)
            .map(|i| self.arcs[i as usize].len() as u32)
            .max()
            .unwrap_or(0)
    }

    /// Vrai si le graphe est **équilibré** : chaque sommet a autant d'arcs
    /// entrants que sortants. C'est la condition qui rend la moyenne initiale
    /// invariante (EX-A43, mode (b)).
    pub fn equilibre(&self) -> bool {
        let mut entrants = vec![0u32; self.n as usize];
        for i in 0..self.n {
            for j in &self.arcs[i as usize] {
                entrants[*j as usize] += 1;
            }
        }
        (0..self.n).all(|i| entrants[i as usize] == self.arcs[i as usize].len() as u32)
    }

    /// Composantes faiblement connexes, comme ensembles ordonnés.
    pub fn composantes(&self) -> Vec<BTreeSet<u32>> {
        let mut vus = vec![false; self.n as usize];
        let mut sortie = Vec::new();
        for depart in 0..self.n {
            if vus[depart as usize] {
                continue;
            }
            let mut composante = BTreeSet::new();
            let mut pile = vec![depart];
            while let Some(i) = pile.pop() {
                if vus[i as usize] {
                    continue;
                }
                vus[i as usize] = true;
                composante.insert(i);
                for j in &self.arcs[i as usize] {
                    pile.push(*j);
                }
                // Le lien inverse compte pour la connexité **faible**.
                for j in 0..self.n {
                    if self.arcs[j as usize].contains(&i) {
                        pile.push(j);
                    }
                }
            }
            sortie.push(composante);
        }
        sortie
    }

    /// Vrai si le graphe est **faiblement** connexe — une seule composante une
    /// fois l'orientation oubliée. Un graphe vide (n = 0) l'est par convention :
    /// il n'a aucune paire à séparer.
    ///
    /// Ce n'est **pas** la condition de propagation : `0 → 1, 0 → 2` est
    /// faiblement connexe, et pourtant rien ne revient de 1 vers 0. Pour cela,
    /// voir [`Graphe::fortement_connexe`].
    pub fn connexe(&self) -> bool {
        self.composantes().len() <= 1
    }

    /// Vrai si le graphe est **fortement** connexe : de tout sommet, tout autre
    /// est atteignable en suivant le sens des arcs.
    ///
    /// C'est la condition qu'exige la connexité conjointe d'EX-C16 — un
    /// digraphe où l'information ne peut pas revenir n'est pas un support de
    /// propagation, quelle que soit sa connexité faible.
    pub fn fortement_connexe(&self) -> bool {
        if self.n <= 1 {
            return true;
        }
        let atteint = |suivants: &dyn Fn(u32) -> Vec<u32>| -> usize {
            let mut vus = vec![false; self.n as usize];
            let mut pile = vec![0u32];
            let mut compte = 0;
            while let Some(i) = pile.pop() {
                if vus[i as usize] {
                    continue;
                }
                vus[i as usize] = true;
                compte += 1;
                pile.extend(suivants(i));
            }
            compte
        };
        let avant = atteint(&|i: u32| self.arcs[i as usize].clone());
        let arriere = atteint(&|i: u32| {
            (0..self.n)
                .filter(|j| self.arcs[*j as usize].contains(&i))
                .collect()
        });
        avant == self.n as usize && arriere == self.n as usize
    }
}

/// Un domaine de panne partagé : la saturation d'un courtier retire d'un coup
/// tous les liens qui le traversent.
#[derive(Clone, Debug)]
pub struct Courtier {
    /// Agents dont le trafic passe par ce courtier.
    pub membres: Vec<u32>,
    /// Probabilité que le courtier soit saturé à un tour donné.
    pub p_saturation: f64,
}

/// Générateur de graphes : produit un graphe par tour et tient le constat de
/// connexité conjointe.
pub struct Generateur {
    /// Nombre de sommets des graphes produits.
    pub n: u32,
    /// Degré sortant visé.
    pub degre: u32,
    /// Courtiers, dont la saturation retire des arêtes **de façon corrélée**.
    pub courtiers: Vec<Courtier>,
    /// Fenêtre glissante sur laquelle la connexité conjointe est constatée.
    pub fenetre: usize,
    /// Union des graphes de la fenêtre.
    historique: Vec<Graphe>,
    /// Tours où la connexité conjointe n'a **pas** été constatée.
    pub tours_sans_connexite_conjointe: u64,
    /// Tours produits depuis le début.
    pub tours: u64,
}

impl Generateur {
    /// Générateur sans courtier : les arêtes tombent indépendamment.
    pub fn nouveau(n: u32, degre: u32, fenetre: usize) -> Generateur {
        Generateur {
            n,
            degre,
            courtiers: Vec::new(),
            fenetre,
            historique: Vec::new(),
            tours_sans_connexite_conjointe: 0,
            tours: 0,
        }
    }

    /// Tire le graphe du tour.
    pub fn tour(&mut self, alea: &mut Alea) -> Graphe {
        // Quels courtiers sont saturés à ce tour ?
        let satures: Vec<usize> = (0..self.courtiers.len())
            .filter(|k| alea.bernoulli(self.courtiers[*k].p_saturation))
            .collect();

        let mut g = Graphe::vide(self.n);
        for i in 0..self.n {
            for _ in 0..self.degre {
                let j = alea.entier(self.n as u64) as u32;
                if j == i {
                    continue;
                }
                // Le lien tombe si un courtier saturé porte les deux extrémités.
                let coupe = satures.iter().any(|k| {
                    let m = &self.courtiers[*k].membres;
                    m.contains(&i) && m.contains(&j)
                });
                if !coupe {
                    g.ajouter(i, j);
                }
            }
        }

        self.tours += 1;
        self.historique.push(g.clone());
        if self.historique.len() > self.fenetre {
            self.historique.remove(0);
        }
        if !self.connexite_conjointe() {
            self.tours_sans_connexite_conjointe += 1;
        }
        g
    }

    /// Union des graphes de la fenêtre : c'est sur elle que la connexité
    /// conjointe se constate.
    pub fn union_de_la_fenetre(&self) -> Graphe {
        let mut u = Graphe::vide(self.n);
        for g in &self.historique {
            for i in 0..self.n {
                for j in g.voisins(i) {
                    u.ajouter(i, *j);
                }
            }
        }
        u
    }

    /// **Constat d'exécution**, jamais hypothèse. Le nom de la méthode le dit,
    /// et le rapport ci-dessous le répète.
    ///
    /// La connexité exigée est la **forte** : sur l'union de la fenêtre, tout
    /// sommet doit atteindre tout autre en suivant le sens des arcs. La faible
    /// rendrait le constat plus favorable qu'il n'est — un digraphe où
    /// l'information part sans revenir serait compté connexe.
    pub fn connexite_conjointe(&self) -> bool {
        self.union_de_la_fenetre().fortement_connexe()
    }

    /// Rapport à afficher (EX-C16).
    pub fn constat(&self) -> String {
        if self.tours == 0 {
            return "aucun tour exécuté".to_string();
        }
        format!(
            "connexité conjointe sur une fenêtre de {} tours : constatée à {} tour(s) sur {} — \
             c'est un **constat d'exécution**, jamais une hypothèse satisfaite par construction. \
             Un graphe conjointement connexe en espérance peut être déconnecté dans la \
             réalisation, et la preuve ne s'en aperçoit pas (§4.2, EX-C16).",
            self.fenetre,
            self.tours - self.tours_sans_connexite_conjointe,
            self.tours
        )
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-C16 — le graphe est **orienté et asymétrique** par défaut : que i voie
    /// j n'oblige pas j à voir i.
    #[test]
    fn le_graphe_est_oriente_et_asymetrique() {
        let mut gen = Generateur::nouveau(64, 3, 5);
        let mut alea = Alea::nouveau(1);
        let g = gen.tour(&mut alea);
        let mut asymetries = 0;
        for i in 0..64u32 {
            for j in g.voisins(i) {
                if !g.voisins(*j).contains(&i) {
                    asymetries += 1;
                }
            }
        }
        assert!(asymetries > 0, "un graphe systématiquement symétrique n'est pas orienté");
    }

    /// Le voisinage **change d'un tour à l'autre**.
    #[test]
    fn le_voisinage_varie_dun_tour_a_lautre() {
        let mut gen = Generateur::nouveau(32, 3, 5);
        let mut alea = Alea::nouveau(2);
        let a = gen.tour(&mut alea);
        let b = gen.tour(&mut alea);
        let differe = (0..32u32).any(|i| a.voisins(i) != b.voisins(i));
        assert!(differe);
    }

    /// EX-C16 — le retrait d'arêtes est **corrélé** : un courtier saturé emporte
    /// tous les liens qui le traversent, d'un coup.
    #[test]
    fn la_saturation_dun_courtier_retire_les_liens_correles() {
        let mut gen = Generateur::nouveau(16, 8, 3);
        // Deux moitiés, chacune derrière son courtier ; celui de la première
        // est saturé en permanence.
        gen.courtiers.push(Courtier {
            membres: (0..8).collect(),
            p_saturation: 1.0,
        });
        let mut alea = Alea::nouveau(3);
        let g = gen.tour(&mut alea);
        // Aucun lien interne à la première moitié.
        for i in 0..8u32 {
            for j in g.voisins(i) {
                assert!(*j >= 8, "le lien {i} → {j} traverse un courtier saturé");
            }
        }
        // Les liens de la seconde moitié, eux, subsistent.
        assert!((8..16u32).any(|i| !g.voisins(i).is_empty()));
    }

    /// EX-C16 — la connexité conjointe est un **constat**, et le rapport le dit
    /// en toutes lettres.
    #[test]
    fn la_connexite_conjointe_est_un_constat_pas_une_hypothese() {
        let mut gen = Generateur::nouveau(32, 4, 10);
        let mut alea = Alea::nouveau(4);
        for _ in 0..40 {
            gen.tour(&mut alea);
        }
        let c = gen.constat();
        assert!(c.contains("constat d'exécution"), "{c}");
        assert!(c.contains("jamais une hypothèse"), "{c}");
    }

    /// Un courtier saturé couvrant **toute** la population désagrège l'essaim :
    /// un lien tombe dès qu'un courtier saturé porte ses deux extrémités, donc
    /// aucun ne survit et la connexité conjointe ne revient jamais.
    ///
    /// L'assertion sur le graphe vide est là exprès. Ce test s'appelait
    /// « deux moitiés isolées » et n'installait qu'un courtier sur les seize
    /// sommets : il passait pour seize composantes singleton, pas pour deux
    /// moitiés — une raison différente de celle qu'il annonçait. Nommer la
    /// vraie raison est la seule façon de ne pas le refaire.
    #[test]
    fn un_courtier_saturé_sur_toute_la_population_desagrege_lessaim() {
        let mut gen = Generateur::nouveau(16, 15, 20);
        gen.courtiers.push(Courtier {
            membres: (0..16).collect(),
            p_saturation: 1.0,
        });
        let mut alea = Alea::nouveau(5);
        for _ in 0..20 {
            gen.tour(&mut alea);
        }
        let u = gen.union_de_la_fenetre();
        assert!(
            (0..16).all(|i| u.voisins(i).is_empty()),
            "le mécanisme est la désagrégation totale, pas une coupe en deux"
        );
        assert_eq!(u.composantes().len(), 16);
        assert!(!gen.connexite_conjointe());
        assert_eq!(gen.tours_sans_connexite_conjointe, 20);
    }

    /// Deux courtiers **disjoints** ne coupent pas l'essaim en deux : ils
    /// suppriment les liens internes à chaque moitié et laissent passer ceux qui
    /// traversent la coupe.
    ///
    /// Conséquence utile, et contre-intuitive : la connexité conjointe **tient**
    /// sur l'union, par les seuls liens croisés. Le modèle de courtier ne sait
    /// donc pas exprimer « deux moitiés internement connexes et mutuellement
    /// isolées » — il faudrait un domaine portant la coupe, qui porterait du
    /// même coup son intérieur.
    #[test]
    fn deux_courtiers_disjoints_laissent_passer_les_liens_croises() {
        let mut gen = Generateur::nouveau(16, 15, 20);
        gen.courtiers.push(Courtier {
            membres: (0..8).collect(),
            p_saturation: 1.0,
        });
        gen.courtiers.push(Courtier {
            membres: (8..16).collect(),
            p_saturation: 1.0,
        });
        let mut alea = Alea::nouveau(5);
        for _ in 0..20 {
            gen.tour(&mut alea);
        }
        let u = gen.union_de_la_fenetre();
        let arcs: Vec<(u32, u32)> = (0..16)
            .flat_map(|i| u.voisins(i).iter().map(move |j| (i, *j)))
            .collect();
        assert!(!arcs.is_empty());
        assert!(
            arcs.iter().all(|(i, j)| (*i < 8) != (*j < 8)),
            "seuls les liens croisés survivent : {arcs:?}"
        );
        assert!(
            gen.connexite_conjointe(),
            "les liens croisés suffisent à la connexité forte de l'union"
        );
    }

    /// La connexité forte n'est pas la faible, et c'est la forte qu'EX-C16
    /// constate : `0 → 1, 0 → 2` est faiblement connexe et ne fait rien revenir.
    #[test]
    fn la_connexite_forte_refuse_ce_que_la_faible_accepte() {
        let mut g = Graphe::vide(3);
        g.ajouter(0, 1);
        g.ajouter(0, 2);
        assert!(g.connexe(), "faiblement connexe");
        assert!(!g.fortement_connexe(), "rien ne revient vers 0");

        g.ajouter(1, 0);
        g.ajouter(2, 0);
        assert!(g.fortement_connexe());
    }

    /// Δ(G) et l'équilibre sont les deux grandeurs dont EX-A13 et EX-A43
    /// dépendent.
    #[test]
    fn le_degre_max_et_lequilibre_se_mesurent() {
        let mut g = Graphe::vide(3);
        g.ajouter(0, 1);
        g.ajouter(1, 2);
        g.ajouter(2, 0);
        assert_eq!(g.degre_max(), 1);
        assert!(g.equilibre(), "le cycle orienté est équilibré");
        assert!(g.connexe());

        g.ajouter(0, 2);
        assert!(!g.equilibre(), "0 a deux sortants et un entrant");
        // Sur un cycle, entrant = sortant : il faut un sommet déséquilibré pour
        // que Δ(G) départage les deux lectures. C'est le **sortant**, celui qui
        // borne la somme de l'itération linéaire.
        assert_eq!(g.degre_max(), 2, "degré sortant de 0, non son degré entrant");
    }
}
