# 6 Interopérabilité

Ce chapitre fixe la manière dont les agents de l’entreprise se relient aux outils, aux données, aux autres agents, aux événements et aux personnes. Il s’appuie sur des protocoles ouverts sous gouvernance neutre : MCP pour l’intégration verticale (agent vers outil), A2A pour l’intégration horizontale (agent vers agent), CloudEvents et AsyncAPI pour les échanges asynchrones. Chaque intégration est examinée, de façon proportionnée, à deux ou à quatre niveaux, du juridique au technique, et n’emploie que des standards inscrits au catalogue, à une version fixée. Les sections 6.5 à 6.7 détaillent chaque protocole; les sections 6.8 et 6.9 traitent des contrats, du versionnage et de la veille.

## 6.1 Quatre niveaux d’interopérabilité et gouvernance intégrée

Une connexion technique ne suffit pas : deux agents qui échangent sans s’entendre sur le sens des données ni sur les responsabilités produisent des erreurs silencieuses. Le cadre transpose donc aux agents le modèle du Cadre européen d’interopérabilité *(European Interoperability Framework, EIF)*.

Le nouvel EIF, publié par la Commission européenne en 2017, décrit l’interopérabilité en quatre couches (juridique, organisationnelle, sémantique et technique), encadrées par une composante transversale, la gouvernance intégrée des services publics, et par une couche de fond, la gouvernance de l’interopérabilité**[157, 158]**. Il énonce 12 principes et 47 recommandations, dont la conclusion d’accords d’interopérabilité dans toutes les couches (recommandation 26)**[157]**. Le texte reste vivant : le règlement (UE) 2024/903 pour une Europe interopérable, en vigueur depuis le 11 avril 2024, confie sa mise à jour au comité pour une Europe interopérable**[159]**. L’EIF vise les services publics européens; le cadre en retient la structure, pas le champ d’application.

Appliqués aux agents, les quatre niveaux posent quatre questions simples :

- **Juridique** : l’échange respecte-t-il les lois et les contrats? Par exemple, un agent qui confie l’analyse d’une réclamation à l’agent d’un partenaire hébergé en Ontario communique des renseignements personnels à l’extérieur du Québec, ce qui exige une EFVP préalable (art. 17 de la Loi sur le privé)**[160]**.
- **Organisationnel** : qui répond de quoi, de part et d’autre? L’EIF parle d’aligner les processus, les responsabilités et les attentes pour atteindre des objectifs communs**[157]**.
- **Sémantique** : les parties comprennent-elles la même chose? L’EIF y inclut l’aspect syntaxique, soit le format exact des informations échangées, pour que ce qui est envoyé soit ce qui est compris**[157]**.
- **Technique** : les systèmes peuvent-ils se joindre de façon sûre? Le niveau couvre les spécifications d’interface, les services d’interconnexion et d’intégration de données et les protocoles de communication sécurisés**[157]**.

La gouvernance intégrée tient le tout dans la durée. L’EIF y exige notamment des structures, des rôles et des responsabilités définis, des ententes de niveau de service, la gestion des accords d’interopérabilité, des procédures de gestion du changement et des plans de continuité et de qualité des données, parce que les changements législatifs, organisationnels et technologiques perturbent régulièrement l’interopérabilité**[157]**. Dans le cadre, ce rôle revient au registre, au catalogue d’entreprise et au comité d’architecture et des risques agentiques (chapitre 11, figure 5).

> **[Figure]**
> - Gouvernance intégrée : registre, catalogue, comité
> - Juridique
> - L’échange respecte-t-il les lois et les contrats?
> - Exigences pour les agents
> - Organisationnel
> - Qui répond de quoi, de part et d’autre?
> - Exigences pour les agents
> - Propriétaire métier nommé, équipe de garde, niveaux de service et voie d’escalade inscrits au contrat d’agent; processus métier alignés de part et d’autre de la délégation
> - Sémantique
> - Les parties comprennent-elles la même chose?
> - Exigences pour les agents
> - Vocabulaire métier commun, modèles de données canoniques, schémas JSON versionnés, descriptions d’outils et de compétences rédigées pour être comprises par un modèle
> - Technique
> - Les systèmes peuvent-ils se joindre de façon sûre?
> - Exigences pour les agents
> - Finalité et fondement de chaque flux de renseignements personnels; EFVP lorsque la loi l’exige, notamment hors Québec; entente écrite et clauses contractuelles avec chaque tiers
> - Protocoles du catalogue (MCP, A2A, CloudEvents, OpenAPI), TLS 1.3 (1.2 en plancher), authentification normalisée (OAuth 2.0, RFC 9700), contexte de trace W3C propagé à chaque appel

***Figure 5 — Quatre niveaux d’interopérabilité appliqués aux agents.** Chaque intégration d’agent se lit de haut en bas : le juridique fixe ce qui est permis, l’organisationnel désigne qui en répond, le sémantique établit le sens des données et le technique, la façon dont elles circulent. La gouvernance intégrée encadre les quatre niveaux. Source : adapté du nouveau Cadre européen d’interopérabilité (Commission européenne, 2017); exigences propres au cadre, dont le tableau 14 donne la formulation qui fait foi.*

*Tableau 14 — Niveaux d’interopérabilité et exigences minimales pour une intégration d’agent*

| **Niveau** | **Question à trancher** | **Exigences minimales** | **Traité à** |
| --- | --- | --- | --- |
| Juridique | L’échange respecte-t-il les lois et les contrats? | Finalité et fondement (consentement ou exception prévue par la loi) documentés pour chaque flux de renseignements personnels; EFVP lorsque la loi l’exige, notamment avant toute communication hors Québec; entente écrite avec chaque tiers; clauses contractuelles pour les agents et serveurs MCP de tiers. | Chapitres 12 et 13 |
| Organisationnel | Qui répond de quoi, de part et d’autre? | Propriétaire métier nommé et équipe de garde de chaque côté; niveaux de service et voie d’escalade inscrits au contrat d’agent; processus métier modélisés et alignés de part et d’autre de la délégation. | Sections 11.1 et 11.4 |
| Sémantique | Les parties comprennent-elles la même chose? | Vocabulaire métier commun; données de référence (taxonomies, listes de codes); schémas JSON Schema 2020-12 versionnés; unités, devises, assiettes de taxes et fuseaux horaires explicites; descriptions d’outils et de compétences rédigées pour être comprises par un modèle. | Section 6.8 |
| Technique | Les systèmes peuvent-ils se joindre de façon sûre? | Protocole du catalogue à la version fixée; TLS 1.3 par défaut et TLS 1.2 toléré comme plancher (choix du cadre, conforme aux recommandations d’A2A**[68, 161]**); authentification normalisée; contexte de trace W3C propagé à chaque appel. | Sections 6.3 à 6.7; chapitres 9 et 10 |
| Gouvernance intégrée (transversale) | L’échange restera-t-il interopérable dans le temps? | Accord d’interopérabilité pour toute intégration qui franchit la frontière d’un domaine métier ou de l’entreprise (EXIG-INT-03); gestion du changement des contrats; plan de continuité; fiche d’agent et catalogue à jour. | Section 6.8; chapitre 11 |
| Gouvernance de l’interopérabilité (fond) | Qui choisit les standards et qui arbitre? | Catalogue des protocoles révisé chaque trimestre; dérogations instruites par le comité. | Sections 6.3, 11.6 et 11.7 |

**EXEMPLE : UNE ERREUR QUE LE PROTOCOLE NE VOIT PAS**

L’agent de facturation d’une filiale transmet par A2A un artefact dont le champ `montant` vaut 1 149,75. L’agent de rapprochement du siège le lit comme un montant hors taxes, alors qu’il inclut la TPS et la TVQ. Les deux agents respectent le protocole à la lettre; seule la revue sémantique (schéma commun, unité et assiette déclarées) prévient l’écart.

`EXIG-INT-01` **· DOIT**

**Revue d’interopérabilité proportionnée**

Toute intégration d’un agent avec un outil, une ressource, un autre agent ou un flux d’événements **DOIT** faire l’objet, avant sa mise en production, d’une revue proportionnée selon le tableau 14 : niveaux sémantique et technique pour une intégration intradomaine qui n’emploie que des outils P0 ou P1 et ne traite pas de renseignements personnels; les quatre niveaux, juridique, organisationnel, sémantique et technique, dans tous les autres cas. Le résultat **DOIT** être consigné dans la fiche d’agent (annexe B).

Pourquoi : une intégration techniquement valide peut être illicite, sans responsable ou fausse sur le sens; l’EIF promeut l’interopérabilité dès la conception**[157]**.

`EXIG-INT-02` **· DOIT**

**Vocabulaire et schémas d’entreprise**

Les données structurées échangées entre agents, entre agents et outils et sur le bus d’événements (arguments et résultats structurés d’outils, parties `data` des messages A2A, charges utiles d’événements) **DOIVENT** être décrites par des schémas JSON Schema 2020-12 versionnés (dans AsyncAPI 3.x, en déclarant explicitement `schemaFormat` à JSON Schema 2020-12, le format par défaut étant le Schema Object d’AsyncAPI; la chaîne d’outils qui lit ces contrats est éprouvée sur ce format avant l’inscription au catalogue, ou la validation JSON Schema 2020-12 s’exécute hors de l’outillage AsyncAPI lorsque celui-ci se limite au draft-07). Les schémas produits par l’entreprise **DOIVENT** s’appuyer sur le vocabulaire métier et les données de référence de l’entreprise (taxonomies, listes de codes, unités et devises explicites) et être gérés au niveau de l’entreprise, et non par chaque équipe d’agent. Un schéma de tiers (serveur MCP, carte d’agent ou contrat d’événement d’un éditeur ou d’un partenaire) **DOIT** être inscrit au catalogue avec son empreinte, épinglé et approuvé; sa correspondance avec le vocabulaire d’entreprise est tenue à l’adaptateur ou à la passerelle. Un schéma de tiers qui déclare un autre dialecte (`$schema`) est inscrit avec son dialecte et validé par un validateur de ce dialecte, ou converti à l’adaptateur ou à la passerelle; à défaut, il est refusé. Le contenu non structuré (parties `text`, `raw` et `url`, blocs texte) n’est pas visé par la présente exigence.

Pourquoi : l’EIF demande une gestion de l’information coordonnée au plus haut niveau et appuyée sur des données de référence**[157]**; JSON Schema 2020-12 est le dialecte par défaut de MCP**[162, 163]**.

`EXIG-INT-03` **· DOIT**

**Accord d’interopérabilité et gestion du changement**

Toute intégration qui franchit la frontière d’un domaine métier ou de l’entreprise **DOIT** être couverte par un accord d’interopérabilité, intégré au contrat d’agent ou d’outil, qui nomme le propriétaire de chaque partie, les niveaux de service, la voie d’escalade et la procédure de gestion du changement (préavis, période de coexistence, tests de non-régression).

Pourquoi : l’EIF recommande des accords d’interopérabilité dans toutes les couches et une gestion explicite du changement**[157]**.

## 6.2 Carte des interactions et protocoles retenus

Le cadre associe un protocole à chaque type d’interaction d’un agent. La figure 6 situe ces interactions autour de l’agent : verticalement vers les outils, horizontalement vers les autres agents, de façon asynchrone vers le bus d’événements et, du côté humain, vers l’interface.

> **[Figure]**
> - Agent
> - raisonne, planifie, appelle
> - des outils, délègue, publie
> - Agent interface utilisateur
> - AG-UI · flux SSE
> - état partagé, formulaires d’approbation
> - Agent outils et données
> - MCP
> - outils, ressources, invites; API existantes via OpenAPI 3.1
> - et adaptateurs
> - intégration verticale
> - Agent agent pair opaque
> - A2A
> - carte d’agent, tâche à états, diffusion en continu, notifications; autre cadriciel, autre organisation
> - horizontale
> - Agent bus d’événements
> - CloudEvents · AsyncAPI
> - découplage temporel, plusieurs
> - abonnés, rejeu; Kafka ou
> - équivalent infonuagique
> - asynchrone
> - Identité et autorisation
> - OpenID Connect, SPIFFE; mTLS ou DPoP
> - Observabilité
> - OpenTelemetry (conventions GenAI),
> - contexte W3C Trace Context
> - Découverte et confiance
> - Catalogue d’entreprise, cartes d’agent
> - signées, registre de serveurs MCP,
> - versions épinglées et empreintes
> - OAuth 2.0 (RFC 9700), échange de jetons (RFC 8693),
> - À surveiller ou à contenir
> - Commerce et paiements agentiques :
> - veille hors production; formats propres
> - à un fournisseur, derrière un adaptateur
> - →
> - →
> - → ↔

***Figure 6 — Carte des interactions de l’agent et protocoles retenus.** L’agent occupe le centre; chaque liaison correspond à un type d’interaction et au protocole retenu. Les cartes périphériques rappellent les fonctions transversales (identité, observabilité, découverte et confiance) et ce qui reste à surveiller ou à contenir : le commerce et les paiements agentiques au statut Surveiller (veille hors production), les formats propres à un fournisseur au statut Contenir (usage existant derrière un adaptateur). OAuth 2.0 y est profilé par la RFC 9700, le profil OAuth 2.1 restant un brouillon. Le tableau 15 fait foi pour les versions et les statuts. Source : cadre CRE-IA-2026-01; répartition MCP et A2A conforme au guide officiel du projet A2A.*

- **Agent → outils et données : MCP.** La cible a des entrées et des sorties définies, souvent sans état; l’agent appelant garde la boucle de raisonnement. Les API existantes y sont exposées par des adaptateurs, sans réécriture (section 6.5).
- **Agent → agent : A2A.** La cible est un agent autonome, potentiellement opaque, qui raisonne, garde un état sur plusieurs tours et peut demander une précision (section 6.6).
- **Agent ↔ bus d’événements : CloudEvents et AsyncAPI.** L’émetteur ignore ses consommateurs; l’échange admet plusieurs abonnés, le découplage dans le temps et le rejeu des entrées (section 6.7).
- **Agent → interface : AG-UI ou flux SSE** ***(Server-Sent Events)*** **structuré.** AG-UI est un protocole ouvert et événementiel (31 types d’événements standard selon la documentation, licence MIT), né d’un partenariat de CopilotKit avec LangChain et CrewAI; il n’impose pas de transport (SSE, WebSockets, webhooks, etc.) et complète MCP et A2A**[164, 165, 166]**. Il demeure au statut Évaluer.

Cette répartition reprend le guide officiel du projet A2A : MCP relie un agent à des outils et à des ressources aux entrées et aux sorties définies, souvent sans état, alors qu’A2A relie des agents autonomes, potentiellement opaques, qui raisonnent et conservent un état sur des échanges à plusieurs tours**[39]**. Les deux se complètent : l’agent spécialiste joint par A2A utilise lui-même des outils MCP. L’événement comble un troisième besoin : un appel d’outil MCP est un échange requête-réponse point à point, sans rétention, ni rejeu, ni diffusion à plusieurs abonnés, alors qu’un journal d’événements persistant découple producteurs et consommateurs dans le temps (voir aussi Kai Waehner**[167]**).

Une question départage la plupart des cas : la cible choisit-elle elle-même ses actions? Elle est un agent si elle choisit elle-même, au moyen d’un modèle, les actions qu’elle exécute; sinon, c’est un outil, même si elle emploie un modèle en interne pour transformer une donnée, conserve l’état d’une tâche ou demande une précision (Tasks, élicitation MCP) (règle du cadre, tableau 7). Si l’émetteur ne doit pas connaître ses destinataires, c’est un événement. Tout appel MCP ou A2A, quel que soit le domaine, passe par la passerelle d’agents, et tout événement par le courtier (EXIG-ARC-01, EXIG-ARC-13; section 9.4); la documentation d’A2A recommande d’ailleurs fortement une solution de gestion d’API devant tout serveur exposé à l’externe**[161]**.

**À RETENIR**

MCP pour ce qui s’exécute, A2A pour ce qui raisonne, l’événement pour ce qui se diffuse. Rien ne contourne les points d’application : la passerelle d’agents pour MCP, A2A et les actions P2 ou P3, la passerelle de modèles pour l’inférence et le courtier pour les événements (EXIG-EVT-07), tous alimentés par le catalogue d’entreprise.

`EXIG-INT-04` **· DOIT**

**Protocole désigné par type d’interaction**

Chaque interaction d’un agent **DOIT** emprunter le protocole que le catalogue désigne pour son type : MCP pour l’accès aux outils, aux ressources et aux invites; A2A pour toute délégation à un agent d’un autre domaine, d’un autre cadriciel, d’un tiers ou d’un autre processus (EXIG-A2A-01, sauf coexistence bornée de l’EXIG-A2A-15); CloudEvents, décrit par un contrat AsyncAPI, pour les événements; pour l’interface utilisateur, AG-UI en pilote ou le flux SSE structuré produit par l’orchestrateur (tableau 15). L’appel d’inférence relève de l’EXIG-ARC-08. Tout format hors catalogue exige une dérogation (section 11.6); un format propriétaire inscrit au statut Contenir reste toléré derrière un adaptateur jusqu’à la date de son plan de sortie, sans nouvel usage (EXIG-INT-06).

Pourquoi : un protocole commun par type d’interaction ramène le maillage de N × M connecteurs à N + M contrats (chapitre 2) et permet à la passerelle d’appliquer une politique uniforme.

`EXIG-INT-05` **· DEVRAIT**

**Agent pair invoqué par A2A, pas déguisé en outil**

Sous réserve de l’obligation d’employer A2A pour toute délégation à un agent d’un autre domaine, d’un autre cadriciel, d’un tiers ou d’un autre processus (EXIG-A2A-01), un sous-agent doté d’un cycle de vie de tâche propre **DEVRAIT** être invoqué comme pair plutôt que déguisé en simple outil sans état; l’enveloppe « agent comme outil » n’est permise qu’entre sous-agents d’un même orchestrateur, dans un même processus, selon le critère de la section 6.2.

Pourquoi : A2A expose le cycle de vie de la tâche (entrée requise, authentification requise, annulation, artefacts), que l’enveloppe en outil masque; l’approbation humaine et l’audit en dépendent**[68]**.

## 6.3 Catalogue des protocoles et standards

Le catalogue des protocoles dit quel standard employer, à quelle version et avec quel degré de confiance. Il distingue ce qui est une norme publiée, ce qui n’est qu’un brouillon et ce qui relève encore de l’annonce. Chaque entrée porte l’un des cinq statuts suivants, éventuellement assorti d’une réserve :

- Adopter usage par défaut, exigé pour toute nouvelle intégration du type visé;
- Évaluer pilotes encadrés, derrière la passerelle d’agents (section 6.9); passage en production seulement après une décision du comité qui fait passer l’entrée au statut Adopter;

- Surveiller veille et essais hors production, sans données réelles;
- Contenir existant toléré derrière un adaptateur, sans nouvel usage, avec un plan de sortie daté;
- Suspendu prononcé pour un motif de sécurité (EXIG-INT-14, EXIG-GOV-14) : la passerelle cesse immédiatement de servir l’élément, sans attendre la fin d’une coexistence.

*Tableau 15 — Catalogue des protocoles et standards (état au 27 octobre 2026)*

| **Interaction** | **Standard et version de référence** | **Statut** | **Règle d’usage** |
| --- | --- | --- | --- |
| Agent → outils et données | Model Context Protocol (MCP), révision 2026-07-28, courante au 27 octobre 2026**[34, 168]**; révision 2025-11-25 au statut Contenir jusqu’au 28 juillet 2027 (EXIG-MCP-22) | **Adopter** | Serveurs inscrits au catalogue et joints par la passerelle; Streamable HTTP en environnement serveur; extensions officielles (Tasks, Apps, extensions d’autorisation telles qu’OAuth Client Credentials et Enterprise-Managed Authorization, cette dernière au statut Évaluer), désactivées par défaut dans MCP, activées seulement si elles sont inscrites au catalogue**[169]**; l’autorisation de base relève du cœur de la spécification (6.5). |
| Agent → agent | Agent2Agent (A2A), version de protocole 1.0 (publication 1.0.0 du 12 mars 2026; correctif 1.0.1 du 28 mai 2026)**[29, 30]** | **Adopter** | Carte d’agent signée et inscrite; liaison JSON-RPC obligatoire; gRPC ou HTTP+JSON en complément (EXIG-A2A-08); en-tête `A2A-Version` à chaque requête; interfaces 0.3 seulement en coexistence bornée (6.6). |
| Agent → API existante | OpenAPI 3.1.x comme version de référence, 3.2.x admise (3.2.1 du 10 septembre 2026)**[170]**; erreurs au format RFC 9457**[171]** | **Adopter** | Aucun appel d’API sans contrat; exposition aux agents par des adaptateurs déclaratifs qui produisent des outils orientés tâche, sans réécrire les services. |
| Séquences d’appels d’API | Arazzo 1.1.0 (OpenAPI Initiative, 17 mai 2026)**[172]** | **Évaluer** | Description lisible par machine des flux déterministes d’appels d’API. |
| Schémas de données | JSON Schema 2020-12**[163]** | **Adopter** | Dialecte unique des contrats d’outils, de compétences et d’événements; aucun `$ref` vers une URI réseau non autorisée**[162]**. |
| Événements asynchrones | CloudEvents 1.0 (révision 1.0.2) pour l’enveloppe; AsyncAPI 3.0 pour le contrat, versions 3.x ultérieures admises après essai de la chaîne d’outils**[173, 174]** | **Adopter** | Tout événement produit ou consommé par un agent; extensions de gouvernance et compteur de sauts (6.7), sous réserve : ces extensions documentées n’ont aucun statut officiel. |
| Identité et autorisation | OAuth 2.0 profilé par la RFC 9700 (BCP 240); OpenID Connect; échange de jetons (RFC 8693); SPIFFE et SPIRE, au stade « Graduated » de la CNCF**[69, 116, 117, 175]** | **Adopter** | Identité propre à chaque agent; jetons délégués à audience restreinte (chapitre 9). |
| Identité et autorisation | OAuth 2.1, Internet-Draft du groupe de travail OAuth, à la révision épinglée au catalogue (draft-ietf-oauth-v2-1-16 du 3 septembre 2026 à l’état des sources)**[176]** | **Adopter avec réserve** | S’aligner sur son profil (PKCE, ni octroi implicite ni octroi par mot de passe) sans le présenter comme une norme publiée. |
| Identité et autorisation | OAuth Client ID Metadata Document (CIMD), brouillon du groupe de travail OAuth de l’IETF (`draft-ietf-oauth-client-id-metadata-document-02` à l’état des sources; la spécification MCP 2026-07-28 renvoie à la version −00)**[216]** | **Adopter avec réserve** | Identification des clients MCP auprès d’un serveur d’autorisation tiers qui annonce la prise en charge (EXIG-MCP-12); sans le présenter comme une norme publiée. |
| Identité et autorisation | Identity Assertion JWT Authorization Grant (ID-JAG, brouillon de groupe de travail) et extension MCP Enterprise-Managed Authorization**[177, 178]** | **Évaluer** | Accès des employés aux serveurs MCP décidé par le fournisseur d’identité de l’entreprise. |
| Identité et autorisation | Transaction Tokens (draft-ietf-oauth-transaction-tokens-11) **[179]** | **Évaluer** | Propagation du contexte d’identité dans la chaîne d’appels interne d’un domaine. |
| Observabilité | OpenTelemetry; conventions sémantiques GenAI au niveau Development, version de référence v1.41.0 (ligne v1.41, correctif v1.41.1 admis), jusqu’à l’homologation d’une version étiquetée du dépôt `semantic-conventions-genai`**[180, 181]** | **Adopter** | Version émise par chaque composant consignée au catalogue; couche de correspondance versionnée dans le collecteur, qui la ramène à la version de référence (EXIG-OBS-01); attributs d’entreprise sous préfixe de domaine inversé (chapitre 10). |
| Observabilité | W3C Trace Context, Recommandation**[103]** | **Adopter** | Contexte propagé dans HTTP, dans le champ `_meta` de MCP, dans A2A et dans CloudEvents. |
| Agent → interface utilisateur | AG-UI (Agent-User Interaction Protocol)**[164]** | **Évaluer** | Pilotes. En production : flux SSE structuré produit par l’orchestrateur, patron interne au statut Adopter, dont le format d’événements est consigné au catalogue. |
| Infrastructure multiagent | AGNTCY : OASF *(Open Agentic Schema Framework)* et Agent Directory Service *(ADS)*; SLIM *(Secure Low-Latency Interactive Messaging)* et Identity**[182]** | **Évaluer** OASF, ADS **Surveiller** SLIM, Identity | Projet de la Linux Foundation candidat à l’AAIF; aucune dépendance de production sans décision du comité (6.9). |
| Commerce et paiements agentiques | Agentic Commerce Protocol (OpenAI et Stripe), AP2, UCP**[41, 183, 184]** | **Surveiller** | Aucun paiement initié par un agent hors des règles de la section 6.9. |
| Réseaux d’agents ouverts, à identité décentralisée (DID du W3C) | Agent Network Protocol (ANP), projet communautaire**[185, 186]** | **Surveiller** | Aucune adoption en production. |
| Formats propres à un fournisseur | Variable | **Contenir** | Tolérés derrière un adaptateur, jamais exposés directement aux autres agents; plan de sortie daté. |

