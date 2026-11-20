# 8 Autonomie et supervision humaine

L’autonomie d’un agent n’est pas une propriété du modèle : c’est une décision d’architecture, prise par une personne imputable, inscrite au registre et appliquée par la passerelle d’agents. Ce chapitre fixe une échelle unique de niveaux (N0 à N4), quatre paliers de risque pour les outils (P0 à P3) et la règle qui les combine. Il précise ensuite comment rendre l’approbation humaine vérifiable, comment interagir avec les agents

qui travaillent en arrière-plan, comment éviter l’approbation machinale et comment traiter les décisions automatisées visées par la Loi 25.

## 8.1 Une échelle unique N0 à N4

Le cadre adopte une seule échelle d’autonomie (figure 14 et tableau 28), que chaque agent déclare et que la plateforme fait respecter.

Deux arguments la fondent. D’abord, l’autonomie est un choix de conception : Feng, McDonald et Zhang (2025) la distinguent de la capacité du modèle et de son environnement, et la définissent par le rôle laissé à l’utilisateur**[83]**. Ensuite, une gouvernance uniforme échoue : selon Gartner (26 mai 2026), la cause profonde des échecs est une gouvernance binaire, qui verrouille tout ou permet tout, et la confusion entre la capacité d’agir d’un agent et la portée des accès qui lui sont accordés; la firme prévoit, dans un communiqué sans méthode publiée, que, d’ici 2027, 40 % des entreprises rétrograderont ou désactiveront des agents autonomes après des incidents de production révélant des lacunes de gouvernance**[95]**.

Chaque niveau se définit donc par deux éléments : le rôle de la personne et l’étendue de ce que l’agent peut faire sans approbation. Le second s’observe appel par appel. N4 se distingue en outre de N3 par l’origine de la tâche, déclenchée sans demande d’une personne (événement, horaire), que la passerelle lit dans un attribut posé par l’orchestrateur ou par le courtier. Le niveau ne dépend ni du nombre d’agents ni de la puissance du modèle : un système multiagent peut réunir des agents de niveaux différents, et, selon le cadre de gouvernance de l’IA agentique de l’Infocomm Media Development Authority (IMDA) de Singapour, l’espace d’action d’un agent, c’est-à-dire ses outils, se distingue de son autonomie**[76, 83]**.

> **[Figure]**
> - Autonomie croissante contrôles compensatoires croissants NX
> - Interdit : l’agent fixe ses objectifs ou ses permissions
> - N0
> - Automatisation déterministe
> - N1
> - Consultatif
> - N2
> - Exécution approuvée
> - N3 N4
> - L’AGENT
> - aucun modèle : flux codé, règles, RPA, API
> - lit, analyse, recommande;
> - aucun effet en écriture
> - prépare l’action, attend l’accord pour chaque écriture
> - exécute seul le réversible sous seuils, dans un ODD
> - s’autodéclenche, opère en
> - continu, ODD certifié
> - LA PERSONNE
> - conçoit les règles
> - et exploite
> - exécute elle-même
> - (opératrice)
> - approuve chaque action
> - (dans la boucle)
> - supervise, traite les exceptions (sur la boucle)
> - gouverne : politiques,
> - audit, coupe-circuit
> - PALIERS D’OUTILS PERMIS
> - hors IA P0 et P1 en lecture P2 sous seuils; P3 après approbation hors bande
> - comme N3; P3 toujours
> - approuvé
> - CONTRÔLES MINIMAUX
> - tests logiciels, revue de code essais d’exactitude
> - points d’arrêt, jeton d’approbation, audit
> - budgets, sagas, disjoncteurs, évaluation continue,
> - PLAFOND PAR CLASSE risque élevé risque modéré ou faible
> - Le niveau est un plafond inscrit au registre, distinct du nombre d’agents et de la capacité du modèle.
> - Toute action P3 (critique, externe ou irréversible) exige une approbation humaine, quel que soit le niveau.
> - Autonomie bornée et supervisée Autonomie étendue sous ODD certifié
> - accès circonscrit, journalisation,
> - P2 après approbation signée; P3 après approbation hors bande
> - retour arrière rapide arrêts testés, réautorisation
> - risque faible, sur décision du comité

***Figure 14 — Échelle d’autonomie N0 à N4.** Chaque marche indique ce que fait l’agent, ce que fait la personne, les paliers d’outils permis et les contrôles minimaux; plus l’autonomie croît, plus les contrôles compensatoires s’accumulent. Le niveau NX, hors de l’échelle, est interdit. Le plafond N4 est réservé à la classe de risque faible, sur décision du comité. Le tableau 28 détaille les contrôles minimaux de chaque niveau. Source : cadre CRE-IA-2026-01, d’après Gartner (2026), AWS, Feng et coll. (2025) et l’IMDA.*

*Tableau 28 — Niveaux d’autonomie : rôles, paliers permis et contrôles minimaux*

| **Niveau** | **Ce que fait l’agent** | **Rôle humain et boucle** | **Paliers permis** | **Contrôles minimaux (cumulatifs)** | **Exemple** |
| --- | --- | --- | --- | --- | --- |
| **N0** Automatisation déterministe | Aucun choix d’action laissé à un modèle : le code fixe chaque pas (flux codé, règles, RPA, API); un modèle peut transformer une donnée sans choisir l’action. N0 qualifie un flux, non un agent. | Conçoit les règles et exploite le flux. | Sans objet | Tests logiciels, revue de code, gestion des changements. | Rapprochement bancaire quotidien codé en règles. |
| **N1** Consultatif | Lit, analyse, recommande, rédige; aucun effet en écriture. | La personne exécute elle-même toute action (rôle d’opérateur); l’agent ne fait que recommander. | P0, P1 | Accès aux données circonscrit, authentification, journalisation de l’usage, essais de sécurité de base, essais d’exactitude et d’hallucination, formation des utilisateurs à une confiance appropriée. | Résumé d’un dossier et texte de réponse affiché à l’écran, que le conseiller copie, relit et envoie lui-même. |
| **N2** Exécution approuvée | Planifie et prépare; chaque action en écriture attend une approbation explicite. | Approuve chaque écriture avant son exécution : humain dans la boucle (HITL). | P0, P1; P2 après approbation signée (service d’approbation, même appareil admis); P3 après approbation signée hors bande (EXIG-AUT-09) | Essais de sécurité poussés, état de la tâche conservé à chaque point d’approbation, jeton d’approbation, journal d’audit, procédure d’intervention propre aux agents. | Modifications de fiches fournisseurs préparées par l’agent, chacune approuvée avant l’écriture. |
| **N3** Autonomie bornée et supervisée | Exécute seul les actions P2 réversibles ou compensables sous seuils déclarés, dans un domaine de conception opérationnel (ODD) documenté; escalade les exceptions. | Supervise par exception, traite les escalades, peut interrompre; revue a posteriori par échantillonnage : humain sur la boucle (HOTL). | P0, P1; P2 sous seuils; P3 après approbation hors bande | Surveillance continue, seuils et budgets appliqués par la passerelle, compensation déclarée, disjoncteurs, retour arrière rapide, propriété claire du comportement de l’agent. | Agent de soutien TI qui classe, fusionne et ferme les billets en double sous un plafond horaire, et escalade le reste. |
| **N4** Autonomie étendue sous ODD certifié | Traite des tâches déclenchées sans demande d’une personne (événement, horaire) et opère en continu, dans un ODD certifié. La passerelle lit l’origine de la tâche et refuse à un agent qui n’est pas N4 toute écriture sans approbation au titre d’une tâche ainsi déclenchée. | Hors de la boucle d’exécution, mais sur la boucle de gouvernance : politiques, audit, coupe-circuit. | Comme N3; P3 toujours approuvé | ODD certifié, évaluation continue, arrêts ciblé et général testés, réautorisation périodique, décision du comité. | Agent de qualité des données qui, sur alerte, met en quarantaine les lots suspects jour et nuit. |
| **NX** Autonomie non bornée | Fixe ses objectifs, modifie ses permissions, écrit et exécute du code hors contraintes. | Aucun contrôle humain effectif. | — | **Interdit** | — |

