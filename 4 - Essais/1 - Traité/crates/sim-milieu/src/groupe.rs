//! Groupe de consommation et rééquilibrage (EX-M17 à EX-M19, EX-M22, EX-M23).
//!
//! **T1 du §2.5** — le coordonnateur de groupe est une autorité à vue globale.
//! Il est instancié **explicitement et séparément** de l'essaim, exactement
//! comme le coordonnateur du scénario F : EX-A12 continue d'interdire à un
//! *agent* d'avoir cette vue. Le protocole, lui, est un mécanisme du modèle et
//! non une dépendance externe — le monde clos tient (§3.3).
//!
//! Les valeurs de phases et de messages sont des valeurs de documentation
//! produit, donc périssables (annexe B). Ce que le simulateur mesure, ce sont
//! celles du **modèle**.

use sim_core::oracle::{Oracle, Registre};
use sim_core::temps::{Duree, Instant};

/// Oracles du groupe (EX-M23). Les deux sont **distincts et jamais confondus**.
pub const UN_SEUL_PROPRIETAIRE: &str =
    "EX-M23 [S] — chaque partition est affectée à au plus un membre";
/// Vivacité **bornée** par le délai de session — l'autre moitié d'EX-M23.
/// Confondre les deux rendrait la moitié des exigences non testable (PD2).
pub const TOUTE_PARTITION_A_UN_PROPRIETAIRE: &str =
    "EX-M23 [L] — toute partition finit par avoir un propriétaire, après expiration du délai de session";

/// Les trois protocoles de rééquilibrage (EX-M17). Le choix est un paramètre
/// de scénario, jamais une constante.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Protocole {
    /// Barrière unique (JoinGroup/SyncGroup) : **4n messages**, deux
    /// aller-retours par membre, **révocation de toutes les tâches en cours** à
    /// chaque changement d'appartenance. Aucune partition n'est servie pendant.
    BarriereUnique,
    /// Coopératif incrémental : deux rééquilibrages consécutifs, le premier ne
    /// révoquant que les partitions qui changent de main. **8n messages**,
    /// quatre aller-retours. Aucune partition n'est servie pendant.
    ///
    /// Note de lecture : le traité se contredit sur ce compte de tours — 8 au
    /// §5.2, 4 au §6.3 et au tableau 5. Le PRD tranche pour quatre
    /// aller-retours et quatre phases (EX-M17, EX-M22), et le désaccord est
    /// consigné plutôt que masqué.
    CooperatifIncremental,
    /// Attribution côté courtier par battement de cœur, convergente membre par
    /// membre : **Θ(1) message par membre et par intervalle**, aucune barrière.
    /// Les partitions restent servies.
    BattementDeCoeur,
}

impl Protocole {
    /// Messages d'un rééquilibrage sur un groupe de n membres.
    pub fn messages(self, n: u32) -> u64 {
        match self {
            Protocole::BarriereUnique => 4 * n as u64,
            Protocole::CooperatifIncremental => 8 * n as u64,
            // Un message par membre et par intervalle : le rééquilibrage n'est
            // pas un événement, c'est un régime.
            Protocole::BattementDeCoeur => n as u64,
        }
    }

    /// Phases, comptées **séparément** des tours et jamais dans la même colonne
    /// (EX-M22).
    pub fn phases(self) -> u64 {
        match self {
            Protocole::BarriereUnique => 2,
            Protocole::CooperatifIncremental => 4,
            Protocole::BattementDeCoeur => 0,
        }
    }

    /// Aller-retours en série d'un rééquilibrage. Ce ne sont **pas** des tours :
    /// voir [`Protocole::tours`].
    pub fn aller_retours(self) -> u64 {
        match self {
            Protocole::BarriereUnique => 2,
            Protocole::CooperatifIncremental => 4,
            // Aucun aller-retour : le courtier pousse l'attribution sur le
            // battement, et n'attend pas de réponse.
            Protocole::BattementDeCoeur => 0,
        }
    }