Les versions sont épinglées au catalogue, pas dans chaque contrat d’agent : une montée de version se décide une fois, pour tout le parc (section 1.6). L’architecture d’entreprise révise le catalogue chaque trimestre et le comité en approuve les changements de statut (EXIG-GOV-18, section 11.7); pour un standard au statut Adopter ou Contenir, la publication d’une version incompatible, d’une dépréciation, d’un retrait accéléré ou d’un correctif de sécurité déclenche une révision extraordinaire, dans les 15 jours ouvrables.

**ATTENTION : NORMES, BROUILLONS ET PRÉVERSIONS**

Plusieurs entrées ne sont pas des normes publiées : OAuth 2.1, ID-JAG et Transaction Tokens sont des Internet-Drafts; les extensions documentées de CloudEvents (Auth Context, Data Classification, Distributed Tracing, etc.) n’ont aucun statut officiel et peuvent être modifiées ou retirées**[187]**; les conventions GenAI d’OpenTelemetry sont au niveau Development, où des changements incompatibles, voire un retrait, peuvent survenir sans garantie de dépréciation préalable**[119, 188]**; le registre officiel MCP est en préversion**[43]**. Le cadre les emploie pour ce qu’ils sont : à une version épinglée, derrière une couche d’adaptation.

`EXIG-INT-06` **· DOIT**

**Statut au catalogue avant tout usage en production**

Tout nouvel usage en production d’un protocole, d’un standard ou d’une extension de protocole **DOIT** reposer sur une entrée du catalogue au statut Adopter. Un usage existant au statut Contenir reste permis derrière un adaptateur jusqu’à l’échéance de son plan de sortie, sans nouvel usage. Le statut Évaluer limite l’usage aux pilotes (EXIG-GOV-20); le statut Surveiller exclut tout usage en production; le statut Suspendu, prononcé pour un motif de sécurité, fait cesser immédiatement le service par la passerelle.

Pourquoi : l’ajout silencieux d’un protocole recrée les intégrations ad hoc que le cadre veut éliminer et soustrait les échanges aux contrôles de la passerelle.

`EXIG-INT-07` **· DOIT**

**Version de référence fixée au catalogue**

Le catalogue **DOIT** fixer, pour chaque standard adopté, la version de référence (révision MCP, version de protocole A2A, version des conventions OpenTelemetry, de CloudEvents et d’AsyncAPI). Chaque serveur, agent et passerelle **DOIT** déclarer les versions qu’il prend en charge. Une déclaration est compatible si elle inclut la version de référence, ou une version au statut Contenir assortie d’une date

de migration inscrite au catalogue (EXIG-MCP-22, EXIG-A2A-15); une déclaration incompatible **DOIT** bloquer l’inscription au catalogue.

Pourquoi : MCP et A2A rejettent explicitement une version non prise en charge (code `UnsupportedProtocolVersion` en MCP, erreur `VersionNotSupportedError` en A2A)**[68, 162]**; un parc aux versions mêlées échoue de façon imprévisible.

`EXIG-INT-08` **· DOIT**

**Révision trimestrielle du catalogue des protocoles**

Chaque entrée du catalogue des protocoles **DOIT** porter la date de révision, le statut retenu et sa justification, et tout changement de statut **DOIT** être notifié aux parrains des agents qui emploient l’entrée. La périodicité de la révision et l’approbation des changements de statut relèvent de l’EXIG-GOV-18.

Pourquoi : entre mars 2025 et juillet 2026, MCP a publié quatre révisions (2025-03-26, 2025-06-18, 2025-11-25 et 2026-07-28) et A2A est passé de la version 0.1 à la version 1.0**[30, 34, 189]**; un catalogue figé devient faux en quelques mois.

`EXIG-INT-09` **· NE DOIT PAS**

**Brouillon présenté comme une norme publiée**

Une exigence d’architecture, une clause contractuelle ou une entrée du catalogue **NE DOIT PAS** présenter un brouillon (Internet-Draft), une préversion ou une annonce de fournisseur comme une norme publiée. Le catalogue indique le statut exact de chaque élément : norme, recommandation, brouillon de groupe de travail, brouillon individuel, préversion ou projet hébergé par une fondation. Pour une extension qui déclare un stade de maturité (Experimental, Beta, Stable), le catalogue l’inscrit extension par extension, et une extension au stade Beta porte une réserve.

Pourquoi : un brouillon peut changer ou expirer (la révision −16 d’OAuth 2.1, du 3 septembre 2026, expirait le 7 mars 2027; la révision −17 l’a remplacée le 31 octobre 2026)**[176]**; une exigence qui s’y appuie doit pouvoir évoluer sans renégocier un contrat.

## 6.4 Matrice de sélection

La matrice traduit la carte de la figure 6 en règle de choix pour les cas courants. Elle se lit par scénario : le protocole découle du type de cible, du couplage recherché et de l’endroit où vit l’état.

*Tableau 16 — Matrice de sélection des protocoles*

| **Scénario** | **Protocole** | **Couplage** | **État côté appelé** | **Raison du choix** |
| --- | --- | --- | --- | --- |
| Processus connu à étapes fixes (réglementé ou audité) | Flux déterministe (chapitre 7) qui appelle des outils MCP ou des API | Piloté par le moteur | Dans le moteur d’exécution durable | Prévisible et auditable; le modèle n’intervient qu’aux étapes qui l’exigent. |
| Agent → outil, base de données ou moteur de recherche documentaire | MCP sur Streamable HTTP | Synchrone et court; réponse JSON ou flux SSE propre à la requête**[190]** | Aucun état cognitif; état applicatif par identifiant explicite, revalidé à chaque appel | Découverte des schémas et contrôle d’accès unifié à la passerelle. |
| Agent → traitement d’outil de longue durée | MCP avec l’extension officielle Tasks (stade Beta), si elle est inscrite au catalogue**[191]** | Asynchrone, par interrogation à l’intervalle annoncé par le serveur, avec un plancher inscrit au catalogue et un quota de tâches par mandant (EXIG-MCP-04) | Tâche durable (identifiant, durée de vie) | Évite de garder une connexion ouverte; annulation coopérative. |
| API REST existante → parc d’agents | Contrat OpenAPI exposé en outils MCP par un adaptateur de composition orienté tâche (EXIG-MCP-06) | Synchrone | Aucun | Réutilise le patrimoine d’API sans connecteur propre à chaque agent. |
| Agent → agent spécialiste, tâche interactive ou en plusieurs tours | A2A | Lâche, par compétence; réponse bloquante, en continu ou par notification push | Tâche à états (huit états de cycle de vie en A2A 1.0, neuf valeurs d’énumération avec `TASK_STATE_UNSPECIFIED`)**[192]** | Suivi de progression, demandes de précision, échange d’artefacts entre cadriciels distincts. |
| Agent → agent d’une autre organisation | A2A par la passerelle, carte signée, jeton délégué | Lâche et contractuel | Tâche à états, opaque pour l’appelant | La confiance repose sur la signature de la carte, le contrat et l’échange de jetons, pas sur le réseau. |
| Système ou agent → plusieurs agents réactifs | CloudEvents et AsyncAPI sur le bus d’événements | Découplé (publication-abonnement) | Journal durable, rejouable dans la limite de la rétention**[140]** | Résilience, absorption des pointes, ajout d’abonnés sans toucher l’émetteur. |
| Agent → interface utilisateur riche | Flux SSE structuré produit par l’orchestrateur, à schéma d’événements versionné au catalogue d’entreprise (patron interne, statut Adopter, section 6.3); AG-UI en pilote seulement (statut Évaluer) | Temps réel | Session d’interface partagée | Synchronise l’état de l’agent et les formulaires d’approbation. |

Lorsqu’un cas ne figure pas dans la matrice, quatre questions qualifient chaque liaison et préparent la soumission exigée par l’EXIG-INT-10. Elles ne sont pas exclusives : une même cible peut relever de MCP pour ses outils et du bus pour ses changements d’état, si bien que la quatrième question se pose pour toute liaison.

1. Les étapes sont-elles connues d’avance? Si oui, un flux déterministe orchestre le travail et n’emploie un agent qu’aux étapes de jugement.
2. La cible est-elle un outil ou une donnée aux entrées et aux sorties définies? Si oui, MCP.
3. La cible choisit-elle elle-même, au moyen d’un modèle, les actions qu’elle exécute? Si oui, c’est un agent, et A2A (EXIG-A2A-01); une cible qui conserve l’état d’une tâche ou demande une précision sans choisir ses actions reste un outil (MCP, extension Tasks, élicitation); au-delà de 5 secondes (seuil fixé par le cadre, EXIG-A2A-07), la diffusion en continu ou les notifications push s’imposent (section 6.6).
4. L’émetteur doit-il ignorer qui consomme, ou faut-il plusieurs abonnés ou un rejeu? Si oui, un événement.

La quatrième question repose sur le découplage logique, non sur le décompte des liaisons : relier N agents deux à deux exige jusqu’à N(N−1)/2 intégrations, mais la passerelle d’agents forme déjà une étoile à N

connexions. Le bus apporte ce que la passerelle n’offre pas : le découplage dans le temps, des abonnés que l’émetteur ignore et le rejeu. La gouvernance des sujets, des schémas et des contrats reste entière.

`EXIG-INT-10` **· DOIT**

**Choix de protocole justifié par la matrice**

Le protocole retenu pour chaque intégration **DOIT** être justifié dans la fiche d’agent par renvoi à une ligne du tableau 16. Un scénario absent de la matrice, ou un choix qui s’en écarte, **DOIT** être soumis à l’architecture d’entreprise avant la construction.

Pourquoi : la justification écrite rend le choix vérifiable en revue et alimente la mise à jour de la matrice.

`EXIG-INT-11` **· DEVRAIT**

**Diffusion d’un changement d’état par événement**

Lorsqu’un changement d’état intéresse plusieurs consommateurs, l’agent ou le système émetteur **DEVRAIT** publier un événement plutôt qu’appeler chaque consommateur par A2A ou par MCP, comme le prévoit l’EXIG-EVT-01.

Pourquoi : l’appel direct couple l’émetteur à chaque consommateur et propage leurs pannes; le bus absorbe les pointes et accepte de nouveaux abonnés sans modifier l’émetteur.

## 6.5 Intégration verticale : Model Context Protocol

Cette section fixe la manière dont l’entreprise relie ses agents à leurs outils, à leurs ressources et à leurs invites au moyen du Model Context Protocol (MCP), dans sa révision 2026-07-28. Elle distingue ce que la spécification exige de ce que le cadre ajoute pour exploiter le protocole à l’échelle de l’entreprise : passerelle d’agents, catalogue d’entreprise, autorisation obligatoire et contrôles de sécurité propres au protocole. Les règles générales de contrat et de versionnage sont à la section 6.8; l’identité et la délégation, au chapitre 9.

### Rôle et gouvernance du protocole

MCP normalise le lien vertical entre un agent et les systèmes qu’il consulte ou modifie. Au lieu d’écrire un connecteur pour chaque couple agent-système, on expose chaque système une seule fois par un serveur MCP, que tout agent conforme peut ensuite utiliser. Anthropic a annoncé MCP comme norme ouverte le 25 novembre 2024**[20]**. La formule « N × M » qui résume ce bénéfice (chapitre 2) est une vulgarisation, non un énoncé de la spécification.

Le 9 décembre 2025, Anthropic a donné MCP à l’Agentic AI Foundation (AAIF), fonds dirigé de la Linux Foundation cofondé par Anthropic, Block et OpenAI; MCP en est un projet fondateur, aux côtés de goose et d’AGENTS.md**[4, 193]**. Au lancement, les membres platine étaient Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft et OpenAI**[4]**. Le modèle de gouvernance technique est resté inchangé : des responsables principaux arbitrent l’évolution de la spécification, qui progresse par des propositions d’amélioration (SEP, *Specification Enhancement Proposals*), tandis que le conseil de l’AAIF gère la stratégie, le budget et les adhésions**[14]**. Depuis la révision 2026-07-28, une SEP prend la forme d’une demande de tirage versée au dépôt de la spécification; une extension officielle suit une filière distincte et exige au moins une implémentation de référence dans un SDK officiel**[168, 169]**. Selon les responsables du projet, on comptait en décembre 2025 10 000 serveurs actifs et plus de 97 millions de téléchargements mensuels des SDK**[14]**.

La spécification est versionnée par date : l’identifiant AAAA-MM-JJ correspond, selon la page Versioning de la spécification, au dernier changement incompatible qu’introduit la révision : c’est la date de sa publication, non celle du gel de sa version candidate. Les révisions publiées sont 2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25 et 2026-07-28, révision courante au 27 octobre 2026**[34, 168, 189]**. Cette dernière a été publiée le 28

juillet 2026, après une version candidate verrouillée le 21 mai 2026 et dix semaines de validation; les SDK TypeScript, Python, Go et C# la prenaient en charge dès sa sortie, le SDK Rust en version bêta**[33, 194]**. La feuille de route publiée le 22 août 2026 n’annonce aucune date pour la prochaine révision; la SEP-3398, acceptée le 14 octobre 2026 et versée au dépôt le 27 octobre, fixe deux publications par an et la reporte au 30 mars 2027, sous réserve du calendrier de transition (annexe H). Elle donne priorité à la messagerie agentique, à un transport natif HTTP (y compris pour les serveurs locaux), à l’identité des agents et à la sécurité d’entreprise (DPoP, fédération d’identité de charge de travail, ID-JAG, échange de jetons), à un contrat unique pour les résultats de `tools/call` et à la découverte progressive des outils**[195]**.

Le registre officiel MCP, lancé en préversion le 8 septembre 2025, l’est toujours selon sa documentation. Il n’héberge que des métadonnées qui renvoient aux paquets, authentifie les espaces de noms, délègue l’analyse de sécurité aux registres de paquets et ne prend pas en charge les serveurs privés; pour ceux-ci, il recommande d’héberger son propre registre MCP privé**[25, 43]**. Le catalogue d’entreprise est donc un composant distinct, sous la responsabilité de l’entreprise (section 6.8 et section 11.4).

`EXIG-MCP-01` **· DOIT**

**Exposition des capacités par MCP, derrière la passerelle**

Tout outil, toute ressource et toute invite mis à la disposition d’un agent **DOIVENT** l’être par un serveur MCP inscrit au catalogue d’entreprise et, dans tout environnement autre qu’un poste de développement individuel sans justificatif de production, publié derrière la passerelle d’agents, vers une version et une empreinte approuvées (sur ce poste, le serveur local obéit à l’EXIG-MCP-08). Seule en est dispensée la fonction locale de palier P0 ou P1 de l’EXIG-ARC-01, exécutée dans l’unité de déploiement de l’agent, sur les données de son propre domaine et inscrite au catalogue avec son palier; une action P2 ou P3 est toujours exposée comme outil MCP inscrit au catalogue. Un outil hébergé par le fournisseur de modèles n’est admis qu’au palier P0. Un hôte ne se connecte jamais directement à un serveur de domaine. Un format d’appel propriétaire n’est toléré que derrière un adaptateur, conformément au statut Contenir du catalogue des protocoles (section 6.3).

Pourquoi : un contrat unique, appliqué en un seul point, permet de filtrer, de journaliser et de révoquer l’accès sans modifier les agents.

`EXIG-MCP-02` **· DOIT**

**Révision de référence vérifiée par la découverte**

Tout serveur MCP mis en production après l’approbation du cadre **DOIT** mettre en œuvre la révision de référence épinglée au catalogue (valeur initiale : 2026-07-28), y compris la méthode `server/discover`. La révision prise en charge par chaque serveur est inscrite et épinglée au catalogue; la passerelle la vérifie par `server/discover` pour un serveur 2026-07-28, et par la réponse à `initialize` pour un serveur antérieur inscrit avec sa date de migration (EXIG-MCP-22), en contournant son propre cache (le résultat porte `ttlMs` et `cacheScope`), à l’homologation, à chaque déploiement et, pour un serveur de tiers, périodiquement, au plus tard à l’échéance de `ttlMs`, et refuse un serveur dont les versions ou capacités annoncées diffèrent de l’inscription.

Pourquoi : la spécification oblige tout serveur 2026-07-28 à implémenter `server/discover`, qui renvoie en une requête ses versions, ses capacités et son identité**[168]**; le catalogue dispose ainsi d’un relevé uniforme à comparer à l’inscription; ce relevé est déclaré par le serveur lui-même (`serverInfo` est auto-déclaré et ne devrait pas fonder une décision de sécurité) : il ne prouve ni l’identité ni l’intégrité du serveur.

### Architecture hôte-client-serveur et primitives

MCP suit une architecture client-serveur à trois rôles. L’hôte est l’application d’IA : un orchestrateur, un agent ou un poste de travail. Il crée un client MCP pour chaque serveur, et chaque client entretient

une connexion dédiée**[63]**. Le protocole comporte deux couches : une couche de données, faite d’échanges JSON-RPC 2.0 (découverte, primitives, notifications), et une couche de transport, qui règle la connexion, le tramage et l’autorisation**[63]**. Comme depuis la révision 2024-11-05, l’identifiant d’une requête ne peut pas être nul; en 2026-07-28, tout résultat porte en outre un champ `resultType`**[162]**.

Un serveur expose trois primitives : les outils, fonctions exécutables découvertes par `tools/list` et appelées par `tools/call` sous le contrôle du modèle; les ressources, données contextuelles identifiées par URI et lues par `resources/list` et `resources/read`; les invites, gabarits réutilisables obtenus par `prompts/list` et `prompts/get`**[63, 64]**. Côté client, l’élicitation, qui permet au serveur de demander une information ou une confirmation à la personne, demeure active; l’échantillonnage *(Sampling)* et les racines *(Roots)* sont dépréciés depuis 2026-07-28**[196]**.

Dans l’entreprise, la passerelle d’agents s’insère entre les hôtes et les serveurs (figure 7). Elle agit en mandataire inverse et applique à chaque requête les contrôles décrits à la section 9.4. Elle peut publier chaque serveur sous son propre point d’accès ou en agréger plusieurs derrière un point d’accès virtuel. Pour l’hôte, un point d’accès virtuel est un serveur : il y crée un seul client. Dans tous les cas, elle préfixe les noms d’outils par l’identifiant de leur serveur au catalogue (EXIG-MCP-20) : la spécification signale le risque de collision de noms et précise que le nom annoncé dans `serverInfo` n’est pas garanti unique**[197]**.

> **[Figure]**
> - Hôte MCP
> - agent, orchestrateur ou poste
> - Client MCP no 1
> - serveur CRM
> - Client MCP no 2
> - serveur ERP
> - Client MCP no 3
> - l’hôte applique le consentement,
> - l’approbation et les délais.
> - Streamable
> - HTTP + TLS
> - Passerelle d’agents
> - • valide le jeton (audience)
> - • compare en-têtes et corps
> - Mcp-Method, Mcp-Name
> - • filtre tools/list selon
> - les portées du jeton
> - • applique paliers P0–P3
> - • cache selon cacheScope
> - • propage traceparent
> - • bloque tout serveur
> - absent du catalogue
> - • journalise chaque appel
> - Serveur MCP de domaine
> - Outils
> - tools/call
> - Ressources
> - resources/read
> - Invites
> - prompts/get
> - Découverte : server/discover
> - Contrats : JSON Schema 2020-12
> - Erreurs métier : isError: true
> - État explicite par identifiant revalidé
> - InputRequiredResult elicitation
> - Extensions (activation explicite) :
> - API OpenAPI, bases de données, SaaS, ERP, CRM
> - Requête 2026-07-28 : autonome, sans session
> - serveur SGED
> - Un client par point d’accès;
> - Interaction humaine : tâches et élicitation
> - tasks · apps · auth (CIMD)
> - POST /mcp · MCP-Protocol-Version: 2026-07-28 · Mcp-Method: tools/call · Mcp-Name: approvisionnement_creer_bon_commande
> - Authorization: Bearer <jeton émis pour ce point d’accès de la passerelle>
> - {"jsonrpc":"2.0","id":42,"method":"tools/call","params":{"name":"approvisionnement_creer_bon_commande","arguments":{…},
> - • retire les clés _meta non admises
> - "_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","traceparent":"00-…"}}}
> - EMA : statut Évaluer, pilotes seulement (section 6.3)
> - →
> - →
> - →
> - →

