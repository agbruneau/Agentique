//! `campagne` — mode sans interface (EX-V10).
//!
//! Produit un CSV des points de mesure et un rapport JSON, **sans aucune
//! dépendance graphique** : le binaire vit dans `sim-agents` et ne connaît pas
//! `sim-viz`. C'est la correction que le §5.1c du PRD apportait à la version 1.0 du
//! PRD, qui logeait les scénarios dans la crate de rendu tout en exigeant
//! d'elle un mode sans rendu.
//!
//! Ni `clap` ni `csv` ne sont tirés : les arguments se comptent sur une main et
//! les champs du CSV sont numériques, donc sans échappement à traiter. §5.2 du PRD
//! fait de la liste des dépendances un indicateur de risque, et une dépendance
//! qu'on n'ouvre pas est la plus lazy des dépendances (PD7).
//!
//! ```bash
//! campagne --scenario c --graine 1 --sortie rapports/
//! ```

use sim_agents::usl::{ajuster_avec_ic, Charge, LIBELLE};
use sim_core::alea::Alea;
use sim_core::Config;
use std::fmt::Write as _;

struct Args {
    scenario: String,
    graine: u64,
    sortie: String,
    sigma: f64,
    kappa: f64,
    p: u32,
    tailles: usize,
    repetitions: u32,
    n_max: u32,
    reechantillonnages: usize,
}

impl Default for Args {
    fn default() -> Self {
        Args {
            scenario: "c".to_string(),
            graine: 1,
            sortie: ".".to_string(),
            sigma: 0.02,
            kappa: 0.0001,
            p: 4_096,
            tailles: 16,
            repetitions: 30,
            n_max: 512,
            reechantillonnages: 400,
        }
    }
}

fn lire_args() -> Result<Args, String> {
    let mut a = Args::default();
    let mut it = std::env::args().skip(1);
    while let Some(cle) = it.next() {
        let mut valeur = || {
            it.next()
                .ok_or_else(|| format!("l'option {cle} attend une valeur"))
        };
        match cle.as_str() {
            "--scenario" => a.scenario = valeur()?,
            "--graine" => a.graine = valeur()?.parse().map_err(|e| format!("{e}"))?,
            "--sortie" => a.sortie = valeur()?,
            "--sigma" => a.sigma = valeur()?.parse().map_err(|e| format!("{e}"))?,
            "--kappa" => a.kappa = valeur()?.parse().map_err(|e| format!("{e}"))?,
            "--p" => a.p = valeur()?.parse().map_err(|e| format!("{e}"))?,
            "--tailles" => a.tailles = valeur()?.parse().map_err(|e| format!("{e}"))?,
            "--repetitions" => a.repetitions = valeur()?.parse().map_err(|e| format!("{e}"))?,
            "--n-max" => a.n_max = valeur()?.parse().map_err(|e| format!("{e}"))?,
            "--reechantillonnages" => {
                a.reechantillonnages = valeur()?.parse().map_err(|e| format!("{e}"))?
            }
            // L'aide demandée n'est pas une erreur : elle sort sur la sortie
            // standard avec le code 0, sans quoi `cargo run` la rapporte comme
            // un échec de processus et casse tout script qui enchaîne.
            "--aide" | "-h" => {
                println!("{AIDE}");
                std::process::exit(0);
            }
            autre => return Err(format!("option inconnue : {autre}\n\n{AIDE}")),
        }
    }
    Ok(a)
}

const AIDE: &str = "\
campagne — mode sans interface

  --scenario <c>            scénario à exécuter (défaut : c)
  --graine <u64>            graine de la campagne
  --sortie <répertoire>     où écrire points.csv et rapport.json
  --sigma <f64>             σ injecté dans le milieu simulé
  --kappa <f64>             κ injecté dans le milieu simulé
  --p <u32>                 plafond structurel de partitions
  --tailles <n>             nombre de tailles mesurées
  --repetitions <n>         répétitions par taille, graines distinctes
  --n-max <n>               plus grande taille mesurée
  --reechantillonnages <n>  tirages pour les intervalles de confiance";

