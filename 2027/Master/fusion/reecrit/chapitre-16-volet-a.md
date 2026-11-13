## Mise en œuvre — Topologies d'orchestration et de chorégraphie multi-agents {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu** : multiplier les agents spécialisés sans gouverner leurs interactions fait croître la facture de jetons de façon quadratique, dilue la responsabilité réglementaire et multiplie les défaillances silencieuses en cascade (OWASP ASI08).
- **Décisions d’architecture** :
  1. *Irréversible à l’échelle de l’entreprise* : adopter un modèle cellulaire fédéré, avec une chorégraphie événementielle entre domaines d’affaires autonomes (Kafka, Solace) et une orchestration déterministe à l’intérieur de chaque domaine.
  2. *Normative dès la conception* : interdire en production tout graphe cyclique libre (« débat ouvert entre pairs ») et limiter les équipes aux six topologies canoniques homologuées, chacune avec des bornes dures de sauts, de budget et de temps.
  3. *Réversible par configuration* : l’affectation d’un modèle ou d’un agent spécialiste à un rôle topologique (exécuteur, critique, soumissionnaire), grâce au découplage par A2A v1.0 et Apache Ossie.
- **Indicateurs de gouvernance** : facteur d’amplification de jetons par transaction métier, nombre moyen et 99e centile de sauts entre agents par saga, taux de convergence au premier passage des boucles critiques, latence du chemin critique de bout en bout.
::::

## 16.9 Orchestration centralisée et chorégraphie décentralisée

La section 16.1 distingue les topologies centralisée et décentralisée. Avec dix ou cent agents spécialisés répartis sur plusieurs lignes d’affaires, le choix prend la forme du dilemme classique des systèmes distribués, que la nature probabiliste des modèles amplifie : confier la conduite du flux à un coordinateur central (orchestration), ou laisser chaque acteur réagir de façon autonome aux faits publiés sur un courtier d’événements (chorégraphie).

Entre 2024 et 2025, plusieurs cadriciels multi-agents expérimentaux ont retenu la « salle de réunion virtuelle » : les agents conversent dans un fil partagé jusqu’à dégager un consensus. C’est la forme libre du débat décrit à la section 16.4. L’interdiction que pose ce volet va au-delà de ce que retient l’exposé : le débat y est admis à trois agents au plus, en lecture seule, sous un gestionnaire qui décide qui parle (section 16.4 et grille de décision), et la section 16.5 traite le transfert et l’essaim comme des patrons valides. Sur une démonstration à trois tours, la formule séduit. Les mesures de Kim et coll. situent le coût de l’architecture décentralisée, à débat et consensus, à 26,1 tours par essai en moyenne, contre 27,7 pour l’architecture centralisée, avec une amplification d’erreurs de 7,8 fois, entre l’orchestrateur et les agents indépendants (sections 16.2 et 16.4). Le calcul qui suit décrit un modèle du maillage, non une mesure.

### Croissance quadratique des échanges et des jetons

Soit un ensemble de $n$ agents qui coopèrent sur un dossier complexe. Dans un maillage conversationnel non contraint, où chaque agent peut interpeller n’importe quel pair et reçoit l’historique complet des échanges, le nombre de canaux potentiels croît selon :

$$C(n) = \frac{n(n - 1)}{2} \in O(n^2)$$

La consommation de jetons d’entrée croît aussi de façon quadratique. Si chaque tour $t \in \{1, \dots, T\}$ ajoute en moyenne $L$ jetons au tampon conversationnel partagé, le volume cumulé de jetons facturés et traités par l’attention au bout de $T$ tours atteint :

$$V_{\text{jetons}}(T) = \sum_{t=1}^{T} (L_0 + t \cdot L) = T \cdot L_0 + \frac{T(T + 1)}{2} L$$

où $L_0$ désigne l’empreinte initiale des consignes système et des schémas d’outils. Au-delà de huit à dix échanges croisés, trois dégradations s’ajoutent :

1. **Érosion du rapport signal/bruit.** Une hypothèse erronée émise au tour 2 reste dans la fenêtre de contexte au tour 9 et continue d’influencer l’attention des agents aval, même réfutée.
2. **Contagion des rationalisations (OWASP ASI08).** Quand un agent amont énonce avec assurance une déduction inexacte, les agents pairs tendent statistiquement à s’aligner sur cette prémisse plutôt qu’à la contredire, par sycophantie entre modèles.
3. **Perte d’efficacité du cache KV.** Quand chaque agent a un préfixe système différent et réingère dans le désordre les interventions des autres, les moteurs d’inférence ne réutilisent plus les préfixes mis en cache. Le coût et le délai avant le premier jeton augmentent ensemble.

### Dualité : gouverner localement, fédérer globalement

Le principe de dualité échelle-couplage du *Domain-Driven Design* (DDD) écarte à la fois le maillage libre et l’orchestrateur monolithique omniscient qui régenterait toute l’entreprise (voir aussi la section 16.5). La règle qui suit s’écarte de ce que retient l’exposé : la section 16.5 et la grille de décision posent, entre domaines, le pair-à-pair par protocole (A2A, chapitre 6) et, à l’intérieur d’un domaine, une topologie centralisée; la grille ne propose de s’en écarter que pour une plateforme unique sous une seule autorité.

- **Dans un contexte borné, l’orchestration déterministe.** Un processus relève d’un domaine métier unique, sous une responsabilité claire : l’instruction d’une réclamation d’assurance chez BCA, le diagnostic complet d’une alerte machine chez BSN. Un coordinateur explicite pilote les étapes, détient l’état d’avancement, applique les délais de garde et agrège les preuves. Un seul identifiant d’exécution indique où en est le dossier.
- **Entre domaines, la chorégraphie événementielle.** Quand la clôture d’un diagnostic technique chez BSN doit déclencher une mise à jour du risque client dans le CRM, un réajustement des prévisions de pièces dans l’ERP industriel et une écriture analytique de provision financière, aucun orchestrateur central ne doit coupler ces trois divisions. Le domaine source publie un événement métier immuable et typé (`EquipmentFailureDiagnosed.v2`, conforme à Apache Ossie) sur le courtier d’entreprise (Kafka ou Solace). Chaque domaine abonné déclenche de façon autonome son propre micro-orchestrateur interne.

