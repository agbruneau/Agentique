//! Vue du scénario A — Les deux régimes.
//!
//! Écran de **démonstration**, et non d'exploration : l'ordre de lecture *est*
//! la démonstration. Chaque compte du tableau 3 porte, sous son énoncé, le
//! curseur qui le déplace ; on ne cherche donc jamais ailleurs ce que fait une
//! poignée, et aucun curseur n'est posé avant l'énoncé qu'il sert.
//!
//! Le croisement est **dessiné**, pas seulement nommé : l'acte 4 trace les deux
//! temps sur toute la plage du délai d'aller simple, et leur intersection est à
//! l'écran, sous le curseur qui la déplace. Deux barres parallèles n'ont jamais
//! croisé quoi que ce soit — elles échangent leur rang, et il faut lire une
//! phrase pour savoir laquelle vient de gagner.
//!
//! Chaque point de la courbe est un appel de plus à `sim_agents::scenario_a` —
//! la vue lit la simulation autant de fois qu'il le faut, elle ne calcule
//! aucun temps et ne tranche aucun verdict (§5.1). L'abscisse du croisement
//! elle-même est lue : c'est le point où le `verdict_temps` **de `sim-agents`**
//! change de camp le long du balayage.
//!
//! Quatre comptes que le traité tient séparés (§1.1, convention de comptage).
//! `Comparaison` n'a pas d'accesseur qui les additionne, et cet écran n'a ni
//! barre empilée ni total : deux barres d'un même acte **se comparent**, elles
//! ne s'ajoutent pas (EX-M13).
//!
//! Ce que cet écran tient, en plus de son contenu :
//!
//! - **EX-V07** — bandeau permanent, sans repli, épinglé **hors de la zone
//!   défilante** et rempli dès l'ouverture : modèle de panne, synchronisme,
//!   graine, temps logique, temps mural. Il dit aussi que ce scénario n'a pas de
//!   bouton « lancer » — il se recalcule à chaque image, ce qu'aucun écran ne
//!   devrait laisser deviner.
//! - **EX-V11** — trois provenances, trois grammaires, qui ne se mélangent dans
//!   aucun champ : `simule` pour ce que la simulation produit, `du_traite` pour
//!   ce qui porte une section et une page, et `de_la_vue` pour ce qui n'est ni
//!   l'un ni l'autre — la graine, qui est une entrée de cet écran.
//! - **PD3** — le nombre de widgets ne dépend pas de n.
//! - **F1** — trois réglages du scénario ne déplacent **aucun** compte affiché.
//!   Ils sont groupés à part, sous ce titre, avec le motif de chacun, plutôt
//!   que rangés parmi ceux qui agissent. Un curseur muet placé au milieu des
//!   autres est le mensonge d'affordance que PD6 interdit ailleurs.

use crate::{
    a_faire, bloc_pd8, cadre, colonne_de_lecture, de_la_vue, du_traite, en_clair, encart,
    legende_des_chiffres, note, poignee, propos, schema, simule, titre, TITRE_SECTION,
};
use eframe::egui;
use egui_plot::{Legend, Line, Plot, PlotPoints, VLine};
use sim_agents::{scenario_a, Comparaison, BLOC_A};
use sim_core::temps::Granularite;

/// Nombre de pas du balayage de l'acte 4 — donc `POINTS_BALAYAGE + 1` appels.
///
/// 48 suffit pour deux droites, et borne le coût : chaque point est un
/// `scenario_a` complet, dont l'entretien de vue est en Θ(n). Le pas qui en
/// découle est **affiché** avec le croisement plutôt que tu — une abscisse lue
/// sur un balayage n'est juste qu'à son pas près.
const POINTS_BALAYAGE: usize = 48;

/// Plage de ℓ₉₉, en millisecondes (PRD §7, scénario A).
const PLAGE_L99: (f64, f64) = (1.0, 500.0);

/// Plage du délai d'aller simple, en millisecondes (PRD §7, scénario A). C'est
/// l'abscisse du balayage : le curseur et la courbe la lisent au même endroit,
/// une figure qui dépasserait la plage du curseur montrant un croisement
/// inatteignable.
///
/// **C'est cet axe-là qui montre le croisement, et pas ℓ₉₉** — le calcul et
/// l'arbitrage sont au registre des décisions, `docs/decisions.md`.
const PLAGE_ALLER_SIMPLE: (f64, f64) = (0.1, 50.0);

