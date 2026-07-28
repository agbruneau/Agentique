# Chapitre 23 — Les frameworks d'orchestration d'entreprise

*Livre III — Encadrer : orchestration en entreprise, cadre réglementaire canadien et terrain financier.
Premier mouvement — autonomie encadrée : orchestration en entreprise (ch. 22-24). Deuxième chapitre du
mouvement : il éprouve sur l'offre réelle le vocabulaire que le ch. 22 a posé.*

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — porte **G-3** ouverte (socle consolidé à zéro entrée) ; volet résiduel de **G-1** non instruit ; instruction d'auteur du 27 juillet 2026. ⚠ **La règle cardinale du PRD §5 est enfreinte.** Voir la note de statut, § 23.6. ⚠ **Ce chapitre est celui du Livre dont les faits se périment le plus vite** : quatre des cinq offres qu'il examine portent un statut de disponibilité daté, et deux d'entre eux étaient pré-disponibilité générale au gel de leur source |
| **Date de gel** | **27 juillet 2026** — gel unique, **D-1 prise** (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Volet résiduel de G-1 non instruit** : **aucun statut de disponibilité de ce chapitre n'a été repris à la source primaire**, et les préversions publiques y sont celles que le Vol. II constatait à son propre gel. Gels de source consommés : **16-17 juillet 2026** (Vol. II ch. 7) et **juin 2026** (Vol. I §2.8.4) — ⚠ **aucun des deux ne tient lieu du gel de la somme** |
| **Socle mobilisé** | **Aucune entrée du socle consolidé** (G-3 ouverte). Les énoncés résolvent contre le **Vol. II *Monographie* ch. 7**, dont les entrées **F-15**, **F-16**, **F-32**, **F-33** et **F-41** conservent leurs niveaux d'origine — **[B]** pour les quatre premières (annonces primaires extraites, citations verbatim), **[B] revalidé** pour F-41 ; l'entrée **Temporal** y demeure au **repérage [C]** et **ne porte aucun fait central** ; l'entrée **CrewAI** s'y tient à **trois niveaux distincts** que la pièce sépare. Le **Vol. I *Monographie* §2.8.4** entre en **[C]** — repérage documentaire (PRD §7.1). **Aucun énoncé n'est central au sens de CA-IV-01** |
| **Garde-fous balayés** | Vol. II — **PRD §8.2.3 (chiffres d'éditeurs auto-déclarés) : quatre occurrences**, § 23.2 (deux) et § 23.4 (deux), chacune attribuée à sa source à l'endroit même où elle est citée ; **PRD §8.4 (neutralité fournisseur) : trois occurrences**, § 23.0, § 23.3 et § 23.5 ; **R-1 : zéro occurrence** ; **R-8 : zéro occurrence** — le sigle n'apparaît pas dans ce chapitre ; **R-2 à R-7 : zéro occurrence**. Vol. III — **R-09 (quatre statuts, dits à chaque mention) : neuf occurrences**, § 23.1 (deux), § 23.2 (deux), § 23.3 (trois) et § 23.4 (deux) ; **R-14 (trois degrés d'absence) : sept occurrences**, § 23.0, § 23.1, § 23.2 (deux), § 23.4 et § 23.5 (deux) ; **R-02 : deux occurrences**, § 23.1 et § 23.5 ; **R-13 : une occurrence**, § 23.5 ; ⚠ **faux ami déclaré** — le « plan de contrôle » du maillage de services pré-agentique (ch. 1 § 1.3.4) n'apparaît pas ici. **R-01, R-03 à R-08, R-10 à R-12 : zéro occurrence** |
| **Volumétrie cible** | ≈ **5 000 mots** de corps (§ 23.0 à § 23.5), **cible dérivée** de l'enveloppe du Livre — 90 000 mots au TOC v0.25 — au prorata des sections, ce chapitre en portant cinq. ☑ **Décompte publiable depuis G-2** ; la mesure réelle est portée au [`README.md`](README.md) du dossier, par [`PRD/decompte.sh`](../PRD/decompte.sh), **seule autorité de décompte**. ⚠ **D-4 interdit l'amputation comme le gonflement** |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.25, entrée du chapitre 23)* — l'offre s'est industrialisée en 2025-2026 (Agent Framework, LangGraph, orchestration événementielle Kafka/Confluent) avec un support MCP **répandu et inégalement établi** et un support A2A de périmètre inégal.

---

⚠ **La thèse a été collationnée contre le texte rédigé de sa source avant la rédaction** (décision 14
du TOC). **Domaine de balayage : une thèse examinée, zéro réalignée.** La forme du TOC **condense**
celle du Vol. II — laquelle ajoute « un support A2A **désormais attesté de première main**, mais de
périmètre inégal » — sans rien lui faire dire de plus : *une condensation qui retranche un qualificatif
positif ne surqualifie pas.* Le corps écrit néanmoins la forme complète, celle de la source, parce que
c'est d'elle que dépend le décompte du § 23.2.

## § 23.0 — Ouverture : ce qu'un principe d'architecture vaut sans produit pour le porter

Les deux mouvements du ch. 22 ont posé un vocabulaire et un principe : quatre options d'orchestration
permettant de situer une architecture sur un continuum d'encadrement, et l'autonomie encadrée comme
mécanisme premier de gouvernance. Reste la question que pose tout architecte d'entreprise une fois la
doctrine admise : **que livre effectivement l'industrie, à quelle date, et avec quel statut de
disponibilité ?** *Un principe d'architecture qu'aucun produit ne sait porter n'est qu'un vœu ; un
produit dont la fonctionnalité décisive est en préversion n'est pas encore une décision d'achat.*

