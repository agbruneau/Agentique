//! `stigmergie-lab` — interface, native et web à partir du même code.
//!
//! Ce crate **ne contient aucune logique de simulation, ni aucune définition de
//! scénario** (§5.1). Il affiche ce que `sim-agents` produit, et rien de plus.
//!
//! Règles d'affichage tenues ici :
//!
//! - **PD3** — la console est en Θ(1) par rapport à n. Aucune ligne par agent
//!   dans le tableau de bord ; l'inspection individuelle est un mode enquête
//!   (EX-V01, EX-V02).
//! - **PD8** — aucun scénario ne s'ouvre sans son bloc de trois, non repliable.
//!   Les trois rangs sont **numérotés et séparés** : un lecteur qui n'a pas lu
//!   le traité doit voir qu'il y en a trois, et lequel est la négation.
//! - **EX-V07** — modèle de panne, synchronisme, graine, temps logique et temps
//!   mural sont affichés en permanence, dans les deux écrans, hors de la zone
//!   défilante.
//! - **EX-V08** — la carte de chaleur de φ est ordonnée par partition, avec une
//!   séparation explicite : il n'y a **pas** de gradient entre partitions.
//! - **EX-V11** — chaque grandeur porte son unité ; ce qui vient du traité
//!   porte sa section et sa page, ce qui vient de la simulation porte
//!   l'étiquette « simulé ». Les deux ne se mélangent jamais.
//! - **F3** — le mot « convergé » n'apparaît nulle part.
//!
//! ## L'ordre de lecture est l'argument
//!
//! Trois écrans **numérotés** portent la démonstration : **A** pose le
//! compromis, **B** montre ce qu'un essaim qui ne se parle pas fait de la trace,
//! **Limites** dit ce que les deux premiers ne prouvent pas. L'entrée par défaut
//! est **A**, comme RQ9 l'exige — « l'entrée par défaut reste A → B et rien
//! d'autre » — et comme la mesure de succès d'O1 le suppose : « un visiteur web
//! lance le scénario A et énonce correctement le compromis diamètre/latence sans
//! avoir lu le traité ».
//!
//! Un quatrième onglet, **Repères**, est délibérément **hors de la numérotation**
//! et posé après un séparateur : c'est une table de consultation, pas une étape.
//! Le numéroter en ferait un quatrième temps de l'argument, qu'il n'est pas ; le
//! retirer laisserait φ, γ, τ, α, β et ℓ₉₉ sans définition nulle part, ce qui est
//! le défaut que la mesure de succès d'O1 — « sans avoir lu le traité » — rend
//! disqualifiant.
//!
//! ## Trois provenances, et une quatrième chose qui n'en est pas une
//!
//! EX-V11 se lit à l'œil, pas dans une note : [`simule`], [`du_traite`] et
//! [`de_la_vue`] **colorent la valeur elle-même**, et [`legende_des_chiffres`],
//! posée sous le bloc de trois de chaque écran, montre les formes côte à côte
//! avant que le lecteur ne rencontre le premier chiffre. La couleur n'est jamais
//! seule à porter la distinction : « simulé » d'un côté, la section et la page
//! de l'autre, restent écrits.
//!
//! La **reformulation en langue courante** ([`en_clair`], `Bloc::en_clair`) n'est
//! aucune des trois : ce n'est ni une mesure, ni une citation, ni un réglage,
//! c'est de la prose du produit. Elle porte donc son propre libellé, et jamais
//! une teinte : lui en donner une l'aurait rangée parmi les provenances qu'EX-V11
//! distingue, ce qu'elle n'est pas. Elle ne contient **aucun chiffre**, et c'est
//! la règle qui empêche la confusion de s'installer par la porte de derrière.
//!
//! ## L'échelle typographique
//!
//! Cinq tailles, posées une fois par [`poser_le_style`] dans le `Style` d'egui,
//! et **jamais** retapées au point d'appel. Ce qui reste en dur dans ce fichier
//! est ce que le style d'egui ne sait pas nommer : [`THESE`], [`TITRE_SECTION`]
//! et [`MESURE`], trois constantes documentées. La version d'avant réglait la
//! taille à quarante endroits, avec huit valeurs distinctes entre 10 et 16 points
//! — ce n'est pas une échelle, c'est l'absence d'échelle, et un lecteur qui
//! cherche la hiérarchie d'un écran ne la trouve pas.
//!
//! ## Les deux cibles
//!
//! Le natif passe par [`lancer_natif`], le web par `lancer_web`, exporté vers
//! JavaScript par `wasm-bindgen` et appelé au chargement du module. Les deux
//! construisent la **même** [`Application`] et posent le **même** style : c'est
//! la condition d'EX-V12, dont la parité de sortie est mesurée par le banc
//! `bancs/parite-wasm`.

#![deny(missing_docs)]
#![deny(rustdoc::broken_intra_doc_links)]

mod scenario_a;
mod scenario_b;

use eframe::egui;

/// Point d'entrée natif.
#[cfg(not(target_arch = "wasm32"))]
pub fn lancer_natif() -> eframe::Result<()> {
    let options = eframe::NativeOptions {
        viewport: egui::ViewportBuilder::default().with_inner_size([1180.0, 820.0]),
        ..Default::default()
    };
    eframe::run_native(
        "stigmergie-lab",
        options,
        Box::new(|cc| {
            poser_le_style(&cc.egui_ctx);
            Ok(Box::new(Application::default()))
        }),
    )
}

