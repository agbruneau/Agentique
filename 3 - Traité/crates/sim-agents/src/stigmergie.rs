//! **Algorithme 2 du ch. 1** — renforcement stigmergique borné sur journal
//! (EX-A01), ses quatre modes de défaillance (EX-A10) et les deux seules bornes
//! que le traité démontre (EX-A11a/b/c).
//!
//! > Un essaim stigmergique n'atteint pas l'optimum, il campe à distance bornée
//! > de lui, et cette distance est un réglage et non un défaut à corriger.
//! > (§1.2, p. 16, 3ᵉ éd.)
//!
//! Ce que ce mécanisme **ne** démontre **pas**, et que l'interface ne doit
//! jamais laisser croire (F3) : la convergence. Le traité écrit que l'énoncé du
//! plancher est « une propriété du tirage, pas un théorème de convergence ».
//! Aucune fonction de ce fichier ne rend un booléen « convergé ».

use crate::essaim::{Membre, Perception};
use sim_core::alea::Alea;
use sim_core::famille::{Familles, TirageDeDecision};
use sim_core::moteur::Moteur;
use sim_core::oracle::{Oracle, Registre};
use sim_core::temps::{Duree, Granularite, Instant};
use sim_core::ActeurId;
use sim_milieu::{Cle, Ecriture, Identite, Latence, Milieu};

/// Nombre de tranches de la série temporelle d'effort.
///
/// **Décision d'affichage du produit, sans provenance dans le traité (F1)** :
/// vingt tranches tiennent dans une figure lisible sans que l'échantillonnage
/// masque la bascule d'utilité. Aucune section du traité ne fixe ce découpage.
pub const NB_TRANCHES: usize = 20;

/// Oracle du **plancher d'exploration** : la probabilité de tirer une ressource
/// non dominante reste au-dessus de sa borne.
pub const PLANCHER: &str = "EX-A11b — plancher d'exploration";
/// Oracle de la **fraction d'effort hors dominante**, la contrepartie mesurée
/// du plancher.
pub const HORS_DOMINANTE: &str = "EX-A11b — fraction d'effort hors dominante";

/// Où l'agent écrit sa trace par rapport à son action.
///
/// **Choix binaire déclaré, sans valeur par défaut** — même discipline
/// qu'EX-A33 : les deux positions ont un mode de défaillance, il n'y a pas de
/// troisième option, et subir celle d'une bibliothèque serait pire que la
/// choisir.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum MomentTrace {
    /// Écriture **avant** l'action. Surestimation : la trace est déposée même
    /// si l'action échoue (EX-A10, « trace optimiste »).
    Avant,
    /// Écriture **après** l'action. Sous-estimation, puis réattaque d'une
    /// ressource déjà traitée par un autre agent qui n'a pas encore vu la trace
    /// (EX-A10, « trace pessimiste »).
    Apres,
}

/// Paramètres du mécanisme — les plages sont celles du scénario B.
#[derive(Clone, Debug, PartialEq)]
pub struct Params {
    /// Nombre d'agents.
    pub n: u32,
    /// Nombre de ressources.
    pub m: u32,
    /// Nombre de partitions du milieu.
    pub p: u32,
    /// Décroissance par fenêtre τ. Le traité pose γ ∈ (0, 1) ; **γ = 1 est hors
    /// domaine et exposé exprès** (EX-A11a).
    pub gamma: f64,
    /// Plancher de la trace φ — il borne le rapport φ_max/φ_min.
    pub phi_min: f64,
    /// Plafond de la trace φ.
    pub phi_max: f64,
    /// Poids de la trace.
    pub alpha: f64,
    /// Poids de l'heuristique.
    pub beta: f64,
    /// Utilité minimale d'une ressource.
    pub eta_min: f64,
    /// Utilité maximale d'une ressource.
    pub eta_max: f64,
    /// Période de cycle T, en millisecondes.
    pub periode_cycle_ms: f64,
    /// Fenêtre de décroissance τ, en millisecondes.
    pub fenetre_tau_ms: f64,
    /// ℓ₉₉ du chemin de durabilité du milieu, en millisecondes. **Entrée** du
    /// modèle (§8.3 du PRD) : T < ℓ₉₉ produit l'essaim aveugle.
    pub l99_milieu_ms: f64,
    /// Instant de bascule d'utilité, en fraction du budget d'événements.
    pub bascule_a: f64,
    /// Où la trace est écrite.
    pub moment_trace: MomentTrace,
    /// Probabilité de crash entre l'action et la validation du décalage
    /// (EX-A10, « rejeu »).
    pub crash_avant_validation: f64,
    /// Vrai si l'action est idempotente. Quand elle ne l'est pas, le rejeu
    /// produit un **effet dupliqué** — le cinquième reste de la conclusion, que
    /// le produit exhibe sans le supprimer.
    pub action_idempotente: bool,
    /// Vrai si toutes les ressources sont sur une seule partition. Faux les
    /// répartit, ce qui rend leurs φ incomparables (EX-A10, « incomparabilité
    /// M2 »).
    pub ressources_sur_une_partition: bool,
    /// Nombre d'enregistrements lus par cycle — la borne de perception
    /// d'EX-A12.
    ///
    /// Elle doit rester **supérieure au débit de production**, soit `n`
    /// enregistrements par période de cycle : chaque agent dépose une trace par
    /// cycle, et un agent qui lit moins que ce que la population écrit accumule
    /// un retard qu'il ne rattrape jamais. Ce n'est pas un défaut à masquer —
    /// c'est le retard de consommation, mesuré par
    /// [`Mesures::retard_consommation_max`] et signalé par
    /// [`Params::avertissements`].
    pub intervalle_lecture: u32,
    /// Probabilité qu'une action échoue (EX-C07 : « faire échouer une opération
    /// d'ordinaire réussie »). C'est ce qui donne son sens à la trace
    /// optimiste : un dépôt sans effet.
    pub echec_action: f64,
    /// Intensité d'un dépôt unitaire. `None` la calibre pour que φ atteigne
    /// φ_max quand toute la population sert la même ressource — voir
    /// [`Params::depot`].
    pub depot_unitaire: Option<f64>,
    /// **Conformité de la population** (EX-C19, phase 6) : part de structure
    /// entre 0 — une famille de décision par agent — et 1 — une famille unique.
    ///
    /// Le défaut est **0**, la population décorrélée, qui est l'hypothèse la plus
    /// favorable et la seule sous laquelle les bornes d'EX-A11c ont été mesurées.
    /// Ce n'est pas la nature du modèle : c'est un réglage à sa valeur extrême, et
    /// PD13 impose de l'afficher comme tel. Toute valeur strictement entre 0 et 1
    /// est une **interpolation du produit**, sans provenance dans le traité.
    pub part_conforme: f64,
    /// **Identité partagée** (EX-M24, condition d'échec) : quand vrai, tous les
    /// agents se présentent au milieu sous une seule session.
    ///
    /// Le milieu appose ce qu'on lui présente ; il ne peut pas savoir que deux
    /// processus partagent une identité. C'est le zombie du §2.1 du traité revenu par la
    /// porte de l'identité, et le préréglage existe pour le **provoquer**
    /// (NF-10), pas pour le corriger.
    pub identite_partagee: bool,
}