Ce chapitre soutient que l'industrialisation a bel et bien eu lieu — mais qu'elle est **plus inégale
que le discours des éditeurs ne le laisse paraître**, et que cette inégalité se loge précisément là où
une institution financière regarde : le **statut de disponibilité**, le **périmètre exact** des
fonctionnalités d'interopérabilité, et la démarcation entre ce qu'un éditeur **documente** et ce qu'il
se contente de **déclarer**. Il couvre **cinq offres**, dans le périmètre exact que le socle autorise :
trois au corps, deux en encadré — dont une que le socle ne documente qu'au niveau du repérage.

⚠ **Une convention de lecture gouverne tout le chapitre.** Lorsqu'il est écrit ci-dessous que « le
socle ne documente pas » telle capacité d'un produit, il faut l'entendre au sens strict : c'est une
**absence de documentation dans le corpus de la somme** — degré 3 de l'échelle R-14 du Vol. III —,
**non un fait négatif vérifié**. La distinction n'est pas de rhétorique : *elle sépare ce qu'un dossier
de conformité peut affirmer de ce qu'il doit aller vérifier lui-même.*

⚠ **Neutralité fournisseur.** Le chapitre **nomme** des offres et **ne recommande** aucune d'elles ;
aucun comparatif indépendant ne figure au socle, et le peu de métriques disponibles est **auto-déclaré
par les éditeurs**. *La neutralité interdit de recommander, non de nommer* — et un statut qui n'est pas
attribué n'est pas revalidable au gel suivant.

**Ce que le chapitre ne traite pas.** Ni l'identité et les registres d'agents, dont les sièges sont aux
**ch. 15 à 18** ; ni le passage à l'échelle d'un parc, qui est au **ch. 24** ; ni la place de la
branche événementielle dans un portefeuille d'intégration d'entreprise, qui relève du **Livre IV** ;
ni aucune adoption en production dans une institution financière canadienne — c'est l'objet du
**ch. 35**, et **aucune des sources citées ici n'y contribue**.

## § 23.1 — Microsoft Agent Framework : la succession assumée

Le premier des trois jalons est daté du **3 avril 2026** : Microsoft Agent Framework atteint sa
**disponibilité générale** (*general availability*, GA) en version 1.0 (Vol. II F-15, **[B]**). Le fait
notable n'est pas la version, c'est la **généalogie**. Agent Framework est le successeur direct de deux
produits antérieurs du même éditeur — l'un issu de la recherche multi-agents, l'autre de l'intégration
d'entreprise —, développés par les mêmes équipes ; il **fusionne** les abstractions d'agents du premier
et les fonctionnalités d'entreprise du second, et le socle cite des **guides de migration publiés** —
⚠ **sans établir qu'il en existe un par lignée** (*absence de documentation, degré 3*).

Lecture de l'auteur — la succession assumée n'est pas un détail de calendrier produit, c'est un
**signal de risque de tiers**. Une institution qui avait bâti sur l'une ou l'autre lignée n'affronte pas
un abandon, mais une **convergence documentée**, assortie de guides publiés. **Ce que le socle
établit** : la filiation, la fusion des abstractions et l'existence de ces guides. **Ce qu'il n'établit
pas** : leur couverture par lignée, leur qualité, le coût réel d'une migration, ni aucun engagement de
support à long terme. *L'inférence porte sur la forme de la transition, pas sur sa facilité.*

Sur le versant **protocolaire**, Agent Framework est l'offre du socle dont le support du protocole
agent-outil est **le mieux caractérisé** : support natif, avec clients, serveurs appelables, outils
locaux et outils hébergés. La **bidirectionnalité** mérite qu'on s'y arrête — le framework consomme des
outils exposés par des serveurs tiers, et peut lui-même en exposer. C'est exactement la doctrine
officielle de complémentarité que le **ch. 8** examine — le protocole agent-outil pour l'intégration
d'outils et de contexte au niveau de l'agent individuel, le protocole agent-agent pour la coordination
entre agents, que le projet résume par « Complementary to MCP, not a replacement » (Vol. II F-16,
**[B]**) —, appliquée ici du premier côté. ⚠ **Et il faut préciser dans le même mouvement ce que la
formule ne dit pas** : le protocole agent-outil fournit un **cadre d'autorisation** fondé sur OAuth, ce
qui **ne rend « sécurisée » aucune implémentation qui s'en réclame** (réserve F-01 du Vol. II) — *un
mécanisme se qualifie par ce que sa spécification démontre, non par ce qu'elle promet* (R-02 du
Vol. III). Le **ch. 11** en documente les surfaces d'attaque.

⚠ **Le socle ne documente aucun support du protocole agent-agent pour Agent Framework lui-même** ; les
intégrations de ce protocole par les plateformes infonuagiques du même éditeur relèvent d'une autre
entrée, traitée au **ch. 8**. Selon la convention posée en ouverture, c'est une **absence de
documentation**, non une absence établie.

Sur le versant de l'**orchestration**, Agent Framework livre des *workflows* à base de graphes
(*graph-based workflows*) avec **routage typé**, **points de contrôle** (*checkpointing*) et
**humain-dans-la-boucle** (*human-in-the-loop*).

