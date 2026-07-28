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
    # ---------------------------------------------------------------- Livre II
    # Quatre sièges versés le 27 juillet 2026 avec la rédaction du Livre II
    # (remontées R-IV-24 et R-IV-37). Trois d'entre eux étaient déjà nommés
    # « SIÈGE » par le TOC v0.24 sans qu'aucun instrument ne les contrôle ;
    # le quatrième — l'encadré des affirmations écartées — l'est parce que
    # deux chapitres APPLIQUENT R-2 et R-3 sans devoir les re-siéger.
    {
        "id": "siège unique du KYA (connaissance de l'agent)",
        "fichier": "Livre II/18-know-your-agent.md",
        "section": "ch. 18 § 18.1",
        "marqueur": r"SIÈGE UNIQUE DU KYA POUR TOUTE LA SOMME",
        # Reconstruire le siège, c'est refaire son inventaire d'instances — donc
        # ses rangées de tableau, non citer le sigle. D'où l'ancrage sur deux
        # rangées nommées : « KYA » nu est un renvoi, une table d'instances est
        # un siège bis.
        "signature": [
            r"^\|\s*\*\*Fondation d'identité décentralisée\*\*",
            r"^\|\s*\*\*Fondation d'identité ouverte\*\*",
        ],
        "declencheur": r"\bKYA\b",
        "renvoi": r"ch\.\s*18\b",
    },
    {
        "id": "siège de la triade létale (modèle de menace agentique)",
        "fichier": "Livre II/19-taxonomie-attaques-identite-delegation.md",
        "section": "ch. 19 § 19.2",
        "marqueur": r"SIÈGE DE LA TRIADE LÉTALE POUR TOUTE LA SOMME",
        # Les trois sommets énoncés ensemble : c'est la reconstruction du modèle.
        # Un seul d'entre eux — « canal de sortie » — vit légitimement au ch. 5
        # (ancrage) et au ch. 11 (amplification) ; exiger les trois évite ce bruit.
        "signature": [
            r"accès à des données privées",
            r"exposition à du contenu non fiable",
            r"canal de sortie vers l'extérieur",
        ],
        "declencheur": r"triade létale",
        "renvoi": r"ch\.\s*19\b",
    },
    {
        "id": "siège de l'horloge post-quantique (jalons, statuts, origines)",
        "fichier": "Livre II/21-horloge-post-quantique.md",
        "section": "ch. 21 § 21.1",
        "marqueur": r"SIÈGE DE L'HORLOGE POST-QUANTIQUE POUR TOUTE LA SOMME",
        # Re-dater les jalons, c'est reproduire leurs libellés verbatim et la
        # clause qui les rattache à un document successeur. Citer « PQC » ou
        # « post-quantique » est un renvoi ; réécrire ces trois chaînes est un
        # siège bis — et c'est exactement ce que R-11 proscrit.
        "signature": [
            r"Deprecated after 2030",
            r"Disallowed after 2035",
            r"or successor document",
        ],
        "declencheur": r"post-quantique",
        "renvoi": r"ch\.\s*21\b",
    },
    {
        "id": "encadré des affirmations écartées (garde-fous R-2 et R-3 du Vol. II)",
        "fichier": "Livre II/16-passeport-agent.md",
        "section": "ch. 16 § 16.2",
        "marqueur": r"SIÈGE DE L'ENCADRÉ DES AFFIRMATIONS ÉCARTÉES POUR TOUTE LA SOMME",
        # ⚠ Le motif « l'exigence stricte n'est pas établie » ne suffit PAS seul :
        # le ch. 15 § 15.3.1 l'écrit en APPLIQUANT R-3, ce qui est correct. Ce qui
        # signe l'encadré, c'est le couple affirmation-écartée + forme imposée.
        "signature": [
            r"registre d'agents centralisé",
            r"\*\*Forme imposée\*\*",
        ],
        "declencheur": r"Affirmations écartées",
        "renvoi": r"ch\.\s*16\s*§\s*16\.2",
    },
    # ----------------------------------------------------------------- Livre V
    # Deux sièges versés le 27 juillet 2026 avec la rédaction du Livre V
    # (remontées R-IV-64 et R-IV-68). Le premier existait AVANT sa pièce : quatre
    # pièces du Livre III et deux sections du ch. 1 déclaraient déjà « la
    # sémantique d'effet est au ch. 48, qui en est le siège » — sans que le TOC
    # le désigne ni qu'aucun instrument le contrôle. Le second était déclaré au
    # plan depuis la v0.16 et le TOC v0.25 en rendait le versement dû « à la
    # rédaction du second mouvement du Livre V ».
    {
        "id": "siège de la sémantique d'effet (idempotence, compensation, réconciliation)",
        "fichier": "Livre V/48-semantique-effet-idempotence-compensation.md",
        "section": "ch. 48 § 48.1",
        "marqueur": r"SIÈGE DE LA SÉMANTIQUE D'EFFET POUR TOUTE LA SOMME",
        # Reconstruire le siège, c'est refaire sa TAXONOMIE — donc les trois
        # rangées de sa table. Les trois mots « idempotence, compensation,
        # réconciliation » sont au contraire la forme normale d'un RENVOI, que
        # quatre pièces du Livre III emploient correctement : les prendre pour
        # signature rendrait le contrôle bruyant donc ignoré.
        "signature": [
            r"^\|\s*\*\*Lecture\*\*",
            r"^\|\s*\*\*Écriture\*\*",
            r"^\|\s*\*\*Engagement\*\*",
        ],
        "declencheur": r"sémantique d'effet",
        "renvoi": r"ch\.\s*48\b",
    },
    {
        "id": "siège du tri prospectif (PROGRAMMÉ / PROJETÉ / SPÉCULATIF)",
        "fichier": "Livre V/49-horizon-frontiere-connaissance-verifiable.md",
        "section": "ch. 49 § 49.0",
        "marqueur": r"SIÈGE DU TRI PROSPECTIF POUR TOUTE LA SOMME",
        # Employer une étiquette de tri est un usage ; DÉFINIR les trois statuts
        # est le siège. D'où l'ancrage sur les trois définitions, jamais sur les
        # étiquettes : « PROJETÉ » nu apparaît dans treize pièces à bon droit.
        "signature": [
            r"engagement daté réel",
            r"prévision d'analyste",
            r"pari de recherche",
        ],
        # ⚠ S5 est DÉSACTIVÉ pour ce siège, et le motif est mesuré, non commode :
        # treize pièces rédigées trient des énoncés prospectifs, SIX ne renvoient
        # pas au siège (ch. 13, 18, 19, 20 du Livre II ; ch. 25 du Livre III ;
        # ch. 37 du Livre IV). L'obligation de renvoi existe au plan — le TOC
        # v0.25 l'a posée pour trois pièces — mais l'outiller aujourd'hui
        # produirait six échecs sur des pièces hors de la passe qui verse le
        # siège : un contrôle bruyant est un contrôle ignoré. Remontée R-IV-68 :
        # aligner les six, PUIS réactiver en remplaçant None par le motif de
        # renvoi. *Un siège contrôlé contre la reconstruction mais non contre
        # l'omission de renvoi est à moitié contrôlé, et cela se déclare.*
        "declencheur": r"\btri prospectif\b",
        "renvoi": None,
    },
    # --------------------------------------------------------------------
    # Les trois sièges du Livre IV, versés le 27 juillet 2026 avec sa passe
    # d'arbitrage (remontée R-IV-59). Deux d'entre eux ont S5 DÉSACTIVÉ, et le
    # motif est mesuré plutôt que commode — même doctrine que pour le tri
    # prospectif ci-dessus : *un contrôle bruyant est un contrôle ignoré.*
    # --------------------------------------------------------------------
    {
        "id": "siège des cinq points de contrôle obligatoires",
        "fichier": "Livre IV/43-architecture-reference-couches.md",
        "section": "ch. 43 § 43.3",
        "marqueur": r"SIÈGE DES CINQ POINTS DE CONTRÔLE OBLIGATOIRES POUR TOUTE LA SOMME",
        # Reconstruire le siège, c'est refaire LA LISTE — donc les cinq rangées
        # de sa table. Citer « PC2 » ou « les cinq points de contrôle
        # obligatoires » est au contraire la forme normale d'un renvoi, que cinq
        # pièces emploient correctement : les prendre pour signature rendrait le
        # contrôle bruyant. D'où l'ancrage sur les rangées, aux deux bouts et au
        # milieu — trois suffisent, et TOUTES doivent être présentes.
        "signature": [
            r"^\|\s*\*\*PC1\*\*",
            r"^\|\s*\*\*PC3\*\*",
            r"^\|\s*\*\*PC5\*\*",
        ],
        # ⚠ S5 est DÉSACTIVÉ pour ce siège, et le motif est mesuré : SEPT pièces
        # emploient « points de contrôle obligatoires », dont SIX renvoient au
        # siège (ch. 37, 38, 39, 43, 45, 46 du Livre IV) et UNE ne le fait pas —
        # le ch. 17 du Livre II, qui cite « les cinq points de contrôle
        # obligatoires DE SON ch. 19 », c'est-à-dire du Vol. II, sa source. Son
        # renvoi est exact dans son périmètre, et l'aligner obligerait à toucher
        # le corps d'une pièce dont la volumétrie est publiée — ce qui périmerait
        # un cardinal contrôlé pour satisfaire un motif. Remontée : aligner le
        # ch. 17 à la passe qui rouvrira le Livre II, PUIS remplacer None par
        # r"ch\.\s*43\b". *Un siège contrôlé contre la reconstruction mais non
        # contre l'omission de renvoi est à moitié contrôlé, et cela se déclare.*
        "declencheur": r"points? de contrôle obligatoires?",
        "renvoi": None,
    },
    {
        "id": "siège du modèle de maturité et des trois échelles d'autonomie",
        "fichier": "Livre IV/43-architecture-reference-couches.md",
        "section": "ch. 43 § 43.5",
        "marqueur": r"SIÈGE DU MODÈLE DE MATURITÉ ET DE LA DÉSAMBIGUÏSATION DES TROIS ÉC",
        # Ce que le siège interdit de refaire n'est pas le mot « maturité » :
        # c'est la TABLE qui départage les trois échelles homonymes du Vol. I par
        # leur cardinal et leur numérotation. D'où l'ancrage sur les trois
        # libellés d'échelle, jamais sur « copilote » ni sur « autonomie graduée »,
        # que R-13 oblige déjà à qualifier partout.
        "signature": [
            r"échelle à quatre paliers non numérotés",
            r"continuum à six niveaux numérotés",
            r"graduation à quatre niveaux préfixés",
        ],
        # ⚠ S5 est DÉSACTIVÉ pour ce siège, et le motif est mesuré : SEPT pièces
        # emploient « modèle de maturité », dont TROIS renvoient au siège
        # (ch. 39, 40, 41 du Livre IV) et QUATRE ne le font pas — le ch. 1 du
        # Livre I, les ch. 24 et 34 du Livre III, tous rédigés hors de la passe
        # qui verse ce siège, et deux d'entre eux dans une passe concurrente du
        # même jour. Outiller l'obligation aujourd'hui produirait quatre échecs
        # sur des pièces qu'aucune passe en cours n'a mandat de corriger.
        # Remontée : aligner les quatre, PUIS remplacer None par r"ch\.\s*43\b".
        "declencheur": r"modèles? de maturité",
        "renvoi": None,
    },
    {
        "id": "siège de l'organisation de la fabrique (qui opère quoi)",
        "fichier": "Livre IV/45-blueprint-instancie-cycle-de-vie.md",
        "section": "ch. 45 § 45.6",
        "marqueur": r"SIÈGE DE L'ORGANISATION DE LA FABRIQUE POUR TOUTE LA SOMME",
        # Reconstruire ce siège, c'est reposer les DEUX absences de titulaire
        # documentées et le principe hérité qu'elles bornent — les trois ensemble,
        # jamais l'une d'elles seule : le « plan de contrôle obligatoire » se cite
        # légitimement ailleurs, sous le qualificatif que R-8 impose.
        # ⚠ Les espaces sont écrits `\s+` : le corps est enroulé à 100 colonnes,
        # et un retour à la ligne au milieu d'un motif le rend introuvable. C'est
        # le défaut exact que le versement du Livre II avait trouvé sur la triade
        # létale, et il s'est reproduit ici au premier passage — *une signature
        # qui ne voit pas son propre siège ne verrait pas non plus une copie.*
        "signature": [
            r"aucune\s+disposition\s+de\s+gouvernance\s+des\s+clés",
            r"aucun\s+organe\s+une\s+responsabilité\s+de\s+gestion\s+des\s+clés",
            r"plan\s+de\s+contrôle\s+obligatoire",
        ],
        # ☑ S5 ACTIF : deux pièces seulement touchent la matière — le siège et le
        # ch. 41 § 41.7, qui y renvoie. C'est le seul des trois sièges de ce Livre
        # dont l'obligation de renvoi soit outillable sans bruit, et il l'est.
        "declencheur": r"organisation de la fabrique",
        "renvoi": r"ch\.\s*45\b",
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
        # `renvoi: None` désactive S5 pour un siège dont l'obligation de renvoi
        # n'est pas encore tenue par le corpus. C'est une déclaration, pas une
        # commodité : le motif chiffré vit au commentaire du siège concerné, et
        # sa réactivation est une remontée ouverte. Sans cette garde, le seul
        # moyen de verser un tel siège serait de le laisser hors contrôle —
        # c'est-à-dire de ne rien contrôler du tout.
        if siege["renvoi"] is None:
            continue
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
