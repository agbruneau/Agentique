//! Vue du scénario B — Fourragement stigmergique.
//!
//! L'écran se lit de haut en bas, et **l'ordre de lecture est la
//! démonstration** : chaque section pose ce qu'elle montre, porte dessous la
//! poignée qui le met à l'épreuve, et sous la poignée le chiffre que cette
//! poignée déplace. Aucun curseur ne vit loin de sa mesure, aucune mesure
//! n'apparaît sans le geste qui la fait bouger.
//!
//! Quatre choix tiennent cette promesse :
//!
//! - **La relance suit la poignée.** Un curseur relâché relance l'exécution.
//!   Tant qu'elle n'a pas eu lieu, les chiffres affichés sont déclarés périmés
//!   — jamais un chiffre d'un réglage à côté d'une poignée d'un autre.
//! - **Une poignée ne relance rien : celle du temps.** Le curseur de tranche du
//!   §3 rejoue la seule série temporelle que la mesure produise
//!   ([`sim_agents::stigmergie::Mesures::effort_par_tranche`]) : on tire, et la
//!   figure bouge à l'image, sans exécution. Ce que l'écran ne peut pas
//!   montrer bouger, il le dit — φ n'est rendu qu'en fin d'exécution, et
//!   reconstituer son état intermédiaire ici serait de la simulation dans la
//!   vue (§5.1 du PRD).
//! - **Les deux bornes se recalculent sans exécution**, parce qu'elles ne
//!   dépendent que des réglages : elles bougent sous le doigt, et γ = 1 les
//!   efface en direct (NF-14). Un **seul** endroit de l'écran les lit ; la
//!   figure d'en dessous en traçait une seconde copie, prise à la dernière
//!   exécution, et deux lecteurs c'est un désaccord possible.
//! - **Un préréglage annonce ce qu'il déplace**, champ par champ, calculé par
//!   différence avec le nominal plutôt que décrit.
//!
//! Rien ici ne calcule un résultat : les bornes viennent de
//! [`Params::bornes_applicables`], les mesures de [`ResultatB`], les six
//! préréglages des constructeurs de [`Params`] (§5.1 du PRD). Ce fichier
//! choisit **où** poser ces valeurs.
//!
//! **Trois exceptions, toutes dans [`VueB::default`] : `n`, le budget et la
//! graine.** `n = 16` et le budget de 150 000 événements sont les défauts du
//! tableau du §7 du PRD, transcrits ici faute d'accesseur : `Params::scenario_b()`
//! pose `n = 64`, et chaque agent lisant ce que toute la population écrit,
//! l'exécution est en Θ(n²) — 64 fait payer seize fois le premier tracé à un
//! lecteur qui n'a encore rien réglé. La graine, elle, ne vient d'aucun tableau.
//! La conséquence se lit à l'écran plutôt que de se taire : aucun des six
//! préréglages n'est marqué « chargé » à l'ouverture, l'écran ne s'ouvrant sur
//! aucun d'eux, et le bouton « nominal » ramène le `n` du scénario. Les trois
//! sont déclarées dans l'onglet « Limites » (PD6), pas seulement ici.
//!
//! **Et une quatrième, qui n'est pas une valeur mais une hypothèse** :
//! `situe_la_tranche` réimplante le découpage du budget en tranches de largeur
//! égale. Son rustdoc dit ce que cela coûte ; l'onglet « Limites » le dit aussi.

use crate::{
    a_faire, bloc_pd8, cadre, colonne_de_lecture, de_la_vue, du_traite, en_clair,
    legende_des_chiffres, note, poignee, propos, schema, simule, titre, MESURE,
};
use eframe::egui;
use egui_plot::{Bar, BarChart, Plot, PlotPoint, Text};
use sim_agents::stigmergie::{Bornes, MomentTrace, Params, NB_TRANCHES};
use sim_agents::{scenario_b, ResultatB, BLOC_B};

/// Largeur en deçà de laquelle les paires de panneaux passent sur une colonne.
const ETROIT: f32 = 640.0;

/// La provenance des deux bornes du traité, telle que `sim-agents` la porte.
///
/// **Couplage par chaîne assumé et nommé**, comme `VAINQUEUR_MAILLE` au
/// scénario A. Cette crate ne contient aucun texte du traité, et une référence
/// de section et de page en est un : la seule copie qui fasse autorité est celle
/// de [`Bornes::LEGENDE`], affichée deux lignes plus bas dans le même cadre. La
/// recopier ici sans garde-fou a déjà produit le défaut exact que F2 vise — le
/// panneau annonçait « p. 13 » sous une légende qui disait « p. 16 », soit deux
/// pages pour une seule source, dans un seul cadre.
///
/// Le test `la_provenance_des_bornes_suit_encore_sim_agents` échoue dès que les
/// deux divergent de nouveau. Le correctif de fond est un accesseur de
/// provenance dans `sim-agents`, hors de la portée de la vue.
const SOURCE_BORNES: &str = "§1.2, p. 16, 4ᵉ éd.";

/// Réglage complet d'une exécution : paramètres, graine, budget.
///
/// La vue le garde pour comparer ce qui est affiché à ce qui est réglé. Quand
/// les deux diffèrent, les chiffres à l'écran décrivent un réglage que
/// l'utilisateur vient de quitter, et le dire est le minimum.
type Reglage = (Params, u64, u64);

/// Un préréglage : son nom, le constructeur de `sim-agents` qui le produit, et
/// l'endroit de l'écran où son effet se lit.
type Prereglage = (&'static str, fn() -> Params, &'static str);

/// Les six préréglages, chacun avec **l'endroit de l'écran** où son effet se
/// lit.
///
/// Les paramètres viennent de `sim-agents` et ne sont pas recopiés ici. Ce que
/// cette table ajoute est la seule chose qu'aucune couche basse ne sait : sous
/// quel titre de section regarder.
const PREREGLAGES: [Prereglage; 6] = [
    (
        "nominal",
        Params::scenario_b,
        "le point de départ, celui auquel les cinq autres se comparent.",
    ),
    (
        "verrouillage (γ = 1)",
        Params::verrouillage,
        "§3 : les deux bornes s'effacent, et tirer la poignée du temps ne déplace plus l'effort \
         vers la moitié devenue la plus utile.",
    ),
    (
        "essaim aveugle (T < ℓ₉₉)",
        Params::essaim_aveugle,
        "§4 : « cycles sans rétroaction » quitte zéro.",
    ),
    (
        "rejeu",
        Params::rejeu,
        "§5 : « effets dupliqués » quitte zéro.",
    ),
    (
        "incomparabilité M2",
        Params::incomparabilite_m2,
        "§5 : la carte de φ se scinde en partitions, et « décisions non fiables » quitte zéro.",
    ),
    (
        "trace optimiste",
        Params::trace_optimiste,
        "§5 : « dépôts sans effet » quitte zéro, « réattaques » retombe.",
    ),
];

