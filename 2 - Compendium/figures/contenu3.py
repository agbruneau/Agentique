#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures du barème A — Livre III (chapitres 22 à 36)."""
from spec import f, NOTE  # noqa: F401

f(22, "22.1", "f-22-01-options-orchestration",
  "Les quatre options d'orchestration, lues par les deux axes qui les ordonnent.",
  "Les quatre options d'orchestration OO1 a OO4, selon qui detient la connaissance du processus "
  "et qui commande l'enchainement.",
  "Tableau 22.1, § 22.1, chapitre 22.", r"^## § 22\.2 ", "bandes",
  "La seule DISCONTINUITÉ est le passage d'OO2 à OO3 : c'est là que le commandement de "
  "l'enchaînement quitte les agents pour le cadre, et que l'enchaînement devient lisible avant "
  "l'exécution. Les autres passages sont graduels.",
  dict(titre="DEUX AXES : QUI SAIT, ET QUI COMMANDE", cols=2, items=[
      ("OO1", "Aucun cadre explicite", "Personne ne détient la connaissance du processus ; les agents commandent l'enchaînement.", "on ne peut rien lire avant l'exécution"),
      ("OO2", "Le cadre est dans l'invite", "Les agents détiennent la connaissance, par l'invite ou le contexte ; ils commandent encore.", "une description, sans force exécutoire établie"),
      ("OO3", "Le cadre seul", "Le cadre détient la connaissance — les agents l'ignorent — et il commande.", "l'enchaînement complet est lisible"),
      ("OO4", "Le cadre et les agents", "Les deux détiennent la connaissance ; le cadre commande.", "l'enchaînement complet est lisible"),
  ]))

f(22, "22.6", "f-22-06-ligne-de-partage",
  "Encadrer plutôt que superviser : la ligne de partage entre autonomie et automatisation.",
  "La ligne de partage entre autonomie encadree et automatisation.",
  "§ 22.6, chapitre 22.", r"^## § 22\.7 ", "paire",
  "⚠ La réponse examinée vient d'UN TEXTE — un manifeste —, non d'un consensus de la discipline. "
  "Que l'encadrement soit présenté comme le mécanisme premier de gouvernance est une thèse de "
  "ce texte, et la somme l'examine sans la ratifier.",
  dict(titre_g="AUTOMATISATION", titre_d="AUTONOMIE ENCADRÉE",
       gauche=("Le chemin est décidé d'avance",
               ["Ce qui peut arriver est énumérable",
                "La supervision porte sur l'exécution du chemin",
                "L'audit rejoue le chemin"],
               "restreindre les droits suffit"),
       droite=("Le chemin est décidé à l'exécution",
               ["Ce qui peut arriver ne s'énumère pas",
                "La supervision arrive après coup",
                "L'encadrement borne le domaine, non le chemin"],
               "d'où l'encadrement comme mécanisme premier")))

f(22, "22.10", "f-22-10-ecart-responsabilite",
  "L'écart de responsabilité : quatre parties, et personne qui ait décidé.",
  "Les quatre parties entre lesquelles l'imputabilite juridique reste indeterminee.",
  "§ 22.10, chapitre 22 — préparé ici, exploité au ch. 29 § 29.3.", NOTE, "bandes",
  "⚠ La section PRÉPARE l'écart, elle ne le traite pas : l'imputabilité du comportement émergent "
  "est au ch. 29 § 29.3. L'indétermination est celle du manifeste, et la somme n'y répond pas — "
  "elle en fixe le lieu.",
  dict(titre="QUATRE PARTIES, UNE IMPUTABILITÉ INDÉTERMINÉE", cols=4, items=[
      ("1", "Le développeur", "Qui a écrit l'agent.", ""),
      ("2", "L'organisation", "Qui impose le cadre.", ""),
      ("3", "Le fournisseur", "Du modèle.", ""),
      ("4", "Le système", "Dont le comportement est émergent.", ""),
  ]))

