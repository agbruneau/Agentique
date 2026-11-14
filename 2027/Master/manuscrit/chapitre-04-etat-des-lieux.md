# Chapitre 4 — État des lieux 2026-2027

*Question directrice : où en sont réellement les entreprises ?*

> **État de référence :** enquête McKinsey « The State of AI in 2026 », connue par un compte rendu du 1er septembre 2026; étude « Measuring Agents in Production » (version 4, juin 2026); taxonomie MAST (versions 2 et 3); pages de l'AAIF et du NIST consultées le 11 novembre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre, classées en pages primaires lues, sources secondaires lues et pages non chargées; les statistiques officielles [13] à [15] ont été lues le 14 novembre 2026.

Trois chiffres reviennent dans presque toutes les présentations sur l'IA agentique : la part des grandes organisations qui mettent des agents à l'échelle, la part des projets qui seront annulés, et le revenu que les éditeurs tirent de leurs agents. Aucun des trois ne mesure la même chose, et aucun ne dit ce que fait un agent une fois déployé.

Ce chapitre sépare le mesuré du prédit et de l'annoncé. L'adoption est réelle, mais concentrée dans les grandes organisations et peu visible dans les résultats financiers. Les agents qui atteignent la production y parviennent parce qu'ils sont étroits : peu d'étapes, un parcours fixé d'avance, un humain à proximité. Ce qui sépare le pilote de la production n'est donc pas d'abord la capacité du modèle de langage. C'est la fiabilité, l'évaluation et les contrôles, c'est-à-dire les sujets d'interopérabilité et d'orchestration dont traite le reste de l'ouvrage.

---

## 4.1 Adoption : mise à l'échelle dans les grandes organisations, stagnation ailleurs

### Ce que mesure l'enquête McKinsey

La dixième édition de l'enquête annuelle de McKinsey sur l'IA s'intitule « The State of AI in 2026: On the Road to ROI ». Sa page n'a pas pu être chargée [11]; les chiffres qui suivent viennent du compte rendu de la revue *FM* du 1er septembre 2026 [8].

| Indicateur | 2026 | Un an plus tôt |
|---|---|---|
| Agents mis à l'échelle dans au moins une fonction, organisations d'au moins 1 G$ US de revenus | 40 % | 27 % |
| Même indicateur, organisations plus petites | 22 % | 22 % |
| IA mise à l'échelle dans toute l'entreprise, tous répondants | 44 % | 38 % |
| Répondants qui attribuent à l'IA une part, même faible, du résultat d'exploitation (EBIT) | 37 % | À peu près la même |
| « Hauts performants » : au moins 5 % du résultat d'exploitation attribué à l'IA, effet jugé significatif | Environ 6 % | Inchangée |

**L'écart de taille se creuse.** La progression est entièrement le fait des grandes organisations; les autres n'ont pas bougé en un an. Le même écart vaut pour l'IA en général : 54 % des organisations d'au moins un milliard de dollars de revenus déclarent une mise à l'échelle à la grandeur de l'entreprise, contre environ le tiers des plus petites [8]. Le compte rendu n'en donne pas la raison.

**« Au moins une fonction » n'est pas l'entreprise.** L'indicateur de 40 % compte une organisation dès qu'un agent y est mis à l'échelle quelque part. Il ne dit rien du nombre de fonctions touchées ni du volume de travail confié. Lu à l'envers, il signifie que six grandes organisations sur dix n'ont encore mis aucun agent à l'échelle.

**La valeur financière ne suit pas l'usage.** Selon le même compte rendu, 80 % des répondants disent que l'IA a amélioré leur productivité individuelle et 50 % qu'elle les aide à mieux décider. La part qui en voit un effet sur le résultat d'exploitation est pourtant stable, et le groupe des hauts performants ne grossit pas. Environ 20 % déclarent que les coûts d'exploitation de l'IA limitent leur usage, et 60 % prévoient tout de même d'augmenter leurs investissements dans l'année [8]. Le coût d'inférence se réduit par le routage entre modèles, jugé au coût par résultat réussi (chapitres 40 et 44).

