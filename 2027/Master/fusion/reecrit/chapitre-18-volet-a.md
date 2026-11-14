## Mise en œuvre — Moteurs d'exécution durable et gestion des cycles de vie de longue durée {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu** : un processus d'entreprise ne s'achève pas en trois secondes dans l'onglet d'un navigateur. Il traverse des pannes d'API externes, des redéploiements d'infrastructure, des analyses d'experts tiers et des délais légaux ou humains de plusieurs jours. Des agents exécutés en mémoire vive obligent à choisir entre perdre les dossiers en cours au moindre redémarrage et réexécuter des appels LLM coûteux et des mutations métier déjà commises.
- **Décisions d'architecture** :
  1.  *Irréversible à moyen terme* : confier la progression, les temporisateurs, les politiques de nouvel essai et l'attente d'approbation à un moteur d'exécution durable à journal d'événements immuable, hors des cadriciels de prompts.
  2.  *Structurante dès le cadrage de la plateforme* : adopter une architecture bi-vitesse, avec Temporal pour les sagas longues de plusieurs semaines, très auditables, et Restate ou Durable Task pour la micro-orchestration à haute cadence et le sans-serveur. L'autre voie est d'assumer l'adhérence à un runtime infonuagique intégré (Bedrock AgentCore).
  3.  *Impérative pour la sécurité et la conformité* : chiffrer côté client les charges utiles journalisées (effacement cryptographique, compatible avec la Loi 25 / RGPD) et revalider le monde et les droits après toute mise en veille prolongée.
- **Indicateurs de gouvernance** : taux de survie sans intervention aux redémarrages d'infrastructure (cible : 100 %), taux de double exécution d'effets de bord (cible : 0 %), consommation CPU/RAM des instances en attente d'approbation humaine (mise à l'échelle à zéro) et zéro erreur de non-déterminisme (`NonDeterminismError`) lors des mises en production continues.
::::

## 18.8 Défaillance volatile et fondements formels de l'exécution durable

Prenons un agent d'instruction financière codé selon les habitudes d'une application web `Node.js` ou Python FastAPI, en mémoire vive. Il reçoit une déclaration de sinistre complexe. Il invoque d'abord un modèle multimodal de raisonnement, qui analyse quarante pages de rapport métallurgique (durée : 22 secondes, coût : 0,48 \$ CAD). Il appelle ensuite un outil MCP qui crée une réserve financière provisoire dans le progiciel comptable, puis envoie une demande de validation asynchrone CIBA au souscripteur principal. À réception de la réponse, quarante-huit heures plus tard, il déclenche l'ordre de règlement.

Quatre défaillances ordinaires interrompent cette séquence :

1.  **Éviction de conteneur ou déploiement continu** : trois heures après la notification au souscripteur, le cluster Kubernetes recycle le pod pour appliquer un correctif de sécurité Linux. La pile d'appels en mémoire (`await waitForApproval()`) disparaît, et aucun processus n'attend le clic sur « Approuver » du lendemain matin (section 18.1).
2.  **Point de contrôle naïf** : certaines bibliothèques d'agents sérialisent l'état du graphe dans une table PostgreSQL à la fin de chaque nœud. Si le conteneur plante après que le serveur MCP a débité la réserve dans l'ERP, mais avant que l'acquittement n'atteigne la bibliothèque, le redémarrage relit le dernier point connu. L'agent réinvoque le LLM, ce qui coûte de nouveau 0,48 \$ CAD et peut donner un montant légèrement différent, puis réexécute l'écriture comptable (section 18.3).
3.  **Attente passive coûteuse** : des processus, des coroutines lourdes ou des connexions WebSocket maintenus pendant des heures, dans l'attente d'un humain ou d'un partenaire B2B, immobilisent de la mémoire et saturent les tables de descripteurs réseau (section 18.6).
4.  **Collision de versions sur les dossiers à cycle long** : un dossier d'indemnisation ou d'octroi hypothécaire vit couramment de quatorze à soixante jours, alors que l'équipe livre trois nouvelles versions du flux par semaine. Sans versionnage de l'historique en vol, changer l'ordre de deux étapes corrompt la désérialisation de tous les dossiers ouverts sous la version précédente (section 18.2).

### Modèle formel de l'exécution durable journalisée

L'exécution durable inverse la relation entre le code et la base de données. Le développeur n'a plus à découper sa logique métier en tables d'état et en files de messages : le moteur scinde l'application en deux plans régis par des lois opposées, comme l'illustre la figure ci-dessous.

![Mécanisme d’exécution durable par journalisation immuable, barrière d’effets de bord et reprise sur crash sans double exécution.](figures/fig-18-a-1.svg)

Formellement, l'exécution d'un workflow est modélisée comme une machine à états déterministe pure $f$ opérant sur un journal d'événements immuable en ajout seul $H_k = \langle e_1, e_2, \dots, e_k \rangle$ persisté avec consensus transactionnel :

$$S_k = f(H_k) = f(\langle e_1, e_2, \dots, e_k \rangle)$$

Cette équation impose une barrière d'effets de bord entre deux types de composants. L'appel au modèle reste du côté des effets, comme le veut la section 18.2.

- **Le code d'orchestration** (workflow dans Temporal, gestionnaire déterministe dans Restate ou Durable Task) : il s'écrit en code impératif séquentiel ordinaire (`if/else`, boucles bornées, `Promise.all`, `try/catch`), mais ne fait aucune entrée-sortie réseau directe, ne lit pas l'horloge système (`Date.now()`) et ne génère aucun nombre aléatoire (`Math.random()`). Il n'agit sur le monde qu'en émettant des commandes vers le moteur durable.
- **Les unités d'effets de bord** (activités dans Temporal, blocs `ctx.run` dans Restate) : le non-déterminisme et les mutations externes résident exclusivement de ce côté, avec les appels d'inférence LLM probabilistes (Open Responses), les invocations d'outils MCP, les délégations A2A v1.0 et les lectures de politiques dynamiques.

