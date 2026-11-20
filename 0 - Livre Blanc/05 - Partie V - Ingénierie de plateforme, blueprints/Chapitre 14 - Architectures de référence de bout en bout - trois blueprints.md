# Chapitre 14 — Architectures de référence de bout en bout : trois blueprints sectoriels et fédérés instanciables

Les chapitres 01 à 13 ont établi séparément chaque composant de l’entreprise agentique : stratification `SoE` / `SoA` / `SoR` et autonomie `L0–L4` (chapitre 01), cadre en quatre plans découplés (chapitre 02), harnais hybride `80/20` (chapitre 03), médiation `MCP` devant couches anti-corruption (chapitre 04), protocole `A2A` et infrastructure `AGNTCY` (chapitre 05), `RAG` gouverné par `ACL` et contrats sémantiques (chapitre 06), topologies multi-agents et `Claim-Check` (chapitre 07), maillage événementiel réactif (chapitre 08), exécution durable et Sagas (chapitre 09), sécurité `Zero-Trust` (`SPIFFE` et `OAuth 2.0 OBO`, chapitre 10), télémétrie `OpenTelemetry GenAI`, `EvalOps` et `SRE` (chapitre 11), gouvernance `OSFI E-23` / `Loi 25` / `EU AI Act` et `FinOps` (chapitre 12), enfin plateforme `IAP`, `AI Gateway` et `GitOps` (chapitre 13).

En production, le défi consiste à **composer ces briques sous contraintes contradictoires**. Un dossier de crédit bancaire exige durabilité transactionnelle et preuve d’audit ; un réseau d’approvisionnement B2B impose l’opacité entre organisations autonomes ; un environnement pharmaceutique ou de défense interdit toute sortie de données hors enclave. Ce chapitre assemble ces acquis en trois **blueprints sectoriels instanciables** (`14.1` à `14.3`), puis en dresse la **synthèse comparative non fonctionnelle** (`14.4`), selon une double lecture **EA** et **SA**. Par frontière d’étanchéité, la coexistence patrimoniale et la feuille de route relèvent du chapitre 15.

## 14.1 Blueprint 1 — Traitement transactionnel hautement réglementé (Temporal + MCP Gateway + OAuth OBO + Audit)

### 14.1.1 Contexte sectoriel et topologie en quatre plans

Le premier blueprint vise les secteurs financier, bancaire et assurantiel — octroi de crédit commercial, règlement de sinistres, conformité — où les agents préparent des mutations comptables sur les `Systems of Record` (`SoR`). Dans la taxonomie du chapitre 12, ces systèmes relèvent des paliers de risque `R3` **ou** `R4` (`OSFI E-23`), de l’article `12.1` **de la Loi 25** (décisions automatisées) et de l’`Annexe III` **de l’**`EU AI Act`. Ils opèrent aux niveaux `L2` **ou** `L3` du chapitre 01 : le système rassemble les preuves, vérifie les écarts et propose une écriture bornée, mais toute mutation pivot ou exception au-delà d’un plafond transite par une porte `Human-in-the-Loop` (`HITL`) effective.

Suivant le modèle en quatre plans du chapitre 02 et les `Golden Paths` de l’`IAP` (chapitre 13), le Blueprint 1 dissocie la planification probabiliste de l’engagement transactionnel (figure `14.1`) :

1. **Plan 1 (**`SoE`**)** : portail conseiller exposant l’avancement du dossier, le différentiel exact de mutation sur le `SoR`, les facteurs explicatifs et les pièces sources pour révision humaine.
2. **Plan 2 (**`SoA`**)** : moteur `Temporal` orchestrant 80 % du flux en code déterministe (éligibilité, plafonds, séquence Saga, minuteries `SLA`) et confinant les 20 % cognitifs dans des `Activities` isolées exécutant le harnais sous `JSON Schema` `strict: true` [339] [340].
3. **Plan 3 (**`Données et Outils`**)** : passerelle `MCP Gateway` (`agentgateway`) appliquant l’autorisation `MCP`, les règles d’`Intent Gate` (`OPA` /`Cedar`) et l’idempotence devant une couche anti-corruption (`ACL`) et une projection `CQRS` alimentée par `CDC` (`Debezium`) [341] [342].

