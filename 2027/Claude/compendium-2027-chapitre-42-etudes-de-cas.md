# Chapitre 42 — Études de cas

*Question directrice : que montrent les déploiements documentés ?*

> **Version 2 — 11 novembre 2026.** État de référence : article de Nubank publié à KDD 2026 (août 2026), étude *Measuring Agents in Production* dans sa version 4, portrait québécois des utilisations de l'IA au 15 juin 2026 et guide du MCN sur l'IA agentique (2026). Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [11] sont des pages primaires lues pour ce chapitre, [12] est secondaire. Les renvois « chapitre N » pointent vers les chapitres du compendium. Chapitre audité et révisé le 12 novembre 2026.

Les récits de déploiement d'agents abondent. Presque tous viennent de ceux qui vendent les agents : communiqués, résultats trimestriels, témoignages de clients. Ils donnent des chiffres sans dire qui a mesuré, par rapport à quoi, ni sur quelle période. Les textes où un déploiement est décrit avec sa méthode de mesure se comptent sur les doigts d'une main.

Ce chapitre s'en tient à ces textes. Il en a trouvé un pour le service à la clientèle, aucun pour le traitement de documents financiers, des fragments pour les opérations TI, et un registre sans évaluation pour le secteur public. La thèse tient en trois constats. Les déploiements documentés sont étroits : un agent, quelques outils, un parcours borné, un humain à portée. Ce qui les distingue n'est pas l'architecture de l'agent, mais ce qui l'entoure : API d'action, piste d'audit, évaluation. Et aucun ne documente l'usage d'un protocole d'interopérabilité. La preuve disponible porte sur la première marche de l'entreprise agentique, pas sur les suivantes.

---

## 42.1 Méthode : hiérarchie des preuves

### Six niveaux

Ce chapitre classe les textes sur un déploiement en six niveaux, du plus au moins probant.

| Niveau | Nature de la source | Source retenue ici | Ce qu'elle permet d'affirmer |
|---|---|---|---|
| 1 | Déploiement décrit par ses auteurs dans un article évalué par les pairs, avec mesure sur trafic réel | Nubank [1] | Une méthode et des gains relatifs, dans une organisation |
| 2 | Étude transversale menée par des chercheurs sur des organisations anonymisées | MAP [2] | Des pratiques répandues, sans audit des systèmes |
| 3 | Étude de cas publiée par un éditeur sur son propre produit | ServiceNow [3] | Des choix de conception; peu ou pas de résultats |
| 4 | Banc d'essai ou expérience contrôlée | [4] [5] [6] [7] | Des ordres de grandeur et des modes d'échec, hors production |
| 5 | Registre ou déclaration administrative | Portrait québécois [8] [9] | L'existence d'initiatives, pas leurs résultats |
| 6 | Communication de fournisseur | Écartée | Rien de vérifiable |

Trois questions suffisent à classer un texte. **Qui mesure ?** Un chercheur indépendant, l'équipe qui a bâti le système, ou le fournisseur. **Par rapport à quoi ?** Une référence humaine, une version antérieure, ou rien. **Qu'est-ce qui est tu ?** Les valeurs absolues, les coûts, les volumes et les échecs manquent presque toujours; leur absence borne ce qu'on peut conclure.

Même le premier niveau a ses limites. L'évaluation par les pairs valide une méthode, pas des chiffres de production que personne d'autre n'a vus. Un cas publié est aussi un cas choisi : aucune organisation ne soumet à une conférence le récit d'un projet abandonné.

### Les cas de fournisseurs, écartés

Un exemple montre pourquoi le sixième niveau est écarté. Le communiqué de la Linux Foundation du 9 avril 2026 sur la première année d'A2A fait état de déploiements actifs en production dans plusieurs secteurs, dont la chaîne d'approvisionnement, les services financiers, l'assurance et les opérations TI [11]. Il ne nomme aucune organisation qui exploite le protocole en production, ne donne que des indicateurs d'adhésion, aucune métrique d'usage, et ne décrit aucune méthode. Les huit entreprises nommées le sont comme soutiens, et les citations relevées viennent de leurs porte-parole. Le texte établit qu'un protocole est soutenu, non qu'il est utilisé.

