#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harnais de mutation de `verifier-piece.py`.

⚠ **Sans la première constatation, un script cassé « détecte » tout.** Le
harnais mesure donc d'abord le **passage sur le corpus intact**, puis introduit
une faute par classe et vérifie qu'elle est **vue** — et, pour deux d'entre
elles, qu'une matière légitime **n'est pas** vue.

*Le contrôle vérifié ici est celui qui manquait pendant cinq semaines : rien ne
distinguait un `.html` régénéré d'un `.html` simplement modifié au même commit
que sa source.*
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SCRIPT = RACINE / "build" / "verifier-piece.py"
CH01 = "Livre I/01-interoperabilite-integration-entreprise"
CH25 = "Livre III/25-e23-risque-modele"


def executer(racine):
    r = subprocess.run(
        [sys.executable, str(racine / "build" / "verifier-piece.py")],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        env={**dict(os.environ), "COMPENDIUM_RACINE": str(racine)},
    )
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def echecs(sortie):
    return [l.strip() for l in sortie.splitlines()
            if re.match(r"^\s*\[[123]\]", l)]


def copier():
    """Copie jetable : les cinquante pièces, leurs rendus, et `build/`.

    ⚠ `figures/` n'en fait PAS partie, et c'est délibéré : ni le rendeur ni le
    vérificateur n'ouvrent un SVG — ils manipulent des chemins. Copier cent
    dix-huit figures à chaque mutation coûterait sans rien éprouver.
    """
    tmp = Path(tempfile.mkdtemp(prefix="rendu-mut-"))
    for f in list(RACINE.glob("Livre */[0-9]*.md")) + list(RACINE.glob("Livre */[0-9]*.html")):
        cible = tmp / f.parent.name / f.name
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, cible)
    (tmp / "build").mkdir()
    for nom in ("rendre-piece.py", "verifier-piece.py", "piece.template"):
        shutil.copy2(RACINE / "build" / nom, tmp / "build" / nom)
    return tmp


# --- une mutation par classe --------------------------------------------------

def m1_source_revisee(tmp):
    """[1] — le `.md` bouge, le `.html` reste : le défaut exact du 31 juillet.

    Une passe de révision du français change un mot au corps et ne régénère
    pas le rendu. C'est ce qui s'est produit six fois entre le 31 juillet et le
    3 août 2026, et rien ne l'a rapporté.
    """
    f = tmp / (CH01 + ".md")
    t = f.read_text(encoding="utf-8")
    assert "coût continu" in t
    f.write_text(t.replace("coût continu", "coût permanent", 1), encoding="utf-8")


def m2_figure_retiree(tmp):
    """[1] et [3] — une figure disparaît du rendu.

    La classe qui a tenu le plus longtemps : **114 des 115 figures** absentes
    des rendus versionnés, sans qu'aucun contrôle ne s'en avise.
    """
    f = tmp / (CH01 + ".html")
    t = f.read_text(encoding="utf-8")
    i = t.index('<figure class="figure">')
    j = t.index("</figure>", i) + len("</figure>")
    f.write_text(t[:i] + t[j:], encoding="utf-8")


def m3_appareil_recopie(tmp):
    """[2] — le rendu recopie l'en-tête à cinq champs.

    La purge du 29 juillet 2026 est une règle de fond, non un effet du
    découpage : un rendeur qui la lèverait publierait la gouvernance avec le
    corps, et le `.md` cesserait d'être la seule source.
    """
    f = tmp / (CH25 + ".html")
    t = f.read_text(encoding="utf-8")
    i = t.index('<main class="corps">')
    bloc = ("\n<table>\n<thead><tr><th>Champ</th><th>Valeur</th></tr></thead>\n"
            "<tbody><tr><td>Statut</td><td>Brouillon</td></tr></tbody>\n</table>\n")
    f.write_text(t[:i] + bloc + t[i:], encoding="utf-8")


def m4_rendu_absent(tmp):
    """[1] — la source est versionnée sans son rendu."""
    (tmp / (CH25 + ".html")).unlink()


