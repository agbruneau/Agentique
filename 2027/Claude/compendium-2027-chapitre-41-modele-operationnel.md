# Chapitre 41 — Modèle opérationnel

*Question directrice : comment s'organise une entreprise où des agents travaillent ?*

> **Version 2 — 11 novembre 2026.** État de référence : articles de McKinsey du 26 septembre 2025 et du 5 octobre 2026, enquête State of AI du 25 août 2026, six travaux de recherche parus de 2022 à 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre : [1] à [10] ont été lues, les articles savants par leur résumé sauf [6]; [11] est secondaire. Les renvois « chapitre N » pointent vers la table des matières. Chapitre audité et révisé le 12 novembre 2026.

Les chapitres précédents traitent l'agent comme un objet technique. Or un agent en production a un propriétaire, des approbateurs et des collègues qui reçoivent ses sorties, relations qu'aucun protocole ne décrit.

Deux littératures en parlent, sans dire la même chose. Les cabinets de conseil décrivent une organisation aplatie, faite de petites équipes qui supervisent des dizaines d'agents. La recherche évaluée par les pairs montre qu'une équipe humain-IA ne fait pas mieux, en moyenne, que le meilleur des deux pris seul, et que les humains délèguent mal.

Thèse de ce chapitre : la ressource rare d'une organisation agentique est la capacité humaine de supervision et de jugement, pas le nombre d'agents. Le modèle opérationnel doit donc répartir le travail par conception, traiter la supervision comme un rôle et protéger les parcours qui forment le jugement.

---

## 41.1 L'organisation agentique : petites équipes orientées résultats

### Le modèle proposé

McKinsey nomme « organisation agentique » un paradigme où humains et agents travaillent côte à côte à grande échelle, et le décline en cinq piliers : modèle d'affaires, modèle opérationnel, gouvernance, main-d'œuvre et culture, technologie et données [1]. Le pilier opérationnel repose sur trois idées.

**Des flux conçus d'abord pour l'IA.** Le processus est repensé de bout en bout, et les humains y sont réintroduits de façon sélective : au-dessus de la boucle pour orienter, dans la boucle là où le contact humain compte [1].

**L'équipe agentique.** Un petit groupe multidisciplinaire possède et supervise les flux d'agents qui livrent un résultat d'affaires complet, par exemple l'accueil d'un client ou la clôture des comptes [1].

**Un réseau plutôt qu'une hiérarchie.** L'organigramme céderait la place à un réseau d'équipes qui s'échangent des tâches et des résultats, avec des structures de décision plates et un fort partage de contexte [1].

L'article de 2026 précise l'outil. La « carte d'orchestration » (*orchestration chart*) indique quels humains et quels agents se réunissent autour d'un résultat, ce que fait chacun, quels transferts subsistent et où l'imputabilité demeure [2]. Autonomie, accès, supervision et escalade deviennent des éléments de la conception du travail.

### Ce qui appuie le modèle

L'article de 2025 se présente lui-même comme un relevé de signaux précoces.

| Affirmation | Fondement déclaré | Portée |
|---|---|---|
| Deux à cinq personnes supervisent de 50 à 100 agents spécialisés [1] | Expérience des auteurs auprès de clients | Anecdote; aucune mesure publiée |
| Les organisations les plus avancées s'organisent davantage en équipes transversales de bout en bout [2] | Enquête auprès de plus de 700 dirigeants | Association; méthode non publiée |
| Près des trois quarts des organisations les plus performantes ont refondu leurs flux, contre un quart des autres [3] | Enquête mondiale annuelle | Déclaratif; association |

Deux nuances viennent des auteurs eux-mêmes. Il n'existe pas de structure gagnante unique : le point commun des organisations avancées est d'organiser le travail de bout en bout et de réduire les transferts [2]. Et aplatir ne crée de valeur que si la coordination supprimée est remplacée par une meilleure information, des droits de décision plus clairs et un jugement humain plus solide [2]. L'enjeu est réel : chez les clients du cabinet, les rôles de coordination ont crû de 1,5 à 2 fois plus vite que les rôles opérationnels en cinq ans [2].

### L'écart avec la pratique

L'organisation agentique est une direction, pas un état constaté. Selon l'enquête de 2026, 40 % des répondants d'organisations d'au moins un milliard de dollars de revenus disent mettre des agents à l'échelle dans au moins une fonction, et huit répondants sur dix déclarent un gain de productivité personnelle [3]. Mais 37 % seulement font état d'un effet positif sur le résultat d'exploitation, et 11 % des organisations auraient atteint le stade où le travail lui-même est repensé [2]. L'étude MAP montre des agents à courte portée : 68 % exécutent moins de dix étapes avant une intervention humaine [11] (chapitre 4).