Lecture de l'auteur — ce triplet se laisse lire avec les catégories du ch. 22 : le graphe comme **cadre
explicite**, le point de contrôle comme instrument de **traçabilité**, l'humain-dans-la-boucle comme
**point d'arrêt** de supervision. **Ce que le socle établit** : les capacités d'un côté, la taxonomie de
l'autre. **Ce qu'il n'établit pas** : le rapprochement, qui est celui de la somme et se développe au
§ 23.5. ⚠ **L'humain-dans-la-boucle des frameworks ne se confond pas avec la révision humaine que le
ch. 27 examine au titre de l'article 12.1 de la Loi 25** : les deux mécanismes se ressemblent et ne
répondent pas au même besoin — le premier est un point d'arrêt d'ingénierie, le second une obligation
légale ouverte **sur demande de la personne concernée**.

Deux réserves accompagnent l'entrée du socle, et l'une d'elles porte loin. La première est mineure : un
des SDK demeure **en préversion**. La seconde ne l'est pas : le socle documente des **limites connues
du magasin de points de contrôle en déploiement distribué multi-conteneurs**.

Lecture de l'auteur — une institution financière canadienne qui déploierait ce framework le ferait,
selon toute vraisemblance, sur une infrastructure conteneurisée distribuée : **la configuration précise
où le socle signale la limite**. Et le mécanisme concerné — le point de contrôle — est celui-là même
dont dépend la **reconstitution *a posteriori* d'une exécution**, c'est-à-dire ce que le ch. 25
rencontrera au titre de la surveillance continue. **Ce que le socle établit** : l'existence de la
limite et son domaine. **Ce qu'il n'établit pas** : sa gravité, son contournement, ni le calendrier de
sa résolution. *La conclusion praticable n'est pas « ne pas déployer », c'est « instruire ce point avant
l'inventaire de modèles » — et cette instruction incombe à l'institution, non à la somme.*

**Ce que le Vol. I ajoute, au régime [C].** Le repérage documentaire du Vol. I situe cette offre dans
une famille — celle des frameworks de grands fournisseurs, qu'il distingue par le **couplage au
fournisseur de modèle**, le **modèle d'exécution** et la **portée d'interopérabilité** — et note deux
voisines : l'une articulée autour du passage de relais entre agents, des garde-fous de validation
d'entrées et de sorties et du traçage intégré ; l'autre organisant des arbres d'agents nativement
interopérables par le protocole agent-agent. ⚠ **Ce repérage n'élève rien** : il vient d'un volume dont
la vérification porte sur les références et non sur le contenu des affirmations, et il **ne porte aucun
fait central**.

## § 23.2 — LangGraph Platform : la GA la plus ancienne, la frontière plateforme/bibliothèque

Le deuxième jalon est antérieur de moins de onze mois au premier : la disponibilité générale de
**LangGraph Platform** est annoncée le **14 mai 2025**, pour le déploiement et la gestion d'agents à
état et de longue durée (*stateful, long-running agents*) — Vol. II F-32, **[B]**, annonce primaire
extraite avec citations verbatim. Le billet nomme des entreprises construisant des agents avec la
**bibliothèque**, et **une** entreprise cliente pour la gestion centralisée, c'est-à-dire pour la
**plateforme**.

⚠ **Ces deux énoncés ne se fusionnent pas, et la source impose elle-même la distinction.** Les premiers
sont cités comme construisant des agents **avec la bibliothèque** ; la seconde est nommée comme cliente
d'entreprise **pour la plateforme**. Le socle ne permet ni de les confondre, ni d'inférer que ces
entreprises figurent parmi les déploiements dénombrés ci-dessous. *Une référence client nommée est un
fait plus solide qu'un décompte agrégé, à condition de ne lui faire dire que ce qu'elle dit.*

Le billet annonce aussi un chiffre. ⚠ **Métrique auto-déclarée, attribuée ici comme elle doit l'être à
chaque occurrence** (PRD Vol. II §8.2.3) : **selon le billet de disponibilité générale de LangChain du
14 mai 2025, l'éditeur déclare que près de 400 entreprises avaient déployé des agents en production via
la plateforme depuis la bêta de juin 2024** — soit sur les onze mois qui séparent les deux dates.
**Cette donnée est auto-déclarée et n'a fait l'objet d'aucune vérification indépendante.** Elle n'est
pas pour autant sans valeur : à la différence des décomptes d'« organisations de soutien » examinés au
**ch. 7**, elle prétend mesurer un **déploiement en production**, ce qui est la grandeur pertinente.
Mais elle est déclarée par le vendeur du produit qu'elle valorise, **sans définition publiée de l'unité
comptée**.

Le point décisif est ailleurs, et il est **de périmètre**. Le billet de mai 2025 **ne mentionne ni le
protocole agent-outil ni le protocole agent-agent**. Une passe d'élévation du 16 juillet 2026 a comblé
une partie de ce silence, mais d'une manière qu'il faut énoncer avec exactitude : le support du
protocole agent-agent est confirmé de première main **pour la plateforme commerciale** — la
documentation officielle décrit un point d'entrée dédié et trois méthodes nommées — **mais pas pour la
bibliothèque libre**, où la fonctionnalité demeurait une **requête ouverte** au 3 avril 2026.

