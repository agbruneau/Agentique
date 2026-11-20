# 7 · Généalogie et gouvernance : des projets propriétaires aux standards ouverts

*Livre I — Coopérer : fondements de l’interopérabilité et couche protocolaire agentique. Second mouvement — la couche protocolaire agentique (ch. 7-11). Premier chapitre du mouvement.*

## 7.0 Introduction : de l’échange de données à l’échange d’intentions

> **Thèse** — en dix-sept mois, la couche protocolaire agentique s’est consolidée sous gouvernance neutre (Linux Foundation) — condition nécessaire et non suffisante de sa crédibilité en entreprise réglementée ; mais « soutien ≠ production », et le transfert de gouvernance d’AP2 vers la FIDO Alliance a été annoncé le **28 avril 2026** (billet officiel de Google Cloud, `S-090` **[A]**, version v0.2, cas *Human-Not-Present*, deux groupes de travail techniques), sans que sa matérialisation soit établie à la revalidation (`S-091`, instruit au ch. 10).

Le second mouvement du Livre s’ouvre ici. Les ch. 1 à 3 ont posé le socle **pré-agentique** ; les ch. 4 à 6, l’**ingénierie de l’agent**. Ce mouvement traite la couche d’interopérabilité agentique proprement dite — le contrat entre un agent et ses outils, le dialogue entre agents, la découverte, le règlement commercial, et les modes d’échec qui leur sont propres.

La proposition directrice tient en un déplacement, et il vaut d’être énoncé avec précision : ce qui transite entre systèmes d’IA n’est plus seulement de la **donnée structurée**, comme dans l’intégration d’entreprise classique (ch. 2), mais des **intentions**, des **tâches** et des **capacités** négociées à l’exécution.

Ce déplacement se lit comme un glissement des noms vers les verbes. Une interface REST est orientée **ressources** : elle expose des entités — un client, une commande, un compte — que l’on crée, lit, modifie ou supprime. Un agent est orienté **actions** : il reçoit un but exprimé en langage naturel, sélectionne des opérations et les compose pour produire un résultat dont la forme n’était pas entièrement prédéterminée.

L’objet de l’échange se déplace ainsi de l’**état partagé** vers l’**action déléguée**. Ce glissement réactive la distinction posée au ch. 1 § 1.1.1 : l’interopérabilité n’est ni la connectivité, ni la compatibilité de formats, mais la capacité d’échanger de l’information et d’en faire un usage utile.

*C’est précisément parce que l’unité d’échange devient l’intention* — entité non déterministe, sous-spécifiée, interprétée à l’inférence — que la connectivité cesse de garantir l’interopérabilité. Le problème se déplace de la plomberie vers la négociation du sens, et c’est ce déplacement que le ch. 9 § 9.4 mesure.

## 7.1 Définir l’interopérabilité agentique et ses niveaux

### 7.1.1 Définition de travail

L’**interopérabilité agentique** se définit comme la capacité de systèmes d’intelligence artificielle agentique — autonomes, hétérogènes, pilotés par grand modèle de langage — à se découvrir mutuellement, se comprendre, déléguer des tâches et collaborer sans intégration point-à-point préalable.

Trois traits la distinguent de l’interopérabilité des systèmes d’information :

1. **l’absence d’intégration préétablie** — la mise en relation se négocie **à l’exécution** ;
2. l’hétérogénéité radicale des acteurs — modèles, cadriciels et fournisseurs distincts ;
3. la nature de ce qui transite — non plus des données structurées mais des intentions et des tâches.

*Cette définition appelle une contrepartie opérationnelle, et son absence est le défaut le plus répandu du domaine.* Un système n’est dit interopérable que si une tâche déléguée d’un agent à un autre aboutit avec un taux de réussite et une fidélité de transfert d’intention vérifiables — et non au seul constat que la connexion s’établit. Le ch. 9 § 9.5 reprend cette exigence comme problème de conformité.

### 7.1.2 Les niveaux LCIM appliqués aux agents

Le modèle des niveaux d’interopérabilité conceptuelle, introduit au ch. 1 § 1.1.2, se transpose directement à la pile agentique (le Tableau 7.1) :

***Tableau 7.1** — Les niveaux du LCIM retenus pour la pile agentique (cinq des sept niveaux de l’échelle du § 1.1.2, hors niveau 0 d’absence et niveau 6 d’interopérabilité conceptuelle).*

| **Niveau** | **Ce qu’il couvre, côté agentique** |
| --- | --- |
| **Technique** | transport et connectivité — HTTP, appels de procédure en JSON, flux d’événements, entrée-sortie standard |
| **Syntaxique** | structure des messages — appels d’outils, cartes d’agent, cycle de vie des tâches |
| **Sémantique** | sens partagé — alignement des intentions, ancrage des termes sur des référents communs |
| **Pragmatique** | inférence de **l’action effectivement voulue** à partir d’un message |
| **Dynamique** | capacité à s’adapter, renégocier, découvrir des partenaires **à l’exécution** |

