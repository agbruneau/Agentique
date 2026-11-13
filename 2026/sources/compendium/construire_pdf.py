"""Recompose le PDF du Compendium à partir de son édition d'origine.

Usage : python construire_pdf.py [source.pdf] [sortie.pdf] [--html extrait.html]
        (par défaut : l'édition d'origine, lue dans git au commit ORIGINE, recomposée
        dans documents/Compendium.pdf; --html garde l'extraction brute)

Aucune source amont n'est versée au dépôt (README, « Documents absents du dépôt ») :
le PDF Typst du 24 oct. 2026 fait foi. sources/commun/extraire.py le relit (PDF balisé),
puis sources/commun/composer.py le recompose avec le gabarit commun.

Particularités traitées ici :
  - page de titre : surtitre, titre, sous-titre, auteur et édition vont sur la couverture;
    la mention « Livrable du dépôt » (pied de la table des matières d'origine) et les
    dates de gel et de compilation vont dans la fiche; la présentation des cinq livres et
    l'exergue forment une page liminaire, avant le sommaire;
  - table des matières d'origine (balisée en Div et Link, non en TOC) : écartée, le
    gabarit en régénère une;
  - structure : les cinq livres (page d'ouverture « L I V R E / I / Coopérer ») passent
    au niveau 1, les chapitres (H1, précédés de « C H A P I T R E / n ») au niveau 2 sous
    la forme « n · titre », les sections H2, H3 et H4 aux niveaux 3, 4 et 5; les deux
    annexes (« A N N E X E ») passent au niveau 1 et leurs sections remontent d'un cran;
  - figures (118, dessins vectoriels Typst : cadres, flèches et texte) : chacune est rendue
    en PNG à 200 dpi depuis sa zone de page et insérée à sa place, sous sa légende
    d'origine; son texte, devenu image, est repris dans le texte de remplacement (alt);
  - légendes « Figure n.n — » et « Tableau n.n — » : numérotation d'origine (par chapitre)
    gardée telle quelle, celle de Typst désactivée; les légendes de tableau égarées en
    paragraphe rejoignent leur tableau;
  - encadrés « Thèse — … » de tête de chapitre (balisés comme un paragraphe) : en citation;
  - titres balisés en paragraphe gras : promus d'après les signets d'origine (912, tous
    retrouvés dans l'ordre);
  - balisage abîmé par des retouches directes du PDF d'origine : l'extracteur commun
    traite éléments vides, étiquettes de liste porteuses de texte, en-têtes de tableau
    répétés, haut de page rattaché au mauvais bloc et lignes de cellule dans la colonne
    voisine; la sous-classe Extracteur ajoute les paragraphes balisés dans le tableau qui
    les suit et la bibliographie de l'annexe I (p. 941-1000), relue par sa géométrie;
  - adresses : coupables à leurs traits d'union (U+200B), sans césure, contrôlées à part;
  - traces de production (plan de rédaction, décisions et garde-fous, portes, remontées,
    lots de travail) : retirées du corps et de la fiche par retraits.py, sur le texte
    extrait, avant composition.

Contrôles laissés dans le code : complétude de l'extraction (écarts connus listés),
figures (texte dans la zone rendue, zone sans mot étranger), colonnes de tableau, ordre
du texte par page, structure du corps (livres, chapitres, annexes, légendes), retraits
comptés et aucune trace de production restante, contrôle mot à mot de composer(),
adresses d'un seul tenant.

Actualisation du 1er novembre 2026 : annexe N, rédigée en HTML dans ce dossier
(actualisation-2026-11.html) et composée après l'annexe I, hors retraits.py; tableaux
numérotés N.1, N.2…, références [AN-1]… Elle ne modifie pas le corps.
"""
import atexit, collections, dataclasses, html, pathlib, re, shutil, subprocess, sys, tempfile, time

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / 'commun'))
import composer as composer_mod
import corrections
import extraire as extraire_mod
import retraits
from composer import ACTUALISATION, AUTEUR, DOCUMENTS, NBSP, actualisation, chaine_typst, composer, date_fr, mots
from extraire import ECARTES, controler_extraction, texte_controle, vers_html
import pymupdf

args = sys.argv[1:]
HTML = pathlib.Path(args.pop(args.index('--html') + 1)) if '--html' in args else None
args = [a for a in args if a != '--html']
SORTIE = DOCUMENTS / 'Compendium.pdf'
# Édition d'origine (Typst 0.15.1, compilée le 24 oct. 2026) : le PDF recomposé ne doit
# pas servir de source à son tour.
ORIGINE = 'd28324a'
OUT = pathlib.Path(args[1]) if len(args) > 1 else SORTIE
TMP = pathlib.Path(tempfile.mkdtemp())
atexit.register(shutil.rmtree, TMP, True)
if args:
    SRC = pathlib.Path(args[0])
else:
    SRC = TMP / 'origine.pdf'
    SRC.write_bytes(subprocess.run(['git', 'show', f'{ORIGINE}:documents/{SORTIE.name}'], cwd=DOCUMENTS,
                                   capture_output=True, check=True).stdout)

# Date de gel : README (tableau des livrables, « Gel au 27 juill. 2026 »); le PDF ne la
# porte pas sur sa page de titre. La date de compilation vient des métadonnées du PDF.
GEL = '27 juillet 2026'
DPI = 200
# Adresses : avec schéma, ou domaine suivi d'un chemin (cloudsecurityalliance.org/…)
ZWSP = '\u200b'
URL = r'(?:https?://|\b[\w-]+(?:\.[\w-]+)+/)\S*'
# En-tête courant à y 6-17 pt, folio des ouvertures de livre à y 752 et de chapitre à
# y 775; le texte courant descend jusqu'à y 744 (p. 152, 165) : marges du gabarit
# commun (60, 60) trop larges en bas.
MARGES = (30, 45)
# Bibliographie de l'annexe I, relue par sa géométrie (Extracteur.lire_biblio)
PAGES_BIBLIO = range(940, 1000)
# Justification d'origine (x de 85 à 533 pt) : la largeur d'une figure s'y rapporte.
JUSTIF_ORIGINE = 448

# Écarts connus du contrôle de complétude (mots du PDF d'origine absents de l'extraction).
# Le texte des figures est compté à part (il passe dans l'image). Reste « don-/née »,
# coupé au saut des p. 71-72 : en fin de page, le contrôle recolle une césure du texte
# courant au mot suivant du flux, ici un autre (« Le »); le mot entier est bien dans
# l'extraction. Enfin, l'en-tête du tableau des mesures de l'annexe I, répété en haut de
# la p. 941 (« Mesure Valeur ») : une fois dans l'extraction, deux fois dans le PDF.
ECARTS_CONNUS = dict.fromkeys('don née mesure valeur'.split(), 1)
# Lignes de cellule encore hors de leur colonne après recolonner() (controler_colonnes) :
#  - p. 905, dernière rangée du tableau des lacunes : retouche directe du PDF d'origine,
#    dont le texte de la 3e colonne est dessiné sous la 1re (« instruite, non close —
#    révision du 6 juillet… ») et la 4e (« ch. 17 § 17.1 ») reste seule à sa place.
COLONNES_CONNUES = ('p. 905, colonne 3 : « ch. 17 § 17.1',)


# ---- figures ------------------------------------------------------------------------

@dataclasses.dataclass(eq=False)
class Figure:
    page: int
    cle: tuple
    bbox: pymupdf.Rect      # zone du texte balisé
    clip: pymupdf.Rect = None   # zone rendue : texte et dessins
    numero: int = 0
    runs: list = dataclasses.field(default_factory=list)

    @property
    def fichier(self):
        return f'figure-{self.numero:03d}.png'


def inventorier_figures(doc):
    """Éléments Figure de l'arborescence : page, clé (chemin d'index), zone. La zone rendue
    s'étend aux dessins (cadres, flèches, fonds) qui touchent le texte de la figure."""
    figures = []
    for p in doc:
        def marcher(b, chemin):
            if b['type'] != 2:
                return
            cle = chemin + (b['index'],)
            if 'Figure' in (b.get('raw'), b.get('std')):
                figures.append(Figure(p.number, cle, pymupdf.Rect(b['bbox'])))
                return
            for c in b.get('blocks', []):
                marcher(c, cle)
        for b in p.get_text('dict', flags=pymupdf.TEXT_COLLECT_STRUCTURE)['blocks']:
            marcher(b, ())
    for i, f in enumerate(figures, 1):
        f.numero = i
        p = doc[f.page]
        clip = pymupdf.Rect(f.bbox)
        dessins = [d['rect'] for d in p.get_drawings()]
        change = True
        while change:   # un cadre peut en toucher un autre (fond, puis bordure)
            change = False
            for r in dessins:
                if r.intersects(clip + (-3, -3, 3, 3)) and not r in clip and r.height < 0.8 * p.rect.height:
                    clip |= r
                    change = True
        f.clip = (clip + (-2, -2, 2, 2)) & p.rect
    return figures


CORBEL = r'C:\Windows\Fonts\corbel.ttf'
CORBEL_B = r'C:\Windows\Fonts\corbelb.ttf'

