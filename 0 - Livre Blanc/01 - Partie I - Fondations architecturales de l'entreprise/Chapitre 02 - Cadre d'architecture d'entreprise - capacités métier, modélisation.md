# Chapitre 2 — Cadre d’architecture d’entreprise : capacités métier, modélisation TOGAF/ArchiMate et topologie en plans

Le déploiement d’agents autonomes en entreprise échoue rarement par insuffisance des modèles fondationnels; il échoue lorsque ces composants probabilistes sont greffés sur le système d’information hors de tout référentiel d’urbanisation [19] [20]. Sans cadre directeur, chaque unité d’affaires finance ses prototypes conversationnels, duplique les connecteurs vers les `Systems of Record (SoR)` et contourne les politiques d’identité, produisant un *Shadow Agentic IT* coûteux et inauditable [21] [20]. Le chapitre précédent a posé la rupture épistémique introduite par la couche de `Systems of Agency`, le spectre d’autonomie bornée (L0 à L4) et la dette cognitive. Ce chapitre fournit à l’architecte d’entreprise (`EA`) et à l’architecte de solutions (`SA`) l’instrumentation macro-architecturale requise pour intégrer ces flottes d’agents aux référentiels existants : cartographie des capacités métier augmentées, extension normative de `TOGAF` et d’`ArchiMate`, topologie cible en quatre plans découplés et gouvernance du portefeuille applicatif [22] [23] [24].

Cette démarche articule systématiquement deux lectures complémentaires. Sur le plan `EA`, elle ancre chaque initiative dans une chaîne de valeur mesurable, maintient la traçabilité du patrimoine et encadre les risques réglementaires et financiers (`FinOps`) [23] [25] [26]. Sur le plan `SA`, elle trace des frontières d’interface stables entre déclenchement, orchestration durable, interopérabilité et contrôle transversal [27] [28] [29]. Conformément au découpage de l’ouvrage, ce chapitre couvre la macro-urbanisation et le portefeuille TI; l’anatomie d’un `Agent Harness` et la règle 80/20 relèvent du chapitre 3, et l’ingénierie de l’`Internal Agentic Platform (IAP)` relève du chapitre 13.

## 2.1 Cartographie des capacités métier augmentées et refonte des chaînes de valeur

L’erreur stratégique la plus répandue consiste à greffer un assistant génératif sur une tâche manuelle isolée sans revoir le processus qui l’héberge. Selon le corpus `BIZBOK` (*Business Architecture Body of Knowledge*) et la 10e édition de `TOGAF`, une architecture métier rigoureuse sépare ce que l’entreprise fait — ses capacités métier (`Business Capabilities`) — de la manière dont elle les enchaîne pour livrer un résultat à un bénéficiaire — ses chaînes de valeur (`Value Streams`) [23] [30]. Une capacité métier demeure stable et indépendante des organigrammes ou des outils, tandis que son support applicatif évolue par vagues [23] [30].

### 2.1.1 De l’automatisation locale de tâches à la réingénierie des chaînes de valeur

Lorsqu’un agent accélère uniquement une micro-tâche locale — par exemple résumer un courriel avant qu’un opérateur ne recopie les champs dans deux progiciels — le gain local est absorbé par les files d’attente inter-départementales, les ressaisies et les délais de cycle globaux [30] [31]. L’augmentation agentique ne produit un effet structurel que par la cartographie croisée entre les étapes d’une chaîne de valeur et les capacités qu’elles invoquent [23] [30].

Dans des chaînes telles que le règlement de sinistres, l’octroi de prêts ou la gestion de l’approvisionnement, la latence découle de trois frictions : l’ingestion d’entrées non structurées, l’assemblage de contexte dispersé entre plusieurs `SoR` et l’escalade humaine sur des exceptions courantes [30] [31]. En décomposant la chaîne selon les guides `TOGAF Value Streams`, l’architecte supprime les transferts inutiles et réorganise le flux autour du traitement par exception [23] [30]. Les dossiers nominaux et les pré-instructions documentaires sont confiés à des acteurs cognitifs opérant sous contrat, tandis que l’expertise humaine est recentrée sur la validation des seuils critiques (`Human-on-the-Loop`) et l’arbitrage des cas ambigus [24] [32].

> **[Figure]**
> - Capacités mobilisées Réalisation métier et applicative
> - Capture et triage
> - sémantique «Agentic Capability»
> - Instruction et contrôle conformité
> - «Hybrid 80/20»
> - Décision financière
> - et règlement «Deterministic Core»
> - Gestionnaire métier «Human-on-the-Loop»
> - Processus réingénieré
> - par exception
> - Agent de triage
> - et extraction «Cognitive Actor»
> - Orchestrateur borné
> - «Cognitive Actor»
> - Système central
> - (SoR) «Deterministic SoR»
> - Réduire le délai de cycle
> - de bout en bout
> - Chaîne de valeur : Traitement de dossier
> - réalise
> - mobilise
> - mobilise
> - mobilise
> - matérialise supervise
> - augmente
> - orchestre
> - exécute contrat via passerelle
> - escalade

