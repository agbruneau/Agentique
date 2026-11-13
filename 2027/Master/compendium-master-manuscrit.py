"""Génère le manuscrit unifié du Compendium maître dans Master/manuscrit/.

Usage : python Master/compendium-master-manuscrit.py

Entrées (jamais modifiées) :
  Claude/compendium-2027-chapitre-NN-*.md, Claude/compendium-2027-annexe-X-*.md
  Gemini/dist/compendium-2027-complet.html

Structure produite : les 47 chapitres de l'édition C gardent leur numéro et
leur texte; chaque chapitre de l'édition G devient le volet « Mise en œuvre »
de son chapitre jumeau, sections et extraits renumérotés à la suite, renvois
recalculés. L'ouverture de G ouvre le volume; ses annexes A à C deviennent F à H.

Ce script régénère tout le manuscrit : les retouches rédactionnelles durables
se font ici (RETOUCHES) ou, une fois le manuscrit adopté comme source, dans
les fichiers de Master/manuscrit/ — auquel cas ne plus relancer ce script.
Les chapitres 48 à 50 (partie X) n'ont pas d'édition d'origine : ils n'existent que dans
Master/manuscrit/, que ce script efface avant de le régénérer.
Dépendance : pandoc sur le PATH.
"""
import collections
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
CLAUDE = os.path.join(RACINE, "Claude")
HTML_G = os.path.join(RACINE, "Gemini", "dist", "compendium-2027-complet.html")
MANUSCRIT = os.path.join(ICI, "manuscrit")
FIGURES = os.path.join(MANUSCRIT, "figures")
FILTRE = os.path.join(ICI, "filtres", "gemini.lua")

# Chapitre de l'édition G -> chapitre hôte (numérotation de l'édition C).
HOTE = {1: 1, 2: 17, 3: 43, 4: 11, 5: 5, 6: 6, 7: 10, 8: 13, 9: 12, 10: 14, 11: 16,
        12: 18, 13: 19, 14: 44, 15: 27, 16: 25, 17: 28, 18: 30, 19: 31, 20: 32, 21: 33,
        22: 34, 23: 40, 24: 38, 25: 41, 26: 45, 27: 46, 28: 46, 29: 47, 30: 47, 31: 47}

TITRES_VOLET = {
    1: "De l'assistance conversationnelle à la main-d'œuvre d'exécution asynchrone",
    2: "Le grand découplage : contrôle déterministe et autonomie probabiliste",
    3: "Modèle de maturité de l'entreprise agentique (niveaux 1 à 5) et antipatterns",
    4: "Gouvernance des standards et anatomie de la pile interopérable",
    5: "Connectivité verticale : outils, ressources, compétences et web",
    6: "Coordination horizontale, découverte et réseau inter-agents",
    7: "Interfaces humain-agent, multimodalité temps réel et protocoles transactionnels",
    8: "Le mur du contexte d'entreprise : ingénierie du contexte à grande échelle",
    9: "Couches sémantiques normalisées et ontologies d'entreprise",
    10: "Architectures de mémoire agentique distribuée et bi-temporelle",
    11: "Topologies d'orchestration et de chorégraphie multi-agents",
    12: "Moteurs d'exécution durable et gestion des cycles de vie de longue durée",
    13: "Maillage événementiel asynchrone et patron Saga à compensation",
    14: "Plan de données AI-natif, passerelles et routage cognitif hybride",
    15: "Fédération des jardins clos SaaS et problème de l'« orchestrateur d'orchestrateurs »",
    16: "Intégration du patrimoine sans API : Computer-Use Agents (CUA), RPA/APA et mainframes",
    17: "Orchestration cyber-physique : convergence IT/OT, OPC-UA et jumeaux numériques",
    18: "Identités non humaines (NHI) de première classe et délégation cryptographique",
    19: "Modélisation des menaces multi-agents (OWASP ASI01–ASI10) et sécurité MCP",
    20: "Défense en profondeur : bacs à sable, garde-fous neuro-symboliques et coupe-circuits",
    21: "Observabilité distribuée de bout en bout avec OpenTelemetry GenAI",
    22: "Cycle de vie ADLC, CI/CD probabiliste, simulation (τ-bench) et ingénierie du chaos",
    23: "FinOps agentique : gouvernance économique et Cost-per-Outcome",
    24: "Conformité réglementaire internationale et canadienne, et droit B2B inter-agents",
    25: "Modèle opérationnel cible, facteur humain (HOTL) et prospective 2028–2030",
    26: "Maillages B2B inter-entreprises, espaces de données et négociation multi-parties",
    27: "Souveraineté cognitive, portabilité multi-cloud et reprise après sinistre cognitif",
    28: "Orchestration en périphérie, opérations déconnectées et passerelles vers l'IA physique",
    29: "Usine logicielle agentique (Agentic SDLC) et modernisation assistée du patrimoine",
    30: "Agentic DataOps, contrats de données auto-réparateurs et SRE autonome",
    31: "Volants d'inertie cognitifs, compilation de consignes et distillation LLM → SLM",
}
TITRE_OUVERTURE = "Ouverture — Architecture et gouvernance du tissu conjonctif agentique"
ANNEXES_G = {
    "A": ("F", "Décisions d'architecture (ADR) et arbres de choix"),
    "B": ("G", "Listes de contrôle d'homologation avant production (75 points)"),
    "C": ("H", "Glossaire normatif français-anglais et index des standards"),
}

