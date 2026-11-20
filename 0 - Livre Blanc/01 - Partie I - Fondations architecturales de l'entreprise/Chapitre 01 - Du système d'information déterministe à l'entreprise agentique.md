# Chapitre 1 — Du système d’information déterministe à l’entreprise agentique : rupture et continuité architecturales

Pendant plus de trois décennies, l’architecture des systèmes d’information d’entreprise a reposé sur un postulat tacite : à entrée identique et à état persistant équivalent, un composant applicatif exécute le même chemin et produit exactement la même sortie. Progiciels de gestion, bus d’intégration, automatisation robotisée de processus et moteurs de règles tiraient leur fiabilité du déterminisme de leurs contrats d’exécution. L’intégration de grands modèles de langage (*Large Language Models*, `LLM`) outillés au cœur des opérations brise ce postulat, non parce qu’elle rend les bases transactionnelles obsolètes, mais parce qu’elle insère une couche de raisonnement probabiliste capable de planifier, d’invoquer des interfaces et d’altérer l’état du monde réel [1] [2] [3].

L’échec de la majorité des premiers pilotes en entreprise découle d’une erreur de catégorisation architecturale : traiter un système agentique comme un simple assistant conversationnel posé devant des interfaces de programmation (`API`), sans redéfinir les frontières d’autorité, le régime temporel, la réversibilité des effets de bord ni l’équilibre entre dette technique et dette cognitive [4] [5] [6]. Un assistant conversationnel fautif expose l’organisation à une erreur de lecture; un système autorisé à muter des actifs transactionnels convertit une ambiguïté sémantique, un bruit d’inférence ou une dérive statistique en incident financier, opérationnel ou réglementaire immédiat [5] [7].

Ce chapitre pose les fondations conceptuelles et les critères d’éligibilité qui permettent à un comité d’architecture d’autoriser ou de disqualifier une charge de travail agentique. Fidèle à sa frontière d’étanchéité, il ne détaille ni les protocoles d’interopérabilité (Partie II) ni les topologies multi-agents et moteurs d’exécution durable (Partie III). Il croise systématiquement la lecture de l’architecte d’entreprise (`EA`), axée sur le portefeuille applicatif, la conformité et la maîtrise des risques, et celle de l’architecte de solutions (`SA`), centrée sur les contrats d’interface, la latence, l’idempotence et le confinement.

## 1.1 Stratification du SI : Systems of Record, Systems of Engagement et Systems of Agency

L’adoption de composants cognitifs autonomes n’efface pas l’urbanisation historique des systèmes d’information; elle y superpose une strate supplémentaire dont le mandat, les invariants et le rythme d’évolution diffèrent profondément des couches sous-jacentes [1] [3].

### 1.1.1 De la dualité `SoR` / `SoE` à l’émergence des `Systems of Agency`

L’architecture d’entreprise classique s’est structurée autour de deux plans complémentaires [3]. À la base résident les systèmes d’enregistrement, ou `Systems of Record (SoR)` : progiciels `ERP`, moteurs bancaires centraux, systèmes de gestion du capital humain (`HCM`), bases `CRM` maîtresses et référentiels de gestion des identités [1] [3]. Leur raison d’être demeure la préservation de la source unique de vérité (`SSOT`) consolidée par les dispositifs de données maîtresses (`MDM`), la haute disponibilité, l’intégrité des enregistrements et la conformité aux exigences réglementaires (`SOX`, `PCI DSS`, `RGPD`) [1]. Ces systèmes reposent sur des flux de validation stricts et n’acceptent que des mises à jour rigoureusement contrôlées [1].

Au-dessus se sont développés les systèmes d’engagement, ou `Systems of Engagement (SoE)` : portails web, messageries, applications mobiles, outils collaboratifs et canaux conversationnels [3]. Ils optimisent l’ergonomie, la collaboration humaine et la réactivité d’interaction tout en générant d’importants volumes

de signaux non structurés [3]. Dans cette urbanisation à deux strates, l’orchestration cognitive entre silos incombait toutefois aux humains : l’opérateur naviguait d’un écran `SoE` à l’autre, interprétait des demandes non structurées, croisait les données de plusieurs `SoR` et saisissait manuellement les écritures finales [3].

Les `Systems of Agency` (`SoA`, ou *Systems of Agents*) occupent cet intervalle opérationnel [3]. Ils désignent des plateformes et environnements d’exécution capables de capter les signaux métier en temps réel, de planifier, de raisonner et de conduire de manière autonome des actions multi-étapes à travers les silos vers un objectif explicite [4] [3]. Contrairement à un agent conversationnel limité à un échange en un seul tour, le `System of Agency` opère dans une boucle d’exécution continue — observer l’intention, planifier, récupérer le contexte, raisonner, agir via des appels d’outils et vérifier la vérité terrain — dans des contextes asynchrones faiblement couplés [2] [4] [3].