    /// Tours, **dans la convention de l'annexe B.1**, que EX-M22 impose : deux
    /// envois indépendants comptent pour un tour, deux envois enchaînés en
    /// comptent deux, donc **un aller-retour vaut deux tours**.
    ///
    /// Le rééquilibrage d'origine coûte ainsi 4 tours et le coopératif 8, ce que
    /// l'annexe B du PRD écrit — et ce que §6.1 et §6.3 du traité écrivent « 4 »
    /// sous leur propre convention. Le battement de cœur coûte 1 tour : un envoi
    /// sans attente.
    ///
    /// Cette fonction rendait les aller-retours sous le nom de tours, soit la
    /// moitié du compte imposé pour les deux protocoles à barrière.
    pub fn tours(self) -> u64 {
        match self {
            Protocole::BattementDeCoeur => 1,
            autre => 2 * autre.aller_retours(),
        }
    }

    /// Les deux premiers protocoles posent une barrière : pendant le
    /// rééquilibrage, **aucune partition n'est servie**.
    pub fn pose_une_barriere(self) -> bool {
        !matches!(self, Protocole::BattementDeCoeur)
    }

    /// Nom court du protocole, tel qu'il s'affiche.
    pub fn nom(self) -> &'static str {
        match self {
            Protocole::BarriereUnique => "barrière unique",
            Protocole::CooperatifIncremental => "coopératif incrémental",
            Protocole::BattementDeCoeur => "battement de cœur",
        }
    }
}

/// Le coût d'un changement de population, ligne à ligne selon le tableau 5
/// (EX-M22). Les colonnes ne se mélangent jamais.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub struct CoutChangement {
    /// Messages échangés.
    pub messages: u64,
    /// Tours, convention de l'annexe B.1 : un aller-retour en vaut deux
    /// (EX-M22). Jamais un compte d'aller-retours.
    pub tours: u64,
    /// Phases du protocole. Jamais dans la même colonne que les tours.
    pub phases: u64,
    /// Validations de décalage provoquées par le changement.
    pub validations_de_decalage: u64,
    /// Points de reprise reconstruits.
    pub points_de_reprise: u64,
    /// Délai avant que le coût soit engagé — non nul pour une sortie non
    /// planifiée, qui attend l'expiration du délai de session.
    pub delai: Duree,
    /// Libellé de la ligne du tableau 5.
    pub ligne: &'static str,
}

/// Le groupe de consommation.
pub struct Groupe {
    /// Protocole de rééquilibrage en vigueur. C'est un paramètre de scénario.
    pub protocole: Protocole,
    /// Membres, ordonnés (PD1).
    membres: Vec<u32>,
    /// Propriétaire de chaque partition. `None` = orpheline.
    attribution: Vec<Option<u32>>,
    /// Délai de session — c'est le **détecteur**, et la vivacité d'EX-M23 ne
    /// s'énonce jamais sans lui.
    pub delai_session: Duree,
    /// Rééquilibrages déclenchés depuis le début.
    pub reequilibrages: u64,
    /// Messages cumulés du protocole de groupe.
    pub messages: u64,
    /// Tours cumulés, convention de l'annexe B.1 (EX-M22).
    pub tours: u64,
    /// Phases cumulées.
    pub phases: u64,
    /// Instant où chaque partition est devenue orpheline. Renseigné dès la
    /// construction : un groupe naît sans membre, donc **toutes ses partitions
    /// sont orphelines depuis sa création**, et cette période compte comme les
    /// autres.
    orphelines_depuis: Vec<Option<Instant>>,
    /// Durée cumulée pendant laquelle des partitions ont été sans propriétaire,
    /// **orphelinat initial compris** : c'est la même période que celle sur
    /// laquelle [`Groupe::suivre_vivacite`] ouvre son attente, et les deux
    /// mesures ne peuvent donc pas se contredire.
    ///
    /// Cumulée **sur les partitions** : p partitions orphelines pendant d tics
    /// comptent p × d, non d.
    pub duree_orpheline: Duree,
    /// Le groupe est-il en cours de rééquilibrage ? Sous barrière, plus rien
    /// n'est servi.
    pub en_reequilibrage: bool,
    /// Une attente de vivacité est-elle déjà ouverte au registre ? Sert
    /// l'idempotence de [`Groupe::suivre_vivacite`] : sans ce drapeau, un appel
    /// par tic empilait une attente par tic, et `Registre::satisfaire` n'en
    /// retire qu'une — toutes les autres échoyaient plus tard, en violations
    /// fabriquées par la fréquence du sondage.
    attente_ouverte: bool,
}