Pour McKinsey, l'organisation existante devient la contrainte [2]. Le diagnostic est plausible, mais il vient d'un cabinet qui vend cette transformation.

---

## 41.2 Complémentarité humain-agent : ce que dit la recherche

### Une définition exigeante

La complémentarité désigne les conditions dans lesquelles une équipe humain-IA fait mieux que les humains seuls et mieux que l'IA seule. Un cadre publié en 2026 dans PNAS Nexus la fonde sur l'intelligence collective et sur trois processus cognitifs : raisonnement, mémoire, attention [5]. Il recense cinq facteurs sociotechniques, dont le calibrage de la confiance et la structure de la tâche, et cinq principes de conception : définir les buts et les contraintes, répartir les rôles, orchestrer l'attention et l'interrogation, bâtir des infrastructures de connaissance, former et évaluer en continu [5].

Montrer qu'un employé assisté fait mieux que sans aide ne démontre pas la complémentarité : il faut aussi battre l'agent seul.

### Ce que mesure la méta-analyse

Vaccaro, Almaatouq et Malone ont agrégé 106 expériences et 370 tailles d'effet, tirées d'études parues de janvier 2020 à juin 2023 [6].

| Comparaison | Taille d'effet (g de Hedges) | Lecture |
|---|---|---|
| Combinaison contre humain seul | 0,64 | L'IA améliore nettement l'humain |
| Combinaison contre le meilleur des deux | −0,23 | En moyenne, la combinaison fait moins bien |
| Idem, tâches de décision | −0,27 | Perte |
| Idem, tâches de création | 0,19 (non significatif) | Gain possible, non établi |
| Idem, quand l'humain seul surpasse l'IA | 0,46 | Gain |
| Idem, quand l'IA seule surpasse l'humain | −0,54 | Perte |

L'ajout d'explications ou d'un indice de confiance de l'IA ne modifie pas significativement ces résultats [6]. Les auteurs recommandent d'attribuer chaque sous-tâche au partenaire qui y excelle, plutôt que de laisser à l'humain la décision finale sur la tâche entière [6].

### Ce que montre l'expérience de terrain

Une expérience préenregistrée chez Procter & Gamble a réparti au hasard 776 professionnels sur de vrais problèmes d'innovation : seuls ou à deux, avec ou sans IA générative [7]. Les personnes seules munies de l'IA ont égalé les équipes qui n'en avaient pas. Avec l'IA, les propositions devenaient équilibrées entre technique et commercial, quelle que soit la spécialité de leur auteur [7]. Le résultat appuie l'idée d'équipes plus petites, mais pour des tâches de création et avec un assistant, non un agent autonome.

### Ce qu'il faut en tirer

Une revue systématique du Journal of Organizational Behavior situe les facteurs qui façonnent la relation entre humains et IA à trois niveaux : individu, groupe, organisation [8]. Agir sur un seul niveau, par exemple former les individus, ne suffit donc pas.

1. **« Un humain plus un agent » n'est pas une garantie.** Quand l'agent est meilleur que l'humain sur une tâche de décision, l'ajout d'un humain décideur tend à dégrader le résultat [6].
2. **La répartition se fait par avantage relatif, tâche par tâche.** Elle suppose de mesurer séparément l'humain seul, l'agent seul et la combinaison, ce que peu d'organisations font.
3. **La supervision se justifie par l'imputabilité, non par la performance.** Un point d'approbation existe parce qu'une personne doit répondre d'une action irréversible (chapitres 22 et 39). Il ne faut pas en attendre une meilleure décision moyenne.

Réserve : ces travaux portent sur des aides à la décision et des assistants, pas sur des agents qui agissent par des outils.

---

## 41.3 Déléguer : conception du travail et confiance

### Les humains délèguent mal

Une expérience publiée dans Information Systems Research compare deux sens de délégation sur une tâche de classification [9]. Quand l'IA délègue une partie des cas aux humains, l'équipe dépasse l'IA seule, même si les humains sollicités sont peu performants. Quand ce sont les humains qui délèguent à l'IA, aucun gain n'apparaît.

