//! Le soupçon, l'époque et le bail (EX-A23, EX-A24, EX-A33, EX-A41).
//!
//! > Un robot mort reste mort et reste sur place ; un agent logiciel soupçonné
//! > mort peut revenir avec son état d'avant et écrire. (§4.3)
//!
//! C'est l'écart entre arrêt franc et arrêt-reprise qui impose l'époque et le
//! bail : les lignes 7 à 10 de l'algorithme 4.3 n'ont **aucun équivalent** dans
//! les protocoles robotiques dont elles descendent.

use sim_core::alea::Alea;
use sim_core::horloge::{Domaines, Horloges};
use sim_core::temps::{Duree, Instant};
use sim_core::ActeurId;

// ---------------------------------------------------------------------------
// EX-A23 — détecteur de style infectieux
// ---------------------------------------------------------------------------

/// Verdict d'un cycle de détection.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum Verdict {
    /// L'acquittement direct est revenu.
    Sain,
    /// Le sondage indirect a confirmé : la cible est suspectée.
    Suspect,
    /// Le sondage indirect a démenti : c'était le lien, pas l'agent.
    LienFautif,
}

/// Coût d'un cycle, compté en messages et en tours.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub struct Cout {
    /// Messages échangés.
    pub messages: u64,
    /// Tours en série.
    pub tours: u64,
}

/// **EX-A23** — détecteur de style infectieux.
///
/// **Deux paramètres seulement** — période de protocole et taille du
/// sous-groupe — et des horloges non synchronisées. Le mode « battement de
/// cœur » est disponible comme terme de comparaison, sa charge croissant
/// quadratiquement avec la taille du groupe.
#[derive(Clone, Debug)]
pub struct DetecteurInfectieux {
    /// Taille du groupe surveillé.
    pub n: u32,
    /// Période de protocole. Premier des deux seuls paramètres.
    pub periode: Duree,
    /// Taille `s` du sous-groupe de sondage indirect. Second, et dernier.
    ///
    /// Noté `k` dans la source, renommé `s` ici : la lettre `k` est réservée au
    /// facteur de réplication.
    pub s: u8,
    /// Extension par suspicion : réduit les fausses détections, **ne les annule
    /// pas**.
    pub suspicion: bool,
    /// Mode battement de cœur — terme de comparaison, charge en n².
    pub battement_de_coeur: bool,
    /// Coût cumulé du détecteur.
    pub cout: Cout,
    /// Soupçons émis, vrais ou faux.
    pub suspicions: u64,
    /// Soupçons portant sur un agent **sain**. Ce compteur est **calculé**,
    /// jamais paramétré (PD12) : c'est de lui que sort le taux de fausses
    /// suspicions.
    pub fausses_suspicions: u64,
    /// Cycles où le sondage indirect a démenti le soupçon direct.
    pub liens_fautifs_detectes: u64,
}

impl DetecteurInfectieux {
    /// Détecteur à deux paramètres — période et taille du sous-groupe — avec
    /// l'extension par suspicion active.
    pub fn nouveau(n: u32, periode: Duree, s: u8) -> DetecteurInfectieux {
        DetecteurInfectieux {
            n,
            periode,
            s,
            suspicion: true,
            battement_de_coeur: false,
            cout: Cout::default(),
            suspicions: 0,
            fausses_suspicions: 0,
            liens_fautifs_detectes: 0,
        }
    }

    /// Coût nominal : **2 messages et 1 tour**.
    pub fn cout_nominal(&self) -> Cout {
        if self.battement_de_coeur {
            // Charge quadratique : chaque membre bat vers tous les autres.
            // `saturating_sub` : `n` est un champ public, et `n = 0` faisait
            // paniquer en debug puis s'enrouler en release — le cycle de
            // suspicion affichait alors le coût du mode infectieux.
            Cout {
                messages: u64::from(self.n) * u64::from(self.n).saturating_sub(1),
                tours: 1,
            }
        } else {
            Cout {
                messages: 2,
                tours: 1,
            }
        }
    }

    /// Coût d'un cycle de suspicion : **au plus 2 + 4s messages et 3 tours**.
    pub fn cout_suspicion(&self) -> Cout {
        Cout {
            messages: 2 + 4 * self.s as u64,
            tours: 3,
        }
    }

