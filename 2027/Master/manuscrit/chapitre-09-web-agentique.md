# Chapitre 9 — Le web agentique

*Question directrice : comment exposer un site ou un service à des visiteurs qui sont des agents ?*

> **État de référence :** brouillon WebMCP du Web Machine Learning Community Group dans sa version du 11 novembre 2026; essai d'origine de Chrome (versions 149 à 156); `draft-ietf-webbotauth-httpsig-protocol-01` du 29 octobre 2026; proposition llms.txt modifiée le 10 août 2026; dépôt NLWeb tel que lu le 11 novembre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre; toutes sont des pages primaires lues pour ce chapitre, sauf [19], marquée secondaire.

Un site web a été conçu pour deux visiteurs : une personne, qui lit et clique, et un robot d'indexation, qui lit et repart. Un troisième se présente désormais : l'agent, qui lit, décide et agit pour le compte de quelqu'un. Faute de mieux, il interprète la page affichée et simule des clics et des saisies, ce que la documentation de Chrome appelle l'*actuation* [4]. Le procédé est fragile : l'agent doit deviner à quoi sert chaque élément, et le site ne sait pas à qui il a affaire.

Quatre propositions tentent d'y remédier, chacune pour une question différente; aucune n'est une norme adoptée à la date de ce chapitre. La thèse défendue ici est que deux d'entre elles engagent l'architecture d'une entreprise : celle qui permet d'agir sur le site (WebMCP) et celle qui identifie le visiteur (Web Bot Auth). L'investissement durable se situe toutefois sous les protocoles : une seule logique d'affaires, servie à tous les types de visiteurs et protégée par des contrôles appliqués côté serveur.

---

## 9.1 Deux paris : identité et capacité

Un article de juillet 2026 résume le débat en deux paris [19]. Le premier est un pari d'**identité** : le site dit qui il est et ce que couvre son contenu, au moyen d'un fichier llms.txt. Le second est un pari de **capacité** : le site déclare ce qu'un agent peut y faire, au moyen de WebMCP. L'auteur soutient que seule la capacité fait avancer une transaction.

Ce cadrage est incomplet pour une entreprise. L'identité dont il parle est celle du site; celle du visiteur conditionne pourtant toute politique d'accès. Et entre se décrire et laisser agir, il existe une position intermédiaire : se laisser interroger. Le chapitre retient donc quatre questions.

| Question | Proposition | Porteurs | Statut au 11 novembre 2026 |
|---|---|---|---|
| Que contient le site ? | llms.txt | Jeremy Howard; dépôt d'Answer.AI | Proposition informelle, hors de toute instance de normalisation [15] |
| Que peut-on lui demander ? | NLWeb | Microsoft; code ouvert sous licence MIT | Démonstration de faisabilité, selon son propre dépôt [7] |
| Que peut-on y faire ? | WebMCP | Éditeurs de Google et de Microsoft; groupe communautaire du W3C | Brouillon de groupe communautaire; essai d'origine dans Chrome [1][3] |
| Qui fait la requête ? | Web Bot Auth | Groupe de travail de l'IETF; auteurs de Cloudflare et de Google | Internet-Draft de groupe de travail, révision 01 [11][12] |

Un groupe communautaire du W3C porte l'expression « web agentique » dans son mandat, mais ses brouillons concernent la communication entre agents et se rattachent à ANP (chapitre 7), non l'interface entre un site et un agent [17]. Un tel groupe publie des rapports, pas des recommandations (chapitre 11).

---

## 9.2 WebMCP : exposer des actions dans le navigateur

### Le principe

Avec WebMCP, une page déclare des outils, et l'agent intégré au navigateur les appelle au lieu de manipuler l'interface. Le brouillon définit une API qui permet à une application web de fournir à des agents des outils écrits en JavaScript [1]. Il présente la page comme un serveur MCP dont les outils s'exécutent dans le script du client plutôt que sur un serveur. La parenté avec MCP (chapitre 5) est conceptuelle : WebMCP reprend la forme de l'outil, pas le protocole de transport.

