#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures du barème A — Livre IV (chapitres 37 à 46)."""
from spec import f, NOTE  # noqa: F401

f(37, "37.3", "f-37-03-non-compositionnalite",
  "La non-compositionnalité de la sûreté : deux arêtes sûres, un chemin qui ne l'est pas.",
  "Un contre-exemple montrant que deux arretes individuellement sures ne composent pas un chemin sur.",
  "§ 37.3, chapitre 37.", r"^## § 37\.4 ", "chaine",
  "C'est ce que le maillage NE PEUT PAS corriger par l'arête : une politique vérifiée à chaque "
  "saut ne dit rien du chemin complet. Le même constat porte la composabilité du ch. 11 § 11.1.1 "
  "et le détournement multi-agents du ch. 19 § 19.4.",
  dict(titre="CHAQUE ARÊTE EST AUTORISÉE — LE CHEMIN NE L'EST PAS",
       rupture=("Aucune arête n'est en faute ; c'est leur composition qui l'est, et aucune ne la voit.", 2),
       maillons=[
           ("Agent A", "autorisé à demander à B"),
           ("Agent B", "autorisé à demander à C"),
           ("Agent C", "détient l'accès sensible"),
       ]))

f(37, "37.5", "f-37-05-pep-pdp",
  "Où se prend la décision d'autorisation, et où elle s'applique.",
  "Le point de decision et le point d'application de politique dans un maillage d'agents.",
  "§ 37.5, chapitre 37.", r"^## § 37\.6 ", "paire",
  "⚠ Le vocabulaire existe et il est BORNÉ : le socle ne porte pas ce que le point d'application "
  "devrait LIRE quand l'appelant est un agent, et le point d'application, quand il existe, peut "
  "ne pas couvrir ce qu'on croit (§ 37.5.3, § 37.5.4).",
  dict(titre_g="POINT DE DÉCISION (PDP)", titre_d="POINT D'APPLICATION (PEP)",
       gauche=("Où la politique est évaluée",
               ["Reçoit le contexte de la requête",
                "Rend un verdict",
                "Ne voit pas nécessairement l'exécution"],
               "le vocabulaire vient de NIST SP 800-207"),
       droite=("Où le verdict mord",
               ["À l'arête, entre deux agents",
                "Refuse ou laisse passer",
                "⚠ ce qu'il doit lire d'un agent n'est pas documenté"],
               "siège : ce chapitre")))

f(37, "37.7", "f-37-07-zero-trust-graphe",
  "Zero trust transposé : de « jamais confiance au réseau » à « jamais confiance au graphe ».",
  "La transposition du principe zero trust du reseau vers le graphe d'agents.",
  "§ 37.7, chapitre 37.", r"^## § 37\.8 ", "paire",
  "La transposition est une LECTURE, non un mécanisme : nommer le graphe à la place du réseau ne "
  "fournit ni l'identité qui s'y vérifie, ni la fraîcheur du verdict (§ 37.8.3). Le principe "
  "change de domaine ; les manques ne changent pas.",
  dict(titre_g="ZERO TRUST RÉSEAU", titre_d="ZERO TRUST AGENTIQUE",
       gauche=("Jamais confiance au réseau",
               ["La localisation n'accorde rien",
                "Chaque appel s'authentifie",
                "Le périmètre cesse d'être une frontière"],
               "NIST SP 800-207"),
       droite=("Jamais confiance au graphe",
               ["La position dans le graphe n'accorde rien",
                "Chaque arête se vérifie",
                "Être invoqué par un pair n'est pas une autorisation"],
               "transposition — ce chapitre")))

f(37, "37.8", "f-37-08-ce-qu-il-voit",
  "Ce que le maillage voit de la chaîne de mandat, et ce qu'il ne peut pas suppléer.",
  "Le perimetre de ce qu'un maillage d'agents voit de la chaine de mandat, et ses trois manques.",
  "§ 37.8, chapitre 37.", r"^## § 37\.9 ", "paire",
  "⚠ Ce qu'il voit EST ÉNUMÉRABLE, et l'énumération est le résultat. Les manques se lisent sur "
  "trois entrées, et AUCUNE NE DÉPEND DU MAILLAGE : ce ne sont pas des défauts de mise en œuvre, "
  "ce sont des propriétés que l'arête ne porte pas.",
  dict(titre_g="CE QU'IL VOIT", titre_d="CE QU'IL NE PEUT PAS SUPPLÉER",
       gauche=("Une arête, à l'instant du passage",
               ["Qui appelle qui",
                "Ce que la politique dit de cette arête",
                "Et il peut en produire une trace"],
               "énumérable — § 37.8.1 et § 37.8.4"),
       droite=("Ce qui ne se lit pas sur une arête",
               ["La chaîne au-delà du saut courant",
                "La fraîcheur du mandat invoqué",
                "L'ancrage de l'identité qui se présente"],
               "trois entrées, aucune ne dépend du maillage")))