    /// Un cycle de détection sur `cible`.
    ///
    /// `vivant` et `lien_coupe` sont connus du moteur ; le détecteur, lui, ne
    /// voit qu'une absence d'acquittement. `domaines` sert à décider si les `s`
    /// pairs partagent le lien fautif — **condition que le protocole ne vérifie
    /// pas** et qu'EX-C14 rend fausse à volonté.
    pub fn cycle(
        &mut self,
        cible: ActeurId,
        vivant: bool,
        lien_coupe: bool,
        domaines: &Domaines,
        alea: &mut Alea,
    ) -> Verdict {
        let nominal = self.cout_nominal();
        self.cout.messages += nominal.messages;
        self.cout.tours += nominal.tours;

        // Le ping direct passe si l'agent vit et que le lien tient.
        if vivant && !lien_coupe {
            return Verdict::Sain;
        }

        // Sondage indirect : s pairs tirés au hasard. Le coût nominal est déjà
        // facturé ci-dessus ; on ajoute le **supplément**, saturé à zéro.
        //
        // En mode battement de cœur, le nominal vaut n(n−1) et dépasse le coût
        // de suspicion dès n = 10 : la soustraction nue paniquait en debug et
        // s'enroulait en release, effaçant la charge quadratique que le scénario
        // J doit précisément montrer — le compteur retombait sur celui du mode
        // infectieux.
        let indirect = self.cout_suspicion();
        self.cout.messages += indirect.messages.saturating_sub(nominal.messages);
        self.cout.tours += indirect.tours.saturating_sub(nominal.tours);

        let mut pairs: Vec<u32> = Vec::with_capacity(self.s as usize);
        for _ in 0..self.s {
            let p = alea.entier(self.n as u64) as u32;
            if p != cible.0 && !pairs.contains(&p) {
                pairs.push(p);
            }
        }

        // Le sondage indirect distingue la perte d'un lien de la mort d'un
        // agent **si et seulement si** les s pairs ne partagent pas le lien
        // fautif. Le protocole ne vérifie pas cette condition.
        let mut avec_cible = pairs.clone();
        avec_cible.push(cible.0);
        let partagent = domaines.partagent(&avec_cible);

        if !vivant {
            self.suspicions += 1;
            return Verdict::Suspect;
        }
        // L'agent vit : seul le lien est coupé.
        if partagent {
            // Les pairs sont derrière la même dépendance : ils confirment le
            // faux soupçon.
            self.suspicions += 1;
            self.fausses_suspicions += 1;
            Verdict::Suspect
        } else {
            self.liens_fautifs_detectes += 1;
            Verdict::LienFautif
        }
    }

    /// Complétude dérivée (§7.3, p. 112, 4ᵉ éd.) : détection entre `(seuil−1)·période +
    /// expiration` et une période de plus.
    ///
    /// C'est **le §7.3 qui dérive cet encadrement**, et non le §4.3 (p. 70, 4ᵉ éd.), qui
    /// ne donne que le majorant de 30 s : « un arrêt survenu juste après une sonde
    /// réussie n'est observé qu'au sondage suivant, entre 0 et 10 s plus tard,
    /// puis exige deux échecs supplémentaires à 10 s d'intervalle, plus 1 s de
    /// délai d'expiration, d'où une détection comprise entre 21 s et 31 s ».
    ///
    /// Aux défauts documentés — 10 s de période, 1 s d'expiration, 3 échecs —
    /// cela donne **21 à 31 s**, et NF-15 exige qu'un test le retrouve.
    ///
    /// `seuil = 0` est **refusé**, et non ramené à 1 : la dérivation du §7.3
    /// compte `seuil − 1` intervalles entre échecs, et à zéro échec il n'y a
    /// pas de détection dont on encadre le délai. Un écrêtage silencieux
    /// rendrait `(1 s, 11 s)` — un encadrement d'allure plausible que rien ne
    /// distingue d'une mesure, ce qui est pire qu'un débordement (SPEC §7,
    /// clause 4 : « une configuration invalide est un refus rendu à l'appelant,
    /// jamais un abandon »). C'est l'arbitrage que `sim_core::detecteur` et
    /// `crate::cycle_de_vie::retirer` tiennent aussi, sur la même dérivation.
    ///
    /// Le produit **sature**, pour la raison qui vaut dans les trois : le profil
    /// release du dépôt ne pose pas `overflow-checks`, et une période proche de
    /// 2⁶⁴ rendrait sinon un encadrement enroulé, c'est-à-dire une détection
    /// annoncée instantanée là où elle est la plus lente.
    pub fn completude(
        periode_s: u64,
        expiration_s: u64,
        seuil: u32,
    ) -> Result<(Duree, Duree), String> {
        if seuil == 0 {
            return Err(
                "seuil d'échec nul refusé : l'encadrement du §7.3 compte les intervalles entre \
                 `seuil` échecs consécutifs, et à zéro échec il n'y a pas de détection à encadrer. \
                 Le délai rendu serait une valeur d'allure plausible sans mesure derrière."
                    .to_string(),
            );
        }
        let min = Duree(
            periode_s
                .saturating_mul(u64::from(seuil - 1))
                .saturating_add(expiration_s),
        );
        Ok((min, Duree(min.0.saturating_add(periode_s))))
    }
}

