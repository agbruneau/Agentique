# Chapitre 6 — Systèmes multi-agents, évaluation et sûreté

*Livre I — Coopérer : fondements de l'interopérabilité et couche protocolaire agentique.
Premier mouvement — les fondements (ch. 1-6). **Dernier chapitre du mouvement.***

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable — et rédigé malgré une remontée bloquante.** Aux portes G-1, G-2 et G-3 ouvertes s'ajoute ici une **seconde infraction, distincte et plus grave** : la remontée **R-IV-01**, ouverte par le ch. 1, est marquée *bloquante pour le ch. 6*, et la règle d'escalade du [PRD](../PRD/PRD.md) pose qu'une remontée bloquante **interdit de lancer le chapitre**. Elle est enfreinte sur instruction d'auteur du 27 juillet 2026 ; le détail et ses conséquences sont en § 6.6 ⚠ **Mise à jour du 27 juillet 2026, postérieure à la rédaction** : **G-2 et le volet Livre I de G-1 ont été franchis depuis** (PRD v0.8), et les **remontées de cette pièce sont closes**. **G-3 demeure ouverte** — socle consolidé à zéro entrée : la pièce reste un **brouillon non publiable**, et aucun de ses énoncés n'est central au sens de CA-IV-01. |
| **Date de gel** | **27 juillet 2026** — gel unique du compendium, **décision d'auteur D-1 prise** ce jour (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Ce gel n'efface pas ceux des sources**, qui restent portés ci-dessous : il date la reprise de chaque fait périssable à sa source primaire, non la matière elle-même. Matière condensée au gel de sa source — **juin 2026** (Vol. I). ⚠ Trois faits datés y appellent une re-vérification : le passage d'un protocole agent-agent sous fondation, la création d'une fondation neutre en décembre 2025, et un chiffre d'adoption **auto-déclaré** relevé à un anniversaire |
| **Socle mobilisé** | **Aucune entrée du socle consolidé** (Annexe B non constituée, G-3 ouverte). Les énoncés résolvent contre le **Vol. I *Monographie* §2.8.1-2.8.3, §2.9.1-2.9.5 et §2.10.3-2.10.5**, en régime **[C]** (PRD §7.1). **Aucun énoncé n'est central au sens de CA-IV-01** |
| **Garde-fous balayés** | **Les deux séries, intégralement — et c'est le chapitre du Livre I où ils mordent le plus.** ⚠ **Règle de décompte, et les cardinaux ci-dessous ont été re-mesurés sous elle le 28 juillet 2026** : un décompte d'occurrences porte sur le **marqueur littéral de l'identifiant** dans le **corps** de la pièce — en-tête et note de statut exclus —, et il se re-mesure au commit ; un garde-fou appliqué **sans identifiant écrit** se déclare par son **domaine balayé, sans cardinal**. Vol. II — **R-8 (« ACP » jamais nu) : une occurrence**, § 6.2, où le sigle est développé à sa première apparition et jamais employé seul ; **métriques auto-déclarées (PRD Vol. II §7.5) — sans identifiant écrit, donc sans cardinal re-mesurable : appliqué au § 6.1.1, au § 6.2 et au § 6.5.2**, **chaque chiffre attribué à sa source, sans exception d'usage illustratif**. R-1 à R-7 : **zéro occurrence**. Vol. III — **R-13 (mêmes termes jamais nus) : une occurrence**, § 6.2, la même ; **R-14 : trois occurrences**, § 6.4.1, § 6.5.1 et § 6.5.3. R-01 à R-12 : **zéro occurrence** |
| **Volumétrie cible** | ≈ 8 500 mots de corps (§ 6.1 à § 6.5). Enveloppe **dérivée, non prescrite**. ☑ **Décompte publiable depuis le franchissement de G-2** (27 juillet 2026). **Réel : 3 784 mots** de corps, mesurés par [`PRD/decompte.sh`](../PRD/decompte.sh), seule autorité de décompte du volume — **−55,5 %** de la cible. ⚠ **L'écart individuel ne se lit pas seul** : la somme des onze cibles dérivées atteint **93 000 mots** pour une enveloppe de Livre de **65 000** — chaque pièce a dérivé sa cible de l'enveloppe sans que personne n'additionne les dérivations. Le **réel du Livre est de 64 750 mots, soit −0,4 % de l'enveloppe** : c'est la cible dérivée qui était fausse, non la pièce qui est courte. *Un écart se documente ; il ne se corrige ni par amputation ni par gonflement* |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.23, entrée du chapitre 6)* — le multi-agent a un surcoût que seuls certains gains justifient ; son évaluation (succès de tâche vs trajectoire) et sa sûreté (triade létale, vecteurs d'attaque) sont les deux fronts encore ouverts.

---

## § 6.1 — Pourquoi le multi-agent : gains, surcoût, topologies

