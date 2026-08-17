#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compose « État de Art.pdf » depuis « État de Art.md », au gabarit du compendium.

    python "5 - Recension/build/rendre-recension.py"

⚠ LE `.md` EST LA SEULE SOURCE QUI FAIT FOI. Le PDF s'en compose, jamais
l'inverse, et les pièces de `chapitres/` ne sont que le brouillon de la boucle :
elles ne sont plus lues une fois le rapport assemblé.

Prérequis : Pandoc ≥ 3.1.7, Typst ≥ 0.12, et les fontes Constantia / Corbel
(replis Cambria / Candara, puis Libertinus Serif). Le script les VÉRIFIE et
sort en erreur : composer à moitié serait pire que ne pas composer.

CE QU'IL FAIT DU MARKDOWN, et c'est tout ce qu'il en fait :
  `## Chapitre N — Titre`  ->  ouverture « CHAPITRE N » + titre de rang 1
  `## Autre chose — Titre` ->  ouverture « AUTRE CHOSE » sans rang + titre
  `### …` `#### …`         ->  descendus d'un cran, et NUMÉROTÉS N.M / N.M.K
                               quand la pièce a un rang et que le titre n'en
                               porte pas déjà un
  `---` seul               ->  retiré, ce n'est qu'un séparateur de lecture
  `: Tableau N.M — …`      ->  étiquette en gras, comme au compendium

⚠ CE QUI PRÉCÈDE LE PREMIER `##` NE PASSE PAS AU PDF — titre du document et
ligne d'auteur y sont portés par la page de titre du gabarit. Tout contenu doit
donc vivre sous un `##`, l'ouverture comprise.

⚠ `figures/` EST COPIÉ DANS LE DOSSIER TEMPORAIRE, et il faut le faire : Typst
résout les chemins d'image depuis le `.typ`, qui vit hors de l'arborescence du
rapport. Les figures se pointent donc en `figures/…svg` dans le markdown — même
chemin de part et d'autre —, et un SVG absent ferait échouer la composition, non
un rendu à trou.

⚠ AUCUNE PORTE DE PAGINATION, contrairement à la chaîne du compendium : les
mille pages exactes sont une instruction propre à ce volume-là. Ici le nombre de
pages est un constat, et il s'affiche pour être lu, pas pour être tenu.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SOURCE = RACINE / "État de Art.md"
SORTIE = RACINE / "État de Art.pdf"
GABARIT = RACINE / "build" / "recension.template"
FIGURES = RACINE / "figures"
FILTRE = RACINE / "build" / "accentuation.lua"

RE_CHAPITRE = re.compile(r"^## Chapitre (\d+)\s+[—-]\s+(.+)$")
RE_PIECE = re.compile(r"^## (.+?)\s+[—-]\s+(.+)$")
RE_RANG_ECRIT = re.compile(r"^\d+(\.\d+)*\b")
# Le rang d'un tableau suit celui de sa pièce, et une pièce sans rang porte une
# lettre : « Tableau E.1 » au sommaire exécutif, faute de numéro de chapitre.
RE_LEGENDE = re.compile(r"^(:\s*)(Tableaux? [\dA-Z]+\.\d+)")
# Un bloc de code ne se transforme pas : un `## ` en son sein est du contenu.
RE_CLOTURE = re.compile(r"^\s*(```|~~~)")


def brut(code):
    return "```{=typst}\n" + code + "\n```\n"


def echappe(texte):
    """Neutralise le balisage Typst d'une étiquette insérée en argument."""
    for c in '\\#$@[]*_`<>"':
        texte = texte.replace(c, "\\" + c)
    return texte


