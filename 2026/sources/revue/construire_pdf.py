"""Recompose le PDF de la Revue de littérature à partir de son édition d'origine.

Usage : python construire_pdf.py [source.pdf] [sortie.pdf] [--html extrait.html]
        (par défaut : l'édition d'origine, lue dans git au commit ORIGINE, recomposée
        dans documents/Revue de littérature.pdf; --html garde l'extraction)

Aucune source amont n'est versée au dépôt (README, « Documents absents du dépôt ») :
le PDF fait foi, corrections du 29 oct. 2026 comprises. sources/commun/extraire.py
le relit (PDF balisé; repli géométrique pour l'annexe du 29 octobre, fusionnée sans
balisage), puis sources/commun/composer.py le recompose avec le gabarit commun.

Particularités traitées ici :
  - page de titre : titre, sous-titre, auteur et date passent sur la couverture, la
    mention de révision dans la fiche;
  - Résumé et Abstract : leur intitulé en gras devient un titre; l'Abstract est
    composé en anglais (césure);
  - titres : sections (H1) en chapitres, sous-sections (H2) en sections du gabarit;
  - légendes « Tableau N. – … » : la numérotation passe à Typst (même suite, contrôlée);
  - gras : celui de la police seulement. Le PDF balise en Strong des passages composés
    en romain (résumé, mentions des références); le rendu d'origine fait foi.

Actualisation du 11 novembre 2026 (prolongeant celle du 1er novembre) : annexe datée,
rédigée en HTML dans ce dossier (actualisation-2026-11.html), composée après l'annexe du
29 octobre; ses tableaux et ses références continuent les suites du document (tableau 12,
référence 193).

Relecture du 11 novembre 2026 (prolongeant celle du 3 novembre) : ses corrections du corps
sont faites à leur place par corrections.py, sur le corps extrait, et consignées en annexe,
dans le tableau que la fiche nomme; les DOI du tableau 14 y reçoivent des points de coupure
(couper_doi).
"""
import atexit, html, pathlib, re, shutil, subprocess, sys, tempfile

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
SORTIE = DOCUMENTS / 'Revue de littérature.pdf'
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
# aucun. L'en-tête du tableau 11 répété en tête de la p. 63 est absorbé par l'extraction,
# qui le soustrait au contrôle; « excep-/tions », coupé entre les p. 62 et 63 dans une
# cellule, s'y recolle donc.
ECARTS_CONNUS = {}


def page_de_titre(pdf):
    """Titre (15 pt), sous-titre (12 pt), ligne auteur · courriel · date, mention de révision."""
    lignes = [(round(l['spans'][0]['size']), ''.join(s['text'] for s in l['spans']).strip())
              for b in pymupdf.open(pdf)[0].get_text('dict')['blocks'] for l in b.get('lines', [])]
    titre = next(t for s, t in lignes if s == 15)
    sous_titre = next(t for s, t in lignes if s == 12)
    auteur, courriel, date = next(t for s, t in lignes if '·' in t and '@' in t).split(' · ')
    revision = next(t for s, t in lignes if t.startswith('Révision du'))
    return dict(titre=titre, sous_titre=sous_titre, auteur=auteur, courriel=courriel, date=date, revision=revision)


def corps(blocs, p):
    # la page de titre : bloc du titre et mention de révision, repris sur la couverture
    assert p['titre'] in blocs[0].html and p['revision'] in blocs[1].html, 'page de titre inattendue'
    h = [b.html for b in blocs[2:]]
    # Résumé, Abstract : intitulé en gras de tête -> titre; l'Abstract court jusqu'au
    # premier chapitre
    for i, b in enumerate(h):
        m = re.match(r'<p><strong>(Résumé|Abstract)</strong> ', b)
        if m:
            h[i] = f'<h2>{m.group(1)}</h2>\n<p>' + b[m.end():]
    debut = next(i for i, b in enumerate(h) if b.startswith('<h2>Abstract'))
    fin = next(i for i, b in enumerate(h) if i > debut and b.startswith('<h2>'))
    h[debut:fin] = [h[debut].split('\n', 1)[0], '<div lang="en">', *h[debut:fin], '</div>']
    h[debut + 2] = h[debut + 2].split('\n', 1)[1]
    # relecture du 3 novembre 2026 : corrections faites à leur place (corrections.py)
    s = corriger('\n'.join(h))
    # légendes : « Tableau N. – » laisse la place à la numérotation de Typst
    nums = [int(n) for n in re.findall(r'<caption>Tableau\xa0(\d+)\.\xa0– ', s)]
    assert nums == list(range(1, len(nums) + 1)) and s.count('<caption>') == len(nums), nums
    return re.sub(r'<caption>Tableau\xa0\d+\.\xa0– ', '<caption>', s)


