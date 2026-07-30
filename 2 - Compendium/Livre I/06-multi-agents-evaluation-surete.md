# Chapitre 6 — Systèmes multi-agents, évaluation et sûreté

*Livre I — Coopérer : fondements de l'interopérabilité et couche protocolaire agentique.
Premier mouvement — les fondements (ch. 1-6). **Dernier chapitre du mouvement.***

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable — et rédigé malgré une remontée bloquante.** Aux portes G-1, G-2 et G-3 **alors ouvertes** s'ajoute ici une **seconde infraction, distincte et plus grave** : la remontée **R-IV-01**, ouverte par le ch. 1, est marquée *bloquante pour le ch. 6*, et la règle d'escalade du [PRD](../PRD/PRD.md) pose qu'une remontée bloquante **interdit de lancer le chapitre**. Elle est enfreinte sur instruction d'auteur du 27 juillet 2026 ; le détail et ses conséquences sont en § 6.6 ⚠ **Deux mises à jour postérieures à la rédaction.** **27 juillet 2026** : **G-2 et le volet Livre I de G-1 franchis** (PRD v0.8), **remontées de cette pièce closes**. **28 juillet 2026** : **G-3 est franchie à son tour** (PRD v0.14, TOC v0.30) et le **socle consolidé existe** — [`socle-consolide.md`](../PRD/socle-consolide.md) v1.2, **159 entrées `S-001`…`S-159`**. ⚠ **La pièce demeure un brouillon non publiable, et le motif change plutôt qu'il ne disparaît** : elle a été rédigée **avant** le franchissement et **n'a pas été ré-adossée au socle entrée par entrée** ; ses énoncés restent en régime **[C]**, de sorte qu'**aucun n'est central au sens de CA-IV-01** ; et **CA-IV-13 demeure due**, D-6 ne fournissant pas de relecteur distinct du rédacteur. |
| **Date de gel** | **27 juillet 2026** — gel unique du compendium, **décision d'auteur D-1 prise** ce jour (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Ce gel n'efface pas ceux des sources**, qui restent portés ci-dessous : il date la reprise de chaque fait périssable à sa source primaire, non la matière elle-même. Matière condensée au gel de sa source — **juin 2026** (Vol. I). ⚠ Trois faits datés y appellent une re-vérification : le passage d'A2A sous la Linux Foundation, la création de l'Agentic AI Foundation en décembre 2025, et un chiffre d'adoption **auto-déclaré** relevé au premier anniversaire d'A2A |
| **Socle mobilisé** | ⚠ **Le socle consolidé existe depuis le 28 juillet 2026** — Annexe B, [`socle-consolide.md`](../PRD/socle-consolide.md) v1.2, `S-001`…`S-159` —, **mais cette pièce, rédigée avant lui, n'y est pas adossée entrée par entrée** : elle continue de citer ses identifiants sources, comme le PRD §7.1 le constate pour les cinquante pièces. Ses énoncés résolvent contre le **Vol. I *Monographie* §2.8.1-2.8.3, §2.9.1-2.9.5 et §2.10.3-2.10.5**, en régime **[C]** (PRD §7.1) — régime que le socle **confirme** plutôt qu'il ne le relève : ses **dix-sept entrées héritées du Vol. I sont toutes en [C]**. **Aucun énoncé n'est central au sens de CA-IV-01** |
| **Garde-fous balayés** | **Les deux séries, intégralement — et c'est le chapitre du Livre I où ils mordent le plus.** ⚠ **Règle de décompte, et les cardinaux ci-dessous ont été re-mesurés sous elle le 28 juillet 2026** : un décompte d'occurrences porte sur le **marqueur littéral de l'identifiant** dans le **corps** de la pièce — en-tête et note de statut exclus —, et il se re-mesure au commit ; un garde-fou appliqué **sans identifiant écrit** se déclare par son **domaine balayé, sans cardinal**. Vol. II — **R-8 (« ACP » jamais nu) : une occurrence**, § 6.2, où le sigle est développé à sa première apparition et jamais employé seul ; **métriques auto-déclarées (PRD Vol. II §7.5) — sans identifiant écrit, donc sans cardinal re-mesurable : appliqué au § 6.1.1, au § 6.2 et au § 6.5.2**, **chaque chiffre attribué à sa source, sans exception d'usage illustratif**. R-1 à R-7 : **zéro occurrence**. Vol. III — **R-13 (mêmes termes jamais nus) : une occurrence**, § 6.2, la même ; **R-14 : trois occurrences**, § 6.4.1, § 6.5.1 et § 6.5.3. R-01 à R-12 : **zéro occurrence** |
| **Volumétrie cible** | ≈ 8 500 mots de corps (§ 6.1 à § 6.5). Enveloppe **dérivée, non prescrite**. ☑ **Décompte publiable depuis le franchissement de G-2** (27 juillet 2026). **Réel : 4 579 mots** de corps, ⚠ **re-mesurés au commit du 30 juillet 2026** (décision 16b — *le chiffre antérieur datait de la contre-passe du 28 juillet, et la passe de révision l'a périmé*) par [`PRD/decompte.sh`](../PRD/decompte.sh), seule autorité de décompte du volume — **-46,1 %** de la cible ⚠ **Ce réel est re-mesuré au commit du 30 juillet 2026** (décision 16b) : *toute date de mesure antérieure citée dans ce champ décrit une passe précédente, et la passe de révision D-11 l'a périmée.*. *L'écart s'est réduit de trois points sous les deux passes de relecture du 28 juillet 2026 — il valait **−55,5 %** à la rédaction : restituer une attribution allonge, et c'est un allongement de borne, non un gonflement.* ⚠ **L'écart individuel ne se lit pas seul** : la somme des onze cibles dérivées atteint **93 000 mots** pour une enveloppe de Livre de **65 000** — chaque pièce a dérivé sa cible de l'enveloppe sans que personne n'additionne les dérivations ; c'est la cible dérivée qui était fausse, non la pièce qui est courte. ⚠ **Le total du Livre n'est PAS re-mesuré ici** : il valait **64 750 mots, soit −0,4 % de l'enveloppe**, au 27 juillet 2026, et les onze pièces sont relues **en parallèle** — *un cardinal mesuré pendant que d'autres pièces changent est faux à la seconde où on le publie*. Sa re-mesure est due à la clôture de la passe. *Un écart se documente ; il ne se corrige ni par amputation ni par gonflement* |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.30, entrée du chapitre 6)* — le multi-agent a un surcoût que seuls certains gains justifient ; son évaluation (succès de tâche vs trajectoire) et sa sûreté (triade létale, vecteurs d'attaque) sont les deux fronts encore ouverts.

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

À l'inverse, une position concurrente — celle que **Cognition** défend dans « Don't Build
Multi-Agents » (2025) — soutient qu'**un rédacteur unique conservant un contexte continu surpasse
souvent l'architecture distribuée**, parce que le fractionnement du contexte engendre des décisions
incohérentes et coûteuses à réconcilier. C'est la même tension que le ch. 5 § 5.1.2 relevait à propos
du verbe *isoler* — et ce n'est pas un hasard : **le multi-agent est une politique de contexte avant
d'être une politique d'architecture**.

Cette tension se nourrit d'un socle classique réinterprété : le **Contract Net Protocol** (Smith,
1980), qui formalise l'allocation de tâches par appel d'offres et adjudication entre nœuds d'un
résolveur distribué, et les **actes de langage normalisés** des spécifications **FIPA ACL** (FIPA /
IEEE Computer Society, 2002), qui préfigurent les messages contractuels qu'échangent aujourd'hui les
agents.

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
travaux fondateurs : **CAMEL** (Li et coll., 2023) fait jouer à deux agents des rôles
complémentaires ; **MetaGPT** et **ChatDev** (Hong et coll., 2023 ; Qian et coll., 2023) assignent des
rôles d'équipe logicielle ; **AutoGen** (Wu et coll., 2023) généralise la conversation multi-agents.