/// L'écran du scénario B.
pub struct VueB {
    params: Params,
    budget: u64,
    graine: u64,
    resultat: Option<ResultatB>,
    /// Réglage qui a produit [`VueB::resultat`] ou [`VueB::refus`]. S'il diffère
    /// du réglage courant, tout chiffre affiché est périmé.
    reglage_affiche: Option<Reglage>,
    /// Réglage et chiffre de tête de l'exécution **d'avant** : un geste se juge
    /// à son écart, pas à une valeur seule.
    avant: Option<(Params, f64)>,
    duree_ms: f64,
    /// Motif du dernier refus de configuration, s'il y en a un (EX-A12).
    refus: Option<String>,
    /// Relance dès qu'une poignée est relâchée.
    auto: bool,
    /// Tranche de temps affichée par la figure du §3. **Survit à la relance** :
    /// c'est ce qui permet de comparer deux réglages au même instant de leur
    /// exécution, et non deux fins d'exécution.
    tranche: usize,
}

impl Default for VueB {
    fn default() -> Self {
        VueB {
            // Les trois champs que cette vue pose au lieu de les lire — n, le
            // budget et la graine : voir le `//!` de tête et l'onglet
            // « Limites ». n et le budget sont les défauts du tableau du §7 du
            // PRD ; `Params::scenario_b()` pose n = 64, l'exécution est en
            // Θ(n²), et le premier tracé se paierait seize fois plus cher avant
            // le premier geste du lecteur. Le bouton « nominal » du §5 ramène le
            // n du scénario, et aucun préréglage n'est marqué « chargé » tant
            // qu'il n'a pas été cliqué.
            params: Params {
                n: 16,
                ..Params::scenario_b()
            },
            budget: 150_000,
            graine: 1,
            resultat: None,
            reglage_affiche: None,
            avant: None,
            duree_ms: 0.0,
            refus: None,
            auto: true,
            // La dernière : c'est celle sur laquelle se lit le chiffre de tête
            // du §2, et l'écran s'ouvre donc sur une figure qui le montre.
            tranche: NB_TRANCHES - 1,
        }
    }
}

impl VueB {
    /// Dessine l'écran entier.
    pub fn afficher(&mut self, ui: &mut egui::Ui) {
        // Première ouverture : l'exécution nominale part seule, pour que le
        // bandeau d'EX-V07 existe avant le premier geste plutôt qu'après.
        if self.reglage_affiche.is_none() {
            self.lancer();
        }

        // Hors de la zone défilante. EX-V07 demande un affichage permanent, et
        // un bandeau qui sort par le haut au premier défilement ne l'est plus.
        colonne_de_lecture(ui, |ui| self.bandeau(ui));
        ui.add_space(6.0);

        egui::ScrollArea::vertical().show(ui, |ui| {
            colonne_de_lecture(ui, |ui| {
                // Le schéma est **avant** la thèse, comme au scénario A et pour
                // la même raison : « un essaim stigmergique n'atteint pas
                // l'optimum » ne veut rien dire tant qu'on n'a pas vu ce qu'est
                // un essaim stigmergique. PD8 exige la présence du bloc de
                // trois, non sa position.
                en_clair(ui, BLOC_B.en_clair);
                ui.add_space(6.0);
                schema_de_la_boucle(ui);
                ui.add_space(6.0);
                bloc_pd8(ui, &BLOC_B);
                ui.add_space(6.0);
                legende_des_chiffres(ui);
                ui.add_space(10.0);
                self.section_execution(ui);
                ui.add_space(10.0);
                self.section_resultat(ui);
                ui.add_space(10.0);
                self.section_bornes(ui);
                ui.add_space(10.0);
                self.section_perception(ui);
                ui.add_space(10.0);
                self.section_modes(ui);
                ui.add_space(10.0);
                self.section_milieu(ui);
                ui.add_space(12.0);
            });
        });

        // La relance se fait après le rendu, et seulement une fois la poignée
        // relâchée : relancer à chaque image d'un glissement rendrait le
        // curseur inutilisable, et le chiffre illisible.
        if self.perime() {
            ui.ctx().request_repaint();
            if self.auto && !ui.input(|i| i.pointer.any_down()) {
                self.lancer();
            }
        }
    }

    /// Vrai quand les chiffres affichés ne décrivent plus les poignées.
    fn perime(&self) -> bool {
        match &self.reglage_affiche {
            Some((p, g, b)) => *p != self.params || *g != self.graine || *b != self.budget,
            None => true,
        }
    }

    /// Exécute le scénario avec le réglage courant.
    fn lancer(&mut self) {
        // `web_time::Instant` et non `std::time::Instant` : sur wasm32, ce
        // dernier panique à l'appel. C'est le seul endroit de l'interface qui
        // lit une horloge murale, et EX-V07 exige qu'elle soit affichée — la
        // retirer serait plus coûteux que l'adapter.
        let depart = web_time::Instant::now();
        match scenario_b(self.params.clone(), self.graine, self.budget) {
            Ok(r) => {
                // Le repère de comparaison est pris **avant** d'écraser le
                // résultat : c'est lui qui donne son écart au geste.
                if let (Some(precedent), Some((p, _, _))) = (&self.resultat, &self.reglage_affiche)
                {
                    self.avant = Some((
                        p.clone(),
                        precedent.part_effort_finale_sur_la_moitie_haute(),
                    ));
                }
                self.resultat = Some(r);
                self.refus = None;
            }
            // Un réglage refusé (EX-A12) se nomme, et vide le résultat : le
            // garder laisserait le bandeau et les chiffres décrire une
            // configuration que l'utilisateur vient de quitter.
            Err(motif) => {
                self.resultat = None;
                self.refus = Some(motif);
            }
        }
        self.reglage_affiche = Some((self.params.clone(), self.graine, self.budget));
        self.duree_ms = depart.elapsed().as_secs_f64() * 1_000.0;
    }

