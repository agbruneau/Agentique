"""Compose CompendiumMaster.pdf à partir du manuscrit unifié.

Usage : python Master/compendium-master-assemble.py

Chaîne : Master/manuscrit/*.md -> Master/build/compendium.md -> pandoc (gabarit.typ,
filtres/typst.lua) -> Master/build/compendium.typ -> typst -> CompendiumMaster.pdf.
Le manuscrit n'est jamais modifié. Dépendances : pandoc et typst sur le PATH.
"""
import glob
import json
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
MANUSCRIT = os.path.join(ICI, "manuscrit")
BUILD = os.path.join(ICI, "build")
SORTIE = os.path.join(RACINE, "CompendiumMaster.pdf")
TITRE = "Interopérabilité et Orchestration en Entreprise Agentique"
EDITION = "Édition consolidée — novembre 2026"
FORMAT = "gfm+fenced_divs+implicit_figures+raw_attribute-smart-gfm_auto_identifiers"

PARTIES = [
    ("Partie I", "Fondements et cadrage", range(1, 5)),
    ("Partie II", "Protocoles et standards d'interopérabilité", range(5, 12)),
    ("Partie III", "Interopérabilité sémantique, données et contexte", range(12, 16)),
    ("Partie IV", "Orchestration", range(16, 23)),
    ("Partie V", "Architecture d'entreprise et plateformes", range(23, 29)),
    ("Partie VI", "Confiance : identité, sécurité, observabilité", range(29, 35)),
    ("Partie VII", "Gouvernance, conformité et droit", range(35, 40)),
    ("Partie VIII", "Économie, organisation et mise en œuvre", range(40, 44)),
    ("Partie IX", "Approfondissements", range(44, 48)),
    ("Partie X", "Recherche scientifique", range(48, 51)),
]
ANNEXES = "ABCDEFGH"

