# Chapitre 30 — Autorisation et délégation

*Question directrice : comment limiter ce qu'un agent peut faire, et le prouver ?*

> **Version 2 — 11 novembre 2026.** État de référence : spécification MCP `2026-07-28` et feuille de route du 22 août 2026; brouillon `draft-ietf-wimse-aims-01` du 2 novembre 2026, qui remplace `draft-klrc-aiagent-auth` [5]; RFC 8693 et RFC 9396; Authorization API 1.0 d'AuthZEN. Les numéros entre crochets renvoient aux sources en fin de chapitre; toutes sont des pages primaires lues pour ce chapitre ([13] en résumé seulement), sauf [16] et [17], marquées secondaires. Chapitre audité et révisé le 12 novembre 2026.

L'identité dit qui est l'agent et pour qui il agit (chapitre 29). L'autorisation dit ce qu'il peut faire, sur quoi, et pendant combien de temps. Pour un logiciel classique, la réponse s'écrit une fois, parce que le chemin d'exécution est connu. Un agent choisit ses outils en cours de route, à partir d'un contexte qu'un tiers peut avoir influencé, et il confie parfois une partie du travail à d'autres agents. Le droit accordé au départ voyage donc plus loin que ne le voit la personne qui l'a accordé.

La question directrice a deux moitiés. Limiter : réduire le droit à ce que la tâche exige, et le réduire encore à chaque délégation. Prouver : pouvoir montrer après coup quel droit existait, qui l'avait accordé et quelle règle a tranché.

La thèse tient en trois phrases. Les standards règlent bien le premier saut, entre un utilisateur, un client et un serveur. Ils règlent mal la suite : la chaîne de sous-agents, la décision opération par opération, la preuve qu'un humain a approuvé. En attendant, un droit n'est un contrôle que s'il est porté par un jeton étroit et court, décidé hors de l'agent, et consigné; ce qui repose sur la bonne conduite de l'agent (annotation, manifeste, confirmation à l'écran) n'est qu'un signal.

---

## 30.1 Moindre privilège et outils trop permissifs

### Pourquoi le privilège enfle

Le moindre privilège suppose de connaître la tâche. Or le brouillon de l'IETF sur la gestion de l'identité des agents (AIMS) place hors de son périmètre la traduction d'une mission en exigences d'autorisation : c'est une étape de planification, laissée à chaque mise en œuvre [4]. Faute de savoir ce dont l'agent aura besoin, on lui donne large.

Le projet OWASP MCP Top 10, encore en bêta, en fait son deuxième risque : des permissions mal délimitées qui s'étendent avec le temps [14].

### Trois étages de sur-permission

Le privilège excessif se loge à trois étages, selon une grille propre à ce chapitre.

**Le jeton.** Le guide de sécurité de MCP décrit le scénario type : un serveur publie toutes ses portées, le client les demande toutes, et un jeton aux portées génériques (`files:*`, `admin:*`) fuit par un journal ou la mémoire [2]. Le vol d'un tel jeton ouvre tous les outils d'un coup, sa révocation interrompt tous les flux, et une portée fourre-tout masque dans la piste d'audit l'intention de chaque opération. Le remède prescrit est progressif : un ensemble initial minimal, limité à la découverte et à la lecture, puis une élévation ciblée quand une opération privilégiée est tentée [1][2].

Une tension subsiste. Quand la réponse 401 n'indique aucune portée, le client devrait demander toutes celles que le serveur déclare dans `scopes_supported`, champ censé ne contenir que le minimum nécessaire au fonctionnement de base [1]. Le moindre privilège dépend donc de la discipline du serveur : déclarer peu, réclamer avec précision.

**L'outil.** Une portée ne peut pas être plus fine que l'outil qu'elle protège. Un outil qui exécute une requête SQL arbitraire reste trop permissif, quelle que soit la portée exigée : le droit réel se trouve dans l'argument. Découper un outil générique en outils étroits donne un sens aux portées étroites. Les annotations par lesquelles un outil se dit en lecture seule ne comptent pas : le protocole les tient pour non fiables (chapitre 5).

