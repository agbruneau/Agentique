# Annexe A — Glossaire raisonné français-anglais de l'entreprise agentique

Ce glossaire fixe la terminologie bilingue contrôlée utilisée dans le liminaire et les douze chapitres de l'ouvrage. Chaque entrée associe le terme français canadien retenu à son équivalent anglais d'usage dans la littérature scientifique, les groupes de normalisation et l'ingénierie logicielle. À la première occurrence majeure d'un concept, l'intitulé français précède sa désignation anglaise entre parenthèses afin d'assurer l'exactitude technique pour un lectorat francophone international.

Conformément à la règle d'étanchéité inter-unités, chaque mécanisme fondateur n'est défini pleinement que dans son unité propriétaire ; les autres chapitres y renvoient sans redéfinition divergente.

## Définitions raisonnées

### Analyse de contrôle STPA (*System-Theoretic Process Analysis*)

Méthode de sûreté système dérivée de STAMP (sigle STPA) recensant les actions de contrôle dangereuses et défauts de rétroaction entre agents, logiciels déterministes et superviseurs humains. *(Unité propriétaire : ch08.)*

### Approbation réflexe (*rubber-stamping / automation bias*)

Défaut de supervision où un valideur entérine machinalement les propositions persuasives d'un agent sans examen critique, exposant l'organisation au régime des décisions exclusivement automatisées. *(Unité propriétaire : ch11.)*

### Blanchiment de frontière (*boundary laundering*)

Défaut de compositionnalité où une donnée externe contaminée reçue par un agent amont est réécrite en prose naturelle vers un agent aval, qui la traite à tort comme une consigne fiable. *(Unité propriétaire : ch05.)*

### Clé d'idempotence transactionnelle (*transactional idempotency key*)

Jeton unique et déterministe associé par l'appelant à une mutation pour garantir qu'une reprise après délai d'attente ou réessai réseau n'applique l'effet métier qu'une seule fois. *(Unité propriétaire : ch06.)*

### Constance multi-essais (*passᵏ consistency*)

Probabilité qu'un agent réussisse intégralement une même tâche opérationnelle sur k exécutions indépendantes consécutives, mesurant la fiabilité réelle en production plutôt que la réussite ponctuelle. *(Unité propriétaire : ch09.)*

### Couche anti-corruption (*Anti-Corruption Layer*)

Façade déterministe (sigle ACL) placée devant les systèmes centraux patrimoniaux pour traduire les formats historiques, préserver l'exactitude décimale et protéger les bases d'autorité contre les requêtes directes. *(Unité propriétaire : ch05.)*

### Couche sémantique métier (*enterprise semantic layer*)

Registre gouverné de définitions univoques des entités, métriques, agrégations et invariants juridiques ancrant les agents sur un sens métier commun plutôt que sur des schémas bruts. *(Unité propriétaire : ch05.)*

### Coût complet par résultat conforme (*Cost per Compliant Outcome*)

Métrique économique (sigle CPO) mesurant le coût total d'une transaction métier menée sans erreur : inférence, réessais, évaluation, sécurité, conformité et supervision humaine. *(Unité propriétaire : ch09.)*

### Coût de transaction cognitif (*cognitive transaction cost*)

Ensemble des coûts de recherche d'information, de négociation contractuelle, de traduction inter-organisations et de vérification qui redessinent les frontières de la firme lorsqu'ils sont abaissés par des agents. *(Unité propriétaire : ch03.)*

### Crypto-agilité post-quantique (*post-quantum cryptographic agility*)

Capacité à renouveler et négocier sans refonte applicative des algorithmes de chiffrement et de signature résistants au quantique malgré l'accroissement des tailles de clés, signatures et rotations de certificats. *(Unité propriétaire : ch07.)*

### Décision fondée exclusivement sur un traitement automatisé (*solely automated decision*)

Décision affectant une personne sans intervention humaine critique dans la boucle, déclenchant en vertu de l'article 12.1 de la Loi 25 des devoirs d'information, d'explication et de révision. *(Unité propriétaire : ch10.)*