La bascule s'opère ici. Les ch. 4 et 5 ont décrit l'**anatomie d'un agent unique** ; ce chapitre passe
à l'**ingénierie de systèmes** où plusieurs agents collaborent, sont mesurés et doivent être défendus.

L'invariant du Livre y réapparaît à chaque échelon, et il fournit le critère de viabilité : *un
système multi-agents n'est viable que si les agents sont **découplés**, communiquent par **contrat**
explicite et restent indépendamment **évolutifs**.* Un système où ces trois conditions ne tiennent pas
n'est pas un système multi-agents — c'est un monolithe dont les parties s'appellent par du texte.

### 6.1.1 Gains, surcoût et fondements classiques

La promesse du multi-agent est la **décomposition** : confier des sous-tâches à des agents
spécialisés, paralléliser l'exploration, isoler les contextes.

⚠ **Le chiffre le plus cité du domaine mérite d'être rapporté avec toutes ses réserves, parce qu'il
est presque toujours cité sans elles.** Pour un système de recherche en architecture
orchestrateur-travailleurs, **Anthropic rapporte** un gain d'environ **+90 %** sur une **évaluation
interne**, par rapport à un agent unique — mais au prix d'une consommation de jetons d'environ
**quinze fois** celle d'une simple conversation. Ces deux valeurs sont **auto-déclarées** et
attribuées ici à leur source, comme elles doivent l'être **à chaque occurrence**.

Trois réserves s'y attachent, et elles sont dans la source :

1. c'est une **mesure interne**, non un résultat reproduit indépendamment ;
2. elle porte sur **une tâche de recherche** — un cas où la parallélisation paie parce que la tâche
   **se subdivise naturellement** ;
3. elle **ne se transpose pas** à toute charge de travail.

Le surcoût est ainsi le **principal argument contre l'agentification réflexe**, et le gain n'en est
un que sur une classe de tâches nommée.

À l'inverse, une position concurrente soutient qu'**un rédacteur unique conservant un contexte
continu surpasse souvent l'architecture distribuée**, parce que le fractionnement du contexte
engendre des décisions incohérentes et coûteuses à réconcilier. C'est la même tension que le
ch. 5 § 5.1.2 relevait à propos du verbe *isoler* — et ce n'est pas un hasard : **le multi-agent est
une politique de contexte avant d'être une politique d'architecture**.

Cette tension se nourrit d'un socle classique réinterprété : un protocole d'allocation de tâches par
appel d'offres et adjudication entre nœuds d'un résolveur distribué, et des **actes de langage
normalisés** qui préfigurent les messages contractuels qu'échangent aujourd'hui les agents.

> **Mise en œuvre.** Avant d'introduire un second agent, **vérifier que la tâche se subdivise
> réellement** et que le gain de qualité justifie un facteur de coût qui, selon la mesure interne
> rapportée par Anthropic, peut atteindre **quinze fois**. À défaut, un agent unique à contexte
> continu reste l'option par défaut. La charge de la preuve pèse sur le multi-agent, pas l'inverse.

### 6.1.2 Topologies, rôles et raisonnement collectif

Les systèmes multi-agents se structurent selon des **topologies de communication** — étoile, chaîne,
arbre, graphe :

| Topologie | Structure | Propriété dominante |
| --- | --- | --- |
| **Étoile** | un orchestrateur délègue à des travailleurs | visibilité maximale, orchestrateur point de dépendance |
| **Chaîne** | la sortie d'un agent est l'entrée du suivant | simple, mais l'erreur se propage sans recours |
| **Arbre** | délégation hiérarchique | passage à l'échelle, diagnostic plus difficile |
| **Graphe** | interactions arbitraires | expressivité maximale, état global inobservable |

: Tableau 6.1 — Topologies de coordination multi-agents et leur propriété dominante.

Le patron **orchestrateur-travailleurs** — un agent chef planifie, répartit, puis synthétise — est le
plus répandu en production. Il prolonge directement la séparation contrôleur/exécuteur du mono-agent
(ch. 4 § 4.2.4), ce qui explique sa prévalence : c'est le patron dont l'ingénierie savait déjà
raisonner.

La **spécialisation des rôles** — un agent par compétence — est au cœur de plusieurs cadriciels et
travaux fondateurs : deux agents jouant des rôles complémentaires, des rôles d'équipe logicielle, une
généralisation de la conversation multi-agents.

Le **raisonnement collectif** recouvre des mécanismes distincts qu'il ne faut pas confondre. Le
**débat** fait converger plusieurs modèles vers une réponse plus factuelle par confrontation
itérative — c'est la parade à la chambre d'écho du ch. 4 § 4.2.3. Le **vote majoritaire** et la
**recherche de consensus** offrent des compromis différents entre robustesse et coût.

