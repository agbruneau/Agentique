## Mise en œuvre — Coordination horizontale, découverte et réseau inter-agents {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Les processus à forte valeur (instruire une garantie complexe, réacheminer un flux logistique international, qualifier un risque de crédit) traversent plusieurs divisions et partenaires externes, qui refusent d’exposer leurs bases de données, leurs consignes système ou leurs modèles internes. Tant qu’un agent opère seul au-dessus de ses outils MCP (chapitre 5), l’entreprise n’automatise que des silos locaux. Sans protocole horizontal normalisé, elle multiplie les adaptateurs fragiles, les boucles infinies entre agents et les risques d’usurpation de capacités (OWASP ASI07).
- **Décisions architecturales structurantes** :
  1.  *Irréversible à moyen terme* : Proscrire l’encapsulation d’agents autonomes à cycles longs derrière de simples outils MCP synchrones; imposer A2A v1.0 pour toute délégation d’objectif entre pairs opaques.
  2.  *Structurante dès le passage à l’échelle (\> 15 agents)* : Remplacer les listes statiques d’URL par un catalogue fédéré modélisé en AGNTCY OASF (*Open Agentic Schema Framework*), où chaque fiche et chaque Agent Card sont signées cryptographiquement (JWS / Sigstore).
  3.  *Progressive selon la criticité réseau* : Conserver HTTPS, SSE et webhooks pour les flux courants. Activer le bus AGNTCY SLIM, couplé au chiffrement de groupe IETF MLS (RFC 9420) hybride post-quantique, pour les cellules collaboratives en temps réel, les sites industriels isolés et les échanges B2B sensibles.
- **Indicateurs de gouvernance associés** : Délai d’intégration d’un nouvel agent spécialiste au maillage (cible : \< 48 h sans redéployer les orchestrateurs), part des tâches longues traitées sans interrogation périodique (\> 95 %), temps de révocation cryptographique MLS et zéro délégation inter-domaines sans signature Agent Card valide.
::::

## 6.8 Protocole A2A v1.0 : Agent Cards, tâches asynchrones et artefacts typés

La distinction entre outil et agent pair est posée à la section 6.6. Elle commande une règle d’architecture : un agent autonome à cycle long ne s’expose pas comme un outil MCP synchrone.

### Choix de la version 1.0 qui orientent la mise en œuvre

Les liaisons, la distinction entre message et tâche, et les parties sont décrites aux sections 6.2 à 6.4. Trois précisions guident la conception :

1.  **Liaisons** : HTTP+JSON/REST, hérité d’ACP, se prête mieux à l’inspection par les passerelles API; JSON-RPC 2.0 sur HTTPS reste le profil universel et gRPC sert la haute performance.
2.  **Message ou tâche** : héritée d’ACP, la distinction évite d’instancier un état lourd pour une interaction résolue en un tour sous deux secondes. Dès qu’un traitement implique asynchronisme, réessais ou validation tierce, l’échange est promu en tâche versionnée.
3.  **Parties typées** : la version 1.0 fusionne les types de parties en un seul (`Part`), qui contient du texte, des octets, une URL ou des données structurées (sections 6.2 et 6.4). Les données structurées sont soumises à JSON Schema et la référence à un fichier se fait par URI présignée bornée dans le temps, ce qui remplace le texte brut ambigu.

| Critère d’ingénierie | Sous-agent en outil MCP (antipatron) | ACP historique (avant la fusion de 2025) | A2A v1.0 — flux SSE (régime T2) | A2A v1.0 — notification poussée par webhook et exécution durable (régimes T3–T4) |
|:-------------|:----------------------|:-----------------|:-----------------------|:-----------------------|
| Opacité et sécurité | Faible : fuite d’indices internes dans le contexte parent | Bonne : isolation des environnements d’exécution locaux | Élevée : Agent Card signée + OAuth 2.1 OBO | Maximale : zéro connexion entrante maintenue pendant l’attente |
| Négociation multi-tours | Absente (texte d’erreur libre ambigu) | Sessions REST locales | Native via l’état `INPUT_REQUIRED` et `contextId` | Native via `INPUT_REQUIRED` / `AUTH_REQUIRED`, qui réveille un `awakeable` |
| Horizon temporel | 1 s à 60 s (délais d’expiration des outils) | Secondes à minutes | 2 s à 3 min (flux HTTP/2 SSE actif) | Minutes à plusieurs semaines (mise en veille complète) |
| Livraison de sortie | Bloc JSON ou texte unique final | Flux MIME multipart | Incrémentale (`TaskArtifactUpdateEvent`) | Artefact immuable notifié par webhook signé JWS |
| Usage recommandé | Proscrit pour un pair autonome | Migré vers la liaison REST d’A2A v1.0 | Coopération interactive reliée à AG-UI | Sagas inter-divisions, conformité et logistique B2B |

### Sécurité de l’Agent Card et usurpation de capacités

Toute interaction commence par la lecture de l’Agent Card (`/.well-known/agent-card.json`; structure à la section 6.2). Deux mécanismes de la version 1.0 en verrouillent l’exposition en production :

