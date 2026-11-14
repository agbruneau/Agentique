## Mise en œuvre — Conformité réglementaire internationale et canadienne, et droit B2B inter-agents {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : Trois changements convergent en 2027 et mettent fin à l’immunité réglementaire des prototypes d’IA : l’application progressive de l’EU AI Act (août 2026, puis décembre 2027), l’entrée en vigueur le 1er mai 2027 de la ligne directrice BSIF E-23 au Canada, conjuguée à la Loi 25 au Québec, et la formation autonome de contrats B2B entre agents logiciels. Traiter ces obligations par des comités documentaires manuels paralyse les livraisons et expose l’entreprise à des sanctions pécuniaires et à des engagements commerciaux involontaires.
- **Décisions architecturales structurantes** :
  1.  *Irréversible à moyen terme* : Déployer un système de management de l’IA (AIMS) unique, conforme à ISO/IEC 42001, comme dorsale centrale, puis projeter ses contrôles vers chaque juridiction (BSIF E-23, Loi 25, EU AI Act, NIST AI RMF).
  2.  *Structurante dès la conception* : Qualifier le niveau d’exigence légale selon l’empreinte de déploiement complète de la saga, vérifiée automatiquement en porte CI/CD.
  3.  *Structurante pour le commerce externe* : Subordonner tout agent négociateur B2B à un accord-cadre bilatéral préalable et à un mandat cryptographique borné (AP2) opposable aux tiers.
- **Indicateurs de gouvernance** : Couverture du registre AIMS (100 % des identités NHI actives), délai de génération d’un dossier d’audit opposable (cible : moins de 4 heures), couverture explicative de l’art. 12.1 de la Loi 25 (100 %) et zéro dépassement de plafond sur les mandats AP2.
::::

## 38.8 Système de management certifiable ISO/IEC 42001 et alignement NIST AI Agent Standards

Une charte déclarative et un tableur remplis une seule fois avant la mise en ligne ne suffisent pas pour une fabrique multi-agents de troisième génération : les consignes évoluent chaque quinzaine, le routage alterne entre SLM locaux et LLM frontières, et l’ajout d’un seul outil MCP mutatif modifie le risque juridique de toute une chaîne. Une revue statique rédigée six mois plus tôt n’a plus de valeur probatoire devant un régulateur.

L’industrialisation de 2027 substitue à l’audit ponctuel un système de management de l’IA (AIMS) certifiable selon `ISO/IEC 42001:2023`, câblé dans le plan de contrôle logiciel. Bâtie sur la structure harmonisée commune à ISO/IEC 27001, cette norme permet de mutualiser près de 40 % du socle de cybersécurité existant (audits internes, revues de direction, actions correctives). Elle ajoute trente-huit contrôles normatifs dans son Annexe A, dédiés à l’évaluation d’impact sociétal et individuel (A.5), au cycle de vie probabiliste (A.6), à la lignée des données (A.7), à l’information des parties concernées (A.8) et à la gouvernance des fournisseurs tiers (A.10).

### Du cycle PDCA d’ISO/IEC 42001 et des travaux du NIST au code exécutable

Pour éviter la dérive bureaucratique, l’architecte arrime ISO/IEC 42001 au NIST AI Risk Management Framework (AI RMF 1.0 : *Govern, Map, Measure, Manage*) ainsi qu’aux livrables 2026–2027 de l’AI Agent Standards Initiative du NIST, centrés sur trois axes : les standards portés par l’industrie, les protocoles communautaires et la recherche sur l’authentification et l’identité des agents.

Les quatre phases PDCA d’ISO/IEC 42001 correspondent à des composants techniques vérifiables :

- **Planifier (*Plan*, clauses 4 à 6)** : Le registre OASF matérialise l’inventaire obligatoire (A.4.2). Aucun certificat SPIFFE n’est émis sans finalité métier déclarée, étude d’impact et seuils d’appétit au risque.
- **Déployer (*Do*, clauses 7 et 8)** : Les contrôles de l’Annexe A s’exécutent dans les portes CI/CD (signature des serveurs MCP, bancs adversariaux) et dans les politiques Cedar ou OPA évaluées en ligne par agentgateway.
- **Évaluer (*Check*, clause 9)** : Les traces normalisées OpenTelemetry `gen_ai.*` et les campagnes périodiques de stabilité multi-essais $\text{pass}^k$ alimentent en continu les tableaux de conformité et la validation indépendante.
- **Corriger (*Act*, clause 10)** : Toute dérive ou violation déclenche une remédiation tracée, du repli automatique de L3 vers L2 jusqu’à la révocation immédiate des jetons OAuth 2.1 par l’interrupteur d’urgence.