f(38, "38.3", "f-38-03-propagation-trace",
  "La propagation de trace à travers les frontières d'agents, et l'endroit où le contexte se perd.",
  "La propagation d'un contexte de trace a travers plusieurs agents, et son point de rupture.",
  "§ 38.3, chapitre 38.", r"^## § 38\.4 ", "chaine",
  "La propagation est un mécanisme du monde applicatif, transposé : ce qui traverse une frontière "
  "d'agents n'est pas garanti d'y survivre, et une trace interrompue ne se recolle pas après coup. "
  "Le ch. 3 § 3.4.5 en porte le versant classique.",
  dict(titre="UN IDENTIFIANT DE TRACE, ET LES FRONTIÈRES QU'IL DOIT FRANCHIR",
       rupture=("Au franchissement d'une frontière d'agents, rien ne garantit que le contexte soit repropagé.", 1),
       maillons=[
           ("Appelant", "ouvre la trace, émet le contexte"),
           ("Agent", "doit le propager à son tour"),
           ("Outil", "le reçoit — ou ne le reçoit pas"),
       ]))

f(38, "38.5", "f-38-05-trace-passeport",
  "L'identité comme clé de jointure entre la trace et le passeport.",
  "La correlation entre une trace d'observabilite et les pieces du passeport d'agent.",
  "§ 38.5, chapitre 38.", NOTE, "chaine",
  "La jointure suppose que les deux côtés portent LE MÊME identifiant — et le ch. 16 établit que "
  "les quatre pièces du passeport n'ont pas d'émetteur commun. Corréler est une exigence "
  "d'architecture, pas une propriété du socle.",
  dict(titre="CE QUI RATTACHE UNE ACTION À QUELQU'UN", maillons=[
      ("Trace", "ce que l'observabilité a enregistré de l'action"),
      ("Identité", "la clé de jointure — encore faut-il qu'elle soit la même des deux côtés"),
      ("Passeport", "carte, registre, mandat, attestations — ch. 16"),
  ]))

f(39, "39.2", "f-39-02-quatre-derives",
  "Les quatre dérives, et le degré de documentation de chacune.",
  "Les quatre sources de derive d'un agent en exploitation, et leur degre de documentation.",
  "§ 39.2, chapitre 39.", r"^## § 39\.3 ", "bandes",
  "⚠ LES QUATRE NE SONT PAS DOCUMENTÉES AU MÊME DEGRÉ. Une seule est instruite par un chapitre ; "
  "une n'est pas au socle et le mot ne doit pas faire croire l'inverse ; une est nommée par les "
  "cadres sans être instrumentée ; la quatrième est portée par le plan et n'entre pas au socle.",
  dict(titre="QUATRE DÉRIVES, QUATRE RÉGIMES DE PREUVE", cols=2, items=[
      ("1", "Dérive d'outil", "La mieux documentée, parce qu'un chapitre l'a instruite.", "§ 39.2.1"),
      ("2", "Dérive de modèle", "N'est pas au socle — le mot ne doit pas faire croire l'inverse.", "§ 39.2.2"),
      ("3", "Dérive d'autonomie", "Nommée par les cadres ; le seul relevé d'instrumentation ne l'instrumente pas.", "§ 39.2.3"),
      ("4", "La quatrième source", "Portée par le plan, et elle n'entre pas au socle.", "§ 39.2.4"),
  ]))

f(39, "39.3", "f-39-03-incident",
  "Révoquer, confiner, imputer : la séquence de réponse à incident agentique.",
  "Les trois leviers de la reponse a incident agentique et leur ordre.",
  "§ 39.3, chapitre 39.", r"^## § 39\.4 ", "chaine",
  "⚠ Le premier levier suppose ce que le ch. 20 § 20.6 déclare absent : aucun mécanisme de "
  "révocation en cascade n'est documenté. Révoquer à la racine ne dit rien de ce qui en a été "
  "dérivé, et la séquence ne se déroule pas d'elle-même.",
  dict(titre="TROIS LEVIERS, DANS CET ORDRE", maillons=[
      ("Révoquer", "retirer ce qui autorise — et la cascade n'est pas documentée"),
      ("Confiner", "borner le rayon plutôt que prévenir — ch. 11 § 11.4.1"),
      ("Imputer", "rattacher l'action à un responsable — Q-E de la grille"),
  ]))

