#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendu HTML d'une pièce du compendium (Vol. IV), depuis son `.md` jumeau.

⚠ **Ce script remplace un rendeur retiré du dépôt.** Les cinquante `.html`
versionnés dataient de la génération du 31 juillet 2026 (`4b3e5fc`) ; les
révisions du 31 juillet au 3 août et du 8 août n'y étaient pas, **114 des 115
figures en étaient absentes**, et les commits ultérieurs sur ces fichiers
étaient des substitutions globales de titre, non des régénérations. La règle
permanente du dépôt — *une source ne se versionne pas sans son rendu* —
était donc tenue en apparence et fausse en fait.

Ce que ce rendu porte, et ce qu'il ne porte pas
------------------------------------------------
**Le corps technique du chapitre, et lui seul** — même coupe que
`build/assemble.py` pour le PDF et que `PRD/decompte.sh` pour la volumétrie :
du premier `---` jusqu'à la **note de statut**, exclue. ⚠ **Ni l'en-tête à cinq
champs, ni la thèse citée, ni la note de statut** : *l'appareil de gouvernance
vit au `.md`, qui reste la seule source.* La purge est celle du 29 juillet 2026,
et `verifier-piece.py` refuse un rendu qui la recopierait.

Les deux défauts du rendeur retiré, corrigés ici
-------------------------------------------------
1. **Balises croisées.** L'ancien rendeur composait le HTML par substitutions
   d'expressions régulières sur le markdown, et produisait des `<em>` et des
   `<strong>` entrelacés que le navigateur re-imbriquait à sa façon. Ici, la
   conversion est confiée à **pandoc**, qui produit un arbre.
2. **Libellés de lien en span de code.** `[`texte`](url)` sortait en
   `<code>` hors du `<a>`. Pandoc met le `<code>` DANS le lien.

Usage :
    python build/rendre-piece.py                 # les cinquante pièces
    python build/rendre-piece.py "Livre I/01-*.md" ...   # celles-là
