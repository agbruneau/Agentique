#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rend le `.html` d'une pièce du compendium depuis son `.md`, sur le gabarit commun.

    python rendre-piece.py "2 - Compendium/Livre I/02-donnees-semantique-ontologies.md"

Écrit le `.html` frère. Le `.md` reste la source : ce script **dérive**, il ne crée rien. Toute
correction se fait au `.md` puis se régénère — jamais l'inverse.

Pourquoi un script plutôt que dix pages écrites à la main : la conversion est mécanique, et sa
partie mécanique est précisément celle qu'on rate en la refaisant. Une classe oubliée sur un
encadré, une ancre qui ne correspond plus à son titre, une légende de table perdue — autant de
défauts que le vérificateur attrape après coup et que le générateur ne produit pas.

CE QUE LE SCRIPT RECONNAÎT DANS LE `.md`

    # Titre                          -> en-tête de page (le numéro est extrait du titre)
    *ligne en italique*              -> phrase de situation
    | Champ | Valeur |  (5 lignes)   -> en-tête à cinq champs
    > **Thèse** …                    -> bloc de thèse
    ## § N.M — Titre                 -> section, ancre et entrée de navigation
    ### N.M.K Titre                  -> sous-section
    #### N.M.K.L Titre               -> sous-sous-section
    > **Perspective recherche.** …   -> encadré de recherche
    > **Mise en œuvre.** …           -> encadré de mise en œuvre
    ⚠ …  (paragraphe)                -> encadré d'avertissement (le ⚠ est retiré, le CSS le pose)
    Lecture de l'auteur — …          -> marquage CA-IV-07
    | … | … |  (table)               -> table défilable
    : Tableau N.M — …                -> légende de table
    - puce  /  1. numéro             -> listes
    ## § N — Note de statut …        -> bloc de statut (le reste de la pièce y entre)

Ce qu'il ne fait pas : juger. La fidélité au TOC, le régime de preuve et le marquage des inférences
restent à la relecture, et le résultat se contrôle avec `verifier-piece.py`.
"""

import html
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
GABARIT = os.path.join(ICI, "..", "assets", "gabarit.html")

LIVRES = {
    "I": "Coopérer",
    "II": "Faire confiance",
    "III": "Encadrer",
    "IV": "Appliquer, exploiter, produire et composer",
    "V": "Livrer et clore",
}


# --------------------------------------------------------------------------- inline
def _inline(texte):
    """Convertit le balisage en ligne. L'ordre compte : le code d'abord, pour que son contenu
    échappe aux autres règles."""
    jetons = []

    def _garder(html_fragment):
        jetons.append(html_fragment)
        return "\x00%d\x00" % (len(jetons) - 1)

    texte = re.sub(r"`([^`]+)`",
                   lambda m: _garder("<code>%s</code>" % html.escape(m.group(1))), texte)
    texte = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                   lambda m: _garder('<a class="lien" href="%s">%s</a>'
                                     % (html.escape(m.group(2), quote=True),
                                        html.escape(m.group(1)))), texte)
    texte = html.escape(texte, quote=False)
    # ⚠ Le gras se convertit AVANT l'italique, et son contenu est non gourmand plutôt que
    # « sans étoile » : la forme courante du corpus — **Vol. I *Monographie* §1.7-1.8** — porte
    # un italique à l'intérieur d'un gras, et un motif [^*]+ la laissait telle quelle à l'écran.
    texte = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", texte)
    texte = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", texte)
    # Marquage CA-IV-07 : « Lecture de l'auteur — » en tête de phrase.
    texte = re.sub(r"(?:<strong>)?Lecture de l['’]auteur(?:</strong>)?\s*—\s*",
                   '<span class="auteur">Lecture de l\'auteur</span> ', texte)
    for i, frag in enumerate(jetons):
        texte = texte.replace("\x00%d\x00" % i, frag)
    return texte


def _bloc_paragraphes(lignes):
    """Regroupe des lignes en paragraphes `<p>`, une ligne vide séparant deux paragraphes."""
    sortie, courant = [], []
    for ligne in lignes:
        if ligne.strip():
            courant.append(ligne.strip())
        elif courant:
            sortie.append("<p>%s</p>" % _inline(" ".join(courant)))
            courant = []
    if courant:
        sortie.append("<p>%s</p>" % _inline(" ".join(courant)))
    return sortie


# --------------------------------------------------------------------------- analyse
def decouper(md):
    """Sépare la pièce en : titre, situation, champs d'en-tête, thèse, et lignes du corps."""
    lignes = md.splitlines()
    titre = num = situation = these = these_prov = None
    champs = []
    i = 0

    while i < len(lignes):
        l = lignes[i]
        if titre is None and l.startswith("# "):
            titre = l[2:].strip()
            m = re.match(r"Chapitre\s+(\d+)\s*—\s*(.*)", titre)
            if m:
                num, titre = m.group(1), m.group(2).strip()
            i += 1
            continue
        if titre and situation is None and l.startswith("*") and not l.startswith("**"):
            bloc = []
            while i < len(lignes) and lignes[i].strip():
                bloc.append(lignes[i].strip())
                i += 1
            # ⚠ Retirer UN seul astérisque de chaque bout, non tous : `strip("*")` mangeait les
            # trois d'une ligne finissant par un gras (« … **fin.*** »), laissant un gras ouvert
            # sans fermeture, que le contrôle [8] attrape après coup.
            situation = re.sub(r"^\*|\*$", "", re.sub(r"^\*|\*$", "", " ".join(bloc), count=1), count=1)
            continue
        if l.startswith("| **") and "|" in l[3:]:
            m = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", l)
            if m:
                champs.append((m.group(1), m.group(2)))
            i += 1
            continue
        if l.startswith("> **Thèse**"):
            m = re.match(r">\s*\*\*Thèse\*\*\s*(\*\(.*?\)\*)?\s*—\s*(.*)", l)
            if m:
                these_prov, these = m.group(1) or "", m.group(2)
            i += 1
            continue
        if l.strip() == "---" and these:
            return titre, num, situation, champs, these, these_prov, lignes[i + 1:]
        i += 1
    raise SystemExit("structure inattendue : titre, en-tête ou thèse introuvable")