- **Carte publique minimale, carte étendue authentifiée** (`capabilities.extendedAgentCard: true`) : l’URL publique anonyme ne révèle que l’identité de routage et les schémas d’authentification. Les compétences fines autorisées pour le locataire de l’appelant se lisent par l’opération `GetExtendedAgentCard`, avec un jeton valide.
- **Signature canonique** (`signatures`, JWS RFC 7515) : l’autorité de plateforme signe la carte canonisée (RFC 8785 JCS), contre l’usurpation de capacités (OWASP ASI07), où un conteneur compromis annoncerait de fausses compétences financières pour intercepter des dossiers. La passerelle agentgateway bloque tout routage vers une carte non certifiée.

### Machine à états d’une tâche et exécution sans interrogation périodique

Lors d’un appel `SendMessage` ou `SendStreamingMessage`, le `contextId` relie les échanges successifs d’un même dossier et le `taskId` identifie l’unité atomique, régie par une machine à états déterministe.

![Cycle de vie complet d’une tâche asynchrone A2A v1.0 : découverte, négociation multi-tours, streaming SSE et notifications push signées.](figures/fig-06-a-1.svg)

Les huit états de `TaskState` sont présentés à la section 6.2 : la version 1.0 les préfixe par `TASK_STATE_` et les écrit en majuscules, valeurs corrigées en 1.0.1 (section 6.4). Le tableau les abrège et précise l’action de l’orchestrateur appelant pour chacun.

| État `TaskState` | Catégorie | Signification protocolaire | Action requise côté orchestrateur appelant |
|:-------------|:------------------|:------------------------------|:-------------------------------------|
| `SUBMITTED` | En cours | Tâche authentifiée, validée et mise en file persistante. | Journaliser le `taskId`; conserver la même clé d’idempotence en cas de réessai. |
| `WORKING` | En cours | Inférence du spécialiste et appels MCP internes en cours. | Consommer le flux SSE (T2) ou suspendre le flux de travail en attente du webhook (T3–T4). |
| `INPUT_REQUIRED` | Interrompu | Donnée métier complémentaire requise pour trancher. | Extraire le schéma demandé, collecter la preuve et rappeler `SendMessage` sur le même `taskId`. |
| `AUTH_REQUIRED` | Interrompu | Consentement hors bande (CIBA, *Client-Initiated Backchannel Authentication*) ou jeton tiers requis. | Acquérir le jeton d’élévation, puis relancer la tâche suspendue. |
| `COMPLETED` | Terminal | Succès; artefacts immuables et typés joints. | Valider l’`outputSchema`, enregistrer l’artefact et passer à l’étape suivante. |
| `FAILED` | Terminal | Échec non récupérable localement malgré les réessais internes. | Déclencher sans délai la séquence de compensation de la saga parente. |
| `CANCELED` | Terminal | Annulation confirmée après une requête `CancelTask`. | Vérifier la libération des verrous temporaires chez le pair. |
| `REJECTED` | Terminal | Refus avant tout effet de bord (politique Cedar, quota). | Basculer vers un pair alternatif de l’annuaire; aucune compensation n’est requise. |

Deux mécanismes de la version 1.0 assurent la résilience sur des réseaux d’entreprise imparfaits :

- **Reconnexion sans perte (`SubscribeToTask`)** : en régime T2 (2 secondes à 3 minutes), l’appelant dont la connexion SSE est interrompue, par le redémarrage d’un pod répartiteur de charge ou un basculement Wi-Fi, invoque `SubscribeToTask` avec le `taskId` et le dernier identifiant d’événement reçu. Le serveur rejoue les transitions d’état manquées depuis son tampon d’événements, sans relancer l’inférence sous-jacente.
- **Assemblage incrémental des artefacts (`append` et `lastChunk`)** : un spécialiste qui produit un rapport d’audit structuré ou un lot de données volumineux émet une suite de `TaskArtifactUpdateEvent` qui partagent le même `artifactId`, avec `append: true` jusqu’au fragment final marqué `lastChunk: true`. L’orchestrateur inspecte la sortie au fil de l’eau, détecte par exemple une violation de politique et émet aussitôt `CancelTask` pour couper les frais d’inférence inutiles.

#### Extrait 6.1 — Séquence JSON-RPC 2.0 A2A (syntaxe de la version 0.3) : soumission asynchrone, suspension input-required et artefact typé

Un orchestrateur soumet à BCA une demande de garantie en mode non bloquant; BCA suspend la tâche en `INPUT_REQUIRED` par webhook, puis livre un artefact typé.

L’extrait suit la syntaxe de la version 0.3 : les états sont en minuscules avec tiret et les parties se distinguent par un champ `kind`; pour la version 1.0, l’exposé indique des états préfixés `TASK_STATE_` et écrits en majuscules (sections 6.2 et 6.4) et un seul type de partie (section 6.4). Les noms d’opérations et de configuration de l’extrait (`message/send`, `blocking`, `pushNotificationConfig`) sont aussi ceux de la version 0.3; la version 1.0 les nomme `SendMessage`, `returnImmediately` et `taskPushNotificationConfig`.

