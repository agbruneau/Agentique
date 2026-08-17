//! File et service par agent (EX-C15), et coût d'une population (EX-C17).
//!
//! > Sa latence de réponse est une **sortie** du modèle, pas une entrée ; elle
//! > croît avec son arriéré. (EX-C15)
//!
//! C'est la condition d'existence de la cascade du §6.1 du traité : sans file, la
//! saturation serait *scriptée* au lieu d'être produite, et l'énoncé du §7.3 —
//! le taux de fausses suspicions est une fonction croissante de la charge —
//! deviendrait un paramètre au lieu d'un résultat.
//!
//! §8.3 du PRD impose de ne jamais mêler les deux ℓ₉₉ : celui du milieu est une
//! **entrée**, celui-ci est une **sortie**. Un affichage qui les confondrait est
//! un défaut bloquant.
//!
//! Ce module ne prouve pas qu'aucun ne les confond. Il fixe le libellé
//! ([`Service::LIBELLE_L99`]) et nomme la sortie ([`Service::l99_de_reponse`]) ;
//! le libellé n'a **aucun appelant** — `sim-viz` ne le lit pas —, de sorte que
//! la séparation est tenue par le nom des deux fonctions, pas par un affichage.
//! La doc de ce module annonçait « des libellés distincts dans toute
//! l'interface » : c'était affirmer un affichage qui n'existe pas.

use crate::temps::{Duree, Instant};
use serde::{Deserialize, Serialize};

/// Coût mémoire unitaire d'un agent (EX-C17).
///
/// Ce que le §2.2 du traité donne, et rien de plus : « de l'ordre de trois cents mots,
/// soit **quelques milliers d'octets** sur une architecture 64 bits, dont **233
/// mots** de zone de tas, pile comprise », puis deux chiffres qu'il refuse
/// d'arbitrer — la documentation d'OTP 29.0.5 « annonce **327** mots à son guide
/// d'efficacité […] et **338** à sa page de mémoire ; l'écart est explicable, et
/// **il reste la meilleure raison de ne rien gager sur le chiffre exact** ». Le
/// seul chiffre *dérivé* que la source publie est un ordre de grandeur : « le
/// plancher mémoire d'un million d'agents de ce type est donc de l'ordre de
/// **2,6 Go** avant tout état applicatif ».
///
/// Le défaut retient 327 parce qu'il faut un nombre pour calculer. C'est un
/// réglage, **pas** l'arbitrage que la source refuse de rendre : « 2 616
/// octets » n'apparaît nulle part dans le traité et ne s'y mettra pas. Ce que
/// NF-15 demande de retrouver ici est l'ordre de grandeur, et c'est ce que le
/// test épingle. Valeur périssable (annexe B) ; ce qui compte est que le
/// plancher mémoire d'une population soit **affiché**.
#[derive(Clone, Copy, Debug, Serialize, Deserialize)]
pub struct CoutAgent {
    /// Empreinte totale, en mots.
    pub mots: u64,
    /// Part allouée sur le tas, en mots.
    pub mots_de_tas: u64,
    /// Largeur d'un mot. 8 sur une machine 64 bits.
    pub octets_par_mot: u64,
}

impl Default for CoutAgent {
    fn default() -> Self {
        CoutAgent {
            mots: 327,
            mots_de_tas: 233,
            octets_par_mot: 8,
        }
    }
}

impl CoutAgent {
    /// Empreinte d'un agent, en octets.
    ///
    /// Les deux facteurs sont des champs publics désérialisés et le profil
    /// release du dépôt ne pose pas `overflow-checks` : le produit sature, sans
    /// quoi 2⁶¹ mots de 8 octets pèseraient **zéro**.
    pub fn octets(&self) -> u64 {
        self.mots.saturating_mul(self.octets_par_mot)
    }

    /// Plancher mémoire d'une population de n agents, affiché avec son unité.
    /// Sature pour le même motif que [`CoutAgent::octets`].
    pub fn plancher(&self, n: u32) -> u64 {
        self.octets().saturating_mul(u64::from(n))
    }

    /// Provenance de la valeur par défaut, à afficher avec elle (F1, F2).
    ///
    /// Elle porte les **deux** chiffres de la source et son refus de trancher :
    /// afficher « 327 mots » seul ferait passer un réglage pour une mesure.
    pub const SOURCE: &'static str =
        "§2.2 du traité — « de l'ordre de trois cents mots, soit quelques milliers d'octets \
         […] dont 233 mots de zone de tas, pile comprise » ; OTP 29.0.5 annonce 327 mots à son \
         guide d'efficacité et 338 à sa page de mémoire, « et il reste la meilleure raison de \
         ne rien gager sur le chiffre exact ». Le défaut retient 327 : réglage, non arbitrage. \
         Valeur périssable (annexe B)";
}

