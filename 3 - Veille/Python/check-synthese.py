#!/usr/bin/env python3
"""Ce qui garde la note de synthèse contre ses trois volumes.

La note (`Note de synthèse.md`, tâche T7.2 du plan d'exécution) résume la veille
(Vol. VI), la revue (Vol. VII) et l'état de l'art (Vol. VIII) sans rien y ajouter.
Chaque affirmation s'y ferme sur un renvoi de la forme

    [VI §9.3, réf. 272 — individuel]      [VII §4.2, réf. 51 — sans revue]
    [VI §2 — déclaration · VII §2.3 — déclaration]      [VIII §13, QO 5 — question]

qui couvre le texte écoulé depuis le renvoi précédent du même paragraphe (une ligne
de tableau entière). Huit contrôles :

  [1] PAGES        — le PDF versionné compte 20 pages à 2 près (critère de T7.2) ;
  [2] PARITÉ       — ce PDF est celui que la source rend aujourd'hui, à l'octet hors
                     des champs d'horodatage (Pandoc 3.11, Typst 0.15.1, polices
                     embarquées de Typst seules) ; NON MESURÉ si l'un manque ;
  [3] RENVOIS      — chaque « VOL §x.y » de la note, entre crochets ou non, nomme une
                     section numérotée du volume, numérotée comme Pandoc et Typst la
                     numérotent ; chaque « QO n » est un item de la section citée ;
                     chaque volume est cité ;
  [4] CHIFFRES     — dans les sections de synthèse, tout chiffre est couvert par un
                     renvoi, et figure dans le texte d'une des sections citées ; un
                     pourcentage doit y être un pourcentage. Les nombres écrits en
                     lettres (« douze », « soixante-trois ») sont lus comme des chiffres,
                     des deux côtés ;
  [5] NIVEAUX      — l'étiquette de preuve appartient au vocabulaire du volume ; pour
                     la revue, elle est le régime le plus faible des notices citées, lu
                     à la notice ; pour la veille et l'état de l'art, elle porte en second
                     terme ce régime quand une notice citée est une prépublication arXiv ;
                     « pipeline » ne vaut qu'aux sections 4.6 à 4.13, que la veille
                     déclare le haut du document (VI §2.2) ;
  [6] BIBLIOGRAPHIE — close dans les deux sens : toute notice citée par un renvoi est
                     listée, toute notice listée est citée, et son fragment se lit dans
                     la notice du volume sous ce numéro ; toute clé [CLÉ] du corps a son
                     entrée, et toute entrée est citée ;
  [7] RÉSUMÉ       — `check-resume.py` rend « OK » sur la page de titre du PDF ;
  [8] SOMMES       — une décomposition « 269 = 179 + 54 + 30 + 6 » tombe juste, une part
                     « 145 sur 189 · 77 % » est son pourcentage arrondi.

⚠ Ce que [4] ne voit pas, et c'est une limite déclarée : un chiffre remplacé par un
autre qui figure AUSSI dans la section citée passe ; un chiffre écrit en lettres hors
du vocabulaire lu (un, une, deux, neuf seul) n'est pas vérifié ; une paraphrase fausse
sans chiffre n'est vue par aucun contrôle — seule la relecture la voit.

Usage, depuis `3 - Veille/` :
    python Python/check-synthese.py              -> 0 si tout tient, 1 sinon
    python Python/check-synthese.py --rendre     -> recompose le PDF, puis contrôle
Harnais : `python Python/check-synthese-mutations.py`. `SYNTHESE_RACINE` déplace la
racine du dépôt lue, ce dont le harnais se sert.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # console cp1252 : ⚠ et ☑ ne s'y encodent pas
sys.stderr.reconfigure(encoding="utf-8")

ICI = Path(__file__).resolve().parent
RACINE = Path(os.environ.get("SYNTHESE_RACINE", ICI.parent.parent))
NOTE = RACINE / "3 - Veille" / "Note de synthèse.md"
PDF = NOTE.with_suffix(".pdf")
VOLUMES = {
    "VI": RACINE / "3 - Veille" / "Veille Technologique.md",
    "VII": RACINE / "3 - Veille" / "Revue de littérature.md",
    "VIII": RACINE / "5 - Recension" / "État de l'art — services financiers.md",
}
PAGES = (18, 22)
OUTILS = ("pandoc 3.11", "typst 0.15.1")
APPAREIL = {"Statut de cette note", "Mode d'emploi", "Références"}

TAGS = {
    "VI": {"pipeline", "individuel", "secondaire", "compagnon", "inférence", "recommandation",
           "déclaration", "question"},
    "VII": {"attestée", "autodéclarée", "sans revue", "corpus", "déclaration", "question"},
    "VIII": {"individuel", "secondaire", "compagnon", "inférence", "recommandation",
             "déclaration", "question"},
}
REGIMES = ["sans revue", "autodéclarée", "attestée"]  # du plus faible au plus fort

fail = []


def ok(n, nom, verdict, detail=""):
    print(f"  [{n}] {nom:13}: {detail}{' -> ' if detail else ''}{'OK' if verdict else 'ECHEC'}")
    return verdict


def lire(p):
    return p.read_bytes().decode("utf-8").replace("\r\n", "\n")


# ------------------------------------------------------------------ volumes

def sans_entete(texte):
    """Le texte après l'en-tête YAML, lignes conservées pour les numéros."""
    lignes = texte.split("\n")
    if lignes and lignes[0] == "---":
        fin = lignes.index("---", 1)
        lignes = [""] * (fin + 1) + lignes[fin + 1:]
    return lignes