// ---------------------------------------------------------------------------
// EX-A33 — bail de quorum
// ---------------------------------------------------------------------------

/// **Clause (1) d'EX-A33** — la politique d'expiration est un **choix binaire
/// déclaré, sans valeur par défaut**. Le simulateur refuse de démarrer si elle
/// n'est pas posée.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum PolitiqueExpiration {
    /// Défaut sûr pour la disponibilité et **catastrophique pour la sécurité** :
    /// un adversaire capable d'induire une partition obtient la levée des
    /// confinements.
    Relacher,
    /// Préserve la sécurité et **transforme toute partition réseau en panne
    /// durable**.
    Maintenir,
}

impl PolitiqueExpiration {
    /// Ce que la politique produit. Les deux ont une conséquence grave ; ce
    /// qui est fautif est de subir l'une sans l'avoir choisie.
    pub fn consequence(self) -> &'static str {
        match self {
            PolitiqueExpiration::Relacher => {
                "défaut sûr pour la disponibilité, CATASTROPHIQUE pour la sécurité : un \
                 adversaire capable d'induire une partition obtient la levée des confinements"
            }
            PolitiqueExpiration::Maintenir => {
                "préserve la sécurité et transforme TOUTE partition réseau en panne durable"
            }
        }
    }

    /// La règle affichée avec le choix.
    pub const LIBELLE: &'static str =
        "le choix doit être posé dans la politique plutôt que subi comme valeur par défaut d'une \
         bibliothèque (§7.2)";
}

/// **EX-A33** — le bail de quorum, **un mécanisme, deux emplois** : `q ≥ 2` pour
/// le jeton de confinement (§7.2), `q = 1` pour le prêt bilatéral entre plans
/// (§7.3). Une seule implantation, conformément à PD7.
#[derive(Clone, Debug)]
pub struct Bail {
    /// Taille du quorum.
    pub q: u32,
    /// Durée D du bail.
    pub d: Duree,
    /// ε **supposé** par le mécanisme. Distinct de l'ε_vrai des horloges.
    pub epsilon_suppose: Duree,
    /// Δ supposé sur le réseau.
    pub delta: Duree,
    /// Ce qui arrive quand le bail expire sans pouvoir être renouvelé.
    pub politique: PolitiqueExpiration,
    /// Détenteur courant et échéance.
    detenteur: Option<(ActeurId, Instant)>,
    /// Messages consommés par le bail.
    pub messages: u64,
    /// Tours consommés.
    pub tours: u64,
    /// Renouvellements accordés.
    pub renouvellements: u64,
    /// Nombre de fois où deux détenteurs ont existé simultanément **sans que
    /// personne ne l'observe**. C'est le troisième mode, et il est invisible.
    pub doubles_detentions: u64,
}

impl Bail {
    /// Construit le bail. **La politique d'expiration est obligatoire** : il n'y
    /// a pas de constructeur qui l'omette (clause 1).
    pub fn nouveau(
        q: u32,
        d: Duree,
        epsilon_suppose: Duree,
        delta: Duree,
        politique: PolitiqueExpiration,
    ) -> Bail {
        Bail {
            q,
            d,
            epsilon_suppose,
            delta,
            politique,
            detenteur: None,
            messages: 0,
            tours: 0,
            renouvellements: 0,
            doubles_detentions: 0,
        }
    }

    /// Étape (1) : demander le bail à un quorum de taille q — **2q messages et
    /// 1 tour**.
    pub fn demander(&mut self, agent: ActeurId, maintenant: Instant) -> Option<Instant> {
        self.messages += 2 * self.q as u64;
        self.tours += 1;
        match self.detenteur {
            Some((autre, echeance)) if autre != agent && maintenant < echeance => None,
            _ => {
                let echeance = maintenant + self.d;
                self.detenteur = Some((agent, echeance));
                Some(echeance)
            }
        }
    }

    /// Étape (3) : renouveler avant `D − ε − Δ`. Chaque renouvellement coûte à
    /// nouveau 2q messages et 1 tour.
    pub fn renouveler(&mut self, agent: ActeurId, maintenant: Instant) -> Option<Instant> {
        self.messages += 2 * self.q as u64;
        self.tours += 1;
        self.renouvellements += 1;
        match self.detenteur {
            Some((d, _)) if d == agent => {
                let echeance = maintenant + self.d;
                self.detenteur = Some((agent, echeance));
                Some(echeance)
            }
            _ => None,
        }
    }

    /// Instant avant lequel il faut renouveler : `D − ε − Δ`.
    pub fn limite_de_renouvellement(&self, obtenu_a: Instant) -> Instant {
        Instant(
            (obtenu_a.0 + self.d.0)
                .saturating_sub(self.epsilon_suppose.0)
                .saturating_sub(self.delta.0),
        )
    }

