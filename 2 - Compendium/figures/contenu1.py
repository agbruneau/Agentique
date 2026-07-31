#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures du barème A — Livre I (chapitres 1 à 11)."""
from spec import f, NOTE  # noqa: F401

# =============================== Livre I ===============================

f(1, "1.3", "f-01-03-soa-vers-maillage",
  "De la SOA au maillage : ce que chaque étage déplace, et le couplage qui décroît.",
  "Quatre etages d'architecture d'integration, de la SOA au maillage de services, "
  "et le couplage que chacun deplace.",
  "§ 1.3, chapitre 1.", r"^## § 1\.4 ", "bandes",
  "Chaque étage déplace le couplage, aucun ne le supprime. Le maillage n'est ici que le "
  "socle transposable — sa déclinaison agentique est le ch. 37, et ce chapitre ne la construit pas.",
  dict(titre="QUATRE ÉTAGES, UN COUPLAGE QUI SE DÉPLACE", fleches=True, cols=4, items=[
      ("1", "SOA", "Contrat de service explicite, découverte, composition.", "§ 1.3.1"),
      ("2", "ESB", "Le bus centralise routage et transformation.", "§ 1.3.2"),
      ("3", "Microservices", "Décentralisation, communication inter-services.", "§ 1.3.3"),
      ("4", "Maillage", "Les préoccupations transversales quittent chaque service.", "§ 1.3.4"),
  ]))

f(1, "1.5", "f-01-05-exactement-une-fois",
  "Livraison et traitement : pourquoi « exactement une fois » n'est pas une garantie de livraison.",
  "Les trois garanties de livraison d'un courtier de messages, et la seule composition "
  "qui rende un traitement exactement-une-fois.",
  "§ 1.5.2, chapitre 1 — siège cité par le ch. 48 § 48.2.", r"^## § 1\.6 ", "bandes",
  "La voie praticable n'est pas une livraison exactement-une-fois — irréalisable sous pannes, "
  "instance du problème des deux généraux — mais un TRAITEMENT exactement-une-fois : "
  "au-moins-une-fois composé avec un consommateur idempotent (ch. 48 § 48.2).",
  dict(titre="TROIS GARANTIES DE LIVRAISON", cols=3, items=[
      ("1", "Au plus une fois", "Perte possible, jamais de doublon.", ""),
      ("2", "Au moins une fois", "Jamais de perte, doublons possibles.", ""),
      ("3", "Exactement une fois", "Irréalisable comme garantie de livraison sous pannes.", ""),
  ]))

f(2, "2.1", "f-02-01-compatibilite-schema",
  "Les quatre régimes de compatibilité de schéma, et le sens d'évolution que chacun protège.",
  "Les quatre regimes de compatibilite de schema : ascendante, descendante, complete, transitive.",
  "Tableau 2.1, § 2.1.5, chapitre 2.", r"^## § 2\.2 ", "bandes",
  "La compatibilité transitive est la seule qui interdise la dérive cumulative que des sauts "
  "successifs, compatibles deux à deux, peuvent produire.",
  dict(titre="QUATRE RÉGIMES, DEUX SENS D'ÉVOLUTION", cols=2, items=[
      ("1", "Ascendante", "Un consommateur mis à jour lit des données produites selon l'ancien schéma.", "backward"),
      ("2", "Descendante", "Un consommateur resté sur l'ancien schéma lit des données produites selon le nouveau.", "forward"),
      ("3", "Complète", "Les deux à la fois : la mise à jour des deux parties dans un ordre quelconque.", "full"),
      ("4", "Transitive", "La garantie s'étend à toutes les versions antérieures, non à la seule précédente.", "transitive"),
  ]))