### 7.1.3 Pragmatique et dynamique : des niveaux existants devenus verrous opérationnels

*Il importe de souligner ce que les niveaux pragmatique et dynamique ne sont pas : des inventions de l’ère agentique.* Le pragmatique et le dynamique figurent en propre dans le modèle d’origine. Ce qui change n’est pas leur existence, mais leur **centralité opérationnelle**. Écrire que l’agentique « ajoute deux niveaux » serait une erreur de fait, et elle est fréquente.

Le déplacement est ailleurs, et il est plus intéressant. Dans l’intégration classique, le verrou dominant se situait au **sémantique** : faire correspondre des schémas et des vocabulaires (ch. 2). Avec des acteurs pilotés par modèle, le **pragmatique** — inférer l’action voulue, et non seulement décoder le contenu — devient le verrou prépondérant.

Ce niveau se manifeste d’une manière propre aux agents : le sens n’est plus calculé par un programme déterministe mais lu par le modèle à l’inférence, à partir de descriptions en langage naturel interprétées au moment de l’exécution. Le niveau **dynamique**, lui, recouvre la négociation et la découverte à l’exécution — ce qui n’avait **pas d’équivalent généralisé** dans les piles d’intégration figées au temps de conception.

Ces deux niveaux, anciens dans la théorie, deviennent ainsi le terrain effectif où se joue — ou échoue — l’interopérabilité agentique.

### 7.1.4 Ce qui change quand les acteurs sont autonomes et non déterministes

Quatre ruptures distinguent l’interopérabilité agentique de l’intégration classique :

- **le non-déterminisme** — un acteur piloté par modèle ne garantit pas une réponse identique à entrée identique, ce qui substitue des garanties probabilistes aux garanties exactes ;
- l’auto-description et la découverte à l’exécution — l’acteur publie ses capacités sous une forme interprétable, et un pair les découvre puis les sélectionne au moment de l’échange ;
- le langage naturel comme surface d’interface — souple, mais ambigu et non vérifiable mécaniquement ;
- l’orientation vers les buts — l’acteur poursuit des objectifs plutôt qu’il n’exécute des instructions littérales, ce qui érige la négociation et la clarification en primitives d’interaction.

*Ces traits, qui font la puissance des systèmes agentiques, sont aussi la racine de leurs modes d’échec* — lesquels ne se résolvent pas au niveau du modèle isolé (ch. 6) mais aux frontières entre acteurs (ch. 11).

### 7.1.5 Reformuler la triade pour des acteurs probabilistes

Les trois termes de l’invariant doivent être réénoncés.

Le **contrat**, déterministe dans le monde des API — une requête valide produit une réponse conforme au schéma (ch. 1 § 1.4.2) —, devient un **contrat comportemental probabiliste** : on ne peut plus garantir qu’une entrée valide produira **invariablement** la sortie attendue, seulement qu’elle la produira avec une certaine probabilité. Les travaux sur les contrats comportementaux d’agents (Bhardwaj, 2026) formalisent cette idée en spécifiant la satisfaction d’un contrat par un triplet — probabilité minimale, tolérance, nombre d’essais — assorti d’une **vérification à l’exécution**.

Le **découplage** s’enrichit de deux dimensions absentes du ch. 1 : le découplage de **modèle** — l’application ne doit pas être liée à un fournisseur de modèle particulier — et de **cadriciel** — elle ne doit pas être liée à un cadriciel d’orchestration donné. Le ch. 9 § 9.3 les développe.

L’**évolution** prend enfin la forme d’un **versionnement des capacités** et d’une **politique de dépréciation** : un agent ou un outil doit pouvoir faire évoluer ce qu’il offre sans briser ses consommateurs.

**Perspective recherche.** Le passage du contrat déterministe au contrat comportemental probabiliste reformule la garantie d’interopérabilité comme une propriété statistique vérifiée à l’exécution plutôt que comme une propriété structurelle vérifiée à la compilation. La spécification par probabilité cible, marge tolérée et répétitions fournit un **objet formel mesurable**, et son contrôle continu rapproche le contrat d’agent des **engagements observables** de la tradition multi-agents plutôt que des sémantiques mentalistes (§ 7.2.1).

### 7.1.6 Pourquoi l’interopérabilité classique ne suffit pas : l’argument de l’étagement

L’interopérabilité classique — appel de procédure à distance, API REST, bus de service (ch. 1 § 1.3 et § 1.4) — atteint ses limites devant les acteurs agentiques sur quatre points :

