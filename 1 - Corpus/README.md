# Le corpus agentique — synthèse consolidée des trois monographies

> **Auteur :** André-Guy Bruneau, M.Sc. IT — Juin–Juillet 2026
>
> Ce document est la **synthèse consolidée** des trois monographies du corpus. Il en articule les
> thèses, les concepts et les apports en un seul document de synthèse. Pour le détail, se reporter
> à chaque volume ; pour l'état de l'art le plus récent et la veille technologique, voir le
> [README du dépôt](../README.md).

---

## Vue d'ensemble

Le corpus réunit trois monographies conçues en progression — des protocoles à la réglementation,
puis à l'organisation — qui, ensemble, répondent à une question unique :

> **Comment une entreprise de services financiers peut-elle déployer, gouverner et exploiter des
> agents d'IA autonomes dans un écosystème réglementé, de manière sécurisée, traçable et
> pérenne ?**

Chaque volume éclaire une facette de cette question et porte sa propre thèse. Les trois thèses
sont complémentaires et forment un triptyque cohérent :

| | **Vol. I — Interopérabilité** | **Vol. II — Orchestration** | **Vol. III — Entreprise** |
|---|---|---|---|
| **Titre** | Interopérabilité agentique en entreprise dans le domaine des services financiers | L'autonomie encadrée | L'entreprise agentique — la fabrique de confiance |
| **Dossier** | [`1 - InteroperabiliteAgentique/`](1%20-%20InteroperabiliteAgentique/) | [`2 - OrchestrationAgentique/`](2%20-%20OrchestrationAgentique/) | [`3 - EntrepriseAgentique/`](3%20-%20EntrepriseAgentique/) |
| **Thèse** | *Autonomie graduée sous contrôle de finalité* | *Autonomie encadrée (framed autonomy)* | *La confiance ne se décrète pas, elle se fabrique* |
| **Portée** | Mondiale (UE, É.-U., R.-U., Asie) | Canada-Québec (cadre réglementaire) | Organisation et cycle de vie (NHI, AgentOps) |
| **Volumétrie** | **569 p.** (7 chapitres + Annexe B, ≈ 263 600 mots) | **387 p.** (29 pièces, 92 059 mots) | **427 p.** (34 pièces, ≈ 160 900 mots) |
| **Méthode** | Formalisme d'ingénierie (ArchiMate 4, ADS) | Socle factuel F-01…F-48, niveaux de preuve [A]/[B]/[C] | Double héritage codifié + socle propre (98 entrées) |
| **Gel** | Juin 2026 | 16–17 juillet 2026 | Hérite des deux gels + pièces propres |

---

## Le fil conducteur : du protocole à la confiance

```mermaid
graph LR
    A["Vol. I — Interopérabilité<br/><i>Découplage, contrat, évolution</i>"] --> B["Vol. II — Orchestration<br/><i>Cadre déterministe ⊃ agents</i>"]
    B --> C["Vol. III — Entreprise<br/><i>Identité = nouveau plan de contrôle</i>"]
    style A fill:#1a5276,color:#fff
    style B fill:#1e8449,color:#fff
    style C fill:#7d3c98,color:#fff
```

> [!NOTE]
> **Progression du corpus**
> - **Vol. I** pose les fondations théoriques et architecturales : comment les agents interopèrent (protocoles, sémantique, sécurité).
> - **Vol. II** instruit ce cadre au grain du droit canadien : comment les orchestrer sous contrainte réglementaire stricte.
> - **Vol. III** ferme la boucle : comment l'organisation fabrique, applique et exploite la confiance nécessaire à leur déploiement.

---

## Vol. I — Interopérabilité agentique en entreprise

📖 **Documents sources :** [`1 - InteroperabiliteAgentique/Monographie.pdf`](1%20-%20InteroperabiliteAgentique/Monographie.pdf) (**569 p.**) · [`Monographie.md`](1%20-%20InteroperabiliteAgentique/Monographie.md)

### Thèse

Les systèmes agentiques fondés sur les LLM ne rendent pas obsolètes les principes d'intégration
classiques : ils les **réinstancient à un niveau d'abstraction supérieur**. L'invariant
transversal — *découplage, contrat, évolution* — reste le socle de tout déploiement pérenne.
L'autonomie des agents doit être **graduée** et placée **sous contrôle de finalité** : l'agent
prépare, l'humain ou le processus déterministe autorise.