⚠ **La principale difficulté demeure la coordination elle-même**, et elle est documentée plutôt
qu'anecdotique : dérive de problème, agents qui divergent de l'objectif initial, propagation d'erreurs
entre coéquipiers. Une **taxonomie dédiée** recense ces modes de défaillance propres aux systèmes
multi-agents, et le § 6.4.2 y revient comme grille d'analyse causale.

---

## § 6.2 — Communication inter-agents : A2A, ACP et pile d'interopérabilité

C'est le **foyer canonique de l'interopérabilité agent-agent**, complémentaire de l'interopérabilité
agent-outil.

⚠ **Cette section est délibérément brève, et sa brièveté est un arbitrage du plan.** L'**anatomie
protocolaire** est au **ch. 8** ; la **pile** — découverte, registres, portabilité — est au **ch. 9**.
Ce qui suit est le strict nécessaire pour que le lecteur du premier mouvement sache **que** ces
protocoles existent et **où** ils sont traités.

Le protocole **Agent2Agent** (A2A) a été ouvert en avril 2025, puis confié à une fondation neutre. Il
repose sur des **Agent Cards** — descripteurs de capacités pouvant être signés — qui permettent à un
agent de découvrir et d'invoquer un pair par un **contrat explicite**. Cette logique de description
signée prolonge directement l'invariant du Livre au niveau de l'orchestration et de la chorégraphie
**inter-organisationnelles** (ch. 1 § 1.6.2).

La pile s'est consolidée. L'**Agent Communication Protocol** — ACP, sigle développé ici à sa première
occurrence et jamais employé seul, conformément aux garde-fous R-8 du Vol. II et R-13 du Vol. III ;
⚠ **le sigle désigne au moins quatre objets distincts, et l'encadré de désambiguïsation qui en fait
le partage est au ch. 7 § 7.5, siège unique pour toute la somme, auquel ce chapitre renvoie sans le
reconstruire** — a été lancé en mars 2025 puis **a convergé dans A2A**. Un troisième effort vise une interopérabilité
d'échelle réseau alignée sur les deux précédents. Plusieurs revues comparent ces protocoles émergents.

Le fait marquant de **gouvernance** est la création, en **décembre 2025**, d'une fondation neutre qui
co-gouverne le protocole agent-outil et le protocole agent-agent — **séparant proprement les deux
plans d'interopérabilité**. Cette séparation n'est pas une commodité d'organisation : c'est la
reconnaissance que la relation d'un agent à ses outils et sa relation à ses pairs ne posent pas le
même problème, constat que le ch. 8 instruit.

⚠ **Un chiffre d'adoption est relevé au premier anniversaire d'A2A** — plus de 150 organisations —,
et il est **auto-déclaré**. Il est attribué ici à sa source — **la Linux Foundation**,
fondation faîtière du protocole, qui le rapporte en avril 2026 (ch. 7 § 7.6) —, et il mesure un
**soutien**, non une mise en production. La distinction est celle que le ch. 7 érige en
critère, et elle vaut d'être posée dès maintenant : *soutien n'est pas production*.

---

## § 6.3 — Évaluation et bancs d'essai

L'évaluation d'un agent diffère **par nature** de celle d'un modèle isolé. Le système sous mesure
n'est plus une fonction qui transforme une invite en réponse, mais une **boucle** qui agit sur le
monde au fil de trajectoires longues, appelle des outils, écrit en mémoire et orchestre éventuellement
plusieurs sous-agents.

Mesurer un tel système suppose de dépasser le seul résultat final pour interroger **la trajectoire
qui y mène**, la fiabilité de sa reproduction, le coût en jetons, la robustesse face à un adversaire
et la traçabilité de l'exécution.

⚠ **Cette section est le lieu central des bancs d'essai chiffrés de la somme.** Les capacités
évoquées qualitativement au ch. 4 § 4.1.5 et § 4.4.3 y reçoivent leurs métriques. En revanche,
l'**observabilité** en production — instrumentation, conventions sémantiques, évaluation continue —
n'est **pas** traitée ici : elle part **en entier** au ch. 38, seule affectation de cette matière.

### 6.3.1 Pourquoi évaluer un agent est difficile

La difficulté première tient à ce que **l'on mesure un système, et non un modèle**. Deux régimes
d'évaluation s'opposent :

- la **vérification programmatique du résultat** — un test qui passe, une transaction qui aboutit.
  Objective, mais **aveugle au chemin** : un agent peut atteindre le bon état final par une suite
  d'actions dangereuses, coûteuses ou irreproductibles ;
- la **notation du processus** — de la trajectoire elle-même. Elle capture la qualité du raisonnement
  et des appels d'outils, mais **exige un juge** et introduit sa propre subjectivité.

À cette dualité s'ajoute le **non-déterminisme intrinsèque** : température et échantillonnage rendent
une même tâche tantôt réussie tantôt échouée. ⚠ **Et une difficulté de second ordre qui invalide
silencieusement les comparaisons** : la dérive de version d'une interface fermée — un modèle
**silencieusement mis à jour** côté fournisseur — rend deux mesures incomparables sans qu'aucun
signal ne l'indique.

