"""Chapitre 2, section 2.1 : quatre générations d'intégration, l'unité intégrée et la forme
du contrat qui la décrit (tableau « Quatre unités d'intégration »)."""
from dessin import Dessin, MARINE, BLEU, FOND, NEUTRE, GRIS, TRAIT

d = Dessin(hauteur=262)

generations = [
    ("EAI", "Le message", "Formats et canaux convenus"),
    ("SOA", "Le service", "Description de service, politiques"),
    ("API", "La ressource", "Description d'interface HTTP"),
    ("EDA", "L'événement", "Attributs de contexte"),
]

X0, LC, ECART = 186, 156, 18           # colonnes
Y_ENTETE, Y_UNITE, Y_CONTRAT, H = 34, 50, 140, 58

# Libellés des lignes
d.texte(30, Y_UNITE + H / 2 + 4.5, "Unité intégrée", 12.5, True, MARINE, "start")
d.texte(30, Y_CONTRAT + H / 2 + 4.5, "Forme du contrat", 12.5, True, MARINE, "start")

for i, (gen, unite, contrat) in enumerate(generations):
    x = X0 + i * (LC + ECART)
    cx = x + LC / 2
    d.texte(cx, Y_ENTETE, gen, 14, True, BLEU)
    d.boite(x, Y_UNITE, LC, H, unite, fond=FOND, trait=BLEU, taille=13.5)
    d.fleche(cx, Y_UNITE + H, cx, Y_CONTRAT, couleur=TRAIT)
    d.rect(x, Y_CONTRAT, LC, H, NEUTRE, TRAIT)
    lignes = 2 if len(contrat) > 24 else 1
    d.paragraphe(cx, Y_CONTRAT + H / 2 + 4.5 - (lignes - 1) * 7.9, contrat, LC - 18, 12, MARINE)

d.trait(30, 222, 850, 222, TRAIT, 0.8)
d.texte(440, 244, "Des générations qui se chevauchent : un centre de gravité, pas une succession stricte",
        11.5, False, GRIS, italique=True)

d.ecrit("fig-02-e1")
