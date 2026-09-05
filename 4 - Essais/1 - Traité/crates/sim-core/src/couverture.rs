//! Couverture conditionnelle (EX-C08) — et le refus d'en faire une complétude
//! (EX-C10b).
//!
//! > L'espace de recherche étant effectivement infini, exécuter davantage de
//! > tests couvre davantage de code et trouve davantage de défauts, sans
//! > qu'aucun critère de complétude existe. (§3.3, algorithme 3.3, étape 7)
//!
//! Ce qui se mesure est donc : combien d'**exécutions distinctes** ont atteint
//! une condition donnée. Ce qui ne se calcule pas, et n'apparaît nulle part
//! ici : un pourcentage de couverture.

use std::collections::BTreeMap;

/// Compteurs d'une seule exécution.
#[derive(Default, Clone, Debug)]
pub struct Couverture {
    comptes: BTreeMap<&'static str, u64>,
}

impl Couverture {
    /// Couverture vide : aucune condition déclarée ni atteinte.
    pub fn nouvelle() -> Couverture {
        Couverture::default()
    }

    /// Signale qu'une condition nommée a été atteinte.
    pub fn atteindre(&mut self, condition: &'static str) {
        *self.comptes.entry(condition).or_insert(0) += 1;
    }

    /// Déclare une condition **sans l'atteindre**, pour qu'elle apparaisse à
    /// zéro plutôt que d'être absente. Une condition absente du rapport se lit
    /// comme une condition qu'on n'a pas cherchée ; une condition à zéro se lit
    /// comme un trou — et c'est le second message qui est vrai (PD6).
    pub fn declarer(&mut self, condition: &'static str) {
        self.comptes.entry(condition).or_insert(0);
    }

    /// Toutes les conditions, déclarées comprises, dans l'ordre des noms.
    pub fn comptes(&self) -> &BTreeMap<&'static str, u64> {
        &self.comptes
    }

    /// Compte d'une condition. Zéro si elle est déclarée sans être atteinte —
    /// et zéro aussi si elle n'est pas déclarée, ce que seul [`Couverture::comptes`]
    /// distingue.
    pub fn compte(&self, condition: &str) -> u64 {
        self.comptes.get(condition).copied().unwrap_or(0)
    }
}

/// Agrégat sur une campagne : combien d'exécutions distinctes ont atteint
/// chaque condition.
#[derive(Default, Clone, Debug)]
pub struct Agregat {
    executions: u64,
    atteintes: BTreeMap<&'static str, u64>,
}

impl Agregat {
    /// Agrégat vide : aucune exécution absorbée.
    pub fn nouveau() -> Agregat {
        Agregat::default()
    }

    /// Absorbe la couverture d'une exécution. Une condition atteinte plusieurs
    /// fois dans la même exécution compte pour **une** : ce qu'EX-C08 mesure
    /// est le nombre d'exécutions distinctes, pas le nombre d'occurrences.
    pub fn absorber(&mut self, c: &Couverture) {
        self.executions += 1;
        for (condition, compte) in c.comptes() {
            let e = self.atteintes.entry(condition).or_insert(0);
            if *compte > 0 {
                *e += 1;
            }
        }
    }

    /// Nombre d'exécutions absorbées — le dénominateur d'EX-C08.
    pub fn executions(&self) -> u64 {
        self.executions
    }

    /// Pour chaque condition, le nombre d'**exécutions distinctes** qui l'ont
    /// atteinte.
    pub fn atteintes(&self) -> &BTreeMap<&'static str, u64> {
        &self.atteintes
    }

    /// Conditions à compte nul ou faible (EX-C08 : « signalent celles à compte
    /// nul ou faible »).
    ///
    /// NF-13 : sur 1 000 graines, une condition jamais atteinte est un
    /// **avertissement de campagne**, pas un échec de test. Le message le dit,
    /// pour que personne ne le convertisse en verdict.
    pub fn faibles(&self, seuil: u64) -> Vec<String> {
        self.atteintes
            .iter()
            .filter(|(_, n)| **n <= seuil)
            .map(|(condition, n)| {
                if *n == 0 {
                    format!(
                        "« {condition} » n'a été atteinte par aucune des {} exécutions — \
                         avertissement de campagne (NF-13), pas un échec : la condition peut \
                         être inatteignable, ou le modèle de faute peut ne pas savoir la \
                         produire (PD6)",
                        self.executions
                    )
                } else {
                    format!(
                        "« {condition} » atteinte par {n} exécution(s) sur {} — sous le seuil \
                         de {seuil}",
                        self.executions
                    )
                }
            })
            .collect()
    }

    /// Ce que le rapport de couverture ne dit pas (EX-C10b). Le texte est
    /// affiché tel quel, et il n'existe aucune fonction qui rende un
    /// pourcentage de couverture.
    pub fn mention_obligatoire() -> &'static str {
        "Aucun critère de complétude n'existe : l'espace de recherche est effectivement infini \
         (§3.3, étape 7). Ces comptes disent ce qui a été atteint, jamais ce qui reste."
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn une_condition_declaree_apparait_a_zero() {
        let mut c = Couverture::nouvelle();
        c.declarer("ISR réduit au meneur");
        assert_eq!(c.compte("ISR réduit au meneur"), 0);
        assert!(c.comptes().contains_key("ISR réduit au meneur"));
    }

    /// EX-C08 — ce qui compte est le nombre d'exécutions distinctes, et non le
    /// nombre d'occurrences dans une même exécution.
    #[test]
    fn lagregat_compte_les_executions_pas_les_occurrences() {
        let mut a = Agregat::nouveau();
        let mut c = Couverture::nouvelle();
        for _ in 0..100 {
            c.atteindre("partition en cours");
        }
        a.absorber(&c);
        assert_eq!(a.atteintes()["partition en cours"], 1);
        assert_eq!(a.executions(), 1);
    }

    #[test]
    fn une_condition_jamais_atteinte_est_signalee_comme_avertissement() {
        let mut a = Agregat::nouveau();
        let mut c = Couverture::nouvelle();
        c.declarer("élection d'un non-membre de l'ISR");
        c.atteindre("écriture validée");
        for _ in 0..10 {
            a.absorber(&c);
        }
        let f = a.faibles(0);
        assert_eq!(f.len(), 1);
        assert!(f[0].contains("aucune"), "{}", f[0]);
        assert!(f[0].contains("NF-13"), "{}", f[0]);
    }

    /// EX-C10b — la mention refuse le critère de complétude, en toutes lettres.
    ///
    /// Le nom de ce test annonçait « aucune fonction ne rend un pourcentage de
    /// couverture », propriété qu'aucune assertion ne vérifie et qu'aucune
    /// assertion **ne peut** vérifier de l'intérieur : elle est tenue par le
    /// type, qui n'expose pas de ratio. Ce que le test vérifie réellement est la
    /// mention, et il est nommé pour cela.
    #[test]
    fn la_mention_obligatoire_refuse_le_critere_de_completude() {
        assert!(Agregat::mention_obligatoire().contains("Aucun critère de complétude"));
    }
}