    /// Étape (4) : **condition d'arrêt locale**, donc terminante sans accord.
    /// L'agent cesse dès que son échéance corrigée est atteinte.
    pub fn doit_ceder(&self, agent: ActeurId, maintenant: Instant) -> bool {
        match self.detenteur {
            Some((d, echeance)) if d == agent => maintenant >= echeance,
            _ => true,
        }
    }

    /// **Coût par observation : nul.** C'est ce qui distingue le bail d'un
    /// accord par action.
    pub const COUT_PAR_OBSERVATION: u64 = 0;

    /// Coût par action : Θ(q) messages et 2 tours.
    pub fn cout_par_action(&self) -> Cout {
        Cout {
            messages: 2 * self.q as u64,
            tours: 2,
        }
    }

    /// **Clause (2) — le troisième mode est invisible, et c'est le point.**
    ///
    /// Si la dérive réelle dépasse l'ε supposé, le détenteur croit son bail
    /// vivant alors que le quorum l'a réattribué. L'invariant est violé **sans
    /// qu'aucun agent ne l'observe**, et ni la latence ni le taux d'erreur ne
    /// le signalent. Seul l'oracle externe le voit.
    pub fn verifier_double_detention(
        &mut self,
        horloges: &Horloges,
        agent: ActeurId,
        maintenant: Instant,
    ) -> Option<String> {
        let echeance = match self.detenteur {
            Some((d, e)) if d == agent => e,
            _ => return None,
        };
        // L'agent juge l'échéance à son horloge, qui dérive.
        let percu = horloges.percu(agent, maintenant);
        if percu < echeance && maintenant >= echeance {
            self.doubles_detentions += 1;
            return Some(format!(
                "double détention à {} : l'agent {} croit son bail vivant (son horloge indique \
                 {}) alors que l'échéance {} est passée. ε_vrai = {:.4} dépasse l'ε supposé. \
                 **Ni la latence ni le taux d'erreur ne le signalent** — seul l'oracle externe le \
                 voit (§7.2, EX-A33 clause 2).",
                maintenant.0, agent.0, percu.0, echeance.0, horloges.epsilon_vrai
            ));
        }
        None
    }

    /// **Clause (3) — dimensionnement de D.** Le surcoût de bavardage vaut
    /// `ℓ₉₉/D` de l'intervalle ; la capacité immobilisée au pire lors d'une
    /// partition vaut `D`. **Aucun réglage ne supprime les deux**, et
    /// l'interface trace les deux courbes ensemble.
    pub fn dimensionnement(&self, l99: Duree) -> (f64, f64) {
        let bavardage = l99.0 as f64 / self.d.0.max(1) as f64;
        let immobilisee = self.d.0 as f64;
        (bavardage, immobilisee)
    }

    /// **Clause (4) — pourquoi l'accord est requis ici et pas ailleurs.**
    pub const POURQUOI_LACCORD: &'static str =
        "deux agents qui décident indépendamment d'isoler deux hôtes appartenant au même quorum \
         RÉALISENT le déni de service que l'attaquant n'avait pas obtenu. La sûreté requise est un \
         invariant global — au plus f hôtes confinés simultanément — qui doit tenir à tout \
         instant. C'est exactement le cas où le substrat événementiel ne suffit pas (§7.2).";

    /// Libellé permanent du volet 4 du scénario J.
    pub const LIBELLE_PERMANENT: &'static str =
        "ici, le bail est sûr **sous hypothèse**, non par construction";
}

// ---------------------------------------------------------------------------
// EX-A24 et EX-A41 — reconfiguration sur soupçon, S1w contre S1
// ---------------------------------------------------------------------------

/// **EX-A41** — l'arbitrage d'époque est un commutateur à **deux positions, et
/// deux seulement**. Toute configuration hors de ces deux positions est rejetée
/// à la construction.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum ArbitrageDepoque {
    /// Le milieu détient l'époque du bail et rejette les écritures d'époque
    /// inférieure. La ligne 10 de l'algorithme 4.3 est **opérante**.
    LeMilieuArbitre,
    /// La sûreté repose alors entièrement sur l'exactitude du détecteur —
    /// hypothèse que le produit refuse. La seule issue restante est de payer un
    /// quorum sur l'appartenance, facturé en Ω(n) messages par décision.
    LeMilieuNarbitrePas,
}

/// Message de rejet d'une troisième voie.
pub const REFUS_TROISIEME_VOIE: &str = "le détecteur ne prouve pas la mort, il la soupçonne";

