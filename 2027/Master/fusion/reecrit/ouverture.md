# Ouverture — Architecture et gouvernance du tissu conjonctif agentique

:::: {.encadre .executive}
::: {.encadre-titre}
**Portée de l'ouverture**
:::

- **Point de départ.** L’ouvrage soutient qu’en 2027 la performance d’une entreprise agentique tient moins à la supériorité d’un grand modèle de langage pris isolément qu’à la robustesse du tissu conjonctif qui relie ses agents spécialisés, ses progiciels patrimoniaux, ses partenaires B2B, ses équipements physiques et ses superviseurs humains. C’est un argument, non un constat : la section 1.5 le tient pour nécessaire par raisonnement, sans qu’aucune mesure le démontre.
- **Thèse architecturale.** Industrialiser l’autonomie exige de conjuguer deux disciplines complémentaires : une interopérabilité ouverte en six couches (connectivité aux outils et aux ateliers, sémantique et mémoire métier, coordination entre pairs, orchestration durable, interaction humain-agent, gouvernance et transactions B2B), et une orchestration hybride qui place des cellules de raisonnement probabiliste à l’intérieur de plans de contrôle déterministes, souverains et auditables.
- **Usage de l’ouvrage.** L’ouverture établit l’architecture de référence du compendium, propose six parcours de lecture par fonction dirigeante ou technique, fixe l’échelle des niveaux d’autonomie (L0 à L4) et pose le dossier initial de l’entreprise fil rouge (Groupe Boréal Inc.), suivie dans les volets « Mise en œuvre ». <!-- ajout partie X -->La partie X confronte l’ouvrage à la recherche publiée, à la veille technologique et au marché (chapitres 48 à 50).<!-- fin ajout -->
::::

## 0.1 Pourquoi ce compendium en 2027

De 2023 à 2025, la première vague d’adoption de l’IA générative en entreprise a pris la forme de l’assistant conversationnel synchrone : clavardoir interne branché sur une base documentaire par génération augmentée par récupération (RAG), ou copilote intégré à une suite bureautique. L’humain y restait le seul point d’intégration du système d’information. Lorsqu’un copilote résumait un contrat, suggérait une requête SQL ou rédigeait un avis d’incident, une personne lisait la proposition, en jugeait la cohérence métier, puis saisissait elle-même la décision dans l’ERP, le CRM ou le système de gestion des services TI.

En 2026, une partie des organisations a commencé à passer de la génération de texte à l’exécution d’actions, en quête de gains mesurables sur des processus de bout en bout. Un agent planifie des séquences en plusieurs étapes, invoque des outils externes, délègue des sous-mandats à d’autres agents spécialisés, conserve un état et écrit directement dans les systèmes d’enregistrement (section 1.1). Le passage est réel, mais inégal. Selon l’enquête déclarative McKinsey de 2026, connue par un compte rendu de presse, 40 % des organisations d’au moins 1 G\$ US de revenus ont mis des agents à l’échelle dans au moins une fonction, contre 27 % un an plus tôt, et 22 % des plus petites (section 4.1). Les agents qui atteignent la production restent étroits : selon l’étude MAP, dont la collecte date de 2025, 68 % exécutent moins de dix étapes avant une intervention humaine et 16 cas sur 20 suivent un workflow structuré et prédéfini (section 4.2).

Ce qui sépare le pilote de la production n’est pas d’abord la capacité du modèle de langage, mais la fiabilité, l’évaluation et les contrôles (chapitre 4). Trois phénomènes font de l’interopérabilité et de l’orchestration la préoccupation des architectes et des directions technologiques :

