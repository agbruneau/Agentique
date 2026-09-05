# Implémentation de référence de la politique de délégation (§ 7.2) et de la
# machine d'états (§ 6.4) de l'article « Projection de l'état de ressource et
# délégation multicritère dans une plateforme HPC à processeurs quantiques ».
#
# Rejoue les déroulés A et B du § 7.5, l'analyse de sensibilité du § 7.5.1, et
# vérifie la totalité de la table de transitions (36 cases) ainsi que les gardes
# de sortie de hors_service. Toute divergence fait échouer une assertion : c'est
# l'exécution de la condition de réfutation RÉF-6.
#
# Usage : python rejeu-politique.py

# ---------------------------------------------------------------- politique § 7

# direction d'optimisation par critère (C1..C5)
DIRECTIONS = ("min", "max", "min", "max", "min")

POIDS = {
    "interactive": (0.40, 0.20, 0.05, 0.30, 0.05),
    "standard":    (0.25, 0.30, 0.15, 0.20, 0.10),
    "precision":   (0.10, 0.55, 0.10, 0.15, 0.10),
}


def normaliser(valeurs, direction):
    bas, haut = min(valeurs), max(valeurs)
    if haut == bas:
        return [1.000] * len(valeurs)  # § 7.2 : un critère qui ne discrimine pas vaut 1
    if direction == "max":
        return [(v - bas) / (haut - bas) for v in valeurs]
    return [(haut - v) / (haut - bas) for v in valeurs]


def politique(candidats, classe, poids=None):
    """candidats : liste de (identifiant, (C1..C5), fidelite_attendue).
    Toutes les candidates sont supposées déjà éligibles (étape 1 franchie).
    Retourne (identifiant retenu, {identifiant: score})."""
    w = poids if poids is not None else POIDS[classe]
    par_critere = list(zip(*(c[1] for c in candidats)))
    normes = [normaliser(vals, d) for vals, d in zip(par_critere, DIRECTIONS)]
    scores = {
        c[0]: sum(w[k] * normes[k][i] for k in range(5))
        for i, c in enumerate(candidats)
    }
    meilleur = max(scores.values())
    gagnants = [c for c in candidats if scores[c[0]] == meilleur]
    # départage lexicographique total : fidélité desc, temps asc, coût asc, id asc
    retenue = min(gagnants, key=lambda c: (-c[2], c[1][0], c[1][2], c[0]))
    return retenue[0], scores


# ------------------------------------------------------- machine d'états § 6.4

ETATS = ("disponible", "etalonnage", "degrade", "hors_service")
EVENEMENTS = ("E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9")

# (état, événement) -> fonction (cause) -> (nouvel état, nouvelle cause)
# None = sans effet (case « — » : renseignée, pas indéfinie).
TABLE = {
    ("disponible", "E1"): lambda c: ("etalonnage", c),
    ("disponible", "E2"): None,
    ("disponible", "E3"): lambda c: ("degrade", c),
    ("disponible", "E4"): None,
    ("disponible", "E5"): lambda c: ("hors_service", "perte_contact"),
    ("disponible", "E6"): None,
    ("disponible", "E7"): lambda c: ("hors_service", "retrait"),
    ("disponible", "E8"): None,
    ("disponible", "E9"): lambda c: ("degrade", c),
    ("etalonnage", "E1"): None,
    # ⚠ La table publiée (§ 6.4) écrit « → D si conforme, sinon → G ». Ce script
    # n'a PAS d'entrée de conformité : il n'implante que la branche conforme,
    # et la branche « sinon → G » n'est exercée par aucune assertion. Sur les
    # trente-six cases, trente-cinq sont rejouées entières ; celle-ci l'est à
    # moitié, et RÉF-6 ne porte donc pas sur la requalification en échec.
    # Relevé par l'audit du 2 septembre 2026 ; à lever en donnant au rejeu un
    # verdict d'étalonnage en entrée.
    ("etalonnage", "E2"): lambda c: ("disponible", c),
    ("etalonnage", "E3"): None,
    ("etalonnage", "E4"): None,
    ("etalonnage", "E5"): lambda c: ("hors_service", "perte_contact"),
    ("etalonnage", "E6"): None,
    ("etalonnage", "E7"): lambda c: ("hors_service", "retrait"),
    ("etalonnage", "E8"): None,
    ("etalonnage", "E9"): None,
    ("degrade", "E1"): lambda c: ("etalonnage", c),
    ("degrade", "E2"): None,
    ("degrade", "E3"): lambda c: ("degrade", c),  # mise à jour de la fidélité
    ("degrade", "E4"): lambda c: ("disponible", c),
    ("degrade", "E5"): lambda c: ("hors_service", "perte_contact"),
    ("degrade", "E6"): None,
    ("degrade", "E7"): lambda c: ("hors_service", "retrait"),
    ("degrade", "E8"): None,
    ("degrade", "E9"): None,
    ("hors_service", "E1"): None,
    ("hors_service", "E2"): None,
    ("hors_service", "E3"): None,
    ("hors_service", "E4"): None,
    ("hors_service", "E5"): None,
    ("hors_service", "E6"): lambda c: ("etalonnage", c) if c == "perte_contact" else None,
    ("hors_service", "E7"): lambda c: ("hors_service", "retrait"),  # maj. cause
    ("hors_service", "E8"): lambda c: ("etalonnage", c) if c == "retrait" else None,
    ("hors_service", "E9"): None,
}


