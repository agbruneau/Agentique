#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mesure la lisibilité des pages d'accueil — les `README.md` du dépôt — et sort 1 hors seuil.

    python Python/check-lisibilite.py          # depuis n'importe quel dossier

Une page d'accueil dit en une page ce que le dossier porte, dans quel état, par où entrer,
comment refaire, et où est le journal ; la chronique datée vit dans les `JOURNAL.md`
(tâches T4.1, T4.2 et T4.4 du plan d'exécution). Ce contrôle rend la règle opposable.

Règle, et seuils — chacun est une constante ci-dessous :

  - SOURCES : les `README.md` que git suit ou suivrait (`git ls-files --cached --others
    --exclude-standard`), présents sur le disque ; aucun ne peut manquer à l'appel.
  - LONGUEUR : `wc -l` au plus LIGNES_MAX.
  - MARQUEURS : aucun des signes d'alerte ou de chronique de MARQUEURS dans le texte de la
    page, tables comprises — le plan exemptait les tables de contrôle, ce contrôle non.
  - GRAS (`**…**` ou `__…__`) : la part des signes en gras dans le texte, espaces exclus,
    marqueurs `**` exclus, sous DENSITE_GRAS_MAX,
    et aucun gras hors titre courant — un titre courant est un gras qui ouvre sa ligne,
    son élément de liste, sa citation ou sa cellule de table, et finit par « : ».
  - JOURNAL : la page renvoie, par un lien qui résout, à un `JOURNAL.md` existant.
  - EXCLUS du texte mesuré : blocs de code clôturés et spans de code — une commande n'est
    pas de la prose, et un `**` dans une ligne de shell n'est pas du gras.

Harnais : `python Python/check-lisibilite-mutations.py`.
"""
import os
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

sys.stdout.reconfigure(encoding="utf-8")  # console cp1252 : les marqueurs ne s'y encodent pas
sys.stderr.reconfigure(encoding="utf-8")

RACINE = Path(os.environ.get("LISIBILITE_RACINE", Path(__file__).resolve().parent.parent))

LIGNES_MAX = 40
DENSITE_GRAS_MAX = 0.05          # strictement sous 5 %
GRAS_HORS_TITRE_MAX = 0
MARQUEURS = "⚠☑☐✎"
MARQUEURS_MAX = 0

CLOTURE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
SPAN = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)", re.S)
GRAS = re.compile(r"\*\*(?=\S)(?P<a>.+?)(?<=\S)\*\*|(?<!\w)__(?=\S)(?P<b>.+?)(?<=\S)__(?!\w)")
OUVRE = re.compile(r"(^|\|)\s*(>\s*)*([-*+]\s+|\d+[.)]\s+)?$")
LIEN = re.compile(r"\]\(\s*(<[^>\n]+>|[^)\s]+)")


def readmes():
    r = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "-z", "--cached", "--others",
                        "--exclude-standard"], cwd=RACINE, capture_output=True)
    if r.returncode != 0:
        sys.exit(f"[lisibilité] git ls-files a échoué dans {RACINE} : {r.stderr.decode(errors='replace')}")
    return sorted(p for p in r.stdout.decode("utf-8").split("\0")
                  if PurePosixPath(p).name == "README.md" and (RACINE / p).is_file())


def masque(texte):
    """Blanchit blocs clôturés et spans de code, longueur et lignes conservées."""
    lignes, dedans = texte.split("\n"), None
    for i, l in enumerate(lignes):
        m = CLOTURE.match(l)
        if dedans is None:
            if m and not (m.group(1)[0] == "`" and "`" in m.group(2)):
                dedans, lignes[i] = m.group(1), " " * len(l)
        else:
            if m and m.group(1)[0] == dedans[0] and len(m.group(1)) >= len(dedans) and not m.group(2).strip():
                dedans = None
            lignes[i] = " " * len(l)
    paragraphes = re.split(r"(\n[ \t]*\n)", "\n".join(lignes))
    return "".join(SPAN.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), p) for p in paragraphes)


def mesurer(rel):
    """Rend (lignes, densité, gras hors titre courant [(n°, extrait)], marqueurs [(n°, signe)], journal)."""
    brut = (RACINE / rel).read_bytes().decode("utf-8", errors="replace").replace("\r\n", "\n")
    lignes = brut.count("\n") + (0 if brut.endswith("\n") or not brut else 1)
    vu = masque(brut)
    marqueurs = [(i, c) for i, l in enumerate(vu.split("\n"), 1) for c in l if c in MARQUEURS]
    signes = sum(1 for c in vu if not c.isspace())
    gras, hors = 0, []
    for i, l in enumerate(vu.split("\n"), 1):
        for m in GRAS.finditer(l):
            interieur = m.group("a") or m.group("b")
            gras += sum(1 for c in interieur if not c.isspace())
            if not (OUVRE.search(l[:m.start()]) and interieur.rstrip().endswith(":")):
                hors.append((i, m.group(0)[:60]))
    journal = False
    dossier = PurePosixPath(rel).parent
    for m in LIEN.finditer(vu):
        cible = unquote(m.group(1).strip("<>").split("#")[0].split("?")[0])
        if PurePosixPath(cible).name == "JOURNAL.md" and not re.match(r"^[A-Za-z][\w+.-]*:", cible):
            chemin = os.path.normpath(RACINE / dossier / cible)
            journal |= os.path.isfile(chemin)
    return lignes, (gras / signes if signes else 0.0), hors, marqueurs, journal


def main():
    pages = readmes()
    if not pages:
        print(f"ÉCHEC — aucun README.md sous {RACINE}")
        return 1
    fautes = []
    print(f"Lisibilité des pages d'accueil — {len(pages)} README.md ; seuils : ≤ {LIGNES_MAX} lignes, "
          f"gras < {DENSITE_GRAS_MAX:.0%} et hors titre courant ≤ {GRAS_HORS_TITRE_MAX}, "
          f"marqueurs {' '.join(MARQUEURS)} ≤ {MARQUEURS_MAX}, lien vers un JOURNAL.md")
    print(f"  {'lignes':>6} {'gras':>6} {'hors':>4} {'marq.':>5} {'journal':>7}  page")
    for rel in pages:
        n, d, hors, marq, journal = mesurer(rel)
        print(f"  {n:>6} {d:>6.1%} {len(hors):>4} {len(marq):>5} {'oui' if journal else 'NON':>7}  {rel}")
        if n > LIGNES_MAX:
            fautes.append(f"{rel} : {n} lignes, plus de {LIGNES_MAX}")
        if d >= DENSITE_GRAS_MAX:
            fautes.append(f"{rel} : gras {d:.1%}, seuil {DENSITE_GRAS_MAX:.0%}")
        if len(hors) > GRAS_HORS_TITRE_MAX:
            fautes += [f"{rel}:{i} : gras hors titre courant — {x}" for i, x in hors]
        if len(marq) > MARQUEURS_MAX:
            fautes += [f"{rel}:{i} : marqueur {c}" for i, c in marq]
        if not journal:
            fautes.append(f"{rel} : aucun lien qui résout vers un JOURNAL.md")
    if fautes:
        print(f"\nÉCHEC — {len(fautes)} écart(s) :")
        for f in fautes:
            print(f"  {f}")
        return 1
    print(f"\nOK — les {len(pages)} pages d'accueil tiennent les seuils.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
