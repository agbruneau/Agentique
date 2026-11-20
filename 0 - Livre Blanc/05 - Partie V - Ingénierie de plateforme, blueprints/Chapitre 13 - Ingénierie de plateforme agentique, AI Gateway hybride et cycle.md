# Chapitre 13 — Ingénierie de plateforme agentique, AI Gateway hybride et cycle de vie industriel (GitOps)

Les douze chapitres précédents ont posé les fondations épistémiques, les protocoles ouverts (`MCP`, `A2A`, `AGNTCY`), l’exécution durable, la sécurité `Zero-Trust`, l’observabilité `OpenTelemetry` /`EvalOps` et la gouvernance `FinOps`. Laisser chaque équipe produit réassembler ces briques de façon artisanale reproduirait la fragmentation : chaque domaine recréerait son harnais d’agent, ses connecteurs d’inférence, ses politiques d’accès et ses scripts de déploiement. Selon le programme *DORA*, **90 %** des organisations sondées en 2025 utilisaient une plateforme interne et **76 %** disposaient d’équipes plateformes dédiées ; surtout, DORA démontre empiriquement que lorsque la qualité de la plateforme interne est élevée, l’impact de l’adoption de l’IA sur la performance organisationnelle devient nettement positif [305].

Ce chapitre ouvre la Partie V en traduisant ces exigences en un socle reproductible. En **lecture** `EA`, il arbitre la séparation plateforme/domaines, la souveraineté d’inférence et la gouvernance du portefeuille. En **lecture** `SA`, il spécifie l’`Internal Agentic Platform` **(**`IAP`**)**, l’`AI Gateway` **hybride**, le `GitOps` **cognitif** et le **déploiement progressif** compatible avec les workflows durables en vol. L’instanciation sectorielle bout-en-bout relève du chapitre 14.

## 13.1 Architecture d’une Internal Agentic Platform (IAP) : Golden Paths et séparation plateforme/domaines

### 13.1.1 De l’IDP classique à l’IAP : absorber la charge cognitive extrinsèque

Le livre blanc *Platforms* de la `CNCF` définit une plateforme interne comme un ensemble curaté de capacités exposées en libre-service pour accélérer la livraison applicative [306]. Sur le plan organisationnel, *Team Topologies* fixe le critère de frontière décisif : la **charge cognitive extrinsèque** [307]. Une équipe `stream-aligned` doit consacrer son effort aux règles métier, contrats de domaine et besoins utilisateurs (sa charge intrinsèque), plutôt qu’à la plomberie d’infrastructure [307].

Une plateforme classique (`IDP`) masque déjà Kubernetes, bases de données et CI/CD [306] [305]. À l’ère agentique, cette charge extrinsèque se démultiplie : orchestration `Temporal` ou `Restate` (chapitre 9), identités `SPIFFE` et `OAuth 2.0 OBO` (chapitre 10), passerelle `MCP` (chapitre 4), traces `OpenTelemetry GenAI` (chapitre 11), imputation `FOCUS` (chapitre 12), fiches `OASF` (chapitre 5) et ordonnancement GPU. L’`Internal Agentic Platform` **(**`IAP`**)** encapsule cette complexité transversale dans un produit interne cohérent [306] [307] :

1. **Gestion en produit interne (**`Platform-as-a-Product`**)** : l’équipe plateforme traite les domaines en clients internes, mesure adoption volontaire et délai de livraison, et maintient des API stables au lieu d’opérer un guichet de billets manuel [306] [305].
2. **Plateforme minimale viable (**`Thinnest Viable Platform`**,** `TVP`**)** : l’`IAP` ne bâtit que les capacités levant des irritants récurrents, évoluant par traction réelle afin d’éviter la bureaucratie technique [307].
3. **Modes d’interaction ciblés** : l’équipe plateforme opère en mode `X-as-a-Service` au quotidien, passe en `Collaboration` pour co-concevoir de nouvelles briques, et s’appuie sur des équipes `Enabling` pour diffuser les pratiques `EvalOps` et `80/20` [307].

### 13.1.2 Anatomie des Golden Paths exécutables : Backstage, Kratix et Crossplane

Un *Golden Path* dépasse la documentation statique : DORA caractérise les plateformes performantes par des flux automatisés en libre-service où sécurité et conformité sont intégrées par défaut [305]. Dans une `IAP`, ces voies pavées reposent sur quatre strates :