def titres(lignes):
    """[(indice de ligne, niveau, numéro ou None, titre)] hors blocs clôturés.

    Numérotation de `section-numbering` : Typst ne fait avancer le compteur que pour
    un titre numéroté, et Pandoc rend `{-}` en titre non numéroté. Vérifié contre les
    signets des trois PDF le 15 septembre 2026 : 94, 61 et 118 sections concordent.
    """
    out, cpt, cloture = [], [0] * 6, None
    for i, l in enumerate(lignes):
        m = re.match(r"^(`{3,}|~{3,})", l)
        if m:
            cloture = None if cloture and l.startswith(cloture) else (cloture or m.group(1))
            continue
        if cloture:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", l)
        if not m:
            continue
        niveau, titre = len(m.group(1)), m.group(2)
        if re.search(r"\{[^}]*(?:-|\.unnumbered)[^}]*\}\s*$", titre):
            out.append((i, niveau, None, re.sub(r"\s*\{[^}]*\}\s*$", "", titre)))
            continue
        cpt[niveau - 1] += 1
        cpt[niveau:] = [0] * (6 - niveau)
        out.append((i, niveau, ".".join(map(str, cpt[:niveau])), titre))
    return out


def volume(v):
    """{'sections': {num: texte}, 'notices': {n: texte}} d'un volume."""
    texte = lire(VOLUMES[v])
    lignes = sans_entete(texte)
    ts = titres(lignes)
    sections = {}
    for k, (i, niv, num, _) in enumerate(ts):
        if num is None:
            continue
        fin = next((j for j, n2, _, _ in ts[k + 1:] if n2 <= niv), len(lignes))
        sections[num] = "\n".join(lignes[i:fin])
    refs = texte.split("# Références {-}")[-1].split("::: {#refs}")[-1].split("\n:::")[0]
    notices = {int(n): t for n, t in re.findall(r"(?m)^(\d+)\. (.*)$", refs)}
    return {"sections": sections, "notices": notices}


# ------------------------------------------------------------------ chiffres

UNITES = {"trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9,
          "dix": 10, "onze": 11, "douze": 12, "treize": 13, "quatorze": 14, "quinze": 15,
          "seize": 16, "vingt": 20, "trente": 30, "quarante": 40, "cinquante": 50,
          "soixante": 60, "cent": 100, "mille": 1000, "deux": 2, "un": 1, "une": 1}
SEULS_EXCLUS = {"un", "une", "deux", "neuf"}   # trop communs, ou homographes (« neuf » = nouveau)


def en_lettres(mot):
    parts = mot.split("-")
    if any(p not in UNITES for p in parts) or (len(parts) == 1 and mot in SEULS_EXCLUS):
        return None
    valeur = 0
    for k, p in enumerate(parts):
        u = UNITES[p]
        if p == "vingt" and k and parts[k - 1] == "quatre":
            valeur += 80 - 4
        elif u >= 100:
            valeur = max(valeur, 1) * u
        else:
            valeur += u
    return str(valeur)


NOMBRE = re.compile(r"(?<![\w.,/])(\d+(?:\.\d+)+|\d{1,3}(?:[   ]\d{3})+(?:,\d+)?|\d+(?:,\d+)?)"
                    r"(?![\w])(\s*%)?")