    /// EX-V07 — modèle de panne, synchronisme, graine, temps logique, temps
    /// mural. Épinglé au-dessus de la zone défilante, sans repli.
    ///
    /// **L'ordre des champs a été mesuré à l'écran.** Le résumé du modèle de
    /// panne venait en tête : douze paramètres, presque tous nuls au nominal,
    /// « omission 0.0000 (probabilité par message) · retard moyen 0.000 ms · … ».
    /// Quatre lignes qui repoussaient le synchronisme, le temps logique et le
    /// temps mural en bas d'un pavé de zéros, sur la seule bande de l'écran que
    /// personne ne peut faire défiler, et cela sur le premier écran de mesure du
    /// produit. Il est maintenant sur sa propre ligne, au rang de la note :
    /// EX-V07 exige qu'il soit affiché en permanence, pas qu'il passe devant les
    /// quatre autres.
    fn bandeau(&self, ui: &mut egui::Ui) {
        cadre(ui, |ui| {
            match &self.resultat {
                Some(r) => {
                    ui.horizontal_wrapped(|ui| {
                        ui.label("synchronisme : asynchrone, Δ finie mais inconnue");
                        ui.separator();
                        ui.label(format!("temps logique : {} µs", r.temps_logique));
                        ui.separator();
                        ui.label(format!("temps mural : {:.0} ms", self.duree_ms));
                    });
                    // Le modèle **actif**, pas une phrase constante : EX-V07
                    // demande ce qui tourne, et les préréglages ne règlent pas
                    // tous le même modèle.
                    note(ui, &format!("modèle de panne : {}", r.modele_de_panne));
                    ui.label(egui::RichText::new(&r.entete).monospace().weak().small());
                    for v in &r.violations {
                        ui.label(
                            egui::RichText::new(format!("violation d'oracle — {v}"))
                                .color(ui.visuals().error_fg_color),
                        );
                    }
                }
                None => {
                    ui.label(
                        egui::RichText::new(
                            "aucune exécution : le bandeau d'EX-V07 décrit ce qui tourne, et rien \
                             ne tourne.",
                        )
                        .color(ui.visuals().warn_fg_color),
                    );
                }
            }

            // EX-V11 — la graine n'est ni mesurée ni citée : c'est une entrée de
            // l'écran, et elle porte donc la troisième grammaire.
            de_la_vue(
                ui,
                "graine",
                format!("{}", self.graine),
                "réglable au §1 — deux graines donnent deux tirages, pas deux modèles",
            );

            if let Some(motif) = &self.refus {
                ui.label(
                    egui::RichText::new(format!("configuration refusée — {motif}"))
                        .color(ui.visuals().error_fg_color),
                );
            }

            // Les avertissements sont ici et non sous la poignée qui les
            // déclenche : ils portent sur l'exécution entière, et deux d'entre
            // eux naissent d'un *rapport* entre deux poignées de sections
            // différentes. Ils viennent des paramètres courants, pas du
            // résultat, donc ils apparaissent pendant le glissement — avant la
            // relance, et non après.
            for a in self.params.avertissements() {
                ui.label(egui::RichText::new(format!("⚠ {a}")).color(ui.visuals().warn_fg_color));
            }

            if self.perime() {
                ui.label(
                    egui::RichText::new(if self.auto {
                        "réglage modifié — les chiffres ci-dessous datent du réglage précédent, \
                         relance dès que la poignée est relâchée."
                    } else {
                        "réglage modifié — les chiffres ci-dessous datent du réglage précédent. \
                         Relance automatique décochée : cliquez « Lancer »."
                    })
                    .color(ui.visuals().warn_fg_color),
                );
            }
        });
    }

    /// §1 — ce qui déclenche une exécution, et ce qui la rend rejouable.
    fn section_execution(&mut self, ui: &mut egui::Ui) {
        cadre(ui, |ui| {
            titre(ui, "1", "L'exécution");
            propos(
                ui,
                "À réglages et graine identiques, deux exécutions rendent les mêmes chiffres, bit \
                 pour bit : rien ici ne dépend de l'horloge (PD1). Changer la graine ne change \
                 que le tirage — c'est la façon de voir ce que le hasard, seul, déplace.",
            );
            a_faire(
                ui,
                "Relancez deux fois sans rien toucher : les chiffres sont identiques. Changez la \
                 graine seule, relancez : ils bougent, et la conclusion de la section 2 ne bouge \
                 pas. C'est la différence entre un résultat et un tirage.",
            );

            poignee(
                ui,
                "n — la population",
                "nombre d'agents. Chacun lit ce que toute la population écrit : doubler n \
                 quadruple à peu près le coût d'une exécution.",
                |ui| ui.add(egui::Slider::new(&mut self.params.n, 4..=256)),
            );

            ui.horizontal_wrapped(|ui| {
                ui.label("graine");
                let _ = ui.add(egui::DragValue::new(&mut self.graine));
                ui.separator();
                ui.label("budget (événements)");
                let _ = ui.add(egui::DragValue::new(&mut self.budget).range(10_000..=2_000_000));
            });
            note(
                ui,
                "Le budget borne l'exécution en événements, jamais en secondes : c'est ce qui la \
                 rend reproductible d'une machine à l'autre (NF-12).",
            );

            ui.add_space(6.0);
            ui.horizontal_wrapped(|ui| {
                if ui.button("Lancer").clicked() {
                    self.lancer();
                }
                ui.checkbox(&mut self.auto, "relancer dès qu'une poignée est relâchée");
            });
        });
    }

    /// §2 — le chiffre auquel tout l'écran répond.
    fn section_resultat(&mut self, ui: &mut egui::Ui) {
        cadre(ui, |ui| {
            titre(ui, "2", "Ce que l'essaim a fait");
            propos(
                ui,
                "À mi-parcours, les utilités basculent : la moitié des ressources la moins bonne \
                 au départ devient la meilleure. L'heuristique η, elle, ne bouge pas — elle \
                 continue de désigner l'ancienne bonne moitié. La trace tire vers le présent, \
                 l'heuristique vers le passé, et un seul chiffre dit lequel l'emporte.",
            );

            let Some(r) = &self.resultat else {
                ui.label("Aucun chiffre : la dernière configuration a été refusée.");
                return;
            };

            let part = r.part_effort_finale_sur_la_moitie_haute();
            mesure_de_tete(
                ui,
                "part de l'effort final dirigée vers la moitié devenue la plus utile",
                format!("{part:.3}"),
            );
            // Le seuil n'est pas retapé : `suit_la_bascule` le porte, et une
            // grandeur du modèle recopiée ici finirait par diverger sans
            // qu'aucun test ne le voie.
            ui.label(if r.suit_la_bascule() {
                "La majorité de cet effort porte sur la moitié devenue la plus utile : l'essaim a \
                 suivi la bascule."
            } else {
                "La majorité de cet effort porte encore sur l'ancienne bonne moitié : l'essaim n'a \
                 pas suivi la bascule."
            });
            if !r.bascule_faite {
                ui.label(
                    egui::RichText::new(
                        "la bascule d'utilité n'a pas eu lieu : le budget d'événements s'est \
                         épuisé avant elle. Le chiffre ci-dessus ne mesure rien.",
                    )
                    .color(ui.visuals().warn_fg_color),
                );
            }

            // L'écart au geste précédent : c'est ce que le curseur vient de
            // faire, et non ce que vaut le réglage courant dans l'absolu.
            if let Some((p, valeur)) = &self.avant {
                let bouge = differences(p, &self.params);
                ui.add_space(4.0);
                ui.add(
                    egui::Label::new(if bouge.is_empty() {
                        format!("exécution précédente, même réglage : {valeur:.3}")
                    } else {
                        format!(
                            "avant ce geste : {valeur:.3} — vous avez déplacé {}",
                            bouge.join(", ")
                        )
                    })
                    .wrap(),
                );
            }

            ui.add_space(6.0);
            simule(
                ui,
                "cycles d'agent",
                format!("{}", r.mesures.cycles),
                "comptage",
            );
            simule(
                ui,
                "écart à l'optimum — mesure seule, sans borne",
                match r.mesures.ecart_a_loptimum() {
                    Some(e) => format!("{e:.3}"),
                    None => "provenance absente".to_string(),
                },
                "fraction",
            );
        });
    }

