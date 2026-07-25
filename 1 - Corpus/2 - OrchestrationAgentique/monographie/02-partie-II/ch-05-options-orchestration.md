# Chapitre 5 — Les options d'orchestration : la taxonomie OO1–OO4

| Champ | Valeur |
|---|---|
| Statut | Rédigé (premier jet fusionné, après relecture adversariale) |
| Date de gel de l'information | 16 juillet 2026 |
| Socle mobilisé (PRD §7) | **F-37** (entrée unique assignée par [TOC.md](../../TOC.md)) ; F-36, F-46, F-01 et F-02 en **renvoi seulement** — aucun contenu repris ici (ch. 2, ch. 6, ch. 13). Un terme du glossaire §D.2 tracé à **F-15** (« humain-dans-la-boucle ») est employé en §5.3 ; aucun contenu de F-15 n'est repris. Aucun énoncé de droit canadien : les renvois aux ch. 11 et 13 sont secs |
| Garde-fous à surveiller (PRD §8) | **Réserves F-37** : préprint v1 non révisé par les pairs, menaces à la validité déclarées par ses propres auteurs — le cadre conceptuel est repris comme référence, les chiffres à titre d'illustration seulement (formulation imposée, PRDPlan §4.4). Réserve F-01 (motif « sécuris » à proximité de MCP) ; R-8 (motif « plan de contrôle » — non employé dans ce chapitre) |
| Volumétrie cible | ~3200 mots |

> **Thèse ([TOC.md](../../TOC.md))** : Le choix d'architecture agentique est un choix de position sur un continuum d'encadrement, objectivable par cinq propriétés et sept critères.

---

L'architecte à qui l'on demande d'« introduire de l'agentique » dans un processus d'octroi de crédit reçoit, en réalité, une question mal posée. Elle suggère une alternative binaire — un processus déterministe *ou* des agents — là où le problème est de savoir qui commande à qui. Un agent peut appeler un processus ; un processus peut appeler un agent ; les deux peuvent s'ignorer, ou se connaître. Ces situations ne diffèrent pas par le degré d'intelligence mise en œuvre : elles diffèrent par la localisation du contrôle. **Lecture de l'auteur** : c'est cette localisation, et non la sophistication du modèle sous-jacent, qui commande ce qu'un exploitant peut établir au sujet de son système. La portée réglementaire de ce constat — ce qu'une institution financière canadienne doit pouvoir démontrer, reconstituer ou défendre — n'est pas établie par le socle de ce chapitre ; la Partie III en établit le contenu et le chapitre 13 la traduction en architecture.

Ce chapitre fournit le vocabulaire de cette distinction. Il l'emprunte à une source unique, et il faut le dire avant d'aller plus loin plutôt qu'après : le cadre présenté ici est celui de Rinderle-Ma, Mangler et leurs coauteurs (TU Munich, arXiv:2606.31518v1), **préprint non révisé par les pairs** dont les auteurs déclarent eux-mêmes des menaces à la validité — le cadre conceptuel est repris ici, les résultats chiffrés à titre d'illustration[^1]. Cette réserve n'est pas une clause de style. Elle commande la manière dont le chapitre distingue, à chaque section, ce qui relève d'une construction conceptuelle réutilisable de ce qui relève d'une expérimentation initiale dont nul ne prétend qu'elle est concluante.

## 5.1 Les quatre options d'orchestration

Le cadre repose sur une taxonomie de quatre **options d'orchestration** (*orchestration options*), notées OO1 à OO4[^2]. Elles se lisent le long de deux axes : la connaissance du processus — qui, de l'agent ou du cadre d'exécution, la détient — et le commandement de l'enchaînement, c'est-à-dire qui décide de l'ordre des opérations.

**OO1 — l'orchestration agentique agnostique au processus.** Des agents collaborent sans qu'aucun cadre explicite ne décrive le processus qu'ils accomplissent. Le socle en donne les moyens techniques : MCP pour l'accès des agents à leurs outils, A2A pour la collaboration entre agents[^2]. Le chapitre 2 en examine l'anatomie ; ce qui importe ici est la conséquence architecturale. En OO1, le processus n'existe nulle part sous forme explicite — ni dans un modèle, ni dans un moteur, ni dans une invite. Il n'existe qu'à titre de propriété émergente de la conversation entre agents. On peut l'observer *a posteriori* dans les journaux, si tant est qu'il y en ait ; on ne peut pas le *lire* avant l'exécution.

**OO2 — l'orchestration agentique consciente d'un cadre.** Les agents restent maîtres de l'enchaînement, mais un cadre leur est communiqué — par l'invite ou par le contexte[^2]. La différence avec OO1 est réelle : le processus est désormais quelque part, il est écrit. **Lecture de l'auteur** : il est écrit à l'endroit précis où sa force exécutoire dépend de la coopération du modèle — un cadre transmis par le contexte est une consigne, non une contrainte. Le socle définit OO2 par le canal de transmission du cadre (invite, contexte) ; il ne se prononce pas sur sa force exécutoire.

