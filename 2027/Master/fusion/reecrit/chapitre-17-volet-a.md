## Mise en œuvre — Le grand découplage : contrôle déterministe et autonomie probabiliste {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu** : à 95 % de précision par décision, une chaîne non encadrée de quinze étapes plafonne à $0,95^{15} \approx 46,3\,\%$ de succès au premier passage, avec des dérives de coût et un risque de non-conformité réglementaire.
- **Décisions d’architecture** :
  1. *Irréversible* : séparer le plan de contrôle déterministe (machine à états durable, règles DMN et Cedar, transactions et compensations Saga) des cellules bornées confiées au modèle (interprétation, diagnostic multi-signaux).
  2. *Structurante dès la conception* : placer chaque appel au modèle entre une garde d’entrée déterministe (schéma, masquage des données personnelles, budget de jetons et de latence) et une garde de sortie qui vérifie les invariants métiers avant toute écriture dans un système d’enregistrement.
  3. *Réversible* : le choix du modèle, petit modèle spécialisé (SLM) ou grand modèle de raisonnement (LLM), dans une cellule bornée, remplaçable sans toucher au graphe d’orchestration parent.
- **Indicateurs de gouvernance** : constance $\text{pass}^5$ sur banc d’homologation, taux de rejet par les gardes d’invariants, taux d’activation du repli, latence et coût au 99e centile ($P_{99}$).
::::

## 17.8 Fiabilité composée d’une chaîne de décisions

Les erreurs d’un agent s’accumulent d’une étape à l’autre (section 17.1). La loi de Lusser, formulée en 1952 en ingénierie aérospatiale, en donne la mesure : la fiabilité d’une série de maillons est le produit de leurs fiabilités. Un prototype juste huit fois sur dix, placé sans garde déterministe devant dix mille événements quotidiens, produit deux mille incidents par jour, à reprendre à la main.

### De l’exactitude ponctuelle ($\text{pass}@1$) à la constance ($\text{pass}^k$)

Les classements académiques mesurent $\text{pass}@k$, la probabilité qu’au moins un essai sur $k$ réussisse. Le critère convient quand un compilateur ou un développeur écarte sans frais les propositions erronées. Un processus transactionnel — instruire un sinistre, modifier un approvisionnement, reconfigurer un équipement — doit au contraire appliquer la politique d’affaires à chacune des $k$ exécutions d’un même dossier. C’est ce que mesure $\text{pass}^k$, métrique des bancs d’évaluation d’agents transactionnels ($\tau\text{-bench}$). Pour $n$ décisions supposées indépendantes, de précision moyenne $p$, la borne de Lusser décroît de façon exponentielle :

$$R_{\text{seq}}(n) = \prod_{i=1}^{n} p_i \approx p^n, \quad \text{pass}^k(n) = p^{nk}$$

Deux ordres de grandeur :

- avec $p = 0,95$, un flux linéaire de $n = 12$ étapes libres réussit $0,95^{12} \approx 54,0\,\%$ des passages ($\text{pass}@1$), et sa reproductibilité sur cinq contrôles successifs ($\text{pass}^5$) tombe à $0,95^{60} \approx 4,6\,\%$;
- avec $p = 0,99$, au prix d’un modèle de pointe, un dossier complexe de $n = 30$ étapes atteint $0,99^{30} \approx 74,0\,\%$ au premier essai et $0,99^{150} \approx 22,1\,\%$ en $\text{pass}^5$, loin des SLA de $99,5\,\%$ exigés en production.

### Erreurs corrélées et coût de l’auto-correction

La dégradation réelle est plus rapide que la borne, car les erreurs successives ne sont pas indépendantes ($P(\text{err}_{i+1} \mid \text{err}_i) \gg 1 - p$) : dans une boucle ouverte, chaque sortie intermédiaire entre dans la fenêtre de contexte du tour suivant (OWASP ASI08 — Cascading Failures). Trois effets en découlent.