MOT = re.compile(r"(?<![\w-])([a-zàâçéèêëîïôûùüÿœ]+(?:-[a-zàâçéèêëîïôûùüÿœ]+)*)(?![\w-])(\.?)")


def nombres(texte):
    """{(valeur normalisée, '%' ou '')} d'un texte. Un numéro de section « §4.13 » n'est
    pas un chiffre : il est la cible d'un renvoi, que [3] vérifie."""
    t = re.sub(r"§\s*\d+(?:\.\d+)*", " ", texte)
    t = re.sub(r"\b1(er|re)\b", "1", t)
    out = set()
    for m in NOMBRE.finditer(t):
        v = re.sub(r"[   ]", "", m.group(1))
        out.add((v, "%" if m.group(2) else ""))
    for m in MOT.finditer(t.lower()):
        if m.group(1) == "sept" and m.group(2):     # « sept. » abrège septembre
            continue
        v = en_lettres(m.group(1))
        if v:
            out.add((v, ""))
    return out


def source_nombres(texte):
    """Nombres d'une section de volume, appels de notice « [12, 15] » retirés."""
    return nombres(re.sub(r"\[\d+(?:\s*[,–-]\s*\d+)*\]", " ", texte))


# ------------------------------------------------------------------ note

RENVOI = re.compile(r"\[((?:VI|VII|VIII) §[^\]]*)\]")
PARTIE = re.compile(r"^(VI|VII|VIII) §(\d+(?:\.\d+)*)(?:, (réf\.|QO) (\d+(?:, \d+)*))? — (.+)$")
CLE = re.compile(r"\[([A-Z]{3,})\]")


def masquer(lignes):
    """Blocs clôturés et spans de code blanchis ; les lignes gardent leur place."""
    out, cloture = [], None
    for l in lignes:
        m = re.match(r"^(`{3,}|~{3,})", l)
        if m or cloture:
            if m:
                cloture = None if cloture and l.startswith(cloture) else (cloture or m.group(1))
            out.append("")
            continue
        out.append(re.sub(r"`[^`\n]*`", lambda x: " " * len(x.group(0)), l))
    return out


def note():
    lignes = masquer(sans_entete(lire(NOTE)))
    ts = titres(lignes)
    # section de niveau 1 de chaque ligne
    section, courant, idx = [], None, {i: t for i, n, _, t in ts if n == 1}
    for i in range(len(lignes)):
        courant = idx.get(i, courant)
        section.append(courant)
    titre_ligne = {i for i, _, _, _ in ts}
    unites = []   # (ligne, section, genre, texte)
    bloc = []

    def vider():
        if not bloc:
            return
        i0 = bloc[0][0]
        if bloc[0][1].startswith("|"):
            for i, l in bloc:
                if not re.match(r"^\|[\s:|-]+\|$", l):
                    unites.append((i, section[i], "rangée", l))
        elif re.match(r"^(- |\d+\. )", bloc[0][1]):
            items = []
            for i, l in bloc:
                if re.match(r"^(- |\d+\. )", l):
                    items.append([i, re.sub(r"^(- |\d+\. )", "", l)])
                else:
                    items[-1][1] += " " + l.strip()
            unites.extend((i, section[i], "item", t) for i, t in items)
        else:
            unites.append((i0, section[i0], "paragraphe", " ".join(l for _, l in bloc)))
        bloc.clear()

    for i, l in enumerate(lignes):
        if not l.strip() or i in titre_ligne:
            vider()
            continue
        bloc.append((i, l))
    vider()
    return lignes, unites


def parties(contenu):
    """Les renvois d'un crochet, ou une erreur de forme."""
    out = []
    for p in contenu.split(" · "):
        m = PARTIE.match(p.strip())
        if not m:
            return None
        v, num, genre, liste, tag = m.groups()
        nums = [int(x) for x in liste.split(", ")] if liste else []
        out.append({"vol": v, "sec": num, "refs": nums if genre == "réf." else [],
                    "qo": nums if genre == "QO" else [], "tag": tag})
    return out


# ------------------------------------------------------------------ [1] [2] PDF

def pages_du_pdf(octets):
    compte = [int(x) for x in re.findall(rb"/Type\s*/Pages\b.*?/Count\s+(\d+)", octets, re.S)]
    if not compte:
        for m in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", octets, re.S):
            try:
                compte += [int(x) for x in re.findall(rb"/Type\s*/Pages\b.*?/Count\s+(\d+)",
                                                      zlib.decompress(m.group(1)), re.S)]
            except zlib.error:
                pass
    return max(compte) if compte else None