def couper_doi(annexe):
    """Tableau 14 : un DOI long, sans point de coupure, débordait sur la colonne des dates.
    Une espace sans chasse après chaque « / », « . » et « - » lui permet de passer à la
    ligne; le contrôle de complétude n'y voit qu'une coupure de mot de plus."""
    debut = annexe.index('<caption>Les trente-six pièces sans attestation en notice')
    fin = annexe.index('</table>', debut)
    t = re.sub(r'<code>10\.[^<]+</code>', lambda m: re.sub(r'(?<=[/.\-])', '​', m.group(0)[6:-7]).join(('<code>', '</code>')),
               annexe[debut:fin])
    assert t.count('​') > 100, 'tableau 14 : DOI introuvables'
    return annexe[:debut] + t + annexe[fin:]


def poser_liens_internes(fiche, texte, annexe, refs_annexe):
    """O-17 : pose des ancres id="sec-...", id="tab-...", id="ref-..." sur les titres de
    section, les tableaux et les entrées bibliographiques, puis convertit tous les appels [n],
    renvois de section et de tableau en liens internes HTML <a href="#..."> résolus dans le PDF."""
    sections = set()

    def ancrer_titre(m):
        tag, num, reste = m.group(1), m.group(2), m.group(3)
        sec_id = 'sec-' + num.replace('.', '-')
        sections.add(num)
        return f'<{tag} id="{sec_id}">{num}{reste}</{tag}>'

    texte = re.sub(r'<(h[23])>(\d+(?:\.\d+)?)( [^<]+)</\1>', ancrer_titre, texte)
    # Identifiants ASCII sur tous les autres titres h2/h3/h4 pour éviter tout nameddest accentué dans la TDM
    extra_sec = 0

    def ancrer_autre_titre(m):
        nonlocal extra_sec
        extra_sec += 1
        return f'<{m.group(1)} id="sec-h-{extra_sec}">{m.group(2)}</{m.group(1)}>'

    texte = re.sub(r'<(h[234])>([^<]+)</\1>', ancrer_autre_titre, texte)
    annexe = re.sub(r'<(h[234])>([^<]+)</\1>', ancrer_autre_titre, annexe)
    refs_annexe = re.sub(r'<(h[234])>([^<]+)</\1>', ancrer_autre_titre, refs_annexe)

    # Ancres sur les 19 tableaux numérotés (11 dans texte, 8 dans annexe)
    tab_num = 0
    tableaux = set()

    def ancrer_table(m):
        nonlocal tab_num
        tab_num += 1
        tableaux.add(str(tab_num))
        return f'<table id="tab-{tab_num}">{m.group(1)}<caption>'

    texte = re.sub(r'<table>(\s*)<caption>', ancrer_table, texte)
    annexe = re.sub(r'<table>(\s*)<caption>', ancrer_table, annexe)
    assert tab_num == 19, f'19 tableaux attendus, {tab_num} trouvés'

    # Ancres sur les entrées bibliographiques [1]..[192] dans texte et [193]..[260] dans refs_annexe
    ref_num = 0
    refs = set()

    def ancrer_li(m):
        nonlocal ref_num
        ref_num += 1
        refs.add(str(ref_num))
        return f'<li id="ref-{ref_num}">'

    debut_refs = re.search(r'<h2[^>]*>Références</h2>', texte).start()
    fin_refs = texte.index('</ol>', debut_refs)
    texte = texte[:debut_refs] + re.sub(r'<li>', ancrer_li, texte[debut_refs:fin_refs]) + texte[fin_refs:]
    assert ref_num == 192, f'192 références initiales attendues, {ref_num} trouvées'
    refs_annexe = re.sub(r'<li>', ancrer_li, refs_annexe)
    assert ref_num == 260, f'260 références totales attendues, {ref_num} trouvées'

    def sec_href(s):
        return '#sec-' + s.replace('.', '-')

    def lier_segment(seg):
        # 1. Appels bibliographiques [n] et plages [a-b]
        seg = re.sub(
            r'\[(\d+)\]',
            lambda m: f'<a href="#ref-{m.group(1)}">[{m.group(1)}]</a>' if m.group(1) in refs else m.group(0),
            seg,
        )
        seg = re.sub(
            r'\[(\d+)([-–])(\d+)\]',
            lambda m: (f'[<a href="#ref-{m.group(1)}">{m.group(1)}</a>{m.group(2)}'
                       f'<a href="#ref-{m.group(3)}">{m.group(3)}</a>]')
            if m.group(1) in refs and m.group(3) in refs else m.group(0),
            seg,
        )
        # 2. Renvois de tableaux : « tableau N », « tableaux N et M », « tableaux N à M »
        seg = re.sub(
            r'\b([Tt]ableaux)(\s+)(\d+)(\s+(?:et|à)\s+)(\d+)\b',
            lambda m: (f'<a href="#tab-{m.group(3)}">{m.group(1)}{m.group(2)}{m.group(3)}</a>'
                       f'{m.group(4)}<a href="#tab-{m.group(5)}">{m.group(5)}</a>')
            if m.group(3) in tableaux and m.group(5) in tableaux else m.group(0),
            seg,
        )
        seg = re.sub(
            r'\b([Tt]ableau)(\s+)(\d+)\b',
            lambda m: f'<a href="#tab-{m.group(3)}">{m.group(0)}</a>' if m.group(3) in tableaux else m.group(0),
            seg,
        )
        # 3. Renvois explicites de sections : « section X.Y », « sections X.Y et Z.W », « sections X à Y »
        seg = re.sub(
            r'\b([Ss]ections)(\s+)(\d+(?:\.\d+)?)((?:,\s*\d+(?:\.\d+)?)*)(\s+(?:et|à)\s+)(\d+(?:\.\d+)?)\b',
            lambda m: (
                f'<a href="{sec_href(m.group(3))}">{m.group(1)}{m.group(2)}{m.group(3)}</a>'
                + re.sub(
                    r'\d+(?:\.\d+)?',
                    lambda sm: f'<a href="{sec_href(sm.group(0))}">{sm.group(0)}</a>'
                    if sm.group(0) in sections else sm.group(0),
                    m.group(4),
                )
                + m.group(5)
                + (f'<a href="{sec_href(m.group(6))}">{m.group(6)}</a>' if m.group(6) in sections else m.group(6))
            ) if m.group(3) in sections else m.group(0),
            seg,
        )
        seg = re.sub(
            r'\b([Ss]ection)(\s+)(\d+(?:\.\d+)?)\b',
            lambda m: f'<a href="{sec_href(m.group(3))}">{m.group(0)}</a>' if m.group(3) in sections else m.group(0),
            seg,
        )
        # 4. Renvois de sous-sections entre parenthèses ou après préposition : (2.2), (2.1, 2.2), (3.1, 17), en 11.1
        seg = re.sub(
            r'(?<=\()(\d+\.\d+)(?:,\s*(\d+(?:\.\d+)?))?(?=\))',
            lambda m: (
                f'<a href="{sec_href(m.group(1))}">{m.group(1)}</a>'
                + (f', <a href="{sec_href(m.group(2))}">{m.group(2)}</a>'
                   if m.group(2) and m.group(2) in sections else (f', {m.group(2)}' if m.group(2) else ''))
            ) if m.group(1) in sections else m.group(0),
            seg,
        )
        seg = re.sub(
            r'(?<=\()(\d+)(?=\))',
            lambda m: f'<a href="{sec_href(m.group(1))}">{m.group(1)}</a>'
            if m.group(1) in sections and int(m.group(1)) in {3, 13, 15, 17, 18} else m.group(0),
            seg,
        )
        seg = re.sub(
            r'\b(en|qu’en)(\s+)(\d+\.\d+)\b',
            lambda m: f'{m.group(1)}{m.group(2)}<a href="{sec_href(m.group(3))}">{m.group(3)}</a>'
            if m.group(3) in sections else m.group(0),
            seg,
        )
        return seg

    def transformer_html(doc):
        # Ne jamais toucher l'intérieur de <a ...>...</a>, <code>...</code>, <h2...>...</h2>, <h3...>...</h3> ou d'une balise HTML
        parties = re.split(r'(<a\b[^>]*>.*?</a>|<code>.*?</code>|<h[23]\b[^>]*>.*?</h[23]>|<[^>]+>)', doc, flags=re.S)
        for i in range(0, len(parties), 2):
            parties[i] = lier_segment(parties[i])
        return ''.join(parties)

    return (
        transformer_html(fiche),
        transformer_html(texte),
        transformer_html(annexe),
        transformer_html(refs_annexe),
    )


