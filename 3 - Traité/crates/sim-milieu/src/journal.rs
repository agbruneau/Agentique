//! Le journal partitionné et ses quatre invariants (EX-M01 à EX-M04).
//!
//! > M1 : l'ordre est total à l'intérieur d'une partition.
//! > M2 : aucun ordre n'est garanti entre partitions.
//! > M3 : un enregistrement validé est durable.
//! > M4 : le compactage ne réordonne jamais, il ne fait que supprimer. (§1.2)
//!
//! Ce que **ce module** ne fait pas, et qui vit ailleurs dans la même crate : la
//! réplication ISR (`replication`), le groupe de consommation (`groupe`), le
//! plan de contrôle (`controle`), le surcoût de format (`format`), l'historique
//! par identité (`historique`) et les quotas (`quota`). Rien ici ne prétend le
//! contraire, et `crate::hors_perimetre()` dit lesquels aucun scénario
//! n'exécute.

use crate::latence::{Latence, Mesures};
use sim_core::alea::Alea;
use sim_core::oracle::{Oracle, Registre};
use sim_core::temps::{Duree, Granularite, Instant};
use sim_core::ActeurId;
use std::collections::{BTreeMap, BTreeSet};

/// Clé de partitionnement et de compactage.
pub type Cle = u64;

/// Un enregistrement du journal.
///
/// La charge utile est un `f64` et sa taille est **déclarée** séparément.
/// Motif : un `Vec<u8>` par enregistrement coûte une allocation à l'écriture et
/// une autre à chaque lecture, ce qui domine le temps d'exécution d'une
/// campagne — mesuré, pas supposé. Le type est `Copy`, la lecture est un
/// memcpy, et `octets` garde le comptage d'EX-M13 exact tout en préparant le
/// surcoût de format d'EX-M11, que `crate::format` calcule.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Enregistrement {
    /// Partition d'origine. Un lecteur multi-partitions en a besoin pour
    /// avancer le bon curseur : la clé ne suffit pas, deux clés pouvant
    /// partager une partition.
    pub partition: u32,
    /// Position dans la partition. Strictement croissante : c'est M1.
    pub decalage: u64,
    /// Clé de l'enregistrement. Elle décide de la partition, et deux clés
    /// distinctes n'ont **aucune** métrique entre elles : il n'y a pas de
    /// gradient dans le milieu (§1.2).
    pub cle: Cle,
    /// Charge utile.
    pub valeur: f64,
    /// Taille déclarée de l'enregistrement, en octets.
    ///
    /// Le surcoût de format réel — 60 octets pour un message seul, 753 pour un
    /// lot de 100 — est EX-M11, et il est calculé par `crate::format`. Ce qui est
    /// compté **ici** est la taille annoncée par l'écrivain : `ecrire` ne
    /// consulte pas `Format`, ce que `crate::hors_perimetre()` déclare.
    pub octets: u32,
    /// Date de l'événement représenté, distincte de la date d'écriture — la
    /// distinction porte le filigrane et les volets d'EX-A06 (phase 5).
    pub date_evenement: Instant,
    /// M3 — vrai une fois l'accusé de durabilité reçu. Un enregistrement non
    /// durable n'est **pas** lisible.
    pub durable: bool,
    /// Auteur, **apposé par le milieu** à la réception à partir de l'identité de
    /// session — jamais lu dans la charge utile (EX-M24, PD14).
    ///
    /// C'est ce qui sépare un témoignage attribuable d'un témoignage anonyme. Le
    /// milieu n'évalue toujours pas le **contenu** : il garantit seulement qui a
    /// déposé. Une trace dont l'auteur serait déclaré par l'écrivain ne serait
    /// pas incomplète, elle serait fausse, et ni EX-A08 ni l'échantillonnage ne
    /// la corrigent (§6.2, p. 71).
    pub auteur: Identite,
}

/// Identité de session présentée à l'écriture, et dont le milieu tire le champ
/// [`Enregistrement::auteur`] (EX-M24).
///
/// La paire est délibérée. `agent` seul suffirait à attribuer ; `session` est ce
/// qui rend la **condition d'échec** exprimable — une identité partagée entre
/// plusieurs processus, ou un jeton réémis à un successeur, ramène au zombie du
/// §2.1 : le point de défaillance résiduel n'est pas le processus, c'est
/// l'identité.
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Debug, Default)]
pub struct Identite {
    /// Agent authentifié pour cette session.
    pub agent: ActeurId,
    /// Session. Deux processus sous une même session sont **indiscernables** du
    /// point de vue du milieu, et c'est le mode de défaillance à provoquer, pas
    /// à corriger.
    pub session: u64,
}

impl Identite {
    /// Identité d'un agent dans une session qui lui est propre — le cas nominal.
    pub fn propre(agent: ActeurId) -> Identite {
        Identite {
            agent,
            session: u64::from(agent.0),
        }
    }

    /// Identité **partagée** par plusieurs agents : le préréglage de la condition
    /// d'échec d'EX-M24 (NF-10).
    ///
    /// Le milieu appose ce qu'on lui présente ; il n'a aucun moyen de savoir que
    /// deux processus se présentent sous la même identité. C'est exactement ce
    /// que le mécanisme ne traite pas, et l'affichage le dit.
    pub fn partagee(agent: ActeurId, session: u64) -> Identite {
        Identite { agent, session }
    }
}

/// Taille par défaut d'un enregistrement du modèle, en octets : la charge utile
/// plus un en-tête minimal.
pub const OCTETS_DEFAUT: u32 = 32;