def pages():
    n = pages_du_pdf(PDF.read_bytes()) if PDF.exists() else None
    tient = n is not None and PAGES[0] <= n <= PAGES[1]
    if not tient:
        fail.append(f"[1] pages — {PDF.name} compte {n} pages ; le critère de T7.2 est 20 à 2 près")
    return ok(1, "pages", tient, f"{n} pages, bornes {PAGES[0]}-{PAGES[1]}")


# Champs qui changent d'un rendu à l'autre de la même source : ceux que `check-article.py`
# neutralise (dates, identifiants d'instance et de fichier, positions du xref).
VOLATILS = [
    (rb"/(Creation|Mod)Date\s*\([^)]*\)", rb"/\1Date()"),
    (rb"<xmp:(ModifyDate|CreateDate)>[^<]*</xmp:\1>", rb"<xmp:\1></xmp:\1>"),
    (rb"<xmpMM:InstanceID>[^<]*</xmpMM:InstanceID>", rb"<xmpMM:InstanceID></xmpMM:InstanceID>"),
    (rb"/ID\s*\[[^\]]*\]", rb"/ID[]"),
    (rb"(?m)^\d{10} (\d{5} [nf])", rb"0000000000 \1"),
    (rb"startxref\s+\d+", rb"startxref"),
]


def sans_horodatage(octets):
    for motif, remplacement in VOLATILS:
        octets = re.sub(motif, remplacement, octets)
    return octets


def outils():
    """None si Pandoc 3.11 et Typst 0.15.1 sont là ; sinon ce qui manque."""
    vus = []
    for attendu in OUTILS:
        exe = attendu.split()[0]
        if shutil.which(exe) is None:
            return f"{exe} absent"
        r = subprocess.run([exe, "--version"], capture_output=True, text=True, encoding="utf-8",
                           errors="replace")
        premiere = (r.stdout.splitlines() or [""])[0]
        if not (premiere == attendu or premiere.startswith(attendu + " ")):
            return f"{exe} vu en « {premiere} », {attendu} attendu"
        vus.append(premiere)
    return None


def rendre(sortie):
    """La commande de composition de la note — la seule, que --rendre et [2] partagent.

    Deux variables la rendent reproductible d'un poste à l'autre : les polices embarquées
    de Typst seules (New Computer Modern y est), et une date de création fixée à celle de
    la note, 15 septembre 2026 à 0 h UTC, au lieu de l'horloge et du fuseau du poste —
    deux rendus successifs sont alors identiques à l'octet (vérifié le 15 septembre 2026).
    """
    env = dict(os.environ, TYPST_IGNORE_SYSTEM_FONTS="true", SOURCE_DATE_EPOCH="1789430400")
    r = subprocess.run(["pandoc", NOTE.name, "--pdf-engine=typst", "-o", str(sortie)],
                       cwd=NOTE.parent, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout).strip()[:400])


def parite():
    manque = outils()
    if manque:
        print(f"  [2] parité       : {manque} -> NON MESURÉ")
        return True
    with tempfile.TemporaryDirectory(prefix="parite-synthese-") as tmp:
        essai = Path(tmp) / "essai.pdf"
        try:
            rendre(essai)
        except RuntimeError as e:
            fail.append(f"[2] parité — la source ne se compose plus : {e}")
            return ok(2, "parité", False, "rendu impossible")
        a, b = sans_horodatage(PDF.read_bytes()), sans_horodatage(essai.read_bytes())
    if a == b:
        return ok(2, "parité", True, f"{len(a)} octets hors horodatage, refait à l'identique")
    fail.append(f"[2] parité — {PDF.name} n'est pas le rendu de {NOTE.name} ({len(a)} octets "
                f"versionnés, {len(b)} refaits) : recomposer par --rendre")
    return ok(2, "parité", False, "le PDF versionné n'est pas celui que la source rend")


# ------------------------------------------------------------------ [3] à [6] texte

