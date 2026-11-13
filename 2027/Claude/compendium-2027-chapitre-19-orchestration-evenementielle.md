# Chapitre 19 — Orchestration événementielle

*Question directrice : quand des agents doivent-ils réagir à des événements au lieu d'être appelés ?*

> **Version 2 — 11 novembre 2026.** État de référence : Apache Flink Agents 0.4, spécification MCP `2026-07-28`, extension Tasks et feuille de route du 22 août 2026, spécification A2A 1.0. Les numéros entre crochets renvoient aux sources en fin de chapitre : [1] à [13] sont des pages primaires; [14] et [15] sont des billets de fournisseurs, signalés comme tels. Les renvois « chapitre N » pointent vers les autres chapitres du compendium. Chapitre audité et révisé le 12 novembre 2026.

La plupart des agents sont appelés : une personne pose une question, un processus invoque une étape, un superviseur délègue. Une bonne part du travail d'une entreprise ne commence pourtant par aucune demande. Une commande est annulée, un capteur dépasse un seuil, un paiement est refusé : le fait se produit, et quelque chose doit s'ensuivre.

L'événement est le bon déclencheur quand le fait existe sans demandeur, quand le travail dure plus longtemps qu'une connexion, ou quand plusieurs consommateurs doivent réagir au même fait. Le journal d'événements vaut ensuite surtout comme substrat : il apporte durabilité, reprise et piste d'audit. La décision reste mieux tenue par un coordinateur explicite : les systèmes documentés orchestrent sur un transport événementiel.

---

## 19.1 Requête-réponse ou événements

Un appel a un destinataire et un demandeur qui attend. Un événement est l'enregistrement d'un fait; il ne nomme pas de destinataire, et celui qui le publie n'attend rien (chapitre 2). Selon la documentation de Kafka, producteurs et consommateurs sont ainsi entièrement découplés [1].

Ce découplage répond à trois situations.

**Le fait précède la demande.** Les auteurs de la proposition Flink Agents décrivent les processus d'entreprise comme asynchrones, à état et continus, et l'agent comme un microservice qui consomme des événements d'affaires au lieu de répondre à des prompts isolés [3].

**Le travail dépasse la connexion.** Un superviseur qui attend de façon synchrone la fin d'une tâche de vingt minutes immobilise des ressources et perd tout si sa connexion tombe (chapitre 18).

**Plusieurs réactions au même fait.** Un événement publié une fois peut être lu par autant de consommateurs qu'il le faut, sans que le producteur les connaisse.

L'équipe RocketMQ d'Alibaba Cloud soutient dans le même sens que les goulots des systèmes multi-agents en production sont opérationnels et non liés à la qualité du modèle : absorption des rafales, isolation des sessions, reprise après panne, auditabilité [15].

| Critère | Requête-réponse | Événements |
|---|---|---|
| Déclencheur | Une demande adressée | Un fait publié |
| Couplage | L'appelant connaît l'appelé | Le producteur ignore les consommateurs |
| Pointe de charge | Subie par l'appelé | Absorbée par le journal |
| Résultat | Dans la réponse | Dans un autre événement, à corréler |
| Vue d'ensemble | Dans le code de l'appelant | À reconstituer à partir du journal |

Les deux dernières lignes sont le prix à payer : il faut corréler, et plus personne ne détient le déroulement complet (section 19.7).

---

## 19.2 Kafka comme dorsale, Flink comme moteur

### Ce que Kafka garantit

Deux propriétés du journal importent pour des agents [1].

- Les événements ne sont pas supprimés après lecture : ils se relisent à volonté pendant une durée de rétention fixée par sujet (*topic*).
- Les événements de même clé vont dans la même partition, et tout consommateur d'une partition les lit dans le même ordre. Avec l'identifiant de dossier ou de session comme clé, on obtient un ordre par dossier, pas un ordre global.

La relecture est la propriété décisive : elle sert à la reprise, aux tests et à l'audit (section 19.4).

### Flink Agents

