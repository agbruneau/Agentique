# 13 Approvisionnement et clauses contractuelles

Les protocoles d’interopérabilité relèvent désormais d’une gouvernance neutre; le risque de dépendance s’est donc déplacé vers les plateformes, leurs extensions et les données qu’elles accumulent. Ce chapitre traduit le cadre en critères d’évaluation des fournisseurs, en dix clauses contractuelles normatives et en une grille de notation. Il s’adresse aux acheteurs, aux juristes, aux architectes et au responsable de la protection des renseignements personnels qui négocient l’acquisition d’une plateforme d’agents, d’un service de modèles, d’une passerelle, d’un serveur MCP ou d’un agent de tiers.

## 13.1 Où se situe désormais le risque de verrouillage

Cette section localise le risque de dépendance envers un fournisseur *(vendor lock-in)*, afin de concentrer la négociation là où il se trouve réellement.

### Des protocoles sous gouvernance neutre

Le Model Context Protocol (MCP) a été versé à l’Agentic AI Foundation (AAIF), fondation hébergée par la Linux Foundation, dès sa création le 9 décembre 2025; AWS, Google et Microsoft figurent parmi ses membres Platine **[4]**. Le protocole Agent2Agent (A2A) est devenu un projet hébergé de l’AAIF, au stade « Growth », le 17 août 2026 **[5, 35]**; son comité directeur technique compte neuf sièges : les huit entreprises concurrentes de la composition annoncée le 12 mars 2026 (AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP et ServiceNow) **[29]**, et Bloomberg depuis le 20 octobre 2026 (erratum no 1 de la section H.4). Pour les protocoles au statut « Adopter » placés sous une fondation neutre, le risque qu’un protocole disparaisse ou passe sous le contrôle d’un seul éditeur est donc faible; il ne l’est pas pour un protocole du catalogue sans gouvernance neutre, et une coalition de membres peut aussi orienter une fondation. Un projet n’est toutefois un « standard AAIF » qu’une fois son admission approuvée et annoncée **[42]**; au 27 octobre 2026, la candidature d’AGNTCY demeure sans décision **[37]** (voir section 6.9).

### Un risque déplacé vers les plateformes

Un protocole ouvert ne rend pas la plateforme ouverte. Le verrouillage se loge désormais dans cinq endroits, résumés au tableau 53. Des éditeurs de passerelles soutiennent en outre que la gouvernance native d’une plateforme s’arrête à sa frontière et ne suit pas l’agent qui en sort. C’est un argument d’éditeurs, cité comme tel, mais il décrit bien le risque que le cadre traite par sa passerelle d’agents et son registre d’entreprise (section 9.4 et section 11.4). Les exemples du tableau illustrent des mécanismes; ils ne jugent pas des produits qui évoluent rapidement.

*Tableau 53 — Où se loge le verrouillage (état au 27 octobre 2026)*

| **Lieu** | **Manifestation** | **Exemple documenté** | **Parade du cadre** |
| --- | --- | --- | --- |
| Extensions de protocole | Une fonction essentielle n’existe que par une extension propre à l’éditeur. | A2A permet de déclarer une extension obligatoire (`required`) dans `capabilities.extensions` **[238]**; MCP admet des extensions à préfixe DNS inversé, désactivées par défaut **[169]**. | EXIG-APP-02 et EXIG-APP-07 |
| Couverture partielle | « Prend en charge MCP » ne vise qu’une partie des primitives ou des liaisons. | Azure API Management gère les outils MCP, mais ni les ressources ni les invites, et les agents A2A en JSON-RPC seulement **[108, 109]**; le greffon AI A2A Proxy de Kong Gateway (3.14 et plus, édition AI Gateway Enterprise) ne gère pas l’état des tâches **[111]**. | Preuves par essais (EXIG-APP-03) |
| Contraintes de produit | Les limites d’orchestration du produit deviennent celles de l’architecture. | Agentforce limite volontairement la délégation entre organisations Salesforce à un seul niveau et signale, pour Agent Script, une limite actuelle de sept sous-agents connectés **[49]**. | Logique d’orchestration détenue par l’entreprise (PRIN-09, chapitre 7) |
| Plan de contrôle et identité | L’inventaire, l’arrêt et l’identité des agents dépendent de la console de l’éditeur. | Copilot Studio crée d’office une identité Entra Agent ID pour chaque nouvel agent depuis juillet 2026 **[48]**; les fonctions de sécurité associées exigent une licence Agent 365 **[324]**, dont les actions de cycle de vie sur des agents infonuagiques tiers sont annoncées comme à venir **[46]**. | EXIG-APP-06 et EXIG-APP-16 |
| Données, définitions et unités | Mémoires, invites système, journaux et unités de facturation propres rendent la sortie coûteuse. | Copilot Studio facture en crédits et désactive les agents personnalisés au-delà de 125 % de la capacité prépayée **[53]**. | EXIG-APP-05 et EXIG-APP-14 |

