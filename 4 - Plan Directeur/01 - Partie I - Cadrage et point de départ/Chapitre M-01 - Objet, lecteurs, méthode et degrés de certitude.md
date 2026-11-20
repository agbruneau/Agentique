# Chapitre M-1 — Objet, lecteurs, méthode et degrés de certitude

*Question directrice : Comment écrire sur neuf années à venir sans prétendre les connaître?*

> **État de référence (16 novembre 2026) :** Ce chapitre arrête la posture éditoriale, les conventions de preuve, l’appareil de marques temporelles et la méthode de planification adaptative de l’ouvrage à la clôture documentaire du 16 novembre 2026.

Écrire en novembre 2026 un document d’architecture couvrant la période 2028-2035 oblige à embrasser neuf années d’évolution technique, normative et prudentielle à partir d’un présent où les premiers protocoles d’agents viennent à peine de se stabiliser (C27, § 4.4) et où la principale mesure publique de leur portée autonome a cessé d’être actualisée en septembre 2026 par saturation de son banc d’essai [1]. Deux écueils symétriques guettent l’exercice. Le premier prolonge en ligne droite les annonces commerciales récentes et fige, sous forme d’exigences pseudo-normatives ou de jalons trimestriels arbitraires, un état de l’art imaginaire. Le second s’en tient à des maximes si abstraites qu’aucun architecte d’institution financière ne peut en tirer un ordre de construction, un plafond de risque par domaine d’affaires ni un critère d’arbitrage.

Le présent ouvrage écarte ces deux impasses par une discipline explicite de la preuve et du temps. Chaque affirmation portant sur l’avenir déclare si elle découle d’un texte adopté fixant une date, d’une annonce révocable d’organisme ou d’éditeur, d’une conjecture rattachée à un scénario et à un signal observable, ou d’un choix prescriptif de conception. Au lieu de supposer l’avenir connu, l’architecture cible isole ce qui ne dépend pas de la trajectoire des modèles — le plan de contrôle que l’institution possède — et organise le reste en parcours adaptatifs franchis sur preuve [2].

## 1.1 Positionnement de l’ouvrage et frontières du périmètre

### 1.1.1 Du Compendium 2027 à l’horizon 2028-2035

Le *Compendium 2027* (ci-après C27) dressait un état de l’art opérationnel à dix-huit mois : protocoles d’accès aux outils et de coordination entre pairs, ingénierie du contexte et de la mémoire, patrons d’exécution durable, identités non humaines, observabilité et premiers textes encadrant l’intelligence artificielle au Canada, au Québec et en Europe (C27, § 1.5, § 4.4). Sur un horizon court, l’analyse s’appuyait directement sur des spécifications publiées [15], des études empiriques de déploiement [3] et des échéances imminentes comme l’entrée en vigueur de la ligne directrice E-23 révisée du Bureau du surintendant des institutions financières (BSIF) le 1er mai 2027 D [4].

Étendre la perspective à la période 2028-2035 — l’année 2027 servant d’année pont entre l’arrêt des faits et l’ouverture du premier palier — change la nature du problème architectural. Les produits commerciaux, les cadriciels d’orchestration et les révisions mineures de protocoles qui structurent un projet annuel seront remplacés ou remaniés bien avant le terme (C27, § 20.6, § 49.3). En revanche, les obligations qui lient une banque, un courtier en valeurs mobilières, une société de fiducie ou un assureur s’inscrivent dans la durée : conservation septennale des dossiers et des communications supervisées en valeurs mobilières [5], tenue des livres au Canada et échéance légale d’exercice des banques fédérales fixée au 30 juin 2033 D [6], engagements viagers en assurance de personnes, migration post-quantique imposée aux administrations publiques fédérales jusqu’à la fin de 2035 D [7] et feuille de route coordonnée du secteur financier du G7 sur la période 2028-2035 A [8].

### 1.1.2 Choix du genre : pourquoi cinq autres formes ont été écartées

Six genres documentaires ont été évalués au regard de leur utilité pour une institution financière réglementée et de leur résistance au vieillissement (C27, § 43.2).