/// Point d'entrée web, appelé par le module JavaScript au chargement.
///
/// L'identifiant `toile` est celui du `<canvas>` de `web/index.html` : les deux
/// doivent rester d'accord, et le message d'échec le dit plutôt que de laisser
/// une page blanche.
///
/// DT4 — hébergement en pages statiques : rien ici ne parle à un serveur, et
/// aucun état n'est conservé entre deux chargements.
#[cfg(target_arch = "wasm32")]
#[wasm_bindgen::prelude::wasm_bindgen(start)]
pub fn lancer_web() {
    use wasm_bindgen::JsCast as _;

    let toile = web_sys::window()
        .and_then(|f| f.document())
        .and_then(|d| d.get_element_by_id("toile"))
        .and_then(|e| e.dyn_into::<web_sys::HtmlCanvasElement>().ok())
        .expect("web/index.html doit contenir un <canvas id=\"toile\">");

    wasm_bindgen_futures::spawn_local(async move {
        let issue = eframe::WebRunner::new()
            .start(
                toile,
                eframe::WebOptions::default(),
                Box::new(|cc| {
                    poser_le_style(&cc.egui_ctx);
                    Ok(Box::new(Application::default()))
                }),
            )
            .await;

        // Écrit dans la page, pas seulement dans la console.
        //
        // Ce futur est **détaché** : `init()` se résout dès la fin du démarrage
        // synchrone, donc une panique ici ne rejette aucune promesse et le
        // `.catch()` d'`index.html` ne se déclenche jamais. Le bloc d'état a
        // déjà été retiré par le `.then()`, et le motif habituel — WebGL 2
        // absent ou désactivé, `eframe` n'ayant pas de repli logiciel — laissait
        // donc exactement la page noire muette que les deux commentaires
        // disent vouloir éviter.
        if let Err(e) = issue {
            let message = format!(
                "L'interface n'a pas démarré : {e:?}. Le motif habituel est WebGL 2 absent \
                 ou désactivé — eframe n'a pas de repli logiciel."
            );
            if let Some(document) = web_sys::window().and_then(|f| f.document()) {
                if let Some(corps) = document.body() {
                    let bloc = document
                        .create_element("pre")
                        .expect("création d'un <pre> dans un document valide");
                    bloc.set_text_content(Some(&message));
                    let _ = corps.append_child(&bloc);
                }
            }
            web_sys::console::error_1(&message.into());
        }
    });
}

// ---------------------------------------------------------------------------
// L'échelle typographique et l'espacement, posés une fois
// ---------------------------------------------------------------------------

/// Installe l'échelle typographique et l'espacement de l'interface.
///
/// Appelée sur les **deux** cibles, au même endroit du démarrage : un style posé
/// d'un seul côté ferait deux interfaces à partir d'un seul code, ce qu'EX-V12
/// interdit.
///
/// Les tailles par défaut d'egui visent une console d'outil — corps à 12,5 et
/// petite à 9 points. Cet écran est un écran de **lecture** : des paragraphes de
/// trois lignes dans une colonne de 820 px, que les valeurs d'origine rendent
/// serrés et fatigants. Les cinq valeurs ci-dessous ont un rapport constant
/// d'environ 1,25 de l'une à la suivante ; c'est ce rapport, et non les valeurs
/// prises isolément, qui fait qu'un lecteur voit la hiérarchie sans la chercher.
pub fn poser_le_style(ctx: &egui::Context) {
    use egui::FontFamily::{Monospace, Proportional};
    use egui::{FontId, TextStyle};

    let mut style = (*ctx.style()).clone();
    style.text_styles = [
        (TextStyle::Heading, FontId::new(20.0, Proportional)),
        (TextStyle::Body, FontId::new(14.5, Proportional)),
        (TextStyle::Button, FontId::new(14.0, Proportional)),
        (TextStyle::Monospace, FontId::new(13.5, Monospace)),
        (TextStyle::Small, FontId::new(11.5, Proportional)),
    ]
    .into();

    // Interligne et respiration. Le défaut d'egui — 4 points entre deux widgets
    // empilés — convient à une rangée de boutons et colle deux paragraphes l'un
    // à l'autre.
    style.spacing.item_spacing = egui::vec2(8.0, 6.0);
    style.spacing.button_padding = egui::vec2(8.0, 4.0);
    ctx.set_style(style);
}

#[derive(PartialEq, Eq, Clone, Copy)]
enum Onglet {
    A,
    B,
    Limites,
    Reperes,
}

/// L'application, identique en natif et en web.
pub struct Application {
    onglet: Onglet,
    /// Hauteur du bandeau d'onglets au tracé précédent, en points logiques.
    /// Voir le commentaire de `update` : sans elle, la ligne d'ordre de lecture
    /// disparaît quand la fenêtre rétrécit.
    hauteur_bandeau: f32,
    /// Filtre de l'onglet « Repères ». Vit ici et non dans une fonction : un
    /// champ de recherche qui s'oublie au changement d'onglet est un champ qu'on
    /// remplit deux fois.
    recherche: String,
    b: scenario_b::VueB,
    a: scenario_a::VueA,
}

impl Default for Application {
    fn default() -> Self {
        Application {
            // RQ9 : « l'entrée par défaut reste A → B et rien d'autre », et la
            // mesure de succès d'O1 est « deux minutes, scénario A, sans avoir
            // lu le traité ».
            onglet: Onglet::A,
            hauteur_bandeau: 0.0,
            recherche: String::new(),
            b: scenario_b::VueB::default(),
            a: scenario_a::VueA::default(),
        }
    }
}

