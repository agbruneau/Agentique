#!/usr/bin/env python3
"""La porte de pagination que la chaine du traite n'avait pas.

⚠ LE FORMAT FERME DE CENT PAGES EST LEVE. Ce controle ne juge donc plus un
nombre de pages : il le rapporte. Ce qu'il attrape encore, et que rien d'autre
n'attrape, c'est un PDF perime, un arbre de pages incoherent et une
bibliographie mal appariee. Depuis le 15 aout 2026 le traite partage sa mise en
page avec la veille et la revue — marges de 117 x 72 pt, corps de 11 pt sur
14,3 pt, appareil a 9 pt debordant a 468 pt —, et l'etalonnage mots -> pages a
ete refait sur cette geometrie.

Quatre pieges, dans cet ordre :
  1. la PAGINATION du rendu — le PDF decrit-il encore la source, ou a-t-il ete
     depasse par une reprise du `.md` ? Et l'arbre de pages est-il coherent ?
  2. le BUDGET de la source — combien de mots-equivalents restent avant que le
     prochain rendu ne franchisse la cible ? C'est la seule mesure qui serve
     AVANT de rendre, et c'est celle que le budget nul reclame ;
  3. l'APPARIEMENT bibliographique — les 123 notices sont-elles contigues, toutes
     citees nommement, et aucune citation ne pointe-t-elle hors liste ?
  4. la PARITE du rendu — le PDF versionne est-il CELUI que la source rend
     aujourd'hui ? [1] ne compare que des horodatages, et un `git clone` les
     egalise ; celui-ci refait le rendu et compare les octets.

Usage : python check-traite.py [Traité.pdf] [Traité.md] [--sans-parite]
        -> sortie 0 si le rendu
tient sa cible, 1 sinon. Se lance de n'importe quel repertoire.

Regle des chemins, reprise de `3 - Veille/Python/` : les defauts se resolvent
contre l'emplacement du script, jamais contre le repertoire courant ; un chemin
donne en argument, lui, reste relatif au repertoire courant.
"""
import io, re, shutil, subprocess, sys, tempfile, zlib
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PDF = RACINE / 'Traité.pdf'
SRC = RACINE / 'Traité.md'

# ⚠ REPLI SEULEMENT, et il a menti. Le compte se LIT au front-matter (voir
# `appariement`) ; cette constante ne sert que si la ligne qui l'annonce
# devient illisible. Figee a 119 jusqu'au 2 septembre 2026 alors que le
# document en porte 123 depuis le 15 aout, elle aurait fait echouer le
# controle a tort le jour ou le front-matter aurait change de forme —
# c'est-a-dire au premier moment ou l'on aurait eu besoin d'un repli.
# *Un repli qui ne suit pas ce qu'il replace est un piege differe.*
REFS = 123           # notices de la section « Références », mesure du 2 septembre 2026

