#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures du barème A — le reliquat.

Sept figures dont la matière ne se lisait pas dans un tableau et qu'une passe de
lecture a fallu instruire séparément. Elles appartiennent aux Livres I, III ;
ce module est un ordre de rédaction, non un rang du volume.
"""
from spec import f, NOTE  # noqa: F401

f(7, "7.3", "f-07-03-chronologie",
  "Dix-sept mois : les lancements, puis les passages sous fondation — et l'ordre s'inverse.",
  "La chronologie des quatre protocoles agentiques, de novembre 2024 a avril 2026, "
  "en lancements puis en passages sous fondation.",
  "§ 7.3, chapitre 7.", r"^## § 7\.4 ", "paire",
  "⚠ LES DEUX SÉQUENCES SONT INVERSES L'UNE DE L'AUTRE, et c'est le fait le plus instructif de "
  "la section : la flèche « agent-outil → agent-agent → infrastructure » que le plan a longtemps "
  "portée est fausse dans les deux lectures. Le cinquième protocole, celui de transaction, n'est "
  "pas de ce décompte.",
  dict(titre_g="LANCEMENTS", titre_d="PASSAGES SOUS FONDATION",
       gauche=("De novembre 2024 à septembre 2025",
               ["nov. 2024 — protocole agent-outil : un éditeur, une spécification, un intendant",
                "mars 2025 — couche d'infrastructure : annuaires et transport dédié",
                "17 mars 2025 — ACP protocolaire, en pré-alpha",
                "avril 2025 — protocole agent-agent : délégation de pair à pair",
                "sept. 2025 — protocole de transaction (ch. 10)"],
               "l'infrastructure précède l'agent-agent"),
       droite=("De juin 2025 à décembre 2025",
               ["juin 2025 — le protocole agent-agent passe à une fondation neutre",
                "29 juill. 2025 — la couche d'infrastructure suit",
                "29 août 2025 — l'ACP protocolaire fusionne dans l'agent-agent",
                "déc. 2025 — la gouvernance du protocole agent-outil est transférée"],
               "quatre protocoles, deux fondations, dont l'une héberge l'autre")))

f(24, "24.3", "f-24-03-cycle-identite",
  "Le cycle de vie de l'identité d'agent à l'échelle du parc, de l'enregistrement à la révocation.",
  "Le cycle de vie gouverne d'une identite d'agent, de l'enregistrement a la revocation.",
  "§ 24.3.1, chapitre 24.", r"^### 24\.3\.2 ", "chaine",
  "⚠ Le risque dominant n'est pas l'attribution mais L'ACCUMULATION : sans propriétaire humain "
  "responsable, parrainage explicite et certification périodique, l'organisation accumule des "
  "identités dont plus personne ne répond — et la révocation, dernier maillon, n'a pas de "
  "mécanisme en cascade documenté (ch. 20 § 20.6).",
  dict(titre="AUCUNE IDENTITÉ SANS CYCLE DE VIE GOUVERNÉ DE BOUT EN BOUT", boucle=True,
       maillons=[
           ("Enregistrement", "un propriétaire humain responsable identifié, un parrainage explicite"),
           ("Attestation", "de sa raison d'être"),
           ("Certification", "périodique, de ses accès"),
           ("Révocation", "et ce qui en a été dérivé"),
       ]))

f(30, "30.2b", "f-30-02b-axe-canada-quebec",
  "L'axe Canada / Québec : pourquoi la qualification temporelle y décide du sens d'une obligation.",
  "L'exigence de qualification temporelle sur l'axe canadien et quebecois du maillage reglementaire.",
  "§ 30.2.7, chapitre 30 — reçu du Vol. I, en [C].", r"^## § 30\.3 ", "bandes",
  "⚠ CETTE SOUS-SECTION EST REÇUE DU VOL. I, EN [C], et elle recoupe la matière que les ch. 25 à "
  "28 portent à leurs propres régimes. EN CAS D'ÉCART, CE SONT EUX QUI FONT FOI : ils résolvent "
  "contre le Vol. II et le Vol. III, à des niveaux supérieurs.",
  dict(titre="TROIS ÉTATS, ET UNE ERREUR DE DATE INVERSE LE SENS", cols=3, items=[
      ("1", "En vigueur", "L'obligation est opposable aujourd'hui.", "art. 12.1 — depuis le 22 sept. 2023"),
      ("2", "Publié, non encore opposable", "Le texte est arrêté ; la date d'application ne l'est pas atteinte.", "E-23 — opposable le 1ᵉʳ mai 2027"),
      ("3", "Sans date opposable", "Le texte ne crée ni ne modifie aucune exigence.", "avis 11-348 — les lois existantes s'appliquent"),
  ]))

f(34, "34.1", "f-34-01-regimes-usage",
  "Le tri par régime d'usage : productivité assistée ou autonomie transactionnelle.",
  "La distinction entre productivite assistee et autonomie transactionnelle dans le bancaire.",
  "§ 34.1.1, chapitre 34 — le critère est posé au ch. 31 § 31.1.3.", r"^### 34\.1\.2 ", "paire",
  "⚠ LA QUASI-TOTALITÉ DES DÉPLOIEMENTS OBSERVÉS EN 2024-2026 RELÈVENT DU PREMIER RÉGIME. "
  "Présenter un copilote comme une autonomie transactionnelle est la confusion que le discours "
  "commercial entretient, et que ce tri existe pour défaire.",
  dict(titre_g="PRODUCTIVITÉ ASSISTÉE", titre_d="AUTONOMIE TRANSACTIONNELLE",
       gauche=("Un copilote rédige, résume, prépare",
               ["Aucune transaction irréversible n'est exécutée sans intervention humaine",
                "Le seuil du ch. 31 § 31.1.1 n'est pas franchi",
                "La quasi-totalité des déploiements observés"],
               "le régime dominant, 2024-2026"),
       droite=("L'agent initie une action à effet financier irrévocable",
               ["Le seuil de finalité est franchi par l'agent",
                "Le régime réglementaire change avec lui",
                "Rare, et rarement ce que le discours désigne"],
               "le régime que le vertical durcit")))

f(34, "34.2", "f-34-02-chaine-sinistre",
  "La chaîne du sinistre : un coordinateur de spécialistes, non un décideur unique.",
  "La chaine du sinistre — declaration, instruction, reglement, subrogation — et les sous-taches "
  "que l'agent orchestre.",
  "§ 34.2.3, chapitre 34.", r"^### 34\.2\.4 ", "chaine",
  "⚠ CHAQUE SOUS-TÂCHE COMPORTE UN RISQUE DE CASCADE : une erreur propagée le long de la chaîne "
  "aboutit à un RÈGLEMENT IRRÉVERSIBLE. Le patron directeur est celui du coordinateur de "
  "spécialistes — l'agent orchestre, il ne décide pas seul.",
  dict(titre="QUATRE TEMPS, ET QUATRE SOUS-TÂCHES ORCHESTRÉES", maillons=[
      ("Déclaration", "le premier avis, et les pièces qui l'accompagnent"),
      ("Instruction", "extraction de pièces, évaluation des dommages, détection de fraude"),
      ("Règlement", "calcul d'indemnité — et il est irréversible"),
      ("Subrogation", "le recours, après coup"),
  ]))

f(34, "34.3", "f-34-03-souscription-vie",
  "La souscription vie accélérée : la chaîne d'orchestration où la contrainte réglementaire est la plus directe.",
  "La chaine de souscription vie acceleree, et les deux regimes qu'elle declenche.",
  "§ 34.3.1, chapitre 34.", r"^### 34\.3\.2 ", "chaine",
  "⚠ DEUX RÉGIMES SE DÉCLENCHENT ENSEMBLE : c'est une décision de tarification du risque sur une "
  "personne physique — donc explicitement de HAUT RISQUE — et, rendue sans intervention humaine, "
  "une décision EXCLUSIVEMENT AUTOMATISÉE qui déclenche les obligations de l'article 12.1 "
  "(ch. 27 § 27.2).",
  dict(titre="LA CHAÎNE TYPE, ET CE QUI MORD À CHAQUE MAILLON", maillons=[
      ("Preuves", "récupération de pièces hétérogènes — dont la donnée de santé"),
      ("Règles", "application des règles de mortalité"),
      ("Tarification", "du risque, sur une personne physique — haut risque"),
      ("Décision", "sans intervention humaine : art. 12.1"),
  ]))

f(35, "35.9", "f-35-09-gouvernances-comparees",
  "Cinq dispositifs de gouvernance sur dix institutions, et ce qu'ils ont en commun.",
  "Les cinq dispositifs de gouvernance de l'IA identifiables parmi les dix institutions examinees.",
  "§ 35.9, chapitre 35.", NOTE, "bandes",
  "⚠ CINQ SUR DIX. Les cinq autres ne publient pas de dispositif identifiable — ce qui est une "
  "absence de publication, non une absence de gouvernance (§ 35.0, troisième classe d'accès). "
  "La comparaison porte sur ce qui est publié, et rien d'autre.",
  dict(titre="CE QUE CINQ DISPOSITIFS PUBLIÉS ONT EN COMMUN", cols=3, items=[
      ("1", "Un titulaire nommé au sommet", "Trois des cinq : un responsable en chef de l'IA ; une responsable mondiale à l'organe de direction exécutive depuis mai 2026 ; un chef de groupe rattaché au chef de la direction depuis février 2026.", "§ 35.2, § 35.4"),
      ("2", "Un dispositif identifiable", "Publié, et donc opposable à sa propre communication.", "cinq des dix institutions examinées"),
      ("3", "Rien sur l'architecture", "Aucun des cinq ne documente l'option d'orchestration de son déploiement.", "ch. 43 § 43.2 — absence de documentation"),
  ]))
