# Chapitre 8 — Découverte et registres

*Question directrice : comment un agent trouve-t-il un outil ou un pair, et pourquoi lui faire confiance ?*

> **État de référence :** registre MCP en préversion (API `v0.1`), spécification A2A 1.0, proposition ARD v0.91 du 26 août 2026, AGNTCY Agent Directory v1.0 du 19 février 2026, documentation d'AWS, de Microsoft, de MuleSoft et d'Apigee consultée le 11 novembre 2026. Les numéros entre crochets renvoient aux sources en fin de chapitre; toutes sont des pages lues pour ce chapitre, [22] étant un communiqué d'éditeur; [23] à [27] ont été ajoutées le 14 novembre 2026, dont [23], [26] et [27] par leur seul résumé.

Un protocole dit comment parler à un outil ou à un agent. Il ne dit pas lequel existe, où il se trouve, ni s'il mérite d'être appelé. Tant que le parc tient en dix serveurs, une liste dans un fichier de configuration suffit. Au-delà, il faut un mécanisme de découverte, et les candidats se multiplient : registre central, fichiers publiés sous `/.well-known`, annuaire pair-à-pair, catalogues de plateformes.

La thèse de ce chapitre tient en une phrase : les mécanismes ouverts répondent à « où est-ce ? » et à « qui le publie ? », aucun ne répond à « est-ce approuvé ? ». Cette troisième question revient à l'entreprise, et le registre interne est l'endroit où elle se tranche. La découverte est un problème technique en voie de normalisation; la confiance reste une décision de gouvernance.

---

## 8.1 Le problème : trouver, décrire, authentifier

Découvrir une capacité suppose trois opérations distinctes.

**Trouver**, c'est obtenir une adresse à partir d'un besoin ou d'un nom. La recherche peut partir d'un identifiant connu, d'un domaine (« que propose cet éditeur ? ») ou d'une intention exprimée en langage naturel (« un outil qui réserve des vols »).

**Décrire**, c'est savoir ce que fait la capacité et comment s'y brancher : transport, version de protocole, schéma d'authentification, compétences annoncées. Une partie de cette description est statique et peut être publiée à l'avance. Une autre ne l'est pas : les outils qu'un serveur MCP expose varient selon l'utilisateur authentifié, la configuration ou l'état du déploiement. C'est pour cette raison que les Server Cards de MCP excluent délibérément la liste des outils, laissée à l'interrogation en direct [5].

**Authentifier**, c'est établir qui publie la description et vérifier qu'elle n'a pas été altérée. Les mécanismes étudiés ici le font de trois façons : preuve de contrôle d'un espace de noms, signature de la description, empreinte cryptographique du contenu.

Il manque une quatrième opération, que ces mécanismes ne prennent pas en charge : **approuver**. Savoir qu'un serveur vient bien de l'éditeur annoncé ne dit rien de la qualité de son code, des données qu'il touche ni de la pertinence de l'autoriser dans un contexte donné.

Deux circonstances de découverte sont à distinguer. À la conception, une personne cherche un outil et le configure dans un hôte; elle peut lire, comparer, demander un avis. À l'exécution, c'est un agent qui interroge un registre et choisit sur la foi d'une description. Ce second cas change la nature du risque : la description devient une entrée non fiable injectée dans le raisonnement du modèle (chapitre 31). La proposition ARD le formule en règle : un score de pertinence renvoyé par une recherche ne doit pas être interprété comme un jugement de confiance, de conformité ou de sûreté [11].

---

## 8.2 Trois modèles : centralisé, fédéré, distribué

Le relevé de référence sur le sujet compare cinq solutions — registre MCP, Agent Cards d'A2A, AGNTCY Agent Directory Service, Microsoft Entra Agent ID et NANDA Index AgentFacts — selon quatre axes : sécurité, authentification, mise à l'échelle et maintenabilité [14]. Son titre oppose les approches centralisées, d'entreprise et distribuées. Ce chapitre retient un découpage voisin, fondé sur l'endroit où réside l'index.

![Trois modèles de découverte, distingués par l'endroit où réside l'index : un dépôt unique, des registres qui indexent ce que chaque domaine publie et se renvoient les requêtes, ou un réseau pair-à-pair sans opérateur central. Ce découpage est celui que retient le chapitre, voisin de celui du relevé de référence.](figures/fig-08-e1.svg)

