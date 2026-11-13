## Mise en œuvre — Interfaces humain-agent, multimodalité temps réel et protocoles transactionnels {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : une fabrique agentique bien orchestrée en arrière-plan (MCP + A2A v1.0) échoue en bout de chaîne si elle restitue ses arbitrages dans une boîte de clavardage, oblige un technicien ganté à taper sur un écran en atelier bruyant, ou confie une carte bancaire partagée à un modèle probabiliste pour payer un fournisseur externe. L’interface humaine et le règlement financier concentrent le risque de complaisance cognitive (OWASP ASI09) et de fraude transactionnelle.
- **Décisions architecturales structurantes** :
  1.  *Irréversible côté sécurité client* : interdire aux agents d’émettre du HTML ou du JavaScript exécutable vers le navigateur; imposer AG-UI avec des descripteurs déclaratifs A2UI, rendus par un catalogue local de composants natifs homologués.
  2.  *Structurante pour le terrain industriel* : déployer WebRTC en duplex intégral (UDP/SRTP) plutôt que des flux TCP pour toute assistance vocale et visuelle en temps réel, avec interruption sous 200 ms et troncature exacte du contexte serveur.
  3.  *Obligatoire pour l’autonomie financière* : proscrire les moyens de paiement statiques partagés au profit de mandats vérifiables AP2 (Checkout Mandate et Payment Mandate, ouverts ou fermés, au format SD-JWT selon la section 10.2, signés via FIDO2 / WebAuthn) et du règlement programmable HTTP 402 (x402).
- **Indicateurs de gouvernance associés** : délai médian d’arbitrage humain éclairé en mode humain sur la boucle (HOTL) (\< 30 s), latence voix-à-voix P95 (\< 450 ms), interruption (\< 200 ms), et 100 % des paiements agentiques couverts par une preuve tripartite (AP2 + Cedar + reçu x402/ERP).
::::

## 10.9 Interfaces réactives pilotées par événements : AG-UI, différentiels d’état, A2UI et MCP-UI

Le flux continu de texte Markdown s’est imposé par défaut comme interface des premiers copilotes. En production d’entreprise en 2027 (souscription d’assurance, tour de contrôle logistique, supervision HOTL), il épuise l’opérateur, qui doit parcourir quarante lignes générées pour repérer une anomalie tarifaire, encourage l’approbation réflexe (OWASP ASI09) et empêche la co-édition structurée d’un dossier métier.

L’architecture sépare le transport bidirectionnel d’événements et d’état (AG-UI) de la spécification déclarative des vues (A2UI et MCP-UI).

### AG-UI (*Agent-User Interaction Protocol*) : synchronisation d’état par JSON Patch

AG-UI est né autour de CopilotKit en 2025, et les moteurs d’orchestration l’ont largement adopté (LangGraph, Microsoft Agent Framework, CrewAI, Mastra). Il normalise la liaison entre l’environnement d’exécution agentique et le client frontal, sur SSE ou WebSockets, autour de quatre familles principales d’événements :

1.  **Cycle d’exécution** (`RUN_STARTED`, `STEP_STARTED`, `STEP_FINISHED`, `RUN_FINISHED`, `RUN_ERROR`) : il expose l’avancement exact de la saga sans divulguer de chaîne de pensée interne sensible.
2.  **Flux de messages** (`TEXT_MESSAGE_START`, `TEXT_MESSAGE_CONTENT`, `TEXT_MESSAGE_END`), corrélés par `messageId`.
3.  **Appels d’outils visibles et frontaux** (`TOOL_CALL_START`, `TOOL_CALL_ARGS`, `TOOL_CALL_END`) : ils permettent aussi d’invoquer une action locale du poste client, comme une invite matérielle WebAuthn.
4.  **État partagé par différentiels (`STATE_SNAPSHOT` et `STATE_DELTA`)** : après un instantané initial, l’agent n’émet plus que des opérations JSON Patch (RFC 6902) atomiques (`replace`, `add`, `remove`). Symétriquement, toute modification de champ par l’opérateur remonte à l’agent sous forme de différentiel typé : l’humain et la machine travaillent sur le même modèle d’état.

