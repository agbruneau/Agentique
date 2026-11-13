"""Retrait des traces de production du Compendium (31 oct. 2026).

L'édition d'origine laisse au texte courant l'appareil de sa fabrication : renvois au plan
de rédaction (TOC et ses versions, PRD, fichiers de travail .md), décisions d'auteur (D-n,
« décision n du TOC »), garde-fous de rédaction des volumes sources (R-n, R-IV-n),
portes de qualité (G-n, contrôles S5 et P6), remontées, collations et balayages de thèses,
fusions de chapitres, lots de travail (L-n), hachages de commit. Ces traces sortent; ce qui
qualifie une affirmation pour le lecteur reste : régimes [A]/[B]/[C], socle et relève,
degrés d'absence, cotes F-xx, H-xx et S-xxx, renvois aux volumes I à III.

Le retrait se fait en deux temps, rejoués à chaque composition sur le texte extrait :
  - des règles systématiques : parenthèses de pur renvoi (« (R-13 du Vol. III) »,
    « (décision 15 du TOC) ») et formules récurrentes (« au sens de R-14 du Vol. III »);
  - des substitutions comptées (retraits.json), phrase par phrase, en quatre étapes : chaque
    « avant » doit se trouver exactement n fois, faute de quoi la composition s'arrête.
    Après chaque étape, les lignes touchées sont normalisées (balises vides, blancs) et les
    blocs vidés retirés.
controler_traces() vérifie enfin qu'aucune trace de la liste TRACES ne subsiste.
"""
import json, pathlib, re

ICI = pathlib.Path(__file__).resolve().parent
VOL = r'(?:du )?Vol\.\s(?:III|II|I)'

# ---- règles systématiques ----------------------------------------------------------------

# éléments de parenthèse qui ne sont qu'une trace
ITEM_TRACE = re.compile('|'.join([
    rf'(?:garde-fous?\s|l.échelle\s|échelle\s)?R-(?:IV-)?\d+[a-z]?(?:\s(?:et|à)\sR-\d+)*(?:\s{VOL})?(?:\simplicite ici)?',
    r'décisions?\s\d+[a-z]?(?:-[ivx]+)?(?:(?:,\s|\set\s|\sà\s)\d+[a-z]?(?:-[ivx]+)?)*(?:\sdu\s(?:TOC|plan))?',
    r'D-\d+[a-z]?(?:\s(?:et|à)\sD-\d+)*',
    rf'(?:PRD|PRDPlan)(?:\s{VOL})?(?:\s?§\s?[\d.]+)?',
    r'(?:voir la note de statut,\s)?remontée\sR-IV-\d+(?:,\s(?:soldée|close sur constat))?',
    r'(?:décision prise sur la\s)?remontée\sR-IV-\d+',
    r'TOC(?:\.md)?(?:\sv\d+\.\d+)?(?:,\sentrée\sdu\s§\s?[\d.]+)?',
    r'risque\s\d+\sdu\sTOC',
    r'alinéa\s[\w-]+', r'soldée', r'close sur constat', r'écart remonté', r'formulation imposée',
    r'statut dit à la mention', r'le statut se dit à chaque mention', r'troisième interdit',
    r'dont le siège est le §\s?[\d.]+ de sa source',
]))
# éléments qui, restés seuls dans la parenthèse, gardent un sens pour le lecteur
CONTENU = re.compile(r"degré \d|troisième degré|siège .+|réserve F-\d+|ch\. \d+ § [\d.]+|explicité au § [\d.]+")
SEP = re.compile(r'\s?[;,:]\s|\s—\s')
PAREN = re.compile(r'(\s?)\(([^()<>]{1,300})\)')


def nettoyer_parenthese(m):
    """« (R-13 du Vol. III ; siège au ch. 7) » -> « (siège au ch. 7) »; « (décision 15 du TOC) » -> ''."""
    morceaux = SEP.split(m.group(2))
    garde = [x for x in morceaux if not ITEM_TRACE.fullmatch(x.strip())]
    if len(garde) == len(morceaux):
        return m.group(0)
    if not garde:
        return ''
    if not all(CONTENU.fullmatch(x.strip()) for x in garde):
        return m.group(0)
    return f'{m.group(1)}({"; ".join(x.strip() for x in garde)})'


FORMULES = [
    # « R-02 du Vol. III : X démontre… ne démontre pas… » : la qualification reste, sa règle sort
    (r"(<p>(?:<em>)?|(?<=[.:] ))R-02(?: du Vol\. III)?( :| —|\.|,)", r"\1Qualification\2"),
    (r"<p><strong>R-14, degré", "<p><strong>Degré"),
    (r"\bR-14(?: du Vol\. III)?,? (degré \d)", r"\1"),
    (r"(Qualification), au sens de R-\d+(?: du Vol\. (?:III|II))?", r'\1'),
    # « absence de documentation au sens de R-14 du Vol. III » : l'échelle des degrés
    # d'absence est portée par l'ouvrage lui-même
    (r"(,)? au sens de (?:l['’]échelle )?R-\d+(?: du Vol\. (?:III|II))?(?(1),)", ''),
    (r" de l['’]échelle R-\d+(?: du Vol\. (?:III|II))?", ''),
    # majuscule rendue au « degré » qui ouvre désormais une phrase
    (r"((?:<p>|[.!?] )(?:<(?:strong|em)>)*)degré (\d)", r"\1Degré \2"),
    (r"\bR-14 (degré \d)", r'\1'),
]


