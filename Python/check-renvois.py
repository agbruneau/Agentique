#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Résout les renvois relatifs des `.md` du dépôt, et sort 1 s'il en reste un mort.

    python Python/check-renvois.py          # depuis la racine du dépôt

Règle — celle du rejeu de l'évaluation du 15 septembre 2026 (§3.2), rendue opposable :

  - SOURCES : les `.md` que git suit ou suivrait (`git ls-files --cached --others
    --exclude-standard`), présents sur le disque. Un fichier ignoré n'en est pas.
  - RENVOIS : liens et images en ligne `[x](cible)`, `[x](<cible avec espaces>)`,
    et définitions de référence `[x]: cible`. Les notes `[^n]:` n'en sont pas.
  - EXCLUS : blocs de code clôturés (``` ou ~~~), spans de code, cibles à schéma
    (`https:`, `mailto:`…) — ce contrôle ne sort pas sur le réseau.
  - CIBLE : décodée (`%20`, `%C3%89`), requête ôtée, résolue depuis le dossier de la
    source (`/…` depuis la racine) ; elle doit être un fichier ou un dossier de la
    même liste, À LA CASSE PRÈS. Le disque ne fait pas foi : Windows confond
    `readme.md` et `README.md`, le clone Linux et GitHub non ; un fichier ignoré
    existe chez l'auteur et nulle part ailleurs.
  - FRAGMENT : `#L12` ou `#L12-L20` vise une ligne qui existe ; tout autre fragment
    vers un `.md` (ou la source elle-même) doit nommer un titre, selon le slug de
    GitHub, ou une ancre `<a id|name>` / `{#id}` de la cible. Fragments vers un
    autre type de fichier : non vérifiés.

⚠ Un chemin cité dans une phrase datée est une donnée : ce contrôle ne regarde que
les CIBLES DE LIEN, jamais la prose. Un renvoi mort se répare en pointant ce qui
existe, en gardant l'ancien nom dans le texte s'il date un fait.

Harnais : `python Python/check-renvois-mutations.py`.
"""
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

sys.stdout.reconfigure(encoding="utf-8")  # console cp1252 : ⚠ et ☑ ne s'y encodent pas
sys.stderr.reconfigure(encoding="utf-8")

RACINE = Path(os.environ.get("RENVOIS_RACINE", Path(__file__).resolve().parent.parent))

CLOTURE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
SPAN = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)", re.S)
DEFINITION = re.compile(r"^ {0,3}\[(?!\^)[^\]]+\]:[ \t]*(<[^>\n]*>|\S+)", re.M)
SCHEMA = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:|^//")
TITRE = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*?)[ \t#]*$")
ANCRE_HTML = re.compile(r"""<a\s[^>]*?\b(?:id|name)\s*=\s*["']([^"']+)["']""", re.I)
ANCRE_PANDOC = re.compile(r"\{#([^\s}]+)[^}]*\}")
LIGNE = re.compile(r"^L(\d+)(?:-L(\d+))?$")
SOULIGNE = re.compile(r"^ {0,3}(=+|-+)[ \t]*$")   # titre setext : la ligne d'avant est le titre

# Renvois morts TOLÉRÉS, chacun avec son motif. Une exemption qui ne correspond plus à
# aucun renvoi mort fait échouer le contrôle : la liste ne peut que rétrécir.
EXEMPTIONS = {
    ("1 - Collection/3 - EntrepriseAgentique/verification/lot-L-03-agent-card.md",
     "#447-agentcardsignature"):
        "citation verbatim de la spécification A2A v1.0.0 : l'ancre vise le document cité, "
        "et la corriger falsifierait la citation",
}


def fichiers():
    r = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "-z", "--cached",
                        "--others", "--exclude-standard"], cwd=RACINE, capture_output=True)
    if r.returncode != 0:
        sys.exit(f"[renvois] git ls-files a échoué dans {RACINE} : {r.stderr.decode(errors='replace')}")
    return sorted({p for p in r.stdout.decode("utf-8").split("\0") if p and (RACINE / p).is_file()})


def masque_code(texte):
    """Rend le texte avec les blocs clôturés et les spans de code blanchis, lignes conservées."""
    lignes, dedans = texte.split("\n"), None
    for i, l in enumerate(lignes):
        m = CLOTURE.match(l)
        if dedans is None:
            if m and not (m.group(1)[0] == "`" and "`" in m.group(2)):
                dedans = m.group(1)
                lignes[i] = ""
        else:
            if m and m.group(1)[0] == dedans[0] and len(m.group(1)) >= len(dedans) and not m.group(2).strip():
                dedans = None
            lignes[i] = ""
    # Les spans ne franchissent pas une ligne blanche : on les cherche paragraphe par paragraphe.
    paragraphes = re.split(r"(\n[ \t]*\n)", "\n".join(lignes))
    blanchir = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    return "".join(SPAN.sub(blanchir, p) for p in paragraphes)


def cibles_en_ligne(texte):
    """Rend (position, cible) pour chaque `](cible)`, parenthèses équilibrées."""
    for m in re.finditer(r"\]\(", texte):
        i = m.end()
        while i < len(texte) and texte[i] in " \t":
            i += 1
        if texte.startswith("<", i):
            fin = texte.find(">", i)
            if fin != -1 and "\n" not in texte[i:fin]:
                yield m.start(), texte[i + 1:fin]
            continue
        j, prof = i, 0
        while j < len(texte) and not texte[j].isspace():
            if texte[j] == "(":
                prof += 1
            elif texte[j] == ")":
                if prof == 0:
                    break
                prof -= 1
            j += 1
        if j > i:
            yield m.start(), texte[i:j]


def slug(titre):
    """Slug de titre à la manière de GitHub : texte rendu, minuscules, ponctuation ôtée."""
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", titre)   # liens et images -> leur texte
    t = re.sub(r"<[^>]+>", "", t).replace("`", "").replace("*", "")
    t = ANCRE_PANDOC.sub("", t).strip().lower()
    t = "".join(c for c in t if c in " -_" or unicodedata.category(c)[0] in "LNM")
    return t.replace(" ", "-")


_ancres = {}


def ancres(rel):
    """Rend (ensemble des ancres, nombre de lignes) d'un .md, avec les suffixes -1, -2 des doublons."""
    if rel not in _ancres:
        texte = (RACINE / rel).read_bytes().decode("utf-8", errors="replace").replace("\r\n", "\n")
        vues, noms, avant = {}, set(), ""
        for l in masque_code(texte).split("\n"):
            m = TITRE.match(l)
            setext = SOULIGNE.match(l) and avant.strip() and not avant.lstrip().startswith(("|", "-", "*", ">"))
            titre = m.group(2) if m else avant if setext else None
            avant = l
            if titre is not None:
                s = slug(titre)
                n = vues.get(s, 0)
                noms.add(s if n == 0 else f"{s}-{n}")
                vues[s] = n + 1
        noms.update(a.lower() for a in ANCRE_HTML.findall(texte))
        noms.update(a.lower() for a in ANCRE_PANDOC.findall(texte))
        _ancres[rel] = (noms, texte.count("\n") + 1)
    return _ancres[rel]


def verifier(source, brute, suivis, dossiers):
    """Rend None si le renvoi tient, sinon la raison."""
    cible = brute.strip()
    if not cible or SCHEMA.match(cible):
        return None
    chemin, _, fragment = cible.partition("#")
    chemin = unquote(chemin.split("?", 1)[0])
    if chemin:
        base = PurePosixPath() if chemin.startswith("/") else PurePosixPath(source).parent
        rel = os.path.normpath(str(base / chemin.lstrip("/"))).replace("\\", "/")
        if rel == "." or rel in dossiers:
            return None
        if rel.startswith("../") or rel not in suivis:
            return f"introuvable (résolue : {rel})"
    else:
        rel = source
    fragment = unquote(fragment)
    m = LIGNE.match(fragment)
    if not fragment or not (m or rel.endswith(".md")):
        return None
    noms, n_lignes = ancres(rel)
    if m:
        return None if max(int(g) for g in m.groups() if g) <= n_lignes else \
            f"ligne {m.group(0)} au-delà de la fin ({n_lignes} lignes dans {rel})"
    return None if fragment.lower() in noms else f"aucun titre ni ancre « {fragment} » dans {rel}"


def main():
    suivis = set(fichiers())
    dossiers = {str(p) for f in suivis for p in PurePosixPath(f).parents if str(p) != "."}
    sources = sorted(f for f in suivis if f.endswith(".md"))
    total, fragments, morts = 0, 0, []
    for source in sources:
        texte = (RACINE / source).read_bytes().decode("utf-8", errors="replace").replace("\r\n", "\n")
        vu = masque_code(texte)
        trouves = list(cibles_en_ligne(vu)) + [(m.start(1), m.group(1)) for m in DEFINITION.finditer(vu)]
        for pos, cible in trouves:
            cible = cible.strip().strip("<>")
            # le masque ne blanchit que le code : hors code, texte masqué et original coïncident
            if not cible or SCHEMA.match(cible.strip()):
                continue
            total += 1
            fragments += "#" in cible
            raison = verifier(source, cible, suivis, dossiers)
            if raison:
                morts.append((source, vu.count("\n", 0, pos) + 1, cible, raison))
    tolere = [m for m in morts if (m[0], m[2]) in EXEMPTIONS]
    morts = [m for m in morts if (m[0], m[2]) not in EXEMPTIONS]
    perimees = set(EXEMPTIONS) - {(m[0], m[2]) for m in tolere}
    for source, ligne, cible, raison in morts:
        print(f"{source}:{ligne}: renvoi mort -> {cible} — {raison}")
    for source, ligne, cible, _ in tolere:
        print(f"{source}:{ligne}: toléré -> {cible} — {EXEMPTIONS[(source, cible)]}")
    for source, cible in sorted(perimees):
        print(f"{source}: exemption périmée -> {cible} — le renvoi n'est plus mort, ou n'existe plus ; "
              f"retirer l'entrée d'EXEMPTIONS")
    print(f"[renvois] {len(sources)} .md, {total} renvois relatifs (dont {fragments} à fragment), "
          f"{len(morts)} mort(s), {len(tolere)} toléré(s), {len(perimees)} exemption(s) périmée(s)")
    return 1 if morts or perimees else 0


if __name__ == "__main__":
    sys.exit(main())
