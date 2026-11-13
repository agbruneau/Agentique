# Chapitre 10 — Commerce agentique

*Question directrice : comment un agent prouve-t-il qu'il a le droit d'acheter ?*

> **Version 2 — 11 novembre 2026.** État de référence : AP2 v0.2, UCP (versions datées; les exemples de la spécification portent `2026-08-25`), Agentic Commerce Protocol `2026-04-17` (bêta), Verifiable Intent (brouillon v0.1), x402 (dépôt de la x402 Foundation) et Machine Payments Protocol. Les numéros entre crochets renvoient aux sources : [1] à [12] sont des pages primaires lues pour ce chapitre; [13] à [16] sont des prépublications dont seul le résumé a été lu; [17] à [19] sont secondaires ou non lues. Chapitre audité et révisé le 12 novembre 2026.

Un paiement par carte repose sur une hypothèse rarement énoncée : la personne qui clique sur « payer » détient le moyen de paiement, ou agit sous les yeux de son titulaire. Un agent qui achète rompt cette hypothèse. Le marchand reçoit une commande d'un logiciel; l'émetteur voit passer une transaction que son client n'a pas saisie; le client découvre le résultat après coup.

L'identité de l'agent ne répond pas à ces inquiétudes. Savoir quel agent émet une requête (chapitres 9 et 29) ne dit rien de ce que son utilisateur l'a autorisé à dépenser. La réponse qui se dégage des spécifications de 2026 est un objet signé, le mandat, qui lie une personne, un panier et un paiement, et que chaque partie vérifie sans se fier au modèle de langage.

Ce chapitre soutient deux thèses. Les protocoles convergent sur la forme de la preuve, mais non sur les rails qui la transportent, et aucun ne couvre un achat de bout en bout. Et la preuve reste étroite : elle montre ce qui a été autorisé, sans dire qui paie quand l'agent se trompe, question que les spécifications lues écartent expressément.

---

## 10.1 Une pile en couches

Un achat par agent se décompose en quatre questions, auxquelles répondent des protocoles distincts.

| Couche | Question | Protocoles |
|---|---|---|
| Découverte | Que vend ce marchand, et par quelle interface ? | UCP (catalogue, profil `/.well-known/ucp`); ACP (flux de produits) |
| Autorisation | Qu'a permis l'utilisateur, et qui est l'agent ? | AP2, Verifiable Intent; Visa Trusted Agent Protocol |
| Paiement | Quel justificatif à portée limitée l'agent présente-t-il ? | Jetons des réseaux et des prestataires de paiement |
| Règlement | Comment la valeur change-t-elle de mains ? | Rails de cartes existants; x402; MPP |

Le découpage est commode, pas normatif. Un billet de l'AAIF, daté du 20 août 2026, retient plutôt cinq responsabilités : brancher un agent sur le parcours d'achat d'un marchand, identifier un agent sur un site existant, prouver ce que l'utilisateur a autorisé, fournir des justificatifs de paiement limités, payer des services numériques [12]. Les deux lectures mènent au même constat : aucun protocole ne couvre un achat complet sur l'ensemble du web.

D'une couche à l'autre, les protocoles se composent : UCP délègue la preuve d'autorisation à AP2, et les exemples d'AP2 couvrent aussi bien les cartes que x402 [1][4]. La concurrence se joue à l'intérieur de chaque couche (section 10.6).

Ils s'appuient sur les protocoles déjà décrits : UCP et ACP se transportent sur MCP (chapitre 5), UCP aussi sur A2A (chapitre 6), et le Trusted Agent Protocol de Visa repose sur les signatures de requêtes HTTP du chapitre 9.

---

## 10.2 Prouver l'intention : AP2 et Verifiable Intent

### Le mandat, unité de preuve

AP2 (Agent Payments Protocol), publié par Google, ne décrit ni catalogue ni panier. La spécification se définit comme une fonction de sécurité logée dans un protocole de commerce, et se dit conçue pour être compatible avec UCP [1]. Son objet est le mandat : un justificatif signé qui atteste ce qu'un utilisateur a approuvé.

La version lue, v0.2, non datée, définit deux mandats [1].

