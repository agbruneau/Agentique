"""Correctifs de l'audit de novembre 2026, lot « cadre-a » (Cadre de référence v1.1).

Passages d'origine pris dans le corps tel qu'il est après les modules 01 à 04.
Les titres des légendes de tableaux et de figures ne sont pas modifiés : construire_pdf.py
contrôle (verifier_numeros) que « Tableau N — titre » et « Figure N — titre » du PDF composé
reprennent les titres des listes d'origine. Seules les parties de légende qui suivent le titre
sont corrigées ici.
"""

CORRECTIONS = [
    # --- R01-28 : avertissements et section 1.7 muets sur l'actualisation et la revue de novembre
    ('Les versions, dates et chiffres reflètent l’état des sources au 27 octobre 2026; vérifications des 27 et 28 octobre 2026 (section 1.7).',
     'Les versions, dates et chiffres reflètent l’état des sources au 27 octobre 2026; vérifications des 27 et 28 octobre 2026 (section 1.7). L’actualisation du 1<sup>er</sup>\xa0novembre 2026 et la revue contradictoire du 3 novembre 2026 sont postérieures à cette date de référence; leurs errata et leurs correctifs, intégrés au corps, sont consignés à l’annexe H (sections H.4 et H.6).',
     'R01-28'),
    ('L’annexe F détaille la méthode, le bilan et les corrections.</p>\n<h2>2 Contexte et enjeux</h2>',
     'L’annexe F détaille la méthode, le bilan et les corrections.</p>\n<p>Deux reprises ont suivi ces vérifications. L’actualisation du 1<sup>er</sup>\xa0novembre 2026 a rouvert sur leur source primaire les sources datées dont dépend une exigence ou une échéance (annexe H, sections H.1 à H.5; seuls ses errata corrigent le corps). La revue contradictoire du 3 novembre 2026 a fait intégrer au corps des correctifs de cohérence interne, de précision normative et de vérification bibliographique (section H.6).</p>\n<h2>2 Contexte et enjeux</h2>',
     'R01-28'),

    # --- R01-37 (appels [1] et [3]) et V3-04 (chiffre et phrase dans un même paragraphe) : « Pourquoi maintenant »
    ('<p><strong>40\xa0%</strong></p>\n<p>des applications d’entreprise intégreront des agents spécialisés d’ici la fin de 2026, contre moins de 5\xa0% en 2025 (prévision Gartner, août 2025)</p>',
     '<p><strong>40\xa0%</strong> des applications d’entreprise intégreront des agents spécialisés d’ici la fin de 2026, contre moins de 5\xa0% en 2025 (prévision Gartner, août 2025)<strong><sup>[1]</sup></strong></p>',
     'R01-37/V3-04'),
    ('<p><strong>&gt;\xa040\xa0%</strong></p>\n<p>des projets d’IA agentique seront annulés d’ici la fin de 2027\xa0: coûts, valeur incertaine, contrôles inadéquats (prévision Gartner, juin 2025)</p>',
     '<p><strong>&gt;\xa040\xa0%</strong> des projets d’IA agentique seront annulés d’ici la fin de 2027\xa0: coûts, valeur incertaine, contrôles inadéquats (prévision Gartner, juin 2025)<strong><sup>[3]</sup></strong></p>',
     'R01-37/V3-04'),
    ('<p><strong>13\xa0%</strong></p>\n<p>des organisations estiment',
     '<p><strong>13\xa0%</strong> des organisations estiment',
     'V3-04'),
    ('<p><strong>&gt;\xa0150\xa0000</strong></p>\n<p>agents en usage',
     '<p><strong>&gt;\xa0150\xa0000</strong> agents en usage',
     'V3-04'),

    # --- R01-16 : le choix par défaut du sommaire (décision 3) est celui du corps
    ('Un flux déterministe ou un agent unique bien outillé est le choix par défaut, et l’on',
     'Un flux déterministe, assisté au besoin par un modèle, est le choix par défaut; l’agent unique bien outillé vient ensuite, et l’on',
     'R01-16'),

    # --- R01-15 : une dérogation ne se renouvelle qu'une fois
    ('Une dérogation souvent renouvelée signale une règle à revoir.',
     'Une règle qui suscite des dérogations répétées est à revoir.',
     'R01-15'),

    # --- R01-31 : même fait, même formulation (la source [14] écrit « 10,000 active servers »)
    ('en décembre 2025 environ 10 000 serveurs actifs',
     'en décembre 2025 10 000 serveurs actifs',
     'R01-31'),

    # --- R01-39 : redites entre l'énoncé et les « Conséquences » de PRIN-03 et PRIN-04; encadré après PRIN-12
    ('et de la portée nécessaire à la tâche. Ses outils',
     'et de la portée nécessaire à la tâche<strong><sup>[96]</sup></strong>. Ses outils',
     'R01-39'),
    ('Conséquences\xa0: les droits effectifs d’un agent délégué ne dépassent jamais l’intersection des droits du mandant, de la portée de l’agent au registre et de la portée nécessaire à la tâche<strong><sup>[96]</sup></strong>, et ne s’élargissent jamais d’un saut à l’autre. Le serveur',
     'Conséquences\xa0: les droits effectifs d’un agent délégué ne s’élargissent jamais d’un saut à l’autre de la chaîne. Le serveur',
     'R01-39'),
    ('Conséquence\xa0: le niveau ne dépasse jamais le plafond de la classe de risque, fixé par l’EXIG-CON-02, seule source de ce plafond (section 12.1).',
     'Conséquence\xa0: l’EXIG-CON-02 reste la seule source de ce plafond (section 12.1).',
     'R01-39'),
    ('<div id="encadre-158">\n<p><strong>À RETENIR</strong></p>\n<p>Trois questions résument l’essentiel des principes qui encadrent l’action des agents (PRIN-03 à PRIN-06, PRIN-10 et PRIN-12; PRIN-07, qui porte sur ce que l’agent lit, relève d’une autre question). Qui a autorisé cette action, et au nom de qui? Peut-on la défaire, ou au moins l’arrêter? Peut-on reconstituer après coup ce qui s’est passé et ce que cela a coûté?</p>\n</div>\n<h4>Interopérer par des contrats ouverts</h4>',
     '<h4>Interopérer par des contrats ouverts</h4>',
     'R01-39'),
    ('(sections 7.8 et 9.9).</p>\n<h3>4.2 Application des principes</h3>',
     '(sections 7.8 et 9.9).</p>\n<div id="encadre-158">\n<p><strong>À RETENIR</strong></p>\n<p>Trois questions résument l’essentiel des principes qui encadrent l’action des agents (PRIN-03 à PRIN-06, PRIN-10 et PRIN-12; PRIN-07, qui porte sur ce que l’agent lit, relève d’une autre question). Qui a autorisé cette action, et au nom de qui? Peut-on la défaire, ou au moins l’arrêter? Peut-on reconstituer après coup ce qui s’est passé et ce que cela a coûté?</p>\n</div>\n<h3>4.2 Application des principes</h3>',
     'R01-39'),

    # --- R01-40 : tableau 6 (renvois aux principes) et tableau 10 (colonne et introduction)
    ('catalogue d’entreprise comme source de découverte (section 6.6 et section 6.8)</td></tr>',
     'catalogue d’entreprise comme source de découverte (PRIN-01, PRIN-02; section 6.6 et section 6.8)</td></tr>',
     'R01-40'),
    ('Registre obligatoire, aucun jeton de production sans fiche complète et à jour, cycle de vie contrôlé (chapitre 11)</td></tr>',
     'Registre obligatoire, aucun jeton de production sans fiche complète et à jour, cycle de vie contrôlé (PRIN-10; chapitre 11)</td></tr>',
     'R01-40'),
    ('Évaluation des facteurs relatifs à la vie privée (EFVP), transparence, droit à la révision et gestion des incidents (chapitre 12)</td></tr>',
     'Évaluation des facteurs relatifs à la vie privée (EFVP), transparence, droit à la révision et gestion des incidents (PRIN-06, PRIN-10; chapitre 12)</td></tr>',
     'R01-40'),
    ('<th><strong>Principes en tension</strong></th><th><strong>Situation</strong></th>',
     '<th><strong>Principes ou enjeux en tension</strong></th><th><strong>Situation</strong></th>',
     'R01-40'),
    ('Le tableau 10 illustre les tensions les plus fréquentes.',
     'Le tableau 10 illustre les tensions les plus fréquentes, entre deux principes ou entre un principe et un autre enjeu (la protection des renseignements personnels, l’utilité).',
     'R01-40'),

    # --- R01-25 : tableau 12, blocs de construction des services transversaux de l'EXIG-ARC-19
    ('<tr><td>Plan A</td><td>Identité de charge de travail; serveur d’autorisation; moteur de politiques; coffre de secrets</td><td>Identité par agent, jetons délégués, décision par appel</td><td>SPIFFE/SPIRE; Microsoft Entra Agent ID<strong><sup>[90]</sup></strong>; AgentCore Identity et AgentCore Policy (langage de règles compatible avec Cedar)<strong><sup>[102]</sup></strong></td></tr>',
     '<tr><td>Plan A</td><td>Identité de charge de travail; serveur d’autorisation; moteur de politiques; coffre de secrets; garde-fous; service d’approbation humaine signée</td><td>Identité par agent, jetons délégués, décision par appel; secrets jamais exposés à l’agent (EXIG-SEC-14); approbation signée par une personne (section 8.5)</td><td>SPIFFE/SPIRE; Microsoft Entra Agent ID<strong><sup>[90]</sup></strong>; AgentCore Identity et AgentCore Policy (langage de règles compatible avec Cedar)<strong><sup>[102]</sup></strong>; coffre de secrets, garde-fous et service d’approbation\xa0: SBB à désigner à l’homologation (EXIG-ARC-20), sans exemple retenu ici</td></tr>',
     'R01-25'),
    ('<tr><td>Plan B</td><td>Collecte et traitement de la télémétrie; évaluation</td><td>Collecte OpenTelemetry, caviardage, évaluation continue</td><td>OpenTelemetry Collector et son processeur de caviardage <em>(redaction)</em><strong><sup>[141]</sup></strong>; AgentCore Observability et Evaluations<strong><sup>[102]</sup></strong></td></tr>',
     '<tr><td>Plan B</td><td>Collecte et traitement de la télémétrie; évaluation; journal d’audit; budgets et quotas</td><td>Collecte OpenTelemetry, caviardage, évaluation continue; journal d’audit chaîné, signé et ancré (EXIG-OBS-12, EXIG-OBS-13); enveloppes et quotas de coûts (EXIG-FIN-04, EXIG-FIN-05)</td><td>OpenTelemetry Collector et son processeur de caviardage <em>(redaction)</em><strong><sup>[141]</sup></strong>; AgentCore Observability et Evaluations<strong><sup>[102]</sup></strong>; journal d’audit et budgets\xa0: SBB à désigner à l’homologation (EXIG-ARC-20), sans exemple retenu ici</td></tr>',
     'R01-25'),

    # --- R01-27 : qui révise les exemples de SBB chaque trimestre
    ('le comité les révise chaque trimestre, avec le catalogue des protocoles (section 11.7).',
     'l’architecture d’entreprise les révise chaque trimestre, avec le catalogue des protocoles (section 11.7).',
     'R01-27'),

    # --- R01-23 : EXIG-ARC-25, la condition d'isolation se lisait à l'envers
    ('<p><strong>Aucun magasin de mémoire partagé sans isolation</strong></p>',
     '<p><strong>Aucun magasin de mémoire longue partagé en écriture</strong></p>',
     'R01-23'),
    ('Une mémoire longue <strong>NE DOIT PAS</strong> être accessible en écriture à des agents ou à des serveurs MCP qui ne sont pas isolés les uns des autres; le partage passe',
     'Une mémoire longue <strong>NE DOIT PAS</strong> être accessible en écriture directe à plus d’un composant, agent ou serveur MCP; le partage passe',
     'R01-23'),
    ('Sont isolés des composants qui ont des identités de charge de travail et des espaces de noms distincts.</p>',
     'Chaque écrivain direct a sa propre identité de charge de travail et son propre espace de noms dans le magasin.</p>',
     'R01-23'),
    ('<td>Aucun magasin de mémoire partagé sans isolation</td>',
     '<td>Aucun magasin de mémoire longue partagé en écriture</td>',
     'R01-23'),
    ('Partager une table de mémoire modifiable entre serveurs MCP non isolés.',
     'Partager en écriture une table de mémoire entre plusieurs agents ou serveurs MCP.',
     'R01-23'),

    # --- V3-05 : contrôles d'écriture de l'EXIG-ARC-23 (mémoires épisodique et sémantique seulement)
    ('contrôles avant toute écriture en mémoire longue, aucun',
     'contrôles avant toute écriture en mémoire épisodique ou sémantique, aucun',
     'V3-05'),

    # --- R01-19 : classe de l'agent de facturation et seuils de classe (tableau 46)
    ('L’agent de facturation est de classe de risque modérée, plafonné au niveau N3; l’outil <code>emettre_avoir</code> est de palier P2 (écriture réversible), et le catalogue lui fixe un seuil d’exécution autonome de 500\xa0$, valeur propre à l’exemple.',
     'L’agent de facturation est de classe de risque modérée, plafonné au niveau N3, car aucun avoir qu’il peut émettre n’excède le seuil de classe que la fonction risques et conformité arrête pour lui (tableau 46); l’outil <code>emettre_avoir</code> est de palier P2 (écriture réversible), et le catalogue lui fixe un seuil d’exécution autonome de 500\xa0$, valeur propre à l’exemple et distincte du seuil de classe.',
     'R01-19'),
    ('action financière, juridique ou irréversible au-delà des seuils déclarés',
     'action financière, juridique ou irréversible au-delà des seuils de classe que la fonction risques et conformité arrête pour l’agent (EXIG-CON-01), distincts du seuil d’exécution autonome d’un outil',
     'R01-19'),

    # --- R02-02 : revue d'interopérabilité proportionnée (chapeau du chapitre 6, EXIG-INT-01 et ses reprises)
    ('Chaque intégration est examinée à quatre niveaux, du juridique au technique, et n’emploie',
     'Chaque intégration est examinée, de façon proportionnée, à deux ou à quatre niveaux, du juridique au technique, et n’emploie',
     'R02-02'),
    ('<p><strong>Revue d’interopérabilité à quatre niveaux</strong></p>',
     '<p><strong>Revue d’interopérabilité proportionnée</strong></p>',
     'R02-02'),
    ('<td>Revue d’interopérabilité à quatre niveaux</td>',
     '<td>Revue d’interopérabilité proportionnée</td>',
     'R02-02'),
    ('<li>Tous <strong>Revue d’interopérabilité aux quatre niveaux</strong> (juridique, organisationnel, sémantique, technique) consignée;',
     '<li>Tous <strong>Revue d’interopérabilité proportionnée</strong> (niveaux sémantique et technique, ou les quatre niveaux selon le tableau 14) consignée;',
     'R02-02'),
    ('résultat de la revue d’interopérabilité aux quatre niveaux (section 6.1)',
     'résultat de la revue d’interopérabilité proportionnée (section 6.1)',
     'R02-02'),

    # --- R02-22 : EXIG-INT-02, données structurées seulement; schéma de tiers dans un autre dialecte
    ('Les données échangées entre agents, entre agents et outils et sur le bus d’événements <strong>DOIVENT</strong>',
     'Les données structurées échangées entre agents, entre agents et outils et sur le bus d’événements (arguments et résultats structurés d’outils, parties <code>data</code> des messages A2A, charges utiles d’événements) <strong>DOIVENT</strong>',
     'R02-22'),
    ('est tenue à l’adaptateur ou à la passerelle.</p>\n<div id="pourquoi-331">',
     'est tenue à l’adaptateur ou à la passerelle. Un schéma de tiers qui déclare un autre dialecte (<code>$schema</code>) est inscrit avec son dialecte et validé par un validateur de ce dialecte, ou converti à l’adaptateur ou à la passerelle; à défaut, il est refusé. Le contenu non structuré (parties <code>text</code>, <code>raw</code> et <code>url</code>, blocs texte) n’est pas visé par la présente exigence.</p>\n<div id="pourquoi-331">',
     'R02-22'),

    # --- R02-09 : révision MCP de référence épinglée au catalogue (EXIG-MCP-02, 09, 15 et 22)
    ('mettre en œuvre la révision 2026-07-28, y compris la méthode <code>server/discover</code>.',
     'mettre en œuvre la révision de référence épinglée au catalogue (valeur initiale\xa0: 2026-07-28), y compris la méthode <code>server/discover</code>.',
     'R02-09'),
    ('conforme à la spécification MCP 2026-07-28\xa0: métadonnées de ressource protégée',
     'conforme à la spécification MCP de la révision de référence épinglée au catalogue (valeur initiale\xa0: 2026-07-28)\xa0: métadonnées de ressource protégée',
     'R02-09'),
    ('une politique fondée sur les en-têtes ne s’applique qu’aux requêtes de la révision 2026-07-28.',
     'une politique fondée sur les en-têtes ne s’applique qu’aux requêtes d’une révision qui les définit (2026-07-28 ou une révision ultérieure épinglée au catalogue).',
     'R02-09'),
    ('avoir migré vers la révision épinglée au catalogue (valeur initiale\xa0: 2026-07-28) au plus tard le 28 juillet 2027',
     'avoir migré vers la révision 2026-07-28 ou vers une révision ultérieure épinglée au catalogue au plus tard le 28 juillet 2027',
     'R02-09'),

    # --- R02-46 : requête HTTP dans l'ordre (ligne de requête, en-têtes, corps); R02-36 : domaine d'exemple
    ('<pre><code>{"jsonrpc": "2.0", "id": 42, "method": "tools/call",\n "params": {\n   "name": "approvisionnement_creer_bon_commande",\n   "arguments": {"idempotency_key": "…", "centre_cout": "CC-4410", "…": "…"},\n   "_meta": {\n     "io.modelcontextprotocol/protocolVersion": "2026-07-28",\n     "io.modelcontextprotocol/clientCapabilities": {"…": "…"},\n     "traceparent": "00-…-…-01"}}}</code></pre>\n<pre><code>POST /mcp HTTP/1.1\nHost: passerelle-agents.interne.exemple\nContent-Type: application/json\nAccept: application/json, text/event-stream\nAuthorization: Bearer &lt;jeton émis pour ce point d’accès de la passerelle&gt;\nMCP-Protocol-Version: 2026-07-28\nMcp-Method: tools/call\nMcp-Name: approvisionnement_creer_bon_commande\nMcp-Param-Cost-Center: CC-4410</code></pre>',
     '<pre><code>POST /mcp HTTP/1.1\nHost: passerelle-agents.ent.ca\nContent-Type: application/json\nAccept: application/json, text/event-stream\nAuthorization: Bearer &lt;jeton émis pour ce point d’accès de la passerelle&gt;\nMCP-Protocol-Version: 2026-07-28\nMcp-Method: tools/call\nMcp-Name: approvisionnement_creer_bon_commande\nMcp-Param-Cost-Center: CC-4410\n\n{"jsonrpc": "2.0", "id": 42, "method": "tools/call",\n "params": {\n   "name": "approvisionnement_creer_bon_commande",\n   "arguments": {"idempotency_key": "…", "centre_cout": "CC-4410", "…": "…"},\n   "_meta": {\n     "io.modelcontextprotocol/protocolVersion": "2026-07-28",\n     "io.modelcontextprotocol/clientCapabilities": {"…": "…"},\n     "traceparent": "00-…-…-01"}}}</code></pre>',
     'R02-46/R02-36'),
    ('<code>ca.exemple/palier-risque</code>',
     '<code>ca.ent/palier-risque</code>',
     'R02-36'),

    # --- C2-17 : la requête illustrée à la figure 7 est abrégée (jsonrpc et id absents du dessin)
    ('La requête illustrée est abrégée\xa0: une requête complète porte aussi les capacités du client dans <code>_meta</code>.',
     'La requête illustrée est abrégée\xa0: une requête complète porte aussi <code>jsonrpc</code> et <code>id</code>, ainsi que les capacités du client dans <code>_meta</code>.',
     'C2-17'),

    # --- R02-38 : force de l'indicatif dans un bloc d'exigence (règle de lecture de la section 1.4)
    ('et une justification introduite par «\xa0Pourquoi\xa0». Créent une obligation normative',
     'et une justification introduite par «\xa0Pourquoi\xa0». Dans l’énoncé d’un bloc, toute phrase à l’indicatif qui prescrit un comportement a la force du degré d’obligation inscrit à l’en-tête du bloc, même sans mot-clé en gras; la justification et les exemples sont informatifs. Créent une obligation normative',
     'R02-38'),
    ('les règles d’interprétation des sections 1.2 (critère de portée et règle du doute), 1.5, 1.6, 4.2 (devoir de l’architecte) et 4.3;',
     'les règles d’interprétation des sections 1.2 (critère de portée et règle du doute), 1.4 (force de l’indicatif dans un bloc), 1.5, 1.6, 4.2 (devoir de l’architecte) et 4.3;',
     'R02-38'),

    # --- R02-30 : la parenthèse « dont environ 72 000 » se rattache aux 77 000 jetons de départ
    ('d’environ 77 000 à environ 8 700 jetons (dont environ 72 000 pour les seules définitions); elle chiffre',
     'd’environ 77 000 jetons (dont environ 72 000 pour les seules définitions) à environ 8 700; elle chiffre',
     'R02-30'),

    # --- V3-08 : légende de la figure 6, cartes périphériques et non bandeaux du bas
    ('Les bandeaux du bas rappellent les fonctions transversales',
     'Les cartes périphériques rappellent les fonctions transversales',
     'V3-08'),

    # --- X1-16 : « maillage » à plusieurs sens; PDP absent du glossaire
    ('des catalogues multiples recréent le maillage au niveau de la gouvernance',
     'des catalogues multiples recréent le maillage N × M au niveau de la gouvernance',
     'X1-16'),
    ('Voir la section 12.2.</td></tr><tr><td><strong>Mandant</strong></td><td><em>principal</em>',
     'Voir la section 12.2.</td></tr><tr><td><strong>Maillage</strong></td><td><em>mesh</em></td><td>Terme à trois sens dans le cadre. (1) L’enchevêtrement des connexions point à point entre N agents et M systèmes, que le cadre remplace par N + M contrats communs derrière la passerelle (chapitre 2, PRIN-01). (2) Le maillage de services <em>(service mesh)</em>, dans lequel les services s’authentifient mutuellement, par exemple en mTLS avec des X.509-SVID (sections 9.3 et 9.4). (3) Le maillage libre, patron où chaque agent sollicite les autres sans plafond, que le cadre interdit (section 7.2). Le cadre n’emploie pas «\xa0maillage d’agents\xa0»\xa0: le point d’application des politiques y est la passerelle d’agents (voir PEP).</td></tr><tr><td><strong>Mandant</strong></td><td><em>principal</em>',
     'X1-16'),
    ('l’administrateur de politiques (PA) établissant ou coupant le chemin<strong><sup>[112]</sup></strong>. Dans le cadre,',
     'l’administrateur de politiques (PA) établissant ou coupant le chemin; PE et PA forment ensemble le point de décision des politiques (PDP) de la même architecture<strong><sup>[112]</sup></strong>. Dans le cadre,',
     'X1-16'),

    # --- X1-18 : AP2, don annoncé à la FIDO Alliance, transfert effectif non établi
    ('AP2, confié à la FIDO Alliance, et l’Universal Commerce Protocol',
     'AP2, dont le don à la FIDO Alliance a été annoncé le 28 avril 2026 (transfert effectif non établi à la fin d’octobre 2026), et l’Universal Commerce Protocol',
     'X1-18'),
    ('Google en a fait don à la FIDO Alliance le 28 avril 2026<strong><sup>[26, 41]</sup></strong>.',
     'Google a annoncé le 28 avril 2026 en faire don à la FIDO Alliance<strong><sup>[26, 41]</sup></strong>; le transfert effectif n’était pas établi à la fin d’octobre 2026.',
     'X1-18'),

    # --- C1-02 : l'historique consigne l'actualisation et les correctifs postérieurs au 28 octobre
    ('Modifications corrélatives\xa0: sommaire, figure 1, sections 1.1, 3.1, 4.1 et 14.2, EXIG-AUT-02, annexe F. Actualisation du 1<sup>er</sup>\xa0novembre 2026 et correctifs de cohérence interne consignés à l’annexe H (le détail des correctifs figure à la section H.6).</td></tr></tbody></table>',
     'Modifications corrélatives\xa0: sommaire, figure 1, sections 1.1, 3.1, 4.1 et 14.2, EXIG-AUT-02, annexe F.</td></tr><tr><td>1.1, mise à jour</td><td>1<sup>er</sup>\xa0nov.\xa02026</td><td>Actualisation (annexe H)\xa0: sources datées rouvertes sur leur source primaire, errata et incohérences prouvés (tableau 72) et propositions soumises au comité; l’architecture normative de la version 1.1 n’est pas modifiée.</td></tr><tr><td>1.1, mise à jour</td><td>3\xa0nov.\xa02026</td><td>Revue contradictoire\xa0: correctifs de cohérence interne, de précision normative et de vérification bibliographique intégrés au corps, aux figures et aux annexes A à G; relevé à la section H.6.</td></tr><tr><td>1.1, mise à jour</td><td>10\xa0nov.\xa02026</td><td>Correctifs ciblés de l’audit de novembre 2026, intégrés au corps, aux figures et aux annexes; relevé à la section H.6.</td></tr></tbody></table>',
     'C1-02'),

    # --- COQ-Cad-194 : appel de référence en exposant (ligne « Sources » du tableau 41)
    ('Sources\xa0: conventions OpenTelemetry GenAI et MCP v1.41.0<strong>[119, 386]</strong>; dernière colonne',
     'Sources\xa0: conventions OpenTelemetry GenAI et MCP v1.41.0<strong><sup>[119, 386]</sup></strong>; dernière colonne',
     'COQ-Cad-194'),

    # --- COQ-Cad-195 : « et coll. » partout
    ('de Feng et al.<strong><sup>[83]</sup></strong>',
     'de Feng et coll.<strong><sup>[83]</sup></strong>',
     'COQ-Cad-195'),

    # --- COQ-Cad-196 et COQ-Cad-200 : mention de source des figures 24, 25, 27 et 28 alignée sur les autres figures
    ('Source\xa0: CRE-IA-2026-01; les six domaines',
     'Source\xa0: cadre CRE-IA-2026-01; les six domaines',
     'COQ-Cad-196/200'),
    ('Source\xa0: CRE-IA-2026-01.</figcaption></figure>\n<ol>',
     'Source\xa0: cadre CRE-IA-2026-01.</figcaption></figure>\n<ol>',
     'COQ-Cad-196/200'),
    ('Source\xa0: CRE-IA-2026-01.</figcaption></figure>\n<p>Le passage du niveau 2',
     'Source\xa0: cadre CRE-IA-2026-01.</figcaption></figure>\n<p>Le passage du niveau 2',
     'COQ-Cad-196/200'),
    ('Source\xa0: CRE-IA-2026-01 (durées',
     'Source\xa0: cadre CRE-IA-2026-01 (durées',
     'COQ-Cad-196/200'),

    # --- COQ-Cad-198 : « logiciels-services » partout
    ('<p><strong>Des unités propres aux plateformes SaaS.</strong>',
     '<p><strong>Des unités propres aux logiciels-services.</strong>',
     'COQ-Cad-198'),
    ('des plateformes SaaS (EXIG-FIN-03)',
     'des logiciels-services (EXIG-FIN-03)',
     'COQ-Cad-198'),
]