### Délégation au nom du mandant (*On-Behalf-Of delegation*)

Mécanisme d'échange de jetons (sigle OBO) préservant l'identité du mandant humain initial (`sub`) et celle de l'agent mandataire (`act`) tout en réduisant les privilèges au strict nécessaire. *(Unité propriétaire : ch07.)*

### Dérive silencieuse d'outil (*silent tool drift*)

Altération discrète des descriptions, schémas ou comportements d'un serveur d'outils sous un même identifiant logique après approbation, créant un vecteur d'empoisonnement de la chaîne d'approvisionnement. *(Unité propriétaire : ch08.)*

### Dette cognitive et d'intention (*cognitive and intent debt*)

Accumulation d'artefacts et de décisions automatisées dont l'équipe ne maîtrise plus la logique sous-jacente ni les hypothèses métier initiales, fragilisant maintenance et conformité. *(Unité propriétaire : ch04.)*

### Économie d'agents virtuels (*virtual agent economy*)

Écosystème d'agents autonomes coordonnés par des mécanismes d'enchères, d'entiercement, de réputation et d'audit qui réalisent des échanges économiques à haute fréquence sous mandat humain. *(Unité propriétaire : ch03.)*

### Effet Ringelmann multi-agents (*multi-agent Ringelmann effect*)

Dégradation marginale de l'efficacité et hausse du coût de coordination lorsque la taille d'un collectif d'agents dépasse son seuil optimal au lieu de préserver une spécialisation frugale. *(Unité propriétaire : ch06.)*

### Exécution durable (*durable execution*)

Orchestration persistant chaque étape et réponse d'inférence dans un journal d'événements afin de reprendre exactement une tâche longue après panne sans réexécuter les effets de bord déjà produits. *(Unité propriétaire : ch06.)*

### Harnais d'agent (*agent harness*)

Enveloppe d'exécution durcie qui isole le modèle, valide les schémas d'entrée et de sortie, applique les plafonds de tours et de budget, et médiatise tout appel d'outil. *(Unité propriétaire : ch04.)*

### Identité non humaine (*Non-Human Identity*)

Identité cryptographique distincte (sigle NHI), attestée et éphémère attribuée à une charge de travail ou à un agent logiciel, par opposition aux comptes génériques et secrets statiques. *(Unité propriétaire : ch07.)*

### Industrialisation cognitive (*cognitive industrialization*)

Standardisation, automatisation à grande échelle et baisse exponentielle du coût unitaire de nombreuses tâches cognitives sous l'effet composé des gains matériels, algorithmiques et d'investissement. *(Unité propriétaire : ch01.)*

### Injection indirecte de consignes (*indirect prompt injection*)

Attaque où des instructions adverses dissimulées dans un document, un courriel ou une réponse d'outil externe détournent l'exécution d'un agent opérant sous les droits d'un usager légitime. *(Unité propriétaire : ch08.)*

### Interopérabilité verticale et horizontale (*vertical and horizontal interoperability*)

Séparation entre les protocoles verticaux reliant un agent à ses outils et les protocoles horizontaux coordonnant la délégation asynchrone entre agents de domaines ou d'organisations distincts. *(Unité propriétaire : ch05.)*

### Loi de Lusser (*Lusser's reliability law for agent chains*)

Loi multiplicative de fiabilité en série montrant que le taux de succès sans erreur d'une chaîne de n étapes indépendantes décroît exponentiellement dès que chaque maillon probabiliste demeure imparfait. *(Unité propriétaire : ch02.)*

### Noyau de contrôle déterministe (*deterministic control core*)

Composants logiciels non probabilistes possédés par l'organisation (registre d'agents, identités, passerelles de politiques, contrats typés, machines à états durables et journaux d'audit) encadrant des modèles substituables. *(Unité propriétaire : ch04.)*

### Partition 80/20 (*80/20 deterministic-probabilistic split*)

