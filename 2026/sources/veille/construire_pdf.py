"""Recompose le PDF de la Veille technologique à partir de son édition d'origine.

Usage : python construire_pdf.py [source.pdf] [sortie.pdf] [--html extrait.html]
        (par défaut : l'édition d'origine, lue dans git au commit ORIGINE, recomposée
        dans documents/Veille Technologique.pdf; --html garde l'extraction)

Aucune source amont n'est versée au dépôt : le PDF fait foi, reprise et errata du
29 oct. 2026 compris. sources/commun/extraire.py le relit (PDF balisé; repli géométrique
pour l'annexe du 29 octobre, pp. 145-152, fusionnée sans balisage), puis
sources/commun/composer.py le recompose avec le gabarit commun.

Particularités traitées ici :
  - page de titre : titre, sous-titre, auteur et date passent sur la couverture, la
    mention de révision dans la fiche;
  - Résumé et Abstract : leur intitulé en gras devient un titre; l'Abstract est
    composé en anglais (césure);
  - titres : sections (H1) en chapitres, sous-sections (H2) en sections; les
    sous-sous-sections (4.11.1, 4.13.1…), balisées H2 elles aussi, en niveau 4;
  - retouches du 29 octobre (lignes recomposées directement dans le PDF) : l'extraction
    recase leurs lignes, mais quelques frontières de paragraphe ou d'item restent
    déplacées; RECOLLER et SCINDER les rétablissent d'après le rendu d'origine;
  - Références : le chapeau en italique, recasé dans la référence 1, en ressort; les
    références sont composées en drapeau, comme à l'origine;
  - annexe du 29 octobre : ses références [343] à [371], composées en grille (numéro
    aligné à droite), redeviennent une liste numérotée comme celles du corps;
  - légendes « Tableau N. – … » : la numérotation passe à Typst (même suite, contrôlée);
  - gras : celui de la police seulement. Le PDF balise en Strong des passages composés
    en romain (intitulés des constats, de paragraphes, d'items); le rendu d'origine fait foi;
  - code : balise Code et police à chasse fixe -> <code>, laissé littéral par composer.

Actualisation du 11 novembre 2026 (prolongeant celle du 1er novembre) : annexe datée,
rédigée en HTML dans ce dossier (actualisation-2026-11.html), composée après l'annexe du
29 octobre; ses tableaux et ses références continuent les suites du document (tableau 27,
référence 372).

Relecture du 11 novembre 2026 (prolongeant celle du 3 novembre) : ses corrections du corps
sont faites à leur place par corrections.py, sur le corps extrait, et consignées au
tableau 31 de l'annexe, que la fiche nomme.
"""
import atexit, collections, html, pathlib, re, shutil, subprocess, sys, tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
from composer import (AUTEUR, DOCUMENTS, actualisation, chaine_typst, composer, date_fr,
                      tableau_relecture)
from extraire import controler_extraction, extraire, texte_controle, vers_html, zones_ecartees
from corrections import corriger
import pymupdf

ACTUALISATION = date_fr(2026, 11, 11)
RELECTURE = date_fr(2026, 11, 11)

args = sys.argv[1:]
HTML = pathlib.Path(args.pop(args.index('--html') + 1)) if '--html' in args else None
args = [a for a in args if a != '--html']
SORTIE = DOCUMENTS / 'Veille Technologique.pdf'
# Dernière édition d'origine (Typst, retouchée le 29 oct. 2026) : le PDF recomposé ne
# doit pas servir de source à son tour.
ORIGINE = 'd28324a'
if len(args) > 1:
    SRC, OUT = pathlib.Path(args[0]), pathlib.Path(args[1])
else:
    OUT = pathlib.Path(args[0]) if len(args) == 1 else SORTIE
    SRC = pathlib.Path(tempfile.mkdtemp()) / 'origine.pdf'
    atexit.register(shutil.rmtree, SRC.parent, True)
    SRC.write_bytes(subprocess.run(['git', 'show', f'{ORIGINE}:documents/{SORTIE.name}'], cwd=DOCUMENTS,
                                   capture_output=True, check=True).stdout)

# Écarts connus du contrôle de complétude (mots du PDF d'origine absents de l'extraction) :
# aucun. Les en-têtes répétés de l'annexe non balisée (tableaux 25 et 26) sont absorbés
# par l'extraction, qui les soustrait au contrôle; celui-ci lit les césures par position
# (« méca-/nisme », « dé-/posi-/taire » des lignes retouchées, p. 1 et 95).
ECARTS_CONNUS = {}

