"""Recompose NiveauMaturité (présentation 16:9 de 7 diapositives) au format lettre.

Usage : python construire_pdf.py [sortie.pdf] [--html corps.html]
        (par défaut : documents/NiveauMaturité.pdf; --html garde le corps produit)

Pas de source amont versée au dépôt : le PDF d'origine (édition Chrome du 29 oct. 2026,
lue dans git au commit ORIGINE) fait foi pour le texte. Son ordre de lecture sort mêlé
(colonnes, libellés espacés lettre par lettre), d'où une autre voie que
sources/commun/extraire.py : on part de la source HTML de la présentation, versée au
commit SOURCE_HTML, on lui reporte les corrections du 29 oct. 2026 (PLAN.md, P4), puis
on vérifie que son texte couvre celui du PDF d'origine, mot pour mot, dans les deux sens.

Mise en page portrait :
  - couverture : titre, auteur, date et version tirés de la ligne de tête de la p. 1;
  - « L'échelle d'un coup d'œil » : la rangée de six cartes devient une pile dessinée en
    Typst (pile.typ, généré ici à partir du HTML), palier 1 en bas, avec les trois bandes;
  - un chapitre par palier : portée, jauge « Palier N sur 6 », question en exergue, puis
    les trois encadrés (« En clair », « Ce qui casse… », « Chez nous… ») en sections.
Pas de table des matières : sept titres sur quelques pages, la pile en tient lieu (les
signets PDF restent, produits par Typst).

Actualisation du 1er novembre 2026 : note datée, rédigée en HTML dans ce dossier
(actualisation-2026-11.html), composée après le palier 6, hors du contrôle d'origine (elle
n'est pas dans le PDF d'origine) mais dans le contrôle mot à mot de composer().
"""
import collections, html, pathlib, re, subprocess, sys, tempfile
import pymupdf

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
from composer import ACTUALISATION, AUTEUR, DOCUMENTS, actualisation, chaine_typst, composer, mots, typographie
from extraire import texte_controle

args = sys.argv[1:]
HTML = pathlib.Path(args.pop(args.index('--html') + 1)) if '--html' in args else None
args = [a for a in args if a != '--html']
SORTIE = DOCUMENTS / 'NiveauMaturité.pdf'
OUT = pathlib.Path(args[0]) if args else SORTIE
ORIGINE = 'd28324a'      # dernière édition d'origine (Chrome), avant recomposition
SOURCE_HTML = '4457a54'  # source HTML de la présentation, d'avant les corrections du 29 oct.

# Corrections du 29 oct. 2026 (PLAN.md, chantier P4, retiré au commit d47db0f) faites dans
# le PDF et absentes de la source versée : (avant, après, occurrences attendues).
CORRECTIONS = [
    ('Technico&shy;Syntaxique', 'Technico-Syntaxique', 2),   # P4.2 : trait d'union
    ('<p class="eyebrow">L\'échelle d\'un coup d\'œil</p>',    # P4.4 : auteur, date, version
     '<p class="eyebrow">L\'échelle d\'un coup d\'œil · André-Guy Bruneau · Octobre 2026 · Version 1.0</p>', 1),
]


def git_show(chemin, commit):
    return subprocess.run(['git', 'show', f'{commit}:{chemin}'], cwd=DOCUMENTS, capture_output=True,
                          check=True).stdout


def source_corrigee():
    s = git_show('NiveauMaturité.html', SOURCE_HTML).decode('utf8')
    for avant, apres, n in CORRECTIONS:
        assert s.count(avant) == n, (avant, s.count(avant))
        s = s.replace(avant, apres)
    return s


def texte(fragment):
    """Texte brut d'un fragment HTML (entités résolues)."""
    return html.unescape(re.sub(r'<[^>]+>', '', fragment)).strip()


