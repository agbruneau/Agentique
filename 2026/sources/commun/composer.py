"""Chaîne de composition commune aux livrables du corpus.

HTML structuré -> pandoc 3 (filtre.lua) -> Typst 0.15.1 (gabarit.typ) -> PDF, puis
contrôle que chaque mot du texte source se retrouve dans le PDF.

Un script de document appelle composer() avec :
  - fragments : {nom: html} ; chaque fragment devient <nom>.typ, à inclure par main ;
  - main : le fichier Typst principal (couverture, sommaire, #include des fragments) ;
  - extras : fichiers propres au document, copiés à côté (figures Typst, images…);
    les .typ sont importés dans chaque fragment ;
  - source_controle : le texte que le PDF doit contenir mot pour mot.

Polices : les PDF du dépôt sont composés sans les polices système (Segoe UI, si présente,
passerait devant Selawik et déplacerait la mise en page), avec TYPST_IGNORE_SYSTEM_FONTS=true
et TYPST_FONT_PATHS vers un dossier contenant Selawik, Inter (✓ ✗ du Cadre), Noto Color Emoji
(⚖ du Compendium) et, pour le Cadre, IBM Plex Sans (IBMPlexSans-Regular.ttf et
IBMPlexSans-SemiBold.ttf, libellés corrigés des schémas). Libertinus Serif, New Computer
Modern Math (𝑁, 𝑀 de la Veille) et DejaVu Sans Mono (⚠, ✎) sont fournies avec Typst.
"""
import collections, html, os, pathlib, re, shutil, subprocess, sys, tempfile, unicodedata
import pymupdf

COMMUN = pathlib.Path(__file__).resolve().parent
DOCUMENTS = COMMUN.parents[1] / 'documents'
MOIS = 'janvier février mars avril mai juin juillet août septembre octobre novembre décembre'.split()
NBSP = ' '
# Forme du nom de l'auteur sur la couverture, dans la fiche et les métadonnées des PDF.
AUTEUR = 'André-Guy Bruneau M.Sc. IT'


def date_fr(a, m, j):
    return f'{j}{"er" if j == 1 else ""} {MOIS[m - 1]} {a}'


# Actualisation de novembre 2026 : chaque livrable reçoit une annexe datée, rédigée en HTML
# dans son dossier (sources/<document>/actualisation-2026-11.html). Le corps n'est pas
# touché; l'annexe fait foi pour la date qu'elle porte.
ACTUALISATION = date_fr(2026, 11, 1)
FICHIER_ACTUALISATION = 'actualisation-2026-11.html'
# Relecture du 3 novembre 2026 (Veille, Revue) : corrections du corps faites à leur place
# et consignées dans un tableau de l'annexe d'actualisation, que la fiche nomme.
RELECTURE = date_fr(2026, 11, 3)


def tableau_relecture(corps, annexe, date=RELECTURE):
    """Numéro du tableau de l'annexe qui consigne la relecture : les tableaux de l'annexe
    continuent la suite du corps, numérotée par Typst dans l'ordre des légendes."""
    legendes = re.findall(r'<caption>([^<]*)', annexe)
    rang = [i for i, l in enumerate(legendes) if l.startswith(f'Errata relevés à la relecture du {date}')]
    assert len(rang) == 1, f'annexe : {len(rang)} tableau(x) de la relecture du {date}'
    return corps.count('<caption>') + rang[0] + 1


def actualisation(dossier):
    """(texte, références) de l'annexe d'actualisation du dossier : les références, à partir
    de leur intertitre « Références de l’actualisation », vont à part pour être composées
    en drapeau, comme celles du corps. Sans références, la seconde partie est vide."""
    s = (pathlib.Path(dossier) / FICHIER_ACTUALISATION).read_text(encoding='utf8')
    i = s.find('<h3>Références de l’actualisation</h3>')
    return (s, '') if i < 0 else (s[:i], s[i:])


def typographie(fragment):
    """Espaces insécables et apostrophe typographique, dans le texte seulement : ni dans
    les balises, ni dans <code> ou <pre>, dont le contenu reste littéral. Les adresses
    web du texte courant deviennent des liens (le gabarit ne les coupe qu'à leurs
    barres, points et traits)."""
    def texte(t):
        t = t.replace('&#39;', '’').replace('&#x27;', '’').replace("'", '’')
        t = re.sub(r' ([:;?!»])', NBSP + r'\1', t)
        t = re.sub(r'« ', '«' + NBSP, t)
        t = re.sub(r'§ ', '§' + NBSP, t)
        return t
    morceaux = re.split(r'(<pre\b.*?</pre>|<code\b.*?</code>)', fragment, flags=re.S)
    return ''.join(m if i % 2 else ''.join(p if j % 2 else texte(p) for j, p in enumerate(re.split(r'(<[^>]+>)', lier_url(m), flags=re.S)))
                   for i, m in enumerate(morceaux))


def lier_url(fragment):
    """Adresses web du texte -> <a href>, hors balises et hors liens existants."""
    def lier(m):
        u = m.group(0).rstrip('.,;:)»')
        return f'<a href="{u.replace("\u200b", "")}">{u}</a>' + m.group(0)[len(u):]
    morceaux = re.split(r'(<a\b.*?</a>|<[^>]+>)', fragment, flags=re.S)
    return ''.join(m if i % 2 else re.sub(r'https?://[^\s<>"]+', lier, m) for i, m in enumerate(morceaux))


