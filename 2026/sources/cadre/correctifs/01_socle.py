"""Correctifs du socle (v1.1) du Cadre de référence issus de l'audit (Option 1)."""

CORRECTIONS = [
    # --- O-09 : Art. 12.1 Loi 25 (« au moment où la personne est informée / où la décision lui est communiquée ») ---
    (
        'Article 12.1 de la Loi sur le privé (article 65.2 de la Loi sur l’accès pour les organismes publics)\xa0: avis au plus tard au moment de la décision;',
        'Article 12.1 de la Loi sur le privé (article 65.2 de la Loi sur l’accès pour les organismes publics)\xa0: avis au plus tard au moment où la personne est informée de la décision;',
        'O-09a',
    ),
    (
        '<li>Si décision sur une personne <strong>Décisions automatisées</strong> (art. 12.1 de la Loi sur le privé)\xa0: avis au plus tard au moment de la décision, explication des principaux facteurs,',
        '<li>Si décision sur une personne <strong>Décisions automatisées</strong> (art. 12.1 de la Loi sur le privé)\xa0: avis au plus tard au moment où la personne est informée de la décision, explication des principaux facteurs,',
        'O-09b',
    ),
    (
        'La personne en est informée au plus tard au moment de la décision, peut obtenir les RP utilisés',
        'La personne en est informée au plus tard au moment où la décision lui est communiquée, peut obtenir les RP utilisés',
        'O-09c',
    ),

    # --- Majeures vérifiées du socle ---
    (
        '<li>L’orchestrateur soumet cette action à un approbateur habilité, hors de la conversation; l’approbation produit un jeton signé lié à l’empreinte de l’action (section 8.5).</li>',
        '<li>L’orchestrateur soumet cette action à deux approbateurs habilités distincts (action P3 d’un agent de classe élevée, dont au moins un n’est pas le mandant), hors de la conversation; chaque approbation produit un jeton signé lié à l’empreinte de l’action (section 8.5, EXIG-AUT-15).</li>',
        'R02-06',
    ),
    (
        'T3 n’a jamais été marquée « terminée » : C3 n’est exécutée que si son effet est incertain.',
        'T3 n’a jamais été marquée « terminée » : C3 n’est exécutée que si l’issue de T3, une fois résolue, est un effet réalisé (EXIG-ORC-16).',
        'R03-05',
    ),
    (
        'Le jeton <strong>DOIT</strong> expirer au plus 15 minutes après sa signature.</p>\n<div id="pourquoi-725">',
        'Le jeton <strong>DOIT</strong> expirer au plus 15 minutes après sa signature; lorsqu’une compensation de saga est approuvée avec l’étape (EXIG-ORC-19), cette approbation est consignée au journal de compensation avec son empreinte et vaut jusqu’à la clôture de la saga.</p>\n<div id="pourquoi-725">',
        'R03-55',
    ),
    (
        '<p><strong>Jeton délégué après deux sauts (extrait)</strong></p>\n<pre><code>{\n  "iss": "https://idp.ent.ca",\n  "sub": "alice",\n  "aud": "https://mcp-finance.ent.ca",',
        '<p><strong>Jeton délégué après deux sauts (extrait : jeton émis pour la passerelle, qui l’échange ensuite pour <code>mcp-finance</code>)</strong></p>\n<pre><code>{\n  "iss": "https://idp.ent.ca",\n  "sub": "alice",\n  "aud": "https://passerelle-agents.ent.ca",',
        'R04-01a',
    ),
    (
        'L’orchestrateur échange le jeton d’Alice contre un jeton délégué à audience unique (étapes 2 et 3), que la passerelle vérifie avant l’appel (étape 5); le serveur cible agit au nom d’Alice, l’agent restant identifié comme acteur courant (étape 6).',
        'L’orchestrateur échange le jeton d’Alice contre un jeton délégué à audience unique visant la passerelle (étapes 2 et 3), que la passerelle vérifie et rééchange pour le serveur cible avant l’appel (étape 5); le serveur cible agit au nom d’Alice, l’agent restant identifié comme acteur courant (étape 6).',
        'R04-01b',
    ),
    (
        '<tr><td>OWASP Agentic AI – Threats and Mitigations (T1 à T17)</td><td>v1.0 du 17 février 2025 (T1 à T15); v1.1 de décembre 2025, qui ajoute T16, abus des protocoles inter-agents, et T17, compromission de la chaîne d’approvisionnement<strong><sup>[87]</sup></strong></td>',
        '<tr><td>OWASP Agentic AI – Threats and Mitigations (T1 à T15; T16 et T17 en v1.1)</td><td>v1.0 du 17 février 2025 (T1 à T15); v1.1 de décembre 2025 (T16, abus des protocoles interagents, et T17, compromission de la chaîne d’approvisionnement, sous réserve de confirmation de la v1.1)<strong><sup>[87]</sup></strong></td>',
        'R04-11a',
    ),
    (
        'chaque menace T1 à T17 pertinente et chaque technique MITRE ATLAS retenue aux exigences',
        'chaque menace T1 à T15 (et T16 à T17 si la v1.1 est confirmée) pertinente et chaque technique MITRE ATLAS retenue aux exigences',
        'R04-11b',
    ),
    (
        'champs libres des systèmes d’enregistrement, réponses d’outils, entrées de mémoire, messages et cartes d’autres agents. Le catalogue d’entreprise <strong>DOIT</strong> marquer',
        'champs libres des systèmes d’enregistrement, réponses d’outils dont la source n’est pas étiquetée fiable au catalogue (seuls les champs structurés et validés par schéma d’un système d’enregistrement interne pouvant recevoir cette étiquette du propriétaire de domaine), entrées de mémoire, messages et cartes d’autres agents. Le catalogue d’entreprise <strong>DOIT</strong> marquer',
        'R04-16a',
    ),
    (
        'champs libres des systèmes d’enregistrement, réponses d’outils, entrées de mémoire, messages et cartes d’autres agents. Il est traité',
        'champs libres des systèmes d’enregistrement, réponses d’outils dont la source n’est pas étiquetée fiable au catalogue, entrées de mémoire, messages et cartes d’autres agents. Il est traité',
        'R04-16b',
    ),
    (
        'NE DOIT PAS</strong> exécuter d’action [C] sans approbation humaine liée à l’action exacte (section 8.5), sauf s’il repart d’un contexte vierge exempt du contenu non fiable.</p>',
        'NE DOIT PAS</strong> exécuter d’action [C] sans approbation humaine liée à l’action exacte (section 8.5), sauf s’il repart d’un contexte vierge exempt du contenu non fiable (nouvelle session ouverte par l’orchestrateur et attestée à la passerelle par un nouvel identifiant de session, sans lecture de mémoire ou d’artefact étiqueté non fiable, seules les sorties contraintes du tableau 39 y étant admises).</p>',
        'R04-53a',
    ),
    (
        'Dès qu’une session a consommé du contenu non fiable, la passerelle d’agents <strong>DOIT</strong> retirer à l’agent, pour le reste de la session, les outils d’envoi vers l’extérieur',
        'Dès qu’une session a consommé du contenu non fiable, la passerelle d’agents <strong>DOIT</strong> retirer à l’agent, pour le reste de la session (sauf nouvelle session ouverte en contexte vierge selon l’EXIG-SEC-04), les outils d’envoi vers l’extérieur',
        'R04-53b',
    ),
    (
        '<tr><td><strong>Faible</strong></td><td>Données publiques ou internes non confidentielles; lecture seule ou actions internes réversibles; aucun effet sur une personne</td>',
        '<tr><td><strong>Faible</strong></td><td>Données publiques ou internes non confidentielles (aucun RP, aucun tiers); lecture seule ou actions internes réversibles bornées au domaine de l’agent; aucun effet sur une personne</td>',
        'R05-15',
    ),
    (
        '<li>Si classe modérée ou élevée <strong>Équipe rouge</strong> propre aux agents et suite d’attaques intégrée à la chaîne d’intégration; contrôles déterministes vérifiés. — <code>EXIG-SEC-23, -24, -25</code></li>',
        '<li>Si classe modérée ou élevée, niveau N3 ou N4, ou contenu non fiable consommé <strong>Équipe rouge</strong> propre aux agents et suite d’attaques intégrée à la chaîne d’intégration; contrôles déterministes vérifiés. — <code>EXIG-SEC-23, -24, -25</code></li>',
        'R06-05a',
    ),
    (
        'Le cadre l’exige avant la mise en production des agents de classe modérée ou élevée, puis au moins chaque année. Voir la section 9.9.',
        'Le cadre l’exige avant la mise en production des agents de classe modérée ou élevée, de niveau N3 ou N4 ou consommant du contenu non fiable, puis au moins chaque année (EXIG-SEC-23). Voir la section 9.9.',
        'R06-05b',
    ),
    (
        'Il est normatif par son contenu, pas par sa forme\xa0: tout outil de registre convient s’il conserve ces champs et leur historique.</p>',
        'Il est normatif par son contenu, pas par sa forme\xa0: tout outil de registre convient s’il conserve ces champs, leur historique et toute valeur ou justification que les exigences du cadre demandent d’inscrire à la fiche (plafonds, seuils, durées, écarts motivés aux recommandations).</p>',
        'R06-08',
    ),
    (
        '<tr><td><strong>Risque et autonomie</strong></td><td>Classe de risque</td><td>Faible, modérée ou élevée, avec l’analyse des critères de la section 8.2 et l’approbation obtenue</td><td>Conception</td></tr>',
        '<tr><td><strong>Risque et autonomie</strong></td><td>Classe de risque</td><td>Faible, modérée ou élevée, avec l’analyse des critères de la section 8.2 et l’approbation obtenue</td><td>Proposition</td></tr>',
        'R06-04',
    ),
    (
        '2 calcule l’empreinte et crée la demande h = SHA-256(outil ‖ arguments canoniques) 3 présente l’action exacte',
        '2 calcule l’empreinte et crée la demande h = SHA-256(JCS({outil, version, definition_digest, agent_id, task_id, arguments})) 3 présente l’action exacte',
        'V3-20',
    ),

    # --- Coquilles du socle du Cadre ---
    (
        '<td><strong>Feuille de route 2027-2030</strong>\xa0: calage sur le calendrier 2027-2030;',
        '<td><strong>Feuille de route</strong>\xa0: calage sur le calendrier 2027-2030;',
        'COQ-226',
    ),
    (
        'sans décision au 27 octobre 2026) <strong>[37]</strong>',
        'sans décision au 27 octobre 2026)<strong><sup>[37]</sup></strong>',
        'COQ-228',
    ),
    (
        'qualifie les clés d’API statiques d’antipatron;',
        'qualifie les clés d’API statiques d’anti-patron;',
        'COQ-230',
    ),
    (
        'quand c’est possible et aux niveaux N3 et N4, l’on réserve',
        'quand c’est possible et, aux niveaux N3 et N4, l’on réserve',
        'COQ-231',
    ),
    (
        'la taxonomie CoALA (Sumers et al., 2024), qui distingue',
        'la taxonomie CoALA (Sumers et coll., 2024), qui distingue',
        'COQ-232a',
    ),
    (
        'la taxonomie CoALA (Sumers et al., 2024).</figcaption>',
        'la taxonomie CoALA (Sumers et coll., 2024).</figcaption>',
        'COQ-232b',
    ),
    (
        'et <code>execute_tool</code> <strong><sup>[119, 120]</sup></strong>.',
        'et <code>execute_tool</code><strong><sup>[119, 120]</sup></strong>.',
        'COQ-233',
    ),
    (
        '(ASI06 <em>Memory &amp; Context Poisoning</em>) <strong>[28]</strong>.',
        '(ASI06 <em>Memory &amp; Context Poisoning</em>)<strong><sup>[28]</sup></strong>.',
        'COQ-234',
    ),
    (
        'SPIFFE et SPIRE, projets diplômés de la CNCF<strong>[70, 116, 117, 175]</strong>',
        'SPIFFE et SPIRE, au stade «\xa0Graduated\xa0» de la CNCF<strong><sup>[70, 116, 117, 175]</sup></strong>',
        'COQ-235',
    ),
    (
        'conformément au statut «\xa0Contenir\xa0» du catalogue des protocoles',
        'conformément au statut Contenir du catalogue des protocoles',
        'COQ-237',
    ),
    (
        'ce qui en fait une cible de falsification de requête côté serveur <em>(SSRF)</em>.',
        'ce qui en fait une cible de falsification de requêtes côté serveur (SSRF).',
        'COQ-241',
    ),
    (
        'elle figure au statut «\xa0Évaluer\xa0» du catalogue (section 6.3).',
        'elle figure au statut Évaluer du catalogue (section 6.3).',
        'COQ-242',
    ),
    (
        'sans elles, un identifiant deviné permet d’accéder',
        'sans ces mesures, un identifiant deviné permet d’accéder',
        'COQ-243',
    ),
    (
        'La migration suit les étapes suivantes.</p>',
        'La migration se fait en sept étapes.</p>',
        'COQ-244',
    ),
    (
        'sous ASI07, communication inter-agents non sécurisée<strong><sup>[28]</sup></strong>.',
        'sous ASI07, communication interagents non sécurisée<strong><sup>[28]</sup></strong>.',
        'COQ-246',
    ),
    (
        'flux en continu (SSE, pour <em>Server-Sent Events</em>, ou gRPC)',
        'flux en continu (SSE ou gRPC)',
        'COQ-247',
    ),
    (
        'par exemple pour des tests de fumée<strong><sup>[244, 245]</sup></strong>.',
        'par exemple pour des tests de vérification rapide <em>(smoke tests)</em><strong><sup>[244, 245]</sup></strong>.',
        'COQ-250',
    ),
    (
        'indique que Cisco fournit l’essentiel des contributions et restait sans décision au 27 octobre 2026<strong><sup>[37]</sup></strong>.',
        'indique que Cisco fournit l’essentiel des contributions; elle restait sans décision au 27 octobre 2026<strong><sup>[37]</sup></strong>.',
        'COQ-252',
    ),
    (
        '<p>Source\xa0: d’après NIST SP 800-207<strong>[73]</strong>; colonne de droite\xa0: choix du cadre.</p>',
        '<p>Source\xa0: d’après NIST SP 800-207<strong><sup>[73]</sup></strong>; colonne de droite\xa0: choix du cadre.</p>',
        'COQ-269',
    ),
    (
        'selon leurs pages de projet) <strong><sup>[116, 117, 321]</sup></strong>.',
        'selon leurs pages de projet)<strong><sup>[116, 117, 321]</sup></strong>.',
        'COQ-270',
    ),
    (
        'Un refus à n’importe quelle étape arrête l’appel; le coupe-circuit agit sur toutes les passerelles à la fois. Source\xa0: CRE-IA-2026-01.</figcaption>',
        'Un refus à n’importe quelle étape arrête l’appel; le coupe-circuit agit sur toutes les passerelles à la fois. Source\xa0: cadre CRE-IA-2026-01.</figcaption>',
        'COQ-271',
    ),
    (
        'en échange d’une révocation en quasi temps réel<strong><sup>[331]</sup></strong>.',
        'en échange d’une révocation en temps quasi réel<strong><sup>[331]</sup></strong>.',
        'COQ-273a',
    ),
    (
        'et par la révocation en quasi temps réel (EXIG-IAM-20).',
        'et par la révocation en temps quasi réel (EXIG-IAM-20).',
        'COQ-273b',
    ),
    (
        'celle-ci déconseille l’octroi implicite (NE DEVRAIT PAS) et ne fait que recommander',
        'celle-ci déconseille l’octroi implicite (SHOULD NOT) et ne fait que recommander',
        'COQ-274a',
    ),
    (
        'La RFC 9700 recommande la liaison du jeton à l’expéditeur (DEVRAIT)<strong><sup>[175]</sup></strong>;',
        'La RFC 9700 recommande la liaison du jeton à l’expéditeur (SHOULD)<strong><sup>[175]</sup></strong>;',
        'COQ-274b',
    ),
    (
        'et MuleSoft Agent Fabric<strong><sup>[138]</sup></strong>, avec sa passerelle Omni Gateway (anciennement Flex Gateway)<strong><sup>[138, 340, 341]</sup></strong>.',
        'et MuleSoft Agent Fabric, avec sa passerelle Omni Gateway (anciennement Flex Gateway)<strong><sup>[138, 340, 341]</sup></strong>.',
        'COQ-275',
    ),
    (
        'interrompre le système de façon sécuritaire (art. 14(4)e))<strong><sup>[61]</sup></strong>.',
        'interrompre le système de façon sécuritaire (art. 14, par. 4, point e))<strong><sup>[61]</sup></strong>.',
        'COQ-276a',
    ),
    (
        'qui l’amène à un état sûr (art. 14(4)e))<strong><sup>[290]</sup></strong>,',
        'qui l’amène à un état sûr (art. 14, par. 4, point e))<strong><sup>[290]</sup></strong>,',
        'COQ-276b',
    ),
    (
        '<td><strong>Admis</strong> ; option pour les GPU, avec réserves.</td>',
        '<td><strong>Admis</strong>; option pour les GPU, avec réserves.</td>',
        'COQ-277',
    ),
    (
        'conformément à EXIG-SEC-09. Ces composants sont des exemples,',
        'conformément à l’EXIG-SEC-09. Ces composants sont des exemples,',
        'COQ-278',
    ),
    (
        'avec EXIG-SEC-18, la passerelle constate que l’empreinte a changé',
        'avec l’EXIG-SEC-18, la passerelle constate que l’empreinte a changé',
        'COQ-279',
    ),
    (
        'les versions suivantes les déclarant obsolètes (v1.42.0, 12 juin 2026); la branche principale',
        'les versions suivantes les déclarant obsolètes; la branche principale',
        'COQ-280',
    ),
    (
        '<code>gen_ai.system_instructions</code> et, depuis la v1.38.0, <code>gen_ai.tool.call.arguments</code>',
        '<code>gen_ai.system_instructions</code>, <code>gen_ai.tool.call.arguments</code>',
        'COQ-281',
    ),
    (
        'selon le calendrier que modifie le règlement (UE) 2026/1744 (art. 113, tel que modifié par le règlement (UE) 2026/1744)<strong><sup>[58, 61, 94, 394]</sup></strong>.',
        'selon le calendrier que modifie le règlement (UE) 2026/1744 (art. 113)<strong><sup>[58, 61, 94, 394]</sup></strong>.',
        'COQ-282',
    ),
    (
        'selon la taxonomie MAST <em>(Multi-Agent System Failure Taxonomy)</em> (section 7.9),',
        'selon la taxonomie MAST <em>(Multi-Agent System Failure Taxonomy</em>; section 7.9),',
        'COQ-283',
    ),
    (
        'et, à titre informatif tant que le cadre officiel de conformité MCP se déclare instable, par ses tests (section 6.8).</p>',
        'et, à titre informatif, par les tests du cadre officiel de conformité MCP, tant que celui-ci se déclare instable (section 6.8).</p>',
        'COQ-284',
    ),
    (
        'Appels d’outils 9 / 15 Coût 0,52 $ / 0,75 $ Délai 38 s / 60 s',
        'Appels d’outils 9 / 15 Coût 0,52 $ CA / 0,75 $ CA Durée 38 s / 60 s',
        'COQ-287-288',
    ),
    (
        'de la télémétrie de la version épinglée et des résultats métier, et les transmettre au parrain et les inscrire au registre.',
        'de la télémétrie de la version épinglée et des résultats métier, les transmettre au parrain et les inscrire au registre.',
        'COQ-289',
    ),
    (
        'Les points marqués non dérogeable ne peuvent faire l’objet d’aucune dérogation',
        'Les points marqués «\xa0non dérogeable\xa0» ne peuvent faire l’objet d’aucune dérogation',
        'COQ-319',
    ),
    (
        '<em>RFC 8693 – OAuth 2.0 Token Exchange (§4.1 act claim)</em>',
        '<em>RFC 8693 — OAuth 2.0 Token Exchange (§4.1 act claim)</em>',
        'COQ-325a',
    ),
    (
        'RFC 9457 – Problem Details for HTTP APIs.',
        'RFC 9457 — Problem Details for HTTP APIs.',
        'COQ-325b',
    ),
    (
        'RFC 8785 – JSON Canonicalization Scheme (JCS).',
        'RFC 8785 — JSON Canonicalization Scheme (JCS).',
        'COQ-325c',
    ),
    (
        'Office des publications de l’Union européenne. doi:10.2799/78681.',
        'Office des publications de l’Union européenne. https://doi.org/10.2799/78681.',
        'COQ-327',
    ),
    (
        'MCP Authorization Extensions (ext-auth) : Enterprise-Managed Authorization',
        'MCP Authorization Extensions (ext-auth): Enterprise-Managed Authorization',
        'COQ-328',
    ),
    (
        'CLI Reference — Agent Directory Service. Agntcy, a Series of LF Projects, LLC.',
        'CLI Reference — Agent Directory Service. AGNTCY, a Series of LF Projects, LLC.',
        'COQ-329',
    ),
    (
        'Shavit, Y., Agarwal, S., Brundage, M., et al. (2023).',
        'Shavit, Y., Agarwal, S., Brundage, M. et al. (2023).',
        'COQ-330',
    ),
    (
        "<em>'One-size-fits-all' agent governance sets enterprises up to fail</em>",
        '<em>«\xa0One-size-fits-all\xa0» agent governance sets enterprises up to fail</em>',
        'COQ-331',
    ),
    (
        'EU Artificial Intelligence Act – Article 113 : Entry into Force and Application',
        'EU Artificial Intelligence Act — Article 113: Entry into Force and Application',
        'COQ-332',
    ),
    (
        'WebAssembly Community Group (s. d.). Security. WebAssembly.org.',
        'WebAssembly Community Group (s. d.). Security. webassembly.org.',
        'COQ-333',
    ),
    (
        'Announcing the "AI Agent Standards Initiative" for Interoperable and Secure Innovation.',
        'Announcing the «\xa0AI Agent Standards Initiative\xa0» for Interoperable and Secure Innovation.',
        'COQ-334',
    ),
    (
        '<em>AI Act — Article 14 : Human oversight</em>.',
        '<em>AI Act — Article 14: Human oversight</em>.',
        'COQ-335a',
    ),
    (
        '<em>AI Act — Article 2 : Scope</em>.',
        '<em>AI Act — Article 2: Scope</em>.',
        'COQ-335b',
    ),
    (
        '<em>AI Act — Annex III : High-risk AI systems referred to in Article 6(2)</em>.',
        '<em>AI Act — Annex III: High-risk AI systems referred to in Article 6(2)</em>.',
        'COQ-335c',
    ),
    (
        '<em>AI Act — Article 26 : Obligations of deployers of high-risk AI systems</em>.',
        '<em>AI Act — Article 26: Obligations of deployers of high-risk AI systems</em>.',
        'COQ-335d',
    ),
    (
        'AI Act — Article 50 : Transparency obligations for providers and deployers of certain AI systems.',
        'AI Act — Article 50: Transparency obligations for providers and deployers of certain AI systems.',
        'COQ-335e',
    ),
    (
        'Move GenAI semantic conventions to its own dedicated repository (demande de tirage nº 3696).',
        'Move GenAI semantic conventions to its own dedicated repository (demande de tirage n<sup>o</sup>\xa03696).',
        'COQ-336-346',
    ),
]
