from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, MARINE

d = Dessin(hauteur=340)

# L'hôte et ses clients
d.rect(30, 30, 430, 270, FOND, BLEU)
d.surtitre(50, 56, "Hôte")
y = 124
for ligne in ["Crée les clients", "Applique les politiques", "Garde l'historique complet",
              "Contrôle toute interaction", "entre serveurs"]:
    d.texte(50, y, ligne, 12, False, MARINE, "start")
    y += 22

serveurs = [("Fichiers d'un dépôt", 59), ("Base de données", 137), ("API externe", 215)]
for i, (nom, y) in enumerate(serveurs):
    d.boite(260, y, 170, 56, "Client %d" % (i + 1), fond="#ffffff", trait=BLEU)
    d.fleche(430, y + 28, 600, y + 28, "JSON-RPC" if i == 0 else None, double=True)
    d.boite(600, y, 250, 56, nom, "outils · ressources · prompts", fond=NEUTRE, trait=GRIS)

d.surtitre(600, 48, "Serveurs", GRIS)
# Isolation entre serveurs
for y in (115, 193):
    d.texte(725, y + 15, "aucun lien direct", 10.5, False, GRIS, italique=True)

d.paragraphe(440, 328, "Un client par serveur. Un serveur ne voit ni la conversation entière "
             "ni les autres serveurs.", 820, taille=11.5)
d.ecrit("fig-05-e1")
