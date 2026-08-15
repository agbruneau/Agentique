#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Primitives de dessin des figures du traite sur les essaims.

Copie adaptee de `2 - Compendium/figures/dessine.py`, et non un import : le
depot fait evoluer separement les copies de ses chaines de fabrication (cf.
README, « Les copies du pipeline evoluent separement »), et le traite est hors
de l'ordre du corpus par construction. Trois divergences, toutes voulues :

  * le viewBox fait 504 unites et non 445 — le traite compose en us-letter a
    marges de 1,9 cm, soit un corps de 7 po = 504 pt (468 pt jusqu'au 13 aout
    2026, quand il composait a 2,54 cm) ;
  * ni `venn` ni `frise` : aucune figure du traite n'en a l'emploi ;
  * deux primitives propres, `courbe` et `barres` — le traite defend des
    enonces quantitatifs (la loi universelle, le taux de base bayesien) dont la
    forme EST l'argument, et qu'un tableau ne rend pas.

⚠ CONVENTION DE DESSIN, non negociable : le viewBox fait `W` unites de large,
soit exactement la largeur du corps. Une unite vaut donc UN POINT au rendu, et
les corps de texte se posent a leur valeur finale — 8,5 pour un libelle, 7 pour
une annotation. Cela suppose `#set image(width: 100%)`, pose dans l'en-tete YAML
du traite : sans cette regle, Typst lit les unites comme des pixels, rend la
figure aux trois quarts de sa largeur et l'echelle des corps de texte tombe
d'un quart.

⚠ CHAQUE FIGURE PORTE SA RESERVE. C'est la discipline du traite portee a
l'image : chaque mecanisme y nomme sa condition d'echec, chaque transposition y
nomme ce qu'elle casse. Une figure qui ne dirait que ce qui marche mentirait par
omission au meme titre. `rendu()` refuse une entree sans reserve.

⚠ RIEN QUI NE SOIT DANS LE TEXTE. Une figure du traite est une reprise, jamais
un ajout : les chiffres, les bornes et les libelles sont ceux du chapitre ou
elle se pose.
"""
from pathlib import Path

RACINE = Path(__file__).resolve().parent

W = 468                       # largeur de l'appareil, en points
# ⚠ 468 pt = 6,5 po. ELLE NE SUIT PLUS LA MARGE, ET C'EST NOUVEAU. Jusqu'au
# 15 août 2026 elle valait la largeur du CORPS DE TEXTE — 504 pt aux marges de
# 1,9 cm, puis 468 pt à celles de 2,54 cm. Depuis la recomposition des trois
# documents du dépôt sur une géométrie commune, le corps ne fait plus que
# 378 pt (marges de 117 pt) et la figure n'y tient pas : l'en-tête du traité
# rend aux figures, aux tableaux et aux blocs de code leurs 468 pt par un
# `pad(x: -45pt)` qui les fait déborder d'un pouce et demi de part et d'autre,
# et c'est CETTE largeur-là que la constante suit désormais. Les deux se
# changent donc toujours ensemble, mais le vis-à-vis a changé : c'est le
# `-45pt` de l'en-tête, non la marge, qui commande. Faute de quoi
# `#set image(width: 100%)` met la figure à l'échelle du bloc qui la contient
# et ses textes avec elle — 468 dans un corps de 378 les comprimerait de 19 %,
# et leurs 8,5 pt tomberaient à 6,9.
# ⚠⚠ ET ELLE NE SUFFIT PAS : les SVG sont des ARTEFACTS, pas des vues. Le
# dépôt a porté du 13 au 15 août 2026 une constante à 468 et dix-neuf figures
# gravées à 504 — le générateur et ses produits divergeaient sans que rien ne
# le dise. Changer W SANS régénérer ne change rien au rendu ; c'est le piège,
# et il est silencieux. Régénérer, c'est `python figures/contenu.py` —
# PAS `dessine.py`, qui est une bibliothèque sans point d'entrée et dont
# l'exécution ne fait rien, en rendant 0.
ENCRE, ACCENT = "#1A1A1A", "#8A3324"
GRIS, GRIS2, FILET = "#4D4D4D", "#767676", "#C4C4C4"
CREME, BLANC, FOND = "#F7F4F1", "#FFFFFF", "#FFFFFF"

STYLE = """
  .l      { font-family: Corbel, Candara, "Segoe UI", sans-serif; }
  .bande  { font-size: 8.5px; font-weight: 700; fill: %s; }
  .rang   { font-size: 7px;   font-weight: 700; fill: %s; }
  .titre  { font-size: 6.5px; font-weight: 700; fill: %s; letter-spacing: .1em; }
  .titreg { font-size: 6.5px; font-weight: 700; fill: %s; letter-spacing: .1em; }
  .ann    { font-size: 7px;   fill: %s; }
  .annf   { font-size: 7px;   font-weight: 700; fill: %s; }
  .renvoi { font-size: 6.2px; fill: %s; }
  .chiffre{ font-size: 8px;   font-weight: 700; fill: %s; }
