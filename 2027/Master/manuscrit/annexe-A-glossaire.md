# Annexe A — Glossaire français-anglais

> Les termes sont ceux qu'emploient les chapitres; le numéro entre parenthèses renvoie au chapitre qui traite la notion. Les équivalents anglais viennent des spécifications et de la documentation citées. Les noms propres de protocoles et d'objets normalisés (Agent Card, Task, SD-JWT) restent en anglais.

Classement par thème, puis alphabétique. Chaque définition fixe l'usage du mot dans l'ouvrage, pas une norme.

## A.1 Agents et orchestration

| Français | Anglais | Sens retenu |
|---|---|---|
| agent | agent | Logiciel dirigé par un modèle de langage, qui utilise des outils en boucle et choisit ses étapes (1) |
| agent borné | bounded agent | Agent qui choisit outils, ordre et paramètres dans une liste fermée, sous un plafond (17) |
| agent d'utilisation d'interface graphique | computer-use agent (CUA) | Agent multimodal qui interprète l'écran et simule les clics et la frappe pour atteindre des applications patrimoniales sans API, sous contrôle (25) |
| assistant | assistant, copilot | Logiciel qui produit une réponse et laisse l'humain agir (1) |
| boucle réflexive | evaluator-optimizer, critic loop | Patron à deux rôles : un agent produit, un autre évalue et fait reprendre (16) |
| cadriciel | framework | Bibliothèque qui fournit la boucle d'agent et le workflow (20) |
| chorégraphie | choreography | Coordination sans coordinateur, par réaction à des événements (19). Les événements sont publiés sur un courtier (Kafka, Solace), et chaque agent y réagit de façon autonome. |
| compensation | compensation | Action qui répare l'effet d'une action déjà exécutée (18) |
| exécution durable | durable execution | Garantie qu'un programme reprend après une panne, là où il s'était arrêté (18). Chaque étape complétée est consignée dans un journal d'événements immuable; après une panne matérielle ou logicielle, le processus reprend au dernier point de contrôle, sans réexécuter les effets de bord déjà commis. |
| harnais | harness | Boucle d'agent déjà réglée, livrée avec ses outils et ses consignes (20) |
| humain dans la boucle | human-in-the-loop | L'humain peut intervenir à chaque cycle de décision; la position s'attache à une action (22). Mode (HITL, niveau L2) qui exige une validation humaine explicite, préalable à chaque mutation engagée dans un système d'enregistrement. |
| humain sur la boucle | human-on-the-loop | L'humain intervient à la conception et surveille le fonctionnement (22). Mode (HOTL, niveau L3) où la flotte d'agents exécute de façon autonome les transactions comprises dans son enveloppe de politique et n'escalade vers l'opérateur humain que les exceptions qui franchissent un seuil quantifié de risque ou d'incertitude. |
| idempotence | idempotency | Propriété d'une opération dont la répétition ne change pas l'effet (18). La clé d'idempotence, identifiant unique et déterministe attaché à une intention de mutation, fait que des réessais d'un même appel d'outil produisent le même état final, sans dupliquer l'effet métier. |
| orchestrateur d'orchestrateurs | meta-orchestrator | Patron d'architecture qui fédère plusieurs moteurs d'agents spécialisés ou propriétaires (CRM, ERP, ITSM, usine) sous un plan de contrôle et de gouvernance transversal et neutre (27) |
| orchestration | orchestration | Coordination d'agents, d'outils et de personnes vers un résultat (16) |
| promesse durable | awakeable | Primitive d'un moteur d'exécution durable (Restate) qui suspend un flux pendant des heures ou des semaines, dans l'attente d'un signal externe ou d'une approbation humaine, et libère la mémoire vive et le processeur (18) |
| rejeu | replay | Relecture d'un journal pour reprendre, tester ou auditer une exécution (18, 19) |
| Saga | saga | Suite de transactions locales, chacune assortie d'une compensation (18). Elle gère des transactions distribuées de longue durée sans verrou global bloquant; en cas d'échec partiel, une chaîne ordonnée d'actions de compensation s'exécute en sens inverse. |
| superviseur | supervisor | Agent central qui répartit le travail entre d'autres agents (16) |
| système multi-agents | multi-agent system | Système où plusieurs agents coopèrent à une même tâche (16, 21) |
| topologie | topology | Répartition qui dit qui décide de l'étape suivante et qui voit quoi (16) |
| transfert | handoff | Passage du contrôle d'un agent à un autre (16) |
| workflow agentique | agentic workflow | Chemin fixé par le concepteur, dont certaines étapes sont confiées à un modèle (1, 17) |