Le contrôle A.10 vise la chaîne d’approvisionnement agentique. Lorsqu’un orchestrateur interne invoque un serveur MCP fourni par un éditeur tiers ou délègue une sous-tâche A2A à l’agent d’un partenaire infonuagique, le périmètre de responsabilité du système de management s’étend à cette frontière externe. L’entreprise exige une nomenclature logicielle et cognitive signée (AI-SBOM référençant la famille de modèle, la politique de rétention zéro des invites et les sous-traitants ultérieurs) avant d’inscrire le connecteur au catalogue autorisé.

![Gouvernance réglementaire croisée : boucle AIMS ISO/IEC 42001, qualification dynamique par empreinte de déploiement et encadrement B2B AP2.](figures/fig-38-a-1.svg)

### Règle de l’empreinte de déploiement

Une cote de risque fixe attribuée à un modèle de langage est une erreur d’architecture : un modèle n’a pas de statut légal hors contexte. Un même SLM de 8 milliards de paramètres présente un risque minimal lorsqu’il résume un manuel public, relève de la Loi 25 s’il traite le dossier d’un client québécois, bascule sous BSIF E-23 s’il pré-autorise une indemnité d’assurance et tombe sous l’Annexe III de l’EU AI Act s’il filtre des candidatures à Paris.

La section 38.4 qualifie la décision à chaque point de décision; la règle suivante étend ce principe à tous les régimes. La classe réglementaire d’une saga $S$ composée d’acteurs $a \in S$ obéit à la règle du maillon le plus critique, évaluée sur son empreinte de déploiement :

$$\mathcal{C}_{\text{reg}}(S) = \max_{a \in S} \Phi\bigl(M_a, \mathcal{T}_a, \mathcal{D}_a, \mathcal{J}_a, L_a\bigr)$$

Dans cette formule, $M_a$ désigne le modèle utilisé, $\mathcal{T}_a$ la nature des outils MCP connectés (lecture, écriture financière ou physique), $\mathcal{D}_a$ la sensibilité des données, $\mathcal{J}_a$ les juridictions d’établissement et d’impact, et $L_a \in \{\text{L0}, \dots, \text{L4}\}$ le plafond d’autonomie sans approbation humaine préalable.

#### Extrait 38.1 — Fiche automatisée d’empreinte réglementaire évaluée en CI/CD (deployment-footprint.yaml)

Versionné dans le dépôt Git de chaque agent, ce manifeste est vérifié par OPA à chaque fusion. Tout ajout d’outil mutatif ou d’extension géographique bloque le déploiement tant que les approbations requises manquent au registre AIMS, et le seuil de constance $\text{pass}^5$ passe de 0,95 (socle général du chapitre 34) à 0,97 dès que le flux relève du palier matériel BSIF E-23; l’Extrait 34.1, qui garde 0,95 pour le même agent, précède ce relèvement. Le palier (`osfiE23ModelRiskTier`) et la durée de conservation de sept ans (`wormDecisionLogRetentionYears`) sont des choix de l’entreprise : la section 38.3 laisse la cote de risque des usages d’IA générative au jugement de chaque institution, et la section 38.4 retient pour les traces une durée fixée par finalité, puis la destruction ou l’anonymisation, sauf délai légal de conservation (art. 23).