f(2, "2.3", "f-02-03-pile-web-semantique",
  "La pile du Web sémantique, et ce que chaque étage ajoute au graphe.",
  "La pile du Web semantique : RDF, RDFS, OWL, JSON-LD, et la validation par SHACL.",
  "§ 2.3.1 et § 2.3.3, chapitre 2.", r"^## § 2\.4 ", "pile",
  "Deux graphes fusionnent par simple union de leurs triplets — POURVU QU'ILS PARTAGENT DES "
  "IDENTIFIANTS. La pile ne fournit pas l'accord sémantique : elle le suppose, et c'est le "
  "même constat que la pile canonique du ch. 1 § 1.1.2 porte un étage plus bas.",
  dict(titre="CE QUE CHAQUE ÉTAGE AJOUTE", couches=[
      ("1", "RDF", "Triplets sujet-prédicat-objet ; chaque ressource porte un identifiant globalement résolvable."),
      ("2", "RDFS", "Vocabulaire et hiérarchies de classes et de propriétés."),
      ("3", "OWL", "Axiomes et inférence sur le graphe."),
      ("4", "JSON-LD", "Sérialisation ; le pont vers les piles de développement existantes."),
  ], notes=[("SHACL et ShEx", "La validation vient par-dessus : un contrat sémantique se pose "
             "sur le graphe, il n'en fait pas partie (§ 2.3.3)."),
            ("La propriété rare", "Fusionner deux schémas relationnels exige un projet ; "
             "fusionner deux graphes qui partagent des identifiants n'exige rien.")]))

f(3, "3.2", "f-03-02-saml-oauth-oidc",
  "SAML, OAuth 2.x et OpenID Connect : trois protocoles, et ce que chacun établit.",
  "Les trois protocoles d'identite federee et d'autorisation deleguee, et ce que chacun etablit.",
  "§ 3.2.1, chapitre 3.", r"^## § 3\.3 ", "bandes",
  "OAuth AUTORISE, il n'authentifie pas : l'employer comme preuve d'identité est précisément "
  "la confusion qu'OpenID Connect existe pour corriger. C'est aussi l'ambiguïté que le "
  "ch. 12 § 12.4 retrouve intacte quand le porteur du jeton est un agent.",
  dict(titre="TROIS PROTOCOLES, TROIS OBJETS", cols=3, items=[
      ("1", "SAML", "Fédération d'authentification par assertions, au navigateur.", "§ 3.2.1"),
      ("2", "OAuth 2.x", "Autorisation déléguée : l'accès à une ressource, jamais une identité.", "§ 3.2.1"),
      ("3", "OpenID Connect", "Une couche d'identité posée sur OAuth, qui lui manquait.", "§ 3.2.1"),
  ]))

f(3, "3.3", "f-03-03-zero-trust",
  "Du périmètre réseau au zero-trust : ce que la confiance cesse de dériver de la localisation.",
  "Comparaison du modele de perimetre reseau et du modele zero-trust.",
  "§ 3.3.1, chapitre 3, sur NIST SP 800-207.", r"^## § 3\.4 ", "paire",
  "NIST SP 800-207 nomme les composants — point de décision, point d'application, évaluation "
  "continue par requête. Il ne dit pas ce qu'un point d'application doit LIRE quand l'appelant "
  "est un agent : c'est l'objet du ch. 37, et le socle n'y répond pas davantage.",
  dict(titre_g="PÉRIMÈTRE RÉSEAU", titre_d="ZERO-TRUST",
       gauche=("La confiance dérive de la localisation",
               ["Dedans le périmètre : implicitement autorisé",
                "Dehors : authentifié à l'entrée, une fois",
                "Le déplacement latéral n'est pas vérifié"],
               "un mur, et ce qu'il laisse passer une fois franchi"),
       droite=("Aucune confiance n'est dérivée de la localisation",
               ["Authentification et autorisation à CHAQUE appel",
                "Point de décision et point d'application distincts",
                "TLS mutuel systématique entre charges de travail"],
               "SPIFFE/SPIRE porte l'identité de charge ; WIMSE l'étend")))