Un journal ne décide de rien; il faut un moteur qui consomme, garde un état et produit. FLIP-531, proposition de juin 2025 cosignée par Sean Falconer, a lancé Flink Agents comme sous-projet d'Apache Flink [3]. L'argument : Flink apporte déjà la faible latence, la tolérance aux pannes, la gestion d'état et l'intégration à Kafka; il lui manquait les abstractions d'agent. La proposition prévoit l'appel de modèles, l'invocation d'outils (dont MCP), le rejeu de flux historiques et une communication asynchrone entre agents par un stockage de flux tel que Kafka. Elle ne mentionne pas A2A.

La page de téléchargement d'Apache Flink donne la version 0.4 comme la plus récente, compatible avec Flink 1.20 à 2.3 [2]. La documentation présente le projet comme un « Agent OS » de flux : l'agent y devient un opérateur du flux de données, des *Actions* traitent des *Events*, et des *Resources* nommées (modèles, outils, prompts, serveurs MCP) sont réutilisables, avec des API Java, Python et YAML [4].

**Le statut.** Les versions 0.x sont des préversions : API et configuration sont expérimentales et peuvent changer de façon incompatible avant la 1.0 [4].

**La portée des garanties.** La page sur la cohérence distingue deux niveaux [5].

| Configuration | Ce qui est garanti | Ce qui ne l'est pas |
|---|---|---|
| Points de contrôle seuls | Chaque entrée affecte une seule fois l'état et la sortie du job | Actions et appels externes peuvent se répéter; un modèle peut répondre autrement |
| Points de contrôle et Action State Store (Kafka ou Fluss) | Les Actions terminées sont réutilisées, non réexécutées; les appels durables enregistrés sont rejoués | L'effet externe : le magasin ne peut pas valider l'opération et son résultat en une seule transaction |

La documentation en conclut qu'il faut un service idempotent ou un mécanisme de réconciliation [5]. Le « exactement une fois » d'un moteur de flux porte sur son état et ses sorties, pas sur le courriel envoyé par un outil. L'idempotence et la compensation du chapitre 18 restent nécessaires.

---

## 19.3 Le patron d'orchestrateur sur flux

Le patron examiné ici vient d'un article de Sean Falconer, alors chez Confluent, publié par SD Times en février 2025 [14]. C'est un texte de fournisseur accompagné d'une démonstration, pas un retour de production.

Les agents publient leurs messages dans un sujet Kafka. Un job Flink lit chaque message et le soumet à un modèle de langage, appelé en SQL. Le modèle choisit l'agent destinataire à partir de définitions structurées : nom, description, entrée, sortie. Flink transmet le message à cet agent, qui écrit son résultat dans le sujet, et la boucle reprend jusqu'à la fin du travail.

Les agents n'ont aucune dépendance explicite entre eux, et aucune logique de routage n'est codée en dur. L'auteur en attend des décisions en temps réel sans workflow figé et une structure des messages contrôlée par la gouvernance des flux.

**C'est une orchestration.** Malgré le vocabulaire événementiel, un composant central décide de tout. Le patron est le superviseur du chapitre 16, transposé sur un flux : le journal remplace l'appel direct, pas le coordinateur.

**Le routage coûte une inférence par message.** Quand la suite des étapes est connue d'avance, une règle déterministe fait le même travail sans ce coût ni cette variabilité (chapitre 17). Les routeurs comparés au chapitre 44 changent d'ailleurs souvent de choix devant une simple reformulation.

**L'auteur nomme lui-même les limites.** Des agents peuvent engendrer un nombre illimité de tâches, ce qui exige une gestion des ressources; il faut suivre l'avancement, détecter les échecs et replanifier; certains processus demandent un ordre strict [14]. Le patron reporte ces points sur l'exploitation.

---

## 19.4 Sessions rejouables et event sourcing

### La session comme flux

RocketMQ-A2A est le seul système examiné ici présenté comme en production. L'article a été accepté dans le volet industriel de FSE 2026; ce chapitre s'appuie sur le billet de ses auteurs, daté du 16 septembre 2026 [15].

L'idée centrale : modéliser chaque session de collaboration comme un flux d'événements persistant et rejouable, et séparer l'envoi des tâches du retour des résultats.

- Un sujet ordinaire distribue les tâches du superviseur vers des agents exécutants sans état. Les rafales s'accumulent dans la file, pas dans la mémoire des exécutants.
- Un canal léger propre à la session, le LiteTopic, ramène résultats et changements d'état vers le superviseur, dans l'ordre et de façon durable. Ces canaux, créés et détruits à la volée, sont récupérés à l'expiration d'un délai.

