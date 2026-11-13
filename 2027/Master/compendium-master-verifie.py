"""Vérifie le manuscrit unifié et CompendiumMaster.pdf.

Usage : python Master/compendium-master-verifie.py

Contrôles du manuscrit : texte de l'édition C repris intégralement (hors bandeau),
volume de texte de l'édition G conservé, numérotation des sections et des extraits,
renvois vers des chapitres existants, aucun reste de l'ancienne structure, sources de
la partie X (chapitres 48 à 50, écrits directement dans le manuscrit) citées et listées,
corrections de l'audit de publication (Master/audit/corrections.json) toutes appliquées.
Contrôles du PDF : signets des parties, chapitres, volets et annexes, figures,
aucun balisage resté apparent. Code de sortie 1 si un contrôle échoue.
"""
import glob
import html
import importlib.util
import os
import re
import sys

import pymupdf

ICI = os.path.dirname(os.path.abspath(__file__))


def module(nom):
    spec = importlib.util.spec_from_file_location(nom, os.path.join(ICI, nom + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


man = module("compendium-master-manuscrit")
asm = module("compendium-master-assemble")
fus = module("compendium-master-fusion")
aud = module("compendium-master-audit")
echecs = []
DERNIER = 50                 # dernier chapitre du volume
PARTIE_X = range(48, 51)     # chapitres sans édition d'origine : écrits dans le manuscrit


def controle(nom, defauts, detail=""):
    nombre = len(defauts) if isinstance(defauts, (list, set)) else int(defauts)
    print("%-58s %s %s" % (nom, "OK" if not nombre else "ÉCHEC (%d)" % nombre, detail))
    if nombre:
        echecs.append(nom)
        if isinstance(defauts, (list, set)):
            for d in list(defauts)[:6]:
                print("    " + str(d)[:150])


def mots(texte):
    return re.findall(r"[0-9A-Za-zÀ-ÖØ-öø-ÿŒœ]+", texte)


def texte_nu(md):
    """Markdown -> mots du texte courant (ni balisage, ni chemins de figures)."""
    md = re.sub(r"\]\([^)\n]*\)|<!--.*?-->|\{\.[^}]*\}", " ", md)
    return mots(md)


def main():
    fichiers = {os.path.basename(f): open(f, encoding="utf-8").read()
                for f in sorted(glob.glob(os.path.join(man.MANUSCRIT, "*.md")))}
    controle("manuscrit : 59 fichiers", int(len(fichiers) != 59), "(%d)" % len(fichiers))

    # Édition C : chaque chapitre et annexe est repris mot pour mot, bandeau excepté.
    defauts = []
    total_c = 0
    for motif in ["compendium-2027-chapitre-%02d-*.md" % n for n in range(1, 48)] + \
                 ["compendium-2027-annexe-%s-*.md" % x for x in "ABCDE"]:
        nom, source = man.fichier_c(motif)
        attendu = man.epure_c(source, nom).strip()
        retire = len(mots(source)) - len(mots(attendu))
        # Les corrections de l'audit de publication sont déclarées au registre : on les
        # applique au texte d'origine avant de comparer.
        attendu = aud.corrige(re.sub(r"^compendium-2027-", "", nom), attendu)
        repris = fichiers[re.sub(r"^compendium-2027-", "", nom)]
        # Les schémas ajoutés aux exposés (figures fig-NN-eK) ne comptent pas comme du texte.
        repris = re.sub(r"(?m)^!\[[^\n]*\]\(figures/fig-\d\d-e\d+\.svg\)\n\n", "", repris)
        total_c += len(mots(attendu))
        if "annexe-A" in nom:
            # Le glossaire de l'annexe H y a été fusionné : des lignes s'ajoutent et une
            # cellule peut être complétée en fin, mais aucune ligne d'origine ne disparaît.
            lignes = iter(repris.split("\n"))
            for ligne in (x for x in attendu.split("\n") if x.strip()):
                debut = ligne[:-2] if ligne.endswith(" |") else ligne
                if not any(x.startswith(debut) for x in lignes):
                    defauts.append("%s : ligne d'origine absente ou déplacée : %s" % (nom, ligne[:60]))
                    break
        elif not repris.startswith(attendu):
            defauts.append(nom)
        if not 0 < retire < 60:
            defauts.append("%s : %d mots retirés du bandeau" % (nom, retire))
    controle("édition C reprise mot pour mot (hors bandeau)", defauts, "(%d mots)" % total_c)

    # Édition G : volume conservé unité par unité (les titres et renvois changent, pas le fond).
    volets = {}
    for nom, texte in fichiers.items():
        if nom.startswith("chapitre-"):
            n = int(nom[9:11])
            volets[n] = re.split(r"(?m)^## Mise en œuvre — .* \{\.volet\}$", texte)[1:]
    defauts = []
    total_g = 0
    rang = {}
    for cle, titre, bloc in man.unites_g():
        if cle is None:
            continue
        # Une formule compte une fois : son écriture TeX, comme dans le manuscrit.
        bloc = re.sub(r'(?s)<math.*?<annotation[^>]*>(.*?)</annotation>.*?</math>', r" \1 ", bloc)
        source = mots(html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r'src="data:[^"]*"', "", bloc))))
        if cle == "ouverture" or isinstance(cle, str):
            unite = "ouverture" if cle == "ouverture" else "annexe-" + man.ANNEXES_G[cle][0]
            if os.path.isfile(os.path.join(fus.REECRIT, unite + ".md")):
                continue          # unité réécrite : contrôlée plus bas contre son original
        if cle == "ouverture":
            repris = fichiers["ouverture.md"]
        elif isinstance(cle, str):
            lettre = man.ANNEXES_G[cle][0]
            repris = next(t for f, t in fichiers.items() if f.startswith("annexe-%s-" % lettre))
        else:
            hote = man.HOTE[cle]
            repris = volets[hote][rang.get(hote, 0)]
            ident = fus.identifiant(hote, rang.get(hote, 0))
            rang[hote] = rang.get(hote, 0) + 1
            if os.path.isfile(os.path.join(fus.REECRIT, ident + ".md")):
                continue          # volet réécrit : contrôlé plus bas contre son original
        ecart = (len(texte_nu(repris)) - len(source)) / len(source)
        total_g += len(source)
        if abs(ecart) > 0.03:
            defauts.append("%s : écart de %.1f %%" % (titre[:50], 100 * ecart))
    controle("édition G non réécrite : volume conservé (±3 % par unité)", defauts,
             "(%d mots)" % total_g)

    # Volets réécrits : conformes à leur original (rien d'inventé, code et figures intacts)
    # et repris tels quels dans le manuscrit, à la numérotation des sections près.
    defauts = []
    avant = apres = nombre = 0
    sans_numero = lambda md: re.sub(r"(?m)^## \d+\.\d+ ", "## ", md).strip()
    for numero, (chemin, expose, textes) in fus.chapitres().items():
        for position, volet in enumerate(textes):
            ident = fus.identifiant(numero, position)
            sortie = os.path.join(fus.REECRIT, ident + ".md")
            if not os.path.isfile(sortie):
                continue
            origine, reecrit = fus.lit(os.path.join(fus.ORIGINE, ident + ".md")), fus.lit(sortie)
            hote = os.path.basename(chemin)
            origine = aud.corrige(hote, origine)
            defauts.extend("%s : %s" % (ident, e) for e in fus.controle(
                origine, reecrit, expose + "\n" + aud.ajouts(hote)))
            if sans_numero(volet) != sans_numero(reecrit):
                defauts.append("%s : le manuscrit ne reprend pas le volet réécrit" % ident)
            nombre += 1
            avant += fus.mots(origine)
            apres += fus.mots(reecrit)
    controle("volets réécrits : conformes et intégrés (%d sur 31)" % nombre, defauts,
             "(%d -> %d mots)" % (avant, apres))

    # Ouverture et annexes F à H réécrites : mêmes garanties, tableaux et listes complets.
    defauts = []
    avant = apres = nombre = 0
    for ident, (motif, _) in fus.UNITES.items():
        sortie = os.path.join(fus.REECRIT, ident + ".md")
        if not os.path.isfile(sortie) or ident in fus.FIGEES:
            continue
        origine, reecrit = fus.lit(os.path.join(fus.ORIGINE, ident + ".md")), fus.lit(sortie)
        unite = os.path.basename(fus.fichier(motif))
        origine = aud.corrige(unite, origine)
        defauts.extend("%s : %s" % (ident, e) for e in fus.controle(
            origine, reecrit, fus.appui(ident) + "\n" + aud.ajouts(unite), False))
        if fus.lit(fus.fichier(motif)).strip() != reecrit.strip():
            defauts.append("%s : le manuscrit ne reprend pas le texte réécrit" % ident)
        nombre += 1
        avant += fus.mots(origine)
        apres += fus.mots(reecrit)
    ajouts = len(fus.AJOUT.findall(fichiers["ouverture.md"]))
    reperes = fichiers["ouverture.md"].count("<!-- ajout partie X -->") \
        + fichiers["ouverture.md"].count("<!-- fin ajout -->")
    if reperes != 2 * ajouts:
        defauts.append("ouverture : repères d'ajout non appariés")
    controle("ouverture et annexes F et G réécrites (%d sur 3)" % nombre, defauts,
             "(%d -> %d mots; %d passages déclarés pour la partie X)" % (avant, apres, ajouts))

    # Glossaire unique : celui de l'annexe H est fusionné dans l'annexe A; l'annexe H
    # ne garde que l'index des standards, tableau inchangé.
    defauts = []
    annexe_h = fus.lit(fus.fichier("annexe-H-*.md"))
    ancienne = fus.lit(os.path.join(fus.REECRIT, "annexe-H.md"))
    tableau = lambda md: [x for x in md.split("\n") if x.startswith("|")]
    if tableau(annexe_h) != tableau(ancienne):
        defauts.append("le tableau d'index de l'annexe H a changé")
    if re.search(r"(?m)^- ", annexe_h) or len(re.findall(r"(?m)^## ", annexe_h)) != 1:
        defauts.append("l'annexe H doit n'avoir qu'une section, sans entrée de glossaire")
    annexe_a = fichiers["annexe-A-glossaire.md"]
    source = fus.lit(os.path.join(fus.ORIGINE, "annexe-H.md")) + ancienne + man.fichier_c(
        "compendium-2027-annexe-A-*.md")[1] + "".join(
        t for f, t in fichiers.items() if f.startswith("chapitre-"))
    nouveaux = set(re.findall(r"\b[A-Z][A-Za-z0-9]*(?:[-/.][A-Za-z0-9]+)*", annexe_a))
    nouveaux = sorted(s for s in nouveaux if re.search(r".[A-Z0-9]", s) and s not in source)
    if nouveaux:
        defauts.append("sigles de l'annexe A absents des deux glossaires : %s" % ", ".join(nouveaux[:10]))
    ajoutees = len(tableau(annexe_a)) - len(tableau(man.fichier_c("compendium-2027-annexe-A-*.md")[1]))
    controle("glossaire unique : annexe H fusionnée dans l'annexe A", defauts,
             "(%d lignes ajoutées)" % ajoutees)

    # Numérotation : sections consécutives par chapitre, extraits sans doublon.
    defauts = []
    for nom, texte in fichiers.items():
        if not nom.startswith("chapitre-"):
            continue
        n = int(nom[9:11])
        sections = [int(k) for k in re.findall(r"(?m)^## %d\.(\d+) " % n, texte)]
        if sections != list(range(1, len(sections) + 1)):
            defauts.append("%s : sections %s" % (nom, sections))
        autres = re.findall(r"(?m)^## (\d+)\.\d+ ", texte)
        if any(int(a) != n for a in autres):
            defauts.append("%s : section d'un autre chapitre" % nom)
        extraits = re.findall(r"(?m)^#### Extrait (\d+)\.(\d+) ", texte)
        if len(set(extraits)) != len(extraits) or any(int(a) != n for a, _ in extraits):
            defauts.append("%s : extraits %s" % (nom, extraits))
    controle("sections consécutives, extraits uniques", defauts)

    # Renvois : chapitres 1 à 50; plus rien de l'ancienne structure de l'édition G.
    defauts = []
    restes = []
    for nom, texte in fichiers.items():
        corps = re.sub(r"(?s)```.*?```", " ", texte)
        for m in re.finditer(r"[Cc]hapitres? (\d+)", corps):
            if not 1 <= int(m.group(1)) <= DERNIER:
                defauts.append("%s : %s" % (nom, m.group(0)))
        g = "".join(re.split(r"(?m)^## Mise en œuvre — .*$", corps)[1:]) \
            if nom.startswith("chapitre-") else (corps if nom[:8] in ("ouvertur", "annexe-F", "annexe-G", "annexe-H") else "")
        for motif in (r"612 pages", r"31 chapitres", r"dix parties", r"\bParties? X\b",
                      r"[Cc]ompendium 2027", r"compendium-box", r"Synthèse exécutive — Chapitre"):
            restes.extend("%s : %s" % (nom, x) for x in re.findall(motif, g))
    controle("renvois vers des chapitres existants", defauts)
    controle("aucun reste de l'ancienne structure de l'édition G", restes)

    # Partie X : même gabarit que les exposés, et correspondance entre appels et sources.
    defauts = []
    nb_sources = 0
    for n in PARTIE_X:
        nom, texte = next((f, t) for f, t in fichiers.items() if f.startswith("chapitre-%02d-" % n))
        for titre in ("Grille de décision", "Points à retenir", "Sources", "Limites de ce chapitre"):
            if len(re.findall(r"(?m)^## %s$" % titre, texte)) != 1:
                defauts.append("%s : section « %s » absente ou en double" % (nom, titre))
        if not re.search(r"(?m)^\*Question directrice : .*\*$", texte) or "{.volet}" in texte:
            defauts.append("%s : question directrice absente, ou volet inattendu" % nom)
        corps, _, fin = texte.partition("\n## Sources\n")
        liste, _, limites = fin.partition("\n## Limites de ce chapitre\n")
        listees = [int(k) for k in re.findall(r"(?m)^(\d+)\. \[", liste)]
        citees = {int(k) for k in re.findall(r"\[(\d+)\]", corps + limites)}
        nb_sources += len(listees)
        if listees != list(range(1, len(listees) + 1)):
            defauts.append("%s : sources non numérotées de 1 à %d" % (nom, len(listees)))
        if citees - set(listees):
            defauts.append("%s : appels sans source : %s" % (nom, sorted(citees - set(listees))))
        if set(listees) - citees:
            defauts.append("%s : sources jamais citées : %s" % (nom, sorted(set(listees) - citees)))
        if re.search(r"\[@|\{\{", texte):
            defauts.append("%s : jeton de rédaction non résolu" % nom)
        # Deux signes de dollar sur une ligne peuvent être lus comme une formule.
        formules = re.findall(r"\$[^\s$|][^$\n]*[^\s\\]\$(?!\d)", texte)
        if formules:
            defauts.append("%s : montants lus comme une formule : %s" % (nom, formules[0][:40]))
    controle("partie X : gabarit des exposés, appels et sources appariés", defauts,
             "(%d sources)" % nb_sources)

    # Audit de publication : chaque correction du registre est en place dans le manuscrit.
    controle("audit : corrections du registre appliquées", aud.controle(),
             "(%d corrections)" % len(aud.registre()))

    # PDF.
    pdf = pymupdf.open(asm.SORTIE)
    plan = pdf.get_toc()
    # L'ouverture précède la première partie : ses signets remontent d'un niveau.
    parties = [t for niv, t, _ in plan if niv == 1 and re.match(r"Partie [IVX]+ —|Annexes$", t)]
    unites = [t for niv, t, _ in plan
              if niv <= 2 and re.match(r"(Ouverture|Chapitre \d+|Annexe [A-H]) —", t)]
    nb_volets = sum(1 for niv, t, _ in plan if niv == 3 and t.startswith("Mise en œuvre — "))
    controle("PDF : 10 parties et les annexes", int(len(parties) != 11), "(%d)" % len(parties))
    attendus = ["Ouverture "] + ["Chapitre %d " % n for n in range(1, DERNIER + 1)] + \
               ["Annexe %s " % x for x in "ABCDEFGH"]
    controle("PDF : ouverture, %d chapitres, 8 annexes, dans l'ordre" % DERNIER,
             [a for a, t in zip(attendus, unites) if not t.startswith(a)]
             or int(len(unites) != len(attendus)), "(%d)" % len(unites))
    controle("PDF : 31 volets « Mise en œuvre »", int(nb_volets != 31), "(%d)" % nb_volets)
    pages = [p for niv, t, p in plan]
    controle("PDF : signets en ordre de page", int(pages != sorted(pages)), "(%d)" % len(plan))
    texte = "\n".join(page.get_text() for page in pdf)
    figures = len(set(re.findall(r"(?m)^Fig\.\s+(\d+)\.\s+–", texte)))
    attendues = sum(len(re.findall(r"(?m)^!\[.*\]\(figures/[^)]+\.svg\)$", t))
                    for t in fichiers.values())
    controle("PDF : %d figures légendées (38 d'origine, %d schémas d'exposé)"
             % (attendues, attendues - 38), int(figures != attendues), "(%d)" % figures)
    balisage = re.findall(r":::+|\{\.volet\}|\{=typst\}|#encadre|#volet|#chapitre", texte)
    controle("PDF : aucun balisage apparent", balisage)
    print("PDF : %d pages, %d mots, %.1f Mo" % (pdf.page_count, len(texte.split()),
                                               os.path.getsize(asm.SORTIE) / 1e6))
    if echecs:
        raise SystemExit("Contrôles en défaut : " + ", ".join(echecs))
    print("Tous les contrôles passent.")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