**Le justificatif en aval.** MCP interdit à un serveur d'accepter ou de relayer un jeton qui n'a pas été émis pour lui [1]. Le serveur appelle donc le système protégé avec un autre justificatif. Si c'est un compte de service aux droits étendus, les droits de l'utilisateur ne bornent plus ce que fait l'outil : le serveur devient un délégué plus puissant que chacun de ses appelants. AIMS prévoit que l'outil échange le jeton reçu contre un jeton propre à la ressource visée, et qualifie d'antipatron le fait qu'un outil relaie aux services le jeton reçu de l'agent [4].

---

## 30.2 Chaînes de délégation et autorité réduite des sous-agents

### Usurper ou déléguer

La RFC 8693 distingue deux sémantiques [6]. Dans l'usurpation, l'agent reçoit les droits de l'utilisateur et en devient indiscernable. Dans la délégation, il garde une identité distincte, et le jeton, composite, nomme les deux parties. Seule la seconde laisse une trace de qui a agi. AIMS la retient : l'utilisateur ou le système figure dans la revendication `sub`, l'agent dans `client_id`, et le serveur de ressources doit se servir des deux pour décider [4].

### Ce que la chaîne perd

Quand un agent en mandate un autre, la RFC 8693 permet d'imbriquer des revendications `act` : la plus externe désigne l'acteur courant, les plus profondes les acteurs antérieurs. Le texte précise toutefois que ces acteurs antérieurs sont informatifs et n'entrent pas dans la décision d'accès [6]. À deux sauts de profondeur, le serveur de ressources décide donc sur la foi de l'utilisateur et du dernier agent seulement. Rien ne garantit que les agents intermédiaires avaient le droit de déléguer, ni qu'ils ont réduit ce qu'ils transmettaient.

AIMS ne comble pas ce vide. Le brouillon ne mentionne pas la revendication `act`, ne représente pas de chaîne d'acteurs, et son champ d'audit « sujet délégué » est au singulier. Sa seule règle d'atténuation porte sur la suite d'échanges qui produit les jetons de transaction : la portée de chaque jeton ne peut jamais excéder celle du jeton présenté pour l'obtenir [4]. Il recommande en revanche de pouvoir reconstituer la chaîne d'exécution complète d'une tâche [4], ce que le jeton seul ne permet pas.

### L'état des travaux

| Mécanisme | Ce qu'il apporte | Ce qui manque | Statut |
|---|---|---|---|
| Échange de jeton (RFC 8693) | Nouveau jeton, portée et audience choisies; `act` | Chaîne informative; un appel au serveur d'autorisation par saut | RFC [6] |
| Transaction Tokens | JWT de courte durée, lié à une transaction, qui conserve identité et contexte le long de la chaîne d'appels | Valable dans un seul domaine de confiance; n'est pas un jeton d'accès | Brouillon du groupe OAuth, envoi à l'IESG visé pour décembre 2026 [8][10] |
| Délégation atténuée vérifiable | Chaîne signée, vérifiable hors ligne maillon par maillon | Voir ci-dessous | Brouillon individuel visant la voie normative, 27 octobre 2026 [9] |

Le dernier mécanisme montre vers quoi tend la réflexion. Chaque jeton enfant porte son autorité dans une entrée `authorization_details` et s'engage sur son parent par une empreinte. Un vérificateur contrôle, sans appeler de serveur d'autorisation, que chaque saut est un sous-ensemble du précédent, que la profondeur reste sous un maximum, que le mandant est le même partout, que l'expiration ne dépasse jamais celle du parent et que le porteur détient la clé [9].