Quand une activité d'inférence LLM s'achève au pas $i$, le moteur persiste atomiquement sa charge utile de retour $r_i$ dans l'événement $e_i$ du journal. Si l'exécutant meurt au pas $k > i$, ou s'il a été évincé de la mémoire pendant neuf jours d'attente humaine (mise à l'échelle à zéro), un nouvel exécutant reconstruit l'état exact $S_k$ en rejouant le code du workflow depuis la première ligne. Au pas $i \le k$, l'intercepteur du SDK retrouve l'événement `ActivityTaskCompleted` dans le journal local $H_k$ et retourne en quelques microsecondes la valeur $r_i$ enregistrée, sans franchir le réseau ni rappeler le LLM. À la frontière $k + 1$, non encore inscrite, l'exécution réelle reprend.

### Clé d'idempotence dérivée du journal

Pendant l'exécution initiale d'une activité, une coupure réseau entre le serveur MCP aval et l'exécutant reste une livraison au moins une fois, pilotée par la politique de nouvel essai de l'activité. Pour obtenir un effet unique de bout en bout sur une écriture financière ou logistique, il suffit de combiner la numérotation déterministe du journal avec l'idempotence du serveur MCP décrite à la section 18.3 :

$$K_{\text{idemp}} = \text{HMAC-SHA256}\!\left(K_{\text{dom}}, \; \text{WfId} \;\|\; \text{Epoch} \;\|\; \text{SeqId}\right)$$

L'identifiant `WfId` (`WorkflowId`) et le numéro de séquence `SeqId` de l'étape restent invariants à travers tous les nouveaux essais d'une même activité, et diffèrent d'une étape légitime suivante dans une boucle. Le système d'enregistrement cible (SAP S/4HANA, Guidewire, Stripe) déduplique donc tout doublon réseau transitoire.

---

## 18.9 Panorama architectural comparé des moteurs d'exécution durable en 2027

Quatre plateformes structurent en 2027 l'exécution durable des systèmes agentiques, avec des philosophies d'architecture distinctes. Deux moteurs ouverts sont portables sur toute infrastructure : Temporal et Restate. Deux piles sont étroitement intégrées à un grand écosystème infonuagique : Microsoft Agent Framework sur Durable Task, et Amazon Bedrock AgentCore. La figure ci-dessous les situe. Le tableau de la section 18.6 reprend ce que les éditeurs disent des effets de leur produit; les matrices qui suivent comparent l'architecture et l'exploitation.

![Positionnement architectural comparé de Temporal, Restate, Microsoft Agent Framework (Durable Task) et Amazon Bedrock AgentCore.](figures/fig-18-a-2.svg)

### Temporal et Temporal Nexus : sagas critiques de plusieurs semaines

Temporal est issu de travaux fondateurs menés chez AWS et Uber, puis publié sous licence ouverte MIT. Il est en 2027 la référence pour l'orchestration des processus critiques de longue durée (régimes T3 et T4 du chapitre 1) dans la banque, l'assurance, le commerce mondial et l'industrie. Son architecture repose sur un découplage par interrogation active (*pull*) : les exécutants, hébergés dans les réseaux sécurisés de chaque division, ouvrent des connexions sortantes gRPC/mTLS vers des files de tâches nommées, sans exposer de port entrant.

Deux capacités distinguent Temporal dans une grande entreprise multi-divisions :

- **Fédération inter-domaines par Temporal Nexus** : au lieu d'un cluster unique partagé, où une équipe pourrait lire les journaux d'une autre, Nexus permet à un workflow de la division BSN d'invoquer une opération durable exposée par l'espace de noms isolé de la division financière BCA. L'appel passe par un contrat RPC typé, avec propagation des annulations, des délais d'expiration et de l'identité, sans exposer les détails internes de BCA.
- **Outillage du cycle de vie long** : requêtes synchrones (Queries), mutations validées en vol (Updates), migration de version sans coupure (Workflow Versioning / Worker Build IDs) et chiffrement de bout en bout par Payload Codec client. Le serveur Temporal, en nuage ou auto-hébergé, ne voit jamais passer en clair un nom d'assuré ou le texte d'un prompt.

### Restate : micro-orchestration à haute cadence et sans serveur

Restate est conçu par les créateurs originaux d'Apache Flink. Il vise la légèreté opérationnelle et la basse latence (T2 et T3). Écrit en Rust autour d'un journal distribué intégré (*Bifrost*, sans dépendance obligatoire à une base Cassandra ou PostgreSQL externe), il fonctionne comme un proxy inverse placé devant les services d'agents. Ses trois abstractions répondent aux besoins des flottes d'agents :

1.  **Services durables** : gestionnaires RPC dont chaque appel d'outil ou de LLM encapsulé dans `ctx.run(...)` est journalisé.
2.  **Virtual Objects adressables par clé** : objets virtuels avec un seul écrivain par clé (*Single-Writer per Key*). Ils permettent d'associer un agent jumeau à chaque numéro de série de machine (BOR-CMP-90441) ou à chaque panier client, en sérialisant les événements concurrents. La section 18.6 décrit plutôt, pour Restate, un journal rejoué où l'état voyage avec chaque requête, avec des services sans état; elle ne traite pas d'état clé-valeur persistant.
3.  **Modèle *push* HTTP/2 sans serveur** : à la différence des exécutants permanents en boucle d'écoute, Restate pousse les invocations en HTTP/2 (avec flux bidirectionnel) vers des fonctions AWS Lambda, Cloud Run, Knative ou des pods Kubernetes standard. Quand un agent appelle `ctx.awakeable()` pour attendre un webhook A2A ou une réponse humaine, Restate suspend la requête HTTP. La facture de calcul de la fonction tombe à zéro jusqu'à la réception du rappel.

### Microsoft Agent Framework (Durable Task Framework, Azure et Dapr)

Le Microsoft Agent Framework résulte de la convergence opérée par Microsoft entre AutoGen (exploration multi-agents) et Semantic Kernel (socle d'entreprise). Son extension durable s'appuie sur le moteur Durable Task Framework, exécutable sur Azure Durable Functions, sur le planificateur géré Durable Task Scheduler ou, de façon portable, sur Kubernetes via Dapr Workflow. Les paquets de cette extension sont en préversion, et son checkpointing durable ne rend ni les outils ni les écritures externes transactionnels ou exécutés exactement une fois (section 18.6). Le cadriciel unifie l'état conversationnel de l'agent (*Durable Agent Threads*) et l'orchestration déterministe de processus en `.NET` (C#) et Python. Il se couple nativement à la délégation d'identité Microsoft Entra ID On-Behalf-Of et interopère directement avec les agents frontaux Microsoft Copilot Studio.

### Amazon Bedrock AgentCore : sessions microVM persistantes et pile gérée AWS

Amazon Bedrock AgentCore s'adresse aux organisations ancrées sur AWS qui veulent exécuter des graphes d'agents arbitraires (LangGraph, Strands Agents, CrewAI, code Python/TypeScript sur mesure) sans gérer elles-mêmes l'infrastructure d'exécution ni les bacs à sable d'outils. Chaque session d'agent s'exécute dans une microVM dédiée, isolée matériellement, qui peut conserver sa mémoire, son système de fichiers local et ses processus d'arrière-plan pendant plusieurs heures d'activité continue. S'y ajoutent AgentCore Gateway (exposition MCP sécurisée), AgentCore Identity et AgentCore Memory. Pour les sagas réglementaires de plusieurs semaines (T4), l'architecture AWS recommandée associe AWS Step Functions, comme trame d'ensemble, à des sessions Bedrock AgentCore pour les phases de raisonnement intensif. Cette association va au-delà de ce que retient l'exposé : la section 18.6 présente côté AWS les Lambda durable functions (points de contrôle et rejeu, exécutions jusqu'à un an, attentes non facturées) et les situe par rapport à Step Functions, service distinct fondé sur un langage de graphe.

### Matrices d'évaluation et d'urbanisation

| Dimension d’ingénierie | Temporal (+ Nexus) | Restate | Microsoft Agent Framework (Durable Task) | Amazon Bedrock AgentCore |
|:---------------|:--------------------|:-------------------|:----------------------|:----------------------|
| Modèle de transport vers l'agent | *Pull* gRPC sortant par les exécutants, sur files de tâches | *Push* HTTP/2 / gRPC (compatible FaaS sans serveur) | *Trigger* Azure Functions ou *Sidecar* Dapr | Runtime géré AWS, par session microVM isolée |
| Latence de journalisation par pas | Aucune latence chiffrée (section 18.6); persistance SQL / Cassandra multi-AZ | Aucune latence chiffrée (section 18.6); journal Rust Bifrost intégré | Aucune latence chiffrée (section 18.6); selon le backend de stockage (Scheduler / Azure Storage) | Faible intra-session; dépend de Step Functions en T4 |
| Horizon maximal de cycle de vie | Aucune limite de durée à une exécution (section 18.1); Continue-As-New natif | Minutes à semaines (Workflows + Awakeables) | Heures à semaines (Durable Orchestrations) | Sessions actives multi-heures; multi-semaines via Step Functions |
| État par entité (acteur virtuel) | Simulé par Workflow-par-Entité | *Virtual Objects* verrouillés par clé; l'exposé décrit des services sans état et un état porté par la requête (section 18.6) | Natif (*Durable Entities* / *Agent Threads*) | Session isolée + service AgentCore Memory |
| Fédération inter-équipes sécurisée | Excellente (Temporal Nexus inter-namespaces) | Bonne via contrats de services HTTP/IDL | Bonne via passerelles Azure API / A2A | Contrôlée par politiques AWS IAM inter-comptes |
| Chiffrement client de bout en bout | Natif (Payload Codec AES-GCM zéro connaissance) | Pris en charge par des intercepteurs de sérialisation du SDK | Chiffrement Azure Key Vault / stockage | Chiffrement AWS KMS géré côté cloud |
| Portabilité et coût de sortie | Maximale (Open Source MIT + Cloud géré multi-régions) | Très élevée (binaire unique BSL / Open + Cloud) | Moyenne-haute (code portable via Dapr, optimal sur Azure) | Faible (fort couplage aux primitives AWS natives) |

| Profil de charge et contrainte métier | Runtime principal recommandé | Justification architecturale | Vigilance opérationnelle |
|:-------------------------|:------------------|:-----------------------------|:--------------------------|
| Saga réglementée multi-jours/semaines (T4, banque BSIF E-23, assurance) | Temporal | Piste d'audit immuable sur longue période, chiffrement par Payload Codec, versionnage fin en vol et isolation Nexus | Dimensionner le compactage Continue-As-New au-delà de 10 000 événements |
| Micro-orchestration d'agents A2A/MCP à haute fréquence ou sans serveur (T2/T3) | Restate | Mise à l'échelle à zéro sur FaaS et verrouillage par clé d'équipement | Encadrer le déterminisme autour des appels `ctx.run` |
| Système d'information centré sur `.NET`, Entra ID et Copilot Studio | Microsoft Agent Framework (Durable Task) | Continuité entre la conversation Teams, la délégation OBO Entra et les workflows C#/Python | Préférer le Durable Task Scheduler dédié aux files de stockage génériques à fort débit |
| Agent analytique lourd exécutant du code Python ou des outils dans un environnement tout AWS | Amazon Bedrock AgentCore (+ Step Functions si T4) | Isolation matérielle microVM clé en main, qui évite de bâtir sa propre flotte de bacs à sable | Encapsuler la logique métier derrière des interfaces propres pour limiter le verrouillage AWS |

---

## 18.10 Patrons de code de production : workflows durables, awakeables et revalidation au réveil

#### Extrait 18.1 — Workflow Temporal de production avec versionnage en vol et approbation CIBA multi-jours

Ce workflow n'importe ni module réseau ni SDK LLM : il orchestre des proxys d'activités typés. Il utilise `patched()` pour introduire sans coupure une règle mineure pendant que des milliers de sinistres dorment en base; une refonte majeure de topologie utilisera le *Worker Deployment Versioning* en mode PINNED, afin que les instances en vol s'achèvent sur leur révision d'origine. Il gère l'attente de quatorze jours, avec relance au troisième jour, et exécute sa compensation dans une portée `CancellationScope.nonCancellable`, pour qu'une annulation externe du dossier n'empêche pas la libération comptable. Le décaissement définitif est l'étape pivot de la section 18.7 : la provision compensable, l'approbation et la revalidation le précèdent.

``` typescript
import {
  proxyActivities,
  defineSignal,
  defineQuery,
  setHandler,
  condition,
  patched,
  CancellationScope,
  ApplicationFailure,
} from "@temporalio/workflow";
import type * as activities from "./claimActivities";

// Configuration différenciée des délais et réessais selon la nature des activités
const {
  extractMetallurgicalReportLlm,
  evaluatePolicyCoverageMcp,
  placeProvisionalReserveMcp,
  releaseProvisionalReserveMcp,
  dispatchCibaApprovalRequest,
  executeFinalSettlementMcp,
} = proxyActivities<typeof activities>({
  startToCloseTimeout: "2 minutes",
  heartbeatTimeout: "20 seconds",
  retry: {
    initialInterval: "2 seconds",
    backoffCoefficient: 2.0,
    maximumInterval: "1 minute",
    maximumAttempts: 4,
    nonRetryableErrorTypes: ["PolicyViolationError", "SchemaValidationError", "UnauthorizedMandateError"],
  },
});

const { revalidateWorldStateAfterWakeup } = proxyActivities<typeof activities>({
  startToCloseTimeout: "30 seconds",
  retry: { maximumAttempts: 3 },
});

export interface CibaDecisionPayload {
  readonly approved: boolean;
  readonly underwriterSubjectId: string;
  readonly signedAssertionJwt: string;
  readonly comment: string;
  readonly decidedAtIso: string;
}

export const cibaApprovalSignal = defineSignal<[CibaDecisionPayload]>(
  "bca.ciba.underwriterDecision"
);
export const claimStatusQuery = defineQuery<{ stage: string; reservedCad: number }>("bca.claim.currentStatus");

export interface ClaimWorkflowInput {
  readonly claimId: string;
  readonly policyNumber: string;
  readonly equipmentSerial: string;
  readonly reportArtifactUri: string;
  readonly initiatingBrokerId: string;
}

export async function adjudicateMachineryBreakdownClaimWorkflow(
  input: ClaimWorkflowInput
): Promise<{ outcome: "SETTLED" | "REJECTED" | "EXPIRED_ESCALATED"; finalAmountCad: number }> {
  let stage = "INITIALIZING";
  let reservedCad = 0;
  let cibaDecision: CibaDecisionPayload | null = null;

  setHandler(claimStatusQuery, () => ({ stage, reservedCad }));
  setHandler(cibaApprovalSignal, (payload) => {
    if (cibaDecision === null) {
      cibaDecision = payload;
    }
  });

  // Étape 1 : Extraction structurée du rapport d'expertise (LLM non déterministe journalisé)
  stage = "EXTRACTING_EVIDENCE";
  const extraction = await extractMetallurgicalReportLlm({
    claimId: input.claimId,
    reportArtifactUri: input.reportArtifactUri,
  });

  // Étape 2 : Vérification de couverture contractuelle via MCP (IBM i / Guidewire)
  stage = "CHECKING_COVERAGE";
  const coverage = await evaluatePolicyCoverageMcp({
    policyNumber: input.policyNumber,
    equipmentSerial: input.equipmentSerial,
    failureRootCauseCode: extraction.rootCauseCode,
    claimedAmountCad: extraction.estimatedRepairCostCad,
  });

  if (!coverage.isEligible) {
    stage = "REJECTED_BY_POLICY";
    return { outcome: "REJECTED", finalAmountCad: 0 };
  }

  // Étape 3 : Constitution d'une provision comptable compensable
  stage = "RESERVING_PROVISION";
  const reservation = await placeProvisionalReserveMcp({
    claimId: input.claimId,
    amountCad: coverage.netPayableCad,
  });
  reservedCad = coverage.netPayableCad;

  try {
    // Seuil HOTL : Au-delà de 15 000 $ CAD, approbation CIBA asynchrone obligatoire (BSIF E-23)
    if (coverage.netPayableCad > 15_000) {
      stage = "AWAITING_UNDERWRITER_CIBA";
      await dispatchCibaApprovalRequest({
        claimId: input.claimId,
        amountCad: coverage.netPayableCad,
        evidenceSummaryUri: extraction.summaryClaimCheckUri,
        escalationTier: "SENIOR_UNDERWRITER",
      });

      // Attente initiale de 3 jours calendaires (0 CPU consommé en mémoire!)
      const answeredWithin3Days = await condition(() => cibaDecision !== null, "3 days");
      if (!answeredWithin3Days) {
        await dispatchCibaApprovalRequest({
          claimId: input.claimId,
          amountCad: coverage.netPayableCad,
          evidenceSummaryUri: extraction.summaryClaimCheckUri,
          escalationTier: "CLAIMS_DIRECTOR_BACKUP",
        });
        // Fenêtre résiduelle de 11 jours (total 14 jours)
        const answeredWithin14Days = await condition(() => cibaDecision !== null, "11 days");
        if (!answeredWithin14Days) {
          await releaseProvisionalReserveMcp({ reservationId: reservation.reservationId });
          reservedCad = 0;
          stage = "EXPIRED_SLA";
          return { outcome: "EXPIRED_ESCALATED", finalAmountCad: 0 };
        }
      }

      if (!cibaDecision!.approved) {
        await releaseProvisionalReserveMcp({ reservationId: reservation.reservationId });
        reservedCad = 0;
        stage = "REJECTED_BY_UNDERWRITER";
        return { outcome: "REJECTED", finalAmountCad: 0 };
      }

      // Évolution sécurisée en vol (déployée sans casser les dossiers déjà démarrés!)
      if (patched("bca-2027-04-post-hibernation-guard")) {
        stage = "REVALIDATING_AFTER_WAKEUP";
        const driftCheck = await revalidateWorldStateAfterWakeup({
          claimId: input.claimId,
          policyNumber: input.policyNumber,
          approverSubjectId: cibaDecision!.underwriterSubjectId,
          signedAssertionJwt: cibaDecision!.signedAssertionJwt,
          expectedNetPayableCad: coverage.netPayableCad,
        });

        if (!driftCheck.canProceed) {
          throw ApplicationFailure.nonRetryable(
            `Dérive post-réveil bloquante : ${driftCheck.blockingReason}`,
            "PostHibernationDriftError"
          );
        }
      }
    }

    // Étape 4 : Décaissement définitif idempotent
    stage = "EXECUTING_SETTLEMENT";
    await executeFinalSettlementMcp({
      claimId: input.claimId,
      reservationId: reservation.reservationId,
      finalAmountCad: coverage.netPayableCad,
    });

    stage = "SETTLED";
    return { outcome: "SETTLED", finalAmountCad: coverage.netPayableCad };
  } catch (err) {
    // Portée non annulable : garantit la libération comptable même si le workflow lui-même est annulé
    if (reservedCad > 0) {
      await CancellationScope.nonCancellable(async () => {
        await releaseProvisionalReserveMcp({ reservationId: reservation.reservationId });
      });
      reservedCad = 0;
    }
    throw err;
  }
}
```

#### Extrait 18.2 — Activités Temporal idempotentes avec clé déterministe et battement de cœur (Heartbeat)

Du côté non déterministe de la barrière, l'activité dérive sa clé d'idempotence des métadonnées immuables du contexte Temporal (`workflowId` + `activityId`). Elle émet un battement de cœur toutes les huit secondes pendant l'appel d'inférence, ce qui permet de détecter en moins de vingt secondes un nœud GPU figé. Elle distingue les erreurs métier définitives des pannes réseau qui justifient un nouvel essai. Le code emploie l'en-tête `X-Idempotency-Key`; l'exposé indique à la place `Idempotency-Key`, que normalise le brouillon de l'IETF (section 18.3).

``` typescript
import { Context, ApplicationFailure } from "@temporalio/activity";
import { createHmac } from "node:crypto";

export function deriveDeterministicIdempotencyKey(domainSalt: string): string {
  const info = Context.current().info;
  return createHmac("sha256", domainSalt)
    .update(
      [info.workflowNamespace, info.workflowExecution.workflowId, info.activityId].join(":")
    )
    .digest("hex");
}

export async function extractMetallurgicalReportLlm(params: {
  claimId: string;
  reportArtifactUri: string;
}): Promise<{
  rootCauseCode: string;
  estimatedRepairCostCad: number;
  summaryClaimCheckUri: string;
}> {
  const ctx = Context.current();
  const hb = setInterval(
    () => ctx.heartbeat({ phase: "awaiting_structured_output", claimId: params.claimId }),
    8_000
  );
  try {
    const response = await fetch("https://agentgateway.internal.boreal.ca/v1/responses", {
      method: "POST",
      signal: ctx.cancellationSignal,
      headers: {
        "Content-Type": "application/json",
        "X-Idempotency-Key": deriveDeterministicIdempotencyKey("bca-llm-extract"),
      },
      body: JSON.stringify({
        model: "boreal-ca-reasoning-tier1",
        input_artifact_uri: params.reportArtifactUri,
        response_format: { type: "json_schema", schema_ref: "ossie://bca/metallurgical-finding.v2" },
      }),
    });

    if (response.status === 422 || response.status === 403) {
      const body = await response.text();
      throw ApplicationFailure.nonRetryable(body, "SchemaValidationError");
    }
    if (!response.ok) {
      throw new Error(`Erreur transitoire passerelle LLM : HTTP ${response.status}`);
    }

    return (await response.json()) as {
      rootCauseCode: string;
      estimatedRepairCostCad: number;
      summaryClaimCheckUri: string;
    };
  } finally {
    clearInterval(hb);
  }
}

export async function placeProvisionalReserveMcp(params: {
  claimId: string;
  amountCad: number;
}): Promise<{ reservationId: string }> {
  const idempotencyKey = deriveDeterministicIdempotencyKey("bca-guidewire-reserve");
  const mcpReply = await invokeBorealMcpTool<{ reservationId: string }>(
    "mcp://bca-guidewire-ledger/reserve_claim_provision",
    {
      idempotencyKey,
      claimId: params.claimId,
      amountCad: params.amountCad,
      currency: "CAD",
    }
  );
  return mcpReply;
}

declare function invokeBorealMcpTool<T>(uri: string, args: Record<string, unknown>): Promise<T>;
```

#### Extrait 18.3 — Micro-orchestration sans serveur sous Restate avec *Virtual Object*, ctx.run et awakeable

Pour les flux opérationnels rapides (T2/T3), où un exécutant permanent par file serait disproportionné, cet extrait Restate montre un Virtual Object indexé par le numéro de série d'un compresseur. Il sérialise les alertes concurrentes, journalise l'appel d'un SLM via `ctx.run`, puis libère la fonction sans serveur grâce à `ctx.awakeable` jusqu'au retour du diagnostic terrain A2A. Cet état clé-valeur (`ctx.get`, `ctx.set`) est celui d'un Virtual Object; la section 18.6 décrit plutôt, pour Restate, un journal rejoué où l'état voyage avec chaque requête, avec des services sans état.

``` typescript
import * as restate from "@restatedev/restate-sdk";

interface TelemetryAlert {
  readonly alertId: string;
  readonly harmonicPeakHz: number;
  readonly bearingTempCelsius: number;
}

interface FieldBenchCallback {
  readonly confirmedWearLevel: "NOMINAL" | "DEGRADED" | "CRITICAL";
  readonly inspectorSpiffeId: string;
}

export const equipmentTriageObject = restate.object({
  name: "bsn.equipmentTriage",
  handlers: {
    handleAnomaly: async (ctx: restate.ObjectContext, alert: TelemetryAlert) => {
      const serialNumber = ctx.key; // Verrouillage exclusif garanti par numéro de série

      const activeIncident = await ctx.get<string>("activeIncidentId");
      if (activeIncident) {
        return { status: "DEDUPLICATED", incidentId: activeIncident };
      }

      ctx.set("activeIncidentId", alert.alertId);
      try {
        // 1. Bloc journalisé : exécuté une seule fois même si le conteneur redémarre ensuite
        const triage = await ctx.run("slm-spectral-classification", async () => {
          const res = await fetch("https://agentgateway.internal.boreal.ca/v1/slm/classify", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ serialNumber, ...alert }),
          });
          if (!res.ok) throw new Error(`Échec SLM HTTP ${res.status}`);
          return (await res.json()) as { confidence: number; suspectComponent: string };
        });

        // 2. Si le doute persiste, création d'un Awakeable durable et mise en veille à 0 CPU
        if (triage.confidence < 0.90) {
          const { id: awakeableId, promise } = ctx.awakeable<FieldBenchCallback>();

          await ctx.run("delegate-a2a-deep-bench", async () => {
            await fetch("https://gateway.boreal.ca/a2a/bsn/acoustic-specialist", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                serialNumber,
                suspectComponent: triage.suspectComponent,
                callbackAwakeableId: awakeableId,
              }),
            });
          });

          // Suspension sur disque ; le bloc finally libère le verrou même en cas de TimeoutError
          const benchVerdict = await promise.orTimeout({ minutes: 45 });
          return { status: "RESOLVED_AFTER_AWAKEABLE", verdict: benchVerdict.confirmedWearLevel };
        }

        return { status: "RESOLVED_FAST_PATH", component: triage.suspectComponent };
      } finally {
        ctx.clear("activeIncidentId");
      }
    },
  },
});
```

#### Extrait 18.4 — Garde obligatoire de revalidation d'état et de mandat après réveil longue durée

Comme introduit au chapitre 1, après neuf jours d'attente d'un expert ou d'un souscripteur, le monde extérieur et les habilitations de sécurité ont pu changer. Les tenir pour figés est une vulnérabilité de type TOCTOU (*Time-of-Check to Time-of-Use*), dont la section 18.5 décrit la vérification. La fonction ci-dessous est la garde post-hibernation appelée dans l'Extrait 18.1. Elle vérifie cryptographiquement le jeton d'approbation CIBA et interroge en temps réel Microsoft Entra ID et le moteur Cedar pour confirmer que le souscripteur détient toujours son mandat au jour du décaissement. Elle contrôle aussi, sur le système maître, que la police n'a été ni suspendue ni frappée d'un gel antifraude pendant le sommeil du workflow.

``` typescript
export interface PostHibernationCheckInput {
  readonly claimId: string;
  readonly policyNumber: string;
  readonly approverSubjectId: string;
  readonly signedAssertionJwt: string;
  readonly expectedNetPayableCad: number;
}

export interface PostHibernationCheckResult {
  readonly canProceed: boolean;
  readonly blockingReason: string | null;
  readonly refreshedOboToken?: string;
}

export async function revalidateWorldStateAfterWakeup(
  input: PostHibernationCheckInput
): Promise<PostHibernationCheckResult> {
  // 1. Vérifier la signature CIBA et l'habilitation active de l'approbateur AU MOMENT DU RÉVEIL
  const iamCheck = await verifyActiveMandateAndExchangeObo({
    subjectId: input.approverSubjectId,
    cibaJwt: input.signedAssertionJwt,
    targetScope: "bca.claims.settle_high_value",
    amountCad: input.expectedNetPayableCad,
  });

  if (!iamCheck.active || !iamCheck.delegatedToken) {
    return {
      canProceed: false,
      blockingReason: `Mandat approbateur révoqué, expiré ou hors plafond (${iamCheck.reason})`,
    };
  }

  // 2. Relire l'état frais du System of Record (détection de dérive TOCTOU pendant le sommeil)
  const livePolicy = await fetchLivePolicySnapshotMcp(input.policyNumber);

  if (livePolicy.status !== "ACTIVE_IN_FORCE") {
    return {
      canProceed: false,
      blockingReason: `Statut police modifié durant la mise en veille : ${livePolicy.status}`,
    };
  }
  if (livePolicy.fraudFreezeFlag) {
    return {
      canProceed: false,
      blockingReason: "Gel conformité / antifraude activé sur le dossier depuis l'instruction initiale",
    };
  }
  if (livePolicy.remainingAnnualAggregateCad < input.expectedNetPayableCad) {
    return {
      canProceed: false,
      blockingReason:
        `Plafond annuel résiduel insuffisant (${livePolicy.remainingAnnualAggregateCad} CAD ` +
        `disponibles pour ${input.expectedNetPayableCad} CAD requis — sinistre concurrent réglé entre-temps)`,
    };
  }

  return {
    canProceed: true,
    blockingReason: null,
    refreshedOboToken: iamCheck.delegatedToken,
  };
}

declare function verifyActiveMandateAndExchangeObo(args: Record<string, unknown>): Promise<{
  active: boolean;
  reason?: string;
  delegatedToken?: string;
}>;
declare function fetchLivePolicySnapshotMcp(policyNumber: string): Promise<{
  status: string;
  fraudFreezeFlag: boolean;
  remainingAnnualAggregateCad: number;
}>;
```

Le troisième contrôle métier (`remainingAnnualAggregateCad`) couvre un cas limite : pendant que le sinistre A attendait neuf jours la signature d'un expert, un sinistre B plus rapide sur la même police a pu consommer le plafond annuel de couverture. Sans cette revalidation au réveil, l'agent décaisserait au-delà de ce que le contrat prévoit.

---

## 18.11 Ingénierie opérationnelle des cycles longs : évolution, compactage et confidentialité du journal

Sur des dizaines de milliers de sagas simultanées, trois disciplines d'exploitation prolongent la section 18.2.

### Prévenir les erreurs de non-déterminisme

Le rejeu applique le code actuel aux événements passés. Supprimer un appel d'activité ou inverser l'ordre de deux promesses rompt donc la correspondance entre le code et les journaux des instances en cours : le runtime lève une exception protectrice (`NonDeterminismError`) et gèle la progression du dossier jusqu'au déploiement d'un correctif. Deux règles évitent ce risque :

- Toute modification structurelle d'un workflow actif passe soit par une barrière de version explicite (`patched("id-changement")` dans l'Extrait 18.1), soit par l'affectation d'exécution par version de build (*Worker Versioning / Build IDs*). Celle-ci route les anciens dossiers vers les exécutants de la version v2.3 jusqu'à leur extinction naturelle et aiguille les nouveaux dossiers vers la version v2.4.
- Le pipeline CI/CD comprend un test de rejeu automatisé (`WorkflowReplayer`), qui met en œuvre la vérification de compatibilité de rejeu évoquée à la section 18.2. Il télécharge un échantillon d'historiques JSON réels (chiffrés ou synthétiques) des trente derniers jours et vérifie en quelques secondes que la nouvelle branche Git les rejoue sans divergence.