f(23, "23.5", "f-23-05-patrons-situes",
  "Les patrons livrés, situés sur la taxonomie du ch. 22 — et celui que le niveau de preuve ne permet pas de situer.",
  "Les patrons livres par les cadriciels d'orchestration, situes sur la taxonomie OO1 a OO4.",
  "Tableau 23.2, § 23.5, chapitre 23.", NOTE, "bandes",
  "⚠ Le POSITIONNEMENT EST UNE CONSTRUCTION D'AUTEUR. Le socle établit ce que chaque produit "
  "livre ; il ne le situe pas sur la taxonomie. Un patron dont le régime de preuve est un simple "
  "repérage [C] ne reçoit AUCUN positionnement — et c'est le cas de l'un des cinq.",
  dict(titre="CE QUE LE SOCLE ÉTABLIT, ET CE QUE L'AUTEUR EN TIRE", cols=1, items=[
      ("OO3/OO4", "Workflows à base de graphes", "Le graphe est un cadre explicite extérieur aux agents — le rang dépend de ce que les agents invoqués savent du processus.", "Agent Framework, GA 1.0"),
      ("—", "Points de contrôle", "Instrument de la propriété de traçabilité, non une option d'orchestration en soi.", "limites en multi-conteneurs"),
      ("—", "Humain-dans-la-boucle", "Point d'arrêt de supervision ; critère de sélection du § 22.3, non un positionnement.", "Agent Framework, GA 1.0"),
      ("aucun", "Agents durables", "Aucun positionnement proposé : le niveau de preuve ne le permet pas.", "repérage [C], ne porte aucun fait central"),
      ("OO1", "Bus d'événements", "Le protocole agent-agent sans cadre de processus explicite est la définition même d'OO1.", "préversion publique sur dorsale rejouable"),
  ]))

f(24, "24.1", "f-24-01-acteur-du-tissu",
  "L'agent comme acteur du tissu d'intégration : une dualité de rôles.",
  "L'agent consommateur et l'agent producteur dans le tissu d'integration d'entreprise.",
  "§ 24.1.1, chapitre 24.", r"^### 24\.1\.2 ", "paire",
  "La dualité RECOUPE celle de l'acteur émetteur et récepteur du ch. 1 : ce n'est pas une "
  "nouveauté agentique, c'est le tissu existant qui reçoit un acteur de plus. Ce qui change "
  "n'est pas le rôle, c'est que son enchaînement n'est plus décidé d'avance.",
  dict(titre_g="AGENT-CONSOMMATEUR", titre_d="AGENT-PRODUCTEUR",
       gauche=("Il invoque, il lit, il interroge",
               ["Invoque une API ou un outil",
                "Lit un flux d'événements",
                "Interroge une source pour fonder son raisonnement"],
               "l'acteur récepteur du ch. 1"),
       droite=("Il déclenche, il émet, il écrit",
               ["Déclenche un workflow",
                "Émet un événement",
                "Écrit dans un système d'information"],
               "l'acteur émetteur du ch. 1")))

f(24, "24.5", "f-24-05-trois-echelles",
  "Les trois échelles d'orchestration, ordonnées par structure de propriété.",
  "Les trois echelles d'orchestration : intra-equipe, inter-equipes, inter-organisations.",
  "Tableau 24.1, § 24.5.2, chapitre 24.", r"^### 24\.5\.3 ", "bandes",
  "⚠ La troisième échelle ne prolonge pas les deux premières : à la frontière de confiance, "
  "LA NATURE DU PROBLÈME CHANGE — contrats juridiques, responsabilité distribuée, aucune autorité "
  "centrale commune. C'est ce que le § 24.7 traite, et non une orchestration plus grande.",
  dict(titre="TROIS ÉCHELLES, ET UNE RUPTURE À LA TROISIÈME", cols=3, items=[
      ("1", "Intra-équipe", "Domaine unique, un propriétaire responsable.", "plan de contrôle homogène, contexte partagé sans friction"),
      ("2", "Inter-équipes", "Plusieurs propriétaires internes.", "accords de niveau de service croisés, contrats d'interface stables, attribution des défaillances"),
      ("3", "Inter-organisations", "Une frontière de confiance : contrats juridiques, responsabilité distribuée, aucune autorité centrale.", "la nature du problème change — § 24.7"),
  ]))