Ses limites, reconnues par l'auteur, mesurent la difficulté du problème. Des agents frères peuvent chacun respecter leur plafond et le dépasser ensemble : un budget global exige un registre partagé, hors du jeton. La révocation est retardée par le cache du vérificateur. La comparaison des portées est syntaxique, si bien que deux déploiements peuvent lire différemment la même chaîne [9]. D'autres brouillons individuels circulent, dont un sur des jetons atténuables hors ligne [16] et un sur un en-tête de délégation vérifié maillon par maillon [17].

Côté instances, la feuille de route de MCP pose le problème en toutes lettres : un agent lance des sous-agents qui devraient recevoir une autorité plus étroite que la sienne. Le groupe de travail Agent Identity, chargé d'y répondre, est en formation; il doit s'appuyer sur l'échange de jeton de la RFC 8693 et sur l'ID-JAG [3]. La charte du groupe OAuth de l'IETF prévoit de nouveaux mécanismes pour l'autorisation des agents automatisés qui agissent pour des utilisateurs, sans jalon daté [10].

### En attendant

Quatre règles se déduisent de ces textes et ne dépendent d'aucun brouillon :

- un sous-agent ne reçoit jamais le jeton de son parent; il en obtient un par échange auprès du serveur d'autorisation;
- le jeton enfant vise une seule audience, porte moins de droits et expire avant celui du parent;
- la profondeur de délégation est bornée par la politique, non par l'agent;
- l'orchestrateur consigne la chaîne complète, puisque le jeton ne la porte pas de façon probante.

---

## 30.3 Autorisation par opération

### La portée ne suffit pas

La RFC 9396, publiée en mai 2023, part d'un constat : la portée OAuth convient à des demandes grossières et ne peut exprimer ni un paiement précis ni un droit d'écriture fichier par fichier [7]. Elle ajoute le paramètre `authorization_details`, un tableau d'objets typés dont les champs communs désignent le lieu (`locations`), les opérations (`actions`), les types de données, la ressource (`identifier`) et le niveau de privilège. L'exemple du texte est une initiation de paiement, avec montant et créancier.

Trois propriétés rendent ce mécanisme utile ici. Le serveur d'autorisation rejette tout type ou champ inconnu. Il renvoie avec le jeton les détails réellement accordés, que l'utilisateur a pu réduire. Il les transmet au serveur de ressources, dans le jeton ou par introspection, et ce dernier applique ce qui a été approuvé [7]. La RFC ne donne pas de méthode générale pour comparer deux demandes : la logique est propre à chaque type.

### Où en sont les protocoles d'agents

MCP s'en tient aux portées, mais les rend dynamiques. Le serveur peut déterminer les portées requises d'après les arguments et le contexte de la requête, puis les réclamer par une réponse 403; le client refait une autorisation et réémet l'appel [1]. L'élévation se fait bien opération par opération, mais ce qui est accordé reste une chaîne de caractères, valable pour tous les appels suivants.

La RFC 9396 ne figure pas parmi les textes sur lesquels s'appuie l'autorisation de MCP [1]. AIMS ne la cite pas non plus; le brouillon demande seulement à l'agent de ne solliciter que les portées et les détails d'autorisation minimaux [4]. L'autorisation par opération portée par le jeton existe donc dans OAuth, mais aucun profil ne l'applique aux agents.

### Trois lieux de décision

**À l'émission du jeton.** Les Transaction Tokens lient le contexte de la transaction, par exemple un montant, à un jeton de courte durée [4][8].

**Dans le serveur de ressources.** Le guide de MCP range parmi les erreurs le fait de tenir les portées d'un jeton pour suffisantes sans logique d'autorisation côté serveur [2]. Le serveur connaît l'objet visé et son propriétaire, ce qu'aucun jeton générique ne dit. La même règle vaut pour les identifiants d'état : en posséder un n'est pas un droit [2].

**À la passerelle.** Elle décide outil par outil, avant que l'appel n'atteigne le serveur (section 24.2).