Le superviseur ne bloque plus sur la tâche longue d'un exécutant. S'il tombe, le flux de la session est relu depuis le point d'interruption : les tâches reprennent au lieu de recommencer, et le journal structuré des interactions sert de preuve pour l'audit.

Selon le billet, le dispositif est versé au projet Apache RocketMQ et sert notamment la plateforme Model Studio d'Alibaba Cloud.

### L'event sourcing appliqué aux agents

ESAA pousse la même logique à l'échelle d'un projet logiciel [12]. L'agent n'écrit ni dans le projet ni dans le journal : il émet des intentions structurées en JSON. Un orchestrateur déterministe les valide, les consigne dans un journal en ajout seul, applique les changements et en dérive une vue matérialisée, vérifiable par rejeu et empreinte. C'est une prépublication à auteur unique, appuyée sur deux études de cas de petite taille : une illustration, pas une preuve de passage à l'échelle.

Le principe : séparer ce que l'agent *propose* de ce qui est *enregistré comme fait*.

### Rejouer n'est pas réexécuter

Le mot « rejeu » recouvre deux opérations distinctes.

**Relire le journal** reconstitue l'état à partir de faits enregistrés. L'opération est déterministe : c'est celle de RocketMQ-A2A à la reprise, d'ESAA à la vérification, et de l'Action State Store de Flink Agents, qui rejoue les résultats sauvegardés sans rappeler la fonction [5].

**Réexécuter sur des entrées historiques** rappelle le modèle. FLIP-531 en fait un usage délibéré : tests de régression, débogage, analyse de la dérive du modèle, sans effets réels [3]. Le résultat peut différer; c'est justement ce qu'on cherche à mesurer.

Un journal qui ne garde que les entrées permet de réexécuter, pas de reconstituer. Pour reprendre après panne et pour auditer, il faut journaliser aussi les décisions du modèle et les résultats des outils. La documentation de Flink Agents ajoute deux conditions : le rejeu doit préserver l'ordre des entrées par clé, et les enregistrements du magasin doivent être conservés aussi longtemps que les points de reprise qui en dépendent [5].

---

## 19.5 Contrepoints : état interrogeable, capture directe des changements

### L'agent a besoin de l'état, pas du flux

Un agent qui répond à une question n'a que faire de la suite des événements; il lui faut l'état qu'ils décrivent. Le Real-Time Context Engine de Confluent, annoncé en disponibilité générale le 18 août 2026 [16], sert par MCP l'état courant de tables construites sur des sujets Kafka [11]. FLIP-531 revendique la même capacité à l'intérieur de Flink : conserver et interroger le contexte sans magasin externe [3].

Le flux reste en amont, comme mécanisme de fraîcheur, et l'agent interroge par un appel d'outil ordinaire (chapitre 15). Événementiel et requête-réponse occupent deux étages.

### Capter les changements sans dorsale

Un système patrimonial ne publie pas d'événements, mais sa base de données tient un journal de ses modifications. La capture des changements en fait une source d'événements sans toucher à l'application (chapitre 25). Elle n'exige pas de dorsale : la documentation de Debezium décrit un moteur embarqué qui livre les changements directement à l'application, pour celles qui ne veulent pas dépendre d'une grappe Kafka [10].

La documentation en énonce les contreparties : positions de lecture gardées par défaut dans un fichier local, doublons à tolérer après une panne; pour un « exactement une fois » plus rigoureux, elle renvoie à la plateforme complète [10].

Un agent déclenché quelques fois par jour par un changement dans une table n'a pas besoin d'un journal distribué et d'un moteur de flux; un déclencheur direct et un traitement idempotent suffisent.

---

## 19.6 Les événements dans les protocoles : Tasks MCP, notifications A2A

MCP et A2A sont des protocoles de requête-réponse dotés de moyens de dire « ce n'est pas fini ». Aucun n'est un bus de messages.

### MCP

La feuille de route d'août 2026 recense trois mécanismes : l'extension Tasks (chapitre 5), le flux `subscriptions/listen` et les notifications de progression. Elle reconnaît le risque d'avoir trois réponses à la même question, sans cycle de vie, modèle d'annulation ni surface d'erreur communs [6].