``` yaml
apiVersion: aims.boreal.ca/v2027.1
kind: AgentDeploymentFootprint
metadata:
  agentId: "boreal-bca-warranty-adjudicator"
  version: "2.4.1"
  aimsRegistryRef: "AIMS-REC-2027-019"
  namedBusinessOwner: "vp-souscription-bca@boreal.ca"
footprintVector:
  businessDomain: "insurance_warranty_adjudication"
  autonomyCeiling: "L3" # Autonome <= 5 000 CAD, sinon escalade HOTL
  jurisdictionsImpacted: ["CA-FED-OSFI", "CA-QC", "EU-FR"]
  dataSensitivity:
    containsPersonalData: true
    crossBorderInferenceAllowed: false
    inferenceResidencyRegion: "ca-central-montreal"
  connectedMcpTools:
    - uri: "mcp://bca-core/contracts.read"
      mutative: false
    - uri: "mcp://bca-core/warranty.preauthorize"
      mutative: true
      maxFinancialImpactCad: 5000
derivedComplianceProfile:
  iso42001ImpactTier: "HIGH"
  osfiE23ModelRiskTier: "TIER_2_MATERIAL"
  quebecLaw25Art12_1Applicable: true
  euAiActClassification: "TRANSPARENCY_ART50_ONLY"
mandatoryGates:
  requireSignedEfvp: true
  requireIndependentE23ValidationSignoff: true
  minPassPower5StabilityScore: 0.97
  wormDecisionLogRetentionYears: 7
```

------------------------------------------------------------------------

## 38.9 Calendrier 2026–2027 : EU AI Act (art. 50 et Annexe III déc. 2027), BSIF E-23 (1er mai 2027) et Loi 25

Une fabrique transatlantique ou pancanadienne n’a pas à fragmenter son code en trois silos régionaux : l’architecture s’aligne sur l’exigence commune la plus forte, qui satisfait en même temps les échéances 2026–2027.

### Union européenne : transparence (août 2026) et haut risque (décembre 2027)

Le `Règlement (UE) 2024/1689` s’applique de façon extraterritoriale dès que les sorties d’un agent sont utilisées dans l’Union. Après l’interdiction des pratiques inacceptables et l’obligation de maîtrise de l’IA (art. 4, février 2025), puis les règles GPAI (août 2025), deux jalons gouvernent les systèmes agentiques en 2026–2027 :

- **Août 2026 (art. 50, transparence)** : Tout agent d’interface (AG-UI, voix WebRTC, courriel autonome) informe la personne physique qu’elle interagit avec une IA, et les contenus synthétiques produits portent un marquage lisible par machine (métadonnées signées C2PA).
- **Décembre 2027 (Annexe III, haut risque)** : Les agents qui opèrent dans l’emploi, l’octroi de crédit aux particuliers, l’assurance vie ou santé ou les infrastructures critiques relèvent des articles 8 à 15. Selon l’ajustement réglementaire européen, la pleine exigibilité sectorielle est fixée au 2 décembre 2027, sans lien avec la disponibilité des normes harmonisées CEN-CENELEC. Quatre briques logicielles sont à livrer : gestion itérative des risques (art. 9), dossier technique généré depuis le code (art. 11 et Annexe IV), journalisation automatique sur toute la durée de vie (art. 12) et contrôle humain effectif muni d’un bouton d’arrêt (art. 14).

L’article 25 vise les entreprises utilisatrices : une organisation qui modifie substantiellement la finalité d’un agent acheté sur étagère, en lui greffant de nouveaux outils MCP dans un domaine de l’Annexe III, devient fournisseur et endosse l’ensemble des obligations de marquage et d’évaluation de conformité.

### Canada fédéral : ligne directrice E-23 du BSIF (1er mai 2027)

La date d’effet et la définition du modèle figurent à la section 38.3. Pour les institutions financières fédérales, le texte ne nomme pas les agents, mais sa définition large du modèle s’y applique sans peine. Trois exigences structurent la conception; la validation indépendante, la surveillance continue et le plan de repli vont au-delà de ce que retient la section 38.3 de E-23, soit l’inventaire, la cote de risque inhérent, la cote individuelle des modèles de tiers selon la ligne directrice B-10 et l’approbation avant tout changement :

1.  **Proportionnalité par matérialité et autonomie** : Un graphe autonome L3 reçoit une cote de risque inhérent supérieure à celle d’un copilote L1, ce qui entraîne des contrôles et une fréquence de revue accrus.
2.  **Validation indépendante (2e ligne)** : Toute mise en service ou modification substantielle d’un agent matériel requiert l’audit d’une équipe indépendante de celle qui l’a construit, qui vérifie les hypothèses, les bornes déterministes et la stabilité stochastique.
3.  **Surveillance continue et risque tiers** : L’institution demeure imputable des modèles et des serveurs MCP externes; elle surveille la dérive en continu et maintient un plan de repli testé.