/// Octets ajoutés par l'identité apposée (EX-M24) : agent et session.
///
/// Ce n'est pas une mesure du traité — le tableau 22 écrit « quelques octets » —
/// mais la taille réelle des deux champs, `u32` et `u64`. Grandeur dérivée du
/// produit, et le comptage est séparé de celui de la charge utile.
pub const OCTETS_IDENTITE: u32 = 12;

/// Une écriture acceptée, avant son accusé de durabilité.
///
/// Le délai est rendu à l'appelant, qui planifie l'événement d'accusé sur le
/// moteur : M3 exige que l'accusé soit un **événement distinct** de l'écriture,
/// et `sim-milieu` ne pousse pas d'événement lui-même — il ne connaît pas le
/// type de charge du moteur (§5.1).
#[derive(Clone, Copy, Debug)]
pub struct Ecriture {
    /// Partition où l'enregistrement a été rangé.
    pub partition: u32,
    /// Position attribuée dans cette partition.
    pub decalage: u64,
    /// Délai avant l'accusé de durabilité. L'appelant en fait un événement.
    pub delai_durabilite: Duree,
}

/// Coûts du milieu (EX-M13).
///
/// Ces compteurs sont **distincts** du compte de messages point à point, que
/// tient `sim-agents` : le §1.1 les tient séparés, et le scénario A perd son
/// sens s'ils sont additionnés.
#[derive(Clone, Copy, Debug, Default)]
pub struct Couts {
    /// Nombre d'écritures acceptées.
    pub ecritures: u64,
    /// Volume écrit, en octets déclarés.
    pub octets_ecrits: u64,
    /// Nombre d'opérations de lecture, et non d'enregistrements lus.
    pub lectures: u64,
    /// Volume lu, en octets déclarés.
    pub octets_lus: u64,
    /// Un tour de journal : une écriture jusqu'à sa durabilité, ou une lecture.
    /// Le §1.3 chiffre une diffusion à « 2 tours de journal ».
    pub tours_journal: u64,
    /// Nombre de passes de compactage effectuées.
    pub compactages: u64,
    /// Enregistrements retirés par rétention ou par compactage.
    pub enregistrements_supprimes: u64,
    /// Octets d'identité apposés par le milieu (EX-M24), comptés **séparément**
    /// des octets de charge utile : c'est le prix de l'attribution, et le tableau
    /// 22 le chiffre à « quelques octets par enregistrement ; 0 message, 0 tour ».
    pub octets_identite: u64,
}

/// Politique de rétention (EX-M10, EX-M20).
///
/// **R est une grandeur unique à trois rôles** : évaporation par politique du
/// milieu (§1.2, §6.1), horizon de reconstruction causale (§6.2), et **horizon
/// réel de la détection** (§7.2). Elle est affichée une fois, et tout oracle
/// dont l'horizon la dépasse est refusé au chargement.
/// Le défaut est **sans rétention et sans compactage** : une politique qu'on
/// n'a pas demandée ne doit pas effacer d'enregistrements.
///
/// **Seule `fenetre` gouverne quoi que ce soit.** `Milieu::compacter` ne prend
/// pas de `Retention` et ne consulte aucune politique : appelé, il compacte. Le
/// champ `compacte` est donc une déclaration d'intention que rien ne lit, et
/// `crate::hors_perimetre()` le dit.
#[derive(Clone, Copy, Debug, Default)]
pub struct Retention {
    /// Fenêtre R, en tics. `None` = rétention illimitée.
    pub fenetre: Option<Duree>,
    /// Le sujet est-il compacté par clé ?
    pub compacte: bool,
}

impl Retention {
    /// Message de refus d'un oracle dont l'horizon dépasse R (EX-M20).
    pub fn refus_horizon(horizon: Duree, r: Duree) -> String {
        format!(
            "oracle refusé : horizon {} > R = {}. Au-delà de R, la propriété redevient \
             invérifiable ; R, non la sensibilité du détecteur, est l'horizon réel de la \
             détection (§6.1, §7.2).",
            horizon.0, r.0
        )
    }
}

/// Une partition : une suite ordonnée, et rien d'autre.
#[derive(Clone, Debug, Default)]
pub struct Partition {
    journal: Vec<Enregistrement>,
    prochain_decalage: u64,
    /// Vrai dès qu'un compactage a eu lieu : le sujet devient **impropre à la
    /// traçabilité** (EX-M10), et l'affichage doit le dire.
    compacte_au_moins_une_fois: bool,
    /// Enregistrements évaporés par la politique de rétention.
    pub evapores: u64,
}

impl Partition {
    /// M1 tient par construction : l'ajout se fait en queue, avec un décalage
    /// strictement croissant. L'oracle le vérifie tout de même — un invariant
    /// vrai par construction cesse de l'être à la première modification, et
    /// c'est exactement ce qu'un oracle armé en permanence protège.
    fn ajouter(
        &mut self,
        partition: u32,
        cle: Cle,
        valeur: f64,
        octets: u32,
        date_evenement: Instant,
        auteur: Identite,
    ) -> u64 {
        let decalage = self.prochain_decalage;
        self.prochain_decalage += 1;
        self.journal.push(Enregistrement {
            partition,
            decalage,
            cle,
            valeur,
            octets,
            date_evenement,
            durable: false,
            auteur,
        });
        decalage
    }