f(4, "4.1", "f-04-01-flux-ou-agent",
  "Flux de travail ou agent : qui tient la tuyauterie, le code ou le modèle.",
  "La distinction entre un flux de travail orchestre par du code et un agent ou le modele "
  "dirige son propre processus.",
  "§ 4.1.4, chapitre 4.", r"^## § 4\.2 ", "paire",
  "La dichotomie a un AUTEUR UNIQUE — c'est celle d'Anthropic (§ 4.1.1) —, et sa reprise "
  "massive par la littérature praticienne n'en fait pas un consensus de la discipline : "
  "elle en fait une convention de vocabulaire d'un éditeur, adoptée.",
  dict(titre_g="FLUX DE TRAVAIL", titre_d="AGENT",
       gauche=("Le code tient la tuyauterie",
               ["Modèles et outils orchestrés par des chemins de code prédéfinis",
                "Coût prévisible et économe",
                "Un chemin de code se teste",
                "Surface d'injection bornée"],
               "orchestration déterministe"),
       droite=("Le modèle tient la tuyauterie",
               ["Le modèle dirige dynamiquement son processus",
                "Coût non prévisible",
                "Une délibération émergente s'évalue statistiquement",
                "Surface d'injection élargie, irréductible au niveau du modèle"],
               "autonomie, et son prix")))

f(4, "4.2", "f-04-02-boucle-agentique",
  "La boucle agentique, et le critère d'arrêt qui la distingue d'un appel unique.",
  "La boucle percevoir, raisonner, agir, observer, et son critere d'arret.",
  "§ 4.2.1, chapitre 4.", r"^## § 4\.3 ", "chaine",
  "Ce qui fait l'agent n'est pas la boucle mais SON CRITÈRE D'ARRÊT — but atteint, budget "
  "d'appels épuisé, échec irrécupérable, demande d'intervention humaine. Sans critère, "
  "la boucle est un générateur de texte qui recommence.",
  dict(titre="LE MODÈLE AUGMENTÉ, ET SA BOUCLE DE CONTRÔLE", boucle=True, maillons=[
      ("Percevoir", "l'invite courante et les observations accumulées"),
      ("Raisonner", "une étape de réflexion ou une décision"),
      ("Agir", "émettre un appel d'outil ou une réponse"),
      ("Observer", "intégrer le résultat au contexte"),
  ]))

f(4, "4.3", "f-04-03-raisonnement",
  "Du raisonnement linéaire à la recherche structurée : trois régimes, et ce que chacun corrige.",
  "Trois regimes de raisonnement : chaine lineaire, coherence interne par echantillonnage, "
  "recherche structuree avec verificateur.",
  "§ 4.3.1 et § 4.3.2, chapitre 4.", r"^## § 4\.4 ", "bandes",
  "Aucun de ces régimes ne rend le raisonnement VÉRIFIABLE : ils réduisent la variance d'une "
  "trace, ils n'en établissent pas la validité. Le vérificateur à l'inférence déplace la "
  "question, il ne la ferme pas.",
  dict(titre="TROIS RÉGIMES, ET CE QUE CHACUN CORRIGE", fleches=True, cols=3, items=[
      ("1", "Chaîne", "Une trace linéaire d'étapes explicitées. Une erreur précoce se propage jusqu'à la conclusion.", "§ 4.3.1"),
      ("2", "Cohérence interne", "Plusieurs traces échantillonnées, et la réponse majoritaire retenue.", "§ 4.3.1"),
      ("3", "Recherche structurée", "L'exploration devient un arbre, guidée par un vérificateur à l'inférence.", "§ 4.3.2"),
  ]))

