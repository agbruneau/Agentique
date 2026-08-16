#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compose « Rapport de l'art.html » et « Rapport de l'art.pdf » depuis le .md.

    Usage : python3 build/rendre-rapport.py [--html-seul] [--pdf-seul]

Prerequis : python3 >= 3.9, markdown-it-py >= 3, Chromium (headless).

POURQUOI UNE CHAINE, ET PAS UN RENDU A LA MAIN. Le depot porte deja le cas
inverse et le declare comme un defaut : « Compendium.html » est ecrit a la main,
aucun script ne la reconstruit, et ses decomptes doivent etre re-releves a la
main a chaque piece touchee — « un rendu qui ne se regenere pas se perime en
silence ». Les deux rendus du rapport se regenerent donc d'une commande, depuis
la SEULE source qui fait foi : « Rapport de l'art.md ».

CE QUE LA CHAINE NE FAIT PAS. Elle n'a AUCUNE porte de pagination. Le compendium
verifie mille pages au build parce que c'est une instruction d'auteur ; le
rapport n'a pas de cible, et son nombre de pages est un CONSTAT de rendu, jamais
une contrainte. La chaine l'affiche, elle ne l'impose pas.

REGLE DE PROVENANCE. Le rendu n'ajoute, ne retire ni ne reformule aucun enonce :
il ne fait que composer. Tout ecart entre un rendu et le .md est un defaut de
cette chaine, jamais une variante du texte.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import zlib
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SOURCE = RACINE / "Rapport de l'art.md"
SORTIE_HTML = RACINE / "Rapport de l'art.html"
SORTIE_PDF = RACINE / "Rapport de l'art.pdf"

TITRE = "Rapport de l'art — interopérabilité, orchestration et coordination agentiques"

# Chromium : chemins connus de cet environnement, puis le PATH. La chaine ne
# telecharge jamais de navigateur — un rendu qui va chercher son moteur sur le
# reseau n'est pas reproductible.
CHROMIUM_CANDIDATS = (
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/usr/bin/google-chrome",
)


# ---------------------------------------------------------------- ancres

def ardoise(texte: str, vus: dict[str, int]) -> str:
    """Rend l'ancre d'un titre, a la regle de GitHub.

    La table des matieres du rapport est ecrite en liens GitHub (`#3-la-couche-`
    ...). Rendre les ancres autrement CASSERAIT la table sans rien signaler :
    c'est la classe de defaut la plus discrete d'un rendu, et la seule que ce
    fichier traite comme bloquante (voir `verifier_ancres`).

    Regle : minuscules, ponctuation retiree sauf tiret et soulignement, espaces
    en tirets, accents CONSERVES, doublons suffixes `-1`, `-2`…
    """
    base = texte.strip().lower()
    base = re.sub(r"[^\w\- ]", "", base, flags=re.UNICODE)
    base = base.replace(" ", "-")
    n = vus.get(base, 0)
    vus[base] = n + 1
    return base if n == 0 else f"{base}-{n}"


def texte_nu(jetons, i: int) -> str:
    """Le texte brut d'un titre : le contenu `inline` entre `heading_open/close`."""
    morceaux = []
    j = i + 1
    while j < len(jetons) and jetons[j].type != "heading_close":
        if jetons[j].type == "inline":
            morceaux.append(jetons[j].content)
        j += 1
    return re.sub(r"[*`_]", "", " ".join(morceaux))


# ---------------------------------------------------------------- rendu