PATCHS_FIGURES = {
    1: ([(95.0, 666.0, 440.0, 675.0)],
        [((95.04, 672.16), "Aucun agent à exploiter dans la matière pré-agentique. Posé en entier au § 1.0.2, éprouvé au Livre IV (ch. 38-40).", 7.0, False, 0x4d4d4d)]),
    9: ([(84.5, 284.5, 445.0, 304.0)],
        [((85.04, 291.01), "La formulation la plus citée est celle d'Anthropic (2024, § 4.1.1), et sa reprise massive par la littérature praticienne", 7.0, False, 0x4d4d4d),
         ((85.04, 301.02), "en fait une convention de vocabulaire largement adoptée.", 7.0, False, 0x4d4d4d)]),
    16: ([(94.5, 415.5, 120.0, 424.0), (84.5, 444.0, 440.0, 463.0)],
         [((95.04, 421.25), "ch. 9 § 9.2.5, ch. 17 § 17.4, ch. 24 § 24.5", 6.2, False, 0x737373),
          ((85.04, 450.26), "Deux axes seulement disposent de protocoles stabilisés — le vertical et l'horizontal. Les deux autres sont traités ailleurs dans la somme.", 7.0, False, 0x4d4d4d)]),
    17: ([(84.5, 420.0, 475.0, 449.0)],
         [((85.04, 426.29), "LES DEUX SÉQUENCES SONT INVERSES L'UNE DE L'AUTRE, et c'est le fait le plus instructif de la section : la flèche «", 7.0, False, 0x4d4d4d),
          ((85.04, 436.29), "agent-outil -> agent-agent -> infrastructure » souvent supposée est fausse dans les deux lectures. Le cinquième", 7.0, False, 0x4d4d4d),
          ((85.04, 446.30), "protocole, celui de transaction, n'est pas de ce décompte.", 7.0, False, 0x4d4d4d)]),
    20: ([(84.5, 628.0, 145.0, 670.0), (262.5, 628.0, 326.0, 659.0)],
         [((85.04, 634.04), "primitives de base et", 7.0, False, 0x4d4d4d),
          ((85.04, 645.04), "racines ; transports", 7.0, False, 0x4d4d4d),
          ((85.04, 656.04), "local et HTTP à deux", 7.0, False, 0x4d4d4d),
          ((85.04, 667.04), "points d'accès", 7.0, False, 0x4d4d4d),
          ((263.06, 634.04), "sollicitation ; serveur", 7.0, False, 0x4d4d4d),
          ((263.06, 645.04), "qualifié serveur de", 7.0, False, 0x4d4d4d),
          ((263.06, 656.04), "ressources", 7.0, False, 0x4d4d4d)]),
    31: ([(84.5, 251.0, 235.0, 259.0)],
         [((85.04, 256.59), "QUATRE JALONS DOCUMENTÉS, ET AUCUNE CONTINUITÉ", 6.5, True, 0x9a3b12)]),
    32: ([(329.5, 371.5, 531.0, 381.5)],
         [((330.06, 378.52), "« Une entité capable d'accorder l'accès à une ressource protégée »", 6.7, True, 0x212121)]),
    34: ([(329.5, 74.0, 535.0, 84.0), (84.5, 196.0, 440.0, 204.5)],
         [((330.06, 81.03), "Aucun établissement financier réglementé, nommément", 8.0, True, 0x212121),
          ((85.04, 202.04), "C'est une ABSENCE DE DOCUMENTATION, non un fait négatif vérifié (troisième degré). Elle ne soutient en", 7.0, False, 0x4d4d4d)]),
    38: ([(84.5, 297.5, 470.0, 316.5)],
         [((85.04, 303.71), "Le passeport est un OBJET DE SYNTHÈSE CONSTRUIT PAR LA SOMME : le socle ne le documente dans aucune des", 7.0, False, 0x4d4d4d),
          ((85.04, 313.71), "spécifications relevées (degré 3). Les quatre pièces existent séparément ; leur assemblage est un énoncé d'auteur.", 7.0, False, 0x4d4d4d)]),
    40: ([(401.5, 626.0, 425.0, 633.5)],
         [((394.5, 631.38), "F-04/F-07, [A]", 6.2, False, 0x737373)]),
    42: ([(401.5, 128.5, 485.0, 136.5), (401.5, 233.5, 500.0, 251.5)],
         [((402.07, 134.03), "[B, degré 2] — non ratifiée", 6.2, False, 0x737373),
          ((402.07, 239.04), "[B, degré 3] — une offre, pas une norme", 6.2, False, 0x737373)]),
    45: ([(84.5, 53.5, 252.0, 61.5)],
         [((85.04, 59.02), "CINQ MAILLONS, QUATRE QUESTIONS EN DÉFAUT (Q-A À Q-D, PLUS LA COMPOSITION)", 6.5, True, 0x9a3b12)]),
    # [V1-40] Figure 22.1 : les deux rangées de la grille nommées par l'axe « qui commande »
    50: ([(84.5, 518.0, 240.0, 526.5)],
         [((85.04, 524.6), "DEUX AXES : QUI SAIT, ET QUI COMMANDE — EN HAUT, LES AGENTS COMMANDENT ; EN BAS, LE CADRE", 6.5, True, 0x9a3b12)]),
    53: ([(94.5, 224.5, 126.0, 233.0), (105.5, 369.5, 195.0, 379.5)],
         [((95.04, 230.62), "OO4/OO3", 7.0, True, 0x9a3b12),
          ((106.04, 376.64), "Humain dans la boucle", 8.5, True, 0x212121)]),
    57: ([(84.5, 295.0, 260.0, 314.5), (306.5, 282.0, 358.0, 290.5), (84.5, 325.0, 445.0, 343.5)],
         [((85.04, 300.94), "le texte est arrêté ; aucune attente nouvelle du Bureau", 7.0, False, 0x4d4d4d),
          ((85.04, 311.94), "n'en découle encore", 7.0, False, 0x4d4d4d),
          ((307.06, 287.94), "Date de prise d'effet", 7.0, True, 0x212121),
          ((85.04, 330.94), "La date de prise d'effet est celle de l'ENTRÉE EN VIGUEUR, non celle de la publication : entre les deux, une institution n'a aucune", 7.0, False, 0x4d4d4d),
          ((85.04, 340.94), "attente nouvelle du Bureau — et après, ces attentes prennent effet sans que le texte ait changé d'un mot.", 7.0, False, 0x4d4d4d)]),
    59: ([(94.5, 541.5, 195.0, 549.5)],
         [((95.04, 547.19), "prend effet le 1er mai 2027 — ch. 25", 6.2, False, 0x737373)]),
    60: ([(105.5, 134.0, 198.0, 177.5), (250.5, 134.0, 341.0, 177.5), (395.5, 122.0, 488.0, 177.5), (84.5, 163.0, 450.0, 182.0)],
         [((106.04, 135.5), "que la décision a été rendue, au plus", 6.0, False, 0x4d4d4d),
          ((106.04, 141.5), "tard lorsqu'on informe la personne —", 6.0, False, 0x4d4d4d),
          ((106.04, 147.5), "l'information l'accompagne", 6.0, False, 0x4d4d4d),
          ((251.05, 135.5), "1° les renseignements utilisés ;", 6.0, False, 0x4d4d4d),
          ((251.05, 141.5), "2° les raisons, facteurs et paramètres ;", 6.0, False, 0x4d4d4d),
          ((251.05, 147.5), "3° le droit de faire rectifier", 6.0, False, 0x4d4d4d),
          ((396.07, 129.03), "Présenter ses observations", 8.0, True, 0x212121),
          ((396.07, 135.5), "l'occasion de présenter ses observations", 6.0, False, 0x4d4d4d),
          ((396.07, 141.5), "à un membre du personnel en mesure", 6.0, False, 0x4d4d4d),
          ((396.07, 147.5), "de réviser la décision", 6.0, False, 0x4d4d4d),
          ((85.04, 171.0), "La troisième information due sur demande — LE DROIT DE FAIRE RECTIFIER — fait partie de l'énumération,", 6.8, False, 0x4d4d4d),
          ((85.04, 180.0), "et l'alinéa distinct est le seul que le socle individualise : il est hors de l'énumération, non son quatrième terme.", 6.8, False, 0x4d4d4d)]),
    61: ([(105.5, 136.0, 295.0, 155.5), (323.5, 136.0, 512.0, 155.5)],
         [((106.04, 140.0), "les obligations du § 27.2 se déclenchent et", 6.5, False, 0x4d4d4d),
          ((106.04, 147.2), "l'information accompagne la communication", 6.5, False, 0x4d4d4d),
          ((324.06, 140.0), "selon l'analyse d'un cabinet — nuance déterminante", 6.5, False, 0x4d4d4d),
          ((324.06, 147.2), "pour les systèmes agentiques, et non tranchée", 6.5, False, 0x4d4d4d)]),
    62: ([(94.5, 280.0, 236.0, 323.5), (383.5, 264.0, 415.0, 274.0), (324.5, 280.0, 491.0, 300.0)],
         [((95.04, 286.04), "Au plus tard au moment où l'entreprise informe la", 6.8, False, 0x4d4d4d),
          ((95.04, 297.05), "personne de la décision — sans demande préalable.", 6.8, False, 0x4d4d4d),
          ((95.04, 311.05), "la décision et sa communication doivent être des", 6.2, False, 0x737373),
          ((95.04, 321.05), "événements émis, identifiables et datés", 6.2, False, 0x737373),
          ((384.07, 271.04), "Présenter ses observations", 8.0, True, 0x212121),
          ((325.06, 286.04), "L'occasion de présenter ses observations à un membre du", 7.0, False, 0x4d4d4d),
          ((325.06, 297.05), "personnel en mesure de réviser la décision.", 7.0, False, 0x4d4d4d)]),
    63: ([(246.5, 68.0, 294.0, 78.0), (322.5, 81.0, 368.0, 89.5)],
         [((254.0, 75.03), "Tiers TIC", 8.5, True, 0x212121),
          ((315.0, 87.03), "dès qu'il décide ou oriente", 6.5, False, 0x4d4d4d)]),
    64: ([(258.5, 390.0, 368.0, 400.0), (247.5, 442.5, 343.0, 450.5), (412.5, 390.0, 490.0, 400.0)],
         [((259.05, 397.17), "Publié, prise d'effet à venir", 8.5, True, 0x212121),
          ((248.05, 448.18), "E-23 et AMF — prennent effet le 1er mai 2027", 6.0, False, 0x737373),
          ((413.07, 397.17), "Sans date d'effet propre", 8.5, True, 0x212121)]),
    74: ([(84.5, 567.5, 215.0, 575.5)],
         [((85.04, 573.03), "DIX INSTITUTIONS (DOUZE ENTRÉES AU SOCLE), TROIS CLASSES D'ACCÈS", 6.5, True, 0x9a3b12)]),
    75: ([(94.5, 473.0, 196.0, 550.0), (412.5, 457.0, 494.0, 466.5)],
         [((95.04, 478.79), "Deux titulaires reconstatés au", 6.8, False, 0x4d4d4d),
          ((95.04, 489.80), "corps (une responsable mondiale", 6.8, False, 0x4d4d4d),
          ((95.04, 500.80), "depuis mai 2026, § 35.4 ; un chef", 6.8, False, 0x4d4d4d),
          ((95.04, 511.80), "de groupe depuis févr. 2026,", 6.8, False, 0x4d4d4d),
          ((95.04, 522.80), "§ 35.3) et un troisième déclaré à", 6.8, False, 0x4d4d4d),
          ((95.04, 533.80), "l'entrée initiale (§ 35.2).", 6.8, False, 0x4d4d4d),
          ((95.04, 547.80), "§ 35.2, § 35.3, § 35.4", 6.2, False, 0x737373),
          ((413.07, 463.79), "Rien sur mandat ni architecture", 7.8, True, 0x212121)]),
    76: ([(84.5, 690.0, 465.0, 698.5)],
         [((85.04, 696.13), "L'ERREUR DE CONCEPTION À PROSCRIRE est de laisser le non-déterminisme remonter au-dessus de la première couche. L'autorisation est", 7.0, False, 0x4d4d4d)]),
    84: ([(84.5, 53.5, 255.0, 61.5), (324.5, 160.0, 460.0, 185.0), (84.5, 230.0, 476.0, 258.5)],
         [((85.04, 59.02), "TROIS DÉRIVES DU SOCLE ET UNE QUATRIÈME SOURCE RELEVÉE (FRONT OUVERT)", 6.5, True, 0x9a3b12),
          ((336.06, 167.03), "Quatrième source (front ouvert)", 8.0, True, 0x212121),
          ((325.06, 182.04), "Mémoire réécrite par modèles auxiliaires — relève [C] hors socle.", 6.8, False, 0x4d4d4d),
          ((85.04, 236.04), "LES QUATRE NE SONT PAS DOCUMENTÉES AU MÊME DEGRÉ. Une seule est instruite par un chapitre ; une n'est pas au socle et le mot", 7.0, False, 0x4d4d4d),
          ((85.04, 246.04), "ne doit pas faire croire l'inverse ; une est nommée par les cadres sans être instrumentée ; la quatrième est portée par une relève [C]", 7.0, False, 0x4d4d4d),
          ((85.04, 256.04), "hors socle (front ouvert).", 7.0, False, 0x4d4d4d)]),
    90: ([(84.5, 466.5, 410.0, 485.0)],
         [((85.04, 472.31), "La boucle suppose que la dérive soit DÉTECTÉE, or le ch. 39 § 39.2 établit que la dérive d'autonomie n'est pas instrumentée", 7.0, False, 0x4d4d4d),
          ((85.04, 482.31), "au socle, que la dérive de modèle n'est pas au socle et que la quatrième source reste un front ouvert.", 7.0, False, 0x4d4d4d)]),
    91: ([(84.5, 235.0, 172.0, 274.0), (197.5, 295.0, 495.0, 325.5), (84.5, 382.5, 305.0, 390.5)],
         [((85.04, 240.97), "E-23 — gouvernance et", 7.0, True, 0x212121),
          ((85.04, 251.97), "surveillance", 7.0, True, 0x212121),
          ((85.04, 270.97), "Ligne directrice IA de l'AMF", 7.0, True, 0x212121),
          ((198.05, 300.98), "substrat typé de", 6.5, False, 0x4d4d4d),
          ((198.05, 311.98), "frontière (inférence)", 6.5, False, 0x4d4d4d),
          ((310.06, 300.98), "cartes signées =", 6.5, False, 0x4d4d4d),
          ((310.06, 311.98), "identité d'appelant", 6.5, False, 0x4d4d4d),
          ((423.07, 300.98), "—", 7.0, True, 0x212121),
          ((85.04, 387.98), "— aucun lien documenté au socle (15 croisements). Se reporter au Tableau 42.1 pour chaque cellule.", 6.2, False, 0x737373)]),
    94: ([(84.5, 355.0, 446.0, 383.5)],
         [((85.04, 361.05), "LE DÉCOUPAGE EST UNE CONSTRUCTION DE LA SOMME ; sa vertu est d'obliger à dire au Tableau 43.1 ce que chaque couche", 7.0, False, 0x4d4d4d),
          ((85.04, 371.05), "tient et ce qu'elle ne porte pas. Quatre réserves commandent la lecture du tableau source (§ 43.1.2).", 7.0, False, 0x4d4d4d)]),
    95: ([(105.5, 281.5, 490.0, 314.5), (386.5, 250.5, 462.0, 279.5), (84.5, 310.5, 416.0, 329.5)],
         [((106.04, 283.0), "un cadre déterministe fait le", 6.0, False, 0x4d4d4d),
          ((106.04, 289.0), "travail, à coût prévisible et", 6.0, False, 0x4d4d4d),
          ((106.04, 295.0), "chemin testable — ch. 22 § 22.5", 6.0, False, 0x4d4d4d),
          ((251.05, 283.0), "le non-déterminisme apporte une", 6.0, False, 0x4d4d4d),
          ((251.05, 289.0), "valeur, et l'encadrement en", 6.0, False, 0x4d4d4d),
          ((251.05, 295.0), "borne le domaine — OO3 ou OO4", 6.0, False, 0x4d4d4d),
          ((387.07, 256.63), "au seuil d'irréversibilité", 6.8, True, 0x9a3b12),
          ((396.07, 276.63), "Ne pas franchir", 8.5, True, 0x212121),
          ((396.07, 283.0), "autorisation et règlement", 6.0, False, 0x4d4d4d),
          ((396.07, 289.0), "restent déterministes —", 6.0, False, 0x4d4d4d),
          ((396.07, 295.0), "ch. 36 § 36.2.1", 6.0, False, 0x4d4d4d),
          ((85.04, 318.0), "La grille est un CRITÈRE D'AUTEUR : le socle ne porte pas de règle d'abstention. Elle réordonne ce que les chapitres", 6.8, False, 0x4d4d4d),
          ((85.04, 327.0), "établissent — elle n'ajoute pas d'exigence, et elle ne dispense d'aucune.", 6.8, False, 0x4d4d4d)]),
    97: ([(401.5, 510.0, 420.0, 518.0)],
         [((402.07, 515.52), "ch. 45 § 45.7", 6.2, False, 0x737373)]),
    98: ([(84.5, 588.5, 476.0, 684.0)],
         [((85.04, 594.47), "Common / Business", 7.0, True, 0x212121),
          ((198.05, 594.47), "Role, Actor,", 7.0, False, 0x4d4d4d),
          ((198.05, 605.47), "Collaboration", 7.0, False, 0x4d4d4d),
          ((310.06, 594.47), "Process, Function,", 7.0, False, 0x4d4d4d),
          ((310.06, 605.47), "Service, Event", 7.0, False, 0x4d4d4d),
          ((423.07, 594.47), "Object (Business Object)", 7.0, False, 0x4d4d4d),
          ((85.04, 624.47), "Application", 7.0, True, 0x212121),
          ((198.05, 624.47), "Component, Interface,", 7.0, False, 0x4d4d4d),
          ((198.05, 635.47), "Collaboration", 7.0, False, 0x4d4d4d),
          ((310.06, 624.47), "Service, Function, Flow", 7.0, False, 0x4d4d4d),
          ((423.07, 624.47), "Object (Data Object)", 7.0, False, 0x4d4d4d),
          ((85.04, 654.47), "Technology", 7.0, True, 0x212121),
          ((198.05, 654.47), "Node, Device", 7.0, False, 0x4d4d4d),
          ((310.06, 654.47), "Technology Service", 7.0, False, 0x4d4d4d),
          ((423.07, 654.47), "Artifact", 7.0, False, 0x4d4d4d),
          ((85.04, 681.47), "En v4, Common est transverse, Physical rejoint Technology et Interaction est retiré ; aucun élément « agent ».", 6.2, False, 0x737373)]),
    99: ([(84.5, 377.5, 215.0, 385.5)],
         [((85.04, 383.25), "SEPT PATRONS DE MODÉLISATION ET LE REGISTRE DES STÉRÉOTYPES", 6.5, True, 0x9a3b12)]),
    101: ([r for k in range(8) for r in ((111.5, 256.0 + 45 * k, 250.0, 266.5 + 45 * k), (94.5, 267.0 + 45 * k, 250.0, 278.5 + 45 * k))],
          [((112.04, 262.93), "Socle d'exécution et souveraineté", 8.5, True, 0x212121),
           ((95.04, 275.93), "Cloud Pak for Integration v16.1, MZR Toronto et Montréal, Sovereign Core.", 7.0, False, 0x4d4d4d),
           ((112.04, 307.94), "Observabilité et opérations", 8.5, True, 0x212121),
           ((95.04, 320.94), "Instana (observabilité agentique en préversion publique), OpenTelemetry natif.", 7.0, False, 0x4d4d4d),
           ((112.04, 352.94), "Gouvernance IA et risque de modèle", 8.5, True, 0x212121),
           ((95.04, 365.94), "watsonx.governance, Compliance Accelerators — ch. 25, ch. 42.", 7.0, False, 0x4d4d4d),
           ((112.04, 397.94), "Couche agentique", 8.5, True, 0x212121),
           ((95.04, 410.95), "watsonx Orchestrate (MCP et A2A), Granite 4.0 — ch. 22, ch. 23.", 7.0, False, 0x4d4d4d),
           ((112.04, 442.95), "Données", 8.5, True, 0x212121),
           ((95.04, 455.95), "Data Fabric et accès gouverné — ch. 5, ch. 24 § 24.4.", 7.0, False, 0x4d4d4d),
           ((112.04, 487.95), "Messagerie et événements", 8.5, True, 0x212121),
           ((95.04, 500.95), "IBM MQ 9.4 LTS, Event Endpoint Management, Confluent.", 7.0, False, 0x4d4d4d),
           ((112.04, 532.96), "Intégration applicative et B2B", 8.5, True, 0x212121),
           ((95.04, 545.96), "App Connect Enterprise v13.0, webMethods Hybrid Integration.", 7.0, False, 0x4d4d4d),
           ((112.04, 577.96), "Exposition et gouvernance des interactions", 8.5, True, 0x212121),
           ((95.04, 590.96), "API Connect v10.0.8, API Agent, DataPower Nano Gateway, ContextForge.", 7.0, False, 0x4d4d4d)]),
    103: ([(443.5, 403.0, 502.0, 433.5)],
          [((444.07, 409.17), "point d'arrêt et trace", 6.8, False, 0x4d4d4d),
           ((444.07, 420.17), "outillant l'art. 12.1", 6.8, False, 0x4d4d4d),
           ((444.07, 431.18), "(personne habilitée)", 6.8, False, 0x4d4d4d)]),
    105: ([(84.5, 151.0, 232.0, 159.0), (443.5, 186.5, 510.0, 206.5)],
          [((85.04, 156.66), "UNE CHAÎNE D'ORCHESTRATION RÉGULÉE (SOUSCRIPTION VIE ET SINISTRES)", 6.5, True, 0x9a3b12),
           ((444.07, 192.66), "point d'arrêt humain", 6.8, False, 0x4d4d4d),
           ((444.07, 203.66), "avant décision (art. 12.1)", 6.8, False, 0x4d4d4d)]),
    106: ([(84.5, 289.5, 511.0, 348.0)],
          [((85.04, 295.24), "T − 3", 6.5, True, 0x9a3b12),
           ((85.04, 321.25), "Inventorier", 7.0, True, 0x212121),
           ((85.04, 334.25), "premier mouvement —", 6.8, False, 0x4d4d4d),
           ((85.04, 345.25), "§ 46.2.2", 6.8, False, 0x4d4d4d),
           ((196.05, 295.24), "T − 2", 6.5, True, 0x9a3b12),
           ((196.05, 321.25), "Coter, puis encadrer", 7.0, True, 0x212121),
           ((196.05, 334.25), "deuxième mouvement —", 6.8, False, 0x4d4d4d),
           ((196.05, 345.25), "§ 46.2.3", 6.8, False, 0x4d4d4d),
           ((307.06, 295.24), "T − 1", 6.5, True, 0x9a3b12),
           ((307.06, 321.25), "Surveiller", 7.0, True, 0x212121),
           ((307.06, 334.25), "troisième mouvement —", 6.8, False, 0x4d4d4d),
           ((307.06, 345.25), "§ 46.2.4", 6.8, False, 0x4d4d4d),
           ((419.07, 295.24), "1er mai 2027", 6.5, True, 0x9a3b12),
           ((419.07, 321.25), "Prise d'effet E-23 / AMF", 7.0, True, 0x212121),
           ((419.07, 334.25), "institutions financières", 6.8, False, 0x4d4d4d),
           ((419.07, 345.25), "(278 jours depuis le gel)", 6.8, False, 0x4d4d4d)]),
    107: ([(258.5, 473.5, 293.0, 483.5)],
          [((259.05, 480.45), "Projeté", 8.5, True, 0x212121)]),
    112: ([(381.0, 360.5, 391.0, 370.0), (250.0, 370.0, 275.0, 378.5)],
          [((250.05, 375.86), "échoue (x)", 7.0, False, 0x4d4d4d),
           ((380.0, 367.86), "->", 7.0, True, 0x9a3b12)]),
    113: ([(258.5, 613.0, 301.0, 622.5), (84.5, 694.0, 440.0, 702.5)],
          [((259.05, 619.8), "PROJETÉ", 8.5, True, 0x212121),
           ((85.04, 699.81), "LE CÔNE S'ÉLARGIT AVEC LE TEMPS (2027-2032), et la discipline qui en découle est la REDATATION : un énoncé prospectif se relit à sa", 7.0, False, 0x4d4d4d)]),
    114: ([(84.5, 583.5, 205.0, 591.5), (306.5, 605.5, 322.0, 613.5), (84.5, 685.5, 481.0, 704.0)],
          [((85.04, 589.23), "LA GRAPPE DE 2027 (PROGRAMMÉ) ET L'HORLOGE DE FOND 2028-2035 (PROJETÉ)", 6.5, True, 0x9a3b12),
           ((307.06, 611.23), "2030/2035", 6.5, True, 0x9a3b12),
           ((85.04, 691.24), "LA GRAPPE DE 2027 CONCENTRE LES ENGAGEMENTS PROGRAMMÉS ; L'HORLOGE 2028-2035 PORTE AUSSI DES JALONS PROJETÉS (NIST IR 8547).", 6.8, False, 0x4d4d4d),
           ((85.04, 701.24), "Une date opposable peut être reportée (§ 49.1.4). La frise distingue engagements fermes et cibles projetées.", 6.8, False, 0x4d4d4d)]),
    115: ([(105.5, 317.0, 185.0, 327.5), (94.5, 330.0, 185.0, 376.5),
           (258.5, 317.0, 344.0, 327.5), (247.5, 330.0, 344.0, 376.5),
           (412.5, 317.0, 495.0, 327.5), (401.5, 330.0, 495.0, 376.5)],
          [((106.04, 323.98), "Convergence / fragmentation", 7.8, True, 0x212121),
           ((95.04, 338.98), "Écosystèmes de protocoles ou", 6.8, False, 0x4d4d4d),
           ((95.04, 349.98), "coexistence stratifiée — § 49.2.", 6.8, False, 0x4d4d4d),
           ((95.04, 363.98), "le verrou est la portabilité neutre", 6.2, False, 0x737373),
           ((259.05, 323.98), "Intensité réglementaire", 7.8, True, 0x212121),
           ((248.05, 338.98), "Grappe de 2027, gouvernance et", 6.8, False, 0x4d4d4d),
           ((248.05, 349.98), "responsabilité — § 49.1, 49.3, 49.10.", 6.8, False, 0x4d4d4d),
           ((248.05, 363.98), "fermeté des échéances et du régime", 6.2, False, 0x737373),
           ((413.07, 323.98), "Souveraineté / ouverture", 7.8, True, 0x212121),
           ((402.07, 338.98), "Souveraineté, menace et horloge", 6.8, False, 0x4d4d4d),
           ((402.07, 349.98), "post-quantique — § 49.4, 49.5, 49.7.", 6.8, False, 0x4d4d4d),
           ((402.07, 363.98), "localisation et migration cryptographique", 6.2, False, 0x737373)]),
    116: ([(84.5, 534.0, 235.0, 542.0), (94.5, 557.0, 228.0, 566.5), (94.5, 620.5, 177.0, 638.0), (448.5, 557.0, 532.0, 566.5)],
          [((85.04, 539.72), "QUATORZE ÉVÉNEMENTS DU TABLEAU 50.1 ILLUSTRÉS PAR TROIS ÉTATS TYPES", 6.5, True, 0x9a3b12),
           ((95.04, 563.72), "agent-outil", 6.5, True, 0x9a3b12),
           ((142.04, 563.72), "Révisions protocolaires", 8.2, True, 0x212121),
           ((95.04, 625.73), "survenu côté MCP (revalidé le 30", 6.2, False, 0x737373),
           ((95.04, 635.73), "juill. 2026) ; A2A inchangé", 6.2, False, 0x737373),
           ((449.07, 563.72), "Désignation de l'organisme", 7.2, True, 0x212121)]),
    117: ([(210.5, 439.0, 271.0, 483.5)],
          [((211.05, 446.14), "Extraction et socle", 8.0, True, 0x212121),
           ((211.05, 459.14), "extrait à la source ;", 6.8, False, 0x4d4d4d),
           ((211.05, 470.14), "l'entrée S-nnn de", 6.8, False, 0x4d4d4d),
           ((211.05, 481.14), "l'annexe B est amendée", 6.8, False, 0x4d4d4d)]),
    118: ([(84.5, 234.5, 330.0, 242.5), (366.5, 285.0, 480.0, 304.5), (366.5, 405.0, 488.0, 424.5)],
          [((85.04, 239.93), "VUE SYNTHÉTIQUE PAR LIVRE DU GEL UNIQUE (27 JUILLET 2026) ET EXEMPLES D'ÉVÉNEMENTS", 6.5, True, 0x9a3b12),
           ((367.06, 290.94), "révisions protocolaires (MCP payé ch. 8) ;", 6.8, False, 0x4d4d4d),
           ((367.06, 301.94), "gouvernance AP2 (ch. 10) ; Assistants API", 6.8, False, 0x4d4d4d),
           ((367.06, 410.95), "suivi du transfert AP2 (§ 49.3.1, § 49.9) et", 6.8, False, 0x4d4d4d),
           ((367.06, 421.95), "registre des 14 événements (Tableau 50.1)", 6.8, False, 0x4d4d4d)]),
}


