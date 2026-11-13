# Annexe F — Décisions d'architecture (ADR) et arbres de choix

Cette annexe réunit les outils des arbitrages courants des comités d’architecture d’entreprise et des ingénieurs principaux : le registre des trente et une décisions d’architecture (ADR-001 à ADR-031) établies dans les volets « Mise en œuvre »; deux arbres de décision, pour trancher les choix de protocole et d’autonomie; un gabarit de fiche ADR adapté aux systèmes probabilistes.

## F.1 Récapitulatif des 31 décisions d’architecture (ADR-001 à ADR-031)

Chaque volet « Mise en œuvre » établit un invariant d’architecture à respecter pour passer à l’échelle. Les 31 fiches ont le statut Acceptée; les fiches ADR-017 et ADR-029 l’assortissent d’une réserve. Le tableau sert d’index : le centre d’excellence agentique peut l’adopter comme socle de la gouvernance interne.

| Code | Chap. | Intitulé normatif de la décision | Invariant technique imposé |
|:----------|:----------|:------------------------------------------|:-------------------------------------|
| **ADR-001** | 1 | Superposition d’un *System of Action* découplé et séparation stricte MCP / A2A | Aucune écriture SQL directe contournant les systèmes d’enregistrement; `ActionEnvelope` obligatoire |
| **ADR-002** | 17 | Interdiction du routage global de processus critiques par inférence LLM non bornée | Le séquencement maître réside dans du code ou une machine à états déterministe |
| **ADR-003** | 43 | Adoption d’un portail d’homologation gradué par niveau de maturité et d’exposition | Recensement obligatoire et blocage réseau des *Shadow Agents* non enregistrés |
| **ADR-004** | 11 | Alignement normatif sur la pile Linux Foundation AAIF et gouvernance anti-verrouillage | Priorité aux standards neutres (MCP, A2A v1.0, Agent Skills, Open Responses) |
| **ADR-005** | 5 | Standardisation de l’exposition d’outils métiers sur MCP Streamable HTTP orienté domaine, Agent Skills et WebMCP | Au plus 15 outils par serveur, orientés intention métier; refus du mappage CRUD 1:1 |
| **ADR-006** | 6 | Utilisation d’A2A v1.0 et d’Agent Cards signées pour toute délégation inter-domaines | Découverte dynamique OASF et transport chiffré SLIM/MLS entre domaines distincts |
| **ADR-007** | 10 | Découplage déclaratif des interfaces génératives via AG-UI et A2UI | Aucun code HTML/JS arbitraire généré par un LLM n’est exécuté sans catalogue déclaratif borné |
| **ADR-008** | 13 | Compilation déterministe du contexte, filtrage ACL pré-récupération et transfert par référence | Filtrage obligatoire selon les ACL et interdiction de relayer l’historique brut intégral |
| **ADR-009** | 12 | Adoption d’Apache Ossie pour la sémantique analytique et d’une ontologie causale versionnée pour les actions | Toute métrique ou règle d’éligibilité passe par la couche sémantique normalisée |
| **ADR-010** | 14 | Architecture de mémoire hybride (Letta + Graphiti bi-temporel), garde anti-ASI06 et effacement crypto-sélectif | Double horodatage `valid_from`/`valid_to` et capacité de purge vérifiable (Loi 25) |
| **ADR-011** | 16 | Standardisation des topologies multi-agents et interdiction des graphes cycliques non bornés | Interdiction des essaims conversationnels libres sur des flux soumis à audit |
| **ADR-012** | 18 | Architecture bi-vitesse d’exécution durable (Temporal + Restate) et revalidation obligatoire post-hibernation | Journalisation déterministe, clés d’idempotence et revalidation au réveil (`awakeable`) |
| **ADR-013** | 19 | Maillage événementiel hybride Kafka/Solace et patron Saga à compensation sans 2PC | Toute mutation possède son inverse compensatoire ou un tampon à fenêtre de grâce |
| **ADR-014** | 44 | Imposition d’agentgateway comme plan de données unique, routage hybride à 3 paliers et affinité de KV-cache | SLM là où une règle explicite l’établit, palier supérieur pour toute classe inconnue; affinité de préfixe du KV-cache activée |
| **ADR-015** | 27 | Ancrage des agents spécialistes selon la gravité des données et fédération par plan de contrôle neutre | Les agents SaaS opèrent sur leurs objets natifs et coopèrent par un en-tête anti-boucle |
| **ADR-016** | 25 | Doctrine d’usage restreint des *Computer-Use Agents* en dernier recours sous double validation | Vérification visuelle avant et après l’action; migration programmée vers un connecteur MCP |
| **ADR-017** | 28 | Architecture en sas par Jumeau numérique et validation déterministe pour toute consigne IT→OT | Aucune écriture directe d’un modèle probabiliste vers un automate PLC/SCADA |
| **ADR-018** | 30 | Identité NHI unique par classe d’agent et échange de jetons RFC 8693 à portée atténuée à chaque saut | Atténuation stricte de portée (`sub`/`act`) et approbation CIBA sur seuil critique |
| **ADR-019** | 31 | Modélisation de menaces ASI01–ASI10 obligatoire et épinglage cryptographique des schémas MCP | Signature SHA-256/Sigstore des schémas d’outils contre les attaques *Rug-Pull* |
| **ADR-020** | 32 | Découplage systématique des garde-fous déterministes (Cedar/OPA) et exécution en microVM isolée | Exécution de code sans sortie réseau implicite et coupe-circuit SOC testé |
| **ADR-021** | 33 | Standardisation sur OpenTelemetry GenAI et collecte souveraine à double couloir PII | Traces distribuées obligatoires avec caviardage PII en amont de l’export |
| **ADR-022** | 34 | Cycle ADLC gouverné par SemVer+Intent, portes de constance $\text{pass}^5$ et déploiement Canary | Homologation sur bancs d’essai de type $\tau$-bench et injection de pannes avant trafic réel |
| **ADR-023** | 40 | Pilotage FinOps par le *Cost-per-Outcome*, disjoncteurs par saga et refacturation interne | Disjoncteur financier en temps réel et mise hors service des agents à ROI négatif |
| **ADR-024** | 38 | Qualification réglementaire dynamique par empreinte de déploiement et mandats B2B bornés | Alignement croisé ISO/IEC 42001, BSIF E-23 (mai 2027), Loi 25 et EU AI Act |
| **ADR-025** | 41 | Modèle *Hub-and-Spoke*, propriétaire métier nominatif et vigilance HOTL instrumentée | Responsabilité humaine explicite et contrôle anti-complaisance cognitive HOTL |
| **ADR-026** | 45 | Maillage B2B fédéré sous connecteurs Dataspace (EDC/ODRL), isolation du diplomate et règlement tripartite déterministe | Identité vLEI, séparation Diplomate/Évaluateur et rapprochement à trois voies hors LLM |
| **ADR-027** | 46 | Géorepérage de l’état complet, inférence confidentielle HYOK/TEE et reprise après sinistre cognitif bimodèle | Résidence juridictionnelle des 6 substrats d’état et bascule en `< 15 min` vers des modèles à poids ouverts |
| **ADR-028** | 46 | Architecture Edge *Local-First* à synchronisation CRDT et pont robotique ROS 2 sous enveloppe matérielle Simplex | Autonomie hors ligne de 72 h, quotas d’escrow CRDT et moniteur matériel IEC 61508 |
| **ADR-029** | 47 | Pipeline Agentic SDLC à séparation des devoirs et modernisation patrimoniale par oracle *Golden Master* et *Shadow Mirroring* | Aucune auto-approbation, score de mutation $\ge 85\,\%$ et parité de 30 jours sans écart |
| **ADR-030** | 47 | Contrats de données *Write-Audit-Publish* (ODCS) et SRE autonome à séparation stricte diagnostic lecture seule / runbooks Cedar | Quarantaine WAP avant exposition aval et aucun shell libre en production |
| **ADR-031** | 47 | Compilation déclarative des consignes et volant de distillation continue LLM → SLM sous sas anti-PII et porte $\text{pass}^5$ | Désidentification irréversible Loi 25, parité $\text{pass}^5 \ge 99\,\%$ et sentinelle 2 % |