f(25, "25.1", "f-25-01-calendrier-e23",
  "E-23 : de la publication à la date opposable.",
  "Le calendrier de la ligne directrice E-23, de sa publication a son entree en vigueur.",
  "§ 25.1, chapitre 25, et Tableau 26.1.", r"^## § 25\.2 ", "frise",
  "La date opposable est celle de l'ENTRÉE EN VIGUEUR, non celle de la publication : entre les "
  "deux, une institution n'a aucune obligation nouvelle — et après, elle en a sans que le texte "
  "ait changé d'un mot.",
  dict(titre="UNE PUBLICATION, UNE ENTRÉE EN VIGUEUR", jalons=[
      ("11 sept. 2025", "Version finale publiée", "le texte est arrêté ; aucune obligation nouvelle n'en découle encore", "plein"),
      ("1ᵉʳ mai 2027", "Date opposable", "institutions financières fédérales ; le texte n'a pas changé, sa portée si", "creux"),
  ]))

f(25, "25.3", "f-25-03-inference-agentique",
  "Comment un texte qui ne nomme pas l'agent l'atteint quand même.",
  "L'inference par laquelle E-23 couvre l'agentique sans la nommer.",
  "§ 25.3, chapitre 25.", r"^## § 25\.4 ", "chaine",
  "⚠ CHAQUE MEMBRE PORTE DU POIDS, et le dernier n'est pas du même ordre que les deux premiers : "
  "que la couverture soit « tenue pour acquise » par des analystes n'est pas qu'elle soit établie "
  "par le texte. La formulation est imposée par la méthode, et rendue dans sa substance.",
  dict(titre="TROIS MEMBRES, ET UN SEUL EST UNE LECTURE", maillons=[
      ("Le texte", "E-23 ne nomme ni l'agentique, ni les agents"),
      ("La définition", "sa définition de « modèle » englobe les méthodes d'IA et d'apprentissage automatique"),
      ("La lecture", "d'où une couverture implicite, que les analystes juridiques canadiens tiennent pour acquise"),
  ]))

f(26, "26.3", "f-26-03-vide-federal",
  "Le vide fédéral, et les quatre instruments qui portent effectivement la charge.",
  "Les quatre instruments qui portent la charge reglementaire en l'absence de loi federale.",
  "Tableau 26.1, § 26.3, chapitre 26, au gel du 27 juillet 2026.", NOTE, "bandes",
  "⚠ Les quatre ne sont pas de même nature : l'un relève du droit général des renseignements "
  "personnels et non du secteur financier, et le quatrième NE CRÉE NI NE MODIFIE aucune exigence. "
  "Un instrument qui porte la charge n'est pas nécessairement un instrument qui l'impose.",
  dict(titre="QUATRE INSTRUMENTS, QUATRE RÉGIMES", cols=2, items=[
      ("1", "E-23", "Risque de modèle, fédéral prudentiel. Version finale publiée le 11 septembre 2025.", "opposable le 1ᵉʳ mai 2027 — ch. 25"),
      ("2", "Ligne directrice IA de l'AMF", "Québec, sectoriel. Finale — jamais « en attente » ni « en projet ».", "publication non datée au jour près — ch. 27"),
      ("3", "Art. 12.1 de la Loi 25", "Québec, droit général des renseignements personnels. En vigueur.", "opposable depuis le 22 septembre 2023 — ch. 27"),
      ("4", "Avis 11-348 des ACVM", "Valeurs mobilières. Publié le 5 décembre 2024 ; ne crée ni ne modifie aucune exigence.", "aucune date — les lois existantes s'appliquent — ch. 28"),
  ]))

