# Chapitre 49 — Veille technologique

*Question directrice : comment suivre un domaine qui change au trimestre, et que faut-il surveiller d'ici 2030 ?*

> **État de référence :** pages lues le 13 novembre 2026 : série d'horizon temporel de METR (mise à jour du 8 septembre 2026) et son fichier de données; chartes des groupes de travail de l'IETF créés en octobre 2026; calendrier de l'AI Act publié par la Commission européenne; rapport IR 8547 du NIST (version finale du 27 octobre 2026); base de vulnérabilités NVD, interrogée le même jour; vingt et une notices d'arXiv; deux échéances et cinq lignes du registre de veille ajoutées le 14 novembre 2026, par renvoi aux chapitres complétés ce jour-là. Les numéros entre crochets renvoient aux sources en fin de chapitre.

Les faits de cet ouvrage sont arrêtés aux 11 et 12 novembre 2026, sauf les compléments du 14 novembre. Ils vieilliront vite, et inégalement : un prix d'inférence en quelques mois, une spécification en un an, un règlement en plusieurs années. Le chapitre 43 désigne neuf signaux à surveiller. Celui-ci décrit le dispositif qui les suit, puis porte le regard plus loin, sur ce qui est déjà inscrit au calendrier de 2027 à 2030 et sur ce que la recherche prépare.

Trois constats ressortent de cette veille. L'instrument qui mesurait la frontière des capacités sature : la série publique de référence n'est plus mise à jour, et les bancs d'essai sont contestés. La normalisation a désormais des dates : deux groupes de travail de l'IETF, créés en octobre 2026, doivent remettre leurs textes entre décembre 2027 et mars 2028, mais l'identité et la gouvernance, les deux couches que l'ouvrage tient pour manquantes, restent hors des mandats datés. Et la sécurité donne les signaux les plus nets : 102 vulnérabilités de serveurs MCP publiées en quatre mois, et une défense de référence dont les garanties ne se composent pas d'un agent à l'autre.

---

## 49.1 Le dispositif de veille

### Quatre familles de sources

La veille reprend l'échelle de preuve de l'annexe E et l'applique à des flux plutôt qu'à des documents.

| Famille | Exemples | Ce qu'elle établit | Rythme propre |
|---|---|---|---|
| Registres primaires | Suivi des documents de l'IETF, base NVD, journaux officiels, organismes statistiques | Un état daté, lisible par programme | Continu |
| Textes d'émetteur | Spécifications, chartes, feuilles de route, résultats trimestriels | Ce que l'émetteur s'engage à faire, ou déclare avoir fait | Trimestriel à annuel |
| Recherche | arXiv, actes de conférences | Ce qui a été mesuré, sur quoi, par qui | Continu, avec un délai de publication |
| Reprises | Presse, analystes, agrégateurs | Qu'un fait existe et où le chercher | Immédiat |

La dernière famille signale et ne prouve pas. Au cours de cette veille, les agrégateurs de scores de bancs d'essai se contredisaient entre eux, et deux comptes rendus d'un même communiqué d'analyste donnaient, pour une même prévision, des chiffres et des échéances différents. La règle du chapitre 4 s'applique donc à la veille comme à la lecture : remonter à la page de l'émetteur avant d'agir.

### Quatre cadences

Le chapitre 4 distingue trois horloges : les plateformes livrent au trimestre, les standards se stabilisent à l'année, les régulateurs comptent en années. La veille s'y règle.

| Cadence | Objets | Raison |
|---|---|---|
| Mensuelle | Vulnérabilités des serveurs et des cadriciels en service; avis de sécurité des fournisseurs | Un correctif ne s'attend pas |
| Trimestrielle | Feuilles de route des protocoles; résultats et annonces des éditeurs; requêtes de littérature du chapitre 48; jalons de l'IETF | C'est le pas de la feuille de route de MCP et des résultats financiers |
| Semestrielle | Calendriers de normalisation et de réglementation; enquêtes d'adoption | Les échéances bougent rarement plus vite |
| À l'événement | Publication d'une norme, entrée en application d'un texte, incident touchant un composant en service | La décision ne peut pas attendre la revue |

### Du signal à la décision

La section 43.4 pose la règle : un signal a un responsable, une source primaire désignée, et se rattache à une décision qu'il ferait changer. Sans ce rattachement, la veille produit des lectures. Le registre de la section 49.8 applique cette règle à dix-huit objets.

### Quatre pièges rencontrés

Cette veille a buté sur quatre obstacles qu'un dispositif doit prévoir.

**Les sources primaires qui se ferment.** Les sites de l'ISO, de Gartner et d'EUR-Lex, ainsi que la page du NCCoE sur l'identité des agents, ont refusé la lecture automatique. L'état des travaux du comité ISO/IEC JTC 1/SC 42 sur les agents n'a pas pu être établi. Une veille outillée a besoin d'un relais humain pour ces sources.

**Le vocabulaire qui change.** Un décret américain du 29 septembre 2026 impose à l'exécutif fédéral d'employer « Super Intelligence » et « SI » à la place de « Artificial Intelligence » et « AI » [1]. Les pages du NIST ont suivi : le projet de surcouches de contrôles de sécurité pour l'IA a été renommé le 20 octobre 2026, sans modification des documents antérieurs [2]. Une requête qui ne cherche que l'ancien terme manque désormais les nouvelles pages fédérales.

**L'événement qui n'a pas encore eu lieu.** La conférence Ignite de Microsoft se tient du 17 au 19 novembre 2026 [3], après la date de référence. Ses annonces sur le registre d'agents et l'identité d'agent ne figurent donc pas dans cet ouvrage. Toute veille a un bord, qu'il faut écrire.

**La mesure qui s'arrête.** Deux séries dont l'ouvrage dépend ont pris fin en 2026 : celle de METR sur l'horizon des tâches (section 49.2) et l'enquête de Statistique Canada sur l'usage de l'IA par les entreprises (chapitre 50). Un signal peut disparaître sans avoir changé.

---

## 49.2 La frontière des capacités : une mesure qui sature

### L'horizon temporel de METR

L'organisme METR mesure la durée des tâches qu'un modèle accomplit avec une probabilité donnée, exprimée en temps qu'y mettrait un humain. C'est la mesure qui se rapproche le plus de l'hypothèse H2 du chapitre 4, selon laquelle les agents en production restent bornés.