Les chiffres de déploiement attribués à de grandes entreprises dans la presse spécialisée et dans les résultats financiers d'éditeurs posent le même problème : périmètre mouvant, absence de base de comparaison, source d'origine introuvable. Aucun n'est repris ici.

### Le cadre : l'étude MAP

L'étude *Measuring Agents in Production* fournit l'arrière-plan sur lequel lire chaque cas [2]. Vingt-cinq auteurs de cinq établissements, dont deux industriels (Intesa Sanpaolo et IBM Research), ont mené vingt études de cas par entrevue, dont quatorze portent sur des systèmes en production et six sur des pilotes, et recueilli 306 réponses valides à un sondage, dont 86 décrivent des agents déployés. Les données datent d'avril à novembre 2025. Le chapitre 4 en détaille les résultats, dont ceux-ci.

- Seize des vingt cas reposent sur des workflows structurés et prédéfinis; 68 % des agents sondés exécutent moins de dix étapes avant une intervention humaine, et 47 % moins de cinq.
- Dix-sept des vingt équipes ont bâti leur système elles-mêmes, par appels directs à l'API d'un modèle, sans cadriciel tiers, alors que 61 % des répondants au sondage disent en utiliser un.
- Les utilisateurs sont d'abord des employés (52 %), puis des clients externes (40 %).
- 74 % des répondants s'appuient surtout sur l'évaluation humaine; 39 % seulement comparent leur agent à une solution non agentique.

Les auteurs énoncent les limites de leur étude : recrutement par leurs réseaux professionnels, concentration dans les Amériques, aucun audit direct des systèmes décrits. Quinze des vingt cas viennent d'organisations mûres. Les cas sont anonymisés et fusionnés, de sorte qu'aucune affirmation ne peut être rattachée à une organisation.

---

## 42.2 Service à la clientèle à grande échelle

### Le cas

Le seul déploiement de premier niveau trouvé est celui de Nubank, banque numérique qui dit servir plus de cent millions d'utilisateurs. Onze de ses employés l'ont décrit dans un article publié à KDD 2026 [1]. Cinq agents de soutien y sont en production, bâtis sur le même cadre : livraison de carte, gestion de dettes, limite de crédit, gestion de carte, explication de produits.

### Une architecture délibérément simple

Chaque agent suit le patron ReAct, à l'intérieur de workflows définis comme des graphes dont le développeur contrôle l'exécution. Le texte ne décrit ni routeur ni système multi-agents, et ne mentionne ni MCP ni A2A. L'agent de livraison de carte dispose de trois outils : `get_customer_profile`, `check_card_delivery` et `reissue_card`. Sa première version n'en avait que deux, une recherche dans la base de connaissances et un transfert à un humain.

Le contexte de l'agent est découpé en composants versionnés séparément : instructions, routines tirées des procédures d'exploitation, macros, spécifications d'outils et mémoire de travail (chapitre 13). Quatre principes guident la conception des outils : composer les enchaînements déterministes dans le code plutôt que dans le prompt, traiter la description d'un outil comme un prompt, réduire la surface de sortie, concevoir pour l'idempotence.

L'agent transfère la conversation à un humain dans trois situations : la demande sort de ses routines, une donnée nécessaire est introuvable, ou sa confiance dans la réponse est faible. Il ne confirme une action au client que sur un succès explicite de l'outil.

### L'infrastructure avant le prompt

Les auteurs nomment un mode d'échec courant : commencer par les prompts et ajouter l'infrastructure ensuite. Ils recommandent l'ordre inverse. Trois couches doivent exister d'abord : identité et authentification, API d'action idempotentes, piste d'audit avec masquage des champs sensibles et durées de conservation. Leur argument est que ces couches survivent aux générations de modèles. L'affirmation repose sur leur expérience; l'article n'apporte pas de comparaison.

### Une démarche pilotée par l'évaluation

La contribution centrale de l'article est sa méthode d'évaluation, que le chapitre 33 détaille : critères binaires, étiquetage par trois analystes, juges automatiques optimisés contre ces étiquettes, puis tests A/B sur trafic réel, lancés à 1 % et élargis. Onze versions de l'agent de livraison de carte (V0 à V10) ont ainsi été comparées; le texte parle de dix variantes à un endroit et de onze à un autre, sans doute selon qu'il compte ou non la version initiale.

### Les résultats