| Critère d’urbanisation | Orchestration monolithique globale | Chorégraphie pure intégrale | Architecture cellulaire fédérée (Standard 2027) |
|:-------------------|:---------------------------|:--------------------------|:---------------------------|
| Autorité de flux | Un seul moteur central pilote toutes les divisions | Aucun point central; réactions par chaînes d’événements | Chorégraphie inter-domaines + orchestration intra-domaine |
| Couplage organisationnel | Très fort : chaque changement local touche le flux maître | Très faible : ajout d’abonnés sans modifier l’émetteur | Optimal : contrats d’événements stables aux frontières |
| Visibilité d’un processus | Native dans la console du moteur central | Difficile : le flux émerge implicitement des journaux | Reconstruite par corrélation OpenTelemetry (`traceparent`) |
| Gestion des échecs globaux | Blocs `try/catch` et compensation pilotée | Événements compensatoires en cascade complexes à tester | Sagas locales orchestrées + événements d’annulation typés |
| Rayon d’impact d’une panne | Critique (point de défaillance unique logique) | Confiné par file d’attente et mémoire tampon du courtier | Isolé par cellule métier avec découplage temporel |
| Conformité réglementaire | Lourde (tout le graphe hérite de la cote maximale) | Audit laborieux des chaînes causales émergentes | Périmètre BSIF E-23 / EU AI Act cloisonné |

---

## 16.10 Anatomie comparative des six topologies canoniques en 2027

Une fois les frontières de domaines tracées, il reste à structurer la collaboration des agents à l’intérieur d’une cellule orchestrée ou d’un sous-réseau coopératif. Ce volet retient six topologies canoniques, illustrées à la figure ci-dessous; l’exposé, qui ne cite aucune donnée d’adoption des patrons en entreprise, classe neuf patrons selon trois topologies et un axe adaptatif (section 16.1). Toute architecture candidate justifie laquelle elle instancie, ou comment elle les compose hiérarchiquement.

![Comparaison architecturale des six topologies multi-agents de production en 2027.](figures/fig-16-a-1.svg)

### 1. Superviseur hiérarchique et routeur

Le superviseur, la hiérarchie et le routeur sont décrits aux sections 16.2 et 16.3. En production, le nœud coordinateur choisit les spécialistes d’après leurs Agent Cards A2A v1.0 et leur transmet un sous-mandat ciblé. La configuration est en étoile, ou en arbre à deux niveaux quand des superviseurs de domaine dirigent des travailleurs spécialisés.

- **Force.** La complexité des échanges reste linéaire, en $O(k)$ pour $k$ spécialistes sollicités. Les agents feuilles s’ignorent : la compromission ou la dérive de l’un ne contamine pas latéralement le contexte des autres.
- **Piège en production : le superviseur entonnoir.** Si un spécialiste d’extraction retourne au superviseur un document JSON de 40 000 jetons pour qu’il le retransmette à un second spécialiste, le superviseur paie deux fois la sérialisation et la génération par le modèle, et risque de tronquer ou d’altérer des identifiants critiques.
- **Remède obligatoire : le passage par référence.** Le spécialiste n° 1 dépose l’artefact volumineux dans un magasin d’objets chiffré, à bail court, et ne retourne au superviseur qu’un résumé de 150 jetons avec un pointeur URI signé (`a2a://artifacts/sha256-...`). Le superviseur le transmet tel quel au spécialiste n° 2.

### 2. Planificateur, exécuteur et critique bornés

Cette topologie prolonge la boucle de réflexion de la section 16.4 par un troisième rôle. Le planificateur structure la démarche, l’exécuteur produit l’artefact ou prépare la transaction avec ses outils MCP, le critique évalue le résultat face aux pièces justificatives, aux invariants métier et aux politiques de conformité avant d’autoriser la sortie ou d’exiger une révision ciblée.

- **Indépendance épistémique.** Faire jouer l’exécuteur et le critique par le même modèle, avec deux consignes système différentes, ne corrige qu’une fraction marginale des erreurs : le modèle partage les mêmes angles morts et valide ses propres hallucinations avec une confiance élevée. En production, le critique combine des vérificateurs déterministes (schémas JSON, moteurs Cedar/OPA, solveurs arithmétiques) et un modèle évaluateur issu d’une famille d’entraînement distincte de celle de l’exécuteur.
- **Condition d’arrêt.** La boucle est bornée par une constante dure $N_{\max} \in \{2, 3\}$ et par un détecteur de convergence. Si l’écart sémantique entre deux révisions successives stagne, ou si le plafond $N_{\max}$ est atteint sans approbation du critique, l’exécution n’échoue pas en silence : elle bascule de façon déterministe en escalade HOTL, avec le journal exact des objections du critique.

### 3. Graphe orienté acyclique dynamique typé

Dans une boucle *ReAct*, l’agent improvise chaque pas après avoir observé le précédent, ce qui enchaîne séquentiellement dix appels coûteux au modèle. Le patron planifier puis exécuter sépare deux temps :

1. **Compilation.** Un modèle de raisonnement analyse la requête une seule fois et émet un graphe orienté acyclique (DAG) déclaratif. Chaque nœud référence une compétence OASF/A2A ou un outil MCP répertorié, avec une liaison explicite des entrées et des sorties typées.
2. **Validation et ordonnancement déterministes.** Avant toute exécution, le moteur de plateforme vérifie hors modèle que le graphe est strictement acyclique (tri topologique de Kahn), que les schémas Apache Ossie connectés sont compatibles, que l’identité appelante détient les portées requises et que le coût estimé cumulé des nœuds respecte le budget de l’`ActionEnvelope`. Il exécute ensuite en parallèle maximal (fan-out) toutes les branches indépendantes.

Sur les processus de collecte multi-sources, d’audit de conformité ou d’enrichissement client 360°, cette topologie divise couramment la latence de bout en bout par un facteur 3 à 5 et réduit de 60 % la facture de jetons, parce qu’elle supprime les appels de routage intermédiaires. Si un nœud échoue sur une surprise métier, le moteur replanifie localement le sous-graphe, limité aux nœuds aval touchés.

### 4. Tableau noir partagé

Issue des premiers systèmes experts acoustiques (Hearsay-II) et reprise en 2026–2027 sur des magasins d’état transactionnels rapides, cette architecture inverse le couplage : aucun orchestrateur ne connaît à l’avance l’ordre d’intervention des spécialistes. Le dossier est un espace mémoire structuré et versionné, qui contient les observations brutes, les hypothèses actives avec leurs intervalles de confiance, les pistes réfutées et un prédicat formel de résolution.

