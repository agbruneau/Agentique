"""Chapitre 36, section 36.2 : autorité réelle et autorité apparente d'un agent logiciel."""
from dessin import (Dessin, MARINE, GRIS, TRAIT, NEUTRE, VERT, FOND_VERT, ROUGE, FOND_ROUGE)

d = Dessin(hauteur=310)

# Autorité apparente : ce que le tiers perçoit (cadre extérieur).
OX, OY, OL, OH = 270, 20, 340, 270
d.rect(OX, OY, OL, OH, fond=FOND_ROUGE, trait=ROUGE, tirets=True)
cx = OX + OL / 2
d.texte(cx, OY + 28, "Autorité apparente", 13.5, gras=True)
d.texte(cx, OY + 47, "ce que le tiers perçoit", 11, couleur=GRIS)
d.texte(cx, OY + 64, "canal, marque, carte d'agent, absence de limite annoncée", 10.5,
        couleur=GRIS)

# Autorité réelle : ce qui est configuré (cadre intérieur).
IX, IY, IL, IH = 320, 110, 240, 100
d.boite(IX, IY, IL, IH, "Autorité réelle",
        "ce qui est configuré : portées, politiques, mandats signés",
        fond=FOND_VERT, trait=VERT, taille=13.5, taille_corps=11)

# L'écart entre les deux cadres.
d.texte(cx, OY + OH - 42, "Écart : le risque juridique", 12.5, gras=True, couleur=ROUGE)
d.texte(cx, OY + OH - 23, "un acte non permis peut lier le mandant", 11, couleur=GRIS)

# Mandant et tiers.
MY = IY + IH / 2
d.boite(30, MY - 40, 170, 80, "Mandant", "la personne qui\ndéploie l'agent", fond=NEUTRE,
        trait=TRAIT)
d.boite(680, MY - 40, 170, 80, "Tiers", "croit raisonnablement l'agent autorisé", fond=NEUTRE,
        trait=TRAIT)
d.fleche(200, MY, IX, MY)
d.texte(235, MY - 8, "configure", 11, couleur=GRIS)
d.fleche(680, MY, OX + OL, MY, "perçoit", decalage=-8, taille=11)

d.ecrit("fig-36-e1")