Ces chiffres sont des déclarations, non des mesures; l'échantillon et les dates de collecte sont inconnus.

### Ce que ne mesurent pas les chiffres des fournisseurs

Les éditeurs publient des indicateurs qui ressemblent à des mesures d'adoption et n'en sont pas.

Salesforce annonce, pour son deuxième trimestre de l'exercice 2027 (clos le 31 juillet 2026), un revenu récurrent annuel d'Agentforce supérieur à 1,5 milliard de dollars, en hausse de plus de 240 % sur un an [4]. Depuis ce trimestre, le périmètre d'Agentforce englobe aussi d'autres offres d'IA, dont Slackbot et Headless 360, sans indication d'un retraitement des périodes antérieures. La croissance n'est donc pas établie à périmètre constant, et un revenu contracté ne dit pas combien d'agents travaillent.

La Linux Foundation, dans son bilan de la première année d'A2A, compte plus de 150 organisations qui appuient le protocole, contre plus de 50 un an plus tôt, et cite son intégration à Azure AI Foundry, à Copilot Studio et à Amazon Bedrock AgentCore Runtime [3]. Le communiqué évoque des déploiements en production sans nommer de client ni donner de métrique. Appuyer un protocole n'est pas l'exploiter.

La règle de lecture vaut pour tout l'ouvrage : distinguer l'enquête déclarative, la prévision d'analyste et l'indicateur de fournisseur, et n'en tenir aucun pour une mesure de ce que font les agents (chapitre 42).

### Ce que mesurent les statistiques officielles

Trois offices statistiques publient une mesure qui ne dépend ni d'un cabinet ni d'un fournisseur. Elle porte sur l'IA en général, non sur les agents.

| Territoire | Mesure | Valeur | Un an plus tôt |
|---|---|---|---|
| Canada | Entreprises ayant utilisé l'IA pour produire des biens ou fournir des services dans les douze mois, deuxième trimestre de 2026 [13] | 19,2 % | 12,2 % |
| Union européenne | Entreprises de dix employés ou plus utilisant une technologie d'IA, 2025 [14] | 20,0 % | 13,5 % |
| États-Unis | Entreprises utilisant l'IA dans une fonction d'affaires, période close le 3 mai 2026 [15] | 19,8 % | Question modifiée en novembre 2025 |

Les trois chiffres convergent vers une entreprise sur cinq, mais ne mesurent pas la même chose : le champ, la période et la question diffèrent. L'écart selon la taille est net. Au Canada, 27,8 % des entreprises de cent employés ou plus utilisent l'IA, contre 19,9 % de celles d'un à quatre employés; aux États-Unis, la part atteint 37 % chez les entreprises d'au moins 250 employés [13][15]. Dans l'Union, elle va de 5,2 % en Roumanie à 42,0 % au Danemark [14]. Au Canada, la finance et les assurances arrivent au deuxième rang des secteurs, à 40,4 %, et 40,0 % des entreprises jugent l'IA sans pertinence pour elles [13].

Aucune de ces enquêtes ne compte les agents. Elles situent toutefois les chiffres des enquêtes privées : dans l'ensemble des entreprises, où une sur cinq utilise l'IA sous une forme quelconque, la part de celles qui exploitent des agents en production est nécessairement plus faible. Les parts de l'enquête McKinsey décrivent un autre champ, celui de ses répondants, des organisations plus grandes, et ne s'y comparent pas directement (chapitre 50).

---

## 4.2 L'écart entre pilote et production : ce que font vraiment les agents déployés

### L'étude MAP

La meilleure source sur les agents en production est une étude universitaire, « Measuring Agents in Production » (MAP), signée par vingt-cinq auteurs [1]. Elle combine vingt études de cas approfondies, quatorze en production et six en pilote, et un sondage de 306 réponses valides, dont 86 portent sur des systèmes déployés, dans 26 domaines. La technologie, la finance et les services aux entreprises dominent l'échantillon.

Le portrait qui en sort est celui d'agents volontairement simples.

