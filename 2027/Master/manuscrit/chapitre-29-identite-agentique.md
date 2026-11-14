# Chapitre 29 — Identité agentique

*Question directrice : qui est cet agent, et au nom de qui agit-il ?*

> **État de référence :** brouillon `draft-ietf-wimse-aims-01` du 2 novembre 2026, brouillon ID-JAG révision 06 du 31 octobre 2026, feuille de route MCP du 22 août 2026, documentation Microsoft Entra Agent ID. Les numéros entre crochets renvoient aux sources en fin de chapitre; [1] à [11] et [13] à [15] sont des pages primaires lues pour ce chapitre, [12] est une note de synthèse, lue elle aussi.

Un système d'identité d'entreprise connaît deux populations : des personnes, qui répondent de leurs actes, et des applications, qui exécutent un code écrit d'avance. Un agent n'entre proprement dans aucune des deux cases. C'est un logiciel, mais il choisit ses actions. Il agit souvent pour une personne, mais en son absence. Il peut naître et disparaître en quelques minutes, et confier une partie de sa tâche à un autre agent.

La question directrice en contient donc deux. « Qui est cet agent » appelle un identifiant propre et une preuve cryptographique. « Au nom de qui agit-il » appelle un contexte de délégation qui survit à chaque saut, de l'utilisateur jusqu'au système appelé.

La thèse de ce chapitre : les briques existent, leur assemblage n'est pas normalisé. L'identité de charge de travail répond à la première question, OAuth à la seconde. Le profil qui les compose pour les agents n'existe, au 11 novembre 2026, qu'à l'état de brouillon informatif. Entre-temps, l'entreprise doit retenir une solution transitoire qui ne l'enferme pas.

---

## 29.1 Une nouvelle classe d'identité

### Ce que les modèles existants supposent

La documentation de Microsoft Entra formule le problème par contraste [2]. Une identité d'application, représentée par un *service principal*, a été conçue pour un service construit et entretenu par une organisation : stabilité à long terme, propriétaire connu, cycle de vie géré. Une identité humaine suppose des mécanismes que seule une personne utilise (mot de passe, authentification multifacteur), une boîte aux lettres et une place dans la hiérarchie.

Un agent déroge aux deux. Il est souvent créé par automatisation ou par un utilisateur dans un outil à faible code. Selon la même page, il peut exister quelques minutes pour une tâche, ou être créé et détruit des milliers de fois par jour. Gérer ce rythme avec des identités d'application laisse derrière soi des secrets et des permissions orphelins.

### Trois façons d'agir

La documentation distingue trois modes, qui déterminent le flux d'authentification [1].

| Mode | Identité utilisée | Flux | Risque principal |
|---|---|---|---|
| Agent interactif | Celle de l'agent, avec des permissions déléguées par l'utilisateur présent | *On-behalf-of* (OBO) | L'agent abuse des droits hérités |
| Agent autonome | Celle de l'agent seul | *Client credentials* | L'agent compromis agit sans contrainte |
| Compte utilisateur d'agent | Un compte utilisateur apparié un pour un à l'identité d'agent | Celui d'un utilisateur | L'agent passe pour un collègue de confiance |

Le troisième mode est une concession aux systèmes qui exigent un objet utilisateur : courriel, calendrier, canaux de collaboration. La documentation recommande de n'y recourir que dans ce cas, et précise que ce compte ne remplace pas l'identité d'agent : les deux doivent exister [1].

### Classe nouvelle ou charge de travail ?

Deux lectures s'opposent en apparence. Pour Microsoft, l'agent demande une construction d'identité spécialisée [2]. La Cloud Security Alliance (CSA) va plus loin dans une note de recherche de septembre 2026 : les modèles d'identité non humaine — comptes de service, clés d'API, certificats de charge de travail — n'auraient pas été conçus pour les agents [12].

L'IETF dit l'inverse. Le brouillon « AI Identity Management System » (AIMS), adopté par le groupe WIMSE, intitule une section « Agents are workloads » : un agent est une charge de travail qui itère avec un modèle de langage et un ensemble d'outils, de services et de ressources jusqu'à une condition d'arrêt [3].

Les deux lectures se concilient. Pour s'authentifier, l'agent est une charge de travail, et les mécanismes éprouvés s'appliquent. Il s'en distingue par trois ajouts : un humain responsable, un contexte de délégation à préserver, un cycle de vie assez rapide pour suivre des instances éphémères.