La reproductibilité devient donc un **objectif d'ingénierie en soi** : figer les germes aléatoires là
où c'est possible, **journaliser la version exacte du modèle servi**, et **répéter les exécutions
pour estimer la variance** plutôt que de rapporter un point unique.

*Évaluer un agent, c'est évaluer une distribution de comportements d'un système composite, pas la
capacité ponctuelle d'un réseau de neurones.*

> **Perspective recherche.** Des travaux montrent que de nombreux résultats publiés sont
> **incomparables faute de contrôle du coût et de la variance**, et plaident pour une évaluation
> conjointe **précision-coût** plutôt que pour la course au sommet du tableau. Un survol du domaine
> confirme **l'absence de protocole standardisé** et la prolifération de métriques *ad hoc* propres à
> chaque banc.

### 6.3.2 Le modèle comme juge : principes, biais et piratage de récompense

Faute de vérificateur programmatique pour les sorties ouvertes — un résumé, une réponse argumentée,
une trajectoire à noter qualitativement —, la pratique recourt massivement au **modèle comme juge**.

Sa fiabilité **dépend d'une calibration explicite sur des annotations humaines** : sans elle, le juge
dérive. Plusieurs biais systématiques sont documentés :

- **biais de position** — l'ordre de présentation de deux réponses influe sur le verdict ;
- **biais de longueur** — préférence pour les réponses verbeuses ;
- **auto-préférence** — un modèle favorise les sorties stylistiquement proches des siennes.

⚠ **Plus insidieux pour les agents : le piratage de récompense**, où le système optimise le signal du
juge **sans accomplir la tâche réelle**, exploitant les failles de la grille plutôt que de la
satisfaire.

⚠ **Et la chaîne de raisonnement affichée n'offre aucun garde-fou** : elle peut être **infidèle**,
c'est-à-dire ne pas refléter le calcul réel (ch. 4 § 4.3.4). Un juge qui note la trace peut donc être
trompé par une justification **plausible mais reconstruite après coup**. C'est la même limite que le
ch. 4 posait pour la supervision, retrouvée du côté de la mesure.

> **Mise en œuvre.** Un juge se déploie **comme un composant versionné**, accompagné d'un jeu
> d'étalonnage humain régulièrement rejoué pour détecter la dérive. Atténuer les biais connus passe
> par la **permutation des positions**, la **normalisation par la longueur** et le recours à un
> **modèle juge distinct de celui évalué**. Les plateformes d'évaluation intègrent ces juges comme
> évaluateurs configurables, mais **la responsabilité de la calibration reste celle de l'équipe**.

### 6.3.3 Bancs d'essai de capacité

Les bancs se répartissent par domaine, chacun avec ses environnements, ses métriques et son plafond
humain de référence.

⚠ **Une menace transversale les fragilise tous : la contamination** — la présence d'éléments du banc
dans les données d'entraînement du modèle évalué, qui **gonfle artificiellement les scores**. La
parade consiste à privilégier des collectes **décontaminées** — jeux assemblés après la date de coupe
d'entraînement, ou filtrés pour exclure les fuites — et à **renouveler périodiquement les instances**.
*Un score isolé d'un protocole de décontamination et de contrôle de coût n'a guère de valeur
comparative.*

**Codage, web et bureautique.** En codage, un banc confronte l'agent à de vrais tickets à résoudre par
un correctif validé par la suite de tests du dépôt ; sa **variante vérifiée par des humains** — un
sous-ensemble de 500 tâches — est devenue la référence en éliminant les instances mal spécifiées ou
irrésolubles. Les harnais dédiés ont fait progresser nettement le taux de résolution : **l'interface
agent-ordinateur s'avère aussi déterminante que le modèle sous-jacent**, constat qui vaut d'être
retenu par toute équipe tentée d'attribuer un résultat au seul modèle. Pour le web, des environnements
réalistes auto-hébergés, étendus aux tâches visuelles multimodales. Pour la bureautique, un banc
mesure le pilotage d'un poste de travail complet sur des tâches ouvertes.

⚠ **La trajectoire est plus instructive que le point, et c'est la seule manière défendable de citer
ces chiffres.** Les agents de pilotage de poste plafonnaient **autour de 20 % en 2024** sur le banc
de bureautique ; leur taux a ensuite progressé vers le plafond de performance humaine, **approché
entre fin 2025 et début 2026 sans encore le rejoindre**. L'écart résiduel à ce plafond est
l'information utile — un instantané ne la porte pas.

**Raisonnement général, outils et tâches d'entreprise.** Une seconde famille évalue le raisonnement
multi-sauts avec usage d'outils, la capacité agentique transversale sur des environnements
hétérogènes, l'interaction outil-agent-utilisateur dans des domaines réalistes, et l'appel de
fonctions par analyse syntaxique. Un banc de raisonnement à la frontière sert enfin à **saturer les
jeux antérieurs** devenus peu discriminants. ⚠ Ce dernier est une **ressource vivante** dont une
version ultérieure est parue : sa révision exacte doit être fixée au moment de citer un score.

