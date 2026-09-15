#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harnais de mutation de `check-renvois.py`.

Doctrine du dépôt : un script de contrôle se vérifie comme le reste, en deux temps.

  1. Le contrôle PASSE sur un corpus propre — ici un mini-corpus écrit par le harnais,
     où chaque forme valide que la règle admet est présente une fois (cible encodée,
     entre chevrons, parenthèses imbriquées, titre accentué, titre en double, titre
     souligné, ancre HTML, ancre de ligne, dossier, chemin depuis la racine, définition de
     référence) : un contrôle qui rejetterait l'une
     d'elles échoue ici, avant toute mutation.
  2. Sur une COPIE du corpus réel, chaque classe de faute est injectée seule, puis
     retirée ; le contrôle doit la nommer, à sa ligne, et sortir 1. Les formes que la
     règle exclut (code, URL) sont injectées aussi, et ne doivent RIEN ajouter.

Le temps 2 se lit contre le verdict du corpus intact, non contre zéro : une passe
voisine non commitée peut laisser un renvoi mort sans rendre le harnais muet.

Le corpus réel n'est jamais muté : `check-renvois.py` lit la copie par `RENVOIS_RACINE`.

Usage :  python Python/check-renvois-mutations.py      (depuis la racine du dépôt)
Sortie 0 si le temps 1 passe et si chaque mutation a le verdict attendu.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # console cp1252 : ⚠ et ☑ ne s'y encodent pas
sys.stderr.reconfigure(encoding="utf-8")

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "check-renvois.py"
DEPOT = ICI.parent
MORT = re.compile(r"^(.+?):(\d+): renvoi mort -> (.+?) — ", re.M)
RESOLUE = re.compile(r"renvoi mort -> .+? — introuvable \(résolue : (.+?)\)$", re.M)


def controle(racine):
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, encoding="utf-8",
                       env={**os.environ, "RENVOIS_RACINE": str(racine), "PYTHONUTF8": "1"})
    return r.returncode, set(MORT.findall(r.stdout)), r.stdout


def git_init(racine):
    subprocess.run(["git", "init", "-q", str(racine)], check=True)


def ecrire(p, texte):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------- temps 1 : corpus propre

EXEMPTE = "1 - Collection/3 - EntrepriseAgentique/verification/lot-L-03-agent-card.md"

PROPRE = {
    "README.md": "\n".join([
        "# Mini-corpus",
        "## § 2.1 — Réponse à Q3, en une phrase",
        "## Doublon",
        "## Doublon",
        "[relatif](docs/guide.md) [encodé](docs/Mon%20fichier%20%C3%A9t%C3%A9.md)",
        "[chevrons](<docs/Mon fichier été.md>) [parenthèses](docs/f(1).md)",
        "[titre accentué](#-21--réponse-à-q3-en-une-phrase) [doublon](#doublon-1)",
        "[ancre de ligne](docs/guide.md#L2) [dossier](docs/) [racine](/docs/guide.md)",
        "![image](docs/f(1).md) [réf][r] [url](https://exemple.invalid/x.md)",
        "[r]: docs/guide.md#un-titre",
        "```",
        "[dans un bloc](absent.md)",
        "```",
        "Un span : `[dans un span](absent.md)`.",
        "",
    ]),
    "docs/guide.md": "# Un titre\nligne 2\n[retour](../README.md#doublon) [setext](#titre-souligné)\n\n"
                     "Titre souligné\n==============\n",
    "docs/Mon fichier été.md": "# x\n",
    "docs/f(1).md": "# x\n<a id=\"ancre-html\"></a>\n[soi](#ancre-html)\n",
    # le renvoi que check-renvois.py tolère : sans lui, son exemption serait périmée
    EXEMPTE:
        "# Lot\n> The [`AgentCardSignature`](#447-agentcardsignature) object\n",
}