""" % (ENCRE, ACCENT, ACCENT, GRIS2, GRIS, ENCRE, GRIS2, ENCRE)


# ---------------------------------------------------------------- utilitaires
def ech(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def coupe(texte, largeur, taille=7.0):
    """Replie un texte a la largeur donnee, en points.

    ⚠ L'avance moyenne de Corbel vaut ~0,475 em sur du francais courant. La
    valeur est APPROCHEE et c'est assume : un debordement se voit au rendu, et
    la marge de 4 % ci-dessous a suffi sur tout le corpus.
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


def nlig(s, largeur, taille=7.0):
    """Nombre de lignes qu'un texte occupe une fois replie. ⚠ TOUTE HAUTEUR DE
    BOITE SE CALCULE AVEC CELA : une hauteur posee au juge deborde des qu'un
    libelle s'allonge, et le debordement ne se voit qu'au rendu."""
    return max(1, len(coupe(s, largeur, taille))) if s else 0


def txt(x, y, s, classe="ann", ancre=None):
    a = f' text-anchor="{ancre}"' if ancre else ""
    return f'<text class="l {classe}" x="{x}" y="{y}"{a}>{ech(s)}</text>'


def bloc_texte(x, y, s, largeur, classe="ann", pas=11, taille=7.0):
    lignes = coupe(s, largeur, taille)
    out = [txt(x, y + i * pas, ligne, classe) for i, ligne in enumerate(lignes)]
    return out, y + max(1, len(lignes)) * pas - pas


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
        raise ValueError(f"{nom} : une figure du traité porte toujours sa réserve")
    y = hauteur + 6
    pied = [ligne(f"M 0 {y} H {W}", FILET, ".6")]
    lignes = coupe(reserve, W - 4, 7.0)
    for i, l in enumerate(lignes):
        pied.append(txt(0, y + 13 + i * 10, l, "ann"))
    total = y + 13 + len(lignes) * 10 - 4

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {total}" '
           f'width="{W}" height="{total}" role="img" aria-label="{ech(alt)}">',
           f'  <!-- {source}',
           '       Genere par figures/contenu.py — ne pas retoucher a la main :',
           '       la retouche se perd a la regeneration. Convention : viewBox de',
           f'       {W} unites = largeur du corps, une unite = un point. -->',
           '  <defs><style>' + STYLE + '  </style></defs>',
           f'  <rect x="0" y="0" width="{W}" height="{total}" fill="{FOND}"/>']
    svg += ["  " + e for e in corps + pied]
    svg.append("</svg>")
    (RACINE / f"{nom}.svg").write_text("\n".join(svg) + "\n", encoding="utf-8")
    return total


# ---------------------------------------------------------------- primitives
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


def chaine(maillons, titre=None, rupture=None, boucle=None):
    """Chaine de maillons flechee. maillon = (nom, detail). `rupture` : (motif, index)
    apres lequel le lien casse — le trait passe au pointille gris et porte sa croix.
    `boucle` : libelle du retour du dernier maillon vers le premier."""
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
                out.append(txt(round(mx + gout / 2), round(y0 + hb / 2 - 5), "✕", "annf", "middle"))
            else:
                out += fleche(mx + 3, y0 + hb / 2, mx + gout - 2)
    bas = y0 + hb
    if nom_rupture:
        # ⚠ Le motif de rupture SE REPLIE : pose sur une ligne, il sort du corps
        # des qu'il depasse une centaine de caracteres, et le debordement ne se
        # voit qu'au rendu — la figure, elle, ne signale rien.
        e, bas = bloc_texte(0, bas + 14, nom_rupture, W, "annf")
        out += e
    if boucle:
        # ⚠ Le libelle se pose SOUS le trait de retour et non dessus : centre sur
        # W/2, il croiserait la ligne horizontale, qui court d'un bout a l'autre.
        y = bas + 12
        out.append(ligne(f"M {round(W - lw/2)} {y0 + hb} V {y} H {round(lw/2)} V {y0 + hb + 4}",
                         ACCENT, ".9", "3 2"))
        out.append(f'<path d="M {round(lw/2)} {y0 + hb} l -3 4 h 6 z" fill="{ACCENT}"/>')
        e, bas = bloc_texte(0, y + 11, boucle, W, "annf")
        out += e
    return out, bas


