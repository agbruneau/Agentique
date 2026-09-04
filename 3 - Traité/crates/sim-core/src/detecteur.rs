//! Le détecteur de défaillance (PD6, PD12, DT6).
//!
//! > Un détecteur ne prouve pas la mort d'un agent : il la soupçonne, à partir
//! > d'indices temporels, et il est caractérisé par sa complétude et son
//! > exactitude. (§6.1 et §7.3 du traité)
//!
//! Un seul objet paramétré, conformément à DT6, parce que les exemplaires sont
//! **comptés dans le traité** et non imaginés (PD7, règle du comptage) :
//! exclusion de l'ensemble synchronisé (§2.1, §6.1), délai de session du groupe
//! de consommation (§6.1), sondage indirect de style infectieux (§4.3, §7.3),
//! reconfiguration sur soupçon (§4.3), détection implicite du best-of-n (§5.1).
//! Cinq exemplaires : le seuil de trois est franchi, la factorisation est due.
//!
//! Ce que PD12 impose et qui se lit dans le code : le taux de fausses
//! suspicions n'est **pas** un paramètre. Il est produit par la comparaison
//! entre la latence de réponse courante et le seuil d'expiration, donc il croît
//! avec la charge. Un paramètre le rendrait invérifiable.

use crate::temps::{Duree, Instant};
use crate::ActeurId;
use std::collections::BTreeMap;

/// État d'un agent **aux yeux d'un autre** (PD12, EX-V13).
///
/// « Mort » n'est pas une observation, c'est une action : elle n'a pas de
/// variante ici. Le passage à `Retire` demande une autorisation nommée.
#[derive(Clone, Copy, PartialEq, Eq, Debug, Default)]
pub enum Etat {
    /// Rien ne permet de le soupçonner. C'est l'état par défaut.
    #[default]
    Sain,
    /// Soupçonné — ce qui n'est pas un fait, seulement le verdict d'un
    /// mécanisme qui peut se tromper (PD12).
    Suspect,
    /// Retiré par une action, et l'action porte son autorisation (EX-V13).
    Retire,
}

impl Etat {
    /// Libellé d'affichage. « mort » n'en fait pas partie, et c'est voulu.
    pub fn libelle(self) -> &'static str {
        match self {
            Etat::Sain => "sain",
            Etat::Suspect => "suspect",
            Etat::Retire => "retiré",
        }
    }
}

/// Les deux propriétés formelles, obligatoires (PD12 : « un détecteur sans ces
/// deux champs ne se construit pas »).
///
/// La complétude est ici une **borne dérivée des paramètres**, pas une
/// déclaration : le §4.3 la calcule pour les défauts documentés — un arrêt juste
/// après une sonde réussie n'est vu qu'au sondage suivant, puis exige les échecs
/// restants, plus le délai d'expiration. À période 10 s, seuil 3 et expiration
/// 1 s, cela donne 21 s à 31 s, et NF-15 exige qu'un test retrouve ce chiffre.
///
/// `#[non_exhaustive]` **ne tient pas PD12 par le type**, contrairement à ce que
/// ce commentaire affirmait. Il interdit hors de cette crate le littéral, la
/// mise à jour fonctionnelle et le filtrage exhaustif — c'est-à-dire qu'il rend
/// l'ajout d'un champ non cassant. Il n'interdit **pas** l'affectation de
/// champ : les quatre champs sont `pub`, la structure est `Copy`, et
/// [`Detecteur::proprietes`] en rend un exemplaire par valeur. Mesuré depuis une
/// crate externe, sur un détecteur ayant porté **une** suspicion, fausse :
///
/// ```text
/// (a) mesuré   : suspicions=1       fausses=1 exactitude=Some(1.0)
/// (a) fabriqué : suspicions=1000000 fausses=0 exactitude=Some(0.0)
/// ```
///
/// Ce que PD12 tient réellement, et qui est plus étroit : le détecteur ne prend
/// jamais ces nombres d'ailleurs que de [`Detecteur::sonder`], et une copie
/// falsifiée ne remonte pas dans l'objet — elle ne trompe qu'un affichage.
/// Le tenir *par le type* demanderait des champs privés et quatre accesseurs,
/// ce qui casse un appelant hors crate (`crates/sim-agents/src/pair_a_pair.rs`,
/// qui lit `p.suspicions` et `p.fausses_suspicions`) : changement d'interface,
/// hors du périmètre du banc de `sim-core`.
#[derive(Clone, Copy, Debug)]
#[non_exhaustive]
pub struct Proprietes {
    /// Délai minimal avant qu'un agent réellement arrêté soit suspecté.
    pub completude_min: Duree,
    /// Délai maximal correspondant.
    pub completude_max: Duree,
    /// Nombre de suspicions portées sur un agent qui répondait — mesuré, jamais
    /// saisi (PD12).
    pub fausses_suspicions: u64,
    /// Nombre total de suspicions portées.
    pub suspicions: u64,
}