| Dimension | Constat | Base |
|---|---|---|
| Autonomie | 68 % exécutent moins de dix étapes avant une intervention humaine (résumé : « au plus dix »); 47 % moins de cinq | Sondage |
| Parcours | 16 cas sur 20 suivent un workflow structuré et prédéfini; un seul explore librement, en bac à sable | Études de cas |
| Modèle | 17 cas sur 20 utilisent un modèle propriétaire; 14 sur 20 n'ajustent aucun poids | Études de cas |
| Destinataire | 92,5 % servent des humains, arrondis à 93 % : 52 % des employés et 40 % des clients externes; 8 % servent des systèmes non humains | Sondage |
| Latence | 66 % tolèrent une réponse en minutes ou plus | Sondage |
| Évaluation | 74 % reposent sur l'évaluation humaine; 52 % utilisent un modèle comme juge | Sondage |
| Outillage | 17 cas sur 20 sont construits sur mesure, sans cadriciel tiers | Études de cas |

Les figures relues portent sur 22 à 69 de ces 86 réponses, selon la question [1]. Comme 17 cas sur 20 dépendent d'un modèle propriétaire, la perte d'un fournisseur de modèles se prépare (chapitre 46). Et comme 14 cas sur 20 n'ajustent aucun poids, la distillation vers de petits modèles reste minoritaire dans la pratique observée (chapitre 47).

### Ce que ce portrait veut dire

**La production s'obtient en réduisant l'autonomie.** Les équipes qui livrent bornent le parcours et placent un humain tôt dans la boucle, sans attendre d'agent autonome sur une longue tâche. Le constat rejoint deux arbitrages que l'ouvrage détaille : où placer le non-déterminisme dans un processus (chapitre 17) et quelles décisions laisser à l'agent (chapitre 22).

**Le contrôle de qualité reste manuel.** Trois quarts des cas étudiés évaluent leur agent sans jeu de bancs d'essai, par tests comparatifs, retours d'utilisateurs et surveillance en production [1]. L'évaluation humaine ne suit pas le volume : elle plafonne le nombre d'agents qu'une équipe peut tenir en service. C'est l'un des verrous de la mise à l'échelle (chapitre 33).

**L'interopérabilité entre agents est encore un besoin plus qu'une pratique.** Dans le sondage, 8 % seulement des systèmes servent autre chose que des personnes, et la plupart des cas étudiés sont construits sur mesure, même si 61 % des répondants disent utiliser un cadriciel [1]. L'échantillon décrit donc des agents isolés, branchés sur les systèmes de leur organisation. Les protocoles de la partie II répondent à une étape que la plupart de ces équipes n'avaient pas encore franchie; les réseaux d'agents entre entreprises (chapitre 45), à une étape plus lointaine.

### Les limites de l'étude

Les auteurs les énoncent [1]. La collecte date d'avril à novembre 2025 : le portrait a un an. L'échantillon a été recruté de proche en proche et par réseaux professionnels, et les cas se concentrent dans les Amériques. Les résultats viennent d'entrevues et de questionnaires, non d'audits des systèmes. Les auteurs y voient un témoignage qualitatif sur une période, pas des taux de prévalence. Aucune étude comparable plus récente n'a été trouvée.

S'ajoute un biais de survie que l'étude ne peut pas corriger : elle renseigne sur la forme d'un agent qui survit, pas sur le nombre de ceux qui échouent.

---

## 4.3 Causes d'annulation : valeur floue, gouvernance, contrôles insuffisants

### Une prévision, pas un constat

Le chiffre le plus cité sur l'échec des projets vient de Gartner : plus de 40 % des projets d'IA agentique seraient annulés d'ici la fin de 2027. Le communiqué d'origine, de juin 2025, n'a pas pu être chargé [12]. La dépêche de Reuters qui en rend compte retient deux causes, la hausse des coûts et une valeur d'affaires floue [9]; selon des reprises du communiqué, Gartner en ajoute une troisième, des contrôles de risque insuffisants.