------------------------------------------------------------------------

## F.2 Arbre de décision : choix du protocole d’interopérabilité

Pour un nouveau service ou flux métier, la question la plus fréquente soumise aux architectes est de choisir entre MCP, A2A v1.0, un courtier d’événements (Kafka / Solace), AG-UI/A2UI ou un *Computer-Use Agent* (CUA). L’arbre ci-dessous donne, dans l’ordre, les questions qui permettent de trancher.

![Arbre de décision normatif pour le choix du protocole d’interopérabilité selon la nature du destinataire et le couplage requis.](figures/fig-f-1.svg)

### Cas limites et règles de départage

1.  **Système externe qui expose déjà un agent propriétaire (Salesforce Agentforce, SAP Joule).** N’encapsulez pas cet agent derrière un outil MCP synchrone si la tâche dure plusieurs secondes ou déclenche des sous-étapes autonomes. Utilisez A2A v1.0 pour préserver l’état asynchrone (`WORKING`, `INPUT_REQUIRED`, `COMPLETED`), la négociation de sécurité et la trace distribuée.
2.  **Plusieurs consommateurs indépendants réagissant au même fait métier.** N’enchaînez pas des appels A2A séquentiels lorsqu’un événement (clôture d’intervention, alerte machine) concerne à la fois la facturation, l’analytique, le CRM et la maintenance. Publiez un événement typé sur Kafka ou Solace, conforme à Apache Ossie; chaque domaine abonné instancie localement sa saga.
3.  **Transaction qui engage une dépense auprès d’un tiers externe.** A2A porte le dialogue de négociation, mais il ne constitue ni une preuve d’autorisation financière ni un contrat d’usage des données partagées. Encadrez le canal par un connecteur EDC (W3C ODRL 2.2 + identité légale vLEI) et liez l’engagement à un mandat cryptographique vérifiable AP2 (plafond, devise, catégorie marchande, expiration) ou, pour les API facturées à la requête, au règlement x402 sur trésorerie plafonnée.
4.  **Action visant un automate d’usine ou un robot mobile en périphérie (IT/OT).** Interdisez toute publication directe d’un modèle sur un registre PLC ou sur un topique moteur ROS 2/DDS. Interposez toujours une passerelle MCP de missions discrètes, validée par un jumeau numérique ou par un arbitre matériel Simplex (`ISO 10218-1:2025` / IEC 61508).

