# Chapitre 44 — La formalisation ArchiMate

*Livre IV — Appliquer, exploiter, produire et composer : AgentMesh, AgentOps, fabrique d'agents et
synthèse architecturale.
Quatrième mouvement — composer (ch. 42-46). Troisième chapitre du mouvement : **il traduit dans un
formalisme ce que le ch. 43 a rangé en couches, et rien d'autre.***

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — rédigé sur instruction d'auteur du 27 juillet 2026, **avant** les portes **G-3**, **G-4** et **G-5**, et hors de l'ordre de rédaction du PRD §6. ⚠ **ET AVANT LE PRÉALABLE QUE LE PLAN NOMME POUR CE CHAPITRE PRÉCISÉMENT** : la **re-vérification du mécanisme d'extension tel que la version de référence le porte** est déclarée par le TOC **préalable au registre des stéréotypes (§ 44.1.9), non note de transition** — *elle n'a pas eu lieu*. Le PRD §12 la nomme au jalon J-IV-5. ⚠ **R-IV-40 et R-IV-41, ouvertes au ch. 37, valent pour tout le Livre** |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** ([`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Volet résiduel de G-1 non instruit, et ce chapitre est celui du Livre où l'omission pèse le plus** : *son ancrage de version est un document de norme d'avril 2026, dont la liste définitive des éléments retirés ou renommés est déclarée **ressource vivante à recouper au gel** — et le recoupement n'a pas été fait.* Gel de source : **juin 2026** (Vol. I). *Il n'est pas celui de la somme.* |
| **Socle mobilisé** | ⚠ **Aucune entrée du socle consolidé** (G-3 ouverte), **et aucune entrée F-xx d'aucun volume** : ce chapitre consomme le **Vol. I *Monographie* ch. 6**, qui entre **en [C]** — *sa vérification porte sur ses références, non sur le contenu de ses affirmations* —, plus **Vol. III *Monographie* §27.2** au seul titre de la matière à formaliser. ⚠ **Conséquence, et elle est plus large ici qu'ailleurs** : **tout ce chapitre est en [C]**, *aucun énoncé n'est central au sens de CA-IV-01*, et **l'élévation en [B] passerait par la lecture des documents de norme que le Vol. I cite** — travail de **G-1**, non de ce chapitre. ⚠ **Une entrée de socle est mobilisée par exception**, au § 44.6 : le **Vol. II F-09** (E-23), pour la seule modalité de sa formulation |
| **Garde-fous balayés** | **Les deux séries, intégralement, y compris les zéros.** Vol. III — **R-14 (trois degrés d'absence) : huit occurrences**, § 44.0 (deux), § 44.1 (trois), § 44.5, § 44.7, § 44.9 ; **R-09 (statut d'un document dit à chaque mention) : six occurrences**, § 44.0 (trois), § 44.1, § 44.7 (deux) ; **R-02 : deux occurrences**, § 44.1 — *un mécanisme d'extension se qualifie par ce que la spécification rend officiel* ; **R-13 (échelle d'autonomie jamais nue) : une occurrence**, § 44.1.7, **renvoyée au siège du ch. 43 § 43.5** ; **R-01 : une occurrence**, § 44.1.6. **R-03 à R-08, R-10 à R-12 : zéro occurrence.** Vol. II — **réserve F-09 (« attendu par E-23 », jamais « exigé ») : trois occurrences**, § 44.6 ; **réserve F-01 (« cadre d'autorisation », jamais « sécurisé ») : une occurrence**, § 44.1.3 ; **R-8 (sigle jamais nu) : deux occurrences**, § 44.1.6, **renvoyées au siège du ch. 7 § 7.5** ; **R-1 à R-7 : zéro occurrence** ; **métriques auto-déclarées : deux occurrences**, § 44.7 et § 44.9, **attribuées à leur éditeur nommé**. ⚠ **Garde-fou PROPRE au chapitre, hérité de sa source et plus nécessaire ici qu'à elle** : *si l'on retire le mot « ArchiMate » et que la phrase tient encore comme un exposé des chapitres amont, c'est une redondance à renvoyer* — **au Vol. I ce chapitre en suivait cinq ; ici il en suit quarante-trois** |
| **Volumétrie cible** | ≈ **8 500 mots** de corps (§ 44.0 à la synthèse), **cible dérivée** de l'enveloppe du Livre (**69 000 mots**, TOC v0.25) au prorata des dix sections et du volume de source consommé — **la deuxième plus haute du Livre**, ce chapitre absorbant un chapitre entier du Vol. I. ☑ **Décompte publiable depuis G-2** ; **réel reporté au [`README.md`](README.md)**. ⚠ **D-4 s'applique** |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.25, entrée du chapitre 44 — le verrou est méthodologique et se nomme d'emblée)* — **ArchiMate n'a aucun élément natif** pour l'agent autonome, l'appel d'outil MCP, l'interaction A2A, l'identité non humaine ou le plan de contrôle ; la seule extension défendable est le mécanisme officiel **Specialization + stéréotype `<<…>>` + Profiles**, sur le modèle du *Risk & Security Overlay*. Ce que le chapitre apporte est une **traduction structurelle**, jamais une reprise du fond conceptuel des livres amont.

☑ **La thèse citée résiste à la collation contre le texte rédigé de sa source — décision 14 du TOC,
appliquée avant la rédaction, et c'est la première du Livre IV dans ce cas.** Le Vol. I écrit que
*« ni ArchiMate 3.2 ni ArchiMate 4 n'introduisent de métaclasse dédiée à l'intelligence artificielle
ou aux agents autonomes »*, et que *« le seul mécanisme d'extension défendable est celui que la
spécification rend officiel : la spécialisation, assortie d'un stéréotype, complétée par les
Profiles »*. **Les deux membres de la thèse sont portés mot pour mot.** ⚠ **Un point mérite néanmoins
d'être borné** : *le Vol. I ne prétend pas avoir balayé les extensions communautaires* — il constate
qu'**aucune solution canonique n'existe** et que *la pratique s'est longtemps appuyée sur des
conventions informelles*. **« Seule extension défendable » est donc un jugement de conformité au
métamodèle, non un fait négatif de corpus** — absence de documentation, non fait négatif vérifié
(R-14 du Vol. III, degré 3).

---

## § 44.0 — Primer ArchiMate et convention de version

⚠ **Le contrat de lecture de la source est refondu en apparat, et il n'est pas reconduit comme
section.** *Ce que le Vol. I devait déclarer à ses cinq chapitres amont, la somme le déclare à
quarante-trois*, et **la forme change** : le garde-fou de non-redondance est porté à l'en-tête, où il
s'applique à chaque phrase, plutôt qu'à une sous-section qu'on lit une fois.

### 44.0.1 Pourquoi un formalisme, et pourquoi celui-là

⚠ **Ce paragraphe est en [C], comme tout le chapitre, et il énonce une thèse d'un volume antérieur, à
attribuer.** Le Vol. I retient ce langage pour une raison qu'il déclare : *c'est un langage de
description d'architecture d'entreprise **normalisé et gouverné par un organisme**, ce qui rend une
convention d'extension **traçable et opposable** là où une notation propriétaire ne le serait pas.*
**Ce que le socle établit** : rien — le socle consolidé compte zéro entrée, et **aucun volume ne verse
de fait sur ce langage**. **Ce qu'il n'établit pas** : que ce langage soit le meilleur, ni qu'un autre
formalisme échouerait.

⚠ **Une distinction est reprise parce que sa confusion est un anti-patron nommé** (§ 44.8) :
**langage**, **méthode**, **cadre**, **outil** et **modèle de référence** sont cinq objets distincts.
*Le langage décrit ; la méthode conduit ; le cadre range ; l'outil édite ; le modèle de référence
propose un contenu.* **Confondre le premier et le second est la faute la plus courante**, et la somme
ne l'écrit qu'une fois.

### 44.0.2 Le cadre, les domaines, les aspects — version de référence

**Ancrage de version, et il commande tout le chapitre** : la version de référence est **ArchiMate 4**
(document normatif d'avril 2026) ; **les équivalences avec la version 3.2 (octobre 2022) figurent en
notes de transition**. ⚠ **Statut dit à chaque mention** (R-09 du Vol. III) : *ce sont des documents
de norme publiés par leur organisme, non des brouillons* — et **la liste définitive des éléments
retirés ou renommés est une ressource vivante à recouper au gel**, ⚠ **recoupement qui n'a pas eu
lieu** (§ 44.0.4).

**Le changement de métamodèle est de fond, et il est confirmé par l'éditeur de la norme.** La version
de référence **substitue aux *couches* un découpage en domaines pairs**, sans hiérarchie implicite
entre eux ; **sept domaines** sont retenus — **Common** (nouveau, transverse), **Business**,
**Application**, **Technology** (qui **absorbe l'ancienne couche Physical**), **Motivation**,
**Strategy**, **Implementation & Migration**. Le noyau réunit les quatre premiers ; le langage complet
y ajoute les trois derniers.

⚠ **Deux mises en garde s'imposent pour la suite, et la première est celle qu'on lit à l'envers.**
*Un* : **il n'existe ni domaine fusionnant Application et Technology, ni domaine Physical distinct** —
*en version de référence, Application et Technology demeurent deux domaines **séparés**, et Physical
est simplement absorbé dans Technology.* **La distinction entre la logique de l'agent et son substrat
d'exécution reste donc valide, mais devient une convention d'altitude plutôt qu'une frontière de
couche.** *Deux* : **les comportements sont unifiés** — *quatre éléments génériques exacts,
**Service**, **Process**, **Function**, **Event**, complétés par les Collaboration et Role génériques,
remplacent les variantes auparavant déclinées par couche.* **Les quatre aspects du langage sont
conservés** : structure active, comportement, structure passive, motivation.

### 44.0.3 Éléments et relations : les libellés exacts, parce que la suite les mobilise sans les redéfinir

**La version de référence réduit le décompte d'éléments d'environ soixante à environ quarante-deux**,
principalement par l'unification des comportements et la suppression de variantes par couche. ⚠ **Le
cardinal est celui que le Vol. I rapporte, en [C]** ; *la somme ne l'a pas re-mesuré sur le document
de norme, et la relève du plan le confirme dans les mêmes termes — **environ 30 % de réduction, de
plus de soixante à une quarantaine**.*

**Les onze relations sont inchangées par rapport aux versions 3.x** : **Composition**,
**Aggregation**, **Assignment**, **Realization**, **Serving**, **Access**, **Influence**,
**Triggering**, **Flow**, **Specialization**, **Association**. ⚠ **La Junction est un connecteur, non
une douzième relation.** ⚠ **Un libellé appelle une vigilance particulière** : **Serving** a remplacé
l'ancien « Used by » **dès les versions 3.x**, et *ce dernier terme ne s'emploie jamais*.

⚠ **Quatre relations portent l'essentiel du sens dans les patrons du § 44.1, et leurs nuances
conditionnent la défendabilité de chacun** : **Serving** — *un élément en sert un autre durablement* ;
**Realization** — *un élément concrétise un comportement ou un service plus abstrait* ; **Assignment**
— *une structure active porte un comportement ou une responsabilité* ; **Access** — *un comportement
lit ou écrit une structure passive*.

### 44.0.4 Convention de version — et le préalable qui n'a pas été tenu

⚠ **C'est le point le plus important de cette section, et il conditionne le § 44.1.9.** Le plan
déclare, en toutes lettres : *la re-vérification du mécanisme **Specialization + stéréotype +
Profiles** tel que le document normatif de référence le porte est **un préalable au registre des
stéréotypes, non une note de transition**.*

☐ **Ce préalable n'a pas été tenu.** *Aucune lecture du document de norme n'a été conduite par la
somme* ; **tout ce que ce chapitre écrit du mécanisme d'extension vient du Vol. I, en [C]**, et
**l'ampleur de la refonte est précisément ce qui rend l'omission coûteuse** : *une refonte de
métamodèle qui retire environ un tiers des éléments et remplace les couches par des domaines est la
plus profonde depuis la création du langage — et le mécanisme d'extension est l'objet même que la
somme lui emprunte.*

⚠ **Deux conséquences sont tirées ici plutôt que laissées à deviner.** *Un* : **le registre des
stéréotypes du § 44.1.9 est reproduit comme registre du Vol. I, en [C], et non comme registre
conforme à la version de référence** — *la différence n'est pas de politesse : un registre présenté
comme conforme à un document qu'on n'a pas lu est une attestation, et CA-IV-14 la proscrit.* *Deux* :
**les substitutions d'éléments retirés que le registre porte** — *pour l'élément de contrat, pour
l'écart de maturité, pour l'indicateur* — **sont des propositions du Vol. I, présentées par lui comme
des conventions gouvernées et non comme des règles natives**, ⚠ *et il déclare lui-même que le devenir
exact de l'un d'eux **reste à confirmer** sur le document normatif.*

⚠ **Une seconde réserve datée pèse sur tout le mouvement, et elle est d'outillage.** À la mi-2026, **la
quasi-totalité des ateliers d'architecture d'entreprise n'exporte et n'importe encore que la version
3.2 nativement**, ⚠ **ce qui rend le blueprint du ch. 45 non échangeable en version de référence dans
la plupart d'entre eux**. *Le chapitre écrit donc en version de référence **avec note d'équivalence
3.2 par patron**, et la note n'est pas un ornement : c'est la condition pour que le modèle soit
ouvrable.*

## § 44.1 — Le problème de modélisation : patrons pour concepts agentiques

### 44.1.1 Le verrou méthodologique : aucun élément natif, le recours à la spécialisation

⚠ **Le verrou commande toute la suite et se pose sans ambiguïté** : *ni la version 3.2, ni la version
de référence n'introduisent de métaclasse dédiée à l'intelligence artificielle ou aux agents
autonomes.* **La refonte du métamodèle vise la simplification du langage, non l'ajout d'une prise en
charge agentique.**

**Le seul mécanisme d'extension défendable est celui que la spécification rend officiel** :
**Specialization**, assortie d'un **stéréotype `<<…>>`**, complétée par les **Profiles** (attributs
typés). ⚠ **Un mécanisme se qualifie par ce que la spécification rend officiel, jamais par ce qu'une
pratique en fait** (R-02 du Vol. III, transposé). ⚠ **Ce levier n'est pas une trouvaille** : *il
reproduit la démarche d'un overlay de risque et de sécurité normalisé par le même organisme, qui
superpose des stéréotypes à des éléments existants **sans inventer de concept**.*

⚠ **La pratique communautaire confirme l'absence de solution canonique**, et le Vol. I le déclare : *la
modélisation d'agents logiciels s'est longtemps appuyée sur des **conventions informelles**.* ⚠ **Le
socle ne documente aucun balayage des extensions communautaires** : absence de documentation, non fait
négatif vérifié (degré 3). *« Seule extension défendable » est un jugement de conformité au
métamodèle, non un constat d'exhaustivité.*

### 44.1.2 Patron « agent » : Application Component, Role, Collaboration

**Le choix de la métaclasse dépend de deux critères orthogonaux : l'altitude — technique ou métier —
et la responsabilité — brique exécutable ou fonction imputable.** Trois options se présentent : *(A)*
brique technique exécutant un modèle et une logique d'outillage → **Application Component** ; *(B)*
fonction métier déléguée porteuse d'une responsabilité → **Role** — *élément générique en version de
référence, héritier de l'ancien « Business Role »* — assigné à un **Business Actor** responsable ;
*(C)* essaim d'agents coopérants → **Application Collaboration**.

**Le patron canonique combine ces facettes** : un **Application Component** stéréotypé `<<Agent>>`,
auquel est **assigné un Role**, et qui **réalise** une **Application Process** stéréotypée
`<<reasoning loop>>` matérialisant la boucle de raisonnement.

⚠ **Le choix de la métaclasse comportementale est tranché une fois et vaut pour tout le chapitre** :
*la boucle plan-agir-observer est un **Process**, parce qu'elle est un enchaînement **ordonné**
d'étapes ; la **Function** est réservée à l'appel d'outil atomique, comportement **non
séquentiel**.*

⚠ **Le compromis porte sur l'imputabilité, et il est le seul enjeu réel de ce patron** : *remonter
l'agent dans le domaine Business **engage une responsabilité métier ou réglementaire** ; le maintenir
dans Application **traduit un statut d'outil sous supervision**.* **Ce n'est pas un choix de
notation ; c'est un choix de qualification** — et **le ch. 43 § 43.2.2 a établi que la qualification
précède l'architecture**.

### 44.1.3 Patron « appel d'outil » : Application Service, Interface, Serving

**Siège de la modélisation de la relation agent-outil ; le protocole n'est pas réexpliqué** — *son
anatomie est au ch. 8.*

Le serveur exposant des capacités outillées est un **Application Component** stéréotypé
`<<MCP Server>>`. **Chaque capacité offerte est une Application Service**, réalisée par ce composant
via **Realization**, et rendue accessible par une **Application Interface**. L'agent consommateur est
relié à cette service par **Serving** — ⚠ **jamais par « Used by »**. La ressource lue est un **Data
Object**, accédé par **Access**.

⚠ **L'anti-confusion à tenir est celle de Serving et de Realization** : *Realization relie le composant
à la capacité qu'il rend effective — le serveur **réalise** le service ; Serving relie le service au
consommateur qu'il dessert — le service **dessert** l'agent.*

⚠ **La granularité recommandée n'est pas un détail** : *une **Application Service par capacité
outillée**, et non un service global indifférencié* — **cette décomposition expose la surface réelle de
délégation et donne un point d'accroche aux contrôles**. *Sans elle, la borne de privilège que le
Livre II exige n'a nulle part où s'attacher.*

⚠ **Le protocole porte un cadre d'autorisation, jamais un protocole « sécurisé »** (réserve F-01 du
Vol. II ; siège **ch. 8**) : *ce que le patron modélise est une surface d'appel, non une garantie.*

### 44.1.4 Patron « interaction agent-agent » : Collaboration, Flow, Triggering

**Siège de la modélisation de la relation agent-agent.** L'échange se modélise par **Flow** pour un
transfert d'information, par **Triggering** pour un déclenchement de comportement, ou par les deux
conjointement. Les agents sont des **Application Components** ; une collaboration durable se réifie en
**Application Collaboration** ; le message est un **Data Object**.

⚠ **Un avertissement de version est ici décisif : l'élément Interaction est retiré en version de
référence.** *Là où la version 3.2 offrait une « Application Interaction » pour le comportement
conjoint, la version de référence le modélise par une **Collaboration** associée à un **comportement
générique unifié** dont l'Assignment porte une **multiplicité supérieure ou égale à deux** — deux
structures actives assignées au même comportement.* **C'est l'un des rares endroits où la note
d'équivalence 3.2 n'est pas cosmétique.**

⚠ **La relation Serving est ici soigneusement réservée** : *elle ne s'emploie que lorsqu'un
agent-spécialiste **offre durablement un service** à d'autres, jamais pour un échange ponctuel.* **Le
compromis Flow / Triggering / Serving — transfert, déclenchement, offre durable — est justifié une
seule fois ici et repris par renvoi.**

### 44.1.5 Patron « identité non humaine » : Role, structure active, overlay de sécurité

**Siège canonique de la modélisation de l'identité non humaine ; son cycle de vie et les mécanismes de
délégation ne sont pas redéroulés** — *ils sont au Livre II, ch. 12 et ch. 17.*

L'identité sous laquelle un agent agit est un **Role**, porté par l'**Application Component** qui
incarne l'agent au moyen d'un **Assignment**. Les justificatifs d'authentification — jeton, clé,
certificat — sont un **Data Object** au plan logique, **matérialisé en Artifact** au plan
technologique. **La délégation, lorsqu'un agent agit pour le compte d'un autre principal, se
représente par une chaîne de relations Assignment.** ⚠ **Le propriétaire humain responsable de
l'identité machine est un Business Actor, rattaché par Assignment au Role** — *c'est ce qui restaure
l'imputabilité, et c'est structurellement la réponse à Q-E de la grille du ch. 14.*

⚠ **Le patron assume une dette de modélisation, et il faut la lire pour ce qu'elle est** : *le langage
n'offre **aucune solution native** pour l'identité machine, et **la distinction entre une identité
humaine et une identité non humaine ne tient qu'au stéréotype et à la convention visuelle, non à une
sémantique du langage**.* **Un modèle dont la distinction la plus lourde de conséquences repose sur
une convention d'annotation est un modèle dont la relecture doit vérifier l'annotation.**

⚠ **Les risques propres aux identités non humaines s'expriment dans le domaine Motivation au moyen des
spécialisations de l'overlay de sécurité** : *un classement daté de ces risques s'injecte comme des
paires **risque / contrôle** — le risque devenant un **Assessment**, le contrôle un **Requirement**
réalisé par un service jouant le rôle de point d'application.* **Le contenu de ces risques n'est pas
réexposé** : il est au **ch. 19**.

### 44.1.6 Patron « plan de contrôle d'agents » et la limite de la découverte dynamique

⚠ **Désambiguïsation obligatoire** (R-8 du Vol. II) : *« plan de contrôle d'agents » s'entend au sens
du patron d'architecture*, et **l'encadré des quatre branches siège au ch. 7 § 7.5** — *ce chapitre y
renvoie et ne le reconstruit pas*.

Le plan de contrôle est une **Application Collaboration** stéréotypée `<<Control Plane>>`, réalisant
un ensemble d'**Application Services** de gouvernance — autorisation, journalisation, application des
politiques, supervision — qui **desservent** le parc. **Son ancrage stratégique passe par une
Capability** ; **les politiques qu'il applique s'expriment en Requirements spécialisés**, ⚠ **et non
en Constraints — l'élément Constraint étant retiré en version de référence au profit d'une
Specialization de Requirement**.

⚠ **À ce patron s'attache une limite structurelle dédiée, et c'est la plus instructive du chapitre.**
*La découverte au moment de l'exécution — carte d'agent, registre, nommage — est **par nature
dynamique**, alors que le langage est un langage de **description statique**.* **Le modèle rend la
mécanique de manière approchée** : *un Application Component figurant le registre ou le catalogue, un
Data Object regroupant les cartes.* ⚠ **Mais la relation de découverte effective — le fait qu'un agent
localise dynamiquement un pair à l'exécution — n'est pas représentable nativement** : *le modèle
décrit **les artefacts** de la découverte, non **son occurrence**.*

⚠ **Et le passeport n'y change rien** : *il ne figure dans aucune spécification à date* (R-01 du
Vol. III ; siège **ch. 16**). **Ce que le modèle pourrait porter est l'artefact d'un objet qui
n'existe pas** — *le formalisme n'ajoute aucune existence à ce qu'il représente.*

### 44.1.7 Patron « humain-agent » : point d'arrêt, double regard, autonomie graduée

**Siège de la modélisation du contrôle de finalité.** La coopération humain-agent est une **Business
Collaboration** réalisant, **en version 3.2 une Business Interaction** et, **en version de référence,
un comportement générique unifié** — *l'élément Interaction étant retiré*.

**Le point d'intervention humain se modélise par l'Assignment d'un Role humain à l'étape irréversible
du comportement** : ⚠ ***c'est l'assignation, et non une annotation, qui inscrit structurellement
l'exigence de supervision.***

⚠ **Le contrôle à quatre yeux appelle une construction particulière, justifiée ici une seule fois** :
*le proposeur et l'approbateur sont **deux Roles distincts**, et **il ne doit exister aucune relation
Flow directe du proposeur vers l'approbateur**.* ⚠ **Cette absence délibérée de Flow est la preuve
d'architecture de la non-collusion** : *structurellement, l'information ne transite pas de l'un à
l'autre sans passer par l'objet de travail soumis et le mécanisme de contrôle.* **La convention est
reprise par renvoi partout où elle s'applique, sans être rejustifiée.**

⚠ **Ce que ce patron atteste, et ce qu'il n'atteste pas.** *Le langage atteste **l'intention** de
contrôle — le Role humain est assigné à l'étape irréversible — **mais non son exercice à
l'exécution**.* **C'est l'écart général entre description statique et état d'instance** (§ 44.9), et
**c'est aussi la limite exacte que le ch. 40 § 40.4 rencontre du côté des indicateurs** : *mesurer la
révision n'est pas mesurer le discernement ; modéliser l'assignation n'est pas modéliser
l'attention.*

⚠ **L'autonomie graduée se traduit par un Profile — niveau d'autonomie, réversibilité — plutôt que par
une relation.** ⚠ **R-13 du Vol. III** : *l'échelle visée n'est jamais nommée nue ; le siège de la
désambiguïsation des trois échelles homonymes est au **ch. 43 § 43.5**, et ce chapitre n'en
reconstruit aucune.*

### 44.1.8 Patron « mémoire, récupération et ancrage gouverné »

**Siège de la modélisation de la persistance et de l'ancrage ; les mécanismes ne sont pas
réexpliqués** — *ils sont au ch. 5.*

La mémoire de l'agent et la base qui la sous-tend sont des **Data Objects**, accédés par la
**Function** de l'agent ; leur matérialisation au plan d'exécution est un **Artifact**. **La couche
sémantique qui structure l'ancrage est un Data Object réalisant un Business Object.**

⚠ **La décomposition recommandée n'est pas neutre, et c'est tout l'apport du patron** : *en
distinguant explicitement le Data Object **de mémoire**, le Data Object **de contexte récupéré** et le
Business Object **sémantique**, le modèle **expose les points où s'appliquent les contrôles** de
prévention de fuite et de filtrage de sortie.* ⚠ ***Sans cette décomposition, la mémoire devient une
boîte opaque où aucun contrôle n'a de point d'ancrage.***

⚠ **Et le ch. 39 § 39.2.4 a rencontré le même objet par l'autre bout** : *une quatrième source de
dérive, la mémoire continûment réécrite par des modèles auxiliaires, y est portée comme **relève à
instruire**, non comme fait.* **Le patron modélise ce que la relève interroge** — *ce qui est
exactement le rôle d'un formalisme, et exactement sa limite.*

### 44.1.9 Le registre des stéréotypes du blueprint

> ⚠ **POINT D'APPUI AVAL — et il est publié sous réserve.** Le plan déclare ce registre **point
> d'appui dont dépendent le ch. 45 et l'Annexe H**, à tenir **en un seul lieu**. ☐ **Le préalable que
> le plan lui assigne — la re-vérification du mécanisme d'extension tel que le document normatif de
> référence le porte — n'a pas été tenu** (§ 44.0.4). **Ce registre est donc reproduit comme registre
> du Vol. I, en [C], et non comme registre conforme à la version de référence.**

**Quatre limites structurelles sont à assumer avant le registre lui-même**, et elles ne se franchissent
par aucun stéréotype.

1. ⚠ **Le langage est un langage de description statique** : *il représente une **intention**
   d'architecture, non un **état d'exécution**.*
2. ⚠ **Le non-déterminisme du comportement d'un agent n'est pas représentable** : *un Process décrit
   le cadre de contrôle **attendu**, jamais le chemin **effectif**.*
3. ⚠ **L'état d'instance échappe au langage**, *qui modélise des **types**, non des **instances***.
4. ⚠ **La dynamicité de la découverte à l'exécution n'est pas native** (§ 44.1.6).

⚠ **S'y ajoute un effet de version sur la méthode** : *la distinction entre la logique de l'agent et
son substrat d'exécution **n'est plus une frontière de couche**, mais une **convention d'abstraction
et de stéréotype*** — étant entendu que **les deux domaines demeurent pairs et distincts, et ne
fusionnent pas**.

| Famille | Stéréotypes | Ce qu'ils annotent | Siège |
|---|---|---|---|
| **Patrons agentiques** | `<<Agent>>`, `<<MCP Server>>`, `<<NHI>>`, `<<Control Plane>>`, `<<reasoning loop>>`, `<<regulatory-requirement>>` | un élément **existant** du langage, dont la sémantique sous-jacente **reste la sienne** | § 44.1.2 à § 44.1.6, § 44.2 |
| **Substitution d'éléments retirés** | `<<Contract>>` (Specialization de Business Object), `<<maturity-gap>>` (Specialization d'Assessment), `<<KPI>>` (Specialization de Driver ou d'Assessment) | ⚠ **propositions du Vol. I, présentées par lui comme conventions gouvernées et non comme règles natives** — *et il déclare que le devenir de l'une d'elles **reste à confirmer** sur le document normatif* | § 44.4, § 43.5.3, § 46.1 |
| **Overlay de risque et de sécurité** | importés tels quels de l'overlay normalisé | ⚠ **non redéfinis ici** — *les redéfinir produirait un dialecte* | overlay d'origine |

: Tableau 44.1 — Le registre des stéréotypes du blueprint. ⚠ **Reproduit du Vol. I, en [C], et publié sous réserve du préalable non tenu (§ 44.0.4).** *Les **Profiles** normalisés portent les attributs typés d'**autonomie**, de **matérialité** et de **réversibilité** — les trois dimensions que les relations ne peuvent pas exprimer.*

⚠ **Le registre ne liste que les stéréotypes propres au blueprint agentique**, et cette borne est la
condition de sa portabilité : *importer un overlay normalisé sans le redéfinir préserve la conformité
au métamodèle ; le réécrire produirait exactement le dialecte que le mécanisme officiel permet
d'éviter.*

## § 44.2 — Motivation : des exigences réglementaires traçables

**Le domaine Motivation porte l'intention, et la somme n'en retient que la charpente.** Les éléments
mobilisés sont **Stakeholder**, **Driver**, **Assessment**, **Goal** et **Outcome**, **Principle** et
**Requirement**.

**La construction propre au blueprint tient en une convention** : *une exigence réglementaire est une
**Specialization de Requirement** stéréotypée `<<regulatory-requirement>>`* — ⚠ **et non un élément
Constraint**, *retiré en version de référence*. **Ce que cette convention achète** : *chaque texte
devient un objet de modèle **auquel une chaîne descendante peut se rattacher*** (§ 44.6).

⚠ **Ce que la somme ne fait pas ici, et il faut le dire au moment où le lecteur l'attendrait** : *elle
ne re-expose ni le contenu des textes — il est au **Livre III** —, ni leur croisement avec les
protocoles — il est au **ch. 42**.* **Ce paragraphe ne dit qu'une chose : où un texte se pose dans un
modèle.** *Le garde-fou de non-redondance s'applique ici plus qu'ailleurs — retirer le mot du langage
laisserait un exposé réglementaire, donc une redondance à renvoyer.*

**Les Assessments propres à l'agentique sont nommés et non développés** : *prolifération non gouvernée
d'agents, risque de modèle, concentration de fournisseurs.* ⚠ **Chacun est un objet de modèle, pas un
constat de la somme** : *le premier est une inférence du Vol. I en [C], les deux autres sont traités
au Livre III.*

## § 44.3 — Strategy : capacités agentiques et chaînes de valeur

**Le domaine Strategy porte trois éléments utiles au blueprint** : **Capability**, **Resource**,
**Course of Action**, plus **Value Stream**.

⚠ **La règle qui compte est une règle d'unité, et son anti-patron est nommé au § 44.8** : *la
**capacité agentique** est l'unité de planification — **ni le modèle, ni l'outil**.* **Une Capability
par serveur d'outils est un anti-patron**, *parce qu'elle fait dépendre le plan de l'implémentation.*

**L'ancrage sur des référentiels de capacités sectoriels** — *cartographies de domaines de service
bancaires ou assurantiels* — **se fait par Specialization**, ce qui **rend la réutilisation transverse
possible sans réinventer la carte**.

⚠ **Le Value Stream conscient de la coopération humain-agent est le seul apport propre de ce domaine**
au blueprint : *il rend visible, à l'échelle d'un flux de valeur, **où l'humain reste dans la
chaîne*** — et **le point d'arrêt du § 44.1.7 est son expression au grain du comportement**.

## § 44.4 — Business : rôles, collaborations humain-agent et objets financiers

**Le domaine Business tranche une question que le § 44.1.2 a posée sans la refermer : à quelle altitude
placer l'agent.**

⚠ **Le critère de bascule est de responsabilité, non de technique** : *un agent monte dans le domaine
Business **quand une responsabilité métier ou réglementaire lui est imputée** ; il reste dans
Application **quand il est un outil sous supervision**.* **Ce critère est une construction du Vol. I,
en [C]** — *aucune source normative ne le pose*.

**La collaboration humain-agent est une Business Collaboration** réalisant un comportement unifié
(§ 44.1.7). **Les objets et produits financiers sont des Business Objects et des Products** ; ⚠ **le
contrat, dont l'élément dédié est retiré en version de référence, se rend par une Specialization de
Business Object stéréotypée `<<Contract>>`** — *convention du registre, publiée sous la réserve du
§ 44.0.4*.

⚠ **Le raffinement d'un parcours humain-agent par une notation de processus dédiée est mentionné comme
possibilité, non comme prescription** : *le langage d'architecture décrit la structure, une notation de
processus décrit l'enchaînement fin — les deux se complètent et ne se remplacent pas.*

## § 44.5 — Application et Technology : agents, protocoles, exécution, résidence

**Les deux domaines demeurent pairs et distincts** (§ 44.0.2), **et la somme n'en retient que ce que la
traduction structurelle exige.**

**Côté Application** : *la métaclasse de l'agent est tranchée au § 44.1.2 ; la distinction **Function /
Process** l'est aussi — **Process** pour la boucle ordonnée, **Function** pour l'appel atomique.* **La
projection des protocoles, de la passerelle et du registre s'instancie sur les patrons du § 44.1**,
⚠ **sans redérivation du triplet** — *la redériver serait l'anti-patron n° 9.*

**Côté Technology** : **Node**, **Device** et **System Software** pour le parc d'exécution ;
**Service**, **Interface** et **Artifact** pour ce qu'il expose ; **Path** et **Communication
Network** pour le substrat d'échange ; ⚠ **et la projection technologique du patron d'identité non
humaine** — *les justificatifs deviennent des Artifacts, l'émetteur d'identité un Node, le magasin de
secrets un System Software.*

⚠ **L'observabilité s'y modélise comme un flux, et c'est le seul point où ce chapitre touche le
mouvement *exploiter*** : *un collecteur exporte la télémétrie par une relation **Flow***. **Ce que ce
formalisme ne dit pas** : *ce que cette télémétrie **porte*** — **le ch. 38 § 38.5 établit qu'elle ne
porte pas la clé de jointure**, et *aucun stéréotype n'y remédie.*

⚠ **La résidence et la souveraineté se modélisent par des Groupings de zone et des Profiles de
juridiction**, *ce qui rend visible une contrainte que le ch. 38 § 38.3 a nommée sans la résoudre* :
**quand des segments de trace transitent par des juridictions différentes, l'unicité de la trace
devient une contrainte d'architecture.** ⚠ **Le socle ne documente pas de mécanisme qui la
garantirait** : absence de documentation, non fait négatif vérifié (degré 3).

## § 44.6 — Points de vue transverses

**Quatre points de vue transverses complètent le blueprint**, et **le troisième est un siège**.

**Sécurité et risque.** *L'overlay normalisé s'applique au parc d'agents **tel quel***, ses stéréotypes
étant **importés et non redéfinis** (§ 44.1.9). **Chaque risque devient un Assessment, chaque contrôle
un Requirement réalisé par un service.**

**Confiance zéro, identité non humaine et segmentation.** *Le point de vue rend visible ce que le
ch. 37 § 37.7 a posé* : **la vérification est une fonction discrète exécutée avant l'établissement
d'une session, et la protection porte sur les ressources et non sur les segments.** ⚠ **Ce que le
formalisme apporte est une chose et une seule** : *il rend **énumérables** les arêtes que le modèle
prévoit de médiatiser* — **et le ch. 37 § 37.9 a établi que l'énumération du complément est la
question opérante**. ⚠ **Il ne dit pas si le déploiement réel les médiatise toutes.**

> ⚠ **SIÈGE DE LA CONFORMITÉ TRAÇABLE.** La chaîne se lit **de l'intention au substrat**, et **aucun
> maillon n'est facultatif** : *un **Driver** de conformité **influence** un **Assessment** de risque,
> qui justifie un **Requirement** — souvent une Specialization stéréotypée `<<regulatory-requirement>>`
> — ; ce Requirement est **réalisé** par un **Course of Action** ou une **Application Function**,
> lesquels sont à leur tour réalisés ou assignés à un **Application Component** ou un **Technology
> Service** concret.* ⚠ **Le critère d'auditabilité du blueprint est qu'aucun Requirement réglementaire
> ne demeure orphelin** — *c'est-à-dire dépourvu d'un élément exécutable qui le réalise effectivement.*

**Sur cette chaîne se construit la matrice d'auditabilité**, qui croise **le Requirement
réglementaire**, **le contrôle**, **le domaine de capacité concerné** et **l'élément qui porte la
responsabilité**. ⚠ **Elle ne se re-dérive pas à partir de rien** : *elle s'ancre sur la matrice du
ch. 42, que le blueprint **relie au modèle** plutôt qu'il ne la reformule.*

⚠ **L'orientation canadienne donne à cette chaîne des points d'ancrage datés, et la modalité de chacun
se porte.** *L'article 12.1 **impose** la traçabilité des décisions automatisées ; la ligne directrice
E-23 **attend** une gestion du risque de modèle qui s'étend aux méthodes d'IA et d'apprentissage
automatique, **jamais « exige »*** (réserve F-09 du Vol. II ; siège **ch. 25**). ⚠ **Chacun devient
dans le modèle un `<<regulatory-requirement>>` dont la chaîne descendante doit aboutir à un élément
exécutable** — *et c'est le seul endroit où ce chapitre touche au fond réglementaire, parce que c'est
le seul où la structure en dépend.*

**Audit et observabilité, avec ségrégation des tâches.** *Le journal d'audit est un **Data Object en
mode ajout seul**, propriété portée par un **Profile** plutôt que par un élément dédié.* **Toute
action sensible se rend par une Function dotée d'un Access en écriture vers ce Data Object, complété
d'un Triggering vers le service de journalisation** — ⚠ **de sorte que l'écriture de la trace soit
structurellement liée à l'exécution de l'action, et non optionnelle**.

⚠ **Un dernier critère distingue deux finalités qu'on confond souvent, et il est structurel** :
*l'observabilité d'exploitation et l'audit réglementaire **exploitent la même télémétrie** mais
**obéissent à des contraintes distinctes de rétention et de résidence**.* **Le blueprint les sépare en
deux Data Objects, voire deux Groupings** — ⚠ ***un journal d'exploitation purgé après quelques
semaines ne saurait tenir lieu de piste d'audit conservée des années.*** *C'est la même distinction
que le ch. 38 § 38.4 pose en régime de production ; ici, elle devient une séparation d'objets.*

## § 44.7 — Gouvernance des vues et organisation du blueprint

**Une vue est une représentation d'un sous-ensemble du modèle ; un point de vue en est le gabarit**,
qui nomme **les parties prenantes visées, leurs préoccupations et les éléments admis**. ⚠ **Deux
dimensions le caractérisent** : *sa **finalité** — concevoir, décider, informer — et son **niveau
d'abstraction** — détail, cohérence, vue d'ensemble.*

⚠ **La gouvernance des vues est ce qui distingue un blueprint d'un jeu de diagrammes**, et le Vol. I en
tire une règle : *états **actuel** et **cible** distingués, versionnement, et **réconciliation
périodique du référentiel avec le parc réel**.* **L'anti-patron correspondant est nommé au § 44.8 :
l'inventaire fantôme — un modèle d'intention déconnecté du parc.**

⚠ **Et c'est ici que le ch. 41 § 41.3 rejoint ce chapitre par l'autre bout** : *le **catalogue
interne** y est proposé comme le lieu où l'organisation sait ce qu'elle produit et exploite*, et
**la réconciliation dont il est question ici en serait le pendant côté modèle**. ⚠ **Ni l'un ni
l'autre n'est porté par une source** : *le catalogue est une construction d'auteur de matière neuve,
la réconciliation une thèse en [C] — les rapprocher est une lecture, et elle est marquée.*

⚠ **Une réserve d'outillage, datée et attribuée** : *à la mi-2026, deux ateliers nommés par le Vol. I
prennent en charge la spécialisation et les profils **sur le socle 3.2**, mais **pas encore l'export
natif de la version de référence*** — ⚠ **information rapportée par le Vol. I, en [C], statut et
version dits à la mention**. **D'où la règle du chapitre** : *écrire en version de référence **avec
note d'équivalence 3.2 par patron***.

## § 44.8 — Bibliothèque de patrons et anti-patrons

**Six patrons forment l'ossature opératoire**, chacun renvoyant à son siège au § 44.1 : *l'agent
gouverné ; le serveur d'outils gouverné ; l'échange agent-agent inter-domaines ; le plan de contrôle ;
le couple point d'arrêt humain / double regard ; la double qualification.* ⚠ **L'apport propre de la
bibliothèque n'est pas la liste, c'est l'instanciation par sous-domaine** : *un même patron se décline
d'un cas d'usage à l'autre **sans renégocier le triplet de modélisation**.*

**Neuf anti-patrons sont nommés avec leur correction**, et ⚠ **trois valent d'être retenus parce qu'un
chapitre aval les commettrait sans s'en apercevoir.**

| Anti-patron | Ce qu'il produit | Correction |
|---|---|---|
| **L'agent « boîte magique » mono-couche** | un seul élément censé tout porter | **décomposer** en Application Component `<<Agent>>` + Role + Application Process `<<reasoning loop>>` — ⚠ *faute de quoi **l'imputabilité et la boucle de raisonnement deviennent illisibles*** |
| **Le point d'arrêt humain décoratif** | un Role humain placé **hors** de l'étape irréversible | **faire tomber le point d'arrêt exactement sur l'action irréversible, par Assignment** — ⚠ *c'est la version structurelle du constat du ch. 40 § 40.4* |
| **L'inventaire fantôme** | un modèle d'intention **déconnecté du parc réel** | **réconcilier le référentiel avec l'inventaire d'agents et le catalogue** (§ 44.7) — ⚠ *et le ch. 40 § 40.2 a établi qu'**aucune source d'énumération du parc opposable n'est documentée*** |
| **L'interaction agent-agent modélisée en Serving** | une offre de service durable là où il n'y a qu'un échange | **réserver Serving à l'agent-spécialiste offert durablement ; rendre l'échange par Flow ou Triggering** |
| **Le serveur d'outils traité comme un élément inventé** | un dialecte non portable | **composer** Application Component + Application Service + Application Interface, *le seul mécanisme d'extension défendable étant Specialization + stéréotype + Profiles* |
| **La capacité réinventée par outil** | une Capability par serveur | **la capacité agentique est l'unité de planification, pas le modèle ni l'outil** (§ 44.3) |
| **Le modèle figé**, non versionné | un livrable de présentation | **gouvernance de vue, états actuel et cible, feuille de route par paliers** (§ 44.7 ; **ch. 43 § 43.5.3**) |
| **La confusion langage / méthode / outil** | une méthode prise pour un langage | **tenir la distinction du § 44.0.1** |
| **Re-expliquer les chapitres amont dans une vue** | de la prose protocolaire ou réglementaire **à la place** d'éléments et de relations | ⚠ **renvoyer**, et porter l'information variable **en carte thermique d'attribut** plutôt qu'en texte — *c'est le garde-fou de non-redondance appliqué à la vue* |

: Tableau 44.2 — Les neuf anti-patrons et leurs corrections. ⚠ **Le dernier est celui que ce chapitre risque à chaque paragraphe**, *puisqu'il suit quarante-trois chapitres au lieu de cinq.*

## § 44.9 — Questions ouvertes : le formalisme face aux systèmes autonomes

⚠ **Trois questions restent ouvertes, et aucune n'est refermée ici.**

**Première — l'adéquation à un système non déterministe.** *Le langage décrit des **types** d'éléments
et des relations **stables** ; or un système agentique se définit par **un état d'instance qui change
à l'exécution** et par **une décision non déterministe** — le même agent, sur la même entrée, peut
emprunter des chemins différents.* ⚠ **Le métamodèle ne dispose d'aucune construction pour représenter
cette variabilité**, et **aucun stéréotype du registre ne la franchit** : *elle relève du registre
descriptif lui-même, non du vocabulaire d'éléments.*

⚠ **La conséquence méthodologique est une complémentarité obligée, et elle est le legs le plus opérant
du chapitre** : *le blueprint fixe **l'intention d'architecture et les contrôles structurels** ;
l'observabilité et l'inventaire vivant renseignent **l'état effectif**.* ⚠ ***Les deux artefacts ne se
substituent pas ; ils se réconcilient*** — et **le ch. 38 a établi que le second terme de cette
complémentarité est précisément celui dont la clé de jointure manque.**

**Deuxième — le modèle vivant.** *L'idée d'un jumeau numérique organisationnel suppose **un modèle
alimenté et corrigé automatiquement**, plutôt qu'un livrable édité à la main.* ⚠ **Le Vol. I rapporte,
en [C] et avec ses éditeurs nommés, que des plateformes d'architecture exposent désormais des serveurs
d'outils sur leur référentiel** — ⚠ **capacités auto-déclarées par leurs éditeurs, statuts et dates
dits à la mention, non vérifiées indépendamment**. *Cela ouvre la possibilité que **des agents
interrogent et modifient le modèle d'architecture** — c'est-à-dire que **l'objet décrit et l'outil qui
le décrit convergent**.*

⚠ **Deux écueils dominent, et le second est structurel.** *Un* : **la vérification du modèle généré** —
*un modèle produit par un agent non déterministe **hérite de l'incertitude de son producteur**, et doit
être validé, faute de quoi le jumeau dérive.* *Deux* : **la tension de fond avec la nature statique du
langage** — *un modèle conçu pour décrire des types stables se prête mal à une réécriture continue par
des processus dont l'état change en permanence.* ⚠ **Et le ch. 41 § 41.5 rencontre exactement la même
difficulté sous un autre nom** : *une boucle de réémission suppose de restituer l'état antérieur de ce
qu'elle corrige.*

**Troisième — overlay contre extension formelle.** *Le pari du blueprint est qu'un **overlay** de
stéréotypes et de profils suffit, **sans inventer d'éléments**.* ⚠ **L'argument pour l'overlay est
l'économie et la stabilité** : *aucune fragmentation du langage, une convention gouvernée plutôt qu'un
dialecte.* ⚠ **L'argument pour l'extension est la fidélité ontologique** : *un stéréotype **ne fait
qu'annoter** un élément dont la sémantique sous-jacente reste celle d'un Application Component ou d'un
Role — **ce qui n'épuise pas le caractère propre de l'agent**.*

⚠ **Et le fait décisif est un fait de non-événement, à écrire avec sa borne** : *la version de
référence a **refondu son métamodèle en profondeur sans ajouter aucune prise en charge native de l'IA
ou des agents*** — **l'occasion d'une extension formelle a été disponible et n'a pas été saisie**.
⚠ **Ce constat vient du Vol. I, en [C], et la re-vérification sur le document normatif n'a pas été
conduite** (§ 44.0.4) : *c'est précisément l'énoncé que le préalable non tenu devait confirmer.*

⚠ **La question reste ouverte, et le blueprint assume sa réponse — l'overlay — comme un choix daté et
révisable, non comme une vérité du langage.**

## Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur.*

1. **Le verrou, posé une fois.** ⚠ **Aucun élément natif** ; **une seule extension défendable** —
   *Specialization + stéréotype + Profiles*, sur le modèle d'un overlay normalisé. Le **ch. 45** et
   l'**Annexe H** l'appliquent **sans le redécider**.
2. ⚠ **Le registre des stéréotypes, publié sous réserve.** ☐ *Le préalable que le plan lui assigne — la
   re-vérification sur le document normatif — **n'a pas été tenu***, et **le registre est reproduit en
   [C], non comme registre conforme**. *Le ch. 45 en dépend, et il en dépend sous la même réserve.*
3. **Les six patrons et les neuf anti-patrons.** ⚠ *Le neuvième anti-patron est le garde-fou du
   chapitre lui-même* : **retirer le mot du langage ; si la phrase tient comme un exposé des chapitres
   amont, c'est une redondance.**
4. ⚠ **SIÈGE : la conformité traçable.** *Driver → Assessment → Requirement → réalisation → élément
   exécutable*, **aucun maillon facultatif**, ⚠ **et le critère d'auditabilité est qu'aucun Requirement
   réglementaire ne demeure orphelin**. Le **ch. 45 § 45.4** l'instancie sur un portefeuille réel ; le
   **ch. 46** l'instrumente.
5. **La séparation structurelle de l'observabilité et de l'audit.** *Deux Data Objects, deux régimes de
   rétention* — ⚠ **un journal d'exploitation purgé ne tient pas lieu de piste d'audit**. Le **ch. 38
   § 38.4** le pose en régime de production ; **ici, il devient une séparation d'objets**.
6. **La complémentarité obligée du modèle et du parc.** ⚠ ***Le modèle fixe l'intention ;
   l'observabilité renseigne l'état ; les deux ne se substituent pas.*** *C'est le legs le plus opérant
   du chapitre, et le ch. 38 en a établi la faiblesse — la clé de jointure manque.*

⚠ **Ce que le chapitre ne lègue pas.** Aucun **fait** : *tout y est en [C]*. Aucune **conformité à la
version de référence** : *le préalable n'a pas été tenu*. Aucun **contenu réglementaire, protocolaire
ou d'exploitation** : *il ne les traduit que structurellement, et le neuvième anti-patron est la règle
qui l'y contraint*. Et aucune **représentation de l'exécution** : *le langage décrit des types ; le
non-déterminisme, l'état d'instance et la découverte dynamique lui échappent, et **aucun stéréotype ne
les rattrape**.*

---

## § 44.10 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle consigne l'écart de
gouvernance sous lequel la pièce a été rédigée (PRD, Annexe A).

**Ce qui est enfreint.** Portes **G-3**, **G-4** et **G-5** ; **volet résiduel de G-1** ; **ordre de
rédaction du PRD §6** ; ⚠ **et le préalable propre à ce chapitre — la re-vérification du mécanisme
d'extension sur le document normatif de référence —, que le TOC déclare *préalable au registre des
stéréotypes, non note de transition*, et que le PRD §12 nomme au jalon J-IV-5.** Instruction d'auteur
du **27 juillet 2026**.

1. **Aucun énoncé n'est central au sens de CA-IV-01, et ici la raison est double** : *le socle
   consolidé compte zéro entrée*, **et la source unique de ce chapitre entre en [C]** — sa
   vérification portant sur ses références et non sur le contenu de ses affirmations. ⚠ **Ce chapitre
   est le seul du Livre dont la totalité du corps est en [C]**, hors une réserve de modalité empruntée
   au Vol. II au § 44.6.
2. **Les décomptes sont publiables** (G-2) ; le réel est reporté au [`README.md`](README.md).
3. **Les renvois « ch. N » vers les Livres III à V sont des renvois de plan.** Ne sont pas rédigés :
   **ch. 25**, **ch. 45**, et l'**Annexe H**. Les renvois vers les **ch. 5, 7, 8, 12, 14, 16, 17, 19**
   résolvent contre du texte ; ceux vers les **ch. 37, 38, 40, 41, 42, 43, 46** résolvent contre du
   texte au terme de la présente passe.
4. **Le registre des stéréotypes est publié sous réserve explicite**, et *aucune conformité à la
   version de référence n'est attestée* — ⚠ **CA-IV-14 : « conforme » s'écrit depuis une constatation
   sur pièce, jamais depuis un document amont.**
5. **CA-IV-13 n'est pas satisfaite** — aucune relecture par un relecteur distinct du rédacteur.

**Remontées ouvertes par ce chapitre :**

- **R-IV-60 — non bloquante, de numérotation, ET ELLE PORTE SUR LE PLAN LUI-MÊME.** La table détaillée
  du ch. 44 numérote **les neuf sous-sections du § 44.1 en « 43.1.1 » à « 43.1.9 »**, ⚠ **soit dans la
  numérotation d'un autre chapitre** ; et sa **table de couverture** dirige la ligne du Vol. III
  *Monographie* §27.2 vers **« § 43 (transverse) »**, ⚠ **alors que le corps de l'entrée du ch. 44
  écrit que ce §27.2 est **consolidé ici**, dans le formalisme.** **Demande remontée** : réalignement
  des dix formes sur la numérotation courante (décision 8). ⚠ **C'est très exactement la classe de
  défaut que le `CLAUDE.md` du dossier consigne pour trois passes de structure consécutives** — *un
  remappage qui ne voit qu'une borne, et qu'aucun des quinze contrôles ne signale* : `check-toc.py`
  porte sur des motifs de ligne et **ne connaît pas les tables détaillées**. *La pièce écrit ses
  sous-sections en 44.1.x et remonte l'écart ; elle ne corrige pas le plan.*
- **R-IV-61 — BLOQUANTE pour la publication du § 44.1.9 et, par dépendance, du ch. 45.** Le plan
  déclare la **re-vérification du mécanisme Specialization + stéréotype + Profiles tel que le document
  normatif de référence le porte** comme **préalable au registre des stéréotypes, non note de
  transition**. ☐ **Elle n'a pas été conduite.** ⚠ **Trois raisons rendent l'omission coûteuse plutôt
  que formelle** : *(a)* la refonte du métamodèle **retire environ un tiers des éléments et remplace
  les couches par des domaines** — c'est la plus profonde depuis la création du langage ; *(b)* **trois
  entrées du registre sont des substitutions d'éléments retirés**, dont le Vol. I déclare lui-même que
  **le devenir de l'une reste à confirmer** ; *(c)* ⚠ **le ch. 45 et l'Annexe H dépendent de ce
  registre**, et *un point d'appui aval publié sous réserve propage sa réserve*. **Demande remontée** :
  **inscription de cette re-vérification au volet résiduel de G-1**, avec **domaine déclaré** — la
  liste des éléments retirés ou renommés, le mécanisme d'extension, et l'état du support d'outillage.
  ⚠ *Le PRD la nomme déjà à J-IV-5 ; ce qui manque n'est pas la mention, c'est l'exécution.*
- **R-IV-62 — non bloquante, de régime, et elle porte sur une classe.** **La totalité du corps de ce
  chapitre est en [C]** — le Vol. I étant sa source unique —, ⚠ **et cela inclut des énoncés que la
  somme traite ailleurs comme structurants** : *la limite du non-déterminisme, l'écart entre intention
  et exercice du contrôle humain, la complémentarité obligée du modèle et de l'observabilité.* **Ces
  trois énoncés sont repris par les ch. 40, 41 et 45**, et *aucun ne peut y devenir central tant qu'il
  reste en [C]*. **Demande remontée** : que **G-3 déclare la voie d'élévation** pour ce chapitre —
  *lecture des sources primaires que le Vol. I cite, avec la borne du PRD §7.1 : **une entrée sans
  source primaire tierce reste une thèse attribuée et ne porte jamais un fait central***. ⚠ *Une
  chaîne de dépendances dont le premier maillon est en [C] ne s'élève pas par ses maillons aval.*

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.25** — § 44.0 à
§ 44.9, dans l'ordre exact —, et **le contrat de lecture de la source est refondu en apparat**, comme
la table le prescrit. La **table de couverture est respectée pour ses sept lignes**, y compris ses
**deux prélèvements déclarés** : **§6.8 part au ch. 45** (exemple de bout en bout) et **§6.10 part au
ch. 43** (maturité par plateaux) — ⚠ *ni l'un ni l'autre n'est repris ici*, et **le §6.0.1 est refondu
en apparat**. Le **garde-fou de non-redondance est tenu de bout en bout** : *aucune phrase de ce
chapitre ne tient comme exposé des chapitres amont si l'on retire le mot du langage*, et **les renvois
remplacent partout la reprise**. Les **notes d'équivalence 3.2 sont portées aux deux patrons qui les
exigent** — *ceux qui mobilisent l'élément retiré* —, et **non aux patrons bâtis sur des éléments
inchangés**. Les **huit occurrences de degré 3** portent leur degré. Les **deux capacités
auto-déclarées** sont attribuées à leur éditeur nommé, avec statut et date. **Aucun siège neuf n'est
posé** ; **le siège de la conformité traçable est repris de la source à son emplacement** (§ 44.6), et
les sièges touchés — l'encadré du **ch. 7 § 7.5**, le passeport au **ch. 16**, les trois échelles au
**ch. 43 § 43.5** — portent leur renvoi.