Les contrôles des niveaux N1 à N3 s’inspirent de ceux que Gartner associe à ses niveaux Observer, Conseiller, Agir avec approbation et Agir de façon autonome (Gartner précise que ceux du niveau Conseiller incluent tous ceux du niveau Observer; le cumul aux niveaux suivants est le choix du cadre); Gartner prévient d’ailleurs que les approbations peuvent s’affaiblir sous la pression du temps ou la fatigue d’approbation**[95]**. Les contrôles de N0 et de N4 sont fixés par le cadre. L’abréviation ODD (domaine de conception opérationnel, *operational design domain*) est un concept de la conduite automatisée des véhicules routiers**[301]**; le cadre l’emploie pour désigner le périmètre documenté (systèmes, données, outils, seuils, plages horaires) hors duquel l’agent s’arrête ou escalade.

L’échelle n’est pas un parcours de maturité dont N4 serait le but. Morris et coll. rappellent que le niveau d’autonomie retenu au déploiement n’a pas à être le maximum que permettent les capacités du modèle**[302]**, et l’OWASP formule le principe de moindre agence (*Least-Agency*) : un comportement agentique déployé sans nécessité élargit la surface d’attaque sans ajouter de valeur**[28]**. Le bon niveau est le plus bas qui atteint l’objectif.

`EXIG-AUT-01` **· DOIT**

**Niveau d’autonomie déclaré et appliqué**

Chaque agent **DOIT** avoir un niveau d’autonomie N1 à N4 (tableau 28; N0 qualifie un flux déterministe, non un agent) inscrit au registre (section 11.4) comme plafond, avec la date d’homologation et le nom de la personne qui l’a approuvé. Le niveau déclaré **DOIT** être le plus bas qui permet d’atteindre l’objectif métier, avec sa justification consignée dans la fiche d’agent. La passerelle d’agents **DOIT** refuser tout appel d’outil qui excède ce plafond, ainsi que, pour un agent qui n’est pas N4, toute écriture sans approbation au titre d’une tâche déclenchée sans demande d’une personne, d’après l’attribut d’origine posé par l’orchestrateur ou par le courtier; un agent ambiant N1 ou N2 peut donc traiter une telle tâche (section 3.3).

Pourquoi : le principe de moindre agence de l’OWASP proscrit l’autonomie inutile**[28]**; Feng et coll. proposent un « certificat d’autonomie » qui fixe le niveau maximal d’un agent et accompagne ses métadonnées**[83]**.

`EXIG-AUT-02` **· DOIT**

**Plafond selon la classe de risque**

Le niveau déclaré **DOIT** être évalué selon les critères du tableau 30 et respecter le plafond que fixe EXIG-CON-02 pour la classe de risque de l’agent (section 12.1, tableau 46) et celui de la phase de mise en œuvre en cours (tableau 58).

Pourquoi : le RIA exige des mesures de contrôle humain proportionnées aux risques, au niveau d’autonomie et au contexte d’utilisation (art. 14, par. 3)**[61, 290, 412]**; les plafonds eux-mêmes sont un choix du cadre.

`EXIG-AUT-03` **· NE DOIT PAS**

**Autonomie non bornée interdite (NX)**

Un agent **NE DOIT PAS** fixer d’autres objectifs que ceux qui lui sont assignés au registre, modifier ses propres permissions ou son niveau d’autonomie, ni écrire et exécuter du code hors des contraintes déclarées. Toute modification des objectifs, des outils ou du niveau d’un agent doit passer par le registre et être approuvée par une personne habilitée, la décision étant consignée au registre. Aucune dérogation n’est possible.

Pourquoi : choix normatif du cadre, et non exigence réglementaire. Mitchell et coll. soutiennent que le risque pour les personnes croît avec l’autonomie et que les agents entièrement autonomes ne devraient pas être développés**[303]**; l’OWASP recommande une double vérification avant qu’un agent ne modifie ses objectifs**[87]**.

`EXIG-AUT-04` **· DOIT**

**Domaine de conception opérationnel (ODD), repli et arrêts pour N3 et N4**

Un agent de niveau N3 ou N4 **DOIT** avoir un ODD documenté (systèmes, données, outils, seuils, volumes, plages horaires) et un comportement de repli déclaré pour toute sortie de ce domaine : arrêt en état sûr, compensation ou escalade vers une file humaine nommée. Les plafonds par exécution de l’EXIG-ORC-26 et les arrêts de l’EXIG-ORC-28 (arrêt ciblé, qui révoque une catégorie d’actions, et arrêt général) s’appliquent à lui comme à tout agent (section 7.8 et section 9.4).

Pourquoi : SAE J3016 distingue ses niveaux 3 et 4 par la partie qui assure le repli à la sortie du domaine; le repli assuré par le système, qu’exige la présente exigence, est celui de son niveau 4**[304]**; le RIA prévoit l’arrêt du système dans un état sûr (art. 14, par. 4, al. e))**[61, 290, 412]** et OpenAI recommande une interruption ciblée ou générale**[291]**.

Pour homologuer un niveau, le cadre recommande l’« évaluation assistée » de Feng et coll. : un utilisateur en attente aide l’agent sur demande et consigne chaque intervention; on augmente graduellement son implication, d’abord par des approbations, puis par des échanges plus fréquents. Le niveau se déduit de l’implication minimale qui permet d’atteindre le seuil de réussite fixé**[83]**.

`EXIG-AUT-05` **· DOIT**

**Homologation et réévaluation du niveau**

Le niveau d’autonomie **DOIT** être homologué avant la mise en production, puis réévalué avant la mise en service de tout changement visé par l’EXIG-GOV-12, qui fait foi pour la liste des déclencheurs (une correction purement typographique de l’invite système, attestée sans effet sur le jeu d’évaluation, n’en est pas un). Tant que la réévaluation n’est pas faite, la version antérieure reste en service; à défaut, l’agent **DOIT** être suspendu, ou remplacé par le flux déterministe de repli s’il existe. Un changement ne permet jamais de fonctionner au-dessus du plafond de classe. La version de modèle servie est épinglée et vérifiée par la passerelle de modèles.

Pourquoi : Feng et coll. prévoient le renouvellement du certificat d’autonomie à chaque changement de l’agent ou de son environnement**[83]**; pour les institutions financières fédérales, la ligne directrice E-23 du BSIF (en vigueur le 1er mai 2027) attend des institutions qu’elles définissent des critères de modification importante d’un modèle, y compris d’IA**[8]**.

### Correspondance avec les autres échelles

Le tableau 29 situe N0 à N4 par rapport aux niveaux des versions de travail antérieures du cadre (section 1.7) et aux échelles de la littérature. Les correspondances avec Gartner et AWS reposent sur les sources citées sous le tableau; celles avec Feng et coll., Morris et coll. et SAE J3016 sont indicatives, car ces échelles décrivent le rôle de l’utilisateur ou un autre objet que le plafond d’actions sans approbation.

*Tableau 29 — Correspondance entre l’échelle du cadre et les autres échelles d’autonomie*

| **Cadre** | **Versions antérieures (section 1.7)** | **Gartner (2026)** | **AWS (portées)** | **Feng et coll. (rôle de l’utilisateur)** | **Morris et coll. (indicatif)** | **SAE J3016 (analogie)** |
| --- | --- | --- | --- | --- | --- | --- |
| **N0** | doc. L0 · prod. L0 | — | — | — | 0 Sans IA | — |
| **N1** | doc. L1 · v0.x N0 · prod. L1 | 1 Observer; 2 Conseiller | Portée 1 | L1 Opérateur | 1 IA outil; 2 IA consultante | — |
| **N2** | doc. L2 · v0.x N1 · prod. L2 | 3 Agir avec approbation | Portée 2 | L2 Collaborateur | 3 IA collaboratrice | — |
| **N3** | doc. L3 · v0.x N2 et N3 · prod. L3 | 4 Agir de façon autonome | Portée 3 | L3 Consultant; L4 Approbateur | 4 IA experte | Niveaux 3 et 4 : une personne supervise, comme au niveau 3, mais le repli est assuré par le système, comme au niveau 4 (EXIG-AUT-04) |
| **N4** | doc. L4 · v0.x N4 · prod. L4, sans la notion multiagent | — | Portée 4, sous restrictions | L5 Observateur, sous restrictions | 5 IA agent (le cadre y distingue N4, bornée, et NX, non bornée; cette distinction ne vient pas de Morris et coll.) | Niveau 4 : repli assuré dans l’ODD |
| **NX** | doc. L5 | — | — | — | 5 IA agent (non bornée; distinction propre au cadre) | Niveau 5 : domaine illimité |