Deux métriques d'affaires servent de juge. Le tNPS est un indice de recommandation mesuré juste après l'interaction. Le SSR (*self-service rate*), ou taux de libre-service, est la part des besoins résolus sans transfert à un humain.

| Cas d'usage | Gain de tNPS (points) | Gain de SSR (points) | Écart au tNPS des experts humains |
|---|---|---|---|
| Livraison de carte | +37 | +29 | −10 |
| Gestion de dettes | +40 | +2,9 | −23,6 |
| Limite de crédit | +4,5 | +7,5 | −7,1 |
| Gestion de carte | +38,3 | +4,8 | −1,1 |
| Explication de produits | +12,3 | −1,5 | −6,2 |

**Les gains sont relatifs.** L'article ne donne aucune valeur absolue de tNPS ou de SSR, et il n'est pas constant sur la base de comparaison : variantes antérieures de l'agent à un endroit, ancienne solution de soutien à un autre, groupe témoin ailleurs. Le gain de 37 points de la livraison de carte se mesure par rapport à V0, la variante la plus limitée. Le recul du SSR pour l'explication de produits est attribué à des échecs passagers de requêtes au modèle.

**L'agent reste sous l'humain partout.** Dans les cinq domaines, la satisfaction mesurée après une interaction avec l'agent est inférieure à celle qu'obtiennent les experts humains. L'écart est presque nul pour la gestion de carte et dépasse vingt points pour la gestion de dettes, que les auteurs tiennent pour le domaine le plus difficile.

**Les deux métriques se négocient.** Renvoyer les cas difficiles aux humains fait monter la satisfaction et baisser le libre-service. Un tableau de bord qui n'afficherait que l'une des deux serait trompeur.

L'article rapporte aussi une leçon de migration. Le passage de GPT-4.1 à GPT-5, plus strict dans le suivi des instructions, a exigé des prompts plus explicites, dont une consigne d'appeler les outils d'abord. Changer de modèle n'a pas été une simple substitution : c'est un changement à requalifier (chapitre 34), ce qui limite aussi la vitesse de bascule vers un modèle de secours (chapitre 46).

### Ce qui n'est pas dit

Ni les volumes de contacts, ni les pays, ni les coûts, ni la latence, ni le taux de transfert, ni la taille des échantillons des tests A/B, ni un test de signification ne figurent dans le texte. Le modèle retenu en production et le cadriciel d'orchestration ne sont pas nommés. Le cas démontre une méthode; il ne permet pas de calculer un rendement.

---

## 42.3 Traitement de documents financiers

### Un secteur qui déploie sans publier

Aucun déploiement documenté de traitement de documents financiers par agents n'a été trouvé. Le secteur n'est pourtant pas absent : dans le sondage de MAP, la finance et la banque comptent parmi les trois domaines les plus cités [2]. Mais aucun des cas d'étude que l'article énumère ne porte cette étiquette; le plus proche automatise un parcours de réclamations d'assurance. La meilleure preuve disponible est de quatrième niveau : un banc d'essai.

### Le banc d'essai

Deux auteurs de l'Université de New York ont comparé quatre architectures d'extraction sur 10 000 documents déposés auprès de la SEC, pour 25 champs répartis en trois familles : mesures financières, gouvernance, rémunération des dirigeants [4]. C'est une prépublication de mars 2026. Les architectures (pipeline séquentiel, fan-out parallèle, hiérarchie superviseur-travailleurs, boucle réflexive) sont décrites au chapitre 16, et leurs coûts au chapitre 40.
**Un document sur quatre contient au moins une erreur, dans le meilleur cas.** La meilleure configuration, réflexive, atteint un F1 de 0,943 par champ, mais une exactitude par document (tous les champs corrects) de 0,758. La plus simple, séquentielle, obtient 0,648 avec le même modèle, Claude 3.5 Sonnet. Aucune architecture ne dispense d'une revue; reste à savoir quels champs y envoyer. La configuration hiérarchique y répond par un seuil de confiance, fixé à 0,85 : les champs sous le seuil sont réattribués, deux fois au plus.