def lire(s):
    """Découpe la présentation : diapositive d'ensemble, puis une par palier."""
    diapos = re.findall(r'<section class="slide"[^>]*>(.*?)</section>', s, re.S)
    assert len(diapos) == 7, len(diapos)
    d = diapos[0]
    tete = texte(re.search(r'<p class="eyebrow">(.*?)</p>', d).group(1)).split(' · ')
    assert len(tete) == 4 and tete[3].startswith('Version '), tete
    pied = re.search(r'<div class="scale-foot">\s*<div>(.*?)</div>\s*<span class="invariant">(.*?)</span>', d, re.S)
    ens = dict(
        rubrique=tete[0], auteur=tete[1], date=tete[2], version=tete[3].removeprefix('Version '),
        titre=texte(re.search(r'<h2>(.*?)</h2>', d).group(1)),
        cartes=[(int(n), texte(nm), texte(q)) for n, nm, q in re.findall(
            r'<li data-lvl="\d"><span class="n">(\d)</span><span class="nm">(.*?)</span><span class="q">(.*?)</span></li>', d)],
        bandes=[texte(b) for b in re.findall(r'<span>(.*?)</span>',
                                             re.search(r'<div class="bands"[^>]*>(.*?)</div>', d, re.S).group(1))],
        notes=[re.sub(r'<p[^>]*>', '<p>', p) for p in re.findall(r'<p[^>]*>.*?</p>', pied.group(1), re.S)],
        invariant=texte(pied.group(2)))
    assert [c[0] for c in ens['cartes']] == list(range(1, 7)) and len(ens['bandes']) == 3 and len(ens['notes']) == 2
    paliers = []
    for n, d in enumerate(diapos[1:], 1):
        g = lambda motif: texte(re.search(motif, d, re.S).group(1))
        p = dict(n=n, badge=g(r'<span class="badge">(.*?)</span>'), nom=g(r'<h2>(.*?)</h2>'),
                 portee=g(r'<p class="level-scope">(.*?)</p>'), jauge=g(r'<p class="meter-cap">(.*?)</p>'),
                 question=re.search(r'<p class="question">(.*?)</p>', d, re.S).group(1),
                 encadres=re.findall(r'<div class="block[^"]*">\s*<span class="label">(.*?)</span>\s*(<p>.*?</p>)', d, re.S))
        assert p['badge'] == f'Palier {n}' and p['jauge'].startswith(f'Palier {n} sur 6') and len(p['encadres']) == 3, p
        paliers.append(p)
    return ens, paliers


def typo(t):
    """Typographie du corps (insécables, apostrophes) pour une chaîne posée en Typst."""
    return html.unescape(re.sub(r'<[^>]+>', '', typographie(f'<p>{html.escape(t, quote=False)}</p>')))


def bornes(bande):
    """« 1 à 3 · … » -> (1, 3); « 6 · … » -> (6, 6)."""
    ns = [int(x) for x in re.findall(r'\d', bande.split('·')[0])]
    return min(ns), max(ns)


def pile_typ(ens):
    """Fichier Typst de la pile (figure d'ensemble) et de la jauge des paliers."""
    cartes = ', '.join(f'({n}, {chaine_typst(typo(nm))}, {chaine_typst(typo(q))})' for n, nm, q in ens['cartes'])
    bandes = ', '.join(f'({chaine_typst(typo(b))}, {bornes(b)[0]}, {bornes(b)[1]})' for b in ens['bandes'])
    return f'''#import "gabarit.typ": *

// Pile des six paliers (généré par construire_pdf.py à partir de la source HTML).
#let paliers = ({cartes},)
#let bandes = ({bandes},)
#let invariant = {chaine_typst(typo(ens['invariant']))}

// Palier 1 en bas : on lit la pile vers le bas quand quelque chose casse. Le palier 6
// (changement de nature) est plein; les bandes regroupent les paliers à droite.
#let pile() = {{
  set text(font: sans, size: 8pt)
  set par(justify: false, leading: 0.45em)
  let h = 38pt
  let cellule(p) = {{
    let (n, nom, q) = p
    let six = n == 6
    let c(normal) = if six {{ white }} else {{ normal }}
    block(width: 100%, height: h, inset: (x: 9pt), radius: 2pt,
      fill: if six {{ accent }} else {{ accent-pale }}, stroke: 0.5pt + if six {{ accent }} else {{ filet }},
      align(horizon, grid(columns: (14pt, 96pt, 1fr), column-gutter: 8pt, align: left + horizon,
        text(size: 15pt, weight: "bold", fill: c(accent), str(n)),
        text(size: 9pt, weight: "semibold", fill: c(encre), hyphenate: false, nom),
        text(fill: c(gris), hyphenate: false, q))))
  }}
  let bande(t) = block(width: 100%, height: 100%, stroke: (left: 1.5pt + accent), inset: (left: 9pt, right: 2pt),
    align(left + horizon, text(size: 7pt, weight: "semibold", fill: accent, tracking: 0.4pt, hyphenate: false, upper(t))))
  figure(kind: image, supplement: [Figure],
    caption: [Les six paliers, du transport du message (1) à la coordination entre agents (6)],
    block(width: 100%, {{
      grid(columns: (1fr, 132pt), rows: (h,) * 6, column-gutter: 12pt, row-gutter: 4pt,
        ..paliers.rev().enumerate().map(((i, p)) => grid.cell(x: 0, y: i, cellule(p))),
        ..bandes.map(((t, bas, haut)) => grid.cell(x: 1, y: 6 - haut, rowspan: haut - bas + 1, bande(t))))
      v(10pt)
      align(center, text(size: 7pt, weight: "semibold", fill: gris, tracking: 0.5pt, upper(invariant)))
    }}))
  v(6pt)
}}

// Jauge d'un palier : portée à gauche, six cases à droite (palier courant plein).
#let jauge(n, legende, portee) = block(above: 2pt, below: 14pt, sticky: true, grid(columns: (1fr, auto),
  column-gutter: 18pt, align: (left + horizon, right + horizon),
  text(style: "italic", fill: gris, size: 11pt, portee),
  stack(dir: ttb, spacing: 5pt,
    stack(dir: ltr, spacing: 2pt, ..range(1, 7).map(i => box(width: 17pt, height: 12pt,
      fill: if i == n {{ accent }} else if i < n {{ accent-pale }},
      stroke: 0.5pt + if i == n {{ accent }} else {{ filet }},
      align(center + horizon, text(font: sans, size: 6.5pt, weight: "semibold",
        fill: if i == n {{ white }} else if i < n {{ accent }} else {{ gris }}, str(i)))))),
    align(right, text(font: sans, size: 6.8pt, weight: "semibold", fill: gris, tracking: 0.6pt, upper(legende))))))
'''


