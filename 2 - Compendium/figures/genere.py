#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genere les figures du barème A de `programme.md`, et les pose dans les pieces.

    python3 figures/genere.py            # dessine et insere
    python3 figures/genere.py --verifier # controle sans rien ecrire

Le contenu vit dans `contenu.py`, les dispositions dans `dessine.py`. Ici, deux
choses seulement : le rendu de chaque entree par la primitive qu'elle nomme, et
l'INSERTION de l'appel markdown dans la piece, devant l'ancre declaree.

⚠ L'INSERTION EST IDEMPOTENTE, et il le faut : la commande se rejoue a chaque
reprise du contenu. Une figure deja posee est REMPLACEE a sa place, jamais
ajoutee une seconde fois — la detection porte sur le nom de fichier, non sur la
legende, qui elle change.

⚠ UNE FIGURE PAR SECTION, sinon deux figures d'un meme § porteraient le meme
rang. Les cinq sections qui en portent deux (11.1, 16.1, 30.2, 31.1, 36.2) les
distinguent par un suffixe de lettre — « Figure 31.1a », « Figure 31.1b ».
"""
import hashlib
import re
import sys
from pathlib import Path

# Console Windows en cp1252 : sans cette ligne, le premier ⚠ imprimé lève
# `UnicodeEncodeError` et le contrôle meurt avant son verdict (évaluation du
# 15 septembre 2026, §8.1).
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import dessine as D
import contenu as C

RACINE = Path(__file__).resolve().parent.parent
FIGURES = Path(__file__).resolve().parent

PRIMITIVES = {
    "bandes": D.bandes, "pile": D.pile, "frise": D.frise, "chaine": D.chaine,
    "matrice": D.matrice, "paire": D.paire, "arbre": D.arbre, "venn": D.venn,
}


def piece(ch):
    for f in sorted(RACINE.glob("Livre */[0-9]*.md")):
        if re.search(r"[/\\]0*%d-" % ch, str(f)):
            return f
    sys.exit(f"[figures] chapitre {ch} introuvable")


def dessine_une(f):
    corps, haut = PRIMITIVES[f["type"]](**f["data"])
    D.rendu(f["nom"], corps, haut, f["alt"], f["source"], f["reserve"])


# ⚠ TROIS FIGURES DU VOLUME NE SE GRAVENT PAS ICI, ET C'EST DÉFINITIF.
# Le volume porte 118 figures ; ce programme en dessine 115. Les trois autres
# sont ANTÉRIEURES au programme : dessinées à la main, avant que `dessine.py`
# n'existe, et aucune des huit primitives ne les rend. Les réexprimer dans le
# langage du graveur produirait trois figures DIFFÉRENTES, pas les mêmes —
# ce serait perdre l'original, non l'automatiser.
#
# ☑ Ce qui manquait, et que ce registre ajoute le 21 août 2026 : les COMPTER et
# les VÉRIFIER. Elles pouvaient jusqu'ici disparaître du dossier ou changer d'un
# octet sans qu'aucun contrôle du dépôt le voie — le graveur ne les connaissait
# pas, et son bilan disait « 115 figures » sur un volume qui en porte 118.
# ⚠ Ce registre n'est PAS une chaîne de rendu : il gèle, il ne regrave pas.
# Retoucher l'une des trois oblige à reporter son empreinte ici, à la main.
#
# ⚠ L'EMPREINTE PORTE SUR LES OCTETS NORMALISÉS EN LF, depuis le 15 septembre 2026.
# Les trois valeurs gelées le 21 août (`e82d87c7412a…`, `7bc70d30bcee…`,
# `6b51f826a50b…`) étaient celles des fichiers en CRLF du disque d'auteur, avant
# que la règle `eol=lf` de `.gitattributes` ne normalise l'arbre : le contrôle
# sortait 1 sur tout clone conforme (évaluation du 15 septembre 2026, §8.1). Elles
# sont réancrées sur les octets LF de l'index — contenu inchangé depuis le
# 31 juillet 2026 —, et le hachage lit le fichier après CRLF → LF : le verdict ne
# dépend plus du réglage `core.autocrlf` de qui clone. Le défaut imprime
# l'empreinte vue en entier, pour qu'une retouche voulue se reporte sans calcul.
ANTERIEURES = {
    "f-01-00-invariant":      ("Livre I/01-interoperabilite-integration-entreprise.md",
                               "732d287e181f41dd64467803275b6ef36cbd8472205c62561e83714c06023d81"),
    "f-01-01-pile-canonique": ("Livre I/01-interoperabilite-integration-entreprise.md",
                               "e586b774d1d11d7ca9e59d7f60e333441c7851a5132dc91b6c9f8fb051a7e33a"),
    "f-08-01-n-fois-m":       ("Livre I/08-anatomie-mcp-a2a.md",
                               "22b4002dc3dad30ba33a78379486c424a5573646e0cc70d2bb66b74c33234287"),
}


def verifie_anterieures():
    """Rend la liste des défauts : figure absente, empreinte changée, appel perdu."""
    defauts = []
    for nom, (piece_rel, empreinte) in sorted(ANTERIEURES.items()):
        svg = FIGURES / f"{nom}.svg"
        if not svg.exists():
            defauts.append(f"{nom} : absente du dossier")
            continue
        vue = hashlib.sha256(svg.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
        if vue != empreinte:
            defauts.append(f"{nom} : empreinte {vue} au lieu de {empreinte[:12]}…")
        p = RACINE / piece_rel
        if not p.exists() or f"../figures/{nom}.svg" not in p.read_text(encoding="utf-8"):
            defauts.append(f"{nom} : plus appelée par {piece_rel}")
    return defauts


def appel(f):
    return (f'![**Figure {f["rang"]}** — {f["legende"]}]'
            f'(../figures/{f["nom"]}.svg)')


def insere(f, texte):
    """Pose l'appel devant l'ancre. Rend (texte, etat)."""
    motif_existant = re.compile(
        r"^!\[[^\]]*\]\(\.\./figures/" + re.escape(f["nom"]) + r"\.svg\)\n\n?",
        re.M)
    texte = motif_existant.sub("", texte)
    ancre = re.compile(f["ancre"], re.M)
    m = ancre.search(texte)
    if not m:
        return texte, "ANCRE INTROUVABLE"
    return texte[:m.start()] + appel(f) + "\n\n" + texte[m.start():], "posée"


def main():
    verif = "--verifier" in sys.argv
    rangs, noms, etats = {}, set(), []
    for f in C.FIGURES:
        if f["rang"] in rangs:
            sys.exit(f"[figures] rang {f['rang']} en double : {f['nom']} et {rangs[f['rang']]}")
        rangs[f["rang"]] = f["nom"]
        if f["nom"] in noms:
            sys.exit(f"[figures] nom {f['nom']} en double")
        noms.add(f["nom"])

    par_piece = {}
    for f in C.FIGURES:
        par_piece.setdefault(f["ch"], []).append(f)

    for ch, lot in sorted(par_piece.items()):
        chemin = piece(ch)
        texte = chemin.read_text(encoding="utf-8")
        for f in lot:
            if not verif:
                dessine_une(f)
            texte, etat = insere(f, texte)
            etats.append((f["nom"], etat))
        if not verif:
            chemin.write_text(texte, encoding="utf-8", newline="\n")

    manques = [n for n, e in etats if e != "posée"]
    anterieures = verifie_anterieures()
    total = len(C.FIGURES) + len(ANTERIEURES)
    print(f"[figures] {total} figures du volume : {len(C.FIGURES)} gravées sur "
          f"{len(par_piece)} pièces, {len(ANTERIEURES)} antérieures au programme "
          f"vérifiées à l'empreinte"
          + (" — VÉRIFICATION SEULE" if verif else ""))
    for n, e in etats:
        if e != "posée":
            print(f"   ⚠ {n} : {e}")
    for d in anterieures:
        print(f"   ⚠ {d}")
    if manques or anterieures:
        sys.exit(f"[figures] {len(manques)} ancre(s) introuvable(s), "
                 f"{len(anterieures)} défaut(s) aux figures antérieures")


if __name__ == "__main__":
    main()