***Figure 7 — MCP 2026-07-28 derrière la passerelle d’agents.** L’hôte crée un client par point d’accès MCP (serveur publié ou point d’accès virtuel); chaque requête, autonome et sans session, traverse la passerelle, qui vérifie le jeton, la concordance des en-têtes et du corps, le palier de l’outil et le catalogue avant de joindre le serveur de domaine. La requête illustrée est abrégée : une requête complète porte aussi `jsonrpc` et `id`, ainsi que les capacités du client dans `_meta`. La passerelle « ignore » les clés `_meta` non reconnues en les retirant (EXIG-MCP-16). L’extension d’autorisation EMA qui y figure est au statut Évaluer : pilotes seulement (section 6.3). Le jeton présenté à la passerelle lui est destiné; elle en obtient un second pour le serveur de domaine (section 9.3). Source : cadre CRE-IA-2026-01, d’après la spécification MCP 2026-07-28**[198]**.*

**Requête tools/call conforme à la révision 2026-07-28 (extrait)**

```
POST /mcp HTTP/1.1
Host: passerelle-agents.ent.ca
Content-Type: application/json
Accept: application/json, text/event-stream
Authorization: Bearer <jeton émis pour ce point d’accès de la passerelle>
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: approvisionnement_creer_bon_commande
Mcp-Param-Cost-Center: CC-4410
{"jsonrpc": "2.0", "id": 42, "method": "tools/call",
 "params": {
   "name": "approvisionnement_creer_bon_commande",
   "arguments": {"idempotency_key": "…", "centre_cout": "CC-4410", "…": "…"},
   "_meta": {
     "io.modelcontextprotocol/protocolVersion": "2026-07-28",
     "io.modelcontextprotocol/clientCapabilities": {"…": "…"},
     "traceparent": "00-…-…-01"}}}
```

Quatre traits ressortent. La requête se suffit à elle-même : aucun identifiant de session. Les en-têtes `Mcp-Method` et `Mcp-Name` recopient le corps pour permettre le routage sans l’analyser, d’où l’obligation de vérifier leur concordance (EXIG-MCP-15). Le jeton n’est valable que pour ce point d’accès de la passerelle (EXIG-MCP-11), qui obtient pour le serveur de domaine un second jeton par échange de jetons (section 9.3). Enfin, l’en-tête `Mcp-Param-Cost-Center` provient d’un argument marqué `x-mcp-header`; un centre de coûts s’y prête, une donnée sensible jamais (EXIG-MCP-18).

**À RETENIR**

Un serveur MCP est un adaptateur sans état cognitif : il expose des capacités à entrées et sorties définies et ne conduit pas la boucle de raisonnement de l’agent appelant. Le modèle propose d’utiliser un outil; la passerelle et le catalogue décident si l’appel est permis, à quelles conditions et sous quel jeton.

### Ce qui change avec la révision 2026-07-28

La révision 2026-07-28 rend le protocole sans état. Pour l’exploitation, c’est une simplification : tout nœud d’un parc peut traiter n’importe quelle requête, sans affinité de session, y compris sur une plateforme sans serveur**[162, 168]**. Pour la sécurité, le risque se déplace des sessions vers les identifiants d’état applicatifs et les nouveaux en-têtes. Le tableau 17 résume les changements et leur effet pour l’entreprise.

*Tableau 17 — Principaux changements de la révision MCP 2026-07-28 et effet pour l’entreprise*

| **Changement** | **Effet pour l’entreprise** |
| --- | --- |
| **Protocole sans état.** Retrait de la poignée de main `initialize`, des sessions protocolaires et de l’en-tête `Mcp-Session-Id` (SEP-2567, SEP-2575); chaque requête porte dans `_meta` sa version de protocole et les capacités du client**[162, 168]**. | À terme, après la migration (EXIG-MCP-22), plus de répartiteurs de charge à sessions persistantes *(sticky sessions)* ni de magasin de sessions partagé; pendant la coexistence, l’affinité ou le magasin de sessions est limité aux serveurs antérieurs inscrits, dont les `Mcp-Session-Id` suivent les règles de l’EXIG-MCP-17. L’état qui doit durer passe par un identifiant explicite émis par le serveur (EXIG-MCP-17). |
| **Découverte.** Méthode `server/discover`, obligatoire pour le serveur, facultative pour le client : versions prises en charge, capacités (extensions comprises) et identité, dans une réponse que l’on peut mettre en cache (`ttlMs` et `cacheScope`) **[168, 199]**. | Sonde d’inventaire et d’homologation; contrôle de cohérence avec le catalogue (EXIG-MCP-02). |
| **En-têtes de routage.** Chaque POST porte `Mcp-Method` et, pour `tools/call`, `resources/read` et `prompts/get`, `Mcp-Name` (SEP-2243); `MCP-Protocol-Version` doit égaler la valeur de `_meta`; tout écart entraîne HTTP 400 et l’erreur −32020 (`HeaderMismatch`)**[168, 190]**. | Routage et politiques possibles sans analyser le corps, à la condition expresse de vérifier la concordance (EXIG-MCP-15). |
| **Requêtes à allers-retours multiples (MRTR, SEP-2322).** Les requêtes initiées par le serveur (`roots/list`, `sampling/createMessage`, `elicitation/create`) cèdent la place à un résultat `InputRequiredResult`; le client relance la requête d’origine avec les réponses et un `requestState` opaque. MRTR s’applique à `tools/call`, `resources/read` et `prompts/get`**[200]**. | Une précision ou une décision humaine s’obtient sans flux ouvert de longue durée; le `requestState` devient une entrée non fiable à protéger (EXIG-MCP-17). La relance garde la clé d’idempotence et compte pour une seule opération au budget et à l’audit; un passage soldé par `input_required` ne consomme pas le jeton d’approbation (section 8.5). |
| **Indices de cache.** `ttlMs` et `cacheScope` obligatoires sur les résultats complets de `tools/list`, `prompts/list`, `resources/list`, `resources/templates/list`, `resources/read` (SEP-2549) et `server/discover`**[168, 201]**. | Cache de passerelle possible; un cache « private » n’est jamais partagé entre contextes d’autorisation (EXIG-MCP-03). |
| **Abonnements.** `subscriptions/listen` remplace le point d’accès GET et `resources/subscribe`; la reprise de flux par `Last-Event-ID` est retirée**[168, 190]**. | Notifications limitées aux types demandés par le client; les méthodes GET et DELETE ne servent plus. |
| **Extensions officielles.** Selon le journal des modifications de la révision 2026-07-28, les tâches longues quittent le cœur pour l’extension officielle `io.` `modelcontextprotocol/tasks` (SEP-2663); MCP Apps est une extension officielle; toute extension est désactivée par défaut et s’active explicitement des deux côtés**[168, 169, 191, 202]**. | Liste d’extensions autorisées au catalogue, quotas pour les tâches, revue des interfaces (EXIG-MCP-04). |
| **Schémas.** `inputSchema` et `outputSchema` acceptent tout mot-clé de JSON Schema 2020-12 (SEP-2106), dialecte par défaut; un autre dialecte peut être déclaré par `$schema`**[168, 197, 201]**. | Contrats plus expressifs; validateurs à durcir contre les références réseau (EXIG-MCP-19). |
| **Cycle de vie.** États *Active*, *Deprecated* et *Removed* (SEP-2596) : une fonctionnalité dépréciée reste dans la spécification au moins douze mois, ou au moins 90 jours en cas de retrait accéléré pour un risque de sécurité actif (avis de sécurité publié ou exploitation documentée)**[34, 196]**. | Migrations planifiées au catalogue, avec échéances (EXIG-MCP-22). |
| **Dépréciations et retraits.** Sont dépréciés Roots, Sampling, la journalisation protocolaire, l’enregistrement dynamique de clients (DCR), l’ancien transport HTTP+SSE et les valeurs `includeContext` « thisServer » et « allServers »; `ping`, `logging/setLevel` et `notifications/roots/list_changed` sont retirés directement, comme conséquences du passage sans état (SEP-2575) : la politique de cycle de vie, adoptée dans la même révision, ne vise pas ces retraits, et la journalisation protocolaire dépréciée n’a plus de réglage de niveau. Le retrait de Roots, de Sampling, de la journalisation et du DCR est possible à partir de la première révision publiée le 28 juillet 2027 ou après (celui d’`includeContext` suit Sampling; celui du transport HTTP+SSE, trois mois après que la SEP-2596 atteint l’état final, soit dès le début de septembre 2026, cette SEP étant finale depuis le 3 juin 2026 : annexe H)**[168, 196]**. | Paramètres d’outil ou URI de ressource au lieu de Roots; appels aux modèles par la passerelle de modèles au lieu de Sampling; sortie d’erreur standard ou OpenTelemetry au lieu de la journalisation protocolaire. |
| **Codes d’erreur.** « Ressource introuvable » passe de −32002 à −32602; la plage −32020 à −32099 est réservée à MCP, dont −32021 (capacité client requise absente) et −32022 (version non prise en charge)**[162, 168]**. | Clients tolérants aux deux codes pendant la transition; supervision des nouveaux codes. |

Une liste d’outils peut varier selon l’autorisation présentée, par exemple pour ne montrer que les outils permis par les portées du jeton, mais jamais selon la connexion ni par effet de bord d’autres requêtes; une liste qui dépend du jeton devrait alors porter `cacheScope` « private »**[197, 199]**.

`EXIG-MCP-03` **· DOIT**

**Listes stables et cache conforme à cacheScope**

Les serveurs MCP internes **DOIVENT** renvoyer leurs outils dans un ordre déterministe, identique d’une requête à l’autre tant que l’ensemble ne change pas; la passerelle qui agrège plusieurs serveurs fusionne leurs listes par identifiant de serveur, puis par nom, et conserve un ordre stable après filtrage. La passerelle **DOIT** respecter `ttlMs` et `cacheScope` : sa clé de cache inclut la méthode et les paramètres de la requête (curseur, URI) et, pour une réponse « private », le contexte d’autorisation, soit l’émetteur, le sujet, le client, l’audience et l’ensemble exact des portées du jeton; une réponse « private » n’est servie qu’à ce même contexte; seule une réponse « public » peut l’être par un cache partagé, ce qui ne dispense pas des contrôles d’accès par primitive; un résultat intermédiaire `input_required` et le résultat d’une relance MRTR (`inputResponses` ou `requestState`) ne sont jamais mis en cache. La passerelle **DOIT** évaluer la politique avant tout service depuis le cache, ne rien mettre en cache en l’absence de `cacheScope`, invalider les entrées d’un contexte à la révocation ou à la suspension de l’agent et à tout changement de portées et, à chaque rétablissement de `subscriptions/listen`, invalider les entrées du serveur et relire ses listes.

Pourquoi : la spécification recommande l’ordre déterministe pour améliorer le taux de succès du cache d’invites, et le cadre l’exige pour ses serveurs (section 10.6); elle interdit de partager un cache « private » entre contextes d’autorisation, ce qui réduit le risque de fuite entre locataires (la spécification précise que `cacheScope` ne remplace pas les contrôles d’accès propres à chaque primitive)**[197, 199, 201]**.

L’extension Tasks confie un travail long à un identifiant durable : le serveur renvoie un `taskId`, une durée de vie et un intervalle d’interrogation; le client suit l’avancement par `tasks/get`, fournit une entrée par `tasks/update` et peut annuler par `tasks/cancel`; les états sont `working`, `input_required`, `completed`, `failed` et `cancelled`**[191]**. Une tâche MCP ne remplace pas l’exécution durable de l’orchestrateur : celui-ci consigne le `taskId` dans son point de contrôle pour reprendre le suivi après une panne (section 7.4). Avec MCP Apps, un outil désigne dans `_meta.ui.resourceUri` une ressource `ui://`; l’hôte l’affiche dans une iframe cloisonnée qu’il contrôle, l’application ne dialogue avec lui que par `postMessage` et n’appelle des outils qu’à travers lui, et `_meta.ui.csp` et `_meta.ui.permissions` encadrent les origines et les permissions**[202]**.

`EXIG-MCP-04` **· DOIT**

**Extensions activées sur liste d’autorisation**

Une extension MCP **DOIT** figurer au catalogue pour le serveur concerné avant d’être activée. Les extensions internes portent le préfixe DNS inversé de l’entreprise, jamais un préfixe réservé (dont le deuxième libellé est `modelcontextprotocol` ou `mcp`). Pour l’extension Tasks, la passerelle impose un quota de tâches actives par mandant et une durée de vie maximale, et toute requête qui crée une tâche porte une clé d’idempotence, quel que soit le palier, afin qu’une panne survenue avant la consignation du `taskId` ne laisse pas de tâche orpheline (section 7.6). Pour MCP Apps, chaque gabarit `ui://` est revu avant l’homologation, l’empreinte de son contenu est épinglée au catalogue et vérifiée à chaque `resources/read` (un écart suspend le gabarit), et le contenu généré qu’il affiche est encodé; l’hôte applique la politique de sécurité du contenu et les permissions inscrites au catalogue, jamais celles de `_meta.ui`, que le serveur déclare.

Pourquoi : les extensions sont désactivées par défaut et s’identifient par un préfixe DNS inversé**[169]**; Akamai signale le déni de service par tâches asynchrones et le script intersites stocké par les interfaces générées**[203]**. La revue préalable des gabarits est une exigence du cadre, que la documentation officielle n’énonce pas.

### Règles d’usage des primitives

Chaque primitive répond à un besoin distinct. Une **ressource** convient quand on sait quelle entité charger : `crm://comptes/9482/sommaire` est déclarée sans effet par le serveur, classée au catalogue comme une lecture (palier P0 ou P1) et se met en cache selon `ttlMs`. Un **outil** convient aux recherches dynamiques, aux calculs et aux écritures, sous un contrat d’entrée strict. Une **invite** publie une procédure normalisée d’un domaine, par exemple la vérification d’un nouveau fournisseur, pour que chaque agent n’ait pas à la réécrire; elle se gère comme la mémoire procédurale, c’est-à-dire comme du code versionné et revu (section 5.5).

La granularité compte autant que le choix de la primitive. Un serveur qui recopie une API de soixante opérations en soixante outils encombre le contexte du modèle et multiplie les occasions de choisir le mauvais outil ou le mauvais paramètre. Un outil `approvisionnement_creer_bon_commande` , qui valide en une seule opération le fournisseur, le centre de coûts et les lignes, se gouverne mieux et se teste plus facilement. Les équipes ne réécrivent pas leurs services REST : des adaptateurs de composition traduisent les opérations OpenAPI pertinentes en outils orientés tâche, qui valident les règles métier (section 5.2 et EXIG-MCP-06).

Lorsque les outils deviennent nombreux, les bonnes pratiques de MCP recommandent à l’hôte, au-delà d’un seuil de l’ordre de 1 à 5 % de la fenêtre de contexte, d’offrir un méta-outil de recherche et de ne charger les définitions complètes qu’au besoin, en les ajoutant après le point de rupture du cache plutôt qu’en

réordonnant la liste**[204]**. Anthropic illustre, par un exemple de plus de 50 outils MCP, que sa propre fonction de recherche d’outils ramène la consommation totale de contexte d’environ 77 000 jetons (dont environ 72 000 pour les seules définitions) à environ 8 700; elle chiffre cette réduction à 85 % (les deux chiffres donnent plutôt près de 89 %)**[205]**. Le choix entre la recherche d’outils et le découpage en plusieurs agents est traité à la section 7.3.

`EXIG-MCP-05` **· DEVRAIT**

**Choix de la primitive selon le besoin**

La lecture d’une entité connue **DEVRAIT** être exposée comme ressource adressée par URI; une recherche, un calcul ou une écriture, comme outil; une procédure normalisée de domaine, comme invite versionnée et revue au même titre que du code. Une ressource ou un gabarit de ressource reçoit au catalogue un palier P0 ou P1, comme un outil de lecture : la passerelle doit appliquer à `resources/read` les contrôles de ce palier, le masquage et le balisage du contenu non fiable (section 9.6). Lorsque l’hôte n’offre pas au modèle la lecture de ressources, un outil de lecture adossé à la ressource la remplace.

Pourquoi : la ressource, déclarée sans effet par le serveur et classée au catalogue, se met en cache, mais une lecture sensible reste une lecture sensible; la spécification laisse en outre à l’application hôte le choix des ressources qu’elle fournit au modèle; l’outil porte un contrat d’entrée strict et passe par les contrôles de palier; l’invite rend une procédure réutilisable sans la recopier dans chaque agent.

`EXIG-MCP-06` **· NE DOIT PAS**

**Aucun miroir CRUD des API**

Un serveur MCP **NE DOIT PAS** exposer une API en recopiant une à une ses opérations élémentaires de création, de lecture, de mise à jour et de suppression. Il expose des outils qui accomplissent des tâches métier complètes et valident eux-mêmes leurs paramètres. Critère de revue : aucun outil d’écriture dont le contrat se réduit à une opération unique de l’API, sans validation métier.

Pourquoi : chaque définition d’outil consomme du contexte et chaque outil de plus est une occasion d’erreur de sélection; une intention métier se classe au catalogue et s’approuve plus clairement qu’une opération technique.

`EXIG-MCP-07` **· DOIT**

**Conventions de nommage et de résultat des outils**

Les outils des serveurs internes **DOIVENT** : porter un nom de 1 à 96 caractères ASCII (lettres, chiffres, `_`, `-`, `.`) préfixé par leur domaine, la marge jusqu’aux 128 caractères de la spécification étant réservée au préfixe de serveur que pose la passerelle (EXIG-MCP-20); renvoyer les erreurs de validation et les erreurs métier comme résultat d’outil marqué `isError: true`, en réservant les erreurs JSON-RPC aux outils inconnus, aux requêtes malformées et aux erreurs du serveur; déclarer un `outputSchema` lorsque leur résultat alimente une étape suivante, puis renvoyer un `structuredContent` conforme, accompagné du même JSON sérialisé dans un bloc texte. Un outil qui renvoie aussi des erreurs structurées les décrit dans son `outputSchema` (union du succès et de l’erreur), et l’hôte ne transmet au modèle qu’une des deux formes du résultat.

Pourquoi : le modèle peut corriger une erreur renvoyée comme résultat, alors qu’une erreur de protocole interrompt l’appel; la spécification exige un `structuredContent` conforme dès qu’un `outputSchema` est déclaré et recommande le bloc texte pour la rétrocompatibilité**[197]**. Exemple complet à l’annexe C.

### Transport et autorisation

MCP définit deux transports normalisés : stdio, entre processus d’une même machine, et Streamable HTTP, qui a remplacé le transport HTTP+SSE en 2025-03-26**[206, 207]**. En 2026-07-28, chaque message du client est un POST distinct vers un point d’accès unique; le serveur répond soit par un objet JSON, soit par un flux

SSE propre à cette requête (que le serveur devrait clore dès que la réponse JSON-RPC finale est envoyée), et le client doit accepter les deux. Le serveur doit valider l’en-tête `Origin` sur toute connexion entrante pour contrer les attaques par réassociation DNS *(DNS rebinding)*, et répondre par HTTP 403 si l’en-tête est présent et invalide; un serveur local devrait n’écouter que sur 127.0.0.1, et tout serveur devrait authentifier les connexions**[190]**. Les bonnes pratiques de sécurité de MCP recommandent d’ailleurs stdio pour limiter l’accès à un serveur local**[208]** : restreindre stdio au poste de développement est donc un choix d’exploitation du cadre, non une exigence de MCP.

`EXIG-MCP-08` **· DOIT**

**Transport selon l’environnement**

Dans tout environnement autre qu’un poste de développement individuel sans justificatif de production (environnement serveur, tableau 7), un serveur MCP **DOIT** être exposé par Streamable HTTP, derrière la passerelle d’agents, sur TLS : TLS 1.3 négocié lorsque le pair le permet, TLS 1.2 au minimum, versions antérieures désactivées. Sur un tel poste, et là seulement, un serveur local est permis, installé depuis le catalogue et exécuté dans un bac à sable aux privilèges minimaux; l’hôte affiche la commande complète avant l’installation et exige une approbation explicite. Ce serveur local emploie stdio ou, en Streamable HTTP, **DOIT** n’écouter que sur l’adresse de bouclage, valider l’en-tête `Origin` et exiger une authentification.

Pourquoi : seul un transport réseau passe par la passerelle, donc par l’identité, la politique et la journalisation; les bonnes pratiques de sécurité de MCP exigent l’affichage de la commande et l’approbation explicite pour l’installation en un clic d’un serveur local, et recommandent son exécution en bac à sable**[208]**.

L’autorisation est *facultative* dans MCP; lorsqu’elle est offerte sur HTTP, elle devrait suivre la spécification d’autorisation, fondée sur le brouillon OAuth 2.1 dans sa version −13, que la spécification MCP cite encore (la version −16 était la plus récente au 27 octobre 2026, et la −17 a paru le 31 octobre 2026; voir la section 6.3) **[209, 210]**. Le serveur MCP y est un serveur de ressources OAuth. Il doit publier ses métadonnées de ressource protégée (RFC 9728), que le client utilise pour découvrir le serveur d’autorisation, et ce dernier doit offrir la découverte RFC 8414 ou OpenID Connect**[211]**. Le client doit inclure le paramètre `resource` (RFC 8707), valant l’URI canonique du serveur MCP, dans ses requêtes d’autorisation et de jeton; le serveur doit vérifier que le jeton lui est destiné et répondre 401 sinon**[71]**. Le jeton circule dans l’en-tête `Authorization: Bearer` de chaque requête, jamais dans l’URL; PKCE s’emploie avec la méthode S256. Depuis 2026-07-28, le serveur d’autorisation devrait renvoyer le paramètre `iss` (RFC 9207), que le client doit valider s’il est présent (et rejeter la réponse s’il est absent alors que les métadonnées annoncent son support)**[209, 212]**. Comme OAuth 2.1 reste un brouillon, le cadre se réfère à OAuth 2.0 profilé par la RFC 9700 (section 9.3).

La spécification prescrit des jetons porteurs; elle n’exige ni mTLS ni DPoP, ni durée de vie précise, et l’intégration de DPoP (RFC 9449) au profil d’autorisation MCP ne figure qu’à sa feuille de route**[195, 209]**. Les jetons liés à l’expéditeur *(sender-constrained)* (RFC 9449 ou RFC 8705), appuyés sur la RFC 9700**[175, 213]**, et les durées de vie courtes sont donc des politiques du cadre. Lorsque la passerelle publie un serveur, l’URI canonique annoncée aux clients est la sienne; elle obtient ensuite, pour le serveur de domaine, un jeton distinct par échange de jetons (section 9.3). Ce choix du cadre respecte l’interdiction du passage de jeton.