def rendre_figures(doc, figures, dossier):
    for f in figures:
        p = doc[f.page]
        # [V1-48 / V2-05] Restaure la bordure droite des cartes en 2e colonne rognée par le clip d'origine à x=530.08
        for d in p.get_drawings():
            if d['rect'].intersects(f.clip) and d.get('color') and d['rect'].x1 > 530.5:
                p.draw_line((530.08, d['rect'].y0), (530.08, d['rect'].y1),
                            color=d['color'], width=d.get('width') or 0.9)
        if f.numero in PATCHS_FIGURES:
            redacts, inserts = PATCHS_FIGURES[f.numero]
            for r in redacts:
                p.add_redact_annot(pymupdf.Rect(*r), fill=False)
            p.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)
            for pt, txt, size, bold, col in inserts:
                c = ((col >> 16) / 255, ((col >> 8) & 255) / 255, (col & 255) / 255)
                p.insert_text(pt, txt, fontsize=size, fontfile=CORBEL_B if bold else CORBEL, color=c)
        pix = p.get_pixmap(dpi=DPI, clip=f.clip)
        pix.set_dpi(DPI, DPI)
        pix.save(dossier / f.fichier)


class Extracteur(extraire_mod.Extracteur):
    """Extracteur commun, plus les figures : leur texte est retiré de l'arborescence à la
    lecture de la page (il passe dans l'image, et recaser() ne doit pas le redistribuer),
    et l'élément Figure se rend en <figure><img>."""

    def __init__(self, pdf, figures, **params):
        super().__init__(pdf, **params)
        self.figures = {f.cle: f for f in figures}
        self.par_page = collections.defaultdict(list)
        for f in figures:
            self.par_page[f.page].append(f)
        self.ancetres = {f.cle[:k] for f in figures for k in range(1, len(f.cle))}
        self.biblio = self.liste_biblio = None   # élément en cours de la bibliographie relue

    def lire_page(self, page):
        ok = super().lire_page(page)
        for f in self.par_page.get(page.number, []):
            pile = [f.cle]
            while pile:
                n = self.noeuds[pile.pop()]
                f.runs += [r for r in n.runs if r.page == page.number]
                n.runs = [r for r in n.runs if r.page != page.number]
                pile += n.enfants
            # texte dessiné dans la figure mais balisé dans l'élément voisin (p. 788 :
            # « § 45.7 », rangé dans le paragraphe suivant) : il suit la figure
            for n in self.noeuds.values():
                egares = [r for r in n.runs if r.page == page.number and pymupdf.Rect(r.bbox) in f.clip]
                if egares:
                    self.ecarts.append(f'p. {page.number + 1} : « {self.texte_runs(egares)[:60]} », balisé hors '
                                       f'de la figure {f.numero} qui le dessine, rendu avec elle')
                    f.runs += egares
                    n.runs = [r for r in n.runs if r not in egares]
        if page.number in PAGES_BIBLIO:
            self.lire_biblio(page)
        return ok

    def lire_biblio(self, page):
        """Bibliographie de l'annexe I (p. 941-1000) : l'arborescence y range chaque page
        dans un seul item de liste, puces, titres de lettre et entrées confondus, et
        recaser() en disperse les lignes. La page est relue par sa géométrie, hors du
        tableau balisé qui la précède (p. 941) : titre (gras, 13 pt et plus), entrée (ligne
        qui commence par une puce), alinéa (ligne en retrait), suite (toute autre ligne :
        l'entrée ou l'alinéa en cours, d'une page à l'autre)."""
        p = page.number
        tableau = [r for k, n in self.noeuds.items() if n.role == 'Table' for r in self.runs_de(k) if r.page == p]
        haut = min((r.bbox[1] for r in tableau), default=0)
        bas = max((r.bbox[3] for r in tableau), default=0)
        dans = lambda r: haut - 1 <= r.bbox[1] and r.bbox[3] <= bas + 2
        entete = []
        for n in self.noeuds.values():
            # le tableau garde ses lignes, balisées ou non (p. 941 : valeurs retouchées
            # « 134 » et « 1065 », hors arborescence, que recaser() remet en cellule)
            entete += [r for r in n.runs if r.page == p and r.bbox[3] < haut - 1]
            n.runs = [r for r in n.runs if r.page != p or r in tableau or dans(r)]
        if any(r.texte.strip() for r in entete):
            # p. 941 : en-tête du tableau répété en haut de page, hors arborescence
            self.ecarts.append(f'p. {p + 1} : en-tête de tableau répété écarté (« {self.texte_runs(entete)[:40]} »)')
        liens = [(l['from'], l['uri']) for l in page.get_links() if l.get('kind') == pymupdf.LINK_URI]
        runs = [r for b in page.get_text('dict', flags=extraire_mod.STRUCTURE & ~pymupdf.TEXT_COLLECT_STRUCTURE)['blocks']
                if b['type'] == 0 for r in self.spans(page, b, liens) if r.bbox[3] > bas + 2]
        racine = self.racines[0]
        nouveau = lambda role, parent: self.noeud(('biblio', p, len(self.noeuds)), role, parent).cle
        lignes = self.lignes_visuelles([r for r in runs if r.texte.strip()])
        gauche = min((l[0].bbox[0] for l in lignes), default=0)
        for l in lignes:
            t = self.texte_runs(l)
            if all(r.flags & 16 for r in l) and max(r.taille for r in l) >= 13:
                niveau = 2 if max(r.taille for r in l) >= 16 else 3   # I.1 / I.2, lettres
                if self.biblio and self.biblio[0] == 'titre' and self.biblio[2] == p:
                    cle = self.biblio[1]          # titre sur deux lignes
                else:
                    cle = nouveau(f'H{niveau}', racine)
                self.biblio = ('titre', cle, p)
            elif t.startswith('•'):
                if not (self.biblio and self.biblio[0] == 'item'):
                    self.liste_biblio = nouveau('L', racine)
                cle = nouveau('LI', self.liste_biblio)
                l = [r for r in l if r.texte.strip() != '•']
                if l and l[0].texte.lstrip().startswith('•'):
                    l[0].texte = l[0].texte.lstrip()[1:].lstrip()
                self.biblio = ('item', cle, p)
            elif self.biblio and (self.biblio[0] == 'item' or
                                  self.biblio[0] == 'p' and l[0].bbox[0] <= gauche + 10):
                cle = self.biblio[1]
            else:
                cle = nouveau('P', racine)
                self.biblio = ('p', cle, p)
            self.noeuds[cle].runs += l

    def sortir_du_tableau(self, table):
        """Texte dessiné au-dessus de l'en-tête d'un tableau mais balisé dans ses rangées
        (p. 597, 763, 803, 822, 841, 851, 901, 904, 940 : paragraphe ou légende qui précède
        le tableau) : il en sort, en paragraphes placés avant lui (un alinéa en retrait
        ouvre un paragraphe)."""
        trs = list(self.rangees(table))
        if not trs:
            return
        for p in sorted({r.page for r in self.runs_de(table)}):
            tete = [r for r in self.runs_de(trs[0]) if r.page == p and r.texte.strip()]
            if not tete:
                continue
            y0 = min(r.bbox[1] for r in tete)
            dessus = [r for tr in trs[1:] for r in self.runs_de(tr) if r.page == p and r.bbox[3] < y0 - 1]
            if not any(r.texte.strip() for r in dessus):
                continue
            for r in dessus:
                self.noeuds[self.proprietaire(r)].runs.remove(r)
            lignes = self.lignes_visuelles(dessus)
            gauche = min(l[0].bbox[0] for l in lignes)
            alineas = []
            for l in lignes:
                if not alineas or l[0].bbox[0] > gauche + 8:
                    alineas.append([])
                alineas[-1] += l
            # juste avant le tableau (ou l'ancêtre qui le porte dans sa section)
            ancetre = table
            while self.noeuds[ancetre].parent is not None and \
                    self.noeuds[self.noeuds[ancetre].parent].role not in extraire_mod.SECTIONS:
                ancetre = self.noeuds[ancetre].parent
            parent = self.noeuds[ancetre].parent or ancetre
            for a in alineas:
                hote = parent + (len(self.noeuds), 'retouche')
                self.noeuds[hote] = extraire_mod.Noeud(hote, 'P', parent)
                freres = self.noeuds[parent].enfants
                freres.insert(freres.index(ancetre), hote)
                self.feuilles.add(hote)
                for r in a:
                    # les éléments en ligne de la cellule (Strong d'en-tête…) ne valent pas
                    # pour lui : son style vient de la police (gras, italique)
                    r.bloc, r.en_ligne = hote, ()
                    self.noeuds[hote].runs.append(r)
            self.ecarts.append(f'p. {p + 1} : {len(alineas)} paragraphe(s) balisé(s) dans le tableau qui les '
                               f'suit, sorti(s) avant lui (« {self.texte_runs(lignes[0])[:50]} »)')

    def recaser(self):
        super().recaser()
        for cle in [k for k, n in self.noeuds.items() if n.role == 'Table']:
            self.sortir_du_tableau(cle)
            for _ in range(2):
                self.completer_rangees(cle)
                self.recolonner(cle)

    def rendre(self, cle, legende=None):
        f = self.figures.get(cle)
        if f:
            alt = re.sub(r'\s+', ' ', ' '.join(' '.join(r.texte for r in l) for l in self.lignes_visuelles(f.runs)))
            largeur = min(100, round(100 * f.clip.width / JUSTIF_ORIGINE))
            return (f'<figure data-figure="{f.numero}"><img src="{f.fichier}" width="{largeur}%" '
                    f'alt="{html.escape(alt.strip())}"></figure>')
        if cle in self.ancetres and not self.runs_de(cle):
            # conteneur sans texte propre : ses enfants, figure comprise
            return '\n'.join(h for c in self.noeuds[cle].enfants
                             if self.noeuds[c].role not in ECARTES and (h := self.rendre(c)))
        return super().rendre(cle, legende)