### Les sept chapitres en spirale

| # | Chapitre | Objet & Concepts clés |
|---|----------|-----------------------|
| 1 | **Théorie de l'interopérabilité des SI** | Fondements et intégration d'entreprise : SOA, microservices, messagerie événementielle, niveaux d'intégration conceptuels. |
| 2 | **Ingénierie des systèmes agentiques** | Agents fondés sur LLM : boucle ReAct, mémoire, invocation d'outils, taxonomie des modes d'échec (MAST). |
| 3 | **Protocoles d'interopérabilité agentique** | Convergence : MCP (outils), A2A (délégation pair-à-pair), ANP ; découverte dynamique, commerce inter-agents, identité, sécurité des frontières. |
| 4 | **Intégration à l'échelle de l'entreprise** | Déploiement : modernisation de l'héritage applicatif, identités non humaines (NHI), plan de contrôle de sécurité, gouvernance, maturité. |
| 5 | **Domaine financier & maillage réglementaire** | Cinq sous-domaines sous quatre « durcisseurs » : irréversibilité du règlement, risque systémique, risque-modèle, double qualification (tiers TIC + modèle). |
| 6 | **Blueprint ArchiMate** | Formalisation (ArchiMate 4) : patrons réutilisables (`<<Agent>>`, `<<MCP Server>>`), traçabilité verticale de l'intention métier aux couches logicielles. |
| 7 | **Prospective 2027-2032** | Chapitre *capstone* : tri épistémique (Programmé / Projeté / Spéculatif) ; échéancier 2027 ; fragmentation des normes ; migration post-quantique. |

### Architecture détaillée de solution (Annexe B)

L'Annexe B projette la monographie sur une entreprise fictive — la **Coopérative financière
Boréalis** — sous forme d'architecture de solution prête au déploiement, consolidée sur la pile **IBM**
(watsonx Orchestrate/Governance, API Connect + DataPower, Confluent, MQ, z/OS Connect, Sovereign Core).
Elle comprend **18 sections, 6 sous-annexes et 28 diagrammes Mermaid**, couvrant :
architecture logique et physique, contrats d'interface, sécurité, NFR/SLO, modèle opérationnel,
stratégie de test et plan de déploiement par plateaux.

### Apports distinctifs du Vol. I

- **Formalisme ArchiMate 4** appliqué à l'IA agentique — premier blueprint d'architecture
  d'entreprise complet pour les systèmes multi-agents en finance.
- **Principe d'autonomie graduée** : séparation structurelle entre la phase de préparation
  (agent probabiliste) et la phase d'engagement (processus déterministe).
- **Double qualification** sectorielle : l'agent doit figurer simultanément au registre des
  modèles (risque-modèle) et au registre des tiers TIC (résilience).
- **Taxonomie MAST** des modes d'échec des systèmes agentiques.

---

## Vol. II — L'autonomie encadrée

📖 **Documents sources :** [`2 - OrchestrationAgentique/Monographie.pdf`](2%20-%20OrchestrationAgentique/Monographie.pdf) (**387 p.**) · [`Monographie.md`](2%20-%20OrchestrationAgentique/Monographie.md)

### Thèse

Dans le secteur financier canadien, sous exigence réglementaire stricte, **le cadre déterministe
invoque les agents, jamais l'inverse**. L'agent est un exécutant encadré (*framed autonomy*) :
les processus soumis à la réglementation s'exécutent dans des workflows déterministes qui
orchestrent les agents, et non l'inverse — parce que le cadre est la seule pièce dont l'exploitant
puisse démontrer la teneur devant un tiers.

### Structure en sept parties

| Partie | Titre & Contenu | Chapitres |
|--------|-----------------|-----------|
| **I** | **Les protocoles d'interopérabilité agentique** — Consolidation en 17 mois (MCP, A2A, AP2, AGNTCY) ; complémentarité et identité d'agent. | Ch. 1-4, 8 |
| **II** | **La sécurité et la maîtrise des risques** — Taxonomie des risques, empoisonnement d'outils, injections d'invites. | Ch. 4-7 |
| **III** | **Le cadre réglementaire canadien** — E-23 (BSIF), AMF, Loi 25, ACVM ; applicabilité implicite à l'IA agentique. | Ch. 9-13 |
| **IV** | **L'interopérabilité financière canadienne** — Migration Lynx vers ISO 20022, RTR, interaction prospective avec AP2. | Ch. 14-16 |
| **V** | **L'adoption par les institutions financières** — Études de cas : TD (hypothécaire en <3 min), Scotiabank (AIDox), CIBC, Manuvie. | Ch. 17-20 |
| **VI** | **La frontière des connaissances** — Onze lacunes assumées et exposées. | Ch. 21 |
| **VII** | **Le blueprint d'intégration d'entreprise** — 6 principes directeurs, instanciation sur la pile IBM (watsonx, App Connect, API Connect, Confluent). | Ch. 22-24 |