**OO3 — l'orchestration de processus invoquant des agents agnostiques.** L'inversion s'opère ici. C'est le processus qui orchestre, et il invoque des agents qui, eux, ignorent le processus dans lequel ils s'insèrent[^2]. L'agent devient une ressource appelée par une activité, au même titre qu'un service. Il conserve son autonomie *à l'intérieur* de la tâche qui lui est confiée — c'est bien un agent, non une fonction — mais l'enchaînement, lui, n'est plus négociable.

**OO4 — l'orchestration explicite d'agents conscients du processus.** Le processus orchestre, et les agents savent qu'ils opèrent dans un processus[^2]. C'est la seule des quatre options où les deux axes sont saturés : le cadre commande *et* l'agent le connaît. **Lecture de l'auteur** : elle ne fait donc pas de la conscience du processus par l'agent un substitut à l'encadrement, mais un ajout à celui-ci ; c'est vraisemblablement l'option la plus exigeante à construire. Le socle définit les quatre options ; il n'établit aucun ordre de coût entre elles.

Deux propriétés de cette taxonomie méritent d'être relevées, parce qu'elles conditionnent son usage. La première est que le cadre déclare des **transitions fluides entre options**[^2] : il ne s'agit pas de quatre catégories étanches dans lesquelles ranger un système, mais de positions sur un continuum, entre lesquelles une architecture peut se déplacer — et, ajoutons-le, dériver. La seconde est qu'aucun des deux axes n'est celui de la capacité. Rien, dans cette taxonomie, ne dit qu'un système OO4 emploie des modèles plus faibles ou des agents moins autonomes qu'un système OO1. Ce qui se déplace d'un bout à l'autre du continuum, c'est le lieu où réside la connaissance du processus et la main qui en commande l'enchaînement — donc le lieu où l'on peut agir sur lui.

Le socle établit que, de OO1 à OO2, on ajoute une description ; que de OO3 à OO4, on ajoute une connaissance ; et que de OO2 à OO3, la main qui tient l'enchaînement change — l'agent cesse d'orchestrer et devient orchestré[^2]. Autrement dit, OO1 et OO2 se distinguent l'une de l'autre par ce que l'agent *sait*, comme OO3 et OO4 entre elles ; c'est le passage de OO2 à OO3 qui change ce qu'il *commande*. **Lecture de l'auteur** : c'est donc entre OO2 et OO3 que se situe la seule discontinuité véritable de la série. Un architecte qui hésite entre OO2 et OO3 ne choisit donc pas entre deux degrés d'une même chose, mais entre deux régimes de responsabilité — dans l'un, l'écart au processus est un comportement possible du système ; dans l'autre, il n'est pas exprimable. Le socle établit la définition de chaque option et la fluidité des transitions ; il ne hiérarchise pas ces transitions et ne désigne aucune d'elles comme un seuil.

**Lecture de l'auteur** : cette taxonomie fournit à un comité d'architecture ce que le vocabulaire courant lui refuse — une question fermée. Demander « ce système est-il agentique ? » n'appelle pas de réponse vérifiable ; demander « où est écrit le processus, et qui peut s'en écarter ? » n'admet, dans ce cadre, que quatre réponses. Le socle établit la taxonomie et ses transitions ; il n'établit pas qu'elle suffise à classer tout système réel sans ambiguïté, et le présent ouvrage ne le prétend pas.

## 5.2 Les cinq propriétés d'évaluation

Une taxonomie qui ne se paie pas ne sert à rien. Le cadre associe donc aux quatre options cinq **propriétés d'évaluation** : l'autonomie (*autonomy*), la spécificité de tâche (*task specificity*), la réactivité (*responsiveness*), l'**assurance de correction** (*correctness assurance*) et la **traçabilité/tractabilité** (*traceability / tractability*)[^3]. Ce sont les cinq dimensions sur lesquelles se lit le prix d'un positionnement.

L'**autonomie** est la latitude laissée à l'agent de décider. La **spécificité de tâche** exprime le degré auquel le comportement est taillé pour une tâche déterminée plutôt que général. La **réactivité** désigne la capacité à répondre à un événement dans les délais requis. L'**assurance de correction** est la garantie que le résultat est conforme à l'attendu. La **traçabilité/tractabilité**, enfin, est la capacité à reconstituer et à suivre l'exécution.