Un outil porte un nom, une description, des schémas d'entrée et de sortie, une fonction d'exécution et des annotations. La page l'enregistre par `document.modelContext.registerTool()`, en contexte sécurisé seulement [1][4].

Chrome documente aussi une voie déclarative : deux attributs posés sur un formulaire HTML, `toolname` et `tooldescription`, en font un outil [5]. Quand l'agent l'invoque, le navigateur remplit les champs sous les yeux de l'utilisateur, et sans l'attribut `toolautosubmit` c'est la personne qui clique sur le bouton d'envoi. L'humain dans la boucle est donc le comportement par défaut [4].

L'outil s'exécute dans la session de l'utilisateur : le brouillon pose comme hypothèse que l'agent hérite de l'identité et du contexte d'authentification du navigateur [1]. Il n'y a ni flux OAuth ni jeton distinct, et l'agent a les droits de la personne connectée. Ensuite, un agent doit visiter la page pour connaître ses outils [4]. WebMCP ne propose pas de découverte hors de la page (chapitre 8).

### Les risques

La section de sécurité du brouillon, non normative, nomme notamment quatre risques [1].

- **L'empoisonnement d'outil.** Le nom et la description d'un outil sont du texte lu par le modèle, donc un vecteur d'injection (chapitre 31).
- **L'injection par la sortie.** Le modèle traite la valeur renvoyée par un outil comme une information fiable, même si elle contient du contenu rédigé par un tiers.
- **L'intention mal représentée.** Rien ne garantit qu'un outil fait ce qu'il annonce, et le brouillon reconnaît qu'aucun mécanisme de vérification n'existe.
- **La surparamétrisation.** Un site peut définir des paramètres que l'agent remplira à partir de ce qu'il sait de l'utilisateur, et en tirer un profil à son insu.

Les parades tiennent surtout en annotations (`readOnlyHint`, `untrustedContentHint`, `consequentialHint`). Le brouillon en fixe lui-même la limite : un agent ne peut pas fonder sa sécurité sur les seules déclarations du site, conclusion qui rejoint celle du chapitre 5. Deux leviers sont plus fermes : l'en-tête `Permissions-Policy: tools=()` désactive WebMCP sur une page, et un outil reste fermé aux autres origines, sauf partage explicite par `exposedTo` [1][6].

Le risque vaut aussi pour le site : le brouillon signale que le chemin de l'interface et celui de l'outil peuvent ne pas appliquer la même validation [1]. Un outil WebMCP doit donc passer par les mêmes validations et les mêmes contrôles d'autorisation côté serveur que le formulaire qu'il double.

### La maturité

Le document est un brouillon de rapport de groupe communautaire, ni norme du W3C ni engagé sur la voie de normalisation; ses quatre éditeurs viennent de Microsoft et de Google [1]. Chrome en a fait un essai d'origine, approuvé le 18 mai 2026 pour les versions 149 à 156, avec une livraison visée en version 157; Gecko et WebKit n'ont donné aucun signal [2][3]. L'API est « en discussion active », et la documentation ne nomme comme agents consommateurs que deux extensions de test [4].

Sa surface a bougé pendant l'essai : le point d'entrée `navigator.modelContext` décrit en juillet [19] est devenu `document.modelContext` [1]. WebMCP reste une expérimentation sérieuse d'un seul moteur, non une cible d'architecture.

---

## 9.3 NLWeb : points d'accès interrogeables

Microsoft a annoncé NLWeb le 19 mai 2025 et en attribue la conception à R. V. Guha, connu pour RSS, RDF et Schema.org [9].