1. **Des îlots d’agents incompatibles.** Chaque grand éditeur de progiciels d’entreprise a doté sa plateforme de son propre moteur d’agents : Salesforce Agentforce pour la relation client, ServiceNow AI Agents pour les flux opérationnels et TI, SAP Joule pour les ressources d’entreprise et la chaîne d’approvisionnement, Microsoft Copilot Studio pour l’environnement collaboratif, Workday Illuminate pour le capital humain. Les équipes d’ingénierie internes bâtissent en parallèle des agents sur mesure sur des cadriciels variés. Sans couche d’interopérabilité normalisée, l’entreprise remplace ses silos applicatifs par des silos d’agents, incapables de se transmettre un contexte fiable, une identité vérifiable ou une transaction compensable.
2. **Des standards ouverts en voie de consolidation.** Ce qui n’était fin 2024 qu’une mosaïque de propositions propriétaires concurrentes s’est organisé, à compter de décembre 2025 et tout au long de 2026, autour de l’Agentic AI Foundation (AAIF) de la Linux Foundation, foyer neutre pour des projets à code ouvert, aux côtés du projet AGNTCY, de l’Apache Software Foundation, du W3C, de l’IETF et de la FIDO Alliance. L’AAIF compte huit membres platine et, selon un décompte approximatif de logos, une cinquantaine de membres or et environ deux cents membres argent, soit quelque 260 organisations (section 11.2). Les rôles se séparent nettement à la couche des protocoles : connectivité verticale aux outils et aux données (Model Context Protocol, MCP), coordination horizontale entre agents pairs (Agent2Agent, A2A v1.0, dans lequel s’est fondu ACP), partage sémantique métier (Apache Ossie), plan de données (agentgateway), autorisation transactionnelle (AP2, x402). La convergence ne va pas plus loin : elle est absente à la couche de l’identité, où s’opposent trois modèles de confiance (sections 11.7 et 11.8), et ce qui entoure le socle MCP et A2A reste en chantier (section 4.4).
3. **Des échéances réglementaires et fiduciaires échelonnées.** Elles s’étalent de 2026 à 2028. Au Canada, la ligne directrice E-23 révisée du Bureau du surintendant des institutions financières (BSIF / OSFI) sur la gestion du risque de modèle entre en vigueur le 1er mai 2027 et assujettit expressément les systèmes d’IA générative et agentique à un inventaire exhaustif, à une cotation de matérialité et à la validation du cycle de vie. Au Québec, la Loi 25, en vigueur, encadre les décisions exclusivement automatisées (article 12.1), les évaluations des facteurs relatifs à la vie privée (ÉFVP) et les transferts transfrontaliers de renseignements personnels, sous peine de sanctions atteignant 25 M\$ CAD ou 4 % du chiffre d’affaires mondial. En Europe, les obligations de transparence de l’article 50 sont actives depuis août 2026. Le règlement (UE) 2026/1744, dit Digital Omnibus sur l’IA, a reculé le calendrier de l’EU AI Act : les obligations visant les systèmes à haut risque de l’annexe III s’appliquent à compter du 2 décembre 2027, celles de l’annexe I à compter du 2 août 2028 (section 4.4). Ce report donne du temps, non une dispense. La norme ISO/IEC 42001 sert de référentiel certifiable de gouvernance dans les appels d’offres B2B.

Le compendium pose un postulat d’ingénierie : les modèles fondationnels doivent être traités comme des composants remplaçables, à obsolescence rapide, alors que l’architecture d’interopérabilité, d’orchestration, de sémantique et de sécurité forme l’infrastructure durable de l’entreprise agentique. C’est une posture, non l’état de la pratique : 17 cas sur 20 de l’étude MAP dépendent d’un modèle propriétaire, et la perte d’un fournisseur de modèles se prépare (section 4.2).

![Architecture de référence à 6 couches et 2 piliers transversaux de l’entreprise agentique en 2027.](figures/fig-00-1.svg)

La figure synthétise le modèle de référence de l’ouvrage. L’architecture décompose le système en six couches horizontales composables, traversées par deux piliers : à gauche, le contrôle d’identité non humaine (NHI) et la sécurité à confiance zéro; à droite, l’observabilité distribuée (OpenTelemetry `gen_ai.*`), le génie logiciel probabiliste (AgentOps) et la gouvernance économique (FinOps).

------------------------------------------------------------------------

## 0.2 Enjeux économiques et opérationnels de 2027

Les analyses publiées par les grands cabinets d’évaluation technologique au seuil de 2027 relèvent un paradoxe : plus les agents individuels gagnent en spécialisation et en autonomie locale, plus le système d’ensemble devient vulnérable au désordre de coordination. Forrester le résume en qualifiant 2027 d’ère de *« la poursuite et du péril du contrôle »* (*The Pursuit and Peril of Control*), et Gartner met en garde contre la dérive des coûts variables.

Trois risques structurels guettent tout programme qui aborde l’orchestration multi-agents avec les habitudes du développement web traditionnel ou des premiers prototypes LLM :

- **La baisse de la fiabilité par composition probabiliste (loi de Lusser).** Si un agent autonome réussit une étape complexe avec une exactitude de 94 %, une chaîne séquentielle non encadrée de dix délégations indépendantes voit sa probabilité de succès sans erreur tomber à $R = 0{,}94^{10} \approx 53{,}9\,\%$. Un microservice classique échoue de façon visible, par une exception HTTP 500; un maillon LLM défaillant produit souvent une rationalisation plausible qui se propage sans signal d’erreur aux agents en aval (OWASP ASI08 — *Cascading Failures*). Les erreurs se composent d’une étape à l’autre (section 1.1). La fiabilité d’entreprise demande donc de sortir de l’invite le routage critique, les invariants d’affaires et la gestion d’état, pour les confier à une épine dorsale déterministe et durable.
- **Les limites d’une interopérabilité purement syntaxique.** Normaliser le format d’échange par JSON-RPC (MCP) ou par descripteurs de tâches (A2A) règle la transmission des messages, non leur sens. Lorsqu’un agent commercial interroge un agent financier sur le « taux d’attrition trimestriel » ou sur l’« exposition nette d’un client », l’absence d’une couche sémantique partagée (Apache Ossie) et d’une ontologie causale d’entreprise produit des décisions incohérentes mais syntaxiquement valides. L’interopérabilité réelle ne se sépare pas de l’ingénierie du contexte ni de la gouvernance de la mémoire. Aucun protocole n’exprime non plus l’approbation, l’escalade ou l’audit d’une décision : cette couche revient à l’entreprise (section 11.9).
- **L’asymétrie économique et sécuritaire des boucles autonomes.** Une requête humaine mal formulée coûte quelques centimes. Une boucle de réessai mutuelle entre deux agents mal orchestrés, qui consomme du calcul d’inférence réflexif pendant une fin de semaine, peut coûter des dizaines de milliers de dollars et saturer les quotas d’API d’un système ERP critique. De même, donner à un agent tous les privilèges de l’utilisateur qui l’invoque transforme toute injection indirecte d’instructions, dissimulée dans un courriel ou un document externe, en voie d’exfiltration de données.

