//! **§3.1, algorithme 1 du ch. 3** — itération de consensus linéaire sur digraphe
//! (EX-A13), et ses quatre modes de défaillance (EX-A43).
//!
//! `x_i(k+1) = x_i(k) + α Σ_j a_ij (x_j(k) − x_i(k))`, avec `0 < α < 1/Δ(G)`.
//!
//! **Modèle de panne vide, synchronisme parfait** — les deux sont affichés en
//! permanence, parce qu'ils sont l'inverse de ceux du reste du produit. C'est
//! le seul mécanisme du périmètre qui ne tolère rien.
//!
//! La convergence est garantie **sans borne de temps** : une vivacité au sens
//! strict, affichée comme telle et **jamais convertie en délai**.
//!
//! ## Pourquoi aucune barre de progression
//!
//! Le traité établit par programmation semi-définie qu'il n'existe pas de
//! fonction de Lyapunov quadratique commune pour cette classe : rien ne mesure
//! « la distance restant à parcourir ». L'exception est double et nommée — sur
//! digraphes équilibrés fortement connexes commutant arbitrairement, le carré
//! de la norme du désaccord **est** une fonction de Lyapunov commune, et la
//! vitesse est minorée par la plus petite connectivité algébrique rencontrée.
//! Là seulement une barre est permise, et elle porte cette minoration.

use sim_core::graphe::Graphe;

/// Signature du mécanisme, affichée sans repli (EX-V07, PD8).
pub const SIGNATURE: &[(&str, &str)] = &[
    ("modèle de panne", "**vide** — ce mécanisme ne tolère aucune panne"),
    ("synchronisme", "**parfait** — tours globaux, aucun retard"),
    ("coût", "Θ(n·d̄) messages par tour"),
    (
        "condition d'arrêt",
        "écart < ε sur R tours — critère **local**, donc heuristique (PD10)",
    ),
    (
        "convergence",
        "garantie **sans borne de temps** : vivacité au sens strict, jamais convertie en délai",
    ),
];

/// Les quatre modes du §3.1, plus la discussion de transposition.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Mode {
    /// Nominal : α < 1/Δ(G), digraphe équilibré, aucun retard, aucun crash.
    Nominal,
    /// (a) « Pas trop grand » : α = 1/Δ(G). Le traité note que l'erreur est
    /// répétée dans la littérature antérieure ; le préréglage la reproduit.
    PasTropGrand,
    /// (b) « Digraphe non équilibré » : la limite est pondérée par la
    /// **topologie**, non par les données.
    DigrapheNonEquilibre,
    /// (c) « Retard » : τ ≥ π/(2·ν_n). La condition est **nécessaire et
    /// suffisante**, pas seulement suffisante.
    Retard,
    /// (d) « Mort ou convergé » : crash-arrêt d'un voisin publiant. Le
    /// crash-arrêt est **hors du modèle de panne** de cet algorithme.
    MortOuConverge,
    /// « Moyeu » — **ne correspond à aucun mode du traité** : c'est la
    /// discussion de transposition, et l'étiquette le dit.
    Moyeu,
}

impl Mode {
    /// Étiquette du mode, avec le renvoi au traité quand il y en a un — et la
    /// mention explicite quand il n'y en a pas.
    pub fn etiquette(self) -> &'static str {
        match self {
            Mode::Nominal => "nominal",
            Mode::PasTropGrand => "(a) pas trop grand — α = 1/Δ(G)",
            Mode::DigrapheNonEquilibre => "(b) digraphe non équilibré",
            Mode::Retard => "(c) retard — τ ≥ π/(2·ν_n)",
            Mode::MortOuConverge => "(d) mort ou convergé — crash-arrêt hors modèle",
            Mode::Moyeu => {
                "« moyeu » — discussion de transposition, ne correspond à AUCUN mode du traité"
            }
        }
    }

    /// Avertissement affiché au moment de l'activation, quand il y a lieu.
    pub fn avertissement(self) -> Option<&'static str> {
        match self {
            Mode::MortOuConverge => Some(
                "le crash-arrêt est HORS du modèle de panne de cet algorithme, dont le modèle est \
                 vide. Ce que le préréglage montre n'est pas une faiblesse de l'algorithme mais \
                 ce qui arrive quand on l'emploie hors de ses hypothèses (§3.1, mode (d)).",
            ),
            Mode::Moyeu => Some(
                "topologie de sujet lu par tous : Δ(G) = n − 1, et le budget de retard \
                 τ < π/(4(n−1)) décroît en 1/n — 7,933 × 10⁻³ unité de temps du protocole à \
                 n = 100. L'arrondi de π/(4n) donnerait 7,9 × 10⁻³, que la borne réellement \
                 écrite dépasse de 0,42 % : un arrondi présenté comme une borne stricte est un \
                 énoncé faux, non une imprécision (§3.1, p. 42). Le milieu offre gratuitement \
                 l'échange non local qui accélère la convergence, et du même geste la topologie \
                 que la source déconseille.",
            ),
            _ => None,
        }
    }
}