f(5, "5.0", "f-05-00-trois-objets",
  "Mémoire, récupération et protocole d'accès : trois objets que la pratique confond.",
  "Les trois objets que la pratique confond : memoire, recuperation, protocole d'acces.",
  "Tableau 5.1, § 5.0, chapitre 5.", r"^## § 5\.1 ", "bandes",
  "Les trois n'ont NI LE MÊME CYCLE DE VIE NI LA MÊME GOUVERNANCE. Les confondre revient à "
  "gouverner l'un par les règles de l'autre — une mémoire interne traitée comme un corpus tiers, "
  "ou l'inverse.",
  dict(titre="TROIS OBJETS, TROIS PROVENANCES", cols=3, items=[
      ("1", "Mémoire", "Ce que l'agent produit et conserve de sa propre activité.", "interne, écrite par l'agent"),
      ("2", "Récupération", "Ce qu'il va chercher dans un corpus tiers.", "externe, écrite par d'autres"),
      ("3", "Protocole d'accès", "La tuyauterie qui relie l'un et l'autre aux sources.", "ni l'un ni l'autre — un transport"),
  ]))

f(5, "5.3", "f-05-03-rag-agentique",
  "Du RAG statique au RAG agentique : d'une passe unique à une boucle de contrôle.",
  "Comparaison du RAG naif en trois etapes et du RAG agentique en boucle.",
  "§ 5.3.1, chapitre 5.", r"^## § 5\.4 ", "paire",
  "Sept points de défaillance récurrents sont recensés sur la chaîne de récupération "
  "(Barnett et coll., 2024). La boucle les rend DÉTECTABLES ; elle ne les supprime pas, "
  "et une passe unique ne pouvait ni les détecter ni les corriger.",
  dict(titre_g="RAG NAÏF", titre_d="RAG AGENTIQUE",
       gauche=("Une passe, une fois pour toutes",
               ["Encoder la requête",
                "Récupérer les passages les plus proches",
                "Conditionner la génération"],
               "la linéarité fait la fragilité"),
       droite=("Une boucle de contrôle",
               ["Planifier la stratégie de recherche",
                "Déclencher une ou plusieurs récupérations",
                "Critiquer ce qui remonte",
                "Itérer, ou s'arrêter"],
               "le pipeline figé devient une boucle")))

f(6, "6.1", "f-06-01-topologies",
  "Les quatre topologies de coordination multi-agents et la propriété dominante de chacune.",
  "Quatre topologies de coordination multi-agents : etoile, chaine, arbre, graphe.",
  "Tableau 6.1, § 6.1.2, chapitre 6.", r"^## § 6\.2 ", "bandes",
  "Chaque topologie échange une propriété contre une autre : la visibilité contre la dépendance, "
  "la simplicité contre le recours, l'échelle contre le diagnostic, l'expressivité contre "
  "l'observabilité de l'état global.",
  dict(titre="QUATRE TOPOLOGIES, QUATRE ARBITRAGES", cols=4, items=[
      ("1", "Étoile", "Un orchestrateur délègue à des travailleurs.", "visibilité maximale, orchestrateur point de dépendance"),
      ("2", "Chaîne", "La sortie d'un agent est l'entrée du suivant.", "simple, mais l'erreur se propage sans recours"),
      ("3", "Arbre", "Délégation hiérarchique.", "passage à l'échelle, diagnostic plus difficile"),
      ("4", "Graphe", "Interactions arbitraires.", "expressivité maximale, état global inobservable"),
  ]))

f(6, "6.4", "f-06-04-potentiel-consistance",
  "Potentiel contre consistance : deux métriques dont la confusion masque l'effondrement.",
  "Comparaison des metriques pass@k et pass^k, potentiel contre consistance.",
  "Tableau 6.2, § 6.4.2, chapitre 6.", r"^## § 6\.5 ", "paire",
  "Une probabilité d'échec par pas même faible SE COMPOSE GÉOMÉTRIQUEMENT sur une longue "
  "trajectoire : c'est l'un des constats les plus robustes du domaine, et la raison pour "
  "laquelle un agent se caractérise par sa courbe de consistance, non par son meilleur potentiel.",
  dict(titre_g="pass@k — LE POTENTIEL", titre_d="pass^k — LA CONSISTANCE",
       gauche=("Au moins une parmi k tentatives réussit",
               ["Ce qu'elle mesure : le potentiel",
                "Ce qu'elle flatte : les systèmes capables de trouver occasionnellement la bonne réponse"],
               "monte avec k"),
       droite=("Les k tentatives réussissent toutes",
               ["Ce qu'elle mesure : la consistance",
                "Ce qu'elle révèle : la chute brutale dès que la fiabilité par étape s'éloigne de la perfection"],
               "s'effondre avec k")))

