//! Les scénarios, comme **données** (§5.1c du PRD).
//!
//! Un scénario est une configuration, des plages de paramètres et un critère
//! d'acceptation — c'est-à-dire un oracle, donc de la logique de simulation et
//! non du rendu. `sim-viz` les affiche ; il ne les définit pas.
//!
//! Chaque scénario porte son **bloc de trois** (PD8), affiché, non repliable, et
//! jamais généré automatiquement : la thèse citée avec sa page, le mécanisme
//! visible, et ce qu'il ne démontre pas. Un scénario dont le troisième champ est
//! vide est un scénario refusé.

use crate::pair_a_pair::Maille;
use crate::stigmergie::{Evt, Fourragement, Params};
use sim_core::moteur::{Budget, Moteur};
use sim_core::temps::{Duree, Granularite};
use sim_core::Config;

/// Le bloc obligatoire de PD8.
#[derive(Clone, Copy, Debug)]
pub struct Bloc {
    /// La thèse **reformulée en langue courante**, sans le vocabulaire du
    /// traité — pour le lecteur qui ne l'a pas lu (persona P1, objectif O1).
    ///
    /// Écrite par le produit, **jamais citée** : elle s'affiche hors des trois
    /// rangs de PD8, qui en compte trois et pas quatre, et l'interface la
    /// désigne comme une reformulation. Une paraphrase présentée au rang d'une
    /// citation serait la confusion de provenance qu'EX-V11 refuse.
    pub en_clair: &'static str,
    /// Une phrase, citée du traité.
    pub these: &'static str,
    /// Section et page **du traité** (F2).
    pub source: &'static str,
    /// Quel réglage produit quel effet observable, et par quel chemin. Jamais
    /// « le système se dégrade ».
    pub mecanisme_visible: &'static str,
    /// La négation explicite, au même rang typographique que la thèse.
    pub ne_demontre_pas: &'static str,
}

// ---------------------------------------------------------------------------
// Scénario A — Les deux régimes
// ---------------------------------------------------------------------------

/// Le bloc de trois du **scénario A** — les deux régimes (PD8).
pub const BLOC_A: Bloc = Bloc {
    en_clair:
        "Deux façons de propager une information dans une population de programmes. Ou bien chacun \
         parle à chacun — c'est la maille. Ou bien chacun écrit dans un cahier commun que les \
         autres relisent — c'est le journal. Le traité soutient que la seconde ne supprime pas le \
         point de passage obligé : elle le déménage du réseau vers ce cahier. Cet écran compare \
         leurs deux factures, en messages et en temps.",
    these: "Elle ne détruit pas le point partagé, elle le déplace dans le milieu.",
    // La thèse citée est au §2.1, p. 25 du traité livré — pas au §1.3, qui
    // fournit les comptes comparés : tableau 3, p. 18, et figure 0, p. 4. Le
    // renvoi précédent, « §1.3, p. 21 », pointait sur une page de la bonne
    // section qui ne contient pas la phrase citée. F2 traite ce cas comme une
    // provenance fausse et non imprécise, d'où l'édition dans le champ.
    source: "§2.1, p. 25 (4ᵉ éd.) — comptes comparés : tableau 3, p. 18, et figure 0, p. 4",
    mecanisme_visible:
        "augmenter n fait croître en n² le compteur d'entretien de vue à gauche, sans toucher au \
         compte de lectures à droite ; augmenter ℓ₉₉ allonge les deux tours de journal à droite, \
         sans toucher à l'aller simple à gauche. Le croisement se déplace sous les deux curseurs.",
    ne_demontre_pas: "rien sur la sûreté. Les deux régimes propagent ; seul le prix diffère.",
};

/// Les trois comptes du scénario A, tenus séparés (§1.1, convention de
/// comptage). Il n'existe aucune méthode qui les additionne.
#[derive(Clone, Copy, Debug)]
pub struct Comparaison {
    /// Taille de la population comparée.
    pub n: u32,
    /// Maille — messages de diffusion utile.
    pub maille_diffusion: u64,
    /// Maille — messages d'**entretien de vue**, comptés à part : c'est le
    /// terme en n² qui fait le croisement.
    pub maille_entretien: u64,
    /// Maille — messages de dépôt.
    pub maille_depot: u64,
    /// Maille — temps écoulé.
    pub maille_temps: Duree,
    /// Journal — écritures.
    pub journal_ecritures: u64,
    /// Journal — lectures.
    pub journal_lectures: u64,
    /// Journal — entretien. Nul : le milieu n'entretient pas de vue.
    pub journal_entretien: u64,
    /// Journal — dépôts.
    pub journal_depot: u64,
    /// Journal — temps écoulé.
    pub journal_temps: Duree,
    /// Journal — tours de journal, l'unité propre au milieu.
    pub journal_tours: u64,
}