1. **Ancrage sur une hallucination précoce** : une mauvaise interprétation contractuelle au tour 3 biaise toutes les requêtes suivantes; le modèle justifie son erreur initiale avec une assurance croissante.
2. **Inflation quadratique des nouvelles tentatives** : un agent laissé libre de « réfléchir » après une erreur d’API empile les traces d’exception dans l’historique transmis à chaque tour, ce qui multiplie par vingt la consommation de jetons sans corriger la cause.
3. **Queue lourde de latence ($P_{99}$)** : les temps de réponse d’une boucle ouverte sont erratiques, incompatibles avec les régimes opérationnels courts.

L’extrait suivant chiffre le gain du découplage : une épine dorsale déterministe et $m \ll n$ cellules bornées, munies de gardes déterministes et d’un repli, portent la fiabilité au-delà de $99,3\,\%$.

#### Extrait 17.1 — Modèle quantitatif de fiabilité composée et de gain d’encapsulation hybride

``` python
from dataclasses import dataclass

@dataclass(frozen=True)
class FlowProfile:
    name: str
    probabilistic_cells: int          # m cellules cognitives sur N étapes totales
    raw_accuracy: float               # Précision brute d'un essai modèle (p)
    guard_detection_rate: float       # Part d'erreurs captées par garde déterministe
    max_verified_retries: int         # Réessais bornés autorisés après interception
    safe_fallback_rate: float         # Succès sûr du circuit de repli (règle / HOTL)

def cell_reliability(cfg: FlowProfile) -> float:
    caught_err = (1.0 - cfg.raw_accuracy) * cfg.guard_detection_rate
    direct_ok = cfg.raw_accuracy * sum(
        caught_err**i for i in range(cfg.max_verified_retries + 1)
    )
    fallback_ok = (caught_err ** (cfg.max_verified_retries + 1)) * cfg.safe_fallback_rate
    return direct_ok + fallback_ok

def evaluate_flow(cfg: FlowProfile, k: int = 5) -> dict[str, float]:
    r_cell = cell_reliability(cfg)
    pass_1 = r_cell ** cfg.probabilistic_cells
    return {
        "cell_rel": round(r_cell, 5),
        "e2e_pass_1": round(pass_1, 4),
        "e2e_pass_k": round(pass_1**k, 4),
    }

if __name__ == "__main__":
    free_chain = FlowProfile("Chaîne LLM libre (15 sauts)", 15, 0.95, 0.0, 0, 0.0)
    hybrid = FlowProfile("Épine déterministe + 3 cellules bornées", 3, 0.95, 0.96, 1, 0.995)
    print(free_chain.name, evaluate_flow(free_chain))
    # {'cell_rel': 0.95, 'e2e_pass_1': 0.4633, 'e2e_pass_k': 0.0213}
    print(hybrid.name, evaluate_flow(hybrid))
    # {'cell_rel': 0.99789, 'e2e_pass_1': 0.9937, 'e2e_pass_k': 0.9688}
```

Un système critique ne s’industrialise pas en visant $p = 0,9999$, mais en réduisant l’exposant $m$ des transitions probabilistes et en filtrant leurs sorties par du code déterministe.

---

## 17.9 Séparation entre plan de contrôle déterministe et cellule bornée

La section 17.2 décrit l’enveloppe déterministe dans sa forme BPMN. En voici une réalisation sur un moteur d’exécution durable : une machine à états déterministe pilote le processus et appelle, à des points fixés à la conception, une cellule bornée dont elle ne reçoit qu’une proposition.

![Architecture d’encapsulation hybride : épine dorsale déterministe gouvernant des cellules cognitives bornées avec gardes d’entrée/sortie et repli.](figures/fig-17-a-1.svg)

L’enveloppe se compose de quatre éléments.

