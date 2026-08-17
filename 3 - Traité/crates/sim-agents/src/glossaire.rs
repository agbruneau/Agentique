//! Le vocabulaire de l'interface, défini une fois.
//!
//! Ce module ne calcule rien : c'est une **donnée**, au même titre que les
//! scénarios du §5.1c du PRD, et il vit ici plutôt que dans `sim-viz` pour la même
//! raison que [`crate::hors_perimetre`] et que `Bornes::LEGENDE` — ce qui vient
//! du traité ne se recopie pas dans la couche qui dessine.
//!
//! ## La règle de portée : on ne définit que ce qui est à l'écran
//!
//! Un glossaire exhaustif du traité serait un second traité, et personne ne le
//! lirait ; celui-ci s'arrête aux termes que l'interface **affiche**. Le §12 C du
//! PRD tient la liste complète, et c'est là qu'un lecteur qui veut tout va.
//!
//! ## La provenance est un champ, pas une note
//!
//! EX-V11 sépare trois provenances et refuse qu'elles se mêlent. Un glossaire
//! est l'endroit où la confusion s'installe le plus facilement : une définition
//! écrite par le produit se lit exactement comme une définition du traité. Chaque
//! entrée porte donc sa [`Terme::provenance`], et trois formes seulement y
//! apparaissent — une référence de section, « nomenclature du produit », ou
//! « réglage de cette interface ».

/// Une entrée du glossaire affiché par l'interface.
#[derive(Clone, Copy, Debug)]
pub struct Terme {
    /// Le titre de section sous lequel l'entrée se range. Les entrées d'un même
    /// groupe sont **contiguës** dans [`glossaire`] : la vue regroupe en
    /// comparant au terme précédent, sans trier.
    pub groupe: &'static str,
    /// Le mot ou le symbole **tel qu'il apparaît à l'écran**, et non sa forme
    /// canonique : un lecteur cherche ici ce qu'il vient de lire ailleurs.
    pub terme: &'static str,
    /// Ce que le terme désigne, en langue courante. Jamais une citation : la
    /// citation, quand elle existe, est dans le bloc de trois du scénario.
    pub definition: &'static str,
    /// D'où vient la définition — section du traité, nomenclature du produit, ou
    /// réglage de l'interface (EX-V11). Jamais vide.
    pub provenance: &'static str,
}