`EXIG-MCP-09` **· DOIT**

**Autorisation obligatoire et conforme à la spécification**

Tout serveur MCP, hormis un serveur local en stdio sur un poste de développement (EXIG-MCP-08), **DOIT** exiger une autorisation OAuth conforme à la spécification MCP de la révision de référence épinglée au catalogue (valeur initiale : 2026-07-28) : métadonnées de ressource protégée (RFC 9728),

indicateur de ressource (RFC 8707) portant l’URI canonique, vérification de l’audience à chaque requête et jeton transmis uniquement par l’en-tête `Authorization`. Chaque serveur publié séparément a sa propre URI canonique; en mode agrégé, les portées sont préfixées par l’identifiant du serveur au catalogue, et la passerelle vérifie que chaque appel vise un serveur couvert par les portées du jeton. Les clients MCP de l’entreprise **DOIVENT** employer PKCE avec S256 (en vérifiant que les métadonnées du serveur d’autorisation annoncent `code_challenge_methods_supported` et en refusant de poursuivre sinon) et, avant d’échanger le code d’autorisation, valider `iss` (RFC 9207) s’il est présent, rejeter la réponse qui en est dépourvue alors que les métadonnées du serveur d’autorisation annoncent son support et, face à un serveur d’autorisation qui ne l’annonce pas, employer une `redirect_uri` distincte par serveur d’autorisation et vérifier l’émetteur attendu pour la transaction (RFC 9700). Les serveurs d’autorisation de l’entreprise **DOIVENT** publier ces annonces et toujours émettre `iss` (avec `authorization_response_` `iss_parameter_supported: true` ).

Pourquoi : la spécification laisse l’autorisation facultative**[209]**; le cadre la rend obligatoire, car un outil sans contrôle d’accès ouvre directement les systèmes d’enregistrement, et l’émission de `iss` protège contre la confusion entre serveurs d’autorisation.

`EXIG-MCP-10` **· DOIT**

**Portées minimales et élévation progressive**

Chaque serveur MCP **DOIT** publier un ensemble initial minimal de portées (`scopes_supported`), refuser les portées génériques (`*`, `all`, `full-access`) et signaler une portée insuffisante par une réponse 403 `insufficient_scope` qui énumère les portées requises. Chaque élévation progressive *(step-up)* est journalisée avec l’identifiant de trace, et le client en limite le nombre de tentatives.

Pourquoi : un agent démarre avec le minimum et n’obtient davantage que sur une demande traçable; c’est le patron de minimisation des portées que décrivent la spécification et ses bonnes pratiques de sécurité**[208, 209]**.

`EXIG-MCP-11` **· NE DOIT PAS**

**Interdiction du passage de jeton**

Un serveur MCP, la passerelle comprise, **NE DOIT PAS** accepter un jeton qui n’a pas été émis pour lui, ni retransmettre en aval un jeton reçu, sauf au serveur d’autorisation, à titre de `subject_token` d’un échange de jetons (EXIG-IAM-12, qui fait foi). Pour appeler une API ou un autre serveur, il obtient son propre jeton, à audience unique, par échange de jetons (section 9.3).

Pourquoi : la spécification interdit explicitement le passage de jeton *(token passthrough)***[208, 209]**; un jeton relayé permettrait à un serveur compromis d’agir partout où ce jeton est valable.

Pour identifier un client, la spécification recommande l’ordre suivant : enregistrement préalable, puis document de métadonnées d’identifiant client (CIMD) si le serveur d’autorisation l’annonce, puis enregistrement dynamique (DCR) en repli, puis saisie manuelle**[214]**. Les CIMD, dont l’identifiant client est une URL HTTPS, ont été ajoutés en 2025-11-25; le DCR (RFC 7591) a été déprécié en 2026-07-28**[168, 215]**. Le brouillon CIMD, adopté par le groupe de travail OAuth de l’IETF mais qui n’est pas une RFC, interdit au client l’authentification par secret partagé, n’admet que des clés publiques, interdit au serveur de suivre automatiquement les redirections, lui fait refuser les adresses à usage spécial et recommande de limiter la lecture à environ 5 Ko (état de la version −02; la spécification MCP 2026-07-28 renvoie à la version −00)**[216]**. Un identifiant préenregistré ou obtenu par DCR est lié à l’émetteur qui l’a délivré : si l’émetteur change, le client se réenregistre**[214]**.

`EXIG-MCP-12` **· DOIT**

**Enregistrement des clients MCP**

Les clients MCP de l’entreprise **DOIVENT** être préenregistrés auprès du serveur d’autorisation ou, pour un serveur d’autorisation tiers qui annonce la prise en charge des CIMD, identifiés par un CIMD. Le DCR ne doit pas être activé pour une nouvelle intégration (EXIG-MCP-22); si le serveur d’autorisation tiers n’offre ni préenregistrement ni CIMD, l’intégration exige une dérogation. Un serveur d’autorisation de l’entreprise qui accepte des CIMD **DOIT** refuser l’authentification par secret partagé, ne suivre aucune redirection (règle du brouillon CIMD, plus stricte que l’EXIG-SEC-12), appliquer pour le reste la règle de sortie réseau de l’EXIG-SEC-12 et borner la taille du document lu.

Pourquoi : le DCR est déprécié et voué au retrait**[196]**; la récupération d’un CIMD expose le serveur d’autorisation à la falsification de requêtes côté serveur (SSRF), que les règles du brouillon préviennent**[216]**.

`EXIG-MCP-13` **· DOIT**

**Consentement par client des mandataires MCP**

Un serveur MCP qui sert de mandataire auprès d’un serveur d’autorisation tiers avec un identifiant client statique **DOIT** obtenir le consentement de l’utilisateur pour chaque client avant de relayer l’autorisation : registre des `client_id` approuvés par utilisateur; page de consentement qui nomme le client, les portées et l’URI de redirection; protection contre la falsification de requête intersites et contre le détournement de clic par incrustation *(clickjacking)*, notamment par `frame-ancestors`; correspondance exacte de `redirect_uri`; paramètre `state` aléatoire, à usage unique, fixé seulement après le consentement; témoins `__Host-` marqués `Secure`, `HttpOnly` et `SameSite=Lax`.

Pourquoi : sans ce consentement, un client malveillant profite d’un consentement donné antérieurement au mandataire; c’est le problème de l’adjoint confus *(confused deputy)*, que la spécification traite par ces mesures obligatoires**[208]**.

Deux extensions officielles d’autorisation, stables depuis la révision 2026-07-28, complètent le cœur du protocole**[217]**. Avec Enterprise-Managed Authorization (EMA), le fournisseur d’identité de l’entreprise décide de l’accès : après l’authentification unique, le client obtient un ID-JAG par échange de jetons (RFC 8693), puis l’échange contre un jeton d’accès par l’octroi JWT bearer (RFC 7523)**[178]**. EMA évite un consentement par serveur et par employé et centralise les politiques d’accès et la révocation**[178]**; comme le brouillon ID-JAG qui la fonde**[177]**, elle figure au statut Évaluer du catalogue (section 6.3). L’extension OAuth Client Credentials couvre les agents qui agissent sans utilisateur; un tel agent s’authentifie sous sa propre identité (section 9.2). Enfin, l’échange de jetons RFC 8693 et la revendication `act` ne font pas partie du cœur de MCP : exiger d’un fournisseur la propagation de la chaîne de délégation relève d’une clause contractuelle (chapitre 13), non d’une conformité MCP.

### Annotations et métadonnées de gouvernance

La spécification prévoit pour chaque outil des annotations : `title`, `readOnlyHint` (faux par défaut), `destructiveHint` (vrai par défaut), `idempotentHint` (faux par défaut) et `openWorldHint` (vrai par défaut); `destructiveHint` et `idempotentHint` n’ont de sens que si l’outil n’est pas en lecture seule. Ce sont des indices : les clients doivent les tenir pour non fiables, sauf s’ils proviennent de serveurs de confiance, et, selon une formulation non normative (« should never »), ne jamais fonder une décision d’usage sur les annotations d’un serveur non fiable**[197, 201]**. Les valeurs par défaut sont prudentes : un outil qui ne déclare rien est présumé destructif et ouvert sur l’extérieur.

L’objet `annotations` ne définit que cinq champs standard et aucune propriété d’extension; la spécification réserve `_meta` aux extensions. Les ébauches qui y ajoutaient des champs `x-enterprise-*` sortaient donc de ce que prévoit la spécification (le cadre en fait une règle, EXIG-MCP-14)**[201]**. Une métadonnée propre

à l’entreprise peut figurer dans le champ `_meta` de l’outil, sous une clé à préfixe DNS inversé détenu par l’entreprise (p. ex. `ca.ent/palier-risque`); déclarée par le serveur, elle n’est pas plus fiable qu’une annotation.

**ATTENTION**

Une annotation `readOnlyHint: true` ne prouve rien : c’est le serveur qui l’affirme. Un serveur compromis ou mal configuré peut déclarer en lecture seule un outil qui supprime des données. Le palier P0 à P3 d’un outil est attribué au catalogue après revue (section 8.3) et appliqué par la passerelle.

`EXIG-MCP-14` **· DOIT**

**Annotations et métadonnées déclarées : de simples indices**

La passerelle et les hôtes **DOIVENT** lire le palier de risque, le seuil d’approbation et l’outil de compensation d’un outil ou d’un gabarit de ressource dans son entrée au catalogue, jamais dans ses annotations ni dans son `_meta`. Les serveurs internes **DOIVENT** néanmoins déclarer leurs annotations, qui **DOIVENT** concorder avec la classification du catalogue : `readOnlyHint` vrai pour un outil P0 ou P1 et faux pour un outil P2 ou P3; `idempotentHint` vrai seulement si une clé d’idempotence est déclarée au catalogue. Un écart **DOIT** bloquer l’homologation; les autres indices relèvent de la revue. Aucune propriété propre à l’entreprise n’est ajoutée à l’objet `annotations`.

Pourquoi : la spécification tient les annotations pour des indices non fiables**[197]**; elles servent l’ergonomie (affichage, demande de confirmation), non la décision de sécurité. L’entrée de catalogue type figure à l’annexe C.

### Sécurité propre à MCP

À terme, après la migration (EXIG-MCP-22), le passage au protocole sans état supprime le détournement d’identifiant de session, que les serveurs antérieurs gardent pendant la coexistence, mais il déplace le risque vers les identifiants d’état applicatifs et le `requestState`, que le serveur doit traiter comme une entrée contrôlée par l’attaquant**[200, 208]**. L’analyse, publiée par Akamai le 25 juin 2026, de la version candidate relève notamment le détournement de flux entre agents par des identifiants ou des objets d’état prévisibles, la manipulation du champ `_meta` contrôlé par le client, la désynchronisation des en-têtes et du corps, la fuite de données par `x-mcp-header`, le script intersites stocké par MCP Apps et le déni de service par tâches asynchrones**[203]**. La spécification contient déjà l’essentiel des contre-mesures; les exigences qui suivent s’y appuient. Les menaces communes à tous les agents, comme l’injection d’instructions et l’exécution de code, sont traitées aux sections 9.5 à 9.7.

**EXEMPLE : LA DÉSYNCHRONISATION**

Une requête porte l’en-tête `Mcp-Name: recherche_publique`, mais son corps appelle `supprimer_base`. Un pare-feu applicatif qui ne lit que l’en-tête laisse passer, et le serveur exécute l’outil destructeur. La spécification ferme cette brèche en obligeant tout serveur qui traite le corps à rejeter l’écart; le cadre ajoute que la passerelle décide d’après le corps analysé, jamais d’après les seuls en-têtes.

`EXIG-MCP-15` **· DOIT**

**Concordance des en-têtes et du corps**

La passerelle et chaque serveur **DOIVENT** vérifier que `MCP-Protocol-Version`, `Mcp-Method`, `Mcp-Name` et chaque en-tête `Mcp-Param-{nom}` (après décodage Base64 éventuel) concordent avec le corps JSON-RPC et sa clé `_meta`, et rejeter par HTTP 400 et l’erreur −32020 toute divergence, ainsi que l’absence de tout en-tête obligatoire selon la révision inscrite au catalogue pour le serveur visé, et non

selon celle que déclare l’appelant. La passerelle fonde ses décisions d’autorisation sur le corps analysé; une politique fondée sur les en-têtes ne s’applique qu’aux requêtes d’une révision qui les définit (2026-07-28 ou une révision ultérieure épinglée au catalogue).

Pourquoi : la spécification impose ce rejet à tout serveur qui traite le corps et recommande à un intermédiaire dont la politique repose sur ces en-têtes de rejeter les requêtes d’une révision antérieure, qui n’imposait pas cette validation**[190]**.

Dans MCP, le code HTTP 403 signale un en-tête `Origin` invalide (transport) ou des portées invalides ou des permissions insuffisantes (autorisation); une divergence d’en-têtes relève du code 400**[190, 209]**. Le champ `_meta`, lui, ne peut pas être purgé en bloc : les clés `io.modelcontextprotocol/protocolVersion` et `io.` `modelcontextprotocol/clientCapabilities` y sont obligatoires, sous peine de rejet par l’erreur −32602, et les clés `traceparent`, `tracestate` et `baggage` y transportent le contexte de trace selon W3C Trace Context et W3C Baggage (SEP-414)**[162, 168]**. Les conventions OpenTelemetry pour MCP, au niveau Development, nomment les *spans* d’après la méthode appelée (attribut `mcp.method.name`)**[386]**; leur emploi est réglé à la section 10.1. Un serveur ne se fie pas non plus à une capacité que le client n’a pas déclarée : il renvoie alors l’erreur −32021**[162]**.

`EXIG-MCP-16` **· DOIT**

**Traitement du champ _meta**

La passerelle et les serveurs **DOIVENT** conserver les clés réservées de `_meta`, soit celles du préfixe `io.modelcontextprotocol/` selon la révision inscrite au catalogue (version de protocole, capacités du client, `clientInfo`, `serverInfo`, `logLevel` et `subscriptionId`, qui marque les notifications de `subscriptions/listen`), ainsi que `traceparent` et `tracestate`, filtrer `baggage` par liste d’autorisation à chaque frontière de confiance, retirer toute autre clé absente de la liste des clés admises que le catalogue tient pour chaque serveur et ne fonder aucun routage, aucun choix de locataire ni aucune autorisation sur `_meta`, `clientInfo` ou `serverInfo`. L’identité du mandant provient exclusivement du jeton vérifié, par exemple de sa revendication `sub`.

Pourquoi : `clientInfo` et `serverInfo` sont auto-déclarés et ne devraient pas servir aux décisions de sécurité**[162]**; Akamai illustre l’élévation de privilèges qu’obtient un attaquant lorsqu’un serveur se fie à `{"tenant": "admin", "authenticated": true}` placé dans `_meta`**[203]**.

`EXIG-MCP-17` **· DOIT**

**État explicite protégé**

Un serveur qui conserve un état entre deux appels **DOIT** émettre des identifiants d’état aléatoires, imprévisibles et à durée de vie bornée, d’au moins 128 bits d’entropie, liés côté serveur à l’utilisateur authentifié (clé formée de l’émetteur et du sujet du jeton vérifié, `iss` et `sub`, et de l’identifiant, sérialisée sans ambiguïté); la possession d’un identifiant ne vaut jamais authentification. Il **DOIT** traiter tout `requestState` reçu comme une entrée contrôlée par un attaquant et, dès que cet état influence l’autorisation, l’accès aux ressources ou la logique métier, en protéger l’intégrité par HMAC ou par chiffrement authentifié (AEAD), sous une clé propre au serveur, y inclure le mandant, l’identifiant du serveur et de l’outil, une courte durée de vie et l’empreinte de la requête d’origine. Toute étape qui porte une approbation ou une écriture P2 ou P3 est à usage unique : le serveur tient un registre des états consommés, partagé par toutes ses répliques et conservé pendant la durée de vie de l’état, et une relance qui présente le même `requestState` pour la même requête renvoie le résultat mémorisé, sans nouvel effet.

Pourquoi : la spécification impose de traiter tout `requestState` comme une entrée contrôlée par un attaquant, d’en protéger l’intégrité (HMAC ou AEAD) dès qu’il influence l’autorisation, l’accès aux ressources ou la logique métier, et de faire respecter l’usage unique côté serveur quand il est requis; elle ne fait que recommander l’inclusion du mandant, d’une courte durée de vie et de l’empreinte de la requête d’origine, et n’offre qu’une orientation non normative sur les identifiants d’état aléatoires liés à l’utilisateur (durcissement du cadre)**[197, 200]**; sans ces mesures, un identifiant deviné permet d’accéder à l’état d’un autre utilisateur, et un état rejoué par un autre mandant n’est rejeté que si le serveur l’a lié au mandant**[200, 208]**.

La directive `x-mcp-header` recopie un argument d’outil dans un en-tête `Mcp-Param-{nom}`. Elle ne s’applique qu’à des types primitifs (chaîne, entier, booléen, à l’exclusion de `number`), à une propriété atteignable statiquement et sous un nom unique; un client Streamable HTTP doit écarter de `tools/list` tout outil dont la directive est invalide**[190, 197]**.

`EXIG-MCP-18` **· NE DOIT PAS**

**Aucune donnée sensible en en-tête**

La directive `x-mcp-header` **NE DOIT PAS** marquer une propriété qui contient un secret (mot de passe, clé d’API, jeton), un renseignement personnel ou toute autre donnée confidentielle. Elle est réservée aux valeurs utiles au routage ou à l’imputation, comme un centre de coûts; la passerelle et les hôtes doivent écarter de `tools/list` tout outil dont une propriété marquée `x-mcp-header` n’est pas inscrite au catalogue comme projection autorisée, ce qui couvre les serveurs de tiers; pour les serveurs internes, l’analyse des schémas en intégration continue complète ce contrôle.

Pourquoi : les en-têtes sont visibles des intermédiaires (répartiteurs de charge, passerelles, outils d’observabilité); la spécification recommande de ne pas y marquer de paramètres sensibles**[190, 197]**, et le cadre en fait une interdiction.

`EXIG-MCP-19` **· DOIT**

**Schémas, URL et icônes : des entrées non fiables**

Les hôtes, les clients hébergés et la passerelle **DOIVENT** traiter comme non fiables les schémas, URL et icônes fournis par un serveur. Concrètement : ne jamais déréférencer automatiquement un `$ref` pointant vers une URI réseau et borner la profondeur et le nombre de sous-schémas; lors de la découverte OAuth, n’accepter que HTTPS et appliquer la règle de sortie réseau de l’EXIG-SEC-12, un serveur d’autorisation interne légitime étant atteint par son entrée de catalogue, jamais par une URL fournie; n’ouvrir une URL d’autorisation que si son schéma est `https` (`http` en bouclage, pour le développement seulement), jamais par un interpréteur de commandes; n’accepter qu’une icône matricielle (PNG, WebP ou JPEG) dont le type est validé par signature binaire, en `https`, de même origine que le serveur et récupérée sans identifiants, ou en `data:`; une icône SVG, format textuel qu’aucune signature binaire ne qualifie, est rendue en image matricielle avant tout affichage, ou refusée.

Pourquoi : un serveur malveillant peut se servir d’un schéma pour un déni de service, de la découverte OAuth pour une SSRF vers les métadonnées infonuagiques ou les services internes, d’une URL ou d’une icône SVG pour exécuter du code**[162, 208]**.

Trois attaques visent les définitions d’outils elles-mêmes. L’**empoisonnement d’outil** *(tool poisoning)* cache des instructions malveillantes dans une description, un schéma ou une valeur de retour. La **substitution après approbation** *(rug pull)* modifie les définitions d’un serveur une fois celui-ci approuvé. L’**ombrage** *(tool shadowing)* laisse la description d’un serveur malveillant modifier l’usage des outils d’un autre serveur. Invariant Labs a décrit les trois le 1er avril 2025, et la fiche de sécurité MCP de l’OWASP les reprend avec l’injection par valeurs de retour**[220, 221]**. Cette fiche recommande de traiter chaque serveur comme un domaine de sécurité indépendant et non fiable, et rappelle que la signature des messages ne fait

pas partie du cœur de MCP**[221]**. L’épinglage au catalogue est réglé à la section 6.8; l’exigence suivante en vérifie la définition à l’exécution. Le comportement du serveur, que la définition ne transporte pas, relève de la signature des artefacts déployés et de la provenance (section 9.8), du contrôle des sorties réseau et des tests de contrat.

`EXIG-MCP-20` **· DOIT**

**Empreintes des définitions et isolement des serveurs**

À l’homologation, à chaque `tools/list` et, avant l’exécution, sur la définition du dernier `tools/list` non périmé (`ttlMs`, EXIG-MCP-03; la liste est relue si l’entrée est périmée), la passerelle **DOIT** calculer l’empreinte de chaque définition d’outil, soit le SHA-256 de sa canonisation RFC 8785 sur le périmètre de la définition publiée fixé par l’EXIG-INT-13 (icônes hachées par leur contenu, champs volatils de `_meta` inscrits au catalogue exclus), et la comparer à l’empreinte épinglée au catalogue; un outil dont l’empreinte diffère est retiré de la liste remise à l’agent et suspendu jusqu’à une nouvelle approbation, et la version entière du serveur l’est au-delà d’un nombre d’écarts inscrit au catalogue (l’EXIG-SEC-18 fait foi pour la suspension). Cette empreinte atteste la définition reçue, non le comportement du serveur. La passerelle **DOIT** traiter chaque serveur comme un domaine de sécurité distinct : elle préfixe tout outil remis à l’agent par l’identifiant de son serveur au catalogue, au moyen d’un séparateur admis dans les noms d’outils mais interdit dans ces identifiants, refuse toute collision de noms et réécrit de façon cohérente le corps et l’en-tête `Mcp-Name`; le catalogue indexe palier et empreinte sur le couple (serveur, nom d’origine); la revue d’homologation recherche dans les descriptions toute mention d’outils ou de serveurs tiers; la sortie de tout outil est une donnée non fiable (section 9.6).

Pourquoi : l’OWASP recommande d’épingler les définitions par empreinte, de les revérifier avant l’exécution et de redemander le consentement lorsqu’elles changent**[221]**; l’empoisonnement d’outil est le risque MCP03 de l’OWASP MCP Top 10**[222]**.

Lorsque l’hôte fait exécuter par le modèle du code qui appelle des outils (« mode code »), ce code s’exécute dans un bac à sable sans accès réseau direct; l’hôte, qui détient les identifiants, applique à chaque appel la même politique d’approbation qu’à un appel direct, et les résultats d’un serveur restent non fiables pour un autre**[204]**. Les exigences de cloisonnement figurent à la section 9.7.