1. elle ne prévoit pas d’auto-description exploitable à l’exécution — un contrat décrit des points d’extrémité au temps de conception, non des capacités négociées à l’inférence ;
2. elle est orientée **ressources** là où les agents sont orientés **actions** ;
3. elle suppose un **appelant déterministe** capable de composer correctement les requêtes ;
4. elle n’offre **aucune primitive native** pour les tâches de longue durée ni pour la négociation.

*Ces limites ne justifient pas de remplacer la pile classique, et c’est le point d’équilibre essentiel contre la surenchère.* Les protocoles agentiques majeurs **réemploient massivement l’existant** : le protocole agent-outil s’appuie sur des appels de procédure en JSON et sur HTTP, et adosse son autorisation à des mécanismes éprouvés ; le protocole agent-agent propose plusieurs liaisons de transport.

*La couche agentique* ***s’étage*** *au-dessus de la pile éprouvée — transport, sérialisation, autorisation — plutôt qu’elle ne s’y substitue.* L’apport propre se situe **au-dessus** : auto-description, découverte à l’exécution, modèle de tâche, négociation. C’est l’argument que le ch. 9 § 9.2 systématise sous le nom d’étagement.

## 7.2 Filiation historique et taxonomie des quatre axes

### 7.2.1 KQML, FIPA-ACL, actes de langage et protocoles à engagements

L’interopérabilité agentique n’est pas sans ascendance, et l’ignorer conduit à réinventer des échecs documentés.

Le langage **KQML** proposait dès le milieu des années 1990 un jeu de **performatifs** — des verbes de communication typés — pour structurer les échanges entre agents (Finin et coll., 1994). Les spécifications **FIPA-ACL** ont prolongé cet effort en normalisant la structure des messages et une bibliothèque d’**actes communicatifs** (FIPA, 2002). Cette tradition s’enracine dans la théorie des actes de langage, qui montre que **dire, c’est faire** — promettre, ordonner, demander étant des actions accomplies par la parole (Austin, 1962 ; Searle, 1969).

*Le verrou historique mérite d’être nommé, parce qu’il se rejoue aujourd’hui.* La sémantique de FIPA-ACL reposait sur une lecture **mentaliste**, définissant la signification d’un message par les croyances et intentions présumées de l’émetteur. Or ces états mentaux ne sont pas observables, donc pas vérifiables : un agent ne peut prouver qu’un pair *croit* ou *veut* ce qu’il déclare. C’est la perte de sémantique vérifiable.

La réponse historique fut de fonder la signification sur des **engagements sociaux observables** plutôt que sur des états mentaux privés (Singh, 1998 ; 2000), et de spécifier les protocoles par les engagements qu’ils créent et règlent (Yolum et Singh, 2002) — pont direct vers les contrats comportementaux du § 7.1.5.

La leçon d’adoption est tout aussi instructive, et elle vaut avertissement : le formalisme lourd de FIPA n’a jamais connu de déploiement à grande échelle. Ce constat plaide, pour la pile agentique actuelle, en faveur de mécanismes plus légers que des logiques mentalistes complètes.

**Perspective recherche.** Le déplacement de la sémantique mentaliste vers une sémantique d’engagements (Singh, 1998 ; 2000 ; Yolum et Singh, 2002) constitue le précédent théorique le plus pertinent pour l’interopérabilité agentique contemporaine : il troque une signification fondée sur des états internes inaccessibles contre une signification fondée sur des obligations sociales observables et vérifiables. Cette filiation éclaire pourquoi le grand modèle de langage — qui **infère** le sens à la lecture plutôt qu’il ne le calcule formellement — réintroduit, sous une autre forme, le problème de vérifiabilité que FIPA n’avait pas résolu.

### 7.2.2 Taxonomie des quatre axes d’interopérabilité

La couche agentique s’organise autour de **quatre axes**, qui constituent la carte du mouvement (le Tableau 7.2) :

***Tableau 7.2** — Les quatre axes de l’interopérabilité agentique et leur lieu de traitement dans la somme.*

| **Axe** | **Nature** | **Ce qu’il porte** | **Où il est traité** |
| --- | --- | --- | --- |
| **Agent-outil** | vertical | un agent invoque des outils et ressources pour étendre ses capacités | ch. 8 § 8.1-8.3 |
| **Agent-agent** | horizontal | des agents autonomes se délèguent des tâches par-delà les frontières | ch. 8 § 8.4-8.6 |
| **Agent-humain** | — | négociation de l’interaction : points de validation, consentement, modalités | ch. 9 § 9.2.5, ch. 17 § 17.4 et ch. 24 § 24.5 (transverse) |
| **Agent-données** | — | accès gouverné aux données, récupération inter-organisationnelle | ch. 2, ch. 9 § 9.4 |