def rendre_fragment(markdown: str) -> tuple[str, list[tuple[int, str, str]]]:
    """Rend le corps HTML et retourne le plan (niveau, ancre, titre)."""
    try:
        from markdown_it import MarkdownIt
    except ModuleNotFoundError:  # pragma: no cover - depend de l'environnement
        sys.exit(
            "[rendre] Dependance manquante : markdown-it-py.\n"
            "         python3 -m pip install markdown-it-py"
        )

    # `gfm-like` apporte les tableaux, dont le rapport est fait. `linkify` est
    # coupe : il exige une dependance de plus, et le rapport n'ecrit aucune URL
    # nue — tous ses liens sont explicites.
    md = MarkdownIt("gfm-like", {"html": False, "typographer": False, "linkify": False})
    jetons = md.parse(markdown)

    vus: dict[str, int] = {}
    plan: list[tuple[int, str, str]] = []
    for i, jeton in enumerate(jetons):
        if jeton.type != "heading_open":
            continue
        titre = texte_nu(jetons, i)
        ancre = ardoise(titre, vus)
        jeton.attrSet("id", ancre)
        plan.append((int(jeton.tag[1]), ancre, titre))

    return md.renderer.render(jetons, md.options, {}), plan


def verifier_ancres(markdown: str, plan: list[tuple[int, str, str]]) -> list[str]:
    """Retourne les liens internes du .md qui ne visent aucun titre rendu.

    Un renvoi qui ne se resout pas est un defaut de rendu, pas une coquille de
    redaction : la table des matieres du rapport ne se lit qu'a travers eux.
    """
    connues = {ancre for _, ancre, _ in plan}
    manquantes = []
    for cible in re.findall(r"\]\(#([^)]+)\)", markdown):
        if cible not in connues:
            manquantes.append(cible)
    return manquantes


# ---------------------------------------------------------------- gabarit