L’élicitation reste le canal par lequel un serveur sollicite une personne, désormais à l’intérieur d’un `InputRequiredResult`. Elle offre deux modes : « form », pour des données structurées selon un schéma plat de types primitifs, et « url », pour une interaction hors bande. Le client doit indiquer quel serveur demande l’information, offrir le refus et l’annulation, afficher l’URL complète et obtenir le consentement avant de l’ouvrir. En mode URL, le serveur ne place ni renseignement sensible ni URL préauthentifiée dans l’URL, vérifie que la personne qui l’ouvre est celle qui a déclenché la demande, et les identifiants tiers ainsi obtenus ne transitent jamais par le client MCP**[223]**.

`EXIG-MCP-21` **· NE DOIT PAS**

**Élicitation : ni secret ni approbation déguisée**

Un serveur **NE DOIT PAS** demander de secret (mot de passe, clé d’API, jeton, donnée de paiement) par élicitation en mode formulaire; ces cas passent par le mode URL. Une réponse d’élicitation **NE DOIT PAS** non plus tenir lieu d’approbation humaine pour une action qui en exige une (toute action pour laquelle le contrôle calculé selon l’EXIG-AUT-10 exige une approbation) : seule compte l’approbation signée, liée à l’action exacte, décrite à la section 8.5. L’hôte doit avertir l’utilisateur, ou refuser la demande, lorsqu’une élicitation en mode formulaire comporte un champ de format `password` ou dont le nom évoque un secret.

Pourquoi : la spécification interdit les secrets en mode formulaire**[223]**; le brouillon IETF WIMSE AIMS précise qu’une confirmation locale dans l’interface ne suffit pas comme autorisation**[93]**.

Le projet OWASP MCP Top 10, édition 2025 encore en phase bêta, fournit une grille de menaces commune**[222]**. Le tableau 18 la met en correspondance avec les exigences du cadre; cette correspondance est une interprétation interne, qui nomme les exigences qui traitent chaque risque sans prétendre le couvrir entièrement. Pour l’analyse de menaces par phase, Hou et coll. décrivent le cycle de vie d’un serveur MCP en quatre phases (création, déploiement, exploitation, maintenance) et seize scénarios de menace répartis entre quatre types d’attaquants**[224]**.

*Tableau 18 — Correspondance entre l’OWASP MCP Top 10 (bêta) et les exigences du cadre*

| **Risque OWASP MCP Top 10 (2025, bêta)** | **Exigences et sections du cadre** |
| --- | --- |
| MCP01 Gestion des jetons et exposition de secrets | EXIG-MCP-11, EXIG-MCP-18, EXIG-MCP-21; section 9.2 |
| MCP02 Élévation de privilèges par dérive des portées | EXIG-MCP-10; section 9.3 |
| MCP03 Empoisonnement d’outil | EXIG-MCP-14, EXIG-MCP-20, EXIG-SEC-18 |
| MCP04 Chaîne d’approvisionnement | EXIG-MCP-20, EXIG-SEC-18; section 9.8 |
| MCP05 Injection et exécution de commandes | EXIG-MCP-08, EXIG-MCP-19; section 9.7 |
| MCP06 Injection d’invite par charges contextuelles | EXIG-MCP-20; section 9.6 |
| MCP07 Authentification et autorisation insuffisantes | EXIG-MCP-09, EXIG-MCP-12, EXIG-MCP-13 |
| MCP08 Absence d’audit et de télémétrie | EXIG-MCP-10; EXIG-OBS-01 et section 10.3 (journal d’audit) |
| MCP09 Serveurs MCP fantômes | EXIG-MCP-01, EXIG-MCP-02; section 11.4 |
| MCP10 Injection de contexte et surpartage | EXIG-MCP-03, EXIG-MCP-16, EXIG-MCP-17 |

### Migration vers la révision 2026-07-28

Les deux générations du protocole coexisteront pendant un temps. Un client peut détecter la génération d’un serveur en tentant une requête moderne et en examinant l’erreur 400 éventuelle avant de revenir à `initialize`; un client de l’entreprise ne revient jamais à `initialize` pour un serveur inscrit au catalogue en 2026-07-28, et la sonde ne sert qu’à l’inventaire et au développement. Sur stdio, `server/discover` sert de sonde de rétrocompatibilité. Un serveur qui ne connaît que 2026-07-28 devrait répondre 405 aux requêtes GET et DELETE et ignorer les en-têtes `Mcp-Session-Id` et `Last-Event-ID`**[168, 190]**; une version non prise en charge entraîne l’erreur −32022**[162]**. La migration se fait en sept étapes.

1. Inventorier les serveurs et les clients et inscrire leur révision au catalogue : `server/discover` pour les serveurs à jour, réponse à `initialize` pour les autres.
2. Ouvrir à la passerelle une double prise en charge bornée : les requêtes 2026-07-28 sont validées par en-têtes et par corps; les requêtes antérieures ne sont acceptées que pour les serveurs inscrits avec une date de migration et sont contrôlées par inspection du corps.
3. Remplacer l’état de session par des identifiants explicites (EXIG-MCP-17) et les requêtes initiées par le serveur par MRTR.
4. Remplacer Sampling par des appels à la passerelle de modèles, Roots par des paramètres d’outil ou des URI de ressource, et la journalisation protocolaire par la sortie d’erreur standard ou OpenTelemetry (section 10.1).
5. Remplacer le DCR par le préenregistrement ou les CIMD (EXIG-MCP-12).
6. Faire passer les tests de contrat et de conformité (section 6.8). Le cadre officiel de tests de conformité MCP reste en préversion (versions 0.x : 0.1.16 courante, 0.2.0-alpha.12 publiée le 1er octobre 2026) : il suit le régime des suites de conformité de l’EXIG-INT-19 et complète les tests internes sans les remplacer**[225, 226]**.

7. Retirer de la passerelle la prise en charge de la révision antérieure à l’échéance fixée.

`EXIG-MCP-22` **· DOIT**

**Migration bornée et abandon des fonctions dépréciées**

Pendant une période de coexistence bornée, la passerelle **DOIT** accepter la génération antérieure de MCP pour les seuls serveurs inscrits au catalogue avec une date de migration, et la refuser pour tout autre. Tous les serveurs et clients en production **DOIVENT** avoir migré vers la révision 2026-07-28 ou vers une révision ultérieure épinglée au catalogue au plus tard le 28 juillet 2027, échéance du cadre qui ne change que par une révision (section 1.6). Un nouveau développement ne doit pas s’appuyer sur une fonction dépréciée (Roots, Sampling, journalisation protocolaire, DCR, transport HTTP+SSE), et toute intégration en production **DOIT** avoir cessé de les employer à la même échéance. Pendant la transition, un client traite −32002 (serveurs antérieurs) comme « ressource introuvable » en réponse à `resources/read`; il ne traite −32602 ainsi que si `error.data` le désigne comme tel, sinon comme une erreur de paramètres, et journalise tout −32602 avec l’identifiant de trace.

Pourquoi : Roots, Sampling, la journalisation et le DCR deviennent admissibles au retrait à partir de la première révision publiée le 28 juillet 2027 ou après (le transport HTTP+SSE obéit à une échéance distincte : trois mois après que la SEP-2596 atteint l’état final, soit dès le début de septembre 2026, cette SEP étant finale depuis le 3 juin 2026, annexe H)**[196]**. L’échéance retenue, choix du cadre, vise à la fois le changement de génération et l’abandon des fonctions dépréciées, deux opérations distinctes : migrer vers 2026-07-28 ne retire pas Sampling d’une intégration. Elle précède la première révision qui pourrait retirer Roots, Sampling, la journalisation et le DCR, celle de la fin de septembre 2027 si le calendrier de la SEP-3398 est tenu (annexe H). Pour le transport HTTP+SSE, elle suit au contraire la première révision qui peut le retirer (celle du 30 mars 2027 si la SEP-3398 est tenue) : le cadre assume cet écart, qui expose un client ou un serveur encore sur ce transport à une rupture dès cette révision, et l’annexe H le renvoie au comité. La spécification recommande aux clients d’accepter aussi −32002, code employé par les versions antérieures pour « ressource introuvable »**[227]**.

## 6.6 Intégration horizontale : protocole Agent2Agent

Cette section fixe les règles d’usage du protocole Agent2Agent (A2A), qui relie un agent à un autre agent lorsque l’appelant délègue un sous-objectif complet sans connaître le fonctionnement interne de l’appelé. MCP (section 6.5) relie un agent à des outils dont les entrées et les sorties sont définies; A2A relie des agents autonomes, potentiellement opaques, qui raisonnent et conservent un état sur des échanges à plusieurs tours**[39]**. Le cadre retient la version de protocole 1.0 (publication 1.0.0 du 12 mars 2026, correctif 1.0.1 du 28 mai 2026)**[30]**.

### Rôle, historique et gouvernance

Google a annoncé A2A le 9 avril 2025 avec plus de 50 partenaires**[21]**, puis l’a confié à la Linux Foundation le 23 juin 2025**[22]**. La version 0.3.0 (30 juillet 2025) a ajouté gRPC et les cartes d’agent signées, et renommé en `agent-card.json` le chemin de découverte**[228, 229]**. L’Agent Communication Protocol (ACP) d’IBM Research a fusionné avec A2A à la fin d’août 2025 : fusion annoncée le 25 août, dépôt archivé le 27 août, annonce de la fondation LF AI & Data (Linux Foundation) le 29 août**[24, 230]**. La version 1.0.0, première version stable, a paru le 12 mars 2026**[29]**. A2A est devenu un projet de stade « Growth » de l’Agentic AI Foundation (AAIF), transfert annoncé le 17 août 2026 et confirmé par le billet du projet du 27 août 2026**[5, 35]**. La chronologie d’ensemble figure à la section 2.2.

Trois faits fondent le choix d’A2A comme protocole agent-agent par défaut. Sa gouvernance est neutre : un comité directeur technique de neuf sièges le pilote : les huit entreprises de la composition annoncée le 12 mars 2026 (AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP et ServiceNow)**[29]**, et Bloomberg depuis le 20 octobre 2026 (erratum, annexe H), sous l’égide de la fondation qui héberge aussi MCP. Son adoption est large : plus de 150 organisations le soutiennent (Linux Foundation, 9 avril 2026), et Microsoft

et AWS l’ont intégré à leurs plateformes d’agents**[15]**. Son outillage est ouvert : six SDK officiels (Python, JavaScript, Java, Go, .NET et Rust), une trousse de compatibilité (`a2a-tck`), un inspecteur et une interface en ligne de commande**[231, 232]**.

**ATTENTION : AU MOINS QUATRE PROTOCOLES « ACP »**

Le sigle désigne au moins quatre protocoles : (1) l’Agent Communication Protocol d’IBM, fusionné dans A2A; (2) l’Agent Connect Protocol d’AGNTCY, dont le dépôt est archivé depuis le 11 avril 2026; (3) l’Agent Client Protocol, créé par Zed pour relier les éditeurs de code aux agents de codage; (4) l’Agentic Commerce Protocol d’OpenAI et de Stripe**[183, 233, 234]**. Toute offre qui invoque un « ACP » pour coordonner des agents se vérifie au regard de ces sens; la liste n’est pas exhaustive.

`EXIG-A2A-01` **· DOIT**

**A2A 1.0 pour toute délégation entre agents**

Toute délégation à un agent d’un autre domaine, d’un autre cadriciel, d’un tiers ou d’un autre processus **DOIT** utiliser A2A, dans la version de protocole épinglée au catalogue (valeur initiale : 1.0), sauf pendant la coexistence bornée de l’EXIG-A2A-15. Un protocole agent-agent propriétaire **DOIT** être contenu derrière un adaptateur, conformément au catalogue (section 6.3). Seuls les transferts entre sous-agents d’un même orchestrateur, dans un même processus, en sont exemptés (EXIG-INT-05). Une cible est un agent si elle choisit elle-même, au moyen d’un modèle, les actions qu’elle exécute; sinon c’est un outil, même si elle conserve l’état d’une tâche ou demande une précision (extension Tasks, élicitation MCP).

Pourquoi : un contrat d’échange unique évite une intégration ad hoc par paire d’agents et garde l’agent appelé remplaçable.

### Carte d’agent 1.0

La carte d’agent *(Agent Card)* est le contrat public d’un agent : un document JSON qui dit qui il est, ce qu’il sait faire, où le joindre et comment s’authentifier. Un agent exposé la publie à `https://{domaine}/.` `well-known/agent-card.json` , URI unique par nom d’hôte : chaque agent exposé reçoit donc son propre nom d’hôte (p. ex. `risque-credit.agents.ent.ca`), à défaut de quoi le champ `tenant` distingue les agents d’un même point d’accès; l’ancien chemin `/.well-known/agent.json` appartient aux versions 0.1 et 0.2, désormais obsolètes**[30, 68]**. La définition normative des objets est le fichier `a2a.proto`, sérialisé en ProtoJSON; les énumérations s’écrivent en majuscules préfixées, par exemple `TASK_STATE_WORKING`**[68]**. Le tableau 19 résume les champs et les règles du cadre; un exemple complet figure à l’annexe C.

*Tableau 19 — Champs de la carte d’agent A2A 1.0 et règles du cadre*

| **Champ** | **Statut dans A2A 1.0** | **Règle du cadre** |
| --- | --- | --- |
| `name`, `description` | Obligatoires | Nom identique à la fiche du registre; description qui dit ce que fait l’agent et ce qu’il ne fait pas. |
| `supportedInterfaces` | Obligatoire; liste ordonnée, la première entrée est préférée; chaque entrée exige `url`, `protocolBinding` et `protocolVersion`, `tenant` est facultatif | Adresses de la passerelle d’agents, jamais l’adresse directe de l’agent (cartes des agents de l’entreprise et cartes de façade des agents de tiers, EXIG-A2A-02). |
| `version` | Obligatoire; format libre | SemVer *(versionnage sémantique; voir la section 6.8)*, incrémentée à chaque changement publié; l’`ETag` dérive du hachage de la représentation servie (EXIG-A2A-04). |
| `capabilities` | Obligatoire; sous-champs facultatifs `streaming`, `pushNotifications`, `extensions`, `extendedAgentCard` | Déclarer le comportement réel; extensions approuvées seulement. |
| `defaultInputModes`, `defaultOutputModes` | Obligatoires | Types média effectivement acceptés et produits. |
| `skills` | Obligatoire; chaque compétence exige `id`, `name`, `description` et `tags` | `id` stable, en minuscules séparées par des traits d’union (*kebab-case*, convention du cadre); une portée OAuth par compétence. |
| `securitySchemes`, `securityRequirements` | Facultatifs; aucun secret dans la carte | Obligatoires; renvoient au fournisseur d’identité de l’entreprise (pour une carte de façade, celui qu’emploie la passerelle). |
| `signatures` | Facultatif | Obligatoire : signature JWS *(JSON Web Signature)* sur la carte canonisée. |
| `provider`, `documentationUrl`, `iconUrl` | Facultatifs | `provider` renseigné par la direction responsable. |

Sources : spécification A2A 1.0 et `a2a.proto`**[192, 235]**; règles : choix du cadre.

**Signature.** La carte peut être signée en JWS (RFC 7515)**[474]** après canonisation JCS *(JSON Canonicalization Scheme)*, le champ `signatures` étant exclu du contenu signé; la spécification recommande au client de vérifier au moins une signature avant de faire confiance à la carte et interdit de vérifier avec une clé expirée ou révoquée**[68, 236]**. Le cadre rend la signature obligatoire : une carte non signée s’imite aussi facilement qu’une page web.

**Carte étendue.** La capacité `extendedAgentCard` active l’opération `GetExtendedAgentCard`, qui exige une authentification et vérifie les permissions du client; la carte étendue ne devrait pas contenir d’information sensible exploitable en cas de fuite**[68]**. On publie ainsi une carte publique minimale et l’on réserve les compétences internes aux clients autorisés.

**Découverte et cache.** La spécification admet trois modes de découverte : URI bien connue, registre organisé (sans API de registre normalisée) et configuration directe; l’accès aux cartes peut être restreint par mTLS, filtrage réseau ou OAuth**[237]**. Dans l’entreprise, la découverte passe par le catalogue d’entreprise, auquel renvoie la fiche de l’agent au registre (section 11.4; EXIG-INT-17). Le guide de découverte recommande un en-tête `Cache-Control`, un `ETag` dérivé du champ `version` ou d’un hachage, et des requêtes conditionnelles (`If-None-Match`)**[237]**. Comme la spécification n’impose pas SemVer pour `version`**[68]**, le cadre l’impose : sans incrément fiable, un client garderait en cache une carte périmée.

**Métadonnées de gouvernance.** La carte 1.0 n’a pas de champ libre au premier niveau, et une extension ne peut pas modifier les structures de base**[192, 238]**. Le niveau d’autonomie, la classe de risque, le centre de coûts et la classification maximale des données restent donc à la fiche du registre (annexe B). Si un pair doit les lire, ils se déclarent comme extension de données dans les `capabilities.extensions` de la carte étendue seulement, jamais dans la carte publique (EXIG-A2A-06). Une extension y figure avec son URI, qui porte la version, une description, l’indicateur `required` et ses paramètres; elle s’active par l’en-tête `A2A-Extensions`, un changement incompatible exige une nouvelle URI, et aucune extension ne doit contourner les contrôles de sécurité de l’agent**[238]**.

`EXIG-A2A-02` **· DOIT**

**Carte publiée et inscrite au catalogue**

Tout agent invocable par d’autres agents **DOIT** publier une carte conforme à A2A 1.0 et aux règles du tableau 19, l’inscrire au catalogue d’entreprise (et la rattacher à sa fiche au registre, section 11.4) et déclarer dans `supportedInterfaces` les adresses de la passerelle d’agents. Un agent exposé hors de l’entreprise **DOIT** aussi publier sa carte à l’URI bien connue; un agent interne ne la publie pas : la carte inscrite au catalogue est sa carte de référence, servie par la passerelle, et la fiche du registre y

renvoie. Pour un agent de tiers, le catalogue conserve la carte d’origine, signée par le tiers et vérifiée à l’homologation, avec son empreinte; la passerelle sert aux agents de l’entreprise une carte de façade, qui porte ses propres adresses, est signée par une clé de l’entreprise et référence l’empreinte de la carte d’origine. Aucun client de l’entreprise ne suit les `supportedInterfaces` d’une carte d’origine.

Pourquoi : la découverte passe par une source contrôlée, et aucun appel ne contourne la passerelle (section 9.4).

`EXIG-A2A-03` **· DOIT**

**Carte signée et vérifiée**

Toute carte inscrite au catalogue d’entreprise **DOIT** porter au moins une signature JWS valide, calculée sur la carte canonisée JCS avec une clé de l’émetteur de la carte (clé gérée par l’entreprise pour ses propres agents et pour les cartes de façade; pour la carte d’origine d’un agent de tiers, clé dont le catalogue consigne la confiance). La règle vaut aussi pour la carte étendue. La passerelle d’agents et les clients **DOIVENT** rejeter une carte sans signature valide ou signée par une clé expirée ou révoquée, rejeter un `jku` ou un `kid` absent du catalogue et refuser une carte de version inférieure à la dernière qu’ils ont vue. Pour les clients externes, l’entreprise publie son jeu de clés (JWKS) sur son domaine principal. La carte ne doit pas contenir de secret.

Pourquoi : une carte usurpée détournerait des tâches et des données vers un faux agent, risque que l’OWASP classe sous ASI07, communication interagents non sécurisée**[28]**.

`EXIG-A2A-04` **· DOIT**

**Version de carte et revalidation du cache**

Le champ `version` de la carte **DOIT** suivre SemVer et être incrémenté à chaque changement publié (règle du cadre). Le serveur qui sert la carte (l’URI bien connue pour un agent exposé, la passerelle pour une carte de référence ou de façade) **DOIT** fournir un `ETag` fort, dérivé du hachage de la représentation servie, signatures comprises, et un `Cache-Control`; une nouvelle signature est un changement publié; le catalogue et les clients **DOIVENT** revalider leur copie par requête conditionnelle. Les règles de compatibilité et de coexistence des versions sont celles de la section 6.8.

Pourquoi : le hachage change dès qu’un octet de la carte change, signatures comprises, ce qu’un numéro de version ne garantit pas; un 304 ne peut donc pas prolonger une carte signée par une clé révoquée (le guide de découverte admet un ETag dérivé d’un hachage). SemVer reste le signal de compatibilité (section 6.8).

`EXIG-A2A-05` **· NE DOIT PAS**

**Aucun champ hors norme dans la carte**

Une carte **NE DOIT PAS** contenir de champ non défini par A2A 1.0, par exemple `x-enterprise-governance`. Une extension **NE DOIT PAS** être publiée sauf si son URI figure au catalogue d’entreprise parmi les extensions approuvées, après revue de sécurité; l’indicateur `required: true` doit recevoir une dérogation du comité d’architecture et des risques agentiques (EXIG-APP-02).

Pourquoi : un champ hors norme n’a aucune sémantique garantie chez les pairs, et une extension obligatoire exclut tout client qui ne la prend pas en charge (erreur `ExtensionSupportRequiredError`)**[68]**.

`EXIG-A2A-06` **· DOIT**

**Compétences internes dans la carte étendue**

Pour un agent exposé hors de l’entreprise, les compétences réservées à des consommateurs internes **DOIVENT** être publiées dans la carte étendue, servie par `GetExtendedAgentCard` après authentification et contrôle des permissions, et la carte publique se limite aux compétences destinées aux appelants

externes. La carte d’un agent interne, servie aux seuls clients authentifiés (EXIG-A2A-02), porte toutes ses compétences. L’extension de gouvernance ne figure que dans la carte étendue.

Pourquoi : la carte publique est lisible par tous; elle ne doit pas cartographier la surface interne de l’entreprise.

### Tâches, messages et artefacts

A2A organise le travail en tâches *(Task)*. Le client envoie un message; le serveur crée la tâche et lui attribue son identifiant, le client ne pouvant pas en imposer un pour une nouvelle tâche (un réessai de `SendMessage` peut donc créer une seconde tâche, d’où la règle de l’EXIG-A2A-07); `contextId` regroupe les tâches et les messages d’une même interaction**[68]**. Les messages et les artefacts, c’est-à-dire les résultats produits par la tâche, se composent de parties *(Part)*. En 1.0, une partie porte exactement un des membres `text`, `raw` (octets encodés en base64), `url` ou `data` (JSON structuré), avec `mediaType`, `filename` et `metadata` facultatifs; elle remplace les anciens `TextPart`, `FilePart` et `DataPart`**[192, 235]**.