*Cette quadripartition n’est pas une cloison étanche* : un système de production mobilise simultanément plusieurs axes (ch. 9 § 9.2.4). Elle fournit le squelette analytique du mouvement et fixe le périmètre de chaque chapitre.

Elle est aussi le socle amont d’un instrument du Livre II. La grille des cinq questions du ch. 14 se construit sur cette taxonomie ; le lecteur qui la rencontrera là-bas doit pouvoir en retrouver la racine ici. Cette filiation directe relie la taxonomie fonctionnelle du Livre I à la grille d’évaluation du Livre II.

### 7.2.3 Panorama introductif des modes d’échec

Avant d’examiner chaque axe, il est utile de poser le cadre des modes d’échec spécifiques. **Six familles** se dégagent, dont le **ch. 11** (§ 11.2.1) reprend et complète l’analyse sous la grille des défaillances émergentes :

- la dérive sémantique en chaîne de délégations — à mesure qu’une intention est retransmise d’agent en agent, son sens **se déforme insensiblement**, chaque relais réinterprétant un message en langage naturel ;
- **l’échec d’ancrage** — un terme n’est pas rattaché au même référent par l’émetteur et le récepteur, qui croient pourtant s’entendre ;
- **l’ambiguïté non résolue** — un acteur agit sur une interprétation arbitraire au lieu de demander une clarification, faute de mécanisme de négociation déclenché ;
- les capacités mal décrites ou mal versionnées — une description inexacte ou périmée conduit à un mauvais appariement ;
- le non-déterminisme propageant des erreurs non reproductibles — une faute survenue à une frontière ne se reproduit pas à l’identique, ce qui en complique le diagnostic ;
- la perte de portabilité — une intégration fonctionnelle avec un fournisseur cesse de l’être avec un autre, faute de contrat partagé.

Ces familles forment la trame que le mouvement spécifie axe par axe, en remontant chaque défaillance au contrat établi — ou défaillant — entre les acteurs (la Figure 7.2).

***Figure 7.2** — Les quatre axes de l’interopérabilité agentique et le lieu de traitement de chacun (seuls les axes vertical et horizontal disposant de protocoles stabilisés).*

## 7.3 Chronologie 2024-2026 : dix-sept mois de consolidation

Une institution financière ne bâtit pas son architecture sur le produit d’un seul éditeur sans se demander ce qu’il adviendra s’il change d’avis. La question n’a rien de théorique : elle est au cœur du risque de tiers, elle figure dans les questionnaires de diligence raisonnable, et elle décide souvent, seule, de la mise en production.

C’est pourquoi cette chronologie n’est pas une chronique d’initiés : elle est la **condition préalable** au reste de la somme.

*Cette chronologie s’ordonne par protocole, non par date de lancement — et l’ordre importe : une flèche « MCP → A2A → AGNTCY » serait fausse dans les deux lectures.* Elle est fausse comme ordre de lancement, et fausse comme ordre de passage sous fondation. Les deux séquences sont inverses l’une de l’autre, et c’est le fait le plus instructif de la section.

**Lancements.** Le point de départ est **novembre 2024** : publication par **Anthropic** du protocole agent-outil (MCP), une interface client-serveur destinée à l’invocation d’outils et à l’échange de données typées, à laquelle un **cadre d’autorisation** s’ajoutera en mars 2025 (ch. 8 § 8.2.1) — le protocole naît propriétaire au sens strict : un éditeur, une spécification, un intendant.

L’essaimage est rapide, et deux initiatives apparaissent presque simultanément en mars 2025 : une **couche d’infrastructure** — annuaires de découverte et transport dédié — explicitement pensée comme complémentaire des protocoles d’échange plutôt que rivale ; et, le **17 mars 2025**, un protocole de communication entre agents — l’ACP protocolaire d’IBM Research et du projet BeeAI, sigle toujours qualifié (§ 7.5) —, en version pré-alpha et d’abord conçu comme une extension du protocole agent-outil.

En **avril 2025** paraît le protocole **agent-agent**, qui traite un problème distinct : non plus l’accès d’un agent à ses outils, mais la délégation de tâches de pair à pair, au moyen de descripteurs appelés **cartes d’agent**. En **septembre 2025** s’y ajoute un protocole compagnon dédié aux transactions pilotées par agents, dont le ch. 10 traite.

Le protocole d’infrastructure de mars 2025 est donc antérieur au protocole agent-agent d’avril 2025. L’ordre inverse, longtemps répété, ne résiste pas aux dates.