Cette finesse a un coût : chaque élévation est un aller-retour, parfois une interaction avec l'utilisateur. La spécification demande au serveur de réclamer en une fois toutes les portées d'une opération, et au client de borner ses tentatives [1]. Deux limites débordent ce chapitre : des approbations trop fréquentes ne contrôlent plus rien (section 22.5), et une suite d'actions permises une à une peut former une trajectoire qui ne l'est pas (section 32.1).

---

## 30.4 Attestation de présence humaine

### Ce que le jeton ne dit pas

Un serveur de ressources qui reçoit un jeton ne sait pas dans quelle situation il a été utilisé. Trois cas se confondent : une personne a consenti au départ, puis s'est absentée; une personne vient d'approuver cette action précise; personne n'est là, et l'agent tourne sans surveillance. Ces trois cas justifient des décisions différentes.

La feuille de route de MCP le reconnaît : l'autorisation du protocole suppose une personne devant un navigateur au moment du consentement, alors que l'appelant agit de plus en plus pour un utilisateur absent. Elle mentionne l'attestation de présence humaine, qui distinguerait un client interactif d'un agent sans surveillance, parmi les sujets en discussion qui pourraient entrer dans le périmètre du futur groupe de travail [3]. Ce n'est pas un livrable. Aucun standard ne couvre ce besoin aujourd'hui.

### Une confirmation locale n'est pas une preuve

AIMS est ici le texte le plus net [4]. Le serveur d'autorisation peut juger qu'une demande exige une confirmation explicite; il devrait alors la refuser ou obtenir une autorisation supplémentaire. Toute confirmation interactive doit être liée à un octroi vérifiable émis par le serveur d'autorisation. L'agent ne doit pas tenir pour suffisante une simple confirmation dans son interface locale. Il devrait la traduire en événement OAuth, par exemple une élévation au moyen de CIBA, le flux d'authentification par canal secondaire d'OpenID.

La raison est structurelle. Un bouton « Approuver » dans l'hôte est invisible du serveur de ressources et de l'auditeur. Un agent détourné par injection peut affirmer qu'il a été pressé. Seul un octroi émis hors de l'agent prouve qu'un humain authentifié a répondu, et le brouillon recommande d'authentifier l'utilisateur par un mécanisme résistant à l'hameçonnage, comme une clé d'accès [4].

Le brouillon admet une lacune : CIBA ne prévoit qu'une demande lancée par le client, et la confirmation en cours d'exécution appelle une spécification supplémentaire [4]. La RFC 9396 permet de joindre des détails d'autorisation à une demande CIBA [7]; associer les deux lierait l'approbation à une opération décrite. Ce rapprochement est une déduction de ce chapitre, aucun profil ne le définit. Le choix des décisions qui exigent un humain relève du chapitre 22.

---

## 30.5 Manifestes de permissions

### Un fichier déclaratif pour le web

La prépublication « Permission Manifests for Web Agents », signée par le Lightweight Agent Standards Working Group (décembre 2025, révisée en janvier 2026), part d'un constat : `robots.txt` a été conçu pour l'exploration, non pour des agents qui remplissent des formulaires et cliquent. Les exploitants de sites n'ont le choix qu'entre bloquer tout trafic automatisé et imposer une authentification lourde [12].

Les auteurs proposent un manifeste JSON, `agent-permissions.json`, publié sous `/.well-known/` ou désigné page par page au moyen d'une balise de lien. Il comporte quatre sections [12] :

- `metadata` : version du schéma, date, auteur;
- `resource_rules` : des règles qui associent un verbe (lire, cliquer, soumettre un formulaire), un sélecteur CSS, un indicateur d'autorisation et des modificateurs tels qu'une limite de débit ou l'exigence d'un humain dans la boucle;
- `action_guidelines` : des directives en langage naturel, graduées de « doit » à « ne devrait pas »;
- `api` : des renvois vers une API équivalente, de type OpenAPI, MCP ou A2A, que l'agent est invité à préférer à la manipulation de la page.