**À RETENIR**

Le protocole est ouvert; il faut négocier l’ouverture là où elle se perd : la couverture réelle du protocole, l’identité des agents, leur arrêt, leurs données et leurs définitions doivent rester sous le contrôle de l’entreprise.

`EXIG-APP-01` **· DOIT**

**Analyse de réversibilité avant tout engagement**

Toute acquisition d’une plateforme d’agents, d’un service de modèles, d’une passerelle ou d’un agent de tiers **DOIT** être précédée d’une analyse de réversibilité documentée : composants et extensions propriétaires utilisés, données et définitions à récupérer, formats de restitution, délai et coût estimés de sortie. L’architecture d’entreprise **DOIT** la valider, et l’analyse **DOIT** être versée au registre.

Pourquoi : le coût de sortie se décide à la signature, pas à la résiliation.

`EXIG-APP-02` **· NE DOIT PAS**

**Aucune dépendance à une extension non approuvée**

Un agent ou un outil de l’entreprise **NE DOIT PAS** dépendre d’une extension de protocole propriétaire absente du catalogue (section 6.3). Une extension admise **DOIT** être identifiée par son URI ou son préfixe versionné et posséder un comportement de repli documenté; elle **NE DOIT PAS** être déclarée obligatoire envers des clients, sauf dérogation (section 11.6).

Pourquoi : une extension obligatoire recrée, au-dessus d’un protocole ouvert, la dépendance que ce protocole devait éliminer.

## 13.2 Critères d’évaluation des fournisseurs

Cette section fixe ce qu’un fournisseur doit démontrer, et comment. Le principe est simple : une preuve reproductible dans l’environnement de l’entreprise l’emporte toujours sur une allégation commerciale.

### Interopérabilité protocolaire

La révision courante de MCP est 2026-07-28 **[34]**. Le projet publie un cadre officiel de tests de conformité, encore en versions 0.x (0.1.16 sur le tag latest de npm, préversions 0.2.0-alpha en cours) **[225, 226]** : ses résultats sont utiles, mais l’entreprise les complète par ses propres scénarios (EXIG-APP-03). Pour A2A 1.0, la trousse officielle a2a-tck, encore en préversion, teste les trois liaisons standard selon les niveaux MUST, SHOULD et MAY, à partir des interfaces déclarées dans la carte d’agent **[243]**. Le fournisseur précise enfin comment il suivra les dépréciations : MCP maintient une fonctionnalité dépréciée au moins douze mois, ou au moins 90 jours en cas de retrait accéléré pour un risque de sécurité actif (avis de sécurité publié ou exploitation documentée), avant de pouvoir la retirer **[34, 196]**.

### Observabilité et données de coûts