def attr(expr):
    return html.escape(expr, quote=True)


def corps(ens, paliers):
    h = [f'<h2>{html.escape(ens["rubrique"], quote=False)}</h2>', '<div data-typst="pile()"></div>', *ens['notes']]
    for p in paliers:
        h += [f'<h2>{html.escape(p["badge"], quote=False)} — {html.escape(p["nom"], quote=False)}</h2>',
              f'<div data-typst="{attr(f"jauge({p['n']}, {chaine_typst(typo(p['jauge']))}, {chaine_typst(typo(p['portee']))})")}"></div>',
              f'<blockquote><p>{p["question"]}</p></blockquote>']
        for etiquette, para in p['encadres']:
            h += [f'<h3>{etiquette}</h3>', para]
    return '\n'.join(h)


def texte_figures(ens, paliers):
    """Texte que les figures Typst posent dans le PDF (pour les deux contrôles)."""
    t = [f'{n} {nm} {q}' for n, nm, q in ens['cartes']] + ens['bandes'] + [ens['invariant']]
    t += [f'{p["portee"]} {" ".join(map(str, range(1, 7)))} {p["jauge"]}' for p in paliers]
    return ' '.join(t)


# --- Contrôle de complétude : PDF d'origine -> texte recomposé -------------------------

def serre(t):
    """Libellé espacé ou non, ramené à ses lettres : « D O N N É E S » -> « DONNÉES »."""
    return re.sub(r'\s+', '', t.replace('’', "'")).upper()


def lignes_origine(pdf):
    for p in pymupdf.open(pdf):
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                yield ''.join(s['text'] for s in l['spans']).replace('\xa0', ' ').strip()


def est_espacee(ligne):
    jetons = ligne.split()
    return len(jetons) >= 4 and sum(len(j) == 1 for j in jetons) > len(jetons) / 2


def controler_completude(pdf, source):
    """Chaque mot du PDF d'origine doit figurer dans la source recomposée, et inversement
    (hors ajouts déclarés). Une ligne espacée lettre par lettre (majorité de jetons d'un
    signe) se compare sans ses espaces, morceau par morceau entre les « · » : sa ligne de
    tête de la p. 1 se répartit sur la couverture."""
    courantes, espacees = [], collections.Counter()
    for l in lignes_origine(pdf):
        if est_espacee(l):
            espacees.update(serre(m) for m in l.split('·') if m.strip())
        else:
            courantes.append(l)
    manque = mots(' '.join(courantes)) - mots(source)
    serree = serre(source)
    absents = {m: n for m, n in espacees.items() if serree.count(m) < n}
    return manque, absents


