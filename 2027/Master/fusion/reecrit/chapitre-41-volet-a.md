## Mise en œuvre — Modèle opérationnel cible, facteur humain (HOTL) et prospective 2028–2030 {.volet}

:::: {.encadre .executive}
::: {.encadre-titre}
**Synthèse exécutive**
:::

- **Enjeu stratégique** : superposer un maillage technique transversal (MCP, A2A, moteurs durables) à une organisation restée en silos produit soit un goulot centralisé, soit des agents orphelins dont plus personne ne maîtrise ni les coûts ni la dérive métier. Par ailleurs, lorsque la fiabilité autonome approche les 90 %, la complaisance cognitive des superviseurs (OWASP ASI09) réduit la validation humaine à une formalité si le poste de travail n’est pas instrumenté.
- **Décisions organisationnelles et architecturales structurantes** :
  1.  *Irréversible culturellement* : déployer un modèle opérationnel Hub-and-Spoke, qui articule un centre d’excellence agentique resserré (plateforme, sécurité, ontologies, FinOps) et des cellules métiers fédérées où chaque boucle active relève d’un propriétaire métier nominatif (*Named Business Owner*) et d’une gouvernance conjointe RH–IT.
  2.  *Structurante dès la mise en service* : fonder la supervision *Human-on-the-Loop* (HOTL) sur des vues différentielles sans prose persuasive, un plafond d’arbitrages par quart et des tests canaris continus d’attention humaine.
  3.  *Préparatoire sans regret (2028–2030)* : fonder les investissements de 2027 sur l’agilité cryptographique, des politiques formelles hors prompts et des moniteurs déterministes, pour accueillir plus tard les marchés B2B liquides, l’auto-conception vérifiée et la *Physical AI* sans refonte du socle.
- **Indicateurs de gouvernance** : agents actifs dotés d’un propriétaire métier nominatif valide dans le SIRH (100 %), taux d’interception des tests canaris HOTL ($\ge 92\,\%$), taux de requalification interne des coordonnateurs touchés, ratio de création de valeur nette sur *Cost-per-Outcome*.
::::

## 41.8 Organisation Hub-and-Spoke : centre d’excellence agentique, propriétaires métiers nommés et tandem RH-IT

Les deux défaillances de la section 41.7 se reconnaissent à des symptômes précis. Dans un laboratoire central éloigné des opérations d’usine, de souscription ou de logistique, la file d’attente dépasse neuf mois en deux trimestres, l’équipe maîtrise mal les cas limites de SAP ou Guidewire et les directions métiers contournent le blocage en achetant clandestinement des agents SaaS non gouvernés. Dans la décentralisation sans socle partagé d’identité, d’ontologie ni de FinOps, cinq départements recodent cinq connecteurs incompatibles vers le même référentiel client et, lors d’un incident critique, l’auteur initial du prompt a changé de poste depuis des mois sans successeur désigné.

### Centre d’excellence et cellules métiers

Le modèle fédéré de la section 41.7 prend ici la forme Hub-and-Spoke : l’infrastructure, la sécurité et la sémantique commune sont centralisées; la logique de domaine, le budget d’usage et la supervision opérationnelle restent au plus près des lignes d’affaires.

![Modèle opérationnel cible Hub-and-Spoke : Centre d’Excellence Agentique, tandem RH-IT, cellules métiers fédérées et supervision HOTL.](figures/fig-41-a-1.svg)