impl Groupe {
    /// Groupe vide sur `p` partitions, toutes orphelines **depuis `creation`**.
    ///
    /// La date de création est un paramètre et non `Instant(0)` : elle ouvre la
    /// période d'orphelinat initial, que [`Groupe::duree_orpheline`] cumule et
    /// que [`Groupe::suivre_vivacite`] met en attente. La supposer nulle
    /// rendrait la durée fausse — et non approximative — pour un groupe créé en
    /// cours d'exécution.
    pub fn nouveau(
        p: u32,
        protocole: Protocole,
        delai_session: Duree,
        creation: Instant,
    ) -> Groupe {
        Groupe {
            protocole,
            membres: Vec::new(),
            attribution: vec![None; p as usize],
            delai_session,
            reequilibrages: 0,
            messages: 0,
            tours: 0,
            phases: 0,
            orphelines_depuis: vec![Some(creation); p as usize],
            duree_orpheline: Duree(0),
            en_reequilibrage: false,
            attente_ouverte: false,
        }
    }

    /// Nombre de partitions — **la seule unité de parallélisme** du côté
    /// consommateur.
    ///
    /// Dérivé de la table d'attribution, et non porté par un champ public : la
    /// table et `orphelines_depuis` sont dimensionnées à la construction, et un
    /// `p` modifiable après coup désaccordait [`Groupe::parallelisme_utile`] de
    /// [`Groupe::debit_instantane`] sans qu'aucun invariant le rattrape.
    pub fn p(&self) -> u32 {
        self.attribution.len() as u32
    }

    /// Arme les deux oracles d'EX-M23 : la sûreté et la vivacité bornée.
    pub fn armer_oracles(&self, registre: &mut Registre) {
        registre.armer(Oracle::surete(UN_SEUL_PROPRIETAIRE, "§2.2, tableau 5"));
        // La vivacité est **bornée par le délai de session**, et c'est la seule
        // condition sous laquelle elle s'énonce (PD2, EX-M23).
        registre.armer(Oracle::vivacite_bornee(
            TOUTE_PARTITION_A_UN_PROPRIETAIRE,
            // Le rééquilibrage suit l'expiration : la borne est la somme.
            // `Duree + Duree` et non `* 2` : l'addition est saturante, et le
            // profil release ne pose pas `overflow-checks` — un produit enroulé
            // rendrait une borne de vivacité *plus courte* que le délai de
            // session, donc une violation fabriquée par l'arithmétique.
            self.delai_session + self.delai_session,
            "§2.2, tableau 5",
        ));
    }

    /// Membres du groupe, ordonnés.
    pub fn membres(&self) -> &[u32] {
        &self.membres
    }

    /// Nombre de membres. Au-delà de `p`, les membres supplémentaires sont
    /// **inertes** : voir la note sur le parallélisme utile (EX-M19).
    pub fn n(&self) -> u32 {
        self.membres.len() as u32
    }

    /// Propriétaire de chaque partition, `None` pour une orpheline.
    pub fn attribution(&self) -> &[Option<u32>] {
        &self.attribution
    }

    /// EX-M19 — **parallélisme utile min(n, p)**. Au plus p agents travaillent ;
    /// les n − p autres sont inactifs, participent à chaque rééquilibrage et
    /// comptent dans le coût de coordination. Le simulateur les compte dans les
    /// messages et **jamais** dans le débit.
    pub fn parallelisme_utile(&self) -> u32 {
        self.n().min(self.p())
    }

    /// Membres inactifs : ils coûtent sans produire. C'est le terme σ du §2.1 du traité
    /// qui grossit pendant que le numérateur reste plat.
    pub fn membres_inactifs(&self) -> u32 {
        self.n().saturating_sub(self.p())
    }

    /// Débit utile instantané, en partitions servies. Nul pendant un
    /// rééquilibrage à barrière.
    pub fn debit_instantane(&self) -> u32 {
        if self.en_reequilibrage && self.protocole.pose_une_barriere() {
            0
        } else {
            self.attribution.iter().filter(|a| a.is_some()).count() as u32
        }
    }