NLWeb se présente comme un ensemble de protocoles ouverts et d'outils à code ouvert qui donnent à un site une interface en langage naturel [7]. Le protocole tient en une méthode, `ask`. Une instance expose deux points d'accès qui prennent les mêmes arguments : `/ask`, en REST, et `/mcp`, qui rend chaque instance utilisable comme serveur MCP. La prise en charge d'A2A est annoncée, sans date [7][8].

Une requête porte la question, au besoin un sous-ensemble de données et les questions précédentes. Un paramètre `mode` choisit entre une liste d'éléments pertinents, la même liste résumée, ou une réponse composée à la manière d'une génération augmentée par récupération [8]. NLWeb s'appuie sur le balisage Schema.org et les flux RSS que les sites publient déjà [7].

À la différence de WebMCP, NLWeb fonctionne côté serveur et ne suppose aucun navigateur : un agent d'entreprise ou un assistant infonuagique peut l'atteindre. Il sert en revanche à interroger un contenu, pas à déclencher une action.

Sa maturité est modeste, de l'aveu de son dépôt : le code y est qualifié de démonstration de faisabilité, et la structure des résultats doit encore changer [7][8]. L'annonce de 2025 nommait des partenaires [9]; aucune donnée d'adoption vérifiable n'a été trouvée pour 2026.

---

## 9.4 Web Bot Auth : signer les requêtes d'agents

### Le problème et le périmètre

Un site reconnaît aujourd'hui un robot à son adresse IP, à son en-tête `User-Agent` ou à une clé d'API partagée. La charte du groupe de travail Web Bot Auth de l'IETF juge ces moyens limités en sécurité, en mise à l'échelle et en gestion [10]. Le groupe vise une authentification cryptographique des clients automatisés : robots d'indexation, archiveurs, robots d'entraînement et agents qui agissent pour un utilisateur.

La charte exclut les API et les interfaces entre agents, l'authentification de l'utilisateur final, un vocabulaire des intentions et toute notion de réputation [10].

### Le mécanisme

Le document du groupe applique les HTTP Message Signatures de la RFC 9421 [12]. L'agent signe chaque requête et y joint trois en-têtes, dont `Signature-Agent`, qui désigne une adresse HTTPS où l'opérateur publie un répertoire de clés au format JWKS. La signature couvre au moins l'autorité ou l'URI visée et porte une date d'expiration. Le serveur récupère le répertoire, vérifie la signature et rattache la requête à l'adresse publiée.

### Ce que la signature prouve

Selon le brouillon [12], une signature valide établit que le détenteur d'une clé publiée à cette adresse a signé le message. Elle ne dit ni qui exploite l'agent, ni s'il est bienveillant, ni si la requête est autorisée. Web Bot Auth fournit un identifiant stable sur lequel fonder une politique, et rien de plus.

Trois limites sont documentées. Il n'y a pas de révocation : retirer une clé n'a d'effet qu'après le rafraîchissement des caches, d'où le recours à des signatures de courte durée. Une signature qui ne couvre que l'autorité peut être rejouée contre le même site jusqu'à son expiration. Et l'identifiant permet de corréler les requêtes d'un agent d'un site à l'autre, ce qui rend le protocole impropre aux agents qui doivent éviter d'être reconnus.

### L'état des travaux et du déploiement

Le groupe n'a qu'un document adopté, à sa révision 01 [11]. Sa charte prévoyait l'envoi des spécifications à l'IESG pour le 30 avril 2026, et du document opérationnel pour le 31 août [10]; la liste des documents ne montre aucun envoi, et ces jalons sont donc dépassés. Une dizaine de brouillons individuels explorent des questions ouvertes, dont un registre et une variante anonyme [11].

Le déploiement précède la norme, et s'en écarte. Cloudflare accepte la signature pour ses robots vérifiés, mais sa documentation renvoie à des brouillons antérieurs et rejette la forme de `Signature-Agent` que le document du groupe prescrit désormais [12][13]. Un opérateur qui signe doit donc vérifier la forme attendue par chaque vérificateur.