/// Le vocabulaire que les écrans emploient, groupé par thème et dans l'ordre où
/// il se rencontre.
///
/// L'ordre n'est **pas** alphabétique, à dessein : un lecteur qui découvre le
/// sujet a besoin de « milieu » avant « trace », et de « trace » avant « γ ».
/// L'ordre alphabétique sert la recherche d'un terme connu, pas l'apprentissage
/// d'un vocabulaire, et l'écran a un champ de recherche pour le premier usage.
pub fn glossaire() -> &'static [Terme] {
    const DEUX_REGIMES: &str = "Les deux façons de coordonner";
    const STIGMERGIE: &str = "Le mécanisme stigmergique";
    const REGLAGES: &str = "Ce que les curseurs déplacent";
    const JUGEMENT: &str = "Ce qui juge un résultat";

    &[
        // -- Les deux façons de coordonner ------------------------------------
        Terme {
            groupe: DEUX_REGIMES,
            terme: "essaim",
            definition:
                "une population de programmes qui poursuivent un but commun sans qu'aucun d'eux \
                 ne voie l'ensemble. C'est l'absence de vue globale qui fait l'essaim, pas le \
                 nombre.",
            provenance: "§1.1 — définition d'essaim",
        },
        Terme {
            groupe: DEUX_REGIMES,
            terme: "maille pair à pair",
            definition:
                "le premier régime : chaque agent nomme ses destinataires et leur envoie un \
                 message. Pour nommer quelqu'un, il faut savoir qu'il est là — d'où le coût \
                 d'entretien de vue, qui est le terme qui explose.",
            provenance: "§1.3, tableau 3, p. 18 (3ᵉ éd.)",
        },
        Terme {
            groupe: DEUX_REGIMES,
            terme: "journal",
            definition:
                "le second régime : chaque agent écrit dans un cahier commun en ajout seul, et \
                 chacun le relit à son rythme. Personne n'a de destinataire à connaître.",
            provenance: "§1.3 ; figure 0, p. 4 (3ᵉ éd.)",
        },
        Terme {
            groupe: DEUX_REGIMES,
            terme: "milieu",
            definition:
                "le substrat partagé où les agents déposent et lisent. Ici, c'est le journal \
                 partitionné, et rien d'autre : le milieu n'est pas une métaphore, c'est le \
                 composant qu'on facture à part.",
            provenance: "§1.2 — algorithme 2",
        },
        Terme {
            groupe: DEUX_REGIMES,
            terme: "entretien de vue",
            definition:
                "ce que la maille dépense pour savoir qui est encore là : à chaque période, \
                 chaque agent sonde chaque autre, soit un coût en n². Le journal n'a aucun \
                 équivalent — ce n'est pas « négligeable », c'est zéro.",
            provenance: "§1.3",
        },
        Terme {
            groupe: DEUX_REGIMES,
            terme: "aller simple",
            definition:
                "le temps d'un message qui part et arrive, sans réponse attendue. C'est l'unité \
                 de temps de la maille.",
            provenance: "§1.1 — convention de comptage",
        },
        Terme {
            groupe: DEUX_REGIMES,
            terme: "tour de journal",
            definition:
                "le chemin complet écriture → accusé de durabilité → lecture. Sa durée est ℓ₉₉, \
                 pas un aller simple : c'est ce qui rend les deux régimes comparables en temps et \
                 non seulement en messages.",
            provenance: "§6.1",
        },
        Terme {
            groupe: DEUX_REGIMES,
            terme: "diamètre",
            definition:
                "le nombre de sauts au pire entre deux agents. Le traité en donne un au journal — \
                 2, en permanence — et n'en donne aucun à la maille. L'interface affiche cette \
                 absence au lieu de la combler.",
            provenance: "§1.3, p. 18 (3ᵉ éd.)",
        },
        // -- Le mécanisme stigmergique ----------------------------------------
        Terme {
            groupe: STIGMERGIE,
            terme: "stigmergie",
            definition:
                "coordonner en modifiant le milieu plutôt qu'en s'adressant à quelqu'un. L'agent \
                 qui dépose ne sait pas qui lira, et l'agent qui lit ne sait pas qui a déposé.",
            provenance: "§1.2",
        },
        Terme {
            groupe: STIGMERGIE,
            terme: "trace",
            definition:
                "un enregistrement en ajout seul et durable. Une fois écrite, elle ne se corrige \
                 pas : elle s'efface d'elle-même, et c'est l'évaporation qui fait ce travail.",
            provenance: "§1.2",
        },
        Terme {
            groupe: STIGMERGIE,
            terme: "φ",
            definition:
                "l'intensité de la trace sur une ressource : combien l'essaim l'a servie \
                 récemment. Elle monte à chaque dépôt et redescend toute seule entre deux \
                 fenêtres.",
            provenance: "§1.2, algorithme 2, p. 14 (3ᵉ éd.)",
        },
        Terme {
            groupe: STIGMERGIE,
            terme: "γ — évaporation",
            definition:
                "ce qui reste d'une trace après une fenêtre : à 0,90, un dixième s'oublie à \
                 chaque tour. C'est l'oubli qui permet de désapprendre ; porté à 1, plus rien ne \
                 s'oublie et les bornes du traité cessent de s'appliquer.",
            provenance: "§1.2, p. 14 (3ᵉ éd.)",
        },
        Terme {
            groupe: STIGMERGIE,
            terme: "τ — fenêtre",
            definition:
                "la durée sur laquelle l'évaporation γ s'applique une fois. Longue, la trace \
                 persiste ; courte, elle s'évapore entre deux décisions.",
            provenance: "§1.2, p. 14 (3ᵉ éd.)",
        },
        Terme {
            groupe: STIGMERGIE,
            terme: "α — poids de la trace",
            definition:
                "combien l'agent écoute ce que l'essaim vient de faire. Élevé, il suit le groupe \
                 et l'essaim se concentre.",
            provenance: "§1.2, algorithme 2, p. 14 (3ᵉ éd.)",
        },
        Terme {
            groupe: STIGMERGIE,
            terme: "η, β — l'heuristique et son poids",
            definition:
                "η est ce que l'agent croyait savoir avant de commencer, et β le crédit qu'il lui \
                 accorde. η ne bouge jamais : après une bascule d'utilité, cette croyance est \
                 périmée, et β élevé retient l'essaim dans le passé.",
            provenance: "§1.2, algorithme 2, p. 14 (3ᵉ éd.)",
        },
        Terme {
            groupe: STIGMERGIE,
            terme: "bascule d'utilité",
            definition:
                "l'épreuve que le scénario B impose à mi-parcours : la moitié des ressources la \
                 moins bonne devient la meilleure, sans que rien ne l'annonce. Un essaim qui ne \
                 sait pas oublier ne la suit pas.",
            provenance: "nomenclature du produit — le traité ne nomme pas cette épreuve",
        },
        // -- Ce que les curseurs déplacent ------------------------------------
        Terme {
            groupe: REGLAGES,
            terme: "n",
            definition:
                "le nombre d'agents. Chaque agent lit ce que toute la population écrit : doubler \
                 n quadruple à peu près le coût d'une exécution.",
            provenance: "réglage de cette interface",
        },
        Terme {
            groupe: REGLAGES,
            terme: "T — période de cycle",
            definition:
                "le temps entre deux décisions du même agent. Sous ℓ₉₉, l'agent redécide avant \
                 d'avoir pu se relire : il agit sur une trace qui ne contient pas encore la \
                 sienne.",
            provenance: "réglage de cette interface",
        },
        Terme {
            groupe: REGLAGES,
            terme: "ℓ₉₉",
            definition:
                "une latence au 99ᵉ centile : le délai que 99 lectures sur 100 ne dépassent pas. \
                 Deux grandeurs distinctes portent ce nom et ne se mêlent jamais — celle du \
                 milieu est une entrée du modèle, celle de réponse d'un agent en est une sortie. \
                 Cette interface n'affiche que la première.",
            // Le renvoi nu « §8.3 » était ambigu et se lisait du mauvais côté :
            // le §8.3 du **traité** porte sur les buts incompatibles (p. 124, 3ᵉ éd.), pas
            // sur les latences. La séparation des deux ℓ₉₉ est une règle du
            // produit, écrite au §8.3 du **PRD**. La grandeur elle-même, elle,
            // vient du §6.1 du traité.
            provenance: "nomenclature du produit — §8.3 du PRD ; la grandeur, elle, est du \
                         §6.1 du traité",
        },
        Terme {
            groupe: REGLAGES,
            terme: "partition",
            definition:
                "une tranche du journal. L'ordre est total à l'intérieur d'une partition et \
                 inexistant entre deux : c'est M2, et c'est pourquoi la carte de φ sépare les \
                 partitions au lieu de les dégrader l'une dans l'autre.",
            provenance: "§6.1 — M1 à M4",
        },
        Terme {
            groupe: REGLAGES,
            terme: "graine",
            definition:
                "le nombre qui fixe tous les tirages au hasard de l'exécution. À graine et \
                 réglages identiques, deux exécutions rendent les mêmes chiffres, bit pour bit.",
            provenance: "réglage de cette interface",
        },
        Terme {
            groupe: REGLAGES,
            terme: "budget d'événements",
            definition:
                "ce qui arrête l'exécution — un compte d'événements, jamais un compte de \
                 secondes. C'est ce qui la rend reproductible d'une machine à l'autre.",
            provenance: "réglage de cette interface",
        },
        Terme {
            groupe: REGLAGES,
            terme: "temps logique / temps mural",
            definition:
                "le temps logique est celui du système modélisé, compté en tics ; le temps mural \
                 est celui que votre machine a passé à calculer. Aucun des deux ne prédit l'autre, \
                 et aucun chiffre d'ici ne prédit la latence d'un système déployé.",
            provenance: "§3.3 — algorithme 3",
        },
        // -- Ce qui juge un résultat ------------------------------------------
        Terme {
            groupe: JUGEMENT,
            terme: "modèle de panne",
            definition:
                "ce qui a le droit de mal tourner dans l'exécution. Ce qui n'y figure pas ne se \
                 produit jamais — et a donc, dans tout résultat, une probabilité de faute nulle. \
                 C'est pourquoi il est affiché en permanence.",
            provenance: "§3.1 — conditions d'utilisabilité d'un modèle",
        },
        Terme {
            groupe: JUGEMENT,
            terme: "asynchrone",
            definition:
                "l'hypothèse de temps de ces exécutions : les délais sont finis, mais aucune \
                 borne n'est connue. On ne peut donc jamais distinguer un agent lent d'un agent \
                 arrêté.",
            provenance: "§4.2",
        },
        Terme {
            groupe: JUGEMENT,
            terme: "oracle",
            definition:
                "un juge automatique attaché à l'exécution. Il n'en existe que deux formes : une \
                 sûreté — « ceci n'arrive jamais » — ou une vivacité bornée — « ceci arrive avant \
                 telle date ». Une vivacité sans borne n'est pas représentable ici.",
            provenance: "§3.3",
        },
        Terme {
            groupe: JUGEMENT,
            terme: "borne",
            definition:
                "ce que le traité démontre d'avance, sans exécution. Elle repose sur des \
                 hypothèses ; quand un réglage les viole, elle est **effacée** et non grisée — y \
                 compris quand la mesure est meilleure qu'elle.",
            provenance: "§1.2, p. 16 (3ᵉ éd.)",
        },
        Terme {
            groupe: JUGEMENT,
            terme: "plancher d'exploration",
            definition:
                "la probabilité minimale qu'une ressource délaissée soit quand même tirée. C'est \
                 ce plancher qui empêche l'essaim d'abandonner définitivement une piste, et c'est \
                 lui qui rend la distance à l'optimum calculable.",
            provenance: "§1.2, p. 16 (3ᵉ éd.)",
        },
        Terme {
            groupe: JUGEMENT,
            terme: "effort hors dominante",
            definition:
                "la part du travail qui ne va pas à la ressource la plus servie. Trop basse, \
                 l'essaim ne cherche plus ; c'est la seconde borne du traité.",
            provenance: "§1.2, p. 16 (3ᵉ éd.)",
        },
        Terme {
            groupe: JUGEMENT,
            terme: "idempotence",
            definition:
                "propriété d'une action qu'on peut refaire sans dommage. C'est le seul recours \
                 contre l'effet dupliqué : la contrainte est reportée sur le système appelé, \
                 jamais levée.",
            provenance: "§5.1, et conclusion p. 129 (3ᵉ éd.)",
        },
        Terme {
            groupe: JUGEMENT,
            terme: "rejeu",
            definition:
                "rejouer une exécution enregistrée pour obtenir exactement la même chose. C'est \
                 aussi le nom du mode de défaillance où un agent applique deux fois un effet qui \
                 ne devait l'être qu'une.",
            provenance: "§3.3, et §5.1 pour le mode de défaillance",
        },
        Terme {
            groupe: JUGEMENT,
            terme: "cycle sans rétroaction",
            definition:
                "un cycle d'agent qui s'est déroulé sans que la trace du cycle précédent ait eu \
                 le temps de devenir lisible. L'essaim agit alors sur un milieu qui ne le reflète \
                 pas encore.",
            provenance: "nomenclature du produit — compteur du scénario B",
        },
    ]
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-V11 — aucune entrée sans provenance : un glossaire est exactement
    /// l'endroit où une définition du produit se lit comme une définition du
    /// traité.
    #[test]
    fn chaque_terme_porte_sa_provenance() {
        for t in glossaire() {
            assert!(!t.groupe.is_empty(), "{}", t.terme);
            assert!(!t.terme.is_empty());
            assert!(!t.definition.is_empty(), "{}", t.terme);
            assert!(!t.provenance.is_empty(), "{}", t.terme);
        }
    }

    /// La vue regroupe en comparant au terme précédent, sans trier : un groupe
    /// qui réapparaîtrait plus bas s'afficherait deux fois sous le même titre.
    #[test]
    fn les_groupes_sont_contigus() {
        let mut vus: Vec<&str> = Vec::new();
        let mut courant = "";
        for t in glossaire() {
            if t.groupe != courant {
                assert!(
                    !vus.contains(&t.groupe),
                    "le groupe « {} » reparaît après avoir été quitté",
                    t.groupe
                );
                vus.push(t.groupe);
                courant = t.groupe;
            }
        }
    }

    /// Les termes ne se répètent pas : deux définitions du même mot, c'est la
    /// question à laquelle le glossaire existe pour répondre, posée deux fois.
    #[test]
    fn aucun_terme_nest_defini_deux_fois() {
        let mut vus: Vec<&str> = glossaire().iter().map(|t| t.terme).collect();
        let total = vus.len();
        vus.sort_unstable();
        vus.dedup();
        assert_eq!(vus.len(), total);
    }
}