Le tableau suivant récapitule les sept ruptures architecturales qui séparent les pratiques héritées des prototypes 2024–2025 des cibles de production 2027 détaillées dans ce compendium. Ces cibles ne décrivent pas l’état général de la pratique : les agents en production restent étroits (section 4.2), et aucun cas documenté ne montre MCP, A2A ou un système multi-agents en production (section 1.5, chapitre 42).

| Axe d’architecture | Pratique prototype héritée (2024–2025) | Cible de production d’entreprise (2027) | Parties de référence |
|:------------------|:------------------------------|:-----------------------------------|:---------------|
| **Modèle d’interaction** | Clavardage synchrone, déclenché et validé à la main par l’utilisateur | Exécution asynchrone pilotée par événements, supervisée par un humain sur la boucle (HOTL) | Parties I et IV |
| **Intégration aux outils et aux pairs** | Connecteurs REST ad hoc codés en dur par cadriciel, invites collées | Pile ouverte à deux couches : MCP + Agent Skills (vertical) et A2A v1.0 + AGNTCY (horizontal) | Partie II |
| **Contexte et mémoire** | RAG vectoriel plat sur documents bruts; historique de conversation tronqué | Ingénierie du contexte, sémantique Apache Ossie, ontologies et graphes bi-temporels (Graphiti) | Partie III |
| **Contrôle de flux et état** | Le LLM décide seul de l’enchaînement, en mémoire vive volatile | Épine dorsale durable (Temporal, Restate), maillage Kafka/Solace et compensations Saga | Partie IV |
| **Patrimoine SaaS, systèmes patrimoniaux et OT** | Agents captifs d’un seul éditeur; systèmes sans API et ateliers ignorés | Gravité des données, plan de contrôle fédéré, CUA confinés et sas OPC UA / jumeau numérique | Parties V et IX |
| **Identité et sécurité** | Clés d’API statiques partagées ou jeton brut de l’utilisateur humain | Identités NHI (SPIFFE/DID), OAuth 2.1 OBO (RFC 8693), OpenSandbox et politiques Cedar/OPA | Parties VI et IX |
| **Opérations, coûts et conformité** | Journaux texte locaux, tests manuels sur 10 exemples, budget infonuagique global | Traces OpenTelemetry `gen_ai.*`, simulation $\tau$-bench ($\text{pass}^k$), coût par résultat, ISO 42001 / E-23 | Parties VI à IX |

------------------------------------------------------------------------

## 0.3 Parcours de lecture par rôle

Un ouvrage qui couvre aussi bien l’échange de jetons (RFC 8693) que la modélisation ontologique, les espaces de données B2B ou la distillation de modèles ne se lit pas forcément du premier au dernier chapitre. L’ordre des neuf premières parties suit une progression logique, des fondations conceptuelles jusqu’à l’écosystème fédéré et l’auto-amélioration gouvernée. <!-- ajout partie X -->La dixième, « Recherche scientifique », se lit à part : elle dit ce que la recherche a mesuré, ce qu’il faut surveiller et ce que vaut le marché.<!-- fin ajout --> Six parcours prioritaires répondent toutefois aux mandats immédiats des décideurs et des spécialistes.

### 1. Parcours CTO / CIO (direction technologique et stratégie de plateforme)

- **Question directrice.** *Comment éviter la fragmentation de notre SI en dix plateformes d’agents concurrentes tout en maîtrisant la souveraineté, le TCO et la rapidité de livraison ?*
- **Séquence prioritaire.** Chapitres 1, 17 et 43 (vision cible, découplage contrôle/autonomie, modèle de maturité N1–N5) → chapitre 11 (gouvernance AAIF et stratégie anti-verrouillage) → chapitre 44 (passerelles natives de l’IA et routage hybride SLM/LLM) → chapitre 27 (fédération des jardins clos SaaS) → chapitres 40 et 41 (FinOps du coût par résultat et modèle *Hub-and-Spoke*) → chapitres 46 et 47 (souveraineté / Cognitive DR, usine Agentic SDLC et distillation LLM → SLM). <!-- ajout partie X -->Pour l’horizon : chapitre 50 (étude de marché et projection de 2027 à 2030).<!-- fin ajout -->
- **Livrables directement réutilisables.** Grille d’audit de maturité, politique d’allocation budgétaire par résultat métier et fiches ADR-001, ADR-004, ADR-015, ADR-023, ADR-027 et ADR-031.

### 2. Parcours architecte d’entreprise et architecte de solutions principales

