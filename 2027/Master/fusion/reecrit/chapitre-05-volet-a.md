## Mise en œuvre — Connectivité verticale : outils, ressources, compétences et web {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Raccorder les agents aux systèmes d’enregistrement par conversion mécanique des API REST existantes abaisse la précision sous les 45 %, augmente la facture de jetons et expose à des écritures partielles non compensées.
- **Décisions architecturales structurantes** :
  1.  *Irréversible à moyen terme* : Imposer MCP sur Streamable HTTP derrière agentgateway comme unique standard vertical côté serveur, sans transport hérité ni clé statique, avec OAuth 2.1 OBO.
  2.  *Structurante dès la conception* : Proscrire le mappage `OpenAPI -> MCP` 1:1 au profit de façades orientées intention métier (5 à 12 outils par spécialiste), dotées d’un `outputSchema`, de clés d’idempotence et d’erreurs cognitives qui guident la correction.
  3.  *Réversible et modulaire* : Empaqueter le savoir-faire procédural dans Agent Skills (`SKILL.md` à divulgation progressive) et instrumenter les portails web internes avec WebMCP, pour éviter 80 à 90 % du recours aux agents de capture d’écran (CUA).
- **Indicateurs de gouvernance associés** : Empreinte de schémas d’outils par session ($< 2\,000$ jetons), précision d’appel au premier essai ($\text{pass}^5 \ge 95\,\%$), latence verticale MCP P95 et couverture d’idempotence des outils mutatifs.
::::

## 5.9 Architecture de production : hôte, client, passerelle et serveur

Les rôles d’hôte, de client et de serveur sont décrits à la section 5.1. En production, l’hôte est un travailleur Temporal, un hôte Goose, un environnement de développement ou un poste opérateur. Une passerelle s’intercale entre le client et le serveur, et le serveur prend la forme d’une façade de domaine, comme le montre la figure ci-dessous.

- **La passerelle (agentgateway)** : Coupure réseau obligatoire, elle inspecte les trames JSON-RPC 2.0, valide OAuth 2.1 et DPoP, exécute l’échange *On-Behalf-Of* (RFC 8693), filtre les outils selon les politiques Cedar et émet les traces OpenTelemetry (`gen_ai.*`). Exiger DPoP et l’échange *On-Behalf-Of* à la passerelle va au-delà de ce que retient la section 5.5 : l’option par défaut y est l’Enterprise-Managed Authorization (ID-JAG) si le fournisseur d’identité et les clients la prennent en charge, sinon le flux OAuth de base, et DPoP comme l’échange de jetons (RFC 8693) figurent au programme d’un groupe de travail en formation. Le serveur aval suit le profil d’autorisation de la section 5.5 : il publie ses métadonnées sur `/.well-known/oauth-protected-resource` (RFC 9728) et refuse tout passage de jeton, c’est-à-dire la réutilisation du jeton reçu pour appeler une autre API. Un jeton dont l’audience (`aud`) ne le désigne pas est rejeté, ce qui empêche qu’un jeton émis pour un service serve à en atteindre un autre.
- **Le serveur de domaine** : Une façade sans planification autonome, qui traduit des intentions d’affaires bornées en transactions sur le système d’enregistrement sous-jacent.

![Architecture d’entreprise du Model Context Protocol (MCP) sur Streamable HTTP, articulée avec Agent Skills, Open Responses et WebMCP.](figures/fig-05-a-1.svg)

### Règles de transport

Les transports sont décrits à la section 5.3. Trois règles s’appliquent en entreprise.

- **`stdio` confiné** : Admis sur le poste développeur ou à l’intérieur d’une microVM OpenSandbox, il est interdit sur le réseau d’entreprise, faute de coupure d’authentification centralisée et de gestion des secrets.
- **HTTP+SSE de 2024 écarté** : Son flux `GET /sse` couplé à `POST /messages` empêchait l’équilibrage sans affinité de session, saturait les pare-feu et interdisait la mise à l’échelle à zéro.
- **Streamable HTTP par défaut** : Tout passe par le point d’accès unique (`POST /mcp`). Une exécution longue, qui exige des notifications de progression (`notifications/progress`), répond en `text/event-stream` (SSE) limité à cette requête (section 5.3). Un serveur à qui il manque une information renvoie un résultat `input_required` (section 5.2). La reprise par Last-Event-ID est supprimée : une requête interrompue est réémise avec un nouvel identifiant (section 5.2).

:::: {.encadre .tip}
::: {.encadre-titre}
**Astuce**
:::

**Streamable HTTP sans état sur Kubernetes** : Les serveurs MCP s’exploitent sans état de session gardé dans la mémoire d’un pod précis : depuis la révision `2026-07-28`, la session et l’en-tête Mcp-Session-Id sont supprimés, et l’état passe par des identifiants explicites (section 5.2). Ils valident MCP-Protocol-Version à chaque appel. Avec l’idempotence déportée dans Redis/Valkey et l’identité portée par le jeton OAuth 2.1 de chaque requête, le parc passe de 2 à 50 pods sans interruption.
::::