f(7, "7.2", "f-07-02-quatre-axes",
  "Les quatre axes de l'interopérabilité agentique et le lieu de traitement de chacun.",
  "Les quatre axes de l'interoperabilite agentique : agent-outil, agent-agent, agent-humain, agent-donnees.",
  "Tableau 7.2, § 7.2.2, chapitre 7.", r"^## § 7\.3 ", "bandes",
  "Deux axes seulement sont protocolaires — le vertical et l'horizontal. Les deux autres sont "
  "traités ailleurs dans la somme, et le fait qu'un axe ait un lieu ne veut pas dire qu'il "
  "ait un protocole.",
  dict(titre="QUATRE AXES, ET OÙ CHACUN EST TRAITÉ", cols=2, items=[
      ("1", "Agent-outil", "Un agent invoque des outils et ressources pour étendre ses capacités.", "vertical — ch. 8 § 8.1-8.3"),
      ("2", "Agent-agent", "Des agents autonomes se délèguent des tâches par-delà les frontières.", "horizontal — ch. 8 § 8.4-8.6"),
      ("3", "Agent-humain", "Points de validation, consentement, modalités de l'interaction.", "Livre II"),
      ("4", "Agent-données", "Accès gouverné aux données, récupération inter-organisationnelle.", "ch. 2, ch. 9 § 9.4"),
  ]))

f(7, "7.5", "f-07-05-collision-acp",
  "Les quatre branches de la collision « ACP » / « (agentic) control plane », et le statut de chacune.",
  "Les quatre objets distincts que le sigle ACP designe dans le corpus, et le statut de chacun.",
  "Tableau 7.3, § 7.5, chapitre 7.", r"^## § 7\.6 ", "bandes",
  "Quatre objets, un seul sigle, et aucun n'est l'autre. La quatrième branche n'a NI INTITULÉ "
  "COMPLET NI IDENTITÉ ÉTABLIS — c'est une lacune du socle, non une abréviation.",
  dict(titre="UN SIGLE, QUATRE OBJETS", cols=2, items=[
      ("a", "ACP protocolaire", "Agent Communication Protocol d'IBM Research et BeeAI.", "fusionné en août 2025 — jamais un standard vivant"),
      ("b", "Agentic Control Plane", "Programme d'un consortium d'institutions financières et de télécommunications.", "annoncé en juillet 2026 — Livre III"),
      ("c", "« agentic control plane »", "Expression employée par IBM pour positionner un produit d'orchestration.", "positionnement commercial, à attribuer"),
      ("d", "Composante ACP", "De la couche d'infrastructure agentique.", "ni intitulé ni identité établis — lacune"),
  ]))

f(8, "8.2", "f-08-02-cinq-jalons",
  "Cinq jalons du protocole agent-outil en moins de deux ans, et ce que chacun ajoute au contrat.",
  "Frise des cinq revisions du protocole agent-outil, de novembre 2024 a juillet 2026.",
  "Tableau 8.3, § 8.2.1, chapitre 8.", r"^## § 8\.3 ", "frise",
  "Le cinquième jalon n'était PAS ACQUIS au gel de la somme : il était annoncé pour le "
  "lendemain, et la revalidation du 30 juillet 2026 l'a constaté ratifié à sa source. "
  "Une densité de révisions millésimées est elle-même une forme de fragmentation (§ 8.2.1).",
  dict(titre="CINQ RÉVISIONS, VINGT MOIS", jalons=[
      ("2024-11", "Version initiale", "primitives de base ; transports local et HTTP à deux points d'accès", "plein"),
      ("2025-03", "Autorisation", "transport diffusable à point unique ; cadre d'autorisation", "plein"),
      ("2025-06", "Sorties structurées", "sollicitation ; racines ; serveur qualifié serveur de ressources", "plein"),
      ("2025-11", "Découverte d'identité", "schémas 2020-12 ; tâches asynchrones expérimentales", "plein"),
      ("2026-07", "Cœur sans état", "suppression des sessions et de la poignée de main ; cadre d'extensions ; dépréciation à douze mois", "creux"),
  ]))

