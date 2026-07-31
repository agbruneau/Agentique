#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Primitives de dessin des figures du compendium.

Huit dispositions couvrent les quatre-vingt-dix « types » listes par
`programme.md` : bandes, pile, frise, chaine, matrice, paire, arbre, venn.
Elles ne sont pas un moteur graphique — elles fixent les CONVENTIONS du volume
pour que cent quinze figures se ressemblent, ce qu'un dessin a la main ne
garantit pas.

⚠ CONVENTION DE DESSIN, heritee des trois premieres figures et non negociable :
le viewBox fait 445 unites de large, soit exactement la largeur du corps
(157,0 mm). Une unite vaut donc UN POINT au rendu, et les corps de texte se
posent a leur valeur finale — 8,5 pour un libelle, 7 pour une annotation.
Toute reprise de la grille du gabarit oblige a regenerer les figures.

⚠ LE FOND EST EXPLICITE, et il n'est pas decoratif : la figure se rend dans DEUX
supports — le PDF, sur blanc, ou le rectangle est invisible, et la page `.html`
de la piece, a theme SOMBRE, ou les textes poses hors des bandes seraient noirs
sur noir.

⚠ CHAQUE FIGURE PORTE SA RESERVE. C'est la signature du volume : la figure 8.1
ne montre pas seulement la reduction N×M, elle montre ce que la couche de
contrat NE PORTE PAS, parce que le paragraphe y consacre sa seconde moitie. Le
parametre `reserve` n'est pas une legende — c'est ce que la figure refuse de
laisser croire. Ne pas le rendre optionnel.
"""
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent

W = 445                       # largeur du corps, en points
ENCRE, ACCENT = "#212121", "#9A3B12"
GRIS, GRIS2, FILET = "#4d4d4d", "#737373", "#C2C2C2"
CREME, FOND, BLANC = "#FAF5F0", "#FDFBF9", "#FFFFFF"

STYLE = """
  .l      { font-family: Corbel, Candara, "Segoe UI", sans-serif; }
  .bande  { font-size: 8.5px; font-weight: 700; fill: %s; }
  .rang   { font-size: 7px;   font-weight: 700; fill: %s; }
  .titre  { font-size: 6.5px; font-weight: 700; fill: %s; letter-spacing: .1em; }
  .titreg { font-size: 6.5px; font-weight: 700; fill: %s; letter-spacing: .1em; }
  .ann    { font-size: 7px;   fill: %s; }
  .annf   { font-size: 7px;   font-weight: 700; fill: %s; }
  .renvoi { font-size: 6.2px; fill: %s; }
  .gris   { font-size: 8.5px; font-weight: 700; fill: %s; }
  .date   { font-size: 6.5px; font-weight: 700; fill: %s; }
