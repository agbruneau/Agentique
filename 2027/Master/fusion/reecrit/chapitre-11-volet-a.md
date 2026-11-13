## Mise en œuvre — Gouvernance des standards et anatomie de la pile interopérable {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : entre 2024 et 2025, la prolifération de cadriciels d’agents captifs et de connecteurs sur mesure a imposé aux entreprises un coût d’intégration quadratique ($N \times M$) et recréé un verrouillage fournisseur. En 2027, une pile protocolaire gouvernée par des fondations neutres conditionne toute mise à l’échelle rentable et auditable entre divisions.
- **Décisions architecturales structurantes** :
  1.  *Irréversible à moyen terme* : standardiser les contrats « sur le fil » autour du socle de l’AAIF (MCP en vertical, A2A v1.0 en horizontal, agentgateway en coupure réseau) et d’ontologies métiers canoniques (Apache Ossie).
  2.  *Structurante dès le cadrage* : appliquer sans dérogation la loi de non-substituabilité entre un outil déterministe (MCP) et un pair autonome (A2A), pour préserver les délais réseau, la chaîne d’identité et le périmètre réglementaire (BSIF E-23, EU AI Act).
  3.  *Réversible par conception* : le choix du moteur de modèle (abstrait derrière Open Responses et Agent Router), du bac à sable (OpenSandbox) ou du studio interne d’un éditeur SaaS.
- **Indicateurs de gouvernance associés** : taux de conformité protocolaire en production (cible $\ge 95\,\%$), délai médian de raccordement d’un domaine métier, temps de bascule entre modèles ($< 4\text{ h}$) et nombre de connecteurs hors norme maintenus en dette technique.
::::

## 11.11 Cartographie institutionnelle 2026–2027

Un code source ouvert ne suffit pas : il faut une gouvernance ouverte. Bâtir sur une bibliothèque sous licence MIT contrôlée à 95 % par un éditeur unique expose à des ruptures d’API trimestrielles, à des optimisations qui favorisent le nuage de son créateur et à une inflation combinatoire des ponts d’intégration. Pour $N$ environnements hôtes et $M$ systèmes cibles, soumis à un facteur annuel de dérive $\delta$, le passage aux protocoles canoniques change l’équation économique :

$$C_{\text{propriétaire}} = (1 + \delta) \cdot (N \times M) \quad \longrightarrow \quad C_{\text{ouvert}} = N + M$$

Dans un groupe qui exploite $N = 12$ environnements d’agents et $M = 45$ systèmes métiers, avec un taux annuel de rupture d’API propriétaires $\delta = 0,35$, passer de $540$ intégrations point-à-point (soit $1,35 \times 540 \approx 729$ maintenances correctives annuelles) à $57$ adaptateurs normalisés réduit d’un ordre de grandeur la surface d’attaque et la dette d’entretien.

![Cartographie institutionnelle 2026–2027 et alignement sur le modèle de référence en 6 couches.](figures/fig-11-a-1.svg)

### Projets de l’AAIF et autorités complémentaires

Le tableau dresse l’inventaire technique des dix projets hébergés par l’AAIF au 11 novembre 2026 (section 11.2) et les rattache aux couches du modèle de référence défini plus bas. La colonne de statut s’en tient à ce que l’exposé établit : A2A a été admis au niveau Growth, et le niveau des neuf autres projets n’a pas pu être établi (section 11.2). Le fil rouge (section 11.14) et l’ADR-004 (section 11.15) placent la plupart de ces projets au socle obligatoire, ce qui va au-delà de ce que retient l’exposé : un seuil de production à Growth ou Impact et la vérification du niveau de chaque projet (sections 11.2 et 11.10).