Abréviations : « doc. » désigne la recherche documentaire (L0 à L5), « v0.x » les deux versions de travail successives, v0.1 et v0.2 (N0 à N4), et « prod. » la version structurée en exigences, dite de production (L0 à L4), soit les quatre ébauches de la section 1.7. Ces ébauches ne sont pas publiées avec le cadre : la colonne ne sert qu’à situer l’historique, les niveaux de même numéro ne se correspondent pas d’une ébauche à l’autre et seule l’échelle du présent chapitre fait foi. Les sources des colonnes suivantes sont Gartner**[95]**, la matrice de portée d’AWS, qui associe la portée 2 à une approbation avant chaque action et la portée 3 à une supervision avec interrupteurs d’arrêt**[75]**, Feng et coll.**[83]** et Morris et coll.**[302]**. Les correspondances avec Gartner et AWS suivent la vérification des sources; celles avec Feng et coll., Morris et coll. et SAE J3016 sont indicatives, car ces échelles décrivent le rôle de l’utilisateur ou un autre objet que le plafond d’actions sans approbation. Les libellés L1 à L5 sont ceux de Feng et coll.; leur « approbateur » (L4) n’intervient que lorsque l’agent le sollicite, ce qui le rapproche de N3 plutôt que de N2.

SAE J3016 est une pratique recommandée (*Recommended Practice*) de SAE International, et non une norme de sécurité. Le cadre ne lui emprunte que deux notions, par analogie : le domaine de conception opérationnel et la question du repli, qui sépare son niveau 3, où l’humain doit reprendre la main, de son niveau 4, où le système assure lui-même le repli à la sortie de son domaine; seul son niveau 5 suppose un domaine illimité**[301, 304]**. Enfin, l’« agent entièrement autonome » de Mitchell et coll., qui écrit et exécute son propre code, correspond à NX**[303]**.

## 8.2 Classer un agent : critères

La classe de risque de l’agent (section 12.1) fixe son plafond; quatre critères déterminent ensuite le niveau réellement autorisé sous ce plafond.

Le cadre retient ces quatre critères comme méthode interne. Ils s’appuient sur des sources reconnues sans en être la transcription. L’IMDA désigne la portée des actions de l’agent, leur réversibilité et son niveau d’autonomie comme déterminants du risque, et recommande de borner le rayon d’action dès la conception**[76]**. OpenAI recommande de noter chaque outil selon qu’il lit ou écrit, sa réversibilité, les permissions requises et son impact financier**[66]**. Le NIST AI RMF demande que les processus de supervision humaine soient définis, évalués et documentés (MAP 3.5)**[74]**.

*Tableau 30 — Quatre critères pour fixer le niveau d’autonomie sous le plafond de la classe*

| **Critère** | **Question posée** | **Ce qu’on examine** | **Effet sur le niveau** |
| --- | --- | --- | --- |
| **Rayon d’impact** | Combien d’enregistrements, de systèmes, de personnes ou de dollars l’agent peut-il toucher en une exécution ininterrompue? | Outils d’écriture autorisés, portées des jetons, plafonds de volume et de montant. | Un rayon élevé abaisse le niveau ou impose des seuils plus bas. |
| **Réversibilité** | L’effet peut-il être annulé, compensé, ou est-il définitif? | Compensation déclarée au catalogue, délai de compensation, effets externes. | Une action irréversible relève du palier P3 : approbation préalable, quel que soit le niveau. |
| **Délai de détection et de récupération** | Combien de temps s’écoule entre une erreur, sa détection et sa correction? | Alertes automatiques, revue par échantillonnage, délai de compensation. | Une détection lente plafonne à N2 (contrôle avant l’action plutôt qu’après), quels que soient les autres critères; l’EXIG-AUT-07 en est le cas extrême. |
| **Observabilité reconstructive** | Peut-on reconstituer ce que l’agent a fait, avec quelles données et sous quelle autorisation? | Traces d’appels d’outils, journal d’audit signé (section 10.3), versions épinglées. | Sans traces d’appels d’outils, ni N3 ni N4. |

Le quatrième critère tient au fait que le raisonnement affiché par un modèle n’explique pas forcément ses actions : l’IMDA rappelle que la chaîne de pensée n’est pas analogue au raisonnement humain**[76]**. Seules les traces des appels d’outils prouvent ce qui a été fait.

Les seuils qui traduisent ces critères en plafonds (nombre d’enregistrements, montants, délais) sont des paramètres d’étalonnage du cadre : le comité d’architecture et des risques agentiques les approuve, les publie avec le catalogue et les révise après chaque incident. Aucune source reconnue ne propose de valeurs universelles. Le niveau autorisé est le plus bas de quatre valeurs : le plafond de la classe, le plafond de la phase de mise en œuvre en cours (tableau 58), le niveau que permettent les quatre critères et le niveau suffisant pour l’objectif.

`EXIG-AUT-06` **· DOIT**

**Classement fondé sur les permissions effectives**

L’évaluation des quatre critères **DOIT** se fonder sur les permissions effectives de l’agent (outils autorisés, portées des jetons, plafonds de volume et de montant), y compris les actions qui ne lui sont accessibles qu’après approbation, et non sur l’intention déclarée. Elle **DOIT** être consignée dans la fiche d’agent (annexe B) et revue par l’architecture d’entreprise et par la sécurité avant l’homologation du niveau.

Pourquoi : Gartner situe la cause de nombreux échecs dans la confusion entre la capacité d’agir et la portée des accès accordés**[95, 305]**; l’IMDA recommande de borner le rayon d’action par les accès aux outils et aux systèmes**[76]**.

`EXIG-AUT-07` **· NE DOIT PAS**

**Règle d’or : pas d’exécution autonome du risque cumulé**

Un agent dont le rayon d’impact, la réversibilité et le délai de détection atteignent les seuils d’étalonnage approuvés par le comité (rayon élevé, réversibilité faible, détection lente) **NE DOIT PAS** être autorisé au-delà de N2, quels que soient ses résultats aux bancs d’essai. En l’absence de seuil approuvé pour un critère, ce critère est réputé atteint.

Pourquoi : règle propre au cadre. L’IMDA lie le risque à la portée et à la réversibilité des actions**[76]**, et Feng et coll. rappellent que les bancs d’essai de capacité ne révèlent pas le niveau d’autonomie approprié**[83]**.

**EXEMPLE**

Un agent de facturation peut modifier 10 000 comptes par exécution (rayon élevé). Ses écritures changent des montants facturés, difficiles à corriger une fois les factures transmises (réversibilité faible), et une erreur ne serait vue qu’à la fermeture mensuelle (détection lente). Malgré d’excellents résultats aux essais, il reste à N2. Pour viser N3, l’équipe agit sur les critères, pas sur les essais : plafond par exécution, détection automatisée des écarts, retenue des factures avant transmission.

## 8.3 Paliers de risque des outils P0 à P3

Le palier mesure le risque d’un outil, indépendamment de l’agent qui l’appelle; il forme le second axe de la supervision.

Un même agent peut lire sans risque et écrire avec risque. Parasuraman, Sheridan et Wickens ont proposé d’automatiser séparément chaque fonction (acquérir l’information, l’analyser, décider, agir), chacune à un niveau propre, un même système pouvant combiner des niveaux différents**[306]**. L’autonomie se règle donc aussi par action, et pas seulement par agent.