Une tâche suit une machine à huit états réels (neuf valeurs d’énumération avec la valeur zéro, figure 8). Deux états sont actifs (`SUBMITTED`, `WORKING`); deux sont interrompus : `INPUT_REQUIRED` quand l’agent attend une précision ou une approbation, `AUTH_REQUIRED` quand il lui faut un justificatif supplémentaire; quatre sont terminaux (`COMPLETED`, `FAILED`, `CANCELED`, `REJECTED`); la valeur zéro `TASK_STATE_UNSPECIFIED` ne désigne aucun état réel**[192]**. Une tâche terminale n’accepte plus de message (`UnsupportedOperationError`) et ne peut plus être annulée (`TaskNotCancelableError`)**[68]**. Les graphies minuscules comme `input-required` appartiennent aux versions 0.x et ne s’emploient plus.

> **[Figure]**
> - ÉTATS ACTIFS ÉTATS INTERROMPUS ÉTATS TERMINAUX
> - TASK_STATE_
> - SUBMITTED
> - TASK_STATE_
> - WORKING
> - TASK_STATE_ INPUT_REQUIRED
> - précision ou approbation
> - TASK_STATE_ AUTH_REQUIRED
> - justificatif supplémentaire
> - TASK_STATE_COMPLETED
> - TASK_STATE_FAILED
> - TASK_STATE_CANCELED
> - TASK_STATE_REJECTED
> - fin de traitement
> - l’agent distant refuse la tâche
> - Un message vers une tâche terminale renvoie UnsupportedOperationError; annuler une tâche terminale renvoie TaskNotCancelableError. Valeur zéro : TASK_STATE_UNSPECIFIED.

***Figure 8 — Cycle de vie d’une tâche A2A 1.0.** Une tâche passe de soumise à en cours, peut s’interrompre pour obtenir une précision, une approbation ou un justificatif, puis aboutit à l’un des quatre états terminaux, après lesquels elle n’accepte plus de message. Les traits pleins montrent la progression nominale; les pointillés, le retour d’un état interrompu vers l’exécution, l’annulation et le refus de la tâche par l’agent distant. Source : A2A Project, `a2a.proto`, version de protocole 1.0.*

Le protocole définit les opérations `SendMessage`, `SendStreamingMessage`, `GetTask`, `ListTasks`, `CancelTask`, `SubscribeToTask`, `GetExtendedAgentCard` et quatre opérations de gestion des configurations de notification push. Par défaut, `SendMessage` attend que la tâche atteigne un état terminal ou interrompu; avec `returnImmediately: true`, il rend la main dès la création de la tâche. `ListTasks` pagine par curseur et omet les artefacts par défaut, ce qui convient aux tableaux de bord d’exploitation**[68]**. Le client suit une tâche longue de trois façons : interrogation périodique (`GetTask`), flux en continu (SSE ou gRPC) ou notifications push**[29, 68]**. Dans la liaison HTTP+JSON, une erreur prend la forme d’un `google.rpc.Status` accompagné d’un `google.rpc.ErrorInfo` du domaine `a2a-protocol.org`**[68]**.

`EXIG-A2A-07` **· DOIT**

**Suivi des tâches longues**

Lorsque la durée attendue d’une tâche, déclarée par compétence au catalogue (95e centile mesuré), dépasse 5 secondes (seuil fixé par le cadre), le client **DOIT** la suivre par flux en continu (`SendStreamingMessage`) ou par notification push, y compris pour le message qui relance une tâche interrompue; un flux ouvert porte des battements de cœur. L’interrogation par `GetTask` peut servir à rétablir le suivi après une coupure, mais ne doit pas servir au suivi courant; la reprise par `SubscribeToTask` est permise après une coupure ou un état interrompu. Avant de réessayer un envoi dont la réponse s’est perdue, le client **DOIT** rechercher une tâche existante par `contextId` et par identifiant de message (`messageId`), et l’agent serveur **DOIT** rattacher à la tâche existante un message déjà reçu. Un délai maximal, inscrit au catalogue, borne les états `INPUT_REQUIRED` et `AUTH_REQUIRED`; à son terme, le serveur clôt la tâche dans un état terminal.

Pourquoi : une connexion bloquante longue se heurte aux délais des intermédiaires réseau, et une boucle d’interrogation consomme sans rien apprendre; la spécification laisse ce choix au client, d’où cette règle interne. La spécification permet à l’agent de détecter un message en double par son `messageId` sans l’y obliger**[68]**; le cadre l’impose, pour que la clé d’idempotence de l’agent appelé reste stable d’un essai à l’autre (section 7.6).

### Liaisons, versions et sécurité

A2A 1.0 définit trois liaisons standard dérivées d’un même modèle abstrait : JSON-RPC 2.0 sur HTTP(S), gRPC sur HTTP/2 avec TLS, et HTTP+JSON (REST), dont le JSON est structurellement équivalent aux définitions Protobuf. La spécification exige d’un agent qui offre plusieurs liaisons une équivalence fonctionnelle (mêmes opérations, résultats sémantiquement équivalents, mêmes erreurs, mêmes schémas d’authentification), et d’une liaison personnalisée un comportement cohérent avec les opérations abstraites**[68]**. Le cadre retient JSON-RPC comme liaison commune, car certaines passerelles ne relaient que celle-là : Azure API Management, par exemple, n’importe les API d’agents A2A qu’en JSON-RPC**[109]**. La liaison SLIMRPC d’AGNTCY est expérimentale et ne fait pas partie des liaisons standard**[239]** (section 6.9).

Chaque requête porte l’en-tête `A2A-Version` au format majeur.mineur (p. ex. `1.0`), ou le paramètre de requête équivalent. Un en-tête vide est interprété comme la version 0.3 (la spécification ne dit rien de l’en-tête absent, que le cadre assimile à un en-tête vide), et un agent qui ne prend pas en charge la version demandée renvoie `VersionNotSupportedError`**[68]** : un client 1.0 qui omet l’en-tête échoue donc contre un serveur 1.0 strict. Le type média `application/a2a+json` est recommandé pour la seule liaison HTTP+JSON; JSON-RPC emploie `application/json`, les flux `text/event-stream` et gRPC Protobuf**[68]**.

Pour la sécurité, la spécification pose les bases et le cadre les durcit. La sécurité de transport est obligatoire en production; la spécification recommande TLS 1.3, et le guide d’implémentation en entreprise admet TLS 1.2 ou plus**[68, 161]**. L’identité relève de la couche transport : les justificatifs s’obtiennent hors bande et voyagent dans les en-têtes HTTP; le serveur authentifie chaque requête (401 si le justificatif manque ou est invalide, 403 s’il est insuffisant) et autorise avant toute opération susceptible de divulguer de l’information. L’autorisation peut se faire par compétence, chaque `AgentSkill` pouvant porter ses propres exigences de sécurité**[161, 192]**. La version 1.0 retire les flux OAuth implicite et par mot de passe, et ajoute le flux Device Code et PKCE**[30]**. Le champ `tenant` permet à un point d’accès d’héberger plusieurs agents ou locataires, les résultats devant rester dans le périmètre autorisé de l’appelant. Enfin, l’agent valide tous ses paramètres d’entrée, limite la taille des messages et des fichiers, et ne journalise ni justificatifs ni renseignements personnels sans protection**[68]**.

Les notifications push demandent une attention particulière : c’est l’agent serveur qui appelle une URL fournie par le client, un point de rappel HTTP *(webhook)*, ce qui en fait une cible de SSRF. La spécification exige que l’agent joigne les justificatifs prévus par la configuration et tente au moins une livraison; elle