def controler_figures(doc, figures):
    """Chaque figure a du texte, et tout ce texte tient dans la zone rendue; la zone ne
    mord sur aucun mot étranger à la figure (légende, paragraphe voisin)."""
    fautes = []
    for f in figures:
        assert f.runs, f'figure {f.numero} (p. {f.page + 1}) sans texte'
        dehors = [r.texte for r in f.runs if not pymupdf.Rect(r.bbox) in f.clip + (-1, -1, 1, 1)]
        assert not dehors, f'figure {f.numero} (p. {f.page + 1}) : texte hors zone {dehors[:3]}'
        siens = [pymupdf.Rect(r.bbox) for r in f.runs]
        p = doc[f.page]
        intrus = [w[4] for w in p.get_text('words') if pymupdf.Rect(w[:4]).intersects(f.clip)
                  and w[1] > 60 and not any(pymupdf.Rect(w[:4]).intersects(s) for s in siens)]
        if intrus:
            fautes.append(f'figure {f.numero} (p. {f.page + 1}) : la zone {f.clip} mord sur {intrus[:8]}')
    assert not fautes, '\n'.join(fautes)


def controler_ordre(doc, brut, seuil=0.9):
    """Ordre du texte courant (corps 10 pt et plus : ni tableaux ni figures) : part des
    suites de cinq mots de chaque page d'origine retrouvées telles quelles dans
    l'extraction. Rend les pages sous le seuil."""
    norm = lambda t: re.findall(r'[^\W_]+', t.replace('\xad', '').lower())
    h = ' ' + ' '.join(norm(texte_controle(brut))) + ' '
    faibles = []
    for p in doc:
        lignes = [''.join(s['text'] for s in l['spans']) for b in p.get_text('dict')['blocks']
                  for l in b.get('lines', []) if l['spans'][0]['size'] >= 10
                  and MARGES[0] < l['bbox'][3] and l['bbox'][1] < p.rect.height - MARGES[1]]
        w = norm(re.sub(r'\xad\s*\n', '', '\n'.join(lignes)).replace('\n', ' '))
        suites = [' ' + ' '.join(w[i:i + 5]) + ' ' for i in range(0, max(0, len(w) - 5), 3)]
        if len(suites) >= 10:
            part = sum(s in h for s in suites) / len(suites)
            if part < seuil:
                faibles.append((p.number + 1, round(part, 2)))
    return faibles


