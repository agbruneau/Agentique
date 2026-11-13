"""Fig. 22-e1 : les positions de l'humain par rapport à l'action de l'agent (section 22.1)."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, MARINE, TRAIT

d = Dessin(hauteur=272)

X0, L, PAS = 40, 250, 275           # trois colonnes : avant, pendant, après
cols = [X0 + i * PAS for i in range(3)]
cx = [x + L / 2 for x in cols]

# ---- avant, pendant, après
for c, t in zip(cx, ["Avant", "Pendant", "Après"]):
    d.texte(c, 24, t, 12.5, True, BLEU)

# ---- trois positions
YB, HB = 36, 56
positions = [("Dans la boucle", "Validation avant exécution"),
             ("Sur la boucle", "Surveillance pendant l'exécution"),
             ("Hors de la boucle", "Revue après coup")]
for x, (titre, corps) in zip(cols, positions):
    d.boite(x, YB, L, HB, titre, corps, taille=13, taille_corps=11.5)

# ---- ligne du temps et action de l'agent
YT = 138
LA, HA = 170, 34
xa = cx[1] - LA / 2
d.trait(X0, YT, xa, YT, couleur=TRAIT, epaisseur=1.4)
d.fleche(xa + LA, YT, X0 + 3 * L + 2 * (PAS - L), YT, couleur=TRAIT)
d.boite(xa, YT - HA / 2, LA, HA, "Exécution de l'action", fond=NEUTRE, trait=GRIS, taille=12)
d.texte(840, YT + 20, "temps", 11, False, GRIS, ancre="end", italique=True)

# ---- moment d'intervention de chaque position
d.fleche(cx[0], YB + HB, cx[0], YT - 2, couleur=BLEU)
d.fleche(cx[1], YB + HB, cx[1], YT - HA / 2, couleur=BLEU)
d.fleche(cx[2], YB + HB, cx[2], YT - 2, couleur=BLEU)

# ---- aux commandes : englobe tout
d.boite(X0, 180, 800, 76, "Aux commandes",
        "Supervise l'activité d'ensemble, décide quand et comment utiliser le système, "
        "y compris de ne pas l'utiliser\nNe se délègue pas : une personne désignée fixe les "
        "limites de l'agent et peut l'arrêter",
        taille=13, taille_corps=11.5)

d.ecrit("fig-22-e1")