En continuité architecturale, le `System of Agency` ne doit jamais remplacer le `System of Record` comme ancrage d’autorité : les impératifs de conformité, de pistes d’audit probantes et d’intégrité des données maîtresses exigent que la vérité transactionnelle demeure dans des registres déterministes gouvernés [1] [5]. La rupture tient au déplacement du centre de gravité de la valeur : après l’ère du stockage structuré (`SoR`) puis de l’interface collaborative (`SoE`), l’avantage structurel appartient aux organisations capables d’orchestrer sûrement l’exécution autonome entre les strates existantes sous garde-fous explicites de gouvernance, d’autorisation et de traçabilité [1] [5] [3].

> **[Figure]**
> - Stratification du SI : SoE, Systems of Agency et SoR
> - Strate 1 — Systems of Engagement (SoE)
> - Strate 2 — Systems of Agency (couche probabiliste bornée)
> - Strate 3 — Systems of Record (SoR — déterministe)
> - Opérateur /Client métier
> - Portails, CRM
> - et canaux
> - Planification
> - adaptative
> - Noyau d'agence
> - (paliers L1-L4)
> - Porte d'impact et HITL / HOTL
> - ERP, Core Banking
> - et SGBD maîtres Vérité maîtresse et journal d'audit
> - Intention
> - Plan borné Action
> - Transaction validée
> - Requête asynchrone
> - Mutation idempotente
> - validée uniquement Lecture seule filtrée
> - (vérité terrain)

*Fig. 1. – Stratification évolutive du système d’information : SoE, Systems of Agency et SoR*

### 1.1.2 Workflows déterministes contre boucles agentiques : le spectre de complexité

Toute intégration d’un modèle génératif ne relève pas de l’agentivité, et toute tâche automatisable ne justifie pas une boucle autonome [2] [8]. Les guides d’ingénierie d’Anthropic et de Microsoft distinguent nettement deux régimes d’architecture selon le siège du contrôle décisionnel [2] [8] :

1. **Les *workflows* déterministes augmentés par LLM** : des chemins de code prédéfinis orchestrent les modèles et les outils selon un graphe figé (enchaînement linéaire, routage conditionnel ou exécution parallèle); le `LLM` accomplit uniquement des sous-tâches bornées telles que la classification, l’extraction structurée ou la synthèse [2] [4].
2. **Les agents autonomes** : le modèle dirige dynamiquement son propre processus, sélectionne les outils à invoquer à chaque itération selon les résultats intermédiaires et détermine lui-même les conditions d’arrêt [2] [4].

Ce partage s’inscrit sur un spectre progressif de complexité : appel direct de modèle sans outil, agent unique outillé, puis coordination multi-agents [8]. Le principe directeur exige d’adopter systématiquement le palier le plus simple capable de satisfaire l’exigence métier [2] [8]. Chaque degré d’autonomie supplémentaire accroît en effet la latence cumulée, la consommation de jetons d’inférence, la surcharge de coordination et la complexité de débogage [2] [8]. Dès qu’un processus présente des étapes prévisibles et des exceptions énumérables, il doit demeurer dans un *workflow* déterministe; l’agentivité ne devient légitime que pour des problèmes ouverts à forte variabilité sémantique où le nombre d’étapes ne peut être codé statiquement et où la résolution exige un retour adaptatif de l’environnement [2] [4].

### 1.1.3 Frontières d’autorité et lecture conjointe EA / SA

L’insertion d’une couche `SoA` entre `SoE` et `SoR` redessine les responsabilités d’architecture. Pour l’architecte d’entreprise (`EA`), l’enjeu central consiste à prévenir une prolifération non gouvernée d’agents départementaux connectés sans médiation aux bases maîtresses, qui contournerait les politiques de conformité et fragmenterait les coûts d’inférence [1] [5]. Pour l’architecte de solutions (`SA`), la priorité réside dans l’asymétrie stricte des accès et la borne d’exécution : accorder des lectures analytiques filtrées tout en interposant une couche de validation déterministe, des plafonds stricts d’itérations et la traçabilité de chaque étape avant toute mutation sur un `SoR` [1] [8] [5].

