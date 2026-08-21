#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contenu des dix-neuf figures du traité, et leur rendu.

    python figures/contenu.py            # écrit les SVG dans figures/
    python figures/contenu.py --md       # réémet les lignes Markdown à insérer

⚠ RIEN QUI NE SOIT DANS LE TEXTE. Chaque entrée porte le `source` d'où son
contenu est tiré, et les figures dérivées d'un tableau en reprennent les
libellés à la lettre. Une figure qui ajouterait une information au chapitre
serait un énoncé sans siège.

⚠ CHAQUE ENTRÉE PORTE SA RÉSERVE — ce que la figure refuse de laisser croire.
C'est la discipline du traité portée à l'image : chaque mécanisme y nomme sa
condition d'échec, chaque transposition y nomme ce qu'elle casse. `dessine.rendu`
refuse une entrée qui n'en a pas, et ce refus est délibéré.
"""
import math
import sys

import dessine as d

FIGURES = []


def f(rang, nom, legende, alt, source, type, reserve, data):
    FIGURES.append(dict(rang=rang, nom=nom, legende=legende, alt=alt,
                        source=source, type=type, reserve=reserve, data=data))


# ============================================================== Introduction
f("0", "f-00-deplacement",
  "Le déplacement que l'ouvrage soutient : ce que la coordination par le milieu achète, et ce qu'elle coûte.",
  "Deux panneaux comparant le regime de l'accord et le regime du milieu evenementiel.",
  "Introduction.", "paire",
  "Le point partagé n'est pas détruit, il est transporté dans le milieu, qui devient le composant "
  "que chaque agent touche, qu'il faut répliquer, exploiter et facturer. La thèse est un déplacement, "
  "non une suppression — et le milieu est le candidat le plus sérieux au titre de point de défaillance "
  "unique que la décentralisation prétendait supprimer.",
  dict(titre_g="RÉGIME DE L'ACCORD", titre_d="RÉGIME DU MILIEU", accent_d=True,
       gauche=("Les agents négocient une décision", [
           "Porter un changement à toute la population coûte un nombre quadratique de messages.",
           "L'émetteur nomme le destinataire : il entretient une vue des membres vivants, "
           "qui est toujours une approximation et jamais un fait.",
           "Un tour vaut un aller simple, et n'a de sens que sous hypothèse synchrone.",
           "Un seul processus fautif par arrêt suffit à retirer la terminaison en asynchrone [1].",
       ], "Ce qu'il tient : un invariant global, à tout instant."),
       droite=("Les agents déposent et lisent des traces", [
           "Une écriture et une lecture par agent ; le diamètre du graphe de coordination "
           "vaut 2 quel que soit le nombre d'agents.",
           "Le producteur n'a pas de destinataire à connaître.",
           "Un tour de journal vaut la latence de queue ℓ₉₉ du chemin écriture-durabilité-lecture.",
           "La sérialisation, que la matière assurait sans protocole, devient un composant à payer.",
       ], "Ce qu'il tient : une décision révocable, sous ordre partiel.")))

# ================================================================= Chapitre 1
f("1.2", "f-01-2-correspondance",
  "La substitution terme à terme de la stigmergie au journal : les quatre correspondances, ce qui survit, et ce qui ne survit pas.",
  "Tableau de correspondance entre les composantes de la stigmergie biologique et celles "
  "d'un journal partitionne.",
  "§ 1.2, chapitre 1.", "matrice",
  "Un partitionnement par hachage détruit la proximité qu'un partitionnement par intervalle "
  "préserverait, au prix d'un point chaud. La perte du gradient est la première rupture de la "
  "transposition, et elle décide de la conception du sujet plus sûrement que n'importe quel "
  "choix de bibliothèque.",
  dict(titre="CE QUE LA SUBSTITUTION CONSERVE, ET CE QU'ELLE DÉTRUIT", lx=104,
       colonnes=["Essaim biologique — Grassé, Heylighen [4][9]",
                 "Essaim logiciel — journal partitionné"],
       rangees=["Trace", "Milieu", "Voisinage", "Évaporation",
                "Indirection", "Gradient"],
       cellules={
           (0, 0): ("", "Le dépôt qu'une action laisse derrière elle."),
           (0, 1): ("", "Un enregistrement, en ajout seul et durable."),
           (1, 0): ("", "Le nid : un espace physique, durable et sans propriétaire."),
           (1, 1): ("", "La partition : ordre total à l'intérieur (M1), aucun entre partitions (M2)."),
           (2, 0): ("", "Ce que l'insecte perçoit sous lui, borné par la portée du capteur."),
           (2, 1): ("", "L'intervalle compris entre le décalage validé de l'agent et la fin courante."),
           (3, 0): ("", "Une décroissance chimique, gratuite et exponentielle."),
           (3, 1): ("", "Une politique de rétention du courtier, ou un facteur γ < 1 appliqué par le lecteur."),
           (4, 0): ("✓", "Aucun destinataire ; la trace survit à son auteur."),
           (4, 1): ("✓", "Conservée : découplage spatial, découplage temporel, persistance."),
           (5, 0): ("", "La phéromone diffuse et construit un champ : l'insecte décide par montée locale."),
           (5, 1): ("✕", "Détruit : lire « la trace près de moi » revient à lire une clé, et il "
                         "n'existe aucune métrique entre deux clés."),
       },
       axes="§ 1.2 — les quatre premières lignes se substituent terme à terme ; la cinquième "
            "survit à la substitution ; la sixième n'y survit pas."))

f("1.3", "f-01-3-diametre",
  "Le diamètre du graphe de coordination : ce que le milieu supprime en topologie, et où le degré réapparaît.",
  "Comparaison entre une maille complete pair a pair et un graphe biparti agents-partitions.",
  "§ 1.3, chapitre 1.", "propre",
  "Le degré n'a pas disparu : il s'est déplacé dans le courtier, sous forme de n/p consommateurs "
  "par partition, et p plafonne le parallélisme. Ce que le logiciel obtient gratuitement en diamètre, "
  "il le repaie sur la durée d'un tour — ℓ₉₉ du chemin de durabilité, non un aller simple — et sur "
  "la contention, dont le régime appartient au chapitre 2.",
  "diametre")

# ================================================================= Chapitre 2
f("2.1a", "f-02-1a-calm",
  "Le critère qui décide de ce qui est décentralisable : le théorème CALM, tranché au niveau du programme et non du stockage.",
  "Arbre de decision fonde sur le theoreme CALM : programme monotone ou non.",
  "§ 2.1, chapitre 2 — d'après [6].", "arbre",
  "Le résultat est constructif dans les deux sens, ce qui en fait une borne et pas un conseil. "
  "Aucun choix de base de données, de courtier ou de bibliothèque ne fait passer un programme "
  "non monotone du côté gauche : pour celui-là, la coordination n'est pas évitable, elle est "
  "seulement déplaçable.",
  dict(titre="CE QUI SE DÉCENTRALISE, ET CE QUI NE SE DÉCENTRALISE PAS",
       racine="Le programme s'exprime-t-il en logique monotone — une conclusion atteinte "
              "n'étant jamais rétractée par l'arrivée de faits supplémentaires ?",
       branches=[
           ("OUI", "Implantation distribuée cohérente et sans coordination",
            "Accumuler, prendre un maximum, détecter un franchissement de seuil, construire "
            "une union. Le programme produit la même sortie quels que soient l'ordre et les "
            "délais des messages : l'accord est évitable."),
           ("NON", "Coordination inévitable, seulement déplaçable",
            "Compter exactement une fois, décrémenter un stock, attribuer un propriétaire "
            "unique. L'invariant doit tenir à tout instant, et le substrat événementiel ne "
            "suffit pas : le prix est celui du chapitre 4."),
       ]))

f("2.1b", "f-02-1b-usl",
  "La loi universelle de scalabilité : pourquoi un essaim qui entretient une vue commune n'a pas un rendement décroissant, mais un maximum.",
  "Deux courbes de capacite relative en fonction du nombre d'agents, l'une plafonnant, "
  "l'autre passant par un maximum puis decroissante.",
  "§ 2.1, chapitre 2 — d'après [3].", "courbe",
  "Ces deux valeurs de σ et de κ sont une illustration arithmétique de la formule citée [3], "
  "et non une mesure : le protocole qui les tirerait d'un journal de messages réel n'est pas "
  "écrit, et la conclusion de l'ouvrage en fait son premier reste. Ce qu'elles établissent tient "
  "néanmoins — dès que κ > 0, dépasser u* est une régression, pas un plafond.",
  dict(titre="C(n) = n ⁄ (1 + σ(n − 1) + κ·n(n − 1))", xmax=100, ymax=20, hcadre=138,
       xlab="nombre d'agents n", ylab="C",
       series=[
           ("σ = 0,05, κ = 0 — cas de la loi d'Amdahl : asymptote horizontale à σ⁻¹ = 20 ×, "
            "jamais dépassée, jamais retrouvée en arrière", "pointille"),
           ("σ = 0,05, κ = 10⁻³ — vue commune entretenue : maximum en "
            "u* = √((1 − σ)/κ), puis débit rétrograde", "plein"),
       ],
       reperes=[(30.8, 9.04, "u* ≈ 30,8")]))

f("2.1c", "f-02-1c-isr",
  "Où la garantie de l'ensemble synchronisé tombe : le déroulé complet à k = 3 répliques et seuil d'accusé m = 2.",
  "Grille de cinq instants montrant la reduction de l'ensemble synchronise et la destruction "
  "d'un enregistrement valide.",
  "§ 2.1, chapitre 2 — d'après [5].", "matrice",
  "Le nombre de disparitions auquel r₂ survit n'est pas k − 1 = 2, il est m − 1 = 1. La borne "
  "s'écrit en fonction du seuil d'accusé m ; nulle part en fonction du facteur de réplication k. "
  "La documentation ne se contredit pas — elle conditionne sa garantie à ce qu'au moins une "
  "réplique reste synchronisée à tout instant, et c'est justement le point.",
  dict(titre="k = 3 RÉPLIQUES, SEUIL D'ACCUSÉ m = 2 : R1 TOMBE À DEUX ARRÊTS", lx=116,
       colonnes=["t₀", "t₁", "t₂", "t₃", "t₄"],
       rangees=["Ensemble synchronisé", "Réplique A, meneur", "Réplique B",
                "Réplique C", "Ce qui survient"],
       cellules={
           (0, 0): ("", "{A, B, C}"), (0, 1): ("", "{A, B}"), (0, 2): ("", "{A, B}"),
           # ⚠ « { } » et non « ∅ » : Corbel n'a pas U+2205, et Typst rend le
           # caractere manquant en tofu — invisible a la generation, visible au PDF.
           (0, 3): ("", "{A}"), (0, 4): ("", "{ }"),
           (1, 0): ("", "r₁"), (1, 1): ("", "r₁"), (1, 2): ("", "r₁ r₂"),
           (1, 3): ("", "r₁ r₂"), (1, 4): ("✕", "arrêt"),
           (2, 0): ("", "r₁"), (2, 1): ("", "r₁"), (2, 2): ("", "r₁ r₂"),
           (2, 3): ("✕", "arrêt"), (2, 4): ("", "—"),
           (3, 0): ("", "r₁"), (3, 1): ("", "r₁, retirée"), (3, 2): ("", "r₁"),
           (3, 3): ("", "r₁"), (3, 4): ("", "r₁, seule vivante"),
           (4, 0): ("", "r₁ accusé ; largeur 3"),
           # ⚠ Pas de point-virgule dans une cellule de 70 pt : le repli le pose
           # en tête de ligne, où il se lit comme une coquille.
           (4, 1): ("", "retard > seuil, sans panne"),
           (4, 2): ("", "r₂ accusé ; largeur 2"),
           (4, 3): ("", "sous m : la partition cesse d'accuser"),
           (4, 4): ("", "élire C laisse r₂ nulle part"),
       },
       axes="§ 2.1 — deux arrêts, donc k ≥ f + 1 respecté à l'égalité. Un retrait pour retard "
            "n'est pas une panne, et le compteur de pannes est à zéro à t₁."))

f("2.3", "f-02-3-metastable",
  "La défaillance métastable : le déclencheur entre et ressort, l'effet de maintien reste.",
  "Chaine de quatre etats, de l'etat stable a l'etat metastable, avec la boucle de maintien.",
  "§ 2.3, chapitre 2 — d'après [50].", "chaine",
  "Une panne métastable est habituellement imputée à son déclencheur, alors que la cause réelle "
  "est l'effet de maintien. En sortir exige une poussée corrective forte : dans l'exemple chiffré "
  "du cadre, un système qui tient à 280 requêtes/s y reste bloqué à 560 requêtes/s par le seul "
  "effet des reprises, et la sortie exige de ramener la charge sous 150 requêtes/s [50]. Aucun "
  "agent n'a fauté, aucun canal n'a omis.",
  dict(titre="LE DÉCLENCHEUR N'EST PAS LA CAUSE",
       boucle="Effet de maintien — amplification du travail ou baisse d'efficacité globale : "
              "le facteur 2 des reprises, le facteur 10 de la perte d'un cache à 90 % de succès. "
              "C'est lui, et non le déclencheur, qui empêche le retour.",
       maillons=[
           ("État stable", "Le système absorbe sa charge. Aucune amplification n'est active."),
           ("État vulnérable", "Aucune surcharge. On peut y tourner des mois ou des années, et "
                               "beaucoup de systèmes de production choisissent d'y tourner en "
                               "permanence, parce qu'il est plus efficace."),
           ("Déclencheur", "Une coupure de 10 s, une perte de cache, une pointe. Il entre, "
                           "puis il ressort."),
           ("État métastable", "Le débit utile est inutilisable, et le retrait du déclencheur "
                               "ne suffit plus à en sortir."),
       ]))

# ================================================================= Chapitre 3
f("3.2", "f-03-2-surete-vivacite",
  "L'asymétrie que toute spécification d'essaim doit trancher : ce qu'une exécution finie peut réfuter, et ce qu'elle ne peut pas.",
  "Deux panneaux opposant une propriete de surete et une propriete de vivacite.",
  "§ 3.2, chapitre 3 — d'après [61].", "paire",
  "Toute propriété est l'intersection d'une propriété de sûreté et d'une propriété de vivacité [61]. "
  "Un cahier des charges qui mêle S1 et L1 sans les nommer produit des exigences dont la moitié "
  "est non testable — et dans un essaim asynchrone, aucune vivacité ne s'énonce inconditionnellement : "
  "elle porte un détecteur de défaillance, ou une hypothèse de synchronisme partiel, et écrire "
  "« l'essaim finit par converger » sans dire laquelle est le défaut de spécification le plus "
  "fréquent du domaine.",
  dict(titre_g="S1 — SÛRETÉ", titre_d="L1 — VIVACITÉ", accent_d=True,
       gauche=("« Deux agents ne détiennent jamais simultanément l'attribution de la même partition. »", [
           "Si elle ne tient pas, il existe un instant identifiable où la mauvaise chose se "
           "produit, et cette mauvaise chose est irrémédiable : aucun prolongement ne la répare.",
           "Se réfute par une exécution de trois secondes.",
           "Un moniteur peut lever l'alerte à l'instant de la violation.",
           "Se démontre en asynchrone.",
       ], "Décidable sur un horizon borné : justiciable de la vérification bornée."),
       droite=("« Tout agent qui rejoint le groupe finit par recevoir une attribution. »", [
           "Aucune exécution partielle n'est irrémédiable : quelle que soit l'exécution finie "
           "déjà observée, il existe un prolongement infini qui la satisfait.",
           "N'est réfutée par aucune exécution finie, donc par aucune campagne de tests.",
           "Aucun moniteur ne peut signaler qu'elle est violée — au mieux, qu'elle n'est pas "
           "encore satisfaite.",
           "Exige au minimum le partiellement synchrone.",
       ], "Non décidable sur horizon fini : aucun échantillon ne la tranche.")))

f("3.3", "f-03-3-validation",
  "Ce que chaque méthode de validation avant déploiement peut réfuter, et ce qu'elle ne peut pas.",
  "Quatre methodes de validation avant deploiement, avec ce que chacune refute et son cout.",
  "§ 3.3, chapitre 3.", "bandes",
  "Aucune des quatre ne réfute une propriété de vivacité, et aucune ne s'étend à tout n : le "
  "problème d'accessibilité est indécidable même lorsque chaque processus a un espace d'états "
  "fini [63]. Vérifier l'essaim à n = 5 ne dit formellement rien de n = 5 000, et ce n'est pas "
  "une borne de complexité qu'un meilleur solveur ferait reculer. Une spécification vérifiée est "
  "une preuve sur un objet mathématique dont on espère qu'il ressemble au programme.",
  dict(titre="QUATRE MÉTHODES, QUATRE DOMAINES DE RÉFUTATION", cols=2, items=[
      ("1", "Vérification exhaustive",
       "Réfute S1 sur le n vérifié, y compris par une trace de 35 étapes qu'aucune campagne "
       "aléatoire ne trouverait. Ne réfute pas S1 pour tout n, ni L1 si la vivacité n'est pas vérifiée.",
       "Cubique en la taille de l'espace d'états joint, lui-même en Θ(|S|ⁿ)."),
      ("2", "Vérification statistique",
       "Réfute S1 avec confiance 1 − δ à ε près. Un événement de probabilité inférieure à ε "
       "est indiscernable de l'impossible.",
       "N = ln(2/δ)/(2ε²) exécutions : 26 492 à ε = 10⁻², puis 2,65 × 10⁶ pour un chiffre de plus."),
      ("3", "Simulation déterministe",
       "Réfute S1 et rejoue le contre-exemple à l'identique, entrelacement compris. Ne réfute "
       "ni la performance ni ℓ₉₉, ni rien de ce qui est hors du monde clos.",
       "Θ(E log E) par exécution ; la campagne se mesure en secondes simulées par seconde-cœur."),
      ("4", "Expérience en production",
       "Réfute l'écart au régime stable, sur le système et ses dépendances réelles. Ne réfute "
       "rien de reproductible : la trace n'est pas rejouable.",
       "Fraction du trafic de production exposée, soit le rayon d'explosion."),
  ]))

# ================================================================= Chapitre 4
f("4.1", "f-04-1-masse",
  "Où la conservation de masse se rompt : la ligne 4 de l'algorithme 1, et pourquoi la fausse valeur est unanime.",
  "Chaine de quatre etapes d'un echange push-pull, avec la perte du message de retour.",
  "§ 4.1, chapitre 4 — d'après [83].", "chaine",
  "Le résultat n'est pas en retard, il est faux — et faux silencieusement : tous les agents "
  "convergent, ils s'accordent tous sur la même valeur, et cette valeur ne correspond à aucune "
  "moyenne réelle. La relance périodique de la ligne 11 plafonne l'erreur accumulée ; elle ne "
  "la corrige pas, et aucun agent ne peut distinguer une estimation stabilisée d'une estimation "
  "amputée.",
  dict(titre="UN SEUL MESSAGE PERDU, ET LA SOMME A DIMINUÉ",
       rupture=("La rupture n'est pas dans l'implantation : elle est dans l'hypothèse. "
                "L'invariant tient en synchrone et sans faute, et perte de message comme arrêt "
                "d'agent le cassent tous deux [83].", 2),
       maillons=[
           ("1. i échantillonne j", "L'agent i tire un pair et lui envoie ⟨PUSH, e, x⟩."),
           ("2. j fusionne", "j répond ⟨PULL, e, x⟩, puis pose x ← (x + x′)/2. Sa part est "
                             "déjà moyennée."),
           ("3. le PULL se perd", "Rien ne revient à i avant τ. i abandonne le cycle et laisse "
                                  "x inchangé."),
           ("4. la somme a baissé", "j a moyenné, i non. La somme des estimations n'égale plus "
                                    "la somme des mesures initiales."),
       ]))

f("4.2", "f-04-2-echelle",
  "Trois exigences de force croissante, et le prix qui les sépare.",
  "Pile de trois regimes de coordination : propager, converger, s'accorder, avec leur cout.",
  "§ 4.2, chapitre 4.", "pile",
  "Faire circuler une information, faire converger des répliques et se mettre d'accord sur une "
  "valeur ne sont pas trois versions de la même chose. En asynchrone pur, la troisième est "
  "impossible : une seule faute d'arrêt suffit à l'empêcher [1]. L'essaim ne résout pas "
  "l'impossibilité, il refuse la question — et paie ce refus en fenêtres pendant lesquelles "
  "l'invariant peut être faux.",
  dict(titre="PROPAGER, CONVERGER, S'ACCORDER",
       couches=[
           ("1", "Propager", "Faire circuler une information dans un réseau non structuré."),
           ("2", "Converger", "Faire s'accorder des répliques en l'absence de nouvelles écritures."),
           ("3", "S'accorder", "Décider une valeur unique : accord, validité, terminaison."),
       ],
       notes=[
           ("S'accorder — consensus, synchronisme partiel",
            "Ω(n) messages par décision : une majorité doit être jointe, et cette majorité est "
            "prouvée nécessaire [65]. Terminaison bornée après stabilisation, non bornée avant."),
           ("Converger — répliques sans conflit",
            "Zéro message dédié : la fusion s'effectue sur le chemin de réplication déjà payé. "
            "Aucune condition d'arrêt — la convergence est une quiescence, qu'aucun agent ne "
            "peut constater localement."),
           ("Propager — rumeur épidémique",
            "Θ(n log log n) messages en O(log n) tours, optimal pour les algorithmes insensibles "
            "à l'adresse [85]. Terminaison locale seulement : la couverture est de probabilité "
            "strictement inférieure à 1."),
       ]))

# ================================================================= Chapitre 5
f("5.1", "f-05-1-abandon",
  "Ce que chaque mécanisme de choix distribué abandonne parmi accord, validité et terminaison.",
  "Grille des trois mecanismes de choix distribue et des proprietes que chacun abandonne.",
  "§ 5.1, chapitre 5.", "matrice",
  "Chaque mécanisme abandonne délibérément au moins une des trois propriétés. Abandonner la "
  "terminaison laisse l'essaim indécis ; abandonner l'accord le laisse divisé sans qu'aucun "
  "agent le sache — et c'est le second qui se paie le plus cher, parce qu'il ne se voit pas. "
  "Sous faute arbitraire, aucune solution à moins de 3f + 1 participants ne tolère f déviants [94] : "
  "ce modèle tue les trois premières lignes.",
  dict(titre="✓ TENUE · ~ TENUE SOUS CONDITION · ✕ ABANDONNÉE", lx=152,
       colonnes=["Accord", "Validité", "Terminaison", "Messages"],
       rangees=["Seuil de quorum (best-of-n)", "Moyenne et alignement",
                "Fusion sans conflit (CRDT)", "Consensus, synchronisme partiel"],
       cellules={
           (0, 0): ("✕", "sous partition"), (0, 1): ("✓", ""),
           (0, 2): ("~", "non borné"), (0, 3): ("", "Θ(n·d̄) par tour"),
           (1, 0): ("~", "à terme"), (1, 1): ("✕", ""),
           (1, 2): ("✕", "asymptotique"), (1, 3): ("", "Θ(n·d̄) par tour"),
           (2, 0): ("✓", ""), (2, 1): ("✕", "le refus est impossible"),
           # ⚠ « aucun message dédié » et non « 0 dédié » : Corbel compose ses
           # chiffres en bas de casse, et un zéro isolé s'y lit comme un « o ».
           (2, 2): ("✕", "quiescence"), (2, 3): ("", "aucun message dédié"),
           (3, 0): ("✓", ""), (3, 1): ("✓", ""),
           (3, 2): ("✓", "conditionnelle"), (3, 3): ("", "Ω(n) par décision"),
       },
       axes="§ 5.1 — « non borné » signifie qu'aucune borne finie n'existe sous les hypothèses "
            "posées, et non qu'elle est grande."))

f("5.2", "f-05-2-sondes",
  "La borne à battre avant de proposer une enchère : deux sondes, 2d messages, un tour, zéro état partagé.",
  "Barres comparant le temps de sejour espere a une sonde et a deux sondes, sous deux charges.",
  "§ 5.2, chapitre 5 — d'après [57].", "barres",
  "Deux choix apportent une amélioration exponentielle sur un seul, tandis que trois choix ne "
  "gagnent qu'un facteur constant sur deux [57]. Le résultat exige que le client soit libre de "
  "choisir son serveur : dans un journal partitionné, la partition est imposée par la clé, parce "
  "que l'ordre par partition est le seul ordre garanti. Router un événement vers la partition la "
  "moins chargée détruit l'ordre par clé, c'est-à-dire la propriété même qui justifiait le "
  "partitionnement.",
  dict(titre="TEMPS DE SÉJOUR ESPÉRÉ, MODÈLE DU SUPERMARCHÉ", vmax=100, lx=196,
       unite="en unités de durée moyenne de service. Coût du mécanisme : 2d messages, 1 tour, "
             "aucun état partagé, aucune hypothèse de synchronisme.",
       items=[
           ("Une seule sonde (d = 1), charge λ = 0,90", 10, "10,00", False),
           ("Deux sondes (d = 2), charge λ = 0,90", 2.61, "≈ 2,61", True),
           ("Une seule sonde (d = 1), charge λ = 0,99", 100, "100,00", False),
           ("Deux sondes (d = 2), charge λ = 0,99", 5.43, "≈ 5,43", True),
       ]))

# ================================================================= Chapitre 6
f("6.1", "f-06-1-cascade",
  "La cascade de l'agent saturé : comment deux détecteurs de défaillance composés transforment une charge en panne.",
  "Chaine de quatre etapes decrivant la cascade d'un agent sature tue par sa sonde de vivacite.",
  "§ 6.1, chapitre 6.", "chaine",
  "Le remède n'est pas un réglage plus généreux. La sonde de disponibilité n'a AUCUN effet sur "
  "l'allocation de partitions d'un consommateur, dont le travail n'arrive pas par un point d'accès "
  "mais par sa propre lecture du journal. La sonde de vivacité ne doit donc tester qu'un blocage "
  "constatable sans travailler — un fil qui n'a pas avancé son décalage —, jamais la capacité à "
  "répondre dans le délai, qui mesure la charge.",
  dict(titre="AUCUN AGENT N'EST TOMBÉ, ET L'ESSAIM S'EFFONDRE",
       boucle="La cascade est complète en trois générations. Le taux de fausses suspicions n'est "
              "pas une constante du détecteur : c'est une fonction croissante de la charge, qui "
              "culmine exactement au moment où le système peut le moins se le permettre.",
       maillons=[
           ("1. Saturation", "La latence de réponse de l'agent franchit le délai d'expiration de "
                             "la sonde, fixé à 1 s. L'agent est vivant."),
           ("2. Mort déclarée", "Trois échecs consécutifs à 10 s d'intervalle : le conteneur est "
                                "redémarré au bout de 30 s."),
           ("3. Rééquilibrage", "Sa disparition en déclenche un : 4 tours et 8n messages sous le "
                                "protocole coopératif."),
           ("4. Report de charge", "Ses partitions échoient à des agents déjà saturés, qui "
                                   "reconstruisent son état et manquent à leur tour leurs échéances."),
       ]))

f("6.2", "f-06-2-trace",
  "Pourquoi la trace distribuée normalisée ne suffit pas : un arbre a une racine et une fin, une décision d'essaim n'en a pas.",
  "Deux panneaux opposant l'arbre d'une trace de requete et le graphe acyclique d'une decision d'essaim.",
  "§ 6.2, chapitre 6.", "paire",
  "L'échantillonnage en queue ne résout pas le problème, il le déplace : trancher après 30 s "
  "suppose que tous les intervalles d'une trace arrivent en moins de 30 s, et les longues chaînes "
  "— exactement celles qu'on voulait retenir — sont les seules systématiquement tronquées. "
  "La reconstruction causale se fait donc hors ligne, sur le journal, pour zéro message vers un "
  "agent ; son horizon réel est la rétention du sujet, et un sujet compacté n'est pas un substrat "
  "de traçabilité.",
  dict(titre_g="TRACE D'UNE REQUÊTE — UN ARBRE", titre_d="DÉCISION D'UN ESSAIM — UN GRAPHE",
       accent_d=True,
       gauche=("Ce que les normes savent représenter", [
           "Chaque intervalle porte un parent unique et un statut pris parmi exactement trois valeurs.",
           "L'arbre a une racine, et il se termine avec elle.",
           "L'échantillonnage en tête borne le nombre de traces retenues ET leur taille.",
           "Le chemin critique se lit sur l'arbre.",
       ], "Structure finie et courte, décidée au point d'entrée."),
       droite=("Ce que l'essaim produit réellement", [
           "Un enregistrement peut être lu par m consommateurs à des jours d'intervalle.",
           "Une décision peut agréger j enregistrements venus de j partitions : ni racine, ni fin.",
           "La décision propagée borne le nombre de traces, mais PAS leur taille — celle-ci croît "
           "avec le nombre d'agents qui liront l'enregistrement, sans borne connue au moment de "
           "la décision.",
           "Le chemin critique devient le plus long chemin d'un graphe : Θ(V+E), qui exige tous "
           "les sommets.",
       ], "Degrés non bornés a priori ; c'est ce que l'échantillonnage ne garantit pas.")))

# ================================================================= Chapitre 7
f("7.2", "f-07-2-taux-base",
  "Le taux de base : pourquoi une sonde presque parfaite produit des alarmes presque toutes fausses, et ce que la corroboration achète.",
  "Barres du taux de detection bayesien selon le taux de fausses alarmes et le regime de corroboration.",
  "§ 7.2, chapitre 7 — d'après [116].", "barres",
  "La corroboration n'améliore pas la détection : elle échange de la détection contre de la "
  "précision, à un taux d'échange extraordinairement favorable — mais à r = 3, la détection "
  "conjointe tombe à 0,343, et deux intrusions sur trois passent inaperçues. Sa condition d'échec "
  "est structurelle : l'essaim est par définition une population majoritairement homogène, et des "
  "détecteurs identiques appliqués à des entrées corrélées commettent des erreurs corrélées. "
  "Rien dans le mécanisme ne mesure où l'on se situe entre les deux extrêmes.",
  dict(titre="PART DES ALARMES QUI SONT VRAIES — P(I|A), MODÈLE D'AXELSSON", vmax=100, lx=214,
       unite="taux de base P(I) = 2 × 10⁻⁵ : 10⁶ enregistrements d'audit par jour, deux "
             "tentatives d'intrusion, dix enregistrements par intrusion.",
       items=[
           ("Détection 1,00 — fausses alarmes 1 × 10⁻⁵", 66, "≈ 66 %", True),
           ("Détection 0,70 — fausses alarmes 1 × 10⁻⁵", 58, "≈ 58 %", True),
           ("Détection 1,00 — fausses alarmes 1 × 10⁻³, soit le plafond de 100 fausses "
            "alarmes par jour", 2, "≈ 2 %", True),
           ("Corroboration r = 3, détecteurs indépendants", 99.99, "≈ 99,99 %", True),
           ("Corroboration r = 3, détecteurs parfaitement corrélés", 2, "≈ 2 %", False),
       ]))


# ================================================================= Chapitre 8
f("8.1", "f-08-1-couverture",
  "Couverture contre efficacité : ce que l'auto-allocation par le milieu achète, et ce qu'elle n'achète pas.",
  "Barres comparant les vulnerabilites trouvees par un essaim coordonne et par des agents independants.",
  "§ 8.1, chapitre 8 — d'après [119].", "barres",
  "Le rapport de 266 à 21 ne se lit pas comme un gain d'efficacité : les deux méthodes ne "
  "consomment pas le même budget de jetons, et l'essaim restreint au périmètre assigné aux agents "
  "indépendants se compare à eux en jetons par vulnérabilité. Ce que l'essaim achète est une "
  "couverture, non un meilleur rendement, et douze trouvailles communes sur l'ensemble montrent "
  "que les deux méthodes ne se remplacent pas. Aucune de ces valeurs n'est reproductible hors de "
  "la version de modèle sur laquelle elle a été prise.",
  dict(titre="VULNÉRABILITÉS NOUVELLES ET VALIDES, QUINZE PROJETS LIBRES", vmax=266, lx=214,
       unite="jugées par un agent arbitre distinct. Budgets de jetons : 27 millions pour "
             "l'essaim coordonné, 6,5 millions pour les agents indépendants.",
       items=[
           ("Essaim coordonné — 45 agents, forum partagé, relecture mutuelle", 266, "266", True),
           ("Agents indépendants — périmètre de code assigné d'avance", 21, "21", False),
           ("Trouvailles communes aux deux méthodes", 12, "12", True),
       ]))

f("8.2", "f-08-2-profil-cache",
  "Le profil caché : ce qu'un groupe de quatre agents retient, et ce qu'un agent unique correctement informé aurait tranché.",
  "Barres de la part des episodes ou l'option cachee obtient la majorite, par modele, avec le plafond solo.",
  "§ 8.2, chapitre 8 — d'après [119].", "barres",
  "Le fait à retenir n'est pas l'écart entre modèles mais l'écart au plafond : un groupe fait "
  "moins bien qu'un seul de ses membres correctement informé, donc la délibération détruit de "
  "l'information au lieu de l'agréger. La barre des autres modèles est tracée à la borne haute "
  "d'un intervalle, et non à une valeur unique. La performance croît avec la capacité du modèle "
  "sans saturer au sommet de la gamme éprouvée : rien n'autorise à extrapoler qu'elle y "
  "parviendra.",
  dict(titre="PART DES ÉPISODES OÙ L'OPTION CACHÉE OBTIENT LA MAJORITÉ", vmax=100, lx=214,
       unite="groupes de quatre agents, quatre cents épisodes par modèle ; scénarios "
             "d'embauche, d'investissement et d'achat immobilier.",
       items=[
           ("Agent unique détenant tous les faits — plafond de référence", 100, "≈ 100 %", False),
           ("Groupe de quatre agents, modèle le plus capable éprouvé", 85, "85 %", True),
           ("Groupe de quatre agents, autres modèles éprouvés", 36, "17 à 36 %", True),
       ]))

f("8.3", "f-08-3-familles",
  "Les quatre familles de défaillance mesurées, et ce que chacune casse dans l'appareil de l'ouvrage.",
  "Grille des quatre familles de defaillance mesurees et de ce que chacune casse dans le traite.",
  "Chapitre 8 — mesures de [119] ; colonne de droite propre à cet ouvrage.", "matrice",
  "Les quatre familles ne sont pas de même statut. La première est un fait positif dont la "
  "réserve est un coût ; les trois autres sont des défaillances. Aucune n'invalide un résultat "
  "des sept premiers chapitres : elles en déplacent le domaine de validité, ce qui est plus "
  "difficile à voir et se corrige moins bien, puisque le mécanisme continue de tourner pendant "
  "que sa borne cesse de tenir.",
  dict(titre="CE QUE LA CAMPAGNE DE 2026 MESURE, ET CE QU'ELLE RETIRE À L'OUVRAGE", lx=104,
       colonnes=["Ce qui est mesuré", "Ce que cela retire à l'ouvrage"],
       rangees=["Coordination", "Conformité", "Épistémique", "Buts incompatibles"],
       cellules={
           (0, 0): ("", "266 vulnérabilités pour 27 millions de jetons contre 21 pour 6,5 "
                        "millions ; douze trouvailles communes ; partage de code et fraction "
                        "de fusion ne montent jamais ensemble."),
           (0, 1): ("", "Rien — le gain est de couverture et non d'efficacité, et "
                        "l'interférence du §2.2 reçoit enfin sa mesure logicielle."),
           (1, 0): ("", "Dix-huit agents sur trente ouvrent la même branche ; plus de la "
                        "moitié d'une population libre bâtit l'un de deux projets ; 2,4 "
                        "millions de demandes pour 117 acceptations."),
           (1, 1): ("", "Sept énoncés qui supposent l'indépendance des tirages ou des "
                        "fautes, du plancher d'exploration à la corroboration de sondes."),
           (2, 0): ("", "Groupes de quatre agents : l'option cachée l'emporte dans 17 à 85 % "
                        "des épisodes, contre un plafond proche de 100 % pour un agent seul "
                        "correctement informé."),
           (2, 1): ("", "La prémisse de la stigmergie — la trace cesse d'être un résidu de "
                        "l'action pour devenir un témoignage sur elle."),
           (3, 0): ("", "Trois mandats contradictoires : escalade jusqu'au sabotage sur tous "
                        "les modèles éprouvés ; issues par force, passivité, trêve ou "
                        "non-règlement, sur cent vingt épisodes par modèle."),
           (3, 1): ("", "Le modèle de panne P, et la gouvernance du §5.3, qui s'applique "
                        "dans le processus même dont on suppose qu'il agit contre le "
                        "système."),
       },
       axes="Ch. 8 — aucune de ces mesures n'est reproductible hors de la version de modèle "
            "sur laquelle elle a été prise."))


# ================================================== figures à dessin propre
def diametre():
    """Maille complète pair à pair contre graphe biparti agents-partitions.

    ⚠ Dessin PROPRE et non primitive : c'est un graphe, et aucune des huit
    dispositions ne dessine un graphe. L'argument du § 1.3 est visuel — le
    diamètre vaut 2 quel que soit n — et une grille de chiffres ne le montre pas.
    """
    lw = (d.W - 26) / 2
    out, hcadre = [], 152
    out.append(d.txt(0, 8, "MAILLE COMPLÈTE PAIR À PAIR", "titreg"))
    out.append(d.txt(round(lw + 26), 8, "JOURNAL PARTITIONNÉ", "titre"))
    out.append(d.rect(0, 14, round(lw), hcadre, d.CREME, d.FILET))
    out.append(d.rect(round(lw + 26), 14, round(lw), hcadre, d.BLANC, d.ACCENT, ".9"))

    # --- panneau gauche : six agents, toutes les arêtes
    cx, cy, r = lw / 2, 72, 42
    pts = []
    for k in range(6):
        a = math.radians(-90 + 60 * k)
        pts.append((round(cx + r * math.cos(a), 1), round(cy + r * math.sin(a), 1)))
    for i in range(6):
        for j in range(i + 1, 6):
            out.append(d.ligne(f"M {pts[i][0]} {pts[i][1]} L {pts[j][0]} {pts[j][1]}",
                               d.GRIS2, ".45"))
    for x, y in pts:
        out.append(f'<circle cx="{x}" cy="{y}" r="4.6" fill="{d.ENCRE}"/>')
    e, _ = d.bloc_texte(10, 138, "n(n − 1)/2 liens · n − 1 messages · 1 tour · "
                                 "Θ(n²) connexions à maintenir et à sonder.", lw - 20)
    out += e

    # --- panneau droit : six agents au-dessus de deux partitions
    x0 = lw + 26
    ax = [round(x0 + 26 + i * 33.6, 1) for i in range(6)]
    ay = 40
    parts = [(round(x0 + 22), 96, round(lw / 2 - 32)), (round(x0 + lw / 2 + 10), 96, round(lw / 2 - 32))]
    for px, py, pw in parts:
        out.append(d.rect(px, py, pw, 17, d.CREME, d.ACCENT, ".7"))
    for i, x in enumerate(ax):
        px, py, pw = parts[0 if i < 3 else 1]
        out.append(d.ligne(f"M {x} {ay} L {round(px + pw / 2, 1)} {py}", d.GRIS2, ".45"))
        out.append(f'<circle cx="{x}" cy="{ay}" r="4.6" fill="{d.ENCRE}"/>')
    out.append(d.txt(round(x0 + 22 + 6), 108, "partition 1", "renvoi"))
    out.append(d.txt(round(x0 + lw / 2 + 16), 108, "partition 2", "renvoi"))
    e, _ = d.bloc_texte(x0 + 10, 138, "n + p·k liens · 1 écriture puis 1 lecture par "
                                      "consommateur · 2 tours de journal · diamètre 2, "
                                      "quel que soit n.", lw - 20)
    out += e
    return out, 14 + hcadre + 8


PROPRES = {"diametre": diametre}

USL = [("σ = 0,05, κ = 0", lambda u: u / (1 + 0.05 * (u - 1))),
       ("σ = 0,05, κ = 10⁻³", lambda u: u / (1 + 0.05 * (u - 1) + 1e-3 * u * (u - 1)))]


# ============================================================ rendu et sortie
def corps(fig):
    t, data = fig["type"], fig["data"]
    if t == "propre":
        return PROPRES[data]()
    if t == "courbe":
        # ⚠ Les fonctions ne vivent pas dans l'entrée : une lambda dans une
        # déclaration de contenu se relit mal, et les deux tracés sont les deux
        # cas de la MÊME formule, qui doit donc s'écrire une fois.
        series = [(lib, USL[i][1], style)
                  for i, (lib, style) in enumerate(data["series"])]
        return d.courbe(series, data["xmax"], data["ymax"], data["titre"],
                        data["xlab"], data["ylab"], data["reperes"], data["hcadre"])
    return getattr(d, t)(**data)


def main():
    lignes = []
    for fig in FIGURES:
        c, h = corps(fig)
        d.rendu(fig["nom"], c, h, fig["alt"], fig["source"], fig["reserve"])
        lignes.append(f'![**Figure {fig["rang"]}** — {fig["legende"]}](figures/{fig["nom"]}.svg)')
    if "--md" in sys.argv:
        print("\n\n".join(lignes))
    else:
        print(f"{len(FIGURES)} figures écrites dans {d.RACINE}")


if __name__ == "__main__":
    main()
