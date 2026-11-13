"""Chapitre 48, section 48.1 : du repérage au corpus retenu, puis notices rendues et retenues
par requête. Les nombres sont ceux du tableau de la section."""
from dessin import Dessin, BLEU, FOND, NEUTRE, GRIS, TRAIT, MARINE

d = Dessin(hauteur=336)

# ---- Panneau de gauche : l'entonnoir
d.surtitre(30, 26, "Du repérage au corpus")
ETAPES = [("124", "notices rendues par dix requêtes", 250),
          ("123", "notices distinctes", 244),
          ("83", "retenues, lues par leur résumé", 236),
          ("82", "confirmées par arXiv ou par un DOI", 228)]
y = 42
for k, (nombre, texte, largeur) in enumerate(ETAPES):
    x = 30 + (250 - largeur) / 2
    d.rect(x, y, largeur, 52, fond=FOND if k < 3 else BLEU, trait=BLEU)
    clair = k == 3
    d.texte(30 + 125, y + 23, nombre, 17, True, "#ffffff" if clair else MARINE)
    d.texte(30 + 125, y + 41, texte, 10.5, False, "#ffffff" if clair else GRIS)
    if k < 3:
        d.fleche(30 + 125, y + 54, 30 + 125, y + 70)
    y += 72

# ---- Panneau de droite : par requête
X0, XB, LMAX = 330, 520, 250
d.surtitre(X0, 26, "Notices par requête")
d.rect(XB + 96, 15, 22, 10, fond="#ffffff", trait=TRAIT, rayon=2)
d.texte(XB + 124, 24, "rendues", 10.5, False, GRIS, "start")
d.rect(XB + 180, 15, 22, 10, fond=BLEU, trait=BLEU, rayon=2)
d.texte(XB + 208, 24, "retenues", 10.5, False, GRIS, "start")
LIGNES = [("Protocoles", 20, 16), ("Coordination", 14, 9), ("Évaluation", 15, 9),
          ("Sécurité", 12, 10), ("Productivité", 12, 7), ("Mémoire", 10, 7),
          ("Gouvernance", 12, 7), ("Mono-agent ou multi-agents", 9, 9),
          ("Adoption", 10, 4), ("Sémantique", 10, 5)]
for k, (theme, rendues, retenues) in enumerate(LIGNES):
    y = 44 + k * 28
    d.texte(X0, y + 14, theme, 11.5, False, MARINE, "start")
    d.rect(XB, y + 2, LMAX * rendues / 20, 16, fond="#ffffff", trait=TRAIT, rayon=2)
    d.rect(XB, y + 2, LMAX * retenues / 20, 16, fond=BLEU, trait=BLEU, rayon=2)
    d.texte(XB + LMAX * rendues / 20 + 8, y + 14, "%d sur %d" % (retenues, rendues), 11, True,
            MARINE, "start")

d.ecrit("fig-48-e1")
