//! **S'accorder** — seuil de quorum, moyenne locale, et la grille qui les juge
//! (EX-A28, EX-A29, EX-A50 à EX-A52, EX-A55, EX-V18).
//!
//! > L'essaim ne résout pas l'impossibilité, il refuse la question — et paie ce
//! > refus en fenêtres pendant lesquelles l'invariant peut être faux. (§4.2)
//!
//! Chaque mécanisme du §5.1 **déclare la propriété qu'il abandonne**, et le
//! simulateur **calcule en permanence le prédicat de cette propriété** afin que
//! la perte soit observable au lieu d'être supposée. Ce prédicat est un
//! privilège de l'observateur : aucun agent n'en dispose, et l'interface le dit.
//!
//! **Ce n'est pas un oracle au sens de `sim-core`.** Aucun `Registre::armer`
//! n'apparaît dans ce fichier : les trois prédicats sont *ad hoc*, hors du
//! registre et donc hors des garanties de PD2. `crate::hors_perimetre()` le
//! déclare (EX-A51), et le mot « armé » est réservé aux quinze oracles du
//! catalogue.

use crate::echantillonnage::ServiceDePairs;
use crate::propagation::FamilleCrdt;
use sim_core::alea::Alea;

/// Les trois mécanismes de la figure 5.1, plus le consensus en repère cité.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Mecanisme {
    /// Décision par seuil, dite *best-of-n* (EX-A28).
    SeuilDeQuorum,
    /// Moyenne locale itérée, sans accord exact (EX-A29).
    MoyenneAlignement,
    /// Fusion de CRDT : convergence sans accord (§4.2).
    FusionCrdt,
    /// Consensus du ch. 4 — **repère cité, jamais mesuré** (DT7).
    ///
    /// Il n'est pas de la figure 5.1 : il est la quatrième ligne du tableau 14,
    /// celle contre laquelle les trois autres se lisent. Sa signature est celle
    /// du consensus, et non celle du seuil de quorum — les confondre remplirait
    /// de faux les deux colonnes qu'EX-V07 interdit de laisser vides, ce qui est
    /// pire que le vide.
    Consensus,
}

/// Verdict d'une case de la grille (EX-V18).
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Case {
    /// ✓ — tenue, et **mesurée**.
    Tenue,
    /// ~ — tenue **sous condition**.
    SousCondition,
    /// ✕ — abandonnée.
    Abandonnee,
    /// Non mesurée : la ligne reste en gris avec la valeur du traité.
    NonLivree,
}

impl Case {
    /// Le symbole affiché dans la grille vivante.
    pub fn symbole(self) -> &'static str {
        match self {
            Case::Tenue => "✓",
            Case::SousCondition => "~",
            Case::Abandonnee => "✕",
            Case::NonLivree => "gris",
        }
    }
}

