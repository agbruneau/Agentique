# Chapitre 25 — Intégration au patrimoine

*Question directrice : comment brancher des agents sur des systèmes qui doivent rester exacts ?*

> **Version 2 — 11 novembre 2026.** État de référence : spécification MCP `2026-07-28`, documentation IBM de CICS TS 6.3, page d'architecture SAP mise à jour le 26 octobre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre. Les sources [1], [2], [7] et [8] sont des textes de praticien, de cabinet-conseil ou d'éditeur : ce qu'elles avancent n'est pas une mesure indépendante. Les renvois « chapitre N » pointent vers la table des matières du compendium. Chapitre audité et révisé le 12 novembre 2026.

Un moteur de tarification, un grand livre ou un système de paie ont une propriété qu'un modèle de langage n'a pas : à entrées identiques, résultat identique, et ce résultat fait foi. Ces systèmes patrimoniaux portent des décennies de règles d'affaires, souvent sur ordinateur central (mainframe), et l'entreprise en répond devant ses clients, ses vérificateurs et ses régulateurs. Un agent est probabiliste : il interprète, il choisit, il se trompe parfois.

La question n'est donc pas de rendre le patrimoine agentique, mais de décider où passe la frontière. La thèse de ce chapitre est que l'agent reste hors du calcul et de l'écriture qui font foi, et qu'il y accède par une couche d'encapsulation qui traduit, valide et limite.

---

## 25.1 Préserver le cœur déterministe

### Un principe et trois zones

La formulation la plus nette vient d'un article de praticien paru dans *Architecture & Governance* le 31 juillet 2026 [1]. Alok Mehta y décrit une application qui aide un retraité à choisir entre un montant forfaitaire et une rente. L'ancienne solution recueillait 33 saisies par formulaire, les versait dans un tableur, puis les transmettait à un analyseur actuariel patrimonial. La refonte a remplacé tout ce qui entourait l'analyseur, sans toucher à celui-ci; des tests de parité ont confirmé que le calcul était inchangé.

L'auteur en tire une règle : préserver le cœur de confiance et moderniser autour de lui l'expérience, les contrôles et l'intégration. L'article parle de *trusted core*, d'*invariant core* et, pour la troisième des trois zones de l'architecture qui en découle, de *deterministic business core*.

| Zone | Contenu | Nature |
|---|---|---|
| Expérience | Web, mobile, voix, dépôt de documents | Agentique, remplaçable |
| Contrôle | Orchestration, validation, politiques, piste d'audit | Déterministe, nouvelle |
| Cœur métier déterministe | Moteur de calcul existant | Déterministe, figé |

### Sept règles de conception

L'article énonce sept règles [1] :

1. **Figer le cœur invariant** : formules, règles, API et contrats de données qui ne doivent pas changer.
2. **Des contrats explicites** : schémas structurés entre agents et systèmes, aucun texte libre à la frontière d'intégration.
3. **Des tests de parité** sur un jeu de cas de référence.
4. **L'IA hors de la frontière de décision** : elle recueille, organise et explique; les calculs réglementés et les approbations restent déterministes.
5. **Les exceptions vont à une personne** : ambiguïté, faible confiance, conflit de politique.
6. **L'observabilité fait partie de l'architecture** : actions, entrées, sorties, latences, échecs, interventions humaines.
7. **Sécuriser les coutures**, même quand le point d'accès patrimonial ne peut pas être redessiné.

La quatrième règle structure les autres : l'agent travaille en amont du cœur (réunir et valider les entrées) et en aval (expliquer le résultat), jamais à la place du calcul. C'est le placement étudié au chapitre 17, appliqué au patrimoine.

### Portée du principe

L'auteur précise lui-même qu'envelopper plutôt que réécrire n'est pas une règle universelle [1]. Préserver le cœur est la voie la moins risquée quand sa logique reste exacte, maintenable et distinctive. Le remplacement peut être préférable quand la plateforme sous-jacente est devenue techniquement obsolète ou incapable de suivre l'évolution des exigences réglementaires ou d'affaires. Fondé sur un seul cas et sans mesure, l'article vaut comme patron raisonné, pas comme preuve.

---

## 25.2 Les systèmes d'enregistrement comme source d'autorité

Un système d'enregistrement est celui dont la donnée fait foi pour un objet d'affaires : le solde, la police, le dossier d'employé. Trois règles préservent cette autorité. Elles relèvent du raisonnement d'architecture; les sources lues les illustrent sans les démontrer.