    /// §3 — les deux bornes du traité, et les poignées qui les déplacent ou les
    /// effacent.
    fn section_bornes(&mut self, ui: &mut egui::Ui) {
        cadre(ui, |ui| {
            titre(
                ui,
                "3",
                "Les deux bornes du traité, et les poignées qui les déplacent",
            );
            propos(
                ui,
                "Ces deux nombres ne dépendent d'aucune exécution : ils se recalculent sous vos \
                 doigts, à partir de φ_min, φ_max, α, β et du nombre de ressources. γ, lui, ne \
                 les déplace pas — porté à 1, il les efface.",
            );
            a_faire(
                ui,
                "Commencez par γ, et portez-le à 1,00 : c'est le seul des cinq curseurs qui \
                 efface les bornes au lieu de les déplacer. Les quatre autres les font glisser \
                 sous le doigt, sans relancer quoi que ce soit.",
            );

            // Le γ nominal vient du constructeur de `sim-agents`, jamais d'une
            // valeur retapée en prose.
            let nominal_gamma = Params::scenario_b().gamma;
            poignee(
                ui,
                "γ — ce qui reste d'une trace après une fenêtre τ",
                &format!(
                    "au nominal {nominal_gamma:.2} : le reste s'évapore à chaque fenêtre. \
                     À 1,00, plus rien ne s'oublie et le traité ne démontre plus rien — regardez \
                     les deux bornes disparaître."
                ),
                |ui| ui.add(egui::Slider::new(&mut self.params.gamma, 0.50..=1.00).step_by(0.01)),
            );
            poignee(
                ui,
                "τ — la durée de cette fenêtre",
                "l'unité de temps de l'oubli, en millisecondes. Longue, la trace persiste ; \
                 courte, elle s'évapore entre deux cycles.",
                |ui| {
                    ui.add(
                        egui::Slider::new(&mut self.params.fenetre_tau_ms, 10.0..=60_000.0)
                            .logarithmic(true)
                            .suffix(" ms"),
                    )
                },
            );
            poignee(
                ui,
                "φ_min — le plancher de la trace",
                "aucune ressource ne descend en dessous : c'est ce qui empêche l'essaim \
                 d'abandonner définitivement une piste. Le rapport φ_min/φ_max fonde les deux \
                 bornes.",
                |ui| {
                    ui.add(
                        egui::Slider::new(&mut self.params.phi_min, 1e-4..=1.0).logarithmic(true),
                    )
                },
            );
            poignee(
                ui,
                "α — le poids de la trace",
                "combien l'agent écoute ce que l'essaim vient de faire. Élevé, il suit le groupe.",
                |ui| ui.add(egui::Slider::new(&mut self.params.alpha, 0.0..=5.0).step_by(0.1)),
            );
            poignee(
                ui,
                "β — le poids de l'heuristique",
                "combien l'agent écoute ce qu'il croyait savoir avant de commencer. Après la \
                 bascule, cette croyance est périmée : β élevé retient l'essaim dans le passé.",
                |ui| ui.add(egui::Slider::new(&mut self.params.beta, 0.0..=5.0).step_by(0.1)),
            );

            // NF-14 — **un seul lecteur** des bornes dans toute la section : ce
            // panneau, sur les paramètres vivants. La figure d'en dessous en
            // traçait une seconde copie, celle de la dernière exécution : relance
            // automatique décochée, le panneau pouvait dire « borne effacée »
            // pendant que la figure dessinait encore le plancher. Deux lecteurs,
            // c'est un désaccord possible, et NF-14 ne l'admet pas.
            ui.add_space(4.0);
            deux_colonnes(
                ui,
                |ui| {
                    egui::Frame::group(ui.style()).show(ui, |ui| {
                        ui.label(egui::RichText::new("Ce que le traité démontre").strong());
                        match self.params.bornes_applicables() {
                            Ok(Bornes {
                                plancher_tirage,
                                fraction_hors_dominante,
                            }) => {
                                du_traite(
                                    ui,
                                    "plancher d'exploration",
                                    format!("{plancher_tirage:.6}"),
                                    SOURCE_BORNES,
                                );
                                du_traite(
                                    ui,
                                    "fraction d'effort hors dominante",
                                    format!("{fraction_hors_dominante:.6}"),
                                    SOURCE_BORNES,
                                );
                            }
                            // NF-14 : la borne est **effacée**, pas grisée ni
                            // pointillée — y compris quand la mesure est
                            // meilleure qu'elle.
                            Err(motif) => {
                                ui.label(
                                    egui::RichText::new(motif).color(ui.visuals().warn_fg_color),
                                );
                            }
                        }
                        ui.add_space(4.0);
                        ui.add(
                            egui::Label::new(
                                egui::RichText::new(Bornes::LEGENDE).italics().small(),
                            )
                            .wrap(),
                        );
                    });
                    // EX-V22 — Φ_c au même rang que les bornes, avec sa précision,
                    // sa structure en regard et « seuil inconnu ». Jamais une
                    // couleur, jamais une zone, jamais un mot de jugement : le
                    // traité n'a aucune mesure du seuil et juge probable qu'il
                    // n'y en ait pas un seul (PD5).
                    ui.add_space(4.0);
                    egui::Frame::group(ui.style()).show(ui, |ui| {
                        ui.label(egui::RichText::new("Conformité de la population").strong());
                        match &self.resultat {
                            Some(r) => match &r.conformite {
                                Ok(c) => {
                                    simule(
                                        ui,
                                        "Φ_c",
                                        format!("{:.4}", c.phi_c),
                                        &format!(
                                            "± {:.4} sur {} paires",
                                            c.precision().unwrap_or(f64::NAN),
                                            c.paires
                                        ),
                                    );
                                    ui.add(
                                        egui::Label::new(
                                            egui::RichText::new(&r.diversite).italics().small(),
                                        )
                                        .wrap(),
                                    );
                                    ui.add(
                                        egui::Label::new(
                                            egui::RichText::new(
                                                sim_agents::conformite::CONSTAT_DE_MESURE,
                                            )
                                            .italics()
                                            .small()
                                            .weak(),
                                        )
                                        .wrap(),
                                    );
                                }
                                Err(motif) => {
                                    ui.label(
                                        egui::RichText::new(motif)
                                            .color(ui.visuals().warn_fg_color),
                                    );
                                }
                            },
                            None => {
                                ui.label(
                                    egui::RichText::new("aucune exécution — Φ_c jamais observé")
                                        .weak(),
                                );
                            }
                        }
                    });
                },
                |ui| {
                    egui::Frame::group(ui.style()).show(ui, |ui| {
                        ui.label(egui::RichText::new("Ce que l'exécution mesure").strong());
                        match &self.resultat {
                            Some(r) => {
                                simule(
                                    ui,
                                    "plancher observé",
                                    jamais_vu(r.mesures.plancher_observe),
                                    "probabilité de tirage",
                                );
                                simule(
                                    ui,
                                    "hors dominante observée",
                                    jamais_vu(r.mesures.hors_dominante_observee),
                                    "fraction",
                                );
                                simule(
                                    ui,
                                    "effort hors dominante, sur toute l'exécution",
                                    match r.mesures.fraction_effort_hors_dominante() {
                                        Some(f) => format!("{f:.3}"),
                                        None => "—".to_string(),
                                    },
                                    "fraction",
                                );
                            }
                            None => {
                                ui.label("aucune exécution à comparer aux bornes.");
                            }
                        }
                    });
                },
            );

            if let Some(r) = &self.resultat {
                ui.add_space(6.0);
                effort_a_la_tranche(ui, r, &mut self.tranche, self.params.bascule_a);
            }
        });
    }

