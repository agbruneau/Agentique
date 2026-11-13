"""Insère dans les exposés du manuscrit les schémas décrits par Master/schemas/schemas.json.

Usage : python Master/compendium-master-schemas.py

Chaque entrée du fichier donne : nom (fichier figures/<nom>.svg, produit par le script
Master/schemas/<nom>.py), chapitre, ancre (début exact du paragraphe de l'exposé après
lequel le schéma vient) et légende. L'insertion se rejoue sans doublon : une ligne de
figure déjà présente pour ce nom est d'abord retirée. Seul l'exposé est touché, jamais
un volet « Mise en œuvre ».
"""
import glob
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
MANUSCRIT = os.path.join(ICI, "manuscrit")
LISTE = os.path.join(ICI, "schemas", "schemas.json")
VOLET = re.compile(r"(?m)^(?=## Mise en œuvre — .* \{\.volet\}$)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    with open(LISTE, encoding="utf-8") as f:
        schemas = json.load(f)
    par_chapitre = {}
    for s in schemas:
        if not os.path.isfile(os.path.join(MANUSCRIT, "figures", s["nom"] + ".svg")):
            raise SystemExit("Figure absente : figures/%s.svg" % s["nom"])
        par_chapitre.setdefault(s["chapitre"], []).append(s)
    for numero, liste in sorted(par_chapitre.items()):
        chemin, = glob.glob(os.path.join(MANUSCRIT, "chapitre-%02d-*.md" % numero))
        with open(chemin, encoding="utf-8") as f:
            morceaux = VOLET.split(f.read())
        lignes = morceaux[0].split("\n")
        for s in liste:
            motif = re.compile(r"^!\[.*\]\(figures/%s\.svg\)$" % re.escape(s["nom"]))
            while any(motif.match(x) for x in lignes):          # retire une insertion antérieure
                i = next(k for k, x in enumerate(lignes) if motif.match(x))
                del lignes[i:i + 2 if i + 1 < len(lignes) and not lignes[i + 1].strip() else i + 1]
            ancre = s["ancre"].strip()
            cibles = [k for k, x in enumerate(lignes) if x.startswith(ancre)]
            if len(cibles) != 1:
                raise SystemExit("%s : ancre trouvée %d fois dans l'exposé du chapitre %d : %s"
                                 % (s["nom"], len(cibles), numero, ancre))
            ligne = lignes[cibles[0]]
            if re.match(r"(#|\||- |\d+\. |>|!\[)", ligne):
                raise SystemExit("%s : l'ancre doit être un paragraphe de texte courant" % s["nom"])
            legende = " ".join(s["legende"].split()).replace("[", "(").replace("]", ")")
            lignes[cibles[0] + 1:cibles[0] + 1] = ["", "![%s](figures/%s.svg)" % (legende, s["nom"])]
        morceaux[0] = "\n".join(lignes)
        with open(chemin, "w", encoding="utf-8", newline="\n") as f:
            f.write("".join(morceaux))
        print("chapitre %d : %s" % (numero, ", ".join(s["nom"] for s in liste)))
    print("%d schémas insérés dans %d chapitres" % (len(schemas), len(par_chapitre)))


if __name__ == "__main__":
    main()