f(27, "27.2", "f-27-02-article-12-1",
  "L'articulation de l'article 12.1 : une obligation inconditionnelle, trois informations dues sur demande, un alinéa distinct.",
  "L'articulation de l'article 12.1 de la Loi 25 : ce qui est du sans demande et ce qui est du sur demande.",
  "Tableau 27.2, § 27.2, chapitre 27, relevé du 21 juillet 2026 sur le texte officiel.",
  r"^## § 27\.3 ", "arbre",
  "⚠ La troisième information due sur demande — LE DROIT DE FAIRE RECTIFIER — était omise par "
  "l'entrée héritée H-06 du Vol. III, et l'alinéa distinct est le seul que le socle individualise : "
  "il est hors de l'énumération, non son quatrième terme.",
  dict(titre="UNE DÉCISION EXCLUSIVEMENT AUTOMATISÉE EST RENDUE",
       racine="Une décision fondée exclusivement sur un traitement automatisé est rendue",
       branches=[
           ("sans demande", "Informer", "que la décision a été rendue, au plus tard au moment de la décision — l'information l'accompagne"),
           ("sur demande", "Trois informations", "1° les renseignements utilisés ; 2° les raisons, facteurs et paramètres ; 3° le droit de faire rectifier"),
           ("alinéa distinct", "Réviser", "l'occasion de présenter ses observations à un membre du personnel en mesure de réviser la décision"),
       ]))

f(27, "27.3", "f-27-03-exclusivement",
  "Le critère « exclusivement » : l'adverbe sur lequel tout se joue.",
  "L'arbre de decision par lequel le critere d'exclusivite declenche ou ecarte l'article 12.1.",
  "§ 27.3, chapitre 27.", r"^## § 27\.4 ", "arbre",
  "⚠ LE TEXTE NE DÉFINIT PAS CE QUE L'EXCLUSIVITÉ EXCLUT. Que l'intervention humaine "
  "significative écarte l'article est l'analyse d'un cabinet, non une position du législateur — "
  "et le § 27.7 cartographie les lectures SANS RENDRE DE VERDICT.",
  dict(titre="TOUT SE JOUE SUR UN ADVERBE",
       racine="Le traitement est-il exclusivement automatisé ?",
       branches=[
           ("oui", "L'article s'applique", "les obligations du § 27.2 se déclenchent, l'information accompagnant la décision"),
           ("intervention humaine", "L'article serait écarté", "selon l'analyse d'un cabinet — nuance déterminante pour les systèmes agentiques, et non tranchée"),
       ]))

f(29, "29.1", "f-29-01-table-traduction",
  "La table de traduction : ce que chaque exigence impose au cadre, et le statut du lien.",
  "La traduction des exigences reglementaires en contraintes de cadre deterministe.",
  "Tableau 29.1, § 29.1, chapitre 29 — repris intact de sa source.", r"^## § 29\.2 ", "bandes",
  "⚠ LE STATUT DU LIEN EST LA COLONNE QUI COMPTE. Plusieurs liens sont des INFÉRENCES D'AUTEUR, "
  "un est une LACUNE OUVERTE — le contenu de la ligne directrice de l'AMF n'est pas au socle, et "
  "rien n'en est dérivable. Traduire n'est pas lire (§ 29.0).",
  dict(titre="SIX EXIGENCES, ET CE QUE LE CADRE DOIT PORTER", cols=2, items=[
      ("E-23", "Inventaire", "Un inventaire d'entreprise des modèles à risque non négligeable, exact et tenu à jour.", "le cadre doit porter l'ensemble de ce qui peut être invoqué"),
      ("E-23", "Cotation", "Une cote de risque par modèle ; le degré d'autonomie est un facteur qualitatif.", "la cote doit être connue au point d'invocation"),
      ("E-23", "Cycle de vie", "Cinq composantes, « pas nécessairement séquentielles » — dont la mise hors service.", "la mise hors service s'interpose entre la décision et l'invocation"),
      ("E-23", "Documentation", "Usages approuvés, limites, dépendances, sources de données.", "l'usage approuvé doit être opposable, donc porté par ce qui autorise"),
      ("Art. 12.1", "Informer", "Au plus tard au moment de la décision — la seule obligation subordonnée à aucune demande.", "le moment de la décision doit être un événement émis, identifiable et daté"),
      ("Art. 12.1", "Réviser", "L'occasion de présenter ses observations à un membre du personnel.", "un point de reprise, et des effets aval bornés — donc défaisables"),
  ]))