L'explication des auteurs écarte l'aversion pour les algorithmes : les participants appréciaient l'aide et suivaient une stratégie cohérente. Ce qui leur manquait est la métaconnaissance, c'est-à-dire la capacité d'évaluer ce qu'ils savent et ne savent pas. Les auteurs la décrivent comme un trait inconscient [9], donc peu sensible à une simple consigne.

Un modèle opérationnel qui laisse chaque employé décider quoi confier à l'agent repose sur la faculté humaine la moins fiable de l'expérience.

### Concevoir plutôt que laisser choisir

- **La règle remplace le choix individuel.** Ce que l'agent traite seul, ce qu'il propose et ce qui lui est interdit se fixe par classe de décision (chapitre 22) et s'inscrit dans la carte d'orchestration [2].
- **L'escalade part de l'agent.** Le sens de délégation qui fonctionne est celui où le système renvoie des cas à l'humain [9], sur des critères définis d'avance.
- **L'humain reçoit une rétroaction sur son propre jugement.** Sans mesure de ses erreurs, il ne peut pas calibrer ce qu'il confie. Cette déduction est propre à ce chapitre.
- **La charge cognitive se règle.** Trop peu d'engagement mène à une dépendance excessive envers l'IA; trop de responsabilités ajoutées, à la surcharge [2].

### La confiance, côté équipe

Une expérience en laboratoire du Journal of Management Information Systems a fait varier la nature d'un coéquipier (humain ou IA) et sa performance [10]. Les coéquipiers IA ont été jugés plus compétents et plus intègres que les humains, mais moins bienveillants. Les écarts se compensent : ni la confiance globale ni la volonté de travailler avec l'IA ne diffèrent. La satisfaction à l'égard du processus de travail, elle, est plus faible avec un coéquipier IA [10].

Le risque dominant n'est donc pas le rejet, mais double : une confiance mal calibrée, visible dans la fatigue d'approbation (chapitre 22), et une expérience de travail appauvrie. Quand le système rédige le premier jet, l'humain se sent moins producteur que réviseur du travail d'un autre [2].

### La confiance, côté organisation

Selon McKinsey, 70 % des répondants se disent personnellement prêts pour l'IA, alors que 27 % des dirigeants jugent leur organisation prête [2]. La confiance des employés dans le soutien de l'organisation est associée à la valeur créée, à chaque stade de maturité [2]; l'article ne publie pas la méthode de l'enquête.

---

## 41.4 Rôles de supervision

### Trois profils, selon McKinsey

L'article de 2025 annonce trois profils [1] :

- des **superviseurs en M**, généralistes à l'aise avec l'IA, qui orchestrent agents et humains à travers plusieurs domaines;
- des **experts en T**, spécialistes qui repensent les flux, traitent les exceptions et garantissent la qualité;
- des **employés de première ligne augmentés**, qui passent moins de temps dans les systèmes et plus avec les personnes.

Ces profils de compétences ne disent pas qui répond de quoi.

### Les rôles à attribuer

Le tableau rassemble les responsabilités réparties par les chapitres de gouvernance et d'exploitation; l'assemblage est une proposition de ce chapitre.

| Rôle | Répond de | Renvoi |
|---|---|---|
| Propriétaire de l'agent | Finalité, limites d'autorité, poursuite ou retrait | Chapitre 39 |
| Responsable d'équipe agentique | Résultat d'affaires de bout en bout; répartition du travail entre humains et agents | [1][2] |
| Expert de domaine | Exceptions, cas limites, qualité | [1] |
| Approbateur | Actions irréversibles ou à fort enjeu, cas par cas | Chapitre 22 |
| Équipe de plateforme | Déploiement, traces, mécanisme d'arrêt, modèle de secours | Chapitres 34 et 46 |
| Vérification indépendante | Contrôles de résultat, audit d'échantillon | Chapitres 33 et 34 |

Une même personne peut tenir deux rôles dans une petite équipe, sauf ceux de propriétaire et de vérificateur du même agent; le chapitre 47 applique la même séparation à l'agent qui produit du code.

### La capacité de supervision borne l'échelle

Selon l'article de 2025, l'adoption sera plafonnée par la capacité de supervision que les humains peuvent fournir, ce qui fait de la gouvernance un goulot possible [1]. La supervision changerait donc de nature : plutôt que de réviser ligne à ligne, les responsables définiraient des politiques, surveilleraient les cas atypiques et régleraient le degré d'intervention humaine [1].

La pratique varie. En mars 2025, avant la vague des agents, 27 % des répondants disaient que des employés révisaient tout le contenu produit par l'IA générative avant usage; une part comparable disait qu'au plus 20 % de ce contenu était vérifié [4].