*Fig. 5. – Cartographie ArchiMate d’une chaîne de valeur réingénierée et de ses capacités augmentées*

La figure précédente exprime cette refonte en notation `ArchiMate` : la chaîne de valeur *Traitement de dossier* concrétise un objectif de réduction du délai de cycle en mobilisant trois capacités aux régimes d’exécution distincts [22] [23]. La capture sémantique est augmentée par un acteur cognitif dédié, l’instruction de conformité couple règles déterministes et raisonnement borné, et la passation financière reste confinée au noyau déterministe du `System of Record` [24] [31].

### 2.1.2 Cartes thermiques et critères d’éligibilité des capacités augmentées

Pour prévenir la dispersion budgétaire, l’`EA` applique sur la carte des capacités (niveaux 1 à 3) des cartes thermiques (*heat maps*) croisant potentiel d’augmentation et exposition au risque [30] [25]. Le guide de Google Cloud et le volet `Generative AI Lens` d’`AWS Well-Architected` convergent sur un principe fondamental : l’approche agentique n’est justifiée que lorsque la tâche comporte une ambiguïté sémantique réelle ou une combinatoire d’exceptions imprévisible [32] [31]. Toute capacité pilotée par des règles stables et des données structurées doit demeurer dans un workflow déterministe classique afin d’éviter la latence et la variance d’un modèle de langage [24] [31].

En croisant les principes de `BIZBOK` et les retours d’ingénierie des architectures cloud, quatre axes guident l’évaluation thermique d’une capacité candidate :

1. **Intensité sémantique des entrées** : part de documents non structurés, d’échanges textuels libres ou de divergences terminologiques entre systèmes [30] [31].
2. **Préparation des données (**`Data Readiness`**)** : présence de référentiels maîtres, de politiques d’accès et d’une chaîne de récupération documentaire gouvernée; comme le montrent les patrons de Martin Fowler et les principes de gouvernance de Microsoft, la fiabilité des systèmes génératifs repose sur une récupération hybride calibrée, le respect strict des frontières de données autorisées et des garde-fous multicouches [20] [33].
3. **Réversibilité des effets de bord** : séparation entre lecture/synthèse, écriture réversible et mutation irréversible (virement, engagement contractuel, modification d’accès) [34] [20].

4. **Tolérance à la latence et profil économique** : adéquation du délai d’inférence et de la consommation de jetons aux accords de niveau de service (`SLA`) de l’étape visée [32] [31].

### 2.1.3 Double lecture EA / SA : modèle opérationnel et frontières d’exécution

La cartographie croisée chaîne de valeur / capacités sert de charnière entre l’urbanisation `EA` et la conception `SA`.

En **lecture EA**, la carte de capacités instrumente l’analyse d’impact et la conformité [30] [25]. Lorsqu’un modèle sous-jacent est déprécié, dérive ou subit une compromission, l’architecte d’entreprise identifie immédiatement les étapes de chaînes de valeur et les parties prenantes touchées [30] [21]. Cette visibilité répond à la fonction `Map` du `NIST AI RMF 1.0` ainsi qu’aux exigences d’évaluation d’impact d’`ISO/IEC 42001:2023` [25] [26]. Chaque capacité augmentée reçoit en outre un propriétaire métier imputable du compromis entre vélocité et charge de supervision humaine [23] [26].

En **lecture SA**, ce découpage fixe les frontières de service [27] [31]. Une chaîne de valeur ne doit jamais être confiée à un agent monolithique traversant des capacités de criticités hétérogènes [24] [31]. Le `SA` segmente le flux en sous-domaines cohérents, isole la logique transactionnelle déterministe et confine le raisonnement probabiliste dans des nœuds bornés par schémas typés, selon l’anatomie et la règle 80/20 détaillées au chapitre 3 [24] [27].

> **Arbitrage EA / SA** — N’approuver aucun projet d’agent tant que la capacité visée n’est pas reliée à une étape de chaîne de valeur dans le référentiel `BIZBOK` /`TOGAF` et classée selon la réversibilité de ses effets de bord. Sur une capacité à règles stables et entrées structurées, l’`EA` et le `SA` imposent un workflow déterministe sans boucle agentique.

## 2.2 Extension du métamodèle TOGAF ADM et stéréotypes ArchiMate pour acteurs cognitifs

Les référentiels d’entreprise existants supposent des logiciels déterministes où un composant applicatif applique une logique figée et où seuls des acteurs humains exercent un jugement contextuel [22] [23]. Introduire des agents sans étendre le métamodèle conduit à les camoufler en simples API techniques (occultant leur autonomie) ou en acteurs humains (brouillant l’imputabilité juridique et la gestion des identités) [22] [21] [34].