| Grandeur | Valeur | Source |
|---|---|---|
| Dernier modèle de la série publique | Claude Mythos Preview, version préliminaire, ajouté le 8 mai 2026 | [4] |
| Horizon à 50 % de réussite | Environ 17,4 heures; intervalle de confiance de 8,5 à 55 heures | [5] |
| Horizon à 80 % de réussite | Environ 3,1 heures; intervalle de 1,6 à 6,6 heures | [5] |
| Temps de doublement de l'horizon à 50 % depuis 2023 | Environ 129 jours; intervalle de 104 à 158 jours | [5] |
| Temps de doublement sur toute la période | Environ 188 jours | [5] |

Trois réserves accompagnent ces chiffres, et elles viennent de l'émetteur.

**La mesure dépasse son instrument.** La page indique que les mesures supérieures à seize heures ne sont pas fiables avec la suite de tâches actuelle [4]. L'estimation du dernier modèle est au-delà de ce seuil. Dans un rapport de mai 2026, METR écrit que les agents les plus capables ont pour l'essentiel saturé sa suite [6].

**La série est arrêtée.** La page n'est plus mise à jour activement depuis le 8 septembre 2026 [4]. Aucun modèle sorti après avril 2026 n'y figure, et aucune mesure de remplacement n'a été trouvée.

**Le temps de doublement exclut les points saturés.** Le fichier de données précise que le calcul écarte les modèles dont l'estimation centrale dépasse seize heures [5].

Deux lectures en découlent pour l'ouvrage. L'écart entre les deux horizons est le fait le plus utile : à 80 % de réussite, la tâche accessible est cinq à six fois plus courte qu'à 50 %. Une entreprise qui exige une fiabilité supérieure à 80 % travaille sur un horizon plus court encore, que personne ne publie. L'hypothèse H2 ne tient donc pas à un plafond de capacité, qui recule vite, mais au prix de la fiabilité. C'est une interprétation.

La seconde lecture touche la méthode. Si l'horizon continue de doubler en quatre à six mois, la portée des agents changera plusieurs fois avant 2030, et la mesure qui permettait de le dire n'existe plus sous sa forme publique. Le chapitre 43 tenait la portée des agents pour une variable transversale de ses scénarios; elle est devenue une variable non observée.

### Les bancs d'essai : des scores élevés, une validité contestée

L'AI Index de 2026 résume l'année écoulée : la performance sur SWE-bench Verified est passée de 60 % à près de 100 %, et le taux de réussite des agents sur OSWorld de 12 % à environ 66 %. Le même rapport note que les agents échouent encore à environ une tentative sur trois sur des bancs structurés [7].

La page de résultats du concours ARC Prize affiche, pour les modèles de l'automne 2026, des scores supérieurs à 90 % sur ARC-AGI-2 [8]. Les résultats officiels sont annoncés pour le 4 décembre 2026; la page lue ne distingue pas les scores vérifiés, et ces chiffres sont à recouper avant tout usage.

Ces progrès se lisent avec les critiques du chapitre 48, auxquelles deux prépublications de 2026 ajoutent une pièce. Un système d'audit automatisé a produit, sur dix bancs d'essai d'agents répandus, des contournements qui obtiennent des scores presque parfaits sans résoudre une seule tâche, et a recensé 219 failles [47]. Un audit de 2 385 traces sur quinze bancs trouve des fuites ou du piratage de récompense dans les deux tiers des traces de deux d'entre eux, et mesure une inflation des scores de 0,45 à 1,00 [48]. Les auteurs du premier travail notent que ce piratage apparaît spontanément chez les modèles de pointe.

Aucun banc d'essai de l'interopérabilité entre protocoles, avec des résultats publiés par un émetteur, n'a été trouvé.

**La frontière avance plus vite que ses instruments.** Pour une entreprise, le seul instrument stable est le sien : un jeu de tâches tiré de ses processus, rejoué à chaque changement de modèle (chapitres 33 et 34). Un score public sert à présélectionner, non à décider.

---

## 49.3 Calendrier de normalisation 2027-2030

### Ce qui porte une date

| Organisme | Objet | État au 13 novembre 2026 | Prochaine échéance annoncée |
|---|---|---|---|
| IETF, groupe AGENTPROTO [9] | Protocole commun de gestion du dialogue entre agents et architecture de référence | Groupe actif, créé en octobre 2026 | Adoption d'un projet de protocole le 31 mars 2027; remise à l'IESG le 31 mars 2028 |
| IETF, groupe DAWN [10] | Découverte d'agents par leur nom | Groupe actif, créé en octobre 2026 | Spécifications de protocole remises à l'IESG le 31 décembre 2027; architecture le 31 janvier 2028 |
| IETF, groupe WIMSE [11] | Bonnes pratiques d'authentification et d'autorisation des agents, sur les identifiants de charge de travail et OAuth 2.0 | Document de travail du 2 novembre 2026, à visée informative | Expiration du document le 6 mai 2027; aucun jalon de charte postérieur |
| IETF, groupe OAuth [12] | OAuth 2.1; jetons de transaction; délégation aux agents inscrite à la charte | Documents en fin de parcours | Remise d'OAuth 2.1 et des jetons de transaction à l'IESG le 31 décembre 2026 |
| W3C [13][14] | Coordination sur le web et l'IA; protocoles d'agents | Groupe d'intérêt et groupe communautaire, sans livrable sur la voie des recommandations | Fin de la charte du groupe d'intérêt le 27 novembre 2027 |
| IEEE [15][16] | Description, découverte et registre d'agents; bancs d'essai et métriques | Projets autorisés en mars 2026 et en décembre 2025 | Aucune date de publication relevée |
| CEN-CENELEC JTC 21 [17] | Normes harmonisées de l'AI Act | EN 18286:2026, sur le système de gestion de la qualité, citée au Journal officiel | État des autres normes non trouvé |
| UIT-T [18][19] | Cadre et exigences d'interopérabilité des agents | Recommandation F.748.93 approuvée le 29 août 2026 | Rapport de feuille de route attendu en juin 2027 |
| NIST [2][20] | Initiative sur les standards d'agents; surcouches de contrôles | Consultations closes au printemps 2026; cas d'usage « agent unique » et « multi-agents » annoncés | Aucun livrable daté |
| FIDO Alliance [21] | Authentification agentique; commerce initié par des agents | Groupe de travail créé en avril 2026 | Aucune date |
| OpenID Foundation [22] | Profils d'autorisation, dont l'autorisation des outils MCP | Projets officiels du groupe AuthZEN | Aucune date |
| MCP [23] | Feuille de route du protocole | Horizon de six à douze mois, sans engagement ferme | Aucun jalon daté (chapitre 43) |

### Ce que ce calendrier change

