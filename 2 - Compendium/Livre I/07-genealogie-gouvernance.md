# Chapitre 7 — Généalogie et gouvernance : des projets propriétaires aux standards ouverts

*Livre I — Coopérer : fondements de l'interopérabilité et couche protocolaire agentique.
Second mouvement — la couche protocolaire agentique (ch. 7-11). **Premier chapitre du mouvement.***

| Champ | Valeur |
|---|---|
| **Statut** | **Brouillon de rédaction, non publiable** — portes G-1, G-2 et G-3 ouvertes ; rédaction sur instruction d'auteur du 27 juillet 2026. ⚠ **Premier chapitre du Livre I à consommer le Vol. II**, dont le régime de preuve diffère : ses faits portent des niveaux **[A]/[B]/[C]** explicites et conservent leur niveau d'origine (PRD §7.1), là où ceux du Vol. I entrent en [C] ⚠ **Mise à jour du 27 juillet 2026, postérieure à la rédaction** : **G-2 et le volet Livre I de G-1 ont été franchis depuis** (PRD v0.8), et les **remontées de cette pièce sont closes**. **G-3 demeure ouverte** — socle consolidé à zéro entrée : la pièce reste un **brouillon non publiable**, et aucun de ses énoncés n'est central au sens de CA-IV-01. |
| **Date de gel** | **27 juillet 2026** — gel unique du compendium, **décision d'auteur D-1 prise** ce jour (registre : [`gel-2026-07-27.md`](../PRD/gel-2026-07-27.md)). ⚠ **Ce gel n'efface pas ceux des sources**, qui restent portés ci-dessous : il date la reprise de chaque fait périssable à sa source primaire, non la matière elle-même. ⚠ **Ce chapitre porte deux gels de source distincts** — **juin 2026** (Vol. I) et **16 juillet 2026** (Vol. II) — et c'est le premier du Livre où l'écart compte : la chronologie qu'il établit s'arrête au bilan public d'avril 2026, et une révision protocolaire majeure était attendue **douze jours après** le gel du Vol. II |
| **Socle mobilisé** | **Aucune entrée du socle consolidé** (G-3 ouverte). Les énoncés résolvent contre le **Vol. I *Monographie* §3.0-3.1 et §3.13.1** (régime **[C]**) et le **Vol. II *Monographie* ch. 1** — dont le TOC assigne à ce chapitre les entrées **F-01, F-02, F-04, F-05, F-43**, à niveau conservé. ⚠ **Tant que G-3 n'est pas franchie, ces identifiants restent préfixés de leur volume** : un « F-01 » nu est indécidable entre deux socles |
| **Garde-fous balayés** | **Les deux séries — et ce chapitre est le siège d'un garde-fou.** ⚠ **Règle de décompte, et les cardinaux ci-dessous ont été re-mesurés sous elle le 28 juillet 2026** : un décompte d'occurrences porte sur le **marqueur littéral de l'identifiant** dans le **corps** de la pièce — en-tête et note de statut exclus —, et il se re-mesure au commit ; un garde-fou appliqué **sans identifiant écrit** se déclare par son **domaine balayé, sans cardinal**. Vol. II — **R-1 (l'ACP protocolaire n'est pas un standard vivant) : trois occurrences**, § 7.3, § 7.4.1 et § 7.5 ; **R-8 (sigle jamais nu, quatre branches) : deux occurrences**, § 7.5, dont le **SIÈGE** de l'encadré pour toute la somme — ⚠ *le sigle qualifié, lui, revient huit fois dans la pièce : c'est un décompte d'emplois, non de marqueurs, et il ne se confond pas avec celui du garde-fou* ; **métriques auto-déclarées (PRD Vol. II §8.2.1) — sans identifiant écrit, donc sans cardinal re-mesurable : appliqué au seul § 7.6**, chaque chiffre attribué à sa source ; ⚠ *le § 7.3, que cet en-tête portait auparavant, n'en porte aucune*. R-2 à R-7 : **zéro occurrence**. Vol. III — **R-13 : une occurrence**, § 7.5, mêmes termes ; **R-14 : deux occurrences**, § 7.4.2 et § 7.5. R-01 à R-12 : **zéro occurrence** |
| **Volumétrie cible** | ≈ 8 000 mots de corps (§ 7.0 à § 7.6). ☑ **Décompte publiable depuis le franchissement de G-2** (27 juillet 2026). **Réel : 4 887 mots** de corps, mesurés par [`PRD/decompte.sh`](../PRD/decompte.sh), seule autorité de décompte du volume — **−38,9 %** de la cible. ⚠ **L'écart individuel ne se lit pas seul** : la somme des onze cibles dérivées atteint **93 000 mots** pour une enveloppe de Livre de **65 000** — chaque pièce a dérivé sa cible de l'enveloppe sans que personne n'additionne les dérivations. Le **réel du Livre est de 64 750 mots, soit −0,4 % de l'enveloppe** : c'est la cible dérivée qui était fausse, non la pièce qui est courte. *Un écart se documente ; il ne se corrige ni par amputation ni par gonflement* |

> **Thèse** *(citée depuis le [`TOC.md`](../PRD/TOC.md) v0.28, entrée du chapitre 7)* — en dix-sept mois, la couche protocolaire agentique s'est consolidée sous gouvernance neutre (Linux Foundation) — condition **nécessaire et non suffisante** de sa crédibilité en entreprise réglementée (formulation du ch. 1 du Vol. II, que les v0.1-v0.5 amputaient de sa restriction) ; mais « soutien ≠ production », et le transfert de gouvernance d'AP2 **est documenté depuis la v0.24** : don à la FIDO Alliance le **28 avril 2026**, version v0.2, cas *Human-Not-Present*, deux groupes de travail techniques — fait **constaté à la source primaire le 27 juillet 2026** (registre du gel, fait 12), instruit au ch. 10.

⚠ **La restriction de cette thèse n'est pas décorative, et elle a déjà été perdue une fois.** Les versions v0.1 à v0.5 du plan citaient la thèse **amputée de « et non suffisante »**, ce qui en inversait la portée : d'un avertissement, elles faisaient une recommandation. La formulation intégrale est celle du ch. 1 du Vol. II, et c'est elle qui est reprise ici. *Une gouvernance neutre ne suffit pas à emporter la décision d'une institution réglementée* — le Livre III établit tout ce qu'il faut y ajouter.