/// Graine du scénario A.
///
/// Figée, et **montrée** figée (EX-V07). Aucun compte affiché n'en dépend : les
/// comptes du tableau 3 sont des formules fermées, et le tirage ne sert qu'aux
/// pertes de messages et aux latences du détecteur, que `Comparaison` ne porte
/// pas. Un curseur de graine serait ici une poignée sans mécanisme.
const GRAINE: u64 = 1;

/// Le fragment de `Comparaison::verdict_temps` qui nomme le vainqueur en temps.
///
/// **Couplage par chaîne française, assumé et nommé.** Ce qui le casse est
/// précis : toute reformulation de `Comparaison::verdict_temps` qui n'écrit plus
/// littéralement ces quatre mots. La figure de l'acte 4 annoncerait alors
/// « aucun croisement » partout, sans une erreur de compilation — d'où le test
/// `le_vainqueur_se_lit_encore_dans_la_phrase_de_verdict`, qui échoue à sa
/// place. Le correctif de fond est au registre des décisions.
const VAINQUEUR_MAILLE: &str = "la maille gagne";

/// L'état réglable du scénario A. Six paramètres, dont quatre agissent.
pub struct VueA {
    n: u32,
    p: u32,
    l99_ms: f64,
    aller_simple_ms: f64,
    degre_depot: u32,
    taux_omission: f64,
    /// Temps mural du dernier recalcul, en millisecondes (EX-V07). Jamais un
    /// temps simulé : c'est le coût de l'image, pas celui du système modélisé.
    duree_ms: f64,
}

impl Default for VueA {
    fn default() -> Self {
        VueA {
            n: 64,
            p: 8,
            l99_ms: 20.0,
            aller_simple_ms: 2.0,
            degre_depot: 3,
            taux_omission: 0.01,
            duree_ms: 0.0,
        }
    }
}

impl VueA {
    /// Dessine l'écran entier, dans l'ordre où il se démontre.
    pub fn afficher(&mut self, ui: &mut egui::Ui) {
        // Le recalcul a lieu **avant** les curseurs, donc sur les valeurs de
        // l'image précédente. C'est ce que fait tout mode immédiat, et la seule
        // façon de placer chaque curseur sous son énoncé plutôt que tous en
        // tête.
        let depart = web_time::Instant::now();
        let c = scenario_a(
            self.n,
            self.p,
            self.l99_ms,
            self.aller_simple_ms,
            self.degre_depot,
            self.taux_omission,
            GRAINE,
        );
        self.duree_ms = depart.elapsed().as_secs_f64() * 1_000.0;

        // Hors de la zone défilante. EX-V07 demande un affichage permanent, et
        // un bandeau qui sort par le haut au premier défilement ne l'est plus.
        colonne_de_lecture(ui, |ui| bandeau(ui, &c, self.taux_omission, self.duree_ms));
        ui.add_space(6.0);

        egui::ScrollArea::vertical()
            .auto_shrink([false; 2])
            .show(ui, |ui| {
                colonne_de_lecture(ui, |ui| {
                    // L'ordre de ces six blocs est celui d'une première lecture,
                    // et il a été mesuré à l'écran plutôt que supposé : de quoi
                    // il s'agit, à quoi ça ressemble, ce que le traité en dit,
                    // comment cet écran s'exécute, comment lire ses chiffres, ce
                    // que ses couleurs veulent dire. Les quatre actes ne
                    // commencent qu'après.
                    //
                    // Le schéma est **avant** la thèse : la thèse est une phrase
                    // du traité, dans le vocabulaire du traité, et un lecteur qui
                    // n'a pas vu ce qu'est une maille ne la comprend pas. PD8
                    // exige que le bloc de trois soit là, non repliable ; il
                    // n'exige pas qu'il soit le premier pixel.
                    en_clair(ui, BLOC_A.en_clair);
                    ui.add_space(6.0);
                    schema_des_deux_regimes(ui);
                    ui.add_space(6.0);
                    bloc_pd8(ui, &BLOC_A);
                    ui.add_space(6.0);
                    comment_cet_ecran_sexecute(ui);
                    ui.add_space(6.0);
                    legende_des_chiffres(ui);
                    ui.add_space(6.0);
                    legende(ui);
                    ui.add_space(6.0);

                    let croises = c.comptes_croises();
                    let verdict =
                        |i: usize| croises.get(i).map(String::as_str).unwrap_or_default();

                    self.acte_diffusion(ui, &c, verdict(0));
                    ui.add_space(6.0);
                    self.acte_entretien(ui, &c, verdict(1));
                    ui.add_space(6.0);
                    self.acte_depot(ui, &c, verdict(2));
                    ui.add_space(6.0);
                    self.acte_temps(ui, &c);
                    ui.add_space(6.0);
                    self.reglages_muets(ui);
                    ui.add_space(12.0);
                });
            });
    }