``` json
[{
  "_step": "1. POST https://agentgateway.internal.boreal.ca/a2a/bca/warranty",
  "jsonrpc": "2.0",
  "id": "rpc-req-4401",
  "method": "message/send",
  "params": {
    "message": {
      "messageId": "msg-901a-77c2",
      "contextId": "ctx-incident-comp-90441",
      "role": "user",
      "parts": [{
        "kind": "data",
        "mimeType": "application/json",
        "data": {
          "equipmentSerial": "BOR-CMP-90441",
          "faultSignatureCode": "VIB-BEARING-OUTER-RACE-H3",
          "estimatedRepairCad": 3850.00,
          "preventiveReplacement": true
        }
      }],
      "metadata": {
        "borealActionEnvelope": {
          "sagaId": "saga-inc-2027-088412",
          "stepIdempotencyKey": "idem-bca-adj-088412-v1",
          "maxRemainingHops": 3,
          "maxBudgetCad": 0.45,
          "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-88a12b33c901d4e2-01"
        }
      }
    },
    "configuration": {
      "acceptedOutputModes": ["application/json", "application/pdf"],
      "blocking": false,
      "pushNotificationConfig": {
        "id": "push-cfg-temporal-088412",
        "url": "https://callbacks.internal.boreal.ca/a2a/v1/webhook",
        "token": "awk-tok-9f8e7d6c5b4a3210",
        "authentication": { "schemes": ["Bearer", "X-A2A-Signature-JWS"] }
      }
    }
  }
},
{
  "_step": "2. Webhook poussé par BCA 9 s plus tard (Transition -> input-required)",
  "kind": "status-update",
  "taskId": "tsk-bca-772019",
  "contextId": "ctx-incident-comp-90441",
  "final": false,
  "status": {
    "state": "input-required",
    "timestamp": "2027-03-14T14:22:19.410Z",
    "message": {
      "messageId": "msg-bca-req-calib",
      "role": "agent",
      "parts": [{
        "kind": "data",
        "mimeType": "application/json",
        "data": {
          "missingField": "lastLubricationComplianceHash",
          "policyClause": "BCA-IND-2026-ART14.2"
        }
      }]
    }
  }
},
{
  "_step": "3. Webhook final après réponse automatique de BSN (completed + Artifact)",
  "kind": "artifact-update",
  "taskId": "tsk-bca-772019",
  "contextId": "ctx-incident-comp-90441",
  "append": false,
  "lastChunk": true,
  "artifact": {
    "artifactId": "art-warranty-auth-99102",
    "name": "warranty-preauthorization-decision",
    "parts": [
      {
        "kind": "data",
        "mimeType": "application/json",
        "data": {
          "decision": "APPROVED_ZERO_DEDUCTIBLE",
          "authorizedCapCad": 4500.00,
          "authorizationCode": "BCA-PREAUTH-2027-551902",
          "validUntilIso": "2027-03-21T14:22:35Z"
        }
      },
      {
        "kind": "file",
        "file": {
          "name": "certificat-couverture-551902.pdf",
          "mimeType": "application/pdf",
          "uri": "https://vault.boreal.ca/artifacts/cert-551902.pdf?sig=8b7a"
        }
      }
    ]
  }
}]
```

:::: {.encadre .warning}
::: {.encadre-titre}
**Avertissement**
:::

**Webhooks : protection contre le SSRF et le DNS rebinding** : Le risque d’une adresse de rappel interne, ou SSRF (falsification de requête côté serveur), est décrit à la section 6.3. L’émetteur le ferme par quatre mesures : une liste blanche des domaines de rappel liée à l’identité SPIFFE/DID de l’appelant; un proxy sortant dédié, isolé du réseau interne; la vérification, à l’ouverture de la connexion, de l’adresse du socket effectif, après une résolution DNS unique épinglée qui pare le DNS rebinding à `TTL = 0`, pour écarter les adresses privées (RFC 1918) et les métadonnées infonuagiques (169.254.169.254); la signature de chaque envoi par un en-tête JWS horodaté muni d’un `nonce` anti-rejeu.
::::

------------------------------------------------------------------------

## 6.9 Découverte dynamique et modélisation des capacités avec AGNTCY OASF et Agent Directory

Dès qu’un groupe exploite des dizaines d’agents répartis entre filiales et partenaires, coder en dur les URL ou injecter cent descriptions textuelles dans la consigne d’un orchestrateur ne tient plus. Confier la sélection au seul jugement sémantique d’un LLM sur de la prose libre gonfle la facture de jetons et ouvre la porte au *SEO d’Agent Card* malveillant. La spécification ne standardise pas l’interrogation d’un catalogue (section 6.7; gouvernance du registre au chapitre 8).

AGNTCY, projet ouvert par Cisco (Outshift) avec LangChain et Galileo, puis confié à la Linux Foundation (chapitre 7), y répond par le couple OASF et Agent Directory.

### OASF : taxonomie déterministe et provenance OCI

OASF fournit un schéma déclaratif versionné qui encadre le cycle de vie d’un agent autour de quatre composantes :

1.  **Taxonomie hiérarchique contrôlée (`skills` et `domains`)** : des identifiants normalisés (`supply_chain/trade_compliance/hs_tariff_classification`), extensibles par espace de noms privé (`x-boreal/*`), remplacent les synonymes flous. La présélection devient une requête d’index exacte, en moins d’une milliseconde.
2.  **Localisateurs multiprotocoles (`locators`)** : une fiche unique relie la référence de l’artefact conteneur, l’URL de l’Agent Card A2A v1.0 et l’identifiant de routage SLIM en temps réel.
3.  **Modules d’évaluation et de conformité (`modules`)** : ils attachent les métriques mesurées en CI/CD (ADLC, chapitre 34), soit la stabilité $\text{pass}^k$, la latence P95 et le coût médian, ainsi que la juridiction d’hébergement et la classification BSIF E-23 ou EU AI Act.
4.  **Signature Sigstore sur registre OCI** : chaque manifeste OASF est publié comme artefact OCI (*Open Container Initiative*) et signé par Cosign / Sigstore dans un journal de transparence vérifiable.