    /// Recherche **binaire** : le journal est trié par décalage (M1). Un
    /// balayage linéaire rendrait le coût d'une exécution quadratique en le
    /// nombre d'écritures, ce que NF-06 interdit — et c'était le cas ici, mesuré
    /// à 64 ms, 316 ms puis 1 405 ms pour n = 20 k, 40 k, 80 k validations.
    fn valider(&mut self, decalage: u64) -> bool {
        match self.journal.binary_search_by_key(&decalage, |e| e.decalage) {
            Ok(i) => {
                self.journal[i].durable = true;
                true
            }
            Err(_) => false,
        }
    }

    /// Tous les enregistrements de la partition, durables ou non, dans l'ordre
    /// des décalages.
    pub fn enregistrements(&self) -> &[Enregistrement] {
        &self.journal
    }

    /// Nombre d'enregistrements durables.
    pub fn durables(&self) -> usize {
        self.journal.iter().filter(|e| e.durable).count()
    }

    /// M1 — les décalages sont strictement croissants.
    fn m1_tient(&self) -> bool {
        self.journal.windows(2).all(|p| p[0].decalage < p[1].decalage)
    }

    /// EX-M10 — un sujet compacté est **impropre à la traçabilité**.
    ///
    /// Sa garantie est qu'un consommateur partant du début voit **au moins**
    /// l'état final de tous les enregistrements dans leur ordre d'écriture. Le
    /// mot « au moins » interdit d'en revendiquer l'unicité : la queue non
    /// compactée peut encore porter des doublons de clés.
    pub fn impropre_a_la_tracabilite(&self) -> Option<&'static str> {
        if self.compacte_au_moins_une_fois {
            Some(
                "sujet compacté — impropre à la traçabilité. Garantie : un consommateur partant \
                 du début voit AU MOINS l'état final de chaque clé, dans l'ordre d'écriture. \
                 « Au moins » interdit d'en revendiquer l'unicité (§6.1, tableau 17).",
            )
        } else {
            None
        }
    }
}

/// Le milieu.
pub struct Milieu {
    partitions: Vec<Partition>,
    /// Distribution du chemin écriture → durabilité. C'est une **entrée** du
    /// modèle, jamais une sortie (§8.3, EX-M09).
    pub latence: Latence,
    /// Unité du temps logique, héritée de la configuration (DT10).
    pub granularite: Granularite,
    couts: Couts,
    /// Latences mesurées du chemin écriture → durabilité (EX-M09).
    pub latences_durabilite: Mesures,
}

/// Noms des oracles armés par le milieu. Ce sont des `&'static str` parce que
/// le registre de `sim-core` les compare par identité de nom.
/// M1 — dans une partition, les décalages croissent strictement.
pub const M1: &str = "M1 — ordre total dans une partition";
/// M2 — entre deux partitions, il n'existe **aucun** ordre. Les comparer est
/// le mode de défaillance, pas une approximation.
pub const M2: &str = "M2 — aucun ordre entre partitions";
/// M3 — ce qui se lit est durable. Un enregistrement non accusé n'est pas
/// lisible, et c'est ce qui donne son prix au chemin de durabilité.
pub const M3: &str = "M3 — un enregistrement lu est durable";
/// M4 — le compactage retire, il ne réordonne jamais.
pub const M4: &str = "M4 — le compactage ne réordonne pas";
/// EX-M10 — après compactage, un consommateur partant du début voit **au moins**
/// l'état final de chaque clé qu'il voyait avant.
///
/// C'est la seule propriété qu'un compactage puisse réellement casser, et le
/// PRD écrit que « sa garantie est un oracle ». Elle ne l'était pas : elle
/// n'existait que comme chaîne d'affichage, et un défaut mesuré sur 36,5 % des
/// compactages tirés au sort laissait la suite de tests verte.
pub const M10: &str = "EX-M10 — le compactage préserve l'état final lisible";

impl Milieu {
    /// Milieu à `nb_partitions` partitions vides.
    pub fn nouveau(nb_partitions: u32, latence: Latence, granularite: Granularite) -> Milieu {
        Milieu {
            partitions: vec![Partition::default(); nb_partitions as usize],
            latence,
            granularite,
            couts: Couts::default(),
            latences_durabilite: Mesures::nouvelle(),
        }
    }

    /// Nombre de partitions. C'est le plafond de parallélisme du milieu.
    pub fn nb_partitions(&self) -> u32 {
        self.partitions.len() as u32
    }

    /// Une partition par son index.
    ///
    /// # Panics
    ///
    /// Si `p >= nb_partitions()`.
    pub fn partition(&self, p: u32) -> &Partition {
        &self.partitions[p as usize]
    }

    /// Les coûts propres du milieu (EX-M13), à ne jamais additionner à ceux du
    /// plan de contrôle ni aux messages point à point des agents.
    pub fn couts(&self) -> Couts {
        self.couts
    }

    /// Partition d'une clé — par hachage, comme le fait un courtier. C'est ce
    /// qui rend les clés chaudes possibles, et les clés chaudes sont la raison
    /// du rééquilibrage (EX-M19).
    pub fn partition_de(&self, cle: Cle) -> u32 {
        // Mélange multiplicatif de Fibonacci : déterministe, sans dépendance,
        // et sans table de hachage (PD1).
        //
        // `.max(1)` comme la fonction sœur de `groupe.rs` : `Milieu::nouveau(0,
        // …)` est constructible et n'assertit rien, et un modulo par zéro
        // paniquerait ici sans que la doc l'annonce.
        let h = cle.wrapping_mul(0x9e37_79b9_7f4a_7c15);
        ((h >> 32) % (self.partitions.len().max(1)) as u64) as u32
    }

