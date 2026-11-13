"""Correctifs de l'audit du 11 novembre 2026, lot « comp-a » (Compendium, Livres I à V et liminaires).

Complète 02_livres1_2.py et 03_livres3_4_5.py : seuls figurent ici les constats que ces modules
laissaient entiers ou à moitié réglés. Chaque passage d'origine porte sur le corps déjà corrigé.
"""

CORRECTIONS = [
    # --- Ch. 6 / ch. 37 : K02-07 (écho du chiffre de CaMeL au ch. 37, aligné sur le § 6.5.2) ---
    ("ne résout par construction qu'environ <strong>deux tiers</strong> des scénarios de son banc d'évaluation — proportion indicative",
     "ne résout par construction qu'une fraction bornée des scénarios de son banc d'évaluation (67 % des tâches avec sécurité prouvée dans la première version de l'article, 77 % dans sa version révisée) — proportion indicative",
     'K02-07'),

    # --- Ch. 6 § 6.5.3 : K02-08 (attribution du principe à l'article dont il est le titre) ---
    ("(principe classique de l'évaluation adaptative en apprentissage contradictoire ; Carlini et Wagner, 2017 ; Tramer et coll., 2020)",
     "(principe classique de l'évaluation adaptative en apprentissage contradictoire ; Carlini et Wagner, 2017 ; Tramer et coll., 2020 ; la formule est reprise en titre par Nasr, Carlini et coll., « The Attacker Moves Second », octobre 2025)",
     'K02-08'),

    # --- Ch. 7 § 7.3 : K02-22 (quatre protocoles, trois durées) ---
    ("Aucun des protocoles étudiés n'est demeuré propriétaire au-delà de treize mois.",
     "Aucun des trois protocoles nés propriétaires n'est demeuré propriétaire au-delà de treize mois (l'ACP protocolaire, né sous l'égide de la Linux Foundation, n'entre pas dans ce décompte).",
     'K02-22'),

    # --- Ch. 2 (renvoi final) : K02-33 (thèse du ch. 2 reprise dans sa forme bornée) ---
    ("La thèse du présent chapitre en est la prémisse : les protocoles agentiques <strong>présupposent</strong> l'accord sémantique et ne le fournissent pas. C'est au",
     "La thèse du présent chapitre en est la prémisse : les protocoles agentiques <strong>présupposent</strong> l'accord sémantique que peu savent établir. C'est au",
     'K02-33'),

    # --- Ch. 8 § 8.2.1 : K02-36 (liste des sous-sections revalidées : six, comme aux § 8.1.4, ch. 11 et ch. 50) ---
    ("le <strong>30 juillet 2026</strong>, et les § 8.1.2, § 8.1.3, § 8.2.1, § 8.2.2 et § 8.2.3 sont revalidés <strong>en bloc</strong>",
     "le <strong>30 juillet 2026</strong>, et les § 8.1.2, § 8.1.3, § 8.2.1, § 8.2.2, § 8.2.3 et § 8.3.1 sont revalidés <strong>en bloc</strong>",
     'K02-36'),

    # --- Ch. 11 § 11.3.2 -> § 11.3.1 : K02-36 (le bloc « Ce que cette revalidation n'établit pas » suit les trois effets qu'il commente) ---
    ("<p>Ce que cette revalidation n'établit pas, et le dire est le geste dû. Elle ne mesure aucune de ces trois conséquences : aucune n'est adossée à un travail publié, aucun identifiant de vulnérabilité ne les documente, et le socle n'en recense pas. Ce sont des <strong>lectures de l'auteur</strong> sur un texte lu, et non des faits — <em>savoir ce qu'une spécification dit n'est pas savoir ce qu'elle expose.</em> Le passage de « nous n'avons pas lu le texte » à « nous l'avons lu et nous en tirons trois hypothèses marquées » est le seul progrès que cette lecture pouvait produire.</p>\n",
     "",
     'K02-36'),
    ("est une source de duplication, non une garantie.</p>\n<p>Un dernier rappel, qui n'est pas de pure forme.",
     "est une source de duplication, non une garantie.</p>\n<p>Ce que cette revalidation n'établit pas, et le dire est le geste dû. Elle ne mesure aucun de ces trois effets : aucun n'est adossé à un travail publié, aucun identifiant de vulnérabilité ne les documente, et le socle n'en recense pas. Ce sont des <strong>lectures de l'auteur</strong> sur un texte lu, et non des faits — <em>savoir ce qu'une spécification dit n'est pas savoir ce qu'elle expose.</em> Le passage de « nous n'avons pas lu le texte » à « nous l'avons lu et nous en tirons trois hypothèses marquées » est le seul progrès que cette lecture pouvait produire.</p>\n<p>Un dernier rappel, qui n'est pas de pure forme.",
     'K02-36'),

    # --- K02-43 (acteurs nommés là où l'annexe I les porte) : ch. 10 § 10.2.1 ---
    ("a été ouverte en mars 2025 par un équipementier de réseau, avec un éditeur de cadriciel",
     "a été ouverte en mars 2025 par l'équipementier de réseau Cisco, avec un éditeur de cadriciel",
     'K02-43'),
    ("sont cinq : l'équipementier initiateur, un constructeur de matériel",
     "sont cinq : l'équipementier initiateur (Cisco), un constructeur de matériel",
     'K02-43'),
    # ch. 10 § 10.3.2, tableau 10.2
    ("<td>un réseau de cartes, avec un fournisseur d'infrastructure de périphérie</td>",
     "<td>Visa, avec Cloudflare (fournisseur d'infrastructure de périphérie)</td>",
     'K02-43'),
    ("<td>un second réseau de cartes</td>",
     "<td>Mastercard (<em>Agent Pay</em>)</td>",
     'K02-43'),
    ("<td>coprésidé par les deux réseaux de cartes</td>",
     "<td>coprésidé par Mastercard et Visa</td>",
     'K02-43'),
    ("<td>un fournisseur d'infrastructure de périphérie, en cours de spécification",
     "<td>Cloudflare (fournisseur d'infrastructure de périphérie), en cours de spécification",
     'K02-43'),
    ("Que le groupe de travail paiements soit coprésidé par les deux réseaux de cartes et bâtisse",
     "Que le groupe de travail paiements soit coprésidé par Mastercard et Visa, les deux réseaux de cartes, et bâtisse",
     'K02-43'),
    # ch. 10 § 10.3 : ACP commercial et MPP
    ("publié en septembre 2025 par un éditeur de modèles et un fournisseur de paiement",
     "publié en septembre 2025 par OpenAI (éditeur de modèles) et Stripe (fournisseur de paiement)",
     'K02-43'),
    ("lancé le <strong>18 mars 2026</strong> par un fournisseur de paiement et une infrastructure de règlement associée",
     "lancé le <strong>18 mars 2026</strong> par Stripe (fournisseur de paiement) et Tempo (infrastructure de règlement associée)",
     'K02-43'),
    # ch. 11 § 11.1.3 : le manifeste APM et l'incident de l'AIID
    ("porté par un manifeste de recherche à dix-huit auteurs :",
     "porté par le manifeste de recherche à dix-huit auteurs sur la gestion agentique des processus d'affaires (<em>Agentic Business Process Management</em>, ch.\xa022 § 22.6) :",
     'K02-43'),
    ("Un agent de codage a exécuté des commandes destructrices durant un gel de code",
     "Un agent de codage (celui de la plateforme Replit) a exécuté des commandes destructrices durant un gel de code",
     'K02-43'),

    # --- Ch. 10 § 10.1.2 : K02-51 (la Linux Foundation n'est pas la faîtière du protocole de paiement) ---
    ("Selon le communiqué de la <strong>Linux Foundation</strong>, fondation faîtière du protocole, daté du <strong>9 avril 2026</strong>, plus de soixante organisations des paiements et des services financiers déclarent leur soutien au protocole.",
     "Selon le communiqué de la <strong>Linux Foundation</strong> daté du <strong>9 avril 2026</strong> — fondation faîtière du protocole agent-agent, non du protocole de paiement, passé à la FIDO Alliance (§ 10.1.3) —, plus de soixante organisations des paiements et des services financiers déclarent leur soutien au protocole de paiement.",
     'K02-51'),

    # --- Ch. 11 § 11.3.2 : K02-74 (renvoi au ch. 20, siège de la vérification continue) ---
    ("seule réponse robuste à la révocation après approbation — demeure immature.",
     "seule réponse robuste à la révocation après approbation — demeure immature (le ch.\xa020 § 20.2-20.3 en porte l'état).",
     'K02-74'),

    # --- Ch. 14 § 14.3 et § 14.5 : K03-26 (« réponse » aux cinq questions : un verdict, sur le papier) ---
    ("Le passeport reçoit une réponse aux cinq questions parce qu'il a été construit pour en recevoir une : c'est la propriété d'un objet de synthèse, pas un résultat.",
     "Le passeport reçoit, sur le papier, une réponse (pleine ou partielle) à chacune des cinq questions parce qu'il a été construit pour en recevoir une : c'est la propriété d'un objet de synthèse, pas un résultat.",
     'K03-26', '*'),
    ("est le seul endroit de la somme où les cinq reçoivent une réponse, et cette réponse y est explicitement <strong>sur le papier</strong>",
     "est le seul endroit de la somme où les cinq questions reçoivent chacune un verdict, et ce verdict y est explicitement <strong>sur le papier</strong> (une réponse pleine, quatre partielles)",
     'K03-26'),
    ("un seul lieu où les cinq reçoivent réponse.",
     "un seul lieu où les cinq questions reçoivent chacune un verdict, sur le papier.",
     'K03-26'),

    # --- Ch. 10 introduction : L02-12 (la thèse n'est imprimée qu'une fois ; le paragraphe qui la répétait ne garde que sa glose) ---
    ("<p>Que la transaction agentique constitue l'<strong>aboutissement financier</strong> de la pile protocolaire est une <strong>lecture de l'auteur</strong> : les sources établissent que le protocole de paiement est un <strong>protocole compagnon</strong> de l'axe agent-agent, dédié aux transactions pilotées par agents, et rien de plus sur sa centralité. Qu'AGNTCY soit une couche d'infrastructure et non un concurrent est, pour sa part, le positionnement officiel déclaré du projet — une déclaration, non un fait vérifié, et que des analyses tierces viennent nuancer. <em>Une lecture de l'auteur et une déclaration de partie intéressée ne sont pas du même ordre, et aucune des deux n'est un fait établi.</em></p>",
     "<p><em>Une lecture de l'auteur et une déclaration de partie intéressée ne sont pas du même ordre, et aucune des deux n'est un fait établi.</em></p>",
     'L02-12'),

    # --- Ch. 9 § 9.2.5, tableau 9.3 : L02-09 (ligne agent-outil alignée sur la revalidation du ch. 8) ---
    ("<td>production ; révision stable, <strong>candidate à venir</strong></td><td>fondation dédiée</td><td>socle pour exposer outils et ressources ; adopter la <strong>révision datée stable</strong>, traiter le cœur sans état comme <strong>cible</strong></td>",
     "<td>production ; révision <code>2026-07-28</code> <strong>ratifiée</strong> (cœur sans état en vigueur)</td><td>fondation dédiée</td><td>socle pour exposer outils et ressources ; adopter la <strong>révision datée en vigueur</strong> — le cœur sans état n'est plus une cible, il est le contrat (ch.\xa08, revalidation du 30 juillet 2026)</td>",
     'L02-09'),

    # --- Ch. 17 : L03-08 (le seuil des « deux sauts » : renvois alignés sur la définition « dès le deuxième saut ») ---
    ("la délégation à plus de deux sauts n'est pas standardisée de bout en bout",
     "la délégation dès le deuxième saut n'est pas standardisée de bout en bout",
     'L03-08'),
    ("déclare la délégation à plus de deux sauts non standardisée",
     "déclare non standardisée la délégation dès le deuxième saut",
     'L03-08'),
    ("<td>Délégation au-delà de deux sauts</td><td><strong>non instruite</strong> — front ouvert hérité du Vol. I</td>",
     "<td>Délégation au-delà de deux sauts</td><td><strong>non instruite</strong> — front ouvert hérité du Vol. I (formulé « au-delà de deux sauts » par H-28 ; le ch.\xa017 le situe dès le deuxième saut)</td>",
     'L03-08'),

    # --- Ch. 40 § 40.2.1 : COQ-Com-088 (l'étiquette de tri est « PROGRAMMÉ », au masculin ; les deux citations de la source, accordées à leur nom, restent telles) ---
    ("<p>« PROGRAMMÉE » n'est pas un mot du chapitre mais une étiquette de tri",
     "<p>« PROGRAMMÉ » n'est pas un mot du chapitre mais une étiquette de tri",
     'COQ-Com-088'),

    # --- Ch. 43 § 43.3 : COQ-Com-091 (anglicisme « release » : « libération humaine », terme du ch. 31) ---
    ("et la release humaine sur l'action irréversible",
     "et la libération humaine sur l'action irréversible",
     'COQ-Com-091'),

    # --- Annexe B, S-075, S-087 (F-41) et S-101 (F-55) : COQ-Com-096 (trait d'union, non signe moins, devant le numéro de révision) ---
    ("Rév. −09 du 6 juill. 2026, exp. 7 janv. 2027 ; −11 du 30 juill. 2026",
     "Rév. -09 du 6 juill. 2026, exp. 7 janv. 2027 ; -11 du 30 juill. 2026",
     'COQ-Com-096'),
    ("§7.9. −00 du 16 oct. 2025, expiré.",
     "§7.9. -00 du 16 oct. 2025, expiré.",
     'COQ-Com-096'),
    ("Balayage sur rév. −01, supplantée",
     "Balayage sur rév. -01, supplantée",
     'COQ-Com-096'),

    # --- FIN DES CORRECTIFS ---
]

