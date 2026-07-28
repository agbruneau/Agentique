#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle des pièces du compendium (Vol. IV) — livrable de la porte G-3.

Ce script est celui que le [PRD](PRD.md) §9 déclare « ☐ à construire en G-3 » et
que le jalon **J-IV-2** attend. Son domaine y est écrit, et c'est sa
spécification : *« les pièces : en-têtes à cinq champs, renvois « ch. N » 1-50,
identifiants du socle consolidé résolvant contre l'Annexe B, identifiants
préfixés de leur volume, registre de gel aligné pièce à pièce, motifs de
balayage §8 »*. `check-sieges.py` en est le **premier versement**, non le
substitut : il lit les pièces **ensemble** pour vérifier l'abstention ; celui-ci
les lit **une à une** contre l'appareil.

⚠ **Ce script est du contenu : il se vérifie comme le reste.** Toute
modification se valide par mutation — constat de **passage sur le corpus
intact**, puis chaque classe de faute introduite et détectée. Le harnais est
`check-compendium-mutations.py`. *Sans la première constatation, un script cassé
« détecte » tout.*

Ce que ce script est, et ce qu'il n'est pas
-------------------------------------------
C'est un contrôle **de forme**, exécuté sur des **motifs de ligne** et des
**décomptes littéraux**. Il ne lit pas le sens. Il ne remplace donc **ni** la
collation de fond de la porte G-4 (lacune de couverture / contradiction), **ni**
la relecture dédiée que CA-IV-11 et CA-IV-13 exigent d'un tiers — et que **D-6
ne fournit pas**. *Un contrôle de forme qui passe n'atteste pas qu'une pièce est
recevable ; il atteste qu'elle ne porte pas les sept classes de défaut ci-dessous.*

Deux verdicts, et la distinction est doctrinale
------------------------------------------------
- **ÉCHEC** — un défaut que la passe qui l'a introduit peut corriger seule.
- **RAPPORT** — un écart **mesuré et déclaré**, sur des pièces qu'aucune passe
  en cours n'a mandat de corriger. Même doctrine que le `renvoi: None` de
  `check-sieges.py` : *un contrôle bruyant est un contrôle ignoré ; un contrôle
  supprimé est une spécification.* Chaque désactivation porte son **motif
  chiffré** et sa **condition de réactivation**.

