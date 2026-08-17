//! **Les sept dettes d'indépendance** du tableau 21 (EX-A58, §8.1).
//!
//! > Sept énoncés de cet ouvrage supposent l'indépendance des tirages ou des
//! > fautes ; aucun ne le dit dans son énoncé ; tous cessent de tenir à
//! > Φ_c = 1. […] Aucun n'est faux ; tous changent de domaine de validité.
//! > (§8.1)
//!
//! Ce module n'ajoute **aucun mécanisme**. Il arme sur du code existant une
//! hypothèse que ce code portait sans la dire, et il applique NF-14 : dès que Φ_c
//! mesuré dépasse la précision de son estimation, la borne correspondante est
//! **effacée** — ni grisée, ni pointillée, ni astérisquée —, y compris quand la
//! mesure est meilleure qu'elle.
//!
//! **C'est le livrable le moins coûteux et le plus facile à oublier de la phase
//! 6.** Six des sept dettes portent sur des bornes déjà livrées et déjà mesurées
//! dans ce dépôt ; sans lui, le simulateur tourne, les bornes cessent de tenir,
//! et rien ne le signale.

use sim_core::famille::Familles;

/// Une dette : un énoncé du produit, l'hypothèse d'indépendance qu'il porte sans
/// le dire, et ce qu'il devient à conformité maximale.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct Dette {
    /// L'énoncé, tel que le tableau 21 le nomme.
    pub enonce: &'static str,
    /// L'hypothèse d'indépendance qu'il suppose.
    pub hypothese: &'static str,
    /// Section du traité où l'énoncé se trouve.
    pub section: &'static str,
    /// Où il est livré dans ce dépôt — code d'exigence et scénario.
    pub livre_ici: &'static str,
    /// Ce qu'il devient à conformité maximale.
    pub a_conformite_maximale: &'static str,
    /// Vrai si le produit sait mettre cette dette en défaut par un réglage.
    ///
    /// Trois des sept sont fausses, et c'est un aveu, pas un détail : la dette
    /// est réelle, le produit ne peut pas la démontrer, et l'affichage doit dire
    /// laquelle des deux situations il montre.
    pub mesurable_ici: bool,
}

/// Les sept dettes, dans l'ordre du tableau 21.
pub const DETTES: &[Dette] = &[
    Dette {
        enonce: "plancher d'exploration du renforcement stigmergique",
        hypothese: "tirages des n agents indépendants",
        section: "§1.2",
        livre_ici: "EX-A11b/c, scénario B — oracle armé en permanence",
        a_conformite_maximale:
            "la population explore comme un seul agent ; le plancher est atteint n fois au \
             même endroit",
        mesurable_ici: true,
    },
    Dette {
        enonce: "redondance de facteur k",
        hypothese: "défaillances des répliques indépendantes",
        section: "§2.1",
        livre_ici: "EX-M05 à EX-M08, scénario D",
        a_conformite_maximale:
            "n répliques valent 1 ; la corrélation porte désormais sur la décision, plus \
             seulement sur la panne",
        mesurable_ici: true,
    },
    Dette {
        enonce: "décorrélation par gigue pleine",
        hypothese: "les délais tirés diffèrent d'un agent à l'autre",
        section: "§2.3",
        livre_ici: "annexe B du PRD — repère externe, non implanté",
        a_conformite_maximale:
            "la gigue décorrèle les instants, jamais le choix : tous relâchent différemment \
             vers la même cible",
        mesurable_ici: false,
    },
    Dette {
        enonce: "approximation de champ moyen",
        hypothese: "échangeabilité ET décorrélation des tirages",
        section: "§3.1",
        livre_ici: "EX-A16, EX-A53, RQ5",
        a_conformite_maximale:
            "la fraction de population dans un état vaut 0 ou 1 ; la fluctuation en 1/√n est \
             fausse",
        mesurable_ici: false,
    },
    Dette {
        enonce: "vérification statistique",
        hypothese: "épisodes échantillonnés indépendants",
        section: "§3.3",
        livre_ici: "§8.4 du PRD, EX-C18, scénario L critère 3",
        a_conformite_maximale:
            "l'échantillon mesure une population plus étroite que celle qu'il croit décrire",
        mesurable_ici: false,
    },
    Dette {
        enonce: "auto-affectation à deux sondes",
        hypothese: "choix des serveurs sondés indépendants",
        section: "§5.2",
        livre_ici: "EX-A05, scénario F critère 3",
        a_conformite_maximale:
            "tous sondent les mêmes candidats ; l'amélioration exponentielle disparaît",
        mesurable_ici: true,
    },
    Dette {
        enonce: "corroboration r parmi n détecteurs",
        hypothese: "détecteurs indépendants",
        section: "§7.2",
        livre_ici: "EX-A31, scénario L",
        a_conformite_maximale:
            "le gain de précision de la corroboration s'annule ; le taux de base reprend ses \
             droits",
        mesurable_ici: true,
    },
];