def assemble(lignes):
    """Rend le markdown de composition, et le nombre de chapitres rencontrés."""
    sortie, chapitres = [], 0
    rang = ""          # rang de la pièce courante ; "" pour une liminaire
    compteurs = [0, 0]  # sections, sous-sections
    dans_code = False
    commence = False

    for ligne in lignes:
        if RE_CLOTURE.match(ligne):
            dans_code = not dans_code
            if commence:
                sortie.append(ligne)
            continue
        if dans_code:
            if commence:
                sortie.append(ligne)
            continue

        m = RE_CHAPITRE.match(ligne)
        if m:
            chapitres += 1
            if int(m.group(1)) != chapitres:
                sys.exit(f"[rendre] chapitre {m.group(1)} rencontré, {chapitres} attendu — "
                         "la numérotation des chapitres doit être contiguë")
            commence, rang, compteurs = True, m.group(1), [0, 0]
            sortie.append(brut(f'#ouverture-piece("CHAPITRE", "{rang}")'))
            sortie.append(f"# {m.group(2).strip()}\n")
            continue

        if ligne.startswith("## "):
            m = RE_PIECE.match(ligne)
            etiquette, titre = (m.group(1), m.group(2)) if m else (ligne[3:], ligne[3:])
            # Le titre d'une liminaire est la QUEUE de l'intitulé, l'étiquette
            # en étant la tête : « Épilogue — ce que… » donne le bandeau
            # « ÉPILOGUE » et le titre « Ce que… ». Sans cette majuscule, la
            # table des matières porte une entrée en bas de casse.
            titre = titre[:1].upper() + titre[1:]
            commence, rang, compteurs = True, "", [0, 0]
            sortie.append(brut(f'#ouverture-piece("{echappe(etiquette.strip().upper())}", none)'))
            sortie.append(f"# {titre.strip()}\n")
            continue

        if not commence:
            continue

        if ligne.startswith("### ") or ligne.startswith("#### "):
            profond = 1 if ligne.startswith("#### ") else 0
            titre = ligne.lstrip("#").strip()
            if profond == 0:
                compteurs = [compteurs[0] + 1, 0]
            else:
                compteurs[1] += 1
            # Un rang déjà écrit par l'auteur fait foi : on ne le double pas.
            if rang and not RE_RANG_ECRIT.match(titre):
                numero = f"{rang}.{compteurs[0]}" + (f".{compteurs[1]}" if profond else "")
                titre = f"{numero} {titre}"
            sortie.append("#" * (2 + profond) + f" {titre}\n")
            continue

        if ligne.startswith("##### "):
            sortie.append("#### " + ligne[6:])
            continue

        if ligne.strip() == "---":
            continue

        sortie.append(RE_LEGENDE.sub(r"\1**\2**", ligne))

    return "\n".join(sortie) + "\n", chapitres


def main():
    for outil in ("pandoc", "typst"):
        if shutil.which(outil) is None:
            sys.exit(f"[rendre] Dépendance manquante : {outil}")
    for chemin in (SOURCE, GABARIT, FILTRE, FIGURES):
        if not chemin.exists():
            sys.exit(f"[rendre] Introuvable : {chemin}")

    texte, chapitres = assemble(SOURCE.read_text(encoding="utf-8").splitlines())
    if chapitres == 0:
        sys.exit("[rendre] Aucun « ## Chapitre N — … » dans la source : rien à composer.")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "recension.md").write_text(texte, encoding="utf-8")
        shutil.copytree(FIGURES, tmp / "figures",
                        ignore=shutil.ignore_patterns("*.py", "__pycache__"))
        subprocess.run(
            ["pandoc", str(tmp / "recension.md"), "-f", "markdown-raw_html",
             f"--template={GABARIT}", f"--lua-filter={FILTRE}",
             "-t", "typst", "-o", str(tmp / "doc.typ")],
            check=True)

        typ = (tmp / "doc.typ").read_text(encoding="utf-8")
        # Les deux mêmes reprises qu'au compendium, et pour les mêmes motifs :
        # Pandoc centre ses tableaux, et pose sous la rangée de tête un
        # `table.hline()` qui se superpose au filet de 1 pt du gabarit et
        # l'efface.
        typ = typ.replace("align(center)[#table", "align(left)[#table")
        typ = re.sub(r"^ *table\.hline\(\),$", "", typ, flags=re.MULTILINE)
        (tmp / "doc.typ").write_text(typ, encoding="utf-8")

        # Le `.typ` intermédiaire est jetable ; `RECENSION_TYP=<dossier>` le
        # garde, seule façon de rejouer un rendu en PNG pour inspecter une page.
        garde = os.environ.get("RECENSION_TYP")
        if garde:
            shutil.copy(tmp / "doc.typ", Path(garde) / "doc.typ")

        subprocess.run(["typst", "compile", "--root", str(tmp),
                        str(tmp / "doc.typ"), str(SORTIE)], check=True)

    print(f"Rendu : {SORTIE} ({chapitres} chapitres)")


if __name__ == "__main__":
    main()