Domaine : les cinquante pièces `NN-slug.md` sous `2 - Compendium/Livre */`.
Sortie 0 si tout passe, 1 sinon.
"""

import os
import re
import sys
import unicodedata
from pathlib import Path

# « 2 - Compendium ». La variable d'environnement n'existe que pour le harnais
# de mutation, qui doit pouvoir pointer une copie du corpus : muter le corpus
# réel pour éprouver son contrôle est le genre de raccourci qui laisse une trace.
RACINE = Path(os.environ.get("COMPENDIUM_RACINE", Path(__file__).resolve().parent.parent))

# La console Windows par défaut est en cp1252 et ne sait pas écrire « § » ni « É ».
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SOCLE = RACINE / "PRD" / "socle-consolide.md"
REGISTRE = RACINE / "PRD" / "registre-gel.md"

# Les cinq champs du PRD §6, dans l'ordre où l'en-tête les porte.
CHAMPS = ["Statut", "Date de gel", "Socle mobilisé", "Garde-fous balayés", "Volumétrie cible"]

CHAPITRES = range(1, 51)  # plafond dur de cinquante (décision 13a du TOC, contrôle C15)

# --------------------------------------------------------------------------
# Délimitation du corps — reprise textuelle de `check-sieges.py`, et le motif
# des deux exclusions n'est pas évident :
#
#  — la **note de statut** hors plan se retire à la publication (PRD §6) et
#    rend compte des remontées : elle CITE les défauts, elle ne les porte pas ;
#  — l'**en-tête à cinq champs** DÉCLARE le balayage, il ne porte pas la
#    matière. La décision 16 du TOC l'écrit en toutes lettres : un décompte
#    d'occurrences porte sur le corps, « en-tête et note de statut exclus ».
#
# Les deux exclusions sont donc la définition même du domaine de comptage, non
# une commodité — les réintroduire en « simplifiant » ferait compter à l'en-tête
# les occurrences qu'il déclare, et tout cardinal deviendrait faux d'un.
# --------------------------------------------------------------------------
FIN_DE_CORPS = re.compile(r"^##\s*§?\s*[\d.]*\s*—?\s*Note de statut", re.M)
DEBUT_DE_CORPS = re.compile(r"^>\s|^##\s", re.M)


def corps(texte):
    """Le corps de la pièce : en-tête à cinq champs et note de statut exclus."""
    debut = DEBUT_DE_CORPS.search(texte)
    texte = texte[debut.start():] if debut else texte
    coupe = FIN_DE_CORPS.search(texte)
    return texte[: coupe.start()] if coupe else texte


def sans_citations(texte):
    """Retire les spans « … » et `…`.

    ⚠ **Neutralisation, avec son motif.** Le corpus **cite abondamment les
    formes qu'il proscrit, pour les proscrire** : « jamais “quatre reports” »,
    « écrire “attendu par E-23”, jamais “exigée par E-23” ». Ces emplois sont
    **métalinguistiques** — la pièce y mentionne la formule, elle ne l'emploie
    pas —, et ils sont **corrects**. Les compter ferait échouer P7 sur les
    pièces les plus rigoureuses du corpus, ce qui est l'inverse de son objet.
    Même doctrine que `strip_guillemets` de `check-toc.py`.
    """
    texte = re.sub(r"«[^«»]*»", "«»", texte)
    texte = re.sub(r"“[^“”]*”", "“”", texte)
    return re.sub(r"`[^`]*`", "``", texte)


def pieces():
    """Les pièces du compendium, triées, hors README."""
    return sorted(p for p in RACINE.glob("Livre */[0-9][0-9]-*.md") if p.name != "README.md")


def entete(texte):
    """{champ: valeur} pour les cinq champs du tableau de tête."""
    trouves = {}
    for ligne in texte.splitlines():
        m = re.match(r"^\|\s*\*\*([^*]+)\*\*\s*\|(.*)\|\s*$", ligne)
        if m and m.group(1).strip() in CHAMPS:
            trouves[m.group(1).strip()] = m.group(2).strip()
    return trouves


def nombre(chaine):
    """« 11 000 », « 11 000 » (espace insécable), « 11000 » → 11000."""
    return int(re.sub(r"[^\d]", "", chaine))


# --------------------------------------------------------------------------
# P4 — la table de résolution, lue à sa source unique.
#
# Le socle consolidé se déclare « **source unique des identifiants S-nnn** :
# aucun autre document du dépôt n'en alloue ». Le script ne recopie donc aucune
# liste : il **extrait** les trois tables du fichier. *Une table d'identifiants
# recopiée dans un script est une seconde source, c'est-à-dire une divergence
# qui attend.*
# --------------------------------------------------------------------------
def tables_du_socle():
    """(S-nnn alloués, identifiants sources résolus, identifiants sources connus).

    « Connu » = une rangée existe. « Résolu » = cette rangée porte un `S-nnn`.
    Les deux ensembles diffèrent de **huit** identifiants, et l'écart est le
    résultat : `F-12`, `F-13`, `F-14` (non attribués par le Vol. II), `F-92` et
    `F-96` (dette de vote non résorbée, PRD §7.1), `H-13`, `H-15`, `H-16`
    (hors socle factuel du Vol. III). Ils sont **connus et non résolus** — donc
    citables avec leur réserve, jamais versables.
    """
    if not SOCLE.exists():
        return None, None, None
    texte = SOCLE.read_text(encoding="utf-8")
    alloues = set(re.findall(r"\*\*(S-\d{3})\*\*", texte))
    connus, resolus = set(), set()
    for ligne in texte.splitlines():
        if not ligne.startswith("|"):
            continue
        for m in re.finditer(r"`([FH]-\d{2}b?)`\**\s*\|\s*(?:→|—)\s*\|\s*([^|]*)", ligne):
            connus.add(m.group(1))
            if re.search(r"S-\d{3}", m.group(2)):
                resolus.add(m.group(1))
    return alloues, resolus, connus


# --------------------------------------------------------------------------
# P5 — la grammaire des décomptes d'en-tête (décision 16 du TOC).
#
# Formes réellement employées par les cinquante pièces :
#   « R-14 (trois degrés d'absence) : deux occurrences, § 3.1.1 et § 3.4.3 »
#   « R-1 à R-8 : zéro occurrence »
#   « R-01 à R-14 : zéro occurrence pour R-01 à R-13 »   ← le « pour » prime
#   « R-13 : le marqueur figure une fois, § 3.3.1 »
#   « R-02 : zéro occurrence de l'identifiant »
# --------------------------------------------------------------------------
MOTS = {
    "zéro": 0, "une": 1, "un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5,
    "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10, "onze": 11, "douze": 12,
    "treize": 13, "quatorze": 14, "quinze": 15, "seize": 16, "dix-sept": 17,
    "dix-huit": 18, "dix-neuf": 19, "vingt": 20, "vingt et une": 21, "vingt et un": 21,
    "vingt-deux": 22, "vingt-trois": 23, "vingt-quatre": 24, "vingt-cinq": 25,
}
CARDINAL = "(?:" + "|".join(sorted(map(re.escape, MOTS), key=len, reverse=True)) + r"|\d+)"
LISTE_R = r"R-\d{1,2}(?:\s*(?:,|et|à)\s*R-\d{1,2})*"
DECOMPTE = re.compile(
    r"(" + LISTE_R + r")\s*(?:\([^)]*\))?\s*:\s*(?:le marqueur figure\s+)?"
    r"(" + CARDINAL + r")\s+(occurrences?|fois)([^;.]{0,45})", re.I)


def deplie(liste):
    """« R-01, R-03 à R-05 » → ['R-01', 'R-03', 'R-04', 'R-05'].

    ⚠ La largeur du numéral est conservée : `R-1` (Vol. II) et `R-01`
    (Vol. III) sont **deux identifiants distincts** portant sur des objets
    différents (décision 7 du TOC), et les confondre ferait compter les
    occurrences de l'une pour l'autre.
    """
    sortie = []
    for jeton in re.split(r"\s*(?:,|et)\s*", liste):
        m = re.match(r"R-(\d{1,2})\s*à\s*R-(\d{1,2})$", jeton)
        if m:
            a, b = m.groups()
            sortie += [f"R-{i:0{len(a)}d}" for i in range(int(a), int(b) + 1)]
        elif re.match(r"R-\d{1,2}$", jeton):
            sortie.append(jeton)
    return sortie


def declarations(cellule):
    """{identifiant: (cardinal, ancré, contradictions)} pour un champ « Garde-fous ».

    « Ancré » = la pièce déclare que **le marqueur compté est l'identifiant
    lui-même** (« occurrences du sigle », « de l'identifiant », « le marqueur
    figure N fois »), ou déclare **zéro**. Hors de ces cas, la décision 16
    admet aussi le **marqueur littéral de la formule** — « degré 3 », « fait
    négatif vérifié », « PROJETÉ » —, que le script ne sait pas dériver de
    l'identifiant : le décompte est alors mesuré et rapporté, non opposé.
    """
    cellule = sans_citations(cellule).replace("**", "").replace("*", "")
    vues, conflits = {}, []
    for m in DECOMPTE.finditer(cellule):
        brut = m.group(2).lower()
        n = MOTS.get(brut, int(brut) if brut.isdigit() else None)
        if n is None:
            continue
        suite = m.group(4)
        # « R-01 à R-14 : zéro occurrence POUR R-01 à R-13 » — le domaine réel
        # est celui du « pour », non celui qui précède les deux-points.
        pour = re.match(r"\s*pour\s+(" + LISTE_R + r")", suite)
        identifiants = deplie(pour.group(1) if pour else m.group(1))
        ancre = bool(re.search(r"du sigle|de l'identifiant", suite)) or \
            m.group(3).lower().startswith("fois") or n == 0
        specifique = "à" not in m.group(1) and "," not in m.group(1)
        for i in identifiants:
            if i in vues and vues[i][0] != n:
                conflits.append((i, vues[i][0], n))
                if not specifique:      # une plage ne détrône pas une déclaration nommée
                    continue
            vues[i] = (n, ancre)
    return vues, conflits


# --------------------------------------------------------------------------
# P7 — les formulations imposées du PRD §8.
#
# ⚠ **Chaque motif est validé par mutation avant emploi** (voir-doit /
# ne-doit-pas-voir), et la moitié « ne-doit-pas-voir » est ici la difficile :
# le corpus **cite abondamment les formes proscrites pour les proscrire**.
# `sans_citations` retire les spans « … », `“ … ”` et `` ` … ` `` où vivent ces
# mentions ; les motifs ci-dessous sont en outre **ancrés sur leur objet** —
# « fixé » n'est fautif que d'un JALON, jamais d'une échéance réglementaire,
# que trois pièces datent à bon droit.
# --------------------------------------------------------------------------
#
# ⚠ **Seconde neutralisation, et c'est la plus large : l'ÉNONCÉ de la
# proscription.** Une pièce qui écrit « les jalons sont **visés**, jamais
# fixés », « ces jalons ne sont pas *fixés* » ou « ce sont quatre cibles
# successives, **non** quatre reports » **applique** la formulation imposée —
# elle ne l'enfreint pas. Ces énoncés emploient l'emphase markdown là où
# d'autres emploient les guillemets, et `sans_citations` ne les voit donc pas.
# **Quatre pièces sur cinquante étaient dans ce cas au premier passage** (ch. 30,
# 33, 36 et 49), toutes correctes : *un motif qui signale une occurrence
# légitime rend le contrôle bruyant, donc ignoré.*
#
# La neutralisation est **bornée à la proposition** — jusqu'au dernier point ou
# point-virgule avant l'occurrence, cinquante caractères au plus. Un « jamais »
# d'une phrase antérieure ne couvre donc pas la suivante.
# ⚠ Les espaces des locutions sont écrits `\s+` : le corps est enroulé à 100
# colonnes, et « ne sont pas » y vit coupé en « ne sont\npas ». C'est le défaut
# exact que `check-sieges.py` avait payé deux fois sur ses signatures, et il
# s'est reproduit ici au premier passage — le ch. 30 échouait pour cela seul.
PROSCRIPTION = re.compile(
    r"jamais|\bnon\b|ne\s+sont\s+pas|n'est\s+pas|ne\s+se\s|plutôt\s+que|au\s+lieu\s+de|"
    r"proscri|interdi|écart(?:é|ée|és|ées)|à\s+éviter", re.I)


def enonce_la_proscription(texte, debut, fin):
    """Vrai si l'occurrence vit dans une proposition qui la proscrit."""
    amont = texte[max(0, debut - 50):debut]
    amont = re.split(r"[.;]", amont)[-1]
    return bool(PROSCRIPTION.search(amont + texte[debut:fin]))


