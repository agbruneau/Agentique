# Chapitre 43 — L'architecture de référence unifiée par couches

*Livre IV — Appliquer, exploiter, produire et composer : AgentMesh, AgentOps, fabrique d'agents et
synthèse architecturale.
Quatrième mouvement — composer (ch. 42-46). Deuxième chapitre du mouvement : **là où le ch. 42 a
constaté cinq vides, celui-ci construit ce qui les comble — et doit dire d'abord à quel titre.***

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — rédigé sur instruction d'auteur du 27 juillet 2026, **avant** les portes **G-3**, **G-4** et **G-5**, et hors de l'ordre de rédaction du PRD §6. ⚠ **R-IV-40 et R-IV-41, ouvertes au ch. 37, valent pour tout le Livre.** ⚠ **Ce chapitre porte TROIS sièges pour toute la somme** — les **cinq points de contrôle obligatoires** (§ 43.3), le **modèle de maturité avec la désambiguïsation des trois échelles d'autonomie** (§ 43.5) et la **collision de vocabulaire « fabrique »** que la décision 12c du TOC lui assigne (§ 43.1). ☑ **Les trois sont versés à [`PRD/check-sieges.py`](../PRD/check-sieges.py)**, constaté sur pièce le 28 juillet 2026 |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** ([`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Volet résiduel de G-1 non instruit.** Gels de source : **16 juillet 2026** (Vol. II), **21 juillet 2026** (Vol. III), **juin 2026** (Vol. I). *Aucun n'est celui de la somme.* |
| **Socle mobilisé** | ⚠ **Écrite avant l'existence du socle consolidé, la pièce ne s'y ré-adosse pas.** L'Annexe B ([`PRD/socle-consolide.md`](../PRD/socle-consolide.md), **159 entrées `S-001`…`S-159`**) existe depuis le **28 juillet 2026**, **porte G-3 franchie** — *la formule « socle consolidé : zéro entrée » a cessé d'être vraie et n'est plus écrite ici* ; les énoncés ci-dessous résolvent **contre les socles des volumes, par leurs identifiants d'origine**, et **la correspondance vers les `S-nnn` reste due**. Vol. II — **F-36**, **F-37**, **F-46** (assignés par le plan) ; **F-07**, **F-08**, **F-15**, **F-16**, **F-32**, **F-33** ; **F-01**, **F-02**, **F-04** (couche protocolaire) ; **F-09**, **F-25**, **F-26**, **F-27** (couche de gouvernance) ; **F-35** avec **F-11** et **F-34** ; **F-17**, **F-21**, **F-28** ; **F-10** en renvoi. Vol. III — **F-01**, **F-04**, **F-08**, **F-09**, **F-11**, **F-35**, **F-40**, **F-46**, **F-47**, **F-52**, **F-70**, **F-71**, **F-90** à **F-96** ; **H-01** à **H-03**, **H-11**, **H-12**, **H-15**, **H-17**, **H-24**, **H-25**, **H-27**, **H-31**. Vol. I *Monographie* §2.13.1, §4.12, §5.12.1-5.12.3 et §6.10, **en [C]**. ⚠ **Les deux séries F-xx sont préfixées de leur volume à chaque emploi** (décision 7 du TOC) — *ce chapitre est, avec le ch. 42, celui où la collision est la plus dense.* ⚠ **Trois des entrées mobilisées n'entrent PAS au socle consolidé, et la pièce le porte à leur emploi** : Vol. III **F-92** et **F-96** — *dette de vote adversarial non résorbée ; **non réfutées, non éprouvées*** — et Vol. III **H-15**, *les cinq points de contrôle obligatoires venant du texte rédigé du Vol. II et non de son socle.* ⚠ **Entrées [C] non élevables** : **H-31** (échelle d'autonomie) et les quatre sections du Vol. I sont des **constructions d'auteur de leur volume**, non des reprises de sources primaires tierces — *l'élévation en [B] par lecture de la source est sans objet, et elles n'entrent jamais comme faits.* **Aucun énoncé n'est central au sens de CA-IV-01** — *les entrées [C] l'interdisent, et **aucun vote adversarial n'a été conduit** sur celles qui n'en sont pas* |
| **Garde-fous balayés** | ⚠ **Règle de comptage, décision 16 du TOC** : les cardinaux ci-dessous portent sur le **marqueur littéral de l'identifiant** dans le **corps** de la pièce — de la première section à la synthèse, **en-tête et note de statut exclus** —, et ils sont **re-mesurés sur le corpus que le commit produit**. ⚠ **Un garde-fou appliqué sans que son identifiant soit écrit voit son DOMAINE déclaré, sans cardinal** (alinéa c) : *le domaine balayé est le corps entier, et les cardinaux antérieurs — qui comptaient les **applications** et non le marqueur — n'étaient re-mesurables par aucune règle écrite.* **Les deux séries sont balayées intégralement, zéros compris.** Vol. II — **réserve F-09 (« attendu par E-23 », jamais « exigé ») : deux occurrences**, § 43.1 et § 43.3 — ⚠ *la formule imposée est employée au-delà, aux § 43.1, § 43.3 et § 43.5 : **domaine déclaré, sans cardinal*** ; **réserve F-37 (préimpression non révisée) : deux occurrences**, § 43.3 ; **réserve F-01 (« cadre d'autorisation », jamais « sécurisé ») : une occurrence**, § 43.1 ; **réserve F-25 : une occurrence**, § 43.1 ; **R-2 (jamais « registre centralisé » pour un annuaire nommé) : une occurrence**, § 43.1 ; **R-3 (une spécification *s'appuie sur* un mécanisme, ne l'impose pas) : une occurrence**, § 43.1 ; **R-5 : une occurrence**, § 43.6 ; **R-8 (sigle jamais nu, quatre branches) : une occurrence**, § 43.4, **renvoyée au siège du ch. 7 § 7.5** ; **métriques auto-déclarées (marqueur « auto-déclaré ») : six occurrences**, § 43.1, § 43.2 (deux) et § 43.5 (trois) ; **R-1, R-4, R-6, R-7 : zéro occurrence** — *R-7 ressort en contexte réglementaire pur, aucune correspondance produit ↔ réglementation, filtré.* Vol. III — **R-09 : deux occurrences**, § 43.1 et § 43.6 ; **R-01 : une occurrence**, § 43.3 ; **R-06 : une occurrence**, § 43.4 ; **R-13 (échelle d'autonomie jamais nue) : une occurrence**, § 43.5, ⚠ **dont le SIÈGE de la désambiguïsation des trois échelles homonymes** — *le garde-fou y est appliqué à chaque rangée de la table du siège sans que l'identifiant soit répété* ; **R-02 et R-14 : zéro occurrence de l'identifiant** — ⚠ *les deux garde-fous sont pourtant tenus, les degrés d'absence étant portés en toutes lettres aux § 43.1 à § 43.6 : **domaine déclaré, corps entier, sans cardinal** (décision 16, alinéa c)*. **R-03 à R-05, R-07, R-08, R-10 à R-12 : zéro occurrence** |
| **Volumétrie cible** | ≈ **6 500 mots** de corps (§ 43.0 à la synthèse), **cible dérivée** de l'enveloppe du Livre (**69 000 mots**, TOC v0.25) au prorata des six sections et du volume de source consommé — *trois volumes y convergent, ce qui est le maximum du Livre.* ☑ **Décompte publiable depuis G-2** ; **réel reporté au [`README.md`](README.md)**. ⚠ **D-4 s'applique** |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) **v0.28**, entrée du chapitre 43 — **thèse réalignée en v0.28**, décisions 8 et 14, remontée R-IV-57)* — les Livres I-IV se composent en une architecture cible neutre à couches (protocoles, identité/registre, orchestration, maillage, exploitation, gouvernance) — ⚠ **fusion déclarée des quatre couches du Vol. II et des trois étages du Vol. III** —, structurée par OO1-OO4, avec **OO3/OO4** imposés sous exigence réglementaire stricte. ⚠ **L'extension de cette formule d'obligation à la fabrique d'identité est une CONSTRUCTION D'AUTEUR, déclarée telle** : *aucune des deux sources ne la porte, le Vol. III posant ses trois étages au titre de son cadrage et déclarant qu'aucune entrée ne les fonde.*