/// **EX-A24** — reconfiguration d'allocation sur soupçon, avec époque.
pub struct Reconfiguration {
    /// Le milieu compare-t-il les époques ? C'est DT9, et le débrayage est un
    /// préréglage nommé, pas un défaut.
    pub arbitrage: ArbitrageDepoque,
    /// Époque courante du bail, par plage.
    epoques: Vec<u64>,
    /// Propriétaire de chaque plage.
    proprietaires: Vec<Option<ActeurId>>,
    /// Écritures rejetées pour époque périmée. Leur existence est ce qui rend
    /// **S1w** observable.
    pub rejets_pour_epoque: u64,
    /// Écritures acceptées alors qu'elles portaient une époque périmée. Non nul
    /// seulement sans arbitrage.
    pub acceptations_perimees: u64,
    /// Instants de début de double détention, par plage.
    debut_double: Vec<Option<Instant>>,
    /// Durée cumulée pendant laquelle deux agents ont détenu la même plage.
    pub duree_double_detention: Duree,
    /// L'idempotence du traitement est-elle active ?
    pub idempotence: bool,
    /// Doubles traitements **aux conséquences effectives** — nul sous
    /// idempotence, qui les rend inoffensifs sans les supprimer.
    pub doubles_effets: u64,
}

impl Reconfiguration {
    /// Reconfiguration neuve sur `plages` plages, toutes sans propriétaire.
    pub fn nouvelle(plages: usize, arbitrage: ArbitrageDepoque) -> Reconfiguration {
        Reconfiguration {
            arbitrage,
            epoques: vec![0; plages],
            proprietaires: vec![None; plages],
            rejets_pour_epoque: 0,
            acceptations_perimees: 0,
            debut_double: vec![None; plages],
            duree_double_detention: Duree(0),
            idempotence: false,
            doubles_effets: 0,
        }
    }

    /// L'époque courante d'une plage.
    pub fn epoque(&self, plage: usize) -> u64 {
        self.epoques[plage]
    }

    /// Le propriétaire d'une plage, s'il y en a un.
    pub fn proprietaire(&self, plage: usize) -> Option<ActeurId> {
        self.proprietaires[plage]
    }

    /// Lignes 7 à 10 : retrait de `m` de la vue, **incrément d'époque**,
    /// recalcul local, demande de bail.
    ///
    /// L'ancien propriétaire n'est pas informé : il se croit toujours
    /// propriétaire, et la double détention commence.
    pub fn reconfigurer(&mut self, plage: usize, nouveau: ActeurId, maintenant: Instant) {
        if self.proprietaires[plage].is_some() {
            self.debut_double[plage] = Some(maintenant);
        }
        self.epoques[plage] += 1;
        self.proprietaires[plage] = Some(nouveau);
    }

    /// Une écriture arrive, estampillée d'une époque.
    ///
    /// **S1w** — sous arbitrage, aucune écriture d'époque inférieure n'est
    /// acceptée. C'est une propriété d'**écriture**, distincte de S1.
    pub fn ecrire(
        &mut self,
        plage: usize,
        auteur: ActeurId,
        epoque: u64,
        maintenant: Instant,
    ) -> bool {
        let courante = self.epoques[plage];
        let perimee = epoque < courante;

        // L'auteur périmé constate son bail périmé en écrivant : la double
        // détention s'achève ici.
        if perimee {
            if let Some(debut) = self.debut_double[plage].take() {
                self.duree_double_detention = self.duree_double_detention + (maintenant - debut);
            }
        }

        match (self.arbitrage, perimee) {
            (ArbitrageDepoque::LeMilieuArbitre, true) => {
                self.rejets_pour_epoque += 1;
                false
            }
            (ArbitrageDepoque::LeMilieuNarbitrePas, true) => {
                // La ligne 10 est inopérante : deux propriétaires écrivent
                // simultanément.
                self.acceptations_perimees += 1;
                if !self.idempotence {
                    self.doubles_effets += 1;
                }
                true
            }
            (_, false) => {
                let _ = auteur;
                true
            }
        }
    }

    /// **S1w** — nomenclature du produit, non un énoncé du traité : aucune
    /// écriture d'époque inférieure n'est acceptée par le milieu.
    pub fn s1w_tient(&self) -> bool {
        self.acceptations_perimees == 0
    }

