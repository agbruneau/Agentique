"""Fusion rédactionnelle : volets « Mise en œuvre » réécrits contre l'exposé de leur chapitre.

Usage :
  python Master/compendium-master-fusion.py --prepare      extrait les volets d'origine
  python Master/compendium-master-fusion.py --controle ID  contrôle un volet réécrit
  python Master/compendium-master-fusion.py --bilan        contrôle tous les volets réécrits
  python Master/compendium-master-fusion.py --integre      intègre les volets au manuscrit

Dossiers : Master/fusion/origine/ID.md (volet avant réécriture, référence des contrôles)
et Master/fusion/reecrit/ID.md (volet réécrit). ID = chapitre-NN-volet-a|b|c.

Un volet réécrit ne doit rien inventer : le contrôle exige que le code, les figures,
les formules, les extraits, les encadrés de décision et de fil rouge soient conservés,
et que tout nombre, sigle ou nom propre du texte figure déjà dans le volet d'origine
ou dans l'exposé du chapitre.
"""
import collections
import glob
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
MANUSCRIT = os.path.join(ICI, "manuscrit")
ORIGINE = os.path.join(ICI, "fusion", "origine")
REECRIT = os.path.join(ICI, "fusion", "reecrit")

VOLET = re.compile(r"(?m)^(?=## Mise en œuvre — .* \{\.volet\}$)")
CODE = re.compile(r"(?ms)^(`{3,})[^\n]*\n.*?^\1[ \t]*$")
FORMULE_BLOC = re.compile(r"\$\$[^\n]+?\$\$")
FORMULE = re.compile(r"(?<![\\$])\$(?![\s$])[^$\n]*?(?<![\s\\])\$")
FIGURE = re.compile(r"(?m)^!\[.*\]\(figures/[^)\n]+\)$")
RENVOI = re.compile(r"(?:[Cc]hapitres?|[Ss]ections?)\s\d+(?:\.\d+)?"
                    r"(?:(?:\s?,\s|\set\s|\sà\s)\d+(?:\.\d+)?)*")
MINUSCULE = "a-zàâäçéèêëîïôöûùüÿœ"
# Passages ajoutés après la fusion, pour annoncer la partie X puis pour renvoyer aux
# compléments du 14 novembre 2026 : ils n'ont pas d'original dans l'édition G. Déclarés par
# ces deux repères, ils sortent du contrôle de conformité; tout le reste du texte y reste soumis.
AJOUT = re.compile(r"<!-- ajout partie X -->.*?<!-- fin ajout -->", re.S)