⚠ **La thèse portait, à la rédaction, un membre qu'aucune de ses deux sources ne porte, et il touchait
une formulation imposée — le réalignement est FAIT, et l'histoire de l'écart se conserve** (décision 17
du TOC, alinéa c). **Forme antérieure, v0.25** : « … structurée par OO1-OO4, avec OO3/OO4 **et la
fabrique d'identité** imposés sous exigence réglementaire stricte ». La thèse du Vol. II écrit :
« architecture cible neutre structurée par OO1-OO4, avec **OO3/OO4** imposés sous exigence
réglementaire stricte ». ⚠ **Le plan y ajoute « et la fabrique d'identité »**, et *ni le Vol. II ni le
Vol. III ne portent cet énoncé* : le Vol. III pose les trois étages **au titre de son cadrage, non de
son socle**, et déclare expressément qu'**aucune entrée ne porte cette architecture**. ⚠ **Et
l'addition est plus lourde qu'un simple ajout** : « imposé sous exigence réglementaire stricte » est
une **formule d'obligation**, or *le principe dont elle vient est lui-même une **Lecture de l'auteur**
du Vol. II, construite par transposition de trois sources dont le socle n'établit l'application ni au
Canada ni à la finance canadienne.* **Étendre une formule d'obligation à un objet qu'elle ne visait
pas est le geste que R-06 du Vol. III interdit sur E-23**, et la somme s'y tient. **Le corps a été
écrit sous la forme bornée** et l'écart avait été **remonté** (R-IV-57, § 43.7). ☑ **La remontée est soldée par l'arbitrage v0.28 du TOC** (décisions 8 et 14), et **la citation
ci-dessus porte la forme réalignée**, reportée **par copie** depuis l'entrée courante du plan.
*Les v0.29 et v0.30 du TOC ne modifient aucune thèse du Livre.*

⚠ **Un second point n'est pas un désalignement mais une fusion déclarée** : le plan porte **six
couches** là où le Vol. II en pose **quatre** ; les deux qui s'ajoutent — **maillage** et
**exploitation** — viennent des trois étages du Vol. III. *La fusion est légitime et c'est l'objet
même du chapitre ; elle se déclare plutôt qu'elle ne se lisse* (§ 43.1).

---

## § 43.0 — Ouverture : à quel titre une architecture de référence se construit

**Le ch. 42 s'achève sur un constat négatif** : quinze croisements, aucun lien documenté, **cinq zones
où l'architecture doit compenser**. **Ce chapitre construit — et doit dire d'abord à quel titre.**

⚠ **Une architecture de référence n'est pas une déduction du socle.** *C'est un ordonnancement : elle
range ce que le socle documente, elle nomme ce qu'il ne documente pas, et elle pose entre les deux des
liens qui sont d'un auteur.* D'où, comme au ch. 29, **plus d'inférences marquées que dans les
chapitres de fait**.

⚠ **Elle est en outre neutre : aucun composant d'éditeur n'y est prescrit.** L'instanciation sur un
portefeuille réel — retenu comme **cas documenté par sources primaires et non comme recommandation** —
est l'objet du **ch. 45**.

⚠ **Et le socle ne la porte pas davantage du côté du Vol. III.** Celui-ci pose ses trois étages **au
titre de son cadrage** et déclare : *« le socle ne documente pas d'architecture composant ces trois
étages — absence de documentation, non fait négatif vérifié »* (degré 3). **Ce que les socles portent,
ce sont les objets que les couches rangent et les bornes de chacun** ; *le découpage, l'ordre des
couches et la nature contractuelle de leurs relations sont d'un auteur.* ⚠ **Le lecteur peut refuser
le découpage sans qu'aucun des faits cités ne tombe.**

**Le chapitre se lit en six temps** : les couches et ce qu'elles portent (§ 43.1) ; où placer la main
qui commande (§ 43.2) ; les cinq points où l'architecture doit produire quelque chose (§ 43.3) ; le
patron qui les unifie (§ 43.4) ; la trajectoire par paliers (§ 43.5) ; et ce qui pourrait être fait
autrement (§ 43.6).

## § 43.1 — Les couches et leurs responsabilités

### 43.1.1 Six couches, et la fusion qui les produit

⚠ **La somme compose deux découpages, et elle le déclare.** Le Vol. II pose **quatre couches** —
protocoles, identité et registre, orchestration, gouvernance ; le Vol. III pose **trois étages** —
**fabrique d'identité**, **maillage**, **AgentOps** — et leurs contrats mutuels. **Les deux se
recouvrent partiellement** : *la fabrique d'identité du Vol. III est la couche « identité et registre »
du Vol. II vue par son producteur ; le maillage et l'AgentOps n'ont pas d'équivalent chez lui.*

⚠ **SIÈGE DE LA COLLISION « FABRIQUE » POUR TOUTE LA SOMME (décision 12c du TOC).** La **fabrique
d'identité** de ce paragraphe est **l'étage qui émet l'identité** ; la **fabrique d'agents** du
**ch. 41** est **le plan qui produit l'agent**. *Les deux sont des étages distincts de la même
architecture, et le mot ne les désigne jamais indistinctement.* ⚠ **Ni l'une ni l'autre n'est le
patron *factory* du catalogue de patrons, ni un titre d'éditeur** — le **ch. 41 § 41.1** porte la table
des quatre emplois, **que ce chapitre ne reconstruit pas**.

| Couche | Ce que les socles documentent | Responsabilité | Ce qu'elle ne porte pas |
|---|---|---|---|
| **Protocoles** | accès aux outils, données typées, **cadre d'autorisation** (Vol. II **F-01**) ; délégation de pair à pair, cartes signées (Vol. II **F-02**) ; complémentarité **déclarée par un projet**, et *un critère de découpage n'est pas une contrainte* (Vol. II **F-16**) ; protocole de transaction, **anatomie non portée** par ce socle (Vol. II **F-04**) | **format et habilitation à la frontière** : *qui parle, par quel format* | le processus, la trace d'instance, la décision, l'humain (**ch. 42**) |
| **Identité et registre** — *fabrique d'identité* | identités d'agents et gabarits d'identité sur des protocoles d'autorisation et d'authentification, **dont les flux étendent ces RFC plutôt qu'ils ne s'y conforment** (Vol. II **F-33**) ; spécification de registre, **brouillon** : profil ancré, énumération d'outils invocables, bornes de privilège (Vol. II **F-07**, **F-08** ; Vol. III **F-40**, **H-03**) | **nommer l'agent** ; **borner ses outils et ses droits hors de lui** | la conformité (statuts pré-normatifs) ; ⚠ **l'inventaire attendu par E-23, qui est un objet distinct** |
| **Orchestration** | taxonomie OO1-OO4, cinq propriétés, sept critères (Vol. II **F-36**) ; réalisations : flux à base de graphes, points de contrôle, humain dans la boucle (Vol. II **F-15**) | **tenir l'enchaînement ; produire la trace ; arrêter pour l'humain** | la qualification juridique du processus ; le contenu des cadres |
| **Maillage** | syntaxe d'autorisation par arête, **pré-version auto-déclarée** (Vol. III **F-71**, **F-70**) ; **écart de couverture entre deux plans d'identité déclaré par l'éditeur** (Vol. III **F-35**) | **appliquer la politique à l'arête** — **siège ch. 37** | l'émission ; ⚠ **la couverture du graphe, qui n'est établie par aucune entrée** |
| **Exploitation** — *AgentOps* | seize métriques **au grain de l'opération**, aucune de parc ; **dimension d'agent qui est un nom, pas une identité** (Vol. III **F-90** à **F-96**) — ⚠ *ces deux énoncés-là relèvent de **F-96** et **F-92**, **exclus du socle consolidé** pour dette de vote adversarial : **non réfutés, non éprouvés*** | **voir, boucler, mesurer** — **siège ch. 38-40** | ⚠ **la clé de jointure entre trace et mandat**, lacune ouverte |
| **Gouvernance** | E-23 : **cinq domaines d'attentes opératoires** (Vol. II **F-09**) ; ligne directrice de l'AMF : **le calendrier seul** (Vol. II **F-25**) ; avis 11-348 (**F-26**) ; article 12.1 (**F-27**) | **inventaire, cotation, cycle de vie, documentation, surveillance** | ⚠ **ce que l'AMF attend — non porté par le socle** |