Passages sous fondation — et, pour les trois protocoles nés propriétaires (MCP, AGNTCY, A2A), l’ordre s’inverse (l’ACP protocolaire d’IBM Research et BeeAI étant né d’emblée sous l’égide de la Linux Foundation dès **mars 2025**). **Juin 2025** : le protocole agent-agent est transféré à une fondation neutre **sous licence permissive**. **29 juillet 2025** : la couche d’infrastructure suit. **29 août 2025** : l’ACP protocolaire **fusionne officiellement** dans le protocole agent-agent — le développement actif cesse, ses actifs y sont versés, des guides de migration sont fournis. **Décembre 2025**, enfin : la gouvernance du protocole agent-outil est transférée à une fondation dédiée, elle-même sous la même faîtière ; son créateur demeure le créateur, mais cesse d’en être l’unique intendant.

De novembre 2024 à **avril 2026** — date à laquelle un bilan public de la première année du protocole agent-agent est dressé —, **dix-sept mois** s’écoulent. En dix-sept mois, quatre protocoles nés dans quatre entreprises différentes — le protocole agent-outil, la couche d’infrastructure, l’ACP protocolaire et le protocole agent-agent — ont convergé vers deux fondations, dont l’une héberge l’autre. Le cinquième, le protocole de transaction, n’est pas de ce décompte : il relève d’une autre fondation, que le § 7.4.2 situe.

Un mot sur ce que cette chronologie a rendu caduc. L’article de synthèse de référence de la période (Ehtesham et coll., **mai 2025**) proposait une trajectoire d’adoption séquentielle plaçant l’ACP protocolaire en deuxième étape. La fusion d’août 2025 a vidé cette étape de sa substance moins de quatre mois après la publication. Le document conserve toute sa valeur de **jalon historiographique** — il documente ce qu’un observateur informé pouvait raisonnablement croire au printemps 2025 — mais il ne peut plus servir de guidance d’architecture. Le ch. 10 § 10.6 en fait son objet. *La vitesse à laquelle il s’est périmé est elle-même une donnée sur le domaine, et un avertissement pour la somme.*

Et la stabilité d’une gouvernance ne signifie pas l’immobilité d’une spécification : à la date de gel du Vol. II, une révision majeure du protocole agent-outil était attendue douze jours plus tard. Le ch. 8 porte cette réserve comme condition de lecture de son anatomie (la Figure 7.3).

***Figure 7.3** — Dix-sept mois : les lancements, puis les passages sous fondation — et l’ordre s’inverse pour les trois protocoles nés propriétaires (l’ACP protocolaire étant né sous fondation dès mars 2025).*

## 7.4 Gouvernance comparée : ce que « neutre » veut dire

### 7.4.1 Deux arrangements pour trois protocoles sous une destination commune

La destination commune masque **deux arrangements distincts pour trois protocoles**, et la nuance importe pour qui doit documenter une dépendance technologique dans un dossier de conformité.

Deux protocoles relèvent **directement** de la fondation faîtière ; le troisième relève d’une **fondation dédiée** formée en décembre 2025 et **hébergée par** la première. *La différence est de degré, non de nature* : dans les trois cas, la propriété intellectuelle et le processus de décision **quittent l’entreprise fondatrice**. Pour l’architecte, la conséquence pratique est identique — *la disparition ou le revirement stratégique du créateur ne fait plus disparaître le protocole*.

*L’arrangement d’un des trois protocoles a changé le 17 août 2026 (constat du 23 octobre) : le protocole agent-agent est passé de la faîtière directe à la* ***fondation dédiée**. La couche d’infrastructure n’a pas été revérifiée.* Encore faut-il préciser ce que « quitter l’entreprise fondatrice » recouvre, car c’est ici que se joue la valeur du transfert pour une institution réglementée. Le socle documente un élément décisif : le protocole agent-agent a été versé **sous licence permissive**, irrévocable, assortie d’une concession expresse de brevets.

Cette précision, d’apparence technique, porte une **garantie juridique concrète**. L’institution qui construit sur ce protocole n’obtient pas seulement la *probabilité* qu’il survive à son créateur ; elle obtient le **droit opposable** de continuer à l’utiliser, de le modifier, et — dans l’hypothèse la plus défavorable — d’en poursuivre elle-même le développement si la fondation venait à l’abandonner. C’est exactement le type de garantie qu’un dossier de risque de tiers cherche à établir, et que nulle assurance contractuelle d’un éditeur ne procure au même degré.

Lecture de l’auteur — le passage sous fondation neutre transforme la nature de la question posée en diligence raisonnable. Devant un protocole propriétaire, l’institution doit évaluer la solidité financière, la stratégie et les intentions d’une entreprise : un exercice de **prospective**. Devant un protocole sous licence permissive et gouvernance multipartite, elle évalue la vitalité d’un projet et la robustesse de ses règles : un exercice de **constat**. Le socle ne l’établit pas ; il en fournit les éléments — transfert d’intendance, licence, composition du comité.

