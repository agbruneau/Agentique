## Mise en œuvre — Cycle de vie ADLC, CI/CD probabiliste, simulation (τ-bench) et ingénierie du chaos {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Transposer les pipelines d’intégration continue du logiciel déterministe (`assert f(x) == y`) ou les bancs d’essai statiques à tour unique du MLOps expose un programme agentique à des régressions en production. Un agent qui affiche 92 % de réussite sur des questions isolées échoue souvent une fois sur deux dans un dialogue réel de huit tours, qui mêle ambiguïté humaine, mutations d’état et lenteurs d’API.
- **Décisions architecturales structurantes** :
  1.  *Irréversible à moyen terme* : Adopter un cycle de vie agentique (ADLC) fondé sur un registre d’agents immuable, versionné en SemVer + Intent. Toute modification de prompt, de paquet Agent Skills, de schéma MCP, de poids de modèle ou de politique Cedar produit un artefact qualifié.
  2.  *Structurante dès le jour 1* : Remplacer $\text{pass}@k$ et les juges automatiques superficiels par des environnements multi-tours normalisés (OpenEnv, famille $\tau$-bench), qui vérifient l’état final exact des bases simulées, et exiger une constance $\text{pass}^k$ stricte ($\text{pass}^5 \ge 0,95$ sur les parcours critiques).
  3.  *Réversible par conception* : Calibrer les paliers de déploiement progressif (mode fantôme, canari à 5 % → 25 % → 100 %) et composer les profils adversariels injectés dans la suite de chaos.
- **Indicateurs de gouvernance associés** : Score de constance $\text{pass}^5$ par domaine critique, survie sans corruption d’état sous chaos protocolaire (taux de survie au chaos = 100 %), temps de retour arrière automatisé inférieur à 30 s, conversion systématique des incidents réels en tests permanents.
::::

## 34.8 Du SDLC déterministe à l’ADLC : gouverner six vitesses de changement par SemVer + Intent

Le cycle de vie agentique (ADLC) prolonge celui du génie logiciel classique (SDLC). Son unité de livraison est l’agent complet, composite et immuable, versionné en SemVer + Intent : c’est le manifeste de version proposé à la section 34.2, ici précisé.

Le comportement d’un spécialiste L3 résulte de six couches qui évoluent à des cadences distinctes : le contrat A2A externe, le point de contrôle exact du modèle (LLM ou SLM), les compétences modulaires (Agent Skills) avec les schémas JSON des serveurs MCP invoqués, le prompt système avec les directives de dépôt (`AGENTS.md`), les politiques déterministes Cedar ou OPA qui bornent son enveloppe d’action, et le code d’infrastructure. Une modification de l’une d’elles est qualifiée par un pipeline CI/CD qui revalide l’ensemble. Les sections 34.1 et 34.2 ajoutent la mémoire aux unités de changement, et le manifeste de version regroupe les politiques de garde-fous et de mémoire; ces six couches ne la nomment pas.

![Pipeline CI/CD probabiliste du cycle de vie ADLC : du registre SemVer+Intent au déploiement Canary sous contrôle pass\^5 et chaos.](figures/fig-34-a-1.svg)

Dans la notation `MAJEUR.MINEUR.CORRECTIF+intent.<empreinte>`, les trois segments numériques suivent la compatibilité contractuelle de l’Agent Card A2A v1.0; le suffixe d’intention scelle cryptographiquement toutes les dépendances cognitives et protocolaires.