| Genre documentaire envisagé | Verdict | Motif méthodologique et opérationnel |
| --- | --- | --- |
| **Compendium, troisième édition** | Écarté | On ne synthétise pas l’état de l’art d’années futures; compiler des conjectures sous l’apparence d’une revue encyclopédique brouillerait la frontière entre constat établi et projection. |
| **Cadre normatif de long terme** | Écarté | Des exigences opposables rédigées fin 2026 pour la fenêtre 2028-2035 vieilliraient en un an face aux révisions protocolaires et réglementaires. |
| **Plan directeur interne d’une institution** | Écarté | Un plan propre à une entreprise suppose un parc applicatif singulier, des budgets, des effectifs et des arbitrages d’achat internes. |
| **Étude prospective seule** | Insuffisant | Éclairer les futurs possibles et les signaux externes sans les traduire en capacités cibles ni en séquence de construction laisse l’architecte sans prise opérationnelle. |
| **Architecture cible seule** | Insuffisant | Une cible décrite sans profils sectoriels ni paliers efface les écarts juridiques entre banque, patrimoine et assurances, et tait l’ordre des préalables. |
| **Architecture stratégique et plan directeur de référence** | **Retenu** | Réunit une prospective vérifiable, une cible en capacités dotées d’identifiants stables, cinq profils sectoriels comparables, trois paliers franchis sur preuve et un dispositif de révision. |

Le statut de l’ouvrage demeure **informatif** : il oriente sans imposer. Il n’ajoute aucune règle obligatoire à un référentiel existant; lorsqu’un profil sectoriel met au jour un besoin propre aux agents, il formule une **proposition d’exigence** motivée qui prépare une révision normative ultérieure sans la préempter.

### 1.1.3 Périmètre couvert et exclusions explicites

Le périmètre couvre les **services financiers réglementés au Canada**, dans leurs quatre sous-secteurs — **banque et coopératives de dépôt** (`M-14`), **gestion de patrimoine** (`M-15`), **assurance de personnes** (`M-16`), **assurance de dommages** (`M-17`) — et le **groupe financier diversifié** (`M-18`). Il embrasse les institutions fédérales supervisées par le BSIF [4], l’Agence de la consommation en matière financière du Canada (ACFC) et la Banque du Canada pour les services bancaires axés sur les consommateurs [9], les entités et groupes coopératifs québécois supervisés par l’Autorité des marchés financiers (AMF) [10], ainsi que l’encadrement des Autorités canadiennes en valeurs mobilières (ACVM) et de l’Organisme canadien de réglementation des investissements (OCRI) [5].

Sur le plan juridique, l’ouvrage établit un **profil fédéral et québécois en profondeur** — intégrant notamment la Loi 25 au Québec [11] et la réforme législative du secteur financier québécois [10] — et ne signale les autres provinces que lorsqu’une norme harmonisée pancanadienne s’applique. L’international n’intervient que lorsqu’il lie les activités extérieures d’un groupe canadien, comme le règlement européen sur l’intelligence artificielle révisé en juillet 2026 pour les opérateurs et administrations concernés [12], ou lorsqu’il cadence les fournisseurs mondiaux et la normalisation. L’objet technique porte sur l’interopérabilité, l’orchestration, le contexte, la mémoire, l’identité, la délégation, l’observabilité et la gouvernance des agents, dans l’entreprise et entre organisations (C27, ch. 23).

Six exclusions bornent ce cadre : (1) aucune organisation nommée, réelle ou inventée pour l’illustration — le *Groupe Boréal* du Compendium 2027 (C27, § 1.10) compris — ni aucun chiffrage attribué à un archétype; (2) aucun choix de produit ou d’éditeur dans les prescriptions; (3) aucun plan projet chiffré en budgets ou effectifs; (4) aucun avis juridique; (5) aucune taille de marché propre à l’ouvrage, vu la dispersion des séries commerciales établie au C27 (C27, § 50.1, § 50.2); (6) exclusion des entités non réglementées, des caisses de retraite autonomes et des secteurs non financiers.

## 1.2 Thèse de travail, lecteurs et quatre décisions appuyées

### 1.2.1 La thèse soumise à l’épreuve des sous-secteurs

L’ouvrage repose sur une thèse de travail réfutable : **sur la période 2028-2035, ce que les textes adoptés datent porte sur la preuve — inventaire, traçabilité, explication, supervision humaine, gestion des tiers et cryptographie — et non sur l’autonomie.**

Les sources primaires arrêtées au 16 novembre 2026 convergent sur ce point. Dès le 1er mai 2027, la ligne directrice E-23 du BSIF exige un inventaire des modèles, une notation du risque intégrant le degré d’autonomie, une revue indépendante et un suivi continu de la dérive D [4]. Le bulletin du BSIF de juillet 2026 sur l’IA générative et agentique attend des identités non humaines uniques, des listes blanches d’outils, des points de contrôle d’approbation humaine sur les actes à fort impact, la notification par les tiers et des replis manuels éprouvés [13]. Au Québec, l’article 12.1 de la loi du secteur privé impose, pour toute décision fondée exclusivement sur un traitement automatisé, l’information de la personne, la communication sur demande des principaux facteurs et paramètres menant à la décision et le droit de soumettre des observations à un employé habilité à la réviser [11]. Côté infrastructure de confiance, le