> [!IMPORTANT]
> **Contribution la plus citable — un résultat négatif**
> En croisant **trois protocoles** (MCP, A2A, AP2) et **cinq corpus de textes canadiens**, **aucun lien documenté par source primaire** n'a été trouvé — quinze croisements, zéro lien. Ce résultat démontre que sous exigence réglementaire stricte, le cadre déterministe doit régir les agents.

### Rigueur méthodologique

- **Socle factuel** de 46 entrées (F-01 à F-48 ; F-12 à F-14 non attribués ; plus F-23b), cotées par niveau de preuve :
  **[A]** vote adversarial 3-0 > **[B]** source primaire extraite > **[C]** repérage.
- **Huit garde-fous** de formulation (R-1 à R-8).
- **Onze lacunes** exposées plutôt que comblées.
- **Grille de conformité** CA-1 à CA-8.

### Apports distinctifs du Vol. II

- **Résultat négatif systématique** (15 croisements protocoles × réglementation = 0 lien documenté), fondamental pour l'architecture réglementée.
- **Méthode de vérification adverse** à niveaux de preuve, transposables à d'autres domaines régulés.
- **Cas d'adoption réels** en institutions financières canadiennes (TD, Scotiabank, CIBC, Manuvie).
- **Options d'orchestration OO1–OO4** : taxonomie des modes d'intégration agents-processus (ABPM).

---

## Vol. III — L'entreprise agentique

📖 **Documents sources :** [`3 - EntrepriseAgentique/Monographie.pdf`](3%20-%20EntrepriseAgentique/Monographie.pdf) (**427 p.**) · [`Monographie.md`](3%20-%20EntrepriseAgentique/Monographie.md)

### Thèse

L'entreprise agentique — celle qui délègue des tâches engageant sa responsabilité à des agents
logiciels — doit se construire sur une **fondation identitaire**. L'identité non humaine est le
**nouveau plan de contrôle** (*identity as the new control plane*). La confiance ne se décrète pas :
elle se **fabrique** par trois capacités — *émettre* une identité opposable, l'*appliquer* au
maillage d'agents, l'*exploiter* dans la durée — sous l'horloge post-quantique.

### Structure en neuf parties

| Partie | Capacité | Objet & Contenu |
|--------|----------|-----------------|
| **I — L'héritage** | — | Évolution de l'identité machine depuis OAuth 2012, identité de charge de travail (SPIFFE/SPIRE), écart de gouvernance NHI. |
| **II — Émettre** | Identité | Le **passeport d'agent** : carte signée (A2A v1.0) + inscription au registre + chaîne de mandat + attestations de conformité. |
| **III — Délégation** | Mandat | Le « problème des deux sauts » : au-delà de deux sauts, aucun mécanisme actuel ne trace la délégation de bout en bout. |
| **IV — Menaces** | Défense | Menaces architecturales sur la chaîne d'identité ; absence de réduction de portée entre mandant et mandataire (MITRE ATLAS). |
| **V — Horloge PQ** | Cryptographie | Migration vers ML-KEM/ML-DSA (FIPS 203/204) ; crypto-agilité comme exigence de conception ; fenêtre critique 2026-2029. |
| **VI — Droit** | Conformité | E-23, AMF, Loi 25 : obligation implicite de registre d'agents et de traçabilité ; droit de révision humaine. |
| **VII — Appliquer** | Maillage | Le *maillage d'agents* (Agent Mesh) comme point d'application des politiques de sécurité. |
| **VIII — Exploiter** | AgentOps | Observabilité, évaluation continue, cycle de vie, réponse aux incidents. |
| **IX — Blueprint** | Organisation | Modèle de maturité (assistance → copilote → orchestration sous revue → autonomie bornée). |

### La fabrique de confiance — boucle continue