impl eframe::App for Application {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        let bandeau = egui::TopBottomPanel::top("onglets").show(ctx, |ui| {
            ui.add_space(4.0);
            // `horizontal_wrapped` et non `horizontal` : sous 600 px, la rangée
            // débordait hors du panneau et le troisième onglet devenait
            // inatteignable.
            ui.horizontal_wrapped(|ui| {
                ui.heading("stigmergie-lab");
                ui.separator();
                ui.selectable_value(&mut self.onglet, Onglet::A, "1 · A — Les deux régimes");
                ui.selectable_value(
                    &mut self.onglet,
                    Onglet::B,
                    "2 · B — Fourragement stigmergique",
                );
                ui.selectable_value(&mut self.onglet, Onglet::Limites, "3 · Limites");
                // Le séparateur porte du sens : ce qui suit n'est pas le
                // quatrième temps de l'argument, et il n'est donc pas numéroté.
                ui.separator();
                ui.selectable_value(&mut self.onglet, Onglet::Reperes, "Repères");
                ui.separator();
                // egui suit `prefers-color-scheme` par défaut, et le lecteur
                // n'avait aucun moyen de voir l'autre thème sans changer son
                // système. Un seul appel d'egui : le bouton bascule la
                // préférence globale, et les deux teintes d'EX-V11 sont
                // choisies pour rester lisibles des deux côtés.
                egui::widgets::global_theme_preference_switch(ui);
            });
            ui.label(
                egui::RichText::new(
                    "Les trois onglets numérotés se lisent dans l'ordre : le deuxième suppose le \
                     premier, et le troisième dit ce que ni l'un ni l'autre ne prouve. « Repères » \
                     n'est pas une étape — c'est le vocabulaire, consultable à tout moment.",
                )
                .weak()
                .small(),
            );
            ui.add_space(4.0);
        });

        // `TopBottomPanel` découpe son contenu à la hauteur qu'il avait au
        // tracé **précédent** (`set_clip_rect` sur le rectangle rechargé). Sous
        // 600 px la rangée d'onglets passe à deux lignes, le bandeau grandit,
        // et la ligne d'ordre de lecture tombait hors du découpage : mesuré à
        // 500 px, une bande vide à sa place jusqu'à la première interaction.
        // Un tracé de plus suffit, et il n'est demandé que le jour où la
        // hauteur change — l'interface reste au repos le reste du temps.
        let hauteur = bandeau.response.rect.height();
        if (hauteur - self.hauteur_bandeau).abs() > 0.5 {
            self.hauteur_bandeau = hauteur;
            ctx.request_repaint();
        }

        egui::CentralPanel::default().show(ctx, |ui| match self.onglet {
            Onglet::B => self.b.afficher(ui),
            Onglet::A => self.a.afficher(ui),
            Onglet::Limites => limites(ui),
            Onglet::Reperes => reperes(ui, &mut self.recherche),
        });
    }
}

// ---------------------------------------------------------------------------
// Les briques de mise en page, communes aux quatre onglets
// ---------------------------------------------------------------------------

/// Largeur maximale de la colonne de lecture, en pixels logiques.
///
/// Jamais en caractères : egui ne mesure pas la ligne avant de la poser. Une
/// phrase qui traverse un écran de 1400 px se relit mal, et l'onglet
/// « Limites » en aligne des dizaines ; la borne est de typographie, pas de
/// goût. Une seule valeur pour les quatre onglets : deux colonnes de largeurs
/// différentes d'un onglet à l'autre se lisent comme un défaut d'alignement.
const LARGEUR_COLONNE: f32 = 820.0;

/// Taille de la thèse citée et de sa négation, en points logiques.
///
/// PD8 exige que les deux portent le **même** rang typographique, et un rang se
/// lit, il ne se déclare pas : la constante est unique pour que la règle ne
/// puisse pas se défaire par une retouche d'un seul côté. Au-dessus du corps,
/// sous le titre d'écran — ce sont les deux phrases que le lecteur emporte.
pub const THESE: f32 = 17.0;

/// Taille du titre d'une section numérotée, en points logiques.
///
/// Entre le corps et [`THESE`] : une section est un repère de navigation, pas un
/// énoncé, et un titre au rang de la thèse ferait croire à six thèses par écran.
pub const TITRE_SECTION: f32 = 16.0;

/// Taille du chiffre auquel un écran répond, en points logiques.
///
/// Hors de l'échelle, à dessein : ce n'est pas du texte, c'est le résultat. Un
/// écran n'en porte **qu'un**, et cette taille est ce qui le dit sans l'écrire.
pub const MESURE: f32 = 30.0;

/// La colonne de lecture : centrée, et jamais plus large que
/// [`LARGEUR_COLONNE`].
pub(crate) fn colonne_de_lecture(ui: &mut egui::Ui, contenu: impl FnOnce(&mut egui::Ui)) {
    let large = ui.available_width().min(LARGEUR_COLONNE);
    let marge = ((ui.available_width() - large) / 2.0).max(0.0);
    ui.horizontal_top(|ui| {
        ui.add_space(marge);
        ui.vertical(|ui| {
            ui.set_max_width(large);
            contenu(ui);
        });
    });
}