Il faut résister à la tentation de remplir mentalement la grille de quatre options par cinq propriétés en y portant des jugements de bon sens. **Lecture de l'auteur** : l'intuition selon laquelle l'autonomie décroîtrait mécaniquement de OO1 à OO4 tandis que la correction et la traçabilité croîtraient dans le même mouvement est plausible ; mais le seul résultat rapporté à la section 5.4 n'en corrobore que le volet correction, aucune mesure n'y porte sur la traçabilité par option, et l'autonomie n'y dispose d'aucune métrique. **Le socle ne l'établit pas comme une propriété générale de la taxonomie**. Ce que le socle établit, c'est une grille d'évaluation et un jeu de résultats expérimentaux sur un scénario. Un architecte qui présenterait à son comité de risque une matrice complète 4 × 5 en la créditant à cette source lui ferait dire ce qu'elle ne dit pas.

Le choix même des cinq propriétés mérite pourtant d'être commenté. **Lecture de l'auteur** : quatre d'entre elles — la spécificité de tâche, l'assurance de correction, la réactivité et la traçabilité — sont des propriétés que l'on *démontre* à un tiers ; ce sont exactement celles que la section 5.4 montrera instrumentées, et l'instrumentation est précisément ce qui rend une propriété opposable. Elles ne décrivent pas ce que le système sait faire, mais ce que l'exploitant peut établir à son sujet. Seule l'autonomie échappe à ce registre : elle qualifie la latitude de la machine, non ce qu'on peut en prouver. Le socle énumère les cinq propriétés sans les répartir ; ce partage est une construction du présent ouvrage. La grille de F-37 est ainsi orientée vers la démonstrabilité — ce qui, sous cette réserve, fonde sa pertinence pour notre objet. Les chapitres 9 à 12 établissent le contenu des obligations canadiennes, et le chapitre 13 en opère la traduction en contraintes d'architecture ; le socle du présent chapitre ne porte aucune caractérisation de ces obligations.

## 5.3 Les sept critères de sélection

Aux propriétés — qui décrivent ce qu'une orchestration *procure* — répondent des critères, qui décrivent ce que la situation *exige*. Le cadre en énonce sept, qualitatifs : la complexité du but, la supervision humaine, les contraintes, l'action humaine, l'espace de décision, l'effort initial et la maintenance[^4].

Les cinq premiers caractérisent le processus lui-même. La **complexité du but** est celle de l'objectif poursuivi. La **supervision humaine** est le degré de contrôle humain requis sur l'exécution. Les **contraintes** sont les obligations qui pèsent sur le déroulement — le socle emploie le terme général, et il faut se garder de le rétrécir : les contraintes réglementaires en sont une espèce, non le genre. L'**action humaine** désigne la présence d'interventions humaines dans le processus. L'**espace de décision** est l'étendue des choix ouverts à chaque point.

Que la supervision humaine et l'action humaine figurent comme deux critères séparés, et non comme un seul, est le détail le plus instructif de cette liste[^4]. Le socle les énonce distinctement ; il n'en donne pas la définition différentielle, et le présent ouvrage ne la fabriquera pas. **Lecture de l'auteur** : la distinction paraît recouvrir celle d'un humain qui *surveille* un processus et d'un humain qui y *accomplit une tâche* — deux situations qu'une architecture ne traite pas de la même façon, la première appelant un point d'observation, la seconde un point d'arrêt, c'est-à-dire un humain-dans-la-boucle (*human-in-the-loop*). Le lecteur canadien mesurera l'enjeu en se reportant au chapitre 11, qui traite de la révision humaine de l'article 12.1 de la Loi 25 et de son rapport à ces figures. Le présent chapitre note seulement que la grille de sélection distingue deux formes de présence humaine là où le discours d'architecture courant n'en connaît qu'une.

Les deux derniers — l'**effort initial** et la **maintenance** — changent de nature, et c'est ce qui rend cette liste intéressante. Ils ne caractérisent pas le processus : ils caractérisent son coût de possession. Le socle établit que l'effort initial et la maintenance figurent explicitement parmi les sept critères[^4] ; il ne documente pas l'intention des auteurs du cadre. **Lecture de l'auteur** : leur présence dans la grille interdit de traiter le choix d'orchestration comme une pure question de conformité fonctionnelle. Un positionnement OO3 ou OO4 exige d'expliciter le processus ; expliciter un processus coûte, à la construction comme à l'entretien — et la grille place ce coût parmi les termes de la décision plutôt que hors d'elle.

**Lecture de l'auteur** : c'est précisément là que se joue la sincérité d'une décision d'architecture en institution financière. La discipline de l'encadrement se paie en effort initial et en maintenance, et il est plus confortable de justifier un positionnement OO1 par son agilité que par son moindre coût d'entrée. Le socle n'établit ni cette économie politique de la décision, ni aucun ordre de grandeur de ces coûts ; il établit que l'effort initial et la maintenance figurent explicitement parmi les critères de sélection, ce qui interdit de les traiter comme des considérations subalternes.

