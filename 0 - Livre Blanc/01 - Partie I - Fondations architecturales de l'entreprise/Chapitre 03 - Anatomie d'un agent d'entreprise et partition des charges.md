# Chapitre 3 — Anatomie d’un agent d’entreprise et partition des charges de travail : la règle hybride 80/20

Les deux chapitres précédents ont établi le cadre macroscopique de l’entreprise agentique : la rupture épistémique introduite par les composants probabilistes entre les systèmes d’engagement (`SoE`) et les systèmes d’enregistrement (`SoR`), puis l’urbanisation du portefeuille en quatre plans découplés. Passer à l’ingénierie concrète exige maintenant d’ouvrir la « boîte noire » de l’unité d’exécution élémentaire : l’agent autonome unitaire. Sur le terrain, les échecs en production proviennent rarement d’un déficit d’intelligence brute du modèle, mais d’une confusion architecturale sur la frontière entre raisonnement statistique et logiciel déterministe [37] [38].

Tout agent d’entreprise robuste repose sur un ou plusieurs modèles d’inférence encapsulés dans un **noyau d’exécution d’agent** (`Agent Harness`) déterministe et confinés dans un environnement système durci [39] [40]. Pour l’architecte de solutions (`SA`), la fiabilité de cette unité dépend de sa boucle de contrôle locale, de son confinement, de l’allocation frugale des modèles et du typage strict de ses interfaces [41] [42]. Pour l’architecte d’entreprise (`EA`), cette anatomie détermine la maîtrise des coûts variables d’inférence (`FinOps`), l’auditabilité des décisions automatisées et la portabilité face à l’obsolescence rapide des modèles [41] [38].

Ce chapitre décompose l’architecture d’un `Agent Harness` et ses enveloppes durcies (`SHADI`, `gVisor`, `Firecracker`), établit la cascade entre `frontier LLMs`, `SLMs` et modèles d’ancrage, formalise la règle hybride **80/20** entre flux déterministes et nœuds cognitifs, puis codifie les contrats typés par `JSON Schema` et décodage contraint. L’analyse porte strictement sur l’agent unitaire et la frontière déterministe/probabiliste; les protocoles réseau relèvent de la Partie II et l’`AI Gateway` mutualisée est traitée au chapitre 13.

## 3.1 Anatomie d’un Agent Harness de production et environnements d’exécution durcis (SHADI)

Un modèle de langage isolé demeure un prédicteur de jetons sans état, dépourvu de mémoire persistante, d’accès aux outils et de conscience des politiques de sécurité. Pour en faire un composant exploitable, il faut l’enchâsser dans un **noyau d’exécution d’agent** (`Agent Harness`), c’est-à-dire la boucle logicielle déterministe qui pilote l’inférence, gère le contexte, applique les plafonds de consommation, valide les appels d’outils et confine les effets système [37] [39] [43].

### 3.1.1 Décomposition fonctionnelle de l’`Agent Harness`

Les retours d’ingénierie sur les agents longue durée montrent qu’un `Agent Harness` articule quatre sous-systèmes déterministes [37] [39] :

1. **Boucle de contrôle et garde-fous de budget (*control loop*)** : elle exécute le cycle perception-raisonnement-action (patron `ReAct` lors d’explorations ouvertes) dans une machine à états bornée [37] [44]. Elle maintient des plafonds explicites d’itérations, de jetons et de latence pour stopper toute boucle circulaire ou erreur répétée d’outil, capturant la trace d’échec afin d’engager un repli déterministe [39] [43].
2. **Assembleur de contexte et sessions longues** : lorsque les tâches dépassent une fenêtre de contexte, la cohérence se dégrade sans discipline de passation [39]. Les travaux d’Anthropic préconisent
  de séparer un agent initialiseur d’un agent d’exécution incrémentale consignant des artefacts de passation structurés (journaux de progression, état des vérifications) entre fenêtres successives [39].
3. **Sélecteur d’inférence** : cette abstraction découple le code applicatif d’un fournisseur donné, aiguille chaque appel (`SLM` spécialisé ou `frontier LLM`) et impose le décodage contraint [41] [42], dialoguant à l’échelle de l’entreprise avec l’`AI Gateway` (chapitre 13).
4. **Répartiteur d’outils et vérification** : il expose les capacités autorisées, valide les arguments avant exécution et retourne des diagnostics exploitables [37] [43]. L’ajout de vérificateurs déterministes indépendants (analyseurs statiques, tests) — ou d’évaluateurs isolés du contexte générateur — évite que le modèle n’auto-valide ses erreurs [39].