- **Question directrice.** *Quels patrons de communication, de gestion d’état et d’intégrité transactionnelle garantissent la résilience de flux multi-agents qui traversent des systèmes hétérogènes et des frontières B2B ?*
- **Séquence prioritaire.** Lecture intégrale des parties I, II, IV, V et IX, complétée par les chapitres 12 et 47 (Apache Ossie, modernisation *Strangler Fig*) et l’annexe F (arbres de décision architecturale). <!-- ajout partie X -->Pour l’état de la preuve : chapitre 48 (ce que la recherche a mesuré, ce qu’elle débat, ce qui lui manque).<!-- fin ajout -->
- **Point d’attention particulier.** Les chapitres 18, 19, 45 et 46 sur l’articulation entre moteurs d’exécution durable (Temporal, Restate), sagas événementielles, maillages B2B EDC et cellules de périphérie déconnectées à synchronisation CRDT.

### 3. Parcours CISO, architecte IAM et responsable cybersécurité

- **Question directrice.** *Comment gouverner des milliers d’identités non humaines dynamiques, prévenir l’empoisonnement d’outils MCP, protéger les secrets B2B et conserver un coupe-circuit instantané ?*
- **Séquence prioritaire.** Chapitre 17 (bornes déterministes) → chapitres 5 et 6 (MCP, A2A et SLIM/MLS) → lecture approfondie des chapitres 29 à 32 → chapitres 45 et 46 (*Clean Rooms*, vLEI, enclaves GPU TEE et clés HYOK) → annexe G (grilles G.1 et G.5). <!-- ajout partie X -->Pour la veille : chapitre 49 (vulnérabilités des serveurs MCP, composition des défenses entre agents, échéance post-quantique). Pour la mesure : sections 8.8 (écosystème réel des serveurs MCP) et 24.5 (premières mesures de passerelles).<!-- fin ajout -->
- **Livrables directement réutilisables.** Architecture d’échange de jetons OAuth 2.1 OBO à portée atténuée, matrice de couverture OWASP ASI01–ASI10, politique d’épinglage cryptographique des serveurs MCP et patron d’isolation en microVM / enclave TEE.

### 4. Parcours responsable plateforme, SRE Agentique et ingénieur AgentOps

- **Question directrice.** *Comment instrumenter, tester avant déploiement, simuler sous chaos, réparer et distiller en continu des systèmes dont le comportement n’est pas déterministe ?*
- **Séquence prioritaire.** Chapitres 18 et 44 (moteurs d’exécution durable, agentgateway, ordonnancement KV-cache) → chapitre 32 (OpenSandbox, politiques en ligne) → chapitres 33, 34 et 40 → chapitres 46 et 47 (flottes de périphérie sous TUF, SRE autonome et distillation Multi-LoRA) → annexe G (grilles G.2 et G.3). <!-- ajout partie X -->Pour la veille : chapitres 48 et 49 (validité des bancs d’essai, registre de veille). Pour l’essai et le retour arrière : sections 21.5 (injection de fautes) et 34.6 (versions et points d’accès).<!-- fin ajout -->
- **Livrables directement réutilisables.** Schéma de télémétrie `gen_ai.*`, pipeline CI/CD ADLC intégrant OpenEnv et $\tau$-bench, matrice de rayon d’impact SRE sous Cedar et porte de promotion $\text{pass}^5$ de distillation.

### 5. Parcours CDO, architecte de données et ingénieur contexte / sémantique

- **Question directrice.** *Comment transformer nos entrepôts, graphes documentaires et couches BI en un modèle du monde cohérent, auto-protégé et non contradictoire pour tous nos agents ?*
- **Séquence prioritaire.** Chapitre 1 (systèmes d’enregistrement et systèmes d’action) → chapitres 12 à 14 → chapitres 45 et 46 (Dataspace ODRL et résidence juridictionnelle) → chapitre 47 (contrats de données Write-Audit-Publish et curation des jeux d’or exempts de PII). <!-- ajout partie X -->Pour l’état de la preuve : chapitre 48 (mémoire et ancrage sémantique).<!-- fin ajout -->

### 6. Parcours direction juridique, conformité, risques et audit interne

- **Question directrice.** *Comment démontrer la conformité de nos agents devant le BSIF, la Commission d’accès à l’information du Québec ou les régulateurs européens, et encadrer juridiquement les actes posés par nos agents ?*
- **Séquence prioritaire.** Ouverture (section 0.4) → chapitre 43 (gouvernance de l’IA fantôme) → chapitre 10 (mandats vérifiables AP2) → chapitre 30 (traçabilité nominative) → chapitres 38 et 41 → chapitres 45 et 46 (vLEI, droit de la concurrence B2B, conflits CLOUD Act / Loi 25 / E-23) → annexe G (grille G.4). <!-- ajout partie X -->Pour le calendrier : chapitre 49 (échéances réglementaires et normatives de 2027 à 2030). Pour l’assurance et les régulateurs : sections 39.6 (lignes de défense et audit interne), 38.3 (AMF et valeurs mobilières) et 35.7 (autres juridictions).<!-- fin ajout -->

------------------------------------------------------------------------

## 0.4 Conventions, échelle d’autonomie et statut des affirmations

Le même mot « agent » désigne tantôt un simple classifieur de texte, tantôt un système autonome habilité à passer des commandes fournisseurs, ce qui brouille la terminologie de bien des comités d’architecture. Tout le compendium applique donc une échelle normative unique à cinq niveaux d’autonomie opérationnelle (L0 à L4). Elle se définit par les droits de mutation sur le système d’information, le régime de supervision humaine et les contrôles d’infrastructure exigés. Cette échelle est propre à l’ouvrage : ses numéros ne se transposent pas aux trois échelles publiées de la section 1.3, où le L3 de Feng et coll. est « consultant » et le niveau 3 de la CSA « conditionnelle ».

