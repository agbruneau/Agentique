#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures du barème A — Livre V (chapitres 47 à 50)."""
from spec import f, NOTE  # noqa: F401

f(47, "47.1", "f-47-01-cinq-horloges",
  "Les cinq composants d'un agent et leurs horloges propres : ce qui les fait changer, et qui en décide.",
  "Les cinq composants d'un agent, ce qui fait changer chacun et qui en decide.",
  "Tableau 47.1, § 47.1, chapitre 47 — construction d'auteur, au 27 juillet 2026 ; "
  "le § 47.8 y renvoie.", r"^## § 47\.2 ", "bandes",
  "⚠ UN SEUL DES CINQ EST DÉCIDÉ PAR L'EXPLOITANT. Les quatre autres changent sous la main d'un "
  "fournisseur, d'un éditeur, d'une chaîne de distribution ou de quiconque a accès au dépôt — et "
  "le protocole autorise le deuxième à changer À L'EXÉCUTION.",
  dict(titre="CINQ COMPOSANTS, CINQ HORLOGES, UN SEUL EXPLOITANT", cols=1, items=[
      ("1", "Poids de modèle", "Version publiée par son fournisseur ; retrait d'une version antérieure.", "décidé par le fournisseur, pas l'exploitant — ch. 6 § 6.3 ; § 47.8"),
      ("2", "Serveurs d'outils", "Révision d'une définition d'outil ; ajout ou retrait d'un serveur.", "décidé par l'éditeur, et le protocole autorise le changement à l'exécution — ch. 20 § 20.1 ; § 47.4"),
      ("3", "Bibliothèques et hôte", "Mise à jour de dépendance ; correctif de sécurité.", "décidé par la chaîne de distribution — § 47.2, § 47.3"),
      ("4", "Invites et instructions", "Édition d'un fichier, sans compilation ni déploiement.", "décidé par quiconque a accès au dépôt — § 47.7, § 47.8"),
      ("5", "Politique d'autorisation", "Révision d'une règle, d'une portée, d'un seuil d'approbation.", "décidé par l'exploitant — et c'est le seul des cinq"),
  ]))

f(47, "47.4", "f-47-04-provenance-miroir",
  "Le retournement du ch. 20 relu comme défaut de provenance : la même attaque, vue de l'autre bout.",
  "La meme attaque lue comme un probleme d'identite au ch. 20 et comme un defaut de provenance ici.",
  "§ 47.4, chapitre 47, et ch. 20 § 20.1.", r"^## § 47\.5 ", "paire",
  "Les deux lectures ne se remplacent pas : l'une explique POURQUOI le verdict d'admission "
  "vieillit, l'autre POURQUOI l'artefact a pu changer sans que rien ne l'atteste. Corriger l'une "
  "sans l'autre laisse l'attaque ouverte.",
  dict(titre_g="LU AU CH. 20 — IDENTITÉ", titre_d="LU ICI — PROVENANCE",
       gauche=("La particularité est le moment",
               ["L'admission a réussi",
                "Le verdict n'est pas borné dans le temps",
                "L'objet vérifié change ensuite"],
               "un problème de fraîcheur du verdict"),
       droite=("La particularité est l'artefact",
               ["Le composant n'a pas de provenance attestée",
                "Rien ne lie ce qui s'exécute à ce qui a été admis",
                "La nomenclature ne voit pas tout (§ 47.7)"],
               "un problème de composition attestée")))

f(48, "48.1", "f-48-01-classes-effet",
  "Les trois classes d'effet d'une action d'agent, et ce qu'une reprise produit.",
  "Les trois classes d'effet d'une action d'agent : lecture, ecriture, engagement.",
  "Tableau 48.1, § 48.1, chapitre 48 — construction d'auteur, au 27 juillet 2026.",
  r"^## § 48\.2 ", "bandes",
  "⚠ L'IDEMPOTENCE EST UNE PROPRIÉTÉ DE L'OUTIL, JAMAIS DU PROTOCOLE QUI L'INVOQUE (ch. 4 "
  "§ 4.4.2). Et sur la troisième classe, rien ne défait : seule la compensation agit, et elle "
  "est sémantique, non transactionnelle.",
  dict(titre="TROIS CLASSES, ET CE QU'UNE REPRISE PRODUIT", cols=3, items=[
      ("1", "Lecture", "Rien : rejouer une lecture ne change pas l'état du système d'enregistrement.", "bornée par le coût et la fraîcheur, non par la correction"),
      ("2", "Écriture", "Un doublon, sauf si l'opération est idempotente.", "l'idempotence est une propriété de l'outil"),
      ("3", "Engagement", "Un second engagement, que rien ne défait.", "seule la compensation agit, et elle est sémantique"),
  ]))