f(40, "40.2", "f-40-02-grille-minimale",
  "La grille minimale d'indicateurs, et ce qui manque pour que chacun se calcule.",
  "Les quatre grandeurs de la grille minimale d'indicateurs de l'AgentOps.",
  "Tableau 40.2, § 40.2.2, chapitre 40 — construction d'auteur en totalité.",
  r"^### 40\.2\.3 ", "bandes",
  "⚠ CONSTRUCTION D'AUTEUR EN TOTALITÉ, et aucune valeur n'est prescrite. La colonne qui compte "
  "est la dernière : pour chacune des quatre grandeurs, quelque chose manque encore pour que "
  "l'indicateur se calcule — et l'une d'elles n'a même pas d'exigence de délai au socle.",
  dict(titre="QUATRE GRANDEURS, QUATRE MANQUES", cols=2, items=[
      ("1", "Disponibilité du parc", "Dénombrement des agents identifiables à l'instant t.", "E-23 attend un inventaire — attente sous condition"),
      ("2", "Couverture de traçabilité", "Part des actions tracées et rattachées à une identité émise et à un mandat.", "l'art. 12.1 impose la restitution des facteurs et paramètres sur demande"),
      ("3", "Délai de révocation", "Durée entre la décision de retrait et le refus par le dernier point d'application.", "aucun cadre canadien instruit ne fixe de délai de propagation"),
      ("4", "Fraîcheur des évaluations", "Âge de la dernière évaluation de chaque agent, rapporté à un seuil.", "deux attentes, aucune exigence"),
  ]))

f(40, "40.6", "f-40-06-cout-par-resultat",
  "Du coût par jeton au coût par résultat métier.",
  "Le deplacement de la grandeur economique du cout par jeton vers le cout par resultat metier.",
  "§ 40.6.2, chapitre 40, et ch. 24 § 24.2.5.", r"^### 40\.6\.3 ", "paire",
  "Le coût par jeton est mesurable et trompeur : il baisse quand l'agent échoue vite. Le coût par "
  "résultat est la seule grandeur qui rende l'effet de plateforme visible — et c'est aussi celle "
  "qui exige de savoir ce qu'est un résultat, ce qu'aucun compteur ne dit.",
  dict(titre_g="COÛT PAR JETON", titre_d="COÛT PAR RÉSULTAT MÉTIER",
       gauche=("Ce que l'infrastructure facture",
               ["Immédiatement mesurable",
                "Baisse quand l'agent échoue vite",
                "Ne dit rien de ce qui a été produit"],
               "une grandeur de fournisseur"),
       droite=("Ce que l'organisation obtient",
               ["Exige de définir le résultat",
                "Intègre les reprises et les échecs",
                "Rend l'effet de plateforme visible"],
               "la seule grandeur qui décide")))

f(41, "41.3", "f-41-03-registre-catalogue",
  "Registre gouverné et catalogue interne : deux objets, deux autorités.",
  "La distinction entre le registre gouverne, opposable a des tiers, et le catalogue interne.",
  "Tableau 41.2, § 41.3, chapitre 41 — construction d'auteur en totalité.",
  r"^## § 41\.4 ", "paire",
  "⚠ CONSTRUCTION D'AUTEUR EN TOTALITÉ. La différence qui compte n'est pas le contenu mais "
  "L'OPPOSABILITÉ : le catalogue n'est opposable à personne — c'est un instrument de gestion, "
  "non de preuve. Le confondre avec un registre fait croire à une preuve qui n'existe pas.",
  dict(titre_g="REGISTRE GOUVERNÉ (ch. 15)", titre_d="CATALOGUE INTERNE (ce chapitre)",
       accent_d=False,
       gauche=("Qu'un tiers vérifie une identité qu'il n'a pas émise",
               ["Opposable à des tiers, dans les limites du Livre II",
                "Porte l'ancrage — le verrou du Livre II",
                "Peuplé par l'émission"],
               "un instrument de preuve"),
       droite=("Que l'organisation énumère ce qu'elle a produit",
               ["Opposable à personne",
                "Porte le gabarit d'origine et l'état de certification",
                "Peuplé par la fabrique"],
               "un instrument de gestion")))

f(41, "41.4", "f-41-04-barriere-certification",
  "La barrière de certification : ce qu'un agent démontre avant d'être admis au maillage.",
  "La barriere de certification entre la fabrique et le maillage.",
  "§ 41.4, chapitre 41.", r"^## § 41\.5 ", "chaine",
  "⚠ La barrière est une CONSTRUCTION D'AUTEUR : aucun mécanisme du socle ne conditionne "
  "l'admission au maillage à une démonstration préalable. Ce que la figure montre est un patron "
  "proposé, non un dispositif documenté.",
  dict(titre="DU GABARIT À L'ADMISSION", maillons=[
      ("Gabarit gouverné", "ce qui se décide une fois pour tout le parc — § 41.2"),
      ("Agent produit", "instancié depuis le gabarit, inscrit au catalogue"),
      ("Barrière", "ce qu'il démontre avant d'entrer"),
      ("Maillage", "où la politique s'applique à l'arête — ch. 37"),
  ]))

