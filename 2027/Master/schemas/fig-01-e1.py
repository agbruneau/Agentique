"""Chapitre 1, section 1.1 : l'échange en un tour de l'assistant, en regard de la boucle de l'agent."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, TRAIT, MARINE

d = Dessin(hauteur=340)

# ---- Assistant : par tours
d.surtitre(40, 30, "Assistant : par tours")
d.boite(40, 52, 190, 50, "Demande", fond=NEUTRE, trait=GRIS)
d.fleche(135, 102, 135, 138)
d.boite(40, 138, 190, 60, "Assistant", fond=NEUTRE, trait=GRIS)
d.fleche(135, 198, 135, 234)
d.boite(40, 234, 190, 50, "Réponse", fond=NEUTRE, trait=GRIS)
d.texte(135, 316, "un tour, puis fin", 11, couleur=GRIS, italique=True)

# séparation
d.trait(280, 20, 280, 320, couleur=TRAIT, tirets=True)

# ---- Agent : en boucle
d.surtitre(330, 30, "Agent : en boucle")

# point de contrôle humain
d.boite(330, 52, 200, 52, "Point de contrôle", "consulter un humain", fond=NEUTRE, trait=GRIS,
        taille=12.5, taille_corps=11)
d.fleche(430, 104, 430, 138, tirets=True, double=True)

# modèle et outil
d.boite(330, 138, 200, 80, "Modèle", "évalue son avancement et choisit la suite")
d.boite(670, 138, 180, 80, "Outil", "agit sur un autre système", fond=NEUTRE, trait=GRIS)
d.fleche(530, 160, 670, 160, "utilise l'outil")
d.fleche(670, 196, 530, 196, "résultat renvoyé", decalage=17)
d.texte(600, 227, "par l'environnement", 10.5, couleur=GRIS)

# condition d'arrêt
d.fleche(430, 218, 430, 252)
d.boite(330, 252, 200, 66, "Condition d'arrêt", "p. ex. nombre maximal d'itérations",
        fond=NEUTRE, trait=GRIS, taille=12.5, taille_corps=11)

d.ecrit("fig-01-e1")
