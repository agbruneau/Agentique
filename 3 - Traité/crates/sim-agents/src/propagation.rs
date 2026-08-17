//! **Propager** — rumeur, anti-entropie, répliques sans conflit, et le coût de
//! l'accord (EX-A19 à EX-A22, EX-A40).
//!
//! Les quatre mécanismes du §4.2, chacun avec son modèle de panne, son
//! synchronisme et son **contrat de canal** posés avant son algorithme. Aucun
//! des quatre ne suppose le même, et c'est le point du scénario I.

use crate::echantillonnage::{Biais, ServiceDePairs};
use sim_core::alea::Alea;

/// État d'un agent vis-à-vis de la rumeur (EX-A19).
#[derive(Clone, Copy, PartialEq, Eq, Debug, Default)]
pub enum Etat {
    /// Ne connaît pas encore la rumeur.
    #[default]
    Susceptible,
    /// La connaît et la propage.
    Infectieux,
    /// La connaît et a cessé de la propager — c'est la ligne 6.
    Retire,
}

/// **EX-A19** — algorithme 2 du ch. 4, rumeur push-pull avec retrait par
/// compteur.
///
/// `cpt` est incrémenté sur **rencontre redondante** — un pair qui connaît déjà
/// la rumeur — et l'agent se retire à `cpt ≥ K`. C'est la **ligne 6**, et c'est
/// elle seule qui sépare Θ(n log log n) de Θ(n log n).
pub struct Rumeur {
    /// Compteur de retrait K. `None` désactive le retrait : c'est le schéma
    /// naïf.
    pub k: Option<u32>,
    /// État de chaque agent. **C'est elle qui porte la population** : il n'y a
    /// pas de champ `n` en regard qu'un appelant pourrait déplacer sans déplacer
    /// les tables. Voir [`Rumeur::n`].
    etat: Vec<Etat>,
    compteur: Vec<u32>,
    /// Messages de rumeur échangés.
    pub messages: u64,
    /// Tours écoulés.
    pub tours: u64,
    /// Anti-entropie active en parallèle — le filet (EX-A20).
    pub anti_entropie: bool,
    /// Fréquence de l'anti-entropie, bridée par le coût de comparaison.
    pub periode_anti_entropie: u64,
    /// Messages consommés par l'anti-entropie, comptés **à part**.
    pub messages_anti_entropie: u64,
    /// Choix de pair sensible à l'adresse : sort du modèle et **efface** la
    /// borne (EX-A42).
    pub sensible_a_ladresse: bool,
}

impl Rumeur {
    /// Population de `n` agents dont **un seul** connaît la rumeur au départ.
    ///
    /// `n = 0` est ramené à 1 : « un seul connaît la rumeur » n'a pas de sens
    /// sur une population vide, et une population vide n'est pas un réglage que
    /// le scénario I balaie. Le constructeur ne rend pas de `Result` parce qu'il
    /// n'a aucune autre condition d'échec ; ce qu'il doit garantir, c'est de ne
    /// jamais abandonner sur un indice hors bornes (SPEC §7, clause 4).
    pub fn nouvelle(n: u32, k: Option<u32>) -> Rumeur {
        let n = n.max(1);
        let mut etat = vec![Etat::Susceptible; n as usize];
        etat[0] = Etat::Infectieux;
        Rumeur {
            k,
            etat,
            compteur: vec![0; n as usize],
            messages: 0,
            tours: 0,
            anti_entropie: false,
            periode_anti_entropie: 10,
            messages_anti_entropie: 0,
            sensible_a_ladresse: false,
        }
    }

    /// Taille de la population — **dérivée** de la table d'états, jamais rangée
    /// en double à côté d'elle. Vaut au moins 1.
    pub fn n(&self) -> u32 {
        self.etat.len() as u32
    }

    /// L'état de l'agent `i`, où `i` est un indice de la population et non un
    /// identifiant tiré du service de pairs — les deux se ressemblent et ne se
    /// confondent pas ici.
    ///
    /// # Panics
    ///
    /// Si `i >= n()`. C'est le seul accès public du module qui indexe sans
    /// borner : les identifiants venus du service de pairs sont écartés à
    /// l'entrée par `Rumeur::tirer`, privé, qui les traite comme un tirage sans
    /// réponse. Le rendre faillible comme
    /// [`crate::echantillonnage::TriDeVue::vue`] est un changement de
    /// signature ; la méthode n'a aucun appelant dans le dépôt.
    pub fn etat(&self, i: u32) -> Etat {
        self.etat[i as usize]
    }

