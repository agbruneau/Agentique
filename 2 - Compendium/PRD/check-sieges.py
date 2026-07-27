#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle inter-pièces des sièges du compendium (Vol. IV).

Ce script solde les remontées **R-IV-05** (socle IAM posé une seule fois au ch. 3)
et **R-IV-09** (encadré R-8 posé une seule fois au ch. 7 § 7.5), qui déclaraient
toutes deux la même dette : *aucun contrôle outillé ne vérifie l'abstention.*
`check-toc.py` ne lit pas les pièces ; `verifier-piece.py` n'en connaît qu'une à
la fois. Le contrôle qui manquait est celui qui les lit **ensemble**.

⚠ **Ce script est du contenu : il se vérifie comme le reste.** Toute modification
se valide par mutation — constat de passage sur le corpus intact, puis chaque
classe de faute introduite et détectée. Le harnais est `check-sieges-mutations.py`.

Ce qu'un siège est, et ce qu'il n'est pas
----------------------------------------
Un **siège** est le lieu unique où une matière est posée pour toute la somme.
C'est l'économie qui justifie la refonte des trois volumes en un ouvrage : chaque
chapitre aval qui **reconstruit** annule cette économie. Un chapitre aval peut
**renvoyer** autant qu'il veut — c'est même ce qu'on attend de lui.

Le script ne sait pas lire le sens. Il ne détecte donc pas « la même matière
redite autrement » : il détecte la **signature de forme** d'un siège reproduite
ailleurs (un tableau, un intitulé de section), et l'**absence de renvoi** dans une
pièce qui touche la matière. C'est un filet, pas une preuve — la collation de
fond (porte G-4) reste due, et ce script ne la remplace pas.

