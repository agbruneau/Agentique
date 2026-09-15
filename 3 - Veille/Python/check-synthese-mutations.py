#!/usr/bin/env python3
"""Le harnais de `check-synthese.py` : chaque classe de faute, introduite puis vue.

Deux temps, comme les harnais voisins. D'abord le contrôle PASSE sur une copie intacte
— sans cela, un contrôle cassé « détecte » tout. Puis chaque mutation part d'une copie
fraîche, y injecte une faute d'une classe, et exige que le contrôle la nomme sous le
numéro attendu. Les mutations « muettes » ferment la marche : un PDF dont seul
l'horodatage bouge, un chiffre dans un span de code ou dans une section d'appareil ne
doivent rien déclencher, faute de quoi le contrôle crierait à chaque passage et
finirait désactivé.

La copie porte la note, son PDF et les sources des trois volumes, aux mêmes chemins
relatifs ; `check-synthese.py` la lit par `SYNTHESE_RACINE`. Le dépôt n'est jamais muté.

Usage, depuis `3 - Veille/` :  python Python/check-synthese-mutations.py
Sortie 0 si le temps 1 passe et si chaque mutation a le verdict attendu. Les mutations
qui exigent un rendu (parité, résumé) sont sautées, et le disent, sans Pandoc 3.11 et
Typst 0.15.1.
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
CHECK = ICI / "check-synthese.py"
DEPOT = ICI.parent.parent
FICHIERS = ("3 - Veille/Note de synthèse.md", "3 - Veille/Note de synthèse.pdf",
            "3 - Veille/Veille Technologique.md", "3 - Veille/Revue de littérature.md",
            "5 - Recension/État de l'art — services financiers.md")
NOTE = "3 - Veille/Note de synthèse.md"
PDF = "3 - Veille/Note de synthèse.pdf"


def executer(racine, *args):
    env = dict(os.environ, SYNTHESE_RACINE=str(racine), PYTHONUTF8="1")
    r = subprocess.run([sys.executable, str(CHECK), *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env)
    return r.returncode, r.stdout + r.stderr


def copie():
    tmp = Path(tempfile.mkdtemp(prefix="mutation-synthese-"))
    for f in FICHIERS:
        (tmp / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(DEPOT / f, tmp / f)
    return tmp


def remplacer(chemin, vieux, neuf, compte=1):
    t = chemin.read_bytes().decode("utf-8")
    assert vieux in t, f"{chemin.name} : « {vieux[:50]} » introuvable"
    chemin.write_bytes(t.replace(vieux, neuf, compte).encode("utf-8"))


def note(tmp, vieux, neuf, compte=1):
    remplacer(tmp / NOTE, vieux, neuf, compte)


def octets(tmp, motif, remplacement):
    p = tmp / PDF
    b = p.read_bytes()
    b2 = re.sub(motif, remplacement, b, count=1)
    assert b2 != b, f"motif {motif!r} absent du PDF"
    p.write_bytes(b2)


# --- une mutation par classe -------------------------------------------------------

def m1(tmp):
    """[1] — le PDF déclare 31 pages."""
    octets(tmp, rb"(/Type\s*/Pages\s*/Count\s*)\d+", rb"\g<1>31")


def m2(tmp):
    """[2] — un mot de la source change, le PDF n'est pas recomposé."""
    note(tmp, "Cette note condense trois documents", "Cette note résume trois documents")


def m2b(tmp):
    """[2] muet — seul l'horodatage du PDF bouge."""
    octets(tmp, rb"/ModDate\(D:\d{14}", rb"/ModDate(D:20991231235959")


def m2c(tmp):
    """[2] muet — rendu sous un autre fuseau : positions du xref décalées, longueur égale."""
    p = tmp / PDF
    b = p.read_bytes()
    b2 = re.sub(rb"(?m)^(\d{10})( \d{5} n)", lambda x: b"%010d" % (int(x.group(1)) - 5) + x.group(2), b)
    b2 = re.sub(rb"startxref(\s+)(\d+)", lambda x: b"startxref%s%d" % (x.group(1), int(x.group(2)) - 5), b2)
    assert b2 != b and len(b2) == len(b)
    p.write_bytes(b2)


def m3(tmp):
    """[3] — un renvoi vers une section que la veille n'a pas."""
    note(tmp, "[VI §7.1, réf. 272 — individuel, sans revue]", "[VI §7.19, réf. 272 — individuel, sans revue]")


def m3b(tmp):
    """[3] — une question ouverte que la section citée ne numérote pas."""
    note(tmp, "QO 14 — question]", "QO 15 — question]")


def m3c(tmp):
    """[3] — un renvoi en prose, hors crochets, vers une section absente."""
    note(tmp, "(VI §2.2, VI §10)", "(VI §2.2, VI §19)")


def m4(tmp):
    """[4] — un chiffre repris qui n'est plus celui de la source."""
    note(tmp, "91,8 %", "91,9 %")


def m4b(tmp):
    """[4] — un nombre en lettres altéré."""
    note(tmp, "douze brouillons individuels traitent", "treize brouillons individuels traitent")