f(41, "41.5", "f-41-05-boucle-reemission",
  "La boucle de réémission : de l'indicateur et de la dérive au gabarit corrigé.",
  "La boucle qui ramene un indicateur d'exploitation ou une derive au gabarit d'agent.",
  "§ 41.5, chapitre 41.", r"^## § 41\.6 ", "chaine",
  "⚠ La boucle suppose que la dérive soit DÉTECTÉE, et le ch. 39 § 39.2 établit que trois des "
  "quatre dérives ne sont pas instrumentées. Une boucle de correction dont l'entrée n'est pas "
  "mesurée ne se referme pas.",
  dict(titre="CE QUI REVIENT AU GABARIT", boucle=True, maillons=[
      ("Gabarit", "ce qui se décide une fois pour tout le parc"),
      ("Parc", "les agents produits, admis, en exploitation"),
      ("Indicateurs et dérive", "ce que l'AgentOps mesure — ch. 39, ch. 40"),
      ("Correction", "portée au gabarit, non à l'agent"),
  ]))

f(42, "42.1", "f-42-01-matrice",
  "La matrice protocoles × textes canadiens : la couverture, et surtout les cases vides.",
  "La matrice croisant les protocoles agentiques et les textes reglementaires canadiens.",
  "Tableau 42.1, § 42.1, chapitre 42.", r"^## § 42\.2 ", "matrice",
  "⚠ Une case vide n'est pas un défaut du protocole : aucun de ces protocoles n'a été écrit pour "
  "répondre à un texte canadien. Le résultat n'est pas un palmarès, c'est une carte de ce que "
  "l'architecture devra compenser (§ 42.4).",
  dict(titre="CE QUE LES PROTOCOLES PORTENT DES EXIGENCES",
       colonnes=["Agent-outil", "Agent-agent", "Paiement agentique"],
       rangees=["E-23 — inventaire et cotation", "E-23 — surveillance continue",
                "Art. 12.1 — informer, expliquer, réviser", "ACVM 11-348 — adaptativité",
                "Cadre bancaire — interface d'accès"],
       cellules={(0, 0): ("—", ""), (0, 1): ("—", ""), (0, 2): ("—", ""),
                 (1, 0): ("—", ""), (1, 1): ("—", ""), (1, 2): ("—", ""),
                 (2, 0): ("—", ""), (2, 1): ("—", ""), (2, 2): ("~", "le mandat porte le consentement, non l'explication"),
                 (3, 0): ("—", ""), (3, 1): ("—", ""), (3, 2): ("—", ""),
                 (4, 0): ("—", ""), (4, 1): ("—", ""), (4, 2): ("—", "")},
       axes="~ partiel · — rien au socle. Se reporter au Tableau 42.1 pour la borne de chaque cellule."))

f(42, "42.3", "f-42-03-renversement",
  "Les trois espèces de vide, et le renversement qu'elles produisent.",
  "Les trois especes de vide de la matrice, et le renversement de lecture qu'elles imposent.",
  "§ 42.3.1 et § 42.3.2, chapitre 42.", r"^### 42\.3\.3 ", "bandes",
  "Le renversement est LE RÉSULTAT LE PLUS UTILE DU CHAPITRE : la question cesse d'être « quel "
  "protocole répond à quelle exigence » pour devenir « qu'est-ce que l'architecture doit porter "
  "que rien ne porte ». Les cinq zones du § 42.4 en sont la réponse.",
  dict(titre="TROIS VIDES, ET CE QU'ILS NE VEULENT PAS DIRE", cols=3, items=[
      ("1", "Le protocole ne le porte pas", "Et ne prétend pas le porter.", "hors périmètre déclaré"),
      ("2", "Le socle ne le documente pas", "Absence de documentation, non fait négatif.", "degré 3"),
      ("3", "Le texte n'exige rien", "L'exigence supposée n'est pas dans l'instrument.", "ne pas faire dire plus"),
  ]))

f(42, "42.4", "f-42-04-zones-compensation",
  "Les cinq zones de compensation architecturale : ce que l'architecture doit porter là où rien ne le porte.",
  "Les cinq zones ou l'architecture doit compenser ce qu'aucun protocole ni texte ne porte.",
  "Tableau 42.2, § 42.4, chapitre 42 — construction d'auteur.", NOTE, "bandes",
  "⚠ CONSTRUCTION D'AUTEUR : le socle porte les termes de chaque ligne, il ne porte pas le lien "
  "qui les joint. Compenser n'est pas se conformer — une zone de compensation est un endroit où "
  "l'architecte répond de ce que personne n'a spécifié.",
  dict(titre="CINQ ZONES, CINQ COMPENSATIONS", cols=1, items=[
      ("Z1", "La production de la trace", "L'art. 12.1 exige les raisons, facteurs et paramètres ; une préimpression enseigne que la journalisation confiée aux agents « n'est généralement pas recommandée ».", "la trace doit être produite par le cadre, non par les agents"),
      ("Z2", "Le point d'arrêt humain", "L'art. 12.1 exige l'occasion de présenter ses observations à un membre du personnel en mesure de réviser.", "le socle ne documente d'humain dans aucun des trois protocoles"),
      ("Z3", "La détectabilité de l'auto-modification", "L'avis 11-348 capte l'adaptativité après déploiement ; E-23 attend une surveillance continue.", "un manifeste scinde l'auto-modification en adaptation et évolution"),
      ("Z4", "L'interface d'accès du cadre bancaire", "Le standard technique n'est pas désigné — fait négatif vérifié.", "traiter le standard comme une variable derrière une frontière d'abstraction"),
      ("Z5", "Le contenu et l'état", "Les réponses protocolaires établissent qui parle ; elles ne couvrent ni l'empoisonnement d'outils, ni l'injection d'invites, ni l'empoisonnement de mémoire.", "le confinement local — ch. 11 § 11.4.1"),
  ]))