    /// Fraction d'agents qui connaissent la rumeur — infectieux **ou** retirés.
    pub fn fraction_informee(&self) -> f64 {
        let informes = self
            .etat
            .iter()
            .filter(|e| **e != Etat::Susceptible)
            .count();
        informes as f64 / self.n() as f64
    }

    /// **Fraction résiduelle de susceptibles.** C'est la grandeur qu'EX-A40
    /// impose d'afficher en regard, avec le K qui la fixe.
    pub fn fraction_residuelle(&self) -> f64 {
        1.0 - self.fraction_informee()
    }

    /// Un tour.
    pub fn tour(&mut self, service: &mut ServiceDePairs, alea: &mut Alea) {
        self.tours += 1;
        let n = self.n();
        let etats = self.etat.clone();
        for i in 0..n {
            if etats[i as usize] != Etat::Infectieux {
                continue;
            }
            let j = match self.tirer(i, service, alea) {
                Some(j) => j,
                None => continue,
            };
            // Push-pull : un message aller, un retour.
            self.messages += 2;
            match etats[j as usize] {
                Etat::Susceptible => {
                    self.etat[j as usize] = Etat::Infectieux;
                }
                // **Rencontre redondante** : le pair connaissait déjà. C'est la
                // ligne 6.
                Etat::Infectieux | Etat::Retire => {
                    self.compteur[i as usize] += 1;
                    if let Some(k) = self.k {
                        if self.compteur[i as usize] >= k {
                            self.etat[i as usize] = Etat::Retire;
                        }
                    }
                }
            }
        }

        // EX-A20 — l'anti-entropie tourne **en parallèle**, comme filet. Elle
        // n'a pas d'état retiré : elle réconcilie tant qu'il reste un écart.
        if self.anti_entropie && self.tours.is_multiple_of(self.periode_anti_entropie) {
            for i in 0..n {
                let j = match self.tirer(i, service, alea) {
                    Some(j) => j,
                    None => continue,
                };
                // Le coût de comparaison est ce qui bride sa fréquence.
                self.messages_anti_entropie += 2;
                if self.etat[i as usize] == Etat::Susceptible
                    && etats[j as usize] != Etat::Susceptible
                {
                    self.etat[i as usize] = Etat::Infectieux;
                }
            }
        }
    }

    /// Le seul point par où un identifiant de pair entre dans ce mécanisme —
    /// donc le seul endroit où il faut le borner. Le service de pairs a **sa
    /// propre** population : au-delà de `n`, il désigne un agent que la rumeur
    /// n'a pas, et le tirage vaut alors un tirage sans réponse (SPEC §7,
    /// clause 4).
    fn tirer(&self, i: u32, service: &mut ServiceDePairs, alea: &mut Alea) -> Option<u32> {
        let n = self.n();
        if self.sensible_a_ladresse {
            // L'agent choisit son pair d'après ce qu'il sait de lui : il sort du
            // modèle, et la borne cesse de s'appliquer dans un sens comme dans
            // l'autre (§4.2, EX-A42).
            let candidat = (i + 1) % n;
            return Some(candidat);
        }
        service.tirer(i, alea).filter(|j| *j < n)
    }

    /// **EX-A40** — la couverture est une **vivacité probabiliste** et ne
    /// s'énonce jamais sans sa condition.
    ///
    /// Le simulateur n'affiche **jamais** « la rumeur a atteint tous les
    /// agents ». La seule formulation admise pour une couverture certaine est
    /// conditionnelle.
    pub fn affichage_couverture(&self) -> String {
        let base = format!(
            "fraction informée {:.4} ; fraction résiduelle de susceptibles {:.4}, fixée par {}",
            self.fraction_informee(),
            self.fraction_residuelle(),
            match self.k {
                Some(k) => format!("K = {k}"),
                None => "l'absence de retrait (K = ∞)".to_string(),
            }
        );
        if self.anti_entropie {
            format!(
                "{base}. Sous anti-entropie active, couverture certaine à terme, **sans borne de \
                 temps** (EX-A40)."
            )
        } else {
            format!(
                "{base}. Aucune couverture certaine n'est annoncée : la probabilité résiduelle de \
                 rester susceptible tend vers une constante fixée par K, pas vers 0 (§4.2)."
            )
        }
    }