    /// §4 — ce que l'essaim perçoit, et à quel retard.
    fn section_perception(&mut self, ui: &mut egui::Ui) {
        cadre(ui, |ui| {
            titre(ui, "4", "Ce que l'essaim voit, et avec quel retard");
            propos(
                ui,
                "Un agent ne voit pas l'essaim : il lit un journal. Entre le moment où il dépose \
                 une trace et celui où les autres peuvent la lire, il s'écoule ℓ₉₉. S'il redécide \
                 plus vite que ça, la rétroaction n'a pas le temps de revenir.",
            );
            a_faire(
                ui,
                "Descendez T sous ℓ₉₉ : le bandeau du haut le signale avant même la relance, et \
                 le compteur de cycles sans rétroaction quitte zéro juste en dessous.",
            );

            poignee(
                ui,
                "T — la période de cycle d'un agent",
                "le temps entre deux décisions du même agent. Descendez-la sous ℓ₉₉ : l'agent \
                 redécide avant d'avoir pu se relire, le bandeau du haut le signale, et le \
                 compteur de cycles sans rétroaction quitte zéro.",
                |ui| {
                    ui.add(
                        egui::Slider::new(&mut self.params.periode_cycle_ms, 1.0..=1000.0)
                            .suffix(" ms"),
                    )
                },
            );
            poignee(
                ui,
                "ℓ₉₉ du milieu — le délai avant qu'une trace soit lisible",
                "une entrée du modèle, jamais une sortie : c'est la latence qu'on impose au \
                 journal, pas celle qu'on mesure sur un agent. Le ℓ₉₉ de réponse d'un agent est \
                 une autre grandeur, et l'écran ne l'affiche pas (§8.3 du PRD).",
                |ui| {
                    ui.add(
                        egui::Slider::new(&mut self.params.l99_milieu_ms, 1.0..=500.0)
                            .suffix(" ms"),
                    )
                },
            );

            if let Some(r) = &self.resultat {
                ui.add_space(4.0);
                simule(
                    ui,
                    "cycles sans rétroaction",
                    format!("{}", r.mesures.cycles_sans_retroaction),
                    "comptage",
                );
                simule(
                    ui,
                    "retard de consommation max",
                    format!("{}", r.mesures.retard_consommation_max),
                    "enregistrements",
                );
                note(
                    ui,
                    "Un retard élevé mais décroissant est sain ; c'est sa dérivée qui alerte, pas \
                     sa valeur (EX-V05, non tracée ici).",
                );
            }
        });
    }

    /// §5 — les modes de défaillance, leurs préréglages et les compteurs qui
    /// les attrapent.
    fn section_modes(&mut self, ui: &mut egui::Ui) {
        cadre(ui, |ui| {
            titre(ui, "5", "Les façons dont le mécanisme casse");
            propos(
                ui,
                "Chaque bouton charge un réglage entier, pas un curseur. Sous chacun, ce qu'il \
                 déplace par rapport au nominal — calculé, pas décrit — puis l'endroit de l'écran \
                 où l'effet se lit.",
            );
            a_faire(
                ui,
                "Chargez un préréglage, allez lire le compteur qu'il nomme, puis reprenez \
                 « nominal ». Un seul compteur doit quitter zéro : c'est la façon de vérifier que \
                 le mode de défaillance est bien celui qui est écrit, et non un effet de bord.",
            );

            let nominal = Params::scenario_b();
            for (nom, fabrique, ou_regarder) in PREREGLAGES {
                let cible = fabrique();
                let actif = cible == self.params;
                ui.horizontal_wrapped(|ui| {
                    // Le préréglage est pris **entier**. Reporter `n` de
                    // l'écran dessus cassait `verrouillage()`, dont
                    // `depot_unitaire` est calibré sur le n du préréglage : γ
                    // cessait d'être la seule variable qui change, ce que ce
                    // préréglage existe pour tenir.
                    if ui.add(egui::Button::new(nom).selected(actif)).clicked() {
                        self.params = cible.clone();
                    }
                    if actif {
                        ui.label(egui::RichText::new("chargé").weak().small());
                    }
                });
                let bouge = differences(&nominal, &cible);
                note(
                    ui,
                    &if bouge.is_empty() {
                        "identique au nominal.".to_string()
                    } else {
                        format!("déplace : {}", bouge.join(", "))
                    },
                );
                note(ui, ou_regarder);
                ui.add_space(6.0);
            }

            ui.separator();
            poignee(
                ui,
                "Moment de la trace — avant ou après l'action",
                "les deux positions ont un mode de défaillance, et il n'y a pas de troisième \
                 option. Avant : la trace est déposée même si l'action échoue. Après : un autre \
                 agent réattaque une ressource déjà traitée.",
                |ui| {
                    ui.horizontal(|ui| {
                        let mut r = ui.selectable_value(
                            &mut self.params.moment_trace,
                            MomentTrace::Apres,
                            "après l'action",
                        );
                        r |= ui.selectable_value(
                            &mut self.params.moment_trace,
                            MomentTrace::Avant,
                            "avant l'action",
                        );
                        r
                    })
                    .inner
                },
            );

            let Some(r) = &self.resultat else { return };
            ui.add_space(4.0);
            simule(
                ui,
                "effets dupliqués",
                format!("{}", r.mesures.effets_dupliques),
                "comptage",
            );
            simule(
                ui,
                "dépôts sans effet",
                format!("{}", r.mesures.depots_sans_effet),
                "comptage",
            );
            simule(
                ui,
                "réattaques",
                format!("{}", r.mesures.reattaques),
                "comptage",
            );
            simule(
                ui,
                "décisions non fiables (M2)",
                format!("{}", r.mesures.decisions_non_fiables),
                "comptage",
            );

            ui.add_space(6.0);
            carte_de_chaleur(ui, r);
        });
    }

    /// §6 — ce que le milieu coûte, compté à part.
    fn section_milieu(&mut self, ui: &mut egui::Ui) {
        cadre(ui, |ui| {
            titre(ui, "6", "Ce que le milieu coûte");
            propos(
                ui,
                "Ces trois compteurs ne sont jamais additionnés aux messages point à point : un \
                 tour de journal et un message ne sont pas la même dépense, et les confondre \
                 rendrait toute comparaison fausse (EX-M13).",
            );
            let Some(r) = &self.resultat else { return };
            simule(
                ui,
                "écritures",
                format!("{}", r.couts_milieu.ecritures),
                "comptage",
            );
            simule(
                ui,
                "tours de journal",
                format!("{}", r.couts_milieu.tours_journal),
                "comptage",
            );
            simule(
                ui,
                "octets lus",
                format!("{}", r.couts_milieu.octets_lus),
                "octets",
            );
        });
    }
}

// ---------------------------------------------------------------------------
// Ce qu'un réglage déplace
// ---------------------------------------------------------------------------