| Modèle | Où réside l'index | Exemples | Force | Limite |
|---|---|---|---|---|
| Centralisé | Un dépôt unique, public ou interne | Registre MCP officiel; catalogues d'entreprise | Simplicité, point de contrôle unique | Point de défaillance et de pouvoir unique |
| Fédéré | Chaque domaine publie; des registres indexent et se renvoient les requêtes | Fichiers `/.well-known`, sous-registres MCP, services de découverte ARD | Autonomie des éditeurs, pluralité des index | Confiance à établir registre par registre |
| Distribué | Un réseau pair-à-pair sans opérateur central | AGNTCY Agent Directory, NANDA | Résilience, intégrité vérifiable | Complexité d'exploitation, retrait difficile |

Le relevé [14] est une prépublication qualitative, sans mesure expérimentale. Plusieurs de ses auteurs sont affiliés à Cisco et au MIT, à l'origine de deux des cinq solutions comparées, et il décrit un état antérieur des spécifications.

Sa recommandation la plus durable est de séparer la résolution d'identité, qui doit être stable, des métadonnées de capacités, qui changent souvent [14]. Les spécifications récentes vont dans ce sens.

Les trois modèles ne s'excluent pas. Une entreprise combine en pratique un registre interne centralisé, des fichiers `/.well-known` pour ce qu'elle expose à l'extérieur et, plus rarement, une participation à un réseau distribué.

---

## 8.3 Le registre MCP : `server.json`, espaces de noms vérifiés

Le chapitre 5 (section 5.7) a présenté le registre officiel : un dépôt central de métadonnées, en préversion, qui exclut les serveurs privés [1]. Son fonctionnement sert de gabarit aux registres internes.

### L'enregistrement

Chaque serveur est décrit par un fichier `server.json` : un nom unique, l'emplacement du serveur (paquet ou URL distante), des instructions d'exécution et des données de découverte [1]. Le registre ne contient que ce pointeur; le code reste dans npm, PyPI ou un registre d'images.

### La preuve de l'espace de noms

Le nom détermine la méthode d'authentification, et inversement [2]. Un nom de la forme `io.github.utilisateur/*` exige une authentification par GitHub. Un nom fondé sur un domaine, comme `com.example/*`, exige la preuve du contrôle de ce domaine, apportée de deux façons : un enregistrement DNS de type TXT qui porte une clé publique (`v=MCPv1; k=ed25519; p=…`), ou un fichier servi à `/.well-known/mcp-registry-auth`. L'éditeur signe ensuite sa publication avec la clé privée correspondante.

Cette preuve établit une chose : celui qui publie sous `com.example` contrôle `example.com`. Elle n'établit rien d'autre.

### Ce que le registre ne promet pas

La politique de modération est explicite : les consommateurs doivent présumer une modération minimale ou nulle [4]. Sont retirés les contenus illégaux, les maliciels, le pourriel et les serveurs qui ne fonctionnent pas. Ne sont **pas** retirés les serveurs de mauvaise qualité ni ceux qui présentent des vulnérabilités de sécurité. Un retrait prend la forme d'un statut `deleted`; la métadonnée reste accessible par l'API. La section 8.8 mesure ce que cette politique laisse passer.

Le registre ne garantit ni sa disponibilité ni la durabilité de ses données [3]. Les métadonnées d'une version sont immuables, à l'exception du champ `status`, qui peut passer à `deprecated` ou à `deleted`.

### Une chaîne à trois maillons

Le registre officiel n'est pas fait pour être interrogé par les applications hôtes [1]. Il alimente des agrégateurs, qui copient ses données par une API REST en lecture seule (`GET /v0.1/servers`, avec pagination par curseur et filtre `updated_since`), à une cadence de l'ordre d'une fois l'heure [3]. Un agrégateur qui met en œuvre la même spécification OpenAPI devient un **sous-registre** : les hôtes l'interrogent par une interface standard, et il peut enrichir chaque enregistrement de ses propres métadonnées sous une clé `_meta` — évaluations, nombre de téléchargements, résultats d'analyse de sécurité.

La curation se fait donc en aval, par conception, avec deux conséquences pour l'entreprise. Un registre interne qui met en œuvre cette interface est consultable par les hôtes compatibles sans adaptation; la base de code du registre officiel n'est toutefois pas prévue pour l'autohébergement [1]. Et c'est au sous-registre interne de porter le statut d'approbation que le registre public ne porte pas.

### Les Server Cards