Le **Checkout Mandate** porte sur le contenu de l'achat. Le marchand émet d'abord un objet de caisse qu'il signe; le mandat y est lié par hachage. L'agent le présente au marchand, qui le vérifie et renvoie un reçu.

Le **Payment Mandate** porte sur l'autorisation de payer. Il est lié au même objet de caisse par hachage, et vérifié par le fournisseur de justificatifs, le réseau et le processeur de paiement du marchand. Un reçu de paiement suit.

Chaque mandat existe en deux états. **Ouvert**, il exprime des contraintes : c'est ce que signe un utilisateur qui délègue un achat à venir. **Fermé**, il décrit une transaction précise. Les vérificateurs ne reçoivent que des mandats fermés.

Les mandats sont des SD-JWT, un format de jeton à divulgation sélective. Un mandat ouvert doit contenir la clé publique de l'agent, dans une revendication `cnf` : c'est ce qui permet ensuite à l'agent, et à lui seul, de signer les mandats fermés qui en découlent. La spécification recommande l'expiration la plus courte que la tâche permette.

### Cinq rôles, dont un qui ne peut pas être un agent

| Rôle | Fonction | Peut être un agent ? |
|---|---|---|
| Shopping Agent | Agit pour l'utilisateur et présente les mandats | Oui, c'est le cas attendu |
| Credential Provider | Vérifie le mandat de paiement et remet un justificatif | Oui ou non |
| Merchant | Signe l'objet de caisse et vérifie le mandat de caisse | Oui ou non |
| Merchant Payment Processor | Vérifie le mandat de paiement | Oui ou non |
| Trusted Surface | Présente à l'utilisateur ce qu'il approuve | Non |

Un même acteur peut tenir plusieurs rôles [1]. Deux exigences donnent au dispositif sa valeur. La surface de confiance ne doit pas être agentique : ce que l'utilisateur voit au moment d'approuver n'est pas produit par un modèle. Et la validation des mandats doit s'exécuter dans du code déterministe, que le rôle soit tenu par un agent ou non. La vérification ne dépend donc jamais du jugement d'un modèle; le choix du contenu des mandats, laissé hors du champ, en dépend.

### Deux parcours

Dans le parcours **avec présence humaine**, l'utilisateur approuve sur la surface de confiance le panier fermé et le paiement. Le fournisseur de justificatifs vérifie le mandat de paiement et remet un justificatif; le marchand conclut la transaction.

Dans le parcours **sans présence humaine**, l'utilisateur approuve des contraintes, sous forme de mandats ouverts. L'agent signe ensuite, avec sa propre clé, les mandats fermés. Un garde-fou encadre les essais : l'agent ne doit pas présenter un nouveau mandat ouvert sans avoir obtenu un reçu de rejet pour le précédent [1].

### Ce qu'AP2 laisse dehors

La spécification énumère ses exclusions [1] : le détail du protocole de commerce; la façon dont l'agent arrête le contenu des mandats; la résolution des litiges, ainsi que la conservation et la récupération des preuves; la délégation de mandat d'un agent à un autre; un langage de requête normalisé pour les mandats.

Elle affirme que mandats et reçus, pris ensemble, donnent de la transaction une image non répudiable, utilisable comme preuve une fois les vérifications réussies. Elle ne répartit pas la responsabilité entre les rôles. La preuve existe; la règle qui dit quoi en faire n'y est pas (chapitre 36).

### Verifiable Intent

Verifiable Intent se présente comme une spécification ouverte d'autorisation cryptographique des agents dans le commerce, au stade de brouillon v0.1 et sous licence Apache 2.0 [7]. Le billet de l'AAIF l'attribue à Mastercard, avec Google, et la décrit comme un complément d'AP2 [12]; la page du projet ne nomme pas ses auteurs.

Sa structure tient en trois couches, chacune contraignant la suivante.

| Couche | Signataire | Contenu |
|---|---|---|
| 1 — Identité | L'émetteur | Un justificatif d'identité |
| 2 — Intention | L'utilisateur | Des contraintes |
| 3 — Action | L'agent | La preuve qu'il agit dans ce périmètre |