impl Params {
    /// Défauts du scénario B.
    pub fn scenario_b() -> Params {
        Params {
            n: 64,
            m: 8,
            p: 8,
            gamma: 0.90,
            phi_min: 0.01,
            phi_max: 1.0,
            alpha: 1.0,
            beta: 1.0,
            eta_min: 0.5,
            eta_max: 1.0,
            periode_cycle_ms: 50.0,
            fenetre_tau_ms: 1_000.0,
            l99_milieu_ms: 20.0,
            bascule_a: 0.5,
            moment_trace: MomentTrace::Apres,
            crash_avant_validation: 0.0,
            action_idempotente: true,
            ressources_sur_une_partition: true,
            // Quatre fois le débit de production à n = 64 : la marge doit être
            // franche, sans quoi la moindre latence de queue transforme un
            // retard passager en retard permanent.
            intervalle_lecture: 256,
            echec_action: 0.05,
            depot_unitaire: None,
            // PD13 — la population décorrélée est un réglage à sa valeur
            // extrême, pas la nature du modèle. C'est l'hypothèse la plus
            // favorable, et la seule sous laquelle les bornes d'EX-A11c ont été
            // mesurées.
            part_conforme: 0.0,
            identite_partagee: false,
        }
    }

    /// Réglages dont l'effet dépasse ce que l'utilisateur croit régler.
    pub fn avertissements(&self) -> Vec<String> {
        let mut a = Vec::new();
        if self.intervalle_lecture < self.n {
            a.push(format!(
                "intervalle de lecture {} < population {} : chaque agent lit moins que ce que \
                 l'essaim écrit par cycle. Le retard de consommation croît sans borne, et ce que \
                 les agents perçoivent est un passé de plus en plus ancien — la mesure reste \
                 juste, mais elle ne porte plus sur le régime qu'on croit observer.",
                self.intervalle_lecture, self.n
            ));
        }
        if self.periode_cycle_ms < self.l99_milieu_ms {
            a.push(format!(
                "T = {:.1} ms < ℓ₉₉ = {:.1} ms : essaim aveugle. L'agent redécide avant que sa \
                 trace soit lisible, et l'exploration dégénère en tirage indépendant (EX-A10).",
                self.periode_cycle_ms, self.l99_milieu_ms
            ));
        }
        if self.gamma >= 1.0 {
            a.push(
                "γ = 1 : hors du domaine (0, 1) posé au §1.2. La trace ne s'oublie plus, les \
                 bornes d'EX-A11c sont effacées (NF-14), et l'essaim ne peut plus désapprendre."
                    .to_string(),
            );
        }
        // La moitié **basse** du domaine exclu ne produisait ni écrêtage, ni
        // avertissement, ni refus : `depot()` rendait +∞ à γ = 0 et `NaN` à
        // γ < 0. Le domaine (0, 1) a deux bords, et les deux se signalent.
        if self.gamma <= 0.0 || self.gamma.is_nan() {
            a.push(format!(
                "γ = {:.3} ≤ 0 : hors du domaine (0, 1) posé au §1.2, et la décroissance par \
                 fenêtre n'y est pas définie. La calibration du dépôt écrête γ à {:.0e} pour rendre \
                 une valeur finie, les bornes d'EX-A11c sont effacées (NF-14), et ce qui s'affiche \
                 n'est plus le régime qu'on croit régler.",
                self.gamma,
                Params::GAMMA_MIN
            ));
        }
        a
    }

    /// Bord **bas** de l'écrêtage de γ dans les trois calculs qui l'évaluent.
    ///
    /// **Décision d'implantation, sans provenance dans le traité (F1)** : le
    /// §1.2 pose γ ∈ (0, 1) sans borner l'intervalle par des valeurs
    /// représentables. Hors domaine, `−ln γ` vaut +∞ à γ = 0 et `NaN` à γ < 0,
    /// et l'un comme l'autre contaminent tout ce qui en descend. L'écrêtage est
    /// une **coercition déclarée** : [`Params::avertissements`] la signale et
    /// [`Params::bornes_applicables`] efface la borne.
    pub const GAMMA_MIN: f64 = 1e-6;

    /// Bord **haut** du même écrêtage, pour la seule calibration du dépôt.
    ///
    /// γ = 1 est un préréglage exposé exprès (EX-A11a, [`Params::verrouillage`]),
    /// et la calibration y diviserait par zéro. Les chemins du moteur, eux, ne
    /// passent pas par ce bord : ils court-circuitent γ ≥ 1 sur `ln γ = 0`, ce
    /// qui est la valeur exacte et non une approche.
    pub const GAMMA_MAX: f64 = 0.999_999;

    /// Intensité d'un dépôt.
    ///
    /// La valeur stationnaire de φ sous un flux de dépôts d'intensité `q`
    /// arrivant au rythme `r` avec décroissance γ par fenêtre τ vaut
    /// `q·r·τ/ln(1/γ)`. Le dépôt par défaut est calibré pour que cette valeur
    /// atteigne φ_max quand **toute** la population sert la même ressource ;
    /// sans cette calibration, φ sature à l'écrêtage dès les premiers cycles,
    /// toutes les ressources se valent, et la trace cesse de piloter le tirage.
    ///
    /// γ est écrêté aux **deux** bords du domaine (0, 1) — voir
    /// [`Params::GAMMA_MIN`] et [`Params::GAMMA_MAX`]. Sans le bord bas, γ = 0
    /// rendait +∞ et γ < 0 rendait `NaN`, et ce `NaN` descendait dans φ, puis
    /// dans les poids de tirage, puis dans les comparaisons qui les classent.
    /// La coercition est déclarée : [`Params::avertissements`] la signale et
    /// [`Params::bornes_applicables`] efface la borne.
    ///
    // ponytail: calibration analytique sur le régime stationnaire d'une
    // exponentielle. Elle suppose un flux régulier ; sous rafales, la valeur
    // dépasse transitoirement. Le paramètre reste réglable à la main pour cette
    // raison — un modèle minimal ne voit pas ce qu'un réglage physique voit.
    pub fn depot(&self) -> f64 {
        if let Some(q) = self.depot_unitaire {
            return q;
        }
        let cycles_par_fenetre = self.fenetre_tau_ms / self.periode_cycle_ms;
        let taux = self.n as f64 * cycles_par_fenetre;
        // `NaN` est traité à part : `f64::clamp` le **propage**, et γ = NaN — que
        // le décodage d'un lien partagé peut produire — sortirait sinon un dépôt
        // `NaN`, ce que cet écrêtage existe précisément pour empêcher.
        let gamma = if self.gamma.is_nan() {
            Params::GAMMA_MIN
        } else {
            self.gamma.clamp(Params::GAMMA_MIN, Params::GAMMA_MAX)
        };
        let decroissance = -libm::log(gamma);
        self.phi_max * decroissance / taux
    }

    /// EX-A11a — **verrouillage prématuré**. γ = 1 supprime l'oubli ; la trace
    /// devient une somme cumulée, le rapport φ_max/φ_min croît sans borne, et la
    /// probabilité de tirage de la dominante tend vers 1.
    pub fn verrouillage() -> Params {
        Params {
            gamma: 1.0,
            // Le dépôt reste celui du régime nominal : γ doit être la **seule**
            // variable qui change de comportement. Le calibrer sur γ = 1
            // donnerait un dépôt quasi nul et masquerait le verrouillage
            // derrière un second effet.
            depot_unitaire: Some(Params::scenario_b().depot()),
            ..Params::scenario_b()
        }
    }

    /// EX-A10 — **essaim aveugle** : T < ℓ₉₉. La rétroaction disparaît, parce
    /// qu'une trace écrite au cycle k n'est pas encore durable au cycle k+1 ;
    /// l'exploration dégénère en tirage indépendant.
    pub fn essaim_aveugle() -> Params {
        Params {
            periode_cycle_ms: 5.0,
            l99_milieu_ms: 200.0,
            ..Params::scenario_b()
        }
    }