Des spécialistes indépendants observent les mutations du tableau noir. Quand un fait de leur compétence apparaît (anomalie BGP, signature spectrale haute fréquence), le spécialiste lit l’état courant, conduit ses investigations MCP et publie un enrichissement atomique, protégé par concurrence optimiste (ETag) sur sa propre sous-clé, pour éviter la famine d’écriture entre experts rapides et lents. Un contrôleur léger vérifie après chaque mutation si le prédicat d’arrêt est satisfait : confiance $\ge 0,92$ sur une cause racine corroborée, ou épuisement du budget temporel. La topologie convient au diagnostic d’incidents cyber-physiques, aux centres SOC et aux opérations réseau complexes. Microsoft range pourtant parmi les antipatrons le partage d’un état modifiable entre agents concurrents, source de données incohérentes (section 16.3, chapitre 14) : l’exposé ne traite pas le tableau noir, et la concurrence optimiste décrite ci-dessus est la parade propre à ce volet.

### 5. Réseau contractuel à enchères internes (Contract Net Protocol, CNP)

Quand plusieurs agents, fournisseurs internes ou passerelles externes peuvent accomplir la même tâche, avec des profils de coût, de charge instantanée, de localisation ou de qualité qui varient en temps réel, un routage statique devient sous-optimal. Le protocole Contract Net, formalisé à l’origine par Reid Smith puis standardisé par la FIPA, a été transposé sur A2A v1.0 et AGNTCY SLIM. Il institue un micro-marché interne en quatre phases :

1. **Annonce (`TaskAnnouncement`).** L’adjudicateur diffuse aux candidats qualifiés le cahier des charges typé : objectif, contraintes de résidence des données, échéance maximale, plafond budgétaire.
2. **Soumission.** Chaque candidat interroge sa file d’attente, ses stocks locaux ou le coût courant de son modèle, puis soumet une offre chiffrée et engageante, assortie d’un bail de capacité court, ou refuse explicitement s’il est saturé.
3. **Adjudication déterministe.** Un algorithme déterministe, jamais un prompt sensible à l’auto-promotion, écarte les baux expirants, classe les offres valides selon une fonction d’utilité pondérée et attribue le mandat exclusif au lauréat par un jeton `TaskAward` borné dans le temps.
4. **Exécution et reddition.** L’écart entre la promesse de la soumission (latence, exactitude) et la performance réelle met à jour le score de réputation de l’agent dans le registre de plateforme. Cela neutralise la malédiction du vainqueur, où un agent sous-estime ses délais pour remporter l’enchère.

### 6. Hybride BPMN 2.0 / DMN et sous-graphes agentiques bornés

Dans les secteurs très réglementés (banque sous BSIF E-23, assurance, santé, aéronautique, secteur public), le flux directeur d’un dossier ne peut pas dépendre de l’interprétation d’un modèle de langage : la séquence légale des notifications, les délais de rétractation, les contrôles anti-blanchiment (KYC/AML) et les seuils de délégation de signature doivent être prouvables.

L’architecture hybride garde comme flux directeur un moteur de processus normatif : ISO/IEC 19510 BPMN 2.0 couplé aux tables de règles OMG DMN, exécuté sur Camunda 8 / Zeebe, UiPath Maestro ou IBM BAMOE. Seules les étapes qui exigent une synthèse documentaire non structurée, un rapprochement sémantique flou ou une négociation assistée sont déléguées à une Service Task qui encapsule un sous-graphe agentique borné, typiquement une cellule planificateur–exécuteur–critique. Quand la cellule retourne sa recommandation structurée, une porte déterministe DMN reprend la main et valide les seuils d’affaires avant toute écriture dans le système d’enregistrement.

### Matrice de sélection topologique

| Topologie multi-agents | Latence bout-en-bout | Multiplicateur coût jetons | Déterminisme du parcours | Tolérance aux pannes partielles | Auditabilité prudentielle | Risque dominant (OWASP ASI) | Cas d’usage de référence |
|:--------------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:---------------|
| 1. Superviseur hiérarchique | Moyenne (séquentielle ou semi-parallèle) | Faible à modéré ($1,3\times$ à $2,0\times$) | Moyen-élevé (étoile contrôlée) | Bonne (réessai ou repli par feuille) | Élevée si le passage par référence est actif | ASI01 / Surcharge du nœud racine | Triage omnicanal, assistance employé multi-applications |
| 2. Planificateur–exécuteur–critique | Moyenne à haute ($1$ à $3$ cycles) | Modéré à élevé ($2,2\times$ à $3,8\times$) | Moyen (boucle bornée par $N_{\max}$) | Élevée (autocorrection sémantique) | Très élevée (journal des objections) | Collusion de biais si même famille de modèles | Souscription complexe, génération de code/SQL, analyse légale |
| 3. DAG dynamique typé | Très faible (parallélisme maximal) | Très faible ($1,1\times$ à $1,5\times$) | Élevé une fois le DAG compilé | Moyenne (recompilation locale sur échec) | Très élevée (graphe figé avant action) | Mauvaise décomposition initiale | Vue 360° client, audit multi-systèmes, due diligence |
| 4. Tableau noir partagé | Variable (convergence opportuniste) | Modéré à élevé selon le nombre d’experts | Faible sur l’ordre, strict sur l’arrêt | Excellente (experts découplés) | Bonne via le journal des révisions ETag | ASI06 Empoisonnement d’état partagé | Diagnostic de cause racine (RCA) télécoms, cyber SOC, maintenance OT |
| 5. Contract Net (enchères) | Moyenne (+1 aller-retour d’enchère) | Modéré (annonces légères JSON) | Élevé (adjudication algébrique) | Excellente (routage hors nœuds saturés) | Élevée (traces d’offres et scores) | Sur-promesse d’un agent mal calibré | Allocation logistique multi-dépôts, approvisionnement B2B, routage GPU |
| 6. Hybride BPMN/DMN + cellule | Calibrée par SLA métier | Minimal (IA confinée aux nœuds flous) | Maximal (ISO 19510 + DMN) | Très élevée (compensations natives BPMN) | Maximale (BSIF E-23, FDA, ISO) | Friction d’évolution si mal découpé | Octroi de crédit, indemnisation d’assurance, dossiers réglementés |

---

## 16.11 Implémentation de référence de trois patrons

Trois extraits codent les mécanismes où une erreur d’implémentation coûte le plus cher en production : le bornage de la boucle exécuteur–critique, l’adjudication d’une enchère Contract Net et l’insertion d’une cellule cognitive dans un flux BPMN 2.0 / DMN.

#### Extrait 16.1 — Cellule Planificateur–Exécuteur–Critique bornée à hétérogénéité de modèles obligatoire

Cet orchestrateur TypeScript impose quatre garde-fous. Au démarrage, il vérifie que l’exécuteur et le critique relèvent de deux familles de fournisseurs distinctes. Il impute chaque coût au budget de l’`ActionEnvelope`, détecte la stagnation des critiques d’un tour à l’autre par une empreinte normalisée, et bascule en escalade HOTL plutôt que de livrer une sortie non homologuée.