*Tableau 31 — Paliers de risque des outils*

| **Palier** | **Nature** | **Exemples** | **Contrôles obligatoires** |
| --- | --- | --- | --- |
| **P0** | Lecture publique | Recherche documentaire publique, catalogue de produits, conversion d’unités. | Identité de charge de travail, limitation de débit, journalisation de l’usage. Un outil dont un argument quitte l’entreprise (requête en texte libre vers un moteur de recherche public, par exemple) porte l’attribut « sortie de données » : il compte comme outil d’envoi (EXIG-SEC-06) et comme propriété [C] (EXIG-SEC-04), et ses arguments passent un contrôle DLP. |
| **P1** | Lecture interne ou sensible | Dossier client, fiche de paie, recherche documentaire interne. | Jeton délégué (section 9.3), contrôle d’accès au document ou à la ligne, masquage des RP en sortie, journal d’audit. |
| **P2** | Écriture réversible, ou compensable vers un état métier équivalent, à impact borné; jamais un effet irréversible ou externe | Billet de service, brouillon de courriel, réservation interne, mise à jour de statut. | Jeton délégué, clé d’idempotence (section 7.6), compensation déclarée (section 7.5), journal d’audit, seuil métier au catalogue (p. ex. 5 000 $), mesuré sur une grandeur que l’agent ne choisit pas, avec sa portée et sa fenêtre (EXIG-AUT-08); approbation au-delà du seuil. |
| **P3** | Action critique, externe ou irréversible | Virement, suppression définitive de données, communication externe officielle, changement d’infrastructure de production. | Jeton délégué, clé d’idempotence (section 7.6), journal d’audit; approbation humaine hors bande à chaque appel, jeton d’approbation lié à l’action, second approbateur pour la classe élevée; jamais exécuté seul par un agent. |

La frontière entre paliers suit l’effet, pas le serveur. Créer un brouillon de courriel est une action P2, car il reste dans l’entreprise et peut être supprimé; l’envoyer à un client est une action P3. Un même serveur MCP expose souvent les deux : chaque outil reçoit son propre palier.

Le palier ne peut pas venir du serveur lui-même. La spécification MCP 2026-07-28 exige que les clients considèrent les annotations d’outils comme non fiables, à moins qu’elles ne proviennent de serveurs de confiance; la référence du schéma précise, en des termes non normatifs (« should never »), que les clients ne fondent jamais une décision d’usage sur les annotations d’un serveur non fiable**[197, 201]**. Les métadonnées de gouvernance vivent donc au catalogue d’entreprise (section 6.8; pour les annotations MCP, section 6.5).

`EXIG-AUT-08` **· DOIT**

**Palier attribué au catalogue après revue**

Chaque outil **DOIT** recevoir un palier P0 à P3 (tableau 31) au catalogue d’entreprise (section 6.8) après revue par son propriétaire et par la sécurité, avec son seuil métier et son outil de compensation s’il y a lieu. Le palier provient du catalogue, jamais des annotations ou des métadonnées déclarées par le serveur. Un outil qui combine plusieurs effets prend le palier le plus élevé; un outil d’écriture sans compensation déclarée, ou dont la clé d’idempotence n’est vérifiée ni nativement ni par adaptateur (EXIG-ORC-22), est classé P3. Un effet irréversible ou externe est P3, même si une compensation est déclarée; P2 suppose une écriture réversible, ou compensable vers un état métier équivalent avec un impact borné. Un outil de compensation reçoit son propre palier (EXIG-ORC-17). Dans les schémas des outils P2 et P3, les montants et les identifiants sont des chaînes ou des entiers en unités mineures. Un outil dont un argument peut atteindre une destination hors du périmètre de confiance porte au catalogue l’attribut « sortie de données », indépendant du palier (EXIG-SEC-06).

Pourquoi : la spécification MCP tient les annotations pour des indices non fiables**[197]**; OpenAI recommande d’attribuer à chaque outil une cote de risque**[66]**.

`EXIG-AUT-09` **· NE DOIT PAS**

**Aucun outil P3 exécuté seul**

Un agent **NE DOIT PAS** exécuter un outil P3 sans une approbation humaine préalable, propre à cet appel et obtenue hors bande, c’est-à-dire sur un appareil et dans une session d’authentification distincts de ceux de l’agent, avec une authentification forte résistante à l’hameçonnage, quel que soit son niveau d’autonomie. La compensation déclarée d’une étape approuvée est couverte par l’approbation de l’étape (EXIG-AUT-12).

Pourquoi : l’IMDA recommande une approbation humaine avant les actions à fort enjeu ou irréversibles, comme la suppression définitive, l’envoi de communications ou les paiements; OpenAI présente l’autorisation préalable des actions irréversibles comme le moyen usuel de limiter les défaillances graves; l’OWASP recommande l’approbation explicite des actions à fort impact (ASI02)**[28, 76, 291]**. Le caractère hors bande est un choix du cadre.

## 8.4 Combiner classe de l’agent et palier de l’outil

Le contrôle exigé pour un appel dépend de la classe de l’agent, de son niveau d’autonomie et du palier de l’outil; les contrôles se cumulent, et l’approbation la plus stricte l’emporte (EXIG-AUT-10).

> **[Figure]**
> - CLASSE DE L’AGENT ↓ · PALIER DE L’OUTIL
> - P0 · lecture publique
> - catalogue, documentation
> - P1 · lecture interne
> - dossier client, paie
> - P2 · écriture réversible
> - billet, brouillon, statut
> - P3 · action critique
> - virement, suppression, envoi
> - Faible
> - plafond N3 (N4 sur décision)
> - Automatique
> - identité de charge, débit
> - Automatique
> - à chaque appel
> - Modéré
> - plafond N3
> - Automatique
> - identité de charge, débit
> - Approbation au-delà
> - du seuil métier déclaré à chaque appel
> - Élevé
> - plafond N2
> - Automatique + audit
> - journalisation complète
> - Approbation signée
> - à chaque action (N2)
> - Approbation hors bande
> - Approbation hors bande
> - Approbation hors bande
> - + second approbateur
> - contrôles du palier (tableau 31)
> - Automatique
> - contrôles du palier (tableau 31)
> - Approbation au-delà
> - du seuil métier déclaré
> - Revue a posteriori
> - échantillon : finalité, minimisation
> - Les contrôles se cumulent; l’approbation la plus stricte l’emporte (EXIG-AUT-10). Le palier d’un outil est inscrit au catalogue; la passerelle ne se fie pas aux annotations déclarées par le serveur.
> - →

***Figure 15 — Contrôle exigé selon la classe de l’agent et le palier de l’outil.** On lit la ligne de la classe de l’agent, puis la colonne du palier de l’outil; la cellule donne le contrôle minimal, en plus des contrôles obligatoires du palier (tableau 31); dans les cellules P3, « approbation signée » s’entend d’une approbation hors bande (EXIG-AUT-09), et la matrice qui fait foi est celle de l’EXIG-AUT-10. Le niveau d’autonomie de l’agent et les déclencheurs d’approbation peuvent rendre le contrôle plus strict, jamais plus souple; il se calcule selon l’EXIG-AUT-10. Source : cadre CRE-IA-2026-01.*

Deux exemples. Un agent de classe modérée, déclaré N3, reclasse un billet de service : outil P2 sous le seuil, il agit seul et l’appel est journalisé. Le même agent veut modifier l’échéance de 40 factures alors que le seuil déclaré de l’outil est de 25 par tâche : la passerelle suspend l’appel et demande une approbation. Si l’agent était déclaré N2, chaque écriture exigerait une approbation, même sous le seuil : le niveau prime alors sur la cellule.

