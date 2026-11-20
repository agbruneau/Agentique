# Chapitre 6 — Ingénierie du contexte, mémoire distribuée et souveraineté sémantique des données

L’interopérabilité verticale avec les outils via `MCP` (chapitre 04) et l’interopérabilité horizontale entre pairs autonomes via `A2A` et `AGNTCY` (chapitre 05) restent inopérantes si chaque agent aborde ses tâches sans continuité cognitive ou interprète les données métier selon des hypothèses improvisées. Un `System of Agency` fiable ne dépend pas seulement de son modèle d’inférence ou de ses connecteurs, mais de la pertinence, de la fraîcheur et de la gouvernance des jetons placés dans sa fenêtre contextuelle à chaque tour [97] [98]. En pratique, nombre d’erreurs imputées au modèle résultent d’un déficit d’architecture contextuelle : fragments documentaires privés de leur contexte parent [99], indicateurs financiers recalculés de manière divergente sur des tables brutes [100] [101], ou souvenirs d’interactions antérieures corrompus déviant les décisions ultérieures [102] [103].

Ce chapitre couvre la dimension mémoire et sémantique du Plan 3 d’interopérabilité (chapitre 02). Côté architecture de solutions (`SA`), il s’agit de structurer la mémoire distribuée sous contrainte d’attention finie, de dépasser le `RAG` naïf par des pipelines fédérés hybrides, structurés et graphiques, et de propager les droits d’accès jusqu’au stockage [98] [104] [105]. Côté architecture d’entreprise (`EA`), il s’agit d’empêcher la formation d’un système parallèle de bases vectorielles et de formules métier concurrentes, en arrimant les agents aux contrats de données, aux couches sémantiques, au `MDM` et aux ontologies d’entreprise [100] [101] [106]. Par frontière d’étanchéité, ce chapitre porte uniquement sur la mémoire cognitive et les connaissances métier ; la persistance transactionnelle des workflows (*checkpointing* et rejeu) relève du chapitre 09.

## 6.1 Taxonomie des quatre mémoires d’entreprise : travail, épisodique, sémantique et procédurale

### 6.1.1 De l’amorce statique à l’ingénierie du contexte : budget d’attention et dégradation

À l’origine des applications génératives, l’ingénierie des amorces (*prompt engineering*) visait à rédiger des consignes statiques pour des requêtes isolées de classification ou de synthèse [98]. Dès qu’un agent opère en boucle multi-tours sur une durée prolongée, chaque appel d’outil, chaque passage récupéré et chaque observation s’ajoutent à l’historique d’inférence [98] [107]. L’ingénierie du contexte (*context engineering*) devient alors la discipline itérative qui sélectionne, compresse, ordonne et évince l’ensemble des jetons fournis au modèle à chaque étape afin de guider son comportement [98].

Cette exigence découle de la mécanique même des transformeurs : chaque jeton établit des relations d’attention avec tous les autres, engendrant `O(n²)` interactions appariées pour une fenêtre de `n` jetons [98] [107]. Bien que la taille nominale des fenêtres s’étende désormais à plusieurs centaines de milliers de jetons, les bancs d’essai de rappel ciblé (*needle-in-a-haystack*) révèlent une dégradation progressive nommée pourrissement du contexte (*context rot*) : à mesure que le volume de jetons croît, la précision du modèle pour retrouver un fait précis ou suivre des dépendances de longue portée décroît [98]. Le contexte actif constitue donc une ressource finie à rendements décroissants, grevée par un budget d’attention limité [98]. Pour le `SA`, élargir passivement la fenêtre d’inférence dégrade à la fois la qualité de raisonnement, la latence de pré-remplissage et le coût unitaire [98] [99].

### 6.1.2 Les quatre strates mémorielles selon CoALA et leur traduction d’entreprise

Afin d’organiser la cognition agentique au-delà d’une fenêtre unique, le cadre `CoALA` (*Cognitive Architectures for Language Agents*), issu des sciences cognitives et de l’intelligence artificielle symbolique, distingue la mémoire de travail active de trois mémoires à long terme [97]. Complétée par les systèmes de contexte virtuel comme `MemGPT` [107] et les gestionnaires applicatifs comme `LangMem` [108], cette taxonomie structure quatre compartiments en entreprise :