f(43, "43.1", "f-43-01-six-couches",
  "Les six couches de l'architecture de référence unifiée, et ce que chacune ne porte pas.",
  "Les six couches de l'architecture de reference unifiee et la responsabilite de chacune.",
  "Tableau 43.1, § 43.1.1, chapitre 43.", r"^### 43\.1\.2 ", "pile",
  "⚠ LE DÉCOUPAGE EST IMPOSÉ PAR LE PLAN ; sa vertu est d'obliger à dire ce que chaque couche ne "
  "porte pas. Quatre réserves commandent la lecture du tableau source (§ 43.1.2), et deux des "
  "entrées de la couche d'exploitation sont exclues du socle consolidé pour dette de preuve.",
  dict(titre="SIX COUCHES, ET CE QUE CHACUNE TIENT", couches=[
      ("1", "Protocoles", "Accès aux outils, données typées, cadre d'autorisation ; délégation de pair à pair, cartes signées. Ne porte ni le sens, ni l'ancrage."),
      ("2", "Identité et registre", "Identités et gabarits d'identité sur des protocoles d'autorisation qui étendent les RFC plutôt qu'ils ne s'y conforment."),
      ("3", "Orchestration", "Tenir l'enchaînement, produire la trace. Taxonomie OO1-OO4, cinq propriétés, sept critères."),
      ("4", "Maillage", "Appliquer la politique à l'arête — siège ch. 37. Ne porte pas l'émission."),
      ("5", "Exploitation — AgentOps", "Seize métriques au grain de l'opération, aucune de parc ; la dimension d'agent est un nom, pas une identité."),
      ("6", "Gouvernance", "Inventaire, cotation, cycle de vie, documentation, surveillance."),
  ]))

f(43, "43.2", "f-43-02-agentifier",
  "Quand agentifier, quand s'abstenir.",
  "L'arbre de decision entre une orchestration deterministe et une orchestration agentique.",
  "§ 43.2.3, chapitre 43.", r"^## § 43\.3 ", "arbre",
  "⚠ La grille est un CRITÈRE D'AUTEUR : le socle ne porte pas de règle d'abstention. Elle "
  "réordonne ce que les chapitres établissent — elle n'ajoute pas d'exigence, et elle ne dispense "
  "d'aucune.",
  dict(titre="LA QUESTION SE POSE AVANT L'ARCHITECTURE",
       racine="L'enchaînement peut-il être décidé d'avance ?",
       branches=[
           ("oui", "S'abstenir", "un cadre déterministe fait le travail, à coût prévisible et chemin testable — ch. 22 § 22.5"),
           ("non", "Agentifier, encadré", "le non-déterminisme apporte une valeur, et l'encadrement en borne le domaine — OO3 ou OO4"),
           ("sous le seuil", "Ne pas descendre", "autorisation et règlement restent déterministes — ch. 36 § 36.2.1"),
       ]))

f(43, "43.3", "f-43-03-points-de-controle",
  "Les cinq points de contrôle obligatoires, posés sur les six couches.",
  "Les cinq points de controle obligatoires de l'architecture de reference.",
  "Tableau 43.2, § 43.3, chapitre 43.", r"^## § 43\.4 ", "bandes",
  "⚠ « Obligatoires » qualifie LE PATRON, non un texte : aucun instrument réglementaire n'impose "
  "ces cinq points. Le tableau source distingue pour chacun ce que le socle porte et ce qui est "
  "de l'auteur — et la figure ne dispense pas de l'y lire.",
  dict(titre="CINQ POINTS, ET LEUR COUCHE", cols=1, items=[
      ("1", "L'émission", "Une identité et ses pièces, avant toute invocation.", "couche identité et registre — ch. 15, ch. 16"),
      ("2", "L'admission", "Le verdict d'entrée au maillage, et sa durée de validité.", "couche maillage — ch. 18, ch. 20"),
      ("3", "L'arête", "La politique appliquée à chaque passage.", "couche maillage — ch. 37"),
      ("4", "La trace", "Produite par le cadre, non par les agents.", "couche orchestration — ch. 38, zone Z1"),
      ("5", "Le point d'arrêt humain", "L'occasion de réviser, exigée par l'art. 12.1.", "couche gouvernance — zone Z2"),
  ]))