def renvois(lignes, unites, vols):
    bons, total, par_vol = True, 0, {v: 0 for v in vols}
    for i, l in enumerate(lignes):
        for m in re.finditer(r"\b(VI|VII|VIII) §(\d+(?:\.\d+)*)", l):
            total += 1
            if m.group(2) not in vols[m.group(1)]["sections"]:
                fail.append(f"[3] renvois — l. {i + 1} : {m.group(0)} ne nomme aucune section "
                            f"numérotée du Vol. {m.group(1)}")
                bons = False
    for i, _, _, texte in unites:
        for m in RENVOI.finditer(texte):
            ps = parties(m.group(1))
            if ps is None:
                fail.append(f"[3] renvois — l. {i + 1} : renvoi mal formé « [{m.group(1)}] »")
                bons = False
                continue
            for p in ps:
                par_vol[p["vol"]] += 1
                sec = vols[p["vol"]]["sections"].get(p["sec"], "")
                for q in p["qo"]:
                    if not re.search(rf"(?m)^{q}\. ", sec):
                        fail.append(f"[3] renvois — l. {i + 1} : {p['vol']} §{p['sec']} n'a pas "
                                    f"de question n° {q}")
                        bons = False
    for v, n in par_vol.items():
        if n == 0:
            fail.append(f"[3] renvois — le Vol. {v} n'est cité par aucun renvoi")
            bons = False
    detail = f"{total} renvois de section, " + ", ".join(f"{v} {n}" for v, n in par_vol.items())
    return ok(3, "renvois", bons, detail)


def chiffres(unites, vols):
    bons, controles, segments = True, 0, 0
    cache = {}
    for i, sec, genre, texte in unites:
        if sec in APPAREIL or sec is None:
            continue
        propre = re.sub(r"^\*\*|\*\*$", "", texte)
        if genre == "rangée":
            morceaux = [(RENVOI.sub(" ", propre), [m.group(1) for m in RENVOI.finditer(propre)])]
        else:
            morceaux, debut = [], 0
            for m in RENVOI.finditer(propre):
                morceaux.append((propre[debut:m.start()], [m.group(1)]))
                debut = m.end()
            morceaux.append((propre[debut:], []))
        for segment, groupes in morceaux:
            segment = CLE.sub(" ", segment)
            vus = nombres(segment)
            if not vus:
                continue
            ps = [p for g in groupes for p in (parties(g) or [])]
            if not ps:
                fail.append(f"[4] chiffres — l. {i + 1} : {', '.join(sorted(v + k for v, k in vus))} "
                            f"sans renvoi qui les couvre")
                bons = False
                continue
            segments += 1
            dispo = set()
            for p in ps:
                cle = (p["vol"], p["sec"])
                if cle not in cache:
                    cache[cle] = source_nombres(vols[p["vol"]]["sections"].get(p["sec"], ""))
                dispo |= cache[cle]
            for valeur, genre_n in sorted(vus):
                controles += 1
                trouve = (valeur, "%") in dispo if genre_n else ((valeur, "") in dispo or (valeur, "%") in dispo)
                if not trouve:
                    cibles = " · ".join(f"{p['vol']} §{p['sec']}" for p in ps)
                    fail.append(f"[4] chiffres — l. {i + 1} : « {valeur}{' %' if genre_n else ''} » "
                                f"ne figure pas dans {cibles}")
                    bons = False
    return ok(4, "chiffres", bons, f"{controles} chiffres sur {segments} passages")


def regime(notice):
    if "prépublication non révisée" in notice:
        return "sans revue"
    if "acceptation annoncée" in notice:
        return "autodéclarée"
    return "attestée"


def regime_hors_revue(notice):
    """Régime de publication d'une notice de la veille ou de l'état de l'art : il n'existe que
    pour une pièce déposée sur arXiv. Sans DOI, sans actes ni `journal_ref` à la notice, c'est une
    prépublication — « sans revue », au sens où la revue l'entend (VII §2.2) —, que la notice le
    dise (« Aucune attestation de publication en notice ») ou qu'elle se taise."""
    if "arXiv" not in notice:
        return None
    if re.search(r"doi:\s*10\.|Proceedings|journal_ref", notice) and "Aucune attestation" not in notice:
        return "attestée"
    return "autodéclarée" if "acceptation annoncée" in notice else "sans revue"