CA/Browser Forum abaisse la validité maximale des certificats TLS publics à 100 jours en mars 2027 puis à 47 jours le 15 mars 2029 D [14], tandis que le Secrétariat du Conseil du Trésor jalonne pour les administrations fédérales l’inventaire cryptographique en 2028 et la bascule post-quantique des systèmes prioritaires fin 2031 puis complète fin 2035 D [7]. Aucun texte n’oblige à rendre un agent autonome; tous imposent de prouver le mandat, le périmètre et le contrôle.

La cible invariante réside dès lors dans le **plan de contrôle possédé par l’entreprise** (registres, identités non humaines, délégation atténuée, politiques déterministes hors modèle, traces assainies et archives probatoires agiles), tandis que **l’autonomie reste la variable conditionnelle**, accordée par domaine d’affaires (`D1` à `D8`) et par classe de décision (`Classe 1` à `Classe 6`). Les cinq profils de la Partie IV (`M-14` à `M-18`) mettent cette proposition à l’épreuve : si un sous-secteur présentait une obligation datée portant sur l’autonomie même, la thèse s’en trouverait corrigée.

### 1.2.2 Lecteurs visés et décisions instruites

Le lecteur principal est l'**architecte d’entreprise** d’une institution financière réglementée, chargé d’en dériver la cible et le plan propres à son établissement. Les lecteurs secondaires appartiennent aux trois lignes de défense (C27, § 39.6) : haute direction technologique, gestion du risque de modèle et de la conformité réglementaire, et audit interne. L’ouvrage appuie **quatre décisions** :

1. **quoi construire d’abord, et quoi différer** le long des trois paliers successifs;
2. **quel stade viser, domaine d’affaires par domaine d’affaires, selon le risque**, le sommet de l’échelle n’étant pas une cible universelle (C27, § 43.1);
3. **quels investissements sont sans regret**, et lesquels dépendent de la réalisation d’un scénario externe;
4. **quand réviser la trajectoire, et sur quel signal** vérifiable (`M-25`).

## 1.3 Discipline du temps et de la preuve : marques, sources et lettres probantes

### 1.3.1 Le bloc comme unité de contrôle et les cinq marques d’énoncé

Pour interdire toute confusion entre fait établi, échéance légale, annonce révocable, projection et prescription, l’unité mécanique de vérification est le **bloc Markdown** (paragraphe, élément de liste, ligne de tableau). L’outillage contrôle cinq marques dont le gabarit est le suivant :

```
[n]                       Constat passé ou présent appuyé sur la source numérotée n du chapitre
[D] [n]                   Énoncé daté : échéance future fixée par un texte officiel adopté
[A] [n]                   Énoncé annoncé : jalon futur publié par un organisme ou un éditeur
[C: scénarios; SIG-nnn]   Énoncé conjecturé : lecture liée à A/B/C/tous et à un signal existant
[P: ID-nnn]               Lieu unique de définition d'une prescription appuyée dans le corps
```

Quatre règles gouvernent leur emploi :

- **Frontière entre daté et annoncé.** Une loi, un règlement officiel ou un scrutin normatif adopté porte la marque d’énoncé **daté**; une feuille de route protocolaire ou une déclaration sectorielle non contraignante porte la marque d’énoncé **annoncé** [8] [16].
- **Encadrement des années postérieures à 2030.** Hors des titres, des grilles de décision, des sections `Limites` et des plages globales `2027-2035` et `2028-2035`, toute mention ponctuelle d’une année de 2031 à 2035 dans le corps doit figurer dans un bloc muni soit d’une marque datée ou annoncée avec sa source — telle la temporisation légale bancaire de 2033 D [6] ou la cible canadienne d’adoption de l’IA fixée à 2034 A [17] — soit d’une marque de conjecture rattachée à un signal de révision C : tous ; SIG-010.
- **Distinction entre administrations publiques et institutions privées.** Lorsqu’un texte ou une ancre ne lie que le secteur public — comme la directive fédérale sur les décisions automatisées visant l’administration fédérale [18], les guides publics canadien et québécois sur l’IA agentique écrits pour les administrations [19], ou les échéances post-quantiques imposées aux administrations canadiennes [7] et américaines [20] — le bloc qui le cite mentionne explicitement les **administrations** concernées.
- **Définition unique des prescriptions.** Chaque identifiant prescriptif est défini une seule fois avec au moins un appui vérifiable dans son bloc, puis cité ailleurs par son code nu.