Un agent qui emprunte les identifiants d'un développeur ou un compte de service partagé n'a pas d'identité : selon la CSA, il devient impossible d'attribuer une action à une instance précise [12]. Le brouillon AIMS range les clés d'API statiques parmi les antipatrons [3].

---

## 29.2 Cycle de vie : création, parrainage, retrait

### La prolifération

Microsoft nomme le problème *agent sprawl* : l'expansion non maîtrisée d'agents sans visibilité, gestion ni contrôle de cycle de vie [1]. Trois sources l'alimentent : des unités d'affaires qui créent des agents hors de la supervision des TI, des agents temporaires qui restent en production indéfiniment, des permissions supérieures au besoin et jamais révisées.

### Création : le gabarit et l'instance

Entra sépare le gabarit d'identité d'agent (*agent identity blueprint*) de l'identité d'agent, qui en est une instance [1]. Les règles d'accès conditionnel, les permissions et les contrôles de gouvernance posés sur le gabarit sont hérités par toutes les instances présentes et futures, et une classe entière d'agents peut être désactivée en une opération. Une politique se décide ainsi une fois, par type d'agent, tandis que l'instance reste identifiable individuellement dans les journaux.

Le brouillon AIMS place à la création un second contrôle, l'évaluation de posture [3]. Au moment d'émettre un justificatif, l'émetteur peut tenir compte de preuves d'environnement d'exécution de confiance, de mesures d'intégrité logicielle ou de la provenance de la chaîne d'approvisionnement, et moduler en conséquence le type de justificatif et sa durée. Le texte n'impose aucun mécanisme. Une attestation de cette nature est une preuve, non une politique, et elle se contrefait avec un accès physique au matériel (chapitre 46).

### Parrainage : un humain derrière chaque agent

Une identité d'agent sans responsable humain est un compte orphelin en puissance. Entra exige au moins un parrain (*sponsor*), représentant d'affaires, à la création de toute identité d'agent et de tout gabarit; le propriétaire (*owner*), administrateur technique, est facultatif [13]. Le parrain peut désactiver l'agent, non le réactiver, et certains groupes sont admis comme parrains. Lors d'une création déléguée sans parrain désigné, l'utilisateur appelant le devient [13], comme dans Copilot Studio [2].

Le cas difficile est le départ du parrain. La documentation demande de maintenir le parrainage pour assurer la succession, sans décrire de mécanisme automatique [13], et le registre d'Agent 365 expose un compteur d'agents sans propriétaire, dont le créateur a quitté l'organisation (chapitre 8). Le processus de départ d'un employé doit donc comprendre la réattribution de ses agents, au même titre que la révocation de ses accès.

### Retrait : l'identifiant survit, le justificatif meurt

Le brouillon AIMS sépare le cycle de vie de l'identifiant de celui des justificatifs [3]. Trois règles en découlent.

- Un identifiant retiré **ne doit pas être réattribué** (consigne non normative), pour que journaux et enregistrements de délégation restent interprétables pendant toute la période de conservation.
- Le retrait arrête le renouvellement des justificatifs et, au besoin, signale le changement d'état aux parties qui s'y fient et aux émetteurs de justificatifs dérivés.
- La posture constatée à l'émission ne dure pas d'elle-même. Le texte propose deux remèdes : des durées de vie plus courtes, ou des signaux d'événements qui déclenchent une révocation ou une réduction de portée. À réception d'un tel signal, un jeton ou une décision en cache devenus invalides ne doivent plus servir.

Le cycle de vie comme processus de gouvernance — inventaire, comités, politiques — relève du chapitre 39.

---

## 29.3 Annuaires d'agents

Deux objets sont souvent confondus. Le **registre** décrit ce qu'un agent ou un outil sait faire et où le joindre; il sert à la découverte (chapitre 8). L'**annuaire** dit qui est l'agent, de qui il relève et ce qu'il a le droit de faire; il sert à l'authentification et à la gouvernance. Le premier répond à « que puis-je appeler ? », le second à « qui m'appelle ? ».

Microsoft illustre la séparation : le registre d'agents converge vers Agent 365, tandis qu'Entra conserve l'identité des agents et les politiques d'accès (chapitres 8 et 26). Du côté de l'annuaire, la documentation décrit un inventaire de toutes les identités d'agent, consultable dans le centre d'administration et par Microsoft Graph, qui suit l'agent de l'inscription à la mise hors service [1]. Toute authentification d'un agent y est journalisée comme telle [2].