impl Mecanisme {
    /// **EX-A51** — la propriété que le mécanisme abandonne, déclarée.
    pub fn propriete_abandonnee(self) -> &'static str {
        match self {
            Mecanisme::SeuilDeQuorum => "accord, **sous partition réseau**",
            Mecanisme::MoyenneAlignement => "validité, et terminaison en temps fini",
            Mecanisme::FusionCrdt => "validité — **le refus est impossible**",
            Mecanisme::Consensus => "disponibilité sous partition, et terminaison en asynchrone pur",
        }
    }

    /// Le prédicat *ad hoc* calculé pour cette propriété — **pas** un oracle du
    /// registre de `sim-core` (EX-A51, voir le `//!` du module).
    ///
    /// Les deux premiers renvoient à une grandeur que le produit tient
    /// réellement : [`SeuilDeQuorum::engagements_incompatibles`] et
    /// [`MoyenneLocale::ecart_a_la_validite`]. Le troisième n'en a aucune, et le
    /// dit : la fusion CRDT ne peut pas refuser, donc il n'y a pas d'opération
    /// « qui aurait dû être refusée » à compter — seul un contrôle ponctuel
    /// existe, [`crate::propagation::FamilleCrdt::verifier_invariant`], et il ne
    /// cumule rien.
    pub fn oracle_arme(self) -> &'static str {
        match self {
            Mecanisme::SeuilDeQuorum => "compteur d'engagements incompatibles simultanés",
            Mecanisme::MoyenneAlignement => {
                "écart mesuré entre la limite atteinte et la moyenne des états initiaux"
            }
            Mecanisme::FusionCrdt => {
                "aucun compteur — contrôle ponctuel `verifier_invariant`, jamais cumulé"
            }
            Mecanisme::Consensus => "aucun — repère cité, jamais mesuré (DT7)",
        }
    }

    /// **EX-A50** — ce que l'interface affiche, et ce qu'elle n'affiche
    /// **jamais**. Aucun mécanisme n'affiche de verdict global.
    pub fn affichage(self) -> (&'static str, &'static str) {
        match self {
            Mecanisme::SeuilDeQuorum => (
                "fraction locale ≥ 1 − δ franchie chez x agents",
                "décidé / accord atteint",
            ),
            Mecanisme::MoyenneAlignement => ("écart ≤ ε sur T tours", "convergé"),
            Mecanisme::FusionCrdt => (
                "répliques identiques chez x agents à cet instant",
                "cohérent / synchronisé",
            ),
            Mecanisme::Consensus => (
                "valeur du traité, en gris — aucune mesure du produit",
                "décidé / consensus atteint",
            ),
        }
    }

    /// Modèle de panne déclaré — colonne du tableau 14, **jamais vide**.
    pub fn modele_de_panne(self) -> &'static str {
        match self {
            Mecanisme::SeuilDeQuorum => "crash-arrêt et omission",
            Mecanisme::MoyenneAlignement => "aucun",
            Mecanisme::FusionCrdt => "crash-arrêt, omission, duplication, désordre",
            Mecanisme::Consensus => "crash-arrêt, omission",
        }
    }

    /// Synchronisme déclaré — colonne du tableau 14, **jamais vide**.
    pub fn synchronisme(self) -> &'static str {
        match self {
            Mecanisme::SeuilDeQuorum => "asynchrone",
            Mecanisme::MoyenneAlignement => "synchrone, tours globaux",
            Mecanisme::FusionCrdt => "asynchrone",
            Mecanisme::Consensus => "synchronisme partiel",
        }
    }

    /// **Tous les verdicts sont conditionnels au modèle P.** Sous faute
    /// arbitraire, la borne 3f + 1 tue les trois mécanismes.
    pub const CONDITIONNEL_AU_MODELE_P: &'static str =
        "verdict conditionnel au modèle P (crash-arrêt et omission) : sous faute arbitraire, \
         aucune solution à moins de 3f + 1 participants ne tolère f déviants, et ce modèle tue \
         les trois premières lignes de la figure 5.1 (§5.1, §2.3)";
}

/// **EX-A28** — DÉCISION-PAR-SEUIL, dit *best-of-n*.
///
/// Opinion échantillonnée localement, diffusion pendant une durée
/// proportionnelle à la qualité, règle de **k-unanimité**, détection de quorum à
/// une fraction locale ≥ 1 − δ.
#[derive(Debug)]
pub struct SeuilDeQuorum {
    /// Taille de la population.
    pub n: u32,
    /// Opinion de chaque agent : index de l'option.
    opinion: Vec<usize>,
    /// Qualité perçue de chaque option — c'est elle qui module la diffusion.
    pub qualites: Vec<f64>,
    /// δ : la fraction locale doit atteindre 1 − δ.
    pub delta: f64,
    /// k de la règle de k-unanimité : l'unique entier qui règle le compromis
    /// vitesse/exactitude.
    pub k: u32,
    /// Nombre d'échantillons consécutifs unanimes, par agent.
    unanimites: Vec<u32>,
    /// Agents ayant engagé une option.
    engage: Vec<Option<usize>>,
    /// Partition réseau : les agents d'indice < n/2 ne parlent plus aux autres.
    pub partition: bool,
    /// **EX-A55** — l'engagement de la ligne 10 est-il révocable, et à quel
    /// coût ?
    pub revocable: bool,
    /// Tours écoulés.
    pub tours: u64,
}

