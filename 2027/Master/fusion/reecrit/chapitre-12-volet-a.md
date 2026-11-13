## Mise en œuvre — Couches sémantiques normalisées et ontologies d'entreprise {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Un protocole normalisé (MCP, A2A v1.0) garantit que deux agents échangent des messages valides, non qu’ils désignent la même réalité métier. Un agent qui interroge directement des tables physiques, ou qui traverse trois divisions définissant chacune autrement un « client actif », une « garantie valide » ou un « stock disponible », automatise à haute cadence des contresens comptables, commerciaux et réglementaires.
- **Décisions architecturales structurantes** :
  1.  *Irréversible à moyen terme* : interdire à tout agent de production d’émettre du SQL libre contre des schémas physiques; imposer le passage exclusif par une couche sémantique déclarative neutre, décrite dans le format d’échange Apache Ossie (section 12.4), projet en incubation dont la seule version parue est la `0.1.1`, et versionnée sous Git.
  2.  *Structurante dès le jour 1* : coupler cette couche de lecture à une ontologie opérationnelle causale, qui formalise les identifiants maîtres inter-systèmes (MDM), les automates d’états légaux et les contrats de préconditions et d’effets des actions mutatives.
  3.  *Réversible par conception* : les moteurs d’exécution vers lesquels l’architecture vise à compiler le manifeste (Snowflake Semantic Views, dbt Semantic Layer, Cube, moteurs d’intelligence d’affaires, serveurs MCP) et le substrat de stockage du graphe ontologique.
- **Indicateurs de gouvernance associés** : taux de couverture des concepts partagés par des manifestes Apache Ossie, taux de rejet transactionnel aval pour violation d’invariant métier (cible \< 0,5 %), écart nul entre les chiffres que l’intelligence d’affaires présente aux comités exécutifs et ceux que consomment les agents, délai de propagation d’une règle d’affaires modifiée.
::::

## 12.8 Les limites du SQL libre sur un patrimoine d’entreprise

Un banc d’essai de 2023 (section 12.1) a mesuré, sur un schéma d’assurance, 16 % de bonnes réponses en SQL direct, contre 54 % sur une représentation en graphe de connaissances. Ces chiffres viennent du résumé de l’article et portent sur un modèle dépassé; 54 % n’est pas un résultat de production. Dans un grand compte qui porte quarante ans d’héritage applicatif, le schéma physique compte 14 000 tables. Elles se répartissent entre des modules SAP S/4HANA (VBAK, MARD, ACDOCA), des fichiers physiques hérités d’IBM i (AS/400) aux mnémoniques de six caractères (CSTSTS, WRTYCD, BAL90D) et des centaines d’objets personnalisés ajoutés dans Salesforce au fil des fusions-acquisitions (`Account_Tier_Legacy_2021__c`).

Un agent qui improvise ses jointures et ses formules d’agrégation sur un tel patrimoine échoue pour quatre causes structurelles.

1.  **Les exclusions métier implicites.** Une table transactionnelle mêle ventes réelles, écritures techniques de contre-passation, commandes internes d’essai et lignes annulées logiquement (`STAT_CD NOT IN ('90', '99')`). Aucune clé étrangère ne documente ces filtres. L’agent qui les omet fausse les agrégats de 8 à 25 %.
2.  **Les pièges d’agrégation à la jointure.** Joindre dans une même requête `SELECT SUM(contract_value)` une table de contrats (1), une table d’équipements (N) et une table d’avenants (M) multiplie silencieusement la valeur du contrat par le produit du nombre d’équipements et du nombre d’avenants. Le moteur s’exécute sans erreur et l’agent défend ce résultat faux.
3.  **La polysémie organisationnelle.** Deux divisions emploient le même terme pour des concepts distincts. Pour l’équipe SaaS, un « client actif » s’est connecté dans les trente derniers jours; pour la finance, c’est un cocontractant sans facture échue depuis plus de soixante jours; pour le support, c’est un parc sous contrat d’assistance ouvert. Sans désambiguïsation formelle, un orchestrateur mélange ces acceptions à chaque délégation A2A.
4.  **L’asymétrie entre observer et muter.** Un agrégat analytique ne suffit jamais à légitimer une action. Lire trois turbines en stock comptable n’indique pas si l’agent a le droit contractuel d’allouer la dernière pièce du stock tampon réservé à un client sous pénalité SLA.

La probabilité d’exactitude d’une décision qui croise $k$ concepts métier s’écrit :

$$P(\text{Exact}) = P(\text{Syntaxe}) \cdot \prod_{j=1}^{k} P(\text{Sens}_j \mid \mathcal{O})$$

Les protocoles de la partie II (MCP, schémas JSON stricts, A2A v1.0) portent $P(\text{Syntaxe})$ au-delà de $0{,}999$. Sans référentiel sémantique partagé $\mathcal{O}$, si chaque concept a une probabilité d’interprétation exacte de $0{,}80$, croiser quatre concepts (client, garantie, stock, priorité SLA) abaisse la fiabilité globale à $0{,}80^4 \approx 0{,}41$, soit près de trois décisions erronées sur cinq.