Le comité de pilotage technique du protocole agent-agent mérite l’examen le plus attentif, parce que c’est le lieu où se décide concrètement l’évolution. Le socle en documente la **composition** : huit organisations, dont les trois grands fournisseurs d’infonuagique publique (AWS, Google Cloud, Microsoft) ensemble, alors qu’ils sont concurrents frontaux sur à peu près tout le reste — et le créateur du protocole au même titre que les sept autres.

Lecture de l’auteur — une instance où siègent huit organisations concurrentes, dont aucune n’est le créateur en position dominante, offre à un tiers évaluateur une garantie **qualitativement différente** de celle d’un comité consultatif convoqué par un éditeur. Le socle établit une **composition**, non un **règlement intérieur** : ni la répartition des droits de vote, ni les règles de décision. L’inférence porte sur la structure, pas sur la procédure, et elle mérite d’être vérifiée par toute institution qui en ferait un argument de dossier.

La présence, à ce comité, de l’organisation qui portait l’ACP protocolaire illustre le mécanisme de la consolidation mieux qu’aucune déclaration d’intention : elle n’y est pas arrivée par adhésion, mais par fusion. En **mai 2025**, elle présentait encore son protocole comme complémentaire du protocole agent-outil ; trois mois plus tard, elle en versait les actifs, arrêtait le développement, et sa responsable entrait au comité de pilotage de l’absorbant. *Un concurrent déclaré est devenu un codécideur* — trajectoire inverse de la fragmentation que le domaine redoutait, jouée en un trimestre.

De cet épisode découle une règle de rédaction qui vaut pour toute la somme : l’ACP protocolaire ne doit jamais être présenté comme un standard vivant. Son développement actif a cessé ; il ne subsiste qu’à travers le protocole absorbant et des adaptateurs.

Ce qui frappe enfin, c’est la régularité des trajectoires : quatre mois pour la couche d’infrastructure, deux pour le protocole agent-agent, treize pour le protocole agent-outil — le plus lent des trois. Aucun des trois protocoles nés propriétaires n’est demeuré propriétaire au-delà de treize mois (l’ACP protocolaire, né sous l’égide de la Linux Foundation, n’entre pas dans ce décompte). Lecture de l’auteur — on peut y lire une conviction partagée du secteur : dans un domaine où la valeur naît de l’interconnexion, la propriété exclusive d’un protocole détruit plus de valeur qu’elle n’en capte. Le socle ne l’établit pas.

### 7.4.2 Les fondations neutres : l’Agentic AI Foundation (Linux Foundation) et la FIDO Alliance

Le passage d’un protocole du contrôle de son auteur vers une fondation neutre est, dans l’histoire de l’interopérabilité, le signal de maturation le plus fiable (ch. 1 § 1.2.2).

La première fondation dédiée — l’**Agentic AI Foundation** (AAIF), constituée sous la **Linux Foundation** — accueille **au même endroit** le protocole agent-outil (MCP), l’environnement d’exécution d’agents `goose` et le format de configuration d’agent `AGENTS.md` (ch. 5 § 5.1.4), c’est-à-dire des contributions de **fournisseurs directement concurrents** (Anthropic, Block, OpenAI). Le mécanisme de la faîtière — comité technique de pilotage, charte de neutralité — découple la spécification de tout acteur unique, et c’est ce découplage institutionnel qui **rend crédible** la politique de dépréciation formelle du ch. 8 § 8.3. L’analogie volontiers invoquée est celle du « playbook Kubernetes/CNCF » (*Cloud Native Computing Foundation*) : un projet d’éditeur dominant, donné tôt à une fondation, attire des contributeurs concurrents précisément parce que sa neutralité est garantie. *Depuis le 4 juin 2026 pour le mandataire ouvert* `agentgateway` *(ch. 37 § 37.3) et depuis le 17 août 2026 pour le protocole agent-agent (A2A), l’AAIF héberge également ces deux composants (§ 7.4.1).*

Une seconde fondation, la **FIDO Alliance**, spécialisée dans l’authentification, prend une importance qui s’instruira au ch. 10 : le **28 avril 2026**, un billet officiel de Google Cloud (`S-090` **[A]**) a annoncé le transfert de gouvernance du **protocole de transaction** (AP2, version v0.2, cas *Human-Not-Present*) vers la FIDO Alliance.