Le brouillon AIMS ne normalise pas cet objet. L'espace de noms, le registre et la politique de conservation des identifiants sont déclarés propres à chaque déploiement, hors du périmètre du texte [3]. Il n'existe donc pas de schéma d'annuaire d'agents interopérable : chaque plateforme a le sien, et le « système d'enregistrement des agents » de Workday en est un autre exemple (chapitre 26).

Faute de norme, deux sources permettent de dresser un contenu minimal. La CSA recommande un registre interne qui consigne l'identité de l'agent, son propriétaire, les outils permis et les agents avec lesquels il peut échanger [12]. Le brouillon AIMS fixe les champs minimaux d'une piste d'audit : identifiant de l'agent, sujet délégant, ressource, action et décision, horodatage et identifiant de corrélation, état de posture ou de risque, événements de remédiation [3]. Un annuaire utile résout chacun de ces champs, et y ajoute ce que la section 29.2 exige : le gabarit, le parrain, le mode d'action, l'état et l'expiration.

Avant tout outil, la CSA recommande d'inventorier les identités d'agents existantes, y compris celles qui réutilisent des identifiants de développeur ou de compte de service [12].

---

## 29.4 Identité de charge de travail : SPIFFE, WIMSE

### SPIFFE : une identité sans secret déployé

SPIFFE définit une charge de travail comme un logiciel déployé avec une configuration particulière pour un seul objet; ce peut être un processus [4].

- Le **SPIFFE ID** est un URI de la forme `spiffe://domaine-de-confiance/identifiant`, par exemple `spiffe://acme.com/billing/payments`.
- Le **domaine de confiance** correspond à la racine de confiance d'un système. Les documents d'identité de ses charges se vérifient contre ses clés racines.
- Le **SVID** est le document par lequel une charge prouve son identité. Il porte un seul SPIFFE ID et prend la forme d'un certificat X.509 ou d'un jeton JWT; la page recommande le premier, le second étant exposé au rejeu.
- La **Workload API** remet à la charge son identifiant, ses clés et ses certificats, ainsi que les lots de confiance qui servent à vérifier les autres charges.

Deux propriétés importent pour les agents. La charge n'a besoin d'aucun secret pour s'adresser à la Workload API : rien n'est à déployer avec elle [4]. Et les clés privées sont de courte durée, renouvelées souvent et automatiquement. C'est le contraire exact de la clé d'API collée dans un fichier de configuration.

### WIMSE et le brouillon AIMS

Le groupe WIMSE de l'IETF travaille à l'identité des charges de travail à travers plusieurs systèmes (chapitre 11). Son brouillon AIMS, révision 01 du 2 novembre 2026, est de portée informative. Il ne définit aucun protocole : il propose un cadre pour appliquer les standards existants aux agents et repérer les manques [3]. Ses auteurs sont rattachés à Defakto Security, AWS, Zscaler, Ping Identity, OpenAI et Okta.

Le texte présente AIMS comme un modèle conceptuel à huit composants empilés : identifiants, justificatifs, approvisionnement, authentification, autorisation, observabilité et remédiation, politique, conformité. Les quatre premiers relèvent de l'identité de charge.

**Identifiant.** Un agent doit être identifié de façon unique. L'identifiant WIMSE est l'identifiant principal, et un SPIFFE ID peut en tenir lieu. Chaque agent en reçoit exactement un.

**Justificatifs.** Un identifiant seul ne suffit pas : l'agent doit détenir un justificatif qui le lie cryptographiquement à cet identifiant, jeton ou certificat X.509. Les justificatifs devraient être de courte durée et doivent porter une expiration explicite. Si un environnement patrimonial exige une autre forme, l'agent échange son justificatif principal contre celle-ci.

**Une règle propre aux agents.** Le modèle de langage ne doit avoir accès ni aux justificatifs de l'agent ni à ceux qu'exigent les outils et les services [3]. Les secrets vivent dans l'enveloppe d'exécution, jamais dans le contexte : ce que le modèle peut lire, une injection de prompts peut tenter de le lui faire divulguer (chapitre 31).

**Authentification.** Deux couches sont décrites.