| Approche d’accès au sens métier | Exactitude analytique chiffrée | Maîtrise des actions mutatives | Portabilité (intelligence d’affaires et agents) | Risque majeur en exploitation |
|:----------------------|:-----------------|:------------------|:----------------|:-------------------------|
| SQL libre sur tables brutes | Faible (16 % de bonnes réponses sur un banc d’essai de 2023, modèle dépassé; section 12.1) | Nulle (aucun automate d’état) | Nulle (couplé au SGBD) | Pièges d’agrégation, oubli des annulations, chiffres inventés |
| Consignes locales par agent (documentation ad hoc) | Moyenne mais divergente | Fragile (prose non vérifiée) | Nulle (enfermé par agent) | Écarts chroniques entre les calculs des agents et les rapports |
| *GraphRAG* documentaire pur (extraction par modèle de langage) | Faible sur agrégats numériques | Incomplète (graphe non typé) | Modérée | Triplets bruyants extraits sans contrôle d’invariants |
| Couplage Apache Ossie et ontologie causale | Déterministe (\> 99 % compilé) | Forte (préconditions formelles) | Maximale (format d’échange en incubation à l’ASF; section 12.4) | Effort initial de gouvernance inter-divisions |

------------------------------------------------------------------------

## 12.9 Apache Ossie comme source unique de la couche analytique

Jusqu’en 2025, les métriques d’une entreprise vivaient en plusieurs exemplaires dans les formats captifs des outils de visualisation (Tableau, Power BI, Looker, Omni), de transformation (dbt), de cubes (Cube) et d’entrepôts (Snowflake, Databricks). Toute évolution d’une règle de marge ou de disponibilité imposait quatre réécritures manuelles, et aucun serveur MCP n’en bénéficiait directement. Le projet et son historique sont décrits à la section 12.4.

### Un manifeste compilé, non un serveur

Apache Ossie n’ajoute aucun composant propriétaire sur le chemin critique des requêtes. Le manifeste YAML est versionné dans un dépôt Git unique, que gouvernent les propriétaires de produits de données. Le dépôt d’Ossie fournit des convertisseurs de référence vers dbt, GoodData, Polaris et Salesforce; la spécification ne décrit aucune interface d’interrogation, et l’exposition aux agents passe par des serveurs MCP propres à chaque éditeur (sections 12.4 et 12.5). L’architecture visée est plus large : un pipeline CI/CD compile le manifeste simultanément vers trois familles de cibles :

- les vues sémantiques natives des entrepôts (Snowflake Semantic Views, Databricks Unity Catalog Metric Views);
- les moteurs analytiques et d’intelligence d’affaires (dbt, Cube, tableaux de bord exécutifs);
- les serveurs MCP analytiques de la fabrique agentique, qui exposent chaque indicateur certifié comme un outil paramétré, sans SQL libre.

Le directeur financier qui consulte son rapport mensuel et l’agent L3 qui statue à 3 h du matin sur une prise en charge urgente exécutent le même arbre relationnel, compilé depuis le même fichier.

### Usage des cinq constructions

Les constructions sont celles de la section 12.2. L’architecture leur assigne les rôles suivants.

1.  **`datasets`.** Chaque entité logique, fait ou dimension nettoyée, est reliée à sa table ou vue source et déclare ses clés primaires (`primary_key`).
2.  **`fields`.** Ils déclarent les dimensions et attributs exposés, avec types stricts, expressions SQL normalisées et marqueurs temporels (`dimension.is_time`). Les colonnes techniques internes restent masquées.
3.  **`metrics`.** Elles figent les formules quantitatives officielles (SUM, COUNT DISTINCT, ratios conditionnels). L’agent invoque `net_allocatable_atp_qty`; il n’invente jamais sa propre soustraction des stocks bloqués.
4.  **`relationships`.** Elles définissent le graphe orienté des jointures légales (`from_columns`, `to_columns`) et leur cardinalité, ce qui interdit le piège d’agrégation dans les requêtes multi-tables.
5.  **`ai_context`.** Présent à la racine comme sur chaque champ, métrique ou relation, il porte les instructions d’interprétation, les synonymes de chaque division et les exclusions explicites qui préviennent les confusions.

### Cycle de vie du manifeste et compatibilité ascendante

Un manifeste partagé par vingt-cinq agents autonomes se gouverne avec la rigueur contractuelle d’une interface publique d’API. Modifier en silence le sens d’un booléen critique, par exemple abaisser de soixante à trente jours le seuil d’arriéré toléré de `is_active_commercial_customer` sans incrémenter la version majeure du modèle, change du jour au lendemain le comportement décisionnel de tous les agents consommateurs. C’est un changement matériel au sens de la ligne directrice BSIF E-23.

Un pipeline de validation continue applique donc trois garde-fous automatisés à chaque demande de fusion Git.