### Compactage d'historique et hygiène d'état

Dans Temporal, par exemple, aucune limite de durée n'est imposée à une exécution (section 18.1), mais l'état grossit : Continue-As-New poursuit l'exécution dans un nouveau maillon de la même chaîne (section 18.2). Un agent jumeau permanent, qui surveille une turbine industrielle vingt-quatre heures sur vingt-quatre, ne doit donc pas boucler indéfiniment (`while (true)`) dans la même exécution.

Tous les $M$ événements (typiquement $M = 1\,000$ transitions ou une fois par période de vingt-quatre heures), le workflow invoque atomiquement la primitive Continue-As-New. Le moteur clôt le journal courant pour l'archivage à froid et instancie une exécution neuve, qui garde le même `WorkflowId`. Il lui transmet seulement l'objet d'état canonique distillé, par exemple 4 Ko de compteurs, de pointeurs vers le graphe bi-temporel Graphiti et de baux actifs. La dette de rejeu technique et la dérive d'accumulation contextuelle sont ainsi purgées.

### Immuabilité du journal et droit à l'oubli (Loi 25 et RGPD)

Le moteur exige un journal immuable pour le rejeu, alors que la Loi 25 au Québec et l'article 17 du RGPD imposent de pouvoir supprimer ou anonymiser les renseignements personnels d'un individu, sur demande légitime ou à l'échéance de rétention. La contradiction n'est qu'apparente. Deux mécanismes conjoints la résolvent :