# ⚠ ETALONNAGE REFAIT LE 15 AOUT 2026, APRES RECOMPOSITION, mesure par RENDU et
# non estime : variantes de `Traité.md` rendues par la chaine canonique depuis la
# racine, page comptee dans le PDF. IL A FALLU LE REFAIRE — les trois documents
# du depot ont ete portes sur une geometrie commune (corps de 378 pt au lieu de
# 468, interligne de 14,3 pt au lieu de 13,6), et une page ne tient plus le meme
# nombre de mots. L'ancien etalonnage, cale sur le rendu a 100 pages du 13 aout,
# donnait une page pour 800 mots ; il en donnerait 25 % de trop aujourd'hui.
#   mots  : +0 -> 142 p. | +1000 -> 143 | +3000 -> 147 | +6000 -> 151
#           +12000 -> 161
#           => pente de 1,58 page par millier de mots dans le regime lineaire,
#              soit UNE PAGE POUR 630 MOTS.
#   figures : +5 -> 144 p. | +10 -> 147
#           => 0,45 page par figure, soit 285 mots-equivalents pour une legende
#              de quatorze mots. Le poste reste le plus cher, mais il l'est
#              moins qu'avant : la figure garde ses 468 pt de large quand le
#              corps est passe a 378, donc sa hauteur n'a pas bouge tandis que
#              celle d'une page de prose, elle, porte moins de texte.
#   tableaux : pas de poste a eux. Un tableau coute ce que couterait son texte
#           en prose, et ce texte est deja dans le compte de mots — constat de
#           l'etalonnage du 13 aout, que le passage a 9 pt de l'appareil des
#           trois documents ne change pas de sens.
# ⚠ IL N'Y A PLUS DE CIBLE NI DE MARGE RESIDUELLE : le format ferme de cent
# pages est leve depuis le 15 aout 2026, et les deux constantes qui les
# portaient ont ete retirees plutot que laissees a mentir. Ce qui suit sert a
# projeter une croissance, pas a juger un depassement.
# ⚠ MOTS_REF COMPTE LE FRONT-MATTER, donc une ligne de COMMENTAIRE ajoutee au
# gabarit pese ici autant qu'une ligne d'argument. C'est ce qui l'a fait bouger
# de 70652 a 71100 : la regle d'emphase posee dans `header-includes` le 15 aout
# 2026 apporte 448 mots de commentaire Typst, et le rendu fait toujours
# 142 pages. La reference se recale donc SANS que la cible bouge — sans quoi la
# projection annoncerait a jamais +0,7 page qu'aucun rendu ne produira. Qui
# reprend ce chiffre le mesure sur un `.md` dont le PDF vient d'etre rendu.
# ⚠ MEME GESTE LE 16 AOUT 2026, de 71100 a 71744 : la regle de bibliographie
# posee dans `header-includes` apporte 644 mots de commentaire Typst, qui ne
# produisent aucune page. La page gagnee — 142 -> 143 — vient d'ailleurs, du
# blanc de 1,15 em rendu aux 123 notices, que le compte de mots ne voit pas.
# Recaler MOTS_REF sans recaler le « 142 p. » ci-dessous ferait mentir les deux.
# ⚠ RECALE LE 2 SEPTEMBRE 2026, de 71744 a 72110, SUR UN `.md` DONT LE PDF
# VIENT D'ETRE OPPOSE AU RENDU — c'est la condition que le commentaire
# ci-dessus pose, et le controle [4] la rend verifiable au lieu de la
# laisser a la bonne foi. La reference portait l'etat du 15 aout au matin
# quand le document livre le meme jour en compte 366 de plus : la
# projection annoncait donc « +0,6 page » a jamais, sur un rendu qui fait
# 143 pages et n'en fera pas 144 pour autant. *Une ligne de base qui
# derive d'un demi-jour rapporte une croissance qui n'existe pas.*
MOTS_REF = 72511     # mots du `.md` entier — front-matter compris — qui rend 143 p.
# ⚠ RECALE UNE SECONDE FOIS LE 2 SEPTEMBRE 2026, de 72110 a 72511, apres la
# QUATRIEME edition : treize legendes d'algorithme renumerotees, trois posees
# au chapitre 2, vingt-deux tableaux numerotes dans la source, et la conclusion
# datee. **Le rendu fait toujours 143 pages** — la pagination est preservee,
# mesuree section par section, une seule frontiere bougeant (§2.3, p. 34 -> 35).
# *Quatre cents mots d'appareil ne font pas une page quand ils se repartissent
# sur vingt-deux legendes et treize titres.*
FIGS_REF = 19
MOTS_PAR_PAGE = 630
MOTS_PAR_FIGURE = 285

fail = []


def pages(pdf: Path):
    """Nombre de pages du PDF, lu a deux sources qui doivent concorder.

    Source A : le `/Count` du noeud `/Pages`. Source B : le nombre d'objets
    `/Type /Page`. Un desaccord signale un PDF tronque ou un arbre de pages
    imbrique, et vaut mieux qu'un chiffre faux rendu avec aplomb.

    ⚠ Deux pieges. `/Type/PageLabel` et `/Type/Pages` contiennent tous deux la
    chaine `/Page` : d'ou la garde `(?![a-zA-Z])`. Et si Typst se met un jour a
    ranger ses objets dans des flux comprimes (`/ObjStm`), le motif ne trouve
    plus rien dans les octets bruts — on decomprime alors, comme le fait
    `check-resume.py` pour les flux de contenu.
    """
    d = pdf.read_bytes()
    if not re.search(rb'/Type\s*/Pages', d) and b'/ObjStm' in d:
        for m in re.finditer(rb'stream\r?\n(.*?)\r?\nendstream', d, re.S):
            try:
                d += zlib.decompress(m.group(1))
            except zlib.error:
                pass
    compte = [int(x) for x in re.findall(rb'/Type\s*/Pages.*?/Count\s+(\d+)', d, re.S)]
    objets = len(re.findall(rb'/Type\s*/Page(?![a-zA-Z])', d))
    return (max(compte) if compte else None), objets