| Couche modifiée de l’artefact | Exemple concret de changement | Impact SemVer + Intent | Suites de qualification CI/CD obligatoires |
|:-------------------|:---------------------------|:-------------------|:---------------------------------|
| 1. Contrat A2A externe | Rupture sur `outputSchema` d’une compétence publiée | Incrément MAJEUR (3.0.0) | Contrats consommateurs, suite complète $\tau$-bench ($\text{pass}^5$), chaos complet, canari long |
| 2. Modèle (LLM / SLM) | Nouvelle révision de poids ou ajustement du budget de raisonnement | Incrément MINEUR + nouvel `intent` | Suite complète $\tau$-bench ($\text{pass}^5$), étalonnage coût/latence, mode fantôme de 24 h |
| 3. Agent Skills et schémas MCP | Ajout d’un 9e outil MCP ou refonte d’un module Agent Skill | Incrément MINEUR (2.5.0) | Tests de surcharge d’outils, simulation multi-tours, chaos sur le nouvel outil |
| 4. Prompt système et `AGENTS.md` | Clarification d’une règle de priorité documentaire | Incrément CORRECTIF + nouvel `intent` | Suite ciblée $\tau$-bench ($\text{pass}^5$ cas d’or) + contrôle anti-injection |
| 5. Politiques Cedar / OPA | Abaissement du seuil HOTL de 5 000 \$ CAD à 3 500 \$ CAD | Révision liée au manifeste | Preuve formelle déterministe (100 % cas limites) + simulation escalade CIBA |
| 6. Code d’infrastructure pur | Optimisation du sérialiseur OTLP hors graphe et hors prompts | Incrément CORRECTIF (2.4.2) | Tests unitaires/intégration déterministes + test de fumée |

#### Extrait 34.1 — Manifeste normatif du Registre d’Agents d’Entreprise (SemVer + Intent)

Le pipeline CI signe ce manifeste avant sa publication dans l’annuaire interne compatible AGNTCY / OASF; il interdit tout écart entre le banc d’essai et la production.

``` yaml
apiVersion: agentops.boreal.ca/v1
kind: AgentReleaseManifest
metadata:
  agentId: boreal-bca-warranty-adjudicator
  version: "2.4.0+intent.9f3a81c"
  division: BCA
  autonomyLevel: L3
  regulatoryClassification:
    bsifE23MaterialityTier: Tier-2-High
    quebecLoi25AutomatedDecision: true
    ownerTeam: coe-garanties-bca@boreal.ca
spec:
  a2aCardDigest:
    "sha256:d0ad65640398d3fdab95fa3c7b6719e1fe574f9f0d94ef071c9d08d9a7770867"
  cognitivePinning:
    # Point de contrôle daté fixe (alias flottant interdit)
    primaryModel: "claude-sonnet-4-6-20261114"
    fallbackSlm: "oci://registry.boreal.ca/slm/qwen3-14b-warranty:3.1.0"
    fallbackSlmDigest:
      "sha256:2bcf2ed0dcfe35c6aca8780afe3d7e9940f39a341e79cff8d402c0f59ddf4b6a"
    temperature: 0.0
    maxReasoningTokens: 2048
    systemPromptDigest:
      "sha256:c8728ba34fbba31aa8a4cc64ad8626bd25dbb5316437f4c59f508c9f5df55c68"
  packagedSkills:
  - name: "as400-endorsement-clause-parser"
    version: "1.3.2"
    digest:
      "sha256:8cb8d13abb2adc37dd0d12b8085270d0fa24e20928ac7cadf30693346fdefdf8"
  pinnedMcpDependencies:
  - serverUri: "https://mcp.bca.internal.boreal.ca/as400-contracts"
    schemaVersion: "2027.02"
    allowedTools:
      - "get_master_lease_contract"
      - "list_active_warranty_endorsements"
      - "issue_provisional_coverage_token"
  policyBundle:
    engine: cedar
    bundleVersion: "bca-warranty-pdp-v4.8"
    digest:
      "sha256:a20a4166692c30cc694a9fe543e4a314eef7a05a4021efd3cb127415e300f95c"
  homologationGates:
    benchmarkSuite: "boreal-taubench-bca-warranty-v5"
    requiredPassPower5Critical: 0.95
    requiredPassPower5Global: 0.88
    requiredChaosSurvivalRate: 1.00
    maxP95CostPerOutcomeCad: 0.45
```

La directive `cognitivePinning` applique l’épinglage de la section 34.2 : aucun agent L2 ou L3 (échelle d’autonomie de l’ouverture, section 0.4) ne peut référencer un alias flottant tel que `latest`; l’identifiant daté exact du modèle (ou le condensat SHA-256 des poids d’un SLM interne) est figé dans le manifeste.

------------------------------------------------------------------------