: Tableau 43.1 — Les six couches de l'architecture de référence unifiée. ⚠ **Le découpage est imposé par le plan ; sa vertu est d'obliger à dire, couche par couche, ce que les socles documentent et ce qu'ils laissent vide.**

### 43.1.2 Quatre réserves qui commandent la lecture du tableau

*Un — la couche protocolaire.* ⚠ **« Cadre d'autorisation », jamais « sécurisé »** : *la sécurité
dépend de l'implémentation*, et le **ch. 8** en est le siège. **Lecture de l'auteur** — *de ces six
couches, la protocolaire est la mieux documentée et la moins porteuse pour un processus réglementé :
une spécification décrit un appel, et un appel n'est pas une décision.* ⚠ **Le choix d'un protocole ne
referme donc aucune des cinq zones de compensation du ch. 42.**

*Deux — la couche d'identité appelle son statut avant son contenu.* ⚠ **Le socle ne documente pas de
registre d'agents centralisé pour la capacité d'annuaire nommée**, et *la somme n'en écrira pas* :
absence de documentation, non fait négatif vérifié (R-2 du Vol. II). Le **registre gouverné** relève
d'une spécification dont **le statut interdit d'en faire un point d'appui** : **brouillon de
laboratoire, non norme ratifiée** (R-09 du Vol. III, statut dit à la mention), ⚠ **et elle *s'appuie
sur* un mécanisme d'identité de charge de travail sans que l'exigence stricte soit établie** (R-3 du
Vol. II).

⚠ **Et le socle IAM pré-agentique de cette couche n'est pas reconstruit ici** : *identité fédérée,
autorisation déléguée et identité de charge de travail sont **posées une seule fois pour toute la
somme au ch. 3 § 3.2 et § 3.3***. **Ce chapitre les transpose aux agents et n'en redémontre aucune** —
*c'est l'économie qui justifie la refonte des trois volumes en un ouvrage, et un chapitre
d'architecture qui la reconstruirait l'annulerait au premier paragraphe.*

**Lecture de l'auteur** — les deux champs obligatoires du **schéma de profil d'agent** — l'énumération
des outils invocables et les bornes de privilège (Vol. III **F-40**) — sont, dans le vocabulaire du
manifeste, un **cadre opérationnel** — *ce que l'agent peut faire, avec quels outils* — **écrit hors
de l'agent, dans un objet lisible avant l'exécution**. ⚠ **Le socle porte les deux termes ; il ne pose
pas le rapprochement**, et *l'état pré-normatif de la spécification interdit d'en tirer autre chose
qu'une direction.* ⚠ **Un second rapprochement est à écarter** : *un registre d'agents et l'inventaire
**attendu par** E-23 ne portent pas sur le même objet* — le premier recense des agents, le second des
modèles dont le risque inhérent est jugé non négligeable. **Les confondre prêterait au régulateur un
périmètre qu'il n'énonce pas.**

*Trois — la couche d'orchestration est celle où réside le cadre, donc celle où se joue tout ce
chapitre.* Le socle y documente, **au niveau d'un cadriciel d'orchestration et à aucun niveau
protocolaire**, les deux mécanismes qui la rendent possible : **les points de contrôle** et **l'humain
dans la boucle** (Vol. II **F-15**).

*Quatre — la couche de gouvernance est la seule dont le socle porte des attentes opératoires, et il ne
les porte que pour un texte sur deux.* Depuis l'extraction du texte intégral d'E-23, EN et FR, le
socle porte **cinq domaines** : cycle de vie à cinq volets « not necessarily sequential » ; inventaire
d'entreprise « accurate, evergreen » ; cotation graduée — « Each model should be assigned a model risk
rating » ; **documentation de modèle** ; surveillance continue visant « autonomous decision making,
autonomous re-parametrization ». ⚠ **La modalité commande la rédaction de toute cette couche** :
*E-23 est fondée sur des principes et rédigée au conditionnel — on écrit « attendu par E-23 », jamais
« exigé ».* ⚠ **Et « documentation de modèle » ou « inventaire », jamais « fiche de modèle »** — *zéro
occurrence dans le texte.*

**Lecture de l'auteur** — ⚠ **cette couche est spécifiable contre un texte et pas contre l'autre,
alors que les deux entreront en vigueur le même jour.** *L'asymétrie n'est pas dans le droit ; elle
est dans le socle*, et le **ch. 49** la reprend.

## § 43.2 — Le positionnement des options d'orchestration par cas d'usage

### 43.2.1 Le principe, et son statut

Le **ch. 29** a énoncé le principe directeur : ⚠ **sous exigence réglementaire stricte, le processus
est imposé de façon déterministe par le cadre, qui invoque les agents ; les agents n'orchestrent pas
le processus** — soit les positions **OO3 et OO4**.

**Lecture de l'auteur** — ⚠ **ce principe est construit par transposition de trois sources dont le
socle n'établit l'application ni au Canada ni à la finance canadienne.** *Il dit où placer la main qui
commande, non comment qualifier un processus.*

Le socle fournit pour cela **sept critères qualitatifs de sélection** — complexité du but, supervision
humaine, contraintes, action humaine, espace de décision, effort initial, maintenance (Vol. II
**F-36**). ⚠ **Deux avertissements les accompagnent.** *Un* : le socle écrit « contraintes » **sans
adjectif** — *les contraintes réglementaires en sont une espèce, non le genre ; un budget de latence
sur un rail de paiement en est une autre.* *Deux* : ⚠ **ces critères orientent un jugement sans
calculer de réponse** — *aucune pondération ni fonction de score ne les relie aux quatre options.*

⚠ **Le socle ne documente l'option d'orchestration d'aucun déploiement agentique canadien** : absence
de documentation, non fait négatif vérifié (degré 3). *Aucune passe n'a instruit l'architecture des
systèmes que le Livre III documente en production* — **et les trois classes ci-dessous ne sont pas des
architectures réelles** : elles sont construites à partir des seules **fonctions** que les sources
primaires décrivent.

### 43.2.2 Trois classes, et ce qui les distingue

**Classe 1 — la décision de crédit avec mémo à un souscripteur humain.** ⚠ **Métrique auto-déclarée,
attribuée à chaque occurrence et non vérifiée indépendamment** : **TD** déclare que son premier modèle
d'IA agentique, développé par **Layer 6**, effectue la pré-adjudication d'un prêt garanti par
l'immobilier et génère des mémos de synthèse pour les souscripteurs, **ramenant un traitement d'environ
quinze heures à moins de trois minutes** — ⚠ **résultats que la source qualifie elle-même de
préliminaires** (Vol. II **F-17**). **Lecture de l'auteur**, *sur la classe seulement* — **cinq des sept
critères y sont saturés**, et le principe du **ch. 29** y conclut à **OO3 ou OO4**. ⚠ **Le socle ne dit
pas où se positionne ce système, et la somme ne le déduit pas d'un gain de temps déclaré.**

**Classe 2 — l'acheminement autonome de courriels commerciaux.** ⚠ **Métrique auto-déclarée, attribuée
à chaque occurrence** : **Scotiabank** déclare que des capacités agentiques traitent de façon autonome
**environ 90 % d'environ 1 500 courriels par jour** en services bancaires aux entreprises, les cas
complexes étant escaladés (Vol. II **F-21**). **Lecture de l'auteur** — ⚠ **la classe est instructive
par ce qu'elle rend indécidable** : *un acheminement
est-il une « décision fondée exclusivement sur un traitement automatisé » au sens de l'article 12.1 ?*
**Le socle ne le dit pas, et la somme n'émet pas d'avis juridique.** Le critère « contraintes » ne se
remplit donc **pas par lecture d'un texte**, mais par **une qualification que l'institution doit
assumer** — ⚠ **et dont le positionnement dépend entièrement.** *La qualification précède
l'architecture.*