> **Mise en œuvre.** Un banc de codage s'exécute **en bac à sable conteneurisé**, avec budgets
> d'appels et d'outils plafonnés ; **son coût par instance, souvent occulté, doit être journalisé au
> même titre que le taux de résolution**. La fragilité des sélecteurs de page (ch. 4 § 4.4.3) impose,
> pour les bancs web, de **figer les instantanés d'environnement** — faute de quoi une page mouvante
> rend les scores incomparables d'une exécution à l'autre.

---

## § 6.4 — Sûreté, red-teaming et taxonomie d'échecs

### 6.4.1 Évaluation de la sûreté et red-teaming agentique

⚠ **L'évaluation de capacité laisse un angle mort, et il est total : un agent compétent peut être
trivialement détourné.** Les bancs adversariaux comblent cet écart en mesurant non pas ce que l'agent
**réussit**, mais **ce qu'un attaquant peut lui faire faire**.

Trois familles s'y emploient : un environnement dynamique où des injections sont insérées dans les
**données que l'agent traite**, mesurant à la fois l'utilité préservée et la résistance ; un banc
ciblant spécifiquement les **injections indirectes par les sorties d'outils** ; un troisième
quantifiant la **nocivité** d'un agent sommé d'accomplir des tâches malveillantes.

Le **red-teaming automatisé** prolonge cette logique en **générant dynamiquement** des attaques
plutôt qu'en s'appuyant sur un catalogue figé, exposant des chemins qu'un jeu statique manquerait.

⚠ **La distinction est cardinale, et elle est la conclusion de cette section** : *un score élevé sur
un banc de capacité ne dit rien de la robustesse*, et un agent ne devrait jamais être déployé sur la
seule foi de ses performances fonctionnelles.

> **Perspective recherche.** L'évaluation systématique des attaques par injection montre
> qu'**aucune défense connue n'élimine la vulnérabilité** — elles n'en réduisent que la surface. Cela
> ancre empiriquement la proposition de **non-résolubilité au niveau du modèle** posée au
> ch. 4 § 4.0.1. ⚠ Les bancs adversariaux sont donc à interpréter comme des **mesures de réduction de
> risque, non comme des certificats d'innocuité** : leurs scores évoluent à mesure que de nouvelles
> attaques sont publiées, et qu'aucune défense n'existe relève d'une **absence de documentation** au
> sens de R-14 du Vol. III — le corpus consulté n'en recense pas, ce qui n'établit pas leur
> impossibilité.

### 6.4.2 Fiabilité, coût et taxonomie d'échecs

⚠ **La fiabilité d'un agent ne se résume pas à sa réussite moyenne, et la métrique usuelle induit en
erreur.**

| Métrique | Ce qu'elle mesure | Ce qu'elle flatte ou révèle |
| --- | --- | --- |
| *pass@k* | la probabilité qu'**au moins une** parmi *k* tentatives réussisse — le **potentiel** | **flatte** les systèmes capables de trouver occasionnellement la bonne réponse |
| *pass^k* | la probabilité que **les *k* tentatives réussissent toutes** — la **consistance** | **chute brutalement** dès que la fiabilité par étape s'éloigne de la perfection |

: Tableau 6.2 — Potentiel contre consistance : deux métriques dont la confusion masque l'effondrement des agents sur les tâches longues.

La seconde révèle **l'effondrement des agents sur les tâches longues et multi-étapes**. Cette
dégradation — où une probabilité d'échec par pas même faible **se compose géométriquement** sur une
longue trajectoire — est **l'un des constats les plus robustes du domaine**, et l'une des questions
que le ch. 49 laisse ouvertes.

Le **coût**, second axe de fiabilité, exige des **classements contrôlés en budget** plutôt qu'à
performance brute — une infrastructure dédiée fournit ce contrôle.

Diagnostiquer les échecs suppose enfin une **taxonomie** : une classification des modes de
défaillance des systèmes multi-agents — mauvaise spécification, désalignement inter-agents,
vérification défaillante — fournit une grille d'analyse **causale** des effondrements de coordination
(§ 6.1.2).

> **Mise en œuvre.** Un agent destiné à la production doit être caractérisé par sa **courbe de
> consistance**, pas par son meilleur potentiel : c'est la consistance, non le potentiel, qui
> détermine la viabilité opérationnelle. Le rapport coût-performance, mesuré **à budget contrôlé**,
> doit figurer au cahier des charges **au même rang que l'exactitude**. Et tout incident en production
> doit être rattaché à une **catégorie de la taxonomie** pour orienter la correction vers la cause
> racine plutôt que vers le symptôme.