""" % (ENCRE, ACCENT, ACCENT, GRIS2, GRIS, ENCRE, GRIS2, GRIS2, ACCENT)


# ---------------------------------------------------------------- utilitaires
def ech(t):
    # ⚠ LE MARQUEUR « ⚠ » NE PARAIT PAS DANS LES FIGURES, et c'est la meme
    # regle que pour le corps : `build/accentuation.lua` l'a retire des 1 072
    # pages le 31 juillet 2026, pour saturation et parce qu'il est hors famille.
    # Le laisser reparaitre dans les figures rouvrirait par l'image ce que la
    # regle vient de fermer par le texte. Les entrees de `contenu.py` peuvent
    # donc l'ecrire — il tombe ici, une fois, pour toutes.
    t = t.replace("⚠ ", "").replace("⚠", "")
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def coupe(texte, largeur, taille=7.0):
    """Replie un texte a la largeur donnee, en points.

    ⚠ L'avance moyenne de Corbel vaut ~0,475 em sur du francais courant. La
    valeur est APPROCHEE et c'est assume : une figure dont le texte deborde se
    voit au rendu, et la marge de 4 % ci-dessous suffit sur tout le corpus.
    """
    if not texte:
        return []
    max_car = max(8, int(largeur / (0.475 * taille) * 0.96))
    lignes, courante = [], ""
    for mot in texte.split():
        essai = (courante + " " + mot).strip()
        if len(essai) <= max_car:
            courante = essai
        else:
            if courante:
                lignes.append(courante)
            courante = mot
    if courante:
        lignes.append(courante)
    return lignes


def txt(x, y, s, classe="ann", ancre=None, rot=None):
    a = f' text-anchor="{ancre}"' if ancre else ""
    if rot is not None:
        return (f'<text class="l {classe}" transform="translate({x},{y}) '
                f'rotate({rot})"{a}>{ech(s)}</text>')
    return f'<text class="l {classe}" x="{x}" y="{y}"{a}>{ech(s)}</text>'


def bloc_texte(x, y, s, largeur, classe="ann", pas=11, taille=7.0):
    out = []
    for i, ligne in enumerate(coupe(s, largeur, taille)):
        out.append(txt(x, y + i * pas, ligne, classe))
    return out, y + max(1, len(coupe(s, largeur, taille))) * pas - pas


def rect(x, y, w, h, fill=CREME, stroke=FILET, sw=".6", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    f = f' fill="{fill}"' if fill else ' fill="none"'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{f} stroke="{stroke}" stroke-width="{sw}"{d}/>'


def ligne(d, stroke=FILET, sw=".6", dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"{da}/>'


def fleche(x1, y, x2, couleur=ACCENT):
    """Fleche horizontale de x1 a x2 (pointe a x2)."""
    return [ligne(f"M {x1} {y} H {x2 - 4}", couleur, ".9"),
            f'<path d="M {x2} {y} l -4 -3 v 6 z" fill="{couleur}"/>']


def fleche_bas(x, y1, y2, couleur=ACCENT):
    return [ligne(f"M {x} {y1} V {y2 - 4}", couleur, ".9"),
            f'<path d="M {x} {y2} l -3 -4 h 6 z" fill="{couleur}"/>']


# ------------------------------------------------------------------- montage
def rendu(nom, corps, hauteur, alt, source, reserve):
    """Assemble un SVG complet et l'ecrit dans `figures/`."""
    if not reserve:
        raise ValueError(f"{nom} : une figure du volume porte toujours sa réserve")
    y = hauteur + 6
    pied = [ligne(f"M 0 {y} H {W}", FILET, ".6")]
    lignes = coupe(reserve, W - 4, 7.0)
    for i, l in enumerate(lignes):
        pied.append(txt(0, y + 13 + i * 10, l, "ann"))
    total = y + 13 + len(lignes) * 10 - 4

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {total}" '
           f'width="{W}" height="{total}" role="img" aria-label="{ech(alt)}">',
           f'  <!-- {source}',
           '       Genere par figures/dessine.py — ne pas retoucher a la main :',
           '       la retouche se perd a la regeneration. Convention : viewBox de',
           '       445 unites = largeur du corps, une unite = un point. -->',
           '  <defs><style>' + STYLE + '  </style></defs>',
           f'  <rect x="0" y="0" width="{W}" height="{total}" fill="{FOND}"/>']
    svg += ["  " + e for e in corps + pied]
    svg.append("</svg>")
    (RACINE / f"{nom}.svg").write_text("\n".join(svg) + "\n", encoding="utf-8")
    return total


# ---------------------------------------------------------------- primitives
def nlig(s, largeur, taille=7.0):
    """Nombre de lignes qu'un texte occupe une fois replie. ⚠ TOUTE HAUTEUR DE
    BOITE SE CALCULE AVEC CELA : une hauteur posee au juge deborde des qu'un
    libelle s'allonge, et le debordement ne se voit qu'au rendu."""
    return max(1, len(coupe(s, largeur, taille))) if s else 0