def controler_colonnes(e):
    """Lignes de cellule qui commencent au début d'une autre colonne que la leur (début
    de colonne : le plus fréquent du rang, par page) : reste de balisage croisé."""
    restes = []
    for cle in [k for k, n in e.noeuds.items() if n.role == 'Table']:
        trs = [[c for c in e.noeuds[tr].enfants if e.noeuds[c].role in ('TD', 'TH')] for tr in e.rangees(cle)]
        lignes = [(j, l) for cells in trs for j, c in enumerate(cells)
                  for l in e.lignes_visuelles([r for r in e.runs_de(c) if r.texte.strip()])]
        cols = collections.defaultdict(collections.Counter)
        for j, l in lignes:
            cols[(l[0].page, j)][round(l[0].bbox[0])] += 1
        debut = {pj: c.most_common(1)[0][0] for pj, c in cols.items()}
        for j, l in lignes:
            p, x0 = l[0].page, l[0].bbox[0]
            autre = [jj for (pp, jj), x in debut.items() if pp == p and jj != j and abs(x - x0) < 3]
            if abs(debut[(p, j)] - x0) > 6 and autre:
                restes.append(f'p. {p + 1}, colonne {j + 1} : « {e.texte_runs(l)[:50]} »')
    return restes


# ---- structure ------------------------------------------------------------------------

