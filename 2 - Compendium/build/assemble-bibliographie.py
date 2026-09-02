#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble l'Annexe I — bibliographie generale consolidee du Vol. IV.

La somme n'a pas de bibliographie propre : elle condense trois monographies qui
en ont chacune une (le Vol. I sous forme de sept fichiers dedies, les Vol. II et
III sous forme de champs de source dans leurs socles factuels). Cette annexe les
REUNIT et les DEDOUBLONNE ; elle n'en ajoute aucune.

Regime, et il est etroit :
  - une entree reprise ici est reprise VERBATIM de sa source ; rien n'est
    reformule, complete de memoire ni verifie a nouveau par ce script ;
  - la deduplication porte sur un identifiant NORMALISE (DOI, arXiv, URL) et,
    a defaut, sur une signature textuelle ; deux formes du meme document ne se
    voient pas a l'oeil, d'ou la normalisation (meme regle que check-veille.py) ;
  - le script ne resout aucun lien et n'atteste d'aucune disponibilite : une
    entree pointant vers une ressource disparue reste exacte et cesse d'etre
    opposable (cf. CLAUDE.md racine, sur le demonstrateur retire du depot).

Sortie : annexe-bibliographie.md, a la racine du dossier du volume.
Usage  : python build/assemble-bibliographie.py [--verifier]
         --verifier : ne reecrit rien, compare les cardinaux et sort 1 si
                      le fichier present ne correspond plus aux sources.
"""

import os
import re
import sys
import unicodedata
from collections import OrderedDict

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(os.path.dirname(RACINE), "1 - Collection")
SORTIE = os.path.join(RACINE, "annexe-bibliographie.md")

VOL1 = os.path.join(CORPUS, "1 - InteroperabiliteAgentique", "Chapitres")
SOCLES = [
    ("Vol. II", os.path.join(CORPUS, "2 - OrchestrationAgentique", "prd", "PRD.md")),
    ("Vol. III", os.path.join(CORPUS, "3 - EntrepriseAgentique", "prd", "PRD.md")),
]

# Les sections de correction de passe ne sont pas de la bibliographie : elles
# consignent ce qu'une verification a change. Les verser produirait des entrees
# qui ne designent aucun document.
EXCLURE_TITRE = ("corrections appliqu",)


def entrees_vol1():
    """Les sept bibliographies du Vol. I, entrees en puces, sections meta exclues."""
    out = []
    fichiers = sorted(
        f for f in os.listdir(VOL1) if "Bibliographie" in f and f.endswith(".md")
    )
    for nom in fichiers:
        saute = False
        with open(os.path.join(VOL1, nom), encoding="utf-8") as fh:
            for ligne in fh:
                ligne = ligne.rstrip("\n")
                if ligne.startswith("#"):
                    saute = any(m in ligne.lower() for m in EXCLURE_TITRE)
                    continue
                if saute:
                    continue
                m = re.match(r"^\s*-\s+(\S.*)$", ligne)
                # 40 caracteres : une entree bibliographique porte au minimum un
                # auteur, une date et un titre. En deca, c'est une puce de prose.
                if m and len(m.group(1)) > 40:
                    out.append(m.group(1).strip())
    return out


def entrees_socles():
    """Les URL primaires citees par les socles des Vol. II et III.

    Les deux volumes n'ont pas de fichier de bibliographie : leurs sources vivent
    dans le corps des entrees F-xx. On n'extrait donc que ce qui est citable sans
    interpretation — une adresse —, et l'entree porte son identifiant d'origine.
    """
    out = []
    for volume, chemin in SOCLES:
        if not os.path.exists(chemin):
            continue
        with open(chemin, encoding="utf-8") as fh:
            texte = fh.read()
        for bloc in re.findall(r"^\s*-\s+\*\*(F-\d+)[^\n]*$", texte, re.M):
            pass  # les identifiants seuls ne suffisent pas ; on passe par les URL
        for ident, url in re.findall(
            r"\*\*(F-\d+)[^\n]*?(https?://[^\s,;)\]]+)", texte
        ):
            out.append((volume, ident, url.rstrip(".,;)")))
    return out


def cle(entree):
    """Identifiant normalise. Deux formes d'un meme document doivent collider."""
    t = entree.lower()
    m = re.search(r"doi\s*[: ]\s*(10\.\S+?)[.\s]*$", t) or re.search(
        r"(10\.\d{4,9}/\S+)", t
    )
    if m:
        return "doi:" + m.group(1).rstrip(".")
    m = re.search(r"arxiv[:\s/]*(\d{4}\.\d{4,5})", t)
    if m:
        return "arxiv:" + m.group(1)
    m = re.search(r"https?://([^\s)]+)", t)
    if m:
        u = re.sub(r"^www\.", "", m.group(1).rstrip("./"))
        u = re.sub(r"/(abs|pdf)/", "/abs/", u)
        return "url:" + u
    return "txt:" + re.sub(r"[^a-z0-9]", "", t)[:70]