### Routage distribué par Agent Directory (DHT Kademlia)

Pour fédérer plusieurs entités sans registre central vulnérable, Agent Directory sépare le stockage de l’indexation. Chaque division garde ses manifestes complets dans son registre OCI local et annonce les empreintes cryptographiques (SHA-256) de ses compétences sur une table de hachage distribuée (DHT) Kademlia. Après une résolution en $\mathcal{O}(\log M)$ sauts et la vérification des signatures, le routeur du plan de contrôle évalue chaque candidat $a$ selon un score déterministe :

$$\text{Score}(a) = \mathbb{I}_{\text{pol}}(a) \cdot \left( w_s S_{\text{sem}}(a) + w_r \text{pass}^k(a) - w_c \hat{C}(a) - w_l \hat{L}_{95}(a) \right)$$

Ici, $\mathbb{I}_{\text{pol}}(a) \in \{0, 1\}$ représente le filtre éliminatoire Cedar/OPA (résidence des données, plafond d’autonomie), $S_{\text{sem}}(a)$ la compatibilité des schémas JSON, $\text{pass}^k(a)$ la fiabilité certifiée, et $\hat{C}(a), \hat{L}_{95}(a)$ le coût et la latence P95 normalisés.

Le cache et la révocation sont gouvernés. Les passerelles agentgateway gardent localement les résolutions OASF fréquentes avec un bail court (TTL de 60 à 300 secondes), pour ne pas solliciter la DHT à chaque micro-transaction. Si la surveillance OpenTelemetry (chapitre 33) détecte en production une dérive soudaine du taux d’erreur ou la compromission d’un serveur sous-jacent, le centre d’opérations AgentOps publie sur le canal prioritaire de l’Agent Directory un avis de révocation signé (*Revocation Record*). En moins de cinq secondes, $\mathbb{I}_{\text{pol}}(a)$ passe à zéro sur toutes les passerelles du groupe : l’agent fautif est isolé et le trafic bascule vers le candidat de rang 2, sans interrompre les sagas en cours.

#### Extrait 6.2 — Manifeste de capacité AGNTCY OASF signé et relié à A2A v1.0

Le manifeste du classificateur douanier de BEL déclare ses compétences, ses localisateurs vers l’Agent Card et SLIM, puis ses modules d’évaluation, de conformité et de provenance.

``` yaml
oasfVersion: "1.0.0"
name: "ca.boreal.bel.customs-harmonized-classifier"
version: "3.1.0"
description: >-
  Spécialiste de classification tarifaire douanière (SH/HS Code) et calcul d'origine
  préférentielle ACEUM/USMCA pour équipements électromécaniques industriels.
authors:
  - "Conformité Douanière & Ingénierie BEL <agentops-bel@boreal.ca>"
createdAt: "2027-02-18T09:30:00Z"

skills:
  - id: "supply_chain/trade_compliance/hs_tariff_classification"
    proficiency: "expert"
  - id: "supply_chain/trade_compliance/usmca_origin_determination"
    proficiency: "expert"

domains:
  - "industrial_manufacturing/heavy_machinery"
  - "cross_border_logistics/north_america_eu"

locators:
  - type: "a2a-agent-card"
    url: "https://gateway.boreal.ca/a2a/bel/customs/agent-card.json"
    digest:
      "sha256:9f44c8e12a08b7d6513e88c247ab19d05c63fe41856f01e23c9914d07b3a2e1c"
  - type: "slim-endpoint"
    uri: "slim://ca.boreal/supply-chain/customs-classifier"

modules:
  - name: "agntcy.oasf.evaluation.metrics"
    data:
      benchmarkSuite: "boreal-customs-eval-2027-q1"
      passHat3Score: 0.984
      p95LatencyMs: 2450
      medianCostPerTaskCad: 0.06

  - name: "agntcy.oasf.governance.compliance"
    data:
      autonomyCeiling: "L3"
      dataResidencyRegions: ["ca-central-1"]
      piiHandling: "PROHIBITED"
      regulatoryClassifications:
        osfiE23Materiality: "NON_APPLICABLE"
        euAiActCategory: "LIMITED_RISK"
      requiredOAuthScopes: ["bel.customs.classify"]

  - name: "agntcy.oasf.security.provenance"
    data:
      ociArtifactRef: "registry.internal.boreal.ca/oasf/bel-customs:3.1.0"
      sigstoreRekorLogIndex: 148920331
      signerIdentity: "spiffe://boreal.ca/ns/cicd/sa/adlc-release-signer"
```

------------------------------------------------------------------------

## 6.10 Transport inter-agents sécurisé à basse latence : SLIM et chiffrement MLS post-quantique

HTTPS suffit aux flux administratifs point à point. Trois contraintes opérationnelles mettent toutefois en échec le modèle requête-réponse HTTP dans les architectures multi-agents denses :

1.  **Sessions collaboratives multipartites** : faire délibérer ou enchérir simultanément cinq agents (diagnostic, stock, douane, transporteur, assureur) sous 150 ms par $N(N-1)$ webhooks HTTP produit une amplification quadratique.
2.  **Traversée des pare-feux IT/OT et des PME** : recevoir des appels HTTP entrants exige d’ouvrir des ports dans les zones industrielles (niveau 3 du modèle Purdue), pratique proscrite en sûreté cyber-physique.
3.  **Rupture du chiffrement aux courtiers intermédiaires** : avec un TLS classique terminé sur chaque proxy ou courtier infonuagique mutualisé, l’infrastructure intermédiaire accède en clair aux offres commerciales et aux secrets industriels.