- **Intégrité référentielle et acyclicité.** Le validateur inspecte les expressions SQL, confirme que les colonnes existent dans le catalogue de l’entrepôt cible et rejette tout cycle ambigu de jointures dans le bloc `relationships`.
- **Détection des ruptures de contrat.** Renommer une métrique, modifier le type de retour d’un champ ou changer la logique d’un prédicat sans mise à jour de version sémantique (SemVer) bloque le déploiement tant que les propriétaires des Agent Cards abonnées n’ont pas contresigné l’impact.
- **Tests d’assertion de référence.** Des requêtes témoins s’exécutent sur un jeu de données figé. Chaque cible de compilation (Snowflake, dbt et Cube, serveur MCP) doit restituer les mêmes valeurs décimales à $10^{-6}$ près.

L’Extrait 12.1 ci-dessous porte `version: "1.0.0"`, alors qu’aucune version 1.0 d’Apache Ossie n’existe : la seule version parue est la `0.1.1`, et la branche `0.3.0.dev0` se déclare impropre à la production (section 12.4). Il arrête aussi une définition unique du « client actif »; or, quand deux domaines définissent un terme différemment, la section 12.7 recommande de nommer deux métriques distinctes, de documenter l’écart et de retirer le terme nu du catalogue exposé aux agents.

#### Extrait 12.1 — Manifeste sémantique complet Apache Ossie (boreal_core_operations.ossie.yaml)

Ce manifeste unifie chez Groupe Boréal la définition d’un client commercial actif, d’une garantie valide et du stock net allouable à la promesse (ATP) :

``` yaml
version: "1.0.0"
name: boreal_core_operations_semantic_model
description: "Modèle sémantique canonique inter-divisions du Groupe Boréal (BSN, BCA, BEL)."

ai_context:
  instructions: >
    Source unique de vérité analytique pour qualifier un client, vérifier l'admissibilité d'une garantie
    équipement et calculer la disponibilité nette de pièces (ATP). Ne jamais assimiler un compte d'essai
    télématique gratuit BSN à un client actif. Ne jamais promettre une pièce sur la base du stock physique
    brut SAP (labst_raw) : interroger exclusivement la métrique net_allocatable_atp_qty.
  synonyms: ["référentiel parc installé Boréal", "vérité client garantie stock"]

datasets:
  - name: enterprise_customer
    description: "Entité cliente maître réconciliée (MDM) entre Salesforce BSN, IBM i BCA et SAP BEL."
    source: boreal_gold.mdm.dim_enterprise_customer
    primary_key: [boreal_party_id]
    fields:
      - name: boreal_party_id
        datatype: String
        expression: { sql: boreal_party_id }
      - name: legal_entity_name
        datatype: String
        expression: { sql: legal_entity_name }
      - name: overdue_balance_over_60d_cad
        datatype: Decimal
        expression: { sql: ar_overdue_60d_amount_cad }
      - name: is_active_commercial_customer
        datatype: Boolean
        expression:
          sql: >
            (commercial_lifecycle_stage = 'SIGNED_CONTRACT_ACTIVE'
             AND is_free_telemetry_trial = FALSE
             AND COALESCE(ar_overdue_60d_amount_cad, 0) = 0
             AND legal_hold_flag = FALSE)
        ai_context:
          instructions: >
            Définition normative Groupe Boréal d'un « client actif ». Exclut les essais SaaS gratuits 90 jours,
            les dossiers en gel contentieux et tout arriéré comptable dépassant 60 jours.
          synonyms: ["client actif", "compte commercial en règle"]

  - name: equipment_warranty_contract
    description: "Contrats de garantie bris de machine synchronisés depuis BCA (IBM i / Guidewire)."
    source: boreal_gold.bca.fct_warranty_coverages
    primary_key: [warranty_contract_id, equipment_serial_number]
    fields:
      - name: warranty_contract_id
        datatype: String
        expression: { sql: warranty_contract_id }
      - name: boreal_party_id
        datatype: String
        expression: { sql: holder_boreal_party_id }
      - name: equipment_serial_number
        datatype: String
        expression: { sql: equipment_serial_number }
      - name: is_warranty_coverage_valid
        datatype: Boolean
        expression:
          sql: >
            (policy_status = 'IN_FORCE'
             AND CURRENT_DATE() BETWEEN effective_start_date AND effective_end_date
             AND telemetry_verified_hours <= contractual_hour_ceiling
             AND lease_delinquency_30d_flag = FALSE)
        ai_context:
          instructions: >
            Vrai uniquement si la police est en vigueur, le plafond d'heures moteur mesuré par télémétrie BSN
            est respecté et le contrat de crédit-bail BCA ne présente aucun impayé > 30 jours.
          synonyms: ["garantie valide", "couverture bris active"]
    metrics:
      - name: active_covered_units_count
        description: "Nombre d'équipements couverts par une garantie valide."
        datatype: Integer
        expression:
          sql: COUNT(DISTINCT CASE WHEN is_warranty_coverage_valid THEN equipment_serial_number END)

  - name: spare_part_plant_inventory
    description: "Position temps réel (CDC Kafka < 30s) des stocks de pièces dans SAP S/4HANA (BEL)."
    source: boreal_gold.bel.fct_sap_spare_inventory_rt
    primary_key: [material_code, plant_depot_code]
    fields:
      - name: material_code
        datatype: String
        expression: { sql: matnr_canonical }
      - name: plant_depot_code
        datatype: String
        expression: { sql: werks_depot_code }
      - name: safety_floor_qty
        datatype: Integer
        expression: { sql: contractual_safety_buffer_qty }
    metrics:
      - name: net_allocatable_atp_qty
        description: "Stock net disponible à la promesse (ATP) hors réservations fermes et tampon SLA."
        datatype: Integer
        expression:
          sql: >
            SUM(GREATEST(0,
              sap_labst_qty - committed_open_reservations_qty - contractual_safety_buffer_qty
            ))
        ai_context:
          instructions: >
            Seule métrique autorisée pour allouer automatiquement une pièce. Retranche du stock libre SAP
            (sap_labst_qty, déjà hors quarantaine qualité) les réservations ouvertes et le tampon contractuel.
          synonyms: ["stock disponible", "disponibilité nette ATP", "pièces allouables"]

relationships:
  - name: warranty_to_enterprise_customer
    description: "Relie chaque contrat de garantie d'équipement à l'entité juridique cliente maître."
    from: equipment_warranty_contract
    to: enterprise_customer
    cardinality: many_to_one
    from_columns: [boreal_party_id]
    to_columns: [boreal_party_id]
    ai_context:
      synonyms: ["titulaire de la garantie", "locataire assuré"]
```