## A.2 Protocoles et découverte

| Français | Anglais | Sens retenu |
|---|---|---|
| artefact | artifact | Livrable produit par une tâche A2A (6) |
| carte d'agent | Agent Card | Document qui décrit un agent de l'extérieur : compétences, interfaces, sécurité (6). Format JSON normalisé par A2A v1.0, généralement publié sous `/.well-known/agent-card.json`, avec les compétences sous `skills`. |
| client | client | Dans MCP, connecteur créé par l'hôte, lié à un seul serveur (5) |
| découverte | discovery | Trouver, décrire et authentifier une capacité avant de l'utiliser (8) |
| élicitation | elicitation | Demande d'information adressée à l'utilisateur par un serveur MCP (5) |
| espace de noms | namespace | Préfixe qui rattache un nom à son propriétaire vérifié (8) |
| extension | extension | Ajout facultatif à un protocole, désactivé par défaut (5) |
| hôte | host | Application d'IA qui crée les clients MCP et applique le consentement (5) |
| liaison | binding | Correspondance entre des opérations abstraites et un transport (6) |
| outil | tool | Fonction décrite par un nom, une description et un schéma, que le modèle peut invoquer (5) |
| passerelle | gateway | Intermédiaire placé sur le chemin de chaque appel, qui applique les politiques (24) |
| registre | registry | Catalogue de serveurs ou d'agents, avec leurs métadonnées (8). Pour les agents d'entreprise, catalogue faisant autorité où chaque agent figure avec son propriétaire métier nominatif, son identité non humaine (NHI), sa version SemVer + Intent, ses outils autorisés et sa cote de risque réglementaire. |
| sans état | stateless | Protocole où chaque requête porte tout ce qu'il faut pour la traiter (5) |
| serveur | server | Dans MCP, service qui expose des outils, des ressources et des prompts (5) |
| sous-registre | subregistry | Registre dérivé d'un registre amont, qui y ajoute curation et politiques (8, 27) |
| tâche | task | Unité de travail à état, suivie par un identifiant (5, 6) |

## A.3 Données, contexte et mémoire