| Couche | Mécanisme | Limite relevée par le brouillon |
|---|---|---|
| Transport | TLS mutuel avec identités de courte durée; maillages de services | Rompu quand un mandataire, une passerelle ou un répartiteur termine TLS |
| Application | Jeton de preuve WIMSE; signatures de messages HTTP (RFC 9421) | Pas de liaison au canal : durées courtes, audience restreinte et nonces nécessaires contre le rejeu |

La limite du transport pèse lourd dans une architecture agentique, où le trafic traverse presque toujours une passerelle (chapitre 24). L'authentification de couche applicative, indépendante du transport, y devient la voie normale.

### Limites

Aucune RFC n'est sortie du groupe WIMSE (chapitre 11); ses jetons et ses preuves sont eux-mêmes des brouillons. SPIFFE est déployable aujourd'hui, dans un périmètre précis. La CSA observe, en le présentant comme son appréciation, que l'attestation suppose un émetteur qui voit et contrôle l'infrastructure sous-jacente, condition qui ne tient pas d'une organisation à l'autre [12]. L'identité de charge établit qui est l'agent chez soi. Elle ne dit rien de la personne pour qui il agit.

---

## 29.5 OAuth pour les agents : délégation, échange de jetons, preuve de possession

### Deux identifiants dans un jeton

Le brouillon AIMS traite OAuth 2.0 comme le cadre de délégation : l'agent est un client OAuth, il obtient un jeton d'accès d'un serveur d'autorisation, et le serveur de ressources l'accepte [3]. Dans un jeton au format JWT, la revendication `client_id` désigne l'agent, et `sub` désigne l'utilisateur ou le système qui délègue. Les deux moitiés de la question directrice tiennent dans ces deux champs.

Le brouillon décrit trois voies d'obtention.

1. **L'utilisateur délègue.** Flux par code d'autorisation. L'utilisateur devrait s'authentifier par une méthode résistante à l'hameçonnage; l'agent s'authentifie auprès du serveur d'autorisation par son justificatif de charge, non par un secret statique.
2. **L'agent agit pour lui-même.** Flux *client credentials* ou assertion JWT (RFC 7523).
3. **L'agent est lui-même la ressource**, appelée par un système ou un autre agent.

Elles recoupent les modes d'Entra : OBO pour l'agent interactif, *client credentials* pour l'agent autonome [1].

### Délégation n'est pas usurpation

L'échange de jetons (RFC 8693, janvier 2020) permet à un client de demander un jeton à partir d'un autre [5]. Le texte distingue deux sémantiques. Dans l'**usurpation** (*impersonation*), la partie agissante reçoit les droits du sujet et se confond avec lui. Dans la **délégation**, elle conserve sa propre identité et agit pour le compte du sujet.

Pour un agent, seule la délégation répond à la question directrice. Un jeton d'usurpation efface l'agent des journaux : on y lit l'utilisateur, alors qu'il n'a rien fait.

La délégation s'exprime par la revendication `act`, qui désigne l'acteur courant. Des `act` imbriqués forment une chaîne : l'acteur courant est à l'extérieur, le plus ancien au plus profond [5]. Une revendication `may_act` déclare qui est autorisé à devenir acteur pour un sujet.

Le consommateur d'un jeton ne doit tenir compte, pour le contrôle d'accès, que des revendications de premier niveau et de l'acteur courant; les acteurs antérieurs sont purement informatifs [5]. La chaîne sert à l'audit, pas à la décision. Une politique qui dépendrait d'un maillon intermédiaire — refuser tout ce qui est passé par tel agent — sort du standard. Les chaînes de délégation et l'autorité réduite des sous-agents sont traitées au chapitre 30.

### Ne pas relayer le jeton

Le brouillon AIMS rejoint ici MCP, qui interdit à un serveur de relayer le jeton reçu (chapitre 5). Qu'un outil relaie aux services en aval le jeton d'accès reçu de l'agent est un antipatron; il procède plutôt par échange de jetons ou par jetons de transaction [3]. Ces derniers sont de courte durée, liés à une transaction, inutilisables comme jetons d'accès, et leur portée ne peut jamais excéder celle du jeton dont ils dérivent.

### Preuve de possession

Un jeton au porteur vaut pour quiconque le détient. DPoP (RFC 9449, septembre 2023) le lie à une clé [6]. Le client joint à chaque requête un en-tête `DPoP`, JWT signé qui porte sa clé publique, la méthode et l'URI de la requête et, devant un serveur de ressources, l'empreinte du jeton d'accès. Le jeton porte l'empreinte de la clé dans sa revendication `cnf`. Un jeton volé ne sert à rien sans la clé privée.