def pandoc(fragment, dest, imports=()):
    subprocess.run(['pandoc', '-f', 'html', '-t', 'typst', '--wrap=none', '--lua-filter', str(COMMUN / 'filtre.lua'),
                    '-o', str(dest)], input=typographie(fragment).encode('utf8'), check=True)
    # pandoc centre ses tableaux (align(center)[...]) : les cellules en héritent
    typ = dest.read_text(encoding='utf8').replace('align(center)[#table(', '[#table(')
    entete = ''.join(f'#import "{i}": *\n' for i in ('gabarit.typ', *imports) if i.endswith('.typ'))
    dest.write_text(entete + typ, encoding='utf8')


def chaine_typst(t):
    return '"' + t.replace('\\', '\\\\').replace('"', '\\"') + '"'


def texte_html(fragment):
    # balises ôtées avant le décodage : « &lt;tool&gt; » reste un mot du texte
    return html.unescape(re.sub(r'<[^>]+>', ' ', fragment))


def mots(t):
    t = unicodedata.normalize('NFC', t).replace('’', "'").replace('\u200b', '')
    # l'extraction colle parfois deux cellules voisines (« 2026-10-31Relecture ») :
    # on coupe à chaque passage minuscule ou chiffre -> majuscule, des deux côtés
    t = re.sub(r'(?<=[a-zà-ÿ0-9])(?=[A-ZÀ-Ý])', ' ', t)
    return collections.Counter(re.findall(r"[^\W_]+", t.lower()))


def controler(source, pdf, marges=(70, 60)):
    """Chaque mot de la source doit figurer dans le PDF.

    Le PDF est lu mot à mot (deux cellules voisines ne se collent pas), hors en-têtes
    et pieds de page; une césure de Typst laisse un trait conditionnel (U+00AD) en fin
    de ligne, retiré pour recoller le mot. Quand la coupure tombe sur un saut de page
    au milieu d'un tableau, l'en-tête répété s'intercale : le mot compte alors si son
    début (avant le trait conditionnel) et sa fin se trouvent tous deux dans le PDF.
    Dans un tableau, l'ordre de lecture peut aussi placer après le trait conditionnel un
    mot de la cellule voisine, que le recollage absorbe (« cin­ » + « onze ») : ce mot
    compte alors pour lui-même. Les mots se comparent hors traits d'union. marges :
    hauteurs (pt) du haut et du bas de page écartées comme en-tête et pied.
    """
    doc = pymupdf.open(pdf)
    haut, bas = marges
    corps = lambda p: [w[4] for w in p.get_text('words') if w[1] > haut and w[3] < p.rect.height - bas]
    rendu = ' '.join(w for p in doc for w in corps(p))
    lu = mots(rendu.replace('­ ', ''))
    debuts = {m.group(1).lower() for m in re.finditer(r'(\w+)­', rendu)}
    manque = mots(source) - lu
    absorbes = mots(' '.join(m.group(1) for m in re.finditer(r'\S*­ (\S+)', rendu)))
    for m in list(manque):
        if any(m.startswith(d) and lu[m[len(d):]] for d in debuts) or absorbes[m] >= manque[m]:
            del manque[m]
    if manque:
        print('Mots de la source absents du PDF :', dict(manque.most_common(30)))
    return doc.page_count, sum(manque.values())


def composer(fragments, main, sortie, source_controle, extras=(), marges=(70, 60)):
    sortie = pathlib.Path(sortie)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        shutil.copy(COMMUN / 'gabarit.typ', tmp)
        for f in extras:
            shutil.copy(f, tmp)
        for nom, frag in fragments.items():
            pandoc(frag, tmp / f'{nom}.typ', [pathlib.Path(f).name for f in extras])
        (tmp / 'main.typ').write_text(main, encoding='utf8')
        brouillon = tmp / 'main.pdf'
        env = os.environ.copy()
        env['TYPST_IGNORE_SYSTEM_FONTS'] = 'true'
        chemins_polices = []
        polices_defaut = pathlib.Path(r'C:\fonts-cadre\gabarit')
        if polices_defaut.is_dir():
            chemins_polices.append(str(polices_defaut))
        if env.get('TYPST_FONT_PATHS'):
            chemins_polices.append(env['TYPST_FONT_PATHS'])
        if chemins_polices:
            env['TYPST_FONT_PATHS'] = os.pathsep.join(chemins_polices)
        subprocess.run(['typst', 'compile', '--root', str(tmp), str(tmp / 'main.typ'), str(brouillon)],
                       env=env, check=True)
        pages, manquants = controler(source_controle, brouillon, marges)
        if manquants:
            rejet = sortie.with_name(sortie.stem + ' (rejeté).pdf')
            shutil.copy(brouillon, rejet)
            sys.exit(f'{manquants} mot(s) manquant(s) : {sortie.name} non remplacé, brouillon dans {rejet}')
        shutil.copy(brouillon, sortie)
    print(f'{sortie} : {pages} pages, texte source intégralement présent')
    return pages