| Dimension architecturale | `System of Record (SoR)` | `System of Engagement (SoE)` | `System of Agency (SoA)` |
| --- | --- | --- | --- |
| **Mandat principal** | Source d’autorité validée (`SSOT`) et conformité [1] | Expérience utilisateur et collaboration [3] | Planification adaptative et action déléguée [4] [3] |
| **Logique dominante** | Déterministe, règles strictes et validation formelle [1] | Interface réactive pilotée par l’humain [3] | Boucle probabiliste bornée (*Thought-Action-Observation*) [4] |
| **Cadence d’évolution** | Lente, contrainte par la gouvernance des données [1] | Rapide, itérations produit continues [3] | Continue (prompts, outils, politiques, modèles) [2] [9] |
| **Tolérance aux écarts** | Nulle sur l’intégrité maîtresse [1] | Moyenne (correction humaine en session) | Faible sans garde-fous : amplification silencieuse [5] |
| **Exposition de droits** | Propriétaire du schéma et des verrous [1] | Droits portés par la session utilisateur | Mandat délégué borné à la tâche [5] |

*Tableau 1.1 — Positionnement comparatif des trois strates du système d’information.*

> **Arbitrage EA / SA** — Aucun agent de la strate `System of Agency` ne doit écrire directement dans les tables d’un `System of Record` ni hériter d’un compte administrateur transversal. L’EA maintient les `SoR` comme unique source d’autorité comptable et réglementaire, tandis que le SA confine l’exécution agentique derrière une frontière idempotente qui dissocie la planification probabiliste de l’engagement transactionnel [1] [5].

## 1.2 Rupture épistémique : non-déterminisme, latence variable et effets de bord irréversibles

Insérer un composant probabiliste au cœur d’une chaîne transactionnelle provoque une rupture épistémique qui invalide trois hypothèses fondatrices du génie logiciel distribué : la reproductibilité déterministe des appels, la prévisibilité des délais synchrones et la sûreté des reprises automatiques sur erreur [10] [11] [5].

### 1.2.1 Non-déterminisme intrinsèque et effondrement du mythe de `temperature = 0`

Le profil `NIST AI 600-1` souligne que le caractère probabiliste des modèles génératifs rend caducs les contrôles traditionnels fondés uniquement sur la revue statique de code avant mise en production [12]. Comme l’inspection du code d’orchestration ne permet plus de prédire l’ensemble des trajectoires d’exécution, l’exigence d’auditabilité se déplace vers la journalisation exhaustive des actions à l’exécution et l’échantillonnage statistique sur essais multiples afin de caractériser la distribution réelle des risques [12].

De nombreuses équipes tentent néanmoins de rétablir le déterminisme en fixant le paramètre d’échantillonnage à `temperature = 0` (décodage glouton). Les recherches d’Horace He et du *Thinking Machines Lab* démontrent pourtant que ce réglage ne garantit pas la reproductibilité bit à bit sur les infrastructures d’inférence en production [10]. La cause opérationnelle première réside dans l’absence d’invariance de lot (*batch invariance*) [10]. Pour optimiser le taux d’occupation des processeurs graphiques (`GPU`), les moteurs de service regroupent dynamiquement les requêtes concurrentes selon la charge instantanée. Lorsque la taille et la composition d’un lot varient, les noyaux `GPU` — notamment les multiplications matricielles, les couches de normalisation `RMSNorm` et le calcul d’attention — modifient l’ordre des réductions en virgule flottante [10].

En raison de la non-associativité de l’arithmétique flottante, ces variations minimes déplacent légèrement les valeurs de sortie (`logits`) [10]. Lorsque deux jetons candidats affichent des probabilités quasi équivalentes, ce décalage suffit à inverser le choix du jeton maximal; par propagation autoregressive, une divergence sur un seul jeton initial entraîne des plans d’action ou des paramètres d’outils complètement différents [10]. Bien que l’usage de noyaux invariants aux lots restaure une reproductibilité stricte, il impose une pénalité sensible de débit et de latence que la majorité des API infonuagiques mutualisées n’absorbe pas par défaut [10]. L’architecte doit donc postuler qu’un statut HTTP `200 OK` retourné par un serveur d’inférence ne garantit ni l’identicité d’un rejeu ni la validité sémantique de la décision prise [10] [12].

### 1.2.2 Latence variable, asymétrie prefill/decode et amplification de queue (`p99`)

La seconde rupture affecte la physique du temps d’exécution. Là où une requête `REST` ou `gRPC` vers un `SoR` présente une variance maîtrisée, l’inférence d’un `LLM` obéit à deux régimes matériels opposés modélisés dans *Sarathi-Serve* [13] :

