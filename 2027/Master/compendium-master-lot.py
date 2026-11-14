"""Applique un lot de modifications au manuscrit et l'inscrit au registre des corrections.

Usage :
  python Master/compendium-master-lot.py Master/lots/<lot>.json --essai   vérifie, n'écrit rien
  python Master/compendium-master-lot.py Master/lots/<lot>.json           applique le lot

Un lot est un fichier JSON :
  {"id": "V1-ch47", "origine": "plan 2027, lot V1-ch47", "categorie": "coherence",
   "remplacements": [{"fichier": "chapitre-47-….md", "avant": "…", "apres": "…", "motif": "…"}]}

C'est la seule voie d'écriture dans Master/manuscrit/ : chaque remplacement est exact, se
fait à un seul endroit du fichier et devient une entrée de Master/audit/corrections.json,
ce qui garde le manuscrit conforme aux contrôles de compendium-master-verifie.py.

Règles vérifiées avant toute écriture; une seule infraction annule le lot entier :
  - catégorie connue, fichier présent dans le manuscrit, motif non vide;
  - « avant » non vide, différent de « apres » et absent de « apres » (sinon une
    réapplication doublerait le texte);
  - « avant » présent une fois exactement dans le fichier, compte tenu des remplacements
    précédents du même lot;
  - « avant » ne déborde pas d'une entrée antérieure du registre : s'il en entame le texte,
    il doit y tenir tout entier;
  - dans un volet « Mise en œuvre », l'ouverture ou les annexes F à H, le passage doit se
    trouver aussi, une fois, dans la copie réécrite (Master/fusion/reecrit/), qui est
    modifiée du même geste.
Un lot déjà appliqué est reconnu et laissé tel quel. Les fins de ligne sont conservées.

Après application : recomposer (compendium-master-assemble.py), puis vérifier
(compendium-master-verifie.py). Si la vérification échoue, annuler par git et corriger le lot.
"""
import glob
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
MANUSCRIT = os.path.join(ICI, "manuscrit")
REECRIT = os.path.join(ICI, "fusion", "reecrit")
REGISTRE = os.path.join(ICI, "audit", "corrections.json")
CATEGORIES = ("coherence", "terminologie", "residu", "factuel", "langue", "renvoi", "temporel",
              "structure", "enrichissement", "harmonisation")
VOLET = re.compile(r"(?m)^## Mise en œuvre — .*$")


def lit(chemin):
    with open(chemin, encoding="utf-8", newline="") as f:
        brut = f.read()
    return brut.replace("\r\n", "\n"), "\r\n" in brut


def ecrit(chemin, texte, crlf):
    with open(chemin, "w", encoding="utf-8", newline="") as f:
        f.write(texte.replace("\n", "\r\n") if crlf else texte)


def copies(nom):
    """Copies réécrites qui doivent suivre le fichier du manuscrit."""
    if nom == "ouverture.md":
        return [os.path.join(REECRIT, "ouverture.md")]
    if nom.startswith("annexe-"):
        return glob.glob(os.path.join(REECRIT, nom[:8] + ".md"))
    return sorted(glob.glob(os.path.join(REECRIT, nom[:11] + "-volet-*.md")))


def suivi(nom, texte, avant):
    """Vrai si le passage relève d'un texte réécrit, dont la copie doit être modifiée aussi."""
    if nom == "ouverture.md" or re.match(r"annexe-[FGH]-", nom):
        return True
    m = VOLET.search(texte)
    return bool(m) and texte.find(avant) > m.start()