1.  **Le *Hub*, centre d’excellence agentique** : une équipe de douze à vingt-cinq spécialistes (pour un groupe de 10 000 à 20 000 personnes), qui ne code pas la logique métier des divisions. Elle livre des chemins pavés : exploitation du moteur d’exécution durable (Temporal / Restate), administration d’agentgateway et du registre OASF/AIMS, gouvernance ontologique (Apache Ossie), harnais d’évaluation CI/CD $\text{pass}^k$, politiques globales Cedar/OPA et pilotage FinOps IA (capacités GPU/API, routage SLM/LLM, refacturation interne au *Cost-per-Outcome*).
2.  **Les *Spokes*, cellules métiers fédérées** : installée dans chaque division, la cellule réunit experts métiers, ingénieurs d’intégration MCP/orchestration, curateur d’ontologie locale et superviseurs HOTL. Avec les gabarits certifiés du *Hub*, elle livre un agent spécialiste homologué en quelques semaines. Sur le plan économique, la relation entre le *Hub* et les *Spokes* passe en six mois d’une simple visibilité des coûts (*Showback*) à une refacturation analytique directe (*Chargeback*) : le *Hub* absorbe le coût fixe du socle mutualisé, tandis que chaque *Spoke* paie mensuellement ses exécutions réelles au *Cost-per-Outcome*, ce qui incite les métiers à préférer les SLM spécialisés à des appels inutiles à des modèles frontières coûteux.

### Propriétaire métier nominatif et tandem RH–IT

Le rôle de propriétaire de l’agent (section 41.4) se précise ainsi, pour éviter les « agents zombies » : aucune identité NHI d’agent de niveau L2, L3 ou L4 ne reste active sans rattachement à un propriétaire métier nominatif (*Named Business Owner*) en exercice. Ce cadre métier, et non l’administrateur technique, porte quatre responsabilités : le budget d’exécution sur son compte de résultat (P&L), la cosignature des seuils d’escalade HOTL, la revue trimestrielle d’exactitude métier et l’obligation d’actionner l’arrêt d’urgence dès qu’une règle commerciale devient caduque.

Le tandem RH–IT synchronise quatre processus autrefois séparés :

- **Couplage direct SIRH – registre d’agents** : lorsqu’un propriétaire métier nominatif quitte son poste ou change de rôle dans Workday, un webhook ouvre un délai de soixante-douze heures pour transférer la tutelle à son successeur; sans signature, le plan de contrôle rétrograde automatiquement ses agents de L3 vers L2 (validation humaine systématique) et gèle leurs signatures externes.
- **Conception conjointe des postes hybrides** : avant d’automatiser les tâches répétitives d’une équipe, le tandem redessine le rôle humain cible, pour enrichir le travail analytique et éviter un poste résiduel fragmenté.
- **Arbitrage capacitaire unifié** : les comités budgétaires comparent sur une grille commune le recrutement humain, l’impartition et le budget d’inférence agentique, rapportés au résultat métier.
- **Certification de littératie IA** : aucun superviseur HOTL ne reçoit ses droits d’approbation CIBA sans validation pratique d’un parcours sur les biais d’automatisation et la lecture critique de preuves. Cette règle va au-delà de ce que retient l’exposé : l’obligation européenne de maîtrise de l’IA (article 4 de l’EU AI Act) a été allégée par le Digital Omnibus (section 41.5, chapitre 35).

| Activité du cycle de vie agentique | Hub — centre d’excellence (plateforme) | CISO, Juridique & Risques | Cellule FinOps IA | Direction RH | Propriétaire métier nominatif | Ingénierie de la cellule |
|:--------------------|:--------------|:---------------|:------------|:----------|:--------------|:------------|
| **Socle (agentgateway, moteur d’exécution durable)** | **R / A** | C | C | I | I | C |
| **Ontologie Ossie & contrats A2A** | **A** | I | I | I | C | **R** |
| **Spécialiste métier & serveurs MCP** | C | C | I | I | **A** | **R** |
| **Qualification Footprint & dossier E-23** | C | **A** | I | I | C | **R** |
| **Plafonds financiers & seuils HOTL** | I | C | C | C | **A / R** | C |
| **Quotas jetons & suivi *Cost-per-Outcome*** | C | I | **R** | I | **A** | C |
| **Postes hybrides, requalification & social** | I | C | I | **A / R** | **R** | I |
| **Arrêt d’urgence** | **R** | **A / R** | C | I | **A / R** | C |

*(Légende RACI : R = Réalisateur, A = Approbateur imputable, C = Consulté, I = Informé.)*

