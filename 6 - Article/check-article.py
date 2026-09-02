#!/usr/bin/env python3
"""Ce que le README de ce dossier a mesuré une fois, gardé à chaque passage.

Le README du 1er septembre 2026 écrivait, de la clôture de la bibliographie :
« c'est une mesure faite pour cette passe, par aucun script du dépôt : rien ne la
garde ». C'était vrai d'elle, et c'était vrai de tout le reste — la parité entre
la source et le rendu, la résolution des renvois écrits à la main, les cardinaux
que le README publie, les valeurs que le script de rejeu attend. Ce fichier est
ce qui les garde. ⚠ Il ne juge pas le propos : il mesure la forme, et il le dit.

Cinq contrôles :
  [1] la BIBLIOGRAPHIE est close dans les deux sens — toute clé définie est
      citée, toute clé citée est définie ;
  [2] la PARITÉ du rendu — le PDF versionné est CELUI que la source rend
      aujourd'hui, comparé à l'octet hors des six champs volatils ;
  [3] les RENVOIS « § X.Y » écrits à la main résolvent tous vers un titre
      numéroté — 165 le 2 septembre 2026, et Typst n'en garde aucun ;
  [4] les CARDINAUX que le README publie — pages, octets, lignes, planches,
      tableaux, notices, titres — sont ceux de la mesure ;
  [5] les SCORES que `rejeu-politique.py` attend sont ceux que l'article imprime
      au § 7.5 — la copie opposée à l'original, pas à une autre copie.

Usage : python check-article.py [--sans-parite]   -> 0 si tout tient, 1 sinon.
Se lance de n'importe quel répertoire ; `ARTICLE_RACINE` déplace le dossier
mesuré, ce dont le harnais de mutation se sert.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

RACINE = Path(os.environ.get("ARTICLE_RACINE", Path(__file__).resolve().parent))
SRC = RACINE / "article-hpc-qpu.typ"
PDF = RACINE / "article-hpc-qpu.pdf"
BIB = RACINE / "references.bib"
README = RACINE / "README.md"
REJEU = RACINE / "rejeu-politique.py"

fail = []


def ok(n, nom, verdict, detail=""):
    print(f"  [{n}] {nom:12}: {detail}{' -> ' if detail else ''}{'OK' if verdict else 'ECHEC'}")
    return verdict


# ---------------------------------------------------------------- [1] bibliographie

def bibliographie(src: str, bib: str):
    definies = re.findall(r"^@\w+\s*\{\s*([^,\s]+)\s*,", bib, re.M)
    doublons = sorted({k for k in definies if definies.count(k) > 1})
    # Les citations : « @clé » hors des étiquettes « <…> ». Le lookbehind écarte
    # l'adresse de l'auteur (« u@gmail ») ; le préfixe écarte les renvois
    # internes (« @fig:… », « @sec:… »), qui ne sont pas des références.
    corps = re.sub(r"<[^>\n]+>", "", src)
    citees = set(re.findall(r"(?<![\w.])@([A-Za-z][\w:\-]*)", corps))
    citees |= set(re.findall(r"#cite\(<([^>]+)>", src))
    citees = {c for c in citees if not re.match(r"(fig|sec|tab|eq|app):", c)}
    mortes = sorted(set(definies) - citees)
    pendantes = sorted(citees - set(definies))
    for nom, liste in (("clés en double", doublons), ("définies jamais citées", mortes),
                       ("citées jamais définies", pendantes)):
        if liste:
            fail.append(f"bibliographie — {nom} : {', '.join(liste)}")
    return ok(1, "bibliographie", not (doublons or mortes or pendantes),
              f"{len(set(definies))} définies, {len(citees & set(definies))} citées")


# ---------------------------------------------------------------------- [2] parité

# ⚠ SIX CHAMPS, ET PAS UN DE PLUS. Mesuré le 1er septembre puis le 2 : deux rendus
# de la même source par le même Typst rendent des fichiers de même taille où seuls
# ces champs diffèrent — le README du 1er septembre en comptait cinq, le `/ID` du trailer est le sixième. `xmpMM:DocumentID`, lui, est dérivé du contenu et ne bouge
# pas — c'est ce qui rend la comparaison concluante. Neutraliser davantage
# aveuglerait le contrôle ; neutraliser moins le ferait crier à chaque rendu.
VOLATILS = [
    (rb"/(Creation|Mod)Date\s*\([^)]*\)", rb"/\1Date()"),
    (rb"<xmp:(ModifyDate|CreateDate)>[^<]*</xmp:\1>", rb"<xmp:\1></xmp:\1>"),
    (rb"<xmpMM:InstanceID>[^<]*</xmpMM:InstanceID>", rb"<xmpMM:InstanceID></xmpMM:InstanceID>"),
    # ⚠ Le sixième : l'identifiant de fichier du trailer, que le README du
    # 1er septembre n'avait pas relevé — il comptait « cinq endroits », et le
    # premier passage de ce contrôle a échoué sur lui, à 51 octets de la fin.
    (rb"/ID\s*\[[^\]]*\]", rb"/ID[]"),
]


def sans_horodatage(octets: bytes) -> bytes:
    for motif, remplacement in VOLATILS:
        octets = re.sub(motif, remplacement, octets)
    return octets


def parite():
    if shutil.which("typst") is None:
        print("  [2] parité      : typst absent -> NON MESURÉ")
        print("      Le rendu versionné n'est donc PAS opposé à sa source. Installer Typst 0.15.1.")
        return True
    with tempfile.TemporaryDirectory(prefix="parite-article-") as tmp:
        essai = Path(tmp) / "essai.pdf"
        r = subprocess.run(["typst", "compile", SRC.name, str(essai)], cwd=RACINE,
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0 or not essai.exists():
            fail.append(f"parité — la source ne compile plus : {(r.stderr or '').strip()[:300]}")
            return ok(2, "parité", False, "rendu impossible")
        a, b = sans_horodatage(PDF.read_bytes()), sans_horodatage(essai.read_bytes())
    if a == b:
        return ok(2, "parité", True, f"{len(a)} octets hors horodatage, refait à l'identique")
    i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
    fail.append(f"parité — {PDF.name} n'est pas le rendu de {SRC.name} : première divergence à "
                f"l'octet {i} ({len(a)} versionnés, {len(b)} refaits). Rendre avant de conclure")
    return ok(2, "parité", False, "le PDF versionné n'est pas celui que la source rend")


# --------------------------------------------------------------------- [3] renvois

def numerotation(src: str):
    """Les titres numérotés comme `set heading(numbering: "1.1")` les numérote."""
    nums, compteur = {}, [0, 0, 0]
    for m in re.finditer(r"(?m)^(=+) (.+)$", src):
        niv = len(m.group(1))
        if niv > 3:
            continue
        compteur[niv - 1] += 1
        for k in range(niv, 3):
            compteur[k] = 0
        nums[".".join(str(c) for c in compteur[:niv])] = m.group(2).strip()
    return nums


def renvois(src: str):
    nums = numerotation(src)
    cites = re.findall(r"§\s*(\d+(?:\.\d+){0,2})", src)
    morts = sorted({c for c in cites if c not in nums})
    if morts:
        fail.append(f"renvois — « § » sans titre : {', '.join(morts)}")
    return ok(3, "renvois", not morts, f"{len(cites)} renvois « § » à la main, {len(set(cites))} cibles")


# ------------------------------------------------------------------- [4] cardinaux

def pages_du_pdf(octets: bytes):
    d = octets
    if not re.search(rb"/Type\s*/Pages", d) and b"/ObjStm" in d:
        for m in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", d, re.S):
            try:
                d += zlib.decompress(m.group(1))
            except zlib.error:
                pass
    compte = [int(x) for x in re.findall(rb"/Type\s*/Pages.*?/Count\s+(\d+)", d, re.S)]
    return max(compte) if compte else None


def entier(s: str) -> int:
    return int(s.replace(" ", "").replace("\u202f", "").replace("\u00a0", ""))


def cardinaux(src: str, bib: str, readme: str):
    """Chaque nombre que le README publie, opposé à la mesure qui le produit."""
    mesures = {
        "pages": pages_du_pdf(PDF.read_bytes()),
        "octets du PDF": PDF.stat().st_size,
        "lignes de la source": src.count("\n") + (0 if src.endswith("\n") else 1),
        "octets de la source": SRC.stat().st_size,
        "titres de niveau 1": len(re.findall(r"(?m)^= ", src)),
        "titres de niveau 2": len(re.findall(r"(?m)^== ", src)),
        "planches": len(re.findall(r"#figure\(\s*fig-", src)),
        "tableaux": len(re.findall(r"caption\s*:", src)) - len(re.findall(r"#figure\(\s*fig-", src)),
        "notices": len(re.findall(r"^@\w+\s*\{", bib, re.M)),
        "lignes du .bib": bib.count("\n") + (0 if bib.endswith("\n") else 1),
    }
    # ⚠ Le README se lit sur ses formes exactes. Une forme qui change casse ce
    # contrôle AVANT de casser le lecteur : c'est voulu.
    motifs = {
        "pages": r"\*\*(\d[\d \u202f]*) p\. / ",
        "octets du PDF": r" p\. / (\d[\d \u202f]*) o\.\*\*",
        "lignes de la source": r"\*\*(\d[\d \u202f]*) l\. / ",
        "octets de la source": r" l\. / (\d[\d \u202f]*) o\.\*\*",
        "titres de niveau 1": r"(\d+) sections de niveau 1",
        "titres de niveau 2": r"(\d+) de niveau 2",
        "planches": r"\*\*(\d+) planches\*\*",
        "tableaux": r"\*\*(\d+) tableaux\*\*",
        "notices": r"\*\*(\d+) entrées / ",
        "lignes du .bib": r" entrées / (\d+) l\.\*\*",
    }
    ecarts = []
    for nom, motif in motifs.items():
        m = re.search(motif, readme)
        if not m:
            ecarts.append(f"{nom} : forme introuvable au README")
            continue
        publie, mesure = entier(m.group(1)), mesures[nom]
        if publie != mesure:
            ecarts.append(f"{nom} : README {publie}, mesure {mesure}")
    for e in ecarts:
        fail.append("cardinaux — " + e)
    return ok(4, "cardinaux", not ecarts, f"{len(motifs)} nombres publiés opposés à la mesure")


# ---------------------------------------------------------------------- [5] scores

def scores(src: str, rejeu: str):
    """Les huit scores : ce que le script assert contre ce que l'article imprime."""
    attendus = sorted(float(v) for _, v in re.findall(r'approx\(s\["([\w\-]+)"\],\s*([\d.]+)\)', rejeu))
    # Six sont en gras dans les deux déroulés ; les deux de la sensibilité sont
    # dans la phrase « 0,750 contre 0,690 ». La forme est celle du 2 septembre 2026.
    publies = [float(v.replace(",", ".")) for v in re.findall(r'bold\("(\d,\d{3})"\)', src)]
    m = re.search(r"(\d,\d{3}) contre (\d,\d{3})", src)
    if m:
        publies += [float(m.group(1).replace(",", ".")), float(m.group(2).replace(",", "."))]
    publies = sorted(publies)
    verdict = attendus == publies and len(attendus) == 8
    if not verdict:
        fail.append(f"scores — le script attend {attendus}, l'article imprime {publies}")
    return ok(5, "scores", verdict, f"{len(attendus)} attendus par le script, {len(publies)} imprimés au § 7.5")


def main():
    for p in (SRC, PDF, BIB, README, REJEU):
        if not p.exists():
            print(f"introuvable : {p}")
            return 1
    src, bib, readme, rejeu = (x.read_text(encoding="utf-8") for x in (SRC, BIB, README, REJEU))
    print(f"Contrôles du dossier — {RACINE.name}")
    bibliographie(src, bib)
    if "--sans-parite" in sys.argv:
        print("  [2] parité      : SAUTÉ sur demande (--sans-parite) -> NON MESURÉ")
    else:
        parite()
    renvois(src)
    cardinaux(src, bib, readme)
    scores(src, rejeu)
    if fail:
        print("\nECHEC :")
        for f in fail:
            print("  -", f)
        return 1
    print("\nTous les contrôles passent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