`subscriptions/listen` ouvre un flux du serveur vers le client, filtré par types de notifications. La page de la spécification en énumère quatre : changement de la liste d'outils, de prompts ou de ressources, et mise à jour de ressources désignées par leur URI [7]. La notification de mise à jour ne porte que l'URI : c'est un signal, après lequel le client relit la ressource. L'extension Tasks ajoute, par ce même flux, `notifications/tasks`, qui porte l'état complet de la tâche; sa page en conclut qu'un client peut alors s'y fier au lieu d'interroger [13]. Après une rupture, le client peut rouvrir un flux; sur stdio, il le doit, car le serveur ne garde aucun état d'abonnement. La page ne prévoit aucun rattrapage des notifications manquées.

Les événements poussés par le serveur, y compris par webhooks, sont un livrable de la période en cours [6]. Le groupe de travail qui en a la charge, créé le 24 mars 2026 sous le nom Triggers and Events et rebaptisé Tasks and Events le 16 octobre, a pour mission un mécanisme de rappel normalisé, assorti de garanties d'ordre valables sur tous les transports [8]. Sa charte exclut expressément une infrastructure générale de publication-abonnement, et sa proposition sur les événements y figure encore au stade d'idéation, avec une cible de fin avril dépassée. MCP ne normalise donc encore ni déclencheur ni webhook.

### A2A

A2A offre deux voies, décrites au chapitre 6. Le flux livre les événements d'une tâche dans l'ordre où ils ont été produits, et un client déconnecté peut se réabonner : le premier événement reçu est alors l'état courant de la tâche [9]. La spécification prévient toutefois qu'un client qui se reconnecte peut ne pas avoir reçu toutes les mises à jour, et que les messages ne doivent pas être tenus pour un mécanisme de livraison fiable d'information critique.

Les notifications poussées s'adressent aux clients déconnectés. L'agent doit tenter la livraison au moins une fois à chaque webhook configuré; les nouvelles tentatives sont permises à la section 4.3.3, recommandées à la section 13.2. Le client doit accuser réception par un code 2xx et devrait traiter les notifications de façon idempotente, des doublons étant possibles [9]. L'agent devrait aussi rejeter les URL de webhook privées, de bouclage ou locales au lien, contre la falsification de requêtes côté serveur (SSRF, chapitre 6) [9].

### Une même règle : notifier, puis relire

| Mécanisme | Ordre | Livraison | Rattrapage après rupture |
|---|---|---|---|
| MCP `subscriptions/listen`, dont `notifications/tasks` [7] [13] | Non précisé | Tant que le flux est ouvert | Aucun; nouvel abonnement, puis `tasks/get` |
| A2A, flux [9] | Ordre de production | Tant que le flux est ouvert | État courant au réabonnement |
| A2A, notification poussée [9] | Non précisé | Au moins une tentative | Lecture de la tâche |
| Journal Kafka [1] | Par partition | Durable | Relecture du journal |

Dans les deux protocoles, l'état de la tâche fait foi : une notification, même porteuse de l'état complet, peut manquer ou arriver en double, et aucun mécanisme ne rejoue celles qui ont été perdues. Un client traite donc toute notification comme une invitation à relire, relit l'état à chaque reconnexion et interroge périodiquement en l'absence de signal. Une organisation qui a besoin d'une livraison ordonnée, durable et rejouable entre agents doit placer un journal derrière le protocole. C'est ce que fait RocketMQ-A2A, qui donne aux échanges asynchrones de style A2A un flux persistant par session [15].

---

## 19.7 Chorégraphie ou orchestration

En orchestration, un coordinateur détient le plan et déclenche les étapes. En chorégraphie, chaque participant réagit aux événements des autres, et le plan n'est écrit nulle part (chapitre 18).

La chorégraphie découple : ajouter un agent, c'est ajouter un abonné. Avec des agents, elle cumule deux difficultés. Le déroulement n'étant détenu par personne, il faut le reconstituer après coup. Et chaque réaction est une décision non déterministe : un agent qui réagit peut publier des événements qui en font réagir d'autres, sans borne. C'est l'« explosion de tâches » que signale l'article sur l'orchestrateur Flink [14]. Les défauts de spécification et de désalignement du chapitre 21 y trouvent un terrain favorable.