def matrice(colonnes, rangees, cellules, titre=None, axes=None, lx=118, hr=30):
    """Grille N×M. `cellules` : dict (r,c) -> (marque, note). Marque : ✓ ~ ✕ ou texte."""
    out = []
    y0 = 14 if titre else 0
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    cw = (W - lx) / len(colonnes)
    ytete = y0 + 14
    for j, c in enumerate(colonnes):
        e, _ = bloc_texte(round(lx + j * cw + 5), ytete, c, cw - 8, "annf")
        out += e
    ycorps = ytete + 8 + 11 * max(len(coupe(c, cw - 8)) for c in colonnes)
    out.append(ligne(f"M 0 {ycorps - 6} H {W}", ENCRE, "1.1"))
    y = ycorps
    for i, r in enumerate(rangees):
        # ⚠ Hauteur PROPRE a chaque rangee : `hr` n'est qu'un plancher. Une
        # hauteur commune posee au juge tronque la rangee la plus chargee, et
        # la troncature ne se voit qu'au rendu.
        hcell = max([nlig(r, lx - 8)] +
                    [nlig(cellules.get((i, j), ("", ""))[1],
                          cw - 20 - (14 if cellules.get((i, j), ("", ""))[0] else 0))
                     for j in range(len(colonnes))])
        h = max(hr, 12 + 11 * hcell)
        if i:
            out.append(ligne(f"M 0 {y - 6} H {W}", FILET, ".5"))
        e, _ = bloc_texte(0, y + 6, r, lx - 8, "annf")
        out += e
        for j in range(len(colonnes)):
            marque, note = cellules.get((i, j), ("", ""))
            cx = round(lx + j * cw + 5)
            if marque:
                out.append(txt(cx, y + 6, marque, "annf"))
            if note:
                e, _ = bloc_texte(cx + (14 if marque else 0), y + 6, note,
                                  cw - 20 - (14 if marque else 0))
                out += e
        y += h
    bas = y - 6
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
    def h_items(panneau):
        # ⚠ Le libelle du panneau SE REPLIE, et sa hauteur entre dans celle du
        # cadre : les libelles de ce traite sont des phrases entieres — un
        # enonce de S1, une exigence — et non des titres de deux mots.
        return (26 + 12 * (nlig(panneau[0], lw - 18, 8.5) - 1)
                + sum(11 * nlig(i, lw - 18) + 8 for i in panneau[1]))
    hcadre = max(h_items(gauche), h_items(droite))
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
        e, yl = bloc_texte(x + 9, y + 16, libelle, lw - 18, "bande", 12, 8.5)
        out += e
        yi = yl + 16
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
    # ⚠ Le connecteur va d'un CENTRE de branche a l'autre : parti du bord gauche,
    # il laisse pendre un segment a gauche de la premiere fleche.
    out.append(ligne(f"M {round(12 + lw/2)} {yb} H {round(12 + (n-1)*(lw+gout) + lw/2)}",
                     FILET, ".6"))
    # ⚠ La consequence SE REPLIE elle aussi, et sa hauteur entre dans celle des
    # boites : « Implantation distribuee coherente et sans coordination » tient
    # tout juste sur une ligne, et le libelle suivant ne tiendra pas.
    lcons = max(nlig(b[1], lw - 18, 8.5) for b in branches)
    hb = 26 + 12 * (lcons - 1) + 11 * max(nlig(b[2], lw - 18) for b in branches)
    for k, (cond, cons, note) in enumerate(branches):
        x = round(12 + k * (lw + gout))
        out += fleche_bas(round(x + lw / 2), yb, yb + 12)
        out.append(txt(x, yb + 22, cond, "rang"))
        out.append(rect(x, yb + 26, round(lw), hb))
        e, _ = bloc_texte(x + 9, yb + 42, cons, lw - 18, "bande", 12, 8.5)
        out += e
        # Les notes s'alignent sur `lcons` et non sur le repli propre a chaque
        # branche : deux notes a des hauteurs differentes se lisent comme une
        # hierarchie entre les branches, ce qu'une alternative ne doit pas dire.
        e, _ = bloc_texte(x + 9, yb + 42 + 12 * (lcons - 1) + 13, note, lw - 18)
        out += e
    return out, yb + 26 + hb


