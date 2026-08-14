//! Réplication ISR(k, m), et les deux invariants qu'elle porte (EX-M05 à
//! EX-M08, EX-M14, EX-M15, EX-M23).
//!
//! > Le nombre de disparitions auquel r₂ survit n'est pas k − 1 = 2, il est
//! > m − 1 = 1. (§2.1, p. 22)
//!
//! Deux invariants **distincts**, et le produit ne les confond jamais :
//!
//! - **R1, sûreté** — tout enregistrement accusé au producteur est présent chez
//!   tout meneur ultérieur de la partition.
//! - **R2, visibilité** — un enregistrement n'est lisible qu'après réplication
//!   à tout l'ensemble synchronisé.
//!
//! Ce que le §6.1 ajoute et qui est le sujet du scénario D : **la perte de R1
//! est muette**. Avec `min.insync.replicas = 1`, l'ISR peut se réduire au seul
//! meneur pendant que les producteurs continuent de recevoir leurs accusés. La
//! tolérance passe de f à 0 sans qu'aucune erreur ne soit émise, et le seul
//! affichage qui le trahit est la largeur d'accusé (EX-V15).

use sim_core::oracle::{Oracle, Registre};
use sim_core::registre::RegistreHypotheses;
use sim_core::temps::{Duree, Instant};

/// R1 — sûreté : un enregistrement accusé survit à toute élection ultérieure.
/// C'est l'invariant qui tombe **muettement** quand `m` vaut 1.
pub const R1: &str = "R1 — tout enregistrement accusé est présent chez tout meneur ultérieur";
/// R2 — visibilité : ce qui est lisible a été répliqué à tout l'ISR courant.
pub const R2: &str = "R2 — un enregistrement lisible a été répliqué à tout l'ISR";

/// Réglage du temporisateur d'appartenance à l'ISR, tel qu'il est nommé dans la
/// documentation d'origine. Sa valeur est périssable (annexe B) ; son **effet**
/// — l'exclusion d'un suiveur vivant sous charge — est le mécanisme.
pub const REGLAGE_LAG: &str = "replica.lag.time.max.ms";

/// Une réplique de la partition.
///
/// Le contenu n'est pas dupliqué : une réplique détient les enregistrements
/// `[0, fin)` du journal du meneur. C'est suffisant pour R1, R2 et la
/// troncature, et cela évite k copies d'un journal qui peut compter des
/// centaines de milliers d'entrées.
#[derive(Clone, Copy, Debug)]
pub struct Replique {
    /// Identifiant de la réplique, stable pour toute l'exécution.
    pub id: u32,
    /// Décalage de fin de journal.
    pub fin: u64,
    /// Fausse après un arrêt. Distincte du retrait de l'ISR : un suiveur retiré
    /// pour retard est **vivant** (EX-M07).
    pub vivante: bool,
    /// Instant du dernier rattrapage du meneur.
    pub derniere_synchro: Instant,
}

/// Pourquoi une écriture a été refusée.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Refus {
    /// |ISR| < m : la partition cesse d'accuser. C'est le **seul** cas où le
    /// producteur apprend quelque chose ; en deçà, la dégradation est muette.
    SousLeSeuil {
        /// Taille de l'ISR au moment du refus.
        isr: u32,
        /// Le seuil `min.insync.replicas` en vigueur.
        m: u32,
    },
    /// Aucun meneur vivant.
    SansMeneur,
}

/// Un enregistrement accusé au producteur, avec la largeur à laquelle il l'a
/// été. C'est cette largeur qui décide de sa survie : **w − 1 disparitions**
/// (§2.1), et non k − 1.
#[derive(Clone, Copy, Debug)]
pub struct Accuse {
    /// Décalage de l'enregistrement accusé.
    pub decalage: u64,
    /// Nombre de répliques qui le détenaient au moment de l'accusé. C'est
    /// **w**, et sa survie tient à `w − 1`, jamais à `k − 1`.
    pub largeur: u32,
}

