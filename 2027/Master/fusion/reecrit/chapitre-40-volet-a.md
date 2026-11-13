## Mise en œuvre — FinOps agentique : gouvernance économique et Cost-per-Outcome {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Le tarif catalogue au million de jetons baisse chaque année, mais la facture réelle des systèmes agentiques dérape souvent à la hausse : boucles inter-agents, raisonnement étendu, réinjection des schémas MCP et crédits d’action des éditeurs SaaS s’additionnent. Une facture mensuelle globale d’API signale le dépassement trente jours trop tard et ne distingue pas les agents créateurs de marge des agents déficitaires.
- **Décisions architecturales structurantes** :
  1.  *Irréversible à moyen terme* : Adopter le coût complet par résultat métier validé (*Cost-per-Outcome*, CPO) comme unité de gouvernance économique, en amortissant le coût des sagas avortées, des compensations et du temps de révision humaine (HOTL) sur les seuls dossiers résolus avec succès.
  2.  *Structurante dès le jour 1* : Implanter dans agentgateway et dans l’`ActionEnvelope` un disjoncteur budgétaire progressif en temps réel, qui fait passer un flux vers un petit modèle (SLM) économique avant d’interrompre proprement toute saga qui atteint son plafond monétaire.
  3.  *Réversible par conception* : La répartition du trafic entre modèles frontières infonuagiques et SLM spécialisés, réarbitrée chaque trimestre selon le couple coût/constance $\text{pass}^5$.
- **Indicateurs de gouvernance associés** : *Cost-per-Outcome* net par processus, comparé au coût humain de référence; taux de lecture du cache de préfixe ($\ge 75\,\%$); part des appels absorbés par des SLM ($\ge 70\,\%$); taux trimestriel de rationalisation du portefeuille.
::::

## 40.7 Le prix au million de jetons et le coût complet des systèmes multi-agents

Une direction financière qui budgète une initiative agentique avec la grille linéaire des copilotes de 2024 (nombre de requêtes multiplié par mille jetons) sous-estime le coût réel de production d’un facteur 8 à 25.

Cet écart tient à la dynamique multiplicative d’une saga autonome L3/L4. Un seul événement métier déclenche un orchestrateur qui sollicite trois spécialistes A2A; chacun exécute quatre cycles *ReAct* avec huit outils MCP et du raisonnement étendu, soit de quinze à trente inférences successives, chacune relisant l’historique et les schémas d’outils (section 40.1). L’ordonnancement qui casse l’affinité du cache ou les réessais d’une API tierce font monter la dépense sans alerte.

![Architecture du moteur FinOps agentique : agrégation temps réel des coûts complets, disjoncteur par saga et attribution du Cost-per-Outcome.](figures/fig-40-a-1.svg)

Les sept postes de coûts directs et cachés d’une transaction agentique, avec leur part typique dans un système non optimisé :