Depuis le 1er juillet 2026, Cloudflare distingue deux modèles : l'accès direct, où un seul opérateur émet les requêtes, et l'accès par intermédiaire, où un service agentique est piloté par de nombreux utilisateurs [14]. On peut se fier à l'intermédiaire sans se fier à chacun de ses utilisateurs : c'est le problème de délégation que la charte de l'IETF écarte, et que traitent la section 29.8 et le chapitre 30.

Le brouillon admet que la vérification soit déléguée à un mandataire placé devant le site [12] : la décision de confiance se déplace alors vers le réseau de diffusion de contenu. La charte demande au groupe d'éviter les goulots d'étranglement architecturaux [10].

---

## 9.5 llms.txt : promesse et usage réel

### La proposition

Jeremy Howard a proposé llms.txt le 3 septembre 2024 [15]. Le fichier, rédigé en Markdown, se compose d'un titre obligatoire, d'un résumé et de listes de liens regroupées par sections. La proposition recommande aussi d'offrir pour chaque page une version Markdown à la même adresse.

Le fichier est destiné à l'inférence : un agent le consulte à la demande. Il ne remplace ni robots.txt ni sitemap.xml [15]; sa promesse est celle d'un index choisi, assez court pour tenir dans une fenêtre de contexte.

### L'usage

Une étude publiée par Ahrefs en juin 2026 mesure l'écart entre la promesse et la pratique [16]. Sur 137 210 domaines suivis par ses outils, 28 % publiaient un fichier llms.txt valide. Parmi eux, 97 % n'ont reçu aucune requête sur ce fichier en mai 2026. Quand le fichier est demandé, 96 % des requêtes viennent de robots, et les catégories liées à l'IA en représentent 19,5 %, selon la lecture que l'étude dit elle-même la plus généreuse. Aucun robot d'IA n'a demandé un llms.txt absent : ils ne le cherchent pas.

Deux réserves accompagnent ces chiffres : l'étude vient d'un fournisseur d'outils de référencement, dont la clientèle est plus technique que la moyenne, et une requête ne prouve pas que le fichier a été lu.

Le fichier se répand malgré tout, en partie sans décision : des plateformes de documentation le génèrent automatiquement, et l'outil Lighthouse de Chrome en vérifie la présence [15]. L'article de juillet rapporte la réserve d'un porte-parole de Google, pour qui son intérêt reste spéculatif [19].

### Ce qu'il faut en retenir

Un llms.txt ne contrôle et ne bloque rien. Son terrain plausible est la documentation technique, lue par des agents de programmation à qui l'on indique le fichier [16]. Hors de ce cas, c'est une couverture peu coûteuse, à condition de la générer à partir du contenu du site pour éviter qu'elle diverge.

La proposition laisse un vide : rien n'y exprime ce qu'un agent a le droit de faire. Une prépublication propose de le combler par un manifeste inspiré de robots.txt (chapitre 30) [18].

---

## 9.6 Conséquences pour les canaux numériques de l'entreprise

**Une logique, plusieurs façades.** Un service peut désormais être atteint par une personne, par un agent dans le navigateur de cette personne et par un agent sans navigateur. Les trois doivent passer par la même couche d'affaires et les mêmes contrôles, de sorte que les réponses ne puissent pas diverger.

**Choisir le canal selon l'agent.** Un agent sans navigateur se sert par une API ou un serveur MCP (chapitre 5). Un agent logé dans le navigateur de l'utilisateur se sert par WebMCP, là où il y a des tâches à accomplir : recherche, prix, réservation, retour. Un agent qui ne fait que lire se contente de pages rendues côté serveur et d'un balisage structuré.

**Traiter WebMCP comme une amélioration progressive.** Un seul moteur le met en œuvre, et à l'essai. Le site doit fonctionner sans lui.