FEUILLE = r"""
/* Palette complete sur :root — le theme sombre ne REDEFINIT que des jetons,
   il n'en introduit aucun. Un rendu imprime part toujours du clair. */
:root{
  --fond:#fbfaf7; --encre:#17181b; --tempere:#4a4d55; --tenu:#6f727c;
  --accent:#8a4b12; --accent-doux:#f3ece3; --filet:#ddd8cf; --filet-fort:#b9b2a6;
  --cadre:#f6f3ee; --code-fond:#f0ece5;
  --serif:Constantia,"Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
  --sans:Corbel,Candara,"Segoe UI",Optima,"Helvetica Neue",Arial,sans-serif;
  --mesure:39.5rem;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --fond:#15161a; --encre:#e6e3dc; --tempere:#b3b0a8; --tenu:#8b8880;
    --accent:#e0913f; --accent-doux:#241d14; --filet:#2e3038; --filet-fort:#454852;
    --cadre:#1b1d22; --code-fond:#22242a;
  }
}
:root[data-theme="dark"]{
  --fond:#15161a; --encre:#e6e3dc; --tempere:#b3b0a8; --tenu:#8b8880;
  --accent:#e0913f; --accent-doux:#241d14; --filet:#2e3038; --filet-fort:#454852;
  --cadre:#1b1d22; --code-fond:#22242a;
}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--fond); color:var(--encre);
  font-family:var(--serif); font-size:17px; line-height:1.62;
  text-rendering:optimizeLegibility;
}
main{max-width:var(--mesure); margin:0 auto; padding:4rem 1.35rem 6rem}

/* --- titraille --- */
h1,h2,h3,h4{font-family:var(--sans); font-weight:600; line-height:1.22;
  letter-spacing:-.005em; text-wrap:balance}
h1{font-size:2.05rem; margin:0 0 .5rem; letter-spacing:-.018em}
h2{font-size:1.42rem; margin:3.4rem 0 1rem; padding-bottom:.42rem;
  border-bottom:1px solid var(--filet-fort)}
h3{font-size:1.12rem; margin:2.3rem 0 .7rem; color:var(--accent)}
h4{font-size:1rem; margin:1.7rem 0 .5rem; color:var(--tempere)}
h1+p{font-size:1.02rem; color:var(--tempere)}

p{margin:0 0 1.05rem}
strong{font-weight:600}
em{font-style:italic; color:var(--tempere)}
strong em,em strong{color:inherit}
hr{border:0; border-top:1px solid var(--filet); margin:2.9rem 0}

a{color:var(--accent); text-decoration:none;
  border-bottom:1px solid color-mix(in srgb,var(--accent) 35%,transparent)}
a:hover{border-bottom-color:var(--accent)}

ul,ol{margin:0 0 1.05rem; padding-left:1.35rem}
li{margin:.3rem 0}
li>p{margin:0 0 .4rem}

blockquote{margin:1.4rem 0; padding:.1rem 0 .1rem 1.1rem;
  border-left:3px solid var(--accent); color:var(--tempere)}

code{font-family:ui-monospace,"Cascadia Mono",Consolas,"SF Mono",Menlo,monospace;
  font-size:.86em; background:var(--code-fond); padding:.1em .34em;
  border-radius:3px; word-break:break-word}
pre{background:var(--code-fond); padding:.9rem 1rem; border-radius:4px;
  overflow-x:auto}
pre code{background:none; padding:0}

/* --- tableaux : la matiere dense du rapport --- */
.tableau{overflow-x:auto; margin:1.5rem 0;
  border:1px solid var(--filet); border-radius:4px; background:var(--cadre)}
table{border-collapse:collapse; width:100%; font-family:var(--sans);
  font-size:.845rem; line-height:1.45}
thead th{background:var(--accent-doux); color:var(--encre); font-weight:600;
  text-align:left; vertical-align:bottom;
  border-bottom:1.5px solid var(--filet-fort)}
th,td{padding:.5rem .68rem; border-bottom:1px solid var(--filet);
  vertical-align:top; text-align:left}
tbody tr:last-child td{border-bottom:0}
td code{font-size:.85em}

/* --- bandeau de tete --- */
.colophon{font-family:var(--sans); font-size:.82rem; color:var(--tenu);
  border:1px solid var(--filet); border-radius:4px; background:var(--cadre);
  padding:.85rem 1rem; margin:0 0 2.6rem}
.colophon b{color:var(--tempere); font-weight:600}

/* --- impression : Letter, bloc horizontal releve sur le compendium --- */
@page{
  size:Letter;
  /* 30,0 mm a gauche et 28,9 mm a droite : valeurs RELEVEES par le compendium
     sur les filets vectoriels des monographies du depot, non decidees ici.
     Le vertical, lui, est propre a ce rapport : 20 mm, au-dessus de la zone
     non imprimable usuelle de 6,35 mm — le compendium avait 18 mm et signale
     que sa titraille courante y tombe sous cette zone. */
  margin:20mm 28.9mm 20mm 30mm;
}
@media print{
  :root{
    --fond:#fff; --encre:#000; --tempere:#333; --tenu:#555;
    --accent:#7a4210; --accent-doux:#f2ece4; --filet:#c9c4bb; --filet-fort:#8d877c;
    --cadre:#fff; --code-fond:#f2efe9;
  }
  body{font-size:9.6pt; line-height:1.42}
  main{max-width:none; margin:0; padding:0}
  .colophon{page-break-inside:avoid}
  h1{font-size:17pt} h2{font-size:12.6pt} h3{font-size:10.6pt} h4{font-size:9.8pt}
  h2,h3,h4{page-break-after:avoid; break-after:avoid}
  h2{page-break-before:auto}
  p,li{orphans:3; widows:3}
  table{font-size:7.6pt}
  th,td{padding:.24rem .38rem}
  .tableau{overflow:visible; page-break-inside:auto; border-radius:0}
  tr{page-break-inside:avoid}
  a{color:var(--encre); border-bottom:0}
  /* Les renvois internes ne s'impriment pas en URL : la table des matieres du
     rapport est deja paginee par le rendu, et une URL par lien la rendrait
     illisible. */
}
"""

