//! **§6.3 du traité** — injection de directive globale avec époque (EX-A07, PD4,
//! EX-V03, EX-V04, EX-V19).
//!
//! > La console écrit dans le journal, jamais aux agents. (PD4)
//!
//! Toute action de l'utilisateur qui modifie le comportement de l'essaim en
//! cours d'exécution est écrite comme **enregistrement de directive** sur un
//! sujet de commande compacté, avec une époque strictement croissante. Il n'y a
//! aucun chemin de commande hors bande.
//!
//! Conséquence assumée et pédagogiquement précieuse : **le curseur de
//! l'utilisateur subit le même retard que le travail ordinaire**, et l'interface
//! le montre. Un réglage qui s'appliquerait instantanément mentirait sur la
//! nature du milieu.

use sim_core::oracle::{Oracle, Registre};
use sim_core::temps::{Duree, Instant};

/// D1 — sûreté : l'ordre des époques est respecté à l'application.
pub const D1: &str =
    "D1 [S] — aucune directive d'époque inférieure n'est appliquée après une supérieure";
/// D2 — vivacité **bornée** par la latence du chemin de commande. Elle ne
/// s'énonce jamais sans son horizon (PD2).
pub const D2: &str = "D2 [L] — toute directive finit par être accusée par les agents vivants";

/// Une directive écrite sur le sujet de commande.
#[derive(Clone, Debug, PartialEq)]
pub struct Directive {
    /// Époque **strictement croissante**. C'est elle qui porte D1.
    pub epoque: u64,
    /// Nom du réglage visé.
    pub reglage: String,
    /// Valeur demandée pour ce réglage.
    pub valeur: f64,
    /// Instant de l'écriture sur le sujet de commande.
    pub ecrite_a: Instant,
}

/// État d'une directive **tel que l'interface a le droit de l'afficher**
/// (EX-V04).
///
/// Il n'y a que deux valeurs. « Appliquée à 100 % » n'existe pas — l'essaim ne
/// peut pas le savoir — et « non appliquée » non plus : l'absence d'accusé ne
/// distingue pas un agent qui n'a pas reçu d'un agent qui n'a pas répondu.
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum EtatDirective {
    /// Au moins `a_min` accusés sont revenus.
    Appliquee,
    /// Moins que `a_min`. C'est tout ce qui peut être dit.
    Indeterminee,
}

impl EtatDirective {
    /// Le libellé affiché — l'un des deux seuls admis.
    pub fn libelle(self) -> &'static str {
        match self {
            EtatDirective::Appliquee => "appliquée",
            EtatDirective::Indeterminee => "indéterminée",
        }
    }
}

/// Le sujet de commande, et le sujet d'accusés qui lui répond.
pub struct SujetDeCommande {
    /// Directives écrites, dans l'ordre d'écriture (M1 sur le sujet).
    journal: Vec<Directive>,
    /// Époque de la dernière directive **appliquée** par chaque agent.
    epoque_par_agent: Vec<u64>,
    /// Accusés reçus, par époque.
    accuses: Vec<(u64, u32)>,
    /// Nombre d'accusés à partir duquel l'état passe à « appliquée ».
    pub a_min: u32,
    /// Latence du chemin de commande — **la même** que celle du travail
    /// ordinaire (PD4).
    pub latence: Duree,
    /// Directives rejetées pour époque périmée. Leur existence est ce qui rend
    /// D1 observable.
    pub rejets_pour_epoque: u64,
    prochaine_epoque: u64,
}

impl SujetDeCommande {
    /// Sujet neuf pour `n` agents, avec son seuil d'accusés et sa latence.
    pub fn nouveau(n: u32, a_min: u32, latence: Duree) -> SujetDeCommande {
        SujetDeCommande {
            journal: Vec::new(),
            epoque_par_agent: vec![0; n as usize],
            accuses: Vec::new(),
            a_min,
            latence,
            rejets_pour_epoque: 0,
            prochaine_epoque: 1,
        }
    }

    /// Arme D1 et D2. `horizon` est la condition de D2 : sans elle, l'énoncé
    /// ne serait pas testable.
    pub fn armer_oracles(&self, registre: &mut Registre, horizon: Duree) {
        registre.armer(Oracle::surete(D1, "§6.3"));
        // **Vivacité conditionnelle** : elle ne s'énonce jamais nue. La
        // condition est la latence du chemin de commande, et l'horizon en
        // découle (PD2, EX-C11).
        registre.armer(Oracle::vivacite_bornee(D2, horizon, "§6.3"));
    }

    /// Les directives écrites, dans l'ordre d'écriture.
    pub fn journal(&self) -> &[Directive] {
        &self.journal
    }