    /// Réattribue les partitions aux membres, en tourniquet déterministe.
    fn attribuer(&mut self, maintenant: Instant) {
        for (i, a) in self.attribution.iter_mut().enumerate() {
            let nouveau = if self.membres.is_empty() {
                None
            } else {
                Some(self.membres[i % self.membres.len()])
            };
            if nouveau.is_some() {
                if let Some(depuis) = self.orphelines_depuis[i].take() {
                    self.duree_orpheline = self.duree_orpheline + (maintenant - depuis);
                }
            }
            *a = nouveau;
        }
    }

    /// Déclenche un rééquilibrage et facture son coût.
    fn reequilibrer(&mut self, maintenant: Instant) {
        let n = self.n();
        self.reequilibrages += 1;
        self.messages += self.protocole.messages(n);
        self.tours += self.protocole.tours();
        self.phases += self.protocole.phases();
        self.en_reequilibrage = self.protocole.pose_une_barriere();
        self.attribuer(maintenant);
        self.en_reequilibrage = false;
    }

    /// Tableau 5 — **création d'un agent sans état** : 0 message sur le milieu,
    /// 0 tour, débit inchangé. Ce n'est pas la même chose qu'entrer dans un
    /// groupe, et le produit ne les confond pas.
    pub fn creer_agent_sans_etat(&self) -> CoutChangement {
        CoutChangement {
            ligne: "création ou destruction d'un agent sans état",
            ..Default::default()
        }
    }

    /// Tableau 5 — **entrée dans un groupe** : Θ(n) messages.
    pub fn entrer(&mut self, membre: u32, maintenant: Instant) -> CoutChangement {
        if !self.membres.contains(&membre) {
            self.membres.push(membre);
            self.membres.sort_unstable();
        }
        let avant = (self.messages, self.tours, self.phases);
        self.reequilibrer(maintenant);
        CoutChangement {
            messages: self.messages - avant.0,
            tours: self.tours - avant.1,
            phases: self.phases - avant.2,
            ligne: "entrée dans un groupe",
            ..Default::default()
        }
    }

    /// Tableau 5 — **sortie planifiée d'un agent porteur** : Θ(n) messages,
    /// plus une validation de décalage et un point de reprise.
    pub fn sortir_planifie(&mut self, membre: u32, maintenant: Instant) -> CoutChangement {
        let portait = self.attribution.contains(&Some(membre));
        self.retirer_membre(membre, maintenant);
        let avant = (self.messages, self.tours, self.phases);
        self.reequilibrer(maintenant);
        CoutChangement {
            messages: self.messages - avant.0,
            tours: self.tours - avant.1,
            phases: self.phases - avant.2,
            validations_de_decalage: portait as u64,
            points_de_reprise: portait as u64,
            ligne: "sortie planifiée d'un agent porteur",
            ..Default::default()
        }
    }

    /// Tableau 5 — **sortie non planifiée** : Θ(n) messages **après expiration
    /// du délai de session**. Entre l'arrêt et cette expiration, le débit des
    /// partitions orphelines est nul, et cette durée est mesurée.
    pub fn sortir_non_planifie(&mut self, membre: u32, maintenant: Instant) -> CoutChangement {
        self.retirer_membre(membre, maintenant);
        // Le rééquilibrage n'a lieu qu'après le délai de session : c'est le
        // détecteur qui le déclenche, pas l'arrêt lui-même.
        let echeance = maintenant + self.delai_session;
        let avant = (self.messages, self.tours, self.phases);
        self.reequilibrer(echeance);
        CoutChangement {
            messages: self.messages - avant.0,
            tours: self.tours - avant.1,
            phases: self.phases - avant.2,
            delai: self.delai_session,
            ligne: "sortie non planifiée",
            ..Default::default()
        }
    }

    fn retirer_membre(&mut self, membre: u32, maintenant: Instant) {
        self.membres.retain(|m| *m != membre);
        for (i, a) in self.attribution.iter_mut().enumerate() {
            if *a == Some(membre) {
                *a = None;
                self.orphelines_depuis[i] = Some(maintenant);
            }
        }
    }