D’autres déclencheurs s’ajoutent à la grille. L’IMDA en énumère quatre catégories : actions à fort enjeu, actions irréversibles, comportements atypiques (accès hors périmètre, trajectoire anormale) et seuils fixés par l’utilisateur**[76]**. La « règle de deux » de Meta (31 octobre 2025) en fournit une autre : dans une session, un agent ne devrait pas cumuler l’exposition à des entrées non fiables, l’accès à des systèmes sensibles ou à des données privées et la capacité de changer d’état ou de communiquer vers l’extérieur; si les trois sont nécessaires, il n’agit pas sans supervision**[307]**. Un agent N3 qui a lu un courriel externe, consulté un dossier P1 et s’apprête à appeler un outil P2 tombe donc sous approbation (section 9.6).

`EXIG-AUT-10` **· DOIT**

**Contrôle calculé à chaque appel**

Pour chaque appel d’outil, la passerelle d’agents, que traversent tout appel MCP et toute action P2 ou P3 (EXIG-ARC-01), **DOIT** déterminer le contrôle exigé. Ce contrôle est l’union des contrôles exigés par la cellule classe × palier de la matrice qui suit (illustrée par la figure 15), par le niveau d’autonomie et la classe les plus contraignants de la chaîne de délégation (EXIG-ORC-23), par les déclencheurs d’approbation (comportement atypique, seuil de l’EXIG-AUT-08, cumul de la règle de deux au sens de l’EXIG-SEC-04 : contenu non fiable, données sensibles et changement d’état ou communication externe) et par les points non dérogeables (EXIG-GOV-17). Les contrôles techniques (jeton délégué, masquage, filtrage par ligne, audit) se cumulent; aucun n’en remplace un autre. Entre exigences d’approbation, l’ordre est : refus, approbation hors bande à deux approbateurs, approbation hors bande, approbation, exécution automatique avec revue a posteriori, exécution automatique; le plus strict est le premier de cette liste. Matrice classe × palier, qui fait foi : pour les classes faible et modérée, exécution automatique aux paliers P0 et P1, exécution automatique sous le seuil métier déclaré et approbation au-delà au palier P2, approbation hors bande au palier P3; pour la classe élevée, exécution automatique avec audit au palier P0, exécution automatique avec revue a posteriori au palier P1, approbation au palier P2 et

approbation hors bande à deux approbateurs au palier P3. La passerelle consigne la règle appliquée dans la trace et dans le journal d’audit (section 10.3).

Pourquoi : cumuler les contrôles et retenir l’approbation la plus forte empêche qu’un agent peu autonome obtienne des droits étendus par un outil mal classé, ou qu’un outil bien classé soit utilisé au-delà du niveau de l’agent. Règle propre au cadre; l’IMDA lie le risque à la portée et à la réversibilité des actions**[76]**.

`EXIG-AUT-11` **· DOIT**

**Échec en mode fermé**

Le service d’approbation, le catalogue, le service de politiques, le registre des jti et le service d’audit sont des dépendances de la passerelle; une politique ou un instantané du catalogue distribués et non échus valent service disponible (EXIG-IAM-18). Si l’une de ces dépendances est indisponible, ou si aucune politique ne couvre l’action demandée, la passerelle **DOIT** refuser tout appel dont le contrôle calculé (EXIG-AUT-10) exige une approbation, donc au moins tout appel P3 et tout appel P2 au-delà du seuil, ainsi que tout appel P2 ou P3 si le service d’audit est indisponible. Une politique ou un instantané échus ne laissent passer que les appels P0. Ces refus sont sans préjudice du refus général de tout appel dépourvu de décision de politique valide (EXIG-IAM-18). Dans tous ces cas, l’orchestrateur **DOIT** suspendre la tâche dans un état reprenable; une compensation refusée pour l’un de ces motifs entre dans la file persistée de l’EXIG-ORC-28.

Pourquoi : l’IMDA recommande de refuser l’action par défaut lorsque l’infrastructure d’approbation fait défaut, par exemple si les superviseurs sont injoignables ou si aucune politique n’existe pour l’action tentée**[76]**; un seuil ne borne l’agent que si la grandeur mesurée échappe à son contrôle, avec une portée et une fenêtre explicites (EXIG-AUT-08).

## 8.5 Approbation humaine vérifiable

Une approbation n’a de valeur que si elle porte sur l’action exacte qui sera exécutée et si la passerelle peut le vérifier sans faire confiance à l’agent.

Un « oui, je confirme » écrit dans la conversation de l’agent ne prouve rien : une injection d’instructions peut l’imiter, et l’agent peut modifier l’action après coup. Le cadre fait donc de l’approbation un objet cryptographique, émis hors de portée de l’agent et lié à l’action par une empreinte (figure 16).

> **[Figure]**
> - Agent Passerelle d’agents
> - point d’application
> - Service d’approbation adossé au fournisseur d’identité
> - Approbateur personne habilitée
> - 1
> - 2 calcule l’empreinte et crée la demande
> - 3 présente l’action exacte, ses paramètres et son effet attendu
> - 4 approuve (authentification forte)
> - 5 jeton d’approbation signé, à usage unique
> - 6
> - 7
> - invalide l’approbation exécution, puis audit
> - N’est jamais une approbation
> - un « oui » écrit dans la conversation de l’agent
> - un résumé rédigé par l’agent
> - une approbation donnée pour d’autres arguments
> - prépare l’action
> - appel soumis à approbation, sans jeton
> - h = SHA-256(JCS({outil, version, definition_digest, agent_id, task_id, arguments}))
> - { h, agent, approbateur, rôle, jti, tâche, exp }
> - rejoue : même clé, réf. de la demande
> - apparie le jeton qu’elle conserve, vérifie signature, expiration
> - et usage unique, recalcule h : toute modification des arguments
> - →

***Figure 16 — Approbation humaine signée, liée à l’action exacte.** La passerelle intercepte l’appel soumis à approbation selon l’EXIG-AUT-10 (P3, P2 au-delà du seuil, niveau N2 ou déclencheur), calcule l’empreinte de l’action et la fait approuver par une personne habilitée; le jeton signé ne vaut que pour cette empreinte, pour une seule opération et pendant 15 minutes au plus. Le jeton est remis à la passerelle, qui le conserve (étape 5); l’agent rejoue l’appel avec la même clé d’idempotence et la référence de la demande, donnée non secrète (étape 6); une double approbation se fait par deux jetons sur le même h (EXIG-AUT-12). Source : cadre CRE-IA-2026-01.*

L’empreinte se calcule ainsi : h = SHA-256(JCS({outil, version, definition_digest, agent_id, task_id, arguments})), c’est-à-dire l’empreinte de la canonisation d’un objet qui réunit l’identifiant pleinement qualifié de l’outil (serveur et nom), sa version épinglée, l’empreinte de sa définition, les identifiants de l’agent et de la tâche, et les arguments; la canonisation d’un objet évite l’ambiguïté d’une concaténation. La canonisation suit la RFC 8785 (JSON Canonicalization Scheme), une RFC informative de la filière indépendante, non endossée par l’IETF, mais stable**[236]**; A2A 1.0 l’emploie déjà pour signer les cartes d’agent**[68]**. Sans canonisation, deux sérialisations du même objet JSON donneraient deux empreintes. Si l’agent, ou une injection, change un seul argument après l’approbation, l’empreinte recalculée par la passerelle ne correspond plus et l’appel est refusé. Cette propriété suppose que la passerelle rejette tout argument non conforme à I-JSON (RFC 7493 : clés dupliquées, nombres hors de la plage exacte d’un double, chaînes invalides) et transmette au serveur exactement la forme canonique hachée; sinon, deux analyseurs JSON peuvent lire deux actions différentes sous le même h. L’empreinte atteste que les octets transmis sont ceux qui ont été approuvés, et non que l’effet est celui qui était attendu. Un exemple de jeton figure à l’annexe C.

La formule est un choix de conception du cadre, pas une norme. Elle met en œuvre l’approbation explicite par action à fort impact que recommande l’OWASP (ASI02)**[28]** et s’appuie sur trois spécifications publiées, dont deux normes : OpenID Connect CIBA (*Client-Initiated Backchannel Authentication*) pour l’approbation hors bande, la RFC 9396 pour décrire l’action et la RFC 8785 pour la canonisation. L’emploi d’`authorization_details` dans un jeton d’approbation est un profil du cadre : la RFC 9396 ne le définit que pour les jetons d’accès.