ESPACE = lambda mot: ' '.join(mot)   # « L I V R E »


def strip(h):
    return re.sub(r'<[^>]+>', '', h).strip()


def surtitres(page):
    """Surtitres de la page de titre, en capitales espacées (« C O M P E N D I U M ») :
    une lettre par mot PyMuPDF; un blanc de plus de 5 pt sépare deux mots."""
    out = []
    for b in page.get_text('dict')['blocks'][:1]:
        for s in (s for l in b['lines'] for s in l['spans']):
            lettres = [w for w in page.get_text('words') if pymupdf.Rect(w[:4]).intersects(pymupdf.Rect(s['bbox']))]
            mot, mots_ = '', []
            for a, w in zip([None] + lettres, lettres):
                if a and w[0] - a[2] > 5:
                    mots_.append(mot)
                    mot = ''
                mot += w[4]
            mots_.append(mot)
            assert ' '.join(mots_).replace(' ', '') == s['text'].replace(' ', ''), s['text']
            out.append(' '.join(mots_).capitalize())
    return out


def page_de_titre(blocs, doc):
    """Page 1 : surtitres espacés, titre, sous-titre, auteur, édition, cinq livres, exergue."""
    h = vers_html([b for b in blocs if b.page == 0]).split('\n')
    assert len(h) == 11 and h[0].startswith('<p>' + ESPACE('COMPENDIUM')), h[:2]
    st = surtitres(doc[0])
    assert ' '.join(' '.join(x.upper()) for x in st).replace('   ', ' ') == strip(h[0]).replace('  ', ' '), st
    surtitre = ' · '.join(st)
    livres = [re.fullmatch(r'<p><strong>(Livre [IV]+ — [^<]+)</strong> (.+)</p>', x).groups() for x in h[5:10]]
    livres = [(t, d.replace('AgentMesh, AgentOps,', 'Maillage d’agents (<em>AgentMesh</em>), exploitation (<em>AgentOps</em>),')) for t, d in livres]
    assert h[10].startswith('<p><em>'), h[10]
    exergue = h[10].replace('cinq termes dont aucun ne supplée l’absence d’un autre',
                            'cinq exigences de gouvernance (adossées aux quatre termes de l’invariant du § 1.0.2) dont aucune ne supplée l’absence d’une autre').replace(
                            "cinq termes dont aucun ne supplée l'absence d'un autre",
                            "cinq exigences de gouvernance (adossées aux quatre termes de l’invariant du § 1.0.2) dont aucune ne supplée l’absence d’une autre")
    # auteur : forme canonique de composer (sans la virgule d'origine), contrôlée contre la p. 1
    assert strip(h[3]).replace(',', '') == AUTEUR, h[3]
    titre = strip(h[1]).replace('Interopérabilité et Orchestration en', 'Interopérabilité et orchestration en').replace(
        'Entreprise Agentique', 'entreprise agentique')
    return dict(surtitre=surtitre, titre=titre,
                sous_titre=strip(h[2]), auteur=AUTEUR, edition=strip(h[4]), livres=livres, exergue=exergue)


def promouvoir_titres(lignes, toc):
    """Les signets d'origine font foi pour les titres : un titre que l'arborescence
    balise en paragraphe gras (§ 44.0.4, § 45.4, I.1, I.2, lettres de l'annexe I) redevient
    un titre du niveau de son signet (signet n -> H n du PDF, rendu h n+1 comme les autres).
    Les signets se retrouvent dans l'ordre, chacun après le précédent."""
    norm = lambda t: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', t)).replace(NBSP, ' ')
                            .replace('’', "'")).strip()
    # espace insécable des signets lue « € » (0xA0 du PDFDocEncoding, mal décodé)
    signets = [(n, norm(t.replace('€', ' '))) for k, (n, t, _) in enumerate(toc) if k == 0 or toc[k - 1][:2] != [n, t]]
    titre = re.compile(r'<h(\d)>(.*)</h\1>')
    gras = re.compile(r'<p><strong>(?:<em>)?([^<]*)(?:</em>)?</strong></p>')
    out, i, promus = list(lignes), 0, []
    for n, t in signets:
        while i < len(out):
            m = titre.fullmatch(out[i]) or gras.fullmatch(out[i])
            if m and norm(m.group(m.lastindex)) == t:
                break
            i += 1
        else:
            raise AssertionError(f'signet introuvable dans le corps : {t}')
        if not out[i].startswith('<h'):
            out[i] = f'<h{n + 1}>{m.group(1)}</h{n + 1}>'
            promus.append(t)
        i += 1
    print(f'titres : {len(signets)} signets retrouvés, dont {len(promus)} balisés en paragraphe et promus')
    return out


