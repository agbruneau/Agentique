## Mise en œuvre — Maillage événementiel asynchrone et patron Saga à compensation {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Quand le travail dure plus longtemps qu’une connexion, que plusieurs consommateurs doivent réagir au même fait ou qu’il faut absorber des pointes de charge (section 19.1 et grille de décision), relier des agents autonomes par des appels synchrones bloquants reproduit les fragilités des architectures point-à-point : couplage temporel, tempêtes de réessais quand l’inférence ralentit, états métier incohérents quand une étape aval échoue après des écritures amont déjà validées. L’entreprise agentique repose alors sur un maillage événementiel asynchrone (architecture événementielle agentique, EDAA) couplé au patron Saga à compensation. Hors de ces cas, l’appel direct reste l’option par défaut : aucune dorsale tant qu’un déclencheur direct suffit (grille de décision, après la section 19.7).
- **Décisions architecturales structurantes** :
  1.  *Irréversible à moyen terme* : Proscrire tout verrouillage transactionnel distribué (validation à deux phases, 2PC / XA) entre agents cognitifs; adopter un socle à deux composantes : routage dynamique à basse latence (Solace PubSub+) et journal immuable relisible (Apache Kafka / Confluent).
  2.  *Structurante dès le jour 1* : Classer chaque outil MCP mutatif et chaque délégation A2A v1.0 en quatre catégories (*compensable*, *pivot*, *réessayable*, *irréversible externe*), imposer le patron Transactional Outbox et confiner toute émission externe derrière un tampon à fenêtre de grâce.
  3.  *Réversible par conception* : Le choix des adaptateurs de capture des changements ou des courtiers périphériques (NATS JetStream) en bordure d’usine, tant que l’enveloppe canonique CloudEvents 1.0 est respectée.
- **Indicateurs de gouvernance associés** : Taux de convergence propre des sagas ($\ge 99,9\,\%$), délai de compensation au 95e centile, taux de dérive en file `SagaDeadLetter` ($< 0,1\,\%$) et zéro émission irréversible externe avant validation du point pivot.
::::

## 19.8 De la requête-réponse bloquante à l’architecture événementielle agentique (EDAA)

Le chapitre 18 traite l’avancement d’un flux individuel : un moteur d’exécution durable (Temporal, Restate) le préserve malgré les pannes et les attentes humaines. Deux problèmes d’urbanisation restent à résoudre : propager en temps réel des milliers de faits opérationnels sans coupler chaque producteur à chaque consommateur, et rétablir l’intégrité métier quand une transaction inter-divisions est annulée à mi-parcours.

Dans les premiers graphes multi-agents, l’invocation synchrone domine : l’agent A appelle l’agent B en HTTP, qui attend un serveur MCP C sollicitant un progiciel D. À mesure que le nombre de maillons $m$ croît, la disponibilité effective diminue selon le produit des disponibilités unitaires $a_i$ :

$$A_{\text{sync}}(m) = \prod_{i=1}^{m} a_i \ll \min_{i} a_i$$

Quand chaque maillon dépend d’un moteur d’inférence à latence variable et d’un progiciel aux fenêtres de maintenance propres, cette topologie produit trois pathologies.

1.  **Tempêtes de réessais** : Un quota HTTP 429 ou une lenteur de SAP bloque les appels amont; des réessais non coordonnés multiplient la charge au moment où le service aval tente de se rétablir.
2.  **Rigidité évolutive** : Greffer un agent critique d’audit ou un indexeur mémoriel (Graphiti) sur un flux existant oblige à modifier et à redéployer les agents producteurs.
3.  **Inadéquation au monde physique** : Les capteurs OPC UA, les avis EDI X12 et les écritures comptables sont des flux continus de faits, non des appels de procédure distante.

L’architecture événementielle agentique (EDAA) reprend le découplage de la section 19.1 : capteurs, progiciels et agents publient des faits métiers immuables sur un maillage gouverné; les agents abonnés filtrent ces faits selon leurs mandats NHI, agissent localement et publient en retour leurs résultats ou des signaux de compensation.

Deux formes de charge utile coexistent sur ce maillage, et le choix entre elles est délibéré.

- **Événement de notification mince** : Il signale seulement qu’une transition d’état a eu lieu sur un identifiant métier. Les consommateurs habilités relisent l’état frais par un serveur MCP, avec le contrôle d’accès appliqué à la source (« notifier, puis relire », section 19.6). Cette forme est obligatoire dès que l’événement touche des renseignements personnels soumis à la Loi 25 ou des clauses tarifaires confidentielles.
- **Transfert d’état porté par l’événement** (*Event-Carried State Transfer*, ECST) : Le message embarque la projection normalisée selon l’ontologie Apache Ossie dont les agents aval ont besoin. Il évite les tempêtes de lectures synchrones vers l’IBM i ou SAP S/4HANA quand une dizaine de travailleurs analytiques réagissent au même fait industriel.