### A2UI et MCP-UI : interfaces génératives sans exécution de code arbitraire

Deux standards permettent à l’agent de composer l’écran adapté au contexte sans faille XSS ni exfiltration de session :

- **MCP-UI** : quand un serveur MCP tiers fournit une visualisation spécialisée absente du système de design interne, MCP-UI l’isole dans une iframe sans origine partagée : `sandbox="allow-scripts"` sans `allow-same-origin`, qui interdit toute évasion du confinement, et directive CSP `connect-src 'none'`. Seul un canal de messages filtrés la relie au client.
- **A2UI (*Agent-to-User Interface*)** : porté par Google fin 2025 pour les interfaces critiques natives, il applique une règle : des données, jamais du code. L’agent transmet une liste plate d’adjacence JSON qui référence uniquement des composants abstraits, liés par JSON Pointer à l’état AG-UI. Le client instancie ses propres composants homologués (React, Angular, Flutter), ce qui garantit la charte graphique et l’accessibilité WCAG, et écarte l’injection de script.

Deux raisons d’ingénierie justifient ce choix en production :

- **Graphe plat d’adjacence et diffusion en continu** : un arbre JSON profondément imbriqué n’est valide qu’une fois reçues toutes ses accolades fermantes. La liste plate d’objets composants d’A2UI permet au poste client de rendre le squelette de la carte dès les cinquante premières millisecondes, puis d’alimenter chaque sous-composant à mesure que les jetons arrivent.
- **Conflits d’édition concurrents (opération `test` de la RFC 6902)** : quand l’humain et l’agent modifient en même temps le même dossier, un `STATE_DELTA` retardé par le réseau risque d’écraser la saisie manuelle de l’opérateur. Chaque lot JSON Patch s’ouvre donc par une opération atomique `{"op": "test", "path": "/_revision", "value": 14}` : le magasin d’état rejette toute mutation obsolète et force une réconciliation explicite.

| Paradigme d’interface | Sécurité client (XSS / ASI01) | Accessibilité et cohérence de l’interface | Co-édition d’état | Usage cible en entreprise (2027) |
|:-----------------|:------------------|:--------------------|:--------------------|:-----------------------|
| Clavardage Markdown brut | Moyenne (liens et images forgés) | Faible sur les dossiers métiers denses | Nulle | Recherche documentaire simple (L0/L1) |
| Génération HTML/JS libre | Critique (inacceptable) | Aléatoire | Fragile | Proscrit en production |
| MCP-UI (iframe isolée) | Élevée sous `sandbox` strict | Propre à l’éditeur tiers | Par pont d’événements | Composants externes spécialisés (CAO, cartes) |
| AG-UI + catalogue A2UI | Maximale (aucun code reçu) | Native (système de design interne) | Bidirectionnelle (RFC 6902) | Postes opérateurs, consoles HOTL, mobile |

#### Extrait 10.1 — Flux AG-UI (STATE_DELTA) et descripteur déclaratif A2UI pour une escalade HOTL

Le premier événement met à jour l’état d’un dossier sous contrôle de révision; le second décrit le panneau de décision que le client instancie.