def m4c(tmp):
    """[4] — un chiffre qu'aucun renvoi ne couvre."""
    note(tmp, "ce corpus s'auto-arbitre à moitié [VII §14.3 — corpus].",
         "ce corpus s'auto-arbitre à moitié [VII §14.3 — corpus]. Un chiffre de 42 % sans renvoi.")


def m4d(tmp):
    """[4] — le VOLUME change sous la note : la veille ne porte plus 91,8 %."""
    remplacer(tmp / "3 - Veille/Veille Technologique.md", "91,8 %", "91,7 %", compte=-1)


def m4e(tmp):
    """[4] — un nombre devenu pourcentage, que la source ne porte qu'en compte."""
    note(tmp, "sur six bancs et 245 caractéristiques", "sur six bancs et 245 % des caractéristiques")


def m4f(tmp):
    """[4] muet — un numéro dans un span de code, un chiffre dans une section d'appareil ;
    le PDF de la copie est recomposé, pour que la parité ne parle pas à la place de [4]."""
    note(tmp, "La couche bouge par rupture.", "La couche bouge par rupture (`v9.9.9`).")
    note(tmp, "**En une séance.**", "**En une séance de 45 minutes.**")


def m5(tmp):
    """[5] — le niveau d'une pièce de la revue monté au-dessus de sa notice."""
    note(tmp, "[VII §15.1, réf. 77, 76, 85 — sans revue]", "[VII §15.1, réf. 77, 76, 85 — attestée]")


def m5b(tmp):
    """[5] — « pipeline » hors des sections 4.6 à 4.13 de la veille."""
    note(tmp, "[VI §9.7 — individuel]", "[VI §9.7 — pipeline]")


def m5c(tmp):
    """[5] — une étiquette de la revue prêtée à l'état de l'art."""
    note(tmp, "[VIII §4.2 — individuel]", "[VIII §4.2 — corpus]")


def m5d(tmp):
    """[5] — un régime de publication sans notice qui le porte."""
    note(tmp, "[VII §3.1 — corpus]", "[VII §3.1 — attestée]")


def m5e(tmp):
    """[5] — le régime de publication d'une prépublication arXiv retiré de l'étiquette : l'écart
    que le critique de la reprise du 15 septembre 2026 a relevé sur le 91,8 %."""
    note(tmp, "[VI §7.1, réf. 272 — individuel, sans revue]", "[VI §7.1, réf. 272 — individuel]")


def m5f(tmp):
    """[5] — un régime de publication prêté à une notice qui n'est pas une prépublication."""
    note(tmp, "[VI §12.2, réf. 80 — individuel]", "[VI §12.2, réf. 80 — individuel, sans revue]")


def m8(tmp):
    """[8] — une décomposition qui ne somme plus, chaque terme restant celui de la source :
    l'écart de l'audit du 8 août, six auto-citations omises."""
    note(tmp, "269 = 179 + 54 + 30 + 6", "269 = 179 + 54 + 30")


def m8b(tmp):
    """[8] — une part qui n'est pas son pourcentage ; 63 % figure pourtant à la section citée."""
    note(tmp, "145 sur 189 · 77 %", "145 sur 189 · 63 %")


def m6(tmp):
    """[6] — une notice listée que rien ne cite."""
    note(tmp, "- **VI [80]**", "- **VI [1]** A survey of agent interoperability protocols\n- **VI [80]**")


def m6b(tmp):
    """[6] — une notice citée par un renvoi, absente des références."""
    note(tmp, "[VI §7.1, réf. 272 — individuel, sans revue]", "[VI §7.1, réf. 272, 271 — individuel, sans revue]")


def m6c(tmp):
    """[6] — un fragment qui ne se lit plus dans la notice du volume."""
    note(tmp, "« An Empirical Study of Model Context Protocol Applications »",
         "« An Empirical Study of Agent Context Protocol Applications »")


def m6d(tmp):
    """[6] — une clé appelée sans entrée."""
    note(tmp, "[PLAN].", "[PLANS].")


def m7(tmp):
    """[7] — un résumé qui déborde sa page, PDF recomposé depuis la source mutée."""
    t = (tmp / NOTE).read_bytes().decode("utf-8")
    debut = t.index("abstract: |\n") + len("abstract: |\n")
    fin = t.index("header-includes: |")
    corps = t[debut:fin]
    (tmp / NOTE).write_bytes((t[:debut] + corps * 4 + t[fin:]).encode("utf-8"))


# Ces deux-là recomposent le PDF de la copie avant de contrôler : M7 pour que le résumé
# débordant soit dans le PDF mesuré, M4f pour que la parité tienne et que seul [4] parle.
RECOMPOSEES = (m4f, m7)