| Français | Anglais | Sens retenu |
|---|---|---|
| cache de prompts | prompt caching | Préfixe de contexte déjà traité, gardé en cache et relu à prix réduit (13, 40, 44) |
| compilation déclarative de consignes | declarative prompt compilation | Approche, illustrée par DSPy, qui remplace les consignes rédigées à la main par des signatures typées, optimisées automatiquement contre une métrique d'évaluation objective (20, 47) |
| contrat de données | data contract | Entente lisible par machine entre producteur et consommateurs d'une donnée (15). Dans sa forme exécutable (ODCS), le producteur s'engage sur le schéma, les bornes d'unités physiques, la stabilité statistique et l'alignement ontologique d'un jeu consommé par des agents aval. |
| couche anticorruption | anti-corruption layer | Couche de traduction qui isole un modèle du système qu'il appelle (25) |
| couche sémantique | semantic layer | Définition partagée des métriques, compilée en requêtes (12). Strate d'abstraction normalisée (Apache Ossie) qui fixe aussi, de façon unique et déterministe, les dimensions d'analyse et la nomenclature des données pour toute l'entreprise. |
| découverte progressive | progressive discovery | Chargement des outils et ressources au fil des besoins (13) |
| dégradation contextuelle | context rot | Baisse progressive de la précision du raisonnement et du respect des consignes à mesure que la fenêtre de contexte s'allonge d'historiques bruts, redondants ou contradictoires (13) |
| fenêtre de contexte | context window | Texte que le modèle peut lire en un appel (13) |
| graphe de connaissances bi-temporel | bi-temporal knowledge graph | Mémoire (Graphiti) qui enregistre séparément l'intervalle de validité d'un fait dans le monde métier (`valid_from` / `valid_to`) et l'instant de son ingestion par le système, pour que les agents ne raisonnent pas sur des faits périmés (14) |
| ingénierie du contexte | context engineering | Discipline qui règle la composition, le moment, le format et la durée de vie de l'information en contexte (13). Elle filtre selon les droits d'accès (ACL), compresse et vérifie dynamiquement l'information fournie à l'agent à chaque étape. |
| mémoire épisodique | episodic memory | Expérience des cycles antérieurs : historiques, trajectoires (14) |
| mémoire procédurale | procedural memory | Savoir-faire : poids du modèle et code de l'agent; la plus risquée à écrire (14) |
| mémoire sémantique | semantic memory | Savoir de l'agent sur le monde et sur lui-même (14) |
| ontologie | ontology | Modèle formel de concepts, de relations et de règles d'un domaine (12). Pour l'entreprise, elle couvre les entités métiers, leurs relations causales, leurs transitions d'états légales et les préconditions d'actions, et donne aux agents un modèle déterministe du monde de l'organisation. |
| skill | skill (Agent Skills) | Dossier `SKILL.md` d'instructions, de scripts et de ressources, chargé par divulgation progressive (13) |
| système d'enregistrement | system of record | Système dont la donnée fait foi (25) |
| systèmes patrimoniaux | legacy systems | Systèmes anciens encore en service, dont l'ordinateur central (25) |
| type de données répliqué sans conflit | conflict-free replicated data type (CRDT) | Structure de données distribuée dont les opérations concurrentes, effectuées hors ligne, convergent mathématiquement vers le même état déterministe quand un nœud en périphérie se reconnecte (46) |
| Write-Audit-Publish | Write-Audit-Publish (WAP) | Patron transactionnel de lakehouse : toute nouvelle ingestion est écrite sur une branche isolée, invisible des agents aval jusqu'à la réussite complète des validations du contrat de données (47) |

## A.4 Identité et autorisation

| Français | Anglais | Sens retenu |
|---|---|---|
| atténuation de portée | scope attenuation | Principe de délégation d'un utilisateur vers un orchestrateur, puis vers un sous-agent : chaque maillon aval reçoit un jeton dont les permissions forment un sous-ensemble strict, limité aux besoins immédiats de sa sous-tâche; aucune norme adoptée ne la garantit de saut en saut (30) |
| chaînage d'identité | identity and authorization chaining | Octroi JWT émis dans un domaine, que l'autre convertit en jeton d'accès (29) |
| charge de travail | workload | Logiciel en exécution, identifié sans mot de passe humain (29) |
| délégation | delegation | Fait d'agir au nom d'autrui, l'agent restant identifiable (29, 30) |
| élévation progressive | step-up authorization | Droit supplémentaire demandé quand une opération l'exige (30) |
| fournisseur d'identité | identity provider | Service qui authentifie et émet les assertions d'identité (29) |
| identité non humaine | non-human identity (NHI) | Identité machine vérifiable cryptographiquement, attribuée en propre à un agent ou à un serveur d'outils, avec un cycle de vie, un propriétaire humain responsable et des politiques de moindre privilège (29, 30) |
| jeton | token | Preuve d'un droit d'accès, à portée et à durée limitées (29, 30) |
| justificatif | credential | Ce qui prouve une identité ou un droit : clé, certificat, jeton (29) |
| mandat | mandate | Justificatif signé qui atteste ce qu'un utilisateur a approuvé pour un achat (10) |
| moindre privilège | least privilege | Principe qui limite chaque droit à ce que la tâche exige (30) |
| parrain | sponsor | Représentant d'affaires qui répond d'un agent; obligatoire chez Entra (29) |
| point d'application | policy enforcement point | Composant qui intercepte la requête et applique la décision (30). En architecture zero trust, passerelle en ligne (agentgateway) qui intercepte et bloque la requête non conforme. |
| point de décision | policy decision point | Composant qui évalue la politique et rend la décision (30). En architecture zero trust, moteur déterministe qui statue sur l'autorisation d'un appel d'outil (Cedar, OPA). |
| serveur d'autorisation | authorization server | Service qui émet les jetons selon la politique (30) |
| serveur de ressources | resource server | Service qui détient la ressource et vérifie le jeton (30) |
| usurpation | impersonation | Échange de jetons où l'agent se confond avec l'utilisateur et disparaît des journaux (29) |