C'est une prévision, émise plus de seize mois avant ce chapitre, et aucun taux d'annulation observé n'a été trouvé. La même dépêche rapporte que Gartner prévoit aussi, pour 2028, qu'au moins 15 % des décisions de travail courantes seront prises de façon autonome par des agents et que le tiers des applications d'entreprise comprendra de l'IA agentique [9]. La firme annonce un tri, pas un reflux.

Selon l'analyste citée, la plupart des projets sont des expérimentations précoces, portées par l'engouement et souvent mal appliquées. Gartner dénonce aussi l'« agent washing », qui rebaptise agents des assistants et des robots conversationnels existants, et estime qu'environ 130 fournisseurs seulement, sur des milliers, offrent de véritables capacités agentiques [9].

### Ce que les données disent de chaque cause

La hausse des coûts, première cause citée, est traitée à la section 4.1. La gouvernance, examinée plus bas, est une cause que cet ouvrage ajoute à celles de Gartner.

**La valeur floue.** L'enquête McKinsey montre le mécanisme : des gains individuels déclarés, qui ne se rendent pas au résultat d'exploitation [8]. L'étude MAP en montre un autre. Parmi ses répondants, 39 % comparent leur agent à une solution non agentique, et 26 % disent qu'aucune base de comparaison valable n'existe [1]. Sans point de comparaison, la valeur ne se démontre pas, et un projet qui ne peut pas prouver son apport est le premier à perdre son budget (mesure de la valeur : chapitre 40).

**Les contrôles insuffisants.** Les praticiens de l'étude MAP désignent la fiabilité, soit un comportement correct et constant dans le temps, comme leur premier défi [1]. La taxonomie MAST précise où elle se perd dans les systèmes multi-agents : problèmes de spécification (41,77 % des échecs observés), désalignement entre agents (36,94 %) et vérification de la tâche (21,30 %) [2].

Ces parts viennent de la version 2 de l'article (avril 2025), qui analyse un peu plus de 200 tâches menées sur sept cadriciels à code ouvert et recense déjà quatorze modes d'échec. La version 3 (octobre 2025) étend le corpus à 1 642 traces; la somme de ses parts par mode donne environ 44 %, 32 % et 24 % (chapitre 21). Il s'agit de systèmes de recherche, pas de déploiements d'entreprise. Les auteurs vont toutefois au-delà : ils jugent que de nombreux échecs viennent de la conception du système et de l'organisation des agents, et conjecturent que l'amélioration des modèles ne suffira pas à les corriger tous [2].

Un autre chiffre de MAP donne la mesure de l'enjeu : 69 % des systèmes décrits lisent des données confidentielles, sur une trentaine de réponses à cette question [1]. Le contrôle d'accès n'est pas un raffinement tardif (chapitres 15 et 30).

**La gouvernance.** Ici, les données sont minces. Dans MAP, 38 % des praticiens placent la performance technique au premier rang de leurs priorités, contre 17 % pour la conformité et 3 % pour la gouvernance [1]. Il serait imprudent d'en conclure qu'elle compte peu : ces répondants construisent des systèmes déjà approuvés. La gouvernance agit plutôt en amont, comme condition d'entrée en production, et aucune des sources lues ne mesure son poids dans les annulations. Inventaire, cycle de vie et imputabilité : chapitre 39.

Les trois causes se ramènent à une seule exigence : pouvoir montrer ce que fait l'agent, ce qu'il rapporte et ce qui l'empêche de nuire. Un pilote peut s'en passer. Un système en production ne le peut pas.

---

## 4.4 Forces en présence : plateformes, standards, régulateurs

### Les plateformes

Les grands éditeurs se disputent le rôle de plan de contrôle des agents de l'entreprise, y compris de ceux qu'ils n'ont pas construits, au point de former une catégorie d'analyste. IBM annonce, dans un billet du 2 novembre 2026, figurer parmi les leaders du premier Magic Quadrant de Gartner consacré aux plateformes de gestion d'agents [7]. Le graphique, daté d'octobre 2026, situe treize éditeurs, dont Microsoft, ServiceNow, Amazon Web Services et Salesforce. IBM y présente watsonx Orchestrate comme un plan de contrôle agentique, capable de gérer des agents d'autres éditeurs.