L’`Agent Harness` concrétise ainsi les systèmes d’IA composés (*Compound AI Systems*) : la fiabilité en production provient du couplage entre inférence et logiciel déterministe [38]. À l’inverse, accumuler dans le harnais des rustines propres aux défauts d’un modèle donné crée un couplage fragile qui devient caduc dès la version suivante [37].

> **[Figure]**
> - Agent Harness (Boucle applicative déterministe)
> - [container]
> - Enveloppe d'exécution
> - durcie (SHADI / Bac à
> - sable) [system]
> - «component» Boucle de contrôle
> - [Machine d'états / Budget]
> - Tours, plafonds et reprise
> - «component» Assembleur contexte
> - [Fenêtre & compaction]
> - Mémoire travail et passation
> - «component» Sélecteur inférence
> - [Cascade SLM / LLM]
> - Aiguille SLM ou frontier LLM
> - «component» Répartiteur d'outils
> - [JSON Schema]
> - Valide arguments avant appel
> - «component» Mémoire chiffrée
> - [SQLCipher]
> - État chiffré au repos
> - «component» Dérivation identité
> - [HKDF-SHA256]
> - did:key par session
> - «component» Porte de secrets
> - [agent_secrets]
> - Trousseau attesté
> - «component» Confinement noyau
> - [Landlock / gVisor / KVM]
> - Syscalls, fichiers, réseau
> - «external_system» Modèles d'inférence
> - SLM local / Frontier LLM (ch. 13)
> - «external_system» Outils et SI cible
> - Code, shell, API (Partie II)
> - Compacte Étape cognitive Invoque
> - Lit / écrit
> - Atteste Scelle
> - Exécute Appel CFG
> - Sous politique

*Fig. 9. – Architecture C4 Component d’un Agent Harness de production et de son confinement SHADI*

> **Arbitrage EA / SA** — Imposer un `Agent Harness` minimal, composable et agnostique du fournisseur (`control loop` bornée, artefacts de passation persistants, validateur d’outils et journalisation structurée) [37] [39]. Le `SA` réduit le couplage aux particularités d’un modèle; l’`EA` protège les investissements applicatifs face au renouvellement rapide des moteurs d’inférence.

### 3.1.2 Menaces d’exécution unitaire selon l’`OWASP`

Dès qu’un agent exécute du code, manipule des fichiers locaux ou interroge des outils, la surface d’attaque s’élargit brutalement. Le référentiel *Agentic AI – Threats and Mitigations* de l’`OWASP` identifie trois risques majeurs au niveau du runtime unitaire [43] :

- **Exécution de code à distance inattendue (**`RCE`**)** : une injection indirecte dans un document lu par l’agent peut détourner son interpréteur ou son accès `shell` pour lancer des commandes arbitraires sur l’hôte [43].
- **Détournement d’outils et fuite de secrets (**`Tool Misuse`**)** : un agent lancé dans un processus ordinaire accède souvent aux variables d’environnement et aux clés du poste ou du microservice, exposant ces secrets en cas de détournement d’objectif [40] [43].
- **Autonomie excessive et déni de portefeuille** : sans plafonds de ressources ni validations humaines sur les opérations destructrices, une boucle non maîtrisée engendre des coûts explosifs et des mutations irréversibles [43].

L’`OWASP` prescrit de ne jamais confier la sécurité d’exécution au prompt système, d’interdire les évaluations dynamiques non bornées (`eval()`), d’isoler chaque environnement dans un bac à sable strict et d’appliquer des identités non humaines (`NHI`) à privilège minimal [40] [43].

### 3.1.3 Environnements durcis sur hôte : l’architecture `SHADI`

Lorsque des agents opèrent près de dépôts locaux, de postes d’ingénierie ou d’identifiants sensibles, les bacs à sable distants éphémères ne suffisent pas [40]. Le projet open source **SHADI** (*Secure Host for Agentic AI Dynamic Instantiation*), développé en `Rust` au sein de l’écosystème `AGNTCY` (Linux Foundation), établit une frontière durcie locale sur cinq couches cryptographiques et système [40] :

1. **Identité dérivée vérifiée** : à partir d’une racine humaine (`SLIM_HUMAN_SEED`), `SHADI` dérive de façon déterministe par `HKDF-SHA256` une identité `did:key` (`Ed25519`) propre à chaque instance d’agent enfant, éliminant les secrets partagés [40].
2. **Porte de secrets (**`agent_secrets`**)** : les jetons restent scellés dans le trousseau du système d’exploitation (avec intégration optionnelle `1Password`) et ne sont injectés dans l’environnement qu’au démarrage d’une session attestée [40].
3. **Confinement noyau OS (**`shadi_sandbox`**)** : piloté par l’utilitaire `shadictl` (permettant notamment d’inspecter et de simuler les règles avant lancement via `--print-policy`), `SHADI` applique des profils portables (`strict`, `balanced`, `connected`) ou des politiques JSON explicites directement via les primitives natives du noyau hôte — `Landlock` (Linux), `Seatbelt` (macOS) et `AppContainers` (Windows) — pour borner lectures, écritures et sorties réseau [40].
4. **Mémoire locale chiffrée (**`shadi_memory`**)** : une brique `Rust` chiffrée par `SQLCipher` protège l’état, le contexte et l’historique persistés sur disque entre deux sessions contre toute inspection non autorisée [40].
5. **Encapsulage** `AgentBridge` : des outils de développement en ligne de commande existants sont enveloppés comme écouteurs authentifiés par `DID` tout en restant soumis au confinement noyau [40].

Le transport réseau associé (`SLIM` /`MLS` et `A2A`) relève du chapitre 5 et l’attestation de grappe (`SPIFFE/SPIRE` et `OAuth 2.0 OBO`) du chapitre 10. Pour l’`EA`, `SHADI` protège les postes d’ingénierie contre les fuites de clés locales avec une empreinte opérationnelle légère [40].

### 3.1.4 Confinement en grappe : `Agent Sandbox`, `gVisor` et `Firecracker`

En environnement serveur multi-locataires, exécuter du code généré dans un conteneur `runc` expose le noyau Linux partagé aux évasions, tandis que les objets Kubernetes `Deployment` et `Job` gèrent mal les sessions agentiques avec état à identité réseau fixe [45] [46]. Le projet `kubernetes-sigs/agent-sandbox` comble ce manque via quatre ressources personnalisées : `Sandbox` (unité persistante à pause/reprise), `SandboxTemplate` (image et `runtimeClassName`), `SandboxWarmPool` (bassin préchauffé ramenant le démarrage sous la seconde) et `SandboxClaim` (allocation transactionnelle) [45].

Sous cette orchestration, deux moteurs d’isolation s’imposent en production :

- `gVisor` interpose un noyau en espace utilisateur en `Go` (`Sentry`) filtré par `seccomp-bpf`, tandis qu’un mandataire séparé (`Gofer`) contrôle les accès fichiers via `9P` sur socket Unix, sans virtualisation imbriquée [45] [46].
- `Firecracker` déploie des microVM sous hyperviseur `KVM` avec noyau invité dédié : sa spécification vérifiée en intégration continue garantit un démarrage (`InstanceStart` → `/sbin/init`) en au plus **125 ms** et un surcoût `VMM` d’au plus **5 MiB** (1 vCPU / 128 MiB) [47].

| Critère | Conteneur `runc` | `SHADI` (hôte local durci) | `gVisor` (`Sentry` + `Gofer`) | MicroVM `Firecracker` (`KVM`) |
| --- | --- | --- | --- | --- |
| Frontière d’isolation | Noyau hôte partagé | `Landlock`, `Seatbelt`, `AppContainers` | Noyau espace utilisateur `Go` + `seccomp-bpf` | Hyperviseur matériel `KVM` et noyau invité |
| Délai de démarrage | Rapide (partage du noyau sur image locale) | Quasi instantané (enveloppe de processus OS) | Sous la seconde via `SandboxWarmPool` | ≤ 125 ms (`InstanceStart` → `/sbin/init`) |
| Surcoût mémoire | Négligeable | Minimal (`Rust` + `SQLCipher`) | Faible à modéré (`Sentry` + `Gofer`) | ≤ 5 MiB pour le `VMM` (1 vCPU / 128 MiB) |
| Secrets et état | Risque d’exposition `env` | Porte `agent_secrets` + `HKDF-SHA256` | Gérée par l’orchestrateur de grappe | Isolation mémoire matérielle par microVM |
| Cas d’usage cible | Proscrit pour code généré | Postes d’ingénierie et données locales | Charges multi-locataires sans `KVM` imbriqué | Exécution de code tiers non fiable |

*Tableau 3.1 — Matrice comparative des technologies de confinement pour agents unitaires.*

> **Arbitrage EA / SA** — Proscrire le conteneur `runc` nu pour tout agent doté d’un interpréteur de code ou d’un `shell` [45] [43]. Déployer `SHADI` près des environnements locaux [40], et imposer `gVisor` ou `Firecracker` via `SandboxWarmPool` en grappe afin de conjuguer isolation forte et latence sous la seconde [45] [46] [47].

## 3.2 Typologie et spécialisation des modèles : frontier LLMs, SLMs spécialisés et cascade d’inférence

Allouer systématiquement un grand modèle frontalier (*frontier LLM*) à chaque étape cognitive d’un agent pénalise autant la latence `SA` que l’équilibre budgétaire `EA`. L’architecture des systèmes composés (`Compound AI Systems`) privilégie au contraire l’assemblage de modèles spécialisés et de routines déterministes selon les caractéristiques de chaque sous-tâche [38].

### 3.2.1 Petits modèles spécialisés (`SLM`) contre `frontier LLMs`

L’analyse publiée par des chercheurs de `NVIDIA` et de Georgia Tech montre que les appels d’un agent d’entreprise consistent majoritairement en sous-tâches répétitives et étroitement bornées — extraction ciblée, routage d’intention, génération `JSON` et remplissage d’arguments d’outils — plutôt qu’en dialogue ouvert [41]. Sur ces tâches focalisées, les petits modèles de langage (`SLM`, typiquement sous 10 à 14 milliards de paramètres) rivalisent avec les grands modèles généralistes antérieurs tout en apportant des gains de **10× à 30×** sur le coût par jeton, la latence et la consommation énergétique [41]. Leur faible taille facilite aussi le réglage fin métier sur des grappes souveraines locales, permettant aux équipes de convertir progressivement les étapes stables initialement prototypées sur `frontier LLM` vers des `SLM` spécialisés, tandis que les grands modèles demeurent réservés aux étapes de synthèse complexe ou d’ambiguïté élevée [41].

Cette spécialisation transforme aussi la gestion de la dette cognitive introduite au chapitre 1 : un `SLM` figé et versionné en interne pour une tâche d’extraction étroite subit beaucoup moins de dérives comportementales imprévues qu’un modèle généraliste mutualisé mis à jour unilatéralement par un fournisseur tiers [41] [38]. Pour l’`EA`, ce découplage préserve à la fois la prévisibilité `FinOps` et la souveraineté opérationnelle sur les traitements à haut volume.

### 3.2.2 Récupération en deux étages (`Bi-Encoder` et `Cross-Encoder`)

La performance et le coût d’un nœud génératif dépendent étroitement de la concision du contexte injecté. Le pipeline de référence en deux étages combine deux modèles non génératifs spécialisés [48] :

1. **Rappel par** `Bi-Encoder` : il encode séparément documents (pré-indexés hors ligne dans une base vectorielle) et requête en vecteurs denses, filtrant rapidement de vastes corpus vers une liste courte de 50 à 100 candidats [48]. Faute d’attention directe entre jetons de la requête et du document, il peine toutefois sur les négations ou contraintes logiques fines [48].
2. **Réordonnancement par** `Cross-Encoder` : il évalue simultanément chaque paire `[requête, candidat]` par attention croisée complète et ne conserve que les 3 à 5 meilleurs extraits pour le modèle génératif [48]. Comme il ne peut être pré-indexé et que son coût croît proportionnellement au nombre `K` de candidats, limiter `K ≤ 100` évite toute dérive de latence tout en réduisant drastiquement le volume de jetons soumis au `LLM` [48]. L’arrimage aux graphes de connaissances et aux `ACL` d’entreprise est développé au chapitre 6.

### 3.2.3 Cascades d’inférence (`FrugalGPT`) et routage amont (`RouteLLM`)

Deux patrons optimisent dynamiquement le compromis coût/précision entre `SLM` et `frontier LLM` à l’intérieur du harnais :

> **[Figure]**
> - Boucle Agent Harness
> - Récupération 2 étages (Bi-Encoder + Cross-Encoder)
> - Routeur / Cascade
> - (SLM vs Frontier)
> - SLM spécialisé (≤ 14B paramètres)
> - Frontier LLM (Escalade complexe)
> - Boucle Agent Harness
> - Récupération 2 étages (Bi-Encoder + Cross-Encoder)
> - Routeur / Cascade
> - (SLM vs Frontier)
> - SLM spécialisé (≤ 14B paramètres)
> - Frontier LLM (Escalade complexe)
> - 1 Requête métier normalisée
> - 2 Bi-Encoder (rappel vectoriel top 50-100)
> - 3 Cross-Encoder (réordonnancement top 3-5)
> - 4 Extraits contextuels compacts
> - 5 Tâche typée + contexte ancré
> - 6 Inférence rapide (ex. extraction / routage JSON)
> - 7 Réponse structurée + score de confiance
> - alt [Confiance >= seuil et schéma valide]
> - 8 Résultat retenu (coût et latence réduits)
> - [Ambiguïté ou échec de validation]
> - 9 Escalade avec trace et contexte borné
> - 10 Raisonnement résiduel structuré
> - 1 1 Résultat consolidé

*Fig. 10. – Séquence de récupération en deux étages et cascade d’inférence SLM vers Frontier LLM*

Dans une **cascade d’inférence** (`FrugalGPT` [49]), illustrée par le diagramme de séquence ci-dessus, le harnais soumet d’abord la requête à un modèle économique (`SLM`), puis contrôle un score de confiance ou la validité structurée du résultat : seule la fraction incertaine est escaladée vers le modèle frontalier [41] [49]. Combinée à l’adaptation de prompt et à l’approximation, cette stratégie atteint la précision du meilleur modèle individuel tout en réduisant le coût jusqu’à **98 %**, ou améliore la précision de `GPT-4` de **4 %** à budget égal [49]. Elle impose toutefois une pénalité de latence additive sur les requêtes escaladées, puisqu’un premier appel a déjà été consommé avant le repli.

À l’inverse, le **routage prédictif amont** (`RouteLLM` [50]) entraîne un routeur léger sur des données de préférence humaine (comme `Chatbot Arena`) enrichies par augmentation de données afin de diriger chaque requête dès l’entrée vers le modèle économique ou le modèle fort, évitant le coût de latence d’un double appel sur les cas difficiles. `RouteLLM` réduit les dépenses d’inférence de **plus de 50 %** (facteur supérieur à **2×**) à qualité comparable tout en transférant efficacement vers de nouveaux couples de modèles lors des

évolutions de portefeuille [50]. La mutualisation réseau de ces routeurs dans une `AI Gateway` d’entreprise relève du chapitre 13.

| Famille de modèles | Rôle unitaire | Ordre de grandeur coût / latence | Atout principal | Garde-fou `SA` / `EA` |
| --- | --- | --- | --- | --- |
| `Bi-Encoder` | Rappel vectoriel (top 50–100) | Très bas; recherche rapide sur index vectoriel | Pré-indexation sur vastes corpus documentaires | Coupler au `Cross-Encoder` pour contraintes fines |
| `Cross-Encoder` | Réordonnancement fin (top 3–5) | Modéré; proportionnel au lot `K` évalué | Attention croisée haute précision | Plafonner `K ≤ 100` sous budget de latence p95 |
| `SLM` (≤ 10–14B) | Extraction, routage, `JSON`, outils | 10× à 30× moindre qu’un `LLM` généraliste | Spécialisable et souverain sur site | Escalade vers modèle fort sur faible confiance |
| `Frontier LLM` | Ambiguïté élevée et synthèse | Élevé; dépend du volume de jetons générés | Forte généralisation *zero-shot* | Restreint aux cas justifiés (`FinOps`) |

*Tableau 3.2 — Matrice d’allocation des familles de modèles dans un agent unitaire.*

> **Arbitrage EA / SA** — Interdire par défaut l’usage d’un `frontier LLM` sur les tâches répétitives et bornées (extraction, classification, formatage `JSON` ou remplissage d’arguments) dès que des `SLM` spécialisés atteignent la précision requise [41], et fixer en politique `FinOps` interne un seuil de revue dès qu’un nœud dépasse quelques milliers d’appels mensuels. Le `SA` expose le routage et la cascade derrière une interface unique dans le harnais; l’`EA` exige la modélisation de ces cascades dans le dossier `FinOps` (chapitre 12) tout en réservant la passerelle réseau partagée au chapitre 13.

## 3.3 Ingénierie de la partition 80/20 entre flux déterministes et nœuds cognitifs

Déléguer l’ensemble d’un processus métier à une boucle `ReAct` libre accroît la latence, multiplie les coûts d’inférence, élargit la surface d’injection de prompt et compromet la reproductibilité exigée lors des audits [37] [43] [44]. La **règle hybride 80/20** codifie la séparation disciplinée des responsabilités.

### 3.3.1 Propriété du flux de contrôle et règle 80/20

Anthropic distingue les **workflows** (où des chemins de code prédéfinis orchestrent modèles et outils) des **agents** (où le modèle contrôle dynamiquement sa propre trajectoire et ses appels d’outils) [37]. Google Cloud recommande pareillement de conserver le routage et les garde-fous dans du code déterministe dès que les étapes sont prévisibles, en réservant le `LLM` à l’interprétation, à l’extraction ou à la synthèse [44].

Selon la **règle hybride 80/20**, environ **80 %** du traitement d’un processus d’entreprise — normalisation d’entrée, validations de schémas, règles réglementaires et calculs financiers, aiguillages conditionnels,

journalisation et écritures dans les `SoR` — demeure dans du **code déterministe**, tandis qu’environ **20 %** — les points confrontés à du langage ambigu ou à des exceptions non structurées — mobilisent un **nœud cognitif** (le plus souvent sans boucle, exceptionnellement en boucle bornée) [37] [38] [44]. Le ratio varie selon la nature du dossier (moins de 10 % en règlement financier, jusqu’à 30 % en analyse documentaire), mais le principe demeure invariable : le déterminisme est le défaut architectural et le probabilisme l’exception justifiée.

### 3.3.2 Arbre de tri en cinq régimes et décomposition mixte

Chaque sous-tâche métier est classée au moyen de l’arbre de décision ci-après afin d’appliquer la complexité minimale viable [37] [44].

*Fig. 11. – Arbre de décision d’allocation des sous-tâches métier selon la règle hybride 80/20*

Cinq régimes d’exécution en découlent :

1. **Règle métier exacte** : seuils légaux, fiscalité, contrôles d’admissibilité et calculs comptables restent en code pur déterministe [38] [44].
2. **Workflow codé fixe** : les séquences connues d’avance s’appuient sur des machines à états ou graphes programmés offrant testabilité unitaire et latence prévisible [37] [44].
3. **Apprentissage prédictif classique** : les scores tabulaires sans texte libre utilisent des modèles prédictifs classiques, plus rapides et plus explicables qu’un `LLM`.
4. **Nœud** `LLM` **contraint sans boucle** : un appel unique à schéma contraint extrait ou classe un texte libre dans un workflow déterministe sans décider du flux suivant [37] [42].
5. **Boucle agentique bornée** : réservée aux investigations ouvertes où les étapes ne peuvent être figées d’avance, sous plafond strict d’itérations, confinement `SHADI` ou microVM et validation humaine sur action critique [37] [39] [43].

Pour illustrer cette décomposition sur un dossier de réclamation d’assurance commerciale pouvant atteindre 250 k$ CA, une approche naïve « tout-agent » exposerait l’entreprise à un risque critique : une injection dissimulée dans une pièce jointe pourrait altérer le calcul d’indemnité ou déclencher un paiement hors plafond [43]. En appliquant la règle 80/20 dans un graphe mixte à état partagé fortement typé, le harnais sépare : (1) ingestion, vérification d’intégrité et génération d’identifiant de traçabilité en code pur; (2) extraction narrative par un nœud `SLM` contraint en `JSON Schema` [41] [51]; (3) vérification de couverture et calcul exact de franchise sur le `SoR` par moteur de règles déterministe; (4) avis juridique structuré

par `LLM` uniquement si une clause d’exclusion ambiguë est détectée [48] [44]; (5) routage déterministe vers approbation humaine au-delà de 25 k$ CA ou en cas d’ambiguïté [43]; (6) mutation transactionnelle encadrée par exécution durable (chapitre 9); (7) rédaction de notification suivie d’une vérification déterministe des montants numériques avant envoi. Sur le plan `SA`, chaque nœud déterministe reste isolément testable par jeux de tests unitaires et simulacres (*mocks*); sur le plan `EA`, le suivi de la part d’étapes cognitives — maintenue sous le seuil cible de 20 % hors exceptions documentaires — sert d’indicateur de santé architecturale lors des revues de portefeuille.

| Sous-tâche métier | Régime retenu | Part cible | Contrat d’interface | Auditabilité `EA` |
| --- | --- | --- | --- | --- |
| Calculs, seuils légaux, contrôles | Code déterministe / Règles | ~80 % (avec flux) | Fonctions pures, couverture unitaire 100 % | Reproductibilité absolue et preuve triviale |
| Enchaînement nominal, mutations `SoR` | Workflow / Graphe d’états | ~80 % (avec règles) | Transitions codées, idempotence (chap. 9) | Parcours figé sans dérive d’exécution |
| Scoring structuré sans texte | ML prédictif classique | Selon domaine | Vecteurs normalisés et seuils versionnés | Explicabilité statistique et coût négligeable |
| Extraction ou synthèse ciblée | Nœud `LLM` /`SLM` sans boucle | ~15 % | `JSON Schema` (`CFG`) + validateur aval | Entrée/sortie journalisée, zéro autonomie |
| Investigation ouverte multi-outils | Boucle agentique bornée | ~5 % | Plafond d’étapes, confinement, `HITL` | Trace complète de trajectoire et budget fixe |

*Tableau 3.3 — Grille de partitionnement 80/20 des sous-tâches d’un processus métier.*

> **Arbitrage EA / SA** — Exiger en revue d’architecture la justification écrite de toute boucle agentique face à un workflow déterministe ponctué de nœuds `LLM` sans boucle [37] [44]. L’`EA` protège l’intégrité comptable des `SoR` et contient le coût variable d’inférence; le `SA` rétablit la testabilité unitaire de 80 % de la base applicative et isole le non-déterminisme derrière des interfaces typées.

## 3.4 Contrats typés d’entrée/sortie (Structured Outputs et JSON Schema)

La partition 80/20 exige des frontières aussi fiables que des contrats d’API entre les 20 % de nœuds cognitifs et les 80 % de code déterministe. Le simple « JSON Mode » probabiliste des premiers modèles ne garantissait que la validité syntaxique globale du document JSON, sans empêcher l’omission de champs obligatoires, l’inversion de types (une chaîne à la place d’un entier), les virgules excédentaires ou l’invention de propriétés non déclarées [42]. Par conséquent, les équipes applicatives devaient multiplier les parseurs

tolérants, les expressions régulières fragiles et les boucles de réessai coûteuses [42] [51]. Le **décodage contraint** (*constrained decoding*) résout cette fragilité directement au niveau de l’échantillonnage des jetons [42] [52].

### 3.4.1 Mécanisme du décodage contraint et accélération `XGrammar`

Les moteurs de production appliquent un **décodage contraint** directement sur la distribution de probabilité des jetons. `OpenAI Structured Outputs` (via `strict: true`) [42] et le moteur ouvert `XGrammar` [52] compilent le `JSON Schema` cible en une **grammaire hors contexte (**`CFG`**)**, tandis qu’`Anthropic` offre un décodage contraint équivalent par le paramètre `output_config.format` de type `json_schema` [51]. À la différence des automates à états finis simples ou des expressions régulières limités par l’absence de pile pour les objets ou tableaux imbriqués récursivement, une `CFG` modélise exactement l’appariement syntaxique complet [42]. À chaque pas de génération, le moteur applique un masque binaire sur la distribution de logits en forçant à `−∞` (probabilité nulle) tout jeton violant la grammaire, rendant impossible l’émission d’une syntaxe non conforme [42] [52].

Sur grappe souveraine de modèles ouverts, le moteur `XGrammar` (`MLC` / `CMU`) élimine le goulot CPU de cette vérification en séparant le vocabulaire entre jetons indépendants du contexte (précalculés en cache) et jetons dépendants évalués par un automate à pile persistant, recouvrant ce calcul avec l’exécution `GPU` [52]. Il atteint des accélérations allant jusqu’à **100×** par rapport aux moteurs antérieurs de génération guidée, stabilisant le budget de latence sans réessai syntaxique, comme le synthétise la séquence suivante [42] [51] [52].

> **[Figure]**
> - Harnais déterministe (Pydantic / Validateur)
> - Moteur d'inférence
> - (CFG + Cache)
> - Modèle de langage
> - (Logits bruts)
> - Système aval (Workflow / Outil)
> - Harnais déterministe (Pydantic / Validateur)
> - Moteur d'inférence
> - (CFG + Cache)
> - Modèle de langage
> - (Logits bruts)
> - Système aval (Workflow / Outil)
> - 1 Requête + JSON Schema Draft 2020-12 (strict: true)
> - 2 Compile grammaire CFG (si schéma inédit) + mise en cache
> - loop [À chaque jeton généré]
> - 3 Distribution de logits bruts
> - 4 Masque binaire CFG (jetons invalides -> -infini)
> - 5 Échantillonnage syntaxique contraint
> - 6 Charge utile JSON conforme à la grammaire
> - 7 Validation sémantique déterministe (Pydantic / règles)
> - alt [Invariants métier satisfaits]
> - 8 Exécute transition ou appel typé
> - [Violation sémantique ou refus typé]
> - 9 Réessai borné (max N) ou repli déterministe

*Fig. 12. – Séquence d’exécution d’un contrat typé par décodage contraint CFG et validation sémantique*

### 3.4.2 Règles de conception `JSON Schema Draft 2020-12` et validation sémantique

Les contrats s’appuient sur le standard agnostique `JSON Schema Draft 2020-12` (`https://json-schema.org/draft/2020-12/schema`), qui normalise le vocabulaire central de structuration et le vocabulaire de validation des types, bornes et motifs [53]. Pour rester compatibles avec les compilateurs `CFG` en mode `strict: true`, les schémas de production doivent toutefois respecter trois contraintes pratiques [42] [51] :

- **Fermeture et exhaustivité** : déclarer `"additionalProperties": false` sur chaque objet et lister toutes les propriétés dans `"required"`, en représentant les champs facultatifs par union avec `null` (`["string", "null"]`) [42] [51].

- **Exclusion de mots-clés dynamiques** : éviter `allOf`, `if/then/else` et certaines disjonctions `anyOf` à la racine qui déclenchent un rejet `HTTP 400` en mode strict [42].
- **Préchauffage du cache grammatical** : la première soumission d’un schéma inédit subit une latence de compilation `CFG` (de quelques secondes à près d’une minute sur schémas massifs) avant mise en cache [42]; les schémas doivent donc être statiques et versionnés.

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ExtractionDeclarationSinistre",
  "type": "object",
  "additionalProperties": false,
  "required": ["statut_analyse", "categorie_sinistre", "montant_reclame_cad", "motif_escalade"],
  "properties": {
    "statut_analyse": { "type": "string", "enum": ["EXTRAIT", "AMBIGU_ESCALADE", "DONNEES_INSUFFISANTES"] },
    "categorie_sinistre": { "type": ["string", "null"], "enum": ["DEGAT_EAU", "INCENDIE", "BRIS_EQUIPEMENT", null] },
    "montant_reclame_cad": { "type": ["number", "null"] },
    "motif_escalade": { "type": ["string", "null"] }
  }
}
```

L’état explicite `AMBIGU_ESCALADE` évite qu’un modèle contraint n’invente une valeur plausible par défaut faute de porte de sortie typée. Par-dessus tout, le décodage contraint garantit **la forme syntaxique, jamais la véracité factuelle** [42]. Comme l’illustre la séquence ci-dessus, le harnais doit systématiquement coupler la sortie contrainte à un validateur déterministe post-génération — par exemple via `Pydantic`, qui exporte directement des schémas `Draft 2020-12` (`OpenAPI 3.1.0`) via `model_json_schema()` pour garantir une source de vérité unique [54].

Ce validateur déterministe applique quatre contrôles systématiques avant toute transition vers les 80 % de code métier en aval :

1. **Invariants relationnels et temporels** : vérifier par code pur que la date d’un sinistre est cohérente avec la période de couverture du contrat et l’horodatage de déclaration.
2. **Contrôle d’ancrage (*grounding*)** : s’assurer que tout identifiant de clause, référence de police ou montant chiffré retourné correspond effectivement aux extraits fournis ou au `SoR` interrogé.
3. **Boucle de réparation bornée** : si un invariant métier échoue, le harnais réinjecte le diagnostic d’erreur exact dans une tentative de correction strictement plafonnée (typiquement un à deux réessais) afin de prévenir toute dérive de budget [39] [43].
4. **Repli déterministe (*fallback*)** : au-delà du plafond ou sur statut `AMBIGU_ESCALADE`, le workflow oriente automatiquement le dossier vers une file humaine ou un traitement dégradé déterministe [43] [44].

Cette rigueur contractuelle prépare directement le typage des outils `MCP` étudié à la Partie II.

> **Arbitrage EA / SA** — Imposer une **source de vérité unique** par nœud cognitif : générer le contrat `JSON Schema Draft 2020-12` depuis les modèles typés applicatifs (`Pydantic` ou équivalent), tester sa compatibilité `strict: true` en intégration continue et doubler chaque appel contraint d’une

> validation sémantique déterministe [42] [54]. Pour le `SA`, le cache `CFG` reste chaud et les parseurs ne cassent plus; pour l’`EA`, les états explicites d’escalade permettent de mesurer objectivement la précision réelle lors des changements de modèle ou des audits.

## Synthèse architecturale du chapitre

Un agent d’entreprise fiable n’est pas un modèle conversationnel laissé en roue libre, mais un composant logiciel hybride où le raisonnement probabiliste demeure minoritaire et strictement encadré. L’articulation d’un `Agent Harness` minimal et observable, d’un confinement système robuste (`SHADI` en local, `gVisor` ou `Firecracker` via `Agent Sandbox` en grappe), d’une cascade frugale associant `Bi-Encoder` /`Cross-Encoder` et `SLM` /`frontier LLM`, de la partition **80/20** et de contrats `JSON Schema Draft 2020-12` doublés d’une validation sémantique déterministe rend l’agent unitaire composable et auditable. La Partie II ouvre désormais cet agent sur l’extérieur : d’abord verticalement vers les outils et le patrimoine (`MCP`, chapitre 4), puis horizontalement entre agents (`A2A` et `AGNTCY`, chapitre 5) et enfin vers les couches de mémoire et de gouvernance sémantique (chapitre 6).