Les trois systèmes lus pour ce chapitre font le même choix : un orchestrateur Flink central [14], un superviseur avec des exécutants sans état [15], un orchestrateur déterministe qui valide les intentions [12]. Tous transportent par événements; aucun ne laisse les agents s'enchaîner librement. L'échantillon est mince, mais sa cohérence indique une pratique : **orchestrer la décision, chorégraphier la diffusion**.

La chorégraphie garde sa place quand trois conditions sont réunies : les réactions sont indépendantes les unes des autres; aucune n'a à être annulée si une autre échoue; aucun ordre n'est requis entre elles. Dès qu'une transaction d'affaires traverse plusieurs agents, il faut un coordinateur, donc une Saga orchestrée (chapitre 18).

Trois garde-fous valent dans tous les cas. Chaque événement porte l'identifiant d'affaires du dossier ou de la demande, distinct de l'`id` d'événement qu'exige CloudEvents (chapitre 2), pour reconstituer une trajectoire (chapitre 33). Au-delà d'un budget par dossier, en événements ou en jetons, le traitement passe à un humain (chapitres 22 et 40). Enfin, le contenu d'un événement est une entrée non fiable : quiconque écrit dans un journal ou une file peut viser l'agent qui le lit, comme le démontre l'injection par les journaux. L'agent déclenché propose, et son action se choisit dans un catalogue borné (chapitres 31 et 47).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Mode de déclenchement | Appel direct | Fait sans demandeur, travail plus long qu'une connexion, plusieurs consommateurs |
| Dorsale d'événements | Aucune tant qu'un déclencheur direct suffit | Relecture, pointes de charge ou consommateurs multiples |
| Moteur d'agents sur flux | Flink Agents à l'essai seulement, vu son statut de préversion | Production si Flink est déjà exploité et qu'une adaptation des API est prévue |
| Contenu du journal | Entrées, décisions du modèle et résultats d'outils | Entrées seules si le seul besoin est le test par réexécution |
| Effets externes | Outils idempotents ou réconciliation | — |
| Coordination | Orchestrateur explicite sur transport événementiel | Chorégraphie pour des réactions indépendantes, sans ordre ni compensation |
| Suivi d'une tâche MCP ou A2A | Notification comme signal, puis relecture de l'état | Interrogation périodique si le client ne peut recevoir d'appel entrant |
| Contexte de l'agent | État interrogeable par un outil | Consommation directe du flux pour un agent qui réagit à chaque événement |
| Action déclenchée par un événement | Proposition, puis procédure d'un catalogue borné | — |

---

## Points à retenir

- L'événement s'impose dans trois cas : fait sans demandeur, travail plus long qu'une connexion, plusieurs consommateurs. Ailleurs, l'appel direct reste plus simple.
- La relecture du journal est la propriété qui compte : elle sert à la reprise, aux tests et à l'audit.
- Flink Agents existe, en version 0.4, mais en préversion. Son « exactement une fois » couvre l'état et les sorties du job, pas les effets externes des outils.
- Rejouer n'est pas réexécuter. Pour reprendre et auditer, le journal doit contenir les décisions du modèle et les résultats des outils, pas seulement les entrées.
- Les systèmes documentés gardent un coordinateur et transportent par événements. La chorégraphie convient aux réactions indépendantes, sans ordre ni compensation.
- MCP et A2A notifient sans rattrapage garanti : l'état de la tâche fait foi et se relit à chaque reconnexion. Les événements poussés et les webhooks de MCP sont encore à l'étude.
- Un événement est une entrée non fiable : l'agent qu'il déclenche propose, et son action se choisit dans un catalogue borné.
- Un agent a le plus souvent besoin de l'état que décrit le flux, pas du flux. À petit volume, une capture directe des changements et un traitement idempotent remplacent la dorsale.

---

## Sources

Pages primaires lues le 11 novembre 2026; [2], [5] à [9] et [13] lues ou relues le 12 novembre :