def rendre_corps(lignes, num):
    """Rend le corps et construit la navigation. Retourne (html, entrées de nav)."""
    sortie, nav = [], []
    i, n = 0, len(lignes)
    dans_statut = False

    def vider(tampon):
        if tampon:
            sortie.extend(_bloc_paragraphes(tampon))
            tampon.clear()

    tampon = []
    while i < n:
        l = lignes[i]

        # --- titre de section -------------------------------------------------
        m = re.match(r"^##\s+§\s*([\d.]+)\s*—\s*(.*)", l)
        if m:
            vider(tampon)
            sig, titre = m.group(1), m.group(2).strip()
            ancre = "s" + sig.replace(".", "")
            statut = "Note de statut" in titre
            if statut and not dans_statut:
                sortie.append('<section class="statut" id="%s">' % ancre)
                dans_statut = True
            sortie.append('<h2%s><span class="sig">§ %s</span>%s</h2>'
                          % ("" if dans_statut else ' id="%s"' % ancre, sig, _inline(titre)))
            nav.append((sig, re.sub(r"<[^>]+>", "", _inline(titre)), ancre))
            i += 1
            continue

        m = re.match(r"^###\s+(.*)", l)
        if m:
            vider(tampon)
            sortie.append("<h3>%s</h3>" % _inline(m.group(1).strip()))
            i += 1
            continue

        m = re.match(r"^####\s+(.*)", l)
        if m:
            vider(tampon)
            sortie.append("<h4>%s</h4>" % _inline(m.group(1).strip()))
            i += 1
            continue

        # --- encadrés (blocs de citation) ------------------------------------
        if l.startswith(">"):
            vider(tampon)
            bloc = []
            while i < n and lignes[i].startswith(">"):
                bloc.append(lignes[i].lstrip(">").strip())
                i += 1
            texte = " ".join(bloc).strip()
            if texte.startswith("**Perspective recherche.**"):
                classe, label = "encadre--recherche", "Perspective recherche"
                texte = texte[len("**Perspective recherche.**"):].strip()
            elif texte.startswith("**Mise en œuvre.**"):
                classe, label = "encadre--oeuvre", "Mise en œuvre"
                texte = texte[len("**Mise en œuvre.**"):].strip()
            else:
                classe, label = "encadre--oeuvre", "Note"
            sortie.append('<div class="encadre %s">\n  <span class="encadre__label">%s</span>\n'
                          "  <p>%s</p>\n</div>" % (classe, label, _inline(texte)))
            continue

        # --- table ------------------------------------------------------------
        if l.startswith("|"):
            vider(tampon)
            rangs = []
            while i < n and lignes[i].startswith("|"):
                rangs.append([c.strip() for c in lignes[i].strip().strip("|").split("|")])
                i += 1
            if len(rangs) >= 2 and set("".join(rangs[1]).replace(" ", "")) <= set("-:"):
                entete, corps_t = rangs[0], rangs[2:]
            else:
                entete, corps_t = None, rangs
            bloc = ['<div class="tableau">', "<table>"]
            if entete:
                bloc.append("  <thead><tr>%s</tr></thead>"
                            % "".join("<th>%s</th>" % _inline(c) for c in entete))
            bloc.append("  <tbody>")
            for rang in corps_t:
                bloc.append("    <tr>%s</tr>" % "".join("<td>%s</td>" % _inline(c) for c in rang))
            bloc.extend(["  </tbody>", "</table>", "</div>"])
            sortie.append("\n".join(bloc))
            # légende éventuelle
            j = i
            while j < n and not lignes[j].strip():
                j += 1
            if j < n and lignes[j].startswith(": "):
                sortie.append('<p class="legende">%s</p>' % _inline(lignes[j][2:].strip()))
                i = j + 1
            continue

        # --- listes -----------------------------------------------------------
        if re.match(r"^\s*[-*]\s+\S", l) or re.match(r"^\s*\d+\.\s+\S", l):
            vider(tampon)
            numerotee = bool(re.match(r"^\s*\d+\.", l))
            items = []
            while i < n and (re.match(r"^\s*(?:[-*]|\d+\.)\s+\S", lignes[i])
                             or (lignes[i].startswith("  ") and lignes[i].strip() and items)):
                if re.match(r"^\s*(?:[-*]|\d+\.)\s+", lignes[i]):
                    items.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", lignes[i]).strip())
                else:
                    items[-1] += " " + lignes[i].strip()
                i += 1
            balise = "ol" if numerotee else "ul"
            classe = "numeros" if numerotee else "puces"
            sortie.append('<%s class="%s">\n%s\n</%s>'
                          % (balise, classe,
                             "\n".join("  <li>%s</li>" % _inline(x) for x in items), balise))
            continue

        # --- séparateur -------------------------------------------------------
        if l.strip() == "---":
            vider(tampon)
            i += 1
            continue

        # --- paragraphe d'avertissement --------------------------------------
        if l.lstrip().startswith("⚠"):
            vider(tampon)
            bloc = []
            while i < n and lignes[i].strip():
                bloc.append(lignes[i].strip())
                i += 1
            texte = " ".join(bloc).lstrip("⚠").strip()
            sortie.append('<div class="avert">\n  <p>%s</p>\n</div>' % _inline(texte))
            continue

        tampon.append(l)
        i += 1

    vider(tampon)
    if dans_statut:
        sortie.append("</section>")
    return "\n\n".join(sortie), nav