**L'agent cite le système, il ne s'en souvient pas.** Une valeur gardée en mémoire d'agent (chapitre 14), dans un cache de lecture (chapitre 5) ou dans une copie préparée pour les agents (chapitre 15) n'a pas d'autorité. Elle sert à orienter le raisonnement. Toute décision qui engage l'entreprise relit la donnée à la source, ou porte la date de sa copie.

**L'écriture passe par l'interface d'affaires du système.** Le patron décrit en 25.1 envoie au moteur patrimonial la même requête structurée que le processus existant [1]. Le système applique alors ses propres validations, comme il le fait pour tout autre appelant. Écrire directement dans ses tables contourne ces validations et retire au système ce qui fonde son autorité.

**C'est le système qui autorise.** Le serveur MCP de CICS reprend la configuration de sécurité de l'interface de gestion existante, rôle compris [5]. SAP écrit que le client demeure responsable des permissions du système dorsal, du choix des outils et des politiques configurées, même derrière sa passerelle [10]. IBM présente pour z/OS Connect une autorisation au niveau de l'opération [7]. Dans les trois cas, la couche agentique n'ajoute pas un régime d'accès parallèle : elle se soumet à celui qui existe. La difficulté est d'acheminer jusqu'au système l'identité au nom de laquelle l'agent agit, puisque MCP interdit de relayer en aval le jeton reçu (chapitre 5). L'échange de jetons et la délégation sont traités aux chapitres 29 et 30. À défaut, le serveur appelle le système sous un compte de service, souvent le justificatif le plus large de la chaîne (chapitre 30).

Le « système d'enregistrement d'agents » de certains éditeurs est autre chose : un registre qui fait foi sur les agents, pas sur les données d'affaires (chapitre 26).

---

## 25.3 Mainframe : des agents sous contrôle pour la modernisation

Deux usages posent des problèmes distincts : interroger le système en exploitation, et en moderniser le code.

### En exploitation : la lecture d'abord

IBM livre avec CICS TS 6.3 un serveur MCP propre au moniteur transactionnel [5]. Il s'exécute dans le serveur JVM de l'interface de gestion, parle Streamable HTTP et regroupe ses outils en *toolboxes*, chacune exposée comme un point d'accès MCP. Le travail MCP s'exécute sous une transaction fournie par CICS, `CWMC`. Le serveur est **activé par défaut**.