    /// 1 — une diffusion. Tableau 3 : n − 1 messages en un tour à gauche,
    /// 1 écriture puis 1 lecture par consommateur en deux tours à droite.
    fn acte_diffusion(&mut self, ui: &mut egui::Ui, c: &Comparaison, verdict: &str) {
        acte(ui, 1, "Une diffusion", |ui| {
            propos(
                ui,
                "Un agent propage un changement à toute la population. À gauche il nomme chacun \
                 des n − 1 autres. À droite il écrit une fois, et chacun lit.",
            );
            a_faire(
                ui,
                "Tirez n : les deux comptes suivent la population, et l'écart entre eux ne bouge \
                 pas. C'est l'acte où les deux régimes se ressemblent le plus.",
            );
            curseur_n(ui, &mut self.n);
            simule(
                ui,
                "maille — un tour",
                format!("{}", c.maille_diffusion),
                "messages",
            );
            simule(
                ui,
                "journal — deux tours de journal",
                format!(
                    "{} écriture + {} lectures",
                    c.journal_ecritures, c.journal_lectures
                ),
                "opérations de journal",
            );
            paire(
                ui,
                c.maille_diffusion as f64,
                (c.journal_ecritures + c.journal_lectures) as f64,
            );
            constat(ui, verdict);
        });
    }

    /// 2 — l'entretien de la vue d'appartenance. Θ(n²) par période de sondage
    /// à gauche, aucun équivalent à droite (§1.3). C'est le terme qui explose.
    fn acte_entretien(&mut self, ui: &mut egui::Ui, c: &Comparaison, verdict: &str) {
        acte(ui, 2, "L'entretien de la vue d'appartenance", |ui| {
            propos(
                ui,
                "Nommer un destinataire suppose de savoir qui est là. La maille l'apprend par \
                 sondage : à chaque période, chaque agent sonde chaque autre. Le journal n'a rien \
                 à entretenir — le producteur n'a pas de destinataire à connaître.",
            );
            a_faire(
                ui,
                "Tirez le même n qu'à l'acte 1 : la barre de gauche croît en n², celle de droite \
                 reste vide. C'est le terme qui décide de tout le reste.",
            );
            curseur_n(ui, &mut self.n);
            simule(
                ui,
                "maille",
                format!("{}", c.maille_entretien),
                "messages par période de sondage",
            );
            simule(
                ui,
                "journal — sans équivalent, et non « négligeable »",
                format!("{}", c.journal_entretien),
                "messages par période de sondage",
            );
            paire(ui, c.maille_entretien as f64, c.journal_entretien as f64);
            constat(ui, verdict);
        });
    }

    /// 3 — un cycle où toute la population dépose : Θ(n·d) contre Θ(n) (§1.2).
    fn acte_depot(&mut self, ui: &mut egui::Ui, c: &Comparaison, verdict: &str) {
        acte(ui, 3, "Un cycle où toute la population dépose", |ui| {
            propos(
                ui,
                "Chacun des n agents dépose une fois. À gauche il nomme d destinataires ; à droite \
                 il écrit, et le compte ne dépend pas de d.",
            );
            a_faire(ui, "Tirez d : seule la barre de gauche s'allonge.");
            poignee(ui, "d — destinataires nommés par dépôt", "", |ui| {
                ui.add(egui::Slider::new(&mut self.degre_depot, 1..=32))
            });
            simule(ui, "maille", format!("{}", c.maille_depot), "messages");
            simule(ui, "journal", format!("{}", c.journal_depot), "écritures");
            paire(ui, c.maille_depot as f64, c.journal_depot as f64);
            constat(ui, verdict);
        });
    }

