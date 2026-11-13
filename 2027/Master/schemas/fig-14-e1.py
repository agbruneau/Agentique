"""Chapitre 14, section 14.1 : les quatre types de mémoire (CoALA) et le risque propre à l'écriture."""
from dessin import (Dessin, BLEU, FOND, NEUTRE, GRIS, TRAIT, MARINE, VERT, FOND_VERT, ROUGE,
                    FOND_ROUGE)

d = Dessin(hauteur=314)

# type, contenu selon CoALA, risque propre à l'écriture (tableau de la section 14.1)
TYPES = [
    ("De travail", "L'information active du cycle de décision en cours",
     "Faible :\nelle disparaît avec la session", "faible"),
    ("Épisodique", "L'expérience des cycles antérieurs : historiques, trajectoires",
     "Un épisode faux sert\nensuite de précédent", "moyen"),
    ("Sémantique", "Le savoir de l'agent sur le monde et sur lui-même",
     "Un fait périmé ou injecté\npasse pour établi", "moyen"),
    ("Procédurale", "Le savoir-faire : poids du modèle et code de l'agent",
     "Le plus élevé :\nelle modifie le comportement", "eleve"),
]

L, ECART_LT, ECART_TRAVAIL = 182, 17, 41
XS = [40]
for i in range(3):
    XS.append(XS[-1] + L + (ECART_TRAVAIL if i == 0 else ECART_LT))
FIN = XS[-1] + L                                    # 840

# ---- une mémoire de travail, trois mémoires à long terme; apprendre, c'est écrire dans ces trois
d.texte((XS[1] + FIN) / 2, 30, "Mémoires à long terme : apprendre, c'est y écrire", 12, True, BLEU)
d.trait(XS[1], 40, FIN, 40, BLEU, 1.2)
d.trait(XS[1], 40, XS[1], 47, BLEU, 1.2)
d.trait(FIN, 40, FIN, 47, BLEU, 1.2)

# ---- ce que chaque mémoire contient
for x, (nom, contenu, _, _) in zip(XS, TYPES):
    d.boite(x, 56, L, 112, nom, contenu, taille=14, taille_corps=11.5)

# ---- le risque propre à l'écriture
d.texte(40, 197, "RISQUE PROPRE À L'ÉCRITURE", 10.5, True, GRIS, "start")
d.trait(222, 193, FIN, 193, "#dfe3ea")
STYLE = {"faible": (FOND_VERT, VERT, VERT), "moyen": (NEUTRE, TRAIT, MARINE),
         "eleve": (FOND_ROUGE, ROUGE, ROUGE)}
for x, (_, _, risque, niveau) in zip(XS, TYPES):
    fond, trait, couleur = STYLE[niveau]
    d.rect(x, 212, L, 76, fond, trait)
    d.paragraphe(x + L / 2, 212 + 33, risque, 1000, 12, couleur)   # coupures faites à la main

d.ecrit("fig-14-e1")