**L'avantage de l'architecture la plus précise ne tient pas à fort volume.** Sur une grappe de test fixe de huit nœuds, la boucle réflexive passe sous la configuration hiérarchique à 50 000 documents par jour et devient la moins précise des quatre à 100 000. Les auteurs l'expliquent par les files d'attente, qui tronquent les boucles de correction. Sa latence au 99e centile dépasse quatre minutes par document, pour une médiane de 74 secondes. Ces résultats de mise à l'échelle sont obtenus sous un budget de calcul fixe, hors production; l'article ne dit pas comment la charge a été générée.

**Chaque architecture a son mode d'échec.** Le pipeline séquentiel échoue surtout sur les renvois entre tableaux (28,4 % de ses erreurs). Les échecs de coordination entre agents, nuls dans le pipeline, représentent 8,1 % des erreurs du fan-out, 12,4 % de celles de la hiérarchie et 14,2 % de celles de la boucle réflexive. Cette dernière se perd surtout dans les divulgations ambiguës (39,3 %), où elle oscille d'une interprétation à l'autre. Ajouter des agents déplace les erreurs sans les supprimer (chapitre 21).

### Portée

Les auteurs énoncent leurs limites : dépôts en anglais auprès de la SEC, 25 champs fixes, tarifs de janvier 2025. Les cinq modèles évalués, de GPT-4o à Mixtral 8x22B, datent de 2024. Le texte contient aussi des incohérences : douze modes d'échec annoncés pour dix présentés, et une configuration optimisée dite récupérer 89 % de l'écart de précision entre pipeline et boucle réflexive, alors que son F1 de 0,924, entre 0,903 et 0,943, n'en récupère qu'environ la moitié. Les rapports entre architectures se transposent mieux que les valeurs.

---

## 42.4 Automatisation des opérations TI

### Un cas d'éditeur : générer le workflow, ne pas l'exécuter

Deux employés de ServiceNow ont décrit la conception de Workflow Generation, une fonction livrée dans la plateforme de l'éditeur [3]; la fiche de l'éditeur situe l'article à la conférence CAIN 2025 [12]. L'utilisateur formule un besoin en langage naturel et le système produit un workflow à faible code. Pour un besoin portant sur les incidents de priorité 1, il génère un déclencheur, une recherche d'enregistrement, une condition et l'envoi d'un courriel.

La conception décompose le travail en deux sous-tâches. La première génère le plan : le nom et l'ordre des étapes. La seconde remplit les entrées d'une étape à la fois. Un orchestrateur sans IA appelle la première une fois, puis la seconde pour chaque étape. Un module de recherche d'environ cent millions de paramètres fournit les noms d'étapes, de tables et de colonnes propres à l'installation du client; un modèle affiné de sept milliards de paramètres, servi par un seul GPU H100, génère le reste. Avant l'ajout de cette recherche, plus de 20 % des noms d'étapes et de tables étaient inventés dans les premières expériences.

Deux choix méritent d'être relevés. Le plan s'affiche d'abord, et l'utilisateur peut arrêter ou reformuler avant que les entrées soient générées. Et le remplissage n'a été activé que pour les étapes dont la qualité était jugée acceptable. Le modèle agit ici à la conception : il produit un artefact déterministe, que la plateforme exécute comme tout autre workflow (chapitre 17).

L'article est une étude de cas autodéclarée, et ses auteurs le reconnaissent. Il ne donne ni score d'évaluation, ni latence, ni coût, ni chiffre d'adoption.

### Les cas anonymes de MAP

Les opérations logicielles forment le bloc le plus fourni des cas que MAP énumère : migration de code, soutien aux développeurs, optimisation de requêtes SQL, assistance aux ingénieurs infonuagiques, et un cas de diagnostic et de résolution d'incidents [2]. Les pratiques rapportées sont défensives. Six équipes limitent leurs agents à la lecture seule. Trois les font tourner dans un bac à sable; un agent de migration teste ses changements dans un environnement miroir, et la fusion n'a lieu qu'après vérification. Une équipe place les outils de production derrière des API intermédiaires qui masquent les fonctions internes. Dans un cas, l'agent remet l'exécution à des ingénieurs.

Une observation touche l'autorisation. Une équipe reproduit les permissions de l'utilisateur par un contrôle d'accès fondé sur les rôles, et rapporte que l'agent peut tout de même contourner ces contrôles quand des outils ou des documents portent des permissions contradictoires (chapitre 30). L'étude ne donne aucun bénéfice mesuré par cas.