JOURNAL = [
    ('Avertissements; § 1.7 (méthode)', 'Mention de l’actualisation du 1er novembre 2026 et de la revue contradictoire du 3 novembre 2026, postérieures à la date de référence du 27 octobre, avec renvoi à l’annexe H (H.4, H.6). Les effectifs de la revue (tranches, défauts, faits) ne figurent plus au corps et ne sont pas repris.', ['R01-28']),
    ('Sommaire exécutif, « Pourquoi maintenant »', 'Appels de référence [1] et [3] ajoutés aux deux premiers chiffres clés; chiffre et phrase composés dans un même paragraphe pour les quatre chiffres.', ['R01-37', 'V3-04']),
    ('Sommaire exécutif, décision 3', 'Le choix par défaut devient le flux déterministe assisté au besoin par un modèle; l’agent unique outillé vient ensuite (PRIN-08, section 7.2).', ['R01-16']),
    ('§ 1.6', '« Une dérogation souvent renouvelée » remplacé par « des dérogations répétées » (une dérogation ne se renouvelle qu’une fois, section 4.3 et EXIG-GOV-16).', ['R01-15']),
    ('§ 6.5 (MCP, rappel du projet)', 'Même fait, même formulation : « environ » retiré devant 10 000 serveurs actifs; la source [14] écrit « 10,000 active servers », sans « plus de » ni « public ». Correction proposée par l’audit (« plus de 10 000 serveurs publics ») non retenue.', ['R01-31']),
    ('§ 4.1 (PRIN-03, PRIN-04; encadré À RETENIR)', 'Redites retirées des « Conséquences » de PRIN-03 (intersection des droits, appel [96] porté à l’énoncé) et de PRIN-04 (plafond de la classe); encadré déplacé après PRIN-12.', ['R01-39']),
    ('§ 2.3 (tableau 6); § 4.3 (tableau 10)', 'Renvois aux principes ajoutés aux enjeux 3, 7 et 8 du tableau 6; colonne et introduction du tableau 10 élargies aux enjeux qui ne sont pas des principes. Légendes des tableaux 5, 6 et 10 non modifiées (liste des tableaux).', ['R01-40']),
    ('§ 5.4 (tableau 12)', 'Garde-fous, approbation humaine signée, journal d’audit et budgets ajoutés aux ABB des plans A et B; SBB à désigner à l’homologation pour les ABB sans exemple.', ['R01-25']),
    ('§ 5.4 (avant le tableau 12)', 'Les exemples de SBB sont révisés chaque trimestre par l’architecture d’entreprise, avec le catalogue des protocoles; la soumission de ces changements au comité, proposée par l’audit, n’est pas ajoutée (le catalogue des protocoles est seul soumis au comité, EXIG-GOV-18).', ['R01-27']),
    ('§ 5.5 (EXIG-ARC-25, anti-patrons); annexe D', 'Une mémoire longue n’a qu’un écrivain direct (agent ou serveur MCP), le partage passant par une ressource en lecture seule ou un service de mémoire; titre de l’exigence et ligne de l’annexe D alignés. Figure 4 non modifiable ici : libellé « magasin partagé entre serveurs non isolés ».', ['R01-23']),
    ('§ 5.5 (figure 4); annexe A.3', 'Contrôles d’écriture de l’EXIG-ARC-23 limités aux mémoires épisodique et sémantique à l’annexe A. Bandeau de la figure 4 non modifiable ici.', ['V3-05']),
    ('§ 5.6; § 12.1 (tableau 46)', 'Classe élevée : « seuils de classe » arrêtés par la fonction risques et conformité (EXIG-CON-01), distincts du seuil d’exécution autonome d’un outil; l’exemple de la section 5.6 le rappelle.', ['R01-19']),
    ('Chapitre 6 (chapeau); EXIG-INT-01; annexes A.3, B et D', 'Revue d’interopérabilité « proportionnée » (deux ou quatre niveaux) : chapeau, titre de l’EXIG-INT-01, grille d’homologation, fiche d’agent et registre.', ['R02-02']),
    ('§ 6.1 (EXIG-INT-02)', 'Exigence limitée aux données structurées; schéma de tiers dans un autre dialecte inscrit avec son dialecte et validé, ou converti, sinon refusé; contenu non structuré non visé.', ['R02-22']),
    ('§ 6.5 (EXIG-MCP-02, MCP-09, MCP-15, MCP-22)', 'La révision 2026-07-28 devient « la révision de référence épinglée au catalogue (valeur initiale : 2026-07-28) »; l’échéance du 28 juillet 2027 vise la révision 2026-07-28 ou une révision ultérieure épinglée.', ['R02-09']),
    ('§ 6.5 (requête tools/call; clé de métadonnées _meta)', 'Ligne de requête et en-têtes placés avant le corps, en un seul bloc; domaine d’exemple aligné sur « ent.ca » (passerelle-agents.ent.ca, préfixe ca.ent). Substitution d’un nom réservé (.example) non retenue : l’en-tête JWS en base64 de la carte d’agent (annexe C.3) encode « cles.ent… » sur une ligne déjà à la limite des 109 signes, et l’enregistrement de ent.ca n’est pas vérifié.', ['R02-46', 'R02-36']),
    ('§ 6.5 (figure 7, légende)', 'La mention « abrégée » couvre aussi jsonrpc et id. Dessin non modifiable ici.', ['C2-17']),
    ('§ 1.4', 'Règle de lecture : toute phrase à l’indicatif qui prescrit un comportement, dans l’énoncé d’un bloc d’exigence, a la force du degré d’obligation de l’en-tête; § 1.4 ajouté aux règles d’interprétation normatives.', ['R02-38']),
    ('§ 6.5 (règles d’usage des primitives)', 'Parenthèse « dont environ 72 000 » rattachée aux 77 000 jetons de départ.', ['R02-30']),
    ('§ 6.2 (figure 6, légende)', '« Bandeaux du bas » remplacé par « cartes périphériques ».', ['V3-08']),
    ('§ 2.3; annexe E (Maillage; PEP)', 'Entrée « Maillage » ajoutée au glossaire (trois sens, « maillage d’agents » non employé); PDP défini à l’entrée PEP (PE et PA).', ['X1-16']),
    ('§ 2.2; § 6.9', 'AP2 : don à la FIDO Alliance annoncé le 28 avril 2026, transfert effectif non établi à la fin d’octobre 2026.', ['X1-18']),
    ('Historique des versions', 'Lignes ajoutées pour l’actualisation du 1er novembre, la revue du 3 novembre et les correctifs de novembre 2026; numéro de version inchangé (1.1).', ['C1-02']),
    ('§ 10.1 (tableau 41, ligne « Sources »); annexe A.8', 'Appel de référence en exposant; « et al. » devient « et coll. ».', ['COQ-Cad-194', 'COQ-Cad-195']),
    ('Figures 24, 25, 27 et 28 (légendes); § 10.5 et 11.1', 'Mention « Source : cadre CRE-IA-2026-01 » alignée sur les autres figures; « plateformes SaaS » remplacé par « logiciels-services ».', ['COQ-Cad-196', 'COQ-Cad-200', 'COQ-Cad-198']),
]