| Poste de coût complet | Mécanisme d’inflation en production | Part typique (non optimisé) | Levier d’optimisation (Standard 2027) |
|:----------------------|:------------------------------|:----------------|:------------------------------|
| **1. Jetons d’entrée répétés (prompts et schémas MCP)** | Réinjection à chaque tour de dizaines de schémas JSON verbeux, sans affinité de cache | 28 % – 38 % | Préfixes statiques canoniques, affinité de cache (lecture à 0,1 fois le prix d’entrée sur la plupart des modèles, section 40.6), moins de 12 outils actifs |
| **2. Jetons de raisonnement** | Génération de 4 000 à 12 000 jetons internes invisibles (tarif de sortie) sur des cas simples | 20 % – 35 % | Triage préalable par SLM et plafond `max_reasoning_tokens` par classe de tâche |
| **3. Échanges inter-agents (A2A)** | Prose narrative entre pairs au lieu de structures JSON compactes Apache Ossie | 8 % – 14 % | Sorties structurées strictes (Open Responses), sans politesse machine à machine |
| **4. Crédits d’action SaaS et API tierces** | Débit unitaire par appel d’agent éditeur, même lors de réessais ou de lectures vides | 10 % – 20 % | Cache de lecture à TTL court sur la passerelle et déduplication par clé d’idempotence |
| **5. Mémoire bi-temporelle et état durable** | Extraction d’entités par LLM à chaque écriture Graphiti et à chaque transition Temporal | 5 % – 9 % | Extraction déportée sur un SLM quantifié, en lot asynchrone; indexation sélective |
| **6. Sagas avortées, boucles et compensations** | Dossiers qui consomment 90 % de leur budget avant d’échouer sans résultat métier | 6 % – 15 % | Sentinelle anti-livelock (chapitre 33) et contrôle déterministe précoce des préconditions |
| **7. Révision humaine (HOTL)** | Temps d’examen d’un expert qualifié sur des escalades mal ciblées | Souvent omis; poste majeur du coût total | Calibrage des seuils Cedar et vue A2UI centrée sur le différentiel de preuves |

### Démonstration arithmétique sur une saga type de dix étapes

Le calcul ci-dessous retient une remise de 80 % sur l’entrée : c’est une hypothèse, car l’exposé relève une lecture du cache de préfixe à 0,1 fois le prix d’entrée sur la plupart des modèles, et à 0,05 ou 0,025 fois sur certains récents (section 40.6).

Deux implémentations d’une même saga d’instruction de dossier, à dix étapes cognitives, montrent l’effet du levier architectural :

- **Architecture naïve (Génération 2 non optimisée)** : Chaque étape appelle un modèle frontière (entrée à 3,00 \$ CAD / M jetons, sortie et raisonnement à 15,00 \$ CAD / M jetons), recharge 18 000 jetons de contexte et de catalogues d’outils non cachés, génère 2 500 jetons de raisonnement latent et 600 jetons de prose, et subit 18 % de sagas avortées ou reprises manuellement. Le coût direct d’une exécution atteint environ 1,01 \$ CAD, et 1,46 \$ CAD par résultat validé une fois amortis les échecs et la surcharge d’escalade HOTL. Sur 50 000 dossiers mensuels, la dépense annuelle atteint 876 000 \$ CAD.
- **Architecture AgentOps gouvernée (Standard 2027)** : Huit des dix étapes (qualification, extraction, formatage MCP, synthèse) passent par un SLM spécialisé à 0,12 \$ CAD / M jetons. Les deux seules étapes d’arbitrage complexe sollicitent le modèle frontière, avec un préfixe ordonné qui obtient 85 % de lectures en cache (remise de 80 % sur l’entrée) et un budget de raisonnement plafonné à 1 024 jetons. Le taux de réussite du premier coup franchit 96 %. Le coût complet amorti tombe à 0,13 \$ CAD par résultat validé, soit 78 000 \$ CAD par an pour le même volume métier : la facture est divisée par plus de onze et le temps de réponse médian diminue de 64 %.

------------------------------------------------------------------------

## 40.8 Modèle et attribution du *Cost-per-Outcome* (CPO)

Une facture mensuelle brute de *« 420 millions de jetons pour 18 400 \$ CAD »* ne dit pas si la plateforme crée de la richesse ou subventionne du gaspillage. L’unité d’œuvre métier auditable est le *Cost-per-Outcome* net (CPO), qui reprend le coût par résultat réussi de la section 40.5.

Un résultat métier validé n’est ni un message affiché, ni la fin technique d’un flux de travail sans exception : c’est l’accomplissement vérifié et durable de l’objectif d’affaires (garantie instruite non contestée sous 72 h, intervention préventive confirmée, facture rapprochée et comptabilisée). Pour que le coût des échecs ne soit pas masqué, le CPO net se calcule sur l’ensemble $\mathcal{S}$ des sagas exécutées sur la période, réussies, échouées ou compensées :