    /// PD4 — l'utilisateur **écrit dans le journal**. Il n'y a pas d'autre
    /// chemin, et la directive n'est pas appliquée à l'écriture : elle le sera
    /// quand les agents la liront.
    pub fn ecrire(&mut self, reglage: &str, valeur: f64, maintenant: Instant) -> Directive {
        let d = Directive {
            epoque: self.prochaine_epoque,
            reglage: reglage.to_string(),
            valeur,
            ecrite_a: maintenant,
        };
        self.prochaine_epoque += 1;
        self.journal.push(d.clone());
        d
    }

    /// Un agent lit et applique une directive.
    ///
    /// **D1** — une directive d'époque inférieure à celle que l'agent a déjà
    /// appliquée est rejetée. C'est ce qui rend l'ordre inutile à garantir : le
    /// milieu ne promet aucun ordre entre partitions (M2), et l'époque suffit.
    pub fn appliquer(&mut self, agent: u32, d: &Directive, maintenant: Instant) -> bool {
        let i = agent as usize;
        if i >= self.epoque_par_agent.len() {
            return false;
        }
        if d.epoque <= self.epoque_par_agent[i] {
            self.rejets_pour_epoque += 1;
            return false;
        }
        // Le chemin de commande subit la même latence que le travail ordinaire.
        if maintenant < d.ecrite_a + self.latence {
            return false;
        }
        self.epoque_par_agent[i] = d.epoque;
        match self.accuses.iter_mut().find(|(e, _)| *e == d.epoque) {
            Some((_, n)) => *n += 1,
            None => self.accuses.push((d.epoque, 1)),
        }
        true
    }

    /// Nombre d'accusés reçus pour une époque (EX-V03).
    pub fn accuses(&self, epoque: u64) -> u32 {
        self.accuses
            .iter()
            .find(|(e, _)| *e == epoque)
            .map(|(_, n)| *n)
            .unwrap_or(0)
    }

    /// EX-V04 — l'état d'une directive, et il n'y en a que deux.
    pub fn etat(&self, epoque: u64) -> EtatDirective {
        if self.accuses(epoque) >= self.a_min {
            EtatDirective::Appliquee
        } else {
            EtatDirective::Indeterminee
        }
    }

    /// EX-V03 — le **retard entre l'écriture et l'application effective**.
    /// C'est la grandeur que PD4 rend visible : le curseur de l'utilisateur
    /// n'est pas plus rapide que le reste.
    pub fn retard(&self, epoque: u64, maintenant: Instant) -> Option<Duree> {
        let d = self.journal.iter().find(|d| d.epoque == epoque)?;
        if self.accuses(epoque) == 0 {
            return None;
        }
        Some(maintenant - d.ecrite_a)
    }

    /// D2 — arme ou satisfait l'attente selon que tous les agents ont accusé.
    pub fn suivre_vivacite(&self, registre: &mut Registre, epoque: u64, maintenant: Instant) {
        if self.accuses(epoque) as usize >= self.epoque_par_agent.len() {
            registre.satisfaire(D2);
        } else {
            registre.attendre(
                D2,
                maintenant,
                format!(
                    "directive d'époque {epoque} : {} accusé(s) sur {} — condition : latence du \
                     chemin de commande, {} tics",
                    self.accuses(epoque),
                    self.epoque_par_agent.len(),
                    self.latence.0
                ),
            );
        }
    }

    /// D1 — vérifie qu'aucun agent ne porte une époque supérieure à la plus
    /// haute écrite.
    pub fn verifier_d1(&self, registre: &mut Registre, maintenant: Instant) {
        let max_ecrite = self.journal.iter().map(|d| d.epoque).max().unwrap_or(0);
        for (i, e) in self.epoque_par_agent.iter().enumerate() {
            if *e > max_ecrite {
                registre.violer(
                    D1,
                    maintenant,
                    format!("agent {i} porte l'époque {e}, supérieure à toute directive écrite"),
                );
                return;
            }
        }
    }