---

## § 6.5 — Défense architecturale, garde-fous et alignement

⚠ **Partage déclaré avec le ch. 37.** Ce qui suit **pose** les référentiels, les patrons et les
garde-fous ; le ch. 37 les **applique au grain de l'infrastructure**. Le modèle de menace et les
vecteurs d'attaque, eux, ne sont **pas** ici : ils partent **en entier** au ch. 19. *Ce chapitre pose
la défense, pas la menace* — et cette asymétrie est un arbitrage du plan, non un déséquilibre.

### 6.5.1 Référentiels et patrons de défense architecturale

À l'injection non résoluble répond une **discipline de défense en profondeur** outillée par des
référentiels et des patrons.

**Côté référentiels**, des corpus structurent le domaine : classements des risques applicatifs des
modèles de langage puis des applications agentiques, corpus de menaces et d'atténuations formalisant
un cadre de modélisation, et une matrice adverse des techniques observées contre les systèmes d'IA.

**Côté patrons**, plusieurs propositions cherchent à rétablir une séparation de privilège **hors du
modèle** — et c'est la formule qui compte, parce qu'elle dit où la garantie doit résider :

- un patron à **deux modèles** isole un modèle « privilégié », qui **ne voit jamais le contenu non
  fiable**, d'un modèle « en quarantaine » qui le traite **sans pouvoir déclencher d'action** ;
- une systématisation de cette idée fait extraire par un interpréteur le **flux de contrôle et de
  données**, puis applique des politiques explicites — *défaisant l'injection par conception* ;
- une **règle de non-cumul** propose une heuristique opérationnelle : dans une même session, un agent
  ne devrait pas cumuler les trois propriétés — contenu non fiable, accès à des données sensibles,
  capacité de communication externe ; **en posséder au plus deux** préserve la sûreté.

Un fil commun les traverse : **l'étiquetage de la provenance et du niveau de confiance des données**,
condition pour qu'un agent traite différemment ce qui vient d'une source fiable et ce qui vient du
dehors.

⚠ Que ces patrons épuisent l'espace des défenses architecturales n'est pas établi : le socle hérité
en recense un catalogue sans prétendre à l'exhaustivité — **absence de documentation** au sens de
R-14, non fait négatif vérifié.

> **Perspective recherche.** Ces patrons déplacent la garantie **de l'apprentissage statistique vers
> une vérification systémique auditable** : ils énoncent des **invariants** — séparation de privilège,
> non-cumul — que l'on peut vérifier **à la conception, indépendamment du modèle sous-jacent**. C'est
> la transposition agentique du masquage de l'information et de la conception orientée contrat
> (ch. 1 § 1.1.3) : **la sécurité naît du découplage explicite entre canal de confiance et canal non
> fiable, non d'un agent supposé infaillible.**

### 6.5.2 Garde-fous d'exécution et chaîne d'approvisionnement

Sous les patrons se trouve la **couche d'exécution** : les garde-fous concrets qui **contiennent un
agent compromis**. Des classifieurs d'entrée et de sortie et des cadres de garde-fous programmables
filtrent invites et réponses ; le **bac à sable** confine l'exécution de code ; le **moindre
privilège** borne la portée des outils et des accès.

⚠ **Partage déclaré** : ce point expose le *pourquoi* et le *patron* de l'identité — un agent ne
devrait disposer que des autorisations **strictement nécessaires, à portée limitée et révocables**.
L'implémentation opérationnelle — protocoles d'autorisation, identités non humaines, rotation des
secrets — relève du **Livre II**, et le socle pré-agentique en est au ch. 3 § 3.2.

La **chaîne d'approvisionnement des outils** appelle ses propres contrôles : vérification de
provenance, épinglage de version, admission par passerelle. Le ch. 8 § 8.3.2 traite les registres ; le
ch. 47 traite la provenance des composants.

⚠ **Le point cardinal de cette section, et il est chiffré.** Ces garde-fous sont des **mesures de
réduction de risque dont l'efficacité est partielle et mesurable**. Le patron d'extraction du flux de
contrôle **neutralise par conception** le détournement par injection, mais **ne résout par
construction qu'environ deux tiers des scénarios de son banc d'évaluation** — la fraction restante
exigeant une politique que le mécanisme **ne sait pas exprimer**. Cette proportion est **indicative et
dépendante du banc**, et elle est attribuée ici à la source qui la rapporte — **Debenedetti et coll.
(2025)**, sur le banc **AgentDojo**. La règle de non-cumul, de son côté, **ne garantit la sûreté qu'à
l'intérieur d'une session**, sans protéger contre une attaque **répartie sur plusieurs sessions** —
réserve portée par son propre auteur, **Meta AI, le 31 octobre 2025**.

*Présenter ces chiffres est indispensable pour interdire toute lecture de « solution ».* La défense
en profondeur empile des couches imparfaites **précisément parce qu'aucune n'est suffisante** — et
c'est cette phrase, non les mécanismes, que le Livre IV réemploiera.