f(30, "30.2a", "f-30-02a-qualification-multiple",
  "La grille de qualification multiple : un agent financier peut relever des trois régimes à la fois.",
  "Les trois qualifications possibles d'un agent financier : systeme TIC, modele, decision automatisee.",
  "Tableau 30.1, § 30.2.1, chapitre 30.", r"^### 30\.2\.2 ", "venn",
  "⚠ Le point méthodologique décisif est LA COEXISTENCE : les trois qualifications ne s'excluent "
  "pas. Un agent qui s'exécute chez un tiers, qui décide, et dont la décision est opposable au "
  "client relève des trois régimes en même temps — et de leurs trois calendriers.",
  dict(titre="TROIS DÉCLENCHEURS, ET ILS SE CUMULENT", centre="les trois",
       ensembles=[("Système TIC", "dès qu'il s'exécute chez un tiers"),
                  ("Modèle", "dès qu'il décide"),
                  ("Décision automatisée", "dès qu'elle est opposable au client")]))

f(31, "31.1a", "f-31-01a-irreversibilite",
  "L'irréversibilité : le point de la chaîne au-delà duquel rien ne se défait.",
  "Le seuil de finalite du reglement sur la chaine de paiement.",
  "§ 31.1.1, chapitre 31 — siège du patron d'irréversibilité pour toute la somme.",
  r"^### 31\.1\.2 ", "chaine",
  "⚠ SIÈGE DU PATRON POUR TOUTE LA SOMME : il est posé ici une seule fois et n'est re-dérivé "
  "nulle part. Ce qui précède le seuil se corrige ; ce qui le franchit se COMPENSE, et une "
  "compensation est une seconde opération, non une annulation (ch. 48 § 48.3).",
  dict(titre="AVANT LE SEUIL, APRÈS LE SEUIL",
       rupture=("Le seuil est la finalité du règlement — il ne se rejoue pas.", 2),
       maillons=[
           ("Intention", "se reformule sans conséquence"),
           ("Instruction", "se corrige tant qu'elle n'est pas passée"),
           ("Règlement", "franchi, il est final"),
           ("Compensation", "une seconde opération, jamais une annulation"),
       ]))

f(31, "31.1b", "f-31-01b-double-qualification",
  "La double-qualification : l'agent comme modèle et comme tiers TIC.",
  "La double qualification d'un agent financier, a la fois modele et service TIC fourni par un tiers.",
  "§ 31.1.4, chapitre 31 — siège du patron-signature pour toute la somme.",
  r"^## § 31\.2 ", "paire",
  "⚠ SIÈGE DU PATRON-SIGNATURE POUR TOUTE LA SOMME, et il n'est re-dérivé nulle part : le "
  "ch. 30 § 30.2.1 déclare lui-même ne faire que l'instancier. Les deux qualifications ne se "
  "choisissent pas — elles se cumulent, avec leurs deux régimes.",
  dict(titre_g="L'AGENT COMME MODÈLE", titre_d="L'AGENT COMME TIERS TIC",
       gauche=("Parce qu'il décide",
               ["Inventaire, cotation, cycle de vie",
                "Documentation des usages approuvés",
                "Surveillance continue"],
               "régime du risque de modèle — ch. 25"),
       droite=("Parce qu'il s'exécute chez un tiers",
               ["Résilience opérationnelle",
                "Inscription au registre des tiers",
                "Continuité et sortie"],
               "régime de la résilience — § 30.2.2")))

f(31, "31.2", "f-31-02-substrat-semantique",
  "Les trois couches du substrat sémantique financier, et ce que l'agent tire de chacune.",
  "Les trois couches du substrat semantique financier : messagerie, capacite, ontologie.",
  "Tableau 31.2, § 31.2.1, chapitre 31 — repris du Vol. I en [C].", r"^### 31\.2\.2 ", "pile",
  "⚠ Repris du Vol. I en régime [C] : c'est une lecture d'un volume source, non un balayage "
  "conduit par la somme. La troisième couche est celle qui fait le garde-fou DÉTERMINISTE — "
  "les deux premières structurent, elles ne désambiguïsent pas.",
  dict(titre="TROIS COUCHES, TROIS APPORTS", couches=[
      ("1", "Messagerie / syntaxe", "Le format d'échange sur le fil. L'agent en tire des champs structurés et des messages validables par schéma."),
      ("2", "Modèle / capacité / cycle de vie", "Ce que fait une institution et comment ses opérations s'enchaînent. L'agent en tire le découpage en capacités bornées qui délimite son périmètre d'action."),
      ("3", "Ontologie / sémantique", "Le sens partagé et les relations logiques. L'agent en tire un garde-fou déterministe pour désambiguïser un terme avant d'agir."),
  ]))