1. **Portail développeur (**`Backstage Software Templates`**)** : via le moteur `Scaffolder`, Backstage propose des gabarits paramétrés par palier (`R1–R4`, chapitre 12) [308]. L’équipe renseigne l’`Agent Owner`, la sensibilité des données et le profil de modèle ; le gabarit génère le dépôt `Agent Harness 80/20`, la CI et les descripteurs initiaux [308]. Les actions personnalisées utilisent le nommage `camelCase` pour éviter les erreurs d’expression, complétées par le mode *Dry Run* et des droits granulaires [308].
2. **Orchestrateur d’API plateforme (**`Kratix Promises`**)** : Kratix empaquette chaque capacité agentique complète sous forme de contrat déclaratif (*Promise*) [309]. Sur instanciation d’une `Promise` d’agent `R3`, Kratix exécute les pipelines de conformité et sécurité puis planifie la livraison multi-grappes [309].
3. **Plan de contrôle d’infrastructure (**`Crossplane v2.4`**)** : Crossplane traduit des définitions composites (`CompositeResourceDefinitions` / `XRD`) en ressources gérées au moyen de `Compositions` versionnées (*Composition Revisions*) et de fonctions de composition [310]. Le domaine obtient base d’état, file, cache et clé virtuelle via une API unifiée sans manipuler les droits IAM ni la topologie réseau sous-jacente [310].
4. **Socle managé pré-câblé** : tout agent créé sur le *Golden Path* reçoit nativement télémétrie `OpenTelemetry GenAI`, identité `SPIFFE` /`Agent ID`, routage par l’`AI Gateway` et la `MCP Gateway`, et suite `EvalOps` initiale [306] [305]. Ce pré-câblage garantit le découplage entre l’équipe plateforme, qui livre la capacité en libre-service, et l’équipe domaine, qui conserve la pleine autonomie sur ses itérations métier [306] [307].

> **[Figure]**
> - Internal Agentic Platform
> - (IAP) — Thinnest Viable
> - Platform
> - [system]
> - «container» Portail développeur
> - [Backstage Scaffolder]
> - Catalogue unifié et gabarits
> - Golden Path exécutables
> - «container» Orchestrateur d'API
> - plateforme [Kratix Promises]
> - Validation conformité, sécurité
> - et distribution multi-grappes
> - «container» Plan de contrôle
> - infrastructure [Crossplane (XRD / Compositions)]
> - Approvisionnement déclaratif
> - GPU, BD, Redis et files
> - «container» Socle managé pré-câblé [AI/MCP Gateway, Temporal, OTel,
> - OPA]
> - Identités SPIFFE, quotas FinOps
> - et EvalOps CI
> - «person»
> - Équipe Domaine
> - Stream-aligned : logique 80/20,
> - prompts et outils MCP métier
> - «person»
> - Équipe Plateforme
> - Produit interne : conçoit et itère
> - les Golden Paths
> - Instancie un gabarit
> - en libre-service
> - Publie gabarits
> - versionnés
> - Maintient les Promises
> - et politiques
> - Déclenche requête
> - de capacité
> - Compose ressources infonuagiques/locales
> - Configure passerelles, identités et télémétrie
> - Déploie et opère les agents via GitOps

*Fig. 49. – Architecture de référence d’une Internal Agentic Platform (IAP) en quatre strates découplées*

### 13.1.3 Frontière stricte plateforme/domaines et régimes d’exception

Standardiser le socle ne signifie pas centraliser la logique métier. Si l’équipe plateforme écrit les prompts ou serveurs `MCP` propres aux `Systems of Record`, elle devient un goulot d’étranglement contraire à *Team*

*Topologies* [307]. Réciproquement, laisser un domaine déployer sa propre passerelle `LLM` compromet sécurité et comptabilité `FinOps`.

Le *Golden Path* reste une incitation privilégiée et non un carcan [306] [307]. Une équipe `Complicated Subsystem` confrontée à des contraintes atypiques peut solliciter une dérogation devant l’`ARB` [307]. Elle supporte alors intégralement l’exploitation, la maintenance et l’audit de sa pile alternative, tout en satisfaisant aux portes d’admission les mêmes contrats `OTel`, `OPA` et d’identité [306] [309].

| Dimension | Équipe Plateforme (`IAP`) | Équipe Domaine | Contrat de contrôle |
| --- | --- | --- | --- |
| **Gabarits** | Maintient `Backstage` et `Kratix Promises` [308] [309] | Instancie en libre-service (`Agent Owner`, `R1–R4`) [308] | Validation schématique sur `PR` |
| **Logique** `80/20` | Fournit SDK harnais et adaptateurs durables [306] | Rédige code déterministe, prompts et outils `MCP` | `JSON Schema` et `EvalOps` |
| **Infra & GPU** | Opère `Crossplane`, passerelles et `vLLM` /`NIM` [310] | Consomme `XRD` et clés virtuelles d’inférence [310] | `Composition Revisions`, quotas |
| **Sécurité & coûts** | Câble `SPIFFE`, `OPA`, `Cosign`, `OTel` et `FOCUS` [306] | Spécifie règles métier et répond aux revues `2LoD` | `Conftest` et admission |
| **Exceptions** | Publie les invariants d’audit obligatoires [306] | Assume astreinte et preuves hors voie pavée [307] | Dérogation `ARB` bornée |

*Tableau 13.1 — Matrice de séparation des responsabilités entre équipe plateforme (*`IAP`*) et équipes domaines.*

> **Arbitrage EA / SA** — Bâtir l’`IAP` selon la *Thinnest Viable Platform* (`TVP`) gérée comme un produit interne : la plateforme détient les *Golden Paths* (`Backstage`, `Kratix`, `Crossplane`), les passerelles partagées et le socle `Zero-Trust` /`OTel` /`GitOps`, tandis que les domaines gardent la maîtrise exclusive de la logique `80/20`, des prompts et des serveurs `MCP` métier [306] [307] [308] [310] [309]. L’`EA` évalue la plateforme selon l’adoption volontaire et le délai de mise en production conforme [306] [305] ; le `SA` interdit toute logique d’affaires dans les couches partagées et soumet les dérogations hors *Golden Path* aux mêmes contrats d’admission et de télémétrie [307] [309].