**Classe 3 — le paiement de grande valeur sur un rail à sémantique commune.** Le rail a **achevé sa
bascule** vers la norme de messagerie financière (Vol. II **F-28**). **Lecture de l'auteur** — *la
contrainte dominante y est d'une autre nature — non d'expliquer mais d'exécuter*, le rail imposant
**une forme de message et un budget de temps**. ⚠ *Un délai à tenir ne se confie pas à un composant
dont la durée d'exécution n'est pas bornée.* La conclusion — **l'agent observe, le rail exécute** —
est celle qu'instancie le **ch. 45 § 45.12**.

**Lecture de l'auteur** — ⚠ **les trois classes se distinguent non par leur degré d'automatisation,
mais par la nature de ce qui les contraint : *expliquer, qualifier, exécuter*.** Le socle établit les
sept critères et les faits de chaque classe ; **il n'établit ni cette tripartition, ni son
exhaustivité.**

### 43.2.3 La grille « quand agentifier, quand s'abstenir »

*← Vol. I* Monographie *§2.13.1, **arrivée** depuis le ch. 6. ⚠ Section en **[C]**.*

⚠ **La première discipline est de minimiser la surface agentique**, et le Vol. I l'énonce comme
**thèse d'un volume antérieur, à attribuer**. *Ne déléguer au modèle que ce que le code ne peut pas
tenir à sa place* : tant qu'un flux est connu d'avance, un **enchaînement déterministe** — où le code
orchestre la tuyauterie et le modèle ne sert qu'aux étapes irréductiblement linguistiques — **est
préférable à une boucle où le modèle pilote sa propre trajectoire**. ⚠ **Le réflexe par défaut est la
retenue** : *préférer le patron le plus contraint qui résout la tâche — un enchaînement avant un
agent, un agent unique avant un système multi-agents.* ⚠ **Agentifier est un choix qui doit se
justifier, pas un point de départ.**

⚠ **La grille intègre un résultat non négociable de son chapitre d'origine** : *dès que la triade
létale est réunie — données privées, contenu non fiable, canal de sortie —, l'injection d'invite n'est
pas évitable au niveau du modèle*, et la réponse est **une défense en profondeur, jamais une
« solution »**. ⚠ **Le siège de la triade est au ch. 19 § 19.2**, celui de la défense au **ch. 6
§ 6.5** ; *ce chapitre n'en reconstruit aucun.*

**Lecture de l'auteur** — ⚠ **la grille et la taxonomie OO ne répondent pas à la même question, et les
composer est un geste du compendium** : *la première demande **s'il faut** un agent, la seconde
**qui commande** quand il y en a un.* **Ce que le socle établit** : les deux instruments, chacun dans
son volume, à leur niveau. **Ce qu'il n'établit pas** : leur articulation — ⚠ *aucune entrée ne les met
en rapport*. La lecture proposée est **un ordre d'application** : *la grille d'abord, la taxonomie
ensuite ; agentifier ce qui doit l'être, puis décider qui commande.* Elle se réfute par la production
d'un cas où la position OO déciderait de l'opportunité d'agentifier.

## § 43.3 — Les points de contrôle obligatoires

> ⚠ **SIÈGE DES CINQ POINTS DE CONTRÔLE OBLIGATOIRES POUR TOUTE LA SOMME.** Ils sont **posés ici une
> seule fois**. Les **ch. 37, 38, 39, 41 et 45** les **citent** et **n'en reconstruisent aucun** ;
> *un chapitre aval qui reposerait la liste annulerait l'économie qui justifie la refonte des trois
> volumes en un ouvrage.*

⚠ **Précaution terminologique, reprise de la source et non résolue par la somme.** Le glossaire du
Vol. II réserve **« point de contrôle »** à la traduction de *checkpointing* — *la persistance de
l'état d'un flux agentique* — alors que le titre de cette section désigne **autre chose** : *les points
où l'architecture doit obligatoirement porter une garantie.* Le second peut s'implémenter par le
premier ; **la somme écrit « point de contrôle obligatoire » pour la seconde notion**. ⚠ **La collision
est signalée par le Vol. II, signalée à son tour par le Vol. III, et signalée ici — trois fois, jamais
résolue** : *elle relève du glossaire de son volume d'origine, que la somme ne modifie pas.*

**Ces points ne sont pas déduits d'une source : ce sont les cinq zones de compensation du ch. 42,
chacune assignée à la couche qui doit la porter.** ⚠ **Quatre deviennent ici des points de contrôle
obligatoires ; la cinquième — l'interface d'accès du cadre bancaire — n'en est pas un, faute
d'objet** : *aucun organisme de normalisation technique n'a été désigné et aucun standard n'est nommé
dans les textes officiels.* Elle est **une frontière d'abstraction** (§ 43.6). **Un cinquième point
s'ajoute, issu non d'une zone mais de la table de traduction du ch. 29. Total : cinq.**

| # | Point de contrôle obligatoire | Ce que le socle porte | Ce qui est de l'auteur |
|---|---|---|---|
| **PC1** | **L'événement de décision** | l'art. 12.1 **impose** d'informer « au plus tard au moment de la décision » — **seule des trois obligations à ne pas être subordonnée à une demande** (Vol. II **F-27**) | *le moment de la décision doit être un **événement daté**, émis par la couche d'orchestration* — ⚠ **un système qui ne sait dire quand la décision a été prise ne peut satisfaire une obligation qui se déclenche à cet instant** |
| **PC2** | **La trace d'instance, produite par le cadre** | l'art. 12.1 exige, sur demande, « les raisons, ainsi que les principaux facteurs et paramètres » — **l'objet est l'instance** ; la journalisation confiée aux agents « n'est généralement pas recommandée » (Vol. II **F-37**, ⚠ **préimpression non révisée, source unique**) ; **les relations causales entrées-sorties sont souvent indéterminables** (Vol. II **F-10**) | **quatre producteurs candidats, trois écartés** — *l'agent par la préimpression, le modèle par le rapport conjoint, **le protocole par la matrice du ch. 42**, dont le typage donne un substrat de frontière et non une trace d'instance.* ⚠ **La trace revient au cadre ; aucune source ne désigne ce producteur, l'élimination est de l'auteur** |
| **PC3** | **Le point d'arrêt humain** | l'art. 12.1 exige l'occasion de présenter ses observations à **un membre du personnel « en mesure de réviser la décision »** ; ⚠ **le socle ne documente d'humain dans aucun protocole** — il le documente au niveau d'**un** cadriciel d'orchestration (Vol. II **F-15**) | *un point d'arrêt ne vaut que si **les effets aval de la décision sont bornés**, donc défaisables* — ⚠ **le socle ne l'énonce pas**, et le versant *sémantique d'effet* est au **ch. 48** |
| **PC4** | **La séparation de l'adaptation et de l'évolution** | le manifeste scinde l'auto-modification en **adaptation éphémère** et **évolution persistante** (Vol. II **F-36** ; Vol. III **H-11**) ; l'avis 11-348 capte l'adaptativité **après déploiement** (**F-26**) ; E-23 **attend** une surveillance visant la re-paramétrisation autonome (**F-09**) | *un système qui traite les deux régimes par le même chemin technique rend **indétectable, dans ses journaux, le moment où une exception est devenue une règle*** — ⚠ **aucune des trois sources ne l'énonce ; leur conjonction est de l'auteur** |
| **PC5** | **Le confinement local** | le manifeste pose l'opérationnalisation **locale** des cadres comme frontière de sécurité et de confidentialité — **confinement, non prévention** ; il nomme aussi le **paradoxe de confidentialité de l'explicabilité** (Vol. III **H-11**) | ⚠ **ce que PC2 exige d'exposer, PC5 exige de restreindre** — *l'arbitrage se documente, il ne se déclare pas résolu* |

: Tableau 43.2 — Les cinq points de contrôle obligatoires, avec ce que le socle porte et ce qui est de l'auteur. ⚠ **SIÈGE UNIQUE** ; les chapitres aval y renvoient sans le reconstruire.