    /// Écrit un enregistrement. Il n'est **pas** lisible tant que son accusé de
    /// durabilité n'est pas revenu (M3) : l'appelant doit planifier
    /// [`Milieu::valider`] à `maintenant + delai_durabilite`.
    pub fn ecrire(
        &mut self,
        partition: u32,
        cle: Cle,
        valeur: f64,
        date_evenement: Instant,
        identite: Identite,
        alea: &mut Alea,
    ) -> Ecriture {
        // EX-M24 — l'auteur vient de l'identité présentée à la réception, et
        // **jamais** de la charge utile. `valeur` est un f64 : il n'y a
        // structurellement aucune place pour un auteur déclaré, et c'est
        // volontaire — la charge utile n'a pas à être inspectée pour que
        // l'attribution soit vraie. Coût : 0 message, 0 tour, quelques octets.
        let decalage = self.partitions[partition as usize].ajouter(
            partition,
            cle,
            valeur,
            OCTETS_DEFAUT,
            date_evenement,
            identite,
        );
        self.couts.ecritures += 1;
        self.couts.octets_ecrits += OCTETS_DEFAUT as u64;
        self.couts.octets_identite += OCTETS_IDENTITE as u64;
        Ecriture {
            partition,
            decalage,
            delai_durabilite: self.latence.tirer(alea, self.granularite),
        }
    }

    /// Les identités qui se présentent sous une **même session** — condition
    /// d'échec d'EX-M24, constatée sur le journal plutôt que supposée.
    ///
    /// Le milieu ne peut pas l'empêcher : il appose ce qu'on lui présente. Il
    /// peut en revanche le **constater après coup**, et c'est la seule chose
    /// honnête à afficher. Une session vue avec deux agents distincts est le
    /// zombie du §2.1 revenu par la porte de l'identité.
    pub fn sessions_partagees(&self) -> Vec<(u64, Vec<ActeurId>)> {
        let mut par_session: BTreeMap<u64, BTreeSet<ActeurId>> = BTreeMap::new();
        for p in &self.partitions {
            for e in &p.journal {
                par_session
                    .entry(e.auteur.session)
                    .or_default()
                    .insert(e.auteur.agent);
            }
        }
        par_session
            .into_iter()
            .filter(|(_, agents)| agents.len() > 1)
            .map(|(s, agents)| (s, agents.into_iter().collect()))
            .collect()
    }

    /// Accuse la durabilité. Compte un tour de journal (EX-M13).
    pub fn valider(&mut self, e: Ecriture) -> bool {
        let ok = self.partitions[e.partition as usize].valider(e.decalage);
        if ok {
            self.couts.tours_journal += 1;
            self.latences_durabilite.ajouter(e.delai_durabilite);
        }
        ok
    }

    /// Lit une partition depuis un décalage. Ne rend que les enregistrements
    /// **durables** (M3), dans l'ordre du journal (M1).
    ///
    /// La lecture s'arrête au premier enregistrement non durable et ne saute
    /// rien : un consommateur lit séquentiellement, il ne pioche pas. Sauter un
    /// trou reviendrait à livrer les enregistrements dans un autre ordre que
    /// celui du journal, donc à casser M1 depuis le côté lecture.
    ///
    /// Le point de départ est trouvé par recherche binaire — le journal est
    /// trié par décalage, y compris après compactage. Un balayage linéaire
    /// rendrait chaque lecture proportionnelle à la taille du journal, et le
    /// coût d'une exécution quadratique en le nombre d'événements, ce que NF-06
    /// interdit.
    pub fn lire(&mut self, partition: u32, depuis: u64, max: usize) -> Vec<Enregistrement> {
        let journal = &self.partitions[partition as usize].journal;
        let debut = journal.partition_point(|e| e.decalage < depuis);
        let lus: Vec<Enregistrement> = journal[debut..]
            .iter()
            .take_while(|e| e.durable)
            .take(max)
            .cloned()
            .collect();
        self.couts.lectures += 1;
        self.couts.tours_journal += 1;
        self.couts.octets_lus += lus.iter().map(|e| e.octets as u64).sum::<u64>();
        lus
    }

    /// Lit plusieurs partitions, en **randomisant activement** l'ordre de
    /// livraison entre elles (EX-M02).
    ///
    /// C'est la part `[C]` d'EX-M02, et c'est une décision du produit et non un
    /// énoncé du traité : M2 dit qu'aucun ordre n'est garanti ; le simulateur va
    /// plus loin et fait en sorte qu'un agent qui en suppose un soit pris en
    /// défaut **par construction**. Un entrelacement stable serait un ordre de
    /// fait, et l'erreur resterait invisible jusqu'au jour où le courtier
    /// change d'humeur.
    ///
    /// L'ordre **à l'intérieur** de chaque partition reste celui du journal :
    /// M1 n'est pas touché.
    /// `budget_total` borne le nombre d'enregistrements rendus **toutes
    /// partitions confondues**, et non par partition : EX-A12 exige un
    /// intervalle borné du milieu, et une borne qui se multiplierait par le
    /// nombre de partitions n'en serait plus une.
    ///
    /// L'ordre des partitions étant tiré au sort à chaque appel, celle qui
    /// consomme le budget varie — un agent ne peut donc pas se reposer sur un
    /// ordre de service stable, ce qui est encore M2.
    pub fn lire_multi(
        &mut self,
        curseurs: &[(u32, u64)],
        budget_total: usize,
        alea: &mut Alea,
    ) -> Vec<Enregistrement> {
        let mut ordre: Vec<usize> = (0..curseurs.len()).collect();
        // Mélange de Fisher-Yates, tiré de l'unique générateur semé (PD1).
        for i in (1..ordre.len()).rev() {
            ordre.swap(i, alea.entier(i as u64 + 1) as usize);
        }
        let mut sortie = Vec::new();
        let mut reste = budget_total;
        for i in ordre {
            if reste == 0 {
                break;
            }
            let (p, depuis) = curseurs[i];
            let lus = self.lire(p, depuis, reste);
            reste -= lus.len().min(reste);
            sortie.extend(lus);
        }
        sortie
    }