def main():
    arguments = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(arguments) != 1:
        raise SystemExit(__doc__)
    essai = "--essai" in sys.argv
    with open(arguments[0], encoding="utf-8") as f:
        lot = json.load(f)
    erreurs = []
    for cle in ("id", "origine", "categorie", "remplacements"):
        if not lot.get(cle):
            erreurs.append("champ « %s » absent du lot" % cle)
    if lot.get("categorie") not in CATEGORIES:
        erreurs.append("catégorie inconnue : %s (admises : %s)" % (lot.get("categorie"), ", ".join(CATEGORIES)))
    if erreurs:
        raise SystemExit("Lot refusé :\n  " + "\n  ".join(erreurs))

    brut, crlf_registre = lit(REGISTRE)
    registre = json.loads(brut)
    suivant = max(c["n"] for c in registre) + 1
    textes, autres = {}, {}
    faits = deja = 0
    for rang, r in enumerate(lot["remplacements"], 1):
        ou = "remplacement %d" % rang
        fichier, avant, apres, motif = (r.get(k) for k in ("fichier", "avant", "apres", "motif"))
        chemin = os.path.join(MANUSCRIT, fichier or "")
        if not fichier or not os.path.isfile(chemin):
            erreurs.append("%s : fichier absent du manuscrit : %s" % (ou, fichier))
            continue
        if not avant or apres is None or not motif:
            erreurs.append("%s : « avant », « apres » et « motif » sont obligatoires" % ou)
            continue
        if avant == apres or avant in apres:
            erreurs.append("%s : « avant » ne doit pas figurer dans « apres » (élargir l'ancre)" % ou)
            continue
        if fichier not in textes:
            textes[fichier] = lit(chemin)
            autres[fichier] = {c: lit(c) for c in copies(fichier)}
        texte, crlf = textes[fichier]
        n = texte.count(avant)
        if n == 0 and apres in texte:
            deja += 1
        elif n == 1:
            # Une entrée antérieure dont le texte disparaît doit contenir l'ancre : c'est ce
            # que le contrôle du registre exige pour la tenir encore pour appliquée.
            apres_coup = texte.replace(avant, apres)
            debords = [c["n"] for c in registre if c["fichier"] == fichier and c["apres"]
                       and c["apres"] in texte and c["apres"] not in apres_coup and avant not in c["apres"]]
            if debords:
                erreurs.append("%s : l'ancre « %s » déborde de l'entrée n° %s du registre (la resserrer "
                               "pour qu'elle tienne dans le texte de cette entrée)"
                               % (ou, avant[:50], ", ".join(map(str, debords))))
                continue
            # Le texte nouveau ne doit pas ramener un passage qu'une entrée antérieure a remplacé.
            retours = [c["n"] for c in registre if c["fichier"] == fichier and c["avant"] not in texte
                       and c["avant"] in apres_coup and c["avant"] not in c["apres"]]
            if retours:
                erreurs.append("%s : le remplacement ramène le texte que l'entrée n° %s du registre a "
                               "remplacé (reformuler)" % (ou, ", ".join(map(str, retours))))
                continue
            if suivi(fichier, texte, avant):
                cibles = [c for c, (t, _) in autres[fichier].items() if t.count(avant) == 1]
                if len(cibles) != 1:
                    erreurs.append("%s : passage d'un texte réécrit introuvable dans sa copie "
                                   "(Master/fusion/reecrit/) : %s" % (ou, avant[:60]))
                    continue
                t, k = autres[fichier][cibles[0]]
                autres[fichier][cibles[0]] = (t.replace(avant, apres), k)
            textes[fichier] = (texte.replace(avant, apres), crlf)
            faits += 1
        else:
            erreurs.append("%s : « %s » trouvé %d fois dans %s" % (ou, avant[:60], n, fichier))
            continue
        if not any(c["fichier"] == fichier and c["avant"] == avant and c["apres"] == apres for c in registre):
            registre.append({"n": suivant, "fichier": fichier, "avant": avant, "apres": apres,
                             "categorie": lot["categorie"], "motif": motif, "origine": lot["origine"]})
            suivant += 1
    if erreurs:
        raise SystemExit("Lot %s refusé, rien n'a été écrit :\n  %s" % (lot["id"], "\n  ".join(erreurs)))
    print("lot %s : %d remplacements à faire, %d déjà en place, registre à %d entrées%s"
          % (lot["id"], faits, deja, len(registre), " (essai, rien d'écrit)" if essai else ""))
    if essai or not faits:
        return
    for fichier, (texte, crlf) in textes.items():
        ecrit(os.path.join(MANUSCRIT, fichier), texte, crlf)
        for c, (t, k) in autres[fichier].items():
            ecrit(c, t, k)
    ecrit(REGISTRE, json.dumps(registre, ensure_ascii=False, indent=1), crlf_registre)
    print("écrit. À faire : compendium-master-assemble.py, puis compendium-master-verifie.py")


if __name__ == "__main__":
    main()