### 1.3.2 Cinq statuts de lecture, trois voies d’accès et sélection des preuves

Chaque source bibliographique déclare sa date ISO de consultation, l’étendue lue (*lu en entier*, *lu par passages*, *résumé seulement*, ou *non lu* pour une piste) et son statut parmi cinq niveaux :

| Statut | Sens documentaire | Règle d’emploi |
| --- | --- | --- |
| `L+` | Texte brut officiel extrait et vérifié localement (`Master/recherche/textes/<id>.txt`). | **Seul statut admis pour fonder une obligation réglementaire** ou une lettre normative. |
| `L` | Page consultée par l’intermédiaire d’un résumé d’outil sans fichier brut complet. | Admis pour un constat secondaire recoupé; exclu pour toute obligation réglementaire. |
| `C` | Source déjà lue et qualifiée dans le Compendium 2027, non relue à neuf. | Valide pour les rappels sourcés du C27, en conservant ses réserves explicites. |
| `R` | Référence repérée dont la page n’a pas été chargée. | Simple piste ou signal; ne fonde ni fait, ni date, ni obligation; déclarée en `Limites`. |
| `F` | Accès fermé : refus HTTP 403, pare-feu, défi automatisé, session ou licence requise. | Aucune obligation n’en dépend; nommée dans les `Limites` et dans la page *À propos*. |

Trois voies d’accès ordonnées sont pratiquées sans jamais contourner une barrière d’accès : téléchargement direct et extraction locale, page rendue sans défi d’humanité, ou dépôt par l’auteur. Au 16 novembre 2026, soixante-dix-sept textes primaires ont été extraits en statut `L+`, tandis que les fichiers PDF protégés de l’AMF, le corps réservé aux membres de la recommandation UIT-T F.748.93 [21] et les spécifications sous licence de FDX, d’ACORD et du CSIO demeurent classés `F`. Sont écartés comme preuve primaire : les études de marché sans méthode publique (citées seulement en fourchettes datées, C27, § 50.2), les billets de cabinets juridiques (limités au repérage), les pages commerciales d’éditeurs, les reprises de presse, les prépublications non évaluées et les brouillons individuels de l’IETF non adoptés par un groupe de travail [22]. Aucune ancre ne remonte à plus de soixante jours avant la composition finale,

et un tirage déterministe de soixante énoncés (`seed=20282035`) permet leur recollation sur texte brut.

### 1.3.3 Lettres probantes des grilles de décision et règle sur les volets du C27

Chaque ligne des grilles de décision indique la nature de son appui selon quatre lettres :

```
[N] [n]   Texte législatif, réglementaire ou officiel lu en statut L+ (fichier local vérifié)
[M]       Mesure empirique, statistique publique ou étude scientifique évaluée par les pairs
[É]       Spécification, documentation technique ou feuille de route d'un éditeur ou projet
[S]       Synthèse architecturale propre à l'ouvrage lorsqu'aucune source directe ne tranche
```

Par ailleurs, conformément aux conclusions de l’évaluation académique du Compendium 2027, les vingt-huit chapitres du C27 dotés de volets *Mise en œuvre* (trente et un volets portant `ADR-001` à `ADR-031`) ne comportent aucun appel de source propre : **aucune prescription du présent ouvrage ne peut s’appuyer sur un volet *Mise en œuvre* seul**, sans co-citation d’une section d’exposé sourcé du C27 (p. ex. C27, § 19.7, § 27.4, § 33.2, § 40.2) ou d’un texte `L+`.

## 1.4 Planifier sous incertitude profonde : parcours adaptatifs et scénarios sans probabilité

### 1.4.1 Les parcours adaptatifs dynamiques (DAPP) appliqués à l’architecture

Face à neuf années où ni la fiabilité réelle des agents, ni l’ouverture des plateformes, ni la convergence juridictionnelle ne se prêtent à un calcul probabiliste, l’ouvrage applique la méthode des **parcours adaptatifs dynamiques** (*Dynamic Adaptive Policy Pathways*, DAPP) exposée par Haasnoot, Warren et Kwakkel dans l’ouvrage de référence de Marchau et ses coauteurs sur la décision sous incertitude profonde [2]. L’incertitude profonde caractérise les contextes rebelles aux lois de probabilité où un plan maître statique devient obsolète dès que l’environnement s’écarte de la prévision centrale [2]. Chaque choix architectural y possède une durée de validité incertaine et s’analyse à travers quatre notions opératoires :