IBM fournit trois agents spécialisés (topologie, appel d'outils, diagnostic) et un agent de routage; les deux derniers spécialisés interrogent le serveur MCP. Ils s'exécutent sur watsonx Assistant for Z. La documentation est explicite : ils sont en lecture seule et ne peuvent rien modifier sur le système [6]. Elle prévient aussi que les réponses peuvent varier selon le modèle sous-jacent.

L'éditeur lui-même commence par le diagnostic en lecture seule : c'est le premier palier. Et un point d'accès MCP actif par défaut sur un système de production s'inscrit à l'inventaire (chapitre 39) : la lecture seule est affirmée pour les agents, pas pour l'ensemble des outils du serveur.

### En modernisation : le modèle mixte

Pour la transformation du code, Capco défend un modèle mixte (*blended*) [2] : un flux de travail conçu par des humains, qui exécute des étapes déterministes pour les tâches prévisibles, utilise des prompts précis pour la génération ciblée, et ne déploie une approche pleinement agentique que là où un raisonnement complexe est requis.

Le cabinet attribue deux risques à l'autonomie complète. L'**erreur amplifiée** : un agent qui interprète mal une règle d'affaires reproduit le défaut, sans bruit, dans des dizaines d'applications. Le **piège de l'hétérogénéité** : des agents en parallèle résolvent le même problème de façons légèrement différentes, et le système cible perd sa cohérence. La supervision humaine reste obligatoire pour l'architecture du cœur, celle des données et le déploiement final. L'autonomie complète convient aux tâches bien définies où la variation est acceptable, comme la documentation tirée d'un code déjà validé.

Capco propose quatre questions à poser à chaque étape [2].

| Question | Si la réponse est oui |
|---|---|
| Le rayon d'impact d'une erreur est-il large ou lent à détecter ? | Pas d'autonomie complète |
| Le résultat doit-il être uniforme sur des centaines de programmes ? | Recette imposée, modèle mixte |
| Un vérificateur peut-il demander comment la décision a été prise ? | Journalisation détaillée de chaque étape |
| L'étape s'exécutera-t-elle des milliers de fois ? | Petits modèles spécialisés et outils déterministes (chapitres 44 et 47) |

Un billet d'AWS du 8 mai 2026 décrit une chaîne construite sur la même idée [8]. Des agents appuyés sur des outils déterministes extraient les règles d'affaires du code COBOL, PL/I et JCL. Un expert valide les spécifications avant toute génération de code. Chaque règle porte un identifiant, repris dans le code produit et dans les tests. Le billet avertit qu'une erreur de spécification se propage au code, et qu'un grand dépôt COBOL ne se confie pas à un agent généraliste.

Cabinet et fournisseur vendent tous deux la démarche : leur convergence n'est pas une preuve indépendante, mais elle indique où placer le contrôle : sur les artefacts intermédiaires (règles extraites, spécifications), pas sur le seul code final. Le critère de sortie reste la parité de comportement avec l'ancien système (25.1).

---

## 25.4 Patrons d'encapsulation

| Patron | Principe | Réserve |
|---|---|---|
| Enveloppe du service existant [1] | La couche nouvelle envoie au cœur la requête qu'il attend déjà; le cœur ne change pas | Hérite des limites de l'interface existante |
| Couche anticorruption [3] | Une façade traduit entre deux sémantiques, pour que le modèle patrimonial ne contamine pas le nouveau | Ajoute de la latence et un service à exploiter |
| Façade d'API sur l'ordinateur central [7] | Des API OpenAPI donnent accès aux applications et aux données z/OS; une passerelle les convertit en outils (chapitre 24) | Effort côté application non précisé par l'éditeur |
| Serveur MCP natif du sous-système [5] | L'éditeur livre les outils avec le produit | Jeu d'outils défini par l'éditeur, à examiner outil par outil |
| Processus exposé comme outil (chapitre 17) | L'outil est une transaction d'affaires entière, avec ses contrôles internes | Exige un moteur de processus |
| Flux de changements en lecture (chapitre 19) | La capture des changements alimente une copie sans charger l'application | La copie ne fait pas foi (25.2) |
| Passerelle d'éditeur [10] | La passerelle expose des API SAP et non SAP comme outils MCP gouvernés | Certains composants ne sont pas en disponibilité générale |

### La couche anticorruption, patron pivot

Issu de la conception pilotée par le domaine, le patron convient, selon Microsoft [3], quand une migration s'étale sur plusieurs étapes ou quand deux sous-systèmes n'ont pas la même sémantique; il ne convient pas sans différence sémantique notable.

Trois de ses consignes valent pour les agents. La couche doit se limiter à la traduction : ni règles d'affaires ni orchestration. Elle sépare des systèmes de niveaux de confiance différents, et c'est donc là que se placent la validation et l'assainissement des entrées. Elle doit être observable, avec des identifiants de corrélation, pour diagnostiquer les échecs de traduction.

C'est dans la couche qu'un vocabulaire d'affaires (« ouvrir un sinistre ») devient la séquence d'appels techniques que le système attend. L'agent reçoit un outil de niveau métier, et la complexité patrimoniale ne franchit pas la frontière. C'est la curation recommandée au chapitre 24.

### Permanente ou transitoire

La même page demande de décider si la couche est permanente ou si elle sera retirée une fois la migration achevée [3]. La question renvoie au figuier étrangleur décrit par Martin Fowler [4] : remplacer un système graduellement, par petites parties, en introduisant des coutures (*seams*) là où il peut être scindé. L'approche exige une architecture transitoire, faite de code destiné à disparaître. Elle ne rend pas la modernisation facile, écrit Fowler; elle rend l'investissement et les bénéfices graduels et visibles.

Si le cœur est sain, l'encapsulation est une architecture cible. S'il est condamné, elle est l'architecture transitoire qui donne des coutures au remplacement. La réponse, à donner au départ, fixe l'effort à consentir sur la couche.

---

## 25.5 Risques : charge et intégrité transactionnelle

Ni [1] ni [2] ne traitent ces deux risques. Ce qui suit relie des exigences lues par un raisonnement signalé comme tel.

### La charge

Un système patrimonial est dimensionné pour des appelants connus : des guichets au rythme humain, des lots en fenêtre de nuit. Un agent décide lui-même du nombre de ses appels : il boucle, réessaie, lance des lectures en parallèle. Ce constat relève du raisonnement, non d'une mesure lue.

Les textes lus offrent trois prises.

- La spécification MCP impose au serveur de limiter le débit des invocations d'outils, et recommande au client des délais d'attente [9]. La limite se pose par agent et par outil, à la passerelle (chapitre 24).
- La couche anticorruption ajoute de la latence et doit elle-même être mise à l'échelle. Sa variante asynchrone, par messages ou événements, découple le domaine moderne des contraintes de débit du système patrimonial [3].
- Dans CICS, le travail MCP s'exécute sous une transaction dédiée [5]. La charge des agents est donc identifiable; s'en servir pour la plafonner est une déduction, non une consigne lue.

S'y ajoutent des mesures traitées ailleurs : cache des lectures (chapitre 5), copies alimentées par les changements (chapitre 19), budgets par agent (chapitre 40).

### L'intégrité transactionnelle

**La réémission.** Une requête MCP interrompue est réémise (chapitre 5), et l'agent d'intégration de 25.1 gère lui aussi reprises et délais [1]. Une écriture non idempotente peut donc s'exécuter deux fois. La clé d'idempotence est le remède; comme la requête réémise porte un nouvel identifiant, la clé voyage en argument de l'outil (chapitre 18). Or une transaction patrimoniale n'en accepte pas toujours : c'est alors à la couche d'encapsulation de la porter et de dédoublonner.

**La frontière de transaction.** Dans une section non normative, la spécification MCP cite la transaction de base de données parmi les états qu'un serveur peut maintenir entre deux appels, au moyen d'un identifiant que le modèle transporte [9]. Sur un système d'enregistrement, ce montage est à éviter : une transaction ouverte entre deux appels attend la décision d'un modèle, verrous tenus. La règle prudente, qui relève du raisonnement, est qu'un appel d'outil corresponde à une transaction d'affaires complète. Ce qui exige plusieurs étapes passe par une Saga et ses compensations (chapitre 18).

**Les garanties ne viennent pas du protocole.** SAP l'écrit pour sa propre pile : persistance, reprises et garanties de livraison dépendent de l'adaptateur et du protocole, le traitement exactement une fois exige un récepteur qui s'y prête, et A2A seul n'assure rien de cela [10]. Microsoft demande de maintenir et de surveiller la cohérence des transactions et des données à travers la couche anticorruption [3].

**L'erreur d'affaires doit remonter.** MCP range l'erreur de logique d'affaires parmi les erreurs d'exécution d'outil, distinctes des erreurs de protocole, que le client devrait transmettre au modèle pour qu'il se corrige [9]. Un rejet du système patrimonial doit donc être traduit en message exploitable. Un échec partiel présenté comme un succès est le pire résultat possible.

**La parité se vérifie.** Les tests de parité sur un jeu de référence [1] se rejouent à chaque changement de la couche. Pour un remplacement, l'exécution en miroir ne vaut sans risque que pour les lectures; les écritures et les traitements par lots demandent une double écriture ou une exécution parallèle rapprochée (chapitre 47).

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Sort du cœur patrimonial | Le figer et l'envelopper | Plateforme obsolète ou incapable de suivre les exigences : le remplacer |
| Place de l'agent | Hors de la frontière de décision : recueillir, valider, expliquer | Décision sans portée réglementaire ni financière (chapitre 17) |
| Premier palier | Lecture seule | Écriture réversible, par outil de niveau métier |
| Voie d'écriture | Interface d'affaires du système | Aucune : pas d'écriture directe dans les tables |
| Autorisation | Décidée par le système d'enregistrement, sous une identité déléguée | — |
| Donnée citée par l'agent | Relue à la source avant toute décision engageante | Copie datée pour l'exploration et la synthèse |
| Encapsulation | Couche anticorruption limitée à la traduction | Sémantiques voisines : façade d'API convertie en outils |
| Modernisation du code | Modèle mixte, validation humaine des artefacts intermédiaires | Autonomie pour la documentation d'un code déjà validé |
| Granularité d'un outil d'écriture | Un appel, une transaction d'affaires complète | Plusieurs étapes : Saga (chapitre 18) |
| Protection de la charge | Limite de débit par agent et par outil | Lectures massives : copie alimentée par les changements |

---

## Points à retenir

- L'agent ne remplace pas le calcul qui fait foi. Il prépare les entrées et explique les résultats; le cœur déterministe reste figé et vérifié par des tests de parité.
- Envelopper n'est pas une règle universelle : un cœur dont la plateforme est obsolète ou ne suit plus les exigences réglementaires ou d'affaires se remplace.
- Un système d'enregistrement garde son autorité si l'agent le cite au lieu de s'en souvenir, écrit par son interface d'affaires et se soumet à son régime d'autorisation.
- Sur l'ordinateur central, l'éditeur lui-même commence par des agents en lecture seule. Le serveur MCP de CICS TS 6.3 est actif par défaut : il doit figurer à l'inventaire.
- Pour moderniser le code, le modèle mixte place le contrôle humain sur les règles extraites et les spécifications. Les sources qui le défendent sont un cabinet et un fournisseur.
- La couche anticorruption est le patron pivot : traduction seulement, validation des entrées, observabilité.
- Il faut déclarer si l'encapsulation est la cible ou une étape d'un remplacement graduel.
- La charge et l'intégrité transactionnelle ne sont réglées par aucun protocole. Limites de débit, idempotence portée par la couche et transaction complète par appel relèvent de la conception.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Architecture & Governance — A. Mehta, « Modernizing Legacy Systems with Agentic AI », 31 juillet 2026](https://www.architectureandgovernance.com/applications-technology/modernizing-legacy-systems-with-agentic-ai/) — article de praticien.
2. [Capco — « AI agents in mainframe modernization », 19 novembre 2025 (PDF)](https://www.capco.com/-/media/CapcoMedia/CAPCO/Intelligence-2025/UK/PDFs/Capco_2025_GenAI_Suite_3_Legacy-Modernization_AI-Agents-in-Mainframe-Modernization.ashx) — point de vue de cabinet-conseil.
3. [Microsoft Learn — patron Anti-Corruption Layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer)
4. [Martin Fowler — Strangler Fig, 22 août 2024](https://martinfowler.com/bliki/StranglerFigApplication.html)
5. [IBM Documentation — CICS TS 6.x, fonctionnement du serveur MCP de CICS](https://www.ibm.com/docs/en/cics-ts/6.x?topic=ai-how-it-works-cics-mcp-server)
6. [IBM Documentation — CICS TS 6.x, fonctionnement des agents CICS](https://www.ibm.com/docs/en/cics-ts/6.x?topic=ai-how-it-works-cics-agents)
7. [IBM — page produit de z/OS Connect](https://www.ibm.com/products/zos-connect) — page commerciale d'éditeur.
8. [AWS — « Reimagining mainframe applications with AWS Transform and Claude Code », 8 mai 2026](https://aws.amazon.com/blogs/migration-and-modernization/reimagining-mainframe-applications-with-aws-transform-and-claude-code/) — billet de fournisseur, lu partiellement.
9. [MCP — Outils, spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)
10. [SAP Architecture Center — A2A et MCP pour l'interopérabilité des agents](https://architecture.learning.sap.com/docs/ref-arch/76ec36)

Aucune source secondaire n'est citée. Les faits sur MCP qui ne figurent pas dans [9] sont repris du chapitre 5.

## Limites de ce chapitre

- L'expression « préserver le cœur déterministe » ne figure pas telle quelle dans [1], qui parle de *deterministic business core*.
- Les sections 25.2 et 25.5 reposent en bonne partie sur un raisonnement d'architecture. Aucune mesure indépendante de la charge imposée par des agents à un système patrimonial, ni d'incidents d'intégrité, n'a été cherchée ni lue.
- La définition du système d'enregistrement et le comportement des verrous d'une transaction ouverte viennent de la connaissance générale.
- Les pages de référence des outils du serveur MCP de CICS n'ont pas été lues : la lecture seule n'est établie que pour les agents préconstruits.
- La documentation technique de z/OS Connect n'a été lue qu'à l'état de table des matières; le chapitre s'appuie sur la page produit.
- Le billet d'AWS [8] n'a été lu que jusqu'à la génération de code, même à la relecture.
- L'audit du 12 novembre 2026 a relu [1], [5], [6], [8], [9] et [10] : faits confirmés, conditions de remplacement corrigées d'après [1]. [2] n'a pu être relu (page en maintenance, PDF hors délai); sa date est confirmée par un extrait de recherche seulement.
- Le pilotage de l'interface utilisateur par un agent, dernier recours quand aucune interface programmable n'existe, n'est couvert par aucune source lue et n'est pas traité.
