## Mise en œuvre — Défense en profondeur : bacs à sable, garde-fous neuro-symboliques et coupe-circuits {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu d’affaires et de risque** : Même avec une identité NHI en place (chapitre 30) et des schémas MCP épinglés (chapitre 31), un modèle de langage reste un moteur probabiliste faillible : une entrée inédite peut le tromper, et il peut inventer un paramètre destructeur. Une architecture qui confie le dernier mot de sécurité à une consigne du prompt système, ou qui exécute le code généré par un agent dans un conteneur partagé, s’expose à une compromission d’infrastructure (ASI05) ou à une dérive financière incontrôlée (ASI08/ASI10).
- **Décisions architecturales structurantes** :
  1.  *Irréversible et non négociable* : Externaliser 100 % des invariants métiers et de sécurité hors du modèle, vers un point de décision (PDP) déterministe fondé sur Cedar ou OPA (Rego), évalué en coupure obligatoire sur la passerelle agentgateway, qui joue le rôle de point d’application (PEP).
  2.  *Structurante pour l’exécution de code et l’usage d’ordinateur (CUA)* : Exclure l’exécution sur un noyau hôte partagé. Le code s’exécute dans des bacs à sable matériels éphémères (microVMs Firecracker ou modules WASI), pilotés par le protocole OpenSandbox de la Linux Foundation AAIF, sans sortie réseau par défaut.
  3.  *Opérationnelle dès la mise en service* : Relier toute la flotte à un coupe-circuit SOC multi-nuages, testé chaque trimestre, qui révoque les identités, fige les sagas durables et détruit les bacs à sable actifs sous le plafond d’homologation de dix secondes (cible interne : moins de deux secondes).
- **Indicateurs de gouvernance associés** : Taux de couverture des outils mutatifs par des règles formelles Cedar/OPA vérifiées par solveur SMT (cible : 100 %), latence d’évaluation du PDP au 99e centile ($< 2\,\text{ms}$), pourcentage de bacs à sable dont la sortie réseau est refusée par défaut (100 %), temps d’arrêt effectif mesuré en exercice (MTTR-Stop $< 2{,}0\,\text{s}$, plafond normatif $< 10\,\text{s}$).
::::

## 32.6 Isolation d’exécution : microVMs (Firecracker), OpenSandbox (AAIF) et bacs à sable WebAssembly (WASI)

Le principe directeur est de présumer la compromission cognitive du modèle. Un agent d’analyse financière qui écrit et exécute un script Python sur une feuille de calcul envoyée par un tiers, un agent d’ingénierie qui compile un correctif sur un dépôt de code, un agent d’usage d’ordinateur (CUA) qui pilote un navigateur complet sur un portail externe sans API : chacun exécute, par définition, du code non fiable généré dynamiquement sous l’influence d’entrées potentiellement hostiles (OWASP ASI05).

### Pourquoi le conteneur Linux standard (Docker / runc) ne suffit pas face à ASI05

Encapsuler l’interpréteur Python ou le navigateur de l’agent dans un conteneur Kubernetes ordinaire ne constitue pas un bac à sable suffisant. Les espaces de noms Linux (`namespaces`) et les groupes de contrôle (`cgroups`) d’un conteneur OCI standard restreignent la visibilité, mais le conteneur partage le noyau Linux de l’hôte (plus de 30 millions de lignes de code C, plus de 300 appels système `syscalls`) avec tous les autres pods du même nœud.

Un attaquant qui oriente la génération de code vers une vulnérabilité noyau récente (escalade de privilèges), qui épuise des descripteurs internes ou qui sonde le réseau local du cluster fait régulièrement céder la paroi d’un conteneur `runc` ordinaire. En 2027, l’isolation d’exécution se répartit donc en trois primitives complémentaires, fédérées par une couche protocolaire ouverte.

### Les trois primitives d’isolation et le standard fédérateur OpenSandbox (AAIF)