4. **Plan 4 (**`Confiance et Audit`**)** : identités machines `SPIFFE` **/**`SPIRE`, délégation `OAuth 2.0 On-Behalf-Of` **(**`RFC 8693`**)**, télémétrie `OpenTelemetry GenAI` sans charge brute (`payload = 0`) et stockage immuable `WORM` sous `Amazon S3 Object Lock` en mode `Compliance` [343] [344] [345].

> **[Figure]**
> - Blueprint 1 — Enclave
> - Transactionnelle Réglementée (4 Plans)
> - [system]
> - «container» Plan 1 : Portail & HITL
> - [SoE / Révision Loi 25]
> - Affiche différentiel SoR
> - et preuve source
> - «container» Plan 2 : Moteur Durable
> - [Temporal HA + Harness 80/20]
> - Journalise replay, Sagas, Signals & Worker Versioning
> - «container» Plan 3 : MCP Gateway
> - [agentgateway + Intent Gate]
> - Médiation Streamable HTTP, OPA/Cedar & Idempotency-Key
> - «container» Plan 3 : Couche ACL /
> - CQRS [Debezium CDC + Projection]
> - Isole lectures SoR et sérialise mutations pivot
> - «container» Plan 4 : Identité & OBO
> - [SPIRE + STS RFC 8693]
> - Émet X.509-SVID et jetons OBO (sub, act[], aud RFC 8707)
> - «container» Plan 4 : Télémétrie &
> - WORM [OTel GenAI + S3 Object Lock]
> - Collecteur mTLS, payload=0 et archivage Compliance Mode
> - «person»
> - Conseiller / Client
> - Initie dossier crédit
> - ou sinistre (L2-L3)
> - «external_system» AI Gateway / Inférence
> - Cascade SLM/LLM
> - (PTU + Spillover)
> - «external_system» System of Record
> - Core Banking / ERP (Autorité comptable)
> - Soumet mandat
> - et valide HITL [OIDC / TLS 1.3]
> - Démarre workflow /
> - Signal approbation
> - [gRPC mTLS]
> - Appels cognitifs
> - bornés (20 %)
> - [AI Gateway]
> - Échange OBO (subject + SVID)
> - [RFC 8693]
> - tools/call + Jeton OBO + Idempotency
> - [MCP HTTP] Lit projection /Mutation pivot
> - [gRPC / REST]
> - CDC lecture /Écriture amortie
> - [BAPI / SQL]
> - Spans & traces
> - décisionnelles
> - [OTLP mTLS]
> - Journaux OPA
> - et piste OBO [OTLP / WORM]

*Fig. 53. – Architecture de référence C4 Container du Blueprint 1 — Traitement transactionnel hautement réglementé sur quatre plans*

### 14.1.2 Cinématique bout en bout : de l’intention `SoE` au scellement `WORM`

Une demande de sinistre ou de crédit suit cinq étapes contractuelles :

1. **Ouverture durable** : après authentification `OIDC` au `SoE`, le service frontal démarre un `Workflow` `Temporal` sous identifiant métier unique servant de clé d’idempotence. L’état initial est répliqué de façon synchrone sur trois zones de disponibilité (`AZ`) avant l’acquittement client [339] [346]. Pour absorber les pointes saisonnières (fin d’exercice ou événements climatiques en assurance), l’espace de noms bascule entre les modes `On-Demand Capacity` et `Provisioned Capacity` dimensionné en unités `TRU` [347].
2. **Extraction documentaire** `80/20` **et** `Claim-Check` : une `Activity` invoque l’`AI Gateway` pour analyser les justificatifs. Les définitions d’outils et consignes stables restent en préfixe pour préserver le cache `KV`, tandis que les extractions routinières sont routées vers un `SLM` spécialisé. Les pièces volumineuses et synthèses typées transitent par `Artifact URI` (chapitre 07) afin de ne pas alourdir l’historique d’événements `Temporal`.
3. **Échange** `OAuth 2.0 OBO` **(**`RFC 8693`**) devant la** `MCP Gateway` : pour lire le dossier client sur la projection `CQRS`, le worker découvre les métadonnées de ressource protégée (`RFC 9728`) et du serveur d’autorisation (`RFC 8414`) [341], puis soumet au *Security Token Service* (`STS`) le `subject_token` de l’initiateur et son propre `actor_token` `SPIFFE` [343]. Le `STS` émet un jeton restreint (`read:policy`) ciblé sur l’audience exacte de la passerelle (`RFC 8707`) et porteur de la revendication structurée `act` [341] [343]. Conformément à la spécification `MCP 2025-11-25`, la passerelle agit en serveur de ressources `OAuth 2.1`, valide l’audience cible et interdit strictement le relais passif de jetons (*token passthrough*) [341] [342].
4. **Décision déterministe, pause** `HITL` **et** `Intent Gate` : les règles impératives (ratios financiers, plafonds, exclusions) s’exécutent hors fenêtre cognitive. Si un seuil `HITL` est atteint, le `Workflow` suspend
  son cours sans consommer de processus grâce à une attente durable (`wait_condition`) bornée par minuteur `SLA` (chapitre 09). Sur approbation ou rectification dans le `SoE`, un `Signal` (ou `Update`) réveille l’instance. Un second échange `RFC 8693` limite alors la portée à l’outil mutateur (`write:settlement`), que l’`Intent Gate` (`OPA` /`Cedar`) dans `agentgateway` confronte au mandat, au plafond et à l’identifiant d’approbation humaine [343] [342].
5. **Saga compensatoire et archivage** `WORM` : en cas d’échec après l’action pivot (ex. échec d’émission du paiement après réservation comptable), `Temporal` exécute en ordre inverse les compensations enregistrées (chapitre 09). En clôture, la trace `OpenTelemetry GenAI` (`trace_id`, `spiffe.workload.id`, chaîne `(sub, act[])`, motifs principaux sans `RP` bruts) est versée dans un compartiment versionné `S3 Object Lock` en mode `Compliance` [344] [345]. Ce mode interdit toute suppression ou réécriture jusqu’à la date d’échéance — même par l’administrateur racine — et permet de placer une mise en attente légale (*Legal Hold*) indépendante en cas de litige [344]. Adossé à l’évaluation *Cohasset Associates* pour `SEC 17a-4`, `FINRA` et `CFTC`, cet archivage soutient directement les vérifications de la troisième ligne de défense (`3LoD`) [344].

### 14.1.3 Continuité multi-régions, versionnement en vol et lecture EA / SA

La mise en production s’appuie sur trois verrous d’exploitation :

- **Réplication** `3-AZ` **et multi-régions** : nativement, `Temporal Cloud` garantit `RPO = 0` et `RTO ≈ 0` sur perte d’une zone de disponibilité [339] [346]. L’activation de la réplication asynchrone multi-régions ou multi-nuages assure `RPO < 1 minute` et `RTO < 20 minutes` avec routage `DNS` transparent et basculement automatique, à condition de maintenir les workers en `Active/Hot-Passive` ou `Active/Active` sur les deux régions [339] [346]. À défaut de réplication HA, les sauvegardes s’effectuent toutes les 4 heures [346].
- **Évolution sans rupture (**`Worker Versioning`**)** : les dossiers réglementés restent ouverts plusieurs jours ou semaines en attente de pièces. Pour modifier le code sans déclencher d’erreur de non-déterminisme au rejeu, `Worker Versioning` associe chaque déploiement à un nom logique et un `Build ID`, et maintient les workflows déjà démarrés en mode `Pinned` sur leur version initiale, tandis que les nouveaux adoptent la révision courante [340].
- **Résilience aux erreurs** `429` **et repli** `L0` : les saturations `LLM` (`HTTP 429`) sont absorbées par recul exponentiel et gigue dans l’`Activity` (avec bascule vers une terminaison homologuée sur l’`AI Gateway`). Si un coupe-circuit cognitif s’ouvre (`FORCED_OPEN`, chapitre 11), le flux déroute les dossiers vers le traitement humain déterministe `L0`.

En **lecture EA**, ce blueprint assure l’imputabilité exigée par `OSFI E-23` et la `Loi 25` (`Agent Owner`, piste `WORM`, recours humain effectif) tout en protégeant les licences `SoR` via `CQRS`. En **lecture SA**, il élimine l’état volatile, bloque le *token passthrough* devant `MCP` et sécurise le rejeu multi-semaines [340] [341] [344].

| Plan | Composants | Contrats clés | Résilience et pannes | Preuve d’audit |
| --- | --- | --- | --- | --- |
| **Plan 1 (**`SoE`**)** | Portail conseiller, écran différentiel `HITL` | `OIDC`, `Loi 25 art. 12.1` (ch. `01`, `12`) | Réessai client idempotent | Trace de révision humaine effective |
| **Plan 2 (**`SoA`**)** | `Temporal HA` + `Harness 80/20` | `Worker Versioning` (`Pinned`), `JSON Schema` | `3-AZ` (`RPO=0`), multi-régions (`RPO<1m`, `RTO<20m`) [339] [346] | Historique rejouable et `Build ID` [340] |
| **Plan 3 (**`Data`**)** | `agentgateway` + `OPA` + `ACL` /`CQRS` | `MCP OAuth 2.1`, `RFC 8707`, idempotence [341] | Rejet *token passthrough*, Sagas post-pivot | Journal `OPA` et état idempotent [342] |
| **Plan 4 (**`Audit`**)** | `SPIRE` + `STS` + `OTel` + `S3 Lock` | `RFC 8693` (`act[]`), `OTel`, `Compliance` [343] [344] | Rotation `SVID` en mémoire ; `mTLS` `OTel` | Piste `(sub, act[])` sous `S3 Object Lock` [344] |

*Tableau 14.1 — Profil d’assemblage, contrats et garanties du Blueprint 1 (Traitement transactionnel hautement réglementé).*

> **Arbitrage EA / SA** — Sur les processus transactionnels `R3` –`R4`, l’`EA` interdit l’écriture directe dans un `SoR` et impose l’archivage `WORM` (`S3 Object Lock Compliance` ou équivalent) des traces `(sub, act[])` et décisions `HITL` [343] [344]. Le `SA` confine l’inférence dans des `Activities` `Temporal` en `Worker Versioning Pinned`, impose l’échange `OAuth 2.0 OBO` (`RFC 8693` + `RFC 8707`) devant la `MCP Gateway` et active la réplication `Temporal` multi-régions avec workers `Active/Hot-Passive` [339] [346] [340] [341].

## 14.2 Blueprint 2 — Maillage inter-départemental et partenaires B2B (A2A + AGNTCY/OASF + Event Mesh)

### 14.2.1 Contexte sectoriel et modèle hybride à deux strates

Le deuxième blueprint traite les chaînes de valeur transversales et étendues aux partenaires externes : approvisionnement *Source-to-Pay*, litiges fournisseurs, douanes et logistique impliquant Achats, Juridique, Finance et agents `SaaS` tiers. Aucune équipe ne gouverne les systèmes internes d’un partenaire externe, et chaque grand département évolue à son propre rythme. L’invariant d’**opacité inter-domaines** (chapitre 05) proscrit donc toute exposition directe des serveurs `MCP` ou des bases de mémoire d’un domaine hors de sa frontière.

Pour allier visibilité contractuelle globale et autonomie locale, ce blueprint déploie le **patron hybride à deux strates** du chapitre 08 (figure `14.2`) :

- **Strate macro-réglementaire fédérée** : un *Process Manager* durable pilote les jalons contractuels, délais `SLA` et escalades entre domaines internes et partenaires B2B via `A2A v1.0` et l’infrastructure `AGNTCY` (`OASF`, `ADS`, `SLIM` /`MLS`) [348] [349].
- **Strate intra-domaine chorégraphiée** : à l’intérieur des domaines et entre sites internes, un `Event Mesh` (`Solace` ou `Kafka`) diffuse des événements `CloudEvents` conformes aux contrats `AsyncAPI 3.0` vers des agents ambiants réactifs, chacun conservant ses outils `MCP` privés [350] [351] [352].

> **[Figure]**
> - Strate Fédérée B2B (A2A
> - & AGNTCY)
> - [system]
> - Strate Intra-Domaine :
> - Event Mesh
> - [system]
> - «container» Passerelle A2A B2B
> - [A2A v1.0 + AgentCard]
> - Valide schémas, TLS 1.3, anti-SSRF & CancelTask
> - «container» Annuaire AGNTCY ADS
> - [OASF + OCI/ORAS + Sigstore]
> - Indexe capacités fédérées
> - et atteste la provenance
> - «container» Transport SLIM / MLS
> - [Pub/Sub + E2EE MLS]
> - Traverse pare-feu B2B sans exposition entrante
> - «container» Event Mesh Hybride [Solace DMR / Kafka Linking]
> - CloudEvents, AsyncAPI 3.0
> - & files Retry / DLQ
> - «container» Agents Domaine Achats
> - [Agents ambiants + MCP GW]
> - Chorégraphie intra-domaine
> - sous plafond ce_ttl
> - «container» Agents Domaine Finance
> - [Agents ambiants + MCP GW]
> - Rapprochement factures
> - et projection SoR
> - «container» Process Manager Macro
> - [Orchestrateur Durable]
> - Pilote jalons SLA, quorum & compensations
> - «external_system» Agent Partenaire B2B
> - Agent SaaS / Fournisseur
> - (Opaque A2A / SLIM)
> - Délègue Task &
> - reçoit Artifacts [A2A SSE / Webhook]
> - Découvre & vérifie
> - fiche OASF [ADS / Sigstore]
> - Chiffre session
> - externe [MLS Group E2EE]
> - Échange Tasks &
> - Artifacts signés
> - [SLIM Sortant]
> - Commandes & jalons
> - [CloudEvents]
> - Diffuse événements
> - Achats [Retry / Backpressure]
> - Diffuse événements
> - Finance [Retry / Backpressure]

*Fig. 54. – Architecture de référence C4 Container du Blueprint 2 — Maillage inter-départemental et B2B via A2A, AGNTCY/OASF et Event Mesh*

### 14.2.2 Fédération `AGNTCY` /`OASF`, délégation `A2A` et traversée B2B `SLIM` /`MLS`

L’interopérabilité horizontale entre le *Process Manager*, les façades départementales et les pairs B2B s’appuie sur quatre verrous :

1. **Catalogue** `AGNTCY ADS` **et taxonomie** `OASF` : chaque façade interne et chaque partenaire B2B déclare ses capacités, compétences et interfaces selon le modèle ouvert `OASF` (*Open Agentic Schema Framework*) publié dans l’`Agent Directory Service` **(**`ADS`**)** [349]. Comme établi au chapitre 05 (stockage adressable `OCI` /`ORAS` et provenance `Sigstore`), l’entreprise ne consomme en production que les fiches répliquées et approuvées dans le miroir interne du registre central d’agents.
2. **Authentification sur** `Agent Card` `A2A` **et fédération** `SPIFFE` : avant toute délégation, la passerelle `A2A` valide l’`Agent Card` (`/.well-known/agent-card.json`) signée (canonisation `JWS`, chapitre 05) et
  négocie le schéma déclaré dans `securitySchemes` (`OAuth 2.0`, `OIDC` ou fédération `mTLS` par *Trust Bundles* `SPIFFE` entre entités appairées) [348]. Respectant la spécification `A2A`, l’identité utilisateur n’est jamais placée dans le corps `JSON-RPC` : elle reste strictement véhiculée et vérifiée au niveau du transport `TLS 1.3` et des en-têtes `HTTP` [348].
3. **Délégation asynchrone (**`SSE`**, Webhooks et** `SLIM` **/**`MLS`**)** : lorsque le partenaire expose une terminaison `HTTPS` mutuellement authentifiée, le *Process Manager* choisit l’une des liaisons normalisées (`JSON-RPC`, `gRPC` ou `HTTP+JSON/REST`) et soumet une `Task` `A2A` avec notifications push par webhook ou diffusion en continu `SendStreamingMessage` (`SSE`) [348]. Si les pare-feu B2B interdisent tout port entrant ou si des relais intermédiaires sont non fiables, les échanges basculent sur le transport `SLIM` d’`AGNTCY` avec chiffrement de groupe `MLS`, maintenant des sessions chiffrées de bout en bout sur connexions sortantes uniquement [349].
4. **Défense des frontières (**`ASI07` **/**`ASI08`**) et coupure** `CancelTask` : tout `Artifact` (bon de commande ou avis logistique structuré) reçu d’un pair externe est traité comme donnée non fiable. La passerelle `A2A` applique validation `JSON`, protection anti-`SSRF` sur toute `URI` distante conformément aux considérations de sécurité `A2A`, filtrage d’injection indirecte avant remise au *Process Manager* et émission de `CancelTask` dès dépassement de `SLA` ou de budget `FinOps` [348].

### 14.2.3 Chorégraphie intra-domaine sur `Event Mesh` et lecture EA / SA

À l’intérieur des domaines de l’entreprise, les jalons issus du *Process Manager* et les flux opérationnels alimentent l’`Event Mesh` :

- **Contrats** `CloudEvents` **/**`AsyncAPI 3.0` **et contrôle d’écho** : chaque événement embarque `ce_correlationid` et un plafond de sauts `ce_ttl` prévenant les boucles d’écho sémantiques (chapitre 08). Les agents ambiants dissocient la lecture courtier de l’appel `LLM` et bornent les messages en vol (`MaxAckPending` ou `max.poll.records`) afin d’éviter les rééquilibrages de partitions sous latence variable.
- **Topologies multi-sites** `Solace DMR` **et** `Kafka Cluster Linking` : en déploiement hybride multi-nuages et périphérie, `Solace` relie les courtiers par *Dynamic Message Routing* (`DMR`) [351]. Sa réplication inter-centres s’appuie sur `Config-Sync` (et la propagation automatique des files durables) tout en respectant les transactions locales ou `XA` sur le site de secours : le mode **synchrone** assure `RPO = 0` mais bride le débit d’un producteur bloquant selon la latence aller-retour inter-sites, tandis que le mode **asynchrone** préserve le débit nominal au prix d’un `RPO` non nul sur panne brutale [350]. Après basculement, les abonnements avec *wildcards* chevauchants sur les ponts sont interdits pour prévenir toute réinjection en boucle vers le courtier d’origine [350]. Sur socle `Kafka` **/**`Confluent`, `Cluster Linking` réplique les partitions octet par octet sans `Kafka Connect` ni `MirrorMaker 2` et évite la décompression-recompression des lots, en conservant des *offsets* globalement identiques qui réduisent fortement le `RTO` de reprise sous mode `KRaft` [352].
- **Gestion des poisons sémantiques** : les échecs répétés de schéma ou de modèle basculent sur des files `Retry` non bloquantes puis une `Dead-Letter Queue` (`DLQ`) enrichie pour arbitrage humain ou traitement déterministe.

En **lecture EA**, ce blueprint protège l’autonomie des départements et facilite le remplacement des fournisseurs `SaaS` grâce au vocabulaire commun `OASF`, tout en maintenant l’imputabilité macro sur le *Process Manager*. En **lecture SA**, il étanchéifie `A2A` (externe), `Event Mesh` (interne) et `MCP` (local), tout en prévenant `SSRF`, boucles de réinjection et perte d’*offsets* au basculement [348] [350] [352].

| Couche ou flux | Technologie et standard | Frontière d’autorité et sécurité | Résilience et pannes |
| --- | --- | --- | --- |
| **Découverte fédérée** | `AGNTCY ADS` + `OASF` (`OCI` /`Sigstore` ch. `05`) [349] | Miroir interne gouverné ; rejet des fiches non signées | Cache catalogue ; tolère une coupure temporaire du pair |
| **Délégation externe** | `A2A v1.0` (`Tasks`, `SSE`, Webhooks, `Agent Card`) [348] | Opacité stricte (zéro `MCP` exposé) ; auth hors `JSON` ; anti-`SSRF` [348] | Reprise asynchrone par ID ; `CancelTask` sous `SLA` [348] |
| **Transport B2B** | `AGNTCY SLIM` + chiffrement `MLS` [349] | Chiffrement bout en bout ; connexions sortantes seules | Streaming faible latence ; resynchronisation `MLS` |
| **Maillage interne** | `Event Mesh` (`Solace DMR`, `Cluster Linking`, `CloudEvents`) [350] [351] [352] | Plafond `ce_ttl`, `AsyncAPI 3.0`, domaines sous `MCP GW` | `Retry` /`DLQ` ; *offsets* identiques (`Cluster Linking`) ou `DR` `Solace` [350] [352] |

*Tableau 14.2 — Frontières de découplage, protocoles et résilience du Blueprint 2 (Maillage inter-départemental et B2B).*

> **Arbitrage EA / SA** — Adopter le patron hybride à deux strates pour toute chaîne multi-départements ou B2B : l’`EA` proscrit la chorégraphie pure sans *Process Manager* durable pour les jalons contractuels et exige une fiche `OASF` signée et enregistrée avant toute connexion externe [348] [349]. Le `SA` garde chaque domaine opaque derrière sa passerelle `A2A`, déploie `SLIM` /`MLS` face aux pare-feu restrictifs, borne l’`Event Mesh` par `ce_ttl` et `DLQ` et arbitre entre `Cluster Linking` et réplication `Solace` synchrone/asynchrone selon la contrainte `RPO` /latence inter-sites [350] [352].

## 14.3 Blueprint 3 — Exploitation souveraine à haute confidentialité (AI Gateway locale + RAG ACL + microVM)

### 14.3.1 Contexte sectoriel et périmètre *Zero Egress*

Le troisième blueprint répond aux impératifs de la recherche pharmaceutique, de la défense, des dossiers cliniques et des secrets industriels soumis au régime physique `Silo` (chapitres 02, 06 et 12). Aucun jeton de prompt, fragment documentaire ni renseignement personnel sensible (`RP` sous Loi 25) ne quitte le périmètre interne vers une API infonuagique publique. L’architecture doit simultanément bloquer trois risques majeurs : l’exécution de code généré arbitraire (`OWASP ASI05`), la fuite inter-chercheurs par similarité vectorielle (`ASI06` / `LLM08`) et la compromission de l’hôte ou de l’hyperviseur dans un hébergement souverain mutualisé.

Comme l’illustre la figure `14.3`, le Blueprint 3 déploie une enclave Kubernetes dépourvue de route sortante vers Internet (*Zero Egress*), unissant une `AI Gateway` **locale** avec inférence confidentielle, un `RAG` **à triple contrôle d’accès** et une **exécution en** `microVM`.

> **[Figure]**
> - Blueprint 3 — Enclave
> - Souveraine Sur Site
> - (Air-Gapped)
> - [system]
> - «container» AI Gateway & EPP [Envoy / Gateway API Inference]
> - Routage KV-cache aware, quotas TPM & Zéro Egress
> - «container» Inférence Confidentielle
> - [llm-d + vLLM / NIM (CoCo)]
> - CPU SEV-SNP/TDX + GPU TEE
> - (Mémoire chiffrée)
> - «container» Attestation & KMS Local
> - [NRAS / Trustee / SPIRE]
> - Vérifie enclave avant déchiffrement des poids
> - «container» Agent Sandbox [WarmPool + Firecracker / Kata]
> - Exécution code & harnais
> - en microVM (≤125 ms) «container» Moteur ReBAC [OpenFGA (ListObjects)]
> - Résout droits utilisateur avant recherche vectorielle
> - «container» Index Vectoriel Silo
> - [Qdrant (is_tenant / Silo)]
> - Segments filtrés par ACL & recherche hybride RRF
> - «container» Base Relationnelle RLS
> - [PostgreSQL (Row Security)]
> - Mémoire & métadonnées
> - verrouillées par session
> - «person»
> - Chercheur / Clinicien
> - Accès interne authentifié
> - (Haute confidentialité)
> - Requête métier (Jeton OIDC interne)
> - [mTLS SPIFFE] Demande objets
> - autorisés [gRPC / ListObjects]
> - Recherche hybride
> - filtrée par IDs
> - [TLS interne]
> - Lit/écrit contexte sous politique RLS
> - [SQL + tenant_id]
> - Inférence locale (aucune sortie WAN)
> - [OpenAI API]
> - Aiguillage EPP (préfixe KV chaud)
> - [gRPC / HTTP]
> - Preuve matérielle SEV-SNP / TDX / GPU
> - [Attestation]

*Fig. 55. – Architecture de référence C4 Container du Blueprint 3 — Enclave souveraine avec AI Gateway locale, RAG ACL et microVM*

### 14.3.2 `AI Gateway` locale, routage `EPP` et inférence confidentielle (`vLLM` /`llm-d` ou `NIM` sous `CoCo`)

L’exploitation interne de modèles ouverts spécialisés se heurte souvent sur Kubernetes aux répartiteurs *round-robin* qui brisent la localité du cache de préfixes `KV` et allongent le *Time to First Token* (`TTFT`). Ce blueprint déploie donc une pile consciente de l’état d’inférence :

1. **Passerelle locale et** `Endpoint Picker` **(**`EPP`**)** : l’`AI Gateway` (`agentgateway` ou `Envoy` intégrant `Kubernetes Gateway API Inference Extension`) applique quotas `TPM`, télémétrie `OpenTelemetry` locale et filtrage réseau, puis route vers un `InferencePool` piloté par l’`Endpoint Picker` **(**`EPP`**)** [342] [353]. L’`EPP` exploite en temps réel la profondeur des files d’attente, la localité du cache `KV` et les adaptateurs `LoRA` chargés pour sélectionner la réplique optimale [353].
2. **Moteur** `llm-d` **/** `vLLM` **ou** `NVIDIA NIM` : l’enclave s’appuie soit sur la pile CNCF `llm-d` orchestrant `vLLM` (*Well-Lit Paths* : routage par préfixe, cache hiérarchisé, désagrégation *prefill/decode*), dont les bancs d’essai documentent jusqu’à **3× plus de débit de sortie**, un `TTFT` **2× plus rapide** et **40 % de réduction du** `TTFT` **et de l’**`ITL` sur Google Vertex sous licence Apache 2.0 [354], soit sur des conteneurs durcis `NVIDIA NIM` miroirs en registre privé lorsque le support `NVIDIA AI Enterprise` est exigé (chapitre 13).
3. **Enclaves** `NVIDIA Confidential Containers` **(**`CoCo`**)** : lorsque les grappes GPU résident chez un hébergeur souverain externe ou sont partagées entre entités, les pods d’inférence s’exécutent via `CoCo`, **Kata Containers** et `NVIDIA GPU Operator` (`cc-manager`, `VFIO passthrough` et `Kata Sandbox Device Plugin`) au-dessus d’enclaves CPU (`AMD SEV-SNP` ou `Intel TDX`) et GPU en mode `Confidential Computing` [355]. La mémoire demeure chiffrée avec vérification d’intégrité, et un service d’attestation cryptographique distant valide l’état de la `TEE` avant la libération des secrets ou poids de modèles déchiffrés [355].

### 14.3.3 Pipeline `RAG` souverain : `OpenFGA`, `Qdrant` partitionné et `PostgreSQL RLS`

Parce qu’un moteur vectoriel classe par proximité sémantique sans notion d’habilitation, le Blueprint 3 découple l’indexation de l’autorisation par trois verrous :

- **Résolution relationnelle** `OpenFGA` **(**`ReBAC`**)** : projet CNCF inspiré de Zanzibar, `OpenFGA` modélise les relations hiérarchiques (essais cliniques, dossiers, documents, équipes) [356]. Avant construction du contexte `LLM`, le pipeline `RAG` applique les primitives `ListObjects` (pré-filtrage) ou `BatchCheck` (post-filtrage, chapitre 06), rendant toute révocation immédiate sans ré-indexation vectorielle [356].
- **Isolation vectorielle** `Qdrant` : créer une collection par groupe alourdit la mémoire et bute sur la limite par défaut de **1 000 collections** par grappe sur Qdrant Cloud [357]. L’architecture privilégie donc le partitionnement par charge utile `is_tenant: true` ou le *Tiered Multitenancy* (qui regroupe les petits locataires sur un *shard* partagé et promeut les plus volumineux vers des *shards* dédiés) filtré par `OpenFGA`, tout en réservant le régime `Silo` physique (collections ou grappes distinctes) aux entités juridiques ou classifications incompatibles [357].
- **Verrou moteur** `PostgreSQL Row-Level Security` **(**`RLS`**)** : les métadonnées, la mémoire épisodique et les vues `Text-to-SQL` activent `ENABLE ROW LEVEL SECURITY` [358]. Lorsqu’aucune politique explicite ne s’applique, PostgreSQL impose un refus par défaut (*default-deny*) et évalue le prédicat d’isolation **avant toute condition ou fonction utilisateur** (hors fonctions `leakproof`), neutralisant toute fuite même si un outil `MCP` omet une clause de filtrage [358].

### 14.3.4 Confinement `microVM` (`Agent Sandbox` + `Firecracker` /`Kata`) et lecture EA / SA

Lorsque les agents exécutent du code analytique ou manipulent des fichiers sensibles (`OWASP ASI05`), le runtime `runc` est remplacé par des `microVM` :

- **Contrôleur** `Kubernetes agent-sandbox` : sous Kubernetes `1.29+` (validation `CEL` des `CRD`), `agent-sandbox` orchestre des environnements isolés à identité stable via `Sandbox`, `SandboxTemplate`, `SandboxClaim` et `SandboxWarmPool`, déléguant le noyau à `gVisor` ou `Kata Containers` via `RuntimeClass` [359].
- **Spécification quantitative** `Firecracker` : testée en intégration continue, la `microVM` `Firecracker` affiche un surcoût mémoire VMM **≤ 5 MiB** (1 vCPU, 128 MiB RAM, hors `MMDS`), atteint `/sbin/init` en **≤ 125 ms** (socket API en ~12 ms temps réel / 8 ms CPU), conserve **plus de 95 % de la performance CPU native** et n’ajoute que **0,06 ms** de latence réseau moyenne [360]. Couplée à `SandboxWarmPool` et à une politique réseau *Zero Egress*, l’isolation matérielle reste quasi instantanée [359] [360].

En **lecture EA**, ce blueprint concilie automatisation analytique et souveraineté stricte (`Loi 25` `Silo`, `ÉFVP` maîtrisée, contrôle des poids et traces). En **lecture SA**, il marie réactivité (`EPP`, `llm-d`, `WarmPool`) et défense en profondeur matérielle (`CoCo` + `Firecracker` /`Kata`) comme relationnelle (`OpenFGA` + `PostgreSQL RLS`) [359] [360] [355] [353] [358] [356].

| Couche | Briques assemblées | Mécanisme d’isolation ou d’accélération | Limite ou coût |
| --- | --- | --- | --- |
| **Inférence locale** | `AI Gateway` + `EPP` + `llm-d` (`vLLM`) ou `NIM` [353] [354] | Cache `KV` et files via `EPP` ; jusqu’à `2×` `TTFT` et `3×` débit (`llm-d`) [353] [354] | `CAPEX` GPU fixe ; maintien local des modèles |
| **Calcul confidentiel** | `NVIDIA CoCo` + `Kata` + `SEV-SNP` /`TDX` + GPU Operator [355] | Mémoire chiffrée et attestation avant libération des clés [355] | Matériel `TEE` requis et service d’attestation interne |
| `RAG` **gouverné** | `OpenFGA` + `Qdrant` (`is_tenant` / `Silo`) + `PostgreSQL RLS` [357] [358] [356] | `ACL` pré-prompt, partition `HNSW` et refus moteur par défaut (`RLS`) [357] [358] | Latence `ReBAC` à maîtriser par cache court (ch. `06`) |
| **Exécution code** | `agent-sandbox` (`WarmPool`) + `Firecracker` / `Kata` [359] [360] | Noyau dédié, démarrage `≤ 125 ms`, `≤ 5 MiB`, `Zero Egress` [360] | Mémoire réservée pour les `WarmPools` actifs |

*Tableau 14.3 — Contrôles de souveraineté, d’isolation mémoire et d’accélération du Blueprint 3 (Haute confidentialité).*

> **Arbitrage EA / SA** — Imposer le périmètre *Zero Egress* et le cloisonnement `Silo` pour toute charge manipulant secrets industriels, données de santé ou dossiers classifiés : l’`EA` bannit les API externes, exige `Confidential Containers` (`CoCo` + attestation) sur tout nœud opéré par un tiers et impose l’auditabilité du filtrage `ACL` pré-prompt [355] [356]. Le `SA` assemble `agent-sandbox` (`SandboxWarmPool` sur `Firecracker` /`Kata`), `EPP` + `llm-d` /`vLLM` (ou `NIM`) et le double verrou `OpenFGA` /`Qdrant` + `PostgreSQL RLS` contre toute fuite inter-locataires [359] [360] [353] [357] [358].

## 14.4 Synthèse comparative non fonctionnelle : latence p95, débit, RPO/RTO, enveloppe FinOps et équipes

L’arbitrage entre ces trois blueprints — ou leur composition sur un même socle `IAP` — repose sur cinq critères non fonctionnels. Les chiffres ci-dessous distinguent rigoureusement les garanties normatives vérifiées des **cibles de dimensionnement d’architecture de référence** servant aux dossiers `ARB` et `FinOps`.

### 14.4.1 Budget de latence `p95` et profils de débit

La latence `p95` totale somme le plan de contrôle, la médiation `MCP` /`A2A` et l’inférence (`TTFT` + `TPOT`). Sur le socle système, `SPIFFE` renouvelle les certificats en mémoire via `Envoy SDS` sans surcoût réseau par requête ; `agentgateway` et `OPA` ajoutent quelques millisecondes ; `Temporal Cloud` maintient un `SLO` `p99` **de 200 ms par région** sur les requêtes workers [347] ; et `Firecracker` ajoute **0,06 ms** de latence réseau moyenne [360]. La variance majeure provient donc de l’inférence et des appels externes. En gabarits de conception sous la règle `80/20` :

1. **Blueprint 1** : un cycle de préparation (projection `CQRS` + 2 à 3 appels `SLM` /`LLM`) vise une **cible machine** `p95` **de 3 à 8 secondes** avant la pause `HITL` asynchrone ; le débit se règle en actions par seconde (`On-Demand` ou `Provisioned Capacity` en `TRUs` sous `Temporal`) [347], tandis que `CQRS` /`CDC` protège le `SoR`.
2. **Blueprint 2** : l’`Event Mesh` distribue les événements intra-sites en **dizaines de millisecondes** (hors réplication synchrone inter-sites), alors qu’une `Task` `A2A` B2B s’inscrit dans une **cible** `p95` **de dizaines de secondes à plusieurs minutes** (ou heures par webhook) [348] [350]. Les courtiers `Solace` ou `Kafka` absorbent les rafales grâce à la régulation `TPM` (*backpressure*) [351] [352].
3. **Blueprint 3** : l’alignement du cache `KV` (`EPP` + `llm-d`, jusqu’à **2×** `TTFT` et **3× débit** [354]) et le filtrage `OpenFGA` /`Qdrant` visent une **cible** `p95` **interactive de 1,5 à 4 secondes** en `RAG` à tour unique, et **4 à 12 secondes** avec exécution de code en `microVM` pré-chauffée (`WarmPool`) [359] [360]. Le débit dépend directement de la bande passante `HBM` des GPU disponibles.

### 14.4.2 Objectifs `RPO` /`RTO` et continuité de service

Suivant les piliers fiabilité d’AWS et d’Azure — où le `RTO` borne la durée maximale d’arrêt sur sinistre unique (distinct du `MTTR` moyen) et le `RPO` la perte temporelle maximale tolérée [361] [362] — les trois blueprints adoptent des topologies graduées :

- **Blueprint 1** : `Temporal` garantit `RPO = 0` et `RTO ≈ 0` sur panne de zone (`3-AZ`) et `RPO < 1 minute` / `RTO < 20 minutes` en réplication multi-régions (ou multi-nuages) sous `SLA` de **99,99 %**, avec archives `WORM` multi-zones [339] [346] [347] [344].
- **Blueprint 2** : `Solace` propose soit la réplication synchrone (`RPO = 0`, bridée par le RTT réseau), soit l’asynchrone (`RPO` faible, basculement coordonné en quelques minutes) [350] ; sous `Kafka`, `Cluster Linking` préserve des *offsets* identiques et raccourcit le `RTO` face à `MirrorMaker 2` [352].
- **Blueprint 3** : pour éviter de doubler un `CAPEX` GPU onéreux en actif-actif, le compromis réaliste place les données (`PostgreSQL`, `Qdrant`, `OpenFGA`, `SPIRE`) en **actif-passif à chaud (**`Warm Standby`**)** (`RPO` de quelques secondes à 5 minutes cible) et la réserve GPU en mode `Pilot Light` ou dégradé sur `SLM` critiques (`RTO` cible de 15 à 60 minutes) [355] [361] [362].

### 14.4.3 Enveloppe `FinOps` et modèle d’équipes (`Team Topologies`)

Alors que **98 %** des équipes `FinOps` gèrent des dépenses d’IA en 2026 [363], le pilotage exige d’allouer d’abord les coûts par périmètre métier à travers les six modèles tarifaires (API à la demande, engagements, capacité provisionnée, lots/préemptible, licences par siège et paliers), puis de suivre le `TCO` **complet à cinq postes** et le **coût par résultat métier réussi** (en plage statistique) [363]. Le **Blueprint 1** présente un `OPEX` prévisible (`PTU` + débordement `PAYG`, supervision `HITL`, `Temporal`, `WORM`) réduit par la partition `80/20`. Le **Blueprint 2** expose le budget à l’amplification inter-agents et aux licences `SaaS` B2B, imposant l’attribution `OpenTelemetry GenAI` + `FOCUS`, le plafond `ce_ttl` et l’arrêt `CancelTask` [348] [363] [345]. Le **Blueprint 3** bascule vers un `CAPEX` GPU et mémoire (`WarmPool`) qui n’est rentable qu’à fort taux d’utilisation partagé via l’`AI Gateway` et `llm-d` [359] [354] [363].

Sur le plan organisationnel, la maîtrise de la **charge cognitive** s’appuie sur `Team Topologies` [364] (figure `14.4`) : une `Platform Team` fournit l’`IAP` en mode `X-as-a-Service` (`AI Gateway`, `agentgateway`, `SPIRE`, `OTel`, `Temporal`, `Event Mesh`, `agent-sandbox` /`llm-d`) après une phase ponctuelle de `Collaboration` lors de l’accueil d’une nouvelle capacité ; une `Enabling Team` intervient en `Facilitation` (`EvalOps`, `FinOps`, `ÉFVP`, revues `2LoD`) ; des `Stream-aligned Teams` (typiquement 5 à 8 ETP incluant l’`Agent Owner`) livrent les cas métier ; et une `Complicated Subsystem Team` reste confinée au **Blueprint 3** pour les noyaux GPU/`CoCo` /`microVM` [360] [355] [364].

> **[Figure]**
> - Équipe Plateforme (IAP — Mode X-as-a-Service)
> - Équipe Habilitante (Enabling — Mode Facilitation)
> - Équipes Alignées sur le Flux (Stream-aligned)
> - Socle IAP & Golden Paths (AI GW, MCP GW, SPIRE, OTel) Moteurs & Enclaves (Temporal, Event Mesh, CoCo/GPU)
> - Cellule EvalOps, FinOps & Conformité 2LoD (E-23 / Loi 25)
> - Domaine Crédit / Sinistres (Blueprint 1 — R3/R4, Temporal)
> - Domaine Achats & B2B (Blueprint 2 — A2A, AGNTCY, Mesh)
> - Domaine R&D / Santé Souverain (Blueprint 3 — vLLM TEE, RAG ACL)
> - soutient
> - X-as-a-Service
> - X-as-a-Service
> - X-as-a-Service
> - facilite EvalOps/Audit
> - cadre OASF/SLA
> - valide ÉFVP/TEE

*Fig. 56. – Modèle opérationnel ArchiMate et topologie d’équipes Team Topologies reliant l’IAP aux trois blueprints sectoriels*

| Critère | Blueprint 1 — Transactionnel | Blueprint 2 — Maillage B2B | Blueprint 3 — Souverain `Silo` |
| --- | --- | --- | --- |
| **Cas et palier** | Crédit, sinistres (`L2` –`L3`, `R3` –`R4`) | *Source-to-Pay*, logistique (`L2` –`L3`, `R2` –`R3`) | R&D pharma, santé, défense (`L1` –`L3`, `R3` –`R4`) |
| **Socle clé** | `Temporal HA` + `MCP GW` + `OBO` + `WORM` [339] [341] [343] [344] | `Process Mgr` + `A2A` + `AGNTCY` + `Event Mesh` [348] [349] [351] | `AI GW` + `EPP` /`llm-d` + `CoCo` + `OpenFGA` /`Qdrant` /`RLS` + `microVM` [359] [355] [353] [358] [356] |
| **Latence** `p95` **cible** | `Temporal` `200 ms p99` [347] ; boucle `3–8 s` avant `HITL` | `Event Mesh` `10–100 ms` ; `A2A` B2B `20 s` à min/h [348] | `RAG` `1,5–4 s` (`TTFT` `2×` `llm-d` [354]) ; `microVM` `4–12 s` [360] |
| **Verrou débit** | Actions/s `Temporal` (`TRU`), amorties `CQRS` [347] | Tampons `Solace` /`Kafka` + *backpressure* `TPM` [351] [352] | Bande `HBM` GPU et `WarmPools` (`3×` `llm-d`) [359] [354] |
| `RPO` **/** `RTO` | `3-AZ` `RPO=0` ; Multi-région `RPO<1m`, `RTO<20m` [339] [346] | `Solace` sync/async ; `Cluster Linking` *offsets* exacts [350] [352] | Données `Warm Standby` (`RPO` qq s–5 min) ; GPU `Pilot Light` (`RTO` 15–60 min) [361] [362] |
| **Profil** `FinOps` | `OPEX` (`PTU` + `PAYG`, `HITL`, `WORM`) borné `80/20` [344] [363] | `OPEX` variable B2B ; contrôle `FOCUS` + `CancelTask` [348] [363] | `CAPEX` GPU, RAM `WarmPool`, licences `NVAIE` via `IAP` [355] [363] |
| **Équipes** | `Platform` + `Stream-aligned` + `Enabling` [364] | `Platform` + `Stream-aligned` multi-domaines + `Enabling` [364] | `Platform` + `Complicated Subsystem` (GPU/`CoCo`) + `Stream-aligned` [364] |

*Tableau 14.4 — Matrice comparative non fonctionnelle des trois blueprints : performance, résilience, économie et organisation.*

> **Arbitrage EA / SA** — Aucune grande entreprise ne doit enfermer son portefeuille dans un unique patron : l’`EA` oriente chaque chaîne de valeur vers le Blueprint 1 (autorité `SoR` `R3` –`R4`), le Blueprint 2 (échanges opaques inter-domaines et B2B) ou le Blueprint 3 (souveraineté *Zero Egress*), en arrimant le modèle économique (`PTU` contre `CAPEX` GPU) au coût par résultat réussi [363] [364]. Le `SA` maintient un socle `IAP` unique (`SPIRE`, `OpenTelemetry GenAI`, `MCP` /`A2A`, `OPA`) en `X-as-a-Service` pour composer au besoin ces briques — déclencher un workflow `Temporal` depuis un jalon `A2A` ou router une sous-tâche sensible vers l’enclave locale — sans dupliquer la gouvernance [342] [364] [345].

## Synthèse architecturale et transition vers le chapitre 15

Ce chapitre a assemblé les standards et patrons des chapitres 01 à 13 en trois blueprints instanciables : le **Blueprint 1** sécurise les processus transactionnels réglementés via `Temporal` (`Worker Versioning` `Pinned`, `3-AZ` et multi-régions), `MCP Gateway` sous `OAuth 2.0 OBO` (`RFC 8693` /`8707`), `ACL` /`CQRS` et archivage `WORM` (`S3 Object Lock Compliance`) [339] [340] [341] [343] [344] ; le **Blueprint 2** fédère les domaines et partenaires B2B via un *Process Manager* parlant `A2A v1.0` et `AGNTCY` (`OASF`, `ADS`, `SLIM` /`MLS`) couplé à un `Event Mesh` (`Solace` ou `Kafka Cluster Linking`) [348] [349] [350] [352] ; le **Blueprint 3** assure la souveraineté stricte par `AI Gateway` et `EPP` sur `llm-d` /`vLLM` ou `NIM` sous `Confidential Containers` (`CoCo`), filtrage `RAG` triple (`OpenFGA`, `Qdrant`, `PostgreSQL RLS`) et `microVM` `Firecracker` /`Kata` sous `agent-sandbox` [359] [360] [355] [353] [354] [357] [358] [356]. Le **chapitre 15** conclut l’ouvrage sur la coexistence avec le patrimoine `BPM` /`iPaaS` /`RPA`, les anti-patrons critiques et la feuille de route d’adoption.