/// La partition répliquée.
#[derive(Clone, Debug)]
pub struct Isr {
    /// Répliques assignées.
    pub k: u32,
    /// `min.insync.replicas` — seuil en deçà duquel la partition cesse
    /// d'accuser. **Ce n'est pas le nombre d'accusés attendus** : une écriture
    /// attend tout l'ISR courant (EX-M05).
    pub m: u32,
    /// Meneur courant, ou `None` après une panne et avant l'élection.
    pub meneur: Option<u32>,
    /// Les `k` répliques assignées, meneur compris.
    pub repliques: Vec<Replique>,
    /// Membres de l'ensemble synchronisé, ordonnés — jamais une table de
    /// hachage (PD1).
    isr: Vec<u32>,
    /// **R2** — borne de visibilité. Les enregistrements de décalage inférieur
    /// sont lisibles ; les autres ne le sont pas, même écrits.
    pub borne_visibilite: u64,
    /// Décalage de fin du journal du meneur.
    pub fin_meneur: u64,
    accuses: Vec<Accuse>,
    /// Temporisateur d'exclusion pour retard (EX-M14).
    pub temporisateur: Duree,
    /// EX-M08 — élire un non-membre de l'ISR est une **option**, avec ses deux
    /// conséquences simulées.
    pub election_hors_isr: bool,
    /// Compteur de **pannes réelles**. Un retrait pour retard ne l'incrémente
    /// jamais (EX-M07) : c'est ce qui rend la chute de R1 lisible.
    pub pannes: u32,
    /// Retraits pour retard, comptés à part.
    pub retraits_pour_retard: u32,
    /// Enregistrements détruits par troncature après une élection hors ISR.
    pub tronques: u64,
}

impl Isr {
    /// Construit une partition répliquée. Les k répliques démarrent
    /// synchronisées et l'ISR les contient toutes.
    pub fn nouvelle(k: u32, m: u32, temporisateur: Duree) -> Isr {
        assert!(k >= 1, "k ≥ 1");
        assert!(m >= 1 && m <= k, "1 ≤ m ≤ k");
        Isr {
            k,
            m,
            meneur: Some(0),
            repliques: (0..k)
                .map(|id| Replique {
                    id,
                    fin: 0,
                    vivante: true,
                    derniere_synchro: Instant(0),
                })
                .collect(),
            isr: (0..k).collect(),
            borne_visibilite: 0,
            fin_meneur: 0,
            accuses: Vec::new(),
            temporisateur,
            election_hors_isr: false,
            pannes: 0,
            retraits_pour_retard: 0,
            tronques: 0,
        }
    }

    /// Déclare le temporisateur au registre des hypothèses fortes (EX-C12).
    ///
    /// C'est une hypothèse **plus forte que le synchronisme partiel** : elle
    /// affirme une borne connue là où le modèle n'en donne pas, et le §6.1 dit
    /// que c'est elle qui casse en premier sous charge.
    pub fn declarer_hypotheses(&self, registre: &mut RegistreHypotheses) {
        registre.declarer(
            REGLAGE_LAG,
            self.temporisateur,
            "§6.1, tableau 17",
            "un suiveur sain rattrape le meneur en moins du temporisateur",
        );
    }

    /// Arme R1 et R2 comme oracles de sûreté. NF-11 veut les invariants du
    /// milieu armés en permanence dans les tests.
    ///
    /// **R2 n'a pas de prédicat, et c'est voulu** : il tient par construction de
    /// `Isr::avancer_visibilite`, qui n'avance la borne que jusqu'au minimum
    /// des `fin` de l'ISR et refuse d'avancer sous `m`. Aucun chemin du produit
    /// ne peut donc rendre lisible un enregistrement non répliqué à tout l'ISR,
    /// et un prédicat qui le vérifierait vérifierait la ligne qui précède. C'est
    /// la même situation que M2 et M3 côté journal — l'oracle reste armé pour
    /// que sa ligne figure au catalogue, non pour qu'il se déclenche.
    pub fn armer_oracles(&self, registre: &mut Registre) {
        registre.armer(Oracle::surete(R1, "§2.1, p. 21 ; §6.1"));
        registre.armer(Oracle::surete(R2, "§6.1"));
    }

    /// Membres de l'ensemble synchronisé, ordonnés.
    pub fn isr(&self) -> &[u32] {
        &self.isr
    }

    /// |ISR| — à afficher en permanence à côté de `m` (EX-V15).
    pub fn taille_isr(&self) -> u32 {
        self.isr.len() as u32
    }

    /// **Marge d'accusé** — nombre de retraits que la partition supporte avant
    /// de cesser d'accuser.
    ///
    /// Grandeur **dérivée du produit** et étiquetée comme telle : le traité ne
    /// l'écrit pas (EX-M15).
    pub fn marge_daccuse(&self) -> i64 {
        self.taille_isr() as i64 - self.m as i64
    }

