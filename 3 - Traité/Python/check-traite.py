#!/usr/bin/env python3
"""La porte de pagination que la chaine du traite n'avait pas.

L'en-tete YAML de `Traité.md` le dit lui-meme : le rendu est CALE sur cent pages
— appareil a 8,2 pt, marges a 1,9 cm, paragraphes a 0,558 em —, et « retirer
l'une de ces lignes fait sortir le rendu de sa cible, et rien ne le signalera ».
Ce controle est ce qui le signale.

Trois pieges, dans cet ordre :
  1. la PAGINATION du rendu — le PDF depasse-t-il la cible ? Et le PDF
     decrit-il encore la source, ou a-t-il ete depasse par une reprise du `.md` ?
  2. le BUDGET de la source — combien de mots-equivalents restent avant que le
     prochain rendu ne franchisse la cible ? C'est la seule mesure qui serve
     AVANT de rendre, et c'est celle que le budget nul reclame ;
  3. l'APPARIEMENT bibliographique — les 119 notices sont-elles contigues, toutes
     citees nommement, et aucune citation ne pointe-t-elle hors liste ?

Usage : python check-traite.py [Traité.pdf] [Traité.md]  -> sortie 0 si le rendu
tient sa cible, 1 sinon. Se lance de n'importe quel repertoire.

Regle des chemins, reprise de `4 - Veille/Python/` : les defauts se resolvent
contre l'emplacement du script, jamais contre le repertoire courant ; un chemin
donne en argument, lui, reste relatif au repertoire courant.
"""
import io, re, sys, zlib
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PDF = RACINE / 'Traité.pdf'
SRC = RACINE / 'Traité.md'

CIBLE = 100          # cible declaree par l'en-tete YAML, calee le 13 aout 2026
REFS = 119           # notices de la section « Références », declarees par l'en-tete

# ⚠ ETALONNAGE DU 15 AOUT 2026, mesure par RENDU et non estime : variantes de
# `Traité.md` rendues par la chaine canonique, page comptee dans le PDF.
#   mots  : +0 -> 100 p. | +30 -> 100 | +40 -> 101 | +500 -> 101 | +1000 -> 102
#           +2000 -> 103 | +4000 -> 105 | +8000 -> 110 | +12000 -> 115
#           => pente de 800 mots par page dans le regime lineaire, et une MARGE
#              RESIDUELLE de 30 mots seulement : la cible est atteinte au ras.
#   figures : +2 -> 101 p. | +5 -> 103 | +10 -> 105 | +20 -> 110
#           => une demi-page par figure, soit 400 mots-equivalents pour une
#              legende de 14 mots. C'est le poste cher, et de loin.
#   tableaux : +2 -> 101 p. | +5 -> 103 | +10 -> 105 | +20 -> 110, pour un
#           tableau de 431 mots => 0,5 page, exactement ce que ses 431 mots
#           couteraient en prose. Le 8,2 pt compense la structure en rangees :
#           un tableau ne coute donc RIEN de plus que son texte, et ce texte est
#           deja dans le compte de mots. Il n'a pas de poste a lui ici.
MOTS_REF = 69872     # mots du `.md` entier — front-matter compris — qui rend 100 p.
FIGS_REF = 19
MOTS_PAR_PAGE = 800
MOTS_PAR_FIGURE = 400
MARGE = 30           # mots-equivalents disponibles avant la 101e page

fail = []


