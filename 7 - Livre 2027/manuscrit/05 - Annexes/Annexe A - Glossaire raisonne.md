# Annexe A — Glossaire raisonné français-anglais de l'entreprise agentique

Ce glossaire fixe la terminologie bilingue contrôlée utilisée de bout en bout dans le liminaire et les douze chapitres de l'ouvrage. Chaque entrée associe le terme français canadien retenu dans la collection à son équivalent anglais d'usage courant dans la littérature scientifique, les groupes de normalisation et l'ingénierie logicielle. Conformément à la charte éditoriale, la première occurrence majeure d'un concept dans un chapitre présente l'intitulé français suivi de sa désignation anglaise entre parenthèses afin de préserver la lisibilité pour un lectorat francophone international tout en assurant la correspondance exacte avec les spécifications techniques.

La règle d'étanchéité inter-unités impose que chaque mécanisme fondateur ne soit défini pleinement que dans l'unité narrative qui en détient la propriété conceptuelle; les autres chapitres y renvoient sans redéfinition divergente. Le présent instrument rassemble ainsi les définitions canoniques issues du registre normatif de l'ouvrage.

## Définitions raisonnées

### Analyse de contrôle STPA (*Systems-Theoretic Process Analysis (STPA)*)

Méthode de sûreté système dérivée du modèle STAMP qui recense les actions de contrôle dangereuses et les défauts de rétroaction entre agents, logiciels déterministes et superviseurs humains avant tout déploiement. *(Unité propriétaire : ch08.)*

### Approbation réflexe (*rubber-stamping / automation bias*)

Défaut de supervision où un valideur humain entérine machinalement les propositions persuasives d'un agent sans examen critique des pièces, exposant l'organisation au régime juridique des décisions exclusivement automatisées. *(Unité propriétaire : ch11.)*

### Clé d'idempotence transactionnelle (*transactional idempotency key*)

Jeton unique et déterministe associé par l'appelant à une requête de mutation pour garantir qu'une reprise après timeout ou réessai de réseau n'applique l'effet métier qu'une seule fois. *(Unité propriétaire : ch06.)*

### Constance multi-essais (*pass^k consistency*)

Probabilité qu'un agent réussisse intégralement une même tâche opérationnelle sur k exécutions indépendantes consécutives, mesurant la fiabilité en production plutôt que la performance moyenne. *(Unité propriétaire : ch09.)*

### Couche anti-corruption (*Anti-Corruption Layer (ACL)*)

Façade d'adaptation déterministe placée devant les systèmes centraux patrimoniaux pour traduire les formats historiques, préserver l'exactitude décimale et protéger les bases d'autorité contre les requêtes directes des agents. *(Unité propriétaire : ch05.)*

### Couche sémantique métier (*enterprise semantic layer*)

Registre gouverné de définitions univoques des entités, métriques, règles d'agrégation et invariants juridiques qui ancre l'interprétation des agents sur une sémantique commune plutôt que sur des schémas techniques bruts. *(Unité propriétaire : ch05.)*

### Coût de transaction cognitif (*cognitive transaction cost*)

Ensemble des coûts de recherche d'information, de négociation contractuelle, de traduction inter-organisations et de vérification qui déterminent les frontières de la firme lorsqu'ils sont abaissés par des agents logiciels. *(Unité propriétaire : ch03.)*

### Coût par résultat conforme (*Cost per Compliant Outcome (CPO)*)

Coût complet d'une transaction métier menée à terme sans erreur ni reprise, intégrant l'inférence, les réessais, l'évaluation, l'infrastructure de sécurité, la conformité et la supervision humaine. *(Unité propriétaire : ch09.)*

### Crypto-agilité post-quantique (*post-quantum cryptographic agility*)

Capacité architecturale à renouveler et négocier sans refonte applicative des algorithmes de chiffrement et de signature résistants aux attaques quantiques malgré l'accroissement des tailles de clés, de signatures et de rotation des certificats. *(Unité propriétaire : ch12.)*

### Décision fondée exclusivement sur un traitement automatisé (*solely automated decision*)

Décision affectant une personne sans intervention humaine réelle et critique dans la boucle, déclenchant en vertu de l'article 12.1 de la Loi 25 des obligations d'information, d'explication et de révision. *(Unité propriétaire : ch10.)*

### Délégation au nom de (*On-Behalf-Of (OBO) delegation*)

Mécanisme d'échange de jetons distinguant explicitement l'identité du mandant humain initial et celle de l'agent mandataire exécutant l'action, tout en réduisant les privilèges au strict nécessaire. *(Unité propriétaire : ch07.)*

### Dérive silencieuse d'outil (*silent tool drift*)

Altération discrète des descriptions, schémas ou comportements d'un serveur d'outils exposé sous un même identifiant logique après autorisation initiale, créant un vecteur d'empoisonnement de la chaîne d'approvisionnement. *(Unité propriétaire : ch08.)*

