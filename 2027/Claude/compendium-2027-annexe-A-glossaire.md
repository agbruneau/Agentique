# Annexe A — Glossaire français-anglais

> **Version 2 — 12 novembre 2026.** Les termes sont ceux qu'emploient les chapitres; le numéro entre parenthèses renvoie au chapitre qui traite la notion. Les équivalents anglais viennent des spécifications et de la documentation citées. Les noms propres de protocoles et d'objets normalisés (Agent Card, Task, SD-JWT) restent en anglais. Annexe auditée et révisée le 12 novembre 2026.

Classement par thème, puis alphabétique. Chaque définition fixe l'usage du mot dans l'ouvrage, pas une norme.

## A.1 Agents et orchestration

| Français | Anglais | Sens retenu |
|---|---|---|
| agent | agent | Logiciel dirigé par un modèle de langage, qui utilise des outils en boucle et choisit ses étapes (1) |
| agent borné | bounded agent | Agent qui choisit outils, ordre et paramètres dans une liste fermée, sous un plafond (17) |
| assistant | assistant, copilot | Logiciel qui produit une réponse et laisse l'humain agir (1) |
| boucle réflexive | evaluator-optimizer, critic loop | Patron à deux rôles : un agent produit, un autre évalue et fait reprendre (16) |
| cadriciel | framework | Bibliothèque qui fournit la boucle d'agent et le workflow (20) |
| chorégraphie | choreography | Coordination sans coordinateur, par réaction à des événements (19) |
| compensation | compensation | Action qui répare l'effet d'une action déjà exécutée (18) |
| exécution durable | durable execution | Garantie qu'un programme reprend après une panne, là où il s'était arrêté (18) |
| harnais | harness | Boucle d'agent déjà réglée, livrée avec ses outils et ses consignes (20) |
| humain dans la boucle | human-in-the-loop | L'humain peut intervenir à chaque cycle de décision; la position s'attache à une action (22) |
| humain sur la boucle | human-on-the-loop | L'humain intervient à la conception et surveille le fonctionnement (22) |
| idempotence | idempotency | Propriété d'une opération dont la répétition ne change pas l'effet (18) |
| orchestration | orchestration | Coordination d'agents, d'outils et de personnes vers un résultat (16) |
| rejeu | replay | Relecture d'un journal pour reprendre, tester ou auditer une exécution (18, 19) |
| Saga | saga | Suite de transactions locales, chacune assortie d'une compensation (18) |
| superviseur | supervisor | Agent central qui répartit le travail entre d'autres agents (16) |
| système multi-agents | multi-agent system | Système où plusieurs agents coopèrent à une même tâche (16, 21) |
| topologie | topology | Répartition qui dit qui décide de l'étape suivante et qui voit quoi (16) |
| transfert | handoff | Passage du contrôle d'un agent à un autre (16) |
| workflow agentique | agentic workflow | Chemin fixé par le concepteur, dont certaines étapes sont confiées à un modèle (1, 17) |

## A.2 Protocoles et découverte

| Français | Anglais | Sens retenu |
|---|---|---|
| artefact | artifact | Livrable produit par une tâche A2A (6) |
| carte d'agent | Agent Card | Document qui décrit un agent de l'extérieur : compétences, interfaces, sécurité (6) |
| client | client | Dans MCP, connecteur créé par l'hôte, lié à un seul serveur (5) |
| découverte | discovery | Trouver, décrire et authentifier une capacité avant de l'utiliser (8) |
| élicitation | elicitation | Demande d'information adressée à l'utilisateur par un serveur MCP (5) |
| espace de noms | namespace | Préfixe qui rattache un nom à son propriétaire vérifié (8) |
| extension | extension | Ajout facultatif à un protocole, désactivé par défaut (5) |
| hôte | host | Application d'IA qui crée les clients MCP et applique le consentement (5) |
| liaison | binding | Correspondance entre des opérations abstraites et un transport (6) |
| outil | tool | Fonction décrite par un nom, une description et un schéma, que le modèle peut invoquer (5) |
| passerelle | gateway | Intermédiaire placé sur le chemin de chaque appel, qui applique les politiques (24) |
| registre | registry | Catalogue de serveurs ou d'agents, avec leurs métadonnées (8) |
| sans état | stateless | Protocole où chaque requête porte tout ce qu'il faut pour la traiter (5) |
| serveur | server | Dans MCP, service qui expose des outils, des ressources et des prompts (5) |
| sous-registre | subregistry | Registre dérivé d'un registre amont, qui y ajoute curation et politiques (8, 27) |
| tâche | task | Unité de travail à état, suivie par un identifiant (5, 6) |

## A.3 Données, contexte et mémoire