**Lecture de l'auteur** — ⚠ **ces cinq points partagent une propriété que le Livre III nomme.**
**Quatre des cinq propriétés d'évaluation** du cadre mobilisé — spécificité de tâche, **assurance de
correction**, réactivité, **traçabilité** — sont **celles que l'exploitant démontre à un tiers**, et ce
sont exactement celles que le cadre instrumente ; ⚠ **la cinquième, l'autonomie, n'a au socle aucune
métrique** (Vol. II **F-37** ; constat repris au **ch. 39 § 39.2**, siège). *Les cinq points relèvent
tous du premier registre : **chacun est un endroit où l'exploitant doit pouvoir produire quelque
chose**, non un endroit où le système doit être bon.*

⚠ **Et le passeport n'y est pas un prérequis** : *il ne figure dans aucune spécification à date*
(R-01 du Vol. III ; siège **ch. 16**). **Les cinq points sont opposables sans lui** ; *c'est ce qui les
distingue des huit principes directeurs du blueprint, dont le premier conditionne l'admission à un
artefact que personne ne délivre* (**ch. 45 § 45.1**).

## § 43.4 — Le plan de contrôle d'agents comme architecture de référence

*← Vol. I* Monographie *§4.12.1 et §5.12.1 — **arrivées** depuis les ch. 24 et 34. ⚠ Section en
**[C]** de bout en bout.*

⚠ **Désambiguïsation obligatoire, à chaque emploi** (R-8 du Vol. II) : **« plan de contrôle
d'agents » s'entend ici au sens du patron d'architecture**, et **l'encadré des quatre branches de la
collision siège au ch. 7 § 7.5** — *ce chapitre y renvoie et ne le reconstruit pas.* ⚠ **Le sigle
correspondant ne s'emploie jamais nu.**

**Le Vol. I décrit un patron dont il tire la valeur de référence d'une convergence.** ⚠ **Repérage
[C], thèse d'un volume antérieur à attribuer** : *plusieurs analystes et fournisseurs y formalisent,
sous des libellés voisins, un plan de contrôle à couches, et un éditeur en fait le positionnement d'un
produit nommé.* ⚠ **La somme reprend le principe, jamais l'instanciation sur des produits nommés** —
*c'est le régime imposé au Vol. III et repris ici.*

**Le principe directeur qui unifie ces propositions est cité pour lui-même** : ⚠ ***séparer
l'intelligence de l'autorité, la capacité de la permission, l'explication de la preuve — ne jamais
laisser le modèle qui décide être aussi celui qui s'auto-autorise ou s'auto-atteste.***

**Lecture de l'auteur** — **ce que le socle établit** : que ce principe est **énoncé** par un volume
antérieur, en [C], et qu'il converge avec **les cinq points de contrôle obligatoires du § 43.3**, dont
il est la formulation abstraite. **Ce qu'il n'établit pas** : *que cette convergence soit un fait du
domaine plutôt qu'un effet du corpus consulté* — ⚠ **le Vol. I ne balaie pas les propositions
divergentes**, et **le socle du Vol. III ne porte aucune entrée sur ce patron** : absence de
documentation, non fait négatif vérifié (degré 3). *Une convergence relevée sur les sources qu'on a
ouvertes est une propriété de la lecture avant d'être une propriété du monde.*

⚠ **La déclinaison en finance régulée porte une formule que la somme borne, et c'est le point le plus
sensible de la section.** Le Vol. I écrit qu'en finance régulée cet enchaînement — *point d'application
unique et obligatoire par lequel transite toute action, sans chemin de contournement* — **« est
réglementairement exigé »**. ⚠ **La somme ne reprend pas cette qualification telle quelle** : *le socle
du Vol. II établit qu'E-23 est **fondée sur des principes** et rédigée au conditionnel, et R-06 du
Vol. III interdit d'écrire « exigé » là où le texte **attend**.* **La forme retenue est donc** : *le
Vol. I qualifie cet enchaînement d'exigence réglementaire ; le socle du Vol. II établit une **attente**
et non une exigence, et l'écart entre les deux n'est pas arbitré ici* — ⚠ **il est signalé**, et il
relève de la collation de fond.

**Ce que le Vol. I attache à ce point d'application est en revanche repris, en [C] et sous
attribution** : il y fait converger **quatre fonctions** — *identification de l'acteur, autorisation
calibrée sur la matérialité et la réversibilité, ségrégation des tâches et double regard, et
journalisation infalsifiable opposable en audit* —, ⚠ **et il pose un couplage obligatoire au registre
de modèles** : *un agent matériel qui décide est un modèle au sens des cadres de risque de modèle.*
**Lecture de l'auteur** — ⚠ **c'est exactement le rapprochement que le § 43.1.2 a écarté** : *un
registre d'agents et un inventaire de modèles ne portent pas sur le même objet.* **Les deux énoncés ne
sont pas contradictoires** — *le Vol. I dit qu'un agent décisionnel **relève** d'un inventaire de
modèles, non que le registre d'agents **soit** cet inventaire* —, **mais la distance entre les deux est
exactement là où une lecture rapide produirait un doublon d'autorité.** *La somme écrit les deux et ne
les fond pas.*

## § 43.5 — Le modèle de maturité de l'entreprise agentique

> ⚠ **SIÈGE DU MODÈLE DE MATURITÉ ET DE LA DÉSAMBIGUÏSATION DES TROIS ÉCHELLES D'AUTONOMIE, POUR TOUTE
> LA SOMME.** Ils sont **posés ici une seule fois**. Les **ch. 39, 40, 41 et 46** y renvoient et
> **n'en reconstruisent aucun** ; ⚠ *le ch. 39 § 39.6 s'abstient explicitement d'en produire un
> autre.*

Lecture de l'auteur — **marquage porté à l'ouverture de la section, qui est une construction d'auteur
en totalité.** **Ce que le socle établit** : l'existence et le contenu de **l'échelle d'autonomie
mobilisée**, à son niveau et sous ses réserves ; l'état de chacun des objets rangés dans les six
couches. **Ce qu'il n'établit pas** : *qu'une trajectoire de déploiement existe* ; *que les exigences
d'identité, de maillage et d'exploitation s'ordonnent par paliers* ; *que le coût d'une question sans
réponse croisse avec le palier d'autonomie consentie.* ⚠ **Le socle ne documente aucun modèle de
maturité de l'entreprise agentique** : absence de documentation, non fait négatif vérifié (degré 3).

⚠ **La section a été réaffectée à sa source le 21 juillet 2026, et le motif se déclare.** Elle
confrontait **trois modèles de maturité d'un corpus d'appui dont aucun des trois ouvrages n'a jamais
été déposé** — **le lot est clos par échec documenté, réversible par dépôt ultérieur**, et **aucun
modèle source n'est plus rapporté**. ⚠ **Le risque a changé de nature sans disparaître** : *la
tentation devient de combler par la construction ce que le retrait a vidé*, et **la parade est le
présent marquage, appliqué sans indulgence**. ⚠ **Les mentions de « corpus d'appui » sont des
marqueurs conditionnels de réouverture, jamais des sources.**

### 43.5.1 L'échelle, citée au complet — et les deux autres dont il faut la séparer

**Selon la proposition du Vol. I**, l'**échelle à quatre paliers non numérotés** — *assistance →
copilote → orchestration sous revue → autonomie bornée* — **indexe l'autonomie consentie sur le
produit matérialité × réversibilité**, non sur la capacité brute du modèle ; l'entrée qui la porte en
rapporte le principe : ⚠ ***un agent ne doit jamais exécuter une action irréversible sans garde-fou
structurel ; la règle est la préparation par l'agent et la libération humaine sur l'action
irréversible*** (Vol. III **H-31**, **[C]**).

⚠ **TROIS ÉCHELLES COEXISTENT AU VOL. I ET PARTAGENT LEURS LIBELLÉS — les nommer nues est proscrit**
(R-13 du Vol. III).

| Échelle | Cardinal et numérotation | Où elle vit dans la somme |
|---|---|---|
| **échelle à quatre paliers non numérotés** | *assistance, copilote, orchestration sous revue, autonomie bornée* — **quatre, sans numéros** | **ce paragraphe**, et le **ch. 14 § 14.4** pour son croisement avec la grille |
| **continuum à six niveaux numérotés de 0 à 5** | **six, numérotés 0-5** ; « copilote » y est le **niveau 2** | **ch. 4 § 4.1.4** |
| **graduation à quatre niveaux préfixés L** | **quatre, L0-L3** ; « copilote » y est le **niveau L0** | **Annexe H** |

