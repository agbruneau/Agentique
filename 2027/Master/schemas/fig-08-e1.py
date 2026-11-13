"""Chapitre 8, section 8.2 : trois modèles de découverte (centralisé, fédéré, distribué),
distingués par l'endroit où réside l'index (tableau de la section)."""
import math
from dessin import Dessin, MARINE, BLEU, FOND, NEUTRE, GRIS, TRAIT

d = Dessin(hauteur=300)

PY, PH, PL = 14, 272, 262                 # panneaux : haut, hauteur, largeur
PANNEAUX = [30, 309, 588]
Y_TITRE, Y_HAUT, Y_BAS = PY + 30, PY + 62, PY + 138

modeles = [
    ("Centralisé", ["Un dépôt unique, public ou interne"]),
    ("Fédéré", ["Chaque domaine publie; des registres", "indexent et se renvoient les requêtes"]),
    ("Distribué", ["Un réseau pair-à-pair", "sans opérateur central"]),
]

for x, (nom, index) in zip(PANNEAUX, modeles):
    cx = x + PL / 2
    d.rect(x, PY, PL, PH, "#ffffff", TRAIT)
    d.texte(cx, Y_TITRE, nom, 14, True, MARINE)
    d.trait(x + 20, PY + 196, x + PL - 20, PY + 196, TRAIT, 0.8)
    d.texte(cx, PY + 218, "Où réside l'index", 10.5, True, GRIS)
    for k, ligne in enumerate(index):
        d.texte(cx, PY + 240 + k * 16, ligne, 11.5, False, MARINE)

# --- Centralisé : des éditeurs inscrivent dans un index unique
cx = PANNEAUX[0] + PL / 2
LE, HE = 72, 26
for dx in (-86, 0, 86):
    d.boite(cx + dx - LE / 2, Y_HAUT, LE, HE, "éditeur", fond=NEUTRE, trait=TRAIT, taille=11,
            couleur=GRIS)
    d.fleche(cx + dx, Y_HAUT + HE, cx + dx * 0.5, Y_BAS, couleur=TRAIT)
d.boite(cx - 80, Y_BAS, 160, 42, "Index unique", fond=FOND, trait=BLEU, taille=13)

# --- Fédéré : chaque domaine publie, plusieurs registres indexent et se renvoient les requêtes
cx = PANNEAUX[1] + PL / 2
LR, HR = 92, 42
r1, r2 = cx - 26 - LR, cx + 26          # bords gauches des deux registres
for dx in (-86, 0, 86):
    d.boite(cx + dx - LE / 2, Y_HAUT, LE, HE, "domaine", fond=NEUTRE, trait=TRAIT, taille=11,
            couleur=GRIS)
d.fleche(cx - 86, Y_HAUT + HE, cx - 86, Y_BAS, couleur=TRAIT)
d.fleche(cx + 86, Y_HAUT + HE, cx + 86, Y_BAS, couleur=TRAIT)
d.fleche(cx - 10, Y_HAUT + HE, cx - 40, Y_BAS, couleur=TRAIT)
d.fleche(cx + 10, Y_HAUT + HE, cx + 40, Y_BAS, couleur=TRAIT)
d.boite(r1, Y_BAS, LR, HR, "registre", fond=FOND, trait=BLEU, taille=12.5)
d.boite(r2, Y_BAS, LR, HR, "registre", fond=FOND, trait=BLEU, taille=12.5)
d.fleche(r1 + LR, Y_BAS + HR / 2, r2, Y_BAS + HR / 2, couleur=BLEU, double=True)

# --- Distribué : des pairs reliés entre eux, sans nœud central
cx = PANNEAUX[2] + PL / 2
cy, R, r = PY + 116, 58, 18
pts = [(cx + R * math.cos(math.radians(-90 + 72 * k)),
        cy + R * 0.82 * math.sin(math.radians(-90 + 72 * k))) for k in range(5)]
for a, b in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (1, 3), (1, 4)]:
    d.trait(*pts[a], *pts[b], TRAIT, 1.2)
for (px, py) in pts:
    d.cercle(px, py, r, FOND, BLEU, 1.3)
    d.texte(px, py + 4, "pair", 10.5, False, MARINE)

d.ecrit("fig-08-e1")