Lecture de l'auteur — cette frontière n'est pas technique, elle est **commerciale**, et elle se lit dans
un dossier d'approvisionnement avant de se lire dans une architecture. L'interopérabilité inter-agents
de cette lignée est, à la date de gel, une **propriété de l'offre commerciale et non de la bibliothèque
libre**. Une institution qui adopterait la bibliothèque en pensant obtenir le protocole agent-agent, ou
qui construirait un scénario de repli sur elle en supposant la parité fonctionnelle, **se tromperait
sur ce qu'elle achète et sur ce qu'elle peut internaliser**. **Ce que le socle établit** : les deux
versants de l'asymétrie. **Ce qu'il n'établit pas** : l'intention de l'éditeur, ni le calendrier d'une
éventuelle convergence.

⚠ **Quant au support du protocole agent-outil, le socle n'en documente aucune source de première main**
— absence de documentation, degré 3, et non fait négatif vérifié. Elle suffit néanmoins à mesurer ce
que la thèse entend par un support « répandu et inégalement établi », et **le décompte le montre plus
précisément encore.**

| Offre | Protocole agent-outil | Protocole agent-agent | Niveau |
|---|---|---|---|
| **Agent Framework** | documenté **de première main** | non documenté | **[B]** (F-15) |
| **LangGraph** | **non documenté** | **plateforme commerciale seulement** — pas la bibliothèque libre | **[B]** (F-32) |
| **Confluent / Kafka** | documenté **de première main** | **préversion publique** | **[B]** (F-33) |
| **Temporal** | **repéré, non extrait** | non documenté | **[C]** — ne porte aucun fait central |
| **CrewAI** | **repéré, non extrait** | documenté **de première main** | **[B]** sur ce seul volet |

: Tableau 23.1 — Les cinq offres et le régime de preuve de leur support protocolaire, au gel du Vol. II (16-17 juillet 2026). ⚠ **Aucune ligne n'a été reprise à la source primaire pour la somme** — le volet résiduel de G-1 est dû.

**Sur les cinq offres, le support du protocole agent-outil n'est documenté de première main que pour
deux** — Agent Framework et Confluent —, **repéré sans extraction pour deux autres** — Temporal et
CrewAI, que le socle range l'un et l'autre au niveau **[C]** —, et **non documenté pour la cinquième**.
*Répandu, en effet ; inégalement établi, surtout — et à aucun moment « généralisé », mot que le
décompte réfute et que la thèse ne porte pas.*

⚠ **C'est de ce décompte que dépend la thèse, et c'est pourquoi CrewAI ne se note jamais d'une
étiquette unique** : lui attribuer un « **[B]** » global écraserait la distinction entre son volet
agent-agent, élevé sur source primaire extraite, et son volet agent-outil, resté au repérage — et le
décompte « **deux offres sur cinq de première main** » tomberait avec elle. Le § 23.4 tient les trois
niveaux séparés.

**Ce que le Vol. I ajoute, au régime [C].** Le repérage du Vol. I décrit la mécanique de cette lignée :
un système agentique y est modélisé comme un **graphe d'états** où chaque nœud transforme un état
partagé et où des **réducteurs** déterminent comment fusionner les mises à jour concurrentes ; la
persistance de l'état après chaque pas autorise **reprise, retour en arrière et intervention humaine**.
⚠ **Ce repérage n'établit aucun statut de disponibilité** : c'est l'entrée du Vol. II qui les porte, et
elle seule.

## § 23.3 — L'orchestration événementielle : le journal avant le cadre

Des trois branches traitées au corps, la troisième est **la seule à ne pas être en disponibilité
générale**, et c'est peut-être la plus intéressante pour une institution financière — *parce qu'elle
raisonne en flux, comme les paiements.*

En **août 2025**, un éditeur annonce des **agents événementiels** sur son offre infonuagique :
exécution sur un moteur de traitement de flux et un bus de messages managés, avec **appel d'outils
déclaré nativement** par le protocole agent-outil (Vol. II F-33, **[B]**). Six mois plus tard, une mise
à jour du **26 février 2026** ajoute trois éléments : une **intégration du protocole agent-agent en
préversion publique** (*Open Preview*), permettant à ces agents d'orchestrer des tâches avec des agents
externes sur toute plateforme compatible ; le **support officiel du serveur d'outils libre** pour son
offre infonuagique ; et une caractérisation du transport qui mérite d'être citée en langue originale
pour ce qu'elle affirme — la collaboration inter-agents s'y opère « all over a reliable, replayable
Kafka backbone », soit **sur une dorsale fiable et rejouable**.

Lecture de l'auteur — c'est là que le présent mouvement rejoint ce que le ch. 22 § 22.4 a établi. Les
travaux repris là-bas — un préprint non révisé par les pairs, dont les auteurs déclarent eux-mêmes des
menaces à la validité — posent que **la journalisation confiée aux agents n'est généralement pas
recommandée**. Un bus d'événements rejouable répond exactement à ce problème : il **externalise le
journal hors des agents**, et le rend rejouable **par construction plutôt que par discipline**. **Ce
que le socle établit** : la caractérisation du transport par son éditeur, et la position des travaux
repris au ch. 22. **Ce qu'il n'établit pas** : le rapprochement entre les deux, qui est une inférence de
la somme — ⚠ **et une inférence dont la portée est bornée.** *Un bus fiable et rejouable fournit un
**journal**, non un **cadre** : il enregistre ce qui s'est produit, il n'impose pas ce qui doit se
produire.* **La traçabilité n'est pas l'encadrement**, et le deuxième mouvement du présent Livre
montrera que les exigences canadiennes réclament **les deux**.