⚠ **La dernière clause de cette thèse a été amendée après la rédaction de la pièce, et la citation ci-dessus porte la forme réalignée.** La pièce citait à l'origine la forme du TOC v0.23 — « AP2 n'a aucun transfert de gouvernance documenté » —, forme que la **remontée R-IV-08 a portée au plan** : la thèse **a été réalignée au TOC v0.24** (décision 8), le transfert étant établi à la source primaire par le Vol. I *Monographie* §3.13.1, et la citation **a été reprise depuis le TOC v0.28** à la passe de correction du 28 juillet 2026. ⚠ **La clause antérieure n'est pas effacée mais située** : elle était **exacte du point de vue du socle du Vol. II**, dont la couverture s'arrêtait à son gel, et **périmée du point de vue du Vol. I**, qui portait le fait daté — *lacune de couverture, non contradiction entre volumes*. Le § 7.4.2 et le **ch. 10 § 10.1.3** en instruisent l'écart.

---

## § 7.0 — Introduction : de l'échange de données à l'échange d'intentions

Le second mouvement du Livre s'ouvre ici. Les ch. 1 à 3 ont posé le socle **pré-agentique** ; les
ch. 4 à 6, l'**ingénierie de l'agent**. Ce mouvement traite la **couche d'interopérabilité agentique
proprement dite** — le contrat entre un agent et ses outils, le dialogue entre agents, la découverte,
le règlement commercial, et les modes d'échec qui leur sont propres.

La proposition directrice tient en un déplacement, et il vaut d'être énoncé avec précision : ce qui
transite entre systèmes d'IA n'est plus seulement de la **donnée structurée**, comme dans
l'intégration d'entreprise classique (ch. 2), mais des **intentions**, des **tâches** et des
**capacités** négociées à l'exécution.

Ce déplacement se lit comme un **glissement des noms vers les verbes**. Une interface REST est
orientée **ressources** : elle expose des entités — un client, une commande, un compte — que l'on
crée, lit, modifie ou supprime. Un agent est orienté **actions** : il reçoit un but exprimé en langage
naturel, sélectionne des opérations et les compose pour produire un résultat **dont la forme n'était
pas entièrement prédéterminée**.

L'objet de l'échange se déplace ainsi de l'**état partagé** vers l'**action déléguée**. Ce glissement
réactive la distinction posée au ch. 1 § 1.1.1 : l'interopérabilité n'est ni la connectivité, ni la
compatibilité de formats, mais la capacité d'échanger de l'information **et d'en faire un usage
utile**.

⚠ **C'est précisément parce que l'unité d'échange devient l'intention** — entité non déterministe,
sous-spécifiée, interprétée à l'inférence — **que la connectivité cesse de garantir
l'interopérabilité**. Le problème se déplace de la plomberie vers la négociation du sens, et c'est ce
déplacement que le ch. 9 § 9.4 mesure.

---

## § 7.1 — Définir l'interopérabilité agentique et ses niveaux

### 7.1.1 Définition de travail

L'**interopérabilité agentique** se définit comme la capacité de systèmes d'intelligence artificielle
agentique — autonomes, hétérogènes, pilotés par grand modèle de langage — à **se découvrir
mutuellement, se comprendre, déléguer des tâches et collaborer sans intégration point-à-point
préalable**.

Trois traits la distinguent de l'interopérabilité des systèmes d'information :

1. **l'absence d'intégration préétablie** — la mise en relation se négocie **à l'exécution** ;
2. **l'hétérogénéité radicale des acteurs** — modèles, cadriciels et fournisseurs distincts ;
3. **la nature de ce qui transite** — non plus des données structurées mais des intentions et des
   tâches.

⚠ **Cette définition appelle une contrepartie opérationnelle, et son absence est le défaut le plus
répandu du domaine.** Un système n'est dit interopérable que si une tâche déléguée d'un agent à un
autre **aboutit avec un taux de réussite et une fidélité de transfert d'intention vérifiables** — et
non au seul constat que la connexion s'établit. Le § 9.5 reprend cette exigence comme problème de
conformité.

### 7.1.2 Les niveaux LCIM appliqués aux agents

Le modèle des niveaux d'interopérabilité conceptuelle, introduit au ch. 1 § 1.1.2, se transpose
directement à la pile agentique :

| Niveau | Ce qu'il couvre, côté agentique |
| --- | --- |
| **Technique** | transport et connectivité — HTTP, appels de procédure en JSON, flux d'événements, entrée-sortie standard |
| **Syntaxique** | structure des messages — appels d'outils, cartes d'agent, cycle de vie des tâches |
| **Sémantique** | sens partagé — alignement des intentions, ancrage des termes sur des référents communs |
| **Pragmatique** | inférence de **l'action effectivement voulue** à partir d'un message |
| **Dynamique** | capacité à s'adapter, renégocier, découvrir des partenaires **à l'exécution** |

: Tableau 7.1 — Les cinq niveaux du LCIM appliqués à la pile agentique.

### 7.1.3 Pragmatique et dynamique : des niveaux existants devenus verrous opérationnels

⚠ **Il importe de souligner ce que ces deux derniers niveaux ne sont pas : des inventions de l'ère
agentique.** Le pragmatique et le dynamique figurent **en propre dans le modèle d'origine**. Ce qui
change n'est pas leur existence, mais leur **centralité opérationnelle**. Écrire que l'agentique
« ajoute deux niveaux » serait une erreur de fait, et elle est fréquente.

Le déplacement est ailleurs, et il est plus intéressant. Dans l'intégration classique, le verrou
dominant se situait au **sémantique** : faire correspondre des schémas et des vocabulaires (ch. 2).
Avec des acteurs pilotés par modèle, le **pragmatique** — inférer l'action voulue, et non seulement
décoder le contenu — devient le verrou prépondérant.

Ce niveau se manifeste d'une manière propre aux agents : **le sens n'est plus calculé par un
programme déterministe mais lu par le modèle à l'inférence**, à partir de descriptions en langage
naturel interprétées au moment de l'exécution. Le niveau **dynamique**, lui, recouvre la négociation
et la découverte à l'exécution — ce qui n'avait **pas d'équivalent généralisé** dans les piles
d'intégration figées au temps de conception.

