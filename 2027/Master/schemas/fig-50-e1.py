"""Chapitre 50, section 50.2 : la dispersion des tailles de marché publiées, pour 2025 et pour
2030, sur une même échelle logarithmique. Valeurs des tableaux de la section, en G$ US."""
import math

from dessin import Dessin, BLEU, FOND, GRIS, TRAIT, MARINE

d = Dessin(hauteur=406)
X0, X1, VMIN, VMAX = 318, 850, 1.0, 2000.0


def x(v):
    return X0 + (X1 - X0) * (math.log10(v) - math.log10(VMIN)) / (math.log10(VMAX) - math.log10(VMIN))


# ---- Axe logarithmique
Y_HAUT, Y_AXE = 34, 374
for v in (1, 10, 100, 1000):
    d.trait(x(v), Y_HAUT, x(v), Y_AXE, couleur="#e3e7ee", epaisseur=1)
    d.texte(x(v), Y_AXE + 17, ("%d G$" % v).replace("1000", "1 000"), 11, False, GRIS)
for v in (2, 5, 20, 50, 200, 500):
    d.trait(x(v), Y_AXE - 4, x(v), Y_AXE, couleur=TRAIT, epaisseur=1)
d.trait(X0, Y_AXE, X1, Y_AXE, couleur=TRAIT)
d.texte(X1, Y_HAUT - 12, "échelle logarithmique, en dollars américains", 10.5, False, GRIS, "end",
        italique=True)


def point(v, y, etiquette, plein=True):
    d.cercle(x(v), y, 5.5, fond=BLEU if plein else "#ffffff", trait=BLEU)
    d.texte(x(v) + 11, y + 4, etiquette, 11, True, MARINE, "start")


def plage(v1, v2, y, etiquette, mediane=None):
    d.rect(x(v1), y - 7, x(v2) - x(v1), 14, fond=FOND, trait=BLEU, rayon=3)
    if mediane:
        d.trait(x(mediane), y - 7, x(mediane), y + 7, couleur=BLEU, epaisseur=2)
    d.texte(x(v2) + 9, y + 4, etiquette, 11, True, MARINE, "start")


def ligne(y, titre, sous):
    d.texte(30, y + 1, titre, 11.5, False, MARINE, "start")
    d.texte(30, y + 14, sous, 10, False, GRIS, "start", italique=True)
    d.trait(X0, y, X1, y, couleur="#eef0f4", epaisseur=1)


d.surtitre(30, 30, "Marché de 2025")
ligne(52, "Omdia", "logiciel d'entreprise seulement")
point(1.5, 52, "1,5")
ligne(86, "Huit séries de cabinets d'études", "agents IA ou IA agentique")
plage(7.06, 8.03, 86, "7,1 à 8,0")
ligne(120, "Gartner, agents et assistants", "ligne de la prévision de dépenses")
point(16.5, 120, "16,5")
ligne(154, "Gartner, agentique intégrée", "selon un blogue tiers, non vérifié")
point(88.2, 154, "88", plein=False)

d.surtitre(30, 196, "Marché de 2030")
ligne(218, "Treize séries de cabinets d'études", "interpolées par l'ouvrage; trait : médiane")
plage(24.5, 54.6, 218, "25 à 55", mediane=46.0)
ligne(252, "Deloitte", "moyenne de sept rapports de tiers")
plage(35, 45, 252, "35 à 45")
ligne(286, "Omdia", "logiciel d'entreprise seulement")
point(41.8, 286, "41,8")
ligne(320, "Gartner, agents et assistants", "selon un blogue tiers, non vérifié")
point(219.9, 320, "220", plein=False)
ligne(354, "Gartner, agentique intégrée", "selon un blogue tiers, non vérifié")
point(1003.6, 354, "1 004", plein=False)

d.ecrit("fig-50-e1")