#### Extrait 5.1 — Cycle de vie protocolaire MCP sur Streamable HTTP et sortie structurée (structuredContent)

Un travailleur Boréal s’initialise auprès d’un serveur MCP d’inventaire, à travers agentgateway, selon le protocole d’avant la révision `2026-07-28`. Depuis cette révision, la poignée de main `initialize` est supprimée : la version et les capacités voyagent dans chaque requête, et la découverte passe par `server/discover` (sections 5.1 et 5.2) :

``` http
POST /mcp/bel-inventory HTTP/1.1
Host: agentgateway.internal.boreal.ca
Authorization: DPoP eyJhbGciOiJFUzI1NiIsInR5cCI6ImF0K2p3dCJ9...
DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2In0...
MCP-Protocol-Version: 2025-11-25
Content-Type: application/json
Accept: application/json, text/event-stream

{
  "jsonrpc": "2.0",
  "id": "init-01",
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
      "roots": { "listChanged": false },
      "sampling": {},
      "elicitation": { "form": {}, "url": {} }
    },
    "clientInfo": {
      "name": "boreal-temporal-maint-worker",
      "version": "3.2.0"
    }
  }
}
```

Dans cet échange, le serveur répond par `InitializeResult`, où il déclare `capabilities.tools`, et le client émet `notifications/initialized`. Il invoque ensuite un outil dont le résultat porte un résumé lisible et un objet JSON validé (`structuredContent`) :

``` json
{
  "jsonrpc": "2.0",
  "id": "call-408",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "1 kit ROTOR-KIT-HX9 disponible immédiatement au dépôt CA-QC-MTL-02 (allée B14)."
      }
    ],
    "structuredContent": {
      "materialCode": "ROTOR-KIT-HX9",
      "plantCode": "CA-QC-MTL-02",
      "availableUnrestrictedQty": 1,
      "unitOfMeasure": "EA",
      "estimatedPickReadyMinutes": 25,
      "schemaRef": "https://schemas.boreal.ca/ossie/v2/stock-availability.json"
    },
    "isError": false
  }
}
```

`structuredContent` s’appuie sur le `Tool.outputSchema` publié lors de `tools/list`. Le moteur d’orchestration aval ou le composant graphique A2UI consomme les champs typés sans analyser de texte.

------------------------------------------------------------------------

## 5.10 Primitives MCP : usages et garde-fous

Les primitives sont définies à la section 5.1. Le tableau plus bas fixe l’usage et le garde-fou de chacune; les points suivants en précisent les mécanismes. Les racines et l’échantillonnage sont toutefois dépréciés depuis la révision de juillet 2026 : ils fonctionnent encore pendant la fenêtre de dépréciation, mais une nouvelle mise en œuvre ne devrait pas les adopter (section 5.1). Les garde-fous qui les concernent valent tant qu’on les utilise.

- **Outils** : Les annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) restent des indices non fiables face à un serveur tiers; seule la politique Cedar appliquée sur agentgateway autorise l’exécution. La passerelle bloque aussi toute notification `notifications/tools/list_changed` dont l’empreinte SHA-256 de schéma n’a pas été scellée au préalable au registre d’homologation, ce qui neutralise les attaques par mutation différée (OWASP ASI04).
- **Ressources et `resource_link`** : Les entités sont exposées sous un URI canonique (`boreal://bca/contracts/CTR-9921`), avec abonnement optionnel par un flux `subscriptions/listen` (section 5.4). Plutôt que d’injecter un rapport de 180 Ko dans la réponse à `tools/call`, l’outil retourne un pointeur `resource_link` (URI, type MIME, taille), que `resources/read` ne lit qu’au besoin.
- **Prompts** : L’équipe propriétaire du progiciel maintient des procédures d’investigation paramétrées et versionnées, pour uniformiser les pratiques d’analyse.
- **Racines (`roots`)** : L’hôte restreint le serveur à des racines d’espaces ou à des compartiments (`file:///workspace/bel`, `s3://boreal-audit/`).
- **Échantillonnage** : Le serveur sollicite une synthèse auprès de l’hôte (`sampling/createMessage`) sans détenir de clé d’API de modèle. Pour contrer l’injection indirecte (OWASP ASI01), l’hôte exécute tout échantillonnage dans un contexte isolé, sans outils mutatifs et sous un plafond `maxTokens`.
- **Élicitation** : Elle sert à obtenir une donnée manquante ou un accord formel. Le serveur ne peut plus envoyer de requête de sa propre initiative : il renvoie un résultat `input_required` qui énumère ce qu’il lui faut, et le client réémet la requête d’origine avec les réponses (section 5.2). Elle procède selon deux modes. Le mode formulaire (`form`) présente un schéma JSON plat (`requestedSchema`), rendu par l’hôte (`accept`, `decline`, `cancel`). Le mode URL (`url`) est une redirection hors bande, obligatoire pour tout secret, consentement OAuth tiers, signature clinique ou validation financière, qui ne doivent pas transiter par le contexte du modèle.