impl SeuilDeQuorum {
    /// Construit le mécanisme.
    ///
    /// **EX-A55** — un engagement **irrévocable** est refusé au chargement : le
    /// seuil de quorum n'est admissible que si l'engagement de sa ligne 10 peut
    /// être annulé par une action locale de coût borné et connu.
    pub fn nouveau(
        n: u32,
        qualites: Vec<f64>,
        delta: f64,
        k: u32,
        revocable: bool,
        alea: &mut Alea,
    ) -> Result<SeuilDeQuorum, String> {
        if !revocable {
            return Err(
                "engagement irrévocable refusé : une décision n'est admissible ici que si un \
                 agent peut l'annuler par une action locale de **coût borné et connu**. Sans \
                 révocabilité, ce mécanisme demande un accord, et l'accord est le ch. 4 (§5.1, \
                 EX-A55)."
                    .to_string(),
            );
        }
        // `k = 0` rend la règle de k-unanimité vraie par vacuité : `vues` est
        // vide, `all` répond vrai sans évaluer sa fermeture, et l'affectation
        // indexe le vecteur vide. Un refus rendu à l'appelant, jamais un abandon
        // (SPEC §7, clause 4).
        if k == 0 {
            return Err(
                "k = 0 refusé : la règle du §5.1 est une k-unanimité sur k opinions observées. \
                 À k = 0 elle est vraie par vacuité, ce qui n'est pas un accord unanime mais \
                 une absence d'observation."
                    .to_string(),
            );
        }
        if qualites.is_empty() {
            return Err(
                "aucune option : le seuil de quorum choisit parmi des options de qualité connue, \
                 et il en faut au moins une (§5.1)."
                    .to_string(),
            );
        }
        let m = qualites.len();
        Ok(SeuilDeQuorum {
            opinion: (0..n as usize).map(|_| alea.entier(m as u64) as usize).collect(),
            n,
            qualites,
            delta,
            k,
            unanimites: vec![0; n as usize],
            engage: vec![None; n as usize],
            partition: false,
            revocable,
            tours: 0,
        })
    }

    fn coupe(&self, i: u32, j: u32) -> bool {
        self.partition && ((i < self.n / 2) != (j < self.n / 2))
    }

    /// Un tour : chaque agent échantillonne k pairs ; si tous portent la même
    /// opinion, il l'adopte. La diffusion est modulée par la qualité.
    pub fn tour(&mut self, service: &mut ServiceDePairs, alea: &mut Alea) {
        self.tours += 1;
        let anciennes = self.opinion.clone();
        for i in 0..self.n {
            let mut vues = Vec::with_capacity(self.k as usize);
            for _ in 0..self.k {
                if let Some(j) = service.tirer(i, alea) {
                    if self.coupe(i, j) {
                        continue;
                    }
                    // Renforcement modulé : un agent diffuse d'autant plus que
                    // la qualité qu'il perçoit est élevée.
                    let q = self.qualites[anciennes[j as usize]];
                    if alea.uniforme() < q {
                        vues.push(anciennes[j as usize]);
                    }
                }
            }
            // Règle de k-unanimité.
            if vues.len() == self.k as usize && vues.iter().all(|o| *o == vues[0]) {
                self.opinion[i as usize] = vues[0];
                self.unanimites[i as usize] += 1;
            } else {
                self.unanimites[i as usize] = 0;
            }

            // Détection de quorum : fraction locale ≥ 1 − δ.
            let echantillon: Vec<usize> = (0..8)
                .filter_map(|_| service.tirer(i, alea))
                .filter(|j| !self.coupe(i, *j))
                .map(|j| anciennes[j as usize])
                .collect();
            if !echantillon.is_empty() {
                let mienne = self.opinion[i as usize];
                let part = echantillon.iter().filter(|o| **o == mienne).count() as f64
                    / echantillon.len() as f64;
                if part >= 1.0 - self.delta {
                    self.engage[i as usize] = Some(mienne);
                }
            }
        }
    }

    /// **EX-A51, oracle armé** — nombre d'options distinctes engagées
    /// simultanément. Au-delà de une, deux options incompatibles sont engagées.
    ///
    /// Privilège de l'observateur : **aucun agent ne le détecte**.
    pub fn engagements_incompatibles(&self) -> usize {
        let mut vues: Vec<usize> = self.engage.iter().flatten().copied().collect();
        vues.sort_unstable();
        vues.dedup();
        vues.len().saturating_sub(1)
    }

    /// Fraction d'agents ayant engagé une option.
    pub fn fraction_engagee(&self) -> f64 {
        self.engage.iter().filter(|e| e.is_some()).count() as f64 / self.n as f64
    }