    /// **S1 au sens du glossaire n'est PAS rétabli par l'arbitrage d'époque.**
    ///
    /// Entre l'instant du soupçon et l'instant où `m` constate son bail périmé,
    /// deux agents détiennent l'attribution. Le simulateur affiche les deux
    /// grandeurs **séparément** et n'écrit jamais « S1 tient » là où seule S1w
    /// tient.
    pub fn affichage_s1(&self, asynchrone: bool) -> Vec<(&'static str, String)> {
        vec![
            (
                "S1w — écritures d'époque périmée rejetées",
                if self.s1w_tient() {
                    format!("tient ; {} rejet(s)", self.rejets_pour_epoque)
                } else {
                    format!(
                        "VIOLÉE ; {} acceptation(s) périmée(s)",
                        self.acceptations_perimees
                    )
                },
            ),
            (
                "S1 (glossaire) — jamais deux détenteurs simultanés",
                format!(
                    "**non rétabli par l'arbitrage d'époque** ; durée de double détention {} {}",
                    self.duree_double_detention.0,
                    if asynchrone {
                        "tics — non bornée en asynchrone"
                    } else {
                        "tics"
                    }
                ),
            ),
            (
                "doubles effets",
                format!(
                    "{} — l'idempotence est {}",
                    self.doubles_effets,
                    if self.idempotence {
                        "active"
                    } else {
                        "désactivée"
                    }
                ),
            ),
        ]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// NF-15 — la complétude retrouve **21 à 31 s** aux défauts documentés
    /// (§7.3, p. 112, 4ᵉ éd.).
    #[test]
    fn la_completude_retrouve_les_21_a_31_secondes() {
        let (min, max) = DetecteurInfectieux::completude(10, 1, 3).expect("réglage documenté");
        assert_eq!((min.0, max.0), (21, 31));
    }

    /// SPEC §7, clause 4 — `seuil = 0` faisait déborder `seuil − 1` sur un
    /// entier non signé : panique en debug, encadrement absurde en release. Il
    /// est désormais **refusé**, et non écrêté : l'écrêtage rendait `(1, 11)`,
    /// un encadrement d'allure plausible que rien ne distingue d'une mesure.
    #[test]
    fn un_seuil_dechec_nul_est_refuse_au_lieu_detre_ecrete() {
        let motif = DetecteurInfectieux::completude(10, 1, 0)
            .expect_err("seuil nul : refus attendu, pas une valeur");
        assert!(motif.contains("zéro échec"), "{motif}");
        // Et le réglage voisin passe : la garde ne mange pas le domaine utile.
        let (min, max) = DetecteurInfectieux::completude(10, 1, 1).expect("un échec suffit");
        assert_eq!((min.0, max.0), (1, 11));
    }

    /// Même arbitrage que `sim_core::detecteur` : le produit `période ×
    /// (seuil − 1)` **sature**. Le profil release ne pose pas
    /// `overflow-checks`, et l'enroulement annonçait une détection quasi
    /// immédiate sur l'encadrement le plus lent représentable.
    #[test]
    fn la_completude_sature_au_lieu_de_senrouler() {
        let (min, max) = DetecteurInfectieux::completude(1u64 << 63, 1, 3).expect("seuil valide");
        assert_eq!((min.0, max.0), (u64::MAX, u64::MAX));
    }

    /// EX-A23 — les coûts : 2 messages et 1 tour en nominal, au plus 2 + 4s
    /// messages et 3 tours par cycle de suspicion.
    #[test]
    fn les_couts_du_detecteur_sont_ceux_du_traite() {
        let d = DetecteurInfectieux::nouveau(128, Duree(2_000), 3);
        assert_eq!(
            d.cout_nominal(),
            Cout {
                messages: 2,
                tours: 1
            }
        );
        assert_eq!(
            d.cout_suspicion(),
            Cout {
                messages: 2 + 4 * 3,
                tours: 3
            }
        );
    }

    /// EX-A23 — le mode battement de cœur est le terme de comparaison, et sa
    /// charge croît **quadratiquement**.
    #[test]
    fn le_battement_de_coeur_coute_quadratiquement() {
        let mut petit = DetecteurInfectieux::nouveau(16, Duree(2_000), 3);
        let mut grand = DetecteurInfectieux::nouveau(160, Duree(2_000), 3);
        petit.battement_de_coeur = true;
        grand.battement_de_coeur = true;
        let rapport = grand.cout_nominal().messages as f64 / petit.cout_nominal().messages as f64;
        assert!(rapport > 90.0, "×{rapport:.1} pour une population ×10");

        // Le mode infectieux, lui, ne dépend pas de n.
        let a = DetecteurInfectieux::nouveau(16, Duree(2_000), 3);
        let b = DetecteurInfectieux::nouveau(160, Duree(2_000), 3);
        assert_eq!(a.cout_nominal(), b.cout_nominal());
    }

    /// EX-A23, EX-C14 — le sondage indirect distingue la perte d'un lien de la
    /// mort **si et seulement si** les s pairs ne partagent pas le lien fautif.
    /// Le protocole ne vérifie pas cette condition.
    #[test]
    fn le_sondage_indirect_echoue_quand_les_pairs_partagent_le_domaine() {
        let mut alea = Alea::nouveau(1);

        // Domaines disjoints : les pairs démentent le faux soupçon.
        let mut d = DetecteurInfectieux::nouveau(64, Duree(2_000), 3);
        let disjoints = Domaines::disjoints(64, 0.0);
        let v = d.cycle(ActeurId(5), true, true, &disjoints, &mut alea);
        assert_eq!(v, Verdict::LienFautif);
        assert_eq!(d.fausses_suspicions, 0);

        // Domaine unique : ils confirment, et l'agent vivant est suspecté.
        let mut d2 = DetecteurInfectieux::nouveau(64, Duree(2_000), 3);
        let unique = Domaines::unique(64, 0.0);
        let v2 = d2.cycle(ActeurId(5), true, true, &unique, &mut alea);
        assert_eq!(v2, Verdict::Suspect);
        assert_eq!(d2.fausses_suspicions, 1);
    }

    /// Un agent réellement arrêté est suspecté quelle que soit la structure.
    #[test]
    fn un_agent_arrete_est_suspecte_dans_tous_les_cas() {
        let mut alea = Alea::nouveau(2);
        for domaines in [Domaines::disjoints(32, 0.0), Domaines::unique(32, 0.0)] {
            let mut d = DetecteurInfectieux::nouveau(32, Duree(2_000), 3);
            assert_eq!(
                d.cycle(ActeurId(1), false, false, &domaines, &mut alea),
                Verdict::Suspect
            );
            assert_eq!(d.fausses_suspicions, 0, "l'agent était vraiment mort");
        }
    }

    /// **EX-A33 clause 1** — la politique d'expiration est un choix binaire
    /// déclaré, et chaque position affiche sa conséquence.
    #[test]
    fn la_politique_dexpiration_est_un_choix_declare() {
        assert!(PolitiqueExpiration::Relacher
            .consequence()
            .contains("CATASTROPHIQUE"));
        assert!(PolitiqueExpiration::Maintenir
            .consequence()
            .contains("panne durable"));
        assert!(PolitiqueExpiration::LIBELLE.contains("plutôt que subi"));
    }

    /// **EX-A33** — étapes et coûts : 2q messages et 1 tour par demande, coût
    /// **nul** par observation.
    #[test]
    fn les_couts_du_bail_sont_ceux_du_traite() {
        let mut b = Bail::nouveau(
            3,
            Duree(30_000),
            Duree(10),
            Duree(200),
            PolitiqueExpiration::Maintenir,
        );
        b.demander(ActeurId(0), Instant(0));
        assert_eq!(b.messages, 6, "2q à q = 3");
        assert_eq!(b.tours, 1);
        assert_eq!(Bail::COUT_PAR_OBSERVATION, 0);
        assert_eq!(
            b.cout_par_action(),
            Cout {
                messages: 6,
                tours: 2
            }
        );
    }

    /// **EX-A33** — la condition d'arrêt est **locale**, donc terminante sans
    /// accord.
    #[test]
    fn la_condition_darret_du_bail_est_locale() {
        let mut b = Bail::nouveau(
            1,
            Duree(1_000),
            Duree(10),
            Duree(100),
            PolitiqueExpiration::Relacher,
        );
        let agent = ActeurId(0);
        b.demander(agent, Instant(0)).unwrap();
        assert!(!b.doit_ceder(agent, Instant(500)));
        assert!(b.doit_ceder(agent, Instant(1_000)));
        // Il faut renouveler avant D − ε − Δ.
        assert_eq!(b.limite_de_renouvellement(Instant(0)), Instant(890));
    }

    /// **EX-A33 clause 2** — le troisième mode est **invisible** : sous dérive
    /// excessive, le détenteur croit son bail vivant alors qu'il est périmé.
    #[test]
    fn le_troisieme_mode_du_bail_est_invisible() {
        let mut alea = Alea::nouveau(3);
        // ε_vrai de 5 % : bien au-delà de l'ε supposé.
        let horloges = Horloges::nouvelles(4, 0.05, &mut alea);
        let mut b = Bail::nouveau(
            2,
            Duree(1_000),
            Duree(10),
            Duree(100),
            PolitiqueExpiration::Maintenir,
        );
        // On cherche un agent dont l'horloge retarde : il croira son bail
        // encore vivant après l'échéance.
        let agent = (0..4u32)
            .map(ActeurId)
            .find(|a| horloges.facteur(*a) < 1.0)
            .expect("au moins une horloge en retard");
        b.demander(agent, Instant(0));

        let avis = b
            .verifier_double_detention(&horloges, agent, Instant(1_010))
            .expect("la double détention doit être constatée");
        assert!(avis.contains("Ni la latence ni le taux d'erreur"), "{avis}");
        assert_eq!(b.doubles_detentions, 1);
        assert!(Bail::LIBELLE_PERMANENT.contains("sous hypothèse"));
    }

    /// **EX-A33 clause 3** — bavardage et capacité immobilisée ne descendent
    /// **jamais ensemble**.
    #[test]
    fn aucun_reglage_de_d_ne_supprime_les_deux_couts() {
        let court = Bail::nouveau(
            2,
            Duree(1_000),
            Duree(10),
            Duree(100),
            PolitiqueExpiration::Maintenir,
        );
        let long = Bail::nouveau(
            2,
            Duree(100_000),
            Duree(10),
            Duree(100),
            PolitiqueExpiration::Maintenir,
        );
        let l99 = Duree(200);
        let (bav_court, imm_court) = court.dimensionnement(l99);
        let (bav_long, imm_long) = long.dimensionnement(l99);
        assert!(bav_court > bav_long, "un bail court bavarde plus");
        assert!(imm_long > imm_court, "un bail long immobilise plus");
        assert!(Bail::POURQUOI_LACCORD.contains("déni de service"));
    }

    /// **EX-A41** — sous arbitrage, **S1w tient** : les écritures d'époque
    /// périmée sont rejetées.
    #[test]
    fn sous_arbitrage_s1w_tient() {
        let mut r = Reconfiguration::nouvelle(4, ArbitrageDepoque::LeMilieuArbitre);
        let m = ActeurId(1);
        let i = ActeurId(2);
        // m détient la plage 0 à l'époque 1.
        r.reconfigurer(0, m, Instant(0));
        let epoque_de_m = r.epoque(0);
        // Faux soupçon : i reprend la plage, l'époque s'incrémente.
        r.reconfigurer(0, i, Instant(100));
        // m revient et écrit avec son époque périmée.
        assert!(
            !r.ecrire(0, m, epoque_de_m, Instant(200)),
            "l'écriture est rejetée"
        );
        assert!(r.s1w_tient());
        assert_eq!(r.rejets_pour_epoque, 1);
    }

    /// **EX-A41** — … et **S1 au sens du glossaire ne tient pas pour autant**.
    /// La durée de double détention est non nulle, et l'interface ne dit jamais
    /// « S1 tient ».
    #[test]
    fn s1_ne_tient_pas_meme_sous_arbitrage() {
        let mut r = Reconfiguration::nouvelle(4, ArbitrageDepoque::LeMilieuArbitre);
        let m = ActeurId(1);
        r.reconfigurer(0, m, Instant(0));
        let epoque_de_m = r.epoque(0);
        r.reconfigurer(0, ActeurId(2), Instant(100));
        r.ecrire(0, m, epoque_de_m, Instant(350));

        assert!(
            r.duree_double_detention.0 > 0,
            "deux détenteurs ont coexisté"
        );
        let affichage = r.affichage_s1(true);
        let s1 = affichage
            .iter()
            .find(|(k, _)| k.starts_with("S1 ("))
            .unwrap();
        assert!(s1.1.contains("non rétabli"), "{}", s1.1);
        assert!(s1.1.contains("non bornée en asynchrone"), "{}", s1.1);
        // Nulle part l'interface n'écrit « S1 tient ».
        assert!(!affichage.iter().any(|(_, v)| v.contains("S1 tient")));
    }

    /// **Critère (7) du scénario J** — sans arbitrage, l'écriture périmée est
    /// acceptée **exactement** à l'instant où m réapparaît et écrit, et pas
    /// avant.
    #[test]
    fn sans_arbitrage_lecriture_perimee_est_acceptee_a_linstant_du_retour() {
        let mut r = Reconfiguration::nouvelle(4, ArbitrageDepoque::LeMilieuNarbitrePas);
        let m = ActeurId(1);
        r.reconfigurer(0, m, Instant(0));
        let epoque_de_m = r.epoque(0);
        r.reconfigurer(0, ActeurId(2), Instant(100));
        assert_eq!(r.acceptations_perimees, 0, "rien avant le retour de m");

        assert!(r.ecrire(0, m, epoque_de_m, Instant(300)), "acceptée");
        assert_eq!(r.acceptations_perimees, 1);
        assert!(!r.s1w_tient(), "S1w tombe sans arbitrage");
        assert_eq!(
            r.doubles_effets, 1,
            "et sans idempotence, l'effet est dupliqué"
        );
    }

    /// L'idempotence laisse les acceptations périmées et annule leurs effets.
    #[test]
    fn lidempotence_annule_les_doubles_effets_sans_les_empecher() {
        let mut r = Reconfiguration::nouvelle(4, ArbitrageDepoque::LeMilieuNarbitrePas);
        r.idempotence = true;
        r.reconfigurer(0, ActeurId(1), Instant(0));
        let e = r.epoque(0);
        r.reconfigurer(0, ActeurId(2), Instant(10));
        r.ecrire(0, ActeurId(1), e, Instant(20));
        assert_eq!(r.acceptations_perimees, 1);
        assert_eq!(r.doubles_effets, 0);
    }

    /// EX-A41 — il n'y a que deux positions, et le message de refus est celui
    /// du traité.
    #[test]
    fn il_ny_a_que_deux_positions() {
        assert!(REFUS_TROISIEME_VOIE.contains("il la soupçonne"));
    }
}
