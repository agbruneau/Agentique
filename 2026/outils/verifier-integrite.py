"""Contrôle d'intégrité éditoriale de Presentation.html entre deux versions.

Compare, dans <main>, la suite des nœuds de texte (espaces insécables compris; les blancs
du code source, espaces, tabulations et retours de ligne, se lisent comme une espace, ainsi
que le navigateur les rend), la suite des éléments sémantiques (main, section, header,
footer, h1-h3, p, em, b, a, figure, img) avec leurs attributs porteurs de sens (href, alt,
data-title, target, rel), et l'image de la figure 3 (empreinte SHA-256 de son attribut src).
Les classes et la mise en forme peuvent changer.

Usage : python outils/verifier-integrite.py [référence] [fichier]
  référence : révision git (défaut HEAD) ou chemin d'un fichier HTML
  fichier   : défaut Presentation.html
Code de sortie : 0 si identique, 1 sinon, 2 si la référence est introuvable.
"""
import hashlib, html.parser, pathlib, re, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parents[1]
SEMANTIQUE = {'main', 'section', 'header', 'footer', 'h1', 'h2', 'h3', 'p', 'em', 'b', 'a', 'figure', 'img'}
ATTRS = ('href', 'alt', 'data-title', 'target', 'rel')


class Lecteur(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.dans_main = 0
        self.textes, self.elements, self.images = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'main':
            self.dans_main += 1
        if not self.dans_main:
            return
        if tag in SEMANTIQUE:
            self.elements.append((tag, tuple((k, a[k]) for k in ATTRS if k in a)))
        if tag == 'img':
            self.images.append(hashlib.sha256(a.get('src', '').encode()).hexdigest())

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        if tag == 'main':
            self.dans_main -= 1

    def handle_data(self, data):
        # blancs ASCII seulement : une espace insécable (U+00A0, U+202F) est du texte
        texte = re.sub(r'[ \t\n\r\f]+', ' ', data).strip(' ')
        if self.dans_main and data.strip():
            self.textes.append(texte)


def lire(source):
    p = RACINE / source
    if p.is_file():
        t = p.read_text(encoding='utf8')
    else:
        r = subprocess.run(['git', 'show', f'{source}:Presentation.html'], cwd=RACINE, capture_output=True)
        if r.returncode:
            print(f'{source} : ni fichier, ni révision git qui porte Presentation.html '
                  f'({r.stderr.decode("utf8", "replace").strip()})', file=sys.stderr)
            sys.exit(2)
        t = r.stdout.decode('utf8')
    lecteur = Lecteur()
    lecteur.feed(t)
    return lecteur


ref = lire(sys.argv[1] if len(sys.argv) > 1 else 'HEAD')
cur = lire(sys.argv[2] if len(sys.argv) > 2 else 'Presentation.html')
ecarts = 0
for nom in ('textes', 'elements', 'images'):
    a, b = getattr(ref, nom), getattr(cur, nom)
    if a == b:
        print(f'{nom:9s} identiques ({len(a)})')
        continue
    ecarts += 1
    print(f'{nom:9s} DIFFÉRENTS ({len(a)} → {len(b)})')
    # premier écart; quand une suite prolonge l'autre, il tombe juste après la plus courte
    i = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
    x, y = (a[i] if i < len(a) else '(fin)'), (b[i] if i < len(b) else '(fin)')
    print(f'  premier écart n° {i} :\n    réf. {x!r}\n    act. {y!r}')
print('Intégrité conservée' if not ecarts else f'{ecarts} écart(s)')
sys.exit(1 if ecarts else 0)