1. **Seuil de bascule d’adaptation (*Adaptation Tipping Point — ATP*).** Il désigne les conditions dans lesquelles une disposition en service cesse de remplir ses exigences de conformité, de coût ou de sûreté [2] — par exemple lorsque le renouvellement manuel de certificats se heurte au plafond de quarante-sept jours en mars 2029 D [14] ou que la multiplication des agents inter-équipes excède la capacité d’homologation artisanale.
2. **Seuil d’opportunité (*Opportunity Tipping Point*).** Il marque le moment où la maturation d’une norme externe — passage en RFC des profils d’identité d’agent à l’IETF [23], prise en charge matérielle des signatures composites [22] ou validation d’un banc d’évaluation longue durée [1] — rend viable l’ouverture d’un palier d’autonomie jusque-là prématuré [2].
3. **Dépendance au sentier et coûts de transfert (*Transfer Costs*).** L’évaluation porte sur des séquences complètes d’actions et sur le coût de bascule d’une branche à l’autre [2] : déléguer le registre d’identité ou la piste d’audit au plan de contrôle captif d’un fournisseur
  unique crée un coût de sortie dirimant si l’institution doit ensuite fédérer plusieurs suites métiers ou isoler ses états par juridiction (C27, § 27.4, § 46.1).
4. **Signaux (*Signposts*) et déclencheurs (*Triggers*) opportuns et fiables.** Le registre de veille sépare l’indicateur suivi (`SIG-nnn`) et le seuil d’action qui précède le point de rupture d’un délai suffisant de mise en œuvre (*lead time*), en respectant les critères d’opportunité temporelle (*timely*) et de fiabilité (*reliable*) sur les forces motrices amont [2].

| Étapes de la méthode DAPP [2] | Réalisation dans les six parties de l’ouvrage |
| --- | --- |
| **1. Cadrage et incertitudes majeures** | Parties I et II (`M-1` à `M-8`) : périmètre canadien-québécois, contraintes externes et scénarios. |
| **2. Vulnérabilités de départ et seuils** | Chapitres `M-2` et `M-19` : stades initiaux par domaine et écarts face aux exigences. |
| **3. Actions candidates et validité** | Chapitres `M-9`, `M-10` et `M-13` : principes, capacités cibles et révision des 31 ADR. |
| **4. Évaluation des parcours** | Chapitres `M-11`, `M-12` et Partie IV (`M-14` à `M-18`) : noyau, variantes et profils sectoriels. |
| **5. Actions sans regret et options** | Partie V (`M-20` à `M-23`) : trois paliers, initiatives sans regret ou conditionnelles et bascules. |
| **6–7. Portes, veille et révision** | Partie VI (`M-24` à `M-26`) et `Annexe F` : portes sur preuve, signaux `SIG-nnn` et risques du plan. |

### 1.4.2 Trois scénarios sans probabilité et une variable transversale

Prolongeant le Compendium 2027 (C27, § 43.3) sur `2028-2035` sans pondération probabiliste, trois scénarios encadrent l’architecture (`M-8`) : **A — Socle étendu** (montée des standards ouverts jusqu’à l’identité, aux registres et à l’observabilité), **B — Archipel** (enfermement durable de la gouvernance dans chaque plateforme éditeur) et **C — Blocs** (fragmentation juridictionnelle des règles de confiance et de résidence). La **portée des agents** est traitée non comme un quatrième scénario, mais comme une **variable transversale partiellement non observée** depuis l’arrêt de la série METR le 8 septembre 2026 [1], alors que 68 % des déploiements observés en production s’arrêtent encore à dix étapes ou moins avant contrôle humain [3].

## 1.5 Consolidation sans intrants externes et ordre d’arbitrage