### Les bancs d'essai : loin de l'autonomie

| Banc d'essai | Tâche | Résultat rapporté |
|---|---|---|
| ITBench (IBM et Université de l'Illinois, février 2025) [5] | 94 scénarios d'automatisation TI | 13,8 % des scénarios de fiabilité résolus; 25,2 % en conformité et sécurité; 0 % en FinOps |
| ORCA-bench (version 3, septembre 2026) [6] | 1 079 tâches d'analyse de cause première | Meilleure exactitude : 25,3 % au niveau moyen, 10,0 % au niveau difficile |

Les deux textes sont des prépublications, lues par leur résumé; celui d'ORCA-bench a été relu à l'audit. ORCA-bench évalue cinq agents de pointe sur six jours de télémétrie d'un système de microservices instrumenté. Le modèle le plus faible avance une cause invraisemblable dans 40 % de ses rapports, et retirer l'accès au code source dégrade tous les modèles. Les auteurs concluent que les agents ne sont pas prêts pour une garde autonome, et rappellent que les systèmes réels sont bien plus vastes que leur banc. Une étude de 2024, menée sur des incidents de production de Microsoft, explorait déjà l'idée de donner à un agent les outils de diagnostic qu'une équipe emploie à la main; son résumé ne rapporte aucun résultat de déploiement [7].

### Lecture

Les trois types de preuves convergent. Ce qui est documenté en production, c'est l'agent qui prépare : il génère un workflow, pose un diagnostic, propose un correctif. L'action sur un système en marche reste à l'humain ou à un moteur déterministe. Les bancs d'essai justifient cette prudence. Le chapitre 34 traite l'exploitation des agents eux-mêmes; la section 47.6, ce qu'exige le passage à une remédiation automatisée, dont un catalogue d'actions bornées contre l'injection par les journaux.

---

## 42.5 Secteur public

### Un registre, pas une évaluation

Le Québec offre une source rare : une déclaration obligatoire. Depuis l'arrêté 2024-01 du 28 février 2024, les organismes publics déclarent chaque année leurs initiatives d'IA au dirigeant principal de l'information, et le ministère de la Cybersécurité et du Numérique (MCN) en publie le portrait [8]. Le chapitre 38 décrit le cadre juridique.

| Indicateur | 2024 | 2025 | 2026 |
|---|---|---|---|
| Initiatives déclarées | 168 | 258 | 432 |
| Organismes déclarants | 65 | 83 | 157 |
| Initiatives de services aux citoyens | 36 | 61 | 73 |

Au 15 juin 2026, les douze catégories d'usage ne comprennent aucune catégorie « agent ». Les plus proches sont l'interaction conversationnelle (53 initiatives) et l'automatisation intelligente des processus (46). La décision automatisée n'en compte qu'une. Les réseaux de la santé, de l'enseignement supérieur et de l'éducation portent les deux tiers du total.

Le jeu de données ouvert associe à chaque initiative un organisme, une catégorie, des bénéfices et un statut, en développement ou en production [9]. Une lecture de la première moitié du fichier de 2026 y relève neuf initiatives dont le nom ou la description emploie le mot « agent ». Ce sont surtout des agents conversationnels : ressources humaines dans des centres de services scolaires, service à la clientèle dans une université, accueil dans un musée. Cinq sont déclarées en production. Ce décompte est partiel et dépend du vocabulaire des déclarants; il indique une présence, pas une proportion.

Le portrait a les limites d'un registre. Les bénéfices sont déclarés par l'organisme, et rien n'indique qu'ils ont été mesurés. Les noms des solutions et des fournisseurs sont remplacés par des termes génériques, pour des raisons de sécurité. La cybersécurité, les renseignements classifiés et certains projets de recherche sont exclus. Rien n'y permet de dire ce qu'un agent fait, avec quels outils, ni avec quel résultat.

### Les cas que le guide autorise

Faute de cas évalués, le texte le plus instructif est celui qui encadre les cas à venir. Le guide du MCN sur l'utilisation responsable de l'IA agentique, daté de 2026, ne décrit aucun déploiement réel et ne nomme aucun protocole [10]. Il avertit : « Un agent d'IA ne devrait pas être retenu par défaut ». L'organisme doit d'abord vérifier qu'une amélioration de processus, une automatisation classique ou un assistant sans capacité d'action ne suffit pas.

Les premiers pilotes devraient être internes, réversibles, limités dans le temps, peu sensibles, supervisés, journalisés, mesurables et plafonnés en budget. Le guide recommande d'éviter en première phase ce qui touche des droits, des décisions administratives, des communications externes, des transactions financières ou des modifications de données officielles, sauf encadrement renforcé et validation spécialisée. Son annexe B propose quatre cas d'usage de référence.

| Cas d'usage de référence | Garde-fous minimaux |
|---|---|
| Préparation de dossiers internes | Sources approuvées, validation humaine, aucun envoi externe automatique |
| Triage de demandes internes | Aucune décision finale automatisée, escalade des cas ambigus |
| Contrôle de la qualité documentaire | Mode suggestion, corrections limitées, revue humaine |
| Centre de services interne | Base de connaissances approuvée, journalisation, transfert à un humain |

Le parcours d'autorisation compte trois étapes : filtrer le cas d'usage, vérifier la préparation du pilote, vérifier la préparation à la production. La dernière prévoit d'inscrire l'agent dans un registre et de tester le retour au mode manuel.

### Lecture

Le secteur public québécois en est à l'inventaire et au cadrage. Ses cas de référence ressemblent à ce que les cas privés documentés montrent déjà : des usages internes, où l'agent prépare et où l'humain valide. La différence est que le guide en fait une condition d'autorisation, là où les entreprises y arrivent par prudence.

---

## 42.6 Enseignements transversaux

### La preuve s'amenuise avec l'ambition

| Domaine | Meilleure preuve trouvée | Niveau | Ce qui manque |
|---|---|---|---|
| Service à la clientèle | Nubank [1] | 1 | Valeurs absolues, coûts, volumes |
| Documents financiers | Banc d'essai [4] | 4 | Tout déploiement documenté |
| Opérations TI | ServiceNow [3], MAP [2], bancs d'essai [5] [6] | 2 à 4 | Résultats mesurés en production |
| Secteur public | Portrait [8] [9], guide [10] | 5 | Toute évaluation |

Le domaine le mieux documenté est aussi le plus borné : des questions de clients sur un produit connu, avec un transfert possible à un humain. Plus la tâche engage des systèmes en marche ou des décisions, moins il existe de textes vérifiables.

### Ce que les cas ont en commun

**Des agents étroits.** Trois outils pour l'agent de livraison de carte de Nubank; deux sous-tâches enchaînées par du code ordinaire chez ServiceNow; des workflows prédéfinis dans seize des vingt cas de MAP. Aucun cas documenté ne repose sur un agent généraliste qui planifie librement.

**L'entourage compte plus que l'agent.** Identité, API idempotentes, piste d'audit, environnement miroir, API intermédiaires : les investissements décrits relèvent de l'ingénierie classique (chapitres 18 et 29). Ils durent plus longtemps que le prompt et que le modèle.

**L'évaluation fixe le rythme.** Nubank fait de la qualité de son pipeline d'évaluation le facteur qui détermine sa vitesse d'itération. MAP montre que cette discipline reste rare : les trois quarts des équipes étudiées (75 %, selon l'étude) évaluent sans jeu de bancs d'essai, et 39 % seulement des répondants comparent l'agent à une solution non agentique.