/// L'itération.
pub struct Iteration {
    /// État courant de chaque agent.
    pub x: Vec<f64>,
    /// États initiaux : leur enveloppe convexe borne la valeur de groupe.
    pub x0: Vec<f64>,
    /// Mode actif — c'est lui qui décide des hypothèses en vigueur.
    pub mode: Mode,
    /// Pas α.
    pub alpha: f64,
    /// Agents arrêtés — ils cessent de publier, et leurs voisins lisent un état
    /// figé.
    arretes: Vec<bool>,
    /// Tours écoulés.
    pub tours: u64,
    /// Écart maximal observé au tour précédent, pour le critère local.
    dernier_ecart: f64,
    /// Tours consécutifs sous ε.
    tours_sous_epsilon: u32,
}

impl Iteration {
    /// Construit l'itération. `alpha_facteur` multiplie 1/Δ(G) : 0,5 en
    /// nominal, 1,0 pour le mode (a).
    pub fn nouvelle(x0: Vec<f64>, g: &Graphe, mode: Mode, alpha_facteur: f64) -> Iteration {
        let delta = g.degre_max().max(1) as f64;
        Iteration {
            arretes: vec![false; x0.len()],
            x: x0.clone(),
            x0,
            mode,
            alpha: alpha_facteur / delta,
            tours: 0,
            dernier_ecart: f64::INFINITY,
            tours_sous_epsilon: 0,
        }
    }

    /// Arrête un agent : il cesse de publier, et son état reste figé.
    pub fn arreter(&mut self, i: usize) {
        if i < self.arretes.len() {
            self.arretes[i] = true;
        }
    }

    /// Un tour.
    ///
    /// Les poids `a_ij` valent 1 en régime nominal — le digraphe est alors
    /// équilibré et la moyenne initiale est invariante. Sous le mode (b), ils
    /// sont asymétriques, et la limite se met à dépendre de la topologie.
    pub fn tour(&mut self, g: &Graphe) {
        let anciens = self.x.clone();
        for i in 0..self.x.len() {
            if self.arretes[i] {
                // L'agent mort ne bouge plus. Ses voisins liront cet état figé,
                // et c'est ce qui fait confondre mort et convergence.
                continue;
            }
            let mut somme = 0.0;
            for j in g.voisins(i as u32) {
                let poids = match self.mode {
                    // Poids asymétrique : dépend du couple, donc la matrice
                    // n'est plus doublement stochastique.
                    Mode::DigrapheNonEquilibre => 1.0 + 0.5 * ((i + *j as usize) % 3) as f64,
                    _ => 1.0,
                };
                somme += poids * (anciens[*j as usize] - anciens[i]);
            }
            self.x[i] = anciens[i] + self.alpha * somme;
        }
        self.tours += 1;

        let ecart = self.ecart();
        if ecart < self.dernier_ecart {
            self.dernier_ecart = ecart;
        }
    }

    /// Écart maximal entre états — la dispersion.
    pub fn ecart(&self) -> f64 {
        let max = self.x.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
        let min = self.x.iter().cloned().fold(f64::INFINITY, f64::min);
        max - min
    }

    /// Moyenne initiale. C'est elle que le régime nominal préserve, et que le
    /// mode (b) abandonne.
    pub fn moyenne_initiale(&self) -> f64 {
        self.x0.iter().sum::<f64>() / self.x0.len() as f64
    }

