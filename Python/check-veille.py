#!/usr/bin/env python3
"""Controles de publication de la veille technologique.

Trois pieges que le rendu Pandoc ne signale jamais :
  1. la numerotation automatique des sections et tableaux casse les renvois en clair ;
  2. les cardinaux ecrits en toutes lettres ne se mettent pas a jour tout seuls ;
  3. deux entrees bibliographiques peuvent pointer le meme document.

Usage : python check-veille.py            -> sortie 0 si tout passe, 1 sinon.

Les motifs ci-dessous ont ete valides sur le document ENTIER. Deux pieges de
motif y sont deja neutralises, ne pas les reintroduire :
  - « (8.9) » ou « (2.0) » sont des numeros de version, pas des renvois ;
  - « quatre-vingt-dix » contient « vingt-dix », qui n'est pas un nombre.
"""
import re, sys, io, collections

SRC = 'Veille Technologique.md'
fail = []


def load():
    s = io.open(SRC, encoding='utf-8').read()
    body = s.split('# Références {-}')[0]
    refs = s.split('::: {#refs}')[1].split('\n:::')[0]
    return body, refs


def sections(body):
    """Numeros que Pandoc attribuera, dans l'ordre. Les titres {-} n'en recoivent pas."""
    sec, out, fence = [0, 0, 0], set(), False
    for ln in body.split('\n'):
        if ln.startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r'^(#{1,3}) (.+)$', ln)
        if not m or '{-}' in m.group(2):
            continue
        lvl = len(m.group(1))
        if lvl == 1:
            sec = [sec[0] + 1, 0, 0]
        elif lvl == 2:
            sec = [sec[0], sec[1] + 1, 0]
        else:
            sec = [sec[0], sec[1], sec[2] + 1]
        out.add('.'.join(str(x) for x in sec[:lvl]))
    return out


def piege1(body):
    """Renvois en clair vers sections, tableaux et questions ouvertes."""
    ok = True
    ex = sections(body)

    unresolved = set()
    for pat in (r'sections? (\d+(?:\.\d+)*)', r'§\s?(\d+(?:\.\d+)*)',
                r'sections? \d+(?:\.\d+)* (?:à|et) (\d+(?:\.\d+)*)'):
        unresolved |= {m.group(1) for m in re.finditer(pat, body) if m.group(1) not in ex}

    # forme parenthesee « (4.11.6) » : n'est un renvoi que si la tete <= nb de sections
    # de tete, et si le contexte gauche n'est pas un nom de produit ou de format.
    version = re.compile(r'(?:v|version|Camunda|OCEL|DSL|[A-Z]{2,})\s*$', re.I)
    top = max(int(x.split('.')[0]) for x in ex)
    for m in re.finditer(r'\((\d+\.\d+(?:\.\d+)?)\)', body):
        g = m.group(1)
        if int(g.split('.')[0]) > top or version.search(body[max(0, m.start() - 14):m.start()]):
            continue
        if g not in ex:
            unresolved.add(g)

    if unresolved:
        fail.append(f'renvois de section non resolus : {sorted(unresolved)}')
        ok = False

    captions = re.findall(r'^: (.+)$', body, re.M)
    blocks = len(re.findall(r'(?:^\|.*\n)+', body, re.M))
    if blocks != len(captions):
        fail.append(f'{blocks - len(captions)} table(s) sans legende : chacune consomme '
                    f'un numero et decale les « tableau N » cites en aval')
        ok = False
    cited = {int(g) for m in re.finditer(r'tableaux? (\d+)(?:\s*(?:à|et|,)\s*(\d+))?', body, re.I)
             for g in m.groups() if g}
    if [n for n in cited if n > len(captions)]:
        fail.append(f'« tableau N » cite hors plage (max {len(captions)}) : '
                    f'{sorted(n for n in cited if n > len(captions))}')
        ok = False

    qo = body[body.find('# Questions ouvertes'):body.find('# Horizon prospectif')]
    nqo = len(re.findall(r'^\d+\. ', qo, re.M))
    hors = [int(m.group(1)) for m in re.finditer(r'QO\s*(\d+)', body) if not 1 <= int(m.group(1)) <= nqo]
    if hors:
        fail.append(f'renvoi « QO n » hors plage (1-{nqo}) : {sorted(set(hors))}')
        ok = False

    print(f'  [1] renvois     : {len(ex)} sections, {len(captions)} tableaux, '
          f'{nqo} questions ouvertes -> {"OK" if ok else "ECHEC"}')
    return ok


MOTS = {'un': 1, 'une': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'cinq': 5, 'six': 6, 'sept': 7,
        'huit': 8, 'neuf': 9, 'dix': 10, 'onze': 11, 'douze': 12, 'treize': 13, 'quatorze': 14,
        'quinze': 15, 'seize': 16, 'dix-sept': 17, 'dix-huit': 18, 'dix-neuf': 19, 'vingt': 20,
        'vingt et un': 21, 'vingt-deux': 22, 'vingt-trois': 23, 'vingt-quatre': 24,
        'vingt-cinq': 25, 'trente': 30, 'quarante': 40, 'cinquante': 50}