Principe maintenant environ 80 % des règles métier, autorisations, transitions d'état et mutations en code déterministe vérifiable, tout en confinant les 20 % probabilistes à l'interprétation et la synthèse bornées. *(Unité propriétaire : ch04.)*

### Quadruple dette agentique (*quadruple agentic debt*)

Engrenage fermé liant dette technique, dette cognitive, dette d'intention et dette de couplage global lorsqu'une chaîne d'agents s'appuie sur le contexte du modèle plutôt que sur un noyau déterministe. *(Unité propriétaire : ch04.)*

### Règle de deux (*Rule of Two*)

Invariant déterministe interdisant dans un même tour d'inférence la conjonction simultanée d'entrées non fiables, de secrets ou données sensibles et d'actions vers l'extérieur ou d'état persistant. *(Unité propriétaire : ch08.)*

### Règle du maillon le plus élevé (*High-Water Mark Rule*)

Principe selon lequel le niveau d'exigence sécuritaire et réglementaire d'une chaîne d'agents s'aligne sur le maillon aval le plus critique sans sas d'assainissement, sans étendre les droits de mutation en amont. *(Unité propriétaire : 00-liminaire.)*

### Saga à point pivot (*pivot-transaction saga*)

Séquence de transactions locales sans verrou distribué où toute étape précédant l'acte irréversible (point pivot) possède une compensation idempotente acheminée sur un canal dédié. *(Unité propriétaire : ch06.)*

### Séparation par construction entre contrôle et données (*control-data separation by design*)

Architecture inspirée des langages à capacités qui extrait le graphe d'appels depuis l'instruction fiable et confine les données non approuvées comme variables opaques. *(Unité propriétaire : ch08.)*

### Télémétrie à double couloir (*dual-lane telemetry*)

Observabilité séparant la télémétrie opérationnelle à faible latence des preuves canoniques horodatées et hachées dédiées à l'audit réglementaire et à la relecture d'incidents. *(Unité propriétaire : ch09.)*

### Tissu conjonctif agentique (*agentic connective tissue*)

Combinaison de l'architecture d'interopérabilité (protocolaire, sémantique, mémorielle et contractuelle) et de l'orchestration déterministe reliant agents spécialisés, patrimoine applicatif, partenaires externes et superviseurs humains. *(Unité propriétaire : 00-liminaire.)*

### Trajectoire adaptative sous seuils (*Dynamic Adaptive Policy Pathways*)

Planification stratégique (sigle DAPP) pré-positionnant des bascules d'architecture et de conformité déclenchées par des signaux mesurables (coût, régulation, cryptographie) plutôt que par des prévisions rigides. *(Unité propriétaire : ch12.)*

## Table synoptique d'équivalence bilingue

