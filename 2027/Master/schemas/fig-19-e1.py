"""Chapitre 19, section 19.7 : orchestration et chorégraphie côte à côte.

En orchestration, un coordinateur détient le plan et déclenche les étapes.
En chorégraphie, chaque participant réagit aux événements des autres; le plan n'est écrit nulle part.
"""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, TRAIT

d = Dessin(hauteur=300)

# ---- Orchestration (gauche)
d.surtitre(40, 32, "Orchestration")
d.boite(130, 48, 200, 64, "Coordinateur", "détient le plan", taille_corps=11.5)
AY, AH, AL = 186, 48, 110
AX = [40, 175, 310]
for x in AX:
    d.boite(x, AY, AL, AH, "Agent", fond=NEUTRE, trait=GRIS)
d.fleche(180, 112, 95, AY, couleur=BLEU)
d.fleche(230, 112, 230, AY, couleur=BLEU)
d.fleche(280, 112, 365, AY, couleur=BLEU)
d.paragraphe(230, 268, "Le coordinateur déclenche les étapes", 380, taille=11.5)

# ---- Séparation
d.trait(440, 28, 440, 280, TRAIT, 1, tirets=True)

# ---- Chorégraphie (droite)
d.surtitre(470, 32, "Chorégraphie")
H = (595, 56)          # agent du haut (x, y)
G = (470, AY)          # agent en bas à gauche
D = (720, AY)          # agent en bas à droite
for (x, y) in (H, G, D):
    d.boite(x, y, AL, AH, "Agent", fond=NEUTRE, trait=GRIS)
# Événements publiés, auxquels les autres réagissent
d.fleche(605, 104, 540, AY, couleur=GRIS, tirets=True)
d.fleche(695, 104, 760, AY, couleur=GRIS, tirets=True)
d.fleche(580, AY + 24, 720, AY + 24, couleur=GRIS, tirets=True)
d.texte(650, 150, "aucun plan écrit", 11.5, False, GRIS, italique=True)
d.paragraphe(650, 268, "Chaque agent réagit aux événements des autres", 380, taille=11.5)

d.ecrit("fig-19-e1")