Ces deux niveaux, anciens dans la théorie, deviennent ainsi **le terrain effectif où se joue — ou
échoue — l'interopérabilité agentique**.

### 7.1.4 Ce qui change quand les acteurs sont autonomes et non déterministes

Quatre ruptures distinguent l'interopérabilité agentique de l'intégration classique :

- **le non-déterminisme** — un acteur piloté par modèle ne garantit pas une réponse identique à
  entrée identique, ce qui **substitue des garanties probabilistes aux garanties exactes** ;
- **l'auto-description et la découverte à l'exécution** — l'acteur publie ses capacités sous une
  forme interprétable, et un pair les découvre puis les sélectionne au moment de l'échange ;
- **le langage naturel comme surface d'interface** — souple, mais **ambigu et non vérifiable
  mécaniquement** ;
- **l'orientation vers les buts** — l'acteur poursuit des objectifs plutôt qu'il n'exécute des
  instructions littérales, ce qui érige **la négociation et la clarification en primitives
  d'interaction**.

⚠ **Ces traits, qui font la puissance des systèmes agentiques, sont aussi la racine de leurs modes
d'échec** — lesquels ne se résolvent pas au niveau du modèle isolé (ch. 6) mais **aux frontières
entre acteurs** (ch. 11).

### 7.1.5 Reformuler la triade pour des acteurs probabilistes

Les trois termes de l'invariant doivent être réénoncés.

Le **contrat**, déterministe dans le monde des API — une requête valide produit une réponse conforme
au schéma (ch. 1 § 1.4.2) —, devient un **contrat comportemental probabiliste** : on ne peut plus
garantir qu'une entrée valide produira **invariablement** la sortie attendue, seulement qu'elle la
produira **avec une certaine probabilité**. Des travaux formalisent cette idée en spécifiant la
satisfaction d'un contrat par un triplet — **probabilité minimale, tolérance, nombre d'essais** —
assorti d'une **vérification à l'exécution**.

Le **découplage** s'enrichit de deux dimensions absentes du ch. 1 : le découplage de **modèle** —
l'application ne doit pas être liée à un fournisseur de modèle particulier — et de **cadriciel** —
elle ne doit pas être liée à un framework d'orchestration donné. Le ch. 9 § 9.3 les développe.

L'**évolution** prend enfin la forme d'un **versionnage des capacités** et d'une **politique de
dépréciation** : un agent ou un outil doit pouvoir faire évoluer ce qu'il offre sans briser ses
consommateurs.

> **Perspective recherche.** Le passage du contrat déterministe au contrat comportemental
> probabiliste **reformule la garantie d'interopérabilité comme une propriété statistique vérifiée à
> l'exécution** plutôt que comme une propriété structurelle vérifiée à la compilation. La
> spécification par probabilité cible, marge tolérée et répétitions fournit un **objet formel
> mesurable**, et son contrôle continu rapproche le contrat d'agent des **engagements observables**
> de la tradition multi-agents plutôt que des sémantiques mentalistes (§ 7.2.1).

### 7.1.6 Pourquoi l'interopérabilité classique ne suffit pas : l'argument de l'étagement

L'interopérabilité classique — appel de procédure à distance, API REST, bus de service (ch. 1 § 1.3
et § 1.4) — atteint ses limites devant les acteurs agentiques sur quatre points :

1. elle **ne prévoit pas d'auto-description exploitable à l'exécution** — un contrat décrit des
   points de terminaison au temps de conception, non des capacités négociées à l'inférence ;
2. elle est orientée **ressources** là où les agents sont orientés **actions** ;
3. elle suppose un **appelant déterministe** capable de composer correctement les requêtes ;
4. elle n'offre **aucune primitive native** pour les tâches de longue durée ni pour la négociation.

⚠ **Ces limites ne justifient pas de remplacer la pile classique, et c'est le point d'équilibre
essentiel contre la surenchère.** Les protocoles agentiques majeurs **réemploient massivement
l'existant** : le protocole agent-outil s'appuie sur des appels de procédure en JSON et sur HTTP, et
adosse son autorisation à des mécanismes éprouvés ; le protocole agent-agent propose plusieurs
liaisons de transport.

*La couche agentique **s'étage** au-dessus de la pile éprouvée — transport, sérialisation,
autorisation — plutôt qu'elle ne s'y substitue.* L'apport propre se situe **au-dessus** :
auto-description, découverte à l'exécution, modèle de tâche, négociation. C'est l'argument que le
ch. 9 § 9.2 systématise sous le nom d'étagement.

---

## § 7.2 — Filiation historique et taxonomie des quatre axes

### 7.2.1 Des langages de communication d'agents aux protocoles à engagements

L'interopérabilité agentique **n'est pas sans ascendance**, et l'ignorer conduit à réinventer des
échecs documentés.

Un premier langage proposait dès le milieu des années 1990 un jeu de **performatifs** — des verbes de
communication typés — pour structurer les échanges entre agents. Des spécifications ultérieures ont
prolongé cet effort en normalisant la structure des messages et une bibliothèque d'**actes
communicatifs**. Cette tradition s'enracine dans la théorie des actes de langage, qui montre que
**dire, c'est faire** — promettre, ordonner, demander étant des actions accomplies par la parole.

⚠ **Le verrou historique mérite d'être nommé, parce qu'il se rejoue aujourd'hui.** La sémantique de
ces spécifications reposait sur une lecture **mentaliste**, définissant la signification d'un message
par les **croyances et intentions présumées** de l'émetteur. Or ces états mentaux **ne sont pas
observables, donc pas vérifiables** : un agent ne peut prouver qu'un pair *croit* ou *veut* ce qu'il
déclare. C'est la **perte de sémantique vérifiable**.

La réponse historique fut de fonder la signification sur des **engagements sociaux observables**
plutôt que sur des états mentaux privés, et de spécifier les protocoles par les engagements qu'ils
créent et règlent — pont direct vers les contrats comportementaux du § 7.1.5.

⚠ **La leçon d'adoption est tout aussi instructive, et elle vaut avertissement** : le formalisme
lourd de cette lignée **n'a jamais connu de déploiement à grande échelle**. Ce constat plaide, pour
la pile agentique actuelle, en faveur de **mécanismes plus légers que des logiques mentalistes
complètes**.