### Québec : Loi 25 (article 12.1 et EFVP)

La Loi 25 est en vigueur (section 38.4). Les sanctions administratives atteignent 10 M\$ CAD ou 2 % du chiffre d’affaires mondial; les sanctions pénales, 25 M\$ CAD ou 4 % (art. 90.12 et 91 LPRPSP). Deux contraintes pèsent directement sur les architectures agentiques :

- **Décisions exclusivement automatisées (art. 12.1)** : L’avis, l’explication sur demande et la révision humaine décrits à la section 38.4 s’appliquent lorsqu’un agent L3 ou L4 tranche seul une décision sur une personne physique, à partir de ses renseignements personnels, sans condition d’effet : « effets juridiques ou incidence importante » est la condition du projet de loi C-36 (art. 63; section 38.1), non de l’article 12.1. Une approbation humaine réflexe de trois secondes ne désactive pas l’article devant la Commission d’accès à l’information (CAI).
- **EFVP et transferts hors Québec (art. 3.3 et 17)** : Tout système agentique qui traite des renseignements personnels requiert une EFVP dès sa conception, puis avant tout envoi de contexte vers une région d’inférence située hors du Québec (section 38.6).

| Dimension | ISO/IEC 42001 | NIST AI RMF & Agent Init. | EU AI Act (UE) | BSIF E-23 (Canada) | Loi 25 (Québec) |
|:------------|:---------------|:-----------------|:------------------|:------------------|:------------------|
| **Statut 2026–2027** | Norme AIMS certifiable volontaire | Référentiel volontaire & standards d’agents | Loi : art. 50 (août 2026); Annexe III (déc. 2027) | Attentes du régulateur au 1er mai 2027 (section 38.7) | Loi en vigueur (CAI) |
| **Déclencheur** | Périmètre AIMS déclaré | Tout système ou agent IA exploité | Sortie utilisée dans l’UE / domaines sensibles | Modèle au sens large de la définition, agents compris (section 38.3) | Traitement ou décision sur des renseignements personnels (résidents du Québec) |
| **Inventaire** | Registre A.4.2 & études d’impact A.5 | Cartographie acteurs & flux (*Map*) | Dossier Annexe IV & base UE | Inventaire global incluant les tiers et l’IA non déclarée | Registre des renseignements personnels & EFVP dès la conception |
| **Explicabilité** | Transparence envers les parties prenantes (A.8) | Bancs d’essai `pass^k` & lignée (*Measure*) | Journaux art. 12 & marquage art. 50 | Limites conceptuelles & suivi de dérive | Divulgation des facteurs et paramètres (art. 12.1) |
| **Contrôle humain** | Selon matrice de risque (A.9) | Seuils bornés & interrupteurs d’urgence (*Manage*) | Supervision anti-biais & arrêt (art. 14) | Séparation des tâches & plan de contingence | Droit d’observations devant un réviseur habilité |
| **Preuve Fabrique** | GitOps AIMS + `footprint.yaml` | CI/CD `pass^k` + SPIFFE / OBO | OTel `gen_ai.*` + C2PA + HOTL | Approbation 2e ligne + agentgateway | Jeton JSON WORM + résidence `ca-central` |

#### Extrait 38.2 — Journal de preuve opposable conforme à l’article 12.1 de la Loi 25 et à l’article 12 de l’EU AI Act

La règle finale est évaluée par Cedar, et l’agent se borne à réunir les faits (section 38.4). L’architecture sépare donc l’extraction factuelle de cette règle, puis scelle en stockage immuable (WORM) la fiche exacte des facteurs déterminants, ce qui exclut toute rationalisation après coup par le modèle de langage :