    /// EX-A42, NF-14 — la borne s'efface dès que le choix de pair devient
    /// sensible à l'adresse.
    pub fn bornes_applicables(&self, biais: Biais) -> Result<(), String> {
        if self.sensible_a_ladresse {
            return Err(
                "borne effacée : l'optimalité Θ(n log log n) de la rumeur push-pull suppose \
                 l'**insensibilité à l'adresse**. Un agent qui choisit son pair d'après ce qu'il \
                 sait de lui sort du modèle, et la borne cesse de s'appliquer « dans un sens \
                 comme dans l'autre » (§4.2) — y compris si la mesure est meilleure (NF-14)."
                    .to_string(),
            );
        }
        biais.bornes_applicables()
    }
}

/// **EX-A21** — les deux familles de répliques sans conflit.
///
/// Elles ne sont **pas interchangeables** : chacune a son hypothèse de canal, et
/// les confondre est fatal (EX-A52).
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum FamilleCrdt {
    /// Treillis à jonction monotone. Convergence pourvu que le système
    /// transmette la charge utile une infinité de fois, par paires, sur des
    /// canaux point à point à **livraison à terme**. Θ(n) octets par message,
    /// Θ(n²) par tour d'anti-entropie complet.
    Etat,
    /// Opérations concurrentes commutatives, **diffusion fiable en ordre
    /// causal**, duplication éliminée par conservation de l'ensemble des
    /// messages déjà livrés. Θ(1) par opération.
    Operations,
}

/// Contrat exigé du transport.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum ContratDeTransport {
    /// Le canal perd, duplique et désordonne. C'est le contrat du milieu entre
    /// partitions — c'est M2.
    PerdDupliqueDesordonne,
    /// Livraison causale, exactement une fois. Strictement plus cher, et le
    /// milieu ne l'offre pas entre partitions.
    CausalExactementUneFois,
}

impl FamilleCrdt {
    /// Le contrat de transport que cette famille **exige**. C'est là que se
    /// joue le choix : le milieu offre le premier, pas le second.
    pub fn contrat_exige(self) -> ContratDeTransport {
        match self {
            FamilleCrdt::Etat => ContratDeTransport::PerdDupliqueDesordonne,
            FamilleCrdt::Operations => ContratDeTransport::CausalExactementUneFois,
        }
    }

    /// Octets par message, à n répliques.
    pub fn octets_par_message(self, n: u32) -> u64 {
        match self {
            FamilleCrdt::Etat => 8 * n as u64,
            FamilleCrdt::Operations => 8,
        }
    }

    /// **EX-A52** — un type qui porte un invariant exigeant un **refus** —
    /// unicité, budget, exclusion mutuelle, capacité maximale — est rejeté à la
    /// construction.
    pub fn verifier_invariant(self, exige_un_refus: bool) -> Result<(), String> {
        if exige_un_refus {
            return Err(
                "type refusé : une fusion sans conflit **ne peut pas refuser**. Un invariant qui \
                 exige un refus — unicité, budget, exclusion mutuelle, capacité maximale — \
                 demande un accord, et ce chapitre-là est le ch. 4 (§5.1, EX-A52)."
                    .to_string(),
            );
        }
        Ok(())
    }

    /// **EX-A52, préréglage** — confondre les deux familles est provocable, et
    /// ce qu'on observe diffère selon la famille.
    ///
    /// Rend `true` si les répliques convergent sous ce contrat.
    pub fn converge_sous(self, contrat: ContratDeTransport) -> bool {
        match (self, contrat) {
            // La jonction est idempotente : le rejeu ne dérange pas.
            (FamilleCrdt::Etat, _) => true,
            (FamilleCrdt::Operations, ContratDeTransport::CausalExactementUneFois) => true,
            // Une opération livrée deux fois s'applique deux fois.
            (FamilleCrdt::Operations, ContratDeTransport::PerdDupliqueDesordonne) => false,
        }
    }

    /// Ce que le mécanisme achète en échange (EX-A52).
    pub const IMMUNITE: &'static str =
        "immunité à la partition : les répliques d'un sous-ensemble connecté continuent de se \
         livrer mutuellement leurs mises à jour sans qu'aucun accord soit requis";
}