# Retouches manuelles du texte G, appliquées après les transformations mécaniques.
# Clé : identifiant d'unité (« ouverture », numéro de chapitre G, lettre d'annexe G).
# Valeur : (expression régulière, remplacement, nombre d'occurrences attendu); le script
# s'arrête si le compte diffère. Elles corrigent ce qui décrivait l'ancienne structure
# de l'édition G : dix parties, 31 chapitres, 612 pages, enchaînement des chapitres.
VOLETS = "volets « Mise en œuvre »"
RETOUCHES = {
    "ouverture": [
        (r"\*\*Portée exécutive de l.Ouverture \(Cadrage du compendium — 612 pages\)\*\*",
         "**Portée de l'ouverture**", 1),
        (r"suivie tout au long des 31 chapitres", "suivie tout au long des " + VOLETS, 1),
        (r"Ce compendium de 612 pages part", "Ce compendium part", 1),
        (r"qui charpente les dix parties de cet ouvrage", "qui charpente cet ouvrage", 1),
        (r"\| Parties I & IV \|", "| Parties I et IV |", 1),
        (r"\| Parties V, IX & X \|", "| Parties V et IX |", 1),
        (r"\| Parties VI & IX \|", "| Parties VI et IX |", 1),
        (r"\| Parties VII, VIII & X \|", "| Parties VI à IX |", 1),
        (r"Un ouvrage de 612 pages couvrant", "Un ouvrage couvrant", 1),
        (r"l’ordre des dix parties suive", "l’ordre des neuf parties suive", 1),
        (r"(Lecture intégrale des parties I, II, IV, V et IX) \(chapitres [^)]*\)", r"\1", 1),
        (r"et l’Annexe A \(arbres", "et l’annexe F (arbres", 1),
        (r"lecture approfondie de la partie VI complète \((chapitres 30 à 32)\)",
         r"lecture approfondie des \1", 1),
        (r"→ Annexe B\.1 et B\.5\.", "→ annexe G (grilles G.1 et G.5).", 1),
        (r"→ partie VII complète \((chapitres 33, 34 et 40)\)", r"→ \1", 1),
        (r"→ Annexe B\.2 et B\.3\.", "→ annexe G (grilles G.2 et G.3).", 1),
        (r"→ partie III complète \((chapitres 12 à 14)\)", r"→ \1", 1),
        (r"Ouverture \(Section 0\.4\)", "Ouverture (section 0.4)", 1),
        (r"→ partie VIII complète \((chapitres 38 et 41)\)", r"→ \1", 1),
        (r"→ Annexe B\.4\.", "→ annexe G (grille G.4).", 1),
        (r"\(parties II à X\)", "(parties II à IX)", 1),
        (r"les 31 chapitres de ce compendium suivent", "les " + VOLETS + " suivent", 1),
        (r"\(Point zéro du compendium\)", "(point zéro du fil rouge)", 1),
        (r"Chaque chapitre de ce compendium prendra appui",
         "Chaque volet « Mise en œuvre » prendra appui", 1),
        (r"Articulation logique des dix parties du compendium",
         "Articulation logique des neuf parties du compendium", 1),
        (r"- Les parties I à III \(chapitres [^)]*\) construisent",
         "- Les parties I à III construisent", 1),
        (r"- Les parties IV et V \(chapitres [^)]*\) bâtissent",
         "- Les parties IV et V bâtissent", 1),
        (r"- Les parties VI à VIII \(chapitres [^)]*\) verrouillent",
         "- Les parties VI à VIII verrouillent", 1),
        (r"- Les parties IX et X \(chapitres? [^)]*\) projettent", "- La partie IX projette", 1),
    ],
    1: [(r"Avant de passer à la conception détaillée des plans de contrôle déterministes "
         r"au chapitre 17, vérifiez que", "Vérifiez que", 1)],
    3: [(r"Avant d’aborder en partie II (l’ingénierie détaillée des protocoles "
         r"d’interopérabilité \(MCP, A2A, OASF\)), confirmez",
         r"Avant d’engager \1, traitée en partie II, confirmez", 1)],
    4: [(r"Avant d’implémenter la connectivité verticale au chapitre 5, vérifiez",
         "Avant d’implémenter la connectivité verticale (chapitre 5), vérifiez", 1)],
    14: [(r"Avant d’aborder au chapitre 27 la fédération des plateformes SaaS patrimoniales, "
          r"validez",
          "Avant de fédérer les plateformes SaaS patrimoniales (chapitre 27), validez", 1)],
    20: [(r"Pour clore cette partie VI dédiée à (l’identité, à la sécurité Zero Trust et à la "
          r"résilience cyber), vérifiez ces huit ultimes exigences",
          r"Pour clore les volets consacrés à \1 (chapitres 30 à 32), vérifiez ces huit exigences",
          1)],
    25: [(r"### Transition vers les parties IX et X — [Dd]u périmètre",
          "### Transition vers la partie IX — du périmètre", 1),
         (r"Le premier \(partie IX, (chapitres 45 et 46)\)", r"Le premier (\1)", 1),
         (r"Le second chantier \(partie X, (chapitre 47)\)", r"Le second chantier (\1)", 1)],
    31: [(r"(?m)^(## 47\.\d+ Décision d’architecture normative), conclusion générale du "
          r"compendium et points de contrôle$",
          r"\1, conclusion générale et points de contrôle", 1),
         (r"### Conclusion générale du compendium — [Ll]’architecture comme art de domestiquer et "
          r"composer l’autonomie",
          "### Conclusion générale — l’architecture comme art de domestiquer et de composer "
          "l’autonomie", 1),
         (r"Au terme des dix parties et des trente et un chapitres de ce compendium de six "
          r"cents pages, une conviction", "Au terme de ce compendium, une conviction", 1),
         (r"\| Partie du compendium \|", "| Domaine |", 1),
         (r"(?m)^\| \*\*[IVX]+ — ", "| **", 10)],
    "A": [(r"Cette première annexe rassemble", "Cette annexe rassemble", 1),
          (r"établies à travers les dix parties du compendium",
           "établies au fil des " + VOLETS, 1),
          (r"Chaque chapitre de cet ouvrage formalise",
           "Chaque volet « Mise en œuvre » formalise", 1)],
    "C": [(r"Cette dernière annexe établit", "Cette annexe établit", 1)],
}

FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
PROTEGE = re.compile(r"(`+[^`\n]*?`+|\$\$[^\n]+?\$\$|(?<![\\$])\$(?![\s$])[^$\n]*?(?<![\s\\])\$"
                     r"|<!--.*?-->|\]\([^)\n]*\))")


def hors_code(texte, fonction):
    """Applique une fonction au texte courant : ni code, ni formule, ni cible de lien."""
    sortie = []
    cloture = None
    for ligne in texte.split("\n"):
        m = FENCE.match(ligne)
        if cloture:
            if m and m.group(1).startswith(cloture) and not ligne.strip().strip("`~"):
                cloture = None
            sortie.append(ligne)
        elif m:
            cloture = m.group(1)
            sortie.append(ligne)
        else:
            morceaux = PROTEGE.split(ligne)
            for i in range(0, len(morceaux), 2):
                morceaux[i] = fonction(morceaux[i])
            sortie.append("".join(morceaux))
    return "\n".join(sortie)


# ---------------------------------------------------------------- édition C

def epure_c(texte, nom):
    """Retire du bandeau d'en-tête la version, l'audit et les notes de fabrication."""
    lignes = texte.split("\n")
    for i, ligne in enumerate(lignes[:12]):
        if not ligne.startswith("> **"):
            continue
        neuve, n1 = re.subn(
            r"^> \*\*(?:Chapitre pilote, version|Version) \d+ — \d+ \w+ \d{4}\.\*\* ", "> ", ligne)
        neuve, n2 = re.subn(
            r" (?:Chapitre|Annexe) audit(?:é|ée) et révis(?:é|ée) le \d+ \w+ \d{4}\.", "", neuve)
        neuve = re.sub(r" Les renvois « chapitre N » [^.]*\.", "", neuve)
        neuve = re.sub(r" Chapitre harmonisé [^.]*\.", "", neuve)
        neuve = re.sub(r"^> (État de référence|Date de référence des faits) :", r"> **\1 :**", neuve)
        if n1 != 1 or n2 != 1:
            raise SystemExit("Bandeau inattendu dans " + nom)
        lignes[i] = neuve
        return "\n".join(lignes)
    raise SystemExit("Bandeau introuvable dans " + nom)