1. **La mémoire de travail (*working memory*)** regroupe les données éphémères présentes dans la fenêtre active au tour courant : amorce système, échanges récents, retours d’outils et bloc actif de travail [97] [98] [107]. Transposant la mémoire virtuelle et la pagination des systèmes d’exploitation, `MemGPT` montre que l’`Agent Harness` (chapitre 03) peut laisser l’agent transférer explicitement des données entre sa mémoire principale en contexte et ses stockages externes via des appels de fonctions et des interruptions [107].
2. **La mémoire épisodique (*episodic memory*)** archive les séquences d’expériences passées : situation observée, raisonnement suivi, action entreprise et résultat obtenu [97] [108]. Elle alimente une adaptation par exemples contextualisés (*few-shot* dynamique), permettant à un agent de réutiliser la trace d’une résolution complexe antérieure plutôt que de repartir de zéro [108].
3. **La mémoire sémantique (*semantic memory*)** stocke les faits durables, politiques, connaissances d’affaires et profils d’entités indépendants d’une session particulière [97] [108]. Opérationnellement, elle se partage entre **collections** documentaires et factuelles — exigeant une consolidation ou une invalidation lors de faits contradictoires — et **profils** à schéma typé offrant une lecture directe par clé métier [108].
4. **La mémoire procédurale (*procedural memory*)** formalise le savoir-faire de l’agent : instructions système, règles de comportement, code ou gabarits de compétences [97] [108]. Là où la mémoire épisodique conserve le récit d’un cas particulier, la mémoire procédurale régit l’exécution future de tous les cas ; en entreprise réglementée, sa mise à jour par rétroaction doit rester soumise à un contrôle de version `Git` et à une approbation explicite plutôt qu’à une auto-écriture autonome en production [108].

| Strate | Contenu cognitif | Support usuel | Mise à jour | Risque majeur | Frontière ch. 09 |
| --- | --- | --- | --- | --- | --- |
| Travail | Tour courant, but actif, extraits immédiats | Fenêtre d’inférence, cache d’amorces | Synchrone par tour (compaction, éviction) | Pourrissement contextuel (`context rot`) | Éphémère ; ne survit pas à une panne serveur |
| Épisodique | Trajectoires passées (`observation`, action, résultat) | Base vectorielle horodatée, espaces de noms | Formation *hot path* ou asynchrone | Empoisonnement (`MINJA`), biais de récence | Garde l’expérience cognitive, non le log de *replay* |
| Sémantique | Faits métier, corpus documentaire, profils, graphe | Index hybride, graphe, tables relationnelles | Pipelines gouvernés et réconciliation | Données périmées, fuite inter-`ACL` | Connaissances stables, distinctes de l’état de saga |
| Procédurale | Directives système, règles métier, compétences | Dépôt `Git` versionné, artefacts `YAML` | Revue humaine et validation `EvalOps` | Dérive silencieuse si modifiée sans contrôle | Définit le comportement, non le curseur d’état |

*Tableau 6.1 — Taxonomie opérationnelle des quatre mémoires d’entreprise agentique et séparation d’avec le chapitre 09.*

### 6.1.3 Stratégies de curation : compaction, prise de notes, hot path et arrière-plan

Maintenir la qualité décisionnelle sur des tâches longues exige quatre mécanismes d’échange entre la mémoire de travail et les couches persistantes [98] [108] :

1. **La compaction** s’exécute à l’approche du plafond d’attention : l’historique actif est synthétisé pour préserver décisions, contraintes et tâches ouvertes, puis injecté dans une fenêtre réinitialisée [98]. Un élagage brutal perd des identifiants clés ; son absence noie le signal sous les traces d’outils [98].
2. **La prise de notes structurée** maintient un journal synthétique externe relu à la demande après réinitialisation de la fenêtre [98].
3. **La récupération juste-à-temps (*just-in-time*)** remplace le pré-chargement massif par des références légères explorées à la demande par outils [98]. Pour contenir la latence d’exploration tout en préservant le signal, l’usage hybride charge d’emblée les invariants critiques et lit les annexes sur besoin [98].
4. **La formation consciente (*hot path*) contre subconsciente (arrière-plan)** règle l’écriture des mémoires épisodique et sémantique [108]. En *hot path*, l’agent consigne de nouveaux faits pendant la session au prix d’une latence accrue ; en arrière-plan, un processus asynchrone extrait et consolide les souvenirs hors ligne sans ralentir l’utilisateur [108].

> **[Figure]**
> - Agent Harness (Exécution
> - cognitive en session)
> - [container]
> - Couche de mémoires cognitives distribuées
> - [container]
> - «component» Mémoire de travail
> - [Fenêtre active]
> - Instructions, tours récents
> - et notes structurées
> - «component» Moteur de compaction
> - [Curation / Éviction]
> - Synthèse de contexte et divulgation juste-à-temps
> - «component» Gestionnaire mémoriel
> - [Hot Path / Async]
> - Arbitre lecture et écriture des mémoires long terme
> - «component» Mémoire épisodique
> - [Vecteurs + Horodatage]
> - Trajectoires passées, cas similaires et préférences
> - «component» Mémoire sémantique
> - [RAG + Graphe + Profils]
> - Corpus documentaire, faits et ontologie métier
> - «component» Mémoire procédurale
> - [Git / Registre YAML]
> - Règles validées, prompts et gabarits de compétences
> - «external_system» Exécution durable
> - (Chapitre 09)
> - Checkpointing transactionnel,
> - replay déterministe et Sagas
> - Sature budget
> - O(n²)
> - Réinitialise avec synthèse
> - Interroge /
> - extrait
> - Lit / consolide
> - expériences
> - Récupère connaissances
> - Charge règles
> - versionnées
> - Distingue état transactionnel [Hors mémoire cognitive]

*Fig. 21. – Topologie des quatre mémoires cognitives d’entreprise et boucle d’ingénierie du contexte*