1. **L’épine dorsale d’état durable** : exécutée sur Temporal, Restate ou un moteur BPMN 2.0/DMN, elle seule détient l’ordre légal des étapes, le journal d’événements rejouable, les clés d’idempotence, les compensations Saga et les budgets. Une injection de prompt ne peut pas sauter un contrôle compilé dans le graphe déterministe.
2. **La garde d’entrée** : avant toute inférence, elle valide le schéma amont, masque les renseignements personnels superflus (Loi 25, RGPD), filtre les motifs d’injection indirecte (OWASP ASI01) et assemble le plus petit contexte suffisant.
3. **La cellule bornée** : le modèle, SLM ou LLM, analyse les signaux ambigus ou non structurés. Ses outils MCP sont restreints à la lecture et à la simulation. Un compteur externe arrête la boucle à $K_{\max}$ tours.
4. **La garde de sortie et le disjoncteur** : la proposition passe par un décodage contraint (Structured Outputs), puis par une vérification déterministe des invariants (Cedar ou OPA, existence des références citées, seuil de confiance calibrée $\tau$). L’épine dorsale n’exécute l’écriture idempotente qu’après cette vérification. En cas de rejet, de dépassement de délai ou d’erreur HTTP 429, le disjoncteur route le dossier vers une règle statique sûre ou une file HOTL.

Deux règles de cette enveloppe vont au-delà de ce que retient l’exposé. Les outils de la cellule sont limités à la lecture et à la simulation; l’exposé admet qu’un outil d’agent borné soit une tâche de service, un sous-processus entier ou l’appel d’un autre processus, que le moteur exécute (section 17.2), et il donne à un agent ouvert accès aux systèmes d’enregistrement par un processus exposé comme outil (section 17.5). Le seuil $\tau$ s’ajoute aux issues nommées; l’exposé demande des issues nommées et routables, et ne tient le niveau de confiance que pour une information d’appoint, car un seuil reporte le problème sur le branchement suivant (section 17.2).

L’extrait suivant applique ce découpage au traitement d’une alerte d’équipement.

#### Extrait 17.2 — Machine à états déterministe (Temporal TypeScript) encapsulant une cellule cognitive

