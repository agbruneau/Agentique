"""Chapitre 3, section 3.1 : les cinq niveaux d'interopérabilité, leur question et ce que
fournissent les protocoles en 2026."""
from dessin import (Dessin, BLEU, FOND, NEUTRE, GRIS, VERT, FOND_VERT, OCRE, FOND_OCRE,
                    ROUGE, FOND_ROUGE)

# du haut vers le bas : le niveau juridique en haut de la pile, le technique en bas
niveaux = [
    ("Juridique et de confiance", "Ont-elles le droit d'agir, et peut-on le prouver ?",
     "Des mécanismes d'authentification; aucune expression des obligations", "rouge"),
    ("Organisationnel", "Qui fait quoi, qui décide, qui répond ?",
     "Des états de tâche; presque rien d'autre", "rouge"),
    ("Sémantique", "Comprennent-elles la même chose ?",
     "Des descriptions en langage naturel; l'interprétation revient au modèle", "ocre"),
    ("Syntaxique", "Peuvent-elles lire le message ?", "Standardisé", "vert"),
    ("Technique", "Les parties peuvent-elles se joindre ?", "Standardisé", "vert"),
]
teintes = {"vert": (FOND_VERT, VERT), "ocre": (FOND_OCRE, OCRE), "rouge": (FOND_ROUGE, ROUGE)}

H, G, Y0 = 52, 8, 44
d = Dessin(hauteur=Y0 + 5 * H + 4 * G + 24)

XN, LN = 24, 206          # niveau
XQ, LQ = 242, 290         # question
XP, LP = 544, 312         # protocoles

d.surtitre(XN, 30, "Niveau")
d.surtitre(XQ, 30, "Question")
d.surtitre(XP, 30, "Ce que fournissent les protocoles en 2026")

for i, (niveau, question, protocoles, teinte) in enumerate(niveaux):
    y = Y0 + i * (H + G)
    d.boite(XN, y, LN, H, niveau, fond=FOND, trait=BLEU, taille=12.5)
    d.rect(XQ, y, LQ, H, fond=NEUTRE, trait=NEUTRE)
    d.texte(XQ + 14, y + H / 2 + 4, question, 11.5, couleur=GRIS, ancre="start")
    fond, trait = teintes[teinte]
    d.boite(XP, y, LP, H, protocoles, fond=fond, trait=trait, taille=11.5, couleur=trait)

d.ecrit("fig-03-e1")