SEPARATEUR_TABLE = re.compile(r"^\s*\|?[\s:\-|]+\|?\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
# Ce que la typographie ne touche pas : code, formules, cibles de liens, adresses.
PROTEGE = re.compile(r"(`+[^`\n]*?`+|\$\$[^\n]+?\$\$|(?<![\\$])\$(?![\s$])[^$\n]*?(?<![\s\\])\$"
                     r"|\]\([^)\n]*\)|<https?://[^>\n]*>|https?://\S+|<!--.*?-->)")

NBSP = "\u00a0"
FINE = "\u202f"


def typographie(texte):
    """Apostrophes courbes et espaces insécables du français."""
    texte = re.sub(r"(?<=\w)'(?=\w)", "\u2019", texte)
    texte = re.sub(r" ([;!?])", FINE + r"\1", texte)
    texte = re.sub(r" :(?=\s|$|\*)", NBSP + ":", texte)
    texte = texte.replace("« ", "«" + NBSP).replace(" »", NBSP + "»")
    texte = re.sub(r"(?<=\d) %", NBSP + "%", texte)
    texte = re.sub(r"(?<=\d) (?=\$|k?\$|M\$|G\$|€)", NBSP, texte)
    return texte


def ligne_typo(ligne):
    if ligne.startswith(":::") or (SEPARATEUR_TABLE.match(ligne) and "-" in ligne):
        return ligne
    morceaux = PROTEGE.split(ligne)
    for i in range(0, len(morceaux), 2):
        morceaux[i] = typographie(morceaux[i])
    return "".join(morceaux)


def typ(texte):
    """Texte courant -> balisage Typst (titres passés au gabarit)."""
    return "[" + re.sub(r"([\\#$*_@<>\[\]`~])", r"\\\1", typographie(texte)) + "]"


def brut(code):
    return "```{=typst}\n" + code + "\n```"


def titre_unite(chemin):
    with open(chemin, encoding="utf-8") as f:
        premiere = f.readline().strip()
    if not premiere.startswith("# "):
        raise SystemExit("Titre manquant dans " + chemin)
    return premiere[2:]


def prepare(chemin, bilan):
    """Titre et volets passés au gabarit, titres décalés d'un niveau, typographie."""
    sortie = []
    cloture = None
    dans_sources = False
    precedent = None
    with open(chemin, encoding="utf-8") as f:
        lignes = f.read().splitlines()
    sur, _, titre = lignes[0][2:].partition(" — ")
    sortie.append(brut("#chapitre(%s, %s)" % (typ(sur), typ(titre))))
    for ligne in lignes[1:]:
        m = FENCE.match(ligne)
        if cloture:
            if m and m.group(1).startswith(cloture) and not ligne.strip().strip("`~"):
                cloture = None
            sortie.append(ligne)
            continue
        if m:
            cloture = m.group(1)
            sortie.append(ligne)
            continue
        if ligne.startswith("# "):
            raise SystemExit("Second titre de niveau 1 dans " + chemin)
        volet = re.match(r"## Mise en œuvre — (.*) \{\.volet\}$", ligne)
        if volet:
            dans_sources = False
            bilan["volets"] += 1
            sortie.append(brut("#volet%s" % typ(volet.group(1))))
            continue
        if re.match(r"#{2,5} ", ligne):
            dans_sources = bool(re.match(r"#+ Sources", ligne))
            precedent = None
            ligne = "#" + ligne
        # Markdown renumérote les listes : dans les sources, un saut de numéro
        # (12 puis 14) ouvre une nouvelle liste pour garder le numéro cité.
        item = re.match(r"(\d+)\. ", ligne)
        if dans_sources and item:
            numero = int(item.group(1))
            if precedent is not None and numero != precedent + 1:
                sortie.extend(["", "<!-- -->", ""])
            precedent = numero
        # Une ligne de tirets collée à un paragraphe en ferait un titre (setext).
        if (re.match(r"(-{3,}|={3,})\s*$", ligne) and sortie and sortie[-1].strip()
                and not sortie[-1].lstrip().startswith("|")):
            sortie.append("")
        sortie.append(ligne_typo(ligne))
    if cloture:
        raise SystemExit("Bloc de code non fermé dans " + chemin)
    return "\n".join(sortie).strip() + "\n"


def corrections():
    """Nombre de corrections du registre de l'audit de publication (0 s'il n'existe pas)."""
    registre = os.path.join(ICI, "audit", "corrections.json")
    if not os.path.isfile(registre):
        return 0
    with open(registre, encoding="utf-8") as f:
        return len(json.load(f))


def unique(motif):
    trouves = sorted(glob.glob(os.path.join(MANUSCRIT, motif)))
    if len(trouves) != 1:
        raise SystemExit("Fichier du manuscrit manquant ou en double : " + motif)
    return trouves[0]


def main():
    os.makedirs(BUILD, exist_ok=True)
    bilan = dict(volets=0)
    morceaux = [prepare(unique("ouverture.md"), bilan)]
    hotes = 0
    for nom, titre, numeros in PARTIES:
        chemins = [unique("chapitre-%02d-*.md" % n) for n in numeros]
        liste = "".join(typ(titre_unite(c)) + ", " for c in chemins)
        morceaux.append(brut("#partie(%s, %s, (%s))" % (typ(nom), typ(titre), liste)))
        for chemin in chemins:
            avant = bilan["volets"]
            morceaux.append(prepare(chemin, bilan))
            hotes += bilan["volets"] > avant
    chemins = [unique("annexe-%s-*.md" % lettre) for lettre in ANNEXES]
    liste = "".join(typ(titre_unite(c)) + ", " for c in chemins)
    morceaux.append(brut("#partie([Annexes], none, (%s))" % liste))
    for chemin in chemins:
        morceaux.append(prepare(chemin, bilan))

    md = os.path.join(BUILD, "compendium.md")
    typst = os.path.join(BUILD, "compendium.typ")
    with open(md, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n\n".join(morceaux))

    subprocess.run([
        "pandoc", md, "-f", FORMAT, "-t", "typst", "--standalone", "--wrap=none",
        "--template", os.path.join(ICI, "gabarit.typ"),
        "--lua-filter", os.path.join(ICI, "filtres", "typst.lua"),
        "-V", "titre=" + TITRE, "-V", "edition=" + EDITION,
        "-V", "nbvolets=%d" % bilan["volets"], "-V", "nbhotes=%d" % hotes,
        "-V", "nbcorrections=%d" % corrections(),
        "-o", typst,
    ], check=True)
    with open(typst, encoding="utf-8") as f:
        source = f.read()
    # pandoc centre les cellules sans alignement explicite : on aligne à gauche.
    source = re.sub(r"align: \((?:auto,)+\)",
                    lambda m: m.group(0).replace("auto", "left"), source)
    source = source.replace('image("figures/', 'image("../manuscrit/figures/')
    with open(typst, "w", encoding="utf-8", newline="\n") as f:
        f.write(source)
    subprocess.run(["typst", "compile", "--root", ICI, typst, SORTIE], check=True)

    pages = subprocess.run(
        ["typst", "query", "--root", ICI, typst, "<fin>", "--field", "value", "--one"],
        check=True, capture_output=True, text=True).stdout.strip()
    mots = sum(len(m.split()) for m in morceaux)
    print("pages : %s, mots (approx.) : %d" % (pages, mots))
    print("chapitres : %d, volets « Mise en œuvre » : %d dans %d chapitres, annexes : %d"
          % (sum(len(n) for _, _, n in PARTIES), bilan["volets"], hotes, len(ANNEXES)))
    print("PDF : %s (%.1f Mo)" % (SORTIE, os.path.getsize(SORTIE) / 1e6))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