| Français | Anglais | Sens retenu |
|---|---|---|
| cache de prompts | prompt caching | Préfixe de contexte déjà traité, gardé en cache et relu à prix réduit (13, 40, 44) |
| contrat de données | data contract | Entente lisible par machine entre producteur et consommateurs d'une donnée (15) |
| couche anticorruption | anti-corruption layer | Couche de traduction qui isole un modèle du système qu'il appelle (25) |
| couche sémantique | semantic layer | Définition partagée des métriques, compilée en requêtes (12) |
| découverte progressive | progressive discovery | Chargement des outils et ressources au fil des besoins (13) |
| fenêtre de contexte | context window | Texte que le modèle peut lire en un appel (13) |
| ingénierie du contexte | context engineering | Discipline qui règle la composition, le moment, le format et la durée de vie de l'information en contexte (13) |
| mémoire épisodique | episodic memory | Expérience des cycles antérieurs : historiques, trajectoires (14) |
| mémoire procédurale | procedural memory | Savoir-faire : poids du modèle et code de l'agent; la plus risquée à écrire (14) |
| mémoire sémantique | semantic memory | Savoir de l'agent sur le monde et sur lui-même (14) |
| ontologie | ontology | Modèle formel de concepts, de relations et de règles d'un domaine (12) |
| skill | skill (Agent Skills) | Dossier `SKILL.md` d'instructions, de scripts et de ressources, chargé par divulgation progressive (13) |
| système d'enregistrement | system of record | Système dont la donnée fait foi (25) |
| systèmes patrimoniaux | legacy systems | Systèmes anciens encore en service, dont l'ordinateur central (25) |

## A.4 Identité et autorisation

| Français | Anglais | Sens retenu |
|---|---|---|
| chaînage d'identité | identity and authorization chaining | Octroi JWT émis dans un domaine, que l'autre convertit en jeton d'accès (29) |
| charge de travail | workload | Logiciel en exécution, identifié sans mot de passe humain (29) |
| délégation | delegation | Fait d'agir au nom d'autrui, l'agent restant identifiable (29, 30) |
| élévation progressive | step-up authorization | Droit supplémentaire demandé quand une opération l'exige (30) |
| fournisseur d'identité | identity provider | Service qui authentifie et émet les assertions d'identité (29) |
| jeton | token | Preuve d'un droit d'accès, à portée et à durée limitées (29, 30) |
| justificatif | credential | Ce qui prouve une identité ou un droit : clé, certificat, jeton (29) |
| mandat | mandate | Justificatif signé qui atteste ce qu'un utilisateur a approuvé pour un achat (10) |
| moindre privilège | least privilege | Principe qui limite chaque droit à ce que la tâche exige (30) |
| parrain | sponsor | Représentant d'affaires qui répond d'un agent; obligatoire chez Entra (29) |
| point d'application | policy enforcement point | Composant qui intercepte la requête et applique la décision (30) |
| point de décision | policy decision point | Composant qui évalue la politique et rend la décision (30) |
| serveur d'autorisation | authorization server | Service qui émet les jetons selon la politique (30) |
| serveur de ressources | resource server | Service qui détient la ressource et vérifie le jeton (30) |
| usurpation | impersonation | Échange de jetons où l'agent se confond avec l'utilisateur et disparaît des journaux (29) |

## A.5 Sécurité et assurance

| Français | Anglais | Sens retenu |
|---|---|---|
| architecture Simplex | Simplex architecture | Sous-système simple et vérifié qui écarte les commandes risquées d'un composant complexe (46) |
| attestation | attestation | Preuve matérielle que la configuration matérielle et logicielle est celle attendue (46) |
| bac à sable | sandbox | Environnement isolé qui borne ce que du code peut atteindre (31) |
| empoisonnement de mémoire | memory & context poisoning | Écriture malveillante en mémoire, à effet différé (14, 31) |
| empoisonnement d'outil | tool poisoning | Instruction cachée dans la description d'un outil (31) |
| environnement d'exécution de confiance | trusted execution environment | Zone isolée par le matériel, souvent une machine virtuelle entière, qui protège la donnée en calcul des logiciels et opérateurs de l'exploitant, guère d'un accès physique (45, 46) |
| garde-fous | guardrails | Contrôles qui bornent les entrées, les sorties ou les actions d'un agent (23, 34) |
| injection indirecte | indirect prompt injection | Consigne déposée par un tiers dans un contenu que l'agent lit (31) |
| invariant | invariant | Règle du système qui doit tenir sur toute la trajectoire (32) |
| piste d'audit | audit trail | Journal complet, jamais échantillonné, de qui a fait quoi et sous quelle autorité (30, 33) |
| trifecta létale | lethal trifecta | Réunion de données privées, de contenu non fiable et d'un canal sortant (31) |
| zero trust | zero trust | Selon NIST SP 800-207, la confiance n'est jamais implicite et s'évalue en continu (32) |