| Primitive MCP | Direction de contrôle | Usage en entreprise | Vecteur de menace principal | Garde-fou obligatoire en production |
|:-----------|:----------------|:------------------------|:----------------------|:-------------------------|
| **Outils** | Le serveur expose, le modèle invoque | Recherches métier agrégées, actions transactionnelles idempotentes | Abus d’outil (ASI02), description empoisonnée (ASI04) | Empreinte SHA-256 du schéma et politique Cedar par outil sur agentgateway |
| **Ressources** | Le serveur expose, l’application sélectionne | Lecture par URI de contrats, de schémas, de journaux | Exfiltration en masse ou saturation du contexte | `resource_link` systématique pour toute charge $> 8\text{ Ko}$ |
| **Prompts** | Le serveur expose, l’hôte déclenche | Procédures d’analyse standardisées par domaine | Dérive ou altération non revue d’un gabarit | Revue de code Git et signature des versions du serveur MCP |
| **Racines** (dépréciées) | Le client déclare au serveur | Cloisonnement des répertoires ou des projets autorisés | Traversée de chemin côté serveur | Vérification canonique côté serveur (`realpath` ou préfixe d’URI) |
| **Échantillonnage** (déprécié) | Le serveur sollicite, l’hôte exécute | Synthèse ou classification locale demandée par un connecteur | Détournement de quota FinOps, injection de prompt inverse | Exécution sur SLM isolé sans outils, quota dur de jetons par appel |
| **Élicitation** | Le serveur sollicite, l’humain valide | Collecte d’un paramètre manquant ou consentement sensible | Hameçonnage interne par formulaire trompeur | Mode `url` exigé sur domaine certifié pour tout secret ou approbation critique |

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Santé & Sciences de la vie — Exposition granulaire de dossiers cliniques HL7 FHIR R4 via MCP audité (Loi 25, HIPAA)**
:::

Dans un centre hospitalier universitaire ou un réseau intégré de soins, au Québec et en Amérique du Nord, brancher un agent d’aide à la préparation de consultation sur l’entrepôt clinique complet d’un dossier santé électronique (DSE) contrevient au principe de nécessité minimale de la Loi 25 et de HIPAA, et compromet la sécurité des patients.

L’architecture de référence déployée en 2027 place le serveur HL7 FHIR R4 derrière un serveur MCP clinique, qui applique quatre verrous :

1.  **Jeton SMART-on-FHIR échangé en OAuth 2.1 OBO** : Sans compte de service global, le serveur MCP reçoit un jeton restreint au praticien actif et à l’identifiant exact du patient pris en charge (`launch/patient`, portées `patient/Observation.rs`, `patient/MedicationRequest.rs`).
2.  **Projection clinique déterministe et pseudonymisation** : Les outils MCP (`fhir_get_active_medications_summary`, `fhir_list_recent_lab_trends`) retirent à la source les identifiants administratifs directs inutiles au raisonnement médical (numéro d’assurance maladie, adresse postale, téléphone) et retournent des structures `structuredContent` normalisées en codes LOINC et SNOMED CT.
3.  **Pointeurs `resource_link` sur l’imagerie et les comptes rendus longs** : Les notes opératoires volumineuses sont retournées sous forme de liens URI `fhir://DocumentReference/...`, lus à la demande, avec journalisation unitaire dans la piste d’audit médico-légale (FHIR AuditEvent).
4.  **Validation médicale hors bande par élicitation en mode URL** : Aucun agent ne crée directement d’ordonnance active. Il prépare un brouillon (`status: draft`) et déclenche une élicitation URL, qui ouvre le module certifié de prescription électronique du DSE pour signature biométrique du clinicien.
::::

------------------------------------------------------------------------

## 5.11 Outils orientés intention métier

L’erreur la plus coûteuse des premiers déploiements MCP, en 2025–2026, est la génération automatique d’outils à partir de spécifications OpenAPI ou Swagger existantes. Pointé sur un progiciel de 90 routes REST conçues pour une interface web, un utilitaire de conversion livre un serveur MCP « en un après-midi », mais inutilisable en production, comme le montre la figure ci-dessous.

![Comparaison architecturale : mappage naïf 1:1 CRUD REST vers MCP face à la conception orientée intention métier agrégée.](figures/fig-05-a-2.svg)

Deux phénomènes expliquent l’échec d’un mappage CRUD 1:1. D’abord, chaque définition d’outil injectée dans la session consomme $t_i$ jetons d’instructions et de schémas JSON, répétés à chaque tour $k \in \{1, \dots, K\}$ de la boucle de raisonnement. Le surcoût fixe de contexte d’une tâche s’écrit :

$$T_{\text{schémas}}(N_{\text{outils}}, K) = K \cdot \sum_{i=1}^{N_{\text{outils}}} t_i$$