def transition(etat, cause, evenement):
    effet = TABLE[(etat, evenement)]
    if effet is None:
        return etat, cause
    resultat = effet(cause)
    return (etat, cause) if resultat is None else resultat


# ---------------------------------------------------------------------- rejeu

def approx(a, b, tol=6e-4):
    return abs(a - b) < tol


def rejouer():
    # Déroulé A (§ 7.5.1) — noyau fixe, classe standard
    parc_a = [
        ("QPU-A", (900, 0.97, 120, 0.95, 0.5), 0.97),
        ("QPU-B", (300, 0.88, 60, 0.80, 0.5), 0.88),
        ("SIM-GPU", (5400, 1.00, 40, 0.99, 12.0), 1.00),
    ]
    retenue, s = politique(parc_a, "standard")
    assert retenue == "QPU-A", f"Déroulé A : {retenue} au lieu de QPU-A"
    assert approx(s["QPU-A"], 0.703) and approx(s["QPU-B"], 0.463) \
        and approx(s["SIM-GPU"], 0.650), f"Déroulé A : scores {s}"

    # Sensibilité (§ 7.5.1) — w2 0,30 → 0,40 aux dépens de w1
    retenue, s = politique(parc_a, "standard", poids=(0.15, 0.40, 0.15, 0.20, 0.10))
    assert retenue == "SIM-GPU" and approx(s["SIM-GPU"], 0.750) \
        and approx(s["QPU-A"], 0.690), f"Sensibilité : {retenue}, {s}"

    # Déroulé B (§ 7.5.2) — campagne variationnelle, classe interactive
    parc_b = [
        ("QPU-A", (3600, 0.97, 480, 0.95, 8.0), 0.97),
        ("QPU-B", (1800, 0.88, 240, 0.80, 4.0), 0.88),
        ("SIM-GPU", (14400, 1.00, 160, 0.99, 40.0), 1.00),
    ]
    retenue, s = politique(parc_b, "interactive")
    assert retenue == "QPU-A", f"Déroulé B : {retenue} au lieu de QPU-A"
    assert approx(s["QPU-A"], 0.774) and approx(s["QPU-B"], 0.488) \
        and approx(s["SIM-GPU"], 0.550), f"Déroulé B : scores {s}"

    # Totalité de la table (§ 6.4) : 4 états × 9 événements, aucune case absente
    assert set(TABLE) == {(e, v) for e in ETATS for v in EVENEMENTS}, "table non totale"
    assert len(TABLE) == 36

    # Gardes de hors_service : la séquence E7, E5, E6 ne remet pas en route
    etat, cause = transition("disponible", None, "E7")   # retrait -> H
    etat, cause = transition(etat, cause, "E5")          # sans effet
    etat, cause = transition(etat, cause, "E6")          # gardé : cause = retrait
    assert (etat, cause) == ("hors_service", "retrait"), "garde E6 en défaut"
    etat, cause = transition(etat, cause, "E8")          # seule sortie légitime
    assert etat == "etalonnage", "E8 doit sortir vers etalonnage"

    # Le retour de service passe par etalonnage, jamais par disponible
    for ev in ("E6", "E8"):
        for c in ("perte_contact", "retrait"):
            e2, _ = transition("hors_service", c, ev)
            assert e2 != "disponible", f"{ev}/{c} : retour direct en disponible"

    print("Rejeu conforme : déroulés A et B, sensibilité, table de transitions "
          "(36/36), gardes de hors_service. RÉF-6 non déclenchée.")


if __name__ == "__main__":
    rejouer()
