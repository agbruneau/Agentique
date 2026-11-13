"""Chapitre 24, section 24.2 : les cinq contrôles d'une passerelle sur un appel d'outil."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, MARINE, TRAIT

d = Dessin(hauteur=262)

# Cadre de la passerelle
d.rect(114, 14, 652, 200, fond="#ffffff", trait=BLEU, rayon=8, tirets=True)
d.surtitre(126, 34, "Passerelle")

HAUT, H = 46, 92            # rangée des contrôles
Y_APPEL = HAUT + H / 2       # voie de l'appel
Y_RETOUR = 176               # voie de la réponse

# Agent et outil, assez hauts pour recevoir les deux voies
d.boite(16, HAUT, 80, 152, "Agent", fond=FOND, trait=BLEU)
d.boite(784, HAUT, 80, 152, "Outil", fond=NEUTRE, trait=GRIS)

controles = [
    ("Identité", "Jeton émis pour ce destinataire"),
    ("Autorisation par outil", "Outil permis à cet appelant"),
    ("Approbation", "Accord humain exigé ou non"),
    ("Quota et budget", "Débit ou enveloppe de l'appelant"),
]
L, PAS = 108, 130
for i, (titre, question) in enumerate(controles):
    x = 126 + i * PAS
    d.boite(x, HAUT, L, H, titre, question, fond=FOND, trait=BLEU, taille=12, taille_corps=10.5)

# Inspection : couvre l'appel et la réponse
xi = 126 + 4 * PAS
d.boite(xi, HAUT, L, 152, "Inspection des contenus",
        "Arguments, réponse et définition de l'outil", fond=FOND, trait=BLEU, taille=12,
        taille_corps=10.5)

# Voie de l'appel
d.fleche(96, Y_APPEL, 126, Y_APPEL, couleur=MARINE)
for i in range(4):
    x = 126 + i * PAS + L
    d.fleche(x, Y_APPEL, x + 22, Y_APPEL, couleur=MARINE)
d.fleche(xi + L, Y_APPEL, 784, Y_APPEL, couleur=MARINE)

# Voie de la réponse
d.fleche(784, Y_RETOUR, xi + L, Y_RETOUR, couleur=GRIS)
d.fleche(xi, Y_RETOUR, 96, Y_RETOUR, couleur=GRIS)
d.texte((96 + xi) / 2, Y_RETOUR - 8, "Réponse balayée avant son retour à l'agent", 11, couleur=GRIS)

# Deux propriétés transversales
d.texte(440, 244, "Toute erreur vaut refus  ·  Chaque décision laisse une trace d'audit", 11.5,
        gras=True, couleur=MARINE)

d.ecrit("fig-24-e1")