| Projet AAIF | Origine initiale | Couche | Rôle normatif en architecture d’entreprise | Statut 2026–2027 |
|:-----------------|:-------------|:--------------|:------------------------------------|:------------------|
| **1. MCP** (*Model Context Protocol*) | Anthropic | C3 (Vertical) | Protocole JSON-RPC 2.0 sur Streamable HTTP qui normalise outils, ressources, prompts, échantillonnage et élicitation. | Texte mis en œuvre; niveau non établi |
| **2. A2A** (*Agent2Agent v1.0*) | Google + IBM (ACP) | C5 (Horizontal) | Délégation asynchrone d’objectifs entre agents pairs opaques, par Agent Cards, tâches durables et artefacts typés. | Niveau Growth |
| **3. `AGENTS.md`** | OpenAI / Communauté | C4 (Contexte) | Convention Markdown qui fixe à la racine d’un dépôt les invariants d’architecture, les tests et les frontières de sécurité. | Niveau non établi |
| **4. goose** | Block | C1 (Hôte) | Hôte et cadriciel agentique modulaire de référence, conçu nativement autour de MCP. | Niveau non établi |
| **5. Agent Router** | Communauté AAIF | C2 (Routage) | Routage dynamique des requêtes entre SLM économiques, LLM de raisonnement et agents spécialisés, selon le coût et la latence. | Niveau non établi |
| **6. agentgateway** | Solo.io | C2 (Plan données) | Proxy natif pour l’IA (Rust) qui assure l’authentification OAuth 2.1 OBO, les politiques Cedar/OPA et les traces MCP/A2A/LLM. | Niveau non établi |
| **7. Agent Skills** | Anthropic | C4 (Savoirs) | Empaquetage procédural portable (`SKILL.md`, `scripts/`, `references/`), chargé par divulgation progressive. | Niveau non établi |
| **8. Open Responses** | OpenAI / Communauté | C4 (Inférence) | Spécification multifournisseurs qui unifie appels de modèles, blocs de raisonnement, flux d’événements et outils distants. | Niveau non établi |
| **9. OpenEnv** | Hugging Face | C1 (Évaluation) | Environnement conteneurisé standardisé pour l’évaluation reproductible, la simulation et le RL d’agents. | Niveau non établi |
| **10. OpenSandbox** | Alibaba | C1 (Isolation) | Environnement d’exécution confiné (microVM, gVisor, WASM) pour le code généré ou les scripts d’outils. | Niveau non établi; obligatoire pour code dynamique |

Cinq autorités complémentaires couvrent le reste du modèle (l’IETF et le W3C sont présentés aux sections 11.4 et 11.3) :

- Linux Foundation AGNTCY fournit la taxonomie formelle de compétences OASF (*Open Agentic Schema Framework*), l’annuaire fédéré Agent Directory (registres OCI et DHT) et le transport temps réel SLIM (*Secure Low-Latency Interactive Messaging*). Retenir OASF et Agent Directory au socle obligatoire (section 11.14, ADR-004) va au-delà de ce que retient l’exposé : adopter un registre interne et suivre le reste, le registre officiel étant en préversion et un projet de l’IEEE naissant (section 11.10).
- Apache Software Foundation (Apache Ossie) gouverne les ontologies métiers et les schémas JSON canoniques, pour que deux agents qui échangent le champ `net_exposure` partagent la même définition comptable.
- L’IETF étend les standards existants à l’identité et à l’autorisation des agents, sans qu’aucun RFC propre aux agents n’existe (section 11.4) : OAuth 2.1, échange RFC 8693 (*On-Behalf-Of*), preuve RFC 9449 (*DPoP*) et chiffrement de groupe RFC 9420 (MLS sous SLIM). L’identité multi-environnements WIMSE n’en est qu’à un document informatif et le groupe n’a publié aucun RFC : l’exposé recommande de la suivre de près (sections 11.4 et 11.10).
- Le W3C encadre DID / Verifiable Credentials 2.0. WebMCP (*Web Machine Learning Community Group*), qui expose les fonctions JavaScript d’une application web active aux agents du navigateur, relève d’un groupe communautaire : un tel groupe est hébergé sans aval du W3C et ses rapports ne sont pas des Recommandations (section 11.3).
- L’alliance FIDO ancre AP2 (*Agent Payments Protocol*) dans des mandats vérifiables signés par clé biométrique (*passkey*), complété par x402 (HTTP 402) pour les micro-règlements programmatiques.