La RFC énonce ses propres limites. DPoP ne remplace pas TLS. Seuls la méthode et l'URI sont signés, pas le corps du message. Un code qui s'exécute dans le contexte du client peut produire des preuves valides [6].

La feuille de route de MCP du 22 août 2026 inscrit DPoP parmi les livrables d'un groupe de travail sur l'identité des agents, encore en formation : finaliser la spécification, puis obtenir une adoption large [9]. Le même groupe doit traiter la fédération d'identités de charge, l'ID-JAG et l'échange de jetons, en coordination avec les groupes OAuth et WIMSE, sans engagement ferme [9]. Le brouillon AIMS cite deux moyens de lier un jeton à son détenteur, le certificat TLS mutuel et DPoP [3]. Un agent qui dispose déjà d'un certificat de charge a donc le choix.

### L'ID-JAG

L'Identity Assertion JWT Authorization Grant fonde l'autorisation gérée par l'entreprise de MCP (chapitre 5). Le brouillon, révision 06 du 31 octobre 2026, vise la voie de normalisation [7]. Le client échange son jeton d'identité auprès du fournisseur d'identité, qui évalue sa politique et émet l'ID-JAG; le client le présente au serveur d'autorisation de la ressource, qui émet son propre jeton d'accès et peut restreindre ou refuser. La revendication `act` y est facultative, et le texte laisse à de futurs profils le soin de dire si l'ID-JAG émis la porte [7]. L'annexe informative « AI Agent using External Tools » s'en passe : l'agent n'y est désigné que par `client_id`, et `sub` reste l'employé [7].

### Ce que OAuth ne règle pas encore

Le brouillon AIMS admet un manque sur l'approbation humaine. Le serveur d'autorisation peut exiger une confirmation explicite, et CIBA, le flux d'authentification par canal secondaire d'OpenID, fournit une approbation hors bande. Mais CIBA part du client et convient mal à une confirmation en cours d'exécution; du travail de spécification pourrait rester à faire. Le texte ajoute qu'une confirmation dans l'interface locale ne constitue pas, à elle seule, une autorisation [3]. L'attestation de présence humaine figure parmi les sujets que le groupe de MCP pourrait prendre en charge [9] (chapitre 30).

La CSA soutient qu'OAuth 2.0, OpenID Connect et SAML ne peuvent pas exprimer les chaînes d'autorité des agents [12]. Le brouillon AIMS montre qu'on va loin avec la famille OAuth. Les deux se rejoignent sur un point : la provenance complète d'une action déléguée sur plusieurs sauts n'a pas de mécanisme natif de vérification.

---

## 29.6 Identité décentralisée

Les Decentralized Identifiers (DID) v1.0 sont une recommandation du W3C depuis le 19 juillet 2022 [10]; la v1.1 n'était, à la lecture, qu'une recommandation candidate datée du 5 mars 2026 [15]. Un DID est un identifiant persistant et mondialement unique qui n'exige pas d'autorité centrale d'enregistrement. Il renvoie à un document DID, qui décrit le sujet et contient notamment des clés publiques. Une méthode DID, définie dans une spécification à part, dit comment créer, résoudre, mettre à jour et désactiver l'identifiant. Le contrôleur d'un DID peut prouver qu'il le contrôle sans la permission d'un tiers.

**L'attrait pour les agents.** Les mécanismes des sections précédentes supposent une racine : le fournisseur d'identité de l'entreprise, ou l'émetteur d'un domaine de confiance. Entre deux organisations sans relation préalable, cette racine manque. C'est le terrain que visent les approches décentralisées : ANP fonde son identité sur les DID (chapitre 7), et un groupe communautaire du W3C annonce une méthode DID et un score de confiance pour les agents, sans avoir rien publié (chapitre 11).

**L'état réel.** La recommandation normalise un modèle de données; l'interopérabilité dépend de la méthode retenue, et chaque méthode a sa spécification [10]. Aucun profil DID propre aux agents n'a été adopté par un organisme de normalisation, d'après les pages lues ici et au chapitre 11. Et le brouillon AIMS, dont les auteurs viennent de plusieurs fournisseurs d'identité, ne s'appuie pas sur les DID [3].