    /// Largeur d'accusé du dernier enregistrement validé (EX-V15).
    pub fn derniere_largeur(&self) -> Option<u32> {
        self.accuses.last().map(|a| a.largeur)
    }

    /// Les deux tolérances, chacune avec sa provenance (EX-M15). Elles ne se
    /// mélangent jamais et ne s'additionnent pas.
    pub fn tolerances(&self) -> (Option<u32>, u32) {
        (
            // Un enregistrement accusé à largeur w survit à w − 1 disparitions.
            self.derniere_largeur().map(|w| w.saturating_sub(1)),
            // R1 tient tant qu'un réplica de l'ISR survit.
            self.taille_isr().saturating_sub(1),
        )
    }

    fn replique_mut(&mut self, id: u32) -> Option<&mut Replique> {
        self.repliques.iter_mut().find(|r| r.id == id)
    }

    fn replique(&self, id: u32) -> Option<&Replique> {
        self.repliques.iter().find(|r| r.id == id)
    }

    /// Le meneur reçoit une écriture. Rend le décalage attribué, ou le refus.
    ///
    /// Le refus n'existe qu'au-dessous du seuil m. **C'est la seule information
    /// que le producteur reçoit**, et c'est pourquoi `m = 1` rend la perte de
    /// R1 muette : il n'y a plus de seuil à franchir.
    pub fn ecrire(&mut self) -> Result<u64, Refus> {
        let meneur = self.meneur.ok_or(Refus::SansMeneur)?;
        if self.taille_isr() < self.m {
            return Err(Refus::SousLeSeuil {
                isr: self.taille_isr(),
                m: self.m,
            });
        }
        let decalage = self.fin_meneur;
        self.fin_meneur += 1;
        let fin_meneur = self.fin_meneur;
        if let Some(r) = self.replique_mut(meneur) {
            r.fin = fin_meneur;
        }
        Ok(decalage)
    }

    /// Un suiveur rattrape le meneur jusqu'à `fin`.
    ///
    /// Quand **toutes** les répliques de l'ISR ont rattrapé un décalage,
    /// celui-ci est accusé au producteur à la largeur `|ISR|`, et la borne de
    /// visibilité avance : c'est R2.
    pub fn repliquer(&mut self, id: u32, fin: u64, maintenant: Instant) {
        let fin_meneur = self.fin_meneur;
        if let Some(r) = self.replique_mut(id) {
            if !r.vivante {
                return;
            }
            r.fin = r.fin.max(fin.min(fin_meneur));
            if r.fin >= fin_meneur {
                r.derniere_synchro = maintenant;
            }
        }
        self.avancer_visibilite();
    }

    /// R2 — la borne n'avance qu'après réplication à **tout** l'ISR.
    ///
    /// Et pas en dessous de `m` : un ISR retombé sous le seuil cesse d'accuser,
    /// ce qui est le seul signal que le producteur reçoive (`Refus::SousLeSeuil`).
    /// Sans cette garde, un retrait pour retard faisait avancer la borne sur
    /// l'ISR restant et accusait à une largeur inférieure à `m` — la même
    /// écriture, soumise une microseconde plus tard, aurait été refusée.
    fn avancer_visibilite(&mut self) {
        let largeur = self.taille_isr();
        if largeur < self.m {
            return;
        }
        let nouvelle = self
            .isr
            .iter()
            .filter_map(|id| self.replique(*id).map(|r| r.fin))
            .min()
            .unwrap_or(0);
        while self.borne_visibilite < nouvelle {
            self.accuses.push(Accuse {
                decalage: self.borne_visibilite,
                largeur,
            });
            self.borne_visibilite += 1;
        }
    }