## 34.9 Simulation multi-tours (OpenEnv et famille $\tau$-bench) : $\text{pass}^k$ plutôt que $\text{pass}@k$

Évaluer un agent sur cinquante paires statiques question-réponse, notées par similarité textuelle ou par un juge automatique indulgent, laisse échapper les échecs d’un dialogue. L’agent échoue rarement au premier tour : il échoue au quatrième quand l’interlocuteur se ravise, au cinquième quand un retour d’outil MCP est ambigu, au sixième quand il oublie une restriction contractuelle lue au début de l’échange.

Deux standards complémentaires structurent l’évaluation avant déploiement en 2027 :

1.  **Environnements d’évaluation normalisés (OpenEnv, Linux Foundation AAIF)** : OpenEnv encapsule de façon reproductible un jumeau transactionnel léger : un état initial de base de données (contrats, stocks, billets), des serveurs MCP simulés déterministes et des sondes d’invariants métiers.
2.  **Bancs d’essai interactifs $\tau$-bench, $\tau^2$-bench et $\tau^3$-bench** : le harnais confronte l’agent à un simulateur d’utilisateur ou de pair piloté par un objectif, qui varie ses formulations et distille ses informations au fil du dialogue. Le verdict ne repose pas sur la qualité du texte généré, mais sur l’égalité déterministe entre l’état final de la base après la conversation et l’état cible unique que dictent les règles d’affaires.

### La mesure $\text{pass}^k$

La section 34.2 définit $\text{pass}^k$. Il s’oppose à $\text{pass}@k$, que la synthèse de code assistée utilise volontiers : la probabilité qu’au moins un essai parmi $k$ générations résolve le problème. Ce critère vaut quand un compilateur filtre gratuitement dix essais avant d’en retenir un. En opérations d’entreprise, la contrainte est inverse : l’agent n’a pas cinq essais devant un client ou un règlement financier, et il doit réussir chacun des $k$ dossiers analogues malgré la variabilité des dialogues. Sur $n$ exécutions indépendantes d’un scénario ayant produit $c$ succès, les deux mesures divergent :

$$\text{pass}@k = 1 - \frac{\binom{n - c}{k}}{\binom{n}{k}}, \qquad \text{pass}^k = \frac{\binom{c}{k}}{\binom{n}{k}} \approx \left(\frac{c}{n}\right)^k$$

Un agent dont la précision unitaire est $p = 0,80$ obtient un $\text{pass}@5 = 1 - 0,20^5 = 99,97\,\%$, mais son $\text{pass}^5 = 0,80^5$ tombe à 32,77 % : au moins une faute métier dans deux tiers des séries de cinq dossiers. Exiger $\text{pass}^5 \ge 0,95$ sur les parcours critiques impose une fiabilité unitaire minimale de $0,95^{1/5} \approx 98,98\,\%$, qui ne peut être atteinte qu’en déportant calculs et garde-fous dans des outils MCP déterministes et des règles Cedar. Ce seuil, comme ceux du manifeste de l’extrait 34.1, va au-delà de ce que retient la section 34.2 : un seuil sur $\text{pass}^k$, dont l’exemple illustratif est 90 % sur quatre tentatives.

Avec exactement $n = k = 5$ trajectoires par scénario, l’estimateur combinatoire sans biais $\binom{c}{5}/\binom{5}{5}$ est binaire ($\{0, 1\}$) pour un scénario isolé. La barrière de promotion évalue donc la moyenne $\overline{\text{pass}^5}$ sur un corpus minimal de $M \ge 100$ scénarios par domaine, vérifie la borne inférieure de l’intervalle de confiance de Wilson à 95 %, et impose zéro violation de politique sur chaque scénario critique.

### Étalonnage des simulateurs

Le modèle qui anime l’utilisateur simulé, comme les évaluateurs sémantiques auxiliaires, demande une hygiène méthodologique. Trois pièges faussent les bancs d’essai internes mal conçus :

