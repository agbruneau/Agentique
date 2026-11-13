"""Extraction d'un PDF balisé (tagged PDF) en HTML structuré pour composer.composer().

Le PDF est la source de vérité quand la source amont manque : ce module relit son
arborescence de structure (PyMuPDF, TEXT_COLLECT_STRUCTURE) page par page et la
recompose en h1-h6, p, ul/ol/li, table, pre/code, em/strong, a href, blockquote.

Principes :
  - identité d'un élément = chemin de ses « index » depuis la racine; un élément coupé
    par un saut de page porte le même chemin sur les deux pages et se recolle seul;
  - le texte d'un bloc (paragraphe, cellule, titre) est remis dans l'ordre visuel :
    une retouche directe du PDF range parfois ses lignes en fin d'arborescence, ou
    dans le dernier bloc de la page; une ligne isolée loin de son bloc rejoint le
    bloc qui la contient géométriquement (ou devient un paragraphe à sa place);
  - artefacts écartés par position (marges haute et basse), table des matières
    d'origine écartée (le gabarit en régénère une);
  - pages sans balisage (annexe fusionnée après coup) : repli géométrique (titres
    par taille de police, paragraphes par retrait ou retrait suspendu, tableaux par
    filet horizontal);
  - en-têtes de tableau répétés aux sauts de page absorbés (une seule fois dans le
    tableau), adresses coupées en fin de ligne recollées; controler_extraction() lit le
    PDF avec les mêmes règles.

Les particularités d'un document se règlent par les paramètres d'extraire() ou dans
son script; ce module reste générique.

Usage : python extraire.py source.pdf [sortie.html] [--niveaux 1:2,2:3]
"""
import collections, dataclasses, html, os, re, sys
import pymupdf

SHY, WJ = '\xad', '⁠'
# Rôles qui rangent du texte en ligne; tout autre rôle est un bloc.
EN_LIGNE = {'Span', 'Em', 'Strong', 'Code', 'Link', 'Reference', 'Quote', 'Formula', 'NonStruct',
            'Lbl', 'Annot', 'Sub', 'BibEntry', 'Ruby', 'Warichu', 'Private'}
CONTENEURS = {'Document', 'DocumentFragment', 'Part', 'Art', 'Sect', 'Div', 'BlockQuote', 'Figure',
              'NonStruct', 'Aside', 'L', 'LI', 'LBody', 'Table', 'THead', 'TBody', 'TFoot', 'TR',
              'TD', 'TH', 'Note', 'Index'}
ECARTES = {'TOC', 'TOCI', 'Artifact'}
# Conteneurs où un paragraphe peut s'insérer (ni liste, ni tableau, ni paragraphe).
SECTIONS = {'Document', 'DocumentFragment', 'Part', 'Art', 'Sect', 'Div', 'BlockQuote', 'Figure', 'Aside', 'Note',
            'NonStruct'}
TITRES_ECARTES = r'^(Table des matières|Sommaire|Contents|Table of contents)$'
STYLES_BALISES = {'Em': 'em', 'Strong': 'strong', 'Code': 'code'}
ORDRE_STYLES = ('a', 'strong', 'em', 'code', 'sup', 'sub')  # imbrication canonique, extérieur d'abord
# espaces insécables gardées (TEXT_PRESERVE_WHITESPACE), ligatures décomposées
STRUCTURE = pymupdf.TEXT_COLLECT_STRUCTURE | pymupdf.TEXT_MEDIABOX_CLIP | pymupdf.TEXT_PRESERVE_WHITESPACE
MONO = re.compile(r'Mono|Courier|Consol|Menlo|Code', re.I)
# Zones du PDF que l'extraction retire à dessein (copies d'un en-tête de tableau répété
# aux sauts de page), par fichier : controler_extraction() ne les lit pas.
ZONES_ABSORBEES = collections.defaultdict(list)


def cle_fichier(pdf):
    return os.path.normcase(os.path.realpath(str(pdf)))


# étiquette d'une entrée de liste ou de bibliographie, en tête de ligne
ETIQUETTE = r'\s*(\d+[.)]|\[\d+\]|[•◦▪‣–—*])\s'


def etiquette_suivante(prec, etiq):
    """Vrai si l'étiquette « etiq » suit « prec » dans une même liste (numéro + 1, ou même puce)."""
    n = lambda e: int(re.sub(r'\D', '', e)) if re.search(r'\d', e) else None
    if n(prec) is None or n(etiq) is None:
        return prec == etiq
    return n(etiq) == n(prec) + 1 and re.sub(r'\d', '', etiq) == re.sub(r'\d', '', prec)


def suite_url(fin, debut, lien_fin=None, lien_debut=None):
    """Vrai si « debut » (premier mot d'une ligne) prolonge l'adresse « fin » (dernier
    mot de la ligne précédente), coupée sans trait : Typst et Chrome coupent une URL
    n'importe où (« https://cloudsecurit / yalliance.org »). Deux mots du même lien se
    recollent quand leur réunion figure dans sa cible; hors lien, la suite doit avoir
    l'allure d'une URL (point, barre, trait, égal ou chiffre), sans majuscule initiale,
    et une adresse qui finit sur un point ne se prolonge que par une minuscule ou un
    chiffre (une phrase neuve prend la majuscule)."""
    a = fin.lstrip('([{«"\'')
    b = re.sub(r'[.,;:)\]}»"\']+$', '', debut)
    if not a or not b or a[-1:].isspace():
        return False
    if re.match(r'https?://', b):
        return False   # une adresse neuve
    if lien_fin or lien_debut:
        # un lien finit ou commence à la coupure : seule sa cible fait foi
        return lien_fin == lien_debut and len(a) >= 4 and (a + b) in lien_fin and re.search(r'[./]', a + b) is not None
    if not re.match(r'https?://\S', a) or re.search(r'[,;:)\]»"]$', a):
        return False
    if a.endswith('.'):
        return b[:1].islower() or b[:1].isdigit()
    return not (b[:1].isupper() or b[:1] in '«([—–' or not re.search(r'[./=\d-]', b))


@dataclasses.dataclass(eq=False)
class Run:
    """Un span de texte, avec sa place dans la page et dans l'arborescence."""
    texte: str
    page: int
    bbox: tuple
    taille: float
    police: str
    flags: int
    lien: str = None
    base: float = 0           # ligne de base
    bloc: tuple = None        # clé du bloc qui le porte
    en_ligne: tuple = ()      # clés des éléments en ligne entre le bloc et le span
    xs: tuple = ()            # abscisse de chaque caractère (pages lues en rawdict)


@dataclasses.dataclass
class Noeud:
    cle: tuple
    role: str
    parent: tuple = None
    enfants: list = dataclasses.field(default_factory=list)   # clés, dans l'ordre de lecture
    runs: list = dataclasses.field(default_factory=list)      # texte porté directement


def cadre(elements):
    """Rectangle englobant d'une liste de runs ou de rectangles (x0, y0, x1, y1)."""
    bs = [e.bbox if isinstance(e, Run) else e for e in elements]
    return min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)


def role(b):
    """Rôle d'un élément : le nom propre au document s'il est connu (Typst range Strong et
    Em sous le rôle standard Span), sinon le rôle standard."""
    raw, std = b.get('raw') or '', b.get('std') or ''
    if raw in EN_LIGNE or raw in CONTENEURS or raw in ECARTES or re.fullmatch(r'H\d?|P|Caption|Title', raw):
        return raw
    return std or raw or 'Span'