#### Extrait 41.1 — Charte d’investiture exécutable d’un *Named Business Owner* (ownership-charter.yaml)

Synchronisée chaque jour avec le SIRH, la charte relie la flotte active à son dirigeant métier imputable :

``` yaml
apiVersion: governance.boreal.ca/v2027.1
kind: NamedBusinessOwnerCharter
metadata:
  charterId: "OWN-BEL-2027-008"
  effectiveDate: "2027-04-01"
  reviewCadenceDays: 90
subjectAgentFleet:
  sagaOrAgentIds: ["boreal-bel-spot-procurement", "boreal-bel-sap-inventory"]
  autonomyGranted: "L3"
accountableExecutive:
  employeeWorkdayId: "EMP-CA-004192"
  fullName: "Marc-Antoine Lavoie"
  roleTitle: "VP Chaîne d'Approvisionnement (BEL)"
  costCenterCode: "CC-4100-LOG-MFG"
  backupDelegateWorkdayId: "EMP-CA-006811"
operationalMandateAndCaps:
  monthlyInferenceAndInfraCapCad: 18500
  maxSingleTransactionCommitmentCad: 15000
  mandatoryBusinessKpis:
    minOrderAccuracyRate: 0.992
    minHotlCanaryCatchRate: 0.92
orphanedAgentPolicy:
  hrStatusTrigger: ["TERMINATED", "LEAVE_EXTENDED", "ROLE_CHANGED"]
  gracePeriodHours: 72
  automaticFallbackAction: "DOWNGRADE_TO_L2_HITL_AND_FREEZE_AP2_SIGNING"
```

------------------------------------------------------------------------

## 41.9 Ergonomie cognitive du Human-on-the-Loop (HOTL) et complaisance d’automatisation (ASI09)

L’escalade vers un opérateur humain en mode *Human-on-the-Loop* (HOTL) est le dernier recours pour les cas ambigus et les exigences légales (EU AI Act art. 14, Loi 25 art. 12.1, BSIF E-23). Or le référentiel OWASP Top 10 for Agentic Applications (ASI09, *Human-Agent Trust Exploitation*) relève un paradoxe, confirmé par l’ergonomie aéronautique : plus l’automatisation est fiable au quotidien, plus la vigilance réelle du superviseur se dégrade vite. Cette dégradation est la fatigue d’approbation évoquée à la section 41.3. Selon l’exposé, un point d’approbation se justifie par l’imputabilité, non par la performance (section 41.2) : l’effectivité visée ci-dessous est celle d’un examen réellement exercé, non d’une meilleure décision moyenne.

### Pourquoi la supervision classique échoue

Deux facteurs cognitifs affaiblissent l’approbateur :

1.  **Chute de vigilance sur signaux rares (*Mackworth Decrement*)** : devant un flux dont 95 % des propositions pré-instruites sont justes, l’approbateur cesse vite d’inspecter les pièces justificatives; le temps médian d’examen tombe sous cinq secondes, c’est l’approbation réflexe.
2.  **Biais de fluidité persuasive** : même lorsqu’il hallucine ou subit une injection adverse, un LLM rédige sa recommandation dans un style posé, structuré et convaincant, qui affaiblit l’esprit critique.

### Quatre règles de conception du poste HOTL

La console A2UI et le routeur d’escalade appliquent quatre règles, pour que le filet humain soit effectif et opposable aux régulateurs :

- **Règle 1 — Vue différentielle contradictoire** : aucun paragraphe élogieux rédigé par l’agent demandeur. L’écran présente côte à côte les valeurs brutes des systèmes sources, la règle exacte qui a motivé l’escalade, une contre-hypothèse critique (avocat du diable) produite par un agent indépendant et l’impact irréversible chiffré.
- **Règle 2 — Fonction de forçage cognitif** : sur les dossiers matériels, la saisie active d’un paramètre vérifié dans la pièce source (franchise retenue, code d’exclusion) remplace le bouton unique « Approuver » et précède le déblocage de l’authentification CIBA.
- **Règle 3 — Plafond de charge cognitive** : l’attention soutenue se budgète, ce qui chiffre le réglage de la charge évoqué à la section 41.3. Le plafond $N_{\text{max}}^{\text{quart}}$ d’arbitrages complexes par quart de durée nette $T_{\text{effectif}}$ s’écrit :