| Niveau | Désignation normative | Droits sur les systèmes d’enregistrement | Régime de supervision humaine | Exigences minimales d’orchestration et d’identité |
|:-------|:-----------------------|:----------------------|:--------------------|:-------------------------|
| **L0** | Exécution déterministe pure (API, règle DMN, robot RPA fixe) | Lecture et écriture strictement codées d’avance, sans inférence | Aucune en exécution nominale (audit classique) | Compte de charge de travail, journalisation standard |
| **L1** | Assistance consultative (copilote synchrone, RAG analytique) | Lecture seule (filtrée par les droits ACL de l’utilisateur) | Humain exécuteur : l’humain lit et saisit toute action | Jeton délégué en lecture seule, masquage PII, télémétrie de base |
| **L2** | Automatisation sous approbation préalable (humain dans la boucle, HITL) | Préparation d’écriture (brouillon de transaction en tampon) | Approbation synchrone ou asynchrone explicite avant validation | État durable (`awakeable`), identité NHI + OBO, protection anti-biais ASI09 |
| **L3** | Autonomie bornée sous supervision par exception (humain sur la boucle, HOTL) | Écriture directe dans une enveloppe bornée (seuils, périmètre, quotas) | Escalade sur seuil de risque (CIBA) et audit continu | Moteur durable, patron Saga compensable, PDP Cedar/OPA en ligne, coupe-circuit |
| **L4** | Orchestration inter-agents et B2B fédérée | Négociation et exécution multi-domaines ou inter-entreprises | Gouvernance par politique et mandats cryptographiques | A2A v1.0 signé, mandats vérifiables AP2, attestation SPIFFE/DID, traces non répudiables |

:::: {.encadre .important}
::: {.encadre-titre}
**Règle d'attribution du niveau d'autonomie et critère de réversibilité**
:::

Lorsqu’un orchestrateur coordonne plusieurs agents spécialistes, le niveau d’exigence sécuritaire et réglementaire de la chaîne entière est dicté par le maillon dont l’empreinte d’action est la plus élevée (règle du maillon le plus élevé, *High-Water Mark Rule*). Un agent de niveau L1 qui transmet une synthèse non assainie à un agent de niveau L3 fait partie du périmètre de sécurité L3 au regard du détournement d’objectif (OWASP ASI01) et de la conformité réglementaire (BSIF E-23, EU AI Act). Le passage de L2 à L3 suppose en outre une réversibilité effective : une écriture ERP dotée d’une compensation Saga est admissible en L3, tandis qu’un acte externe irréversible, sans fenêtre de grâce ni séquestre (décaissement définitif, notification réglementaire opposable, mouvement mécanique hors sas Simplex), reste soumis à une approbation CIBA (L2) ou à un verrou déterministe matériel.

Cette règle va au-delà de ce que retient le chapitre 1, qui fixe le niveau d’autonomie par agent et par classe d’action (section 1.3).
::::

### Critères d’évaluation technologique utilisés dans l’ouvrage

Chaque fois que le compendium compare des protocoles, des moteurs d’orchestration ou des architectures de mémoire (parties II à IX), l’analyse s’appuie sur cinq critères explicites plutôt que sur la popularité d’un outil :

1. **Gouvernance et neutralité du fournisseur.** La spécification appartient-elle à une fondation ouverte regroupant plusieurs acteurs (Linux Foundation AAIF, ASF, IETF, W3C, FIDO) ou dépend-elle de la feuille de route commerciale d’un éditeur unique ? Au sein de l’AAIF, la gouvernance technique varie d’un projet à l’autre (section 11.2).
2. **Déterminisme des frontières et auditabilité.** Peut-on reconstruire après coup, devant un auditeur interne ou un régulateur externe, l’état exact, l’identité délégante, la version de politique et les entrées qui ont conduit à une mutation ?
3. **Tolérance aux pannes et sémantique de reprise.** Que se passe-t-il concrètement si un nœud de calcul disparaît ou si une API externe expire à la septième étape d’un processus de dix étapes ?
4. **Coût marginal en latence et en jetons.** Quel est le multiplicateur d’appels LLM, la surcharge de sérialisation et l’effet sur la réutilisation du KV-cache lorsque le volume passe de dix requêtes par jour à dix mille par heure ?
5. **Coût de sortie.** Quel effort d’ingénierie faut-il pour remplacer le modèle sous-jacent, changer de fournisseur infonuagique ou substituer un agent spécialiste sans réécrire le plan d’orchestration ?

### Faits vérifiés et projections 2027

Un compendium de référence pour 2027 doit distinguer ce qui est établi de ce qui émerge. Dans l’ensemble des chapitres :