*Cette annonce est portée par le Vol. I Monographie § 3.13.1 (et confirmée en [A] à la source primaire sous S-090), tandis que le socle du Vol. II constate à trois mois (et lors de la vérification du 23 octobre 2026) que le transfert n’est pas encore matérialisé sur le dépôt d’origine (S-091 [B, degré 1])*. Les deux énoncés sont **compatibles** — annonce officielle d’avril 2026 d’un côté, transfert non encore matérialisé à la revalidation de l’autre —, et le **ch. 10 § 10.1.3** en instruit le détail.

## 7.5 Encadré de désambiguïsation : la collision « (agentic) control plane » à quatre branches

*SIÈGE DE CET ENCADRÉ POUR TOUTE LA SOMME.* Cet encadré est posé ici une seule fois. Le ch. 10, qui reçoit par ailleurs le chapitre source du Vol. II dont il provient, y renvoie sans le reconstruire.

Le sigle **« ACP »** désigne au moins quatre objets distincts dans ce volume (auxquels s’ajoute l’*Agentic Commerce Protocol* au ch. 10 § 10.3.2), et l’ouvrage ne l’emploie jamais nu. Chaque emploi porte son qualificatif complet. *« Distincts » ne veut pas dire « tous vivants » : la branche (a) a cessé d’être un standard vivant, et la table le dit.* (le Tableau 7.3)

***Tableau 7.3** — Les quatre branches de la collision « ACP » / « (agentic) control plane », et le statut de chacune.*

|  | **Objet** | **Statut** |
| --- | --- | --- |
| **(a)** | **l’ACP protocolaire** — *Agent Communication Protocol* d’IBM Research et BeeAI | fusionné dans le protocole agent-agent en août 2025 ; n’est plus un standard vivant |
| **(b)** | l’**Agentic Control Plane** d’un consortium d’institutions financières et de télécommunications | programme annoncé en juillet 2026 ; traité au Livre III |
| **(c)** | l’expression **agentic control plane** employée par **IBM** pour positionner un produit d’orchestration | positionnement commercial, à attribuer à IBM à chaque occurrence ; traité au Livre III |
| **(d)** | la **composante ACP** de la couche d’infrastructure agentique | ni intitulé complet ni identité établis — voir la lacune ci-dessous |

Le socle n’établit l’absence de lien que pour un seul de ces couples, et il faut être précis sur ce que « distincts » recouvre. Une entrée du socle du Vol. II pose que l’*Agentic Control Plane* du consortium **n’a aucun lien** avec l’ACP protocolaire — **pure homonymie**, et c’est un **fait négatif établi**. Sur le couple **(a)/(c)**, en revanche, le socle ne dit rien de tel, et le silence mérite d’être relevé plutôt que comblé : ce sont **deux objets d’IBM**, et rien n’établit qu’ils soient étrangers l’un à l’autre — ni qu’ils soient liés. C’est une **absence de documentation**, non un fait négatif vérifié.

Lacune héritée, portée et non comblée. La **quatrième branche (d)** est relevée lors de la rédaction du chapitre source : le socle mentionne une « composante ACP » propre à la couche d’infrastructure, dont des **analyses tierces** relèvent un chevauchement avec le protocole agent-agent. Le socle n’établit ni son intitulé complet, ni son identité — ou sa non-identité — avec l’ACP protocolaire. En l’absence de source primaire, la somme **ne tranche pas** : elle désigne cet objet par « la composante ACP de la couche d’infrastructure », **toujours qualifié**, et s’interdit de l’agréger aux trois autres.

Cette lacune est portée ici, encadrée, et renvoyée au ch. 49 pour son état final. Elle n’est pas comblée — et la combler par une analyse tierce serait précisément la faute que l’ouvrage proscrit : *aucune lacune déclarée ne se comble par une source de moindre qualité* (la Figure 7.5).

***Figure 7.5** — Les quatre branches de la collision « ACP » / « (agentic) control plane », et le statut de chacune.*

## 7.6 Lecture critique des métriques d’adoption : « soutien » n’est pas « production »

Il reste à examiner les chiffres par lesquels ces protocoles annoncent leur réussite, et à le faire avec une sévérité que la littérature promotionnelle ne s’impose pas.

Les données disponibles sont les suivantes, et chacune est attribuée à sa source, comme elle doit l’être à chaque occurrence. En **avril 2026**, la Linux Foundation — fondation faîtière des deux protocoles — annonce que plus de 150 organisations déclarent leur soutien au protocole agent-agent, contre plus de 50 au lancement. Un communiqué de la Linux Foundation du 29 juillet 2025 fait état de plus de 65 entreprises déclarant leur soutien à la couche d’infrastructure.

*Ces deux chiffres ne se rapprochent pas* : plus de huit mois les séparent, et le socle n’enregistre **aucune actualisation ultérieure** du second. Les comparer serait fautif.