$$\text{CPO}_{\text{net}} = \frac{\sum_{s \in \mathcal{S}} \left( C_{\text{inf}}(s) + C_{\text{mcp}}(s) + C_{\text{mem}}(s) + C_{\text{hotl}}(s) \right)}{N_{\text{validés}} - N_{\text{annulés}}}$$

Dans cette équation, $C_{\text{inf}}(s)$ cumule le coût exact des *spans* d’inférence (tarif plein hors cache, tarif d’amorçage et de lecture du cache, tarif de sortie couvrant génération et raisonnement). $C_{\text{mcp}}(s)$ additionne les crédits d’outils tiers et les bacs à sable OpenSandbox, $C_{\text{mem}}(s)$ intègre les opérations de mémoire et d’exécution durable, et $C_{\text{hotl}}(s)$ valorise le temps réel de révision humaine au taux horaire chargé de l’approbateur. Au dénominateur, toute décision annulée ou reprise manuellement sous 72 heures ($N_{\text{annulés}}$) est déduite.

Le calcul de $C_{\text{inf}}(s)$ comporte un piège d’instrumentation : les fournisseurs d’inférence rapportent différemment les jetons lus en cache. Certains incluent `cache_read_input_tokens` dans `input_tokens`, d’autres ne rapportent dans `input_tokens` que le reliquat non caché. La passerelle agentgateway normalise donc `gen_ai.usage.input_tokens` en volume total d’entrée avant l’export OTLP, et l’entrepôt analytique protège la soustraction par un plancher `GREATEST(..., 0)`.

Hausser la constance $\text{pass}^5$ (chapitre 34) ou couper les boucles dès la deuxième répétition stérile (chapitre 33) réduit donc le CPO net.

#### Extrait 40.1 — Requête SQL analytique d’attribution du *Cost-per-Outcome* sur les *spans* OpenTelemetry

Exécutée toutes les heures dans l’entrepôt analytique alimenté par le flux OTel assaini, la requête rapproche les coûts complets des événements métiers validés :