------------------------------------------------------------------------

## 12.10 De la lecture analytique à l’action sûre : l’ontologie opérationnelle causale

Un manifeste Apache Ossie fixe la vérité descriptive : humains et logiciels s’accordent sur ce qui est. Or l’entreprise agentique ne se borne pas à lire des agrégats; ses agents modifient l’état des systèmes transactionnels. Une couche analytique ne modélise ni la légalité des transitions d’état, ni la causalité opérationnelle. Lire `net_allocatable_atp_qty = 2` à Montréal-Est ne dit pas à l’orchestrateur :

1.  si l’ordre de travail courant se trouve à l’état `DIAGNOSIS_QUALIFIED`, qui autorise le passage vers `WARRANTY_AND_PARTS_COMMITTED`;
2.  quelles préconditions inter-divisions doivent être réunies simultanément (client commercial actif au sens d’Ossie, compatibilité de nomenclature BOM certifiée, plafond financier d’autonomie L3 respecté);
3.  dans quel cas exceptionnel une règle métier autorise à puiser dans le tampon `safety_floor_qty`;
4.  quel outil MCP inverse appeler en compensation si l’affectation terrain échoue ensuite.

L’ontologie opérationnelle causale répond à ces questions. Elle est le second pilier de l’architecture duale que représente la figure suivante : Apache Ossie gouverne les noms et les métriques, l’ontologie causale gouverne les états, les invariants et les actions. Ce second pilier, que la décision (c) de l’ADR-009 exige pour tout outil MCP mutatif L2+, va au-delà de ce que retient la section 12.3, qui ne prescrit aucune ontologie au départ et la réserve aux domaines bornés à fort enjeu ou aux secteurs dotés d’une ontologie de référence. Il s’appuie sur le registre de l’Extrait 12.2, non sur la spécification d’ontologie d’Ossie, jeune et sans moteur d’inférence défini (section 12.4).

![Architecture duale couplant la couche sémantique analytique Apache Ossie et l’ontologie opérationnelle causale au sein d’un pipeline neuro-symbolique.](figures/fig-12-a-1.svg)

| Concept canonique | Ambiguïtés historiques des silos | Vérité analytique (Apache Ossie) | Règle causale et d’action (ontologie opérationnelle) |
|:---------------------|:-------------------------|:-------------------------|:----------------------------|
| Client (`EnterpriseCustomer`) | Essai gratuit SaaS (BSN), locataire à bail (BCA), acheteur de pièces (BEL) | Booléen certifié `is_active_commercial_customer` sur clé `boreal_party_id` | Invariant : toute mutation L3 sans pré-paiement exige `is_active_commercial_customer == true` |
| Garantie (`WarrantyCoverage`) | Police active aux dates calendaires, mais plafond d’heures moteur dépassé | Booléen `is_warranty_coverage_valid` croisant dates, loyers et heures IoT | Action `PreauthorizeClaim` : autorisée depuis `IN_FORCE`; escalade HOTL si coût \> 5 000 \$ CAD |
| Stock (`SpareInventory`) | Colonne brute LABST mêlant stock libre et tampon d’urgence `SLA 99,5 %` | Métrique `net_allocatable_atp_qty` isolant le tampon contractuel | Action `AllocateWarrantyReplacementPart` : accès à `safety_floor_qty` réservé au rang `PLATINUM_995` |

#### Extrait 12.2 — Contrat d’action cinétique et vérificateur déterministe de préconditions (TypeScript)

Ces garde-fous s’exécutent dans un registre ontologique typé avant tout appel MCP, non dans une consigne en prose que le modèle peut oublier :