def fichier_c(motif):
    trouves = glob.glob(os.path.join(CLAUDE, motif))
    if len(trouves) != 1:
        raise SystemExit("Source C manquante ou en double : " + motif)
    with open(trouves[0], encoding="utf-8") as f:
        return os.path.basename(trouves[0]), f.read().replace("\r\n", "\n").strip() + "\n"


# ---------------------------------------------------------------- édition G

def unites_g():
    """Découpe le corps HTML en unités de niveau h1 : ouverture, parties, chapitres, annexes."""
    with open(HTML_G, encoding="utf-8") as f:
        page = f.read()
    corps = page[page.index("</nav>") + len("</nav>"):page.rindex("</body>")]
    debuts = [m.start() for m in re.finditer(r"<h1[\s>]", corps)]
    unites = []
    for i, d in enumerate(debuts):
        bloc = corps[d:debuts[i + 1] if i + 1 < len(debuts) else len(corps)]
        titre = re.sub(r"<[^>]+>", "", bloc[:bloc.index("</h1>")])
        titre = re.sub(r"\s+", " ", titre).strip()
        if titre.startswith("Ouverture"):
            cle = "ouverture"
        elif (m := re.match(r"Chapitre (\d+) —", titre)):
            cle = int(m.group(1))
        elif (m := re.match(r"Annexe ([A-C]) —", titre)):
            cle = m.group(1)
        elif titre.startswith("PARTIE"):
            cle = None            # introductions de parties : non reprises
        else:
            raise SystemExit("Titre G inattendu : " + titre)
        unites.append((cle, titre, bloc))
    return unites


def convertit(bloc, tmp):
    """HTML -> Markdown par pandoc et le filtre de style; les figures vont dans tmp/media."""
    source = os.path.join(tmp, "unite.html")
    with open(source, "w", encoding="utf-8") as f:
        f.write("<html><body>" + bloc + "</body></html>")
    resultat = subprocess.run(
        ["pandoc", source, "-f", "html", "-t", "commonmark_x-smart", "--wrap=none",
         "--lua-filter", FILTRE, "--extract-media", "media"],
        check=True, capture_output=True, cwd=tmp)
    if resultat.stderr.strip():
        print("pandoc :", resultat.stderr.decode("utf-8", "replace").strip())
    return resultat.stdout.decode("utf-8").replace("\r\n", "\n")