``` sql
WITH span_costs AS (
    SELECT
        s.attributes['saga.id']::STRING                        AS saga_id,
        s.attributes['business.process.code']::STRING          AS process_code,
        GREATEST(
            COALESCE(s.attributes['gen_ai.usage.input_tokens']::INT, 0)
            - COALESCE(s.attributes['gen_ai.usage.cache_read_input_tokens']::INT, 0),
            0
        )                                                      AS uncached_in_tokens,
        COALESCE(
            s.attributes['gen_ai.usage.cache_read_input_tokens']::INT, 0
        )                                                      AS cached_in_tokens,
        COALESCE(s.attributes['gen_ai.usage.output_tokens']::INT, 0)
          + COALESCE(s.attributes['gen_ai.usage.reasoning_tokens']::INT, 0)        AS billable_out_tokens,
        COALESCE(s.attributes['mcp.external_api_cost_cad']::DOUBLE, 0.0)           AS mcp_api_cost_cad,
        COALESCE(s.attributes['memory.op_cost_cad']::DOUBLE, 0.0)                  AS mem_op_cost_cad,
        COALESCE(s.attributes['hotl.review_seconds']::DOUBLE, 0.0) * (84.0 / 3600) AS hotl_labor_cost_cad,
        p.uncached_in_per_1m_cad,
        p.cached_in_per_1m_cad,
        p.output_per_1m_cad
    FROM otel_clean.genai_spans s
    LEFT JOIN finops.model_pricing_catalog p
        ON s.attributes['gen_ai.response.model']::STRING = p.model_id
       AND s.start_time BETWEEN p.effective_from AND p.effective_to
    WHERE s.start_time >= DATEADD('day', -30, CURRENT_TIMESTAMP())
),
saga_full_cost AS (
    SELECT
        saga_id,
        ANY_VALUE(process_code) AS process_code,
        SUM(
            (uncached_in_tokens / 1e6) * COALESCE(uncached_in_per_1m_cad, 0)
          + (cached_in_tokens   / 1e6) * COALESCE(cached_in_per_1m_cad, 0)
          + (billable_out_tokens / 1e6) * COALESCE(output_per_1m_cad, 0)
          + mcp_api_cost_cad
          + mem_op_cost_cad
          + hotl_labor_cost_cad
        ) AS total_saga_cost_cad
    FROM span_costs
    GROUP BY saga_id
)
SELECT
    c.process_code,
    COUNT(c.saga_id)                                                       AS total_sagas_launched,
    COUNT_IF(o.outcome_status = 'VALIDATED' AND NOT o.reopened_within_72h) AS net_validated_outcomes,
    ROUND(SUM(c.total_saga_cost_cad), 2)                                   AS total_spend_cad,
    ROUND(
        SUM(c.total_saga_cost_cad)
        / NULLIF(COUNT_IF(o.outcome_status = 'VALIDATED' AND NOT o.reopened_within_72h), 0),
        4
    )                                                                      AS net_cost_per_outcome_cad
FROM saga_full_cost c
LEFT JOIN business_events.saga_outcomes o
    ON c.saga_id = o.saga_id
GROUP BY c.process_code
ORDER BY total_spend_cad DESC;
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Tarification des éditeurs SaaS en 2027 : pièges des crédits d’action et de la tarification au résultat**
:::

Les éditeurs SaaS B2B combinent désormais crédits d’action prépayés et tarification au résultat (section 40.4). Quatre garde-fous s’imposent à la négociation :

1.  **Gratuité contractuelle des erreurs et des vérifications d’idempotence** : Aucun crédit n’est débité lorsqu’un appel A2A ou MCP échoue (HTTP 429/5xx), renvoie un résultat vide ou rejoue une clé d’idempotence déjà exécutée.
2.  **Définition bilatérale et auditable du résultat** : Un abandon client ne compte pas comme une résolution; la facturation s’ancre sur un statut transactionnel vérifié, sans réouverture sous 72 heures.
3.  **Aucune surtaxe IA sur l’accès aux données du client** : Garantir que l’interrogation des tables métiers du client par des agents externes, via des serveurs MCP, ne subisse pas un tarif dissuasif destiné à imposer l’agent propriétaire de l’éditeur.
4.  **Plafonds programmables sans majoration punitive** : Exiger des alertes API en temps réel à 80 % et à 95 % de l’enveloppe, raccordées au moteur FinOps interne.
::::

------------------------------------------------------------------------

## 40.9 Disjoncteur budgétaire en temps réel et quatre leviers structurels

Pour qu’un emballement financier nocturne ne se reproduise pas, la gouvernance descend dans le plan de données synchrone (agentgateway) : un disjoncteur budgétaire progressif par saga réalise le plafond par exécution de la section 40.3. L’exposé tient toutefois un quota de jetons à la passerelle pour un frein, non pour un mur : le dépassement se constate après coup et des requêtes concurrentes peuvent excéder le plafond (section 40.3).

Chaque `ActionEnvelope` porte un plafond `maxTotalCostCad` proportionné à l’enjeu métier (p. ex. 1,20 \$ CAD pour une maintenance prédictive standard). À chaque traversée de la passerelle, un compteur atomique cumule la dépense de la saga et applique trois régimes gradués :

- **Zone nominale (\< 70 % du plafond)** : Routage vers les modèles nominaux du manifeste SemVer + Intent.
- **Zone d’économie forcée (`70 % à 100 %`)** : Plutôt que d’interrompre une saga presque achevée, la passerelle bascule l’appel vers le SLM de repli économique et limite `max_reasoning_tokens` afin de conclure proprement la synthèse.
- **Zone de coupure franche (`≥ 100 %`)** : Rejet immédiat `FINOPS_BUDGET_EXHAUSTED`; Temporal déclenche les compensations requises et la mise en file d’examen humain.

#### Extrait 40.2 — Middleware TypeScript de disjoncteur budgétaire progressif sur agentgateway

Le middleware cumule le coût de la saga, puis renvoie sa décision : poursuite, repli vers le SLM ou arrêt.

``` typescript
export interface BudgetStateStore {
  incrementAndGetCost(sagaId: string, deltaCostCad: number, ttlSeconds: number): Promise<number>;
}