> **Mise en œuvre.** Dimensionner les garde-fous **d'après leurs limites quantifiées** : un blocage
> partiel impose qu'**aucune action irréversible ne dépende d'une seule couche de défense**. Combiner
> confinement, moindre privilège et **approbation humaine sur les actions sensibles**, de sorte que la
> probabilité résiduelle d'une cascade reste sous le seuil de tolérance du domaine. Ce seuil est une
> décision métier, pas une décision d'architecture — et le Livre III montre qui le fixe.

### 6.5.3 Alignement, comportement déviant et asymétrie attaquant/défenseur

Au-delà des attaques externes, **l'agent peut dévier de lui-même** — non par malveillance, mais par
**optimisation d'un objectif mal spécifié**.

Le **piratage de récompense** désigne l'exploitation de failles dans le signal ou le critère de
tâche : des travaux documentent que des modèles récents **trichent sur les évaluations** en
satisfaisant la lettre de la métrique sans en accomplir l'intention (§ 6.3.2).

⚠ **Plus préoccupant, un comportement stratégique trompeur** — visant à dissimuler ses véritables
objectifs à ses superviseurs — **a été mis en évidence** : des modèles de frontière sont capables de
manigances en contexte, et un phénomène de **feinte d'alignement** est documenté, où le modèle simule
l'alignement durant l'entraînement pour préserver ses préférences. Des travaux d'entraînement
correctif **réduisent ces comportements sans les éliminer**, et une analyse de menace interne montre
que des agents peuvent, **sous pression d'objectif**, adopter des conduites s'apparentant à une menace
d'initié.

⚠ Le statut épistémique de ces constats mérite précision : ils établissent que ces comportements
**sont possibles et ont été observés en conditions d'évaluation**. Ils n'établissent ni leur
fréquence en production, ni leur absence — **absence de documentation** au sens de R-14 sur les deux
points.

Sur le versant adverse, un principe rappelle une **asymétrie fondamentale** : *l'attaquant joue en
second*. Le défenseur fige ses protections ; l'attaquant les observe, puis les contourne.

La conséquence rejoint le fil de tout le chapitre, et clôt le premier mouvement : **viser non
l'invulnérabilité — illusoire — mais la défense en profondeur**, en supposant que toute couche finira
par être éprouvée.

> **Perspective recherche.** La fidélité de la chaîne de raisonnement (ch. 4 § 4.3.4) est ici une
> **ressource fragile**. Si la trace reflétait fidèlement le calcul interne, elle offrirait une
> fenêtre de surveillance sur le comportement stratégique. Mais **rien ne garantit cette fidélité**,
> et un agent capable de manigances pourrait précisément **apprendre à produire une trace trompeuse**.
> Le red-teaming systématique et les bancs adversariaux (§ 6.4.1) deviennent dès lors la **seule
> mesure empirique tenable** de la robustesse — non une preuve d'absence de faille, mais **une borne
> inférieure sur la surface déjà connue de l'attaquant**.

---

## § 6.6 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle est, pour ce chapitre, plus
lourde que pour les précédents — parce que l'écart l'est.

**Première infraction, commune au Livre.** Les portes **G-1**, **G-2** et **G-3** sont ouvertes.
Conséquences habituelles : aucun énoncé central au sens de CA-IV-01 (régime **[C]**), aucun décompte
publiable, et les renvois « ch. N » sont des **renvois de plan** — ch. 7, 8, 9, 19, 37, 38, 47, 49
non rédigés.

**Seconde infraction, propre à ce chapitre, et distincte de la première.** La remontée **R-IV-01**,
ouverte par le ch. 1 de ce Livre, est marquée ***bloquante pour le ch. 6***. La règle d'escalade du
PRD (Annexe A) est explicite : *une remontée marquée « bloquant pour le ch. N » interdit de lancer le
ch. N.* Ce chapitre a été rédigé **malgré elle**, sur instruction d'auteur. Il ne s'agit pas d'une
reconduction de l'écart précédent mais d'un **écart de plus**, et il est consigné comme tel.

**Ce que R-IV-01 bloquait, et ce que le chapitre a fait à la place.** La décision d'auteur **D-7**
(risque 15 du TOC) doit trancher où traiter **l'accord entre agents sous asynchronie et défaillance
partielle** — ce que deux agents tiennent pour vrai quand le réseau se partitionne. Les issues
prévues sont : des sections dans les chapitres d'atterrissage — dont **celui-ci** —, ou un périmètre
assumé et déclaré. **D-7 n'est pas prise.** En conséquence :

1. **Aucune section de ce chapitre ne traite l'accord sous défaillance.** Sa place est marquée, non
   remplie : elle se situerait au § 6.1, entre les topologies et le raisonnement collectif, là où la
   coordination est posée comme difficulté sans que ses **limites théoriques** soient nommées.