f(31, "31.5", "f-31-05-quatre-plans",
  "Les quatre plans où circule la donnée régulée dans une boucle agentique.",
  "Les quatre plans de circulation de la donnee regulee : inference, plongements, traces, journaux.",
  "Tableau 31.4, § 31.5.1, chapitre 31 — repris du Vol. I en [C].", r"^### 31\.5\.2 ", "bandes",
  "⚠ LES TROIS PREMIERS SONT RAREMENT PENSÉS EN TERMES DE RÉSIDENCE. Une architecture qui ne "
  "couvre que le stockage laisse circuler la donnée régulée sur trois plans qu'elle ne voit pas — "
  "et l'invite contient invariablement du contexte client, même quand la sortie paraît anodine.",
  dict(titre="QUATRE PLANS, ET LA RÉSIDENCE DOIT LES COUVRIR TOUS", cols=2, items=[
      ("1", "Inférence", "L'invite soumise au modèle contient invariablement du contexte client — extraits de dossier, montants, identifiants.", "rarement pensé en termes de résidence"),
      ("2", "Plongements", "La représentation vectorielle du contenu régulé.", "rarement pensé en termes de résidence"),
      ("3", "Traces", "Ce que l'observabilité conserve de la boucle.", "rarement pensé en termes de résidence"),
      ("4", "Journaux d'audit", "Ce qui vaut pièce, et se conserve pour cela.", "le seul plan habituellement traité"),
  ]))

f(32, "32.4", "f-32-04-maillon-absent",
  "Le cadre bancaire axé sur le consommateur : la chaîne, et le maillon qui manque.",
  "La chaine de la loi au standard technique du cadre bancaire ouvert, et le maillon absent.",
  "§ 32.4, chapitre 32.", NOTE, "chaine",
  "⚠ C'est un FAIT NÉGATIF VÉRIFIÉ, non une absence de documentation — et c'est la formulation "
  "la plus stricte du Livre. L'état de la désignation est porté par le ch. 30 § 30.3, et il "
  "n'est pas doublé ici.",
  dict(titre="LA LOI IMPOSE UN STANDARD TECHNIQUE UNIQUE",
       rupture=("Sans organisme désigné, pas de standard ; sans standard, pas d'interface — la chaîne s'arrête ici.", 1),
       maillons=[
           ("La loi", "impose un standard technique unique"),
           ("La désignation", "par arrêté du ministre des Finances, d'un organisme de normalisation"),
           ("Le standard", "reste à fixer"),
           ("L'interface", "n'existe pas"),
       ]))

f(33, "33.2", "f-33-02-chronologie-rtr",
  "La chronologie du rail de paiement en temps réel, telle que l'exploitant la communique.",
  "La chronologie du rail de paiement en temps reel, de 2023 a la mi-2026.",
  "Tableau 33.1, § 33.2, chapitre 33.", r"^## § 33\.3 ", "frise",
  "⚠ La chronologie est celle que L'EXPLOITANT COMMUNIQUE : elle décrit un avancement déclaré, "
  "non un rail en service. Le dernier jalon est en cours, et aucune date de mise en service "
  "n'y figure.",
  dict(titre="UN AVANCEMENT DÉCLARÉ, ET SON DERNIER JALON OUVERT", jalons=[
      ("juin 2023", "Composante d'échange", "livrée par un premier partenaire", "plein"),
      ("16 avr. 2024", "Reprise du programme", "deux nouveaux partenaires de livraison et d'exploitation", "plein"),
      ("T3 2025", "Compensation et règlement", "construction complétée", "plein"),
      ("T4 2025", "Tests internes", "complétés", "plein"),
      ("T1 2026", "Acceptation utilisateur", "complétée", "plein"),
      ("mi-2026", "Tests industriels", "en cours", "creux"),
  ]))