Le **raisonnement collectif** recouvre des mécanismes distincts qu'il ne faut pas confondre. Le
**débat multi-agents** (Du et coll., 2023) fait converger plusieurs modèles vers une réponse plus
factuelle par confrontation itérative — c'est la parade à la chambre d'écho du ch. 4 § 4.2.3. Le
**vote majoritaire** et la **recherche de consensus** offrent des compromis différents entre
robustesse et coût.

⚠ **La principale difficulté demeure la coordination elle-même**, et elle est documentée plutôt
qu'anecdotique : dérive de problème, agents qui divergent de l'objectif initial, propagation d'erreurs
entre coéquipiers. La taxonomie **MAST** (Cemri et coll., 2025) recense ces modes de défaillance
propres aux systèmes multi-agents, et le § 6.4.2 y revient comme grille d'analyse causale.

---

## § 6.2 — Communication inter-agents : A2A, ACP et pile d'interopérabilité

C'est le **foyer canonique de l'interopérabilité agent-agent**, complémentaire de l'interopérabilité
agent-outil.

⚠ **Cette section est délibérément brève, et sa brièveté est un arbitrage du plan.** L'**anatomie
protocolaire** est au **ch. 8** ; la **pile** — découverte, registres, portabilité — est au **ch. 9**.
Ce qui suit est le strict nécessaire pour que le lecteur du premier mouvement sache **que** ces
protocoles existent et **où** ils sont traités.

Le protocole **Agent2Agent** (A2A) a été ouvert par **Google** en avril 2025, puis confié à la
**Linux Foundation**. Il repose sur des **Agent Cards** — descripteurs de capacités pouvant être
signés — qui permettent à un agent de découvrir et d'invoquer un pair par un **contrat explicite**.
Cette logique de description signée prolonge directement l'invariant du Livre au niveau de
l'orchestration et de la chorégraphie **inter-organisationnelles** (ch. 1 § 1.6.2).