![Architecture Événementielle Agentique (EDAA) combinant Solace PubSub+, Confluent Kafka et le cycle aller-retour d’une Saga à compensation avec Transactional Outbox et tampon d’actions irréversibles.](figures/fig-19-a-1.svg)

### Choix des courtiers : Kafka, Solace et NATS

En 2027, trois familles de courtiers jouent des rôles complémentaires. AGNTCY SLIM (chiffrement de bout en bout *Messaging Layer Security*) s’y ajoute quand des essaims d’agents échangent sur des réseaux non fiables.

- **Apache Kafka / Confluent (journal immuable et relecture dans le temps)** : Journal canonique des sagas, partitionné par clé métier (`equipmentSerialNumber` ou `sagaId`), dont l’ordre et la relecture sont décrits à la section 19.2. Il conserve l’historique sur des mois, alimente les pipelines de contexte (Apache Flink), fournit une piste d’audit chronologique opposable sous BSIF E-23 et permet de réexécuter un incident réel dans un bac à sable OpenEnv pour vérifier la non-régression d’un agent.
- **Solace PubSub+ (maillage dynamique *Event Mesh* et passerelle IT/OT)** : Là où Kafka emploie des sujets plats, Solace route les messages selon des hiérarchies arborescentes fines (jusqu’à 128 niveaux, ex. `boreal/bel/qc/mtl02/compressor/BOR-90441/vibration/critical`), évaluées avec jokers `*` et \> directement par le courtier. Un spécialiste peut souscrire aux seules alertes critiques québécoises sans ingérer le flux nominal européen. La traduction multiprotocole est native (MQTT Sparkplug, AMQP 1.0, REST, WebSockets).
- **NATS + JetStream (périphérie industrielle et micro-coordination)** : Binaire léger à latence sous la milliseconde, NATS convient aux usines sujettes aux coupures WAN et à la coordination de travailleurs d’extraction SLM par diffusion puis collecte des réponses.

| Dimension d’évaluation | Apache Kafka / Confluent | Solace PubSub+ (Event Mesh) | NATS + JetStream |
|:----------------|:----------------------------|:---------------------------|:---------------------------|
| Paradigme primaire | Journal distribué immuable à rétention longue | Maillage orienté routage dynamique et filtrage fin | Messagerie très légère de périphérie |
| Filtrage des sujets | Sujets plats; filtrage délégué aux consommateurs / Flink | Arborescence riche avec jokers évalués par le courtier | Hiérarchie par jetons (. / `*` / \>) rapide en mémoire |
| Protocoles natifs | Binaire Kafka + Kafka Connect / passerelle REST | Multiprotocole natif : MQTT, AMQP 1.0, JMS, REST, WSS | Protocole NATS sobre, support MQTT et WebSockets |
| Ordre et relecture d’audit | Ordre total par partition; relecture de longs historiques (E-23) | Files durables à acquittement fin; relecture bornée au tampon | Flux JetStream répliqués pour fenêtres tactiques |
| Latence p99 intra-zone | 5 à 25 ms (débit séquentiel élevé) | 0,5 à 5 ms (commutation fine à faible gigue) | 0,15 à 2 ms (empreinte minimale inter-conteneurs) |
| Rôle agentique optimal | Journal canonique des sagas, audit, mémoire et analytique | Collecte IT/OT, fédération multi-nuages, routage sélectif | Usines déconnectables, essaims locaux de travailleurs SLM |

Chez Groupe Boréal, Solace capte et filtre à basse latence les signaux OT et applicatifs aux frontières, puis déverse les événements qualifiés dans Kafka par un pont certifié, pour l’orchestration durable et l’audit réglementaire.

Le pont impose un choix de conception : la clé de partitionnement dans Kafka, puisque l’ordre n’est garanti qu’à l’intérieur d’une partition (section 19.2).

- Sur les sujets d’état d’actifs physiques ou contractuels (`bel.equipment.telemetry`, `bca.policy.lifecycle`), la clé est l’identifiant canonique de la ressource métier (BOR-CMP-90441) : une alerte de rétablissement ne peut pas être consommée avant l’alerte de panne qui l’a précédée de 200 millisecondes.
- Sur les sujets de coordination transactionnelle (`boreal.saga.commands`, `boreal.saga.compensations`), la clé est `aigovsagaid` : tous les jalons aller et retour d’une même saga sont sérialisés dans leur ordre causal, sans goulot global entre deux sagas indépendantes.
- Quand des événements franchissent le périmètre de l’entreprise vers un fournisseur logistique externe, la charge utile est encapsulée dans un groupe chiffré AGNTCY SLIM (protocole IETF *Messaging Layer Security*, RFC 9420) : même un courtier relais intermédiaire ne peut lire le contenu métier en clair.

---

## 19.9 Ingénierie de l’événement agentique : CloudEvents 1.0, Transactional Outbox et anti-tempête