$$N_{\text{max}}^{\text{quart}} = \left\lfloor \frac{T_{\text{effectif}} \cdot \eta_{\text{vig}}}{t_{\text{analyse}}^{\text{min}}} \right\rfloor$$

Pour $T_{\text{effectif}} = 360\text{ min}$, un coefficient de maintien de vigilance $\eta_{\text{vig}} = 0{,}65$ et un examen sérieux incompressible $t_{\text{analyse}}^{\text{min}} = 7\text{ min}$, la charge maximale s’établit à 33 dossiers complexes par quart. Au-delà, le système met les sagas non urgentes en file durable plutôt que de presser l’examen. Ce plafond calculé va au-delà de ce que retient l’exposé : aucune norme publiée ne fixe la charge d’un superviseur, et la supervision se dimensionne selon la charge mesurée d’exceptions et d’approbations (section 41.4).

- **Règle 4 — Tests canaris d’attention** : la plateforme insère au hasard (3 à 5 % du volume) des dossiers synthétiques plausibles qui contiennent une anomalie subtile connue d’avance (garantie échue la veille, numéro de série discordant), afin de mesurer l’étanchéité réelle du contrôle humain. Si l’interface A2UI les présente à l’identique d’un dossier réel (*aveugle* côté opérateur), leur enveloppe Temporal porte un scellé `dryRunCanary` bloqué sur agentgateway, de sorte qu’une approbation accidentelle ne déclenche jamais d’écriture ni de virement effectif dans un système d’enregistrement (*System of Record*).

#### Extrait 41.2 — Protocole anti-complaisance cognitive HOTL par tests canaris (ASI09 / TypeScript)

Ce capteur s’évalue sur une fenêtre glissante d’au moins cinq canaris, pour écarter le bruit de début de quart. En cas d’érosion de l’attention, il durcit automatiquement la friction de l’interface et ralentit le flux entrant :