### 2.2.1 Adaptation du cycle TOGAF ADM et de l’Architecture Repository

La méthode `ADM` de `TOGAF 10` permet d’intégrer ces composants dès la phase préliminaire par l’extension de son `Content Metamodel` [23]. L’architecte complète les phases canoniques par des livrables et portes de contrôle dédiés :

- **Phase préliminaire et Phase A (*Architecture Vision*)** : inscription de l’autonomie bornée, de la séparation probabiliste/déterministe et de la portabilité ouverte dans les principes d’architecture [23] [35]. L’`Architecture Board` intègre les exigences de la fonction `Govern` du `NIST AI RMF 1.0` et d’`ISO/IEC 42001:2023` pour fixer les mandats de délégation [25] [26].
- **Phase B (*Business Architecture*)** : ajout aux cartes de capacités et de chaînes de valeur des contrats d’intention (*Intent Contracts*), des seuils d’escalade `Human-on-the-Loop` et de la responsabilité métier associée [23] [30].

- **Phase C (*Information Systems — Data & Application*)** : recensement des sources de contexte et contrats sémantiques côté données; séparation côté applicatif entre orchestrateurs, acteurs cognitifs, passerelles d’outils et registres d’agents [23] [24] [33].
- **Phase D (*Technology Architecture*)** : modélisation des environnements d’exécution durcis, du routage d’inférence, des coffres d’identités machine (`NHI`) et du cloisonnement multi-locataires (`Silo` vs `Pooled`) [28] [19] [29].
- **Phases E, F, G et H (*Migration, Governance & Change*)** : séquencement de la transformation par paliers de risque, intégration des tests `EvalOps` comme critère d’homologation en phase G et détection de dérive comportementale en phase H pour réamorcer un cycle `ADM` [23] [24] [25] [33].

Sur le plan documentaire, cette adaptation enrichit trois artefacts canoniques de l’`Architecture Repository` de `TOGAF` : le catalogue des capacités métier intègre le niveau de criticité et le degré d’autonomie cible; la spécification des exigences d’architecture formalise les seuils de qualité, de sécurité et de réversibilité opposables aux équipes de réalisation; enfin, le document de définition d’architecture consigne la frontière exacte entre les flux déterministes conservés et les composants cognitifs introduits [23] [25] [26]. L’architecte d’entreprise évite ainsi que les spécifications d’agents ne demeurent confinées dans des dépôts applicatifs isolés sans visibilité transversale [24] [19].

### 2.2.2 Profils et stéréotypes ArchiMate 3.2 pour acteurs cognitifs et garde-fous

La spécification `ArchiMate 3.2` offre deux mécanismes d’extension officiels : la relation de spécialisation (*Specialization*) et les profils (*Profiles*) [22]. Un profil attache à une métaclasse standard un stéréotype entre guillemets (`«stéréotype»`) et des attributs gouvernés tout en préservant strictement la sémantique de base et l’héritage des relations valides pour l’échange via l’*ArchiMate Exchange File Format* [22].

Un acteur cognitif est modélisé comme une spécialisation d’`Application Component` — jamais d’un `Business Actor` — car il reste un artefact logiciel sans personnalité juridique [22] [26]. La figure suivante illustre ce métamodèle étendu sur les couches `Motivation`, `Strategy`, `Business` et `Application`.

> **[Figure]**
> - Couche Motivation (Gouvernance) Couche Strategy et Business (Capacités et Mandat) Couche Application (Acteurs cognitifs et Contrats)
> - Politique de garde-fou
> - «Guardrail Policy» Exigence d'audit et SLO
> - «Eval / Risk Gate»
> - Capability (Base ArchiMate 3.2)
> - Capacité augmentée «Agentic Capability»
> - Compétence agentique
> - «Skill / Playbook»
> - Mandat d'intention
> - «Intent Contract»
> - Responsable métier «Human-on-the-Loop»
> - Application Component
> - (Base ArchiMate 3.2)
> - Acteur cognitif «Cognitive Actor»
> - Catalogue gouverné
> - «Agent Registry»
> - Maillage multi-agents «Agent Collaboration»
> - Contrat d'outil «Tool Contract (MCP)»
> - réalise
> - spécialise
> - spécialise
> - borne
> - prouve
> - délègue
> - cadre équipe
> - fédère expose SI inventorie

*Fig. 6. – Extension du métamodèle ArchiMate 3.2 et stéréotypes normatifs pour acteurs cognitifs*

Cette structuration trace une ligne continue entre la contrainte de gouvernance et le contrat technique [22] [21] [34]. Le tableau 2.1 recense les stéréotypes retenus et leurs attributs obligatoires dans le référentiel `TOGAF` [22] [23].