/// Un cadre de **section** — le rang de cadre le plus fort, pleine largeur.
///
/// Trait visible, fond du panneau : c'est ce qui découpe un écran en sections
/// numérotées. Les deux autres rangs sont [`encart`], qui accompagne sans
/// découper, et le cadre du bloc de trois, que [`bloc_pd8`] pose lui-même.
pub(crate) fn cadre(ui: &mut egui::Ui, contenu: impl FnOnce(&mut egui::Ui)) {
    egui::Frame::group(ui.style())
        .inner_margin(egui::Margin::symmetric(10.0, 8.0))
        .show(ui, |ui| {
            ui.set_width(ui.available_width());
            contenu(ui);
        });
}

/// Un cadre d'**appui** — fond léger, aucun trait.
///
/// Pour ce qui aide à lire sans faire partie de la démonstration : la
/// reformulation en langue courante, la clé de lecture des chiffres, la légende
/// des couleurs, une entrée de glossaire. Un lecteur qui saute tous les encarts
/// perd le confort et garde l'argument entier ; c'est le critère qui décide
/// entre les deux rangs, et non la longueur du contenu.
///
/// Aucun trait, à dessein : deux rangs de cadre qui portent tous deux un trait
/// se distinguent mal, et l'interface d'avant les confondait — tout y était
/// `Frame::group`, donc rien n'y était mis en avant.
pub(crate) fn encart(ui: &mut egui::Ui, contenu: impl FnOnce(&mut egui::Ui)) {
    egui::Frame::group(ui.style())
        .fill(ui.visuals().faint_bg_color)
        .stroke(egui::Stroke::NONE)
        .inner_margin(egui::Margin::symmetric(10.0, 8.0))
        .show(ui, |ui| {
            ui.set_width(ui.available_width());
            contenu(ui);
        });
}

/// Le titre numéroté d'une section — l'ordre de lecture est la démonstration.
pub(crate) fn titre(ui: &mut egui::Ui, numero: &str, texte: &str) {
    ui.horizontal_wrapped(|ui| {
        ui.label(egui::RichText::new(numero).monospace().weak());
        ui.label(
            egui::RichText::new(texte)
                .strong()
                .size(TITRE_SECTION),
        );
    });
    ui.add_space(3.0);
}

/// Ce que la section montre, posé **avant** les poignées.
pub(crate) fn propos(ui: &mut egui::Ui, texte: &str) {
    ui.label(texte);
    ui.add_space(6.0);
}

/// Le geste que la section demande, et ce qu'il faut regarder pendant.
///
/// C'est la seule ligne d'un écran qui s'adresse au lecteur à l'impératif, et
/// elle était jusqu'ici noyée en fin de paragraphe — « Tirez n : les deux comptes
/// suivent la population » se lisait comme une observation, pas comme une
/// consigne. La séparer est ce qui fait passer l'écran d'une page à lire à une
/// manipulation à faire, ce qui est tout le propos d'un simulateur.
///
/// **Sans teinte**, comme [`de_la_vue`] et pour la même raison : les deux
/// couleurs de l'écran désignent les deux provenances externes d'EX-V11, et une
/// troisième les affaiblirait toutes. Le mot « À faire » porte la distinction.
pub(crate) fn a_faire(ui: &mut egui::Ui, texte: &str) {
    ui.horizontal_top(|ui| {
        ui.spacing_mut().item_spacing.x = 6.0;
        ui.label(egui::RichText::new("À faire").small().strong());
        ui.add(egui::Label::new(egui::RichText::new(texte).strong()).wrap());
    });
    ui.add_space(8.0);
}

/// Une précision de second rang.
pub(crate) fn note(ui: &mut egui::Ui, texte: &str) {
    ui.add(egui::Label::new(egui::RichText::new(texte).weak().small()).wrap());
}

/// Une poignée : son nom en clair, le curseur pleine largeur dessous, et ce que
/// le curseur fait sous le curseur.
///
/// L'ordre compte : on ne doit jamais avoir à chercher ailleurs ce que fait une
/// poignée. `effet` vide n'écrit rien — c'est le cas quand la phrase de tête de
/// la section a déjà dit ce que la poignée déplace.
pub(crate) fn poignee(
    ui: &mut egui::Ui,
    nom: &str,
    effet: &str,
    widget: impl FnOnce(&mut egui::Ui) -> egui::Response,
) {
    ui.label(egui::RichText::new(nom).strong());
    ui.scope(|ui| {
        // Le curseur prend la largeur disponible moins la boîte de valeur :
        // à 500 px comme à 1400, la course reste manipulable. Posé dans un
        // `scope` : régler `slider_width` sur le `ui` courant fuirait sur tout
        // ce qui suit dans la même section.
        ui.spacing_mut().slider_width = (ui.available_width() - 110.0).clamp(90.0, 480.0);
        let _ = widget(ui);
    });
    if !effet.is_empty() {
        note(ui, effet);
    }
    ui.add_space(8.0);
}

/// Le cadre d'un schéma, avec la mention qui empêche de le lire comme une mesure.
///
/// Un dessin dans une interface de simulation est ambigu par nature : rien ne
/// distingue à l'œil une figure tracée sur des données d'une figure tracée sur
/// rien. `legende` est donc obligatoire, et chaque appel y écrit ce que le schéma
/// **ne** montre **pas** — c'est PD6 appliqué au dessin.
pub(crate) fn schema(
    ui: &mut egui::Ui,
    hauteur: f32,
    legende: &str,
    dessin: impl FnOnce(&egui::Painter, egui::Rect, &egui::Visuals),
) {
    encart(ui, |ui| {
        let large = ui.available_width();
        let (reponse, peintre) =
            ui.allocate_painter(egui::vec2(large, hauteur), egui::Sense::hover());
        dessin(&peintre, reponse.rect, ui.visuals());
        ui.add_space(4.0);
        note(ui, legende);
    });
}