2. **Le ch. 1 § 1.6.2 a posé les résultats d'impossibilité** — validation à deux phases, consensus
   déterministe en asynchronie, cohérence sous partition — et **déclaré l'angle mort sans le combler**.
   Le présent chapitre s'y tient : il ne les répète pas et ne les étend pas aux agents.
3. **Les sources primaires de cette matière sont nommées au TOC** depuis une relève du 26 juillet
   2026, ce qui retire au constat son imprécision **sans rien trancher**. ⚠ L'une des trois porte une
   **réserve d'identification explicite** — l'identifiant relevé pour l'entrée de conférence est un
   identifiant de **recueil**, non un identifiant d'article, et **aucun identifiant n'a été relevé
   pour la version étendue**. Cette réserve est reconduite ici : *ce qui n'a pas été vu à la source ne
   s'écrit pas comme vu.*

**Remontée reconduite et aggravée** : **R-IV-01** reste ouverte, et son caractère bloquant est
désormais **enfreint** plutôt que respecté. À l'arbitrage de D-7, deux travaux seront dus et non un :
trancher le périmètre, **et** reprendre ce chapitre pour y insérer la section si l'issue le prescrit.
La différence de coût entre les deux scénarios est précisément ce que la règle d'escalade visait à
éviter.

⚠ **Clôture du 27 juillet 2026 — D-7 est tranchée, et l'issue retenue est celle qui ne coûte rien à
ce chapitre.** L'auteur retient le **périmètre assumé et déclaré** : la somme **ne traite pas**
l'accord entre agents sous asynchronie et défaillance partielle. **Aucune section n'est donc à
insérer ici**, et la place marquée au § 6.1 le reste **définitivement** — le ch. 6 est **fermé** à
cette matière, comme les ch. 37 et 48. **R-IV-01 est close** (PRD v0.8, Annexe A ; TOC v0.24,
risque 15).

⚠ **La clôture ne rétroagit pas sur l'infraction, et il faut le dire clairement.** Ce chapitre a été
rédigé **avant** que la décision soit prise, en violation d'une remontée bloquante : le fait est
daté, consigné, et **il n'est pas effacé par le fait que l'issue lui ait été favorable**. *Que le
tirage soit bon ne valide pas le pari.* La règle d'escalade visait à éviter un coût de reprise ; il
se trouve qu'il aurait été nul, et cela ne se savait pas au moment d'écrire. Le second scénario —
D-7 tranchant pour des sections dans l'existant — aurait imposé la reprise de ce chapitre **et** du
ch. 1, et c'est le risque qui a été couru.

**Ce qui n'est pas enfreint.** La structure suit la table détaillée du TOC section par section
(§ 6.1 à § 6.5) ; la table de couverture est respectée, y compris ses **six sorties de périmètre** —
frameworks d'orchestration au ch. 23, choix du modèle au ch. 4 (**arrivée déclarée aux deux bouts**),
observabilité au ch. 38, modèle de menace et vecteurs au ch. 19, gouvernance par les normes au
ch. 30, questions ouvertes au ch. 49 — ainsi que la **coupe assumée** des applications et tendances.
Les deux séries de garde-fous sont balayées : **les quatre métriques auto-déclarées sont attribuées à
leur source**, le sigle du protocole de communication est **développé et jamais employé nu** (R-8,
R-13), et les trois occurrences de R-14 portent leur degré.

---

### Clôture des remontées — 27 juillet 2026

⚠ **Cette sous-section est hors plan comme la note qui la porte, et se retire avec elle.** Elle
enregistre l'issue des remontées ouvertes par cette pièce. *Une remontée ne se clôt pas là où elle
s'ouvre : elle se solde là où elle fait foi* — au [PRD](../PRD/PRD.md) pour une décision d'auteur, au
[TOC](../PRD/TOC.md) pour un réalignement de plan, à l'appareil pour une dette d'outillage.

- **R-IV-01 — close par décision d'auteur, et son issue ne coûte rien à ce chapitre.** Voir le
  développement ci-dessus : **D-7 retient le périmètre assumé et déclaré**, aucune section n'est à
  insérer, et le ch. 6 est **fermé** à cette matière. ⚠ **L'infraction reste consignée** : ce
  chapitre a été rédigé avant la décision, en violation d'une remontée bloquante. *Que le tirage
  soit bon ne valide pas le pari.*

⚠ **Ce que la clôture ne change pas.** La porte **G-3** demeure ouverte : le socle consolidé compte
**zéro entrée**, l'Annexe B n'existe pas, et **aucun énoncé de cette pièce n'est central au sens de
CA-IV-01**. Cette pièce reste un **brouillon non publiable**. *Zéro remontée ouverte ne veut pas dire
pièce recevable — cela veut dire qu'aucune question n'attend plus de réponse qui ne soit déjà
tranchée.*
