#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôles mécaniques d'une pièce du compendium — les deux rendus, .md et .html.

    python verifier-piece.py "2 - Compendium/Livre I/01-interoperabilite-integration-entreprise"

L'argument est le chemin **sans extension** ; les deux fichiers sont contrôlés ensemble, parce que
c'est ensemble qu'ils se versionnent. Sortie 0 si tout passe, 1 sinon.

Ce que ce script couvre — sept défauts qu'aucun rendu ne signale :

    [1] appariement      les deux rendus existent, et le .html cite bien son .md
    [2] structure HTML   balises appariées, ancres de navigation résolues
    [3] autonomie        aucune ressource externe (police, script, image, @import)
    [4] césure           lang="fr-CA" présent — la justification en dépend
    [5] légendes         toute table porte une légende, des deux côtés
    [6] en-tête          les cinq champs du PRD §6, aucun omis
    [7] renvois          les liens relatifs pointent vers des cibles existantes
    [8] résidus          du Markdown resté littéral dans le rendu (faute de générateur)

Ce qu'il ne couvre pas, et qui reste à la relecture : la fidélité au TOC, le régime de preuve, le
marquage des inférences, la justesse des renvois « ch. N ». Un script ne lit pas un plan.

⚠ Ce script est du contenu : il se vérifie comme le reste. Toute modification se valide par
mutation — introduire chacune des fautes dans une copie et vérifier que le script échoue, APRÈS
avoir constaté qu'il passe sur la pièce intacte. Sans cette seconde vérification, un script cassé
« détecte » tout.
"""

import os
import re
import sys

# Balises dont le déséquilibre casse le rendu. Les balises auto-fermantes (meta, br, img…) et les
# éléments à fermeture optionnelle sont hors liste : leur compter les fermetures produirait un faux
# positif systématique.
BALISES = [
    "html", "head", "body", "main", "nav", "section", "div", "p", "h1", "h2", "h3", "h4",
    "dl", "dt", "dd", "ol", "ul", "li", "table", "thead", "tbody", "tr", "th", "td",
    "footer", "header", "script", "style", "span", "em", "strong", "code", "a",
]

CHAMPS_ENTETE = ["Statut", "Date de gel", "Socle mobilisé", "Garde-fous balayés", "Volumétrie cible"]


def _sans_commentaires(html):
    """Retire les commentaires HTML : le gabarit y montre des balises en exemple, et les compter
    déséquilibrerait le décompte sans qu'aucun rendu n'en souffre."""
    return re.sub(r"<!--.*?-->", "", html, flags=re.S)


def controle_appariement(base, ecarts):
    chemin_md, chemin_html = base + ".md", base + ".html"
    for chemin in (chemin_md, chemin_html):
        if not os.path.isfile(chemin):
            ecarts.append("[1] rendu manquant : %s" % chemin)
    if ecarts:
        return None, None
    md = open(chemin_md, encoding="utf-8").read()
    html = open(chemin_html, encoding="utf-8").read()
    attendu = os.path.basename(chemin_md)
    if attendu not in html:
        ecarts.append("[1] le .html ne renvoie pas vers son .md (« %s » absent)" % attendu)
    return md, html


def controle_structure(html, ecarts):
    corps = _sans_commentaires(html)
    for balise in BALISES:
        ouvrants = len(re.findall(r"<%s\b" % balise, corps))
        fermants = len(re.findall(r"</%s>" % balise, corps))
        if ouvrants != fermants:
            ecarts.append("[2] balise <%s> déséquilibrée : %d ouvrante(s), %d fermante(s)"
                          % (balise, ouvrants, fermants))
    ids = set(re.findall(r'id="([^"]+)"', corps))
    ancres = set(re.findall(r'href="#([^"]+)"', corps))
    for ancre in sorted(ancres - ids):
        ecarts.append("[2] ancre de navigation sans cible : #%s" % ancre)
    if not ancres:
        ecarts.append("[2] aucune ancre de navigation — la barre latérale est vide")


def controle_autonomie(html, ecarts):
    corps = _sans_commentaires(html)
    motifs = [
        (r'<link\b[^>]*\bhref=', "balise <link> (feuille ou police distante)"),
        (r'<script\b[^>]*\bsrc=', "script distant"),
        (r'@import\b', "@import CSS"),
        (r'url\(\s*["\']?https?:', "ressource distante en url()"),
        (r'<img\b[^>]*\bsrc=\s*["\']?https?:', "image distante"),
        (r'rel="canonical"', "balise canonical — la page n'est pas publiée en ligne"),
        (r'property="og:', "balise og: — la page n'est pas publiée en ligne"),
    ]
    for motif, libelle in motifs:
        if re.search(motif, corps, re.I):
            ecarts.append("[3] %s : la page doit se lire hors ligne" % libelle)


def controle_cesure(html, ecarts):
    if not re.search(r'<html\b[^>]*\blang="fr-CA"', html):
        ecarts.append('[4] lang="fr-CA" absent de <html> : la césure automatique est désactivée '
                      "et la justification creuse des lézardes")
    # ⚠ Le motif est ancré à gauche exprès : `"hyphens: auto" in html` serait satisfait par le seul
    # `-webkit-hyphens: auto`, et une feuille qui n'aurait gardé que la forme préfixée passerait le
    # contrôle en ne coupant les mots dans aucun navigateur moderne. Trou trouvé par mutation.
    if not re.search(r"(?<![-\w])hyphens\s*:\s*auto", html):
        ecarts.append("[4] `hyphens: auto` (forme non préfixée) absent de la feuille de style")
    if not re.search(r"text-align\s*:\s*justify", html):
        ecarts.append("[4] `text-align: justify` absent de la feuille de style")


def controle_legendes(md, html, ecarts):
    corps = _sans_commentaires(html)
    tables_html = len(re.findall(r"<table\b", corps))
    legendes_html = len(re.findall(r'class="legende"', corps))
    if tables_html != legendes_html:
        ecarts.append("[5] .html : %d table(s) pour %d légende(s) — une table sans légende consomme "
                      "quand même un numéro" % (tables_html, legendes_html))

    # En Markdown, une table est un bloc de lignes commençant par « | » ; sa légende est la ligne
    # « : … » qui suit le bloc. Les tableaux de gouvernance (en-tête à cinq champs, tables de
    # correspondance) ne sont pas des tables numérotées : seules celles qui suivent une ligne vide
    # et sont suivies d'une ligne « : » comptent. On se borne donc à signaler l'écart, pas à
    # l'imposer — d'où le contrôle par égalité côté HTML seul, et un simple avis ici.
    tables_md = len(re.findall(r"^\|", md, re.M))
    if tables_md and not re.search(r"^:\s+\S", md, re.M) and legendes_html:
        ecarts.append("[5] .md : aucune légende « : … » alors que le .html en porte %d"
                      % legendes_html)


def controle_entete(md, html, ecarts):
    for champ in CHAMPS_ENTETE:
        if champ not in md:
            ecarts.append("[6] .md : champ d'en-tête manquant — « %s » (PRD §6)" % champ)
        if champ not in html:
            ecarts.append("[6] .html : champ d'en-tête manquant — « %s » (PRD §6)" % champ)
    if "Thèse" not in md:
        ecarts.append("[6] .md : la thèse citée depuis le TOC est absente")


def controle_residus(html, ecarts):
    """Balisage Markdown resté littéral dans le rendu — la faute que produit un générateur, jamais
    une écriture à la main. Elle ne casse rien : elle s'affiche, et c'est pire."""
    corps = _sans_commentaires(html)
    corps = re.sub(r"<style>.*?</style>", "", corps, flags=re.S)
    corps = re.sub(r"<script>.*?</script>", "", corps, flags=re.S)
    residus = [
        (r"\*\*", "gras Markdown non converti (**)"),
        (r"\]\(", "lien Markdown non converti ]("),
        (r"(?m)^\s*#{2,4}\s", "titre Markdown non converti (##)"),
    ]
    for motif, libelle in residus:
        n = len(re.findall(motif, corps))
        if n:
            ecarts.append("[8] %s : %d occurrence(s)" % (libelle, n))


def controle_renvois(base, md, html, ecarts):
    dossier = os.path.dirname(base) or "."
    liens = set(re.findall(r"\]\(([^)#][^)]*)\)", md))
    liens |= set(re.findall(r'href="((?!#|https?:|mailto:)[^"]+)"', _sans_commentaires(html)))
    for lien in sorted(liens):
        cible = os.path.normpath(os.path.join(dossier, lien.replace("%20", " ")))
        if not os.path.exists(cible):
            ecarts.append("[7] renvoi relatif sans cible : %s" % lien)


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[2].strip())
        return 2
    base = argv[1]
    for suffixe in (".md", ".html"):
        if base.endswith(suffixe):
            base = base[: -len(suffixe)]

    ecarts = []
    md, html = controle_appariement(base, ecarts)
    if md is not None:
        controle_structure(html, ecarts)
        controle_autonomie(html, ecarts)
        controle_cesure(html, ecarts)
        controle_legendes(md, html, ecarts)
        controle_entete(md, html, ecarts)
        controle_residus(html, ecarts)
        controle_renvois(base, md, html, ecarts)

    nom = os.path.basename(base)
    print("Contrôles de pièce — %s" % nom)
    if ecarts:
        for ecart in ecarts:
            print("  %s" % ecart)
        print("\n%d écart(s). La pièce n'est pas prête à être committée." % len(ecarts))
        return 1
    print("  [1] appariement des deux rendus       -> OK")
    print("  [2] structure HTML et ancres          -> OK")
    print("  [3] autonomie de la page              -> OK")
    print("  [4] justification et césure           -> OK")
    print("  [5] légendes des tables               -> OK")
    print("  [6] en-tête à cinq champs et thèse    -> OK")
    print("  [7] renvois relatifs                  -> OK")
    print("  [8] balisage Markdown résiduel        -> OK")
    print("\nTous les contrôles passent.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