/// **EX-A22** — le consensus, réduit à son coût et à sa fenêtre.
///
/// **Aucun protocole n'est implanté** (DT7). Ce qui est modélisé, c'est le prix :
/// Ω(n) messages par décision, terminaison bornée **après** stabilisation
/// seulement, indisponibilité ≈ un délai d'élection après arrêt du meneur.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum ClasseDeDetecteur {
    /// Détecteur **fort** : tolère un nombre quelconque de défaillances.
    Fort,
    /// Fortement exact à terme (◇W) : exige une **majorité de corrects**, et
    /// c'est prouvé nécessaire.
    FortementExactATerme,
}

impl ClasseDeDetecteur {
    /// Nombre de défaillances tolérées sur n participants.
    pub fn tolerance(self, n: u32) -> u32 {
        match self {
            ClasseDeDetecteur::Fort => n.saturating_sub(1),
            ClasseDeDetecteur::FortementExactATerme => (n.saturating_sub(1)) / 2,
        }
    }

    /// Pourquoi cette classe exige ce nombre de corrects.
    pub fn justification(self) -> &'static str {
        match self {
            ClasseDeDetecteur::Fort => "détecteur fort : un nombre quelconque de défaillances",
            ClasseDeDetecteur::FortementExactATerme => {
                "détecteur fortement exact à terme : majorité de corrects exigée, et prouvée \
                 nécessaire (§4.2)"
            }
        }
    }
}

/// Le coût d'une décision d'accord, sans le protocole.
#[derive(Clone, Copy, Debug)]
pub struct CoutAccord {
    /// Nombre de participants à l'accord.
    pub n: u32,
    /// Classe de détecteur supposée — elle fixe le nombre de corrects exigé.
    pub classe: ClasseDeDetecteur,
    /// Délai d'élection, qui fixe la fenêtre d'indisponibilité.
    pub delai_election_ms: f64,
}

impl CoutAccord {
    /// Ω(n) messages par décision.
    pub fn messages_par_decision(&self) -> u64 {
        self.n as u64
    }

    /// La terminaison n'est bornée **qu'après** l'instant de stabilisation.
    /// Avant, elle ne l'est pas — et le simulateur ne fabrique pas de délai.
    pub fn terminaison(&self, stabilise: bool) -> Option<f64> {
        if stabilise {
            Some(self.delai_election_ms)
        } else {
            None
        }
    }

    /// Ce qui s'affiche à la place d'une borne, avant stabilisation.
    pub const LIBELLE_TERMINAISON: &'static str =
        "avant l'instant de stabilisation, aucune borne de terminaison n'existe. Le simulateur \
         n'en affiche pas : « non bornée » ne veut pas dire « grande » (§4.2, DT7)";
}

#[cfg(test)]
mod tests {
    use super::*;

    /// SPEC §7, clause 4 — `n = 0` indexait un vecteur vide. La population est
    /// ramenée à un agent, et le tour ne panique pas. La population n'est plus
    /// un champ public : ce qui reste atteignable est un **service de pairs plus
    /// grand** que la rumeur, et il ne panique pas non plus.
    #[test]
    fn une_population_vide_ou_plus_petite_que_le_service_ne_panique_pas() {
        let mut r = Rumeur::nouvelle(0, Some(3));
        assert_eq!(r.n(), 1);
        let mut s = crate::echantillonnage::ServiceDePairs::nouveau(1, crate::echantillonnage::Biais::Uniforme);
        let mut alea = Alea::nouveau(1);
        r.tour(&mut s, &mut alea);

        let mut petite = Rumeur::nouvelle(4, Some(3));
        petite.anti_entropie = true;
        petite.periode_anti_entropie = 1;
        let mut grand = crate::echantillonnage::ServiceDePairs::nouveau(
            64,
            crate::echantillonnage::Biais::Uniforme,
        );
        for _ in 0..20 {
            petite.tour(&mut grand, &mut alea);
        }
        assert_eq!(petite.n(), 4, "la population reste celle du mécanisme");
        assert!(petite.fraction_informee() <= 1.0);
    }