| Couche `ArchiMate` | Élément | Stéréotype étendu | Rôle dans l’ADM et attributs gouvernés |
| --- | --- | --- | --- |
| `Motivation` | `Constraint` | `«Guardrail Policy»` | Bornes fermes `MAESTRO` / `OWASP` (autonomie, portée `ACL`, budget) [21] [34]. |
| `Motivation` | `Requirement` | `«Eval / Risk Gate»` | Critères d’homologation `NIST` et `ISO 42001` en phase G [25] [26]. |
| `Strategy` | `Capability` | `«Agentic Capability»` | Capacité augmentée (criticité, niveau L0–L4, propriétaire) [22] [30]. |
| `Strategy` | `Resource` | `«Skill / Playbook»` | Instructions versionnées et procédures réutilisables [22] [36]. |
| `Business` | `Actor` | `«Human-on-the-Loop»` | Superviseur humain tranchant les escalades et portant l’imputabilité [22] [24]. |
| `Business` | `Contract` | `«Intent Contract»` | Mandat délégué : objectif borné, données permises et arrêt [22] [26] [20]. |
| `Application` | `Component` | `«Cognitive Actor»` | Composant agentique (modèle abstrait, contexte, identité `NHI`) [22] [20]. |
| `Application` | `Component` | `«Agent Registry»` | Catalogue central des identités, versions et propriétaires [28] [20]. |
| `Application` | `Collaboration` | `«Agent Collaboration»` | Maillage ou motif (`Sequential`, `Handoff`, `Group Chat`) [22] [27]. |
| `Application` | `Service` | `«Tool Contract (MCP)»` | Services et mutations du SI sous contrat typé idempotent [22] [28] [35]. |

*Tableau 2.1 — Extension du métamodèle TOGAF ADM et profils ArchiMate 3.2 pour acteurs cognitifs.*

### 2.2.3 Double lecture EA / SA : traçabilité référentielle contre exécutabilité des contrats

L’extension par profils `ArchiMate 3.2` réconcilie gouvernance d’entreprise et rigueur d’implémentation [22] [24].

En **lecture EA**, les éléments stéréotypés alimentent les analyses de portefeuille, de risque et de conformité sans perturber les outils `EA` en place [22] [23]. En vue d’un audit `ISO/IEC 42001:2023` ou d’une revue `NIST AI RMF`, le référentiel fournit la preuve de traçabilité reliant chaque `«Cognitive Actor»` à son `«Intent Contract»`, à son rôle `«Human-on-the-Loop»`, aux `«Guardrail Policy»` applicables et aux `«Eval / Risk Gate»` franchis avant mise en production [22] [25] [26]. L’intégration d’un `«Agent Registry»` ferme la porte aux déploiements hors gouvernance [24].

En **lecture SA**, cette modélisation impose une discipline d’interface stricte : aucun `«Cognitive Actor»` n’accède directement à un `SoR`; il passe par un `«Tool Contract (MCP)»` gouverné et déclare ses échanges inter-agents en `«Agent Collaboration»` bornée [22] [27] [28]. Les métadonnées du profil `ArchiMate` servent de spécification amont aux manifestes déclaratifs consommés par la couche plateforme [24] [33].

> **Arbitrage EA / SA** — Interdire de modéliser un agent comme un `Business Actor` dans `ArchiMate`; le typer systématiquement en `«Cognitive Actor»` (spécialisation d’`Application Component`) rattaché à un `«Human-on-the-Loop»` et à une `«Guardrail Policy»`. Cela préserve la conformité `ArchiMate 3.2`, clarifie l’imputabilité et contraint le `SA` à doter chaque agent d’une identité machine et de contrats d’interface.

## 2.3 Architecture cible de référence en quatre plans découplés

Un métamodèle d’urbanisation reste impuissant si les équipes mélangent dans un même module l’interface utilisateur, les prompts, la gestion d’état, les appels ERP, les secrets et la télémétrie [24] [33]. Ce couplage bloque la substitution des modèles, empêche la mutualisation des outils et étend la surface d’attaque [21] [20]. L’écosystème infonuagique converge vers un découplage structurel inspiré des architectures de plans de contrôle et de plans de données [24] [28] [19] [29].

### 2.3.1 Fondement infonuagique natif : séparation des plans de contrôle, de données et d’exécution

Selon le livre blanc *Cloud Native Artificial Intelligence* (`CNAI`) de la `CNCF`, l’industrialisation de l’IA exige de séparer un plan de contrôle (*Control Plane*) déclaratif — responsable de l’ordonnancement, du routage des versions et des politiques — d’un plan de données (*Data Plane*) dédié aux flux d’inférence et aux gisements vectoriels [29]. Les architectures de référence des grands fournisseurs infonuagiques appliquent ce principe à l’entreprise agentique [24] [28] [19] :

