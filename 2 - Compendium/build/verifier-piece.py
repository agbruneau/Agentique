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

Ce script les distingue. Quatre contrôles, dans cet ordre de sévérité :

**[1] Parité stricte** — le rendu re-fabriqué depuis le `.md` courant est
identique, octet pour octet, au `.html` versionné. C'est le contrôle qui
compte : il ne suppose rien de la forme du rendu, il refait le travail.

**[2] Purge de l'appareil** — le rendu ne porte **ni l'en-tête à cinq champs, ni
la note de statut**, ni la thèse citée hors de sa tête. *La purge du 29 juillet 2026 est une
règle de fond : le rendu publie le corps, la gouvernance vit au `.md`.* Le
contrôle [1] la couvre déjà par construction ; celui-ci la rend **opposable au
rendeur lui-même**, dont une évolution pourrait la lever sans que personne ne
le voie.

**[4] Statut** — la tête rendue porte le statut de la pièce, « hors compte des
livrables » et « non publiable » compris (15 septembre 2026, décision D-18). *Un
lecteur du `.html` ne doit pas avoir à ouvrir le `.md` pour savoir ce que vaut la
pièce.*

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
sys.stdout.reconfigure(encoding="utf-8")  # console cp1252 : ⚠ et ☑ ne s'y encodent pas
sys.stderr.reconfigure(encoding="utf-8")

_spec = importlib.util.spec_from_file_location(
    "rendre_piece", Path(__file__).resolve().parent / "rendre-piece.py")
rendre_piece = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rendre_piece)

RACINE = rendre_piece.RACINE

# Les marques de l'appareil de gouvernance, telles qu'elles apparaîtraient dans un
# rendu qui les recopierait. ⚠ Depuis le 15 septembre 2026, la TÊTE rendue
# (`<header class="titre">`) porte la thèse citée et le statut de la pièce — voir
# `rendre-piece.py` : la thèse n'est donc refusée qu'au CORPS, après la tête ; le
# tableau d'en-tête et la note de statut le restent partout.
APPAREIL = (
    ("en-tête à cinq champs", re.compile(r"<th>Champ</th>\s*<th>Valeur</th>"), "partout"),
    ("thèse citée", re.compile(r"<strong>Thèse</strong>\s*<em>\(citée depuis"), "corps"),
    ("note de statut", re.compile(r"<h[1-6][^>]*>[^<]*Note de statut", re.I), "partout"),
)
TETE = re.compile(r'<header class="titre">(.*?)</header>', re.S)

# [4] — le statut rendu. Le volume est une archive de travail hors compte des
# livrables (D-18, 15 septembre 2026), et chaque pièce un brouillon non publiable :
# un lecteur du `.html` le lit en tête, sans ouvrir le `.md`.
STATUT_RENDU = re.compile(r'<p class="titre__statut">(.*?)</p>', re.S)
STATUT_EXIGE = ("hors compte des livrables", "non publiable")

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
        tete = TETE.search(sans_commentaire)
        hors_tete = TETE.sub(" ", sans_commentaire)
        for quoi, motif, ou in APPAREIL:
            if motif.search(sans_commentaire if ou == "partout" else hors_tete):
                echecs.append(f"[2] {nom} : le rendu porte « {quoi} »"
                              + (" hors de sa tête" if ou == "corps" else "") +
                              f". Le `.html` publie le corps technique ; l'appareil de "
                              f"gouvernance vit au `.md`, seule source.")

        # [4] — le statut en tête, lisible sans le `.md`.
        statut = STATUT_RENDU.search(tete.group(1)) if tete else None
        manque = [s for s in STATUT_EXIGE if not statut or s not in statut.group(1)]
        if manque:
            echecs.append(f"[4] {nom} : la tête rendue ne dit pas « {' », « '.join(manque)} » — "
                          f"le lecteur du `.html` ne voit pas que la pièce est un brouillon "
                          f"non publiable d'une archive hors compte des livrables (D-18).")

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
          f"(parité stricte, purge de l'appareil, statut en tête, figures).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