def corps(blocs, p, toc):
    """Corps du livre (des livres aux annexes), et ce que la page de titre et la table des
    matières d'origine laissent à la fiche."""
    debut = next(i for i, b in enumerate(blocs) if b.html.startswith(f'<p>{ESPACE("LIVRE")}</p>'))
    avant = blocs[:debut]
    # avant le livre I : page de titre (p. 1) et table des matières (p. 2-14), dont seule
    # la mention « Livrable du dépôt » est du texte courant
    assert all(b.page is not None and b.page < 14 for b in avant), 'liminaires inattendus'
    statut = [l for l in vers_html(avant).split('\n') if l.startswith('<p><strong>Livrable du dépôt.</strong>')]
    assert len(statut) == 1
    # une ligne par élément de premier rang (les listes et les tableaux en comptent
    # plusieurs, sans effet sur les motifs cherchés ici)
    h = promouvoir_titres(vers_html(blocs[debut:]).split('\n'), toc)
    out, annexe, i = [], False, 0
    livres = chapitres = annexes = entetes = 0
    while i < len(h):
        b = h[i]
        if b == f'<p>{ESPACE("LIVRE")}</p>':
            num, titre, sous = h[i + 1:i + 4]
            num, titre = re.fullmatch(r'<p><strong>([IV]+)</strong></p>', num).group(1), strip(titre)
            assert sous.startswith('<p><em>'), sous
            out += [f'<h1>Livre {num} — {titre}</h1>', sous]
            livres += 1
            i += 4
            continue
        if b == f'<p>{ESPACE("CHAPITRE")}</p>':
            num = re.fullmatch(r'<p><strong>(\d+)</strong></p>', h[i + 1]).group(1)
            m = re.fullmatch(r'<h2>(.+)</h2>', h[i + 2])
            chapitres += 1
            assert m and int(num) == chapitres, (num, h[i + 2][:80])
            out.append(f'<h2>{num} · {m.group(1)}</h2>')
            i += 3
            continue
        if b == f'<p>{ESPACE("ANNEXE")}</p>':
            # titre d'annexe : H1 (Annexe I) ou paragraphe en gras (Annexe B, titre balisé
            # en P dans l'arborescence)
            m = re.fullmatch(r'<h2>(Annexe\s.+)</h2>|<p><strong>(Annexe\s[^<]+)</strong></p>', h[i + 1])
            assert m, h[i + 1][:80]
            out.append(f'<h1>{(m.group(1) or m.group(2)).replace(NBSP, " ")}</h1>')
            annexe, annexes = True, annexes + 1
            i += 2
            continue
        if annexe:   # sections d'annexe : un cran plus haut (h3 -> h2…)
            b = re.sub(r'<(/?)h([3-6])>', lambda m: f'<{m.group(1)}h{int(m.group(2)) - 1}>', b)
        m = re.fullmatch(r'<p><strong>([^<]+)</strong></p>', b)
        if m and out and out[-1].startswith('<table'):
            # reste d'en-tête répété que l'extracteur commun n'a pas absorbé (texte
            # étranger intercalé) : ses mots sont tous ceux de l'en-tête qui précède
            tete = re.sub(r'<[^>]+>|\s', '', out[-1].split('</thead>')[0]).lower()
            if all(x in tete for x in re.findall(r'\w+', html.unescape(m.group(1)).lower())):
                entetes += 1
                i += 1
                continue
        out.append(b)
        i += 1
    assert (livres, chapitres, annexes) == (5, 50, 2), (livres, chapitres, annexes)
    print(f"corps : {entetes} reste(s) d'en-tête de tableau répété écarté(s)")
    s = '\n'.join(out)
    # encadrés de thèse
    s, n = re.subn(r'<p><strong>Thèse</strong> —(.*?)</p>', r'<blockquote><p><strong>Thèse</strong> —\1</p></blockquote>', s)
    # légendes de figure : rejoignent l'image qui les suit (ou, à défaut, qui les précède)
    leg = r'<p>(<strong>Figure \d+\.\d+[a-z]?</strong> —(?:(?!</p>).)*)</p>'
    fig = r'<figure (data-figure="\d+")>(<img [^>]*>)</figure>'
    s = re.sub(leg + r'\n' + fig, r'<figure \2>\3<figcaption>\1</figcaption></figure>', s)
    s = re.sub(fig + r'\n' + leg, r'<figure \1>\2<figcaption>\3</figcaption></figure>', s)
    # légendes de tableau égarées dans un paragraphe, juste avant leur tableau
    s = re.sub(r'<p>(<strong>Tableau \d+\.\d+</strong> —(?:(?!</p>).)*)</p>\n<table>(?:<caption></caption>)?(?!<caption>)',
               r'<table><caption>\1</caption>', s)
    s = s.replace('<caption></caption>', '')
    # rangées entièrement vides (cellules vidées par une retouche du PDF : p. 849)
    s = re.sub(r'<tr>(?:<td></td>)+</tr>', '', s)
    return couper_adresses(s), statut[0]


def controler_corps(s, nb_figures):
    """Structure du corps : légendes en place, figures toutes posées et légendées."""
    figs = re.findall(r'<figure data-figure="(\d+)">(?:(?!</figure>).)*</figure>', s)
    assert [int(n) for n in figs] == list(range(1, nb_figures + 1)), 'figures manquantes ou en désordre'
    sans = re.findall(r'<figure data-figure="(\d+)"><img [^>]*></figure>', s)
    egarees = re.findall(r'<p><strong>(?:Figure|Tableau) \d+\.\d+[a-z]?</strong> —', s)
    nums = lambda k: re.findall(rf'<(?:figcaption|caption)><strong>{k} (\d+\.\d+[a-z]?)(?: <em>[^<]*</em>)?</strong>', s)
    return dict(figures=len(figs), figures_sans_legende=sans, legendes_egarees=len(egarees),
                legendes_figure=len(nums('Figure')), legendes_tableau=len(nums('Tableau')))


# ---- Typst ------------------------------------------------------------------------------

def pandoc_sans_images(fragment, dest, imports=()):
    """composer.pandoc(), plus deux retouches propres au Compendium :
      - il importe chaque fichier d'« extras » dans chaque fragment : les images en sont
        exclues (un PNG ne s'importe pas);
      - largeurs de colonnes : le plancher de filtre.lua (mot le plus long d'une ligne)
        dépasse parfois la justification à lui seul (identifiants draft-ietf-…, p. 148
        et 467 recomposées) : la somme est ramenée à 100 %, l'identifiant se coupant
        à ses traits d'union."""
    PANDOC(fragment, dest, [i for i in imports if i.endswith('.typ')])

    def ramener(m):
        parts = [float(x) for x in re.findall(r'([\d.]+)%', m.group(1))]
        if sum(parts) <= 100:
            return m.group(0)
        return 'columns: (' + ', '.join(f'{x * 100 / sum(parts):.2f}%' for x in parts) + ')'
    typ = dest.read_text(encoding='utf8')
    dest.write_text(re.sub(r'columns: \(((?:[\d.]+%,? ?)+)\)', ramener, typ), encoding='utf8')


def appeler_figures_et_tableaux(h):
    """[O-05] Appelle chaque figure et chaque tableau par son numéro dans le paragraphe
    de texte courant voisin lorsqu'aucun renvoi numéroté n'y figure encore."""
    lignes = h.split('\n')
    sans_cap = re.sub(r'<(?:caption|figcaption)>.*?</(?:caption|figcaption)>', '', h, flags=re.S)
    sans_fig = re.sub(r'<figure\b.*?</figure>', '', sans_cap, flags=re.S)
    for idx, l in enumerate(lignes):
        m_tab = re.search(r'^<table><caption><strong>Tableau ([\d.I]+[a-z]?)</strong>', l)
        m_fig = re.search(r'^<figure data-figure="\d+"><img [^>]*><figcaption><strong>Figure ([\d.]+[a-z]?)</strong>', l)
        if not m_tab and not m_fig:
            continue
        kind = 'Tableau' if m_tab else 'Figure'
        num = (m_tab or m_fig).group(1)
        if re.search(rf'\b{kind.lower()}[\s\u00a0]+{re.escape(num)}\b', sans_fig, flags=re.I):
            continue
        art = 'le' if kind == 'Tableau' else 'la'
        cible = None
        for j in range(idx - 1, max(-1, idx - 6), -1):
            if lignes[j].startswith('<p>') and lignes[j].endswith('</p>') and not lignes[j].startswith('<p><strong>'):
                cible = j
                break
        if cible is None:
            for j in range(idx + 1, min(len(lignes), idx + 6)):
                if lignes[j].startswith('<p>') and lignes[j].endswith('</p>') and not lignes[j].startswith('<p><strong>'):
                    cible = j
                    break
        if cible is not None:
            p = lignes[cible]
            if p.endswith('.</p>'):
                lignes[cible] = p[:-5] + f' ({art} {kind}\u00a0{num}).</p>'
            elif p.endswith(' :</p>'):
                lignes[cible] = p[:-6] + f' ({art} {kind}\u00a0{num})\u00a0:</p>'
            else:
                lignes[cible] = p[:-4] + f' ({art} {kind}\u00a0{num})</p>'
    return '\n'.join(lignes)


def couper_adresses(h):
    """Adresses du texte (hors balises et code) : une coupure possible (U+200B) après
    chaque trait d'union. Sans elle, filtre.lua met en boîte insécable le segment
    « a2a-protocol-surpasses-150-… » d'une adresse, qui déborde alors de la page."""
    morceaux = re.split(r'(<pre\b.*?</pre>|<code\b.*?</code>|<[^>]+>)', h, flags=re.S)
    return ''.join(m if i % 2 else re.sub(URL, lambda u: u.group(0).replace(ZWSP, '').replace('-', '-' + ZWSP), m)
                   for i, m in enumerate(morceaux))