- Microsoft (`CAF`) étend les plans de contrôle existants pour centraliser la visibilité inter-plateformes, graduer les politiques selon l’autonomie et le rayon d’impact, appliquer le moindre privilège aux identités d’agents et garantir la souveraineté des données [24] [20].
- AWS (`Prescriptive Guidance`) cloisonne les comptes entre gouvernance, passerelles partagées de modèles, coffres `OAuth 2.0` et environnements d’exécution isolés [28].
- Google Cloud déploie l’échelle multi-unités sur un modèle *hub-and-spoke* doté de périmètres `VPC Service Controls` et d’interfaces ouvertes (`A2A` et `MCP`) [19].

L’*Agentic AI Foundation* (`AAIF`) de la Linux Foundation — réunissant `MCP`, `goose` et `AGENTS.md` aux côtés d’`A2A` et `AGNTCY` — fournit des contrats indépendants des cadriciels propriétaires [35]. En parallèle, le *Technology Radar* de Thoughtworks recommande de traiter le harnais d’entreprise comme un produit léger et fédéré distribuant outils, bacs à sable et capteurs déterministes [36].

### 2.3.2 Anatomie des quatre plans de l’architecture de référence

Afin de cloisonner les responsabilités techniques et organisationnelles à travers l’ouvrage, l’architecture cible de l’entreprise agentique synthétise ces approches en **quatre plans découplés** : trois plans d’exécution superposés et un plan transversal de contrôle, de confiance et d’observabilité.

> **[Figure]**
> - Entreprise agentique —
> - Architecture cible en
> - quatre plans
> - [system]
> - Plan 1 : Expérience
> - [container]
> - Plan 2 : Orchestration
> - [container]
> - Plan 3 : Interopérabilité
> - [container]
> - Plan 4 : Confiance et
> - observabilité
> - [container]
> - «container» SoE / Portails
> - [UI, CRM]
> - Intention et HITL
> - «container» Points d'entrée
> - [API, Bus]
> - Signaux ambiants
> - «container» Workflows durables
> - [États]
> - Replay et Sagas
> - «container» Routeur 80/20
> - [Code + LLM]
> - Isole logique critique
> - «container» MCP Gateway
> - [Outils]
> - Contrats API et SoR
> - «container» Maillage A2A / AGNTCY
> - [Pairs]
> - Annuaires, Artifacts
> - «container» Mémoire et sémantique
> - [RAG, ACL]
> - Gouverne contexte
> - «container» Zero-Trust [NHI, OBO, OPA]
> - Moindre privilège
> - «container» OTel, EvalOps, FinOps
> - [Télémétrie]
> - Dérive et coûts
> - «person»
> - Opérateur / Client
> - Intention / HITL
> - «external_system» Signaux B2B
> - Événements
> - «external_system» Systems of Record
> - ERP, core banking
> - «external_system» Agents SaaS tiers
> - Éditeurs fédérés
> - Mandat [HTTPS]
> - Signal [Events]
> - Soumet
> - Démarre
> - Pilote
> - Outils [MCP]
> - Tâches
> - [A2A]
> - Contexte
> - [ACL]
> - Mute [Idempotent]
> - Fédère
> - [B2B]
> - Garde-fous
> - Portées OBO
> - Traces et coûts

*Fig. 7. – Architecture cible de référence en quatre plans découplés de l’entreprise agentique*

1. **Plan 1 — Plan d’expérience et de déclenchement** : Surface d’entrée des intentions vers le `System of Agency` [24] [19]. Il réunit les `Systems of Engagement (SoE)` humains (portails, interfaces conversationnelles, consoles de validation `Human-in/on-the-Loop`) et les points d’entrée API ou événementiels captant les signaux métiers et partenaires B2B [24] [27]. Ce plan ne porte ni logique de planification ni accès direct aux bases maîtres; il normalise l’intention et transmet le contexte d’identité initial [28] [19].
2. **Plan 2 — Plan d’orchestration et d’exécution durable** : Moteur de cycle de vie des tâches longues, garantissant la cohérence d’état face aux pannes, aux attentes humaines et aux limites de quotas [27] [31]. Il héberge le routeur arbitrant entre flux déterministes et nœuds cognitifs (voir le chapitre 3) ainsi que les topologies de coordination dirigée, collaborative ou réactive traitées dans la Partie III (chapitres 7 à 9) [27] [32] [31].
3. **Plan 3 — Plan d’interopérabilité et de contexte** : Couche d’abstraction isolant les orchestrateurs du patrimoine applicatif et documentaire [28] [35] [33]. Il regroupe la médiation verticale vers les outils et `SoR` (`MCP Gateway`), la délégation horizontale inter-agents (`A2A` et annuaires `AGNTCY`) incluant les agents `SaaS` tiers, et la couche mémoire et sémantique appliquant les contrôles `ACL` [28] [19] [35] [33]. Ces mécanismes constituent l’objet de la Partie II (chapitres 4 à 6).
4. **Plan 4 — Plan transversal de confiance, de sécurité et d’observabilité** : Plan de contrôle irriguant verticalement les trois autres plans [24] [29] [21]. Il concentre les identités non humaines (`NHI`), la délégation restreinte, les portes d’intention, la défense en sept couches contre les menaces `MAESTRO` et `OWASP`, la télémétrie distribuée, les boucles `EvalOps`, la gouvernance `FinOps` et la conformité (`NIST AI RMF`, `ISO/IEC 42001`) [24] [21] [34] [25] [26]. Ces domaines sont détaillés dans la Partie IV (chapitres 10 à 12), et leur socle d’ingénierie unifié (`IAP` et `AI Gateway`) est présenté au chapitre 13.