def temps_1(base):
    racine = base / "propre"
    git_init(racine)
    for rel, texte in PROPRE.items():
        ecrire(racine / rel, texte)
    code, morts, sortie = controle(racine)
    ok = code == 0 and not morts
    print(f"  temps 1 — corpus propre ({len(PROPRE)} fichiers, formes valides et exclues) : "
          f"{'PASSE' if ok else 'ÉCHEC'} (sortie {code})")
    if not ok:
        print(sortie)
        return False
    # Sur ce corpus qui sort 0, réparer le renvoi toléré doit suffire à faire sortir 1.
    ecrire(racine / EXEMPTE, PROPRE[EXEMPTE].replace("(#447-agentcardsignature)", "(#lot)"))
    code, morts, sortie = controle(racine)
    bon = code == 1 and not morts and "1 exemption(s) périmée(s)" in sortie
    print(f"    {'☑' if bon else '⚠'} M0  exemption périmée (renvoi toléré réparé) — "
          f"{'DÉTECTÉE' if bon else f'NON DÉTECTÉE (sortie {code})'}")
    return bon


# ---------------------------------------------------------------- temps 2 : corpus réel

def copie_du_depot(base):
    """Copie les .md et les .gitignore réels ; les autres fichiers suivis, en fichiers vides."""
    r = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "-z", "--cached", "--others",
                        "--exclude-standard"], cwd=DEPOT, capture_output=True, check=True)
    racine = base / "reel"
    git_init(racine)
    for rel in filter(None, r.stdout.decode("utf-8").split("\0")):
        src = DEPOT / rel
        if not src.is_file():
            continue
        dst = racine / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if rel.endswith(".md") or Path(rel).name in (".gitignore", ".gitattributes"):
            shutil.copyfile(src, dst)
        else:
            dst.touch()
    return racine