// ---------------------------------------------------------------------------
// La grammaire des chiffres (EX-V11)
// ---------------------------------------------------------------------------

/// La teinte des grandeurs **mesurées ici** (EX-V11), lisible sur les deux
/// thèmes. Elle double l'étiquette « simulé », elle ne la remplace pas : un
/// lecteur qui ne distingue pas les teintes lit encore le mot.
fn teinte_simule(ui: &egui::Ui) -> egui::Color32 {
    if ui.visuals().dark_mode {
        egui::Color32::from_rgb(120, 190, 255)
    } else {
        egui::Color32::from_rgb(18, 88, 168)
    }
}

/// La teinte des grandeurs **citées du traité** (EX-V11). Même règle : elle
/// double la référence de section et de page, elle ne la remplace pas.
fn teinte_traite(ui: &egui::Ui) -> egui::Color32 {
    if ui.visuals().dark_mode {
        egui::Color32::from_rgb(216, 176, 100)
    } else {
        egui::Color32::from_rgb(140, 92, 8)
    }
}

/// La reformulation en langue courante, posée **avant** le bloc de trois.
///
/// Elle sert le persona P1 — « n'a pas lu le traité, arrive par un lien » — et la
/// mesure de succès d'O1, qui suppose qu'un visiteur énonce le compromis « sans
/// avoir lu le traité ». Or la première phrase que cet écran lui montrait était
/// une citation du traité, dans le vocabulaire du traité : « Elle ne détruit pas
/// le point partagé, elle le déplace dans le milieu. » Rien dans cette phrase
/// n'est faux, et rien n'y est intelligible à froid.
///
/// Elle est **au-dessus** du bloc, jamais dedans : PD8 en compte trois rangs, et
/// un quatrième rang, même utile, casserait la lecture que ce bloc existe pour
/// imposer. Le libellé dit qu'il s'agit d'une reformulation du produit, pour que
/// nul ne la cite comme une phrase de l'ouvrage.
pub fn en_clair(ui: &mut egui::Ui, texte: &str) {
    encart(ui, |ui| {
        ui.label(
            egui::RichText::new("En clair — reformulation de l'interface, pas une citation")
                .small()
                .strong()
                .weak(),
        );
        ui.add_space(3.0);
        ui.add(egui::Label::new(texte).wrap());
    });
}

/// Le bloc de trois de PD8 : thèse citée, mécanisme visible, et ce que le
/// scénario ne démontre pas — au même rang typographique que la thèse.
///
/// Les trois rangs sont numérotés et séparés par un filet : c'est la seule
/// façon qu'un lecteur voie qu'il y en a **trois**, et que le troisième est une
/// négation et non une note de bas de page. Rien n'est repliable.
///
/// Ce bloc ne fait que cela. La reformulation en langue courante est
/// [`en_clair`], appelée juste avant ; la clé de lecture d'EX-V11 est
/// [`legende_des_chiffres`], appelée juste après. Les trois sont distinctes parce
/// qu'elles s'adressent à trois choses : la thèse, le lecteur, les chiffres.
pub fn bloc_pd8(ui: &mut egui::Ui, bloc: &sim_agents::Bloc) {
    egui::Frame::group(ui.style())
        .inner_margin(egui::Margin::symmetric(10.0, 8.0))
        .show(ui, |ui| {
            ui.set_width(ui.available_width());

            rang(ui, "1", "La thèse, citée du traité");
            ui.add(
                egui::Label::new(
                    egui::RichText::new(bloc.these)
                        .italics()
                        .size(THESE)
                        .strong(),
                )
                .wrap(),
            );
            ui.label(
                egui::RichText::new(bloc.source)
                    .color(teinte_traite(ui))
                    .small(),
            );

            ui.add_space(6.0);
            ui.separator();
            rang(
                ui,
                "2",
                "Le mécanisme visible — quel réglage produit quel effet, et par quel chemin",
            );
            ui.add(egui::Label::new(bloc.mecanisme_visible).wrap());

            ui.add_space(6.0);
            ui.separator();
            rang(ui, "3", "Ce que ce scénario ne démontre pas");
            // Même taille et même graisse que la thèse : PD8 demande le même
            // rang typographique, et un rang se lit, il ne se déclare pas.
            ui.add(
                egui::Label::new(egui::RichText::new(bloc.ne_demontre_pas).size(THESE).strong())
                    .wrap(),
            );
        });
}

/// L'en-tête numéroté d'un des trois rangs de PD8.
fn rang(ui: &mut egui::Ui, numero: &str, titre: &str) {
    ui.horizontal_wrapped(|ui| {
        ui.spacing_mut().item_spacing.x = 6.0;
        // Sans couleur : les trois teintes de l'écran sont réservées à la
        // grammaire d'EX-V11, et un numéro de rang teinté prêterait à croire
        // qu'il dit d'où vient une grandeur.
        ui.label(egui::RichText::new(numero).monospace().small().strong());
        ui.label(egui::RichText::new(titre).small().strong().weak());
    });
    ui.add_space(2.0);
}