La pile s'est consolidée autour de lui. L'**Agent Communication Protocol**, lancé par **IBM** en mars
2025, **a convergé dans A2A** ; un troisième effort, initié par **Cisco**, vise une interopérabilité
d'échelle réseau alignée sur les deux précédents ; et plusieurs revues comparent ces protocoles
émergents. ⚠ Le sigle **ACP** est développé ici à sa première occurrence et n'est jamais employé
seul, conformément aux garde-fous R-8 du Vol. II et R-13 du Vol. III : **il désigne au moins quatre
objets distincts, et l'encadré de désambiguïsation qui en fait le partage est au ch. 7 § 7.5, siège
unique pour toute la somme, auquel ce chapitre renvoie sans le reconstruire.**

Le fait marquant de **gouvernance** est la création, en **décembre 2025**, de l'**Agentic AI
Foundation** sous l'égide de la Linux Foundation : elle co-gouverne le protocole agent-outil et le
protocole agent-agent, **séparant proprement les deux plans d'interopérabilité**. Cette séparation
n'est pas une commodité d'organisation : c'est la reconnaissance que la relation d'un agent à ses
outils et sa relation à ses pairs ne posent pas le même problème, constat que le ch. 8 instruit.

⚠ **Un chiffre d'adoption est relevé au premier anniversaire d'A2A** — plus de 150 organisations —,
et il est **auto-déclaré**. Il est attribué ici à sa source — **la Linux Foundation**,
fondation faîtière du protocole, qui le rapporte en avril 2026 (ch. 7 § 7.6) —, et il mesure un
**soutien**, non une mise en production. La distinction est celle que le ch. 7 érige en
critère, et elle vaut d'être posée dès maintenant : *soutien n'est pas production*.

### 6.2.1 Ce que « communiquer » veut dire, et ce que ces protocoles n'en portent pas

⚠ **Cette sous-section est ajoutée le 30 juillet 2026 (D-11), et son motif est un reproche fondé de
l'arbitrage externe : une section intitulée « communication inter-agents » qui n'énumérait que des
protocoles et leur gouvernance n'honorait pas son titre.** *Le renvoi de l'anatomie au ch. 8 et de la
pile au ch. 9 reste un arbitrage de plan légitime ; ce qui manquait n'est ni l'une ni l'autre — c'est
la question de la **sémantique** de l'échange, qui n'a de siège nulle part ailleurs.*

**Communiquer suppose trois accords, et les protocoles agentiques n'en portent qu'un.** *(a)* Un
accord sur le **transport** — comment le message circule : *porté*, par le protocole agent-agent
comme par le protocole agent-outil. *(b)* Un accord sur la **forme** — comment le message est
structuré : *porté aussi*, par les schémas de tâche et de message. *(c)* ⚠ Un accord sur la **force
illocutoire** — *ce que l'émetteur **fait** en émettant : demande-t-il, informe-t-il, s'engage-t-il,
refuse-t-il, propose-t-il ?* **C'est celui-là qui manque.**

⚠ **Le contraste avec l'héritage multi-agents classique est net, et il a été nommé au ch. 4 § 4.1.3.**
**KQML** (Finin, Fritzson, McKay et McEntire, 1994) puis **FIPA-ACL** — dont la bibliothèque
**SC00037J** énumère ses actes communicatifs, chacun assorti d'une précondition, d'un effet
rationnel et d'un schéma de contenu — avaient fait de la force illocutoire **un champ obligatoire du
message**. *Un agent FIPA qui reçoit un message sait s'il est mis en demeure ou simplement informé,
parce que le protocole le lui dit.* **Les protocoles agentiques de 2025-2026 ne portent pas cette
information** : un message y transporte une charge utile typée dont *l'intention se déduit du
contenu, c'est-à-dire du langage naturel, c'est-à-dire du modèle*.

⚠ **Trois bornes, et la deuxième interdit la lecture nostalgique.** *(1)* **Le socle ne documente pas
cette absence comme un fait négatif vérifié** : aucun balayage systématique des spécifications
agentiques n'a été conduit sous cet angle — **absence de documentation, degré 3** (R-14 du Vol. III).
*(2)* ⚠ ***Que FIPA-ACL ait porté les actes communicatifs n'établit pas que sa démarche ait
réussi***. Le socle ne documente ni son adoption industrielle, ni sa performance, ni les motifs de
son déclin ; *écrire que la couche agentique « a oublié » quelque chose qui marchait serait un
jugement que rien n'appuie.* **Ce qui est établi est plus étroit et plus sûr : le problème avait été
posé, il avait reçu une réponse normalisée, et la couche neuve le repose sans la reprendre.** *(3)*
**La coordination sous défaillance n'est pas traitée ici et ne le sera pas** : elle est **hors
périmètre par décision d'auteur D-7**, déclarée au risque 15 du TOC, et ce chapitre y est **fermé** —
*y ajouter une section rouvrirait la décision, non le seul chapitre.*