**L'humain reste la référence et le recours.** Il est la mesure à laquelle l'agent est comparé, et il n'est égalé dans aucun des cinq domaines de Nubank. Il est aussi le destinataire du transfert, l'exécutant du correctif, le valideur du dossier (chapitre 22).

### Ce que les cas ne montrent pas

**Aucun protocole d'interopérabilité.** L'article de Nubank ne mentionne ni MCP ni A2A. Dix-sept des vingt équipes de MAP, interrogées en 2025, ont bâti sur mesure. Le communiqué qui affirme l'usage d'A2A en production ne nomme personne [11]. Aucun texte lu ne décrit non plus d'agents de plusieurs entreprises qui négocient ou échangent des données entre eux (chapitre 45). Cela ne prouve pas que ces protocoles sont absents de la production : un article paraît souvent longtemps après le système qu'il décrit. Mais la thèse de l'ouvrage, selon laquelle l'interopérabilité conditionne la mise à l'échelle, ne s'appuie encore sur aucun cas documenté. Elle repose sur l'analyse des protocoles (chapitres 5 et 6), non sur l'observation.

**Aucun système multi-agents en production.** La seule comparaison chiffrée d'architectures multi-agents lue ici est un banc d'essai, et la part des échecs de coordination y croît avec la complexité de l'architecture.