/// La file et le service d'un agent.
///
/// La file est **bornée** : au-delà, les demandes sont rejetées plutôt
/// qu'accumulées sans fin, ce qui est le comportement d'un système réel et ce
/// qui rend le délestage observable.
#[derive(Clone, Debug)]
pub struct Service {
    /// Temps de service d'une demande.
    pub temps_service: Duree,
    /// Capacité de la file. Zéro = illimitée.
    pub capacite: usize,
    /// Dates de **fin de service** des demandes acceptées et non encore
    /// achevées. Croissantes par construction : le serveur est unique.
    fins: Vec<Instant>,
    /// Instant où le serveur se libère.
    libre_a: Instant,
    /// Demandes acceptées depuis le début.
    pub servies: u64,
    /// Demandes rejetées faute de place. C'est le délestage, et il se voit.
    pub rejetees: u64,
    /// Latences de réponse mesurées — **sorties** du modèle.
    latences: Vec<u64>,
}

impl Service {
    /// File neuve. `capacite` à zéro signifie « illimitée », auquel cas rien
    /// n'est jamais rejeté et l'arriéré croît sans borne.
    pub fn nouveau(temps_service: Duree, capacite: usize) -> Service {
        Service {
            temps_service,
            capacite,
            fins: Vec::new(),
            libre_a: Instant(0),
            servies: 0,
            rejetees: 0,
            latences: Vec::new(),
        }
    }

    /// Arriéré : demandes acceptées dont le service n'est pas achevé.
    pub fn arriere(&self) -> usize {
        self.fins.len()
    }

    /// Soumet une demande. Rend la latence de réponse **produite**, ou `None`
    /// si la file est pleine.
    ///
    /// La latence n'est jamais tirée d'une distribution : elle est calculée à
    /// partir de l'arriéré. C'est ce qui la rend croissante avec la charge sans
    /// qu'aucun paramètre ne le décrète.
    pub fn soumettre(&mut self, arrivee: Instant) -> Option<Duree> {
        // Ce qui est achevé quitte l'arriéré avant qu'on juge de la place.
        self.avancer(arrivee);
        if self.capacite > 0 && self.arriere() >= self.capacite {
            self.rejetees += 1;
            return None;
        }
        // Le serveur prend la demande dès qu'il est libre, mais jamais avant
        // son arrivée.
        let debut = Instant(self.libre_a.0.max(arrivee.0));
        let fin = debut + self.temps_service;
        self.libre_a = fin;
        self.fins.push(fin);
        let latence = fin - arrivee;
        self.servies += 1;
        self.latences.push(latence.0);
        Some(latence)
    }

    /// Fait avancer la file jusqu'à `maintenant` : les demandes dont le service
    /// est achevé quittent l'arriéré.
    pub fn avancer(&mut self, maintenant: Instant) {
        self.fins.retain(|fin| *fin > maintenant);
    }

    /// ℓ₉₉ **de réponse de l'agent** — une sortie du modèle (§8.3 du PRD). Ne jamais
    /// afficher sous le même libellé que le ℓ₉₉ du milieu.
    pub fn l99_de_reponse(&self) -> Option<Duree> {
        if self.latences.is_empty() {
            return None;
        }
        let mut tri = self.latences.clone();
        tri.sort_unstable();
        let rang = ((0.99 * tri.len() as f64).ceil() as usize).saturating_sub(1);
        Some(Duree(tri[rang.min(tri.len() - 1)]))
    }

    /// Latence de la dernière demande servie. C'est elle que le détecteur
    /// confronte à son expiration (PD12).
    pub fn derniere_latence(&self) -> Option<Duree> {
        self.latences.last().map(|l| Duree(*l))
    }

    /// Libellé imposé (§8.3 du PRD) : les deux ℓ₉₉ ne portent jamais le même. Aucun
    /// appelant à ce jour ; voir la note du module.
    pub const LIBELLE_L99: &'static str =
        "ℓ₉₉ de réponse de l'agent — SORTIE du modèle, produite par la file et le temps de \
         service (EX-C15). À ne jamais confondre avec le ℓ₉₉ du milieu, qui est une entrée.";
}

#[cfg(test)]
mod tests {
    use super::*;

    /// EX-C17, NF-15 — ce que le §2.2 du traité permet de **retrouver** est un ordre de
    /// grandeur, pas un chiffre exact : la source donne 327 *et* 338 mots et
    /// dit que l'écart « reste la meilleure raison de ne rien gager sur le
    /// chiffre exact ». Sont épinglés d'abord les trois énoncés qui sont dans le
    /// traité — 233 mots de tas, « quelques milliers d'octets », « de l'ordre de
    /// 2,6 Go » pour un million —, ensuite, et séparément, l'arithmétique du
    /// défaut retenu, qui n'est pas un chiffre du traité.
    #[test]
    fn le_cout_dun_agent_retrouve_lordre_de_grandeur_du_traite() {
        let c = CoutAgent::default();

        // Du traité, textuellement.
        assert_eq!(c.mots_de_tas, 233, "« dont 233 mots de zone de tas »");
        assert!(
            (327..=338).contains(&c.mots),
            "le défaut se tient entre les deux chiffres que la source donne : {} mots",
            c.mots
        );
        assert!(
            (1_000..10_000).contains(&c.octets()),
            "« quelques milliers d'octets » : {} octets",
            c.octets()
        );
        let go = c.plancher(1_000_000) as f64 / 1e9;
        assert!(
            (go - 2.6).abs() < 0.26,
            "« de l'ordre de 2,6 Go » pour un million d'agents : {go:.3} Go"
        );
        // La provenance porte les deux chiffres et le refus de trancher.
        assert!(CoutAgent::SOURCE.contains("327"), "{}", CoutAgent::SOURCE);
        assert!(CoutAgent::SOURCE.contains("338"), "{}", CoutAgent::SOURCE);
        assert!(
            CoutAgent::SOURCE.contains("ne rien gager sur le chiffre exact"),
            "{}",
            CoutAgent::SOURCE
        );

        // Et l'arithmétique du réglage — 327 × 8 —, qui n'est **pas** un chiffre
        // du traité : garde de non-régression sur le défaut, rien de plus.
        assert_eq!(c.octets(), 2_616);
        assert_eq!(c.plancher(1_000), 2_616_000);
    }