### Un signal, pas un contrôle

Les auteurs le disent eux-mêmes : la conformité est volontaire et le format, non exécutoire par conception. Un agent malveillant ignore le fichier. Les directives en langage naturel sont difficiles à faire respecter et peuvent servir de vecteur d'injection; le contenu du manifeste doit être traité comme une entrée non fiable. L'article ne présente ni évaluation empirique ni donnée d'adoption, seulement deux mises en œuvre de référence [12].

Ici, c'est la ressource qui annonce ce qu'elle accepte. Les déclarations de ce genre sont de force inégale.

| Déclaration | Qui déclare | Qui l'applique |
|---|---|---|
| `agent-permissions.json` [12] | Le site | Personne; conformité volontaire |
| Annotations d'outil (chapitre 5) | Le serveur MCP | Personne; non fiables par défaut |
| `scopes_supported` [1] | Le serveur de ressources | Le serveur d'autorisation et le serveur |
| Politique d'usage ODRL (chapitre 45) | Le fournisseur de données | Le connecteur; ODRL ne prescrit aucune application |
| Politique codifiée (section 30.6) | L'entreprise | Un point d'application |

Deux usages s'en dégagent. Pour les agents qui naviguent sur des sites tiers, le cadriciel devrait vérifier les règles structurées avant toute commande, de façon déterministe, et ne jamais injecter les directives en langage naturel comme des instructions de confiance. Pour les sites de l'entreprise, le manifeste indique aux agents bien conçus le canal voulu, sans remplacer l'autorisation.

Une autre prépublication, lue en résumé, suit la voie inverse : traduire en contrôles d'accès vérifiables, par extension d'OAuth 2.0 et d'OpenID Connect, des permissions que l'utilisateur exprime en langage naturel [13].

---

## 30.6 Politiques codifiées et points d'application

### Séparer la décision de l'application

L'Authorization API 1.0 du groupe AuthZEN de l'OpenID Foundation, spécification finale publiée le 11 janvier 2026, normalise le dialogue entre un point d'application, qui intercepte la requête, et un point de décision, qui tranche [11]. La question tient en quatre éléments : un sujet, une action, une ressource et un contexte. La réponse est un booléen, accompagné au besoin de motifs ou d'obligations. Des interfaces de recherche renvoient ce qu'un sujet peut atteindre, ce qui permet de filtrer les outils présentés à un agent avant qu'il les appelle.

Le langage de politique est hors du périmètre de cette spécification [11]. AIMS va dans le même sens : une politique peut s'exprimer dans n'importe quel format codifié, pourvu qu'elle soit versionnée, révisable et évaluée de façon cohérente. Le brouillon précise qu'un langage commun n'est pas nécessaire, la confiance entre domaines passant par les jetons (chapitres 29 et 45). Il cite l'interface d'AuthZEN pour interroger un point de décision externe [4]. Le choix du langage revient donc à l'entreprise; l'interface, elle, est normalisée.

### Où appliquer

| Point d'application | Ce qu'il peut décider | Sa limite |
|---|---|---|
| Serveur d'autorisation | Émettre ou non, portée, audience, durée | Ignore les arguments de l'appel, sauf détails d'autorisation |
| Passerelle | Outil permis, quota, approbation (chapitre 24) | Ignore les règles d'affaires du système |
| Serveur de ressources | Objet, propriétaire, montant | Une mise en œuvre par serveur |
| Hôte ou cadriciel | Confirmation, filtrage des outils | Situé dans la frontière de l'agent; ne prouve rien |

Les trois premiers se complètent; le quatrième ne remplace aucun d'eux. Le brouillon « MCP Security Gateway » de Microsoft, détaillé au chapitre 24, illustre un piège : la liste de refus y prime et toute erreur vaut refus, mais une liste d'autorisation vide laisse passer tous les outils [15]. Le moindre privilège demande une configuration délibérée.