| Plan | Enjeu `EA` | Enjeu `SA` | Contrats d’interface | Chapitres |
| --- | --- | --- | --- | --- |
| **Plan 1 — Expérience** | Ergonomie, `HITL` /`HOTL`, rationalisation `SoE` | Normalisation, identité, découplage | Paquets typés, enveloppes, jetons | Chap. 1, 8, 14 |
| **Plan 2 — Orchestration** | Chaînes de valeur, criticité, cibles `RTO` /`RPO` | Rejeu, Sagas, plafonds d’itérations | États workflow, schémas, mandats | Chap. 3, 7–9 |
| **Plan 3 — Interopérabilité** | Réutilisation, souveraineté, portabilité | Médiation idempotente, pagination, `ACL` | Normes `MCP`, `A2A`, `AGNTCY` | Chap. 4–6 |
| **Plan 4 — Confiance (transversal)** | Conformité `ISO 42001` /`NIST`, registre, `FinOps` | Attestation `NHI`, moindre privilège, `EvalOps` | Certificats `SVID`, `OBO`, `OPA`, `OTel` | Chap. 10–13 |

*Tableau 2.2 — Matrice de responsabilité architecturale des quatre plans découplés.*

La pérennité de cette topologie tient au strict respect des contrats entre plans adjacents. Entre les Plans 1 et 2, l’interaction privilégie l’émission d’un mandat borné et d’un identifiant de corrélation, permettant au `SoE` de rester réactif ou d’attendre une validation humaine asynchrone sans bloquer de session applicative [24] [27]. Entre les Plans 2 et 3, tout appel d’outil ou de mémoire transite par des contrats typés, paginés et idempotents, de sorte que la reprise sur incident d’un orchestrateur ne duplique aucune écriture dans un `SoR` [28] [31] [35]. Enfin, le Plan 4 opère en interception obligatoire plutôt qu’en journalisation passive a posteriori : aucune délégation ou requête d’outil n’aboutit sans vérification préalable d’identité machine et de politique d’intention [24] [21] [34].

### 2.3.3 Double lecture EA / SA : résilience aux pannes transversales et isolement multi-locataires

La topologie en quatre plans offre une réponse structurée aux défaillances opérationnelles comme aux attaques multi-couches [21] [34].

En **lecture EA**, ce découplage prévient le verrouillage intégral de la pile technologique : l’entreprise peut remplacer une interface du Plan 1, faire évoluer son moteur du Plan 2 ou basculer de modèle fondationnel sans reconstruire ses connecteurs `MCP` du Plan 3 ni affaiblir l’audit du Plan 4 [29] [35] [20]. L’alignement sur le cadre `MAESTRO` de la `Cloud Security Alliance` (`CSA`) montre en outre qu’en séparant ces plans, une compromission d’écosystème ou de données (Plan 3) ne peut ni escalader librement dans la logique d’orchestration (Plan 2) ni altérer les journaux et garde-fous (Plan 4) [21] [34].

En **lecture SA**, les frontières inter-plans proscrivent les court-circuits architecturaux : aucune interface du Plan 1 ne requête directement un index vectoriel du Plan 3 sans traverser l’orchestrateur et les contrôles du Plan 4, et aucun nœud du Plan 2 ne dépend des schémas physiques d’un `SoR` [24] [28] [19]. En environnement multi-locataires, le `SA` arbitre entre l’isolement physique (`Silo`) pour les unités sensibles et la mutualisation sous quotas (`Pooled`) pour les services communs, tout en conservant un Plan 4 unifié [28] [19].

> **Arbitrage EA / SA** — Exiger que tout dossier d’architecture répartisse explicitement ses composants entre les quatre plans de référence et rejeter tout flux contournant le Plan 3 (accès direct aux `SoR`) ou le Plan 4 (secrets statiques ou absence de télémétrie). Pour le multi-locataires, mutualiser le Plan 4 de gouvernance mais cloisonner les gisements de mémoire du Plan 3 en mode `Silo` dès qu’apparaissent des données réglementées.

## 2.4 Gouvernance du portefeuille : arbitrage Acheter (agents SaaS) vs Assembler vs Construire

La multiplication des agents embarqués chez les éditeurs logiciels confronte l’architecte d’entreprise à un arbitrage économique et stratégique inédit : faut-il activer les agents natifs des progiciels `SaaS` existants, assembler une couche composable sur des plateformes managées et standards ouverts, ou construire des agents sur mesure [24] [28] [36]?