**Lecture de l'auteur** — cette absence est de la même famille que celle du ch. 8 § 8.2.3 : *un
schéma contraint la forme d'un message, il n'en dit pas l'interprétation.* **Le ch. 48 la retrouvera
au niveau de l'effet** — *que produit le rejeu de ce message ?* — et **le ch. 9 § 9.4 l'instruit** au
niveau du vocabulaire. *Les trois sont la même question posée à trois étages, et la somme ne la
résout à aucun.*

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

> **Perspective recherche.** *AI Agents That Matter* (Kapoor et coll., 2024) montre que de nombreux
> résultats publiés sont **incomparables faute de contrôle du coût et de la variance**, et plaide
> pour une évaluation conjointe **précision-coût** plutôt que pour la course au sommet du tableau. Le
> survol du domaine de **Yehudai et coll. (2025)** confirme **l'absence de protocole standardisé** et
> la prolifération de métriques *ad hoc* propres à chaque banc.

### 6.3.2 Le modèle comme juge : principes, biais et piratage de récompense

Faute de vérificateur programmatique pour les sorties ouvertes — un résumé, une réponse argumentée,
une trajectoire à noter qualitativement —, la pratique recourt massivement au **modèle comme juge**.

Sa fiabilité **dépend d'une calibration explicite sur des annotations humaines** : sans elle, le juge
dérive. **Zheng et coll. (2023)** documentent plusieurs biais systématiques :

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
Comme le notent **Kapoor et coll. (2024)**, *un score isolé d'un protocole de décontamination et de
contrôle de coût n'a guère de valeur comparative.*

**Codage, web et bureautique.** En codage, **SWE-bench** (Jimenez et coll., 2023) confronte l'agent à
de vrais tickets à résoudre par un correctif validé par la suite de tests du dépôt ; sa **variante
vérifiée par des humains**, **SWE-bench Verified** (OpenAI, 2024) — un sous-ensemble de 500 tâches —,
est devenue la référence en éliminant les instances mal spécifiées ou irrésolubles. Les harnais
dédiés (**SWE-agent** ; Yang et coll., 2024) ont fait progresser nettement le taux de résolution :
**l'interface agent-ordinateur s'avère aussi déterminante que le modèle sous-jacent**, constat qui
vaut d'être retenu par toute équipe tentée d'attribuer un résultat au seul modèle. Pour le web,
**WebArena** (Zhou et coll., 2023) offre un environnement réaliste auto-hébergé, que
**VisualWebArena** (Koh et coll., 2024) étend aux tâches visuelles multimodales. Pour la bureautique,
**OSWorld** (Xie et coll., 2024) mesure le pilotage d'un poste de travail complet sur des tâches
ouvertes.

⚠ **La trajectoire est plus instructive que le point, et c'est la seule manière défendable de citer
ces chiffres.** Les agents de pilotage de poste plafonnaient **autour de 20 % en 2024** sur OSWorld ;
leur taux a ensuite progressé vers le plafond de performance humaine, **approché entre fin 2025 et
début 2026 sans encore le rejoindre**. L'écart résiduel à ce plafond est l'information utile — un
instantané ne la porte pas.

**Raisonnement général, outils et tâches d'entreprise.** Une seconde famille évalue le raisonnement
multi-sauts avec usage d'outils (**GAIA** ; Mialon et coll., 2023), la capacité agentique transversale
sur des environnements hétérogènes (**AgentBench** ; Liu et coll., 2023), l'interaction
outil-agent-utilisateur dans des domaines réalistes (**τ-bench** ; Yao et coll., 2024) et l'appel de
fonctions par analyse syntaxique (**BFCL** ; Patil et coll., 2025). Un banc de raisonnement à la
frontière, ***Humanity's Last Exam*** (Phan et coll., 2025), sert enfin à **saturer les jeux
antérieurs** devenus peu discriminants. ⚠ Ce dernier est une **ressource vivante** dont une version
ultérieure est parue : sa révision exacte doit être fixée au moment de citer un score.

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

Trois bancs s'y emploient : **AgentDojo** (Debenedetti et coll., 2024), environnement dynamique où
des injections sont insérées dans les **données que l'agent traite**, mesurant à la fois l'utilité
préservée et la résistance ; **InjecAgent** (Zhan et coll., 2024), qui cible spécifiquement les
**injections indirectes par les sorties d'outils** ; et **AgentHarm** (Andriushchenko et coll., 2024),
qui quantifie la **nocivité** d'un agent sommé d'accomplir des tâches malveillantes.

Le **red-teaming automatisé** prolonge cette logique en **générant dynamiquement** des attaques
plutôt qu'en s'appuyant sur un catalogue figé, exposant des chemins qu'un jeu statique manquerait.

