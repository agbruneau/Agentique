# Chapitre 15 — Données prêtes pour les agents

*Question directrice : les données de l'entreprise sont-elles utilisables par un agent ?*

> **État de référence :** spécification MCP `2026-07-28`, documentation des éditeurs au 11 novembre 2026, et cinq bancs d'essai parus entre novembre 2024 et octobre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre. La documentation d'un éditeur établit ce qu'un produit déclare faire, non ce qu'il fait en production.

Un protocole règle la manière d'appeler un système. Il ne dit rien de ce que ce système contient. Un agent correctement branché sur un entrepôt mal décrit, périmé ou trop largement ouvert produit des réponses fausses avec la même assurance que des réponses justes, et il les produit plus vite qu'un analyste.

Ce chapitre défend une thèse en deux temps. D'abord, une donnée est prête pour un agent quand quatre conditions sont réunies : elle se trouve et se comprend sans son auteur, son état est connu au moment de la lecture, elle est lue sous l'identité de la personne qui demande, et elle est exposée par une interface à la mesure de ce qu'un modèle sait manipuler. Ensuite, aucune de ces conditions ne peut être confiée au modèle : les bancs d'essai montrent que les agents trouvent la bonne source plus souvent qu'ils ne savent la combiner à une autre, et qu'ils ne protègent pas d'eux-mêmes une information confidentielle.

---

## 15.1 Qualité et fraîcheur

### Ce qu'un agent ne remarque pas

Un analyste qui voit un chiffre d'affaires négatif ou deux fiches pour le même client s'arrête. Un agent poursuit. La qualité des données cesse alors d'être un irritant pour devenir un facteur de justesse.

Une équipe de Berkeley a étudié pendant environ deux mois six entreprises, dans six secteurs, qui construisent des agents de données en production [5]. Elle en tire quatre propriétés des charges de travail réelles, absentes des bancs d'essai usuels :

1. **L'intégration de plusieurs bases.** La réponse exige de croiser des systèmes de gestion de bases de données différents.
2. **Des clés de jointure mal formées.** Le même identifiant s'écrit différemment d'un système à l'autre.
3. **La transformation de texte non structuré.** L'information utile est enfouie dans un champ de texte libre.
4. **La connaissance du domaine.** La question suppose des règles que les données ne contiennent pas.

Ces quatre propriétés sont une bonne liste de contrôle : chacune désigne un défaut que l'entreprise peut corriger en amont, par des clés harmonisées, des champs extraits et des définitions publiées.

### La fraîcheur est une information, pas une garantie

Un agent doit savoir de quand date ce qu'il lit. Le protocole MCP offre trois appuis (chapitre 5 pour le reste du protocole).

Le premier est l'annotation `lastModified`, un horodatage facultatif qu'un serveur peut attacher à une ressource [1]. Le deuxième est le champ `ttlMs`, obligatoire sur toute lecture de ressource, qui indique pendant combien de temps le client peut tenir le résultat pour frais [2]. Le troisième est l'abonnement : depuis la révision de juillet 2026, le client ouvre un flux `subscriptions/listen` pour les ressources qu'il suit et reçoit `notifications/resources/updated` à chaque changement [1].

La spécification précise toutefois que `ttlMs` est un indice de fraîcheur et non une garantie : le serveur peut changer la donnée avant son expiration [2]. Aucun de ces mécanismes ne dit si la donnée de fond est à jour par rapport à ce qui était promis : un serveur peut servir fidèlement, avec un `ttlMs` court et un `lastModified` exact, une table que le pipeline n'a pas rafraîchie depuis trois jours.

### Écrire la promesse

Pour que la fraîcheur de fond soit connue, il faut qu'elle soit promise quelque part sous une forme lisible par une machine. C'est l'objet du contrat de données. L'Open Data Contract Standard (ODCS), maintenu par le projet Bitol, en est à la version 3.2.0 [9]. Il définit le contrat comme l'entente entre un producteur de données et ses consommateurs.

Sa section sur les niveaux de service intéresse directement un agent : chaque engagement s'y exprime par une propriété et une valeur, assorties d'une unité au besoin, et les propriétés nommées comprennent la latence, la fréquence de mise à jour, la rétention et la disponibilité [9].