impl Comparaison {
    /// Nomme **lequel des trois comptes** est croisé, et dans quel sens. Le PRD
    /// l'exige : un point de croisement sans le compte qu'il croise est un
    /// nombre sans provenance.
    pub fn comptes_croises(&self) -> Vec<String> {
        let mut v = Vec::new();
        v.push(format!(
            "diffusion : maille {} message(s), journal {} écriture(s) + {} lecture(s) — {}",
            self.maille_diffusion,
            self.journal_ecritures,
            self.journal_lectures,
            if self.maille_diffusion <= self.journal_ecritures + self.journal_lectures {
                "la maille tient"
            } else {
                "le journal tient"
            }
        ));
        v.push(format!(
            "entretien de vue : maille {} message(s) par période de sondage, journal {} — sans \
             équivalent à droite, le producteur n'ayant pas de destinataire à connaître (§1.3)",
            self.maille_entretien, self.journal_entretien
        ));
        v.push(format!(
            "cycle de dépôt de toute la population : maille {} message(s), journal {} — Θ(n·d) \
             contre Θ(n) (§1.2)",
            self.maille_depot, self.journal_depot
        ));
        v
    }

    /// Le temps au bout duquel toute la population est informée — la partie que
    /// le traité refuse d'escamoter.
    pub fn verdict_temps(&self, g: Granularite) -> String {
        format!(
            "un aller simple à gauche ({:.3} ms) contre deux tours de journal à droite ({:.3} ms) \
             — {}",
            g.ms_depuis_tics(self.maille_temps),
            g.ms_depuis_tics(self.journal_temps),
            if self.maille_temps <= self.journal_temps {
                "la maille gagne en temps"
            } else {
                "le journal gagne en temps"
            }
        )
    }

    /// Diamètre. Le traité en donne un pour le journal et **aucun** pour la
    /// maille ; l'interface affiche l'absence au lieu de combler (F1).
    pub fn diametres() -> (&'static str, &'static str) {
        (
            "journal : 2 en permanence (§1.3, p. 18, 4ᵉ éd.)",
            Maille::DIAMETRE,
        )
    }
}

/// Exécute la comparaison des deux régimes pour un point (n, ℓ₉₉, …).
///
/// Le calcul est analytique et non simulé, parce que les grandeurs comparées
/// sont des **comptes**, que le traité écrit comme des formules fermées
/// (tableau 3). Ce qui est simulé, c'est le comportement des mécanismes eux-
/// mêmes — la maille tient un vrai détecteur, et le journal un vrai chemin de
/// durabilité.
///
/// **`p` n'a aucun effet, et l'interface le règle quand même.** Le tableau 3 ne
/// fait pas dépendre du nombre de partitions les comptes comparés ici — une
/// écriture, n lectures, deux tours —, donc rien n'en dépend dans le calcul.
/// L'écran du scénario A porte pourtant un curseur « p — partitions » de 1 à 64
/// dont le déplacement ne change aucun chiffre affiché : un réglage qui ne règle
/// rien, déclaré par [`crate::hors_perimetre`] au même rang que le reste (PD6).
pub fn scenario_a(
    n: u32,
    p: u32,
    l99_ms: f64,
    aller_simple_ms: f64,
    degre_depot: u32,
    taux_omission: f64,
    graine: u64,
) -> Comparaison {
    let g = Granularite::Micro;
    let mut alea = sim_core::alea::Alea::nouveau(graine);
    let mut maille = Maille::nouvelle(n, degre_depot, aller_simple_ms, taux_omission, 1_000.0, g);

    let maille_temps = maille.diffuser(&mut alea);
    let vivants = vec![true; n as usize];
    let maille_entretien = maille.entretenir_vue(&vivants, &mut alea);
    let maille_depot = maille.cycle_de_depot();

    // Côté journal, tableau 3 : 1 écriture (+ k − 1 réplications, absentes en
    // phase 1), puis 1 lecture par consommateur, en 2 tours de journal.
    let journal_temps = g.tics_depuis_ms(2.0 * l99_ms);
    let _ = p;

    Comparaison {
        n,
        maille_diffusion: maille.comptes.messages_diffusion,
        maille_entretien,
        maille_depot,
        maille_temps,
        journal_ecritures: 1,
        journal_lectures: n as u64,
        journal_entretien: 0,
        journal_depot: n as u64,
        journal_temps,
        journal_tours: 2,
    }
}

// ---------------------------------------------------------------------------
// Scénario B — Fourragement stigmergique
// ---------------------------------------------------------------------------

