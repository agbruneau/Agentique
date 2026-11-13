"""Chapitre 35, section 35.2 : dates d'application de l'AI Act après le Digital Omnibus."""
from dessin import Dessin, BLEU, GRIS, TRAIT, OCRE

d = Dessin(hauteur=250)

# Axe proportionnel au temps : 2 août 2025 (mois 0) à 2 août 2028 (mois 36).
X0, X1, Y = 110, 770, 135


def x(mois):
    return X0 + (X1 - X0) * mois / 36


d.trait(X0 - 40, Y, X1 + 40, Y, couleur=TRAIT, epaisseur=1.6)

# (mois, date, lignes de l'objet, effet, couleur, au-dessus de l'axe ?)
jalons = [
    (0, "2 août 2025", ["Modèles GPAI"], "Inchangé", GRIS, True),
    (12, "2 août 2026", ["Transparence (art. 50)"], "Inchangé", GRIS, False),
    (16, "2 décembre 2026", ["Marquage (art. 50(2)), délai transitoire",
                             "Nouvelles interdictions (art. 5)"], "Nouveau", BLEU, True),
    (24, "2 août 2027", ["Bac à sable par État membre"], "Reporté", OCRE, False),
    (28, "2 décembre 2027", ["Haut risque, annexe III"], "Reporté", OCRE, True),
    (36, "2 août 2028", ["Haut risque, annexe I"], "Reporté", OCRE, False),
]

for mois, date, objet, effet, couleur, haut in jalons:
    cx = x(mois)
    d.cercle(cx, Y, 6, fond="#ffffff", trait=couleur, epaisseur=2)
    if haut:
        d.trait(cx, Y - 8, cx, Y - 49 + 15 * (len(objet) - 1), couleur=TRAIT)
        d.texte(cx, Y - 94, effet.upper(), 10.5, gras=True, couleur=couleur)
        d.texte(cx, Y - 75, date, 12.5, gras=True)
        for i, ligne in enumerate(objet):
            d.texte(cx, Y - 57 + 15 * i, ligne, 11, couleur=GRIS)
    else:
        d.trait(cx, Y + 8, cx, Y + 22, couleur=TRAIT)
        d.texte(cx, Y + 40, date, 12.5, gras=True)
        d.texte(cx, Y + 58, objet[0], 11, couleur=GRIS)
        d.texte(cx, Y + 78, effet.upper(), 10.5, gras=True, couleur=couleur)

d.ecrit("fig-35-e1")