Les conventions GenAI d’OpenTelemetry sont toutes au niveau de stabilité Development et ont été déplacées en mai 2026 (déclarées obsolètes dans semantic-conventions à la v1.42.0, le 12 juin 2026) vers un dépôt dédié qui n’a encore publié aucune version étiquetée **[180, 181, 462]**. « Compatible OpenTelemetry » ne suffit donc pas : le fournisseur déclare la version qu’il émet, et l’entreprise vérifie la propagation du contexte de trace à chaque saut. Par exemple, le SDK Python de Microsoft Agent Framework propage le contexte W3C vers les serveurs MCP que l’agent ouvre lui-même, mais pas vers les outils MCP hébergés par un fournisseur **[295]**. Pour les coûts, FOCUS *(FinOps Open Cost and Usage Specification)* 1.4 (ratifiée le 4 juin 2026) normalise les données de facturation, sans définir d’indicateurs par agent **[408, 463, 464]**; FOCUS 1.5, dont la ratification est prévue le 3 décembre 2026, prévoit, dans son brouillon de travail, l’identité du modèle et le détail des jetons **[465]**. Le coût par tâche réussie se calcule en joignant ces données à la télémétrie (section 10.6).

### Identité, délégation et arrêt

Le cadre exige une identité non humaine distincte par agent (section 9.2); la réutilisation d’identités (NHI9) et les secrets de longue durée (NHI7) figurent au Top 10 des identités non humaines de l’OWASP **[91]**. MCP impose un jeton propre à chaque serveur et interdit de relayer un jeton reçu, mais n’exige ni l’échange de jetons de la RFC 8693 ni la revendication `act` **[209]** : la délégation vérifiable relève donc d’une exigence contractuelle distincte (EXIG-APP-08). Le cadre retient en outre, comme grille informative d’évaluation d’une passerelle d’agents (section 9.4), sept portes de conception d’un plan de contrôle d’agents, dont la neutralité de l’application des politiques au niveau du transport et la propagation vérifiée de l’identité humaine déléguée (choix du cadre, inspiré d’un billet de MuleSoft, argument d’éditeur).

### Performance mesurée, pas annoncée

Les chiffres publiés par les fournisseurs (TrueFoundry **[143, 144]**, agentgateway **[142]**) ne se comparent pas, pour les raisons que donne l’encadré de la section 9.4, et l’EXIG-APP-04 en tire la règle d’évaluation.

`EXIG-APP-03` **· DOIT**

**Preuves de conformité protocolaire**

L’architecture d’entreprise **DOIT** exiger du fournisseur qu’il démontre la prise en charge de MCP 2026-07-28 et, pour toute solution qui délègue ou reçoit des tâches entre agents, d’A2A 1.0, par des essais reproductibles dans l’environnement de l’entreprise : rapport a2a-tck sans échec de niveau MUST pour chaque liaison déclarée, scénarios de conformité MCP exécutés avec le cadre officiel ou une suite équivalente approuvée par l’architecture d’entreprise, chaque suite épinglée à une étiquette et, tant qu’elle est en préversion, bloquante seulement pour les tests restés stables pendant deux versions (EXIG-GOV-19), et liste explicite des primitives, liaisons et versions non prises en charge.

Pourquoi : « prend en charge » couvre souvent une partie seulement du protocole (tableau 53).

`EXIG-APP-04` **· DOIT**

**Mesures de performance reproductibles**

Toute valeur de latence ajoutée, de débit ou de disponibilité invoquée par un fournisseur **DOIT** être mesurée dans les conditions de l’entreprise, politiques, traçage et journalisation actifs, aux 50e et 99e centiles (P50 et P99), avec la méthode, le matériel, le type de trafic et les données brutes. Une valeur publiée par le fournisseur **NE DOIT PAS** servir d’exigence ni de critère de notation.

Pourquoi : les allégations publiques sont incomparables, parfois contradictoires.

`EXIG-APP-05` **· DOIT**

**Télémétrie et données de coûts ouvertes**

L’architecture d’entreprise **DOIT** exiger que la solution exporte traces, métriques et journaux par OTLP selon une version des conventions GenAI qu’elle déclare et que le catalogue consigne, avec le réglage d’ `OTEL_SEMCONV_STABILITY_OPT_IN` (EXIG-OBS-01), qu’elle propage le contexte W3C Trace Context sur chaque saut qu’elle contrôle et qu’elle fournisse ses données de facturation au format FOCUS 1.4 ou ultérieur, avec la correspondance entre ses unités propres (crédits, messages) et les jetons consommés.