``` typescript
export type WorkOrderState =
  | "TRIAGE_PENDING" | "DIAGNOSIS_QUALIFIED" | "WARRANTY_AND_PARTS_COMMITTED" | "DISPATCHED" | "CLOSED";

export interface DomainSnapshot {
  readonly partyId: string;
  readonly isActiveCommercialCustomer: boolean; // Issu d'Apache Ossie
  readonly slaTier: "STANDARD" | "GOLD_990" | "PLATINUM_995";
  readonly isWarrantyValid: boolean;            // Issu d'Apache Ossie
  readonly estimatedRepairCostCad: number;
  readonly currentWorkOrderState: WorkOrderState;
  readonly netAllocatableAtpQty: number;        // Issu d'Apache Ossie
  readonly safetyFloorQty: number;
}

export type PreconditionVerdict =
  | { readonly status: "EXECUTABLE"; readonly nextState: WorkOrderState }
  | { readonly status: "REQUIRES_HOTL"; readonly reasonCode: string; readonly queue: string }
  | { readonly status: "ILLEGAL_ACTION"; readonly violatedInvariant: string };

export const AllocateWarrantyReplacementPart = {
  actionId: "boreal.ontology.action.AllocateWarrantyReplacementPart",
  mcpTool: "sap_reserve_critical_spare_part",
  compensationMcpTool: "sap_release_spare_part_reservation",
  allowedFrom: ["DIAGNOSIS_QUALIFIED"] as ReadonlyArray<WorkOrderState>,
  targetState: "WARRANTY_AND_PARTS_COMMITTED" as WorkOrderState,

  verify(snap: DomainSnapshot, reqQty: number, allowSafetyTap: boolean): PreconditionVerdict {
    if (!Number.isInteger(reqQty) || reqQty <= 0) {
      return { status: "ILLEGAL_ACTION", violatedInvariant: `Quantité demandée invalide (${reqQty}).` };
    }
    if (!AllocateWarrantyReplacementPart.allowedFrom.includes(snap.currentWorkOrderState)) {
      return { status: "ILLEGAL_ACTION", violatedInvariant: `État illégal : ${snap.currentWorkOrderState}.` };
    }
    if (!snap.isActiveCommercialCustomer) {
      return { status: "ILLEGAL_ACTION", violatedInvariant: `Tiers ${snap.partyId} inactif au sens Ossie.` };
    }
    if (snap.netAllocatableAtpQty < reqQty) {
      const canTapBuffer = allowSafetyTap && snap.slaTier === "PLATINUM_995" &&
        (snap.netAllocatableAtpQty + snap.safetyFloorQty >= reqQty);
      if (!canTapBuffer) {
        return { status: "ILLEGAL_ACTION", violatedInvariant: `Stock ATP insuffisant (${snap.netAllocatableAtpQty}).` };
      }
    }
    if (!snap.isWarrantyValid) {
      return { status: "REQUIRES_HOTL", reasonCode: "OUT_OF_WARRANTY_QUOTE_NEEDED", queue: "bsn-commercial-hotl" };
    }
    if (snap.estimatedRepairCostCad > 5000) {
      return { status: "REQUIRES_HOTL", reasonCode: "EXCEEDS_L3_CEILING_5000_CAD", queue: "bca-underwriting-hotl" };
    }
    return { status: "EXECUTABLE", nextState: AllocateWarrantyReplacementPart.targetState };
  }
};
```

Le modèle garde sa souplesse linguistique pour qualifier un symptôme complexe, mais il ne peut enfreindre ni une transition d’état, ni un seuil actuariel, ni le tampon protégé, puisque le vérificateur s’exécute avant l’appel. Sous forte concurrence, ce pré-contrôle, fondé sur une vue analytique rafraîchie par CDC en moins de trente secondes, reste doublé d’une garde atomique Compare-And-Set dans le serveur MCP transactionnel. Elle arbitre sans sur-allocation deux sagas parallèles qui visent la dernière pièce disponible (`ATP = 1`).

------------------------------------------------------------------------

## 12.11 Résolution neuro-symbolique avant la planification

Une alerte textuelle imprécise (« Usine Boisbriand – Compresseur ligne 3 en surchauffe ») doit être reliée aux clés canoniques `boreal_party_id` et `matnr_canonical`. Un pipeline de résolution neuro-symbolique, ancré dans l’ontologie, s’en charge avant la planification.

Le *GraphRAG* documentaire de 2024 demandait à un modèle d’extraire des triplets approximatifs de documents PDF. Celui de 2027 projette les référentiels maîtres (MDM), les nomenclatures d’ingénierie (BOM) et les relations d’Apache Ossie dans un graphe typé et gouverné. Avant toute génération de plan par le modèle orchestrateur, le médiateur exécute quatre étapes déterministes en moins de 80 ms.