    /// EX-M14 — l'appartenance à l'ISR est décidée par un **temporisateur**, pas
    /// par un accord.
    ///
    /// Sous saturation, l'exclusion frappe des suiveurs **vivants** : c'est le
    /// démenti de l'hypothèse, et le registre l'enregistre (EX-C12).
    pub fn avancer(&mut self, maintenant: Instant, hypotheses: &mut RegistreHypotheses) {
        let meneur = self.meneur;
        let fin_meneur = self.fin_meneur;
        let temporisateur = self.temporisateur;
        let mut a_retirer = Vec::new();

        for id in self.isr.clone() {
            if Some(id) == meneur {
                continue;
            }
            let r = match self.replique(id) {
                Some(r) => *r,
                None => continue,
            };
            if r.fin >= fin_meneur {
                continue;
            }
            // Le suiveur est en retard. L'hypothèse — « il rattrape en moins du
            // temporisateur » — est mise à l'épreuve à chaque évaluation.
            let en_retard_depuis = maintenant - r.derniere_synchro;
            let tenue = en_retard_depuis <= temporisateur;
            hypotheses.eprouver(REGLAGE_LAG, tenue);
            if !tenue {
                a_retirer.push((id, r.vivante));
            }
        }

        for (id, vivante) in a_retirer {
            self.isr.retain(|x| *x != id);
            if vivante {
                // EX-M07 — retrait pour retard : le compteur de **pannes** ne
                // bouge pas. Confondre les deux rendrait la chute de R1
                // inexplicable.
                self.retraits_pour_retard += 1;
            }
        }
        self.avancer_visibilite();
    }

    /// Retire une réplique de l'ISR pour retard, sans attendre le
    /// temporisateur. Sert le rejeu pas à pas du scénario D.
    pub fn retirer_pour_retard(&mut self, id: u32) {
        if self.isr.contains(&id) {
            self.isr.retain(|x| *x != id);
            self.retraits_pour_retard += 1;
        }
        self.avancer_visibilite();
    }

    /// Arrêt d'une réplique — une **panne réelle**, comptée comme telle.
    pub fn arreter(&mut self, id: u32) {
        if let Some(r) = self.replique_mut(id) {
            if r.vivante {
                r.vivante = false;
                self.pannes += 1;
            }
        }
        self.isr.retain(|x| *x != id);
        if self.meneur == Some(id) {
            self.meneur = None;
        }
        self.avancer_visibilite();
    }

    /// Élit un meneur. Rend son identifiant, ou `None` si aucun n'est éligible.
    ///
    /// EX-M05 — le meneur est élu **parmi les membres de l'ensemble
    /// synchronisé**. EX-M08 — élire un non-membre est une option, et ses deux
    /// conséquences sont simulées : troncature des journaux, destruction de
    /// l'enregistrement chez ses détenteurs.
    pub fn elire(&mut self) -> Option<u32> {
        // D'abord dans l'ISR : c'est le régime nominal, et il préserve R1.
        if let Some(id) = self
            .isr
            .iter()
            .copied()
            .find(|id| self.replique(*id).map(|r| r.vivante).unwrap_or(false))
        {
            self.meneur = Some(id);
            self.fin_meneur = self.replique(id).map(|r| r.fin).unwrap_or(0);
            return Some(id);
        }
        if !self.election_hors_isr {
            // Attendre le retour d'un membre : R1 est préservée, et
            // l'indisponibilité est **non bornée** — jamais « grande ».
            return None;
        }
        // Élection d'un non-membre : le nouveau meneur impose sa fin de
        // journal, et tout ce qui la dépasse est détruit chez ses détenteurs.
        let candidat = self
            .repliques
            .iter()
            .filter(|r| r.vivante)
            .max_by_key(|r| r.fin)
            .map(|r| (r.id, r.fin))?;
        let (id, fin) = candidat;
        self.tronques += self.fin_meneur.saturating_sub(fin);
        self.meneur = Some(id);
        self.fin_meneur = fin;
        self.borne_visibilite = self.borne_visibilite.min(fin);
        for r in &mut self.repliques {
            r.fin = r.fin.min(fin);
        }
        // **|ISR| n'est donc pas monotone décroissante.** Le temporisateur ne
        // décide que du retrait, mais EX-M08 réinitialise l'ISR au nouveau
        // meneur : si les retraits l'avaient vidé, |ISR| repasse de 0 à 1, et
        // c'est ce que le scénario D parcourt à `Choix::ElireHorsIsr`. La
        // monotonie ne vaut donc **qu'hors élection hors ISR**, et
        // `crate::hors_perimetre()` le dit ainsi.
        self.isr = vec![id];
        Some(id)
    }