La couche réseau d’AGNTCY lève ces trois verrous en associant le transport SLIM au chiffrement de groupe IETF MLS (RFC 9420).

### SLIM sur gRPC (HTTP/2 ou WebSocket)

SLIM (*Secure Low-Latency Interactive Messaging*), implémenté en Rust pour une latence déterministe, remplace le routage IP/port par un adressage sémantique hiérarchique (`organisation/namespace/classe-agent/instance-id`), inspiré des réseaux orientés information (ICN). Chaque nœud ne maintient qu’une connexion sortante persistante, sur gRPC en flux (HTTP/2 ou WebSocket), vers le relais le plus proche :

- **Zéro port entrant exposé** : un agent d’usine initie le canal sortant et reçoit les tâches A2A v1.0 encapsulées sans jamais exposer d’adresse IP entrante.
- **Modes unifiés** : requête-réponse, flux de jetons et canaux de publication-abonnement en multidiffusion cohabitent sur la même primitive.

![Architecture de la pile réseau AGNTCY : découverte fédérée OASF / Agent Directory et transport SLIM chiffré de bout en bout par MLS post-quantique.](figures/fig-06-a-2.svg)

### Confidentialité de groupe post-quantique avec IETF MLS (RFC 9420)

Au-dessus du routage SLIM, le protocole *Messaging Layer Security* (MLS, RFC 9420) chiffre les charges utiles de bout en bout entre les agents d’une session et rend les relais intermédiaires aveugles au contenu. Dans sa structure d’arbre binaire à cliquet asymétrique TreeKEM, chaque participant occupe une feuille liée à son identité (SPIFFE SVID ou DID). Lorsqu’un agent externe rejoint une négociation puis la quitte après quatre minutes, l’opération Commit renouvelle le secret d’époque le long du chemin vers la racine en $\mathcal{O}(\log N)$ opérations cryptographiques. Elle garantit la confidentialité persistante et la sécurité post-compromission (PCS).

En 2027, les sessions SLIM/MLS inter-organisations imposent la suite hybride post-quantique X25519MLKEM768, qui combine la courbe elliptique X25519 et l’encapsulation ML-KEM-768 (NIST FIPS 203), avec des signatures ML-DSA (FIPS 204). Cette suite pare les collectes passives de type *Harvest Now, Decrypt Later* sur les secrets industriels qui transitent par Internet. Deux enseignements de déploiement :

- **Surcoût post-quantique négligeable devant l’inférence** : un `KeyPackage` hybride X25519MLKEM768 ajoute environ 1,2 kilooctet à la poignée de main initiale du groupe MLS. L’encapsulation et la décapsulation s’exécutent en moins de 0,4 milliseconde sur un processeur serveur standard, puis un chiffrement symétrique matériel AES-256-GCM tourne à débit filaire. Ce coût est imperceptible devant une inférence de modèle de 300 à 2 000 millisecondes.
- **Pontage d’A2A sur SLIM par démon local et collisions d’époques** : les équipes métiers n’ont pas à réécrire leurs agents. L’agent spécialiste expose localement sur 127.0.0.1 son serveur A2A v1.0 standard; un démon SLIM local gère l’attestation SPIFFE, l’arbre MLS et l’encapsulation JSON-RPC ou gRPC sur HTTP/2, dans des salles d’exécution éphémères détruites dès la clôture de la saga. Conformément à la RFC 9420, le relais SLIM ordonne linéairement les trames Commit concurrentes, sans accès au clair, pour prévenir toute bifurcation d’époque, et il évince les feuilles silencieuses qui retarderaient le renouvellement post-compromission (PCS).

#### Extrait 6.3 — Configuration d’un nœud passerelle SLIM sous MLS hybride post-quantique

Le nœud passerelle SLIM de BEL se connecte en gRPC sur HTTP/2 avec repli sur WebSocket, tient son identité de SPIFFE, impose MLS hybride aux pairs externes et relie un agent A2A local à une route SLIM.

``` yaml
# slim-node-gateway.yaml — Nœud relais/client AGNTCY SLIM durci (Production 2027)
node:
  id: "boreal-bel-mtl-slim-01"
  organization: "ca.boreal"
  namespace: "supply-chain"

transport:
  primaryProtocol: "http2-grpc"
  fallbackProtocol: "websocket"
  upstreamRelays:
    - endpoint: "https://slim-mesh.boreal.ca:443"
      alpn: ["slim-v1"]
      keepAliveIntervalMs: 15000
      maxConcurrentStreams: 512

identity:
  provider: "spiffe-workload-api"
  socketPath: "unix:///run/spire/sockets/agent.sock"
  expectedTrustDomain: "boreal.ca"
  federatedExternalTrust:
    enabled: true
    allowedDidMethods: ["did:wba"]
    policyEngineEndpoint: "http://127.0.0.1:8181/v1/data/boreal/slim/admission"

mlsSecurity:
  enabled: true
  mandatoryForExternalPeers: true
  cipherSuite: "MLS_256_X25519MLKEM768_AES256GCM_SHA384_MLDSA65"
  keyRotationPolicy:
    maxEpochDurationSeconds: 900
    maxMessagesPerEpoch: 5000
    rotateImmediatelyOnMemberLeave: true
  keyPackageLifetimeHours: 24

a2aBridge:
  exposeLocalAgents:
    - localAgentName: "bel-spot-procurement-orchestrator"
      slimRoute: "ca.boreal/supply-chain/procurement-orchestrator"
      upstreamA2aUrl: "http://127.0.0.1:9080/a2a/v1"
```

