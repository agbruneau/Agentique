#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compose l'echantillon de design : les memes tranches de texte, deux gabarits.

    python3 build/echantillon.py

Sortie : `echantillon-avant.pdf` et `echantillon-apres.pdf`, a la racine.

DEUX TRANCHES, et le choix des deux est une mesure, non un gout :
  ch. 1, § 1.0 -> § 1.1.2   — 7,4 % de gras, 0,7 ⚠ par page : le chapitre le
                              PLUS SOBRE du volume ;
  ch. 8, § 8.1 -> § 8.2.1   — 35,0 % de gras, 2,9 ⚠ par page : le chapitre dont
                              la densite de gras est la plus proche du corps
                              entier (34,7 %).
⚠ La premiere tranche seule mentirait. Relevee le 31 juillet 2026 sur les
cinquante chapitres de `compendium.pdf`, la part de gras va de 5,3 % a 65,2 %,
mediane 39,0 % — un echantillon pris au chapitre 1 montrerait une regle qui
n'a presque rien a corriger. Les deux tranches ensemble bornent le corpus.

Ce qui separe les deux rendus, et rien d'autre :
  avant  = `compendium.template`, tranches nues            (l'etat du 31 juillet)
  apres  = `echantillon.template`, tranches + deux figures (recommandations 1, 3, 8)

Artefact connu, propre a l'echantillon : la table des matieres numerote ses
entrees dans l'ordre (1, 2) tandis que les ouvertures portent le rang reel des
pieces (1, 8). Le volume complet n'a pas ce decalage, puisqu'il les contient
toutes.

⚠ Un echantillon ne se juge pas sur sa source. Le script MESURE les deux PDF
qu'il vient d'ecrire et imprime le releve — glyphes hors famille, part de gras,
nombre de figures. C'est ce releve qui vaut constat, pas ce fichier.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assemble  # noqa: E402  — piece(), brut(), echappe_typst()

RACINE = Path(__file__).resolve().parent.parent

# (piece, rang, debut de tranche, fin de tranche, note de statut, ancre, figure)
# L'ancre est la ligne DEVANT laquelle la figure se pose — donc en fin de la
# sous-section qu'elle illustre, jamais en tete de la suivante.
TRANCHES = [
    dict(
        piece="Livre I/01-interoperabilite-integration-entreprise.md", rang=1,
        debut=r"^## § 1\.0 ", fin=r"^### 1\.1\.3 ", note="1.8",
        ancre=r"^### 1\.0\.3 ",
        figure="![**Figure 1.0** — L'invariant de la somme : les trois termes "
               "que le chapitre éprouve, et le quatrième qu'il annonce sans "
               "l'éprouver.](../figures/f-01-00-invariant.svg)",
    ),
    dict(
        piece="Livre I/08-anatomie-mcp-a2a.md", rang=8,
        debut=r"^## § 8\.1 ", fin=r"^### 8\.2\.2 ", note="8.8",
        ancre=r"^### 8\.1\.2 ",
        figure="![**Figure 8.1** — La réduction de N×M à N+M par une couche de "
               "contrat, et les trois choses que cette couche ne porte pas."
               "](../figures/f-08-01-n-fois-m.svg)",
    ),
]

RE_PREMIERE_SECTION = re.compile(r"^## § ")

# ---- regle d'accentuation (recommandation 3), appliquee au markdown ----
# Le corpus met sous UNE SEULE graisse trois choses qui ne sont pas de meme
# espece : un terme qu'il definit, une proposition qu'il tient pour saillante,
# et une insistance de passage. A 34,7 % du texte courant, la graisse ne les
# distingue plus et ne signale plus rien. La regle les separe, et le critere
# de la deuxieme est FOURNI PAR L'AUTEUR — c'est le ⚠ qu'il posait devant :
#
#   ⚠ + gras   -> ITALIQUE. La proposition que l'auteur signale garde un
#                 accent, et c'est l'accent de clause en usage typographique.
#                 Le ⚠ lui-meme tombe au rendu (regle 1 du gabarit).
#   gras <= 3 mots -> GRAS CONSERVE. C'est un terme ; le gras le denote.
#   gras >  3 mots -> ROMAIN. Une proposition non signalee n'a pas besoin de
#                 relief : la syntaxe la porte. C'est la seule perte de la
#                 regle, et elle est reversible piece par piece.
#
# ⚠ Le seuil de trois mots est MECANIQUE et c'est assume pour un echantillon :
# une passe d'auteur trancherait au cas par cas. Il ne pretend qu'a rendre la
# proposition mesurable sur un PDF.
RE_SAILLANT = re.compile(r"⚠\s*\*\*(.+?)\*\*", re.S)
RE_GRAS = re.compile(r"\*\*(.+?)\*\*", re.S)


def accentuation(texte):
    # Par bloc separe d'une ligne vide : sans cette borne, un `**` sans fermeture
    # dans son paragraphe avalerait le paragraphe suivant.
    blocs = []
    for bloc in texte.split("\n\n"):
        bloc = RE_SAILLANT.sub(lambda m: "⚠ *" + m.group(1) + "*", bloc)
        bloc = RE_GRAS.sub(
            lambda m: m.group(0) if len(m.group(1).split()) <= 3 else m.group(1),
            bloc)
        blocs.append(bloc)
    return "\n\n".join(blocs)


def tranche(spec, applique):
    """Preambule de la piece (titre, situation, en-tete, these) + la tranche.

    `assemble.piece()` exige les trois appareils d'en-tete et coupe le corps sur
    la note de statut : la tranche garde donc le preambule intact et rouvre en
    queue la borne qu'elle vient de trancher.
    """
    lignes = (RACINE / spec["piece"]).read_text(encoding="utf-8").splitlines()
    debut, fin = re.compile(spec["debut"]), re.compile(spec["fin"])
    ancre = re.compile(spec["ancre"])

    sortie, dans_tranche = [], False
    for ligne in lignes:
        if not dans_tranche:
            if debut.match(ligne):
                dans_tranche = True
            elif RE_PREMIERE_SECTION.match(ligne):
                continue          # section hors tranche : ecartee
            else:
                sortie.append(ligne)
                continue
        elif fin.match(ligne):
            break
        if dans_tranche and applique and ancre.match(ligne):
            sortie.extend([spec["figure"], ""])
        sortie.append(ligne)
    sortie.append("")
    sortie.append(f"## § {spec['note']} — Note de statut "
                  "*(hors plan — à retirer à la publication)*")
    texte = "\n".join(sortie) + "\n"
    return accentuation(texte) if applique else texte


def compose(gabarit, applique, sortie):
    tmp = Path(tempfile.mkdtemp())
    try:
        shutil.copytree(RACINE / "figures", tmp / "figures")
        romain, _, verbe, sous = assemble.LIVRES[0]
        morceaux = [assemble.brut(
            f"#ouverture-livre[{assemble.echappe_typst(romain)}]"
            f"[{assemble.echappe_typst(verbe)}][{assemble.echappe_typst(sous)}]")]
        for i, spec in enumerate(TRANCHES):
            src = tmp / f"tranche-{i}.md"
            src.write_text(tranche(spec, applique), encoding="utf-8")
            corps, _ = assemble.piece(src, spec["rang"])
            morceaux.append(corps)
        (tmp / "echantillon.md").write_text("\n".join(morceaux), encoding="utf-8")

        subprocess.run(
            ["pandoc", str(tmp / "echantillon.md"), "-f", "markdown-raw_html",
             "--template", str(RACINE / "build" / f"{gabarit}.template"),
             "-t", "typst", "-o", str(tmp / "doc.typ")], check=True)

        # Les deux memes retouches que `build-pdf.sh` applique au .typ de Pandoc.
        typ = (tmp / "doc.typ").read_text(encoding="utf-8")
        typ = typ.replace("align(center)[#table", "align(left)[#table")
        typ = re.sub(r"^ *table\.hline\(\),$", "", typ, flags=re.M)
        (tmp / "doc.typ").write_text(typ, encoding="utf-8")

        subprocess.run(["typst", "compile", "--root", str(tmp),
                        str(tmp / "doc.typ"), str(sortie)], check=True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return sortie


def mesure(pdf):
    """Releve sur le PDF — jamais sur la source."""
    import fitz
    doc = fitz.open(pdf)
    texte = "".join(p.get_text() for p in doc)
    fontes, gras, italique, total = {}, 0, 0, 0
    for page in doc:
        for bloc in page.get_text("dict")["blocks"]:
            for ligne in bloc.get("lines", []):
                for span in ligne["spans"]:
                    nom = span["font"].split("+")[-1]
                    fontes[nom] = fontes.get(nom, 0) + len(span["text"])
                    # Le texte courant, et lui seul : la titraille et l'appareil
                    # sont en Corbel et n'entrent pas dans le budget d'accent.
                    if nom.startswith("Constantia"):
                        total += len(span["text"])
                        if "Bold" in nom:
                            gras += len(span["text"])
                        elif "Italic" in nom:
                            italique += len(span["text"])
    # ⚠ L'italique compte AUTANT que le gras : une regle qui deplacerait
    # l'accent de l'un vers l'autre ne corrigerait rien, et le premier essai de
    # cet echantillon a fait exactement cela.
    return (f"{doc.page_count:3} p | ⚠ {texte.count('⚠'):3} | "
            f"gras {100 * gras / total:5.1f} % | "
            f"ital. {100 * italique / total:5.1f} % | "
            f"hors famille {sum(c for n, c in fontes.items() if n.startswith(('SegoeUI', 'Cambria'))):3} car. | "
            f"{len(re.findall(r'Figure [0-9]', texte))} fig. | "
            f"{len(re.findall(r'Tableau [0-9]', texte))} tabl.")


def main():
    for gabarit, figure, nom in (("compendium", False, "echantillon-avant.pdf"),
                                 ("echantillon", True, "echantillon-apres.pdf")):
        pdf = compose(gabarit, figure, RACINE / nom)
        print(f"{nom:24} {mesure(pdf)}")


if __name__ == "__main__":
    main()