1.  **Aucun renseignement personnel brut dans les arguments d'orchestration** : le workflow ne manipule que des identifiants pseudonymisés (`subjectRef: "SUBJ-88412"`) et des pointeurs vers le coffre documentaire gouverné.
2.  **Chiffrement par enveloppe et effacement cryptographique** : un Payload Codec client chiffre chaque charge utile d'événement en AES-256-GCM, avec une clé de données dérivée par client et par dossier, logée dans le KMS souverain de l'entreprise. Quand le droit à l'effacement s'exerce après la clôture légale du dossier, la destruction de cette clé rend indéchiffrables les octets archivés dans les journaux historiques. L'intégrité de la chaîne d'audit et la conformité à la vie privée sont ainsi conciliées.

---

## 18.12 Application au fil rouge et éclairages sectoriels

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Dossier d'indemnisation bris de machine sur 14 jours chez BCA**
:::

**Processus ciblé** : instruction de bout en bout d'un sinistre majeur d'assurance bris de machine (185 000 \$ CAD), à la suite de la rupture de l'arbre principal d'une presse d'emboutissage chez un équipementier automobile ontarien assuré par Boréal Capital & Assurances (BCA).

**Situation antérieure et échec du premier prototype (fin 2026)** : un tel dossier s’étalait sur 29 jours calendaires en médiane, car il dépend d'un rapport métallurgique externe, de vérifications sur les contrats patrimoniaux IBM i (AS/400), d'une contre-expertise tarifaire des pièces avec Boréal Équipements & Logistique (BEL) et de la signature formelle d'un souscripteur principal habilité au-delà de 100 000 \$ CAD. Un premier prototype, construit à l'automne 2026 sur un graphe d'agents Python à points de contrôle simples, a connu deux incidents en recette. Lors d'une mise à jour du conteneur au Jour 4, trois dossiers de test ont réexécuté leur étape de réservation comptable sur l'environnement Guidewire de pré-production. L'absence de revalidation au réveil a laissé passer un décaissement simulé sur une police résiliée entre-temps.