------------------------------------------------------------------------

## 6.11 Traversée des frontières organisationnelles et fédération multilocataire (ANP)

À l’intérieur de l’entreprise, SPIRE et Microsoft Entra ID procurent une racine de confiance unifiée. Quand un agent achats doit consulter en temps réel les agents de vingt fournisseurs externes indépendants, la direction sécurité n’acceptera pas de fédérer son annuaire interne avec l’extérieur. ANP (*Agent Network Protocol*) répond à ce cas sur l’Internet ouvert des agents (chapitre 7).

### Identités Web décentralisées (did:wba) et DMZ agentique

ANP évite les registres spéculatifs complexes et s’appuie sur la méthode `did:wba` (*Web-Based Agent DID*), conforme à W3C DID Core :

1.  **Ancrage DNS/TLS natif** : l’identifiant `did:wba:b2b-agents.acier-laurentides.ca:sales:rfq-responder` se résout par HTTPS vers `https://b2b-agents.acier-laurentides.ca/sales/rfq-responder/did.json`, liant cryptographiquement les clés publiques de l’agent à la propriété du domaine Web de l’entreprise et à son attestation légale vérifiable (vLEI / GLEIF).
2.  **Négociation de méta-protocole** (encore en brouillon, à réserver aux prototypes selon le chapitre 7) : avant d’ouvrir la tâche A2A v1.0, l’en-tête ANP accorde la version des schémas métiers partagés (ex. UN/CEFACT ou DCSA) et les plafonds de cadence.

| Standard | Fonction dans la pile | Périmètre cible | Identité native | Maturité (2027) |
|:--------------|:--------------------------|:--------------------|:------------------|:-------------------|
| A2A v1.0 *(+ fusion ACP)* | Délégation d’objectifs, états de tâche, artefacts et webhooks | Intra-entreprise et B2B structuré | OAuth 2.1 OBO, mTLS ou DID | Spécification 1.0 stable, protocole par défaut dans l’écosystème ouvert d’origine occidentale (LF / AAIF; sections 6.4 et 6.5); usage en production affirmé sans organisation nommée (section 6.7) |
| AGNTCY OASF + Directory | Taxonomie des compétences, provenance OCI et index DHT | Flottes \> 15 agents et consortiums | Sigstore / SPIFFE / DID | Annuaire en version 1.0, à évaluer (Linux Foundation) |
| AGNTCY SLIM + MLS | Messagerie gRPC sans port entrant et chiffrement de bout en bout post-quantique | Essaims en temps réel, sites IT/OT, salles B2B | Feuilles TreeKEM (SPIFFE / `did:wba`) | À l’essai : SLIM en brouillon IETF individuel; MLS normalisé (RFC 9420) |
| ANP (`did:wba`) | Identité décentralisée sur DNS/TLS et découverte Web ouverte | Écosystèmes B2B multi-fournisseurs | W3C DID (`did:wba`) + vLEI | À l’essai, derrière une DMZ |

En production, aucun agent interne n’est exposé directement au réseau externe. Toute interaction ANP/A2A franchit une DMZ agentique, qui vérifie le `did:wba` et le vLEI, rejette tout champ de texte libre non borné pour bloquer l’injection indirecte (OWASP ASI01), applique des quotas stricts par partenaire (isolation des locataires) et marque le contexte interne avec `external_partner_origin = true`.

La passerelle réécrit aussi les en-têtes de télémétrie distribuée (W3C Trace Context `traceparent` / `tracestate`). Elle tient une table de corrélation locale avec l’identifiant de trace externe, pour faciliter le diagnostic conjoint des incidents B2B, et retire tout attribut interne susceptible de révéler aux tiers la topologie des microservices ou les noms des modèles utilisés en interne.

#### Extrait 6.4 — Document d’identité ANP (did:wba) et politique Cedar d’admission DMZ

Le `did.json` d’un répondeur de demandes de prix publie sa clé d’authentification et ses points d’accès. La politique Cedar de la DMZ agentique admet la réponse d’un fournisseur invité et authentifié, en JSON validé et sans instruction libre, et interdit l’accès aux ressources classifiées.

``` json
{
  "_endpoint": "GET https://b2b-agents.acier-laurentides.ca/sales/rfq-responder/did.json",
  "@context": ["https://www.w3.org/ns/did/v1", "https://w3id.org/security/suites/jws-2020/v1"],
  "id": "did:wba:b2b-agents.acier-laurentides.ca:sales:rfq-responder",
  "verificationMethod": [{
    "id": "did:wba:b2b-agents.acier-laurentides.ca:sales:rfq-responder#key-auth-1",
    "type": "JsonWebKey2020",
    "controller": "did:wba:b2b-agents.acier-laurentides.ca:sales:rfq-responder",
    "publicKeyJwk": { "kty": "OKP", "crv": "Ed25519", "x": "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo" }
  }],
  "authentication": ["did:wba:b2b-agents.acier-laurentides.ca:sales:rfq-responder#key-auth-1"],
  "service": [
    {
      "id": "#a2a",
      "type": "A2AAgentEndpoint",
      "serviceEndpoint": "https://b2b-agents.acier-laurentides.ca/a2a/v1/rfq-responder"
    },
    {
      "id": "#vlei",
      "type": "LegalEntityVerifiableCredential",
      "serviceEndpoint": "https://b2b-agents.acier-laurentides.ca/vc/gleif-vlei.vc.json"
    }
  ]
}
```