### 6.1.4 Frontière stricte entre mémoire cognitive et persistance transactionnelle

La figure 6.1 trace la frontière d’étanchéité de l’ouvrage : les quatre strates cognitives gèrent la pertinence informationnelle et la continuité sémantique [97] [108], tandis que la persistance transactionnelle — journal d’événements, *checkpointing*, reprise après panne et sagas — relève du chapitre 09. Un orchestrateur ne reconstruit jamais l’étape d’un traitement critique à partir d’un résumé épisodique probabiliste.

> **Arbitrage EA / SA** — Interdire de confier l’état de reprise d’un workflow transactionnel à une mémoire épisodique ou à une synthèse de contexte, et proscrire l’auto-réécriture non versionnée de la mémoire procédurale en production [108]. Le `SA` dissocie dans l’`Agent Harness` la mémoire de travail soumise à compaction [98] [107], les collections consolidées en arrière-plan par espaces de noms [108] et le moteur durable du chapitre 09. L’`EA` exige que toute modification de la mémoire procédurale transite par `Git` et une batterie de non-régression `EvalOps`.

## 6.2 De la recherche naïve à l’Agentic RAG fédéré : hybride lexical/vectoriel, Text-to-SQL gouverné et graphes

### 6.2.1 Limites du RAG vectoriel naïf et apport du Contextual Retrieval

Le `RAG` naïf découpe les documents en blocs fixes de quelques centaines de jetons, calcule des vecteurs denses et injecte les plus proches voisins sémantiques dans l’amorce [99] [104]. En entreprise, cette chaîne linéaire échoue pour quatre raisons [99] [104] [109] :

1. **Perte du contexte référentiel** : un bloc isolé mentionnant une variation trimestrielle de revenu de 3 % perd toute utilité si l’entité émettrice et l’exercice fiscal figuraient uniquement en tête du document [99].
2. **Cécité aux identifiants exacts** : les plongements denses capturent la proximité thématique mais manquent fréquemment les chaînes littérales telles qu’un code d’erreur `TS-999`, un numéro de pièce ou une référence réglementaire [99].
3. **Rigidité du flux à passe unique** : le pipeline statique ne sait ni diagnostiquer des passages hors sujet ni reformuler une requête sous-spécifiée [104] [110].
4. **Incapacité analytique et synthétique** : la similarité locale échoue sur les calculs tabulaires exacts et sur les synthèses transversales d’un corpus entier [109] [100].

Pour résoudre la fragmentation dès l’ingestion, le patron `Contextual Retrieval` préfixe chaque bloc de texte par un court résumé situationnel de 50 à 100 jetons généré à partir du document parent, puis indexe ce bloc enrichi à la fois en vecteurs denses (`Contextual Embeddings`) et en index lexical (`Contextual BM25`) [99]. Sur des jeux de test d’entreprise (code, finance, documentation technique), les vecteurs contextualisés seuls abaissent de **35 %** les échecs de récupération dans le top-20 ; l’ajout du `BM25` contextualisé porte la réduction à **49 %** ; enfin, la combinaison avec un réordonnanceur `Cross-Encoder` en second étage (chapitre 03) atteint **67 %** de baisse des échecs [99]. Ce pré-traitement reste économiquement viable en exploitant le cache d’amorces (*Prompt Caching*) sur le document complet partagé entre ses fragments, réduisant la latence d’indexation de plus d’un facteur 2 et son coût jusqu’à 90 % selon les mesures publiées [99].

### 6.2.2 Recherche hybride lexicale/vectorielle et fusion RRF

Combiner la recherche lexicale `BM25` (sensible aux correspondances exactes, à la rareté `IDF` et à la longueur de document) avec la recherche vectorielle dense suppose de réconcilier des scores aux échelles hétérogènes [99] [111]. Additionner directement une similarité cosinus bornée et un score `BM25` non borné rend le classement fragile selon les corpus [112].

L’algorithme de référence adopté par les moteurs de recherche hybride (tels qu’Azure AI Search) est la fusion par rang réciproque (`Reciprocal Rank Fusion`, `RRF`) établie par Cormack, Clarke et Büttcher [112] [111]. Au lieu de normaliser les scores bruts, `RRF` évalue chaque document `d` à partir de son seul rang `rang_i(d)` dans chaque liste retournée en parallèle : `score_RRF(d) = Σ 1 / (k + rang_i(d))` [112] [111]. Les évaluations empiriques prouvent qu’une constante de lissage `k = 60` neutralise les pics isolés d’un moteur tout en récompensant les fragments bien classés sur les deux modalités, surpassant les moteurs individuels et la fusion de Condorcet sans aucun apprentissage préalable [112] [111]. Cette fusion rapide fournit les 50 à 100 candidats ensuite filtrés par `Cross-Encoder` [99] [111].

### 6.2.3 Boucles de l’Agentic RAG et raffinement correctif (CRAG)

L’`Agentic RAG` remplace l’exécution linéaire rigide par une boucle où un agent planifie la recherche, décompose les questions composites, choisit les moteurs appropriés et vérifie la qualité des preuves collectées avant de répondre [104]. Ce saut architectural évite que le générateur ne produise des réponses plausibles à partir de passages récupérés par défaut mais non pertinents [104] [110].