Un bus asynchrone sans discipline transactionnelle déplace le désordre sans le résoudre. Trois mécanismes fiabilisent les échanges.

### 1. Éliminer la double écriture : Transactional Outbox et registre d’idempotence

Si un serveur MCP valide un COMMIT SQL de réservation de stock puis tente de publier `InventoryReserved` sur Kafka, un crash ou une coupure réseau entre les deux opérations laisse un stock bloqué sans événement émis. En production, ni un agent ni un serveur MCP ne publie directement sur le courtier à côté d’une écriture en base. La mutation métier et l’insertion dans la table `agent_outbox_events` s’exécutent dans la même transaction ACID locale. Une scrutation SQL périodique générerait une charge inutile : un connecteur de capture des changements (section 19.5) lit plutôt en continu le journal des transactions, Debezium sur le WAL PostgreSQL ou sur les journaux de réplication SAP / IBM i. Il extrait chaque ligne engagée en moins de 15 millisecondes et la publie sur le courtier avec une garantie « au moins une fois ».

Côté consommateur, chaque travailleur ou serveur MCP tient une table de déduplication transactionnelle indexée sur `aigovidempotencykey`. Elle conserve le statut d’exécution (`IN_PROGRESS`, `COMPLETED`) et l’empreinte de la réponse produite. Quand un rééquilibrage de groupe de consommateurs Kafka livre de nouveau un message déjà traité, l’agent restitue le résultat antérieur sans réinvoquer le modèle de langage ni doubler la réservation physique. Avec un registre de schémas (Schema Registry) qui impose la compatibilité ascendante et descendante stricte (*Full Transitive Compatibility*), une saga en veille pendant dix jours survit sans erreur de désérialisation au déploiement d’une nouvelle version d’agent.

### 2. Normaliser l’enveloppe : CloudEvents 1.0 et Claim-Check

Tous les messages adoptent la norme CNCF CloudEvents 1.0, enrichie des attributs de gouvernance agentique (`aigov*`). Pour les artefacts volumineux (liasses PDF, spectres vibratoires), l’émetteur applique le patron Claim-Check : le fichier chiffré réside dans un stockage objet immuable, et l’événement ne transporte que son URI avec une empreinte SHA-256 vérifiable. L’extrait 19.1 réunit l’enveloppe, le contrat de compensation et la référence Claim-Check.

#### Extrait 19.1 — Événement agentique normatif CloudEvents 1.0 avec gouvernance et *Claim-Check*

``` json
{
  "specversion": "1.0",
  "id": "evt-0195f3c8-8a14-7d20-9b41-6c02e4419a08",
  "source": "spiffe://boreal.ca/ns/bel-erp/sa/mcp-sap-inventory",
  "type": "ca.boreal.bel.inventory.part.reserved.v2",
  "subject": "equipment/BOR-CMP-90441/material/INJ-MOD-V12",
  "time": "2027-04-09T14:22:11.408Z",
  "datacontenttype": "application/json",
  "dataschema": "https://schemas.boreal.ca/ossie/v2/inventory-event.schema.json",
  "traceparent": "00-7d4e9a12b8c041559f0218a4c7103e21-89a1c402f1b30042-01",
  "aigovsagaid": "saga-inc-2027-119405",
  "aigovidempotencykey": "saga-inc-2027-119405:step-01:sap-reserve",
  "aigovautonomyceiling": "L3",
  "aigovhopremaining": 3,
  "aigovbudgetremainingcad": "1.05",
  "aigovinitiatingactor": "urn:boreal:iot:bsn-vibration-guardian-v4",
  "data": {
    "reservationDocumentNumber": "SAP-RES-4409812",
    "plantCode": "CA-QC-MIR-01",
    "materialCode": "INJ-MOD-V12",
    "reservedQuantity": 1,
    "unitValuationCad": 14800.00,
    "leaseExpiresAt": "2027-04-09T18:22:11Z",
    "compensationContract": {
      "classification": "COMPENSABLE",
      "mcpServer": "https://agentgateway.internal.boreal.ca/mcp/bel/sap-mm",
      "inverseToolName": "sap_release_spare_part_reservation",
      "correlationParameters": {
        "reservationDocumentNumber": "SAP-RES-4409812",
        "plantCode": "CA-QC-MIR-01"
      }
    },
    "diagnosticClaimCheck": {
      "artifactUri": "s3://boreal-telemetry/2027/04/09/fft-BOR-CMP-90441.parquet",
      "sha256Digest": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
      "encryptionKeyRef": "kms://ca-central-1/boreal-ot-cmk"
    }
  }
}
```

### 3. Prévenir les tempêtes cognitives auto-entretenues (OWASP ASI08)