f(43, "43.5", "f-43-05-echelles-homonymes",
  "Trois échelles d'autonomie homonymes : « copilote » ne désigne pas la même chose trois fois.",
  "Les trois echelles d'autonomie homonymes du Vol. I, et le rang de copilote dans chacune.",
  "Tableau 43.3, § 43.5.1, chapitre 43.", r"^### 43\.5\.2 ", "bandes",
  "⚠ « COPILOTE » DÉSIGNE UN PALIER DE LA PREMIÈRE, LE NIVEAU 2 DE LA DEUXIÈME ET LE NIVEAU L0 "
  "DE LA TROISIÈME. Citer un rang sans nommer son échelle est une erreur de lecture que la somme "
  "commet ailleurs si elle n'y prend pas garde.",
  dict(titre="UN MÊME MOT, TROIS RANGS", cols=3, items=[
      ("1", "Quatre paliers non numérotés", "Assistance, copilote, orchestration sous revue, autonomie bornée.", "ce paragraphe, et ch. 14 § 14.4"),
      ("2", "Six niveaux, 0 à 5", "« Copilote » y est le niveau 2.", "ch. 4 § 4.1.4"),
      ("3", "Quatre niveaux L0-L3", "« Copilote » y est le niveau L0.", "Annexe H"),
  ]))

f(44, "44.0", "f-44-00-cadre-archimate",
  "Le cadre ArchiMate : trois domaines, trois aspects, et où les concepts agentiques se posent.",
  "Le cadre ArchiMate croisant les domaines et les aspects.",
  "§ 44.0.2 et § 44.0.3, chapitre 44.", r"^### 44\.0\.4 ", "matrice",
  "⚠ AUCUN ÉLÉMENT NATIF NE DÉSIGNE UN AGENT (§ 44.1.1). Les concepts agentiques ne se posent "
  "dans ce cadre que par SPÉCIALISATION d'éléments existants — c'est le verrou méthodologique du "
  "chapitre, et la figure le montre en laissant les cases telles qu'elles sont.",
  dict(titre="DOMAINES × ASPECTS, ET LE VERROU",
       colonnes=["Actif — structure", "Comportement", "Passif — objets"],
       rangees=["Business", "Application", "Technology"],
       cellules={(0, 0): ("", "Rôle, acteur, collaboration"),
                 (0, 1): ("", "Processus, fonction, interaction"),
                 (0, 2): ("", "Objet métier"),
                 (1, 0): ("", "Composant, interface, collaboration"),
                 (1, 1): ("", "Service, fonction, flux"),
                 (1, 2): ("", "Objet de données"),
                 (2, 0): ("", "Nœud, dispositif"),
                 (2, 1): ("", "Service technique"),
                 (2, 2): ("", "Artefact")},
       axes="Aucune case ne porte d'élément « agent » : la spécialisation est le seul recours."))

f(44, "44.1", "f-44-01-huit-patrons",
  "Les huit patrons de modélisation, et les éléments ArchiMate que chacun spécialise.",
  "Les huit patrons de modelisation des concepts agentiques en ArchiMate.",
  "§ 44.1.2 à § 44.1.8 et § 44.1.9, chapitre 44.", r"^### 44\.1\.9 ", "bandes",
  "⚠ CHAQUE PATRON EST UNE SPÉCIALISATION, non un élément du langage : le registre des "
  "stéréotypes (§ 44.1.9) est reproduit du Vol. I en [C]. Modéliser un agent en ArchiMate est un "
  "arbitrage de notation, et le § 44.9 dit ce que le formalisme ne sait pas dire.",
  dict(titre="HUIT PATRONS, ET LEURS ÉLÉMENTS", cols=2, items=[
      ("1", "Agent", "Application Component, Role, Collaboration.", "§ 44.1.2"),
      ("2", "Appel d'outil", "Application Service, Interface, Serving.", "§ 44.1.3"),
      ("3", "Interaction agent-agent", "Collaboration, Flow, Triggering.", "§ 44.1.4"),
      ("4", "Identité non humaine", "Role, structure active, overlay de sécurité.", "§ 44.1.5"),
      ("5", "Plan de contrôle d'agents", "Et la limite de la découverte dynamique.", "§ 44.1.6"),
      ("6", "Humain-agent", "Point d'arrêt, double regard, autonomie graduée.", "§ 44.1.7"),
      ("7", "Mémoire et ancrage", "Récupération et ancrage gouverné.", "§ 44.1.8"),
      ("8", "Registre des stéréotypes", "Ce qui tient les sept précédents ensemble.", "§ 44.1.9 — reproduit en [C]"),
  ]))