Pourquoi : sans traces ni coûts exportables, l’entreprise ne peut ni auditer ses agents ni comparer ses fournisseurs (section 10.1).

`EXIG-APP-06` **· DOIT**

**Identité et arrêt sous le contrôle de l’entreprise**

L’architecture d’entreprise **DOIT** exiger que la solution attribue à chaque agent une identité non humaine distincte, fédérable au fournisseur d’identité de l’entreprise et sans clé statique partagée, et permette à l’entreprise de suspendre ou de révoquer un agent, ses jetons et ses sessions depuis ses propres outils, par exemple au moyen d’événements CAEP **[344]**, sans attendre une intervention du fournisseur, dans le délai de l’EXIG-IAM-20. Ce mécanisme est celui que décrit la fiche d’un agent intégré à un logiciel-service (EXIG-ARC-02).

Pourquoi : un coupe-circuit qui dépend de la console d’un éditeur n’est pas un coupe-circuit d’entreprise (section 9.4).

## 13.3 Clauses contractuelles normatives

Les dix clauses suivantes sont des exigences minimales. Elles s’insèrent dans tout contrat d’acquisition ou de renouvellement visé par ce chapitre; leur rédaction juridique relève des affaires juridiques. Les délais marqués « cible du cadre » sont des choix internes, ajustables par dérogation (section 11.6). Une dérogation qui porte sur un engagement contractuel (délai négocié sous la cible, extension obligatoire admise par l’EXIG-APP-02, offre retenue malgré un échec éliminatoire selon l’EXIG-APP-17) prend la forme d’un écart contractuel : le comité le décide; il vaut jusqu’à l’échéance du contrat, sans la limite de six mois de l’EXIG-GOV-16; il est inscrit au registre et revu à chaque renouvellement. Aucune dérogation ni aucun écart contractuel ne peut porter sur ce que les clauses 4 à 6 reprennent d’une obligation légale (art. 17 et 18.3 de la Loi sur le privé; EXIG-GOV-17). Dans ce chapitre, « Loi sur le privé » désigne la Loi sur la protection des renseignements personnels dans le secteur privé (RLRQ, c. P-39.1).

**DROIT APPLICABLE**

L’entreprise demeure responsable des renseignements personnels qu’elle confie à un fournisseur, y compris en cas d’incident **[414]**. La Loi sur le privé ne prévoit pas de responsabilité « conjointe » : elle impose un contrat écrit qui encadre le mandataire (art. 18.3) **[56]**. Les clauses donnent à l’entreprise les moyens de remplir ses propres obligations (section 12.2).

`EXIG-APP-07` **· DOIT**

**Clause 1 — Interopérabilité ouverte et portabilité des cartes**

Le contrat **DOIT** engager le fournisseur à prendre en charge A2A 1.0 en entrée et en sortie pour toute délégation entre agents; à publier des cartes d’agent conformes à la spécification A2A, dont le fichier `a2a.proto` est la définition normative, à l’adresse `/.well-known/agent-card.json` pour les agents exposés; à n’exiger aucune extension propriétaire pour déléguer une tâche à un agent tiers ou en recevoir une; et à maintenir une version de protocole dépréciée au moins pendant la période prévue par la spécification ou, à défaut, pendant 12 mois (cible du cadre), avec préavis écrit avant son retrait.

Pourquoi : avec A2A 1.0 natif et sans extension imposée, l’entreprise change de fournisseur sans réécrire ses délégations; le schéma de la carte relève de la spécification A2A, non d’un éditeur ni d’un autre projet **[68]**.

`EXIG-APP-08` **· DOIT**

**Clause 2 — Conformité MCP et délégation d’identité**

Le contrat **DOIT** exiger que tout outil ou connecteur exposé par le fournisseur respecte MCP 2026-07-28 et sa spécification d’autorisation : paramètre `resource` de la RFC 8707, jeton propre à chaque serveur, interdiction de relayer un jeton reçu **[71, 209]**. Il **DOIT** exiger en outre, comme engagement distinct de la conformité MCP, l’acceptation de jetons délégués émis par échange de jetons (RFC 8693) dont la revendication `act` identifie l’acteur courant; l’intersection des droits porte sur `sub` et sur l’`act` externe, et les acteurs imbriqués ne servent qu’à l’audit (RFC 8693, section 4.1) **[69]**. La prise en charge de l’extension Enterprise-Managed Authorization **PEUT** être valorisée dans la notation de la ligne « Identité et délégation » **[178]**.