## A.5 Sécurité et assurance

| Français | Anglais | Sens retenu |
|---|---|---|
| délégué confus | confused deputy | Vulnérabilité classique, que les architectures agentiques amplifient : un agent légitime, doté de privilèges élevés, est manipulé par une entrée externe non fiable et exerce ses droits au profit d'un attaquant (31) |
| architecture Simplex | Simplex architecture | Sous-système simple et vérifié qui écarte les commandes risquées d'un composant complexe (46). Patron de sûreté robotique (IEC 61508) : un moniteur matériel déterministe et isolé peut couper un contrôleur IA adaptatif au profit d'un contrôleur d'arrêt sûr certifié. |
| attestation | attestation | Preuve matérielle que la configuration matérielle et logicielle est celle attendue (46) |
| bac à sable | sandbox | Environnement isolé qui borne ce que du code peut atteindre (31). Isolation matérielle ou logicielle (microVM Firecracker, OpenSandbox, WebAssembly/WASI) où s'exécutent le code généré et les outils tiers, sans accès implicite au système hôte ni au réseau interne. |
| biais et complaisance d'automatisation | automation bias, rubber-stamping | Tendance d'un opérateur humain trop sollicité à approuver machinalement les recommandations fluides et persuasives d'un agent (OWASP ASI09); elle prive d'effet un contrôle HITL mal calibré (22) |
| coupe-circuit | kill switch | Mécanisme d'urgence piloté par le centre d'opérations de sécurité (SOC) : il révoque immédiatement les jetons OAuth, suspend les sagas actives et isole un agent ou un serveur MCP compromis (32) |
| détention exclusive de clé en HSM | Hold Your Own Key (HYOK) | Modèle cryptographique souverain : les clés maîtresses de chiffrement d'état et de pseudonymisation résident exclusivement dans un module matériel (HSM) sous contrôle juridique du client, hors de portée de l'opérateur infonuagique (46) |
| empoisonnement de mémoire | memory & context poisoning | Écriture malveillante en mémoire, à effet différé (14, 31) |
| empoisonnement d'outil | tool poisoning | Instruction cachée dans la description d'un outil (31). Attaque par injection indirecte dont les directives malveillantes se cachent aussi dans les schémas de paramètres et dans les charges utiles qu'un serveur MCP retourne. |
| environnement d'exécution de confiance | trusted execution environment | Zone isolée par le matériel, souvent une machine virtuelle entière, qui protège la donnée en calcul des logiciels et opérateurs de l'exploitant, guère d'un accès physique (45, 46). Chiffré par le matériel (AMD SEV-SNP, Intel TDX, NVIDIA H100/B200 CC) et attesté par racine silicium, il permet l'inférence souveraine sans exposer les données en clair à l'hébergeur. |
| garde-fous | guardrails | Contrôles qui bornent les entrées, les sorties ou les actions d'un agent (23, 34) |
| injection indirecte | indirect prompt injection | Consigne déposée par un tiers dans un contenu que l'agent lit (31) |
| invariant | invariant | Règle du système qui doit tenir sur toute la trajectoire (32) |
| piste d'audit | audit trail | Journal complet, jamais échantillonné, de qui a fait quoi et sous quelle autorité (30, 33) |
| rug-pull MCP | MCP rug pull | Attaque de chaîne d'approvisionnement : un serveur MCP externe, d'abord bénin lors de son homologation, modifie ensuite à distance le comportement ou la description de ses outils pour exfiltrer des données (31) |
| trifecta létale | lethal trifecta | Réunion de données privées, de contenu non fiable et d'un canal sortant (31) |
| zero trust | zero trust | Selon NIST SP 800-207, la confiance n'est jamais implicite et s'évalue en continu (32) |

