# Audit de publication — Compendium maître, édition consolidée de novembre 2026

Audit du 13 novembre 2026, sur `CompendiumMaster.pdf` (1 056 pages avant audit, 1 059 après)
et sur son manuscrit (`Master/manuscrit/`, 59 fichiers, environ 380 000 mots).

## Résultat

- **425 constats** relevés à la lecture intégrale : 17 bloquants, 121 majeurs, 287 mineurs.
- **356 corrections** portées au texte, toutes inscrites dans `corrections.json`
  (fichier, texte avant, texte après, catégorie, motif) et contrôlées par
  `compendium-master-verifie.py` : 121 de cohérence, 81 de terminologie, 68 résidus de
  fabrication, 28 de fait, 21 de langue, 14 de renvoi, 13 de temps, 10 de structure.
- **41 points laissés à l'auteur** (tableau en fin de document) : ils demandent une
  décision de fond qu'une correction courte ne peut pas prendre.
- 11 constats rejetés après vérification à la source, 22 non retenus (correction de
  goût, chiffre du cas fictif sans preuve, réserve de sourçage à garder), 41 réglés par
  une convention posée en tête d'ouvrage plutôt que par une correction.

Le détail de chaque constat, avec sa décision, est dans `constats.json`.

## Méthode

1. **Lecture intégrale** du manuscrit en dix tranches (neuf pour l'ouverture et les
   chapitres, une pour les annexes, confrontées aux chapitres), par dix agents de
   lecture en lecture seule, selon une grille commune : langue, cohérence, renvois,
   structure, résidus de fabrication, terminologie, temps, faits, fond.
2. **Arbitrage** des constats ouverts : l'exposé sourcé prime sur le volet; la prose
   s'aligne sur l'extrait de code qu'elle présente; un décompte faux se corrige au
   nombre annoncé; un fait douteux se vérifie à la source primaire. Huit tranches ont
   été arbitrées par leur agent de lecture, les deux dernières (chapitres 42 à 50) et
   les points transversaux par le coordonnateur.
3. **Revue** de chaque correction proposée avant application; une vingtaine écartées.
4. **Contrôles mécaniques** sur tout le manuscrit et sur le PDF (ci-dessous).
5. **Application** par registre, recomposition du PDF, vérification automatique.