class Extracteur:
    """Paramètres (tous facultatifs) :
      niveaux : {niveau du PDF: niveau du gabarit}, ou fonction (niveau, texte) -> niveau;
                None écarte le titre (gabarit : 1 = partie, 2 = chapitre, 3-4 = sections);
      marges : (haut, bas) en points; un span entièrement dans ces bandes est un artefact
               (en-tête, pied, numéro de page, souvent rangés dans l'arborescence);
      artefacts : expressions régulières de spans à écarter où qu'ils soient;
      titres_ecartes : titres à écarter (table des matières d'origine);
      styles_balises : {rôle: balise HTML} pris dans l'arborescence; retirer 'Strong'
               quand le PDF balise en Strong du texte composé en romain;
      polices : déduit aussi em/strong/code de la police (italique, gras, chasse fixe);
      cesure_trait : trait ordinaire en fin de ligne : 'garder' (Typst, qui césure par
               trait conditionnel), 'couper', ou 'auto' (selon les formes du document);
      legende : début d'une légende de tableau, pour le repli des pages sans balisage;
      saut_rangee : excès d'interligne (pt) qui ouvre une rangée, même repli;
      pastilles : code en ligne composé dans une pastille à marge interne (Chrome) : la
               marge, lue comme une espace, est retirée entre le code et la ponctuation
               qui l'enserre (« ( typ ) » -> « (typ) », « l’ ETag » -> « l’ETag »);
      pages : pages à lire (toutes par défaut)."""

    def __init__(self, pdf, niveaux=None, marges=(60, 60), artefacts=(), titres_ecartes=TITRES_ECARTES,
                 styles_balises=STYLES_BALISES, polices=True, cesure_trait='garder',
                 legende=r'^(Tableau|Table|Figure)\s*\d', saut_rangee=0.8, pastilles=False, pages=None):
        self.saut_rangee = saut_rangee
        self.pastilles = pastilles
        self.doc = pymupdf.open(pdf)
        self.niveaux = niveaux or {}
        self.marges = marges
        self.artefacts = [re.compile(a) for a in artefacts]
        self.titres_ecartes = re.compile(titres_ecartes, re.I) if titres_ecartes else None
        self.styles_balises = styles_balises
        self.polices = polices
        self.cesure_trait = cesure_trait
        self.legende = re.compile(legende)
        self.pages = range(self.doc.page_count) if pages is None else pages
        self.noeuds = {}
        self.racines = []
        self.vocabulaire = collections.Counter()
        self.ecarts = []   # pages ou éléments traités par repli, pour le rapport
        self.etiquettes_nu = {}   # repli : paragraphe ouvert par une étiquette -> étiquette
        # en-têtes répétés retirés : zones (page, Rect) que le contrôle ne lit pas
        self.zones_absorbees = ZONES_ABSORBEES[cle_fichier(pdf)]
        self.zones_absorbees.clear()

    # ---- lecture de l'arborescence ------------------------------------------------

    def noeud(self, cle, r, parent):
        n = self.noeuds.get(cle)
        if n is None:
            n = self.noeuds[cle] = Noeud(cle, r, parent)
            if parent is None:
                self.racines.append(cle)
            else:
                self.noeuds[parent].enfants.append(cle)
        return n

    def artefact(self, page, bbox, texte):
        h = page.rect.height
        if bbox[3] <= self.marges[0] or bbox[1] >= h - self.marges[1]:
            return True
        return any(a.search(texte) for a in self.artefacts)

    def spans(self, page, bloc0, liens):
        """Spans d'un bloc de texte PyMuPDF (type 0), artefacts écartés."""
        lien = lambda b: next((u for r, u in liens if r.x0 <= (b[0] + b[2]) / 2 <= r.x1 and
                               r.y0 <= (b[1] + b[3]) / 2 <= r.y1), None)
        for ligne in bloc0['lines']:
            for s in ligne['spans']:
                t = (s['text'] if 'text' in s else ''.join(c['c'] for c in s['chars'])).replace(WJ, '')
                if not t or self.artefact(page, s['bbox'], t):
                    continue
                run = lambda t, bbox, uri, xs=(): Run(t, page.number, tuple(bbox), s['size'], s['font'], s['flags'],
                                                      uri, s['origin'][1], xs=tuple(xs))
                chars = [c for c in s.get('chars', ()) if c['c'] != WJ]
                if 'chars' in s and liens and any(pymupdf.Rect(r).intersects(s['bbox']) for r, _ in liens):
                    # caractères (rawdict) : un lien posé sur une partie du span seulement
                    # (page sans balisage, où un span couvre la ligne) n'en prend que sa part
                    morceaux = []
                    for c in chars:
                        u = lien(c['bbox'])
                        if morceaux and morceaux[-1][2] == u:
                            morceaux[-1][0] += c['c']
                            morceaux[-1][1] = (morceaux[-1][1][0], s['bbox'][1], c['bbox'][2], s['bbox'][3])
                            morceaux[-1][3].append(c['bbox'][0])
                        else:
                            morceaux.append([c['c'], (c['bbox'][0], s['bbox'][1], c['bbox'][2], s['bbox'][3]), u,
                                             [c['bbox'][0]]])
                    for t, bbox, u, xs in morceaux:
                        yield run(t, bbox, u, xs)
                    continue
                yield run(t, s['bbox'], lien(s['bbox']), [c['bbox'][0] for c in chars])

    def lire_page(self, page):
        liens = [(l['from'], l['uri']) for l in page.get_links() if l.get('kind') == pymupdf.LINK_URI]
        d = page.get_text('dict', flags=STRUCTURE)
        if not any(b['type'] == 2 for b in d['blocks']):
            return False

        def marcher(b, parent, chaine):
            if b['type'] == 2:
                cle = (parent or ()) + (b['index'],)
                n = self.noeud(cle, role(b), parent)
                for c in b.get('blocks', []):
                    marcher(c, cle, chaine + (cle,))
            elif b['type'] == 0:
                if parent is None:   # texte hors arborescence : paragraphe anonyme
                    racine = self.racines[-1] if self.racines else None
                    parent = self.noeud(('hors', page.number, len(self.noeuds)), 'P', racine).cle
                    chaine = (parent,)
                n = self.noeuds[parent]
                # du texte posé directement dans un conteneur forme un élément anonyme
                if n.role in CONTENEURS:
                    anon = n.enfants[-1] if n.enfants and n.enfants[-1][-1:] == ('anon',) else None
                    if anon is None:
                        anon = self.noeud(parent + (len(n.enfants), 'anon'), 'Span', parent).cle
                    n, chaine = self.noeuds[anon], chaine + (anon,)
                for r in self.spans(page, b, liens):
                    r.en_ligne = chaine
                    n.runs.append(r)

        for b in d['blocks']:
            marcher(b, None, ())
        return True

    # ---- en-têtes de tableau répétés ---------------------------------------------

    def absorber(self, page, runs):
        """Retire des runs (copies d'un en-tête répété) et note leur zone pour le contrôle."""
        for r in runs:
            self.zones_absorbees.append((page, pymupdf.Rect(r.bbox)))

    def rangees(self, cle):
        """Rangées (TR) d'un tableau, hors tableaux imbriqués."""
        n = self.noeuds[cle]
        if n.role == 'TR':
            yield cle
        elif n.role not in ECARTES:
            for c in n.enfants:
                if self.noeuds[c].role != 'Table':
                    yield from self.rangees(c)

    def absorber_entetes(self):
        """En-tête de tableau répété par Typst à chaque nouvelle page : hors arborescence
        (texte anonyme « hors »), il deviendrait un paragraphe après le tableau, ou des
        lignes que recaser() verserait dans les cellules. Est retiré le texte anonyme posé
        au-dessus de la première ligne du tableau sur une page suivante, sans autre texte
        entre les deux, et dont tous les mots sont ceux de la première rangée."""
        hors, autres = collections.defaultdict(list), collections.defaultdict(list)
        for k, n in self.noeuds.items():
            for r in n.runs:
                if r.texte.strip():
                    (hors if k[0] == 'hors' else autres)[r.page].append((k, r))
        total = 0
        for cle, n in list(self.noeuds.items()):
            if n.role != 'Table':
                continue
            trs = list(self.rangees(cle))
            if not trs:
                continue
            tete = self.runs_de(trs[0])
            # en-tête d'un seul tenant (sans blancs ni césures) : un fragment de mot coupé
            # autrement qu'à la première page (« pres- / crit ») s'y retrouve aussi
            tete_txt = re.sub(r'[\s\xad]', '', ''.join(r.texte for r in tete).lower())
            p0 = min((r.page for r in tete), default=None)
            corps = collections.defaultdict(list)
            for tr in trs:
                for r in self.runs_de(tr):
                    corps[r.page].append(r)
            siens = {id(r) for r in self.runs_de(cle)}
            for p, rs in corps.items():
                if p == p0 or not rs:
                    continue
                y = min(r.bbox[1] for r in rs)
                # plafond : bas du dernier texte étranger au tableau posé au-dessus de lui
                plafond = max((r.bbox[3] for _, r in autres.get(p, ()) if id(r) not in siens and r.bbox[3] <= y + 1),
                              default=0)
                retires = []
                for k, r in hors.get(p, ()):
                    mots_r = set(re.findall(r'\w+', r.texte.lower()))
                    if plafond - 1 <= r.bbox[1] < y and all(m in tete_txt for m in mots_r) \
                            and any(x is r for x in self.noeuds[k].runs):
                        self.noeuds[k].runs.remove(r)
                        retires.append(r)
                if retires:
                    self.absorber(p, retires)
                    total += len(retires)
                    # blancs de la même bande, sans objet une fois l'en-tête retiré
                    y0, y1 = min(r.bbox[1] for r in retires), max(r.bbox[3] for r in retires)
                    for k in {k for k, _ in hors.get(p, ())}:
                        n2 = self.noeuds[k]
                        n2.runs = [r for r in n2.runs if not (r.page == p and not r.texte.strip()
                                                              and y0 - 1 <= r.bbox[1] and r.bbox[3] <= y1 + 1)]
        if total:
            self.ecarts.append(f'{total} span(s) d\'en-tête de tableau répété absorbé(s)')

    # ---- classement bloc / en ligne -----------------------------------------------

    def classer(self):
        """Un nœud est un bloc feuille s'il ne contient aucun bloc : son texte (et celui de
        ses descendants en ligne) forme un paragraphe, un titre, une cellule…

        Deux retouches de l'arborescence d'abord :
          - un élément de bloc vide (appel de note Note > Lbl > Link sans texte, citation
            vide) est retiré : le paragraphe qui le contient passerait pour un conteneur de
            blocs et se romprait en un fragment par élément en ligne. Restent les éléments
            en ligne, les figures et les éléments de tableau (cellules vidées que recaser()
            peut remplir), et leurs ancêtres;
          - une étiquette de liste (Lbl) qui porte une phrase et non un repère (« • »,
            « 2. ») est le terme d'une liste à alinéa suspendu : elle devient un paragraphe
            de l'item, que liste() fond dans le paragraphe qui le suit (sans quoi elle
            serait écartée avec les repères)."""
        gardes = {'Figure', 'Table', 'THead', 'TBody', 'TFoot', 'TR', 'TD', 'TH'}
        vides = {}

        def vide(cle):
            if cle not in vides:
                n = self.noeuds[cle]
                vides[cle] = n.role not in gardes and not n.runs and all(vide(c) for c in n.enfants)
            return vides[cle]
        for n in list(self.noeuds.values()):
            n.enfants = [c for c in n.enfants if self.noeuds[c].role in EN_LIGNE or not vide(c)]
        self.termes_liste = set()
        for cle, n in self.noeuds.items():
            if n.role == 'Lbl' and len(re.sub(r'\s', '', ''.join(r.texte for r in self.runs_de(cle)))) > 6:
                n.role = 'P'
                self.termes_liste.add(cle)
        a_bloc = {}

        def contient_bloc(cle):
            if cle not in a_bloc:
                n = self.noeuds[cle]
                a_bloc[cle] = any((self.noeuds[c].role not in EN_LIGNE) or contient_bloc(c) for c in n.enfants
                                  if self.noeuds[c].role not in ECARTES)
            return a_bloc[cle]

        self.feuilles = set()

        def descendre(cle, feuille):
            n = self.noeuds[cle]
            if n.role in ECARTES:
                return
            if feuille is None and n.runs and contient_bloc(cle):
                # texte mêlé à des blocs (P qui contient une liste…) : il passe en tête,
                # dans un élément anonyme
                anon = cle + ('anon',)
                self.noeuds[anon] = Noeud(anon, 'Span', cle, runs=n.runs)
                n.enfants.insert(0, anon)
                n.runs = []
            if feuille is None and not contient_bloc(cle) and (n.role not in CONTENEURS or n.runs or n.enfants):
                feuille = cle
                self.feuilles.add(cle)
            for r in n.runs:
                r.bloc = feuille
                i = r.en_ligne.index(feuille) if feuille in r.en_ligne else -1
                r.en_ligne = tuple(r.en_ligne[i + 1:])
            for c in n.enfants:
                descendre(c, feuille)

        for r in self.racines:
            descendre(r, None)

    def runs_de(self, cle, exclure=()):
        n = self.noeuds[cle]
        out = list(n.runs)
        for c in n.enfants:
            if self.noeuds[c].role not in ECARTES and self.noeuds[c].role not in exclure:
                out += self.runs_de(c, exclure)
        return out

    # ---- retouches : lignes égarées -----------------------------------------------

    def recaser(self):
        """Une ligne retouchée peut être rangée dans un autre bloc que celui qu'elle
        prolonge visuellement (souvent le dernier de la page), ce qui creuse un trou dans
        le bloc d'origine. Par page, chaque bloc garde son plus gros amas vertical de
        lignes; les autres lignes, une à une et jusqu'à stabilité, restent si elles
        touchent leur bloc, rejoignent sinon le bloc de même corps qu'elles touchent; les
        dernières deviennent une cellule de la rangée qui les contient, ou un paragraphe à
        leur place.

        Avant cela, un amas de lignes en haut de page, rangé dans un bloc qui commence plus
        bas sans venir de la page précédente, rejoint le bloc qui terminait celle-ci quand
        la phrase s'y poursuit : sans quoi cet amas étranger, s'il est le plus fourni,
        resterait au bloc et en chasserait les lignes propres (l'ordre du texte
        s'inverserait). Après, les lignes de cellule rangées dans la colonne voisine
        rejoignent la cellule de leur colonne (recolonner)."""
        par_page = collections.defaultdict(lambda: collections.defaultdict(list))
        for f in self.feuilles:
            for r in self.runs_de(f):
                par_page[r.page][f].append(r)
        pages_de = collections.defaultdict(set)
        for p, blocs in par_page.items():
            for f in blocs:
                pages_de[f].add(p)
        # bloc qui finit chaque page (ligne la plus basse) sans se poursuivre à la suivante,
        # et la fin de son texte (sa ligne la plus basse, dernier span)
        dernier, fin = {}, {}
        for p, blocs in par_page.items():
            bas_page = max(((r.bbox[3], r.bbox[2], f, i) for f, rs in blocs.items() for i, r in enumerate(rs)
                            if r.texte.strip()), default=None)
            if bas_page and p + 1 not in pages_de[bas_page[2]] and \
                    self.noeuds[bas_page[2]].role in ('P', 'LBody', 'LI', 'Span'):
                dernier[p] = bas_page[2]
                fin[p] = blocs[bas_page[2]][bas_page[3]].texte.rstrip()
        # suite de phrase : la page précédente ne finit pas sur une ponctuation finale, ou
        # le haut de page commence par une minuscule (un encadré flottant en haut de page
        # ne se rattache pas)
        suite = lambda p, t: not re.search(r'[.!?:;»)\]]$', fin[p]) or t[:1].islower()
        for p, blocs in sorted(par_page.items()):
            etendue, tailles, egares = {}, {}, []
            haut_page = min((r.bbox[1] for rs in blocs.values() for r in rs if r.texte.strip()), default=0)
            for f, runs in blocs.items():
                amas, bas = [], None
                for r in sorted((r for r in runs if r.texte.strip()), key=lambda r: r.bbox[1]):
                    if amas and r.bbox[1] - bas < 1.5 * r.taille:
                        amas[-1].append(r)
                        bas = max(bas, r.bbox[3])
                    else:
                        amas.append([r])
                        bas = r.bbox[3]
                if not amas:
                    continue
                if len(amas) > 1 and p - 1 not in pages_de[f] and amas[0][0].bbox[1] <= haut_page + 1 \
                        and dernier.get(p - 1) not in (None, f) \
                        and suite(p - 1, self.texte_runs(self.lignes_visuelles(amas[0])[0])):
                    hote = dernier[p - 1]
                    for l in self.lignes_visuelles(amas[0]):
                        self.ecarts.append(f'p. {p + 1} : haut de page rendu au bloc de la page précédente '
                                           f'« {self.texte_runs(l)[:50]} »')
                        for r in l:
                            self.noeuds[self.proprietaire(r)].runs.remove(r)
                            r.bloc = hote
                            self.noeuds[hote].runs.append(r)
                    amas = amas[1:]
                principal = max(amas, key=lambda a: sum(len(r.texte.strip()) for r in a))
                etendue[f] = cadre(principal)
                tailles[f] = {round(r.taille, 1) for r in principal}
                for a in amas:
                    if a is not principal:
                        egares += [(f, l) for l in self.lignes_visuelles(a)]

            def touche(l, g):
                x0, y0, x1, y1 = cadre(l)
                gx0, gy0, gx1, gy1 = etendue[g]
                h = max(r.taille for r in l)
                ecart = max(gy0 - y1, y0 - gy1, 0)
                return ecart < 0.6 * h and x0 < gx1 and x1 > gx0 and any(
                    abs(r.taille - t) <= 0.5 for r in l for t in tailles[g])

            def deplacer(l, f, hote):
                self.ecarts.append(f'p. {p + 1} : ligne déplacée « {self.texte_runs(l)[:60]} »')
                y0, y1 = cadre(l)[1], cadre(l)[3]
                # les blancs de la même ligne suivent le texte qu'ils séparent
                blancs = [r for r in blocs[f] if not r.texte.strip() and y0 - 1 <= r.bbox[1] and r.bbox[3] <= y1 + 1]
                for r in l + blancs:
                    self.noeuds[self.proprietaire(r)].runs.remove(r)
                    r.bloc = hote
                    self.noeuds[hote].runs.append(r)

            grandir = lambda g, l: etendue.__setitem__(g, cadre([etendue[g], cadre(l)]))
            change = True
            while change and egares:
                change = False
                for f, l in list(egares):
                    hote = f if touche(l, f) else next((g for g in etendue if g != f and touche(l, g)), None)
                    if hote is None:
                        continue
                    if hote != f:
                        deplacer(l, f, hote)
                    grandir(hote, l)
                    egares.remove((f, l))
                    change = True
            for f, l in egares:
                x0, y0, x1, y1 = cadre(l)
                hote = next((g for g in etendue if 'retouche' in g and touche(l, g)), None)
                if hote is None:
                    hote = self.inserer_cellule(f, p, l) or self.inserer_paragraphe(f, p, y0)
                    etendue[hote], tailles[hote] = cadre(l), {round(r.taille, 1) for r in l}
                deplacer(l, f, hote)
                grandir(hote, l)
        self.hors_colonne = []
        for cle in [k for k, n in self.noeuds.items() if n.role == 'Table']:
            # deux passes : une rangée ne se complète qu'une fois ses lignes recasées
            for _ in range(2):
                self.completer_rangees(cle)
                self.recolonner(cle)
        for p, n in sorted(collections.Counter(p + 1 for p, _ in self.hors_colonne).items()):
            self.ecarts.append(f'p. {p} : {n} span(s) de tableau rendu(s) à la cellule de leur colonne')

    def completer_rangees(self, table):
        """Rangée balisée sans ses cellules vides (coin d'un tableau à double entrée,
        cellule fusionnée verticalement) : pandoc la décalerait à gauche. Chaque cellule
        présente va à la colonne qui contient son centre; une cellule vide est rétablie
        aux autres. Début de chaque colonne : la médiane des débuts de ses cellules dans
        les rangées complètes (colonnes centrées comprises)."""
        cellules = lambda tr: [c for c in self.noeuds[tr].enfants if self.noeuds[c].role in ('TD', 'TH')]
        texte = lambda c: [r for r in self.runs_de(c) if r.texte.strip()]
        trs = list(self.rangees(table))
        n = max((len(cellules(t)) for t in trs), default=0)
        debuts = collections.defaultdict(list)
        for t in trs:
            if len(cellules(t)) == n:
                for j, c in enumerate(cellules(t)):
                    if texte(c):
                        debuts[j].append(min(r.bbox[0] for r in texte(c)))
        if len(debuts) != n:
            return
        d = [sorted(debuts[j])[len(debuts[j]) // 2] for j in range(n)]
        if d != sorted(set(d)):
            return
        for t in trs:
            cs = cellules(t)
            if len(cs) >= n or not all(texte(c) for c in cs):
                continue
            centre = lambda c: (min(r.bbox[0] for r in texte(c)) + max(r.bbox[2] for r in texte(c))) / 2
            place = {max([i for i, x in enumerate(d) if x - 3 <= centre(c)] or [0]): c for c in cs}
            if len(place) != len(cs) or [place[k] for k in sorted(place)] != cs:
                continue
            role = self.noeuds[cs[0]].role
            rangee = []
            for k in range(n):
                if k not in place:
                    place[k] = t + (len(self.noeuds), 'coin')
                    self.noeuds[place[k]] = Noeud(place[k], role, t)
                rangee.append(place[k])
            self.noeuds[t].enfants = [c for c in self.noeuds[t].enfants if c not in cs] + rangee
            p = min(r.page for c in cs for r in self.runs_de(c)) + 1
            self.ecarts.append(f'p. {p} : rangée de {len(cs)} cellule(s) sur {n}, cellule(s) vide(s) rétablie(s)')

    def colonnes(self, table):
        """Rangées (cellules) d'un tableau, et début (x, pt) de chaque colonne, le même à
        chaque page : celui des cellules de la première rangée (l'en-tête) si aucune n'est
        vide, sinon None. Une estimation par la majorité des rangées échoue quand la
        rangée mal balisée l'emporte en nombre."""
        trs = [[c for c in self.noeuds[tr].enfants if self.noeuds[c].role in ('TD', 'TH')]
               for tr in self.rangees(table)]
        if not trs:
            return trs, None
        debuts = [min([r.bbox[0] for r in self.runs_de(c) if r.texte.strip()] or [None]) for c in trs[0]]
        return trs, None if None in debuts else debuts

    def recolonner(self, cle):
        """Une retouche range parfois des lignes ou des spans de cellule dans la cellule
        voisine de la même rangée, et la lecture visuelle les entrelace (« sa période
        traverse deux de commentaires échéances »). Dans une rangée complète, un span qui
        commence au-delà du début d'une colonne suivante, ou exactement au début d'une
        colonne précédente (débuts : ceux de l'en-tête, colonnes()), rejoint la cellule
        de cette colonne; un span collé au précédent (virgule après un code qui déborde)
        suit son sort. Restent où ils sont : un span qui commence un peu à gauche de sa
        colonne (nombre aligné à droite, en-tête centré), et, sous le reste de la rangée,
        un segment qui enjambe une colonne (note posée sous le tableau)."""
        trs, debuts = self.colonnes(cle)
        if not debuts or len(debuts) < 2 or debuts != sorted(set(debuts)):
            return
        for tr, cells in zip(self.rangees(cle), trs):
            # cellule ajoutée pour une ligne égarée (inserer_cellule) : sa ligne rejoint,
            # elle aussi, la cellule de sa colonne
            propres = [c for c in cells if c[-1] != 'retouche']
            if len(propres) != len(debuts):
                continue
            for c in cells:
                j = propres.index(c) if c in propres else None
                for l in self.lignes_visuelles(self.runs_de(c)):
                    # segments de spans contigus : un segment qui enjambe le début d'une
                    # colonne n'est pas une ligne de cellule (note posée sous le tableau,
                    # sur toute la justification)
                    segments, seg = {}, []
                    for r in l:
                        if seg and r.bbox[0] - seg[-1].bbox[2] > 0.8 * r.taille:
                            seg = []
                        seg.append(r)
                        segments[id(r)] = seg
                    enjambe = lambda seg: any(seg[0].bbox[0] < d - 3 and max(x.bbox[2] for x in seg) > d + 3
                                              for d in debuts[1:])
                    # span précédent de la ligne et sa colonne : un span qui lui est collé
                    # le suit (une virgule après un code qui déborde de sa colonne reste
                    # dans sa cellule)
                    prec = None
                    for r in l:
                        k = max([i for i, d in enumerate(debuts) if d - 3 <= r.bbox[0]] or [0])
                        colle = prec and r.bbox[0] - prec[0].bbox[2] < 0.5 * r.taille
                        if colle:
                            k = prec[1]
                        if propres[k] == c or (j is not None and k < j and abs(r.bbox[0] - debuts[k]) >= 3
                                               and not colle):
                            prec = (r, propres.index(c) if c in propres else k)
                            continue
                        # sous le reste de la rangée, un segment qui enjambe une colonne
                        # reste où il est
                        bas = max((x.bbox[3] for cc in cells if cc != c for x in self.runs_de(cc)
                                   if x.page == r.page and x.texte.strip()), default=0)
                        if r.bbox[1] >= bas and enjambe(segments[id(r)]):
                            prec = (r, propres.index(c) if c in propres else k)
                            continue
                        self.noeuds[self.proprietaire(r)].runs.remove(r)
                        r.bloc = propres[k]
                        self.noeuds[propres[k]].runs.append(r)
                        self.feuilles.add(propres[k])
                        if r.texte.strip():
                            self.hors_colonne.append((r.page, r))
                        prec = (r, k)
            n = self.noeuds[tr]
            n.enfants = [c for c in n.enfants if c[-1] != 'retouche' or self.runs_de(c)]

    def texte_runs(self, runs):
        return re.sub(r'\s+', ' ', ' '.join(r.texte for r in runs)).strip()

    def inserer_cellule(self, voisin, page, ligne):
        """Ligne égarée à hauteur d'une rangée de tableau, hors de toute cellule : la
        retouche a remplacé le contenu d'une cellule vide; une cellule neuve la reçoit, à
        sa place dans l'ordre des colonnes."""
        x0, y0, x1, y1 = cadre(ligne)
        for cle, n in self.noeuds.items():
            if n.role != 'TR':
                continue
            rs = [r for r in self.runs_de(cle) if r.page == page and r not in ligne]
            if not rs:
                continue
            _, ry0, _, ry1 = cadre(rs)
            if not ry0 - 1 <= (y0 + y1) / 2 <= ry1 + 1:
                continue
            cellules = [c for c in n.enfants if self.noeuds[c].role in ('TD', 'TH')]
            vides = [c for c in cellules if not self.runs_de(c)]
            pos = next((i for i, c in enumerate(cellules)
                        if any(r.page == page for r in self.runs_de(c)) and
                        min(r.bbox[0] for r in self.runs_de(c) if r.page == page) > x0), len(cellules))
            if vides:   # cellule balisée mais vidée : la plus proche de la colonne visée
                c = min(vides, key=lambda c: abs(cellules.index(c) - pos))
                self.feuilles.add(c)
                return c
            nouveau = cle + (len(self.noeuds), 'retouche')
            self.noeuds[nouveau] = Noeud(nouveau, 'TD', cle)
            n.enfants.insert(n.enfants.index(cellules[pos]) if pos < len(cellules) else len(n.enfants), nouveau)
            self.feuilles.add(nouveau)
            return nouveau
        return None

    def proprietaire(self, run):
        for k in (*reversed(run.en_ligne), run.bloc):
            if any(x is run for x in self.noeuds[k].runs):
                return k
        raise KeyError(run.texte)

    def inserer_paragraphe(self, voisin, page, y):
        """Nouveau paragraphe dans la section qui contient « voisin », avant le premier
        élément qui commence après lui, page puis hauteur (sinon en fin de section). Quand
        tout le document est une seule section (Typst : une racine Document), une ligne
        égarée en bas de page partirait sinon en fin de volume."""
        cle = voisin
        while self.noeuds[cle].parent is not None and self.noeuds[self.noeuds[cle].parent].role not in SECTIONS:
            cle = self.noeuds[cle].parent
        parent = self.noeuds[cle].parent or cle
        nouveau = parent + (len(self.noeuds), 'retouche')
        self.noeuds[nouveau] = Noeud(nouveau, 'P', parent)
        freres = self.noeuds[parent].enfants
        # début de chaque frère, mis en cache (les lignes déplacées ne le changent guère)
        cache = self.__dict__.setdefault('_debuts', {})

        def debut(c):
            if c not in cache:
                cache[c] = min(((r.page, r.bbox[1]) for r in self.runs_de(c)), default=None)
            return cache[c]
        pos = next((i for i, c in enumerate(freres) if (d := debut(c)) is not None and d > (page, y)), len(freres))
        freres.insert(pos, nouveau)
        self.feuilles.add(nouveau)
        return nouveau

    # ---- pages sans balisage : repli géométrique -----------------------------------

    def lire_page_nue(self, page, taille_corps, tailles_titres):
        """Recompose une page sans arborescence : titres (gras, plus grands que le corps),
        paragraphes (retrait de première ligne, blanc vertical), tableaux (filet horizontal
        sous la ligne d'en-tête, texte plus petit que le corps, légende au-dessus)."""
        self.ecarts.append(f'p. {page.number + 1} : sans balisage, repli géométrique')
        liens = [(l['from'], l['uri']) for l in page.get_links() if l.get('kind') == pymupdf.LINK_URI]
        lignes = []
        # rawdict : caractère par caractère, pour borner les liens (spans)
        for b in page.get_text('rawdict', flags=STRUCTURE & ~pymupdf.TEXT_COLLECT_STRUCTURE)['blocks']:
            for l in b.get('lines', []):
                # une ligne PyMuPDF peut enjamber deux cellules : coupe aux grands blancs
                seg = []
                for r in self.spans(page, {'lines': [l]}, liens):
                    if seg and r.bbox[0] - seg[-1].bbox[2] > r.taille:
                        lignes.append(seg)
                        seg = []
                    seg.append(r)
                if seg:
                    lignes.append(seg)
        lignes.sort(key=lambda s: (round(s[0].bbox[1]), s[0].bbox[0]))
        if self.racines:
            racine = self.racines[-1]
        else:
            racine = self.noeud(('nu',), 'Document', None).cle
        haut = lambda s: s[0].bbox[1]
        petit = lambda s: max(r.taille for r in s) < 0.92 * taille_corps
        texte = lambda s: ''.join(r.texte for r in s).strip()
        gauche = min((s[0].bbox[0] for s in lignes if not petit(s)), default=0)
        filets = sorted(it['rect'].y0 for it in page.get_drawings()
                        if it['rect'].height < 2 and it['rect'].width > 0.3 * page.rect.width)

        # tableaux : chaque filet sépare l'en-tête (au-dessus) du corps (en dessous)
        tableaux, pris = [], set()
        for fy in filets:
            dessus = []
            for i in range(len(lignes) - 1, -1, -1):   # remonte depuis le filet
                s = lignes[i]
                if s[0].bbox[3] > fy + 1 or i in pris:
                    continue
                if not petit(s):
                    break
                dessus.insert(0, i)
            groupes = []
            for i in dessus:
                if groupes and haut(lignes[i]) - haut(lignes[groupes[-1][-1]]) <= 1.5 * lignes[i][0].taille:
                    groupes[-1].append(i)
                else:
                    groupes.append([i])
            if not groupes:
                continue
            entete = groupes[-1]
            debut_leg = next((g for g in range(len(groupes) - 1)
                              if self.legende.search(texte(lignes[groupes[g][0]]))), None)
            legende = [i for g in groupes[debut_leg:-1] for i in g] if debut_leg is not None else []
            corps = []
            for i, s in enumerate(lignes):
                if haut(s) >= fy - 1 and i not in pris:
                    if not petit(s):
                        break
                    corps.append(i)
            tableaux.append((legende, entete, corps))
            pris |= set(legende) | set(entete) | set(corps)

        elements = [(haut(lignes[e[1][0]]), 'table', e) for e in tableaux]
        elements += [(haut(s), 'ligne', i) for i, s in enumerate(lignes) if i not in pris]
        elements.sort(key=lambda e: e[0])

        precedent = getattr(self, 'dernier_nu', None)   # dernier élément de la page nue précédente
        if precedent and precedent[0] != page.number - 1:
            precedent = None
        der = None   # dernière ligne posée dans le paragraphe ou le titre ouvert
        for _, genre, contenu in elements:
            if genre == 'table':
                cle = self.tableau_nu(racine, lignes, *contenu, precedent=precedent)
                precedent, der = (page.number, cle, 'table'), None
                continue
            s = lignes[contenu]
            gras = all(r.flags & 16 for r in s if r.texte.strip())
            taille = round(max(r.taille for r in s), 1)
            if gras and taille > 1.05 * taille_corps:
                if precedent and precedent[2] == 'titre' and der and haut(s) - der[0].bbox[3] < 0.5 * taille:
                    cle = precedent[1]   # titre sur plusieurs lignes
                else:
                    connus = sorted(set(tailles_titres) | {taille}, reverse=True)
                    niveau = tailles_titres.get(taille) or 1 + connus.index(taille)
                    cle = self.noeud(racine + (len(self.noeuds), 'nu'), f'H{niveau}', racine).cle
                self.noeuds[cle].runs += s
                precedent, der = (page.number, cle, 'titre'), s
                continue
            retrait = s[0].bbox[0] > gauche + 0.5 * taille
            # interligne mesuré de ligne de base à ligne de base : un fragment de code, plus
            # petit, fausserait l'écart entre boîtes
            serre = der is None or max(r.base for r in s) - max(r.base for r in der) < 1.6 * taille_corps
            # entrée à étiquette (« 346. », « [12] », « • ») : ses lignes suivantes, en
            # retrait suspendu, la prolongent; l'étiquette suivante (numéro + 1, ou même
            # puce) en ouvre une autre, même en tête de page, où l'interligne ne se mesure pas
            etiq = re.match(ETIQUETTE, texte(s))
            etiq_prec = self.etiquettes_nu.get(precedent[1]) if precedent and precedent[2] == 'p' else None
            entree = not retrait and etiq and etiq_prec is not None and                 etiquette_suivante(etiq_prec[0], etiq.group(1))
            # retrait suspendu : la ligne commence là où le texte suit l'étiquette
            suspendu = retrait and etiq_prec is not None and abs(s[0].bbox[0] - etiq_prec[1]) < 2
            suite = precedent and precedent[2] == 'p' and not entree and serre and (not retrait or suspendu)
            if suite:
                cle = precedent[1]   # même paragraphe, ou suite de celui de la page précédente
            else:
                cle = self.noeud(racine + (len(self.noeuds), 'nu'), 'P', racine).cle
                if etiq and not retrait:
                    # abscisse du texte après l'étiquette (caractères lus en rawdict)
                    xs = [x for r in s for x in r.xs]
                    brut = ''.join(r.texte for r in s)
                    i = len(brut) - len(brut.lstrip()) + etiq.end() - (len(texte(s)) - len(texte(s).lstrip()))
                    while i < len(brut) and brut[i].isspace():
                        i += 1
                    if len(xs) == len(brut) and i < len(xs):
                        self.etiquettes_nu[cle] = (etiq.group(1), xs[i])
            self.noeuds[cle].runs += s
            precedent, der = (page.number, cle, 'p'), s
        self.dernier_nu = precedent

    def tableau_nu(self, racine, lignes, legende, entete, corps, precedent):
        cols = []
        for i in entete:
            x = lignes[i][0].bbox[0]
            if not any(abs(x - c) < 3 for c in cols):
                cols.append(x)
        cols.sort()
        colonne = lambda s: max([j for j, c in enumerate(cols) if c <= s[0].bbox[0] + 3] or [0])
        titres = [''.join(r.texte for i in entete for r in lignes[i] if colonne(lignes[i]) == j).strip()
                  for j in range(len(cols))]
        # rangées : dans une cellule, les lignes se suivent à l'interligne minimal; une
        # rangée neuve l'excède des marges internes des cellules (≈ 1 pt de plus dans le
        # gabarit des annexes Typst, où un fragment de code abaisse sa ligne de ≈ 0,5 pt;
        # lignes de base regroupées à 1,5 pt près pour la même raison)
        bases = []
        for b in sorted(lignes[i][0].base for i in corps):
            if not bases or b - bases[-1] > 1.5:
                bases.append(b)
        pas = min((b - a for a, b in zip(bases, bases[1:])), default=0)
        debuts = [b for k, b in enumerate(bases) if k == 0 or b - bases[k - 1] > pas + self.saut_rangee]
        rangee = lambda s: max(j for j, b in enumerate(debuts) if b <= s[0].base + 1.5)
        suite = precedent and precedent[2] == 'table' and self.titres_nu(precedent[1]) == titres
        if suite:
            table = precedent[1]
            tbody = self.noeuds[table].enfants[-1]
            # en-tête répété à la page neuve : le tableau garde celui de sa première page
            for i in entete:
                self.absorber(lignes[i][0].page, lignes[i])
        else:
            table = self.noeud(racine + (len(self.noeuds), 'nu'), 'Table', racine).cle
            if legende:
                cap = self.noeud(table + ('legende',), 'Caption', table).cle
                for i in legende:
                    self.noeuds[cap].runs += lignes[i]
            tr = self.noeud(table + ('thead', 0), 'TR', self.noeud(table + ('thead',), 'THead', table).cle).cle
            for j in range(len(cols)):
                th = self.noeud(tr + (j,), 'TH', tr).cle
                for i in entete:
                    if colonne(lignes[i]) == j:
                        self.noeuds[th].runs += lignes[i]
            tbody = self.noeud(table + ('tbody',), 'TBody', table).cle
        n0 = len(self.noeuds[tbody].enfants)
        coupee = suite and corps and not any(colonne(lignes[i]) == 0 and rangee(lignes[i]) == 0 for i in corps)
        trs = {}
        for i in corps:
            s = lignes[i]
            k, j = rangee(s), colonne(s)
            if k == 0 and coupee:
                tr = self.noeuds[tbody].enfants[n0 - 1]   # rangée coupée par le saut de page
            else:
                if k not in trs:
                    trs[k] = self.noeud(tbody + (len(self.noeuds),), 'TR', tbody).cle
                    for jj in range(len(cols)):
                        self.noeud(trs[k] + (jj,), 'TD', trs[k])
                tr = trs[k]
            self.noeuds[self.noeuds[tr].enfants[j]].runs += s
        return table

    def titres_nu(self, table):
        thead = next((c for c in self.noeuds[table].enfants if self.noeuds[c].role == 'THead'), None)
        if thead is None:
            return None
        tr = self.noeuds[thead].enfants[0]
        return [''.join(r.texte for r in self.noeuds[c].runs).strip() for c in self.noeuds[tr].enfants]

    # ---- texte d'un bloc -------------------------------------------------------------

    def lignes_visuelles(self, runs):
        """Runs d'un bloc rangés en lignes visuelles (page, haut en bas, gauche à droite)."""
        out = []
        for p in sorted({r.page for r in runs}):
            lignes = []
            for r in sorted((r for r in runs if r.page == p), key=lambda r: r.bbox[1]):
                h = r.bbox[3] - r.bbox[1]
                for l in lignes:
                    recouvre = min(l[1], r.bbox[3]) - max(l[0], r.bbox[1])
                    if recouvre > 0.5 * min(h, l[1] - l[0]):
                        l[2].append(r)
                        l[0], l[1] = min(l[0], r.bbox[1]), max(l[1], r.bbox[3])
                        break
                else:
                    lignes.append([r.bbox[1], r.bbox[3], [r]])
            for l in sorted(lignes, key=lambda l: l[0]):
                out.append(sorted(l[2], key=lambda r: r.bbox[0]))
        return out

    def styles(self, r, titre):
        st = set()
        for k in r.en_ligne:
            s = self.styles_balises.get(self.noeuds[k].role)
            if s:
                st.add(s)
        if self.polices and not titre:
            if r.flags & 2:
                st.add('em')
            if r.flags & 16:
                st.add('strong')
            if MONO.search(r.police):
                st.add('code')
        if r.lien:
            st.add(('a', r.lien))
        return st

    def morceaux(self, cle, titre=False, exclure=()):
        """Texte d'un bloc en morceaux [texte, styles], lignes recollées : trait
        conditionnel retiré, trait ordinaire gardé ou non selon cesure_trait."""
        out = []
        for l in self.lignes_visuelles(self.runs_de(cle, exclure)):
            ligne, prec = [], None
            # corps et ligne de base dominants de la ligne : un span plus petit et décalé
            # est un exposant (ordinal, appel de note) ou un indice
            poids = collections.Counter()
            for r in l:
                poids[(round(r.taille, 1), round(r.base, 1))] += len(r.texte.strip())
            t0, b0 = max(poids, key=poids.get) if poids else (0, 0)
            for r in l:
                t = r.texte
                if prec and r.bbox[0] - prec.bbox[2] > 0.2 * r.taille and not ligne[-1][0][-1:].isspace() \
                        and not t[:1].isspace():
                    t = ' ' + t
                st = self.styles(r, titre)
                if r.taille < 0.9 * t0 and r.texte.strip():
                    if b0 - r.base > 0.15 * t0:
                        st.add('sup')
                    elif r.base - b0 > 0.1 * t0:
                        st.add('sub')
                ligne.append([t, st])
                prec = r
            while out and not out[-1][0].strip():
                out.pop()
            while ligne and not ligne[0][0].strip():
                ligne.pop(0)
            if not ligne:
                continue
            if out:
                fin, debut = out[-1][0].rstrip(), ligne[0][0].lstrip()
                if fin.endswith(SHY):
                    out[-1][0] = fin[:-1]
                elif self.adresse_coupee(out, ligne):
                    out[-1][0] = fin
                elif fin.endswith('-') and debut[:1].isalpha() and self.couper(fin, debut):
                    out[-1][0] = fin[:-1]
                elif fin.endswith(('-', '/')) and debut[:1].isalnum():
                    out[-1][0] = fin
                else:
                    out[-1][0] = fin + ' '
                ligne[0][0] = debut
            out += ligne
        for m in out:
            m[0] = m[0].replace(SHY, '')
        return out

    def adresse_coupee(self, out, ligne):
        """Fin de « out » et début de « ligne » : une adresse coupée en fin de ligne, à
        recoller sans espace (suite_url, la règle même du contrôle de complétude)."""
        lien = lambda st: next((s[1] for s in st if isinstance(s, tuple)), None)
        fin, lien_fin = '', lien(out[-1][1])
        for i, (t, _) in enumerate(reversed(out)):
            t = t.rstrip() if i == 0 else t
            m = re.search(r'\S*$', t).group(0)
            fin = m + fin
            if len(m) < len(t):
                break
        debut, lien_debut = '', lien(ligne[0][1])
        for i, (t, _) in enumerate(ligne):
            t = t.lstrip() if i == 0 else t
            m = re.match(r'\S*', t).group(0)
            debut += m
            if len(m) < len(t):
                break
        return suite_url(fin.replace(SHY, ''), debut.replace(SHY, ''), lien_fin, lien_debut)

    def couper(self, fin, debut):
        """Trait en fin de ligne : césure à retirer (vrai) ou trait d'union à garder."""
        if self.cesure_trait == 'garder':
            return False
        if self.cesure_trait == 'couper':
            return True
        a = re.search(r'(\w+)-$', fin)
        b = re.match(r'\w+', debut)
        if not (a and b):
            return False
        a, b = a.group(1).lower(), b.group(0).lower()
        return self.vocabulaire[a + b] > self.vocabulaire[f'{a}-{b}']

    def en_ligne_html(self, cle, titre=False, exclure=()):
        out, pile = [], []

        def fermer():
            s = pile.pop()
            out.append(f'</{s if isinstance(s, str) else "a"}>')
        for texte, st in self.morceaux(cle, titre, exclure):
            voulu = sorted(st, key=lambda s: (ORDRE_STYLES.index(s if isinstance(s, str) else 'a'), str(s)))
            while pile and pile != voulu[:len(pile)]:
                fermer()
            # les blancs de tête restent hors des balises qu'on ouvre
            tete = re.match(r'\s*', texte).group(0)
            if tete and len(pile) < len(voulu):
                out.append(tete)
                texte = texte[len(tete):]
            for s in voulu[len(pile):]:
                out.append(f'<a href="{html.escape(s[1])}">' if isinstance(s, tuple) else f'<{s}>')
                pile.append(s)
            out.append(html.escape(texte, quote=False))
        while pile:
            fermer()
        h = ''.join(out)
        for _ in range(3):   # blancs de queue sortis des balises
            h = re.sub(r'(\s+)(</(?:em|strong|code|a|sup|sub)>)', r'\2\1', h)
        h = re.sub(r'<(em|strong|code|sup|sub)>(\s*)</\1>', r'\2', h)
        h = re.sub(r'[ \t\r\n]+', ' ', h).strip(' ')   # espaces insécables gardées
        if self.pastilles:
            h = re.sub(r'([(’]) (<code>)', r'\1\2', h)
            h = re.sub(r'(</code>) ([),.;])', r'\1\2', h)
        return h

    def texte(self, cle):
        return ''.join(t for t, _ in self.morceaux(cle)).strip()

    # ---- rendu HTML -----------------------------------------------------------------

    def niveau(self, r, texte):
        n = int(r[1:]) if r[1:].isdigit() else 1
        return self.niveaux(n, texte) if callable(self.niveaux) else self.niveaux.get(n, n)

    def contient(self, cle, roles):
        n = self.noeuds[cle]
        return n.role in roles or any(self.contient(c, roles) for c in n.enfants if self.noeuds[c].role not in ECARTES)

    def rendre(self, cle, legende=None):
        n = self.noeuds[cle]
        r = n.role
        if r in ECARTES or (not self.runs_de(cle) and r not in ('TD', 'TH')):
            return ''
        if cle in self.feuilles:
            if re.fullmatch(r'H\d?', r):
                t = self.texte(cle)
                if self.titres_ecartes and self.titres_ecartes.search(t):
                    return ''
                lv = self.niveau(r, t)
                return '' if lv is None else f'<h{lv}>{self.en_ligne_html(cle, titre=True)}</h{lv}>'
            if r in ('TD', 'TH', 'LBody', 'LI'):
                return self.en_ligne_html(cle, exclure={'Lbl'} if r == 'LI' else ())
            if r == 'Code':
                code = '\n'.join(''.join(x.texte for x in l) for l in self.lignes_visuelles(self.runs_de(cle)))
                return '<pre><code>' + html.escape(code, quote=False) + '</code></pre>'
            contenu = self.en_ligne_html(cle)
            return f'<p>{contenu}</p>' if contenu else ''
        enfants = [c for c in n.enfants if self.noeuds[c].role not in ECARTES]
        if r == 'L':
            return self.liste(enfants)
        if r == 'Table':
            return self.tableau(cle, legende)
        corps = '\n'.join(h for _, h in self.rendre_suite(enfants, legende))
        if r == 'BlockQuote':
            return f'<blockquote>{corps}</blockquote>'
        return corps

    def rendre_suite(self, enfants, legende=None):
        """Rend une suite de frères en [(clé, html)]. Une légende (Caption) va au tableau qui
        la suit immédiatement, sinon à celui qui la précède, sinon reste un paragraphe."""
        a_table = [self.contient(c, {'Table'}) for c in enfants]
        legendes = {}
        for i, c in enumerate(enfants):
            if self.noeuds[c].role == 'Caption' and c in self.feuilles:
                if i + 1 < len(enfants) and a_table[i + 1]:
                    cible = i + 1
                else:
                    cible = i - 1 if i > 0 and a_table[i - 1] else None
                if cible is not None and cible not in legendes:
                    legendes[cible] = c
        pris = set(legendes.values())
        out = []
        for i, c in enumerate(enfants):
            if c in pris:
                continue
            leg = legendes.get(i)
            if leg is None and legende is not None and a_table[i]:
                leg, legende = legende, None
            h = self.rendre(c, legende=leg)
            if h:
                out.append((c, h))
        return out

    def liste(self, items):
        lbl = None
        for li in items:
            lbls = [c for c in self.noeuds[li].enfants if self.noeuds[c].role == 'Lbl']
            if lbls:
                lbl = self.texte(lbls[0])
                break
        m = re.fullmatch(r'\(?(\d+)[.)]?', lbl or '')
        lettre = re.fullmatch(r'\(?([a-zA-Z])[.)]', lbl or '')
        if m:
            balise, attrs = 'ol', f' start="{m.group(1)}"' if m.group(1) != '1' else ''
        elif lettre:
            balise, attrs = 'ol', f' type="{"a" if lettre.group(1).islower() else "A"}"'
        else:
            balise, attrs = 'ul', ''
        corps = []
        for li in items:
            n = self.noeuds[li]
            if n.role != 'LI' or li in self.feuilles:
                corps.append(f'<li>{self.rendre(li)}</li>')
                continue
            parts = []
            terme = None   # terme d'un alinéa suspendu (étiquette porteuse d'une phrase)
            for c, h in self.rendre_suite([c for c in n.enfants if self.noeuds[c].role != 'Lbl']):
                if c in getattr(self, 'termes_liste', ()) and h.startswith('<p>') and h.endswith('</p>'):
                    terme = (terme + ' ' if terme else '') + h[3:-4]
                    continue
                if terme:
                    h = f'<p>{terme} {h[3:]}' if h.startswith('<p>') else f'{terme} {h}'
                    terme = None
                parts.append(h)
            if terme:
                parts.append(f'<p>{terme}</p>')
            corps.append('<li>' + '\n'.join(parts) + '</li>')
        return f'<{balise}{attrs}>\n' + '\n'.join(corps) + f'\n</{balise}>'

    def tableau(self, cle, legende):
        rangees = []

        def collecter(c, en_tete):
            n = self.noeuds[c]
            if n.role == 'TR':
                rangees.append((c, en_tete))
            elif n.role not in ECARTES and n.role != 'Caption':
                for e in n.enfants:
                    collecter(e, en_tete or n.role == 'THead')
        collecter(cle, False)
        if legende is None:
            legende = next((c for c in self.noeuds[cle].enfants if self.noeuds[c].role == 'Caption'), None)
        tete, corps = [], []
        for tr, en_tete in rangees:
            cellules = [c for c in self.noeuds[tr].enfants if self.noeuds[c].role in ('TD', 'TH')]
            if not cellules:
                continue
            if en_tete or (not corps and all(self.noeuds[c].role == 'TH' for c in cellules)):
                # en-tête répété à chaque page sous le même élément : la première page compte
                p0 = min((r.page for c in cellules for r in self.runs_de(c)), default=None)
                for c in cellules:
                    for r in self.runs_de(c):
                        if r.page != p0:
                            self.noeuds[self.proprietaire(r)].runs.remove(r)
                            self.absorber(r.page, [r])
                tete.append('<tr>' + ''.join(f'<th>{self.rendre(c)}</th>' for c in cellules) + '</tr>')
            else:
                b = lambda c: 'th' if self.noeuds[c].role == 'TH' else 'td'
                corps.append('<tr>' + ''.join(f'<{b(c)}>{self.rendre(c)}</{b(c)}>' for c in cellules) + '</tr>')
        cap = f'<caption>{self.en_ligne_html(legende)}</caption>' if legende else ''
        return ('<table>' + cap + (f'<thead>{"".join(tete)}</thead>' if tete else '') +
                f'<tbody>{"".join(corps)}</tbody></table>')

    # ---- ensemble ---------------------------------------------------------------------

    def extraire(self):
        nues = [i for i in self.pages if not self.lire_page(self.doc[i])]
        if nues:
            # le repli classe les titres selon les tailles qu'ont les titres balisés
            tailles, titres = collections.Counter(), collections.defaultdict(collections.Counter)
            for n in self.noeuds.values():
                for r in n.runs:
                    tailles[round(r.taille, 1)] += len(r.texte)
                    if re.fullmatch(r'H\d', n.role):
                        titres[round(r.taille, 1)][int(n.role[1])] += 1
            corps = tailles.most_common(1)[0][0] if tailles else 11
            tailles_titres = {t: c.most_common(1)[0][0] for t, c in titres.items()}
            for i in nues:
                self.lire_page_nue(self.doc[i], corps, tailles_titres)
        for n in self.noeuds.values():
            for r in n.runs:
                self.vocabulaire.update(w.lower() for w in re.findall(r'\w+(?:-\w+)*', r.texte.replace(SHY, '')))
        self.absorber_entetes()
        self.classer()
        self.recaser()
        blocs = []
        for racine in self.racines:
            enfants = [c for c in self.noeuds[racine].enfants if self.noeuds[c].role not in ECARTES]
            for c, h in self.rendre_suite(enfants):
                p = min((r.page for r in self.runs_de(c)), default=None)
                blocs.append(Bloc(p, h))
        return blocs


@dataclasses.dataclass
class Bloc:
    page: int   # première page (0 = première page du PDF)
    html: str


def extraire(pdf, **params):
    """Liste de blocs HTML de premier niveau, dans l'ordre de lecture; voir Extracteur pour
    les paramètres (niveaux, marges, artefacts, styles_balises, polices, cesure_trait…)."""
    e = Extracteur(pdf, **params)
    blocs = e.extraire()
    extraire.dernier = e
    return blocs


def vers_html(blocs):
    return '\n'.join(b.html for b in blocs)


def texte_controle(fragment):
    """Texte d'un fragment HTML pour le contrôle mot à mot, numéros de listes compris
    (le PDF d'origine les porte en toutes lettres)."""
    def numeroter(m):
        debut = int(re.search(r'start="(\d+)"', m.group(1)).group(1)) if 'start=' in m.group(1) else 1
        items = re.split(r'(<li>)', m.group(2))
        k = 0
        for i, x in enumerate(items):
            if x == '<li>':
                items[i] = f'<li>{debut + k}. '
                k += 1
        return ''.join(items)
    # listes imbriquées : numérote de l'intérieur vers l'extérieur
    while True:
        f2 = re.sub(r'<ol([^>]*)>((?:(?!<ol\b)(?!</ol>).)*)</ol>', lambda m: '<OL>' + numeroter(m) + '</OL>',
                    fragment, flags=re.S)
        if f2 == fragment:
            break
        fragment = f2
    fragment = re.sub(r'</?(?:em|strong|code|a|sup|sub)(?=[\s>])[^>]*>', '', fragment)   # en ligne : sans blanc
    return html.unescape(re.sub(r'<[^>]+>', ' ', fragment))


def lire_par_position(pages):
    """Mots du PDF dans l'ordre du flux, à ceci près qu'un mot coupé en fin de ligne
    (trait conditionnel, ou adresse coupée sans trait : suite_url) se recolle au premier
    mot de la ligne qui le suit visuellement : la ligne suivante de son bloc si elle est
    juste dessous, sinon une ligne juste dessous qui commence dans la même colonne, ou,
    au bas de la colonne, la première de la même colonne en page suivante. Dans l'ordre
    du flux, une ligne retouchée directement dans le PDF est rangée en fin de page, une
    cellule de tableau peut s'intercaler (« préimpres- la sion »), un en-tête répété
    s'interposer au saut de page. Sans suite visuelle, le mot se recolle au suivant du
    flux, comme avant.
    pages : [(page PyMuPDF, [(Rect, texte, (bloc, ligne))] dans l'ordre du flux)]."""
    mots_d, lignes, liens_p, largeurs = [], {}, {}, {}
    for page, mots_p in pages:
        largeurs[page.number] = page.rect.width
        liens_p[page.number] = [(l['from'], l['uri']) for l in page.get_links() if l.get('kind') == pymupdf.LINK_URI]
        for r, t, (b, l) in mots_p:
            lignes.setdefault((page.number, b, l), []).append(len(mots_d))
            mots_d.append((page.number, r, t))
    cadres = {c: pymupdf.Rect(cadre([mots_d[k][1] for k in ks])) for c, ks in lignes.items()}
    par_page = collections.defaultdict(list)
    for c in lignes:
        par_page[c[0]].append(c)

    def lien(k):
        p, r = mots_d[k][0], mots_d[k][1]
        centre = pymupdf.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)
        return next((u for z, u in liens_p[p] if z.contains(centre)), None)

    suite, pred = {}, {}   # dernier mot d'une ligne <-> premier mot de sa suite
    accu = lambda k: (accu(pred[k]).removesuffix(SHY) if k in pred else '') + mots_d[k][2]
    for cle in sorted(lignes, key=lambda c: (c[0], cadres[c].y0, cadres[c].x0)):
        der = lignes[cle][-1]
        t = accu(der) if der in pred else mots_d[der][2]
        coupe = t.endswith(SHY)
        if not coupe and not re.search(r'https?://|[./]', t):
            continue
        p, L, h = cle[0], cadres[cle], mots_d[der][1].height
        colonne = lambda z: L.x0 - 2 <= z.x0 < L.x1
        sous = lambda z: z.y0 > L.y0 + 0.5 * h and z.y0 - L.y1 < 0.6 * h
        c = (p, cle[1], cle[2] + 1)
        if c not in cadres or not sous(cadres[c]):
            dessous = [c for c in par_page[p] if c != cle and sous(cadres[c]) and colonne(cadres[c])]
            if not dessous and L.width < 0.6 * largeurs[p] and \
                    not any(cadres[c].y0 > L.y0 + 0.5 * h and colonne(cadres[c]) for c in par_page[p]):
                # bas d'une colonne étroite (cellule) : la suite est en tête de la même
                # colonne, page suivante, sous l'en-tête répété. Le texte courant garde
                # l'ordre du flux.
                dessous = [c for c in par_page.get(p + 1, ()) if colonne(cadres[c])]
                dessous = [min(dessous, key=lambda c: (cadres[c].y0, cadres[c].x0))] if dessous else []
            if not dessous:
                continue
            c = min(dessous, key=lambda c: (cadres[c].y0, cadres[c].x0))
        prem = lignes[c][0]
        if prem in pred or prem == der:
            continue
        if coupe or suite_url(t, mots_d[prem][2], lien(der), lien(prem)):
            suite[der], pred[prem] = prem, der

    def mot(k):
        t = mots_d[k][2]
        return (t.removesuffix(SHY) + mot(suite[k])) if k in suite else t
    return [mot(k) for k in range(len(mots_d)) if k not in pred]


def controler_extraction(pdf, fragment, marges=(60, 60), pages=None, ecarter=()):
    """Complétude : chaque mot du texte courant du PDF (lu mot à mot, hors marges et hors
    zones « ecarter » = [(page, Rect)], p. ex. la table des matières, et hors en-têtes
    répétés que l'extraction de ce PDF a absorbés) figure dans le HTML. Rend (manquants,
    surnuméraires) en Counter, après recollage des césures et des adresses coupées en fin
    de ligne, chaque ligne à celle qui la suit visuellement (lire_par_position)."""
    from composer import mots
    doc = pymupdf.open(pdf)
    pages = range(doc.page_count) if pages is None else pages
    zones = collections.defaultdict(list)
    for q, z in list(ecarter) + ZONES_ABSORBEES.get(cle_fichier(pdf), []):
        zones[q].append(z)
    lues = []
    for i in pages:
        p = doc[i]
        mots_p = []
        for w in p.get_text('words'):
            r = pymupdf.Rect(w[:4])
            if r.y1 <= marges[0] or r.y0 >= p.rect.height - marges[1]:
                continue
            if any(z.intersects(r) for z in zones.get(i, ())):
                continue
            mots_p.append((r, w[4].replace(WJ, ''), (w[5], w[6])))
        lues.append((p, mots_p))
    rendu = ' '.join(lire_par_position(lues))
    rendu = re.sub(SHY + r'\s+', '', rendu).replace(SHY, '')
    pdf_mots = mots(rendu)
    html_mots = mots(texte_controle(fragment))
    return pdf_mots - html_mots, html_mots - pdf_mots


def zones_ecartees(pdf, roles=('TOC', 'TOCI'), titres=TITRES_ECARTES):
    """Rectangles de la table des matières d'origine (et de son titre), pour le contrôle."""
    doc = pymupdf.open(pdf)
    zones = []
    for p in doc:
        def marcher(b):
            if b['type'] == 2:
                if b.get('raw') in roles or b.get('std') in roles:
                    zones.append((p.number, pymupdf.Rect(b['bbox'])))
                    return
                if re.fullmatch(r'H\d?', b.get('std') or '') and titres:
                    t = ''.join(s['text'] for c in b.get('blocks', []) if c['type'] == 0
                                for l in c['lines'] for s in l['spans']).strip()
                    if re.search(titres, t, re.I):
                        zones.append((p.number, pymupdf.Rect(b['bbox'])))
                for c in b.get('blocks', []):
                    marcher(c)
        for b in p.get_text('dict', flags=pymupdf.TEXT_COLLECT_STRUCTURE)['blocks']:
            marcher(b)
    return zones


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    niveaux = {}
    if '--niveaux' in sys.argv:
        spec = sys.argv[sys.argv.index('--niveaux') + 1]
        args.remove(spec)
        niveaux = {int(a): int(b) for a, b in (x.split(':') for x in spec.split(','))}
    pdf = args[0]
    blocs = extraire(pdf, niveaux=niveaux)
    h = vers_html(blocs)
    if len(args) > 1:
        open(args[1], 'w', encoding='utf8').write(h)
    else:
        sys.stdout.write(h)
    manque, surplus = controler_extraction(pdf, h, ecarter=zones_ecartees(pdf))
    print(f'{len(blocs)} blocs; mots du PDF absents du HTML : {sum(manque.values())}'
          f' {dict(manque.most_common(20))}; mots en trop : {sum(surplus.values())} {dict(surplus.most_common(20))}',
          file=sys.stderr)
    for e in extraire.dernier.ecarts:
        print('  ' + e, file=sys.stderr)


if __name__ == '__main__':
    sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
    main()