    /// EX-A10 — **rejeu** : crash entre l'action et la validation de décalage.
    /// φ reste inchangé, parce que le dépôt est idempotent par M1 + M4 ; l'effet
    /// de l'action, lui, est dupliqué si l'action ne l'est pas.
    pub fn rejeu() -> Params {
        Params {
            crash_avant_validation: 0.2,
            action_idempotente: false,
            ..Params::scenario_b()
        }
    }

    /// EX-A10 — **incomparabilité M2** : les ressources comparées sont placées
    /// sur deux partitions, où aucun ordre n'est garanti.
    pub fn incomparabilite_m2() -> Params {
        Params {
            ressources_sur_une_partition: false,
            ..Params::scenario_b()
        }
    }

    /// EX-A10 — **trace optimiste** : écriture avant l'action.
    pub fn trace_optimiste() -> Params {
        Params {
            moment_trace: MomentTrace::Avant,
            ..Params::scenario_b()
        }
    }

    /// Les deux bornes que le traité démontre (EX-A11c).
    ///
    /// Plancher de tirage : (1/m)·(φ_min/φ_max)^α·(η_min/η_max)^β
    /// Fraction d'effort hors dominante : ((m−1)/m)·(même produit)
    ///
    /// `libm::pow` et non `f64::powf` : DT1.
    pub fn bornes(&self) -> Bornes {
        let facteur = libm::pow(self.phi_min / self.phi_max, self.alpha)
            * libm::pow(self.eta_min / self.eta_max, self.beta);
        let m = self.m as f64;
        Bornes {
            plancher_tirage: facteur / m,
            fraction_hors_dominante: facteur * (m - 1.0) / m,
        }
    }

    /// NF-14 — les hypothèses qui conditionnent les bornes. Un réglage qui en
    /// viole une **efface** la borne, il ne la grise pas.
    ///
    /// Les gardes couvrent **tout** ce que [`Params::bornes`] consomme, et pas
    /// seulement le couple φ : η, `m` et les deux exposants entrent dans la
    /// même formule, et un seul d'entre eux hors domaine rend une probabilité
    /// négative, supérieure à 1, infinie ou `NaN`. Rendre une telle valeur en
    /// `Ok` serait pire que de rendre une borne fausse : `NaN` fait échouer
    /// toute comparaison, donc l'oracle [`PLANCHER`] ne se déclencherait
    /// jamais, et un oracle muet se lit comme un oracle satisfait.
    ///
    /// La dernière garde est celle qu'EX-A58 impose : la **conformité de la
    /// population** est le quatrième réglage qui conditionne ces bornes, parce
    /// que le plancher d'EX-A11c suppose des tirages indépendants (tableau 21
    /// de la deuxième édition). L'effacement suit le **réglage** et jamais Φ_c
    /// mesuré — voir le §0.1 du PRD.
    pub fn bornes_applicables(&self) -> Result<Bornes, String> {
        // Le domaine a **deux** bords : γ ≥ 1 supprime l'oubli, γ ≤ 0 le rend
        // indéfini, et la forme négative attrape `NaN` par la même occasion.
        if !(self.gamma > 0.0 && self.gamma < 1.0) {
            return Err(format!(
                "borne effacée : γ = {:.3} est hors du domaine (0, 1) que le traité pose au §1.2. \
                 Au-delà de 1, sans oubli, φ_max/φ_min n'est plus borné ; à 0 ou en deçà, la \
                 décroissance par fenêtre n'est pas définie. Dans les deux cas le plancher calculé \
                 ne s'applique plus — il n'est ni grisé ni pointillé, il est retiré (NF-14).",
                self.gamma
            ));
        }
        if self.phi_min <= 0.0 || self.phi_min > self.phi_max {
            return Err(
                "borne effacée : l'écrêtage [φ_min, φ_max] est vide ou non positif ; le rapport \
                 qui fonde le plancher n'existe pas"
                    .to_string(),
            );
        }
        if self.eta_min <= 0.0 || self.eta_min > self.eta_max {
            return Err(
                "borne effacée : l'intervalle d'utilité [η_min, η_max] est vide ou non positif ; \
                 le second rapport du produit n'existe pas"
                    .to_string(),
            );
        }
        if self.m == 0 {
            return Err(
                "borne effacée : m = 0 — sans ressource, il n'y a pas de probabilité de tirage \
                 à minorer"
                    .to_string(),
            );
        }
        if self.alpha < 0.0 || self.beta < 0.0 {
            return Err(format!(
                "borne effacée : α = {:.3}, β = {:.3} — le traité pose des poids positifs au \
                 §1.2, et un exposant négatif inverse le rapport, ce qui rend un « plancher » \
                 supérieur à 1.",
                self.alpha, self.beta
            ));
        }
        if self.part_conforme > 0.0 {
            return Err(format!(
                "borne effacée : part de conformité = {:.3} — le plancher d'EX-A11c suppose les \
                 tirages des n agents indépendants (tableau 21), et dès que deux agents partagent \
                 une famille de décision cette hypothèse est violée par le réglage lui-même. La borne \
                 est retirée, pas grisée (NF-14, EX-A58).",
                self.part_conforme
            ));
        }
        Ok(self.bornes())
    }
}

/// Les deux bornes démontrées.
#[derive(Clone, Copy, Debug)]
pub struct Bornes {
    /// Probabilité minimale de tirage de toute ressource visible.
    pub plancher_tirage: f64,
    /// Fraction d'effort permanente hors ressource dominante.
    pub fraction_hors_dominante: f64,
}

impl Bornes {
    /// Légende obligatoire (EX-A11c), citée du traité.
    ///
    /// La provenance **nomme son édition** : `BLOC_B` cite la même page à
    /// l'autre bout du même écran avec sa mention, et une page citée sans elle
    /// est une provenance fausse, pas imprécise (F2). `sim-viz` recopie cette
    /// chaîne dans `SOURCE_BORNES` et tient la copie accordée par un test.
    pub const LEGENDE: &'static str =
        "un essaim stigmergique n'atteint pas l'optimum, il campe à distance bornée de lui, et \
         cette distance est un réglage et non un défaut à corriger (§1.2, p. 16, 3ᵉ éd.)";
}

/// Une ressource à exploiter.
#[derive(Clone, Copy, Debug)]
pub struct Ressource {
    /// Utilité réelle, susceptible de basculer en cours d'exécution. L'agent ne
    /// la connaît pas : il ne la découvre qu'en agissant.
    pub utilite: f64,
    /// Heuristique perçue η — l'information *a priori*, et elle est
    /// **statique**.
    ///
    /// Elle est informative au départ : η décroît comme l'utilité initiale,
    /// comme le fait toute heuristique digne de ce nom. Après la bascule, elle
    /// est **périmée** et pointe vers l'ancienne bonne ressource. C'est
    /// exactement le conflit que le scénario B met en scène : l'heuristique
    /// tire vers le passé, la trace vers le présent, et le rapport α/β décide
    /// lequel gagne.
    ///
    /// Elle est déterministe, et non tirée au sort : un η aléatoire ferait
    /// dépendre le critère d'acceptation de la graine, ce qui n'est plus un
    /// critère.
    pub eta: f64,
    /// Partition du milieu où la trace de cette ressource est écrite. Deux
    /// partitions n'ont **aucun** ordre entre elles (M2).
    pub partition: u32,
}

/// État d'un agent.
#[derive(Clone, Debug)]
struct Agent {
    id: ActeurId,
    membre: Membre,
    /// Trace perçue par ressource, écrêtée dans [φ_min, φ_max].
    phi: Vec<f64>,
    /// Curseurs de lecture par partition.
    curseurs: Vec<u64>,
    /// Curseurs **validés** — le point de reprise après un crash.
    curseurs_valides: Vec<u64>,
    derniere_actualisation: Instant,
    cycles: u64,
    /// Écritures déposées dont l'accusé de durabilité n'est pas revenu. Non
    /// vide au moment de décider, c'est l'essaim aveugle : l'agent redécide
    /// sans avoir vu l'effet de son dernier dépôt.
    en_vol: Vec<Ecriture>,
}

