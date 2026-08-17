//! Partage d'une exécution par URL (EX-V09) et parité de sortie (EX-V12).
//!
//! > Toute exécution est partageable par une URL encodant graine +
//! > configuration ; le destinataire voit exactement la même chose. (EX-V09)
//!
//! L'encodage est **textuel et sans dépendance** : les champs sont des nombres
//! et des identifiants courts, et un format `clé:valeur` séparé par des points
//! virgules suffit. Tirer un encodeur base64 ou un sérialiseur d'URL pour cela
//! serait précisément la dérive que RQ3 surveille.
//!
//! Ce qui rend le partage honnête n'est pas l'encodage mais la **version** : un
//! lien produit par une autre version du binaire est refusé, pas réinterprété
//! (NF-03).

use crate::stigmergie::{MomentTrace, Params};

/// Une exécution partageable.
#[derive(Clone, Debug, PartialEq)]
pub struct Lien {
    /// Version du binaire qui a produit le lien. Un lien d'une autre version
    /// est **refusé**, pas réinterprété (NF-03).
    pub version: String,
    /// Scénario encodé.
    pub scenario: String,
    /// Graine de l'exécution.
    pub graine: u64,
    /// Budget d'événements.
    pub budget: u64,
    /// Les paramètres du scénario, au complet.
    pub params: Params,
}

fn f(x: f64) -> String {
    // **Aucun arrondi.** L'affichage par défaut d'un `f64` rend la plus courte
    // écriture décimale qui se relit à l'identique ; `{:.9}` rendait une écriture
    // plus courte encore, mais qui ne se relit pas.
    //
    // La différence n'est pas théorique. Tous les champs ne viennent pas d'un
    // curseur : `Params::verrouillage()` **calcule** son dépôt unitaire, et
    // 8,231290285767679·10⁻⁵ arrivait chez le destinataire en 8,2313·10⁻⁵. Le
    // lien encodait bien le champ, le décodait sans erreur, et faisait exécuter
    // un autre dépôt — la panne qu'EX-V09 doit rendre impossible, et que NF-03
    // ne rattrape pas puisque la version, elle, est la bonne.
    format!("{x}")
}

impl Lien {
    /// Encode le lien. Le résultat est un fragment d'URL, à placer après `#`.
    pub fn encoder(&self) -> String {
        let p = &self.params;
        [
            format!("v={}", self.version),
            format!("s={}", self.scenario),
            format!("g={}", self.graine),
            format!("b={}", self.budget),
            format!("n={}", p.n),
            format!("m={}", p.m),
            format!("p={}", p.p),
            format!("ga={}", f(p.gamma)),
            format!("phmin={}", f(p.phi_min)),
            format!("phmax={}", f(p.phi_max)),
            format!("al={}", f(p.alpha)),
            format!("be={}", f(p.beta)),
            format!("etmin={}", f(p.eta_min)),
            format!("etmax={}", f(p.eta_max)),
            format!("T={}", f(p.periode_cycle_ms)),
            format!("tau={}", f(p.fenetre_tau_ms)),
            format!("l99={}", f(p.l99_milieu_ms)),
            format!("bas={}", f(p.bascule_a)),
            format!(
                "tr={}",
                match p.moment_trace {
                    MomentTrace::Avant => "avant",
                    MomentTrace::Apres => "apres",
                }
            ),
            format!("cr={}", f(p.crash_avant_validation)),
            format!("id={}", p.action_idempotente as u8),
            format!("un={}", p.ressources_sur_une_partition as u8),
            format!("il={}", p.intervalle_lecture),
            format!("ea={}", f(p.echec_action)),
            // Le dépôt unitaire **doit** voyager : `Params::verrouillage()` le
            // pose explicitement pour que γ soit la seule variable qui change,
            // et l'omettre faisait voir au destinataire une exploration plate
            // là où l'émetteur voyait le verrouillage — dépôt divisé par 10⁵,
            // traces différentes, sans le moindre refus. C'est le critère de
            // sortie (4) de la phase 2 qui tombait.
            match p.depot_unitaire {
                Some(q) => format!("q={}", f(q)),
                None => "q=auto".to_string(),
            },
            // Les deux réglages de phase 6 voyagent pour la même raison que le
            // dépôt unitaire : un lien qui les omettrait ferait voir au
            // destinataire une population décorrélée là où l'émetteur voyait la
            // conformité, sans le moindre refus. C'est EX-V09 qui tomberait.
            format!("cf={}", f(p.part_conforme)),
            format!("ip={}", p.identite_partagee as u8),
        ]
        .join(";")
    }