    /// Limite atteinte, approchée par la moyenne courante.
    pub fn limite(&self) -> f64 {
        self.x.iter().sum::<f64>() / self.x.len() as f64
    }

    /// **Enveloppe convexe des états initiaux.** Sous le mode (b), la valeur de
    /// groupe reste **indéterminée** à l'intérieur : l'interface affiche les
    /// trois grandeurs ensemble, jamais la limite seule.
    pub fn enveloppe_initiale(&self) -> (f64, f64) {
        (
            self.x0.iter().cloned().fold(f64::INFINITY, f64::min),
            self.x0.iter().cloned().fold(f64::NEG_INFINITY, f64::max),
        )
    }

    /// Critère **local** d'arrêt : écart < ε sur R tours consécutifs.
    ///
    /// PD10 : ce prédicat paraît dire « le consensus est atteint ». Sous le mode
    /// (d), il est satisfait alors qu'un agent est mort et que ses voisins
    /// lisent un état figé.
    pub fn critere_local(&mut self, epsilon: f64, r: u32) -> bool {
        if self.ecart() < epsilon {
            self.tours_sous_epsilon += 1;
        } else {
            self.tours_sous_epsilon = 0;
        }
        self.tours_sous_epsilon >= r
    }

    /// EX-A43 — aucun scalaire monotone de progression n'est affiché, **sauf**
    /// dans l'exception nommée : digraphe équilibré fortement connexe.
    ///
    /// Rend `None` hors de l'exception. C'est un refus, pas une lacune.
    pub fn progression(&self, g: &Graphe) -> Option<f64> {
        if !(g.equilibre() && g.connexe()) {
            return None;
        }
        let (bas, haut) = self.enveloppe_initiale();
        let etendue = haut - bas;
        if etendue <= 0.0 {
            return Some(1.0);
        }
        Some((1.0 - self.ecart() / etendue).clamp(0.0, 1.0))
    }

    /// Libellé du refus, quand la progression n'est pas disponible.
    pub const REFUS_PROGRESSION: &'static str =
        "aucune barre de progression : le traité établit par programmation semi-définie qu'il \
         n'existe pas de fonction de Lyapunov quadratique commune pour cette classe. Rien ne \
         mesure la distance restant à parcourir (§3.1).";

    /// Ce que l'interface affiche pour ce mécanisme — les trois grandeurs
    /// ensemble quand la limite n'est pas la moyenne initiale (EX-A43, mode b).
    pub fn affichage(&self) -> Vec<(&'static str, String)> {
        let (bas, haut) = self.enveloppe_initiale();
        vec![
            ("limite atteinte", format!("{:.6}", self.limite())),
            ("moyenne initiale", format!("{:.6}", self.moyenne_initiale())),
            (
                "enveloppe convexe des états initiaux",
                format!(
                    "[{bas:.6}, {haut:.6}] — la valeur de groupe y reste **indéterminée** quand \
                     le digraphe n'est pas équilibré"
                ),
            ),
            ("écart courant", format!("{:.9}", self.ecart())),
            ("tours", format!("{}", self.tours)),
        ]
    }
}

/// Budget de retard : τ < π/(4·Δ(G)) (EX-A43, mode (c)).
pub fn budget_de_retard(delta: u32) -> f64 {
    std::f64::consts::PI / (4.0 * delta.max(1) as f64)
}

#[cfg(test)]
mod tests {
    use super::*;
    use sim_core::alea::Alea;
    use sim_core::graphe::Generateur;

    fn cycle(n: u32) -> Graphe {
        let mut g = Graphe::vide(n);
        for i in 0..n {
            g.ajouter(i, (i + 1) % n);
        }
        g
    }

    fn etats(n: usize) -> Vec<f64> {
        (0..n).map(|i| i as f64).collect()
    }