    /// 4 — le temps, la partie que le traité refuse d'escamoter : un aller
    /// simple contre deux tours de journal à ℓ₉₉. Le seul des quatre comptes
    /// dont le vainqueur change sous les curseurs.
    fn acte_temps(&mut self, ui: &mut egui::Ui, c: &Comparaison) {
        acte(ui, 4, "Le temps qu'il faut pour que tout le monde sache", |ui| {
            propos(
                ui,
                "Le prix en messages n'est pas le prix en temps. À gauche, un aller simple. À \
                 droite, deux tours de journal à ℓ₉₉. C'est ici, et ici seulement, que les deux \
                 barres se croisent.",
            );
            a_faire(
                ui,
                "Montez ℓ₉₉ : la maille passe devant. Montez le délai d'aller simple : le journal \
                 repasse. La figure du bas dit à quel endroit exactement le verdict change de \
                 camp.",
            );
            poignee(
                ui,
                "ℓ₉₉ du chemin de durabilité (ms) — entrée du modèle",
                "",
                |ui| ui.add(egui::Slider::new(&mut self.l99_ms, PLAGE_L99.0..=PLAGE_L99.1)),
            );
            poignee(ui, "délai d'aller simple pair à pair (ms)", "", |ui| {
                ui.add(egui::Slider::new(
                    &mut self.aller_simple_ms,
                    PLAGE_ALLER_SIMPLE.0..=PLAGE_ALLER_SIMPLE.1,
                ))
            });
            let maille_ms = Granularite::Micro.ms_depuis_tics(c.maille_temps);
            let journal_ms = Granularite::Micro.ms_depuis_tics(c.journal_temps);
            simule(ui, "maille — un aller simple", format!("{maille_ms:.3}"), "ms");
            simule(
                ui,
                "journal — deux tours de journal à ℓ₉₉",
                format!("{journal_ms:.3}"),
                "ms",
            );
            paire(ui, maille_ms, journal_ms);
            constat(ui, &c.verdict_temps(Granularite::Micro));

            ui.add_space(6.0);
            self.croisement(ui);

            ui.add_space(6.0);
            let (journal, maille) = Comparaison::diametres();
            du_traite(ui, "diamètre du journal", "2".to_string(), journal);
            // F1 — le traité ne donne pas de diamètre à la maille, et l'absence
            // s'affiche au même rang plutôt que de se combler.
            note(ui, &format!("diamètre de la maille : {maille}"));
        });
    }

    /// Le croisement, **dessiné** plutôt que nommé.
    ///
    /// Aucun temps n'est calculé ici : chaque point est un appel à
    /// `sim_agents::scenario_a`, et le croisement est l'abscisse où **son**
    /// `verdict_temps` change de camp. La vue lit, elle ne tranche pas.
    fn croisement(&self, ui: &mut egui::Ui) {
        let g = Granularite::Micro;
        let (c_maille, c_journal) = teintes(ui);
        let pas = (PLAGE_ALLER_SIMPLE.1 - PLAGE_ALLER_SIMPLE.0) / POINTS_BALAYAGE as f64;

        let mut maille = Vec::with_capacity(POINTS_BALAYAGE + 1);
        let mut journal = Vec::with_capacity(POINTS_BALAYAGE + 1);
        let mut bascule = None;
        let mut precedent: Option<bool> = None;
        for i in 0..=POINTS_BALAYAGE {
            let aller = PLAGE_ALLER_SIMPLE.0 + pas * i as f64;
            let c = scenario_a(
                self.n,
                self.p,
                self.l99_ms,
                aller,
                self.degre_depot,
                self.taux_omission,
                GRAINE,
            );
            maille.push([aller, g.ms_depuis_tics(c.maille_temps)]);
            journal.push([aller, g.ms_depuis_tics(c.journal_temps)]);
            let gagne = c.verdict_temps(g).contains(VAINQUEUR_MAILLE);
            if bascule.is_none() && matches!(precedent, Some(p) if p != gagne) {
                bascule = Some(aller);
            }
            precedent = Some(gagne);
        }

        Plot::new("croisement_temps")
            .height(180.0)
            .legend(Legend::default())
            .x_axis_label("délai d'aller simple pair à pair (ms)")
            .y_axis_label("temps (ms)")
            // Figure de lecture, pas bac à sable : sans cela, la molette est
            // mangée par le tracé — il zoome au lieu que la page défile, et les
            // bornes automatiques partent avec. Le curseur au-dessus est le seul
            // moyen de déplacer cette figure, ce qui est le propos de l'écran.
            .allow_scroll(false)
            .allow_zoom(false)
            .allow_drag(false)
            .allow_boxed_zoom(false)
            .show(ui, |p| {
                p.line(
                    Line::new(PlotPoints::from(maille))
                        .name("maille — un aller simple")
                        .color(c_maille)
                        .width(2.0_f32),
                );
                p.line(
                    Line::new(PlotPoints::from(journal))
                        .name("journal — deux tours à ℓ₉₉")
                        .color(c_journal)
                        .width(2.0_f32),
                );
                p.vline(VLine::new(self.aller_simple_ms).name("délai réglé ci-dessus"));
                if let Some(x) = bascule {
                    p.vline(VLine::new(x).name("croisement"));
                }
            });

        match bascule {
            Some(x) => constat(
                ui,
                &format!(
                    "croisement : à ℓ₉₉ = {:.0} ms, le verdict change de camp vers un aller simple \
                     de {x:.1} ms — sous cette valeur la maille gagne en temps, au-dessus le \
                     journal. Montez ℓ₉₉ et le croisement se déplace vers la droite. Balayage à \
                     {pas:.1} ms près.",
                    self.l99_ms
                ),
            ),
            // F1 — l'absence de croisement se dit, elle ne se devine pas à une
            // courbe qui n'en coupe aucune autre.
            None => constat(
                ui,
                &format!(
                    "aucun croisement sur la plage du délai d'aller simple : à ℓ₉₉ = {:.0} ms, le \
                     même régime gagne en temps partout. Baissez ℓ₉₉ pour ramener le croisement \
                     dans la plage.",
                    self.l99_ms
                ),
            ),
        }
    }

