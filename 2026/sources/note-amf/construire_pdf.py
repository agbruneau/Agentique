"""Compose le PDF de la Note AMF IA à partir de l'export HTML de Claude Docs.

Usage : python construire_pdf.py [source.html] [sortie.pdf]
        (par défaut : note-amf-ia.html -> ../../documents/Note AMF IA.pdf)

Chaîne commune : sources/commun/composer.py. Le script retire de l'HTML la page de
titre et la fiche signalétique pour les poser sur la couverture, et remplace le
calendrier intégré (absent de l'export) par la figure de calendrier.typ.

Actualisation des 1er et 11 novembre 2026 et relecture du 11 novembre 2026 : annexe H,
rédigée en HTML dans ce dossier (actualisation-2026-11.html), composée après l'annexe G;
les corrections du corps sont faites à leur place dans note-amf-ia.html et consignées
au tableau H.3.
"""
import html, pathlib, re, sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
from composer import AUTEUR, DOCUMENTS, actualisation, chaine_typst, composer, date_fr, texte_html

ACTUALISATION = date_fr(2026, 11, 11)
RELECTURE = date_fr(2026, 11, 11)

SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ICI / 'note-amf-ia.html'
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else DOCUMENTS / 'Note AMF IA.pdf'
# AUTEUR vient de composer : la mention @u_… de l'export ne se résout pas hors de Claude Docs


def decouper(s):
    titre = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
    sous_titre = re.search(r'<p><em>(.*?)</em></p>', s[titre.end():], re.S)
    date = re.search(r'<time[^>]*datetime="(\d{4})-(\d{2})-(\d{2})"', s)
    fiche = re.search(r'<table>.*?</table>', s, re.S)
    assert titre.start() < fiche.start() and 'Rubrique' in fiche.group(0)
    corps = s[fiche.end():]
    corps, n = re.subn(r'<figure data-embed="[^"]*">.*?</figure>', '<div data-typst="calendrier()"></div>', corps, flags=re.S)
    assert n == 1, f'{n} figure(s) intégrée(s); calendrier.typ n\'en dessine qu\'une'
    return dict(titre=html.unescape(titre.group(1)), sous_titre=html.unescape(sous_titre.group(1)),
                date=date_fr(*(int(x) for x in date.groups())),
                fiche='<div class="fiche">' + fiche.group(0) + '</div>', corps=corps)


def main():
    p = decouper(SRC.read_text(encoding='utf8'))
    typo = lambda t: chaine_typst(t.replace("'", '’'))
    main_typ = f'''#import "gabarit.typ": *
#set document(title: {chaine_typst(p['titre'])},
  description: "Profil d'application québécois CRE-IA-2026-01-QC (version 1.0, {p['date']}; actualisation du {ACTUALISATION} et relecture du {RELECTURE} à l'annexe H)",
  keywords: ("AMF", "intelligence artificielle", "agents", "CRE-IA-2026-01-QC"))
#show: note.with(titre-court: "Note AMF IA", pied: [CRE-IA-2026-01-QC · version 1.0 · actualisation du {ACTUALISATION}])
#couverture(surtitre: [Note d'instruction · CRE-IA-2026-01-QC], titre: {typo(p['titre'])},
  sous-titre: {typo(p['sous_titre'])}, auteur: {chaine_typst(AUTEUR)}, date: {chaine_typst(p['date'])},
  fiche: include "fiche.typ")
#sommaire()
#include "corps.typ"
// annexe H : tableaux numérotés H.1, H.2… dans leur légende (les tableaux du corps n'ont
// pas de légende), sans la numérotation de Typst
#[#set figure(numbering: none)
#include "actualisation.typ"]
#[#set par(justify: false, linebreaks: "simple")
#include "references-actualisation.typ"]
'''
    # l'en-tête de la fiche (« Rubrique », « Valeur ») n'est pas repris sur la couverture
    # l'actualisation et la relecture passent en dernières lignes de la fiche
    ajouts = (f'<tr><td>Actualisation</td><td>1er et {ACTUALISATION}, annexe H</td></tr>'
              f'<tr><td>Relecture</td><td>{RELECTURE} : corrections du corps faites à leur place, '
              f'consignées à l&#39;annexe H (tableau H.3)</td></tr></tbody>')
    p['fiche'] = p['fiche'].replace('</tbody>', ajouts, 1)
    assert 'Actualisation' in p['fiche'] and 'Relecture' in p['fiche']
    fiche = re.sub(r'<thead>.*?</thead>', '', p['fiche'], flags=re.S)
    annexe, refs_annexe = actualisation(ICI)
    source = ' '.join(texte_html(t) for t in (p['titre'], p['sous_titre'], fiche, p['corps'], annexe, refs_annexe))
    composer({'fiche': p['fiche'], 'corps': p['corps'], 'actualisation': annexe,
              'references-actualisation': refs_annexe}, main_typ, OUT, source,
             extras=[ICI / 'calendrier.typ'])


if __name__ == '__main__':
    main()