    /// **Critère (1) du scénario I** — la fraction résiduelle de susceptibles
    /// converge vers une constante non nulle fonction de K et **ne décroît
    /// pas** quand on allonge le budget. Une décroissance serait un défaut
    /// d'implantation du retrait.
    #[test]
    fn critere_1_la_fraction_residuelle_ne_decroit_pas_avec_le_budget() {
        let mesurer = |tours: u32| {
            let mut r = Rumeur::nouvelle(2_000, Some(3));
            let mut s = ServiceDePairs::nouveau(2_000, Biais::Uniforme);
            let mut alea = Alea::nouveau(1);
            for _ in 0..tours {
                r.tour(&mut s, &mut alea);
            }
            r.fraction_residuelle()
        };
        let court = mesurer(50);
        let long = mesurer(400);
        assert!(court > 0.0, "la fraction résiduelle doit être non nulle");
        assert!(
            (long - court).abs() < 1e-12,
            "la fraction résiduelle ne doit pas décroître : {court} puis {long}"
        );
    }

    /// … et elle **dépend de K** : c'est la ligne 6 qui la fixe.
    #[test]
    fn la_fraction_residuelle_depend_de_k() {
        let mesurer = |k: u32| {
            let mut r = Rumeur::nouvelle(2_000, Some(k));
            let mut s = ServiceDePairs::nouveau(2_000, Biais::Uniforme);
            let mut alea = Alea::nouveau(2);
            for _ in 0..300 {
                r.tour(&mut s, &mut alea);
            }
            r.fraction_residuelle()
        };
        let petit_k = mesurer(1);
        let grand_k = mesurer(6);
        assert!(
            petit_k > grand_k,
            "K plus petit laisse plus de susceptibles : {petit_k} contre {grand_k}"
        );
    }

    /// **Critère (2)** — avec le retrait désactivé, le compte de messages passe
    /// de Θ(n log log n) à Θ(n log n). L'écart est l'effet de la **ligne 6
    /// seule**, et l'interface l'attribue nommément.
    #[test]
    fn critere_2_le_retrait_seul_explique_lecart_de_messages() {
        let mesurer = |k: Option<u32>| {
            let mut r = Rumeur::nouvelle(2_000, k);
            let mut s = ServiceDePairs::nouveau(2_000, Biais::Uniforme);
            let mut alea = Alea::nouveau(3);
            // On s'arrête dès que la rumeur a couvert ce qu'elle peut couvrir.
            for _ in 0..200 {
                r.tour(&mut s, &mut alea);
            }
            (r.messages, r.fraction_informee())
        };
        let (avec_retrait, couverture_avec) = mesurer(Some(3));
        let (sans_retrait, couverture_sans) = mesurer(None);
        assert!(
            sans_retrait > avec_retrait * 3,
            "sans retrait {sans_retrait} messages, avec {avec_retrait}"
        );
        // Le prix de l'économie : la couverture est moindre.
        assert!(couverture_sans > couverture_avec);
    }

    /// **EX-A40** — le simulateur n'affiche **jamais** « la rumeur a atteint
    /// tous les agents ». La seule formulation certaine est conditionnelle.
    #[test]
    fn ex_a40_la_couverture_ne_sennonce_jamais_nue() {
        let mut r = Rumeur::nouvelle(500, Some(3));
        let mut s = ServiceDePairs::nouveau(500, Biais::Uniforme);
        let mut alea = Alea::nouveau(4);
        for _ in 0..100 {
            r.tour(&mut s, &mut alea);
        }
        let a = r.affichage_couverture();
        assert!(!a.contains("a atteint tous"), "{a}");
        assert!(a.contains("fraction résiduelle"), "{a}");
        assert!(a.contains("K ="), "{a}");

        // Avec l'anti-entropie, la formulation certaine est admise — mais elle
        // reste conditionnelle et sans borne de temps.
        r.anti_entropie = true;
        let b = r.affichage_couverture();
        assert!(b.contains("Sous anti-entropie active"), "{b}");
        assert!(b.contains("sans borne de temps"), "{b}");
    }

    /// **EX-A20** — l'anti-entropie est le **filet** : elle rattrape les
    /// susceptibles que le retrait a abandonnés, à un coût compté séparément.
    #[test]
    fn ex_a20_lanti_entropie_rattrape_les_susceptibles() {
        let mesurer = |filet: bool| {
            let mut r = Rumeur::nouvelle(1_000, Some(2));
            r.anti_entropie = filet;
            let mut s = ServiceDePairs::nouveau(1_000, Biais::Uniforme);
            let mut alea = Alea::nouveau(5);
            for _ in 0..300 {
                r.tour(&mut s, &mut alea);
            }
            (r.fraction_residuelle(), r.messages_anti_entropie)
        };
        let (sans, cout_sans) = mesurer(false);
        let (avec, cout_avec) = mesurer(true);
        assert!(avec < sans, "le filet doit rattraper : {avec} contre {sans}");
        assert_eq!(cout_sans, 0);
        assert!(cout_avec > 0, "et son coût est compté à part");
    }