    /// EX-M23 `[S]` — chaque partition est affectée à au plus un membre. Vérifié
    /// par construction du type `Option<u32>`.
    ///
    /// Le prédicat écrit ici est **plus fort** que l'énoncé d'EX-M23 : il cherche
    /// un propriétaire qui ne serait plus membre. **Aucune suite d'appels publics
    /// ne peut l'atteindre** — les deux seuls scripteurs de `attribution` sont
    /// `attribuer`, qui n'assigne que des membres courants, et `retirer_membre`,
    /// qui met `None` sur les partitions du partant, et le second est toujours
    /// suivi du premier. C'est la situation que la
    /// crate nomme ailleurs pour M2 et M3 ([`crate::journal::Milieu::verifier`])
    /// et pour R2 ([`crate::replication::Isr::armer_oracles`]) : l'oracle reste
    /// armé pour que sa ligne figure au catalogue, non pour qu'il se déclenche.
    ///
    /// Le prédicat est conservé plutôt que supprimé pour la raison que
    /// [`crate::journal::Partition`] donne déjà de M1 : un invariant vrai par
    /// construction cesse de l'être à la première modification. Le test
    /// `une_partition_na_quun_proprietaire` livre le contre-exemple depuis
    /// l'intérieur du module — le seul endroit d'où l'état est constructible —
    /// pour que le prédicat ne puisse pas être vidé sans qu'un test tombe
    /// (NF-10).
    pub fn verifier_surete(&self, registre: &mut Registre, maintenant: Instant) {
        for (i, a) in self.attribution.iter().enumerate() {
            if let Some(m) = a {
                if !self.membres.contains(m) {
                    registre.violer(
                        UN_SEUL_PROPRIETAIRE,
                        maintenant,
                        format!("partition {i} attribuée au membre {m}, qui a quitté le groupe"),
                    );
                    return;
                }
            }
        }
    }

    /// EX-M23 `[L]` — arme **une** attente tant qu'au moins une partition est
    /// orpheline, et la satisfait dès que toutes ont un propriétaire.
    ///
    /// Idempotent : appelée à chaque tic, cette méthode n'ouvre pas une attente
    /// par tic. L'attente porte le compte des orphelines et la condition, pas
    /// une par partition — la vivacité d'EX-M23 est énoncée sur *toute*
    /// partition, et une attente par partition en ferait autant de propriétés
    /// distinctes.
    pub fn suivre_vivacite(&mut self, registre: &mut Registre, maintenant: Instant) {
        if self.attribution.iter().all(|a| a.is_some()) {
            if self.attente_ouverte {
                registre.satisfaire(TOUTE_PARTITION_A_UN_PROPRIETAIRE);
                self.attente_ouverte = false;
            }
        } else if !self.attente_ouverte {
            self.attente_ouverte = true;
            registre.attendre(
                TOUTE_PARTITION_A_UN_PROPRIETAIRE,
                maintenant,
                format!(
                    "{} partition(s) orpheline(s) ; la condition est l'expiration du délai de \
                     session ({} tics), qui est le détecteur",
                    self.attribution.iter().filter(|a| a.is_none()).count(),
                    self.delai_session.0
                ),
            );
        }
    }

    /// EX-M18 — le nombre de rééquilibrages **n'a pas de borne**, et le
    /// simulateur n'en affiche aucune : le compte cumulé, jamais une estimation
    /// de fin.
    pub fn affichage_reequilibrages(&self) -> String {
        format!(
            "{} rééquilibrage(s) cumulé(s) — la condition d'arrêt est l'atteinte d'une génération \
             stable, et elle n'est pas garantie (EX-M18). Aucune estimation de fin n'est affichée.",
            self.reequilibrages
        )
    }