def tri(entree):
    """Tri alphabetique insensible aux diacritiques et au balisage."""
    t = re.sub(r"[*_`]", "", entree)
    return unicodedata.normalize("NFD", t).encode("ascii", "ignore").decode().lower()


def construire():
    brutes = entrees_vol1()
    uniques = OrderedDict()
    fondus = 0
    for e in brutes:
        k = cle(e)
        if k in uniques:
            fondus += 1
        else:
            uniques[k] = e
    liste = sorted(uniques.values(), key=tri)
    socle = entrees_socles()
    return brutes, liste, fondus, socle


def rendre(brutes, liste, fondus, socle):
    L = []
    a = L.append
    a("# Annexe I — Bibliographie générale consolidée")
    a("")
    a("*Annexe du plan (`TOC.md`), neuvième et dernière. Elle réunit les bibliographies des trois")
    a("monographies sources et les dédoublonne ; elle n'ajoute aucune entrée.*")
    a("")
    a("---")
    a("")
    a("## Régime de cette annexe — à lire avant toute citation")
    a("")
    a("⚠ **Cette annexe est une RÉUNION, non une vérification.** Chaque entrée est reprise")
    a("**verbatim** de la bibliographie du volume qui la porte ; *rien n'y est reformulé, complété de")
    a("mémoire, ni vérifié à nouveau*. Le niveau de preuve d'un fait ne se lit donc **jamais** ici :")
    a("il se lit à l'entrée de socle qui le porte ([Annexe B](PRD/socle-consolide.md)), et une")
    a("référence présente dans cette liste **n'atteste de rien** sinon qu'un volume source l'a citée.")
    a("")
    a("⚠ **Elle ne se confond pas avec les deux autres inventaires du volume, et les trois se")
    a("distinguent par leur objet.**")
    a("")
    a("| Pièce | Ce qu'elle inventorie | Autorité |")
    a("|---|---|---|")
    a("| [`annexe-references.md`](annexe-references.md) | les **faits** sur lesquels la somme s'adosse — 159 entrées `S-nnn` | abrégé du socle ; le socle fait foi |")
    a("| **La présente annexe** | les **documents** d'où ces faits et leur contexte proviennent | réunion des sources ; **aucune autorité propre** |")
    # ⚠ `audit-references.md` n'est PAS au dépôt : le rapport de validation a été
    # retiré avec les pièces d'audit internes. Le lien a donc été défait à la main
    # dans l'annexe versionnée, et le générateur a continué de l'émettre — d'où
    # l'échec de `--verifier` : *un générateur qui ne reproduit plus son livrable
    # cesse d'être l'autorité de ce livrable.* La ligne est alignée sur la forme
    # versionnée (2 septembre 2026), avec la mention d'absence plutôt qu'un lien mort.
    a("| `audit-references.md` — ⚠ **non versé au dépôt** | la **validation** des 159 références sur cinq critères | rapport de mesure, **jamais citable à l'appui d'un énoncé** |")
    a("")
    a("⚠ **Trois bornes.** *(a)* **Le Vol. I fournit la quasi-totalité des entrées**, parce qu'il est")
    a("le seul des trois à tenir une bibliographie séparée ; les **Vol. II et III** portent leurs")
    a("sources **dans le corps de leurs entrées de socle**, et seules leurs adresses primaires sont")
    a("reprises ici, sous leur identifiant d'origine. *L'asymétrie est celle des sources, non un défaut")
    a("de la réunion.* *(b)* **Aucun lien n'est résolu par l'assemblage** : une entrée pointant une")
    a("ressource disparue **reste exacte et cesse d'être opposable**. *(c)* ⚠ **La dédoublonnage porte")
    a("sur un identifiant normalisé** — DOI, arXiv, URL — et, à défaut, sur une signature textuelle :")
    a("*deux formes du même document ne se voient pas à l'œil.*")
    a("")
    a("| Mesure | Valeur |")
    a("|---|---|")
    a(f"| Entrées relevées aux sept bibliographies du Vol. I | **{len(brutes)}** |")
    a(f"| Doublons fondus par identifiant normalisé | **{fondus}** |")
    a(f"| **Entrées uniques de la présente annexe** | **{len(liste)}** |")
    a(f"| Adresses primaires reprises des socles des Vol. II et III | **{len(socle)}** |")
    a("")
    a("*Cardinaux produits par [`build/assemble-bibliographie.py`](build/assemble-bibliographie.py)")
    a("à chaque exécution — jamais recopiés (règle des décomptes du dépôt).*")
    a("")
    a("---")
    a("")
    a("## I.1 — Entrées consolidées du Vol. I")
    a("")
    lettre = None
    for e in liste:
        prem = tri(e)[:1].upper() or "—"
        if not prem.isalpha():
            prem = "—"
        if prem != lettre:
            lettre = prem
            a("")
            a(f"### {lettre}")
            a("")
        a(f"- {e}")
    a("")
    a("---")
    a("")
    a("## I.2 — Les Vol. II et III, et pourquoi cette annexe ne peut pas les servir")
    a("")
    a("⚠ **Constat mesuré le 30 juillet 2026, et il est le résultat le plus utile de l'assemblage :")
    a("les socles des Vol. II et III ne portent PAS leurs sources sous une forme reprenable.**")
    a("Le balayage de leurs deux PRD rend **une seule adresse pour l'ensemble des deux volumes** ;")
    a("leurs entrées `F-xx` citent leurs sources **en prose et par leur nom** — « lautorite.qc.ca »,")
    a("« Norton Rose Fulbright », « rapport annuel Desjardins 2025 » —, jamais par un identifiant")
    a("résoluble.")
    a("")
    a("⚠ **Ce que cela veut dire, et il faut le dire sans l'adoucir.** *(a)* **La consolidation est")
    a("structurellement asymétrique** : le Vol. I fournit une bibliographie parce qu'il en tient une ;")
    a("les deux autres n'en fournissent aucune parce qu'ils n'en tiennent pas. *L'annexe ne réunit donc")
    a("pas trois bibliographies — elle en réunit une, et constate l'absence des deux autres.* *(b)* ⚠ Le")
    a("procédé des deux volumes **n'est pas fautif à sa date** : leur régime de preuve repose sur")
    a("l'entrée de socle, qui porte le niveau, la date et la réserve — *une entrée `[A]` dont la source")
    a("est nommée en prose reste une entrée `[A]`.* *(c)* ⚠ **Mais il rend leur vérification par un")
    a("tiers plus coûteuse d'un ordre de grandeur** : un relecteur qui veut remonter à la source doit")
    a("la retrouver, là où le Vol. I la lui donne. *C'est précisément le coût que l'arbitrage externe")
    a("nomme quand il écrit que le système de renvois reste opaque au lecteur externe.*")
    a("")
    a("**Ce que l'annexe fait donc, et ce qu'elle laisse ouvert.** Elle **ne fabrique aucune référence**")
    a("depuis une mention en prose — *déduire une adresse d'un nom d'éditeur serait exactement la faute")
    a("que la décision 18 du TOC vient de proscrire ailleurs*. La constitution d'une bibliographie pour")
    a("les Vol. II et III est **un travail de leurs volumes**, non de la somme, et elle est **remontée**")
    a("comme telle.")
    a("")
    if socle:
        a("**La seule adresse relevée**, versée pour l'exactitude du décompte :")
        a("")
        a("| Volume | Entrée | Adresse |")
        a("|---|---|---|")
        vus = set()
        for volume, ident, url in socle:
            k = (volume, ident, url)
            if k in vus:
                continue
            vus.add(k)
            a(f"| {volume} | `{ident}` | <{url}> |")
        a("")
    a("---")
    a("")
    a("*Annexe assemblée le 30 juillet 2026, décision d'auteur D-11 (PRD §15).*")
    return "\n".join(L) + "\n"


def main():
    brutes, liste, fondus, socle = construire()
    contenu = rendre(brutes, liste, fondus, socle)
    if "--verifier" in sys.argv:
        if not os.path.exists(SORTIE):
            print("ÉCHEC — annexe-bibliographie.md absente")
            return 1
        actuel = open(SORTIE, encoding="utf-8").read()
        if actuel != contenu:
            print("ÉCHEC — annexe-bibliographie.md ne correspond plus à ses sources")
            return 1
        print(f"OK — {len(liste)} entrées uniques, {fondus} doublons fondus.")
        return 0
    with open(SORTIE, "w", encoding="utf-8") as fh:
        fh.write(contenu)
    print(
        f"OK — {len(liste)} entrées uniques écrites "
        f"({len(brutes)} relevées, {fondus} doublons fondus, "
        f"{len(socle)} adresses de socle)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
