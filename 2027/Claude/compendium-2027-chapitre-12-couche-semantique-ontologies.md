# Chapitre 12 — Couche sémantique et ontologies

*Question directrice : comment garantir que deux agents donnent le même sens au même terme ?*

> **Version 2 — 11 novembre 2026.** État de référence : dépôt `apache/ossie` (branche principale; spécification cœur et spécification d'ontologie en version `0.3.0.dev0`), page du projet à l'Apache Incubator, documentation du serveur MCP de dbt. Les numéros entre crochets renvoient aux sources en fin de chapitre : [1] à [11] sont des pages primaires lues pour ce chapitre, [12] et [13] des billets de fournisseurs lus et traités comme sources secondaires, [14] une source reprise de la carte thématique. Les renvois « chapitre N » pointent vers les chapitres du compendium. Chapitre audité et révisé le 12 novembre 2026.

Deux agents peuvent échanger un message parfaitement formé et ne pas parler de la même chose. L'agent des ventes demande le « revenu du trimestre » à l'agent des finances; l'un pense aux commandes signées, l'autre aux montants reconnus en comptabilité. Aucun protocole ne signale l'écart : le schéma est respecté, le chiffre est plausible, et il est faux pour celui qui le reçoit.

MCP et A2A confient le sens à des descriptions en langage naturel, interprétées par un modèle (chapitres 5 et 6). Ce choix a supprimé le coût d'accord préalable qui avait freiné les générations précédentes (chapitre 2). Il laisse à l'entreprise la charge de fixer son vocabulaire ailleurs.

La thèse de ce chapitre tient en une phrase : aucun mécanisme ne garantit à lui seul l'accord de sens; on s'en approche par trois étages. Une couche sémantique fixe les mesures. Une ontologie fixe les concepts et leurs relations. Un contrôle d'intention vérifie que les agents poursuivent le même but. Le premier étage est mûr, le deuxième est coûteux, le troisième relève encore de la recherche. Quant au standard censé rendre les deux premiers portables, Open Semantic Interchange, il est moins avancé que l'étiquette « v1.0 » sous laquelle il circule ne le laisse croire.

---

## 12.1 Pourquoi l'accord syntaxique ne suffit pas

### Ce que le schéma ne dit pas

Un schéma JSON déclare qu'un champ `revenue` est un nombre décimal. Il ne dit ni la devise, ni la période, ni si les remboursements sont déduits, ni quelle table fait autorité. Dans MCP, ces précisions tiennent dans la description de l'outil, c'est-à-dire dans une phrase (chapitre 3). Deux serveurs écrits par deux équipes porteront deux phrases, et le modèle fera de son mieux avec chacune.

L'erreur qui en résulte a une propriété gênante : elle est silencieuse. Une erreur de syntaxe produit un rejet. Une erreur de sens produit une réponse bien formée, que l'agent suivant reprend comme un fait. Dans une chaîne d'agents, l'écart se propage sans qu'aucun contrôle de protocole ne le voie.

### Trois objets à accorder

Le mot « sens » recouvre trois objets différents, qui n'appellent pas le même instrument.

| Objet | Question type | Instrument | Maturité |
|---|---|---|---|
| La mesure | Comment calcule-t-on le revenu net ? | Couche sémantique | Produits établis |
| Le concept | Qu'est-ce qu'un client actif, et que peut-on en déduire ? | Ontologie, graphe de connaissances | Technique ancienne, coûteuse à tenir |
| L'intention | Que cherche-t-on à accomplir avec ce chiffre ? | Contexte partagé, détection de conflits | Recherche |

### Ce que montrent les bancs d'essai

Laisser un modèle écrire du SQL sur un schéma brut revient à lui faire deviner la couche sémantique. Un banc d'essai de 2023 a mesuré le prix de cette devinette. Sur un schéma d'assurance et des questions d'entreprise allant du rapport à la métrique, GPT-4 interrogeant directement la base SQL, sans exemples, obtenait 16 % de bonnes réponses; les mêmes questions posées sur une représentation en graphe de connaissances, bâtie d'une ontologie et de correspondances, en obtenaient 54 % [11].

Deux précautions s'imposent. Ces chiffres viennent du résumé de l'article, datent de novembre 2023 et portent sur un modèle dépassé. Et 54 % n'est pas un résultat de production. La leçon durable est le sens de l'écart : un modèle répond mieux quand le vocabulaire d'affaires lui est donné que lorsqu'il doit le reconstruire à partir de noms de colonnes. Le chapitre 15 arrive au même constat avec Spider 2.0, banc d'essai de la fin de 2024 sur des schémas d'entreprise réels.

---

## 12.2 La couche sémantique : métriques et dimensions gouvernées

### Définition

Une couche sémantique associe la logique d'affaires aux données, pour que les métriques soient calculées de la même manière quel que soit l'outil qui les demande. La formule vient d'un éditeur de catalogues, qui résume la répartition des rôles ainsi : la couche sémantique fixe comment une mesure se calcule, l'ontologie fixe ce qu'un concept veut dire [13].

Le vocabulaire est stable d'un produit à l'autre, et la spécification cœur d'Apache Ossie en donne une forme neutre [3].

| Construction | Rôle |
|---|---|
| Jeu de données (`datasets`) | Entité logique, table de faits ou de dimension, rattachée à une source physique; porte ses clés |
| Champ (`fields`) | Attribut de ligne servant à grouper, filtrer ou calculer; peut être marqué comme dimension temporelle |
| Relation (`relationships`) | Jointure déclarée entre deux jeux de données, y compris par clés composées |
| Métrique (`metrics`) | Agrégation nommée, propre à un jeu de données ou transversale au modèle |
| Contexte pour l'IA (`ai_context`) | Consignes, synonymes et exemples destinés aux outils d'IA |

Un fragment illustratif, construit d'après la forme que décrit la spécification :

```yaml
name: sales_analytics
datasets:
  - name: orders
    source: sales.public.orders
    fields:
      - name: amount
        expression: { sql: amount }
        ai_context:
          synonyms: [montant, chiffre d'affaires]
metrics:
  - name: total_revenue
    expression: { sql: SUM(orders.amount) }
```

### Ce que l'agent y gagne

L'agent ne rédige plus la requête. Il nomme une métrique et des dimensions; la couche compile le SQL. Trois effets en découlent.

**Le calcul devient déterministe.** Deux agents qui demandent `total_revenue` par région obtiennent le même chiffre, parce que la jointure et l'agrégation ne dépendent plus de l'interprétation d'un modèle.

**La surface d'erreur rétrécit.** Le modèle choisit parmi des noms gouvernés au lieu de naviguer dans les colonnes d'un schéma brut.

**La définition devient auditable.** Elle est écrite une fois, versionnée, et l'on peut montrer quelle version a produit un chiffre.

### Ce qu'elle ne fait pas

La couche sémantique exécute des calculs prédéfinis; elle ne raisonne pas [13]. Elle sait calculer le revenu par client. Elle ne sait pas qu'un sous-traitant de second rang est une sorte de fournisseur, ni qu'un client sous sanction ne doit pas recevoir d'offre. Son plafond est la profondeur conceptuelle.

Elle ne règle pas non plus le désaccord entre deux couches. Une entreprise qui a défini « revenu » dans son outil d'intelligence d'affaires, dans son entrepôt et dans sa plateforme de vente a trois couches sémantiques, donc trois vérités. C'est le problème que vise le format d'échange décrit en 12.4.

---

## 12.3 Ontologies et graphes de connaissances

### Définition

Une ontologie décrit formellement les concepts d'un domaine, leurs relations et les contraintes qui les lient, sous une forme lisible par une machine. La définition classique, due à Tom Gruber, en fait la spécification explicite d'une conceptualisation [13]. Les standards associés sont ceux du web sémantique : RDF pour les énoncés, OWL pour la logique, SPARQL pour l'interrogation. Un graphe de connaissances est ce qu'on obtient quand on peuple une ontologie avec les entités réelles de l'entreprise.

Là où la couche sémantique répond à « combien », l'ontologie répond à « qu'est-ce que » et « qu'en découle-t-il ». Elle permet trois choses qu'un modèle dimensionnel n'exprime pas : la hiérarchie de concepts (un employé est une personne), l'identité (ce qui fait que deux enregistrements désignent le même client) et la règle (un client dont les achats dépassent un seuil appartient à une catégorie).

| Critère | Couche sémantique | Ontologie |
|---|---|---|
| Objet | Métriques et dimensions | Concepts, relations, règles |
| Origine | Intelligence d'affaires | Représentation des connaissances |
| Résultat | SQL gouverné, indicateurs constants | Graphe, déductions, modèle conceptuel |
| Raisonnement | Aucun | Inférence à partir de règles formelles |
| Standards | Définitions YAML et SQL; format d'échange en cours | RDF, OWL, SPARQL |
| Apport pour un agent | Accès déterministe aux chiffres | Compréhension du domaine |

Ce tableau condense la comparaison d'un éditeur [13]; il vaut comme cadrage, non comme résultat de recherche.

### L'argument en faveur des agents

RelationalAI, membre du groupe à l'origine d'Open Semantic Interchange, formule l'argument sans détour : les modèles dimensionnels servent l'analyse et le rapport, alors qu'un agent doit raisonner [12]. Son exemple est une question de chaîne d'approvisionnement : quelle est l'exposition de l'entreprise si un fournisseur de second rang s'arrête ? Répondre suppose de savoir ce qu'est un fournisseur de second rang, par quelles relations il se rattache aux produits, et quelles règles définissent l'exposition. Sans ontologie, l'agent redécouvre cette logique à chaque question, avec le coût en jetons et le risque d'incohérence que cela comporte.

L'argument est plausible, mais il vient d'un fournisseur de moteur de raisonnement, sans mesure à l'appui. La seule donnée chiffrée lue ici est celle du banc d'essai cité en 12.1 [11].

### Le coût, leçon déjà apprise

Les ontologies ne sont pas une nouveauté, et leur histoire avec les agents est instructive. Les systèmes multi-agents de l'ère FIPA, vers 1995-2005, exigeaient une ontologie partagée avant tout échange, et cette exigence a pesé sur leur adoption (chapitre 2). Rien n'indique que le coût de construction et d'entretien ait disparu. Ce qui a changé, c'est que l'ontologie n'est plus un préalable à la communication : les agents se comprennent approximativement sans elle. Elle devient un investissement ciblé, justifié là où l'approximation coûte cher.

Deux situations le justifient. La première est un domaine borné, à fort enjeu, où une erreur de catégorie a une conséquence réglementaire ou financière. La seconde est un secteur qui dispose déjà d'une ontologie de référence : la finance et la santé en ont [13], et l'industrie s'appuie sur ses propres modèles d'information, OPC UA et AAS (chapitre 28). Dans les deux cas, on réutilise avant de construire.

Entre entreprises, un espace de données partage un vocabulaire de politiques d'usage (ODRL), pas la sémantique commerciale (chapitre 45); l'accord sémantique y reste un obstacle (chapitre 37).

---

## 12.4 Open Semantic Interchange, devenu Apache Ossie

### Chronologie

Open Semantic Interchange (OSI) a été lancé en septembre 2025 par un groupe d'éditeurs et d'utilisateurs comprenant Snowflake, Salesforce, dbt Labs, BlackRock et RelationalAI, selon une source secondaire [13]. Les jalons suivants sont lus à la source.

| Date | Événement | Source |
|---|---|---|
| 11 décembre 2025 | Version `0.1.1` de la spécification cœur, qualifiée de version initiale | [3] |
| 27 janvier 2026 | Snowflake annonce que la première version est disponible, sous licence Apache 2.0; huit nouveaux membres, dont Databricks | [7] |
| 28 avril 2026 | Cinq groupes de travail ouverts; quatorze nouveaux participants, dont Oracle et Cloudera | [6] |
| 29 mai 2026 | Première version de développement de la spécification d'ontologie, `0.2.0.dev0` | [5] |
| 22 juin 2026 | Entrée à l'Apache Incubator sous le nom Apache Ossie | [2] |

Le dépôt vit désormais sous `apache/ossie` et se présente comme l'ancien OSI [1]. Le billet de janvier promettait une gouvernance neutre confiée à une fondation [7]; c'est chose faite, avec une réserve. Un projet en incubation n'a pas encore reçu l'aval complet de l'Apache Software Foundation, et la page du projet ne contient encore aucun rapport d'étape [2].

### « v1.0 » n'est pas un numéro de version

La table des matières de ce compendium, comme le billet d'Atlan, parle d'OSI « v1.0 » [13]; celui de Snowflake annonce une « première version » sans numéro [7]. L'historique des versions de la spécification ne contient aucune version 1.0 [3]. Il en liste deux : `0.1.1`, la version initiale, et `0.3.0.dev0`, en cours de développement, qui remplace une `0.2.0.dev0` jamais publiée. La section des publications du dépôt est vide [1]. La version en développement porte un avertissement sans équivoque : « Schema is mutable; do not depend on this version in production » [3].

Elle introduit d'ailleurs des ruptures : le champ d'extension change de nom, le tableau qui regroupait plusieurs modèles dans un document disparaît, et les références de métriques changent de cible. Un fichier conforme à la version de décembre 2025 n'est pas conforme à la branche principale de novembre 2026.

Il faut donc lire « v1.0 » comme une étiquette de communication désignant la première publication, et citer le numéro réel dans toute exigence contractuelle ou technique.

### Ce que couvre la spécification cœur

Un document Ossie, en YAML ou en JSON, décrit un seul modèle sémantique, avec les constructions présentées en 12.2 [3]. Quatre choix de conception méritent l'attention.

**Un SQL portable, et des dialectes opaques.** Une expression s'écrit d'abord dans un dialecte défini par la spécification, `OSSIE_SQL_2026`. Des variantes propres à un moteur peuvent l'accompagner, mais Ossie les traite comme opaques : une mise en œuvre peut les ignorer.

**Des extensions déclarées non portables.** Le champ `nonportable_extensions` accueille des données propres à un fournisseur. La sémantique cœur ne doit pas en dépendre, et un consommateur doit conserver celles qu'il ne comprend pas. Le nom dit l'essentiel : tout ce qui s'y loge reste captif.

**Un contexte pour l'IA.** Le champ `ai_context` reçoit des consignes, des synonymes et des exemples de questions. L'historique des versions le décrit comme un contexte pour agents. C'est le seul point où la spécification évoque les agents.

**Pas d'interface d'interrogation.** La spécification décrit des définitions, pas la manière de les interroger. Dans la version courante, une métrique ne peut pas en référencer une autre, et un champ ne peut pas en référencer un autre. Le contrôle d'accès n'y figure pas.

Le dépôt fournit, autour du texte, un SDK Python, des outils de validation, un évaluateur de portabilité et des convertisseurs de référence vers dbt, GoodData, Polaris et Salesforce [1].

### La spécification d'ontologie

L'« extension ontologique » annoncée par RelationalAI le 29 mai 2026 [12] est, dans le dépôt, un document distinct, au même numéro de version de développement [5]. Ses constructions sont peu nombreuses.

| Construction | Ce qu'elle exprime |
|---|---|
| `concept`, de type `EntityType` ou `ValueType` | Une entité d'affaires ou un type de valeur |
| `extends` | La spécialisation : un concept en étend un autre |
| `identify_by` | Les relations qui identifient une entité |
| `relationships`, avec rôles et `multiplicity` | Les liens entre concepts et leur cardinalité |
| `derived_by` | Une règle de dérivation, que la spécification compare à une vue |
| `requires` | Une contrainte sur la population d'un concept ou d'une relation |
| `iri` et `prefixes` | Le rattachement à un vocabulaire externe |

L'exemple de la spécification donne le ton :

```yaml
name: EnterpriseOntology
ontology:
  - concept: SocialSecurityNr
    type: ValueType
    extends: [Integer]
  - concept: Employee
    type: EntityType
    extends: [Person]
```

Le lien avec les données passe par des documents de correspondance séparés. Chacun relie une ontologie à un modèle sémantique et indique, par des expressions SQL sur les champs, comment peupler concepts et relations. L'ancienne forme, où les correspondances étaient incluses dans l'ontologie, est dépréciée. La spécification précise que l'analyseur et les convertisseurs ne prennent pas encore en charge les documents de correspondance autonomes [5].

Trois constats cadrent les attentes. Le document ne décrit aucun moteur d'inférence : règles et contraintes sont des définitions qu'un outil peut évaluer, pas un raisonnement garanti. Il ne remplace pas les standards du web sémantique, mais permet d'y renvoyer par des IRI; ses exemples pointent vers des vocabulaires publics existants. Enfin, il est plus jeune et moins outillé que la spécification cœur.

### La feuille de route

La feuille de route du dépôt ne donne ni date ni version cible, et ne mentionne aucune version 1.0 [4]. Elle distingue les travaux en cours (sémantique des métriques, intégration aux catalogues, ontologie) des travaux futurs. Parmi ces derniers figurent trois éléments qui manquent aujourd'hui à un usage agentique : un langage d'interrogation sémantique avec un moteur de référence et une suite de tests de conformité, une couche sémantique « native IA » comprenant des requêtes vérifiées et le contrôle de ce qui est exposé à l'IA, et des identifiants stables assortis de normes de validation.

Ossie est donc, à ce jour, un format d'échange de définitions entre outils, muet sur la manière dont un agent les découvre ou les interroge à l'exécution. Sa valeur : écrire une définition une fois et la porter d'un outil à l'autre.

---

## 12.5 Exposer la sémantique aux agents

Une définition gouvernée ne sert à rien si l'agent ne la consulte pas. Faute d'interface standard, l'exposition passe par les produits, le plus souvent par MCP.

### Trois modes d'exposition

| Mode | Ce que fait l'agent | Risque principal |
|---|---|---|
| Outils sémantiques | Liste les métriques, choisit des dimensions, lance la requête | Catalogue trop vaste, noms ambigus |
| Contexte injecté | Lit définitions, synonymes et exemples, puis agit | Coût en jetons, contexte périmé |
| SQL libre | Rédige et exécute sa propre requête | Jointure ou agrégation fausse, sans signal |

Le serveur MCP de dbt illustre le premier mode [8][9]. Ses outils de couche sémantique forment une séquence : `list_metrics` énumère les métriques définies, `get_dimensions` et `get_entities` donnent ce par quoi on peut les découper, `get_dimension_values` les valeurs possibles, `query_metrics` exécute la requête avec filtres et regroupements. Un outil mérite d'être signalé : `get_metrics_compiled_sql` renvoie le SQL compilé sans l'exécuter. Il permet de consigner, pour chaque chiffre, la requête exacte qui l'a produit.

Le même serveur offre le troisième mode, par `text_to_sql` et `execute_sql`. La documentation traite le premier de ces outils à part : c'est le seul que la désactivation des fonctions d'IA par un administrateur fait disparaître [9]. Les serveurs gérés des grandes plateformes de données suivent une répartition comparable entre analyse sur vues sémantiques et exécution de SQL (chapitre 15).

Le deuxième mode repose sur les champs `ai_context` décrits en 12.4, ou sur leurs équivalents propres à chaque produit. Il relève de l'ingénierie du contexte : que charger, quand, et à quel coût (chapitre 13).

### Règles de conception

Cinq règles se dégagent. Ce sont des propositions de ce chapitre : les trois premières s'appuient sur la documentation lue, les deux dernières sur les chapitres voisins.

1. **Découvrir avant d'interroger.** L'agent consulte la liste des métriques et leurs dimensions avant toute requête. Une métrique absente du catalogue donne lieu à une demande de clarification, non à une improvisation en SQL.
2. **Garder la requête compilée.** Le SQL produit par la couche sémantique entre dans la piste d'audit avec la version du modèle.
3. **Stabiliser les noms.** La documentation de dbt indique que l'éditeur évite de renommer ou de retirer des outils, parce que des clients s'en servent dans leurs listes d'autorisation, et recommande d'épingler une version du serveur autohébergé pour obtenir un jeu d'outils figé [9]. La même discipline vaut pour les noms de métriques : les renommer rompt silencieusement les agents qui les ont appris.
4. **Borner le SQL libre.** Lecture seule, périmètre restreint, permissions de l'utilisateur appelant (chapitre 15).
5. **Traiter les descriptions comme une surface d'attaque.** Synonymes, consignes et exemples sont du texte injecté dans le contexte du modèle (chapitre 31). Leur modification passe par la même revue que le code.

### Une limite à garder en vue

Rien de tout cela n'est standardisé au niveau sémantique. MCP transporte l'appel; il ne dit pas qu'une métrique s'appelle une métrique. Deux serveurs de deux éditeurs exposent deux jeux d'outils différents pour le même besoin. Un format d'échange commun réduirait l'écart en amont, puisque les deux serveurs liraient les mêmes définitions. L'interface d'interrogation commune, elle, n'est qu'un projet de la feuille de route d'Ossie [4].

---

## 12.6 Divergence d'intention : le pont vers l'orchestration

### Le même mot, le même calcul, deux buts

Supposons le vocabulaire fixé : les deux agents partagent la définition du revenu et celle du client actif. Ils peuvent encore diverger sur ce qu'ils cherchent à faire. L'un optimise le délai de traitement d'une réclamation, l'autre la conformité du dossier; chacun agit correctement selon sa lecture de l'objectif commun, et le résultat d'ensemble est incohérent.

Dans sa version 2, la taxonomie MAST range 36,94 % des échecs multi-agents observés dans le désalignement entre agents [14]; la version 3 ramène cette part à environ 32 % (chapitre 21). Une prépublication de mars 2026 donne un nom au phénomène, la divergence d'intention sémantique, et y voit une cause première de ces échecs [10].

### Le cadre de consensus sémantique

Cette prépublication propose un intergiciel à six composants, qui couvrent le contexte partagé, la représentation de l'intention, la détection des conflits, leur résolution, le suivi de la dérive et la gouvernance [10]. D'après le résumé, l'idée est de représenter explicitement l'intention de chaque agent et de la confronter au contexte du processus d'affaires.

Le résumé rapporte une évaluation de 600 exécutions sur trois cadriciels et quatre scénarios d'entreprise. Le cadre y atteint 100 % de complétion des workflows, contre 25,1 % pour la meilleure solution de comparaison. Il détecte 65,2 % des conflits sémantiques, avec une précision de 27,9 %. L'auteur le présente comme indépendant du protocole et compatible avec MCP et A2A.

Ces résultats appellent une lecture prudente. La prépublication a un seul auteur et n'a pas été évaluée par les pairs. Selon le chapitre 21, qui en a lu le texte, les 600 exécutions sont simulées, sans vrais appels de modèle, et l'agent juge de comparaison atteint 93,2 % de précision. Une précision de 27,9 % signifie que près de trois alertes sur quatre sont fausses; à ce taux, un point de contrôle humain branché sur le détecteur serait vite ignoré (chapitre 22).

### Ce qu'on peut en retenir

Au niveau des buts, aucun instrument n'est mûr. Trois pratiques simples tiennent lieu de consensus. L'intention s'écrit dans le message de délégation, avec les critères de réussite et les arbitrages attendus (chapitre 13). L'agent qui reçoit une tâche ambiguë demande une clarification au lieu de trancher seul. Et un contrôle indépendant vérifie le résultat par rapport à l'objectif, pas seulement par rapport au format. Le chapitre 21 développe ces remèdes.

La couche sémantique y contribue indirectement. Un modèle de processus et un vocabulaire partagés donnent aux déclarations d'intention un référentiel commun; sans eux, deux intentions exprimées dans deux vocabulaires ne sont même pas comparables.

---

## 12.7 Gouverner le vocabulaire d'entreprise

Aucun instrument ne fonctionne sans réponse à une question de fond : qui décide de ce que veut dire un terme ?

### Le vocabulaire comme code

Un modèle sémantique est un fichier texte. Il se versionne, se révise et se valide comme du code, et l'outillage existe : schémas, validateurs, SDK [1]. Cette pratique donne trois garanties qu'un glossaire dans un document partagé ne donne pas : un historique des changements, une revue avant publication et la possibilité de tests automatiques.

Les tests comptent le plus dans un contexte agentique. Un jeu de questions de référence, avec la métrique et les dimensions attendues pour chacune, se rejoue à chaque changement du modèle sémantique et à chaque changement de modèle de langage, y compris pour chaque modèle qu'un routeur peut choisir (chapitre 44) ou un petit modèle distillé (chapitre 47). C'est la seule façon de détecter qu'un synonyme ajouté pour un agent en égare un autre.

### Rôles

| Rôle | Responsabilité |
|---|---|
| Propriétaire d'un terme | Tranche la définition; répond de sa justesse |
| Intendant du modèle sémantique | Tient le fichier, applique la revue, publie les versions |
| Équipe d'agents | Signale les ambiguïtés rencontrées en exploitation; propose synonymes et exemples |
| Architecture d'entreprise | Arbitre entre domaines quand un terme a deux propriétaires |

Le dernier cas est le plus fréquent et le plus politique. Quand les ventes et les finances définissent le revenu différemment, la solution n'est pas d'en choisir une. Elle consiste à nommer deux métriques distinctes, à documenter leur écart, et à retirer le terme nu du catalogue exposé aux agents.

### Un ordre de travail

Commencer par les métriques contestées, celles dont deux tableaux de bord donnent deux valeurs. Elles sont peu nombreuses, leur coût d'ambiguïté est connu, et la couche sémantique suffit.

Ajouter ensuite une ontologie pour un domaine borné où les agents doivent classer ou déduire, en partant d'un vocabulaire sectoriel quand il en existe un.

Formaliser enfin les règles. Les politiques d'entreprise vivent dans des documents et des usages; tant qu'elles n'ont pas été converties en définitions lisibles par machine, aucun format n'y change rien (chapitres 13 et 39).

### Portabilité et dépendance

Le format d'échange est une assurance contre le verrouillage, à condition de le lire correctement. Trois vérifications s'imposent avant de s'y fier : la version exacte que le produit lit et écrit; la part des définitions logée dans les extensions non portables; le sort des expressions écrites dans un dialecte propre au moteur. Une clause d'exportation dans un format ouvert, avec numéro de version, a sa place dans les contrats (chapitre 27).

Ce que le format ne porte pas reste à gouverner ailleurs. Le contrôle d'accès aux métriques n'est pas dans la spécification [3]; il relève des données et de l'autorisation (chapitres 15 et 30).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Accès des agents aux chiffres | Outils de couche sémantique : métriques et dimensions nommées | Exploration ponctuelle par un analyste : SQL libre en lecture seule |
| Définition des métriques | Une couche sémantique unique par domaine, versionnée comme du code | Deux définitions légitimes : deux métriques nommées, jamais un terme nu |
| Ontologie | Aucune au départ | Domaine borné à fort enjeu, ou ontologie sectorielle déjà disponible |
| Format d'échange | Suivre Apache Ossie; exiger l'import et l'export avec numéro de version | Parc à un seul outil : le format natif suffit |
| Version d'Ossie | Ne rien bâtir en production sur `0.3.0.dev0` | Prototype dont la réécriture est prévue |
| Spécification d'ontologie d'Ossie | Veille | Projet pilote avec un fournisseur membre du groupe de travail |
| Extensions de fournisseur | Minimales et inventoriées | Fonction sans équivalent portable, avec plan de sortie |
| Synonymes et consignes pour l'IA | Soumis à la même revue que le code | — |
| Contrôle d'intention | Intention écrite dans la délégation, clarification, vérification indépendante | Intergiciel de consensus : expérimentation seulement |
| Traçabilité d'un chiffre | Requête compilée et version du modèle consignées | — |

---

## Points à retenir

- Les protocoles transportent des mots; ils n'en fixent pas le sens. Une erreur sémantique ne produit pas de rejet, mais un résultat plausible et faux.
- Trois objets sont à accorder : la mesure, le concept et l'intention. Chacun a son instrument et son degré de maturité.
- La couche sémantique rend le calcul déterministe : l'agent nomme une métrique, la couche compile la requête. C'est l'étage le plus rentable et le plus mûr.
- L'ontologie ajoute hiérarchies, identité et règles. Son coût reste élevé; elle se justifie dans un domaine borné à fort enjeu.
- Open Semantic Interchange est devenu Apache Ossie, entré en incubation le 22 juin 2026. Il n'existe pas de version 1.0 : la seule version parue est la `0.1.1` de décembre 2025, et la branche en développement se déclare impropre à la production.
- La spécification d'ontologie d'Ossie est un document distinct, plus jeune, sans moteur d'inférence défini, et dont l'outillage de correspondance n'est pas terminé.
- Ossie est un format d'échange de définitions, pas une interface d'exécution. L'exposition aux agents passe aujourd'hui par des serveurs MCP propres à chaque éditeur.
- La divergence d'intention subsiste quand le vocabulaire est partagé. Le seul remède instrumenté lu pour ce chapitre est une prépublication, évaluée en simulation, dont le détecteur a une précision de 27,9 %.
- Le vocabulaire se gouverne comme du code : un propriétaire par terme, des versions, une revue, des jeux d'essai rejoués à chaque changement.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Apache Ossie — dépôt et README](https://github.com/apache/ossie)
2. [Apache Incubator — page du projet Ossie](https://incubator.apache.org/projects/ossie.html)
3. [Apache Ossie — spécification cœur, version 0.3.0.dev0](https://raw.githubusercontent.com/apache/ossie/main/core-spec/spec.md)
4. [Apache Ossie — feuille de route](https://raw.githubusercontent.com/apache/ossie/main/ROADMAP.md)
5. [Apache Ossie — spécification d'ontologie, version 0.3.0.dev0](https://raw.githubusercontent.com/apache/ossie/main/ontology/ontology.md)
6. [Apache Ossie — point communautaire du 28 avril 2026](https://ossie.apache.org/updates/osi-april-2026-community-update/)
7. [Snowflake — billet du 27 janvier 2026 sur la première version d'OSI](https://www.snowflake.com/en/blog/open-semantic-interchanges-specs-finalized/)
8. [dbt — à propos du serveur MCP](https://docs.getdbt.com/docs/dbt-ai/about-mcp)
9. [dbt — outils du serveur MCP](https://docs.getdbt.com/docs/dbt-ai/mcp-available-tools)
10. [Semantic Consensus: Process-Aware Conflict Detection and Resolution for Enterprise Multi-Agent LLM Systems (arXiv 2604.16339)](https://arxiv.org/abs/2604.16339) — résumé seulement; le texte est lu au chapitre 21.
11. [A Benchmark to Understand the Role of Knowledge Graphs on LLM's Accuracy for Question Answering on Enterprise SQL Databases (arXiv 2311.07509)](https://arxiv.org/abs/2311.07509) — résumé seulement.

Billets de fournisseurs lus, traités comme sources secondaires :

12. [RelationalAI — sémantique ontologique dans OSI, 29 mai 2026](https://www.relational.ai/post/bringing-ontological-semantics-to-open-semantic-interchange-osi)
13. [Atlan — ontologie et couche sémantique, mise à jour du 9 octobre 2026](https://atlan.com/know/ontology-vs-semantic-layer/)

Source reprise de la carte thématique, non relue pour ce chapitre :

14. [Why Do Multi-Agent LLM Systems Fail? — MAST (arXiv 2503.13657)](https://arxiv.org/html/2503.13657v2)

## Limites de ce chapitre

- L'intitulé de la section 12.4 a été modifié. La table des matières et la carte thématique annoncent « Open Semantic Interchange v1.0 et son extension ontologique »; le dépôt ne contient aucune version 1.0, et le projet a changé de nom. Aucun autre chapitre ne reprend l'étiquette « v1.0 ».
- Les pages ont été lues par un outil d'extraction qui condense le texte, y compris à l'audit du 12 novembre 2026. Celui-ci a relu [2] à [7], [10] et [11], qui confirment dates, versions, avertissement de production, constructions de l'ontologie, feuille de route et chiffres des résumés. Noms de champs et fragments YAML restent à vérifier dans le dépôt; le fragment de la section 12.2 est une illustration, non un extrait.
- Le README [1], source de la liste des convertisseurs, et la documentation de dbt [8][9] n'ont pas été relus à l'audit. Le point communautaire d'avril renvoie à un dépôt distinct, `apache/ossie-converters`.
- La date de lancement d'OSI et la liste de ses fondateurs viennent d'Atlan [13]. Le point communautaire daté du 28 avril cite l'ancien dépôt, mais ses liens mènent au nouveau et il se dit en incubation, signe d'une mise à jour postérieure; la date du transfert n'a pas été établie.
- Les définitions de RDF, d'OWL, de SPARQL et du graphe de connaissances, ainsi que le rappel des ontologies dans les systèmes multi-agents classiques, viennent de la connaissance générale et du chapitre 2, non d'une page du W3C lue pour ce chapitre. SHACL n'a pas été examiné.
- Aucun produit d'ontologie d'entreprise n'a été étudié à la source. Les ontologies proposées par les plateformes de données et les vues sémantiques de Snowflake ne sont connues que par Atlan ou par le chapitre 15.
- Les deux articles [10] et [11] ne sont connus ici que par leur résumé; le caractère simulé de l'évaluation de [10] est repris du chapitre 21. La part de 36,94 % (MAST, version 2 [14], non relue) concorde avec les chapitres 3, 4 et 21; celle d'environ 32 % est une somme calculée au chapitre 21. Le banc d'essai [11] date de 2023; aucune mesure récente et indépendante du gain apporté par une couche sémantique ou une ontologie n'a été lue.
- Les chiffres d'Atlan (délais de mise en œuvre, gains de précision, prévisions d'analystes) ont été écartés, faute de source primaire lue.
- Les règles de conception de la section 12.5, les rôles et l'ordre de travail de la section 12.7 sont des propositions de ce chapitre, non des résultats tirés d'une source.