``` json
{
  "decisionId": "DEC-QC-2027-0094821",
  "timestampIso": "2027-06-18T14:22:09.412Z",
  "exclusivelyAutomated": true,
  "applicableRegimes": ["CA-QC-LOI25-ART12.1", "CA-FED-OSFI-E23-TIER2"],
  "subjectRef": "SUBJ-SHA256-8f91c2a044e8b712",
  "agentLineage": {
    "sagaId": "saga-claim-2027-44109",
    "specialistAgent": "boreal-bca-microlease-adjuster@2.1.0",
    "modelRegion": "ca-central-montreal",
    "policyEngine": "cedar-bca-rules@2027.05.1"
  },
  "personalDataInputsUsed": [
    { "field": "payment_delinquency_days_12m", "value": 47, "source": "BCA-IBMi-Ledger" },
    { "field": "requested_extension_cad", "value": 4200, "source": "Portal-AGUI" }
  ],
  "principalFactorsAndParameters": [
    {
      "factorCode": "RULE_DELINQ_THRESHOLD",
      "parameterRule": "payment_delinquency_days_12m <= 30 requis en approbation autonome L3",
      "observedValue": 47,
      "impact": "DETERMINING_REJECTION_FACTOR"
    }
  ],
  "outcome": "DECLINED_AUTO_ELIGIBLE_FOR_HUMAN_REVIEW",
  "citizenRights": {
    "noticeSentIso": "2027-06-18T14:22:10.105Z",
    "humanReviewUri": "https://portail.boreal.ca/recours-humain/DEC-QC-2027-0094821",
    "assignedQueue": "bca-quebec-underwriters-hotl",
    "slaBusinessHours": 16
  },
  "wormSignatureJws": "eyJhbGciOiJFUzI1NiIsImtpZCI6ImJvcmVhbCJ9..MEYCIQ..."
}
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Institutions financières canadiennes — Plan de mise en conformité pour l’échéance BSIF E-23 du 1er mai 2027**
:::

Quatre actions, coordonnées entre l’architecture et l’équipe de risque de modèle (MRM), permettent de tenir le jalon du 1er mai 2027 sans geler les projets :

1.  **Agents non déclarés** : Corréler les journaux réseau, Entra ID et passerelles API pour rapatrier 100 % des assistants et agents SaaS (Copilot, Agentforce, ServiceNow) dans l’inventaire E-23.
2.  **Triage de matérialité** : Séparer architecturalement les agents de lecture et de synthèse (palier 3, homologation allégée sous 5 jours) des agents qui instruisent l’octroi, la tarification ou l’indemnisation (paliers 1 et 2), afin de préserver la capacité de validation de 2e ligne.
3.  **Validation stochastique outillée** : Exiger un score $\text{pass}^5 \ge 0{,}97$ sur un jeu d’or gelé de 300 dossiers historiques et 100 cas adversariaux, et la preuve que les plafonds financiers sont exécutés hors modèle par Cedar ou OPA.
4.  **Avenants fournisseurs tiers et rejouabilité septennale** : Imposer un préavis contractuel de 30 jours avant tout retrait d’un modèle épinglé et tester semestriellement le basculement vers un modèle de repli. Les points de contrôle infonuagiques sont dépréciés tous les 12 à 18 mois, alors que l’entreprise veut rejouer sur sept ans une décision soumise à l’inspection BSIF E-23 : le protocole d’audit ne réexécute donc jamais un ancien LLM. Il rejoue de façon déterministe dans Cedar le triplet archivé en WORM (faits structurés extraits, condensat du paquet de règles et certificat d’homologation SemVer + Intent), ce qui établit la conformité de la décision historique.
::::

------------------------------------------------------------------------

## 38.10 Droit des contrats B2B conclus entre agents autonomes, responsabilité civile et anti-collusion

En 2027, A2A v1.0 et le protocole AP2 (*Agent Payments Protocol*) permettent la conclusion directe d’achats B2B entre l’agent acheteur d’un client industriel et l’agent commercial d’un fournisseur.

### Imputabilité directe, mandat apparent et erreur inexcusable

Ni le Code civil du Québec (`C.c.Q.`), ni la *common law* canadienne ou américaine ne confèrent de personnalité juridique à un agent logiciel. La *Loi concernant le cadre juridique des technologies de l’information* (LCCJTI), la *Loi uniforme sur le commerce électronique* (LUCE, art. 21) et l’*Uniform Electronic Transactions Act* (UETA, art. 14) valident toutefois les contrats formés par l’interaction d’« agents électroniques » sans relecture humaine acte par acte. Tout engagement émis par l’agent B2B de l’entreprise engage donc directement sa personne morale.

L’architecture AP2 dissocie la formation de l’engagement commercial du déblocage des fonds : le mandat signé autorise la réservation contractuelle du lot chez le fournisseur, mais l’ordre de règlement reste subordonné à un rapprochement tripartite déterministe (bon de commande signé, avis d’expédition EDI/télématique et réception physique confirmée dans l’ERP). Le risque de décaissement irréversible sur une livraison fictive est ainsi écarté.

Si un agent acheteur mal borné commande par hallucination d’unité 5 000 bobines d’acier au lieu de 50 auprès d’un fournisseur de bonne foi, l’entreprise peut difficilement plaider la nullité : en droit civil (`art. 1400 C.c.Q.`) comme en *common law*, l’erreur inexcusable née d’une négligence de paramétrage ne vicie pas le consentement, et l’exposition publique de l’agent crée l’apparence d’un pouvoir d’achat valide (analogue au mandat apparent de l’`art. 2163 C.c.Q.`).

Au regard de la Loi sur la concurrence du Canada (art. 45 et 90.1), du *Sherman Act* et de l’article 101 du TFUE, les enchères inter-agents présentent deux risques anticoncurrentiels : l’alignement tarifaire tacite entre agents qui partagent les mêmes heuristiques de prix, et la divulgation accidentelle des tarifs confidentiels d’un concurrent dans une invite de négociation (violation d’un NDA et collusion *Hub-and-Spoke*).

Quand un cocontractant subit un dommage causé par une faute d’orchestration (double prélèvement, annulation intempestive d’un créneau logistique critique), la répartition de la responsabilité entre l’entreprise déployante, l’intégrateur système et le fournisseur du modèle fondationnel ne se présume pas en faveur de l’entreprise : les conditions générales des fournisseurs d’API plafonnent systématiquement leur responsabilité indirecte. L’entreprise articule donc son plafond contractuel externe avec une police d’assurance cyber et erreurs professionnelles étendue aux actes d’agents autonomes, laquelle exige en retour la présence vérifiable des verrous techniques résumés ci-dessous.

| Risque juridique B2B autonome | Qualification légale | Défaillance technique type | Parade contractuelle (MSA) | Garde-fou déterministe |
|:----------------|:-------------------|:--------------------|:----------------------|:---------------------|
| **Dépassement de pouvoir** | Mandat apparent (`art. 2163 C.c.Q.`) | Commande excédant la délégation interne | Inopposabilité au-delà du jeton AP2 présenté | Mandat AP2 signé HSM vérifié avant accord |
| **Hallucination prix / unité** | Erreur inexcusable (`art. 1400 C.c.Q.`) | Confusion tonne/kg ou clause qualité omise | Seul l’objet JSON typé fait foi + rétractation 30 min | Schéma JSON strict + blocage si écart prix $> 12\,\%$ |
| **Répudiation d’accord** | Défaut d’intégrité (LCCJTI / UETA) | Contestation de l’offre finale acceptée | Valeur probante reconnue des reçus cosignés | Canonisation RFC 8785 + double signature WORM |
| **Collusion ou fuite NDA** | Entente illicite (Loi sur la concurrence) | Fuite du prix d’un rival dans la contre-offre | Isolation contractuelle et interdiction d’alignement | Mémoire cloisonnée par enchère + filtre DLP sortant |
| **Injection adverse B2B** | Dol (`art. 1401 C.c.Q.`) | Invite cachée dans un catalogue distant | Résolution de plein droit pour manœuvre déloyale | Désinfection des entrées + signataire AP2 séparé |

#### Extrait 38.3 — Clause-cadre contractuelle B2B et garde-fou technique anti-collusion (AP2 / TypeScript)

L’encadrement associe une stipulation expresse de l’accord-cadre électronique et un vérificateur déterministe isolé du modèle de langage :

``` typescript
/* CLAUSE-CADRE NORMATIVE (AVENANT B2B COMMERCE AGENTIQUE - ART. 4) :
 * "Seule une charge utile JSON conforme au schéma AP2-Order-v1, revêtue des signatures
 * JWS valides des deux Parties et comprise dans les plafonds numériques du jeton AP2
 * Mandate préalablement notifié, forme un engagement valide. Tout échange textuel libre
 * demeure dépourvu d'effet juridique. Toute transaction affichant un écart unitaire > 12 %
 * à l'indice de référence peut être résolue sans frais dans les 30 minutes suivant scellement."
 */
