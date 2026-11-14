"""Corrections de l'audit de publication : registre unique, appliqué au manuscrit.

Usage :
  python Master/compendium-master-audit.py --applique   applique le registre au manuscrit
  python Master/compendium-master-audit.py --bilan      décompte par fichier et par catégorie

Le registre Master/audit/corrections.json liste chaque correction retenue à l'audit :
fichier du manuscrit, texte avant, texte après, catégorie et motif. Une correction est
un remplacement exact, à un seul endroit du fichier. Le script est idempotent : une
correction déjà appliquée est laissée telle quelle.

Le manuscrit reste soumis aux contrôles de compendium-master-verifie.py, qui compare
les exposés à l'édition C et les volets à leur original : la vérification applique le
même registre au texte de référence avant de comparer (fonction corrige), si bien que
seules les corrections déclarées ici peuvent écarter le manuscrit de ses sources.
Les volets, l'ouverture et les annexes F à H réécrits ont une copie dans
Master/fusion/reecrit/ : la correction y est reportée.

Le registre porte aussi, sous les catégories « enrichissement » et « harmonisation », les
compléments postérieurs à l'audit (sections ajoutées aux exposés, mise à jour des annexes,
renvois croisés) : même mécanisme, mêmes contrôles. compendium-master-assemble.py les
décompte à part des corrections de l'audit.
"""
import collections
import glob
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
MANUSCRIT = os.path.join(ICI, "manuscrit")
REECRIT = os.path.join(ICI, "fusion", "reecrit")
REGISTRE = os.path.join(ICI, "audit", "corrections.json")


def registre():
    if not os.path.isfile(REGISTRE):
        return []
    with open(REGISTRE, encoding="utf-8") as f:
        return json.load(f)


def par_fichier():
    groupes = collections.defaultdict(list)
    for c in registre():
        groupes[c["fichier"]].append(c)
    return groupes


def corrige(nom, texte):
    """Applique à un texte de référence les corrections du fichier `nom` qui s'y trouvent."""
    for c in par_fichier().get(os.path.basename(nom), []):
        if c["avant"] in texte:
            texte = texte.replace(c["avant"], c["apres"])
        elif c["avant"].endswith("\n") and texte.endswith(c["avant"].rstrip("\n")):
            # Ligne supprimée en toute fin d'un texte de référence sans saut de ligne final.
            texte = texte[:-len(c["avant"].rstrip("\n"))] + c["apres"]
    return texte


def ajouts(nom):
    """Textes introduits par les corrections d'un fichier : appui des contrôles de conformité."""
    return "\n".join(c["apres"] for c in par_fichier().get(os.path.basename(nom), []))


def copies(nom):
    """Copies réécrites (Master/fusion/reecrit) du contenu d'un fichier du manuscrit."""
    if nom == "ouverture.md":
        return [os.path.join(REECRIT, "ouverture.md")]
    if nom.startswith("annexe-"):
        return glob.glob(os.path.join(REECRIT, nom[:8] + ".md"))
    return sorted(glob.glob(os.path.join(REECRIT, nom[:11] + "-volet-*.md")))


def lit(chemin):
    with open(chemin, encoding="utf-8") as f:
        return f.read()


def ecrit(chemin, texte):
    with open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write(texte)


def applique():
    faites = deja = 0
    erreurs = []
    for nom, corrections in sorted(par_fichier().items()):
        chemin = os.path.join(MANUSCRIT, nom)
        texte = lit(chemin)
        reecrits = {c: lit(c) for c in copies(nom)}
        for c in corrections:
            n = texte.count(c["avant"])
            if n == 1:
                texte = texte.replace(c["avant"], c["apres"])
                faites += 1
            elif n == 0 and (not c["apres"] or c["apres"] in texte):
                deja += 1
            else:
                erreurs.append("%s n° %s : « %s » trouvé %d fois" % (nom, c["n"], c["avant"][:60], n))
                continue
            for copie in reecrits:
                if reecrits[copie].count(c["avant"]) == 1:
                    reecrits[copie] = reecrits[copie].replace(c["avant"], c["apres"])
        ecrit(chemin, texte)
        for copie, contenu in reecrits.items():
            ecrit(copie, contenu)
    print("corrections appliquées : %d, déjà en place : %d, en erreur : %d" % (faites, deja, len(erreurs)))
    for e in erreurs:
        print("  " + e)
    if erreurs:
        raise SystemExit(1)


def controle():
    """Écarts entre le registre et le manuscrit; liste vide si tout est appliqué."""
    defauts = []
    numeros = [c["n"] for c in registre()]
    if len(set(numeros)) != len(numeros):
        defauts.append("numéros de correction en double")
    for nom, corrections in par_fichier().items():
        chemin = os.path.join(MANUSCRIT, nom)
        if not os.path.isfile(chemin):
            defauts.append("%s : fichier absent du manuscrit" % nom)
            continue
        texte = lit(chemin)
        for c in corrections:
            if c["apres"] and c["apres"] not in texte and not any(
                    d["n"] > c["n"] and d["avant"] in c["apres"] for d in corrections):
                defauts.append("%s n° %s : correction absente du manuscrit" % (nom, c["n"]))
            elif c["avant"] in texte and c["avant"] not in c["apres"]:
                defauts.append("%s n° %s : texte d'avant encore présent" % (nom, c["n"]))
    return defauts


def bilan():
    r = registre()
    print("%d corrections dans %d fichiers" % (len(r), len({c["fichier"] for c in r})))
    for categorie, nombre in collections.Counter(c["categorie"] for c in r).most_common():
        print("  %-14s %d" % (categorie, nombre))
    for d in controle():
        print("  ÉCART : " + d)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if "--applique" in sys.argv:
        applique()
    elif "--bilan" in sys.argv:
        bilan()
    else:
        raise SystemExit(__doc__)