**Architecture durable déployée en production (T1–T2 2027 — Architecture bi-vitesse BCA / BSN)** : l'équipe plateforme du Groupe Boréal déploie un cluster Temporal régional canadien, réservé aux sagas T3/T4 (Montréal / Toronto en réplication synchrone, Payload Codec chiffré par des clés KMS canadiennes pour la conformité à la Loi 25). Restate assure en frontal, chez Boréal Services Numériques (BSN), la déduplication à la milliseconde des rafales télématiques (Extrait 18.3).

1.  **Jour 1 (00 h 00 — 00 h 04)** : à la réception de la déclaration et des photos préliminaires, Temporal démarre le workflow `bca-claim-2027-009412` (Extrait 18.1). L'extraction initiale, la lecture contractuelle encapsulée sur l'IBM i et l'inscription d'une provision prudente idempotente de 185 000 \$ CAD s'exécutent en 3 minutes et 40 secondes.
2.  **Jours 1 à 9 (hibernation à coût nul, déploiements sans effet)** : le dossier exige l'analyse du laboratoire métallurgique indépendant, et le workflow enregistre une attente durable. Pendant ces 9 jours, l'instance consomme 0 millicœur de CPU et 0 Mo de RAM sur les exécutants Kubernetes. Au Jour 5, l'équipe BCA déploie deux mises à jour logicielles (dont l'ajout de la garde `patched("bca-2027-04-post-hibernation-guard")`) et subit un redémarrage planifié de nœuds infonuagiques : aucun des 1 420 dossiers de sinistres actifs en sommeil n'est perturbé.
3.  **Jour 10 (réception du rapport, cellule critique, escalade CIBA)** : le webhook signé du laboratoire dépose le rapport PDF dans le coffre et réveille le workflow. La cellule *Exécuteur–Critique* de BCA (chapitre 16) relève un facteur d'usure normale qui ramène l'indemnité nette admissible à 162 400 \$ CAD. Elle transmet au souscripteur principal une demande d'approbation CIBA accompagnée d'un comparatif visuel A2UI.
4.  **Jours 13 et 14 (relance, revalidation TOCTOU, règlement)** : après une relance automatique au Jour 13, le souscripteur signe cryptographiquement sa validation le Jour 14 à 09 h 12. La garde post-hibernation (Extrait 18.4) confirme en 420 millisecondes que le mandat du souscripteur est actif dans Entra ID, que la police est en règle et que le plafond annuel résiduel couvre les 162 400 \$ CAD. La provision est ensuite ajustée et le virement définitif émis.