`EXIG-AUT-12` **· DOIT**

**Jeton d’approbation lié à l’action exacte**

Toute approbation exigée par le contrôle calculé selon l’EXIG-AUT-10 (cellule classe × palier de la matrice, toute écriture d’un agent de niveau N2, déclencheurs d’approbation dont le dépassement de seuil, la règle de deux de l’EXIG-SEC-04 et le retrait déterministe de l’EXIG-SEC-06) **DOIT** produire

un jeton signé par le service d’approbation adossé au fournisseur d’identité, contenant au minimum : l’émetteur et l’audience (la passerelle); l’empreinte h, SHA-256 de la canonisation selon la RFC 8785 de l’objet {outil, version, definition_digest, agent_id, task_id, arguments}, dont les arguments incluent la clé d’idempotence; l’identifiant de l’approbateur, pseudonyme stable au sein du service, et son rôle (mandant ou tiers); les identifiants de la tâche et de l’agent; une date d’expiration et un identifiant de jeton à usage unique (`jti`). La double approbation se fait par deux jetons sur le même h. La passerelle **DOIT** rejeter tout argument non conforme à I-JSON (RFC 7493) et transmettre au serveur exactement la forme canonique hachée; elle conserve le jeton et ne le remet ni à l’agent ni à son modèle (EXIG-IAM-06). Avant l’exécution, elle **DOIT** vérifier la signature, l’émetteur, l’audience, l’expiration, la concordance de l’agent et de la tâche avec l’appelant authentifié, ainsi que le nombre et la distinction des approbateurs qu’exige le contrôle calculé, puis recalculer h; toute différence annule l’approbation. Le jeton couvre une seule opération : jusqu’à son expiration, la passerelle relaie toute présentation de la même opération (même appelant, même tâche, même h), et le système visé déduplique par la clé (EXIG-ORC-22); toute présentation avec une autre empreinte est refusée comme rejeu; un passage soldé par une demande de précision ou par un refus ne consomme pas le jeton. Après l’expiration, si l’issue est inconnue, la passerelle interroge le système visé par la clé : si l’effet est attesté, aucune nouvelle approbation n’est demandée; sinon, une nouvelle approbation est requise. Le registre des `jti` est partagé par toutes les instances de la passerelle, à écriture atomique, et fermé en cas d’indisponibilité (EXIG-AUT-11). Lorsqu’une compensation de saga est approuvée avec l’étape P2 ou P3 (EXIG-ORC-15 et EXIG-ORC-16), la demande d’approbation inclut l’empreinte de sa compensation déclarée, bornée au montant et aux bénéficiaires d’origine et liée à la même clé d’idempotence; cette approbation préalable est consignée au journal de compensation avec son empreinte et la passerelle accepte cette entrée signée du journal de compensation (y compris pour une compensation de palier P3 au sens de l’EXIG-AUT-09) jusqu’à la clôture de la saga, au-delà de l’échéance de 15 minutes du jeton d’exécution initiale. L’édition d’une action par l’approbateur est une nouvelle action : la passerelle recalcule le contrôle de l’EXIG-AUT-10 et h avant d’émettre le jeton, et celui qui a édité ne peut pas être le seul approbateur d’un appel qui en exige deux. Un outil P3 qui agit sur une ressource modifiable reçoit dans ses arguments approuvés les valeurs résolues qui déterminent l’effet (bénéficiaire, montant) ou une précondition de version (version ou ETag de la ressource) vérifiée à l’exécution; à défaut, la fiche déclare le risque résiduel de modification entre l’approbation et l’exécution. Le jeton d’exécution initiale **DOIT** expirer au plus 15 minutes après sa signature.

Pourquoi : un lien cryptographique entre la décision humaine et l’action exécutée détecte toute modification des arguments après l’approbation, pourvu que la passerelle et le serveur lisent les mêmes octets; ce mécanisme, la durée de validité et la règle d’une opération par jeton, qui concilie l’approbation et le réessai idempotent, sont des choix du cadre.

`EXIG-AUT-13` **· NE DOIT PAS**

**Ce qui n’est jamais une approbation**

La passerelle **NE DOIT PAS** accepter comme approbation un message d’acquiescement dans la conversation de l’agent, un résumé ou une justification rédigés par l’agent, une confirmation locale dans l’interface de l’agent, ni une approbation donnée pour d’autres arguments, une autre tâche ou un autre agent.

Pourquoi : le brouillon de groupe de travail WIMSE AIMS précise qu’une confirmation locale dans l’interface ne suffit pas comme autorisation**[93]**.

`EXIG-AUT-14` **· DEVRAIT**

**Approbation hors bande normalisée**

L’approbation hors bande d’un appel P3 (EXIG-AUT-09), ou celle que requiert un agent sans interface, **DEVRAIT** passer par OpenID Connect CIBA : le service d’approbation lance une demande d’authentification dorsale, et l’approbateur confirme sur son propre appareil. Un `binding_message` court, dérivé de h ou de la tâche, affiché à l’approbateur et, si l’agent a une interface, sur celle-ci, et consigné dans la demande et dans le jeton, aide à reconnaître la demande; le lien à l’action repose sur h (EXIG-AUT-12). L’action **DEVRAIT** être décrite par le paramètre `authorization_details` de la RFC 9396 lorsqu’elle comporte des paramètres que les portées ne peuvent exprimer, comme un montant ou un destinataire.

Pourquoi : CIBA Core 1.0 est une spécification finale de l’OpenID Foundation qui découple l’appareil de l’agent de celui de l’approbateur**[310]**; le brouillon WIMSE AIMS cite CIBA en exemple d’autorisation par palier, tout en notant ses limites en cours d’exécution, et le livre blanc de l’OpenID Foundation propose CIBA pour l’approbation humaine des agents**[93, 311]**; la RFC 9396 exprime les autorisations fines que `scope` ne peut exprimer**[312]**.

`EXIG-AUT-15` **· DOIT**

**Approbateurs habilités et formés**

Chaque combinaison de classe, de palier et de motif d’approbation (cellule, niveau, déclencheur) pour laquelle le contrôle calculé selon l’EXIG-AUT-10 exige une approbation **DOIT** avoir une liste d’approbateurs habilités, inscrite au registre (EXIG-GOV-04). L’approbation peut être donnée par le mandant lui-même, comme confirmation de sa propre action, sauf pour un appel P3 d’un agent de classe élevée : deux approbateurs distincts **DOIVENT** alors approuver, dont au moins un qui n’est pas le mandant et ne relève ni de sa ligne hiérarchique ni du parrain de l’agent. Les approbateurs autres que le mandant sont inscrits à la liste; ils **DOIVENT** posséder la compétence du domaine et l’autorité de refuser, et avoir été formés aux modes de défaillance des agents. Tout approbateur **DOIT** s’authentifier par authentification forte (au moins deux facteurs), résistante à l’hameçonnage (FIDO2 ou WebAuthn, par exemple) pour une approbation P3. Le service d’approbation vérifie, avant de signer, que l’approbateur est habilité pour le contrôle visé, et le rôle de chaque approbateur (mandant ou tiers) est consigné à l’audit.

Pourquoi : le RIA confie le contrôle humain des systèmes à haut risque à des personnes ayant la compétence, la formation et l’autorité nécessaires (art. 26, par. 2)**[447]**; l’IMDA demande que les superviseurs connaissent les modes de défaillance des agents**[76]**. Le second approbateur, la confirmation par le mandant et la règle d’indépendance sont des choix du cadre.

## 8.6 Interaction humaine avec les agents ambiants

Un agent ambiant travaille en arrière-plan, déclenché par des événements; la personne n’est pas devant lui quand il a besoin d’elle, et l’interaction doit être conçue en conséquence.