def bandes(items, titre=None, fleches=False, cols=None, h=None):
    """N boites libellees en ligne (ou en grille). item = (rang, nom, detail, renvoi)."""
    n = len(items)
    cols = cols or n
    rangs = (n + cols - 1) // cols
    gout = 15
    lw = (W - gout * (cols - 1)) / cols
    y0 = 14 if titre else 0
    lmax = max(nlig(i[2], lw - 20) for i in items)
    rmax = max(nlig(i[3], lw - 20, 6.2) for i in items)
    hb = h or (36 + 11 * lmax + (10 * rmax if rmax else 0))
    out = []
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    for k, (rang, nom, detail, renvoi) in enumerate(items):
        c, r = k % cols, k // cols
        x = round(c * (lw + gout))
        y = y0 + r * (hb + 16)
        out.append(rect(x, y, round(lw), hb))
        if rang:
            out.append(txt(x + 10, y + 18, rang, "rang"))
            out.append(txt(x + 10 + 5 + 6 * len(rang), y + 18, nom, "bande"))
        else:
            out.append(txt(x + 10, y + 18, nom, "bande"))
        e, _ = bloc_texte(x + 10, y + 33, detail, lw - 20)
        out += e
        if renvoi:
            yr = y + 36 + 11 * lmax
            for i, l in enumerate(coupe(renvoi, lw - 20, 6.2)):
                out.append(txt(x + 10, yr + i * 10, l, "renvoi"))
        if fleches and c < cols - 1 and k < n - 1:
            mx = x + lw + 2
            out += fleche(mx + 1, y + hb / 2, mx + gout - 3)
    return out, y0 + rangs * (hb + 16) - 16


def pile(couches, titre=None, notes=None, inverse=True):
    """Couches empilees. couche = (rang, nom, detail). `notes` : annotations a droite."""
    lw = W * 0.52 if notes else W
    out = []
    y0 = 14 if titre else 0
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    seq = list(reversed(couches)) if inverse else couches
    y = y0
    for rang, nom, detail in seq:
        # ⚠ Hauteur PROPRE a chaque couche : une hauteur commune deborde des que
        # l'une porte un libelle plus long que les autres.
        hb = 24 + 11 * nlig(detail, lw - 20) + (6 if detail else 0)
        out.append(rect(0, y, round(lw), hb))
        out.append(txt(10, y + 17, rang, "rang"))
        out.append(txt(10 + 5 + 6 * len(str(rang)), y + 17, nom, "bande"))
        if detail:
            e, _ = bloc_texte(10, y + 30, detail, lw - 20)
            out += e
        y += hb + 4
    bas = y - 4
    if notes:
        nx = lw + 16
        ny = y0 + 12
        for etiquette, corps in notes:
            out.append(txt(nx, ny, etiquette, "annf"))
            e, ny = bloc_texte(nx, ny + 12, corps, W - nx)
            out += e
            ny += 16
        bas = max(bas, ny - 10)
    return out, bas


def frise(jalons, titre=None, rebours=False, couloirs=None):
    """Ligne de temps. jalon = (date, libelle, note, etat) ; etat : plein|creux|barre."""
    out = []
    y0 = 14 if titre else 0
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    axe = y0 + 26
    out.append(ligne(f"M 0 {axe} H {W - 6}", ACCENT, ".9"))
    if rebours:
        out.append(f'<path d="M 0 {axe} l 6 -3 v 6 z" fill="{ACCENT}"/>')
    else:
        out.append(f'<path d="M {W} {axe} l -6 -3 v 6 z" fill="{ACCENT}"/>')
    n = len(jalons)
    # ⚠ UNE COLONNE PAR JALON, et non des reperes repartis sur l'axe : reparti,
    # le dernier libelle deborde a droite, et le rabattre le fait chevaucher
    # l'avant-dernier. La colonne borne le repli du texte, donc la collision.
    pas = W / n
    lt = pas - 9
    bas = axe
    for i, (date, libelle, note, etat) in enumerate(jalons):
        cx = pas * i
        x = round(cx + 5, 1)
        if etat == "creux":
            out.append(f'<circle cx="{x}" cy="{axe}" r="3.2" fill="{FOND}" stroke="{ACCENT}" stroke-width=".9"/>')
        elif etat == "barre":
            out.append(ligne(f"M {x-3} {axe-3} l 6 6 M {x-3} {axe+3} l 6 -6", GRIS2, "1"))
        else:
            out.append(f'<circle cx="{x}" cy="{axe}" r="3.2" fill="{ACCENT}"/>')
        lx = round(cx)
        out.append(txt(lx, axe - 10, date, "date"))
        e, yb = bloc_texte(lx, axe + 16, libelle, lt, "annf")
        out += e
        if note:
            e, yb = bloc_texte(lx, yb + 13, note, lt)
            out += e
        bas = max(bas, yb)
    return out, max(bas, axe + 20)