    /// Les deux produits saturent : `mots` et `octets_par_mot` sont publics et
    /// désérialisés, et le profil release ne pose pas `overflow-checks`.
    #[test]
    fn le_cout_sature_au_lieu_de_senrouler() {
        let enorme = CoutAgent {
            mots: 1u64 << 61,
            mots_de_tas: 0,
            octets_par_mot: 8,
        };
        assert_eq!(enorme.octets(), u64::MAX, "2⁶¹ × 8 valait zéro octet");

        let gros = CoutAgent {
            mots: 1u64 << 40,
            mots_de_tas: 0,
            octets_par_mot: 8,
        };
        assert_eq!(gros.plancher(u32::MAX), u64::MAX);
    }

    /// EX-C15 — la latence est une **sortie** : elle croît avec l'arriéré, sans
    /// qu'aucun paramètre ne le décrète.
    #[test]
    fn la_latence_croit_avec_larriere() {
        let mut s = Service::nouveau(Duree(10), 0);
        // Toutes les demandes arrivent en même temps : le serveur les met en
        // file, et chacune attend celles qui la précèdent.
        let premiere = s.soumettre(Instant(0)).unwrap();
        let deuxieme = s.soumettre(Instant(0)).unwrap();
        let dixieme = (0..8).map(|_| s.soumettre(Instant(0)).unwrap()).last().unwrap();
        assert_eq!(premiere, Duree(10));
        assert_eq!(deuxieme, Duree(20));
        assert_eq!(dixieme, Duree(100));
        assert!(dixieme > premiere, "la charge produit la latence");
    }

    /// Un agent qui n'est pas chargé répond en un temps de service.
    #[test]
    fn sans_arriere_la_latence_est_le_temps_de_service() {
        let mut s = Service::nouveau(Duree(10), 0);
        assert_eq!(s.soumettre(Instant(0)), Some(Duree(10)));
        assert_eq!(s.soumettre(Instant(100)), Some(Duree(10)));
    }

    /// La file bornée rejette au lieu d'accumuler sans fin.
    #[test]
    fn une_file_bornee_rejette() {
        let mut s = Service::nouveau(Duree(10), 2);
        assert!(s.soumettre(Instant(0)).is_some());
        assert!(s.soumettre(Instant(0)).is_some());
        assert!(s.soumettre(Instant(0)).is_none(), "file pleine");
        assert_eq!(s.rejetees, 1);
    }

    /// §8.3 du PRD — le libellé du ℓ₉₉ de réponse dit qu'il est une sortie.
    #[test]
    fn les_deux_l99_ne_portent_pas_le_meme_libelle() {
        assert!(Service::LIBELLE_L99.contains("SORTIE"));
        assert!(Service::LIBELLE_L99.contains("jamais confondre"));
        let s = Service::nouveau(Duree(1), 0);
        assert_eq!(s.l99_de_reponse(), None, "sans mesure, pas de percentile");
    }

    /// PD12 — c'est cette latence que le détecteur confronte à son expiration,
    /// et c'est ainsi qu'un agent vivant mais saturé devient suspect.
    #[test]
    fn la_latence_produite_alimente_le_detecteur() {
        use crate::detecteur::{Detecteur, Etat};
        use crate::ActeurId;

        let mut s = Service::nouveau(Duree(10), 0);
        let mut d = Detecteur::nouveau(Duree(100), Duree(50), 3).expect("réglage valide");
        let cible = ActeurId(0);

        // Agent peu chargé : il répond sous l'expiration.
        for i in 0..3 {
            let l = s.soumettre(Instant(i * 1_000)).unwrap();
            d.sonder(cible, true, l, Instant(i * 100));
        }
        assert_eq!(d.etat(cible), Etat::Sain);

        // Agent saturé : la latence produite dépasse l'expiration, et le
        // détecteur le suspecte — alors qu'il est vivant.
        for i in 0..10 {
            let l = s.soumettre(Instant(3_000)).unwrap();
            d.sonder(cible, true, l, Instant(3_000 + i * 100));
        }
        assert_eq!(d.etat(cible), Etat::Suspect);
        assert!(d.proprietes().fausses_suspicions > 0);
    }
}