def main():
    blocs = extraire(SRC, niveaux={1: 2, 2: 3}, styles_balises={'Em': 'em', 'Code': 'code'})
    brut = vers_html(blocs)
    if HTML:
        HTML.write_text(brut, encoding='utf8')
    # complétude : chaque mot du texte courant d'origine (hors marges et table des
    # matières) doit se retrouver dans l'extraction
    manque, _ = controler_extraction(SRC, brut, ecarter=zones_ecartees(SRC))
    inexplique = {m: n for m, n in manque.items() if n > ECARTS_CONNUS.get(m, 0)}
    if inexplique:
        sys.exit(f'extraction incomplète : {inexplique}')
    print(f'extraction : {len(blocs)} blocs, écarts connus seulement ({sum(manque.values())} mots)')

    p = page_de_titre(SRC)
    # l'auteur signe sous sa forme canonique (« André-Guy Bruneau, M.Sc. IT » à l'origine)
    assert p['auteur'].startswith('André-Guy Bruneau'), p['auteur']
    p['auteur'] = AUTEUR
    texte = corps(blocs, p)
    # sous-titre : majuscules à la française, comme la page de titre de la Veille (audit
    # du 11 novembre 2026, coquille « Orchestration Agentiques »)
    assert p['sous_titre'] == 'Interopérabilité et Orchestration Agentiques', p['sous_titre']
    p['sous_titre'] = 'Interopérabilité et orchestration agentiques'
    revision = p['revision'].removeprefix('Révision du ').strip()
    annexe, refs_annexe = actualisation(ICI)
    annexe = couper_doi(annexe)
    fiche = ('<div class="fiche"><table><tbody>'
             f'<tr><td>Auteur</td><td>{html.escape(p["auteur"])} · {html.escape(p["courriel"])}</td></tr>'
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
  keywords: ("revue de littérature", "agents", "interopérabilité", "orchestration", "arXiv"))
#show: note.with(titre-court: "Revue de littérature", pied: [Faits gelés au {p['date']} · actualisation du {ACTUALISATION}])
// légendes au-dessus des tableaux, comme dans l'édition d'origine, et jamais seules
// en bas de page
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.caption.where(position: top): it => block(sticky: true, it)
#couverture(surtitre: [Revue de littérature], titre: {typo(p['titre'])},
  sous-titre: {typo(p['sous_titre'])}, auteur: {chaine_typst(p['auteur'])}, date: {chaine_typst(p['date'])},
  fiche: include "fiche.typ")
#sommaire()
#include "corps.typ"
#pagebreak(weak: true)
#include "actualisation.typ"
#[#set par(justify: false, linebreaks: "simple")
#include "references-actualisation.typ"]
'''
    fiche, texte, annexe, refs_annexe = poser_liens_internes(fiche, texte, annexe, refs_annexe)
    source = ' '.join(texte_controle(t) for t in (p['titre'], p['sous_titre'], fiche, texte, annexe, refs_annexe))
    composer({'fiche': fiche, 'corps': texte, 'actualisation': annexe, 'references-actualisation': refs_annexe},
             main_typ, OUT, source)


if __name__ == '__main__':
    main()