Pourquoi : sans jeton délégué qui identifie le mandant et l’acteur courant, l’intersection des droits du mandant et de l’agent ne peut pas s’appliquer (section 9.3).

`EXIG-APP-09` **· DOIT**

**Clause 3 — Télémétrie exportable et explicabilité**

Le contrat **DOIT** garantir à l’entreprise un accès continu aux traces et aux journaux d’exécution de ses agents, y compris la version exacte du modèle, les outils appelés et les approbations. Pour toute décision concernant une personne, le fournisseur **DOIT** fournir de quoi l’informer des renseignements personnels utilisés et des raisons, principaux facteurs et paramètres de la décision (art. 12.1, qui vise les décisions fondées exclusivement sur un traitement automatisé; l’étendre à toute décision est un choix du cadre), et de quoi soutenir la révision par un membre du personnel, dans un délai fixé (cible du cadre : 10 jours); il **DOIT** restituer ces éléments à l’entreprise, qui les conserve à son dossier de décision au moins un an après la décision (art. 11, EXIG-OBS-11), et permettre ainsi de répondre aux demandes d’accès dans les 30 jours (art. 32) **[56]**.

Pourquoi : l’obligation d’expliquer reste à l’entreprise; elle vise les facteurs déterminants, non l’algorithme **[318]**.

`EXIG-APP-10` **· DOIT**

**Clause 4 — Usage limité au mandat et interdiction d’entraînement**

Le contrat **DOIT** préciser les mesures de confidentialité, limiter l’usage des renseignements à l’exécution du mandat et en interdire la conservation après son échéance, sous réserve des restitutions de l’EXIG-APP-14 et du gel notifié par l’entreprise (art. 18.3) **[56]**. Il **DOIT** aussi interdire expressément d’utiliser les données de l’entreprise (invites, contextes, sorties, traces, mémoires, plongements vectoriels) pour entraîner, ajuster ou évaluer des modèles du fournisseur ou de tiers, sauf autorisation écrite distincte, et fixer la conservation des invites et des sorties chez le fournisseur, détection des abus comprise : nulle, ou bornée et déclarée.

Pourquoi : la loi ne nomme pas l’entraînement; l’interdiction explicite découle de la limitation au mandat et ferme toute ambiguïté.

`EXIG-APP-11` **· DOIT**

**Clause 5 — Résidence, transferts et lois étrangères**

Le contrat **DOIT** déclarer chaque lieu de traitement ou de conservation des données de l’entreprise (inférence, outils, mémoires, journaux, sous-traitants), prévoir un préavis écrit de tout changement (cible du cadre : 90 jours), constituer, après une EFVP qui conclut à une protection adéquate, l’entente écrite exigée par l’article 17 de la Loi sur le privé **[56]** lorsque des renseignements personnels sont communiqués hors du Québec, autres provinces comprises, ou confiés à un tiers établi hors du Québec pour traitement ou conservation, et documenter l’exposition du fournisseur à des lois étrangères d’accès aux données, avec les mesures compensatoires retenues, par exemple un chiffrement à clés tenues hors de portée du fournisseur et l’épinglage régional du traitement, sans inférence interrégionale **[416]**.

Pourquoi : le *Clarifying Lawful Overseas Use of Data Act* (CLOUD Act) des États-Unis oblige un fournisseur qui y est assujetti à divulguer les données sous sa garde ou son contrôle, où qu’elles soient **[417]**; le gouvernement fédéral reconnaît que le stockage au Canada ne suffit pas à écarter la compétence de tribunaux étrangers, tout en ne relevant aucun cas documenté de gouvernement étranger cherchant à accéder aux données d’entreprises canadiennes détenues par des fournisseurs **[418]**. L’EFVP pondère ce risque.