Le registre décrit des entrées publiées par leur éditeur. L'extension Server Cards, au stade bêta [6], permet à un serveur distant de se décrire lui-même par un document statique : identité, points d'accès, versions de protocole prises en charge. L'emplacement recommandé est `<url-du-serveur>/server-card` [5]. La carte est indicative : si elle contredit la réponse en direct de `server/discover`, le client devrait se fier à cette dernière. Elle ne doit contenir ni identifiants ni topologie interne, puisqu'elle est publique.

---

## 8.4 Découverte par `/.well-known`

Le second modèle renverse la logique : au lieu de s'inscrire dans un dépôt, chaque domaine publie sa propre description à un emplacement convenu, selon le principe des URI bien connues (RFC 8615).

### Les Agent Cards d'A2A

Un agent A2A se décrit par une Agent Card (chapitre 6). La spécification 1.0 enregistre le chemin `/.well-known/agent-card.json`, qui doit renvoyer la carte [8]. La documentation distingue trois stratégies de découverte : l'URI bien connue (agents publics), les registres organisés (entreprise, places de marché) et la configuration directe (relations statiques) [7].

**A2A ne définit pas d'API de registre.** La documentation le dit expressément et précise que la question est à l'étude dans la communauté [7]. Chaque catalogue d'entreprise a donc sa propre interface.

**La signature est facultative.** Une carte peut être signée en JWS après canonicalisation; un client devrait vérifier au moins une signature avant de se fier à une carte, et ne doit pas utiliser une clé expirée ou révoquée [8]. Ce sont un « peut » et un « devrait » : une carte non signée est conforme.

**Une carte publique ne doit pas tout dire.** Pour les informations sensibles, la documentation recommande la carte étendue, servie seulement à un client authentifié, et la protection du point d'accès par mTLS, restriction réseau ou OAuth [7].

### Le catalogue de domaine : deux spécifications en mouvement

Une Agent Card décrit un agent. Reste à énumérer tout ce qu'un domaine propose : agents, serveurs MCP, compétences. Deux travaux s'y emploient, et ils ne s'accordent pas encore sur le nom du fichier.

**AI Catalog** définit un conteneur JSON typé et imbricable, dont chaque entrée désigne un artefact par son type de média et le référence par URL ou l'inclut directement [9]. Le fichier se publie à `/.well-known/ai-catalog.json` [10]. Le travail est mené par l'Agent Card Working Group sous l'égide de la Linux Foundation, dans un dépôt qualifié de temporaire; la spécification n'est pas finalisée, et son adoption dépendra d'un vote des comités directeurs d'A2A et de MCP [9]. Elle ne remplace pas les formats propres à chaque protocole. Elle prévoit des Trust Manifests facultatifs, signés indépendamment, pour authentifier versions, attestations et provenance, ainsi qu'un profil `did:web` pour l'identité des éditeurs. Du côté de MCP, la proposition qui institue les Server Cards s'appuie sur ce catalogue pour la découverte à l'échelle d'un domaine [5].

**Agentic Resource Discovery (ARD)** ajoute la couche de recherche. Sa version 0.91, au statut de proposition et datée du 26 août 2026, définit un manifeste d'entrées publié à `/.well-known/ard.json` et une interface de registre : une recherche en langage naturel obligatoire (`POST /search`), une exploration par facettes et une liste, toutes deux facultatives [11]. Elle traite `/.well-known/ai-catalog.json` comme le chemin de son prédécesseur : un consommateur peut le consulter par courtoisie, et un éditeur devrait migrer. Sa page d'accueil affirme pourtant qu'ARD ne remplace ni MCP, ni A2A, ni AI Catalog, et qu'il existera de nombreux services de découverte, y compris internes aux entreprises [12].

ARD précise la fédération en trois modes : le registre interroge ses pairs et fusionne les résultats, il renvoie des références que le client choisit de suivre, ou il se limite à son index local [11]. Côté confiance, une règle ferme : le domaine de confiance cryptographique déclaré dans le manifeste doit correspondre au domaine de l'éditeur présent dans l'identifiant.

L'état des lieux est donc celui d'une convergence inachevée. Les deux textes partagent le modèle d'entrée et les types de média, mais le chemin canonique diffère selon la page lue. Le projet IEEE P3931, autorisé en 2026 sur la description, la découverte et les registres d'agents, s'y ajoute et donnera au mieux un texte en 2027 (chapitre 11). Coder en dur l'un ou l'autre chemin est prématuré.

### Ce que prouve un fichier `/.well-known`