Une remarque de méthode, enfin, sur l'usage de ces sept critères. Le socle les qualifie de **critères qualitatifs de sélection**[^4] : ils orientent un jugement, ils ne calculent pas une réponse. Aucune fonction de score, aucune pondération, aucun arbre de décision ne les relie aux quatre options. Une institution qui voudrait industrialiser ce choix — et il est légitime qu'elle le veuille, pour le rendre reproductible d'un projet à l'autre — devra construire elle-même cette pondération, et l'assumer comme sa propre décision d'entreprise plutôt que comme une conclusion de la littérature. Le chapitre 19 reprend ces critères pour positionner des cas d'usage financiers sur la taxonomie ; il le fera sous cette réserve.

## 5.4 Les métriques quantitatives et les résultats expérimentaux

Le cadre propose enfin une instrumentation des propriétés de la section 5.2. La spécificité de tâche s'y mesure par la complexité cyclomatique (*cyclomatic complexity*) et par la métrique ABC ; l'assurance de correction, par la précision, le rappel et le F1 (*precision, recall, F1*) ; la réactivité, par le taux de faux négatifs (*false negative rate*, FNR) et par la vitesse de réaction ; la traçabilité, par la correction du journal (*log correctness*)[^5].

Deux observations s'imposent sur cette liste, et la première porte sur ce qui n'y figure pas : **l'entrée F-37 du socle ne rapporte aucune métrique quantitative pour l'autonomie**[^5]. Le lecteur remarquera que les quatre propriétés instrumentées sont exactement celles que la section 5.2 range du côté de la démonstrabilité — spécificité, correction, réactivité, traçabilité —, et que la seule qui reste sans mesure est celle qui décrit la latitude laissée à la machine. Le présent chapitre ne conclut rien de ce silence : l'entrée du socle ne rapporte aucune métrique d'autonomie, et établir si l'article lui-même n'en propose pas relèverait d'une relecture ciblée du préprint, qui n'est pas conduite ici. Il le signale, parce qu'un architecte qui bâtirait un tableau de bord sur ces métriques trouverait le trou lui-même.

La seconde observation est que ces métriques sont, dans leur majorité, empruntées à des disciplines établies — le génie logiciel pour la complexité cyclomatique et la métrique ABC, l'évaluation des classifieurs pour la précision, le rappel et le F1. **Lecture de l'auteur** : cet emprunt est un atout pratique — ce sont des mesures que les fonctions de validation d'une institution financière savent déjà lire — et il appelle une prudence, car une métrique importée conserve les hypothèses de son domaine d'origine. Le socle établit la liste des métriques proposées ; il n'établit pas leur validité comme indicateurs de risque en contexte financier. Le chapitre 20 examine leur candidature à ce titre, et la présente comme telle.

Viennent les résultats. Sur un scénario d'éclairage prédictif, le cadre rapporte un F1 de **0,40 pour l'orchestration non encadrée (OO1)**, de **0,97 pour l'orchestration encadrée d'agents (OO4)** et de **1,00 pour le déterministe pur**[^6]. Ces trois nombres sont, dans ce chapitre, des illustrations et rien d'autre. Les auteurs déclarent eux-mêmes des menaces à la validité : expériences initiales, invites non comparées entre elles, facteurs confondants[^1]. Un scénario d'éclairage n'est pas un processus de crédit ; un F1 obtenu une fois sur une tâche d'éclairage prédictif ne se transporte pas dans un dossier réglementaire canadien. Ces chiffres n'entrent dans cet ouvrage ni comme preuve, ni comme ordre de grandeur transposable, ni comme argument.

Deux enseignements plus robustes accompagnent ces mesures, et ceux-là sont des énoncés de conception, non des mesures ponctuelles. Le premier, tel que le socle l'énonce : la journalisation confiée aux agents « n'est généralement pas recommandée »[^6]. **Lecture de l'auteur** : si la trace n'est pas produite par l'agent, elle doit l'être ailleurs — faute de quoi la traçabilité dépend de la bonne volonté de la partie dont on cherche justement à contrôler le comportement. Le socle déconseille le producteur ; il n'en désigne aucun autre, et le choix de ce lieu reste une décision d'architecture. Le second enseignement : les contraintes temporelles exigent des *frames* ou des outils externes, les temps de raisonnement des modèles de langage étant imprévisibles[^6]. Un délai qui doit être tenu ne peut pas être confié à un composant dont la durée d'exécution n'est pas bornée ; la Partie IV examine les contraintes temporelles des rails de paiement canadiens.