Le tout forme une chaîne de délégation en SD-JWT, où chaque maillon est lié au suivant par confirmation de clé. La page annonce huit types de contraintes vérifiables par machine et en nomme quatre : bornes de montant, listes de marchands autorisés, plafonds de budget, conditions de récurrence. Elle fournit des correspondances avec AP2, ACP et UCP.

Le format et la logique sont ceux d'AP2. L'apport propre est le premier maillon, qui rattache la chaîne à un émetteur : selon le billet de l'AAIF, marchands et émetteurs peuvent ainsi vérifier l'approbation chacun de leur côté [12].

---

## 10.3 Passage en caisse : ACP et UCP

### Agentic Commerce Protocol

L'Agentic Commerce Protocol (ACP) a été élaboré par Stripe et OpenAI, sous licence Apache 2.0 [5]. Il permet à un marchand d'exposer un passage en caisse destiné aux agents, par REST ou par MCP. Le marchand demeure le marchand attitré (*merchant of record*) : il décide des produits vendus, de leur présentation et de l'exécution des commandes.

Le dépôt qualifie la spécification de **bêta** [6]. Cinq versions datées se sont succédé depuis septembre 2025, dont deux en janvier 2026 (négociation de capacités, extensions, gestionnaires de paiement); la plus récente, `2026-04-17`, couvre le panier, le flux de produits, les commandes, l'authentification et MCP. Le paiement délégué s'appuie sur un jeton à portée limitée, le Shared Payment Token, dont Stripe est le premier prestataire compatible [5].

Trois réserves s'imposent. La gouvernance est conjointe entre OpenAI et Stripe; le passage à une fondation neutre est annoncé sans échéance [6]. Le site reconnaît que la découverte des marchands compatibles est encore en développement, et que chaque plateforme d'IA gère son propre processus de participation [5]. Enfin, le premier débouché du protocole s'est rétréci : selon le billet de l'AAIF, OpenAI a recentré son usage sur la découverte de produits en mars 2026 [12]; un billet de fournisseur, qui cite la presse, parle d'un abandon de l'achat intégré à ChatGPT faute d'adoption [17].

### Universal Commerce Protocol

UCP se présente comme un standard ouvert qui va de la découverte au suivi après achat [2]. Sa page d'accueil le dit élaboré par Google, Shopify, de grands détaillants, Microsoft, Meta, Salesforce et Stripe, entre autres, et appuyé notamment par Mastercard, Visa et PayPal. La licence est Apache 2.0.

Le protocole s'organise en capacités : catalogue, panier, passage en caisse, liaison d'identité par OAuth 2.0, commande. Des capacités pour l'hébergement et la restauration sont à l'état de brouillon [2].

Son mécanisme central est la négociation [3]. Le marchand publie un profil à l'adresse `/.well-known/ucp`. La plateforme de l'agent publie le sien et en transmet l'adresse à chaque requête, dans un en-tête `UCP-Agent` ou dans les métadonnées MCP. Les capacités sont appariées par nom, à la version commune la plus récente. Quatre transports sont prévus : `rest`, `mcp`, `a2a` et `embedded`, ce dernier affichant la caisse du marchand dans l'interface de la plateforme.

Le paiement passe par des gestionnaires (*payment handlers*) que le marchand déclare et classe par préférence [3]. La plateforme obtient un jeton du fournisseur de justificatifs et le remet au marchand; elle ne devrait pas toucher aux données de carte brutes, ce qui lui évite le périmètre PCI DSS. Pour un agent autonome, l'extension AP2 remplace le jeton par des mandats : le marchand signe l'état du panier, la plateforme produit, après consentement de l'utilisateur, un mandat de caisse et un mandat de paiement, et le processeur vérifie le second [3][4]. Les requêtes peuvent aussi porter des signatures RFC 9421 (chapitre 9).

La spécification énonce elle-même deux limites [3]. Le lien entre un nom et un domaine prouve la provenance, pas la confiance : négocier ou non avec une contrepartie reste la décision de chaque partie. Et UCP ne prescrit aucun calendrier de dépréciation; le retrait d'une version est une décision du marchand, loin de la fenêtre minimale de douze mois de MCP (chapitre 5).

### Comparaison