    /// Compacte une partition : pour chaque clé, seul son dernier état est
    /// conservé (M4).
    ///
    /// La suppression ne réordonne rien — c'est l'invariant, et il est vérifié
    /// par [`Milieu::verifier_m4`] : la suite restante doit être une sous-suite
    /// de la suite d'origine, décalages inchangés.
    ///
    /// **Le compactage s'arrête à la frontière de durabilité.** Seule la fenêtre
    /// lisible — le préfixe durable, celui que [`Milieu::lire`] rend — est
    /// compactée ; la queue, à partir du premier enregistrement dont l'accusé
    /// n'est pas revenu, est laissée intacte.
    ///
    /// Sans cette borne, la garantie d'EX-M10 tombe. Elle dit qu'un consommateur
    /// partant du début voit **au moins** l'état final de chaque clé ; or
    /// remplacer un état durable par un successeur situé **derrière** un trou non
    /// durable ne le remplace pas, il le supprime — `lire` s'arrête au trou, et
    /// la clé n'a plus aucun état visible. Sur 5 000 compactages tirés au sort,
    /// 36,5 % des clés perdaient ainsi leur dernier état lisible, sans qu'aucun
    /// oracle ne s'arme.
    ///
    /// Compacter au-delà de la frontière n'aurait de toute façon pas de sens :
    /// un enregistrement non encore accusé n'est pas un état, c'est une écriture
    /// en cours.
    pub fn compacter(&mut self, partition: u32) -> Vec<Enregistrement> {
        let p = &mut self.partitions[partition as usize];
        let avant = p.journal.clone();

        // La frontière : indice du premier non durable, ou la fin.
        let frontiere = p
            .journal
            .iter()
            .position(|e| !e.durable)
            .unwrap_or(p.journal.len());

        // Dernier enregistrement par clé **dans la fenêtre lisible**, plus toute
        // la queue. Parcours en arrière, conservation du premier vu : aucun tri,
        // donc aucune occasion de réordonner.
        //
        // `BTreeSet` et non `Vec` + `contains` : ce dernier rendait le
        // compactage quadratique en le nombre de clés distinctes — 1,0 ms à
        // 5 000 enregistrements, 120 ms à 40 000 — dans la fonction même où
        // NF-06 venait d'être réparée côté `valider`. `HashSet` est interdit par
        // `clippy.toml` (PD1).
        let mut garder = vec![false; p.journal.len()];
        let mut cles_vues: BTreeSet<Cle> = BTreeSet::new();
        for i in (frontiere..p.journal.len()).rev() {
            garder[i] = true;
        }
        for i in (0..frontiere).rev() {
            if cles_vues.insert(p.journal[i].cle) {
                garder[i] = true;
            }
        }
        let mut k = 0;
        p.journal.retain(|_| {
            let g = garder[k];
            k += 1;
            g
        });

        p.compacte_au_moins_une_fois = true;
        let supprimes = (avant.len() - p.journal.len()) as u64;
        self.couts.compactages += 1;
        self.couts.enregistrements_supprimes += supprimes;
        avant
    }

    /// EX-M10, EX-M20 — applique la rétention : les enregistrements dont la date
    /// **d'événement** est antérieure à `maintenant − R` s'évaporent.
    ///
    /// La suppression se fait **en tête**, sans réordonner : c'est M4 appliqué
    /// à la politique de rétention comme il l'est au compactage. Elle s'arrête
    /// donc au premier enregistrement à garder — un enregistrement récent
    /// protège tous ceux qui le suivent, même vieux.
    ///
    /// C'est une conséquence de la grandeur choisie, et elle est assumée :
    /// `date_evenement` est la date de **l'événement représenté**, pas celle de
    /// l'écriture (le journal ne stocke pas cette dernière), et elle n'a aucune
    /// raison d'être croissante — un rejeu d'événements anciens la fait
    /// décroître. Un `partition_point` sur ce prédicat serait une recherche
    /// binaire sur une suite non partitionnée : le résultat dépendrait de
    /// l'endroit où la binaire atterrit, pas de la politique. C'est un balayage,
    /// linéaire en ce qu'il supprime.
    pub fn appliquer_retention(&mut self, partition: u32, maintenant: Instant, r: Duree) -> u64 {
        let limite = Instant(maintenant.0.saturating_sub(r.0));
        let p = &mut self.partitions[partition as usize];
        let avant = p.journal.len();
        let garder = p
            .journal
            .iter()
            .position(|e| !(e.date_evenement < limite && e.durable))
            .unwrap_or(p.journal.len());
        p.journal.drain(..garder);
        let evapores = (avant - p.journal.len()) as u64;
        p.evapores += evapores;
        // EX-M13 : le libellé du compteur dit « par rétention **ou** par
        // compactage ». Seul le compactage l'alimentait.
        self.couts.enregistrements_supprimes += evapores;
        evapores
    }