# Frontières déplacées par les retouches : (avant, après). « recoller » réunit deux blocs
# que l'extraction a séparés ([balise fermante + ouvrante] retirées entre les deux
# chaînes); « scinder » ouvre un bloc avant la chaîne. Chaque retouche doit s'appliquer
# exactement une fois.
RECOLLER = [
    # p. 2, Abstract, 3e paragraphe : « twelve individual / drafts submitted… »
    ('enforceable traceability — twelve individual', ' ', 'drafts submitted to the IETF'),
    # p. 7, constat 2 : « (quatre / SDK Tier-1 en bêta) »
    ('non sa révision courante (quatre', ' ', 'SDK Tier-1 en bêta)'),
    # p. 8, constat 9 : « Au-/delà de deux sauts »
    ('commandité par Token Security</strong>). Au-', '', 'delà de deux sauts, douze'),
    # p. 65, § 7.10 : « revérifié sur le texte le 15 août 2026, / A2A v1.0.0 … »
    ('<em>revérifié sur le texte le 15 août 2026</em>,', ' ', 'A2A v1.0.0 ne mentionne'),
    # p. 76, question 2 : « aucun / adopté : reste lequel, quand »
    ('chaînes à N sauts [162] [276] [277], aucun', ' ', 'adopté : reste <strong>lequel, quand</strong>.'),
]
SCINDER = [
    # Abstract : le 4e paragraphe s'ouvre sur « The edition of 15 August 2026 »
    ('p', 'The edition of 15 August 2026 extends'),
    # Sommaire exécutif : un paragraphe par constat
    ('p', '2. L’adoption précède l’assurance.'),
    ('p', '10. Le corpus compagnon compte'),
    # § 7.10 : « Le fait négatif n'en est que plus net » ouvre un paragraphe
    ('p', 'Le fait négatif n’en est que plus net'),
    # § 11, question 3
    ('li', '<strong>Découverte digne de confiance.</strong>'),
    # § 12.3 : chaque pari ouvre un paragraphe
    ('p', '<strong>La convergence de l’identité.</strong>'),
]


def niveau(n, texte):
    """H1 -> chapitre (2), H2 -> section (3); les sous-sous-sections (4.11.1…), balisées
    H2 dans le PDF, passent au niveau 4."""
    if n == 2 and re.match(r'\d+\.\d+\.\d+\s', texte):
        return 4
    return {1: 2, 2: 3}.get(n, n + 1)


def page_de_titre(pdf):
    """Titre (15 pt), sous-titre (12 pt), ligne auteur · courriel · date, mention de révision."""
    lignes = [(round(l['spans'][0]['size']), ''.join(s['text'] for s in l['spans']).strip())
              for b in pymupdf.open(pdf)[0].get_text('dict')['blocks'] for l in b.get('lines', [])]
    titre = next(t for s, t in lignes if s == 15)
    sous_titre = next(t for s, t in lignes if s == 12)
    auteur, courriel, date = next(t for s, t in lignes if '·' in t and '@' in t).split(' · ')
    revision = next(t for s, t in lignes if t.startswith('Révision du'))
    return dict(titre=titre, sous_titre=sous_titre, auteur=auteur, courriel=courriel, date=date, revision=revision)


def retoucher(s):
    for avant, joint, apres in RECOLLER:
        motif = re.escape(avant) + r'</(p|li)>\n<\1>' + re.escape(apres)
        assert len(re.findall(motif, s)) == 1, f'retouche introuvable : {avant!r}'
        s = re.sub(motif, lambda m: avant + joint + apres, s)
    for balise, debut in SCINDER:
        assert s.count(debut) == 1, f'scission introuvable : {debut!r}'
        i = s.index(debut)
        s = s[:i].rstrip(' ') + f'</{balise}>\n<{balise}>' + s[i:]
    return s


def references_reprise(s):
    """Références [343] à [371] : un <p> par référence (« 343. … ») -> <ol start="343">."""
    debut = s.index('<h3>Références de la reprise</h3>\n') + len('<h3>Références de la reprise</h3>\n')
    refs = re.findall(r'<p>(.*?)</p>\n?', s[debut:])
    assert ''.join(f'<p>{r}</p>\n' for r in refs).rstrip('\n') == s[debut:].rstrip('\n'), \
        'références de la reprise : bloc inattendu'
    nums = [re.match(r'(\d+)\. ', r) for r in refs]
    assert [m and int(m.group(1)) for m in nums] == list(range(343, 372)), 'références de la reprise : numérotation'
    corps = '\n'.join(f'<li><p>{r[m.end():]}</p></li>' for r, m in zip(refs, nums))
    return s[:debut] + f'<ol start="343">\n{corps}\n</ol>'