| Terme français | Équivalent anglais | Unité de référence |
|---|---|---|
| analyse de contrôle STPA | System-Theoretic Process Analysis | ch08 |
| approbation réflexe | rubber-stamping / automation bias | ch11 |
| blanchiment de frontière | boundary laundering | ch05 |
| clé d'idempotence transactionnelle | transactional idempotency key | ch06 |
| constance multi-essais | passᵏ consistency | ch09 |
| couche anti-corruption | Anti-Corruption Layer | ch05 |
| couche sémantique métier | enterprise semantic layer | ch05 |
| coût complet par résultat conforme | Cost per Compliant Outcome | ch09 |
| coût de transaction cognitif | cognitive transaction cost | ch03 |
| crypto-agilité post-quantique | post-quantum cryptographic agility | ch07 |
| décision fondée exclusivement sur un traitement automatisé | solely automated decision | ch10 |
| délégation au nom du mandant | On-Behalf-Of delegation | ch07 |
| dérive silencieuse d'outil | silent tool drift | ch08 |
| dette cognitive et d'intention | cognitive and intent debt | ch04 |
| économie d'agents virtuels | virtual agent economy | ch03 |
| effet Ringelmann multi-agents | multi-agent Ringelmann effect | ch06 |
| exécution durable | durable execution | ch06 |
| harnais d'agent | agent harness | ch04 |
| identité non humaine | Non-Human Identity | ch07 |
| industrialisation cognitive | cognitive industrialization | ch01 |
| injection indirecte de consignes | indirect prompt injection | ch08 |
| interopérabilité verticale et horizontale | vertical and horizontal interoperability | ch05 |
| loi de Lusser | Lusser's reliability law for agent chains | ch02 |
| noyau de contrôle déterministe | deterministic control core | ch04 |
| partition 80/20 | 80/20 deterministic-probabilistic split | ch04 |
| quadruple dette agentique | quadruple agentic debt | ch04 |
| règle de deux | Rule of Two | ch08 |
| règle du maillon le plus élevé | High-Water Mark Rule | 00-liminaire |
| saga à point pivot | pivot-transaction saga | ch06 |
| séparation par construction entre contrôle et données | control-data separation by design | ch08 |
| télémétrie à double couloir | dual-lane telemetry | ch09 |
| tissu conjonctif agentique | agentic connective tissue | 00-liminaire |
| trajectoire adaptative sous seuils | Dynamic Adaptive Policy Pathways | ch12 |

## Repères méthodologiques et conventions d'interprétation

L'ouvrage distingue systématiquement les résultats mesurés par études empiriques publiées, les obligations issues de textes légaux ou prudentiels connus à la date de gel du 2 décembre 2026, et les heuristiques d'ingénierie de la collection (comme la partition 80/20 entre code déterministe et raisonnement probabiliste).

Les anglicismes techniques et sigles normalisés (`MCP`, `A2A`, `SPIFFE`, `WIMSE`, `OBO`, `DPoP`, `CIBA`, `FIDO`, `JCS`, `ML-DSA`, `STPA`, `FOCUS`, `DAPP`, `FinOps`, passᵏ) sont conservés tels quels après mise en contexte, tandis que les concepts d'architecture et de gouvernance sont systématiquement rédigés en français canadien dans la prose courante.

### Frontière entre couches déterministes, probabilistes et sémantiques

Le modèle de langage demeure un composant statistique substituable générant des propositions sous contrainte de schéma, tandis que le harnais d'exécution, les passerelles d'outils, les identités non humaines et les machines à états durables forment le noyau déterministe possédé par l'institution. Les protocoles ouverts de connectivité (`MCP`, `A2A`) standardisent le transport mais ne remplacent ni les couches sémantiques métier ni l'imputabilité juridique.

### Sigles normalisés et portée de transférabilité

| Sigle | Domaine | Signification usuelle |
|---|---|---|
| `MCP` / `A2A` | Interopérabilité | *Model Context Protocol* et *Agent-to-Agent* |
| `SPIFFE` / `WIMSE` | Identité des charges | Attestation éphémère d'identité non humaine |
| `OBO` / `DPoP` | Délégation d'accès | Échange de jetons *On-Behalf-Of* et preuve de possession |
| `CIBA` / `FIDO` | Approbation humaine | Consentement asynchrone lié cryptographiquement |
| `JCS` (`RFC 8785`) | Preuve et audit | Canonisation JSON avant empreinte `SHA-256` |
| `ML-DSA` / `SLH-DSA` | Post-quantique | Signatures normalisées `NIST FIPS 204` et `205` |
| `STAMP` / `STPA` | Sûreté système | Analyse du contrôle fondée sur les boucles de contrainte |
| `FOCUS` / `DAPP` | Économie et stratégie | Imputation normalisée des coûts et trajectoires adaptatives |

### Règle de cohérence entre texte, diagrammes et registres

Les intitulés figurant dans la table d'équivalence bilingue s'appliquent à l'identique aux légendes des vingt-trois figures originales ainsi qu'aux entrées des Annexes B et C, évitant tout glissement sémantique entre architecture logicielle, sécurité et conformité.