/// La clé de lecture d'EX-V11, **montrée** plutôt que décrite.
///
/// Les trois lignes d'exemple passent par [`simule`], [`du_traite`] et
/// [`de_la_vue`] : ce que le lecteur apprend ici est exactement ce qu'il verra
/// plus bas, au pixel près, et la démonstration ne peut pas se désynchroniser du
/// rendu réel. La valeur d'exemple est le mot « valeur » et non un nombre : un
/// nombre inventé dans une interface qui exige la provenance de chaque grandeur
/// serait la faute que cette légende sert à empêcher (F2).
pub fn legende_des_chiffres(ui: &mut egui::Ui) {
    encart(ui, |ui| {
        ui.label(
            egui::RichText::new("Comment lire les chiffres de cet écran")
                .small()
                .strong()
                .weak(),
        );
        ui.add_space(2.0);
        simule(
            ui,
            "une grandeur produite par l'exécution en cours",
            "valeur".into(),
            "unité",
        );
        du_traite(
            ui,
            "une grandeur citée du traité",
            "valeur".into(),
            "§ et page",
        );
        de_la_vue(
            ui,
            "une entrée de cet écran, ni mesurée ni citée",
            "valeur".into(),
            "d'où elle vient",
        );
        ui.add_space(2.0);
        note(
            ui,
            "Aucun champ ne porte les trois à la fois : une mesure, une citation et un réglage ne \
             se comparent qu'à distance de lecture (EX-V11).",
        );
    });
}

/// Une grandeur issue de la **simulation** (EX-V11, F2).
///
/// La valeur est en chasse fixe — les chiffres s'alignent d'une ligne à
/// l'autre — et teintée. `unite` est l'**unité**, et rien d'autre : une
/// qualification (« deux tours de journal à ℓ₉₉ ») appartient au libellé, où
/// elle ne prend pas la place qu'EX-V11 réserve à la dimension. Un compte sans
/// dimension porte « comptage », pour que le blanc ne se lise pas comme un
/// oubli. L'étiquette « simulé » vient après l'unité, jamais avant.
pub fn simule(ui: &mut egui::Ui, nom: &str, valeur: String, unite: &str) {
    ui.horizontal_wrapped(|ui| {
        ui.spacing_mut().item_spacing.x = 5.0;
        ui.label(format!("{nom} :"));
        ui.label(
            egui::RichText::new(valeur)
                .monospace()
                .strong()
                .color(teinte_simule(ui)),
        );
        if !unite.is_empty() {
            ui.label(egui::RichText::new(unite).weak());
        }
        ui.label(
            egui::RichText::new("simulé")
                .small()
                .color(teinte_simule(ui)),
        );
    });
}

/// Une grandeur issue du **traité** (EX-V11, F2). Jamais dans le même champ
/// qu'une grandeur simulée.
///
/// Même chasse fixe que [`simule`] pour que les deux se comparent à l'œil, et
/// l'autre teinte. `source` est la référence de section et de page : elle est
/// obligatoire, et c'est elle qui distingue la ligne même sans la couleur.
pub fn du_traite(ui: &mut egui::Ui, nom: &str, valeur: String, source: &str) {
    ui.horizontal_wrapped(|ui| {
        ui.spacing_mut().item_spacing.x = 5.0;
        ui.label(format!("{nom} :"));
        ui.label(
            egui::RichText::new(valeur)
                .monospace()
                .strong()
                .color(teinte_traite(ui)),
        );
        ui.label(
            egui::RichText::new(source)
                .small()
                .color(teinte_traite(ui)),
        );
    });
}

/// Une grandeur qui n'est **ni** du traité **ni** de la simulation : une entrée
/// de l'écran (EX-V11).
///
/// La graine des deux scénarios est le cas type. Elle n'a pas de page à citer et
/// n'est le résultat d'aucune mesure ; lui prêter la grammaire de l'une ou
/// l'autre serait le mélange qu'EX-V11 refuse. Sans teinte, à dessein : les deux
/// couleurs de l'écran désignent les deux provenances externes, et une troisième
/// couleur les affaiblirait toutes. `note` dit d'où vient la valeur — le réglage
/// qui la pose, ou la raison pour laquelle elle est figée.
pub fn de_la_vue(ui: &mut egui::Ui, nom: &str, valeur: String, note: &str) {
    ui.horizontal_wrapped(|ui| {
        ui.spacing_mut().item_spacing.x = 5.0;
        ui.label(format!("{nom} :"));
        ui.label(egui::RichText::new(valeur).monospace().strong());
        ui.label(egui::RichText::new("réglage de la vue").weak().small());
        if !note.is_empty() {
            ui.label(egui::RichText::new(note).weak().small());
        }
    });
}

// ---------------------------------------------------------------------------
// L'onglet « Repères » — le vocabulaire
// ---------------------------------------------------------------------------