| | ACP | UCP |
|---|---|---|
| Origine | Stripe et OpenAI [5] | Google, Shopify et un large groupe de détaillants et de plateformes [2] |
| Statut | Bêta, versions datées [6] | Versions datées; verticales en brouillon [2][3] |
| Découverte du marchand | En développement [5] | Profil `/.well-known/ucp` [3] |
| Preuve d'autorisation | Jeton de paiement à portée limitée | Mandats AP2, sur activation [4] |
| Gouvernance | Deux mainteneurs fondateurs [6] | Un « organe de gouvernance » cité, non nommé [3] |

Les deux laissent au marchand la relation client et l'exécution. ACP part de la caisse; UCP part de la découverte et descend jusqu'à la commande.

---

## 10.4 Réseaux de cartes

### Visa Trusted Agent Protocol

La page de Visa décrit le Trusted Agent Protocol comme un standard cryptographique qui permet aux marchands de distinguer un agent légitime d'un robot ou d'un collecteur [8]. Le mécanisme est celui de la RFC 9421 : l'agent joint une signature à sa requête; le marchand reconstitue la base de signature et la vérifie avec la clé publique de l'agent.

Le protocole prévoit en outre la validation de l'intention de l'agent, ainsi que des signatures pour la reconnaissance du consommateur et pour le paiement. Le billet de l'AAIF, qui l'attribue à Cloudflare et à Visa, précise qu'il s'appuie sur Web Bot Auth et indique si l'agent signé navigue ou tente de payer [12].

Un marchand qui bloque les robots à sa périphérie bloque aussi les agents acheteurs; une signature vérifiable lui permet de laisser passer ceux qui viennent payer. Le protocole répond donc à une question antérieure à celle d'AP2 : il ne prouve pas ce que l'utilisateur a autorisé, mais que l'appelant est un agent reconnu. La page parle d'agents approuvés par Visa; l'approbation relève du réseau, pas d'un registre ouvert.

### Mastercard Agent Pay

Les pages de Mastercard sont restées inaccessibles [18]. Mastercard est à l'origine de Verifiable Intent, selon le billet de l'AAIF [12], et figure parmi les appuis d'UCP [2]. Le même billet range Mastercard, avec Visa, American Express et Stripe, parmi les acteurs dotés chacun d'un schéma propriétaire de justificatifs limités, faute de standard ouvert commun aux réseaux. D'après un résumé de moteur de recherche, Mastercard y annonce l'intégration de Verifiable Intent aux API d'intention d'Agent Pay, dont le fonctionnement reste à établir.

---

## 10.5 Règlement natif : x402

Les protocoles précédents ajoutent une preuve à des rails existants. x402 fait l'inverse : il place le paiement dans l'échange HTTP lui-même.

### Mécanisme

x402 se définit comme un standard de paiement ouvert, sous licence Apache 2.0, qui permet à un service de facturer l'accès à une API ou à un contenu directement sur HTTP, au moyen du code d'état 402 Payment Required [9]. L'échange s'appuie sur trois en-têtes [10] :

1. le client demande une ressource; le serveur répond 402 et joint ses exigences de paiement dans `PAYMENT-REQUIRED`;
2. le client prépare une charge de paiement et réémet sa requête avec `PAYMENT-SIGNATURE`;
3. le serveur vérifie et règle le paiement, puis sert la ressource avec `PAYMENT-RESPONSE`.

Le serveur peut vérifier et régler lui-même, ou s'en remettre à un **facilitateur**, qui expose `/verify` et `/settle` [9][10]. Trois schémas sont documentés : `exact` (un montant précis), `upto` (un plafond par requête, le vendeur réglant l'usage réel) et `batch-settlement` (séquestre et bons hors chaîne, encaissés par lots, sur chaînes EVM seulement) [10].

Le client n'a ni compte, ni session, ni identifiants à gérer [9]. C'est l'attrait pour un agent : payer une ressource à l'unité, sans relation commerciale préalable.

### Gouvernance et portée