: Tableau 43.3 — Les trois échelles d'autonomie homonymes du Vol. I. ⚠ **« Copilote » désigne un palier de la première, le niveau 2 de la deuxième et le niveau L0 de la troisième** : *le terme ne s'emploie jamais seul.* ⚠ **L'indexation sur matérialité × réversibilité ne discrimine pas davantage** — la graduation L0-L3 indexe deux de ses niveaux sur les mêmes critères. **Seuls le cardinal et la numérotation discriminent.**

⚠ **L'entrée qui porte la première est en [C] et NON ÉLEVABLE**, et la conséquence est structurante :
*l'échelle est une **construction d'auteur du Vol. I**, introduite par « La proposition de
l'ouvrage… », non la reprise d'une source primaire tierce — **l'élévation en [B] par lecture de la
source est sans objet**.* Elle entre comme **thèse d'un volume antérieur, à attribuer à chaque
emploi**, jamais comme fait. ⚠ **Le croisement qui suit ne peut donc rien établir ; il ordonne.**

### 43.5.2 Le croisement par palier, et ce qu'il ordonne

⚠ **Ce que cette section ajoute au ch. 14 § 14.4, et ce qu'elle en reprend.** Le ch. 14 § 14.4 a croisé
**les cinq questions** avec cette même échelle et a ordonné les **exigences d'identité** par palier.
**La colonne « identité » ci-dessous en est la reprise et ne la refait pas.** *Ce que ce paragraphe
ajoute est le croisement avec les **autres couches** — ce qu'un palier exige du maillage et de
l'exploitation —, et la lecture qui en découle : **à chaque palier, la dette contractée n'est pas la
même selon la couche**.*

| Palier *(échelle à quatre paliers non numérotés ; H-31, [C])* | Identité exigible *(reprise du ch. 14 § 14.4)* | Maillage exigible | Exploitation exigible | Ce que le socle offre, et ce qu'il n'offre pas |
|---|---|---|---|---|
| **assistance** — l'humain engage chaque action | **Q-A** : *sans identifiant, la trace ne s'impute à rien* | **le point d'application est l'humain qui engage** : l'autorisation par arête n'est pas requise | une trace **rattachable à la personne qui engage** | **offre** : une signature démontrant l'intégrité d'un contenu canonicalisé au regard d'une clé. ⚠ **n'offre pas** : l'obligation de signer — *la signature est facultative* |
| **copilote** *(palier de cette échelle-là — quatre paliers **non numérotés** ; jamais le niveau 2 du continuum 0-5 ni le niveau L0 de la graduation L0-L3)* | **Q-B** s'ajoute : *contresigner ce qu'on n'a pas produit suppose de savoir qui l'a produit* | **le contresignataire tient lieu de point d'application** ; la couverture des arêtes n'est pas encore en cause | **la détection d'un changement d'outil entre deux contresignatures** | ⚠ **n'offre rien qui ancre la confiance** — *l'ancrage est renvoyé hors du protocole* ; et **ni version, ni empreinte, ni signature au type décrivant un outil** |
| **orchestration sous revue** — la revue porte sur une chaîne | **Q-C** devient centrale : *une chaîne qui ne s'interroge qu'à l'admission ne soutient pas une revue portant sur l'exécution* | **le point d'application par arête devient exigible** — *c'est le lieu où une chaîne se vérifie à chaque saut* | **la corrélation entre la trace et la chaîne de mandat** | **offre** : un format de mandat versionné, l'expression de la délégation par un attribut normalisé, une syntaxe d'autorisation par arête. ⚠ **n'offre pas** : l'interrogeabilité à l'instant *t* ; **la clé de jointure** (ch. 38 § 38.5) ; et *la propagation borne elle-même sa portée à un domaine de confiance* |
| **autonomie bornée** — plus aucun acte n'est contresigné à l'unité | **les cinq questions, simultanément** | **la couverture du graphe devient la question opérante** (ch. 37 § 37.5) | **la boucle complète** : évaluer, détecter, répondre, réviser (ch. 39) — ⚠ **et la réémission du gabarit**, qui n'a pas de socle (ch. 41 § 41.5) | ⚠ **n'offre ni révocation outillée, ni délai de propagation, ni métrique de parc** — *les trois manques se cumulent au palier où ils coûtent le plus* |

: Tableau 43.4 — Le croisement des quatre paliers avec trois couches. ⚠ **Construction d'auteur en totalité** ; *aucun palier n'est porté par une entrée de socle.*

**Lecture de l'auteur** — ⚠ **le croisement ne rend aucun mécanisme suffisant à un palier bas.** *Un
fait borné ne varie pas avec le palier* : la section d'une spécification qui ne comporte aucun moyen
d'établir le statut d'une clé n'en comporte pas plus pour un agent d'assistance que pour un agent en
autonomie bornée. ⚠ **Le palier change le coût du défaut, non le défaut** — et *une entreprise qui
ordonnerait ses exigences par palier accepterait, en connaissance de cause, de porter aux paliers bas
une dette dont l'échéance est le palier suivant.*

### 43.5.3 La feuille de route par plateaux, et l'écart entre ambition et déploiement

*← Vol. I* Monographie *§5.12.2 — **arrivée** depuis le ch. 34 — et §6.10, **prélevé au ch. 44**, qui
traite par ailleurs son chapitre d'origine en bloc. ⚠ **[C]**.*

Le Vol. I modélise la trajectoire comme **une suite ordonnée de paliers** — *un état de référence, des
états intermédiaires, un état cible* —, chacun **agrégeant un jeu d'incréments de capacité**, ⚠ **et
il pose la règle qui compte** : *un palier ne se franchit qu'en débloquant un jeu de **contrôles
vérifiables**, non en empilant des fonctionnalités.* ⚠ **L'instrument est nommé et daté** : *c'est une
transposition du **modèle LCIM** — Wang, Tolk et Wang, 2009 — aux agents, et la somme n'en est ni
l'auteur ni le dépositaire.* **Lecture de l'auteur** — ⚠ *c'est le même énoncé que le § 43.3 sous une
autre forme : **chaque palier est un endroit où l'exploitant doit pouvoir produire quelque chose**.*

**Sa transposition financière déplace l'axe de lecture** : ⚠ *chaque palier ne débloque pas seulement
des capacités d'interopérabilité, il débloque surtout des **contrôles**.* Le Vol. I situe **la
réduction de risque la plus forte non au sommet de cette grille mais à son passage intermédiaire** —
*là où l'application de politique et les contrôles d'accès deviennent **systématiques et non plus
ponctuels***. ⚠ **Repérage [C], thèse attribuée** : *une institution qui pousse l'autonomie sans avoir
franchi ce palier accumule du risque non gouverné.*

⚠ **L'écart entre ambition et déploiement encadre la lecture, et chacun de ses chiffres est
auto-déclaré et attribué.** Le Vol. I rapporte, **tous de statut analyste ou enquête et marqués
ressources vivantes à re-vérifier** : *environ un tiers des organisations à un niveau de maturité 3 ou
supérieur ; une quasi-totalité qui **prévoient** des déploiements ; environ un déploiement sur dix
réellement en production* — écart que les analystes nomment le **purgatoire des pilotes**. **D'autres
enquêtes qu'il cite avancent des chiffres plus bas encore, également auto-déclarés et nommément
attribués** : *les enquêtes de **McKinsey/QuantumBlack** (2025) et le rapport **MIT NANDA**
(Challapally et coll., 2025).* ⚠ **Aucune de ces grandeurs n'est vérifiée indépendamment, aucune n'est
reprise comme fait, et la somme n'en dérive rien.** *Ce qu'elles éclairent est une chose et une
seule* : **la gouvernance est régulièrement citée comme blocage principal** — ⚠ *ce qui, s'il fallait
le retenir, validerait a contrario le patron du
palier intermédiaire : **c'est l'absence de contrôles, non l'insuffisance des modèles, qui retiendrait
les déploiements**.* **Lecture de l'auteur, et elle est faible par construction** : *un constat tiré
d'enquêtes auto-déclarées ne vaut pas mieux que ses sources.*