``` typescript
export interface HotlReviewSample {
  readonly isSyntheticCanary: boolean;
  readonly expectedCanaryAction?: "REJECT" | "MODIFY";
  readonly humanDecision: "APPROVE" | "REJECT" | "MODIFY";
  readonly dwellSeconds: number;
  readonly evidenceLinksOpened: number;
  readonly minExpectedDwellSeconds: number;
}

export interface HotlQueueStatus {
  readonly canaryCatchRate: number;
  readonly suspectedRubberStampRate: number;
  readonly state: "HEALTHY" | "DRIFT_WARNING" | "ASI09_MITIGATION_ACTIVE";
  readonly actions: ReadonlyArray<string>;
}

export function assessHotlQueueVigilance(
  samples: ReadonlyArray<HotlReviewSample>,
  minCanarySampleSize: number = 5
): HotlQueueStatus {
  const canaries = samples.filter((s) => s.isSyntheticCanary);
  const caught = canaries.filter(
    (c) => c.humanDecision === c.expectedCanaryAction || c.humanDecision === "REJECT"
  );
  const hasStatQuorum = canaries.length >= minCanarySampleSize;
  const canaryCatchRate = canaries.length > 0 ? caught.length / canaries.length : 1.0;

  const liveApprovals = samples.filter(
    (s) => !s.isSyntheticCanary && s.humanDecision === "APPROVE"
  );
  const hastyApprovals = liveApprovals.filter(
    (s) => s.dwellSeconds < s.minExpectedDwellSeconds && s.evidenceLinksOpened === 0
  );
  const suspectedRubberStampRate =
    liveApprovals.length > 0 ? hastyApprovals.length / liveApprovals.length : 0.0;

  if ((hasStatQuorum && canaryCatchRate < 0.85) || suspectedRubberStampRate > 0.15) {
    return {
      canaryCatchRate,
      suspectedRubberStampRate,
      state: "ASI09_MITIGATION_ACTIVE",
      actions: [
        "FORCE_ACTIVE_PARAMETER_ENTRY_UI",
        "THROTTLE_L3_ESCALATION_RATE_25_PCT",
        "ALERT_OPERATIONS_LEAD_FOR_SHIFT_RELIEF"
      ]
    };
  }
  if ((hasStatQuorum && canaryCatchRate < 0.92) || suspectedRubberStampRate > 0.08) {
    return {
      canaryCatchRate,
      suspectedRubberStampRate,
      state: "DRIFT_WARNING",
      actions: ["EMPHASIZE_CONTRASTIVE_DEVIL_ADVOCATE_PANEL"]
    };
  }
  return { canaryCatchRate, suspectedRubberStampRate, state: "HEALTHY", actions: [] };
}
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Relations de travail, conduite du changement et requalification — Du coordonnateur au superviseur de flotte**
:::

Dans un contexte syndiqué ou conventionné, au Canada comme en Europe, la transformation des métiers administratifs de coordination repose sur trois engagements explicites :

1.  **Finalité non disciplinaire garantie par entente** : les métriques d’interception des tests canaris sont agrégées par file pour calibrer l’ergonomie et la formation; une charte cosignée interdit leur usage pour sanctionner individuellement un salarié.
2.  **Parcours certifiant de 120 heures** : les anciens coordonnateurs, détenteurs de la mémoire concrète des exceptions clients et des écrans patrimoniaux, forment le meilleur vivier interne pour devenir superviseurs d’exceptions HOTL, curateurs d’ontologies métier et analystes qualité AgentOps.
3.  **Simulateur de relève pour les juniors** : pour éviter que l’automatisation des cas simples ne prive les nouvelles recrues d’apprentissage terrain (problème de relève de la section 41.5), un jumeau de rejeu soumet aux analystes juniors des dossiers historiques réels à instruire avant confrontation avec les vétérans.
::::

------------------------------------------------------------------------

## 41.10 Horizon 2028–2030 : marchés B2B autonomes liquides, auto-conception vérifiée et Physical AI

Les trajectoires de 2028–2030 restent des hypothèses plausibles : des verrous scientifiques, normatifs et physiques ne sont pas résolus fin 2026–2027.

### Trois frontières après 2027 et leurs verrous

1.  **Marchés B2B autonomes liquides (2028–2029)** : au-delà des relations bilatérales pré-contractualisées du chapitre 38, la généralisation des identifiants d’entités juridiques vérifiables (vLEI de la GLEIF) et des annuaires AGNTCY ouvrira des bourses sectorielles instantanées (fret spot, flexibilité électrique industrielle, capacité GPU). *Verrou critique* : l’instauration de coupe-circuits systémiques de place de marché, capables d’enrayer les krachs éclairs que provoqueraient des milliers d’agents réagissant en millisecondes au même choc externe.
2.  **Auto-conception agentique sous preuve formelle (2029–2030)** : des méta-architectes synthétiseraient à la volée de nouveaux sous-agents et adaptateurs protocolaires. *Verrou scientifique* : tant que la validation reste purement statistique, l’auto-modification en production restera bannie des secteurs critiques (BSIF E-23, santé, énergie). Son adoption exigera une synthèse neuro-symbolique vérifiée, où chaque graphe généré s’accompagne d’une preuve formelle vérifiable par machine (Lean 4, TLA+, solveurs SMT sur politiques Cedar) attestant la terminaison et l’inviolabilité des invariants.
3.  ***Physical AI* incarnée et identités NHI post-quantiques (2028–2030)** : l’intégration entre orchestrateurs d’entreprise (A2A/MCP) et modèles Vision-Langage-Action (VLA) qui pilotent des robots mobiles et des cellules d’assemblage se heurte au verrou de la certification déterministe de sûreté machine (IEC 61508 / ISO 13849). Par ailleurs, la conservation septennale des journaux WORM et des mandats AP2 face à la menace *Harvest Now, Decrypt/Forge Later* impose d’amorcer la migration des signatures vers des suites composites hybrides post-quantiques (ECDSA P-256 + ML-DSA-65 selon NIST FIPS 204). Comme chaque signature ML-DSA-65 occupe 3 309 octets (\~4,5 Ko en Base64url), on l’applique dès maintenant aux scellés WORM et aux mandats externes AP2, tout en conservant des jetons par référence sur les sauts RFC 8693 internes, afin de ne pas saturer les tampons d’en-têtes HTTP de 8 Ko.

| Horizon 2028–2030 | Hypothèse plausible | Verrou non résolu fin 2026–2027 | Décision « sans regret » dès 2027 |
|:---------------|:----------------------------|:----------------------------|:----------------------------|
| **Marchés B2B liquides** | Enchères spot inter-agents via vLEI et règlement séquestré instantané | Coupe-circuits contre les krachs éclairs et fiscalité transfrontalière temps réel | Adopter A2A v1.0, les mandats AP2 et préparer l’identité vLEI |
| **Auto-conception vérifiée** | Synthèse dynamique de sous-graphes prouvés formellement avant déploiement | Passage à l’échelle des preuves automatiques (Lean 4 / TLA+) sur SI complexes | Externaliser dès maintenant toute politique critique hors prompt dans Cedar |
| ***Physical AI* (VLA)** | Jonction directe entre sagas métiers et robotique industrielle polyvalente | Certification IEC 61508 de contrôleurs neuronaux continus | Interposer des jumeaux numériques et une enveloppe matérielle de sûreté |
| **NHI post-quantiques** | Signatures hybrides ML-DSA sur SPIFFE, OBO et archives WORM | Taille des en-têtes HTTP post-quantiques et maturité HSM | Garantir l’agilité cryptographique dans agentgateway et les journaux |

#### Extrait 41.3 — Invariant formel Cedar préparant l’auto-conception vérifiée et l’agilité post-quantique (horizon 2028–2030)

Exprimés dès 2027 dans un langage décidable qu’un solveur SMT peut analyser (tel Cedar Automated Reasoning), les interdits structurels garantissent qu’un futur méta-agent proposant un sous-graphe en 2029 ne pourra ni s’auto-octroyer des privilèges, ni signer avec un algorithme cryptographique déprécié :

``` cedar
// Invariant 1 : Interdiction absolue d'auto-élévation ou d'homologation sans preuve formelle
forbid (
  principal is Boreal::Agent,
  action == Boreal::Action::"RegisterDynamicSubAgent",
  resource is Boreal::AgentRegistry
)
unless {
  context.smtProofVerified == true &&
  principal.delegatedScopes.containsAll(context.proposedScopes) &&
  resource.namedBusinessOwnerStatus == "ACTIVE_WORKDAY"
};

