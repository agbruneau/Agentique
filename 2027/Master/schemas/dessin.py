"""Bibliothèque de dessin des schémas des exposés : un seul style pour tous.

Un schéma est un petit script Python placé dans Master/schemas/ :

    from dessin import Dessin, MARINE, BLEU, FOND, GRIS, VERT, OCRE, ROUGE
    d = Dessin(hauteur=300)            # largeur fixe : 880
    d.boite(40, 40, 200, 70, "Hôte", "Crée les clients, applique les politiques")
    d.fleche(240, 75, 320, 75, "JSON-RPC")
    d.ecrit("fig-05-e1")               # -> Master/manuscrit/figures/fig-05-e1.svg
                                       #    et un aperçu PNG dans Master/build/apercu/

Règles de style : fond blanc, texte marine, accents bleus, remplissages très clairs,
police sans empattement, traits fins. Peu de couleurs, peu de texte, pas d'ombre.
"""
import html
import os

ICI = os.path.dirname(os.path.abspath(__file__))
FIGURES = os.path.join(os.path.dirname(ICI), "manuscrit", "figures")
APERCU = os.path.join(os.path.dirname(ICI), "build", "apercu")

LARGEUR = 880
MARINE = "#14233f"
BLEU = "#2f5fd0"
GRIS = "#5f6b7a"
TRAIT = "#9aa5b4"
FOND = "#eef2fb"        # remplissage bleu très clair
NEUTRE = "#f5f6f8"      # remplissage gris très clair
VERT = "#2c6b58"
FOND_VERT = "#e9f3ef"
OCRE = "#8a5a12"
FOND_OCRE = "#f8f1e4"
ROUGE = "#9c2f2f"
FOND_ROUGE = "#f9eaea"
POLICE = "Segoe UI, Calibri, sans-serif"


def coupe(texte, largeur, taille):
    """Découpe un texte en lignes qui tiennent dans une largeur donnée (en pixels)."""
    maxi = max(6, int(largeur / (taille * 0.54)))
    lignes = []
    for bloc in str(texte).split("\n"):
        ligne = ""
        for mot in bloc.split():
            if ligne and len(ligne) + 1 + len(mot) > maxi:
                lignes.append(ligne)
                ligne = mot
            else:
                ligne = (ligne + " " + mot).strip()
        lignes.append(ligne)
    return lignes


