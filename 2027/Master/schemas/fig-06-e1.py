from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, TRAIT, MARINE

d = Dessin(hauteur=330)

# Rangée horizontale : A2A entre agents
d.boite(30, 64, 130, 60, "Client", fond=NEUTRE, trait=GRIS)
d.rect(240, 36, 390, 102, "#ffffff", TRAIT, tirets=True)
d.surtitre(256, 54, "Atelier", GRIS)
d.boite(256, 64, 170, 60, "Agent « gérant d'atelier »", taille=12.5)
d.boite(444, 64, 170, 60, "Agent « mécanicien »", taille=12.5)
d.boite(720, 64, 130, 60, "Agent d'un fournisseur", taille=12.5)

d.fleche(160, 94, 256, 94, "A2A", couleur=BLEU, double=True)
d.texte(208, 114, "plusieurs", 10.5, False, GRIS)
d.texte(208, 127, "tours", 10.5, False, GRIS)
d.fleche(614, 94, 720, 94, "A2A", couleur=BLEU, double=True)
d.texte(667, 114, "commande", 10.5, False, GRIS)
d.texte(667, 127, "d'une pièce", 10.5, False, GRIS)

# Axe vertical : MCP vers les outils du mécanicien
mx = 529
d.trait(mx, 124, mx, 196, GRIS, 1.4)
d.texte(mx + 10, 166, "MCP", 10.5, True, GRIS, "start")
outils = ["Lecteur de diagnostic", "Base de manuels", "Pont élévateur"]
xs = [289, 454, 619]
d.trait(xs[0] + 75, 196, xs[2] + 75, 196, GRIS, 1.4)
for x, nom in zip(xs, outils):
    d.fleche(x + 75, 196, x + 75, 226, couleur=GRIS)
    d.boite(x, 226, 150, 44, nom, fond=NEUTRE, trait=GRIS, taille=12)

d.paragraphe(440, 304, "A2A, horizontal : des agents s'associent sur des tâches. "
             "MCP, vertical : un agent utilise des capacités.", 820, taille=11.5)
d.ecrit("fig-06-e1")
