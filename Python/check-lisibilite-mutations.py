#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harnais de mutation de `check-lisibilite.py`.

Doctrine du dépôt : un contrôle se vérifie comme le reste, en deux temps.

  1. Le contrôle PASSE sur un corpus propre écrit ici, où chaque forme que la règle admet
     est présente une fois : une page de 40 lignes pile, en fins de ligne CRLF ; des titres
     courants en tête de ligne, d'élément de liste, de citation et de cellule de table ; du
     gras et un marqueur dans un span de code ; du gras dans un bloc clôturé ; un lien vers le
     journal d'un dossier parent, entre chevrons avec fragment, puis encodé. Un contrôle qui
     rejetterait l'une d'elles échoue ici, avant toute mutation.
  2. Sur une COPIE des pages et des journaux réels, chaque faute est injectée seule dans une
     page réelle ; le contrôle doit nommer cette page, et elle seule, avec la faute attendue,
     et sortir 1. Les formes légitimes injectées ne doivent rien ajouter.

Le corpus réel n'est jamais muté : `check-lisibilite.py` lit la copie par `LISIBILITE_RACINE`.

Usage :  python Python/check-lisibilite-mutations.py
Sortie 0 si le temps 1 passe et si chaque mutation a le verdict attendu.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # console cp1252 : les marqueurs ne s'y encodent pas
sys.stderr.reconfigure(encoding="utf-8")

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "check-lisibilite.py"
DEPOT = ICI.parent
CIBLE = "3 - Veille/README.md"          # la page réelle que les mutations frappent


def controle(racine):
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, encoding="utf-8",
                       env={**os.environ, "LISIBILITE_RACINE": str(racine), "PYTHONUTF8": "1"})
    fautes = re.findall(r"^  (.+?)(?::\d+)? : (.+)$", r.stdout.split("ÉCHEC —")[-1], re.M) if r.returncode else []
    return r.returncode, fautes, r.stdout


def ecrire(p, texte, fin="\n"):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(texte.replace("\n", fin).encode("utf-8"))


# ---------------------------------------------------------------- temps 1 : corpus propre

def page_propre():
    lignes = [
        "# Une page propre",
        "",
        "**Statut :** une ligne qui ouvre sur un titre courant.",
        "",
        "- **Réserve :** un titre courant d'élément de liste.",
        "1. **Étape :** un titre courant de liste numérotée.",
        "",
        "> **Note :** un titre courant de citation.",
        "",
        "| Champ | Valeur |",
        "|---|---|",
        "| **Rendu :** | 7 p. |",
        "",
        "Un span de code n'est pas de la prose : `**gras**` et `⚠` n'y comptent pas.",
        "",
        "```bash",
        "echo **pas du gras** dans un bloc clôturé",
        "```",
        "",
        "**Journal :** [le journal](<../JOURNAL.md#une-section>) et [le même, encodé](../JOURNAL%2Emd).",
    ]
    lignes += [f"Ligne de remplissage numéro {i}, écrite pour que la page atteigne quarante lignes."
               for i in range(40 - len(lignes))]
    assert len(lignes) == 40
    return "\n".join(lignes) + "\n"


def temps_1(base):
    racine = base / "propre"
    subprocess.run(["git", "init", "-q", str(racine)], check=True)
    ecrire(racine / "dossier" / "README.md", page_propre(), fin="\r\n")
    ecrire(racine / "JOURNAL.md", "# Journal\n\n## Une section\n")
    ecrire(racine / "README.md", "# Racine\n\nUne page sans gras, dont le journal est à [`JOURNAL.md`](JOURNAL.md).\n")
    code, fautes, sortie = controle(racine)
    ok = code == 0 and not fautes and "2 README.md" in sortie
    print(f"  temps 1 — corpus propre (40 lignes CRLF, titres courants, code, lien encodé) : "
          f"{'PASSE' if ok else 'ÉCHEC'} (sortie {code})")
    if not ok:
        print(sortie)
    return ok


# ---------------------------------------------------------------- temps 2 : corpus réel