recommande un délai d’expiration de 10 à 30 secondes, des reprises avec repli exponentiel et le rejet des URL visant `127.0.0.0/8`, `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `localhost` ou une adresse lien-local. Le récepteur doit valider l’authenticité de la notification et répondre par un code 2xx; il devrait vérifier que la tâche signalée est l’une des siennes. La livraison est tentée « au moins une fois », sans garantie de succès (reprises facultatives) et avec des doublons possibles, d’où un traitement idempotent**[68]**.

`EXIG-A2A-08` **· DOIT**

**Version annoncée et liaisons standard**

Tout client A2A **DOIT** envoyer `A2A-Version` à chaque requête, sauf un client 0.3 pendant la période de l’EXIG-A2A-15. Tout agent **DOIT** exposer la liaison JSON-RPC et peut ajouter gRPC ou HTTP+JSON lorsque la passerelle d’agents les prend en charge, à condition d’offrir par chaque liaison les mêmes opérations, les mêmes erreurs et les mêmes schémas d’authentification. Une liaison non standard, dont SLIMRPC, ne sert pas en production; elle n’est employée qu’en essai hors production, sans données réelles, conformément à son statut Surveiller au catalogue (EXIG-INT-06).

Pourquoi : la version explicite évite les replis silencieux vers 0.3, et une liaison commune garde chaque agent joignable par toutes les plateformes retenues.

`EXIG-A2A-09` **· DOIT**

**Transport chiffré et authentification à chaque requête**

Tout échange A2A **DOIT** négocier TLS 1.3 lorsque le pair le permet, TLS 1.2 au minimum, versions antérieures désactivées, avec validation des certificats, transiter par la passerelle d’agents et être authentifié à chaque requête. L’agent serveur **DOIT** autoriser avant toute opération qui lit ou divulgue de l’information, valider ses paramètres et borner la taille des messages et des fichiers. Un message ou une tâche A2A reçu est une source de contexte au sens de l’EXIG-SEC-03 et porte les étiquettes de la session qui l’a produit (EXIG-SEC-04).

Pourquoi : la passerelle applique au trafic entre agents les contrôles déjà appliqués aux outils; la documentation A2A recommande fortement une solution de gestion d’API pour les agents exposés**[161]**.

`EXIG-A2A-10` **· DOIT**

**Autorisation par compétence et par locataire**

Chaque compétence publiée **DOIT** être associée à une portée OAuth dédiée, déclarée dans ses `securityRequirements` et inscrite au catalogue. L’appelant **DOIT** présenter à la passerelle un jeton délégué dont l’audience est la passerelle, à l’adresse publiée dans `supportedInterfaces`; la passerelle en obtient par échange un second, à audience unique, pour l’agent appelé (section 9.3, EXIG-IAM-12 et IAM-14). Comme un message A2A s’adresse à l’agent, la compétence visée **DOIT** être désignée par une métadonnée d’une extension approuvée (EXIG-A2A-05), que la passerelle vérifie contre la portée du jeton, et l’agent serveur **DOIT** router de façon déterministe vers cette seule compétence; à défaut, chaque compétence a son propre point d’accès. Lorsqu’un point d’accès sert plusieurs locataires, la passerelle **DOIT** vérifier que le `tenant` demandé figure parmi les locataires que le jeton autorise.

Pourquoi : le moindre privilège s’applique à la compétence, pas à l’agent entier; un jeton valide pour analyser un dossier ne doit pas permettre d’accorder un prêt.

`EXIG-A2A-11` **· NE DOIT PAS**

**Flux OAuth permis et flux retirés**

Les agents et leurs clients **NE DOIVENT PAS** employer l’octroi implicite ni l’octroi par mot de passe. Ils doivent utiliser le code d’autorisation avec PKCE (ou le Device Code pour un appareil sans navigateur,

réservé aux clients inscrits au catalogue, sous accès conditionnel et avec une durée de code courte) quand une personne s’authentifie, les justificatifs client, authentifiés par mTLS, `private_key_jwt` ou SVID et jamais par secret partagé, pour un agent qui agit en son nom propre et, pour la délégation, l’échange de jetons de la RFC 8693.

Pourquoi : A2A 1.0 a retiré ces flux**[30, 235]**, et la RFC 9700 interdit l’octroi par mot de passe et déconseille l’octroi implicite**[175]**. Les flux permis sont ceux du profil de la RFC 9700**[175]** et de l’échange de jetons de la RFC 8693**[69]**.

`EXIG-A2A-12` **· DOIT**

**Notifications push durcies**

Le cadre rend obligatoires les recommandations de la spécification. L’agent serveur **DOIT** appliquer à l’URL de webhook, à l’enregistrement et à chaque livraison, la règle de sortie réseau de l’EXIG-SEC-12, sortir par la passerelle d’agents ou par le mandataire de sortie, appliquer un délai d’expiration compris entre 10 et 30 secondes et des reprises à repli exponentiel, bornées en nombre et en durée au catalogue. Un récepteur interne légitime, comme un orchestrateur de l’entreprise, est atteint par son entrée de catalogue, jamais par l’URL fournie. Le récepteur **DOIT** authentifier la notification, vérifier que l’identifiant de tâche lui appartient et traiter chaque notification de façon idempotente.

Pourquoi : un webhook non filtré permet à un client malveillant de faire sonder le réseau interne par l’agent.

`EXIG-A2A-13` **· DOIT**

**Traçage et corrélation des tâches**

Chaque appel A2A **DOIT** propager l’en-tête W3C `traceparent` et être tracé côté appelant par un span `invoke_agent` de type CLIENT. Vers un agent hors du périmètre de confiance, la passerelle ouvre une nouvelle trace reliée par un lien de span et filtre `baggage` par liste d’autorisation (EXIG-OBS-02). Le journal d’audit **DOIT** consigner `taskId`, `contextId` et l’identifiant de trace (section 10.1 et section 10.3).

Pourquoi : la v1.41.0 des conventions OpenTelemetry n’a pas de convention propre à A2A (une convention A2A, au niveau Development, figure depuis peu dans la branche principale du dépôt semantic-conventions-genai, sans version étiquetée)**[241]**; la convention des agents trace un agent distant par un span `invoke_agent` CLIENT**[120]**, et la documentation A2A recommande le traçage distribué**[161]**.

### Déroulement d’une délégation avec approbation

La figure 9 montre comment A2A, MCP et l’approbation humaine se combinent. Un orchestrateur confie l’analyse d’un dossier de crédit commercial à un agent spécialiste; l’inscription de la décision dans l’ERP est classée P3 au catalogue et exige donc deux approbations humaines d’approbateurs distincts (agent de classe élevée et outil P3, section 8.3 et EXIG-AUT-15).

> **[Figure]**
> - Orchestrateur
> - client A2A
> - Passerelle
> - d’agents
> - Agent crédit
> - serveur A2A
> - Serveurs MCP
> - bureau de crédit, ERP
> - 1 « Analyser le dossier 8841 »
> - 2 compétence « risque de crédit »
> - carte d’agent (signature vérifiée)
> - 3 SendStreamingMessage A2A-Version: 1.0 · jeton délégué · traceparent
> - 4 WORKING
> - tools/call lire_dossier
> - 5 INPUT_REQUIRED : approbation requise
> - 6 action exacte à approuver
> - 7
> - 8 tools/call enregistrer
> - 9 artefact + COMPLETED
> - 10 confirmation + réf. d’audit
> - Personnes
> - utilisateur, 2 approbateurs
> - Catalogue
> - cartes signées (via passerelle)
> - deux jetons d’approbation signés : remis à la passerelle, qui les conserve
> - SendStreamingMessage (même taskId) + références d’approbation
> - + même clé, réf. d’approbation

***Figure 9 — Délégation A2A avec appel MCP et approbation humaine.** Les numéros renvoient aux étapes ci-dessous. La passerelle d’agents se trouve sur chaque appel, et l’écriture n’a lieu qu’avec deux jetons d’approbation liés à l’action exacte (EXIG-AUT-15). Le couloir « Personnes » réunit l’utilisateur et les deux approbateurs habilités distincts (section 8.5); les jetons d’approbation restent à la passerelle, qui n’en communique que les références, données non secrètes. Source : élaboration du cadre, d’après la spécification A2A 1.0 et MCP 2026-07-28.*

1. L’utilisateur demande à l’orchestrateur d’analyser le dossier 8841.
2. L’orchestrateur cherche au catalogue d’entreprise la compétence « risque de crédit », obtient la carte de l’agent spécialiste et en vérifie la signature.
3. Il obtient un jeton délégué dont l’audience est la passerelle, puis envoie `SendStreamingMessage` à la passerelle avec `A2A-Version: 1.0`, le jeton et `traceparent`; la passerelle l’échange contre un jeton à audience unique pour l’agent crédit. Le message porte le sous-objectif structuré et des références de documents, jamais l’historique brut de la conversation (section 7.7).
4. L’agent crédit passe à `WORKING` et lit le dossier par un outil MCP (`tools/call`), sous un jeton échangé pour l’audience du serveur MCP.
5. Prêt à inscrire sa recommandation motivée (il n’accorde ni ne refuse aucun crédit, carte C.3), il passe à `INPUT_REQUIRED` et décrit, dans une partie `data`, l’action exacte à approuver : outil, arguments (clé d’idempotence comprise), montant.
6. L’orchestrateur soumet cette action à deux approbateurs habilités distincts (action P3 d’un agent de classe élevée, dont au moins un n’est pas le mandant), hors de la conversation; chaque approbation produit un jeton signé lié à l’empreinte de l’action (section 8.5, EXIG-AUT-15).
7. L’orchestrateur envoie un nouveau message rattaché au même `taskId`, qui transmet les références des deux approbations; les jetons signés restent à la passerelle (EXIG-AUT-12).
8. L’agent crédit appelle l’outil d’écriture de l’ERP avec les références d’approbation et une clé d’idempotence (section 7.6); la passerelle vérifie que les deux jetons, valides et d’approbateurs distincts dont un autre que le mandant, correspondent exactement à cet appel avant de le relayer.
9. L’agent livre son artefact, et la tâche passe à `COMPLETED`.
10. L’orchestrateur confirme le résultat à l’utilisateur avec la référence du journal d’audit.

Si l’un des approbateurs refuse ou si le délai d’approbation expire, l’orchestrateur annule la tâche (`CancelTask`) et aucune écriture n’a lieu. Un « oui » saisi dans la conversation n’est jamais une approbation : seuls comptent les jetons signés, vérifiés par la passerelle.

### Migration et compatibilité

Une carte 1.0 peut annoncer à la fois des interfaces 0.3 et 1.0, distinguées par `protocolVersion`, et les SDK officiels assurent la rétrocompatibilité**[29, 68]**. Les principaux changements à absorber sont les suivants : `supportedInterfaces` remplace `url`, `preferredTransport` et `additionalInterfaces`; les parties sont unifiées; les états prennent le préfixe `TASK_STATE_`; l’opération de flux devient `SendStreamingMessage`**[235]**. Les SDK n’ont pas atteint la 1.0 en même temps : celui de JavaScript n’est en disponibilité générale que depuis le 22 juillet 2026**[242]**. La trousse `a2a-tck` teste les trois liaisons standard, à partir des interfaces déclarées dans la carte, selon trois niveaux : MUST (échec bloquant), SHOULD (échec signalé, non bloquant) et MAY (test sauté si la fonction n’est pas déclarée)**[243]**. L’interface en ligne de commande officielle, présentée le 1er octobre 2026 (versions publiées dès le 9 septembre 2026), s’insère dans les chaînes d’intégration grâce à sa sortie JSON et à ses codes de sortie prévisibles, par exemple pour des tests de vérification rapide *(smoke tests)***[244, 245]**.

`EXIG-A2A-14` **· DOIT**

**Compatibilité vérifiée avant inscription**

Un agent **DOIT** réussir tous les tests de niveau MUST d’`a2a-tck`, sur chaque liaison déclarée, avant son inscription au registre, à chaque déploiement de l’agent (code ou SDK compris) et à chaque nouvelle version de sa carte, avec une version d’`a2a-tck` épinglée à une étiquette au catalogue. Tant que la ligne visée de la trousse est alpha, seuls bloquent les tests MUST restés stables pendant deux versions de la trousse; les autres résultats sont consignés. Tout échec d’un test de niveau SHOULD **DOIT** être consigné à la fiche (annexe B, bloc « Évaluation »), avec une échéance de correction.

Pourquoi : la conformité se prouve par un test reproductible, pas par une déclaration du fournisseur.

`EXIG-A2A-15` **· DEVRAIT**

**Migration bornée depuis la version 0.3**

Un agent encore en 0.3 **DEVRAIT** migrer par double publication : sa carte annonce une interface 1.0 et une interface 0.3, cette dernière portant une date de retrait absolue inscrite au catalogue, au plus six mois après l’approbation du cadre ou, si elle est postérieure, après l’inscription de l’agent (choix du cadre). Passé cette date, conformément à l’EXIG-INT-06 et à l’EXIG-A2A-08, la passerelle refuse toute requête dont la version effective (en-tête `A2A-Version` ou paramètre de requête, une valeur absente ou vide valant 0.3) n’est pas prise en charge par l’interface inscrite au catalogue.

**Migration bornée depuis la version 0.3**

Un agent encore en 0.3 doit migrer par double publication : sa carte annonce une interface 1.0 et une interface 0.3, cette dernière portant une date de retrait absolue inscrite au catalogue, au plus six mois après l’approbation du cadre ou, si elle est postérieure, après l’inscription de l’agent (choix du cadre). Passé cette date, la passerelle doit refuser toute requête dont la version effective (en-tête `A2A-Version` ou paramètre de requête, une valeur absente ou vide valant 0.3) n’est pas prise en charge par l’interface inscrite au catalogue.

Pourquoi : la coexistence évite de basculer tous les clients le même jour, et l’échéance empêche la version obsolète de devenir permanente.

## 6.7 Interopérabilité événementielle

Cette section encadre les échanges asynchrones : un agent ou un système publie un fait sur un bus d’événements, et un ou plusieurs agents y réagissent sans que l’émetteur les connaisse. Elle fixe l’enveloppe, les contrats, les attributs de gouvernance et les garanties sur lesquelles une conception peut réellement compter. Le bus est l’infrastructure de messagerie qui porte les sujets; le courtier, son composant d’application, y authentifie les agents et applique les listes de contrôle d’accès (EXIG-EVT-07).

### Quand préférer l’événement

MCP et A2A fonctionnent par demande et réponse : l’appelant connaît son destinataire et attend un résultat. L’événement convient mieux dans trois cas. **Découplage dans le temps** : le traitement peut attendre, ou le consommateur peut être indisponible un moment (lots de nuit, pointes de charge, réaction aux changements d’état d’un ERP). **Plusieurs abonnés** : un même fait intéresse plusieurs agents, et l’on veut en ajouter sans toucher à l’émetteur. **Rejeu** : on veut relire la séquence des faits pour un audit ou pour évaluer une nouvelle version d’agent. Par exemple, une alerte de rupture de stock intéresse la planification, l’approvisionnement et le service à la clientèle; publiée une fois, elle les atteint tous les trois sans que le détecteur les connaisse.

L’argument du nombre de liaisons (N(N−1)/2 liaisons deux à deux, contre N vers un courtier) ne distingue pas le bus de la passerelle d’agents, qui forme déjà une étoile à N connexions; l’apport propre du bus est le découplage logique décrit ci-dessus. Les sujets, les schémas et les contrats restent à gouverner. L’abonnement évite aussi le délai propre aux boucles d’interrogation. Comme le souligne Kai Waehner, conseiller indépendant en diffusion de données en continu *(data streaming)*, MCP n’offre ni garantie de livraison ni cohérence, alors qu’un journal persistant et ordonné découple producteurs et consommateurs : les deux approches se complètent**[167, 246]**.

`EXIG-EVT-01` **· DEVRAIT**

**Recours au bus pour l’asynchrone**

Une interaction qui n’attend pas de réponse immédiate, qui intéresse plusieurs consommateurs ou qui doit pouvoir être rejouée **DEVRAIT** passer par le bus d’événements de l’entreprise plutôt que par une chaîne d’appels A2A ou MCP. Le choix suit la matrice de la section 6.4 et le patron de chorégraphie de la section 7.2. Le bus n’est pas un chemin hors des points d’application : le courtier en est un (EXIG-EVT-07).

Pourquoi : une chaîne d’appels synchrones lie la disponibilité de chaque agent à celle de tous les autres.

### Enveloppe et contrats

Le cadre retient CloudEvents 1.0 comme enveloppe. La dernière révision publiée est la 1.0.2 (février 2022), les producteurs indiquent toujours `specversion` « 1.0 », et le projet a obtenu le statut « Graduated » de la CNCF le 25 janvier 2024**[173, 247]**. CloudEvents exige quatre attributs de contexte (`id`, `source`, `specversion`, `type`) et en propose quatre facultatifs (`datacontenttype`, `dataschema`, `subject`, `time`)**[173]**. Le contrat de chaque sujet se décrit en AsyncAPI 3.x : la 3.0.0 date du 5 décembre 2023, et la 3.1.0, publiée le 31 janvier 2026, est une version mineure sans rupture**[174, 249]**.

Sur Kafka, la liaison CloudEvents offre un mode binaire (attributs, sauf `datacontenttype` porté par l’en-tête `content-type`, dans des en-têtes préfixés `ce_`; données telles quelles dans la valeur) et un mode structuré (événement complet en `application/cloudevents+json`); un « Key Mapper » facultatif, à activer explicitement, peut copier `partitionkey` dans la clé Kafka**[250]**. Le cadre retient le mode binaire par défaut : les données restent intactes, et les intermédiaires filtrent sur les attributs sans désérialiser la charge utile. Un consommateur détermine le mode d’après l’en-tête `content-type` : un type qui commence par `application/cloudevents` indique le mode structuré, tout autre type le mode binaire**[250]**. Un exemple d’événement complet figure à l’annexe C.

`EXIG-EVT-02` **· DOIT**

**Enveloppe CloudEvents complète**

Tout événement produit ou consommé par un agent **DOIT** respecter CloudEvents 1.0 et porter, en plus des quatre attributs requis, `time` et, dès que l’événement porte `data`, `datacontenttype` et `dataschema` (exigence du cadre; pour un événement par référence, `dataschema` décrit la ressource que vise `dataref`). Un événement d’un système existant que consomme un agent passe par un adaptateur de mise en conformité. Le `type` **DOIT** être un nom en domaine inversé qui inclut sa version (exigence du cadre; la norme recommande seulement le préfixe en domaine inversé), par exemple `ca.ent.logistique.alerte.` `rupture.v1` .

Pourquoi : un consommateur doit savoir, sans ouvrir la charge utile, ce qu’il reçoit, quand le fait s’est produit (ou, si cet instant est inconnu, l’heure que la source retient de façon uniforme) et quel schéma le valide.

`EXIG-EVT-03` **· DOIT**

**Contrat AsyncAPI au catalogue**

Chaque sujet du bus **DOIT** être décrit par un contrat AsyncAPI 3.x inscrit au catalogue d’entreprise. Le contrat précise le schéma versionné des données et la clé de partition; l’entrée de catalogue précise le propriétaire, la classification et les producteurs et consommateurs autorisés, pour lesquels AsyncAPI ne définit aucun champ normalisé (section 6.8). Un changement incompatible de schéma crée un nouveau `type` versionné, selon les règles de la section 6.8.

Pourquoi : sans contrat, chaque consommateur devine le format et casse au premier changement.

### Extensions de gouvernance

Les attributs requis par CloudEvents ne disent ni quel agent a lancé la chaîne, ni au nom de qui, ni à quel coût. Le cadre ajoute donc des extensions, en privilégiant celles que CloudEvents documente déjà; ces extensions documentées n’ont pas de statut officiel et peuvent évoluer, et trois d’entre elles (Auth Context, Data Classification et Expiry Time) ne figurent pas dans la révision 1.0.2, qui ne documente que Dataref, Distributed Tracing, Partitioning, Sampling et Sequence**[187, 251]**, si bien que le cadre fige au catalogue la version qu’il en retient. Un nom d’attribut ne contient que des minuscules ASCII et des chiffres, et ne devrait pas dépasser 20 caractères; le préfixe `x` n’est ni exigé ni défini par la norme, et le cadre le garde pour signaler ses propres extensions**[173]**. Pour désigner l’initiateur, l’extension documentée Auth Context remplace une extension maison : elle est purement informative, déconseille les renseignements personnels dans `authid` et interdit d’inclure dans `authclaims` des justificatifs permettant d’usurper directement l’identité du mandant**[252]**.

Le contexte de trace mérite une précision. L’extension Distributed Tracing prévoit que, pour une transmission en plusieurs sauts, `traceparent` porte la trace de départ et non celle de chaque saut; elle ne remplace pas les en-têtes de traçage du transport**[253]**. Les conventions OpenTelemetry de messagerie, au niveau Development, recommandent que le producteur injecte le contexte de création dans le message et relient par défaut producteur et consommateur par des liens de span plutôt que par parenté (la parenté n’étant admise que pour un message unique)**[254]**.

*Tableau 20 — Attributs d’extension CloudEvents exigés par le cadre*

| **Attribut** | **Origine** | **Contenu** | **Règle du cadre** |
| --- | --- | --- | --- |
| `traceparent` (`tracestate` facultatif) | Extension documentée Distributed Tracing | Contexte W3C Trace Context de la trace que poursuit l’agent émetteur | Obligatoire; jamais un identifiant métier |
| `authtype`, `authid` | Extension documentée Auth Context | Type de mandant, selon les valeurs recommandées par l’extension (`app_user` pour l’utilisateur final d’une application, `user` pour un compte d’infrastructure, `service_account`, `api_key`, `system` pour une identité volontairement masquée, `unauthenticated`, `unknown`), et son identifiant | Obligatoires; `authid` pseudonyme |
| `dataclassification`, `dataregulation`, `datacategory` | Extension documentée Data Classification**[255]** | étiquettes recommandées par l’extension lorsque aucun régime n’en définit : `public`, `internal`, `confidential` ou `restricted`; régime applicable (liste séparée par des virgules); catégorie selon le régime (p. ex. `sensitive-pii`, exemple américain de l’extension) | `dataclassification` obligatoire; les deux autres dès que l’événement touche des RP |
| `xagentorigin` | Propre au cadre | Identifiant au registre et version de l’agent qui a publié le premier événement de la chaîne | Obligatoire sur tout événement publié par un agent; posé par l’intercepteur de publication (EXIG-EVT-07) |
| `xagenthopcount` | Propre au cadre | Entier (type Integer de CloudEvents) : nombre de publications d’agents dans la chaîne causale (1 pour la première) | Obligatoire; posé par l’intercepteur de publication : 1 de plus que le plus grand compteur reçu |
| `xagentmaxhops` | Propre au cadre | Entier (type Integer de CloudEvents) : plafond de sauts inscrit à l’entrée de catalogue du sujet; l’événement dont le compteur atteint ce plafond n’est pas traité, si bien qu’un plafond N laisse traiter N − 1 événements de la chaîne | Obligatoire; 4 par défaut; minimum de la valeur reçue et du plafond du sujet de publication |
| `xcostcenter` | Propre au cadre | Centre de coûts imputé | Obligatoire; valeur du référentiel financier |
| `partitionkey`, `sequence`, `expirytime`, `dataref` | Extensions documentées | Clé de partition, rang, échéance, référence externe aux données | Au besoin, de préférence à toute extension maison |

`EXIG-EVT-04` **· DOIT**

**Attributs de gouvernance présents et vérifiés**

Tout événement publié par un agent **DOIT** porter les attributs obligatoires du tableau 20. Est un événement d’agent tout événement publié sous une identité d’agent inscrite au registre : le courtier ou l’intercepteur de publication **DOIT** rejeter à la publication l’événement d’un tel producteur qui ne les porte pas (EXIG-EVT-07). Un consommateur **DOIT** en outre refuser un événement d’agent qui en est dépourvu et le diriger vers la file de lettres mortes *(dead-letter queue)* du sujet, inscrite au catalogue, qui hérite de la classification maximale du sujet et de ses listes de contrôle d’accès. Il **DOIT** aussi tenir compte de `dataclassification` et rejeter l’événement dont il ne peut respecter les exigences ou dont il ne reconnaît pas la valeur, comme l’exige l’extension Data Classification, qui demande aussi aux intermédiaires de ne pas modifier ces attributs**[255]**. Un intermédiaire qui relaie un événement ne doit pas modifier `traceparent`; un agent qui publie un nouvel événement en réaction y **DOIT** porter un `traceparent` de la même trace que l’événement reçu, dont le span parent est son propre span de publication, et relier son span de traitement à l’événement reçu par un lien de span, pour que la trace

garde l’arbre causal (ou, s’il ouvre la chaîne, le `traceparent` de la trace qu’il ouvre), sauf pour un événement d’origine externe, régi par l’EXIG-OBS-02 (section 10.1).

Pourquoi : sans ces attributs, une chaîne d’agents n’est ni traçable, ni imputable, ni bornée.

`EXIG-EVT-05` **· NE DOIT PAS**

**Aucun renseignement personnel direct dans les attributs**

Les attributs d’un événement, lus par chaque intermédiaire et recopiés dans les journaux et les traces, **NE DOIVENT PAS** contenir de renseignement personnel direct (nom, courriel, numéro de compte) ni de justificatif; une personne n’y figure que sous un identifiant pseudonyme opaque, qui demeure un renseignement personnel (section 12.2) et dont la table de correspondance reste hors du bus. Les données personnelles volumineuses ou sensibles restent dans le système source; l’événement ne transmet qu’une référence (`dataref`), sans `data`, dont l’accès est contrôlé.

Pourquoi : un bus réplique chaque événement chez tous ses abonnés; limiter les RP qu’il transporte réduit d’autant la surface à protéger au titre de la Loi 25 (section 12.2).

### Prévention des tempêtes d’événements

Dans une chorégraphie, aucun composant central ne voit l’ensemble. Deux agents qui réagissent chacun aux événements de l’autre peuvent donc s’entretenir indéfiniment : la planification révise une prévision, l’approvisionnement ajuste une commande, ce qui déclenche une nouvelle révision, et ainsi de suite. Chaque tour consomme des jetons et peut produire des effets réels. Le compteur de sauts, posé par l’intercepteur de publication et non par l’agent, coupe cette boucle de façon déterministe, sans dépendre du jugement d’un modèle (figure 10), à condition que le système d’enregistrement modifié propage les attributs : ajuster une commande est une écriture à l’ERP, qui publie son propre événement. Un plafond de largeur, tenu par le courtier par identifiant de trace, borne en outre les chaînes qui se ramifient : sans lui, k abonnés qui republient chacun produisent jusqu’à 1 + k + k² + k³ événements en quatre sauts. Ce compteur et son plafond sont des conventions propres au cadre : aucune extension CloudEvents normalisée ne les couvre**[187]**.

> **[Figure]**
> - Bus d’événements de l’entreprise · sujets régis par contrats AsyncAPI · enveloppe CloudEvents
> - Détecteur de rupture
> - publie l’alerte
> - saut 1/4
> - Planification
> - consomme, republie
> - saut 2/4
> - Approvisionnement
> - consomme, republie
> - saut 3/4
> - Agent N File de lettres mortes
> - Règle de chaque consommateur
> - si xagenthopcount xagentmaxhops
> - lettres mortes + alerte
> - sinon traiter, publier hop + 1
> - Chaque événement porte le contexte de la trace poursuivie (traceparent), l’agent d’origine, l’initiateur et le centre de coûts.
> - reçoit 3/4, republie 4/4
> - saut 4/4 non traité
> - + alerte d’observabilité
> - ≥
> - →

***Figure 10 — Chorégraphie événementielle et compteur de sauts.** Chaque republication augmente `xagenthopcount`; l’événement qui atteint le plafond (4 par défaut) n’est pas traité : il part en file de lettres mortes et déclenche une alerte. Source : élaboration du cadre; enveloppe CloudEvents 1.0.*

`EXIG-EVT-06` **· DOIT**

**Compteur de sauts et coupure des boucles**

L’intercepteur de publication de la plateforme, et non l’agent, **DOIT** poser les attributs de chaîne (EXIG-EVT-07). Pour le premier événement d’une chaîne : `xagenthopcount` à 1, `xagentorigin` à l’identifiant et à la version de l’agent, `xagentmaxhops` au plafond inscrit à l’entrée de catalogue du

sujet (4 par défaut). Pour un événement publié en réaction : `xagenthopcount` à 1 de plus que le plus grand compteur reçu, `xagentorigin` recopié, `xagentmaxhops` au minimum de la valeur reçue et du plafond du sujet de publication. Un système d’enregistrement adapté qui publie à la suite d’une écriture d’agent propage ces attributs par sa boîte d’envoi. Un consommateur qui reçoit un événement dont `xagenthopcount` atteint ou dépasse `xagentmaxhops` **DOIT** s’abstenir de le traiter, le diriger vers la file de lettres mortes et lever une alerte, regroupée par chaîne. Le courtier **DOIT** en outre plafonner le nombre d’événements par identifiant de trace dans une fenêtre de temps inscrite au catalogue. Un événement de compensation, déclaré comme tel au contrat du sujet et publié sous l’identité de compensation (EXIG-ORC-28), n’est pas soumis au plafond de sauts; il reste soumis à l’autorisation et à un budget propre. Le plafond d’un sujet ne se relève que par une modification revue de son entrée de catalogue.

Pourquoi : posés à la publication, hors de l’agent, les attributs bornent la chaîne sans dépendre du jugement d’un modèle; le minimum des plafonds fait prévaloir le sujet le plus strict, et le plafond par trace borne les chaînes ramifiées, que le compteur seul ne borne pas. Un système qui ne propage pas les attributs rompt encore la chaîne causale : le plafond par trace reste alors la seule borne. Une saga qui échoue près du plafond doit pouvoir se compenser.

`EXIG-EVT-07` **· DOIT**

**Autorisation fondée sur l’identité, pas sur les attributs**

Le droit de publier ou de consommer sur un sujet **DOIT** reposer sur l’identité authentifiée de l’agent auprès du courtier et sur des listes de contrôle d’accès par sujet, tirées de l’entrée de catalogue du sujet (producteurs et consommateurs autorisés). Une décision d’autorisation ne doit pas se fonder sur `authtype`, `authid` ou un autre attribut de l’événement pour accorder un accès (`dataclassification` ne peut que le restreindre). Les données reçues **DOIVENT** être traitées comme du contenu non fiable (section 9.6).

Pourquoi : l’extension Auth Context est informative et n’est pas un mécanisme de sécurité**[252]**; n’importe quel producteur peut y écrire n’importe quoi.

### Garanties réelles d’un bus

Apache Kafka sert ici d’exemple parce que ses garanties sont documentées avec précision; un autre courtier se juge sur les mêmes questions. Le tableau 21 distingue ce que le courtier garantit de ce qui reste à la charge de la conception.

*Tableau 21 — Garanties d’un bus Kafka et responsabilités de la conception*

| **Propriété** | **Ce que Kafka garantit** | **Ce qui reste à la conception** |
| --- | --- | --- |
| Livraison | « Au moins une fois » par défaut; le producteur idempotent (depuis 0.11.0.0) évite les doublons dus aux réessais internes d’une même session de producteur; un redémarrage du producteur ou du relais exige `transactional.id` ou la déduplication par le consommateur**[140]** | Consommateurs idempotents et déduplication |
| Exactement une fois | Cycle lecture-traitement-écriture entre sujets Kafka (transactions, consommateur `read_committed`); un système externe doit coopérer**[140, 256]** | Clé d’idempotence vérifiée par le système cible; patron de la boîte d’envoi |
| Ordre | Par partition seulement; les événements de même clé vont dans la même partition**[257]** | Choisir la clé selon l’entité dont l’ordre compte |
| Répartition du travail | Rééquilibrage natif des groupes de consommateurs; files coopératives *(share groups)* dont l’ordre n’est garanti qu’à l’intérieur d’un lot**[258]** | Réserver les files coopératives aux tâches indépendantes |
| Rejeu | Relecture depuis un décalage sauvegardé, dans la limite de la rétention configurée**[140]** | Rétention suffisante; rejeu isolé; aucune promesse de décisions identiques |

Quelques repères de version aident à fixer au catalogue la version plancher du courtier. Kafka 4.0 (18 mars 2025) est la première version majeure entièrement sans ZooKeeper et généralise le nouveau protocole de rééquilibrage des groupes**[259]**. Les files coopératives sont prêtes pour la production depuis Kafka 4.2.0 (17 février 2026), et Kafka 4.4.0 (22 octobre 2026) leur ajoute des files de lettres mortes**[260, 261]**.

La conséquence pratique tient en une phrase : un effet réel n’est jamais protégé par le bus, mais par l’idempotence du consommateur et du système cible. Kafka seul n’empêche pas un double paiement. Pour publier de façon fiable un changement d’état et l’événement qui l’annonce, le producteur applique le patron de la boîte d’envoi *(transactional outbox)* : il écrit l’événement dans une table de sa base, dans la même transaction locale que le changement, puis un relais le publie. Aucun événement ne part ainsi pour une transaction annulée, et aucun changement validé ne reste sans événement.

Le rejeu appelle la même prudence. Confluent présente le rejeu déterministe des événements comme le fondement de l’investigation d’un incident, de l’audit réglementaire, de la validation de modèle et des mises à jour sûres des agents**[262]**. Rejouer les entrées ne garantit pourtant pas que l’agent reprendra les mêmes décisions, car rien n’assure qu’un modèle produise la même sortie à entrées identiques. Le cadre parle donc de rejeu des entrées pour l’audit et la réévaluation, jamais de reproduction des décisions.

`EXIG-EVT-08` **· DOIT**

**Effets réels protégés par l’idempotence**

Tout consommateur dont le traitement produit un effet hors du bus **DOIT** être idempotent : il déduplique sur l’identité de l’événement (`source` et `id`; le producteur et le relais de la boîte d’envoi **DOIVENT** les conserver à chaque renvoi du même événement, ce que la norme permet sans l’imposer) et transmet au système cible une clé d’idempotence que ce dernier vérifie (section 7.6). Cette clé dérive du couple (`source`, `id`) de l’événement déclencheur, jamais de l’identifiant d’une tâche ouverte par le consommateur; l’état de déduplication est conservé au moins pendant la rétention du sujet et mis à jour dans la même transaction que l’effet, ou complété par une requête d’état qui constate l’effet. Un producteur qui publie à la suite d’un changement dans sa base **DOIT** appliquer le patron de la boîte d’envoi ou un mécanisme transactionnel équivalent. La sémantique « exactement une fois » du courtier ne doit pas être invoquée comme protection contre un double effet externe.

Pourquoi : la livraison est « au moins une fois »**[140]**; sans idempotence, une seule reprise suffit à payer deux fois une facture.

`EXIG-EVT-09` **· DOIT**

**Ordre garanti par la clé de partition**

Lorsqu’un flux exige l’ordre des événements d’une même entité (dossier, commande, session), la clé de partition **DOIT** être l’identifiant technique de cette entité, sans renseignement personnel direct (EXIG-EVT-05; un identifiant pseudonyme est admis et traité comme un renseignement personnel, pour la conservation comme pour l’accès), porté par `partitionkey` et précisé au contrat AsyncAPI. La clé native du courtier **DOIT** égaler `partitionkey` : sur Kafka, le producteur la fixe lui-même ou active le « Key Mapper » facultatif de la liaison, qui reprend par défaut la clé fournie par l’utilisateur**[250]**. L’ordre suppose en outre un nombre de partitions figé pendant la vie du sujet, un traitement séquentiel par clé chez le consommateur et un relais de boîte d’envoi ordonné. Les files coopératives ne doivent pas servir à un tel flux; elles conviennent aux bassins d’exécutants dont les tâches sont indépendantes.

Pourquoi : Kafka ne garantit l’ordre qu’au sein d’une partition, et une file coopérative ne le garantit qu’à l’intérieur d’un lot.

`EXIG-EVT-10` **· DOIT**

**Conservation des entrées et rejeu isolé**

Les sujets qui alimentent des agents de classe de risque modérée ou élevée **DOIVENT** conserver leurs événements au moins pendant la fenêtre d’enquête inscrite à la fiche de l’agent (au moins 90 jours pour la classe modérée et un an pour la classe élevée), selon la règle de durée de l’EXIG-CON-10 : durée liée à la finalité, inscrite à la fiche et appliquée automatiquement, dans la limite du calendrier de conservation applicable aux RP; la durée de conservation des traces de l’agent, inscrite à la même fiche, est au moins égale à cette fenêtre, et le journal d’audit suit l’EXIG-OBS-13; un sujet qui alimente plusieurs agents retient la plus longue de leurs fenêtres, et l’effacement des RP d’un sujet conservé se fait par chiffrement par personne ou par sujet, puis destruction de la clé. Tout rejeu d’audit ou d’évaluation **DOIT** s’exécuter dans un environnement isolé où les outils à effet sont remplacés par des doublures; ses résultats servent à l’audit et à l’évaluation continue (section 10.4), jamais à répéter des actions en production. La reprise opérationnelle d’un groupe de consommateurs après une panne n’est pas un rejeu au sens de cette exigence : l’EXIG-EVT-08 la régit.

Pourquoi : rejouer des entrées contre des outils réels répéterait leurs effets, et un modèle peut décider autrement la seconde fois.

Le bus ne porte aucun jeton, et l’initiateur qu’indiquent `authtype` et `authid` est informatif (EXIG-EVT-07) : sans point d’application au courtier, un consommateur agirait sous sa seule identité, hors de l’intersection des droits (PRIN-03) et de la limite de délégation. Conformément à l’EXIG-EVT-07, le courtier et l’intercepteur de publication de la plateforme constituent donc un point d’application au même titre que la passerelle : ils authentifient le producteur, appliquent les listes de contrôle d’accès par sujet, posent eux-mêmes les attributs de gouvernance (identité de l’agent producteur, référence de délégation, compteur et plafond de sauts de l’EXIG-EVT-06, étiquettes de contamination et de sensibilité de la session productrice, EXIG-SEC-04), refusent un événement dont le `dataschema` ne figure pas parmi les schémas épinglés pour le sujet, et rejettent à la publication l’événement d’un agent qui ne porte pas les attributs du tableau 20. Toute action P2 ou P3 qu’un consommateur exécute à la suite d’un événement traverse la passerelle d’agents, sous la délégation que référence l’événement, échangée selon la RFC 8693 (EXIG-IAM-08), ou, à défaut, sous un mandat de service inscrit au catalogue pour ce sujet et pour ce consommateur; un saut exécuté sous la délégation que référence l’événement compte comme un niveau dans la profondeur de délégation de l’EXIG-ORC-04.

## 6.8 Contrats, versionnage et catalogue d’entreprise

Cette section fixe ce que chaque interface offerte à un agent doit déclarer, comment ses versions évoluent sans briser ses consommateurs et ce que contient le catalogue d’entreprise.

### Ce que chaque contrat déclare

Un contrat a deux faces : ce que le fournisseur publie dans le format du protocole, et ce que l’entreprise fixe au catalogue. Comme les annotations MCP sont des indices non fiables (EXIG-MCP-14) et que la carte A2A n’admet aucun champ de gouvernance hors norme (EXIG-A2A-05), tout ce qui commande une décision de sécurité vit au catalogue (tableau 22; exemples à l’annexe C).

*Tableau 22 — Contenu minimal des contrats, par type d’interface*

| **Interface** | **Contrat publié** | **Entrée fixée au catalogue** |
| --- | --- | --- |
| Outil MCP | Nom préfixé par le domaine; description destinée au modèle, qui dit ce que fait l’outil et ce qu’il ne fait pas; `inputSchema` et, au besoin, `outputSchema` en JSON Schema 2020-12; clé d’idempotence pour tout outil à effet (section 7.6) | Version et empreinte; palier P0 à P3 et seuil, avec sa grandeur, son unité, sa portée et sa fenêtre (section 8.3, EXIG-AUT-08); compensation de toute écriture P2; propriétaire et équipe de garde; classification maximale des données |
| Ressource et invite MCP | Ressource adressée par URI; invite nommée et décrite | Version et empreinte (pour un gabarit `ui://`, empreinte de son contenu); palier P0 ou P1 d’une ressource (EXIG-MCP-05); classification; propriétaire et équipe de garde |
| Agent A2A | Carte A2A 1.0 signée (section 6.6) | Version et empreinte; portée OAuth par compétence et durée attendue par compétence (EXIG-A2A-07); renvoi à la fiche du registre; pour un agent de tiers, carte d’origine et son empreinte (EXIG-A2A-02) |
| Sujet d’événement | Contrat AsyncAPI 3.x, avec la clé de partition, et `type` versionné (section 6.7) | Producteurs et consommateurs autorisés; classification; plafond de sauts et plafond par trace (EXIG-EVT-06); file de lettres mortes; propriétaire et équipe de garde |
| API existante | Contrat OpenAPI 3.1.x ou 3.2.x; erreurs au format RFC 9457**[171]** | Outils MCP qui l’exposent, chacun avec son entrée |