Supprimer la racine ne supprime pas la question de la confiance : savoir qu'un agent contrôle un identifiant ne dit pas qui en répond. La posture recommandée au chapitre 11 pour cette couche est d'attendre, en isolant la dépendance derrière un adaptateur.

---

## 29.7 État de la normalisation

Le tableau classe les textes par solidité.

| Texte | Organisme | État au 11 novembre 2026 |
|---|---|---|
| OAuth 2.0 Token Exchange, RFC 8693 [5] | IETF | RFC, janvier 2020 |
| DPoP, RFC 9449 [6] | IETF | RFC, septembre 2023 |
| DID v1.0 [10] | W3C | Recommandation, 19 juillet 2022 |
| SPIFFE [4] | Projet SPIFFE | Spécification de projet |
| Identity and Authorization Chaining [8] | IETF, OAuth | Révision 17 du 19 juillet 2026; approuvé, file du RFC Editor (état « bloqué ») |
| ID-JAG [7] | IETF, OAuth | Révision 06, document de groupe |
| AIMS [3] | IETF, WIMSE | Révision 01, informatif |
| Identité d'agent dans MCP [9] | Projet MCP | Groupe de travail en formation |
| Identité et autorisation des agents [11] | NIST, NCCoE | Document de réflexion; projet éventuel |

**Les briques sont normalisées, l'assemblage ne l'est pas.** L'échange de jetons, la preuve de possession et les identifiants décentralisés sont des normes publiées depuis des années. Ce qui porte le mot « agent » est au mieux un brouillon de groupe. Le texte le plus complet, AIMS, est informatif et se présente comme un guide d'application.

**Le brouillon AIMS exclut plusieurs sujets de son périmètre** [3] : la traduction d'une mission en exigences d'autorisation, le modèle et le format des politiques, qu'il ne recommande pas de normaliser, les critères de conformité, l'espace de noms et le registre des identifiants. Il dépend en outre de textes encore à l'état de brouillon pour l'accès entre domaines et les jetons de transaction.

**Les organismes publics consultent.** Le document de réflexion du NCCoE, publié le 5 février 2026, expose les considérations d'un projet de démonstration éventuel [11]. Il sollicitait des avis jusqu'au 2 avril 2026. La page d'annonce ne donne pas d'échéancier au-delà. Le chapitre 11 replace ces travaux parmi les instances et décrit la voie chinoise, qui pose une racine nationale.

---

## 29.8 Identité entre organisations

À l'intérieur d'une organisation, un seul fournisseur d'identité arbitre. Entre deux organisations, il faut que l'une accepte ce que l'autre atteste. Les textes lus offrent trois mécanismes, qui supposent chacun une relation préalable différente.

| Mécanisme | Relation requise | Ce qui traverse la frontière |
|---|---|---|
| Chaînage d'identité et d'autorisation [8] | Le domaine B fait confiance aux clés de signature du serveur d'autorisation de A | Un octroi JWT, que B convertit en jeton d'accès |
| ID-JAG [7] | Un fournisseur d'identité commun, reconnu par le serveur d'autorisation de la ressource | Une assertion émise par ce fournisseur |
| Identifiants décentralisés [10] | Aucune racine commune; une méthode DID partagée | Une preuve de contrôle de l'identifiant |

### Le chaînage

Le brouillon *OAuth Identity and Authorization Chaining Across Domains* est le plus avancé : sa révision 17, du 19 juillet 2026, est approuvée et visée comme norme proposée; sa fiche la place dans la file du RFC Editor, à l'état « bloqué », sans numéro de RFC [8]. Le mécanisme tient en trois temps. Le client du domaine A découvre le serveur d'autorisation du domaine B. Il échange un jeton qu'il détient contre un octroi JWT auprès du serveur de A (RFC 8693). Il présente cet octroi au serveur de B (RFC 7523), qui le valide et émet un jeton d'accès pour sa ressource. Le même protocole se répète à chaque frontière.

Deux propriétés le rendent adapté aux agents. Le domaine B reste maître de ses jetons : il n'accepte jamais un jeton de A, seulement une assertion qu'il convertit selon sa politique. Et les revendications peuvent être transcrites à chaque étape, pour faire correspondre les identifiants de sujet, limiter les données communiquées à l'autre domaine ou réduire les permissions [8].

Le brouillon AIMS recommande cette approche et y ajoute un principe : l'interopération transporte dans les jetons le résultat des politiques, sans exiger le partage d'un langage de politique [3]. Chaque organisation garde ses règles; elles ne s'échangent que des conclusions.

