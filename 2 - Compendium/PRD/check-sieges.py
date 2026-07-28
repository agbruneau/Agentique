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
    # Deux marqueurs ORPHELINS du Livre II, versés le 28 juillet 2026 : déclarés
    # dans leur pièce — parfois désignés par le TOC — et jamais contrôlés. Un
    # marqueur sans entrée à cette table est un siège posé en DEUX gestes sur
    # trois : le lecteur aval est prévenu, l'appareil ne l'est pas.
    {
        "id": "siège du statut projeté de la normalisation du passeport",
        "fichier": "Livre II/16-passeport-agent.md",
        "section": "ch. 16 § 16.4",
        "marqueur": r"SIÈGE DU STATUT PROJETÉ DE LA NORMALISATION DU PASSEPORT POUR TOUTE LA SOMME",
        # Ce que le siège interdit de refaire n'est pas le mot « passeport » —
        # tout le chapitre le porte — mais le TRI des trois voies : re-dater
        # l'agenda, c'est réécrire les trois scénarios avec leur statut. D'où
        # l'ancrage sur les trois intitulés, jamais sur « PROJETÉ » nu, que le
        # siège du tri prospectif (ch. 49 § 49.0) régit déjà pour son compte.
        "signature": [
            r"Scénario\s+1\s+—\s+normalisation\s+par\s+extension",
            r"Scénario\s+2\s+—\s+assemblage\s+par\s+une\s+fondation",
            r"Scénario\s+3\s+—\s+préemption\s+par\s+le\s+produit",
        ],
        # ☑ S5 ACTIF, mesuré : UNE pièce hors siège touche la matière — le ch. 50
        # § 50.1, ligne « Normalisation du passeport d'agent » — et elle renvoie
        # « ch. 16 en entier ». ⚠ Renvoi ancré au CHAPITRE, non à la section, pour
        # cette raison exacte : exiger « § 16.4 » ferait échouer une pièce qui
        # renvoie proprement — même doctrine que le socle IAM ci-dessus.
        "declencheur": r"[Nn]ormalisation\s+du\s+passeport",
        "renvoi": r"ch\.\s*16\b",
    },
    {
        "id": "siège de la restriction du garde-fou R-08 (usurpation du justificatif propre)",
        "fichier": "Livre II/19-taxonomie-attaques-identite-delegation.md",
        "section": "ch. 19 § 19.6",
        "marqueur": r"SIÈGE DE LA RESTRICTION DU GARDE-FOU R-08 POUR TOUTE LA SOMME",
        # La restriction du 21 juillet 2026 est une FORMULATION, et c'est elle que
        # le siège pose une seule fois : l'objet étroit (le justificatif propre),
        # la définition de l'usurpation, et le degré. Les trois ensemble — la
        # troisième seule (« absence de documentation, non un fait négatif
        # vérifié ») est la formule générale du degré 3, que R-14 fait écrire
        # partout : la prendre pour signature ferait feu sur tout le corpus.
        "signature": [
            r"usurpation\s+du\s+justificatif\s+propre\s+d'un\s+agent",
            r"présentation\s+par\s+un\s+attaquant",
            r"se\s+faire\s+passer\s+pour\s+cet\s+agent",
        ],
        # ☑ S5 ACTIF, mesuré : TROIS pièces touchent la matière, les TROIS
        # renvoient (ch. 12, ch. 20 du Livre II ; ch. 50 du Livre V).
        # ⚠ Deux ancrages sont contraints ici, et pour deux motifs distincts.
        #  — Le RENVOI ne peut pas s'ancrer sur « R-08 » : les ch. 12 § 12.2 et
        #    ch. 20 § 20.0/§ 20.9 écrivent « son siège est le ch. 19 § 19.6 » et
        #    n'écrivent NULLE PART l'identifiant — le ch. 20 le déclare lui-même
        #    en en-tête, « le renvoi est de section, non d'identifiant ». Ancrer
        #    sur le sigle ferait échouer les deux pièces qui renvoient le mieux.
        #  — Il s'ancre au CHAPITRE et non au § 19.6 parce que le ch. 50 § 50.1
        #    renvoie « ch. 19 § 19.1 ; ch. 20 ; la portée de R-08 » : exact dans
        #    son périmètre, et exiger § 19.6 le ferait échouer.
        # ⚠ Le DÉCLENCHEUR ne peut pas s'écrire « usurpation du justificatif » :
        # le ch. 12 § 12.2 écrit « l'usurpation du **justificatif propre d'un
        # agent** », l'emphase tombant au milieu du motif. Même classe de défaut
        # que le retour à la ligne — un balisage inséré dans un motif multi-mots
        # le rend introuvable —, et il a été trouvé ici au premier passage.
        "declencheur": r"justificatif\s+propre\s+d'un\s+agent",
        "renvoi": r"ch\.\s*19\b",
    },
    # --------------------------------------------------------------- Livre III
    # Les NEUF sièges du Livre III, versés le 28 juillet 2026. Huit d'entre eux
    # étaient la dette déclarée au PRD §9 : le fichier était écrit en parallèle
    # par la rédaction des Livres IV et V le jour où le Livre III s'est clos, et
    # *payer une dette d'outillage pendant qu'un autre écrit le même fichier
    # produirait une table incohérente que le harnais ne détecterait pas.* Les
    # passes concurrentes sont closes ; la dette se paie. Le neuvième — la grille
    # d'architecture des plateformes P&C — a reçu ses renvois entrants depuis.
    # ⚠ Les formes FRANÇAISES font foi : le TOC v0.29 s'est réaligné sur les
    # pièces (« critère anti-emballement », « quatre-yeux »), une signature sous
    # un nom que le plan déclare sous un autre étant la classe d'indécidabilité
    # que la décision 7 proscrit.
    {
        "id": "siège du patron d'irréversibilité (finalité du règlement)",
        "fichier": "Livre III/31-vertical-financier-durcisseurs.md",
        "section": "ch. 31 § 31.1.1",
        "marqueur": r"SIÈGE DU PATRON D'IRRÉVERSIBILITÉ POUR TOUTE LA SOMME",
        # Ce que le siège interdit de refaire est l'ÉNONCÉ COMPOSÉ qui borne la
        # saga : le fait ne se rétracte pas, donc aucune compensation
        # déterministe, donc un recouvrement. « Irréversible » nu se cite
        # partout à bon droit — au ch. 4 sur l'outil, au ch. 44 sur l'étape
        # modélisée : l'ancrer serait rendre le contrôle bruyant donc ignoré.
        "signature": [
            r"ne\s+se\s+rétractent\s+pas\s+par\s+simple\s+instruction\s+inverse",
            r"aucune\s+compensation\s+déterministe",
            r"recouvrement\s+incertain\s+et\s+coûteux",
        ],
        # ⚠ S5 DÉSACTIVÉ, et le motif est mesuré, non commode : DEUX pièces hors
        # siège touchent la matière sous sa forme composée, UNE renvoie (ch. 34
        # du Livre III), UNE ne renvoie pas — le **ch. 49 § 49.10** du Livre V,
        # dont le scénario de rupture écrit « l'irréversibilité du règlement
        # interdirait la correction a posteriori » en renvoyant à § 49.9 et au
        # ch. 48 § 48.4, jamais au ch. 31. ⚠ **Le marqueur du siège lui-même est
        # en écart** : re-mesuré le 28 juillet 2026, il énumère ses renvois
        # entrants sans nommer le ch. 49. Remontée : instruire l'écart au ch. 49
        # ET au relevé du siège, PUIS remplacer None par r"ch\.\s*31\b".
        # *Un siège contrôlé contre la reconstruction mais non contre l'omission
        # de renvoi est à moitié contrôlé, et cela se déclare.*
        "declencheur": r"irréversibilité\s+du\s+règlement|patron\s+d'irréversibilité",
        "renvoi": None,
    },
    {
        "id": "siège du risque systémique (agents corrélés)",
        "fichier": "Livre III/31-vertical-financier-durcisseurs.md",
        "section": "ch. 31 § 31.1.2",
        "marqueur": r"SIÈGE DU RISQUE SYSTÉMIQUE POUR TOUTE LA SOMME",
        # Le siège pose la CHAÎNE causale du risque macro — uniformité des
        # modèles, donc corrélation des comportements, donc mimétisme, donc
        # événements auto-amplifiés. Les trois ensemble ; « risque systémique »
        # nu est la forme normale d'un renvoi.
        "signature": [
            r"corrélation\s+des\s+comportements",
            r"mimétisme",
            r"auto-amplifiés",
        ],
        # ⚠ S5 DÉSACTIVÉ, motif mesuré : DEUX pièces touchent, UNE renvoie
        # (ch. 34), UNE ne renvoie pas — le **ch. 49 § 49.10**, dont le
        # paragraphe « Le risque systémique des agents corrélés » reprend la
        # matière depuis le Vol. I sans nommer le ch. 31. ⚠ **Le marqueur du
        # siège affirme le contraire** : re-mesuré le 28 juillet 2026, il écrit
        # « aucune autre pièce de la somme ne le consomme » — énoncé que ce
        # contrôle réfute. *Le premier passage d'un contrôle inter-pièces trouve
        # les écarts qu'aucune pièce ne peut voir seule ; celui-ci en est un.*
        # Remontée : instruire les deux, PUIS remplacer None par r"ch\.\s*31\b".
        "declencheur": r"risque\s+systémique",
        "renvoi": None,
    },
    {
        "id": "siège du patron-signature de la double-qualification (modèle ET tiers TIC)",
        "fichier": "Livre III/31-vertical-financier-durcisseurs.md",
        "section": "ch. 31 § 31.1.4",
        "marqueur": r"SIÈGE DU PATRON-SIGNATURE POUR TOUTE LA SOMME",
        # Reconstruire ce siège, c'est reposer le SECOND régime en entier — les
        # trois obligations de résilience opérationnelle qui font du même agent
        # un tiers TIC. Le ch. 30 l'INSTANCIE et le déclare (« ne faire que
        # l'instancier ») : il cite le régime, il ne le re-dérive pas.
        "signature": [
            r"registre\s+des\s+tiers\s+technologiques",
            r"risque\s+de\s+concentration",
            r"stratégie\s+de\s+sortie\s+testée",
        ],
        # ☑ S5 ACTIF : DEUX pièces touchent, les DEUX renvoient (ch. 30 et ch. 34
        # du Livre III). Renvoi ancré à la SECTION — les deux l'écrivent ainsi.
        "declencheur": r"double-qualification",
        "renvoi": r"ch\.\s*31\s*§\s*31\.1\.4",
    },
    {
        "id": "siège du critère anti-emballement (serveurs d'outils sectoriels)",
        "fichier": "Livre III/31-vertical-financier-durcisseurs.md",
        "section": "ch. 31 § 31.2.6",
        "marqueur": r"SIÈGE DU CRITÈRE ANTI-EMBALLEMENT POUR TOUTE LA SOMME",
        # Le critère tient dans une TABLE de trois lignes qui départage ce qu'on
        # annonce de ce que c'est. La refaire, c'est re-arbitrer le critère ;
        # écrire « aucun serveur sectoriel ratifié » est un renvoi.
        "signature": [
            r"^\|\s*\*\*Adoption\s+interne\*\*",
            r"^\|\s*\*\*Outillage\s+de\s+développement\*\*",
            r"^\|\s*\*\*Serveur\s+d'exécution\s+en\s+disponibilité\s+générale\*\*",
        ],
        # ☑ S5 ACTIF : UNE pièce touche, elle renvoie (ch. 34, cinq fois).
        # ⚠ Le déclencheur ne peut PAS s'écrire « anti-emballement » nu : le
        # ch. 49 § 49.0 emploie « garde-fou anti-emballement » et « discipline
        # anti-emballement » pour un TOUT AUTRE objet — la règle du tri
        # prospectif, dont le siège est ailleurs. Homonymie mesurée, écartée par
        # l'ancrage sur « critère » et « siège », les deux formes que les pièces
        # qui visent CE siège emploient.
        "declencheur": r"(critère|siège)\s+anti-emballement",
        "renvoi": r"ch\.\s*31\s*§\s*31\.2\.6",
    },
    {
        "id": "siège du patron du quatre-yeux (indépendance anti-collusion)",
        "fichier": "Livre III/31-vertical-financier-durcisseurs.md",
        "section": "ch. 31 § 31.3.4",
        "marqueur": r"SIÈGE DU PATRON DU QUATRE-YEUX POUR TOUTE LA SOMME",
        # ⚠ Première signature de ce siège, RETIRÉE au premier passage : ancrée
        # sur les trois termes « préparateur-vérificateur », « indépendance
        # d'exécution » et « canal latéral », elle déclarait le ch. 34 en
        # reconstruction (S4). Or le ch. 34 renvoie SIX FOIS au § 31.3.4 : il
        # applique le patron en le nommant. *Trois termes dispersés dans un
        # chapitre ne sont pas une reconstruction* — d'où l'ancrage sur les
        # ÉNONCÉS composés : la règle d'asymétrie, et deux des trois conditions
        # d'étanchéité qui la rendent opposable.
        "signature": [
            r"l'agent\s+qui\s+propose\s+ne\s+doit\s+jamais\s+être\s+l'agent",
            r"liés\s+à\s+des\s+identités\s+distinctes",
            r"ne\s+partager\s+aucun\s+canal\s+latéral",
        ],
        # ⚠ S5 DÉSACTIVÉ, motif mesuré : DEUX pièces touchent, UNE renvoie
        # (ch. 34), UNE ne renvoie pas — le **ch. 44 § 44.5**, qui écrit « le
        # contrôle à quatre yeux appelle une construction particulière,
        # justifiée ici une seule fois » et **ne cite le ch. 31 nulle part**
        # (zéro occurrence dans la pièce). ⚠ Ce qu'il construit est le RENDU
        # ArchiMate du patron — deux Roles, aucun Flow direct —, non le patron :
        # S4 ne tire donc pas, et c'est correct. *Mais une pièce qui déclare
        # justifier « une seule fois » une matière dont le siège est ailleurs
        # doit nommer ce siège.* Remontée : aligner le ch. 44, PUIS remplacer
        # None par r"ch\.\s*31\b".
        "declencheur": r"quatre[- ]yeux",
        "renvoi": None,
    },
    {
        "id": "siège du patron AML agentique (asymétrie d'autorité)",
        "fichier": "Livre III/31-vertical-financier-durcisseurs.md",
        "section": "ch. 31 § 31.4.3",
        "marqueur": r"SIÈGE DU PATRON AML AGENTIQUE POUR TOUTE LA SOMME",
        # Les deux propriétés qui expliquent la primauté du domaine, plus la
        # règle d'autorité qui en découle. Les trois ensemble : la troisième
        # seule est une formule d'asymétrie que plusieurs chapitres écrivent
        # légitimement sur d'autres matières.
        "signature": [
            r"saturé\s+d'alertes\s+à\s+fort\s+taux\s+de\s+faux\s+positifs",
            r"déclarations\s+d'opérations\s+suspectes",
            r"la\s+décision\s+de\s+déclarer\s+demeure\s+humaine",
        ],
        # ☑ S5 ACTIF : UNE pièce touche, elle renvoie (ch. 34).
        # ⚠ Le déclencheur ne peut PAS s'écrire « AML » ni « anti-blanchiment »
        # nus : mesuré, le sigle apparaît aux ch. 2 et ch. 3 du Livre I sur le
        # domaine PRÉ-agentique — le contrôle de conformité classique, qui n'est
        # pas la matière de ce siège. Deux échecs sur des pièces qui n'ont rien
        # à renvoyer : un contrôle bruyant est un contrôle ignoré.
        "declencheur": r"anti-blanchiment\s+agentique",
        "renvoi": r"ch\.\s*31\s*§\s*31\.4\.3",
    },
    # ⚠ Les deux pièces suivantes portent leur marqueur sous le mot « domicile »,
    # non sous « SIÈGE … POUR TOUTE LA SOMME ». La forme est celle de la pièce et
    # elle fait foi : normaliser le marqueur au motif que les autres sièges en
    # emploient un autre reviendrait à contrôler une chaîne que le corpus
    # n'écrit pas — c'est-à-dire à ne rien contrôler.
    {
        "id": "domicile de la grille de risque des identités non humaines",
        "fichier": "Livre III/24-passage-echelle-entreprise.md",
        "section": "ch. 24 § 24.3.4",
        "marqueur": r"Cette\s+sous-section\s+est\s+le\s+domicile\s+unique\s+de\s+cette\s+grille",
        # Reconstruire le domicile, c'est ré-énumérer les dix risques en nommant
        # l'instrument. D'où l'ancrage sur son nom exact et sur les deux bornes
        # de la liste — « identité non humaine » nu traverse tout le corpus.
        "signature": [
            r"Non-Human\s+Identities\s+Top\s+10",
            r"mise\s+hors\s+service\s+défaillante",
            r"usage\s+humain\s+d'une\s+identité\s+non\s+humaine",
        ],
        # ☑ S5 ACTIF, et VIDE aujourd'hui, ce qui n'est pas la même chose que
        # désactivé : mesuré, AUCUNE pièce hors ch. 24 ne nomme l'instrument —
        # le seul renvoi entrant, celui du § 24.6, est INTRA-pièce et invisible
        # à S5 par construction (S5 est un contrôle inter-pièces). Le contrôle
        # est donc armé pour la suite sans échouer aujourd'hui.
        # ⚠ Le déclencheur ne peut PAS s'écrire « OWASP » ni « Top 10 » : mesuré,
        # quatre autres pièces citent d'AUTRES listes du même éditeur. Ce siège
        # tient une grille nommée, pas un éditeur.
        "declencheur": r"Non-Human\s+Identities\s+Top\s+10",
        "renvoi": r"ch\.\s*24\b",
    },
    {
        "id": "domicile de l'application des permissions à la récupération",
        "fichier": "Livre III/24-passage-echelle-entreprise.md",
        "section": "ch. 24 § 24.4.2",
        "marqueur": (r"Cette\s+sous-section\s+est\s+le\s+domicile\s+unique\s+de\s+l'application"
                     r"\s+des\s+permissions\s+à\s+la\s+récupération"),
        # Le critère strict, le point d'architecture qui le rend opposable — le
        # filtrage DANS la recherche et non après —, et le second canal.
        "signature": [
            r"ne\s+doit\s+jamais\s+récupérer\s+ni\s+restituer\s+un\s+fragment",
            r"plus\s+proche\s+voisin\s+approximatif",
            r"mémoire\s+de\s+flotte",
        ],
        # ☑ S5 ACTIF et vide, même régime que le domicile ci-dessus : mesuré,
        # aucune pièce hors ch. 24 n'emploie « mémoire de flotte » ; le renvoi
        # entrant connu (§ 24.6) est intra-pièce.
        "declencheur": r"mémoire\s+de\s+flotte",
        "renvoi": r"ch\.\s*24\b",
    },
    {
        "id": "siège de la grille d'architecture des plateformes d'assurance de dommage",
        "fichier": "Livre III/34-sous-domaines-financiers.md",
        "section": "ch. 34 § 34.2.2",
        "marqueur": (r"Cette\s+sous-section\s+est\s+le\s+siège\s+de\s+la\s+grille\s+d'architecture"
                     r"\s+des\s+plateformes\s+d'assurance\s+de\s+dommage"),
        # La grille est une OPPOSITION à deux termes plus trois axes de décision.
        # Refaire l'opposition, c'est refaire la grille ; citer « portabilité du
        # modèle » seule ne l'est pas — d'où l'exigence des trois.
        "signature": [
            r"l'agent\s+est\s+embarqué\s+dans\s+le\s+cœur\s+de\s+police",
            r"le\s+cœur\s+est\s+exposé\s+comme\s+outil",
            r"\*\*portabilité\s+du\s+modèle\*\*",
        ],
        # ☑ S5 ACTIF et vide : les deux renvois entrants que la pièce déclare —
        # § 34.5.2 et § 34.5.6 — sont INTRA-pièce, donc hors du champ de S5 ;
        # mesuré, aucune pièce externe ne touche la matière. Armé pour la suite.
        "declencheur": r"grille\s+d'architecture\s+des\s+plateformes",
        "renvoi": r"ch\.\s*34\b",
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
        # ⚠ S5 reste DÉSACTIVÉ, mais le motif est RE-MESURÉ le 28 juillet 2026 et
        # il a bougé : QUATORZE pièces hors siège trient des énoncés prospectifs,
        # DIX renvoient au siège, QUATRE ne renvoient pas — ch. 12, 13, 19 et 20
        # du Livre II. Le relevé du versement en comptait six ; les passes de
        # correction ont aligné le ch. 25 du Livre III et le ch. 37 du Livre IV,
        # le ch. 18 a cessé d'employer le motif, et le ch. 12 est entré au
        # domaine. *Le compte diminue, il ne s'annule pas : quatre pièces du
        # Livre II emploient encore le tri sans nommer son siège.* Remontée
        # R-IV-68, toujours ouverte : aligner les quatre, PUIS réactiver en
        # remplaçant None par r"ch\.\s*49\b". *Un siège contrôlé contre la
        # reconstruction mais non contre l'omission de renvoi est à moitié
        # contrôlé, et cela se déclare.*
        "declencheur": r"\btri prospectif\b",
        "renvoi": None,
    },
    {
        "id": "siège du verrou sémantique et pragmatique (programme de recherche)",
        "fichier": "Livre V/49-horizon-frontiere-connaissance-verifiable.md",
        "section": "ch. 49 § 49.6",
        "marqueur": r"SIÈGE DU VERROU SÉMANTIQUE ET PRAGMATIQUE POUR TOUTE LA SOMME",
        # Le verrou est un CONSTAT composé — les standards excellent en bas de
        # pile et sont pauvres en haut — et sa conséquence : le passage d'un
        # contrat syntaxique à un contrat sémantique. « Sémantique » nu est le
        # vocabulaire propre du ch. 2 : l'ancrer ferait feu sur tout un chapitre
        # qui traite la matière à un autre grain et à un autre régime.
        "signature": [
            r"excellent\s+aux\s+niveaux\s+technique\s+et\s+syntaxique",
            r"contrat\s+syntaxique\s+à\s+un\s+contrat\s+sémantique",
        ],
        # ⚠ S5 DÉSACTIVÉ, et le motif mesuré est plus dur que prévu — il porte
        # sur le siège lui-même. Le siège DÉCLARE que « le ch. 2 (données et
        # sémantique), le ch. 9 (découverte) et le ch. 43 l'appliquent et y
        # renvoient » ; mesuré le 28 juillet 2026, cette déclaration est fausse
        # pour deux des trois : le **ch. 2 ne cite le ch. 49 nulle part** (zéro
        # occurrence), et le **ch. 43 n'emploie « verrou » nulle part**. Sur le
        # déclencheur retenu, QUATRE pièces touchent la matière, TROIS renvoient
        # (ch. 9 du Livre I ; ch. 24 et ch. 34 du Livre III), UNE ne renvoie pas
        # — le ch. 2, que le siège nomme pourtant en premier.
        # ⚠ Et la chaîne du siège n'existe nulle part ailleurs : « verrou
        # sémantique » et « 49.6 » ont ZÉRO occurrence hors de la pièce. *Un
        # siège qu'aucune pièce ne nomme est un siège que personne ne peut
        # respecter par autre chose que le hasard.* Remontée : aligner le ch. 2,
        # PUIS remplacer None par r"ch\.\s*49\b".
        "declencheur": r"interopérabilité\s+sémantique",
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
        # ⚠ S5 reste DÉSACTIVÉ, motif RE-MESURÉ le 28 juillet 2026 : CINQ pièces
        # hors siège emploient « points de contrôle obligatoires », QUATRE
        # renvoient (ch. 37, 38, 39, 45 du Livre IV), UNE ne le fait pas — le
        # ch. 17 du Livre II, inchangé depuis le versement. ⚠ Sa muette n'est pas
        # un oubli mais une HOMONYMIE, et la pièce la déclare elle-même en
        # en-tête : « un faux ami est déclaré — le “point de contrôle” du
        # glossaire du Vol. II traduit une notion de reprise sur incident et
        # n'est pas le “point de contrôle obligatoire” de son ch. 19 ; la
        # collision est signalée et non résolue (§ 17.4) ». *Son renvoi est exact
        # dans son périmètre* — il vise le ch. 19 du Vol. II, sa source, non le
        # ch. 43 de la somme. Aligner obligerait à toucher le corps d'une pièce
        # dont la volumétrie est publiée, périmant un cardinal contrôlé pour
        # satisfaire un motif. Remontée : trancher l'homonymie à la passe qui
        # rouvrira le Livre II, PUIS remplacer None par r"ch\.\s*43\b".
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
        # ⚠ S5 reste DÉSACTIVÉ, motif RE-MESURÉ le 28 juillet 2026, et la mesure
        # requalifie la dette plus qu'elle ne la réduit : SIX pièces hors siège
        # emploient « modèle de maturité », TROIS renvoient (ch. 24 du Livre III,
        # ch. 39 et ch. 41 du Livre IV), TROIS ne renvoient pas — et les trois ne
        # sont pas de même nature.
        #  — ch. 1 et ch. 9 du Livre I : HOMONYMIE mesurée, non omission. Leur
        #    § 1.2 s'intitule « Cadres de référence et modèles de maturité » et
        #    traite les échelles d'interopérabilité PRÉ-agentiques ; le ch. 9
        #    renvoie explicitement au ch. 1 § 1.2.2. *Autre objet, autre siège* —
        #    les aligner sur le ch. 43 serait introduire un renvoi faux.
        #  — ch. 34 du Livre III : seule muette de fond, et elle est motivée —
        #    la pièce déclare le modèle de maturité financier « hors périmètre :
        #    il va au Livre IV », renvoi de LIVRE et non de chapitre.
        # *La dette n'est donc pas de quatre pièces à aligner mais d'une seule à
        # préciser* ; le déclencheur, lui, reste homonymique et c'est ce qui
        # interdit d'armer S5. Remontée : préciser le renvoi du ch. 34 et borner
        # le déclencheur au modèle de maturité AGENTIQUE, PUIS remplacer None.
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
    # Deux marqueurs ORPHELINS du Livre IV, versés le 28 juillet 2026. Le second
    # était désigné « (SIÈGE) » par le TOC depuis la v0.16 sans qu'aucun
    # instrument ne le contrôle.
    {
        "id": "siège de la collision « fabrique » (décision 12c du TOC)",
        "fichier": "Livre IV/43-architecture-reference-couches.md",
        "section": "ch. 43 § 43.1",
        "marqueur": r"SIÈGE DE LA COLLISION « FABRIQUE » POUR TOUTE LA SOMME",
        # Ce que le siège pose est la DÉSAMBIGUÏSATION des deux étages, par ce
        # que chacun fait. Le mot « fabrique » nu est précisément ce que la
        # décision 12c autorise à employer quand le sens est déterminable de la
        # phrase : l'ancrer inverserait la règle qu'il s'agit de tenir.
        # ⚠ Ce siège départage DEUX emplois ; la table des QUATRE emplois du
        # mot vit au ch. 41 § 41.1, que ce chapitre déclare ne pas reconstruire.
        # Elle n'est pas versée ici : autre matière, autre siège, autre passe.
        "signature": [
            r"l'étage\s+qui\s+émet\s+l'identité",
            r"le\s+plan\s+qui\s+produit\s+l'agent",
        ],
        # ☑ S5 ACTIF : TROIS pièces touchent, les TROIS renvoient (ch. 24 du
        # Livre III, ch. 41 du Livre IV, ch. 49 du Livre V).
        "declencheur": r"fabrique\s+d'agents",
        "renvoi": r"ch\.\s*43\b",
    },
    {
        "id": "siège de la conformité traçable (chaîne de l'intention au substrat)",
        "fichier": "Livre IV/44-formalisation-archimate.md",
        "section": "ch. 44 § 44.6",
        "marqueur": r"SIÈGE DE LA CONFORMITÉ TRAÇABLE",
        # Reconstruire le siège, c'est refaire la CHAÎNE et son critère
        # d'auditabilité. D'où l'ancrage sur le stéréotype, sur le maillon
        # intermédiaire et sur le critère — « auditabilité » nu est un mot
        # courant du corpus, mesuré dans dix pièces.
        "signature": [
            r"regulatory-requirement",
            r"Course\s+of\s+Action",
            r"ne\s+demeure\s+orphelin",
        ],
        # ☑ S5 ACTIF : UNE pièce touche, elle renvoie (ch. 45 du Livre IV).
        "declencheur": r"Requirement\s+réglementaire",
        "renvoi": r"ch\.\s*44\b",
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