Le dépôt d'origine, chez Coinbase, n'est plus qu'une copie de développement : le projet a été transféré sous une x402 Foundation (`x402-foundation/x402`) [10]. Le protocole vise tous les réseaux, cryptographiques comme fiduciaires; les SDK listés visent des chaînes de blocs, et le billet de l'AAIF décrit un règlement en cryptomonnaies stables [10][12].

Parmi ses principes, un seul touche à la sécurité : ni le facilitateur ni le serveur ne doivent pouvoir déplacer des fonds au-delà de l'intention du client [10]. Les pages lues ne disent rien du remboursement, du litige ni de l'identité du payeur.

### MPP, le voisin

Le Machine Payments Protocol (MPP), corédigé par Tempo et Stripe, emploie le même code 402 avec une autre grammaire : le serveur émet un défi (Challenge) qui liste les options de paiement, le client répond par un justificatif (Credential) qui prouve le paiement, le serveur renvoie un reçu (Receipt) [11]. Il se veut neutre quant au moyen de paiement (cryptomonnaies stables, cartes, virements). Sa page renvoie à un brouillon de l'IETF sans en préciser l'état. Litiges et identité y sont présentés comme des ajouts possibles, non comme des acquis.

### Ce que cela vaut pour une entreprise

Le règlement natif convient à un cas précis : des appels nombreux et de faible valeur vers des services que l'agent découvre en cours de tâche. Il déplace toutefois la preuve. Les pages lues ne décrivent aucune autorisation distincte du paiement : le droit d'acheter s'y confond avec la capacité de produire une charge de paiement valide. La limite de dépense n'est pas dans le protocole; elle doit être posée en amont, sur le portefeuille ou à la passerelle (chapitre 40). Un mandat AP2 peut porter l'autorisation et x402 le règlement, puisque AP2 se déclare indépendant de l'instrument [1].

---

## 10.6 Rails non interopérables : état de la fragmentation

| Besoin | Propositions concurrentes | Pont entre elles |
|---|---|---|
| Passage en caisse | ACP, UCP | Aucun dans les pages lues; MCP comme transport commun |
| Preuve d'intention | AP2, Verifiable Intent | Correspondances de Verifiable Intent avec AP2, ACP et UCP [7] |
| Reconnaissance de l'agent | Trusted Agent Protocol; dispositifs des autres réseaux | Web Bot Auth comme socle [12] |
| Justificatif limité | Schémas de Stripe, Visa, Mastercard, American Express | Aucun; schémas propriétaires [12] |
| Paiement sur HTTP 402 | x402, MPP | Aucun dans les pages lues |

**La fragmentation est horizontale.** Les protocoles s'emboîtent d'une couche à l'autre et se doublent au sein d'une couche. Un marchand qui veut être joignable par tout agent doit mettre en œuvre deux caisses, reconnaître plusieurs schémas de signature et accepter plusieurs jetons.

**Les mêmes acteurs sont des deux côtés.** Stripe corédige ACP et MPP, et figure parmi les concepteurs d'UCP [2][5][11]. La fragmentation traduit des paris parallèles plutôt que des camps.

L'AAIF a constitué un groupe de travail sur le commerce agentique, présidé par un représentant de Shopify et coprésidé par un représentant d'OpenAI, soit un acteur de chacun des deux protocoles de caisse [12]. Le billet pose trois principes : aucune couche ne devrait exiger la pile entière d'un fournisseur; un agent devrait pouvoir utiliser plusieurs réseaux de paiement; l'autorisation devrait rester lisible quand la tâche change d'agent, cas qu'AP2 exclut. Aucun livrable n'y est cité; la gouvernance de l'AAIF est décrite au chapitre 11.

Pour l'entreprise, la conséquence est une architecture à adaptateurs : un modèle interne du panier, du mandat et du paiement, et un adaptateur par protocole externe, pour qu'un changement de version ou l'abandon d'un rail ne touche pas le cœur.

---

## 10.7 Sécurité

Les quatre prépublications retenues n'ont été lues qu'en résumé; leurs chiffres sont ceux des auteurs.

### Des garanties implicites