Chaque couche délègue la sécurité ou le transport au standard spécialisé éprouvé, plutôt que de réinventer une pile monolithique.

:::: {.encadre .important}
::: {.encadre-titre}
**Important**
:::

**Niveaux de maturité** : distinguer, dans une architecture, les briques que l’exposé donne pour mises en œuvre et hébergées par une fondation (MCP Streamable HTTP, A2A v1.0) ou adossées à des RFC de la famille OAuth (OAuth 2.1 OBO), celles dont le niveau n’a pas pu être établi (`AGENTS.md`, Agent Skills, agentgateway) et les standards déployés par paliers encadrés en 2027 (fédérations AGNTCY inter-entreprises et règlements AP2/x402 soumis aux homologations bancaires). WebMCP relève d’un groupe communautaire du W3C : l’exposé ne voit rien de prêt pour la production de ce côté (section 11.10). Le seuil de maturité par instance figure à la section 11.10.
::::

------------------------------------------------------------------------

## 11.12 Modèle de référence en 6 couches et loi de non-substituabilité de l’outil et du pair

Ce modèle de référence en six couches (C1 à C6) décompose, selon une lecture ascendante d’inspiration OSI, les strates d’infrastructure et de transport sous-jacentes à la vue fonctionnelle de l’Ouverture. Il garantit l’indépendance de substitution : remplacer un moteur de couche 1 ou un routeur de couche 2 laisse intacts les contrats fonctionnels des couches 3 à 6. Contrairement à OSI, la pile agentique doit transporter aussi le sens métier, l’intention déléguée, l’identité atténuée et le budget économique, à travers des composants non déterministes :

1.  **Couche 1 — Isolation, évaluation et hôtes (OpenSandbox, OpenEnv, goose, moteurs durables)** : fournit le socle physique et temporel, soit l’exécution durable à journalisation déterministe (Temporal, Restate), le confinement microVM/WASM pour tout code non fiable, les bancs d’homologation reproductibles et la télémétrie OpenTelemetry.
2.  **Couche 2 — Plan de données IA, routage et identité (agentgateway, Agent Router, SLIM/MLS, OAuth 2.1 OBO)** : assure l’acheminement chiffré post-quantique, la vérification des identités non humaines (NHI via SPIFFE/WIMSE), l’atténuation des portées à chaque saut, l’arbitrage coût/latence entre modèles et l’évaluation des politiques Cedar ou OPA.
3.  **Couche 3 — Connectivité verticale (MCP sur Streamable HTTP)** : normalise l’invocation déterministe et typée des fonctions métiers, la lecture de ressources adressables par URI et les demandes contrôlées d’échantillonnage ou d’élicitation.
4.  **Couche 4 — Sémantique et portabilité cognitive (Apache Ossie, Agent Skills, `AGENTS.md`, Open Responses)** : découple le sens des entités d’affaires, le savoir-faire procédural de l’organisation et le contrat d’appel d’inférence des poids propriétaires d’un modèle particulier.
5.  **Couche 5 — Coordination horizontale (A2A v1.0, AGNTCY OASF et Agent Directory, ANP)** : assure la découverte dynamique des capacités publiées, la négociation de modalités et le cycle de vie asynchrone de tâches déléguées entre pairs autonomes opaques, y compris au-delà des frontières de l’entreprise.
6.  **Couche 6 — Interaction humaine et commerce (AG-UI, A2UI, WebRTC, WebMCP, AP2, x402)** : couvre la synchronisation d’état bidirectionnelle avec les opérateurs humains, le rendu d’interfaces génératives déclaratives sans injection de code, les flux vocaux temps réel et la signature cryptographique de mandats financiers.

### La loi de non-substituabilité : un outil MCP n’est pas un pair A2A

MCP et A2A v1.0 reposent tous deux sur JSON-RPC 2.0 sur HTTP, et certaines équipes tentent de les réduire à un seul protocole. Deux antipatrons en résultent :

