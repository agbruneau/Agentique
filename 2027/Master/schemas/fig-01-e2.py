"""Chapitre 1, section 1.2 : les cinq termes de la taxonomie et qui décide du chemin."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, TRAIT, MARINE

d = Dessin(hauteur=300)

termes = [
    ("LLM augmenté", "un modèle doté de récupération, d'outils et de mémoire", "Le modèle,\nsur un appel"),
    ("Workflow agentique", "des chemins de code prédéfinis", "Le concepteur"),
    ("Agent", "le modèle dirige son déroulement et son usage des outils", "Le modèle"),
    ("Système multi-agents", "plusieurs agents, chacun avec sa spécialité", "Les modèles, dans une topologie donnée"),
    ("Système d'IA composé", "plusieurs composants en interaction", "Variable"),
]

X0, L, G = 26, 152, 18
xs = [X0 + i * (L + G) for i in range(5)]
droite = xs[-1] + L

# progression
d.fleche(X0, 36, droite, 36)
d.texte(X0, 24, "du plus simple", 11, couleur=GRIS, ancre="start", italique=True)
d.texte(droite, 24, "au plus englobant", 11, couleur=GRIS, ancre="end", italique=True)

# termes
for x, (terme, definition, _) in zip(xs, termes):
    d.boite(x, 52, L, 96, terme, definition, fond=NEUTRE, trait=GRIS, taille=12.5, taille_corps=11)

# qui décide du chemin
d.surtitre(440, 176, "Qui décide du chemin", ancre="middle")
for x, (_, _, qui) in zip(xs, termes):
    d.boite(x, 192, L, 54, qui, fond=FOND, trait=BLEU, taille=12)

# relation d'inclusion
xa, xb = xs[1], xs[3] + L
d.trait(xa, 258, xa, 266); d.trait(xb, 258, xb, 266); d.trait(xa, 266, xb, 266)
d.texte((xa + xb) / 2, 286, "tous sont aussi des systèmes d'IA composés", 11, couleur=GRIS,
        italique=True)

d.ecrit("fig-01-e2")