Un tel fichier prouve que son contenu est servi par le domaine, rien de plus. Qui compromet le serveur web contrôle le catalogue; une signature dont la clé est publiée sur le même domaine n'ajoute alors aucune protection. Ce constat est une déduction; il explique pourquoi les deux spécifications prévoient des manifestes signés indépendamment.

---

## 8.5 AGNTCY : l'adressage par contenu

Le troisième modèle supprime l'opérateur central. L'Agent Directory d'AGNTCY, publié en version 1.0 le 19 février 2026 sous licence Apache 2.0, est un annuaire distribué où les agents annoncent leurs capacités [13]. Le relevé [14] le désigne sous le nom d'Agent Directory Service (ADS). AGNTCY dans son ensemble est traité au chapitre 7.

Quatre choix de conception le caractérisent [13].

- **Un schéma commun.** Les enregistrements suivent l'Open Agentic Schema Framework (OASF), qui décrit un agent par des compétences hiérarchisées, des domaines et des modules d'extension, dont A2A et MCP.
- **Un identifiant dérivé du contenu.** Chaque enregistrement est nommé par un identifiant de contenu (CID), une empreinte cryptographique. Toute modification produit un identifiant différent.
- **Un stockage standard.** Les enregistrements sont des artefacts OCI; tout serveur conforme à la spécification de distribution OCI peut participer.
- **Une découverte en deux temps.** Une table de hachage distribuée (Kad-DHT de libp2p) associe d'abord une capacité à des identifiants, puis un identifiant aux serveurs qui l'hébergent.

Les enregistrements peuvent être signés, et un nom de domaine vérifiable peut être associé à un identifiant. Une organisation peut exploiter ses propres nœuds et les relier à d'autres, l'authentification entre organisations reposant sur SPIFFE/SPIRE. Le billet de lancement range encore parmi les travaux en cours les performances de la table distribuée et les politiques de vérification de la chaîne de confiance.

L'adressage par contenu apporte une propriété que les deux autres modèles n'ont pas : l'**intégrité par construction**. Référencer un enregistrement par son empreinte, c'est épingler une version exacte, qu'aucun intermédiaire ne peut modifier sans que cela se voie. Il ne dit en revanche ni qui a publié — c'est le rôle de la signature — ni si le contenu est digne de confiance. Et il complique le retrait : un contenu immuable, répliqué sur des nœuds indépendants, ne se supprime pas par une décision centrale. Ce dernier point est une déduction.

Pour une entreprise, ce modèle se justifie surtout dans un écosystème entre organisations où aucun participant ne peut ou ne veut tenir l'index. À l'intérieur d'un périmètre unique, un registre centralisé offre le même service à moindre coût d'exploitation. Entre partenaires qui échangent des données, l'espace de données offre une autre voie : le connecteur EDC (Eclipse Dataspace Components) produit son catalogue selon les justificatifs présentés (chapitre 45).

---

## 8.6 Catalogues d'entreprise

Le tableau résume ce que la documentation des éditeurs de plateformes décrit au 11 novembre 2026.

| Catalogue | Ce qu'il recense | Alimentation | Contrôle |
|---|---|---|---|
| AWS Agent Registry [15][16] | Serveurs MCP, agents (carte A2A), compétences, ressources personnalisées | Publication, synchronisation depuis une URL, détection automatique des ressources AgentCore dans AWS Organizations | Approbation manuelle ou automatique; dépréciation |
| Registre de Microsoft Agent 365 [18][19] | Agents Microsoft, de partenaires, publiés par l'organisation, partagés par leur créateur | Plateformes Microsoft, téléversement d'un manifeste | Blocage, suppression, signaux de risque; identité gérée dans Entra |
| MuleSoft Agent Registry [20][22] | Agents, serveurs MCP, modèles | Publication dans Anypoint Exchange; scanners de plateformes tierces | Agents et serveurs MCP : politiques inapplicables via passerelle tierce (octobre 2026; chapitre 27) |
| Apigee API hub [21] | API, dont MCP comme style d'API; attribut de type Code, Model, Agent ou Skill | Synchronisation des métadonnées de serveurs et d'outils MCP (préversion) | Celui du catalogue d'API existant |