    /// **La case « accord » de la grille**, remplie par la mesure.
    ///
    /// Elle bascule de ✓ à ✕ dès que deux options incompatibles sont engagées —
    /// ce qui est exactement ce qu'une partition produit.
    pub fn case_accord(&self) -> Case {
        if self.engagements_incompatibles() > 0 {
            Case::Abandonnee
        } else if self.partition {
            // Sous partition, l'accord n'est tenu que tant que les deux côtés
            // n'ont pas encore engagé : c'est une condition, pas une garantie.
            Case::SousCondition
        } else {
            Case::Tenue
        }
    }
}

/// **EX-A29** — MOYENNE-LOCALE : moyenne du voisinage du tour, i compris ;
/// arrêt local et non concerté sur |Δx_i| ≤ ε pendant T tours.
///
/// Réutilise le noyau de mise à jour de l'alignement (EX-A02) ; ce qui change
/// n'est pas la règle mais le **statut de la sortie** — un choix collectif, non
/// un paramètre d'ordre — donc les oracles armés.
pub struct MoyenneLocale {
    /// État courant de chaque agent.
    pub x: Vec<f64>,
    x0: Vec<f64>,
    /// Tours écoulés.
    pub tours: u64,
    sous_epsilon: Vec<u32>,
    /// Un agent figé — il ne bouge plus et fixe la limite pour tout l'essaim.
    fige: Vec<bool>,
}

impl MoyenneLocale {
    /// Initialise à partir des états de départ.
    pub fn nouvelle(x0: Vec<f64>) -> MoyenneLocale {
        let n = x0.len();
        MoyenneLocale {
            x: x0.clone(),
            x0,
            tours: 0,
            sous_epsilon: vec![0; n],
            fige: vec![false; n],
        }
    }

    /// Mode « capture » : un seul agent figé fixe la limite pour tout l'essaim.
    pub fn figer(&mut self, i: usize) {
        self.fige[i] = true;
    }

    /// Un tour : chaque agent prend la moyenne de son voisinage, lui compris.
    pub fn tour(&mut self, service: &mut ServiceDePairs, alea: &mut Alea, degre: u32) {
        self.tours += 1;
        let anciens = self.x.clone();
        for i in 0..self.x.len() {
            if self.fige[i] {
                continue;
            }
            let mut somme = anciens[i];
            let mut compte = 1.0;
            for _ in 0..degre {
                if let Some(j) = service.tirer(i as u32, alea) {
                    somme += anciens[j as usize];
                    compte += 1.0;
                }
            }
            let nouveau = somme / compte;
            if (nouveau - anciens[i]).abs() <= 1e-3 {
                self.sous_epsilon[i] += 1;
            } else {
                self.sous_epsilon[i] = 0;
            }
            self.x[i] = nouveau;
        }
    }

    /// **EX-A51, oracle armé** — écart entre la limite atteinte et la moyenne
    /// des états initiaux. C'est la **validité**, et c'est ce que le mécanisme
    /// abandonne.
    pub fn ecart_a_la_validite(&self) -> f64 {
        let moyenne_initiale = self.x0.iter().sum::<f64>() / self.x0.len() as f64;
        let limite = self.x.iter().sum::<f64>() / self.x.len() as f64;
        (limite - moyenne_initiale).abs()
    }

    /// Arrêt local, **non concerté**. PD10 : il ne dit rien de l'essaim.
    pub fn arret_local(&self, i: usize, t: u32) -> bool {
        self.sous_epsilon[i] >= t
    }

    /// Mode « arrêt prématuré » : deux sous-populations franchissent ε sur deux
    /// valeurs différentes.
    pub fn arrets_sur_valeurs_distinctes(&self, t: u32, ecart_min: f64) -> bool {
        let arretes: Vec<f64> = (0..self.x.len())
            .filter(|i| self.arret_local(*i, t))
            .map(|i| self.x[i])
            .collect();
        if arretes.len() < 2 {
            return false;
        }
        let max = arretes.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
        let min = arretes.iter().cloned().fold(f64::INFINITY, f64::min);
        max - min > ecart_min
    }
}