def largeurs_tableaux(md):
    """Reporte les largeurs de colonnes d'origine dans la ligne de séparation des tableaux."""
    lignes = md.split("\n")
    sortie = []
    attente = None
    for ligne in lignes:
        m = re.match(r"<!-- colonnes: ([\d ]*)-->$", ligne)
        if m:
            attente = [int(x) for x in m.group(1).split()]
            continue
        if attente is not None and re.match(r"^\|[ :|-]+\|$", ligne):
            cellules = ligne.strip("|").split("|")
            if len(cellules) == len(attente) and sum(attente) > 0:
                neuves = []
                for cellule, largeur in zip(cellules, attente):
                    c = cellule.strip()
                    tirets = "-" * max(3, largeur)
                    neuves.append((":" if c.startswith(":") else "") + tirets
                                  + (":" if c.endswith(":") else ""))
                ligne = "|" + "|".join(neuves) + "|"
            attente = None
        sortie.append(ligne)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(sortie))


def formate(numeros):
    """[5, 6, 10, 11] -> « 5, 6, 10 et 11 »; [12, 13, 14] -> « 12 à 14 »."""
    groupes = []
    for n in numeros:
        if groupes and n == groupes[-1][-1] + 1:
            groupes[-1].append(n)
        else:
            groupes.append([n])
    morceaux = []
    for g in groupes:
        if len(g) >= 3:
            morceaux.append("%d à %d" % (g[0], g[-1]))
        else:
            morceaux.extend(str(n) for n in g)
    if len(morceaux) == 1:
        return morceaux[0]
    return ", ".join(morceaux[:-1]) + " et " + morceaux[-1]


RENVOI = re.compile(r"(?P<mot>[Cc]hapitres?|Chap\.)(?P<esp>[  ])"
                    r"(?P<liste>\d+(?:(?:\s?,\s|\s+et\s+|\s+à\s+)\d+)*)(?!\d|\.\d)")
ARTICLE = {"les": "le", "Les": "Le", "des": "du", "Des": "Du", "aux": "au", "Aux": "Au"}


def renvois(texte, journal):
    """Recalcule les renvois « Chapitre N » de l'édition G vers les chapitres hôtes."""
    sortie = []
    fin = 0
    for m in RENVOI.finditer(texte):
        numeros = []
        for element in re.split(r"\s?,\s|\s+et\s+", m.group("liste")):
            bornes = [int(x) for x in re.split(r"\s+à\s+", element)]
            numeros.extend(range(bornes[0], bornes[-1] + 1))
        if not numeros or any(n not in HOTE for n in numeros):
            journal.append("non recalculé : " + m.group(0))
            continue
        hotes = sorted({HOTE[n] for n in numeros})
        avant = texte[fin:m.start()]
        pluriel = m.group("mot").endswith("s")
        if pluriel and len(hotes) == 1:
            am = re.search(r"\b(les|Les|des|Des|aux|Aux)(\W*)$", avant)
            if am:
                avant = avant[:am.start()] + ARTICLE[am.group(1)] + am.group(2)
            else:
                journal.append("pluriel devenu singulier sans article : …%s%s"
                               % (avant[-25:], m.group(0)))
        if m.group("mot") == "Chap.":
            mot = "Chap."
        else:
            mot = "chapitre" if len(hotes) == 1 else "chapitres"
            if re.search(r"[.!?][\s*(« ]+$", texte[:m.start()]):
                mot = mot.capitalize()
        sortie.append(avant + mot + m.group("esp") + formate(hotes))
        fin = m.end()
    sortie.append(texte[fin:])
    return "".join(sortie)


def ponctuation(texte):
    """Pas d'espace devant le point-virgule, comme dans l'édition C."""
    return re.sub(r"(?<=[^\s|])[   ];(?=[\s)»*_|]|$)", ";", texte)


