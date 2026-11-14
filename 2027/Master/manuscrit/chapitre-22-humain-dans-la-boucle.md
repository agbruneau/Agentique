# Chapitre 22 — L'humain dans la boucle

*Question directrice : quelles décisions un agent peut-il prendre seul ?*

> **État de référence :** cadre de Singapour pour l'IA agentique, version 1.5 du 20 mai 2026; spécification MCP `2026-07-28`; article 14 du règlement européen sur l'IA, avec les dates d'application affichées le jour de la lecture. Les numéros entre crochets renvoient aux sources en fin de chapitre, toutes des pages primaires lues pour ce chapitre; [14] à [17] ont été ajoutées le 14 novembre 2026.

Placer un humain devant chaque action d'un agent semble la réponse prudente. Elle ne tient pas. Un agent qui demande une approbation à chaque pas n'apporte guère plus qu'un assistant, et l'approbateur trop sollicité cesse de lire ce qu'il approuve. À l'inverse, un agent laissé seul devant un paiement ou une suppression de données engage l'organisation sans que personne ait décidé.

La thèse de ce chapitre est que la question directrice ne se tranche ni pour l'entreprise ni pour l'agent, mais par classe de décision, selon trois critères : la gravité d'une erreur, la réversibilité de l'action et la possibilité réelle qu'un humain la contrôle. L'approbation humaine est une ressource rare, qui se dégrade quand on la gaspille. Il faut donc en demander peu, au bon endroit, l'imposer par des moyens techniques et mesurer qu'elle reste effective. L'autonomie, elle, s'élargit sur preuve et se retire automatiquement.

---

## 22.1 Dans la boucle, sur la boucle, hors de la boucle

### Trois positions, plus une

Le vocabulaire remonte aux lignes directrices du groupe d'experts de haut niveau de la Commission européenne (2019), qui distinguent trois approches de supervision [1].

- **Dans la boucle** (*human-in-the-loop*) : l'humain peut intervenir à chaque cycle de décision du système. Le texte ajoute aussitôt que ce n'est, dans bien des cas, ni possible ni souhaitable.
- **Sur la boucle** (*human-on-the-loop*) : l'humain intervient à la conception et surveille le fonctionnement.
- **Aux commandes** (*human-in-command*) : l'humain supervise l'activité d'ensemble et décide quand et comment utiliser le système, y compris de ne pas l'utiliser.

L'expression « hors de la boucle » ne figure pas dans ce texte. L'usage l'applique à l'agent qui agit sans supervision en direct et dont les actions sont, au mieux, vérifiées après coup. C'est le dernier niveau du cadre de Singapour : l'agent opère, l'humain observe [2].

Ces positions disent quand l'humain intervient par rapport à l'effet de l'action : avant, pendant ou après. Le guide québécois sur l'IA agentique retient les trois mêmes formes : validation avant exécution, surveillance pendant l'exécution, revue après coup pour les actions internes, réversibles et de faible impact [12].