**AWS Agent Registry** est le plus explicite sur le cycle de vie. Un éditeur prépare un enregistrement à l'état de brouillon, le soumet; un curateur l'approuve ou le rejette, et peut plus tard le déprécier pour le retirer de la découverte [15]. Seuls les enregistrements approuvés sont visibles des consommateurs, humains ou agents. La recherche combine sémantique et mots-clés, et chaque registre expose un point d'accès MCP, de sorte qu'un client MCP peut y chercher sans SDK propre à AWS [16]. L'accès se règle par IAM ou par jeton JWT d'un fournisseur d'identité d'entreprise. La soumission déclenche un événement qui peut lancer un pipeline de revue existant. Le service est lancé sous un nouvel espace de noms, `agent-registry`; celui de la préversion publique n'est plus pris en charge depuis le 30 octobre 2026.

La même documentation formule deux mises en garde. Le registre valide un enregistrement contre le schéma MCP ou A2A, mais ne vérifie ni les paquets, ni les dépôts, ni les points d'accès référencés : c'est au consommateur de le faire, par listes d'autorisation et épinglage de versions [17]. Et l'approbation automatique, prévue pour le développement, exige des contrôles compensatoires [16].

**Microsoft** a réparti les rôles : Agent 365 devient le registre et le plan de contrôle unifiés, Entra conserve l'identité des agents et les politiques d'accès [18]. L'inventaire complet, y compris les agents dépourvus d'identité Entra, se consulte dans le centre d'administration Microsoft 365. Deux compteurs y traduisent des préoccupations de gouvernance : les agents sans propriétaire, dont le créateur a quitté l'organisation, et les agents non gérés, créés hors d'Agent 365 [19]. Le chapitre 29 traite l'identité, le chapitre 26 la plateforme.

**MuleSoft** mise sur la détection. Ses scanners parcourent d'autres plateformes — Amazon Bedrock, Google Vertex AI et Microsoft Azure Copilot (janvier 2026), puis les agents de ServiceNow et les serveurs MCP de Kong Gateway (octobre) — et inscrivent au registre ce qu'ils trouvent [20]. Le communiqué de janvier 2026 précise que les métadonnées sont normalisées selon le format de carte A2A [22]. Les notes de version lues n'attribuent pas de statut de disponibilité à chaque fonction.

**Apigee API hub** prolonge le catalogue d'API : MCP y figure comme style d'API depuis octobre 2025, de premier rang depuis décembre 2025, et le serveur MCP d'API hub est en disponibilité générale depuis le 24 juillet 2026 [21]. Les notes lues ne mentionnent pas A2A.

Deux logiques d'alimentation se dégagent : la **déclaration**, où l'éditeur soumet son enregistrement, et la **détection**, où le registre va chercher ce qui existe. La première produit des enregistrements de qualité mais ignore ce qui n'a pas été déclaré. La seconde révèle les agents créés hors processus, sans rien dire de leur légitimité. Un inventaire fiable exige les deux (chapitre 39).

Chaque catalogue voit mieux son propre écosystème que celui des autres. Une entreprise multi-plateformes aura donc plusieurs registres, dont la fédération est l'objet du chapitre 27.

---

## 8.7 Le registre comme point de gouvernance

Aucun des mécanismes ouverts ne décide : espace de noms authentifié, carte signée ou contenu adressé par empreinte, la preuve porte sur l'origine ou l'intégrité, jamais sur l'acceptabilité. Le registre interne est l'endroit où l'entreprise ajoute cette décision. Trois conditions en font un point de gouvernance plutôt qu'un simple annuaire.

**Un cycle de vie explicite.** Les états observés convergent : brouillon, soumis, approuvé ou rejeté, déprécié, retiré [3][15]. Chaque transition a un responsable. Les critères d'approbation relèvent de l'entreprise; une liste minimale, proposée ici à titre de suggestion, comprend un propriétaire nommé, une provenance vérifiée, une version épinglée, la classe de données touchées et la nature des actions permises. Une approbation vaut pour une version : un serveur peut modifier ses descriptions après coup, d'où une nouvelle approbation à tout changement de définition (chapitre 31).

**Un propriétaire pour chaque entrée.** Le compteur d'agents sans propriétaire de Microsoft [19] désigne un risque général : une capacité que personne ne maintient reste découvrable. Le départ d'un propriétaire devrait déclencher une réattribution ou une dépréciation.

**Une application effective.** Un registre que l'on peut contourner n'est qu'une documentation. L'approbation ne vaut que si la passerelle refuse les appels vers ce qui n'est pas inscrit (chapitre 24) et si l'identité de l'agent appelant est vérifiée (chapitre 29). La dépréciation doit se propager de la même façon : retirer une entrée de la recherche ne coupe pas les connexions déjà configurées.