// Invariant 2 : Agilité cryptographique — rejet des signatures non hybrides post-quantiques sur WORM
forbid (
  principal is Boreal::Agent,
  action == Boreal::Action::"SealLongTermAuditRecord",
  resource is Boreal::WormVault
)
unless {
  ["ES256_MLDSA65_HYBRID", "MLDSA87_FIPS204"].contains(context.signatureSuite)
};
```

:::: {.encadre .sectoriel}
::: {.encadre-titre}
**Industrie manufacturière et robotique (Physical AI) — L’architecture Simplex pour l’usine 2029**
:::

Pour faire coopérer un modèle robotique VLA adaptatif avec des opérateurs humains sous norme IEC 61508 SIL 3, le patron de référence est l’architecture Simplex matériellement isolée : le modèle neuronal propose des trajectoires optimales, mais un moniteur cinématique déterministe, formellement prouvé et logé sur un microcontrôleur temps réel distinct, audite chaque commande. Dès que l’état projeté s’approche de la frontière de collision ou de surcouple, le moniteur coupe le canal neuronal et passe la main à un contrôleur de repli certifié, qui met la cellule en arrêt sûr. C’est le pendant cyber-physique du découplage entre plan de contrôle et cellule autonome décrit dans ce compendium.
::::

------------------------------------------------------------------------

## 41.11 Application au fil rouge : bilan à 12 mois de la Fabrique Agentique Boréal et réorganisation des métiers

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Groupe Boréal : bilan chiffré à 12 mois (T4 2026 – T4 2027) et transformation des métiers**
:::

**Point de départ (T4 2026)** : 47 prototypes dispersés, dont 19 *Shadow Agents*, une boucle incontrôlée de onze heures sur erreur HTTP 429 qui a coûté 41 000 \$ CAD, des comptes de service sur-privilégiés qui compromettaient la conformité à la Loi 25 et à BSIF E-23, et 46 heures de coordination manuelle entre ServiceNow (BSN), IBM i (AS/400) (BCA) et SAP S/4HANA (BEL).

**Bilan audité à 12 mois (décembre 2027)** :

1.  **Gouvernance Hub-and-Spoke en régime établi** : un centre d’excellence de 16 spécialistes à Montréal soutient les trois cellules divisionnaires, qui exploitent 28 agents spécialistes réutilisables et 11 sagas transversales, couverts à 100 % par neuf propriétaires métiers nominatifs investis (Extrait 41.1). Aucun *Shadow Agent* ne subsiste.
2.  **Performance opérationnelle, conformité et HOTL** : le délai médian de résolution passe de 46 heures à 11 minutes (88,6 % en autonomie L3, 11,4 % en escalade HOTL). L’homologation est acquise sans réserve majeure sous BSIF E-23 (1er mai 2027), Loi 25 (art. 12.1) et EU AI Act (art. 50). Le taux d’interception des tests canaris se maintient à 95,2 % sur l’année.
3.  **Bilan financier vérifié** : le coût complet annuel d’exploitation (plateforme, SLM internes traitant 79 % des volumes et LLM frontières sur les 21 % complexes) s’établit à 1,94 M\$ CAD (*Cost-per-Outcome* moyen pondéré tous processus de 0,41 \$ CAD, dont 0,19 \$ CAD sur la maintenance prédictive). Les gains bruts et bris évités atteignent 16,74 M\$ CAD, soit 14,80 M\$ CAD de valeur nette créée et un ROI net de 7,6 fois la mise dès le premier exercice.
4.  **Transition sociale sans licenciement** : sur les 42 coordonnateurs autrefois absorbés par la ressaisie inter-systèmes, zéro suppression sèche d’emploi; après 120 heures de formation certifiante RH–IT, 24 sont devenus superviseurs d’exceptions HOTL, 11 curateurs d’ontologies et analystes qualité dans les cellules, et 7 conseillers grands comptes.
5.  **Feuille de route 2028–2030 approuvée par le conseil d’administration** : sur ce socle rentable et auditable, Boréal a voté trois chantiers pluriannuels prudents : l’adoption de l’identité vérifiable vLEI fin 2028 pour étendre les achats AP2 de BEL au fret routier nord-américain, la migration hybride post-quantique ML-DSA des archives septennales de BCA et un premier banc d’essai *Simplex* de chariots robotisés VLA dans l’entrepôt de Montréal-Est.
::::

------------------------------------------------------------------------

## 41.12 Décision d’architecture, transition vers l’entreprise étendue et points de contrôle

:::: {.encadre .adr}
::: {.encadre-titre}
**ADR-025 — Modèle Hub-and-Spoke, propriétaire métier nominatif et vigilance HOTL instrumentée**
:::

- **Statut** : Acceptée \| Périmètre : Entreprise & Ressources Humaines \| Révision : Annuelle
- **Contexte** : une fabrique multi-agents techniquement saine dérive rapidement si aucun cadre métier n’est imputable de ses résultats, si les mouvements RH créent des boucles orphelines, ou si la complaisance cognitive vide le contrôle humain de sa substance (OWASP ASI09).
- **Options évaluées** :
  1.  *Propriété exclusivement IT* : Rejetée — la DSI ne détient ni le budget d’affaires ni la légitimité d’arbitrage métier.
  2.  *Décentralisation intégrale dans les métiers* : Rejetée — fragmentation ontologique et non-conformité ISO/IEC 42001 / BSIF E-23.
  3.  *Fédération Hub-and-Spoke avec charte obligatoire de propriétaire métier nominatif couplée au SIRH et tests canaris continus sur les files HOTL*. Retenue.
- **Décision** : (a) séparer le centre d’excellence (socle, sécurité, ontologies, FinOps) des cellules métiers; (b) exiger pour tout agent L2–L4 un propriétaire métier nominatif actif, avec rétrogradation automatique sous 72 heures en cas de vacance dans le SIRH; (c) imposer sur toute file HOTL une vue différentielle, un plafond cognitif par quart et un taux d’interception des canaris $\ge 92\,\%$, à finalité non disciplinaire.
- **Conséquences** : imputabilité économique et réglementaire permanente et preuve empirique de l’effectivité du contrôle humain, en contrepartie d’une intégration SIRH–registre et d’un investissement soutenu en requalification interne.
::::

### Vers la partie IX

Une fois la fabrique interne en régime nominal, deux chantiers s’ouvrent en partie IX, après le plan de données d’inférence du chapitre 44. Le premier (chapitres 45 et 46) franchit les frontières de confiance légale, de juridiction infonuagique et de connectivité permanente : interconnecter les agents à ceux de centaines de partenaires B2B par des espaces de données régulés (Dataspace EDC / ODRL et identité vLEI) sans divulguer ni prix de réserve ni marges internes; protéger la souveraineté cognitive face aux lois extraterritoriales par des enclaves matérielles GPU TEE et la reprise après sinistre cognitif (Cognitive DR); opérer en coupure réseau totale sur des sites industriels distants ou robotisés (CRDT, pont ROS 2 sous enveloppe matérielle Simplex).

Le second (chapitre 47) applique la fabrique gouvernée au système d’information lui-même : décapsuler les cœurs patrimoniaux RPG/COBOL par une usine logicielle à séparation des devoirs (Agentic SDLC), protéger automatiquement les contrats de données et les SLO d’exploitation (Agentic DataOps et SRE autonome), et réduire trimestre après trimestre les coûts d’inférence par compilation déclarative et distillation continue LLM → SLM.

### Liste de contrôle de mise en production

1.  **Partage *Hub-and-Spoke*** : la matrice RACI entre le centre d’excellence et les cellules métiers fédérées est-elle formalisée et appliquée sans chevauchement ?
2.  **Couverture par un propriétaire métier nominatif** : chaque boucle active possède-t-elle un propriétaire métier nominatif portant son budget FinOps, ses SLI d’exactitude et son droit d’arrêt ?
3.  **Protection anti-orphelinat SIRH** : tout départ ou changement de poste dans le SIRH déclenche-t-il le transfert de tutelle sous 72 heures ou le repli automatique de l’agent en L2 ?
4.  **Ergonomie différentielle HOTL** : les consoles d’arbitrage affichent-elles les pièces sources et une contre-hypothèse critique plutôt qu’un texte persuasif généré par l’agent demandeur ?
5.  **Budget d’attention humaine** : le volume d’escalades complexes par superviseur et par quart respecte-t-il un plafond cognitif explicite évitant l’approbation réflexe ?
6.  **Tests canaris anti-ASI09** : un flux continu d’escalades synthétiques canaris vérifie-t-il l’attention effective des files HOTL dans un cadre transparent et non punitif ?
7.  **Pacte de requalification et relève** : le tandem RH–IT opère-t-il les parcours certifiants pour les coordonnateurs reconvertis ainsi que le simulateur d’entraînement des juniors ?
8.  **Préparation sans regret 2028–2030** : l’agilité cryptographique, l’externalisation des règles dans Cedar/OPA et l’isolation matérielle IT/OT préparent-elles le socle aux évolutions post-2027 ?