Dans un maillage, deux agents abonnés au même objet peuvent entrer en résonance sans fin : l’un normalise une fiche, l’autre recalcule un score et republie l’événement. C’est l’explosion de tâches de la section 19.7. Trois verrous déterministes bloquent cette dérive : (a) la décrémentation obligatoire de `aigovhopremaining` à chaque réaction, qui route en quarantaine passive tout message tombé à 0; (b) le filtrage d’auto-causalité, qui ignore toute mutation émise par la même identité SPIFFE ou hors du sous-schéma surveillé; (c) l’isolation après trois échecs vers une file de lettres mortes sémantique (`.dlq`), pour ne jamais bloquer une partition Kafka.

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Transport aérien & Logistique — Sagas de réacheminement en perturbation majeure (IRROPS)**
:::

Quand un épisode de verglas ferme deux pistes d’un pivot aéroportuaire nord-américain (*Irregular Operations*, IRROPS), une compagnie aérienne et sa filiale cargo doivent recomposer en moins de vingt minutes des dizaines de rotations d’aéronefs, des équipages soumis aux limites légales de temps de service (Transports Canada / FAR Part 117) et des milliers d’expéditions pharmaceutiques sous chaîne du froid.

En 2027, les transporteurs de pointe remplacent les verrous centraux sur le système de services aux passagers (PSS) par un maillage Solace PubSub+ (télémétrie avionique ACARS et portes en temps réel) couplé à Kafka et Temporal :

1.  **Réservations spéculatives à bail court** : L’*Agent Fret Critique* bloque pour 15 minutes de la soute sur un vol partenaire A2A et un camion frigorifique sous douane, pendant que l’*Agent Équipage* vérifie la légalité des pilotes de réserve.
2.  **Compensation immédiate sur veto légal** : Si le contrôleur des temps de repos ou la douane refuse l’itinéraire au point pivot, la saga libère en moins de trois secondes la soute partenaire et le camion. La rétention fantôme de capacité, qui bloquait auparavant le réseau, disparaît.
::::

---

## 19.10 Le patron Saga en environnement probabiliste

Dès qu’un processus modifie plusieurs systèmes d’enregistrement autonomes (SAP, ServiceNow, Guidewire), le protocole de validation à deux phases (2PC / XA) est impraticable : les plateformes SaaS refusent les verrous externes, et un verrou exclusif maintenu pendant dix secondes d’inférence, ou quatre heures d’attente HOTL, bloquerait l’exploitation.

Le patron Saga (Garcia-Molina & Salem) remplace l’atomicité instantanée par une suite de transactions locales $T_1, \dots, T_n$, validées immédiatement et associées à des compensations inverses $C_i$. Toute saga bien formée s’ordonne autour d’une unique transaction pivot $T_p$ :

$$S = \langle T_1, \dots, T_{p-1}, T_p, T_{p+1}, \dots, T_n \rangle$$

Si une étape $T_k$ ($k \le p$) échoue ou essuie un refus de politique, le coordinateur dépile les compensations en ordre inverse strict (LIFO) :

$$\text{Comp}(S, k) = \langle C_{k-1}, C_{k-2}, \dots, C_1 \rangle$$

Le tableau fixe l’ordre des quatre classes d’effets de bord : étapes compensables, pivot unique (point de non-retour décisionnel), étapes réessayables dont la convergence est garantie, puis actions irréversibles externes sous tampon.

| Classe d’effet de bord | Position obligatoire | Propriété formelle | Exemples en entreprise | Exigence sur le serveur MCP / pair A2A |
|:-------------|:----------------|:----------------------|:----------------------|:------------------------|
| 1. Compensable | Avant le pivot ($T_1 \dots T_{p-1}$) | Annulable proprement par une opération inverse $C_i$ | Réservation temporaire SAP, blocage d’agenda technicien | Exposer l’outil inverse, un bail d’expiration (TTL) et l’idempotence |
| 2. Pivot | Bascule unique ($T_p$) | Son succès scelle l’engagement; son échec lance l’annulation | Adjudication de garantie BCA, validation CIBA, mandat AP2 | Atomicité stricte, contrôle complet des politiques Cedar/OPA |
| 3. Réessayable | Après le pivot ($T_{p+1} \dots T_n$) | Aucun refus métier possible; converge par réessai | Imputation analytique interne, mise à jour mémoire ou CRM | Idempotence sur `stepIdempotencyKey` |
| 4. Irréversible | Terminale sous tampon | Traverse la frontière physique ou juridique | Avis EDI externe, courriel client, consigne MES, virement | Passage obligatoire par un tampon à fenêtre de grâce |

### Contre-mesures au déficit d’isolation (ACD sans I) entre sagas concurrentes

Une saga ne fournit pas les garanties d’une transaction relationnelle ACID, mais seulement les garanties ACD : ses mutations intermédiaires sont visibles des autres agents avant que le pivot soit atteint. Deux sagas concurrentes sur le même équipement ou le même plafond de crédit client s’exposent à trois anomalies classiques : mises à jour perdues, lectures sales d’un état qu’une annulation défera trois secondes plus tard, et lectures non reproductibles. Trois contre-mesures s’appliquent au niveau des serveurs MCP.