    /// EX-V19 — l'affichage d'une action sur n : le rééquilibrage déclenché,
    /// son compte de messages et son compte de tours, plus le retard subi.
    pub fn affichage_v19(
        &self,
        epoque: u64,
        maintenant: Instant,
        messages: u64,
        tours: u64,
    ) -> String {
        format!(
            "directive d'époque {epoque} : {} — {} accusé(s) sur {} ; retard {} ; le \
             rééquilibrage déclenché coûte {messages} message(s) et {tours} tour(s). \
             L'utilisateur qui redimensionne l'essaim subit le même retard que le travail \
             ordinaire (PD4).",
            self.etat(epoque).libelle(),
            self.accuses(epoque),
            self.epoque_par_agent.len(),
            match self.retard(epoque, maintenant) {
                Some(r) => format!("{} tics", r.0),
                None => "non encore mesurable".to_string(),
            },
        )
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn sujet() -> SujetDeCommande {
        SujetDeCommande::nouveau(4, 3, Duree(100))
    }

    /// PD4 — écrire une directive ne l'applique pas. Elle passe par le journal,
    /// et le retard est celui du travail ordinaire.
    #[test]
    fn ecrire_une_directive_ne_lapplique_pas() {
        let mut s = sujet();
        let d = s.ecrire("n", 32.0, Instant(0));
        assert_eq!(s.accuses(d.epoque), 0);
        assert_eq!(s.etat(d.epoque), EtatDirective::Indeterminee);

        // Avant la latence, aucun agent ne peut l'appliquer.
        assert!(!s.appliquer(0, &d, Instant(50)));
        assert!(s.appliquer(0, &d, Instant(100)));
        assert_eq!(s.accuses(d.epoque), 1);
    }

    /// EX-V04 — il n'y a que deux états, et « appliquée » exige a_min accusés.
    #[test]
    fn une_directive_est_appliquee_ou_indeterminee_et_rien_dautre() {
        let mut s = sujet();
        let d = s.ecrire("n", 32.0, Instant(0));
        for agent in 0..2 {
            s.appliquer(agent, &d, Instant(200));
        }
        assert_eq!(
            s.etat(d.epoque),
            EtatDirective::Indeterminee,
            "2 < a_min = 3"
        );
        s.appliquer(2, &d, Instant(200));
        assert_eq!(s.etat(d.epoque), EtatDirective::Appliquee);

        // Même tous accusés, le libellé ne devient jamais « appliquée à 100 % ».
        s.appliquer(3, &d, Instant(200));
        assert_eq!(s.etat(d.epoque).libelle(), "appliquée");
    }

    /// D1 — une directive d'époque inférieure est rejetée, quel que soit l'ordre
    /// dans lequel elle arrive. C'est ce qui dispense d'exiger un ordre du
    /// milieu, que M2 refuse de fournir.
    #[test]
    fn d1_une_epoque_inferieure_est_rejetee() {
        let mut s = sujet();
        let d1 = s.ecrire("n", 16.0, Instant(0));
        let d2 = s.ecrire("n", 32.0, Instant(10));

        // L'agent reçoit la plus récente en premier — M2 l'autorise.
        assert!(s.appliquer(0, &d2, Instant(200)));
        assert!(!s.appliquer(0, &d1, Instant(200)), "époque périmée");
        assert_eq!(s.rejets_pour_epoque, 1);

        let mut r = Registre::nouveau();
        s.armer_oracles(&mut r, Duree(1_000));
        s.verifier_d1(&mut r, Instant(200));
        assert!(r.violations().is_empty());
    }

    /// D2 — la vivacité ne s'énonce **jamais** sans sa condition.
    #[test]
    fn d2_est_une_vivacite_conditionnelle() {
        let mut s = sujet();
        let mut r = Registre::nouveau();
        s.armer_oracles(&mut r, Duree(10_000));
        let d = s.ecrire("n", 32.0, Instant(0));

        s.suivre_vivacite(&mut r, d.epoque, Instant(0));
        assert_eq!(r.attentes_ouvertes(), 1);

        for agent in 0..4 {
            s.appliquer(agent, &d, Instant(200));
        }
        s.suivre_vivacite(&mut r, d.epoque, Instant(200));
        assert_eq!(r.attentes_ouvertes(), 0);
        assert!(r.violations().is_empty());
    }

    /// … et son horizon dépassé est une violation, comme toute vivacité bornée.
    #[test]
    fn d2_viole_si_son_horizon_est_depasse() {
        let mut s = sujet();
        let mut r = Registre::nouveau();
        s.armer_oracles(&mut r, Duree(500));
        let d = s.ecrire("n", 32.0, Instant(0));
        s.suivre_vivacite(&mut r, d.epoque, Instant(0));
        r.echoir(Instant(501));
        assert_eq!(r.violations().len(), 1);
    }

    /// EX-V03, EX-V19 — le retard est mesuré et affiché, avec le coût du
    /// rééquilibrage déclenché.
    #[test]
    fn le_retard_et_le_cout_du_reequilibrage_sont_affiches() {
        let mut s = sujet();
        let d = s.ecrire("n", 32.0, Instant(0));
        assert_eq!(
            s.retard(d.epoque, Instant(150)),
            None,
            "aucun accusé encore"
        );
        s.appliquer(0, &d, Instant(150));
        assert_eq!(s.retard(d.epoque, Instant(150)), Some(Duree(150)));

        let a = s.affichage_v19(d.epoque, Instant(150), 128, 4);
        assert!(a.contains("128 message"), "{a}");
        assert!(a.contains("4 tour"), "{a}");
        assert!(a.contains("même retard que le travail ordinaire"), "{a}");
        assert!(a.contains("indéterminée"), "{a}");
    }
}