### Prouver

AIMS donne ici la réponse la plus précise [4]. Un déploiement doit tenir des journaux d'audit durables, où toute altération est décelable, et suffisants pour reconstituer le comportement de l'agent et son contexte d'autorisation. Sept champs au minimum y figurent : l'identifiant authentifié de l'agent, le sujet délégué, la ressource ou l'outil, l'action et la décision, l'horodatage et un identifiant de corrélation, l'état de posture ou de risque, et les événements de révocation avec leur cause.

Un destinataire de signaux de révocation ou de risque, diffusés par exemple par le Shared Signals Framework, doit appliquer sans retard indu l'autorisation réduite, et ne doit plus utiliser les jetons ni les décisions mis en cache qui ont cessé d'être valides [4]. Le délai n'est pas chiffré.

Le guide de MCP demande de journaliser chaque élévation, portée demandée et portée accordée [2]. Dans l'interface d'AuthZEN, un refus est une réponse HTTP 200 dont la décision vaut faux [11] : il faut compter les décisions, non les codes d'erreur. Enfin, consigner la version de la politique qui a tranché rend la décision rejouable (déduction de ce chapitre).

Le manque d'audit et de télémétrie est le huitième risque du classement OWASP [14]. La séparation entre trace, échantillonnable, et piste d'audit, jamais échantillonnée, relève du chapitre 33.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Portées initiales | Ensemble minimal, lecture et découverte; élévation à la demande | Flux sans utilisateur : portées préapprouvées par politique; site déconnecté : droits répartis avant la coupure (chapitre 46) |
| Conception des outils | Étroits, un effet par outil | Outil générique derrière une règle sur ses arguments |
| Justificatif en aval | Obtenu par échange de jeton, lié à l'appelant | Système patrimonial sans OAuth : compte de service restreint et audit renforcé |
| Délégation à un sous-agent | Jeton neuf, plus étroit, plus court, par échange en ligne; profondeur bornée | Aucun cas pour le relais du jeton parent |
| Opérations à fort enjeu | Décision dans le serveur de ressources, sur l'objet et le montant | Détails d'autorisation (RFC 9396) si le serveur d'autorisation les gère |
| Preuve d'approbation humaine | Octroi émis par le serveur d'autorisation | Confirmation locale pour les actions réversibles et à faible enjeu |
| Manifestes de sites tiers | Règles structurées appliquées par le cadriciel | Directives en langage naturel : jamais comme instructions |
| Politique | Codifiée, versionnée, évaluée hors de l'agent | Très petit parc : listes à la passerelle |
| Piste d'audit | Sept champs d'AIMS, plus la chaîne et la version de politique | — |

---

## Points à retenir