> **Perspective recherche.** Le déplacement de la sémantique mentaliste vers une sémantique
> d'engagements constitue **le précédent théorique le plus pertinent** pour l'interopérabilité
> agentique contemporaine : il troque une signification fondée sur des états internes inaccessibles
> contre une signification fondée sur des **obligations sociales observables et vérifiables**. Cette
> filiation éclaire pourquoi le grand modèle de langage — qui **infère** le sens à la lecture plutôt
> qu'il ne le calcule formellement — **réintroduit, sous une autre forme, le problème de
> vérifiabilité** que la lignée mentaliste n'avait pas résolu.

### 7.2.2 Taxonomie des quatre axes d'interopérabilité

La couche agentique s'organise autour de **quatre axes**, qui constituent la carte du mouvement :

| Axe | Nature | Ce qu'il porte | Où il est traité |
| --- | --- | --- | --- |
| **Agent-outil** | vertical | un agent invoque des outils et ressources pour étendre ses capacités | ch. 8 § 8.1-8.3 |
| **Agent-agent** | horizontal | des agents autonomes se délèguent des tâches par-delà les frontières | ch. 8 § 8.4-8.6 |
| **Agent-humain** | — | négociation de l'interaction : points de validation, consentement, modalités | Livre II |
| **Agent-données** | — | accès gouverné aux données, récupération inter-organisationnelle | ch. 2, ch. 9 § 9.4 |

: Tableau 7.2 — Les quatre axes de l'interopérabilité agentique et leur lieu de traitement dans la somme.

⚠ **Cette quadripartition n'est pas une cloison étanche** : un système de production mobilise
simultanément plusieurs axes (ch. 9 § 9.2.4). Elle fournit le squelette analytique du mouvement et
fixe le périmètre de chaque chapitre.

⚠ **Elle est aussi le socle amont d'un instrument du Livre II.** La **grille des cinq questions** du
ch. 14 se construit sur cette taxonomie ; le lecteur qui la rencontrera là-bas doit pouvoir en
retrouver la racine ici. C'est l'une des économies de la refonte, et elle suppose que ce paragraphe
ne disparaisse pas d'une révision ultérieure.

### 7.2.3 Panorama introductif des modes d'échec

Avant d'examiner chaque axe, il est utile de poser le cadre des modes d'échec spécifiques. **Six
familles** se dégagent, dont la taxonomie complète est au **ch. 11** :

- **la dérive sémantique en chaîne de délégations** — à mesure qu'une intention est retransmise
  d'agent en agent, son sens **se déforme insensiblement**, chaque relais réinterprétant un message
  en langue naturelle ;
- **l'échec d'ancrage** — un terme n'est pas rattaché au même référent par l'émetteur et le
  récepteur, **qui croient pourtant s'entendre** ;
- **l'ambiguïté non résolue** — un acteur agit sur une interprétation arbitraire **au lieu de
  demander une clarification**, faute de mécanisme de négociation déclenché ;
- **les capacités mal décrites ou mal versionnées** — une description inexacte ou périmée conduit à
  un mauvais appariement ;
- **le non-déterminisme propageant des erreurs non reproductibles** — une faute survenue à une
  frontière **ne se reproduit pas à l'identique**, ce qui en complique le diagnostic ;
- **la perte de portabilité** — une intégration fonctionnelle avec un fournisseur cesse de l'être
  avec un autre, faute de contrat partagé.

Ces familles forment la trame que le mouvement spécifie axe par axe, en remontant chaque défaillance
**au contrat établi — ou défaillant — entre les acteurs**.

---

## § 7.3 — Chronologie 2024-2026 : dix-sept mois de consolidation

Une institution financière ne bâtit pas son architecture sur le produit d'un seul éditeur sans se
demander **ce qu'il adviendra s'il change d'avis**. La question n'a rien de théorique : elle est au
cœur du risque de tiers, elle figure dans les questionnaires de diligence raisonnable, et **elle
décide souvent, seule, de la mise en production**.

C'est pourquoi cette chronologie n'est pas une chronique d'initiés : elle est la **condition
préalable** au reste de la somme.

⚠ **Cette chronologie s'ordonne par protocole, non par date de lancement — et l'ordre importe,
parce que les versions v0.1 à v0.5 du plan portaient une flèche « MCP → A2A → AGNTCY » qui était
fausse dans les deux lectures.** Elle était fausse comme ordre de lancement, et fausse comme ordre de
passage sous fondation. Les deux séquences sont **inverses l'une de l'autre**, et c'est le fait le
plus instructif de la section.

**Lancements.** Le point de départ est **novembre 2024** : publication du protocole agent-outil, une
interface client-serveur destinée à l'invocation d'outils et à l'échange de données typées, assortie
d'un **cadre d'autorisation** — le protocole naît propriétaire au sens strict : un éditeur, une
spécification, un intendant.

L'essaimage est rapide, et **deux initiatives apparaissent presque simultanément en mars 2025** :
une **couche d'infrastructure** — annuaires de découverte et transport dédié — explicitement pensée
comme complémentaire des protocoles d'échange plutôt que rivale ; et, le **17 mars 2025**, un
**protocole de communication entre agents** — l'ACP protocolaire d'IBM Research et du projet BeeAI,
sigle toujours qualifié (§ 7.5) —, en version pré-alpha et d'abord conçu comme une extension du
protocole agent-outil.

En **avril 2025** paraît le protocole **agent-agent**, qui traite un problème distinct : non plus
l'accès d'un agent à ses outils, mais la **délégation de tâches de pair à pair**, au moyen de
descripteurs appelés **cartes d'agent**. En **septembre 2025** s'y ajoute un protocole compagnon
dédié aux **transactions pilotées par agents**, dont le ch. 10 traite.

⚠ **Le protocole d'infrastructure de mars 2025 est donc antérieur au protocole agent-agent d'avril
2025.** L'ordre inverse, longtemps répété, ne résiste pas aux dates.