Domaine : toutes les pièces `NN-slug.md` sous `2 - Compendium/Livre */`.
Sortie 0 si tout passe, 1 sinon.
"""

import os
import re
import sys
from pathlib import Path

# « 2 - Compendium ». La variable d'environnement n'existe que pour le harnais de
# mutation, qui doit pouvoir pointer une copie du corpus : muter le corpus réel
# pour éprouver son contrôle est le genre de raccourci qui laisse une trace.
RACINE = Path(os.environ.get("COMPENDIUM_RACINE", Path(__file__).resolve().parent.parent))

# La console Windows par défaut est en cp1252 et ne sait pas écrire « § » ni « É ».
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# --------------------------------------------------------------------------
# La table des sièges. C'est la seule chose à modifier quand un siège s'ajoute.
#
#   fichier      — la pièce qui porte le siège (relative à « 2 - Compendium »)
#   section      — l'intitulé du siège, tel que le renvoi doit le nommer
#   marqueur     — le motif qui prouve que le siège se déclare comme tel
#   signature    — motifs dont la présence HORS du siège vaut reconstruction ;
#                  TOUS doivent être présents pour conclure (un seul serait bruyant)
#   declencheur  — motif indiquant qu'une pièce TOUCHE la matière du siège
#   renvoi       — motif prouvant qu'elle renvoie au siège plutôt que de le refaire
# --------------------------------------------------------------------------
SIEGES = [
    {
        "id": "R-IV-09 — encadré de désambiguïsation à quatre branches (garde-fou R-8)",
        "fichier": "Livre I/07-genealogie-gouvernance.md",
        "section": "ch. 7 § 7.5",
        "marqueur": r"SIÈGE DU GARDE-FOU R-8 POUR TOUTE LA SOMME",
        "signature": [
            r"^\|\s*\*\*\(a\)\*\*",
            r"^\|\s*\*\*\(b\)\*\*",
            r"^\|\s*\*\*\(c\)\*\*",
            r"^\|\s*\*\*\(d\)\*\*",
        ],
        "declencheur": r"\bACP\b",
        "renvoi": r"ch\.\s*7\s*§\s*7\.5",
    },
    {
        "id": "R-IV-05 — socle IAM (identité fédérée, autorisation déléguée, zero-trust)",
        "fichier": "Livre I/03-securite-identite-gouvernance.md",
        "section": "ch. 3 § 3.2 et § 3.3",
        "marqueur": r"SIÈGE DU SOCLE IAM POUR TOUTE LA SOMME",
        # Reconstruire le socle IAM, c'est lui rouvrir des SECTIONS, pas le citer.
        # D'où l'ancrage sur les intitulés de section, jamais sur les termes nus :
        # « OAuth » cité dans une phrase est un renvoi ; « ### N.M OAuth… » est un siège bis.
        "signature": [
            r"^#{3,4}\s*\d+\.\d+(\.\d+)?\s.*\b(SAML|OpenID Connect|OAuth)\b",
            r"^#{2,4}\s*(§\s*)?\d+\.\d+(\.\d+)?\s.*\b([Zz]ero-trust|identité de charge de travail)\b",
        ],
        "declencheur": r"\b(identité fédérée|autorisation déléguée|identité de charge de travail)\b",
        # ⚠ Renvoi ancré au CHAPITRE, non à la section : le socle IAM couvre deux
        # sections (§ 3.2 et § 3.3), et une pièce qui écrit « posé une seule fois
        # au ch. 3 » renvoie correctement. Exiger « § 3.2 » ferait échouer le ch. 1,
        # qui renvoie proprement — un contrôle bruyant est un contrôle ignoré.
        "renvoi": r"ch\.\s*3\b",
    },
    {
        "id": "mécanique de la fusion de l'ACP protocolaire",
        "fichier": "Livre I/08-anatomie-mcp-a2a.md",
        "section": "ch. 8 § 8.5.1",
        "marqueur": r"SIÈGE DE LA MÉCANIQUE DE LA FUSION POUR TOUTE LA SOMME",
        "signature": [r"^#{3,4}\s*\d+\.\d+\.\d+\s+La convergence par fusion\s+—\s+mécanique"],
        "declencheur": r"convergence par fusion|fusion de l'ACP protocolaire",
        "renvoi": r"ch\.\s*8\s*§\s*8\.5\.1",
    },
]

# Les deux zones où un motif ne compte pas, et le motif du second n'est pas
# évident :
#
#  — la **note de statut** hors plan cite les sièges pour rendre compte ;
#  — l'**en-tête à cinq champs** DÉCLARE le balayage des garde-fous, il ne porte
#    pas la matière. Le champ « Garde-fous balayés » du ch. 1 énumère les sigles
#    dont il déclare **zéro emploi** — les y voir comme des emplois inverse
#    exactement le sens de la déclaration. Trois faux positifs neutralisés ici ;
#    les réintroduire en « simplifiant » rendrait le contrôle bruyant donc ignoré.
FIN_DE_CORPS = re.compile(r"^##\s*§?\s*[\d.]*\s*—?\s*Note de statut", re.M)
DEBUT_DE_CORPS = re.compile(r"^>\s|^##\s", re.M)


def corps(texte):
    """Le corps de la pièce : en-tête à cinq champs et note de statut exclus.

    Le corps commence à la thèse citée (bloc « > ») ou au premier titre de
    section, selon ce qui vient en premier — donc après le tableau d'en-tête.
    """
    debut = DEBUT_DE_CORPS.search(texte)
    texte = texte[debut.start():] if debut else texte
    coupe = FIN_DE_CORPS.search(texte)
    return texte[: coupe.start()] if coupe else texte


def pieces():
    """Toutes les pièces du compendium, triées, hors README."""
    trouvees = sorted(RACINE.glob("Livre */[0-9][0-9]-*.md"))
    return [p for p in trouvees if p.name != "README.md"]


def controler():
    echecs = []
    corpus = pieces()
    if not corpus:
        return ["Aucune pièce trouvée sous « Livre */ » — domaine vide, contrôle sans objet."]

    for siege in SIEGES:
        chemin = RACINE / siege["fichier"]
        nom = siege["id"]

        # ---- S1 : le siège existe -------------------------------------
        if not chemin.exists():
            echecs.append(f"[S1] {nom} : la pièce {siege['fichier']} est absente.")
            continue
        texte_siege = chemin.read_text(encoding="utf-8")

        # ---- S2 : le siège se déclare comme tel -----------------------
        # Sans marqueur, un rédacteur aval ne peut pas savoir qu'il en existe un ;
        # l'abstention qu'on lui demande devient une devinette.
        if not re.search(siege["marqueur"], texte_siege):
            echecs.append(
                f"[S2] {nom} : le siège ({siege['section']}) ne porte pas son marqueur "
                f"« {siege['marqueur']} »."
            )

        # ---- S3 : le siège porte bien sa propre signature -------------
        # Contrôle du contrôle : une signature qui ne voit plus son siège est
        # une signature périmée, et elle ne verrait pas non plus une copie.
        manquants = [m for m in siege["signature"]
                     if not re.search(m, corps(texte_siege), re.M)]
        if manquants:
            echecs.append(
                f"[S3] {nom} : la signature ne résout plus contre son propre siège "
                f"({len(manquants)} motif(s) sur {len(siege['signature'])} sans occurrence). "
                f"Le siège a changé de forme, ou la signature est périmée."
            )

        # ---- S4 : personne d'autre ne la porte ------------------------
        for piece in corpus:
            if piece == chemin:
                continue
            texte = corps(piece.read_text(encoding="utf-8"))
            if all(re.search(m, texte, re.M) for m in siege["signature"]):
                echecs.append(
                    f"[S4] {nom} : {piece.relative_to(RACINE)} porte la signature complète "
                    f"du siège — reconstruction. Renvoyer à {siege['section']}, ne pas refaire."
                )

        # ---- S5 : qui touche la matière renvoie au siège --------------
        for piece in corpus:
            if piece == chemin:
                continue
            texte = corps(piece.read_text(encoding="utf-8"))
            if re.search(siege["declencheur"], texte) and not re.search(siege["renvoi"], texte):
                echecs.append(
                    f"[S5] {nom} : {piece.relative_to(RACINE)} touche la matière "
                    f"(motif « {siege['declencheur']} ») sans renvoyer à {siege['section']}."
                )

    return echecs


def main():
    echecs = controler()
    if echecs:
        print(f"ÉCHEC — {len(echecs)} écart(s) :")
        for e in echecs:
            print(f"  {e}")
        return 1
    print(f"OK — les {len(SIEGES)} sièges tiennent sur {len(pieces())} pièces (S1-S5).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
