#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parité `.md` / `.html` des cinquante pièces — contrôle de la règle permanente.

Le dépôt tient une règle : **une source ne se versionne pas sans son rendu.**
⚠ **Elle a été tenue en apparence et fausse en fait du 31 juillet au 2 septembre
2026** : les cinquante `.html` dataient de la génération du 31 juillet, les
révisions du français des 31 juillet au 3 août n'y étaient pas, **114 des 115
figures en étaient absentes**, et deux commits ultérieurs les avaient touchés —
par substitution globale du titre, non par régénération. *Un fichier modifié au
même commit que sa source n'est pas un fichier régénéré, et rien ne les
distinguait.*

Ce script les distingue. Trois contrôles, dans cet ordre de sévérité :

**[1] Parité stricte** — le rendu re-fabriqué depuis le `.md` courant est
identique, octet pour octet, au `.html` versionné. C'est le contrôle qui
compte : il ne suppose rien de la forme du rendu, il refait le travail.

**[2] Purge de l'appareil** — le rendu ne porte **ni l'en-tête à cinq champs, ni
la thèse citée, ni la note de statut**. *La purge du 29 juillet 2026 est une
règle de fond : le rendu publie le corps, la gouvernance vit au `.md`.* Le
contrôle [1] la couvre déjà par construction ; celui-ci la rend **opposable au
rendeur lui-même**, dont une évolution pourrait la lever sans que personne ne
le voie.

**[3] Figures** — chaque image du `.md` est dans le rendu, à la même source.
Redondant avec [1], et c'est voulu : *c'est la classe de défaut qui a tenu cinq
semaines, et un contrôle qui ne la nomme pas ne la rapporte pas.*

Sortie 0 si les cinquante pièces tiennent, 1 sinon.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import importlib.util

_spec = importlib.util.spec_from_file_location(
    "rendre_piece", Path(__file__).resolve().parent / "rendre-piece.py")
rendre_piece = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rendre_piece)

RACINE = rendre_piece.RACINE

# Les trois marques de l'appareil de gouvernance, telles qu'elles apparaîtraient
# dans un rendu qui les recopierait.
APPAREIL = (
    ("en-tête à cinq champs", re.compile(r"<th>Champ</th>\s*<th>Valeur</th>")),
    ("thèse citée", re.compile(r"<strong>Thèse</strong>\s*<em>\(citée depuis")),
    ("note de statut", re.compile(r"<h[1-6][^>]*>[^<]*Note de statut", re.I)),
)

# ⚠ Les commentaires HTML sont retirés avant [2], et le motif est un piège
# vécu : le gabarit porte lui-même, en commentaire, la phrase « NI EN-TÊTE À
# CINQ CHAMPS, NI THÈSE, NI NOTE DE STATUT ». *Un contrôle qui lit la règle
# écrite dans le fichier comme une infraction au fichier échoue sur les
# cinquante pièces le jour de sa mise en service.*
COMMENTAIRE = re.compile(r"<!--.*?-->", re.S)

IMAGE_MD = re.compile(r"!\[[^\]]*\]\((\.\./figures/[^)]+)\)")
IMAGE_HTML = re.compile(r'<img src="([^"]+)"')


def controler():
    echecs = []
    pieces = rendre_piece.pieces()
    for md in pieces:
        nom = md.relative_to(RACINE).as_posix()
        cible = md.with_suffix(".html")
        if not cible.exists():
            echecs.append(f"[1] {nom} : aucun rendu `.html` — la règle permanente "
                          f"du dépôt veut la source et son rendu au même commit.")
            continue
        versionne = cible.read_text(encoding="utf-8")

        # [1] — on refait le rendu et on compare. Le fichier n'est pas réécrit.
        refait = rendre_piece.composer(md)
        if refait != versionne:
            a, b = refait.splitlines(), versionne.splitlines()
            ligne = next((i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y),
                         min(len(a), len(b)) + 1)
            echecs.append(
                f"[1] {nom} : le rendu versionné n'est pas celui que le `.md` "
                f"courant produit — première divergence ligne {ligne} "
                f"({len(b)} lignes versionnées, {len(a)} refabriquées). "
                f"`python build/rendre-piece.py` le régénère.")

        # [2] — la purge du 29 juillet 2026.
        sans_commentaire = COMMENTAIRE.sub(" ", versionne)
        for quoi, motif in APPAREIL:
            if motif.search(sans_commentaire):
                echecs.append(f"[2] {nom} : le rendu porte « {quoi} ». Le `.html` "
                              f"publie le corps technique ; l'appareil de "
                              f"gouvernance vit au `.md`, seule source.")

        # [3] — les figures, nommément.
        attendues = IMAGE_MD.findall(md.read_text(encoding="utf-8"))
        rendues = [s for s in IMAGE_HTML.findall(versionne) if s.startswith("../figures/")]
        if attendues != rendues:
            manquantes = [s for s in attendues if s not in rendues]
            echecs.append(
                f"[3] {nom} : {len(attendues)} figure(s) au `.md`, {len(rendues)} "
                f"au rendu" + (f" — absente(s) : {', '.join(manquantes[:3])}"
                               if manquantes else " — l'ordre diffère") + ".")
    return echecs, len(pieces)


def main():
    echecs, n = controler()
    if echecs:
        print(f"ÉCHEC — {len(echecs)} écart(s) sur {n} pièces :")
        for e in echecs:
            print(f"  {e}")
        return 1
    print(f"OK — les {n} rendus `.html` sont ceux que les `.md` produisent "
          f"(parité stricte, purge de l'appareil, figures).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