impl Proprietes {
    /// Exactitude mesurée : fraction des suspicions qui étaient fausses. Rend
    /// `None` tant qu'aucune suspicion n'a été portée — l'absence de mesure
    /// s'affiche, elle ne se comble pas par un zéro (F1).
    pub fn exactitude(&self) -> Option<f64> {
        if self.suspicions == 0 {
            None
        } else {
            Some(self.fausses_suspicions as f64 / self.suspicions as f64)
        }
    }
}

/// Vue du détecteur sur une cible.
#[derive(Clone, Copy, Debug, Default)]
struct Vue {
    etat: Etat,
    echecs_consecutifs: u8,
    derniere_sonde: Instant,
}

/// Le détecteur paramétré.
#[derive(Clone, Debug)]
pub struct Detecteur {
    /// Période entre deux sondes.
    pub periode: Duree,
    /// Délai au-delà duquel une réponse est comptée comme absente. C'est ce
    /// seuil, confronté à la latence **produite** par la charge, qui fabrique
    /// les fausses suspicions.
    pub expiration: Duree,
    /// Nombre d'échecs consécutifs avant suspicion.
    pub seuil: u8,
    /// Taille du sous-groupe de sondage indirect. Zéro vaut « inactif », et
    /// `resume()` l'écrit ainsi plutôt que d'afficher un nombre (PD6).
    ///
    /// Le coût qu'il annonce — au plus 2 + 4s messages et 3 tours par cycle de
    /// suspicion — est celui d'EX-A23. **Ce détecteur ne l'applique pas
    /// lui-même** : la mécanique infectieuse vit dans
    /// `sim_agents::soupcon::DetecteurInfectieux`, qui tient ses propres
    /// compteurs. Ce champ règle la forme de l'objet fixée au §5.1 du PRD, pas un
    /// comportement de `sim-core`.
    pub sondage_indirect: u8,
    /// Extension par suspicion propagée. Même réserve : réglable ici,
    /// appliquée dans `sim-agents`.
    pub suspicion: bool,

    vues: BTreeMap<u32, Vue>,
    proprietes: Proprietes,
    /// Messages émis par le détecteur — 2 par sonde, aller et retour (EX-A23).
    messages: u64,
}

impl Detecteur {
    /// Construit un détecteur. Les trois paramètres actifs sont obligatoires :
    /// il n'existe pas de constructeur par défaut, parce qu'un détecteur sans
    /// seuil ni expiration n'a ni complétude ni exactitude (PD12).
    ///
    /// # Erreurs
    ///
    /// Deux réglages sont **refusés à l'appelant**, et non écrêtés : `seuil`
    /// nul — un détecteur qui suspecte sans indice n'a pas d'exactitude à
    /// mesurer, et la complétude dérivée du §7.3 du traité compte `seuil − 1`
    /// intervalles —, et une `expiration` qui n'est pas strictement plus courte
    /// que `periode`, auquel cas deux sondes se chevauchent et le compte
    /// d'échecs consécutifs cesse de vouloir dire quoi que ce soit (§4.3 du
    /// traité). C'était un `assert!` jusqu'au banc ; la clause 4 du §7 de
    /// `docs/SPEC.md` — « une configuration invalide est un refus rendu à
    /// l'appelant, jamais un abandon » — est la même que celle sous laquelle
    /// `sim_agents::soupcon::DetecteurInfectieux::completude` et
    /// `sim_agents::cycle_de_vie::retirer` refusent le seuil nul, et les trois
    /// dérivent le même encadrement de 21 à 31 s.
    pub fn nouveau(periode: Duree, expiration: Duree, seuil: u8) -> Result<Detecteur, String> {
        if seuil == 0 {
            return Err(
                "seuil d'échec nul refusé : un détecteur qui suspecte sans indice n'a \
                        aucune exactitude à mesurer, et l'encadrement de complétude compte les \
                        intervalles entre `seuil` échecs consécutifs (PD12)."
                    .to_string(),
            );
        }
        if expiration >= periode {
            return Err(format!(
                "expiration {} ≥ période {} refusée : le §4.3 du traité veut l'expiration \
                 strictement plus courte que la période, sans quoi deux sondes se chevauchent et \
                 le compte d'échecs consécutifs ne veut plus rien dire.",
                expiration.0, periode.0
            ));
        }
        Ok(Detecteur {
            periode,
            expiration,
            seuil,
            sondage_indirect: 0,
            suspicion: false,
            vues: BTreeMap::new(),
            proprietes: Proprietes {
                completude_min: Duree(0),
                completude_max: Duree(0),
                fausses_suspicions: 0,
                suspicions: 0,
            },
            messages: 0,
        })
    }