MOT = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿŒœ]+")
# Noms propres et termes anglais que la statistique prendrait pour des noms communs.
CASSE_GARDEE = set(
    "Groupe Agent Agents Cognitive Policy Draft Ad Loop New As First Escrow Workflow Runbook "
    "Est Micro Multi Client Local Saga Cache Chapitre Critique Durable Continue Extension "
    "Trois Trace Standards Centre Excellence Agentique Audit Registre Entreprise "
    "Départemental Gouverné Orchestré Fédéré Porte Aveugle Scellé".split())
# Cas que la règle générale traite mal, corrigés après coup.
CASSE_CORRIGEE = [
    ("souveraineté Cognitive", "souveraineté cognitive"),
    ("(Français canadien", "(français canadien"),
    ("responsable Cybersécurité", "responsable cybersécurité"),
]


def statistiques(textes):
    """Compte, dans le texte courant, chaque mot en minuscules et chaque mot à majuscule
    initiale rencontré en milieu de phrase (indice d'un nom propre)."""
    bas = collections.Counter()
    haut = collections.Counter()
    for texte in textes:
        for ligne in texte.split("\n"):
            if ligne.startswith(("#", "|", ":::", "`", "    ", "<!--", "![")):
                continue
            ligne = re.sub(r"`[^`]*`|[$][^$]*[$]|[*][^*\n]+[*]", " ", ligne)
            for m in MOT.finditer(ligne):
                mot = m.group(0)
                if mot.islower():
                    bas[mot] += 1
                elif mot[0].isupper() and mot[1:].islower():
                    avant = ligne[:m.start()].rstrip()
                    if avant and avant[-1] not in ".!?:;—–(«*-|>" and not avant[-1].isdigit():
                        haut[mot] += 1
    return bas, haut


def casse_titres(md, lexique, journal):
    """Titres de l'édition G : majuscule au premier mot et aux noms propres seulement."""
    bas, haut = lexique

    def commun(mot):
        if mot in CASSE_GARDEE:
            return False
        if len(mot) == 1:
            return True                      # « L’ », « D’ » en cours de titre
        return (mot[1:].islower() and bas[mot.lower()] >= 3
                and haut[mot] * 3 < bas[mot.lower()])

    def titre(m):
        morceaux = re.split(r"([*][^*\n]+[*]|`[^`\n]+`|[{][^}]*[}]$)", m.group(3))
        premier = True
        for i in range(0, len(morceaux), 2):
            def mot(mm):
                nonlocal premier
                w = mm.group(0)
                seul = len(w) == 1 and mm.string[mm.end():mm.end() + 1] in ("’", "'")
                # Le premier mot du titre, et celui qui suit un tiret long, gardent la majuscule.
                if premier or mm.string[:mm.start()].rstrip().endswith("—"):
                    premier = False
                    return w
                if w[0].isupper() and (seul or len(w) > 1) and commun(w):
                    return w.lower()
                return w
            morceaux[i] = MOT.sub(mot, morceaux[i])
        neuf = "".join(morceaux)
        for ancien, corrige in CASSE_CORRIGEE:
            neuf = neuf.replace(ancien, corrige)
        if neuf != m.group(3):
            journal.append((m.group(3), neuf))
        return m.group(1) + (m.group(2) or "") + neuf

    return re.sub(r"(?m)^(#{2,4} )((?:\d+[.]\d+|[A-H][.]\d+|\d+[.]) )?(.+)$", titre, md)


def usage(texte):
    """Minuscule à « partie II » et à « compendium », comme dans l'édition C."""
    texte = re.sub(r"(?<![|.!?] )(?<!^)\bPartie(s?) (?=[IVX]+\b)", r"partie\1 ", texte)
    return re.sub(r"\b[Cc]ompendium(?: 2027)?\b", "compendium", texte)