GABARIT = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="État détaillé du champ agentique, établi sur le seul contenu du dépôt Agentique.">
<meta name="generator" content="build/rendre-rapport.py">
<style>{feuille}</style>
</head>
<body>
<main>
<div class="colophon">
<b>Rendu dérivé.</b> Cette page est composée depuis <code>Rapport de l'art.md</code>,
<b>seule source qui fait foi</b>, par <code>build/rendre-rapport.py</code>. Elle
n'ajoute, ne retire ni ne reformule aucun énoncé — tout écart avec le <code>.md</code>
est un défaut de la chaîne de rendu, jamais une variante du texte.
<b>Aucune ressource externe</b> : ni police, ni script, ni image distante.
<b>Aucune porte de pagination</b> : le nombre de pages du PDF est un constat, non une cible.
</div>
{corps}
</main>
</body>
</html>
"""


# ---------------------------------------------------------------- PDF

def trouver_chromium() -> str:
    for chemin in CHROMIUM_CANDIDATS:
        if os.path.isfile(chemin) and os.access(chemin, os.X_OK):
            return chemin
    trouve = shutil.which("chromium") or shutil.which("google-chrome")
    if trouve:
        return trouve
    sys.exit(
        "[rendre] Chromium introuvable.\n"
        "         Attendu a l'un de : " + ", ".join(CHROMIUM_CANDIDATS)
    )


def composer_pdf(chemin_html: Path, sortie: Path) -> None:
    navigateur = trouver_chromium()
    with tempfile.TemporaryDirectory() as profil:
        commande = [
            navigateur,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=20000",
            f"--user-data-dir={profil}",
            f"--print-to-pdf={sortie}",
            chemin_html.resolve().as_uri(),
        ]
        res = subprocess.run(commande, capture_output=True, text=True, timeout=300)
    if not sortie.exists() or sortie.stat().st_size == 0:
        sys.exit(f"[rendre] Chromium n'a produit aucun PDF.\n{res.stderr[-2000:]}")


def compter_pages(pdf: Path) -> int | None:
    """Compte les pages sans dependance tierce, ou rend None.

    On inflate les flux compresses puis on compte les objets `/Type /Page`. Si
    le compte est douteux, la fonction rend None : un chiffre sans provenance
    sure ne vaut pas mieux que pas de chiffre.
    """
    brut = pdf.read_bytes()
    matiere = bytearray(brut)
    for flux in re.findall(rb"stream\r?\n(.*?)endstream", brut, re.S):
        try:
            matiere += zlib.decompress(flux)
        except zlib.error:
            continue
    pages = len(re.findall(rb"/Type\s*/Page[^s]", bytes(matiere)))
    return pages or None


# ---------------------------------------------------------------- entree

def main() -> int:
    arg = argparse.ArgumentParser(description=__doc__)
    arg.add_argument("--html-seul", action="store_true")
    arg.add_argument("--pdf-seul", action="store_true")
    opts = arg.parse_args()

    if not SOURCE.exists():
        sys.exit(f"[rendre] Source introuvable : {SOURCE}")

    markdown = SOURCE.read_text(encoding="utf-8")
    corps, plan = rendre_fragment(markdown)

    # Pandoc-like : chaque tableau va dans son propre conteneur defilant, sinon
    # le corps de la page defile horizontalement sur petit ecran.
    corps = corps.replace("<table>", '<div class="tableau"><table>')
    corps = corps.replace("</table>", "</table></div>")

    manquantes = verifier_ancres(markdown, plan)
    if manquantes:
        sys.exit(
            "[rendre] Renvois internes non resolus — le rendu casserait la table :\n"
            + "\n".join(f"         #{c}" for c in sorted(set(manquantes)))
        )

    if not opts.pdf_seul:
        page = GABARIT.format(
            titre=html.escape(TITRE, quote=True), feuille=FEUILLE, corps=corps
        )
        SORTIE_HTML.write_text(page, encoding="utf-8", newline="\n")
        octets = SORTIE_HTML.stat().st_size
        print(f"Rendu : {SORTIE_HTML.name} ({octets:n} octets, {len(plan)} titres)")
    elif not SORTIE_HTML.exists():
        sys.exit("[rendre] --pdf-seul exige un HTML deja compose.")

    if not opts.html_seul:
        composer_pdf(SORTIE_HTML, SORTIE_PDF)
        pages = compter_pages(SORTIE_PDF)
        octets = SORTIE_PDF.stat().st_size
        compte = f"{pages} pages" if pages else "pagination non mesuree"
        print(f"Rendu : {SORTIE_PDF.name} ({octets:n} octets, {compte})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