``` typescript
import { createHash } from "node:crypto";

export interface ModelEndpointDescriptor {
  readonly providerFamily: "anthropic" | "openai" | "google" | "mistral" | "meta-local";
  readonly modelId: string;
  readonly gatewayRoute: string;
}

export interface CriticVerdict {
  readonly approved: boolean;
  readonly severityScore: number; // 0.0 (conforme) à 1.0 (blocage critique)
  readonly violatedInvariants: ReadonlyArray<string>;
  readonly actionableFeedback: string;
  readonly tokenCostCad: number;
}

export interface ExecutionAttempt<TOutput> {
  readonly draft: TOutput;
  readonly evidenceUris: ReadonlyArray<string>;
  readonly tokenCostCad: number;
}

export type BoundedCellOutcome<TOutput> =
  | { readonly status: "APPROVED"; readonly output: TOutput; readonly iterations: number; readonly totalCostCad: number }
  | { readonly status: "ESCALATE_HOTL"; readonly lastDraft: TOutput; readonly reason: string; readonly auditTrail: ReadonlyArray<CriticVerdict> };

export class BoundedPECOrchestrator<TInput, TOutput> {
  private readonly maxIterations: number;

  constructor(
    private readonly executorModel: ModelEndpointDescriptor,
    private readonly criticModel: ModelEndpointDescriptor,
    private readonly executeStep: (input: TInput, feedback: string | null) => Promise<ExecutionAttempt<TOutput>>,
    private readonly evaluateStep: (input: TInput, attempt: ExecutionAttempt<TOutput>) => Promise<CriticVerdict>,
    private readonly deterministicPolicyCheck: (draft: TOutput) => ReadonlyArray<string>,
    options: { maxIterations?: number } = {}
  ) {
    if (executorModel.providerFamily === criticModel.providerFamily) {
      throw new Error(
        `Violation ADR-011 : L'Exécuteur (${executorModel.modelId}) et le Critique ` +
        `(${criticModel.modelId}) doivent appartenir à des familles de modèles distinctes.`
      );
    }
    this.maxIterations = Math.min(Math.max(options.maxIterations ?? 3, 1), 3);
  }

  public async runBoundedCell(
    input: TInput,
    maxBudgetCad: number
  ): Promise<BoundedCellOutcome<TOutput>> {
    let spentCad = 0;
    let priorFeedback: string | null = null;
    const seenViolationHashes = new Set<string>();
    const auditTrail: CriticVerdict[] = [];
    let latestAttempt: ExecutionAttempt<TOutput> | null = null;

    for (let iteration = 1; iteration <= this.maxIterations; iteration++) {
      latestAttempt = await this.executeStep(input, priorFeedback);
      spentCad += latestAttempt.tokenCostCad;

      if (spentCad > maxBudgetCad) {
        return {
          status: "ESCALATE_HOTL",
          lastDraft: latestAttempt.draft,
          reason: `Plafond budgétaire cellule dépassé (${spentCad.toFixed(3)} / ${maxBudgetCad.toFixed(3)} CAD)`,
          auditTrail,
        };
      }

      // 1. Garde déterministe rapide (gratuit et infaillible) avant d'appeler le Critique LLM
      const hardViolations = this.deterministicPolicyCheck(latestAttempt.draft);
      if (hardViolations.length > 0) {
        const hardSig = createHash("sha256").update(["HARD", ...[...hardViolations].sort()].join("::")).digest("hex");
        if (seenViolationHashes.has(hardSig)) {
          return {
            status: "ESCALATE_HOTL",
            lastDraft: latestAttempt.draft,
            reason: `Stagnation déterministe à l'itération ${iteration} (${hardViolations[0]})`,
            auditTrail,
          };
        }
        seenViolationHashes.add(hardSig);
        priorFeedback = `Violations déterministes bloquantes : ${hardViolations.join(" | ")}`;
        continue;
      }

      // 2. Évaluation sémantique indépendante par le Critique hétérogène
      const verdict = await this.evaluateStep(input, latestAttempt);
      spentCad += verdict.tokenCostCad;
      auditTrail.push(verdict);

      if (verdict.approved && verdict.violatedInvariants.length === 0) {
        return {
          status: "APPROVED",
          output: latestAttempt.draft,
          iterations: iteration,
          totalCostCad: spentCad,
        };
      }
      if (spentCad > maxBudgetCad) {
        return {
          status: "ESCALATE_HOTL",
          lastDraft: latestAttempt.draft,
          reason: `Plafond budgétaire cellule dépassé après revue (${spentCad.toFixed(3)} / ${maxBudgetCad.toFixed(3)} CAD)`,
          auditTrail,
        };
      }

      // 3. Détection de stagnation : si l'Exécuteur reproduit exactement les mêmes fautes, inutile de boucler
      const violationSignature = createHash("sha256")
        .update([...verdict.violatedInvariants].sort().join("::"))
        .digest("hex");

      if (seenViolationHashes.has(violationSignature)) {
        return {
          status: "ESCALATE_HOTL",
          lastDraft: latestAttempt.draft,
          reason: `Stagnation cognitive détectée à l'itération ${iteration} sur les mêmes invariants`,
          auditTrail,
        };
      }

      seenViolationHashes.add(violationSignature);
      priorFeedback = verdict.actionableFeedback;
    }

    return {
      status: "ESCALATE_HOTL",
      lastDraft: latestAttempt!.draft,
      reason: `Convergence non atteinte après le plafond dur de ${this.maxIterations} itérations`,
      auditTrail,
    };
  }
}
```

#### Extrait 16.2 — Adjudicateur typé d’enchères internes *Contract Net Protocol* (CNP) sur A2A v1.0

Un coordinateur logistique sollicite en même temps plusieurs agents de centres de distribution ou de transporteurs homologués. Le gagnant est choisi par un score multicritère normalisé, pondéré par la fiabilité historique que la plateforme a vérifiée, ce qui neutralise toute tentative d’un agent tiers de gonfler sa confiance déclarée.

``` typescript
export interface TaskAnnouncement {
  readonly cfpId: string;
  readonly capabilityOasfUri: string;
  readonly requiredJurisdiction: "CA-QC" | "CA-ON" | "US-EAST" | "EU-DE";
  readonly maxAcceptableLatencyMs: number;
  readonly reservePriceCad: number;
  readonly bidSubmissionWindowMs: number;
  readonly payloadSchemaRef: string;
}