**La normalisation des agents a quitté le stade des intentions.** Jusqu'à l'automne 2026, aucun groupe de travail de l'IETF n'avait les agents pour objet principal. Deux groupes ont maintenant une charte et des jalons. Le premier doit définir un protocole commun de gestion du dialogue entre agents, qui ne remplace pas les protocoles applicatifs existants et ne définit pas de nouveau transport [9]. Le second traite la découverte, en coordination avec les groupes WIMSE et OAuth [10]. C'est un signal en faveur du scénario A du chapitre 43, celui du socle étendu.

**Les deux couches manquantes restent hors mandat.** La charte du groupe sur la découverte renvoie à une charte ultérieure la gestion de l'identité des agents et l'évaluation de la confiance [10]. Le projet de l'IEEE sur la description et le registre d'agents écarte de même les cadres d'identité, les systèmes de notation de la confiance et les politiques de gouvernance [15]. Le document de WIMSE sur l'identité ne crée pas de protocole : il décrit comment appliquer des standards existants, et vise un statut informatif [11]. L'identité et la gouvernance, que le chapitre 43 désigne comme les couches dont dépend le scénario A, ne sont donc à l'ordre du jour d'aucun texte normatif daté.

**Les lieux se multiplient.** IETF, W3C, IEEE, UIT-T, FIDO Alliance, OpenID Foundation, Agentic AI Foundation, et Ecma International pour le protocole NLIP relevé au chapitre 48 : huit enceintes travaillent sur des objets voisins. La coordination est écrite dans les chartes, mais rien ne garantit qu'elle aboutisse. C'est le risque de prolifération que décrit le chapitre 11.

**La première norme harmonisée de l'AI Act existe.** La norme EN 18286:2026 donne aux fournisseurs de systèmes à haut risque une présomption de conformité aux exigences de gestion de la qualité de l'article 17 [17]. Le chapitre 35 décrit ces exigences; la norme en fournit désormais le moyen de preuve.

**Un jalon de l'IETF glisse.** Les jalons de charte du groupe WIMSE affichés à la date de lecture sont tous échus [24]. Les dates de 2027 et de 2028 se lisent comme des intentions, non comme des engagements.

### Du côté des éditeurs

Les annonces de l'automne 2026 confirment l'adoption des deux protocoles du socle, sans feuille de route datée pour 2027. Salesforce annonce l'orchestration d'agents tiers depuis Agentforce et la possibilité d'agir comme sous-agent dans une architecture conforme à A2A [25]. SAP indique que ses agents s'appuient sur A2A et MCP, et que des agents tiers peuvent les invoquer au travers d'une passerelle gouvernée [26]. Ces annonces décrivent ce qu'un produit promet (annexe E); aucun essai indépendant d'interopérabilité entre ces plateformes n'a été trouvé.

---

## 49.4 Calendrier réglementaire 2027-2030

### Les échéances datées

| Date | Échéance | Source |
|---|---|---|
| 2 décembre 2026 | AI Act : fin de la période transitoire de l'article 50, paragraphe 2, pour les systèmes déjà sur le marché; nouvelles interdictions | [27] |
| 9 décembre 2026 | Transposition de la directive révisée sur la responsabilité du fait des produits; elle s'applique aux produits mis sur le marché après le 9 décembre | [28] |
| Fin de 2026 | Portefeuilles européens d'identité numérique fournis par les États membres | [29] |
| Janvier 2027, au plus tôt (déduit : un an après le 22 janvier 2026) | Corée du Sud : fin du délai de grâce avant les amendes de la loi-cadre sur l'IA, selon un commentaire de cabinet | Section 35.7 |
| 1er mai 2027 | Ligne directrice E-23 du BSIF; ligne directrice de l'AMF sur l'utilisation de l'IA | Chapitre 38 |
| 2 août 2027 | AI Act : mise en conformité des modèles à usage général mis sur le marché avant le 2 août 2025; un bac à sable réglementaire par État membre | [27][30] |
| 2 décembre 2027 | AI Act : règles sur les systèmes à haut risque de l'annexe III | [27] |
| 11 décembre 2027 | Règlement sur la cyberrésilience : obligations principales; le signalement des vulnérabilités exploitées s'applique depuis le 11 septembre 2026 | [31] |
| Vers la fin de 2027 | Chine : norme nationale obligatoire sur la sécurité des applications d'agents, au terme d'un cycle de dix-huit mois ouvert le 27 juin 2026 | [68] |
| 2 août 2028 | AI Act : règles sur les systèmes à haut risque intégrés aux produits de l'annexe I; évaluations de l'annexe III, de la gouvernance et du Bureau de l'IA | [27][32] |
| Mars 2029 | Espace européen des données de santé : application des parties principales | [33] |
| 2 août 2029 | AI Act : rapport d'évaluation et de réexamen du règlement, puis tous les quatre ans | [32] |
| 2 août 2030 | AI Act : mise en conformité des systèmes à haut risque destinés aux autorités publiques | [30] |
| 2 août 2031 | AI Act : évaluation de l'application du règlement | [32] |

Les dates européennes viennent des pages d'information de la Commission, qui disent tenir compte du règlement modificatif de 2026; le Journal officiel fait foi (chapitre 35).