Aucune source lue ne fournit de norme pour le nombre d'agents qu'une personne peut superviser. La charge réelle dépend du taux d'exceptions, de la réversibilité des actions et de la qualité des demandes d'approbation, toutes mesurables (chapitres 22 et 34).

### Les agents de contrôle

McKinsey propose d'intégrer aux flux des agents critiques, des agents garde-fous et des agents de conformité [1]. Ils raccourcissent la file d'attente humaine sans déplacer l'imputabilité, qui reste humaine dans l'article même, et leur fiabilité s'établit comme celle de tout agent; un juge automatique s'étalonne contre des étiquettes humaines (chapitre 33).

---

## 41.5 Compétences

### Ce qui prend de la valeur

Trois compétences sont dites en demande croissante : la résolution de problèmes de bout en bout, la conception de systèmes et la reconnaissance des cas limites où les agents échouent [1]. Des employés sans formation technique apprendraient à gérer des flux agentiques aussi vite que des ingénieurs [1]; l'affirmation repose sur des observations précoces, non sur une étude.

La recherche suggère une quatrième compétence, la métaconnaissance [9] : savoir ce qu'on sait conditionne la délégation.

### Le problème de la relève

L'expertise se construit en faisant le travail d'entrée : l'analyste apprend en analysant. Si les agents absorbent ce travail, le gain de productivité d'aujourd'hui peut devenir un déficit de jugement demain [2]. Or le jugement est précisément ce que les rôles de supervision exigent.

Le modèle opérationnel doit donc prévoir comment se forme un superviseur qui n'a jamais exécuté la tâche supervisée. McKinsey avance trois réponses : la pratique délibérée et la rétroaction à la place du travail d'entrée disparu, des gestionnaires qui coordonnent moins et font davantage exercer un jugement à conséquences croissantes, et des cheminements qui récompensent la maîtrise d'un métier et l'orchestration d'agents plutôt que la taille de l'équipe dirigée [2].

### Former par rôle

L'article de 2026 décrit une institution financière passée d'une formation générale à un apprentissage par rôle, avec accompagnement entre pairs, développement propre aux gestionnaires et démonstrations répétées en situation réelle [2]. Du côté réglementaire, l'obligation européenne de maîtrise de l'IA a été allégée par le Digital Omnibus (chapitre 35), tandis que la ligne directrice E-23 du BSIF demande à la haute direction de veiller aux compétences (chapitre 39).

---

## 41.6 Conduite du changement

### L'adoption sans transformation

Le constat de 2026 est paradoxal : les employés utilisent l'IA chaque jour, et les flux de travail, les droits de décision, les incitatifs et les pratiques de gestion restent intacts [2]. En 2025 déjà, la refonte des flux était, parmi 25 attributs testés, celui qui pesait le plus sur l'effet déclaré de l'IA générative sur le résultat d'exploitation; 21 % des organisations utilisatrices disaient avoir refondu au moins certains flux [4]. Le modèle statistique n'explique toutefois qu'une faible part de la variance (R² de 0,20) et repose sur des déclarations [4].

Le taux d'utilisation est donc un mauvais indicateur de changement. Les marqueurs utiles portent sur la structure : transferts supprimés, composition des équipes modifiée, gestion du rendement révisée [2].

### Dire où va le gain

Les attentes sur l'emploi dépassent les faits. En 2026, 14 % des répondants d'organisations utilisatrices disent que l'IA a contribué à une baisse des effectifs dans l'année, alors que 32 % l'anticipaient un an plus tôt; 39 % prévoient une baisse pour l'année suivante [3].

McKinsey recommande de rendre explicite l'usage de la capacité libérée : plus de production, un travail différent, une charge plus soutenable, un coût moindre, ou une combinaison [2]. Une société des sciences de la vie fixe ainsi des principes avant les cas particuliers : l'IA appuie le travail sans remplacer l'expertise ni la supervision humaines, et que l'employé demeure imputable du travail assisté [2].

### Les leviers

- **Un mandat doté d'autorité.** La transformation traverse affaires, technologie, talents et risque; il faut un dirigeant capable de déplacer budgets et talents rares et de trancher [2].
- **L'exemple de la direction.** D'après un résumé de l'enquête, les organisations les plus performantes déclarent deux fois plus souvent un engagement démontré de leurs dirigeants et des processus définis de mesure de l'effet [3].
- **Un domaine vitrine.** Repenser un ou deux domaines de bout en bout pour apprendre en situation, plutôt que multiplier les pilotes [1].
- **L'apprentissage dans le travail.** Champions internes, démonstrations hebdomadaires, cercles de pairs [2].