/// Le glossaire de `sim-agents`, filtrable.
///
/// Cet onglet n'existait pas, et c'est le manque que l'objectif O1 rendait le
/// plus coûteux : les deux écrans emploient φ, γ, τ, α, β, η, ℓ₉₉, M2, partition
/// et une dizaine d'autres termes que rien, nulle part, ne définissait. Chacun
/// est explicable en deux phrases ; aucune n'était écrite.
///
/// La vue ne tient **aucun** texte : tout vient de [`sim_agents::glossaire`], au
/// même titre que les scénarios (§5.1). Le filtre porte sur le terme **et** sur
/// la définition — on cherche un mot qu'on a lu, mais aussi une notion dont on ne
/// connaît pas le nom, ce qui est le cas exact d'un lecteur qui découvre.
fn reperes(ui: &mut egui::Ui, recherche: &mut String) {
    egui::ScrollArea::vertical()
        .auto_shrink([false; 2])
        .show(ui, |ui| {
            colonne_de_lecture(ui, |ui| {
                ui.heading("Repères — le vocabulaire de ces écrans");
                ui.label(
                    "Les définitions ci-dessous sont en langue courante et volontairement \
                     courtes : elles servent à lire les deux scénarios, pas à remplacer le \
                     traité. Chacune porte d'où elle vient — une section de l'ouvrage, une \
                     nomenclature propre à ce produit, ou un réglage de cette interface. La \
                     confusion entre ces trois-là est précisément ce qu'EX-V11 refuse ailleurs \
                     dans l'interface ; un glossaire est l'endroit où elle s'installerait le plus \
                     facilement.",
                );
                ui.add_space(10.0);

                ui.horizontal_wrapped(|ui| {
                    ui.label("Filtrer");
                    ui.add(
                        egui::TextEdit::singleline(recherche)
                            .hint_text("un terme, ou un mot de sa définition")
                            .desired_width(260.0),
                    );
                    if !recherche.is_empty() && ui.button("effacer").clicked() {
                        recherche.clear();
                    }
                });
                ui.add_space(8.0);

                let filtre = recherche.to_lowercase();
                let retenus: Vec<&sim_agents::Terme> = sim_agents::glossaire()
                    .iter()
                    .filter(|t| {
                        filtre.is_empty()
                            || t.terme.to_lowercase().contains(&filtre)
                            || t.definition.to_lowercase().contains(&filtre)
                    })
                    .collect();

                // Le compte est affiché même quand il vaut zéro : un filtre qui
                // ne rend rien et une liste vide se ressemblent trop.
                note(
                    ui,
                    &format!(
                        "{} entrées sur {}",
                        retenus.len(),
                        sim_agents::glossaire().len()
                    ),
                );
                ui.add_space(6.0);

                let mut groupe_courant = "";
                for t in retenus {
                    if t.groupe != groupe_courant {
                        groupe_courant = t.groupe;
                        ui.add_space(6.0);
                        ui.label(
                            egui::RichText::new(t.groupe)
                                .strong()
                                .size(TITRE_SECTION),
                        );
                        ui.add_space(4.0);
                    }
                    encart(ui, |ui| {
                        ui.horizontal_wrapped(|ui| {
                            ui.label(egui::RichText::new(t.terme).strong());
                            // La provenance est teintée comme une citation quand
                            // c'en est une, et neutre sinon : la teinte du traité
                            // sur « réglage de cette interface » dirait le
                            // contraire de ce que la ligne écrit.
                            if t.provenance.starts_with('§') {
                                ui.label(
                                    egui::RichText::new(t.provenance)
                                        .small()
                                        .color(teinte_traite(ui)),
                                );
                            } else {
                                ui.label(egui::RichText::new(t.provenance).small().weak());
                            }
                        });
                        ui.add(egui::Label::new(t.definition).wrap());
                    });
                    ui.add_space(4.0);
                }

                ui.add_space(12.0);
                note(
                    ui,
                    "Cette table s'arrête aux termes que ces écrans affichent. Le traité et le PRD \
                     en tiennent une plus longue ; ce qui manque ici manque parce que l'interface \
                     ne le montre pas, jamais parce qu'il serait secondaire.",
                );
                ui.add_space(12.0);
            });
        });
}

// ---------------------------------------------------------------------------
// L'onglet « Limites »
// ---------------------------------------------------------------------------

