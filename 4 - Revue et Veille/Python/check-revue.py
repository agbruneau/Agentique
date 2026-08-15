#!/usr/bin/env python3
"""Controles de publication de la revue de litterature.

Quatre pieges, tous verifies sur le document ENTIER :
  1. l'appariement bibliographique — toute reference citee existe, toute reference
     existante est citee, et la numerotation est contigue ;
  2. les tableaux — chaque bloc porte sa legende, faute de quoi la numerotation
     automatique de Pandoc decale les « tableau N » cites en aval ;
  3. les doublons — deux entrees ne doivent pas designer le meme document, ce qui
     arrive des qu'une piece arrive par deux fronts de recherche ;
  4. les cardinaux du regime de preuve — c'est le resultat principal de la revue,
     et il est enonce a cinq endroits qui doivent concorder avec la bibliographie.

Usage : python check-revue.py            -> sortie 0 si tout passe, 1 sinon.
"""
import re, sys, io, collections
from pathlib import Path

# Meme regle que check-veille.py : le chemin se resout contre l'emplacement du
# script, jamais contre le repertoire courant.
SRC = Path(__file__).resolve().parent.parent / 'Revue de littérature.md'
SOCLE = 50   # [1-50] : socle academique herite de la veille, repris en bloc
fail = []


def load():
    s = io.open(SRC, encoding='utf-8').read()
    corps, refs = s.split('# Références {-}')
    return corps, refs.split('::: {#refs}')[1].split('\n:::')[0]


def appariement(corps, refs):
    """Toute reference citee existe, toute reference existante est citee NOMMEMENT.

    ⚠ Piege verifie par mutation, ne pas le reintroduire : la section de
    cartographie du corpus cite des PLAGES — « [51-63] ». Si on les developpe pour
    l'appariement, elles couvrent l'integralite de la bibliographie et le controle
    devient aveugle aux orphelines : orpheliner une entree ne le fait plus tomber.
    On exige donc un appel NOMME pour chaque entree, et les plages ne servent qu'a
    verifier qu'elles ne debordent pas de la bibliographie.
    """
    defini = [int(m.group(1)) for m in re.finditer(r'(?m)^(\d+)\. ', refs)]
    ok = True
    if defini != list(range(1, len(defini) + 1)):
        fail.append('numerotation des references non contigue')
        ok = False

    sans_plages = re.sub(r'\[\d+\s*[-–]\s*\d+\]', '', corps)
    nomme = set()
    for m in re.finditer(r'\[(\d+(?:\s*,\s*\d+)*)\]', sans_plages):
        nomme |= {int(x) for x in m.group(1).split(',')}
    plages = set()
    for m in re.finditer(r'\[(\d+)\s*[-–]\s*(\d+)\]', corps):
        plages |= set(range(int(m.group(1)), int(m.group(2)) + 1))

    if (nomme | plages) - set(defini):
        fail.append(f'citees mais absentes de la liste : {sorted((nomme | plages) - set(defini))}')
        ok = False

    # Le corpus a deux origines et deux regimes de citation, declares en §2.1 :
    # le socle herite de la veille est repris EN BLOC et cite par sa plage ; les
    # pieces versees par la passe neuve doivent, elles, etre discutees une a une.
    socle = set(range(1, SOCLE + 1))
    neuves = set(defini) - socle
    orphelines = neuves - nomme
    if orphelines:
        fail.append(f'pieces de la passe neuve jamais citees nommement : {sorted(orphelines)} — '
                    f'une plage qui les couvre ne vaut pas discussion')
        ok = False
    engagees = len(socle & nomme)
    print(f'  [1] appariement : {len(defini)} definies ; {len(neuves & nomme)}/{len(neuves)} neuves '
          f'citees nommement, {engagees}/{len(socle)} du socle discutees -> {"OK" if ok else "ECHEC"}')
    return ok


def tableaux(corps):
    caps = re.findall(r'(?m)^: (.+)$', corps)
    blocs = len(re.findall(r'(?:^\|.*\n)+', corps, re.M))
    ok = blocs == len(caps)
    if not ok:
        fail.append(f'{blocs - len(caps)} table(s) sans legende : chacune consomme un numero '
                    f'et decale les « tableau N » cites en aval')
    cites = {int(g) for m in re.finditer(r'tableaux? (\d+)', corps, re.I) for g in m.groups()}
    hors = [n for n in cites if n > len(caps)]
    if hors:
        fail.append(f'« tableau N » cite hors plage (max {len(caps)}) : {sorted(hors)}')
        ok = False
    print(f'  [2] tableaux    : {blocs} blocs, {len(caps)} legendes -> {"OK" if ok else "ECHEC"}')
    return ok