def lit(chemin):
    with open(chemin, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n")


def ecrit(chemin, texte):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write(texte.strip() + "\n")


def chapitres():
    """{numéro: (chemin, exposé, [volets])} pour les chapitres qui ont au moins un volet."""
    resultat = {}
    for chemin in sorted(glob.glob(os.path.join(MANUSCRIT, "chapitre-*.md"))):
        morceaux = VOLET.split(lit(chemin))
        if len(morceaux) > 1:
            numero = int(os.path.basename(chemin)[9:11])
            resultat[numero] = (chemin, morceaux[0], morceaux[1:])
    return resultat


def identifiant(numero, rang):
    return "chapitre-%02d-volet-%s" % (numero, "abc"[rang])


# Unités hors chapitres : textes de l'édition G sans exposé jumeau. La valeur donne le
# fichier du manuscrit et les textes d'appui dont un ajout peut provenir.
UNITES = {
    "ouverture": ("ouverture.md", ["chapitre-01-*.md", "chapitre-04-*.md", "chapitre-11-*.md"]),
    "annexe-F": ("annexe-F-*.md", []),
    "annexe-G": ("annexe-G-*.md", []),
    "annexe-H": ("annexe-H-*.md", ["annexe-A-*.md"]),
}


# Unités sorties du circuit de réécriture : le glossaire de l'annexe H a été fusionné dans
# l'annexe A, directement dans le manuscrit. Sa version réécrite reste comme trace.
FIGEES = {"annexe-H"}


def fichier(motif):
    trouves = glob.glob(os.path.join(MANUSCRIT, motif))
    if len(trouves) != 1:
        raise SystemExit("Fichier du manuscrit manquant ou en double : " + motif)
    return trouves[0]


def appui(ident):
    """Textes d'appui d'une unité : exposés des chapitres cités, ou annexe A."""
    return "\n".join(VOLET.split(lit(fichier(motif)))[0] for motif in UNITES[ident][1])


def prose(md):
    """Texte courant : sans code, formules, figures ni renvois de chapitre ou de section."""
    md = CODE.sub(" ", md)
    md = FIGURE.sub(" ", md)
    md = FORMULE_BLOC.sub(" ", md)
    md = FORMULE.sub(" ", md)
    md = re.sub(r"`[^`\n]*`", " ", md)
    return RENVOI.sub(" ", md)


def mots(md):
    return len(re.findall(r"[0-9A-Za-zÀ-ÖØ-öø-ÿŒœ]+", md))


def encadres(md, erreurs):
    """Compte les encadrés par genre et vérifie que leurs balises sont appariées."""
    compte = collections.Counter()
    etat = None
    for n, ligne in enumerate(md.split("\n"), 1):
        if not ligne.startswith(":::"):
            continue
        m = re.match(r":::: \{\.encadre \.(\w+)\}$", ligne)
        if m and etat is None:
            compte[m.group(1)] += 1
            etat = "ouvert"
        elif ligne == "::: {.encadre-titre}" and etat == "ouvert":
            etat = "titre"
        elif ligne == ":::" and etat == "titre":
            etat = "corps"
        elif ligne == "::::" and etat == "corps":
            etat = None
        else:
            erreurs.append("ligne %d : balise d'encadré inattendue « %s »" % (n, ligne))
            return compte
    if etat is not None:
        erreurs.append("encadré non fermé en fin de volet")
    return compte


def controle(origine, reecrit, expose, volet=True):
    """Liste des écarts d'un texte réécrit; vide s'il est conforme.

    volet=False pour une unité hors chapitre (ouverture, annexe) : un titre de niveau 1,
    et aucune ligne de tableau ni, dans une annexe, aucune entrée de liste ne disparaît.
    """
    e = []
    reecrit = AJOUT.sub("", reecrit)
    if reecrit.split("\n", 1)[0] != origine.split("\n", 1)[0]:
        e.append("la première ligne (titre) doit rester identique")
    if volet:
        if len(re.findall(r"(?m)^## Mise en œuvre", reecrit)) != 1 or re.search(r"(?m)^# ", CODE.sub("", reecrit)):
            e.append("un seul titre de volet, aucun titre de niveau 1")
    else:
        if len(re.findall(r"(?m)^# ", CODE.sub("", reecrit))) != 1:
            e.append("un seul titre de niveau 1")
        compte = lambda motif, md: len(re.findall(motif, CODE.sub("", md)))
        if compte(r"(?m)^\|", reecrit) != compte(r"(?m)^\|", origine):
            e.append("tableaux : %d lignes au lieu de %d, aucune ne doit disparaître ni s'ajouter"
                     % (compte(r"(?m)^\|", reecrit), compte(r"(?m)^\|", origine)))
        if origine.startswith("# Annexe") and compte(r"(?m)^- ", reecrit) != compte(r"(?m)^- ", origine):
            e.append("listes : %d entrées au lieu de %d, aucune ne doit disparaître ni s'ajouter"
                     % (compte(r"(?m)^- ", reecrit), compte(r"(?m)^- ", origine)))

    if [m.group(0) for m in CODE.finditer(reecrit)] != [m.group(0) for m in CODE.finditer(origine)]:
        e.append("les blocs de code doivent tous être repris à l'identique, dans le même ordre")
    if FIGURE.findall(reecrit) != FIGURE.findall(origine):
        e.append("les lignes de figure doivent être reprises à l'identique, dans le même ordre")
    sans_code_o, sans_code_r = CODE.sub(" ", origine), CODE.sub(" ", reecrit)
    for formule in FORMULE_BLOC.findall(sans_code_r):
        if formule not in origine:
            e.append("formule modifiée ou nouvelle : %s" % formule[:70])
    for formule in FORMULE.findall(FORMULE_BLOC.sub(" ", sans_code_r)):
        if formule not in origine:
            e.append("formule en ligne modifiée ou nouvelle : %s" % formule[:70])
    extrait = r"(?m)^#### Extrait (\d+\.\d+) "
    if re.findall(extrait, reecrit) != re.findall(extrait, origine):
        e.append("les titres « #### Extrait N.k — … » doivent tous rester, mêmes numéros, même ordre")

    avant, apres = encadres(origine, []), encadres(reecrit, e)
    for genre in ("adr", "filrouge"):
        if apres[genre] != avant[genre]:
            e.append("encadrés « %s » : %d au lieu de %d" % (genre, apres[genre], avant[genre]))
    for genre in apres:
        if apres[genre] > avant[genre]:
            e.append("encadré « %s » ajouté" % genre)
    adr = r"(?m)^\*\*ADR-\d+ — .*\*\*$"
    if re.findall(adr, reecrit) != re.findall(adr, origine):
        e.append("le titre de l'encadré ADR doit rester identique")

    # Sections : même premier numéro, numérotation consécutive, sections finales conservées.
    numeros_o = re.findall(r"(?m)^## (\d+|[A-H])\.(\d+) ", origine)
    numeros_r = re.findall(r"(?m)^## (\d+|[A-H])\.(\d+) ", reecrit)
    if not numeros_o:
        pass
    elif not numeros_r or numeros_r[0] != numeros_o[0]:
        e.append("la première section doit garder le numéro %s.%s" % numeros_o[0])
    elif [int(k) for _, k in numeros_r] != list(range(int(numeros_r[0][1]),
                                                      int(numeros_r[0][1]) + len(numeros_r))):
        e.append("les sections « ## N.k » doivent se suivre sans trou ni doublon")
    if len(numeros_r) > len(numeros_o):
        e.append("plus de sections numérotées que dans l'original")
    for repere in ("fil rouge", "Décision d’architecture"):
        if re.search(r"(?m)^## .*%s" % repere, origine) and not re.search(r"(?m)^## .*%s" % repere, reecrit):
            e.append("la section dont le titre contient « %s » doit rester" % repere)
    liste = r"(?ms)^### Liste de contrôle de mise en production\n(.*?)(?=^#|\Z)"
    if re.search(liste, origine):
        points = lambda md: len(re.findall(r"(?m)^\d+\.\s", re.search(liste, md).group(1)))
        if not re.search(liste, reecrit):
            e.append("le titre « ### Liste de contrôle de mise en production » doit rester")
        elif points(reecrit) != points(origine):
            e.append("liste de contrôle : %d points au lieu de %d" % (points(reecrit), points(origine)))
    if re.search(r"(?m)^#{5,} ", sans_code_r):
        e.append("pas de titre au-delà du niveau 4")

    # Rien d'inventé : nombres, sigles et noms propres viennent de l'original ou de l'exposé.
    source = origine + "\n" + expose
    connus = set(re.findall(r"\d+(?:[.,]\d+)*", prose(source)))
    nouveaux = sorted(set(re.findall(r"\d+(?:[.,]\d+)*", prose(reecrit))) - connus)
    if nouveaux:
        e.append("nombres absents de l'original et de l'exposé : %s" % ", ".join(nouveaux[:15]))
    sigles = set(re.findall(r"\b[A-Z][A-Za-z0-9]*(?:[-/.][A-Za-z0-9]+)*", prose(reecrit)))
    sigles = sorted(s for s in sigles if re.search(r".[A-Z0-9]", s) and s not in source)
    if sigles:
        e.append("sigles ou noms absents de l'original et de l'exposé : %s" % ", ".join(sigles[:15]))
    propres = set(re.findall(r"(?<=[%s,;] )[A-ZÀ-Ý][a-zà-ÿ]{3,}" % MINUSCULE, prose(reecrit)))
    propres = sorted(p for p in propres if p not in source)
    if propres:
        e.append("noms propres absents de l'original et de l'exposé : %s" % ", ".join(propres[:15]))
    adresses = set(re.findall(r"https?://\S+", sans_code_r)) - set(re.findall(r"https?://\S+", source))
    if adresses:
        e.append("adresse web ajoutée : %s" % ", ".join(sorted(adresses)[:3]))

    rapport = mots(reecrit) / mots(origine)
    if rapport > 1.10:      # l'alignement sur l'exposé ajoute des phrases de renvoi
        e.append("le volet réécrit est plus long que l'original (%.0f %%)" % (100 * rapport))
    if rapport < 0.45:
        e.append("le volet réécrit ne garde que %.0f %% de l'original : trop coupé" % (100 * rapport))
    return e


def prepare():
    # Une fois des volets réécrits, la référence ne doit plus bouger : le manuscrit
    # contient alors le texte réécrit, pas l'original.
    for chemin in glob.glob(os.path.join(REECRIT, "*.md")):
        reference = os.path.join(ORIGINE, os.path.basename(chemin))
        if not os.path.isfile(reference) or lit(reference) != lit(chemin):
            raise SystemExit("Des volets réécrits existent déjà : --prepare écraserait leur référence.")
    travail = []
    for numero, (chemin, expose, volets) in chapitres().items():
        for rang, volet in enumerate(volets):
            ident = identifiant(numero, rang)
            ecrit(os.path.join(ORIGINE, ident + ".md"), volet)
            travail.append(dict(
                id=ident, chapitre=numero,
                titre=volet.split("\n", 1)[0][len("## Mise en œuvre — "):-len(" {.volet}")],
                fichier_chapitre="Master/manuscrit/" + os.path.basename(chemin),
                origine="Master/fusion/origine/%s.md" % ident,
                sortie="Master/fusion/reecrit/%s.md" % ident,
                autres_volets=len(volets) - 1, mots=mots(volet)))
    print(json.dumps(travail, ensure_ascii=False))


def examine(ident, cache):
    volet = ident not in UNITES
    expose = cache[int(ident[9:11])][1] if volet else appui(ident)
    origine = lit(os.path.join(ORIGINE, ident + ".md"))
    chemin = os.path.join(REECRIT, ident + ".md")
    if not os.path.isfile(chemin):
        return None, ["fichier absent : Master/fusion/reecrit/%s.md" % ident], origine
    reecrit = lit(chemin)
    return reecrit, controle(origine, reecrit, expose, volet), origine


def prepare_unites():
    """Copie l'ouverture et les annexes F à H du manuscrit comme référence de leur réécriture."""
    for ident, (motif, _) in UNITES.items():
        reference = os.path.join(ORIGINE, ident + ".md")
        if os.path.isfile(reference):
            raise SystemExit("Référence déjà extraite : " + reference)
        ecrit(reference, lit(fichier(motif)))
        print("%s : %d mots" % (ident, mots(lit(reference))))


def bilan(integre):
    cache = chapitres()
    idents = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(ORIGINE, "*.md")))
    idents = [ident for ident in idents if ident not in FIGEES]
    defauts = 0
    avant = apres = 0
    textes = {}
    for ident in idents:
        reecrit, erreurs, origine = examine(ident, cache)
        if erreurs:
            defauts += 1
            print("%s : %d écart(s)" % (ident, len(erreurs)))
            for erreur in erreurs:
                print("    " + erreur)
        else:
            avant += mots(origine)
            apres += mots(reecrit)
            textes[ident] = reecrit
    print("volets conformes : %d sur %d; mots : %d -> %d (%.0f %%)"
          % (len(textes), len(idents), avant, apres, 100 * apres / avant if avant else 0))
    if not integre:
        return defauts
    if defauts:
        raise SystemExit("Intégration refusée : %d volet(s) non conforme(s)." % defauts)
    for numero, (chemin, expose, volets) in cache.items():
        dernier = len(re.findall(r"(?m)^## %d\.\d+ " % numero, expose))
        neufs = []
        for rang in range(len(volets)):
            volet = textes[identifiant(numero, rang)].strip()

            def renumerote(m):
                nonlocal dernier
                dernier += 1
                return "## %d.%d " % (numero, dernier)

            neufs.append(re.sub(r"(?m)^## %d\.\d+ " % numero, renumerote, volet))
        ecrit(chemin, "\n\n".join([expose.strip()] + neufs))
    unites = [ident for ident in UNITES if ident in textes]
    for ident in unites:
        ecrit(fichier(UNITES[ident][0]), textes[ident])
    print("manuscrit mis à jour : %d chapitres, %d unités hors chapitre" % (len(cache), len(unites)))
    return 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if "--prepare-unites" in sys.argv:
        prepare_unites()
    elif "--prepare" in sys.argv:
        prepare()
    elif "--controle" in sys.argv:
        ident = sys.argv[sys.argv.index("--controle") + 1]
        reecrit, erreurs, origine = examine(ident, chapitres())
        if erreurs:
            print("%s : %d écart(s) à corriger" % (ident, len(erreurs)))
            for erreur in erreurs:
                print("  - " + erreur)
            raise SystemExit(1)
        print("%s : conforme (%d mots -> %d mots, %.0f %%)"
              % (ident, mots(origine), mots(reecrit), 100 * mots(reecrit) / mots(origine)))
    elif "--autotest" in sys.argv:
        # Un volet d'origine, comparé à lui-même, doit être conforme.
        cache = chapitres()
        for chemin in sorted(glob.glob(os.path.join(ORIGINE, "*.md"))):
            origine = lit(chemin)
            ident = os.path.basename(chemin)[:-3]
            if ident in UNITES:
                erreurs = controle(origine, origine, appui(ident), False)
            else:
                erreurs = controle(origine, origine, cache[int(ident[9:11])][1])
            if erreurs:
                print(os.path.basename(chemin), erreurs)
        print("autotest terminé")
    elif "--bilan" in sys.argv:
        raise SystemExit(1 if bilan(False) else 0)
    elif "--integre" in sys.argv:
        bilan(True)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