**Passages sous fondation — et l'ordre s'inverse.** **Juin 2025** : le protocole agent-agent est
transféré à une fondation neutre **sous licence permissive**. **29 juillet 2025** : la couche
d'infrastructure suit. **29 août 2025** : l'ACP protocolaire **fusionne officiellement** dans le
protocole agent-agent — le développement actif cesse, ses actifs y sont versés, des guides de
migration sont fournis. **Décembre 2025**, enfin : la gouvernance du protocole agent-outil est
transférée à une fondation dédiée, elle-même sous la même faîtière ; son créateur **demeure le
créateur, mais cesse d'en être l'unique intendant**.

De novembre 2024 à **avril 2026** — date à laquelle un bilan public de la première année du protocole
agent-agent est dressé —, **dix-sept mois** s'écoulent. En dix-sept mois, quatre protocoles nés dans
quatre entreprises différentes ont convergé vers **deux fondations, dont l'une héberge l'autre**.

⚠ **Un mot sur ce que cette chronologie a rendu caduc, et c'est le garde-fou R-1 du Vol. II.** Un
survey académique de référence proposait une trajectoire d'adoption séquentielle plaçant l'ACP
protocolaire en deuxième étape. **La fusion d'août 2025 a vidé cette étape de sa substance moins de
quatre mois après la publication.** Le document conserve toute sa valeur de **jalon
historiographique** — il documente ce qu'un observateur informé pouvait raisonnablement croire au
printemps 2025 — mais **il ne peut plus servir de guidance d'architecture**. Le ch. 10 § 10.6 en fait
son objet. *La vitesse à laquelle il s'est périmé est elle-même une donnée sur le domaine, et un
avertissement pour la somme.*

⚠ **Et la stabilité d'une gouvernance ne signifie pas l'immobilité d'une spécification** : à la date
de gel du Vol. II, une **révision majeure du protocole agent-outil était attendue douze jours plus
tard**. Le ch. 8 porte cette réserve comme condition de lecture de son anatomie.

---

## § 7.4 — Gouvernance comparée : ce que « neutre » veut dire

### 7.4.1 Trois arrangements sous une destination commune

La destination commune masque **trois arrangements distincts**, et la nuance importe pour qui doit
documenter une dépendance technologique dans un dossier de conformité.

Deux protocoles relèvent **directement** de la fondation faîtière ; le troisième relève d'une
**fondation dédiée** formée en décembre 2025 et **hébergée par** la première. ⚠ **La différence est
de degré, non de nature** : dans les trois cas, la propriété intellectuelle et le processus de
décision **quittent l'entreprise fondatrice**. Pour l'architecte, la conséquence pratique est
identique — *la disparition ou le revirement stratégique du créateur ne fait plus disparaître le
protocole*.

Encore faut-il préciser ce que « quitter l'entreprise fondatrice » recouvre, car **c'est ici que se
joue la valeur du transfert** pour une institution réglementée. Le socle documente un élément
décisif : le protocole agent-agent a été versé **sous licence permissive**, irrévocable, assortie
d'une **concession expresse de brevets**.

Cette précision, d'apparence technique, porte une **garantie juridique concrète**. L'institution qui
construit sur ce protocole n'obtient pas seulement la *probabilité* qu'il survive à son créateur ;
elle obtient le **droit opposable** de continuer à l'utiliser, de le modifier, et — dans l'hypothèse
la plus défavorable — **d'en poursuivre elle-même le développement** si la fondation venait à
l'abandonner. C'est exactement le type de garantie qu'un dossier de risque de tiers cherche à
établir, et **que nulle assurance contractuelle d'un éditeur ne procure au même degré**.

Lecture de l'auteur — le passage sous fondation neutre **transforme la nature de la question posée en
diligence raisonnable**. Devant un protocole propriétaire, l'institution doit évaluer la solidité
financière, la stratégie et les intentions d'une entreprise : un exercice de **prospective**. Devant
un protocole sous licence permissive et gouvernance multipartite, elle évalue la vitalité d'un projet
et la robustesse de ses règles : un exercice de **constat**. Le socle ne l'établit pas ; il en
fournit les éléments — transfert d'intendance, licence, composition du comité.

Le comité de pilotage technique du protocole agent-agent mérite l'examen le plus attentif, parce que
**c'est le lieu où se décide concrètement l'évolution**. Le socle en documente la **composition** :
huit organisations, dont **les trois grands fournisseurs d'infonuagique public ensemble**, alors
qu'ils sont concurrents frontaux sur à peu près tout le reste — et le créateur du protocole **au même
titre que les sept autres**.

Lecture de l'auteur — une instance où siègent huit organisations concurrentes, **dont aucune n'est le
créateur en position dominante**, offre à un tiers évaluateur une garantie **qualitativement
différente** de celle d'un comité consultatif convoqué par un éditeur. ⚠ Le socle établit une
**composition**, non un **règlement intérieur** : ni la répartition des droits de vote, ni les règles
de décision. **L'inférence porte sur la structure, pas sur la procédure**, et elle mérite d'être
vérifiée par toute institution qui en ferait un argument de dossier.

La présence, à ce comité, de l'organisation qui portait l'ACP protocolaire illustre le mécanisme de
la consolidation mieux qu'aucune déclaration d'intention : elle **n'y est pas arrivée par adhésion,
mais par fusion**. Trois mois après avoir présenté son protocole comme complémentaire, elle en versait
les actifs, arrêtait le développement, et sa responsable entrait au comité de pilotage de l'absorbant.
*Un concurrent déclaré est devenu un codécideur* — trajectoire inverse de la fragmentation que le
domaine redoutait, jouée en un trimestre.

⚠ **De cet épisode découle une règle de rédaction qui vaut pour toute la somme (R-1 du Vol. II) :
l'ACP protocolaire ne doit jamais être présenté comme un standard vivant.** Son développement actif a
cessé ; il ne subsiste qu'à travers le protocole absorbant et des adaptateurs.

⚠ **Ce qui frappe enfin, c'est la régularité des trajectoires** : quatre mois pour la couche
d'infrastructure, deux pour le protocole agent-agent, treize pour le protocole agent-outil — le plus
lent des trois. **Aucun des protocoles étudiés n'est demeuré propriétaire au-delà de treize mois.**
Lecture de l'auteur — on peut y lire une conviction partagée du secteur : dans un domaine où la
valeur naît de l'interconnexion, **la propriété exclusive d'un protocole détruit plus de valeur
qu'elle n'en capte**. Le socle ne l'établit pas.