Reste le verdict, que le socle rattache à la même entrée. Sur un scénario soumis à une réglementation stricte — un processus de don de sang régi par la directive européenne 2002/98/CE —, le cadre conclut que **l'orchestration non encadrée est « inacceptable » lorsque des exigences strictes d'exécution et de documentation s'appliquent, et que les tâches essentielles doivent être imposées de façon déterministe par le cadre**[^7].

Il faut manier ce verdict avec exactitude. Il est adossé au même préprint et aux mêmes réserves ; il porte sur un scénario européen, dans un domaine qui n'est pas la finance, sous une directive qui n'a aucune application au Canada. **Lecture de l'auteur** : ce qui paraît transposable n'est pas le verdict lui-même mais son mécanisme — dès lors qu'une exigence porte sur la *manière* dont une tâche doit être exécutée et documentée, et non seulement sur son résultat, un dispositif qui ne peut ni garantir l'exécution ni produire la trace échoue à l'exigence, quel que soit son taux de réussite moyen. Le socle établit le verdict pour son scénario ; il n'établit pas sa transposition au cadre canadien. Cette transposition est l'objet du chapitre 13, qui la conduit explicitement et l'expose comme un raisonnement, non comme un fait rapporté.

> **État de la connaissance vérifiable — sur quoi repose exactement la taxonomie OO1–OO4**
>
> Question : de quel niveau de validation empirique la taxonomie OO1–OO4 et son verdict sur les scénarios réglementés disposent-ils ?
>
> Ce que le socle établit, à la date de gel du présent chapitre (16 juillet 2026) : le cadre est porté par **une seule source**, un préprint versé le 30 juin 2026 — seize jours avant cette date de gel — et non révisé par les pairs, dont les auteurs déclarent des menaces à la validité de leurs propres expériences (expériences initiales, invites non comparées, facteurs confondants)[^1]. Les résultats chiffrés proviennent d'un scénario d'éclairage prédictif ; le verdict sur les contextes réglementés, d'un scénario de don de sang sous directive européenne[^6][^7].
>
> Ce que le socle n'établit pas : aucune reproduction indépendante de ces résultats ; aucune application documentée de la taxonomie à un processus d'institution financière, canadienne ou autre ; aucune validation des métriques proposées comme indicateurs de risque en contexte financier.
>
> Recherche menée le 16 juillet 2026 : le seul corpus interrogé est le socle du PRD (§7 et §9.1, 77 sources récupérées) ; il ne contient ni reproduction indépendante des résultats de F-37, ni application financière documentée de la taxonomie. Aucune recherche externe nouvelle n'a été conduite pour ce chapitre — la lacune est portée en signalement de gouvernance (candidate à une entrée §10 du PRD), et non résolue ici.
>
> En l'absence de source primaire, la question reste ouverte ; aucune inférence n'est proposée ici. Le présent ouvrage retient donc le cadre pour ce qu'il vaut — un vocabulaire d'architecture et une grille d'analyse — et s'interdit d'en tirer une preuve. La force du principe d'encadrement ne repose pas, dans cet ouvrage, sur ce seul préprint : le chapitre 13 en établit la convergence avec deux autres sources (F-36, F-46). Ces sources ne sont pas pleinement indépendantes — une autrice de F-37 cosigne F-36 —, et le chapitre 13 en tient compte.

## Ce que ce chapitre établit, et ce qu'il ne dit pas

Trois acquis pour la suite. **Premièrement**, un vocabulaire : quatre options d'orchestration ordonnées par la localisation de la connaissance du processus, avec des transitions fluides entre elles, et non des catégories étanches. La question « ce système est-il agentique ? » est remplacée par « où est écrit le processus, et qui peut s'en écarter ? ». **Deuxièmement**, une grille de coût : cinq propriétés d'évaluation — dont quatre, selon la lecture proposée ici et non selon le socle, sont des propriétés de démonstrabilité — et sept critères de sélection dont deux, l'effort initial et la maintenance, interdisent de présenter l'encadrement comme gratuit. **Troisièmement**, deux enseignements de conception utilisables immédiatement : la journalisation n'est généralement pas à confier aux agents — d'où la question, ouverte, du lieu où la trace se produit —, et un délai à tenir ne se confie pas à un composant dont la durée d'exécution est imprévisible.

Ce que ce chapitre ne dit pas doit être énoncé avec la même netteté. Il ne dit pas qu'un positionnement OO4 soit *démontré* supérieur à un positionnement OO1 : il rapporte un écart de F1 mesuré une fois, sur un scénario d'éclairage prédictif, par un préprint dont les auteurs avertissent des menaces à la validité. Il ne dit pas que la grille des cinq propriétés puisse être remplie option par option — le socle ne porte pas cette matrice. Il ne dit pas non plus ce qu'est un *frame*, ni comment on l'écrit : la distinction entre frames normatifs et opérationnels, et les capacités qu'un système doit posséder pour être gouverné par eux, relèvent du chapitre 6. Il ne dit rien, enfin, du droit canadien, dont la Partie III établit le contenu et le chapitre 13 la traduction en architecture.