/// §8.3 — ce que le produit ne mesure pas, affiché en permanence.
///
/// En une seule liste, les énoncés formaient un mur que personne ne lit jusqu'au
/// bout, ce qui revient à ne pas les afficher — le mensonge que PD6 cherche
/// justement à empêcher. Ils sont donc rangés en sections nommées, chacune avec
/// son compte et une phrase qui dit **comment** la lire, et la colonne est
/// bornée en largeur. Rien n'est repliable et rien n'est retiré : la structure
/// est la seule chose qui change.
fn limites(ui: &mut egui::Ui) {
    egui::ScrollArea::vertical()
        .auto_shrink([false; 2])
        .show(ui, |ui| {
            colonne_de_lecture(ui, |ui| {
                ui.heading("Ce que ce simulateur ne mesure pas");
                ui.label(
                    "Une méthode de validation se définit autant par ce qu'elle ne réfute pas \
                     (§8.3). Cet onglet n'est pas une annexe : il porte le même rang que les deux \
                     écrans de mesure, parce qu'un mécanisme absent du modèle a, dans tout \
                     résultat, une probabilité de faute nulle — et c'est un mensonge silencieux \
                     (PD6).",
                );
                ui.add_space(12.0);

                section(
                    ui,
                    "Hors de portée de la mesure",
                    "Ces grandeurs ne sont ici ni justes ni fausses : elles ne sont pas produites.",
                    &[
                        "La performance réelle. Le temps simulé n'est pas le temps mesuré. Aucun \
                         chiffre d'ici ne prédit la latence d'un système déployé.",
                        "Les deux ℓ₉₉ ne portent jamais le même libellé. Le ℓ₉₉ du milieu est une \
                         entrée du modèle ; le ℓ₉₉ de réponse d'un agent est une sortie (EX-C15). \
                         Cette interface n'affiche que le premier : elle ne fait tourner que les \
                         scénarios A et B, qui n'ont pas de file par agent.",
                        "Ce qui est hors du monde clos : aucune bibliothèque tierce, aucune \
                         dépendance, aucun système d'exploitation n'est testé.",
                        "La vivacité. Aucune trace finie ne la réfute. Ce qui est produit est au \
                         mieux une vivacité conditionnelle.",
                        "Tout n. Vérifier à n = 5 ne dit formellement rien de n = 5 000.",
                        "Les événements de probabilité inférieure au seuil d'échantillonnage : ils \
                         ne sont pas déclarés absents, ils ne sont pas vus.",
                        "Les fautes corrélées. La corrélation s'injecte, elle ne se mesure pas — \
                         faute d'un estimateur qui ne demande pas déjà la vue globale qu'on \
                         cherchait à éviter.",
                        "L'uniformité du tirage de pairs. Le service d'échantillonnage est aussi \
                         uniforme qu'on le lui demande, alors que les implantations réelles ne le \
                         sont que localement (§4.1).",
                    ],
                );

                section(
                    ui,
                    "Ce que le produit ne contient pas — côté agents",
                    "Un module écrit mais qu'aucun scénario n'appelle compte ici comme absent : il \
                     a le même effet qu'un module inexistant sur un résultat affiché.",
                    sim_agents::hors_perimetre(),
                );
                section(
                    ui,
                    "… côté milieu",
                    "Même règle, appliquée au journal partitionné et à son plan de contrôle.",
                    sim_milieu::hors_perimetre(),
                );
                section(
                    ui,
                    "… côté modèle de faute",
                    "Ce qu'aucune exécution de cette interface ne tire, quelle que soit la graine.",
                    sim_core::faute::ModeleFaute::hors_modele(),
                );

                section(
                    ui,
                    "Ce que cette interface n'affiche pas",
                    "Producteur implanté et testé dans les couches basses, aucun point d'appel \
                     ici. L'interface s'arrête aux deux scénarios, à cet onglet et au vocabulaire.",
                    &[
                        // Sans astérisques d'emphase : egui n'a pas d'analyseur
                        // Markdown et les rendrait littéralement.
                        "EX-V07 — les pertes de messages et les propriétés du détecteur du \
                         scénario A : « Comparaison » ne les porte pas, donc aucun compte affiché \
                         n'y dépend de la graine, et celle-ci y reste fixée à 1 — montrée, jamais \
                         réglable. Le bandeau, lui, est tenu dans les deux écrans, épinglé hors de \
                         la zone défilante et rempli dès l'ouverture",
                        "EX-V02 — le mode « enquête », inspection d'un agent individuel",
                        "EX-V03, EX-V04, EX-V19 — directive, époque et sujet des accusés",
                        "EX-V05 — la dérivée du retard de consommation",
                        "EX-V06 — la distribution du chemin de durabilité",
                        "EX-V09 — le partage par fragment d'URL (encodé et décodé par \
                         `sim-agents::partage`, jamais lu ici)",
                        "EX-V13 à EX-V18 — détecteur, taux de base, ISR, cascade, plan de \
                         contrôle, grille du tableau 14",
                        "EX-V20, EX-V21 — leviers de gouvernance et leur fenêtre de violation",
                        "le parcours « le fil » (O6) et l'export : ni l'un ni l'autre n'existe",
                        "les huit autres blocs de trois. Dix scénarios sont écrits dans \
                         « sim-agents » avec leur thèse, leur mécanisme et leur reformulation en \
                         langue courante ; deux seulement ont un écran",
                    ],
                );

                ui.add_space(4.0);
                ui.label(
                    egui::RichText::new(sim_core::couverture::Agregat::mention_obligatoire())
                        .italics()
                        .weak(),
                );
                ui.add_space(12.0);
            });
        });
}

/// Une section de l'onglet « Limites ».
///
/// Le compte est affiché : une liste sans compte laisse croire qu'on l'a
/// parcourue. Le chapeau dit comment lire la section — sans lui, deux listes
/// voisines paraissent dire la même chose, alors que l'une nomme ce qui n'est
/// pas mesuré et l'autre ce qui n'existe pas.
fn section(ui: &mut egui::Ui, titre: &str, chapeau: &str, lignes: &[&str]) {
    cadre(ui, |ui| {
        ui.horizontal_wrapped(|ui| {
            ui.label(egui::RichText::new(titre).size(TITRE_SECTION).strong());
            ui.label(
                egui::RichText::new(format!("— {} énoncés", lignes.len()))
                    .weak()
                    .small(),
            );
        });
        // Le chapeau n'est pas atténué : il dit comment lire la liste, et une
        // consigne de lecture en gris pâle ne se lit pas. L'italique suffit à
        // le distinguer des énoncés.
        ui.add(egui::Label::new(egui::RichText::new(chapeau).italics()).wrap());
        ui.add_space(6.0);
        for ligne in lignes {
            puce(ui, ligne);
        }
    });
    ui.add_space(10.0);
}

/// Une puce à retrait pendant : la suite d'une ligne longue s'aligne sous le
/// texte, jamais sous la puce.
///
/// `Label::wrap` est explicite parce qu'en disposition horizontale egui étend
/// par défaut au lieu de replier — sans lui, chaque énoncé sortait de l'écran
/// par la droite.
fn puce(ui: &mut egui::Ui, texte: &str) {
    ui.horizontal_top(|ui| {
        ui.spacing_mut().item_spacing.x = 6.0;
        ui.label(egui::RichText::new("—").weak());
        ui.add(egui::Label::new(texte).wrap());
    });
    ui.add_space(6.0);
}