1.  **Verrous sémantiques** : Toute étape compensable $T_i$ pose sur l’entité métier un indicateur visible d’état transitoire (`status = RESERVED_PENDING_SAGA`, avec `lockedBySagaId` et `leaseExpiresAt`). Un second agent qui inspecte la même pièce critique voit qu’un arbitrage est en cours : il attend l’expiration du bail court ou choisit un dépôt alternatif, au lieu d’écraser l’enregistrement.
2.  **Opérations commutatives** : Préférer, chaque fois que possible, des mutations additives ou soustractives (`debit_quota(delta)`) aux écritures d’écrasement absolu (`set_balance(valeur)`). Leur compensation inverse reste valide quel que soit l’ordre dans lequel d’autres sagas s’intercalent entre $T_i$ et $C_i$.
3.  **Réordonnancement pessimiste des risques** : Placer juste avant le pivot les étapes les plus exposées à la contention ou au rejet réglementaire, pour réduire la durée d’exposition des ressources verrouillées sémantiquement en amont.

### Compensation déterministe, compensation sémantique et orchestration hybride

La compensation déterministe invoque directement une API symétrique sans appel au modèle (`release_reservation`); elle est à privilégier. Dans les processus longs (T3/T4), l’état physique ou comptable peut toutefois changer entre $T_i$ et $C_i$ : une pièce réservée a déjà quitté son rayon d’entrepôt (prélèvement terminé), des frais contractuels de dédit s’appliquent, un taux de change a bougé. Quand l’API inverse signale cette dérive (`STATE_DRIFTED`), le coordinateur exécute un plan de remédiation sémantique pré-homologué (émission d’un bon de réintégration magasin ou d’un avoir sous plafond financier). Si l’écart dépasse la tolérance, il bascule en `SagaDeadLetter` vers un superviseur HOTL.

Dès qu’une transaction d’affaires traverse plusieurs agents, la chorégraphie pure sans coordinateur est proscrite : il faut un coordinateur (section 19.7). Sous régime réglementé (BSIF E-23), elle l’est même pour des réactions indépendantes, ce qui va au-delà de ce que retient la section 19.7 : la chorégraphie y garde sa place quand les réactions sont indépendantes, sans annulation ni ordre requis. Le bus diffuse les faits découplés, comme à la section 19.7, et un coordinateur explicite (Temporal / Restate) pilote l’orchestration durable : il persiste chaque contrat inverse *avant* d’émettre l’action aller, par enregistrement préalable de la compensation. En contrepartie, toute API inverse $C_i$ traite comme un succès idempotent l’absence d’enregistrement (`ALREADY_ABSENT`), quand un délai d’attente réseau ambigu a interrompu $T_i$ avant son exécution réelle. Tout échec survenant *après* le pivot $T_p$ bascule en recouvrement avant, non en annulation, qui serait illégale à ce stade. L’extrait 19.2 implémente ce coordinateur : pile LIFO déterministe, enregistrement préalable, remédiation sémantique plafonnée, escalade en `SagaDeadLetter`.

#### Extrait 19.2 — Coordinateur TypeScript de Saga avec pile LIFO déterministe et sémantique

