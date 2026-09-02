//! `sim-agents` — les mécanismes du traité, tels qu'écrits.
//!
//! Chaque mécanisme implante l'algorithme du traité avec sa signature complète :
//! modèle de panne, hypothèse de synchronisme, hypothèses sur le milieu,
//! condition d'arrêt, modes de défaillance. Aucun d'eux ne dessine quoi que ce
//! soit (§5.1 du PRD).
//!
//! **Périmètre à la clôture de la phase 6** : les trente et un modules couvrent
//! les mécanismes des chapitres 1 à 8, les treize scénarios comme données, et le
//! vocabulaire que l'interface affiche ([`glossaire()`] — une donnée, pas un
//! mécanisme, posée ici parce que ce qui vient du traité ne se recopie pas dans
//! la couche qui dessine). Ce
//! qui reste hors du modèle est énuméré par [`hors_perimetre`], et cette liste
//! est tenue à jour à chaque fin de phase — une liste périmée fait mentir
//! l'interface dans le sens inverse de celui que PD6 protège.

#![deny(missing_docs)]
#![deny(rustdoc::broken_intra_doc_links)]

pub mod accord;
pub mod adhesion;
pub mod agregat_fenetre;
pub mod agregation;
pub mod alignement;
pub mod allocation;
pub mod arbitrage;
pub mod cascade;
pub mod causalite;
pub mod conformite;
pub mod consensus_lineaire;
pub mod cycle_de_vie;
pub mod deliberation;
pub mod dettes;
pub mod directive;
pub mod echantillonnage;
pub mod elasticite;
pub mod essaim;
pub mod glossaire;
pub mod gouvernance;
pub mod pair_a_pair;
pub mod partage;
pub mod propagation;
pub mod reconfiguration;
pub mod scenario;
pub mod scenario_d;
pub mod scenario_m;
pub mod soupcon;
pub mod stigmergie;
pub mod taux_de_base;
pub mod usl;

pub use essaim::{Membre, Perception};
pub use glossaire::{glossaire, Terme};
pub use scenario::{scenario_a, scenario_b, Bloc, Comparaison, ResultatB, BLOC_A, BLOC_B};
pub use conformite::Conformite;
pub use dettes::{Dette, EtatDeBorne, DETTES};
pub use scenario_d::{Choix, ScenarioD, BLOC_D};
pub use scenario_m::{scenario_m, ResultatM, BLOC_M};
pub use stigmergie::{Bornes, Evt, Fourragement, Mesures, MomentTrace, Params};