/// Le bloc de trois du **scénario B** — le fourragement stigmergique (PD8).
pub const BLOC_B: Bloc = Bloc {
    en_clair:
        "Des agents choisissent où travailler sans jamais se parler : chacun laisse derrière lui \
         une trace, lit celles des autres dans le cahier commun, et les traces s'effacent peu à \
         peu. C'est la stigmergie — la coordination passe par le milieu, pas par les messages. À \
         mi-parcours, l'écran change ce qui est utile : l'essaim doit désapprendre. Le traité \
         soutient qu'il ne trouvera jamais exactement le mieux, mais qu'il en restera à une \
         distance qu'on sait calculer d'avance.",
    these: "Un essaim stigmergique n'atteint pas l'optimum, il campe à distance bornée de lui.",
    source: "§1.2, p. 16 (4ᵉ éd.) — algorithme 1.2, p. 14 ; définition d'essaim, §1.1",
    mecanisme_visible:
        "porter γ à 1 supprime le terme de décroissance dans le calcul de φ ; la trace devient une \
         somme cumulée, le rapport φ_max/φ_min croît sans borne, la probabilité de tirage de la \
         ressource dominante tend vers 1, et la bascule d'utilité à mi-course ne déplace plus \
         l'effort.",
    ne_demontre_pas:
        "la convergence — « cet énoncé est une propriété du tirage, pas un théorème de \
         convergence » (§1.2). Ni l'émergence : le paramètre d'ordre Φ appartient au modèle de \
         Vicsek avec bruit, et aucun mécanisme du périmètre ne le fournit (PD5).",
};

/// Résultat d'une exécution du scénario B.
pub struct ResultatB {
    /// Les grandeurs de population mesurées.
    pub mesures: crate::stigmergie::Mesures,
    /// Hachage de l'entrelacement — l'empreinte de rejeu (NF-01).
    pub trace: u64,
    /// Violations d'oracle constatées, dans l'ordre.
    pub violations: Vec<String>,
    /// Index de la ressource la plus exploitée à la fin.
    pub meilleure_ressource: usize,
    /// Vrai si la bascule d'utilité à mi-course a bien eu lieu.
    pub bascule_faite: bool,
    /// Les bornes théoriques, ou la **raison de leur effacement** quand un
    /// réglage viole leurs hypothèses (NF-14).
    pub bornes: Result<crate::stigmergie::Bornes, String>,
    /// En-tête d'export : version, graine, hachage de configuration (NF-03).
    pub entete: String,
    /// φ moyen sur la population, par ressource (PD3).
    pub phi_moyen: Vec<f64>,
    /// Partition de chaque ressource — la carte de chaleur s'ordonne par
    /// partition, avec une séparation explicite (EX-V08).
    pub partition_des_ressources: Vec<u32>,
    /// Coûts propres du milieu, jamais additionnés aux messages point à point
    /// (EX-M13).
    pub couts_milieu: sim_milieu::Couts,
    /// Temps logique écoulé, en tics (EX-V07).
    pub temps_logique: u64,
    /// Modèle de panne **actif** de cette exécution, tel qu'il est réglé
    /// (EX-V07, EX-C06). Dérivé de la configuration, jamais recopié dans la
    /// vue : deux préréglages ne règlent pas le même modèle, et un libellé
    /// constant l'affirmerait quand même.
    pub modele_de_panne: String,
    /// Réglages dont l'effet dépasse ce qui est réglé.
    pub avertissements: Vec<String>,
    /// **Φ_c mesuré** sur les décisions déposées (EX-A56, EX-V22).
    ///
    /// `Err` quand l'estimation refuse — les ressources réparties sur plusieurs
    /// partitions rendent Φ_c indéfini, M2 ne fournissant aucun ordre entre
    /// elles (DT14).
    ///
    /// **Elle ne décide de l'effacement d'aucune borne** : c'est le réglage qui
    /// le décide, dans [`Params::bornes_applicables`]. Φ_c ne sépare pas la
    /// corrélation due à la fonction de décision de celle due au milieu partagé,
    /// et l'afficher comme cause serait une fausse alarme
    /// (`conformite::CONSTAT_DE_MESURE`).
    pub conformite: Result<crate::conformite::Conformite, String>,
    /// Structure des familles de décision, à afficher **à côté** de Φ_c et jamais
    /// à sa place (EX-C19, EX-V22).
    pub diversite: String,
}

impl ResultatB {
    /// Part d'effort dirigée vers la ressource devenue la meilleure, sur toute
    /// la fenêtre post-bascule. Ce compte inclut la transition : il mesure
    /// « combien de temps l'essaim a mis », pas « où il a fini ».
    pub fn part_effort_sur_la_meilleure(&self) -> f64 {
        let total: u64 = self.mesures.effort_apres_bascule.iter().sum();
        if total == 0 {
            return 0.0;
        }
        self.mesures.effort_apres_bascule[self.meilleure_ressource] as f64 / total as f64
    }