    /// EX-A13 — en régime nominal sur digraphe équilibré, l'itération converge
    /// et **préserve la moyenne initiale**.
    #[test]
    fn en_nominal_la_moyenne_initiale_est_invariante() {
        let g = cycle(16);
        let mut it = Iteration::nouvelle(etats(16), &g, Mode::Nominal, 0.5);
        let moyenne = it.moyenne_initiale();
        for _ in 0..2_000 {
            it.tour(&g);
        }
        assert!(it.ecart() < 1e-6, "écart {}", it.ecart());
        assert!(
            (it.limite() - moyenne).abs() < 1e-9,
            "limite {} contre moyenne initiale {moyenne}",
            it.limite()
        );
    }

    /// EX-A43 (a) — à α = 1/Δ(G), l'itération **cesse de converger**. Le traité
    /// note que l'erreur est répétée dans la littérature antérieure.
    #[test]
    fn mode_a_alpha_egal_a_un_sur_delta_ne_converge_plus() {
        let g = cycle(16);
        let mut nominal = Iteration::nouvelle(etats(16), &g, Mode::Nominal, 0.5);
        let mut limite = Iteration::nouvelle(etats(16), &g, Mode::PasTropGrand, 1.0);
        // Le cycle orienté a une connectivité algébrique faible : la
        // convergence y est lente, et c'est une propriété du graphe, pas du
        // mécanisme.
        for _ in 0..3_000 {
            nominal.tour(&g);
            limite.tour(&g);
        }
        assert!(nominal.ecart() < 1e-6, "écart nominal {}", nominal.ecart());
        assert!(
            limite.ecart() > 1.0,
            "à α = 1/Δ(G) l'écart doit rester grand, or {}",
            limite.ecart()
        );
    }

    /// EX-A43 (b) — sous digraphe non équilibré, la limite est pondérée par la
    /// **topologie** et non par les données. L'interface affiche les trois
    /// grandeurs ensemble.
    #[test]
    fn mode_b_la_limite_quitte_la_moyenne_initiale() {
        let g = cycle(16);
        let mut it = Iteration::nouvelle(etats(16), &g, Mode::DigrapheNonEquilibre, 0.2);
        let moyenne = it.moyenne_initiale();
        for _ in 0..3_000 {
            it.tour(&g);
        }
        assert!(
            (it.limite() - moyenne).abs() > 1e-3,
            "la limite {} devrait quitter la moyenne initiale {moyenne}",
            it.limite()
        );
        // Mais elle reste dans l'enveloppe convexe des états initiaux, où elle
        // est **indéterminée**.
        let (bas, haut) = it.enveloppe_initiale();
        assert!(it.limite() >= bas - 1e-9 && it.limite() <= haut + 1e-9);
        let a = it.affichage();
        assert!(a.iter().any(|(k, _)| *k == "moyenne initiale"));
        assert!(a
            .iter()
            .any(|(_, v)| v.contains("indéterminée")));
    }

    /// EX-A43 (d), PD10 — un agent mort cesse de publier, ses voisins lisent un
    /// état figé, et le critère local **confond mort et convergence**.
    #[test]
    fn mode_d_le_critere_local_confond_mort_et_convergence() {
        // Deux agents seulement : si l'un meurt d'emblée, l'autre le rejoint et
        // le critère local est satisfait — alors qu'aucun accord n'a eu lieu.
        let mut g = Graphe::vide(2);
        g.ajouter(0, 1);
        g.ajouter(1, 0);
        let mut it = Iteration::nouvelle(vec![0.0, 100.0], &g, Mode::MortOuConverge, 0.5);
        it.arreter(1);
        // Le critère s'évalue à chaque tour : c'est ce que fait un agent.
        let mut satisfait = false;
        for _ in 0..500 {
            it.tour(&g);
            satisfait = it.critere_local(1e-6, 5);
        }
        assert!(satisfait, "le critère local est satisfait, écart {}", it.ecart());
        // Et pourtant la limite n'est pas la moyenne initiale : c'est l'état de
        // l'agent mort qui a tout décidé.
        assert!((it.limite() - 100.0).abs() < 1e-6);
        assert!((it.moyenne_initiale() - 50.0).abs() < 1e-9);
        assert!(Mode::MortOuConverge.avertissement().unwrap().contains("HORS du modèle"));
    }