/// Ce que le modèle **ne** produit **pas**, à la clôture de la phase 6, à
/// afficher au même rang que ce qu'il produit (PD6, PD9).
///
/// Aucune interface, aucun document ne doit suggérer que la couverture du
/// traité est complète : le produit s'arrête sur un budget, jamais sur une
/// complétude.
///
/// **Cette liste est un livrable, pas un commentaire.** Un mécanisme absent a,
/// dans tout résultat, une probabilité de faute nulle, et c'est un mensonge
/// silencieux ; mais une liste qui déclare absent un mécanisme livré est le
/// mensonge symétrique, et le banc de vérification du dépôt a montré qu'il est le plus facile
/// des deux à laisser s'installer. Toute entrée retirée d'ici doit l'être parce
/// que le mécanisme est **branché**, jamais parce qu'il est écrit quelque part.
///
/// **Sans balisage Markdown dans les entrées** : `sim-viz` les affiche telles
/// quelles par un `egui::RichText`, qui n'a pas d'analyseur — astérisques et
/// accents graves s'y liraient littéralement, un retour à la ligne couperait la
/// puce. Un nom de module ou d'item se marque donc par des guillemets, et
/// `sim-viz` tient la règle par un test sur les trois listes d'absences.
pub fn hors_perimetre() -> &'static [&'static str] {
    &[
        "tableau 15 — les six mécanismes d'allocation rendent les valeurs citées du \
         traité, pas une mesure : aucune tâche n'est allouée, la graine est ignorée \
         (scénario F)",
        "nombre de partitions du scénario A — « scenario_a » reçoit « p » et le jette : aucun \
         des comptes du tableau 3 n'en dépend. Le curseur « p — partitions » de l'écran, \
         gradué de 1 à 64, ne déplace donc aucun chiffre affiché, et rien à côté de lui ne \
         le dit",
        "prix de l'anarchie — « rapport_mesure » est renseigné par l'appelant ; aucun \
         équilibre ni optimum n'est calculé (EX-A54, scénario K)",
        "corroboration r parmi n — les formules de Bayes sont là, la fenêtre W, les \
         empreintes et le compte d'émetteurs distincts ne le sont pas (EX-A31, scénario L)",
        "file d'attente et arriéré par agent — la cascade calcule un ℓ₉₉ agrégé par \
         formule fermée ; ses générations viennent d'un décalage de phase posé à la \
         main, pas de la saturation (EX-C15, scénario J)",
        "mode (c) « retard » de l'algorithme 3.1 du ch. 3 — déclaré comme préréglage, \
         sans effet sur l'itération (EX-A43)",
        "mode asynchrone pur et son refus des configurations terminantes (scénario I, \
         critère 7) ; point de croisement en n (critère 11)",
        "modèle de temps synchrone du scénario H — ni horloge de Poisson, ni couplage, \
         ni commutateur (DT11)",
        "tableaux 7, 11 et 12 et figure 4.2 du traité — seuls le tableau 14 et la \
         figure 5.1 sont remplis",
        "oracles du §5.1 du traité au registre — les trois mécanismes d'accord portent des \
         prédicats ad hoc, hors du registre de « sim-core » et de ses garanties PD2 \
         (EX-A51)",
        "blocs de trois des scénarios C, H et I (PD8) ; et huit des dix blocs livrés — \
         D, E, F, G, J, K, L, M — n'ont aucun point d'affichage : « sim-viz » ne lit que \
         « BLOC_A » et « BLOC_B », un réexport n'étant pas un affichage",
        "débit émergent du scénario C — « usl::Charge::mesurer » applique la formule \
         d'échelle universelle et y ajoute un bruit ; il n'y a ni milieu, ni latence, ni \
         boucle à événements sous cette « mesure ». La régression inverse donc la formule \
         qui a produit les points",
        "trois des sept colonnes du tableau 14 — « tours_jusqua_larret », « messages_par_tour » \
         et « condition_darret » sont des citations formatées, pas des mesures (EX-V18)",
        "sept mécanismes des phases 1 à 5 n'ont aucun appelant hors de leurs propres tests — \
         adhésion (EX-A03), alignement (EX-A02), causalité (EX-A08), consensus linéaire \
         (EX-A13, EX-A43), directive avec époque (EX-A07), reconfiguration (EX-A44, \
         EX-A45) et cycle de vie (EX-A26, EX-A48, EX-A27 — sondes, ordre de chute et budget \
         de perturbation, dont la seule référence hors du module est le « mod tests » de \
         « gouvernance ») : écrits et testés, exécutés par aucun scénario",
        "six des quinze oracles du catalogue ne sont armés par aucune exécution — \
         « CONSERVATION », « ACCORD_LOCAL », « D1 », « D2 », « UN_SEUL_PROPRIETAIRE » et \
         « TOUTE_PARTITION_A_UN_PROPRIETAIRE ». Deux ne sont armés nulle part, pas même par \
         un test : « PushPull::armer_oracle » et « Alignement::armer_oracles » n'ont aucun \
         appelant, si bien que « CONSERVATION » et « ACCORD_LOCAL » ne sont jamais inscrits \
         à un registre. Les quatre autres n'ont d'appelant que dans les tests de leur \
         propre module. Neuf tournent : « PLANCHER » et « HORS_DOMINANTE » par le scénario B, \
         M1 à M4 et M10 par le journal, R1 et R2 par le scénario D",
        "contre-exemple des prédicats locaux (PD10, EX-A39) — « ACCORD_LOCAL » porte son \
         contre-exemple et le réglage qui le met en défaut, et « Registre::criteres_locaux » \
         les rend ; aucun registre ne le porte à l'exécution — voir l'entrée sur les \
         oracles — et aucun affichage ne les lit",
        "agrégat de couverture entre exécutions (EX-C08) — « Agregat::absorber » et « faibles » \
         n'ont aucun appelant, et le binaire « campagne », seul chemin multi-exécutions du \
         produit, n'agrège aucune couverture : les conditions à compte nul ne sont donc \
         signalées nulle part",
        "graphe de communication (EX-C16) — le générateur, les courtiers, le retrait corrélé \
         d'arêtes et le constat de connexité conjointe n'ont d'appelant que dans des tests ; \
         seul le type « Graphe » sert en production",
        "mécanismes du chapitre 8 sans appelant — dépôt aveugle (EX-A57) et file d'arbitrage \
         (EX-A59) sont implantés et testés unitairement, et aucun scénario ne les exécute. \
         La file n'a même pas d'émetteur, faute de régime du §8.3 du traité dans le monde \
         clos (T3) : le panneau d'EX-V23 n'a donc rien à afficher et n'est pas câblé",
        "tableau 21 à l'écran (EX-A58) — « dettes::verdicts » est calculé par le scénario M et \
         par personne d'autre ; « sim-viz » ne lit pas le module, donc l'hypothèse \
         d'indépendance de chaque énoncé n'est pas affichée à côté de sa valeur",
    ]
}