Le mécanisme `Corrective RAG` (`CRAG`) formalise cette porte de contrôle au moyen d’un évaluateur léger classant la confiance de la récupération selon trois verdicts [110] :

1. **Verdict** `Correct` : les passages validés subissent un raffinement par décomposition et recomposition en bandes de connaissance (*knowledge strips*) afin d’extraire les seules phrases utiles et d’économiser le budget d’attention [110].
2. **Verdict** `Incorrect` : les passages médiocres sont écartés, la requête est reformulée et l’agent bascule vers une source complémentaire fédérée autorisée [104] [110].
3. **Verdict** `Ambigu` : l’évaluateur fusionne les bandes internes filtrées avec une requête d’appoint pour lever l’ambiguïté [110].

### 6.2.4 Données structurées et synthèses globales : Text-to-SQL gouverné et GraphRAG

L’`Agentic RAG` fédéré ne peut traiter les requêtes quantitatives ou transversales par simple recherche documentaire [109] [100]. Exposer un schéma `SQL` physique brut à un `LLM` pour générer des requêtes à la volée échoue lourdement sur les systèmes réels : sur un banc d’essai d’assurance comptant 43 requêtes métier, Sequeda, Allemang et Jacob mesurent une exactitude de **16 %** seulement avec `GPT-4` en *zero-shot* sur le schéma physique, contre **54 %** lorsque les requêtes s’appuient sur une couche sémantique ontologique formalisant le contexte métier [100].

Pour fiabiliser le `Text-to-SQL` en production, les plateformes modernes telles que `Snowflake Cortex Analyst` et `dbt Semantic Layer` remplacent les tables brutes par des modèles sémantiques `YAML` (ou vues sémantiques `CREATE SEMANTIC VIEW`) déclarant explicitement tables logiques, dimensions, valeurs énumérées, mesures agrégées et chemins de jointure approuvés, complétés par un catalogue de requêtes vérifiées (*verified queries*) guidant le modèle sur les questions récurrentes [113] [101]. Le `SQL` généré s’exécute sous les rôles d’accès existants de l’entrepôt sans exposition des données pour entraînement [113]. En complément, le `SA` encapsule l’exécution derrière un analyseur syntaxique déterministe (`AST`) vérifiant l’absence d’opérations de mutation et un rôle strict en lecture seule.

Pour les synthèses globales portant sur l’ensemble d’un corpus (tendances transversales, risques systémiques) ou les enquêtes multi-sauts, `GraphRAG` indexe les documents en deux temps : extraction par `LLM` d’un graphe d’entités et de relations, puis détection hiérarchique de communautés pré-résumées [109]. Une requête globale déclenche une synthèse *Map-Reduce* sur ces résumés communautaires, produisant sur des corpus d’environ un million de jetons des réponses nettement plus complètes et diversifiées que le `RAG` vectoriel, au prix d’un budget d’indexation supérieur [109].