La liste des plateformes que cet éditeur cite comme partenaires possibles recoupe le périmètre du
chapitre : **un seul de ces noms** renvoie à une offre dont le socle confirme de première main, chez
son propre éditeur, un support du protocole agent-agent. Un autre est cité **sans que le produit visé
soit précisé**, et le socle ne permet pas de le rattacher à la plateforme commerciale plutôt qu'à la
bibliothèque libre — laquelle n'a précisément aucun support documenté. **La frontière posée au § 23.2
interdit de trancher à la place de la source.**

Lecture de l'auteur — la recoupe vaut d'être notée pour ce seul cas, où la somme dispose
d'attestations **des deux côtés** plutôt que d'un seul. Elle ne va pas plus loin : la mention est une
déclaration d'un éditeur sur ce que **son** intégration permettrait, la confirmation vient de l'éditeur
cité et porte sur **son propre** produit, et **aucune source du socle ne documente une liaison
effectivement établie entre deux de ces offres** — l'une des deux extrémités étant du reste en
préversion.

⚠ **Deux réserves sont dirimantes.** Les fonctionnalités décrites sont **pré-disponibilité générale** —
préversion publique ou accès anticipé. Et la source **ne nomme aucun client et ne publie aucun chiffre
d'adoption** : *l'adoption en production ne peut pas en être inférée.* Le contraste avec la section
précédente est instructif : l'un publie un chiffre auto-déclaré qu'il faut attribuer, l'autre n'en
publie aucun — ce qui interdit toute affirmation d'adoption mais épargne au lecteur une métrique
invérifiable. **Aucune des deux situations ne permet d'écrire que la branche événementielle est
déployée en production dans une institution financière.**

**Un fait de propriété, enfin**, dont ce chapitre ne développe pas les conséquences. L'acquisition de
cet éditeur par un grand fournisseur d'infrastructure a été **annoncée le 8 décembre 2025 et clôturée
le 17 mars 2026** — dix-neuf jours après la mise à jour décrite ci-dessus (Vol. II F-41, **[B]
revalidé**). Ce qui en découle pour un portefeuille d'intégration d'entreprise relève du **Livre IV**,
sous la réserve de **neutralité fournisseur**. Retenons ici le seul point qui concerne l'architecte en
amont de son choix : **la trajectoire événementielle décrite ci-dessus a changé de propriétaire entre
son annonce et la date de gel de sa source.**

**Ce que le Vol. I ajoute, au régime [C].** Une troisième famille y est décrite, qui mêle déterminisme
et agentivité par un **modèle événementiel** : des étapes enchaînées par décorateurs de démarrage et
d'écoute, articulant des équipes d'agents à rôles au sein de flux pilotés par événements ; ou des
étapes déclenchées par des événements, offrant une primitive légère pour composer comportements
agentiques et passages strictement déterministes. **Ces approches rendent explicite le graphe de
dépendances entre étapes**, ce qui facilite la traçabilité et la composition — *et c'est précisément la
propriété que le § 23.5 identifiera comme un matériau, non comme un positionnement.*

## § 23.4 — Deux cas en encadré : Temporal et CrewAI

Les deux offres restantes **ne se traitent pas au même niveau de preuve**, et c'est la raison de leur
mise en encadré.

> **État de la connaissance vérifiable — l'adoption d'entreprise de Temporal.** Question : quelle est
> l'adoption d'entreprise de cette offre, et quel est le statut exact de son support des agents et du
> protocole agent-outil ? **Recherche : aucune.** La passe d'élévation bornée du 16 juillet 2026 ne
> l'a pas instruite — elle portait sur quatre autres cibles. ⚠ **La lacune du socle (PRD Vol. II
> §10.3, réduite en P0) subsiste ici faute de tentative, non par échec de recherche**, et les chiffres
> d'adoption d'entreprise demeurent non vérifiés. *La distinction importe en dossier de conformité :
> rien n'autorise à conclure que ces chiffres résisteraient à la vérification, ni qu'ils s'y
> déroberaient.* Le socle n'en conserve qu'un **repérage documentaire** — un billet officiel décrivant
> une intégration en préversion publique, chaque invocation d'agent s'exécutant comme activité
> orchestrée dans un *workflow* durable, ainsi que des recettes d'outillage dans la documentation —
> **sans extraction intégrale du contenu**. ⚠ **Ce niveau de preuve interdit à ces éléments de porter
> un fait central** ; ils sont mentionnés comme repérage, et à ce titre seulement. En l'absence de
> source primaire extraite, la question reste ouverte ; **aucune inférence n'est proposée ici**.