**Faire de la gestion des robots une politique d'identité.** Le brouillon de l'IETF distingue trois résultats de vérification : vérifiée, invalide ou non vérifiée faute d'information [12]; la requête non signée relève de la politique du site. La politique d'accès se définit alors par catégorie d'opérateur. L'identité de l'opérateur ne règle pas l'autorisation de l'utilisateur représenté, qui relève des chapitres 29 et 30, ni la preuve du droit d'acheter (chapitre 10).

**Signer ses propres agents.** Une entreprise dont les agents visitent des sites tiers a intérêt à publier un répertoire de clés et à signer ses requêtes, avec des clés distinctes par usage et des signatures de courte durée. Le Trusted Agent Protocol de Visa s'appuie déjà sur Web Bot Auth (chapitre 10).

**Mesurer avant d'investir.** Les journaux du serveur disent quels agents viennent, ce qu'ils demandent et s'ils lisent les fichiers publiés à leur intention.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Canal principal pour les agents | API ou serveur MCP adossé à la logique d'affaires [S] | Parcours qui n'existe que dans l'interface web : envisager WebMCP |
| WebMCP | Expérimenter dans l'essai d'origine, sur un parcours à faible risque [S] | Aucune tâche à accomplir sur le site : s'abstenir |
| Actions à effet (achat, réservation) par WebMCP | Soumission par l'utilisateur, annotation `consequentialHint`, contrôles côté serveur [É] | — |
| Annotations d'outils | Les renseigner, sans en faire une mesure de sécurité [É] | — |
| NLWeb | Attendre; exposer la recherche par un outil MCP existant [É] | Contenu riche en Schema.org et volonté d'expérimenter |
| Robots et agents entrants | Vérifier les signatures Web Bot Auth par le mandataire ou le réseau de diffusion; trois résultats distincts [É] | Trafic d'agents négligeable : conserver les règles actuelles |
| Requête signée | L'identifier, puis appliquer la politique de sa catégorie [É] | Ne jamais y voir une autorisation |
| Agents sortants | Signer, avec clés distinctes et expiration courte [É] | Agent qui doit rester non corrélable : le protocole ne convient pas |
| llms.txt | Le générer pour la documentation technique [M] | Site sans documentation : facultatif; retirer un fichier produit par défaut et non entretenu |

---

## Points à retenir