    /// EX-M19 — l'interface nomme la **cause mesurée** et le remède qui en
    /// découle, jamais une métaphore spatiale.
    pub fn diagnostic_parallelisme(&self) -> String {
        if self.membres_inactifs() == 0 {
            format!(
                "n = {} ≤ p = {} : tous les membres travaillent, parallélisme utile {}",
                self.n(),
                self.p(),
                self.parallelisme_utile()
            )
        } else {
            format!(
                "n = {} > p = {} : {} membre(s) inactif(s). Ils ne produisent aucun débit et \
                 participent à chaque rééquilibrage — c'est le terme σ qui grossit pendant que le \
                 numérateur reste plat. Cause mesurée : coût de coordination du rééquilibrage. \
                 Remède : augmenter p, ou refondre la clé.",
                self.n(),
                self.p(),
                self.membres_inactifs()
            )
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn groupe(p: u32, protocole: Protocole) -> Groupe {
        Groupe::nouveau(p, protocole, Duree(45_000), Instant(0))
    }

    /// EX-M23 `[L]` — l'orphelinat **initial** est une période comme les autres.
    /// Un groupe naît sans membre : `suivre_vivacite` ouvre une attente dès la
    /// création, et `duree_orpheline` doit cumuler la même période. Sans cela,
    /// deux mesures du même fait se contredisent.
    #[test]
    fn lorphelinat_initial_est_compte_comme_les_autres() {
        let mut g = groupe(2, Protocole::BattementDeCoeur);
        let mut o = Registre::nouveau();
        g.armer_oracles(&mut o);
        g.suivre_vivacite(&mut o, Instant(0));
        assert_eq!(
            o.attentes_ouvertes(),
            1,
            "l'oracle voit l'orphelinat initial"
        );
        g.entrer(0, Instant(500));
        g.suivre_vivacite(&mut o, Instant(500));
        assert_eq!(o.attentes_ouvertes(), 0);
        assert_eq!(
            g.duree_orpheline,
            Duree(1_000),
            "2 partitions × 500 tics depuis la création"
        );
    }

    /// La date de création n'est pas supposée nulle : un groupe créé en cours
    /// d'exécution ne cumule pas d'orphelinat antérieur à lui-même.
    #[test]
    fn un_groupe_cree_en_cours_dexecution_ne_cumule_pas_davant() {
        let mut g = Groupe::nouveau(2, Protocole::BattementDeCoeur, Duree(45_000), Instant(700));
        g.entrer(0, Instant(900));
        assert_eq!(
            g.duree_orpheline,
            Duree(400),
            "2 × 200 tics, et non 2 × 900"
        );
    }

    /// EX-M17 — les trois protocoles ont trois coûts distincts, et le choix est
    /// un paramètre.
    #[test]
    fn les_trois_protocoles_ont_trois_couts() {
        assert_eq!(Protocole::BarriereUnique.messages(10), 40, "4n");
        assert_eq!(Protocole::CooperatifIncremental.messages(10), 80, "8n");
        assert_eq!(
            Protocole::BattementDeCoeur.messages(10),
            10,
            "Θ(1) par membre"
        );
        assert_eq!(Protocole::BarriereUnique.phases(), 2);
        assert_eq!(Protocole::CooperatifIncremental.phases(), 4);
        assert!(Protocole::BarriereUnique.pose_une_barriere());
        assert!(!Protocole::BattementDeCoeur.pose_une_barriere());
    }

    /// EX-M22 — « l'unité de tour est celle de l'annexe B.1 » : un aller-retour
    /// vaut deux tours. L'annexe B chiffre 2 aller-retours = **4 tours** pour le
    /// protocole d'origine et 4 aller-retours = **8 tours** pour le coopératif.
    #[test]
    fn les_tours_sont_comptes_dans_la_convention_de_lannexe_b1() {
        assert_eq!(Protocole::BarriereUnique.aller_retours(), 2);
        assert_eq!(Protocole::BarriereUnique.tours(), 4);
        assert_eq!(Protocole::CooperatifIncremental.aller_retours(), 4);
        assert_eq!(Protocole::CooperatifIncremental.tours(), 8);
        // Un envoi sans attente : un tour, aucun aller-retour.
        assert_eq!(Protocole::BattementDeCoeur.aller_retours(), 0);
        assert_eq!(Protocole::BattementDeCoeur.tours(), 1);
        // Les tours ne sont jamais les phases (EX-M22).
        for p in [
            Protocole::BarriereUnique,
            Protocole::CooperatifIncremental,
            Protocole::BattementDeCoeur,
        ] {
            assert_ne!(p.tours(), p.phases(), "{}", p.nom());
        }
    }

    /// EX-M22 — un agent **sans état** ne coûte rien sur le milieu. Ce n'est pas
    /// la même ligne du tableau 5 qu'une entrée dans un groupe.
    #[test]
    fn un_agent_sans_etat_ne_coute_rien() {
        let g = groupe(8, Protocole::CooperatifIncremental);
        let c = g.creer_agent_sans_etat();
        assert_eq!(c.messages, 0);
        assert_eq!(c.tours, 0);
        assert_eq!(
            c,
            CoutChangement {
                ligne: c.ligne,
                ..Default::default()
            }
        );
    }

    /// EX-M22 — l'entrée dans un groupe coûte Θ(n).
    #[test]
    fn lentree_dans_un_groupe_coute_theta_n() {
        let mut g = groupe(8, Protocole::BarriereUnique);
        g.entrer(0, Instant(0));
        let c = g.entrer(1, Instant(1));
        assert_eq!(c.messages, 8, "4n à n = 2");
        assert_eq!(c.phases, 2);
        assert_eq!(c.tours, 4, "2 aller-retours = 4 tours, convention B.1");
    }

    /// EX-M22 — la sortie planifiée d'un porteur ajoute une validation de
    /// décalage et un point de reprise ; la sortie non planifiée attend le
    /// délai de session.
    #[test]
    fn les_deux_sorties_ne_coutent_pas_la_meme_chose() {
        let mut g = groupe(4, Protocole::CooperatifIncremental);
        g.entrer(0, Instant(0));
        g.entrer(1, Instant(0));
        let planifiee = g.sortir_planifie(0, Instant(10));
        assert_eq!(planifiee.validations_de_decalage, 1);
        assert_eq!(planifiee.points_de_reprise, 1);
        assert_eq!(planifiee.delai, Duree(0));

        g.entrer(0, Instant(20));
        let non_planifiee = g.sortir_non_planifie(0, Instant(30));
        assert_eq!(
            non_planifiee.delai,
            Duree(45_000),
            "après expiration du délai de session"
        );
        assert_eq!(
            non_planifiee.validations_de_decalage, 0,
            "rien n'a été validé"
        );
    }

    /// EX-M19 — au-delà de p, les membres supplémentaires coûtent sans produire.
    #[test]
    fn au_dela_de_p_les_membres_coutent_sans_produire() {
        let mut g = groupe(4, Protocole::BarriereUnique);
        for m in 0..4 {
            g.entrer(m, Instant(0));
        }
        assert_eq!(g.parallelisme_utile(), 4);
        assert_eq!(g.membres_inactifs(), 0);
        let messages_a_4 = g.messages;

        for m in 4..12 {
            g.entrer(m, Instant(0));
        }
        assert_eq!(
            g.parallelisme_utile(),
            4,
            "le débit utile reste plafonné par p"
        );
        assert_eq!(g.membres_inactifs(), 8);
        assert!(
            g.messages > messages_a_4 * 3,
            "le coût de coordination, lui, a explosé"
        );
        assert!(g.diagnostic_parallelisme().contains("Remède"));
        // L'interface nomme la cause mesurée, jamais une métaphore spatiale.
        assert!(!g.diagnostic_parallelisme().contains("espace"));
    }

    /// EX-M23 `[S]` — une partition n'a jamais deux propriétaires. Le type le
    /// garantit ; l'oracle vérifie en outre qu'aucun propriétaire n'est un
    /// partant.
    ///
    /// Le contre-exemple est **construit ici**, en écrivant directement dans
    /// `attribution` : aucune suite d'appels publics ne peut laisser un
    /// non-membre propriétaire, et la doc de [`Groupe::verifier_surete`] le dit.
    /// Sans ce contre-exemple, le test passait avec un `verifier_surete` au corps
    /// vide — il ne faisait jamais partir personne (NF-10).
    #[test]
    fn une_partition_na_quun_proprietaire() {
        let mut g = groupe(4, Protocole::BattementDeCoeur);
        let mut o = Registre::nouveau();
        g.armer_oracles(&mut o);
        g.entrer(0, Instant(0));
        g.entrer(1, Instant(0));
        g.verifier_surete(&mut o, Instant(1));
        assert!(o.violations().is_empty());
        let proprietaires: Vec<u32> = g.attribution().iter().flatten().copied().collect();
        assert_eq!(proprietaires.len(), 4, "les quatre partitions sont servies");

        // État inatteignable de l'extérieur, et c'est précisément pourquoi il se
        // fabrique ici : l'oracle doit voir un propriétaire non membre.
        g.attribution[2] = Some(77);
        g.verifier_surete(&mut o, Instant(2));
        assert_eq!(o.violations().len(), 1, "{:?}", o.violations());
        assert!(o.violations()[0].details.contains("partition 2"));
        assert!(o.violations()[0].details.contains("qui a quitté le groupe"));
    }

    /// EX-M23 `[L]` — la vivacité ne s'énonce **jamais** sans sa condition, et la
    /// durée orpheline est mesurée.
    #[test]
    fn la_vivacite_porte_sa_condition_et_la_duree_orpheline_est_mesuree() {
        let mut g = groupe(2, Protocole::BattementDeCoeur);
        let mut o = Registre::nouveau();
        g.armer_oracles(&mut o);
        g.entrer(0, Instant(0));

        g.retirer_membre(0, Instant(100));
        g.suivre_vivacite(&mut o, Instant(100));
        assert_eq!(o.attentes_ouvertes(), 1, "l'attente porte la condition");

        g.entrer(1, Instant(200));
        g.suivre_vivacite(&mut o, Instant(200));
        assert_eq!(o.attentes_ouvertes(), 0);
        assert_eq!(g.duree_orpheline, Duree(200), "deux partitions × 100 tics");
        assert!(o.violations().is_empty());
    }

    /// EX-M23 `[L]`, PD2 — l'attente est une **propriété**, pas un compteur de
    /// sondages. Sonder à chaque tic n'empilait pas moins d'une attente par tic,
    /// et `Registre::satisfaire` n'en retire qu'une : toutes les autres
    /// échoyaient ensuite en violations, à une date où la condition était
    /// pourtant remplie. Le nombre de violations dépendait donc de la fréquence
    /// du sondage.
    #[test]
    fn sonder_la_vivacite_a_repetition_nempile_pas_les_attentes() {
        let mut g = groupe(2, Protocole::BattementDeCoeur);
        let mut o = Registre::nouveau();
        g.armer_oracles(&mut o);
        for t in 0..10 {
            g.suivre_vivacite(&mut o, Instant(t));
        }
        assert_eq!(
            o.attentes_ouvertes(),
            1,
            "une attente, quel que soit le nombre de sondages"
        );

        g.entrer(0, Instant(10));
        g.suivre_vivacite(&mut o, Instant(10));
        assert_eq!(o.attentes_ouvertes(), 0);

        // Bien au-delà de l'horizon : rien n'échoit, parce que rien ne traîne.
        o.echoir(Instant(1_000_000));
        assert!(o.violations().is_empty(), "{:?}", o.violations());
    }

    /// EX-M18 — le compte cumulé s'affiche, jamais une estimation de fin.
    #[test]
    fn aucune_estimation_de_fin_nest_affichee() {
        let mut g = groupe(4, Protocole::BarriereUnique);
        for m in 0..5 {
            g.entrer(m, Instant(0));
        }
        let a = g.affichage_reequilibrages();
        assert!(a.contains("cumulé"));
        assert!(a.contains("n'est pas garantie"));
        assert!(!a.contains("fin prévue"));
    }

    /// EX-M17 — sous barrière, aucune partition n'est servie pendant le
    /// rééquilibrage ; sous battement de cœur, le service continue.
    #[test]
    fn la_barriere_suspend_le_service_le_battement_de_coeur_non() {
        let mut barriere = groupe(4, Protocole::BarriereUnique);
        barriere.entrer(0, Instant(0));
        barriere.en_reequilibrage = true;
        assert_eq!(barriere.debit_instantane(), 0);

        let mut battement = groupe(4, Protocole::BattementDeCoeur);
        battement.entrer(0, Instant(0));
        battement.en_reequilibrage = true;
        assert_eq!(battement.debit_instantane(), 4);
    }
}