    /// Critère d'acceptation (1) : **où l'essaim a fini**. Part d'effort de la
    /// dernière tranche dirigée vers la ressource devenue la meilleure.
    ///
    /// C'est ce compte-là qui répond à « l'essaim sait-il désapprendre », et
    /// non le cumul : un essaim qui bascule correctement mais lentement a un
    /// cumul médiocre et une dernière tranche nette.
    pub fn part_effort_finale_sur_la_meilleure(&self) -> f64 {
        match self.mesures.effort_par_tranche.last() {
            Some(t) => {
                let total: u64 = t.iter().sum();
                if total == 0 {
                    0.0
                } else {
                    t[self.meilleure_ressource] as f64 / total as f64
                }
            }
            None => 0.0,
        }
    }

    /// Ressource la plus servie en fin d'exécution.
    ///
    /// C'est sur elle que se lisent les critères (1) et (2), et non sur un
    /// seuil de concentration : exiger qu'une fraction donnée de l'effort se
    /// porte sur une seule ressource contredirait la thèse du scénario, qui est
    /// que l'essaim **campe à distance bornée** de l'optimum sans l'atteindre.
    pub fn ressource_la_plus_servie_en_fin(&self) -> usize {
        self.mesures
            .effort_par_tranche
            .last()
            .map(|t| {
                t.iter()
                    .enumerate()
                    .max_by_key(|(_, n)| **n)
                    .map(|(j, _)| j)
                    .unwrap_or(0)
            })
            .unwrap_or(0)
    }

    /// Part d'effort final dirigée vers la **moitié devenue la plus utile**.
    ///
    /// C'est sur cette grandeur que se lit le désapprentissage, et non sur la
    /// ressource d'utilité maximale. Motif : le mécanisme tire selon
    /// φ^α·η^β, donc son attracteur est le maximum de u·η, pas celui de u. Avec
    /// les réglages du scénario B, trois ressources ont un produit u·η à moins
    /// de 2 % l'une de l'autre : l'essaim se répartit entre elles, ce qui est
    /// exactement « camper à distance bornée de l'optimum » et non un défaut.
    /// Exiger qu'une ressource nommée l'emporte testerait une propriété que le
    /// traité ne revendique pas.
    pub fn part_effort_finale_sur_la_moitie_haute(&self) -> f64 {
        let tranche = match self.mesures.effort_par_tranche.last() {
            Some(t) => t,
            None => return 0.0,
        };
        let total: u64 = tranche.iter().sum();
        if total == 0 {
            return 0.0;
        }
        // Après bascule, l'utilité croît avec l'indice : la moitié haute est la
        // seconde moitié des indices.
        let moitie = tranche.len() / 2;
        tranche[moitie..].iter().sum::<u64>() as f64 / total as f64
    }

    /// Critère (1) — l'essaim **suit** la bascule : à la fin, la majorité de
    /// son effort porte sur les ressources devenues les plus utiles.
    pub fn suit_la_bascule(&self) -> bool {
        self.part_effort_finale_sur_la_moitie_haute() > 0.5
    }

    /// Critère d'acceptation (3) : aucune violation de l'oracle EX-A11b.
    pub fn borne_tenue(&self) -> bool {
        self.violations.is_empty()
    }
}

