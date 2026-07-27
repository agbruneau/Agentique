#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harnais de mutation de `check-sieges.py`.

Doctrine du dépôt : *un script de contrôle est du contenu, il se vérifie comme le
reste.* La validation se fait en **deux temps, et le premier n'est pas facultatif** :

  1. constater que le contrôle **passe** sur le corpus intact ;
  2. introduire chaque classe de faute et constater qu'il **échoue**.

Sans le premier temps, un script cassé « détecte » tout et se croit bon.

Le corpus réel n'est jamais muté : chaque mutation s'applique à une copie jetable,
que `check-sieges.py` lit via la variable `COMPENDIUM_RACINE`.

Usage :  python check-sieges-mutations.py
Sortie 0 si le contrôle passe intact ET attrape les cinq mutations.
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SCRIPT = Path(__file__).resolve().parent / "check-sieges.py"

# La console Windows par défaut est en cp1252 et ne sait pas écrire « ☑ ».
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CH03 = "Livre I/03-securite-identite-gouvernance.md"
CH06 = "Livre I/06-multi-agents-evaluation-surete.md"
CH07 = "Livre I/07-genealogie-gouvernance.md"
CH08 = "Livre I/08-anatomie-mcp-a2a.md"


def executer(racine):
    """Retourne (code, sortie) de check-sieges.py sur la racine donnée."""
    r = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        env={**dict(__import__("os").environ), "COMPENDIUM_RACINE": str(racine)},
    )
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def copier():
    """Copie jetable du corpus : les pièces seules suffisent au contrôle."""
    tmp = Path(tempfile.mkdtemp(prefix="sieges-mut-"))
    for livre in RACINE.glob("Livre *"):
        shutil.copytree(livre, tmp / livre.name)
    return tmp


# --- les cinq mutations, une par contrôle -------------------------------------

def m1_marqueur_retire(tmp):
    """S2 — un siège perd son marqueur : plus personne ne sait qu'il en est un."""
    p = tmp / CH07
    p.write_text(p.read_text(encoding="utf-8")
                 .replace("SIÈGE DU GARDE-FOU R-8 POUR TOUTE LA SOMME",
                          "Encadré de désambiguïsation"), encoding="utf-8")


def m2_signature_recopiee(tmp):
    """S4 — une autre pièce reconstruit l'encadré au lieu d'y renvoyer."""
    p = tmp / CH06
    faux = ("\n\n| | Objet | Statut |\n| --- | --- | --- |\n"
            "| **(a)** | l'ACP protocolaire | fusionné |\n"
            "| **(b)** | l'Agentic Control Plane du consortium | annoncé |\n"
            "| **(c)** | l'expression employée par un éditeur | commercial |\n"
            "| **(d)** | la composante ACP de la couche d'infrastructure | non établie |\n"
            "\n: Tableau 6.9 — Les quatre branches.\n")
    texte = p.read_text(encoding="utf-8")
    coupe = texte.index("## § 6.3")
    p.write_text(texte[:coupe] + faux + texte[coupe:], encoding="utf-8")


def m3_renvoi_retire(tmp):
    """S5 — une pièce touche la matière du siège sans plus y renvoyer."""
    p = tmp / CH08
    texte = p.read_text(encoding="utf-8")
    p.write_text(re.sub(r"ch\.\s*7\s*§\s*7\.5", "plus haut", texte), encoding="utf-8")


def m4_signature_perimee(tmp):
    """S3 — le siège change de forme : sa signature ne le voit plus, ni une copie."""
    p = tmp / CH07
    texte = p.read_text(encoding="utf-8")
    p.write_text(texte.replace("| **(d)** |", "| **(4)** |"), encoding="utf-8")


def m5_siege_absent(tmp):
    """S1 — la pièce qui porte un siège disparaît du corpus."""
    (tmp / CH03).unlink()


MUTATIONS = [
    ("M1  S2 — marqueur de siège retiré", m1_marqueur_retire, "[S2]"),
    ("M2  S4 — signature du siège recopiée ailleurs", m2_signature_recopiee, "[S4]"),
    ("M3  S5 — renvoi au siège retiré", m3_renvoi_retire, "[S5]"),
    ("M4  S3 — signature périmée contre son propre siège", m4_signature_perimee, "[S3]"),
    ("M5  S1 — pièce porteuse du siège absente", m5_siege_absent, "[S1]"),
]


def main():
    print("Temps 1 — le contrôle passe-t-il sur le corpus intact ?")
    code, sortie = executer(RACINE)
    if code != 0:
        print("  ☐ NON. Le corpus est en écart ; aucune mutation n'est interprétable.")
        print("    " + sortie.strip().replace("\n", "\n    "))
        return 1
    print(f"  ☑ OUI — {sortie.strip()}")

    print("\nTemps 2 — chaque classe de faute est-elle attrapée ?")
    echecs = 0
    for nom, muter, attendu in MUTATIONS:
        tmp = copier()
        try:
            muter(tmp)
            code, sortie = executer(tmp)
            if code != 0 and attendu in sortie:
                print(f"  ☑ {nom}")
            elif code != 0:
                print(f"  ☐ {nom} — échoue, mais pas sur {attendu} : contrôle voisin déclenché")
                echecs += 1
            else:
                print(f"  ☐ {nom} — NON DÉTECTÉE (sortie 0)")
                echecs += 1
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    if echecs:
        print(f"\nÉCHEC — {echecs} mutation(s) sur {len(MUTATIONS)} non attrapée(s).")
        return 1
    print(f"\nOK — passe intact, et attrape les {len(MUTATIONS)} mutations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
