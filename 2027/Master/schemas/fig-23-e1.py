"""Chapitre 23, section 23.1 : vue en couches à l'échelle de l'entreprise (synthèse du chapitre),
avec le plan de contrôle transversal. Fonction du plan de contrôle reprise du tableau de 23.2."""
from dessin import Dessin, MARINE, BLEU, FOND, NEUTRE, GRIS, TRAIT

d = Dessin(hauteur=316)

couches = [
    ("Interaction", "Canaux, interfaces, points d'approbation humaine"),
    ("Agents et orchestration", "Raisonnement, plans, coordination, exécution durable"),
    ("Contexte et connaissance", "Mémoire, couche sémantique, données"),
    ("Accès", "Outils, API, systèmes patrimoniaux, autres agents"),
    ("Modèles", "Modèles de langage, routage, choix du fournisseur et repli"),
]

X, L, H, ECART, Y0 = 30, 600, 48, 10, 18
XP, LP = 660, 190                      # plan de contrôle
for i, (nom, role) in enumerate(couches):
    y = Y0 + i * (H + ECART)
    d.rect(X, y, L, H, NEUTRE, TRAIT)
    d.texte(X + 18, y + H / 2 + 4.5, nom, 13, True, MARINE, "start")
    d.texte(X + 222, y + H / 2 + 4, role, 11.5, False, GRIS, "start")
    d.trait(X + L, y + H / 2, XP, y + H / 2, BLEU, 1.3, tirets=True)

HP = 5 * H + 4 * ECART
d.rect(XP, Y0, LP, HP, FOND, BLEU)
cx = XP + LP / 2
d.texte(cx, Y0 + 42, "Plan de contrôle", 13.5, True, MARINE)
d.texte(cx, Y0 + 60, "transversal", 11.5, False, BLEU, italique=True)
d.trait(XP + 24, Y0 + 78, XP + LP - 24, Y0 + 78, BLEU, 0.8)
y = Y0 + 106
for composant in ["Registre", "Identité", "Politique", "Observabilité", "Budgets"]:
    d.texte(cx, y, composant, 12, False, MARINE)
    y += 24
d.trait(XP + 24, y - 4, XP + LP - 24, y - 4, BLEU, 0.8)
d.texte(cx, y + 22, "Décider, configurer, observer", 11, False, GRIS, italique=True)

d.ecrit("fig-23-e1")