### 2.4.1 Recomposition du portefeuille applicatif face aux agents embarqués

Les cadres stratégiques de Microsoft (`CAF`), d’AWS et de Thoughtworks montrent que l’opposition binaire entre achat sur étagère et développement interne est devenue insuffisante pour gouverner les agents d’IA [24] [28] [36]. L’arbre décisionnel séquentiel du `CAF` exige d’abord de valider qu’un cas d’usage requiert réellement une capacité de raisonnement plutôt qu’un automatisme déterministe; il examine ensuite si un agent `SaaS` prêt à l’emploi suffit avant d’envisager l’assemblage faible code, le développement PaaS ou le déploiement sur infrastructure dédiée [24]. Cette hiérarchisation éclaire le positionnement de deux familles de solutions dans le patrimoine :

- **Les progiciels horizontaux formant les** `Systems of Record` **(ERP, CRM, SIRH, bureautique)** héritent des contrôles d’accès natifs de l’éditeur; leurs agents embarqués sont pertinents lorsque le processus demeure confiné au périmètre fonctionnel et de données d’un seul environnement `SaaS` [24] [20].
- **Les flux transversaux et différenciateurs inter-systèmes** s’accommodent mal d’une logique fermée propre à un seul éditeur : y contraindre l’organisation fait perdre la maîtrise des politiques d’évaluation, de l’ingénierie du contexte et du portage entre modèles [24] [36] [33].

Dès lors, hors des capacités purement déterministes qui demeurent sans agent, le portefeuille s’organise autour de trois régimes complémentaires [24] [31] [36] :

1. **Acheter (*Buy* — Agents** `SaaS` **natifs)** : activation d’agents prêts à l’emploi livrés dans les progiciels existants sur des tâches standardisées et à faible personnalisation (productivité bureautique, soutien interne, requêtes intra-progiciel) [24] [20].

2. **Assembler (*Assemble* — Plateforme composable)** : assemblage d’agents et de workflows sur des services managés faible code ou PaaS adossés aux standards ouverts (`MCP`, `A2A`) pour relier plusieurs `SoR` et `SaaS` sans réécrire les couches de base [24] [28] [35] [36].
3. **Construire (*Build* — Agents sur mesure)** : développement interne orienté code sur plateforme d’entreprise pour les capacités à forte différenciation concurrentielle, à latence stricte ou à souveraineté imposant le contrôle direct des modèles et du harnais d’exécution [24] [19] [36] [33].

### 2.4.2 Critères d’arbitrage et matrice décisionnelle du portefeuille

Deux dérives symétriques menacent le portefeuille TI : l’activation incontrôlée d’agents `SaaS` crée des silos cognitifs disjoints hors de tout contrôle centralisé, tandis que le tout-construit engendre un empilement artisanal fragile dont le coût de maintien croît avec chaque évolution de modèle ou de protocole [24] [20] [36] [33]. L’arbre de décision ci-dessous formalise le tri initial en comité d’architecture.

*Fig. 8. – Arbre décisionnel de gouvernance du portefeuille : Acheter, Assembler ou Construire*

L’arbitrage définitif croise six critères évalués conjointement par les équipes d’architecture d’entreprise, de solutions, de sécurité et de finance [24] [25] [26] [20].

| Critère d’arbitrage | Acheter (Agent `SaaS` natif) | Assembler (Plateforme composable) | Construire (Agent sur mesure) |
| --- | --- | --- | --- |
| **Différenciation métier** | Faible : productivité ou processus générique interne [24] | Moyenne : composition originale sur briques managées [24] [28] | Forte : cœur concurrentiel ou logique propriétaire [24] [36] |
| **Données et** `SoR` | Cantonnées à un seul progiciel `SaaS` [24] [20] | Flux entre plusieurs `SoR` via API et `MCP` [28] [35] | Couplage profond aux données souveraines [19] [20] |
| **Délai de déploiement** | Court (immédiat à semaines) sous gouvernance existante [24] | Modéré (semaines à quelques mois) [24] [28] | Long (mois à trimestres, durcissement inclus) [24] [36] |
| **Profil économique (**`TCO`**)** | Licences par siège ou frais d’usage éditeur [24] | Coût plateforme managée et inférence sous quotas [28] [31] | Investissement d’ingénierie et d’exploitation interne [24] [36] |
| **Maîtrise modèles et** `evals` | Opaque : modèles et seuils dictés par l’éditeur [24] [20] | Hybride : sélection de modèles et `evals` internes [24] [33] | Totale : modèles, garde-fous, capteurs et `evals` [36] [33] |
| **Verrouillage et sortie** | Élevé : dépendance feuille de route `SaaS` [24] [35] | Faible à modéré via normes `AAIF` (`MCP`, `A2A`) [35] [36] | Faible côté éditeur, dette interne gouvernée [36] [33] |

