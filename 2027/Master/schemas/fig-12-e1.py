"""Chapitre 12, introduction et section 12.1 : message conforme au schéma, sens divergent."""
from dessin import (Dessin, BLEU, FOND, NEUTRE, GRIS, TRAIT, MARINE, VERT, ROUGE, FOND_ROUGE)

d = Dessin(hauteur=380)

GX, GL = 40, 220            # agent des ventes
DX, DL = 620, 220           # agent des finances
MILIEU = 440

# ---- l'échange : la syntaxe est respectée (introduction du chapitre, section 12.1)
d.boite(GX, 36, GL, 76, "Agent des ventes")
d.boite(DX, 36, DL, 76, "Agent des finances")
d.fleche(GX + GL, 58, DX, 58, "demande le « revenu du trimestre »", couleur=MARINE, decalage=-9,
         taille=12)
d.fleche(DX, 90, GX + GL, 90, "réponse : revenue, nombre décimal", decalage=19, taille=12)
d.texte(MILIEU, 132, "schéma respecté", 11.5, True, VERT)

# ---- ce que chacun entend par le même terme
for x, l, sens in [(GX, GL, ["commandes signées"]),
                   (DX, DL, ["montants reconnus", "en comptabilité"])]:
    d.trait(x + l / 2, 112, x + l / 2, 158, TRAIT, tirets=True)
    d.rect(x, 158, l, 70, "#ffffff", TRAIT, tirets=True)
    y = 158 + (70 - 16 - 16.5 * len(sens)) / 2 + 11      # bloc centré : « entend : » + sens
    d.texte(x + l / 2, y, "entend :", 11, False, GRIS, italique=True)
    for i, ligne in enumerate(sens):
        d.texte(x + l / 2, y + 19 + 16.5 * i, ligne, 12.5)

d.texte(MILIEU, 190, "≠", 26, True, ROUGE)
d.texte(MILIEU, 214, "même terme, deux sens", 12, True, ROUGE)

# ---- syntaxe contre sens (section 12.1)
d.trait(40, 252, 840, 252, "#dfe3ea")
d.boite(40, 272, 390, 74, "Erreur de syntaxe", "Produit un rejet", fond=NEUTRE, trait=GRIS,
        taille_corps=12)
d.boite(450, 272, 390, 74, "Erreur de sens : silencieuse",
        "Produit une réponse bien formée,\nque l'agent suivant reprend comme un fait",
        fond=FOND_ROUGE, trait=ROUGE, couleur=ROUGE, taille_corps=12)

d.ecrit("fig-12-e1")