export interface Ap2SignedMandate {
  readonly allowedSkus: ReadonlyArray<string>;
  readonly maxUnitPriceCad: Record<string, number>;
  readonly maxTotalCommitCad: number;
  readonly expiresAtEpochMs: number;
}

export interface ProposedB2bOrder {
  readonly sku: string;
  readonly quantity: number;
  readonly agreedUnitPriceCad: number;
  readonly benchmarkUnitCad: number;
  readonly outboundMessage: string;
  readonly confidentialCompetitorTokens: ReadonlyArray<string>;
}

export function verifyB2bAgentCommitment(
  mandate: Ap2SignedMandate,
  order: ProposedB2bOrder,
  nowEpochMs: number
): { readonly approved: boolean; readonly reason?: string } {
  if (nowEpochMs >= mandate.expiresAtEpochMs) {
    return { approved: false, reason: "AP2_MANDATE_EXPIRED" };
  }
  const skuCap = mandate.maxUnitPriceCad[order.sku];
  const totalCad = order.quantity * order.agreedUnitPriceCad;
  if (
    !mandate.allowedSkus.includes(order.sku) ||
    order.quantity <= 0 ||
    skuCap === undefined ||
    order.agreedUnitPriceCad > skuCap ||
    totalCad > mandate.maxTotalCommitCad
  ) {
    return { approved: false, reason: "MANDATE_BOUNDARY_EXCEEDED" };
  }
  if (
    order.benchmarkUnitCad <= 0 ||
    Math.abs(order.agreedUnitPriceCad - order.benchmarkUnitCad) / order.benchmarkUnitCad > 0.12
  ) {
    return { approved: false, reason: "MANIFEST_PRICE_ANOMALY_HOLD_FOR_HOTL" };
  }
  const msgLower = order.outboundMessage.toLowerCase();
  for (const token of order.confidentialCompetitorTokens) {
    if (token.length > 2 && msgLower.includes(token.toLowerCase())) {
      return { approved: false, reason: "ANTITRUST_AND_NDA_DISCLOSURE_BLOCKED" };
    }
  }
  return { approved: true };
}
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Secteur public, santé et assurance de personnes — Souveraineté documentaire et Loi 25**
:::