`EXIG-APP-12` **· DOIT**

**Clause 6 — Notification d’incident**

Le contrat **DOIT** obliger le fournisseur à aviser sans délai le RPRP de l’entreprise de toute violation ou tentative de violation des obligations de confidentialité (art. 18.3) et à aviser l’entreprise sans délai, et au plus tard dans le délai que le contrat fixe (cible du cadre : 24 heures après la prise de connaissance par le fournisseur), de tout incident touchant ses données, ses identités ou ses agents, y compris une action d’agent non autorisée, une injection réussie ou une fuite par un outil; à transmettre les éléments requis pour l’avis à la Commission d’accès à l’information (CAI) et pour le registre des incidents; et à préserver les preuves et les versions en cause tant que dure le gel notifié par l’entreprise (EXIG-CON-23). Pour une institution financière fédérale, que l’avis au BSIF astreint à 24 heures ou moins, le contrat **DEVRAIT** fixer un délai plus court (cible du cadre : quatre heures).

Pourquoi : le mandataire doit aviser sans délai de toute violation (art. 18.3), et l’entreprise doit aviser la CAI « avec diligence » lorsque l’incident présente un risque de préjudice sérieux (art. 3.5), la loi ne fixant aucun délai en heures **[56]**; la cible de 24 heures reprend l’ordre de grandeur du délai de signalement au BSIF sans suffire à le respecter à elle seule : l’avis exige 24 heures ou moins, sans fixer le point de départ, d’où le délai plus court que le contrat d’une institution financière fédérale devrait fixer **[434]** (section 12.8).

`EXIG-APP-13` **· DOIT**

**Clause 7 — Audit, sécurité et transparence des changements**

Le contrat **DOIT** accorder à l’entreprise un droit de vérification, l’accès aux résultats des évaluations de sécurité et d’équipe rouge des composants agentiques, fondées au minimum sur l’OWASP Top 10 for Agentic Applications 2026 **[28]**, la liste à jour des modèles, serveurs MCP, agents et sous-traitants intégrés avec leurs versions, un préavis écrit d’au moins 90 jours (cible du cadre) avant tout retrait ou changement de version de modèle, y compris derrière un alias, que le fournisseur en juge ou non le comportement modifié, et l’accès à la version en cause pendant toute enquête d’incident (EXIG-CON-23).

Pourquoi : un changement de modèle ou de fournisseur peut exiger la mise à jour de l’EFVP **[413]** et, dans les institutions financières fédérales, la revue prévue par la ligne directrice E-23, qui inclut les modèles de fournisseurs **[8]**; le NIST AI RMF demande des politiques sur les risques de tiers (GOVERN 6.1) **[74]**.

`EXIG-APP-14` **· DOIT**

**Clause 8 — Réversibilité et sortie**

Le contrat **DOIT** prévoir qu’à l’échéance, à la résiliation ou sur demande, le fournisseur restitue dans des formats ouverts, structurés et documentés les mémoires des agents (épisodique, sémantique, procédurale), les graphes de connaissances, les définitions d’agents (invites système, cartes, compétences, flux, politiques), la configuration des outils, les journaux d’audit, les traces, les index vectoriels, les jeux d’évaluation, les artefacts d’ajustement autorisés, les preuves d’approbation signées et les éléments de décision (EXIG-APP-09); qu’il prête assistance pendant une période de transition (cible du cadre : six mois); puis qu’il détruise les données après la restitution attestée, et l’atteste par écrit. La destruction est suspendue pendant toute enquête, tout gel (EXIG-CON-23) ou toute conservation pour litige notifiés par l’entreprise.

Pourquoi : la mémoire et les définitions forment l’actif que l’entreprise doit garder (section 5.5); la loi exige que le contrat prévoie que le mandataire ne conserve pas les renseignements après le mandat **[56]**.

`EXIG-APP-15` **· DOIT**

**Clause 9 — Accord écrit au sens de l’article 25(4) du RIA**