def chaine(maillons, titre=None, rupture=None, boucle=False):
    """Chaine de maillons flechee. maillon = (nom, detail). `rupture` : index apres
    lequel le lien casse — le trait passe au pointille gris et porte son motif."""
    nom_rupture, idx = (rupture or (None, None))
    n = len(maillons)
    gout = 22
    lw = (W - gout * (n - 1)) / n
    hb = 34 + 11 * max([nlig(m[1], lw - 18) for m in maillons] + [0])
    out = []
    y0 = 14 if titre else 0
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    for k, (nom, detail) in enumerate(maillons):
        x = round(k * (lw + gout))
        out.append(rect(x, y0, round(lw), hb))
        out.append(txt(x + 9, y0 + 17, nom, "bande"))
        if detail:
            e, _ = bloc_texte(x + 9, y0 + 30, detail, lw - 18)
            out += e
        if k < n - 1:
            mx = x + lw
            if idx is not None and k == idx:
                out.append(ligne(f"M {mx + 3} {y0 + hb/2} H {mx + gout - 3}", GRIS2, ".9", "2.5 2"))
                out.append(txt(mx + gout / 2, y0 + hb / 2 - 6, "✕", "annf", "middle"))
            else:
                out += fleche(mx + 3, y0 + hb / 2, mx + gout - 2)
    bas = y0 + hb
    if nom_rupture:
        bas += 14
        out.append(txt(0, bas, nom_rupture, "annf"))
    if boucle:
        y = y0 + hb + 10
        out.append(ligne(f"M {round(W - lw/2)} {y0 + hb} V {y} H {round(lw/2)} V {y0 + hb + 4}", ACCENT, ".9"))
        out.append(f'<path d="M {round(lw/2)} {y0 + hb} l -3 4 h 6 z" fill="{ACCENT}"/>')
        bas = max(bas, y + 4)
    return out, bas


def matrice(colonnes, rangees, cellules, titre=None, axes=None):
    """Grille N×M. `cellules` : dict (r,c) -> (marque, note). Marque : ✓ ~ ✕ ou texte."""
    out = []
    y0 = 14 if titre else 0
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    lx = 108
    cw = (W - lx) / len(colonnes)
    hr = 30
    ytete = y0 + 14
    for j, c in enumerate(colonnes):
        e, _ = bloc_texte(round(lx + j * cw + 5), ytete, c, cw - 8, "annf")
        out += e
    ycorps = ytete + 8 + 11 * max(len(coupe(c, cw - 8)) for c in colonnes)
    out.append(ligne(f"M 0 {ycorps - 6} H {W}", ENCRE, "1.1"))
    for i, r in enumerate(rangees):
        y = ycorps + i * hr
        e, _ = bloc_texte(0, y + 12, r, lx - 8, "annf")
        out += e
        if i:
            out.append(ligne(f"M 0 {y - 4} H {W}", FILET, ".5"))
        for j in range(len(colonnes)):
            marque, note = cellules.get((i, j), ("", ""))
            cx = round(lx + j * cw + 5)
            if marque:
                out.append(txt(cx, y + 12, marque, "annf"))
            if note:
                e, _ = bloc_texte(cx + (14 if marque else 0), y + 12, note, cw - 20)
                out += e
    bas = ycorps + len(rangees) * hr - 4
    out.append(ligne(f"M 0 {bas} H {W}", ENCRE, "1.1"))
    if axes:
        bas += 13
        out.append(txt(0, bas, axes, "renvoi"))
    return out, bas