# --------------------------------------------------------------------------- assemblage
def main(argv):
    if len(argv) != 2:
        print("usage: rendre-piece.py <pièce.md>")
        return 2
    chemin_md = argv[1]
    if not chemin_md.endswith(".md"):
        chemin_md += ".md"
    md = open(chemin_md, encoding="utf-8").read()
    titre, num, situation, champs, these, these_prov, corps_lignes = decouper(md)
    corps, nav = rendre_corps(corps_lignes, num)

    livre = re.search(r"Livre ([IVX]+)", situation or "")
    livre_num = livre.group(1) if livre else "I"
    livre_court = "Livre %s" % livre_num
    fil = re.sub(r"\s+", " ", (situation or "")).strip().rstrip(".")

    entete_html = "\n".join(
        "    <dt>%s</dt>\n    <dd>%s</dd>" % (html.escape(c), _inline(v)) for c, v in champs)
    nav_html = "\n".join(
        '    <li><a href="#%s"><span class="num">%s</span>%s</a></li>' % (a, s, html.escape(t))
        for s, t, a in nav)

    toc_version = "v0.23"
    m = re.search(r"TOC\.md`?\)?\s*(v[\d.]+)", md)
    if m:
        toc_version = m.group(1)

    gabarit = open(GABARIT, encoding="utf-8").read()
    # Le gabarit porte ses points de substitution en commentaire ; on les remplace en bloc.
    page = gabarit
    page = re.sub(r"<!--\n  =+\n  GABARIT.*?-->\n", "", page, flags=re.S)
    page = page.replace("{{TITRE}}", html.escape(titre))
    page = page.replace("{{NUM}}", num or "")
    page = page.replace("{{LIVRE_COURT}}", livre_court)
    page = page.replace("{{LIVRE}}", html.escape(fil.split(".")[0]))
    page = page.replace("{{SITUATION}}", _inline(fil))
    page = page.replace("{{RESUME_META}}",
                        html.escape(re.sub(r"<[^>]+>", "", _inline(these))[:300], quote=True))
    page = page.replace("{{THESE}}", _inline(these))
    page = page.replace("{{TOC_VERSION}}", toc_version)
    page = page.replace("{{FICHIER_MD}}", os.path.basename(chemin_md))
    page = re.sub(r"  <ol>\n(?:.*?)\n  </ol>", "  <ol>\n%s\n  </ol>" % nav_html, page, count=1,
                  flags=re.S)
    page = re.sub(r"  <dl>\n(?:.*?)\n  </dl>", "  <dl>\n%s\n  </dl>" % entete_html, page, count=1,
                  flags=re.S)
    page = re.sub(r"<!-- \{\{CORPS\}\}.*?-->", corps, page, count=1, flags=re.S)

    chemin_html = chemin_md[:-3] + ".html"
    with open(chemin_html, "w", encoding="utf-8") as f:
        f.write(page)
    print("rendu : %s  (%d sections, %d champs d'en-tête, %d octets)"
          % (os.path.basename(chemin_html), len(nav), len(champs), len(page)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