### 7.4.2 Les fondations neutres et ce qu'elles hébergent

Le passage d'un protocole du contrôle de son auteur vers une fondation neutre est, dans l'histoire de
l'interopérabilité, **le signal de maturation le plus fiable** (ch. 1 § 1.2.2).

La fondation dédiée accueille **au même endroit** le protocole agent-outil, un environnement
d'exécution d'agents et un format de configuration d'agent (ch. 5 § 5.1.4) — c'est-à-dire des
contributions de **fournisseurs directement concurrents**. Le mécanisme de la faîtière — comité
technique de pilotage, charte de neutralité — **découple la spécification de tout acteur unique**, et
c'est ce découplage institutionnel qui **rend crédible** la politique de dépréciation formelle du
ch. 8 § 8.3.

Une seconde fondation, spécialisée dans l'authentification, prend une importance qui n'apparaîtra
qu'au ch. 10 : c'est elle qui a reçu le **protocole de transaction**, le **28 avril 2026**.

⚠ **Ce fait est porté par le Vol. I *Monographie* §3.13.1, au régime [C], et le socle du Vol. II ne
le documentait pas** — *absence de documentation*, **degré 3 de l'échelle R-14 du Vol. III**, et non
une négation. Les deux énoncés sont **compatibles**, et le **ch. 10 § 10.1.3** en instruit l'écart. ⚠ **Une version antérieure de ce passage écrivait « annoncé, non vérifié au socle »** : la
formule suivait le plan et le Vol. II sans lire jusqu'au bout le §3.13.1 du Vol. I, qui est pourtant
l'une des sources de ce chapitre. **Corrigé ; remontée R-IV-12 ouverte au ch. 10 § 10.7.**

L'analogie volontiers invoquée est celle d'un projet d'infrastructure antérieur donné tôt à une
fondation : **un projet d'éditeur dominant attire des contributeurs concurrents précisément parce que
sa neutralité est garantie**.

---

## § 7.5 — Encadré de désambiguïsation : la collision à quatre branches

> ⚠ **SIÈGE DU GARDE-FOU R-8 POUR TOUTE LA SOMME.** Cet encadré est **posé ici une seule fois**. Le
> ch. 10, qui reçoit par ailleurs le chapitre source du Vol. II dont il provient, **y renvoie sans le
> reconstruire** — c'est un partage déclaré (décision 6 du TOC), et l'un des deux écarts que la
> révision v0.17 du plan a soldés.

Le sigle **« ACP »** désigne **au moins quatre objets distincts**, tous actifs, et le garde-fou R-8
du Vol. II — comme R-13 du Vol. III — **proscrit son emploi nu dans tout l'ouvrage**. Chaque emploi
porte son qualificatif complet.

| | Objet | Statut |
| --- | --- | --- |
| **(a)** | **l'ACP protocolaire** — *Agent Communication Protocol* d'IBM Research et BeeAI | fusionné dans le protocole agent-agent en août 2025 ; ⚠ **jamais un standard vivant** (R-1) |
| **(b)** | l'**Agentic Control Plane** d'un consortium d'institutions financières et de télécommunications | programme annoncé en juillet 2026 ; traité au Livre III |
| **(c)** | l'expression **agentic control plane** employée par un éditeur pour positionner un produit d'orchestration | positionnement commercial ; traité au Livre III |
| **(d)** | la **composante ACP** de la couche d'infrastructure agentique | ⚠ **ni intitulé complet ni identité établis** — voir la lacune ci-dessous |

: Tableau 7.3 — Les quatre branches de la collision « ACP » / « (agentic) control plane », et le statut de chacune.

⚠ **Le socle n'établit l'absence de lien que pour un seul de ces couples**, et il faut être précis
sur ce que « distincts » recouvre. Une entrée du socle du Vol. II pose que l'*Agentic Control Plane*
du consortium **n'a aucun lien** avec l'ACP protocolaire — **pure homonymie**, et c'est un fait
établi. Sur le couple **(a)/(c)**, en revanche, **le socle ne dit rien de tel, et le silence mérite
d'être relevé plutôt que comblé** : ce sont **deux objets du même éditeur**, et rien n'établit qu'ils
soient étrangers l'un à l'autre — **ni qu'ils soient liés**. C'est une **absence de documentation**
au sens de R-14 du Vol. III, **non un fait négatif vérifié**.

⚠ **Lacune héritée, portée et non comblée** *(PRD du Vol. II §10.7)*. La **quatrième branche (d)**
est relevée lors de la rédaction du chapitre source : le socle mentionne une « composante ACP »
propre à la couche d'infrastructure, dont des **analyses tierces** relèvent un chevauchement avec le
protocole agent-agent. **Le socle n'établit ni son intitulé complet, ni son identité — ou sa
non-identité — avec l'ACP protocolaire.** En l'absence de source primaire, la somme **ne tranche
pas** : elle désigne cet objet par « la composante ACP de la couche d'infrastructure », **toujours
qualifié**, et s'interdit de l'agréger aux trois autres.

Cette lacune est **portée ici, encadrée, et renvoyée au ch. 49** pour son état final. Elle n'est pas
comblée — et la combler par une analyse tierce serait précisément la faute que la règle du dépôt
proscrit : *aucune lacune déclarée ne se comble par une source de moindre qualité*.

---

## § 7.6 — Lecture critique des métriques d'adoption : « soutien » n'est pas « production »

Il reste à examiner **les chiffres par lesquels ces protocoles annoncent leur réussite**, et à le
faire avec une sévérité que la littérature promotionnelle ne s'impose pas.

Les données disponibles sont les suivantes, **et chacune est attribuée à sa source, comme elle doit
l'être à chaque occurrence** (PRD du Vol. II §8.2.1). En **avril 2026**, **la Linux Foundation —
fondation faîtière des deux protocoles — annonce que plus de 150 organisations déclarent leur
soutien** au protocole agent-agent, contre plus de 50 au lancement. Un **communiqué de la même
fondation du 29 juillet 2025** fait état de **plus de 65 entreprises** déclarant leur soutien à la
couche d'infrastructure.