    /// EX-M06 — l'oracle R1. Sa violation est un **résultat attendu** du
    /// scénario D, pas un défaut du simulateur.
    pub fn verifier_r1(&self, registre: &mut Registre, maintenant: Instant) {
        let meneur = match self.meneur {
            Some(m) => m,
            None => return, // Sans meneur, il n'y a pas de « meneur ultérieur ».
        };
        let fin = self.replique(meneur).map(|r| r.fin).unwrap_or(0);
        for a in &self.accuses {
            if a.decalage >= fin {
                registre.violer(
                    R1,
                    maintenant,
                    format!(
                        "enregistrement {} accusé à largeur {} absent du meneur {meneur} \
                         (fin de journal {fin}) — il survivait à {} disparition(s), il y en a eu \
                         {} et {} retrait(s) pour retard",
                        a.decalage,
                        a.largeur,
                        a.largeur.saturating_sub(1),
                        self.pannes,
                        self.retraits_pour_retard
                    ),
                );
                return;
            }
        }
    }

    /// EX-V15 — les trois grandeurs affichées côte à côte, **sans jamais être
    /// additionnées**. C'est le seul affichage qui trahit la perte muette de R1.
    pub fn affichage_v15(&self) -> Vec<(&'static str, String)> {
        let (tol_largeur, tol_isr) = self.tolerances();
        vec![
            ("|ISR| courant", format!("{}", self.taille_isr())),
            ("m (min.insync.replicas)", format!("{}", self.m)),
            (
                "largeur d'accusé du dernier validé",
                match self.derniere_largeur() {
                    Some(w) => format!("{w}"),
                    None => "aucun enregistrement validé".to_string(),
                },
            ),
            (
                "marge d'accusé |ISR| − m",
                format!("{} — grandeur dérivée du produit", self.marge_daccuse()),
            ),
            (
                "survit à (largeur − 1)",
                match tol_largeur {
                    Some(t) => format!("{t} disparition(s) — §2.1"),
                    None => "—".to_string(),
                },
            ),
            (
                "R1 tient tant que (|ISR| − 1)",
                format!("{tol_isr} disparition(s) — §6.1"),
            ),
            ("pannes réelles", format!("{}", self.pannes)),
            (
                "retraits pour retard",
                format!("{} — jamais comptés comme pannes (EX-M07)", self.retraits_pour_retard),
            ),
        ]
    }