1.  **Noyaux d’espace utilisateur (gVisor / `runsc`)** : gVisor intercepte les appels système de l’application invitée dans un noyau de sécurité écrit en Go, en espace utilisateur (*Sentry*), et ne laisse passer vers le noyau hôte qu’une fraction restreinte de primitives. C’est un compromis adapté au durcissement de serveurs MCP existants : pas de pénalité mémoire lourde, mais un surcoût sur les entrées/sorties disque intensives.
2.  **Micro-machines virtuelles matérielles (Firecracker / Cloud Hypervisor sur KVM)** : Conçu pour le calcul multi-locataire hostile, Firecracker établit une frontière de virtualisation matérielle complète (Intel VT-x / AMD-V / ARM Virtualization Extensions), avec un moniteur minimal écrit en Rust (\~50 000 lignes de code, sans périphériques patrimoniaux superflus). Chaque session d’agent dispose de son propre noyau Linux invité. Grâce à la restauration différentielle d’instantanés mémoire (chargement paresseux `uffd`), une microVM Python préchauffée, avec `pandas`, `polars` et `scipy` déjà en mémoire, démarre en 8 à 15 millisecondes, ce qui rend l’isolation matérielle compatible avec un usage interactif.
3.  **Bacs à sable à capacités WebAssembly (WASI 0.2+ Component Model)** : Pour un connecteur de transformation déterministe, un parseur documentaire ou un outil MCP léger qui n’exige pas un système d’exploitation POSIX complet, WebAssembly offre des garanties par construction : mémoire linéaire bornée, aucun appel système implicite et modèle de capacités explicites. Un module WASI ne voit ni l’horloge, ni le système de fichiers, ni une prise réseau tant que l’hôte ne lui remet pas la poignée correspondante. Le démarrage prend de 0,2 à 2 millisecondes, pour une empreinte de quelques mégaoctets.
4.  **La couche d’abstraction ouverte OpenSandbox (Linux Foundation AAIF)** : Versé à l’*Agentic AI Foundation* aux côtés de MCP et A2A, OpenSandbox lève le verrouillage fournisseur des environnements d’exécution d’agents en normalisant un *Sandbox Protocol* : une API de cycle de vie (`create`/`pause`/`snapshot`/`destroy`) et une API d’exécution de commandes et de fichiers. L’équipe code son agent une seule fois contre le SDK OpenSandbox : le flux tourne sur un conteneur local en développement et passe sans modification à un pool haute densité de microVMs Firecracker sur Kubernetes en production.

OpenSandbox intègre aussi deux contrôles contre l’exfiltration de données : le refus de toute sortie réseau par défaut (`defaultEgress: DENY_ALL`) et un mandataire externe de justificatifs (*Credential Vault Proxy*). Au lieu d’injecter un jeton OAuth ou une clé API dans une variable d’environnement de la microVM, où le code généré par l’agent pourrait le lire par `os.environ` et l’exfiltrer par stéganographie, on retire toute interface réseau routable à la microVM. Elle ne communique que par un canal `vsock` avec un mandataire de l’hôte, qui vérifie la destination contre une liste blanche stricte et ajoute l’en-tête Authorization à l’extérieur de la frontière de virtualisation.

| Dimension d’ingénierie | Conteneur OCI standard (`runc`) | Noyau utilisateur (gVisor) | MicroVM matérielle (Firecracker) | Composant WebAssembly (WASI 0.2) | OpenSandbox (AAIF sur Firecracker) |
|:--------------|:----------------|:-----------------|:----------------|:------------------|:-----------------|
| Frontière de sécurité | Noyau hôte partagé (`namespaces`/`seccomp`) | Interception `syscalls` en espace utilisateur | Virtualisation CPU matérielle (KVM) | Mémoire linéaire et capacités Wasm | Matérielle KVM + mandataire de secrets hors VM |
| Démarrage (à froid / depuis un instantané) | 150 – 400 ms | 200 – 500 ms | 125 ms à froid / \< 15 ms depuis un instantané | 0,2 – 2 ms | 10 – 18 ms (pool préchauffé) |
| Surcoût mémoire par instance | \~15 Mo | \~35 – 60 Mo | \~25 – 45 Mo (avec déduplication) | 1 – 5 Mo | \~30 Mo actif / 0 Mo mis sur disque |
| Compatibilité de l’écosystème | 100 % Linux natif | \~97 % Linux (hors ioctl bas niveau) | 100 % Linux, binaires C/Python, CUA | Langages compilables vers `wasm32-wasip2` | 100 % Linux + API unifiée multi-SDK |
| Protection des secrets et sortie réseau | Configuration CNI manuelle fragile | Configuration CNI externe | Réseau TAP à configurer soi-même | Aucune capacité réseau par défaut | Natif : refus de la sortie + injection externe |
| Cas d’usage nominal 2027 | Orchestrateurs internes déterministes | Serveurs MCP métiers internes | Exécution de code Python/Bash arbitraire | Parseurs, validateurs et greffons rapides | Standard d’entreprise pour le code d’IA et les CUA |

Le gabarit suivant décrit l’environnement de l’analyste Python de Boréal : aucune entrée réseau, sortie refusée par défaut, secrets injectés hors de la VM.

#### Extrait 32.1 — Profil déclaratif OpenSandbox sans egress réseau et mandataire de secrets hors VM

``` yaml
apiVersion: sandbox.aaif.org/v1
kind: SandboxTemplate
metadata:
  name: boreal-python-analyst-isolated
  namespace: boreal-agent-sandboxes
spec:
  runtimeClass: "firecracker-kvm-snapshot"
  baseSnapshotId: "snap-py312-polars-202702-signed"
  lifecycle:
    maxWallClockSeconds: 180
    idleSuspendAfterSeconds: 30
    destroyAndScrubMemoryOnExit: true
  resources:
    vcpuCount: 2
    memoryMiB: 512
    maxPids: 64
    ephemeralScratchMiB: 256
  filesystem:
    rootReadOnly: true
    writablePaths: ["/tmp/work"]
    blockHostMounts: true
  networkPolicy:
    ingress: "NONE"
    defaultEgress: "DENY_ALL"
    # Bloque matériellement l'IMDS 169.254.169.254 et fd00:ec2::254
    blockCloudMetadataIp: true
    allowedVsockProxyRoutes:
      - name: "internal-snowflake-readonly-gateway"
        destinationHost: "agentgateway.internal.boreal.ca"
        destinationPort: 443
        allowedPathPrefix: "/mcp/bca-snowflake-analytics/"
        credentialInjection:
          # Le secret n'entre jamais dans la RAM de la microVM invitée
          mode: "HOST_SIDE_PROXY_INJECT"
          tokenExchangeAudience:
            "mcp://gateway.boreal.ca/mcp/bca-snowflake-analytics"
          maxRequestsPerSession: 12
```

