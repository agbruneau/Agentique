"""Chapitre 10, section 10.1 : la pile du commerce agentique en quatre couches."""
from dessin import Dessin, coupe, BLEU, FOND, NEUTRE, GRIS, TRAIT, MARINE

d = Dessin(hauteur=350)


def bloc(x, y, l, h, texte, taille=12, couleur=MARINE, ancre="middle", gras=False, italique=False,
         largeur=None):
    """Texte centré verticalement dans une zone; centré ou aligné à gauche."""
    lignes = coupe(texte, largeur or l - 16, taille)
    total = len(lignes) * taille * 1.32
    yy = y + (h - total) / 2 + taille * 0.95
    xx = x + l / 2 if ancre == "middle" else x + 14
    for ligne in lignes:
        d.texte(xx, yy, ligne, taille, gras, couleur, ancre, italique)
        yy += taille * 1.32


COUCHES = [   # questions et protocoles : tableau de la section 10.1
    ("Découverte", "Que vend ce marchand, et par quelle interface ?",
     "UCP : catalogue, profil /.well-known/ucp\nACP : flux de produits"),
    ("Autorisation", "Qu'a permis l'utilisateur, et qui est l'agent ?",
     "AP2, Verifiable Intent\nVisa Trusted Agent Protocol"),
    ("Paiement", "Quel justificatif à portée limitée\nl'agent présente-t-il ?",
     "Jetons des réseaux et des prestataires\nde paiement"),
    ("Règlement", "Comment la valeur change-t-elle de mains ?",
     "Rails de cartes existants\nx402; MPP"),
]

X0, XQ, XP, XF = 40, 210, 530, 840      # bords : couche | question | protocoles | fin
Y0, H, ECART = 44, 64, 10

d.texte(X0, 28, "COUCHE", 10.5, True, BLEU, "start")
d.texte(XQ + 14, 28, "QUESTION", 10.5, True, BLEU, "start")
d.texte(XP + 14, 28, "PROTOCOLES", 10.5, True, BLEU, "start")

for i, (couche, question, protocoles) in enumerate(COUCHES):
    y = Y0 + i * (H + ECART)
    d.rect(X0, y, XF - X0, H, "#ffffff", TRAIT)                 # la rangée
    d.boite(X0, y, XQ - X0, H, couche, fond=FOND, trait=BLEU, taille=14)
    bloc(XQ, y, XP - XQ, H, question, 12.5, MARINE, "start", italique=True, largeur=1000)
    d.rect(XP, y + 8, XF - XP - 8, H - 16, NEUTRE, TRAIT, rayon=4)
    bloc(XP, y + 8, XF - XP - 8, H - 16, protocoles, 12, GRIS, "start", largeur=1000)

d.ecrit("fig-10-e1")