/// Ce que devient une borne, à Φ_c donné.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum EtatDeBorne {
    /// Affichée : l'hypothèse d'indépendance tient, à la précision de la mesure.
    Affichee,
    /// **Effacée** (NF-14). Ni grisée, ni pointillée, ni astérisquée — y compris
    /// quand la mesure est meilleure que la borne effacée.
    Effacee,
}

/// Verdict porté sur une dette à une conformité mesurée.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Verdict {
    /// La dette concernée.
    pub dette: Dette,
    /// Ce que devient sa borne.
    pub etat: EtatDeBorne,
}

impl Verdict {
    /// Le libellé affiché à la place de la borne, quand elle est effacée.
    ///
    /// La phrase du traité est reprise telle quelle, parce qu'elle est exactement
    /// ce qu'il faut lire : ce n'est pas un résultat qui devient faux, c'est un
    /// domaine de validité qui change.
    pub fn libelle(&self) -> String {
        match self.etat {
            EtatDeBorne::Affichee => format!("{} — borne affichée", self.dette.enonce),
            EtatDeBorne::Effacee => format!(
                "{} — borne EFFACÉE : {} suppose « {} ». {}. Aucun n'est faux ; tous changent \
                 de domaine de validité ({})",
                self.dette.enonce,
                self.dette.livre_ici,
                self.dette.hypothese,
                self.dette.a_conformite_maximale,
                self.dette.section
            ),
        }
    }
}

/// Applique NF-14 aux sept dettes, **d'après le réglage** et non d'après la
/// mesure.
///
/// Le critère est la structure des familles de décision (EX-C19) : dès que deux
/// agents partagent une famille, leurs tirages ne sont **démontrablement** plus
/// indépendants, et NF-14 s'applique — « un réglage qui viole une hypothèse
/// efface la borne ».
///
/// **Pourquoi pas Φ_c mesuré**, qui était le premier critère écrit ici. Parce que
/// Φ_c ne sépare pas ses deux causes : sur un essaim stigmergique il vaut déjà
/// ≈ 0,17 avec un tirage par agent, la corrélation venant du milieu que tous
/// lisent (voir [`crate::conformite::CONSTAT_DE_MESURE`]). Effacer une borne sur
/// cette base serait affirmer que l'hypothèse d'indépendance des **tirages** est
/// violée alors que ce qui est mesuré est la coordination — une fausse alarme, et
/// la discipline de PD12 vaut ici : ce qui est soupçonné ne se présente pas comme
/// prouvé.
///
/// Φ_c reste affiché comme une **mesure**, à côté et jamais à la place.
///
/// **Ce que ce critère efface de trop, et il faut le dire.** La structure des
/// familles viole l'indépendance des **tirages**. Or trois des sept dettes
/// supposent l'indépendance d'autre chose : la deuxième celle des *défaillances*
/// de répliques, la cinquième celle des *épisodes* échantillonnés, la troisième
/// celle des *délais* de gigue. Un curseur de familles ne touche à aucune des
/// trois, et leurs bornes sont pourtant effacées avec les quatre autres. Le
/// verdict est donc conservateur, et il l'est dans le sens que NF-14 ne demande
/// pas : effacer une borne dont l'hypothèse tient est l'erreur symétrique de
/// garder une borne dont l'hypothèse est tombée. Le corriger déplacerait le
/// critère de sortie de la phase 6, qui compte sept effacements ; c'est une
/// décision de produit, pas de module.
pub fn verdicts(familles: &Familles) -> Vec<Verdict> {
    let efface = familles.diversite_effective() < familles.n();
    DETTES
        .iter()
        .map(|d| Verdict {
            dette: *d,
            etat: if efface {
                EtatDeBorne::Effacee
            } else {
                EtatDeBorne::Affichee
            },
        })
        .collect()
}