``` json
[{
  "_comment": "1. Événement AG-UI : mise à jour différentielle (JSON Patch RFC 6902)",
  "type": "STATE_DELTA",
  "threadId": "thr-hotl-bca-88412",
  "runId": "run-99201",
  "delta": [
    { "op": "test", "path": "/_revision", "value": 14 },
    { "op": "replace", "path": "/_revision", "value": 15 },
    { "op": "replace", "path": "/claim/status", "value": "AWAITING_UNDERWRITER_HOTL" },
    { "op": "replace", "path": "/claim/estimatedCostCad", "value": 6420.00 },
    { "op": "add", "path": "/escalationReasons/0", "value": "Dépassement du plafond L3 (5 000 $ CAD)" }
  ]
},
{
  "_comment": "2. Événement A2UI : liste plate d'adjacence instanciée par React",
  "type": "CUSTOM",
  "name": "a2ui.surfaceUpdate",
  "value": {
    "surfaceId": "hotl-decision-panel",
    "catalogId": "https://ui.boreal.ca/catalogs/bca-underwriting-v2.json",
    "rootComponentId": "card-root",
    "components": [
      {
        "id": "card-root",
        "component": "BorealEscalationCard",
        "props": { "severity": "warning", "title": "Escalade HOTL — Compresseur BOR-CMP-90441" },
        "children": ["diff-evidence", "cap-adjuster", "fido-action-bar"]
      },
      {
        "id": "diff-evidence",
        "component": "ContradictionDiffTable",
        "dataBinding": { "rowsPath": "/evidenceComparison", "ceilingPath": "/policy/l3CeilingCad" }
      },
      {
        "id": "cap-adjuster",
        "component": "CurrencyBoundInput",
        "props": { "label": "Plafond approuvé (CAD)", "min": 0, "max": 15000 },
        "twoWayBinding": "/claim/approvedCapCad"
      },
      {
        "id": "fido-action-bar",
        "component": "WebAuthnMandateBar",
        "props": { "approveActionId": "SIGN_AP2_CART", "requireHardwarePasskey": true }
      }
    ]
  }
}]
```

---

## 10.10 Agents vocaux et visuels temps réel : WebRTC en duplex intégral et gestion de l’interruption

En usine d’usinage, en entrepôt frigorifique ou lors d’une intervention sur turbine, le technicien porte des gants isolants, tient un outil de mesure et travaille sous 85 dB(A) de bruit mécanique. L’écran tactile devient impraticable : l’audio mains libres et le flux caméra en temps réel deviennent le canal principal de la fabrique agentique.

### WebRTC plutôt que WebSockets sur TCP

Transporter de la voix interactive sur WebSockets (TCP) échoue dès qu’un opérateur se déplace entre deux bornes Wi-Fi 6E ou 5G privée : une perte radio de 2 % bloque la file d’attente TCP (blocage en tête de file), l’audio se fige pendant près d’une seconde, puis une rafale incompréhensible arrive d’un coup.

Une architecture terrain de production repose donc sur WebRTC en duplex intégral, terminé sur une passerelle média de périphérie (SFU) :

- **Audio Opus sur UDP / SRTP** (trames de 20 ms, correction d’erreur FEC intégrée au flux) : il absorbe la gigue radio sans interruption.
- **Piste vidéo sobre** (1 à 2 trames/s à la demande) : elle suffit pour lire une plaque signalétique ou inspecter un bornier sans saturer les GPU.
- **DataChannel SCTP couplé** : il synchronise en même temps l’affichage AG-UI/A2UI sur une tablette posée à proximité.

### Budget de latence et interruption

La fluidité conversationnelle exige un délai inférieur à 450 millisecondes entre la fin sémantique du tour humain et le premier échantillon sonore de réponse :

$$L_{\text{voix}} = L_{\text{net}} + L_{\text{VAD/EOU}} + L_{\text{inf}} + L_{\text{audio}} \le 450\text{ ms}$$

Dans cette décomposition, $L_{\text{net}}$ couvre le transport aller-retour UDP/SRTP, $L_{\text{VAD/EOU}}$ la détection de fin de tour, $L_{\text{inf}}$ le temps au premier jeton du modèle et $L_{\text{audio}}$ la synthèse vocale. Les modèles parole à parole (S2S) natifs abaissent ce délai vers 280 ms, mais les chaînes cascadées en diffusion continue (VAD neuronale + STT + SLM + TTS basse latence, environ 390 ms) restent privilégiées en environnement industriel réglementé : leur étape texte intermédiaire permet un filtrage déterministe du vocabulaire de sûreté et produit une transcription d’audit exacte.

L’invariant critique est l’interruption. Lorsque le technicien coupe la parole à l’agent (« *Stop, la vanne est grippée !* »), le détecteur vocal, qui filtre les bruits d’impact mécanique, doit purger le tampon audio du client en moins de 200 ms, interrompre la synthèse serveur par le `DataChannel` et tronquer l’historique conversationnel de l’agent au mot exact réellement entendu, afin d’éviter tout décalage dangereux sur les consignes non prononcées.