export interface GatewayRoutingDecision {
  readonly action: "ALLOW_NOMINAL" | "DOWNGRADE_TO_SLM" | "ABORT_BUDGET_EXCEEDED";
  readonly effectiveModel: string;
  readonly effectiveMaxReasoningTokens: number;
  readonly remainingBudgetCad: number;
}

export async function enforceSagaBudgetPolicy(
  sagaId: string,
  maxBudgetCad: number,
  requestedModel: string,
  fallbackSlmModel: string,
  requestedReasoningTokens: number,
  lastStepCostCad: number,
  store: BudgetStateStore
): Promise<GatewayRoutingDecision> {
  const consumedCad = await store.incrementAndGetCost(sagaId, lastStepCostCad, 86_400);
  const ratio = consumedCad / maxBudgetCad;
  const remaining = Math.max(0, maxBudgetCad - consumedCad);

  if (ratio >= 1.0) {
    return {
      action: "ABORT_BUDGET_EXCEEDED",
      effectiveModel: "none",
      effectiveMaxReasoningTokens: 0,
      remainingBudgetCad: 0,
    };
  }
  if (ratio >= 0.70) {
    return {
      action: "DOWNGRADE_TO_SLM",
      effectiveModel: fallbackSlmModel,
      effectiveMaxReasoningTokens: Math.min(requestedReasoningTokens, 256),
      remainingBudgetCad: remaining,
    };
  }
  return {
    action: "ALLOW_NOMINAL",
    effectiveModel: requestedModel,
    effectiveMaxReasoningTokens: requestedReasoningTokens,
    remainingBudgetCad: remaining,
  };
}
```

Quatre leviers d’architecture, dont les principes figurent à la section 40.6, réduisent structurellement de 50 à 75 % le numérateur du CPO, à constance $\text{pass}^5$ égale :

1.  **Affinité stricte du cache de préfixe** : D’après la page de prix d’Anthropic, la lecture d’un préfixe déjà en cache coûte 0,1 fois le prix d’entrée sur la plupart des modèles, et 0,05 ou 0,025 fois sur certains récents (section 40.6) : il faut pour cela bannir tout horodatage ou UUID dynamique en tête de consigne système. Constitution statique et schémas d’outils triés figés en début de contexte, plus routage par affinité d’agent, portent le taux de lecture du cache au-delà de 80 %.
2.  **Cascade asymétrique SLM $\rightarrow$ LLM frontière** : Confier 75 % des étapes atomiques (triage, extraction JSON, formatage MCP) à des SLM de 7 à 14 milliards de paramètres, affinés sur les traces d’or validées au chapitre 34, pour un vingtième du coût d’un modèle frontière.
3.  **Allègement des schémas MCP** : Limiter chaque spécialiste à moins de douze outils cohérents plutôt que de recharger quarante définitions JSON verbeuses à chaque tour.
4.  **Traitement par lots différé sur les régimes T3/T4** : Diviser par deux le tarif fournisseur sur les analyses documentaires dont l’échéance opérationnelle tolère quelques heures.

### Arbitrage entre API infonuagiques gérées et grappes GPU internes

Faut-il auto-héberger ses modèles sur accélérateurs dédiés ou consommer des API facturées au jeton ? En 2027, la réponse FinOps est une architecture d’écrêtage hybride.

Pour les modèles frontières généralistes, dont l’obsolescence est trimestrielle, l’auto-hébergement reste déficitaire hors contraintes régaliennes : la sous-utilisation nocturne des grappes coûte plus cher que la marge infonuagique. Le calcul change avec un socle de spécialistes SLM (7B à 32B, servis par vLLM ou SGLang en lots continus) dont le taux d’occupation GPU dépasse 48 % sur 24 heures, lissé la nuit par les tâches analytiques T3/T4. Le coût marginal interne au million de jetons tombe alors 60 à 75 % sous les tarifs publics, et la résidence locale des données est garantie. La passerelle agentgateway absorbe le trafic de base à l’interne et ne déborde vers les API infonuagiques que lors des pointes ou pour les 20 % de raisonnements frontières complexes.

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Industrie et logistique à faible marge : protéger la marge unitaire lors des perturbations opérationnelles**
:::

Dans la distribution industrielle ou le transport, la marge nette d’une commande courante dépasse rarement 5 % (parfois moins de 8 \$ CAD). Lors d’un blizzard ou d’un blocage portuaire qui déclenche la replanification simultanée de 12 000 expéditions, laisser chaque saga activer son raisonnement maximal absorberait toute la marge des commandes sauvées.

La règle FinOps industrielle indexe donc le plafond de l’enveloppe sur la marge contributive (`maxTotalCostCad = min(PlafondAbsolu, 0,08 * MargeCommande)`). Les flux courants passent par des heuristiques L0 et des SLM sobres; l’orchestration cognitive profonde est réservée aux équipements critiques soumis à des pénalités SLA majeures.
::::

------------------------------------------------------------------------

## 40.10 Refacturation interne et rationalisation trimestrielle du portefeuille

Financer toute l’inférence sur le budget central des TI encourage la prolifération d’agents d’utilité marginale. Passer de l’affichage des coûts à la refacturation interne réelle aux centres de coûts métiers responsabilise immédiatement les divisions. Cette refacturation, que l’ADR-023 impose à tout flux L2–L4, va au-delà de ce que retient l’exposé : afficher d’abord les coûts sans les refacturer, et ne refacturer qu’une fois la clé d’imputation fiable (section 40.2 et grille de décision).

Quand une saga transversale franchit plusieurs divisions (par exemple une alerte télématique initiée chez BSN, qui sollicite un spécialiste garantie chez BCA puis une réservation chez BEL), la règle d’imputation propage le centre de coûts donneur d’ordre (`finops.origin_cost_center`) dans le W3C Baggage. L’intégralité du coût variable est refacturée au processus métier bénéficiaire du résultat final. Une division qui fournit des outils MCP ou A2A n’a ainsi pas à brider ses propres quotas pour se protéger des demandes internes.

#### Extrait 40.3 — Politique déclarative de refacturation interne (*Chargeback*) multi-divisions

La politique déclare l’imputation, le socle partagé et, pour chaque division, les seuils mensuels et le comportement au dépassement :

``` yaml
apiVersion: finops.boreal.ca/v1
kind: InternalChargebackPolicy
metadata:
  fiscalYear: 2027
  currency: CAD
  billingCadence: monthly