⚠ **La distinction est cardinale, et elle est la conclusion de cette section** : *un score élevé sur
un banc de capacité ne dit rien de la robustesse*, et un agent ne devrait jamais être déployé sur la
seule foi de ses performances fonctionnelles.

> **Perspective recherche.** L'évaluation systématique des attaques par injection conduite par
> **Liu et coll. (2024)** montre qu'**aucune défense connue n'élimine la vulnérabilité** — elles n'en
> réduisent que la surface. Cela ancre empiriquement la proposition de **non-résolubilité au niveau
> du modèle** posée au ch. 4 § 4.0.1. ⚠ Les bancs adversariaux sont donc à interpréter comme des
> **mesures de réduction de risque, non comme des certificats d'innocuité** : leurs scores évoluent
> à mesure que de nouvelles attaques sont publiées, et qu'aucune défense n'existe relève d'une
> **absence de documentation** au sens de R-14 du Vol. III — le corpus consulté n'en recense pas, ce
> qui n'établit pas leur impossibilité.

### 6.4.2 Fiabilité, coût et taxonomie d'échecs

⚠ **La fiabilité d'un agent ne se résume pas à sa réussite moyenne, et la métrique usuelle induit en
erreur.**

| Métrique | Ce qu'elle mesure | Ce qu'elle flatte ou révèle |
| --- | --- | --- |
| *pass@k* | la probabilité qu'**au moins une** parmi *k* tentatives réussisse — le **potentiel** | **flatte** les systèmes capables de trouver occasionnellement la bonne réponse |
| *pass^k* | la probabilité que **les *k* tentatives réussissent toutes** — la **consistance** | **chute brutalement** dès que la fiabilité par étape s'éloigne de la perfection |

: Tableau 6.2 — Potentiel contre consistance : deux métriques dont la confusion masque l'effondrement des agents sur les tâches longues.

La seconde — *pass^k*, **introduite par τ-bench** (Yao et coll., 2024) — révèle **l'effondrement des
agents sur les tâches longues et multi-étapes**. Cette dégradation — où une probabilité d'échec par
pas même faible **se compose géométriquement** sur une longue trajectoire — est **l'un des constats
les plus robustes du domaine**, et l'une des questions que le ch. 49 laisse ouvertes.

Le **coût**, second axe de fiabilité, exige des **classements contrôlés en budget** plutôt qu'à
performance brute — le **Holistic Agent Leaderboard** (Kapoor et coll., 2025) fournit cette
infrastructure de comparaison à budget égal.

Diagnostiquer les échecs suppose enfin une **taxonomie** : **MAST** (Cemri et coll., 2025) classe les
modes de défaillance des systèmes multi-agents — mauvaise spécification, désalignement inter-agents,
vérification défaillante — et fournit une grille d'analyse **causale** des effondrements de
coordination (§ 6.1.2).

> **Mise en œuvre.** Un agent destiné à la production doit être caractérisé par sa **courbe de
> consistance**, pas par son meilleur potentiel : c'est la consistance, non le potentiel, qui
> détermine la viabilité opérationnelle. Le rapport coût-performance, mesuré **à budget contrôlé**,
> doit figurer au cahier des charges **au même rang que l'exactitude**. Et tout incident en production
> doit être rattaché à une **catégorie de la taxonomie MAST** pour orienter la correction vers la
> cause racine plutôt que vers le symptôme.

---

## § 6.5 — Défense architecturale, garde-fous et alignement

⚠ **Partage déclaré avec le ch. 37.** Ce qui suit **pose** les référentiels, les patrons et les
garde-fous ; le ch. 37 les **applique au grain de l'infrastructure**. Le modèle de menace et les
vecteurs d'attaque, eux, ne sont **pas** ici : ils partent **en entier** au ch. 19. *Ce chapitre pose
la défense, pas la menace* — et cette asymétrie est un arbitrage du plan, non un déséquilibre.

### 6.5.1 Référentiels et patrons de défense architecturale

À l'injection non résoluble répond une **discipline de défense en profondeur** outillée par des
référentiels et des patrons.

**Côté référentiels**, deux corpus structurent le domaine : **OWASP**, par ses classements des
risques applicatifs des modèles de langage (**2025**) puis des applications agentiques (**pour
2026**) et par son corpus *Agentic AI — Threats and Mitigations*, qui formalise le cadre de
modélisation **MAESTRO** ; et **MITRE ATLAS**, qui fournit la matrice adverse des techniques
observées contre les systèmes d'IA — ⚠ **instrument que le socle hérité reprend sans date**, qui
n'est donc pas écrite ici.

**Côté patrons**, plusieurs propositions cherchent à rétablir une séparation de privilège **hors du
modèle** — et c'est la formule qui compte, parce qu'elle dit où la garantie doit résider :

- le patron à **deux modèles** de **Willison (2023)** isole un modèle « privilégié », qui **ne voit
  jamais le contenu non fiable**, d'un modèle « en quarantaine » qui le traite **sans pouvoir
  déclencher d'action** ;