Le déploiement industriel exige en plus de soigner la détection sémantique de fin de tour (EOU) et la traversée réseau :

- **Coupures prématurées sur hésitation technique** : un détecteur acoustique naïf qui déclenche la réponse après 350 ms de silence coupe la parole à un technicien qui lit un manomètre (« *La pression d’huile affiche… quarante-deux virgule… huit bars* »). Un micro-modèle syntaxique EOU léger (moins de 150 millions de paramètres, latence de 12 ms sur CPU) évalue si l’énoncé en cours est grammaticalement achevé avant d’autoriser l’agent à prendre la parole, ce qui réduit de 70 % les collisions vocales.
- **Relais TURN d’entreprise sur port 443** : sur les réseaux d’usine segmentés, où l’UDP direct est parfois filtré entre zones, des serveurs TURN internes dédiés, avec repli DTLS/SRTP, garantissent un établissement d’appel ICE en moins de 300 ms sans acheminer le flux média par un nuage public tiers.

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Terrain industriel et conformité — transparence multimodale (EU AI Act, art. 50) et biométrie vocale (Loi 25)**
:::

Les interfaces vocales et visuelles activent deux exigences légales en 2027 :

1.  **EU AI Act (articles 50 et 5)** : l’article 50, actif depuis août 2026, impose d’informer clairement l’utilisateur dès l’ouverture d’un canal vocal synthétique. L’article 5(1)(f) interdit les systèmes qui infèrent les émotions des employés sur le lieu de travail, hors sûreté médicale ou fatigue critique : tout module d’analyse émotionnelle de la voix est exclu.
2.  **Biométrie sous la Loi 25 et la LCCJTI au Québec** : identifier un employé par empreinte vocale sur WebRTC constitue une base biométrique, qui exige un consentement exprès, une ÉFVP et une déclaration à la CAI 60 jours avant le déploiement. L’authentification se fait plutôt par badge matériel FIDO2/NFC.
::::

---

## 10.11 Commerce agentique : mandats vérifiables AP2 (FIDO, SD-JWT) et règlement HTTP x402

De nombreux flux de travail agentiques débouchent sur un engagement financier : achat unitaire d’une donnée douanière ou météo haute précision, réservation de fret ponctuel ou commande d’une pièce critique.

![Architecture convergente du dernier kilomètre : interfaces réactives AG-UI / A2UI et WebRTC d’un côté, chaîne d’autorisation AP2 et règlement HTTP x402 de l’autre.](figures/fig-10-a-1.svg)

Une carte d’entreprise partagée confiée à un agent viole la non-répudiation : en cas d’hallucination ou d’injection indirecte, aucune preuve cryptographique ne relie le décaissement à une intention approuvée. AP2 (section 10.2) et x402 (section 10.5) ferment cette brèche.

### AP2 (*Agent Payments Protocol*) : mandats ouverts et fermés

AP2, publié par Google, définit dans sa v0.2 un Checkout Mandate (le contenu de l’achat) et un Payment Mandate (l’autorisation de payer), chacun ouvert ou fermé, au format SD-JWT (section 10.2). L’exposé retient pour leur approbation une surface de confiance non agentique et une validation en code déterministe; l’exigence d’une signature matérielle (passkey FIDO2 ou HSM) va au-delà. La mise en œuvre repose sur les deux parcours de la v0.2 :

1.  **Parcours avec présence humaine (mandats fermés, validation HOTL)** : l’approbateur signe via WebAuthn le hachage SHA-256 exact du panier (articles, quantités, montant, devise et DID marchand), ce qui rend impossible toute altération ultérieure par l’agent.
2.  **Parcours sans présence humaine (mandats ouverts, autonomie L3/L4)** : délégation préalable à contraintes déterministes (plafond unitaire et journalier, catégories UNSPSC, liste blanche de DID marchands et expiration TTL), qui permet aux agents d’acheter sans attente humaine dans un cadre borné.