Aucune relecture humaine n'a eu lieu. L'audit porte sur le texte et sa cohérence, non
sur une revérification des 936 sources : seuls les faits signalés comme douteux ont été
vérifiés en ligne (spécification A2A 1.0, conventions GenAI d'OpenTelemetry, RFC 6585 et
9420, documentation IBM, Solace, Restate, pages arXiv, brouillon AIMS de l'IETF, etc.).

## Contrôles mécaniques

| Contrôle | Résultat |
|---|---|
| Renvois de section, d'extrait, d'annexe et d'ADR | Tous résolus |
| Appels `[n]` et listes de sources, 50 chapitres | Appariés : aucun appel sans source, aucune source jamais citée |
| Gabarit des exposés (question, état de référence, grille, points, sources, limites) | Complet après harmonisation du bandeau des chapitres 44 à 47 |
| Cadence de révision des 31 fiches ADR | Cinq fiches se contredisaient (ADR-001, 019, 020, 022, 023) : alignées sur leur statut |
| PDF : débordement hors de la zone de texte, titres orphelins, glyphes manquants, balisage apparent | Aucun |
| PDF : signets, parties, chapitres, volets, figures | Conformes (1 938 signets, 67 figures) |
| Adresses des sources (790 distinctes) | 694 répondent; 1 morte (Gravitee, chapitre 23, signalée dans la source); 95 non concluantes depuis le poste d'audit (blocage des robots ou du mandataire : McKinsey, canada.ca, w3.org, github.com, doi.org), à revérifier depuis un navigateur |

## Décisions prises pour tout l'ouvrage

- **Plan initial.** Les sections « Limites » nommaient « table des matières » et « carte
  thématique » le plan de commande de l'ouvrage, que le lecteur ne voit pas : le terme
  est maintenant « plan initial », défini dans « À propos de cette édition ». Les
  mentions du « commanditaire » sont retirées.
- **Fil rouge.** Le cas du Groupe Boréal est une fiction située en 2027 et en 2028,
  racontée au passé : « À propos » le dit. Les faits du monde réel postérieurs à la
  date de référence et donnés pour accomplis ont, eux, été corrigés.
- **Dates de référence.** 11 novembre 2026 pour les chapitres 1 à 47, 13 novembre 2026
  pour la partie X : dit dans « À propos » et dans les annexes D et E.
- **A2A 1.0.** Les volets des chapitres 6, 27 et 32 et l'annexe F employaient les noms
  d'opérations de la version 0.3 : la prose et l'Extrait 27.1 suivent maintenant la
  version 1.0 (`SendMessage`, `returnImmediately`, `taskPushNotificationConfig`…);
  l'Extrait 6.1, gardé tel quel, est présenté comme suivant la syntaxe de la 0.3.
- **Terminologie.** « délégué confus » (glossaire compris), « OPC UA », « antipatron »,
  « point de contrôle », « réessayable », « géorepérage », « maîtrise de l'IA » (article
  4 de l'AI Act), encadrés « Astuce » et « Avertissement ».
- **Figures.** Titres incrustés corrigés dans `fig-f-1.svg`, `fig-f-2.svg` (numéros
  d'une ancienne structure) et `fig-44-a-1.svg` (valeurs et nom alignés sur le texte).
- **Annexe E.** Les sections E.1 à E.3 disent maintenant qu'elles portent sur les
  chapitres 1 à 47 et renvoient à E.4 pour la partie X.

## Après l'audit : compléments du 14 novembre 2026

Cet audit porte sur l'état du 13 novembre 2026. Le lendemain, 193 entrées ont été
ajoutées au registre, hors audit, sous deux catégories nouvelles.

- **164 enrichissements** : sections ou sous-sections ajoutées aux exposés de vingt
  chapitres (4, 8, 14, 18, 20, 21, 22, 23, 24, 26, 33, 34, 35, 37, 38, 39, 40, 41, 42
  et 44), avec leurs sources, leurs limites et les lignes correspondantes des grilles de
  décision et des points à retenir; puis révision de la partie X (chapitres 48 à 50) et
  de l'ouverture pour tenir compte de ces sources. Les chapitres 1 à 47 listent
  maintenant 774 sources, contre 709; la partie X, 244, contre 227.
- **29 harmonisations** : chronologie (annexe D) et décompte des sources (annexe E) mis
  à jour, quatre renvois croisés vers les nouvelles sections, la contradiction des
  limites du chapitre 19 sur le maillage d'événements, trois retouches de forme, et le
  passage des renvois de l'ouverture sous les repères des passages déclarés. Neuf lignes
  s'ajoutent au glossaire (annexe A), hors registre, ce que son contrôle admet.

Ces compléments passent tous les contrôles de `compendium-master-verifie.py`. Ils n'ont
pas été relus selon la grille de cet audit : aucune lecture intégrale, aucun arbitrage.
Le PDF compte 1 090 pages. Sa page « À propos de cette édition » décompte à part les
356 corrections de l'audit et les 193 compléments. Une évaluation d'ensemble de
l'édition, avec ses réserves, est dans `Master/evaluation/evaluation-academique.md`.

Les sources ajoutées ont été chargées le 14 novembre 2026, sauf celles que les limites
des chapitres donnent pour non lues. Aucun nouveau contrôle d'ensemble des adresses n'a
été fait.

Deux points s'ajoutent à ceux que l'auteur doit trancher.

- **Sources connues par leur seul résumé.** Plusieurs compléments reposent sur le résumé
  d'une prépublication ou sur une analyse de cabinet; les limites de chaque chapitre le
  disent. Elles sont à lire en entier avant de s'y fier.
- **Textes restés inaccessibles.** Directive fédérale sur la prise de décisions
  automatisée, article 12.1 codifié de la loi québécoise sur le secteur privé, ligne
  directrice de l'AMF sur l'IA, référentiel SecNumCloud, rapport Gartner sur la gestion
  d'agents, documentation de ServiceNow, rapport McKinsey sur le maillage agentique.

## Après l'audit : plan de travail, priorités 0 et 1 (14 novembre 2026)

Le plan de travail `plan.md` reprend les points ouverts par ordre de gravité. Ses lots et
leurs comptes rendus sont dans `Master/lots/`; chaque lot passe par
`compendium-master-lot.py`, qui l'inscrit au registre.

- **Priorité 0.** Les 41 points laissés à l'auteur sont relocalisés dans
  `Master/audit/points-ouverts.json` : chaque point y est situé par son texte, avec sa
  ligne actuelle, son lot et son état. Ce fichier fait foi pour l'état des points; le
  tableau ci-dessous reste celui du 13 novembre. Un point était déjà clos : le glossaire
  donne « délégué confus » depuis l'entrée n° 257 (ch. 31, ligne 19).
- **Priorité 1, lot P1-B1.** Le point bloquant est clos (ch. 47, ligne 541) : le fil
  rouge du chapitre 47 reprend les chiffres du chapitre 25. Quatre entrées de catégorie
  `coherence`, n° 550 à 553. Le bilan du chapitre 47 dit maintenant que le sous-module
  de 2008 a été refait par l'usine d'après son oracle de transactions : ce raccord n'est
  pas dans le chapitre 25, et l'auteur doit le confirmer.
- **Priorité 1, lots P1-B2 à P1-B4 : ouverts.** La ligne directrice de l'AMF sur l'IA,
  la Directive fédérale sur la prise de décisions automatisée et la loi québécoise
  codifiée n'ont toujours pas été lues : aucun texte n'a été déposé dans
  `Master/recherche/sources-locales/`, et une recherche de copies archivées n'a rien
  donné. Les sections 38.2 à 38.4, 39.6 et 22.6 gardent leurs réserves.

Restent ouverts 39 points : 10 majeurs et 29 mineurs. Le registre compte 553 entrées :
les 356 corrections de l'audit et 197 inscriptions postérieures, que la page « À propos
de cette édition » décompte à part. Le PDF compte 1 091 pages et passe tous les
contrôles. Ces quatre corrections n'ont pas été relues par un second lecteur.

## Après l'audit : plan de travail, priorités 2 à 4 (14 novembre 2026)

Les comptes rendus sont dans `Master/lots/`; `Master/audit/points-ouverts.json` donne
l'état de chaque point.

- **Les 41 points laissés à l'auteur sont clos.** Les dix majeurs et les trente mineurs
  ont été tranchés selon les règles de l'audit (lots P2-M et P3-m); trois mineurs sont
  clos sans correction, après vérification à la source. Le tableau ci-dessous reste
  celui du 13 novembre.
- **Second audit des 193 compléments.** Deux lecteurs qui ne les avaient pas écrits ont
  relevé 95 constats : aucun bloquant, 19 majeurs, 76 mineurs. Quatre-vingt-six sont
  corrigés; neuf restent, listés dans `Master/lots/P2-fiabilite.md`.
- **Recollationnement de 200 chiffres.** 182 phrases vérifiables, 4 erreurs, soit
  2,2 %; 18 phrases non vérifiables.
- **Lecture au-delà du résumé.** Des 134 sources des chapitres 1 à 47 connues par leur
  seul résumé et citées, 124 ont été relues : 64 confirmées, 54 à nuancer, 6 en erreur.
  Les phrases sont corrigées, et les limites des chapitres disent quelles sources ont
  été relues. L'annexe E publie ces trois résultats.
- **Compléments.** Quatre lacunes déclarées sont comblées (ch. 14, 20, 24, 38), avec
  quatorze sources : les chapitres 1 à 47 en listent 789. Le cas fictif est signalé sur
  chaque encadré du fil rouge. Quatre sections de volet sans appui dans leur exposé le
  disent en tête, dont la section 38.10 sur le droit des contrats.

Ces contrôles lisent les sources par un outil qui en rend des extraits : aucun n'a été
recoupé sur le texte brut. Restent ouverts : les trois textes réglementaires jamais lus
(lots P1-B2 à B4), le contrôle des adresses des sources (lot P3-L1, refusé par le
contrôle de permissions), les quatre textes facultatifs du lot P3-L2 et le niveau de
preuve dans les grilles de décision (lot P4-1).

## Ce qui reste à décider avant impression

- **Auteur, mention légale, licence, ISBN** : la page de titre et les métadonnées du PDF
  n'en portent pas; rien n'a été inventé.
- **Libellé d'édition** : « Édition consolidée — novembre 2026 » est conservé.
- **Sources connues par un tiers** : Gartner, McKinsey, ISO et EUR-Lex restent cités par
  des reprises; les limites de chaque chapitre le disent.
- **Les 41 points ci-dessous.**

## Points laissés à l'auteur

| Fichier | Ligne | Gravité | Constat |
|---|---|---|---|
| ch. 47 | 541 | bloquant | Le fil rouge du chapitre 25 (lignes 681-691) ne parle ni de quatre agents CUA, ni de 0,62 $ par transaction, ni de 14 secondes par écran : il décrit une seule cellule CUA confinée sur un sous-module de 2008 (6,5 % du volume, 19 secondes par avenant), 14 programmes RPGLE déjà encapsulés en MCP et une refonte « Big Bang » de 28 M$… |
| ch. 05 | 446 | majeur | L'Extrait 5.1, intitulé « Cycle de vie protocolaire MCP », montre la poignée de main `initialize` d'avant la révision 2026-07-28, que la grille de décision impose pourtant à tout nouveau serveur distant. À l'auteur de refaire l'extrait (`server/discover`, version et capacités dans chaque requête) ou d'en changer le titre pour le… |
| ch. 10 | 40 | majeur | Nouveau constat issu de la vérification en ligne. L'exposé ne dit pas que Google a apporté AP2, et Mastercard Verifiable Intent, à la FIDO Alliance le 28 avril 2026 (groupe de travail technique sur les paiements). Or l'ouverture (l. 191), l'annexe H (l. 15), le chapitre 49 (l. 112, 341) et le volet du chapitre 11 (l. 432) rattac… |
| ch. 10 | 142 | majeur | La sous-section « Mastercard Agent Pay » ne décrit pas le produit (pages non lues, appui sur « un résumé de moteur de recherche », « Mastercard y annonce » sans antécédent clair). À l'auteur : la documenter sur une source lue (par exemple le communiqué de la FIDO Alliance du 28 avril 2026, qui présente Verifiable Intent), ou la … |
| ch. 12 | 803 | majeur | L'ADR-009 « Acceptée » impose Apache Ossie en production alors que la grille de décision (ligne 309) dit de ne rien bâtir en production sur `0.3.0.dev0`; le paragraphe de raccord constate l'écart sans conclure. L'auteur devrait dire dans l'ADR (décision b ou condition de révision) que l'adoption porte sur la version parue `0.1.1… |
| ch. 18 | 879 | majeur | Contradiction dans l'encadré : la situation antérieure donnait 14 jours en moyenne, alors que le résultat (ligne 891) part de 29 jours pour arriver à 13,5. Seule l'occurrence de la situation antérieure est corrigée. |
| ch. 27 | 242 | majeur | La ligne ne donne pas de version et ne contredit donc pas l'exposé à la lettre. Reste un écart de fond : le volet fait converser SAP Joule en A2A v1.0 (extrait 27.1), alors que le chapitre 26 établit que SAP vise A2A 0.3.0, incompatible avec la 1.0 (lignes 96 et 199), et que la page de Workday ne mentionne ni MCP ni A2A (ligne 1… |
| ch. 30 | 331 | majeur | Le volet rend obligatoires un propriétaire technique et un transfert ou une suspension automatique sous 72 heures au départ du parrain, alors que l'exposé du chapitre 29 constate que le propriétaire est facultatif chez Entra (l. 61) et qu'aucun mécanisme automatique de succession n'est décrit (l. 63). L'auteur pourrait préciser … |
| ch. 43 | 397 | majeur | Le seuil pass^5 ≥ 0,95 et l'exécution durable sont rattachés à deux portes différentes. Vague 3 / porte G3 ici, et alerte « GAP_G3:NEEDS_DURABLE_RUNTIME_AND_PASS5 » dans l'Extrait 43.2 (ligne 383); mais porte G2 dans la vague 2 (ligne 396 : exécution durable obligatoire), dans la politique Cedar « automatisant la Porte G2 » (lig… |
| ch. 44 | 526 | majeur | Contredit le fil rouge du chapitre 43 : à la même date (fin T1 2027), le chapitre 43 (ligne 464) annonce « 100 % des agents actifs munis d’identités SPIFFE nominatives », après révocation des clés personnelles à J+45 (ligne 395) et traitement des 19 Shadow Agents. De même, le chapitre 43 route tout le trafic LLM par la passerell… |
| ch. 45 | 287 | majeur | Un déploiement de 2027 est présenté comme accompli, alors que l'édition est arrêtée au 13 novembre 2026; la phrase affirme en outre un « état de l'art vérifié » que l'exposé dément (section 45.1 : négociation et collusion « relèvent encore de la recherche »; acceptation du vLEI non vérifiée). Même tournure ligne 424 (« En 2027, … |
| ch. 01 | 364 | mineur | La stratification attribuée à Gartner (Pace-Layered) comprendrait systèmes d'enregistrement, de différenciation et d'innovation; les « systèmes d'engagement » viennent d'une autre typologie. À l'auteur de retirer l'attribution à Gartner (« a suivi une stratification en trois étages ») ou de vérifier à la source; ne pas remplacer… |
| ch. 04 | 60 | mineur | Les parts ne se recoupent pas : 52 + 40 = 92 (et non 93), et 93 + 8 = 101. Effet d'arrondi probable; à l'auteur de vérifier dans l'étude MAP et, au besoin, d'ajouter « (arrondis) ». |
| ch. 04 | 93 | mineur | La section cite les trois causes de Gartner (hausse des coûts, valeur floue, contrôles insuffisants, l. 87) puis examine valeur floue, contrôles et gouvernance. À l'auteur de dire en une phrase que la hausse des coûts est traitée en 4.1 et que la gouvernance est une cause ajoutée par l'ouvrage. |
| ch. 10 | 349 | mineur | « MCP-UI » : 8 occurrences dans le chapitre 10 et 1 dans l'ouverture (l. 184); « MCP Apps » (extension officielle stable) : chapitre 5 (1), chapitre 7 (4), annexe B (2). Aucune entrée au glossaire de l'annexe A. La forme du volet revient plus de cinq fois : on ne corrige pas tout. À l'auteur de dire en 10.9 que MCP-UI désigne le… |
| ch. 16 | 780 | mineur | Fragment BPMN dit « exécutable » dont le graphe est rompu : aucun `sequenceFlow` ne relie `Task_PostGateDMN` à la passerelle `Gw_RouteAuthorization`, qui n'a aucun flux entrant. L'auteur devrait ajouter, après la ligne 780, un flux de `Task_PostGateDMN` vers `Gw_RouteAuthorization` (les cibles `Task_HumanUnderwriterReview` et `T… |
| ch. 16 | 847 | mineur | Chronologie du fil rouge serrée : « problème initial » au « début T1 2027 » (ligne 835), conformité validée trois mois avant le 1er mai 2027, soit vers le 1er février 2027, puis « bilan à 90 jours » (ligne 849). L'auteur devrait soit avancer le cadrage (fin 2026, cohérent avec le dossier initial du T4 2026 de l'ouverture), soit … |
| ch. 18 | 401 | mineur | Ligne « Latence de journalisation par pas » dont trois cellules sur quatre répondent « Aucune latence chiffrée (section 18.6) » : elle ne compare rien. L'auteur devrait soit supprimer la ligne du tableau, soit la retitrer « Persistance du journal » en retirant ces mentions et en adaptant la cellule AgentCore. |
| ch. 18 | 939 | mineur | La clé d'idempotence est décrite avec trois jeux de noms (WfId, Epoch, SeqId; espace de noms, workflowId, activityId; workflowId, stepSequenceId). L'auteur pourrait dire une fois que l'identifiant d'activité est le numéro de séquence de l'étape, et expliquer ou retirer « Epoch » dans la formule de la ligne 359. |
| ch. 19 | 259 | mineur | L'indicateur de gouvernance fixait un taux de dérive en `SagaDeadLetter` inférieur à 0,05 %, alors que le bilan du même volet affiche 0,06 % comme un résultat conforme. |
| ch. 30 | 218 | mineur | La page « Security Best Practices » de MCP est citée sous l'arborescence docs/…/tutorials/security/ au chapitre 30 et sous specification/2026-07-28/basic/ aux chapitres 24 et 31. Les deux arborescences peuvent coexister sur le site : l'auteur doit vérifier laquelle a été lue pour le chapitre 30 et aligner au besoin. |
| ch. 31 | 19 | mineur | Le chapitre 31 écrit « délégué confus » six fois (l. 19, 98, 202, 371, 373, 384), comme les chapitres 5 et 24, alors que le glossaire de l'annexe A donne « adjoint confus ». À harmoniser globalement : soit le glossaire s'aligne sur l'usage du corps (8 occurrences), soit le corps sur le glossaire. |
| ch. 31 | 698 | mineur | Le texte annonce quatre barrières (B1 à B4), mais le point 3, intitulé « Quarantaine de la mémoire et vue différentielle A2UI (B3 et B4) », ne décrit que la vue différentielle. L'auteur devrait ajouter une phrase sur la quarantaine de la mémoire (B3), puisque l'attaque visait une écriture en mémoire épisodique. |
| ch. 32 | 355 | mineur | Ordres de grandeur différents pour l'évaluation du PDP dans le même volet : « sub-milliseconde », « en microsecondes » ici; « 0,4 à 1,5 milliseconde » (l. 347), « < 2 ms » au 99e centile (l. 257), « 0,62 ms » (l. 626). Les chiffres peuvent viser le moteur Cedar seul d'un côté, l'appel complet au PDP de l'autre : l'auteur devrait… |
| ch. 34 | 297 | mineur | Les six couches énumérées dans la phrase (code d'orchestration, modèle, prompt et AGENTS.md, Agent Skills, schémas MCP, politiques Cedar/OPA) ne sont pas les six lignes du tableau qui suit (l. 305-310), qui ajoute le contrat A2A externe et fusionne Agent Skills et schémas MCP. À l'auteur d'aligner l'énumération de la phrase sur … |
| ch. 35 | 239 | mineur | Le cadre de Singapour (version 1.5) est cité sous deux adresses dans l'ouvrage; celle du chapitre 35 est la seule de sa forme. Constat déplacé du chapitre 39 (qui suit l'usage majoritaire) vers cette ligne. À l'auteur de vérifier que l'adresse majoritaire sert bien la version 1.5, puis d'unifier. |
| ch. 38 | 283 | mineur | Le manifeste 34.1 classe déjà l'agent boreal-bca-warranty-adjudicator « Tier-2-High » avec un seuil de 0,95, alors que la fiche 38.1 exige 0,97 pour le palier matériel. Aucune correction courte ne vaut pour les deux chapitres : à l'auteur de dire, s'il le souhaite, que le relèvement à 0,97 intervient avec la version 2.4.1. |
| ch. 43 | 395 | mineur | La méthode fixe une amnistie de 30 jours à la porte G1; le fil rouge du même volet (ligne 455) applique la porte G1 avec une « amnistie déclarative de trois semaines ». Harmoniser, ou dire que Boréal a raccourci le délai. |
| ch. 43 | 455 | mineur | Le chapitre répartit les 47 initiatives entre BEL (14), BCA (11), BSN (18) et les fonctions centrales (4); le dossier initial de l'ouverture (ligne 157) les situe « dans les trois divisions ». Les deux décomptes ne se recouvrent pas : préciser l'un ou l'autre. |
| ch. 45 | 430 | mineur | Le texte annonce une règle Cedar exacte « au centime et au kilogramme près »; l'Extrait 45.3 qui l'illustre est un arbitre Python (three_way_match.py) qui tolère un écart de 0,02 $ (ligne 497) et un ratio de tolérance sur la quantité (ligne 489). Accorder le texte et l'extrait. |
| ch. 46 | 198 | mineur | À vérifier dans la spécification TUF : elle ne prescrit pas, à ma connaissance, une clé hors ligne pour le rôle `snapshot`; dans les déploiements courants, `snapshot` et `timestamp` sont signés par des clés en ligne, seules `root` et `targets` étant hors ligne. |
| ch. 46 | 352 | mineur | La « configuration d'agentgateway » de l'Extrait 46.1 emploie le groupe d'API `gateway.aaif.linuxfoundation.org/v1`, alors que l'Extrait 44.1 configure le même agentgateway du Groupe Boréal sous `agentgateway.aaif.io/v1alpha2` (chapitre 44, ligne 262). Les noms de régions divergent aussi (`ca-central-montreal`/`ca-east-toronto` … |
| ch. 46 | 580 | mineur | La liste de contrôle renvoie aux « 6 substrats d’état proposés (section 46.9) », mais son énumération ne reprend pas les six couches de 46.9 : elle scinde la mémoire en deux (graphes, index vectoriels) et omet la sixième couche, les journaux d'abus et de télémétrie du fournisseur de modèle (ligne 309). |
| ch. 46 | 719 | mineur | Trois couches annoncées et énumérées, mais le tableau « Couche du pont cyber-physique » qui suit (lignes 731 à 736) en compte quatre : la planification locale / VLA et l'arbitre Simplex, fondus dans le point 3 de la liste, y sont deux couches distinctes. |
| ch. 46 | 811 | mineur | Les types d'action du manifeste (Extrait 46.6) ne portent pas les noms des primitives que la passerelle expose selon le texte (ligne 722 : `NavigateToNamedWaypoint`, `InspectGaugeAtPose`, `DockAtStation`). |
| ch. 47 | 432 | mineur | L'Extrait 47.2 interdit au bâtisseur specs/, tests/golden_master/ et .github/workflows/, mais pas tests/acceptance/, répertoire que le texte (lignes 301, 308, 326) désigne comme l'oracle verrouillé par ACL. Chemin à ajouter ou noms à harmoniser. |
| ch. 47 | 546 | mineur | « Contrats bissextiles » n'a pas de sens établi : seule une année est bissextile. Préciser (contrats signés une année bissextile, ou couvrant un 29 février). |
| ch. 47 | 728 | mineur | Le tableau autorise deux isolations R1 par 15 minutes, alors que la politique Cedar de l'Extrait 47.6 (context.mutationsInLast30Min == 0, valable pour R1 et R2), le fil rouge (ligne 888) et l'ADR-030 (ligne 908) limitent l'agent à une seule mutation par 30 minutes. |
| ch. 47 | 887 | mineur | La phrase déduit de « 64 % des incidents nocturnes R1/R2 résolus sans intervention humaine » une baisse des réveils de 19 à 5 par mois, soit 74 % : 64 % de 19 laisserait environ 7 réveils. Chiffres à réconcilier ou lien de cause à préciser. |
| ouverture | 22 | mineur | L'ouverture avance « plus de 300 organisations membres » puis indique que son propre chapitre 11 ne confirme pas ce chiffre (décompte de la section 11.2 : environ 260). À l'auteur de retirer le chiffre de 300 ou de le sourcer. |
| ouverture | 76 | mineur | Le parcours CISO / architecte IAM, dont la question porte sur les identités non humaines, saute le chapitre 29 (Identité agentique). Si l'auteur veut l'inclure, la correction la plus courte est « chapitres 29 à 32 ». |