**Aucun rendement.** Pas un des textes lus ne donne à la fois un coût et un bénéfice d'affaires; le banc d'essai financier chiffre un coût par document, mais en regard d'une précision. Les modèles de calcul du chapitre 40 ne peuvent donc pas être étalonnés sur des cas publics.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Preuve exigée avant d'imiter un cas | Niveau 1 ou 2 : mesure sur trafic réel ou étude indépendante | Cas de fournisseur recevable s'il nomme le client, la métrique, la base de comparaison et la période |
| Premier cas d'usage | Interne, réversible, surtout en lecture, mesurable | Service externe si le transfert à un humain, les API idempotentes et la piste d'audit existent déjà |
| Architecture de départ | Un agent par cas d'usage, peu d'outils, parcours borné | Multi-agents si les sous-domaines sont indépendants et que le gain est mesuré sur ses propres données |
| Ordre de construction | Identité, API d'action, audit, puis prompts | Prototype jetable, sans accès à des systèmes réels |
| Mesure du succès | Deux métriques opposées (satisfaction et libre-service), en test A/B, avec l'écart à la référence humaine | Usage interne à faible volume : revue humaine d'un échantillon |
| Extraction documentaire | Hiérarchie avec seuil de confiance et revue humaine des champs incertains | Boucle réflexive à faible volume quand l'erreur coûte cher; pipeline séquentiel à très fort volume |
| Opérations TI | Diagnostic en lecture seule; action par un humain ou un workflow déterministe | Action automatique sur des procédures réversibles, éprouvées en bac à sable |
| Génération de workflows | Plan montré à l'utilisateur avant le détail; exécution par le moteur existant | — |
| Changement de modèle | Revalidation des prompts et des juges sur le jeu d'étiquettes | — |
| Secteur public québécois | Les quatre cas de référence du guide, avec plafond de consommation | Usage touchant des droits ou des décisions : encadrement renforcé et validation spécialisée |

---

## Points à retenir

- Un seul déploiement d'agents à grande échelle a été trouvé dans un article évalué par les pairs avec mesure sur trafic réel : celui de Nubank, en service à la clientèle.
- Ses gains sont relatifs à une base mal définie, et ses agents restent sous les experts humains dans les cinq domaines mesurés.
- Pour les documents financiers, la preuve est un banc d'essai : au mieux, trois documents sur quatre sont entièrement corrects, et l'architecture la plus précise perd son avantage à fort volume.
- En opérations TI, les agents documentés préparent, diagnostiquent ou génèrent un workflow. Les bancs d'essai situent l'analyse autonome d'incidents entre 10 % et 25 % de réussite.
- Le portrait québécois recense 432 initiatives d'IA, sans catégorie pour les agents et sans résultat mesuré. Le guide du MCN réserve les premiers pilotes à des usages internes et réversibles.
- Les cas documentés ont quatre traits communs : agents étroits, infrastructure avant prompt, évaluation comme facteur limitant, humain comme référence et recours.
- Aucun cas documenté ne montre MCP, A2A ou un système multi-agents en production. Ce silence tient en partie au délai de publication, mais il laisse la thèse de l'interopérabilité sans appui empirique.
- Coûts, volumes et échecs manquent partout. Un cas se juge d'abord à ce qu'il tait.

---

## Sources

Pages primaires lues le 11 novembre 2026; [1], [2], [3], [4], [6], [8], [10] et [11] relues à l'audit du 12 novembre 2026 :

