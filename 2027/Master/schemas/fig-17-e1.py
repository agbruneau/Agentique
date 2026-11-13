"""Fig. 17-e1 : le spectre en quatre positions, du workflow à l'agent ouvert (section 17.1)."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, MARINE, TRAIT

d = Dessin(hauteur=290)

X0, L, PAS = 210, 145, 160          # première colonne, largeur d'une colonne, pas entre colonnes
cols = [X0 + i * PAS for i in range(4)]
FIN = cols[-1] + L                  # 835

# ---- les deux pôles
d.fleche(X0, 34, FIN, 34, couleur=TRAIT, double=True)
d.texte(X0, 20, "Workflow : chemins de code prédéfinis", 11, False, GRIS, ancre="start")
d.texte(FIN, 20, "Agent : le modèle dirige son processus", 11, False, GRIS, ancre="end")

# ---- en-têtes des quatre positions
noms = ["Workflow", "Étapes agentiques", "Agent borné", "Agent ouvert"]
for x, nom in zip(cols, noms):
    d.texte(x + L / 2, 70, nom, 13.5, True, MARINE)

# ---- étiquettes des lignes
Y1, H1 = 84, 58
Y2, H2 = 154, 74
d.paragraphe(40, Y1 + H1 / 2 + 4, "Qui décide du chemin", 165, taille=12, couleur=MARINE, ancre="start", gras=True)
d.paragraphe(40, Y2 + H2 / 2 + 4, "Ce que décide le modèle", 165, taille=12, couleur=MARINE, ancre="start", gras=True)

# ---- qui décide du chemin : le concepteur (gris) ou le modèle (bleu)
qui = [("Le concepteur", "entièrement", False),
       ("Le concepteur", "entre les étapes", False),
       ("Le modèle", "dans une région délimitée", True),
       ("Le modèle", None, True)]
for x, (titre, corps, modele) in zip(cols, qui):
    if modele:
        d.boite(x, Y1, L, H1, titre, corps, taille=12.5, taille_corps=11)
    else:
        d.boite(x, Y1, L, H1, titre, corps, fond=NEUTRE, trait=GRIS, taille=12.5, taille_corps=11)

# ---- ce que décide le modèle
quoi = ["Le contenu d'une étape : classer, extraire, rédiger",
        "La conduite d'une étape, outils compris",
        "Outils, ordre et paramètres, dans une liste fermée et sous un plafond",
        "Le plan, les outils, le critère d'arrêt"]
for x, t in zip(cols, quoi):
    d.rect(x, Y2, L, H2, fond="#ffffff", trait=TRAIT)
    lignes = len(__import__("dessin").coupe(t, L - 18, 11.5))
    y = Y2 + (H2 - lignes * 11.5 * 1.32) / 2 + 11.5 * 0.95
    d.paragraphe(x + L / 2, y, t, L - 18, taille=11.5, couleur=MARINE)

# ---- frontière de visibilité, entre la deuxième et la troisième position
xf = cols[1] + L + (PAS - L) / 2
d.trait(xf, 52, xf, Y2 + H2 + 10, couleur=BLEU, tirets=True)
d.texte(xf, Y2 + H2 + 28, "Frontière de visibilité", 11.5, True, BLEU)
d.texte(xf - 10, Y2 + H2 + 48, "le processus ne voit que l'entrée et la sortie", 11, False, GRIS,
        ancre="end", italique=True)
d.texte(xf + 10, Y2 + H2 + 48, "chaque appel d'outil est une activité du processus", 11, False,
        GRIS, ancre="start", italique=True)

d.ecrit("fig-17-e1")