- Les protocoles, fondations, cadres de sécurité et produits présentés comme socles d’architecture (MCP, A2A v1.0, les dix projets hébergés par l’AAIF au 11 novembre 2026, contre trois à sa création (section 11.2), la pile AGNTCY, Apache Ossie, OpenTelemetry `gen_ai.*`, OWASP ASI01–ASI10, la famille $\tau$-bench, Temporal, Restate, Microsoft Agent Framework, Bedrock AgentCore, MuleSoft Agent Fabric, UiPath Maestro) existent et sont documentés fin 2026. Cela ne vaut pas preuve d’usage : aucun cas documenté ne montre MCP, A2A ou un système multi-agents en production (section 1.5, chapitre 42). <!-- ajout partie X -->Les statistiques officielles situent l’usage de l’IA, toutes formes confondues, à une entreprise sur cinq environ (section 4.1).<!-- fin ajout --> Certains de ces socles restent en chantier : les conventions d’OpenTelemetry sont au statut « Development », le registre officiel de MCP est en préversion et l’identité des agents n’a pas de profil adopté (section 4.4).
- Les échéances juridiques (BSIF E-23 et ligne directrice de l’AMF sur l’IA au 1er mai 2027, EU AI Act annexe III en décembre 2027, obligations actives de la Loi 25 et de l’article 50 européen) reposent sur les textes en vigueur. La date de décembre 2027 est connue par une reproduction non officielle du règlement (UE) 2026/1744 (section 4.4), dont le chapitre 35 confirme le report par les considérants publiés sur EUR-Lex. Le texte signale systématiquement les zones où des guides d’application sectoriels demeurent attendus.
- Les pratiques d’avant-garde, soit la contractualisation B2B entièrement autonome d’entreprise à entreprise via AP2 et x402 et l’auto-assemblage dynamique d’essaims sans topologie pré-approuvée, sont balisées comme des frontières émergentes, avec les verrous juridiques et prudentiels qui en limitent encore le déploiement généralisé.
- Les projections <!-- ajout partie X -->au-delà de 2027 sont réunies au chapitre 50, qui sépare ce qu’un texte date, ce qu’un émetteur annonce et ce qui reste une conjecture.<!-- fin ajout -->

------------------------------------------------------------------------

## 0.5 Dossier initial du fil rouge : Groupe Boréal Inc.

Les concepts d’interopérabilité et d’orchestration montrent leur difficulté réelle au contact d’un système d’information patrimonial, formé par des décennies d’acquisitions, de dettes techniques et d’obligations légales hétérogènes. Plutôt que des exemples limités à trois fonctions Python idéalisées, les volets « Mise en œuvre » suivent la transformation d’une entreprise de référence fictive mais réaliste : Groupe Boréal Inc. (« Groupe Boréal »).

:::: {.encadre .filrouge}
::: {.encadre-titre}
**Fil rouge — Dossier d'architecture initial du Groupe Boréal (T4 2026)**
:::

**Profil général.** Conglomérat industriel, financier et numérique dont le siège social est établi à Montréal (Québec), qui compte 14 500 employés et réalise un chiffre d’affaires annuel de 6,8 G\$ CAD en Amérique du Nord et en Union européenne.

**Trois divisions opérationnelles.**

1. **Boréal Équipements & Logistique (BEL — 3,6 G\$ CAD).** Fabrication d’équipements électromécaniques lourds (4 usines au Québec, en Ontario et en Allemagne) et distribution de pièces (9 centres logistiques). Socle technique : SAP S/4HANA (avec SAP Joule), exécution manufacturière Siemens Opcenter, automates d’atelier exposés en OPC UA et MQTT, courtiers d’événements Confluent Kafka et Solace PubSub+, partenaires logistiques raccordés en EDI X12.
2. **Boréal Capital & Assurances (BCA — 1,9 G\$ CAD).** Financement d’équipements, crédit-bail commercial et assurance bris de machine. Filiale assujettie à la supervision fédérale canadienne du BSIF (ligne directrice E-23 applicable au 1er mai 2027), qui traite des renseignements personnels soumis à la Loi 25. Socle technique : système central de contrats et d’indemnisation sur IBM i (AS/400), dépourvu d’API REST modernes, Guidewire, Workday, entrepôt analytique Snowflake et annuaire Microsoft Entra ID.
3. **Boréal Services Numériques (BSN — 1,3 G\$ CAD).** Plateforme infonuagique B2B de télématique industrielle et de maintenance prédictive, qui relie 180 000 machines déployées chez 22 000 entreprises clientes au Canada, aux États-Unis et en Europe (soumise à l’EU AI Act pour ses modules prédictifs et d’assistance). Socle technique : Salesforce Sales/Service Cloud (Agentforce), ServiceNow ITSM/FSM, Microsoft Copilot Studio dans Teams, et grappe Kubernetes interne qui héberge des services analytiques et des modèles ouverts.

**La situation à l’automne 2026 (point de départ du fil rouge).** Un audit conjoint Architecture–Sécurité, ordonné à la suite de deux incidents, recense 47 initiatives agentiques disparates dans les trois divisions et les fonctions centrales, dont 19 déployées hors de tout contrôle TI (agents fantômes) :