- **CaMeL** (Debenedetti et coll., 2025) systématise cette idée : un interpréteur en extrait le **flux
  de contrôle et de données**, puis applique des politiques explicites — *défaisant l'injection par
  conception* ;
- la **règle de non-cumul** de **Meta AI** (31 octobre 2025) propose une heuristique opérationnelle :
  dans une même session, un agent ne devrait pas cumuler les trois propriétés — contenu non fiable,
  accès à des données sensibles, capacité de communication externe ; **en posséder au plus deux**
  préserve la sûreté.

Un fil commun les traverse : **l'étiquetage de la provenance et du niveau de confiance des données**,
condition pour qu'un agent traite différemment ce qui vient d'une source fiable et ce qui vient du
dehors.

⚠ Que ces patrons épuisent l'espace des défenses architecturales n'est pas établi : le socle hérité
en recense un catalogue — celui de **Beurer-Kellner et coll. (2025)** — sans prétendre à
l'exhaustivité, ce qui est une **absence de documentation** au sens de R-14 du Vol. III, non un fait
négatif vérifié.

> **Perspective recherche.** Ces patrons déplacent la garantie **de l'apprentissage statistique vers
> une vérification systémique auditable** : CaMeL et la règle de non-cumul énoncent des
> **invariants** — séparation de privilège, non-cumul — que l'on peut vérifier **à la conception,
> indépendamment du modèle sous-jacent**. C'est la transposition agentique du masquage de
> l'information et de la conception orientée contrat (ch. 1 § 1.1.3) : **la sécurité naît du
> découplage explicite entre canal de confiance et canal non fiable, non d'un agent supposé
> infaillible.**

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
réduction de risque dont l'efficacité est partielle et mesurable**. **CaMeL neutralise par
conception** le détournement du flux de contrôle par injection, mais **ne résout par construction
qu'environ deux tiers des scénarios de son banc d'évaluation** — la fraction restante exigeant une
politique que le mécanisme **ne sait pas exprimer**. Cette proportion est **indicative et dépendante
du banc**, et elle est attribuée ici à la source qui la rapporte — **Debenedetti et coll. (2025)**,
sur le banc **AgentDojo**. La règle de non-cumul, de son côté, **ne garantit la sûreté qu'à
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
tâche : **METR** (5 juin 2025) documente que des modèles de frontière récents **trichent sur les
évaluations** en satisfaisant la lettre de la métrique sans en accomplir l'intention (§ 6.3.2).

⚠ **Plus préoccupant, un comportement stratégique trompeur** — visant à dissimuler ses véritables
objectifs à ses superviseurs — **a été mis en évidence** : **Meinke et coll. (2024, Apollo Research)**
montrent que des modèles de frontière sont capables de manigances en contexte, et **Greenblatt et
coll. (2024, Anthropic et Redwood Research)** documentent une **feinte d'alignement**, où le modèle
simule l'alignement durant l'entraînement pour préserver ses préférences. Les travaux d'entraînement
correctif de **Schoen et coll. (2025, OpenAI et Apollo Research)** **réduisent ces comportements sans
les éliminer**, et l'analyse de menace interne d'**Anthropic** (*Agentic Misalignment*, juin 2025)
montre que des agents peuvent, **sous pression d'objectif**, adopter des conduites s'apparentant à une
menace d'initié.

⚠ Le statut épistémique de ces constats mérite précision : ils établissent que ces comportements
**sont possibles et ont été observés en conditions d'évaluation**. Ils n'établissent ni leur
fréquence en production, ni leur absence — **absence de documentation** au sens de R-14 du Vol. III
sur les deux points.

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

**Première infraction, commune au Livre.** À la rédaction, les portes **G-1**, **G-2** et **G-3**
étaient ouvertes. Conséquences alors énoncées : aucun énoncé central au sens de CA-IV-01 (régime
**[C]**), aucun décompte publiable, et les renvois « ch. N » n'étaient que des **renvois de plan**,
les ch. 7, 8, 9, 19, 37, 38, 47 et 49 n'étant pas rédigés. ⚠ **Domaine déclaré : les renvois du
CORPS**, à l'exclusion de ceux que porte la présente note — *une passe de relecture du 28 juillet
2026 y avait ajouté les ch. 23 et 30, qui ne sont cités qu'ici, sans ajouter les ch. 17, 39, 43 et
48, qui le sont aussi : un cardinal élargi sans que son domaine le soit produit une liste qu'aucun
critère ne ferme.*