Un agent qui cherche un outil à l'exécution ne devrait voir que les enregistrements approuvés, et ce qu'il y lit reste une donnée à valider avant toute installation ou connexion [17]. La recherche dans le registre contribue par ailleurs à l'économie de contexte : interroger au besoin évite de charger d'avance tout le catalogue (chapitre 13).

---

## 8.8 Ce que mesurent les études de l'écosystème

Les sections précédentes décrivent des mécanismes. Cinq études récentes mesurent ce qui circule réellement dans les registres et les places de marché publics. Aucune ne porte sur un registre interne.

### Des catalogues gonflés

Une campagne de quatorze jours sur six places de marché a relevé près de 17 000 entrées de serveurs, dont un peu moins de la moitié sont des projets valides. Le reste est fait de dépôts vides, de gabarits, de copies inactives et de projets abandonnés [25]. Parmi les serveurs valides, 40,9 % ont été mis à jour dans les 90 jours, et 21,9 % sont inactifs depuis plus d'un an. Le nombre d'entrées d'un catalogue ne dit donc rien de l'offre utilisable.

### Des identités qui se détournent

Une étude de 67 057 serveurs dans six registres montre que le lien entre une entrée et son éditeur n'est pas entretenu [24]. Les registres étudiés ne vérifient ni les liens soumis ni leur propriétaire, et ne mettent pas leurs fiches à jour quand un compte change. Deux détournements en découlent. Quand le compte GitHub d'un mainteneur est supprimé, son nom redevient disponible après 90 jours, et quiconque le reprend hérite de l'entrée. Quand le compte est renommé, l'ancien nom devient lui aussi réclamable. Les auteurs comptent, dans quatre registres, 304 serveurs exposés au détournement par redirection et 212 comptes GitHub réenregistrables; le total de 516 cas est une somme faite ici, absente du texte relu. Sur npm, 80,6 % de 408 groupes de noms voisins sont tenus par des développeurs différents. S'y ajoutent des justificatifs laissés dans des exemples de configuration : neuf jetons d'accès GitHub, dont cinq encore valides.

### Des entrées qui changent sous le même nom

Le recensement le plus proche du sujet de ce chapitre porte sur le registre public de MCP lui-même : 21 643 serveurs et 72 606 enregistrements de version, relevés en août 2026 [23]. D'après son résumé, 51,1 % des serveurs à plusieurs versions ont changé ce qu'ils annoncent d'une version à l'autre, 40,6 % l'ont fait sans le signaler, et 4,2 % ont redirigé leur point d'accès distant vers un autre hôte en gardant la même identité au registre. Le protocole ne signale pas ce dernier changement aux clients déjà installés. Cette dérive silencieuse va de pair avec des chances presque trois fois plus élevées de constat de gravité élevée (rapport de cotes de 2,96). La popularité protège peu : le nombre d'étoiles d'un dépôt est un mauvais indicateur de sûreté.

### Des défauts fréquents, des scanners peu fiables

L'étude porte sur 1 899 serveurs à code ouvert; son résumé rapporte 7,2 % de vulnérabilités générales et 5,5 % d'empoisonnement d'outil propre à MCP, mais le texte les tire de sous-échantillons (583 dépôts pour l'analyse statique, 83 pour le balayage propre à MCP), et ses auteurs demandent un balayage de sécurité automatisé dans les registres [26]. Le recensement du registre public observe, sur les 14 353 serveurs dont le code a pu être balayé (66 % du registre) et après correction par la précision de son scanner (0,56), environ 7,6 % de constats de gravité élevée [23]. L'instrument lui-même est toutefois en cause : sur une collection de 64 611 serveurs, dont 37 288 ont pu être sondés, les scanners existants en signalent 96,89 % comme risqués, et moins de la moitié des alertes vérifiées à la main sont fondées [27].

### Ce que ces mesures changent

Elles donnent un contenu aux critères d'approbation de la section 8.7.

| Constat mesuré | Conséquence pour le registre interne |
|---|---|
| La moitié des entrées des places de marché sont sans valeur [25] | Sélectionner, non refléter |
| Une entrée peut changer de mains sans changer de nom [24] | Vérifier le propriétaire à l'inscription, puis périodiquement |
| Un serveur change ce qu'il annonce, ou son hôte, sous la même identité [23] | Épingler la version et le point d'accès; comparer les définitions à chaque synchronisation |
| La popularité protège peu [23] | Ne pas approuver sur le nombre d'étoiles ou de téléchargements |
| Les scanners se contredisent et surestiment [27] | Tenir un résultat de balayage pour un signal de tri, non pour une décision |