## § 43.6 — Alternatives, variantes et frontières d'abstraction

**Cette architecture est neutre ; elle n'en est pas moins réalisable, et le socle documente de quoi.**

**Pour la couche d'orchestration, trois réalisations sont au socle**, et **chacune porte son statut à
la mention** (R-09 du Vol. III) : *un cadriciel d'éditeur en **disponibilité générale**, portant les
flux à base de graphes, les points de contrôle et l'humain dans la boucle* (Vol. II **F-15**) ; *une
plateforme dont **le support d'un protocole n'est confirmé de première main que pour son offre
commerciale**, non pour sa bibliothèque ouverte* (Vol. II **F-32**) ; *une
orchestration événementielle dont les capacités agentiques déclarent un appel d'outils natif et une
intégration en **préversion ouverte**, ⚠ **sans qu'aucun client ni chiffre d'adoption ne figure à la
source*** (Vol. II **F-33**). ⚠ **Deux autres cadriciels sont au socle en [C] et ne portent aucun fait
central ici.** *Le ch. 23 les traite ; ce chapitre les nomme comme réalisations documentées, jamais
comme recommandations.*

⚠ **Une seule de ces réserves engage ce chapitre.** Le socle documente **des limites connues du
magasin de points de contrôle d'un cadriciel nommé en déploiement distribué** (Vol. II **F-15**).
**Lecture de l'auteur** — ⚠ *la persistance de l'état est le mécanisme dont dépend **PC3**, le point
d'arrêt humain* ; **le socle ne relie ce magasin à aucun des autres points**. *Une limite connue de ce
mécanisme est un **risque d'architecture**, non un détail d'exploitation.*

**La frontière d'abstraction, elle, est la cinquième zone du ch. 42 — celle qui n'est pas devenue un
point de contrôle.** ⚠ **Aucun organisme de normalisation technique n'a été désigné par arrêté
ministériel et aucun standard n'est nommé dans les textes officiels** ; *la candidature d'un format
d'industrie relève du **commentaire d'industrie***, attribué comme tel (R-5 du Vol. II, formulation
imposée). **La discipline qui en découle est celle du ch. 32** : *traiter le standard d'accès comme une
variable derrière une frontière d'abstraction.* ⚠ **Ce n'est pas un choix de protocole agentique** —
*aucun n'est nommé dans les textes.*

**Lecture de l'auteur** — ⚠ **une frontière d'abstraction n'est pas un point de contrôle, et les
confondre coûterait deux fois.** *Un point de contrôle est un endroit où l'architecture **doit
produire** quelque chose ; une frontière d'abstraction est un endroit où elle **doit pouvoir changer
d'avis** sans se refaire.* **Ce que le socle établit** : l'absence de désignation, **par balayage
documenté**. **Ce qu'il n'établit pas** : que cette absence dure, ni qu'une désignation future soit
compatible avec l'un des protocoles de la pile.

## Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur.*

1. **Les six couches, et leur statut de découpage.** ⚠ **Fusion déclarée de quatre couches et de trois
   étages** ; *le socle porte les objets rangés, jamais le rangement.* Le **ch. 45** l'instancie
   couche par couche, le **ch. 44** le formalise.
2. **La collision « fabrique », posée ici pour la somme.** ⚠ *La fabrique d'identité **émet** ; la
   fabrique d'agents du ch. 41 **produit**.* **Siège de la distinction** ; la table des quatre emplois
   reste au **ch. 41 § 41.1**.
3. ⚠ **SIÈGE : les cinq points de contrôle obligatoires.** Posés **une seule fois**. Les **ch. 37, 38,
   39, 41 et 45** y renvoient. *Chacun est un endroit où l'exploitant doit pouvoir **produire** quelque
   chose, non un endroit où le système doit être bon* — **et aucun ne suppose le passeport**.
4. ⚠ **SIÈGE : le modèle de maturité et les trois échelles d'autonomie.** Posés **une seule fois**,
   avec leur cardinal et leur numérotation. Le **ch. 39 § 39.6 s'abstient explicitement d'en produire
   un autre** ; le **ch. 40 § 40.6** y renvoie pour départager les trois échelles homonymes.
5. **L'ordre d'application de deux instruments.** *La grille « quand agentifier » d'abord, la taxonomie
   OO ensuite.* ⚠ **Construction du compendium, réfutable.**
6. **La distinction point de contrôle / frontière d'abstraction.** *Produire quelque chose, contre
   pouvoir changer d'avis.* Le **ch. 45 § 45.13** instancie la seconde, le **ch. 46** séquence
   l'instrumentation des cinq premiers.

⚠ **Ce que le chapitre ne lègue pas.** Aucune **prescription de composant** : *l'architecture est
neutre, et les réalisations sont des cas documentés.* Aucune **qualification juridique** : *la
qualification précède l'architecture, et elle appartient à l'institution.* Aucune **exigence** là où
les textes portent une **attente** — ⚠ **et l'écart entre « exigé » et « attendu » est le point où ce
chapitre a dû borner sa propre source**. Et aucun **modèle de maturité fondé** : *le socle n'en
documente aucun, le corpus d'appui a été retiré, et ce qui reste est une construction marquée.*

---

## § 43.7 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle consigne l'écart de
gouvernance sous lequel la pièce a été rédigée (PRD, Annexe A).

**Ce qui est enfreint.** Portes **G-3**, **G-4** et **G-5** ; **volet résiduel de G-1** ; **ordre de
rédaction du PRD §6**. Instruction d'auteur du **27 juillet 2026**. ⚠ **G-3 a depuis été franchie —
28 juillet 2026 —, et cela ne rattrape pas la pièce** : *elle a été écrite sans socle consolidé, et son
ré-adossement aux `S-nnn` reste dû.* **G-4 et G-5 demeurent ouvertes.**

1. **Aucun énoncé n'est central au sens de CA-IV-01.** ⚠ **Et ce chapitre est celui du Livre où la
   proportion d'inférences marquées est la plus haute** : *une architecture de référence range, nomme
   et relie — les liens sont d'un auteur, et le socle ne porte que les objets rangés.*
2. **Les décomptes sont publiables** (G-2) ; le réel est reporté au [`README.md`](README.md).
3. **Les renvois « ch. N » : état FINAL de la passe, et non ordre d'écriture.** ⚠ *La forme
   antérieure de ce point photographiait l'instant où cette pièce a été écrite et déclarait « ne
   sont pas rédigés : ch. 44 et ch. 45 » — alors que **la même passe les a écrits ensuite** ; elle
   est corrigée ici sur l'état que le commit produit.* **Les dix chapitres du Livre IV (ch. 37 à
   46) sont rédigés**, comme le sont les **cinquante chapitres des cinq Livres** : *tous les
   renvois « ch. N » de cette pièce résolvent donc contre du texte.* ⚠ **Les renvois vers les
   ANNEXES restent des renvois de plan** — *aucune annexe du compendium n'est rédigée*, l'annexe H
   comprise. ⚠ **Ce qui reste vrai de la forme antérieure, et qui est daté** : à l'heure où ce
   chapitre a été écrit, n'étaient rédigés ni les ch. 23, 29, 32 et 34 du Livre III, ni les ch. 48
   et 49 du Livre V, non plus que les ch. 44 et ch. 45 — *les renvois qui les visent ont été posés
   comme renvois de plan et n'ont pas été re-vérifiés contre le texte paru après eux.* ⚠ **Et «
   résoudre contre du texte » ne vaut pas recevabilité** : *le texte visé est lui-même un
   brouillon hors portes.*