    /// Les trois réglages du scénario qui ne déplacent aucun compte affiché.
    ///
    /// Ils restent réglables et dans leur plage — le PRD les déclare — mais
    /// hors du chemin de démonstration, chacun avec le motif de son silence.
    fn reglages_muets(&mut self, ui: &mut egui::Ui) {
        cadre(ui, |ui| {
            ui.label(
                egui::RichText::new("Réglages déclarés qui ne déplacent aucun compte affiché")
                    .strong()
                    .size(TITRE_SECTION),
            );
            propos(
                ui,
                "Ils sont ici pour que personne ne les cherche parmi ceux qui agissent, et pour \
                 que leur silence soit lu plutôt que découvert.",
            );

            poignee(ui, "p — partitions", "", |ui| {
                ui.add(egui::Slider::new(&mut self.p, 1..=64))
            });
            motif(
                ui,
                "n'entre dans aucun des quatre comptes ci-dessus : les (k − 1) réplications par \
                 partition du tableau 3 ne sont pas comptées en phase 1.",
            );

            poignee(ui, "taux d'omission", "", |ui| {
                ui.add(egui::Slider::new(&mut self.taux_omission, 0.0..=0.20))
            });
            motif(
                ui,
                "tire de vraies pertes dans la maille, et le compte des messages perdus n'est pas \
                 porté jusqu'ici : aucun compte mesuré ne bouge quand vous le tirez. Le seul \
                 mouvement qu'il produit est le libellé du modèle de panne, en tête d'écran, qui \
                 recopie le réglage.",
            );

            motif(
                ui,
                "la graine, montrée dans le bandeau, est figée à 1 : le tirage ne sert qu'aux \
                 pertes et aux latences du détecteur, dont aucune sortie n'est affichée ici. Deux \
                 graines donnent le même écran ; un curseur le démentirait.",
            );
        });
    }
}

// ---------------------------------------------------------------------------
// Le vocabulaire visuel, déclaré une fois et tenu partout
// ---------------------------------------------------------------------------

/// Les deux teintes, maille puis journal.
///
/// Elles se lisent dans les deux thèmes : `egui` suit la préférence du système,
/// et un couple choisi pour le sombre passe sous le seuil de contraste en
/// clair. Bleu et orangé plutôt que rouge et vert (deuxième forme de lisibilité).
fn teintes(ui: &egui::Ui) -> (egui::Color32, egui::Color32) {
    if ui.visuals().dark_mode {
        (
            egui::Color32::from_rgb(120, 175, 255),
            egui::Color32::from_rgb(240, 160, 70),
        )
    } else {
        (
            egui::Color32::from_rgb(30, 90, 190),
            egui::Color32::from_rgb(175, 90, 10),
        )
    }
}