export interface AgentBid {
  readonly cfpId: string;
  readonly bidderAgentId: string;
  readonly bidderSpiffeId: string;
  readonly jurisdiction: "CA-QC" | "CA-ON" | "US-EAST" | "EU-DE";
  readonly quotedCostCad: number;
  readonly guaranteedP95LatencyMs: number;
  readonly selfReportedConfidence: number; // 0..1 (pondéré avec prudence!)
  readonly capacityHoldUntilIso: string;
}

export interface PlatformReputationRecord {
  readonly verifiedPassKScore: number;     // Mesuré par télémétrie réelle (0..1)
  readonly slaComplianceRate30d: number;   // Taux de respect des délais promis (0..1)
}

export interface TaskAward {
  readonly awardId: string;
  readonly cfpId: string;
  readonly winningBidderAgentId: string;
  readonly agreedMaxCostCad: number;
  readonly leaseExpiresAtIso: string;
  readonly utilityScore: number;
  readonly runnerUpAgentId: string | null;
}

export function adjudicateContractNetBids(
  announcement: TaskAnnouncement,
  bids: ReadonlyArray<AgentBid>,
  reputationLedger: ReadonlyMap<string, PlatformReputationRecord>,
  nowEpochMs: number
): TaskAward | null {
  // 1. Filtrage éliminatoire strict (contraintes réglementaires, bail actif, plafond FinOps et SLA)
  const eligibleBids = bids.filter((bid) => {
    const rep = reputationLedger.get(bid.bidderAgentId);
    if (!rep || rep.verifiedPassKScore < 0.80) return false;
    if (bid.jurisdiction !== announcement.requiredJurisdiction) return false;
    if (bid.quotedCostCad <= 0 || bid.quotedCostCad > announcement.reservePriceCad) return false;
    if (bid.guaranteedP95LatencyMs > announcement.maxAcceptableLatencyMs) return false;
    const holdExpiryMs = Date.parse(bid.capacityHoldUntilIso);
    if (Number.isNaN(holdExpiryMs) || holdExpiryMs < nowEpochMs + announcement.maxAcceptableLatencyMs) return false;
    return true;
  });

  if (eligibleBids.length === 0) {
    return null;
  }

  // 2. Évaluation déterministe : 45 % Fiabilité prouvée, 35 % Économie, 20 % Vélocité
  const scored = eligibleBids.map((bid) => {
    const rep = reputationLedger.get(bid.bidderAgentId)!;
    const costEfficiency = 1 - bid.quotedCostCad / announcement.reservePriceCad;
    const speedEfficiency = 1 - bid.guaranteedP95LatencyMs / announcement.maxAcceptableLatencyMs;
    const calibratedReliability =
      0.85 * (rep.verifiedPassKScore * rep.slaComplianceRate30d) +
      0.15 * Math.min(Math.max(bid.selfReportedConfidence, 0), 1);

    const utilityScore =
      0.45 * calibratedReliability +
      0.35 * costEfficiency +
      0.20 * speedEfficiency;

    return { bid, utilityScore };
  });

  scored.sort(
    (a, b) =>
      b.utilityScore - a.utilityScore ||
      a.bid.quotedCostCad - b.bid.quotedCostCad ||
      a.bid.bidderAgentId.localeCompare(b.bid.bidderAgentId)
  );

  const winner = scored[0];
  const runnerUp = scored.length > 1 ? scored[1].bid.bidderAgentId : null;

  return {
    awardId: `award-${announcement.cfpId}-${nowEpochMs}`,
    cfpId: announcement.cfpId,
    winningBidderAgentId: winner.bid.bidderAgentId,
    agreedMaxCostCad: winner.bid.quotedCostCad,
    leaseExpiresAtIso: winner.bid.capacityHoldUntilIso,
    utilityScore: Number(winner.utilityScore.toFixed(4)),
    runnerUpAgentId: runnerUp,
  };
}
```

#### Extrait 16.3 — Encapsulation d’une cellule cognitive dans un processus réglementé BPMN 2.0 / DMN

Ce fragment BPMN 2.0 exécutable (Camunda 8 / Zeebe) insère une délégation A2A bornée entre trois barrières déterministes : une table DMN amont qui vérifie la recevabilité contractuelle, un minuteur d’expiration en frontière (`boundaryEvent`) qui empêche la lenteur d’inférence de bloquer le dossier, et une passerelle exclusive (`exclusiveGateway`) aval qui oriente vers l’enregistrement automatique ou vers un souscripteur humain.

``` xml
<bpmn:process id="bca-claim-adjudication-v3"
              name="Instruction Sinistre Sous Contrôle BSIF E-23"
              isExecutable="true"
              xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"
              xmlns:zeebe="http://camunda.org/schema/zeebe/1.0"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <!-- 1. Filtre déterministe amont : Table DMN d'admissibilité contractuelle de base -->
  <bpmn:businessRuleTask id="Task_PreCheckDMN" name="Vérifier Franchise et Statut Police (DMN)">
    <bpmn:extensionElements>
      <zeebe:calledDecision decisionId="dmn-policy-eligibility-v4" resultVariable="preCheck" />
    </bpmn:extensionElements>
  </bpmn:businessRuleTask>

  <!-- 2. Cellule cognitive bornée invoquée via connecteur A2A gouverné -->
  <bpmn:serviceTask id="Task_AgenticTechnicalReview" name="Cellule A2A : Analyse Rapport Expertise &amp; Clauses">
    <bpmn:extensionElements>
      <zeebe:taskDefinition type="io.boreal.a2a.bounded-pec-worker:v2" retries="2" />
      <zeebe:taskHeaders>
        <zeebe:header key="targetAgentCard"
          value="https://gateway.boreal.ca/a2a/bca/claims-pec" />
        <zeebe:header key="maxIterations" value="3" />
        <zeebe:header key="maxBudgetCad" value="1.85" />
        <zeebe:header key="requiredOboScope" value="bca.claims.analyze_technical_report" />
      </zeebe:taskHeaders>
    </bpmn:extensionElements>
  </bpmn:serviceTask>

  <!-- Barrière temporelle déterministe : interruption propre si la cellule dépasse 90 secondes -->
  <bpmn:boundaryEvent id="Timer_AgentSlaBreach" attachedToRef="Task_AgenticTechnicalReview" cancelActivity="true">
    <bpmn:timerEventDefinition>
      <bpmn:timeDuration xsi:type="bpmn:tFormalExpression">PT90S</bpmn:timeDuration>
    </bpmn:timerEventDefinition>
  </bpmn:boundaryEvent>

  <!-- 3. Table DMN aval de gouvernance HOTL (aucun commit direct sur la seule foi du LLM) -->
  <bpmn:businessRuleTask id="Task_PostGateDMN" name="Statuer Autorisation Décaissement vs Escalade HOTL (DMN)">
    <bpmn:extensionElements>
      <zeebe:calledDecision decisionId="dmn-e23-disbursement-gate" resultVariable="gateDecision" />
    </bpmn:extensionElements>
  </bpmn:businessRuleTask>

  <bpmn:exclusiveGateway id="Gw_RouteAuthorization" name="Décision Porte DMN" default="Flow_ToHumanUnderwriter" />

  <bpmn:sequenceFlow id="Flow_1" sourceRef="Task_PreCheckDMN" targetRef="Task_AgenticTechnicalReview" />
  <bpmn:sequenceFlow id="Flow_2" sourceRef="Task_AgenticTechnicalReview" targetRef="Task_PostGateDMN" />
  <bpmn:sequenceFlow id="Flow_TimeoutFallback" sourceRef="Timer_AgentSlaBreach" targetRef="Task_HumanUnderwriterReview" />
  <bpmn:sequenceFlow id="Flow_AutoCommit" sourceRef="Gw_RouteAuthorization" targetRef="Task_CommitGuidewire">
    <bpmn:conditionExpression xsi:type="bpmn:tFormalExpression">
      = gateDecision.allowStraightThrough = true and agentResult.status = "APPROVED" and claimAmountCad &lt;= 10000
    </bpmn:conditionExpression>
  </bpmn:sequenceFlow>
  <bpmn:sequenceFlow id="Flow_ToHumanUnderwriter" sourceRef="Gw_RouteAuthorization" targetRef="Task_HumanUnderwriterReview" />