La taxonomie OO1–OO4 n'est pas une recommandation. C'est un instrument de mesure de la position que l'on occupe — y compris lorsqu'on ne l'a pas choisie.

---

## Notes

[^1]: PRD §7.7, **F-37** (niveau [B] — article lu intégralement ; confiance haute pour le cadre, moyenne pour les chiffres). Source primaire : Rinderle-Ma, Mangler et al. (TU Munich), « Design and Implementation of Agentic Orchestrations and Orchestration of Agents », arXiv:2606.31518v1, 30 juin 2026. **Réserves F-37** : préprint v1 non révisé par les pairs ; les auteurs déclarent eux-mêmes des menaces à la validité (expériences initiales, invites non comparées, facteurs confondants). Formulation imposée : PRDPlan §4.4, cas « préprint académique » — le cadre conceptuel est repris comme référence, les résultats chiffrés à titre d'illustration seulement.

[^2]: PRD §7.7, **F-37**, apport (1) : taxonomie des quatre options d'orchestration — OO1 orchestration agentique agnostique au processus (MCP pour les outils, A2A pour la collaboration, aucun cadre explicite) ; OO2 orchestration agentique consciente d'un cadre (invite/contexte) ; OO3 orchestration de processus invoquant des agents agnostiques ; OO4 orchestration explicite d'agents conscients du processus ; transitions fluides entre options. Source primaire : arXiv:2606.31518v1. Sur MCP et A2A eux-mêmes (F-01, F-02) : voir ch. 2 — aucun contenu n'en est repris ici.

[^3]: PRD §7.7, **F-37**, apport (2) : cinq propriétés d'évaluation — autonomie, spécificité de tâche, réactivité, assurance de correction, traçabilité/tractabilité. Source primaire : arXiv:2606.31518v1. Formes terminologiques imposées : `monographie/90-annexes/annexe-d-glossaire.md` §D.2.

[^4]: PRD §7.7, **F-37**, apport (3), volet qualitatif : critères de sélection — complexité du but, supervision humaine, contraintes, action humaine, espace de décision, effort initial, maintenance. Source primaire : arXiv:2606.31518v1. Le socle les qualifie de **critères qualitatifs** ; il ne documente ni pondération, ni fonction de score, ni règle de décision les reliant aux options.

[^5]: PRD §7.7, **F-37**, apport (3), volet quantitatif : complexité cyclomatique et métrique ABC pour la spécificité ; précision, rappel et F1 pour la correction ; FNR et vitesse de réaction pour la réactivité ; correction du journal pour la traçabilité. Source primaire : arXiv:2606.31518v1. **L'entrée du socle ne rapporte aucune métrique quantitative pour la cinquième propriété (l'autonomie)** — constat sur l'entrée F-37 du socle, non sur l'article. F-37 est de niveau [B] pour lecture intégrale (PRD Annexe A) ; trancher si l'absence est celle de l'article supposerait une relecture ciblée du préprint, non conduite pour ce chapitre.

[^6]: PRD §7.7, **F-37**, apport (4) : résultats empiriques sur un scénario d'éclairage prédictif — F1 de 0,40 (OO1), 0,97 (OO4) et 1,00 (déterministe pur) ; enseignements : la journalisation confiée aux agents « n'est généralement pas recommandée » ; les contraintes temporelles exigent des frames ou outils externes, les temps de raisonnement des modèles de langage étant imprévisibles. Source primaire : arXiv:2606.31518v1. **Chiffres cités en illustration seulement** (réserves F-37, note 1).

[^7]: PRD §7.7, **F-37**, apport (5) : verdict pour les scénarios réglementés (processus de don de sang sous directive 2002/98/CE) — l'orchestration non encadrée est « inacceptable » quand des exigences strictes d'exécution et de documentation s'appliquent ; les tâches essentielles doivent être imposées de façon déterministe par le cadre. Source primaire : arXiv:2606.31518v1, sous les réserves de la note 1. La convergence de ce verdict avec F-36 (manifeste APM) et F-46 (architecture de référence d'IBM) est établie au **ch. 13** ; elle n'est pas reprise ici (périmètre TOC.md).