Lorsque l’entreprise est fournisseur d’un système d’IA à haut risque au sens du règlement européen sur l’IA (RIA), ou le devient, notamment en y apposant son nom, en le modifiant substantiellement ou en réaffectant un agent à un usage de l’annexe III (art. 25(1)), le contrat avec chaque tiers qui fournit un outil, un service, un composant ou un modèle intégré **DOIT** constituer l’accord écrit exigé par l’article 25(4), tel que modifié par le règlement (UE) 2026/1744 **[58, 61]**. Le cadre y exige au minimum la documentation technique, l’accès aux journaux, l’accès pour essais et l’assistance en cas d’incident. Les outils, services, processus et composants rendus publics sous licence libre et ouverte sont exemptés de l’accord, sauf s’il s’agit de modèles d’IA à usage général; pour un tel composant, ou pour un modèle à usage général dont le fournisseur refuse l’accord, l’entreprise s’appuie sur la documentation que ce fournisseur doit fournir (art. 53) ou recourt à une dérogation (section 11.6).

Pourquoi : ces obligations visent les systèmes de l’annexe III à compter du 2 décembre 2027 et ceux de l’annexe I à compter du 2 août 2028 **[57]** (section 12.4).

`EXIG-APP-16` **· DOIT**

**Clause 10 — Révocation des identités non humaines**

Le contrat **DOIT** prévoir, à la suspension d’un agent, l’invalidation côté fournisseur de ses jetons, consentements, abonnements de notification et webhooks dans le délai de l’EXIG-IAM-20, réception des événements CAEP comprise; et, à la fin du contrat, la révocation par le fournisseur, dans les 24 heures qui suivent la fin de la période de transition de l’EXIG-APP-14 (cible du cadre), ou sans délai en cas de faute ou d’incident, de toutes les identités non humaines, justificatifs, jetons, consentements OAuth, abonnements de notification et webhooks liés à l’entreprise, avec attestation écrite. La coupure côté entreprise passe par le mécanisme de l’EXIG-APP-06, sans attendre le fournisseur. L’entreprise **DOIT** révoquer de son côté les accès qu’elle a accordés et vérifier l’absence d’accès résiduel.

Pourquoi : le retrait inadéquat est le premier risque du Top 10 NHI de l’OWASP (NHI1) **[91]**; le NIST AI RMF prévoit un déclassement sécuritaire (GOVERN 1.7) **[74]**, et le livre blanc de l’OpenID Foundation (section 2.9) recommande un retrait formel propagé à tous les systèmes intégrés **[311]**.

**Aucune clause contraire à l’EXIG-GOV-17 (application de l’EXIG-APP-12).** Un contrat conclu ou renouvelé après l’adoption du cadre **NE DOIT PAS** comporter de clause contraire à un point de l’EXIG-GOV-17. Un engagement contractuel en vigueur à l’adoption ne prime sur le cadre que pour une transition bornée, inscrite au registre, et jamais sur un point de l’EXIG-GOV-17 (section 4.3). Pourquoi : une clause d’éditeur ne peut pas écarter ce qu’aucune dérogation interne ne peut écarter; sinon un contrat signé après l’adoption suffirait à exécuter des actions P3 sans approbation.

## 13.4 Grille d’évaluation