### Ce qui reste hors de portée

Ces mécanismes transportent une assertion. Ils ne disent pas pourquoi B devrait croire A. La confiance initiale, soit l'échange des clés et la portée de ce que chacun accepte, reste une affaire d'entente bilatérale et de contrat (chapitre 36). Le vLEI de la GLEIF vise ce maillon en rattachant une signature à une personne morale enregistrée; son extension aux agents reste une orientation sans format publié (chapitre 45).

L'identité de charge ne franchit pas d'elle-même la frontière, pour la raison donnée en 29.4, même si certains écosystèmes la fédèrent : l'annuaire d'AGNTCY fonde l'authentification entre organisations sur SPIFFE (chapitre 8). Du côté des protocoles d'agents, la CSA note que les Agent Cards signées d'A2A prouvent qu'une carte vient du domaine qu'elle revendique, mais qu'aucun mécanisme natif ne vérifie encore la provenance complète d'une action déléguée [12] (chapitre 6).

En pratique, une entreprise qui ouvre ses agents à un partenaire part d'une relation bilatérale explicite, émet des assertions de courte durée et à audience restreinte, et exige que la délégation reste visible : l'agent du partenaire se présente comme agent, pour le compte d'un sujet nommé.

### Le web public et l'intermédiaire

Depuis le 1er juillet 2026, Cloudflare distingue l'accès direct, où un seul opérateur émet les requêtes, de l'accès par intermédiaire, où un service agentique est piloté par de nombreux utilisateurs; se fier à l'opérateur ne revient pas à se fier à chacun d'eux, d'où une confiance transitive [14]. La signature identifie l'opérateur, non l'utilisateur représenté (chapitre 9), et la transmission de ce dernier par l'en-tête `Forwarded` n'est qu'à l'essai [14]. Par déduction, seul un jeton OAuth exigé par le site porterait un sujet délégant vérifiable, au sens de 29.5. L'agent qui achète relève du chapitre 10.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Identité d'un agent | Identité propre, une par agent, distincte de celles des utilisateurs et des applications [É] | Jamais pour un agent en production |
| Justificatifs | Courte durée, émis à l'exécution, renouvelés automatiquement [É] | Système patrimonial : justificatif dérivé par échange, jamais de clé statique partagée |
| Accès du modèle aux secrets | Aucun; les secrets restent dans l'enveloppe d'exécution [É] | — |
| Responsable humain | Parrain obligatoire, propriétaire technique désigné, tous deux réattribués au départ [É] | — |
| Sémantique d'échange de jetons | Délégation, avec `act` [N] | Usurpation seulement si le système cible ne peut rien d'autre, avec journalisation compensatoire |
| Compte utilisateur pour un agent | Non [É] | Système qui exige un objet utilisateur; l'identité d'agent demeure |
| Authentification derrière une passerelle | Couche applicative [S] | Maillage de bout en bout sans terminaison TLS : TLS mutuel |
| Jetons d'accès | Liés au détenteur (TLS mutuel ou DPoP), audience restreinte [N] | Liaison non prise en charge : durée très courte |
| Appels en aval d'un outil | Échange de jetons ou jeton de transaction [N] | Aucun cas pour le relais du jeton reçu |
| Annuaire | Celui du fournisseur d'identité, complété des attributs de 29.3 [S] | Parc multi-plateformes : annuaire maître indépendant |
| Accès entre organisations | Chaînage d'identité sur entente bilatérale [S] | Fournisseur d'identité commun : ID-JAG |
| Identité décentralisée | Veille [S] | Consortium sectoriel qui impose une méthode |

---

## Points à retenir