- **Collusion de famille de modèles** : quand l’utilisateur simulé (ou un juge de conformité rédactionnelle) vient de la même famille de poids que l’agent évalué, tous deux partagent des angles morts corrélés, ce qui gonfle le score $\text{pass}^5$ de 6 à 11 points par rapport au trafic humain réel. La norme d’architecture impose une hétérogénéité croisée : l’agent testé fait face à des profils animés par une famille de modèles distincte.
- **Dérive vers des dialogues trop coopératifs** : les modèles alignés par apprentissage par renforcement produisent par défaut des utilisateurs simulés courtois, structurés et patients. La distribution des profils est donc stratifiée à partir des grappes observées dans les traces anonymisées (messages elliptiques de trois mots, fautes de frappe sur les références d’équipement, impatience explicite dès le quatrième tour).
- **Primauté de l’assertion déterministe** : comme à la section 34.3, le contrôle déterministe prime. Au moins 80 % de la décision de passage repose sur l’inspection programmatique de l’état final des tables simulées, des événements Kafka émis et des journaux Cedar. Les 20 % restants, confiés à un modèle critique indépendant, se limitent aux propriétés non relationnelles : absence de divulgation d’instructions internes, clarté de l’explication fournie au client (Loi 25), justesse du résumé transmis à un superviseur HOTL.

| Référentiel / Métrique | Topologie d’interaction simulée | Mode de vérification du verdict | Angle mort corrigé | Usage cible dans le pipeline ADLC |
|:----------------|:-------------------------|:--------------------|:--------------------|:------------------|
| Évaluation à tour unique | Question isolée → Réponse statique | Similarité lexicale ou juge automatique | Aucun suivi d’état ni d’outil | Filtrage rapide des extracteurs L0/L1 |
| $\tau$-bench (classique) | Agent outillé (MCP) $\leftrightarrow$ utilisateur simulé; seul l’agent mute la base | Assertion exacte sur l’état final de la base + politique | Détecte l’oubli de règles sur 5 à 15 tours | Barrière CI standard de tout spécialiste L2/L3 |
| $\tau^2$-bench (double contrôle) | L’agent et l’utilisateur agissent simultanément sur l’état partagé | Convergence de l’état couplé (monde client + SI) | Détecte les conflits quand le client agit en parallèle | Dépannage technique interactif, support IT/OT |
| Environnements fédérés | Graphe multi-agents A2A complet sous horizons longs et bruit | État distribué multi-domaines + budget/sécurité | Détecte les pannes en cascade (ASI08) inter-divisions | Homologation des sagas transversales L3 |
| Seuil $\text{pass}^5$ vs $\text{pass}@1$ | $k=5$ trajectoires stochastiques par scénario (profils variés) | Exigence de 5/5 convergences sans violation | Écarte les agents performants mais irréguliers | Critère bloquant de mise en production |

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Service client à haut volume (télécoms, commerce, SaaS) : double contrôle et incohérence humaine**
:::

Dans un centre de contact qui traite 80 000 interactions par jour, les agents échouent principalement parce que l’interlocuteur modifie lui-même l’état du monde et change d’intention en cours de dialogue, ce que modélise $\tau^2$-bench.

Pendant qu’un agent diagnostique une passerelle optique, l’abonné débranche un câble sans le mentionner, refuse une option au tour 4, exige la résiliation au tour 6, puis accepte un technicien au tour 9 en changeant d’adresse. La suite OpenEnv d’un service client à fort volume doit donc tester systématiquement quatre archétypes synthétiques :

1.  L’interlocuteur fragmentaire, qui tait les informations clés tant que l’agent ne pose pas les questions de diagnostic.
2.  L’acteur à double contrôle, qui modifie un paramètre local ou un panier dans un autre canal et invalide les lectures faites trois tours plus tôt.
3.  L’indécis contradictoire, qui inverse sa demande après une pré-réservation : l’agent doit déclencher l’outil de compensation avant d’engager la nouvelle action.
4.  Le négociateur persuasif hors politique, qui invoque une urgence émotionnelle crédible pour obtenir un geste commercial supérieur au plafond L3.
::::

------------------------------------------------------------------------

## 34.10 Ingénierie du chaos agentique