- **Incident financier.** Un agent prototype d’achat chez BEL est entré un dimanche dans une boucle de réessai non bornée, à la suite d’une erreur HTTP 429 mal gérée. La boucle a duré 11 heures et consommé 41 000 \$ CAD de jetons d’un modèle de raisonnement frontière, avant une détection manuelle le lundi matin.
- **Incident de conformité.** Un assistant interne de pré-qualification utilisait un jeton de compte de service partagé, avec un accès en lecture élargi à des dossiers RH ainsi qu’à des tables de sinistres hors périmètre chez BCA, sans journalisation de l’employé donneur d’ordre. Cette lacune est incompatible avec la piste d’audit qu’exigent la Loi 25 et l’échéance BSIF E-23.
- **Cloisonnement opérationnel entre silos.** Lorsqu’une sonde télématique BSN détecte une dérive vibratoire critique sur un compresseur industriel sous contrat, quatre agents locaux existent déjà (diagnostic BSN, billetterie ServiceNow, contrat BCA, stock SAP), mais aucun ne peut coopérer avec les autres. Trois coordonnateurs humains passent en moyenne 46 heures à recopier des numéros de série entre quatre écrans pour valider la garantie, réserver la pièce et dépêcher un technicien certifié.

**Le mandat 2027.** Le comité exécutif confie à l’architecte en chef la conception de la Fabrique Agentique Boréal (*Boréal Agentic Fabric*), avec trois objectifs chiffrés à douze mois : ramener le délai de bout en bout d’une intervention prédictive sous 25 minutes en autonomie supervisée L3, réduire de 55 % le coût d’inférence par dossier traité, et réussir l’homologation réglementaire croisée BSIF E-23 / Loi 25 / ISO/IEC 42001 avant le deuxième trimestre 2027.
::::

Chaque volet « Mise en œuvre » s’appuie sur une brique précise de ce chantier et montre, schémas et contrats de code à l’appui, comment passer d’un ensemble de prototypes fragiles à une architecture d’entreprise interopérable, résiliente et gouvernée.

------------------------------------------------------------------------

## 0.6 Carte des standards, protocoles et cadres de référence 2027

Les équipes d’architecture butent en 2026–2027 sur la densité d’acronymes d’un écosystème qui s’est structuré vite. Le tableau ci-dessous situe les dix-huit standards techniques, cadres de sécurité et régimes réglementaires qui traversent le compendium : organisme de tutelle, couche de la pile à six couches, fonction et chapitres où leur implémentation est détaillée.

| Standard / Cadre | Organisme de tutelle (fin 2026) | Couche principale | Fonction architecturale | Chapitres clés |
|:-----------------|:----------------|:----------------|:----------------------------------|:--------------|
| **MCP** (*Model Context Protocol*) | Linux Foundation (AAIF) | Couche 1 (Vertical) | Protocole JSON-RPC 2.0 qui normalise l’accès des modèles et des agents aux outils, aux ressources documentaires et aux invites métiers | Chap. 1, 5, 31, 46 et 47 |
| **Agent Skills & `AGENTS.md`** | Linux Foundation (AAIF) | Couche 1 (Vertical) | Formats ouverts d’empaquetage modulaire de compétences exécutables et de consignes contextuelles de dépôt | Chap. 5, 11, 13 et 34 |
| **Open Responses** | Linux Foundation (AAIF) | Couche 1 (Inférence) | Spécification d’API partagée qui normalise les sorties structurées et les événements d’inférence entre fournisseurs de modèles | Chap. 5, 11, 44 et 46 |
| **WebMCP** | Écosystème Web / W3C CG | Couche 1 (Web) | Exposition native d’outils et de contexte structuré par les applications web au navigateur et aux agents | Chap. 5 et 9 |
| **agentgateway & Agent Router** | Linux Foundation (AAIF) | Couche 1 (Plan de données) | Passerelles natives de l’IA qui unifient le routage multi-LLM, le multiplexage MCP, le proxy A2A et les politiques de débit | Chap. 11, 32, 44, 46 et 47 |
| **Apache Ossie** (*OSI*) | Apache Software Foundation | Couche 2 (Sémantique) | Standard ouvert d’échange sémantique qui unifie définitions de métriques, dimensions et relations ontologiques | Chap. 12, 13, 27 et 47 |
| **A2A v1.0** (*Agent2Agent*, dont ACP) | Linux Foundation (AAIF) | Couche 3 (Horizontal) | Protocole pair à pair de découverte (Agent Cards), de délégation asynchrone de tâches et de partage d’artefacts entre agents | Chap. 1, 6, 11, 27 et 45 |
| **AGNTCY (OASF, SLIM, *Directory*)** | Linux Foundation | Couche 3 (Réseau) | Schéma descriptif universel de capacités (OASF), annuaire fédéré et messagerie chiffrée MLS à faible latence (SLIM) | Chap. 6, 7, 11 et 45 |
| **AG-UI & A2UI / MCP-UI** | Communautés Open Source | Couche 5 (Interface) | Flux bidirectionnel d’événements d’état agentique (AG-UI) et génération déclarative sécurisée de composants d’interface (A2UI) | Chap. 7 et 10 |
| **OPC UA & MQTT Sparkplug** | OPC Foundation / Eclipse | Couche 1 & 4 (IT/OT) | Protocoles industriels normalisés pour l’exploration sémantique et la télémétrie en temps réel des équipements d’usine | Chap. 1, 28 et 46 |
| **OAuth 2.1 OBO, RFC 8693 & CIBA** | IETF / OpenID Foundation | Transversal (Identité) | Échange de jetons délégués à portée atténuée (`sub`/`act`) et authentification hors bande asynchrone pour les actions critiques | Chap. 30, 32 et 47 |
| **SPIFFE / SPIRE & W3C DIDs / VCs** | CNCF (LF) / W3C | Transversal (Identité) | Attestation cryptographique de l’identité machine (NHI) et justificatifs vérifiables de provenance ou de mandat | Chap. 10, 29, 30, 45 et 46 |
| **OWASP ASI01–ASI10** | Fondation OWASP | Transversal (Sécurité) | Taxonomie de référence des dix risques critiques propres aux applications agentiques autonomes et multi-agents | Chap. 31, 32, 41 et 47 |
| **OpenSandbox & OpenEnv** | Linux Foundation (AAIF) | Sécurité & AgentOps | Exécution isolée et sécurisée du code et des outils (OpenSandbox); environnements normalisés d’évaluation et de RL (OpenEnv) | Chap. 32, 34 et 47 |
| **OpenTelemetry (`gen_ai.*`)** | CNCF (Linux Foundation) | Transversal (AgentOps) | Conventions sémantiques neutres pour tracer de bout en bout les appels de modèles, les jetons, les outils MCP et les graphes A2A | Chap. 33, 40 et 47 |
| **AP2 & x402** | FIDO Alliance / LF (x402) | Couche 6 (Commerce) | Mandats cryptographiques d’intention et de panier (AP2), couplés au règlement financier natif sur le code HTTP 402 (x402) | Chap. 10, 38 et 45 |
| **ISO/IEC 42001 & NIST AI RMF** | ISO/IEC / NIST | Couche 6 (Gouvernance) | Système de management de l’IA certifiable en amélioration continue (PDCA) et référentiels de maîtrise des risques | Chap. 35 et 38 |
| **EU AI Act, BSIF E-23 & Loi 25** | UE / BSIF Canada / Québec | Couche 6 (Réglementaire) | Obligations légales contraignantes de transparence, de gestion du risque de modèle (1er mai 2027), d’ÉFVP et de supervision humaine | Chap. 1, 35, 38, 46 et 47 |

