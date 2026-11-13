"""Chapitre 31, section 31.4 : trajet d'une injection indirecte jusqu'au détournement d'objectif."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, TRAIT, ROUGE, FOND_ROUGE

d = Dessin(hauteur=334)

# Voie légitime (haut) et voie de l'injection (bas)
YH, YB, H = 20, 128, 64
d.boite(16, YH, 140, H, "Utilisateur", "la victime, non l'auteur", fond=NEUTRE, trait=GRIS)
d.boite(16, YB, 140, H, "Tiers", "auteur de la consigne", fond=FOND_ROUGE, trait=ROUGE,
        couleur=ROUGE)
XC, LC = 226, 200
d.boite(XC, YB, LC, H, "Contenu lu par l'agent",
        "page, courriel, billet, ligne de base de données, réponse d'API", fond=FOND_ROUGE,
        trait=ROUGE, couleur=ROUGE, taille=12, taille_corps=10.5)
d.fleche(156, YB + H / 2, XC, YB + H / 2, couleur=ROUGE)
d.paragraphe(191, YB + H / 2 - 22, "dépose une\nconsigne", 70, taille=10.5, couleur=ROUGE)

# Agent
XA, LA = 486, 120
d.boite(XA, YH, LA, YB + H - YH, "Agent", fond=FOND, trait=BLEU)
d.fleche(156, YH + H / 2, XA, YH + H / 2, "tâche légitime", couleur=GRIS)
d.fleche(XC + LC, YB + H / 2, XA, YB + H / 2, couleur=ROUGE)
d.paragraphe((XC + LC + XA) / 2, YB + H / 2 - 22, "résultat\nd'outil", 60, taille=10.5,
             couleur=ROUGE)

# Détournement
XD, LD, HD = 656, 208, 104
YM = (YH + YB + H) / 2
d.boite(XD, YM - HD / 2, LD, HD, "Détournement d'objectif (ASI01)",
        "un but qui n'est plus celui du mandant, poursuivi avec des moyens légitimes",
        fond=FOND_ROUGE, trait=ROUGE, couleur=ROUGE, taille=12, taille_corps=10.5)
d.fleche(XA + LA, YM, XD, YM, couleur=ROUGE)

# Ce que l'attaquant en tire, selon les capacités de l'agent
YR, YE, HE, LE, PE = 240, 262, 56, 158, 172.5
effets = [
    ("Exfiltration", "données privées et\ncanal sortant"),
    ("Action non voulue", "outils à effet\n(ASI02)"),
    ("Exécution de code", "interpréteur\n(ASI05, MCP05)"),
    ("Persistance", "écriture en mémoire\n(ASI06)"),
    ("Approbation", "obtenue par tromperie\n(ASI09)"),
]
d.trait(XD + LD / 2, YM + HD / 2, XD + LD / 2, YR, couleur=TRAIT)
d.trait(16 + LE / 2, YR, 16 + 4 * PE + LE / 2, YR, couleur=TRAIT)
for i, (titre, condition) in enumerate(effets):
    x = 16 + i * PE
    d.fleche(x + LE / 2, YR, x + LE / 2, YE, couleur=TRAIT)
    d.boite(x, YE, LE, HE, titre, condition, fond="#ffffff", trait=GRIS, taille=12,
            taille_corps=10.5)
d.texte(16, YR - 9, "Selon les capacités de l'agent", 10.5, couleur=GRIS, ancre="start")

d.ecrit("fig-31-e1")