1. [Apache Kafka — Introduction](https://kafka.apache.org/intro)
2. [Apache Flink — téléchargements (Flink Agents 0.4)](https://flink.apache.org/downloads/)
3. [FLIP-531 — Flink Agents](https://cwiki.apache.org/confluence/display/FLINK/FLIP-531:+Initiate+Flink+Agents+as+a+new+Sub-Project)
4. [Flink Agents — vue d'ensemble](https://nightlies.apache.org/flink/flink-agents-docs-latest/docs/get-started/overview/)
5. [Flink Agents — cohérence](https://nightlies.apache.org/flink/flink-agents-docs-latest/docs/operations/consistency/)
6. [MCP — feuille de route du 22 août 2026](https://modelcontextprotocol.io/development/roadmap.md)
7. [MCP — Subscriptions, spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)
8. [MCP — charte du groupe de travail Tasks and Events](https://modelcontextprotocol.io/community/working-groups/tasks-events.md)
9. [Spécification A2A 1.0](https://a2a-protocol.org/latest/specification/) (sections 3, 4.3 et 13.2)
10. [Debezium 3.7 — Debezium Engine](https://debezium.io/documentation/reference/stable/development/engine.html)
11. [Confluent — Real-Time Context Engine, vue d'ensemble](https://docs.confluent.io/cloud/current/ai/real-time-context-engine/overview.html) (début de page)
12. [ESAA: Event Sourcing for Autonomous Agents (arXiv 2602.23193)](https://arxiv.org/abs/2602.23193) (résumé)
13. [MCP — extension Tasks](https://modelcontextprotocol.io/extensions/tasks/overview.md)

Billets de fournisseurs, lus; [15] relu le 12 novembre :

14. [SD Times — orchestrateur multi-agents Flink/Kafka](https://sdtimes.com/how-to-build-a-multi-agent-orchestrator-using-flink-and-kafka/) (S. Falconer, Confluent, février 2025)
15. [Alibaba Cloud — RocketMQ-A2A accepté à ACM FSE 2026](https://www.alibabacloud.com/blog/rocketmq-a2a-paper-accepted-at-acm-fse-defining-a-reliable-collaboration-paradigm-for-ai-agents_603558) (16 septembre 2026); article d'origine non lu, DOI 10.1145/3803437.3805231
16. [Confluent — New in Confluent Intelligence and AI Tools](https://confluent.io/blog/2026-q3-confluent-intelligence-ai-update) (18 août 2026)

## Limites de ce chapitre

- **EDAgent (ICDCS 2026)**, nommé parmi les appuis, n'a pas été retrouvé et n'est pas utilisé.
- **RocketMQ-A2A** est décrit d'après le billet de ses auteurs, non d'après l'article. Le statut de production reste une affirmation de l'éditeur; les chiffres du billet ont été écartés.
- **L'orchestrateur Flink/Kafka** repose sur un billet de février 2025, antérieur à Flink Agents. Aucun retour de production indépendant n'a été trouvé pour ce patron ni pour Flink Agents, dont la version 0.4 n'est pas datée sur la page lue.
- **ESAA** n'est connu que par son résumé; **Confluent**, par le début d'une page et un billet [16].
- **A2A** : la section 13.2, lue pendant l'audit, lève la réserve sur la sécurité des notifications poussées; elle recommande (SHOULD) les nouvelles tentatives que la section 4.3.3 se borne à permettre (MAY). **MCP** : la page de l'extension Tasks [13] lève l'écart avec le chapitre 5, ses notifications passant par `subscriptions/listen`. Aucune page lue ne précise l'ordre de ces notifications; la relecture à la reconnexion est une recommandation de ce chapitre.
- **CloudEvents** est repris du chapitre 2, sans lecture de sa spécification.
- Les définitions de l'orchestration, de la chorégraphie et de l'event sourcing, l'exemple du superviseur en attente et la capture des changements appliquée au patrimoine relèvent de la connaissance générale. Les conditions d'emploi de la chorégraphie, les garde-fous de la section 19.7 et la grille de décision sont des recommandations de ce chapitre, non des résultats tirés d'une source.
- Le « maillage d'événements » de la carte et les autres courtiers ne sont pas traités, faute de source lue; DDS, la publication-abonnement de ROS 2, l'est au chapitre 46.