1.  **Résolution d’entités.** Un appariement lexical et vectoriel sur les alias de sites résout la mention brute vers l’URI unique `urn:boreal:asset:BOR-CMP-90441`. Si plusieurs actifs candidats subsistent, le médiateur suspend toute action mutative et exige une désambiguïsation explicite.
2.  **Expansion bornée à deux sauts.** Le médiateur traverse les relations certifiées (Actif → Pièces compatibles BOM → Dépôts régionaux rattachés; Actif → Contrat de garantie BCA).
3.  **Hydratation chiffrée.** Les métriques et attributs certifiés d’Apache Ossie sont exécutés, avec paramètres, sur les entités résolues.
4.  **Élagage de l’espace d’actions.** Les préconditions ontologiques sont évaluées pour ne transmettre au modèle planificateur qu’un dossier d’état certifié, accompagné des seules actions légalement exécutables ou admissibles à l’escalade HOTL.

Le résolveur de l’Extrait 12.3 interroge Ossie par un client `OssieClient.query`; la spécification ne décrit pourtant aucune interface d’interrogation, qui figure parmi les travaux futurs de la feuille de route, et l’exposition aux agents passe par des serveurs MCP propres à chaque éditeur (sections 12.4 et 12.5).

#### Extrait 12.3 — Résolveur neuro-symbolique pré-planification (NeuroSymbolicPlanningResolver en Python)

Le résolveur suivant prépare le dossier de planification :

``` python
from dataclasses import dataclass
from typing import Any, Protocol, Sequence

@dataclass(frozen=True)
class AssetNode:
    party_id: str; legal_name: str; sla_tier: str; serial: str
    valid_bom_parts: tuple[str, ...]; depots: tuple[str, ...]; wo_state: str

class OntologyGraph(Protocol):
    def resolve_asset(self, mention: str, device_hint: str | None) -> Sequence[AssetNode]: ...

class OssieClient(Protocol):
    def query(self, model: str, dims: Sequence[str], metrics: Sequence[str], filters: dict[str, Any]) -> list[dict]: ...

class NeuroSymbolicPlanningResolver:
    MODEL = "boreal_core_operations_semantic_model"

    def __init__(self, graph: OntologyGraph, ossie: OssieClient) -> None:
        self._graph, self._ossie = graph, ossie

    def prepare_planning_brief(
        self, site_mention: str, device_hint: str | None, part_code: str, est_cost_cad: float
    ) -> dict[str, Any]:
        matches = self._graph.resolve_asset(site_mention, device_hint)
        if len(matches) != 1:
            return {
                "status": "DISAMBIGUATION_REQUIRED",
                "candidates": [m.serial for m in matches],
                "admissible_actions": [],
            }

        asset = matches[0]
        if asset.wo_state != "DIAGNOSIS_QUALIFIED" or part_code not in asset.valid_bom_parts:
            reason = f"État {asset.wo_state} illégal." if asset.wo_state != "DIAGNOSIS_QUALIFIED" else f"Pièce {part_code} hors BOM."
            return {
                "status": "READY",
                "admissible_actions": [],
                "blocked": [{"action": "AllocateWarrantyReplacementPart", "reason": reason}],
            }

        cust = self._ossie.query(
            model=self.MODEL,
            dims=["enterprise_customer.is_active_commercial_customer",
                  "equipment_warranty_contract.is_warranty_coverage_valid"],
            metrics=[
                "equipment_warranty_contract.active_covered_units_count"
            ],
            filters={"enterprise_customer.boreal_party_id": asset.party_id,
                     "equipment_warranty_contract.equipment_serial_number": asset.serial},
        )
        inv = self._ossie.query(
            model=self.MODEL,
            dims=["spare_part_plant_inventory.plant_depot_code"],
            metrics=["spare_part_plant_inventory.net_allocatable_atp_qty"],
            filters={"spare_part_plant_inventory.material_code": part_code,
                     "spare_part_plant_inventory.plant_depot_code": list(asset.depots)},
        )

        c_fact = cust[0] if cust else {}
        active = bool(c_fact.get("is_active_commercial_customer", False))
        warranty = bool(c_fact.get("is_warranty_coverage_valid", False))
        atp = {r["plant_depot_code"]: int(r["net_allocatable_atp_qty"]) for r in inv}
        viable = [d for d, q in atp.items() if q >= 1]

        admissible, blocked = [], []
        if active and warranty and viable and est_cost_cad <= 5000.0:
            admissible.append({"action": "AllocateWarrantyReplacementPart", "mode": "L3_AUTO", "depot": viable[0]})
        elif active and viable:
            admissible.append({"action": "AllocateWarrantyReplacementPart", "mode": "HOTL_ESCALATION"})
        else:
            blocked.append({"action": "AllocateWarrantyReplacementPart", "reason": "Client inactif ou rupture ATP."})

        return {
            "status": "READY",
            "canonical_asset": {"party_id": asset.party_id, "serial": asset.serial, "wo_state": asset.wo_state},
            "ossie_facts": {"active_customer": active, "valid_warranty": warranty, "atp_by_depot": atp},
            "admissible_actions": admissible,
            "blocked": blocked,
        }
```