spec:
  directVariableAttribution:
    correlationKey: "saga.id"
    passThroughAtActualCost:
      - "otel.gen_ai.inference_spend"
      - "otel.mcp.external_saas_credits"
  sharedPlatformAllocation:
    monthlyFixedPoolCad: 28500.00
    allocationFormula: "70% pro-rata sagas + 30% pro-rata jetons totaux"
  businessUnits:
    - divisionId: BEL
      costCenter: "CC-4100-LOG-MFG"
      monthlySoftAlertCad: 18000.00
      monthlyHardCapCad: 24000.00
      overCapBehavior: "restrict-l1-assistants-preserve-l3-production"
    - divisionId: BCA
      costCenter: "CC-2200-FIN-INS"
      monthlySoftAlertCad: 22000.00
      monthlyHardCapCad: 30000.00
      overCapBehavior: "require-vp-ciba-override"
    - divisionId: BSN
      costCenter: "CC-3300-SAAS-OPS"
      monthlySoftAlertCad: 32000.00
      monthlyHardCapCad: 42000.00
      overCapBehavior: "enforce-slm-tier-on-standard-tenants"
```

Chaque trimestre, le comité conjoint (CTO, CFO, métiers) arbitre le registre d’agents selon quatre décisions normatives :

| Profil observé sur 90 jours | Constance $\text{pass}^5$ | CPO par rapport à la référence (humain ou L0) | Décision obligatoire du comité de portefeuille |
|:--------------------|:-----------------|:---------------------------|:-----------------------------------|
| **1. Champion stratégique** | $\ge 0,95$ | Gain net $> 3\times$ et forte baisse du délai de cycle | **Industrialiser et étendre** : déploiement multi-pays et durcissement des contrats MCP |
| **2. Efficace mais dispendieux** | $\ge 0,95$ | Valeur prouvée, mais coût LLM élevé à grand volume | **Distiller (LLM $\rightarrow$ SLM)** : affiner un SLM interne sur les traces d’or (-85 % de coût) |
| **3. Sur-ingénierie cognitive** | $\ge 0,92$ | Arbre de décision fixe payé au tarif d’un agent L3 | **Rétrograder en L0 déterministe** : convertir en workflow Temporal ou en SQL pur |
| **4. Zombie ou destructeur de marge** | $< 0,85$ ou usage marginal | CPO complet supérieur à celui du processus initial (révision humaine incluse) | **Mettre hors service sous 15 jours** : révoquer l’identité NHI et libérer le budget |

------------------------------------------------------------------------

## 40.11 Application au fil rouge : gouvernance économique chez Groupe Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : Zéro récidive de l'incident à 41 000 \$ CAD et baisse de 61 % du coût par dossier**
:::

**Point de départ (Automne 2026)** : Groupe Boréal dépensait 74 000 \$ CAD/mois sur 47 initiatives disparates sans indicateur de valeur et venait de subir la boucle incontrôlée de onze heures sur erreur HTTP 429 à 41 000 \$ CAD un dimanche chez BEL. Le mandat exécutif exigeait -55 % de coût d’inférence par dossier traité.

**Transformation FinOps sur T1–T2 2027** :

1.  **Disjoncteur par saga** : Activation universelle du disjoncteur `enforceSagaBudgetPolicy` sur agentgateway. Lors d’une panne réelle de la passerelle EDI X12 d’un transporteur, un dimanche de février, 42 sagas logistiques basculent en SLM à 0,84 \$ CAD puis se mettent proprement en pause à 1,20 \$ CAD : la facture totale de l’incident est contenue à 50,40 \$ CAD, contre 41 000 \$ CAD quatre mois plus tôt.
2.  **Cache et distillation SLM** : La normalisation des préfixes système fait passer le taux de lecture du cache de 19 % à 84,6 %, tandis que deux SLM de 14 milliards de paramètres hébergés chez BSN absorbent 76 % des appels d’inférence du groupe sans dégrader le score $\text{pass}^5$.
3.  **Rationalisation du portefeuille** : La première revue de refacturation interne, en mars 2027, conduit à mettre hors service 7 agents « zombies » déficitaires, à rétrograder 4 pseudo-agents en workflows déterministes Temporal L0 (coût divisé par 400), et à réallouer l’enveloppe dégagée vers l’extension européenne de la plateforme télématique.

**Bilan audité à fin T2 2027** :

- **Baisse du coût moyen d’inférence et d’orchestration par dossier validé** : -61,4 % (au-delà de la cible exécutive de -55 % fixée dans le mandat annuel).
- ***Cost-per-Outcome* net du flux de maintenance prédictive** : abaissé de 0,38 \$ CAD lors du pilote initial à 0,19 \$ CAD tout compris (révision humaine et échecs amortis), pour 3 400 \$ CAD de casse matérielle et de pénalités contractuelles évitées en moyenne par intervention.
- **Variance budgétaire mensuelle** : stabilisée sous ±3,5 %, ce qui fait de l’intelligence artificielle une ligne industrielle à marge unitaire gouvernée, et non plus un centre de coûts imprévisible.
::::

------------------------------------------------------------------------

## 40.12 Décision d’architecture normative et points de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-023 — Pilotage FinOps par le Cost-per-Outcome, disjoncteurs par saga et refacturation interne**
:::

- **Statut** : Acceptée \| Périmètre : FinOps IA & Contrôle de Gestion \| Révision : Semestrielle
- **Contexte** : L’autonomie multi-agents expose l’entreprise à une forte variance des coûts unitaires (boucles, raisonnement étendu, crédits SaaS) que les plafonds mensuels globaux ne détectent qu’après sinistre, sans corrélation avec la valeur créée.
- **Options évaluées** :
  1.  *Quotas mensuels globaux par clé d’API* : Paralyse toute une division en fin de mois lorsqu’un seul agent dérive. Rejetée.
  2.  *Sélection systématique du modèle le moins cher au million de jetons* : Dégrade $\text{pass}^5$, multiplie réessais et escalades HOTL, et renchérit le coût complet par résultat. Rejetée.
  3.  *Gouvernance par le Cost-per-Outcome net (CPO), disjoncteur progressif par saga sur agentgateway et refacturation interne* : Protège chaque transaction en temps réel et aligne l’architecture sur la marge métier vérifiée. Retenue.
- **Décision** : Tout flux L2–L4 doit définir un événement formel de résultat validé, imposer un plafond `maxTotalCostCad` dans son `ActionEnvelope` contrôlé par disjoncteur progressif, refacturer ses coûts complets (échecs et HOTL inclus) à sa division métier et subir un arbitrage trimestriel de portefeuille.
- **Conséquences** :
  - *Positives* : Risque d’emballement financier freiné, non exclu (un plafond est un frein, pas un mur : section 40.3), élimination naturelle des cas d’usage sans ROI, autofinancement du socle par les gains unitaires prouvés.
  - *Négatives / Coûts assumés* : Instrumentation des événements de clôture métier dans les systèmes d’enregistrement et mise à jour continue du barème multi-modèles.
- **Condition de révision** : Révision semestrielle des barèmes fournisseurs et des seuils de distillation SLM.
::::

### Liste de contrôle de mise en production

1.  **Événement métier joint** : Un événement transactionnel vérifiable alimente-t-il automatiquement le dénominateur net du *Cost-per-Outcome* (hors réouvertures sous 72 h) ?
2.  **Amortissement intégral** : Le numérateur du CPO inclut-il les sagas échouées, les compensations, les crédits d’outils tiers et le temps de révision humaine ?
3.  **Disjoncteur progressif actif** : Chaque saga porte-t-elle un plafond `maxTotalCostCad` appliqué en ligne par agentgateway, avec repli SLM à 70 % et arrêt propre à 100 % ?
4.  **Affinité de cache vérifiée** : Les préfixes système sont-ils exempts de champs dynamiques, pour plus de 75 % de lectures en cache ?
5.  **Plafond de raisonnement borné** : Le paramètre `max_reasoning_tokens` est-il calibré par tâche plutôt que laissé sans limite ?
6.  **Cascade SLM prioritaire** : Les tâches atomiques d’extraction et de triage sont-elles servies par des SLM qualifiés en $\text{pass}^5$ ?
7.  **Protection contre la double taxation SaaS** : Les connecteurs d’agents tiers excluent-ils le débit de crédits sur erreurs techniques et doublons d’idempotence ?
8.  **Rattachement de la refacturation et arbitrage** : Chaque agent possède-t-il un centre de coûts métier imputable et une revue trimestrielle planifiée ?