FORMULATIONS = [
    {
        "id": "E-23 — « attendu par », jamais « exigé par »",
        "motif": r"exig(?:é|ée|és|ées|e|ent)\s+par\s+E-23",
        "forme": "« attendu par E-23 » (PRD §8 ; PRD Vol. II §7.3, PRDPlan Vol. II §4.4)",
    },
    {
        "id": "RTR — « quatre cibles successives », jamais « quatre reports »",
        "motif": r"quatre\s+reports",
        "forme": "« quatre cibles successives — 2019, 2022, 2023, 2026 » (R-4 du Vol. II)",
    },
    {
        # Ancré sur le jalon : « l'échéance était fixée au 2 août 2026 » (§ 30) et
        # « le décret, qui fixe des échéances » (§ 33) portent sur des textes
        # réglementaires, où la date EST fixée — R-11 ne les vise pas.
        "id": "jalons NIST — « visée », jamais « fixée »",
        "motif": r"jalons?[^.;»]{0,60}\bfix(?:é|ée|és|ées)\b"
                 r"|\b(?:NIST|post-quantiques?)\b[^.;»]{0,60}\bjalons?[^.;»]{0,30}\bfix",
        "forme": "« visée », statut du document porté (R-11 du Vol. III)",
    },
    {
        "id": "MCP — « cadre » d'autorisation, jamais « sécurisé »",
        "motif": r"MCP[^.;»]{0,60}\bs[ée]curis(?:é|ée|és|ées)\b"
                 r"|\bs[ée]curis(?:é|ée)\b[^.;»]{0,30}\bMCP\b",
        "forme": "« cadre d'autorisation » fondé sur OAuth (réserve F-01 du Vol. II)",
    },
]