---

## 41.7 Centre d'excellence ou modèle fédéré

### Ce que font les organisations

La seule donnée lue sur la structure date de mars 2025 et vise l'IA générative, non les agents [4]. Elle décrit une centralisation sélective :

- le risque, la conformité et la gouvernance des données suivent souvent un modèle entièrement centralisé, de type centre d'excellence;
- les talents techniques et l'adoption des solutions suivent le plus souvent un modèle hybride, mi-central, mi-réparti;
- les organisations de moins de 500 millions de dollars de revenus centralisent plus volontiers aussi ces deux éléments.

### Ce que propose McKinsey

L'article de 2025 range la montée en puissance d'un centre d'excellence en IA parmi les premiers gestes [1]. Celui de 2026 décrit une capacité d'exécution, l'« usine de missions agentiques » : elle prend un résultat d'affaires, refond le travail en flux hybride, construit agents et contrôles, puis laisse des actifs réutilisables [2]. Le responsable d'affaires y apporte le résultat visé, les contraintes et l'imputabilité; les fonctions de risque, de conformité, juridique et de ressources humaines y siègent dès le départ, et la propriété du produit est attribuée au lancement, non après le pilote [2].

### Une répartition par fonction

La question « centre ou fédération » est mal posée : la réponse diffère selon la fonction. Le tableau, synthèse propre à ce chapitre, s'appuie sur [2], [4] et les chapitres cités.

| Fonction | Placement | Raison |
|---|---|---|
| Politiques, classes de décision, appétit pour le risque | Central | Une règle par organisation (chapitre 39) |
| Identité, registre, passerelle, observabilité, routage d'inférence, arrêt d'urgence | Central, en plateforme | Contrôle uniforme; réutilisation (chapitres 23, 24, 29, 33, 34, 44) |
| Évaluation et vérification indépendante | Central ou partagé | Indépendance à l'égard du propriétaire |
| Refonte des flux de travail | Fédéré, appuyé par une équipe centrale | Exige la connaissance du domaine |
| Propriété et supervision des agents | Fédéré | L'imputabilité suit le résultat d'affaires |

Deux modes de défaillance encadrent le choix. Un centre qui examine tout devient un goulot (chapitre 39). Une fédération sans plateforme ni règles communes produit une prolifération d'agents sans contexte ni pilotage, que McKinsey tient pour une recette de chaos [1]. La feuille de route du chapitre 43 fixe l'ordre : la plateforme commune avant le deuxième agent.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Unité d'organisation | Petite équipe responsable d'un résultat de bout en bout, avec un propriétaire nommé par agent | Séparation des tâches imposée par la réglementation : conserver la frontière fonctionnelle |
| Répartition du travail | Par avantage relatif, tâche par tâche, consignée dans une carte d'orchestration | Tâche sans mesure comparative : humain décideur, puis mesurer |
| Qui décide de déléguer | La conception du travail, par classe de décision; l'escalade part de l'agent | Création ou exploration à faible enjeu : discrétion individuelle |
| Point d'approbation | Justifié par l'imputabilité et l'irréversibilité | Jamais pour « améliorer » une décision où l'agent est meilleur |
| Dimensionnement de la supervision | Selon la charge mesurée d'exceptions et d'approbations | Aucun ratio publié d'agents par personne n'est à reprendre |
| Formation | Par rôle, en situation, avec rétroaction sur le jugement | Sensibilisation générale : comme socle seulement |
| Relève | Pratique délibérée là où l'agent absorbe le travail d'entrée | Métiers dont le travail d'entrée n'est pas automatisé |
| Structure de pilotage | Central pour les règles et la plateforme, fédéré pour la refonte et la propriété | Petite organisation ou démarrage : tout centraliser |
| Mesure du changement | Flux refondus et résultats | Le taux d'utilisation ne renseigne que sur l'adoption |

---

## Points à retenir