/// Les champs d'un réglage que l'écran sait montrer, sous forme comparable.
///
/// Sert de base à [`differences`] : un préréglage annonce alors ce qu'il change
/// au lieu de le décrire, et la description ne peut pas mentir sur le code.
fn empreinte(p: &Params) -> [(&'static str, String); 13] {
    [
        ("n", p.n.to_string()),
        ("γ", format!("{:.2}", p.gamma)),
        ("φ_min", format!("{:.4}", p.phi_min)),
        ("α", format!("{:.1}", p.alpha)),
        ("β", format!("{:.1}", p.beta)),
        ("T", format!("{:.0} ms", p.periode_cycle_ms)),
        ("τ", format!("{:.0} ms", p.fenetre_tau_ms)),
        ("ℓ₉₉", format!("{:.0} ms", p.l99_milieu_ms)),
        (
            "moment de la trace",
            match p.moment_trace {
                MomentTrace::Avant => "avant l'action",
                MomentTrace::Apres => "après l'action",
            }
            .to_string(),
        ),
        (
            "crash avant validation",
            format!("{:.2}", p.crash_avant_validation),
        ),
        (
            "action idempotente",
            oui_non(p.action_idempotente).to_string(),
        ),
        (
            "ressources sur une partition",
            oui_non(p.ressources_sur_une_partition).to_string(),
        ),
        (
            "dépôt unitaire",
            match p.depot_unitaire {
                Some(q) => format!("fixé à {q:.3e}"),
                None => "calibré".to_string(),
            },
        ),
    ]
}

/// « oui » ou « non », pour l'empreinte.
fn oui_non(v: bool) -> &'static str {
    if v {
        "oui"
    } else {
        "non"
    }
}

/// Ce qui change entre deux réglages, champ par champ.
///
// ponytail: « de … à … » plutôt qu'une flèche — les polices embarquées par
// `eframe` n'ont pas U+2192, et un caractère absent se rend en carré vide. Un
// glyphe manquant dans le seul endroit de l'écran qui explique un geste est un
// défaut d'affichage, pas un détail de typographie.
fn differences(avant: &Params, apres: &Params) -> Vec<String> {
    empreinte(avant)
        .into_iter()
        .zip(empreinte(apres))
        .filter(|((_, a), (_, b))| a != b)
        .map(|((nom, a), (_, b))| format!("{nom} : {a} puis {b}"))
        .collect()
}

// ---------------------------------------------------------------------------
// Les briques propres à cet écran
// ---------------------------------------------------------------------------

/// La boucle stigmergique, **dessinée** — le mécanisme que tout l'écran mesure.
///
/// C'est la définition du mot « stigmergie », et elle tient en deux flèches :
/// l'agent dépose dans le milieu, le milieu se relit plus tard. Il n'y a
/// **aucune flèche entre deux agents**, et c'est cette absence qui fait le
/// mécanisme — un paragraphe la dit en trois lignes, un dessin en zéro.
///
/// Rien n'entre ici : ni φ mesuré, ni γ réglé, ni ℓ₉₉. Les symboles écrits dans
/// les deux boîtes nomment les curseurs plus bas et n'en portent pas la valeur,
/// pour la même raison que le schéma du scénario A est figé — une figure qui
/// bouge sans mesurer est une affordance qui ment (PD6).
fn schema_de_la_boucle(ui: &mut egui::Ui) {
    let petite = egui::TextStyle::Small.resolve(ui.style());
    let corps = egui::TextStyle::Body.resolve(ui.style());

    schema(
        ui,
        150.0,
        "Schéma du mécanisme, sans aucune grandeur : les lettres nomment les curseurs des \
         sections 3 et 4, elles n'en montrent pas la valeur. Ce qu'il ne montre pas : le nombre \
         d'agents — ils font tous la même chose —, la partition qui porte chaque trace, et le \
         fait qu'un agent peut relire une trace qui n'est pas encore la sienne.",
        move |p, r, v| {
            let encre = v.text_color();
            let large = (r.width() * 0.32).min(280.0);
            let y = r.center().y + 6.0;
            let agent = egui::Rect::from_center_size(
                egui::pos2(r.left() + r.width() * 0.22, y),
                egui::vec2(large, 76.0),
            );
            let milieu = egui::Rect::from_center_size(
                egui::pos2(r.right() - r.width() * 0.22, y),
                egui::vec2(large, 76.0),
            );
            let trait_boite = egui::Stroke::new(1.0_f32, encre);
            p.rect_stroke(agent, 4.0, trait_boite);
            p.rect_stroke(milieu, 4.0, trait_boite);

            let ligne = |boite: egui::Rect, rang: f32, texte: &str, police: egui::FontId| {
                p.text(
                    egui::pos2(boite.center().x, boite.top() + 10.0 + rang * 20.0),
                    egui::Align2::CENTER_TOP,
                    texte,
                    police,
                    encre,
                );
            };
            ligne(agent, 0.0, "un agent", corps.clone());
            ligne(agent, 1.0, "il ne parle à personne", petite.clone());
            ligne(agent, 2.0, "il tire selon φ^α · η^β", petite.clone());
            ligne(milieu, 0.0, "le milieu — le journal", corps);
            ligne(milieu, 1.0, "il porte les traces φ", petite.clone());
            ligne(
                milieu,
                2.0,
                "il en oublie une part γ à chaque τ",
                petite.clone(),
            );

            // Les deux flèches, décalées de part et d'autre de l'axe : posées à
            // la même hauteur, elles se superposeraient et la boucle se lirait
            // comme un simple aller-retour.
            let fleche = egui::Stroke::new(1.6_f32, encre);
            let aller = (
                egui::pos2(agent.right(), y - 22.0),
                egui::pos2(milieu.left(), y - 22.0),
            );
            let retour = (
                egui::pos2(milieu.left(), y + 22.0),
                egui::pos2(agent.right(), y + 22.0),
            );
            p.arrow(aller.0, aller.1 - aller.0, fleche);
            p.arrow(retour.0, retour.1 - retour.0, fleche);
            p.text(
                egui::pos2((aller.0.x + aller.1.x) / 2.0, y - 28.0),
                egui::Align2::CENTER_BOTTOM,
                "il dépose une trace",
                petite.clone(),
                encre,
            );
            p.text(
                egui::pos2((retour.0.x + retour.1.x) / 2.0, y + 28.0),
                egui::Align2::CENTER_TOP,
                "il la relit — ℓ₉₉ plus tard",
                petite,
                encre,
            );
        },
    );
}

/// Deux panneaux côte à côte, empilés quand l'écran est étroit.
fn deux_colonnes(
    ui: &mut egui::Ui,
    gauche: impl FnOnce(&mut egui::Ui),
    droite: impl FnOnce(&mut egui::Ui),
) {
    if ui.available_width() < ETROIT {
        gauche(ui);
        ui.add_space(6.0);
        droite(ui);
    } else {
        ui.columns(2, |col| {
            gauche(&mut col[0]);
            droite(&mut col[1]);
        });
    }
}

/// Un minimum sur les cycles qui n'a jamais été mis à jour vaut `+∞`.
///
/// L'écrire tel quel le donnerait pour une mesure, alors que c'est l'absence
/// d'une mesure : « inf » affiché en face de « plancher observé » se lirait comme
/// un résultat (F2).
///
/// **Le cas de γ = 1 ne le produit plus.** `Fourragement::verifier_bornes` relève
/// les deux minimums avant de consulter le portail NF-14, donc une borne effacée
/// n'efface plus la mesure. La sentinelle ne subsiste que pour une exécution
/// qu'aucun cycle n'a traversée.
fn jamais_vu(v: f64) -> String {
    if v.is_finite() {
        format!("{v:.6}")
    } else {
        "jamais observé".to_string()
    }
}