**Résultats homologués devant le comité des risques (BSIF E-23)** :

- Zéro doublon transactionnel et 100 % de survie sur 18 déploiements applicatifs réalisés en heures ouvrables.
- Temps de cycle médian des sinistres lourds ramené de 29 jours à 13,5 jours (96 % du temps correspond aux délais physiques externes de laboratoire et de réparation).
- Piste d'audit déterministe exportable en un clic, qui reconstitue chaque entrée, version de modèle, clé d'idempotence et jeton d'approbation CIBA du Jour 1 au Jour 14.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Assurance & Crédit Hypothécaire — Orchestrer des dossiers de 30 à 90 jours entre expiration de pièces, blocage de taux et BSIF E-23**
:::

L'octroi d'un prêt hypothécaire résidentiel ou commercial au Canada s'étale typiquement de 30 à 90 jours, de la pré-qualification initiale au décaissement chez le notaire, en passant par la levée des conditions d'inspection, l'évaluation agréée du bien immobilier et la vérification des avis de cotisation fiscale.

Sur cet horizon, chaque preuve documentaire a sa propre date de péremption réglementaire : un blocage de taux d'intérêt expire à 90 jours, une attestation d'emploi à 30 jours, et une cote de bureau de crédit peut se dégrader si l'emprunteur contracte un prêt automobile deux semaines avant la signature notariale. Les institutions financières canadiennes soumises à la ligne directrice BSIF E-23 modélisent donc chaque dossier hypothécaire comme un workflow durable maître, entouré de minuteries parallèles de validité documentaire :