Réussir $\text{pass}^5 \ge 0,95$ sur des serveurs simulés qui répondent en 40 millisecondes ne suffit pas. L’incident initial du Groupe Boréal (41 000 \$ CAD consommés en onze heures un dimanche chez BEL, sur une erreur HTTP 429 mal gérée) montre que la sûreté d’un agent se juge à son comportement quand son environnement se dégrade.

L’ingénierie du chaos agentique applique au pipeline CI/CD l’épreuve sous conditions dégradées de la section 34.7 : elle injecte cinq classes de perturbations reproductibles sur les flux MCP et A2A.

1.  **Chaos de débit et de transport (HTTP 429, 503, coupures SSE)** : vérifier que l’agent respecte Retry-After, n’invente jamais une confirmation fictive lorsque l’outil échoue (faux succès) et bascule proprement vers le repli ou la mise en veille.
2.  **Chaos de latence asymétrique** : injecter un délai de 14 secondes sur un serveur MCP patrimonial pour prouver que les clés d’idempotence bloquent toute double écriture en cas de relance d’activité Temporal.
3.  **Chaos de dérive sémantique et de troncature** : retourner un JSON valide mais partiel (`null` inattendu, devise non convertie) pour vérifier que l’agent déclenche une escalade HOTL plutôt que d’inventer une valeur.
4.  **Chaos de préconditions périmées** : simuler l’épuisement de la dernière pièce entre la lecture et la réservation pour valider l’exécution exacte des compensations de la saga.
5.  **Chaos adversariel (OWASP ASI01 / ASI04)** : insérer dans les textes qu’un outil documentaire retourne une injection indirecte qui tente de provoquer un appel d’outil non autorisé.

#### Extrait 34.2 — Harnais Python d’évaluation multi-tours OpenEnv calculant $\text{pass}^5$ sous chaos MCP

Le proxy injecte des erreurs HTTP 429 reproductibles par graine et compte les clés d’idempotence reçues. La fonction rejoue chaque scénario dans une base neuve, compare l’état final à l’état attendu et ne valide la barrière que si les seuils critique et global sont atteints, sans violation de politique.

``` python
from dataclasses import dataclass
import math
import random
from typing import Callable, Dict, Sequence

@dataclass
class ScenarioSpec:
    scenario_id: str
    critical: bool
    initial_db_snapshot: Dict[str, object]
    expected_final_db_state: Dict[str, object]
    user_goal_prompt: str

class McpChaosProxy:
    """Proxy OpenEnv injectant des fautes protocolaires reproductibles par graine."""
    def __init__(self, real_router: Callable, seed: int, rate_429: float = 0.15) -> None:
        self._router = real_router
        self._rng = random.Random(seed)
        self._rate_429 = rate_429
        self.mutating_keys_seen: Dict[str, int] = {}

    async def call_tool(self, tool_name: str, args: Dict[str, object]) -> Dict[str, object]:
        idem_key = str(args.get("idempotencyKey", ""))
        if idem_key:
            self.mutating_keys_seen[idem_key] = self.mutating_keys_seen.get(idem_key, 0) + 1
        if self._rng.random() < self._rate_429:
            raise RuntimeError("HTTP_429_RATE_LIMITED: Retry-After=2")
        return await self._router(tool_name, args)

async def evaluate_suite_pass_power_k(
    suite: Sequence[ScenarioSpec],
    run_episode_fn: Callable,
    n_trials: int = 5,
    k: int = 5,
) -> Dict[str, object]:
    if n_trials < k:
        raise ValueError("n_trials doit être supérieur ou égal à k")
    crit_scores, all_scores, policy_violations = [], [], 0

    for scenario in suite:
        successes = 0
        for trial in range(n_trials):
            world_db = copy_deep_snapshot(scenario.initial_db_snapshot)
            chaos_proxy = McpChaosProxy(real_router=bind_db_tools(world_db), seed=1000 + trial)

            report = await run_episode_fn(
                goal=scenario.user_goal_prompt,
                persona_variant=trial,
                mcp_gateway=chaos_proxy,
                max_turns=12,
            )

            db_matches = (world_db == scenario.expected_final_db_state)
            safe_exec = (report.cedar_denials == 0 and not report.uncompensated_side_effects)
            if not safe_exec:
                policy_violations += 1
            if db_matches and safe_exec:
                successes += 1

        score_k = math.comb(successes, k) / math.comb(n_trials, k)
        all_scores.append(score_k)
        if scenario.critical:
            crit_scores.append(score_k)

    mean_crit = sum(crit_scores) / max(len(crit_scores), 1)
    mean_global = sum(all_scores) / max(len(all_scores), 1)
    return {
        "pass_power_k_critical": round(mean_crit, 4),
        "pass_power_k_global": round(mean_global, 4),
        "policy_violations": policy_violations,
        "gate_passed": (mean_crit >= 0.95 and mean_global >= 0.88 and policy_violations == 0),
    }
```