    /// **Critère (3)** — avec le choix de pair sensible à l'adresse, la borne
    /// cesse d'être affichée, **dans les deux sens**.
    #[test]
    fn critere_3_la_sensibilite_a_ladresse_efface_la_borne() {
        let mut r = Rumeur::nouvelle(100, Some(3));
        assert!(r.bornes_applicables(Biais::Uniforme).is_ok());
        r.sensible_a_ladresse = true;
        let e = r.bornes_applicables(Biais::Uniforme).unwrap_err();
        assert!(e.contains("insensibilité à l'adresse"), "{e}");
        assert!(e.contains("y compris si la mesure est meilleure"), "{e}");
    }

    /// **EX-A21** — les deux familles exigent deux contrats de transport
    /// différents, et ce n'est pas un détail : c'est ce qui décide de la
    /// convergence.
    #[test]
    fn ex_a21_les_deux_familles_exigent_deux_contrats() {
        assert_eq!(
            FamilleCrdt::Etat.contrat_exige(),
            ContratDeTransport::PerdDupliqueDesordonne
        );
        assert_eq!(
            FamilleCrdt::Operations.contrat_exige(),
            ContratDeTransport::CausalExactementUneFois
        );
        // La famille « état » coûte Θ(n) octets par message, l'autre Θ(1).
        assert_eq!(FamilleCrdt::Etat.octets_par_message(100), 800);
        assert_eq!(FamilleCrdt::Operations.octets_par_message(100), 8);
    }

    /// **EX-A52, préréglage** — confondre les deux familles est provocable : un
    /// type fondé sur les opérations sous canal qui duplique **ne converge
    /// pas** ; un type fondé sur l'état survit au rejeu, parce que sa jonction
    /// est idempotente.
    #[test]
    fn ex_a52_confondre_les_familles_est_fatal_pour_une_seule() {
        assert!(!FamilleCrdt::Operations.converge_sous(ContratDeTransport::PerdDupliqueDesordonne));
        assert!(FamilleCrdt::Operations.converge_sous(ContratDeTransport::CausalExactementUneFois));
        assert!(FamilleCrdt::Etat.converge_sous(ContratDeTransport::PerdDupliqueDesordonne));
        assert!(FamilleCrdt::Etat.converge_sous(ContratDeTransport::CausalExactementUneFois));
    }

    /// **EX-A52** — un type portant un invariant de refus est rejeté à la
    /// construction, avec le message du §5.1.
    #[test]
    fn ex_a52_un_invariant_de_refus_est_rejete() {
        assert!(FamilleCrdt::Etat.verifier_invariant(false).is_ok());
        let e = FamilleCrdt::Etat.verifier_invariant(true).unwrap_err();
        assert!(e.contains("ne peut pas refuser"), "{e}");
        assert!(e.contains("ch. 4"), "{e}");
        assert!(FamilleCrdt::IMMUNITE.contains("sans qu'aucun accord soit requis"));
    }

    /// **EX-A22** — la classe de détecteur décide de la tolérance, et la
    /// majorité exigée par ◇W est prouvée nécessaire.
    #[test]
    fn ex_a22_la_classe_de_detecteur_decide_de_la_tolerance() {
        assert_eq!(ClasseDeDetecteur::Fort.tolerance(7), 6);
        assert_eq!(ClasseDeDetecteur::FortementExactATerme.tolerance(7), 3);
        assert!(ClasseDeDetecteur::FortementExactATerme
            .justification()
            .contains("prouvée nécessaire"));
    }

    /// **EX-A22, DT7** — avant stabilisation, aucune borne de terminaison. Le
    /// simulateur n'en fabrique pas.
    #[test]
    fn ex_a22_avant_stabilisation_aucune_borne_de_terminaison() {
        let c = CoutAccord {
            n: 64,
            classe: ClasseDeDetecteur::FortementExactATerme,
            delai_election_ms: 200.0,
        };
        assert_eq!(c.terminaison(false), None);
        assert_eq!(c.terminaison(true), Some(200.0));
        assert_eq!(c.messages_par_decision(), 64, "Ω(n) par décision");
        assert!(CoutAccord::LIBELLE_TERMINAISON.contains("ne veut pas dire « grande »"));
    }
}