La colonne de droite est une lecture de ce chapitre. Ces études portent sur des registres publics et sur du code ouvert; la plupart sont des prépublications, et trois ne sont connues ici que par leur résumé.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Source de vérité interne | Un registre interne avec approbation | Registres séparés par environnement ou par unité, s'ils sont fédérés |
| Serveurs MCP publics | Sélection approuvée, tirée d'un sous-registre | Jamais le registre officiel interrogé directement par les hôtes |
| Interface du registre interne | Spécification OpenAPI du registre MCP | Catalogue de plateforme si le parc est homogène |
| Alimentation | Déclaration et détection automatique | Petit parc : déclaration seule |
| Approbation | Manuelle en production | Automatique en développement, avec contrôles compensatoires |
| Référence à une entrée | Version épinglée, empreinte si elle est disponible; nouvelle approbation à tout changement de définition | — |
| Agents exposés à l'extérieur | Agent Card à l'URI bien connue; carte étendue pour le sensible | Agents internes : registre seulement |
| Signature des Agent Cards | Signer et vérifier entre organisations | Échanges internes déjà protégés par mTLS |
| Catalogue de domaine | Attendre la stabilisation; sinon générer `ai-catalog.json` et `ard.json` d'une même source | Découvrabilité externe érigée en objectif d'affaires |
| Découverte par les agents à l'exécution | Limitée aux entrées approuvées; métadonnées tenues pour non fiables | — |
| Annuaire distribué | Veille | Écosystème entre organisations sans opérateur central acceptable |
| Synchronisation depuis un registre public | Comparer les définitions et le point d'accès à la version approuvée; tout écart suspend l'entrée | — |

---

## Points à retenir

- Découvrir comporte trois opérations — trouver, décrire, authentifier — et en laisse une quatrième à l'entreprise : approuver.
- Le registre MCP prouve qui contrôle un espace de noms. Sa politique déclare une modération minimale et ne retire pas les serveurs vulnérables; la curation est confiée aux sous-registres.
- A2A enregistre le chemin `/.well-known/agent-card.json`, mais ne définit pas d'API de registre, et la signature des cartes y est facultative.
- Le catalogue de domaine n'est pas stabilisé : AI Catalog publie `ai-catalog.json`, la proposition ARD v0.91 retient `ard.json`.
- Un score de pertinence n'est pas un jugement de confiance. La règle vaut pour toute recherche faite par un agent.
- L'adressage par contenu d'AGNTCY garantit l'intégrité d'un enregistrement, pas son auteur ni sa qualité.
- Les catalogues d'entreprise se distinguent par leur alimentation : déclaration, détection, ou les deux. AWS, le plus explicite, ne vérifie pas ce que ses enregistrements référencent.
- Un registre ne gouverne que s'il a un cycle de vie, un propriétaire par entrée et une passerelle qui applique ses décisions. Une approbation vaut pour une version, pas pour un serveur.
- Les mesures de l'écosystème public justifient l'approbation : la moitié des entrées des places de marché sont sans valeur, des entrées changent de mains ou de contenu sous le même nom, et les scanners se contredisent.

---

## Sources

Pages lues le 11 novembre 2026 :