Une violation de politique Cedar ou un effet de bord non compensé (`policy_violations > 0`) bloque la promotion du manifeste candidat, quel que soit le score moyen.

La section 34.6 renvoie à la compensation les effets externes déjà produits, mais certaines actions ne se compensent pas. Une réservation de stock interne se libère par une transaction inverse; un courriel juridique déjà expédié à un client externe ou un télégramme EDI transmis à un douanier ne se retire pas si la dernière étape de la saga échoue dix secondes plus tard. Quand le proxy provoque une panne tardive à l’étape finale d’une saga multi-divisions, le harnais vérifie que les connecteurs externes irréversibles appliquent le patron de boîte d’envoi différée : l’outil MCP enregistre l’intention d’envoi en tampon et n’émet physiquement la communication vers l’extérieur qu’après validation complète de la saga par l’orchestrateur durable (ou expiration d’une fenêtre de rétractation HOTL de quatre-vingt-dix secondes).

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur financier (BSIF E-23 au 1er mai 2027) : industrialiser la validation indépendante des modèles**
:::

Sous la ligne directrice BSIF E-23, la deuxième ligne de défense (gestion indépendante du risque de modèle) ne peut plus mettre six semaines à valider manuellement des agents mis à jour deux fois par mois.

Le couple SemVer + Intent et OpenEnv permet une homologation continue gouvernée :

1.  L’équipe indépendante des risques maintient son propre référentiel scellé de scénarios $\tau$-bench et de chaos, inaccessible en écriture aux équipes de développement pour exclure tout sur-ajustement aux tests.
2.  Toute révision mineure qui reste dans l’enveloppe architecturale approuvée (Cedar intact, même niveau d’autonomie) et franchit 100 % des barrières $\text{pass}^5$ et de survie au chaos sur ce banc scellé reçoit en vingt minutes un certificat d’homologation numérique, archivé avec le manifeste. Les comités humains sont réservés aux changements majeurs.
::::

------------------------------------------------------------------------

## 34.11 Déploiement progressif : mode fantôme et canari épinglé par saga

La section 34.2 décrit le déploiement par paliers et la probation. Une version SemVer + Intent validée en simulation traverse en production deux étapes, orchestrées par agentgateway et Temporal :

1.  **Mode fantôme sans effet de bord** : la passerelle duplique en asynchrone 10 à 20 % du trafic réel vers la version candidate. Tous les outils MCP de lecture interrogent les données réelles; tous les outils MCP mutatifs sont interceptés par un bouchon sans écriture. Un comparateur mesure pendant 24 heures la concordance des décisions, la latence et l’écart de coût par rapport à la version active, avant d’exposer le moindre client.
2.  **Canari épinglé par saga** : la version d’un agent ne change jamais au milieu d’une conversation ou d’une saga multi-tours en cours. Le routeur oriente 5 % des nouvelles sagas vers le candidat et épingle cette version dans l’état durable de la saga jusqu’à sa clôture. Si un SLO OpenTelemetry dérive, le contrôleur rebascule en moins de 30 secondes 100 % des nouvelles sagas sur la version stable (retour arrière de version, section 34.6).

#### Extrait 34.3 — Politique déclarative de déploiement *Canary* et de retour en arrière automatique (*rollback*)

La politique déclare le miroir de trafic du mode fantôme, les paliers du canari, l’épinglage par `saga.id` et les conditions de retour arrière automatique, évaluées toutes les 30 secondes.