/// **EX-V18** — la grille vivante, qui fusionne trois provenances qu'il ne faut
/// pas confondre (F2) :
///
/// - les **sept colonnes du tableau 14** — mécanisme, modèle de panne,
///   synchronisme, messages par tour, tours jusqu'à l'arrêt, condition d'arrêt,
///   propriété abandonnée ;
/// - les **trois cases de la figure 5.1** — accord, validité, terminaison ;
/// - `valeur_du_traite`, **ajoutée par le produit** et affichée en gris.
///
/// **Quatre colonnes sur les sept sont remplies par la mesure**, pas toutes :
/// `tours_jusqua_larret`, `messages_par_tour` et `condition_darret` sont des
/// citations formatées, ce que `crate::hors_perimetre()` déclare.
#[derive(Clone, Debug)]
pub struct Ligne {
    /// Le mécanisme que cette ligne décrit.
    pub mecanisme: Mecanisme,
    /// Modèle de panne déclaré. Cette colonne n'est **jamais** vide (EX-V07).
    pub modele_de_panne: &'static str,
    /// Hypothèse de synchronisme déclarée. Jamais vide non plus.
    pub synchronisme: &'static str,
    /// Messages par tour, mesurés.
    pub messages_par_tour: String,
    /// Tours jusqu'à l'arrêt. « non borné » signifie qu'aucune borne finie
    /// n'existe sous les hypothèses posées — **et non qu'elle est grande**.
    pub tours_jusqua_larret: String,
    /// Ce qui fait arrêter le mécanisme, ou l'absence d'une telle condition.
    pub condition_darret: String,
    /// La propriété que ce mécanisme abandonne pour obtenir les autres.
    pub propriete_abandonnee: &'static str,
    /// Accord — figure 5.1, rempli par la mesure.
    pub accord: Case,
    /// Validité — figure 5.1.
    pub validite: Case,
    /// Terminaison — figure 5.1.
    pub terminaison: Case,
    /// Valeur du traité, affichée **en gris en regard** de la mesure.
    pub valeur_du_traite: &'static str,
}

/// La légende du traité, reprise **telle quelle**.
pub const LEGENDE_NON_BORNE: &str =
    "« non borné » signifie qu'aucune borne finie n'existe sous les hypothèses posées, **et non \
     qu'elle est grande** (§5.1, figure 5.1)";

impl Ligne {
    /// Construit la ligne d'un mécanisme. Les colonnes « modèle de panne » et
    /// « synchronisme » ne sont **jamais vides** : elles portent la signature
    /// déclarée (EX-V07).
    // Huit arguments : les quatre colonnes du tableau 14 qui ne se dérivent pas
    // du mécanisme, les trois cases de la figure 5.1, et la valeur du traité.
    // Les regrouper dans une structure intermédiaire ajouterait un type sans
    // ajouter de sens, et la ligne du tableau **est** déjà cette structure.
    #[allow(clippy::too_many_arguments)]
    pub fn nouvelle(
        mecanisme: Mecanisme,
        messages_par_tour: String,
        tours_jusqua_larret: String,
        condition_darret: String,
        accord: Case,
        validite: Case,
        terminaison: Case,
        valeur_du_traite: &'static str,
    ) -> Ligne {
        Ligne {
            modele_de_panne: mecanisme.modele_de_panne(),
            synchronisme: mecanisme.synchronisme(),
            propriete_abandonnee: mecanisme.propriete_abandonnee(),
            mecanisme,
            messages_par_tour,
            tours_jusqua_larret,
            condition_darret,
            accord,
            validite,
            terminaison,
            valeur_du_traite,
        }
    }

    /// Vrai si la ligne est entièrement mesurée. Une ligne non livrée reste en
    /// gris avec les valeurs du traité.
    pub fn mesuree(&self) -> bool {
        ![self.accord, self.validite, self.terminaison].contains(&Case::NonLivree)
    }
}