f(8, "8.4", "f-08-04-agent-card-tache",
  "L'auto-description et l'unité de travail de l'axe horizontal : la carte, la tâche, le message.",
  "L'Agent Card signee, le cycle de vie d'une tache et la hierarchie message-partie-artefact.",
  "§ 8.4.2, chapitre 8.", r"^## § 8\.5 ", "pile",
  "La signature lie l'authenticité de la carte à son DOMAINE D'ORIGINE — elle ne dit rien du "
  "comportement de l'agent qu'elle décrit. L'écart entre ce qu'une carte déclare et ce qu'un "
  "agent fait est l'objet du ch. 9 § 9.4.2, et aucun mécanisme de la v1.0 ne le ferme.",
  dict(titre="TROIS STRUCTURES DE LA VERSION 1.0", couches=[
      ("1", "Agent Card", "Document publié à un emplacement bien connu : identité, capacités, modalités d'interaction. Signée depuis la v1.0."),
      ("2", "Tâche", "L'unité de travail : un objet à état — soumise, en cours, requérant une entrée, achevée, échouée, annulée, rejetée."),
      ("3", "Message · partie · artefact", "La hiérarchie autour de laquelle les échanges s'articulent."),
  ]))

f(8, "8.6", "f-08-06-dans-entre",
  "« Dans les agents, entre les agents » : la répartition déclarée des deux axes.",
  "La repartition declaree entre l'axe agent-outil et l'axe agent-agent.",
  "§ 8.6.3, chapitre 8.", r"^## § 8\.7 ", "paire",
  "⚠ CETTE DOCTRINE EST CELLE DU PROJET AGENT-AGENT. Elle est déclarée par une partie, "
  "et le socle la trace comme telle : une complémentarité affirmée par l'un des deux n'est "
  "pas un constat des deux.",
  dict(titre_g="DANS LES AGENTS", titre_d="ENTRE LES AGENTS",
       gauche=("Axe vertical — agent-outil",
               ["L'intégration des outils et du contexte",
                "Au niveau de l'agent individuel",
                "ch. 8 § 8.1 à § 8.3"],
               "un agent étend ses capacités"),
       droite=("Axe horizontal — agent-agent",
               ["La communication et la coordination",
                "Entre agents autonomes, par-delà les frontières",
                "ch. 8 § 8.4 à § 8.6"],
               "des agents se délèguent des tâches")))

f(9, "9.1", "f-09-01-trois-moments",
  "Les trois moments de la découverte agentique, que le monde des services web réduisait à un seul.",
  "Les trois moments de la decouverte agentique : decouverte, selection, resolution.",
  "Tableau 9.1, § 9.1.2, chapitre 9.", r"^## § 9\.2 ", "chaine",
  "Les réduire à un seul est la leçon d'UDDI, et elle se répète : un registre qui répond « qui "
  "existe ? » ne répond ni « qui convient ? » ni « comment l'atteindre ? ».",
  dict(titre="TROIS QUESTIONS, TROIS MÉCANISMES", maillons=[
      ("Découverte", "qui existe ? — énumérer les agents et outils accessibles dans un périmètre"),
      ("Sélection", "qui convient à cette tâche ? — choisir celui dont les capacités répondent à l'intention"),
      ("Résolution", "où et comment l'atteindre ? — adresse, transport, paramètres de connexion"),
  ]))