def main():
    ens, paliers = lire(source_corrigee())
    # auteur affiché : forme titrée de composer, qui prolonge celle de la ligne de tête
    assert AUTEUR.startswith(ens['auteur'] + ' '), (AUTEUR, ens['auteur'])
    texte_corps = corps(ens, paliers)
    if HTML:
        HTML.write_text(texte_corps, encoding='utf8')
    sous_titre = pymupdf.open(stream=git_show(f'documents/{SORTIE.name}', ORIGINE)).metadata['subject'].split(' — ')[0]
    fiche = ('<div class="fiche"><table><tbody>'
             f'<tr><td>Auteur</td><td>{html.escape(AUTEUR)}</td></tr>'
             f'<tr><td>Version</td><td>{html.escape(ens["version"])} · {html.escape(ens["date"].lower())}</td></tr>'
             '<tr><td>Édition d’origine</td><td>Présentation de sept diapositives (16:9), '
             'recomposée au format lettre</td></tr>'
             f'<tr><td>Actualisation</td><td>{ACTUALISATION}, en dernière page</td></tr>'
             '</tbody></table></div>')
    annexe, refs_annexe = actualisation(ICI)
    figures = texte_figures(ens, paliers)
    corps_controle = ' '.join([texte_controle(texte_corps), figures])
    couverture = ' '.join([ens['rubrique'], ens['titre'], AUTEUR, ens['date'], 'Version', ens['version']])

    with tempfile.TemporaryDirectory() as tmp:
        origine = pathlib.Path(tmp) / 'origine.pdf'
        origine.write_bytes(git_show(f'documents/{SORTIE.name}', ORIGINE))
        # complétude : rien du PDF d'origine ne manque à la recomposition...
        manque, absents = controler_completude(origine, couverture + ' ' + corps_controle)
        if manque or absents:
            sys.exit(f'texte du PDF d\'origine absent de la recomposition : {dict(manque)} {absents}')
        # ... et le corps n'ajoute rien, hors chiffres des jauges (le PDF d'origine n'en
        # porte qu'un par palier, en filigrane). Les mots des libellés espacés se comptent
        # dans leurs lettres serrées (« PALIER1SUR6 » contient « palier »).
        lignes = list(lignes_origine(origine))
        serrees = '|'.join(serre(l) for l in lignes if est_espacee(l))
        surplus = {m: n for m, n in (mots(corps_controle) - mots(' '.join(lignes))).items()
                   if not m.isdigit() and serrees.count(m.upper()) < n}
        if surplus:
            sys.exit(f"texte recomposé absent du PDF d'origine : {surplus}")
        print(f'complétude : texte du PDF d\'origine intégralement repris, rien d\'ajouté au corps')

        pile = pathlib.Path(tmp) / 'pile.typ'
        pile.write_text(pile_typ(ens), encoding='utf8')
        t = lambda x: chaine_typst(typo(x))
        main_typ = f'''#import "gabarit.typ": *
#import "pile.typ": *
#set document(title: {t(ens['titre'])},
  description: "{sous_titre} — version {ens['version']}, {ens['date'].lower()}",
  keywords: ("interopérabilité", "maturité", "agents", "orchestration"))
#show: note.with(titre-court: "Échelle de maturité", pied: [Version {ens['version']} · {ens['date'].lower()} · actualisation du {ACTUALISATION}])
// signets : l'ensemble et les six paliers, comme l'édition d'origine
#set heading(bookmarked: false)
#show heading.where(level: 2): set heading(bookmarked: true)
// question du palier, en exergue, jamais seule en bas de page
#show quote.where(block: true): it => block(above: 6pt, below: 16pt, sticky: true, stroke: (left: 2.5pt + accent),
  inset: (left: 11pt, y: 3pt), {{
    set par(justify: false, leading: 0.5em)
    text(font: sans, size: 12.5pt, weight: "semibold", fill: accent, it.body)
  }})
#couverture(surtitre: [Échelle de maturité], titre: {t(ens['titre'])},
  sous-titre: {t(sous_titre)}, auteur: {t(AUTEUR)}, date: {t(ens['date'])},
  fiche: include "fiche.typ")
#include "corps.typ"
#pagebreak(weak: true)
#include "actualisation.typ"
#[#set par(justify: false, linebreaks: "simple")
#include "references-actualisation.typ"]
'''
        source = ' '.join([texte_controle(f) for f in (fiche, annexe, refs_annexe)] +
                          [ens['titre'], sous_titre, AUTEUR, ens['date'], corps_controle])
        composer({'fiche': fiche, 'corps': texte_corps, 'actualisation': annexe,
                  'references-actualisation': refs_annexe}, main_typ, OUT, source, extras=[pile])


if __name__ == '__main__':
    main()