    /// EX-M20 — refuse un oracle dont l'horizon dépasse R. Au-delà, la
    /// propriété redevient invérifiable, et c'est R — non la sensibilité du
    /// détecteur — qui est l'horizon réel de la détection.
    pub fn verifier_horizon(horizon: Duree, retention: &Retention) -> Result<(), String> {
        match retention.fenetre {
            Some(r) if horizon > r => Err(Retention::refus_horizon(horizon, r)),
            _ => Ok(()),
        }
    }

    /// Arme les oracles du milieu (NF-11 : activables en permanence dans les
    /// tests, coûteux mais exacts).
    ///
    /// M2 n'est pas un oracle de la même nature que les autres : il n'énonce
    /// pas ce qui doit tenir, mais ce qui n'est **pas** garanti. Il est armé
    /// quand même, et ce qu'il vérifie est que le simulateur randomise
    /// effectivement — un entrelacement devenu stable serait une régression.
    pub fn armer_oracles(&self, registre: &mut Registre) {
        registre.armer(Oracle::surete(M1, "§1.2, p. 13"));
        registre.armer(Oracle::surete(M2, "§1.2, p. 13"));
        registre.armer(Oracle::surete(M3, "§1.2, p. 13"));
        registre.armer(Oracle::surete(M4, "§1.2, p. 13"));
        registre.armer(Oracle::surete(M10, "§6.1, tableau 17"));
    }

    /// Vérifie **M1** sur l'état courant. Une violation arrête l'exécution
    /// (EX-C09).
    ///
    /// **M1 seul**, et le nom de la méthode ne prétend plus autre chose. M3 et
    /// M2 n'ont pas de prédicat d'état falsifiable :
    ///
    /// - M3 — « un enregistrement lu est durable » — est tenu par la
    ///   **définition** de [`Milieu::lire`], qui s'arrête au premier non durable.
    ///   Tout prédicat écrit sur la fenêtre lisible serait une tautologie : sur
    ///   les 131 071 motifs de durabilité possibles à n ≤ 16, aucun ne le
    ///   déclencherait. Ce qui garde M3 est le test qui provoque le cas, pas un
    ///   oracle armé.
    /// - M2 énonce une **absence** de garantie. Ce que le simulateur doit tenir
    ///   est que l'entrelacement reste randomisé, ce qu'établit un test unitaire.
    ///
    /// Aucun des deux ne se réfute donc sur une trace finie, et c'est pourquoi
    /// leur prédicat n'existe pas. La propriété qui, elle, est falsifiable et
    /// qu'un compactage peut casser est EX-M10 : voir [`Milieu::verifier_m10`].
    ///
    /// **Cette méthode n'a aucun appelant hors test**, non plus que
    /// `verifier_m4` et `verifier_m10` : `crate::hors_perimetre()` le déclare.
    /// M1 à M4 et M10 sont armés à chaque exécution du scénario B, et aucune
    /// exécution n'évalue leur prédicat.
    pub fn verifier(&self, registre: &mut Registre, maintenant: Instant) {
        for (i, p) in self.partitions.iter().enumerate() {
            if !p.m1_tient() {
                registre.violer(M1, maintenant, format!("partition {i} : décalages non croissants"));
            }
        }
    }

    /// EX-M10 — après compactage, chaque clé qui avait un état lisible en a
    /// toujours un, et c'est le **dernier** qu'elle avait.
    ///
    /// À appeler comme [`Milieu::verifier_m4`], avec la suite d'avant. Les deux
    /// sont complémentaires et aucun ne remplace l'autre : M4 regarde les
    /// décalages, celui-ci regarde ce que le consommateur voit. Un compactage
    /// qui remplace un état durable par un successeur situé derrière un trou non
    /// durable satisfait M4 — la sous-suite est intacte — et casse EX-M10.
    pub fn verifier_m10(
        &self,
        partition: u32,
        avant: &[Enregistrement],
        registre: &mut Registre,
        maintenant: Instant,
    ) {
        let lisible_de = |journal: &[Enregistrement]| -> Vec<(Cle, f64)> {
            let mut vus: Vec<(Cle, f64)> = Vec::new();
            for e in journal.iter().take_while(|e| e.durable) {
                match vus.iter_mut().find(|(c, _)| *c == e.cle) {
                    Some(v) => v.1 = e.valeur,
                    None => vus.push((e.cle, e.valeur)),
                }
            }
            vus
        };
        let etats_avant = lisible_de(avant);
        let etats_apres = lisible_de(&self.partitions[partition as usize].journal);

        for (cle, valeur) in etats_avant {
            match etats_apres.iter().find(|(c, _)| *c == cle) {
                Some((_, v)) if *v == valeur => {}
                Some((_, v)) => registre.violer(
                    M10,
                    maintenant,
                    format!(
                        "partition {partition} : la clé {cle} lisait {valeur} avant le \
                         compactage et lit {v} après"
                    ),
                ),
                None => registre.violer(
                    M10,
                    maintenant,
                    format!(
                        "partition {partition} : la clé {cle} avait l'état final lisible \
                         {valeur} et n'a plus aucun état lisible après le compactage"
                    ),
                ),
            }
        }
    }