def pagination(pdf: Path, src: Path):
    n, objets = pages(pdf)
    if n is None:
        fail.append(f'{pdf.name} : aucun noeud /Pages lisible — controle inapplicable')
        print('  [1] pagination  : PDF illisible -> ECHEC')
        return False
    ok = True
    if n != objets:
        fail.append(f'{pdf.name} : /Count annonce {n} pages, {objets} objets /Type/Page '
                    f'trouves — PDF tronque ou arbre de pages imbrique')
        ok = False
    # ⚠ LE FORMAT FERME DE CENT PAGES EST LEVE LE 15 AOUT 2026. Le compte de
    # pages se RAPPORTE, il ne se juge plus : le tenir aurait exige de retrancher
    # 288 mots d'argument ou de descendre l'appareil sous 8,2 pt, c'est-a-dire de
    # payer un nombre rond avec de la lisibilite. Ce qui reste vrai et donc
    # bloquant ci-dessous : un PDF qui ne decrit plus sa source, et un arbre de
    # pages incoherent. Un controle qui juge une cible abandonnee ne mesure plus
    # rien — il perime, et on finit par le desactiver pour de mauvaises raisons.
    # ⚠ Le piege qui rendrait ce controle complaisant : un PDF PERIME. La source
    # peut avoir grossi de dix pages sans que le PDF le sache, et le compte de
    # pages passerait au vert sur un document faux. Le controle [2] mesure la
    # source elle-meme, mais l'horodatage suffit a dire que [1] ne vaut plus.
    perime = src.exists() and src.stat().st_mtime > pdf.stat().st_mtime
    if perime:
        fail.append(f'{pdf.name} est anterieur a {src.name} : le compte de pages ne decrit '
                    f'plus la source. Rendre avant de conclure — voir [2] pour la projection')
        ok = False
    etat = 'OK' if ok else 'ECHEC'
    print(f'  [1] pagination  : {n} pages, sans cible'
          f'{" — PDF perime" if perime else ""} -> {etat}')
    return ok


def budget(s: str):
    """Le budget de pages, mesure sur la SOURCE, avant tout rendu.

    Deux postes seulement, parce que la mesure n'en a trouve que deux : les mots
    et les figures. Un tableau coute ce que couterait son texte en prose, et ce
    texte est deja compte dans les mots (cf. l'etalonnage en tete de fichier).
    """
    mots = len(s.split())
    figs = len(re.findall(r'\]\(figures/', s))
    surplus = (mots - MOTS_REF) + (figs - FIGS_REF) * MOTS_PAR_FIGURE
    ok = True
    # ⚠ Ne juge plus, RAPPORTE. La reference est desormais le rendu du 15 aout
    # 2026 a 142 pages, celui de la geometrie commune aux trois documents du
    # depot : elle dit de combien le document a grossi depuis, ce qui est utile a
    # un auteur et n'est pas un verdict. L'etalonnage mots -> pages n'est de
    # toute facon fiable qu'a la page pres — deux sources aux MEMES mots et
    # MEMES figures rendent 100 et 101 pages, mesure du 15 aout 2026. Il ne
    # pouvait donc pas porter un jugement au mot pres, et il ne le porte plus.
    print(f'  [2] croissance  : {mots} mots, {figs} figures -> {surplus:+d} mots-equivalents '
          f'depuis la reference du 2 septembre 2026 (~{surplus / MOTS_PAR_PAGE:+.1f} page)')
    print(f'      ordre de grandeur : 1 page ~ {MOTS_PAR_PAGE} mots '
          f'~ {MOTS_PAR_PAGE // MOTS_PAR_FIGURE} figures, mesure a la recomposition du 15 aout')
    return ok