"""

import html
import os
import re
import subprocess
import sys
from pathlib import Path

# ⚠ `COMPENDIUM_RACINE` surcharge la racine, comme pour `check-compendium.py` :
# sans elle, le harnais de mutation ne pourrait pas travailler sur une copie
# jetable, et il faudrait muter le dépôt lui-même pour éprouver le contrôle.
RACINE = Path(os.environ.get("COMPENDIUM_RACINE",
                             Path(__file__).resolve().parent.parent))
GABARIT = RACINE / "build" / "piece.template"
MARQUE = "Interopérabilité et Orchestration en Entreprise Agentique"

# La coupe du corps. Identique à `corps_compendium()` de PRD/decompte.sh : s'y
# écarter donnerait deux définitions du corps, donc deux volumétries.
FIN_DU_CORPS = re.compile(r"^##\s.*Note de statut", re.M)

TITRE = re.compile(r"^#\s+Chapitre\s+(\d+)\s+—\s+(.*)$", re.M)


def pieces():
    return sorted(RACINE.glob("Livre */[0-9][0-9]-*.md"))


def decouper(texte):
    """Rend (numéro, titre, situe, corps markdown)."""
    m = TITRE.search(texte)
    if not m:
        raise SystemExit("titre « # Chapitre N — … » introuvable")
    numero, titre = int(m.group(1)), m.group(2).strip()

    # Le bloc en italique qui suit le titre porte le Livre puis le mouvement.
    apres = texte[m.end():]
    situe = ""
    bloc = re.match(r"\s*\*(.+?)\*\s*\n\s*\n", apres, re.S)
    if bloc:
        situe = " ".join(bloc.group(1).split()).rstrip(".")

    i = texte.index("\n---\n")
    corps = texte[i + 5:]
    fin = FIN_DU_CORPS.search(corps)
    if fin:
        corps = corps[:fin.start()]
    return numero, titre, situe, corps.strip()


def pandoc(markdown):
    r = subprocess.run(
        ["pandoc", "--from=markdown-smart", "--to=html5",
         "--syntax-highlighting=none", "--wrap=none"],
        input=markdown, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise SystemExit(f"pandoc a échoué : {r.stderr.strip()[:400]}")
    return r.stdout


def ancre(numero_section):
    return "s" + numero_section.replace(".", "")


# Les enveloppes sémantiques de la feuille de style, et leur source markdown.
# ⚠ Elles ne sont pas décoratives : `.avert` porte le losange d'avertissement
# par `::before`, et `.encadre--recherche` / `.encadre--oeuvre` matérialisent le
# dispositif à deux lectorats que le ch. 1 § 1.0.3 déclare et que tout le
# Livre I reconduit. Un rendu qui les perdrait afficherait le texte sans le
# dispositif — c'est-à-dire en dirait moins que le `.md`.
ENCADRES = {
    "Perspective recherche": "encadre--recherche",
    "Mise en œuvre": "encadre--oeuvre",
}

CITATION = re.compile(r"<blockquote>\s*(.*?)\s*</blockquote>", re.S)
AVERT = re.compile(r"<p>⚠\s*(.*?)</p>", re.S)
AUTEUR = re.compile(r"Lecture de l'auteur\s*—\s*")
TABLE = re.compile(r"(<table>.*?</table>)", re.S)
LEGENDE_PANDOC = re.compile(r"<caption>(.*?)</caption>\s*", re.S)


def enveloppes(h):
    """Rétablit les enveloppes sémantiques que la feuille de style attend."""

    def encadre(m):
        interieur = m.group(1)
        for libelle, classe in ENCADRES.items():
            marque = f"<strong>{libelle}.</strong>"
            if marque in interieur:
                interieur = interieur.replace(marque, "", 1).lstrip()
                interieur = re.sub(r"^<p>\s*", "<p>", interieur)
                return (f'<div class="encadre {classe}">\n'
                        f'  <span class="encadre__label">{libelle}</span>\n'
                        f'  {interieur.strip()}\n</div>')
        return m.group(0)

    h = CITATION.sub(encadre, h)
    h = AVERT.sub(lambda m: f'<div class="avert">\n  <p>{m.group(1).strip()}</p>\n</div>', h)
    h = AUTEUR.sub('<span class="auteur">Lecture de l\'auteur</span> ', h)

    # Pandoc rend « : Tableau 1.1 — … » en <caption> DANS la table ; la feuille
    # de style la veut en légende SOUS la table, et la table dans un cadre qui
    # défile — une table de neuf colonnes ne tient pas dans la colonne de texte.
    def tableau(m):
        bloc = m.group(1)
        leg = LEGENDE_PANDOC.search(bloc)
        sous = ""
        if leg:
            bloc = bloc.replace(leg.group(0), "")
            sous = f'\n<p class="legende">{leg.group(1).strip()}</p>'
        return f'<div class="tableau">\n{bloc}\n</div>{sous}'

    return TABLE.sub(tableau, h)


def figures(corps_html):
    """Normalise les `<figure>` de pandoc sur la feuille de style du volume.

    Pandoc rend déjà une image seule dans son paragraphe en
    `<figure><img><figcaption>` — l'arbre voulu, et c'est pourquoi ce script
    n'en fabrique pas un second. Deux retouches suffisent : la classe `figure`,
    que la feuille de style attend pour poser le carton clair sous des SVG
    dessinés pour le PDF ; et le retrait de `aria-hidden="true"`, que pandoc
    met sur la légende parce qu'il la croit redondante avec l'`alt`.
    ⚠ *Elle ne l'est pas ici* : au `.md`, l'`alt` **est** la légende, et la
    masquer aux lecteurs d'écran retirerait « Figure 1.0 » du seul endroit du
    rendu qui porte la numérotation.
    """
    corps_html = corps_html.replace("<figure>\n<img", '<figure class="figure">\n  <img')
    return corps_html.replace('<figcaption aria-hidden="true">', "  <figcaption>")


TITRE_H2 = re.compile(r'^<h2 id="[^"]*">(.*?)</h2>$', re.M)
NUMEROTE = re.compile(r"^§\s*([\d.]+)\s*—\s*(.*)$", re.S)


def corps_et_nav(corps_md, numero):
    brut = pandoc(corps_md)
    sections = []

    def h2(m):
        texte = m.group(1)
        n = NUMEROTE.match(texte)
        if n:
            num, titre = n.group(1), n.group(2)
            sections.append((num, titre))
            return f'<h2 id="{ancre(num)}"><span class="sig">§ {num}</span>{titre}</h2>'
        # Un h2 sans numéro de section — « Synthèse : … », par exemple. Il entre
        # à la navigation sous une ancre dérivée de son rang, jamais de son
        # titre : un titre qui bouge ne doit pas casser un lien.
        cle = f"{numero}.h{len(sections)}"
        sections.append((cle, texte))
        return f'<h2 id="{ancre(cle)}">{texte}</h2>'

    brut = TITRE_H2.sub(h2, brut)
    # Les id que pandoc dérive des titres de h3 et au-delà sont retirés : aucun
    # ancrage du volume n'en dépend, et ils changent à chaque retouche de titre.
    brut = re.sub(r'<(h[3-6]) id="[^"]*">', r"<\1>", brut)
    brut = enveloppes(brut)
    brut = figures(brut)

    if not sections:
        raise SystemExit("aucun titre de section : la coupe du corps est fausse")

    lignes = "\n".join(
        f'    <li><a href="#{ancre(n)}"><span class="num">{n}</span>'
        f'{t}</a></li>' for n, t in sections)
    return brut.strip(), lignes


def composer(md):
    """Rend le HTML de la pièce, sans l'écrire — c'est ce que le contrôle de
    parité compare au fichier versionné."""
    texte = md.read_text(encoding="utf-8")
    numero, titre, situe, corps_md = decouper(texte)
    corps, nav_lignes = corps_et_nav(corps_md, numero)

    livre = md.parent.name                      # « Livre I »
    fil = situe.split(".")[0].strip()           # « Livre I — Coopérer : … »
    e = html.escape

    nav = (f'<nav class="nav" aria-label="Table des matières du chapitre">\n'
           f'  <div class="nav__marque">{MARQUE}</div>\n'
           f'  <div class="nav__sous">{livre} · Chapitre {numero}</div>\n'
           f'  <ol>\n{nav_lignes}\n  </ol>\n'
           f'  <div class="nav__pied">\n'
           f'    Vol.&nbsp;IV — <em>{MARQUE}</em><br>\n'
           f'    <a href="{md.name}">Version Markdown</a>\n'
           f'  </div>\n</nav>')

    entete = (f'<header class="titre">\n'
              f'  <div class="titre__fil">{e(fil)}</div>\n'
              f'  <h1><span class="chap">Chapitre {numero}</span>{e(titre)}</h1>\n'
              f'  <p class="titre__situe">{situe}</p>\n'
              f'</header>')

    sortie = GABARIT.read_text(encoding="utf-8")
    for cle, valeur in (("{{TITRE_ONGLET}}", f"{e(f'Chapitre {numero} — {titre}')} · {MARQUE}"),
                        ("{{DESCRIPTION}}", e(situe)),
                        ("{{NAV}}", nav),
                        ("{{HEADER}}", entete),
                        ("{{CORPS}}", corps),
                        ("{{LIVRE}}", livre),
                        ("{{NUMERO}}", str(numero))):
        sortie = sortie.replace(cle, valeur)

    return sortie


def rendre(md):
    cible = md.with_suffix(".html")
    cible.write_text(composer(md), encoding="utf-8")
    return cible, cible.stat().st_size


def main(argv):
    cibles = [Path(a).resolve() for a in argv] if argv else pieces()
    if not cibles:
        print("aucune pièce")
        return 1
    if not GABARIT.exists():
        print(f"gabarit introuvable : {GABARIT}")
        return 1
    for md in cibles:
        f, n = rendre(md)
        print(f"  ☑ {f.relative_to(RACINE).as_posix():58} {n:>8} octets")
    print(f"\nOK — {len(cibles)} rendu(s) écrit(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