def temps_2(base):
    racine = copie_du_depot(base)
    code0, morts0, sortie0 = controle(racine)
    print(f"  temps 2 — corpus réel copié : verdict intact {code0}, {len(morts0)} renvoi(s) mort(s) "
          f"de référence")

    # Une source réelle, et un voisin réel de son dossier, pour que les cibles cassées
    # diffèrent d'une cible vraie d'un octet ou d'une casse.
    source = next(p for p in ("2 - Compendium/README.md", "3 - Veille/README.md", "README.md")
                  if (racine / p).is_file())
    dossier = (racine / source).parent
    voisin = next(p.name for p in sorted(dossier.iterdir())
                  if p.is_file() and p.suffix == ".md" and p.name != "README.md")
    encode = voisin.replace(" ", "%20")
    fin = len((racine / source).read_text(encoding="utf-8").split("\n"))
    ignore = "__pycache__/mutation-ignoree.md"

    # (nom, lignes ajoutées à la fin de la source, cible attendue morte ou None, rang de la ligne fautive)
    mutations = [
        ("M1  cible absente", ["[m](absent-mutation.md)"], "absent-mutation.md", 1),
        ("M2  cible réelle amputée d'un octet", [f"[m](<{voisin[:-4]}.m>)"], f"{voisin[:-4]}.m", 1),
        ("M3  cible réelle à la mauvaise casse", [f"[m](<{voisin.upper()}>)"], voisin.upper(), 1),
        ("M4  cible encodée cassée", [f"[m]({encode[:-3]}%C3%A9.md)"], f"{encode[:-3]}%C3%A9.md", 1),
        ("M5  titre absent", ["[m](#titre-qui-n-existe-pas)"], "#titre-qui-n-existe-pas", 1),
        ("M6  ancre de ligne au-delà de la fin", [f"[m](<{voisin}#L999999>)"], f"{voisin}#L999999", 1),
        ("M7  définition de référence morte", ["", "[ref-mutation]: absent-ref.md"], "absent-ref.md", 2),
        ("M8  image morte", ["![m](figures/absente-mutation.svg)"], "figures/absente-mutation.svg", 1),
        ("M9  cible ignorée par git, présente sur disque", [f"[m]({ignore})"], ignore, 1),
        ("M10 renvoi mort dans un bloc clôturé", ["", "```", "[m](absent-bloc.md)", "```"], None, 0),
        ("M11 renvoi mort dans un span de code", ["Voir `[m](absent-span.md)`."], None, 0),
        ("M12 URL morte (hors périmètre)", ["[m](https://exemple.invalid/absent.md)"], None, 0),
        ("M13 cible réelle encodée, valide", [f"[m]({encode})"], None, 0),
    ]

    ok = True
    original = (racine / source).read_bytes()
    (dossier / ignore).parent.mkdir(exist_ok=True)
    (dossier / ignore).write_text("# ignorée\n", encoding="utf-8", newline="\n")
    for nom, ajout, attendue, rang in mutations:
        (racine / source).write_bytes(original + ("\n" + "\n".join(ajout) + "\n").encode("utf-8"))
        code, morts, sortie = controle(racine)
        (racine / source).write_bytes(original)
        nouveaux = morts - morts0
        if attendue is None:
            bon = nouveaux == set() and code == code0
            verdict = "ignorée (attendu)" if bon else f"FAUX POSITIF : {sorted(nouveaux)}"
        else:
            vise = (source, str(fin + rang), attendue)
            bon = code == 1 and nouveaux == {vise}
            verdict = "DÉTECTÉE à sa ligne" if bon else f"NON DÉTECTÉE (sortie {code}, vus {sorted(nouveaux)})"
        ok &= bon
        print(f"    {'☑' if bon else '⚠'} {nom} — {verdict}")

    # M14 : un fichier que des renvois réels visent disparaît ; chacun doit tomber, et eux seuls.
    visee = cible_la_plus_visee(racine)
    sauve = (racine / visee).read_bytes()
    (racine / visee).unlink()
    code, morts, sortie = controle(racine)
    (racine / visee).write_bytes(sauve)
    nouveaux = morts - morts0
    resolues = set(RESOLUE.findall(sortie)) - set(RESOLUE.findall(sortie0))
    bon = code == 1 and bool(nouveaux) and resolues == {visee}
    ok &= bon
    print(f"    {'☑' if bon else '⚠'} M14 fichier cible retiré ({visee}) — "
          f"{len(nouveaux)} renvoi(s) réel(s) tombé(s)" + ("" if bon else f" : ÉCHEC, résolues {resolues}"))

    # M15 : l'exemption vise-t-elle encore un renvoi mort du corpus réel ? Sinon le temps 1
    # l'éprouve en vain, et check-renvois.py sort déjà 1 sur « exemption périmée ».
    exempte = racine / EXEMPTE
    bon = exempte.is_file() and b"(#447-agentcardsignature)" in exempte.read_bytes() \
        and any(s == EXEMPTE and c == "#447-agentcardsignature" for s, _, c in
                set(re.findall(r"^(.+?):(\d+): toléré -> (.+?) — ", sortie0, re.M)))
    ok &= bon
    print(f"    {'☑' if bon else '⚠'} M15 exemption en vigueur sur le corpus réel — "
          f"{'tolérée à sa ligne' if bon else 'NE VISE PLUS RIEN : la retirer de check-renvois.py'}")
    return ok


def cible_la_plus_visee(racine):
    """Rend le .md réel que le plus de renvois relatifs valides désignent (hors README)."""
    os.environ["RENVOIS_RACINE"] = str(racine)
    import importlib.util
    spec = importlib.util.spec_from_file_location("check_renvois", SCRIPT)
    cr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cr)
    suivis = set(cr.fichiers())
    compte = {}
    for s in (f for f in suivis if f.endswith(".md")):
        vu = cr.masque_code((racine / s).read_text(encoding="utf-8"))
        for _, c in cr.cibles_en_ligne(vu):
            chemin = cr.unquote(c.split("#")[0].split("?")[0])
            if not chemin or cr.SCHEMA.match(chemin) or chemin.startswith("/"):
                continue
            rel = os.path.normpath(os.path.join(os.path.dirname(s), chemin)).replace("\\", "/")
            if rel in suivis and rel.endswith(".md") and not rel.endswith("README.md"):
                compte[rel] = compte.get(rel, 0) + 1
    return max(sorted(compte), key=compte.get)


def main():
    print("Harnais de check-renvois.py")
    with tempfile.TemporaryDirectory(prefix="renvois-") as tmp:
        base = Path(tmp)
        ok = temps_1(base) and temps_2(base)
    print("Toutes les mutations ont le verdict attendu." if ok else "⚠ HARNAIS EN ÉCHEC.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