- Un agent s'authentifie comme une charge de travail. Il s'en distingue par un parrain humain, un contexte de délégation à préserver et un cycle de vie rapide.
- La question « qui, et au nom de qui » se lit dans deux champs d'un jeton : `client_id` pour l'agent, `sub` pour celui qui délègue. Un jeton d'usurpation efface le premier.
- Dans une chaîne `act`, seul l'acteur courant compte pour le contrôle d'accès; les acteurs antérieurs sont informatifs. La chaîne sert à l'audit.
- Le modèle de langage ne doit jamais voir un justificatif. Les clés d'API statiques et le relais, par un outil, du jeton reçu sont des antipatrons.
- Un identifiant d'agent retiré ne se réattribue pas : les journaux doivent rester lisibles.
- L'annuaire d'agents n'a pas de schéma normalisé. Registre de découverte et annuaire d'identité sont deux objets distincts.
- Les briques sont des normes publiées (RFC 8693, RFC 9449, DID v1.0). Leur composition pour les agents n'existe qu'en brouillon : AIMS est informatif, l'ID-JAG n'est pas une RFC, le groupe de MCP se forme.
- Entre organisations, le chaînage d'identité est le mécanisme le plus proche de la publication. Il transporte une assertion; la confiance initiale reste contractuelle.
- L'identité décentralisée vise un vrai manque, sans profil adopté pour les agents.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Microsoft Learn — Microsoft Entra security for AI overview](https://learn.microsoft.com/en-us/entra/agent-id/security-for-ai-overview) (mise à jour du 14 août 2026)
2. [Microsoft Learn — What are agent identities?](https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities) (mise à jour du 15 juin 2026)
3. [IETF — draft-ietf-wimse-aims-01, « AI Identity Management System »](https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/)
4. [SPIFFE — concepts](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/)
5. [RFC 8693 — OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693.html)
6. [RFC 9449 — OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://www.rfc-editor.org/rfc/rfc9449.html)
7. [IETF — draft-ietf-oauth-identity-assertion-authz-grant-06](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/)
8. [IETF — draft-ietf-oauth-identity-chaining-17](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/)
9. [MCP — feuille de route, mise à jour du 22 août 2026](https://modelcontextprotocol.io/development/roadmap.md)
10. [W3C — Decentralized Identifiers (DIDs) v1.0](https://www.w3.org/TR/did-1.0/)
11. [NIST — annonce du document de réflexion du NCCoE, 5 février 2026](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents)

Source secondaire, lue :

12. [Cloud Security Alliance — « Agentic Identity: Emerging Standards and Security Guidance », note de recherche du 16 septembre 2026](https://labs.cloudsecurityalliance.org/research/csa-slack-20260916-225950-csa-styled/) — synthèse appuyée en partie sur des billets de fournisseurs; plusieurs conclusions sont l'appréciation de ses auteurs.

Pages primaires lues le 12 novembre 2026, lors de l'audit :

13. [Microsoft Learn — Owners, sponsors, and managers in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers)
14. [Cloudflare — agents signés et robots vérifiés](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/)
15. [W3C — Decentralized Identifiers (DIDs) v1.1](https://www.w3.org/TR/did-1.1/)

## Limites de ce chapitre

- Les pages ont été lues par un outil qui en produit un condensé. Lors de l'audit, les obligations d'AIMS citées ici, l'état du chaînage et l'annexe de l'ID-JAG sur les agents ont été relus; les RFC et les autres passages restent à contrôler sur le texte.
- Pour Entra, trois pages ont été lues; celle des gabarits ne l'a pas été. Le départ d'un parrain n'a pas de mécanisme décrit dans la page lue [13]. Les conditions de licence, décrites au chapitre 26, ne sont pas reprises.
- La répartition entre Agent 365 et Entra, le compteur d'agents sans propriétaire, l'usage de SPIFFE par AGNTCY, les DID dans ANP, les groupes du W3C, le vLEI et la portée de la signature Web Bot Auth sont repris des chapitres 7, 8, 9, 11, 26 et 45, non de pages lues pour ce chapitre.
- Les justificatifs vérifiables du W3C, la fédération SPIFFE, CIBA, les signaux d'événements et les jetons de transaction ne sont connus ici que par les mentions qu'en font les sources lues. Les changements de la v1.1 des DID par rapport à la v1.0 n'ont pas été lus.
- La fiche du chaînage n'explique pas l'état « bloqué »; une dépendance en attente est une supposition.
- Aucun chiffre d'adoption n'est cité : la seule estimation rencontrée est non chiffrée et de source secondaire.
- Lors de l'audit du 14 novembre 2026, [10] (W3C DID v1.0), [12] (CSA) et [15] (W3C DID v1.1) ont renvoyé un accès restreint (HTTP 403 anti-robot au script automatique); leurs titres, dates et statuts (recommandation DID v1.0 du 19 juillet 2022; recommandation candidate DID v1.1 du 5 mars 2026) sont confirmés par recherche web.
- La liste d'attributs d'annuaire de 29.3 et la grille de décision sont des synthèses propres à ce chapitre.