def retouche(md, cle):
    for motif, neuf, attendu in RETOUCHES.get(cle, []):
        md, n = re.subn(motif, neuf, md)
        if n != attendu:
            raise SystemExit("Retouche %r : %d occurrence(s) au lieu de %d : %s"
                             % (cle, n, attendu, motif[:70]))
    if cle == "A":   # registre des ADR : la colonne « Chap. » donne le chapitre hôte
        md, n = re.subn(r"(?m)^(\| \*\*ADR-\d+\*\* \| )(\d+)( \|)",
                        lambda m: m.group(1) + str(HOTE[int(m.group(2))]) + m.group(3), md)
        if n != 31:
            raise SystemExit("Registre des ADR : %d lignes au lieu de 31" % n)
    # En tête de ligne ou d'élément de liste, le renvoi prend la majuscule.
    return re.sub(r"(?m)^(\s*(?:[-*+] |\d+\.\s+)?)chapitre(s?)(?= \d)", r"\1Chapitre\2", md)


def figures(md, tmp, prefixe):
    """Range les figures extraites sous un nom stable et corrige leurs chemins."""
    compteur = [0]

    def renomme(m):
        compteur[0] += 1
        nom = "%s-%d.svg" % (prefixe, compteur[0])
        shutil.copyfile(os.path.join(tmp, m.group(1)), os.path.join(FIGURES, nom))
        return "](figures/%s)" % nom

    md = re.sub(r"\]\((media/[0-9a-f]+\.svg)\)", renomme, md)
    return md, compteur[0]


def volets_reecrits():
    """Vrai si des volets réécrits (Master/fusion/reecrit) diffèrent de leur original."""
    for chemin in glob.glob(os.path.join(ICI, "fusion", "reecrit", "*.md")):
        reference = os.path.join(ICI, "fusion", "origine", os.path.basename(chemin))
        if not os.path.isfile(reference):
            return True
        with open(chemin, encoding="utf-8") as f, open(reference, encoding="utf-8") as g:
            if f.read() != g.read():
                return True
    return False