1. [Le registre MCP](https://modelcontextprotocol.io/registry/about)
2. [Registre MCP — authentification à la publication](https://modelcontextprotocol.io/registry/authentication.md)
3. [Registre MCP — agrégateurs et sous-registres](https://modelcontextprotocol.io/registry/registry-aggregators.md)
4. [Registre MCP — politique de modération](https://modelcontextprotocol.io/registry/moderation-policy.md)
5. [SEP-2127 — MCP Server Cards](https://modelcontextprotocol.io/seps/2127-mcp-server-cards.md)
6. [MCP — vue d'ensemble des extensions](https://modelcontextprotocol.io/extensions/overview.md)
7. [A2A — découverte des agents](https://a2a-protocol.org/latest/topics/agent-discovery/)
8. [A2A — spécification 1.0, sections 8 et 14.3](https://a2a-protocol.org/latest/specification/)
9. [AI Catalog — dépôt de travail](https://github.com/Agent-Card/ai-catalog)
10. [AI Catalog — site](https://ai-catalog.io)
11. [ARD — spécification v0.91](https://agenticresourcediscovery.org/spec/)
12. [ARD — page d'accueil](https://agenticresourcediscovery.org)
13. [AGNTCY — Directory v1](https://blogs.agntcy.org/technical/2026/02/19/dir-v1.html)
14. [Evolution of AI Agent Registry Solutions (arXiv 2508.03095, v3)](https://arxiv.org/abs/2508.03095)
15. [AWS Agent Registry — concepts](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-concepts.html)
16. [AWS Agent Registry — capacités](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-key-capabilities.html)
17. [AWS Agent Registry — protection des données](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-data-protection.html)
18. [Microsoft — convergence du registre d'agents vers Agent 365](https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence)
19. [Microsoft — registre d'agents du centre d'administration](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry)
20. [MuleSoft Agent Fabric — notes de version](https://docs.mulesoft.com/general/agent-fabric-release-notes)
21. [Apigee API hub — notes de version](https://docs.cloud.google.com/apigee/docs/apihub/release-notes)

Communiqué d'éditeur :

22. [Salesforce — découverte automatisée dans MuleSoft Agent Fabric (22 janvier 2026)](https://www.salesforce.com/news/stories/mulesoft-agent-fabric-automated-agent-discovery/)

Études de mesure, lues le 14 novembre 2026 pour la section 8.8 :

23. [Kraishan — Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem (arXiv 2609.14119, 12 septembre 2026)](https://arxiv.org/abs/2609.14119) — prépublication, un seul auteur; résumé seulement.
24. [Li et Gao — Toward Understanding Security Issues in the Model Context Protocol Ecosystem (arXiv 2510.16558, version 1 du 18 octobre 2025)](https://arxiv.org/html/2510.16558v1) — prépublication.
25. [Guo et coll. — A Measurement Study of Model Context Protocol (arXiv 2509.25292, version 1 du 29 septembre 2025)](https://arxiv.org/html/2509.25292v1) — prépublication.
26. [Hasan et coll. — Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers (arXiv 2506.13538, version 5 du 13 avril 2026)](https://arxiv.org/abs/2506.13538) — résumé seulement.
27. [Chen et coll. — Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability (arXiv 2607.11086, 13 juillet 2026)](https://arxiv.org/abs/2607.11086) — prépublication; résumé seulement.

## Limites de ce chapitre

- Les sources [23], [26] et [27], d'abord connues par leur seul résumé, ont été relues au-delà du résumé le 14 novembre 2026, par un outil qui en rend des extraits; les écarts relevés sont corrigés dans le texte.
- Plusieurs pages longues ([8], [11], [13], [14], [20], [21]) ont été lues par un outil d'extraction qui les condense; les formulations normatives rapportées ne sont pas des citations.
- L'audit du 12 novembre 2026 a relu [1], [3], [6], [11], [16], [18], [20], [21] et le résumé de [14].
- La relation entre AI Catalog et ARD reste ambiguë : la spécification ARD parle d'un prédécesseur, sa page d'accueil d'une coexistence.
- NANDA n'est connu que par le relevé [14], cosigné par ses concepteurs. Entra Agent ID n'est abordé que par la page de convergence, et le schéma détaillé des Server Cards n'a pas été lu.
- La documentation d'AWS n'emploie pas le terme « disponibilité générale » dans les pages lues. Chez MuleSoft, la normalisation au format de carte A2A ne repose que sur le communiqué [22].
- Les remarques sur la compromission d'un domaine (8.4) et sur le retrait dans un réseau distribué (8.5), ainsi que les critères d'approbation (8.7), sont des raisonnements de ce chapitre.
- Les seules données chiffrées sur l'écosystème sont celles de la section 8.8, ajoutée le 14 novembre 2026. [23], [26] et [27] n'y sont connus que par leur résumé; [24] et [25] ont été lus par l'outil d'extraction. Le résumé de [23] ne dit pas si les 40,6 % se rapportent à tous les serveurs à plusieurs versions ou à ceux qui ont changé. [25] donne des décomptes différents dans son résumé et dans ses tableaux; ceux du tableau des serveurs sont retenus. La parution de [26] dans une revue, signalée par un index d'articles, ne figure pas sur la page lue.
- Ces études portent sur des registres et des places de marché publics. Aucune donnée sur des registres internes d'entreprise ni sur leur adoption n'a été trouvée, et la colonne « Conséquence pour le registre interne » est une lecture de ce chapitre.