def paire(gauche, droite, titre_g=None, titre_d=None, accent_d=True):
    """Deux panneaux cote a cote. Chaque panneau : (libelle, [lignes], legende)."""
    lw = (W - 26) / 2
    # ⚠ Les deux panneaux prennent la MEME hauteur de cadre, mesuree sur le plus
    # charge : deux cadres inegaux se lisent comme une hierarchie entre eux, ce
    # qu'une comparaison ne doit jamais suggerer.
    def h_items(items):
        return 26 + sum(11 * nlig(i, lw - 18) + 8 for i in items)
    hcadre = max(h_items(gauche[1]), h_items(droite[1]))
    out = []
    hauts = []
    for k, (panneau, tg, ac) in enumerate(((gauche, titre_g, False), (droite, titre_d, accent_d))):
        x = round(k * (lw + 26))
        y = 0
        if tg:
            out.append(txt(x, 8, tg, "titre" if ac else "titreg"))
            y = 14
        libelle, items, legende = panneau
        out.append(rect(x, y, round(lw), hcadre, BLANC if ac else CREME,
                        ACCENT if ac else FILET, ".9" if ac else ".6"))
        out.append(txt(x + 9, y + 16, libelle, "bande"))
        yi = y + 32
        for it in items:
            e, _ = bloc_texte(x + 9, yi, it, lw - 18)
            out += e
            yi += 11 * nlig(it, lw - 18) + 8
        yb = y + hcadre
        if legende:
            e, yb = bloc_texte(x, yb + 13, legende, lw, "annf")
            out += e
        hauts.append(yb)
    return out, max(hauts)


def arbre(racine, branches, titre=None):
    """Racine, puis N branches. branche = (condition, consequence, note)."""
    out = []
    y0 = 14 if titre else 0
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    e, yb = bloc_texte(0, y0 + 10, racine, W, "bande", 12, 8.5)
    out += e
    yb += 12
    n = len(branches)
    gout = 14
    lw = (W - 24 - gout * (n - 1)) / n
    out.append(ligne(f"M 12 {yb} H {round(12 + (n-1)*(lw+gout) + lw/2)}", FILET, ".6"))
    hb = 26 + 11 * max(len(coupe(b[1], lw - 18)) for b in branches)
    for k, (cond, cons, note) in enumerate(branches):
        x = round(12 + k * (lw + gout))
        out += fleche_bas(round(x + lw / 2), yb, yb + 12)
        out.append(txt(x, yb + 22, cond, "rang"))
        out.append(rect(x, yb + 26, round(lw), hb))
        out.append(txt(x + 9, yb + 42, cons.split("|")[0], "bande"))
        e, _ = bloc_texte(x + 9, yb + 55, note, lw - 18)
        out += e
    return out, yb + 26 + hb


def venn(ensembles, centre, titre=None):
    """Deux ou trois ensembles et leur intersection nommee."""
    out = []
    y0 = 14 if titre else 0
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    n = len(ensembles)
    r = 52
    cy = y0 + r + 8
    cx0 = W / 2 - (r * 0.62 if n == 2 else r * 0.72)
    pos = ([(cx0, cy), (cx0 + r * 1.24, cy)] if n == 2 else
           [(cx0, cy - 14), (cx0 + r * 1.44, cy - 14), (cx0 + r * 0.72, cy + 34)])
    for (cx, cyy), (nom, detail) in zip(pos, ensembles):
        out.append(f'<circle cx="{round(cx,1)}" cy="{round(cyy,1)}" r="{r}" fill="{CREME}" '
                   f'fill-opacity=".55" stroke="{FILET}" stroke-width=".6"/>')
    for (cx, cyy), (nom, detail) in zip(pos, ensembles):
        dy = -r + 16 if cyy <= cy else r - 6
        out.append(txt(round(cx), round(cyy + dy), nom, "bande", "middle"))
        if detail:
            for i, l in enumerate(coupe(detail, 118)):
                out.append(txt(round(cx), round(cyy + dy + 12 + i * 10), l, "ann", "middle"))
    mx, my = (sum(p[0] for p in pos) / n, sum(p[1] for p in pos) / n)
    out.append(txt(round(mx), round(my + (4 if n == 2 else 10)), centre, "rang", "middle"))
    # ⚠ Le troisieme ensemble est pose PLUS BAS que les deux autres : sa hauteur
    # se compte depuis son propre centre, non depuis `cy`, sans quoi son libelle
    # et son detail passent sous le filet de la reserve.
    bas = cy + r + (48 if n == 3 else 8)
    return out, bas
