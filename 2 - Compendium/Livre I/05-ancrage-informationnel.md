# Chapitre 5 — Ancrage informationnel : mémoire, contexte, RAG agentique

*Livre I — Coopérer : fondements de l'interopérabilité et couche protocolaire agentique.
Premier mouvement — les fondements (ch. 1-6).*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — rédigé sur instruction d'auteur du 27 juillet 2026, **avant** les portes G-1, G-2 et G-3 du [PRD](../PRD/PRD.md) §5 ⚠ **Mise à jour du 27 juillet 2026, postérieure à la rédaction** : **G-2 et le volet Livre I de G-1 ont été franchis depuis** (PRD v0.8), et les **remontées de cette pièce sont closes**. ⚠ **Mise à jour du 28 juillet 2026, passe de relecture** : **G-3 est franchie à son tour** (PRD v0.14, TOC v0.30) et le socle consolidé existe — **159 entrées** —, mais **aucune ne couvre le périmètre de fusion de ce chapitre** (voir *Socle mobilisé*). La pièce reste donc un **brouillon non publiable** : aucun de ses énoncés n'est central au sens de CA-IV-01, et **CA-IV-11 comme CA-IV-13 demeurent insatisfaites**, D-6 ne fournissant pas de relecteur distinct du rédacteur. |
| **Date de gel** | **27 juillet 2026** — gel unique du compendium, **décision d'auteur D-1 prise** ce jour (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Ce gel n'efface pas ceux des sources**, qui restent portés ci-dessous : il date la reprise de chaque fait périssable à sa source primaire, non la matière elle-même. Matière condensée au gel de sa source — **juin 2026** (Vol. I). ⚠ **Deux fonctions produit citées y étaient en bêta à cette date ; il n'en reste qu'une au gel unique** — l'**édition de contexte** (§ 5.1.3) est toujours en bêta, en-tête d'activation daté inchangé ; l'**outil de mémoire** (§ 5.1.4) est passé en **disponibilité générale**. Constats pris à la source primaire le 27 juillet 2026 (registre du gel, faits 9 et 10). *Le seul écart que la re-datation du Livre I ait trouvé va dans le sens favorable : la pièce était trop prudente, non fausse* |
| **Socle mobilisé** | **Aucune entrée du socle consolidé — et depuis le 28 juillet 2026 ce n'est plus faute d'Annexe B, mais faute de couverture.** L'[Annexe B](../PRD/socle-consolide.md) est constituée (G-3 franchie, **159 entrées `S-001`…`S-159`**) ; ⚠ **aucune de ses entrées ne procède des §2.6-2.7 du Vol. I *Monographie***, périmètre de fusion de ce chapitre — balayage exhaustif de la colonne *Provenance* des 159 entrées, les **dix-sept** entrées héritées du Vol. I (`S-143`…`S-159`) venant de ses §7.x, §3.10.x, §2.10.2.x, §5.0.2-§5.1.1, de son Annexe B et de sa *Synthèse*. **Fait négatif vérifié** au sens de R-14 du Vol. III, domaine déclaré. Les énoncés résolvent donc contre le **Vol. I *Monographie* §2.6-2.7**, en régime **[C]** (PRD §7.1), comme avant la porte. **Aucun énoncé n'est central au sens de CA-IV-01.** ⚠ *Les seules entrées consolidées touchant la mémoire et la récupération portent sur leur empoisonnement — ainsi `S-069` et `S-152` —, matière affectée au **ch. 19** et exclue au § 5.0 : la couverture du socle et la sortie de périmètre du plan concordent* |
| **Garde-fous balayés** | **Les deux séries, intégralement.** ⚠ **Règle de décompte, et les cardinaux ci-dessous ont été re-mesurés sous elle le 28 juillet 2026** : un décompte d'occurrences porte sur le **marqueur littéral de l'identifiant** dans le **corps** de la pièce — en-tête et note de statut exclus —, et il se re-mesure au commit ; un garde-fou appliqué **sans identifiant écrit** se déclare par son **domaine balayé, sans cardinal**. Vol. II — R-1 à R-8 : **zéro occurrence** ; ⚠ **une réserve d'usage tenue** : les fonctions produit non généralement disponibles sont nommées comme telles, jamais présentées comme disponibles en général — c'est la doctrine que R-4 du Vol. II impose au RTR, appliquée ici par analogie hors de son domaine propre. ⚠ **Elles étaient deux au gel de la source, il n'en reste qu'une au gel unique** (§ 5.1.3) ; la réserve **est levée pour la seconde** (§ 5.1.4), sur constat à la source primaire — *une réserve se lève sur pièce, comme elle se pose.* ⚠ **Réserve `F-01` du Vol. II (MCP « cadre » d'autorisation, jamais « sécurisé ») : applicable depuis le 28 juillet 2026** — la décision 15 du TOC ayant fait nommer le protocole que la pièce désignait par périphrase, **trois occurrences de « MCP » entrent au corps** (§ 5.0, § 5.4.1 deux fois) ; **aucune ne le qualifie de sécurisé**, l'anatomie protocolaire partant au ch. 8. Vol. III — R-01 à R-13 : **zéro occurrence** ; **R-14 (trois degrés d'absence) : deux occurrences**, § 5.0 et § 5.2.2 — la première est un **fait négatif vérifié**, cas rare dans ce Livre, établi par le balayage documenté que le TOC porte sous l'entrée de ce chapitre |
| **Volumétrie cible** | ≈ 7 500 mots de corps (§ 5.1 à § 5.4). Enveloppe **dérivée, non prescrite**. ☑ **Décompte publiable depuis le franchissement de G-2** (27 juillet 2026). **Réel : 4 864 mots** de corps, mesurés par [`PRD/decompte.sh`](../PRD/decompte.sh) le 28 juillet 2026, seule autorité de décompte du volume — **−35,1 %** de la cible. ⚠ **Le réel a bougé DEUX fois le même jour, et les deux motifs sont un régime de preuve, non un gonflement** : **+390 mots** à la passe de relecture — la décision 15 du TOC a fait rétablir les auteurs, les dates et les noms d'instruments que la pièce désignait par périphrase —, puis **+77 mots** à la contre-vérification, qui a marqué **deux constructions d'auteur restées nues** (CA-IV-07, § 5.1.2 et § 5.2.2). Les deux passes sont journalisées au § 5.5. *Aucun écart n'a été corrigé ni par amputation ni par gonflement* (D-4). ⚠ **L'écart individuel ne se lit pas seul** : la somme des onze cibles dérivées du Livre atteint **93 000 mots** pour une enveloppe de **65 000** — chaque pièce a dérivé sa cible de l'enveloppe sans que personne n'additionne les dérivations, de sorte que la cible dérivée est fausse autant que la pièce est courte. ⚠ **Le réel du LIVRE n'est pas reporté ici** : il n'est pas re-mesurable pendant que les onze pièces sont en relecture simultanée, et **se re-mesure au terme de la passe**, sur le corpus que le commit produit |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.30, entrée du chapitre 5 — citée par copie, identique à la forme reprise depuis la v0.23)* — l'agent persistant se construit par l'ingénierie du contexte et une pile de récupération gouvernée.

---

## § 5.0 — Ce que ce chapitre traite, et ce qu'il ne traite pas

*Cadrage d'ouverture. La table détaillée du TOC ouvre ce chapitre à § 5.1 ; ce paragraphe liminaire
n'est pas une section du plan mais l'apparat qui en déclare la frontière, comme le ch. 4 le fait pour
la sienne.*

Un modèle de langage est **intrinsèquement sans état** : chaque appel d'inférence ne connaît du monde
que ce que sa fenêtre de contexte contient à l'instant de l'invocation, et tout ce qui en sort est
oublié dès la requête suivante. Or un agent, par définition, **agit dans la durée** — il enchaîne des
tours, poursuit un but sur plusieurs pas, reprend une tâche interrompue.

L'écart entre un modèle amnésique et un agent persistant se comble par une discipline d'ingénierie :
la gestion de l'**état informationnel** que l'agent écrit et relit. C'est l'objet de ce chapitre, et
il repose sur une distinction qu'il faut tenir fermement parce que la pratique la brouille :

| | Ce que c'est | Provenance |
| --- | --- | --- |
| **Mémoire** | ce que l'agent **produit et conserve** de sa propre activité | interne, écrite par l'agent |
| **Récupération** (RAG) | ce qu'il **va chercher** dans un corpus tiers | externe, écrite par d'autres |
| **Protocole d'accès** | la tuyauterie qui relie l'un et l'autre aux sources | ni l'un ni l'autre — un transport |

: Tableau 5.1 — Trois objets que la pratique confond, et qui n'ont ni le même cycle de vie ni la même gouvernance.

Le troisième — le protocole d'accès agent-outil, soit le **Model Context Protocol** (MCP) — n'est pas
traité ici : son anatomie est au **ch. 8**. Les deux premiers occupent respectivement les § 5.1-5.2
et les § 5.3-5.4.

⚠ **Ce chapitre ne traite pas l'empoisonnement de la mémoire et des sources, et cette absence est un
constat de source, non un oubli.** Un balayage documenté des §2.6-2.7 du Vol. I *Monographie* n'y
relève **aucune occurrence** de cette matière : elle vit ailleurs dans le volume source — au
§2.10.2.2 —, et le plan l'affecte au **ch. 19**, qui la relit comme un risque d'**identité des
sources**. C'est, au sens de l'échelle R-14 du Vol. III, un **fait négatif vérifié** — établi par
balayage — et non une absence de documentation. La distinction compte : ici on peut affirmer que la
matière n'est pas dans la source ; ailleurs dans ce Livre, on n'a pu affirmer que ne pas l'avoir
trouvée.

Le partage est donc net et il vaut d'être posé d'emblée : **ce chapitre pose l'ancrage ; le ch. 19 en
pose le versant hostile.** Le § 5.4.2 marque le point de jonction sans le franchir.

Le fil du **coût** domine par ailleurs tout ce qui suit. Chaque jeton conservé dans la fenêtre est
facturé **à chaque tour** — ce qui fait de la budgétisation du contexte une contrainte d'ingénierie de
premier ordre, non un raffinement d'optimisation.

---

![**Figure 5.0** — Mémoire, récupération et protocole d'accès : trois objets que la pratique confond.](../figures/f-05-00-trois-objets.svg)

## § 5.1 — Du modèle sans état à l'agent persistant : mémoire et ingénierie du contexte

*Le TOC intitule cette section « Du **LLM** sans état à l'agent persistant » ; la pièce traduit le
sigle, le registre du corpus n'admettant un terme technique anglais qu'entre parenthèses à sa
première occurrence. Déviation d'intitulé déclarée au titre de la décision 8 du TOC, remontée en
§ 5.5 ; la matière et la provenance sont inchangées.*

### 5.1.1 Taxonomie de la mémoire

Le passage du modèle sans état à l'agent persistant emprunte sa structuration aux architectures
cognitives classiques (ch. 4 § 4.2.2), qui distinguaient déjà mémoire de travail et mémoire à long
terme.

La **mémoire de travail** correspond au contenu effectivement présent dans la fenêtre de contexte au
moment de l'inférence : invite système, historique récent, observations d'outils du tour courant,
bloc de raisonnement actif. Elle est **volatile, bornée et coûteuse** — son occupation se paie en
jetons à chaque appel.

La **mémoire à long terme** vit hors de la fenêtre, dans un magasin externe que l'agent interroge
sélectivement. Les revues du domaine — Zhang et coll. (2024), Wu et coll. (2025) — reprennent une
tripartition issue de la psychologie cognitive et des architectures symboliques :

- la mémoire **épisodique** consigne des événements situés et datés — « lors de la session du 3 mars,
  l'utilisateur a refusé telle option » ;
- la mémoire **sémantique** retient des faits décontextualisés et stables — « l'utilisateur préfère le
  français canadien » ;
- la mémoire **procédurale** encode des compétences, des routines et des consignes d'action — « pour
  déployer, exécuter ces étapes dans cet ordre ».

⚠ **Cette taxonomie n'est pas une commodité descriptive : elle oriente les choix
d'implémentation**, parce que chaque type appelle un magasin, un rythme d'écriture et une politique de
récupération **distincts**. L'épisodique se prête à un journal horodaté et à une recherche par
similarité ; le sémantique, à un profil structuré ou à un graphe de faits ; le procédural, à des
fichiers relus à chaque démarrage (§ 5.1.4).

La cohérence d'un agent persistant tient précisément à ce que ces registres soient **gérés
explicitement** plutôt que noyés dans un historique conversationnel indifférencié. Un agent dont
toute la mémoire est un historique est un agent dont la mémoire ne se gouverne pas.

> **Perspective recherche.** La transposition de la mémoire humaine vers les agents est un programme
> de recherche actif, non une simple métaphore. Les revues de Wu et coll. (2025) et de Zhang et
> coll. (2024) cartographient les mécanismes — encodage, stockage, rappel, oubli — et soulignent que
> **la frontière entre mémoire et apprentissage
> paramétrique reste théoriquement floue** : ce que l'agent retient dans un magasin externe relève
> d'une mémoire **non paramétrique**, distincte de l'auto-amélioration par mise à jour des poids
> (ch. 4 § 4.3.5). C'est la même distinction que le ch. 4 posait entre adaptation en contexte et
> mise à jour du modèle, vue du côté de l'état plutôt que du côté de l'apprentissage.

### 5.1.2 L'ingénierie du contexte comme discipline

La gestion de la mémoire de travail s'est constituée en **discipline d'ingénierie à part entière**.
Son point de départ est empirique, et il est contre-intuitif : **les modèles n'exploitent pas
uniformément leur fenêtre de contexte**.

Deux phénomènes documentés le montrent. La **perte au milieu** (*lost in the middle*, Liu et coll.,
2023) établit que l'information placée au centre d'un long contexte est nettement moins bien utilisée
que celle située en tête ou en queue, dessinant une courbe de performance en U. La **dégradation
progressive** de la qualité à mesure que la fenêtre se remplit (*context rot*) s'y ajoute.

⚠ **Ensemble, ces deux constats ruinent une intuition répandue** : élargir indéfiniment la fenêtre ne
résout pas le problème de la mémoire. *Un contexte plus grand n'est pas un contexte mieux utilisé*,
et il coûte plus cher à chaque tour. C'est le point le plus important de la section, et celui que les
annonces de fenêtres toujours plus vastes rendent le plus facile à oublier.

L'ingénierie du contexte répond par un répertoire d'opérations désormais standardisé, que la
formulation de LangChain (2025) ordonne en **quatre verbes** :

- **écrire** — déporter hors fenêtre, dans un espace de travail ou une mémoire, ce qui doit survivre
  au-delà du tour ;
- **sélectionner** — n'admettre dans la fenêtre que ce qui sert le tour courant ;
- **compacter** — résumer ou comprimer l'historique pour libérer du budget ;
- **isoler** — cloisonner les contextes entre sous-tâches ou sous-agents pour éviter la contamination
  croisée.

⚠ **Le quatrième verbe fait débat, et le débat mérite d'être rapporté plutôt que tranché.** Cognition
(Yan, 2025) plaide au contraire pour un **fil de contexte continu et un rédacteur unique**
(*single writer*) plutôt qu'un cloisonnement multi-agents, au motif que l'isolation **fragmente le
contexte partagé** dont dépend la cohérence. Le ch. 6 § 6.1 retrouvera exactement cette tension en
pesant le surcoût du multi-agent.

Lecture de l'auteur — les deux positions ne portent vraisemblablement pas sur les mêmes tâches, ce
qui expliquerait qu'elles coexistent sans se réfuter. Le socle **rapporte les deux prises de position
et le motif de la seconde** ; il **n'établit pas** leurs domaines de validité respectifs, qu'aucune
des deux ne déclare. La conciliation est proposée comme lecture, non comme constat.

Anthropic (2025) présente l'ensemble de ces opérations comme la pratique consistant à **curer
délibérément l'ensemble minimal de jetons à haute valeur informationnelle**, plutôt qu'à accumuler.
C'est l'expression directe du fil du coût : chaque opération vise à maximiser le rendement
informationnel **par jeton facturé**.

> **Mise en œuvre.** Deux conséquences opérationnelles nettes. *(a)* **La taille effectivement utile
> de la fenêtre est inférieure à sa taille nominale**, et la **position** de l'information dans le
> contexte est une variable de conception, non un détail : placer les consignes critiques et les
> données saillantes en tête ou en queue. *(b)* Traiter le budget de jetons comme une **ressource
> rare à allouer explicitement** — d'autant que les jetons de raisonnement des modèles de réflexion
> (ch. 4 § 4.3.4) grèvent **le même budget**.

### 5.1.3 Compaction réversible, résumé et oubli actif

La **compaction** est l'opération par laquelle un agent réduit l'empreinte de son historique pour
rester sous le seuil de sa fenêtre tout en préservant l'essentiel de ce qu'il a accompli.

Le mécanisme canonique est l'**auto-compaction à seuil** : lorsque l'occupation approche d'une limite
configurée, l'agent déclenche un résumé de la portion ancienne de l'historique, qui remplace les
tours détaillés par une synthèse compacte. Une fonction produit apparentée, documentée par Anthropic
(2025) — l'**édition de contexte** (*context editing*) —, permet de retirer ou de condenser des
éléments devenus inutiles, par exemple des observations d'outils volumineuses dont **seul le verdict
importe encore**.

⚠ **Cette fonction est en bêta**, avec une version d'interface datée que son éditeur prescrit de
fixer au moment d'intégrer, son comportement et son contrat pouvant évoluer. Elle est citée comme
telle et **jamais présentée comme une disponibilité générale**. ⚠ **Statut re-vérifié à la
documentation d'Anthropic le 27 juillet 2026, au gel unique : toujours en bêta**, en-tête
d'activation daté inchangé (registre du gel, fait 9). *C'est la seule des deux fonctions produit de
ce chapitre à l'être encore.*

L'enjeu de conception est la **réversibilité**. Une compaction agressive risque d'effacer un détail
qui redeviendra pertinent ; une compaction trop prudente ne libère pas assez de budget. La bonne
pratique consiste à **compacter en conservant un pointeur vers la trace intégrale**, déportée dans un
magasin persistant, de sorte que le résumé reste **augmentable à la demande** sans peser sur la
fenêtre courante.

L'**oubli actif** complète le dispositif : plutôt que de tout retenir, l'agent élague délibérément
les éléments à faible valeur — bruit conversationnel, tentatives avortées, redondances. Le bénéfice
est double, et le second est moins évident que le premier : réduire le contexte améliore le coût,
**et** atténue la dégradation décrite en § 5.1.2.

La compaction n'est donc **pas une simple troncature, mais une politique d'allocation** : elle
arbitre, tour après tour, ce qui mérite de rester dans la mémoire de travail et ce qui peut être
résumé ou écarté.

### 5.1.4 Mémoire procédurale et fichiers de configuration d'agent

La mémoire procédurale se matérialise par une stratification claire entre trois plans :

1. le **contexte actif** — ce qui occupe la fenêtre au tour courant ;
2. l'**espace de travail** (*scratchpad*) — où l'agent note des résultats partiels qu'il relira **au
   sein de la même tâche** ;
3. le **magasin persistant** — ce qui survit **entre les sessions**.

L'**outil de mémoire** d'Anthropic (2025) instrumente ce dernier plan en tant que primitive, offrant
à l'agent des opérations explicites pour écrire, relire et mettre à jour une mémoire externe.
⚠ **Cette fonction était en bêta au gel de la source (juin 2026) ; elle est en disponibilité générale
au gel unique de la somme** — constat pris à la documentation d'Anthropic le 27 juillet 2026, qui
déclare l'absence de tout en-tête d'activation de bêta (registre du gel, fait 10). Son identifiant de
type reste daté, et c'est **lui** qui fixe le contrat : une fonction généralement disponible n'est
pas une fonction dont l'interface a cessé de se versionner.

Au-dessus de cette mécanique, une convention s'est imposée pour la mémoire procédurale **durable** :
les **fichiers de configuration d'agent** relus au démarrage. Le format `AGENTS.md`, contribué à
l'Agentic AI Foundation de la Linux Foundation le **9 décembre 2025**, et son équivalent `CLAUDE.md`
codifient, dans un fichier **versionné avec le projet**, les consignes, conventions et routines que
l'agent doit appliquer à chaque exécution.

Ces fichiers jouent un **double rôle** qui mérite d'être explicité, parce qu'il est rarement nommé :
ils sont à la fois une **mémoire procédurale** — le « comment faire » stable de l'agent — et une
**spécification d'agent** — le contrat explicite de son comportement attendu.

C'est l'invariant du Livre au plan mémoriel : la procédure est **découplée** de toute session
particulière, exprimée comme un **contrat** lisible par l'humain et par la machine, et elle **évolue**
par édition du fichier plutôt que par ré-entraînement. Le passage de ces formats sous gouvernance de
fondation confirme leur statut de **point d'interopérabilité** plutôt que de détail d'implémentation
propriétaire — et c'est à ce titre que le ch. 7 les reprend.

> **Mise en œuvre.** En déploiement, la mémoire procédurale gagne à être **traitée comme du code** :
> fichiers versionnés dans le dépôt, revus en revue de code, et **tenus courts** pour ne pas gonfler
> la fenêtre à chaque démarrage. Cette dernière contrainte est réelle et souvent négligée : un
> fichier de consignes qui grossit sans discipline devient un coût fixe payé à chaque exécution.

---

## § 5.2 — Architectures de mémoire long terme et pile de récupération

### 5.2.1 Architectures de mémoire long terme et pile de récupération

Au-delà des fichiers de configuration, plusieurs architectures proposent des magasins structurés et
des politiques de gestion explicites. Elles se distinguent moins par leur mécanique de stockage que
par la **métaphore d'organisation** qu'elles retiennent, et cette métaphore commande leurs propriétés.

Une première lignée pose l'**analogie du système d'exploitation**. MemGPT (Packer et coll., 2023),
aujourd'hui porté par le projet Letta, fait gérer au modèle lui-même une hiérarchie mémoire à trois
niveaux — un contexte principal en fenêtre, une mémoire d'archives et une mémoire de rappel hors
fenêtre — en **paginant** l'information entre ces niveaux comme un système d'exploitation gère la
mémoire virtuelle.

Une deuxième introduit un **flux de mémoire horodaté** : les Generative Agents (Park et coll., 2023)
l'assortissent d'un mécanisme de récupération combinant **récence, importance et pertinence**, et
d'une réflexion qui synthétise des souvenirs de plus haut niveau.

D'autres visent la mise en production — Mem0 (Chhikara et coll., 2025), couche extensible extrayant
et consolidant les faits saillants au fil des échanges —, organisent la mémoire en système
multi-agents dédié — MIRIX (Wang et Chen, 2025) — ou appliquent un principe d'interconnexion
dynamique entre souvenirs — A-MEM (Xu et coll., 2025).

Une dernière lignée structure la mémoire comme un **graphe de connaissances temporel**, où faits et
relations portent une **validité datée** : Zep, fondé sur le moteur Graphiti (Rasmussen et coll.,
2025). C'est la seule des lignées ci-dessus dont la description porte explicitement la **révision**
d'un fait ; les autres n'en disent rien, ce qui n'établit pas qu'elles n'en traitent pas.

Sous ces architectures opère une **pile de récupération mutualisée** avec celle du RAG (§ 5.3.2) :
bases vectorielles pour la recherche dense, recherche **hybride** combinant dense et lexical,
**réordonnancement** des candidats.

⚠ **Ce partage est délibéré et il éclaire la thèse.** La différence entre mémoire et récupération
tient **moins à la mécanique qu'à la provenance et au cycle de vie** de ce qui est stocké : état
produit par l'agent d'un côté, corpus externe de l'autre. Deux objets qui partagent leur outillage et
diffèrent par leur gouvernance — c'est exactement la configuration où l'on confond les deux, et où la
confusion coûte cher.

> **Perspective recherche.** Ces architectures convergent vers une représentation **hybride** où le
> graphe temporel concurrence l'index vectoriel pur. Chez Zep/Graphiti (Rasmussen et coll., 2025),
> modéliser explicitement l'évolution des faits dans le temps — **une relation peut devenir caduque
> sans être effacée** — répond au problème de la
> cohérence d'une mémoire qui doit oublier ou réviser plutôt qu'accumuler. La parenté avec les
> graphes de connaissances du ch. 2 § 2.3.5 n'est pas fortuite : mémoire à long terme et récupération
> structurée partagent un même substrat.

### 5.2.2 Consolidation, ancrage et évaluation de la mémoire

Une mémoire à long terme n'a de valeur que si elle est correctement **écrite**, **consolidée** et, au
besoin, **oubliée**. Ces trois opérations sont distinctes :

- l'**écriture** décide ce qui mérite d'être retenu et sous quelle forme ;
- la **consolidation** fusionne, met à jour et abstrait des souvenirs épars en représentations plus
  stables — c'est elle qui transforme une série d'épisodes en un fait sémantique, ou qui **révise un
  fait obsolète** ;
- l'**oubli** élague ce qui est périmé ou contradictoire, pour éviter que la mémoire ne dérive en
  magasin incohérent.

⚠ **Ces opérations touchent directement à la fiabilité, et par un mécanisme qu'il faut nommer.** Une
mémoire mal gérée devient **une source d'hallucinations** : un agent qui rappelle un fait erroné avec
aplomb propage l'erreur sur toute la trajectoire.

Lecture de l'auteur — la différence avec une hallucination ordinaire tiendrait à ce que celle-ci est
*persistante* et *auto-confirmante*, l'agent relisant le souvenir erroné à la session suivante. Le
socle **établit la propagation de l'erreur sur la trajectoire** ; il **ne caractérise pas** cette
persistance entre sessions, et ne la mesure pas.

Deux pratiques atténuent ce risque, et elles reviendront à l'identique côté récupération (§ 5.4.2) :

- les **citations** — ancrer chaque assertion mémorisée à sa source ou à l'épisode qui l'a produite,
  de sorte que l'agent puisse **justifier** ce qu'il avance plutôt que de le confabuler ;
- l'**abstention** — reconnaître qu'il ne sait pas, plutôt qu'inventer un souvenir absent.

L'évaluation de la mémoire fait l'objet de bancs dédiés : LongMemEval (Wu et coll., 2024) mesure la
mémoire interactive à long terme sur des historiques étendus, LoCoMo (Maharana et coll., 2024) la
mémoire conversationnelle sur de très longues durées, MemoryAgentBench (Hu et coll., 2025) la
mémoire au fil d'interactions incrémentales.

⚠ **Ce que ces bancs vérifient dépasse le rappel**, et c'est ce qui en fait autre chose qu'une mesure
de stockage : ils éprouvent la capacité à **mettre un fait à jour**, à **l'oublier quand il le faut**
et à **raisonner sur plusieurs souvenirs** — c'est-à-dire la qualité de la **consolidation**. Qu'il
n'existe pas de mesure consolidée de cette qualité au-delà de ces bancs relève d'une **absence de
documentation** au sens de R-14 du Vol. III, non d'un fait négatif vérifié.

> **Mise en œuvre.** En production, l'évaluation de la mémoire s'inscrit dans la boucle d'évaluation
> continue que le ch. 39 instruit : constituer, **à partir des traces réelles**, des jeux d'épreuve
> mesurant le rappel, la mise à jour et l'abstention. ⚠ **La consolidation et l'oubli doivent être
> instrumentés et observables au même titre que les appels d'outils** — faute de quoi une dérive
> silencieuse de la mémoire passe inaperçue jusqu'à ce qu'elle se traduise en erreur visible. C'est,
> transposé à l'état interne, le principe d'observabilité du ch. 3 § 3.4.5.

---

## § 5.3 — RAG agentique : planifier-récupérer-critiquer-itérer

L'ancrage par la mémoire dote l'agent d'un état interne qu'il écrit et relit ; il reste néanmoins
**coupé des corpus volumineux et mouvants** — bases documentaires, entrepôts relationnels, graphes de
connaissances — qui dépassent la fenêtre de contexte.

La **génération augmentée par récupération** (*Retrieval-Augmented Generation*, RAG), introduite par
Lewis et coll. (2020) pour les tâches à forte intensité de connaissances, constitue le second pilier
de l'ancrage. Là où la mémoire est l'état que l'agent **possède**, la récupération est l'information
qu'il **va chercher au moment voulu**.

### 5.3.1 Du RAG statique au RAG agentique

Le RAG dit *naïf* enchaîne une fois pour toutes trois étapes — encoder la requête, récupérer les
passages les plus proches, conditionner la génération.

⚠ **Cette linéarité fait sa fragilité, et le constat est documenté plutôt qu'intuitif** : Barnett et
coll. (2024) recensent **sept** points de défaillance récurrents de l'ingénierie d'un système de
récupération, du contenu manquant au passage pertinent mais non extrait — autant de pannes qu'**une
passe unique ne peut ni détecter ni corriger**.

Le RAG **agentique** répond en transformant le pipeline figé en **boucle de contrôle** : l'agent
planifie sa stratégie de recherche, déclenche une ou plusieurs récupérations, **critique** la
suffisance et la pertinence des éléments obtenus, puis décide d'itérer, de reformuler ou de
s'arrêter. La revue de Singh et coll. (2025) cartographie cet espace, où la récupération devient
**une action outillée parmi d'autres** plutôt qu'une étape préalable — ce qui la place,
structurellement, dans la boucle du ch. 4 § 4.2.1.

Deux mécanismes auto-correcteurs en constituent l'ossature. Self-RAG (Asai et coll., 2023) entraîne
le modèle à émettre des jetons de réflexion qui décident **à la volée** s'il faut récupérer, puis
évaluent la pertinence des passages et l'étayage de chaque affirmation produite. Corrective RAG
(Yan et coll., 2024) ajoute un **évaluateur léger** qui note la qualité de la récupération et,
lorsqu'elle est jugée incorrecte ou ambiguë, déclenche un **repli** plutôt que de générer sur des
bases erronées.

La **récupération itérative entrelacée au raisonnement** — IRCoT (Trivedi et coll., 2023), FLARE
(Jiang et coll., 2023), Self-Ask (Press et coll., 2023) — pousse la même idée : chaque étape de
raisonnement peut déclencher une nouvelle requête, ce qui réduit les hallucinations sur les questions
**multi-sauts** en rapprochant la génération de ses sources à chaque pas.

> **Perspective recherche.** La frontière entre RAG agentique *invité* et *entraîné* se déplace vers
> l'**apprentissage de la politique de récupération** : Search-R1 (Jin et coll., 2025) optimise par
> renforcement une politique qui intercale raisonnement et appels à un moteur de recherche, et
> instancie ainsi, pour la récupération, la logique du renforcement multi-tours du ch. 4 § 4.3.5.
> La boucle cesse alors d'être un échafaudage
> d'invite pour devenir un **comportement appris**, vérifiable contre la justesse finale.

> **Mise en œuvre.** La boucle auto-correctrice **échange du coût contre de la fiabilité** : chaque
> tour de critique et de re-récupération consomme des jetons et de la latence. Le **critère d'arrêt**
> — nombre maximal de tours, budget d'appels, seuil de confiance de l'évaluateur — est donc un
> paramètre de conception au même titre que pour toute boucle agentique, et non un détail. Un
> évaluateur de pertinence léger, à la manière de Corrective RAG, est souvent **plus économique
> qu'une re-génération complète** par un modèle frontière.

### 5.3.2 Stratégies de récupération, ingestion et structures

La qualité d'un système de récupération se joue **d'abord au stade de la récupération et de
l'ingestion**, en amont de toute boucle agentique. C'est un ordre de priorité que la fascination pour
la boucle fait souvent oublier.

**Côté récupération**, la pratique a convergé vers l'**hybridation**. La recherche **dense** par
plongements — DPR (Karpukhin et coll., 2020), Contriever (Izacard et coll., 2022) — est forte sur la
proximité sémantique ; la recherche **lexicale** creuse, de type BM25, reste supérieure sur les
termes rares, les identifiants et les correspondances exactes. Les listes de résultats sont fusionnées
par la **fusion de rangs réciproques** (*Reciprocal Rank Fusion*, RRF), qui **combine les rangs sans
recalibrer les scores**, puis un **réordonnanceur** — modèle d'interaction tardive comme ColBERT
(Khattab et Zaharia, 2020), ou réordonnanceur croisé — affine le classement final sur un petit
ensemble de candidats. Le choix des encodeurs et des réordonnanceurs s'appuie sur des bancs dédiés :
BEIR (Thakur et coll., 2021) pour la généralisation zéro-coup, MTEB (Muennighoff et coll., 2023) pour
les plongements de texte. Les techniques d'**expansion de requête** — HyDE (Gao et coll., 2023),
qui génère un document hypothétique pour densifier la recherche — complètent l'arsenal.

**Côté ingestion**, le découpage naïf en fenêtres de taille fixe **brise le contexte et dégrade la
pertinence**. Deux techniques y répondent : le découpage **contextuel**, qui préfixe chaque fragment
d'un résumé situant sa place dans le document, et le découpage **tardif** (*late chunking*), qui
encode le document entier **avant** de le segmenter, pour que chaque fragment hérite du contexte
global.

**Pour les questions exigeant l'agrégation d'informations dispersées**, les structures hiérarchiques
et de graphe deviennent décisives : RAPTOR (Sarthi et coll., 2024) construit récursivement un arbre
de résumés autorisant une récupération à plusieurs niveaux de granularité ; GraphRAG (Edge et coll.,
2024) extrait du corpus un graphe de connaissances dont les communautés servent les requêtes globales
de synthèse ; HippoRAG (Jimenez Gutierrez et coll., 2024) s'inspire de la consolidation
neurobiologique pour la récupération multi-sauts.

> **Mise en œuvre.** Le pont avec le graphe de connaissances et la pile du Web sémantique a été posé
> au ch. 2 § 2.4.2, où GraphRAG a son traitement ; la récupération structurée le matérialise du côté
> agentique. En pratique, la chaîne *dense + BM25 → RRF → réordonnancement* forme un **contrat de
> récupération stable**
> dont chaque maillon se substitue indépendamment sans réécrire l'appelant — application directe du
> découplage à des corpus qui évoluent en continu. Le réordonnancement, par son coût marginal, se
> réserve aux quelques dizaines de candidats de tête.

---

![**Figure 5.3** — Du RAG statique au RAG agentique : d'une passe unique à une boucle de contrôle.](../figures/f-05-03-rag-agentique.svg)

## § 5.4 — Données structurées, accès d'entreprise et gouvernance d'ancrage

### 5.4.1 Données structurées et accès d'entreprise

⚠ **Une part majeure de l'information d'entreprise ne réside pas dans des documents non structurés**
mais dans des bases relationnelles, où l'accès passe par une **requête** plutôt que par une
similarité vectorielle. La récupération documentaire, à elle seule, laisse cette part hors d'atteinte.

La traduction d'une question en langage naturel vers une requête exécutable — le *text-to-SQL* — est
le **pendant structuré** de la récupération, et sa version agentique en hérite la boucle : générer
une requête, l'exécuter, **observer le résultat ou l'erreur**, corriger, recommencer.

Les bancs d'essai jalonnent une montée en difficulté instructive. Spider (Yu et coll., 2018) a posé
le cadre de l'analyse sémantique inter-domaines ; BIRD (Li et coll., 2023) a introduit les **grandes
bases bruitées** et la contrainte d'**efficacité d'exécution**, rapprochant l'évaluation des
conditions réelles ; Spider 2.0 (Lei et coll., 2025) franchit un seuil en confrontant les modèles à
des flux d'entreprise réalistes — schémas massifs, dialectes multiples, requêtes imbriquées sur des
entrepôts infonuagiques.

⚠ **C'est sur ce dernier que le constat porte** : Lei et coll. (2025) y observent que les méthodes
**en une passe s'effondrent**, et que seule une démarche agentique — exploration du schéma, exécution
incrémentale, correction d'erreurs — maintient une performance utile. Itérer contre le moteur est
précisément ce que la boucle apporte au-delà de la simple génération, et le constat est ici **mesuré
plutôt qu'argumenté**.

L'accès aux données structurées rejoint ici la question du **transport**, traitée au ch. 8. Un
serveur MCP exposant une base offre à l'agent un **contrat d'outil stable** — interroger, lister les
schémas, décrire une table — qui découple l'agent de la mécanique de connexion et
d'authentification.

Cette couche est **complémentaire de la récupération documentaire, non concurrente** : l'une récupère
du texte non structuré pertinent, l'autre donne accès à la **donnée structurée vivante**. Un agent
d'entreprise combine couramment les deux — récupérer une note de politique, l'agréger à des chiffres
tirés d'un entrepôt.

> **Mise en œuvre.** Exposer un entrepôt par un serveur MCP plutôt que par une connexion codée en
> dur applique le découplage au niveau des données : **le contrat d'outil survit
> aux changements de moteur sous-jacent**, et la gouvernance d'accès se centralise à la passerelle au
> lieu de se disperser dans chaque agent. La génération de requêtes agentique réclame en contrepartie
> des **garde-fous d'exécution** — requêtes en lecture seule, périmètre de tables limité, plafonds de
> lignes et de temps — pour éviter qu'une boucle de correction n'engendre des requêtes coûteuses ou
> destructrices sur une base de production.

### 5.4.2 Gouvernance d'accès, ancrage et évaluation

Dès lors qu'un agent récupère et restitue de l'information d'entreprise, **trois exigences se
superposent** : que l'accès respecte les droits de l'utilisateur, que la réponse soit ancrée et
traçable, et que le tout soit mesurable.

**La gouvernance d'accès** impose que le contrôle des permissions — par rôles (RBAC) ou par attributs
(ABAC) — s'applique **au niveau du document, voire du fragment**, et non seulement à l'interface de
l'agent.

⚠ **Le mode d'échec ici est silencieux, et c'est ce qui le rend grave.** Un index vectoriel qui
mélange sans cloisonnement des documents soumis à des habilitations distinctes **contourne le modèle
d'autorisation sans jamais lever d'erreur**. La récupération doit donc filtrer les candidats selon
l'identité de l'**utilisateur effectif** avant la génération — faute de quoi **l'agent devient un
canal de fuite de contrôle d'accès**. C'est la propagation d'identité du ch. 3 § 3.2.3 appliquée aux
données, et le ch. 17 en montrera la version multi-saut. Ce chapitre pose le principe ; son
application à l'échelle du parc d'entreprise a son domicile au **ch. 24 § 24.4.2**, qui n'est pas
refait ici.

**L'ancrage.** Réduire les hallucinations exige davantage que de bons passages : il faut une
**attribution vérifiable** et un **comportement d'abstention**. La citation **affirmation par
affirmation** — rattacher chaque énoncé de la réponse au fragment source précis qui l'étaye — rend le
résultat auditable ; l'abstention assumée — répondre « information indisponible » plutôt que combler
le vide — est préférable à une réponse plausible mais non étayée. Ce sont les deux mêmes pratiques
qu'au § 5.2.2, et leur récurrence n'est pas fortuite : mémoire et récupération échouent de la même
manière.

**L'évaluation** doit porter sur **deux axes distincts**, et les découpler est indispensable :

| Axe | Ce qu'on mesure | Instruments |
| --- | --- | --- |
| **Récupération** | le rappel — les bons passages ont-ils été trouvés ? | métriques classiques de recherche d'information, dont le *Recall@K* |
| **Génération augmentée** | fidélité au contexte, pertinence de la réponse et du contexte | RAGAS (Es et coll., 2023), sans référence humaine ; ARES (Saad-Falcon et coll., 2024), juges légers entraînés ; le banc CRAG (Yang et coll., 2024) pour les systèmes complets |

: Tableau 5.2 — Les deux axes d'évaluation d'un système de récupération, à mesurer séparément.

⚠ **Une réponse fausse peut tenir à un bon générateur nourri de mauvais passages, ou l'inverse** —
et **seul le diagnostic séparé oriente la correction**. Mesurer la seule qualité finale dit qu'il y a
un problème, jamais où il est.

⚠ **Point de jonction avec le ch. 19, marqué et non franchi.** La récupération agentique n'est pas
qu'un mécanisme d'ancrage : elle est aussi un **vecteur d'attaque**. En récupérant du contenu non
fiable — courriel, page web, document partagé — et en l'injectant dans le flux de raisonnement d'un
agent qui dispose par ailleurs de données privées et d'un canal de sortie, elle réunit les conditions
d'une exfiltration. **Tout passage récupéré doit être traité comme du contenu non fiable susceptible
de porter une injection d'invite indirecte.**

Conformément au fil de la sécurité posé au ch. 4 § 4.0.1, **ce risque ne se résout pas au niveau du
modèle** : il appelle une défense en profondeur — étiquetage de provenance des fragments,
cloisonnement des privilèges, contrôle du canal de sortie. Le modèle de menace, la triade de
conditions et les incidents documentés sont **au ch. 19** ; la défense architecturale, **au ch. 6
§ 6.5**. Ce chapitre s'arrête ici, et c'est l'arbitrage du plan.

---

## § 5.5 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle consigne l'écart de
gouvernance sous lequel ce chapitre a été rédigé, conformément à la règle d'escalade du
[PRD](../PRD/PRD.md) Annexe A : *un rédacteur ne corrige jamais le TOC, ce PRD ni le Conspectus — il
remonte.*

**Ce qui est enfreint** — les portes **G-1**, **G-2** et **G-3** sont ouvertes. Rédaction sur
instruction d'auteur du 27 juillet 2026. Conséquences :

1. **Aucun énoncé n'est central au sens de CA-IV-01** — régime **[C]** hérité du Vol. I.
2. **Les décomptes sont publiables depuis le 27 juillet 2026** — G-2 franchie, `PRD/decompte.sh` versionnée et éprouvée sur les trois corpus entiers.
3. **Les renvois « ch. N » étaient des renvois de plan, non de texte**, les ch. 6, 7, 8, 17, 19 et 39
   n'étant pas rédigés à la date de rédaction. ⚠ **Ils le sont depuis** — les cinquante chapitres
   existent en brouillon hors portes —, et la relecture du 28 juillet 2026 a re-vérifié **chaque
   renvoi de section contre le plan** (TOC v0.30) : ch. 2 § 2.3.5 et § 2.4.2, ch. 3 § 3.2.3 et
   § 3.4.5, ch. 4 § 4.2.1, § 4.2.2, § 4.3.4 et § 4.3.5, ch. 6 § 6.1 et § 6.5, ch. 39 — tous résolvent.
   Le **ch. 4 § 4.0.1** est un apparat de sa pièce, hors table détaillée : il est vérifié **contre la
   pièce**, où le fil de la sécurité est effectivement posé. Le **ch. 24 § 24.4.2** est vérifié contre
   sa pièce et contre `PRD/check-sieges.py`, qui l'enregistre comme domicile. ⚠ **La re-vérification
   contre le TEXTE reste due** pour les pièces que la passe de relecture modifie en parallèle : un
   renvoi qui résout contre le plan ne prouve pas qu'il résout contre la prose.

**Remontée ouverte par ce chapitre**, à l'instance d'arbitrage — **D-6, non désignée à la rédaction ;
prise le 27 juillet 2026 : l'auteur, sans délégation** :

- **R-IV-07 — non bloquante, à échéance G-1.** Deux fonctions produit citées au § 5.1.3 et § 5.1.4
  sont **en bêta** à la date d'arrêt des sources, avec une version d'interface datée. Le chapitre les
  nomme comme telles et ne les présente jamais comme disponibles en général — mais leur statut est
  précisément ce qui peut changer entre le gel de la source et le gel de la somme, dans les deux
  sens : passage en disponibilité générale, ou retrait. **À re-vérifier une à une en G-1**, et non à
  reconduire de mémoire.

**Une observation de méthode, sans remontée.** Ce chapitre porte le **premier fait négatif vérifié**
du Livre I (§ 5.0) : l'absence de matière d'empoisonnement dans les §2.6-2.7 du Vol. I est établie
par un balayage documenté que le TOC porte sous l'entrée du chapitre, et non simplement non trouvée.
La distinction entre les trois degrés de R-14 n'est donc pas ici une précaution rhétorique : elle
sépare deux énoncés de statut réellement différent, et le chapitre en fait usage aux deux niveaux
(§ 5.0 pour le degré 1, § 5.2.2 pour le degré 3).

**Ce qui n'est pas enfreint.** La structure suit la table détaillée du TOC section par section
(§ 5.1 à § 5.4) ; le § 5.0 est un apparat de cadrage, non une section du plan, et il est déclaré tel.
La table de couverture est respectée, y compris la sortie de périmètre du §2.10.2.2 vers le ch. 19 :
**aucune sous-section d'empoisonnement n'est écrite ici**, le § 5.4.2 se bornant à marquer le point
de jonction. Les deux séries de garde-fous sont balayées et déclarées ; les deux occurrences de R-14
du Vol. III sont marquées avec leur **degré** ; les fonctions en bêta portent leur réserve d'usage.

**Une déviation d'intitulé, déclarée au titre de la décision 8 du TOC** (et de la règle *(c)* de sa
décision 15, « les intitulés de section suivent le plan ; une déviation fondée se déclare »). Le plan
intitule la section **« Du LLM sans état à l'agent persistant : mémoire et ingénierie du contexte »** ;
la pièce écrit **« Du modèle sans état… »**. Motif : le registre du corpus n'admet un terme technique
anglais qu'entre parenthèses à sa première occurrence, et le sigle nu en tête de section ne s'y prête
pas. **C'est la seule déviation d'intitulé de la pièce** : la table détaillée du TOC porte
**quatorze** intitulés — quatre sections et dix sous-sections —, et les **treize** autres sont repris
mot à mot, le § 5.2.1 (« et pile de récupération », tombé) et le § 5.3 (virgules pour traits d'union)
ayant été **réalignés** à la relecture du 28 juillet 2026. Remontée ci-dessous.

---

### Clôture des remontées — 27 juillet 2026

⚠ **Cette sous-section est hors plan comme la note qui la porte, et se retire avec elle.** Elle
enregistre l'issue des remontées ouvertes par cette pièce. *Une remontée ne se clôt pas là où elle
s'ouvre : elle se solde là où elle fait foi* — au [PRD](../PRD/PRD.md) pour une décision d'auteur, au
[TOC](../PRD/TOC.md) pour un réalignement de plan, à l'appareil pour une dette d'outillage.

- **R-IV-07 — close par le franchissement de G-1 (volet Livre I), et c'est la seule remontée du Livre
  dont la re-datation ait changé un fait.** Les deux fonctions produit ont été reprises à la source
  primaire le 27 juillet 2026 (registre du gel, faits 9 et 10) : l'**édition de contexte** (§ 5.1.3)
  est **toujours en bêta**, en-tête d'activation daté inchangé ; l'**outil de mémoire** (§ 5.1.4) est
  passé en **disponibilité générale**. Le § 5.1.4, l'en-tête et le champ des garde-fous sont corrigés.
  ⚠ **L'écart va dans le sens favorable** : une fonction qui passe en disponibilité générale rendait
  la pièce **trop prudente**, non fausse — elle ne l'avait jamais présentée comme disponible. *C'est
  le mode de péremption le moins coûteux, et le seul que la re-datation du Livre I ait rencontré.*

⚠ **Ce que la clôture ne change pas** *(état au 27 juillet 2026 ; la porte a bougé le lendemain —
voir la passe de relecture ci-dessous)*. La porte **G-3** demeure ouverte : le socle consolidé compte
**zéro entrée**, l'Annexe B n'existe pas, et **aucun énoncé de cette pièce n'est central au sens de
CA-IV-01**. Cette pièce reste un **brouillon non publiable**. *Zéro remontée ouverte ne veut pas dire
pièce recevable — cela veut dire qu'aucune question n'attend plus de réponse qui ne soit déjà
tranchée.*

---

### Passe de relecture — 28 juillet 2026

⚠ **Hors plan comme la note qui la porte, et se retire avec elle.** Cette sous-section enregistre ce
qu'une passe de relecture a changé dans la pièce, et ce qu'elle n'a pas pu changer.

**Ce qui a bougé hors de la pièce, et qui la conditionne.** La porte **G-3 est franchie** depuis le
28 juillet 2026 (PRD v0.14, TOC v0.30) : l'Annexe B existe, sous la forme du
[socle consolidé](../PRD/socle-consolide.md), **159 entrées `S-001` à `S-159`**.

⚠ **Ce socle ne couvre pas la matière de ce chapitre, et le constat est un fait négatif vérifié.**
Balayage exhaustif de la colonne *Provenance* des 159 entrées : **aucune ne procède des §2.6-2.7 du
Vol. I *Monographie***, périmètre de fusion de ce chapitre. Les **dix-sept** entrées héritées du
Vol. I (`S-143` à `S-159`) proviennent de ses §7.x, §3.10.x, §2.10.2.x, §5.0.2-§5.1.1, de son
Annexe B et de sa *Synthèse* — jamais de §2.6 ni de §2.7. C'est un **fait négatif vérifié** au sens de
R-14 du Vol. III, domaine déclaré, et non une absence de documentation. **Trois conséquences.**
*(1)* Les énoncés de cette pièce continuent de résoudre contre le **Vol. I *Monographie* §2.6-2.7**,
en régime **[C]** (PRD §7.1), et **aucun n'est central au sens de CA-IV-01**. *(2)* Les seules entrées
consolidées qui touchent la mémoire et la récupération portent sur leur **empoisonnement** — ainsi
`S-069` et `S-152` —, matière que le plan affecte au **ch. 19** et que ce chapitre exclut au § 5.0 :
*la couverture du socle et la sortie de périmètre du plan concordent.* *(3)* La pièce reste un
**brouillon non publiable** : **CA-IV-11 et CA-IV-13 demeurent insatisfaites**, D-6 ne fournissant pas
de relecteur distinct du rédacteur. ⚠ *Une porte franchie n'est pas une pièce recevable, et un socle
qui ne documente pas une matière ne la rend pas centrale.*

**Ce que la relecture a corrigé dans la pièce.**

1. **Décision 15 du TOC — l'attribution ne s'anonymise jamais.** La pièce désignait ses instruments et
   ses attributeurs par périphrase : « un recensement […] en dénombre sept », « une position
   concurrente », « une formulation d'usage », « un troisième [banc] », « des bancs dédiés », « une
   première lignée ». Les **auteurs et les dates sont rétablis** aux § 5.1.1 à § 5.4.2, ainsi que les
   noms des instruments repris — bancs, architectures de mémoire, mécanismes auto-correcteurs, pile de
   récupération, cadres d'évaluation —, et le **Model Context Protocol** est nommé là où la pièce
   écrivait « un serveur d'accès normalisé ». ⚠ **La parade de péremption est maintenue là où la
   décision la maintient** — règle *(a)* : les deux fonctions produit gardent leur dénomination
   générique et **leur numéro de version n'est pas cité**, seul leur **éditeur** étant nommé au titre
   de l'attribution.
2. **Décision 16 — les cardinaux du corps re-mesurés**, non les seuls cardinaux d'en-tête : « trois
   objets », « quatre verbes », « trois plans », « trois opérations », « deux pratiques », « trois
   étapes », « sept points de défaillance », « trois exigences », « deux axes » — tous vérifiés par
   balayage contre ce qu'ils annoncent. Le cardinal des intitulés de section (quatorze, treize repris)
   est neuf et mesuré.
3. **Décision 17 — la thèse est re-citée par copie depuis le TOC v0.30**, et elle est **identique** à
   la forme citée depuis la v0.23 : le plan n'a pas amendé cette entrée. Le bloc de tête porte
   désormais la version courante.
4. **Décision 7 — deux renvois complétés** : « au sens de R-14 » (§ 5.2.2) devenu « R-14 du Vol. III »,
   et « les §2.6-2.7 du Vol. I » (§ 5.0) devenu « du Vol. I *Monographie* ».
5. **Régime de preuve — deux énoncés bornés.** Le § 5.4.1 affirmait que le constat du banc était
   « l'un des rares endroits du Livre I où l'agentivité se justifie par une mesure » : **jugement
   d'auteur sur un domaine que personne n'a dénombré**, remplacé par l'attribution du constat à ses
   auteurs. Le § 5.2.1 affirmait qu'une architecture « répond le plus directement au problème que les
   autres contournent » : **comparaison non étayée**, remplacée par ce que les descriptions portent, et
   par ce que leur silence n'établit pas.

**Remontées ouvertes par cette passe** — ⚠ **sans identifiant alloué, et le motif est opposable** : la
règle *(1)* du PRD §13 veut qu'une plage neuve se prenne **au-dessus du maximum constaté sur pièces**,
jamais au-dessus du maximum supposé ; or **cinquante relectures courent en parallèle** sur le même
appareil, et le maximum constaté à cet instant est faux à l'instant suivant. *C'est exactement le
défaut que R-IV-75 a payé.* L'allocation revient à la passe d'arbitrage.

- **Intitulé du § 5.1 — non bloquante.** Le plan écrit « Du **LLM** sans état », la pièce « Du
  **modèle** sans état ». Déviation fondée et déclarée (décision 8) ; **au plan de trancher** s'il
  reprend la forme française ou s'il maintient le sigle.
- **Lacune du socle consolidé pour les §2.6-2.7 du Vol. I — non bloquante, à échéance G-4.** La
  totalité de la matière de ce chapitre est hors socle. Ce n'est **pas une contradiction** entre
  volumes mais une **lacune de couverture**, du genre que l'Annexe C du TOC oblige la collation de fond
  à balayer. Elle se **signale**, elle ne se comble pas par une source de moindre qualité.
- **Cardinal de Livre au champ *Volumétrie* — non bloquante.** Le total du Livre I qui y figurait
  (64 750 mots) datait de la rédaction et **n'est pas re-mesurable pendant que les onze pièces du
  Livre sont en relecture simultanée**. Il est retiré au profit du seul réel de la pièce, mesuré.
  **Le total du Livre se re-mesure au terme de la passe**, par `PRD/decompte.sh`, sur le corpus que le
  commit produit.

---

### Contre-vérification de la relecture — 28 juillet 2026

⚠ **Hors plan comme la note qui la porte.** Une seconde passe a repris la relecture ci-dessus **en
cherchant à la prendre en défaut**, plutôt qu'à la confirmer : *une attestation de relecture est une
attestation comme une autre — elle se constate sur pièce.* Ce qu'elle a constaté, dans les deux sens.

**Ce que la re-mesure confirme.** Les attributions rétablies au titre de la décision 15 résolvent
**une à une** contre les §2.6-2.7 du Vol. I *Monographie* — auteurs, millésimes, noms d'instruments et
date du 9 décembre 2025 comprises : **aucune source n'a été inventée**. ⚠ **Domaine déclaré sans
cardinal** (décision 16c) : *le balayage a porté sur **toutes** les mentions d'auteur, de millésime et
de nom d'instrument des § 5.1.1 à § 5.4.2, confrontées au texte des §2.6.1 à §2.7.4 de la source ; le
nombre d'« attributions » n'est pas publiable, faute d'une règle qui dise si l'unité est l'instrument
ou l'occurrence.* Le réel de **4 787 mots** que la relecture déclarait est re-mesuré par
`PRD/decompte.sh` et retrouvé **à l'unité près** — *le champ porte aujourd'hui 4 864, les 77 mots
d'écart étant ceux que la présente passe a ajoutés.* Les **quatorze intitulés** de la table détaillée
sont recomptés (quatre sections, dix sous-sections) et les **treize** repris le sont mot à mot. La
thèse est identique à celle de l'entrée du chapitre au TOC v0.30. Les cardinaux du corps, les
**trois** occurrences de « MCP » et les **deux** de « R-14 » sont recomptés au marqueur littéral
(décision 16). **Aucune régression n'a été trouvée dans le diff de la relecture.**

**Ce que la re-mesure contredit — une correction fausse, rectifiée.** L'énumération des provenances du
socle portait « **§1.0.2** » parmi les sections du Vol. I dont procèdent les dix-sept entrées héritées.
⚠ **Aucune cellule *Provenance* de `S-143` à `S-159` ne porte cette section** : elle n'apparaît qu'à
l'**intérieur** de l'énoncé de `S-153`, et sous la forme §1.0.2.1. La mention est retirée aux **deux
sites** (en-tête, § 5.5). *Le fait négatif vérifié qu'elle accompagnait n'est pas touché — il porte sur
l'absence de §2.6 et de §2.7, et cette absence est confirmée par le même balayage.* ⚠ **La leçon est de
méthode** : *un balayage qui déclare son domaine doit énumérer ce qu'il a vu, non ce qu'il croit avoir
vu — une provenance de trop suffit à rendre l'attestation invérifiable.*

**Ce que la relecture avait manqué — deux constructions d'auteur non marquées.** La pièce ne portait
**aucune** occurrence de « Lecture de l'auteur », alors que deux de ses énoncés sont des inférences que
la source ne fait pas : la conciliation des deux positions sur l'isolation (§ 5.1.2) et la
caractérisation de l'hallucination mémorielle comme *persistante* et *auto-confirmante* (§ 5.2.2).
**Les deux portent désormais leur marqueur** et disent ce que le socle établit et n'établit pas
(**CA-IV-07**). ⚠ *La passe qui a nommé les attributeurs a rendu ces deux inférences plus visibles sans
les marquer : nommer une source ne dispense pas de marquer ce qu'on lui ajoute.* ⚠ **Le cardinal des
pièces du Livre qui portent le marqueur n'est pas publié** : il n'est pas re-mesurable pendant que les
onze sont en relecture simultanée (décision 16b).

⚠ **Ce que la contre-vérification ne change pas.** Elle **ne relève d'aucune porte** et **ne satisfait
ni CA-IV-11 ni CA-IV-13** : D-6 désigne l'auteur comme instance unique, et *deux passes du même
appareil ne font pas un relecteur distinct du rédacteur*. La pièce demeure un **brouillon non
publiable**.