/// Mesures de l'exécution. Toutes sont des **sorties** du modèle et portent
/// l'étiquette « simulé » à l'affichage (EX-V11, F2).
#[derive(Clone, Debug, Default)]
pub struct Mesures {
    /// Cycles d'agent exécutés, toutes ressources confondues.
    pub cycles: u64,
    /// Effort dirigé vers chaque ressource, en cycles, sur toute l'exécution.
    pub effort: Vec<u64>,
    /// Effort dirigé vers chaque ressource **après** la bascule d'utilité.
    pub effort_apres_bascule: Vec<u64>,
    /// Effort par tranche de temps, `[tranche][ressource]`.
    ///
    /// Le cumul post-bascule mélange la transition et le régime atteint ; il ne
    /// répond donc pas à « l'essaim sait-il désapprendre », seulement à
    /// « combien de temps met-il ». C'est la série temporelle que le scénario B
    /// trace, et c'est sur sa dernière tranche que se juge le désapprentissage.
    pub effort_par_tranche: Vec<Vec<u64>>,
    /// Utilité effectivement récoltée par l'essaim.
    pub utilite_recoltee: f64,
    /// Utilité qu'aurait récoltée un essaim omniscient allant toujours au
    /// meilleur. Sert l'écart à l'optimum, **tracé sans borne** : le traité
    /// écrit que l'essaim campe à distance bornée sans jamais chiffrer cette
    /// distance, et l'interface ne la chiffre pas non plus.
    pub utilite_optimale: f64,
    /// Minimum, sur tous les cycles, de la probabilité de tirage la plus faible.
    pub plancher_observe: f64,
    /// Minimum, sur tous les cycles, de la fraction d'effort hors dominante.
    pub hors_dominante_observee: f64,
    /// EX-A10 « rejeu » — effets dupliqués par une action non idempotente.
    pub effets_dupliques: u64,
    /// EX-A10 « incomparabilité M2 » — décisions jouées sur un écart de φ
    /// inférieur au seuil de fiabilité, entre ressources de partitions
    /// distinctes. Le traité les déclare « sans objet ».
    pub decisions_non_fiables: u64,
    /// Cycles où l'agent redécide **avant** que sa propre trace précédente soit
    /// durable. C'est la signature de l'essaim aveugle : la rétroaction n'a pas
    /// le temps de revenir, et l'exploration dégénère en tirage indépendant.
    pub cycles_sans_retroaction: u64,
    /// Actions échouées (EX-C07).
    pub actions_echouees: u64,
    /// EX-A10 « trace optimiste » — dépôts effectués pour une action qui a
    /// échoué : la trace surestime, et rien dans le milieu ne le trahit.
    pub depots_sans_effet: u64,
    /// EX-A10 « trace pessimiste » — actions engagées sur une ressource qu'un
    /// autre agent venait de traiter sans que sa trace soit encore visible.
    pub reattaques: u64,
    /// EX-A10 « trace pessimiste » — actions échouées qui n'ont **rien** laissé
    /// dans le milieu. C'est la sous-estimation, symétrique de
    /// [`Mesures::depots_sans_effet`] : le milieu ignore un travail tenté, et un
    /// autre agent peut donc réattaquer la ressource.
    pub actions_sans_trace: u64,
    /// Retard de consommation maximal observé : nombre d'enregistrements entre
    /// le curseur d'un agent et la fin du journal.
    ///
    /// EX-V05 : c'est sa **dérivée** qui alerte, pas sa valeur. Un retard élevé
    /// mais décroissant est sain ; un retard faible et croissant est la seule
    /// alarme qui se tienne.
    pub retard_consommation_max: u64,
}

impl Mesures {
    /// Écart à l'optimum, **mesure seule** (scénario B).
    pub fn ecart_a_loptimum(&self) -> Option<f64> {
        if self.utilite_optimale <= 0.0 {
            return None;
        }
        Some(1.0 - self.utilite_recoltee / self.utilite_optimale)
    }

    /// Fraction d'effort mesurée hors la ressource la plus servie.
    pub fn fraction_effort_hors_dominante(&self) -> Option<f64> {
        let total: u64 = self.effort.iter().sum();
        if total == 0 {
            return None;
        }
        let dominante = *self.effort.iter().max().unwrap_or(&0);
        Some((total - dominante) as f64 / total as f64)
    }
}

/// Charge des événements du mécanisme.
#[derive(Clone, Copy, Debug)]
pub enum Evt {
    /// L'agent démarre un cycle.
    Cycle,
    /// Accusé de durabilité d'une écriture.
    Durabilite(Ecriture),
}

/// Le fourragement stigmergique complet.
pub struct Fourragement {
    /// Les paramètres de l'exécution.
    pub params: Params,
    /// Le journal partitionné dans lequel les agents déposent et lisent.
    pub milieu: Milieu,
    /// Les ressources à exploiter, avec leur utilité et leur partition.
    pub ressources: Vec<Ressource>,
    /// Les grandeurs mesurées — toutes des **sorties** du modèle.
    pub mesures: Mesures,
    /// Le tirage de décision de la population (EX-C19). À `part_conforme = 0`,
    /// chaque agent a sa famille et rien n'est partagé.
    pub tirage: TirageDeDecision,
    agents: Vec<Agent>,
    granularite: Granularite,
    bascule_faite: bool,
    /// Dernière fois qu'un agent, quel qu'il soit, a agi sur chaque ressource.
    /// Sert **uniquement** à mesurer les réattaques : c'est une vue globale,
    /// donc un privilège de l'observateur, et aucun agent n'y accède (§8.3 du PRD,
    /// EX-A12).
    derniere_action_sur: Vec<Instant>,
}