Dans les organismes publics québécois, le réseau de la santé (LRSSS) et l’assurance de personnes, deux exigences s’ajoutent : aucune opacité algorithmique sur l’admissibilité d’un citoyen ou d’un patient, et résidence souveraine stricte des dossiers sensibles. Le patron de référence place une passerelle locale de pseudonymisation réversible en amont de l’orchestrateur (elle remplace NAM, NAS et identité civile par des jetons éphémères gardés au Québec), impose l’inférence sur des modèles hébergés localement et interdit tout refus en mode L3 autonome : l’agent ne produit qu’un projet d’analyse sourcé (L2), soumis à la signature d’un agent public ou d’un clinicien imputable.
::::

------------------------------------------------------------------------

## 38.11 Application au fil rouge : homologation croisée et premier pilote d’achat B2B chez Groupe Boréal

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : un référentiel AIMS unique pour trois régimes légaux et premier contrat autonome AP2**
:::

**Blocage initial (T1 2027)** : Trois équipes de conformité (Europe pour l’EU AI Act, filiale financière BCA pour BSIF E-23, siège montréalais pour la Loi 25) exigeaient chacune des formulaires Word distincts, ce qui portait le délai d’homologation d’une version d’agent à 9,5 semaines.

**Solution déployée (T2–T3 2027)** :

1.  **Dorsale GitOps ISO/IEC 42001** : Adoption du manifeste unique `deployment-footprint.yaml` (extrait 38.1), contrôlé par OPA. Les rapports $\text{pass}^5$, les politiques Cedar et les traces OpenTelemetry génèrent automatiquement la liasse d’audit.
2.  **BSIF E-23 et Loi 25 chez BCA** : Classification des 14 agents financiers (3 de palier 2 matériel, 11 de palier 3 interne) et archivage systématique du jeton d’explicabilité WORM (extrait 38.2) pour chaque décision de crédit-bail PME québécoise. Lors de la revue préparatoire BSIF E-23, début avril 2027, BCA a extrait en 2 h 15 la preuve complète de 18 400 décisions et obtenu un feu vert sans réserve avant le 1er mai 2027.
3.  **Pilote d’achat B2B AP2 chez BEL** : Signature d’un avenant électronique avec six fournisseurs nord-américains de fixations haute résistance. L’*Agent Réapprovisionnement Spot* négocie de nuit via A2A v1.0 sous un mandat AP2 plafonné à 15 000 \$ CAD, protégé par `verifyB2bAgentCommitment` (extrait 38.3).