------------------------------------------------------------------------

## 32.7 Évaluation continue PDP/PEP hors du modèle : OPA (Rego), Cedar et raisonnement automatisé

OpenSandbox confine où et comment le code s’exécute. Il reste à décider quels appels d’outils MCP et quelles délégations A2A l’agent a le droit d’émettre. Ce volet part de l’hypothèse qu’un système probabiliste ne se sécurise pas uniquement avec un second système probabiliste : un modèle juge placé devant l’agent principal réduit le bruit statistique, mais laisse une probabilité jointe d’échec strictement positive face à une entrée adversariale bien construite. La section 32.5 ne l’établit pas : elle donne un signal, non une preuve, sur un seul point de mesure.

Pour tout invariant d’affaires, réglementaire ou de sécurité (plafond d’engagement en dollars, interdiction d’écrire depuis une session teintée par un document externe, séparation des tâches, restriction horaire), la vérification s’exécute dans un moteur symbolique déterministe, placé hors de portée du modèle de langage. Le PEP et le PDP décrits plus bas relèvent des gestes 1 et 2 de la section 32.2 : écrire les invariants, les vérifier hors de l’agent.

![Architecture de défense en profondeur : garde-fous neuro-symboliques PEP/PDP hors du LLM, confinement OpenSandbox et coupe-circuit SOC.](figures/fig-32-a-1.svg)

### Architecture neuro-symbolique PEP / PDP en coupure obligatoire

L’architecture de la figure sépare le raisonnement neuronal, qui propose une intention d’action, du contrôle symbolique, qui statue sur son admissibilité :

1.  Le point d’application (PEP, agentgateway) intercepte 100 % des requêtes JSON-RPC MCP (`tools/call`) et des messages A2A (`SendMessage`). Aucun serveur MCP d’entreprise n’accepte de trafic réseau direct qui contournerait la passerelle (verrouillage mTLS mutuel). Le PEP valide le jeton RFC 8693, extrait le sujet humain (`sub`), l’agent immédiat (`act.sub`) et l’étiquette de teinte de la session (`sessionTaint`), puis désérialise les arguments typés de l’outil demandé.
2.  Le point de décision (PDP, Cedar ou OPA) évalue cette requête d’autorisation en mémoire locale (bibliothèque embarquée en Rust ou en Go dans le PEP, ou démon auxiliaire (*sidecar*) Unix) contre le référentiel de politiques signées de l’entreprise, en 0,4 à 1,5 milliseconde. Il retourne l’un de trois verdicts : `ALLOW` (transmission immédiate au serveur MCP), `DENY` (rejet avec trace d’audit SIEM) ou `STEP_UP_CIBA` (déclenchement du flux d’approbation humaine hors bande décrit au chapitre 30).

### Choisir entre Open Policy Agent (Rego) et Cedar

Les deux moteurs ouverts dominants en 2027 ont chacun leur domaine :

- **OPA (Rego)**, projet gradué de la CNCF dérivé de Datalog, est expressif sur des documents JSON arbitrairement imbriqués. Il reste la référence pour valider des manifestes d’infrastructure Kubernetes, des configurations de déploiement CI/CD ou des graphes complexes de routage réseau.
- **Cedar**, langage de politiques ouvert conçu autour de la vérification formelle et adopté pour la gouvernance des agents, apporte trois propriétés aux systèmes d’autorisation transactionnels :
  1.  **Terminaison bornée et évaluation sub-milliseconde** : Cedar interdit les boucles non bornées et la récursion générale, ce qui garantit un temps d’évaluation prévisible, en microsecondes pour le moteur seul; les autres chiffres de ce volet, de 0,4 à 2 millisecondes, visent l’appel complet au PDP.
  2.  **Priorité du refus (`forbid` l’emporte sur `permit`)** : Par défaut tout est interdit; une action n’est autorisée que s’il existe au moins une clause `permit` applicable et aucune clause `forbid` satisfaite. Une équipe de sécurité centrale peut ainsi poser trois règles `forbid` cardinales qu’aucune politique `permit` locale, écrite par une division métier, ne peut affaiblir par inadvertance.
  3.  **Vérification par solveurs SMT (raisonnement automatisé)** : La sémantique de Cedar se traduit en formules décidables, et Cedar exclut les flottants IEEE 754 au profit d’entiers 64 bits (`Long`), par exemple en cents, pour éliminer tout contournement par arrondi binaire. Le pipeline CI/CD prouve donc avant la mise en production, pour toute requête $q = (p, a, r, c)$, qu’une politique révisée $P'$ respecte l’invariant $\text{Inv}(q)$ :