## A.6 Architecture, exploitation et économie

| Français | Anglais | Sens retenu |
|---|---|---|
| banc d'essai | benchmark | Jeu de tâches à résultat vérifiable, répété pour comparer (33) |
| budget d'erreur | error budget | Marge d'échec admise, qui règle le rythme du changement et l'autonomie (34) |
| cache KV | KV cache | État de calcul d'un préfixe déjà traité, que le serveur d'inférence réutilise (44) |
| cascade | cascade | Petit modèle d'abord, escalade vers un grand après coup (44) |
| délai du premier jeton | time to first token | Temps entre l'envoi de la requête et le début de la réponse (44) |
| dérive | drift | Évolution du comportement, brusque après un changement ou graduelle sans déclencheur (34, 35) |
| développement piloté par la spécification | spec-driven development | Pratique qui tire de la spécification un plan, des tâches, puis le code (47) |
| distillation | distillation | Entraînement d'un petit modèle (élève) sur les sorties d'un grand (enseignant) pour une tâche étroite (47) |
| exécution en miroir | experiment (Scientist) | Ancien et nouveau chemins exécutés sur les mêmes entrées; seul l'ancien sert (47) |
| figuier étrangleur | strangler fig | Remplacement d'un système par parties, la parité de comportement servant de critère de sortie (25, 47) |
| infonuagique | cloud computing | Services informatiques fournis à la demande par un tiers (26) |
| juge automatique | automated judge | Modèle qui note la sortie d'un autre modèle (33) |
| maillage agentique | agentic AI mesh | Infrastructure qui rend les agents joignables et gouvernables (23) |
| mise à l'échelle | scaling | Passage d'un pilote à un usage étendu (4) |
| observabilité | observability | Capacité de reconstituer une exécution à partir de ses signaux (33) |
| passerelle d'inférence | inference gateway | Passerelle Gateway API dotée d'un routage et d'un équilibrage de charge conscients du modèle (44) |
| plan de contrôle | control plane | Couche qui décide : registre, identité, politique, budgets (23) |
| plan de données | data plane | Couche qui exécute les décisions sur le chemin de chaque appel (23, 44) |
| retour arrière | rollback | Retour à une version ou à un état antérieur (34) |
| routage de modèles | model routing | Choix, avant l'appel, d'un modèle à la mesure de chaque étape (40, 44) |
| test de mutation | mutation testing | Faute injectée dans le code pour vérifier qu'un test échoue (47) |
| test par propriétés | property-based testing | Invariant vérifié sur des entrées générées (47) |
| trace | trace | Arbre de spans d'une exécution, qui sert au diagnostic et peut être échantillonné (33) |
| verrouillage | lock-in | Dépendance qui rend coûteux le changement de fournisseur (20, 27) |

## A.7 Gouvernance et droit

| Français | Anglais | Sens retenu |
|---|---|---|
| clause de sortie | exit clause | Clause qui fixe ce qui se récupère en quittant un fournisseur (27) |
| connecteur | connector | Composant qui met en œuvre les échanges d'un espace de données chez chaque participant (37, 45) |
| espace de données | data space | Cadre de partage de données entre organisations, sous règles communes (37) |
| haut risque | high-risk | Catégorie de l'AI Act, définie par l'usage du système (35) |
| imputabilité | accountability | Obligation, pour une personne désignée, de répondre d'un agent (39) |
| inventaire | inventory | Liste tenue à jour des agents, de leurs droits et de leurs responsables (39) |
| prépublication | preprint | Article diffusé avant l'évaluation par les pairs (passim) |
| rapprochement à trois voies | three-way matching | Concordance du bon de commande, de la réception et de la facture avant paiement (45) |
| salle blanche de données | data clean room | Environnement où ne s'exécute qu'un code approuvé par tous, et d'où ne sort qu'un résultat convenu (45) |
| souveraineté numérique | digital sovereignty | Maîtrise du lieu, du droit applicable et des dépendances (37) |
| système décisionnel automatisé | automated decision system | Selon le projet de loi C-36, technologie qui appuie ou remplace le jugement de décideurs humains (38) |

## A.8 Sigles fréquents

| Sigle | Développé | Chapitre |
|---|---|---|
| A2A | Agent2Agent Protocol | 6 |
| AAIF | Agentic AI Foundation | 11 |
| ACP | Agent Communication Protocol, Agentic Commerce Protocol ou Agent Context Protocol | 6, 7, 10 |
| AP2 | Agent Payments Protocol | 10 |
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