Une analyse formelle modélise x402, MPP, ACP et AP2 dans le vérificateur Tamarin [13]. Sur 86 cas de vérification, elle reproduit 46 cas connus ou d'étalonnage et relève 40 constats de cohérence formelle non documentés jusque-là. Les contre-exemples font ressortir trois familles de lacunes : des liaisons manquantes, des contraintes d'état absentes, des correspondances non garanties d'une étape à l'autre. Les auteurs en tirent 18 principes de sécurité communs.

Leur diagnostic : intention, délégation, usage du justificatif, règlement et exécution sont répartis entre acteurs et étapes, si bien qu'aucun message ni participant ne peut seul faire respecter la sécurité. Les garanties restent implicites dans des spécifications et des mises en œuvre de référence mouvantes; elles devraient y être écrites.

### Des failles indépendantes du modèle

Une deuxième prépublication, signée d'un seul auteur, recense 33 vulnérabilités structurelles sur trois plateformes de commerce agentique, que son résumé ne nomme pas [15]. Chacune réussit de façon déterministe quel que soit le modèle déployé, avec un taux de succès de 100 % là où la mesure a été faite en conditions réelles; trois d'entre elles s'enchaînent en un détournement de paiement de bout en bout. La défense proposée ramène le taux de succès à zéro pour quatre des cinq classes structurelles.

L'article sépare les attaques structurelles, logées dans le protocole, des attaques sémantiques comme l'injection de prompt (chapitre 31). Améliorer le modèle ne corrige pas les premières.

### L'écart entre la spécification et l'exécution

Une troisième étude porte sur le cycle de vie des mandats d'AP2 [16]. Signature, liaison explicite et expiration donnent des garanties au niveau de la spécification. À l'exécution, les nouveaux essais, la concurrence et l'orchestration rompent des hypothèses tacites : un mandat valide peut être rejoué, ou appliqué à un autre contexte. La réponse proposée est une couche de vérification à l'exécution qui impose la liaison au contexte et l'usage unique du mandat, au moyen de nonces à durée limitée. Les auteurs rapportent une latence d'environ 3,8 ms jusqu'à 10 000 transactions par seconde, résultat obtenu **par simulation**.

Un agent qui réémet une requête après une coupure fait ce que ferait un attaquant qui rejoue un mandat : distinguer les deux exige une clé d'idempotence et un état partagé entre vérificateurs (chapitre 18). UCP demande d'ailleurs au marchand d'imposer l'idempotence contre les doubles débits [3].

### Une lecture transversale

Une systématisation des connaissances couvre sept protocoles, dont AP2, x402, ACP et MPP, et ordonne les menaces selon cinq dimensions, de l'intégrité de l'agent à la conformité réglementaire [14]. Elle en dérive douze vecteurs d'attaque qui traversent les couches : une défaillance née dans le raisonnement ou l'outillage se propage jusqu'à la garde des fonds et au règlement.

D'autres prépublications, repérées mais non lues, visent AP2 et x402 pris isolément [19].

### Fraude et litiges

Les spécifications produisent des éléments de preuve; elles ne disent ni qui les conserve, ni qui supporte la perte. AP2 exclut expressément la résolution des litiges [1]; MPP la range parmi les ajouts possibles [11]; les pages de x402 n'en parlent pas. Le droit applicable relève du chapitre 36; la grille de décision retient une mesure minimale : verser mandats et reçus à la piste d'audit.

---

## 10.8 Approvisionnement interentreprises entre agents

C'est la section la moins étayée du chapitre : aucune spécification ni aucun article évalué par les pairs sur l'approvisionnement entre agents n'a été trouvé. Elle s'appuie sur un billet de fournisseur [17], sur les exclusions des spécifications lues et sur le chapitre 45, qui traite contrats d'usage, négociation et règlement entre organisations.

### Un modèle pensé pour le consommateur

Les protocoles décrits modélisent un achat de détail; le billet résume en trois écarts ce qui en sépare l'approvisionnement [17].

| Hypothèse des protocoles de détail | Réalité de l'approvisionnement |
|---|---|
| Un prix affiché | Des prix contractuels, par compte, palier de volume et droits |
| Un panier prêt à payer | Un dossier, de la soumission à la commande, prêt à approuver |
| Un acheteur, un justificatif | Un groupe d'achat, des seuils budgétaires, une chaîne d'approbation |

