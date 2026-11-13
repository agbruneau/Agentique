"""Chapitre 40, section 40.1 : la part de l'entrée dans les jetons facturés, puis les trois
multiplicateurs (boucle, topologie, outils), avec les seuls chiffres donnés par le texte."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, TRAIT, MARINE

d = Dessin(hauteur=310)
X0, LARG = 30, 820

# ---- Bandeau du haut : un document, pipeline séquentiel (banc d'essai [3])
d.texte(X0, 30, "Un document, pipeline séquentiel", 12, True, MARINE, "start")
ENTREE, SORTIE = 142340, 3820
y_barre, h_barre = 42, 36
l_entree = LARG * ENTREE / (ENTREE + SORTIE)
d.rect(X0, y_barre, l_entree, h_barre, fond=BLEU, trait=BLEU, rayon=3)
d.rect(X0 + l_entree, y_barre, LARG - l_entree, h_barre, fond=GRIS, trait=GRIS, rayon=2)
d.texte(X0 + 14, y_barre + 23, "Entrée : 142 340 jetons, plus de 97 %", 13, True, "#ffffff", "start")
d.texte(X0 + LARG, y_barre + h_barre + 17, "Sortie : 3 820 jetons", 11.5, False, GRIS, "end")
d.texte(X0, y_barre + h_barre + 17,
        "Instructions système, historique, contenu récupéré, dernier résultat d'outil : "
        "renvoyés à chaque tour", 11.5, False, GRIS, "start")

# ---- Trois panneaux : les multiplicateurs
Y_P, H_P, L_P, E_P = 118, 172, 260, 20


def panneau(i, titre):
    x = X0 + i * (L_P + E_P)
    d.rect(x, Y_P, L_P, H_P, fond=NEUTRE, trait=TRAIT)
    d.texte(x + 16, Y_P + 26, titre, 12.5, True, MARINE, "start")
    return x


def barres(x, lignes, maxi, y0):
    """lignes : (étiquette, valeur, texte de la valeur, principale ?)"""
    x_barre, l_max = x + 108, 80
    for k, (etiquette, valeur, affiche, principale) in enumerate(lignes):
        y = y0 + k * 30
        d.texte(x + 16, y + 13, etiquette, 11.5, False, MARINE, "start")
        l = max(3, l_max * valeur / maxi)
        d.rect(x_barre, y, l, 18, fond=FOND if principale else "#ffffff",
               trait=BLEU if principale else TRAIT, rayon=2)
        d.texte(x_barre + l + 6, y + 13, affiche, 11.5, True, BLEU if principale else GRIS, "start")


x = panneau(0, "Boucle")
barres(x, [("Conversation", 1, "1", False),
           ("Agent", 4, "≈ ×4", True),
           ("Multi-agents", 15, "≈ ×15", True)], 15, Y_P + 44)
d.texte(x + 16, Y_P + H_P - 16, "Mesure interne d'Anthropic, en jetons", 10.5, False, GRIS, "start",
        italique=True)

x = panneau(1, "Topologie")
barres(x, [("Pipeline", 0.187, "0,187 $", False),
           ("Réflexive", 0.430, "0,430 $", True)], 0.430, Y_P + 44)
d.texte(x + 16, Y_P + 126, "Coût par document : ×2,3", 11.5, True, MARINE, "start")
d.texte(x + 16, Y_P + H_P - 16, "Même modèle", 10.5, False, GRIS, "start", italique=True)

x = panneau(2, "Outils")
d.paragraphe(x + 16, Y_P + 57,
             "Définitions d'outils, blocs d'appel\net de résultat : payés en jetons\n"
             "d'entrée, à chaque requête", L_P - 32, taille=11.5, couleur=MARINE, ancre="start")
d.paragraphe(x + 16, Y_P + 126,
             "Dizaines de serveurs MCP :\ncatalogue entier payé à chaque tour", L_P - 32,
             taille=11.5, couleur=GRIS, ancre="start")

d.ecrit("fig-40-e1")