    /// Décode un lien.
    ///
    /// NF-03 — un lien produit par une autre version est **refusé**, pas tenté :
    /// l'entrelacement n'est garanti que sur la même version du binaire, et
    /// afficher une figure différente sous la même URL serait pire que refuser.
    pub fn decoder(fragment: &str, version_courante: &str) -> Result<Lien, String> {
        let mut champs: Vec<(&str, &str)> = Vec::new();
        for morceau in fragment.split(';') {
            match morceau.split_once('=') {
                Some((c, v)) => champs.push((c, v)),
                None if morceau.is_empty() => {}
                None => return Err(format!("champ mal formé : « {morceau} »")),
            }
        }
        let get = |cle: &str| -> Result<&str, String> {
            champs
                .iter()
                .find(|(c, _)| *c == cle)
                .map(|(_, v)| *v)
                .ok_or_else(|| format!("champ « {cle} » absent du lien"))
        };
        let nombre = |cle: &str| -> Result<f64, String> {
            get(cle)?
                .parse::<f64>()
                .map_err(|e| format!("champ « {cle} » illisible : {e}"))
        };
        let entier = |cle: &str| -> Result<u64, String> {
            get(cle)?
                .parse::<u64>()
                .map_err(|e| format!("champ « {cle} » illisible : {e}"))
        };

        let version = get("v")?.to_string();
        if version != version_courante {
            return Err(format!(
                "lien refusé : produit par la version {version}, binaire courant \
                 {version_courante}. NF-03 refuse le rejeu inter-versions au lieu de le tenter — \
                 le destinataire ne verrait pas la même chose, et c'est précisément ce que le \
                 partage promet."
            ));
        }

        let params = Params {
            n: entier("n")? as u32,
            m: entier("m")? as u32,
            p: entier("p")? as u32,
            gamma: nombre("ga")?,
            phi_min: nombre("phmin")?,
            phi_max: nombre("phmax")?,
            alpha: nombre("al")?,
            beta: nombre("be")?,
            eta_min: nombre("etmin")?,
            eta_max: nombre("etmax")?,
            periode_cycle_ms: nombre("T")?,
            fenetre_tau_ms: nombre("tau")?,
            l99_milieu_ms: nombre("l99")?,
            bascule_a: nombre("bas")?,
            moment_trace: match get("tr")? {
                "avant" => MomentTrace::Avant,
                "apres" => MomentTrace::Apres,
                autre => return Err(format!("moment de trace inconnu : « {autre} »")),
            },
            crash_avant_validation: nombre("cr")?,
            action_idempotente: entier("id")? != 0,
            ressources_sur_une_partition: entier("un")? != 0,
            intervalle_lecture: entier("il")? as u32,
            echec_action: nombre("ea")?,
            part_conforme: nombre("cf")?,
            identite_partagee: entier("ip")? != 0,
            depot_unitaire: match get("q")? {
                "auto" => None,
                v => Some(
                    v.parse::<f64>()
                        .map_err(|e| format!("champ « q » illisible : {e}"))?,
                ),
            },
        };

        Ok(Lien {
            version,
            scenario: get("s")?.to_string(),
            graine: entier("g")?,
            budget: entier("b")?,
            params,
        })
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::scenario_b;

    fn lien() -> Lien {
        Lien {
            version: sim_core::VERSION.to_string(),
            scenario: "B".to_string(),
            graine: 42,
            budget: 20_000,
            params: Params {
                n: 16,
                ..Params::scenario_b()
            },
        }
    }

    /// EX-V09 — encoder puis décoder rend exactement les mêmes réglages.
    #[test]
    fn un_lien_se_decode_en_ce_quil_encode() {
        let a = lien();
        let b = Lien::decoder(&a.encoder(), sim_core::VERSION).unwrap();
        assert_eq!(a, b);
    }

    /// EX-V09, critère de sortie de la phase 2 — **un lien partagé reproduit la
    /// figure exactement chez le destinataire**. Ce n'est pas l'égalité des
    /// réglages qui le prouve, c'est celle de la trace d'exécution.
    #[test]
    fn un_lien_partage_reproduit_la_figure_chez_le_destinataire() {
        let emetteur = lien();
        let fragment = emetteur.encoder();

        // Le destinataire ne dispose que du fragment.
        let recu = Lien::decoder(&fragment, sim_core::VERSION).unwrap();

        let chez_lemetteur =
            scenario_b(emetteur.params.clone(), emetteur.graine, emetteur.budget).unwrap();
        let chez_le_destinataire =
            scenario_b(recu.params.clone(), recu.graine, recu.budget).unwrap();

        assert_eq!(
            chez_lemetteur.trace, chez_le_destinataire.trace,
            "les deux exécutions doivent avoir la même trace"
        );
        assert_eq!(chez_lemetteur.mesures.effort, chez_le_destinataire.mesures.effort);
        assert_eq!(
            chez_lemetteur.mesures.effort_par_tranche,
            chez_le_destinataire.mesures.effort_par_tranche,
            "la figure elle-même, tranche par tranche"
        );
    }

    /// Deux réglages différents produisent deux liens différents — sans quoi le
    /// partage confondrait des exécutions distinctes.
    #[test]
    fn deux_reglages_distincts_donnent_deux_liens_distincts() {
        let a = lien();
        let mut b = lien();
        b.params.gamma = 0.91;
        assert_ne!(a.encoder(), b.encoder());

        let mut c = lien();
        c.graine = 43;
        assert_ne!(a.encoder(), c.encoder());
    }

    /// EX-V09 — un préréglage qui **pose** son dépôt unitaire voyage aussi
    /// exactement que celui qui le laisse calculer.
    ///
    /// `Params::verrouillage()` pose `depot_unitaire = Some(φ_max·(−ln γ)/(n·τ/T))`,
    /// une valeur calculée et non un cran de curseur : elle a les cinquante-trois
    /// bits d'un `f64`. L'encodage à neuf décimales en gardait cinq chiffres
    /// significatifs — 8,231290285767679·10⁻⁵ partait en `0.000082313` —, et le
    /// destinataire exécutait un autre dépôt sans qu'aucun refus ne le signale.
    /// C'est la panne exacte que le commentaire du champ `q` décrit, revenue par
    /// la précision au lieu de l'omission.
    #[test]
    fn le_depot_unitaire_pose_traverse_le_lien_sans_perte() {
        let emetteur = Lien {
            params: Params {
                n: 16,
                ..Params::verrouillage()
            },
            ..lien()
        };
        let recu = Lien::decoder(&emetteur.encoder(), sim_core::VERSION).unwrap();
        assert_eq!(
            recu.params.depot_unitaire, emetteur.params.depot_unitaire,
            "le dépôt unitaire a changé de valeur en traversant le lien"
        );
        assert_eq!(
            scenario_b(emetteur.params.clone(), emetteur.graine, 20_000)
                .unwrap()
                .trace,
            scenario_b(recu.params.clone(), recu.graine, 20_000)
                .unwrap()
                .trace,
            "le destinataire ne voit pas la même figure"
        );
    }

    /// Aucun champ flottant du lien n'est arrondi : ce que l'émetteur exécute
    /// est ce que le destinataire exécute, bit pour bit.
    #[test]
    fn aucun_champ_flottant_nest_arrondi_par_lencodage() {
        // Une valeur qui ne s'écrit pas en neuf décimales, sur chacun des
        // flottants que le lien transporte.
        let irrationnel = 1.0f64 / 3.0;
        let p = Params {
            gamma: 1.0 - irrationnel / 7.0,
            phi_min: irrationnel / 1_000.0,
            eta_min: irrationnel,
            periode_cycle_ms: 50.0 + irrationnel,
            depot_unitaire: Some(Params::scenario_b().depot()),
            ..Params::scenario_b()
        };
        let a = Lien { params: p, ..lien() };
        let b = Lien::decoder(&a.encoder(), sim_core::VERSION).unwrap();
        assert_eq!(a, b);
    }

    /// NF-03 — un lien d'une autre version est refusé, avec la raison.
    #[test]
    fn un_lien_dune_autre_version_est_refuse() {
        let mut a = lien();
        a.version = "0.0.0".to_string();
        let e = Lien::decoder(&a.encoder(), sim_core::VERSION).unwrap_err();
        assert!(e.contains("NF-03"), "{e}");
        assert!(e.contains("refusé"), "{e}");
    }

    #[test]
    fn un_lien_tronque_est_refuse() {
        let e = Lien::decoder("v=0.1.0;s=B", sim_core::VERSION).unwrap_err();
        assert!(e.contains("absent"), "{e}");
    }
}