La grille du tableau 54 rend les offres comparables. Chaque critère reçoit une note de 0 à 3 : 0, absent ou non démontré; 1, partiel ou inscrit à une feuille de route datée; 2, démontré par le fournisseur; 3, démontré par un essai reproductible de l’entreprise. Lorsqu’une exigence impose un essai de l’entreprise (EXIG-APP-03, EXIG-APP-04, EXIG-APP-06), la note d’un critère que l’entreprise n’a pas vérifié est plafonnée à 1. La preuve d’un autre critère qui suppose un agent pilote (coûts, réversibilité) peut être cotée provisoirement à 2, sur la démonstration du fournisseur, et se confirme au premier pilote. Un critère est en échec si sa note est inférieure à 3 lorsqu’une exigence impose un essai de l’entreprise, et inférieure à 2 ailleurs. Le refus d’une clause DOIT de la section 13.3 est un échec éliminatoire, quel que soit le score. Un critère, ou une partie de critère, sans objet pour la solution évaluée (un serveur MCP n’a pas de carte d’agent; un composant libre et gratuit n’a pas de facturation) est coté « Sans objet » avec justification, comme à l’annexe A, et son poids est réparti au prorata entre les autres critères. Le score est la moyenne pondérée des notes. Une offre est admissible si elle n’échoue à aucun critère éliminatoire; le cadre ne fixe pas de seuil de score, puisqu’une offre sans échec éliminatoire dépasse toujours 2,0, et le score sert à classer les offres admissibles. La colonne « Applicable à » désigne les types de solution que vise chaque critère (plateforme, agent, service de modèles, passerelle, serveur MCP); pour un autre type, le critère, ou sa partie visée, est coté « Sans objet ». Les pondérations sont indicatives : selon la classe la plus élevée des agents visés par l’acquisition, le comité peut les rééquilibrer d’au plus 5 points par critère, en le justifiant, la somme des poids demeurant égale à 100 et un critère éliminatoire gardant un poids d’au moins 5.

*Tableau 54 — Grille d’évaluation des fournisseurs de solutions agentiques*

| **Critère** | **Ce qui est évalué** | **Applicable à** | **Preuve attendue** | **Poids** | **Éliminatoire** |
| --- | --- | --- | --- | --- | --- |
| Interopérabilité protocolaire | MCP 2026-07-28; A2A 1.0 natif pour toute solution qui délègue ou reçoit des tâches; primitives et liaisons couvertes; extensions | Plateforme, agent, passerelle, serveur MCP (MCP); plateforme et agent qui délèguent ou reçoivent des tâches (A2A); sans objet pour un service de modèles | Rapport a2a-tck, résultats de conformité MCP, liste des écarts | 20 | **Oui** |
| Identité et délégation | Identité par agent, fédération, jetons délégués, révocation par l’entreprise | Toutes | Démonstration dans le locataire de l’entreprise; essai de révocation chronométré, comparé à la cible de l’EXIG-IAM-20 | 15 | **Oui** |
| Sécurité et chaîne d’approvisionnement | Garde-fous, bacs à sable, inventaire versionné des composants, équipe rouge | Toutes | Rapports d’essai; inventaire; droit d’audit (clause 7) | 15 | **Oui** |
| Observabilité et audit | OTLP, conventions épinglées, propagation du contexte, journal d’audit exportable | Toutes | Trace complète sur les sauts que la solution contrôle, et liste des ruptures, produites pendant l’essai | 15 | **Oui** |
| Données, résidence et conformité | Lieux de traitement, article 17, interdiction d’entraînement, article 12.1, incidents | Toutes | Clauses 3 à 6 acceptées; carte des flux pour l’EFVP | 15 | **Oui** |
| Réversibilité | Formats de restitution, assistance, délai de sortie | Toutes | Essai de restitution sur un agent pilote | 10 | **Oui** |
| Coûts et FinOps | Données FOCUS, unités propres, plafonds par agent (EXIG-APP-05, EXIG-FIN-03, EXIG-FIN-05) | Toutes, sauf un composant libre et gratuit | Export FOCUS d’un mois de pilote (sans objet pour un composant libre et gratuit) | 5 | **Oui** |
| Performance mesurée | Latence ajoutée P50 et P99, débit, disponibilité | Toutes | Banc d’essai reproductible de l’entreprise (EXIG-APP-04) | 5 | Non |

`EXIG-APP-17` **· DOIT**

**Application de la grille**

Toute acquisition visée par ce chapitre **DOIT** être évaluée avec la grille du tableau 54. Une offre en échec sur un critère éliminatoire, au sens de la section 13.4, ou qui refuse une clause DOIT de la section 13.3, **DOIT** être écartée, sauf dérogation approuvée, sous la forme d’un écart contractuel (section 13.3). La grille remplie et ses preuves **DOIVENT** être conservées au registre (section 11.4) et réévaluées à chaque renouvellement de contrat.

Pourquoi : une grille commune rend les décisions traçables et comparables d’une acquisition à l’autre.
