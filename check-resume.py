#!/usr/bin/env python3
"""Le budget de mise en page que rien d'autre ne voit.

Le gabarit Typst compose le resume dans un bloc QUI NE SE SCINDE PAS : un resume
trop long ne passe pas a la page suivante, il se fait rogner sous la marge basse
— et `pandoc` sort 0. Ni `check-veille.py` ni le rendu ne le signalent.

Ce controle mesure la position reelle de la derniere ligne de texte de la page de
titre, dans le PDF rendu, et la confronte a la marge basse.

Usage : python check-resume.py [Veille Technologique.pdf]  -> sortie 0 si le
resume tient sur sa page, 1 sinon.
"""
import io, re, sys, zlib

MARGE_BASSE = 73.7   # 2,6 cm, valeur de l'en-tete YAML
DEGAGEMENT = 10.0    # sous ce seuil, le resume frole la marge : on alerte


def objets(d):
    """{numero: corps} pour tous les objets indirects du fichier."""
    return {int(m.group(1)): m.group(2)
            for m in re.finditer(rb'(?m)^(\d+) 0 obj\b(.*?)\bendobj', d, re.S)}


def flux(corps, d):
    """Contenu decompresse d'un objet flux."""
    m = re.search(rb'stream\r?\n(.*?)\r?\nendstream', corps, re.S)
    if not m:
        return b''
    brut = m.group(1)
    if b'/FlateDecode' in corps:
        try:
            return zlib.decompress(brut)
        except zlib.error:
            return b''
    return brut


def page_une(d, objs):
    """Contenu de la premiere page, dans l'ordre reel de l'arbre des pages.

    Deux pieges : `/Type/PageLabel` contient `/Page`, et l'ordre du fichier
    n'est pas celui du document — seul `/Kids` donne la premiere page.
    """
    kids = None
    for corps in objs.values():
        if re.search(rb'/Type\s*/Pages', corps) and b'/Kids' in corps:
            k = re.search(rb'/Kids\s*\[(.*?)\]', corps, re.S)
            if k:
                kids = [int(x) for x in re.findall(rb'(\d+) 0 R', k.group(1))]
                break
    if not kids:
        kids = [n for n, c in objs.items() if re.search(rb'/Type\s*/Page(?![a-zA-Z])', c)]
    if not kids:
        return b'', None
    m = re.search(rb'/Contents\s+(\d+) 0 R', objs[kids[0]])
    return (flux(objs[int(m.group(1))], d), kids[0]) if m else (b'', kids[0])


def ordonnees(contenu):
    """Toutes les ordonnees ou du texte est effectivement pose.

    Le gabarit Typst ne pose PAS la position dans la matrice de texte : `Tm` y
    vaut `1 0 0 -1 0 0`, et la position reelle est portee par le `cm` qui
    precede chaque `BT`. Mesurer `Tm` rend zero partout — piege verifie.
    """
    cms = [(m.end(), float(m.group(6))) for m in re.finditer(
        rb'([-\d.]+) +([-\d.]+) +([-\d.]+) +([-\d.]+) +([-\d.]+) +([-\d.]+) +cm', contenu)]
    ys = []
    for bt in re.finditer(rb'\bBT\b', contenu):
        precedents = [y for fin, y in cms if fin <= bt.start()]
        if precedents:
            ys.append(precedents[-1])
    return ys


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else 'Veille Technologique.pdf'
    d = io.open(src, 'rb').read()
    contenu, num = page_une(d, objets(d))
    if not contenu:
        print(f'{src} : page de titre illisible — controle inapplicable')
        return 1
    ys = ordonnees(contenu)
    if not ys:
        print(f'{src} : aucun texte localise en page 1 — controle inapplicable')
        return 1
    bas = min(ys)
    marge = bas - MARGE_BASSE
    etat = 'OK' if marge >= DEGAGEMENT else ('LIMITE' if marge >= 0 else 'ECHEC')
    print(f'Budget de mise en page — {src}')
    print(f'  page de titre : {len(ys)} lignes de texte, derniere a y = {bas:.1f} pt')
    print(f'  marge basse   : {MARGE_BASSE} pt -> degagement {marge:+.1f} pt  [{etat}]')
    if marge < 0:
        print(f'\nECHEC : le resume deborde de {-marge:.1f} pt sous la marge basse.\n'
              f'  Le bloc du gabarit Typst ne se scinde pas : ce qui deborde est ROGNE,\n'
              f'  invisible au rendu comme a `check-veille.py`. Condenser le resume.')
        return 1
    if marge < DEGAGEMENT:
        print(f'\nLIMITE : {marge:.1f} pt de degagement seulement. Toute reprise du '
              f'resume le fera deborder.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