- Tant que les pièces arrivent au fil de l'eau, des exécutants d'extraction (SLM / LLM documentaires) vérifient la cohérence croisée des revenus et n'immobilisent aucune ressource entre deux envois du courtier.
- Si l'acte notarié est repoussé au Jour 42, une minuterie durable invalide l'attestation d'emploi échue, abaisse le statut d'avancement du dossier et déclenche une demande ciblée de talon de paie récent par le portail courtier A2UI.
- Quarante-huit heures avant le décaissement final des fonds en fidéicommis, une garde de revalidation pré-clôture réinterroge les listes de sanctions et recalcule les ratios d'amortissement (ABD/ATD) sur la version exacte de la politique de crédit en vigueur.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Santé & Recherche Clinique — Parcours longitudinaux multi-mois, immuabilité du journal et effacement cryptographique (Loi 25 / RGPD)**
:::

Dans l'orchestration des parcours de soins oncologiques ou le suivi d'essais cliniques multicentriques de Phase III s'étendant sur 6 à 24 mois, des agents spécialisés assistent les coordonnateurs de recherche. Ils planifient les examens d'imagerie aux fenêtres protocolaires exactes (J+28, J+84, J+168), détectent tôt les effets indésirables déclarés par le patient et préparent les formulaires de pharmacovigilance.