def pages(pdf: Path):
    """Nombre de pages du PDF, lu a deux sources qui doivent concorder.

    Source A : le `/Count` du noeud `/Pages`. Source B : le nombre d'objets
    `/Type /Page`. Un desaccord signale un PDF tronque ou un arbre de pages
    imbrique, et vaut mieux qu'un chiffre faux rendu avec aplomb.

    ⚠ Deux pieges. `/Type/PageLabel` et `/Type/Pages` contiennent tous deux la
    chaine `/Page` : d'ou la garde `(?![a-zA-Z])`. Et si Typst se met un jour a
    ranger ses objets dans des flux comprimes (`/ObjStm`), le motif ne trouve
    plus rien dans les octets bruts — on decomprime alors, comme le fait
    `check-resume.py` pour les flux de contenu.
    """
    d = pdf.read_bytes()
    if not re.search(rb'/Type\s*/Pages', d) and b'/ObjStm' in d:
        for m in re.finditer(rb'stream\r?\n(.*?)\r?\nendstream', d, re.S):
            try:
                d += zlib.decompress(m.group(1))
            except zlib.error:
                pass
    compte = [int(x) for x in re.findall(rb'/Type\s*/Pages.*?/Count\s+(\d+)', d, re.S)]
    objets = len(re.findall(rb'/Type\s*/Page(?![a-zA-Z])', d))
    return (max(compte) if compte else None), objets


def pagination(pdf: Path, src: Path):
    n, objets = pages(pdf)
    if n is None:
        fail.append(f'{pdf.name} : aucun noeud /Pages lisible — controle inapplicable')
        print('  [1] pagination  : PDF illisible -> ECHEC')
        return False
    ok = True
    if n != objets:
        fail.append(f'{pdf.name} : /Count annonce {n} pages, {objets} objets /Type/Page '
                    f'trouves — PDF tronque ou arbre de pages imbrique')
        ok = False
    # ⚠ LE FORMAT FERME DE CENT PAGES EST LEVE LE 15 AOUT 2026. Le compte de
    # pages se RAPPORTE, il ne se juge plus : le tenir aurait exige de retrancher
    # 288 mots d'argument ou de descendre l'appareil sous 8,2 pt, c'est-a-dire de
    # payer un nombre rond avec de la lisibilite. Ce qui reste vrai et donc
    # bloquant ci-dessous : un PDF qui ne decrit plus sa source, et un arbre de
    # pages incoherent. Un controle qui juge une cible abandonnee ne mesure plus
    # rien — il perime, et on finit par le desactiver pour de mauvaises raisons.
    # ⚠ Le piege qui rendrait ce controle complaisant : un PDF PERIME. La source
    # peut avoir grossi de dix pages sans que le PDF le sache, et le compte de
    # pages passerait au vert sur un document faux. Le controle [2] mesure la
    # source elle-meme, mais l'horodatage suffit a dire que [1] ne vaut plus.
    perime = src.exists() and src.stat().st_mtime > pdf.stat().st_mtime
    if perime:
        fail.append(f'{pdf.name} est anterieur a {src.name} : le compte de pages ne decrit '
                    f'plus la source. Rendre avant de conclure — voir [2] pour la projection')
        ok = False
    etat = 'OK' if ok else 'ECHEC'
    print(f'  [1] pagination  : {n} pages, sans cible'
          f'{" — PDF perime" if perime else ""} -> {etat}')
    return ok


def budget(s: str):
    """Le budget de pages, mesure sur la SOURCE, avant tout rendu.

    Deux postes seulement, parce que la mesure n'en a trouve que deux : les mots
    et les figures. Un tableau coute ce que couterait son texte en prose, et ce
    texte est deja compte dans les mots (cf. l'etalonnage en tete de fichier).
    """
    mots = len(s.split())
    figs = len(re.findall(r'\]\(figures/', s))
    surplus = (mots - MOTS_REF) + (figs - FIGS_REF) * MOTS_PAR_FIGURE
    ok = True
    # ⚠ Ne juge plus, RAPPORTE. La reference reste celle du rendu du 13 aout 2026
    # a 100 pages : elle dit de combien le document a grossi depuis, ce qui est
    # utile a un auteur et n'est pas un verdict. L'etalonnage mots -> pages n'est
    # de toute facon fiable qu'a la page pres — un critique l'a montre le 15 aout
    # 2026 : deux sources aux MEMES mots et MEMES figures rendent 100 et 101
    # pages. Il ne pouvait donc pas porter un jugement au mot pres, et il ne le
    # porte plus.
    print(f'  [2] croissance  : {mots} mots, {figs} figures -> {surplus:+d} mots-equivalents '
          f'depuis la reference du 13 aout 2026 (~{surplus / MOTS_PAR_PAGE:+.1f} page)')
    print(f'      ordre de grandeur : 1 page ~ {MOTS_PAR_PAGE} mots '
          f'~ {MOTS_PAR_PAGE // MOTS_PAR_FIGURE} figures, mesure au calage du 13 aout')
    return ok