### Dette cognitive et d'intention (*cognitive and intent debt*)

Accumulation d'artefacts logiciels et de décisions automatisées dont l'organisation ne maîtrise plus la logique sous-jacente ni les hypothèses métier initiales, fragilisant la maintenance et la conformité. *(Unité propriétaire : ch04.)*

### Économie d'agents virtuels (*virtual agent economy*)

Écosystème d'agents autonomes coordonnés par des mécanismes d'enchères, d'entiercement, de réputation et d'audit réglementaire qui réalisent des échanges économiques à haute fréquence sous mandat humain. *(Unité propriétaire : ch03.)*

### Effet Ringelmann multi-agents (*multi-agent Ringelmann effect*)

Dégradation marginale de l'efficacité et hausse du coût de coordination lorsque la taille d'un collectif d'agents dépasse le seuil optimal de la tâche au lieu de maintenir une spécialisation frugale. *(Unité propriétaire : ch06.)*

### Exécution durable (*durable execution*)

Modèle d'orchestration persistant chaque étape et chaque réponse d'inférence dans un journal d'événements afin de reprendre exactement une tâche longue après panne sans réexécuter les effets de bord déjà produits. *(Unité propriétaire : ch06.)*

### Harnais d'agent (*agent harness*)

Enveloppe d'exécution durcie qui isole le modèle, valide les schémas d'entrée et de sortie, applique les plafonds de tours et de budget, et médiatise tout appel d'outil. *(Unité propriétaire : ch04.)*

### Identité non humaine (*Non-Human Identity (NHI)*)

Identité cryptographique distincte, attestée et à courte durée de vie attribuée à une charge de travail ou à un agent logiciel, par opposition aux comptes génériques ou clés statiques partagées. *(Unité propriétaire : ch07.)*

### Industrialisation cognitive (*cognitive industrialization*)

Standardisation, automatisation à grande échelle et chute exponentielle du coût unitaire de nombreuses tâches cognitives sous l'effet composé des gains matériels, algorithmiques et d'investissement. *(Unité propriétaire : ch01.)*

### Interopérabilité verticale et horizontale (*vertical and horizontal interoperability*)

Séparation architecturale entre les protocoles verticaux reliant un agent à ses outils et sources de contexte et les protocoles horizontaux coordonnant la délégation asynchrone entre agents de domaines ou d'organisations distincts. *(Unité propriétaire : ch05.)*

### Loi de Lusser appliquée aux chaînes d'agents (*Lusser's reliability law for agent chains*)

Loi multiplicative de fiabilité en série montrant que la probabilité de succès sans erreur d'une chaîne de n étapes indépendantes décroît exponentiellement avec la longueur lorsque chaque maillon probabiliste demeure imparfait. *(Unité propriétaire : ch02.)*

### Noyau de contrôle déterministe (*deterministic control core*)

Ensemble des composants logiciels non probabilistes possédés par l'organisation (registre d'agents, identités, passerelles de politiques, contrats typés, machines à états durables et journaux d'audit) qui encadrent des modèles substituables. *(Unité propriétaire : ch04.)*

### Partition 80/20 (*80/20 deterministic-probabilistic split*)

Principe d'ingénierie consistant à maintenir environ 80 % des règles métier, autorisations, transitions d'état et mutations en code déterministe vérifiable, en confinant les 20 % de raisonnement probabiliste à l'interprétation et à la synthèse bornées. *(Unité propriétaire : ch04.)*

### Règle du maillon le plus élevé (*High-Water Mark Rule*)

Principe de durcissement selon lequel le niveau d'exigence sécuritaire et de conformité d'une chaîne d'agents s'aligne sur le maillon aval le plus critique qu'elle alimente sans sas d'assainissement, sans pour autant étendre les droits de mutation aux maillons amont. *(Unité propriétaire : 00-liminaire.)*

### Saga à point pivot (*pivot-transaction saga*)

Séquence de transactions locales coordonnées sans verrou distribué où toute étape précédant l'acte irréversible (point pivot) possède une action compensatoire idempotente acheminée sur un canal dédié. *(Unité propriétaire : ch06.)*

### Séparation par construction entre contrôle et données (*control-data separation by design*)

Architecture de sécurité inspirée des langages à capacités qui extrait le graphe d'appels d'outils depuis l'instruction fiable tout en confinant les contenus externes non approuvés afin d'empêcher toute injection indirecte. *(Unité propriétaire : ch08.)*

### Télémétrie à double couloir (*dual-lane telemetry*)

Architecture d'observabilité séparant la télémétrie opérationnelle à faible latence des preuves canoniques horodatées et hachées dédiées à l'audit réglementaire et à la relecture d'incidents. *(Unité propriétaire : ch09.)*

### Tissu conjonctif agentique (*agentic connective tissue*)

Combinaison de l'architecture d'interopérabilité (protocolaire, sémantique, mémorielle et contractuelle) et du plan d'orchestration déterministe qui relie les agents spécialisés, les systèmes patrimoniaux, les partenaires externes et les superviseurs humains. *(Unité propriétaire : 00-liminaire.)*