/// Le chiffre auquel l'écran répond : gros, et toujours étiqueté « simulé »
/// (EX-V11).
fn mesure_de_tete(ui: &mut egui::Ui, nom: &str, valeur: String) {
    ui.add(egui::Label::new(nom).wrap());
    ui.horizontal_wrapped(|ui| {
        ui.label(egui::RichText::new(valeur).strong().size(MESURE));
        ui.label(egui::RichText::new("simulé").weak().small());
    });
}

// ---------------------------------------------------------------------------
// Les deux figures
// ---------------------------------------------------------------------------

/// EX-V08 — carte de φ **ordonnée par partition**, une couleur et une entrée de
/// légende par partition : il n'y a pas de gradient d'une partition à l'autre,
/// et une figure qui le suggérerait serait un défaut bloquant (RQ4).
///
/// Chaque étiquette est posée **au centre de son groupe**, en coordonnées de
/// tracé : la position calculée est celle qui sert, et non une position calculée
/// puis jetée au profit d'une rangée de libellés tassés à gauche. Une
/// correspondance fausse est pire qu'une absence.
fn carte_de_chaleur(ui: &mut egui::Ui, r: &ResultatB) {
    ui.label(egui::RichText::new("Trace φ par ressource, groupée par partition").strong());
    note(
        ui,
        "Une barre par ressource, en hauteur de trace φ moyenne sur la population. Les partitions \
         sont séparées et colorées à part : M2 ne garantit aucun ordre entre elles, donc comparer \
         deux barres de couleurs différentes ne veut rien dire.",
    );

    let mut partitions: Vec<u32> = r.partition_des_ressources.clone();
    partitions.sort_unstable();
    partitions.dedup();

    // Un histogramme par partition : la séparation est portée par la couleur et
    // la légende, pas seulement par un trou.
    //
    // Le remplissage est posé **barre par barre**, jamais laissé à
    // `BarChart::color` : celui-ci le rend à 20 % d'alpha, ce qui est visible
    // sur fond sombre et quasiment blanc sur fond clair — la figure qu'EX-V08
    // exige, illisible sur la moitié des postes. Mesuré aux deux thèmes.
    let mut groupes: Vec<(u32, Vec<Bar>, f64, egui::Color32)> = Vec::new();
    let mut x = 0.0f64;
    for (rang, p) in partitions.iter().enumerate() {
        let debut = x;
        let couleur = teinte_partition(rang);
        let mut barres = Vec::new();
        for (j, phi) in r.phi_moyen.iter().enumerate() {
            if r.partition_des_ressources[j] != *p {
                continue;
            }
            barres.push(
                Bar::new(x, *phi)
                    .width(0.72)
                    .fill(couleur)
                    .stroke(egui::Stroke::new(1.0_f32, couleur))
                    .name(format!("ressource {j} — partition {p}")),
            );
            x += 1.0;
        }
        let centre = ((debut + x - 1.0) / 2.0).max(debut);
        groupes.push((*p, barres, centre, couleur));
        // Le trou entre deux partitions.
        x += 1.5;
    }

    // Le socle où tombent les étiquettes : sous la plus haute barre, en fraction
    // d'elle, pour que la marge suive l'échelle au lieu d'être un nombre en dur.
    let haut = r
        .phi_moyen
        .iter()
        .copied()
        .fold(0.0_f64, f64::max)
        .max(1e-9);
    let socle = -0.16 * haut;

    // Aucune légende en cartouche : `Legend` se pose par défaut en haut à droite,
    // c'est-à-dire **sur les barres les plus hautes** — mesuré à 500 px, le
    // cartouche recouvrait les deux ressources dominantes, celles que la figure
    // existe pour montrer. La correspondance couleur ↔ partition est déjà portée
    // par l'étiquette posée au centre de chaque groupe, qui ne recouvre rien.
    Plot::new("phi_par_partition")
        .height(180.0)
        .show_axes([false, true])
        .allow_drag(false)
        .allow_zoom(false)
        .allow_scroll(false)
        .allow_boxed_zoom(false)
        .include_y(socle)
        .show(ui, |plot| {
            for (p, barres, centre, couleur) in groupes {
                plot.bar_chart(
                    BarChart::new(barres)
                        .name(format!("partition {p}"))
                        .color(couleur),
                );
                plot.text(
                    Text::new(
                        PlotPoint::new(centre, socle * 0.55),
                        egui::RichText::new(format!("partition {p}")).small(),
                    )
                    .anchor(egui::Align2::CENTER_CENTER),
                );
            }
        });
}

/// La teinte d'une partition, par rang dans la figure.
///
/// Le cycle par nombre d'or est celui qu'`egui_plot` attribue de lui-même ; il
/// est repris ici parce que la couleur automatique passe par
/// `BarChart::color`, qui remplit à 20 % d'alpha. La teinte est posée à pleine
/// opacité sur la barre, et la même sert la légende : la correspondance
/// couleur ↔ partition reste vraie des deux côtés.
fn teinte_partition(rang: usize) -> egui::Color32 {
    const NOMBRE_DOR: f32 = 0.618_034;
    // `S = 0,85`, `V = 0,50` : assez sombre pour tenir sur fond clair, assez
    // saturé pour tenir sur fond sombre. Vérifié aux deux thèmes.
    egui::ecolor::Hsva::new((rang as f32 * NOMBRE_DOR).fract(), 0.85, 0.5, 1.0).into()
}