Ce domaine cumule deux contraintes : aucune tolérance à la perte d'échéance (manquer une fenêtre biologique invalide le point de mesure statistique de l'essai) et une protection stricte des renseignements de santé (Loi sur les renseignements de santé et de services sociaux et Loi 25 au Québec, RGPD en Europe, HIPAA aux États-Unis). L'architecture durable déployée dans les réseaux hospitaliers universitaires repose sur :

1.  Des moteurs durables auto-hébergés sur une infrastructure souveraine certifiée santé, avec Continue-As-New à chaque cycle thérapeutique mensuel.
2.  Une séparation par jeton d'anonymisation : le journal durable ne contient que le code d'inclusion clinique (TRIAL-ONC-4419) et les horodatages protocolaires. Tout retrait de consentement d'un participant déclenche à la fois l'annulation, immédiate et prouvable, de toutes les minuteries futures du workflow et l'effacement cryptographique des charges utiles transitoires hors du dossier médical légal.
::::

---

## 18.13 Décision d’architecture normative et liste de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-012 — Architecture bi-vitesse d'exécution durable (Temporal + Restate) et revalidation obligatoire post-hibernation**
:::

- **Statut** : acceptée \| Périmètre : tous les flux agentiques asynchrones ou mutatifs (L2 à L4, régimes T2 à T4) \| Révision : annuelle
- **Contexte** : l'exécution d'agents multi-étapes dans des processus applicatifs sans état, ou sur les seuls points de contrôle de bibliothèques conversationnelles, provoque des pertes de contexte lors des redéploiements Kubernetes, des doubles appels d'inférence coûteux, des écritures dupliquées dans les progiciels centraux et des failles TOCTOU après l'attente d'une approbation humaine.
- **Options évaluées** :
  1.  *Points de contrôle ad hoc par cadriciel Python/TS sur PostgreSQL* : rejetée. Cette option ne résout ni l'idempotence atomique des effets de bord en vol, ni les minuteries distribuées à l'échelle, ni le versionnage sûr du code sur les dossiers de longue durée.
  2.  *Runtime propriétaire d'un hyperscaler unique pour tout centraliser* : rejetée comme standard global, pour son coût de sortie élevé et son incompatibilité avec les exigences de portabilité hybride Canada / Europe et d'ateliers industriels sur site.
  3.  *Socle d'exécution durable ouvert à deux vitesses (Temporal pour les sagas métier T3/T4, Restate pour la micro-orchestration à haute cadence T2/T3)* : retenue, avec dérogation encadrée vers Durable Task pour les charges exclusivement internes `.NET`/Azure.
- **Décision** :
  1.  Tout flux agentique qui dépasse 30 secondes, enchaîne plus d'une mutation externe ou comporte une attente asynchrone (CIBA, webhook A2A) s'exécute sur un moteur durable homologué. Temporal (fédéré par Temporal Nexus entre divisions) sert les processus critiques de plusieurs jours; Restate sert les objets virtuels par équipement et l'orchestration légère sans serveur.
  2.  Tout appel LLM, MCP ou A2A se place du côté activité (Activity / `ctx.run`) et transmet une clé d'idempotence dérivée par HMAC du couple `(workflowId, stepSequenceId)`.
  3.  Toutes les charges utiles persistées dans les journaux durables sont chiffrées côté client (AES-256-GCM), sans donnée personnelle brute (Loi 25 / RGPD).
  4.  Toute sortie de mise en veille de plus de 15 minutes exécute une activité dédiée de revalidation du mandat IAM et de l'état frais du système d'enregistrement avant toute mutation aval.
- **Conséquences** :
  - *Positives* : résilience aux pannes matérielles et aux déploiements continus, coût CPU nul pendant les attentes humaines de plusieurs semaines, fin des doubles facturations d'inférence et piste d'audit (BSIF E-23).
  - *Négatives / coûts assumés* : apprentissage par les développeurs des règles de déterminisme du code de workflow, tests `WorkflowReplayer` obligatoires en CI/CD et exploitation du service de clés KMS pour le Payload Codec.
- **Condition de révision** : réévaluation annuelle selon la convergence d'interopérabilité des standards CloudEvents et des moteurs durables sans serveur.
::::

### Liste de contrôle de mise en production

Huit points à valider avant d'étendre les workflows durables aux transactions multi-systèmes compensables par chorégraphie (chapitre 19) :

1.  **Pureté déterministe vérifiée** : les fichiers de définition de workflow sont-ils exempts d'appel réseau direct, de lecture d'horloge système non interceptée, de génération aléatoire et de dépendance globale mutable ?
2.  **Tests de rejeu en intégration continue** : le pipeline CI/CD bloque-t-il toute demande de fusion qui provoque une `NonDeterminismError` sur le corpus d'historiques récents de production ?
3.  **Clés d'idempotence de bout en bout** : chaque activité mutative (MCP ou A2A) dérive-t-elle sa clé d'idempotence de l'identifiant d'exécution et du numéro de séquence du journal, plutôt que d'un UUIDv4 aléatoire régénéré à chaque nouvel essai ?
4.  **Classification des exceptions** : les erreurs définitives (rejet de politique Cedar, schéma invalide, autorisation refusée) sont-elles marquées non réessayables (`nonRetryable`), pour éviter de nouveaux essais inutiles ?
5.  **Mise en veille réelle** : les attentes d'approbation humaine CIBA ou de partenaires externes passent-elles exclusivement par des signaux durables et des `awakeables`, sans bloquer de fil d'exécution (`sleep` système et scrutation active interdits) ?
6.  **Garde de revalidation post-hibernation (TOCTOU)** : tout réveil après une suspension de plus de 15 minutes revérifie-t-il l'habilitation active de l'approbateur et l'état courant des entités métier avant l'action finale ?
7.  **Compactage Continue-As-New planifié** : les workflows de longue durée ou récurrents purgent-ils périodiquement leur historique d'événements, en ne transférant qu'un résumé d'état borné ?
8.  **Chiffrement client et effacement cryptographique** : un Payload Codec chiffre-t-il les entrées et sorties journalisées avec des clés sous contrôle de l'entreprise, et aucun renseignement personnel direct n'apparaît-il en clair dans les identifiants de workflow ni dans les métadonnées de recherche ?