Le statut de ces textes est inégal. L’AAIF distingue trois niveaux (Sandbox, Growth, Impact), et seul celui d’A2A est établi, au niveau Growth (section 11.2). Pour l’identité des agents, aucun RFC propre aux agents n’existe, et l’identité décentralisée (DID) relève de la posture « attendre » (sections 11.4 et 11.10). Aucune norme ISO/IEC propre aux agents n’a été repérée, et l’initiative du NIST n’a produit aucun livrable normatif à ce jour (sections 11.5 et 11.6).

### Articulation des parties du compendium

La progression des chapitres suit un principe d’ingénierie : on ne peut orchestrer durablement que ce qui est interopérable par ses protocoles et sa sémantique, ni mettre en production à grande échelle que ce qui est identifié par cryptographie, observable, souverain et borné sur le plan économique.

- Les parties I à III construisent le modèle anatomique, protocolaire et sémantique : elles définissent les acteurs, séparent le contrôle déterministe de l’inférence probabiliste, déploient la pile ouverte MCP / A2A / AGNTCY / AG-UI et traitent l’alignement du sens métier par Apache Ossie et la mémoire bi-temporelle.
- Les parties IV et V construisent le moteur d’exécution et d’intégration au réel : topologies d’orchestration et de chorégraphie, exécution durable sur plusieurs jours (Temporal, Restate), sagas événementielles à compensation (Kafka, Solace), passerelles natives de l’IA à routage SLM/LLM, puis fédération des suites SaaS (Agentforce, ServiceNow, SAP Joule, Copilot Studio), des écrans patrimoniaux sans API (CUA) et des ateliers industriels (OPC UA, jumeaux numériques).
- Les parties VI à VIII traitent l’exploitabilité industrielle, sécuritaire, financière et juridique : identités non humaines à confiance zéro, défense active contre OWASP ASI01–ASI10, observabilité OpenTelemetry, homologation par simulation $\tau$-bench et ingénierie du chaos, FinOps du coût par résultat, conformité réglementaire 2027 et modèle organisationnel du Centre d’Excellence Agentique.
- La partie IX prolonge l’architecture au-delà des frontières de l’entreprise, puis vers la méta-ingénierie continue : maillages B2B inter-entreprises (Dataspace EDC / ODRL, vLEI, *Clean Rooms*), souveraineté cognitive et Cognitive DR, cellules de périphérie déconnectées et robotique ROS 2 sous architecture Simplex, puis usine logicielle Agentic SDLC de modernisation patrimoniale, Agentic DataOps/SRE et distillation continue LLM → SLM.
- La partie X <!-- ajout partie X -->change de registre et regarde l’ouvrage du dehors : une revue de littérature confronte ses thèses à la recherche publiée, une veille technologique fixe ce qu’il faut surveiller d’ici 2030, et une étude de marché projette 2027 à 2030 en séparant le daté, l’annoncé et le conjecturé (chapitres 48 à 50).<!-- fin ajout -->

La partie I pose les fondations architecturales de cette main-d’œuvre numérique d’exécution asynchrone.