def corps(blocs, p):
    # la page de titre : bloc du titre et mention de révision, repris sur la couverture
    assert p['titre'] in blocs[0].html and p['revision'] in blocs[1].html, 'page de titre inattendue'
    s = retoucher('\n'.join(b.html for b in blocs[2:]))
    h = s.split('\n')
    # Résumé, Abstract : intitulé en gras de tête -> titre; l'Abstract court jusqu'aux
    # mots-clés
    for i, b in enumerate(h):
        m = re.match(r'<p><strong>(Résumé|Abstract)</strong> ', b)
        if m:
            h[i] = f'<h2>{m.group(1)}</h2>\n<p>' + b[m.end():]
    debut = next(i for i, b in enumerate(h) if b.startswith('<h2>Abstract'))
    fin = next(i for i, b in enumerate(h) if i > debut and b.startswith(('<h2>', '<p><strong>Mots-clés')))
    h[debut:fin] = [h[debut].split('\n', 1)[0], '<div lang="en">', h[debut].split('\n', 1)[1], *h[debut + 1:fin],
                    '</div>']
    s = '\n'.join(h)
    # Références : le chapeau en italique, recasé dans la référence 1, passe devant la liste
    m = re.search(r'<h2>Références</h2>\n<ol>\n<li><p>(<em>Plusieurs références renvoient[^<]*</em>) ', s)
    assert m, 'chapeau des références introuvable'
    s = s[:m.start()] + f'<h2>Références</h2>\n<p>{m.group(1)}</p>\n<ol>\n<li><p>' + s[m.end():]
    return references_reprise(s)


def legendes(s):
    # légendes : « Tableau N. – » laisse la place à la numérotation de Typst
    nums = [int(n) for n in re.findall(r'<caption>Tableau\xa0(\d+)\.\xa0– ', s)]
    assert nums == list(range(1, len(nums) + 1)) and s.count('<caption>') == len(nums), nums
    return re.sub(r'<caption>Tableau\xa0\d+\.\xa0– ', '<caption>', s)