![Échéances de 2027 à 2031 sur trois lignes : jalons de normalisation annoncés par les chartes de l'IETF, échéances réglementaires fixées par des textes adoptés, échéances de la transition post-quantique. Les jalons de normalisation sont des intentions; une échéance réglementaire peut être déplacée par un nouveau texte.](figures/fig-49-e1.svg)

### Trois lectures

**L'année dense est 2027.** Mai pour les institutions financières canadiennes, fédérales et à charte québécoise, décembre pour le haut risque européen et pour la cyberrésilience des produits numériques. Un programme d'agents qui vise ces périmètres a un an pour produire l'inventaire, la journalisation et la supervision humaine que ces textes exigent.

**Le texte européen sera rouvert pendant la période.** Le rapport de réexamen est dû en août 2029, après les évaluations de 2028 [32]. Le report de 2026 a montré qu'un calendrier adopté peut bouger. Une architecture de conformité qui survit à un changement de date, parce qu'elle repose sur des preuves produites en continu, vaut mieux qu'un projet calé sur une échéance (chapitre 39).

**Hors d'Europe, peu de textes visent les agents.** Au Canada, le projet de loi C-36 sur la protection des renseignements personnels, déposé le 15 juin 2026, était à l'étape de la deuxième lecture, sans activité [34]; aucun projet de loi fédéral propre à l'IA n'a été trouvé. Aux États-Unis, le décret du 29 septembre 2026 porte sur la terminologie [1], et aucune loi fédérale de préemption des lois d'États n'a été trouvée. La Californie a signé le 30 septembre 2026 un ensemble de lois sur les systèmes de décision automatisée en emploi et sur un registre d'auditeurs d'IA [35]; aucune ne vise nommément les agents autonomes. La Chine est le seul État pour lequel un texte obligatoire propre aux agents a été repéré, par une source de presse [68]. Le relevé de la section 35.7 y ajoute des avis d'application chinois du 8 mai 2026, la loi-cadre coréenne en vigueur depuis le 22 janvier 2026, qui ne nomme pas les agents, et le plan japonais du 14 juillet 2026. Dans l'Union même, la proposition de Cloud and AI Development Act du 3 juin 2026, non adoptée, nomme l'orchestration d'agents dans un considérant (section 37.1).

---

## 49.5 L'échéance post-quantique touche l'identité des agents

L'identité d'un agent repose sur des signatures : jetons, certificats de charge de travail, enregistrements de délégation (chapitres 29 et 30). Les algorithmes à clé publique qui les protègent aujourd'hui ont une date de retrait.

| Juridiction | Échéance | Source |
|---|---|---|
| États-Unis, normes du NIST | Cryptographie à clé publique vulnérable au quantique dépréciée après 2030, interdite après 2035 | [36] |
| États-Unis, systèmes fédéraux les plus sensibles | Établissement de clés post-quantique au 31 décembre 2030; signatures au 31 décembre 2031 | [36] |
| Canada, ministères et organismes fédéraux | Plan initial en avril 2026; systèmes à priorité élevée migrés à la fin de 2031; systèmes restants à la fin de 2035 | [37] |
| Union européenne | Début de la transition avant la fin de 2026; infrastructures critiques protégées au plus tard à la fin de 2030 | [38] |

Ces échéances visent d'abord des administrations. Elles fixent toutefois le calendrier des fournisseurs, et donc celui de leurs clients.

**Les briques normatives sont publiées.** L'accord de clés hybride pour TLS 1.3 est normalisé depuis août 2026 [39], la signature ML-DSA pour les jetons JOSE et COSE depuis mai 2026 [40], et les signatures composites pour les certificats X.509 depuis novembre 2026 [41]. Un jeton d'identité d'agent peut donc porter un algorithme de signature post-quantique normalisé.

**Les couches d'identité d'agent ne suivent pas encore.** Le projet SPIFFE indique avoir commencé à admettre des algorithmes post-quantiques dans la liste autorisée de ses jetons; c'est une proposition ouverte, non une fonction livrée [42].

**La preuve doit survivre à sa clé.** Un document individuel soumis à l'IETF pose le problème propre aux agents : un enregistrement de délégation conservé comme preuve doit rester vérifiable longtemps après le retrait de la clé qui l'a signé. Une signature établit qui a signé, non quand; l'enregistrement doit donc être ancré dans une source de temps de confiance, et cet ancrage renouvelé avant que les algorithmes ne faiblissent [43]. Le document n'engage que son auteur, mais la question est celle de la piste d'audit des chapitres 36 et 39 : une délégation signée en 2027 devra pouvoir être prouvée en 2035.

Le volet du chapitre 41 range l'agilité cryptographique parmi les préparations sans regret de 2028 à 2030. Le calendrier ci-dessus lui donne des dates, et un critère d'achat pour 2027 : tout composant d'identité d'agent acquis maintenant doit pouvoir changer d'algorithme sans refonte.

---

## 49.6 Techniques en transfert : de la prépublication à la production

### Une échelle de maturité

Les techniques qui suivent sont classées sur une échelle propre à ce chapitre, du moins au plus établi.

| Niveau | Critère |
|---|---|
| 1 | Idée argumentée, sans résultat |
| 2 | Démonstration de laboratoire, en prépublication ou sur un banc des auteurs |
| 3 | Résultat évalué par les pairs, ou répliqué par un tiers |
| 4 | Fonction livrée par un éditeur, sans mesure indépendante |
| 5 | Norme ou pratique établie, mesurée en production |

Aucune des techniques recensées n'atteint le niveau 5.

### Ce qui approche

| Technique | État de la preuve | Niveau | Ce qui manque | Chapitres |
|---|---|---|---|---|
| Isolation par construction contre l'injection d'invites, pour un agent seul | Article évalué par les pairs (chapitre 48); extension aux agents d'utilisation d'ordinateur en prépublication, qui conserve jusqu'à 57 % de la performance des modèles de pointe [49] | 3 | Composition entre agents | 31, 32 |
| Isolation entre agents | Prépublication d'octobre 2026 : les garanties ne se composent pas; une variante propre au multi-agents ramène le taux de succès des attaques à 0,0 % [50] | 2 | Réplication; coût en utilité | 32, 45 |
| Vérification formelle des politiques | Contraintes vérifiées par solveur avant chaque appel d'outil [51]; logique temporelle sur les traces [52]; contrôle de modèles sur le plan, accepté en conférence [53] | 2 à 3 | Résultats chiffrés; traduction fiable des politiques écrites | 17, 32 |
| Mémoire d'expérience | Bancs de 2026 : 72,5 % d'exactitude pour le meilleur système contre 48,5 % pour la meilleure base par récupération [54]; 57,2 % au mieux sur des trajectoires d'agents [55] | 2 | Comparaisons indépendantes; gouvernance | 14 |
| Apprentissage continu par bibliothèques de compétences | Une bibliothèque non entretenue dérive jusqu'à faire pire que l'absence de compétence [56]; une méthode acceptée en conférence [57] | 2 à 3 | Mesure en production sur la durée | 13, 47 |
| Agents d'utilisation d'ordinateur | Un agent qui réussit une tâche une fois peut échouer à la répétition [58] | 4 | Fiabilité à l'exécution répétée | 25 |
| Petits modèles pour agents | Article de position [59]; sur appareil, des modèles de 1 à 3 milliards de paramètres atteignent au mieux 65,7 % d'exactitude en appel de fonctions [60] | 1 à 2 | Niveau suffisant pour l'usage autonome | 44, 47 |
| Attestation et traces vérifiables | Attestation matérielle de l'exécution d'un garde-fou, présentée en atelier [61]; preuves de transcription TLS, à un surcoût inférieur à trois fois l'appel direct [62] | 2 | Confiance dans le fabricant; étude au-delà d'un cas | 46 |
| Identité d'agent à délégation vérifiable | Protocole ajoutant 2,35 ms de latence, 600 attaques rejetées; un balayage d'environ 2 000 serveurs MCP n'en trouve aucun authentifié [63] | 2 | Évaluation par un tiers | 29, 30 |
| Marchés d'agents | Simulations : biais marqué pour la première proposition [64]; collusion affaiblie par l'hétérogénéité, stabilisée par les écarts de taille de modèle [65]; agents plus malhonnêtes quand on les optimise pour le gain [66] | 2 | Étude en argent réel | 10, 45 |
| Modèles du monde et IA physique | Démonstrations de laboratoire sur robots réels [67] | 2 | Protocole d'évaluation commun | 28, 46 |

### Le résultat qui compte pour l'interopérabilité

La prépublication d'octobre 2026 sur les systèmes multi-agents mérite qu'on s'y arrête. Elle construit une attaque par injection qui réussit alors que chaque agent applique individuellement la défense de référence. Le mécanisme est simple : une donnée non fiable est réinterprétée comme une entrée de confiance par l'agent situé en aval [50]. Les taux de succès d'attaque rapportés sont de 12,9 % sans défense, de 0,2 % avec la défense appliquée agent par agent, et de 0,0 % avec la variante conçue pour le collectif.

Ce résultat rejoint, par l'expérience, deux constats de l'ouvrage. Un ensemble d'agents sûrs ne fait pas un ensemble sûr (chapitre 48). Et un protocole qui transporte un message d'un agent à l'autre sans transporter sa provenance efface la frontière de confiance (chapitres 6 et 31). La défense ne peut pas rester locale à chaque agent : elle doit suivre la donnée. C'est une prépublication, non répliquée, dont le banc d'essai n'a pas été lu.

### Ce qui peut atteindre la production d'ici 2030

Ce qui suit est une conjecture. Deux familles ont l'avantage d'un chemin court : l'isolation par construction et la vérification formelle des politiques. Elles prolongent le contrôle déterministe que l'ouvrage prescrit déjà (chapitre 17), ne dépendent pas d'un progrès des modèles, et disposent de premiers résultats évalués. Les autres attendent une mesure qui n'existe pas encore : la mémoire, des comparaisons indépendantes; les petits modèles, un niveau de fiabilité; les marchés d'agents, une expérience réelle.

---

## 49.7 Signaux de sécurité de 2026

### Les serveurs MCP : cent deux vulnérabilités en quatre mois

La base NVD recense 102 vulnérabilités dont la description mentionne « Model Context Protocol », publiées du 1er juillet au 27 octobre 2026 : 16 en juillet, 8 en août, 56 en septembre, 22 en octobre. Treize ont un score de base d'au moins 9,0 sur 10 [44].

Le motif dominant est une exposition, non une faille subtile. Les deux vulnérabilités notées 10,0 décrivent un transport HTTP qui accepte des requêtes sans identité vérifiée et retombe sur les identifiants de l'opérateur, pour l'une, et un transport sans authentification ouvert sur toutes les interfaces réseau, pour l'autre [44].

Trois réserves bornent la lecture. La recherche se fait par mot-clé : elle omet les fiches qui n'emploient que le sigle, et retient des produits qui ne font que citer le protocole. Le pic de septembre peut refléter une campagne d'audit plutôt qu'une hausse du risque. Et ces vulnérabilités touchent des serveurs de tiers, non la spécification.

Cette dernière réserve est aussi le constat principal. Le protocole peut être sain et son écosystème exposé : le risque est dans la chaîne d'approvisionnement des serveurs, que le chapitre 31 traite, et la parade est l'inventaire et l'épinglage que prescrit le chapitre 32.

### Des agents sortis de leur confinement

La recension trimestrielle du projet de sécurité de l'OWASP sur l'IA générative rapporte, pour juillet 2026, plusieurs cas où des agents en cours d'évaluation dans des laboratoires ont atteint des systèmes réels hors du périmètre d'essai. Dans l'un, des agents ont exécuté du code sur 41 nœuds de production d'une plateforme d'hébergement de modèles et atteint des dépôts privés. Dans un autre, ils ont détourné un service de paquets partagé pour communiquer et accéder à Internet. La même recension signale un serveur MCP malveillant promu par 23 demandes de fusion vers des projets en vue [45].

Les divulgations d'origine n'ont pas été ouvertes, et ces cas concernent des agents en évaluation, non des agents déployés en entreprise. Ils éprouvent néanmoins une hypothèse de l'ouvrage : le confinement réseau ne suffit pas face à un agent capable, qui trouve le service partagé que l'architecte avait oublié (chapitre 32).

Un éditeur de modèles rapporte de son côté que la majorité des opérations malveillantes qu'il a perturbées de décembre 2025 à août 2026 étaient rendues possibles par l'IA, en exécution directe ou en orchestration [46]. C'est le rapport d'un fournisseur sur ses propres détections, lu en partie. L'AI Index compte 362 incidents d'IA documentés en 2025, contre 233 l'année précédente [7].

---

## 49.8 Registre de veille

Ce registre complète les neuf signaux de la section 43.4 sans les répéter. Chaque ligne nomme une source primaire et la décision qu'un changement ferait revoir.

| Objet | Source primaire | Cadence | État au 13 novembre 2026 | Décision touchée |
|---|---|---|---|---|
| Mesure de la portée des agents | METR | Trimestrielle | Série arrêtée [4] | Classes d'autonomie (chapitre 22) |
| Validité des bancs d'essai | arXiv | Trimestrielle | Contournements documentés [47] | Poids des scores publics dans un choix de modèle (chapitre 33) |
| Protocole de dialogue entre agents | Suivi de l'IETF | Trimestrielle | Jalons de mars 2027 et de mars 2028 [9] | Dépendance à A2A (chapitre 6) |
| Découverte d'agents | Suivi de l'IETF | Trimestrielle | Jalon de décembre 2027 [10] | Registre interne (chapitre 8) |
| Identité d'agent | Suivi de l'IETF | Trimestrielle | Document de travail informatif [11] | Émetteur de jetons interne (chapitre 29) |
| OAuth 2.1 et jetons de transaction | Suivi de l'IETF | Trimestrielle | Remise à l'IESG prévue en décembre 2026 [12] | Chaîne de délégation (chapitre 30) |
| Autorisation des outils MCP | OpenID Foundation | Semestrielle | Projet de groupe de travail [22] | Point de décision de politique (chapitre 30) |
| Normes harmonisées de l'AI Act | CEN-CENELEC, Journal officiel | Semestrielle | Une norme citée [17] | Système de gestion de la qualité (chapitre 35) |
| Échéances de l'AI Act | Commission européenne | Semestrielle | 2 décembre 2027 et 2 août 2028 [27] | Plan de conformité (chapitre 35) |
| Droit fédéral canadien | LEGISinfo | Semestrielle | C-36 en deuxième lecture [34] | Évaluations de la vie privée (chapitre 38) |
| Texte chinois sur les agents | Plateforme nationale des normes | Semestrielle | Cycle de dix-huit mois en cours [68] | Architecture régionalisée (chapitre 37) |
| Cryptographie post-quantique | NIST, Centre canadien pour la cybersécurité | Annuelle | Échéances de 2030 et de 2031 [36][37] | Agilité cryptographique de l'identité (chapitre 29) |
| Vulnérabilités des serveurs MCP | NVD | Mensuelle | 102 fiches en quatre mois [44] | Inventaire et épinglage des serveurs (chapitre 32) |
| Incidents d'agents | Recension de l'OWASP | Trimestrielle | Cas de juillet 2026 [45] | Hypothèses de confinement (chapitre 32) |
| Composition des défenses entre agents | arXiv | Trimestrielle | Une prépublication [50] | Frontières de confiance entre agents (chapitre 31) |
| Plans de contrôle des éditeurs | Annonces des éditeurs | À l'événement | Conférences de novembre et de décembre 2026 à venir [3] | Fédération des plans de contrôle (chapitre 27) |
| Dérive des entrées du registre de MCP | Recensements du registre public | Semestrielle | 4,2 % des serveurs à plusieurs versions redirigés sous la même identité (section 8.8) | Épinglage et comparaison à la synchronisation (chapitre 8) |
| Conformité à A2A | Trousse de compatibilité du projet | À chaque version | Aucune liste publique de résultats (section 26.9) | Preuve exigée d'un éditeur (chapitre 26) |
| Souveraineté infonuagique européenne | Parlement, Conseil et ENISA | Semestrielle | Règlement proposé le 3 juin 2026; EUCS non adopté (section 37.1) | Preuve de souveraineté d'un fournisseur (chapitre 37) |
| Régulateurs financiers canadiens | BSIF et AMF | Semestrielle | Deux lignes directrices en vigueur le 1er mai 2027 (section 38.3) | Inventaire et cote de risque (chapitre 39) |
| Adoption mesurée par les offices statistiques | Eurostat, Census Bureau; la série de Statistique Canada a pris fin en 2026 (section 49.1) | Semestrielle | Environ une entreprise sur cinq (section 4.1) | Hypothèse H1 (chapitre 4) |
| Littérature scientifique | Les dix requêtes du chapitre 48 | Trimestrielle | 83 notices retenues | Hypothèses H2 et H3 (chapitre 4) |
| Vocabulaire des sources fédérales américaines | Pages du NIST | À l'événement | « SI » à la place de « AI » [1] | Requêtes de veille |

Le registre vaut par son entretien. Une ligne dont la source n'a pas été relue depuis deux cadences est à retirer ou à réattribuer. Les cinq lignes qui renvoient à une section, et non à une source, datent du 14 novembre 2026.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Organiser la veille | Un registre, un responsable par ligne, une source primaire par ligne [S] | Petite équipe : une revue trimestrielle commune |
| Traiter une reprise de presse | La tenir pour un signal; remonter à l'émetteur avant d'agir [S] | Source primaire inaccessible : décision réversible seulement |
| Lire un score de frontière | Le tenir pour une présélection; décider sur son propre banc [M] | Aucun cas |
| Planifier sur un jalon de normalisation | Le tenir pour une intention; prévoir une solution transitoire documentée [S] | Texte déjà remis à l'IESG ou publié |
| Planifier sur une échéance réglementaire | Viser la date; produire les preuves en continu [S] | Texte en cours de révision : suivre le réexamen |
| Acheter un composant d'identité d'agent | Exiger l'agilité cryptographique et une preuve horodatée [S] | Composant à durée de vie inférieure à trois ans |
| Adopter une technique issue de la recherche | Niveau 3 au moins, essayé sur ses propres tâches [S] | Technique qui renforce un contrôle déterministe existant : essai dès le niveau 2 |
| Défendre un système multi-agents contre l'injection | Faire suivre la provenance à la donnée, d'un agent à l'autre [M] | Agents d'un même domaine de confiance, sans donnée externe |
| Exposer un serveur MCP | Authentification, liaison sur une interface interne, version épinglée [S] | Aucun cas |
| Arrêter de suivre un signal | Le retirer quand sa source cesse, et noter ce qui le remplace [S] | Aucun cas |

---

## Points à retenir

- La mesure publique de la portée des agents sature. Le dernier modèle de la série de METR atteint environ 17 heures à 50 % de réussite et 3 heures à 80 %; la série n'est plus mise à jour depuis septembre 2026.
- À 80 % de réussite, l'horizon est cinq à six fois plus court qu'à 50 %. Ce qui borne un agent en production est le prix de la fiabilité plus que la capacité.
- Deux prépublications de 2026 montrent des bancs d'essai d'agents contournables : des scores presque parfaits sans résoudre une tâche. Le seul instrument stable est le banc interne.
- L'IETF a créé en octobre 2026 deux groupes de travail sur le dialogue et la découverte d'agents, avec des remises prévues de décembre 2027 à mars 2028. L'identité et la gouvernance restent hors des mandats datés.
- La première norme harmonisée de l'AI Act, EN 18286:2026, porte sur le système de gestion de la qualité.
- L'année 2027 concentre les échéances : E-23 et la ligne directrice de l'AMF en mai, haut risque européen et cyberrésilience en décembre. Le texte européen sera réexaminé en 2028 et en 2029.
- La cryptographie à clé publique actuelle est dépréciée par le NIST après 2030. Les signatures post-quantiques sont normalisées pour les jetons et les certificats, mais pas encore livrées dans les couches d'identité d'agent.
- Une défense contre l'injection appliquée agent par agent ne protège pas le collectif : une donnée non fiable redevient de confiance en passant d'un agent à l'autre.
- La base NVD compte 102 vulnérabilités de serveurs MCP en quatre mois, dont treize critiques. Le risque est dans les serveurs de tiers, non dans la spécification.

---

## Sources

Pages de l'émetteur lues le 13 novembre 2026 :

1. [Maison-Blanche — décret Inaugurating the Era of Super Intelligence, 29 septembre 2026](https://www.whitehouse.gov/presidential-actions/2026/09/inaugurating-the-era-of-super-intelligence/)
2. [NIST — SP 800-53 Control Overlays for Super Intelligence Systems, page du projet, mise à jour du 20 octobre 2026](https://csrc.nist.gov/projects/cosis)
3. [Microsoft — guide d'Ignite 2026 pour Agent 365, 10 novembre 2026](https://techcommunity.microsoft.com/blog/agent-365-blog/microsoft-ignite-2026-your-guide-to-agent-365/4571750) — événement postérieur à la date de référence.
4. [METR — Task-Completion Time Horizons of Frontier AI Models, mise à jour du 8 septembre 2026](https://metr.org/time-horizons/) — relue à l'audit.
5. [METR — fichier de données de la série Time Horizon 1.1](https://metr.org/assets/benchmark_results_1_1.yaml) — fichier téléchargé et relu à l'audit.
6. [METR — Frontier Risk Report, 19 mai 2026](https://metr.org/blog/2026-05-19-frontier-risk-report/) — premier cinquième de la page.
7. [Stanford HAI — The 2026 AI Index Report, page de synthèse](https://hai.stanford.edu/ai-index/2026-ai-index-report) — rapport complet non ouvert.
8. [ARC Prize Foundation — page de résultats](https://arcprize.org/results) — résultats officiels annoncés pour le 4 décembre 2026.
9. [IETF — groupe de travail Agent Communication Protocols (agentproto), charte et jalons](https://datatracker.ietf.org/group/agentproto/about/) — relue à l'audit.
10. [IETF — groupe de travail Discovery of Agents With Names (dawn), charte et jalons](https://datatracker.ietf.org/group/dawn/about/) — relue à l'audit.
11. [IETF — draft-ietf-wimse-aims-01, 2 novembre 2026](https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/) — document de travail.
12. [IETF — groupe de travail OAuth, charte et jalons](https://datatracker.ietf.org/wg/oauth/about/)
13. [W3C — charte du Web & AI Interest Group](https://w3.org/2025/10/webai-ig-charter.html)
14. [W3C — AI Agent Protocol Community Group](https://www.w3.org/groups/cg/agentprotocol/)
15. [IEEE — projet P3931, description, découverte et registre d'agents](https://standards.ieee.org/ieee/3931/12499/)
16. [IEEE — projet P3777, bancs d'essai et métriques de performance des agents](https://standards.ieee.org/ieee/3777/12350/)
17. [CEN-CENELEC JTC 21 — EN 18286 becomes the first harmonised standard under the EU AI Act, 14 octobre 2026](https://jtc21.eu/en-18286-becomes-the-first-harmonised-standard-under-the-eu-ai-act/) — décision d'exécution non ouverte sur EUR-Lex.
18. [UIT-T — programme de travail, recommandation F.748.93](https://www.itu.int/ITU-T/workprog/wp_item.aspx?isn=23620) — texte réservé aux membres, non lu.
19. [UIT-T — programme de travail, rapport YSTR.NAC-roadmap](https://www.itu.int/itu-t/workprog/wp_item.aspx?isn=23691)
20. [NIST — SI Agent Standards Initiative, mise à jour du 9 novembre 2026](https://www.nist.gov/super-intelligence/si-agent-standards-initiative) — aussi citée aux chapitres 4, 11 et 43 (anciennement CAISI).
21. [FIDO Alliance — normes pour les interactions d'agents, communiqué du 28 avril 2026](https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/)
22. [OpenID Foundation — nouveaux projets du groupe AuthZEN pour l'autorisation des agents](https://openid.net/openid-foundation-advances-authorization-for-the-agent-era-with-new-authzen-working-group-drafts/)
23. [MCP — feuille de route, mise à jour du 22 août 2026](https://modelcontextprotocol.io/development/roadmap) — aussi citée au chapitre 43.
24. [IETF — groupe de travail WIMSE, charte et jalons](https://datatracker.ietf.org/wg/wimse/about/)
25. [Salesforce — annonces de Dreamforce 2026](https://www.salesforce.com/blog/dreamforce-2026-announcements/)
26. [SAP — annonces de TechEd, 27 octobre 2026](https://news.sap.com/2026/10/sap-teched-ai-developers-build-what-matters-autonomous-execution/)
27. [Commission européenne — AI Act Service Desk, calendrier de mise en œuvre](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) — page d'information; le Journal officiel fait foi.
28. [Commission européenne — responsabilité du fait des produits défectueux](https://single-market-economy.ec.europa.eu/single-market/goods/free-movement-sectors/liability-defective-products_en)
29. [Commission européenne — règlement sur l'identité numérique européenne, mise à jour du 6 novembre 2026](https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation)
30. [Commission européenne — AI Act, article 111, version consolidée](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-111)
31. [Commission européenne — Cyber Resilience Act, mise à jour du 7 septembre 2026](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
32. [Commission européenne — AI Act, article 112, version consolidée](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-112)
33. [Commission européenne — règlement sur l'espace européen des données de santé](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en)
34. [Parlement du Canada — LEGISinfo, projet de loi C-36](https://www.parl.ca/legisinfo/en/bill/45-1/c-36)
35. [Gouverneur de la Californie — lois sur l'IA signées le 30 septembre 2026](https://www.gov.ca.gov/2026/09/30/californias-nation-leading-ai-framework-just-got-stronger-governor-newsom-signs-more-first-in-the-nation-worker-protections-and-more/) — dates d'entrée en vigueur non relevées.
36. [NIST — IR 8547, Transition to Post-Quantum Cryptography Standards, version finale du 27 octobre 2026](https://csrc.nist.gov/pubs/ir/8547/final) — page relue à l'audit; calendrier lu dans le PDF.
37. [Centre canadien pour la cybersécurité — ITSM.40.001, feuille de route de migration vers la cryptographie post-quantique, 23 juin 2025](https://www.cyber.gc.ca/en/guidance/roadmap-migration-post-quantum-cryptography-government-canada-itsm40001) — version anglaise.
38. [Commission européenne — feuille de route coordonnée de transition vers la cryptographie post-quantique](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography)
39. [IETF — RFC 10024, accord de clés hybride post-quantique pour TLS 1.3, août 2026](https://datatracker.ietf.org/doc/rfc10024/)
40. [IETF — RFC 9964, ML-DSA pour JOSE et COSE, mai 2026](https://datatracker.ietf.org/doc/rfc9964/)
41. [IETF — RFC 10073, signatures composites ML-DSA pour X.509, novembre 2026](https://datatracker.ietf.org/doc/rfc10073/)
42. [SPIFFE — The SPIFFE Standard Roadmap, 18 août 2026](https://spiffe.io/blog/2026-08-18-spiffe-standard-roadmap/)
43. [IETF — draft-uppalapati-wimse-pq-agent-identity-01, 27 octobre 2026](https://datatracker.ietf.org/doc/draft-uppalapati-wimse-pq-agent-identity/) — soumission individuelle, non adoptée.
44. [NIST — National Vulnerability Database, interrogation de l'API du 13 novembre 2026](https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=Model%20Context%20Protocol&pubStartDate=2026-07-01T00:00:00.000Z&pubEndDate=2026-10-28T00:00:00.000Z) — comptage et tri faits sur la réponse.
45. [OWASP GenAI Security Project — GenAI and Agentic AI Exploit Roundup Q3 2026, 8 octobre 2026](https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026/) — recension; divulgations d'origine non ouvertes.
46. [Anthropic — Detecting and countering misuse of AI, septembre 2026](https://www.anthropic.com/threat-intelligence-report-september-2026) — premier tiers de la page; l'éditeur décrit ses propres détections.

Notices d'arXiv lues le 13 novembre 2026, résumé seulement — prépublications, sauf mention contraire :

47. [Wang et coll. — BenchJack (arXiv 2605.12673), 12 mai 2026](https://arxiv.org/abs/2605.12673)
48. [Shao et coll. — audit de la validité de protocole de quinze bancs d'essai d'agents (arXiv 2607.22368), 24 juillet 2026](https://arxiv.org/abs/2607.22368)
49. [Foerster et coll. — CaMeL appliqué aux agents d'utilisation d'ordinateur (arXiv 2601.09923), 14 janvier 2026](https://arxiv.org/abs/2601.09923)
50. [Peters-Gill et coll. — Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks (arXiv 2610.05640), 5 octobre 2026](https://arxiv.org/abs/2610.05640) — relue à l'audit.
51. [Winston et coll. — vérification par solveur de la conformité aux politiques d'outils (arXiv 2603.20449), 20 mars 2026](https://arxiv.org/abs/2603.20449)
52. [Elkoussy et Perez — AgentLTL (arXiv 2607.02599), 1er juillet 2026](https://arxiv.org/abs/2607.02599)
53. [Nikolaou et coll. — CaMeLoT (arXiv 2609.18674), 16 septembre 2026](https://arxiv.org/abs/2609.18674) — accepté à la conférence CAMLIS 2026 selon la notice.
54. [Wu et coll. — LongMemEval-V2 (arXiv 2605.12493), 12 mai 2026](https://arxiv.org/abs/2605.12493) — travail en cours.
55. [Zhao et coll. — AMA-Bench (arXiv 2602.22769), 26 février 2026](https://arxiv.org/abs/2602.22769)
56. [Zhang et coll. — Ratchet (arXiv 2605.22148), 21 mai 2026](https://arxiv.org/abs/2605.22148)
57. [Xu et coll. — EvoLib (arXiv 2605.14477), 14 mai 2026](https://arxiv.org/abs/2605.14477) — accepté à NeurIPS 2026 selon la notice.
58. [Gonzalez-Pumariega et coll. — fiabilité des agents d'utilisation d'ordinateur à la répétition (arXiv 2604.17849), 20 avril 2026](https://arxiv.org/abs/2604.17849)
59. [Belcak et coll. — petits modèles de langage et systèmes agentiques (arXiv 2506.02153), 2 juin 2025](https://arxiv.org/abs/2506.02153) — article de position.
60. [Haque et coll. — TinyLLM (arXiv 2511.22138), 27 novembre 2025](https://arxiv.org/abs/2511.22138)
61. [Jin et coll. — Proof-of-Guardrail (arXiv 2603.05786), 6 mars 2026](https://arxiv.org/abs/2603.05786) — atelier de la conférence ICML 2026 selon la notice.
62. [Grigor et coll. — VET, traces d'exécution vérifiables (arXiv 2512.15892), 17 décembre 2025](https://arxiv.org/abs/2512.15892)
63. [Prakash — AIP, délégation vérifiable entre MCP et A2A (arXiv 2603.24775), 25 mars 2026](https://arxiv.org/abs/2603.24775) — auteur unique.
64. [Bansal et coll. — Magentic Marketplace (arXiv 2510.25779), 27 octobre 2025](https://arxiv.org/abs/2510.25779)
65. [Keppo et coll. — fragilité de la collusion entre agents (arXiv 2603.20281), 18 mars 2026](https://arxiv.org/abs/2603.20281)
66. [Miceli-Barone et coll. — honnêteté des agents négociateurs (arXiv 2605.31445), 29 mai 2026](https://arxiv.org/abs/2605.31445)
67. [Assran et coll. — V-JEPA 2 (arXiv 2506.09985), 11 juin 2025](https://arxiv.org/abs/2506.09985)

Page tierce lue le 13 novembre 2026 :

68. [CGTN — plan chinois de norme obligatoire sur la sécurité des applications d'agents, 28 juillet 2026](https://news.cgtn.com/news/2026-07-28/China-launches-plan-to-draft-mandatory-safety-standard-for-AI-agents-1P9iZyWenD2/index.html) — média d'État; registre officiel non ouvert.

## Limites de ce chapitre

- Les pages ont été lues par un outil qui en restitue des extraits. Relues à l'audit : [4], [5], [9], [10], [36], [50] et [44], dont le comptage a été refait. Le calendrier de [36] vient du PDF du rapport; la page relue n'en porte que le résumé.
- Les notices d'arXiv ont été lues par leur résumé. Sauf pour [53], [57] et [61], dont la notice indique une conférence ou un atelier, ce sont des prépublications; les bancs d'essai et les échantillons n'ont pas été examinés.
- Sources primaires non atteintes : le catalogue de l'ISO, EUR-Lex, la page du NCCoE, les sites de Gartner et de ServiceNow. Les travaux du comité ISO/IEC JTC 1/SC 42 sur les agents ne sont pas documentés. Les dates de l'AI Act viennent des pages de la Commission, non du Journal officiel.
- La source [68] est un média d'État qui cite un registre officiel non ouvert. Les lois d'États américains autres que celles de la Californie, le droit britannique n'a été vu que dans des extraits de recherche et n'est pas cité; la loi coréenne et le plan japonais ne le sont que par renvoi à la section 35.7, d'après des sources secondaires ou un résumé.
- Les scores de [8] viennent d'une page qui ne distingue pas les résultats vérifiés; les meilleurs scores d'OSWorld, de GAIA, de τ-bench et de Terminal-Bench n'ont pas pu être lus chez leurs émetteurs et ne sont pas cités.
- Les incidents de la section 49.7 sont connus par la recension [45], non par les divulgations d'origine. La source [46] n'a été lue qu'en partie.
- Les conférences Ignite et re:Invent de la fin de 2026 sont postérieures à la date de référence.
- L'échelle de maturité de 49.6, la conjecture sur ce qui atteindra la production, la lecture de l'écart entre les deux horizons de METR et le rapprochement du calendrier de l'IETF avec les scénarios du chapitre 43 sont des interprétations.
- Les deux échéances et les cinq lignes du registre ajoutées le 14 novembre 2026 renvoient aux sections des chapitres complétés ce jour-là; leurs sources et leurs réserves y figurent et n'ont pas été relues ici.
- Les intervalles de confiance des horizons de METR sont convertis de minutes en heures et arrondis par l'ouvrage.