class Dessin:
    def __init__(self, hauteur, largeur=LARGEUR):
        self.l, self.h, self.e = largeur, hauteur, []

    # ---- primitives
    def rect(self, x, y, l, h, fond="#ffffff", trait=TRAIT, rayon=6, epaisseur=1.2, tirets=False):
        self.e.append('<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" stroke="%s" '
                      'stroke-width="%g"%s/>' % (x, y, l, h, rayon, fond, trait, epaisseur,
                                                ' stroke-dasharray="5 4"' if tirets else ""))

    def cercle(self, x, y, r, fond=FOND, trait=BLEU, epaisseur=1.4):
        self.e.append('<circle cx="%g" cy="%g" r="%g" fill="%s" stroke="%s" stroke-width="%g"/>'
                      % (x, y, r, fond, trait, epaisseur))

    def trait(self, x1, y1, x2, y2, couleur=TRAIT, epaisseur=1.3, tirets=False):
        self.e.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="%g"%s/>'
                      % (x1, y1, x2, y2, couleur, epaisseur,
                         ' stroke-dasharray="5 4"' if tirets else ""))

    def texte(self, x, y, t, taille=13, gras=False, couleur=MARINE, ancre="middle", italique=False):
        """Une ligne de texte; ancre = start | middle | end; y est la ligne de base."""
        self.e.append('<text x="%g" y="%g" text-anchor="%s" font-family="%s" font-size="%g"%s%s '
                      'fill="%s">%s</text>' % (x, y, ancre, POLICE, taille,
                                              ' font-weight="bold"' if gras else "",
                                              ' font-style="italic"' if italique else "",
                                              couleur, html.escape(str(t))))

    def paragraphe(self, x, y, t, largeur, taille=11.5, couleur=GRIS, ancre="middle", gras=False,
                   italique=False):
        """Texte sur plusieurs lignes; renvoie l'ordonnée de la ligne suivante."""
        for ligne in coupe(t, largeur, taille):
            self.texte(x, y, ligne, taille, gras, couleur, ancre, italique)
            y += taille * 1.32
        return y

    # ---- éléments composés
    def boite(self, x, y, l, h, titre, corps=None, fond=FOND, trait=BLEU, taille=13,
              taille_corps=11, couleur=MARINE):
        """Rectangle avec un titre en gras et, au besoin, un texte plus petit dessous.
        Le tout est centré; vérifier à l'aperçu que le texte tient dans la hauteur."""
        self.rect(x, y, l, h, fond, trait)
        lignes_titre = coupe(titre, l - 16, taille)
        lignes_corps = coupe(corps, l - 16, taille_corps) if corps else []
        total = len(lignes_titre) * taille * 1.25 + len(lignes_corps) * taille_corps * 1.32 \
            + (4 if lignes_corps else 0)
        cy = y + (h - total) / 2 + taille * 0.95
        for ligne in lignes_titre:
            self.texte(x + l / 2, cy, ligne, taille, True, couleur)
            cy += taille * 1.25
        cy += 4 - taille * 0.95 + taille_corps * 0.95 if lignes_corps else 0
        for ligne in lignes_corps:
            self.texte(x + l / 2, cy, ligne, taille_corps, False, GRIS)
            cy += taille_corps * 1.32

    def fleche(self, x1, y1, x2, y2, etiquette=None, couleur=GRIS, tirets=False, double=False,
               decalage=-6, taille=10.5):
        """Flèche de (x1, y1) vers (x2, y2); étiquette posée au milieu, décalée de `decalage`."""
        self.e.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="1.4"%s/>'
                      % (x1, y1, x2, y2, couleur, ' stroke-dasharray="5 4"' if tirets else ""))
        longueur = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 or 1
        ux, uy = (x2 - x1) / longueur, (y2 - y1) / longueur
        for (px, py, sx, sy) in [(x2, y2, ux, uy)] + ([(x1, y1, -ux, -uy)] if double else []):
            bx, by = px - 9 * sx, py - 9 * sy
            self.e.append('<polygon points="%g,%g %g,%g %g,%g" fill="%s"/>'
                          % (px, py, bx - 4 * sy, by + 4 * sx, bx + 4 * sy, by - 4 * sx, couleur))
        if etiquette:
            self.texte((x1 + x2) / 2, (y1 + y2) / 2 + decalage, etiquette, taille, False, couleur)

    def surtitre(self, x, y, t, couleur=BLEU, ancre="start"):
        """Petite étiquette en capitales, pour nommer un panneau ou une colonne."""
        self.e.append('<text x="%g" y="%g" text-anchor="%s" font-family="%s" font-size="10" '
                      'font-weight="bold" letter-spacing="1.2" fill="%s">%s</text>'
                      % (x, y, ancre, POLICE, couleur, html.escape(str(t).upper())))

    # ---- sortie
    def svg(self):
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">\n'
                '<rect width="%d" height="%d" fill="#ffffff"/>\n'
                % (self.l, self.h, self.l, self.h, self.l, self.h)
                + "\n".join(self.e) + "\n</svg>\n")

    def ecrit(self, nom):
        """Écrit figures/<nom>.svg et un aperçu PNG dans build/apercu/<nom>.png."""
        os.makedirs(FIGURES, exist_ok=True)
        os.makedirs(APERCU, exist_ok=True)
        chemin = os.path.join(FIGURES, nom + ".svg")
        with open(chemin, "w", encoding="utf-8", newline="\n") as f:
            f.write(self.svg())
        try:
            import pymupdf
            page = pymupdf.open(chemin)[0]
            page.get_pixmap(dpi=110).save(os.path.join(APERCU, nom + ".png"))
            print("écrit :", chemin, "| aperçu :", os.path.join(APERCU, nom + ".png"))
        except Exception as erreur:      # l'aperçu est un confort, pas une condition
            print("écrit :", chemin, "| aperçu impossible :", erreur)