f(44, "44.8", "f-44-08-anti-patrons",
  "Les neuf anti-patrons, et le dernier — celui que le chapitre risque de commettre.",
  "Les neuf anti-patrons de modelisation agentique et leurs corrections.",
  "Tableau 44.2, § 44.8, chapitre 44.", r"^## § 44\.9 ", "bandes",
  "⚠ LE DERNIER EST CELUI QUE CE CHAPITRE RISQUE DE COMMETTRE — modéliser pour modéliser, et "
  "produire un blueprint que personne n'instancie. Le tableau source porte les neuf et leur "
  "correction ; la figure n'en donne que la structure.",
  dict(titre="NEUF ANTI-PATRONS, ET UNE CORRECTION CHACUN", cols=3, items=[
      ("1-3", "Sur la notation", "Confondre un agent avec un composant, un outil avec un service, une collaboration avec un flux.", "corrections au Tableau 44.2"),
      ("4-6", "Sur la gouvernance", "Modéliser l'autonomie sans son point d'arrêt, l'identité sans son ancrage, la trace sans son producteur.", "corrections au Tableau 44.2"),
      ("7-9", "Sur la portée", "Étendre le formalisme au-delà de ce qu'il sait dire — dont le dernier, que ce chapitre risque de commettre.", "§ 44.9"),
  ]))

f(45, "45.2", "f-45-02-vue-c1-c8",
  "La vue en couches C1-C8 du blueprint, avec ses statuts datés.",
  "Les huit couches du blueprint instancie, avec le statut date de chacune.",
  "Tableau 45.2, § 45.2, chapitre 45.", r"^## § 45\.3 ", "pile",
  "⚠ TOUS LES STATUTS SONT AUTO-DÉCLARÉS. Une couche « livrée » l'est au dire de son fournisseur, "
  "et la somme n'a rien vérifié en production. Instancier un blueprint ne prouve pas qu'il "
  "fonctionne — c'est ce que le § 45.0 pose, et le § 45.15 y revient.",
  dict(titre="HUIT COUCHES, HUIT STATUTS AUTO-DÉCLARÉS", couches=[
      ("C1", "Socle d'exécution", "Ce sur quoi les agents s'exécutent."),
      ("C2", "Protocoles", "Les deux axes, et le paiement — ch. 8, ch. 10."),
      ("C3", "Identité et registre", "L'émission et l'inscription — ch. 15, ch. 16."),
      ("C4", "Maillage", "Le point d'application à l'arête — ch. 37."),
      ("C5", "Orchestration", "L'enchaînement et sa trace — ch. 22, ch. 23."),
      ("C6", "Données et ancrage", "L'accès gouverné — ch. 5, ch. 24 § 24.4."),
      ("C7", "Exploitation", "Observabilité, évaluation, incident — ch. 38 à ch. 40."),
      ("C8", "Gouvernance", "Inventaire, cotation, documentation — ch. 25, ch. 42."),
  ]))

f(45, "45.8", "f-45-08-naissance-vie-mort",
  "Naissance, vie et mort d'un agent d'entreprise.",
  "Le cycle de vie complet d'un agent d'entreprise, de l'enregistrement a l'archivage probatoire.",
  "§ 45.8, § 45.9 et § 45.10, chapitre 45.", r"^## § 45\.11 ", "frise",
  "⚠ La mort est la partie la moins outillée : la révocation en cascade n'est pas documentée "
  "(ch. 20 § 20.6), et l'archivage probatoire suppose une trace qui vaille pièce — ce que le "
  "ch. 38 § 38.4 déclare dissymétrique au socle.",
  dict(titre="TROIS TEMPS, ET LE DERNIER EST LE MOINS OUTILLÉ", jalons=[
      ("Naissance", "Enregistrement", "émission du passeport, admission au maillage — § 45.8", "plein"),
      ("Vie", "Délégations", "vérifications par arête, traces, évaluations, renouvellements, migration post-quantique — § 45.9", "plein"),
      ("Mort", "Révocation", "cascade dans la chaîne de mandat, retrait du maillage, archivage probatoire — § 45.10", "creux"),
  ]))

f(45, "45.11", "f-45-11-flux-credit",
  "Flux 1 — la décision de crédit assistée par agents : le processus commande.",
  "Le flux de decision de credit assistee par agents, ou le processus commande l'enchainement.",
  "§ 45.11, chapitre 45.", r"^## § 45\.12 ", "chaine",
  "Le processus COMMANDE, et c'est ce qui range ce flux en OO3 ou OO4 : la décision de crédit "
  "est une décision opposable au client (ch. 27), et son enchaînement doit être lisible avant "
  "l'exécution.",
  dict(titre="LE PROCESSUS COMMANDE, LES AGENTS EXÉCUTENT", maillons=[
      ("Demande", "reçue, qualifiée"),
      ("Agents", "invoqués par le cadre, chacun sur une capacité bornée"),
      ("Décision", "rendue par le processus, non par un agent"),
      ("Restitution", "informer, expliquer, offrir la révision — art. 12.1"),
  ]))