`EXIG-INT-12` **· DOIT**

**Contrat complet avant l’inscription**

Toute interface offerte à un agent **DOIT** disposer, avant son inscription au catalogue d’entreprise, d’un contrat publié et d’une entrée de catalogue qui contiennent au minimum les éléments du tableau 22. Un élément manquant bloque l’inscription.

Pourquoi : la passerelle n’applique que des règles écrites; sans palier ni compensation déclarés, l’agent déciderait seul de ce qui est sûr.

### Versionnage sémantique

La version d’un protocole ne dit rien des contrats publiés sur lui. Or la définition d’un outil MCP ne comporte aucun champ de version**[197]**, et le champ `version` d’une carte A2A est de format libre**[68]**. Le cadre impose donc aux contrats le versionnage sémantique (SemVer), de forme MAJEUR.MINEUR.CORRECTIF, tenu au catalogue :

- **majeur** : tout changement qui peut faire échouer ou tromper un consommateur (élément retiré ou renommé, nouveau paramètre obligatoire, valeurs admises restreintes en entrée, valeur ajoutée à une énumération de sortie, changement de sens à format constant);
- **mineur** : ajout compatible et reformulation d’une description sans changement de sens, établie par la revue sémantique (EXIG-INT-16);
- **correctif** : correction qui ne change ni la définition publiée ni le comportement attendu.

Le changement de sens est le plus dangereux, car aucun validateur ne le voit : un montant qui passe de hors taxes à toutes taxes comprises reste un nombre valide (section 6.1). A2A applique la même logique à ses extensions, dont tout changement incompatible exige une nouvelle URI**[238]**.

`EXIG-INT-13` **· DOIT**

**Versionnage sémantique des contrats**

Tout contrat inscrit au catalogue **DOIT** porter une version SemVer, incrémentée à chaque publication selon les règles ci-dessus : au moins mineure pour toute modification de la définition publiée, majeure pour tout changement incompatible, y compris de sens. Pour un agent A2A, c’est le champ `version` de sa carte (EXIG-A2A-04). L’unité de version est l’outil, la ressource, l’invite, la carte d’agent ou le sujet; un serveur MCP n’est qu’un agrégat d’entrées. La définition publiée, que canonise l’empreinte (EXIG-INT-15, EXIG-INT-16, EXIG-MCP-20), comprend : pour un outil MCP, le nom, le titre, la descrip

tion, les icônes, les schémas d’entrée et de sortie, les annotations et `_meta`, hors champs volatils inscrits au catalogue; pour une ressource ou une invite, son URI ou son nom, sa description et, pour un gabarit `ui://`, son contenu; pour une carte A2A, la carte canonisée sans le champ `signatures`; pour un sujet, le contrat AsyncAPI converti en JSON.

Pourquoi : un numéro régi par des règles connues dit au consommateur s’il peut migrer sans risque (règle du cadre).

`EXIG-INT-14` **· DOIT**

**Coexistence d’au moins 60 jours**

À la publication d’une version majeure, la version majeure précédente **DOIT** rester disponible au moins 60 jours (choix du cadre), avec une date de retrait inscrite au catalogue dès ce moment et annoncée aux consommateurs connus. Seul un motif de sécurité justifie un retrait anticipé : sur décision du comité, la version visée passe d’abord à l’état « suspendue », et la passerelle cesse immédiatement de la servir (EXIG-GOV-14); le comité fixe ensuite la date de retrait. Pendant la coexistence, la passerelle sert la version majeure précédente sous un nom d’outil suffixé par sa version majeure (p. ex. `domaine_outil_v2`) pour MCP, et sous une entrée `supportedInterfaces` par version majeure pour A2A, et elle route selon la dépendance épinglée de l’appelant; deux types d’événements coexistants (v1 et v2) portent un même identifiant de fait (`id` ou clé métier), et le consommateur abonné aux deux déduplique. Un contrat de tiers relève de l’EXIG-INT-16.

Pourquoi : un délai connu permet de planifier les migrations; il concorde avec le préavis de retrait d’un agent (section 11.5).

### Épinglage et approbation des changements

Un consommateur ne suit jamais « la dernière version ». Il dépend d’une version identifiée par son numéro et par son empreinte, soit le condensé SHA-256 de la définition canonisée selon la RFC 8785**[236]**. Le numéro dit ce que le fournisseur affirme; l’empreinte prouve la définition que l’agent reçoit, non le comportement du serveur, qui relève de la signature des artefacts déployés et de la provenance (section 9.8), du contrôle des sorties réseau et des tests de contrat. L’empreinte d’un contrat AsyncAPI porte sur sa conversion en JSON, canonisée de la même façon. La fiche d’agent consigne ces dépendances (annexe B); la passerelle vérifie l’empreinte à l’exécution (EXIG-MCP-20, EXIG-SEC-18) et, pour un événement, le courtier et le registre de schémas du consommateur vérifient que le `dataschema` reçu figure parmi les schémas épinglés (EXIG-EVT-07). L’OWASP recommande d’épingler les définitions par empreinte et de redemander le consentement à chaque modification**[221]**.

`EXIG-INT-15` **· DOIT**

**Dépendances épinglées par version et empreinte**

Chaque agent **DOIT** déclarer dans sa fiche, pour chaque outil, ressource, invite, agent appelé et sujet d’événement, la version épinglée et l’empreinte approuvée. Une dépendance ne doit pas désigner une version flottante (« dernière », plage de versions); changer de version est une modification de la fiche, revue et tracée. L’épinglage porte sur MAJEUR.MINEUR et sur l’empreinte; un correctif, qui ne change pas l’empreinte, se suit sans modifier la fiche. À l’activation d’une version mineure, le propriétaire du contrat migre en lot les épinglages après avis aux consommateurs, ou la passerelle sert la mineure précédente pendant une fenêtre de migration inscrite au catalogue; au plus deux versions mineures d’une même majeure sont actives à la fois (choix du cadre).

Pourquoi : sans épinglage, un fournisseur peut changer la définition que lit l’agent à l’insu de son parrain; l’épinglage ne prouve pas pour autant le comportement du fournisseur, qui relève de la section 9.8.

`EXIG-INT-16` **· DOIT**

**Nouvelle approbation à toute modification**

Toute modification de la définition publiée d’un outil, d’une ressource, d’une invite ou d’une carte d’agent, y compris la reformulation d’une description, **DOIT** être revue et approuvée de nouveau au catalogue avant d’être servie aux agents, y compris pour les serveurs et agents de tiers. La revue confirme aussi le palier attribué. Pour un tiers, dont l’entreprise ne contrôle ni le calendrier ni la chaîne d’intégration : la version est tenue au catalogue par l’entreprise; le contrat prévoit un préavis de changement de définition et un point d’accès de préversion (chapitre 13); un test différentiel à l’entrée du catalogue remplace la chaîne d’intégration de l’EXIG-INT-19; une revue accélérée vise un délai cible inscrit au catalogue. Hors préavis, la modification suspend l’outil ou l’agent jusqu’à la revue (EXIG-MCP-20) : ce mode fermé est le comportement assumé, la coexistence de l’EXIG-INT-14 étant alors impossible.

Pourquoi : le modèle lit la description comme une consigne, et la substitution après approbation *(rug pull)* exploite justement un changement présenté comme anodin (section 9.8).

### Catalogue d’entreprise

Le catalogue d’entreprise recense tous les contrats joignables par les agents. Le catalogue des protocoles (section 6.3) dit quels standards employer; le catalogue d’entreprise, quels contrats existent sur ces standards. Le registre (section 11.4) dit qui répond d’un agent et avec quel risque; le catalogue, par quel contrat et dans quelle version. Le registre officiel MCP, en préversion, n’en tient jamais lieu**[43]**.

Chaque version de contrat est « en revue », « active », « dépréciée » (avec sa date de retrait), « suspendue » (motif de sécurité, EXIG-INT-14) ou « retirée », à l’image du cycle *Active*, *Deprecated*, *Removed* que MCP applique à ses propres fonctionnalités**[34]**. Ces états sont distincts de ceux de la fiche d’agent. Sans la liste des consommateurs de chaque version, on découvre ceux d’une version retirée par leurs pannes.

`EXIG-INT-17` **· DOIT**

**Catalogue unique, source de la découverte**

L’entreprise **DOIT** tenir un seul catalogue d’entreprise, sous une même autorité et articulé avec le registre de gouvernance (section 11.4), qui recense chaque version de contrat (outil, ressource ou invite MCP, regroupés par serveur, carte d’agent A2A, sujet AsyncAPI) avec son état, son propriétaire, son empreinte et, s’il y a lieu, sa date de retrait. La découverte passe par lui, jamais par une adresse configurée à la main; la passerelle ne sert que les versions actives et les versions dépréciées non échues, jamais une version suspendue ou retirée.

Pourquoi : deux sources de vérité finissent par diverger.

`EXIG-INT-18` **· DOIT**

**Consommateurs connus avant tout retrait**

Le catalogue **DOIT** indiquer les consommateurs connus de chaque version active ou dépréciée, tirés des fiches d’agents et rapprochés chaque mois des appels observés par la passerelle (fréquence fixée par le cadre). Une version n’est retirée qu’à l’échéance annoncée, jamais avant la fin de la coexistence de l’EXIG-INT-14 sauf suspension de sécurité (EXIG-INT-14, EXIG-GOV-14), et après avis à ses consommateurs connus. La passerelle refuse tout appel d’une version absente de la fiche de l’appelant (EXIG-IAM-17); le rapprochement avec les appels observés est un contrôle de cohérence, rendu continu pendant la fenêtre de dépréciation.

Pourquoi : le rapprochement révèle les écarts entre les fiches et les appels avant que le retrait ne brise un consommateur.

### Tests de compatibilité

Une règle de versionnage ne tient que si une machine la vérifie; seul le changement de sens échappe à la comparaison des schémas et relève de la revue sémantique (EXIG-INT-01 et EXIG-INT-16). Les suites de conformité complètent les tests internes : `a2a-tck` (EXIG-A2A-14)**[243]** et le cadre officiel de tests de conformité MCP, encore en versions 0.x (préversion 0.2.0-alpha en cours)**[225, 226]**. Les deux suites suivent un même régime (EXIG-INT-19). Ces tests forment le premier étage de l’évaluation continue (section 10.4).

`EXIG-INT-19` **· DOIT**

**Détection automatique des ruptures**

La chaîne d’intégration **DOIT** comparer chaque nouvelle version d’un contrat à la version active précédente et bloquer toute publication qui contient un changement incompatible sans incrément majeur, ou dont l’empreinte change sans incrément au moins mineur. Avant son activation, la nouvelle version **DOIT** réussir le jeu d’évaluation de chaque agent consommateur connu, rejoué en environnement isolé contre elle (section 10.4) avec le seuil de réussite inscrit à sa fiche, et, pour un agent A2A, les tests de l’EXIG-A2A-14. Une suite de conformité (`a2a-tck`, cadre officiel de conformité MCP ou suite équivalente approuvée par l’architecture d’entreprise, EXIG-APP-03) est épinglée à une étiquette au catalogue; tant que sa ligne est alpha ou en préversion 0.x, ses résultats sont consignés et ne bloquent que sur les tests restés stables pendant deux versions de la suite. Pour un tiers, l’EXIG-INT-16 s’applique.

Pourquoi : une règle de compatibilité vérifiée à la main finit par céder sous la pression d’une livraison.

## 6.9 Protocoles émergents et veille

Cette section situe les travaux qui n’ont pas le statut Adopter (section 6.3) et en encadre l’usage; le processus de veille relève de la section 11.7.

### Ce que l’AAIF héberge réellement

Au 22 octobre 2026, l’Agentic AI Foundation (AAIF) héberge dix projets : MCP, goose, AGENTS.md, agentgateway, A2A, Agent Router et, annoncés ce jour-là, Agent Skills, Open Responses, OpenEnv et OpenSandbox**[38, 130]**. L’admission suit un processus formel : proposition publique, triage, recommandation du comité technique, puis approbation du conseil d’administration, suivie des formalités juridiques et de l’intégration technique menées avec la Linux Foundation**[42, 263]**. Un projet proposé n’est qu’un candidat, et l’hébergement garantit une gouvernance neutre, non la maturité d’une spécification.

`EXIG-INT-20` **· NE DOIT PAS**

**Qualification « AAIF » non vérifiée**

Un document d’architecture, un appel d’offres ou un contrat **NE DOIT PAS** qualifier un projet de « projet de l’AAIF » ni de « standard de l’AAIF » s’il ne figure pas à la liste des projets publiée par la fondation au terme d’une admission approuvée; un projet dont la proposition est ouverte est dit « candidat à l’AAIF ». L’hébergement par l’AAIF ne dispense d’aucun critère d’admission au statut Adopter (EXIG-GOV-19).

Pourquoi : AGNTCY, souvent présenté comme une composante de l’AAIF, n’en est qu’un candidat**[37]**; l’erreur fausse l’analyse du risque fournisseur.

### AGNTCY

AGNTCY, rendu public par Cisco en mars 2025, est un projet de la Linux Foundation depuis le 29 juillet 2025**[23]**. Sa proposition à l’AAIF, déposée par Cisco le 12 octobre 2026, fait état de 81 organisations qui l’appuient et indique que Cisco fournit l’essentiel des contributions; elle restait sans décision au 27 octobre 2026**[37]**. Le tableau 23 présente ses principaux composants.

*Tableau 23 — Principaux composants d’AGNTCY et statut au catalogue (état au 27 octobre 2026)*

| **Composant** | **Fonction vérifiée** | **Statut** |
| --- | --- | --- |
| OASF *(Open Agentic Schema Framework)* | Modèle de données extensible, inspiré d’OCSF *(Open Cybersecurity Schema Framework)*, qui décrit des agents par des enregistrements annotés de compétences et de domaines; l’Agent Directory Service (ADS) y convertit des définitions de serveurs MCP, des cartes d’agent A2A et des Agent Skills**[264, 265]** | **Évaluer** |
| Agent Directory Service (ADS) | Annuaire d’enregistrements OASF stockés comme artefacts OCI *(Open Container Initiative)*, adressés par leur condensé, signés et vérifiables**[266, 267]** | **Évaluer** |
| SLIM *(Secure Low-Latency Interactive Messaging)* | Messagerie sur gRPC et HTTP/2, sessions chiffrées de bout en bout par MLS *(Messaging Layer Security)* (RFC 9420)**[268, 269]** | **Surveiller** |
| Identity | Identifiants d’agents et de serveurs MCP adossés à des justificatifs vérifiables du W3C (« Agent Badges »)**[270]** | **Surveiller** |

Trois précautions s’imposent. Les spécifications d’ADS et de SLIM soumises à l’IETF sont des brouillons individuels**[271, 272]**. La résistance de SLIM à l’ordinateur quantique, parfois avancée, n’est pas étayée : les suites cryptographiques initiales de MLS sont classiques**[269]**. Enfin, la liaison SLIMRPC reste expérimentale (EXIG-A2A-08), et la carte d’agent suit le schéma d’A2A, non celui d’OASF.

`EXIG-INT-21` **· DOIT**

**Pilotes AGNTCY subordonnés au catalogue**

Tout pilote d’OASF ou d’ADS **DOIT** traiter le catalogue d’entreprise comme source de vérité : les enregistrements de l’annuaire en sont dérivés, et aucun agent n’y découvre un outil ou un agent absent du catalogue. Une propriété de sécurité alléguée, comme la résistance de SLIM au quantique, ne doit pas entrer dans une analyse de risque sans preuve de la configuration effective. Toute dépendance de production à un composant d’AGNTCY exige une décision du comité.

Pourquoi : un annuaire parallèle recréerait deux sources de vérité, et une propriété non démontrée ne protège rien.

### Commerce et paiements agentiques

Trois protocoles principaux se disputent le commerce agentique, sans convergence; d’autres initiatives existent, que le catalogue inscrit au statut Surveiller lorsqu’elles touchent l’entreprise. L’Agentic Commerce Protocol d’OpenAI et de Stripe (septembre 2025) demeure en bêta**[183]**; son jeton de paiement partagé est limité à un marchand et au montant d’un panier, et masque les justificatifs de paiement à la plateforme d’IA**[27]**. AP2 *(Agent Payments Protocol)*, publié par Google en septembre 2025, étend A2A et MCP par des mandats signés qui prouvent l’intention et l’autorisation de l’utilisateur; sa version 0.2 ajoute les paiements en l’absence de l’utilisateur *(Human Not Present)*, et Google a annoncé le 28 avril 2026 en faire don à la FIDO Alliance**[26, 41]**; le transfert effectif n’était pas établi à la fin d’octobre 2026. UCP *(Universal Commerce Protocol)*, annoncé en janvier 2026 par Google en collaboration avec des détaillants et des plateformes de commerce, prend en charge REST, MCP et A2A et est compatible avec AP2**[184]**. Les trois restent au statut Surveiller, mais leurs patrons inspirent déjà la règle qui suit.

`EXIG-INT-22` **· DOIT**

**Paiements initiés par un agent**

Tout paiement, achat ou engagement financier déclenché par un agent, quel que soit le protocole, **DOIT** être classé P3 et n’être exécuté qu’avec une approbation humaine signée, propre à la transaction et liée à l’action exacte (section 8.5). L’agent ne doit pas recevoir ni transmettre de justificatif de paiement; il ne manipule que des jetons émis hors de lui, à usage unique et à courte échéance, limités à un bénéficiaire et à un montant, et liés à l’empreinte de l’approbation et à la clé d’idempotence de l’étape. Chaque paiement **DOIT** laisser au journal d’audit une preuve d’intention signée : l’approbation de la personne

habilitée, qui peut être distincte du mandant. Est « en l’absence de l’utilisateur » tout paiement sans approbation humaine propre à la transaction; il ne doit pas être autorisé, et l’adoption d’un protocole qui l’encadre ne l’autorise pas sans révision du cadre.

Pourquoi : AP2 fonde l’imputabilité d’un paiement sur des mandats signés, l’Agentic Commerce Protocol limite son jeton à un marchand et à un montant; le cadre généralise ces patrons à tout paiement.

### Signaux à suivre

La veille n’est vérifiable que si l’on sait ce que l’on attend : une décision de l’AAIF sur AGNTCY ou la première version étiquetée du dépôt dédié semantic-conventions-genai d’OpenTelemetry (section 10.1)**[181]**. Une révision de MCP, standard au statut Adopter, ne relève pas de ces signaux : sa publication déclenche la révision extraordinaire de l’EXIG-GOV-18, et l’annonce de sa date relève de la révision trimestrielle (la SEP-3398 la fixe au 30 mars 2027, sous réserve; section 6.5).

`EXIG-INT-23` **· DOIT**

**Signal de révision inscrit au catalogue**

Chaque entrée du catalogue des protocoles au statut Évaluer ou Surveiller **DOIT** indiquer le signal qui déclenchera le réexamen de son statut et la date de sa dernière vérification. L’apparition du signal **DOIT** entraîner une révision extraordinaire de l’entrée, sans attendre l’échéance trimestrielle. Pour une entrée au statut Adopter ou Contenir, une nouvelle révision, une dépréciation ou une version stable relève de l’EXIG-GOV-18, qui en fixe la révision extraordinaire.

Pourquoi : l’admission d’un projet à l’AAIF ou la publication d’une RFC ne devrait pas attendre trois mois pour être prise en compte.

**À RETENIR**

Une fondation neutre n’est pas un statut au catalogue, et une annonce n’est pas une norme : un travail émergent n’entre en production que par le statut Adopter.