impl Fourragement {
    /// Construit l'exécution. Rend une erreur si un agent ne satisfait pas la
    /// définition d'essaim (EX-A12), ou si le réglage ne décrit aucun monde.
    ///
    /// `p = 0` est refusé ici et non plus bas : sans cette garde, un milieu à
    /// zéro partition se construit sans broncher, puis la première écriture
    /// indexe un vecteur vide dans `sim-milieu`. Un refus rendu à l'appelant
    /// vaut mieux qu'un abandon deux couches plus loin, d'autant que `p` arrive
    /// d'un lien partagé sans contrôle (EX-V09, NF-03).
    pub fn nouveau(params: Params, granularite: Granularite, alea: &mut Alea) -> Result<Self, String> {
        if params.p == 0 {
            return Err(
                "p = 0 : un journal sans partition n'est pas un milieu. Le renforcement \
                 stigmergique suppose au moins une partition où déposer (EX-M01)."
                    .to_string(),
            );
        }
        if params.m == 0 {
            return Err(
                "m = 0 : aucune ressource à exploiter. Le mécanisme du §1.2 suppose un choix \
                 entre au moins une ressource."
                    .to_string(),
            );
        }
        let milieu = Milieu::nouveau(
            params.p,
            Latence::depuis_l99(params.l99_milieu_ms),
            granularite,
        );

        let dernier = (params.m.max(2) - 1) as f64;
        let ressources: Vec<Ressource> = (0..params.m)
            .map(|j| Ressource {
                // La ressource 0 est la meilleure au départ, la dernière le
                // devient après la bascule.
                utilite: 1.0 - 0.9 * (j as f64 / params.m as f64),
                // η suit l'utilité initiale : informatif avant la bascule,
                // périmé après.
                eta: params.eta_max - (params.eta_max - params.eta_min) * (j as f64 / dernier),
                partition: if params.ressources_sur_une_partition {
                    0
                } else {
                    j % params.p
                },
            })
            .collect();
        // L'amorce ne sert plus à tirer η ; elle reste consommée une fois pour
        // que le hachage de configuration continue de distinguer les graines.
        let _ = alea.bits();

        let tirage = TirageDeDecision::nouveau(Familles::interpole(
            params.n,
            params.part_conforme,
        ));

        let perception = Perception::IntervalleMilieu {
            enregistrements_max: params.intervalle_lecture,
        };
        let mut agents = Vec::with_capacity(params.n as usize);
        for i in 0..params.n {
            // `None` — le milieu de ce scénario croît sans borne, donc il n'y a
            // pas de total fini auquel comparer l'intervalle de lecture, et la
            // garde `IntervalleMilieu` ne peut rien établir ici. C'était déjà
            // vrai avec l'ancien `u64::MAX`, qu'aucun `u32` ne pouvait
            // atteindre ; le dire par le type vaut mieux que de le cacher
            // derrière une comparaison qui a l'air d'en être une.
            let membre = Membre::nouveau(perception, params.n, None)?;
            agents.push(Agent {
                id: ActeurId(i),
                membre,
                phi: vec![params.phi_min; params.m as usize],
                curseurs: vec![0; params.p as usize],
                curseurs_valides: vec![0; params.p as usize],
                derniere_actualisation: Instant(0),
                cycles: 0,
                en_vol: Vec::new(),
            });
        }

        let mesures = Mesures {
            plancher_observe: f64::INFINITY,
            hors_dominante_observee: f64::INFINITY,
            effort: vec![0; params.m as usize],
            effort_apres_bascule: vec![0; params.m as usize],
            effort_par_tranche: vec![vec![0; params.m as usize]; NB_TRANCHES],
            ..Default::default()
        };

        Ok(Fourragement {
            derniere_action_sur: vec![Instant(0); params.m as usize],
            params,
            milieu,
            ressources,
            mesures,
            tirage,
            agents,
            granularite,
            bascule_faite: false,
        })
    }

    /// Arme les oracles du mécanisme (EX-A11b, NF-11).
    pub fn armer_oracles(&self, registre: &mut Registre) {
        registre.armer(Oracle::surete(PLANCHER, "§1.2, p. 16, 3ᵉ éd."));
        registre.armer(Oracle::surete(HORS_DOMINANTE, "§1.2, p. 16, 3ᵉ éd."));
        self.milieu.armer_oracles(registre);
    }

    /// Planifie le premier cycle de chaque agent. Les départs sont étalés sur
    /// une période : sans cela, les n agents cycleraient exactement ensemble et
    /// la contention mesurée serait un artefact du démarrage.
    pub fn amorcer(&mut self, moteur: &mut Moteur<Evt>) {
        let periode = self.periode();
        for i in 0..self.agents.len() {
            let decalage = Duree(moteur.alea.entier(periode.0.max(1)));
            let id = self.agents[i].id;
            moteur.pousser(decalage, id, Evt::Cycle);
        }
    }

    fn periode(&self) -> Duree {
        self.granularite.tics_depuis_ms(self.params.periode_cycle_ms)
    }

    /// Traite un événement. C'est la boucle de l'appelant qui l'appelle, le
    /// moteur restant passif (§5.1 du PRD).
    pub fn traiter(&mut self, moteur: &mut Moteur<Evt>, cible: ActeurId, evt: Evt) {
        match evt {
            Evt::Cycle => self.cycle(moteur, cible),
            Evt::Durabilite(e) => self.durabilite(moteur, cible, e),
        }
    }

    /// Un cycle de l'algorithme 2 : lecture d'intervalle, calcul de φ,
    /// écrêtage, tirage α/β, action, écriture.
    fn cycle(&mut self, moteur: &mut Moteur<Evt>, cible: ActeurId) {
        let i = cible.0 as usize;
        let maintenant = moteur.maintenant();
        self.appliquer_bascule(moteur);

        // Le cycle est cadencé par T, **indépendamment** de l'accusé de
        // durabilité. C'est ce qui rend T < ℓ₉₉ exprimable : un agent qui
        // redécide avant le retour de son dépôt n'a pas vu l'effet de son
        // action, et l'essaim devient aveugle (EX-A10).
        self.replanifier(moteur, cible);
        if !self.agents[i].en_vol.is_empty() {
            self.mesures.cycles_sans_retroaction += 1;
            moteur.couverture.atteindre("cycle sans rétroaction");
        }

        // 1. Lecture d'un intervalle borné du milieu (EX-A12).
        let intervalle = self.agents[i].membre.intervalle_max();
        let curseurs: Vec<(u32, u64)> = self.agents[i]
            .curseurs
            .iter()
            .enumerate()
            .map(|(p, d)| (p as u32, *d))
            .collect();
        let lus = self
            .milieu
            .lire_multi(&curseurs, intervalle, &mut moteur.alea);

        // Retard de consommation : ce que l'agent n'a pas encore vu.
        let retard: u64 = (0..self.milieu.nb_partitions())
            .map(|p| {
                self.milieu.partition(p).enregistrements().len() as u64
                    - self.agents[i].curseurs[p as usize].min(
                        self.milieu.partition(p).enregistrements().len() as u64,
                    )
            })
            .sum();
        self.mesures.retard_consommation_max = self.mesures.retard_consommation_max.max(retard);

        // 2. Décroissance depuis la dernière actualisation, puis dépôts lus.
        self.actualiser_phi(i, maintenant, &lus);

        // 3. Écrêtage.
        for phi in &mut self.agents[i].phi {
            *phi = phi.clamp(self.params.phi_min, self.params.phi_max);
        }

        // 4. Tirage α/β.
        let poids = self.poids(i);
        self.verifier_bornes(moteur, &poids);
        self.compter_incomparabilite(moteur, i, &poids);
        // EX-C19 — le uniforme du tirage α/β vient de la famille de décision,
        // non directement du générateur : deux agents d'une même famille
        // décident ensemble. À une famille par agent, c'est exactement l'ancien
        // comportement, un tirage par agent.
        // Le tour est le rang du cycle dans la boucle de cet agent, non la date :
        // les cycles sont décalés, donc deux agents ne partagent jamais un
        // instant, et une clé par instant rendrait EX-C19 inerte.
        let tour = self.agents[i].cycles;
        let u = self
            .tirage
            .uniforme(cible, "tirage α/β", tour, &mut moteur.alea);
        let choix = match Alea::pondere_avec(&poids, u) {
            Some(j) => j,
            None => {
                // Aucune ressource ne porte de poids : l'écrêtage garantit que
                // cela ne peut pas arriver, mais si cela arrivait, le
                // simulateur ne fabrique pas de choix par défaut.
                moteur.couverture.atteindre("tirage impossible — tous les poids nuls");
                return;
            }
        };

        // 5 à 7. Action et écriture, dans l'ordre déclaré (MomentTrace).
        //
        // Les deux positions ont leur mode de défaillance, et il n'y en a pas de
        // troisième : déposer avant, c'est risquer une trace sans effet ;
        // déposer après, c'est laisser une fenêtre pendant laquelle un autre
        // agent réattaque une ressource déjà traitée.
        match self.params.moment_trace {
            MomentTrace::Avant => {
                let e = self.deposer(moteur, i, choix);
                self.agents[i].en_vol.push(e);
                if !self.agir(moteur, i, choix) {
                    self.mesures.depots_sans_effet += 1;
                    moteur.couverture.atteindre("dépôt sans effet — trace optimiste");
                }
            }
            MomentTrace::Apres => {
                // La trace pessimiste dépose **ce qui a eu lieu** : une action
                // qui échoue ne laisse pas de trace, et c'est tout le contraste
                // avec la trace optimiste (EX-A10). Déposer quand même faisait
                // surestimer autant que le mode optimiste, sans le dire — et
                // `depots_sans_effet` restait à zéro parce qu'il n'était
                // incrémenté que dans l'autre branche.
                if self.agir(moteur, i, choix) {
                    let e = self.deposer(moteur, i, choix);
                    self.agents[i].en_vol.push(e);
                } else {
                    self.mesures.actions_sans_trace += 1;
                    moteur
                        .couverture
                        .atteindre("action échouée sans trace — trace pessimiste");
                }
            }
        }

        self.agents[i].cycles += 1;
        self.mesures.cycles += 1;
        self.mesures.effort[choix] += 1;
        if self.bascule_faite {
            self.mesures.effort_apres_bascule[choix] += 1;
        }
        let tranche = (moteur.evenements_consommes() as usize * NB_TRANCHES
            / moteur.budget.evenements_max.max(1) as usize)
            .min(NB_TRANCHES - 1);
        self.mesures.effort_par_tranche[tranche][choix] += 1;
        moteur.marquer(choix as u64);
    }