⚠ **Ces deux chiffres ne se rapprochent pas** : plus de huit mois les séparent, et le socle
n'enregistre **aucune actualisation ultérieure** du second. Les comparer serait fautif.

Ces chiffres sont réels, datés, adossés à des communiqués officiels. Ils sont aussi — **et c'est là
tout le problème** — **auto-déclarés**.

**Trois réserves s'imposent, par ordre de gravité croissante.**

**La première : la notion même d'« organisation de soutien » n'est définie nulle part.** Elle ne
distingue pas l'entreprise qui a inscrit son logo sur une page d'annonce de celle qui a affecté une
équipe d'ingénierie au protocole pendant un an. *Une métrique dont l'unité n'est pas définie ne
mesure rien de vérifiable* ; elle indique une **direction**, pas une **grandeur**. Un responsable de
la conformité qui recevrait un tel chiffre à l'appui d'une décision d'architecture serait fondé à
demander ce qu'on y a compté — **et ne trouverait pas la réponse dans la source**.

**La deuxième : le soutien déclaré ne vaut pas déploiement en production.** C'est la réserve
centrale, et elle traverse toute la somme. Un architecte qui lirait le chiffre d'avril 2026 comme
« 150 systèmes agentiques interopérables en exploitation » **commettrait une erreur de catégorie**.
Le Livre III établit que le nombre d'institutions financières canadiennes documentant par sources
primaires un déploiement agentique **se compte sur les doigts de deux mains**. ⚠ *L'écart entre les
deux ordres de grandeur — la centaine d'organisations qui déclarent leur soutien à un protocole
mondial, la poignée d'institutions qui documentent une mise en production — est l'un des
enseignements les plus robustes de la somme.*

**La troisième porte sur la croissance elle-même.** Le passage de plus de 50 à plus de 150
organisations en douze mois, **tel que la Linux Foundation le rapporte en avril 2026**, est un
triplement apparent. Mais **un triplement d'une grandeur non définie reste non défini**. La progression établit
qu'un nombre croissant d'organisations jugent utile d'**associer publiquement leur nom** au
protocole : information sur la **dynamique** du domaine, non sur sa **maturité technique**.

**Faut-il pour autant écarter ces chiffres ? Non — et il serait malhonnête de le faire.** Ils
constituent le meilleur indicateur public disponible de **l'attention** que le secteur porte à ces
protocoles, et cette attention est elle-même un fait pertinent pour une institution qui évalue le
risque de pérennité d'un standard. Un protocole auquel plus de 150 organisations déclarent leur
soutien **a peu de chances d'être abandonné dans les dix-huit mois**. *C'est exactement ce que ces
chiffres établissent, et rien de plus.*

⚠ **Le lecteur exigeant en retiendra la portée exacte.** La **composition du comité de pilotage
technique** — huit organisations concurrentes — est un indicateur de gouvernance **nettement plus
solide** que le décompte des soutiens : ses membres sont **nommés**, leur engagement est
**vérifiable** dans les dépôts publics, et leur nombre restreint **interdit la comptabilité
complaisante**. *Quand la somme devra juger de la pérennité d'un protocole, elle regardera qui
décide, non combien applaudissent.*

**Ce que ce chapitre établit — trois acquis pour la suite du mouvement.** *(1)* La couche protocolaire
agentique **est sortie du régime propriétaire** : aucun des quatre protocoles retenus ici n'est
gouverné par son créateur seul. ⚠ **La restriction est importante et elle est celle de la thèse** :
elle **s'étend au protocole de transaction, mais par une seconde fondation** — celle qui est
spécialisée dans l'authentification, et qui l'a reçu le **28 avril 2026** (Vol. I *Monographie*
§3.13.1, régime **[C]** ; ch. 10 § 10.1.3). ⚠ **Le socle du Vol. II, lui, n'en documentait aucun
transfert** — *absence de documentation*, et **non un fait négatif vérifié** : une lacune de
couverture ouverte à son registre, non une propriété établie. Les deux énoncés sont **compatibles**,
et le ch. 10 § 10.1.3 en tire la règle de lecture. ⚠ **La conséquence pour la thèse n'est pas une
révision mais une précision** : la couche protocolaire est sortie du régime propriétaire **par
plusieurs fondations distinctes, organisées par axe**, non par une seule. *(2)* La consolidation ne s'est pas faite par coexistence polie **mais par
fusion réelle**. *(3)* Les métriques publiées mesurent **l'attention, non la production**.

**Ce que ce chapitre ne dit pas mérite d'être énoncé aussi clairement.** Il ne dit pas que ces
protocoles sont **sûrs** : la gouvernance neutre ne préjuge en rien de la robustesse d'une
implémentation, et le ch. 11 expose les surfaces d'attaque que le socle **nomme** — sans en dater la
documentation ni en établir la mécanique. Il ne dit pas que les protocoles agent-outil et agent-agent
soient interchangeables ni concurrents : le ch. 8 § 8.6 examine la doctrine de complémentarité qui les
articule, **et par qui elle est déclarée**. Il ne dit pas enfin que la neutralité de la gouvernance
**suffise** à emporter la décision d'une institution réglementée — c'est l'objet du Livre III que
d'établir tout ce qu'il faut y ajouter.

*La consolidation protocolaire est le point de départ du mouvement. Elle n'en est pas la conclusion.*

---

## § 7.7 — Note de statut *(hors plan — à retirer à la publication)*

⚠ **Cette section n'est pas au TOC et n'a pas vocation à survivre.**

**Ce qui est enfreint** — portes **G-1**, **G-2**, **G-3** ouvertes ; rédaction sur instruction
d'auteur du 27 juillet 2026. Conséquences habituelles, plus deux propres à ce chapitre :

1. **Aucun énoncé n'est central au sens de CA-IV-01.**
2. **Les décomptes sont publiables depuis le 27 juillet 2026** — G-2 franchie, `PRD/decompte.sh` versionnée et éprouvée sur les trois corpus entiers.
3. **Les renvois « ch. N » sont des renvois de plan** — ch. 8-11, 14, 49 et le Livre III non rédigés.
4. **⚠ Deux régimes de socle coexistent dans ce chapitre, et G-3 devra les fondre.** C'est le premier
   du Livre I à consommer le Vol. II : ses entrées **conservent leur niveau** [A]/[B]/[C], là où
   celles du Vol. I entrent en [C]. Tant que la renumérotation de G-3 n'est pas publiée, **les
   identifiants restent préfixés de leur volume** — un « F-01 » nu serait indécidable entre les deux
   socles. Le chapitre s'y tient et ne cite aucun identifiant nu.