    /// EX-M15 — l'avertissement que le protocole n'émet pas.
    ///
    /// > Avec `min.insync.replicas = 1`, l'ISR peut se réduire au seul meneur
    /// > pendant que les producteurs reçoivent toujours leurs accusés : la
    /// > tolérance passe de f à 0 **sans qu'aucune erreur ne soit émise**.
    ///
    /// C'est le seul endroit du produit où l'affichage vaut mieux que le
    /// protocole, et le scénario D est bâti autour.
    pub fn perte_muette(&self) -> Option<String> {
        let taille = self.taille_isr();
        if self.m == 1 && taille <= 1 {
            return Some(format!(
                "ISR réduit à {taille} réplique avec m = 1 : la tolérance est tombée à 0 \
                 disparition, et aucune erreur n'est émise au producteur. Seule la largeur \
                 d'accusé le trahit (§6.1, EX-M15)."
            ));
        }
        // `m == 1` est bien la seule condition, et c'est ce qui fait la thèse du
        // scénario D : sous m > 1, l'ISR retombé sous le seuil cesse d'accuser
        // (`avancer_visibilite`) et refuse l'écriture suivante
        // (`Refus::SousLeSeuil`). Le producteur est informé, donc rien n'est
        // muet. C'est `min.insync.replicas = 1` qui supprime les deux signaux à
        // la fois.
        None
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn isr() -> (Isr, Registre, RegistreHypotheses) {
        let i = Isr::nouvelle(3, 2, Duree(30));
        let mut o = Registre::nouveau();
        let mut h = RegistreHypotheses::nouveau();
        i.armer_oracles(&mut o);
        i.declarer_hypotheses(&mut h);
        (i, o, h)
    }

    /// EX-M05 — une écriture est accusée quand **tout l'ISR** l'a reçue, et sa
    /// largeur est la taille de l'ISR à cet instant.
    #[test]
    fn une_ecriture_est_accusee_a_la_largeur_de_lisr() {
        let (mut i, _, _) = isr();
        i.ecrire().unwrap();
        // Le meneur seul ne suffit pas : R2 n'avance pas.
        assert_eq!(i.borne_visibilite, 0, "R2 n'avance qu'après tout l'ISR");
        i.repliquer(1, 1, Instant(1));
        assert_eq!(i.borne_visibilite, 0, "il manque encore une réplique");
        i.repliquer(2, 1, Instant(1));
        assert_eq!(i.borne_visibilite, 1);
        assert_eq!(i.derniere_largeur(), Some(3));
    }

    /// EX-M15 — les deux tolérances ont deux provenances et ne se confondent
    /// pas : w − 1 pour l'enregistrement (§2.1), |ISR| − 1 pour R1 (§6.1).
    #[test]
    fn les_deux_tolerances_restent_distinctes() {
        let (mut i, _, _) = isr();
        i.ecrire().unwrap();
        i.repliquer(1, 1, Instant(1));
        i.repliquer(2, 1, Instant(1));
        i.retirer_pour_retard(2);
        let (par_largeur, par_isr) = i.tolerances();
        assert_eq!(par_largeur, Some(2), "accusé à largeur 3 → survit à 2");
        assert_eq!(par_isr, 1, "|ISR| = 2 → R1 tient tant qu'une survit");
    }

    /// NF-16 — l'hypothèse du temporisateur est **rendue fausse** et le mode de
    /// défaillance annoncé se produit : l'exclusion frappe un suiveur **vivant**.
    ///
    /// C'est l'énoncé du §6.1 : c'est cette hypothèse qui casse en premier sous
    /// charge, et le registre en tient le compte.
    #[test]
    fn nf16_sous_charge_lexclusion_frappe_un_suiveur_vivant() {
        let (mut i, _, mut h) = isr();
        i.ecrire().unwrap();
        i.repliquer(1, 1, Instant(0));
        i.repliquer(2, 1, Instant(0));

        // Le meneur avance ; la réplique 2 ne rattrape plus, mais elle est
        // vivante — elle est seulement lente.
        i.ecrire().unwrap();
        i.repliquer(1, 2, Instant(10));

        // Avant le temporisateur, l'hypothèse tient.
        i.avancer(Instant(20), &mut h);
        assert_eq!(i.taille_isr(), 3, "personne n'est encore exclu");
        assert_eq!(h.get(REGLAGE_LAG).unwrap().dementis, 0);

        // Au-delà, elle est démentie, et un suiveur vivant est exclu.
        i.avancer(Instant(40), &mut h);
        assert_eq!(i.taille_isr(), 2, "la réplique lente est exclue");
        assert!(
            i.repliques.iter().find(|r| r.id == 2).unwrap().vivante,
            "elle est exclue alors qu'elle est vivante — c'est tout le point"
        );
        assert_eq!(i.pannes, 0, "aucune panne : EX-M07");
        assert_eq!(i.retraits_pour_retard, 1);
        assert!(
            h.get(REGLAGE_LAG).unwrap().dementis > 0,
            "le registre doit compter le démenti (EX-C12)"
        );
    }

    /// EX-M08 — l'élection reste dans l'ISR tant qu'un membre vit, et R1 tient.
    #[test]
    fn lelection_reste_dans_lisr_quand_elle_le_peut() {
        let (mut i, mut o, _) = isr();
        i.ecrire().unwrap();
        i.repliquer(1, 1, Instant(0));
        i.repliquer(2, 1, Instant(0));
        i.arreter(0);
        let nouveau = i.elire().expect("un membre de l'ISR vit encore");
        assert!(nouveau == 1 || nouveau == 2);
        i.verifier_r1(&mut o, Instant(5));
        assert!(o.violations().is_empty());
    }

    /// R2 — la borne de visibilité ne dépasse jamais la réplique la plus en
    /// retard de l'ISR.
    #[test]
    fn r2_ne_depasse_pas_la_replique_la_plus_en_retard() {
        let (mut i, _, _) = isr();
        for _ in 0..5 {
            i.ecrire().unwrap();
        }
        i.repliquer(1, 5, Instant(1));
        i.repliquer(2, 3, Instant(1));
        assert_eq!(i.borne_visibilite, 3, "la plus en retard borne la visibilité");
    }

    /// Sans meneur, il n'y a pas de « meneur ultérieur » : R1 ne peut pas être
    /// violée par une partition simplement indisponible. C'est la distinction
    /// entre perdre une donnée et ne pas pouvoir la servir.
    #[test]
    fn une_partition_sans_meneur_ne_viole_pas_r1() {
        let (mut i, mut o, _) = isr();
        i.ecrire().unwrap();
        i.repliquer(1, 1, Instant(0));
        i.repliquer(2, 1, Instant(0));
        i.arreter(0);
        i.arreter(1);
        i.arreter(2);
        i.verifier_r1(&mut o, Instant(9));
        assert!(o.violations().is_empty());
    }
}