> **[Figure]**
> - Pipeline Agentic RAG
> - fédéré [container]
> - «component» Routeur et planificateur
> - [Classification d'intention]
> - Décompose la requête et
> - sélectionne les moteurs
> - «component» Recherche hybride [Contextual BM25 + Vecteurs]
> - Fusion RRF (k=60) puis Cross-Encoder
> - «component» Text-to-SQL gouverné
> - [Modèle sémantique + AST]
> - Compile SQL contraint sur métriques et jointures
> - «component» Moteur GraphRAG
> - [Entités + Communautés]
> - Traversée multi-sauts ou synthèse globale Map-Reduce
> - «component» Évaluateur CRAG
> - [Confiance à 3 verdicts]
> - Correct / Ambigu / Incorrect
> - et filtrage de bandes
> - «container» Nœud cognitif
> - [Agent Harness]
> - Formule requête initiale ou itérative
> - «external_system» Entrepôt analytique
> - Vues sémantiques
> - en lecture seule
> - «external_system» Fenêtre de contexte
> - Preuves sourcées
> - compactes
> - Soumet requête
> - Texte / Réf.
> - exactes
> - Agrégations /
> - KPI chiffrés
> - Thèmes globaux /
> - liens multi-sauts
> - Exécute lecture seule
> - Top-K fusionnés
> - Résultat typé
> - Synthèse graphe
> - Incorrect : réécrit / réplique
> - Correct : injecte preuves

*Fig. 22. – Pipeline d’Agentic RAG fédéré : routage adaptatif, recherche hybride RRF, Text-to-SQL gouverné et GraphRAG*

| Approche | Cas optimaux | Latence et `FinOps` | Mécanisme clé | Limite principale |
| --- | --- | --- | --- | --- |
| `RAG` vectoriel naïf | Corpus homogène non critique | Faible latence, coût minime | Similarité cosinus simple | Contexte fragmenté, faible rappel lexical, pas d’agrégation [99] |
| Hybride `Contextual` + `RRF` | Procédures, contrats, tickets, code | Indexation cachée abordable, latence modérée | Préfixes contextuels, fusion `k = 60`, `Cross-Encoder` | Inadapté aux calculs exacts et synthèses globales [99] [111] |
| `Agentic RAG` (`CRAG`) | Dossiers composites multi-sources | Latence variable selon réessais | Verdicts de confiance et bandes filtrées | Risque de boucles sans plafond de tours [104] [110] |
| `Text-to-SQL` gouverné | Métriques chiffrées et séries temporelles | Latence d’entrepôt, inférence contenue | Modèle sémantique `YAML`, jointures et `verified queries` | Dépend du maintien rigoureux des couches sémantiques [113] [101] |
| `GraphRAG` hiérarchique | Synthèses thématiques et liens multi-sauts | Coût d’indexation élevé, exécution *Map-Reduce* | Communautés pré-résumées et graphe d’entités | Rafraîchissement incrémental onéreux [109] |

*Tableau 6.2 — Matrice de sélection des moteurs d’interrogation dans l’Agentic RAG fédéré.*

> **Arbitrage EA / SA** — Exclure le `RAG` vectoriel naïf et le `Text-to-SQL` sur schémas physiques bruts dès qu’une réponse informe une décision opérationnelle [99] [100]. Le `SA` déploie par défaut la recherche hybride contextualisée avec fusion `RRF` (`k = 60`) et réordonnanceur [99] [112], restreint le `Text-to-SQL` aux vues sémantiques validées avec vérification syntaxique en lecture seule [113] [101], et borne à 2 ou 3 les itérations `CRAG`. L’`EA` limite `GraphRAG` aux corpus stratégiques à forte valeur relationnelle pour éviter l’inflation des coûts d’indexation [109].

## 6.3 Souveraineté sémantique : arrimage aux Data Contracts, couches BI, MDM et ontologies métier

### 6.3.1 Le risque de schisme analytique entre BI humaine et agents autonomes

L’essor autonome d’équipes IA produit fréquemment une dérive silencieuse : les définitions de métriques et d’entités métier sont recodées de manière ad hoc dans des amorces système ou des descriptions d’outils `MCP`, en marge des référentiels d’informatique décisionnelle (`BI`) [101]. Lorsque le tableau de bord financier d’un comité exécutif affiche un résultat différent de celui calculé par un agent d’analyse des revenus sur la même période, l’organisation perd la traçabilité de ses chiffres [100] [101].

La **souveraineté sémantique** exige que le sens métier, les règles d’agrégation, les seuils de qualité et la classification des données résident en un point unique partagé entre humains (`BI`) et agents [101] [106]. Au lieu d’enfouir la logique métier dans des prompts vulnérables à l’enchevêtrement `CACE` (chapitre 01), l’architecture arrime les pipelines de contexte aux contrats et couches gouvernées existantes [113] [101].

### 6.3.2 Contrats de données exécutables : Open Data Contract Standard (ODCS)

Un pipeline de contexte alimenté par des tables ou flux dont le schéma ou la qualité dérivent sans contrat devient une source d’erreurs silencieuses. Porté par `Bitol` au sein de la Linux Foundation AI & Data, l’`Open Data Contract Standard` (`ODCS`) normalise cet accord producteur-consommateur sous forme de spécifications `YAML` versionnées dans `Git` [106].

Dans sa version `v3`, l’`ODCS` unifie la représentation logique et physique des objets (tables relationnelles, documents, flux) et de leurs propriétés tout en intégrant la classification de sensibilité (`public`, `restricted`), les assertions automatisables de qualité, les accords de niveau de service (`SLA`), les équipes responsables et les définitions autoritatives (*authoritative definitions*) liant chaque attribut au glossaire d’entreprise [106]. Branché en amont de l’indexation agentique, le contrat `ODCS` assure trois garde-fous :

1. **Sélection contractuelle des champs** : seuls les attributs documentés et compatibles avec la politique de confidentialité du domaine alimentent les index ou profils d’agents [106] [114].
2. **Détection de rupture de fraîcheur et de qualité** : l’échec d’une règle `ODCS` ou la violation d’un `SLA` suspend la confiance accordée au gisement plutôt que d’exposer des faits périmés [106].
3. **Enrichissement sémantique sans redondance** : les noms métier (`businessName`), descriptions et synonymes du contrat nourrissent directement les routeurs de contexte et les outils `MCP` [106].

### 6.3.3 Couches sémantiques partagées, MDM et passage au Golden Context

Deux piliers du patrimoine de données complètent les contrats d’interface : la couche sémantique analytique et la gestion des données maîtresses (`MDM`) [113] [101].

Des couches telles que `dbt Semantic Layer` (via le moteur `MetricFlow`) ou les vues sémantiques `Snowflake` déplacent la définition des entités, dimensions et métriques hors de chaque outil `BI` vers un modèle centralisé [113] [101]. `MetricFlow` résout automatiquement les jointures entre modèles et expose des indicateurs gouvernés aux tableaux de bord comme aux agents via `API` et serveur `MCP` [101]. Toute révision d’une formule comptable ou opérationnelle se propage ainsi instantanément et à l’identique vers l’ensemble des consommateurs humains et agentiques [101].

Le `MDM` lève quant à lui l’ambiguïté identitaire entre systèmes sources hétérogènes (`ERP`, `CRM`, facturation) en consolidant des *Golden Records* pour les clients, produits et fournisseurs. L’architecture agentique prolonge cette approche en reliant chaque *Golden Record* aux contrats `ODCS`, aux pièces contractuelles non structurées et aux relations hiérarchiques du graphe métier — constituant un **Golden Context** unifié sur lequel l’agent raisonne sans dupliquer les entités [100] [106].

### 6.3.4 Ontologies métier OWL 2 et validation déterministe par SHACL

Dans les domaines réglementaires ou industriels à forte densité de règles, des descriptions `YAML` isolées ne suffisent pas à formaliser les relations complexes. Les standards du `W3C` — `OWL 2` et `SHACL` — apportent la rigueur formelle requise [115] [116].

`OWL 2` (*Web Ontology Language*) définit les classes métier, hiérarchies, propriétés et axiomes logiques indépendamment des bases physiques [116], permettant les gains de précision mesurés lorsque des mappings ontologiques comblent l’écart entre langage métier et schémas relationnels [100]. Tandis qu’`OWL 2` exprime la sémantique du domaine, `SHACL` (*Shapes Constraint Language*) valide de façon purement déterministe les graphes de données `RDF` face à un graphe de formes (*shapes graph*) en vérifiant cardinalités, types, plages de valeurs et intégrité relationnelle [115]. Combiné en intégration d’entreprise aux pipelines `GraphRAG` [109], un contrôle `SHACL` en amont bloque ou place en revue d’intendance toute entité extraite qui viole les invariants structurels du domaine, préservant la pureté du graphe de connaissances [109] [115].

> **[Figure]**
> - Données maîtresses et Contrats (Plan 3)
> - Souveraineté sémantique
> - Consommateurs gouvernés
> - Data Contracts «ODCS v3 YAML»
> - Données brutes (ERP, CRM, SoR)
> - Moteur MDM «Golden Records»
> - Couche sémantique «MetricFlow / Views»
> - Graphe métier «Golden Context»
> - Ontologie métier «OWL 2 / SHACL»
> - Tableaux de bord BI
> - «Usage humain»
> - Agentic RAG &
> - Text-to-SQL
> - MCP Gateway
> - (Ch. 04)
> - Acteurs cognitifs
> - «Agents»
> - qualité /sensibilité résout types / SLA
> - alimente
> - valide SHACL
> - KPI uniques vues /jointures
> - relations
> - expose
> - contexte

*Fig. 23. – Chaîne de souveraineté sémantique : des contrats de données ODCS et du MDM à la consommation agentique*

> **Arbitrage EA / SA** — Interdire de redéfinir des indicateurs métier ou des entités maîtresses dans les prompts d’agents ou des index vectoriels détachés de la gouvernance de données [100] [101]. L’`EA` rattache la propriété des contrats `ODCS` [106], des couches sémantiques (`MetricFlow` / vues sémantiques) [113] [101], du `MDM` et de l’ontologie `OWL 2` [116] aux *Data Owners* métier afin de maintenir une source de vérité unique entre `BI` et agents. Le `SA` couple les outils `MCP` et le `Text-to-SQL` exclusivement à ces couches gouvernées, interdit l’indexation de jeux sans contrat `ODCS` valide et exécute des contrôles `SHACL` avant toute publication dans le graphe d’entreprise [115].

## 6.4 Gouvernance mémorielle : propagation des ACL, prévention de l’empoisonnement et isolation multi-locataires

### 6.4.1 Failles vectorielles (OWASP LLM08:2025) et propagation des ACL

Les index documentaires et mémoires épisodiques regroupent des données de sensibilité inégale (procédures publiques, contrats confidentiels, dossiers RH). Or, la transformation d’un texte en vecteur numérique ne préserve pas nativement les listes de contrôle d’accès (`ACL`) du système source [114]. La catégorie `OWASP LLM08:2025 Vector and Embedding Weaknesses` identifie cinq menaces critiques sur cette couche : la divulgation non autorisée par défaut d’alignement des `ACL`, les fuites inter-locataires et conflits de fédération, l’inversion d’embeddings permettant de reconstituer les textes sources, l’empoisonnement des données à l’ingestion (comme du texte invisible injecté dans un document) et l’altération comportementale du modèle [114].

L’indexation sous un compte de service unique sans filtrage au moment de la requête expose immédiatement l’agent au risque de divulgation transversale [105] [114]. Deux mécanismes éprouvés rétablissent l’étanchéité :

1. **Le filtrage par attributs de principaux sur l’index (*Security Filter Pattern*)** associe à chaque fragment les identifiants d’utilisateurs ou de groupes autorisés et impose une clause performante telle que `search.in` sur chaque requête [117]. Comme le rappelle la documentation `Azure AI Search`, ces chaînes indexées ne constituent pas une authentification native : le service appelant doit authentifier l’utilisateur, résoudre ses groupes auprès du fournisseur d’identité (via délégation `OBO`, détaillée au chapitre 10), rejeter toute requête non filtrée et synchroniser les révocations [117].
2. **L’autorisation relationnelle fine (**`ReBAC`**) externe via** `OpenFGA` — inspirée de `Google Zanzibar` et hébergée à la `CNCF` — gère l’héritage hiérarchique complexe (dossiers, groupes imbriqués, partages directs sur `SharePoint`, `Google Drive` ou `Confluence`) [105]. Selon le profil de sélectivité, le `SA` choisit entre le **pré-filtrage** via `ListObjects` injecté en filtre vectoriel (idéal lorsque l’utilisateur n’accède qu’à une petite fraction du corpus afin de garantir un top-*K* complet, bien que plus lourd sur des relations `and` ou `but not`) et le **post-filtrage** sur un sur-échantillon de `2×` à `3×` candidats validés en lot via `BatchCheck` [105]. Pour les corpus soumis à révocations fréquentes, l’index local synchronisé via `GET /changes` est doublé d’un ultime `/check` sur les candidats retenus [105].

### 6.4.2 Prévention de l’empoisonnement mémoriel (ASI06) : menaces et gardes d’exécution

Contrairement aux injections éphémères, l’empoisonnement de mémoire persistante (`OWASP ASI06: Memory & Context Poisoning`) grave une altération durable dans l’état de l’agent [118]. Trois travaux de sécurité démontrent l’efficacité redoutable de cette classe d’attaques :

1. `PoisonedRAG` modélise la corruption de base `RAG` comme une optimisation conjointe et prouve que l’injection de **cinq textes malveillants** par question cible dans un corpus de millions de documents suffit à atteindre **90 %** de taux de succès pour imposer la réponse voulue, tout en échappant aux filtres simples de perplexité [119].
2. `AgentPoison` implante des portes dérobées dans la mémoire à long terme ou les bases `RAG` d’agents autonomes sans modifier ni ré-entraîner le modèle [102]. Par optimisation contrainte de déclencheurs dans un sous-espace d’embeddings, l’attaque obtient plus de **80 %** de succès avec un taux d’empoisonnement sous **0,1 %** et moins de **1 %** de dégradation sur requêtes légitimes [102].
3. `MINJA` (*Memory Injection Attacks via Query-Only Interaction*) démontre qu’un attaquant dépourvu d’accès direct en écriture peut empoisonner la mémoire d’un agent par de simples requêtes conversationnelles, en l’amenant à enregistrer des étapes de pontage logique (*bridging steps*) raccourcies progressivement jusqu’à détourner les requêtes futures d’autres victimes [103].

La parade sécurise le chemin d’écriture en plus du chemin de lecture [114] [118]. Le projet `OWASP Agent Memory Guard` (référence `ASI06`) interpose un garde d’exécution inspectant toute écriture avant persistance pour bloquer ou mettre en quarantaine les directives malveillantes [118]. Ce contrôle s’appuie sur quatre règles : étiquetage de provenance distinguant les faits `SoR` des sources externes non fiables [114] ; journalisation par empreinte cryptographique permettant le retour arrière par instantané (*snapshot rollback*) [118] ; interdiction d’alimenter une mémoire épisodique partagée entre utilisateurs à partir d’interactions non vérifiées (bloquant `MINJA`) [103] ; et extraction documentaire brute ignorant le texte caché lors de la vectorisation [114].

### 6.4.3 Isolation multi-locataires : Silo, Bridge, Pool, HNSW partitionné et RLS

Qu’il s’agisse de clients externes sur une plateforme mutualisée ou de lignes d’affaires cloisonnées, le partage physique d’index ou de mémoires expose à trois risques : fuite transversale [114], contention de voisin bruyant (*noisy neighbor*) et distorsion statistique des scores lexicaux [120] [121].

Transposant les régimes `Silo`, `Pool` et `Bridge` de l’`AWS SaaS Lens` [120], l’architecte ajuste l’isolation au risque : le régime `Pool` mutualise l’index sous un filtre `tenant_id` (coût minimal mais vigilance sur la contention), le régime `Silo` dédie base, collection et chiffrement (isolation maximale à coût fixe élevé), et `Bridge` mutualise par défaut tout en isolant les locataires critiques [120].

Deux moteurs matérialisent ces régimes :

1. **Dans** `Qdrant`, multiplier les collections au-delà de quelques centaines d’entités est coûteux (`Qdrant Cloud` plafonne par défaut à 1 000 collections par grappe) [121]. En mode `Pool`, l’index `is_tenant: true` (`v1.11.0+`) co-localise les vecteurs sur disque, tandis que `m: 0` et `payload_m: 16` remplacent le graphe `HNSW` global par des sous-graphes isolés par locataire [121]. En mode `Bridge`, `sharding_method: CUSTOM` promeut les grands comptes vers des *shards* dédiés par `shard_key`, et le paramètre `idf` (`v1.19.0+`) isole les statistiques `BM25` par locataire [121].
2. **Dans** `PostgreSQL` **(**`RLS`**)**, `ALTER TABLE ... ENABLE ROW LEVEL SECURITY` impose un refus par défaut et évalue les prédicats par commande (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) avant toute condition ou fonction non `LEAKPROOF` issue de la requête [122].

> **[Figure]**
> - Utilisateur (Jeton OBO)
> - Agent Harness
> - Garde mémoire
> - (Policy / ASI06)
> - OpenFGA
> - (ReBAC) Stockage vectoriel et épisodique isolé
> - Utilisateur (Jeton OBO) Agent Harness Garde mémoire
> - (Policy / ASI06)
> - OpenFGA
> - (ReBAC)
> - Stockage vectoriel et épisodique isolé
> - Flux A — Récupération gouvernée par ACL (Pre-filtering / Post-filtering)
> - 1 Requête métier (mandat OBO)
> - 2 ListObjects(user, "viewer", "doc")
> - 3 ID autorisés [doc_12, doc_48]
> - 4 Recherche hybride (tenant_id = T1 AND doc_id IN autorisés)
> - 5 Fragments cloisonnés (HNSW + IDF par locataire)
> - 6 BatchCheck(user, "viewer", candidats) [contrôle de fraîcheur si révocations]
> - 7 Verdict autorisé
> - Flux B — Écriture protégée contre l'empoisonnement (Hot Path / Async)
> - 8 Propose écriture mémoire (source, locataire T1, contenu)
> - 9 Vérifie provenance, confiance et détecte directives injectées
> - alt [Contenu sain et provenance attestée]
> - 10 Écrit sous tenant_id = T1 avec empreinte et horodatage
> - 1 1 Confirmation indexée
> - [Contenu suspect ou origine non fiable]
> - 12 Rejet ou mise en quarantaine (audit immuable)

*Fig. 24. – Séquence de propagation des ACL (OpenFGA), garde d’écriture anti-empoisonnement et isolation multi-locataires*

| Régime | Implémentation type | Frontière et impact | Contention / `IDF` | Profil `FinOps` | Cas d’usage cible |
| --- | --- | --- | --- | --- | --- |
| `Pool` logique | Collection unique avec `is_tenant: true` ou `PostgreSQL RLS` | Cloisonnement logique ou moteur ; exige filtrage systématique | Risque de contention `CPU` /E/S et biais `IDF` sans scoping [121] | Coût unitaire minimal, passe au-delà de `1 000` locataires [120] [121] | Équipes internes ou locataires standards homogènes |
| `Bridge` à paliers | `HNSW` cloisonné (`m: 0`, `payload_m`) + *custom shards* sélectifs | Sous-graphes étanches et séparation physique des grands comptes | Contenu pour les locataires sur *shard* dédié [121] | Mutualisation par défaut avec palier dédié facturable [120] | Plateforme mixant nombreux petits domaines et comptes critiques |
| `Silo` physique | Base, collection ou grappe dédiée + clé de chiffrement propre | Isolation matérielle/cryptographique complète [120] | Nul ; ressources, graphes et statistiques dédiés | Surcoût fixe élevé par entité, gestion de flotte plus lourde [120] | Données hautement réglementées (santé, finance souveraine) |

*Tableau 6.3 — Arbitrage d’isolation multi-locataires pour les index vectoriels et les mémoires cognitives d’entreprise.*

> **Arbitrage EA / SA** — Proscrire tout index vectoriel partagé sans propagation des `ACL` à la requête et interdire le partage en écriture d’une mémoire épisodique entre utilisateurs sans validation de provenance [105] [114] [103]. Le `SA` arbitre entre pré-filtrage `OpenFGA ListObjects` et post-filtrage `BatchCheck` (`2×–3×`), active `RLS` sur tout stockage relationnel et configure le partitionnement `is_tenant` / `payload_m` / `idf` ou le sharding à paliers `Bridge` [105] [121] [122]. L’`EA` impose le régime `Silo` physique dès que s’appliquent des exigences strictes de souveraineté ou de conformité (données de santé, secrets d’affaires, Loi 25 traitée au chapitre 12) et exige une inspection anti-`ASI06` doublée d’un audit immuable des écritures persistantes [118].

## Synthèse et transition vers la Partie III

Avec la maîtrise de l’ingénierie du contexte, de l’`Agentic RAG` fédéré, de la souveraineté sémantique et de la gouvernance mémorielle, ce chapitre clôt la Partie II dédiée à l’interopérabilité. Le Plan 3 dispose désormais de connecteurs verticaux normalisés (`MCP`, chapitre 04), de protocoles horizontaux entre agents (`A2A` et `AGNTCY`, chapitre 05) et d’un substrat de mémoire et de connaissances gouverné et sécurisé (chapitre 06).

Reste alors le défi central de la dynamique collective : comment orchestrer ces agents outillés et contextualisés sur des processus complexes sans explosion des coûts ni dérive d’objectif (`Goal Drift`) ? Quand adopter une topologie dirigée par graphe face à une chorégraphie réactive sur *Event Mesh*, et comment garantir une reprise transactionnelle sans faille ? La Partie III répond à ces questions dès le chapitre 07 avec l’étude des patrons d’orchestration multi-agents.