# --------------------------------------------------------------------------
# P2 — ce qui n'est PAS un renvoi interne.
#
# Trois neutralisations, chacune avec son motif :
#  (a) « le ch. 21 du Vol. II », « Vol. III *Monographie* ch. 19 » désignent une
#      SOURCE, pas le compendium — sa numérotation lui est propre ;
#  (b) « les anciens ch. 55 et 56 » est une **correspondance gelée** : la
#      décision 13d du TOC interdit de la réécrire, et un contrôle qui la
#      signalerait pousserait à la corriger, c'est-à-dire à faire résoudre les
#      renvois gelés au mauvais chapitre ;
#  (c) « ch. 12 § 12.9 » du chapeau de titre vit hors du corps, comme le reste
#      de l'en-tête.
# --------------------------------------------------------------------------
RENVOI = re.compile(r"(.{0,70}?)\bch\.\s*(\d{1,3})\b(.{0,25})", re.S)
MARQUEUR_SOURCE = re.compile(r"Vol\.\s*I{1,3}\b|Monographie|Synthèse|PRDPlan")
CORRESPONDANCE_GELEE = re.compile(r"\bancien(?:s|ne|nes)?\s*$|\bfusion v0\.\d+\s*(?:des|du)\s*$")


def controler():
    echecs, rapport = [], []
    corpus = pieces()
    if not corpus:
        return ["Aucune pièce trouvée sous « Livre */ » — domaine vide, contrôle sans objet."], []

    alloues, resolus, connus = tables_du_socle()
    if alloues is None:
        echecs.append("[P4] socle-consolide.md est absent — les identifiants ne résolvent contre rien.")

    nus_par_piece, exclus_cites, decomptes_rapportes = {}, [], []

    for piece in corpus:
        nom = piece.relative_to(RACINE).as_posix()
        texte = piece.read_text(encoding="utf-8")
        tete = entete(texte)
        b = corps(texte)

        # ---- P1 : l'en-tête à cinq champs (PRD §6) --------------------
        # Un champ absent ou vide n'est pas un oubli de forme : c'est une
        # déclaration manquante — quel gel, quel socle, quel balayage.
        for champ in CHAMPS:
            if champ not in tete:
                echecs.append(f"[P1] {nom} : champ « {champ} » absent de l'en-tête.")
            elif not re.search(r"\w", tete[champ]):
                echecs.append(f"[P1] {nom} : champ « {champ} » vide.")

        # ---- P2 : les renvois « ch. N » résolvent dans 1-50 -----------
        for m in RENVOI.finditer(b):
            amont, n, aval = m.group(1), int(m.group(2)), m.group(3)
            if MARQUEUR_SOURCE.search(amont) or MARQUEUR_SOURCE.search(aval):
                continue
            if CORRESPONDANCE_GELEE.search(amont):
                continue
            if n not in CHAPITRES:
                echecs.append(
                    f"[P2] {nom} : renvoi « ch. {n} » hors du domaine 1-50 "
                    f"(plafond de cinquante, décision 13a du TOC).")

        # ---- P3 : identifiants de socle préfixés de leur volume -------
        # Segmentation par phrase, doctrine du contrôle C8 de `check-toc.py` :
        # la mention de volume gouverne la phrase où elle vit, pas le document.
        if "Vol. II" in b and "Vol. III" in b:
            nus = 0
            for seg in re.split(r"[.;|\n]", segments(sans_citations(b))):
                for m in re.finditer(r"\b[FH]-\d{2,3}[a-z]?\b", seg):
                    if "VOL2" not in seg and "VOL3" not in seg:
                        nus += 1
            if nus:
                nus_par_piece[nom] = nus

        # ---- P4 : les identifiants de socle résolvent -----------------
        if alloues is not None:
            for m in re.finditer(r"\bS-\d{1,4}\b", b):
                if m.group(0) not in alloues:
                    echecs.append(
                        f"[P4] {nom} : « {m.group(0)} » n'est alloué par aucune entrée de "
                        f"socle-consolide.md — source unique des identifiants S-nnn.")
            for m in re.finditer(r"\b[FH]-\d{1,3}[a-z]?\b", b):
                ident = m.group(0)
                if ident not in connus:
                    echecs.append(
                        f"[P4] {nom} : « {ident} » ne résout contre aucune des deux tables "
                        f"de correspondance (socle-consolide.md §4 et §5).")
                elif ident not in resolus:
                    exclus_cites.append((nom, ident))

        # ---- P5 : les décomptes de l'en-tête se re-mesurent -----------
        if "Garde-fous balayés" in tete:
            vues, conflits = declarations(tete["Garde-fous balayés"])
            for ident, a, z in conflits:
                echecs.append(
                    f"[P5] {nom} : « {ident} » est déclaré deux fois au champ "
                    f"« Garde-fous balayés », à {a} puis à {z} — l'en-tête se contredit.")
            for ident, (n, ancre) in sorted(vues.items()):
                reel = len(re.findall(r"\b" + re.escape(ident) + r"\b", b))
                if reel == n:
                    continue
                ligne = f"{nom} : « {ident} » déclaré {n}, mesuré {reel} au corps"
                if ancre:
                    echecs.append(
                        f"[P5] {ligne} — décompte annoncé sur le marqueur littéral de "
                        f"l'identifiant (décision 16a du TOC).")
                else:
                    decomptes_rapportes.append(ligne)

        # ---- P7 : les formulations imposées du PRD §8 -----------------
        propre = sans_citations(b)
        for f in FORMULATIONS:
            for m in re.finditer(f["motif"], propre, re.I):
                if enonce_la_proscription(propre, m.start(), m.end()):
                    continue
                echecs.append(
                    f"[P7] {nom} : « {m.group(0).strip()[:60]} » — forme proscrite. "
                    f"Écrire {f['forme']}.")

    # ---- P6 : le registre de gel est aligné pièce à pièce -------------
    echecs += controler_registre(corpus)

    # ---- P8 : le seuil de J-IV-2 ---------------------------------------
    echecs += controler_resolution_du_toc()

    # ---- Les trois rapports déclaratifs -------------------------------
    #
    # ⚠ Aucun des trois n'est un contrôle supprimé : chacun est mesuré, chiffré,
    # et porte sa condition de réactivation. *Un contrôle bruyant est un
    # contrôle ignoré ; un contrôle supprimé est une spécification.*
    if nus_par_piece:
        total = sum(nus_par_piece.values())
        rapport.append(
            f"[P3 — DÉCLARATIF] {total} emplois nus de « F-xx » ou « H-xx » dans le corps de "
            f"{len(nus_par_piece)} pièces mixtes (décision 7 du TOC : un F-xx nu est indécidable "
            f"entre deux socles).\n"
            f"    ⚠ **P3 est déclaratif, et le motif est mesuré, non commode** : le préfixe y est "
            f"le plus souvent porté par l'en-tête de la rangée, du tableau ou du paragraphe — "
            f"une portée que la segmentation par phrase ne voit pas —, et opposer les "
            f"{total} occurrences ferait échouer trente pièces qu'aucune passe n'a mandat de "
            f"corriger. **Réactivation** : après le versement des identifiants consolidés S-nnn "
            f"au corps des pièces (porte G-3, §7.1 du PRD), qui rend la question sans objet.\n"
            + "\n".join(f"      {v:4d}  {k}" for k, v in
                        sorted(nus_par_piece.items(), key=lambda x: -x[1])))
    if exclus_cites:
        rapport.append(
            f"[P4 — DÉCLARATIF] {len(exclus_cites)} citations d'entrées **connues mais non "
            f"versées** au socle consolidé (§6 du socle : dette de vote non résorbée F-92 et "
            f"F-96 ; hors socle factuel H-13, H-15, H-16).\n"
            f"    Ce n'est pas un défaut de pièce : le PRD §7.1 les tient pour **citables avec "
            f"leur réserve, jamais versables**, et les pièces concernées portent la réserve. "
            f"L'écart devient bloquant le jour où l'une d'elles porte une thèse.\n"
            + "\n".join(f"      {n}  ←  {i}" for n, i in exclus_cites))
    if decomptes_rapportes:
        rapport.append(
            f"[P5 — DÉCLARATIF] {len(decomptes_rapportes)} cardinaux d'en-tête que le décompte "
            f"du **marqueur d'identifiant** ne reproduit pas.\n"
            f"    ⚠ La décision 16a admet **deux marqueurs** : l'identifiant (« R-14 ») ou la "
            f"formule (« degré 3 », « fait négatif vérifié », « PROJETÉ »). Ces cardinaux-ci "
            f"portent sur la formule, que le script ne sait pas dériver de l'identifiant — il "
            f"les mesure sans les opposer. **Réactivation** : quand chaque déclaration nommera "
            f"le marqueur qu'elle compte, comme les pièces des ch. 25, 32 et 39 le font déjà "
            f"(« occurrences du sigle »).\n"
            + "\n".join(f"      {x}" for x in decomptes_rapportes))

    return echecs, rapport