Le rapport n'a pas été lu, et le classement des autres éditeurs n'est pas vérifié. Un point s'en dégage : la gestion d'agents est devenue une catégorie de produit où plusieurs éditeurs prétendent à la fois. Une organisation qui en utilise déjà plusieurs se retrouvera avec plusieurs plans de contrôle (chapitres 26 et 27; lecture des évaluations d'analystes : section 26.8).

### Les standards

Les protocoles ouverts ont un foyer commun : l'Agentic AI Foundation, qui héberge dix projets, dont MCP et A2A [6]; le chapitre 11 en décrit la gouvernance et les niveaux de maturité. Les deux protocoles centraux ont franchi un seuil en 2026 : A2A a publié sa version 1.0, présentée comme sa première spécification stable [3], et la révision `2026-07-28` de MCP, sans état, fait d'un serveur distant une charge HTTP ordinaire (chapitres 5 et 6).

Le socle existe donc. Ce qui l'entoure reste en chantier : le registre officiel de MCP est en préversion (chapitre 5), l'identité des agents n'a pas de profil adopté (chapitre 29), et les conventions d'observabilité d'OpenTelemetry restent au statut « Development » (chapitre 33).

### Les régulateurs

**En Europe, le calendrier a reculé.** Le règlement (UE) 2026/1744 du 8 juillet 2026, dit Digital Omnibus sur l'IA, modifie l'AI Act. D'après une reproduction non officielle du texte, il est en vigueur depuis le 27 juillet 2026, et les obligations visant les systèmes à haut risque de l'annexe III s'appliquent à compter du 2 décembre 2027; celles de l'annexe I, à compter du 2 août 2028 [10]. Le chapitre 35 en tire les conséquences pour les systèmes d'agents.

**Aux États-Unis, l'approche est volontaire.** L'AI Agent Standards Initiative du NIST, lancée en février 2026, repose sur trois piliers : des lignes directrices volontaires pour appuyer la normalisation menée par l'industrie, la réduction des obstacles à l'interopérabilité des protocoles communautaires, et la recherche sur l'authentification et l'identité des agents [5]. La page de l'initiative, mise à jour le 9 novembre 2026, ne mentionne aucun profil d'interopérabilité ni aucun livrable normatif publié; elle recense des consultations, dont un document de réflexion du NCCoE sur l'identité et l'autorisation des agents (chapitre 11).

**Au Canada et au Québec**, le cadre est traité au chapitre 38.

### Trois horloges

Les plateformes livrent au trimestre, les standards se stabilisent à l'année, les régulateurs comptent en années. Cet ordre crée la tentation de 2027. Une plateforme vend dès maintenant, sous forme propriétaire, la gouvernance que les standards ne fournissent pas encore. L'acheter règle le problème immédiat et crée une dépendance que les standards viendront, plus tard, rendre évitable.

---

## 4.5 Hypothèses de l'ouvrage pour l'horizon 2027

Chacune des six hypothèses de l'ouvrage repose sur ce qui précède et s'accompagne du signal qui l'infirmerait.

| Hypothèse | Fondement | Signal contraire |
|---|---|---|
| H1. La mise à l'échelle reste concentrée dans les grandes organisations | Écart de 40 % à 22 % [8] | Progression nette des plus petites dans la prochaine enquête |
| H2. Les agents en production restent bornés et supervisés; l'autonomie s'élargit par classe de décision | Étude MAP [1] pour l'état présent; l'élargissement est une projection de l'ouvrage | Étude comparable montrant des parcours longs sans intervention |
| H3. Le verrou est la conception du système, non le modèle | MAP et MAST [1][2] | Disparition des échecs de coordination avec une nouvelle génération de modèles |
| H4. MCP et A2A forment le socle; identité, registres et observabilité ne sont pas stabilisés | Chapitres 5, 6, 11 et 29 | Norme adoptée sur l'identité des agents |
| H5. Les grandes organisations vivront avec plusieurs plans de contrôle | Catégorie d'analyste, offres concurrentes [7] | Consolidation autour d'un seul éditeur ou d'un registre fédéré standard |
| H6. Un tri des projets aura lieu, sur la preuve de valeur et les contrôles | Prévision de Gartner [9], stagnation de l'effet sur les résultats [8] | Hausse marquée de la part des répondants qui voient un effet sur le résultat d'exploitation |

Ces hypothèses ne sont pas des prévisions chiffrées. Elles fixent le point de vue de l'ouvrage : celui d'une entreprise qui décide avant que les standards soient complets, avec des agents moins autonomes que ne le suggèrent les annonces. Le chapitre 43 les reprend pour bâtir ses scénarios.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Lire un chiffre d'adoption | Le classer : enquête déclarative, prévision ou indicateur de fournisseur [S] | Mesure indépendante, à méthode publiée |
| Portée d'un premier agent en production | Workflow prédéfini, peu d'étapes, supervision humaine [M] | Tâche réversible, en bac à sable |
| Preuve de valeur | Base de comparaison non agentique fixée avant le pilote [S] | Tâche nouvelle, sans équivalent : indicateur de résultat convenu d'avance |
| Passage du pilote à la production | Exiger évaluation, contrôle d'accès et imputabilité [S] | Aucun cas |
| Plan de contrôle | Retenir celui d'un éditeur déjà en place, avec clause de sortie [S] | Parc de plusieurs éditeurs : prévoir la fédération (chapitre 27) |
| Dépendance aux standards | Bâtir sur MCP et A2A; tenir le reste pour remplaçable [É] | Besoin immédiat d'identité ou de registre : solution transitoire documentée |
| Calendrier réglementaire | Planifier sur les échéances européennes de décembre 2027 et d'août 2028 [N] | Aucune activité visée par l'AI Act; institution financière fédérale canadienne : E-23, 1er mai 2027 (chapitre 38) |

---

## Points à retenir

- Dans l'enquête McKinsey de 2026, la part des grandes organisations qui mettent des agents à l'échelle dans au moins une fonction passe de 27 % à 40 %. Elle reste à 22 % chez les plus petites.
- L'effet sur les résultats ne suit pas : la part des répondants qui attribuent à l'IA une partie de leur résultat d'exploitation est stable, à 37 %.
- Les agents en production sont étroits : moins de dix étapes avant une intervention humaine pour la plupart, un parcours prédéfini, une évaluation par des personnes. Ce portrait date de 2025 et ne décrit que les projets qui ont abouti.
- Les « 40 % de projets annulés » sont une prévision de Gartner de juin 2025, non un constat. Aucun taux d'annulation observé n'a été trouvé.
- Les échecs documentés des systèmes multi-agents tiennent d'abord à la spécification et à la coordination. De meilleurs modèles ne les corrigeront pas seuls.
- Un revenu d'éditeur ou un nombre d'organisations qui appuient un protocole ne mesure pas l'usage en production.
- Les plateformes vendent déjà la gouvernance que les standards ne fournissent pas encore. C'est le principal arbitrage de 2027.
- Le report européen donne du temps, pas une dispense : les obligations sur le haut risque s'appliquent à partir de décembre 2027.
- Selon les offices statistiques du Canada, de l'Union européenne et des États-Unis, environ une entreprise sur cinq utilise l'IA. Aucun ne compte les agents.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Measuring Agents in Production (arXiv 2512.04123, version 4)](https://arxiv.org/abs/2512.04123) — première moitié du texte et extraits relus le 14 novembre 2026.
2. [Why Do Multi-Agent LLM Systems Fail? (arXiv 2503.13657)](https://arxiv.org/html/2503.13657v2) — résumé de la version 3, première partie de la version 2 et extraits relus le 14 novembre 2026.
3. [Linux Foundation — bilan de la première année d'A2A, 9 avril 2026](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)
4. [Salesforce — résultats du deuxième trimestre de l'exercice 2027](https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/)
5. [NIST — SI Agent Standards Initiative (anciennement CAISI)](https://www.nist.gov/super-intelligence/si-agent-standards-initiative)
6. [Agentic AI Foundation — projets](https://aaif.io/projects)
7. [IBM — annonce sur le Magic Quadrant 2026 des plateformes de gestion d'agents](https://www.ibm.com/new/announcements/ibm-named-a-leader-in-the-2026-gartner-magic-quadrant-for-ai-agent-management-platforms) — billet de fournisseur.

Sources secondaires lues :

8. [FM — Companies' financial value from AI holds firm in 2026, 1er septembre 2026](https://www.fm-magazine.com/news/2026/sep/companies-financial-value-from-ai-holds-firm-in-2026/) — compte rendu de l'enquête McKinsey.
9. [Reuters, repris par The Star — Over 40% of agentic AI projects will be scrapped by 2027, 25 juin 2025](https://www.thestar.com.my/tech/tech-news/2025/06/25/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says)
10. [AI Act Explorer — Digital Omnibus on AI](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/) — reproduction non officielle du règlement, lue en partie.

Pages non chargées :

11. [McKinsey — The State of AI in 2026](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) — délai dépassé (confirmé le 14 novembre 2026).
12. [Gartner — communiqué du 25 juin 2025](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) — accès refusé.

Statistiques officielles, pages lues le 14 novembre 2026 :

13. [Statistique Canada — Analysis on artificial intelligence use by businesses in Canada, second quarter of 2026 (11 juin 2026)](https://www150.statcan.gc.ca/n1/pub/11-621-m/11-621-m2026010-eng.htm)
14. [Eurostat — 20% of EU enterprises use AI technologies (11 décembre 2025)](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251211-2)
15. [U.S. Census Bureau — Large Firms With at Least 20 Employees Biggest AI Users (26 mai 2026)](https://census.gov/library/stories/2026/05/ai-use-businesses.html)

## Limites de ce chapitre

- Les sources [1] et [2], d'abord connues par leur seul résumé, ont été relues au-delà du résumé le 14 novembre 2026, par un outil qui en rend des extraits; les écarts relevés sont corrigés dans le texte.
- Le rapport de McKinsey n'a pu être chargé ni à la rédaction ni à l'audit du 14 novembre 2026 (délai dépassé). Ses chiffres viennent d'un compte rendu de presse, relu le 12 novembre 2026; l'échantillon et les dates de collecte et de publication restent inconnus.
- Le communiqué de Gartner [12] a encore retourné HTTP 403 à l'audit du 14 novembre 2026. La troisième cause d'annulation repose sur des reprises; la dépêche relue ne la mentionne pas. Le Magic Quadrant n'est connu que par le billet d'IBM.
- L'étude MAP a été relue à l'audit sur sa première moitié, par un outil qui condense les pages. Son résumé dit « au plus dix étapes » pour 68 % des agents, son corps « moins de dix ». Les parts MAST de la version 3 sont des sommes calculées au chapitre 21.
- Le Digital Omnibus a été lu sur un site non officiel; le chapitre 35 confirme le report des dates par les considérants publiés sur EUR-Lex.
- L'état du registre MCP, de l'identité des agents et des conventions d'observabilité est repris des chapitres 5, 29 et 33, sans relecture de leurs sources.
- La lecture du rôle de la gouvernance en 4.3, la tentation décrite en 4.4, les hypothèses de 4.5 et les conséquences tirées de MAP pour les chapitres 46 et 47 sont des interprétations, non des résultats.
- Les statistiques officielles de la section 4.1, lues le 14 novembre 2026 par l'outil d'extraction, portent sur l'IA en général et sur des champs différents. Leur rapprochement et la borne qu'il fixe à l'adoption des agents sont une lecture de ce chapitre.
- Aucun cas d'entreprise nommé n'est cité, faute de source primaire vérifiée (chapitre 42). La gouvernance est traitée plus brièvement que les autres causes, faute de données.