LangChain définit les agents ambiants comme des agents qui écoutent un flux d’événements et agissent en conséquence, éventuellement sur plusieurs événements à la fois, sans être nécessairement entièrement autonomes (section 3.3). Pour les relier aux personnes, son billet de janvier 2025 décrit trois patrons : notifier, questionner et réviser**[86]**. Le schéma de la boîte de réception d’agents (*Agent Inbox*) y associe quatre réponses : `accept`, `edit`, `response` et `ignore`, activées une à une par les drapeaux `allow_accept`, `allow_edit`, `allow_respond` et `allow_ignore`**[313]**.

*Tableau 32 — Trois patrons d’interaction avec un agent ambiant*

| **Patron** | **Quand l’employer** | **Ce que fait l’agent** | **Réponses admises** |
| --- | --- | --- | --- |
| **Notifier** | Événement important que la politique interdit à l’agent de traiter (p. ex. un contrat reçu pour signature). | Signale sans agir. | Prendre connaissance. |
| **Questionner** | Information manquante ou ambiguë. | Suspend la tâche et pose une question ciblée au lieu de deviner. | Répondre. |
| **Réviser** | Action soumise à approbation selon le contrôle calculé (EXIG-AUT-10). | Place l’action préparée dans la file, avec son effet attendu. | Accepter, éditer, répondre par une rétroaction, ignorer (refus). |

Éditer une action revient à approuver une autre action : l’action éditée repasse par l’EXIG-AUT-10 avant l’émission du jeton, avec un nouvel indicateur de risque, la passerelle calcule l’empreinte des arguments modifiés, et c’est cette version que couvre le jeton (EXIG-AUT-12). Microsoft recommande aussi de distinguer l’approbation, qui fait avancer le flux, de la rétroaction, qui renvoie le travail à l’agent, et de restreindre les points d’approbation à des invocations d’outils précises**[9]**. Les protocoles offrent les mécanismes d’attente : en A2A 1.0, une tâche passe à l’état `TASK_STATE_INPUT_REQUIRED` ou `TASK_STATE_AUTH_REQUIRED` (section 6.6)**[68]**; en MCP, un serveur pose une question par élicitation, sans jamais demander de secret par formulaire**[223]**.

Le « voyage dans le temps » souvent associé à ce patron n’est pas une réponse de la boîte de réception : c’est une fonction des points de contrôle de LangGraph, qui permet de rejouer une exécution depuis un point antérieur ou de bifurquer après avoir modifié l’état**[283]**. Il sert au diagnostic et à la correction; rejouer une étape réexécute ses effets. Enfin, le dépôt `agent-inbox` est archivé, en lecture seule, depuis le 20 septembre 2026**[313]** : le cadre adopte le patron, pas l’outil.

Un piège d’implémentation mérite attention. Dans LangGraph, `interrupt()` exige un mécanisme de points de contrôle (*checkpointer*), qui doit être persistant en production; à la reprise, le nœud interrompu redémarre depuis son début, si bien que le code placé avant l’interruption s’exécute de nouveau**[82]**. Un appel d’écriture placé avant le point d’approbation serait donc rejoué.

`EXIG-AUT-16` **· DOIT**

**Boîte de réception persistante**

Tout agent ambiant de niveau N2 ou plus **DOIT** acheminer ses interactions humaines par une boîte de réception persistante qui met en œuvre les trois patrons du tableau 32. Chaque demande **DOIT** indiquer le patron, la tâche, l’agent, une échéance fixée par cas d’usage et, pour le patron Réviser, l’effet attendu. Une demande Réviser sans réponse à l’échéance expire : l’action n’est pas exécutée et la tâche passe à une file d’escalade nommée. Une question sans réponse suspend la tâche, puis l’escalade; une notification est escaladée si sa politique l’exige. « Ignorer » vaut refus.

Pourquoi : les patrons de LangChain évitent que l’agent devine (il pose une question plutôt que d’halluciner) ou agisse sans validation humaine (révision d’une action avant son exécution)**[86]**; l’expiration en refus applique l’échec en mode fermé de l’EXIG-AUT-11.

`EXIG-AUT-17` **· DOIT**

**État persisté et effets après le point d’approbation**

L’orchestrateur **DOIT** conserver l’état de la tâche de façon durable à chaque point d’approbation obligatoire, dans un moteur d’exécution durable (section 7.4). Un appel à effet de bord ne doit pas précéder

le point d’interruption dans la même étape, et tout effet de bord suit l’EXIG-ORC-12 (clé déterministe, ou étape journalisée exécutée au plus une fois).

Pourquoi : Microsoft recommande de persister l’état aux points d’approbation obligatoires pour reprendre sans rejouer le travail antérieur**[9]**, et LangGraph réexécute le code qui précède une interruption**[82]**.

`EXIG-AUT-18` **· DOIT**

**Réautorisation périodique des agents ambiants**

Le mandat d’agent ambiant, consentement inscrit au serveur d’autorisation qui permet à un agent ambiant de niveau N3 ou N4 d’obtenir, à sa demande, des jetons délégués d’au plus 15 minutes au nom du mandant tant que le mandat est valide et que le mandant est actif (section 9.3), **DOIT** expirer à une échéance inscrite à sa fiche, au plus égale à la période d’attestation par le parrain, soit 12 mois au plus pour un agent de classe modérée ou faible (section 11.5 et EXIG-GOV-13). Avant l’échéance, l’agent entre en drainage : il n’accepte plus de nouvelle tâche pendant une marge au moins égale à la durée maximale d’une saga. À l’échéance, l’agent s’arrête vers l’avant, sans préjudice du canal de compensation (EXIG-ORC-28), jusqu’à ce qu’une personne habilitée renouvelle le mandat.

Pourquoi : OpenAI recommande des expirations périodiques qui maintiennent l’agent à l’arrêt jusqu’à ce qu’un humain le révise et le réautorise**[291]**.

## 8.7 Éviter l’approbation machinale

Un contrôle humain que personne n’exerce vraiment donne une fausse assurance; le cadre le conçoit et le mesure au lieu de le présumer.

Le phénomène est documenté. Parasuraman et Manzey (2010) montrent que le biais d’automatisation produit des erreurs d’omission et de commission, touche les novices comme les experts, s’observe aussi en équipe et ne disparaît ni avec la formation ni avec les consignes; la complaisance apparaît surtout sous charge multitâche**[314]**. OpenAI note qu’un utilisateur qui doit approuver rapidement beaucoup de décisions voit sa capacité à les examiner sérieusement diminuer**[291]**.

Les référentiels en tirent des exigences. Le RIA demande que les personnes chargées du contrôle restent conscientes du biais d’automatisation (art. 14, par. 4, al. b))**[61, 290, 412]**; pour les systèmes à haut risque de l’annexe III, ces obligations s’appliquent à compter du 2 décembre 2027, et du 2 août 2028 pour ceux de l’annexe I, selon le RIA modifié par le règlement (UE) 2026/1744**[58, 315, 447]**. L’OWASP décrit la menace T10 « Overwhelming Human in the Loop » : un attaquant submerge les réviseurs de demandes pour provoquer fatigue et approbations précipitées**[87]**. Le risque ASI09 « Human-Agent Trust Exploitation » vise la surconfiance : biais d’automatisation, autorité perçue, explications fabriquées**[28]**.

**ATTENTION**

Plus d’approbations ne veut pas dire plus de sécurité. Au-delà d’un certain volume, chaque approbation devient un clic. Le cadre préfère des approbations moins nombreuses, mieux ciblées et mesurées, et automatise ce dont le contrôle calculé (EXIG-AUT-10) est automatique.

`EXIG-AUT-19` **· DOIT**

**Écran d’approbation fidèle à l’action**

L’écran d’approbation **DOIT** présenter l’action exacte, ses paramètres, son effet attendu, sa réversibilité et sa compensation, la provenance des données qui l’ont motivée (en signalant tout contenu non fiable) et un indicateur de risque produit par les règles du catalogue, non par le modèle. L’écran et