    /// Décroissance γ puis intégration des dépôts lus.
    ///
    /// `exp(ln γ · x)` plutôt que `pow(γ, x)` : mathématiquement identique,
    /// `ln γ` se calcule une fois par cycle au lieu d'une fois par
    /// enregistrement lu, et `exp` coûte moins que `pow`. Les deux viennent de
    /// `libm`, donc la portabilité de DT1 tient. Quand γ = 1, `ln γ = 0` et le
    /// facteur vaut 1 sans qu'aucune transcendante soit évaluée.
    fn actualiser_phi(&mut self, i: usize, maintenant: Instant, lus: &[sim_milieu::Enregistrement]) {
        let tau = self.granularite.tics_depuis_ms(self.params.fenetre_tau_ms).0.max(1) as f64;
        let ln_gamma = if self.params.gamma >= 1.0 {
            0.0
        } else {
            // Bord bas écrêté : à γ ≤ 0, `ln γ` vaut −∞ ou `NaN`, et le facteur
            // de décroissance contaminerait tous les φ, puis les poids de
            // tirage, puis les comparaisons qui les classent (PD1).
            libm::log(self.params.gamma.max(Params::GAMMA_MIN))
        };
        let decroissance = |duree: f64| {
            if ln_gamma == 0.0 {
                1.0
            } else {
                libm::exp(ln_gamma * duree / tau)
            }
        };

        let ecoule = (maintenant - self.agents[i].derniere_actualisation).0 as f64;
        let facteur = decroissance(ecoule);
        if facteur != 1.0 {
            for phi in &mut self.agents[i].phi {
                *phi *= facteur;
            }
        }
        self.agents[i].derniere_actualisation = maintenant;

        for e in lus {
            let j = e.cle as usize;
            if j >= self.agents[i].phi.len() {
                continue;
            }
            let age = (maintenant - e.date_evenement).0 as f64;
            self.agents[i].phi[j] += e.valeur * decroissance(age);
            // Le curseur avance sur ce qui a été lu, dans la partition d'où
            // l'enregistrement vient — et non dans celle de la ressource, qui
            // n'est la même que par coïncidence.
            let part = e.partition as usize;
            self.agents[i].curseurs[part] = self.agents[i].curseurs[part].max(e.decalage + 1);
        }
    }

    /// Poids de tirage w_j = φ_j^α · η_j^β.
    ///
    /// Les exposants unitaires — le réglage par défaut du scénario B — sont
    /// traités sans appel à `pow`. Ce n'est pas une approximation : `x^1` vaut
    /// exactement `x`, bit pour bit. Sur le chemin le plus chaud du produit,
    /// c'est deux transcendantes de moins par ressource et par cycle.
    fn poids(&self, i: usize) -> Vec<f64> {
        let (a, b) = (self.params.alpha, self.params.beta);
        self.agents[i]
            .phi
            .iter()
            .zip(&self.ressources)
            .map(|(phi, r)| {
                let t = if a == 1.0 { *phi } else { libm::pow(*phi, a) };
                let h = if b == 1.0 { r.eta } else { libm::pow(r.eta, b) };
                t * h
            })
            .collect()
    }

    /// EX-A11b — l'oracle porte sur la **probabilité de tirage calculée**, qui
    /// est exacte à chaque cycle, et non sur la fréquence empirique, qui
    /// fluctue. Une violation est réfutable à l'instant où elle survient, et
    /// signale soit un défaut d'implantation, soit une erreur du traité.
    fn verifier_bornes(&mut self, moteur: &mut Moteur<Evt>, poids: &[f64]) {
        let total: f64 = poids.iter().sum();
        if total <= 0.0 {
            return;
        }
        let p_min = poids.iter().fold(f64::INFINITY, |a, w| a.min(w / total));
        let p_max = poids.iter().fold(0.0f64, |a, w| a.max(w / total));
        let hors_dominante = 1.0 - p_max;

        // **La mesure d'abord, la borne ensuite.** NF-14 efface une borne, jamais
        // une mesure : les deux grandeurs observées se relèvent quel que soit
        // l'état de l'hypothèse, sans quoi un réglage qui efface la borne
        // effacerait du même geste ce qu'il fallait précisément regarder à sa
        // place.
        self.mesures.plancher_observe = self.mesures.plancher_observe.min(p_min);
        self.mesures.hors_dominante_observee = self.mesures.hors_dominante_observee.min(hors_dominante);

        let bornes = match self.params.bornes_applicables() {
            Ok(b) => b,
            // NF-14 : hypothèse violée, borne effacée. Il n'y a alors rien à
            // vérifier — et surtout pas une borne affaiblie. Le libellé ne nomme
            // plus γ : les hypothèses effaçables sont six, et le motif exact est
            // rendu par `bornes_applicables` à qui l'affiche.
            Err(_) => {
                moteur.couverture.atteindre("bornes effacées");
                return;
            }
        };

        // Tolérance d'arrondi : les bornes sont des produits de puissances, et
        // l'égalité exacte n'est pas atteignable en flottant. Le seuil est
        // relatif, donc indépendant de l'échelle des paramètres.
        let marge = 1e-12;
        if p_min < bornes.plancher_tirage * (1.0 - marge) {
            moteur.oracles.violer(
                PLANCHER,
                moteur.maintenant(),
                format!(
                    "probabilité de tirage minimale {p_min:.9} sous le plancher \
                     {:.9} — défaut d'implantation ou erreur du traité (§1.2, p. 16, 3ᵉ éd.)",
                    bornes.plancher_tirage
                ),
            );
        }
        if hors_dominante < bornes.fraction_hors_dominante * (1.0 - marge) {
            moteur.oracles.violer(
                HORS_DOMINANTE,
                moteur.maintenant(),
                format!(
                    "fraction hors dominante {hors_dominante:.9} sous la borne {:.9}",
                    bornes.fraction_hors_dominante
                ),
            );
        }
    }

