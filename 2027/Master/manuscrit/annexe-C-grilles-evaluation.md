# Annexe C — Grilles d'évaluation

> Les trois grilles reprennent des critères posés dans les chapitres. Propositions sans validation empirique, elles ordonnent des questions sans produire de score comparable d'une entreprise à l'autre.

Chaque grille demande une preuve, pas une déclaration. Une case se coche quand un essai, un journal ou un document daté la justifie.

## C.1 Interopérabilité

La grille reproduit celle du chapitre 3 (section 3.6).

| Niveau | 0 — Ad hoc | 1 — Déclaré | 2 — Vérifié | 3 — Gouverné |
|---|---|---|---|---|
| Technique | Connecteurs sur mesure | Protocole standard, version déclarée | Conformité testée | Passerelle, politique de versions et de dépréciation |
| Syntaxique | Texte libre | Schémas d'entrée publiés | Schémas d'entrée et de sortie validés des deux côtés | Schémas versionnés, compatibilité testée avant publication |
| Sémantique | Descriptions libres | Descriptions normalisées, glossaire | Termes rattachés à un vocabulaire de référence; jeux d'essai d'interprétation | Vocabulaire gouverné, dérive mesurée |
| Organisationnel | Aucun responsable désigné | Propriétaire et rôle pour chaque agent | Règles d'escalade et points d'approbation testés | Classes de décision, piste d'audit rejouable, revue périodique |
| Juridique et de confiance | Clés partagées | Identité propre à chaque agent, portées limitées | Délégation tracée, cartes signées et vérifiées, contrats couvrant les tiers | Preuve opposable, révocation centralisée, obligations cartographiées |

Trois règles d'usage :

- **On évalue une relation, pas une entreprise.** L'unité d'analyse est le couple agent-outil ou agent-agent.
- **Le score est celui du niveau le plus faible.** Une relation au stade 3 sur le plan technique et au stade 0 sur le plan organisationnel est au stade 0.
- **La cible dépend du risque.** Le stade 1 suffit à une lecture interne sans effet. Une action à effet externe, ou une relation qui traverse une frontière d'organisation, demande au moins le stade 2 sur toutes les lignes, organisation et droit compris. Le stade 3 se justifie pour les actions irréversibles (chapitre 18) et les secteurs réglementés.

Les protocoles amènent presque sans effort au stade 1 sur les deux premières lignes; le stade 2 y demande des tests de conformité et des schémas de sortie. Les trois autres lignes restent au stade 0 tant que l'entreprise n'a rien décidé.

## C.2 Orchestration

Cette grille s'applique à un processus confié en tout ou en partie à des agents. La dernière colonne donne le chapitre source.

| Critère | Question | Preuve attendue | Chapitre |
|---|---|---|---|
| Nécessité | Un agent unique outillé a-t-il été mesuré d'abord ? | Comparaison à l'agent unique, à budget égal, puis sous charge | 16, 21 |
| Décomposition | Les sous-tâches sont-elles indépendantes ? | Analyse de la tâche; une tâche séquentielle couplée reste à un seul agent | 16 |
| Région agentique | Quelle part du processus décide le modèle ? | Position déclarée : workflow, étapes agentiques, agent borné ou agent ouvert | 17 |
| Limites | Montants, seuils et autorisations sont-ils hors du modèle ? | Limites appliquées hors du prompt : outil, moteur, passerelle ou couche d'autorisation | 17, 22 |
| Délégation | Chaque délégation précise-t-elle objectif, format, limites et condition d'arrêt ? | Gabarit de délégation; absence de doublons dans les traces | 16, 21 |
| Effet unique | Les outils à effet sont-ils idempotents ? | Clé d'idempotence dérivée de l'étape durable; essai de rejeu | 18 |
| Compensation | Chaque action réversible a-t-elle sa compensation ? | Déclarée par le propriétaire de l'outil, idempotente, jamais générée par le modèle | 18 |
| Irréversible | Les actions sans retour suivent-elles un pivot explicite ? | Approbation journalisée, liée aux paramètres exacts | 18 |
| Reprise | L'exécution reprend-elle après une panne ? | Essai de reprise; sorties du modèle journalisées et relues au rejeu; reprise décidée hors de l'agent fautif | 18, 19 |
| Repli de modèle | Un modèle de secours est-il qualifié d'avance ? | Cadriciel multi-modèles; délai de bascule mesuré par exercice | 20, 44, 46 |
| Changement | Un changement de prompt, d'outil ou de modèle est-il traité comme un changement de code ? | Manifeste versionné; rejeu avant production; exécutions en cours finies sur l'ancienne version | 18, 34 |
| Vérification | Le contrôle porte-t-il sur l'objectif, et non sur le seul format ? | Tests déterministes là où ils existent; vérificateur indépendant | 21 |
| Supervision | La position de l'humain est-elle fixée par classe de décision ? | Classes selon gravité, réversibilité et faisabilité de la supervision | 22 |
| Journal | Peut-on reconstituer une exécution ? | Traces avec décisions du modèle, résultats d'outils et identifiant d'affaires; piste d'audit distincte, jamais échantillonnée | 19, 33 |
| Succès | Le résultat est-il vérifié sans se fier au compte rendu de l'agent ? | Contrôle de l'état final du système cible, sur plusieurs essais | 33, 34 |
| Coût | Le coût par résultat réussi est-il suivi ? | Plafonds par exécution et par période; coût par résultat réussi, comparé à une base de référence | 40 |