## A.6 Architecture, exploitation et économie

| Français | Anglais | Sens retenu |
|---|---|---|
| banc d'essai | benchmark | Jeu de tâches à résultat vérifiable, répété pour comparer (33) |
| budget d'erreur | error budget | Marge d'échec admise, qui règle le rythme du changement et l'autonomie (34) |
| cache KV | KV cache | État de calcul d'un préfixe déjà traité, que le serveur d'inférence réutilise (44). Le partage de cache (KV-Cache Sharing), technique d'ordonnancement de l'inférence, achemine les tours successifs d'un même agent, ou d'agents qui partagent un long préfixe, vers les nœuds GPU qui détiennent déjà les tenseurs d'attention précalculés. |
| calcul d'inférence réflexif | test-time compute | Allocation dynamique de jetons et de cycles de délibération interne supplémentaires au moment de l'inférence, pour résoudre des problèmes complexes de planification, de vérification logique ou d'arbitrage entre plusieurs contraintes (44) |
| cascade | cascade | Petit modèle d'abord, escalade vers un grand après coup (44) |
| coût par résultat métier validé | cost-per-outcome | Métrique principale du FinOps agentique : coût total (inférence, mémoire, orchestration et API tierces) rapporté au nombre d'unités de valeur métier résolues sans reprise manuelle (40) |
| cycle de vie agentique | Agent Development Lifecycle (ADLC) | Discipline qui étend le SDLC classique et gère ensemble le code déterministe, les consignes système, le choix des modèles, les schémas d'outils MCP, les suites de simulation probabilistes et la surveillance comportementale continue (34) |
| délai du premier jeton | time to first token | Temps entre l'envoi de la requête et le début de la réponse (44) |
| dérive | drift | Évolution du comportement, brusque après un changement ou graduelle sans déclencheur (34, 35). La dérive sémantique est l'écart graduel entre le comportement effectif d'un système agentique en production et ses spécifications initiales, causé par l'évolution des données réelles, des modèles sous-jacents ou des API externes. |
| développement piloté par la spécification | spec-driven development | Pratique qui tire de la spécification un plan, des tâches, puis le code (47) |
| distillation | distillation | Entraînement d'un petit modèle (élève) sur les sorties d'un grand (enseignant) pour une tâche étroite (47). Le transfert est supervisé (SFT) et préférentiel (DPO) : les capacités du modèle enseignant passent à des adaptateurs légers LoRA (Multi-LoRA), servis à haute densité sur un petit modèle spécialisé d'entreprise. |
| exécution en miroir | experiment (Scientist) | Ancien et nouveau chemins exécutés sur les mêmes entrées; seul l'ancien sert (47). Appelée aussi shadow mirroring; appliquée au figuier étrangleur, elle réplique le trafic réel vers le nouveau service, sans commettre ses écritures, pour prouver une parité exacte avec le système patrimonial avant la bascule. |
| figuier étrangleur | strangler fig | Remplacement d'un système par parties, la parité de comportement servant de critère de sortie (25, 47) |
| gravité des données | data gravity | Principe d'urbanisation : les agents spécialistes de domaine se déploient au plus près des référentiels maîtres volumineux et réglementés qu'ils exploitent, plutôt que de dupliquer ces données vers un orchestrateur central (27) |
| infonuagique | cloud computing | Services informatiques fournis à la demande par un tiers (26) |
| ingénierie d'exploitation agentique | AgentOps | Pratiques, pipelines et contrôles opérationnels qui assurent la fiabilité, l'observabilité distribuée, l'évaluation continue et le déploiement sécurisé des systèmes multi-agents en production (34) |
| ingénierie du chaos agentique | agentic chaos engineering | Pratique qui injecte délibérément des pannes d'outils, des latences extrêmes, des réponses malformées et des tentatives d'injection adversariale, pour éprouver la résilience d'un système multi-agents avant et après sa mise en production (34) |
| juge automatique | automated judge | Modèle qui note la sortie d'un autre modèle (33) |
| jumeau numérique | digital twin | Modèle causal et physique, synchronisé avec une usine, un équipement ou une chaîne logistique; étape de simulation déterministe, obligatoire avant l'application d'une consigne issue d'un agent (28) |
| livelock conversationnel | livelock | Pathologie multi-agents : deux agents ou plus échangent indéfiniment des demandes de clarification ou des reformulations polies, sans jamais atteindre l'état terminal ni lever d'erreur technique (33) |
| maillage agentique | agentic AI mesh | Infrastructure qui rend les agents joignables et gouvernables (23) |
| métrique `pass^k` | `pass^k` | Mesure de fiabilité opérationnelle introduite dans l'écosystème τ-bench : probabilité qu'un agent réussisse les k essais indépendants d'une même tâche; `pass@k` se contente d'un seul succès sur k tentatives (33, 34) |
| mise à l'échelle | scaling | Passage d'un pilote à un usage étendu (4) |
| observabilité | observability | Capacité de reconstituer une exécution à partir de ses signaux (33) |
| oracle de caractérisation patrimoniale | golden master | Jeu immuable de dizaines de milliers d'entrées et de sorties historiques réelles, avec des cas limites, capturé sur un système central (RPG, COBOL); il prouve au centime près la parité fonctionnelle d'un service modernisé avant la bascule (47) |
| passerelle d'inférence | inference gateway | Passerelle Gateway API dotée d'un routage et d'un équilibrage de charge conscients du modèle (44) |
| petit modèle de langage spécialisé | small language model (SLM) | Modèle compact, sans définition admise de la taille, affiné ou distillé pour des tâches ciblées d'extraction, de routage ou de classification, à basse latence et à faible coût (44, 47) |
| plan de contrôle | control plane | Couche qui décide : registre, identité, politique, budgets (23) |
| plan de données | data plane | Couche qui exécute les décisions sur le chemin de chaque appel (23, 44) |
| reprise après sinistre cognitif | cognitive disaster recovery (cognitive DR) | Discipline de continuité d'activité qui garantit, en moins de quinze minutes (`RTO < 15 min`, `RPO = 0`), la bascule d'un fournisseur de modèle frontière défaillant ou retiré vers une grappe souveraine à poids ouverts, calibrée d'avance sur les mêmes contrats Open Responses et MCP (46) |
| retour arrière | rollback | Retour à une version ou à un état antérieur (34) |
| routage de modèles | model routing | Choix, avant l'appel, d'un modèle à la mesure de chaque étape (40, 44) |
| système d'action | system of action | Strate d'architecture dédiée à l'interprétation des événements, à la planification multi-agents durable et à l'exécution gouvernée d'actions transversales, au-dessus des systèmes d'enregistrement existants (1) |
| test de mutation | mutation testing | Faute injectée dans le code pour vérifier qu'un test échoue (47) |
| test par propriétés | property-based testing | Invariant vérifié sur des entrées générées (47) |
| trace | trace | Arbre de spans d'une exécution, qui sert au diagnostic et peut être échantillonné (33) |
| verrouillage | lock-in | Dépendance qui rend coûteux le changement de fournisseur (20, 27) |
| volant d'inertie cognitif | data flywheel | Boucle fermée et gouvernée qui convertit les traces de production validées par l'issue métier et les corrections humaines HOTL, après désidentification irréversible, en amélioration continue et en distillation de SLM (47) |