- Quatre propositions répondent à quatre questions : ce que le site contient (llms.txt), ce qu'on peut lui demander (NLWeb), ce qu'on peut y faire (WebMCP) et qui fait la requête (Web Bot Auth).
- Aucune n'est une norme adoptée au 11 novembre 2026.
- WebMCP reprend la forme de l'outil MCP et l'exécute dans la page, avec la session de l'utilisateur. Seul Chrome le met en œuvre, à l'essai; Gecko et WebKit n'ont donné aucun signal.
- Les annotations d'un outil WebMCP sont des déclarations du site. Le brouillon reconnaît qu'aucun mécanisme ne vérifie qu'un outil fait ce qu'il annonce.
- NLWeb expose une méthode `ask` en REST et en MCP. Son dépôt le qualifie de démonstration de faisabilité.
- Web Bot Auth prouve qu'une requête vient du détenteur d'une clé publiée. Il ne dit rien de l'intention, de l'autorisation ni de l'utilisateur représenté.
- Le groupe de l'IETF a dépassé les jalons de sa charte, et la mise en œuvre la plus visible suit des brouillons antérieurs.
- Selon l'étude d'Ahrefs, 97 % des fichiers llms.txt observés n'ont reçu aucune requête en un mois. Le fichier garde un intérêt pour la documentation technique.
- La décision qui dure est indépendante des protocoles : une seule logique d'affaires, des contrôles côté serveur, et une politique d'accès fondée sur l'identité du visiteur.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [WebMCP — brouillon de rapport du Web Machine Learning Community Group](https://webmachinelearning.github.io/webmcp/)
2. [Chrome for Developers — essai d'origine de WebMCP (9 juin 2026)](https://developer.chrome.com/blog/ai-webmcp-origin-trial)
3. [blink-dev — Intent to Experiment: WebMCP (15 mai 2026)](https://groups.google.com/a/chromium.org/g/blink-dev/c/gmYffo5WOE8)
4. [Chrome for Developers — documentation de WebMCP](https://developer.chrome.com/docs/ai/webmcp)
5. [Chrome for Developers — API déclarative de WebMCP](https://developer.chrome.com/docs/ai/webmcp/declarative-api)
6. [Chrome for Developers — sécurité des outils WebMCP](https://developer.chrome.com/docs/ai/webmcp/secure-tools)
7. [NLWeb — README du dépôt](https://github.com/nlweb-ai/NLWeb)
8. [NLWeb — API REST](https://github.com/nlweb-ai/NLWeb/blob/main/docs/nlweb-rest-api.md)
9. [Microsoft — Introducing NLWeb (19 mai 2025)](https://news.microsoft.com/source/features/company-news/introducing-nlweb-bringing-conversational-interfaces-directly-to-the-web/)
10. [IETF — charte du groupe de travail Web Bot Auth](https://datatracker.ietf.org/wg/webbotauth/about/)
11. [IETF — documents du groupe de travail Web Bot Auth](https://datatracker.ietf.org/wg/webbotauth/documents/)
12. [IETF — draft-ietf-webbotauth-httpsig-protocol-01](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/)
13. [Cloudflare — Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/)
14. [Cloudflare — Verified bots (intégrant les anciens agents signés depuis le 1er juillet 2026)](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/)
15. [llms.txt — page de la proposition](https://llmstxt.org/)
16. [Ahrefs — étude de 137 000 sites sur llms.txt (15 juin 2026)](https://ahrefs.com/blog/llmstxt-study/) — étude d'un fournisseur, lue en entier.
17. [W3C — AI Agent Protocol Community Group](https://www.w3.org/community/agentprotocol/) et sa [fiche de groupe](https://www.w3.org/groups/cg/agentprotocol) — accès automatisé refusé (HTTP 403) le 14 novembre 2026; fiche vérifiée par recherche web.
18. [Permission Manifests for Web Agents (arXiv 2601.02371)](https://arxiv.org/abs/2601.02371) — prépublication; résumé initial, puis extraits relus le 14 novembre 2026.

Source secondaire :

19. [Search Engine Journal — The Agentic Web Is Splitting Into Two Bets: Identity And Capability (10 juillet 2026)](https://searchenginejournal.com/the-agentic-web-is-splitting-into-two-bets-identity-and-capability/578685)

## Limites de ce chapitre

- La source [18], d'abord connue par son seul résumé, a été relue au-delà du résumé le 14 novembre 2026, par un outil qui en rend des extraits; les écarts relevés sont corrigés dans le texte.
- Les pages ont été lues par un outil qui en produit un compte rendu; les formulations rapportées sont des paraphrases.
- Relues pendant l'audit : [1] à [3], [6], [10] à [14]. Les autres, dont [7] à [9] et [16], reposent sur la lecture condensée du 11 novembre 2026.
- Le texte de la RFC 9421 n'a pas été lu. La version stable de Chrome n'a pas été vérifiée : le chapitre ne dit pas si l'essai d'origine est terminé.
- Le dépassement des jalons du groupe Web Bot Auth est déduit de la comparaison entre sa charte et la liste de ses documents. L'adoption par d'autres opérateurs que Cloudflare n'a pas été vérifiée.
- Aucune donnée d'adoption de NLWeb ou de WebMCP n'est citée. Les propos du porte-parole de Google et l'ancien point d'entrée `navigator.modelContext` ne sont connus que par [19].
- La concentration de la décision de confiance dans les réseaux de diffusion de contenu et les options de la grille de décision sont des jugements de ce chapitre.