def doublons(refs):
    """Deux entrees ne doivent pas designer le meme document."""
    def norm(u):
        u = re.sub(r'^https?://(?:www\.)?', '', u.rstrip('.,;)').lower())
        u = re.sub(r'[#?].*$', '', u).rstrip('/')
        return re.sub(r'v\d+$', '', u.replace('/abs/', '/').replace('/pdf/', '/'))

    entries = re.findall(r'(?m)^(\d+)\. (.*)$', refs)
    ok = True
    for label, pat, key in (('URL', r'https?://\S+', norm),
                            ('DOI', r'10\.\d{4,}/[^\s;,)]+', lambda x: x.rstrip('.').lower()),
                            ('arXiv', r'arXiv:(\d{4}\.\d{4,5})', str.lower)):
        seen = collections.defaultdict(set)
        for n, t in entries:
            for v in re.findall(pat, t, re.I):
                seen[key(v)].add(n)
        for v, ns in seen.items():
            if len(ns) > 1:
                fail.append(f'{label} partage par les entrees {sorted(ns)} : {v[:70]}')
                ok = False
    print(f'  [3] doublons    : {len(entries)} entrees confrontees -> {"OK" if ok else "ECHEC"}')
    return ok


MOTS = {'sept': 7, 'douze': 12, 'treize': 13,
        'vingt-six': 26, 'vingt-huit': 28, 'trente et une': 31}


def regimes(corps, refs):
    """Le resultat principal de la revue, mesure sur la bibliographie elle-meme.

    Le regime se lit a la mention portee par l'entree : une reference de revue ou
    d'actes, une acceptation autodeclaree, ou rien. Les trois comptes sont ensuite
    exiges partout ou le texte les enonce — resume, section de physionomie, tableau.
    """
    entries = re.findall(r'(?m)^(\d+)\. (.*)$', refs)
    arxiv = [t for _, t in entries if 'arxiv.org/abs/' in t]
    att = [t for t in arxiv if 'prépublication non révisée' not in t and 'autodéclarée' not in t
           and 'acceptation annoncée' not in t]
    auto = [t for t in arxiv if 'acceptation annoncée' in t]
    aucun = [t for t in arxiv if 'prépublication non révisée' in t]
    ok = True
    if len(att) + len(auto) + len(aucun) != len(arxiv):
        fail.append('une entree arXiv ne tombe dans aucun des trois regimes')
        ok = False
    mesure = {'attestees': len(att), 'autodeclarees': len(auto), 'sans revue': len(aucun),
              'arXiv': len(arxiv), 'total': len(entries)}
    # Ce que le texte annonce, en chiffres et en toutes lettres.
    #
    # ⚠ Piege verifie par mutation, ne pas le reintroduire : un motif qui ne connait que
    # l'ancien cardinal ne tombe pas quand le corpus grossit — il cesse de chercher, et le
    # controle passe au vert sur un document faux. Les alternatives nommees couvrent donc
    # l'ancienne ET la nouvelle valeur ; a chaque grossissement, les ajouter ici AVANT de
    # rejouer le controle.
    for nom, cle, motif in (
            ('entrees du corpus', 'total', r'corpus (\d+) pièces|(\d+) entrées et a deux origines'),
            ('pieces arXiv', 'arXiv', r'(\d+) pièces déposées sur arXiv|corpus de (\d+) pièces'),
            ('attestees', 'attestees', r'\*\*(douze|treize|sept)\*\* portent une attestation|\*\*(Douze|Treize|Sept) pièces sur \d+'),
            ('autodeclarees', 'autodeclarees', r'(Vingt-six|Vingt-huit|Trente et une) (?:autres )?(?:pièces )?annoncent'),
            ('sans revue', 'sans revue', r'Les (\d+) restantes'),
    ):
        vus = [g for m in re.finditer(motif, corps) for g in m.groups() if g]
        for v in vus:
            n = MOTS.get(v.lower(), None)
            n = int(v) if n is None and v.isdigit() else n
            if n is not None and n != mesure[cle]:
                fail.append(f'« {v} » annonce pour {nom} : la bibliographie en compte {mesure[cle]}')
                ok = False
    # le tableau des regimes
    for m in re.finditer(r'(?m)^\|\s*(?:Publication attestée|Acceptation auto-déclarée|Aucun signe)[^|]*\|\s*(\d+)\s*\|', corps):
        pass
    print(f'  [4] regimes     : {mesure["attestees"]} attestees, {mesure["autodeclarees"]} autodeclarees, '
          f'{mesure["sans revue"]} sans revue, sur {mesure["arXiv"]} arXiv -> {"OK" if ok else "ECHEC"}')
    return ok


if __name__ == '__main__':
    corps, refs = load()
    print(f'Controles de publication — {SRC.name}')
    res = [appariement(corps, refs), tableaux(corps), doublons(refs), regimes(corps, refs)]
    if fail:
        print('\nECHEC :')
        for f in fail:
            print('  -', f)
        sys.exit(1)
    print('\nTous les controles passent.')