def m5_commentaire_de_doctrine(tmp):
    """[2] — *ne doit pas voir* : la règle citée en commentaire n'est pas une
    infraction.

    ⚠ La garde du contrôle, et elle est vécue : le gabarit porte lui-même la
    phrase « NI EN-TÊTE À CINQ CHAMPS, NI THÈSE, NI NOTE DE STATUT », et la
    première version de [2] échouait sur les cinquante pièces le jour de sa
    mise en service. *Un contrôle qui lit la règle écrite dans le fichier comme
    une violation du fichier ne contrôle rien : il se contrôle lui-même.*
    """
    f = tmp / (CH01 + ".html")
    t = f.read_text(encoding="utf-8")
    i = t.index('<main class="corps">')
    f.write_text(t[:i] + "\n<!-- Note de statut : Champ / Valeur, thèse citée. -->\n"
                 + t[i:], encoding="utf-8")


def m6_figure_deplacee(tmp):
    """[3] — les figures y sont toutes, dans le mauvais ordre.

    *Un contrôle qui compte les figures sans les ordonner accepte un rendu qui
    place la figure 1.5 avant la 1.0.*
    """
    f = tmp / (CH01 + ".html")
    t = f.read_text(encoding="utf-8")
    a = t.index('<figure class="figure">')
    fa = t.index("</figure>", a) + len("</figure>")
    b = t.index('<figure class="figure">', fa)
    fb = t.index("</figure>", b) + len("</figure>")
    f.write_text(t[:a] + t[b:fb] + t[fa:b] + t[a:fa] + t[fb:], encoding="utf-8")


MUTATIONS = [
    ("M1  [1] la source révisée, le rendu inchangé", m1_source_revisee, "[1]", "echec"),
    ("M2  [1][3] une figure retirée du rendu", m2_figure_retiree, "[3]", "echec"),
    ("M3  [2] le rendu recopie l'en-tête à cinq champs", m3_appareil_recopie, "[2]", "echec"),
    ("M4  [1] la source versionnée sans son rendu", m4_rendu_absent, "[1]", "echec"),
    ("M5  [2] la règle citée EN COMMENTAIRE", m5_commentaire_de_doctrine, "[2]", "muet"),
    ("M6  [3] les figures dans le mauvais ordre", m6_figure_deplacee, "[3]", "echec"),
]


def main():
    print("Temps 1 — que rend le contrôle sur le corpus intact ?")
    code, sortie = executer(RACINE)
    base = echecs(sortie)
    if base or code != 0:
        print(f"  ☐ {len(base)} écart(s), sortie {code} — la ligne de base n'est pas")
        print("    à zéro ; aucune mutation n'est interprétable tant qu'elle n'y est pas.")
        for e in base[:5]:
            print(f"    {e}")
        return 1
    print("  ☑ ligne de base à zéro sur les cinquante pièces.")

    print("\nTemps 2 — chaque classe de faute est-elle vue ?")
    manques = 0
    for nom, muter, attendu, genre in MUTATIONS:
        tmp = copier()
        try:
            muter(tmp)
            _, s = executer(tmp)
            neufs = echecs(s)
            if genre == "muet":
                # ⚠ La garde porte sur SA classe, pas sur le silence complet :
                # insérer un commentaire dans un rendu casse la parité [1], et
                # c'est juste. Ce qu'on éprouve ici, c'est que [2] ne lise pas
                # un commentaire comme une infraction.
                indus = [e for e in neufs if e.startswith(attendu)]
                vu = not indus
                verdict = (f"{attendu} muet (attendu)" if vu
                           else f"écart indu : {indus[0][:64]}")
            else:
                vu = any(e.startswith(attendu) for e in neufs)
                verdict = "vue" if vu else (
                    "aucun écart" if not neufs else f"écart voisin : {neufs[0][:64]}")
            print(f"  {'☑' if vu else '☐'} {nom} — {verdict}")
            manques += 0 if vu else 1
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    if manques:
        print(f"\nÉCHEC — {manques} mutation(s) sur {len(MUTATIONS)} non vue(s).")
        return 1
    print(f"\nOK — ligne de base à zéro, et les {len(MUTATIONS)} mutations sont vues.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