    /// EX-A10 « incomparabilité M2 » — une décision entre deux ressources de
    /// partitions distinctes n'est fiable que si l'écart de φ excède la
    /// décroissance sur Δ + ℓ₉₉. En deçà, M2 ne fournit aucune relation et
    /// l'ordre relatif est sans objet.
    fn compter_incomparabilite(&mut self, moteur: &mut Moteur<Evt>, i: usize, poids: &[f64]) {
        if self.params.ressources_sur_une_partition {
            return;
        }
        let mut classes: Vec<usize> = (0..poids.len()).collect();
        // Ordre **total** sur les poids : `partial_cmp(…).unwrap_or(Equal)`
        // cesse d'être transitif dès qu'un poids vaut `NaN`, et le classement
        // dépend alors du parcours de l'algorithme de tri (PD1).
        classes.sort_by(|a, b| poids[*b].total_cmp(&poids[*a]));
        if classes.len() < 2 {
            return;
        }
        let (a, b) = (classes[0], classes[1]);
        if self.ressources[a].partition == self.ressources[b].partition {
            return;
        }
        let tau = self.granularite.tics_depuis_ms(self.params.fenetre_tau_ms).0.max(1) as f64;
        let fenetre = self.granularite.tics_depuis_ms(self.params.l99_milieu_ms).0 as f64;
        // Même écrêtage du bord bas que dans `actualiser_phi` : `pow` d'une base
        // négative à exposant fractionnaire rend `NaN`, et un seuil `NaN` rend
        // la comparaison fausse sans que rien ne le signale.
        let seuil = self.params.phi_max
            * (1.0 - libm::pow(self.params.gamma.max(Params::GAMMA_MIN), fenetre / tau));
        if (self.agents[i].phi[a] - self.agents[i].phi[b]).abs() < seuil {
            self.mesures.decisions_non_fiables += 1;
            moteur
                .couverture
                .atteindre("décision inter-partitions sous le seuil de fiabilité");
        }
    }

    /// L'agent agit sur la ressource et récolte son utilité. Rend `false` si
    /// l'action a échoué (EX-C07).
    fn agir(&mut self, moteur: &mut Moteur<Evt>, i: usize, j: usize) -> bool {
        let _ = i;
        let maintenant = moteur.maintenant();

        // Mesure de réattaque : un autre agent a-t-il traité cette ressource
        // trop récemment pour que sa trace ait pu être vue ? La fenêtre est
        // ℓ₉₉, c'est-à-dire le temps que met le milieu à rendre la trace
        // lisible. Cette comparaison est un privilège de l'observateur : aucun
        // agent ne dispose de cette information (§8.3 du PRD).
        let fenetre = self.granularite.tics_depuis_ms(self.params.l99_milieu_ms);
        if (maintenant - self.derniere_action_sur[j]) < fenetre && self.mesures.cycles > 0 {
            self.mesures.reattaques += 1;
            moteur
                .couverture
                .atteindre("réattaque d'une ressource déjà traitée");
        }
        self.derniere_action_sur[j] = maintenant;

        if moteur.alea.bernoulli(self.params.echec_action) {
            self.mesures.actions_echouees += 1;
            moteur.couverture.atteindre("action échouée");
            return false;
        }

        self.mesures.utilite_recoltee += self.ressources[j].utilite;
        self.mesures.utilite_optimale += self
            .ressources
            .iter()
            .map(|r| r.utilite)
            .fold(0.0f64, f64::max);
        true
    }

    /// Dépôt de la trace dans le milieu, et planification de l'accusé de
    /// durabilité — événement distinct de l'écriture (M3).
    fn deposer(&mut self, moteur: &mut Moteur<Evt>, i: usize, j: usize) -> Ecriture {
        let intensite = self.params.depot() * self.ressources[j].utilite;
        let id = self.agents[i].id;
        // EX-M24 — l'identité est présentée au milieu, qui l'appose. Sous
        // `identite_partagee`, tous les agents se présentent sous la session 0 :
        // le milieu appose fidèlement une identité fausse, et seul
        // `Milieu::sessions_partagees` le constate après coup.
        let identite = if self.params.identite_partagee {
            Identite::partagee(id, 0)
        } else {
            Identite::propre(id)
        };
        let e = self.milieu.ecrire(
            self.ressources[j].partition,
            j as Cle,
            intensite,
            moteur.maintenant(),
            identite,
            &mut moteur.alea,
        );
        moteur.pousser(e.delai_durabilite, id, Evt::Durabilite(e));
        e
    }

    /// Accusé de durabilité, puis validation du décalage.
    fn durabilite(&mut self, moteur: &mut Moteur<Evt>, cible: ActeurId, e: Ecriture) {
        let i = cible.0 as usize;
        self.milieu.valider(e);
        if let Some(pos) = self.agents[i]
            .en_vol
            .iter()
            .position(|v| v.partition == e.partition && v.decalage == e.decalage)
        {
            self.agents[i].en_vol.remove(pos);
        }

        // EX-A10 « rejeu » — crash entre l'action et la validation du décalage.
        if moteur.alea.bernoulli(self.params.crash_avant_validation) {
            moteur.couverture.atteindre("crash avant validation de décalage");
            // Le point de reprise reste au dernier décalage validé : au cycle
            // suivant, l'agent relit et refait. φ ne bouge pas — le dépôt est
            // idempotent par M1 + M4 — mais l'effet de l'action, lui, se
            // duplique si l'action ne l'est pas.
            self.agents[i].curseurs = self.agents[i].curseurs_valides.clone();
            if !self.params.action_idempotente {
                self.mesures.effets_dupliques += 1;
            }
        } else {
            self.agents[i].curseurs_valides = self.agents[i].curseurs.clone();
        }
    }

    fn replanifier(&mut self, moteur: &mut Moteur<Evt>, cible: ActeurId) {
        let periode = self.periode();
        moteur.pousser(periode, cible, Evt::Cycle);
    }

    /// Bascule d'utilité à mi-course : révèle si l'essaim sait désapprendre.
    fn appliquer_bascule(&mut self, moteur: &Moteur<Evt>) {
        if self.bascule_faite {
            return;
        }
        let seuil = (moteur.budget.evenements_max as f64 * self.params.bascule_a) as u64;
        if moteur.evenements_consommes() < seuil {
            return;
        }
        self.bascule_faite = true;
        // L'ordre des utilités s'inverse : ce qui était le meilleur devient le
        // pire. η ne bouge pas — seule la trace peut porter l'information.
        let n = self.ressources.len();
        for (j, r) in self.ressources.iter_mut().enumerate() {
            r.utilite = 1.0 - 0.9 * ((n - 1 - j) as f64 / n as f64);
        }
    }

    /// Vrai si la bascule d'utilité a eu lieu.
    pub fn bascule_faite(&self) -> bool {
        self.bascule_faite
    }

    /// φ **moyen sur la population**, par ressource.
    ///
    /// PD3 : c'est une grandeur de population, pas une ligne par agent. Un
    /// tableau de bord qui afficherait le φ de chaque agent serait en Θ(n)
    /// d'attention, et à n = 12 500 ce ne serait plus une console.
    pub fn phi_moyen(&self) -> Vec<f64> {
        let n = self.agents.len().max(1) as f64;
        let mut somme = vec![0.0; self.params.m as usize];
        for a in &self.agents {
            for (j, phi) in a.phi.iter().enumerate() {
                somme[j] += phi;
            }
        }
        somme.iter().map(|s| s / n).collect()
    }