def copie_du_depot(base):
    """Copie les README.md, les JOURNAL.md et les .gitignore réels, suivis ou non ignorés."""
    r = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "-z", "--cached", "--others",
                        "--exclude-standard"], cwd=DEPOT, capture_output=True, check=True)
    racine = base / "reel"
    subprocess.run(["git", "init", "-q", str(racine)], check=True)
    for rel in filter(None, r.stdout.decode("utf-8").split("\0")):
        if Path(rel).name in ("README.md", "JOURNAL.md", ".gitignore") and (DEPOT / rel).is_file():
            (racine / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(DEPOT / rel, racine / rel)
    return racine


def ajouter_lignes(t, n):
    return t + "".join(f"Ligne ajoutée {i}.\n" for i in range(n))


def remplacer_ligne(t, motif, neuf):
    lignes = t.split("\n")
    i = next(k for k, l in enumerate(lignes) if motif in l)
    lignes[i] = neuf
    return "\n".join(lignes)


def temps_2(base):
    racine = copie_du_depot(base)
    code0, fautes0, sortie0 = controle(racine)
    print(f"  temps 2 — corpus réel copié : sortie {code0}, {len(fautes0)} écart(s) de référence")
    if code0 != 0:
        print(sortie0)
        return False
    page = racine / CIBLE
    original = page.read_text(encoding="utf-8")
    n0 = original.count("\n")
    long_titre = "**" + "x" * 400 + " :** remplace la première ligne de prose."

    # (nom, transformation du texte, extrait de faute attendu, ou None pour « rien »)
    mutations = [
        ("M1  une ligne de trop (41)", lambda t: ajouter_lignes(t, 41 - n0), "41 lignes, plus de 40"),
        ("M2  la quarantième ligne, pile", lambda t: ajouter_lignes(t, 40 - n0), None),
        ("M3  ⚠ dans la prose", lambda t: remplacer_ligne(t, "Quatre documents", "⚠ Quatre documents publiés."), "marqueur ⚠"),
        ("M4  ☑ dans une cellule de table", lambda t: remplacer_ligne(t, "| Vol. VI", "| Vol. VI ☑ | x | x | x |"), "marqueur ☑"),
        ("M5  ✎ dans la dernière ligne", lambda t: t.rstrip("\n") + " ✎\n", "marqueur ✎"),
        ("M5b ⚠ et gras dans un bloc clôturé", lambda t: t + "```\n⚠ **sortie** d'un script\n```\n" if n0 <= 37 else None, None),
        ("M6  gras de proposition", lambda t: remplacer_ligne(t, "Quatre documents", "Quatre documents, **et c'est voulu**."), "gras hors titre courant"),
        ("M7  titre courant sans deux-points", lambda t: t.replace("**Refaire :**", "**Refaire**", 1), "gras hors titre courant"),
        ("M8  gras en milieu de ligne, deux-points compris", lambda t: remplacer_ligne(t, "Quatre documents", "Quatre documents **publiés :** ici."), "gras hors titre courant"),
        ("M9  densité de gras au seuil franchi", lambda t: remplacer_ligne(t, "Quatre documents", long_titre), "seuil 5%"),
        ("M10 lien vers le journal retiré", lambda t: t.replace("](JOURNAL.md)", "](ARCHIVES.md)"), "aucun lien qui résout vers un JOURNAL.md"),
        ("M11 lien vers un journal absent", lambda t: t.replace("](JOURNAL.md)", "](absent/JOURNAL.md)"), "aucun lien qui résout vers un JOURNAL.md"),
        ("M12 gras et marqueur en span de code", lambda t: remplacer_ligne(t, "Quatre documents", "Quatre documents : `**x**` et `⚠`."), None),
    ]
    ok = True
    for nom, transformer, attendue in mutations:
        mute = transformer(original)
        if mute is None:
            print(f"    ⚠ {nom} — INAPPLICABLE à {CIBLE}")
            ok = False
            continue
        page.write_text(mute, encoding="utf-8", newline="\n")
        code, fautes, sortie = controle(racine)
        page.write_text(original, encoding="utf-8", newline="\n")
        if attendue is None:
            bon = code == 0 and not fautes
            verdict = "ignorée (attendu)" if bon else f"FAUX POSITIF : {fautes}"
        else:
            bon = code == 1 and fautes and all(p == CIBLE for p, _ in fautes) and any(attendue in f for _, f in fautes)
            verdict = "DÉTECTÉE sur la page" if bon else f"NON DÉTECTÉE (sortie {code}, vus {fautes})"
        ok &= bool(bon)
        print(f"    {'☑' if bon else '⚠'} {nom} — {verdict}")

    # M13 : une page d'accueil neuve, non suivie et non ignorée, est mesurée comme les autres.
    neuve = racine / "4 - Essais" / "README.md"
    ecrire(neuve, ajouter_lignes("# Neuve\n\n**Journal :** [j](<../JOURNAL.md>)\n", 38))
    code, fautes, sortie = controle(racine)
    neuve.unlink()
    bon = code == 1 and fautes == [("4 - Essais/README.md", "41 lignes, plus de 40")]
    ok &= bon
    print(f"    {'☑' if bon else '⚠'} M13 page neuve non suivie, 41 lignes — "
          f"{'DÉTECTÉE' if bon else f'NON DÉTECTÉE (sortie {code}, vus {fautes})'}")

    # M14 : une page ignorée par git n'est pas une page d'accueil du dépôt.
    ignoree = racine / "__pycache__" / "README.md"
    ecrire(ignoree, ajouter_lignes("# Ignorée\n", 60))
    code, fautes, _ = controle(racine)
    shutil.rmtree(ignoree.parent)
    bon = code == 0 and not fautes
    ok &= bon
    print(f"    {'☑' if bon else '⚠'} M14 page ignorée par .gitignore — {'ignorée (attendu)' if bon else f'FAUX POSITIF : {fautes}'}")
    return ok


def main():
    print("Harnais de check-lisibilite.py")
    with tempfile.TemporaryDirectory(prefix="lisibilite-") as tmp:
        base = Path(tmp)
        ok = temps_1(base) and temps_2(base)
    print("Toutes les mutations ont le verdict attendu." if ok else "⚠ HARNAIS EN ÉCHEC.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