Le médiateur divise aussi par trois la consommation de jetons de raisonnement du modèle planificateur, qui n’a plus à tâtonner par des appels d’outils infructueux.

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Commerce omnicanal et distribution — Promesse de disponibilité (ATP), tarification unifiée et retours**
:::

Dans le commerce omnicanal et la distribution B2B, les agents d’achat externes et les agents internes d’après-vente exposent toute divergence sémantique entre canaux.

1.  **Stock comptable en magasin et promesse de disponibilité.** Un ERP affiche 4 articles en succursale, mais 2 sont dans des paniers physiques en rayon, 1 est un modèle d’exposition abîmé et 1 attend son ramassage *Click & Collect*. Sans une métrique Apache Ossie qui intègre une décote de surface de vente et les verrous de l’orchestrateur de commandes (OMS), l’agent promet un retrait express qui échoue en rupture client.
2.  **Non-cumul promotionnel.** L’ontologie causale doit encoder l’incompatibilité entre remises cadres B2B, démarques saisonnières et gestes de rétention avant toute émission d’offre ferme.
3.  **Remboursements sans retour physique.** Lorsque le transport retour excède la valeur résiduelle d’un article défectueux, l’ontologie autorise un crédit immédiat sans étiquette de retour, mais verrouille cette transition dès que le score de récurrence d’incidents du compte ou du transporteur dépasse le seuil antifraude.
::::

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Santé et sciences de la vie — Terminologies normatives (HL7 FHIR, SNOMED CT) et interdiction de l'approximation vectorielle**
:::

Dans les réseaux hospitaliers, l’assurance santé et la pharmacovigilance, l’alignement sémantique s’appuie sur des ontologies cliniques internationales : ressources HL7 FHIR R5, nomenclature SNOMED CT, analyses LOINC et référentiels médicamenteux RxNorm et Santé Canada. Une règle de sûreté médicale s’impose : aucun agent de coordination des soins ou de pré-autorisation ne doit résoudre un terme clinique par simple proximité cosinus entre vecteurs. Dans un espace vectoriel dense, « hyperkaliémie sévère » et « hypokaliémie sévère » affichent une similarité supérieure à $0{,}94$ tout en appelant des gestes opposés. Toute résolution passe par un serveur terminologique déterministe, qui valide les hiérarchies IS-A de SNOMED CT et les profils FHIR.
::::

------------------------------------------------------------------------

## 12.12 Application au fil rouge : l’alignement sémantique inter-divisions chez Groupe Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : réconcilier « client actif », « garantie valide » et « stock disponible » entre BSN, BCA et BEL**
:::

**L’alerte d’audit interne (février 2027).** En élargissant les flux inter-divisions à 1 100 dossiers sur trois semaines, l’audit interne de Groupe Boréal a constaté que 19,4 % des sagas subissaient soit un rejet transactionnel tardif dans SAP ou l’AS/400, soit une perte financière sèche. Trois ambiguïtés sémantiques en étaient la cause directe.

1.  **Le faux « client actif » (37 400 \$ CAD de pièces expédiées à perte).** Pour stimuler son adoption SaaS, Boréal Services Numériques (BSN) accordait 90 jours d’essai gratuit à des prospects industriels dont le compte Salesforce portait `Account.Status__c = 'Active'`. L’orchestrateur assimilait ce champ local à un contrat commercial en vigueur et engageait des réservations prioritaires pour des prospects non facturables.
2.  **La fausse « garantie valide » (litiges inter-filiales).** Sur l’IBM i (AS/400) de Boréal Capital & Assurances (BCA), une police restait au statut `IN_FORCE` jusqu’à son échéance annuelle, même lorsque le locataire avait dépassé de 1 200 heures son quota contractuel d’utilisation mesuré par la télémétrie BSN, ou accusait 45 jours d’impayé de crédit-bail. L’agent BCA, qui lisait la seule colonne POLSTS, accordait indûment la gratuité.
3.  **Le faux « stock disponible » (pénalités SLA chez Boréal Équipements & Logistique, BEL).** Un premier serveur MCP lisait directement la colonne physique `MARD.LABST` dans SAP S/4HANA. Par deux fois, un agent a alloué à un dépannage ordinaire la dernière turbine gardée en tampon contractuel de sécurité pour une aluminerie québécoise sous SLA 99,5 %.

**Remédiation du Bureau de Gouvernance Sémantique (mars–avril 2027).**

- **Dépôt fédéré `boreal-semantic-contracts` sous Apache Ossie** : un comité tripartite (propriétaire produit BSN, actuaire BCA, logistique BEL) a normalisé en trois semaines les 42 métriques et dimensions transversales du groupe (dont l’Extrait 12.1), compilées par CI/CD vers Snowflake et les serveurs MCP analytiques.
- **Médiation neuro-symbolique obligatoire (Extraits 12.2 et 12.3)** : résolution préalable vers `boreal_party_id` et blocage déterministe de toute ponction sur un tampon de sécurité hors SLA `PLATINUM_995`.

**Résultats vérifiés au trimestre suivant (T2 2027).**