Les spécifications confirment cet écart par leurs silences. AP2 place hors de son champ la délégation de mandat d'un agent à un autre [1], alors qu'une chaîne d'approbation est une délégation à plusieurs maillons. Les contraintes que nomme Verifiable Intent (montant, marchands, budget, récurrence) expriment la consigne d'une personne, non la politique d'une organisation [7].

### Ce qui peut servir dès maintenant

A2A fournit la délégation de tâche entre agents qui ne se contrôlent pas (chapitre 6); une demande de prix, une proposition et une contre-proposition peuvent s'y échanger. Aucun protocole lu ne fixe la sémantique commerciale : forme d'une soumission, d'un bon de commande, de conditions de paiement.

Quatre orientations se dégagent, à titre d'hypothèses de travail.

**Garder le système d'enregistrement comme autorité.** Prix contractuels, seuils et approbations vivent dans le progiciel de gestion. L'agent les consulte par des outils (chapitre 5); il ne les porte pas dans un mandat.

**Traiter l'approbation comme un point de contrôle déterministe.** La chaîne d'approbation relève de l'orchestration et de l'humain dans la boucle (chapitres 17 et 22), non du protocole de paiement.

**Rapprocher avant de payer.** Un mandat prouve une autorisation, pas une livraison; le chapitre 45 propose de ne l'émettre qu'après concordance du bon de commande, de la réception et de la facture (section 45.7).

**Rendre les données commerciales lisibles par machine.** Le billet insiste sur ce préalable : attributs complets, unités cohérentes, conditions par compte exposées par API plutôt que dans des PDF ou des portails [17]. C'est le sujet du chapitre 15.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Autoriser un agent à acheter | Présence humaine : approbation du panier fermé sur une surface non agentique | Achats répétitifs de faible valeur : mandat ouvert, contraintes étroites, expiration courte |
| Preuve d'autorisation | Mandats signés, vérifiés en code déterministe | — |
| Protocole de caisse, côté marchand | Modèle interne et adaptateurs, selon les plateformes d'agents visées | Canal unique imposé par un partenaire |
| Reconnaissance des agents à la périphérie | Vérification des signatures de requêtes HTTP (chapitre 9) | Site sans transaction |
| Plafond de dépense | Imposé hors de l'agent : justificatif, portefeuille ou passerelle | — |
| Règlement natif (x402, MPP) | Micropaiements de services, portefeuille dédié et plafonné | Contrepartie connue et volume élevé : contrat et facturation classiques |
| Mandats à l'exécution | Usage unique, liaison au contexte, versement à la piste d'audit | — |
| Achat interentreprises | Approbation dans l'orchestration, prix dans le système d'enregistrement, mandat après rapprochement à trois voies (chapitre 45) | Achats hors contrat sous un seuil : traitement de type détail |
| Dépendance à un protocole | Aucun engagement exclusif; versions épinglées | Protocole stabilisé et passé sous gouvernance neutre |

---

## Points à retenir

- Un agent prouve son droit d'acheter par un mandat signé qui lie un utilisateur, un panier et un paiement, non par son identité.
- AP2 et Verifiable Intent convergent sur la forme : des SD-JWT, des contraintes signées par l'utilisateur, une action signée par l'agent, une vérification en code déterministe.
- Aucun protocole ne couvre un achat de bout en bout. Les couches s'emboîtent; à l'intérieur de chacune, deux propositions ou plus se doublent.
- ACP et UCP laissent au marchand la relation client et l'exécution. Ils diffèrent par le périmètre, la découverte et la gouvernance.
- Les réseaux de cartes ajoutent la reconnaissance de l'agent et des justificatifs limités, par des schémas propriétaires sans standard commun.
- x402 et MPP placent le paiement dans l'échange HTTP. Le plafond de dépense doit venir d'ailleurs.
- Les analyses de sécurité, en prépublication, concluent que les garanties sont implicites et que les failles tiennent au protocole, non au modèle.
- Litiges, responsabilité et approvisionnement interentreprises restent hors du champ des spécifications.

---

## Sources

Pages primaires lues le 11 novembre 2026; [1], [3], [6], [7], [10] et [12] relues le 12 novembre :

