"""Chapitre 11, section 11.1 : carte des instances, par nature et par degré d'avancement."""
from dessin import Dessin, MARINE, BLEU, TRAIT, FOND, NEUTRE, coupe

d = Dessin(hauteur=378)

# Colonnes : degré d'avancement du texte le plus avancé, croissant vers la droite.
LX, LL = 20, 130                       # colonne des étiquettes de ligne
COLS = [(160, 120), (290, 165), (465, 212), (687, 171)]
ENTETES = ["Rien de propre\naux agents", "Aucun texte publié", "Brouillons", "Textes publiés"]
DROITE = COLS[-1][0] + COLS[-1][1]

d.fleche(COLS[0][0], 30, DROITE, 30, "degré d'avancement", decalage=-8, taille=11)
for (cx, cl), t in zip(COLS, ENTETES):
    lignes = coupe(t, cl, 11.5)
    for i, ligne in enumerate(lignes):
        d.texte(cx + cl / 2, 68 - 15 * (len(lignes) - 1 - i), ligne, 11.5, gras=True)

# Lignes : nature de l'instance.
H1, H, G, ECART = 58, 58, 8, 18
Y1 = 82
Y2 = Y1 + 2 * H1 + G + ECART
Y3 = Y2 + H + ECART
LIGNES = [(Y1, 2 * H1 + G, "Fondation et instances ouvertes"),
          (Y2, H, "Organismes formels"),
          (Y3, H, "Puissances publiques")]
for y, h, t in LIGNES:
    n = len(coupe(t, LL - 10, 11.5))
    d.paragraphe(LX, y + h / 2 + 4 - 7.5 * (n - 1), t, LL - 10, taille=11.5, couleur=MARINE,
                 ancre="start", gras=True)
for y in (Y2 - ECART / 2, Y3 - ECART / 2):
    d.trait(LX, y, DROITE, y, couleur="#dfe3ea", epaisseur=1)


def case(col, y, h, titre, corps, principal=False):
    cx, cl = COLS[col]
    if principal:
        d.boite(cx, y, cl, h, titre, corps, fond=FOND, trait=BLEU, taille=13, taille_corps=11)
    else:
        d.boite(cx, y, cl, h, titre, corps, fond=NEUTRE, trait=TRAIT, taille=12.5,
                taille_corps=10.5)


case(2, Y1, H1, "W3C, groupes communautaires", "Protocole, identité, confiance, conformité")
case(2, Y1 + H1 + G, H1, "IETF", "Profils d'OAuth et de WIMSE\nWeb Bot Auth")
case(3, Y1, 2 * H1 + G, "AAIF", "Dix projets, dont MCP et A2A : spécifications publiées et mises "
     "en œuvre", principal=True)
case(0, Y2, H, "ISO/IEC SC 42", None)
case(1, Y2, H, "UIT-T, IEEE", "Sujet à l'étude;\nprojets autorisés")
case(1, Y3, H, "NIST/CAISI", "Consultations; document de réflexion sur l'identité")
case(3, Y3, H, "SAC (Chine)", "Série GB/Z 185-2026\nen sept parties")

d.ecrit("fig-11-e1")
