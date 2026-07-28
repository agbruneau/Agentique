# Chapitre 46 — Instrumentation et feuille de route vers le 1ᵉʳ mai 2027

*Livre IV — Appliquer, exploiter, produire et composer : AgentMesh, AgentOps, fabrique d'agents et
synthèse architecturale.
Quatrième mouvement — composer (ch. 42-46). **Dernier chapitre du mouvement et du Livre** : il
séquence dans le temps ce que les quatre précédents ont posé dans l'espace.*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — rédigé sur instruction d'auteur du 27 juillet 2026, **avant** les portes **G-3**, **G-4** et **G-5**, et hors de l'ordre de rédaction du PRD §6. ⚠ **R-IV-40 et R-IV-41, ouvertes au ch. 37, valent pour tout le Livre.** ⚠ **Ce chapitre est le seul du Livre dont l'objet est daté de bout en bout** : *son argument porte sur un compte à rebours, et **un compte à rebours ne se recopie pas — il se recalcule*** (§ 46.2) |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** ([`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Volet résiduel de G-1 non instruit** : *aucun jalon externe du § 46.3 n'a été repris à la source primaire*, et **c'est la matière la plus périssable du Livre**. Gel de source : **16 juillet 2026** (Vol. II) ; *il n'est pas celui de la somme, et l'écart de onze jours **change le compte à rebours*** |
| **Socle mobilisé** | ☑ **Le socle consolidé existe depuis le 28 juillet 2026** — [`socle-consolide.md`](../PRD/socle-consolide.md) v1.2, **159 entrées**, porte **G-3 franchie** (PRD v0.14). ⚠ **Les pièces n'ont PAS été re-citées en `S-nnn`** (PRD §7.1) : elles citent les identifiants sources préfixés, que les deux tables de correspondance résolvent — ici **Vol. II F-09 → `S-009`**, **Vol. II F-25 → `S-023`**, **Vol. II F-37 → `S-035`**, **Vol. II F-44 → `S-042`**. Vol. II — **F-09** *(attentes d'E-23, **[A/B mixte]** — **[A]** pour la publication, l'entrée en vigueur, la portée et la définition de « modèle » ; **[B]** pour les exigences opératoires extraites du texte intégral : inventaire, cotation, documentation et son appendice, surveillance continue, **absence de disposition transitoire** ; ⚠ **ce chapitre mobilise les deux strates**)* ; **F-25** *(calendrier de la ligne directrice de l'AMF)* ; **F-37** *(propriétés, métriques et enseignements d'orchestration)* ; **F-44** *(outils de gouvernance et d'observabilité — inférences marquées)*. **En renvoi seulement** : F-10, F-29, F-34, F-35, F-36, F-42. ⚠ **L'état de re-datation des quatre entrées mobilisées se lit avant tout emploi** : **F-37 ☑ inchangée**, **F-09 ☑ inchangée (partielle)**, ⚠ **F-25 et F-44 ☐ non établie** — *accès refusé par l'hôte, HTTP 403* —, et *ce sont exactement les deux entrées d'où ce chapitre tire sa matière la plus périssable : le calendrier de la seconde autorité et les statuts d'outillage du § 46.1*. **Aucun énoncé n'est central au sens de CA-IV-01**, et **aucun ne l'est sur une composante non re-vérifiée** ; *le franchissement de G-3 n'a conduit aucun vote adversarial — il reste dû pour toute entrée appelée à porter un fait central* |
| **Garde-fous balayés** | ⚠ **Règle de comptage, décision 16 du TOC** : les cardinaux ci-dessous portent sur le **marqueur littéral de l'identifiant** dans le **corps** de la pièce — de la première section à la synthèse, **en-tête et note de statut exclus** —, et ils sont **re-mesurés sur le corpus que le commit produit**. ⚠ **Un garde-fou appliqué sans que son identifiant soit écrit voit son DOMAINE déclaré, sans cardinal** (alinéa c) : *le domaine balayé est le corps entier, et les cardinaux antérieurs — qui comptaient les **applications** et non le marqueur — n'étaient re-mesurables par aucune règle écrite.* **Les deux séries sont balayées intégralement, zéros compris.** Vol. II — **réserve F-09 (« attendu par E-23 », jamais « exigé » ; « documentation de modèle » et « inventaire », jamais « fiche de modèle » *à propos d'E-23*) : une occurrence de l'identifiant**, § 46.3 — ⚠ *la formule imposée est employée à chaque énoncé sur E-23 des § 46.1, § 46.2 et § 46.3 : **domaine déclaré, sans cardinal*** ; **R-7 (le rapprochement entre une métrique ou un produit et l'instrumentation d'E-23 est une inférence d'auteur) : une occurrence**, § 46.1, ⚠ **nommé par volume — à ne pas confondre avec R-07 du Vol. III, qui porte lui aussi sur l'inférence produit ↔ réglementation** ; **réserve F-37 (préimpression non révisée) : une occurrence**, § 46.1 ; **réserve F-25 (jamais « en attente » ni « en projet ») : une occurrence**, § 46.3 ; **R-4 et réserve F-29 : une occurrence chacun**, § 46.3, en renvoi ; **R-5 (aucun standard technique désigné — formulation imposée) : une occurrence**, § 46.3 ; **métriques auto-déclarées (marqueur « auto-déclaré ») : une occurrence**, § 46.1 ; **§8.4 (neutralité fournisseur) appliqué par prudence : domaine déclaré, § 46.1, sans cardinal** — *le garde-fou est borné au mouvement d'instanciation, et ce chapitre mobilise pourtant des produits nommés* ; **R-1, R-2, R-3, R-6, R-8 : zéro occurrence.** Vol. III — **R-09 : une occurrence**, § 46.3 ; **R-11 (jalons « visés », jamais « fixés ») : une occurrence**, § 46.3 ; **R-14 : zéro occurrence de l'identifiant** — ⚠ *les degrés d'absence sont portés en toutes lettres aux § 46.1, § 46.2 et § 46.3 : **domaine déclaré, sans cardinal***. **R-01 à R-08, R-10, R-12, R-13 : zéro occurrence** |
| **Volumétrie cible** | ≈ **3 000 mots** de corps (§ 46.0 à la synthèse), **cible dérivée** de l'enveloppe du Livre (**69 000 mots**, TOC v0.25) au prorata des trois sections — **la plus basse du Livre**. ☑ **Décompte publiable depuis G-2** ; **réel reporté au [`README.md`](README.md)**. ⚠ **D-4 s'applique** |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) **v0.28**, entrée du chapitre 46 — **thèse collationnée et amendée en v0.28**, décisions 8 et 14, remontée R-IV-107)* — les métriques d'évaluation des orchestrations (correction, réactivité, traçabilité) sont l'instrumentation **candidate** des programmes E-23/AMF — ⚠ **« candidate » est un mot de l'auteur, absent du socle, et aucune source ne valide cet emploi** ; **le partage 4 → 3 tient à l'objet mesuré** — *artefact de conception pour la quatrième propriété instrumentée, comportement en exploitation pour les trois retenues* —, ⚠ **et la raison de fond disponible appuie les quatre, non les trois** ; la feuille de route se séquence sur l'entrée en vigueur commune (inventaire → encadrement → surveillance). ⚠ **Partage déclaré avec le ch. 40** : *la grille dérivée là-bas, l'instrumentation candidate ici.*

☑ **Les deux membres de la thèse ont résisté à la collation contre le texte rédigé de leur source —
décision 14 du TOC, appliquée avant la rédaction, et c'est l'un des deux seuls cas du Livre IV.** Le
Vol. II porte les deux membres **mot pour mot** ; le plan y ajoutait seulement, entre parenthèses,
**les trois mouvements que la source nomme elle-même**. ⚠ **Un point méritait d'être borné, et il vient
de la source** : *le mot « candidate » est **de l'auteur**, il n'est pas au socle, et **aucune source
ne valide l'emploi de ces métriques à ce titre**.* **Le corps l'écrit ainsi de bout en bout.**

⚠ **Ce que la thèse citée a gagné en v0.28, et pourquoi la citation ci-dessus est plus longue que la
forme v0.25 que cette pièce portait** (décision 17 du TOC, alinéa c) : *l'arbitrage a **amendé
l'entrée du plan sans en changer les deux membres*** — il y a **inscrit la borne du mot « candidate »**
que ce corps appliquait déjà, **motivé le partage 4 → 3 à la ligne Fusion** par l'objet mesuré, écrit
que **la raison de fond disponible appuie les quatre propriétés et non les trois**, et **déclaré le
partage avec le ch. 40** (remontées R-IV-107 et R-IV-109). *Aucune de ces additions ne contredit le
corps ; toutes y étaient déjà écrites, et c'est le plan qui les a rejointes.*

---

## § 46.0 — Ouverture : une architecture qu'on ne sait pas instrumenter est une intention

Le **ch. 42** a établi qu'**aucun protocole ne répond aux attentes des trois textes dont le socle porte
le contenu**, et que les deux autres lignes de sa matrice sont **vides pour des raisons opposées**. Le
**ch. 43** a construit les couches qui doivent compenser, le **ch. 44** les a formalisées, le **ch. 45**
les a instanciées.

**Reste ce qu'E-23 *attend* d'un programme de risque de modèle, et qui n'est pas un schéma** : ⚠ *des
normes de fréquence, de portée et de critères ; un suivi de la performance ; des seuils de
dépassement.* ⚠ ***Que mesure-t-on ? À quelle fréquence ? Contre quel seuil ?*** **Une architecture
qu'on ne sait pas instrumenter est une intention.**

⚠ **Ce chapitre soutient une proposition étroite, et il faut en énoncer l'étroitesse avant de la
défendre.** *Les métriques que la littérature académique attache aux options d'orchestration sont des
**candidates** à l'instrumentation d'un programme de risque de modèle canadien.* ⚠ **« Candidates » :
le mot est de l'auteur, il n'est pas au socle, et aucune source ne valide leur emploi à ce titre.** *Ce
chapitre les présente comme telles, expose ce qui manque pour qu'elles cessent de l'être, et séquence
le travail qui ne dépend, lui, d'aucune de ces réserves.*

⚠ **Et la frontière avec le ch. 40 se pose ici**, parce que les deux chapitres parlent d'indicateurs :
*le **ch. 40** dérive une grille **de ce que les cadres attendent**, et il ne produit **aucune
valeur** ; celui-ci demande si **des métriques existantes** pourraient servir cette grille.* ⚠ **Les
deux aboutissent au même endroit par deux chemins** : *le premier trouve une colonne de manques, le
second trouve des candidates sans validation.*

## § 46.1 — Des métriques académiques aux indicateurs de risque de modèle

### 46.1.1 Le point de départ est une liste, et sa source porte sa réserve

Une préimpression instrumente **quatre de ses cinq propriétés d'évaluation** : *la **spécificité de
tâche** par des mesures de complexité de code ; l'**assurance de correction** par la précision, le
rappel et leur moyenne harmonique ; la **réactivité** par le taux de faux négatifs et la vitesse de
réaction ; la **traçabilité** par la correction du journal* (Vol. II **F-37**, **[B]**).

⚠ **La réserve ne se détache jamais de l'entrée** : *préimpression **non révisée par les pairs**, dont
**les auteurs déclarent eux-mêmes des menaces à la validité*** — le cadre conceptuel est repris, **les
résultats chiffrés à titre d'illustration seulement**. ⚠ **La cinquième propriété, l'autonomie, ne
dispose d'aucune métrique dans l'entrée du socle** — *constat repris du **ch. 39 § 39.2.3**, qui en est
le siège, et dont il ne se conclut rien.*

⚠ **Le plan en retient trois — correction, réactivité, traçabilité — et le partage n'est pas celui de
la source.** *La quatrième propriété instrumentée, la spécificité de tâche, **n'y figure pas**.*
**Lecture de l'auteur** — *la ligne de partage paraît être celle de **l'objet mesuré** : les mesures de
complexité portent sur **un artefact de conception**, les trois autres sur **un comportement en
exploitation**, seul objet d'une surveillance continue.* ⚠ **Le socle n'opère pas ce partage et n'en
fournit pas le motif** ; *l'écart entre les quatre propriétés instrumentées et les trois retenues est
signalé plutôt que comblé.*

### 46.1.2 L'autre versant, et la modalité qui commande toute la section

Depuis l'extraction de son texte intégral, le socle porte ce que la ligne directrice E-23 **attend** en
matière de surveillance continue — ⚠ **et la modalité est contraignante** : *E-23 est **fondée sur des
principes** et rédigée au conditionnel ; **elle attend, elle n'exige pas***.

**Son principe de surveillance attend** : *des normes de **fréquence, de portée et de critères** par
palier de risque ; le suivi de **la performance, de l'usage, des données d'entrée et des dépendances
externes** ; des **seuils de dépassement** ; et, verbatim, des processus pour traiter les défis propres
à l'IA et à l'apprentissage automatique — **« autonomous decision making, autonomous re-parametrization,
and the elevated potential for model drift »***.

⚠ **Les deux listes se regardent. Il faut résister à la tentation de les superposer.**

| Métrique candidate | Ce qu'E-23 **attend** en regard | ⚠ Pourquoi ce n'est pas une correspondance |
|---|---|---|
| **précision, rappel, moyenne harmonique** — assurance de correction | **suivi de la performance** | *les deux portent sur la conformité d'un résultat à l'attendu, mais **l'un est une mesure de laboratoire sur un scénario**, l'autre **une attente de dispositif sur un parc*** |
| **vitesse de réaction, taux de faux négatifs** — réactivité | **seuils de dépassement** | ⚠ *le socle **ne dit pas de quelle grandeur*** |
| **correction du journal** — traçabilité | **documentation de modèle et inventaire**, dont l'appendice énumère les champs | ⚠ *objets **d'une tout autre nature** qu'un journal d'exécution* |

: Tableau 46.1 — Les trois rapprochements plausibles, et pourquoi aucun n'est documenté. ⚠ **Le socle porte les deux termes de chacun ; il n'en porte aucun rapprochement.** *Ce sont des candidatures, pas des correspondances.*

### 46.1.3 Une raison de fond appuie la candidature — et elle n'appuie pas le partage

**Lecture de l'auteur**, posée au **ch. 43 § 43.3** et non au socle : *les **quatre** propriétés
instrumentées — **spécificité de tâche comprise** — sont celles qu'un exploitant peut **démontrer à un
tiers**, et **c'est l'instrumentation qui rend une propriété démontrable***. **Et un programme de
risque de modèle est précisément un dispositif de démonstration à un tiers.**

⚠ **La convergence d'objet est réelle ; elle ne vaut pas validation.** ⚠ **Et il faut la noter
exactement** : *cette raison appuie les **quatre** propriétés, **la spécificité de tâche comprise**, et
non les trois que retient le plan.* ***Elle ne fournit donc aucun motif au partage 4 → 3***, que le
socle n'opère pas davantage.

### 46.1.4 L'outillage, et le garde-fou le plus important du chapitre

Le socle documente, **chez un éditeur nommé**, des capacités qui portent sur les mêmes objets —
*inventorier, coter, surveiller* : ⚠ **selon la documentation de cet éditeur**, un produit de
gouvernance **en disponibilité générale déclarée** depuis une date nommée, assorti en 2025 d'une
gouvernance agentique ; et, ⚠ **en préversion publique annoncée**, une observabilité d'agents et de
modèles (Vol. II **F-44**). ⚠ **Statuts auto-déclarés, attribués à leur éditeur, non vérifiés
indépendamment.** *Le socle documente par ailleurs des capacités d'orchestration chez d'autres
éditeurs — **siège ch. 43 § 43.6** — ;* ⚠ **aucune n'est ici comparée aux précédentes.**

⚠ **Et c'est ici que le garde-fou le plus important de ce chapitre s'applique.** ***Le rapprochement
entre un produit de gouvernance et E-23 est une inférence d'auteur : l'éditeur ne revendique aucune
conformité à E-23, et aucune source ne documente ce lien*** (R-7 du Vol. II ; **fait négatif ÉTABLI**,
siège **ch. 45 § 45.4**). **La même règle vaut pour le produit d'observabilité.** ⚠ **Le rapprochement
avec la ligne directrice de l'AMF est lui aussi une inférence d'auteur** — *mais **le régime d'absence
diffère**, et le ch. 45 § 45.4 en est le siège.*

⚠ **Que l'éditeur ne revendique rien à l'endroit d'E-23 n'autorise aucune généralisation** : *le socle
atteste au contraire, pour un module de conformité issu d'un accord de revente daté, **des contenus que
l'éditeur destine à trois cadres nommés** — **aucun des trois n'est un texte canadien**.*

> **État de la recherche — la validité de ces métriques comme indicateurs de risque.** **Question** :
> les métriques de correction, de réactivité et de traçabilité sont-elles **valides** comme indicateurs
> de risque de modèle en contexte financier canadien ? **État** : lacune ouverte le 16 juillet 2026 ;
> ⚠ **aucune passe de recherche n'a été conduite**. **Ce que le socle établit** : les quatre propriétés
> instrumentées et leurs métriques, et un jeu de résultats sur un scénario unique. **Ce qu'il n'établit
> pas** : ⚠ *aucune reproduction indépendante ; aucune application documentée de la taxonomie à un
> processus d'institution financière ; **aucune validation de ces métriques comme indicateurs de
> risque***. **Corpus à ouvrir** : la préimpression elle-même, à sa source primaire, et les
> publications de l'autorité postérieures au gel. **Critère de clôture** : qu'une validation soit
> documentée, ou que son absence soit **établie par balayage** plutôt que présumée. ⚠ **La question
> reste ouverte ; aucune inférence n'est proposée ici.**

## § 46.2 — Feuille de route type : inventaire, encadrement, surveillance

### 46.2.1 Le compte à rebours, recalculé et non recopié

⚠ **Un compte à rebours est le cardinal le plus périssable qu'un chapitre puisse porter, et celui-ci
est recalculé au gel de la somme plutôt que repris de sa source.** *Du **27 juillet 2026** — date du
gel unique — au **1ᵉʳ mai 2027**, il reste **neuf mois et quatre jours**, soit **278 jours**.* ⚠ **Le
Vol. II en comptait neuf mois et quinze jours à son propre gel du 16 juillet 2026** : *l'écart de onze
jours entre les deux gels est exactement l'écart entre les deux comptes*, **et c'est pourquoi le chiffre
ne se recopie pas.**

⚠ **Et le texte ne porte aucune disposition transitoire.** *La ligne directrice de l'AMF, **finale** —
et ⚠ **jamais « en attente » ni « en projet »** — **entre en vigueur à la même date**.* ⚠ **Cette
convergence commande le séquencement**, *et elle est la seule chose que la somme puisse en tirer* :
**le socle ne porte de ce second texte que son calendrier.**

### 46.2.2 Premier mouvement — inventorier

**E-23 attend un inventaire des modèles dont le risque inhérent est jugé non négligeable, tenu à
l'échelle de l'entreprise, exact, tenu à jour et soumis à des contrôles robustes** ; ⚠ **son appendice
en énumère les champs** — *identifiant, nom, cote de risque, propriétaire, développeur, origine, puis,
pour les modèles à risque non négligeable, version, date de déploiement, réviseur, approbateur,
dépendances, sources de données, usages approuvés, limites, date de revue, état de surveillance,
prochaine revue.*

⚠ **Ce premier mouvement ne dépend d'aucune des réserves du § 46.1** : *il est tracé au texte, il est
daté, et **il se conduit sans qu'aucune métrique académique n'y intervienne**.*

⚠ **Il porte cependant une difficulté propre, et c'est celle du périmètre.** *E-23 **ne nomme ni
l'agentique, ni les agents, ni l'orchestration** — vérification mécanique sur le texte intégral. Sa
définition de « modèle », laissée « intentionally broad », **englobe les méthodes d'IA et
d'apprentissage automatique**, et le texte vise expressément la prise de décision autonome et la
re-paramétrisation autonome ; d'où une **couverture implicite** que des analystes juridiques tiennent
pour acquise* — ⚠ **inférence d'analystes, jamais « le régulateur exige pour l'IA agentique ».** **La
conduite qui en découle est celle du ch. 25** : *traiter la couverture comme acquise, **et documenter
qu'on le fait par prudence plutôt que par obligation établie**.* ⚠ **L'inventaire est le lieu où cette
prudence se paie ou s'économise.**

⚠ **Et c'est ici que le ch. 40 § 40.2 rejoint ce chapitre par l'autre bout** : *sa grille demande **un
dénominateur** — une source d'énumération du parc opposable à l'inventaire attendu — et **déclare
qu'aucune n'est documentée** (degré 3).* ***L'inventaire attendu par E-23 et le dénombrement d'un parc
d'agents ne portent pas sur le même objet, et le ch. 43 § 43.1.2 l'a écrit*** : *le premier recense des
modèles, le second des agents.*

### 46.2.3 Deuxième mouvement — coter, puis encadrer

**E-23 attend que chaque modèle reçoive une cote de risque, et que la portée, l'échelle et l'intensité
de la gestion soient proportionnées à ce risque.** ⚠ **La cotation précède l'encadrement parce qu'elle
le calibre.**

**Vient ensuite le travail que les ch. 29 et 43 ont défini** : *positionner chaque processus sur les
options d'orchestration, et **imposer un cadre déterministe à ceux qui relèvent d'une exigence
stricte***.

⚠ **La chaîne qui rend l'encadrement opposable n'est pas reconstruite ici** : *de l'intention au
substrat — pilote de conformité, évaluation de risque, exigence, réalisation, élément exécutable —,
elle a **son siège pour toute la somme au ch. 44 § 44.6**, avec son critère d'auditabilité (*aucune
exigence réglementaire orpheline*). **Ce chapitre y renvoie et n'en refait aucun maillon** ; il en tire
seulement la conséquence de calendrier : *une exigence qu'aucun élément exécutable ne réalise au
1ᵉʳ mai 2027 est une exigence non encadrée, quelle que soit la qualité du schéma qui la porte.*

**Lecture de l'auteur** — ⚠ *la cotation attendue par E-23 et la grille de sélection de la
préimpression **portent sur le même geste** — décider combien d'encadrement mérite un processus — **mais
aucune source ne les relie***, et ⚠ **les sept critères de sélection sont qualitatifs : ils orientent
un jugement, ils ne calculent pas une réponse.** ***Une institution qui voudrait industrialiser ce
choix devra construire elle-même sa pondération et l'assumer comme sa propre décision.***

### 46.2.4 Troisième mouvement — surveiller

⚠ **C'est le seul des trois où l'instrumentation du § 46.1 trouve sa place, et c'est donc le seul qui
hérite de ses réserves.**

**Un enseignement du socle y commande pourtant une décision d'architecture immédiate, et il ne dépend
d'aucun chiffre** : *la journalisation confiée aux agents « **n'est généralement pas recommandée** »*
⚠ **(préimpression, source unique)**. **Lecture de l'auteur** — *si la trace n'est pas produite par
l'agent, et si E-23 **attend** un état de surveillance par modèle inventorié, alors **le lieu de
production de la trace est une décision à prendre avant le 1ᵉʳ mai 2027, non après**.* ⚠ **Le socle
déconseille un producteur ; il n'en désigne aucun autre** — *et le **ch. 43 § 43.3** en a fait le point
de contrôle obligatoire PC2, dont il déclare que **l'élimination des trois autres candidats est de
l'auteur**.*

⚠ **Un mot, enfin, sur ce que cette feuille de route ne peut pas faire.** *Elle est séquencée sur deux
textes **dont un seul est au socle par son contenu**.* ⚠ **Le socle ne porte de la ligne directrice de
l'AMF que son calendrier** ; *son contenu article par article relève d'une **lacune déclarée**.*
**Lecture de l'auteur** — ⚠ *la convergence des dates rend rationnel **un programme unique plutôt que
deux** ; **elle ne dit rien de ce que le second texte attend**, et la somme ne le fabriquera pas.*

## § 46.3 — Les jalons externes à surveiller

⚠ **Cette section est la plus périssable de la somme, et elle porte sa péremption dans son objet
même** : *elle recense des événements dont **la survenue est ce qui la périme**.* ⚠ **Elle recoupe les
événements de péremption du ch. 50 sans les reconstruire** — *ce chapitre en est le siège ;* ⚠ *il n'était
pas rédigé à la date de cette pièce, il l'est depuis, hors portes.*

| Jalon | Ce que le socle en porte, à sa date | ⚠ Régime |
|---|---|---|
| **Entrée en vigueur d'E-23** et de la **ligne directrice IA de l'AMF**, **1ᵉʳ mai 2027** | échéances **datées d'un texte publié** (Vol. II **F-09**, **F-25**) | **PROGRAMMÉ** — *seul jalon du tableau dans ce tri* |
| **Cadre bancaire — désignation d'un organisme de normalisation technique** | ⚠ *aucun organisme désigné, **aucun standard nommé** dans les textes officiels* ; le règlement est **prépublié**, son texte final peut changer (Vol. II **F-34**, **F-35**) | ⚠ **fait négatif VÉRIFIÉ, borné aux chaînes cherchées** ; *la candidature d'un format d'industrie relève du **commentaire d'industrie*** (R-5 du Vol. II) |
| **Rail de paiement en temps réel** | ⚠ **quatre cibles successives — 2019, 2022, 2023, 2026 —, jamais « quatre reports », et jamais « lancé »** (réserve F-29, R-4 du Vol. II ; siège **ch. 33**) | *renvoi seul ; ce chapitre n'en tire rien* |
| **Révision majeure du protocole agent-outil** | **annoncée au brouillon**, ⚠ **sa date n'est pas confirmée à la source** (R-09 du Vol. III) | ⚠ **aucun tri prospectif ne lui est attribué**, *et l'abstention est motivée : le PROGRAMMÉ exige un engagement daté réel, et c'est la date qui manque* |
| **Jalons post-quantiques** | ⚠ **« visés », jamais « fixés »**, statut du document porté (R-11 du Vol. III) | ⚠ **siège au ch. 21**, *qui ne se fusionne jamais* — renvoi seul |
| **Conventions sémantiques d'instrumentation** | ⚠ **premier des cinq échelons, aucune version citable** (siège **ch. 38 § 38.2**) | **SPÉCULATIF** — *aucun jalon daté n'est relevé* |

: Tableau 46.2 — Les jalons externes à surveiller, avec leur régime épistémique. ⚠ **Un seul est PROGRAMMÉ ; deux sont des faits négatifs bornés ; trois sont des renvois dont le siège est ailleurs.**

⚠ **Les trois statuts employés dans la colonne de régime — PROGRAMMÉ, PROJETÉ, SPÉCULATIF — ne sont
pas définis ici** : *leur **siège pour toute la somme est au ch. 49 § 49.0***, et ce chapitre les
**applique sans les redéfinir**. *Un tri qui redéfinirait ses propres statuts au lieu de renvoyer au
siège ferait diverger la seule échelle prospective de l'ouvrage.*

⚠ **Lecture de l'auteur, et c'est le dernier énoncé du Livre** : *des six jalons, **un seul porte une
date opposable**, et **c'est celui qui commande la feuille de route**. Les cinq autres sont des états
d'attente — **et un programme séquencé sur des états d'attente n'a qu'un seul point d'ancrage**.*
⚠ **Le socle ne documente aucun mécanisme de surveillance de ces jalons** : absence de documentation,
non fait négatif vérifié (degré 3). ***Ce que la somme peut faire est les nommer et les dater ; les
surveiller est le travail du ch. 50 —*** ⚠ ***non rédigé à la date de cette pièce, rédigé depuis, hors portes.***

## Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur.*

1. **Le mot « candidate », et ce qu'il refuse.** ⚠ *Trois métriques sont **candidates** à
   l'instrumentation d'un programme de risque de modèle ; **aucune source ne valide cet emploi**, et le
   mot est de l'auteur.* **Le ch. 49 enregistrera si la candidature a été instruite.**
2. **Les trois rapprochements, et pourquoi aucun n'est une correspondance.** ⚠ *Le socle porte les deux
   termes de chacun ; **il n'en porte aucun rapprochement**.*
3. **Le partage 4 → 3, signalé et non comblé.** ⚠ *La raison de fond appuie **quatre** propriétés ;
   **le plan en retient trois**, et le socle n'opère pas le partage.*
4. **La feuille de route en trois mouvements, et l'asymétrie de leurs dépendances.** ⚠ ***Le premier ne
   dépend d'aucune réserve ; le troisième en hérite toutes.*** *C'est le seul legs opératoire du
   chapitre : **on peut commencer par l'inventaire sans avoir tranché la validité d'une seule
   métrique**.*
5. **Le compte à rebours, recalculé au gel de la somme.** ⚠ **278 jours**, *neuf mois et quatre
   jours* — **et l'écart de onze jours avec le compte de la source est exactement l'écart entre les
   deux gels.** *Un cardinal daté ne se recopie pas.*
6. **Les six jalons, et leur régime.** ⚠ *Un seul est **PROGRAMMÉ**.* **Le ch. 50 en est le siège pour
   la surveillance ; ce chapitre les nomme et les date.**

⚠ **Ce que le chapitre ne lègue pas.** Aucune **validation** : *la candidature reste une candidature.*
Aucun **seuil** : *le socle ne dit pas de quelle grandeur.* Aucune **attente de la seconde autorité** :
*le socle n'en porte que le calendrier, et la somme ne fabriquera pas le contenu qui manque.* Et aucune
**conformité** : ⚠ *le rapprochement entre un outil et une attente réglementaire reste une inférence
d'auteur, à chaque occurrence, et **l'éditeur ne revendique rien**.*

---

## § 46.4 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle consigne l'écart de
gouvernance sous lequel la pièce a été rédigée (PRD, Annexe A).

**Ce qui est enfreint.** Portes **G-3**, **G-4** et **G-5** ; **volet résiduel de G-1** — ⚠ **et c'est
le chapitre du Livre où l'omission est la plus visible** : *son § 46.3 recense six jalons dont **aucun
n'a été repris à la source primaire au gel de la somme*** ; **ordre de rédaction du PRD §6**.
Instruction d'auteur du **27 juillet 2026**.

1. **Aucun énoncé n'est central au sens de CA-IV-01.** ⚠ **Et l'entrée principale du chapitre est
   mixte** : *E-23 y entre à deux niveaux — l'un pour son calendrier et sa portée, l'autre pour ses
   exigences opératoires extraites du texte intégral —, **et ce chapitre mobilise les deux strates**.
   Confondre les deux ferait porter à une extraction ce qu'un vote adversarial avait établi, ou
   l'inverse.*
2. **Les décomptes sont publiables** (G-2) ; le réel est reporté au [`README.md`](README.md). ⚠ **Et le
   compte à rebours du § 46.2.1 est recalculé, non recopié** — *278 jours du 27 juillet 2026 au
   1ᵉʳ mai 2027.*
3. **Les renvois « ch. N » : état FINAL de la passe, et non ordre d'écriture.** ⚠ *La forme
   antérieure de ce point photographiait l'instant où cette pièce a été écrite ; elle est corrigée
   ici sur l'état que le commit produit.* **Les dix chapitres du Livre IV (ch. 37 à 46) sont
   rédigés**, comme le sont les **cinquante chapitres des cinq Livres** : *tous les renvois « ch.
   N » de cette pièce résolvent donc contre du texte.* ⚠ **Ce qui reste vrai de la forme
   antérieure, et qui est daté** : à l'heure où ce chapitre a été écrit, n'étaient rédigés ni les
   ch. 25, 29 et 33 du Livre III, ni les ch. 49 et 50 du Livre V — *les renvois qui les visent ont
   été posés comme renvois de plan et n'ont pas été re-vérifiés contre le texte paru après eux.* ⚠
   **Et « résoudre contre du texte » ne vaut pas recevabilité** : *le texte visé est lui-même un
   brouillon hors portes.*
4. **La neutralité fournisseur est appliquée par prudence**, ⚠ *le garde-fou étant borné au mouvement
   d'instanciation alors que ce chapitre mobilise des produits nommés* : **statuts auto-déclarés
   attribués, aucune comparaison, aucune recommandation.**
5. **CA-IV-13 n'est pas satisfaite** — aucune relecture par un relecteur distinct du rédacteur.

**Remontées ouvertes par ce chapitre :**

- **R-IV-107 — non bloquante, de partage non motivé, et elle est héritée.** Le plan retient **trois** des
  **quatre** propriétés instrumentées — *correction, réactivité, traçabilité* —, **et écarte la
  spécificité de tâche**. ⚠ **Le socle n'opère pas ce partage et n'en fournit pas le motif**, et *la
  seule raison de fond disponible — que ces propriétés sont celles qu'un exploitant **démontre** à un
  tiers — **appuie les quatre**, non les trois*. **La source signale déjà l'écart chez elle.**
  **Demande remontée** : que **le motif du partage soit écrit à la ligne Fusion**, ou que **la
  quatrième propriété soit réintégrée**. ⚠ *Un partage repris de passe en passe sans motif finit par
  ressembler à un résultat.*
  ☑ **Issue, 27 juillet 2026** — **TOC, ligne Fusion** — le **partage 4 → 3** des propriétés
  instrumentées est **motivé à la ligne Fusion** : *l'objet mesuré — artefact de conception
  contre comportement en exploitation* ; ⚠ **et la borne est écrite** : *la raison de fond
  disponible appuie les **quatre**, non les trois.* **La citation en tête de cette pièce porte
  la forme amendée** (décision 17 du TOC).
- **R-IV-108 — non bloquante, de fait périssable, et elle vise un domaine plutôt qu'un fait.** Le
  § 46.3 recense **six jalons externes**, ⚠ **dont un seul est PROGRAMMÉ et dont aucun n'a été repris à
  la source primaire au gel de la somme**. *Deux d'entre eux sont des faits négatifs vérifiés bornés
  aux chaînes cherchées ; un troisième est annoncé au brouillon sans date confirmée ; un quatrième est
  au premier échelon d'une échelle de maturité sans version citable.* **Demande remontée** : que **le
  volet résiduel de G-1 inscrive les six jalons de ce tableau à son domaine**, avec **le critère de
  reprise de chacun** — *une désignation publiée, un arrêté, une ratification, une publication de
  version.* ⚠ *Un tableau de jalons dont aucun n'est re-daté au gel est un tableau daté d'un autre
  jour, et c'est le seul défaut qui périme un chapitre entier plutôt qu'un énoncé.*
  ☑ **Issue, 27 juillet 2026** — **PRD, volet résiduel de G-1, DOMAINE DÉCLARÉ** — les **six
  jalons externes** entrent au domaine **avec le critère de reprise de chacun** : *une
  désignation publiée, un arrêté, une ratification, une publication de version* ; ⚠ *un tableau
  de jalons dont aucun n'est re-daté au gel est daté d'un autre jour.*
- **R-IV-109 — non bloquante, de frontière entre chapitres.** Le **ch. 40** dérive une **grille
  d'indicateurs** de ce que les cadres attendent et **ne produit aucune valeur** ; ce chapitre demande
  si **des métriques existantes** pourraient servir un programme réglementaire. ⚠ **Les deux
  aboutissent au même constat par deux chemins — manques d'un côté, candidatures sans validation de
  l'autre — et le plan ne déclare pas leur articulation.** **Demande remontée** : que **la ligne Fusion
  du ch. 46 déclare le partage avec le ch. 40** — *la grille dérivée d'un côté, l'instrumentation
  candidate de l'autre* —, comme le TOC le fait pour les partages déclarés du ch. 40 § 40.3 avec le
  ch. 49. ⚠ *Deux chapitres qui produisent le même constat sans se déclarer se répéteront à la
  relecture, ou se contrediront.*
  ☑ **Issue, 27 juillet 2026** — **TOC, ligne Fusion** — le **partage avec le ch. 40 est déclaré**
  : *la grille dérivée d'un côté, l'instrumentation candidate de l'autre* ; ⚠ *deux chapitres
  qui produisent le même constat sans se déclarer se répéteront à la relecture, ou se
  contrediront.*

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.28** — § 46.1 à
§ 46.3, dans l'ordre exact —, et le § 46.0 est une introduction de chapitre. La **table de couverture
est respectée pour son unique ligne** : Vol. II §20.1-20.3 en **condensé**. ⚠ **Cardinaux re-mesurés au commit du 28 juillet 2026, sur le marqueur littéral et sur le corps seul** (décision 16 du TOC) ; *les cardinaux antérieurs comptaient les applications du garde-fou et n'étaient re-mesurables par aucune règle écrite.* La **forme imposée « attendu par E-23 » est tenue à chaque énoncé sur E-23 —
domaine déclaré, sans cardinal** (alinéa c), le marqueur littéral y comptant **deux occurrences** ; et
⚠ **« fiche de modèle » compte zéro occurrence à propos d'E-23**, re-mesuré. Le **garde-fou
d'inférence produit ↔ réglementation est nommé par volume** — marqueur littéral « R-7 », **une
occurrence**, § 46.1 —, ⚠ *les deux séries portant chacune un garde-fou sur ce même geste et le renvoi
nu étant indécidable*. La **réserve de la préimpression** est portée à chaque mobilisation — marqueur
littéral « F-37 », **une occurrence** —, et **ses résultats chiffrés ne sont pas repris**. Le **statut
auto-déclaré du § 46.1 — une occurrence du marqueur « auto-déclaré »** — est attribué à son éditeur
nommé. Le **compte à rebours est recalculé au gel de la somme**, et **l'écart avec celui
de la source est déclaré**. Le marqueur littéral **« degré 3 » compte deux occurrences**, chacune portant son
degré, et **les deux faits négatifs vérifiés portent leur borne**. **Aucun siège neuf n'est posé** ; les sièges touchés — les
points de contrôle obligatoires au **ch. 43 § 43.3**, la correspondance réglementaire au **ch. 45
§ 45.4**, l'horloge post-quantique au **ch. 21**, l'état des conventions au **ch. 38 § 38.2** —
portent leur renvoi.