    /// EX-A43 (c) — le budget de retard décroît avec Δ(G), et le mode « moyeu »
    /// le rend minuscule : **7,933 × 10⁻³** à n = 100.
    ///
    /// NF-15 — c'est la valeur que le §3.1 (p. 42) écrit désormais, après avoir
    /// tranché l'écart que ce test avait relevé : « l'arrondi de π/(4n) donnerait
    /// 7,9 × 10⁻³, que la borne réellement écrite dépasse de 0,42 % : un arrondi
    /// présenté comme une borne stricte est un énoncé faux, non une
    /// imprécision ». Le test continue de vérifier la **valeur exacte** que le
    /// modèle produit, et que l'arrondi la dépasse — l'énoncé corrigé du traité
    /// est ainsi retrouvé, pas cité.
    #[test]
    fn le_budget_de_retard_decroit_avec_le_degre() {
        assert!(budget_de_retard(1) > budget_de_retard(10));
        let moyeu_a_100 = budget_de_retard(99);
        assert!(
            (moyeu_a_100 - 7.933e-3).abs() < 1e-6,
            "π/(4·99) = {moyeu_a_100}"
        );
        assert!(
            moyeu_a_100 > 7.9e-3,
            "l'arrondi « moins de 7,9 × 10⁻³ » est dépassé par la borne réellement écrite"
        );
        // … et de 0,42 %, comme le §3.1 le chiffre.
        assert!(
            ((moyeu_a_100 / 7.9e-3 - 1.0) * 100.0 - 0.42).abs() < 0.01,
            "dépassement de {:.3} %",
            (moyeu_a_100 / 7.9e-3 - 1.0) * 100.0
        );
        // Avec Δ = n plutôt que n − 1, l'arrondi tiendrait — c'est de là qu'il
        // venait, et c'est ce qui le rend faux comme borne sur Δ(G) = n − 1.
        assert!(budget_de_retard(100) < 7.9e-3);
        // L'avertissement affiche la valeur exacte, jamais l'arrondi seul.
        let a = Mode::Moyeu.avertissement().unwrap();
        assert!(a.contains("7,933"), "{a}");
    }

    /// EX-A43 — hors de l'exception nommée, **aucune** barre de progression.
    #[test]
    fn aucune_progression_hors_de_lexception_nommee() {
        // Digraphe non connexe : pas d'exception, donc pas de progression.
        let mut g = Graphe::vide(4);
        g.ajouter(0, 1);
        g.ajouter(1, 0);
        let it = Iteration::nouvelle(etats(4), &g, Mode::Nominal, 0.5);
        assert_eq!(it.progression(&g), None);
        assert!(Iteration::REFUS_PROGRESSION.contains("Lyapunov"));

        // Cycle équilibré fortement connexe : l'exception s'applique.
        let c = cycle(8);
        let it2 = Iteration::nouvelle(etats(8), &c, Mode::Nominal, 0.5);
        assert!(it2.progression(&c).is_some());
    }

    /// Le mécanisme tourne sur un graphe variable dans le temps, ce qui est le
    /// cas d'usage réel (EX-C16).
    #[test]
    fn literation_supporte_un_graphe_variable() {
        let mut gen = Generateur::nouveau(24, 4, 8);
        let mut alea = Alea::nouveau(9);
        let g0 = gen.tour(&mut alea);
        let mut it = Iteration::nouvelle(etats(24), &g0, Mode::Nominal, 0.2);
        let depart = it.ecart();
        for _ in 0..600 {
            let g = gen.tour(&mut alea);
            it.tour(&g);
        }
        assert!(it.ecart() < depart / 10.0, "écart {} depuis {depart}", it.ecart());
    }

    /// PD8 — la signature affiche le modèle de panne vide et le synchronisme
    /// parfait, qui sont l'inverse de ceux du reste du produit.
    #[test]
    fn la_signature_affiche_le_modele_vide_et_le_synchronisme_parfait() {
        let m = SIGNATURE.iter().find(|(k, _)| *k == "modèle de panne").unwrap();
        assert!(m.1.contains("vide"));
        let s = SIGNATURE.iter().find(|(k, _)| *k == "synchronisme").unwrap();
        assert!(s.1.contains("parfait"));
        let c = SIGNATURE.iter().find(|(k, _)| *k == "convergence").unwrap();
        assert!(c.1.contains("jamais convertie en délai"));
    }
}