> **CrewAI — première main sur le protocole agent-agent, repérage sur le protocole agent-outil,
> autodéclaration sur l'adoption.** Cette offre se documente **à trois niveaux de preuve distincts**,
> qu'il faut tenir séparés — c'est ce qui la distingue de la précédente, uniformément au repérage.
> *(1)* Le support du **protocole agent-agent** y est documenté de première main, **élevé [B] le
> 16 juillet 2026** sur source primaire extraite : la documentation officielle énonce que « CrewAI
> treats A2A protocol as a first-class delegation primitive », décrit une variante d'installation
> dédiée et deux classes de configuration nommées, et porte un journal des modifications daté depuis
> novembre 2025. *(2)* Le support du **protocole agent-outil** relève d'un deuxième régime : il est
> documenté officiellement par l'éditeur — connexion par trois transports, les outils étant consommés
> comme des outils natifs — mais le socle le laisse au **repérage [C]**, n'en ayant pas extrait le
> contenu, et l'élévation du 16 juillet 2026 n'a porté que sur le premier volet. ⚠ **Il ne peut donc
> porter aucun fait central** — d'où le décompte du § 23.2. *(3)* Les **chiffres d'adoption** relèvent
> d'un troisième régime. ⚠ **Métrique auto-déclarée** (PRD Vol. II §8.2.3) : **selon CrewAI — qui ne
> publie à cet endroit ni source datée ni définition de l'unité comptée —, l'éditeur déclare que sa
> plateforme est employée par des entreprises du Fortune 500 et qu'elle a enregistré environ deux
> milliards d'exécutions sur douze mois. Ces données sont auto-déclarées et n'ont fait l'objet d'aucune
> vérification indépendante.** ⚠ **L'écart avec la métrique du § 23.2 joue contre celle-ci** : celle-là
> est datée et rattachée à un billet identifiable, donc situable et contestable ; celle-ci ne l'est
> pas. Ces chiffres **ne fondent aucune affirmation d'adoption en production dans le secteur financier
> canadien**.

**Ce que le Vol. I ajoute, au régime [C].** Le thème d'ingénierie que ces deux cas illustrent est celui
de l'**exécution durable** — garantir qu'un système agentique long survive aux pannes, reprenne là où
il s'est arrêté et **n'exécute pas deux fois une action non idempotente**. Le repérage du Vol. I note
que la persistance interne d'un framework s'appuie de plus en plus sur des **moteurs dédiés**, et que
s'y ajoutent des **garde-fous structurels** — intervention humaine, sorties structurées, diffusion de
résultats partiels — et une **observabilité native**. ⚠ **La mécanique de ces moteurs est posée au
ch. 22 § 22.5.1 et n'est pas reconstruite ici** ; la **sémantique d'effet** que le mot « idempotente »
appelle est au **ch. 48**, qui en est le siège.

## § 23.5 — Grille de lecture : ce que les patrons livrés positionnent, et ce qu'ils ne positionnent pas

Il reste à faire ce pour quoi le ch. 22 a construit son vocabulaire : **situer les patrons livrés sur
la taxonomie OO1-OO4**.

⚠ **L'exercice appelle un avertissement préalable, et il est dirimant.** **Aucune source du socle ne
positionne un framework sur l'échelle OO1-OO4** : la taxonomie est un cadre académique, les produits
sont documentés par leurs éditeurs, et **le corpus de la somme ne contient aucune source rapprochant
les deux** — *absence de documentation, degré 3, conformément à la convention posée au § 23.0.* Le
tableau qui suit est donc **intégralement une construction d'auteur**.

Lecture de l'auteur — le tableau ci-dessous rapproche ce que le socle établit d'un côté et de l'autre.
**Ce que le socle établit** : les capacités documentées de chaque offre, et la taxonomie du ch. 22.
**Ce qu'il n'établit pas** : le moindre positionnement, qu'aucune source ne porte.

| Patron livré | Ce que le socle établit | Positionnement proposé *(construction d'auteur)* |
|---|---|---|
| *Workflows* à base de graphes, routage typé | Agent Framework, GA 1.0 (F-15) | le graphe est un **cadre explicite extérieur aux agents** — **OO3 ou OO4** selon que les agents invoqués sont ou non conscients du processus |
| Points de contrôle | Agent Framework, GA 1.0 ; limites en multi-conteneurs (F-15) | instrument de la propriété **traçabilité**, **non une option d'orchestration** en soi |
| Humain-dans-la-boucle | Agent Framework, GA 1.0 (F-15) | **point d'arrêt de supervision** ; critère de sélection du ch. 22 § 22.3, non un positionnement |
| Agents durables | Temporal — **repérage [C]**, ne porte aucun fait central | **aucun positionnement proposé** : le niveau de preuve ne le permet pas |
| Bus d'événements comme transport inter-agents | Confluent, protocole agent-agent en préversion publique sur dorsale rejouable (F-33) | le protocole agent-agent **sans cadre de processus explicite est la définition même d'OO1** ; le bus ajoute **le journal, non le cadre** |

: Tableau 23.2 — Les patrons livrés, situés sur la taxonomie du ch. 22 § 22.1. **La colonne de droite est une construction d'auteur en totalité** — aucune source du socle ne rapproche produits et taxonomie.

De ce tableau, un enseignement se dégage, et c'est le principal du chapitre. **Aucun des frameworks
examinés ne livre un positionnement ; ils livrent des matériaux qui en autorisent plusieurs.** Un même
framework sert à câbler un graphe déterministe qui invoque des agents pour des tâches bornées — de
l'ordre d'OO3 — ou à laisser un agent choisir librement ses outils sans cadre explicite — de l'ordre
d'OO1. *Le produit n'arbitre pas ; la configuration arbitre.* Le cadre repris au ch. 22 rappelle
d'ailleurs que **les transitions entre options sont fluides**, ce qui est la même observation vue depuis
la théorie.

Lecture de l'auteur — et elle engage la suite du Livre : **si le positionnement est un fait de
configuration et non de produit, alors la question « quel framework choisir ? » est mal posée pour une
institution réglementée.** La bonne question est « **quel cadre imposer, et quel produit sait le
porter ?** » — *l'ordre des termes n'est pas indifférent.* **Ce que le socle établit** : les deux
moitiés — la taxonomie d'un côté, les capacités documentées de l'autre. **Ce qu'il n'établit pas** : le
rapprochement, ni cette conséquence de méthode. C'est elle qui explique pourquoi le **Livre IV**
construit son architecture de référence **à partir des exigences et non du catalogue**, et pourquoi le
**ch. 29** est le pivot qui les traduit.

⚠ **Une dernière borne, et elle est de vocabulaire.** Rien de ce qui précède n'autorise à ranger ces
offres sur une échelle d'autonomie : les échelles d'autonomie ne s'emploient jamais nues (R-13 du
Vol. III), elles se nomment par leur cardinal et leur numérotation, et **le ch. 14 § 14.4 en est le lieu
de croisement pour toute la somme**. *Un produit ne se situe pas sur une échelle d'autonomie ; une
configuration s'y situe.*