![Les positions de l'humain selon le moment où il intervient par rapport à l'action de l'agent (avant, pendant ou après); la position « aux commandes » englobe les trois. L'expression « hors de la boucle » vient de l'usage, non des lignes directrices de 2019.](figures/fig-22-e1.svg)

### Ce que la distinction ne dit pas

**La position s'attache à une action, pas à un système.** Un même agent lit un dossier hors de la boucle, rédige une réponse sur la boucle et l'envoie dans la boucle. Qualifier un agent de « HITL » ne renseigne sur rien tant que la liste des actions soumises à approbation n'est pas donnée.

**La position « aux commandes » ne se délègue pas.** Quelle que soit l'autonomie accordée, une personne désignée décide que l'agent existe, fixe ses limites et peut l'arrêter. Le guide québécois en fait une condition d'autorisation : un agent qui ne peut pas être interrompu rapidement ne devrait pas être autorisé [12]. L'imputabilité correspondante relève du chapitre 39.

Le texte de 2019 pose enfin un principe de compensation : toutes choses égales, moins un humain peut superviser un système, plus les essais doivent être étendus et la gouvernance stricte [1]. Sortir l'humain de la boucle déplace donc le travail vers l'évaluation (chapitre 33), les garde-fous et l'exploitation (chapitre 34).

---

## 22.2 Échelles graduées d'autonomie

Le chapitre 1 a aligné trois échelles d'autonomie. Elles ne mesurent pas la même chose, et c'est ce qui les rend complémentaires.

| Échelle | Critère | Niveaux | Apport propre |
|---|---|---|---|
| Feng et coll. [3] | Rôle de l'utilisateur | 5 : opérateur, collaborateur, consultant, approbateur, observateur | L'autonomie est un choix de conception, distinct de la capacité |
| Singapour [2] | Degré d'intervention humaine | 4, repris de [3] | Autonomie et espace d'action sont deux axes |
| Cloud Security Alliance (CSA) [4] | Contrôles exigés | 6, de 0 à 5, calqués sur SAE J3016 | Chaque niveau a son autorité d'approbation et sa fréquence de revue |

**Le niveau n'est pas une propriété du modèle.** Pour Feng et ses coauteurs, un agent capable peut fonctionner à faible autonomie s'il doit consulter son utilisateur avant chaque action [3]. Un modèle plus performant ne justifie donc pas, à lui seul, un niveau plus élevé.

**Le niveau vaut pour une configuration.** Les mêmes auteurs proposent des « certificats d'autonomie » : un tiers attesterait le niveau maximal auquel un agent peut fonctionner, compte tenu de son modèle, de ses prompts, de ses outils et de son environnement; un changement d'outils ou d'environnement invaliderait le certificat [3]. Cette proposition de recherche se transpose à l'interne : une autorisation d'autonomie se rattache à une configuration et se réexamine quand celle-ci change.

**Le niveau fixe qui signe.** L'échelle de la CSA associe à chaque niveau une autorité : le propriétaire d'affaires au niveau 1, le gestionnaire et la sécurité au niveau 2, un comité de revue au niveau 3, la direction avec acceptation de risque documentée au niveau 4. La fréquence de revue suit la même pente, d'annuelle à hebdomadaire [4].

**Le sommet n'est pas une cible.** L'auteur de l'échelle de la CSA juge le niveau 5 inapproprié en entreprise aujourd'hui [4]. Feng et ses coauteurs estiment que les risques du niveau « observateur » dépassent souvent ses bénéfices, sauf en environnement clos, parce que des erreurs simples se composent d'étape en étape [3].

Ces échelles servent de vocabulaire et d'échelle d'autorisation. Aucune n'est une norme : celle de la CSA est un billet de son dirigeant, présenté comme une invitation à la discussion. Elle laisse ouvertes deux questions : un système a-t-il un seul niveau ou un niveau par capacité et par contexte, et comment vérifier le niveau auquel il fonctionne réellement [4] ? La section 22.4 répond à la première; la seconde relève de l'observabilité (chapitre 33).

---

## 22.3 Autonomie méritée et retour arrière

L'expression « autonomie méritée » désigne une autonomie accordée par paliers, à mesure que l'agent fait ses preuves. Les échelles lues n'en donnent pas les critères : le billet de la CSA dit qu'un niveau supérieur exige de convaincre une autorité plus élevée, sans définir de règle de promotion [4]. Ce que les sources documentent, c'est le déploiement progressif et le repli.

### Élargir sur preuve

Faute de pouvoir tester d'avance tous les comportements d'un agent, le cadre de Singapour recommande un déploiement graduel, réglé sur trois axes : les utilisateurs (d'abord les personnes formées), les outils (d'abord des serveurs MCP en liste blanche), les systèmes exposés (d'abord les systèmes internes à faible risque) [2]. L'étude de cas Dayos, dans le même document, montre la suite : l'entreprise interdit aujourd'hui à son agent ses actions les plus risquées et réexaminera ce choix quand d'autres protections auront été validées en conditions réelles [2].

### Ce que la confiance change

Anthropic a mesuré le phénomène sur son propre agent de programmation. Les nouveaux utilisateurs laissent l'agent agir sans approbation dans environ 20 % des sessions; vers 750 sessions, la proportion dépasse 40 %. Dans le même temps, la part des tours où l'utilisateur interrompt l'agent passe d'environ 5 % à environ 9 % [5]. Les auteurs y lisent un déplacement de la supervision et non un abandon : l'utilisateur expérimenté cesse d'approuver chaque action, mais surveille et intervient davantage.

La mesure vient d'un seul éditeur, sur son produit. Elle suggère que l'autonomie méritée fait passer l'humain de la position « dans la boucle » à la position « sur la boucle ». Elle ne le retire pas.

### Retirer sans délibérer

Trois sources décrivent le mouvement inverse.

- Un agent qui fonctionne normalement au niveau 3 pourrait retomber automatiquement au niveau 1 dès qu'une anomalie est détectée, ou pendant un incident de sécurité [4].
- Quand l'infrastructure d'approbation fait défaut, parce que le superviseur est injoignable ou que l'action est nouvelle et sans règle établie, l'action est refusée par défaut [2].
- Le maintien en production ne se présume pas : un agent devrait pouvoir être suspendu si les incidents se répètent, si les journaux sont insuffisants ou si la supervision réelle diminue [12].

D'où une règle asymétrique, proposée ici : la promotion se décide par classe de décision, sur des preuves consignées, par l'autorité du niveau visé; la rétrogradation est déclenchée par un signal et n'attend aucune décision. Le chapitre 34 décrit une variante, où un budget d'erreur règle l'autonomie.

---

## 22.4 Gouverner par classe de décision

### Trois questions

Avant la mise en service de son agent de billetterie informatique, Dayos a coté chaque type de billet selon trois questions [2] :

1. **Gravité** : si l'agent se trompe, quelles sont les conséquences ?
2. **Réversibilité** : l'action peut-elle être défaite ?
3. **Faisabilité de la supervision** : est-il réaliste qu'un humain révise chaque étape ?

Trois paliers en découlent. Le premier (60 % des billets : réinitialisations de mots de passe, demandes d'accès ou de statut) est automatisé : l'agent propose, le demandeur confirme, sans ingénieur, avec un audit d'échantillon aux deux semaines. Au deuxième (30 % : mises à jour du plan comptable, correspondances d'intégration, connexions d'API en échec), l'agent diagnostique et propose, mais un ingénieur qualifié signe avant toute exécution. Le troisième (10 % : déploiements en production, changements de sécurité et de permissions) reste interdit à l'agent [2].

La troisième question est décisive : une approbation qu'un humain ne peut pas exercer avec sérieux, faute de temps ou de compétence, n'est pas un contrôle.

### Les classes qui appellent une approbation

Le cadre de Singapour en nomme quatre familles : les actions à fort enjeu, les actions irréversibles (supprimer des données, envoyer une communication, payer), les comportements atypiques (un accès hors du périmètre de travail) et les seuils fixés par l'utilisateur lui-même [2]. Le guide québécois rend la supervision obligatoire quand l'agent modifie une donnée officielle, déclenche une action dans un système, produit une recommandation qui touche une personne ou une organisation, utilise des renseignements personnels ou confidentiels, communique avec un tiers, engage une dépense ou traite un cas ambigu ou litigieux [12].

Le tableau suivant, propre à ce chapitre, en tire une grille de départ.

| Classe de décision | Exemple | Position par défaut | Contrôle associé |
|---|---|---|---|
| Lire, analyser | Recherche, diagnostic | Hors de la boucle | Périmètre de lecture, journal |
| Agir : réversible, faible enjeu | Réinitialiser un mot de passe | Sur la boucle | Audit d'échantillon, annulation |
| Agir : partiellement réversible | Modifier le plan comptable | Dans la boucle, sur proposition | Approbateur compétent |
| Agir : irréversible ou à fort enjeu | Payer, supprimer, écrire à un tiers | Dans la boucle, à chaque fois | Plafond, approbation liée aux paramètres |
| Comportement atypique | Accès hors périmètre | Escalade | Détection d'anomalie |
| Hors mandat | Modifier ses propres permissions | Interdit | Refus technique |

Cette grille prolonge la gradation « interpréter, choisir, engager » du chapitre 17 et le traitement du point de non-retour au chapitre 18.

### Une limite se programme

L'approbation doit être imposée par des contrôles au niveau du système plutôt que par des consignes dans le prompt, qui peuvent être contournées ou « oubliées » [2]. Une politique qui cantonne un agent aux systèmes de développement ne vaut rien s'il peut techniquement atteindre la production [4]. L'agent ne doit jamais pouvoir élargir ses permissions, modifier ses règles, effacer ses journaux ou contourner les validations prévues [12].

La classe d'une décision s'évalue donc hors du modèle : dans l'outil, à la passerelle (chapitre 24) ou dans la couche d'autorisation (chapitre 30). Elle ne peut pas non plus reposer sur ce qu'un outil déclare de lui-même. MCP exige que le client tienne les annotations d'un outil pour non fiables, sauf si le serveur est de confiance [9]. Classer les actions revient à l'entreprise.

---

## 22.5 Concevoir les points d'approbation : fatigue et goulots

### L'approbation qui ne contrôle plus

Anthropic rapporte que les utilisateurs de son agent de programmation acceptent 93 % des demandes de permission, et nomme l'effet : une fatigue d'approbation, où l'on cesse de prêter attention à ce qu'on approuve [6]. Le cadre de Singapour fait le même constat : exiger une supervision continue nourrit le biais d'automatisation et la fatigue d'alerte [2]. Feng et ses coauteurs ajoutent qu'un agent mal aligné pourrait profiter du désengagement de l'approbateur pour faire passer une action risquée [3].

Le goulot n'est pas le délai. Dans l'étude Measuring Agents in Production (MAP), 66 % des agents déployés tolèrent des temps de réponse de l'ordre de la minute ou plus [7], et une exécution suspendue peut attendre sans coût (chapitre 18). Ce qui manque est l'attention de l'approbateur.

### Ce que dit la recherche indépendante

La seule mesure de la fatigue d'approbation qui précède vient d'un éditeur, sur son propre produit [6]. Quatre sources qui ne portent pas sur le produit de leur auteur vont dans le même sens, chacune avec sa limite; deux d'entre elles, [14] et [15], comptent néanmoins des auteurs employés par des éditeurs d'outils agentiques.

**Le biais d'automatisation est mesuré depuis longtemps.** Une revue systématique de 74 études, surtout sur l'aide à la décision clinique, établit que l'utilisateur d'un système d'aide suit aussi ses erreurs. Quand le conseil est faux, le risque de décision incorrecte augmente de 26 % (rapport de risques de 1,26, calculé à titre indicatif sur quatre études), et de 6 % à 11 % des réponses d'abord justes deviennent fausses après consultation du système [16]. La charge de travail, la complexité de la tâche et la pression du temps aggravent le biais. L'expérience le réduit sans l'éliminer, et l'effet de la formation est incertain. Ce qui aide tient à la conception : rendre l'utilisateur comptable de sa décision, afficher un niveau de confiance tenu à jour, fournir une information plutôt qu'une recommandation, et moins mettre le conseil en évidence [16]. L'article a été publié en ligne en 2011 (numéro de 2012) et porte sur des aides à la décision, non sur des agents.

**Les développeurs supervisent par raccourcis.** Trois chercheurs de Microsoft ont interrogé 17 développeurs expérimentés, en juillet et en août 2025, sur leur façon de superviser des agents de programmation [15]. Ils distinguent quatre formes de travail : le cadrage préalable, la planification conjointe, la surveillance en temps réel et la révision après coup. La surveillance en temps réel est rarement pratiquée. La révision repose sur quatre raccourcis : tenir le plan de l'agent pour un reflet fidèle de son travail, tenir des tests réussis pour une garantie, parcourir des yeux plutôt que lire, et se fier à l'agent en terrain inconnu. Les auteurs y voient une supervision « suffisante », imposée par le coût d'une révision complète, et non de la négligence. L'étude est exploratoire, et douze participants travaillent chez l'employeur des auteurs [15].

**La conception actuelle des agents use le superviseur.** Un article de position de chercheurs de Hugging Face et de Data & Society reprend le terme de fatigue d'approbation et en décrit les ressorts [14]. La même personne doit à la fois utiliser l'agent et autoriser ses actions. Une révision de routine mobilise une pensée rapide, peu propice à l'analyse. Déléguer fait perdre la pratique des tâches qu'il faudra ensuite juger. Enfin, un signal d'approbation dégradé, s'il sert à l'entraînement, apprend au système à réduire la friction. L'article ne rapporte aucune mesure propre.

**La supervision prescrite n'est pas prouvée.** Green a recensé 41 politiques qui imposent une supervision humaine d'algorithmes gouvernementaux. D'après cet article, les données disponibles suggèrent que les personnes ne peuvent pas exercer les fonctions qu'on attend d'elles, si bien que ces politiques légitiment des outils défaillants. Il propose d'exiger de l'organisme qu'il justifie, preuves empiriques à l'appui, la forme de supervision qu'il retient [17]. La cinquième règle ci-dessous répond à cette exigence.

Ces sources confirment la direction, non l'ampleur : aucune ne mesure l'usure de l'approbation chez des approbateurs d'agents en entreprise.

### Six règles de conception

**1. En demander moins.** Le premier levier est de borner plutôt que de demander. L'étude de cas Tencent du cadre de Singapour décrit des permissions graduées : lecture sans approbation, modification de fichiers approuvée pour la session, commandes et appels réseau approuvés, outils MCP régis par des règles d'autorisation, de demande ou de refus [2]. Le second levier est le réviseur automatique. Le mode automatique d'Anthropic confie à un classifieur l'examen des appels d'outils de l'agent. L'éditeur publie ses erreurs : 0,4 % de blocages à tort sur du trafic réel, mais 17 % d'actions excessives non détectées sur un échantillon de 52 cas. Il précise que ce mode ne remplace pas une révision humaine attentive sur une infrastructure à fort enjeu [6] : le réviseur raccourcit la file, sans remplacer l'approbateur au point de non-retour.

**2. Rendre la demande lisible.** Une demande courte et contextualisée, qui énonce le risque et, s'il existe, un score de confiance, plutôt que des journaux bruts [2]. Pour une commande complexe, une explication en langage clair qui signale les effets de bord [2].

**3. Choisir la forme de la réponse.** Approuver ou refuser suffit pour une action simple. Pour un plan, mieux vaut laisser l'humain le modifier. Pour une action à haut risque, une justification écrite peut être exigée [2]. MCP distingue trois réponses à une demande d'élicitation : accepter, décliner, annuler [10]. La troisième rappelle qu'une fenêtre fermée n'est ni un refus ni un consentement. Un processus doit traiter l'absence de réponse comme une non-approbation.

**4. Choisir l'approbateur.** Il doit avoir l'expertise du domaine [2] et l'information nécessaire pour comprendre l'action, l'accepter, la modifier, la refuser ou l'escalader [12].

**5. Mesurer la supervision.** Le cadre de Singapour propose trois indicateurs : le taux de rejet ou de modification, dont une valeur faible peut signaler une approbation machinale; le temps de réponse, dont la brièveté peut signaler la fatigue; et les approbateurs dont le profil s'écarte nettement de la norme [2]; l'audit interne peut en être chargé (section 39.6).

**6. Prévoir la panne.** Refus par défaut si l'approbateur est injoignable [2]; critères d'escalade fixés d'avance, par exemple des sources contradictoires, une incertitude élevée ou un seuil de coût dépassé [12]. Hors ligne, faute d'approbateur, l'autonomie se borne par des droits alloués avant la coupure (chapitre 46).

**Quatre compléments.** L'article de position [14] ajoute à ces règles des moyens que les cadres cités plus haut ne nomment pas.

- *Regrouper* (règle 1) : laisser l'agent finir un lot de changements liés, puis présenter l'ensemble, plutôt qu'une demande par action.
- *Faire réfléchir avant de montrer* (règle 3) : pour une décision à fort enjeu, demander à l'approbateur de consigner son avis avant de voir la recommandation de l'agent.
- *Séparer les intérêts* (règle 4) : l'approbateur ne devrait pas être celui qui profite de l'approbation, et aucun objectif de productivité ne devrait décourager l'examen.
- *Glisser des tâches témoins* (règle 5) : insérer dans le flux des cas à réponse connue, pour vérifier que l'approbateur relève l'erreur; suivre aussi le temps de révision qui baisse à taux d'approbation constant, et les questions qui se raréfient.

### La mécanique

Un point d'approbation est une suspension durable. Dans LangGraph, la fonction `interrupt()` met un nœud en pause; l'état est sauvegardé par un *checkpointer* sous un identifiant de fil, le graphe attend indéfiniment, puis reprend avec la réponse de l'humain. À la reprise, le nœud redémarre depuis son début : un effet placé avant l'interruption serait rejoué, et la documentation demande de le placer après, ou dans un nœud distinct [8].

Côté protocoles, un serveur MCP à qui il manque une information renvoie un résultat `input_required`; le client doit montrer quel serveur demande et permettre de décliner [10]. L'extension Tasks, encore en bêta, porte le même état pour les opérations longues (chapitre 5). A2A prévoit `INPUT_REQUIRED` et `AUTH_REQUIRED`; le second peut porter l'approbation d'une personne, mais ne vaut pas autorisation en soi (chapitre 6). La spécification MCP dit qu'il « devrait » toujours y avoir un humain capable de refuser une invocation d'outil, et que le client devrait montrer les arguments avant l'appel [9] : le protocole transporte la demande, il n'impose pas qu'elle soit posée. Une approbation vaut pour des paramètres exacts et se journalise comme un résultat d'étape (chapitre 18). Pour faire preuve, elle doit être un octroi du serveur d'autorisation, non un clic dans l'interface de l'agent (section 30.4).

---

## 22.6 Exigences réglementaires de supervision

**Union européenne.** L'article 14 du règlement sur l'IA exige que les systèmes à haut risque soient conçus pour être supervisés efficacement par des personnes physiques. Les mesures doivent être proportionnées aux risques, au niveau d'autonomie et au contexte d'utilisation. Les personnes chargées de la supervision doivent pouvoir comprendre les capacités et les limites du système, rester conscientes du biais d'automatisation, interpréter les sorties, décider de ne pas utiliser le système ou d'en écarter le résultat, et l'interrompre par un bouton d'arrêt ou une procédure équivalente, vers un état sûr [11]. La double vérification par deux personnes n'est imposée que pour l'identification biométrique à distance. La page consultée affiche une application le 2 décembre 2027 pour les systèmes de l'annexe III et le 2 août 2028 pour ceux de l'annexe I [11]; le chapitre 35 traite ce calendrier.

L'article exige une capacité de supervision, non l'approbation de chaque action. Et il nomme le biais d'automatisation parmi les risques à maîtriser : selon la lecture proposée ici, un approbateur qui clique machinalement n'en respecte pas l'esprit.

**Québec.** Le guide du ministère de la Cybersécurité et du Numérique (2026) veut une supervision « réelle, documentée et proportionnée au risque ». Il exige que les actions à incidence significative soient validées avant leur exécution, et précise que la supervision ne doit pas être symbolique [12].

**Canada.** Selon le guide fédéral sur sa portée, la Directive sur la prise de décisions automatisée couvre l'automatisation partielle, y compris quand un humain est dans la boucle ou qu'un agent public rend la décision finale [13]. La présence d'un humain ne sort donc pas un système de son champ. L'article 12.1 de la loi québécoise sur le secteur privé (Loi 25) vise les décisions fondées exclusivement sur un traitement automatisé; selon la lecture retenue au chapitre 38, qui développe ces textes, une intervention mineure, sans répercussion réelle, ne l'écarte pas.

Ces textes demandent tous une capacité effective de comprendre, de refuser et d'arrêter, proportionnée au risque. Aucun texte lu ne dresse la liste des décisions interdites aux agents : elle revient à l'organisation.

---

## 22.7 La pratique : des agents à courte portée

L'étude MAP repose sur 20 études de cas et 306 réponses valides à un sondage, dans 26 domaines, entre avril et novembre 2025; 86 de ces réponses décrivent des agents déployés ou en pilote [7]. Parmi eux, 68 % exécutent moins de dix étapes avant une intervention humaine (au plus dix selon le résumé), et 47 % moins de cinq. Et 74 % s'appuient surtout sur l'évaluation humaine. Plus de neuf sur dix servent des humains plutôt que d'autres logiciels, et 52 % de leurs utilisateurs sont des employés de l'organisation. Les auteurs écrivent que les équipes restreignent délibérément l'autonomie pour la stabilité en production, et envisagent l'humain dans la boucle comme un principe de conception durable plutôt que comme une contrainte provisoire [7].

Les mesures d'Anthropic sur son API publique concordent. Sur un échantillon d'environ un million d'appels d'outils, quelque 73 % semblent comporter un humain dans la boucle sous une forme ou une autre, et 80 % viennent d'agents dotés d'au moins une protection; les auteurs tiennent ces chiffres pour des bornes supérieures. Environ 0,8 % des appels paraissent irréversibles, et près de la moitié relèvent du génie logiciel [5].

La courte portée est donc un choix d'ingénierie, non un plafond technique. Et si les actions irréversibles sont rares, une politique qui leur réserve l'approbation ne vise qu'une petite fraction du trafic : la file peut rester courte, donc lisible. Les auteurs de la seconde étude jugent qu'exiger l'approbation de chaque action crée de la friction sans gain de sécurité assuré, et s'attachent à la capacité de surveiller et d'intervenir [5].

Les deux sources ont leurs limites : MAP ne prétend pas couvrir l'ensemble des agents et signale un biais de participation, et les données d'Anthropic viennent d'un seul fournisseur, qui classe les appels avec son propre modèle.

---

## Grille de décision

| Décision | Option par défaut | Quand s'en écarter |
|---|---|---|
| Unité de gouvernance | La classe de décision, cotée en gravité, réversibilité et faisabilité de la supervision [S] | Agent à action unique : un niveau par agent suffit |
| Lecture et analyse | Sans approbation, dans un périmètre appliqué techniquement [S] | Renseignements personnels ou confidentiels |
| Action réversible à faible enjeu | Sur la boucle, avec audit d'échantillon [N] | Anomalie détectée : retour à l'approbation |
| Action irréversible ou à fort enjeu | Approbation préalable, liée aux paramètres exacts [N] | Montant sous un plafond fixé par classe |
| Lieu d'application | Outil, passerelle ou couche d'autorisation [N] | Jamais le prompt seul |
| Promotion d'autonomie | Par classe, sur preuve consignée, signée par l'autorité du niveau visé [S] | — |
| Rétrogradation | Automatique, sur signal [S] | — |
| Approbateur injoignable | Refus par défaut [N] | Action réversible, déjà autorisée sur la boucle |
| Preuve que la supervision reste effective | Taux de modification, temps de révision, tâches témoins [N] | Classe laissée sans approbation humaine |

---

## Points à retenir

- « Dans », « sur » et « hors de la boucle » qualifient une action, pas un agent. La position « aux commandes », soit décider d'utiliser l'agent et pouvoir l'arrêter, ne se délègue pas.
- Les échelles d'autonomie fournissent un vocabulaire et une échelle d'autorisation. Aucune n'est une norme, et leur sommet n'est pas une cible.
- Le niveau d'autonomie est un choix de conception, rattaché à une configuration. Un meilleur modèle ne le relève pas de lui-même.
- La décision se gouverne par classe, selon la gravité, la réversibilité et la faisabilité de la supervision.
- Une limite écrite seulement dans un prompt ou une politique n'est pas une limite.
- L'approbation s'use : il faut en demander moins, la rendre lisible et la mesurer. La recherche indépendante confirme la direction; l'ampleur, chez des approbateurs d'agents en entreprise, n'a pas été mesurée.
- L'autonomie s'élargit sur preuve et se retire sur signal. La confiance déplace l'humain vers la surveillance; elle ne le retire pas.
- Les textes réglementaires lus demandent une capacité effective de comprendre, de refuser et d'arrêter, non un clic par action.
- En production, la courte portée est délibérée et les actions irréversibles sont rares.

---

## Sources

Pages primaires lues le 11 novembre 2026 :

1. [Groupe d'experts de haut niveau sur l'IA — Ethics Guidelines for Trustworthy AI (2019)](https://www.aepd.es/sites/default/files/2019-12/ai-ethics-guidelines.pdf) — passage « Human oversight », copie hébergée par l'AEPD.
2. [IMDA — Model AI Governance Framework for Agentic AI, version 1.5 (20 mai 2026)](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) — autonomie, risques, section 2.2.2, déploiement graduel; cas Dayos et Tencent.
3. [Feng, McDonald et Zhang — Levels of Autonomy for AI Agents (arXiv 2506.12469)](https://arxiv.org/html/2506.12469)
4. [Cloud Security Alliance — Leveling Up Autonomy in Agentic AI (28 janvier 2026)](https://cloudsecurityalliance.org/blog/2026/01/28/levels-of-autonomy)
5. [Anthropic — Measuring AI agent autonomy in practice (18 février 2026)](https://www.anthropic.com/research/measuring-agent-autonomy)
6. [Anthropic — How we built Claude Code auto mode (25 mars 2026)](https://www.anthropic.com/engineering/claude-code-auto-mode)
7. [Pan et coll. — Measuring Agents in Production (arXiv 2512.04123, version 4)](https://arxiv.org/html/2512.04123v4) — première moitié du texte.
8. [LangGraph — Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
9. [MCP — Outils, spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)
10. [MCP — Élicitation, spécification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)
11. [Règlement européen sur l'IA — article 14, supervision humaine](https://artificialintelligenceact.eu/article/14/)
12. [Ministère de la Cybersécurité et du Numérique — Guide sur l'utilisation responsable de l'intelligence artificielle agentique (2026)](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/cybersecurite_numerique/Intelligence_artificielle/GU_IA_Agentique.pdf)
13. [Gouvernement du Canada — guide sur la portée de la Directive sur la prise de décisions automatisée](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/automated-decision-making/guide-scope-directive-automated-decision-making.html)

Pages lues le 14 novembre 2026, pour la section 22.5 :

14. [Mitchell, Ghosh et Passi — AI Agents Push Humans Out of the Loop (arXiv 2608.23642, version 3 du 6 septembre 2026)](https://arxiv.org/html/2608.23642) — article de position; premiers cinq sixièmes du texte.
15. [Dhanorkar, Passi et Vorvoreanu — Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents (arXiv 2606.05391, 3 juin 2026)](https://arxiv.org/html/2606.05391) — prépublication; premiers deux tiers du texte.
16. [Goddard, Roudsari et Wyatt — Automation bias: a systematic review of frequency, effect mediators, and mitigators (*JAMIA*, vol. 19, n° 1, janv.-févr. 2012, pp. 121-127, publ. en ligne 16 juin 2011, DOI 10.1136/amiajnl-2011-000089)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) — revue systématique.
17. [Green — The Flaws of Policies Requiring Human Oversight of Government Algorithms (Computer Law & Security Review 45, 2022; arXiv 2109.05067)](https://arxiv.org/abs/2109.05067) — résumé, puis extraits relus le 14 novembre 2026.

## Limites de ce chapitre

- La source [17], d'abord connue par son seul résumé, a été relue au-delà du résumé le 14 novembre 2026, par un outil qui en rend des extraits; les écarts relevés sont corrigés dans le texte.
- Les sources [3], [8] et [13] ont été lues par un outil qui résume la page, sans recoupement. À l'audit du 12 novembre 2026, les passages cités de [2], de [4] à [7] et de [9] à [11] ont été relus à la source; ils concordent, aux précisions près de 22.4 et 22.7. Les sources [1] et [12] ont été lues dans leur texte, par sections pour [1].
- L'usage de « hors de la boucle » vient de la connaissance générale. « Autonomie méritée » n'est définie par aucune source lue.
- Le texte de la Directive fédérale et celui de l'article 12.1 n'ont pas pu être chargés, ni à la rédaction ni le 14 novembre 2026; la lecture de l'article 12.1 est reprise du chapitre 38, qui la transpose de la règle du secteur public par analogie. La norme ISO/IEC 42105 sur la supervision humaine, en cours de publication selon le chapitre 35, n'a pas été consultée.
- Sont des propositions de ce chapitre : la règle asymétrique de promotion et de rétrogradation, le tableau des classes de décision, la formulation des six règles de conception et la lecture de l'article 14 quant à l'approbation machinale.
- Les mesures [5] et [6] portent sur les produits de l'éditeur qui les publie. Les sources [14] à [17], ajoutées le 14 novembre 2026, en sont indépendantes mais ne comblent pas ce manque : [14] est un article de position, [15] une étude par entretiens dont douze des dix-sept participants travaillent chez l'employeur des auteurs, [16] une revue systématique publiée en ligne en 2011 (numéro de 2012) sur les aides à la décision, et [17], d'abord connu par son résumé, a été relu par extraits le 14 novembre 2026. Aucune mesure indépendante de la fatigue d'approbation chez des approbateurs d'agents en entreprise n'a été trouvée.
- Les sources [14] à [16] ont été lues par l'outil d'extraction, qui ne restitue que le début des textes longs : la fin de [14] et de [15] n'a pas été lue. La sous-section « Ce que dit la recherche indépendante », les quatre compléments aux règles et la ligne de la grille sur la preuve de la supervision datent du 14 novembre 2026; le rattachement de chaque complément à une règle est de ce chapitre.