PANDOC = composer_mod.pandoc
composer_mod.pandoc = pandoc_sans_images
DUREES = collections.defaultdict(float)


class Chrono:
    """subprocess de composer.py, chronométré par commande (pandoc, typst)."""
    def __getattr__(self, nom):
        return getattr(subprocess, nom)

    @staticmethod
    def run(cmd, *a, **k):
        t = time.time()
        try:
            return subprocess.run(cmd, *a, **k)
        finally:
            DUREES[pathlib.Path(cmd[0]).stem] += time.time() - t


composer_mod.subprocess = Chrono()


def main():
    t0 = time.time()
    doc = pymupdf.open(SRC)
    figures = inventorier_figures(doc)
    e = Extracteur(SRC, figures, niveaux={1: 2, 2: 3, 3: 4, 4: 5}, marges=MARGES,
                   styles_balises={'Em': 'em', 'Strong': 'strong', 'Code': 'code'})
    blocs = e.extraire()
    controler_figures(doc, figures)
    restes = controler_colonnes(e)
    inexplique = [r for r in restes if not r.startswith(COLONNES_CONNUES)]
    assert not inexplique, inexplique
    brut = vers_html(blocs)
    if HTML:
        HTML.write_text(brut, encoding='utf8')
    # complétude : chaque mot du texte courant d'origine (hors marges) se retrouve dans
    # l'extraction, sauf le texte des figures, contrôlé à part (dans la zone rendue)
    zones = [(f.page, pymupdf.Rect(r.bbox)) for f in figures for r in f.runs]
    manque, _ = controler_extraction(SRC, brut, marges=MARGES, ecarter=zones)
    # en-têtes de tableau répétés à chaque page : écartés à dessein (une fois dans
    # l'extraction, à chaque page dans le PDF)
    inexplique = {m: n for m, n in manque.items() if n > ECARTS_CONNUS.get(m, 0)}
    if inexplique:
        sys.exit(f'extraction incomplète ({sum(inexplique.values())} mots) : '
                 f'{dict(collections.Counter(inexplique).most_common(40))}')
    # ordre : les pages de tableaux retouchés (p. 736, 803, 905, 940) restent sous 90 %
    faibles = controler_ordre(doc, brut)
    print(f'ordre : {len(faibles)} page(s) sous 90 % de suites retrouvées {faibles}')
    assert len(faibles) <= 6, faibles
    mots_figures = sum(len(re.findall(r'\w+', r.texte)) for f in figures for r in f.runs)
    print(f'extraction : {len(blocs)} blocs, {len(figures)} figures ({mots_figures} mots en image), '
          f'écarts connus seulement ({sum(manque.values())} mots), {time.time() - t0:.0f} s')
    for x in e.ecarts:
        print('  ' + x)

    p = page_de_titre(blocs, doc)
    texte, statut = corps(blocs, p, doc.get_toc())
    texte, statut, n = retraits.retirer_traces(texte, statut)
    print(f'traces de production : {n} substitutions et motifs comptés, aucune trace restante')
    if HTML:
        HTML.with_suffix('.corps.html').write_text(texte, encoding='utf8')
    texte, n_corr = corrections.corriger(texte)
    texte = appeler_figures_et_tableaux(texte)
    texte = couper_adresses(texte)
    restantes = retraits.controler_traces(texte)
    assert not restantes, f'traces de production introduites par les correctifs : {restantes}'
    if n_corr:
        print(f'correctifs : {len(n_corr)} interventions appliquées')
    bilan = controler_corps(texte, len(figures))
    print('structure :', bilan)
    assert not bilan['figures_sans_legende'] and not bilan['legendes_egarees'], bilan

    m = re.match(r'D:(\d{4})(\d\d)(\d\d)', doc.metadata['creationDate'])
    compile_le = date_fr(*map(int, m.groups()))
    fiche = ('<div class="fiche"><table><tbody>'
             f'<tr><td>Auteur</td><td>{html.escape(p["auteur"])}</td></tr>'
             f'<tr><td>Édition</td><td>{html.escape(p["edition"])}</td></tr>'
             f'<tr><td>Faits gelés au</td><td>{GEL} (revalidations ciblées des 28–30 juillet, 2 septembre et 23–29 octobre 2026 ; voir ch. 50 § 50.3–50.4)</td></tr>'
             f'<tr><td>Compilé le</td><td>12 novembre 2026 (édition initiale du {compile_le})</td></tr>'
             f'<tr><td>Statut</td><td>{statut[3:-4]}</td></tr>'
             f'<tr><td>Actualisation</td><td>{ACTUALISATION}, annexe N</td></tr>'
             '</tbody></table></div>')
    annexe, refs_annexe = actualisation(ICI)
    annexe, refs_annexe = couper_adresses(annexe), couper_adresses(refs_annexe)
    liminaire = ''.join(f'<p><strong>{html.escape(t)}</strong><br>{d}</p>' for t, d in p['livres'])
    liminaire += ('<p><strong>Annexes (B, I et N)</strong><br>Le lettrage conserve les identifiants du plan de la somme : '
                  'l’annexe B porte le socle consolidé des fiches sources (<code>S-001</code> à <code>S-159</code>), '
                  'l’annexe I la bibliographie générale et l’annexe N l’actualisation de novembre 2026 '
                  '(les lettres intermédiaires désignant les registres de production retirés à la publication).</p>')
    liminaire += f'<blockquote>{p["exergue"]}</blockquote>'
    meta = doc.metadata
    typo = lambda t: chaine_typst(t.replace("'", '’'))
    main_typ = f'''#import "gabarit.typ": *
#set document(title: {typo(meta['title'])}, description: {typo(meta['subject'])},
  keywords: ({', '.join(chaine_typst(k.strip()) for k in meta['keywords'].split(','))}))
#show: note.with(titre-court: "Compendium", pied: [Gel au {GEL} (revalidé oct. 2026) · actualisation du {ACTUALISATION}])
// numérotation d'origine (par chapitre) gardée dans les légendes : celle de Typst se tait
#set figure(numbering: none)
// légendes au-dessus des tableaux, sous les figures, comme dans l'édition d'origine
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.caption.where(position: top): it => block(sticky: true, it)
#show figure.where(kind: image): set block(above: 14pt, below: 16pt)
// sections de quatrième rang (H4 d'origine, 1.1.3.1…)
#show heading.where(level: 5): it => block(above: 10pt, below: 5pt, sticky: true,
  text(font: sans, size: 9.5pt, weight: "regular", style: "italic", fill: gris, it.body))
#show quote.where(block: true): it => block(width: 100%, inset: (left: 12pt, y: 6pt),
  stroke: (left: 2pt + accent), fill: accent-pale, it.body)
// adresses : coupées à leurs traits d'union ou barres obliques, jamais par une césure
// qui leur ajouterait un trait
#show regex({chaine_typst(URL)}): it => text(hyphenate: false, it)
#couverture(surtitre: {typo(p['surtitre'])}, titre: text(hyphenate: false, {typo(p['titre'])}),
  sous-titre: {typo(p['sous_titre'])}, auteur: {typo(p['auteur'])}, date: {typo(p['edition'])},
  fiche: include "fiche.typ")
#page(header: none, {{
  v(30pt)
  set par(justify: false)
  include "liminaire.typ"
}})
#sommaire()
#include "corps.typ"
#include "actualisation.typ"
#[#set par(justify: false, linebreaks: "simple")
#include "references-actualisation.typ"]
'''
    dossier = TMP / 'figures'
    dossier.mkdir()
    rendre_figures(doc, figures, dossier)
    source = ' '.join(texte_controle(t) for t in (p['surtitre'], p['titre'], p['sous_titre'], fiche, liminaire, texte,
                                                  annexe, refs_annexe))
    # adresses (URL, chemins) : Typst les coupe en fin de ligne n'importe où, sans trait
    # (« cloudsecuri|tyalliance ») ; contrôlées à part, d'un seul tenant, blancs ôtés
    source = source.replace(ZWSP, '')
    adresses = re.findall(URL, source)
    source = re.sub(URL, ' ', source)
    t1 = time.time()
    brouillon = TMP / OUT.name
    composer({'fiche': fiche, 'liminaire': liminaire, 'corps': texte, 'actualisation': annexe,
              'references-actualisation': refs_annexe}, main_typ, brouillon, source,
             extras=sorted(dossier.iterdir()))
    # hors en-têtes et pieds, comme composer.controler()
    rendu = re.sub(r'[\s\xad\u200b]+', '', ''.join(w[4] for pg in pymupdf.open(brouillon) for w in pg.get_text('words')
                                             if w[1] > 70 and w[3] < pg.rect.height - 60))
    absentes = [a for a in adresses if re.sub(r'\s+', '', a) not in rendu]
    if absentes:
        shutil.copy(brouillon, OUT.with_name(OUT.stem + ' (rejeté).pdf'))
        sys.exit(f'{len(absentes)} adresse(s) absente(s) du PDF : {absentes[:10]}')
    shutil.copy(brouillon, OUT)
    print(f'adresses : {len(adresses)}, toutes présentes; composition : {time.time() - t1:.0f} s '
          f'(pandoc {DUREES["pandoc"]:.0f} s, typst {DUREES["typst"]:.0f} s); {OUT}')


if __name__ == '__main__':
    main()