- Le moindre privilège se joue à trois étages : le jeton, l'outil et le justificatif que le serveur emploie en aval. Le troisième peut dépasser les droits de chaque appelant.
- MCP inscrit l'élévation progressive dans son flux, mais le résultat dépend du serveur, qui doit déclarer peu et réclamer avec précision.
- Dans une chaîne de délégation, les acteurs antérieurs sont informatifs selon la RFC 8693, et aucune norme adoptée ne garantit l'atténuation de saut en saut. En attendant, chaque saut repasse par le serveur d'autorisation, et l'orchestrateur consigne la chaîne.
- L'autorisation par opération existe dans OAuth (RFC 9396) sans profil pour les agents; elle se décide aujourd'hui dans le serveur de ressources et à la passerelle.
- Une confirmation dans l'interface de l'agent n'est pas une preuve; seul un octroi émis par le serveur d'autorisation en est une. L'attestation de présence humaine n'a pas de standard.
- Un manifeste de permissions est un signal volontaire, et son texte libre est une entrée non fiable.
- AuthZEN normalise l'interface entre point d'application et point de décision; le langage de politique reste un choix d'entreprise.
- Prouver, c'est tenir un journal de chaque décision où toute altération se détecte, et appliquer les révocations aux décisions mises en cache.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [MCP — Autorisation, spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization.md)
2. [MCP — Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)
3. [MCP — Feuille de route, mise à jour du 22 août 2026](https://modelcontextprotocol.io/development/roadmap.md)
4. [IETF — draft-ietf-wimse-aims-01, AI Identity Management System](https://www.ietf.org/archive/id/draft-ietf-wimse-aims-01.txt)
5. [IETF — draft-klrc-aiagent-auth, remplacé par [4]](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/)
6. [RFC 8693 — OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693.html)
7. [RFC 9396 — OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html)
8. [IETF — draft-ietf-oauth-transaction-tokens](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/)
9. [IETF — draft-asor-wimse-agent-delegation-chain-03](https://www.ietf.org/archive/id/draft-asor-wimse-agent-delegation-chain-03.html)
10. [IETF — charte du groupe de travail OAuth](https://datatracker.ietf.org/wg/oauth/about/)
11. [OpenID AuthZEN — Authorization API 1.0](https://openid.net/specs/authorization-api-1_0.html)
12. [Permission Manifests for Web Agents (arXiv 2601.02371)](https://arxiv.org/abs/2601.02371)
13. [Authenticated Delegation and Authorized AI Agents (arXiv 2501.09674)](https://arxiv.org/abs/2501.09674) — résumé seulement
14. [OWASP MCP Top 10 — page du projet](https://owasp.org/projects/mcp-top-10)
15. [Microsoft — MCP Security Gateway 1.0, brouillon](https://microsoft.github.io/agent-governance-toolkit/specs/MCP-SECURITY-GATEWAY-1.0/)

Sources secondaires (résultat de recherche seulement, pages non lues) :

16. [IETF — draft-niyikiza-oauth-attenuating-agent-tokens-00](https://www.ietf.org/archive/id/draft-niyikiza-oauth-attenuating-agent-tokens-00.html)
17. [IETF — draft-hamr-oauth-agent-delegation-01](https://www.ietf.org/archive/id/draft-hamr-oauth-agent-delegation-01.html)

## Limites de ce chapitre

- Les pages ont été lues par un outil qui en restitue un résumé. L'audit du 12 novembre a relu, avec citations, AIMS [4], la spécification [1] et la feuille de route [3] de MCP, [5], [9], [10], [11] et le résumé de [12]; les énoncés qui en dépendent sont confirmés ou corrigés. Les mots-clés attribués aux RFC 8693 et 9396 et au guide [2] n'ont pas été relus.
- AIMS est un brouillon de groupe de travail, de statut visé informatif; [9], [16] et [17] sont des brouillons individuels. Aucun n'est une norme; tous peuvent changer ou expirer.
- La charte OAuth lue (version 06) n'affiche pas de date d'approbation; une révision en juin 2026, relevée dans un résultat de recherche, n'a pas été confirmée et n'est pas reprise. L'intitulé « Complex Delegation » de la version 1, non retrouvé, est retiré.
- CIBA et le Shared Signals Framework sont décrits d'après AIMS, sans lecture de leurs spécifications; [8] et [15] n'ont pas été relus pendant l'audit. Les fiches détaillées des risques OWASP n'ont pas été lues.
- Les trois étages de sur-permission, le découpage des outils, les quatre règles de la section 30.2, le tableau des points d'application et le rapprochement entre CIBA et la RFC 9396 sont des analyses de ce chapitre, non des énoncés de norme.
- Aucun langage de politique n'est comparé, faute de source lue. Aucun chiffre d'adoption ou d'efficacité n'est cité : les sources lues n'en donnent pas.
- Le passage entre domaines (chaînage d'identité, ID-JAG) est laissé au chapitre 29, et les politiques d'usage entre organisations au chapitre 45.