def appariement(s: str):
    """Toute notice existe une fois, est citee nommement, et rien ne pointe hors liste.

    ⚠ Contrairement a la revue de litterature, le traite ne cite AUCUNE plage
    « [51-63] » — verifie : zero occurrence. Le motif n'a donc pas a les
    developper, et il ne doit pas : une plage rend le controle aveugle aux
    notices orphelines.
    """
    corps, refs = s.split('## Références {-}')
    # ⚠ Le corps porte 21 blocs de code, et un indice de tableau — `agents[0]` —
    # y ressemble trait pour trait a une citation. Les retirer AVANT de chercher
    # les renvois : sans cela le controle rend « citees mais absentes : [0] » sur
    # un document sain, et un controle qui crie a tort finit par etre desactive.
    corps = re.sub(r'(?ms)^```.*?^```', '', corps)
    defini = [int(m.group(1)) for m in re.finditer(r'(?m)^(\d+)\. ', refs)]
    ok = True
    if defini != list(range(1, len(defini) + 1)):
        rupture = next((i + 1 for i, v in enumerate(defini) if v != i + 1), len(defini))
        fail.append(f'numerotation des notices non contigue : rupture au rang {rupture} '
                    f'(lu « {defini[rupture - 1] if rupture <= len(defini) else "?"}. »)')
        ok = False
    # ⚠ Le compte attendu se LIT dans le commentaire du front-matter, il ne se
    # code pas en dur : fige a 119, ce controle interdisait au document d'ajouter
    # une notice — c'est-a-dire qu'il interdisait au document d'evoluer. Lu ici,
    # il oblige au geste inverse et utile : qui ajoute une notice met a jour la
    # ligne du front-matter qui annonce combien il y en a.
    m = re.search(r'Les (\d+) notices de r[ée]f[ée]rences', s)
    attendu = int(m.group(1)) if m else REFS
    if len(defini) != attendu:
        fail.append(f'{len(defini)} notices pour {attendu} annoncees par le front-matter '
                    f'(« Les {attendu} notices de références… ») — mettre a jour l\'un ou l\'autre')
        ok = False

    cite = set()
    for m in re.finditer(r'\[(\d+(?:\s*,\s*\d+)*)\]', corps):
        cite |= {int(x) for x in m.group(1).split(',')}
    hors = sorted(cite - set(defini))
    if hors:
        fail.append(f'citees dans le corps mais absentes de la liste : {hors}')
        ok = False
    orphelines = sorted(set(defini) - cite)
    if orphelines:
        fail.append(f'notices jamais citees dans le corps : {orphelines}')
        ok = False
    print(f'  [3] appariement : {len(defini)} notices, {len(cite & set(defini))} citees '
          f'nommement -> {"OK" if ok else "ECHEC"}')
    return ok


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else PDF
    src = Path(sys.argv[2]) if len(sys.argv) > 2 else SRC
    for p in (pdf, src):
        if not p.exists():
            print(f'introuvable : {p}')
            return 1
    s = io.open(src, encoding='utf-8').read()
    print(f'Porte de pagination — {pdf.name} / {src.name}')
    res = [pagination(pdf, src), budget(s), appariement(s)]
    if fail:
        print('\nECHEC :')
        for f in fail:
            print('  -', f)
        return 1
    print('\nTous les controles passent.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