JOURNAL = [
    ('ch. 37 § 37.6', "Alignement du chiffre de CaMeL (67 % dans la première version de l'article, 77 % dans la version révisée) sur le § 6.5.2", 'K02-07'),
    ('ch. 6 § 6.5.3', "Attribution de la formule « l'attaquant joue en second » à l'article qui la porte en titre (Nasr, Carlini et coll., octobre 2025)", 'K02-08'),
    ('ch. 7 § 7.4.1', "Précision que les treize mois de propriété exclusive valent pour les trois protocoles nés propriétaires, non pour l'ACP protocolaire", 'K02-22'),
    ('ch. 2 § 2.4.2 (renvoi final)', "Reprise de la thèse du ch. 2 dans sa forme bornée (« que peu savent établir »)", 'K02-33'),
    ('ch. 8 § 8.2.1', "Liste des sous-sections revalidées le 30 juillet 2026 portée à six (ajout du § 8.3.1), comme au § 8.1.4, au ch. 11 et au ch. 50", 'K02-36'),
    ('ch. 11 § 11.3.1-11.3.2', "Déplacement du bloc « Ce que cette revalidation n'établit pas » sous les trois effets sur la surface d'attaque qu'il qualifie (§ 11.3.1)", 'K02-36'),
    ('ch. 10 § 10.2.1', "Nomination de Cisco comme initiateur d'AGNTCY et premier des cinq membres formateurs", 'K02-43'),
    ('ch. 10 § 10.3.3 et tabl. 10.2', "Nomination de Visa (avec Cloudflare), de Mastercard et de Cloudflare dans le tableau 10.2 et dans la lecture qui le suit", 'K02-43'),
    ('ch. 10 § 10.3.2 et § 10.3.4', "Nomination d'OpenAI et de Stripe (ACP commercial), de Stripe et de Tempo (MPP)", 'K02-43'),
    ('ch. 11 § 11.1.3 et § 11.2.2', "Nomination du manifeste de recherche sur la gestion agentique des processus d'affaires (ch. 22 § 22.6) et de la plateforme de l'agent de codage de l'incident 1152", 'K02-43'),
    ('ch. 10 § 10.1.2', "Précision que la Linux Foundation est la faîtière du protocole agent-agent, non du protocole de paiement passé à la FIDO Alliance", 'K02-51'),
    ('ch. 11 § 11.3.2', "Renvoi au ch. 20 § 20.2-20.3, siège de la vérification d'intégrité continue", 'K02-74'),
    ('ch. 14 § 14.1, § 14.3 et synthèse, ch. 16 § 16.5', "Réponse aux cinq questions du passeport rapportée à un verdict sur le papier (une réponse pleine, quatre partielles), en cohérence avec le tableau 16.4", 'K03-26'),
    ('ch. 10 introduction', "Suppression de la seconde rédaction de la thèse (le paragraphe qui répétait l'encadré ne garde que sa glose)", 'L02-12'),
    ('ch. 9 § 9.2.5, tabl. 9.3', "Ligne « Agent-outil » alignée sur la revalidation du 30 juillet 2026 (révision 2026-07-28 ratifiée, cœur sans état en vigueur)", 'L02-09'),
    ('ch. 24 § 24.3.2, ch. 31 § 31.3.4, ch. 49 tabl. 49.2', "Seuil des deux sauts : renvois alignés sur la définition du ch. 17 (dès le deuxième saut), la formulation de H-28 étant signalée", 'L03-08'),
    ('ch. 40 § 40.2.1', "Étiquette de tri « PROGRAMMÉ » au masculin dans la mention de l'étiquette", 'COQ-Com-088'),
    ('ch. 43 § 43.5.1', "« libération humaine » pour l'anglicisme « release humaine »", 'COQ-Com-091'),
    ('annexe B, S-075, S-087, S-101', "Trait d'union (non signe moins) devant les numéros de révision -09, -11, -00 et -01", 'COQ-Com-096'),
]