f(35, "35.0", "f-35-00-classes-acces",
  "Les trois classes d'accès documentaire, et ce que chacune autorise à écrire.",
  "Les trois classes d'acces documentaire du chapitre d'etudes de cas, avec leur cardinal.",
  "Tableau 35.1, § 35.0, chapitre 35, au gel du Vol. II.", r"^## § 35\.1 ", "bandes",
  "⚠ La troisième classe est une ABSENCE DOCUMENTÉE, non une absence d'activité (§ 35.8). Tout "
  "le chapitre se lit à travers cette échelle : un cas de la première classe et un cas de la "
  "troisième ne s'opposent pas au même régime de preuve.",
  dict(titre="DIX CAS, TROIS RÉGIMES DE PREUVE", cols=3, items=[
      ("5", "Sources primaires directement accessibles", "Trois communiqués et deux rapports annuels.", "aucune réserve d'accès"),
      ("4", "Accès dégradé", "Page rendue par script vérifiée par index ; domaines refusant le chargement automatisé, lus sur miroirs ; rapport trop volumineux pour extraction complète.", "la réserve accompagne chaque énoncé"),
      ("1", "Aucune source primaire", "Absence documentée.", "non absence d'activité — § 35.8"),
  ]))

f(36, "36.2a", "f-36-02a-stratification-paiement",
  "La stratification de la chaîne de paiement, et l'endroit où l'agentique est admise.",
  "Les trois couches de la chaine de paiement, et l'admission de l'agentique a chacune.",
  "Tableau 36.1, § 36.2.1, chapitre 36 — repris du Vol. I en [C].", r"^### 36\.2\.2 ", "pile",
  "⚠ L'ERREUR DE CONCEPTION À PROSCRIRE est de laisser le non-déterminisme descendre sous la "
  "première couche. L'autorisation est une VÉRIFICATION, non une délibération ; le règlement "
  "doit rester déterministe et fondé sur des règles, identique à ce qu'il est aujourd'hui.",
  dict(titre="TROIS COUCHES, UNE SEULE ADMET L'AGENTIQUE", inverse=False, couches=[
      ("3", "Règlement", "La finalité. NON — doit rester déterministe et fondé sur des règles."),
      ("2", "Autorisation", "Vérifier qu'une instruction est conforme à un mandat préexistant : montant, bénéficiaire, fenêtre temporelle, politique de consentement. NON — vérification, non délibération."),
      ("1", "Intention, orchestration, négociation", "Interpréter un besoin exprimé en langage naturel, comparer des offres, composer un panier, préparer une instruction. OUI — c'est là que le non-déterminisme apporte une valeur réelle."),
  ]))

f(36, "36.2b", "f-36-02b-trou-responsabilite",
  "L'achat non intentionnel : le trou que les cadres de litige existants ne couvrent pas.",
  "Le patron de risque de l'achat agentique non intentionnel et les trois causes qui y menent.",
  "§ 36.2.6, chapitre 36.", r"^### 36\.2\.7 ", "bandes",
  "⚠ Ce sont L'IRRÉVERSIBILITÉ ET LA DÉLÉGATION COMBINÉES qui ouvrent le trou — ni l'une ni "
  "l'autre séparément. L'agent exécute DANS LES LIMITES APPARENTES de son mandat : il n'y a ni "
  "fraude ni dépassement, et c'est pourquoi les cadres de litige ne s'y appliquent pas.",
  dict(titre="TROIS CAUSES, UN MÊME RÉSULTAT", cols=3, items=[
      ("1", "Dérive d'interprétation", "De l'intention exprimée par le mandant.", ""),
      ("2", "Empoisonnement", "Du contexte ou de la mémoire — ch. 19.", ""),
      ("3", "Collusion", "Entre agents.", ""),
  ]))