1. [Gupta et coll. — Building Customer Support AI Agents at 100M-User Scale, KDD 2026 (arXiv 2606.08867v1)](https://arxiv.org/html/2606.08867v1) — texte, sauf la fin de l'annexe.
2. [Pan et coll. — Measuring Agents in Production (arXiv 2512.04123v4)](https://arxiv.org/html/2512.04123v4) — texte, sauf la fin des annexes.
3. [Marquez Ayala et Béchard — Generating a Low-code Complete Workflow via Task Decomposition and RAG (arXiv 2412.00239)](https://arxiv.org/html/2412.00239)
4. [Kulkarni et Kulkarni — Benchmarking Multi-Agent LLM Architectures for Financial Document Processing (arXiv 2603.22651v1)](https://arxiv.org/html/2603.22651v1) — prépublication.
5. [Jha et coll. — ITBench (arXiv 2502.05352)](https://arxiv.org/abs/2502.05352) — prépublication; résumé seulement.
6. [Gong et coll. — ORCA-bench: How Ready Are Language Model Agents for Oncall? (arXiv 2607.28545)](https://arxiv.org/abs/2607.28545) — prépublication; résumé seulement.
7. [Roy et coll. — Exploring LLM-based Agents for Root Cause Analysis (arXiv 2403.04123)](https://arxiv.org/abs/2403.04123) — résumé seulement.
8. [Québec — Portrait des utilisations de l'IA dans l'administration publique](https://www.quebec.ca/gouvernement/numerique/intelligence-artificielle-administration-publique/portrait)
9. [Données Québec — Portrait public des utilisations de l'IA, jeu de données](https://www.donneesquebec.ca/recherche/dataset/portrait-public-des-utilisations-de-l-ia-dans-l-administration-publique-quebecoise) — métadonnées et première moitié du fichier de 2026.
10. [MCN — Guide sur l'utilisation responsable de l'intelligence artificielle agentique (PDF)](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/cybersecurite_numerique/Intelligence_artificielle/GU_IA_Agentique.pdf) — texte intégral.
11. [Linux Foundation — communiqué du 9 avril 2026 sur la première année d'A2A](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)

Source secondaire :

12. [ServiceNow AI Research — fiche de publication de l'article de Marquez Ayala et Béchard](https://www.servicenow.com/research/publication/orlando-marquez-gene-cain2025.html) — résultat de recherche seulement, page non lue.

## Limites de ce chapitre

- Toutes les pages, sauf le guide [10] lu en texte intégral, ont été lues au moyen d'un outil d'extraction automatique qui résume la page. À l'audit, les tableaux tirés de [1] et de [4], les chiffres de [2], le portrait [8] et le communiqué [11] ont été relus par le même outil et concordent; ils n'ont pas été collationnés à l'œil sur les PDF.
- MAP compte deux établissements industriels parmi les cinq de ses auteurs : son indépendance envers les organisations étudiées, que suppose le niveau 2, n'est pas établie. Sa part de 75 % d'équipes sans banc d'essai est un pourcentage, donné sans compte.
- La hiérarchie en six niveaux est une proposition de ce chapitre, pas un résultat de recherche.
- L'« étude sur la génération de workflows » que la table des matières nomme parmi les appuis n'est pas identifiée dans la carte thématique. L'article de ServiceNow [3] a été retenu parce qu'il correspond à cette description, sans certitude que ce soit l'étude visée. Sa parution à CAIN 2025 ne repose que sur [12] : la page arXiv relue ne la mentionne pas.
- Les intitulés de la table des matières sont conservés, mais la section 42.3 présente un banc d'essai et non un déploiement, et la section 42.4 repose en partie sur des bancs d'essai lus par leur seul résumé [5] [6] [7]. Les résultats d'ITBench datent de février 2025; ni son résumé ni une mise à jour n'ont été relus à l'audit. Le banc d'essai financier [4] ne dit pas comment la charge de ses essais de mise à l'échelle a été produite.
- La recherche de cas n'est pas exhaustive : une douzaine de pages ont été lues. D'autres articles industriels existent sans doute, et l'affirmation « un seul déploiement de premier niveau » vaut pour cette recherche seulement.
- Le fichier de données du portrait [9] n'a été lu qu'à moitié, et la répartition des initiatives par statut, publiée sous forme d'image, n'a pas été lue. Aucun cas du secteur public hors Québec n'a été examiné; les guides du Canada et de la Nouvelle-Galles du Sud que cite le guide du MCN n'ont pas été relus ici.
- La description de Nubank comme banque numérique et l'année de sortie des modèles du banc d'essai financier viennent de la connaissance générale. La réserve de la version 1 sur le sigle SSR est levée : la relecture de [1] y trouve « self-service rate ».