- **Antipatron 1 — le « pair déguisé en outil » sur MCP** : dissimuler un agent autonome multi-tours derrière un appel `tools/call` MCP provoque des expirations HTTP 504 en cascade, masque la consommation récursive de jetons et empêche la gestion des états asynchrones (`WORKING`, `INPUT_REQUIRED`) quand une approbation humaine différée est requise.
- **Antipatron 2 — le « microservice déguisé en agent » sur A2A** : envelopper un calcul fiscal ou une requête SQL déterministe dans un serveur A2A doté d’un LLM ajoute 1 à 3 secondes de latence, introduit un risque d’hallucination inutile et soumet un composant ordinaire aux obligations réglementaires du risque de modèle (BSIF E-23).

| Critère d’architecture | Connectivité verticale — MCP (Couche 3) | Coordination horizontale — A2A v1.0 (Couche 5) |
|:----------------------|:-------------------------------------|:----------------------------------------|
| **Nature de la cible** | Capacité déterministe typée (*boîte de verre* : API, base, calcul) | Pair autonome opaque (*boîte noire* dotée de raisonnement et de mémoire propres) |
| **Contrat publié** | Schémas stricts (`inputSchema` / `outputSchema`) par primitive | Agent Card (`/.well-known/agent-card.json`) orientée compétences (`skills`) |
| **Régime temporel** | Millisecondes à quelques secondes (appel atomique borné) | Secondes à plusieurs jours, par machine à états (`SUBMITTED`, `WORKING`, `COMPLETED`) |
| **Couplage cognitif** | L’appelant prescrit *quelle* fonction exécuter, avec ses arguments exacts | L’appelant formule *quel* objectif atteindre; le pair planifie le *comment* |
| **Frontière d’identité** | Accès délégué à une ressource technique du domaine | Traversée de frontière organisationnelle, avec échange OAuth 2.1 OBO (RFC 8693) |
| **Profil FinOps et risque** | Coût marginal fixe; hors inventaire des modèles autonomes | Coût d’inférence variable plafonné (`ActionEnvelope`); gouvernance BSIF E-23 |

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Éditeurs SaaS B2B — Stratégie d’ouverture protocolaire face aux écosystèmes hyperscalers**
:::

Pour un éditeur SaaS B2B, refuser les standards ouverts par crainte d’être réduit à une base passive conduit, en 2027, à l’éviction lors des renouvellements de grands comptes. Les éditeurs performants structurent leur ouverture sur deux niveaux :

1.  **Ouvrir l’accès transactionnel par un serveur MCP distant** : exposer ses opérations unitaires validées sur Streamable HTTP et OAuth 2.1 remplace les accès fragiles par l’interface et préserve l’intégrité des règles métiers.
2.  **Monétiser le savoir-faire différenciant par A2A v1.0** : conserver ses modèles sectoriels et ses heuristiques propriétaires derrière une façade d’agent spécialiste A2A, facturée au résultat. Les orchestrateurs clients lui délèguent des missions à forte valeur sans pouvoir extraire sa propriété intellectuelle interne.
::::

------------------------------------------------------------------------

## 11.13 Cycle de vie des spécifications ouvertes et stratégies anti-verrouillage

MCP négocie ses révisions calendaires par l’en-tête MCP-Protocol-Version, tandis qu’A2A suit un versionnement sémantique (v1.0). Contre les extensions propriétaires qui rendent un composant captif, l’architecture combine une validation déclarative en passerelle et l’abstraction du plan d’inférence, conformément à l’isolement des dépendances instables derrière un adaptateur (section 11.10).

#### Extrait 11.1 — Matrice déclarative de conformité protocolaire (boreal-protocol-policy.yaml)

La politique fixe les versions de MCP et d’A2A admises, les transports, les contraintes de conception des outils, les règles d’identité et l’espace de noms des extensions d’éditeur; en production, tout composant non conforme est bloqué.

