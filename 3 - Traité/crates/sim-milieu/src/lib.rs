//! `sim-milieu` — le journal partitionné, et rien d'autre.
//!
//! Le milieu est ce dans quoi les agents déposent et lisent des traces. Il ne
//! connaît aucun algorithme d'agent et n'implante aucun protocole d'accord
//! (§5.1, DT7).
//!
//! **Périmètre à la clôture de la phase 5** : M1 à M4 (EX-M01 à EX-M04), la
//! latence du chemin de durabilité avec son ℓ₉₉ (EX-M09), les coûts propres du
//! milieu (EX-M13), la réplication ISR (EX-M05 à EX-M08, EX-M14, EX-M15), la
//! rétention et le compactage (EX-M10, EX-M20), le surcoût de format,
//! l'idempotence du producteur et le coût d'écriture d'un lot (EX-M11, EX-M12,
//! EX-M16), le groupe de consommation (EX-M17 à EX-M19, EX-M22, EX-M23) et le
//! plan de contrôle (EX-M21).
//!
//! **Ajouté en phase 6** : l'identité apposée à l'écriture (EX-M24, dans
//! [`journal`]), l'historique vérifié par identité ([`historique`], EX-M25) et
//! le quota par ressource ([`quota`], EX-M26). Les trois viennent du ch. 8 de la
//! deuxième édition du traité, qui les **propose** sans qu'aucune source ne les
//! mesure : ce que le milieu en offre est un coût et une condition d'échec, pas
//! une validation.
//!
//! Ce que le milieu **ne** produit **pas** est énuméré par [`hors_perimetre`].

#![deny(missing_docs)]
#![deny(rustdoc::broken_intra_doc_links)]

pub mod controle;
pub mod format;
pub mod groupe;
pub mod historique;
pub mod journal;
pub mod latence;
pub mod quota;
pub mod replication;

pub use controle::PlanDeControle;
pub use format::{Format, Producteur};
pub use groupe::{Groupe, Protocole};

pub use historique::Historique;
pub use journal::{
    Cle, Couts, Ecriture, Enregistrement, Identite, Milieu, Partition, M1, M2, M3, M4,
};
pub use quota::{Politique, Quotas};
pub use latence::{Latence, Mesures};
pub use replication::{Isr, Refus, Replique, R1, R2};

/// Ce que le milieu ne sait pas produire, à afficher au même rang que ce qu'il
/// sait produire (PD6). Un mécanisme absent a, dans tout résultat, une
/// probabilité de faute nulle — c'est le mode (b) du §3.2.
///
/// La distinction qui compte ici n'est pas « écrit / pas écrit » mais
/// « branché / pas branché » : un module que personne n'appelle a exactement le
/// même effet sur un résultat qu'un module qui n'existe pas.
pub fn hors_perimetre() -> &'static [&'static str] {
    &[
        "époques et arbitrage des écritures périmées — le milieu ne compare aucune \
         époque ; l'arbitrage vit côté agent (DT9)",
        "surcoût de format dans les octets comptés — `Format` retrouve les chiffres du \
         traité, mais `ecrire` facture une taille fixe et ne le consulte pas (EX-M11)",
        "tout le module `format` en exécution — le surcoût de lot (EX-M11), l'idempotence du \
         producteur (EX-M12) et le coût d'écriture d'un lot (EX-M16) sont des calculatrices \
         vérifiées par leurs tests ; `Producteur` et `CoutLot` n'ont aucun appelant, donc aucun \
         doublon n'est rejeté et aucun coût par enregistrement n'est facturé dans un résultat",
        "fonction de clé du milieu — `Milieu::partition_de` n'a d'appelant que son test : \
         `ecrire` range l'enregistrement dans la partition que l'écrivain nomme, et la \
         concentration d'un résultat vient du réglage du scénario, pas d'un hachage de clé",
        "refus d'un oracle au-delà de R (EX-M20) — `Milieu::verifier_horizon` et `Retention` \
         n'ont aucun appelant : aucun chargement ne refuse quoi que ce soit, et R n'existe dans \
         aucune exécution comme grandeur unique. `appliquer_retention` reçoit sa fenêtre en \
         paramètre",
        "temporisateur d'appartenance à l'ISR en exécution (EX-M14) — `Isr::avancer` n'a \
         d'appelant que ses tests ; le scénario D retire la réplique à la main. L'hypothèse \
         `replica.lag.time.max.ms` est donc déclarée au registre EX-C12 sans jamais y être \
         éprouvée, quelle que soit la trajectoire : le démenti annoncé — sous charge, \
         l'exclusion frappe un suiveur vivant — n'est produit que par un test unitaire",
        // Sans astérisques d'emphase, et sans retour à la ligne : egui n'a pas
        // d'analyseur Markdown et rendrait les deux littéralement.
        "réintégration dans l'ensemble synchronisé — le temporisateur ne décide que du \
         retrait, et aucune réplique retirée pour retard ne revient (EX-M14). |ISR| est donc \
         monotone décroissante hors élection hors ISR : EX-M08 réinitialise l'ISR au \
         nouveau meneur, ce qui la fait remonter de 0 à 1 sur la trajectoire du scénario D",
        "historique par identité (EX-M25) et quota par ressource (EX-M26) — implantés et \
         testés, aucun scénario ne les instancie : ni `scenario_m`, ni aucun autre",
        "prédicats des oracles du journal — M1 à M4 et M10 sont armés à chaque exécution, et \
         `Milieu::verifier`, `verifier_m4` et `verifier_m10` n'ont aucun appelant hors test ; \
         une violation ne pourrait donc pas arrêter l'exécution comme EX-C09 le décrit",
        "drapeau `Retention::compacte` — `Milieu::compacter` ne prend pas de politique et ne \
         le lit jamais : appelé, il compacte (EX-M10)",
        "durée du rééquilibrage — la barrière est posée et levée dans le même appel, \
         donc « aucune partition n'est servie » n'est observable par personne (EX-M17)",
        "révocation différenciée entre protocoles — les trois produisent la même \
         réattribution ; seuls les compteurs diffèrent (EX-M17)",
        "rétention, compactage, groupe de consommation et plan de contrôle en \
         exécution — implantés et testés, mais aucun scénario ne les appelle : ils \
         n'influencent aucun résultat affiché",
    ]
}

#[cfg(test)]
mod tests {
    /// PD6 — la liste est affichée telle quelle par l'onglet « Limites » de
    /// `sim-viz`, qui pose un `egui::RichText` sans analyseur Markdown. Des
    /// astérisques d'emphase s'y afficheraient littéralement, et un retour à la
    /// ligne y couperait la puce. Le commentaire au-dessus de la liste l'écrit
    /// depuis l'origine ; deux entrées l'ont violé quand même, d'où ce test.
    #[test]
    fn aucune_entree_ne_porte_de_balisage_markdown() {
        for e in super::hors_perimetre() {
            assert!(!e.contains('*'), "astérisque d'emphase : {e}");
            assert!(!e.contains('\n'), "retour à la ligne : {e}");
        }
    }
}