``` typescript
export type StepKind = "COMPENSABLE" | "PIVOT" | "RETRIABLE";

export interface CompensationPlan {
  readonly stepName: string;
  readonly deterministicUndo: (idempotencyKey: string) => Promise<{
    status: "COMPENSATED" | "STATE_DRIFTED";
    driftReason?: string;
  }>;
  readonly semanticRemediation?: (
    driftReason: string,
    idempotencyKey: string
  ) => Promise<{ status: "REMEDIATED"; adjustmentCostCad: number }>;
}

export interface SagaStep<TResult> {
  readonly name: string;
  readonly kind: StepKind;
  readonly forwardAction: (idempotencyKey: string) => Promise<TResult>;
  readonly buildCompensation?: () => CompensationPlan;
}

export interface DurableSagaJournal {
  persistAhead(sagaId: string, plan: CompensationPlan): Promise<void>;
  recordEvent(sagaId: string, event: string, meta: Record<string, unknown>): Promise<void>;
  escalateDeadLetter(sagaId: string, stepName: string, error: string): Promise<void>;
}

export class AgenticSagaCoordinator {
  private readonly compensationStack: CompensationPlan[] = [];
  private pivotPassed = false;

  constructor(
    private readonly sagaId: string,
    private readonly maxDriftCad: number,
    private readonly journal: DurableSagaJournal
  ) {}

  public async executeStep<TResult>(step: SagaStep<TResult>): Promise<TResult> {
    if (this.pivotPassed && step.kind === "COMPENSABLE") {
      throw new Error(`Invariant violé [${this.sagaId}] : étape compensable interdite après pivot.`);
    }
    if (step.kind === "COMPENSABLE") {
      if (!step.buildCompensation) throw new Error(`Compensation manquante sur '${step.name}'.`);
      const plan = step.buildCompensation();
      // Enregistrement préalable sur disque AVANT l'appel réseau aller (couvre les timeouts ambigus)
      await this.journal.persistAhead(this.sagaId, plan);
      this.compensationStack.push(plan);
    }

    try {
      const res = await step.forwardAction(`${this.sagaId}:fwd:${step.name}`);
      if (step.kind === "PIVOT") this.pivotPassed = true;
      await this.journal.recordEvent(this.sagaId, "STEP_OK", { step: step.name, kind: step.kind });
      return res;
    } catch (err) {
      const reason = err instanceof Error ? err.message : String(err);
      if (!this.pivotPassed) {
        await this.unwindCompensations(reason);
      } else {
        await this.journal.escalateDeadLetter(
          this.sagaId,
          step.name,
          `Recouvrement avant requis après pivot : ${reason}`
        );
      }
      throw err;
    }
  }

  private async unwindCompensations(reason: string): Promise<void> {
    await this.journal.recordEvent(this.sagaId, "ROLLBACK_START", { reason });
    let driftCad = 0;

    while (this.compensationStack.length > 0) {
      const plan = this.compensationStack.pop()!;
      const undoKey = `${this.sagaId}:undo:${plan.stepName}`;
      try {
        const res = await plan.deterministicUndo(undoKey);
        if (res.status === "COMPENSATED") continue;

        if (!plan.semanticRemediation) throw new Error(`Dérive non couverte : ${res.driftReason}`);
        const sem = await plan.semanticRemediation(res.driftReason ?? "DRIFT", `${undoKey}:sem`);
        driftCad += sem.adjustmentCostCad;
        if (driftCad > this.maxDriftCad) {
          throw new Error(`Écart sémantique (${driftCad} CAD) supérieur au plafond (${this.maxDriftCad} CAD)`);
        }
      } catch (compErr) {
        const msg = compErr instanceof Error ? compErr.message : String(compErr);
        await this.journal.escalateDeadLetter(this.sagaId, plan.stepName, msg);
        throw compErr;
      }
    }
  }
}
```

---

## 19.11 Confinement des actions irréversibles : tampon à fenêtre de grâce et coupe-circuit

Aucune API ne permet de « rappeler » un courriel client déjà lu, un avis d’expédition EDI X12 856 transmis à un transporteur routier, une consigne d’usinage envoyée à un MES ou un virement AP2/x402. Un méta-gouverneur d’audit ou une sonde de détection d’intrusion (OWASP ASI01/ASI02) fonctionne souvent en inspection parallèle asynchrone, avec quelques secondes de décalage. Dans un système multi-agents, émettre instantanément vers l’extérieur crée alors une vulnérabilité irrécupérable.

Toute architecture L3/L4 interpose par conséquent, devant ses connecteurs de sortie externes, un tampon à fenêtre de grâce adossé à une table transactionnelle durable. L’intention scellée est retenue pendant une durée calibrée sur la criticité métier (typiquement 60 à 300 secondes, ou jusqu’à réception d’une contresignature cryptographique de l’*Agent Critique* indépendant). Durant cette fenêtre, le tampon écoute les événements d’annulation (`ca.boreal.saga.aborted`) et de révocation d’identité SPIFFE; à l’échéance, il réévalue la politique Cedar/OPA juste-à-temps avant de sceller l’émission externe. L’extrait 19.3 en donne l’implémentation.

#### Extrait 19.3 — Tampon Python asynchrone à fenêtre de grâce pour sorties irréversibles