- **Le temps jusqu’au premier jeton (**`TTFT`**, *Time-to-First-Token*)**, gouverné par la phase de préremplissage (*prefill*) intensif en calcul, dont le coût croît avec la longueur du prompt système, de l’historique et des descriptifs d’outils injectés [13].
- **Le temps entre jetons générés (**`TBT` **/** `TPOT`**, *Time-Per-Output-Token*)**, limité par la bande passante mémoire durant la phase de décodage séquentiel et proportionnel au volume du raisonnement généré [13].

Dans les moteurs à mise en lots continue (*continuous batching*), l’arrivée de longs contextes en préremplissage interrompt les itérations de décodage des requêtes actives et provoque de fortes pointes de latence de queue en l’absence d’ordonnancement par tranches (*chunked-prefills*) [13].

Cette instabilité locale s’amplifie de manière critique dans les boucles multi-tours selon la loi des systèmes distribués formalisée par Dean et Barroso (*The Tail at Scale*) : dès qu’une transaction globale dépend séquentiellement ou en éventail de multiples appels sous-jacents, la probabilité de subir la latence du 99e centile (`p99`) d’au moins un maillon croît rapidement avec le nombre d’étapes [11]. Un enchaînement multi-tours d’appels d’inférence et d’outils amplifie ainsi sensiblement les latences de queue et compromet les compromis de réactivité attendus par l’utilisateur [2] [11]. Maintenir des appels synchrones bloquants depuis un `System of Engagement` expose les serveurs frontaux à l’épuisement des fils d’exécution et aux expirations en cascade; l’exécution asynchrone, les plafonds stricts d’itérations et des budgets temporels bornés s’imposent comme exigences structurelles [8] [4] [11].

### 1.2.3 Effets de bord irréversibles et rayon d’impact (`blast radius`)

La convergence du non-déterminisme et de l’accès aux outils d’entreprise produit le risque le plus critique : l’exécution d’effets de bord irréversibles [5] [7]. Le référentiel `OWASP LLM06:2025` définit l’*agence excessive* (`Excessive Agency`) comme l’octroi à un agent de fonctions, de permissions ou d’une autonomie excédant son strict mandat [5]. Une hallucination, une erreur de typage ou un détournement d’objectif (*Agent Goal Hijack*, `ASI01` de l’*OWASP Top 10 for Agentic Applications*) déclenché par une injection indirecte dans un document ou un courriel externe se traduit alors par un abus d’outils (`ASI02`), un détournement de privilèges hérités (`ASI03`) ou des défaillances en cascade (`ASI08`) [5] [7].

L’architecte de solutions doit classer chaque interface selon sa réversibilité et son rayon d’impact (`blast radius`) : lecture de dossiers ou création d’un brouillon interne contre virement financier, suppression en base de production, révocation de certificats ou envoi d’une notification client officielle [5]. De plus, la reprise sur panne par simple relance automatique (*retry*), sûre dans un contrat `REST` idempotent, devient dangereuse si l’état intermédiaire n’est pas consigné : relancer une inférence après coupure réseau

peut amener le modèle à générer un plan différent et déclencher une double mutation sémantique. Les lectures et préparations réversibles doivent donc demeurer isolées des mutations critiques, ces dernières étant verrouillées derrière une porte déterministe et une validation appropriée [5] [7].

> **[Figure]**
> - Rupture épistémique : boucle probabiliste et porte d'irréversibilité
> - SoE
> - Noyau d'agence
> - (SoA)
> - Inférence LLM
> - (probabiliste)
> - Porte d'impact (HITL / Idempot.) SoR (Autorité)
> - SoE Noyau d'agence
> - (SoA)
> - Inférence LLM
> - (probabiliste)
> - Porte d'impact (HITL / Idempot.)
> - SoR (Autorité)
> - 1 Intention ambiguë + mandat
> - loop [Raisonnement (k tours bornés)]
> - 2 Prompt + outils + contexte
> - 3 Plan / outil (TTFT + TPOT)
> - Même à temperature=0, la variance de lots (batch) peut modifier les jetons choisis.
> - alt [Lecture réversible]
> - 4 Requête faible impact
> - 5 Lecture moindre privilège
> - 6 Vérité terrain
> - 7 Résultat (HTTP 200 OK)
> - [Mutation irréversible]
> - 8 Proposition + justification
> - 9 Attente validation HITL
> - 10 Approbation explicite
> - 1 1 Écriture + clé idempotence
> - 12 Confirmation + audit
> - 13 Effet de bord confirmé
> - 14 Synthèse (contrôle sémantique)

*Fig. 2. – Rupture épistémique en exécution : boucle probabiliste, latence cumulée et porte d’irréversibilité*

| Critère technique | Contrat déterministe (`SoR` / workflow) | Contrat probabiliste (`System of Agency`) |
| --- | --- | --- |
| **Reproductibilité** | Identique bit à bit à entrée et état constants | Variable selon charge de lots et version [10] [9] |
| **Mode d’échec** | Exception explicite, code `4xx` /`5xx`, erreur schéma | Succès HTTP `200 OK` masquant un écart sémantique [12] [5] |
| **Régime de latence** | Courte, bornée, prévisible | Asymétrique (`TTFT` + `TPOT`), amplification `p99` [11] [13] |
| **Vérification préalable** | Tests unitaires et revue statique de code | Échantillonnage multi-essais et journaux d’exécution [10] [12] |
| **Reprise sur panne** | Relance sûre sous clé d’idempotence | Risque de divergence et de double effet lors d’une relance non bornée [10] [5] |

*Tableau 1.2 — Caractérisation comparée des contrats logiciels déterministes et probabilistes.*

> **Arbitrage EA / SA** — Les systèmes `SoA` doivent fonctionner en mode asynchrone par défaut et proscrire les appels synchrones bloquants depuis le `SoE` sur des boucles multi-tours. Le SA classe chaque outil par palier de réversibilité et impose l’idempotence sur toute écriture, tandis que l’EA exige une porte d’approbation préalable et une piste d’audit immuable pour tout effet de bord externe ou financier [11] [12] [5].

## 1.3 Spectre d’autonomie opérationnelle (`L0` à `L4`) et modalités Human-in/on-the-Loop

L’autonomie opérationnelle n’est ni un interrupteur binaire ni une propriété dictée par la seule puissance du modèle retenu : elle représente un choix d’architecture délibéré, découplé des capacités brutes du `LLM` sous-jacent [14]. Un modèle de frontière très capable peut et doit être volontairement verrouillé à un palier supervisé dans un processus réglementé, tandis qu’un modèle spécialisé peut opérer de façon autonome dans un périmètre entièrement réversible [14].

### 1.3.1 Échelle graduée `L0` à `L4` : de la logique figée à l’autonomie bornée sous contrat

Les travaux de Feng, McDonald et Zhang établissent une taxonomie à cinq niveaux fondée sur le rôle assumé par l’utilisateur (*Operator*, *Collaborator*, *Consultant*, *Approver*, *Observer*) et introduisent le concept de *certificats d’autonomie* pour formaliser et borner contractuellement l’enveloppe d’action autorisée d’un agent [14]. En architecture d’entreprise, il convient d’ancrer cette gradation sur le socle déterministe `L0` afin d’obtenir une échelle opérationnelle en cinq paliers (`L0` à `L4`), excluant volontairement l’autonomie illimitée hors gouvernance en production :

- `L0` **— Exécution déterministe sans agentivité** : logique entièrement codée et *workflows* statiques prédéfinis sans sélection dynamique d’outils [2] [4]. Ce palier sert à la fois de référence de base pour les processus stables et de cible de repli sûr [2].
- `L1` **— Opérateur assisté (*Operator* / *Assist Mode*)** : l’humain dirige chaque étape et sollicite le modèle pour résumer, extraire des champs ou rédiger des propositions; aucune action vers les systèmes en aval n’est exécutée sans commande explicite [4] [14].
- `L2` **— Collaborateur guidé (*Collaborator*)** : l’agent propose un plan et prépare les lectures en boucle courte, en partageant l’exécution pas à pas avec l’opérateur qui conserve la possibilité d’éditer le plan et de reprendre le contrôle à tout instant [14].
- `L3` **— Exécuteur supervisé par exception (*Consultant* / *Approver* borné)** : l’agent planifie et exécute de façon autonome des séquences multi-étapes dans un périmètre autorisé (lectures fédérées, corrélations, écritures mineures compensables), mais s’interrompt automatiquement dès qu’une ambiguïté dépasse un seuil, qu’un plafond d’itérations est atteint ou qu’une mutation critique est requise [8] [4] [14].
- `L4` **— Autonomie bornée sous contrat (*Observer* certifié)** : l’agent conduit le traitement de bout en bout, incluant la récupération autonome sur erreurs d’outils, à l’intérieur d’une enveloppe contractuelle stricte (périmètre fonctionnel, budget d’inférence, opérations exclusivement réversibles ou compensables, certificat d’autonomie), sous surveillance continue et capacité d’arrêt immédiat [14] [15].

> **[Figure]**
> - Spectre d'autonomie (L0-L4) et transitions de supervision humaine
> - L0 — Déterministe (Workflow codé)
> - Logique figée, zéro autonomie LLM; repli sûr par défaut
> - L 1 — Opérateur assisté (HITL strict)
> - Suggestion ponctuelle; exécution sur commande explicite
> - L2 — Collaborateur guidé (HITL partagé)
> - Plan proposé par l'agent; co-édition et passage de relais
> - L3 — Exécuteur supervisé (HITL sélectif + HOTL)
> - Boucle bornée; arrêt sur effet irréversible ou seuil
> - L4 — Autonomie bornée (HOTL + certificat)
> - Enveloppe réversible; vigilance continue et arrêt sûr
> - Ambiguïté sémantique
> - Itération rapide
> - Outils compensables Mutation irréversible (HITL)
> - Enveloppe certifiée Dérive HOTL
> - Bouton d'arrêt sûr (Art. 14)
> - Plafond d'itérations

*Fig. 3. – Spectre d’autonomie opérationnelle (L0–L4) et transitions de supervision humaine*

### 1.3.2 Modalités `Human-in-the-Loop` et `Human-on-the-Loop` face aux biais cognitifs

La supervision humaine s’organise selon deux régimes complémentaires. Le contrôle `Human-in-the-Loop` **(**`HITL`**)** suspend l’exécution sur le chemin critique avant toute mutation sensible via une confirmation ou un mécanisme de retour de contrôle (*Return of Control*) jusqu’à réception d’une approbation explicite (`L1`, `L2` et points d’arrêt `L3`) [4] [5]. La supervision `Human-on-the-Loop` **(**`HOTL`**)** maintient l’humain en vigie asynchrone sur un flux autonome borné (`L4`) au moyen de journaux d’activité, d’escalades d’anomalies et de coupe-circuits d’urgence [14] [15].

Toutefois, la présence formelle d’un humain dans la boucle ne garantit pas l’efficacité du contrôle. La synthèse empirique de Parasuraman et Manzey établit que dès qu’une automatisation présente une fiabilité perçue élevée mais imparfaite, les opérateurs — experts comme novices — réallouent leur attention sous charge multitâche et succombent à la complaisance et au **biais d’automatisation** : ils approuvent mécaniquement (*rubber-stamping*) des propositions fluides sans contre-vérification indépendante [16]. Le `NIST AI 600-1` intègre ce phénomène dans la catégorie de risque *Human-AI Configuration* [12], et le référentiel `OWASP` le classe parmi les vecteurs d’exploitation de la confiance humain-agent (`ASI09`) [7].

À l’opposé, la modalité `HOTL` expose l’organisation au paradoxe formulé dès 1983 par Lisanne Bainbridge dans *Ironies of Automation* : plus un automate absorbe avec succès les tâches routinières, plus le superviseur relégué à l’observation passive perd sa maîtrise pratique et sa conscience de situation; lorsqu’une défaillance rare et atypique survient, l’opérateur manque précisément des repères requis pour diagnostiquer la situation et reprendre le contrôle sous pression [17]. Pour contrer ces deux risques cognitifs, l’**Article 14 du Règlement européen (**`EU AI Act`**)** oblige à doter les systèmes à haut risque d’interfaces permettant aux superviseurs humains de comprendre les limites réelles du système, de demeurer vigilants face au biais d’automatisation, d’ignorer ou de renverser toute recommandation et d’actionner un « bouton d’arrêt » ramenant le système vers un état sûr [15].

### 1.3.3 Critères d’éligibilité et de disqualification d’un cas d’usage

Tout cas d’usage candidat doit subir un filtrage structuré sur quatre axes : l’ambiguïté sémantique des données entrantes, le coût d’une erreur d’interprétation, la réversibilité technique et légale des effets de bord, ainsi que la capacité d’absorption humaine des revues `HITL`. Un processus est **disqualifié** des paliers autonomes `L3` –`L4` lorsque sa logique se formalise en règles déterministes stables [2], que ses mutations sont irréversibles sans compensation [5], que la cadence des approbations provoquerait un biais d’automatisation généralisé [16] ou que la réglementation impose un jugement humain explicite [15].

| Profil métier | Ambiguïté | Réversibilité et impact | Palier | Contrôle exigé | Décision EA / SA |
| --- | --- | --- | --- | --- | --- |
| Rapprochement comptable et écritures `ERP` | Nulle | Irréversible / impact financier | `L0` | Règles codées, zéro agentivité [2] | **Disqualifié** : conserver déterministe [2] |
| Analyse de sinistres ou notes juridiques | Élevée | Élevé si décision automatisée | `L1` **–**`L2` | `HITL` synchrone avec preuves sources [4] [15] | **Éligible en assistance** : synthèse sans écriture |
| Support client ou incidents TI multi-étapes | Moyenne à élevée | Mixte : lectures + seuils (p. ex. ≤ 250 $ CA) | `L3` | Autonomie bornée; `HITL` au-delà du seuil [4] [5] | **Éligible par exception** sous plafonds stricts [8] |
| Indexation, veille et routage interne | Moyenne | Faible / annulable et versionné | `L4` | `HOTL`, échantillonnage et arrêt sûr (`Art. 14`) [12] [15] | **Éligible en autonomie bornée** par certificat [14] |
| Décision de crédit ou sanction réglementée | Variable | Irréversible / droits fondamentaux | `L1` max | `HITL` explicite anti-biais [12] [15] [16] | **Disqualifié pour** `L3` **–**`L4` : contrôle légal [15] |

*Tableau 1.3 — Matrice d’éligibilité, de disqualification et de calibrage d’autonomie (*`L0` *–*`L4`*).*

> **Arbitrage EA / SA** — Aucune porte `HITL` ne doit se réduire à un bouton binaire présenté en série à un opérateur surchargé, sous peine d’institutionnaliser le biais d’automatisation [15] [16]. Le SA conçoit des écrans d’approbation exposant le différentiel exact de mutation sur le `SoR`, les limites de confiance et la preuve source, tandis que l’EA réserve le palier `L4` aux seuls périmètres réversibles dotés d’un coupe-circuit vers `L0` [5] [14] [15].

## 1.4 Dette technique contre dette cognitive : dérive silencieuse et couplage aux modèles

La viabilité pluriannuelle d’une architecture agentique dépend enfin de sa résistance à une famille d’endettement plus insidieuse que la dette logicielle classique, parce qu’elle affecte simultanément les équipes humaines, les artefacts d’intention et le comportement statistique des modèles [18] [6].

### 1.4.1 Le modèle à trois dettes : technique, cognitive et d’intention

Dans le développement traditionnel, la dette technique s’accumule dans le code source. Les recherches de Margaret-Anne Storey montrent que l’IA générative et agentique réduit la friction d’écriture tout en créant un goulet d’étranglement sur l’assimilation humaine, et proposent un **modèle à trois dettes** (*Triple Debt Model*) [6] :

1. **La dette technique (dans le code)** : compromis structurels, connecteurs fragiles et défauts de modularité qui freinent l’évolution logicielle [6].
2. **La dette cognitive (dans les personnes)** : érosion des modèles mentaux partagés au sein des équipes lorsque la vélocité de production d’artefacts générés par l’IA dépasse la capacité humaine de
  révision et de compréhension [6]. Cette *capitulation cognitive* produit des systèmes qui fonctionnent en apparence mais dont plus personne ne maîtrise les décisions sous-jacentes lors d’un incident [6].
3. **La dette d’intention (dans les artefacts)** : disparition des justifications, objectifs, hypothèses de conformité et contraintes métier (*the why*) [6]. Lorsque des règles critiques sont enfouies dans des instructions narratives sans documentation vivante ni dossier de décision, ni les nouveaux ingénieurs ni les autres agents ne peuvent faire évoluer le système sûrement [6].

### 1.4.2 Enchevêtrement `CACE`, cascades de correction et consommateurs non déclarés

Ces trois dimensions se conjuguent aux lois de dette cachée formulées par Sculley et ses collègues pour les systèmes d’apprentissage automatique [18]. Au cœur de cette dynamique opère le principe `CACE` **(*Changing Anything Changes Everything*)** : contrairement à un module logiciel encapsulé, une chaîne probabiliste présente un enchevêtrement global où l’ajustement d’une phrase du prompt, d’un seuil ou d’un descriptif d’outil peut déstabiliser des comportements éloignés [18]. Cet enchevêtrement engendre trois pathologies récurrentes en production [18] :

- **Les cascades de correction (*correction cascades*)** : pour corriger des erreurs ponctuelles, les équipes empilent des rustines heuristiques — consignes impératives dans le prompt, filtres regex en sortie, règles d’exception dans l’orchestrateur — qui lient rigidement le système aux biais d’une version précise de modèle [18].
- **Les consommateurs non déclarés (*undeclared consumers*)** : des applications aval consomment directement les sorties d’un agent sans contrat d’interface formalisé ni inscription au registre `EA`, subissant des bris silencieux au moindre changement de formulation ou de taux d’abstention [18].
- **L’érosion des frontières et la dette de configuration** : l’agrégation de logique métier, de directives de sécurité et de paramètres d’inférence dans des prompts monolithiques détruit l’encapsulation et concentre les coûts de maintenance hors du code applicatif [18].

> **[Figure]**
> - Boucles de dette cognitive, de dette d'intention et de couplage aux modèles
> - Facteurs de dérive
> - Triple dette et vulnérabilités
> - Contre-mesures EA / SA
> - Mises à jour opaques fournisseur de modèle Prompts et rustines heuristiques (CACE) Vélocité générative sans assimilation
> - Couplage modèle (formats, seuils) Dette d'intention (motifs implicites) Dette cognitive (perte du modèle mental)
> - Consommateurs cachés et régression silencieuse
> - Abstraction modèle et contrats typés Artefacts d'intention versionnés
> - Évaluation continue et repli L0
> - Changement de comportement Enchevêtrement Logique enfouie Érosion mentale
> - Panne à la bascule Édition aveugle Diagnostic impossible
> - Découple l'API Restaure le pourquoi
> - Détecte avant prod

*Fig. 4. – Boucles de dette cognitive, de dette d’intention et de couplage aux modèles*

### 1.4.3 Dérive silencieuse, mises à jour opaques et couplage aux modèles

Le risque ultime naît du **couplage aux modèles** face à la non-stationnarité des services infonuagiques hébergés [18] [9]. L’étude longitudinale de Chen, Zaharia et Zou comparant les versions de mars et juin 2023 des modèles commerciaux `GPT-3.5` et `GPT-4` sur des bancs d’essai constants a fourni la preuve empirique de cette instabilité : sous l’effet de mises à jour opaques d’alignement ou d’infrastructure côté fournisseur, l’exactitude de `GPT-4` sur le suivi de raisonnement en chaîne mathématique s’est effondrée brutalement tandis que les défauts de formatage de code augmentaient [9].

Contrairement à un bris de contrat `API` classique produisant une erreur explicite, la dérive d’un modèle demeure **silencieuse** : l’interface continue de répondre normalement mais modifie la distribution de ses choix d’outils, son taux de refus ou sa conformité de format [12] [18] [9]. Maîtriser ces quatre dettes impose d’encapsuler l’inférence derrière des contrats typés déterministes, de mesurer la variance de base sur des batteries d’essais multiples avant toute promotion de prompt ou de modèle [10] [12] [9], et d’externaliser l’intention métier dans des artefacts gouvernés [14] [6].

| Type de dette | Lieu de résidence | Mécanisme d’accumulation | Symptôme en production | Contre-mesure EA / SA |
| --- | --- | --- | --- | --- |
| **Dette technique** | Code et connecteurs [6] | Contournements et absence de typage | Pannes de schéma et maintenance coûteuse | Contrats typés, modularité et tests [8] |
| **Dette cognitive** | Équipes humaines [6] | Vélocité dépassant la revue humaine [6] | *Capitulation cognitive* et diagnostic bloqué [6] | Limiter la complexité; revue à rythme humain [2] [6] |
| **Dette d’intention** | Prompts et artefacts [6] | Règles métier enfouies sans motif [6] | Régressions lors d’évolutions mineures [6] | Artefacts d’intention et `ADR` versionnés [6] |
| **Couplage modèle** | Cascades `CACE` [18] | Rustines sur biais + mises à jour opaques [18] [9] | Dérive silencieuse et verrouillage API [9] | Abstraction fournisseur et tests multi-essais [10] [12] [9] |

*Tableau 1.4 — Typologie comparée des quatre dettes en ingénierie agentique.*

> **Arbitrage EA / SA** — Toute règle métier impérative (plafond financier, obligation légale, seuil d’éligibilité) doit résider dans du code ou un moteur de politiques déterministe versionné, jamais dans une consigne textuelle exposée au principe `CACE` et aux dérives de modèles [18] [9] [6]. L’EA impose la traçabilité d’intention et la portabilité multi-modèles au portefeuille, tandis que le SA proscrit les consommateurs non déclarés et conditionne toute bascule de modèle à une évaluation statistique multi-essais [10] [12] [18].

## Synthèse et transition

L’entreprise agentique repose sur un équilibre exigeant entre **continuité** et **rupture** : préserver l’intégrité des `Systems of Record` et privilégier les *workflows* déterministes dès que la tâche est prévisible [1] [2], tout en confinant le non-déterminisme de la strate `Systems of Agency`, son amplification de latence `p99`, ses effets irréversibles et sa quadruple dette [10] [11] [5] [6]. À partir de ces fondations et critères d’éligibilité, le **Chapitre 2** transpose ces exigences dans les cadres d’urbanisation `TOGAF` et `ArchiMate` et formalise l’architecture cible en quatre plans découplés.