``` yaml
apiVersion: architecture.boreal.ca/v2027
kind: ProtocolGovernancePolicy
metadata:
  name: boreal-aaif-baseline-2027
  owner: coe-architecture-agentique@boreal.ca
spec:
  enforcementMode: block_non_compliant_in_prod
  verticalConnectivity:
    protocol: mcp
    allowedProtocolVersions: ["2025-06-18", "2026-07-28"]
    deprecatedGracePeriodDays: 90
    transports:
      remoteProductionAllowed: ["streamable-http"]
      forbidden: ["legacy-http-sse", "stdio"] # stdio réservé à OpenSandbox local
    toolDesignConstraints:
      maxToolsPerServer: 15
      requireOutputSchema: true
      requireIdempotencyKeyOnMutatingTools: true
  horizontalCoordination:
    protocol: a2a
    minVersion: "1.0.0"
    requireSignedAgentCard: true
    canonicalPayloadRegistry: "https://schemas.boreal.ca/ossie/v2/"
  securityAndIdentity:
    forbidStaticApiKeys: true
    requiredDelegationFlow: "urn:ietf:params:oauth:grant-type:token-exchange"
    requireDpopSenderConstraint: true
  vendorExtensionsPolicy:
    permittedNamespace: "_meta.vendor"
    requireGracefulDegradationWhenStripped: true
```

En homologation dans OpenEnv, le pipeline CI/CD purge systématiquement `_meta.vendor` : tout composant qui échoue sans ses métadonnées propriétaires se voit refuser le déploiement. La même gouvernance protège la chaîne d’approvisionnement logicielle contre les mutations furtives des schémas distants : chaque manifeste d’outils MCP et chaque Agent Card A2A approuvés voient leur empreinte SHA-256 scellée dans le registre interne de la passerelle. Si un éditeur SaaS modifie silencieusement la description d’un outil ou élargit ses paramètres lors d’une mise à jour nocturne, agentgateway détecte la divergence d’empreinte et met la route en quarantaine avant qu’un agent interne n’interprète ce schéma non audité.

Coder directement contre le SDK exclusif d’un laboratoire d’IA, ou lui confier l’hébergement de l’état de session, interdit tout basculement d’urgence en cas de panne infonuagique ou de révision tarifaire. Les appels passent par Open Responses derrière Agent Router, avec `storeStateRemotely: false` : l’historique décisionnel reste sous le contrôle du moteur durable interne. Les modèles à raisonnement ajoutent une contrainte : leurs traces latentes chiffrées (*Encrypted Reasoning Items*) sont liées cryptographiquement au fournisseur émetteur et ne peuvent pas être rejouées vers un modèle concurrent en cours de conversation. Le moteur durable ne conserve donc d’un tour à l’autre que les faits structurés et les résultats d’outils canoniques.

#### Extrait 11.2 — Port d’abstraction anti-verrouillage TypeScript sur Open Responses

Le client ci-dessous interdit au niveau du type le stockage d’état chez le fournisseur et transmet à Agent Router une preuve DPoP, le profil de routage, la zone de résidence des données et le plafond de coût.