def appariement(s: str):
    """Toute notice existe une fois, est citee nommement, et rien ne pointe hors liste.

    ⚠ Contrairement a la revue de litterature, le traite ne cite AUCUNE plage
    « [51-63] » — verifie : zero occurrence. Le motif n'a donc pas a les
    developper, et il ne doit pas : une plage rend le controle aveugle aux
    notices orphelines.
    """
    corps, refs = s.split('## Références {-}')
    # ⚠ Le corps porte 21 blocs de code, et un indice de tableau — `agents[0]` —
    # y ressemble trait pour trait a une citation. Les retirer AVANT de chercher
    # les renvois : sans cela le controle rend « citees mais absentes : [0] » sur
    # un document sain, et un controle qui crie a tort finit par etre desactive.
    corps = re.sub(r'(?ms)^```.*?^```', '', corps)
    defini = [int(m.group(1)) for m in re.finditer(r'(?m)^(\d+)\. ', refs)]
    ok = True
    if defini != list(range(1, len(defini) + 1)):
        rupture = next((i + 1 for i, v in enumerate(defini) if v != i + 1), len(defini))
        fail.append(f'numerotation des notices non contigue : rupture au rang {rupture} '
                    f'(lu « {defini[rupture - 1] if rupture <= len(defini) else "?"}. »)')
        ok = False
    # ⚠ Le compte attendu se LIT dans le commentaire du front-matter, il ne se
    # code pas en dur : fige a 119, ce controle interdisait au document d'ajouter
    # une notice — c'est-a-dire qu'il interdisait au document d'evoluer. Lu ici,
    # il oblige au geste inverse et utile : qui ajoute une notice met a jour la
    # ligne du front-matter qui annonce combien il y en a.
    m = re.search(r'Les (\d+) notices de r[ée]f[ée]rences', s)
    attendu = int(m.group(1)) if m else REFS
    if len(defini) != attendu:
        fail.append(f'{len(defini)} notices pour {attendu} annoncees par le front-matter '
                    f'(« Les {attendu} notices de références… ») — mettre a jour l\'un ou l\'autre')
        ok = False

    cite = set()
    for m in re.finditer(r'\[(\d+(?:\s*,\s*\d+)*)\]', corps):
        cite |= {int(x) for x in m.group(1).split(',')}
    hors = sorted(cite - set(defini))
    if hors:
        fail.append(f'citees dans le corps mais absentes de la liste : {hors}')
        ok = False
    orphelines = sorted(set(defini) - cite)
    if orphelines:
        fail.append(f'notices jamais citees dans le corps : {orphelines}')
        ok = False
    print(f'  [3] appariement : {len(defini)} notices, {len(cite & set(defini))} citees '
          f'nommement -> {"OK" if ok else "ECHEC"}')
    return ok


# ⚠ CE QUE LA CHAINE REND EST REPRODUCTIBLE A L'OCTET, et c'est ce qui rend le
# controle [4] possible sous cette forme. Mesure du 2 septembre 2026 : deux
# rendus de la meme source par la meme chaine donnent des fichiers de MEME
# taille dont seuls quatre champs different, tous volatils par construction —
# les deux dates du trailer, l'identifiant de fichier, les dates XMP et
# l'identifiant d'instance XMP. Neutralises, les octets coincident.
#
# Comparer les OCTETS plutot que le texte extrait n'est pas un exces de zele :
# un extracteur ne voit ni les figures, ni la geometrie, ni les fontes, et
# l'audit du 2 septembre 2026 a mesure que deux extracteurs du depot lisent
# differemment le meme PDF — l'un d'eux ne rendait AUCUN libelle « Tableau N »
# la ou l'autre les lit tous. Un controle de parite fonde sur l'extraction
# heriterait de cette cecite ; fonde sur les octets, il ne herite de rien.
VOLATILS = [
    (rb'/(Creation|Mod)Date\s*\([^)]*\)', rb'/\1Date()'),
    (rb'/ID\s*\[[^\]]*\]', rb'/ID[]'),
    (rb'<xmp:(ModifyDate|CreateDate|MetadataDate)>[^<]*</xmp:\1>', rb'<xmp:\1></xmp:\1>'),
    (rb'<xmpMM:InstanceID>[^<]*</xmpMM:InstanceID>', rb'<xmpMM:InstanceID></xmpMM:InstanceID>'),
]


def sans_horodatage(octets: bytes) -> bytes:
    """Le PDF prive des seuls champs qui changent d'un rendu a l'autre."""
    for motif, remplacement in VOLATILS:
        octets = re.sub(motif, remplacement, octets)
    return octets