Cette architecture ne règle pas la question de l’attribution de responsabilité en cas de litige. Mandats et reçus donnent de la transaction une image non répudiable, utilisable comme preuve une fois les vérifications réussies; mais AP2 exclut expressément la résolution des litiges et ne répartit pas la responsabilité entre les rôles (sections 10.2 et 10.7). La preuve existe; la règle qui dit quoi en faire n’y est pas. La mesure minimale retenue par l’exposé est de verser mandats et reçus à la piste d’audit (section 10.7).

### Règlement programmable x402 (HTTP 402 Payment Required)

Le mécanisme de l’échange HTTP 402 est décrit à la section 10.5. x402 est un protocole distinct d’AP2 (sections 10.1 et 10.5) : un mandat AP2 peut porter l’autorisation et x402 le règlement, puisqu’AP2 se déclare indépendant de l’instrument. Le dépôt d’origine de x402, chez Coinbase, a été transféré sous une x402 Foundation (section 10.5). x402 permet à l’agent de payer à la requête une API externe ou un serveur MCP marchand distant sur Streamable HTTP. Entre le défi 402 et la relance, la passerelle lit `PAYMENT-REQUIRED` (tarif exact, actif, bénéficiaire) et vérifie par Cedar, sur agentgateway, que l’offre respecte le mandat ouvert AP2 actif. Elle relance ensuite avec `PAYMENT-SIGNATURE`; un facilitateur agréé compense le paiement et la réponse 200 OK porte `PAYMENT-RESPONSE` (Extrait 10.3).

Le cas limite est celui d’un règlement compensé alors que le serveur marchand échoue (HTTP 502/504) avant de livrer la charge utile. L’exposé ne décrit pas de garantie contre ce cas dans x402, dont les pages lues ne disent rien du remboursement, du litige ni de l’identité du payeur (section 10.5) : c’est ici la mise en œuvre de la passerelle qui la porte. `PAYMENT-SIGNATURE` lie alors cryptographiquement l’`Idempotency-Key` et le hachage SHA-256 de la requête : toute relance présente la preuve du débit déjà honoré et récupère la réponse mise en cache, sans double facturation. Les achats de montant élevé privilégient une pré-autorisation à capture conditionnelle.

| Rail transactionnel | Friction d’ouverture | Contrôle granulaire par panier | Délai et frais | Cas d’usage cible (2027) |
|:-------------------|:------------------|:---------------------|:-----------------|:-----------------------|
| Carte virtuelle partagée | Faible | Nul (plafond global aveugle) | Temps réel; 1,5–2,9 % | Déconseillé pour agents autonomes |
| Bon de commande EDI / ERP | Très lourde (semaines) | Élevé (rapprochement 3-voies) | Jours (ACH / virement) | Contrats cadres récurrents (\> 10 000 \$ CAD) |
| AP2 sur rails bancaires / cartes | Modérée | Maximal (mandats AP2 ouverts ou fermés, FIDO2) | Secondes; litiges hors du champ d’AP2 (section 10.2) | Achats ponctuels interentreprises d’équipements et de fret |
| AP2 + HTTP x402 | Nulle (aucun compte préalable) | Maximal (mandat AP2 + coupe-circuit) | \< 250 ms; \< 0,001 \$ | Micropaiements d’API et données à l’acte |

#### Extrait 10.2 — Intent Mandate et Cart Mandate AP2, vocabulaire initial de 2025 (W3C VC 2.0 + assertion FIDO2)

L’Intent Mandate de mars 2027 borne les achats de l’orchestrateur BEL : montants, catégories UNSPSC et marchands autorisés. L’extrait suit le vocabulaire initial d’AP2 (2025) : un mandat nommé Intent Mandate, au format W3C VC 2.0; pour AP2 v0.2, l’exposé indique à la place un Checkout Mandate et un Payment Mandate, chacun ouvert ou fermé, au format SD-JWT (section 10.2).