``` typescript
export interface InferenceRoutingPolicy {
  readonly capabilityProfile: "fast-triage-slm" | "domain-specialist" | "deep-reasoning";
  readonly dataResidencyZone: "CA-QC-LAW25" | "EU-GDPR" | "US-EAST";
  readonly maxCostCadPerCall: number;
}

export interface OpenResponseRequest {
  readonly specVersion: "open-responses/1.0";
  readonly instructions: string;
  readonly input: ReadonlyArray<{
    readonly type: "message" | "item_reference";
    readonly role?: "user" | "system" | "developer";
    readonly content?: string;
  }>;
  readonly mcpServers?: ReadonlyArray<{
    readonly serverLabel: string;
    readonly serverUrl: string;
    readonly allowedTools: ReadonlyArray<string>;
  }>;
  readonly textFormatSchema?: Record<string, unknown>;
  readonly storeStateRemotely: false; // Rétention d'état externe strictement interdite
}

export interface OpenResponseResult<T> {
  readonly responseId: string;
  readonly servedByModelId: string;
  readonly parsedOutput: T;
  readonly billedCostCad: number;
}

export class BorealVendorNeutralModelClient {
  constructor(
    private readonly routerUrl: string,
    private readonly obtainDpopArtifacts: (
      htm: string,
      htu: string
    ) => Promise<{ accessToken: string; dpopProof: string }>
  ) {}

  async invokeStructured<T>(
    request: OpenResponseRequest,
    routing: InferenceRoutingPolicy,
    signal?: AbortSignal
  ): Promise<OpenResponseResult<T>> {
    const endpoint = `${this.routerUrl}/v1/responses`;
    const { accessToken, dpopProof } = await this.obtainDpopArtifacts("POST", endpoint);
    const res = await fetch(endpoint, {
      method: "POST",
      signal,
      headers: {
        "Content-Type": "application/json",
        "Authorization": `DPoP ${accessToken}`,
        "DPoP": dpopProof,
        "X-Agent-Router-Profile": routing.capabilityProfile,
        "X-Agent-Residency-Zone": routing.dataResidencyZone,
        "X-Agent-Max-Cost-CAD": routing.maxCostCadPerCall.toFixed(4)
      },
      body: JSON.stringify(request)
    });
    if (!res.ok) throw new Error(`Échec Agent Router (${res.status})`);
    return (await res.json()) as OpenResponseResult<T>;
  }
}
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur public et infrastructures critiques — Clauses de réversibilité dans les marchés publics (Loi 25, EU AI Act)**
:::

Pour les organismes publics québécois, canadiens et européens soumis à la Loi 25, au RGPD et à l’article 25 de l’EU AI Act (échéance haut risque de décembre 2027), la réversibilité protocolaire est une exigence de souveraineté opérationnelle. Les cahiers d’appel d’offres 2027 imposent quatre clauses techniques :

1.  **Ouverture native sans surtaxe** : exposition obligatoire des capacités par MCP (AAIF) et A2A v1.0, sans frais discriminatoires par appel externe.
2.  **Propriété et exportabilité cognitive** : restitution intégrale des procédures métiers au format ouvert Agent Skills (`SKILL.md`) et en schémas JSON standardisés.
3.  **Absence d’état captif** : interdiction de subordonner l’exécution à un historique décisionnel enfermé dans un nuage propriétaire non réplicable.
4.  **Preuve contractuelle de substitution** : démonstration annuelle, sur banc OpenEnv, d’un changement de modèle sous-jacent en moins de 48 heures, sans régression critique.
::::

------------------------------------------------------------------------

## 11.14 Application au fil rouge : charte d’interopérabilité du Groupe Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Rationalisation des 47 initiatives vers le socle normatif AAIF**
:::

**État initial (T4 2026)** : l’audit des 47 initiatives dispersées entre BEL, BCA et BSN relève 11 cadriciels d’agents incompatibles, des connecteurs SAP et Snowflake réécrits trois fois et deux pilotes captifs de l’API d’état hébergée d’un fournisseur américain, ce qui bloque le repli de BCA vers une région canadienne conforme à la Loi 25.

**Urbanisation en trois anneaux (8 semaines)** : plutôt que d’imposer un langage unique aux équipes TypeScript (BSN), Python (BCA) et Java/ABAP (BEL), l’architecture impose l’uniformité des protocoles sur le fil :

- **Anneau 1 (socle obligatoire)** : MCP (Streamable HTTP) en vertical; A2A v1.0 et AGNTCY OASF en horizontal; Apache Ossie (`schemas.boreal.ca/ossie/v2`) pour les 18 objets métiers canoniques; Open Responses par Agent Router et agentgateway; OpenSandbox pour tout script.
- **Anneau 2 (toléré sous passerelle $\le 6$ mois)** : les agents natifs Salesforce Agentforce et Copilot Studio restent dans leur périmètre local, à condition de ne communiquer que par des façades A2A v1.0 et MCP filtrées par agentgateway.
- **Anneau 3 (interdit immédiatement)** : clés d’API statiques, MCP stdio distant, génération OpenAPI brute (\> 15 outils) et `storeStateRemotely: true`.

**Résultats mesurés à T2 2027** :

- **Rationalisation** : extinction de 8 des 11 cadriciels redondants au profit d’un catalogue partagé de serveurs MCP et d’Agent Cards.
- **Raccordement** : un nouvel agent raccordé à deux *Systems of Record* passe de 9 semaines à 6 jours ouvrables.
- **Réversibilité prouvée (BSIF E-23)** : bascule réelle de l’agent garantie BCA vers un modèle souverain hébergé à Montréal en 2 h 15, avec un écart de précision de 0,7 % sous OpenEnv et aucune modification du code métier.
::::

------------------------------------------------------------------------

## 11.15 Décision d’architecture normative et points de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-004 — Alignement normatif sur la pile Linux Foundation AAIF et gouvernance anti-verrouillage**
:::

- **Statut** : acceptée \| Périmètre : entreprise (développements internes et acquisitions SaaS) \| Révision : semestrielle
- **Contexte** : la dispersion des SDK propriétaires et des états d’inférence hébergés multiplie les coûts d’intégration ($N \times M$) et crée un verrouillage incompatible avec les exigences de BSIF E-23, de la Loi 25 et de l’EU AI Act.
- **Options évaluées** :
  1.  *Autonomie totale par produit* : rejetée — silos entre divisions, duplication des connecteurs et failles d’identité.
  2.  *Cadriciel logiciel unique imposé* : rejetée — incompatible avec les agents natifs des progiciels SaaS (SAP, Salesforce, ServiceNow) et avec la diversité des piles internes.
  3.  *Standardisation des protocoles sur le fil (socle AAIF + AGNTCY + IETF + Ossie)* : liberté de mise en œuvre interne, sous réserve du respect des contrats protocolaires ouverts, vérifiés en passerelle. Retenue.
- **Décision** : adopter le modèle en 6 couches fondé sur MCP (Streamable HTTP), A2A v1.0, AGNTCY OASF, Apache Ossie, Open Responses (`storeStateRemotely: false`), agentgateway (OAuth 2.1 OBO + DPoP) et OpenSandbox/OpenEnv. Confiner toute extension d’éditeur sous `_meta.vendor`, avec une dégradation gracieuse vérifiée en CI/CD.
- **Conséquences** :
  - *Positives* : complexité réduite à $N + M$, substitution de modèle en moins de 4 heures, clauses d’achat opposables aux éditeurs.
  - *Négatives, coûts assumés* : gouvernance continue du registre ontologique Apache Ossie et exploitation des pipelines de conformité OpenEnv.
- **Condition de révision** : semestrielle, selon les publications techniques de l’AAIF, de l’IETF (WIMSE) et du W3C (WebMCP).
::::

### Liste de contrôle de mise en production

Avant toute mise en production sur ce socle protocolaire, il faut vérifier huit critères :

1.  **Loi de non-substituabilité** : aucun agent multi-tours lent n’est-il dissimulé derrière un outil MCP, et aucun service déterministe simple n’est-il exposé inutilement en pair A2A ?
2.  **Validation de version en coupure** : la passerelle contrôle-t-elle MCP-Protocol-Version et les Agent Cards A2A v1.0 signées, et rejette-t-elle les transports obsolètes ?
3.  **Zéro état captif** : tous les appels cognitifs transitent-ils par Open Responses, avec refus du stockage d’état distant chez le fournisseur de LLM ?
4.  **Purge des extensions propriétaires** : les bancs OpenEnv valident-ils le fonctionnement nominal des flux après suppression automatique de `_meta.vendor` ?
5.  **Schémas métiers canoniques** : les charges entre divisions pointent-elles vers le registre versionné Apache Ossie ?
6.  **Confinement systématique** : toute exécution de script dynamique passe-t-elle par OpenSandbox, sans accès réseau libre ?
7.  **Clauses contractuelles SaaS** : les contrats d’édition exigent-ils MCP (Streamable HTTP + OAuth 2.1) et A2A v1.0 sans surcoût d’accès ?
8.  **Exercice de réversibilité** : un test chronométré de changement de modèle a-t-il été réussi ce trimestre sur un flux critique ?