## A.7 Gouvernance et droit

| Français | Anglais | Sens retenu |
|---|---|---|
| clause de sortie | exit clause | Clause qui fixe ce qui se récupère en quittant un fournisseur (27) |
| connecteur | connector | Composant qui met en œuvre les échanges d'un espace de données chez chaque participant (37, 45) |
| empreinte de déploiement | deployment footprint | Règle de qualification juridique : le niveau de conformité applicable à un agent polyvalent se détermine d'après la criticité maximale des données et des systèmes aval auxquels il a effectivement accès (38) |
| espace de données | data space | Cadre de partage de données entre organisations, sous règles communes (37). Les données ne sont pas centralisées : des connecteurs normalisés (EDC) appliquent techniquement des contrats d'usage ODRL et vérifient les identités légales vLEI. |
| haut risque | high-risk | Catégorie de l'AI Act, définie par l'usage du système (35) |
| IA agentique fantôme | shadow agents | Agents autonomes que des employés créent ou connectent, par des outils infonuagiques ou des clés personnelles, à l'insu des équipes d'architecture, de sécurité et de conformité (43) |
| imputabilité | accountability | Obligation, pour une personne désignée, de répondre d'un agent (39) |
| inventaire | inventory | Liste tenue à jour des agents, de leurs droits et de leurs responsables (39) |
| prépublication | preprint | Article diffusé avant l'évaluation par les pairs (passim) |
| prolifération anarchique d'agents | agent sprawl | Multiplication non coordonnée d'agents autonomes dans les unités d'affaires et les suites de logiciels en tant que service, d'où des redondances fonctionnelles, des angles morts de sécurité et un dérapage des coûts d'inférence (29, 43) |
| rapprochement à trois voies | three-way matching | Concordance du bon de commande, de la réception et de la facture avant paiement (45) |
| salle blanche de données | data clean room | Environnement où ne s'exécute qu'un code approuvé par tous, et d'où ne sort qu'un résultat convenu (45). Elle s'appuie sur un environnement chiffré par le matériel pour la négociation interentreprises à plusieurs parties, sans exposer les données en clair à la contrepartie. |
| souveraineté numérique | digital sovereignty | Maîtrise du lieu, du droit applicable et des dépendances (37) |
| système décisionnel automatisé | automated decision system | Selon le projet de loi C-36, technologie qui appuie ou remplace le jugement de décideurs humains (38) |

## A.8 Sigles fréquents

| Sigle | Développé | Chapitre |
|---|---|---|
| A2A | Agent2Agent Protocol | 6 |
| AAIF | Agentic AI Foundation | 11 |
| ACP | Agent Communication Protocol, Agentic Commerce Protocol ou Agent Context Protocol | 6, 7, 10 |
| AP2 | Agent Payments Protocol | 10 |
| CRDT | Conflict-Free Replicated Data Type | 46 |
| DID | Decentralized Identifier | 7, 29 |
| DSP | Dataspace Protocol | 37, 45 |
| HYOK | Hold Your Own Key | 46 |
| ID-JAG | Identity Assertion JWT Authorization Grant | 5, 29 |
| MAST | Multi-Agent System Failure Taxonomy | 21 |
| MCP | Model Context Protocol | 5 |
| SEP | Specification Enhancement Proposal | 5, 11 |
| TEE | Trusted Execution Environment | 45, 46 |
| TTFT | Time to First Token | 44 |
| WIMSE | Workload Identity in Multi-System Environments | 11, 29 |
