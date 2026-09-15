#!/usr/bin/env python3
"""Le harnais de `check-vol1.py` : chaque classe de faute, introduite dans une copie, puis vue.

Deux temps, comme les harnais du dépôt. D'abord le contrôle doit PASSER sur le dossier
intact — sans quoi il « détecte » tout. Puis une copie du dossier reçoit une faute par
classe, et le contrôle doit la voir ; une mutation « muette » ferme la marche : un PDF dont
seul l'horodatage change doit passer la parité.

Les mutations de parité [3] demandent la chaîne complète (voir `check-vol1.py`) et une
trentaine de secondes chacune ; sans elle, elles sont SAUTÉES et le harnais le dit.

Usage : python Python/check-vol1-mutations.py   -> 0 si tout est vu, 1 sinon.
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

RACINE = Path(__file__).resolve().parent.parent
CHECK = RACINE / "Python" / "check-vol1.py"
FICHIERS = ("Monographie.md", "Monographie.pdf", "README.md",
            "build/build-pdf.sh", "build/fesp.template", "build/inject-pagination.py")


def executer(racine: Path, *args):
    env = dict(os.environ, VOL1_RACINE=str(racine), PYTHONUTF8="1")
    r = subprocess.run([sys.executable, str(CHECK), *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env)
    return r.returncode, r.stdout + r.stderr


def copie():
    tmp = Path(tempfile.mkdtemp(prefix="mutation-vol1-"))
    for f in FICHIERS:
        (tmp / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / f, tmp / f)
    return tmp


def remplacer(chemin: Path, vieux: str, neuf: str):
    t = chemin.read_text(encoding="utf-8")
    assert t.count(vieux) >= 1, f"{chemin.name} : « {vieux[:50]} » introuvable"
    chemin.write_text(t.replace(vieux, neuf, 1), encoding="utf-8", newline="\n")


# --- une mutation par classe -----------------------------------------------------

AUTEUR_ORPHELIN = "Zéphyrin-Orphelin"


def m1_notice_orpheline(tmp):
    """[2] — une notice ajoutée à la bibliographie du ch. 3, que le corps ne cite nulle part."""
    md = tmp / "Monographie.md"
    t = md.read_text(encoding="utf-8")
    assert AUTEUR_ORPHELIN.lower() not in t.lower(), "l'auteur témoin figure déjà dans le volume"
    ancre = "\n## Chapitre 4 —"
    assert t.count(ancre) == 1
    notice = (f"\n- {AUTEUR_ORPHELIN}, Q. (2026). *Une notice que le corps ne cite pas*. "
              "Éditeur témoin, injectée par le harnais.\n")
    md.write_text(t.replace(ancre, notice + ancre, 1), encoding="utf-8", newline="\n")


def m2_registre_perime(tmp):
    """[2] — une notice du registre sort de la bibliographie : le registre ne la couvre plus."""
    md = tmp / "Monographie.md"
    t = md.read_text(encoding="utf-8")
    lignes = [l for l in t.split("\n") if l.startswith("- ") and "*Spectral: Open-Source API Description Linter*" in l]
    assert len(lignes) == 1, "notice témoin du registre introuvable"
    md.write_text(t.replace(lignes[0] + "\n", "", 1), encoding="utf-8", newline="\n")


def m3_pagination_publiee(tmp):
    """[1] — le README publie un nombre de pages que le PDF n'a pas."""
    readme = tmp / "README.md"
    t = readme.read_text(encoding="utf-8")
    m = re.search(r"(\*\*Lire :\*\*.*?\()(\d+)( p\.\))", t)
    assert m, "ligne « Lire » introuvable"
    readme.write_text(t[:m.start(2)] + str(int(m.group(2)) + 1) + t[m.end(2):], encoding="utf-8", newline="\n")


def m4_rendu_perime(tmp):
    """[3] — la source change d'un mot, le PDF n'est pas recomposé."""
    remplacer(tmp / "Monographie.md", "# Remerciements", "# Remerciement")


def m4b_horodatage_seul(tmp):
    """[3] — *ne doit pas voir* : seules les dates du PDF bougent."""
    p = tmp / "Monographie.pdf"
    b = p.read_bytes()
    b2 = re.sub(rb"/ModDate\s*\(D:\d{14}", rb"/ModDate(D:20991231235959", b, count=1)
    assert b2 != b, "aucun /ModDate à muter"
    p.write_bytes(b2)


MUTATIONS = [
    ("M1  [2] notice orpheline injectée", m1_notice_orpheline, "[2]", "echec"),
    ("M2  [2] registre périmé", m2_registre_perime, "[2]", "echec"),
    ("M3  [1] pagination publiée fausse", m3_pagination_publiee, "[1]", "echec"),
    ("M4  [3] source reprise, PDF non recomposé", m4_rendu_perime, "[3]", "echec"),
    ("M4b [3] seul l'horodatage du PDF bouge", m4b_horodatage_seul, "[3]", "muet"),
]

NOMS = {"[1]": "pagination —", "[2]": "appariement —", "[3]": "parité —"}


def main():
    print("Temps 1 — le contrôle passe-t-il sur le dossier intact ?")
    code, sortie = executer(RACINE)
    if code != 0:
        print("  ☐ non : aucune mutation n'est interprétable.")
        print(sortie)
        return 1
    parite = "NON MESURÉ" not in sortie
    print("  ☑ oui" + ("" if parite else " — parité NON MESURÉE (chaîne incomplète) : M4 et M4b seront sautées"))

    print("\nTemps 2 — chaque classe de faute est-elle vue, et par le contrôle attendu ?")
    manques = sautees = 0
    for nom, muter, attendu, genre in MUTATIONS:
        if attendu == "[3]" and not parite:
            print(f"  – {nom} — sautée")
            sautees += 1
            continue
        tmp = copie()
        try:
            muter(tmp)
            # Une faute de [1] ou de [2] qui touche la source rompt aussi la parité, par
            # construction : on la mesure donc sans [3], pour exiger qu'elle soit vue par SON contrôle.
            code, sortie = executer(tmp, *(() if attendu == "[3]" else ("--sans-parite",)))
            echecs = [l.strip()[2:] for l in sortie.splitlines() if l.strip().startswith("- ")]
            if genre == "muet":
                vu = code == 0 and not echecs
                verdict = "aucun échec (attendu)" if vu else f"échec indu : {echecs[:1]}"
            else:
                # vue par SON contrôle, et par lui seul : un échec voisin ne compte pas
                vu = code != 0 and bool(echecs) and all(e.startswith(NOMS[attendu]) for e in echecs)
                verdict = "vue" if vu else (f"échec voisin : {echecs[0][:90]}" if echecs else "aucun échec")
            print(f"  {'☑' if vu else '☐'} {nom} — {verdict}")
            manques += 0 if vu else 1
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    if manques:
        print(f"\nÉCHEC — {manques} mutation(s) non vue(s).")
        return 1
    print(f"\nOK — dossier intact tenu, et les {len(MUTATIONS) - sautees} mutations jouées sont vues"
          f"{f' ; {sautees} de parité sautées, chaîne incomplète' if sautees else ''}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