def poser_liens_internes(fragments):
    """O-17 : pose des ancres id="sec-...", id="tab-...", id="ref-..." sur les titres de
    section, les tableaux et les entrées bibliographiques, puis convertit tous les appels [n],
    renvois de section et de tableau en liens internes HTML <a href="#..."> résolus dans le PDF."""
    sections = set()
    extra_sec = 0

    def ancrer_titre(m):
        tag, num, reste = m.group(1), m.group(2), m.group(3)
        sec_id = 'sec-' + num.replace('.', '-')
        sections.add(num)
        return f'<{tag} id="{sec_id}">{num}{reste}</{tag}>'

    def ancrer_autre_titre(m):
        nonlocal extra_sec
        extra_sec += 1
        return f'<{m.group(1)} id="sec-h-{extra_sec}">{m.group(2)}</{m.group(1)}>'

    for k in ('corps', 'references', 'reprise', 'references-reprise', 'actualisation', 'references-actualisation'):
        fragments[k] = re.sub(r'<(h[234])>(\d+(?:\.\d+)*)( .*?)</\1>', ancrer_titre, fragments[k])
        fragments[k] = re.sub(r'<(h[234])>(.*?)</\1>', ancrer_autre_titre, fragments[k])

    tab_num = 0
    tableaux = set()

    def ancrer_table(m):
        nonlocal tab_num
        tab_num += 1
        tableaux.add(str(tab_num))
        return f'<table id="tab-{tab_num}">{m.group(1)}<caption>'

    for k in ('corps', 'reprise', 'actualisation'):
        fragments[k] = re.sub(r'<table>(\s*)<caption>', ancrer_table, fragments[k])
    assert tab_num == 31, f'31 tableaux attendus, {tab_num} trouvés'

    ref_num = 0
    refs = set()

    def ancrer_li(m):
        nonlocal ref_num
        ref_num += 1
        refs.add(str(ref_num))
        return f'<li id="ref-{ref_num}">'

    for k, attendu in (('references', 342), ('references-reprise', 371), ('references-actualisation', 446)):
        fragments[k] = re.sub(r'<li>', ancrer_li, fragments[k])
        assert ref_num == attendu, f'{attendu} références attendues après {k}, {ref_num} trouvées'

    def sec_href(s):
        return '#sec-' + s.replace('.', '-')

    def lier_crochet(m):
        interieur = m.group(1)
        nombres = re.findall(r'\d+', interieur)
        if not nombres or not all(n in refs for n in nombres):
            return m.group(0)
        interieur_lie = re.sub(r'\d+', lambda nm: f'<a href="#ref-{nm.group(0)}">{nm.group(0)}</a>', interieur)
        return f'[{interieur_lie}]'

    def lier_tableaux(m):
        mot, esp, suite = m.group(1), m.group(2), m.group(3)
        nombres = re.findall(r'\d+', suite)
        if not nombres or not all(n in tableaux for n in nombres):
            return m.group(0)
        premier = nombres[0]
        fin_premier = len(premier)
        reste = re.sub(r'\d+', lambda nm: f'<a href="#tab-{nm.group(0)}">{nm.group(0)}</a>', suite[fin_premier:])
        return f'<a href="#tab-{premier}">{mot}{esp}{suite[:fin_premier]}</a>{reste}'

    def lier_sections(m):
        mot, esp, suite = m.group(1), m.group(2), m.group(3)
        nums = re.findall(r'\d+(?:\.\d+)*', suite)
        if not nums or not all(n in sections for n in nums):
            return m.group(0)
        premier = nums[0]
        fin_premier = len(premier)
        reste = re.sub(r'\d+(?:\.\d+)*', lambda nm: f'<a href="{sec_href(nm.group(0))}">{nm.group(0)}</a>', suite[fin_premier:])
        return f'<a href="{sec_href(premier)}">{mot}{esp}{suite[:fin_premier]}</a>{reste}'

    def lier_segment(seg):
        # 1. Appels bibliographiques [n], listes [n, m] et plages [a-b]
        seg = re.sub(r'\[(\d+(?:\s*[,;–-]\s*\d+)*)\]', lier_crochet, seg)
        # 2. Renvois de tableaux : « tableau N », « tableaux N, M et K »
        seg = re.sub(
            r'\b([Tt]ableaux?)(\s+)(\d+(?!\.\d)(?:(?:\s*,\s*|\s+(?:et|à)\s+)\d+(?!\.\d))*)\b',
            lier_tableaux,
            seg,
        )
        # 3. Renvois explicites de sections : « section X.Y », « § X.Y », « sections X à Y et Z »
        seg = re.sub(
            r'(?:(\b[Ss]ections?|§)(\s*))(\d+(?:\.\d+)*(?:(?:\s*,\s*|\s+(?:et|à)\s+)\d+(?:\.\d+)*)*)\b',
            lier_sections,
            seg,
        )
        # 4. Renvois de sous-sections entre parenthèses ou après « en »
        seg = re.sub(
            r'(?<=\()(\d+\.\d+(?:\.\d+)?)(?:,\s*(\d+\.\d+(?:\.\d+)?))*(?=\))',
            lambda m: re.sub(
                r'\d+\.\d+(?:\.\d+)?',
                lambda sm: f'<a href="{sec_href(sm.group(0))}">{sm.group(0)}</a>'
                if sm.group(0) in sections else sm.group(0),
                m.group(0),
            ),
            seg,
        )
        seg = re.sub(
            r'\b(en|qu’en)(\s+)(\d+\.\d+(?:\.\d+)?)\b',
            lambda m: f'{m.group(1)}{m.group(2)}<a href="{sec_href(m.group(3))}">{m.group(3)}</a>'
            if m.group(3) in sections else m.group(0),
            seg,
        )
        return seg

    def transformer_html(doc):
        parties = re.split(r'(<a\b[^>]*>.*?</a>|<code>.*?</code>|<h[234]\b[^>]*>.*?</h[234]>|<[^>]+>)', doc, flags=re.S)
        for i in range(0, len(parties), 2):
            parties[i] = lier_segment(parties[i])
        return ''.join(parties)

    for k in list(fragments.keys()):
        fragments[k] = transformer_html(fragments[k])
    return fragments