/// La légende de couleur, donnée avant le premier acte : la teinte désigne le
/// régime partout, et rien d'autre.
fn legende(ui: &mut egui::Ui) {
    let (maille, journal) = teintes(ui);
    encart(ui, |ui| {
        ui.horizontal_wrapped(|ui| {
            ui.label(
                egui::RichText::new("■ maille pair à pair")
                    .color(maille)
                    .strong(),
            );
            ui.add_space(10.0);
            ui.label(egui::RichText::new("■ journal").color(journal).strong());
        });
        note(
            ui,
            "Dans chaque acte, la barre la plus longue est le régime le plus cher sur ce \
             compte-là, et une barre absente vaut zéro, pas « peu ». Les deux barres d'un acte se \
             comparent entre elles et à rien d'autre : elles ne s'additionnent pas, et aucun total \
             n'existe (§1.1).",
        );
    });
}

/// Les six sommets d'un hexagone régulier, en fraction du rayon.
///
/// Écrits plutôt que calculés : `f64::cos` et `f64::sin` sont interdits par
/// NF-02, et s'accorder une exception « parce que ce n'est qu'un dessin »
/// rouvrirait la discussion à chaque figure suivante. Six valeurs exactes
/// coûtent moins cher qu'une exception.
const HEXAGONE: [(f32, f32); 6] = [
    (1.0, 0.0),
    (0.5, 0.866_025_4),
    (-0.5, 0.866_025_4),
    (-1.0, 0.0),
    (-0.5, -0.866_025_4),
    (0.5, -0.866_025_4),
];

/// La thèse de l'écran, **dessinée** : le point de passage obligé ne disparaît
/// pas, il change de place.
///
/// C'est la seule chose de cet écran qui se comprend sans lire une phrase, et
/// elle manquait : les quatre actes comparent des longueurs de barre, ce qui
/// dit *combien* mais jamais *pourquoi*. À gauche, quinze liens que quelqu'un
/// doit entretenir ; à droite, six liens vers un point unique. Le lecteur voit
/// le n² et le n avant qu'on les lui nomme.
///
/// Aucune donnée n'entre ici — ni n, ni ℓ₉₉, ni un compte de `Comparaison`. Une
/// figure de cet écran qui varierait sous les curseurs sans être une mesure
/// serait exactement le mensonge d'affordance que PD6 interdit ailleurs ; le
/// dessin est donc figé, et sa légende le dit.
fn schema_des_deux_regimes(ui: &mut egui::Ui) {
    let (c_maille, c_journal) = teintes(ui);
    let petite = egui::TextStyle::Small.resolve(ui.style());
    let corps = egui::TextStyle::Body.resolve(ui.style());

    schema(
        ui,
        190.0,
        "Schéma figé à six agents : ce n'est pas le n réglé plus bas, et aucune grandeur mesurée \
         n'y entre. Les deux comptes annoncés sont ceux du dessin lui-même, vérifiables à l'œil. \
         Il ne montre ni le temps, ni les pannes, ni ce que coûte une écriture — seulement qui \
         doit connaître qui.",
        move |p, r, v| {
            let encre = v.text_color();
            let demi = r.width() / 2.0;
            let rayon = (demi * 0.30).min(r.height() * 0.26);
            let gauche = egui::pos2(r.left() + demi * 0.5, r.center().y + 10.0);
            let droite = egui::pos2(r.right() - demi * 0.5, r.center().y + 10.0);
            let sommets = |centre: egui::Pos2| -> Vec<egui::Pos2> {
                HEXAGONE
                    .iter()
                    .map(|(x, y)| egui::pos2(centre.x + x * rayon, centre.y + y * rayon))
                    .collect()
            };
            let a = sommets(gauche);
            let b = sommets(droite);

            p.text(
                egui::pos2(gauche.x, r.top()),
                egui::Align2::CENTER_TOP,
                "maille — chacun nomme chacun",
                corps.clone(),
                c_maille,
            );
            p.text(
                egui::pos2(droite.x, r.top()),
                egui::Align2::CENTER_TOP,
                "journal — personne ne nomme personne",
                corps,
                c_journal,
            );

            // À gauche, toutes les paires : c'est l'entretien de vue de l'acte 2,
            // et c'est pour cela que le dessin en vaut la peine.
            let trait_maille = egui::Stroke::new(1.0_f32, c_maille);
            for (i, depart) in a.iter().enumerate() {
                for arrivee in a.iter().skip(i + 1) {
                    p.line_segment([*depart, *arrivee], trait_maille);
                }
            }

            // À droite, une arête par agent vers le milieu — et rien entre agents.
            let trait_journal = egui::Stroke::new(1.0_f32, c_journal);
            for pt in &b {
                p.line_segment([*pt, droite], trait_journal);
            }
            let boite =
                egui::Rect::from_center_size(droite, egui::vec2(rayon * 1.05, rayon * 0.55));
            p.rect_filled(boite, 3.0, c_journal);
            p.text(
                boite.center(),
                egui::Align2::CENTER_CENTER,
                "milieu",
                petite.clone(),
                v.extreme_bg_color,
            );

            // Les agents par-dessus les liens : un nœud à demi recouvert par un
            // trait se lit comme un trait qui s'arrête.
            for pt in a.iter().chain(b.iter()) {
                p.circle_filled(*pt, 5.0, encre);
            }

            p.text(
                egui::pos2(gauche.x, r.bottom()),
                egui::Align2::CENTER_BOTTOM,
                "à six agents : 15 liens à entretenir",
                petite.clone(),
                encre,
            );
            p.text(
                egui::pos2(droite.x, r.bottom()),
                egui::Align2::CENTER_BOTTOM,
                "à six agents : 6 liens, tous vers le même point",
                petite,
                encre,
            );
        },
    );
}