/// Construit la grille à partir des mesures.
pub fn grille(quorum: &SeuilDeQuorum, moyenne: &MoyenneLocale, crdt: FamilleCrdt) -> Vec<Ligne> {
    vec![
        Ligne::nouvelle(
            Mecanisme::SeuilDeQuorum,
            format!("{} par tour et par agent", quorum.k + 8),
            "non borné".to_string(),
            format!("fraction locale ≥ 1 − δ = {:.2}", 1.0 - quorum.delta),
            quorum.case_accord(),
            Case::Tenue,
            Case::SousCondition,
            "seuil de quorum : accord abandonné sous partition (figure 5.1)",
        ),
        Ligne::nouvelle(
            Mecanisme::MoyenneAlignement,
            "Θ(d̄) par tour et par agent".to_string(),
            "non borné".to_string(),
            "|Δx_i| ≤ ε pendant T tours — local et non concerté".to_string(),
            Case::Tenue,
            if moyenne.ecart_a_la_validite() > 1e-6 {
                Case::Abandonnee
            } else {
                Case::Tenue
            },
            Case::Abandonnee,
            "moyenne locale : validité et terminaison en temps fini abandonnées",
        ),
        Ligne::nouvelle(
            Mecanisme::FusionCrdt,
            format!("{} octets par message", crdt.octets_par_message(64)),
            "non borné".to_string(),
            "aucune — la fusion est continue".to_string(),
            Case::Tenue,
            Case::Abandonnee,
            Case::SousCondition,
            "fusion CRDT : validité abandonnée, le refus est impossible",
        ),
        // Le consensus reste **en repère cité**, jamais mesuré (DT7).
        Ligne::nouvelle(
            Mecanisme::Consensus,
            "Ω(n) par décision".to_string(),
            "bornée après stabilisation seulement".to_string(),
            "décision du quorum".to_string(),
            Case::NonLivree,
            Case::NonLivree,
            Case::NonLivree,
            "consensus, synchronisme partiel : Ω(n) messages par décision, terminaison \
             conditionnelle — repère cité, jamais mesuré (DT7)",
        ),
    ]
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::echantillonnage::Biais;

    /// SPEC §7, clause 4 — une configuration invalide est un refus rendu à
    /// l'appelant, jamais un abandon. À `k = 0` la règle de k-unanimité était
    /// vraie par vacuité et l'affectation indexait un vecteur vide.
    #[test]
    fn un_k_nul_ou_sans_option_est_refuse_au_lieu_de_paniquer() {
        let mut alea = Alea::nouveau(1);
        let refus = SeuilDeQuorum::nouveau(16, vec![0.9, 0.5], 0.1, 0, true, &mut alea);
        assert!(refus.is_err(), "k = 0 doit être refusé");
        let refus = SeuilDeQuorum::nouveau(16, Vec::new(), 0.1, 3, true, &mut alea);
        assert!(refus.is_err(), "une liste d'options vide doit être refusée");
        // Et le réglage voisin, lui, passe : la garde ne mange pas le domaine utile.
        assert!(SeuilDeQuorum::nouveau(16, vec![0.9, 0.5], 0.1, 1, true, &mut alea).is_ok());
    }

    fn quorum(revocable: bool) -> Result<SeuilDeQuorum, String> {
        let mut alea = Alea::nouveau(1);
        SeuilDeQuorum::nouveau(256, vec![0.9, 0.85], 0.10, 3, revocable, &mut alea)
    }

    /// **EX-A55** — un engagement irrévocable est **refusé au chargement**.
    #[test]
    fn ex_a55_un_engagement_irrevocable_est_refuse() {
        let e = quorum(false).unwrap_err();
        assert!(e.contains("coût borné et connu"), "{e}");
        assert!(e.contains("ch. 4"), "{e}");
        assert!(quorum(true).is_ok());
    }

    /// **Critère de sortie de la phase 3** — la case « accord » du seuil de
    /// quorum **bascule sous partition** : deux quorums locaux se forment de
    /// part et d'autre de la coupe, et aucun agent ne le détecte.
    #[test]
    fn la_case_accord_bascule_sous_partition() {
        let mut sans = quorum(true).unwrap();
        let mut avec = quorum(true).unwrap();
        avec.partition = true;
        let mut s = ServiceDePairs::nouveau(256, Biais::Uniforme);
        let mut alea = Alea::nouveau(2);
        for _ in 0..200 {
            sans.tour(&mut s, &mut alea);
            avec.tour(&mut s, &mut alea);
        }
        assert_eq!(
            avec.case_accord(),
            Case::Abandonnee,
            "sous partition, deux options incompatibles doivent être engagées ({} distinctes)",
            avec.engagements_incompatibles() + 1
        );
        assert!(
            avec.engagements_incompatibles() > 0,
            "l'oracle armé doit compter les engagements incompatibles"
        );
        assert_ne!(sans.case_accord(), Case::Abandonnee, "sans partition, l'accord tient");
    }

    /// **EX-A50** — aucun mécanisme n'affiche de verdict global.
    #[test]
    fn ex_a50_aucun_verdict_global_nest_affiche() {
        for m in [
            Mecanisme::SeuilDeQuorum,
            Mecanisme::MoyenneAlignement,
            Mecanisme::FusionCrdt,
        ] {
            let (affiche, jamais) = m.affichage();
            assert!(!affiche.is_empty());
            assert!(!jamais.is_empty());
            // Ce qui est affiché ne contient jamais le verdict interdit.
            for interdit in ["décidé", "convergé", "accord atteint", "cohérent"] {
                assert!(
                    !affiche.contains(interdit),
                    "« {affiche} » contient le verdict interdit « {interdit} »"
                );
            }
        }
    }

    /// **EX-A51** — chaque mécanisme déclare la propriété qu'il abandonne, et
    /// l'oracle correspondant est nommé.
    #[test]
    fn ex_a51_chaque_mecanisme_declare_ce_quil_abandonne() {
        assert!(Mecanisme::SeuilDeQuorum
            .propriete_abandonnee()
            .contains("sous partition"));
        assert!(Mecanisme::MoyenneAlignement
            .propriete_abandonnee()
            .contains("terminaison"));
        assert!(Mecanisme::FusionCrdt
            .propriete_abandonnee()
            .contains("le refus est impossible"));
        for m in [
            Mecanisme::SeuilDeQuorum,
            Mecanisme::MoyenneAlignement,
            Mecanisme::FusionCrdt,
        ] {
            assert!(!m.oracle_arme().is_empty());
        }
        assert!(Mecanisme::CONDITIONNEL_AU_MODELE_P.contains("3f + 1"));
    }

    /// **EX-A29, EX-A51** — la moyenne locale abandonne la **validité** : un
    /// seul agent figé fixe la limite pour tout l'essaim, et l'oracle armé le
    /// mesure.
    #[test]
    fn ex_a29_un_agent_fige_capture_la_limite() {
        let x0: Vec<f64> = (0..64).map(|i| i as f64).collect();
        let mut m = MoyenneLocale::nouvelle(x0);
        m.figer(0); // Son état vaut 0, la moyenne initiale vaut 31,5.
        let mut s = ServiceDePairs::nouveau(64, Biais::Uniforme);
        let mut alea = Alea::nouveau(3);
        for _ in 0..2_000 {
            m.tour(&mut s, &mut alea, 4);
        }
        assert!(
            m.ecart_a_la_validite() > 1.0,
            "la capture doit éloigner la limite de la moyenne initiale, écart {}",
            m.ecart_a_la_validite()
        );
    }

    /// **EX-V18** — les colonnes « modèle de panne » et « synchronisme » ne sont
    /// **jamais vides**, et la légende du « non borné » est reprise telle
    /// quelle.
    #[test]
    fn ex_v18_la_grille_ne_laisse_aucune_signature_vide() {
        let q = quorum(true).unwrap();
        let m = MoyenneLocale::nouvelle(vec![1.0, 2.0, 3.0]);
        let g = grille(&q, &m, FamilleCrdt::Etat);
        assert_eq!(g.len(), 4);
        for l in &g {
            assert!(!l.modele_de_panne.is_empty(), "{:?}", l.mecanisme);
            assert!(!l.synchronisme.is_empty(), "{:?}", l.mecanisme);
            assert!(!l.propriete_abandonnee.is_empty());
            assert!(!l.valeur_du_traite.is_empty());
        }
        assert!(LEGENDE_NON_BORNE.contains("et non qu'elle est grande"));
    }

    /// **EX-V18, DT7** — la ligne « consensus » reste **non livrée**, donc en
    /// gris avec la valeur du traité. Elle n'est jamais mesurée.
    #[test]
    fn ex_v18_la_ligne_consensus_reste_un_repere_cite() {
        let q = quorum(true).unwrap();
        let m = MoyenneLocale::nouvelle(vec![1.0, 2.0]);
        let g = grille(&q, &m, FamilleCrdt::Etat);
        let consensus = g.last().unwrap();
        assert!(!consensus.mesuree(), "le consensus n'est jamais mesuré");
        assert!(consensus.valeur_du_traite.contains("DT7"));
        assert_eq!(consensus.accord, Case::NonLivree);

        // Les trois autres, elles, sont mesurées.
        assert!(g[0].mesuree());
        assert!(g[1].mesuree());
        assert!(g[2].mesuree());
    }

    /// Les cases portent les symboles du traité.
    #[test]
    fn les_cases_portent_les_symboles_du_traite() {
        assert_eq!(Case::Tenue.symbole(), "✓");
        assert_eq!(Case::SousCondition.symbole(), "~");
        assert_eq!(Case::Abandonnee.symbole(), "✕");
    }
}