def segments(texte):
    """Masque les points non terminaux avant la segmentation par phrase.

    Sans ce masquage, « Vol. II » serait coupé de son identifiant et le contrôle
    fabriquerait des faux positifs à chaque mention de volume. Repris tel quel
    de `sentence_segments` de `check-toc.py` : *deux implémentations de la même
    segmentation divergeraient, et le désaccord serait invisible.*
    """
    texte = texte.replace("Vol. III", "VOL3").replace("Vol. II", "VOL2").replace("Vol. I", "VOL1")
    texte = re.sub(r"(?<=\d)\.(?=\d)", "_", texte)
    return re.sub(r"\b(ch|art|juill|janv|févr|avr|sept|oct|nov|déc)\.", r"\1_", texte)


def normalise(chaine):
    """Repli des accents et de la casse — « juill. » et « juillet » restent distincts."""
    plat = unicodedata.normalize("NFD", chaine.lower())
    return "".join(c for c in plat if unicodedata.category(c) != "Mn")


MOIS = ["janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


def date_de_gel(valeur):
    """« **27 juillet 2026** — gel unique… » → « 27 juillet 2026 »."""
    m = re.search(r"(\d{1,2})\s*(?:ᵉʳ)?\s+(" + "|".join(MOIS) + r"|" +
                  "|".join(x[:5] + r"\." for x in MOIS) + r")\s+(20\d\d)", valeur, re.I)
    if not m:
        return None
    mois = normalise(m.group(2)).rstrip(".")
    plein = next((x for x in MOIS if normalise(x).startswith(mois)), mois)
    return f"{int(m.group(1))} {plein} {m.group(3)}"


def controler_registre(corpus):
    """P6 — une ligne par pièce, date de gel et volumétrie concordantes.

    ⚠ **Ce contrôle ne mesure pas la volumétrie : il la confronte.** La seule
    autorité de décompte du volume est `decompte.sh` (PRD §9, porte G-2), et
    porter ici un second tokéniseur créerait une seconde autorité — c'est-à-dire
    une divergence qui attend. Le registre porte la mesure ; ce contrôle vérifie
    qu'elle **concorde avec ce que la pièce déclare**, ce que le PRD §9 demande
    en toutes lettres : *« se re-vérifie contre l'en-tête de la pièce avant tout
    usage »*.
    """
    if not REGISTRE.exists():
        return ["[P6] PRD/registre-gel.md est absent — condition de sortie (e) de la porte G-3."]

    lignes = {}
    for ligne in REGISTRE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*\d+\s*\|[^|]*\|\s*\[`([^`]+)`\][^|]*\|([^|]*)\|([^|]*)\|"
                     r"([^|]*)\|([^|]*)\|", ligne)
        if m:
            lignes[m.group(1)] = [x.strip() for x in m.groups()[1:]]

    echecs = []
    attendus = {p.relative_to(RACINE).as_posix() for p in corpus}
    for orpheline in sorted(set(lignes) - attendus):
        echecs.append(f"[P6] registre-gel.md : ligne « {orpheline} » sans pièce correspondante.")

    for piece in corpus:
        nom = piece.relative_to(RACINE).as_posix()
        if nom not in lignes:
            echecs.append(f"[P6] {nom} : aucune ligne au registre de gel.")
            continue
        _, gel_reg, cible_reg, reel_reg = lignes[nom]
        tete = entete(piece.read_text(encoding="utf-8"))

        gel_tete = date_de_gel(tete.get("Date de gel", ""))
        if gel_tete and date_de_gel(gel_reg) != gel_tete:
            echecs.append(f"[P6] {nom} : date de gel « {gel_reg} » au registre, "
                          f"« {gel_tete} » à l'en-tête.")

        volumetrie = tete.get("Volumétrie cible", "")
        m = re.search(r"[≈~]\s*\*{0,2}\s*([\d   ]+?)\s*\*{0,2}\s*mots", volumetrie)
        if m and nombre(cible_reg) != nombre(m.group(1)):
            echecs.append(f"[P6] {nom} : cible {cible_reg} au registre, "
                          f"{m.group(1).strip()} à l'en-tête.")

        # Vingt-six pièces publient leur mesure en tête ; vingt-quatre la
        # renvoient au README de leur Livre. Là où la pièce la publie, les deux
        # doivent coïncider — c'est le seul rapprochement que ce script fait
        # sans se doter d'un second tokéniseur.
        m = re.search(r"[Rr]éel[^:]{0,25}:\s*\*{0,2}\s*([\d   ]+?)\s*\*{0,2}\s*mots",
                      volumetrie)
        if m and nombre(reel_reg) != nombre(m.group(1)):
            echecs.append(f"[P6] {nom} : volumétrie réelle {reel_reg} au registre, "
                          f"{m.group(1).strip()} à l'en-tête.")
    return echecs


TOC = RACINE / "PRD" / "TOC.md"


def controler_resolution_du_toc():
    """P8 — le seuil que le jalon J-IV-2 énonce, rendu opposable.

    Le PRD §12 fixe pour sortie de J-IV-2 que « **100 % des F-xx cités par le
    TOC résolvent contre l'Annexe B** ». Tant que cette phrase n'a pas
    d'exécutable, c'est une spécification et non un seuil — *un contrôle dont
    l'exécutable n'est pas versionné est une spécification, pas un contrôle*.

    Deux décisions de lecture, écrites parce qu'elles ne vont pas de soi.

    **(1) « Résoudre » inclut résoudre vers une EXCLUSION DÉCLARÉE.** Cinq
    identifiants sont connus du socle sans y être versés — `F-92` et `F-96`
    (dette de vote), `H-13`, `H-15`, `H-16` (hors socle factuel) —, plus les
    trois non attribués `F-12` à `F-14`. Un renvoi vers eux **n'est pas
    pendant** : il tombe sur une rangée qui dit ce qu'ils sont et pourquoi ils
    ne sont pas versés. *C'est même la valeur propre de l'Annexe B : elle
    répond aussi des entrées qu'elle refuse.* Exiger un `S-nnn` ferait échouer
    le seuil sur les deux entrées que le socle a délibérément écartées — un
    contrôle qui punit la déclaration d'une exclusion enseigne à ne pas la
    déclarer.

    **(2) Les zones gelées du TOC sont hors domaine.** Les rangées
    d'historique et les journaux citent les identifiants **de leur passe** et
    ne se corrigent jamais (règle du fichier). Les y opposer rendrait le
    contrôle faux à chaque version : mêmes exemptions que `check-toc.py`.
    """
    if not TOC.exists():
        return ["[P8] `PRD/TOC.md` est absent — le seuil de J-IV-2 n'est pas mesurable."]
    _, _, connus = tables_du_socle()
    if connus is None:
        return ["[P8] `PRD/socle-consolide.md` est absent — le seuil de J-IV-2 "
                "n'est pas mesurable."]
    lignes = [l for l in TOC.read_text(encoding="utf-8").splitlines()
              if not l.startswith("| Historique")]
    zone = "\n".join(lignes).split("## Journal v0.")[0]
    cites = set(re.findall(r"(?<![\w-])([FH]-\d+b?)(?![\w-])", zone))
    pendants = sorted(cites - connus)
    if pendants:
        return [f"[P8] {len(pendants)} identifiant(s) de socle cité(s) par le TOC ne résolvent "
                f"pas contre l'Annexe B — {', '.join(pendants)}. Seuil de J-IV-2 : "
                f"{len(cites & connus)}/{len(cites)}."]
    return []


def main():
    echecs, rapport = controler()
    for bloc in rapport:
        print(bloc)
        print()
    if echecs:
        print(f"ÉCHEC — {len(echecs)} écart(s) :")
        for e in echecs:
            print(f"  {e}")
        return 1
    print(f"OK — les {len(pieces())} pièces tiennent (P1-P8), "
          f"{len(rapport)} rapport(s) déclaratif(s) ci-dessus.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