- L'organisation agentique de McKinsey, faite de petites équipes orientées résultats qui supervisent des flux d'agents, s'appuie sur des cas de clients et des enquêtes déclaratives. C'est une direction, pas un état constaté.
- En moyenne, une combinaison humain-IA fait mieux que l'humain seul, mais moins bien que le meilleur des deux. Le gain apparaît quand l'humain est le plus fort sur la tâche.
- La supervision humaine se justifie par l'imputabilité, non par une meilleure décision moyenne.
- Les humains délèguent mal, faute de savoir évaluer ce qu'ils savent. La délégation se fixe par conception, et l'escalade part de l'agent.
- L'obstacle n'est pas le rejet des agents, mais une confiance mal calibrée et une satisfaction moindre à l'égard du processus de travail.
- La capacité de supervision borne la mise à l'échelle. Aucun ratio d'agents par superviseur n'est établi.
- Si les agents absorbent le travail d'entrée, la relève des superviseurs doit être organisée délibérément.
- Le changement se mesure à la refonte des flux, des rôles et des incitatifs, pas au taux d'utilisation.
- Centre d'excellence ou fédération : le choix se fait fonction par fonction, règles et plateforme au centre, refonte et propriété des agents dans les domaines.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [McKinsey — The agentic organization: Contours of the next paradigm for the AI era (26 septembre 2025)](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era)
2. [McKinsey — AI is changing work; now it has to change the organization (5 octobre 2026)](https://www.mckinsey.com/capabilities/people-and-organization/our-insights/ai-is-changing-work-now-it-has-to-change-the-organization)
3. [McKinsey — The state of AI in 2026: On the road to ROI (25 août 2026)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) — lecture partielle.
4. [McKinsey — The State of AI: How organizations are rewiring to capture value (12 mars 2025)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value) — lecture partielle.
5. [Gonzalez et coll. — Toward a science of human–AI teaming for decision making, PNAS Nexus 5(3), 2026](https://par.nsf.gov/biblio/10696564-toward-science-humanai-teaming-decision-making-complementarity-framework) — notice et résumé.
6. [Vaccaro, Almaatouq et Malone — When combinations of humans and AI are useful (arXiv 2405.06087; Nature Human Behaviour, 2024)](https://arxiv.org/abs/2405.06087) — texte de la prépublication.
7. [Dell'Acqua et coll. — The Cybernetic Teammate (NBER, document de travail 33641, avril 2025)](https://www.nber.org/papers/w33641) — résumé.
8. [Bankins et coll. — A multilevel review of artificial intelligence in organizations, Journal of Organizational Behavior 45(2), 2024](https://merit.url.edu/en/publications/a-multilevel-review-of-artificial-intelligence-in-organizations-i/) — notice et résumé.
9. [Fügener et coll. — Cognitive Challenges in Human–Artificial Intelligence Collaboration, Information Systems Research 33(2), 2022](https://ideas.repec.org/a/inm/orisre/v33y2022i2p678-696.html) — notice et résumé.
10. [Dennis, Lakhiwal et Sachdeva — AI Agents as Team Members, Journal of Management Information Systems 40(2), 2023](https://jmis-web.org/articles/1614) — notice et résumé.

Source secondaire :

11. [Measuring Agents in Production (étude MAP, arXiv 2512.04123)](https://arxiv.org/abs/2512.04123) — repris du chapitre 4, non relu ici.

## Limites de ce chapitre

- Le rapport State of Organizations 2026 de McKinsey, cité par la table des matières, n'a pas été lu. L'article [2] le remplace; la méthode des enquêtes qu'il cite n'y est pas publiée.
- Les enquêtes [3] et [4] ont été lues partiellement, sans leurs figures. À l'audit, les pages de McKinsey n'ont pas répondu; des résumés de recherche web confirment le titre et la date de [3], ses parts de 40 %, 37 %, 14 %, 32 % et 39 % et l'écart de refonte des flux. L'engagement des dirigeants « deux fois plus souvent » n'y figure que dans un résumé secondaire.
- Les chiffres de [2] n'ont pas pu être relus à l'audit; un résumé attribue les 11 % à une autre page de McKinsey.
- Les travaux [5], [7], [8], [9] et [10] ne sont connus que par leur résumé. L'article [7] aurait depuis paru dans Organization Science avec un échantillon légèrement différent (résumé de recherche non vérifié).
- La recherche citée en 41.2 et 41.3 précède les agents à base de modèle de langage ou porte sur des assistants. Sa transposition aux agents autonomes est une hypothèse de ce chapitre.
- Aucune étude évaluée par les pairs n'a été trouvée sur le nombre d'agents qu'une personne peut superviser, ni sur l'efficacité comparée d'un centre d'excellence et d'un modèle fédéré.
- Le lien entre travail d'entrée et formation de l'expertise (41.5) relève de la connaissance générale et de l'argument de [2], non d'une mesure.
- Les tableaux de 41.4 et de 41.7 sont des synthèses de ce chapitre.