5. **⚠ Le chapitre porte deux gels de source distincts** — juin 2026 et 16 juillet 2026 — et une
   révision protocolaire majeure était attendue **douze jours après le second**. La chronologie du
   § 7.3 est exacte **à sa date** et le déclare.

**Remontées ouvertes par ce chapitre :**

- **R-IV-08 — non bloquante, à échéance G-1, et de conséquence thétique. ⚠ INSTRUITE PAR LE CH. 10,
  ET LE DÉFAUT ÉTAIT ICI.** *Rédaction d'origine :* le statut du transfert de gouvernance du protocole
  de transaction était donné pour **annoncé, non vérifié au socle**, à instruire si une source
  primaire datée était extraite.

  ⚠ **Elle ne l'était pas : la source était déjà dans le périmètre de fusion de ce chapitre.** Le
  **Vol. I *Monographie* §3.13.1** — l'une des trois sources assignées à ce chapitre — porte le
  transfert comme **fait daté et sourcé** (28 avril 2026). Ce chapitre l'avait manqué en suivant le
  plan et le Vol. II sans lire jusqu'au bout sa propre source du Vol. I. **Le § 7.4.2 et le § 7.6 sont
  corrigés** ; l'instruction complète est au **ch. 10 § 10.1.3**, et la **remontée R-IV-12** y porte
  la demande de réalignement du plan au titre de la décision 8.

  ⚠ **À la rédaction, la thèse citée en tête est restée inchangée, et c'était délibéré** : elle était
  **citée verbatim depuis le TOC v0.23**, et un rédacteur ne corrige pas le TOC — il remonte. Sa
  dernière clause (« AP2 n'a aucun transfert de gouvernance documenté ») était **exacte du point de
  vue du socle du Vol. II** et **périmée du point de vue du Vol. I** ; l'écart était exposé au § 7.6
  et instruit au ch. 10. ⚠ **La thèse a depuis été réalignée au TOC v0.24 sur cette remontée, et le
  bloc de tête a été re-cité depuis le TOC v0.28 le 28 juillet 2026** : *la citation porte désormais
  la forme réalignée, et la comparaison mot à mot avec le plan courant résout.*

  *Leçon de méthode, portée au skill de rédaction : une pièce ne se rédige pas sur la seule source que
  le plan met en avant, mais sur l'intégralité de son périmètre de fusion.*
- **R-IV-09 — non bloquante.** Le § 7.5 est le **siège** de l'encadré de désambiguïsation pour toute
  la somme, et le ch. 10 doit s'y **renvoyer sans le reconstruire**. Aucun contrôle outillé ne
  vérifie cette abstention — même classe que R-IV-05, ouverte au ch. 3 pour le socle IAM. **Un motif
  de balayage inter-pièces couvrirait les deux**, et reste à construire en G-3.

**Ce qui n'est pas enfreint.** La structure suit la table détaillée du TOC (§ 7.0 à § 7.6) ; la table
de couverture est respectée, dont les **deux sorties de périmètre vers le ch. 49** — le reste du
§3.13 du Vol. I et le §7.3 — et le **siège de l'encadré R-8 en § 7.5**. La **thèse est citée dans sa
forme intégrale**, restriction « et non suffisante » comprise. La chronologie est ordonnée **par
protocole**, avec les deux séquences inverses explicitées. Les **métriques auto-déclarées du § 7.6
sont attribuées**, R-1 est tenu à ses trois occurrences, le sigle à quatre branches est **toujours
qualifié**, et la lacune héritée est **encadrée sans être comblée**.

---

### Clôture des remontées — 27 juillet 2026

⚠ **Cette sous-section est hors plan comme la note qui la porte, et se retire avec elle.** Elle
enregistre l'issue des remontées ouvertes par cette pièce. *Une remontée ne se clôt pas là où elle
s'ouvre : elle se solde là où elle fait foi* — au [PRD](../PRD/PRD.md) pour une décision d'auteur, au
[TOC](../PRD/TOC.md) pour un réalignement de plan, à l'appareil pour une dette d'outillage.

- **R-IV-08 — close par réalignement du plan (décision 8).** La **thèse du ch. 7 est amendée au TOC
  v0.24** : sa dernière clause tenait qu'AP2 n'avait aucun transfert de gouvernance documenté ; le
  transfert est **établi à la source primaire** (28 avril 2026, v0.2, cas *Human-Not-Present*, deux
  groupes de travail techniques — registre du gel, fait 12). ⚠ **La clause n'est pas effacée mais
  située** : exacte du point de vue du socle du Vol. II, périmée du point de vue du Vol. I. *Le
  volume le plus ancien ne se corrige pas ; sa lacune de couverture est une information datée.* Le
  § 7.4.2 et le § 7.6 de cette pièce, déjà corrigés, résolvent désormais contre un plan qui dit la
  même chose qu'eux.
- **R-IV-09 — close par versement d'appareil**, du même mouvement que R-IV-05 :
  [`PRD/check-sieges.py`](../PRD/check-sieges.py) vérifie qu'aucune pièce ne reconstruit l'encadré du
  § 7.5 et que toute pièce touchant la matière y renvoie. ⚠ **Il a trouvé un défaut réel au premier
  passage** — le ch. 6 § 6.2 développait le sigle sans pointer vers l'encadré —, corrigé. *Le
  contrôle qui manquait n'était pas un contrôle de plus : c'était le seul qui lisait les pièces
  ensemble.*

⚠ **Ce que la clôture ne change pas.** La porte **G-3** demeure ouverte : le socle consolidé compte
**zéro entrée**, l'Annexe B n'existe pas, et **aucun énoncé de cette pièce n'est central au sens de
CA-IV-01**. Cette pièce reste un **brouillon non publiable**. *Zéro remontée ouverte ne veut pas dire
pièce recevable — cela veut dire qu'aucune question n'attend plus de réponse qui ne soit déjà
tranchée.*