</bpmn:process>
```

---

## 16.12 Gouvernance anti-dérive : coupe-circuits topologiques et antipatrons

Même quand une équipe choisit d’abord une topologie saine, la maintenance continue des consignes système, l’ajout d’agents spécialistes dans l’annuaire OASF et l’évolution silencieuse des poids des modèles introduisent des pathologies structurelles en production. L’ingénierie AgentOps de 2027 traite la topologie d’exécution comme une surface d’attaque et de dérive financière, surveillée en temps réel dans la passerelle agentgateway et le collecteur OpenTelemetry.

### Quatre mécanismes de confinement

Pour qu’un graphe multi-agents se termine en temps fini et à coût borné, quatre garde-fous d’infrastructure s’appliquent indépendamment du raisonnement des agents :

1. **Compteur de sauts décrémenté de façon atomique.** Comme le champ TTL d’un paquet IPv4, l’entier `maxRemainingHops` transporté dans l’en-tête signé de l’`ActionEnvelope` perd une unité à chaque délégation horizontale A2A v1.0. Quand un orchestrateur délègue en parallèle à trois spécialistes (fan-out), il divise ou plafonne de même le sous-budget de chaque branche $B_i$ :

$$B_i \le \alpha_i \cdot B_{\text{rest}}, \quad \sum_{i=1}^{k} \alpha_i \le 1 - \varepsilon$$

où $\varepsilon$ réserve le budget de l’étape finale d’agrégation. Tout appel entrant dont le compteur vaut zéro est rejeté par la passerelle en HTTP 429 Too Many Requests, avant même d’invoquer un GPU.

2. **Détection de cycles par graphe d’appels en session.** Un compteur de sauts protège contre l’infini, mais pas contre deux agents A et B qui gaspillent six sauts à se renvoyer la balle (`A -> B -> A -> B`). La passerelle garde dans le contexte de trace OpenTelemetry la liste ordonnée des combinaisons `(targetAgentId, skillId, canonicalInputHash)` déjà traversées par la saga. Toute réinvocation identique, sans mutation intermédiaire de l’état externe, déclenche un court-circuit immédiat.

3. **Isolement strict des fenêtres de contexte.** Les cadriciels de première génération transmettaient à chaque sous-agent tout le fil amont. Une délégation A2A de production n’envoie au spécialiste aval que l’objet JSON validé par son `inputSchema`. Cette hygiène réduit de 70 % la consommation de jetons, améliore le taux de succès du cache KV du spécialiste et bloque la propagation latérale des injections de prompt cachées dans les étapes antérieures (OWASP ASI01).

4. **Dégradation par routage de secours pré-câblé.** Quand un nœud non critique d’un DAG dynamique ou un soumissionnaire Contract Net expire, le moteur ne fait pas échouer toute la saga si une réponse partielle qualifiée suffit au métier, et ne laisse pas un modèle improviser une stratégie de sauvetage. Chaque arc du graphe déclare sa politique d’échec : `FAIL_FAST`, `SUBSTITUTE_RUNNER_UP` (bascule vers le second de l’enchère) ou `DEGRADE_WITH_FLAG` (poursuite avec un marquage explicite d’incertitude, qui abaisse le plafond d’autonomie de L3 à L2).

### Antipatrons observés en production

| Antipatron topologique | Description du dysfonctionnement | Signature télémétrique (OpenTelemetry) | Correctif architectural normatif |
|:----------------|:----------------------------|:---------------------------|:---------------------------|
| Le comité bavard | Quatre à six agents débattent en boucle ouverte sur un tampon commun, sans arbitre déterministe | Ratio jetons générés / jetons utiles $> 12:1$; variance extrême de durée (P99 $> 8\times$ P50) | Remplacer par un DAG typé (collecte) suivi d’une cellule exécuteur–critique bornée à $N_{\max} = 2$ |
| Le superviseur entonnoir | Le superviseur central recopie par génération du modèle de gros tableaux ou documents d’un agent feuille à un autre | Spans du superviseur représentant $> 65\,\%$ du coût total et dégradations d’exactitude sur les codes SKU/ID | Imposer le passage par référence : transfert d’URI d’artefacts immuables hors de la voie cognitive |
| Le ping-pong de politesse | Deux agents autonomes se remercient ou se redemandent mutuellement confirmation de clôture d’une tâche | Alternance périodique `agent.A <-> agent.B` avec charge utile quasi vide avant épuisement du TTL | Protocole d’état fini A2A strict (COMPLETED terminal non réentrant) + détection de cycle sur `traceId` |
| La critique incestueuse | L’agent critique utilise le même modèle et le même contexte RAG bruité que l’agent exécuteur | Taux d’approbation au tour 1 $> 99\,\%$, mais taux de défauts découverts après coup inchangé | Imposer deux familles de modèles distinctes (ADR-011) + exécuter en amont les gardes déterministes Cedar |
| L’orchestrateur dieu | Un seul graphe central encode les règles internes de cinq départements et de trente serveurs MCP | Déploiements bloqués par la coordination inter-équipes; rayon d’impact total à chaque changement de schéma | Scinder selon les contextes bornés : chorégraphie événementielle inter-divisions + micro-workflows locaux |

---

## 16.13 Application au fil rouge et éclairages sectoriels

L’erreur la plus fréquente d’un centre d’excellence nouvellement créé est de décréter une topologie unique pour toute l’entreprise, par exemple un superviseur hiérarchique partout, par souci d’uniformité. Au Groupe Boréal Inc., les contraintes opérationnelles, physiques et réglementaires des trois divisions diffèrent trop pour cela. L’équipe d’architecture a institué une sélection topologique différenciée, articulée autour d’un bus chorégraphique commun.

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : sélection topologique différenciée sur les trois divisions (BSN, BEL, BCA)**
:::

**Problème initial (début T1 2027).** Au cadrage de la Fabrique Agentique Boréal, trois équipes pilotes proposaient des architectures incompatibles. Chez BSN, une équipe avait prototypé un « essaim conversationnel » de cinq agents pour diagnostiquer les pannes complexes de compresseurs : chaque incident consommait en moyenne 84 000 jetons et durait 4 minutes, avec 11 % de contradictions non résolues. Chez BEL, un routeur statique affectait toujours les commandes urgentes de pièces au dépôt le plus proche, sans tenir compte des engorgements de préparation ni des grèves de transporteurs locaux. Chez BCA, la direction de la conformité refusait qu’un orchestrateur LLM libre pilote l’instruction d’un dossier soumis à la ligne directrice BSIF E-23.

**Architecture retenue par division, reliée par chorégraphie entre les divisions.**

1. **Boréal Services Numériques (BSN) : tableau noir pour le diagnostic multi-signaux, DAG typé pour l’enrichissement client.**
    - Quand une machine industrielle remonte une alerte composite ambiguë (vibrations, surchauffe de l’huile, chutes de pression intermittentes), un tableau noir transactionnel, hébergé sur Redis Enterprise / PostgreSQL avec verrouillage ETag, agrège en parallèle les observations de trois travailleurs spécialisés : un SLM vibratoire, un SLM thermodynamique et l’historique des interventions ServiceNow. Dès que le prédicat de corroboration franchit $0,92$ de confiance, en 3,4 secondes en moyenne, le diagnostic figé est publié sur Kafka (`EquipmentFailureDiagnosed.v2`).
    - Pour préparer le dossier de soutien client dans Salesforce Agentforce, BSN utilise un DAG dynamique typé qui compile en parallèle la lecture télémétrique, l’état contractuel et les billets ouverts. La latence d’affichage chez le conseiller passe de 19 secondes à 2,1 secondes.
2. **Boréal Équipements & Logistique (BEL) : enchères internes Contract Net (CNP), sous la garde du jumeau numérique.**
    - En réaction par chorégraphie à l’événement `EquipmentFailureDiagnosed.v2`, le coordinateur logistique de BEL lance un appel d’offres CNP d’une fenêtre de 800 millisecondes auprès des agents des neuf centres logistiques nord-américains et de trois transporteurs express raccordés.
    - Chaque agent de dépôt calcule sa soumission à partir du stock libre dans SAP S/4HANA, de la charge instantanée des quais d’expédition et de l’empreinte carbone et du coût du transport. L’adjudicateur (Extrait 16.2) attribue la réservation au dépôt optimal, souvent Québec ou Mississauga plutôt que Montréal-Est saturé. Les coûts de fret d’urgence baissent de 23 % et le respect du SLA passe à 98,7 %.
3. **Boréal Capital & Assurances (BCA) : flux directeur hybride BPMN 2.0 / DMN qui encapsule une cellule planificateur–exécuteur–critique.**
    - Pour toute instruction de garantie ou de sinistre bris de machine, BCA impose un flux directeur déterministe sur Camunda 8 / Zeebe (Extrait 16.3). Les vérifications de police en vigueur sur l’IBM i (AS/400) et le calcul des plafonds de franchise sont exécutés à 100 % par des tables DMN, sans aucun appel à un modèle.
    - Seule l’analyse croisée du rapport technique de panne et des clauses particulières d’exclusion est confiée à une cellule planificateur–exécuteur–critique limitée à $N_{\max} = 3$ tours : exécuteur sur Claude, critique indépendant sur Gemini, hébergés en région canadienne conformément à la Loi 25. Cette isolation a permis aux auditeurs internes de valider la conformité BSIF E-23 trois mois avant l’échéance du 1er mai 2027.

**Bilan à 90 jours.** Les boucles infinies entre agents ont disparu : 0 incident, contre 3 par mois en phase prototype. Le facteur d’amplification de jetons baisse de 68 % chez BSN, de 84 000 à 26 500 jetons sur les cas complexes. La traçabilité OpenTelemetry est unifiée, de l’alerte du capteur à la comptabilisation financière.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Télécommunications — Auto-cicatrisation des réseaux 5G Standalone (niveau 4 du TM Forum) par tableau noir et hiérarchie régionale**
:::

Les opérateurs engagés en 2027 vers le niveau 4 des réseaux autonomes du TM Forum font face à un défi d’échelle : une tempête ou une coupure de fibre optique génère en quelques secondes 50 000 alarmes corrélées à travers le réseau d’accès radio (Open RAN), le transport optique et le cœur 5G Standalone multi-fournisseurs.

Une orchestration centralisée unique s’effondrerait sous la latence et le volume de télémétrie. Les architectures déployées en production chez les grands opérateurs combinent donc deux topologies :

1. **Grappe régionale MEC : tableau noir à haute vitesse.** Des agents spécialisés par couche réseau (radio RF, routage IP/MPLS, tranches réseau B2B) alimentent un tableau noir d’incident local et isolent en moins de 5 secondes le défaut physique racine parmi des milliers d’alarmes symptômes.
2. **NOC national : superviseur hiérarchique borné à deux niveaux.** Quand la remédiation locale exige de réallouer du spectre ou de réacheminer du trafic inter-régional qui touche des SLA entreprises critiques, le superviseur régional soumet un plan d’action chiffré au contrôleur déterministe national (vérificateur de politiques SON, jumeau de topologie réseau) avant application sur les contrôleurs SMO. Tout contournement direct entre deux agents de cellules radio voisines, sans passage par les gardes de stabilité, est bloqué pour éviter les oscillations de charge (flapping).
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Industrie pharmaceutique et sciences de la vie (GxP) — Homologation GAMP 5 par encapsulation BPMN/DMN de cellules critiques**
:::

Dans la fabrication biopharmaceutique soumise aux bonnes pratiques GxP, au guide ISPE GAMP 5 (2e édition) et à la réglementation FDA 21 CFR Part 11 (signatures électroniques et intégrité des données ALCOA+), la libération d’un lot de vaccins ou de principes actifs exige l’examen des dossiers de lot et l’investigation de tout écart de procédé.

Un graphe libre d’agents autonomes qui statuerait sur un écart de stérilisation rendrait le système informatique non validable lors d’une inspection réglementaire. La topologie hybride BPMN/DMN et cellule critique s’impose en 2027 comme patron de référence : elle accélère de 60 % la préparation des dossiers qualité sans compromettre la conformité.

- Le workflow BPMN 2.0 validé impose la séquence immuable des contrôles, l’horodatage infalsifiable et la signature électronique nominative de la personne qualifiée (QP), en régime strict L2 sur la décision finale de libération.
- Dans une étape circonscrite d’investigation documentaire, une cellule exécuteur–critique compare l’écart observé à dix ans d’historiques CAPA, vérifie chaque citation contre le PDF original indexé par empreinte SHA-256 et produit un projet de rapport structuré. Le critique indépendant certifie l’absence d’affirmation non sourcée avant sa présentation à la QP.
::::

---

## 16.14 Décision d’architecture normative et liste de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-011 — Standardisation des topologies multi-agents et interdiction des graphes cycliques non bornés**
:::

- **Statut** : Acceptée \| Périmètre : Ensemble des systèmes multi-agents (L1 à L4) \| Révision : Semestrielle
- **Contexte** : les équipes produits assemblent des flottes d’agents spécialisés par A2A v1.0 et divers cadriciels applicatifs. Sans contrainte structurelle sur la topologie des graphes d’interaction, l’organisation s’expose à des croissances quadratiques de consommation de jetons, à des boucles entre pairs, à la dégradation du cache KV et à l’impossibilité de démontrer le déterminisme des contrôles devant les régulateurs (BSIF E-23, Loi 25, EU AI Act).
- **Options évaluées** :
  1. *Liberté totale laissée aux cadriciels d’équipes (maillage conversationnel ouvert)* : rejetée. Les coûts deviennent imprévisibles, les défaillances en cascade ne sont pas contenues (OWASP ASI08) et la piste d’audit est illisible.
  2. *Topologie unique (superviseur hiérarchique partout)* : rejetée. Elle crée des goulots artificiels sur les diagnostics parallèles, interdit l’optimisation économique par enchères logistiques et ne suffit pas aux exigences formelles BPMN des processus financiers réglementés.
  3. *Catalogue fermé de six topologies homologuées, sous architecture cellulaire fédérée* : chorégraphie événementielle typée entre domaines métiers, choix explicite et documenté parmi les six topologies canoniques à l’intérieur de chaque domaine, garde-fous déterministes obligatoires. Retenue.
- **Décision** :
  1. Toute intégration entre domaines privilégie la chorégraphie, avec des événements métier immuables conformes aux schémas Apache Ossie. L’orchestration directe est réservée aux frontières d’un même contexte borné ou d’une saga définie par contrat.
  2. Les graphes cycliques libres sont interdits en production. Seules sont autorisées les boucles de rétroaction planificateur–exécuteur–critique, sous réserve d’un plafond dur $N_{\max} \le 3$, d’un détecteur de stagnation et de l’emploi obligatoire de deux familles de modèles distinctes pour l’exécuteur et le critique.
  3. Tout transfert de données volumineuses ($> 2\,000$ jetons) entre agents par l’intermédiaire d’un superviseur doit emprunter le passage par référence plutôt que la régénération textuelle.
  4. Les processus soumis à une cotation de matérialité élevée (BSIF E-23, GxP, octroi financier) doivent adopter la topologie hybride n° 6 (flux directeur BPMN 2.0 / DMN).
- **Conséquences** :
  - *Positives* : coût maximal par transaction prévisible, parallélisme maîtrisé, conformité prudentielle native, élimination par construction des rafales d’appels entre agents.
  - *Négatives et coûts assumés* : un magasin d’artefacts éphémères à maintenir pour le passage par référence, un double approvisionnement en fournisseurs de modèles pour l’hétérogénéité exécuteur/critique, et une revue d’architecture préalable à l’enregistrement de tout nouveau graphe orchestrateur.
- **Condition de révision** : réévaluation semestrielle des seuils de latence et des poids d’utilité du Contract Net à la lumière des métriques OpenTelemetry de production.
::::

### Liste de contrôle de mise en production

Avant d’homologuer un système multi-agents, et avant d’aborder au chapitre 18 le moteur d’exécution durable qui en conservera l’état, chaque architecture passe les huit vérifications suivantes :

1. **Frontières DDD respectées.** Le graphe évite-t-il de coupler les bases internes de plusieurs divisions dans un orchestrateur dieu, au profit d’événements métier typés aux frontières organisationnelles ?
2. **Rattachement explicite au catalogue topologique.** Le dossier d’architecture justifie-t-il laquelle des six topologies canoniques il emploie, au regard des contraintes de latence, de budget et d’auditabilité ?
3. **Acyclicité prouvée ou bornage strict.** Si le graphe est un DAG dynamique, un tri topologique déterministe rejette-t-il tout cycle avant l’exécution ? S’il comporte une boucle critique, la constante $N_{\max} \le 3$ et l’arrêt sur stagnation sont-ils codés en dur hors du prompt ?
4. **Indépendance épistémique du critique.** Dans toute cellule exécuteur–critique de niveau L2 à L4, le modèle critique vient-il d’une famille distincte de celle du modèle producteur, et des contrôles déterministes gratuits le précèdent-ils ?
5. **Hygiène du contexte et passage par référence.** Chaque sous-agent reçoit-il seulement son schéma d’entrée minimal, et les charges utiles volumineuses transitent-elles par un pointeur URI signé, sans traverser la fenêtre de génération du superviseur ?
6. **Coupe-circuits en passerelle.** La passerelle décrémente-t-elle `maxRemainingHops` à chaque saut A2A et bloque-t-elle les combinaisons `(agent, skill, inputHash)` répétées dans une même trace OpenTelemetry ?
7. **Adjudication déterministe des enchères.** Si le protocole Contract Net est utilisé, le classement des offres repose-t-il sur une fonction algébrique pondérée par la réputation que mesure la plateforme, plutôt que sur l’auto-évaluation déclarative des agents ?
8. **Politique de dégradation par branche.** Chaque délégation, parallèle ou séquentielle, définit-elle son comportement déterministe à l’expiration (`FAIL_FAST`, `SUBSTITUTE_RUNNER_UP`, `DEGRADE_WITH_FLAG` ou escalade HOTL) ?
