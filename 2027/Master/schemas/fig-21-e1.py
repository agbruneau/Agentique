"""Chapitre 21, section 21.1 : les quatorze modes d'échec de MAST en trois catégories.

Parts par mode : version 3 (tableau de la section 21.1). Totaux v3 : sommes calculées dans le
chapitre (l'article ne les publie pas). Totaux v2 : publiés par la version 2.
"""
from dessin import Dessin, BLEU, FOND, GRIS, MARINE

CATEGORIES = [
    ("Défauts de spécification", "v3 : 44,2 %  ·  v2 : 41,77 %", [
        ("Consigne de tâche non respectée", 11.8),
        ("Rôle non respecté", 1.5),
        ("Répétition d'étapes", 15.7),
        ("Perte de l'historique de conversation", 2.8),
        ("Condition d'arrêt ignorée", 12.4),
    ]),
    ("Désalignement entre agents", "v3 : 32,4 %  ·  v2 : 36,94 %", [
        ("Réinitialisation de la conversation", 2.2),
        ("Clarification non demandée", 6.8),
        ("Dérive hors de la tâche", 7.4),
        ("Rétention d'information", 0.85),
        ("Apport d'un autre agent ignoré", 1.9),
        ("Écart entre raisonnement et action", 13.2),
    ]),
    ("Vérification de la tâche", "v3 : 23,5 %  ·  v2 : 21,30 %", [
        ("Arrêt prématuré", 6.2),
        ("Vérification absente ou incomplète", 8.2),
        ("Vérification incorrecte", 9.1),
    ]),
]

def pct(v):
    return ("%g" % v).replace(".", ",") + " %"

LC, ECART, X0 = 252, 22, 40
Y_TETE, H_TETE = 20, 62
Y_LIGNES, PAS = 110, 36
ECHELLE = 175 / 16.0                    # pixels par point de pourcentage

d = Dessin(hauteur=Y_LIGNES + 6 * PAS - 8)
for i, (nom, part, modes) in enumerate(CATEGORIES):
    x = X0 + i * (LC + ECART)
    d.rect(x, Y_TETE, LC, H_TETE, FOND, BLEU)
    d.texte(x + LC / 2, Y_TETE + 26, nom, 13, True)
    d.texte(x + LC / 2, Y_TETE + 47, part, 11.5, False, GRIS)
    y = Y_LIGNES
    for libelle, v in modes:
        d.texte(x + 4, y, libelle, 11, False, MARINE, ancre="start")
        largeur = v * ECHELLE
        d.rect(x + 4, y + 6, largeur, 7, BLEU, BLEU, rayon=1, epaisseur=0.5)
        d.texte(x + 4 + largeur + 6, y + 13.5, pct(v), 10.5, False, GRIS, ancre="start")
        y += PAS

d.ecrit("fig-21-e1")