Le standard ne mentionne pas les agents. La proposition suivante est donc celle de ce chapitre : exposer à l'agent, avec la donnée, la latence promise et l'heure de la dernière mise à jour, et lui faire dire l'âge de ce qu'il rapporte. Un outil peut aussi refuser de répondre quand l'engagement n'est pas tenu. Quand c'est un agent qui produit la donnée, le même contrat devient le critère d'un audit avant publication (chapitre 47).

---

## 15.2 Catalogues, lignage et registre de données

### Un registre de données, pendant du registre d'agents

Avant de lire une donnée, un agent doit la trouver. Une architecture proposée par Megagon Labs pour les systèmes d'IA composés traite ce besoin par symétrie : à côté du registre d'agents, elle place un **registre de données**, qui conserve les métadonnées des données de l'entreprise (noms, descriptions, schémas, détails de connexion) et en permet la recherche [4]. Un planificateur de données traduit ensuite une demande en langage naturel en plan de requête. L'architecture de référence du chapitre 23 reprend ce couple.

La portée de cette source est limitée : c'est une prépublication d'avril 2025, dont la plupart des composants sont décrits au niveau du concept, sans évaluation chiffrée [4].

### Le catalogue comme point de gouvernance

En pratique, le registre de données d'une entreprise est son catalogue. L'évolution notable de 2026 est que le catalogue ne décrit plus seulement des tables : il gouverne aussi les points d'accès des agents. Chez Databricks, chaque serveur MCP géré de l'espace `system.ai` est un objet sécurisable du catalogue; les droits d'invocation s'accordent par des octrois, et chaque appel peut être soumis à des politiques [13]. Les points d'accès propres à l'espace de travail (Genie par espace, ancien point d'accès SQL), en préversion publique, échappent toutefois à ces octrois et politiques [13]. Chez Snowflake, le serveur MCP est un objet doté de ses propres privilèges, et l'accès au serveur ne donne pas accès aux outils : chaque outil exige son propre octroi [12].

L'inventaire des données, l'inventaire des outils et les droits qui s'y rattachent tendent ainsi à loger au même endroit, ce qui simplifie l'audit, mais lie la gouvernance des agents à la plateforme de données choisie (chapitres 8 et 27).

### Le lignage

Savoir d'où vient une donnée sert à deux choses pour un agent : juger s'il peut s'y fier, et permettre à un humain de remonter d'une réponse à sa source.

OpenLineage répond au premier besoin par un standard ouvert. Projet de niveau « Graduate » de la LF AI & Data Foundation, il modélise le lignage par trois entités, le jeu de données, la tâche et l'exécution, enrichies de facettes; parmi celles d'un jeu de données figurent le schéma, le lignage au niveau de la colonne, la propriété et les assertions de qualité [10].

Rien dans les pages lues ne relie OpenLineage aux agents. Le lien est une inférence : si ces métadonnées sont déjà émises sous une forme normalisée, un catalogue peut les présenter à l'agent, et un outil peut refuser une table dont la dernière exécution a échoué.

Le second besoin relève de la provenance du contexte (chapitre 13) et de l'observabilité (chapitre 33). Le journal d'audit de Microsoft Copilot en montre la forme minimale : il consigne, pour chaque interaction, qui a interrogé l'assistant, quand, et quelles ressources ont servi à produire la réponse [17].

---

## 15.3 Contrôle d'accès hérité de l'utilisateur

### Deux identités possibles

Quand un agent interroge un entrepôt, la requête s'exécute sous une identité. Il n'y en a que deux possibles : celle de l'agent ou celle de la personne qui a posé la question. La documentation des deux grandes plateformes de données décrit ce choix dans des termes presque identiques [11][14].

| | Identité de service | Identité de l'utilisateur |
|---|---|---|
| Qui interroge | L'application ou l'agent, sous un compte de service | L'utilisateur final, authentifié par OAuth |
| Convient quand | Tous les utilisateurs ont le même accès, ou n'ont pas de compte dans la plateforme | Les droits varient par personne; la piste d'audit doit être nominative |
| Risque propre | L'agent devient un compte à privilèges; le filtrage repose sur le code de l'application | Repli silencieux sur le compte de service; composants qui ignorent l'identité |

L'héritage des droits de l'utilisateur a un avantage décisif : les politiques existantes s'appliquent sans être réécrites. Selon Snowflake, les politiques d'accès aux lignes et de masquage s'appliquent sans configuration supplémentaire quand l'agent passe par le serveur MCP géré [11].

Dans le modèle à identité de service, tout dépend de l'application. Snowflake recommande alors que chaque politique échoue en mode fermé : un attribut de session manquant doit renvoyer zéro ligne, et non toutes les lignes [11].

### Un plafond, non une cible

Hériter des droits de l'utilisateur ne signifie pas donner à l'agent tous ces droits. Databricks restreint le jeton de l'utilisateur aux seules portées d'API que l'auteur de l'agent a déclarées [14]. Les droits de la personne fixent un plafond; ceux de la tâche fixent ce qui est réellement accordé (chapitre 30).

Le transport de l'identité jusqu'à la donnée pose un problème distinct : MCP interdit à un serveur de relayer en aval le jeton qu'il a reçu, et il faut donc un échange de jeton pour atteindre le système derrière le serveur (chapitres 5 et 29). Entre organisations, l'accès relève d'un autre mécanisme : le connecteur du fournisseur produit son catalogue selon les justificatifs présentés et conclut un accord régi par une politique (chapitre 45).

### Cinq endroits où l'héritage se rompt

La documentation des éditeurs est franche sur les cas où le modèle ne tient pas. Ils méritent d'être testés un à un.

**Le repli silencieux.** Chez Databricks, si le jeton transmis est absent, la fonction qui construit le client de l'utilisateur se rabat sur le principal de service sans lever d'erreur [14].

**Les composants à droits du propriétaire.** Chez Snowflake, les services de recherche Cortex Search interrogent avec les droits de leur propriétaire : tout rôle autorisé à interroger un service voit tout ce qu'il a indexé [11].

**L'outil qui contourne l'agent.** Snowflake recommande de n'exposer qu'un agent Cortex sur un serveur destiné aux questions d'affaires gouvernées : l'outil d'exécution de SQL, placé à côté, permettrait de contourner les vues sémantiques et les requêtes vérifiées de l'agent. Le SQL direct va sur un serveur distinct, sous un rôle au moindre privilège, et les serveurs se découpent selon les frontières d'accès et les publics [11][12].

**Le cache partagé.** Dans MCP, une réponse marquée `private` ne doit pas être partagée entre contextes d'autorisation, et le serveur ne doit pas compter sur ce marquage pour empêcher un accès [2].

**L'absence qui ressemble à un refus.** Une ligne masquée par une politique est invisible pour l'agent, qui conclut qu'elle n'existe pas. Snowflake suggère de demander à l'agent d'énoncer que ses résultats ne couvrent que les données visibles par l'utilisateur [11]. C'est une consigne de prompt, donc une atténuation et non un contrôle.

---

## 15.4 Exposition : entrepôts, API, flux d'événements

Une donnée gouvernée doit encore être présentée à l'agent. Cinq modes coexistent : le SQL libre sur l'entrepôt, l'outil paramétré ou la vue sémantique, l'API d'un système d'enregistrement, l'état matérialisé d'un flux et l'index de recherche. Le bon choix dépend de la nature de la donnée.

### Les entrepôts

Les deux grandes plateformes offrent des serveurs MCP gérés. Celui de Snowflake prend en charge plusieurs types d'outils, dont un agent Cortex, la recherche, l'analyse sur vues sémantiques et l'exécution de SQL, en lecture seule par défaut [12]. Celui de Databricks distingue un serveur d'analyse en langage naturel, en disponibilité générale, d'un serveur d'exécution de SQL encore en bêta [13].

La documentation de Snowflake illustre l'écart entre un protocole et sa mise en œuvre [12] : le serveur suit la révision `2025-11-25` du protocole, antérieure à la révision sans état de juillet 2026, et n'expose que des outils. Les mécanismes de fraîcheur décrits en 15.1 n'y sont donc pas disponibles.

Le choix entre SQL libre et outil borné est le plus structurant. MCP Toolbox for Databases, serveur MCP à code source ouvert, propose les deux : un outil sur mesure y est un énoncé SQL à paramètres, tandis que des outils génériques, dont `execute_sql`, servent à l'exploration [20].

Le banc d'essai Spider 2.0 donne la mesure du risque du SQL libre. Sur 632 problèmes tirés de cas d'entreprise, avec des bases qui comptent souvent plus de mille colonnes, un agent fondé sur le modèle o1-preview n'en résout que 21,3 %; des méthodes fondées sur GPT-4 atteignaient 91,2 % de précision d'exécution sur Spider 1.0, une mesure différente [6]. Ces chiffres datent de la fin de 2024, mais l'écart entre un schéma d'école et un schéma réel est la leçon durable. La couche sémantique (chapitre 12) et les outils paramétrés réduisent le problème.

### Les API

Les systèmes d'enregistrement s'exposent par leurs API, transformées en outils par une passerelle (chapitres 24 et 25). Une API conçue pour une application renvoie souvent plus de champs qu'un agent n'en a besoin, ce qui gonfle le contexte et élargit l'exposition.

### Les flux d'événements

Un agent n'a pas à consommer un flux; il a besoin de l'état que le flux décrit. Le Real-Time Context Engine de Confluent applique ce principe : c'est l'interface MCP d'une table matérialisée sur un sujet Kafka, par laquelle un agent interroge l'état le plus récent [18]. Un billet de l'éditeur du 18 août 2026 le donne en disponibilité générale [19].

Le flux matérialisé règle la fraîcheur, mais ne donne que l'état courant : l'historique et les agrégats restent dans l'entrepôt (chapitre 19).

---

## 15.5 Données non structurées

Documents, courriels, pages et conversations forment une part importante de ce qu'un agent consulte. Leur difficulté tient à une asymétrie : le contenu se copie facilement dans un index, mais les permissions vivent dans le système source.

### Copier les permissions, ou interroger la source

La documentation d'Azure AI Search décrit plusieurs façons d'appliquer un contrôle d'accès au niveau du document [15]. La seule en disponibilité générale, le filtre de sécurité, repose sur une comparaison de chaînes entre l'identité de l'appelant et des champs de l'index. Les autres, en préversion, ingèrent les métadonnées de permission de la source et les comparent au jeton de l'utilisateur.

Le point faible commun est la synchronisation : un changement de permission dans la source n'a d'effet qu'après une nouvelle synchronisation de l'index [15]. Pour SharePoint, la documentation précise qu'un changement sur un niveau parent, hérité par les éléments enfants, exige une resynchronisation explicite, et que les liens de partage ouverts à toute l'organisation et les utilisateurs invités ne sont pas pris en charge [16].

La même documentation indique l'autre voie : interroger SharePoint directement, la gouvernance demeurant alors dans la source [16]. Le compromis est général. Un index copié offre la maîtrise de la pertinence, au prix d'une copie des droits qu'il faut tenir à jour. L'interrogation à la source garantit des droits exacts, au prix d'une dépendance à ce que la source sait chercher.

### Le partage excessif

Hériter fidèlement des permissions ne protège que si ces permissions sont justes. Microsoft l'écrit pour son assistant : il respecte les permissions existantes de SharePoint et de OneDrive, et si un contenu est déjà partagé trop largement, il peut le faire remonter à quiconque y a accès [17]. Ce qu'une recherche manuelle laissait enfoui devient accessible par une question.

Les contrôles proposés agissent à quatre niveaux : restreindre ce qui est découvrable, restreindre l'accès aux sites, réviser les accès dans le temps, et protéger les fichiers par étiquettes [17]. Le chiffrement ajoute une distinction utile : pour qu'un contenu chiffré soit résumé, l'utilisateur doit détenir à la fois le droit de le voir et celui d'en extraire le contenu. Le droit de lire et le droit de faire traiter par un modèle peuvent donc être séparés. Ce droit ne protège pas la donnée pendant le traitement : quand le modèle tourne chez un tiers, cette protection relève de l'inférence confidentielle (chapitre 46).

### Extraire avant d'interroger

Le non structuré se loge aussi dans les bases, sous forme de champs de texte. Le banc d'essai DAB observe que les agents s'en remettent presque entièrement aux expressions régulières pour en extraire l'information, ce qui échoue dès que la formulation varie [5]. Extraire en amont les entités utiles vers des colonnes typées reste plus sûr.

---

## 15.6 Leçon des bancs d'essai : fragmentation et droits d'accès

Cinq bancs d'essai simulent des données qui ressemblent à celles d'une entreprise. Aucun ne mesure un déploiement réel, et leurs chiffres portent sur les modèles disponibles à leur date.

| Banc d'essai | Ce qu'il simule | Résultat principal |
|---|---|---|
| Spider 2.0 (ICLR 2025) [6] | 632 problèmes de SQL sur des bases réelles, souvent plus de mille colonnes | 21,3 % de réussite |
| EnterpriseBench (EMNLP 2025) [3] | 500 tâches dans quatre domaines (génie logiciel, RH, finance, administration); sources fragmentées; hiérarchies de contrôle d'accès | 41,8 % d'achèvement pour le meilleur modèle, selon le résumé |
| CRMArena-Pro (prépublication, mai 2025) [7] | 19 tâches de vente, de service et de soumission, validées par des experts | Environ 58 % en un tour, 35 % en plusieurs tours |
| DAB (prépublication, version d'octobre 2026) [5] | 104 requêtes, 17 jeux de données, 4 systèmes de bases de données | 57 % au premier essai pour le meilleur agent |
| VAKRA (prépublication, août 2026) [8] | Plus de 8 000 API, 62 domaines, documents et politiques d'usage des outils | 70,4 % sur les tâches à un saut; 50 à 51 % en composition |

### La fragmentation

EnterpriseBench, conçu chez Fujitsu Research, place une couche de contrôle d'accès devant chaque source : le contenu inaccessible est filtré avant d'atteindre l'agent [3].

Son analyse d'erreurs, menée sur cent tâches, est instructive : les échecs les plus fréquents sont la décomposition de la tâche (20 cas) et le choix du mauvais outil (18), alors que la récupération du contexte n'en explique que deux. Avec un plan de référence, les résultats s'améliorent d'environ 40 à 50 % [3].

DAB arrive à un constat voisin avec des modèles de 2026. Parmi les réponses fausses, environ 57 % tiennent à une mise en œuvre incorrecte et 31 % à un plan incorrect; la sélection de mauvaises données n'en représente que 11 % [5]. Les agents trouvent la source et échouent à la joindre aux autres.

La conséquence pratique est contre-intuitive. Multiplier les connecteurs ne rend pas les données utilisables. Ce qui manque, ce sont les éléments qui permettent de combiner les sources : des clés communes, des définitions partagées, des parcours connus entre systèmes.

### Les droits d'accès

Trois résultats convergent sur le second thème. CRMArena-Pro rapporte que les agents n'ont à peu près aucune conscience spontanée de la confidentialité; une consigne ciblée l'améliore, mais souvent au détriment de la réussite des tâches [7]. VAKRA observe des échecs graves sur les questions soumises à des politiques d'usage : pour les requêtes auxquelles il ne faut pas répondre, le score le plus bas est de 2,4 % (Claude Opus 4.7, évalué sur un sous-ensemble), le suivant étant à 3,7 % [8]. Dans le tableau : « 70,4 % à un saut et 50 à 51 % en composition pour le meilleur modèle ». EnterpriseBench, lui, ne s'en remet pas au modèle : il filtre en amont.

La leçon rejoint celle de la section 15.3. Une règle d'accès exprimée en langage naturel dans un prompt est une préférence que le modèle respecte parfois. Une règle appliquée par la couche de données est un contrôle.

### Ce que ces bancs ne disent pas

EnterpriseBench repose sur des données synthétiques [3]; DAB ne couvre que quatre systèmes à code source ouvert [5]. Aucun des cinq bancs ne mesure à la fois des contrôles d'accès réels et des plateformes de données commerciales (chapitre 33).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Identité d'exécution des requêtes | Celle de l'utilisateur, avec jeton restreint aux portées de la tâche [É] | Accès identique pour tous, ou utilisateurs sans compte dans la plateforme : identité de service et politiques en mode fermé |
| Comportement en l'absence d'identité | Échec explicite [S] | — |
| Exposition d'un entrepôt | Outils paramétrés ou vues sémantiques [M] | SQL libre en lecture seule pour l'exploration, sur un serveur distinct |
| Découpage des serveurs | Par frontière d'accès et par public [É] | Très petit parc à droits uniformes |
| Point d'accès MCP d'une plateforme | Objet gouverné par le catalogue (octrois, politiques) [É] | Point d'accès hors catalogue : exploration seulement |
| Fraîcheur | Latence promise par contrat de données, âge de la donnée restitué par l'agent [S] | Données de référence stables |
| Données en mouvement | État matérialisé interrogeable [É] | Besoin de réagir à l'événement : chapitre 19 |
| Documents à permissions fines | Interrogation à la source [S] | Index copié si la pertinence l'exige, avec resynchronisation des permissions planifiée et vérifiée |
| Recherche sur populations distinctes | Un service ou un filtre par population [É] | Contenu réellement public à l'interne |
| Champs de texte libre | Extraction en amont vers des colonnes typées [S] | Volume faible : outil d'extraction dédié |
| Confidentialité | Contrôle dans la couche de données [M] | Consigne de prompt en complément seulement |
| Mise en service | Revue du partage excessif avant l'ouverture aux agents [É] | — |
| Métadonnées de qualité et de lignage | Émises sous forme normalisée et visibles au catalogue [S] | — |

---

## Points à retenir

- Une donnée est prête pour un agent quand elle est trouvable, d'un état connu, lue sous l'identité du demandeur et exposée par une interface bornée. Aucune de ces conditions ne se délègue au modèle.
- Les bancs d'essai convergent : les agents trouvent la source plus souvent qu'ils ne savent la combiner à une autre. La fragmentation se traite par des clés et des définitions communes, pas par davantage de connecteurs.
- Les agents ne protègent pas spontanément une information confidentielle. Une règle d'accès placée dans un prompt est une atténuation; seule la couche de données en fait un contrôle.
- L'héritage des droits de l'utilisateur réemploie les politiques existantes, mais se rompt à des endroits précis : repli silencieux sur un compte de service, composants à droits du propriétaire, outil de SQL libre voisin d'un agent gouverné, cache partagé.
- Les droits de l'utilisateur sont un plafond. Le jeton remis à l'agent doit être restreint à la tâche.
- Dans MCP, `ttlMs` est un indice de fraîcheur de la réponse et `lastModified` une date facultative; aucun ne dit si la donnée de fond respecte ce qui était promis. Cette promesse s'écrit dans un contrat de données.
- Pour les documents, copier les permissions dans un index crée une dette de synchronisation. Interroger la source garde les droits exacts.
- Hériter de permissions trop larges revient à les amplifier. Le partage excessif se corrige avant la mise en service.
- Un serveur MCP géré ne donne pas tout le protocole : celui de Snowflake n'expose que des outils, sur la révision `2025-11-25`, et certains points d'accès de Databricks échappent aux octrois du catalogue. Ce qu'un produit prend en charge se vérifie.

---

## Sources

Spécifications et articles, pages primaires lues le 11 novembre 2026 :

1. [MCP — Resources, spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)
2. [MCP — Caching, spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)
3. [Can LLMs Help You at Work? A Sandbox for Evaluating LLM Agents in Enterprise Environments — EnterpriseBench (arXiv 2510.27287, EMNLP 2025)](https://arxiv.org/html/2510.27287v1)
4. [Orchestrating Agents and Data for Enterprise: A Blueprint Architecture for Compound AI (arXiv 2504.08148)](https://arxiv.org/html/2504.08148)
5. [Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents — DAB (arXiv 2603.20576, version 3)](https://arxiv.org/html/2603.20576v3)

Articles d'abord lus au niveau du résumé, puis relus par extraits le 14 novembre 2026 :

6. [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows (arXiv 2411.07763, ICLR 2025)](https://arxiv.org/abs/2411.07763)
7. [CRMArena-Pro (arXiv 2505.18878)](https://arxiv.org/abs/2505.18878)
8. [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies (arXiv 2608.12282)](https://arxiv.org/abs/2608.12282)

Standards et documentation d'éditeurs, pages primaires lues le 11 novembre 2026 :

9. [Open Data Contract Standard v3.2.0](https://bitol-io.github.io/open-data-contract-standard/latest/home) et sa [section sur les niveaux de service](https://bitol-io.github.io/open-data-contract-standard/latest/service-level-agreement/)
10. [OpenLineage — documentation](https://openlineage.io/docs/) et [facettes de jeux de données](https://openlineage.io/docs/spec/facets/dataset-facets/)
11. [Snowflake — Snowflake-managed MCP or the Cortex Agents REST API](https://docs.snowflake.com/developer-guide/cortex-ai-cookbook/mcp-or-agent-rest-api) (vérifiée par l'éditeur le 4 octobre 2026)
12. [Snowflake — Snowflake-managed MCP server](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)
13. [Databricks — Managed MCP servers](https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp.html) (mise à jour le 10 novembre 2026)
14. [Databricks — Authentication for agents](https://docs.databricks.com/aws/en/generative-ai/agent-framework/agent-authentication) (mise à jour le 23 octobre 2026)
15. [Microsoft — Document-level access control, Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview)
16. [Microsoft — Use a SharePoint indexer to ingest permission metadata](https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists)
17. [Microsoft — Data protection and auditing for Microsoft Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture-data-protection-auditing) (datée du 9 novembre 2026)
18. [Confluent — Real-Time Context Engine, vue d'ensemble](https://docs.confluent.io/cloud/current/ai/real-time-context-engine/overview.html) (mise à jour le 3 novembre 2026; début de page seulement)
19. [Confluent — New in Confluent Intelligence and AI Tools, 18 août 2026](https://confluent.io/blog/2026-q3-confluent-intelligence-ai-update)
20. [MCP Toolbox for Databases — dépôt et fichier README](https://github.com/googleapis/mcp-toolbox)

Sources secondaires : aucune n'est citée. Les sources [11] à [20] sont de la documentation ou des billets d'éditeurs : primaires pour ce que le produit déclare, sans valeur de preuve indépendante.

## Limites de ce chapitre

- Les sources [6], [7] et [8], d'abord connues par leur seul résumé, ont été relues au-delà du résumé le 14 novembre 2026, par un outil qui en rend des extraits; les écarts relevés sont corrigés dans le texte.
- Les pages ont été lues par un outil d'extraction; pour les plus longues, seule la première partie a été couverte ([5], [18]). 
- L'audit du 12 novembre 2026 a relu [1], [2], [5] (environ 60 %), le résumé de [8], la section des niveaux de service de [9], [12], [13] et [19] : mécanismes MCP, chiffres de DAB et de VAKRA, propriétés d'ODCS et statuts de Snowflake, Databricks et Confluent sont confirmés. EnterpriseBench, Spider 2.0, CRMArena-Pro, OpenLineage et la documentation de Microsoft n'ont pas été relus.
- Le taux de 41,8 % d'EnterpriseBench vient du résumé de l'article et n'a pas été retrouvé dans les tableaux lus.
- La section relue d'ODCS cite les ajouts de la version 3.2.0 et annonce une version 4.0.0 : le numéro cité peut vieillir vite.
- Le choix de Snowflake, Databricks, Microsoft et Confluent reflète la documentation accessible, non une évaluation du marché. Aucun fait n'a été vérifié en exécutant un produit, et les statuts (préversion, bêta, disponibilité générale) changent vite.
- L'usage d'ODCS et d'OpenLineage au service des agents est une inférence de ce chapitre : les pages lues ne mentionnent pas les agents.
- La remarque sur les API qui renvoient trop de champs et le compromis entre index copié et interrogation à la source viennent de la connaissance générale. L'option « exploration seulement » pour un point d'accès hors catalogue est un raisonnement de ce chapitre.
- Aucune donnée d'adoption n'est citée. Les normes de qualité des données (ISO 8000, ISO/IEC 25012) et les catalogues ouverts n'ont pas été consultés.