/// Exécute le scénario B.
pub fn scenario_b(
    params: Params,
    graine: u64,
    budget_evenements: u64,
) -> Result<ResultatB, String> {
    let g = Granularite::Micro;
    // Le modèle de faute déclare **ce que le scénario injecte réellement**.
    // `ModeleFaute::default()` est sans faute ; l'écrire ici pendant que
    // `echec_action` et `crash_avant_validation` tournent faisait afficher
    // « aucune faute » à côté du compteur d'effets dupliqués qu'elles
    // produisent (EX-C06, EX-V07).
    //
    // Le moteur ne s'en sert toujours pas pour tirer : ces deux fautes sont
    // tirées par le mécanisme lui-même, dans `stigmergie`. Ce que la
    // configuration porte est donc la **déclaration** — versionnée, hachée,
    // affichée — et `hors_modele()` dit que le tirage est ailleurs.
    let mut fautes = sim_core::faute::ModeleFaute::default();
    fautes.injections = vec![
        sim_core::faute::Injection::Echec {
            operation: "action de l'agent".to_string(),
            probabilite: params.echec_action,
        },
        sim_core::faute::Injection::Echec {
            operation: "crash avant validation".to_string(),
            probabilite: params.crash_avant_validation,
        },
    ];
    let config = Config {
        graine,
        granularite: g,
        fautes: fautes.clone(),
        evenements_max: budget_evenements,
        secondes_coeur_max: None,
        scenario: "B".to_string(),
    };
    let mut moteur: Moteur<Evt> = Moteur::nouveau(graine, g, Budget::evenements(budget_evenements));

    // **Seconde instance d'`Alea` sur ce chemin, et il faut la dire.** Le moteur
    // porte la sienne ; celle-ci n'existe que pour l'amorçage, et elle est semée
    // de `graine ^ 0x5eed` — donc PD1 tient, le rejeu est exact et deux graines
    // distinctes restent distinctes. Ce qui ne tient pas est la valeur de
    // `Alea::tirages()` comme signal de divergence : les tirages d'amorçage
    // n'entrent pas dans le compteur du moteur, et un écart de chemin pendant
    // l'amorçage ne s'y verrait pas.
    let mut f = {
        let mut amorce = sim_core::alea::Alea::nouveau(graine ^ 0x5eed);
        Fourragement::nouveau(params, g, &mut amorce)?
    };
    f.armer_oracles(&mut moteur.oracles);
    moteur.couverture.declarer("cycle sans rétroaction");
    moteur
        .couverture
        .declarer("crash avant validation de décalage");
    moteur
        .couverture
        .declarer("décision inter-partitions sous le seuil de fiabilité");
    f.amorcer(&mut moteur);

    while let Some(ev) = moteur.suivant() {
        f.traiter(&mut moteur, ev.cible, ev.charge);
    }

    let violations = moteur
        .oracles
        .violations()
        .iter()
        .map(|v| format!("{} à {} : {}", v.oracle, v.date.0, v.details))
        .collect();

    let conformite =
        crate::conformite::estimer(f.milieu.partition(0).enregistrements()).map_err(str::to_string);

    Ok(ResultatB {
        conformite,
        diversite: f.tirage.familles().affichage(),
        meilleure_ressource: f.meilleure_ressource(),
        bascule_faite: f.bascule_faite(),
        bornes: f.params().bornes_applicables(),
        phi_moyen: f.phi_moyen(),
        partition_des_ressources: f.ressources.iter().map(|r| r.partition).collect(),
        couts_milieu: f.milieu.couts(),
        temps_logique: moteur.maintenant().0,
        avertissements: f.params().avertissements(),
        mesures: f.mesures.clone(),
        trace: moteur.trace().valeur(),
        violations,
        entete: config.entete(),
        modele_de_panne: fautes
            .resume()
            .iter()
            .map(|(cle, valeur)| format!("{cle} {valeur}"))
            .collect::<Vec<_>>()
            .join(" · "),
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Le traité livré, **texte cherchable**. C'est la source Pandoc/Typst dont
    /// `Traité.pdf` est le rendu : la provenance qu'un bloc cite s'y vérifie
    /// contre l'original, jamais contre une copie dérivée.
    const TRAITE: &str = include_str!("../../../Traité.md");

    /// Intervalles de pages des sections citées, **mesurés** dans `Traité.pdf` —
    /// troisième édition, 143 pages — par
    /// `pymupdf.open("Traité.pdf").get_toc()`.
    ///
    /// L'intervalle est fermé aux **deux** bouts, parce qu'une page porte la fin
    /// d'une section et le début de la suivante : la p. 5 achève l'introduction
    /// et ouvre le §1.1, et la thèse du scénario M y est.
    const PAGES_DES_SECTIONS: [(&str, u32, u32); 5] = [
        ("introduction", 3, 5),
        ("1.2", 12, 17),
        ("2.1", 23, 30),
        ("5.3", 82, 87),
        ("8.3", 124, 128),
    ];

    /// Les blocs dont la page a été **retrouvée dans le traité livré** — la
    /// troisième édition, 143 pages —, avec leur nom. Ce qu'ils citent est
    /// vérifié contre le traité par
    /// [`la_these_de_chaque_bloc_verifie_est_a_la_page_citee`].
    ///
    /// Il n'y a **pas** de liste de noms à côté : une liste qu'on compare à
    /// elle-même n'établit rien, et c'était le défaut de la version précédente.
    fn blocs_verifies() -> [(&'static str, &'static Bloc); 5] {
        [
            ("A", &BLOC_A),
            ("B", &BLOC_B),
            ("D", &crate::scenario_d::BLOC_D),
            ("K", &crate::gouvernance::BLOC_K),
            ("M", &crate::scenario_m::BLOC_M),
        ]
    }

    /// Découpe le traité en sections, par leurs titres : l'octet où chacune
    /// commence, et son étiquette — « 2.1 », « 8.3 », « introduction »,
    /// « conclusion ». Calculée sur le texte **déjà minusculé**, pour que les
    /// décalages coïncident avec ceux de la recherche.
    fn sections(traite: &str) -> Vec<(usize, String)> {
        let mut v = Vec::new();
        let mut octet = 0usize;
        for ligne in traite.split_inclusive('\n') {
            if let Some(titre) = ligne
                .strip_prefix("### ")
                .or_else(|| ligne.strip_prefix("## "))
            {
                let mot = titre.split_whitespace().next().unwrap_or("");
                v.push((octet, mot.trim_end_matches('.').to_string()));
            }
            octet += ligne.len();
        }
        v
    }

    /// Le plus long préfixe d'`aiguille` présent tel quel dans `traite` : sa
    /// longueur en octets, et l'octet où il commence dans le traité.
    fn plus_long_prefixe(traite: &str, aiguille: &str) -> Option<(usize, usize)> {
        let mut fin = aiguille.len();
        while fin > 0 {
            if aiguille.is_char_boundary(fin) {
                if let Some(pos) = traite.find(&aiguille[..fin]) {
                    return Some((fin, pos));
                }
            }
            fin -= 1;
        }
        None
    }

    /// Les provenances qu'un champ `source` déclare : pour chaque marqueur de
    /// section — `§X.Y`, « introduction », « conclusion » —, la **première** page
    /// citée après lui et avant le marqueur suivant.
    ///
    /// Les pages qui ne suivent aucun marqueur ne sont pas rattachables et ne
    /// sont donc pas vérifiées : « tableau 3, p. 18 » du bloc A est dans ce cas.
    fn provenances(source: &str) -> Vec<(String, u32)> {
        let bas = source.to_lowercase();
        let mut marqueurs: Vec<(usize, String)> = Vec::new();
        for (i, _) in bas.match_indices('§') {
            let etiquette: String = bas[i + '§'.len_utf8()..]
                .chars()
                .take_while(|c| c.is_ascii_digit() || *c == '.')
                .collect();
            let etiquette = etiquette.trim_end_matches('.').to_string();
            if !etiquette.is_empty() {
                marqueurs.push((i, etiquette));
            }
        }
        for mot in ["introduction", "conclusion"] {
            for (i, _) in bas.match_indices(mot) {
                marqueurs.push((i, mot.to_string()));
            }
        }
        marqueurs.sort();

        let mut v = Vec::new();
        for (k, (debut, etiquette)) in marqueurs.iter().enumerate() {
            let fin = marqueurs.get(k + 1).map_or(bas.len(), |(j, _)| *j);
            let portion = &bas[*debut..fin];
            if let Some(p) = portion.find("p. ") {
                let chiffres: String = portion[p + "p. ".len()..]
                    .chars()
                    .take_while(|c| c.is_ascii_digit())
                    .collect();
                if let Ok(page) = chiffres.parse::<u32>() {
                    v.push((etiquette.clone(), page));
                }
            }
        }
        v
    }

    /// Les dix blocs livrés, avec leur nom. Une seule liste : elle sert à la
    /// clause de provenance et à la clause d'édition, qui portent toutes deux
    /// sur les dix et qui divergeaient quand chacune tenait la sienne.
    fn tous_les_blocs() -> [(&'static str, &'static Bloc); 10] {
        [
            ("A", &BLOC_A),
            ("B", &BLOC_B),
            ("D", &crate::scenario_d::BLOC_D),
            ("E", &crate::adhesion::BLOC_E),
            ("F", &crate::allocation::BLOC_F),
            ("G", &crate::agregat_fenetre::BLOC_G),
            ("J", &crate::cascade::BLOC_J),
            ("K", &crate::gouvernance::BLOC_K),
            ("L", &crate::taux_de_base::BLOC_L),
            ("M", &crate::scenario_m::BLOC_M),
        ]
    }

    /// F2 — le champ `source` d'un bloc PD8 porte **la section et la page**. Une
    /// page manquante n'est pas une imprécision : c'est une provenance absente,
    /// et cinq blocs sur dix en étaient là.
    #[test]
    fn les_dix_blocs_portent_leur_section_et_leur_page() {
        for (nom, b) in tous_les_blocs() {
            assert!(b.source.contains('§'), "bloc {nom} : aucune section");
            assert!(
                b.source.contains("p. "),
                "bloc {nom} : aucune page — provenance absente (F2)"
            );
            for (champ, valeur) in [
                ("en_clair", b.en_clair),
                ("these", b.these),
                ("mecanisme_visible", b.mecanisme_visible),
                ("ne_demontre_pas", b.ne_demontre_pas),
            ] {
                assert!(!valeur.trim().is_empty(), "bloc {nom} : champ {champ} vide");
            }
        }
    }

    /// F2, clause d'édition — **la page seule n'est pas une provenance.**
    ///
    /// Le traité livré dans ce dépôt est la **troisième** édition, du 15 août
    /// 2026, 143 pages, et ces cinq blocs citaient des pages qui n'y résolvent
    /// pas — trois d'entre elles tombant hors de la section citée. Mesuré dans le
    /// PDF du dépôt :
    ///
    /// | bloc | page citée | ce qu'on y trouve | page réelle dans le traité |
    /// |---|---|---|---|
    /// | A | §1.3, p. 21 | §1.3, mais pas la thèse | §2.1, p. 25 |
    /// | B | §1.2, p. 13 | §1.2, ni la thèse ni l'algorithme 1.2 | p. 16 ; algo 2 p. 14 |
    /// | D | §2.1, p. 22 | §1.3 — hors de la section citée | p. 26 ; fig. 2.1c p. 28 |
    /// | K | §5.3, p. 63 | §4.2 — hors de la section citée | tableau 16, p. 84 |
    /// | M | §8.3, p. 94 | §6.2 — hors de la section citée | p. 127 |
    ///
    /// La clause porte sur **les dix**, et non sur les cinq ci-dessus. Les blocs
    /// E, F, G, J et L citaient déjà des pages qui résolvent dans la troisième
    /// édition — algorithme 1.3 p. 21, figure 5.2 p. 80, tableau 15 p. 81, §7.1
    /// p. 104, figure 6.1 p. 91, tableau 13 p. 72, figure 7.2 p. 107, tableau 19
    /// p. 110, toutes retrouvées —, mais ils ne la nommaient pas : leurs pages
    /// se relisaient donc comme celles d'une édition inconnue, ce qui est
    /// précisément ce que F2 refuse. Ils vivent dans cinq modules de mécanismes,
    /// hors du morceau où cette clause a été écrite, et c'est la seule raison
    /// pour laquelle elle ne les couvrait pas.
    ///
    /// Ils restent hors de [`blocs_verifies`], pour un autre motif : deux de
    /// leurs thèses sont des reformulations du produit et non des citations, de
    /// sorte que la vérification mot pour mot du test suivant ne s'y applique
    /// pas.
    ///
    /// **Ce test ne vaut que par le suivant.** Nommer une édition est une clause
    /// de forme : une page fausse qui la nomme la satisfait. C'est
    /// [`la_these_de_chaque_bloc_verifie_est_a_la_page_citee`] qui interroge le
    /// traité.
    #[test]
    fn les_dix_blocs_nomment_leur_edition() {
        for (nom, b) in tous_les_blocs() {
            assert!(
                b.source.contains("4ᵉ éd."),
                "bloc {nom} : page citée sans son édition — {}",
                b.source
            );
        }
    }

    /// F2 — **la thèse citée par un bloc se retrouve dans le traité livré, sous
    /// la section que le bloc nomme, à une page que cette section contient.**
    ///
    /// C'est ce que le test précédent ne peut pas faire, et c'est ce pour quoi
    /// les deux existent. La vérification tient en trois temps, tous menés
    /// contre `Traité.md` — la source Pandoc dont le PDF est le rendu :
    ///
    /// 1. la thèse est **retrouvée mot pour mot**, en un ou plusieurs morceaux
    ///    contigus (la casse et la ponctuation finale exceptées) ;
    /// 2. **chaque** morceau tombe sous une section que `source` nomme — c'est
    ///    ce qui a manqué aux blocs A, D, K et M, dont la page citée tombait hors
    ///    de la section citée ;
    /// 3. chaque page citée à côté d'un marqueur de section tombe dans
    ///    l'intervalle mesuré de cette section ([`PAGES_DES_SECTIONS`]).
    ///
    /// Le point 2 vaut épreuve de l'**épissure** du bloc M : sa thèse est reprise
    /// de deux endroits, l'introduction p. 5 pour la proposition principale et le
    /// §8.3 du traité, p. 127, pour l'énumération des trois — troisième édition
    /// dans les deux cas —, et `source` doit nommer les deux.
    /// Le §8.3 écrit la proposition autrement — « la mesure ajoute qu'il rend
    /// tout aussi bon marché » —, de sorte qu'un aveu qui ne citerait que lui
    /// serait faux.
    ///
    /// **Ce qui reste hors de portée, et il faut le dire.** `Traité.md` ne porte
    /// aucune pagination : elle naît du rendu Typst. Une page fausse **à
    /// l'intérieur** de la bonne section passe donc encore — c'était le cas du
    /// bloc B, qui citait la p. 13 pour une thèse qui est p. 16, l'une et l'autre
    /// dans le §1.2. Vérifier la page exacte demanderait de lire le PDF, donc une
    /// dépendance d'extraction, ou de committer un dépouillement page à page,
    /// c'est-à-dire une seconde copie du traité qui peut diverger de la première
    /// sans que rien ne le dise. L'intervalle de section ramène la latitude de
    /// 143 pages à cinq ou six ; le reste est tenu par la relecture.
    #[test]
    fn la_these_de_chaque_bloc_verifie_est_a_la_page_citee() {
        let traite = TRAITE.to_lowercase();
        let sections = sections(&traite);
        let section_a = |octet: usize| -> String {
            sections
                .iter()
                .rev()
                .find(|(debut, _)| *debut <= octet)
                .map_or_else(|| "hors section".to_string(), |(_, e)| e.clone())
        };

        for (nom, b) in blocs_verifies() {
            // 1 et 2 — la thèse, morceau par morceau, et la section de chacun.
            let these = b.these.to_lowercase();
            let mut reste = these.trim_end_matches(['.', ' ']);
            let mut morceaux = 0;
            while reste.chars().any(char::is_alphanumeric) {
                let (long, octet) = plus_long_prefixe(&traite, reste).unwrap_or_else(|| {
                    panic!("bloc {nom} : « {reste} » ne se trouve nulle part dans le traité livré")
                });
                assert!(
                    long >= 30,
                    "bloc {nom} : la thèse se disloque en morceaux de moins de 30 signes \
                     — « {} » ; ce n'est plus une citation",
                    &reste[..long]
                );
                let section = section_a(octet);
                let (libelle, nommee) = match section.as_str() {
                    "introduction" | "conclusion" => (
                        format!("l'{section}"),
                        b.source.to_lowercase().contains(&section),
                    ),
                    _ => (
                        format!("§{section}"),
                        b.source.contains(&format!("§{section}")),
                    ),
                };
                assert!(
                    nommee,
                    "bloc {nom} : « {} » est dans {libelle} du traité, que `source` ne nomme \
                     pas — {}",
                    &reste[..long.min(60)],
                    b.source
                );
                reste = reste[long..].trim_start_matches(|c: char| !c.is_alphanumeric());
                morceaux += 1;
            }
            assert!(morceaux >= 1, "bloc {nom} : thèse vide");

            // 3 — chaque page citée est dans l'intervalle de la section citée.
            let declarees = provenances(b.source);
            assert!(
                !declarees.is_empty(),
                "bloc {nom} : aucune page rattachée à une section — {}",
                b.source
            );
            for (section, page) in declarees {
                let (_, debut, fin) = PAGES_DES_SECTIONS
                    .iter()
                    .find(|(s, _, _)| *s == section)
                    .unwrap_or_else(|| {
                        panic!(
                            "bloc {nom} : intervalle de pages non mesuré pour {section} \
                             — le relever dans `Traité.pdf` avant de citer"
                        )
                    });
                assert!(
                    (*debut..=*fin).contains(&page),
                    "bloc {nom} : {section} occupe les pages {debut} à {fin} du traité livré, \
                     et le bloc cite la p. {page} — {}",
                    b.source
                );
            }
        }
    }

    /// Scénario A, critère d'acceptation — à n faible et ℓ₉₉ élevé, la maille
    /// gagne **en temps** : un aller simple contre deux tours de journal.
    #[test]
    fn a_petite_echelle_la_maille_gagne_en_temps() {
        let c = scenario_a(8, 8, 200.0, 2.0, 3, 0.0, 1);
        assert!(c.maille_temps < c.journal_temps);
        assert!(c
            .verdict_temps(Granularite::Micro)
            .contains("la maille gagne"));
    }

    /// Et à ℓ₉₉ faible, le journal reprend l'avantage : le croisement est
    /// déplaçable par le curseur, comme l'exige le scénario.
    #[test]
    fn a_faible_l99_le_journal_gagne_en_temps() {
        let c = scenario_a(8, 8, 0.5, 20.0, 3, 0.0, 1);
        assert!(c.journal_temps < c.maille_temps);
    }

    /// Scénario A, critère d'acceptation — à n élevé, l'entretien de vue croît
    /// quadratiquement alors que le compte de lectures reste en Θ(n).
    #[test]
    fn a_grande_echelle_lentretien_de_vue_ecrase_la_maille() {
        let petit = scenario_a(16, 8, 20.0, 2.0, 3, 0.0, 1);
        let grand = scenario_a(160, 8, 20.0, 2.0, 3, 0.0, 1);
        let facteur_entretien = grand.maille_entretien as f64 / petit.maille_entretien as f64;
        let facteur_lectures = grand.journal_lectures as f64 / petit.journal_lectures as f64;
        assert!(
            facteur_entretien > 90.0,
            "entretien ×{facteur_entretien:.1}"
        );
        assert!(
            (facteur_lectures - 10.0).abs() < 0.01,
            "lectures ×{facteur_lectures:.1}"
        );
        assert_eq!(grand.journal_entretien, 0);
    }

    /// F1 — le diamètre de la maille n'est pas inventé.
    #[test]
    fn le_diametre_de_la_maille_reste_absent() {
        let (journal, maille) = Comparaison::diametres();
        assert!(journal.contains("2 en permanence"));
        assert!(maille.contains("provenance absente"));
    }
}