``` cedar
// Politique Cedar exécutée en coupure sur la DMZ Agentique du Groupe Boréal
permit (
  principal is ExternalAgent,
  action == Action::"a2a:SubmitTaskResponse",
  resource is BorealProcurementSession
)
when {
  principal.didMethod == "did:wba" &&
  principal.hasValidGleifVlei == true &&
  principal.erpVendorStatus == "APPROVED_ACTIVE" &&
  resource.invitedSuppliers.contains(principal.did) &&
  context.payloadMimeType == "application/json" &&
  context.schemaValidationPassed == true &&
  context.containsFreeformInstructions == false
};

forbid (principal is ExternalAgent, action, resource)
when {
  [
    "INTERNAL_CONFIDENTIAL",
    "BSIF_REGULATED",
    "PII_LOI25"
  ].contains(resource.dataClassification)
};
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Chaîne logistique mondiale — Fédération d'annuaires d'agents entre donneurs d'ordres et transporteurs**
:::

Lors d’une fermeture portuaire imprévue ou d’un arrêt d’écluse sur la Voie maritime du Saint-Laurent, les messages EDI X12 / EDIFACT atteignent leur limite : conçus pour exécuter des contrats-cadres figés, ils ne savent pas négocier à la volée un réacheminement multimodal conditionnel.

En 2027, les chargeurs et transitaires combinent OASF, ANP et SLIM/MLS en trois temps : (1) sélection, dans un Agent Directory fédéré, des transporteurs qui disposent des certifications requises (`corridor:rotterdam-montreal`, `hazmat:class-9`), sans exposer leurs tarifs; (2) ouverture de canaux A2A v1.0 isolés sous chiffrement MLS post-quantique, qu’aucun courtier infonuagique ni concurrent ne peut lire pour connaître les cotations spot; (3) échange de connaissements électroniques (*eBL*) sous forme d’artefacts typés conformes aux schémas DCSA, ce qui ramène le réacheminement complet de 38 heures à 14 minutes.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur Financier & Assurances — Muraille de Chine informationnelle inter-filiales sous BSIF E-23 et Loi 25**
:::

Dans un groupe qui détient à la fois des filiales commerciales et une institution financière supervisée, l’interopérabilité agentique ne doit pas violer les murailles de Chine (*Information Barriers*). La Loi 25 québécoise interdit le partage interne de renseignements personnels hors de la finalité consentie, et la ligne directrice BSIF E-23 (1er mai 2027) impose une frontière d’auditabilité autour des modèles de risque.

A2A v1.0 matérialise ici le patron d’adjudication à divulgation minimale. Interrogé par la filiale industrielle, l’agent de la filiale d’assurance n’expose ni le dossier financier ni l’historique de sinistralité; son `outputSchema` ne renvoie qu’un verdict signé (APPROVED / ESCALATE), le plafond couvert en dollars et un jeton d’autorisation opaque. La donnée sensible reste confinée dans son enclave réglementaire, et le processus transversal demeure automatisé.
::::

------------------------------------------------------------------------

## 6.12 Application au fil rouge : interconnexion horizontale chez Groupe Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Maillage horizontal A2A v1.0 et SLIM entre BSN, BCA et BEL**
:::

**Impasse initiale (fin T4 2026)** : Une fois leurs premiers serveurs MCP bâtis localement, les équipes de BSN, BCA et BEL avaient tenté de relier leurs agents par des webhooks REST ad hoc. Résultat : deux semaines d’adaptation à chaque nouveau flux, des doublons de réservation lorsque l’IBM i (AS/400) de BCA mettait 95 secondes à analyser un avenant complexe, et le refus de la sécurité industrielle d’ouvrir des ports HTTPS entrants vers les quatre usines BEL.

**Architecture déployée (T1–T2 2027)** :

1.  **Catalogue AGNTCY OASF et Agent Cards certifiées** : les 18 agents spécialistes du groupe sont publiés en artefacts OCI signés par Cosign (Extrait 6.2). agentgateway vérifie chaque signature JWS avant le routage et a bloqué en 4 ms un faux agent injecté lors d’un test d’intrusion d’une équipe rouge.
2.  **Boucle `INPUT_REQUIRED` auto-résolue entre BCA et BSN** : dans 22 % des dossiers de maintenance préventive, l’*Agent Garantie* de BCA réclame la preuve de lubrification des six derniers mois par l’état `INPUT_REQUIRED` (Extrait 6.1). Temporal capte le webhook signé, récupère l’empreinte certifiée auprès du spécialiste télémétrie de BSN et relance le même `taskId`, sans intervention humaine.
3.  **Tunnels sortants SLIM + MLS en usine et DMZ ANP fournisseurs** : les usines BEL ne maintiennent qu’une liaison sortante gRPC (SLIM), chiffrée en MLS X25519MLKEM768. En parallèle, la DMZ agentique relie par `did:wba` 25 fournisseurs nord-américains pré-qualifiés (Extrait 6.4) pour les demandes de prix d’urgence, en JSON strict.

**Résultats mesurés à 90 jours** :

- **Intégration d’un nouvel agent spécialiste au maillage** : réduite de 6 semaines à 1,5 jour.
- **Dossiers incomplets (`INPUT_REQUIRED`) résolus sans humain** : 89 % traités en moins de 6 secondes (contre 19 heures de courriels internes auparavant).
- **Consultation spot de 3 fournisseurs externes** : ramenée de 28 heures à 4 minutes 10 secondes, avec zéro port entrant ouvert sur les périmètres d’usine.
::::

------------------------------------------------------------------------

## 6.13 Décision d’architecture et liste de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-006 — Utilisation d'A2A v1.0 et d'Agent Cards signées pour toute délégation inter-domaines**
:::

- **Statut** : Acceptée \| Périmètre : Fabrique Agentique d’Entreprise & DMZ B2B \| Révision : Semestrielle
- **Contexte** : Coordonner des agents autonomes répartis entre divisions réglementées, usines IT/OT et partenaires externes exige un protocole horizontal qui respecte l’opacité interne des pairs, les cycles longs et la traversée sécurisée des frontières réseau, sans dépendance à un éditeur unique.
- **Options évaluées** :
  1.  *Agents exposés comme outils MCP distants* : Rejetée, car elle bloque les contextes sur les cycles longs et prive l’architecture d’une machine à états asynchrone (`INPUT_REQUIRED`, webhooks).
  2.  *Bus propriétaire mono-éditeur SaaS* : Rejetée, car il verrouille le contrat et convient mal aux systèmes patrimoniaux et industriels.
  3.  *Standardisation A2A v1.0 + AGNTCY OASF / Directory + SLIM/MLS ciblé* : Retenue, pour sa gouvernance ouverte Linux Foundation, sa gestion native du flux et des notifications asynchrones, sa découverte signée et son chiffrement post-quantique.
- **Décision** :
  1.  Toute délégation inter-domaines ou B2B emprunte A2A v1.0, munie d’une `ActionEnvelope` (`sagaId`, clé d’idempotence, budget, `maxRemainingHops`).
  2.  Chaque Agent Card porte une signature JWS validée à la passerelle et correspond à un manifeste OASF signé dans l’Agent Directory.
  3.  Toute tâche dont la durée P95 dépasse 60 secondes utilise obligatoirement le mode non bloquant, avec des notifications poussées par webhook signé, reliées au moteur durable. Cette règle va au-delà de ce que retient l’exposé : la grille de décision garde les notifications poussées par défaut et admet l’interrogation périodique si le client ne peut pas recevoir d’appels entrants.
  4.  Les flux vers les sites IT/OT et les sessions multipartites B2B passent par SLIM sous chiffrement IETF MLS (X25519MLKEM768) et traversent la DMZ agentique (ANP `did:wba` + Cedar).
- **Conséquences** :
  - *Positives* : Découplage des équipes, remplacement sans interruption des modèles sous-jacents, résilience aux coupures longues et confidentialité post-quantique de bout en bout.
  - *Négatives / Coûts assumés* : Exploitation de la chaîne de signature Sigstore/JWS, gouvernance des schémas JSON inter-domaines et maintien des relais SLIM en DMZ.
- **Condition de révision** : Publication d’une révision majeure d’A2A ou convergence normative W3C/AAIF sur l’identité d’agents B2B.
::::

### Liste de contrôle de mise en production

Avant d’homologuer une interconnexion horizontale inter-domaines ou B2B, vérifiez les huit points suivants :

1.  **Authenticité de l’Agent Card** : Le fichier `/.well-known/agent-card.json` comporte-t-il une signature JWS canonique vérifiée en coupure, et réserve-t-il ses compétences sensibles à la carte étendue (`GetExtendedAgentCard`) ?
2.  **Provenance OASF certifiée** : Le manifeste OASF est-il signé dans le registre OCI par Sigstore/Cosign, avec des métriques $\text{pass}^k$, de coût et de latence P95 à jour ?
3.  **Aucune interrogation périodique sur les tâches longues** : Toute délégation de plus de 60 secondes utilise-t-elle des notifications `taskPushNotificationConfig` qui réveillent un état durable, plutôt qu’une boucle d’interrogation `GetTask` ? Cette exigence va au-delà de ce que retient l’exposé : la grille de décision admet l’interrogation périodique si le client ne peut pas recevoir d’appels entrants.
4.  **Durcissement anti-SSRF des webhooks** : Les URL de rappel sont-elles restreintes par liste blanche d’identité, protégées contre les adresses IP internes privées et munies d’un `nonce` horodaté et signé ?
5.  **Schémas JSON fermés** : Les parties de données structurées et les artefacts imposent-ils `additionalProperties: false` et le rejet de toute prose d’instruction libre sur les flux externes (OWASP ASI01) ?
6.  **Compteur de sauts déterministe** : La passerelle décrémente-t-elle `maxRemainingHops` à chaque appel A2A v1.0 et rejette-t-elle l’appel à zéro ?
7.  **Chiffrement MLS post-quantique** : Les sessions de groupe SLIM, ou celles qui traversent un courtier tiers, activent-elles X25519MLKEM768 avec une rotation immédiate des clés au départ d’un membre ?
8.  **Terminaison en DMZ agentique (ANP)** : Les agents externes `did:wba` sont-ils authentifiés par une attestation d’entité légale (vLEI/ERP), isolés par des quotas dédiés et privés de tout accès aux données réglementées ?