def niveaux(unites, vols):
    """Ajout de la reprise du 15 septembre 2026 : une étiquette de la veille ou de l'état de l'art
    porte, après une virgule, le régime de publication de la pièce citée quand celle-ci est une
    prépublication arXiv — « individuel, sans revue ». À régime égal, étiquette égale : sans ce
    second terme, le 91,8 % d'un audit non révisé s'affichait « individuel » quand le 40,55 % d'une
    pièce de même régime, cité par la revue, s'affichait « sans revue »."""
    bons, compte = True, {}
    for i, _, _, texte in unites:
        for m in RENVOI.finditer(texte):
            for p in parties(m.group(1)) or []:
                v, etiquette = p["vol"], p["tag"]
                compte[etiquette] = compte.get(etiquette, 0) + 1
                ou = f"l. {i + 1} : [{v} §{p['sec']} — {etiquette}]"
                tag, _, publication = etiquette.partition(", ")
                if tag not in TAGS[v] or (publication and (v == "VII" or publication not in REGIMES)):
                    fail.append(f"[5] niveaux — {ou} : étiquette hors du vocabulaire du Vol. {v}")
                    bons = False
                    continue
                if v != "VII":
                    notices = vols[v]["notices"]
                    faibles = [r for r in (regime_hors_revue(notices[n]) for n in p["refs"] if n in notices) if r]
                    attendu = min(faibles, key=REGIMES.index) if faibles else None
                    if attendu and publication != attendu:
                        fail.append(f"[5] niveaux — {ou} : la notice citée est une prépublication arXiv "
                                    f"au régime « {attendu} », que l'étiquette doit porter")
                        bons = False
                    elif publication and not attendu:
                        fail.append(f"[5] niveaux — {ou} : un régime de publication exige la notice "
                                    f"arXiv qui le porte")
                        bons = False
                if v == "VI" and tag == "pipeline":
                    maj = [int(x) for x in p["sec"].split(".")]
                    if not (maj[0] == 4 and len(maj) > 1 and 6 <= maj[1] <= 13):
                        fail.append(f"[5] niveaux — {ou} : « pipeline » ne vaut qu'aux sections "
                                    f"4.6 à 4.13 de la veille")
                        bons = False
                if v == "VII":
                    notices = vols["VII"]["notices"]
                    if p["refs"]:
                        faibles = [regime(notices[n]) for n in p["refs"] if n in notices]
                        attendu = min(faibles, key=REGIMES.index) if faibles else None
                        if attendu and tag != attendu:
                            fail.append(f"[5] niveaux — {ou} : les notices citées portent au plus "
                                        f"« {attendu} »")
                            bons = False
                    elif tag in REGIMES:
                        fail.append(f"[5] niveaux — {ou} : un régime de publication exige la notice "
                                    f"qui le porte")
                        bons = False
    detail = ", ".join(f"{t} {n}" for t, n in sorted(compte.items(), key=lambda x: -x[1]))
    return ok(5, "niveaux", bons, detail)


def normal(t):
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)          # liens Markdown -> texte
    return re.sub(r"\s+", " ", t.replace("**", "").replace("*", "").replace("`", "")).strip()


def bibliographie(lignes, unites, vols):
    brut = lire(NOTE)
    corps, _, refs = brut.partition("\n# Références {-}\n")
    if not refs:
        fail.append("[6] bibliographie — section « Références {-} » introuvable")
        return ok(6, "bibliographie", False)
    cles = set(re.findall(r"(?m)^- \*\*\[([A-Z]+)\]\*\*", refs))
    listees = {}
    bons = True
    for v, n, frag in re.findall(r"(?m)^- \*\*(VI|VII|VIII) \[(\d+)\]\*\* (.*)$", refs):
        n = int(n)
        if (v, n) in listees:
            fail.append(f"[6] bibliographie — {v} [{n}] listée deux fois")
            bons = False
        listees[(v, n)] = frag
        notice = vols[v]["notices"].get(n)
        if notice is None:
            fail.append(f"[6] bibliographie — {v} [{n}] : le Vol. {v} n'a pas de notice {n}")
            bons = False
        elif normal(frag) not in normal(notice):
            fail.append(f"[6] bibliographie — {v} [{n}] : le fragment « {normal(frag)[:60]} » ne se lit "
                        f"pas dans la notice {n} du Vol. {v}")
            bons = False
    citees = set()
    for _, _, _, texte in unites:
        for m in RENVOI.finditer(texte):
            for p in parties(m.group(1)) or []:
                citees |= {(p["vol"], n) for n in p["refs"]}
    for v, n in sorted(citees - set(listees)):
        fail.append(f"[6] bibliographie — {v} réf. {n} citée par un renvoi, absente des références")
        bons = False
    for v, n in sorted(set(listees) - citees):
        fail.append(f"[6] bibliographie — {v} [{n}] listée, citée par aucun renvoi")
        bons = False
    masque = "\n".join(masquer(corps.split("\n")))
    appelees = set(CLE.findall(masque))
    for k in sorted(appelees - cles):
        fail.append(f"[6] bibliographie — [{k}] appelée dans le corps, sans entrée")
        bons = False
    vols_cites = {p["vol"] for _, _, _, t in unites for m in RENVOI.finditer(t) for p in parties(m.group(1)) or []}
    for k in sorted(cles - appelees - vols_cites):
        fail.append(f"[6] bibliographie — [{k}] a une entrée, n'est appelée nulle part")
        bons = False
    return ok(6, "bibliographie", bons,
              f"{len(cles)} documents, {len(listees)} notices listées, {len(citees)} citées")