``` json
{
  "@context": ["https://www.w3.org/ns/credentials/v2", "https://schemas.agentpayments.org/ap2/v1"],
  "id": "urn:uuid:ap2-intent-boreal-bel-2027-0391",
  "type": ["VerifiableCredential", "AP2IntentMandate"],
  "issuer": "did:wba:boreal.ca:treasury:procurement-authority",
  "validFrom": "2027-03-01T00:00:00Z",
  "validUntil": "2027-03-31T23:59:59Z",
  "credentialSubject": {
    "delegatedAgent": "spiffe://boreal.ca/ns/bel/sa/spot-procurement-orchestrator",
    "mandateClass": "HUMAN_NOT_PRESENT_BOUNDED",
    "constraints": {
      "currency": "CAD",
      "maxSingleTransactionAmount": "2500.00",
      "maxDailyCumulativeAmount": "7500.00",
      "allowedUnspscCategories": ["78101800", "81141601"],
      "allowedMerchantDids": [
        "did:wba:b2b-agents.acier-laurentides.ca:sales:rfq-responder",
        "did:wba:api.customs-tariffs-na.ca:x402:gateway"
      ]
    },
    "cartMandateBindingTemplate": {
      "requiredDigestAlgorithm": "SHA-256",
      "exampleLockedCartDigest":
      "sha256:4e91b8c02d77a6f315c48b206d93e7a158c04f2b76d19a3890e82d3f11a04c92"
    }
  },
  "proof": {
    "type": "DataIntegrityProof",
    "cryptosuite": "ecdsa-rdfc-2019",
    "verificationMethod": "did:wba:boreal.ca:treasury:proc#fido2-hsm-key-04",
    "proofPurpose": "assertionMethod",
    "fido2AuthenticatorData": "SZYN5YgOjGh0NBcPZHZgW4_krrmihjLHmVzzuoMdl2MFAAAAAQ...",
    "proofValue": "z3FXQjecWufY46kLp2mN8qR9vT1xW"
  }
}
```

#### Extrait 10.3 — Séquence HTTP 402 (x402) couplée à la vérification du mandat AP2

Une vérification tarifaire douanière à 0,04 USD : défi 402, relance par la passerelle après contrôle du mandat, puis reçu. L’extrait montre un montage de mise en œuvre, où la passerelle contrôle le mandat AP2 avant la relance et où le reçu est qualifié d’immuable; l’exposé retient qu’AP2 et x402 sont des protocoles distincts, que les pages x402 lues ne décrivent aucune autorisation distincte du paiement et que le serveur sert la ressource avec `PAYMENT-RESPONSE` après règlement (sections 10.1 et 10.5).