def courbe(series, xmax, ymax, titre=None, xlab="", ylab="", reperes=None, hcadre=150):
    """Traces y = f(x) sur un cadre commun.

    `series` : liste de (libelle, f, style) ; style ∈ {plein, pointille}.
    `reperes` : liste de (x, y, libelle) — un point nomme sur le trace.

    ⚠ Une courbe est ici un ARGUMENT et non un ornement : le traite soutient
    qu'un essaim tenant une vue commune a un MAXIMUM et non un rendement
    decroissant, enonce dont la forme est la demonstration. Un tableau de
    valeurs ne montre pas un retournement ; un trace, si.
    """
    out = []
    y0 = 14 if titre else 0
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    gx, gy = 34, y0 + 4                 # coin haut-gauche du cadre de trace
    lgd = 150                            # colonne de legende, a droite
    cw, ch = W - gx - lgd, hcadre
    px = lambda x: gx + cw * x / xmax
    py = lambda y: gy + ch * (1 - y / ymax)

    out.append(ligne(f"M {gx} {gy} V {gy + ch} H {gx + cw}", ENCRE, ".9"))
    for frac in (0.25, 0.5, 0.75, 1.0):  # graduations horizontales
        yy = round(py(ymax * frac), 1)
        out.append(ligne(f"M {gx} {yy} H {gx + cw}", FILET, ".4", "2 3"))
        out.append(txt(gx - 5, yy + 2.5, f"{ymax * frac:g}", "renvoi", "end"))
    for frac in (0.25, 0.5, 0.75, 1.0):
        xx = round(px(xmax * frac), 1)
        out.append(txt(xx, gy + ch + 11, f"{xmax * frac:g}", "renvoi", "middle"))
    out.append(txt(gx + cw, gy + ch + 22, xlab, "renvoi", "end"))
    out.append(txt(gx - 5, gy - 3, ylab, "renvoi", "end"))

    ly = gy + 12
    for libelle, f, style in series:
        pts = []
        for i in range(0, 201):
            x = xmax * i / 200
            if x <= 0:
                continue
            pts.append(f"{round(px(x), 1)} {round(py(min(f(x), ymax)), 1)}")
        out.append(ligne("M " + " L ".join(pts), ACCENT, "1.2",
                         "3 2" if style == "pointille" else None))
        out.append(ligne(f"M {gx + cw + 12} {ly - 2.5} h 14", ACCENT, "1.2",
                         "3 2" if style == "pointille" else None))
        e, ly = bloc_texte(gx + cw + 30, ly, libelle, lgd - 32)
        out += e
        ly += 16
    for x, y, libelle in (reperes or []):
        cx, cy = round(px(x), 1), round(py(y), 1)
        out.append(f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="{ACCENT}"/>')
        out.append(txt(cx + 6, cy - 4, libelle, "annf"))
    return out, max(gy + ch + 24, ly - 10)


def barres(items, vmax, titre=None, unite="", lx=176):
    """Barres horizontales. item = (libelle, valeur, etiquette, plein).

    `plein` a faux dessine la barre en creux : c'est la valeur de reference a
    laquelle les autres se comparent.
    """
    out = []
    y0 = 14 if titre else 0
    if titre:
        out.append(txt(0, 8, titre, "titre"))
    bw = W - lx - 60
    y = y0 + 4
    for libelle, valeur, etiquette, plein in items:
        nl = nlig(libelle, lx - 10)
        h = max(13, 11 * nl)
        e, _ = bloc_texte(0, y + 9, libelle, lx - 10)
        out += e
        lg = max(1.2, bw * valeur / vmax)
        out.append(rect(lx, y + 1.5, round(lg, 1), 9,
                        ACCENT if plein else BLANC, ACCENT, ".7"))
        out.append(txt(lx + lg + 5, y + 9, etiquette, "chiffre"))
        y += h + 7
    bas = y - 7
    if unite:
        # ⚠ Meme regle que la rupture d'une chaine : l'unite se replie sur toute
        # la largeur du corps, et non a partir de `lx`.
        for i, l in enumerate(coupe(unite, W, 6.2)):
            out.append(txt(0, bas + 12 + i * 9, l, "renvoi"))
        bas += 12 + 9 * (len(coupe(unite, W, 6.2)) - 1)
    return out, bas