### Synthèse : ce que le chapitre lègue à la somme

*Section de sortie sans homologue direct dans la source — construction d'éditeur.*

1. **Une industrialisation datée, et son inégalité.** Deux jalons de disponibilité générale sont datés
   et vérifiables — 14 mai 2025 et 3 avril 2026 —, la branche événementielle demeurant en préversion au
   gel de sa source. Le **ch. 35** ne réutilise aucun de ces faits : *il traite d'institutions, non
   d'éditeurs.*
2. **Le décompte « deux offres sur cinq de première main », et ce qui le tient.** Il ne tient que si
   CrewAI est noté **à trois niveaux séparés**. *Une étiquette unique le renverserait sans qu'aucun
   contrôle ne le signale.*
3. **La frontière plateforme / bibliothèque libre.** Elle est **commerciale**, non technique, et se lit
   dans un dossier d'approvisionnement. Le **ch. 24 § 24.2** la reprend au grain de la stratégie de
   standards ouverts, sans la redémontrer.
4. **Le journal n'est pas le cadre.** Un bus rejouable externalise la trace ; il n'impose rien. C'est
   la distinction que le **ch. 29** consomme pour montrer que les exigences canadiennes réclament les
   deux.
5. **Aucun produit n'arbitre le degré d'encadrement.** La question se pose dans l'ordre inverse — quel
   cadre imposer, quel produit sait le porter. Le **Livre IV** en fait sa méthode de construction.

⚠ **Ce que le chapitre ne lègue pas.** Aucun classement, aucune recommandation, aucune adoption en
production dans une institution financière canadienne. Aucune métrique utilisable sans son attribution.
Et **aucun positionnement établi** sur la taxonomie du ch. 22 : *le tableau 23.2 est une lecture, et il
se déclare telle à chacune de ses lignes.*

---

## § 23.6 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.** Elle consigne l'écart de
gouvernance sous lequel la pièce a été rédigée (PRD, Annexe A) : *un rédacteur ne corrige jamais le
TOC, ce PRD ni le Conspectus — il **remonte**.*

**Ce qui est enfreint.** La porte **G-3** et le **volet résiduel de G-1**. Instruction d'auteur du
27 juillet 2026. ⚠ **La porte G-4 ne conditionne pas ce chapitre** : sa ligne Fusion ne cite que le
Vol. II et le Vol. I. ⚠ **L'ordre de rédaction du PRD §6 n'est pas enfreint.**

1. **Aucun énoncé n'est central au sens de CA-IV-01.** Le socle consolidé compte zéro entrée ; les
   identifiants cités — F-15, F-16, F-32, F-33, F-41 — sont **ceux du Vol. II**, préfixés à chaque
   emploi (décision 7). Les éléments repris du Vol. I entrent en **[C]** et une élévation supposerait la
   lecture des sources primaires que le Vol. I cite.
2. ⚠ **Le volet résiduel de G-1 pèse plus lourd ici que sur tout autre chapitre du Livre.** Ce chapitre
   vit de **statuts de disponibilité**, et **aucun n'a été repris à la source primaire** : une
   préversion publique de février 2026 a pu passer en disponibilité générale, une requête ouverte au
   3 avril 2026 a pu être close, un SDK en préversion a pu être publié. *Chacun de ces faits est vrai à
   sa date et faux à la suivante* — et le **ch. 50** enregistrera ces événements de péremption.
3. **Les décomptes sont publiables** (G-2). L'écart à la cible est relevé au [`README.md`](README.md) du
   dossier et alimente **D-4**, déjà tranchée.
4. **Les renvois « ch. N » vers les chapitres non rédigés sont des renvois de plan.** Ils résolvent
   contre l'entrée du TOC : **ch. 24, 25, 27, 29, 35** (présent Livre, même passe), **ch. 48**,
   **ch. 50** et le **Livre IV** dans son ensemble. Résolvent contre du **texte rédigé** : **ch. 1
   § 1.3.4**, **ch. 7**, **ch. 8**, **ch. 11**, **ch. 14 § 14.4**, **ch. 15 à 18** et **ch. 22**.

**Remontées ouvertes par ce chapitre :**

- **R-IV-78 — non bloquante, de forme, et corollaire de R-IV-77.** Le TOC intitule le § 23.4 « **Deux
  cas en encadré** » : la forme y est **prescrite par le plan**. Or le skill de rédaction pose que les
  encadrés « cessent au Livre III ». ⚠ **Les deux règles ne portent pas sur le même objet et l'écart
  est réel** : la règle du skill vise les **deux dispositifs hérités du Vol. I** — « Perspective
  recherche » et « Mise en œuvre » —, tandis que le § 23.4 emploie le dispositif du **Vol. II**, l'état
  de la connaissance vérifiable, que rien n'a supprimé. La pièce a suivi le TOC, qui prime sur le
  contenu. **Demande remontée** : que la règle du skill nomme les dispositifs qu'elle éteint, plutôt
  que le mot « encadré ». *Une règle formulée sur un mot plutôt que sur un objet éteint plus que ce
  qu'elle vise.*