    /// Les défauts documentés du §4.3 / §6.1 du traité : `periodSeconds 10`,
    /// `timeoutSeconds 1`, `failureThreshold 3`. Les valeurs sont périssables
    /// (annexe B) ; leur **effet** est le mécanisme.
    ///
    /// # Erreurs
    ///
    /// Celles de [`Detecteur::nouveau`] : à `tics_par_seconde` nul, période et
    /// expiration valent toutes deux zéro et le réglage est refusé.
    pub fn defauts_documentes(tics_par_seconde: u64) -> Result<Detecteur, String> {
        Detecteur::nouveau(Duree(10 * tics_par_seconde), Duree(tics_par_seconde), 3)
    }

    /// Complétude dérivée : bornes du délai de détection d'un agent réellement
    /// arrêté (§4.3, EX-A23).
    ///
    /// Borne basse : l'arrêt survient juste avant une sonde, il reste les
    /// `seuil − 1` échecs suivants, plus l'expiration du dernier.
    /// Borne haute : l'arrêt survient juste après une sonde réussie, il faut
    /// attendre une période entière de plus.
    ///
    /// Le produit sature : `periode` et `seuil` sont publics et le profil
    /// release du dépôt ne pose pas `overflow-checks`. Sans cela, `periode`
    /// = 2⁶³ et `seuil` = 3 rendaient une borne basse de **1 tic** au lieu de
    /// 2⁶⁴ — un détecteur annoncé instantané là où il est le plus lent.
    pub fn completude(&self) -> (Duree, Duree) {
        let echecs_restants = Duree(
            self.periode
                .0
                .saturating_mul(u64::from(self.seuil.saturating_sub(1))),
        );
        let min = echecs_restants + self.expiration;
        let max = min + self.periode;
        (min, max)
    }

    /// Les deux propriétés formelles, à afficher avec le détecteur (PD12).
    pub fn proprietes(&self) -> Proprietes {
        let (min, max) = self.completude();
        Proprietes {
            completude_min: min,
            completude_max: max,
            ..self.proprietes
        }
    }

    /// État courant d'une cible aux yeux du détecteur.
    pub fn etat(&self, cible: ActeurId) -> Etat {
        self.vues.get(&cible.0).map(|v| v.etat).unwrap_or_default()
    }

    /// Nombre de messages émis par le détecteur, compté à part du trafic
    /// ordinaire (EX-M13 : le coût de coordination ne se mêle pas au débit).
    pub fn messages(&self) -> u64 {
        self.messages
    }

    /// Exécute une sonde.
    ///
    /// `vivant` et `latence` sont fournis par le moteur, qui les connaît : le
    /// détecteur, lui, ne voit qu'un délai. C'est précisément l'écart entre les
    /// deux qui produit une fausse suspicion, et le simulateur est le seul à
    /// pouvoir la compter — l'interface doit dire qu'aucun agent ne dispose de
    /// cette information (§8.3 du PRD).
    ///
    /// Rend l'état après la sonde.
    pub fn sonder(
        &mut self,
        cible: ActeurId,
        vivant: bool,
        latence: Duree,
        maintenant: Instant,
    ) -> Etat {
        self.messages += 2; // aller et retour (EX-A23, coût nominal)
        let seuil = self.seuil;
        let expiration = self.expiration;
        let vue = self.vues.entry(cible.0).or_default();
        vue.derniere_sonde = maintenant;

        if vue.etat == Etat::Retire {
            return Etat::Retire;
        }

        // La sonde échoue si l'agent ne répond pas — ou s'il répond trop tard.
        // Le second cas est celui du §7.3 : un agent saturé mais vivant est
        // classé défaillant, et c'est ce qui rend le taux de fausses suspicions
        // fonction croissante de la charge.
        let echec = !vivant || latence > expiration;
        if echec {
            vue.echecs_consecutifs = vue.echecs_consecutifs.saturating_add(1);
            if vue.echecs_consecutifs >= seuil && vue.etat == Etat::Sain {
                vue.etat = Etat::Suspect;
                self.proprietes.suspicions += 1;
                if vivant {
                    self.proprietes.fausses_suspicions += 1;
                }
            }
        } else {
            // Un agent qui répond redevient sain : le détecteur peut se
            // dédire, et c'est ce qui le distingue d'un verdict.
            vue.echecs_consecutifs = 0;
            vue.etat = Etat::Sain;
        }
        vue.etat
    }