/// La répartition de l'effort **à une tranche**, et la poignée qui déplace la
/// tranche.
///
/// C'est la seule figure de l'écran qui bouge sans relancer : les tranches sont
/// déjà dans le résultat, et le curseur les rejoue à l'image. C'est là que le
/// mécanisme se voit *dans le temps* — l'effort quitte l'ancienne bonne moitié
/// après la bascule, ou refuse de la quitter quand γ = 1.
///
/// Ses deux absences — φ lui-même et le plancher du traité — sont écrites **sous
/// la figure**, à l'écran, plutôt que comblées (PD6, F1) ; elles ne sont pas
/// répétées ici. La conséquence de code est qu'elle ne lit **aucune** borne, ce
/// qui lui interdit d'en dessiner une que le panneau vient d'effacer (NF-14), et
/// qu'elle n'a pas de légende : le tracé ne contient que du simulé, dit une fois
/// dans le libellé au-dessus, et une légende de dix entrées sur une figure de
/// 500 px en recouvrait les deux tiers (EX-V11).
fn effort_a_la_tranche(ui: &mut egui::Ui, r: &ResultatB, tranche: &mut usize, bascule_a: f64) {
    let series = &r.mesures.effort_par_tranche;
    let Some(derniere) = series.len().checked_sub(1) else {
        return;
    };
    *tranche = (*tranche).min(derniere);

    // Part de l'effort d'une tranche revenant à une ressource : la
    // normalisation d'un compte déjà affiché, et rien d'autre.
    let part = |t: &[u64], j: usize| {
        let total: u64 = t.iter().sum();
        if total == 0 {
            0.0
        } else {
            t[j] as f64 / total as f64
        }
    };

    let vedette = r.meilleure_ressource;
    ui.label(egui::RichText::new("L'effort à une tranche, et la poignée du temps").strong());
    note(
        ui,
        &format!(
            "Une barre par ressource : la part de l'effort de cette tranche qui lui revient \
             (simulé), de 0 à 1. Celle qui est en évidence est la ressource n° {vedette}, la plus \
             servie en fin d'exécution. L'axe vertical ne bouge jamais — c'est ce qui rend deux \
             tranches, et deux réglages, comparables à l'œil."
        ),
    );

    let courante = &series[*tranche];
    // Remplissage posé barre par barre, et non par `BarChart::color` : celui-ci
    // rend le fond à 20 % d'alpha, ce qui est visible sur fond sombre et
    // quasiment blanc sur fond clair. Mesuré aux deux thèmes.
    let (vif, terne) = (ui.visuals().hyperlink_color, egui::Color32::GRAY);
    let barres: Vec<Bar> = (0..courante.len())
        .map(|j| {
            Bar::new(j as f64, part(courante, j))
                .width(0.7)
                .fill(if j == vedette { vif } else { terne })
                .name(format!("ressource {j}"))
        })
        .collect();
    Plot::new("effort_a_la_tranche")
        .height(200.0)
        // Axe horizontal masqué, comme la carte de φ : les graduations d'un
        // indice de ressource n'ont pas de valeur intermédiaire à afficher.
        .show_axes([false, true])
        .allow_drag(false)
        .allow_zoom(false)
        .allow_scroll(false)
        .allow_boxed_zoom(false)
        // 0 à 1, fixé : une part se lit sur son échelle naturelle, et un axe qui
        // se remet à l'échelle sous le doigt annulerait le mouvement qu'on tire
        // le curseur pour voir.
        .include_y(0.0)
        .include_y(1.0)
        .show(ui, |plot| plot.bar_chart(BarChart::new(barres)));

    poignee(
        ui,
        "tranche — la poignée du temps",
        "elle ne relance rien : ces tranches sont dans le résultat déjà calculé. Tirez-la d'un \
         bout à l'autre pour voir l'effort quitter — ou refuser de quitter — l'ancienne bonne \
         moitié. Elle survit à la relance : chargez un préréglage, la tranche reste, et les deux \
         exécutions se comparent au même instant.",
        |ui| ui.add(egui::Slider::new(tranche, 0..=derniere)),
    );
    ui.add(
        egui::Label::new(format!(
            "tranche {} sur {} — {}",
            *tranche + 1,
            series.len(),
            situe_la_tranche(*tranche, series.len(), bascule_a, r.bascule_faite)
        ))
        .wrap(),
    );
    simule(
        ui,
        &format!("part de cette tranche revenant à la ressource {vedette}"),
        format!("{:.3}", part(courante, vedette)),
        "fraction",
    );
    note(
        ui,
        "Ce que cette figure ne montre pas : φ lui-même, ni le plancher du traité. La trace n'est \
         rendue qu'en fin d'exécution, donc son évaporation entre deux tranches n'est visible \
         nulle part ici — la recalculer dans l'interface en ferait un chiffre inventé (PD6, \
         §5.1 du PRD). Le plancher, lui, vaut quelques dix-millièmes contre des parts en \
         dixièmes : sur cet axe il se confondrait avec le zéro, et sa comparaison à échelle \
         égale est celle des deux panneaux au-dessus.",
    );
}

/// Où tombe une tranche par rapport à la bascule d'utilité.
///
/// **Hypothèse réimplantée dans la vue, et nommée ici : le budget d'événements
/// est découpé en tranches de largeur égale.** C'est ce que fait
/// `Fourragement::traiter`, qui indexe par
/// `événements_consommés × NB_TRANCHES / budget`, et c'est ce qui rend
/// comparables la fraction de budget `bascule_a` et la fraction de tranches.
/// `sim-agents` ne rend pas la tranche de bascule ; le jour où le découpage
/// cesserait d'être uniforme, cette étiquette mentirait sans qu'aucune erreur de
/// compilation ne le signale. Le correctif de fond est un accesseur dans
/// `sim-agents`, hors de la portée de la vue.
fn situe_la_tranche(
    tranche: usize,
    nb_tranches: usize,
    bascule_a: f64,
    bascule_faite: bool,
) -> &'static str {
    if !bascule_faite {
        "la bascule d'utilité n'a pas eu lieu dans cette exécution"
    } else if nb_tranches > 0 && (tranche as f64) / nb_tranches as f64 >= bascule_a {
        "après la bascule d'utilité"
    } else {
        "avant la bascule d'utilité"
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Ce qu'un préréglage annonce déplacer est calculé sur le préréglage
    /// lui-même : la ligne ne peut pas se désynchroniser du code de
    /// `sim-agents`.
    #[test]
    fn la_ligne_de_differences_nomme_ce_que_le_prereglage_deplace() {
        let nominal = Params::scenario_b();
        assert!(differences(&nominal, &nominal).is_empty());

        // `verrouillage` change γ, et fige le dépôt pour que γ reste la seule
        // variable de comportement.
        let d = differences(&nominal, &Params::verrouillage());
        assert_eq!(d.len(), 2, "{d:?}");
        assert_eq!(d[0], "γ : 0.90 puis 1.00", "{d:?}");
        assert!(
            d[1].starts_with("dépôt unitaire : calibré puis fixé"),
            "{d:?}"
        );

        // `essaim aveugle` ne touche qu'aux deux temps.
        let d = differences(&nominal, &Params::essaim_aveugle());
        assert_eq!(d.len(), 2, "{d:?}");
        assert_eq!(d[0], "T : 50 ms puis 5 ms", "{d:?}");
    }

    /// La page citée sous les deux bornes est celle que `sim-agents` porte.
    ///
    /// Ce test est le garde-fou de `SOURCE_BORNES` : le panneau du §3 et la
    /// légende d'EX-A11c sont affichés dans le même cadre, à quatre lignes l'un
    /// de l'autre, et ils ont déjà annoncé deux pages différentes pour une seule
    /// source. Une repagination du traité fait maintenant échouer ce test au
    /// lieu de laisser l'écran citer une page qui n'existe plus (F2).
    #[test]
    fn la_provenance_des_bornes_suit_encore_sim_agents() {
        assert!(
            Bornes::LEGENDE.contains(SOURCE_BORNES),
            "SOURCE_BORNES = {SOURCE_BORNES}, Bornes::LEGENDE = {}",
            Bornes::LEGENDE
        );
    }

    /// Chaque préréglage de la table désigne un endroit de l'écran, jamais rien.
    #[test]
    fn chaque_prereglage_dit_ou_regarder() {
        for (nom, _, ou) in PREREGLAGES {
            assert!(!ou.is_empty(), "{nom} n'indique aucun repère");
        }
    }

    /// La frontière de l'étiquette « avant / après » tombe bien à `bascule_a`
    /// du découpage, et l'absence de bascule l'emporte sur les deux.
    #[test]
    fn la_tranche_se_situe_de_part_et_dautre_de_la_bascule() {
        assert_eq!(
            situe_la_tranche(9, NB_TRANCHES, 0.5, true),
            "avant la bascule d'utilité"
        );
        assert_eq!(
            situe_la_tranche(10, NB_TRANCHES, 0.5, true),
            "après la bascule d'utilité"
        );
        assert_eq!(
            situe_la_tranche(19, NB_TRANCHES, 0.5, false),
            "la bascule d'utilité n'a pas eu lieu dans cette exécution"
        );
    }
}