f(48, "48.2", "f-48-02-exactement-une-fois",
  "La seule composition qui tienne sous pannes : livraison au-moins-une-fois et consommateur idempotent.",
  "La composition d'une livraison au-moins-une-fois et d'un consommateur idempotent.",
  "§ 48.2, chapitre 48, sur le siège du ch. 1 § 1.5.2.", r"^## § 48\.3 ", "chaine",
  "⚠ La livraison exactement-une-fois est IRRÉALISABLE sous pannes — instance du problème des "
  "deux généraux (ch. 1 § 1.5.2). Ce qui s'obtient est un TRAITEMENT exactement-une-fois, et il "
  "se paie du côté du consommateur, jamais du protocole.",
  dict(titre="CE QUI SE COMPOSE, ET CE QUI EN RÉSULTE", maillons=[
      ("Au moins une fois", "la livraison ne perd rien, et peut répéter"),
      ("Consommateur idempotent", "la répétition ne produit pas de second effet"),
      ("Exactement une fois", "un traitement, non une livraison"),
  ]))

f(48, "48.3", "f-48-03-compensation",
  "Compensation et sagas au grain de l'agent : ce qui se défait, et ce qui se compense.",
  "La sequence d'une saga au grain de l'agent et son chemin de compensation.",
  "§ 48.3, chapitre 48.", r"^## § 48\.4 ", "chaine",
  "⚠ UNE COMPENSATION EST UNE SECONDE OPÉRATION, jamais une annulation : elle est sémantique et "
  "non transactionnelle, et elle a ses propres effets. Le seuil d'irréversibilité du ch. 31 "
  "§ 31.1.1 est ce qui la rend nécessaire, et ce qui la rend insuffisante.",
  dict(titre="QUAND UNE ÉTAPE ÉCHOUE À MI-PARCOURS",
       rupture=("L'étape échoue : ce qui précède ne se défait pas, il se compense — en sens inverse, une opération à la fois.", 1),
       maillons=[
           ("Étape 1", "engagée, et son effet est acquis"),
           ("Étape 2", "échoue"),
           ("Compensation 1", "une seconde opération, avec ses propres effets"),
       ]))

f(49, "49.0", "f-49-00-cone-incertitude",
  "Le cône d'incertitude et les trois statuts épistémiques.",
  "Les trois statuts epistemiques d'un enonce prospectif : programme, annonce, speculatif.",
  "§ 49.0.1 et § 49.0.2, chapitre 49.", r"^### 49\.0\.3 ", "bandes",
  "⚠ LE CÔNE S'ÉLARGIT AVEC LE TEMPS, et la discipline qui en découle est la RE-DATATION : un "
  "énoncé prospectif se relit à sa date, jamais à celle de sa lecture. Le chapitre ne prédit "
  "pas — il classe, et il dit à quel titre.",
  dict(titre="TROIS STATUTS, ET AUCUN N'EST UNE PRÉDICTION", cols=3, items=[
      ("1", "PROGRAMMÉ", "Une date opposable, portée par un instrument en vigueur ou une décision prise.", "le cône est étroit"),
      ("2", "ANNONCÉ", "Une cible communiquée par celui qui la porte, sans force opposable.", "le cône s'élargit"),
      ("3", "SPÉCULATIF", "Aucun jalon daté au socle ; un raisonnement, et ses conditions.", "le cône est ouvert"),
  ]))

f(49, "49.1", "f-49-01-grappe-echeances",
  "La grappe d'échéances 2027-2032, et la concentration de 2027.",
  "La grappe des echeances datees de 2027 a 2032, avec la concentration de 2027.",
  "§ 49.1, chapitre 49.", r"^## § 49\.2 ", "frise",
  "⚠ SEULES LES ÉCHÉANCES PROGRAMMÉES FIGURENT ICI. Le « programmé » lui-même est mouvant "
  "(§ 49.1.4) : une date opposable peut être reportée, et l'a déjà été dans ce corpus. La frise "
  "est un squelette daté, non un calendrier.",
  dict(titre="LE SQUELETTE DATÉ, ET LUI SEUL", jalons=[
      ("2027", "La concentration", "E-23 opposable le 1ᵉʳ mai ; l'essentiel des jalons de la somme y tombe — § 49.1.1", "plein"),
      ("2028-2029", "Identité et standards", "l'horloge de fond des travaux normatifs — § 49.1.2", "creux"),
      ("2030", "Post-quantique", "premier jalon des instruments fédéraux — ch. 21", "creux"),
      ("2032", "Règlement", "les échéances financières et de règlement — § 49.1.3", "creux"),
  ]))