```mermaid
graph TD
    E1["É1 — Émettre<br/>Passeport d'agent<br/>(identité opposable)"] --> E2["É2 — Appliquer<br/>Agent Mesh<br/>(point d'application)"]
    E2 --> E3["É3 — Exploiter<br/>AgentOps<br/>(observabilité continue)"]
    E3 --> E1
    style E1 fill:#1a5276,color:#fff
    style E2 fill:#1e8449,color:#fff
    style E3 fill:#7d3c98,color:#fff
```

### Apports distinctifs du Vol. III

- **Le passeport d'agent** : objet de synthèse unifiant identité, mandat, conformité et enregistrement — concept original de la monographie.
- **Le problème des deux sauts** : démonstration que la délégation multi-saut actuelle perd sa traçabilité opposable au-delà du premier saut.
- **L'horloge post-quantique** comme contrainte de conception architecturale (et non comme problème futur), avec fenêtre d'action critique 2026-2029.
- **AgentOps** : formalisation des pratiques d'observabilité et de gestion du cycle de vie spécifiques aux agents.

---

## Les trois monographies en dialogue

### Convergence des thèses

Les trois thèses ne se contredisent pas : elles sont **trois coupes d'un même objet**.

| Dimension | Vol. I | Vol. II | Vol. III |
|-----------|--------|---------|----------|
| **Qui contrôle ?** | Le contrôle de finalité (humain ou processus déterministe) | Le cadre réglementaire (workflow déterministe) | L'identité vérifiable (passeport d'agent) |
| **Quel invariant ?** | Découplage, contrat, évolution | Cadre ⊃ agent (jamais l'inverse) | Émettre → Appliquer → Exploiter |
| **Quel horizon ?** | Architecture mondiale 2027-2032 | Échéancier réglementaire canadien (mai 2027) | Migration post-quantique 2030-2035 |

### Héritage et filiation

```mermaid
graph TD
    V1["Vol. I — Interopérabilité"] -->|"Théorie du découplage<br/>Anatomie des protocoles<br/>Sécurité agentique"| V2["Vol. II — Orchestration"]
    V1 -->|"Verrou identifié :<br/>identité NHI et<br/>délégation multi-saut"| V3["Vol. III — Entreprise"]
    V2 -->|"Questions ouvertes :<br/>valeur crypto des Agent Cards<br/>mécanique des attaques"| V3
    style V1 fill:#1a5276,color:#fff
    style V2 fill:#1e8449,color:#fff
    style V3 fill:#7d3c98,color:#fff
```

- **Vol. II présuppose Vol. I** pour la théorie du découplage, l'ingénierie des agents LLM et l'anatomie des protocoles.
- **Vol. I illustre mondialement** ce que **Vol. II instruit au grain du droit canadien**.
- **Vol. III prolonge les deux** sur leur verrou commun : l'identité non humaine et son exploitation.

---

## Protocoles et standards structurants

Les trois monographies convergent sur un socle commun de protocoles et standards :

### Protocoles agentiques

| Protocole | Rôle | Volumes |
|-----------|------|---------|
| **MCP** (Model Context Protocol) | Accès client-serveur aux outils et données (JSON-RPC 2.0) | I, II, III |
| **A2A** (Agent2Agent) | Délégation de tâches de pair à pair ; Agent Cards signées | I, II, III |
| **AP2** (Agent Payments Protocol) | Transactions financières agentiques | I, II |
| **ANP** (Agent Network Protocol) | Réseau d'agents décentralisé | I |
| **AGNTCY** | Couche d'infrastructure agentique | II |

### Standards d'identité et de sécurité

| Standard | Rôle | Volumes |
|----------|------|---------|
| **OAuth 2.0 / OIDC** | Autorisation et identité fédérée (RFC 6749, RFC 8693) | I, II, III |
| **SCIM 2.0** (RFC 7643) | Annuaire d'entreprise, extension pour profils d'agents | II, III |
| **SPIFFE / SPIRE** | Identité des charges de travail (CNCF) | I, III |
| **WIMSE** (IETF) | Identité en environnements multi-systèmes ; jetons de transaction | III |
| **VC / DID** (W3C) | Accréditations vérifiables, identité décentralisée | III |
| **FIPS 203 / 204** (NIST) | Cryptographie post-quantique (ML-KEM, ML-DSA) | I, III |

### Standards financiers et réglementaires

| Standard / Texte | Rôle | Volumes |
|------------------|------|---------|
| **ISO 20022** | Messagerie financière sémantique (Lynx, RTR) | I, II |
| **E-23** (BSIF) | Risque de modèle — entrée en vigueur 1er mai 2027 | I, II, III |
| **Loi 25** (Québec) | Renseignements personnels, droit de révision humaine | I, II, III |
| **AMF** (ligne directrice IA) | Encadrement sectoriel québécois | I, II, III |
| **DORA / AI Act** (UE) | Résilience opérationnelle et encadrement de l'IA | I |

---

## Concepts transversaux

Sept concepts traversent les trois monographies et forment le vocabulaire commun du corpus :

1. **Autonomie graduée / encadrée** — L'agent prépare, l'humain ou le processus déterministe autorise. L'autonomie n'est pas binaire : elle progresse par paliers de maturité vérifiables, de l'assistance au copilote puis à l'autonomie bornée.
2. **Découplage, contrat, évolution** — L'invariant architectural : les composants interagissent par contrat (et non par couplage direct), ce qui permet l'évolution indépendante de chaque partie.
3. **Identité non humaine (NHI)** — L'identité de l'agent est le nouveau plan de contrôle. Sans identité propre et gouvernée, le principe du moindre privilège est inapplicable.
4. **Passeport d'agent** — Objet de synthèse combinant carte signée, inscription au registre, chaîne de mandat et attestations de conformité — concept original du Vol. III.
5. **Maillage d'agents (Agent Mesh)** — Architecture d'intégration appliquant les politiques de sécurité à chaque interaction inter-agents ; le point d'application de l'identité.
6. **Crypto-agilité** — Capacité de remplacer rapidement les algorithmes cryptographiques, exigence de conception face à la fenêtre de migration post-quantique 2026-2035.
7. **Traçabilité de bout en bout** — Chaque action d'agent doit pouvoir être imputée, auditée et rejouée — exigence réglementaire (E-23, Loi 25) autant qu'architecturale.

---

## Recommandations consolidées

Les trois volumes convergent sur un ensemble de recommandations pratiques pour les institutions financières :

### Architecture et déploiement

- **Séparer préparation et engagement** : l'agent probabiliste prépare ; le processus déterministe engage. Aucun accès transactionnel non contraint pour les agents.
- **Gouverner le MCP** : imposer un *Control Plane* (passerelle d'API / AI Gateway) pour intercepter, valider et journaliser chaque action sortante des agents.
- **Encapsuler les agents dans des workflows stricts** (BPMN/BPEL) avec traçabilité intégrée pour respecter les exigences d'auditabilité.
- **Réutiliser les contrats existants** : les accès des agents aux systèmes *legacy* doivent se faire par les APIs et événements déjà en place.

### Identité et sécurité

- **Passer des identités statiques aux identités dynamiques** : remplacer les clés d'API par des identités avec mandat vérifiable et durée de vie bornée.
- **Superviser chaque arête du maillage** : les protocoles actuels perdent la trace au-delà du premier saut de délégation ; une supervision stricte est requise.
- **Intégrer des points d'arrêt humains auditables** sous forme d'actes de délégation signés cryptographiquement.
- **Concevoir pour la cryptographie post-quantique dès maintenant** : fenêtre d'action critique 2026-2029, jalons NIST 2030/2035.

### Conformité et gouvernance

- **Tenir un registre centralisé et vérifiable** des modèles et des agents — obligation implicite d'E-23 et de la Loi 25.
- **Démontrer l'anti-collusion** (*maker-checker*) dans l'architecture elle-même.
- **Exposer les lacunes plutôt que les combler** par des sources de moindre qualité — discipline méthodologique du corpus.
- **Adopter de manière incrémentale** selon des paliers de maturité vérifiables.

---

## Ordre de lecture

**Vol. I → Vol. II → Vol. III**, la [veille technologique](../Veille%20Technologique.md) servant d'entrée rapide ou de mise à jour.

| Profil du lecteur | Point d'entrée recommandé |
|---|---|
| **Pressé** | La [veille technologique](../Veille%20Technologique.md) (161 p., état de l'art le plus récent) |
| **Architecte / chercheur** | Vol. I, chapitre 1 — lecture séquentielle en spirale |
| **Praticien canadien** | Vol. II, chapitre 13 — « le pont : des contraintes réglementaires aux *frames* déterministes » |
| **RSSI / responsable identité** | Vol. III, Partie II — le passeport d'agent et la chaîne de mandat |
| **Décideur** | Ce README, puis la veille technologique |

---

## Volumétrie du corpus

| | Vol. I | Vol. II | Vol. III | **Total du corpus** |
|---|---|---|---|---|
| **Pages** | 569 | 387 | 427 | **1 383 p.** |
| **Mots** | ≈ 263 600 | 92 059 | ≈ 160 900 | **≈ 516 500 (> 500 000)** |
| **Pièces** | 7 chap. + Annexe B | 29 (24 chap. + annexes) | 34 (28 chap. + annexes) | **70 pièces rédigées** |
| **Socle factuel** | Vérification adverse | 46 entrées (F-01–F-48) | 98 entrées (F-01–F-98) + 33 héritées | **144 entrées codifiées (46 + 98)** |
| **Diagrammes** | 28 Mermaid | — | — | **28+ diagrammes** |

---

## Avertissements

> [!WARNING]
> - **Aucun avis juridique ni conseil d'investissement.** Ces ouvrages rapportent des textes et en proposent des lectures d'architecture qui engagent leur auteur seul.
> - **Aucune recommandation de fournisseur.** Les instanciations sur une pile d'éditeur (IBM notamment) sont des cas documentés, pas des verdicts comparatifs.
> - **Le domaine se périme par trimestres.** Chaque volume porte sa date de gel ; les échéances de revalidation sont suivies dans le [README du dépôt](../README.md).
> - **Assistance par agents.** Ces travaux ont été produits avec l'assistance de pipelines de recherche multi-agents ; la responsabilité éditoriale est celle de l'auteur.

---

## Structure du dossier

```
1 - Corpus/
├── README.md                                ← ce fichier (synthèse consolidée)
├── CLAUDE.md                                ← guide pour Claude Code dans ce dossier
├── 1 - InteroperabiliteAgentique/           Vol. I (569 p., ≈ 263 600 mots)
│   ├── Chapitres/                             7 chapitres + 7 bibliographies + Annexe B (ADS)
│   ├── Monographie.md / .pdf                  assemblage
│   └── build/                                 pipeline FESP (Mermaid → Pandoc → Typst)
├── 2 - OrchestrationAgentique/              Vol. II (387 p., 92 059 mots)
│   ├── monographie/                           29 pièces (parties I-VII, annexes, registre des gels)
│   ├── prd/                                   PRD, PRDPlan, TOC, audit — gouvernance
│   ├── verification/                          revalidations et grille de conformité
│   ├── build/                                 assemblage + pipeline Pandoc → Typst
│   └── Monographie.md / .pdf                  assemblage
└── 3 - EntrepriseAgentique/                 Vol. III (427 p., ≈ 160 900 mots)
    ├── README.md                              présentation du volume (déposée le 29 juill. 2026)
    ├── CLAUDE.md                              conventions du volume
    ├── monographie/                           34 pièces rédigées + registre des gels
    ├── prd/                                   PRD v1.3, TOC v0.8, PRDPlan v0.5 — gouvernance
    ├── verification/                          30 rapports de vérification
    ├── build/                                 pipeline FESP
    └── Monographie.md / .pdf                  assemblage
```

---

## Décomptes du dépôt final

☑ **Toute la volumétrie de ce document a été re-mesurée sur pièce le 29 juillet 2026**, à la passe de
dépôt final, et elle est **inchangée** : les trois paginations (`pypdf`), les 29 et 34 pièces des
Vol. II et III, les 28 diagrammes du Vol. I (motif ancré) et le total du corpus — **1 383 p. /
≈ 516 500 mots / 70 pièces / 144 entrées de socle codifiées**. ⚠ **Une re-mesure qui confirme ne change
aucun état** : le Vol. III demeure **rédigé et non publiable**.

⚠ **Ce document ne couvre pas le Vol. IV**, et c'est délibéré : la synthèse porte sur le **triptyque**.
Le compendium — *La somme agentique*, **arrêté en révision finale le 29 juillet 2026, 810 p., non
publiable** — se situe au [README du dépôt](../README.md) et vit sous
[`2 - Compendium/`](../2%20-%20Compendium/). **Il ne se substitue pas à ces trois volumes tant qu'il
n'est pas recevable, et il ne l'est pas** : les trois volumes sources font foi.

---

*Synthèse consolidée — juillet 2026 · décomptes re-mesurés au dépôt final du 29 juillet 2026*