f(9, "9.2", "f-09-02-quatre-strates",
  "La pile protocolaire agentique : quatre strates, dont une seule ne s'empile pas.",
  "Les quatre strates de la pile protocolaire agentique, dont l'identite qui est transversale.",
  "Tableau 9.2, § 9.2.2 et § 9.2.3, chapitre 9.", r"^## § 9\.3 ", "pile",
  "L'analogie en couches a une limite, et elle est portée par la quatrième strate : "
  "l'identité et la confiance NE S'EMPILENT PAS, elles traversent tout. Une pile qui la "
  "dessinerait comme un étage dirait le contraire du chapitre.",
  dict(titre="TROIS STRATES EMPILÉES", couches=[
      ("1", "Transport et session", "Trajectoire vers le découplage, liaisons multiples — ch. 8 § 8.1.3."),
      ("2", "Découverte et capacités", "Trouver, sélectionner, résoudre — § 9.1."),
      ("3", "Sémantique et orchestration", "L'écart entre accord de protocole et compréhension — § 9.4."),
  ], notes=[("Identité et confiance", "⚠ Transversale : elle ne s'empile pas, elle traverse "
             "les trois autres. Traitée au ch. 3 et dans tout le Livre II.")]))

f(9, "9.5", "f-09-05-pyramide-evaluation",
  "La pyramide d'évaluation de l'interopérabilité agentique : trois étages, aucun ne subsumant le suivant.",
  "Les trois etages de l'evaluation de l'interoperabilite agentique.",
  "Tableau 9.4, § 9.5.1, chapitre 9.", NOTE, "pile",
  "Aucun étage ne subsume le suivant : une conformité protocolaire parfaite n'établit ni "
  "l'interopérabilité entre implémentations, ni le résultat d'une collaboration. Le troisième "
  "étage est INTRINSÈQUEMENT NON DÉTERMINISTE, et c'est pourquoi il ne se certifie pas comme les deux autres.",
  dict(titre="TROIS ÉTAGES, TROIS NATURES", couches=[
      ("1", "Conformité protocolaire", "Un message est-il valide ? Une transition d'état légale ? — déterministe et automatisable."),
      ("2", "Interopérabilité entre implémentations", "Deux implémentations distinctes du même protocole se comprennent-elles ? — déterministe, plus coûteux."),
      ("3", "Bancs de tâches inter-agents", "La collaboration produit-elle le résultat attendu ? — non déterministe."),
  ]))

f(10, "10.3", "f-10-03-trois-roles",
  "Les trois rôles que le commerce agentique dissocie, et ce que la dissociation fait disparaître.",
  "Les trois roles du commerce agentique : mandant humain, agent executant, commercant.",
  "Tableau 10.1, § 10.3.1, chapitre 10.", r"^## § 10\.4 ", "bandes",
  "Ce que la dissociation fait disparaître est le SIGNAL, pas le droit : le commerçant perd "
  "la capacité d'observer un parcours humain, sans perdre l'obligation de savoir à qui il vend.",
  dict(titre="TROIS RÔLES, ET CE QUE CHACUN PERD", cols=3, items=[
      ("1", "Mandant humain", "Détient l'intention et l'autorité de payer.", "n'a plus la présence à l'écran au moment de l'achat"),
      ("2", "Agent exécutant", "Détient la délégation et l'opération de la transaction.", "n'a aucun signal perceptuel prouvant qu'un humain agit"),
      ("3", "Commerçant", "Détient la livraison du bien ou du service.", "n'a plus la capacité d'observer un parcours humain"),
  ]))

f(10, "10.4", "f-10-04-mandat-preuve",
  "Le mandat comme couche de preuve opposable : la chaîne qui rattache une transaction à un consentement.",
  "La chaine intention, panier, paiement, signee et horodatee, comme couche de preuve opposable.",
  "§ 10.4.2 et § 10.1.4, chapitre 10.", r"^## § 10\.5 ", "chaine",
  "⚠ Un mandat signé est un cadre d'autorisation opposable ; il n'est JAMAIS un dispositif "
  "« sécurisé ». Il prouve qu'un consentement a été émis — pas qu'il était éclairé, ni que "
  "l'agent qui l'a sollicité était intègre (réserve F-01 du Vol. II).",
  dict(titre="SIGNÉE ET HORODATÉE À CHAQUE MAILLON", maillons=[
      ("Intention", "ce que le mandant a voulu, avant la recherche"),
      ("Panier", "ce que l'agent a composé, et sur quoi le mandant s'est accordé"),
      ("Paiement", "l'opération, rattachée aux deux précédents"),
      ("Litige", "l'élément probant, s'il faut remonter la chaîne"),
  ]))