1. [AP2 — spécification v0.2](https://ap2-protocol.org/ap2/specification/)
2. [UCP — page d'accueil](https://ucp.dev/)
3. [UCP — vue d'ensemble de la spécification](https://ucp.dev/latest/specification/overview/) — lue à l'audit, hormis la toute fin.
4. [UCP et AP2](https://ucp.dev/documentation/ucp-and-ap2/)
5. [Agentic Commerce Protocol — site](https://www.agenticcommerce.dev/)
6. [Agentic Commerce Protocol — dépôt](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol)
7. [Verifiable Intent](https://verifiableintent.dev/)
8. [Visa — Trusted Agent Protocol, aperçu](https://developer.visa.com/capabilities/trusted-agent-protocol/overview)
9. [x402 — introduction](https://docs.x402.org/introduction)
10. [x402 — README du dépôt d'origine](https://github.com/coinbase/x402), copie de développement de `x402-foundation/x402`.
11. [Machine Payments Protocol — aperçu](https://mpp.dev/overview)
12. [AAIF — « How does agentic commerce work », 20 août 2026](https://aaif.io/blog/how-does-agentic-commerce-work) — primaire pour le groupe de travail de l'AAIF, secondaire pour les protocoles décrits.

Prépublications, résumé lu seulement :

13. [A Formal Analysis of Agent Payment Protocols (arXiv 2609.00060)](https://arxiv.org/abs/2609.00060)
14. [SoK: Security of Autonomous LLM Agents in Agentic Commerce (arXiv 2604.15367)](https://arxiv.org/abs/2604.15367)
15. [Protocol-Level Attacks on Agentic Commerce Platforms (arXiv 2607.21824)](https://arxiv.org/abs/2607.21824)
16. [Zero-Trust Runtime Verification for Agentic Payment Protocols (arXiv 2602.06345)](https://arxiv.org/abs/2602.06345)

Sources secondaires :

17. [Inriver — « Why B2B agentic commerce can't run on retail protocols », septembre 2026](https://www.inriver.com/resources/b2b-agentic-commerce-retail-protocols/) — billet de fournisseur, lu.
18. [Mastercard Agent Pay](https://www.mastercard.com/us/en/business/artificial-intelligence/mastercard-agent-pay.html) et [Mastercard — Verifiable Intent](https://www.mastercard.com/us/en/news-and-trends/stories/2026/verifiable-intent.html) — pages non lues (accès refusé), connues par un résumé de moteur de recherche.
19. Prépublications repérées par recherche, non lues : [arXiv 2608.23858](https://arxiv.org/abs/2608.23858) (AP2), [arXiv 2605.11781](https://arxiv.org/abs/2605.11781) (x402), [arXiv 2609.11757](https://arxiv.org/abs/2609.11757) (AP2).

## Limites de ce chapitre

- Les quatre articles de sécurité, lus en résumé, ne sont pas évalués par les pairs d'après leur page arXiv.
- Pages de Mastercard inaccessibles : le nom d'Agent Pay vient de la table des matières, son lien avec Verifiable Intent d'un résumé de recherche.
- L'attribution d'AP2 à Google repose sur l'avis de droit d'auteur de la page et sur le billet de l'AAIF.
- La vue d'ensemble d'UCP, relue à l'audit hormis sa toute fin, lève la réserve sur l'architecture de paiement; l'organe de gouvernance qu'elle cite n'est pas nommé. Pour Visa, seule la page d'aperçu a été lue.
- Pour x402, ni la version du protocole, ni la liste des réseaux, ni les statuts de la fondation n'ont été établis; le dépôt de la fondation n'a pas été lu. Pour MPP, le brouillon de l'IETF n'a pas été lu.
- Le recentrage d'OpenAI en mars 2026 est rapporté par deux billets, non vérifié auprès d'OpenAI.
- La section 10.8 repose sur un billet de fournisseur et sur le chapitre 45. Ses orientations sont un raisonnement, non un résultat de source.
- Aucune donnée d'adoption ni de fraude n'est citée. Deux articles de la carte thématique (paiements entre agents sur chaîne de blocs, TessPay) n'ont pas été lus.