/// EX-V07 — permanent, sans repli, épinglé au-dessus de la zone défilante.
///
/// **Cinq champs, et rien d'autre.** Les quatre phrases qui expliquaient
/// comment cet écran s'exécute étaient ici, en gris pâle sous les champs : quatre
/// lignes de commentaire pesant deux fois plus que l'état qu'elles commentent,
/// épinglées au sommet des deux écrans, avant le premier mot du sujet. Elles sont
/// passées dans la zone défilante ([`comment_cet_ecran_sexecute`]), où elles
/// restent visibles à l'ouverture et cessent d'occuper la seule bande que
/// personne ne peut faire défiler. EX-V07 nomme cinq grandeurs ; il ne demande
/// pas que leur mode d'emploi soit épinglé avec elles.
fn bandeau(ui: &mut egui::Ui, c: &Comparaison, taux_omission: f64, duree_ms: f64) {
    cadre(ui, |ui| {
        ui.horizontal_wrapped(|ui| {
            ui.label("synchronisme : asynchrone, Δ finie mais inconnue");
            ui.separator();
            ui.label(format!(
                "temps logique : {} µs (maille) · {} µs (journal)",
                c.maille_temps.0, c.journal_temps.0
            ));
            ui.separator();
            ui.label(format!("temps mural : {}", temps_mural(duree_ms)));
            ui.separator();
            ui.label(format!(
                "modèle de panne : omission de message, p = {taux_omission:.3}"
            ));
        });
        de_la_vue(
            ui,
            "graine",
            format!("{GRAINE}"),
            "figée ici — EX-V07 demande qu'elle soit montrée, pas qu'elle soit réglable",
        );
    });
}

/// Ce que le bandeau d'EX-V07 ne dit pas de lui-même.
///
/// Trois pièges de lecture, chacun sur une exécution qui n'a pas de bouton
/// « lancer » : le temps mural ne compte pas le balayage, le temps logique n'est
/// pas une horloge, et le modèle de panne est lu du réglage. Rien ici n'est
/// repliable, et le bloc s'ouvre en tête de la zone défilante : il est lu au
/// premier coup d'œil sans occuper la bande épinglée.
fn comment_cet_ecran_sexecute(ui: &mut egui::Ui) {
    encart(ui, |ui| {
        ui.label(
            egui::RichText::new("Comment cet écran s'exécute")
                .small()
                .strong()
                .weak(),
        );
        ui.add_space(3.0);
        note(
            ui,
            &format!(
                "Ce scénario n'a pas de bouton « lancer » : il se recalcule à chaque image, et le \
                 temps mural du bandeau est celui de ce seul recalcul — le balayage de l'acte 4, \
                 qui rappelle `scenario_a` {} fois de plus sur la plage du délai d'aller simple, \
                 n'y est pas compté. Le temps logique n'est pas une horloge qui avance : les \
                 comptes du tableau 3 sont des formules fermées, et les deux valeurs sont les deux \
                 horizons comparés à l'acte 4. Le modèle de panne est lu du réglage — à la \
                 différence du scénario B, `scenario_a` n'en déclare aucun.",
                POINTS_BALAYAGE + 1
            ),
        );
    });
}