$$\forall q,\; \text{Cedar}(P', q) = 1 \implies \text{Inv}(q) = 1$$

La preuve porte sur la politique, relativement à l’invariant écrit. La complétude des invariants reste la limite relevée à la section 32.2.

En pratique, OPA (Rego v1) gouverne l’admission d’infrastructure en CI/CD et sur Kubernetes, et Cedar statue en temps réel sur chaque transaction MCP. La politique OPA suivante refuse tout gabarit dont la classe d’exécution n’est ni Firecracker sous KVM ni WASI, dont la sortie réseau n’est pas refusée par défaut, ou dont une route injecte le secret dans la VM.

#### Extrait 32.2 — Politique d’admission OPA (Rego v1) validant les gabarits OpenSandbox

``` rego
package boreal.admission.sandbox

import rego.v1

default allow := false

allow if {
    count(deny) == 0
}

deny contains msg if {
    input.kind == "SandboxTemplate"
    not input.spec.runtimeClass in {"firecracker-kvm-snapshot", "wasmtime-wasi-p2"}
    msg := sprintf("Runtime interdit hors KVM/WASI : %v", [input.metadata.name])
}

deny contains msg if {
    input.kind == "SandboxTemplate"
    input.spec.networkPolicy.defaultEgress != "DENY_ALL"
    msg := "Politique réseau defaultEgress != DENY_ALL refusée (ASI05)"
}

deny contains msg if {
    some route in input.spec.networkPolicy.allowedVsockProxyRoutes
    route.credentialInjection.mode != "HOST_SIDE_PROXY_INJECT"
    msg := sprintf("Secret injecté dans la VM sur la route %v", [route.name])
}
```

Les cinq politiques Cedar suivantes expriment les invariants de Boréal : deux autorisations selon le montant, puis trois clauses `forbid` inconditionnelles.

#### Extrait 32.3 — Politique déterministe Cedar gouvernant les outils MCP financiers et logistiques

``` cedar
// Politique d'entreprise Boréal — Gouvernance déterministe des appels MCP
// Montants exprimés en cents entiers 64 bits (Long) pour décidabilité SMT.

// 1. AUTORISATION NOMINALE L3 : Pré-autorisation garantie (<= 5 000,00 $ CAD)
permit (
  principal is Boreal::AgentIdentity,
  action == Boreal::McpTool::"bca_guidewire__preauthorize_warranty_claim",
  resource is Boreal::WarrantyContract
)
when {
  principal.blueprintId == "bp-bca-warranty-tier2" &&
  principal.attestationValid == true &&
  resource.division == "BCA" &&
  context.hasValidOboToken == true &&
  context.toolArgs.amountCentsCad <= 500000 &&
  context.remainingSagaHops >= 1
};

// 2. AUTORISATION AVEC ESCALADE CIBA VALIDÉE (5 000,01 $ à 50 000,00 $ CAD)
permit (
  principal is Boreal::AgentIdentity,
  action == Boreal::McpTool::"bca_guidewire__preauthorize_warranty_claim",
  resource is Boreal::WarrantyContract
)
when {
  principal.blueprintId == "bp-bca-warranty-tier2" &&
  principal.attestationValid == true &&
  resource.division == "BCA" &&
  context.hasValidOboToken == true &&
  context.toolArgs.amountCentsCad > 500000 &&
  context.toolArgs.amountCentsCad <= 5000000 &&
  context.remainingSagaHops >= 1 &&
  context.cibaApprovalPresent == true &&
  context.cibaVerifiedTxHash == context.computedArgsHash
};

// 3. GARDE-FOU INCONDITIONNEL (FORBID #1) : Séparation des tâches (SoD)
// Aucun approbateur CIBA ne peut autoriser un dossier qu'il a lui-même initié.
forbid (
  principal,
  action == Boreal::McpTool::"bca_guidewire__preauthorize_warranty_claim",
  resource
)
when {
  context.cibaApprovalPresent == true &&
  context.cibaApproverSub == context.initiatingHumanSub
};

// 4. GARDE-FOU INCONDITIONNEL (FORBID #2) : Suivi de teinte (Anti-ASI01/ASI06)
// Une session teintée par une source externe ne peut muter un tiers payé.
forbid (
  principal,
  action in [
    Boreal::McpTool::"bel_sap_ap__update_vendor_bank_account",
    Boreal::McpTool::"bel_sap_mm__override_delivery_address"
  ],
  resource
)
when {
  context.sessionTaint == "UNTRUSTED_EXTERNAL"
};

// 5. GARDE-FOU INCONDITIONNEL (FORBID #3) : Coupe-feu budgétaire et gel SOC
forbid (principal, action, resource)
when {
  principal.killSwitchQuarantined == true ||
  context.sagaConsumedCentsCad >= context.sagaMaxBudgetCentsCad
};
```

La règle `FORBID #2` compare une valeur que le modèle ne peut pas altérer. Même si une technique d’injection de prompt inédite contournait entièrement la vigilance du modèle, l’appel à `update_vendor_bank_account` échouerait sur l’évaluation déterministe de `context.sessionTaint == "UNTRUSTED_EXTERNAL"`.

------------------------------------------------------------------------

## 32.8 Coupe-circuits SOC multi-nuages et révocation des états et des jetons

La dernière ligne de défense répond à la question qu’un conseil d’administration ou un régulateur (BSIF, article 14 du règlement européen sur l’IA sur le contrôle humain effectif) pose au CISO : en combien de secondes le centre d’opérations de sécurité (SOC) peut-il arrêter une flotte d’agents en boucle divergente, ou compromise un dimanche soir sur deux nuages distincts, sans corrompre la comptabilité en cours ? Le coupe-circuit met en œuvre, en urgence, la révocation en cours de tâche que la section 32.3 tire du principe 6 de SP 800-207.

### Pourquoi la désactivation dans l’annuaire IAM ne suffit pas en urgence

Dans une architecture distribuée, désactiver le compte dans l’annuaire d’identité n’a d’effet qu’après cinq à soixante minutes :

- les jetons d’accès JWT déjà émis restent acceptés localement jusqu’à leur `exp` si les passerelles ne reçoivent pas de flux de révocation actif;
- les workflows durables en cours dans Temporal ou Restate gardent leurs files de tâches actives et poursuivent leurs réessais automatiques;
- les bacs à sable OpenSandbox déjà démarrés poursuivent leurs calculs en mémoire vive.

À l’inverse, un interrupteur unique qui couperait toute l’IA de l’entreprise au moindre incident localisé paralyserait inutilement le support client et la logistique. Le coupe-circuit respecte un plafond normatif d’homologation inférieur à dix secondes de bout en bout (S-14, y compris vers des nœuds périphériques distants) et vise moins de deux secondes sur ses plans de contrôle infonuagiques. Il s’articule en quatre paliers, pilotés par le protocole OpenID Shared Signals Framework (SSF / CAEP, *Continuous Access Evaluation Profile*).

| Palier de coupe-circuit | Déclencheurs automatiques ou SOC | Actions atomiques coordonnées (passerelle, STS, moteur d’exécution, bac à sable) | MTTR-Stop cible | Protocole de reprise contrôlée |
|:---------------|:----------------------|:--------------------------|:--------|:--------------------------|
| Palier 1 — Chirurgical (saga unitaire) | Dépassement du budget ou des sauts d’une saga, boucle locale détectée (ASI08) | Invalidation du `sagaId` dans le cache d’agentgateway, signal `pause` sur le workflow Temporal, destruction du bac à sable associé. | \< 500 ms | Inspection de l’historique d’événements par l’équipe AgentOps; compensation de la saga ou reprise corrigée. |
| Palier 2 — Connecteur (outil ou serveur MCP) | Alerte de changement après approbation (SHA-256), erreurs 5xx en grand nombre ou anomalie d’exfiltration sur un outil | Fermeture du disjoncteur sur la route MCP dans agentgateway; mise en attente durable des sagas dépendantes, sans perte d’état. | \< 1,0 s | Revalidation Sigstore du serveur MCP, rotation des identifiants aval, réouverture progressive. |
| Palier 3 — Classe d’agent (*Blueprint*) | Comportement déviant systémique (ASI10), vulnérabilité sur un prompt ou un modèle précis | Diffusion CAEP révoquant tous les jetons où `act.blueprint_id == X`; retrait du `ClusterSPIFFEID` dans SPIRE; gel forensique des sagas actives. | \< 2,0 s | Retour à la version N-1 signée du *Blueprint*, campagne de tests adverses de non-régression, approbation du CISO. |
| Palier 4 — Domaine ou région | Incident cyber majeur multi-systèmes ou compromission d’un cluster régional | Bascule globale d’agentgateway en lecture seule (L1) ou coupure franche; arrêt de tous les pools OpenSandbox de la zone. | \< 2,0 s | Activation du plan de continuité métier manuel ou déterministe; audit forensique complet avant réarmement par paliers. |

Sur les moteurs durables (Temporal, Restate), le coupe-circuit de palier 3 exécute par défaut un gel forensique (suspension de la file de travailleurs) plutôt qu’un arrêt forcé (`terminate`) des sagas engagées à mi-chemin. Figer l’état exact sur disque préserve la preuve pour l’enquête du SOC et permet d’exécuter ensuite les transactions de compensation des réservations déjà faites (chapitre 18), sans stocks verrouillés ni écritures comptables orphelines.

Le playbook SOAR suivant exécute le coupe-circuit de palier 3 : cinq opérations en parallèle, puis un reçu signé.

#### Extrait 32.4 — Orchestrateur Python automatisé de Kill Switch SOC multi-nuages

``` python
# Playbook SOAR / SOC — Coupe-Circuit Palier 3 (Gel d'un Blueprint d'agent)
from __future__ import annotations
import asyncio
import hashlib
import hmac
import json
import time
from dataclasses import dataclass

@dataclass(frozen=True)
class KillSwitchOrder:
    incident_id: str
    blueprint_id: str
    spiffe_id_uri: str
    temporal_task_queue: str
    initiated_by_soc_analyst: str
    reason: str

@dataclass(frozen=True)
class KillSwitchReceipt:
    incident_id: str
    elapsed_ms: float
    caep_broadcast_ok: bool
    gateway_quarantine_nodes: int
    spire_entry_evicted: bool
    temporal_queue_paused: bool
    sandboxes_terminated: int
    audit_hmac_sha256: str

async def execute_tier3_agent_killswitch(
    order: KillSwitchOrder,
    ssf_transmitter,
    gateway_control_plane,
    spire_server_client,
    temporal_admin_client,
    opensandbox_fleet_client,
    worm_audit_signing_key: bytes,
) -> KillSwitchReceipt:
    t0 = time.perf_counter()

    # Exécution parallèle sur les 5 plans de contrôle (cible < 2 000 ms)
    async def broadcast_caep_revocation() -> bool:
        return await ssf_transmitter.publish_security_event(
            event_type=(
                "https://schemas.openid.net/secevent/caep/"
                "event-type/credential-change"
            ),
            subject={"format": "uri", "uri": order.spiffe_id_uri},
            reason_admin=f"[{order.incident_id}] {order.reason}",
        )

    async def quarantine_on_all_gateways() -> int:
        # Pousse principal.killSwitchQuarantined = true dans le cache Cedar
        return await gateway_control_plane.quarantine_blueprint_globally(
            blueprint_id=order.blueprint_id, ttl_seconds=86400
        )

    async def revoke_spire_workload_identity() -> bool:
        return await spire_server_client.suspend_registration_by_spiffe_id(
            order.spiffe_id_uri
        )

    async def freeze_durable_workflows_forensically() -> bool:
        # Gèle la file d'activités sans détruire l'historique d'événements
        return await temporal_admin_client.pause_task_queue_dispatch(
            task_queue=order.temporal_task_queue,
            reason=f"SOC KillSwitch {order.incident_id}",
        )

    async def purge_active_microvms() -> int:
        return await opensandbox_fleet_client.terminate_by_label(
            label_selector=f"agent.boreal.ca/blueprint={order.blueprint_id}",
            scrub_memory=True,
        )

    async with asyncio.TaskGroup() as tg:
        t_caep = tg.create_task(broadcast_caep_revocation())
        t_gw = tg.create_task(quarantine_on_all_gateways())
        t_spire = tg.create_task(revoke_spire_workload_identity())
        t_temp = tg.create_task(freeze_durable_workflows_forensically())
        t_sbx = tg.create_task(purge_active_microvms())

    elapsed_ms = round((time.perf_counter() - t0) * 1000.0, 2)
    payload_for_worm = json.dumps(
        {
            "incident_id": order.incident_id,
            "blueprint_id": order.blueprint_id,
            "analyst": order.initiated_by_soc_analyst,
            "elapsed_ms": elapsed_ms,
            "timestamp_epoch": int(time.time()),
        },
        sort_keys=True,
    ).encode("utf-8")
    signature = hmac.new(
        worm_audit_signing_key, payload_for_worm, hashlib.sha256
    ).hexdigest()

    return KillSwitchReceipt(
        incident_id=order.incident_id,
        elapsed_ms=elapsed_ms,
        caep_broadcast_ok=t_caep.result(),
        gateway_quarantine_nodes=t_gw.result(),
        spire_entry_evicted=t_spire.result(),
        temporal_queue_paused=t_temp.result(),
        sandboxes_terminated=t_sbx.result(),
        audit_hmac_sha256=signature,
    )
```

------------------------------------------------------------------------

## 32.9 Application au fil rouge et éclairages sectoriels

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : déploiement du PDP Cedar vérifié formellement et exercice trimestriel du coupe-circuit SOC**
:::

**Défi opérationnel (T2 2027)** : À l’approche de l’ouverture généralisée de la Fabrique Agentique Boréal aux trois divisions (BSN, BCA et BEL), le comité des risques du conseil d’administration exige deux garanties avant d’autoriser le passage à l’autonomie supervisée L3 sur 15 000 événements quotidiens : (1) la preuve mathématique qu’aucune hallucination de modèle ne peut violer les plafonds de délégation financière ni la Loi 25; (2) la démonstration chronométrée qu’une dérive du type « boucle d’achat à 41 000 \$ CAD », vécue fin 2026, est désormais stoppée en moins de trois secondes.

**Architecture mise en production** :

1.  **Référentiel unifié de 142 politiques Cedar vérifiées par SMT** : Toutes les passerelles agentgateway, déployées en actif-actif sur Azure Canada Central et dans les centres de données sur site de Montréal, embarquent le moteur Cedar en Rust. À chaque demande de tirage Git qui modifie une politique d’accès aux outils MCP, l’analyseur formel `cedar-spec-checker` vérifie 18 théorèmes d’invariance (dont la séparation des tâches BCA, le blocage d’écriture sous teinte externe et le plafond budgétaire par saga). Latence ajoutée mesurée en production : 0,62 ms au 99e centile.
2.  **Pool OpenSandbox sur Firecracker pour l’analytique et les CUA** : Les travailleurs d’analyse vibratoire Python de BSN et les agents d’automatisation d’écrans patrimoniaux de BCA sont migrés des conteneurs standards vers un pool préchauffé de microVMs Firecracker géré par OpenSandbox, avec `defaultEgress: DENY_ALL` et restauration d’instantané en 12 millisecondes.
3.  **Premier exercice trimestriel d’arrêt d’urgence (mai 2027)** : Sans prévenir l’équipe de garde du SOC, l’équipe d’ingénierie du chaos injecte un comportement d’agent déviant (ASI10 + ASI08) sur un clone de production de l’*Agent Réapprovisionnement* de BEL, programmé pour tenter 80 réservations inter-usines par minute et exfiltrer un journal vers une IP externe.

**Chronométrage relevé lors de l’exercice** :

- **$t + 0{,}0\,\text{s}$** : La première tentative de connexion sortante hors liste blanche est bloquée par le pare-feu `vsock` d’OpenSandbox.
- **$t + 1{,}1\,\text{s}$** : Le détecteur de vélocité OpenTelemetry repère l’anomalie de cadence des appels MCP et déclenche automatiquement l’ordre de coupe-circuit de palier 3 (Extrait 32.4).
- **$t + 2{,}4\,\text{s}$ (`MTTR-Stop = 1,3 s` après détection)** : Les 14 instances agentgateway bloquent le *Blueprint*, le `ClusterSPIFFEID` est suspendu, 9 workflows Temporal en vol sont figés en pause forensique et 4 microVMs Firecracker actives sont détruites avec effacement de la mémoire.
- **Impact métier et financier constaté** : 0,00 \$ CAD de perte, 0 écriture erronée dans SAP S/4HANA, reprise nominale sur la version saine précédente en 11 minutes après compensation automatique des baux de réservation.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Fournisseurs infonuagiques et SaaS — Isolation multi-locataire du code généré à la volée**
:::

Un éditeur SaaS B2B offre à ses 22 000 entreprises clientes des agents capables d’exécuter des transformations de données personnalisées ou des scripts d’extension. Une évasion de bac à sable ne compromet pas seulement l’éditeur : elle franchit la frontière entre locataires concurrents. Trois mesures supplémentaires s’imposent en environnement multi-locataire hostile :

1.  **Aucune réutilisation de microVM entre locataires** : Un instantané de base vierge peut être partagé en lecture seule (copie sur écriture). Dès qu’une instance Firecracker a reçu le moindre octet du locataire A, elle n’est jamais recyclée pour le locataire B : elle est détruite et ses pages mémoire sont remises à zéro par l’hyperviseur (`MADV_DONTNEED` / `mem_scrub`).
2.  **Canaux auxiliaires du processeur** : Désactivation de l’hyperthreading ou ordonnancement de cœur dédié sur les nœuds qui exécutent du code généré arbitraire, pour neutraliser les canaux auxiliaires micro-architecturaux du cache CPU (L1TF, MDS, variantes Spectre).
3.  **Chiffrement éphémère par locataire des volumes de travail** : Tout espace temporaire `/tmp/work` monté dans la microVM utilise une clé symétrique volatile, générée pour la seule durée de la tâche et purgée à la fin du processus Firecracker.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Opérations cyber-physiques et énergie — Modes de repli sûrs à l’activation d’un coupe-circuit**
:::

Dans un centre de tri automatisé, une centrale hydroélectrique ou une usine chimique, déclencher un coupe-circuit informatique sans avoir conçu la physique sous-jacente peut être aussi dangereux que l’anomalie initiale. Si un agent d’optimisation énergétique pilote des consignes de chauffage ou de débit et qu’un palier 3 le fige, les équipements physiques ne doivent pas rester bloqués sur une valeur transitoire instable.

L’architecture IT/OT impose une convention de bail court à battement de cœur côté automate programmable (PLC / SCADA) : toute consigne d’optimisation suggérée par le *System of Action* porte une validité bornée (par exemple 60 secondes). Quand le coupe-circuit SOC fige l’agent et interrompt le renouvellement du bail validé par le jumeau numérique, l’automate bascule sans à-coup vers sa loi de commande nominale locale, déterministe et pré-programmée (état de repli sûr). L’installation reste ainsi continue sur le plan physique, sans dépendre du réseau informatique.
::::

------------------------------------------------------------------------

## 32.10 Décision d’architecture normative et points de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-020 — Découplage systématique des garde-fous déterministes (Cedar/OPA) et exécution en microVM isolée**
:::

- **Statut** : Acceptée \| Périmètre : sécurité à l’exécution et SOC \| Révision : semestrielle
- **Contexte** : Les modèles de langage restent probabilistes et vulnérables aux entrées adversariales inédites. Leur confier le respect des plafonds métiers, ou exécuter le code qu’ils produisent dans des conteneurs à noyau partagé, crée un risque inacceptable d’escalade système (ASI05) et de pertes opérationnelles rapides (ASI08/ASI10).
- **Options évaluées** :
  1.  *Garde-fous purement neuronaux (modèles modérateurs en série) et conteneurs Docker standards* : Coût initial faible, mais aucune garantie formelle d’invariance et exposition directe du noyau Linux hôte aux évasions de code généré. Rejetée.
  2.  *Validation humaine synchrone sur 100 % des actions et machines virtuelles lourdes traditionnelles* : Dégrade la vélocité métier, induit le biais d’approbation réflexe (ASI09) et impose 30 à 60 secondes de démarrage par tâche. Rejetée.
  3.  *Architecture neuro-symbolique (PEP agentgateway + PDP Cedar vérifié par SMT), isolation OpenSandbox sur microVMs Firecracker ou WASI sans sortie réseau, et coupe-circuit SOC à quatre paliers via OpenID SSF/CAEP* : Retenue.
- **Décision** : (a) Tout appel d’outil MCP mutatif ou toute délégation A2A est évalué hors du modèle par un PDP déterministe (Cedar en temps réel, OPA en admission CI/CD) dont les clauses `forbid` cardinales sont prouvées par raisonnement automatisé; (b) toute exécution de code généré, d’analyse de fichiers tiers ou de session CUA s’effectue exclusivement dans un bac à sable éphémère à virtualisation matérielle (Firecracker) ou à capacités WASI, via OpenSandbox, en politique `DENY_ALL` sortante et avec injection des secrets hors de la VM; (c) chaque classe d’agent est raccordée au coupe-circuit SOC, testé chaque trimestre lors d’un exercice chronométré (plafond d’homologation `< 10 s`, cible automatisée `MTTR-Stop < 2 s`).
- **Conséquences** :
  - *Positives* : Vérification hors du modèle du respect des limites financières et de la séparation des tâches, relativement aux invariants écrits (l’exposé y voit un signal, non une preuve, à la section 32.5; la complétude de ces invariants n’est pas démontrée, section 32.2), immunité du cluster hôte face au code malveillant généré, arrêt d’urgence quasi instantané sans corruption transactionnelle.
  - *Négatives / coûts assumés* : Nœuds supportant la virtualisation imbriquée ou le métal nu (KVM `/dev/kvm`) pour Firecracker, et gouvernance conjointe des schémas Cedar entre architectes métiers et SecOps.
- **Condition de révision** : Réévaluation semestrielle selon l’évolution des performances du modèle de composants WASI et des spécifications OpenSandbox au sein de la Linux Foundation AAIF.
::::

### Liste de contrôle de mise en production

Au terme des volets consacrés à l’identité, à la sécurité zero trust et à la résilience cyber (chapitres 30 à 32), huit exigences se vérifient avant toute ouverture au trafic réel :

1.  **Aucun invariant dans le prompt** : Les limites financières, règles de séparation des tâches, plages horaires et restrictions de teinte sont-elles codées dans un PDP déterministe (Cedar/OPA) externe au modèle, plutôt que dans les consignes textuelles de l’agent ?
2.  **Passage obligé par le PEP** : L’architecture réseau (mTLS, politiques CNI) interdit-elle à un pod d’agent d’appeler un serveur MCP en contournant l’évaluation PEP/PDP de la passerelle agentgateway ?
3.  **Preuve formelle en CI/CD** : Les clauses `forbid` critiques des politiques Cedar sont-elles vérifiées par solveur SMT à chaque déploiement, afin de prouver l’absence de régression d’autorisation ?
4.  **Virtualisation matérielle du code dynamique** : Toute exécution d’interpréteur (Python, Bash, JS) ou de navigateur CUA pilotée par un agent tourne-t-elle dans une microVM dédiée (Firecracker) ou un composant WASI détruit après usage, et jamais dans un conteneur qui partage le noyau hôte ?
5.  **Refus de la sortie réseau par défaut et blocage des métadonnées** : Les bacs à sable bloquent-ils par défaut toute sortie Internet ainsi que l’adresse de métadonnées infonuagiques (169.254.169.254), en limitant la communication au seul canal `vsock` contrôlé ?
6.  **Secrets hors de la mémoire invitée** : Les jetons d’accès aux services autorisés sont-ils injectés à l’extérieur de la microVM par un mandataire de l’hôte (*Credential Vault Proxy*), de sorte que le code de l’agent ne lise jamais le secret brut ?
7.  **Coupe-circuit SOC à gel forensique** : Le playbook de coupe-circuit révoque-t-il ensemble les SVID/JWT (CAEP), les routes agentgateway et les microVMs, tout en mettant les sagas Temporal/Restate en pause conservatoire pour préserver l’audit et les compensations ?
8.  **Homologation trimestrielle par exercice** : Le temps d’arrêt effectif de bout en bout a-t-il été mesuré sous le plafond normatif de 10 secondes (et sous la cible automatisée MTTR-Stop de 2 secondes) lors d’un test réel d’injection de compromission, au cours des 90 derniers jours ?
