"""Chapitre 30, section 30.2 : chaîne de délégation et ce qu'elle perd."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, MARINE, TRAIT, OCRE

d = Dessin(hauteur=404)

# Rangée des acteurs
Y, H = 20, 54
d.boite(16, Y, 150, H, "Utilisateur", fond=NEUTRE, trait=GRIS)
d.boite(236, Y, 170, H, "Agent", fond=FOND, trait=BLEU)
d.boite(476, Y, 170, H, "Sous-agent", fond=FOND, trait=BLEU)
d.boite(716, Y, 148, H, "Serveur de ressources", fond=NEUTRE, trait=GRIS, taille=12)
d.fleche(166, Y + H / 2, 236, Y + H / 2, "délègue", decalage=-7)
d.fleche(406, Y + H / 2, 476, Y + H / 2, "mandate", decalage=-7)
d.fleche(646, Y + H / 2, 716, Y + H / 2, "présente", decalage=-7)


def jeton(x, y, l, h, titre, lignes):
    d.rect(x, y, l, h, fond="#ffffff", trait=BLEU)
    d.texte(x + 12, y + 20, titre, 11.5, gras=True, ancre="start")
    yy = y + 40
    for retrait, t, couleur, italique in lignes:
        d.texte(x + 12 + retrait, yy, t, 11, couleur=couleur, ancre="start", italique=italique)
        yy += 17


# Jetons : celui du sous-agent est plus étroit
YJ, HJ = 104, 92
jeton(236, YJ, 170, HJ, "Jeton de l'agent",
      [(0, "sub : utilisateur", MARINE, False), (0, "act : agent", MARINE, False)])
jeton(491, YJ, 140, HJ, "Jeton du sous-agent",
      [(0, "sub : utilisateur", MARINE, False), (0, "act : sous-agent", MARINE, False),
       (14, "act : agent", OCRE, True)])
d.trait(321, Y + H, 321, YJ, couleur=TRAIT)
d.trait(561, Y + H, 561, YJ, couleur=TRAIT)

# Serveur d'autorisation
YS = 266
d.boite(236, YS, 410, 48, "Serveur d'autorisation", fond=NEUTRE, trait=GRIS)
d.fleche(321, YS, 321, YJ + HJ)
d.texte(331, 236, "émet", 10.5, couleur=GRIS, ancre="start")
d.fleche(561, YS, 561, YJ + HJ, couleur=BLEU)
yy = 214
for t, gras in [("échange de jeton", True), ("une seule audience", False),
                ("moins de droits", False), ("expire avant le parent", False)]:
    d.texte(571, yy, t, 10.5, gras=gras, couleur=BLEU, ancre="start")
    yy += 14

# Décision du serveur de ressources
d.rect(716, YJ, 148, HJ, fond="#ffffff", trait=GRIS)
d.texte(790, YJ + 20, "Décide sur", 11.5, gras=True)
d.texte(790, YJ + 40, "sub et acteur courant", 11, couleur=MARINE)
d.paragraphe(790, YJ + 64, "Acteurs antérieurs : informatifs", 120, taille=11, couleur=OCRE,
             italique=True)
d.trait(790, Y + H, 790, YJ, couleur=TRAIT)

# Ce que la chaîne perd
d.surtitre(16, 344, "Ce que la chaîne perd", couleur=OCRE)
d.texte(16, 366, "Rien ne garantit que l'agent avait le droit de déléguer, ni qu'il a réduit "
        "ce qu'il transmettait.", 11.5, couleur=MARINE, ancre="start")
d.texte(16, 384, "L'orchestrateur consigne la chaîne complète, que le jeton ne porte pas de "
        "façon probante.", 11.5, couleur=MARINE, ancre="start")

d.ecrit("fig-30-e1")
