"""Chapitre 18, section 18.4 : le patron Saga.

Transactions locales T1 à T3, échec de T3, compensations en ordre inverse (C2 puis C1),
et l'état intermédiaire visible entre chaque étape et sa compensation.
"""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, ROUGE, FOND_ROUGE, OCRE

d = Dessin(hauteur=254)

Y, H, L = 52, 64, 130
X = [45, 210, 375, 540, 705]          # T1, T2, T3, C2, C1

d.surtitre(X[0], 36, "Transactions locales")
d.surtitre(X[3], 36, "Compensations, en ordre inverse", couleur=GRIS)

d.boite(X[0], Y, L, H, "T1", "validée")
d.boite(X[1], Y, L, H, "T2", "validée")
d.boite(X[2], Y, L, H, "T3", "échec", fond=FOND_ROUGE, trait=ROUGE, couleur=ROUGE)
d.boite(X[3], Y, L, H, "C2", "compense T2", fond=NEUTRE, trait=GRIS)
d.boite(X[4], Y, L, H, "C1", "compense T1", fond=NEUTRE, trait=GRIS)

cy = Y + H / 2
for i in range(4):
    d.fleche(X[i] + L, cy, X[i + 1], cy, couleur=ROUGE if i == 2 else GRIS)

# Accolades : entre une étape et sa compensation, l'état intermédiaire est visible.
bas = Y + H
def accolade(xa, xb, y):
    d.trait(xa, bas + 6, xa, y, OCRE, tirets=True)
    d.trait(xb, bas + 6, xb, y, OCRE, tirets=True)
    d.trait(xa, y, xb, y, OCRE, tirets=True)

accolade(X[1] + L / 2, X[3] + L / 2, bas + 30)
accolade(X[0] + L / 2, X[4] + L / 2, bas + 58)

d.texte(440, bas + 92, "État intermédiaire visible entre une étape et sa compensation", 12.5,
        True, OCRE)
d.texte(440, bas + 114, "Un autre agent peut lire une réservation qui sera annulée, "
        "et décider sur cette base", 11.5, False, GRIS)

d.ecrit("fig-18-e1")