- **R-IV-79 — non bloquante, de cardinal daté.** La thèse et le § 23.2 reposent sur le décompte « deux
  offres sur cinq de première main », qui est **un cardinal annoncé en toutes lettres**. ⚠ **Il n'est
  vrai qu'au gel du Vol. II** : il bascule dès qu'une seule des trois offres au repérage est élevée, et
  le volet résiduel de G-1 n'a précisément pas été exécuté. **Demande remontée** : que ce cardinal soit
  inscrit au **registre des faits à re-mesurer au gel de publication**, comme l'a été celui du ch. 18
  (remontée R-IV-31), et que **le tableau 23.1 porte sa date** au même titre que le tableau 18.1.
  *Un cardinal annoncé en toutes lettres ne se met pas à jour tout seul.*

**Ce qui n'est pas enfreint.** La structure suit la **table détaillée du TOC v0.25** — § 23.1 à § 23.5,
dans l'ordre exact —, le § 23.0 étant une **ouverture de chapitre**. La **table de couverture est
respectée pour ses deux lignes** : le Vol. II §7.1-7.5 est condensé aux § 23.1-23.5, et le Vol. I
§2.8.4 **arrive** aux § 23.1-23.4, **arrivée déclarée aux deux bouts** — le ch. 6 en déclare le départ.
⚠ **Les quatre sous-sections du Vol. I sont toutes reçues** : §2.8.4.1 au § 23.2, §2.8.4.2 au § 23.1,
§2.8.4.3 au § 23.3, §2.8.4.4 au § 23.4 — *aucune n'est perdue en chemin*, ce qui était le risque de la
répartition d'une source unique sur quatre destinations. La **décision 14 a été exécutée avant la
rédaction**, domaine déclaré : une thèse examinée, zéro réalignée. Les **garde-fous des deux séries
sont balayés et déclarés, y compris à zéro occurrence**. Les **quatre métriques auto-déclarées sont
attribuées à chaque occurrence, sans exception d'usage illustratif** (PRD Vol. II §7.5 et §8.2.3), et
**les quatre statuts de disponibilité sont dits à chaque mention** (R-09 du Vol. III). Les **sept
occurrences de R-14 portent leur degré**. La **lacune PRD Vol. II §10.3 est portée et non comblée** :
elle est déclarée subsistante **faute de tentative**, non par échec de recherche — *la distinction est
celle que le Vol. II a lui-même établie, et l'effacer transformerait une lacune d'instruction en un
constat.* Enfin, **la neutralité fournisseur est tenue** : cinq offres nommées, aucune recommandée, et
le fait de propriété du § 23.3 rapporté **sans en tirer de conséquence de portefeuille**.


---

### Clôture des remontées — 27 juillet 2026

⚠ **Cette sous-section est hors plan comme la note qui la porte, et se retire avec elle.** Elle
enregistre l'issue des remontées ouvertes par cette pièce. *Une remontée ne se clôt pas là où elle
s'ouvre : elle se solde là où elle fait foi* — au [PRD](../PRD/PRD.md) pour une décision ou un régime,
au [TOC](../PRD/TOC.md) pour un réalignement de plan, à l'appareil pour une dette d'outillage.

⚠ **Renumérotation, à lire avant les numéros.** *Les remontées de ce Livre portaient d'abord les
numéros **R-IV-38 à R-IV-61** ; une **passe concurrente écrivait les Livres IV et V dans le même dépôt
le même jour** et les avait consommés. **Le Livre III a été renuméroté en R-IV-76 à R-IV-99** à la
découverte de la collision — **aucun numéro n'est partagé**.*

- **R-IV-78 — close avec R-IV-77 (PRD v0.10 §8).** ⚠ *Le § 23.4 est la preuve de la clarification* : **le
  plan prescrit l'encadré** — son intitulé porte « Deux cas en encadré » — **et le dispositif employé
  est celui du Vol. II**, que la règle d'extinction ne vise pas. *La pièce avait suivi le TOC, qui prime
  sur le contenu.*
- **R-IV-79 — close par versement au registre du volet résiduel de G-1 (PRD v0.10 §5).** Le cardinal
  « **deux offres sur cinq de première main** », ⚠ *dont **la thèse du chapitre dépend***, entre au
  **registre des faits à re-mesurer au gel de publication** — *il **bascule dès qu'une seule des trois
  offres au repérage est élevée***. ☑ **Le tableau 23.1 porte sa date**, comme le tableau 18.1 du
  ch. 18 après R-IV-31.

⚠ **Ce que la clôture ne change pas.** Les portes **G-3** et — pour les chapitres qui citent le
Vol. III — **G-4** demeurent ouvertes ; le socle consolidé compte **zéro entrée** ; **aucun énoncé de
cette pièce n'est central au sens de CA-IV-01**. **CA-IV-11 et CA-IV-13 ne sont pas satisfaites** —
*aucune relecture par un relecteur distinct du rédacteur*. Cette pièce reste un **brouillon non
publiable**. *Zéro remontée ouverte ne veut pas dire pièce recevable : cela veut dire qu'aucune
question n'attend plus de réponse qui ne soit déjà tranchée.*