### Trajectoire adaptative sous seuils (DAPP) (*Dynamic Adaptive Policy Pathways (DAPP)*)

Méthode de gouvernance et de planification stratégique pré-positionnant des bascules d'architecture et de conformité déclenchées par des signaux mesurables (coût, réglementation, cryptographie ou compétence) plutôt que par des prévisions rigides. *(Unité propriétaire : ch12.)*

## Table synoptique d'équivalence bilingue

| Terme français | Équivalent anglais | Unité de référence |
|---|---|---|
| analyse de contrôle STPA | Systems-Theoretic Process Analysis (STPA) | ch08 |
| approbation réflexe | rubber-stamping / automation bias | ch11 |
| clé d'idempotence transactionnelle | transactional idempotency key | ch06 |
| constance multi-essais | pass^k consistency | ch09 |
| couche anti-corruption | Anti-Corruption Layer (ACL) | ch05 |
| couche sémantique métier | enterprise semantic layer | ch05 |
| coût de transaction cognitif | cognitive transaction cost | ch03 |
| coût par résultat conforme | Cost per Compliant Outcome (CPO) | ch09 |
| crypto-agilité post-quantique | post-quantum cryptographic agility | ch12 |
| décision fondée exclusivement sur un traitement automatisé | solely automated decision | ch10 |
| délégation au nom de | On-Behalf-Of (OBO) delegation | ch07 |
| dérive silencieuse d'outil | silent tool drift | ch08 |
| dette cognitive et d'intention | cognitive and intent debt | ch04 |
| économie d'agents virtuels | virtual agent economy | ch03 |
| effet Ringelmann multi-agents | multi-agent Ringelmann effect | ch06 |
| exécution durable | durable execution | ch06 |
| harnais d'agent | agent harness | ch04 |
| identité non humaine | Non-Human Identity (NHI) | ch07 |
| industrialisation cognitive | cognitive industrialization | ch01 |
| interopérabilité verticale et horizontale | vertical and horizontal interoperability | ch05 |
| loi de Lusser appliquée aux chaînes d'agents | Lusser's reliability law for agent chains | ch02 |
| noyau de contrôle déterministe | deterministic control core | ch04 |
| partition 80/20 | 80/20 deterministic-probabilistic split | ch04 |
| règle du maillon le plus élevé | High-Water Mark Rule | 00-liminaire |
| saga à point pivot | pivot-transaction saga | ch06 |
| séparation par construction entre contrôle et données | control-data separation by design | ch08 |
| télémétrie à double couloir | dual-lane telemetry | ch09 |
| tissu conjonctif agentique | agentic connective tissue | 00-liminaire |
| trajectoire adaptative sous seuils (DAPP) | Dynamic Adaptive Policy Pathways (DAPP) | ch12 |

## Repères d'usage entre couches déterministes et probabilistes

Une source fréquente d'ambiguïté dans les projets d'entreprise tient à la confusion entre le modèle de langage, composant statistique substituable, et l'agent logiciel pris comme système complet. Dans le lexique de cet ouvrage, le modèle génère des propositions ou des appels structurés sous contrainte de schéma, tandis que le harnais d'exécution, les passerelles d'outils, les identités non humaines et les machines à états durables forment le noyau de contrôle déterministe que l'organisation possède en propre.

### Frontière entre connectivité protocolaire et sémantique métier

Les protocoles ouverts de connectivité verticale vers les outils et de délégation horizontale entre pairs standardisent le transport et la description syntaxique des interfaces. Ils ne résolvent ni la définition univoque des indicateurs financiers, ni la gouvernance des accès aux données personnelles, ni la traduction exacte vers les systèmes patrimoniaux. D'où la place centrale accordée aux couches sémantiques, aux ontologies d'entreprise et aux façades anti-corruption qui protègent la précision décimale et les bases d'autorité.

### Économie de la constance et mesure du coût complet

Évaluer un flux agentique à partir d'un taux de réussite ponctuel sur un banc isolé ou d'un prix unitaire par million de jetons masque les échecs cumulés en chaîne et les coûts de reprise humaine. Les notions de constance multi-essais et de coût complet par résultat conforme ramènent la décision à l'unité économique réellement livrable : un dossier clôturé sans erreur, vérifiable et opposable en audit.

### Imputabilité, délégation cryptographique et facteur humain

Aucun agent autonome ne constitue un sujet de droit ni un acteur métier responsable au sens juridique. Les concepts d'identité non humaine éphémère, de délégation explicite au nom du mandant et d'approbation hors bande liée à l'empreinte canonique d'un acte assurent la continuité entre l'authentification technique et la responsabilité de direction. Parallèlement, la prévention de l'approbation réflexe et le maintien de quotas de traitement manuel préservent la capacité de repli lors d'incidents majeurs.