``` python
from __future__ import annotations
import asyncio
from dataclasses import dataclass
from typing import Awaitable, Callable, Protocol

class PolicyGuard(Protocol):
    async def authorize_jit(self, saga_id: str, spiffe_id: str, action_type: str) -> bool: ...

class SealedEgressConnector(Protocol):
    async def send_external(self, idempotency_key: str, payload: dict) -> str: ...

@dataclass(frozen=True)
class StagedEgressAction:
    action_id: str
    saga_id: str
    spiffe_id: str
    action_type: str
    grace_seconds: int
    payload: dict

class IrreversibleOutboxBuffer:
    def __init__(self, guard: PolicyGuard, connector: SealedEgressConnector) -> None:
        self._guard = guard
        self._connector = connector
        self._aborts: dict[str, dict[str, asyncio.Event]] = {}
        self._aborted_sagas: set[str] = set()

    def trigger_abort(self, saga_id: str) -> None:
        self._aborted_sagas.add(saga_id)
        for ev in self._aborts.get(saga_id, {}).values():
            ev.set()

    async def stage_and_release(
        self,
        item: StagedEgressAction,
        audit: Callable[[str, str], Awaitable[None]],
    ) -> str | None:
        if item.saga_id in self._aborted_sagas:
            await audit(item.saga_id, f"PURGED_PRE_ABORTED:{item.action_id}")
            return None

        abort_ev = asyncio.Event()
        self._aborts.setdefault(item.saga_id, {})[item.action_id] = abort_ev
        await audit(item.saga_id, f"STAGED:{item.action_id}")

        try:
            await asyncio.wait_for(abort_ev.wait(), timeout=float(item.grace_seconds))
            await audit(item.saga_id, f"PURGED_ON_ABORT:{item.action_id}")
            return None
        except asyncio.TimeoutError:
            if item.saga_id in self._aborted_sagas:
                await audit(item.saga_id, f"PURGED_ON_ABORT:{item.action_id}")
                return None
            if not await self._guard.authorize_jit(item.saga_id, item.spiffe_id, item.action_type):
                await audit(item.saga_id, f"BLOCKED_JIT_POLICY:{item.action_id}")
                return None
            key = f"{item.saga_id}:egress:{item.action_id}"
            ext_ref = await self._connector.send_external(key, item.payload)
            await audit(item.saga_id, f"DISPATCHED:{ext_ref}")
            return ext_ref
        finally:
            if saga_waiters := self._aborts.get(item.saga_id):
                saga_waiters.pop(item.action_id, None)
                if not saga_waiters:
                    self._aborts.pop(item.saga_id, None)
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur Financier & Assurance — Contre-passation comptable immuable sous BSIF E-23**
:::

Dans une institution financière ou un assureur soumis aux normes IFRS 17 et à la ligne directrice BSIF E-23 (1er mai 2027), la compensation d’une étape comptable obéit à un interdit : aucune écriture inscrite au journal auxiliaire ou au grand livre ne peut être modifiée ni supprimée (DELETE).

Quand une saga d’indemnisation inscrit en $T_1$ une provision technique de 8 500 \$ CAD dans Guidewire, puis s’interrompt au pivot $T_p$ à la suite de la détection d’un doublon contractuel, l’outil MCP de compensation $C_1$ génère une écriture de contre-passation miroir horodatée. Elle porte la référence `reversesEntryId` ainsi que l’identifiant du modèle et de la règle déclenchante, ce qui préserve la piste d’audit devant le régulateur.
::::

---

## 19.12 Application au fil rouge : annulation inter-divisions chez Groupe Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Autopsie d'une annulation inter-divisions sur refus de conformité BCA**
:::

**Incident réel (`saga-inc-2027-119405`)** : Un vendredi à 14 h 22, un compresseur industriel installé chez un client aéronautique à Mirabel émet sur MQTT Sparkplug une alerte critique d’injection. Solace PubSub+ la capte, le pont la transmet à Confluent Kafka, et elle instancie un workflow Temporal piloté par `AgenticSagaCoordinator`.

**Phase aller compensable (1,9 seconde)** :

1.  **Étape $T_1$ — Stocks Boréal Équipements & Logistique (BEL, SAP S/4HANA)** : Après enregistrement préalable de $C_1$, l’*Agent Stocks* réserve l’unique module d’injection INJ-MOD-V12 de l’Est canadien (14 800 \$ CAD, bail 4 h). La table Transactional Outbox valide SAP-RES-4409812 et publie l’extrait 19.1.
2.  **Étape $T_2$ — Terrain Boréal Services Numériques (BSN, ServiceNow FSM)** : Blocage du créneau de 17 h 00 d’un électromécanicien haute tension et d’un camion-atelier (FSM-HOLD-88210). Aucune confirmation client n’est émise avant le pivot.

**Refus au point pivot $T_p$ chez Boréal Capital & Assurances (BCA, 14 h 29)** :

- L’*Agent Garantie* BCA relève sur l’IBM i (AS/400) deux verrous bloquants : le coût (14 800 \$ CAD) dépasse le plafond L3 (5 000 \$ CAD dans Cedar), et le client accuse un impayé litigieux de 94 jours qui suspend la couverture gratuite.
- Sollicitée par escalade asynchrone CIBA / A2UI, la souscriptrice BCA refuse la prise en charge sous garantie et exige un bon de commande prépayé.

**Annulation automatique en ordre LIFO (3,8 secondes)** :

1.  **Zéro fuite externe** : Le signal `ca.boreal.saga.aborted` interdit toute sortie du tampon; aucune promesse erronée de gratuité n’a été envoyée au client.
2.  **Compensation $C_2$ (ServiceNow FSM)** : `fsm_cancel_slot_allocation("FSM-HOLD-88210")` libère en 640 ms le technicien et le camion-atelier, aussitôt réaffectés à une urgence à Laval.
3.  **Compensation $C_1$ (SAP S/4HANA)** : `sap_release_spare_part_reservation("SAP-RES-4409812")` remet aussitôt le module INJ-MOD-V12 en stock disponible à la vente.
4.  **Rebond commercial** : L’événement de clôture déclenche dans Salesforce Agentforce la préparation d’une soumission d’intervention facturable, transmise au directeur de compte en deux minutes.

**Bilan T2 2027 (18 400 sagas)** : 99,94 % de convergence propre (validation ou annulation complète en 3,8 s médianes, 7,4 s au 99e centile); zéro stock fantôme dans SAP S/4HANA, contre une moyenne antérieure de 23 réservations bloquées par semaine; coût moyen d’orchestration d’une annulation inférieur à 0,002 \$ CAD (aucun appel au modèle durant le dépilement déterministe); 11 dossiers seulement (0,06 %) escaladés en `SagaDeadLetter`, à cause de dérives physiques d’entrepôt résolues en moins de quinze minutes par les superviseurs logistiques.
::::

---

## 19.13 Décision d’architecture normative et points de contrôle

Retenir le maillage hybride Solace/Kafka pour toute mutation touchant au moins deux systèmes d’enregistrement, comme le fait l’ADR-013, va au-delà de ce que retient l’exposé : la grille de décision (après la section 19.7) garde l’appel direct par défaut, sans dorsale tant qu’un déclencheur direct suffit, et réserve la dorsale à la relecture, aux pointes de charge ou aux consommateurs multiples.

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-013 — Maillage événementiel hybride Kafka/Solace et patron Saga à compensation sans 2PC**
:::

- **Statut** : Acceptée \| Périmètre : Fabrique Agentique d’Entreprise (BEL, BCA, BSN) \| Révision : Annuelle
- **Contexte** : Les flux inter-divisions traversent des progiciels hétérogènes (SAP, IBM i, Guidewire, ServiceNow, OT), avec des étapes d’inférence ou d’approbation HOTL incompatibles avec tout verrouillage synchrone.
- **Options évaluées** :
  1.  *Transactions distribuées (2PC / XA)* : Rejetée — indisponible sur les API SaaS et nuisible à la disponibilité des bases centrales.
  2.  *Chorégraphie pure sans coordinateur* : Rejetée — état global opaque, risque de tempêtes d’événements (ASI08) et auditabilité insuffisante sous BSIF E-23.
  3.  *Maillage hybride Solace/Kafka + Sagas orchestrées durablement* : Solace pour le filtrage temps réel IT/OT, Kafka (CloudEvents 1.0 et Outbox) comme journal immuable, coordinateur durable ordonné autour d’un point pivot, avec tampon pour les sorties irréversibles. Retenue.
- **Décision** : Toute mutation touchant au moins deux systèmes d’enregistrement s’exécute sous forme de Saga qui interdit les étapes compensables après le pivot, persiste $C_i$ avant $T_i$, utilise Transactional Outbox et isole les sorties externes derrière un tampon à fenêtre de grâce.
- **Conséquences** :
  - *Positives* : Découplage temporel, résilience aux pannes partielles, relecture d’audit exacte, disparition des réservations fantômes.
  - *Négatives / Coûts assumés* : Gestion explicite de la cohérence finale dans les interfaces AG-UI et développement systématique des outils inverses MCP.
- **Condition de révision** : Réexamen annuel selon l’évolution des standards d’événements de la Linux Foundation AAIF.
::::

### Liste de contrôle de mise en production

Avant d’homologuer un flux multi-agents asynchrone, vérifier les huit points suivants :

1.  **Ordre autour du pivot** : Toutes les étapes pouvant échouer pour cause métier précèdent-elles l’unique pivot $T_p$, ne laissant après lui que des opérations réessayables idempotentes ?
2.  **Enregistrement préalable** : Le descripteur `CompensationPlan` est-il persisté sur disque durable *avant* l’appel réseau de l’action aller $T_i$ ?
3.  **Compensation déterministe prioritaire** : Les annulations $C_i$ appellent-elles des API déterministes sans appel au modèle, les remédiations sémantiques bornées étant réservées aux dérives d’état avérées ?
4.  **Atomicité de la Transactional Outbox** : Les serveurs MCP passent-ils par une table d’envoi transactionnelle alimentée par capture des changements, sans double écriture non atomique ?
5.  **Enveloppe CloudEvents 1.0 et Claim-Check** : Les messages portent-ils `sagaId`, `idempotencyKey`, `hopRemaining` et `traceparent`, et les artefacts lourds transitent-ils par URI signée avec hachage SHA-256 ?
6.  **Baux d’expiration (TTL)** : Chaque réservation amont possède-t-elle un bail d’expiration autonome dans le système d’enregistrement, en cas de retard prolongé de l’annulation ?
7.  **Tampon sur sorties irréversibles** : Les connecteurs externes (EDI, courriel client, paiement, MES) vérifient-ils l’absence d’annulation et la politique Cedar juste avant l’émission ?
8.  **Tests de chaos sur l’annulation** : Tous les chemins $C_k \dots C_1$ et l’escalade `SagaDeadLetter` sont-ils testés par injection automatique de pannes en CI/CD ?