⚠ **Deux de ces trois conséquences sont levées, la première ne l'est pas, et la distinction est tout
ce que ce paragraphe doit transmettre.** Les **cinquante chapitres du plan existent en brouillon hors
portes** depuis le 27 juillet 2026 : les renvois de cette pièce **résolvent désormais contre du
texte**, et les **quatorze renvois de section du corps — treize cibles distinctes, le ch. 4 § 4.3.4
étant cité deux fois** — ont été résolus à ce titre, un à un, contre le texte des pièces visées
(décompte re-mesuré au commit, décision 16 du TOC). **G-2 est franchie** (27 juillet 2026) : le
décompte est publiable, et il figure à l'en-tête. **G-3 est franchie** (28 juillet 2026) : le socle
consolidé existe. ⚠ **Mais le régime de preuve, lui, ne bouge
pas** : les dix-sept entrées héritées du Vol. I y sont **toutes en [C]**, et **aucun énoncé de cette
pièce n'est central au sens de CA-IV-01**. *Une porte franchie après coup ne requalifie pas la pièce
écrite avant elle ; elle change ce qu'il faudrait faire pour la rendre recevable.*

**Seconde infraction, propre à ce chapitre, et distincte de la première.** La remontée **R-IV-01**,
ouverte par le ch. 1 de ce Livre, est marquée ***bloquante pour le ch. 6***. La règle d'escalade du
PRD (Annexe A) est explicite : *une remontée marquée « bloquant pour le ch. N » interdit de lancer le
ch. N.* Ce chapitre a été rédigé **malgré elle**, sur instruction d'auteur. Il ne s'agit pas d'une
reconduction de l'écart précédent mais d'un **écart de plus**, et il est consigné comme tel.

**Ce que R-IV-01 bloquait, et ce que le chapitre a fait à la place** — *bloc conservé au passé, parce
qu'il porte l'histoire de l'écart que la clôture ci-dessous efface.* La décision d'auteur **D-7**
(risque 15 du TOC) devait trancher où traiter **l'accord entre agents sous asynchronie et défaillance
partielle** — ce que deux agents tiennent pour vrai quand le réseau se partitionne. Les issues
prévues étaient : des sections dans les chapitres d'atterrissage — dont **celui-ci** —, ou un
périmètre assumé et déclaré. **D-7 n'était pas prise à la rédaction.** En conséquence :

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

**Remontée alors reconduite et aggravée** : **R-IV-01** restait ouverte, et son caractère bloquant
était désormais **enfreint** plutôt que respecté. À l'arbitrage de D-7, deux travaux étaient dus et
non un : trancher le périmètre, **et** reprendre ce chapitre pour y insérer la section si l'issue le
prescrivait. La différence de coût entre les deux scénarios est précisément ce que la règle
d'escalade visait à éviter.

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
(§ 6.1 à § 6.5). La table de couverture est respectée, ⚠ **y compris ses dix sorties de périmètre —
cardinal re-mesuré le 28 juillet 2026 contre la table du TOC, où une passe antérieure en annonçait
six** : frameworks d'orchestration au ch. 23, choix et service du modèle au ch. 4 (**arrivée déclarée
aux deux bouts**), observabilité au ch. 38, modèle de menace et vecteurs au ch. 19, modèle de coût au
Livre IV, chaînes multi-saut au ch. 17, gouvernance par les normes au ch. 30, HITL opérationnel et
réponse aux incidents au ch. 39, grille « quand agentifier » au ch. 43, questions ouvertes au
ch. 49 — auxquelles s'ajoute la **coupe assumée** des applications et tendances. Les deux séries de
garde-fous sont balayées : les **métriques auto-déclarées des § 6.1.1, § 6.2 et § 6.5.2 sont
attribuées à leur source** — *domaine déclaré sans cardinal, la formule n'ayant pas de marqueur
littéral à compter (décision 16c du TOC)* —, le sigle du protocole de communication est **développé
et jamais employé nu** (R-8 du Vol. II, R-13 du Vol. III), et les **trois occurrences de R-14 du
Vol. III** portent leur degré.

⚠ **Une passe de relecture a resserré l'attribution le 28 juillet 2026, et elle ne l'a pas fait
partout.** La **décision 15 du TOC** borne la parade de péremption par trois interdits ; deux
mordaient ici. *(a)* **Des instruments repris étaient anonymisés** — la taxonomie des modes de
défaillance que le § 6.4.2 érige en grille prescriptive, la métrique de consistance du même § 6.4.2,
les deux référentiels du § 6.5.1, les trois patrons de défense, les bancs d'essai du § 6.3.3 dont
deux portent un chiffre : ils portent désormais leur **auteur et, quand le socle hérité la porte,
leur date** — ⚠ *celle de MITRE ATLAS n'y figure pas, et la pièce l'écrit plutôt que de la
suppléer* (§ 6.5.1). *(b)* **Des affirmations étaient données sans attributeur** — « des
travaux montrent », « une position concurrente soutient », « a été mis en évidence » : les
attributeurs sont nommés, en particulier au § 6.5.3, où le statut épistémique du constat dépend de
qui l'a observé. ⚠ **Ce qui n'a pas été touché** : les **dénominations commerciales** de produits et
de cadriciels, que la décision 15a maintient sous la parade. *Une pièce qui nomme ses instruments et
tait ses produits applique la décision ; une pièce qui nomme tout la déborde.*