``` yaml
apiVersion: agentops.boreal.ca/v1
kind: ProgressiveRolloutPolicy
metadata:
  targetAgent: boreal-bca-warranty-adjudicator
  candidateVersion: "2.4.0+intent.9f3a81c"
  baselineVersion: "2.3.4+intent.41b02e8"
spec:
  routingStrategy:
    stickinessKey: "saga.id"                  # Épinglage strict de version sur toute la vie de la saga
    shadowStage:
      enabled: true
      trafficMirrorPercent: 15
      duration: 24h
      mutatingMcpMode: "dry-run-intercept"
      minDecisionConcordance: 0.98
    canarySteps:
      - weightPercent: 5
        bakeDuration: 2h
        minCompletedSagas: 80
      - weightPercent: 25
        bakeDuration: 6h
        minCompletedSagas: 400
      - weightPercent: 100
        bakeDuration: 0h
  automatedRollbackTriggers:
    evaluationInterval: 30s
    conditions:
      - metric: "otel.gen_ai.livelock_abort_rate"
        operator: ">"
        threshold: 0.002                      # > 0,2 % de boucles sémantiques -> Rollback immédiat
      - metric: "otel.cedar.policy_denial_rate_delta"
        operator: ">"
        threshold: 0.005                      # Hausse > +0,5 pt de rejets Cedar
      - metric: "otel.hotl.escalation_rate_relative_increase"
        operator: ">"
        threshold: 0.35                       # Hausse relative > +35 % d'escalades HOTL
      - metric: "finops.p95_cost_per_saga_cad"
        operator: ">"
        threshold: 0.55
  postIncidentAutomation:
    exportFailedTracesToOpenEnvQueue: true    # Boucle fermée : trace d'échec -> futur test tau-bench
```

La directive finale referme la boucle avec le chapitre 33 : chaque désaveu HOTL ou retour arrière du canari extrait automatiquement la trace anonymisée pour enrichir la suite permanente $\tau$-bench.

------------------------------------------------------------------------

## 34.12 Application au fil rouge : le filet à 1 200 scénarios du Groupe Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : le critère pass\^5 a bloqué une régression invisible au pass@1**
:::

**Dispositif en place (mars 2027)** : Le Centre d’Excellence Agentique exploite un environnement OpenEnv de 1 200 scénarios multi-tours, issus des dossiers historiques et de traces anonymisées : 450 scénarios garantie/crédit-bail BCA (dont 120 critiques BSIF E-23), 400 scénarios logistiques BEL et 350 scénarios télématiques BSN. Chaque candidature exécute 6 000 conversations simulées ($k=5$) en 14 minutes, pour un coût de 38 \$ CAD, grâce à des profils simulés animés par des SLM calibrés.

**Interception critique en pré-production (semaine 11 de 2027)** : Une équipe soumet la révision `2.5.0+intent.c092d1b` de l’*Agent Garantie BCA*, qui adopte une nouvelle révision de modèle 25 % moins coûteuse. Au premier essai ($\text{pass}@1$), le score global semble progresser à 93,8 % (contre 93,1 % en production).

Le pipeline ADLC bloque pourtant la promotion à l’étape chaos et $\tau$-bench :

- Sur le segment critique des « Compresseurs opérés hors plage thermique avec avenant nordique », la constance $\text{pass}^5$ tombe de 96,4 % à 68,2 % dès que le proxy de chaos injecte 6 secondes de latence ou un HTTP 429 sur le serveur MCP télématique.
- L’analyse montre que le nouveau modèle, pour abréger sa chaîne d’actions face à un outil lent, présumait une fois sur douze que l’absence de relevé valait conformité et pré-autorisait indûment 4 200 \$ CAD sur des contrats exclus.

**Correction structurelle et bilan (T2 2027)** : En déplaçant la vérification de présence du relevé télématique hors du prompt vers une règle déterministe Cedar bloquante, la version `2.5.1+intent.f441a9e` remonte à $\text{pass}^5 = 98,1\,\%$ et à 100 % de survie au chaos, puis valide 24 heures de mode fantôme à 99,4 % de concordance. Cet incident de pré-production est archivé comme cas d’école interne : une métrique moyenne à essai unique masque les queues de distribution dangereuses. Sur le semestre, Groupe Boréal effectue 18 mises en production hebdomadaires avec 0 incident P1 et obtient le quitus d’audit BSIF E-23 trois semaines avant l’échéance légale du 1er mai 2027.
::::