Avec $N_{\text{outils}} = 85$ points d’accès moyens ($t_i \approx 290$ jetons) et une transaction de $K = 6$ appels séquentiels pour reconstituer une jointure métier, l’agent consomme 147 900 jetons à relire le catalogue d’outils, avant de compter les données retournées. Ensuite, si la probabilité que le modèle choisisse le bon point d’accès et renseigne sans erreur ses clés étrangères internes vaut $p = 0,85$ à chaque étape, la fiabilité d’une séquence de $K = 6$ appels tombe à $p^6 \approx 0,377$ (37,7 %), en deçà du seuil d’exploitation industrielle.

| Dimension d’ingénierie | Antipatron : mappage CRUD REST 1:1 | Patron cible : outils MCP orientés intention métier |
|:-----------------------|:------------------------------------|:----------------------------------------|
| **Granularité du catalogue** | 40 à 150 points d’accès calqués sur les tables physiques | 5 à 12 outils cohésifs, alignés sur les actes métiers du domaine |
| **Empreinte de contexte par tour** | 12 000 à 35 000 jetons de schémas JSON bruyants | 800 à 1 800 jetons nets, discriminants |
| **Exécution des jointures** | Probabiliste : le modèle enchaîne 5 GET et croise en mémoire | Déterministe : jointure compilée en TypeScript ou en Go dans le serveur MCP |
| **Intégrité des mutations** | Écritures partielles orphelines en cas d’échec à l’étape $k$ | Atomique et idempotente (`idempotencyKey` et bail TTL, ou compensation) |
| **Couplage au progiciel** | Fuite des colonnes internes SQL ou ERP dans les prompts | Encapsulation par les types canoniques Apache Ossie |
| **Volume des réponses** | Tableaux JSON bruts non bornés, qui saturent le contexte | Pagination par curseur opaque et projection des seuls attributs utiles |
| **Traitement des erreurs** | Codes HTTP 400/500 ou traces techniques, qui provoquent des boucles | Erreurs cognitives structurées (`recoveryGuidance`), qui guident la correction |

### Pagination et erreurs cognitives

Un serveur MCP de production applique deux disciplines :

1.  **Pagination par curseur signé et plafond de cardinalité** : Un outil de recherche limite sa réponse à 15–20 entrées condensées ($\le 16\text{ Ko}$) et retourne un `nextCursor` opaque, accompagné de `totalMatched`. Au-delà de plusieurs centaines de lignes, le message invite l’agent à resserrer ses filtres métiers plutôt qu’à paginer en boucle.
2.  **Séparation entre faute protocolaire JSON-RPC et rejet métier `isError: true`** : Une erreur JSON-RPC (-32603) signale une panne technique. Un refus fonctionnel (rupture locale, révision d’article obsolète, clôture comptable) retourne un `result` marqué `isError: true`, avec une directive `recoveryGuidance` qui permet au modèle de se corriger dès le tour suivant.

#### Extrait 5.2 — Serveur MCP TypeScript orienté domaine avec pagination et erreurs cognitives auto-correctrices

L’outil de recherche de pièces de BEL applique ces deux disciplines :

``` typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

const server = new McpServer({
  name: "boreal-bel-spare-parts-mcp",
  version: "2.1.0"
});

const SearchStockInput = z.object({
  equipmentSerialNumber: z.string().describe("Numéro de série équipement (ex: BOR-CMP-90441)"),
  failureSymptomCode: z.string().optional().describe("Code défaut télématique normalisé"),
  preferredRegion: z.enum(["CA-QC", "CA-ON", "US-NE", "EU-FR"]),
  pageSize: z.number().int().min(1).max(20).default(10),
  cursor: z.string().optional().describe("Curseur opaque issu d'un appel précédent")
});

const SearchStockOutput = z.object({
  compatibleParts: z.array(z.object({
    materialCode: z.string(),
    descriptionFr: z.string(),
    plantCode: z.string(),
    availableQty: z.number(),
    leadTimeHours: z.number()
  })),
  pagination: z.object({
    totalMatched: z.number(),
    returnedCount: z.number(),
    nextCursor: z.string().nullable()
  })
});

server.registerTool(
  "bel_find_compatible_spare_stock",
  {
    title: "Recherche de pièces compatibles disponibles par équipement",
    description:
      "Résout la nomenclature exacte d'un équipement par son numéro de série et retourne les stocks disponibles dans la région cible. Utiliser avant toute réservation.",
    inputSchema: SearchStockInput.shape,
    outputSchema: SearchStockOutput.shape,
    annotations: {
      readOnlyHint: true,
      destructiveHint: false,
      idempotentHint: true,
      openWorldHint: false
    }
  },
  async (args, extra) => {
    const equipment = await sapCatalogRepo.lookupSerial(args.equipmentSerialNumber);

    // Erreur cognitive exploitable : guide immédiatement l'agent sans boucle aveugle
    if (!equipment) {
      const candidates = await sapCatalogRepo.fuzzyMatchSerial(args.equipmentSerialNumber, 3);
      return {
        isError: true,
        content: [{
          type: "text",
          text: JSON.stringify({
            errorCode: "EQUIPMENT_SERIAL_NOT_FOUND",
            retryable: true,
            providedSerial: args.equipmentSerialNumber,
            closestValidSerials: candidates,
            recoveryGuidance:
              "Le numéro de série fourni est introuvable dans SAP S/4HANA. Vérifiez le préfixe divisionnaire (ex: BOR-CMP-) parmi closestValidSerials ou interrogez le contrat client avant de réessayer."
          })
        }]
      };
    }

    const page = await sapInventoryService.queryCompatibleStock({
      bomId: equipment.activeBomId,
      symptomCode: args.failureSymptomCode,
      region: args.preferredRegion,
      limit: args.pageSize,
      cursor: args.cursor,
      traceId: extra?._meta?.traceparent as string | undefined
    });

    const payload = {
      compatibleParts: page.items,
      pagination: {
        totalMatched: page.totalCount,
        returnedCount: page.items.length,
        nextCursor: page.nextCursor ?? null
      }
    };

    return {
      isError: false,
      structuredContent: payload,
      content: [{
        type: "text",
        text: `${page.items.length}/${page.totalCount} pièce(s) compatible(s) trouvée(s) en zone ${args.preferredRegion}.`
      }]
    };
  }
);
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Industrie Manufacturière & Énergie (IT/OT) — Serveurs MCP en lecture seule sur OPC UA et historiens d'usine**
:::

Pour raccorder des agents de diagnostic industriel aux ateliers sans menacer l’intégrité des automates programmables (PLC), les ingénieurs IT/OT placent un serveur MCP d’observation dans la zone démilitarisée industrielle (IDMZ, niveau 3.5 du modèle Purdue) :

- Le serveur MCP interroge un réplica de l’historien de procédés (OSIsoft PI / AVEVA, InfluxDB) et une passerelle OPC UA configurée en lecture seule, matériellement et cryptographiquement.
- Plutôt que d’exposer des millions de points bruts à 100 Hz, qui satureraient la fenêtre de contexte, les outils MCP calculent localement, en Rust ou Python, les descripteurs physiques pertinents (valeur efficace RMS, kurtosis vibratoire, dérive thermique sur 30 minutes, corrélation avec les changements d’outil MES) et ne renvoient au modèle que le vecteur d’anomalie condensé.
::::

------------------------------------------------------------------------

## 5.12 Compétences et navigateur : Agent Skills, AGENTS.md, Open Responses et WebMCP

Des outils MCP ne suffisent pas sans doctrine d’emploi formalisée, mais figer toutes les procédures de l’entreprise dans un prompt système permanent de 35 000 jetons pèse sur le budget FinOps et dilue l’attention du modèle. La pile AAIF et W3C y répond par trois standards cognitifs et une interface navigateur.

### Agent Skills : divulgation progressive en trois paliers

Un paquet Agent Skills (AAIF) est un répertoire versionné et portable, centré sur `SKILL.md` et accompagné au besoin de `scripts/` et de `references/`. Il se charge en trois paliers :

- **Palier 1 — Découverte au repos (\~60–90 jetons)** : Seul l’en-tête YAML (`name`, et `description` des conditions d’activation) est préchargé, ce qui permet d’indexer 25 compétences métiers sous les 2 000 jetons.
- **Palier 2 — Activation ciblée** : Lorsque la mission correspond, l’hôte injecte le corps procédural de `SKILL.md` ($< 2\,500$ jetons), qui dicte l’enchaînement des outils MCP et les seuils de contrôle.
- **Palier 3 — Références à la demande et scripts confinés** : Les barèmes détaillés restent dans `references/`. Les calculs déterministes de `scripts/` s’exécutent dans OpenSandbox, hors de la fenêtre de contexte.

`AGENTS.md` consigne à la racine de chaque dépôt les invariants permanents de l’espace de travail. Open Responses monte dynamiquement les serveurs MCP requis, avec une liste blanche stricte (`allowedTools`).

#### Extrait 5.3 — Paquet portable Agent Skills (SKILL.md) et montage filtré sous Open Responses

La compétence de triage d’écart de stock de BEL tient dans le `SKILL.md` suivant :

``` markdown
---
name: boreal-sap-stock-discrepancy-triage
description: Diagnostique et résout un écart entre le stock théorique SAP S/4HANA et le comptage physique dépôt chez BEL. Activer lors d'une alerte d'inventaire négatif, d'un écart de préparation WMS ou avant d'autoriser un ajustement de stock L2/L3.
metadata:
  owner: coe-supply-chain@boreal.ca
  version: "1.4.0"
  compliance: ["SOX-INV-04"]
---

# Procédure normalisée — Triage d'écart de stock (BEL)