------------------------------------------------------------------------

## F.3 Arbre de décision : choix entre code déterministe, workflow et boucle agentique

Une erreur d’architecture fréquente, observée en 2025–2026, consiste à appeler un grand modèle de langage, coûteux et lent, pour exécuter une logique conditionnelle déterministe. À l’opposé, coder en dur mille embranchements `if/else` pour traiter des courriels litigieux multilingues crée une lourde dette de maintenance. L’arbre suivant applique une règle de parcimonie cognitive : employer le niveau d’inférence minimal que l’entropie réelle du problème exige.

![Arbre de décision normatif arbitrant entre service déterministe L0, workflow enrichi par SLM, automatisation HITL L2 et orchestration multi-agents L3/L4.](figures/fig-f-2.svg)

------------------------------------------------------------------------

## F.4 Gabarit de fiche ADR pour système agentique

À la différence d’une fiche ADR logicielle classique, la fiche d’une décision touchant un composant agentique doit documenter explicitement son plafond d’autonomie, son enveloppe économique et son mécanisme de repli déterministe. Le gabarit YAML/Markdown ci-dessous se versionne avec le code, dans le dépôt du projet :

``` yaml
adr_id: "ADR-XXXX"
title: "Intitulé court et prescriptif de la décision"
status: "Proposed | Accepted | Deprecated | Superseded"
date: "2027-01-15"
owners:
  architecture_lead: "prenom.nom@entreprise.ca"
  named_business_owner: "prenom.nom@entreprise.ca"
risk_and_autonomy:
  autonomy_ceiling: "L0 | L1 | L2 | L3 | L4"
  regulatory_footprint:
    bsif_e23_materiality: "Low | Moderate | High"
    quebec_law25_automated_decision: false
    eu_ai_act_tier: "Minimal | Art50 | HighRisk_AnnexIII"
  owasp_asi_mitigated: ["ASI01", "ASI02", "ASI03", "ASI08"]
technical_invariants:
  vertical_protocol: "MCP Streamable HTTP (pinned SHA-256)"
  horizontal_protocol: "A2A v1.0 via agentgateway"
  durable_runtime: "Temporal | Restate | None (stateless L1)"
  compensation_strategy: "Saga inverse | Lease | Buffer"
  max_cost_per_outcome_cad: 0.75
  minimum_eval_gate: "pass^5 >= 0.96 on domain simulation suite"
fallback_and_killswitch:
  degraded_mode: "Route vers file manuelle ServiceNow"
  soc_killswitch_id: "ks-domain-workflow-04"
review_trigger: "Semestrielle ou changement majeur modèle/outil"
```

Si toutes les fiches suivent ce descripteur, le pipeline CI/CD (chapitre 34) peut bloquer automatiquement tout déploiement dont le plafond financier, le coupe-circuit SOC ou le propriétaire métier nominatif n’est pas renseigné et signé.