4. **TROIS sièges sont posés par cette pièce**, et non deux : les cinq points de contrôle obligatoires
   (§ 43.3), le modèle de maturité avec les trois échelles (§ 43.5), ⚠ **et la collision « fabrique »
   (§ 43.1, décision 12c du TOC)** — *ce dernier porte la forme pleine du marqueur et n'avait pourtant
   pas été compté.* ☑ **Les TROIS sont versés à [`PRD/check-sieges.py`](../PRD/check-sieges.py)** —
   constaté sur pièce le 28 juillet 2026 : *la table porte **vingt-six sièges**, et le troisième —
   la collision « fabrique » — y est entré ce jour-là comme **marqueur orphelin**, avec celui du
   ch. 44 § 44.6.* ⚠ **Cette pièce n'atteste que ce qu'elle a constaté** : *l'entrée de table et le
   rejeu du harnais relèvent de la passe qui verse, non de celle-ci ; un marqueur de siège qu'aucune
   table ne contrôle laisserait passer une reconstruction ailleurs dans la somme.*
5. **CA-IV-13 n'est pas satisfaite** — aucune relecture par un relecteur distinct du rédacteur.

**Remontées ouvertes par ce chapitre :**

- **R-IV-57 — non bloquante, de thèse, et elle touche une formulation imposée.** La thèse du ch. 43 au
  TOC v0.25 porte « avec OO3/OO4 **et la fabrique d'identité** imposés sous exigence réglementaire
  stricte ». ⚠ **Aucune des deux sources ne porte cet énoncé** : la thèse du Vol. II s'arrête à
  « OO3/OO4 », et le Vol. III pose ses trois étages **au titre de son cadrage**, en déclarant
  expressément qu'**aucune entrée ne porte cette architecture** (degré 3). ⚠ **Et l'addition est plus
  lourde qu'un ajout de portée** : *« imposé sous exigence réglementaire stricte » est une formule
  d'obligation, et le principe dont elle vient est lui-même une **Lecture de l'auteur** du Vol. II,
  construite par transposition de trois sources dont le socle n'établit l'application ni au Canada ni
  à la finance canadienne.* **Demande remontée** : réalignement au titre des **décisions 8 et 14**,
  et — *si l'extension à la fabrique d'identité est voulue* — **qu'elle soit déclarée construction
  d'auteur à la ligne Fusion**, comme le TOC le fait pour le ch. 41.
  ☑ **Issue, 27 juillet 2026** — **TOC, décisions 8 et 14** — « **et la fabrique d'identité**
  imposée sous exigence réglementaire stricte » : ⚠ **l'extension est déclarée construction
  d'auteur à la ligne Fusion**, *aucune des deux sources ne la portant, et « imposé » étant une
  formule d'obligation que R-06 borne.* **La citation en tête de cette pièce porte la forme
  réalignée** (décision 17 du TOC).
- **R-IV-58 — non bloquante, de divergence entre volumes, et elle n'est PAS une contradiction.** Le
  **Vol. I** qualifie le point d'application unique et obligatoire en finance régulée d'enchaînement
  **« réglementairement exigé »** (§ 43.4). Le **socle du Vol. II** établit qu'E-23 est **fondée sur
  des principes**, ses douze énoncés numérotés au conditionnel, et **R-06 du Vol. III interdit
  d'écrire « exigé » là où le texte attend**. ⚠ **Les deux énoncés ne sont pas logiquement
  incompatibles** — *le Vol. I peut viser un autre corpus réglementaire que le canadien, qu'il ne
  nomme pas à cet endroit* —, **mais la somme ne peut pas reprendre la formule du Vol. I sans
  enfreindre une formulation imposée**. La pièce **écrit les deux états et ne les arbitre pas**.
  **Demande remontée** : que **la collation de fond (G-4) inscrive ce couple à son domaine** et
  détermine si le Vol. I vise un corpus que le Vol. II ne balaie pas. ⚠ *C'est une lacune de
  couverture apparente, non une contradiction ; et le volume le plus ancien ne se corrige pas.*
  ☑ **Issue, 27 juillet 2026** — **PRD, domaine de G-4** — le couple « le Vol. I écrit
  *réglementairement exigé* / le Vol. II établit une **attente** » entre au domaine ; ⚠ **ce
  n'est pas une contradiction** : *lacune de couverture apparente, et le volume le plus ancien
  ne se corrige pas.*
- **R-IV-59 — non bloquante, de dette d'appareil, ET ELLE EST DUE PAR CETTE PASSE.** Ce chapitre pose
  **deux sièges neufs** — les cinq points de contrôle obligatoires et le modèle de maturité avec la
  désambiguïsation des trois échelles. ⚠ **Cinq chapitres déjà rédigés y renvoient** (ch. 37, 38, 39,
  40, 41), *et aucun contrôle outillé ne vérifie qu'ils n'en reconstruisent aucun.* **Demande
  remontée** : **versement des deux sièges à la table `SIEGES` de `check-sieges.py`**, avec **rejeu du
  harnais de mutation**, avant tout commit de clôture du Livre. ⚠ *La table est passée de trois à sept
  sièges avec le Livre II, et le versement y avait trouvé un défaut réel au premier passage — dont un
  siège qui ne résolvait pas contre lui-même.*
  ☑ **Issue, 27 juillet 2026** — **appareil** — les **trois sièges du Livre** versés à la table
  des sièges du contrôle inter-pièces, **harnais de mutation rejoué** ; ⚠ **deux défauts réels
  trouvés au premier passage**, dont *un chapitre qui touchait la matière d'un siège sans y
  renvoyer*. ⚠ **Ce que cette clôture avait manqué** : *deux marqueurs de siège du Livre — la
  collision « fabrique » (ch. 43 § 43.1) et la conformité traçable (ch. 44 § 44.6) — **n'avaient
  été ni comptés ni versés***. ☑ **Leur versement est FAIT** — *constaté sur pièce le 28 juillet
  2026 : les deux entrent à la table comme **marqueurs orphelins**, qui porte désormais **vingt-six
  sièges**.*

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.28** — § 43.1 à
§ 43.6, dans l'ordre exact —, **inchangée en v0.29 et en v0.30**, et le § 43.0 est une introduction de
chapitre. La **table de couverture est respectée pour ses six lignes**, y compris ses trois régimes
propres : Vol. II §19.1-19.4 en **condensé** ; Vol. III *Monographie* §27.1 et §27.4 en **condensé**,
⚠ *son §27.2 partant au ch. 44 et ses §27.3/§27.5 au ch. 45, **qui ne sont pas repris ici*** ;
Vol. I §5.12.1-5.12.3 et §4.12 en
**arrivées** depuis les ch. 34 et 24, §2.13.1 en **arrivée** depuis le ch. 6, et **§6.10 prélevé au
ch. 44**, qui traite par ailleurs son chapitre d'origine en bloc. La **neutralité fournisseur est
tenue** : *aucun composant n'est prescrit, les réalisations sont nommées comme cas documentés, et
leurs statuts sont dits à chaque mention.* ⚠ **Cardinaux re-mesurés au commit du 28 juillet 2026, sur
le marqueur littéral et sur le corps seul** (décision 16 du TOC) ; *les cardinaux antérieurs comptaient
les applications du garde-fou et n'étaient re-mesurables par aucune règle écrite.* **R-13 est tenu à
chaque emploi d'une échelle d'autonomie — domaine déclaré, sans cardinal** (alinéa c), le marqueur
littéral y comptant **une occurrence**, au § 43.5, siège de la
désambiguïsation ; **le cardinal et la numérotation de leur échelle** y sont portés, et **« copilote »
n'est jamais employé nu**. La **forme « attendu par E-23 » est tenue à chaque énoncé sur E-23 —
domaine déclaré**, le marqueur littéral « F-09 » y comptant **deux occurrences**, et ⚠ **l'unique
endroit où une source écrit « exigé » est signalé, borné et remonté** plutôt que repris. Le marqueur
littéral **« degré 3 » compte quatre occurrences**, chacune portant son degré. Les **six métriques
auto-déclarées** sont attribuées à l'institution ou à l'analyste **nommé** qui les publie — ⚠ **TD et
Layer 6, Scotiabank, McKinsey/QuantumBlack et MIT NANDA sont désormais nommés en toutes lettres**
(décision 15 du TOC, alinéa b, premier titre). **Les cinq points de contrôle obligatoires ne sont pas
déduits d'une source, et la pièce l'écrit** : *ce sont les cinq zones du ch. 42 assignées à leur
couche, dont quatre seulement deviennent des points de contrôle.*