1. **Vérification des mouvements en transit** : Appeler `bel_find_compatible_spare_stock` puis `sap_list_pending_goods_movements` sur les 48 dernières heures avant de conclure à une perte sèche.
2. **Rapprochement statistique** : Exécuter dans `OpenSandbox` le script `scripts/reconcile_wms_sap_delta.py` sur l'export JSON retourné.
3. **Règle financière SOX** :
   - Écart absolu <= 750 $ CAD et cause identifiée (erreur d'emplacement interne) : préparer la régularisation via `sap_propose_inventory_adjustment`.
   - Écart > 750 $ CAD ou numéro de série réglementé : consulter `references/sox-escalation-matrix.md` et déclencher une approbation superviseur `HOTL`.
```

Lorsqu’un travailleur active cette compétence par Open Responses, il restreint la surface d’outils MCP exposée au modèle :

``` json
{
  "specVersion": "open-responses/1.0",
  "storeStateRemotely": false,
  "instructions": "Applique strictement la compétence activée boreal-sap-stock-discrepancy-triage.",
  "mcpServers": [
    {
      "serverLabel": "sap-bel-inventory",
      "serverUrl": "https://agentgateway.internal.boreal.ca/mcp/bel-inventory",
      "allowedTools": [
        "bel_find_compatible_spare_stock",
        "sap_list_pending_goods_movements",
        "sap_propose_inventory_adjustment"
      ]
    }
  ],
  "input": [
    {
      "type": "message",
      "role": "user",
      "content": "Alerte WMS dépôt CA-QC-MTL-02 : 0 unité physique trouvée en B14 pour ROTOR-KIT-HX9 alors que SAP affiche 1 EA (valeur 1 840 $ CAD)."
    }
  ]
}
```

### WebMCP : l’application web comme serveur d’outils côté client

Piloter une application web interne par un agent de capture d’écran (CUA) souffre d’une latence élevée (15–40 s), d’un surcoût visuel et d’une fragilité aux refontes CSS. La spécification WebMCP, incubée au W3C Web Machine Learning Community Group, permet à la page active d’exposer au navigateur des outils JavaScript typés. Exécutés dans l’onglet de l’opérateur, ces outils héritent de sa session authentifiée et pilotent l’état de l’interface en direct. Ils se désinscrivent automatiquement par `AbortSignal` au changement de vue, sous isolation stricte d’origine (`Permissions-Policy: tools=(self)`).

| Standard vertical | Lieu d’exécution | Ce qu’il normalise | Coût en contexte | Cas d’emploi privilégié |
|:------------|:-------------------|:-------------------------|:------------------|:-------------------------|
| **Serveur MCP** | Service distant (Streamable HTTP) | Accès transactionnel aux API, bases et systèmes (outils, ressources) | \~150–250 jetons par outil exposé | Flux de travail asynchrone sans humain, ou accès sécurisé entre systèmes |
| **Agent Skills** | Hôte et OpenSandbox | Savoir-faire procédural métier et scripts déterministes associés | \~70 jetons au repos; \~1 800 actif | Standardiser une méthode métier complexe de façon portable |
| **`AGENTS.md`** | Racine du dépôt ou espace de travail | Invariants locaux, commandes de vérification, frontières interdites | \~300–800 jetons fixes par espace | Guider les agents d’ingénierie, de données et d’audit documentaire |
| **WebMCP** | Onglet actif du navigateur client (W3C) | Fonctions d’interface typées et formulaires annotés dans la session humaine | Outils exposés sur la seule vue active | Co-navigation rapide humain-agent, sans extraction du DOM ni CUA |

#### Extrait 5.4 — Instrumentation hybride WebMCP (API impérative registerTool + formulaire déclaratif)

Dans la console web des répartiteurs de Boréal Services Numériques, l’enregistrement suivant rend l’écran de planification terrain pilotable par l’assistant navigateur de l’opérateur :

``` typescript
// Enregistrement impératif lié au montage/démontage du composant de carte terrain
export function mountDispatchMapWebMcpTools(dispatchStore: DispatchViewStore): () => void {
  const controller = new AbortController();
  const modelCtx =
    (navigator as unknown as { modelContext?: ModelContextContainer }).modelContext ??
    (document as unknown as { modelContext?: ModelContextContainer }).modelContext;

  if (!modelCtx?.registerTool) {
    return () => {};
  }

  modelCtx.registerTool(
    {
      name: "bsn_filter_nearby_certified_technicians",
      description:
        "Filtre en direct sur la carte opérateur les techniciens certifiés haute pression disponibles dans un rayon donné autour du site client actif.",
      inputSchema: {
        type: "object",
        properties: {
          maxRadiusKm: { type: "number", minimum: 5, maximum: 250 },
          requiredCertification: { type: "string", enum: ["HP-COMP-L2", "ELEC-HV", "CRYO"] },
          availableWithinHours: { type: "number", minimum: 1, maximum: 72 }
        },
        required: ["maxRadiusKm", "requiredCertification"],
        additionalProperties: false
      },
      execute: async (input: Record<string, unknown>) => {
        const matches = await dispatchStore.applyMapFilter(input);
        return {
          content: [{
            type: "text",
            text: `${matches.length} technicien(s) affiché(s) sur la carte (plus proche : ${matches[0]?.etaMinutes ?? "N/A"} min).`
          }]
        };
      }
    },
    { signal: controller.signal } // Désinscription automatique dès fermeture de la vue
  );

  return () => controller.abort();
}
```

Pour les écrans de saisie simples, WebMCP offre aussi une syntaxe HTML déclarative, sans code JavaScript supplémentaire. L’attribut `toolautosubmit="false"` laisse à l’opérateur le clic final de validation :

``` html
<form id="sla-credit-note" action="/api/bsn/credits" method="post"
      toolname="bsn_prepare_sla_credit_draft"
      tooldescription="Pré-remplit une demande d'avoir commercial après un dépassement SLA vérifié"
      toolautosubmit="false">
  <input type="text" name="ticketId" toolparamdescription="Identifiant du billet ServiceNow (ex: INC009412)" required />
  <input type="number" name="creditAmountCad" min="0" max="2500" step="0.01"
         toolparamdescription="Montant proposé en dollars canadiens selon barème contractuel" required />
  <textarea name="justification" toolparamdescription="Synthèse factuelle de l'écart SLA mesuré" required></textarea>
  <button type="submit">Valider et soumettre l'avoir</button>
</form>
```

------------------------------------------------------------------------

## 5.13 Application au fil rouge : connectivité verticale au Groupe Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Industrialisation des serveurs MCP SAP S/4HANA, Snowflake et ServiceNow**
:::

**Problème rencontré début 2027** : Lors des premiers essais d’intégration chez BEL et BSN, un prestataire avait généré automatiquement un serveur MCP qui exposait 112 opérations OData brutes de SAP S/4HANA. Une équipe analytique de BCA laissait un agent exécuter du SQL généré à la volée sur Snowflake, avec un compte de service partagé. Résultat : 29 000 jetons consommés par tour, un taux de réussite $\text{pass}^5$ plafonné à 54 % sur les réservations complexes, et un veto immédiat du CISO devant le risque d’injection SQL sémantique et d’accès transversal aux tables clients soumises à la Loi 25.

**Architecture verticale mise en production (T1–T2 2027)** : L’équipe plateforme remplace ces prototypes par trois serveurs MCP orientés domaine, en Streamable HTTP sans état derrière agentgateway. Un registre Git interne de compétences et l’instrumentation WebMCP les complètent :

1.  **Serveur MCP SAP S/4HANA (BEL — 8 outils métiers)** : Il encapsule la vérification de nomenclature, la réservation idempotente à bail temporel (`ttlHoldMinutes`) et la proposition d’ajustement d’inventaire par les BAPI officielles, avec les erreurs cognitives de l’Extrait 5.2.
2.  **Serveur MCP Snowflake & Contrats (BCA — 6 outils + ressources URI)** : Le SQL libre généré par le modèle est interdit. Le serveur n’expose que des vues paramétrées gouvernées sous OAuth 2.1 OBO, avec masquage dynamique des champs nominatifs (Loi 25), pagination par curseur (max 15 lignes) et renvoi de pointeurs `resource_link` pour les annexes PDF.
3.  **Serveur MCP ServiceNow ITSM/FSM (BSN — 7 outils + prompts + élicitation URL)** : Il gère le cycle de vie des billets télématiques, l’affectation de techniciens et le déclenchement d’élicitations URL sécurisées dès qu’un geste commercial dépasse le plafond automatique.
4.  **Catalogue de 14 paquets Agent Skills et WebMCP sur le portail BSN** : Les procédures d’audit de stock et de garantie sont formalisées en `SKILL.md` portables, et 9 outils WebMCP sont ajoutés à la console web des répartiteurs BSN, ce qui élimine un projet coûteux d’automatisation par capture d’écran.

**Gains mesurés en production après 90 jours** :

- **Empreinte de contexte** : -94,3 % sur les schémas et métadonnées par tour (de 29 000 à 1 650 jetons) et -78 % sur le volume total de jetons consommés par tâche verticale complète.
- **Fiabilité d’exécution ($\text{pass}^5$ sous OpenEnv)** : de 54 % à 96,8 %, grâce aux outils d’intention agrégés, aux sorties `structuredContent` et aux messages `recoveryGuidance`.
- **Poste répartiteur (WebMCP)** : préparation d’un dossier d’affectation complexe ramenée de 38 secondes (prototype CUA visuel) à 1,4 seconde, avec validation finale humaine garantie (`toolautosubmit="false"`).
- **Conformité de sécurité** : 100 % des appels tracés nominalement par employé ou par saga initiatrice, par OAuth 2.1 OBO et DPoP sur agentgateway; zéro secret applicatif stocké dans les agents.
::::

------------------------------------------------------------------------

## 5.14 Décision d’architecture et liste de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-005 — Standardisation de l'exposition d'outils métiers sur MCP Streamable HTTP orienté domaine, Agent Skills et WebMCP**
:::

- **Statut** : Acceptée \| Périmètre : Tous les connecteurs systèmes, compétences métiers et portails web internes \| Révision : Semestrielle
- **Contexte** : L’exposition brute d’API REST granulaires ou de requêtes SQL libres aux modèles de langage augmente les coûts de jetons, dégrade la fiabilité des séquences à plusieurs étapes, couple les agents aux schémas physiques des progiciels et ouvre des vulnérabilités d’autorisation. Les agents de capture d’écran (CUA) appliqués à nos propres applications web internes ajoutent une latence et une fragilité évitables.
- **Options évaluées** :
  1.  *Convertisseurs automatiques OpenAPI-vers-MCP sur les API existantes* : Rejetée — surcharge cognitive (\> 50 outils), jointures probabilistes fragiles, absence d’idempotence native.
  2.  *Bibliothèques d’outils codées en dur dans chaque cadriciel d’agent* : Rejetée — aucune réutilisation entre Python, TypeScript et studios SaaS; gouvernance de sécurité dispersée.
  3.  *Façades MCP orientées domaine sur Streamable HTTP + paquets Agent Skills + WebMCP pour le Web interne* : Retenue.
- **Décision** :
  1.  Tout accès vertical côté serveur passe par un serveur MCP en Streamable HTTP (mode sans état privilégié) derrière agentgateway, authentifié en OAuth 2.1 OBO et limité à 15 outils au maximum par serveur, orientés intention métier. Cette authentification va au-delà de ce que retient la section 5.5, où l’option par défaut est l’Enterprise-Managed Authorization (ID-JAG) si le fournisseur d’identité et les clients la prennent en charge, sinon le flux OAuth de base.
  2.  Chaque outil mutatif exige une clé d’idempotence explicite. Chaque outil déclare un `outputSchema`, retourne `structuredContent` et produit des erreurs métier qui guident la correction (`isError: true` + `recoveryGuidance`). Les charges volumineuses ($> 8\text{ Ko}$) transitent par `resource_link`.
  3.  Les procédures opérationnelles transversales sont externalisées dans des paquets Agent Skills (`SKILL.md` à divulgation progressive), dont les scripts s’exécutent sous OpenSandbox.
  4.  Toute nouvelle vue d’application web interne fréquemment assistée par agent expose ses actions par WebMCP plutôt que de recourir à un CUA par capture d’écran, réservé aux systèmes patrimoniaux fermés traités au chapitre 25.
- **Conséquences** :
  - *Positives* : Précision d’appel supérieure à 95 %, économie de jetons, sécurité par moindre privilège et portabilité des compétences métiers.
  - *Négatives / Coûts assumés* : Travail explicite de conception produit pour façonner les façades MCP de domaine, plutôt que de générer des connecteurs bruts.
- **Condition de révision** : Semestrielle, selon l’évolution des spécifications MCP (AAIF) et l’avancement du standard WebMCP au sein du W3C.
::::

### Liste de contrôle de mise en production

Avant sa mise en production, chaque connecteur vertical satisfait aux huit vérifications suivantes :

1.  **Streamable HTTP et identité** : Le serveur MCP fonctionne-t-il sur Streamable HTTP derrière agentgateway, avec vérification de MCP-Protocol-Version et jeton OAuth 2.1 OBO, sans `stdio` sur le réseau ni clé d’API partagée ?
2.  **Sobriété et cohésion du catalogue** : Le serveur expose-t-il au plus 12 à 15 outils conçus autour d’intentions métiers complètes, sans conversion 1:1 de tables CRUD ?
3.  **Validation et idempotence** : Chaque outil valide-t-il son `inputSchema`, publie-t-il son `outputSchema` (`structuredContent`) et exige-t-il une `idempotencyKey` pour toute opération à effet de bord ?
4.  **Protection de la fenêtre de contexte** : Les recherches sont-elles toutes paginées par curseur borné, et les documents de plus de 8 Ko retournés sous forme de pointeurs `resource_link` ?
5.  **Erreurs cognitives exploitables** : Les rejets fonctionnels retournent-ils `isError: true` avec un champ `recoveryGuidance` précis qui permet au modèle de se corriger sans boucler ?
6.  **Confinement de l’échantillonnage et de l’élicitation** : Si l’échantillonnage, déprécié (section 5.1), est encore utilisé, les demandes `sampling/createMessage` sont-elles isolées, sans outils et sous quota strict, et toute collecte de secret ou d’approbation sensible passe-t-elle par le mode URL hors bande de l’élicitation (résultat `input_required`, section 5.2) ?
7.  **Divulgation progressive des compétences** : Les procédures complexes sont-elles structurées en paquets Agent Skills (`SKILL.md` concis, `scripts/` confinés dans OpenSandbox) plutôt qu’empilées dans une consigne système monolithique ?
8.  **Priorité à WebMCP sur le Web interne** : Aucune automatisation par capture d’écran n’est-elle commandée pour un portail web interne capable d’exposer ses actions par WebMCP (`toolautosubmit="false"` pour les mutations sensibles) ?