## 13.2 Topologie de l’AI Gateway hybride : multi-nuages et inférence souveraine sur site (vLLM, NIM)

### 13.2.1 Unification de l’accès aux modèles : Agent Router (GAIE) et LiteLLM

Aucun `Agent Harness` ne doit coder en dur des clés API ni des dialectes propriétaires. L’`AI Gateway` **hybride** forme l’unique façade normalisée — compatible avec l’API OpenAI — derrière laquelle coexistent des modèles frontaliers infonuagiques (`PAYG` ou `PTU`, chapitre 12) et des grappes souveraines sur site ou en nuage privé [311] [312].

Deux solutions ouvertes dominent cette couche de médiation :

1. **Plan de données Envoy (**`Agent Router` **/** `GAIE`**)** : issu d’*Envoy AI Gateway* sous l’*Agentic AI Foundation* tout en conservant le groupe `aigateway.envoyproxy.io`, **Agent Router** s’appuie sur Envoy et la *Kubernetes Gateway API Inference Extension* (`GAIE`) [311] [313]. À l’aide d’`AIGatewayRoute`, il gère virtualisation de modèles, bascule entre fournisseurs (*Provider Fallback*), *Prompt Caching* unifié par `cache_control`, passerelles `MCP` et politiques de débit et de quotas sensibles aux jetons (*Usage-based Rate Limiting* et *Quota Policy*) [311].
2. **Mandataire unifié et gouvernance budgétaire (**`LiteLLM Proxy`**)** : fédérant plus de cent fournisseurs externes et moteurs locaux, `LiteLLM Proxy` repose sur des **clés virtuelles (**`Virtual Keys`**)** [312]. Chaque clé associe un agent à des plafonds budgétaires et quotas `TPM` /`RPM` atomiques dans `Redis`, avec suivi des dépenses dans `PostgreSQL` [312].

En pratique, `Agent Router` s’impose sur les grappes Kubernetes raccordées à `GAIE`, tandis que `LiteLLM` accélère la gouvernance budgétaire sur des catalogues multi-fournisseurs hétérogènes [311] [312]. Dans les deux cas, la passerelle applique les bornes du chapitre 12 : aucun renseignement personnel (`RP`) non masqué ni actif critique ne quitte l’enclave souveraine [311].

### 13.2.2 Ordonnancement sensible à l’inférence sur Kubernetes : GAIE et llm-d

Le répartiteur HTTP classique (*round-robin*) échoue sur les moteurs d’inférence. Une boucle agentique mobilise de larges blocs de cache clé-valeur (`KV Cache`) en GPU, maintient des flux longs et dépend fortement de la réutilisation de préfixes [313] [314] [315]. La spécification `GAIE` et la pile `llm-d` **v1.0** sur `vLLM` répondent à ces contraintes [313] [315] :

1. `InferencePool` **et** `Endpoint Picker` **(**`EPP`**)** : `InferencePool` remplace le `Service` Kubernetes devant les pods de modèles [313] [315]. Envoy consulte l’ordonnanceur `EPP` via `ext-proc` [313] [315]. Un pipeline *Filter-Score-Pick* analyse files d’attente, partage équitable multi-locataires, adaptateurs `LoRA` et affinité de cache de préfixe pour diriger la requête vers le réplica détenant déjà le préfixe système [313] [315]. `llm-d` y ajoute des prédicteurs ML de latence (`TTFT` /`TPOT`) protégeant les `SLO` [315].
2. **Architecture** `V1` **de** `vLLM` **et** `Automatic Prefix Caching` **(**`APC`**)** : `vLLM V1` sépare serveur API, noyau d’ordonnancement (`Engine Core`), travailleurs GPU et coordinateur de parallélisme de données (`DP Coordinator`) [314]. Avec `PagedAttention` et `APC` (`enable_prefix_caching=True`), les requêtes partageant consignes système ou schémas `MCP` réutilisent directement les blocs KV sans recalculer le pré-remplissage (`prefill`) [316]. Pour les modèles hybrides Mamba, `--enable-mamba-shared-prefix-checkpoint` enregistre un point de reprise à la jonction du préfixe partagé [316].
3. **Désagrégation *Prefill / Decode* (**`P/D`**) et transfert RDMA (**`NIXL`**)** : la phase *prefill* est limitée par le calcul (*compute-bound*), alors que la phase *decode* dépend de la bande passante mémoire (*memory-bandwidth-bound*) [317] [315]. Sur une instance unifiée, l’arrivée d’un long contexte interrompt les
  générations en cours et dégrade l’`ITL` [317]. La désagrégation `P/D` isole ces phases sur des pools GPU distincts reliés par transfert KV rapide (`NixlConnector` RDMA ou `LMCache`) [317] [315]. La documentation `vLLM` précise toutefois une règle capitale : **la désagrégation** `P/D` **n’augmente pas le débit brut (*throughput*)** ; elle permet de régler séparément le parallélisme (`tp`, `pp`) pour optimiser le `TTFT` et maîtriser la latence de queue (`tail ITL`) [317].

> **[Figure]**
> - AI Gateway Hybride (Agent Router / LiteLLM)
> - [container]
> - Inférence multi-nuages
> - (R1-R2 / PII filtrées)
> - [container]
> - Enclave GPU souveraine sur site (R3-R4 / Air-gap)
> - [container]
> - «component» Garde d'accès & Quotas
> - [Virtual Keys + Redis]
> - Plafonds TPM/RPM et
> - imputation coûts
> - «component» Routeur sémantique &
> - repli [AIGatewayRoute / Router]
> - Résidence Loi 25, cache_control
> - et failover
> - «component» API Frontier LLMs [PAYG / PTU infonuagique]
> - Raisonnement complexe et
> - débordement
> - «component» Inference Gateway (GAIE)
> - [InferencePool + EPP (llm-d)]
> - Affinité cache KV et prédiction
> - TTFT/TPOT
> - «component» Grappes vLLM (P/D +
> - NIXL) [PagedAttention + APC]
> - Pools Prefill/Decode sur RDMA
> - «component» NVIDIA NIM Operator
> - [NIMCache + NIMService]
> - Microservices sur PVC hors ligne
> - «component» Agent Harness / SoA
> - [Client OpenAI-compatible]
> - Appelle /v1/chat/completions
> - avec clé virtuelle et balises
> - FinOps
> - Envoie requête
> - Valide budget et jetons
> - Flux autorisés / PTU Flux souverains R3-R4
> - ext-proc Routage local

*Fig. 50. – Topologie de l’AI Gateway hybride reliant routage multi-nuages, GAIE/llm-d, vLLM P/D et enclave souveraine NVIDIA NIM*

### 13.2.3 Enclave souveraine et air-gapped sur site : NVIDIA NIM Operator

Sous contrainte de la Loi 25, de secrets industriels ou de réseaux isolés (*air-gapped*), l’exploitation sur site requiert un conditionnement reproductible. Le `NVIDIA NIM Operator` gère sur Kubernetes le cycle de vie de microservices conteneurisés portables (`NIM`) — raisonnement, enfouissement (*embedding*) et réordonnancement — derrière une API compatible OpenAI avec prise en charge de l’allocation dynamique de ressources (`DRA`), de l’observabilité et des quotas [318]. Lorsque les chaînes agentiques nécessitent plusieurs modèles coordonnés (par exemple génération augmentée par récupération combinant enfouissement, réordonnancement et `LLM`), la ressource `NIMPipeline` orchestre leur déploiement conjoint de manière déclarative [318].

En environnement déconnecté sans accès NGC ni Internet, le déploiement via `NIMCache` et `NIMService` impose quatre contrôles [319] :

1. **Miroir local et pré-chargement sur** `PVC` : images et poids de modèles sont miroités en interne et montés sur un volume persistant (`PVC`) via `fromCache` [319].
2. **Conformité POSIX non-root** : sur des stockages tels que `NFS` qui ignorent `fsGroup`, les droits des fichiers pré-chargés doivent correspondre explicitement à `spec.userID` et `spec.groupID` [319].
3. **Omission de** `spec.authSecret` : lorsque les modèles sont entièrement pré-cachés, omettre `spec.authSecret` empêche l’injection de `NGC_API_KEY` et toute requête sortante vers NGC [319].
4. **Certificats privés** : derrière un mandataire TLS interne, un `ConfigMap` de certificats racines privés est raccordé via `spec.proxy.certConfigMap` [319].

### 13.2.4 Matrice d’arbitrage hybride et lecture EA / SA

| Critère | Nuage (`PAYG` / `PTU`) | Grappe `vLLM` + `GAIE` / `llm-d` | Enclave `NVIDIA NIM` |
| --- | --- | --- | --- |
| **Souveraineté** | Régions contractuelles ; filtrage PII requis | Totale (données et cache confinés localement) [314] | Maximale (hors ligne sans `NGC_API_KEY`) [319] |
| **Cache et routage** | `cache_control` unifié à la passerelle [311] | `PagedAttention`, `APC` et score `EPP` [313] [316] [315] | Cache persistant `NIMCache` sur `PVC` [318] [319] |
| **Latence** `TTFT` **/** `ITL` | Bruit voisin (`PAYG`) ou capacité `PTU` | Contrôle par désagrégation `P/D` (`NIXL` RDMA) [317] [315] | Prévisible sur GPU dédiés [318] |
| **Charge d’exploitation** | Minimale (aucun GPU à opérer) | Élevée (réglage `tp` /`pp`, réseau RDMA) [317] [315] | Modérée à élevée (opérateur K8s, POSIX, miroir) [318] [319] |
| **Usage cible** | Raisonnement complexe `frontier` (`R1–R2`) | Volume interne `SLM`, longs préfixes partagés [315] | Flux `R3–R4`, Loi 25 et enclaves isolées [319] |

*Tableau 13.2 — Comparaison des substrats d’inférence hybride derrière l’*`AI Gateway`*.*

> **Arbitrage EA / SA** — Imposer l’`AI Gateway` hybride (`Agent Router` /`GAIE` ou `LiteLLM` + `Redis`) comme point de passage unique de l’inférence, appliquant clés virtuelles, quotas `TPM` /`RPM` et résidence hors du code applicatif [311] [313] [312]. L’`EA` dirige les tâches anonymisées vers le nuage et confine données sensibles (`R3–R4`) et haut volume `SLM` sur grappes souveraines (`vLLM` ou `NIM`) [315] [319] ; le `SA` remplace le *round-robin* par `InferencePool` + `EPP` (`llm-d`) sensible au cache `APC`, réserve `P/D` aux `SLO` stricts de latence de queue et limite chaque bascule aux juridictions homologuées [313] [316] [317] [315].

## 13.3 GitOps cognitif : versionnement conjoint du code, des prompts, des schémas OASF/MCP et politiques OPA

### 13.3.1 Transposer OpenGitOps aux systèmes non déterministes

La spécification `OpenGitOps` **v1.0.0** impose quatre principes : état désiré **déclaratif**, stockage **versionné et immuable**, extraction automatique (*pulled automatically*) par des agents internes et **réconciliation continue** [320]. Un contrôleur tel qu’**Argo CD** compare en boucle l’état vif au dépôt Git (`Synced` contre `OutOfSync`) et corrige toute altération manuelle par auto-guérison (*self-healing*), éliminant les justificatifs administratifs Kubernetes des pipelines CI externes [320] [321].

Appliquer ce modèle aux seuls conteneurs néglige cependant le couplage `CACE` du chapitre 1. Le comportement réel d’un agent résulte d’un **quintette cognitif** indissociable : code `80/20` et workflows, prompts et paramètres, contrats `OASF` et `MCP` (`server.json`), politiques `OPA` (`Rego`) et jeux `EvalOps`. Modifier un seul de ces artefacts hors de Git provoque une dérive invisible pour les sondes HTTP d’Argo CD [320] [321] [322].

### 13.3.2 Le dilemme du registre de prompts : découplage dynamique contre immuabilité Git

Des registres tels que `Langfuse Prompt Management` dissocient l’édition textuelle du déploiement logiciel : les équipes produit ajustent un prompt en interface web, promeuvent une étiquette (`staging` → `production`) et propagent la révision sans latence grâce au cache client SDK [322]. Utile pour itérer vite sur un assistant `R1`, ce découplage heurte `OpenGitOps` dès le palier `R3–R4` [320] [322] :

1. **Rupture d’atomicité au repli** : un retour arrière Git sur le code combiné à un prompt déjà promu crée un état hybride jamais testé conjointement.
2. **Déficit de traçabilité réglementaire** : sans lien CI cryptographique, prouver quel couple exact code-prompt a généré une décision devient fragile [322] [323].

La réponse d’ingénierie consiste à verrouiller les prompts par les portes CI décrites par `Promptfoo` [323]. Sur toute `Pull Request` modifiant `prompts/**`, `promptfoo/promptfoo-action@v1` exécute une évaluation différentielle avant/après (assertions déterministes et juges `LLM`), publie le bilan dans la `PR` et bloque la fusion en cas de régression [323]. L’`IAP` distingue ainsi deux régimes :

- **Régime couplé strict (**`R3–R4`**)** : les prompts résident dans Git ; toute édition visuelle ouvre une `PR` validée par `Promptfoo`, et la production épingle une révision immuable [320] [323].
- **Régime découplé borné (**`R1–R2`**)** : le registre dynamique (`Langfuse`) reste admis, mais le passage à l’étiquette `production` exige un test `EvalOps` automatisé et la trace `(prompt_name, version)` dans `OpenTelemetry` [322].

### 13.3.3 Contrats OASF/MCP, politiques OPA/Conftest et chaîne SLSA/Sigstore

Le `GitOps` cognitif verrouille simultanément schémas protocolaires, règles de gouvernance et chaîne d’approvisionnement :

1. **Contrats** `OASF` **et** `MCP` **(**`server.json`**)** : sous `AGNTCY`, chaque fiche d’agent porte deux champs `SemVer` (`version` et `schema_version`) validés en CI contre des schémas immuables, en distinguant erreurs bloquantes et avertissements [324]. Tout serveur `MCP` décrit par `server.json` est contrôlé face au schéma `server.schema.json` (Draft-07) du registre officiel, qui avertit explicitement contre l’injection de commandes dans les arguments CLI et recommande l’exécution sans interpréteur (`posix_spawn`) avec consentement préalable [325].
2. **Politiques** `OPA` **(**`Rego`**) et** `Conftest` : **Open Policy Agent** découple la prise de décision de l’exécution applicative en évaluant des données structurées JSON/YAML via le langage déclaratif `Rego` à travers toute la pile : pipelines CI/CD, passerelles Envoy/Istio, admission Kubernetes (`OPA Gatekeeper`) et contrôle d’invocation d’outils d’agents (*Agent Tool Calling*) [326]. Dès l’ouverture d’une `PR`, `Conftest` applique les règles `deny_` aux manifestes Kubernetes, configurations Terraform, pipelines et descripteurs d’agents afin d’intercepter les non-conformités avant toute fusion [327].
3. **Signature sans clé (**`Sigstore Cosign`**) et provenance** `SLSA v1.2` : une fois les tests validés, la CI génère une attestation `in-toto` conforme à la spécification approuvée `SLSA v1.2` (`https://slsa.dev/provenance/v1`), consignant dans `buildDefinition` et `runDetails` l’origine exacte du dépôt, la révision et le bâtisseur automatisé [328]. `Sigstore Cosign` appose une signature sans clé persistante (*keyless signing*) liant un certificat éphémère à l’identité `OIDC` du workflow (`Fulcio`) et enregistrant la preuve au journal de transparence `Rekor`, dont la racine de confiance est distribuée par `TUF` [329]. À l’admission en grappe, signature et provenance sont vérifiées avant toute synchronisation `Argo CD` [321] [328] [329].

> **[Figure]**
> - 1. Dépôt Git (Source unique immuable)
> - 2. Portes CI automatisées (Pull Request)
> - 3. Réconciliation GitOps et admission
> - 4. Exécution cible
> - Code Harnais 80/20 & Workflows durables Prompts versionnés & jeux EvalOps
> - Contrats OASF & MCP server.json
> - Politiques OPA (Rego) & manifestes K8s
> - Promptfoo / EvalOps (non-régression PR)
> - Validateur OASF & server.schema.json
> - Conftest / OPA Test (règles deny_)
> - Build OCI + Cosign & provenance SLSA v1.2
> - Registre OCI & Journal Rekor
> - Argo CD (Sync & Self-Heal)
> - Contrôle d'admission (Gatekeeper / Sigstore)
> - Pods Agents & Workers durables
> - Registre OASF & MCP Gateway
> - compare vs main valide SemVer contrôle statique
> - empaquette
> - approuve PR approuve PR approuve PR
> - pousse artefacts signés
> - vérifie signatures
> - soumet état désiré
> - déploie si attesté publie fiches validées

*Fig. 51. – Chaîne complète du GitOps cognitif : dépôt unifié, portes CI multi-artefacts, attestation Sigstore/SLSA et réconciliation Argo CD*

### 13.3.4 Synthèse de co-versionnement et arbitrage EA / SA

| Artefact | Source de vérité | Porte CI (`PR`) | Attestation | Réconciliation |
| --- | --- | --- | --- | --- |
| **Code harnais** `80/20` | Git applicatif [320] | Tests unitaires et rejeu | OCI `Cosign` + `SLSA v1.2` [328] [329] | `Argo CD` (`Sync`, `Self-Heal`) [321] |
| **Prompts et gabarits** | Git (`R3–R4`) ou registre (`R1–R2`) [322] | Différentiel `Promptfoo` [323] | Paquet signé ou révision figée | Déploiement atomique ou étiquette [322] |
| **Contrats** `OASF` **/** `MCP` | Dépôt versionné [324] [325] | Validateur `OASF` + `server.schema.json` | Signature `Cosign` [329] | Publication auto post-sync [321] |
| **Politiques** `OPA` **(**`Rego`**)** | Dépôt gouvernance [326] | `opa test` + `Conftest` [327] | Bundle `Cosign` + `Rekor` [329] | Rechargement via `Argo CD` [321] |
| **Jeux** `EvalOps` | Dépôt `evals/` | Validation schéma et juge | Empreinte jointe CI [328] | Exécution CI et `AnalysisTemplate` |

*Tableau 13.3 — Matrice de versionnement conjoint et portes automatisées du* `GitOps` *cognitif.*

> **Arbitrage EA / SA** — Étendre les quatre principes `OpenGitOps` au **quintette cognitif complet** (code, prompts, schémas `OASF` /`MCP`, règles `OPA`, jeux `EvalOps`) et interdire l’édition non testée en production sur tout agent `R3–R4` [320] [321] [322] [323]. L’`EA` exige provenance `SLSA v1.2` et signature `Sigstore` sur chaque décision auditable, tout en tolérant des étiquettes dynamiques sous garde `EvalOps` en `R1–R2` [328] [329] [322]. Le `SA` verrouille la `PR` par `Conftest`, validateurs `OASF` /`server.schema.json` et `Promptfoo`, puis réconcilie via `Argo CD` avec `Self-Heal` et vérification à l’admission [321] [327] [323] [324] [325].

## 13.4 Déploiement progressif (shadow, canary, blue/green) et compatibilité des workflows durables en vol

### 13.4.1 Mode fantôme (Shadow), Canary et Blue/Green pour systèmes agentiques

Malgré les tests hors ligne, un changement de modèle ou de prompt reste exposé à la variance du trafic réel. La livraison progressive contient le rayon d’impact au moyen de `Kubernetes Gateway API` et `Argo Rollouts` [330] [331] :

1. **Mode fantôme (*Shadow* /** `Traffic Mirroring`**)** : via le filtre `HTTPRouteRequestMirror` de la `Gateway API` (ou l’étape `setMirrorRoute` d’Argo Rollouts), la passerelle duplique de façon asynchrone les requêtes vers une version candidate `v2` tout en renvoyant au client la seule réponse de `v1` [332] [331]. La spécification impose qu’un seul point d’aboutissement reçoive la copie et que la réponse
  miroir soit obligatoirement ignorée (`MUST be ignored`) [331]. Pour éviter qu’un agent `v2` n’exécute une **double écriture** sur le `System of Record` via un outil `MCP` mutateur, tout trafic miroir doit propager un en-tête de simulation forçant la `MCP Gateway` à détourner les écritures vers des bouchons [332].
2. **Canari (**`Canary`**) et** `AnalysisTemplate` : `Argo Rollouts` augmente par paliers le poids vers `v2` (`setWeight`, `pause`) via un routeur compatible plutôt que par le seul ratio de réplicas [330]. Chaque palier exécute un `AnalysisRun` issu d’un `AnalysisTemplate` interrogeant `Prometheus`, `OpenTelemetry` ou `EvalOps` selon des seuils `successCondition` ; au-delà de `failureLimit`, le contrôleur avorte et restaure `v1` [330] [333].
3. **Bascule bleu/vert (**`Blue/Green`**)** : lorsque deux versions frontales ne peuvent cohabiter, `Argo Rollouts` valide `v2` sur un `previewService` via `prePromotionAnalysis` avant de commuter l’`activeService` [334]. Le délai `scaleDownDelaySeconds` maintient `v1` actif le temps que les nœuds mettent à jour leurs règles réseau et drainent les flux ouverts [334].

### 13.4.2 Le défi des workflows durables en vol : rejeu déterministe et dérive de version

Les stratégies réseau visent des requêtes courtes. Or un workflow durable sous `Temporal`, `Restate` ou `Dapr Workflow` (chapitre 9) demeure **en vol** des heures ou des jours dans l’attente d’un minuteur ou d’une décision `Human-on-the-Loop` [335] [336] [337].

Dans un moteur à rejeu d’événements (`Temporal`, `Dapr Workflow`), au réveil d’un dossier endormi, le travailleur recharge le code actif pour rejouer l’historique passé [335] [337]. Si un *rolling update* a remplacé `v1` par un code `v2` modifiant l’ordre des activités ou des minuteurs, les commandes divergent de l’historique enregistré, déclenchant une **erreur de non-déterminisme** qui bloque le workflow en vol [335] [338].

### 13.4.3 Temporal Worker Versioning (Pinned / Rainbow), Patching, Restate immuable et Dapr

L’`IAP` industrialise les mécanismes natifs de compatibilité offerts par les moteurs durables :

1. `Temporal Worker Versioning` **et déploiements arc-en-ciel (*Rainbow*)** : depuis Temporal Server `v1.29.1+` et les SDK modernes (`Go v1.35+`, `Python v1.11+`, `TypeScript v1.12+`, `Java v1.29+`), chaque déploiement de travailleurs porte un `Build ID` au sein d’un `Worker Deployment` [335]. Le mode `Pinned` garantit que chaque workflow achève son exécution sur le `Build ID` exact de son démarrage au sein de **déploiements arc-en-ciel** (plus de deux versions simultanées) : `Current` ou `Ramping` reçoivent les nouveaux flux tandis que les anciens travailleurs terminent les dossiers en vol sans rustines ni erreur de rejeu, jusqu’à ce que Temporal signale leur drainage complet pour mise hors service [335]. Le mode `Auto-Upgrade` migre les workflows vers la nouvelle cible — utile au-delà de la durée de rétention des révisions — mais oblige à maintenir manuellement la compatibilité de rejeu [335]. `Temporal` proscrit toutefois d’activer ce versionnement sur des files spécifiques à un travailleur individuel pour ne pas épuiser les limites par version [335].
2. `Temporal Patching API` **et rejeu CI** : sous `Auto-Upgrade`, le code protège chaque évolution logique par `patched("id")`, qui écrit un marqueur dans l’historique des nouvelles exécutions et garde l’ancienne branche (`false`) pour les dossiers antérieurs [338]. Règle impérative de `Temporal` : **toujours placer la branche la plus récente en tête du bloc** `if patched(...)` (`v3` avant `v2`), sinon les nouvelles exécutions évaluent d’abord l’ancienne branche à `true` et s’y figent [338]. La CI exécute en outre des tests de rejeu sur historiques de production réels [335].
3. `Restate` **— Déploiements immuables par révision** : `Restate` enregistre chaque révision sous un point HTTP ou `ARN` FaaS **immuable** (`restate deployments register`) et achemine toute invocation,
  reprise ou attente sur la révision exacte de départ, sans aucune logique conditionnelle dans le code [336]. Sur Kubernetes, l’opérateur `Restate` crée une révision par changement de gabarit et réduit les anciennes après drainage, tout en conseillant de scinder les traitements pluri-mensuels en appels différés enchaînés [336].
4. `Dapr Workflow` **— Déterminisme et** `continue-as-new` : fondé sur un journal rejoué par sidecar avec concurrence bornée, `Dapr Workflow` exige un déterminisme strict en cours de vol et recommande `continue-as-new` (ou sous-workflows enfants) pour tronquer périodiquement l’historique des agents continus entre deux cycles [337].

> **[Figure]**
> - Passerelle /Argo Rollouts
> - Moteur Durable (Temporal / Restate)
> - Worker v1 (Current / Révision A)
> - Worker v2 (Canary / Révision B)
> - AnalysisTemplate
> - (OTel / EvalOps)
> - Passerelle /Argo Rollouts
> - Moteur Durable (Temporal / Restate)
> - Worker v1 (Current / Révision A)
> - Worker v2 (Canary / Révision B)
> - AnalysisTemplate
> - (OTel / EvalOps)
> - 1. Phase Shadow (Traffic Mirroring sans effet de bord)
> - 1 Requête réelle client (réponse retournée)
> - 2 Copie asynchrone RequestMirror (réponse ignorée, écritures bloquées)
> - 3 Émet latence, erreurs et scores fantômes
> - 2. Phase Canary / Ramping avec Workflow Pinning (en vol)
> - 4 Déclare v2 en Ramping (ex. 20 % nouveaux flux)
> - Workflow wf-101 (démarré sur v1) se réveille après attente HITL / minuteur
> - 5 Route wf-101 (Pinned sur Build ID v 1 /endpoint immuable A) -> zéro erreur de rejeu
> - 6 Route nouveau wf-204 (Build ID v2 /endpoint immuable B)
> - 7 Télémétrie SLO comportementale et coûts
> - 3. Promotion progressive ou retour arrière et drainage
> - 8 successCondition validée -> promeut v2 (Current)
> - Anciens workers v 1 maintenus jusqu'au drainage complet de wf-101
> - 9 Achève wf-101 proprement
> - 10 Mise à zéro (scaleDown) après drainage

*Fig. 52. – Séquence de déploiement progressif (Shadow, Canary) articulée avec l’épinglage des workflows durables en vol*

### 13.4.4 Matrice de sélection et arbitrage EA / SA

| Mécanisme | Couche | Usage principal | Garde-fou impératif |
| --- | --- | --- | --- |
| `Shadow` **(**`RequestMirror`**)** | Passerelle `L7` [332] [331] | Observer `v2` sous trafic réel [332] | Réponse ignorée ; **bouchonnage** `MCP` [332] [331] |
| `Canary` **(**`AnalysisTemplate`**)** | Trafic + métriques [330] [333] | Montée graduelle sous `SLO` /`EvalOps` [330] | `failureLimit` et repli auto [333] |
| `Blue/Green` | Service actif/aperçu [334] | Bascule atomique sur rupture frontale [334] | Calibrer `scaleDownDelaySeconds` [334] |
| `Temporal` `Pinned` | `Task Queue` + `Build ID` [335] | Isoler les workflows en vol sans rustine [335] | Maintenir builds jusqu’au drainage [335] |
| `Temporal` `Auto-Upgrade` | Marqueur `patched()` [335] [338] | Workflows multi-mois [335] | Branche récente en tête + rejeu CI [335] [338] |
| `Restate` **immuable** | Endpoint / `ARN` figé [336] | Zéro code de compatibilité [336] | Scinder attentes multi-mois [336] |
| `Dapr` **(**`continue-as-new`**)** | Journal sidecar [337] | Tronquer boucles continues [337] | Vérifier tâches en cours [337] |

*Tableau 13.4 — Articulation entre livraison progressive réseau et compatibilité des workflows durables en vol.*

> **Arbitrage EA / SA** — Interdire les mises à jour en place non versionnées sur tout travailleur hébergeant des workflows agentiques longs ou `Human-on-the-Loop` [335] [336]. Côté réseau, le `SA` enchaîne `Shadow` (`HTTPRouteRequestMirror` avec écritures simulées) puis `Canary` (`Argo Rollouts` + `AnalysisTemplate` `OTel` /`EvalOps`) [330] [333] [332] [331]. Côté durable, le `SA` privilégie les **déploiements arc-en-ciel épinglés** (`Temporal` `Pinned` par `Build ID` ou révisions immuables `Restate`), réservant `Auto-Upgrade` + `Patching` (vérifié par rejeu CI) ou `continue-as-new` aux processus dépassant la rétention des révisions [335] [338] [336] [337]. L’`EA` préserve ainsi l’intégrité des dossiers et des contrôles humains sous `SLA` lors des déploiements continus.

## Synthèse architecturale et transition vers le chapitre 14

Ce chapitre a défini le socle opérationnel de l’entreprise agentique. L’`Internal Agentic Platform` **(**`IAP`**)** réduit la charge cognitive extrinsèque via des *Golden Paths* exécutables (`Backstage`, `Kratix`, `Crossplane`) [306] [307] [308] [310] [309]. L’`AI Gateway` **hybride** (`Agent Router` /`GAIE`, `LiteLLM`) arbitre entre

nuages publics et enclaves souveraines (`vLLM` /`llm-d`, `NVIDIA NIM`) sous budgets de jetons [311] [313] [312] [315] [319]. Enfin, le `GitOps` **cognitif** co-versionne, évalue et signe le quintette comportemental [320] [326] [328] [329] [323], tandis que l’épinglage des workflows durables sécurise les déploiements progressifs [330] [335] [336]. Le **chapitre 14** assemble ces standards au sein de trois **blueprints d’architecture de référence** prêts à être instanciés.