Ces chiffres sont réels, datés, adossés à des communiqués officiels. Ils sont aussi — et c’est là tout le problème — **auto-déclarés**.

Trois réserves s’imposent, par ordre de gravité croissante.

La première : la notion même d’« organisation de soutien » n’est définie nulle part. Elle ne distingue pas l’entreprise qui a inscrit son logo sur une page d’annonce de celle qui a affecté une équipe d’ingénierie au protocole pendant un an. *Une métrique dont l’unité n’est pas définie ne mesure rien de vérifiable* ; elle indique une **direction**, pas une **grandeur**. Un responsable de la conformité qui recevrait un tel chiffre à l’appui d’une décision d’architecture serait fondé à demander ce qu’on y a compté — et ne trouverait pas la réponse dans la source.

La deuxième : le soutien déclaré ne vaut pas déploiement en production. C’est la réserve centrale, et elle traverse toute la somme. Un architecte qui lirait le chiffre annoncé par la Linux Foundation en avril 2026 comme « 150 systèmes agentiques interopérables en exploitation » commettrait une erreur de catégorie. Le Livre III établit que le nombre d’institutions financières canadiennes documentant par sources primaires un déploiement agentique se compte sur les doigts de deux mains. *L’écart entre les deux ordres de grandeur — la centaine d’organisations qui déclarent leur soutien à un protocole mondial, la poignée d’institutions qui documentent une mise en production — est l’un des enseignements les plus robustes de la somme.*

La troisième porte sur la croissance elle-même. Le passage de plus de 50 à plus de 150 organisations en douze mois, tel que la Linux Foundation le rapporte en avril 2026, est un triplement apparent. Mais un triplement d’une grandeur non définie reste non défini. La progression établit qu’un nombre croissant d’organisations jugent utile d’associer publiquement leur nom au protocole : information sur la **dynamique** du domaine, non sur sa **maturité technique**.

Faut-il pour autant écarter ces chiffres ? Non — et il serait malhonnête de le faire. Ils constituent le meilleur indicateur public disponible de **l’attention** que le secteur porte à ces protocoles, et cette attention est elle-même un fait pertinent pour une institution qui évalue le risque de pérennité d’un standard. Un protocole auquel la Linux Foundation recense plus de 150 organisations déclarant leur soutien bénéficie d’un indice d’attention publique élevé du secteur ; *c’est exactement ce que ces chiffres établissent, sans garantir ni une durée de survie chiffrée ni une maturité de production.*

Le lecteur exigeant en retiendra la portée exacte. La composition du comité de pilotage technique — huit organisations concurrentes — est un indicateur de gouvernance **nettement plus solide** que le décompte des soutiens : ses membres sont **nommés**, leur engagement est **vérifiable** dans les dépôts publics, et leur nombre restreint interdit la comptabilité complaisante. *Quand la somme devra juger de la pérennité d’un protocole, elle regardera qui décide, non combien applaudissent.*

Ce que ce chapitre établit — trois acquis pour la suite du mouvement.

*(1)* La couche protocolaire agentique est sortie du régime propriétaire : aucun des quatre protocoles retenus ici n’est gouverné par son créateur seul. La restriction s’étend au protocole de transaction, mais par une seconde fondation — la **FIDO Alliance**, vers laquelle son transfert a été annoncé le **28 avril 2026** (Vol. I *Monographie* § 3.13.1 et billet officiel `S-090` **[A]** ; transfert non encore matérialisé au relevé `S-091` **[B, degré 1]**, ch. 10 § 10.1.3). Pour la thèse, la conséquence est une précision, non une révision : la couche protocolaire est sortie du régime propriétaire par plusieurs fondations distinctes, organisées par axe, non par une seule.

*(2)* La consolidation ne s’est pas faite par coexistence polie mais par fusion réelle.

*(3)* Les métriques publiées mesurent l’attention, non la production.

Ce que ce chapitre ne dit pas mérite d’être énoncé aussi clairement. Il ne dit pas que ces protocoles sont **sûrs** : la gouvernance neutre ne préjuge en rien de la robustesse d’une implémentation, et le ch. 11 expose les surfaces d’attaque que le socle **nomme** — sans en dater la documentation ni en établir la mécanique. Il ne dit pas que les protocoles agent-outil et agent-agent soient interchangeables ni concurrents : le ch. 8 § 8.6 examine la doctrine de complémentarité qui les articule, et par qui elle est déclarée. Il ne dit pas enfin que la neutralité de la gouvernance **suffise** à emporter la décision d’une institution réglementée — c’est l’objet du Livre III que d’établir tout ce qu’il faut y ajouter.

*La consolidation protocolaire est le point de départ du mouvement. Elle n’en est pas la conclusion.*