def parite(pdf: Path, src: Path):
    """[4] — le PDF versionne est-il CELUI que la source rend aujourd'hui ?

    ⚠ C'EST LE CONTROLE QUE [1] NE FAIT PAS, ET LE PIEGE QU'IL LAISSE PASSER
    EST GRAND. [1] compare deux HORODATAGES ; or un `git clone` les pose tous
    deux a la date du checkout, et [1] devient aveugle sur un depot frais —
    exactement l'etat dans lequel un tiers lit le depot. Il est aveugle aussi
    quand la source est reprise dans la meme seconde que le rendu, et quand le
    rendu est refait apres une regression du gabarit sans que la source bouge.
    Celui-ci REFAIT le rendu et compare, ce qui ne suppose aucune date.

    Le prix est une chaine et une trentaine de secondes. Quand la chaine
    manque, le controle se DECLARE non mesure plutot que de passer en silence :
    PD6 du dossier — ce qui est absent s'affiche au meme rang que ce qui est
    present —, et un controle qui se tait quand il ne peut pas mesurer finit
    par etre cru quand il ne mesure rien.
    """
    if shutil.which('pandoc') is None or shutil.which('typst') is None:
        print('  [4] parite      : chaine absente (pandoc et/ou typst) -> NON MESURE')
        print('      Le rendu versionne n\'est donc PAS oppose a sa source. Pour le faire :')
        print('      OUT_PDF=/tmp/essai.pdf bash build/build-pdf.sh, puis relancer ce controle')
        return True

    with tempfile.TemporaryDirectory(prefix='parite-traite-') as tmp:
        essai = Path(tmp) / 'essai.pdf'
        # ⚠ `cwd=RACINE` n'est pas decoratif : les dix-neuf figures sont citees
        # en chemin relatif par la source, et la chaine ne se lance que de la.
        r = subprocess.run(['pandoc', src.name, '--pdf-engine=typst', '--toc', '-o', str(essai)],
                           cwd=RACINE, capture_output=True, text=True, encoding='utf-8',
                           errors='replace')
        if r.returncode != 0 or not essai.exists():
            fail.append(f'le rendu d\'essai a echoue — la chaine ne compose plus la source : '
                        f'{(r.stderr or "").strip()[:300]}')
            print('  [4] parite      : rendu impossible -> ECHEC')
            return False
        a = sans_horodatage(pdf.read_bytes())
        b = sans_horodatage(essai.read_bytes())

    if a == b:
        print(f'  [4] parite      : {len(a)} octets hors horodatage, refait a l\'identique -> OK')
        return True

    # Localiser la divergence : un octet suffit a la nommer, et l'ecart de
    # taille dit s'il s'agit d'un ajout ou d'une retouche en place.
    i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
    fail.append(f'{pdf.name} n\'est PAS le rendu de {src.name} : premiere divergence a l\'octet '
                f'{i} ({len(a)} octets versionnes contre {len(b)} refaits). Le rendu versionne '
                f'decrit un autre etat de la source — rendre avant de conclure')
    print('  [4] parite      : le PDF versionne n\'est pas celui que la source rend -> ECHEC')
    return False


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    pdf = Path(args[0]) if args else PDF
    src = Path(args[1]) if len(args) > 1 else SRC
    for p in (pdf, src):
        if not p.exists():
            print(f'introuvable : {p}')
            return 1
    s = io.open(src, encoding='utf-8').read()
    print(f'Porte de pagination — {pdf.name} / {src.name}')
    res = [pagination(pdf, src), budget(s), appariement(s)]
    # ⚠ `--sans-parite` existe pour l'iteration rapide sur la source, et pour
    # RIEN D'AUTRE : le controle [4] est le seul qui oppose le rendu a ce
    # qu'il pretend rendre. Le sauter en passe de cloture reviendrait a
    # publier un PDF que personne n'a compare a sa source.
    if '--sans-parite' in sys.argv:
        print('  [4] parite      : SAUTE sur demande (--sans-parite) -> NON MESURE')
    else:
        res.append(parite(pdf, src))
    if fail:
        print('\nECHEC :')
        for f in fail:
            print('  -', f)
        return 1
    print('\nTous les controles passent.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