def appliquer_regles(s):
    s = PAREN.sub(nettoyer_parenthese, s)
    for motif, repl in FORMULES:
        s = re.sub(motif, repl, s)
    return s


# ---- substitutions comptées ------------------------------------------------------------

VIDE = re.compile(r'(?:<(p|li|blockquote|h\d)>)+(?:</(?:p|li|blockquote|h\d)>)+')


def normaliser(l):
    """Ligne amputée : balises en ligne vidées, blancs de bord de bloc et blancs doublés."""
    while re.search(r'<(em|strong)>\s*</\1>', l):
        l = re.sub(r'<(em|strong)>\s*</\1>', '', l)
    l = re.sub(r'(<(?:p|li|td|th|blockquote|h\d)>) +', r'\1', l)
    l = re.sub(r' +(</(?:p|li|td|th|blockquote|h\d)>)', r'\1', l)
    return re.sub(r' {2,}', ' ', l)


def appliquer_etape(s, substitutions, globales):
    avant = s.split('\n')
    for a, b, n in substitutions:
        assert s.count(a) == n, f'retrait : {s.count(a)} occurrence(s) au lieu de {n} de « {a[:70]} »'
        s = s.replace(a, b)
    for motif, repl, n in globales:
        trouve = len(re.findall(motif, s))
        assert trouve == n, f'retrait : {trouve} occurrence(s) au lieu de {n} de {motif}'
        s = re.sub(motif, repl, s)
    apres = s.split('\n')
    assert len(apres) == len(avant), 'une substitution a changé le découpage en blocs'
    out = []
    for l, l0 in zip(apres, avant):
        if l != l0:
            l = normaliser(l)
            for t in ('em', 'strong'):
                assert l.count(f'<{t}>') == l.count(f'</{t}>'), f'balises <{t}> déséquilibrées : {l[:80]}'
            if VIDE.fullmatch(l):
                continue
        out.append(l)
    return '\n'.join(out)


# ---- contrôle de sortie ------------------------------------------------------------------

TRACES = [r'\bTOC\b', r'\bPRD', r'\bD-\d+[a-z]?\b', r'[Dd]écisions? \d+[a-z]? du', r'\bR-(?:IV-|G-)?\d+\b',
          r'\bG-\d\b', r'[Cc]ollation|collationn', r'\blignes? Fusion\b|\bfusion v0', r'[Dd]omaine de balayage',
          r'tables? de couverture|table détaillée', r'\blots? (?:<code>)?L-\d', r'[Rr]emontées? R-',
          r'registre du (?:plan|gel)|volet résiduel', r'\bS5\b|\bP6\b|check-sieges',
          r'(?<![\w/.-])(?!(?:AGENTS|CLAUDE|SECURITY|PROTOCOL|agents)\.md)[\w-]+\.md\b', r'\bv0\.\d+ du plan|\bTOC v\d',
          r'présente pièce|hors portes|arbre courant|règle du dépôt', r'\bcommit\s(?:<code>)?[0-9a-f]{7}']


def controler_traces(s):
    """Traces encore présentes au texte (hors balises) : [(motif, extrait)]."""
    t = re.sub(r'<[^>]+>', '', s).replace('\xa0', ' ')
    return [(p, t[max(0, m.start() - 40):m.end() + 40]) for p in TRACES for m in re.finditer(p, t)]


STATUT = ("Depuis le 23 octobre 2026 (décision D-21, qui amende D-18), ce volume est l'un des cinq livrables du "
          "dépôt. Ses cinquante chapitres sont publiables pour l'édition de novembre 2026 (décision D-20), et "
          "chacun porte son statut en tête.",
          "Édition intégrale de novembre 2026 (cinquante chapitres). Ce volume constitue la somme encyclopédique "
          "de la collection L'entreprise agentique.")


def retirer_traces(corps, statut):
    """Corps et mention de statut de la fiche, traces retirées; contrôle de sortie compris."""
    corps = appliquer_regles(corps)
    etapes = json.loads((ICI / 'retraits.json').read_text(encoding='utf8'))['etapes']
    for e in etapes:
        corps = appliquer_etape(corps, e['substitutions'], e['globales'])
    assert statut.count(STATUT[0]) == 1, 'mention de statut introuvable'
    statut = statut.replace(*STATUT)
    restes = controler_traces(corps + statut)
    assert not restes, f'{len(restes)} trace(s) de production restante(s) : {restes[:5]}'
    n = sum(len(e['substitutions']) + len(e['globales']) for e in etapes)
    return corps, statut, n