ENTIER = r"\d{1,3}(?:[   ]\d{3})+|\d+"
SOMME = re.compile(rf"(?<![\w,.])({ENTIER})\s*=\s*((?:{ENTIER})(?:\s*\+\s*(?:{ENTIER}))+)(?![\w,])")
PART = re.compile(r"(?<![\w,.])(\d+) sur (\d+)\s*·\s*(\d+(?:,\d+)?)\s*%")


def sommes(unites):
    """[8] — une décomposition écrite « 269 = 179 + 54 + 30 + 6 » tombe juste, et une part écrite
    « 145 sur 189 · 77 % » est son pourcentage arrondi. [4] vérifie que chaque terme est celui de la
    source ; [8] vérifie qu'ensemble ils forment ce que la note dit — ajouté à la reprise du
    15 septembre 2026, après une décomposition de l'audit du 8 août qui ne sommait plus."""
    bons, vues = True, 0
    entier = lambda s: int(re.sub(r"[   ]", "", s))
    for i, sec, _, texte in unites:
        if sec in APPAREIL or sec is None:
            continue
        propre = RENVOI.sub(" ", texte)
        for m in SOMME.finditer(propre):
            vues += 1
            total, termes = entier(m.group(1)), [entier(x) for x in m.group(2).split("+")]
            if sum(termes) != total:
                fail.append(f"[8] sommes — l. {i + 1} : « {m.group(0).strip()} » : les termes font {sum(termes)}")
                bons = False
        for m in PART.finditer(propre):
            vues += 1
            a, b, pct = int(m.group(1)), int(m.group(2)), float(m.group(3).replace(",", "."))
            if b == 0 or abs(100 * a / b - pct) > 0.5:
                reel = f"{100 * a / b:.1f}".replace(".", ",") if b else "—"
                fail.append(f"[8] sommes — l. {i + 1} : « {m.group(0)} » : {a} sur {b} font {reel} %")
                bons = False
    return ok(8, "sommes", bons, f"{vues} décompositions et parts")


def resume():
    if not PDF.exists():
        fail.append(f"[7] résumé — {PDF.name} absent")
        return ok(7, "résumé", False)
    r = subprocess.run([sys.executable, str(ICI / "check-resume.py"), str(PDF)], capture_output=True,
                       text=True, encoding="utf-8", errors="replace",
                       env=dict(os.environ, PYTHONUTF8="1"))
    etat = re.search(r"degagement ([+-][\d.]+) pt\s+\[(\w+)\]", r.stdout)
    tient = r.returncode == 0 and etat is not None and etat.group(2) == "OK"
    if not tient:
        fail.append(f"[7] résumé — check-resume.py : {etat.group(0) if etat else r.stdout.strip()[-120:]}")
    return ok(7, "résumé", tient, f"dégagement {etat.group(1)} pt" if etat else "illisible")


def main():
    if "--rendre" in sys.argv[1:]:
        manque = outils()
        if manque:
            print(f"--rendre : {manque}. Composition impossible.")
            return 1
        rendre(PDF)
        print(f"Rendu : {PDF.name}")
    print(f"Contrôles de la note de synthèse — {NOTE.name}")
    vols = {v: volume(v) for v in VOLUMES}
    lignes, unites = note()
    for f in (pages, parite):
        f()
    renvois(lignes, unites, vols)
    chiffres(unites, vols)
    niveaux(unites, vols)
    bibliographie(lignes, unites, vols)
    resume()
    sommes(unites)
    if fail:
        print("\nECHEC :")
        for f in fail:
            print("  -", f)
        return 1
    print("\nTous les contrôles passent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