<!-- Boucle qualité PRDPlan §4.2 — état :
     1. Rédaction ................ fait (gel : 16 juillet 2026)
     2. Traçabilité (CA-1, CA-5) . fait (7 notes, toutes tracées à F-37 + arXiv:2606.31518v1 ;
                                   termes anglais en italique entre parenthèses à la 1re occurrence du chapitre :
                                   orchestration options, autonomy, task specificity, responsiveness,
                                   correctness assurance, traceability/tractability, cyclomatic complexity,
                                   precision/recall/F1, false negative rate, log correctness, human-in-the-loop)
     3. Balayage garde-fous ...... fait (réserve F-37 : formulation « préprint » de §4.4 posée en ouverture, répétée
                                   à chaque occurrence des chiffres et en encadré ; motif « sécuris » : absent ;
                                   motifs R-8 « ACP » / « control plane » / « plan de contrôle » : absents ;
                                   motif R-7 « E-23 » : absent — renvois aux ch. 9/11/13/20 sans affirmation ;
                                   motif §8.2.2 « % » : absent ; aucun chiffre auto-déclaré d'institution ou d'éditeur)
     4. Relecture adversariale ... fait (deux relecteurs indépendants ; 14 constats bloquants et 16 réserves,
                                   pour l'essentiel des doublons entre les deux rapports. Réfutations retenues
                                   et corrigées :
                                   - RENVOI FAUX : « les trois chapitres de la Partie III » — la Partie III en
                                     compte cinq (ch. 9-13, TOC.md). Corrigé en « les chapitres 9 à 12 […] et le
                                     chapitre 13 ». Même famille que le « dix-huit mois » du ch. 1 : cardinal
                                     dérivé jamais recalculé contre le TOC. LEÇON : recompter tout cardinal annoncé.
                                   - TAXONOMIE INVERSÉE (§5.1) : « les trois premières options se distinguent par
                                     ce que l'agent sait ; la troisième et la quatrième, par ce qu'il commande »
                                     — faux au regard de F-37 (OO3 = le processus commande déjà) et contredit par
                                     les deux phrases précédentes du même paragraphe. Le partage correct est
                                     {OO1, OO2} l'agent commande / {OO3, OO4} le processus commande ; à l'intérieur
                                     de chaque paire, c'est la connaissance qui varie. Réécrit ; marqueur
                                     « Lecture de l'auteur » déplacé en tête de la stretch interprétative.
                                     Racine corrigée aussi : l'« axe unique » posé en ouverture de §5.1 (le socle
                                     n'en pose aucun) → deux axes, connaissance et commandement.
                                   - AUTOCONTRADICTION 3 vs 4 : §5.2 comptait trois propriétés démontrables,
                                     §5.4 et la conclusion quatre. Réconcilié sur QUATRE (l'instrumentation de
                                     §5.4 inclut la spécificité) et marqué « Lecture de l'auteur » aux trois
                                     endroits — le socle liste cinq propriétés sans les répartir.
                                   - FAUSSETÉ SUR L'OUVRAGE (§5.4) : « il ne dispose pas de la source complète »
                                     — contredit F-37 [B — article lu intégralement] et PRD Annexe A ; le PDF est
                                     au dépôt. La contrainte de périmètre du rédacteur n'est pas une propriété de
                                     l'ouvrage (CA-6). Reformulé sur l'entrée du socle ; note [^5] alignée.
                                   - INFÉRENCES NON MARQUÉES, toutes marquées ou réduites au socle : thèse
                                     d'ouverture (portée réglementaire renvoyée aux Parties III/ch. 13) ;
                                     « un cadre transmis par le contexte est une consigne » ; « OO4 la plus
                                     exigeante à construire » (le socle n'ordonne aucun coût) ; « la trace doit
                                     être produite par l'orchestrateur » (le socle déconseille un producteur,
                                     n'en désigne aucun) ; intention prêtée aux auteurs du cadre (« refuse de »,
                                     « pose ce coût sur la table ») ; rapprochement avec les fenêtres de règlement.
                                   - DROIT CANADIEN hors socle : caractérisation des obligations canadiennes en
                                     §5.2 et énoncé de droit québécois en §5.3 (art. 12.1 sans F-27 ni note) —
                                     tous deux contredisaient la clôture « Il ne dit rien, enfin, du droit
                                     canadien ». Réduits à des renvois secs (ch. 9-12, ch. 11, ch. 13).
                                   - EMBELLISSEMENT : « domotique » (2 occ. + conclusion) — F-37 dit « éclairage
                                     prédictif », le domaine était inventé. Corrigé aux trois endroits.
                                   - « sources indépendantes » (encadré) : Rinderle-Ma cosigne F-36 ET F-37 ;
                                     PRD B.1 écrit « trois sources » sans l'adjectif. Corrigé + non-indépendance
                                     explicitée.
                                   - CAUTION EMPIRIQUE SURESTIMÉE (§5.2) : « cohérente avec les résultats » pour
                                     une intuition à trois volets dont un seul (correction) est mesuré. Borné.
                                   - ENCADRÉ §4.4 : segment « Recherche menée le [date] » absent, « sources
                                     supplémentaires » au lieu de « source primaire ». Forme imposée rétablie ;
                                     l'absence de recherche externe est désormais dite explicitement.
                                   - CA-5 : « autonomie » et « réactivité » sans équivalent anglais alors que les
                                     trois autres propriétés en portaient un. Ajoutés.
                                   - En-tête : F-15 (terme de glossaire employé) déclaré ; F-27 retiré du corps.
                                   - Réserve 16 (mineure) : référence arXiv portée en corps à l'ouverture.
                                   Constat écarté : aucun. Réserve appliquée partiellement : n° 12 (périmètre du
                                   verdict) — le jugement de valeur non marqué « la contribution la plus lourde »
                                   est retiré, mais le verdict et son mécanisme restent exposés, sous renvoi
                                   explicite au ch. 13 ; le retrait complet relève d'un arbitrage TOC/PRD ci-dessous.)
     5. Commit + registre de gel . FAIT — pièce fusionnée, enregistrée au registre de gel
        et publiée (étiquette mono-v1.0).
        ⚠ Statut rectifié le 17 juillet 2026 (audit global). Il portait « À FAIRE » sur une
        pièce publiée depuis son gel. Défaut systémique : 16 des 29 pièces le portaient ;
        l'audit global n'en avait relevé que 4, faute d'avoir balayé son domaine entier.
        « Un statut qui ment est pire qu'un statut absent » (PRD v1.9) : la règle vaut
        pour le bloc qui l'énonce.

     Signalements de gouvernance (ne pas corriger ici — PRD/TOC/PRDPlan font autorité) :
     - PRD §6 (Partie VI) énumère cinq critères de sélection (« complexité du but, supervision humaine,
       contraintes réglementaires, action humaine, espace de décision ») là où F-37 §7.7 en donne sept
       (+ effort initial, maintenance) et écrit « contraintes » sans l'adjectif. TOC (thèse du ch. 5) dit sept.
       Retenu ici : F-37 §7.7 (le socle prime). À arbitrer par le PRD.
     - F-37 ne rapporte pas de métrique quantitative pour l'autonomie (5e propriété) — asymétrie exposée en §5.4,
       non comblée. Élévation possible par relecture du préprint (hors périmètre : PDF non lu, consigne de tâche).
     - Aucune lacune PRD §10 ne couvre le caractère mono-source et non reproduit du cadre OO1–OO4 ;
       l'encadré §5.4 la traite au format §4.4 sans créer d'entrée. Candidate à une §10.8.
     - « Convergence à sources INDÉPENDANTES » : l'abstract de TOC.md emploie l'adjectif, PRD B.1 non
       (« convergence à trois sources »). Rinderle-Ma cosigne F-36 et F-37 : deux des trois sources
       partagent une autrice. Le ch. 5 a retiré l'adjectif et explicité la non-indépendance ; à arbitrer
       au TOC/PRD AVANT la rédaction du ch. 13, qui porte la démonstration de convergence.
     - Terminologie « cadre » vs « *frame* » : le glossaire §D.2 fixe « *frame* » (normatif/opérationnel,
       F-36) mais définit OO2 comme « agentique consciente d'un cadre » (F-37). Le ch. 5 retient donc
       « cadre » pour le frame de OO2 (forme du glossaire) et « *frame* » pour l'enseignement F-37 sur les
       contraintes temporelles (forme du PRD §7.7 et de la note [^6]). §D.2 pose que « la terminologie de
       la Partie II fait référence » et le ch. 5 l'ouvre : cette double forme se propagera si elle n'est
       pas arbitrée. Proposition : ajouter à §D.2 l'équivalence « cadre (*frame*) » avec trace F-37.
     - Glossaire §D.2 incomplet pour F-37 : trois des cinq propriétés d'évaluation (autonomie,
       spécificité de tâche, réactivité) n'y ont pas d'entrée, alors que « assurance de correction » et
       « traçabilité/tractabilité » en ont une. Le ch. 5 a posé les équivalents anglais en corps (CA-5) ;
       l'enrichissement du glossaire reste à faire (hors périmètre de cette tâche).
     - Périmètre du verdict F-37 (apport 5) : TOC.md borne le ch. 5 à quatre sections (OO1-OO4, cinq
       propriétés, critères, métriques) et PRD §6 assigne nommément le verdict « orchestration non
       encadrée inacceptable en contexte réglementé » au contenu obligatoire de la Partie III (ch. 13).
       Le ch. 5 l'expose comme donnée du socle avec renvoi explicite au ch. 13 pour la transposition.
       Risque de doublon à arbitrer : soit TOC.md ajoute une section 5.5 au ch. 5, soit le ch. 5 réduit
       le verdict à une mention et le ch. 13 le porte seul.
-->