------------------------------------------------------------------------

## 34.13 Décision d’architecture normative et points de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-022 — Cycle ADLC gouverné par SemVer+Intent, portes de constance pass\^5 et déploiement Canary**
:::

- **Statut** : Acceptée \| Périmètre : Qualité ADLC & CI/CD (L2–L3) \| Révision : Semestrielle
- **Contexte** : Les modifications non coordonnées de prompts, de modèles ou de schémas MCP, et les tests superficiels à tour unique, exposent l’entreprise à des régressions silencieuses dans des dialogues multi-tours soumis aux aléas réseau et humains.
- **Options évaluées** :
  1.  *Édition des prompts à chaud hors pipeline CI/CD* : Aucune traçabilité; non conforme à BSIF E-23 et à ISO/IEC 42001. Rejetée.
  2.  *Tests unitaires classiques complétés par 50 questions statiques en $\text{pass}@1$* : Aveugle à l’inconstance stochastique, aux dérives multi-tours et aux pannes sous HTTP 429. Rejetée.
  3.  *Pipeline ADLC sur registre immuable SemVer+Intent, simulation d’état OpenEnv / $\tau$-bench en $\text{pass}^5$, chaos protocolaire et déploiement en mode fantôme puis canari* : Concilie vélocité hebdomadaire et sûreté démontrable. Retenue.
- **Décision** : Toute livraison L2–L3 requiert un manifeste signé SemVer + Intent, qui fige modèles, prompts, Agent Skills, contrats MCP et politiques Cedar. La promotion exige $\text{pass}^5 \ge 0,95$ sur le corpus critique, 100 % de survie au chaos, un mode fantôme sans mutation pour tout changement de modèle et un canari épinglé par `saga.id` avec retour arrière automatisé.
- **Conséquences** :
  - *Positives* : Suppression des régressions furtives de modèles, capitalisation d’un patrimoine de tests métiers reproductibles, homologation réglementaire fluide.
  - *Négatives / coûts assumés* : Budget de calcul des simulations multi-tours en CI et maintenance des bouchons d’état OpenEnv.
- **Condition de révision** : Révision semestrielle des seuils $\text{pass}^k$ selon la criticité métier.
::::

### Liste de contrôle de mise en production

1.  **Épinglage SemVer + Intent complet** : Le manifeste fige-t-il l’identifiant daté du modèle (zéro alias `latest`), les condensats SHA-256 des prompts et des Agent Skills, les schémas MCP et le paquet Cedar ?
2.  **Assertion sur l’état final** : La suite OpenEnv / $\tau$-bench valide-t-elle l’état exact des tables simulées plutôt que la seule apparence textuelle de la réponse ?
3.  **Barrière bloquante $\text{pass}^5$** : Chaque scénario critique réussit-il de façon constante sur cinq trajectoires stochastiques distinctes ($\text{pass}^5 \ge 0,95$) ?
4.  **Profils à double contrôle et contradictoires** : La simulation éprouve-t-elle les revirements d’intention et les actions concurrentes de l’utilisateur ($\tau^2$-bench) ?
5.  **Résilience au chaos protocolaire et sécuritaire** : L’agent maintient-il l’idempotence, la compensation de la saga et le refus d’inventer sous HTTP 429/503, latence extrême et injections indirectes ?
6.  **Étanchéité du mode fantôme** : En mode fantôme sur trafic réel, 100 % des appels MCP mutatifs sont-ils bloqués par un intercepteur sans écriture en production ?
7.  **Affinité de version par saga en canari** : Une saga démarrée sur une révision conserve-t-elle cette même révision jusqu’à sa clôture ?
8.  **Conversion automatique d’incident en test** : Chaque retour arrière du canari ou désaveu HOTL alimente-t-il systématiquement le corpus permanent de non-régression ?