*Tableau 2.3 — Matrice décisionnelle multicritère Acheter vs Assembler vs Construire pour le portefeuille agentique.*

### 2.4.3 Portes d’homologation de l’Architecture Review Board (ARB) et clauses de réversibilité

Quel que soit le régime choisi, aucun agent ne contourne les exigences du portefeuille [24] [26] [20]. Un agent `SaaS` activé en quelques clics crée un risque critique s’il requiert des permissions excessives ou contourne la surveillance centralisée [21] [34] [20]. Conformément à la norme `ISO/IEC 42001:2023` — qui couvre explicitement les systèmes fournis par des tiers comme les développements internes — et aux cadres de gouvernance d’AWS, Microsoft et Google Cloud, l’`ARB` impose quatre verrous obligatoires [28] [19] [26] [20] :

1. **Enregistrement au catalogue (**`«Agent Registry»`**)** : déclaration du propriétaire métier, du niveau L0–L4, du rayon d’impact et de la classification des données avant toute mise en production [26] [20].
2. **Médiation aux frontières des plans** : tout agent `SaaS` dialogue avec le SI via les contrats du Plan 3 (`A2A` ou `MCP` filtré par passerelle) sous moindre privilège et quotas du Plan 4 [28] [19] [35] [20].
3. **Propriété des évaluations et journaux** : en tout régime, l’entreprise conserve ses suites `evals`, métriques de qualité et journaux d’audit pour comparer tout changement d’éditeur ou de modèle [25] [36] [33].
4. **Clauses contractuelles et techniques de réversibilité** : refus d’enfouir la logique métier dans des paramétrages fermés; exportabilité exigée des compétences, instructions et traces [35] [26] [36].

### 2.4.4 Double lecture EA / SA : arbitrages de portefeuille et dette d’intégration

L’arbitrage du portefeuille cristallise l’alignement permanent entre `EA` et `SA` [23] [24] [20].

En **lecture EA**, l’objectif consiste à concentrer l’ingénierie sur les capacités différenciatrices (*Construire* et *Assembler*) tout en prévenant la prolifération redondante d’agents `SaaS` [24] [20] [36]. Les progiciels horizontaux conservent leur rôle de `SoR`, tandis que la couche de `Systems of Agency` garde sa portabilité grâce aux standards ouverts de l’`AAIF` [35] [20]. Si les coûts ou limites d’un agent acheté freinent une chaîne de valeur, l’`EA` planifie sa bascule vers une composition ouverte [24] [35].

En **lecture SA**, ce choix dicte la maîtrise de la dette d’intégration [27] [33]. Devant un agent `SaaS`, le `SA` interpose des adaptateurs anti-corruption, des délégations bornées et des coupe-circuits contre la saturation des API ou la fuite de contexte [28] [21] [34] [20]. En régime assemblé ou construit, le `SA` consomme un harnais d’entreprise léger adossé aux chemins pavés de la plateforme interne présentée au chapitre 13 [29] [36] [33].

> **Arbitrage EA / SA** — Adopter le régime **Assembler** sur standards ouverts (`MCP`, `A2A`) comme choix par défaut pour les workflows inter-systèmes, confiner l’option **Acheter** aux commodités contenues dans un seul `SaaS`, et réserver l’option **Construire** aux capacités à forte propriété intellectuelle, souveraineté stricte ou latence critique justifiées devant l’`ARB`. Dans tous les cas, l’entreprise garde la maîtrise de ses contrats sémantiques, journaux et évaluations.

## Synthèse et transition vers le chapitre 3

Ce chapitre a posé les fondations d’urbanisation de l’entreprise agentique. La cartographie croisée `BIZBOK` /`TOGAF` arrime les agents à la refonte des chaînes de valeur plutôt qu’à l’automatisation isolée de tâches [23] [30]. L’extension du cycle `TOGAF ADM` et les profils `ArchiMate 3.2` dotent le référentiel des stéréotypes nécessaires (`«Cognitive Actor»`, `«Intent Contract»`, `«Guardrail Policy»`) pour satisfaire `NIST AI RMF` et `ISO/IEC 42001` [22] [25] [26]. L’architecture cible en quatre plans découplés — Expérience, Orchestration durable, Interopérabilité/Contexte et Confiance/Observabilité — prévient les couplages fragiles et borne la propagation des risques [28] [29] [20]. Enfin, l’arbitrage *Acheter vs Assembler vs Construire* protège le portefeuille contre l’enfermement propriétaire et la dette d’intégration [24] [35] [36].

Ces frontières macro-architecturales posées, il reste à ouvrir la boîte noire du Plan 2 au niveau d’un acteur unitaire : comment structurer le noyau d’exécution d’un agent (`Agent Harness`) et partitionner concrètement le travail entre logique déterministe et nœuds cognitifs? C’est l’objet du chapitre 3 et de sa règle hybride 80/20.