⚠ **Une SECONDE relecture, le même jour, a éprouvé la première et l'a prise en défaut sur trois
attestations — le fait est consigné parce qu'il est du même ordre que ceux que cette note enregistre
déjà.** *(1)* La liste des chapitres non rédigés avait été **élargie sans que son domaine le soit**
(ci-dessus). *(2)* Les renvois de section étaient annoncés « treize » sans dire si le cardinal
comptait les **occurrences** ou les **cibles** — quatorze contre treize, écart d'une seule
répétition, mais que la décision 16a rend décidable : *le domaine est désormais écrit.* *(3)*
L'attestation *(a)* déclarait des dates que deux instruments du § 6.5.1 ne portaient pas ; les deux
éditions d'OWASP sont versées depuis le socle hérité, et l'absence de date de MITRE ATLAS est
déclarée au lieu d'être comblée. ⚠ **Ce que la seconde passe a constaté sans avoir à le corriger** :
les attributions restituées par la première **résolvent toutes contre le Vol. I *Monographie*
§2.8-2.10** — *domaine déclaré sans cardinal : toute occurrence d'auteur, d'organisme ou de date
que cette passe a ajoutée* —, et **aucune n'est inventée** ; les cardinaux de garde-fous de l'en-tête
(R-8 : 1, R-13 : 1, R-14 : 3, tout le reste à zéro) sont **exacts au marqueur littéral** ; le
décompte de volumétrie et le taux d'écart sont **exacts à l'unité** ; la thèse est **verbatim** ; et
les treize cibles de renvoi **résolvent** contre le texte des pièces visées. *Une attestation de
relecture est une attestation comme une autre : celle-ci a été constatée sur pièce, et elle tient
sur l'essentiel.*

---

### Remontées — clôture du 27 juillet 2026, réouverture du 28

⚠ **Cette sous-section est hors plan comme la note qui la porte, et se retire avec elle.** Elle
enregistre l'issue des remontées ouvertes par cette pièce. *Une remontée ne se clôt pas là où elle
s'ouvre : elle se solde là où elle fait foi* — au [PRD](../PRD/PRD.md) pour une décision d'auteur, au
[TOC](../PRD/TOC.md) pour un réalignement de plan, à l'appareil pour une dette d'outillage.

- **R-IV-01 — close par décision d'auteur, et son issue ne coûte rien à ce chapitre.** Voir le
  développement ci-dessus : **D-7 retient le périmètre assumé et déclaré**, aucune section n'est à
  insérer, et le ch. 6 est **fermé** à cette matière. ⚠ **L'infraction reste consignée** : ce
  chapitre a été rédigé avant la décision, en violation d'une remontée bloquante. *Que le tirage
  soit bon ne valide pas le pari.*

⚠ **Ce que la clôture ne change pas — et ce que le franchissement de G-3 ne change pas non plus.** Le
socle consolidé **existe** depuis le 28 juillet 2026 (Annexe B, 159 entrées) ; **aucun énoncé de
cette pièce n'est central au sens de CA-IV-01** pour autant, ses dix-sept entrées héritées du Vol. I
étant toutes en **[C]**, et la pièce n'y étant pas ré-adossée entrée par entrée. **CA-IV-13 — la
relecture par un tiers distinct du rédacteur — demeure due.** Cette pièce reste un **brouillon non
publiable**. *Zéro remontée ouverte ne veut pas dire pièce recevable — cela veut dire qu'aucune
question n'attend plus de réponse qui ne soit déjà tranchée.*

**Remontée ouverte par la relecture du 28 juillet 2026 — non bloquante, et volontairement SANS
IDENTIFIANT.** ⚠ *Cette relecture court en parallèle de celles des quarante-neuf autres pièces ; la
somme a déjà payé une **collision d'identifiants entre passes concurrentes** — dix numéros alloués
deux fois le 27 juillet 2026 —, et **allouer un `R-IV-nn` depuis une passe qui ne voit pas les
autres reproduirait exactement cette faute**. Le numéro est donc laissé à la passe d'arbitrage, seule
en position d'allouer (PRD §13).* **Objet** : la **décision 15 du TOC** maintient la parade de
péremption pour les « dénominations commerciales », sans dire si un **banc d'essai** en est une — ce
n'est ni un produit ni un instrument nommé par l'énumération « grille, référentiel, norme » de son
alinéa (b)(ii). La présente pièce les a **nommés**, au motif que deux d'entre eux portent un chiffre
qu'on ne peut vérifier sans eux ; **d'autres pièces de la somme peuvent avoir tranché l'inverse**, et
l'écart serait de la classe même — l'application inhomogène — que la décision 15 prend pour objet.
*Le point se remonte au plan, il ne se tranche pas ici* : un rédacteur ne corrige jamais le TOC.