f(49, "49.11", "f-49-11-trois-axes",
  "Trois axes, et des futurs qui s'y lisent différemment.",
  "Les trois axes selon lesquels les scenarios 2027-2032 se lisent.",
  "§ 49.11.2, chapitre 49.", r"^### 49\.11\.3 ", "bandes",
  "⚠ SIX CONDITIONS, ET AUCUNE N'EST ACQUISE (§ 49.11.4). Les axes ordonnent des lectures ; ils "
  "ne pondèrent aucun scénario, et les discontinuités à faible probabilité et fort impact "
  "(§ 49.11.3) ne s'y rangent pas.",
  dict(titre="TROIS AXES, ET AUCUNE PONDÉRATION", cols=3, items=[
      ("1", "Les protocoles", "Convergence ou coexistence stratifiée gouvernée — § 49.2.", "le verrou est la portabilité neutre"),
      ("2", "La gouvernance", "Bifurcation par couche ; neutralité contestée — § 49.3.", "les groupes communautaires comme signal faible"),
      ("3", "La menace", "Trajectoire, et l'horloge post-quantique — § 49.4, § 49.5.", "la seule échéance datée du Livre II"),
  ]))

f(50, "50.2", "f-50-02-evenements-peremption",
  "Les quatorze événements de péremption, et ce que chacun ferait refaire.",
  "Les quatorze evenements de peremption de la somme, avec leur tri prospectif.",
  "Tableau 50.1, § 50.2, chapitre 50 — état au gel.", r"^## § 50\.3 ", "bandes",
  "⚠ UN ÉVÉNEMENT SURVENU N'EST PAS UN ÉVÉNEMENT PAYÉ. L'un des quatorze est survenu à moitié — "
  "l'annonce est établie, la suite ne l'est pas —, et un autre est le seul du corpus dont le "
  "dispositif ait été éprouvé par le réel (ch. 8, revalidation du 30 juillet 2026).",
  dict(titre="QUATORZE ÉVÉNEMENTS, ET TROIS ÉTATS", cols=3, items=[
      ("survenu", "Révisions protocolaires", "La couche protocolaire du Livre I se périme au rythme de ses DEUX spécifications, non de la seule première.", "payé — ch. 8, revalidation du 30 juillet 2026"),
      ("à moitié", "Transfert de gouvernance", "L'annonce du don est établie ; la suite ne l'est pas.", "candidat survenu à moitié, et c'est la moitié qui compte"),
      ("attendu", "Désignation de l'organisme", "Fait négatif vérifié : quatre chaînes, trois textes, zéro occurrence.", "ch. 32 — ce qui se refait est tout le chapitre"),
  ]))

f(50, "50.3", "f-50-03-protocole-revalidation",
  "Le protocole de revalidation : la boucle, et son déclencheur.",
  "La boucle du protocole de revalidation de la somme, et son declencheur.",
  "§ 50.3, chapitre 50.", r"^## § 50\.4 ", "chaine",
  "⚠ Le protocole ne se déclenche pas seul : il suppose une VEILLE qui constate l'événement. "
  "Revalider n'est pas retoucher un texte gelé — c'est confronter chaque énoncé au texte neuf "
  "(ch. 8, revalidation du 30 juillet 2026).",
  dict(titre="CE QUI SE REFAIT, ET DANS QUEL ORDRE", boucle=True, maillons=[
      ("Événement", "l'un des quatorze survient, et la veille le constate"),
      ("Extraction", "le texte neuf est extrait à sa source, à sa date"),
      ("Confrontation", "chaque énoncé y est confronté — non retouché"),
      ("Registre", "le gel est repoussé, et la date inscrite"),
  ]))

f(50, "50.4", "f-50-04-carte-fraicheur",
  "La carte de fraîcheur : les cinquante chapitres et la date de gel de chacun.",
  "La carte de fraicheur des cinquante chapitres de la somme, par date de gel.",
  "§ 50.4, chapitre 50 — le registre de gel par chapitre.", NOTE, "matrice",
  "⚠ UNE DATE DE GEL N'EST PAS UNE DATE DE PÉREMPTION : un chapitre gelé plus tôt n'est pas "
  "faux, il est daté. Ce que la carte montre est l'ordre dans lequel la revalidation devrait "
  "s'exercer, non un classement de fiabilité.",
  dict(titre="CINQ LIVRES, UN GEL UNIQUE, ET LES ÉVÉNEMENTS QUI L'ENTAMENT",
       colonnes=["Gel de la somme", "Événements de péremption qui le touchent"],
       rangees=["Livre I — Coopérer", "Livre II — Faire confiance", "Livre III — Encadrer",
                "Livre IV — Appliquer", "Livre V — Livrer et clore"],
       cellules={
           (0, 0): ("", "27 juillet 2026"),
           (0, 1): ("", "révisions protocolaires — l'un des deux est survenu et payé"),
           (1, 0): ("", "27 juillet 2026"),
           (1, 1): ("", "normalisation du passeport ; jalons post-quantiques ; premier incident public"),
           (2, 0): ("", "27 juillet 2026"),
           (2, 1): ("", "désignation de l'organisme ; lancement du rail temps réel"),
           (3, 0): ("", "27 juillet 2026"),
           (3, 1): ("", "conventions sémantiques d'observabilité"),
           (4, 0): ("", "27 juillet 2026"),
           (4, 1): ("", "transfert de gouvernance du protocole de paiement"),
       },
       axes="Se reporter au Tableau 50.1 pour les onze événements, leur trace et leur tri prospectif."))