f(45, "45.12", "f-45-12-flux-paiement",
  "Flux 2 — le paiement normalisé vers le rail de grande valeur : l'agent observe, le rail exécute.",
  "Le flux de paiement vers le rail de grande valeur, ou l'agent observe et le rail execute.",
  "§ 45.12, chapitre 45.", r"^## § 45\.13 ", "chaine",
  "⚠ L'AGENT N'EXÉCUTE PAS. Le rail est déterministe et le reste : c'est l'application directe "
  "de la stratification du ch. 36 § 36.2.1 et du seuil d'irréversibilité du ch. 31 § 31.1.1.",
  dict(titre="L'AGENT S'ARRÊTE AVANT LE SEUIL",
       rupture=("Le seuil de finalité : l'agent observe, il ne franchit pas.", 2),
       maillons=[
           ("Intention", "l'agent interprète, compose, prépare"),
           ("Instruction", "normalisée, validable par schéma"),
           ("Rail", "exécute, de façon déterministe"),
           ("Observation", "l'agent lit ce qui s'est passé"),
       ]))

f(45, "45.14", "f-45-14-souscription-vie",
  "L'exemple de bout en bout : la souscription vie augmentée, et sa variante en sinistres.",
  "La chaine de souscription vie augmentee de bout en bout, et les points ou le regime mord.",
  "§ 45.14, chapitre 45, et ch. 34 § 34.3.1.", r"^## § 45\.15 ", "chaine",
  "⚠ La donnée de santé est une donnée sensible, et la souscription est un domaine de HAUT "
  "RISQUE (ch. 34 § 34.3.5). Chaque maillon de cette chaîne est un endroit où le régime mord — "
  "et l'exemple ne prouve pas que le blueprint tienne : c'est ce que le § 45.15 arbitre.",
  dict(titre="UNE CHAÎNE D'ORCHESTRATION RÉGULÉE", maillons=[
      ("Proposition", "reçue, et le consentement recueilli"),
      ("Collecte", "dossiers, déclarations, données de santé"),
      ("Évaluation", "agents invoqués sur des capacités bornées"),
      ("Décision", "opposable — informer, expliquer, réviser"),
  ]))

f(46, "46.2", "f-46-02-compte-a-rebours",
  "Le compte à rebours vers le 1ᵉʳ mai 2027 : trois mouvements sur l'axe qui reste.",
  "Les trois mouvements de la feuille de route vers le 1er mai 2027, lus a rebours.",
  "§ 46.2, chapitre 46.", r"^## § 46\.3 ", "frise",
  "⚠ Le compte à rebours est RECALCULÉ, non recopié (§ 46.2.1) : une durée citée d'un document "
  "antérieur serait fausse dès sa publication. La feuille de route est un patron d'auteur ; "
  "aucun instrument n'impose cette séquence.",
  dict(titre="TROIS MOUVEMENTS, UNE DATE", rebours=True, jalons=[
      ("1ᵉʳ mai 2027", "E-23 opposable", "institutions financières fédérales", "plein"),
      ("−3", "Surveiller", "troisième mouvement — § 46.2.4", "creux"),
      ("−2", "Coter, puis encadrer", "deuxième mouvement — § 46.2.3", "creux"),
      ("−1", "Inventorier", "premier mouvement — § 46.2.2 ; sans lui, rien ne se cote", "plein"),
  ]))

f(46, "46.3", "f-46-03-jalons-externes",
  "Les jalons externes à surveiller, et le seul qui soit programmé.",
  "Les jalons externes a surveiller, avec leur regime epistemique.",
  "Tableau 46.2, § 46.3, chapitre 46.", NOTE, "bandes",
  "⚠ UN SEUL EST PROGRAMMÉ. Les autres sont attendus, annoncés ou spéculatifs — et bâtir une "
  "feuille de route sur un jalon spéculatif, c'est dater un plan sur une supposition. Les trois "
  "statuts épistémiques sont posés au ch. 49 § 49.0.1.",
  dict(titre="TROIS RÉGIMES, ET UN SEUL JALON DATÉ", cols=3, items=[
      ("1", "Programmé", "Une date opposable, portée par un instrument en vigueur.", "un seul des jalons"),
      ("2", "Annoncé", "Une cible communiquée par celui qui la porte.", "ni opposable ni garantie"),
      ("3", "Spéculatif", "Aucun jalon daté au socle.", "ne fonde aucune planification"),
  ]))