/// Le temps mural, ou le fait qu'il passe sous la résolution de l'horloge.
///
/// `performance.now()` est volontairement grossi dans les navigateurs ; afficher
/// « 0,0 µs » laisserait croire à une mesure absente plutôt qu'à une mesure trop
/// fine pour l'instrument.
fn temps_mural(duree_ms: f64) -> String {
    let us = duree_ms * 1_000.0;
    if us < 1.0 {
        "sous la résolution de l'horloge (< 1 µs)".to_string()
    } else {
        format!("{us:.0} µs")
    }
}

/// Un acte : son numéro, son titre, et son contenu — énoncé, curseur, comptes,
/// barres, constat, dans cet ordre.
fn acte(ui: &mut egui::Ui, numero: u32, nom: &str, contenu: impl FnOnce(&mut egui::Ui)) {
    cadre(ui, |ui| {
        titre(ui, &numero.to_string(), nom);
        contenu(ui);
    });
}

/// Le curseur de n, posé sous chacun des deux énoncés qu'il sert.
fn curseur_n(ui: &mut egui::Ui, n: &mut u32) {
    poignee(ui, "n — agents", "", |ui| {
        ui.add(egui::Slider::new(n, 4..=2_000))
    });
}

/// Les deux barres d'un acte, à la même échelle. Jamais empilées : la longueur
/// compare, elle n'ajoute pas.
fn paire(ui: &mut egui::Ui, maille: f64, journal: f64) {
    let (c_maille, c_journal) = teintes(ui);
    let haut = maille.max(journal);
    ui.add_space(2.0);
    barre(ui, maille, haut, c_maille);
    barre(ui, journal, haut, c_journal);
}

/// Une barre — et **rien du tout** quand la valeur est nulle.
///
/// Un `ProgressBar` à zéro peint quand même ses coins arrondis : à l'acte 2, le
/// compte que le scénario existe pour montrer *absent* se lisait comme une
/// petite quantité présente. Zéro n'est pas « peu ».
fn barre(ui: &mut egui::Ui, valeur: f64, haut: f64, teinte: egui::Color32) {
    if valeur <= 0.0 || haut <= 0.0 {
        ui.add_space(11.0);
        return;
    }
    ui.add(
        egui::ProgressBar::new((valeur / haut) as f32)
            .fill(teinte)
            .desired_height(9.0)
            .rounding(2.0),
    );
}

/// Le constat d'un acte — la phrase que `sim-agents` produit, sous les barres
/// qu'elle décrit, jamais reléguée en pied d'écran.
fn constat(ui: &mut egui::Ui, texte: &str) {
    ui.add_space(4.0);
    ui.add(egui::Label::new(egui::RichText::new(texte).strong()).wrap());
}

/// Le motif du silence d'un réglage.
fn motif(ui: &mut egui::Ui, texte: &str) {
    note(ui, texte);
    ui.add_space(6.0);
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Le vainqueur en temps se lit dans une **phrase formatée** de
    /// `sim-agents`, faute d'accesseur. Ce test est le garde-fou du couplage :
    /// une reformulation de `Comparaison::verdict_temps` le fait échouer, au
    /// lieu de faire annoncer « aucun croisement » partout à la figure de
    /// l'acte 4.
    #[test]
    fn le_vainqueur_se_lit_encore_dans_la_phrase_de_verdict() {
        let g = Granularite::Micro;
        // ℓ₉₉ long, aller simple court : la maille gagne en temps.
        let maille = scenario_a(8, 1, 200.0, 1.0, 3, 0.0, GRAINE);
        assert!(
            maille.verdict_temps(g).contains(VAINQUEUR_MAILLE),
            "{}",
            maille.verdict_temps(g)
        );
        // L'inverse : la phrase ne doit alors **pas** porter le fragment.
        let journal = scenario_a(8, 1, 1.0, 50.0, 3, 0.0, GRAINE);
        assert!(
            !journal.verdict_temps(g).contains(VAINQUEUR_MAILLE),
            "{}",
            journal.verdict_temps(g)
        );
    }
}