    /// Retire une cible. PD12 : le passage de « suspect » à « retiré » **nomme
    /// l'action qui l'a produit et son autorisation** ; il n'y a pas de
    /// transition automatique depuis la suspicion.
    pub fn retirer(&mut self, cible: ActeurId, action: &str, autorisation: &str) -> String {
        self.vues.entry(cible.0).or_default().etat = Etat::Retire;
        format!(
            "acteur {} retiré par « {action} », autorisé par {autorisation}",
            cible.0
        )
    }

    /// Affichage du détecteur (PD6 : ses réglages sont montrés au même rang que
    /// le taux d'omission ; RQ7 : un détecteur enfoui rend la moitié des modes
    /// de défaillance inexplicables).
    pub fn resume(&self, unite: &str) -> Vec<(&'static str, String)> {
        let p = self.proprietes();
        vec![
            ("période", format!("{} {unite}", self.periode.0)),
            ("expiration", format!("{} {unite}", self.expiration.0)),
            ("seuil", format!("{} échecs consécutifs", self.seuil)),
            (
                "sondage indirect",
                match self.sondage_indirect {
                    0 => "inactif — aucun pair sondé".to_string(),
                    s => format!("{s} pairs — au plus {} messages, 3 tours (EX-A23)", 2 + 4 * u32::from(s)),
                },
            ),
            (
                "extension par suspicion",
                if self.suspicion {
                    "active — le soupçon se propage (EX-A23)".to_string()
                } else {
                    "inactive".to_string()
                },
            ),
            (
                "complétude",
                format!("détection entre {} et {} {unite}", p.completude_min.0, p.completude_max.0),
            ),
            (
                "exactitude",
                match p.exactitude() {
                    Some(x) => format!(
                        "{:.3} de fausses suspicions sur {} portées — mesurée, jamais saisie (PD12)",
                        x, p.suspicions
                    ),
                    None => "aucune suspicion portée — provenance absente (F1)".to_string(),
                },
            ),
            ("messages émis", format!("{}", self.messages)),
        ]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// NF-15 — le chiffre du traité doit être **retrouvé**, pas cité :
    /// « détection entre 21 s et 31 s » (§4.3, EX-A23), à `periodSeconds 10`,
    /// `timeoutSeconds 1`, `failureThreshold 3`.
    #[test]
    fn la_completude_retrouve_les_21_a_31_secondes() {
        // Granularité milliseconde : 1 000 tics par seconde.
        let d = Detecteur::defauts_documentes(1_000).expect("réglage documenté");
        let (min, max) = d.completude();
        assert_eq!(min, Duree(21_000), "borne basse en ms");
        assert_eq!(max, Duree(31_000), "borne haute en ms");
    }

    /// Le produit `période × (seuil − 1)` sature. Deux champs publics et un
    /// profil release sans `overflow-checks` : l'enroulement annonçait une
    /// détection en **1 tic** sur le détecteur le plus lent représentable.
    #[test]
    fn la_completude_sature_au_lieu_de_senrouler() {
        let d = Detecteur::nouveau(Duree(1u64 << 63), Duree(1), 3).expect("réglage valide");
        let (min, max) = d.completude();
        assert_eq!(min, Duree(u64::MAX), "2⁶³ × 2 sature au lieu de valoir 0");
        assert_eq!(max, Duree(u64::MAX));
    }

    /// PD12 — un agent vivant mais lent est suspecté. C'est l'énoncé du §7.3 :
    /// le taux de fausses suspicions est une fonction croissante de la charge,
    /// et il est ici **produit**, jamais paramétré.
    #[test]
    fn un_agent_vivant_mais_lent_devient_suspect() {
        let mut d = Detecteur::nouveau(Duree(10), Duree(1), 3).expect("réglage valide");
        let cible = ActeurId(0);
        for i in 0..3 {
            d.sonder(cible, true, Duree(5), Instant(i * 10));
        }
        assert_eq!(d.etat(cible), Etat::Suspect);
        let p = d.proprietes();
        assert_eq!(p.suspicions, 1);
        assert_eq!(
            p.fausses_suspicions, 1,
            "l'agent répondait : la suspicion est fausse"
        );
        assert_eq!(p.exactitude(), Some(1.0));
    }

    #[test]
    fn un_agent_rapide_reste_sain() {
        let mut d = Detecteur::nouveau(Duree(10), Duree(5), 3).expect("réglage valide");
        let cible = ActeurId(1);
        for i in 0..20 {
            d.sonder(cible, true, Duree(1), Instant(i * 10));
        }
        assert_eq!(d.etat(cible), Etat::Sain);
        assert_eq!(d.proprietes().suspicions, 0);
        assert_eq!(
            d.proprietes().exactitude(),
            None,
            "aucune mesure : rien à afficher"
        );
    }

    /// La suspicion se dédit : un agent qui répond de nouveau redevient sain.
    /// Sans cela, le détecteur rendrait un verdict et non un soupçon.
    #[test]
    fn le_detecteur_se_dedit() {
        let mut d = Detecteur::nouveau(Duree(10), Duree(1), 2).expect("réglage valide");
        let cible = ActeurId(2);
        d.sonder(cible, false, Duree(0), Instant(0));
        d.sonder(cible, false, Duree(0), Instant(10));
        assert_eq!(d.etat(cible), Etat::Suspect);
        d.sonder(cible, true, Duree(0), Instant(20));
        assert_eq!(d.etat(cible), Etat::Sain);
    }

    /// PD12 — « mort » n'est pas une observation, c'est une action. Le retrait
    /// nomme son autorisation.
    #[test]
    fn le_retrait_nomme_son_autorisation() {
        let mut d = Detecteur::nouveau(Duree(10), Duree(1), 2).expect("réglage valide");
        let cible = ActeurId(3);
        d.sonder(cible, false, Duree(0), Instant(0));
        d.sonder(cible, false, Duree(0), Instant(10));
        let ligne = d.retirer(
            cible,
            "reconfiguration sur soupçon",
            "budget de perturbation",
        );
        assert_eq!(d.etat(cible), Etat::Retire);
        assert!(ligne.contains("budget de perturbation"), "{ligne}");
        // Un retiré ne redevient pas sain sur une sonde réussie : le retrait est
        // une décision, pas un état observé.
        d.sonder(cible, true, Duree(0), Instant(20));
        assert_eq!(d.etat(cible), Etat::Retire);
    }

    #[test]
    fn le_detecteur_refuse_une_expiration_plus_longue_que_sa_periode() {
        let r = std::panic::catch_unwind(|| {
            Detecteur::nouveau(Duree(1), Duree(10), 3).expect("réglage valide")
        });
        assert!(r.is_err());
    }

    /// PD6 dans les deux sens : « inactif » quand le réglage est nul, la valeur
    /// réelle quand il ne l'est pas. Afficher « inactif » sur un champ réglé
    /// est le mensonge symétrique de celui que PD6 vise, et c'est celui que
    /// le banc a trouvé installé.
    #[test]
    fn le_resume_suit_le_reglage_au_lieu_de_le_taire() {
        let ligne = |d: &Detecteur, cle: &str| {
            d.resume("ms")
                .into_iter()
                .find(|(k, _)| *k == cle)
                .map(|(_, v)| v)
                .unwrap()
        };

        let inactif = Detecteur::defauts_documentes(1_000).expect("réglage documenté");
        assert_eq!(inactif.sondage_indirect, 0);
        assert!(ligne(&inactif, "sondage indirect").contains("inactif"));
        assert!(ligne(&inactif, "extension par suspicion").contains("inactive"));

        let mut regle = Detecteur::defauts_documentes(1_000).expect("réglage documenté");
        regle.sondage_indirect = 3;
        regle.suspicion = true;
        let s = ligne(&regle, "sondage indirect");
        assert!(s.contains('3'), "{s}");
        assert!(s.contains("14"), "2 + 4×3 = 14 messages : {s}");
        assert!(
            !s.contains("inactif"),
            "un réglage posé ne s'affiche pas « inactif » : {s}"
        );
        assert!(ligne(&regle, "extension par suspicion").contains("active"));
    }
}