``` typescript
import { proxyActivities, ApplicationFailure } from "@temporalio/workflow";

export interface AlertWorkflowInput {
  readonly sagaId: string;
  readonly assetSerial: string;
  readonly criticalSla: boolean;
  readonly sensorDigest: string;
  readonly redactedNotes: string;
}

export interface DiagnosticProposal {
  readonly rootCauseCode: "BEARING_WEAR" | "VALVE_CAVITATION" | "THERMAL_OVERLOAD" | "SENSOR_DRIFT" | "UNKNOWN";
  readonly calibratedConfidence: number;
  readonly recommendedPartSku: string | null;
  readonly estimatedRepairCostCad: number;
  readonly citedHashes: ReadonlyArray<string>;
}

interface DeterministicActivities {
  checkContractDmn(assetSerial: string): Promise<{ covered: boolean; capCad: number }>;
  verifyInvariantsCedar(
    proposal: DiagnosticProposal,
    capCad: number,
    validHashes: ReadonlyArray<string>
  ): Promise<{ allowed: boolean; reason?: string }>;
  reservePartIdempotentMcp(sagaId: string, sku: string): Promise<{ reservationId: string }>;
  triggerDeterministicFallback(sagaId: string, reason: string): Promise<{ ticketId: string }>;
}

interface CognitiveCellActivities {
  runBoundedDiagnosticCell(args: {
    assetSerial: string;
    sensorDigest: string;
    notes: string;
    maxIterations: number;
    maxReasoningTokens: number;
  }): Promise<{ proposal: DiagnosticProposal; validHashes: string[] }>;
}

const det = proxyActivities<DeterministicActivities>({
  startToCloseTimeout: "5 seconds",
  retry: { maximumAttempts: 3 },
});

const cog = proxyActivities<CognitiveCellActivities>({
  startToCloseTimeout: "8 seconds",
  retry: {
    maximumAttempts: 2,
    nonRetryableErrorTypes: ["PromptInjectionError", "BudgetExhaustedError"],
  },
});

export async function resolveEquipmentAlertWorkflow(
  input: AlertWorkflowInput
): Promise<{ status: "AUTO_RESOLVED" | "FALLBACK_ESCALATED"; refId: string }> {
  // S1-S2 : Admissibilité contractuelle 100 % déterministe (DMN)
  const contract = await det.checkContractDmn(input.assetSerial);
  if (!contract.covered) {
    const fb = await det.triggerDeterministicFallback(input.sagaId, "CONTRACT_EXCLUDED");
    return { status: "FALLBACK_ESCALATED", refId: fb.ticketId };
  }

  // S3 : Cellule cognitive confinée (outils MCP lecture seule, K_max = 5, SLA 8 s)
  let proposal: DiagnosticProposal;
  let validHashes: string[];
  try {
    const out = await cog.runBoundedDiagnosticCell({
      assetSerial: input.assetSerial,
      sensorDigest: input.sensorDigest,
      notes: input.redactedNotes,
      maxIterations: 5,
      maxReasoningTokens: 2048,
    });
    proposal = out.proposal;
    validHashes = out.validHashes;
  } catch (err) {
    const code = err instanceof Error ? `CELL_ABORT:${err.message}` : "CELL_ABORT";
    const fb = await det.triggerDeterministicFallback(input.sagaId, code);
    return { status: "FALLBACK_ESCALATED", refId: fb.ticketId };
  }

  // Garde de sortie déterministe : confiance calibrée + politique Cedar + ancrage SHA-256
  const tau = input.criticalSla ? 0.90 : 0.82;
  if (proposal.calibratedConfidence < tau || proposal.rootCauseCode === "UNKNOWN") {
    const fb = await det.triggerDeterministicFallback(input.sagaId, "BELOW_CONFIDENCE_FLOOR");
    return { status: "FALLBACK_ESCALATED", refId: fb.ticketId };
  }

  const guard = await det.verifyInvariantsCedar(proposal, contract.capCad, validHashes);
  if (!guard.allowed) {
    const fb = await det.triggerDeterministicFallback(
      input.sagaId,
      `INVARIANT_REJECTED:${guard.reason ?? "POLICY"}`
    );
    return { status: "FALLBACK_ESCALATED", refId: fb.ticketId };
  }

  // S4 : Mutation transactionnelle idempotente exécutée hors du modèle
  if (!proposal.recommendedPartSku) {
    throw ApplicationFailure.nonRetryable("SKU manquant malgré validation garde.");
  }
  const res = await det.reservePartIdempotentMcp(input.sagaId, proposal.recommendedPartSku);
  return { status: "AUTO_RESOLVED", refId: res.reservationId };
}
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur bancaire et assurances — reproductibilité et explicabilité déterministe sous BSIF E-23**
:::

Pour les institutions financières fédérales soumises à la ligne directrice BSIF E-23 révisée (en vigueur le 1er mai 2027) et pour les assureurs assujettis à l’Annexe III de l’EU AI Act (décembre 2027), le découplage trace une frontière d’imputation des décisions que les équipes de gestion du risque de modèle peuvent vérifier.

1. **Extraction sourcée, par la cellule bornée** : le modèle structure les faits tirés de constats ou d’états financiers hétérogènes, et attache à chaque attribut la coordonnée exacte et l’empreinte du passage source.
2. **Adjudication déterministe, par table DMN ou moteur actuariel** : les calculs de ratios prudentiels, de franchises, d’exclusions légales et d’octroi restent codés dans des tables déterministes versionnées. Deux dossiers aux faits extraits identiques reçoivent, avec une probabilité de $1,000$, la même décision tarifaire et le même motif réglementaire opposable.
::::

---

## 17.10 Matrice d’arbitrage : API, RPA, BPMN/DMN, petit modèle et cellule bornée

Les critères de la section 17.6 désignent la région à confier au modèle; le tableau suivant guide le choix de la technologie d’exécution. Additionner des lignes de facture ou router un code postal avec un modèle génératif multiplie la latence par cent et le coût marginal par dix mille, et ajoute un risque d’erreur arithmétique. À l’inverse, maintenir dix mille expressions régulières pour interpréter des litiges techniques multilingues crée une dette fragile.

| Critère d’arbitrage | API / Microservice | RPA vs CUA encadré | BPMN 2.0 & Règles DMN | Travailleur SLM (Tâche) | Cellule LLM bornée |
|:-------------|:--------------|:-----------------|:----------------|:-------------------|:-----------------|
| Entrées types | JSON, Protobuf, EDI typé | Écrans patrimoniaux sans API | Attributs structurés, événements | Texte libre, PDF, journaux bruités | Signaux multi-sources ambigus |
| Mécanisme | Algorithme compilé exact | Sélecteurs UI (RPA) / Vision (CUA) | Machine à états & tables booléennes | Extraction mono-tour contrainte | Investigation bornée (`K <= 6`) |
| Latence $P_{95}$ | 5 à 80 ms | 2–15 s (RPA); 8–45 s (CUA) | 10 à 150 ms | 120 à 600 ms | 1,5 à 9,0 s |
| Coût unitaire | $< 0,0001$ \$ CAD | $0,005\text{–}0,08$ \$ CAD | $< 0,0005$ \$ CAD | $0,0005\text{–}0,005$ \$ CAD | $0,02\text{–}0,35$ \$ CAD |
| Constance $\text{pass}^5$ | $100\,\%$ | $92\text{–}98\,\%$ | $100\,\%$ | $94\text{–}99\,\%$ | $82\text{–}96\,\%$ brut ($> 99\,\%$ gardé) |
| Auditabilité | Immédiate (tests unitaires) | Moyenne (captures vidéo/journaux) | Maximale (tables lisibles métier) | Modérée (jeu étalon doré) | Forte uniquement sous garde |
| Rôle cible | Calculs, CRUD, mutations SI | Pont transitoire AS/400 / client lourd | Épine dorsale, barèmes et seuils | Triage massif, normalisation | Diagnostic complexe, exceptions |

Trois invariants règlent les combinaisons.

- **Aucune arithmétique probabiliste** : tout calcul monétaire, fiscal, calendaire ou physique s’exécute exclusivement en code déterministe ou en DMN (section 17.6).
- **Confinement des agents graphiques (CUA)** : quand un système patrimonial sans API exige une interaction par écran, le CUA est placé derrière un serveur MCP qui expose une opération atomique, encadrée d’assertions visuelles déterministes à chaque écran critique.
- **Chaînage SLM $\rightarrow$ DMN par défaut** : pour la majorité des dossiers administratifs, un SLM d’extraction qui alimente une table DMN remplace une boucle ReAct, plus coûteuse.

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Chaînes d'approvisionnement et réseaux critiques — continuité déterministe en cas de défaillance d'inférence**
:::

Un centre de distribution national, un répartiteur électrique ou une logistique hospitalière ne peut pas laisser une panne régionale d’API GPU immobiliser ses opérations physiques. L’architecture hybride impose un exercice trimestriel de débranchement cognitif : l’accès aux services d’inférence est coupé sur une fraction canari du trafic. En moins de 500 millisecondes, le disjoncteur de l’épine dorsale bascule sur ses règles statiques de secours : réapprovisionnement min/max standard SAP et routage déterministe vers les files d’opérateurs. L’organisation perd pour un temps l’optimisation fine de l’agent, mais conserve 100 % de sa continuité.
::::

---

## 17.11 Contrats d’entrée et de sortie typés, bornes d’exécution

Les issues nommées que demande la section 17.2 deviennent un contrat par quatre mécanismes, tous appliqués hors du modèle.

1. **Décodage contraint et énumérations fermées** : la sortie obéit à une grammaire stricte (JSON Schema Draft 2020-12, `additionalProperties: false`). Les codes d’action appartiennent à un ensemble `enum` fini, qui comprend une valeur d’abstention (UNKNOWN).
2. **Preuves d’ancrage par empreinte (SHA-256)** : chaque affirmation factuelle cite l’identifiant du fragment injecté et le préfixe de son empreinte. La garde de sortie le vérifie en $\mathcal{O}(1)$ et écarte les citations hallucinées.
3. **Plafond sur les jetons de raisonnement** : avec les modèles à calcul adaptatif au moment de l’inférence, borner les seuls jetons visibles laisse le modèle dépenser 20 000 jetons de réflexion cachée sur un cas ambigu. Le harnais plafonne donc séparément `max_output_tokens` et `max_reasoning_tokens`.
4. **Échéance temporelle monotone et confiance calibrée hors prompt** : avant chaque tour $k + 1 \le K_{\max}$, le harnais vérifie qu’il reste assez de millisecondes avant l’échéance SLA pour forcer une synthèse. L’attribut `calibratedConfidence` ne vient jamais d’une auto-évaluation rédigée par le modèle, systématiquement trop confiante lors d’une hallucination. Le harnais le calcule après coup, par étalonnage de température ou prédiction conforme sur les `logprobs` des jetons de l’énumération `rootCauseCode`, contre un jeu de validation hors échantillon.

Les bornes dépendent de la classe de cellule.

| Classe de cellule | Profil de modèle | Tours lecture ($K_{\max}$) | Plafond jetons réflexion | Latence $P_{99}$ max | Budget unitaire | Repli sur dépassement |
|:---------------|:--------------|:--------------|:--------------|:------------|:-----------|:-----------------|
| C1 — Extraction atomique | SLM 3B–14B | $0$ (mono-passe) | $0$ (désactivé) | $600\text{ ms}$ | $0,003$ \$ CAD | Modèle secondaire ou file saisie |
| C2 — Diagnostic opérationnel | SLM domaine / LLM rapide | $3$ à $5$ | $\le 2\,048$ | $8,0\text{ s}$ | $0,08$ \$ CAD | Synthèse partielle + escalade HOTL |
| C3 — Adjudication complexe | LLM de raisonnement | $4$ à $6$ | $\le 6\,144$ | $25,0\text{ s}$ | $0,35$ \$ CAD | Gel sans écriture + dossier CIBA |
| C4 — Méta-gouverneur critique | Famille LLM distincte | $0$ à $2$ | $\le 1\,536$ | $3,5\text{ s}$ | $0,05$ \$ CAD | *Fail-Closed* (blocage préventif L3) |

Le schéma de sortie de la cellule de diagnostic réunit ces contraintes.

#### Extrait 17.3 — Schéma JSON normatif de sortie bornée avec ancrage factuel (Draft 2020-12)

``` json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.boreal.ca/fabric/v2/diagnostic-output.json",
  "title": "BoundedDiagnosticCellOutput",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schemaVersion",
    "rootCauseCode",
    "calibratedConfidence",
    "uncertaintyFlags",
    "recommendedPartSku",
    "estimatedRepairCostCad",
    "evidenceCitations",
    "rationale"
  ],
  "properties": {
    "schemaVersion": { "const": "2.1.0" },
    "rootCauseCode": {
      "type": "string",
      "enum": ["BEARING_WEAR", "VALVE_CAVITATION", "THERMAL_OVERLOAD", "SENSOR_DRIFT", "UNKNOWN"]
    },
    "calibratedConfidence": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
    "uncertaintyFlags": {
      "type": "array",
      "maxItems": 4,
      "items": {
        "type": "string",
        "enum": ["CONFLICTING_SENSORS", "MISSING_LOG", "OUT_OF_DISTRIBUTION", "AMBIGUOUS_CLAUSE"]
      }
    },
    "recommendedPartSku": {
      "type": ["string", "null"],
      "pattern": "^[A-Z0-9]{3,8}-[A-Z0-9]{2,8}-[A-Z0-9]{2,6}$"
    },
    "estimatedRepairCostCad": { "type": "number", "minimum": 0.0, "maximum": 50000.0 },
    "evidenceCitations": {
      "type": "array",
      "minItems": 1,
      "maxItems": 6,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["chunkId", "sha256Prefix16"],
        "properties": {
          "chunkId": { "type": "string", "minLength": 4, "maxLength": 64 },
          "sha256Prefix16": { "type": "string", "pattern": "^[a-f0-9]{16}$" }
        }
      }
    },
    "rationale": { "type": "string", "minLength": 20, "maxLength": 500 }
  }
}
```

---

## 17.12 Application au fil rouge : Boréal Services Numériques et BCA

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Encapsulation des boucles d'investigation de pannes chez BSN et d'adjudication chez BCA**
:::

**Situation initiale (T4 2026)** : en parallèle de l’incident déclencheur à 41 000 \$ CAD, causé par un prototype d’achat qui avait bouclé pendant onze heures un dimanche sur une erreur HTTP 429 non gérée, Boréal Services Numériques (BSN) exploitait un agent d’investigation de pannes télématiques. C’était une boucle ReAct ouverte, qui exposait dix-neuf outils ServiceNow, Snowflake et Salesforce. Trois défauts bloquaient son passage à l’échelle.

1. *Inconstance des décisions* : rejouée cinq fois sur une même dérive de pression, la boucle concluait trois fois à une usure mécanique, une fois à un bruit de capteur, et modifiait une fois sans droit la priorité SLA du billet ($\text{pass}^5 = 61\,\%$).
2. *Tempêtes de requêtes* : au moindre ralentissement de Snowflake, l’agent relançait jusqu’à quatorze requêtes SQL redondantes. La latence $P_{99}$ montait à 142 s et le coût moyen à 1,85 \$ CAD par alerte.
3. *Veto réglementaire de BCA* : la direction des risques de Boréal Capital & Assurances (BCA) interdisait toute connexion aux polices bris de machine avant l’échéance BSIF E-23 du 1er mai 2027, faute de frontière prouvable entre le diagnostic probabiliste et le calcul contractuel de la franchise.

**Architecture déployée (février 2027)** : l’équipe remplace la boucle ouverte par le workflow Temporal de l’extrait 17.2.

- **Chez BSN** : l’épine dorsale assemble en amont les séries temporelles agrégées et retire des notes de terrain les identifiants d’employés (Loi 25). La cellule, de classe C2, n’accède plus qu’à 4 outils MCP en lecture seule, sous un plafond de $K_{\max} = 5$ tours, 2 048 jetons de raisonnement et 8,0 s. Sa sortie est conforme au schéma `BoundedDiagnosticCellOutput`.
- **Chez BCA** : le code de panne validé est transmis à un moteur déterministe DMN et Cedar, qui calcule exactement la couverture, le plafond annuel et la franchise selon les règles Guidewire / IBM i.
- **Repli** : pour les 3,1 % d’alertes hors distribution (`OUT_OF_DISTRIBUTION`) ou sous le seuil $\tau = 0,90$, le disjoncteur ouvre un dossier AG-UI à l’ingénieur de niveau 2, sans écriture risquée dans l’ERP.

**Résultats vérifiés sur 18 400 alertes (45 jours)** : la constance $\text{pass}^5$ passe de 61,0 % à 99,2 % (homologation interne BSIF E-23 obtenue), la latence $P_{99}$ de 142 s à 9,4 s, et le coût moyen d’inférence de 1,85 \$ CAD à 0,06 \$ CAD (-96,8 %).
::::

---

## 17.13 Décision d’architecture et liste de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-002 — Interdiction du routage global de processus critiques par inférence LLM non bornée**
:::

- **Statut** : acceptée \| Périmètre : Fabrique Agentique d’Entreprise (L2 à L4) \| Révision : semestrielle
- **Contexte** : une boucle agentique qui pilote librement des séquences d’outils à effets subit une chute exponentielle de fiabilité composée ($p^n$), des défaillances en cascade (OWASP ASI08) et des dérives de coût sur erreurs transitoires. Elle est incompatible avec l’auditabilité qu’exigent BSIF E-23, la Loi 25 et l’EU AI Act.
- **Options évaluées** :
  1. *Boucle LLM autonome de bout en bout, avec prompt durci* : rejetée. Une consigne textuelle ne garantit ni les invariants, ni la latence $P_{99}$, ni les budgets.
  2. *Exclusion totale des modèles génératifs des flux métiers* : rejetée. Elle maintient des délais manuels de 48 heures sur les pièces et les signaux non structurés.
  3. *Épine dorsale déterministe durable encapsulant des cellules bornées* : retenue. Les transitions d’état, les calculs DMN et Cedar et les écritures MCP idempotentes s’exécutent hors du modèle; le LLM est restreint à des cellules en lecture seule, validées par des gardes d’entrée et de sortie, avec circuit de repli.
- **Décision** : aucun flux critique ne confie son aiguillage global ni l’exécution directe d’écritures irréversibles à une boucle probabiliste ouverte. Toute cellule en production impose : (a) compteur externe $K_{\max}$, délai strict et plafond de jetons de raisonnement; (b) schéma JSON fermé, avec option d’abstention (UNKNOWN) et empreintes d’ancrage; (c) garde déterministe d’invariants avant toute écriture par l’épine dorsale; (d) repli déterministe testé chaque trimestre.
- **Conséquences** :
  - *Positives* : constance $\text{pass}^5 > 99\,\%$, maîtrise des coûts et des SLA, auditabilité réglementaire, continuité d’activité en cas de panne d’inférence.
  - *Négatives, coûts assumés* : modélisation explicite préalable des machines à états durables, des tables DMN et des contrats JSON.
- **Condition de révision** : réétalonnage semestriel des plafonds $K_{\max}$ et des seuils $\tau$, sur preuves statistiques tirées des bancs $\text{pass}^k$.
::::

### Liste de contrôle de mise en production

Huit exigences à valider avant de déployer un flux hybride.

1. **Homologation en constance** : le flux complet a-t-il franchi un banc d’au moins cent cas réels et contradictoires, mesuré en $\text{pass}^5$ et non en $\text{pass}@1$ ?
2. **Écritures et calculs hors du modèle** : règles tarifaires, seuils financiers, clés d’idempotence et appels MCP à effets s’exécutent-ils tous dans l’épine dorsale ?
3. **Lecture seule dans la cellule** : les outils exposés à la cellule sont-ils tous sans effet de bord irréversible ?
4. **Quatre plafonds** : le harnais borne-t-il $K_{\max}$, les jetons d’entrée et de sortie, les jetons de raisonnement caché et l’échéance temporelle monotone ?
5. **Droit à l’abstention** : le schéma JSON fermé (`additionalProperties: false`) prévoit-il un statut UNKNOWN et des drapeaux d’incertitude, contre les réponses fabriquées ?
6. **Contrôle des citations** : la garde de sortie vérifie-t-elle par calcul que chaque empreinte citée appartient au contexte injecté ?
7. **Test de débranchement cognitif** : la bascule en moins de 500 ms vers le mode dégradé, règles statiques ou file HOTL, est-elle prouvée sous injection d’erreurs HTTP 429 et HTTP 504 ?
8. **Opposabilité réglementaire** : peut-on isoler, devant un auditeur BSIF E-23 ou Loi 25, la table DMN ou la politique Cedar exacte qui a autorisé chaque transaction ?