Trois refus découlent de la grille. Sans mesure contre l'agent unique, pas de système multi-agents. Sans clé d'idempotence, pas d'outil à effet, sauf action irréversible livrée au plus une fois après le pivot. Sans succès vérifié, pas d'élargissement de l'autonomie.

## C.3 Plateforme

Cette grille sert à lire une offre de plateforme d'agents et à préparer le contrat. Les questions et l'échelle viennent des chapitres 26 et 27.

### Six questions sur l'interopérabilité annoncée

| Question | Ce qu'il faut obtenir |
|---|---|
| Dans quel sens ? | Entrant et sortant : la plateforme appelle des agents externes et se laisse appeler |
| À quel statut ? | Disponibilité générale; une préversion ou une feuille de route n'engagent pas l'éditeur |
| Quelle version ? | Révision du protocole réellement mise en œuvre, et délai de mise à niveau |
| À quelle profondeur ? | Niveau atteint pour un agent tiers, sur l'échelle ci-dessous |
| Avec quelle identité ? | Fournisseur d'identité de l'entreprise accepté pour les agents, non celui de la plateforme |
| À quelles conditions ? | Licences, prérequis et clauses qui restreignent l'ouverture technique |

### Échelle de traitement d'un agent tiers

| Niveau | Ce que fait la plateforme |
|---|---|
| 1 — Inventorié | L'agent tiers figure au registre |
| 2 — Observé | Ses traces et ses appels d'outils remontent au plan de contrôle |
| 3 — Gouverné | Une identité, des politiques d'accès et un pouvoir de blocage s'appliquent à lui |
| 4 — De plein droit | Il reçoit les mêmes rapports, garde-fous et capacités qu'un agent natif |

Échelle proposée par le chapitre 26, non normative. Presque toutes les plateformes examinées atteignent le niveau 1, parfois le niveau 3; aucune page lue ne documente le niveau 4. Cible par défaut : niveau 3, écart avec l'agent natif noté; le niveau 1 suffit à un recensement.

### Critères de plan de contrôle

| Critère | Question | Preuve attendue | Chapitre |
|---|---|---|---|
| Chemin obligé | Tout appel passe-t-il par un point d'application ? | Politique réseau qui ferme les autres chemins, serveurs locaux et justificatifs directs compris | 23, 24 |
| Registre | Le registre fait-il autorité, avec un propriétaire par entrée ? | Cycle de vie; inscription avant tout routage; accès programmatique sans supplément | 8, 23, 27 |
| Contrôles par appel | Identité, autorisation par outil, approbation, quota, inspection des contenus ? | Journal de chaque décision; échec fermé | 24 |
| Jeton en aval | La passerelle se présente-t-elle avec un justificatif distinct ? | Échange de jeton ou justificatif propre à la passerelle; aucun relais du jeton reçu | 24, 30 |
| Portabilité | Quels actifs s'exportent, sous quel format et à quelle fréquence ? | Liste : définitions d'agents, prompts, compétences, configuration des outils, mémoire en texte, traces, jeux d'évaluation, journaux d'audit | 27 |
| Traces | Les traces sortent-elles dans un schéma que l'entreprise maîtrise ? | Export OpenTelemetry au minimum, normalisé au collecteur vers un schéma interne | 33 |
| Changement de modèle | L'éditeur prévient-il avant de remplacer un modèle ? | Clause de préavis; rejeu du banc d'essai interne | 27, 34 |
| Sortie | La sortie a-t-elle été répétée ? | Essai de sortie réussi pendant la durée du contrat | 27 |

### Essai minimal avant engagement

Faute d'essais indépendants, l'entreprise vérifie elle-même au moins trois scénarios (chapitre 26) :

1. un agent externe appelle la plateforme;
2. la plateforme appelle un agent externe;
3. un agent tiers est inscrit, restreint, puis révoqué depuis le plan de contrôle.

Le quatrième, l'essai de sortie, s'inscrit au contrat et se répète pendant sa durée (chapitre 27) : une clause de sortie se prouve par cet essai, pas par sa rédaction.