ALT = '|'.join(sorted(MOTS, key=len, reverse=True))


def piege2(body):
    """Un cardinal en toutes lettres doit valoir la liste qu'il annonce — PARTOUT.

    Le piege n'est pas le nombre pose au titre de la liste : c'est celui qui la cite
    a distance (sommaire executif, conclusion, divulgation) et que personne ne re-mesure.
    On mesure donc la liste une fois, puis on exige que TOUTES ses mentions concordent.
    """
    def between(a, b):
        i = body.find(a)
        return body[i:body.find(b, i + 1)]

    # Chaque liste est ancree sur les tournures qui la citent REELLEMENT. Un nom nu ne
    # suffit pas : « constats » et « questions » servent aussi a des enumerations locales
    # (« Trois constats se degagent », la grille des « cinq questions » de la §7.6), que
    # la veille emploie legitimement. Un controle qui les confondrait crierait au loup.
    listes = [
        ('constats du sommaire executif',
         len(re.findall(r'\*\*(\d+)\.\s', between('# Sommaire exécutif', '# Introduction'))),
         [rf'tient en ({ALT}) constats']),
        ('contributions',
         len(re.findall(r'^\d+\.\s', between('## Contributions', '## Organisation'), re.M)),
         [rf'apporte ({ALT}) contributions']),
        ('questions ouvertes',
         len(re.findall(r'^\d+\.\s', between('# Questions ouvertes', '# Horizon'), re.M)),
         [rf'({ALT}) questions ouvertes', rf'^({ALT}) questions, directement']),
    ]
    ok, total = True, 0
    for nom, mesure, motifs in listes:
        vus = []
        for pat in motifs:
            # « quatre-vingt-dix » contient « vingt-dix » : l'ancrage a gauche l'empeche.
            vus += [(m.group(1).lower(), body[:m.start()].count('\n') + 1)
                    for m in re.finditer(rf'(?<![\w-]){pat}', body, re.I | re.M)]
        total += len(vus)
        if not vus:
            fail.append(f'plus aucun cardinal n\'annonce la liste « {nom} » — '
                        f'tournure modifiee ? le controle est devenu aveugle')
            ok = False
            continue
        for mot, ligne in vus:
            if MOTS[mot] != mesure:
                fail.append(f'« {mot} » pour « {nom} » (l. {ligne}) : la liste en compte {mesure}')
                ok = False
    print(f'  [2] cardinaux   : {len(listes)} listes, {total} mentions confrontees '
          f'-> {"OK" if ok else "ECHEC"}')
    return ok


def piege3(refs):
    """Deux entrees ne doivent pas designer le meme document."""
    def norm(u):
        u = re.sub(r'^https?://(?:www\.)?', '', u.rstrip('.,;)').lower())
        u = re.sub(r'[#?].*$', '', u).rstrip('/')
        return re.sub(r'v\d+$', '', u.replace('/abs/', '/').replace('/pdf/', '/'))

    entries = re.findall(r'^(\d+)\. (.*)$', refs, re.M)
    ok = True
    nums = [int(n) for n, _ in entries]
    if nums != list(range(1, len(nums) + 1)):
        fail.append('numerotation des references non contigue')
        ok = False

    for label, pat, key in (('URL', r'https?://\S+', norm),
                            ('DOI', r'10\.\d{4,}/[^\s;,)]+', lambda x: x.rstrip('.').lower()),
                            ('arXiv', r'arXiv:(\d{4}\.\d{4,5})', str.lower)):
        seen = collections.defaultdict(set)
        for n, t in entries:
            for v in re.findall(pat, t, re.I):
                seen[key(v)].add(n)
        for v, ns in seen.items():
            if len(ns) > 1:
                fail.append(f'{label} partage par les entrees {sorted(ns)} : {v[:80]}')
                ok = False
    print(f'  [3] biblio      : {len(entries)} entrees -> {"OK" if ok else "ECHEC"}')
    return ok


def liens(body, refs):
    """Toute reference citee existe, toute reference existante est citee."""
    defined = {int(m.group(1)) for m in re.finditer(r'^(\d+)\. ', refs, re.M)}
    cited = {int(x) for m in re.finditer(r'\[(\d+(?:\s*,\s*\d+)*)\]', body) for x in m.group(1).split(',')}
    ok = True
    if cited - defined:
        fail.append(f'references citees mais absentes de la liste : {sorted(cited - defined)}')
        ok = False
    if defined - cited:
        fail.append(f'references presentes mais jamais citees : {sorted(defined - cited)}')
        ok = False
    print(f'  [+] appariement : {len(defined)} definies, {len(cited)} citees -> {"OK" if ok else "ECHEC"}')
    return ok


if __name__ == '__main__':
    body, refs = load()
    print(f'Controles de publication — {SRC}')
    results = [piege1(body), piege2(body), piege3(refs), liens(body, refs)]
    if fail:
        print('\nECHEC :')
        for f in fail:
            print('  -', f)
        sys.exit(1)
    print('\nTous les controles passent.')