`authorization_details` sont produits par la passerelle à partir des seuls arguments canonisés que couvre h et du schéma de l’outil inscrit au catalogue, jamais d’un texte fourni par l’agent; l’écran montre tous les champs, sauf ceux que le catalogue déclare non significatifs, ainsi que la grandeur calculée du seuil (EXIG-AUT-08). La prévisualisation ne doit pas avoir d’effet de bord : aucun appel autre qu’une lecture, aucun changement d’état. Le raisonnement de l’agent peut être affiché comme information secondaire, mais il ne doit pas tenir lieu de justification suffisante.

Pourquoi : l’OWASP (ASI09) recommande un résumé de risque en langage clair plutôt qu’une justification produite par le modèle, et la séparation entre prévisualisation et effet**[28]**; la spécification MCP recommande de montrer à l’utilisateur les entrées de l’outil avant l’appel**[197]**.

`EXIG-AUT-20` **· DOIT**

**Charge d’approbation maîtrisée**

Les files d’approbation **DOIVENT** être priorisées selon le risque. Les demandes semblables peuvent être regroupées à l’affichage, mais chaque action conserve son propre jeton d’approbation (EXIG-AUT-09 et EXIG-AUT-12). La fréquence des demandes adressées à chaque approbateur **DOIT** être plafonnée selon un seuil fixé par le comité, et la charge **DOIT** être répartie entre approbateurs, avec rotation. Seules les actions dont le contrôle calculé selon l’EXIG-AUT-10 est automatique échappent à l’approbation. La capacité d’approbation **DOIT** être dimensionnée à la conception et inscrite au registre (volume prévu, y compris la charge que crée l’EXIG-SEC-06, avec une marge); un plafond de demandes par agent et par tâche s’ajoute au plafond par approbateur. Au dépassement, les actions sont mises en file, jamais approuvées par défaut; une demande qui expire vaut refus, et un agent émetteur qui dépasse un seuil déclaré est suspendu par un arrêt ciblé.

Pourquoi : contre la menace T10, l’OWASP recommande de prioriser les files de révision par risque, d’automatiser les approbations à faible risque, de limiter la fréquence des demandes et de répartir dynamiquement la charge entre réviseurs**[87]**; la rotation est un choix du cadre.

`EXIG-AUT-21` **· DOIT**

**Mesure de la qualité de la supervision**

La plateforme **DOIT** produire chaque mois, par approbateur et par cas d’usage : le taux d’approbation sans modification, les taux de rejet et de modification, le temps de réponse, les renversements suspects (action refusée puis approuvée) et les approbateurs dont le taux d’approbation sans modification ou le temps de réponse s’écarte de la médiane du cas d’usage d’un seuil fixé par le comité. Pour les appels d’outils à effet exécutés sans approbation préalable aux niveaux N3 et N4, une revue humaine a posteriori **DOIT** porter sur un échantillon stratifié par risque : 5 % de ces appels pour la classe modérée et 1 % pour la classe faible (choix du cadre), bornés par une taille minimale et une taille maximale absolues par période, que le comité fixe pour détecter un taux d’anomalie cible avec une confiance déclarée (EXIG-EVA-03). La comparaison à la médiane exige au moins trois approbateurs par cas d’usage; à défaut, la référence est prise entre cas d’usage comparables. Le comité **DOIT** fixer ces seuils d’alerte par cas d’usage et examiner les écarts signalés.

Pourquoi : l’IMDA recommande de suivre le taux d’intervention des réviseurs (rejet ou modification des actions de l’agent), dont un niveau bas peut signaler une approbation machinale, et le temps de réponse des réviseurs**[76]**; l’OWASP recommande de détecter les renversements suspects**[87]** et le NIST juge utile de recueillir la fréquence des cas où une personne passe outre aux sorties du système, et leurs motifs**[74]**. Aucune source reconnue ne fixe de seuil universel.

## 8.8 Décisions automatisées et droit à la révision

Quand un agent décide seul à propos d’une personne, la Loi 25 crée des droits précis, et une approbation de pure forme ne les fait pas disparaître; la section 12.2 traite l’ensemble des obligations.

L’article 12.1 de la Loi sur la protection des renseignements personnels dans le secteur privé (RLRQ, c. P-39.1, « Loi sur le privé ») vise toute décision fondée exclusivement sur un traitement automatisé de renseignements personnels. L’entreprise doit en informer la personne au plus tard au moment où elle lui communique la décision. À la demande de la personne, elle l’informe des RP utilisés, des raisons et des principaux facteurs et paramètres ayant mené à la décision, ainsi que de son droit de faire rectifier ces renseignements. La personne doit pouvoir présenter ses observations à un membre du personnel en mesure de réviser la décision**[56, 316]**. Le défaut d’informer la personne de la décision ou de lui donner l’occasion de présenter ses observations, en contravention à l’article 12.1, est expressément un motif de sanction administrative pécuniaire (art. 90.1, par. 5°)**[56, 317]**, et les renseignements utilisés pour prendre une décision doivent être conservés au moins un an après celle-ci (art. 11)**[56]**. Pour les organismes publics, la disposition équivalente est l’article 65.2 de la Loi sur l’accès aux documents des organismes publics et sur la protection des renseignements personnels (RLRQ, c. A-2.1, « Loi sur l’accès »)**[318]**.

Qu’est-ce qui rend une décision « exclusivement » automatisée? Selon l’interprétation gouvernementale de l’article 65.2, c’est le cas lorsqu’aucune personne physique n’a exercé de contrôle important : une intervention humaine mineure, sans effet réel sur le résultat, ne fait pas échapper à l’obligation, alors qu’un outil d’aide qui fournit des éléments à un employé qui décide lui-même n’est pas visé. Cette interprétation précise aussi qu’il n’est pas requis de divulguer l’algorithme : le mot « principaux » limite l’explication aux facteurs déterminants**[318]**. Sous le règlement général sur la protection des données de l’Union européenne (RGPD), les lignes directrices WP251rev.01 vont dans le même sens : on ne peut contourner la règle en fabriquant une intervention humaine, et le contrôle doit être exercé par une personne qui a l’autorité et la compétence de modifier la décision**[319]**.

**DROIT APPLICABLE**

La Commission d’accès à l’information (CAI) n’a pas publié de critères de l’intervention humaine significative pour le secteur privé. Les exigences ci-dessous constituent une interprétation prudente du cadre, fondée par analogie sur l’article 65.2 et sur WP251rev.01; leur application à un cas précis relève des affaires juridiques.

`EXIG-AUT-22` **· DOIT**

**Décisions visées par l’article 12.1**

Voir l’EXIG-CON-07 (obligations envers la personne), l’EXIG-CON-08 (révision humaine significative) et l’EXIG-CON-09 (conservation), qui font foi. Règle résiduelle : tout agent dont les décisions concernant une personne sont fondées exclusivement, au sens de l’EXIG-CON-08, sur un traitement automatisé de ses RP **DOIT** être de classe élevée.

Pourquoi : obligations de l’article 12.1 et de l’article 11 de la Loi sur le privé (pour un organisme public, l’article 65.2 de la Loi sur l’accès prévoit des obligations d’information équivalentes)**[56]**; une obligation légale n’a qu’une source dans le cadre, le chapitre 12.

`EXIG-AUT-23` **· DOIT**

**Révision humaine significative**

Voir l’EXIG-CON-08, qui porte le test de révision humaine significative (autorité, compétence, accès à toutes les données pertinentes, temps) et la qualification, faite a priori à l’EFVP et à la fiche, avec un défaut prudent : la décision est réputée exclusivement automatisée tant que la preuve contraire n’y est pas consignée. Règle résiduelle : les indicateurs de l’EXIG-AUT-21 servent de contrôle a posteriori; un écart requalifie la décision et déclenche les avis dus (EXIG-CON-07). Le degré d’intervention humaine et l’étape où elle a lieu **DOIVENT** être consignés dans l’EFVP.

Pourquoi : interprétation prudente du cadre, et non règle expresse de la Loi 25; par analogie, une validation de pure forme ne retire pas le caractère exclusivement automatisé selon l’interprétation gouvernementale de l’article 65.2 (secteur public)**[318]**, et WP251rev.01 demande de consigner dans l’analyse d’impact le degré et l’étape de l’intervention humaine**[319]**.