- **Rejets transactionnels ou annulations aval** : abaissés de 19,4 % à 0,28 %.
- **Expéditions ou prises en charge hors contrat** : ramenées à 0 \$ CAD sur 18 500 dossiers consécutifs.
- **Concordance entre intelligence d’affaires et agents** : 100 % d’identité mathématique entre les tableaux de bord exécutifs du siège de Montréal et les métriques que lisent en temps réel les 24 agents spécialistes.
::::

------------------------------------------------------------------------

## 12.13 Décision d’architecture et points de contrôle

L’ADR-009 ci-dessous adopte Apache Ossie pour la production. Selon la section 12.4, aucune version 1.0 n’existe et la branche `0.3.0.dev0` se déclare impropre à la production; la grille de décision du chapitre recommande de ne rien bâtir en production sur cette version, de suivre Apache Ossie comme format d’échange et d’exiger l’import et l’export avec numéro de version.

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-009 — Adoption d'Apache Ossie pour la sémantique analytique et d'une ontologie causale versionnée pour les actions**
:::

- **Statut** : Acceptée \| Périmètre : données d’entreprise et fabrique agentique \| Révision : annuelle
- **Contexte** : L’interrogation directe des schémas physiques (SQL libre) et l’absence de définitions partagées entre divisions provoquent des erreurs d’agrégation, des interprétations contradictoires des concepts pivots (client, couverture, stock) et des mutations qui violent des invariants métier.
- **Options évaluées** :
  1.  *Exemples SQL dans les consignes des agents* : documenter les tables dans chaque consigne. Rejetée : duplication ingérable, dérive face aux évolutions de schéma et risque élevé de chiffres inventés.
  2.  *Couche sémantique captive d’un outil d’intelligence d’affaires unique* : forcer tous les agents à passer par l’API propriétaire d’un éditeur. Rejetée : verrouillage critique, coût prohibitif à haute cadence machine et absence de modélisation des mutations.
  3.  *Architecture duale ouverte : manifestes YAML Apache Ossie et ontologie opérationnelle causale* : standardiser les métriques, les relations et les instructions `ai_context` sous Apache Ossie, compilé vers l’entrepôt et les serveurs MCP, et lier chaque outil mutatif à un contrat formel d’état et de préconditions, évalué avant la planification. Retenue.
- **Décision** : (a) le SQL libre sur tables physiques est interdit en production pour tout agent L1–L4; (b) tout concept partagé entre deux applications ou divisions doit figurer au référentiel Git Apache Ossie; (c) tout outil MCP mutatif L2+ doit être adossé à une action ontologique qui déclare ses états sources légaux, ses préconditions vérifiables sur Ossie et sa compensation.
- **Conséquences** :
  - *Positives* : identité mathématique entre les rapports d’intelligence d’affaires et les agents, indépendance vis-à-vis des moteurs analytiques, quasi-disparition des rejets aval et auditabilité formelle (BSIF E-23).
  - *Négatives et coûts assumés* : gouvernance inter-divisions (intendance sémantique), maintien des clés maîtres MDM et modélisation explicite des automates d’états.
- **Condition de révision** : alignement annuel sur les versions publiées d’Apache Ossie (ASF) et de la Linux Foundation AAIF.
::::

### Liste de contrôle de mise en production

Le premier point et la décision (a) de l’ADR-009 vont au-delà de ce que retient la section 12.5 : elle borne le SQL libre (lecture seule, périmètre restreint, permissions de l’appelant) et l’admet en lecture seule pour l’exploration ponctuelle d’un analyste.

1.  **Interdiction du SQL libre.** Aucun agent de production ne détient-il un accès qui lui permette d’exécuter du SQL généré librement sur les tables physiques des ERP, des CRM ou des lacs bruts ?
2.  **Manifestes sous CI/CD.** Les concepts transversaux sont-ils définis en YAML Apache Ossie, validés par revue croisée métier et compilés automatiquement vers l’intelligence d’affaires et les serveurs MCP ?
3.  **Contenu des blocs `ai_context`.** Chaque entité, chaque métrique critique et chaque relation documente-t-elle ses règles de désambiguïsation, ses synonymes par division et ses exclusions ?
4.  **Pièges d’agrégation.** Toutes les agrégations multi-tables reposent-elles exclusivement sur les `relationships` certifiées du manifeste ?
5.  **Résolution MDM stricte.** Le médiateur de pré-planification résout-il les mentions locales en URI maîtres uniques, et exige-t-il une clarification dès qu’une ambiguïté subsiste ?
6.  **Préconditions déterministes.** Chaque outil MCP mutatif possède-t-il un automate d’états légaux et un vérificateur exécuté avant l’appel transactionnel ?
7.  **Routage typé vers HOTL.** Les dépassements de plafond ou les cas hors garantie produisent-ils un verdict structuré `REQUIRES_HOTL` vers la file compétente, plutôt qu’une improvisation du modèle ?
8.  **Tests de concordance.** Une suite automatisée vérifie-t-elle, à chaque déploiement, que les valeurs retournées aux agents égalent au centime près celles des rapports officiels ?