L’exécution du présent ouvrage s’est déroulée sur un dépôt dépourvu des répertoires externes `Claude/`, `../2026/` (`CRE-IA-2026-01`) et `sources-locales/`, seule l’archive Git locale donnant accès en lecture seule au Compendium 2027 et à une édition exploratoire antérieure (`Gemini/`). L’audit de cette dernière ayant établi une rédaction à quotas rigides, deux tiers de faux renvois en `.1` vers le C27 et plusieurs erreurs chronologiques ou juridiques, quatre garde-fous ont été appliqués : (1) dépouillement complet en pistes évaluées dans `Master/fusion/pistes.json` et réécriture intégrale à neuf contrôlée par empreintes de douze mots consécutifs; (2) interdiction de créer tout identifiant fictif du Cadre 2026 absent (`corpus_2026_absent` dans l'`Annexe D`), seuls ses trois plans transversaux attestés (`Plan A`, `Plan B`, `Plan C`) étant mis en correspondance en `M-9` et `Annexe E`; (3) extraction locale vérifiée de soixante-dix-sept textes primaires `L+`; (4) rejet de tout quota d’identifiants par chapitre.

Toute contradiction documentaire est consignée dans `Master/fusion/divergences.md` et tranchée selon quatre rangs successifs : **(a)** le texte primaire lu sur son fichier brut `L+` fait foi — ainsi le règlement (UE) 2026/1744 du 8 juillet 2026 encadrant aussi les administrations publiques reporte l’Annexe III au 2 décembre 2027 D [12], et le bulletin du BSIF sur l’IA agentique est daté sur pièce de juillet 2026 [13]; **(b)** à défaut, l’énoncé sourcé prime sur l’énoncé non sourcé (l’exposé sourcé du C27 prévalant sur ses volets *Mise en œuvre*); **(c)** à parité, la lecture vérifiée la plus récente l’emporte [15] [16]; **(d)** si aucun texte primaire accessible ne tranche, l’ouvrage garde le degré le plus prudent et inscrit la réserve dans les `Limites`.

## 1.6 Architecture éditoriale, identifiants et parcours de lecture

La **capacité cible** sert de pivot unique reliant les six parties (`M-1` à `M-26`) et les huit annexes (`A` à `H`, dont `A`, `B`, `C`, `D` et `F` sont générées mécaniquement à partir des registres JSON). Sept classes d’identifiants à trois chiffres sans quota structurent cette traçabilité :

```
PRI-nnn   Principe d'architecture (M-9)           POR-nnn   Porte de passage sur preuve (M-20..M-24)
CAP-nnn   Capacité cible à 10 champs (M-10)       INI-nnn   Initiative de feuille de route (M-20..M-23)
DEC-nnn   Décision d'architecture 2035 (M-13)     SIG-nnn   Signal externe de révision (M-25)
PEX-nnn   Proposition d'exigence sectorielle (M-14..M-18)
```

| Lecteur | Objectif opérationnel | Parcours prioritaire dans les six parties (`M-1` à `M-26`) |
| --- | --- | --- |
| **Architecte d’entreprise ou sécurité** | Définir le noyau possédé, la carte des capacités et la trajectoire des ADR | `M-1`, `M-2`, `M-4`, `M-5`, Partie III (`M-9` à `M-13`), profils concernés en Partie IV, `M-19` à `M-23`, `Annexe E`. |
| **Risque de modèle et cyberrisque (2e ligne)** | Arrêter les critères d’homologation E-23, les classes de décision et les portes | `M-1` (§ 1.3), `M-2`, `M-3`, `M-5`, `M-6`, `M-12`, Partie IV, `M-24` et `M-26`. |
| **Conformité et affaires juridiques** | Contrôler l’assise fédérale et québécoise, les cloisons de groupe et les réserves | `M-1` (§ 1.3, § 1.5), `M-3`, `M-5`, `M-14` à `M-18`, `Annexe A` et `Annexe D`. |
| **Haute direction TI et portefeuille** | Séquencer les investissements sans regret, les options et la veille | *Sommaire pour décision*, `M-1` (§ 1.2, § 1.4), `M-7`, `M-8`, `M-11`, `M-20` à `M-25`. |

## Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Genre éditorial sur 2028-2035 | Architecture stratégique en capacités prolongée d’un plan directeur de référence informatif | Uniquement lors de la déclinaison budgétaire et applicative interne propre à une institution | [S] |
| Planification sous incertitude à neuf ans | Trois scénarios sans probabilité et parcours adaptatifs pilotés par seuils de bascule et signaux | Lorsqu’un acte législatif ou réglementaire adopté fixe une date opposable certaine | [M] [2] |
| Qualification d’une obligation réglementaire | Exiger un texte primaire officiel extrait et vérifié localement en statut `L+` | Jamais : tout texte fermé (`F`) ou repéré (`R`) est déclaré en `Limites` sans portée normative | [N] [4] |
| Portée des textes visant le secteur public | Mentionner explicitement les administrations publiques dans tout bloc citant une échéance administrative | Si une clause contractuelle d’approvisionnement public lie expressément un fournisseur financier | [N] [18] |
| Emploi des volets *Mise en œuvre* du C27 | Co-citer systématiquement l’exposé sourcé du C27 ou un texte `L+` et généraliser tout produit nommé | Conserver en l’état une ADR seulement lorsqu’elle énonce déjà un invariant fonctionnel neutre | [S] |

## Limites

1. **Synchronisation inter-volumes (**`DIV-02`**) et décloisonnement interne.** Initialement produit sans le dossier `../2026/`, le registre de traçabilité `Master/registre/traceabilite.json` et l'`Annexe D` ont été rétro-synchronisés sur `CRE-IA-2026-01` v1.2 (`0/24 PEX` à `corpus_2026_absent`), et le profil québécois `2026/documents/Note AMF IA.pdf` (`CRE-IA-2026-01-QC`) a été décloisonné dans le corpus `L+`; seuls `Claude/` et `Master/recherche/sources-locales/` demeurent absents du dépôt.
2. **Textes fermés (**`F`**) hors corpus lu et compléments ouverts (**`L+`**).** Demeurent honnêtement au statut `F` sans contournement : les PDF hébergés sur `lautorite.qc.ca` (`T-01`, `T-02`, `T-13`, `T-14`, `T-15`, `HTTP 403`), le référentiel `TOGAF`, le corps réservé aux membres TIES de la recommandation UIT-T F.748.93 [21] et les spécifications sous licence de FDX, d’ACORD et du CSIO. En revanche, la collecte HTTPS ouverte du 19 novembre 2026 (`DC-P10`) a intégré en statut `L+` l’article fondateur en libre accès de Haasnoot et al. (2013, dépôt institutionnel TU Delft) sur les parcours adaptatifs [24] — complétant l’ouvrage de 2019 [2] — ainsi que le cadre *NIST AI RMF 1.0* (`NIST AI 100-1`) [25].
3. **Profil juridictionnel.** L’analyse juridique couvre en profondeur le ressort fédéral canadien et le Québec, sans prétendre à un inventaire exhaustif des droits provinciaux des neuf autres provinces et trois territoires.
4. **Rédaction agentique.** La part produite par des agents, le périmètre non relu humainement et les résultats du tirage de recollation (`seed=20282035`) sont détaillés dans la page liminaire *À propos de cette édition*.

## Sources

1. METR, *Task-Completion Time Horizons of Frontier AI Models (Time Horizon 1.1)*, mise à jour 2026-09-08, lu en entier le 2026-11-16, statut L+, texte : P-34.txt.
2. V. A. W. J. Marchau et al. (dir.) et M. Haasnoot, A. Warren et J. H. Kwakkel, *Decision Making under Deep Uncertainty: From Theory to Practice* (ch. 1 et ch. 4 : *Dynamic Adaptive Policy Pathways*), Springer, 2019, lu en entier le 2026-11-16, statut L+, texte : N-10.txt.
3. M. Pan et al., *Measuring Agents in Production (MAP)* (`arXiv:2512.04123`, 2026), et M. Cemri et al., *Why Do Multi-Agent LLM Systems Fail? (MAST)* (`arXiv:2503.13657v2`, NeurIPS 2025), 2025-2026, lu par passages le 2026-11-16, statut L+, texte : P-38.txt.
4. Bureau du surintendant des institutions financières (BSIF), *Guideline E-23 – Model Risk Management (2027)*, publié le 2025-09-11, lu en entier le 2026-11-16, statut L+, texte : T-05.txt.
5. Organisme canadien de réglementation des investissements (OCRI), *Investment Dealer and Partially Consolidated Rules* (règles 3200, 3400, 3600, 3800), 2026-08-11, lu par passages le 2026-11-16, statut L+, texte : T-23.txt.
6. Parlement du Canada, *Loi sur les banques* (`L.C. 1991, ch. 46`, art. 21, 239, 416, 489, 627.06+), à jour au 2026-10-29, lu par passages le 2026-11-16, statut L+, texte : T-16.txt.
7. Secrétariat du Conseil du Trésor du Canada, *Avis de mise en œuvre de la Politique sur la sécurité : Migration vers la cryptographie post-quantique (AMOPS / SPIN)*, en vigueur le 2025-10-09, lu en entier le 2026-11-16, statut L+, texte : P-23.txt.
8. G7 Cyber Expert Group, *Advancing a Coordinated Roadmap for the Transition to Post-Quantum Cryptography in the Financial Sector*, janvier 2026, lu en entier le 2026-11-16, statut L+, texte : P-24.txt.
9. Parlement du Canada, *Loi sur les services bancaires axés sur les consommateurs* (`L.C. 2026, ch. 3, art. 224`), sanctionnée le 2026-03-26 (à jour au 2026-10-29), lu en entier le 2026-11-16, statut L+, texte : T-19.txt.
10. Parlement du Québec, *Loi visant principalement à améliorer l’encadrement du secteur financier, la protection des dépôts d’argent et le régime de fonctionnement des institutions financières* (`L.Q. 2018, c. 23`, *Loi sur les assureurs* et *LDPSF*), sanctionnée le 2018-06-13, lu par passages le 2026-11-16, statut L+, texte : QC-03.txt.
11. Parlement du Québec, *Loi modernisant des dispositions législatives en matière de protection des renseignements personnels* (`L.Q. 2021, c. 25` — Loi 25, modifiant `RLRQ, c. P-39.1`), sanctionnée le 2021-09-22, lu par passages le 2026-11-16, statut L+, texte : QC-01.txt.
12. Parlement européen et Conseil de l’Union européenne, *Règlement (UE) 2026/1744 du 8 juillet 2026 modifiant le règlement (UE) 2024/1689 (omnibus numérique sur l’IA)*, JOUE du 2026-07-24, lu en entier le 2026-11-16, statut L+, texte : P-02.txt.
13. BSIF, *Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security, and Operational Resilience* (*Technology Risk Bulletin*), juillet 2026 (modifié le 2026-07-13), lu en entier le 2026-11-16, statut L+, texte : T-09.txt.
14. CA/Browser Forum, *Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates* v2.3.1 (Ballot SC-081v3 du 2025-04-11), lu par passages le 2026-11-16, statut L+, texte : P-26.txt.
15. Model Context Protocol, *Specification (Revision 2026-07-28)*, 2026-07-28, lu en entier le 2026-11-16, statut L+, texte : P-10.txt.
16. Projet Model Context Protocol et Linux Foundation AAIF, *MCP Roadmap et Agent Identity WG*, 2026-08-22, lu en entier le 2026-11-16, statut L+, texte : P-11.txt.

17. Innovation, Sciences et Développement économique Canada (ISDE), *L’IA pour tous : Stratégie nationale du Canada en matière d’intelligence artificielle*, juin 2026, lu en entier le 2026-11-16, statut L+, texte : P-31.txt.
18. Secrétariat du Conseil du Trésor du Canada, *Guide sur la portée de la Directive sur la prise de décisions automatisée*, mis à jour le 2026-09-15, lu en entier le 2026-11-16, statut L+, texte : CAN-09.txt.
19. Secrétariat du Conseil du Trésor du Canada, *Guide sur l’utilisation de l’intelligence artificielle agentive* (2026-09-15), et Ministère de la Cybersécurité et du Numérique du Québec, *Guide sur l’utilisation responsable de l’IA agentique* (2026), lu en entier le 2026-11-16, statut L+, texte : P-32.txt.
20. Executive Office of the President — Office of Management and Budget (OMB), *Memorandum M-26-15: Transition to Post-Quantum Cryptography*, 2026-06-24, lu en entier le 2026-11-16, statut L+, texte : P-21.txt.
21. Union internationale des télécommunications (UIT-T), *Fiche publique de la Recommandation F.748.93 : Framework and requirements for AI agent interoperability* (approuvée le 2026-08-29; corps réservé aux membres TIES), lu en entier le 2026-11-16, statut L+, texte : P-20.txt.
22. IETF Datatracker, *RFC 9964 (ML-DSA JOSE/COSE), RFC 10024 (TLS 1.3 Hybrid ML-KEM), RFC 10073 (Composite ML-DSA X.509) et draft-uppalapati-wimse-pq-agent-identity-01*, 2026-10-27 (publications mai à novembre 2026), lu par passages le 2026-11-16, statut L+, texte : P-27.txt.
23. IETF Datatracker, *Workload Identity in Multi System Environments (wimse) Charter & draft-ietf-wimse-aims-01*, mise à jour 2026-11-02, lu en entier le 2026-11-16, statut L+, texte : P-12.txt.
24. M. Haasnoot, J. H. Kwakkel, W. E. Walker et J. ter Maat, *Dynamic adaptive policy pathways: A method for crafting robust decisions for a deeply uncertain world* (*Global Environmental Change*, 2013, copie en libre accès TU Delft Repository), 2013-02-01, lu le 2026-11-19, lu en entier, statut L+, texte : THEO-HAASNOOT-2013.txt.
25. NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0, NIST AI 100-1)*, 2023-01-26, lu le 2026-11-19, lu par passages, statut L+, texte : NIST-AI-RMF.txt.