/// Les dettes que le produit sait mettre en défaut par un réglage, et celles
/// qu'il porte sans savoir les démontrer.
///
/// À afficher ensemble : une dette non mesurable ici n'est pas une dette
/// moindre, c'est une dette dont le produit ne peut que citer la conséquence
/// (PD6).
pub fn partage_mesurable() -> (usize, usize) {
    let m = DETTES.iter().filter(|d| d.mesurable_ici).count();
    (m, DETTES.len() - m)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn le_tableau_21_porte_ses_sept_lignes() {
        assert_eq!(DETTES.len(), 7);
        for d in DETTES {
            assert!(!d.enonce.is_empty());
            assert!(!d.hypothese.is_empty());
            assert!(d.section.starts_with('§'));
            assert!(!d.livre_ici.is_empty());
            assert!(!d.a_conformite_maximale.is_empty());
        }
    }

    #[test]
    fn quatre_dettes_sur_sept_sont_mesurables_ici() {
        // Le §0.0 du PRD annonce que six des sept portent sur des mesures
        // livrées ; seules quatre ont un curseur qui les met en défaut. La
        // différence est ce que l'affichage doit dire, et ce test la fixe.
        assert_eq!(partage_mesurable(), (4, 3));
    }

    #[test]
    fn une_famille_par_agent_naffiche_aucun_effacement() {
        let f = Familles::une_par_agent(24);
        for v in verdicts(&f) {
            assert_eq!(v.etat, EtatDeBorne::Affichee);
            assert!(v.libelle().contains("borne affichée"));
        }
    }

    #[test]
    fn des_que_deux_agents_partagent_une_famille_les_sept_bornes_seffacent() {
        for f in [Familles::unique(24), Familles::interpole(24, 0.5)] {
            let v = verdicts(&f);
            assert_eq!(v.len(), 7);
            assert!(
                v.iter().all(|x| x.etat == EtatDeBorne::Effacee),
                "diversité {} sur {} agents",
                f.diversite_effective(),
                f.n()
            );
        }
        assert!(verdicts(&Familles::unique(24))[0].libelle().contains("EFFACÉE"));
    }

    #[test]
    fn leffacement_suit_le_reglage_et_non_une_mesure() {
        // C'est la correction imposée par le constat de mesure : Φ_c mesuré ne
        // sépare pas la conformité de la coordination, donc il ne peut pas
        // décider d'un effacement. Le réglage, lui, est connu.
        let interpolee = Familles::interpole(100, 0.01);
        assert!(interpolee.diversite_effective() < interpolee.n());
        assert!(verdicts(&interpolee)
            .iter()
            .all(|v| v.etat == EtatDeBorne::Effacee));
    }

    #[test]
    fn le_libelle_deffacement_ne_dit_jamais_que_le_resultat_est_faux() {
        let l = verdicts(&Familles::unique(8))[0].libelle();
        assert!(l.contains("changent de domaine de validité"));
        // La phrase du traité dit « Aucun n'est faux » : c'est la rassurance. Ce
        // qu'il faut interdire est l'inverse — annoncer que le résultat livré
        // serait devenu faux.
        assert!(!l.contains("devient faux"));
        assert!(!l.contains("résultat faux"));
    }
}