def main():
    if volets_reecrits() and "--force" not in sys.argv:
        raise SystemExit(
            "Le manuscrit contient des volets réécrits (Master/fusion/reecrit) : le régénérer "
            "les remplacerait par le texte d'origine. Après une régénération voulue (--force), "
            "relancer « compendium-master-fusion.py --integre ».")
    if os.path.isdir(MANUSCRIT):
        shutil.rmtree(MANUSCRIT)
    os.makedirs(FIGURES)

    # Édition C : texte repris tel quel, bandeau épuré.
    chapitres = {}
    noms = {}
    sections_c = {}
    for n in range(1, 48):
        nom, texte = fichier_c("compendium-2027-chapitre-%02d-*.md" % n)
        chapitres[n] = epure_c(texte, nom)
        noms[n] = re.sub(r"^compendium-2027-", "", nom)
        numerotees = [int(k) for k in re.findall(r"(?m)^## %d\.(\d+) " % n, texte)]
        if numerotees != list(range(1, len(numerotees) + 1)):
            raise SystemExit("Sections de %s non consécutives" % nom)
        sections_c[n] = len(numerotees)
    annexes = {}
    for lettre in "ABCDE":
        nom, texte = fichier_c("compendium-2027-annexe-%s-*.md" % lettre)
        annexes[lettre] = (re.sub(r"^compendium-2027-", "", nom), epure_c(texte, nom))

    # Édition G : conversion, renumérotation, renvois.
    journal = []
    bilan = dict(volets=0, sections=0, extraits=0, figures=0, parties_omises=0)
    decal_sections = dict(sections_c)      # dernière section numérotée de chaque hôte
    decal_extraits = {}                    # extraits déjà placés dans chaque hôte
    volets = {n: [] for n in range(1, 48)}
    ouverture = None
    annexes_g = {}
    casse = []
    with tempfile.TemporaryDirectory() as tmp:
        converties = []
        for cle, titre, bloc in unites_g():
            if cle is None:
                bilan["parties_omises"] += 1
                continue
            converties.append((cle, titre, largeurs_tableaux(convertit(bloc, tmp))))
        lexique = statistiques(list(chapitres.values()) + [md for _, _, md in converties])
        for cle, titre, md in converties:
            md = casse_titres(md, lexique, casse)
            premiere, _, suite = md.partition("\n")
            if not premiere.startswith("# "):
                raise SystemExit("Unité G sans titre : " + titre)

            if cle == "ouverture":
                md = "# " + TITRE_OUVERTURE + "\n" + suite
                prefixe = "fig-00"
            elif isinstance(cle, str):
                lettre, neuf = ANNEXES_G[cle]
                md = "# Annexe %s — %s\n%s" % (lettre, neuf, suite)
                md, n = re.subn(r"(?m)^## %s\.(\d+) " % cle, r"## %s.\1 " % lettre, md)
                bilan["sections"] += n
                prefixe = "fig-" + lettre.lower()
            else:
                hote = HOTE[cle]
                base = decal_sections[hote]
                compte = [0]

                def section(m, base=base, hote=hote, compte=compte):
                    compte[0] += 1
                    return "## %d.%d " % (hote, base + int(m.group(1)))

                md = "## Mise en œuvre — %s {.volet}\n%s" % (TITRES_VOLET[cle], suite)
                md = re.sub(r"(?m)^## %d\.(\d+) " % cle, section, md)
                decal_sections[hote] = base + compte[0]
                bilan["sections"] += compte[0]

                # Extraits « N.k » : même indice, décalé si l'hôte accueille plusieurs volets.
                base_x = decal_extraits.get(hote, 0)
                indices = [int(k) for k in re.findall(r"Extrait %d\.(\d+)" % cle, md)]
                md = hors_code(md, lambda s, b=base_x, h=hote: re.sub(
                    r"\bExtrait %d\.(\d+)" % cle,
                    lambda m: "Extrait %d.%d" % (h, b + int(m.group(1))), s))
                decal_extraits[hote] = base_x + (max(indices) if indices else 0)
                bilan["extraits"] += len(set(indices))
                md = md.replace("**Synthèse exécutive — Chapitre %d**" % cle,
                                "**Synthèse exécutive**")
                md = re.sub(r"(?m)^(#+ Liste de contrôle de mise en production) — Chapitre %d$"
                            % cle, r"\1", md)
                prefixe = "fig-%02d" % hote
                bilan["volets"] += 1

            md = hors_code(md, lambda s: renvois(s, journal))
            md = hors_code(md, ponctuation)
            md = hors_code(md, usage)
            md = retouche(md, cle)
            if cle == "ouverture":
                md, n = figures(md, tmp, prefixe)
                ouverture = md
            elif isinstance(cle, str):
                md, n = figures(md, tmp, prefixe)
                annexes_g[ANNEXES_G[cle][0]] = md
            else:
                prefixe += "-" + "abc"[len(volets[HOTE[cle]])]
                md, n = figures(md, tmp, prefixe)
                volets[HOTE[cle]].append(md)
            bilan["figures"] += n

    def ecrit(nom, texte):
        with open(os.path.join(MANUSCRIT, nom), "w", encoding="utf-8", newline="\n") as f:
            f.write(texte.strip() + "\n")

    ecrit("ouverture.md", ouverture)
    for n in range(1, 48):
        ecrit(noms[n], "\n\n".join([chapitres[n].strip()] + [v.strip() for v in volets[n]]))
    for lettre, (nom, texte) in annexes.items():
        ecrit(nom, texte)
    slugs = {"F": "decisions-architecture", "G": "listes-controle", "H": "glossaire-normatif"}
    for lettre, md in annexes_g.items():
        ecrit("annexe-%s-%s.md" % (lettre, slugs[lettre]), md)

    print("volets : %(volets)d, sections renumérotées : %(sections)d, extraits : %(extraits)d, "
          "figures : %(figures)d, introductions de parties G omises : %(parties_omises)d" % bilan)
    print("chapitres sans volet : %s" % [n for n in range(1, 48) if not volets[n]])
    for ligne in journal:
        print("  " + ligne)
    print("titres de l'édition G dont la casse a été normalisée : %d" % len(casse))
    if "--casse" in sys.argv:
        for ancien, neuf in casse:
            print("  %s => %s" % (ancien, neuf))
    print("manuscrit : %s (%d fichiers)" % (MANUSCRIT, len(os.listdir(MANUSCRIT)) - 1))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