MUTATIONS = [
    # (nom, mutation, contrôle attendu, genre, exige un rendu, fragment attendu dans l'échec)
    ("M1  [1] le PDF déclare 31 pages", m1, "1", "echec", False, "compte 31 pages"),
    ("M2  [2] source reprise, PDF non recomposé", m2, "2", "echec", True, "n'est pas le rendu"),
    ("M2b [2] seul l'horodatage du PDF bouge", m2b, "2", "muet", True, ""),
    ("M2c [2] positions du xref décalées (fuseau)", m2c, "2", "muet", True, ""),
    ("M3  [3] renvoi vers une section absente", m3, "3", "echec", False, "VI §7.19 ne nomme aucune section"),
    ("M3b [3] question ouverte non numérotée", m3b, "3", "echec", False, "pas de question n° 15"),
    ("M3c [3] renvoi en prose vers une section absente", m3c, "3", "echec", False, "VI §19 ne nomme aucune section"),
    ("M4  [4] chiffre altéré dans la note", m4, "4", "echec", False, "« 91,9 % » ne figure pas"),
    ("M4b [4] nombre en lettres altéré", m4b, "4", "echec", False, "« 13 » ne figure pas"),
    ("M4c [4] chiffre sans renvoi", m4c, "4", "echec", False, "42% sans renvoi"),
    ("M4d [4] le volume change sous la note", m4d, "4", "echec", False, "« 91,8 % » ne figure pas dans VI §7.1"),
    ("M4e [4] compte devenu pourcentage", m4e, "4", "echec", False, "« 245 % » ne figure pas"),
    ("M4f [4] chiffres en code et en appareil", m4f, "4", "muet", True, ""),
    ("M5  [5] niveau de la revue monté", m5, "5", "echec", False, "portent au plus « sans revue »"),
    ("M5b [5] « pipeline » hors 4.6-4.13", m5b, "5", "echec", False, "ne vaut qu'aux sections"),
    ("M5c [5] étiquette hors vocabulaire", m5c, "5", "echec", False, "hors du vocabulaire du Vol. VIII"),
    ("M5d [5] régime sans notice", m5d, "5", "echec", False, "exige la notice"),
    ("M5e [5] prépublication sans son régime", m5e, "5", "echec", False, "prépublication arXiv au régime « sans revue »"),
    ("M5f [5] régime prêté à une notice non arXiv", m5f, "5", "echec", False, "exige la notice arXiv"),
    ("M6  [6] notice listée jamais citée", m6, "6", "echec", False, "VI [1] listée, citée par aucun renvoi"),
    ("M6b [6] notice citée jamais listée", m6b, "6", "echec", False, "VI réf. 271 citée par un renvoi"),
    ("M6c [6] fragment absent de la notice", m6c, "6", "echec", False, "ne se lit pas dans la notice 54"),
    ("M6d [6] clé appelée sans entrée", m6d, "6", "echec", False, "[PLANS] appelée dans le corps"),
    ("M7  [7] résumé qui déborde, PDF recomposé", m7, "7", "echec", True, "check-resume.py"),
    ("M8  [8] décomposition qui ne somme plus", m8, "8", "echec", False, "les termes font 263"),
    ("M8b [8] part fausse, pourcentage présent à la source", m8b, "8", "echec", False, "145 sur 189 font 76,7 %"),
]


def echecs(sortie):
    """{numéro de contrôle: [lignes d'échec]} — chaque mutation doit nommer SA faute."""
    out = {}
    for m in re.finditer(r"(?m)^\s*- \[(\d)\] (.*)$", sortie):
        out.setdefault(m.group(1), []).append(m.group(2))
    return out


def main():
    print("Temps 1 — le contrôle passe-t-il sur une copie intacte ?")
    tmp = copie()
    try:
        code, sortie = executer(tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if code != 0:
        print("  ☐ non : aucune mutation n'est interprétable.\n" + sortie)
        return 1
    rendu = "NON MESURÉ" not in sortie
    print("  ☑ oui" + ("" if rendu else " — parité NON MESURÉE : les mutations à rendu seront sautées"))

    print("\nTemps 2 — chaque classe de faute est-elle vue ?")
    manques = 0
    for nom, muter, attendu, genre, a_rendu, indice in MUTATIONS:
        if a_rendu and not rendu:
            print(f"  – {nom} — sautée (Pandoc 3.11 et Typst 0.15.1 requis)")
            continue
        tmp = copie()
        try:
            muter(tmp)
            code, sortie = executer(tmp, *(["--rendre"] if muter in RECOMPOSEES else []))
            vus = echecs(sortie)
            if genre == "muet":
                bon = code == 0 and not vus
                verdict = "aucun échec (attendu)" if bon else f"échec indu : {sorted(vus)}"
            else:
                bon = code != 0 and any(indice in l for l in vus.get(attendu, []))
                verdict = "vue" if bon else (f"échec voisin {sorted(vus)}" if vus else "aucun échec")
            print(f"  {'☑' if bon else '☐'} {nom} — {verdict}")
            if not bon:
                manques += 1
                print("    " + "\n    ".join(sortie.strip().splitlines()[-6:]))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    if manques:
        print(f"\nÉCHEC — {manques} mutation(s) sans le verdict attendu.")
        return 1
    print(f"\nOK — copie intacte tenue, et les {len(MUTATIONS)} mutations ont le verdict attendu.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