def main():
    blocs = extraire(SRC, niveaux=niveau, styles_balises={'Em': 'em', 'Code': 'code'})
    brut = vers_html(blocs)
    if HTML:
        HTML.write_text(brut, encoding='utf8')
    p = page_de_titre(SRC)
    texte = corps(blocs, p)
    if HTML:
        HTML.with_suffix('.corps.html').write_text(texte, encoding='utf8')
    # complétude : chaque mot du texte courant d'origine (hors marges et table des
    # matières) doit se retrouver dans l'extraction mise en forme. Le contrôle porte sur
    # le HTML retouché; seuls les écarts connus sont tolérés.
    manque, _ = controler_extraction(SRC, blocs[0].html + blocs[1].html + texte, ecarter=zones_ecartees(SRC))
    tolere = collections.Counter(ECARTS_CONNUS)
    inexplique = {m: n for m, n in manque.items() if n > tolere[m]}
    if inexplique:
        sys.exit(f'extraction incomplète : {inexplique}')
    inutiles = {m: n for m, n in tolere.items() if manque[m] < n}
    assert not inutiles, f'écarts tolérés qui ne se produisent pas : {inutiles}'
    print(f'extraction : {len(blocs)} blocs, écarts connus seulement ({sum(manque.values())} mots)')
    # relecture du 3 novembre 2026 : corrections faites à leur place (corrections.py), après
    # le contrôle d'extraction, qui porte sur le texte d'origine
    p['sous_titre'] = p['sous_titre'].replace('Orchestration Agentiques', 'orchestration agentiques')
    texte = legendes(corriger(texte))
    revision = p['revision'].removeprefix('Révision du ').strip()
    annexe, refs_annexe = actualisation(ICI)
    # signature : la forme commune (AUTEUR) remplace celle de l'origine
    fiche = ('<div class="fiche"><table><tbody>'
             f'<tr><td>Auteur</td><td>{html.escape(AUTEUR)} · {html.escape(p["courriel"])}</td></tr>'
             f'<tr><td>Faits gelés au</td><td>{html.escape(p["date"])}</td></tr>'
             f'<tr><td>Révision</td><td>{html.escape(revision)}</td></tr>'
             f'<tr><td>Actualisation</td><td>{ACTUALISATION}, en annexe</td></tr>'
             f'<tr><td>Relecture</td><td>{RELECTURE} : corrections du corps faites à leur place, '
             f'consignées en annexe (tableau {tableau_relecture(texte, annexe, RELECTURE)})</td></tr>'
             '</tbody></table></div>')
    typo = lambda t: chaine_typst(t.replace("'", '’'))
    main_typ = f'''#import "gabarit.typ": *
#set document(title: {chaine_typst(p['titre'])},
  description: "{p['sous_titre']}. Faits gelés au {p['date']}; reprise datée et errata du 29 octobre 2026, actualisation du {ACTUALISATION} et relecture du {RELECTURE} en annexe.",
  keywords: ("veille technologique", "agents", "interopérabilité", "orchestration", "MCP", "A2A"))
#show: note.with(titre-court: "Veille technologique", pied: [Faits gelés au {p['date']} · actualisation du {ACTUALISATION}])
// légendes au-dessus des tableaux, comme dans l'édition d'origine, et jamais seules
// en bas de page
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.caption.where(position: top): it => block(sticky: true, it)
#couverture(surtitre: [Veille technologique], titre: {typo(p['titre'])},
  sous-titre: {typo(p['sous_titre'])}, auteur: {chaine_typst(AUTEUR)}, date: {chaine_typst(p['date'])},
  fiche: include "fiche.typ")
#sommaire()
#include "corps.typ"
// références : en drapeau, comme dans l'édition d'origine (URL longues)
#[#set par(justify: false, linebreaks: "simple")
#include "references.typ"]
#include "reprise.typ"
#[#set par(justify: false, linebreaks: "simple")
#include "references-reprise.typ"]
#pagebreak(weak: true)
#include "actualisation.typ"
#[#set par(justify: false, linebreaks: "simple")
#include "references-actualisation.typ"]
'''
    source = ' '.join(texte_controle(t) for t in (p['titre'], p['sous_titre'], fiche, texte, annexe, refs_annexe))
    # quatre fragments : corps, références, annexe de la reprise, ses références
    a = texte.index('<h2>Références</h2>')
    b = texte.index('<h2>Annexe : reprise du 29 octobre 2026</h2>')
    c = texte.index('<h3>Références de la reprise</h3>')
    assert a < b < c
    fragments = poser_liens_internes({
        'fiche': fiche, 'corps': texte[:a], 'references': texte[a:b], 'reprise': texte[b:c],
        'references-reprise': texte[c:], 'actualisation': annexe, 'references-actualisation': refs_annexe,
    })
    composer(fragments, main_typ, OUT, source)


if __name__ == '__main__':
    main()