    /// M4 — la suite d'après compactage est une sous-suite de celle d'avant,
    /// décalages inchangés et ordre préservé.
    pub fn verifier_m4(
        &self,
        partition: u32,
        avant: &[Enregistrement],
        registre: &mut Registre,
        maintenant: Instant,
    ) {
        let apres = &self.partitions[partition as usize].journal;
        let mut i = 0;
        for e in apres {
            match avant[i..].iter().position(|a| a.decalage == e.decalage) {
                Some(pos) => i += pos + 1,
                None => {
                    registre.violer(
                        M4,
                        maintenant,
                        format!(
                            "partition {partition} : décalage {} apparu ou déplacé par le \
                             compactage",
                            e.decalage
                        ),
                    );
                    return;
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use sim_core::temps::Granularite;

    fn milieu(p: u32) -> Milieu {
        Milieu::nouveau(p, Latence::fixe(20.0), Granularite::Micro)
    }

    fn ecrire_et_valider(m: &mut Milieu, p: u32, cle: Cle, v: u8, alea: &mut Alea) {
        let e = m.ecrire(p, cle, v as f64, Instant(0), Identite::propre(ActeurId(0)), alea);
        m.valider(e);
    }

    /// EX-M01 — l'ordre est total dans une partition, quelle que soit l'ordre
    /// d'arrivée des clés.
    #[test]
    fn m1_lordre_est_total_dans_une_partition() {
        let mut m = milieu(1);
        let mut alea = Alea::nouveau(1);
        for i in 0..100u8 {
            ecrire_et_valider(&mut m, 0, (i % 7) as Cle, i, &mut alea);
        }
        let lus = m.lire(0, 0, 1_000);
        assert_eq!(lus.len(), 100);
        for (i, e) in lus.iter().enumerate() {
            assert_eq!(e.decalage, i as u64);
        }
        let mut r = Registre::nouveau();
        m.armer_oracles(&mut r);
        m.verifier(&mut r, Instant(0));
        assert!(r.violations().is_empty());
    }

    /// EX-M03 — un enregistrement écrit n'est pas lisible avant son accusé de
    /// durabilité. L'accusé est un événement distinct, séparé par une latence.
    #[test]
    fn m3_un_enregistrement_non_valide_nest_pas_lisible() {
        let mut m = milieu(1);
        let mut alea = Alea::nouveau(2);
        let e = m.ecrire(0, 1, 9.0, Instant(0), Identite::propre(ActeurId(0)), &mut alea);
        assert!(e.delai_durabilite > Duree(0), "l'accusé est séparé par une latence");
        assert!(m.lire(0, 0, 10).is_empty(), "non durable, donc non lisible");
        assert!(m.valider(e));
        assert_eq!(m.lire(0, 0, 10).len(), 1);
    }

    /// EX-M02 — l'entrelacement entre partitions est **activement randomisé**.
    /// Un ordre stable serait un ordre de fait, et un agent qui s'y fierait ne
    /// serait jamais pris en défaut ici — pour l'être en production.
    #[test]
    fn m2_lentrelacement_entre_partitions_est_randomise() {
        let mut m = milieu(4);
        let mut alea = Alea::nouveau(3);
        for p in 0..4u32 {
            for i in 0..5u8 {
                ecrire_et_valider(&mut m, p, p as Cle * 100 + i as Cle, i, &mut alea);
            }
        }
        let curseurs: Vec<(u32, u64)> = (0..4).map(|p| (p, 0)).collect();
        let mut premieres_cles = Vec::new();
        for _ in 0..50 {
            let lus = m.lire_multi(&curseurs, 20, &mut alea);
            premieres_cles.push(lus[0].cle / 100);
        }
        let distinctes: Vec<u64> = {
            let mut d = premieres_cles.clone();
            d.sort_unstable();
            d.dedup();
            d
        };
        assert!(
            distinctes.len() >= 3,
            "seulement {} partitions ont ouvert la lecture : l'entrelacement est trop stable",
            distinctes.len()
        );
    }

    /// M1 survit à la randomisation de M2 : à l'intérieur d'une partition,
    /// l'ordre reste total. Les deux invariants ne se contredisent pas.
    #[test]
    fn m2_ne_casse_pas_m1() {
        let mut m = milieu(3);
        let mut alea = Alea::nouveau(4);
        for p in 0..3u32 {
            for i in 0..6u8 {
                ecrire_et_valider(&mut m, p, i as Cle, i, &mut alea);
            }
        }
        let curseurs: Vec<(u32, u64)> = (0..3).map(|p| (p, 0)).collect();
        // Budget **total** : 18 pour trois partitions de six.
        let lus = m.lire_multi(&curseurs, 18, &mut alea);
        assert_eq!(lus.len(), 18);

        // La sortie est faite de trois blocs contigus, un par partition, dans un
        // ordre inter-partitions quelconque. À l'intérieur de chaque bloc, les
        // décalages sont strictement croissants : M1 tient malgré M2.
        for bloc in lus.chunks(6) {
            let decalages: Vec<u64> = bloc.iter().map(|e| e.decalage).collect();
            assert_eq!(decalages, (0..6).collect::<Vec<u64>>());
        }
    }

    /// EX-M04 — le compactage supprime, il ne réordonne pas.
    #[test]
    fn m4_le_compactage_ne_reordonne_pas() {
        let mut m = milieu(1);
        let mut alea = Alea::nouveau(5);
        // Trois clés, réécrites dans un ordre entrelacé.
        for (cle, v) in [(1u64, 10u8), (2, 20), (1, 11), (3, 30), (2, 21), (1, 12)] {
            ecrire_et_valider(&mut m, 0, cle, v, &mut alea);
        }
        let avant = m.compacter(0);
        let apres = m.partition(0).enregistrements().to_vec();

        // Une seule valeur par clé, la dernière.
        assert_eq!(apres.len(), 3);
        assert_eq!(apres[0].cle, 3);
        assert_eq!(apres[1].cle, 2);
        assert_eq!(apres[2].cle, 1);
        assert_eq!(apres[2].valeur, 12.0);

        // Décalages strictement croissants, donc ordre préservé.
        assert!(apres.windows(2).all(|w| w[0].decalage < w[1].decalage));

        let mut r = Registre::nouveau();
        m.armer_oracles(&mut r);
        m.verifier_m4(0, &avant, &mut r, Instant(0));
        assert!(r.violations().is_empty(), "{:?}", r.violations());
    }

    /// L'oracle M4 doit **détecter** un réordonnancement, sans quoi il ne
    /// protège rien (NF-10 : le mode de défaillance se provoque).
    #[test]
    fn m4_detecte_un_reordonnancement() {
        let mut m = milieu(1);
        let mut alea = Alea::nouveau(6);
        for i in 0..4u8 {
            ecrire_et_valider(&mut m, 0, i as Cle, i, &mut alea);
        }
        let avant = m.partition(0).enregistrements().to_vec();
        // On fabrique un « après » inversé, tel qu'un compactage fautif le
        // produirait, et on vérifie que l'oracle le voit.
        let mut inverse = m;
        inverse.partitions[0].journal.reverse();
        let mut r = Registre::nouveau();
        inverse.armer_oracles(&mut r);
        inverse.verifier_m4(0, &avant, &mut r, Instant(7));
        assert_eq!(r.violations().len(), 1);
        assert_eq!(r.violations()[0].oracle, M4);
    }

    /// EX-M13 — le milieu expose son coût, et les tours de journal se comptent.
    #[test]
    fn les_couts_du_milieu_se_comptent() {
        let mut m = milieu(1);
        let mut alea = Alea::nouveau(7);
        for i in 0..10u8 {
            ecrire_et_valider(&mut m, 0, i as Cle, i, &mut alea);
        }
        m.lire(0, 0, 100);
        let c = m.couts();
        assert_eq!(c.ecritures, 10);
        // 10 accusés de durabilité + 1 lecture = 11 tours de journal.
        assert_eq!(c.tours_journal, 11);
        assert_eq!(c.lectures, 1);
        assert!(c.octets_lus > 0);
    }

    /// EX-M09 — le ℓ₉₉ du chemin de durabilité est mesuré et extrait.
    #[test]
    fn le_l99_de_durabilite_est_mesure() {
        let mut m = Milieu::nouveau(1, Latence::depuis_l99(20.0), Granularite::Micro);
        let mut alea = Alea::nouveau(8);
        for i in 0..20_000u32 {
            let e = m.ecrire(0, i as Cle, 0.0, Instant(0), Identite::propre(ActeurId(0)), &mut alea);
            m.valider(e);
        }
        let l99 = m.latences_durabilite.l99().unwrap();
        let ms = Granularite::Micro.ms_depuis_tics(l99);
        assert!((ms - 20.0).abs() < 2.0, "ℓ₉₉ mesuré {ms:.2} ms");
    }

    /// EX-M10 — un sujet compacté se déclare impropre à la traçabilité, et sa
    /// garantie porte le mot « au moins ».
    #[test]
    fn un_sujet_compacte_est_impropre_a_la_tracabilite() {
        let mut m = milieu(1);
        let mut alea = Alea::nouveau(10);
        assert!(m.partition(0).impropre_a_la_tracabilite().is_none());
        for (cle, v) in [(1u64, 1u8), (1, 2)] {
            ecrire_et_valider(&mut m, 0, cle, v, &mut alea);
        }
        m.compacter(0);
        let avis = m.partition(0).impropre_a_la_tracabilite().unwrap();
        assert!(avis.contains("AU MOINS"), "{avis}");
        assert!(avis.contains("interdit d'en revendiquer l'unicité"), "{avis}");
    }

    /// EX-M20 — la rétention évapore la tête du journal, sans réordonner.
    #[test]
    fn la_retention_evapore_la_tete_sans_reordonner() {
        let mut m = milieu(1);
        let mut alea = Alea::nouveau(11);
        for i in 0..10u8 {
            let e = m.ecrire(
                0,
                i as Cle,
                i as f64,
                Instant(i as u64 * 100),
                Identite::propre(ActeurId(0)),
                &mut alea,
            );
            m.valider(e);
        }
        let evapores = m.appliquer_retention(0, Instant(1_000), Duree(500));
        assert!(evapores > 0, "rien n'a été évaporé");
        let restants = m.partition(0).enregistrements();
        assert!(restants.windows(2).all(|w| w[0].decalage < w[1].decalage));
        assert!(restants.iter().all(|e| e.date_evenement >= Instant(500)));
    }

    /// EX-M20 — un oracle dont l'horizon dépasse R est refusé, avec la phrase
    /// qui dit pourquoi.
    #[test]
    fn un_oracle_au_dela_de_r_est_refuse() {
        let r = Retention {
            fenetre: Some(Duree(1_000)),
            compacte: false,
        };
        assert!(Milieu::verifier_horizon(Duree(999), &r).is_ok());
        let e = Milieu::verifier_horizon(Duree(1_001), &r).unwrap_err();
        assert!(e.contains("horizon réel de la détection"), "{e}");
        // Sans rétention, aucun horizon n'est refusé.
        assert!(Milieu::verifier_horizon(Duree(u64::MAX), &Retention::default()).is_ok());
    }

    #[test]
    fn les_cles_se_repartissent_sur_les_partitions() {
        let m = milieu(8);
        let mut vues = vec![0u32; 8];
        for cle in 0..2_000u64 {
            vues[m.partition_de(cle) as usize] += 1;
        }
        assert!(vues.iter().all(|&n| n > 100), "{vues:?}");
    }
}