f(11, "11.1a", "f-11-01a-amplification",
  "Ce que la couche d'interopérabilité amplifie : trois mécanismes qui font basculer des propriétés locales.",
  "Les trois mecanismes par lesquels la couche agentique fait basculer des proprietes locales.",
  "§ 11.1.1 et § 11.1.2, chapitre 11.", r"^### 11\.1\.3 ", "bandes",
  "⚠ LA TRIADE LÉTALE N'EST PAS POSÉE ICI : son siège est le ch. 19 § 19.2, qui en porte le "
  "modèle de menace, les conditions et les incidents. Ce chapitre n'en traite que "
  "l'amplification, propre à la couche d'interopérabilité — et l'amplification n'est pas la menace.",
  dict(titre="CE QUE LA COMPOSITION AJOUTE À LA MENACE", cols=3, items=[
      ("1", "La surface n'est pas composable", "Deux systèmes sûrs séparément ne font pas un assemblage sûr.", "§ 11.1.1"),
      ("2", "La frontière est franchie", "Ce qui traverse un protocole échappe au périmètre qui le validait.", "§ 11.1.3"),
      ("3", "L'effet se cumule", "Une défaillance locale se propage en cascade dans le graphe.", "§ 11.2.2"),
  ]))

f(11, "11.1b", "f-11-01b-trois-surfaces",
  "Les trois surfaces d'attaque, distinguées par ce que chacune corrompt.",
  "Les trois surfaces d'attaque de la couche agentique : l'outil, l'invite, la memoire.",
  "Tableau 11.3, § 11.1.4, chapitre 11.", r"^## § 11\.2 ", "bandes",
  "⚠ La typologie est une CONSTRUCTION D'ÉDITEUR, non un énoncé de source primaire, et elle "
  "ne doit pas masquer l'asymétrie : les trois surfaces ne sont ni également documentées "
  "ni également défendues (§ 11.1.4).",
  dict(titre="TROIS SURFACES, TROIS CANAUX", cols=3, items=[
      ("1", "L'outil", "Corrompt la capacité de l'agent.", "canal : la description lue à l'inférence"),
      ("2", "L'invite", "Corrompt son instruction.", "canal : le contexte"),
      ("3", "La mémoire", "Corrompt son état.", "canal : la persistance entre exécutions"),
  ]))

f(11, "11.4", "f-11-04-confinement",
  "Confiner plutôt que prévenir : ce que le renversement change, et ce qu'il ne promet pas.",
  "Le renversement du raisonnement de securite : borner le rayon de la compromission plutot "
  "que l'empecher.",
  "§ 11.4.1, chapitre 11.", NOTE, "paire",
  "Le renversement ne suppose PAS que les surfaces du § 11.1 soient refermées — il suppose "
  "l'inverse, et c'est ce qui le rend praticable. Une frontière qui borne un rayon ne dit "
  "rien de la probabilité de la compromission qu'elle borne.",
  dict(titre_g="PRÉVENIR", titre_d="CONFINER",
       gauche=("Empêcher la compromission",
               ["Suppose que les surfaces se referment",
                "Une seule brèche annule la démarche",
                "Non protocolaire : les spécifications ne répondent ni du contenu ni de l'état"],
               "l'ordre habituel du raisonnement"),
       droite=("Borner le rayon de la compromission",
               ["Restreindre le contexte de chaque agent",
                "Restreindre ses capacités",
                "Le cadre local devient frontière de sécurité et de confidentialité"],
               "ce que le manifeste propose (§ 11.1.3)")))