    /// Indice de la ressource la plus utile — connaissance de l'observateur,
    /// jamais d'un agent (§8.3 du PRD).
    pub fn meilleure_ressource(&self) -> usize {
        self.ressources
            .iter()
            .enumerate()
            // Ordre **total** sur l'utilité — voir `compter_incomparabilite`
            // (PD1).
            .max_by(|a, b| a.1.utilite.total_cmp(&b.1.utilite))
            .map(|(j, _)| j)
            .unwrap_or(0)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-A11c — la borne nominale est celle que le traité démontre, et elle est
    /// finie. Sert d'ancre aux tests de bord qui suivent.
    #[test]
    fn les_bornes_nominales_sont_finies_et_dans_zero_un() {
        let b = Params::scenario_b().bornes_applicables().expect("réglage nominal");
        assert!(b.plancher_tirage.is_finite() && b.plancher_tirage > 0.0);
        assert!(b.plancher_tirage <= 1.0, "un plancher est une probabilité");
        assert!(b.fraction_hors_dominante.is_finite());
        assert!(b.fraction_hors_dominante >= 0.0);
    }

    /// NF-14 — le portail refuse **tout** réglage qui rendrait une probabilité
    /// hors de [0, 1], et non le seul couple φ. Un `Ok` portant `NaN` empêcherait
    /// l'oracle [`PLANCHER`] de se déclencher, et un oracle muet se lit comme un
    /// oracle satisfait.
    #[test]
    fn aucun_reglage_de_bord_ne_rend_une_probabilite_hors_domaine() {
        let bords: Vec<(&str, Params)> = vec![
            ("γ = 1", Params { gamma: 1.0, ..Params::scenario_b() }),
            // Le domaine (0, 1) a **deux** bords, et la moitié basse ne
            // produisait ni écrêtage, ni avertissement, ni refus.
            ("γ = 0", Params { gamma: 0.0, ..Params::scenario_b() }),
            ("γ < 0", Params { gamma: -0.5, ..Params::scenario_b() }),
            ("γ = NaN", Params { gamma: f64::NAN, ..Params::scenario_b() }),
            ("φ_min = 0", Params { phi_min: 0.0, ..Params::scenario_b() }),
            ("φ vide", Params { phi_min: 2.0, phi_max: 1.0, ..Params::scenario_b() }),
            ("η_max = 0", Params { eta_max: 0.0, ..Params::scenario_b() }),
            ("η nuls", Params { eta_min: 0.0, eta_max: 0.0, ..Params::scenario_b() }),
            ("η_min < 0", Params { eta_min: -0.5, ..Params::scenario_b() }),
            ("m = 0", Params { m: 0, ..Params::scenario_b() }),
            ("α < 0", Params { alpha: -1.0, ..Params::scenario_b() }),
            ("β < 0", Params { beta: -1.0, ..Params::scenario_b() }),
        ];
        for (nom, p) in bords {
            match p.bornes_applicables() {
                Err(motif) => assert!(
                    motif.contains("borne effacée"),
                    "{nom} : le refus doit porter son motif (NF-14), reçu « {motif} »"
                ),
                Ok(b) => panic!(
                    "{nom} : borne rendue applicable — plancher = {}, hors dominante = {}",
                    b.plancher_tirage, b.fraction_hors_dominante
                ),
            }
        }
    }

    /// N5, les deux bords — hors du domaine (0, 1), la calibration du dépôt
    /// rendait `+∞` à γ = 0 et `NaN` à γ < 0, sans écrêtage, sans avertissement
    /// et sans refus. Le `NaN` descendait dans φ, puis dans les poids, puis dans
    /// les comparaisons qui les classent, **où il détruisait l'ordre
    /// déterministe** (PD1).
    #[test]
    fn les_deux_bords_du_domaine_de_gamma_sont_ecretes_et_signales() {
        for gamma in [0.0, -0.5, f64::NAN] {
            let p = Params { gamma, ..Params::scenario_b() };
            let d = p.depot();
            assert!(d.is_finite() && d > 0.0, "γ = {gamma} : dépôt {d}");
            assert!(
                p.avertissements().iter().any(|a| a.contains("hors du domaine (0, 1)")),
                "γ = {gamma} : le bord bas doit être signalé"
            );
        }
        // Le bord haut, lui, reste écrêté comme avant : γ = 1 est un préréglage.
        assert!(Params { gamma: 1.0, ..Params::scenario_b() }.depot().is_finite());
        // Et le domaine utile n'est pas mangé par les gardes.
        assert!(Params::scenario_b().avertissements().is_empty());
    }

    /// PD1 — l'ordre des poids est **total**. Avec
    /// `partial_cmp(…).unwrap_or(Equal)`, un seul `NaN` rendait la comparaison
    /// non transitive, et le résultat du tri dépendait de la position du `NaN`
    /// dans l'entrée, donc du parcours de l'algorithme.
    #[test]
    fn lordre_des_poids_ne_depend_pas_de_la_position_dun_nan() {
        let trier = |mut v: Vec<f64>| {
            let mut idx: Vec<usize> = (0..v.len()).collect();
            idx.sort_by(|a, b| v[*b].total_cmp(&v[*a]));
            v = idx.iter().map(|i| v[*i]).collect();
            v
        };
        let a = trier(vec![3.0, f64::NAN, 1.0, 2.0]);
        let b = trier(vec![1.0, f64::NAN, 3.0, 2.0]);
        // Mêmes valeurs, ordres d'entrée différents, même sortie — ce que
        // `partial_cmp(…).unwrap_or(Equal)` ne donnait pas.
        assert_eq!(
            a.iter().map(|x| format!("{x}")).collect::<Vec<_>>(),
            b.iter().map(|x| format!("{x}")).collect::<Vec<_>>()
        );
        assert!(a[0].is_nan(), "l'ordre total place `NaN` à un rang fixe, {a:?}");
        assert_eq!(&a[1..], &[3.0, 2.0, 1.0]);
    }

    /// EX-A58 — la conformité de la population efface la borne, parce que le
    /// plancher suppose les tirages indépendants (tableau 21). L'effacement suit
    /// le **réglage**, jamais Φ_c mesuré (§0.1 du PRD).
    #[test]
    fn une_part_de_conformite_non_nulle_efface_la_borne() {
        assert!(Params::scenario_b().bornes_applicables().is_ok());
        for part in [0.25, 0.5, 0.75, 1.0] {
            let p = Params { part_conforme: part, ..Params::scenario_b() };
            let motif = p.bornes_applicables().expect_err("la borne doit être effacée");
            assert!(motif.contains("tirages"), "le motif doit nommer l'hypothèse violée");
        }
    }

    /// SPEC §7, clause 4 — une configuration invalide est un refus rendu à l'appelant,
    /// jamais un abandon. `p = 0` construisait un milieu à zéro partition, et
    /// c'est `sim-milieu` qui tombait à la première écriture.
    #[test]
    fn un_reglage_sans_partition_ou_sans_ressource_est_refuse_et_ne_panique_pas() {
        let mut alea = Alea::nouveau(7);
        for (nom, params) in [
            ("p = 0", Params { p: 0, ..Params::scenario_b() }),
            ("m = 0", Params { m: 0, ..Params::scenario_b() }),
            (
                "p = 0, multipartition",
                Params { p: 0, ressources_sur_une_partition: false, ..Params::scenario_b() },
            ),
        ] {
            assert!(
                Fourragement::nouveau(params, Granularite::Milli, &mut alea).is_err(),
                "{nom} devait être refusé"
            );
        }
    }

    /// EX-A11c — le plancher vaut (1/m)·(φ_min/φ_max)^α·(η_min/η_max)^β. Retrouvé
    /// à la main sur les défauts du scénario B, pour que la formule ne dérive pas
    /// sans qu'un test le dise.
    #[test]
    fn le_plancher_retrouve_la_formule_du_traite() {
        let p = Params::scenario_b();
        let attendu = (p.phi_min / p.phi_max) * (p.eta_min / p.eta_max) / p.m as f64;
        let b = p.bornes();
        assert!((b.plancher_tirage - attendu).abs() < 1e-12);
        assert!((b.fraction_hors_dominante - attendu * (p.m as f64 - 1.0)).abs() < 1e-12);
    }
}