``` http
### 1. Requête initiale de l'agent vers un service externe de décisions tarifaires douanières
POST /v2/hs-classification/ruling-lookup HTTP/1.1
Host: api.customs-tariffs-na.ca
Content-Type: application/json

{"componentSpec": "Rotor haute pression Inconel 718", "originCountry": "US", "destCountry": "CA"}

### 2. Défi tarifaire retourné par le serveur marchand (0,04 USD à l'acte)
HTTP/1.1 402 Payment Required
Content-Type: application/problem+json
PAYMENT-REQUIRED: eyJ4NDAyVmVyc2lvbiI6Miwic2NoZW1lIjoiZXhhY3QiLCJhbW91bnQi...

{"title": "Paiement x402 requis", "amount": "0.04 USD", "expiresAt": "2027-03-14T14:25:00Z"}

### 3. Relance par agentgateway après contrôle Cedar de l'Intent Mandate AP2 et signature HSM
POST /v2/hs-classification/ruling-lookup HTTP/1.1
Host: api.customs-tariffs-na.ca
Content-Type: application/json
Idempotency-Key: x402-saga-088412-step-ruling
PAYMENT-SIGNATURE: eyJ4NDAyVmVyc2lvbiI6MiwiYXAyTWFuZGF0ZVJlZiI6InVybjp1dWlk...

{"componentSpec": "Rotor haute pression Inconel 718", "originCountry": "US", "destCountry": "CA"}

### 4. Règlement atomique via facilitateur agréé, réponse métier et reçu comptable immuable
HTTP/1.1 200 OK
Content-Type: application/json
PAYMENT-RESPONSE: eyJzZXR0bGVkIjp0cnVlLCJ0eEhhc2giOiIweDRmOGIyYzE5Li4uIn0=

{"hsCode": "8414.90.41.00", "mfnDutyRate": 0.0, "usmcaEligible": true, "rulingRef": "CBSA-2026-8812"}
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Commerce interentreprises et technologies financières — encadrement cryptographique des micropaiements d’API et des achats ponctuels**
:::

L’homologation d’AP2 et de x402 par une direction financière exige trois verrous en passerelle sortante :

1.  **Ségrégation des clés et criblage LCB-FT (KYT)** : aucun conteneur d’agent ne détient de clé de signature financière. Cette règle va au-delà de ce que retient l’exposé : en parcours sans présence humaine, l’agent signe lui-même les mandats fermés avec sa propre clé, publiée dans la revendication `cnf` du mandat ouvert (section 10.2). Seul le module trésorerie d’agentgateway signe `PAYMENT-SIGNATURE`, après filtrage en temps réel des listes de sanctions (OFAC, CANAFE/SCRS, UE) et validation par un facilitateur institutionnel agréé.
2.  **Coupe-circuit de vélocité horaire** : indépendamment des mandats individuels, un coupe-circuit déterministe bloque toute signature si le flux agrégé de la flotte dépasse un plafond horaire anormal (par exemple 500 \$ CAD/h sur les API externes), ce qui interrompt toute boucle de drainage.
3.  **Imputation ERP automatisée** : chaque `PAYMENT-RESPONSE` est corrélé au `sagaId` OpenTelemetry et versé quotidiennement au grand livre SAP S/4HANA avec sa preuve AP2, opposable aux auditeurs externes.
::::

---

## 10.12 Application au fil rouge : poste opérateur multimodal et achats ponctuels chez Groupe Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : poste opérateur AG-UI/A2UI, guidage vocal WebRTC en usine et achats ponctuels AP2/x402**
:::

**Frictions résiduelles (début 2027)** : en usine BEL, les techniciens devaient ôter leurs gants toutes les six minutes pour chercher un couple de serrage sur tablette sous 84 dB(A), tandis que les souscripteurs BCA perdaient 14 minutes par escalade HOTL à relire des synthèses textuelles. Côté achats, émettre un bon de commande SAP pour une requête douanière à 0,04 \$ USD ou pour un coursier urgent coûtait plus cher en frais administratifs que le service lui-même.

**Architecture déployée (T2 2027)** :

1.  **Postes AG-UI et A2UI chez BCA et BSN** : déploiement d’un catalogue de 16 composants React certifiés (Extrait 10.1). Sur escalade \> 5 000 \$ CAD, le souscripteur examine le tableau différentiel des clauses AS/400, ajuste le plafond en RFC 6902 et signe le Checkout Mandate AP2 avec sa clé matérielle YubiKey FIDO2.
2.  **Guidage mains libres WebRTC dans les 4 usines BEL** : casques ostéophoniques antibruit (Opus + caméra de lunettes à 1,5 trame/s) connectés à la chaîne cascadée SLM locale, avec badgeage FIDO2/NFC sans biométrie vocale (Loi 25) et annonce conforme à l’article 50 de l’EU AI Act.
3.  **Règlements AP2 et x402** : un mandat ouvert AP2 mensuel borné (Extrait 10.2) autorise l’orchestrateur BEL à régler à l’acte les vérifications tarifaires via x402 (Extrait 10.3) et les affrètements express sous 2 500 \$ CAD.

**Résultats mesurés en production** :

- **Temps médian de décision HOTL chez BCA** : abaissé de 14 minutes à 22 secondes, avec +19 % de détection des exclusions subtiles.
- **Assistance vocale en atelier (84 dB)** : latence P95 de 390 ms, interruption à 165 ms et -27 % sur le temps de remise en route des broches d’usinage.
- **Transactions autonomes** : 1 420 micropaiements x402 et 64 affrètements AP2 au T2 2027, avec zéro anomalie de réconciliation SAP.
::::

---

## 10.13 Décision d’architecture normative et points de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-007 — Découplage déclaratif des interfaces génératives via AG-UI et A2UI**
:::

- **Statut** : acceptée \| périmètre : interfaces humaines, terminaux de terrain et paiements agentiques \| révision : semestrielle
- **Contexte** : l’exposition directe des agents aux utilisateurs et aux réseaux de paiement introduit des risques élevés d’injection côté client (XSS), de complaisance d’approbation (OWASP ASI09), de coupures audio sur Wi-Fi industriel et d’engagements financiers non répudiables mal bornés.
- **Options évaluées** :
  1.  *Clavardage Markdown + cartes d’entreprise partagées* : rejetée, pour la lenteur cognitive en HOTL et l’absence de preuve cryptographique par panier.
  2.  *Génération libre de HTML/JavaScript par LLM* : rejetée, pour le risque critique d’exécution de code arbitraire dans le navigateur.
  3.  *Pile normalisée AG-UI + A2UI, WebRTC terrain et mandats AP2 / x402* : retenue, pour la séparation du code et des données, la synchronisation RFC 6902, la résilience UDP, l’autorisation matérielle FIDO2 et les mandats SD-JWT.
- **Décision** :
  1.  Toute interface applicative agentique utilise AG-UI (`STATE_DELTA` RFC 6902) et A2UI sur catalogue local homologué (ou iframe isolée MCP-UI pour les outils tiers).
  2.  Tout canal vocal ou visuel en temps réel emprunte WebRTC (SRTP + `DataChannel`), avec troncature du contexte à l’interruption (\< 200 ms), sans biométrie vocale ni inférence émotionnelle.
  3.  Tout décaissement initié par un agent requiert un mandat AP2 ouvert ou fermé (SD-JWT) signé matériellement (FIDO2/HSM), validé par Cedar et réglé en passerelle par des rails agréés ou par HTTP x402.
- **Conséquences** :
  - *Positives* : protection contre les XSS génératifs, revues HOTL rapides et éclairées, utilisabilité mains libres en atelier et auditabilité financière complète.
  - *Négatives / coûts assumés* : gouvernance du catalogue A2UI, infrastructure de relais WebRTC et raccordement à un facilitateur AP2/x402.
- **Condition de révision** : unification éventuelle d’A2UI et de MCP-UI sous l’AAIF, ou ouverture des API agentiques sur le rail canadien RTR.
::::

### Liste de contrôle de mise en production

Avant d’ouvrir une interface agentique ou d’autoriser une transaction autonome, huit exigences se vérifient :

1.  **Catalogue d’interface fermé** : le client rejette-t-il tout HTML/JavaScript libre généré pour n’afficher que des composants du catalogue local A2UI (ou une iframe MCP-UI sans `allow-same-origin`) ?
2.  **Validation serveur des différentiels AG-UI** : les opérations RFC 6902 entrantes sont-elles revalidées contre les règles métiers du serveur avant toute mutation de l’état partagé ?
3.  **Affichage différentiel HOTL** : les vues d’escalade mettent-elles en relief les preuves contradictoires plutôt qu’un texte uniforme propice à l’approbation réflexe (OWASP ASI09) ?
4.  **Troncature exacte à l’interruption WebRTC** : une interruption vocale coupe-t-elle l’audio en moins de 200 ms tout en alignant la mémoire serveur sur le dernier mot réellement entendu ?
5.  **Conformité Loi 25 et EU AI Act** : l’annonce d’interaction avec une IA est-elle explicite, sans collecte d’empreinte vocale biométrique ni détection d’émotions des employés ?
6.  **Signature matérielle AP2** : chaque mandat AP2, ouvert ou fermé, est-il signé hors du conteneur agentique par une clé FIDO2/WebAuthn ou un HSM ? Cette exigence est plus stricte que l’exposé, selon lequel l’agent signe lui-même les mandats fermés avec sa propre clé (section 10.2).
7.  **Coupe-circuit et criblage sur x402** : la passerelle vérifie-t-elle la liste blanche des bénéficiaires, la clé d’idempotence et le plafond horaire global avant d’émettre `PAYMENT-SIGNATURE` ?
8.  **Traçabilité comptable ERP** : chaque reçu `PAYMENT-RESPONSE` est-il lié au `sagaId` OpenTelemetry et archivé automatiquement avec le mandat AP2 dans l’ERP financier ?