fn main() {
    let args = match lire_args() {
        Ok(a) => a,
        Err(e) => {
            eprintln!("{e}");
            std::process::exit(2);
        }
    };
    if args.scenario != "c" {
        eprintln!(
            "seul le scénario C est disponible en campagne à ce stade ; les autres arrivent avec \
             leurs phases (PD9 : le produit s'arrête sur un budget, jamais sur une complétude)"
        );
        std::process::exit(2);
    }

    let charge = Charge::nouvelle(args.sigma, args.kappa, args.p);
    let mut alea = Alea::nouveau(args.graine);
    let points = charge.campagne(2, args.n_max, args.tailles, args.repetitions, &mut alea);
    let ajustement = match ajuster_avec_ic(&points, args.reechantillonnages, &mut alea) {
        Some(a) => a,
        None => {
            // RQ2 : si l'identification échoue, le résultat négatif est publié
            // tel quel — c'est un résultat sur le protocole.
            eprintln!(
                "ajustement impossible : le système normal est dégénéré sur cette plage de n. \
                 C'est un résultat sur le protocole de mesure, pas une erreur d'exécution (RQ2)."
            );
            std::process::exit(1);
        }
    };

    let config = Config {
        graine: args.graine,
        granularite: sim_core::temps::Granularite::Micro,
        fautes: sim_core::faute::ModeleFaute::default(),
        evenements_max: 0,
        secondes_coeur_max: None,
        scenario: "C".to_string(),
    };
    let entete = config.entete();

    // --- points.csv ---
    let mut csv = String::new();
    let _ = writeln!(csv, "# {entete}");
    let _ = writeln!(csv, "# {LIBELLE}");
    let _ = writeln!(csv, "n,debit_relatif");
    for p in &points {
        let _ = writeln!(csv, "{},{:.9}", p.n, p.debit_relatif);
    }

    // --- rapport.json ---
    let u = ajustement.estimation.u_etoile();
    let mut json = String::new();
    let _ = writeln!(json, "{{");
    let _ = writeln!(json, "  \"entete\": \"{entete}\",");
    let _ = writeln!(json, "  \"libelle\": \"{LIBELLE}\",");
    let _ = writeln!(json, "  \"injectes\": {{ \"sigma\": {}, \"kappa\": {} }},", args.sigma, args.kappa);
    let _ = writeln!(
        json,
        "  \"estimation\": {{ \"sigma\": {:.9}, \"kappa\": {:.11} }},",
        ajustement.estimation.sigma, ajustement.estimation.kappa
    );
    let _ = writeln!(
        json,
        "  \"ic_sigma\": [{:.9}, {:.9}],",
        ajustement.ic_sigma.bas, ajustement.ic_sigma.haut
    );
    let _ = writeln!(
        json,
        "  \"ic_kappa\": [{:.11}, {:.11}],",
        ajustement.ic_kappa.bas, ajustement.ic_kappa.haut
    );
    match (u, &ajustement.ic_u_etoile) {
        (Some(u), Some(ic)) => {
            let _ = writeln!(json, "  \"u_etoile\": {u:.4},");
            let _ = writeln!(json, "  \"ic_u_etoile\": [{:.4}, {:.4}],", ic.bas, ic.haut);
        }
        _ => {
            // F1 : l'absence s'affiche, elle ne se comble pas.
            let _ = writeln!(json, "  \"u_etoile\": null,");
            let _ = writeln!(
                json,
                "  \"u_etoile_absence\": \"κ nul ou σ ≥ 1 : il n'existe pas de maximum\","
            );
        }
    }
    let _ = writeln!(json, "  \"points\": {},", points.len());
    let _ = writeln!(json, "  \"reechantillonnages\": {},", ajustement.reechantillonnages);
    let residu_max = ajustement
        .residus
        .iter()
        .fold(0.0f64, |a, r| a.max(r.abs()));
    let _ = writeln!(json, "  \"residu_relatif_max\": {residu_max:.6},");
    let dans_ic = ajustement.ic_sigma.contient(args.sigma) && ajustement.ic_kappa.contient(args.kappa);
    let _ = writeln!(json, "  \"validation_croisee_reussie\": {dans_ic}");
    let _ = writeln!(json, "}}");

    let repertoire = std::path::Path::new(&args.sortie);
    if let Err(e) = std::fs::create_dir_all(repertoire) {
        eprintln!("impossible de créer {} : {e}", args.sortie);
        std::process::exit(1);
    }
    for (nom, contenu) in [("points.csv", &csv), ("rapport.json", &json)] {
        if let Err(e) = std::fs::write(repertoire.join(nom), contenu) {
            eprintln!("impossible d'écrire {nom} : {e}");
            std::process::exit(1);
        }
    }

    println!("{entete}");
    println!("{LIBELLE}");
    println!(
        "σ̂ = {:.6} [{:.6}, {:.6}]   κ̂ = {:.8} [{:.8}, {:.8}]",
        ajustement.estimation.sigma,
        ajustement.ic_sigma.bas,
        ajustement.ic_sigma.haut,
        ajustement.estimation.kappa,
        ajustement.ic_kappa.bas,
        ajustement.ic_kappa.haut,
    );
    match u {
        Some(u) => println!("û* = {u:.1} agents"),
        None => println!("û* : aucun maximum — κ nul ou σ ≥ 1 (provenance absente, F1)"),
    }
    println!(
        "validation croisée : {}",
        if dans_ic {
            "les paramètres injectés sont dans l'intervalle de confiance"
        } else {
            "ÉCHEC — les paramètres injectés sont hors de l'intervalle"
        }
    );
    println!("écrit dans {}/points.csv et {}/rapport.json", args.sortie, args.sortie);
    if !dans_ic {
        std::process::exit(1);
    }
}
