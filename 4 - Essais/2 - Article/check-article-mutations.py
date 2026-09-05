#!/usr/bin/env python3
"""Le harnais de `check-article.py` : chaque classe de faute, introduite puis vue.

Deux temps. D'abord le constat que le contrôle PASSE sur le dossier intact — sans
lui, un contrôle cassé « détecte » tout. Puis, pour chaque contrôle, une copie du
dossier reçoit une faute de sa classe, et le contrôle doit la voir. Une mutation
« ne doit pas voir » ferme la marche : un PDF dont seul l'horodatage change doit
passer la parité, sinon le contrôle crie à chaque rendu et finit désactivé.

Usage : python check-article-mutations.py   -> 0 si tout est vu, 1 sinon.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent
CHECK = RACINE / "check-article.py"
FICHIERS = ("article-hpc-qpu.typ", "article-hpc-qpu.pdf", "references.bib",
            "README.md", "rejeu-politique.py", ".gabarit-arxiv.typ", ".figures.typ")


def executer(racine: Path, *args):
    env = dict(os.environ, ARTICLE_RACINE=str(racine), PYTHONUTF8="1")
    r = subprocess.run([sys.executable, str(CHECK), *args], capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=env)
    return r.returncode, r.stdout + r.stderr


def copie():
    tmp = Path(tempfile.mkdtemp(prefix="mutation-article-"))
    for f in FICHIERS:
        shutil.copy2(RACINE / f, tmp / f)
    return tmp


def remplacer(chemin: Path, vieux: str, neuf: str):
    t = chemin.read_text(encoding="utf-8")
    assert t.count(vieux) >= 1, f"{chemin.name} : « {vieux[:40]} » introuvable"
    chemin.write_text(t.replace(vieux, neuf, 1), encoding="utf-8")


# --- une mutation par classe ---------------------------------------------------

def m1_cle_morte(tmp):
    """[1] — une entrée du .bib que le corps ne cite plus."""
    (tmp / "references.bib").write_text(
        (tmp / "references.bib").read_text(encoding="utf-8")
        + "\n@misc{orpheline,\n  title = {Une entrée que rien ne cite},\n  year = {2026}\n}\n",
        encoding="utf-8")


def m1b_cle_pendante(tmp):
    """[1] — une citation du corps que le .bib ne définit pas."""
    remplacer(tmp / "article-hpc-qpu.typ", "@survey", "@surveyy")


def m2_rendu_perime(tmp):
    """[2] — le PDF versionné n'est plus celui de la source : un mot de la source change."""
    remplacer(tmp / "article-hpc-qpu.typ", "Quatre états et un niveau", "Cinq états et un niveau")


def m2b_horodatage_seul(tmp):
    """[2] — *ne doit pas voir* : seul l'horodatage du PDF bouge."""
    p = tmp / "article-hpc-qpu.pdf"
    b = p.read_bytes()
    b2 = re.sub(rb"/ModDate\(D:\d{14}", rb"/ModDate(D:20991231235959", b, count=1)
    assert b2 != b, "aucun /ModDate à muter"
    p.write_bytes(b2)


def m3_renvoi_mort(tmp):
    """[3] — un « § » vers une section qui n'existe pas."""
    remplacer(tmp / "article-hpc-qpu.typ", "§ 7.5", "§ 7.9")


def m4_cardinal_faux(tmp):
    """[4] — le README publie un nombre que la mesure ne rend pas."""
    remplacer(tmp / "README.md", "**8 planches**", "**9 planches**")


def m5_score_divergent(tmp):
    """[5] — l'article imprime un score que le script n'attend pas (RÉF-6 par la forme)."""
    remplacer(tmp / "article-hpc-qpu.typ", 'bold("0,703")', 'bold("0,713")')


MUTATIONS = [
    ("M1  [1] entrée définie jamais citée", m1_cle_morte, "[1]", "echec"),
    ("M1b [1] citation jamais définie", m1b_cle_pendante, "[1]", "echec"),
    ("M2  [2] source reprise, PDF non recomposé", m2_rendu_perime, "[2]", "echec"),
    ("M2b [2] seul l'horodatage du PDF bouge", m2b_horodatage_seul, "[2]", "muet"),
    ("M3  [3] renvoi « § » vers une section absente", m3_renvoi_mort, "[3]", "echec"),
    ("M4  [4] cardinal du README faux", m4_cardinal_faux, "[4]", "echec"),
    ("M5  [5] score imprimé divergent du script", m5_score_divergent, "[5]", "echec"),
]


def echecs(sortie: str):
    return [l.strip() for l in sortie.splitlines() if l.strip().startswith("- ")]


def main():
    print("Temps 1 — le contrôle passe-t-il sur le dossier intact ?")
    code, sortie = executer(RACINE)
    if code != 0:
        print("  ☐ non : aucune mutation n'est interprétable.")
        print(sortie)
        return 1
    parite_mesurable = "NON MESURÉ" not in sortie
    print("  ☑ oui" + ("" if parite_mesurable else " — parité NON MESURÉE (typst absent) : M2 et M2b seront sautées"))

    print("\nTemps 2 — chaque classe de faute est-elle vue ?")
    manques = 0
    for nom, muter, attendu, genre in MUTATIONS:
        if attendu == "[2]" and not parite_mesurable:
            print(f"  – {nom} — sautée")
            continue
        tmp = copie()
        try:
            muter(tmp)
            code, sortie = executer(tmp)
            neufs = echecs(sortie)
            if genre == "muet":
                vu = code == 0 and not neufs
                verdict = "aucun échec (attendu)" if vu else f"échec indu : {neufs[:1]}"
            else:
                vu = code != 0 and any(attendu.strip("[]") in l.split("—")[0] or attendu in l
                                       for l in neufs) or (code != 0 and attendu in sortie and neufs)
                verdict = "vue" if vu else ("aucun échec" if not neufs else f"échec voisin : {neufs[0][:70]}")
            print(f"  {'☑' if vu else '☐'} {nom} — {verdict}")
            manques += 0 if vu else 1
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    if manques:
        print(f"\nÉCHEC — {manques} mutation(s) non vue(s).")
        return 1
    print(f"\nOK — dossier intact tenu, et les {len(MUTATIONS)} mutations sont vues.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