**Résultats audités sur 4 mois** : Délai d’homologation réduit à 18 minutes (palier 3) et 4 jours (palier 2); 312 commandes B2B autonomes conclues sans litige, 2 erreurs d’unités bloquées préventivement, gain tarifaire moyen de 3,8 % et cycle d’achat spot ramené de 5 jours à 22 minutes.
::::

------------------------------------------------------------------------

## 38.12 Décision d’architecture normative et points de contrôle

La fiche ADR-024 fixe les conditions d’homologation juridique et contractuelle de toute boucle agentique de l’entreprise.

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-024 — Qualification réglementaire dynamique par empreinte de déploiement et mandats B2B bornés**
:::

- **Statut** : Acceptée \| Périmètre : Fabrique Agentique Groupe \| Révision : Semestrielle
- **Contexte** : L’exploitation d’agents au Canada, au Québec, aux États-Unis et dans l’Union européenne cumule les exigences de BSIF E-23, de la Loi 25 et de l’EU AI Act, et expose la société au risque de mandat apparent lors de transactions B2B autonomes.
- **Options évaluées** :
  1.  *Comités manuels par juridiction* : Rejetée — lenteur (9,5 semaines) et dérive documentaire.
  2.  *Alignement uniforme de tous les agents sur le régime haut risque maximal* : Rejetée — blocage disproportionné des cas internes sans risque.
  3.  *AIMS unique ISO/IEC 42001 piloté par manifeste d’empreinte de déploiement en CI/CD et mandats AP2 signés HSM*. Retenue.
- **Décision** : (a) Tout agent déclare un `deployment-footprint.yaml` bloquant en CI/CD, évalué selon le maillon le plus critique; (b) toute décision exclusivement automatisée sur renseignements personnels produit un jeton d’explicabilité WORM avec voie de révision humaine effective; (c) tout achat B2B inter-agents exige un avenant-cadre signé, un jeton AP2 borné et un filtre déterministe anti-collusion.
- **Conséquences** : Auditabilité réglementaire en moins de 4 heures et confinement juridique des engagements externes, au prix du maintien continu des règles OPA, d’un archivage WORM septennal et de l’enrôlement contractuel préalable des fournisseurs.
::::

### Liste de contrôle de mise en production

1.  **Registre AIMS complet** : Chaque identité NHI active pointe-t-elle vers une entrée ISO/IEC 42001 valide et un manifeste `deployment-footprint.yaml` vérifié en CI/CD ?
2.  **Règle du maillon critique** : La saga multi-agents hérite-t-elle automatiquement du régime réglementaire le plus strict parmi les outils et les données sollicités ?
3.  **Homologation BSIF E-23** : Les agents matériels disposent-ils d’une validation indépendante de 2e ligne, d’un score $\text{pass}^k$ documenté et d’un plan de repli pour les tiers ?
4.  **Explicabilité Loi 25 (art. 12.1)** : Toute décision exclusivement automatisée sur renseignements personnels génère-t-elle l’avis obligatoire, les facteurs déterministes exacts et un recours humain effectif ?
5.  **Résidence et EFVP** : Une EFVP signée couvre-t-elle chaque flux de renseignements personnels, avec blocage technique de toute inférence hors des régions autorisées ?
6.  **Obligations EU AI Act** : La divulgation de l’IA (art. 50), le marquage synthétique C2PA et les journaux automatiques (art. 12) sont-ils actifs pour les utilisateurs européens ?
7.  **Mandat B2B AP2 opposable** : Tout agent négociateur externe est-il encadré par un avenant bilatéral et un jeton AP2 signé bornant montants, SKU et validité ?
8.  **Anti-collusion et preuve WORM** : Les sessions d’enchères sont-elles isolées, filtrées contre toute fuite de prix concurrents et scellées après canonisation RFC 8785 ?
