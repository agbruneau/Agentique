# Chapitre M-18 — Groupe financier diversifié et synthèse comparative

*Question directrice : Que peut-on partager entre entités, et que faut-il cloisonner?*

> **État de référence (16 novembre 2026) :** Ce chapitre examine le groupe financier diversifié réunissant activités de dépôt, de gestion de patrimoine, d’assurance de personnes et d’assurance de dommages au Canada et au Québec, puis dresse la synthèse comparative des quatre profils de la Partie IV. Toutes les obligations et échéances datées reposent sur les textes primaires lus sur texte brut (`L+`). Les textes de l’AMF bloqués au téléchargement (`T-01`, `T-02`, `T-13` à `T-15`, `T-25`, `N-03`), les codifications de LégisQuébec (`T-04`, `T-28`, `T-29`, `N-02`, `c. C-67.3`) et les référentiels sous barrière ou licence (`T-22`, `T-24`, `N-08`, `R-11`, `T-30`, `T-31`) figurent au statut `F` dans les limites : aucune obligation ni aucune preuve de niveau normatif n’en dépend.

La majorité des actifs financiers au Canada et au Québec relèvent de groupes congloméraux — à société mère bancaire, d’assurance ou coopérative — présents dans trois ou quatre sous-secteurs (chapitres M-14 à M-17) [1] [3] [16] [20]. Ériger un « agent universel de groupe » sur une mémoire client unique constitue un antipatron illégal : le groupe demeure scindé en **personnes morales distinctes** soumises à l’interdiction de transmettre les données bancaires vers l’assurance [1] [2], à l’autonomie des finalités de consentement [14] [28] et aux règles de convenance et d’indépendance en courtage [8] [9] [16].

La règle cardinale (`PRI-010`, `PRI-015`) consiste donc à **mutualiser le plan de contrôle technique sans données clients** — identités non humaines, moteur déterministe de politiques, gabarits d’inventaire, routage sans état et télémétrie cyber — **et à cloisonner cryptographiquement par entité juridique les contextes, mémoires, consentements, livres et agrégats réglementaires** (`CAP-021`, `CAP-032`, `CAP-037`) [2] [14] [22] [30].

## 18.1 Types d’institutions

Trois configurations juridiques de groupes financiers diversifiés opèrent au Canada et au Québec, chacune gouvernée par une loi faîtière qui détermine le superviseur chef de file et le régime des opérations internes.

1. **Groupes à société mère bancaire fédérale.** Articulés autour d’une banque de l’annexe I régie par la *Loi sur les banques* (`L.C. 1991, ch. 46`) — dont les six banques d’importance systémique nationale (*D-SIBs*) [1] [20] —, ils contrôlent une société de fiducie et de prêt fédérale (`L.C. 1991, ch. 45`) [4], un courtier en placement et gestionnaire de portefeuille membre de l’OCRI et inscrit auprès des ACVM [8] [9], un gestionnaire de fonds d’investissement et des filiales d’assurance-vie et d’assurance de dommages [3] [16]. Le
  canal bancaire y est soumis aux restrictions de l’article 416 et du règlement `DORS/92-330` envers l’assurance [1] [2].
2. **Groupes à société de portefeuille d’assurance et groupes actifs à l’échelle internationale (IAIG).** Structurés sous la *Loi sur les sociétés d’assurances* (`L.C. 1991, ch. 47`) — incluant quatre IAIG ayant leur siège au Canada [3] [20] — ou sous charte québécoise [16], ils réunissent assurances de personnes ou de dommages, fonds distincts, gestion d’actifs, courtage en placement et parfois banque ou société de fiducie affiliée [3] [4] [9].
3. **Groupes financiers coopératifs québécois.** Organisés autour d’une fédération de caisses et de coopératives de services financiers réformée par la Partie II de `L.Q. 2018, c. 23` [16], ils intègrent institutions de dépôts, assureurs autorisés du Québec, courtiers en valeurs mobilières et fiducie sous la surveillance consolidée de l’Autorité des marchés financiers (AMF), avec faculté d’adhésion volontaire au cadre fédéral des services bancaires axés sur les consommateurs [5] [6].

## 18.2 Régulateurs et textes applicables

Le groupe diversifié relève d’une **supervision matricielle** croisant surveillance prudentielle consolidée (BSIF ou AMF) et autorités fonctionnelles par métier (ACFC, Banque du Canada, ACVM, OCRI, CCRRA/OCRA, CANAFE, CAI et CPVP). Toute plateforme transversale hérite de la règle la plus stricte applicable aux filiales qui la consomment (`CAP-049`, `C27, § 38.3` [30]). À l’inverse (`EF-06`), la *Directive sur la prise de décisions automatisée* du Conseil du Trésor ne régit que les ministères et organismes des **administrations** fédérales publiques inscrites à la *Loi sur la gestion des finances publiques* et ne lie aucune entité d’un groupe financier privé [29].

| Régime transversal de groupe | Textes primaires lus (`L+`) | Effet direct sur l’architecture du groupe |
| --- | --- | --- |
| **Impartition intra-groupe et apparentés** | BSIF *B-10* (section A3, Principe 8, § 2.3.2.1–2.3.5.1) [22]; *Loi sur les banques* (art. 485.1–489) [1]; *Loi sur les sociétés d’assurances* (art. 517.1–521) [3]; `L.Q. 2018, c. 23` (*Loi sur les assureurs*, art. 45–49) [16] | *B-10* soumet expressément aux **ententes avec des tiers** les services fournis par la société mère, les filiales et les sociétés affiliées [22]; conditions du marché entre apparentés [1] [3]; au Québec, imputation des actes combinés des groupements contrôlés (art. 46) et pouvoir de l’AMF d’inspecter tout affilié technologique non réglementé (art. 48) ou d’interdire l’impartition (art. 49) [16]. |
| **Modèles, cyber, résilience et climat consolidés** | BSIF *E-23* [21], *B-13* [23], *E-21* [24], Bulletin juillet 2026 [25], Regard octobre 2026 [26], *B-15* [20] | Inventaire des modèles au **1er mai 2027** D [21]; **interdiction sous *B-15* (exercice 2028 D) de combiner en un agrégat unique** les émissions financées bancaires, les émissions associées à l’assurance et celles des actifs sous gestion (Annexe 2-2 `b) ii`) [20]; temporisation simultanée des lois bancaire, d’assurances et de fiducie au **30 juin 2033** D [1] [3] [4]. |
| **Muraille banque-assurance et ouverture bancaire** | *Loi sur les banques* (art. 416, 627.08) [1]; `DORS/92-330` (art. 2, 5, 7.1, 8, 9) [2]; *LSAC* et projet de règlement [5] [6] | Interdiction de transmettre les données clients bancaires à un assureur ou courtier affilié (art. 8) et de promouvoir une assurance non autorisée sur page Web ou application bancaire (art. 7.1 et 9) [2]; registre ouvert supervisé par la Banque du Canada et interdiction du grattage d’écran (art. 171) [5] [6]. |
| **Vie privée, santé, génétique et LBC/FAT** | *Loi 25* (art. 3.3, 12–14, 12.1, 17, 18.3) [14]; `L.Q. 2023, c. 5` [15]; *LPRPDE* [28]; *Non-discrimination génétique* et `2020 CSC 17` [12] [13]; *LRPCFAT* (art. 5, 9.6) [27] | Autonomie de chaque filiale au regard des finalités de consentement [14] [28]; prohibition pénale génétique [12] [13]; assujettissement conjoint LBC/FAT des banques, caisses, fiducies, assureurs-vie et courtiers en valeurs mobilières [27]. |

## 18.3 Cas d’usage prioritaires par domaine d’affaires et classe de décision

À l’échelle conglomérale, seuls les cas d’usage préservant l’étanchéité des personnes morales sont admis sous étiquetage d’entité mandante (`CAP-021`, `CAP-036`, `C27, § 22.4` [30]).

| Domaine | Cas d’usage transversaux légitimes au niveau du groupe | Classes | Garde-fou juridique impératif |
| --- | --- | --- | --- |
| `D1` Relation client | Authentification fédérée du client multi-entités et aiguillage de premier niveau cloisonné par canal. | `Classe 1`, `Classe 2` | Blocage déterministe de toute promotion ou redirection vers l’assurance vie/auto/habitation depuis un canal bancaire (`DORS/92-330` art. 7.1 et 9) [2]. |
| `D2` Conseil multi-produits | Planification financière intégrée uniquement sous mandat explicite et consentement granulaire inter-filiales. | `Classe 1` à `Classe 3` | Séparation de la convenance valeurs mobilières (`NI 31-103` art. 13.3, OCRI `3400`) [8] [9], du conseil LDPSF (art. 27) et des 3 soumissions courtiers hors groupe (art. 38) [16]. |
| `D3` Souscription et octroi | Exécution strictement isolée par entité juridique sur un plan d’inférence sans état partagé (`CAP-029`). | `Classe 3`, `Classe 5` | Interdiction de contaminer un score bancaire par un dossier médical d’assurance-vie ou un test génétique prohibé [2] [12] [14]. |
| `D4` Opérations et paiements | Services internes de règlement et de vérification d’accréditation ouverte [5] [6] [7], isolés par locataire statutaire (`CAP-026`). | `Classe 2` à `Classe 4` | Tenue séparée des livres au Canada par loi constitutive (`Banques` art. 239; `Assurances` art. 262; `Fiducie` art. 244) [1] [3] [4]. |
| `D5` Différends et sinistres | Orientation des plaintes vers la filiale débitrice et le recours externe compétent (ombudsman bancaire ou organisme indépendant de conciliation en assurance, voir M-14, M-16 et M-17) sans fusionner les dossiers. | `Classe 1` à `Classe 3` | Interdiction du terme « ombudsman » interne bancaire (art. 627.43(2)) [1] et respect des délais et recours propres à chaque métier [1] [9] [17]. |
| `D6` Conformité, LBC et risque | Risque de concentration des tiers (*B-10* § 2.2.3) [22], inventaire fédéré *E-23* [21] et corrélation LBC/FAT légalement permise [27]. | `Classe 1` à `Classe 3` | Cloisonnement du secret des déclarations d’opérations douteuses (`CAP-021`) [27] et gestion des conflits sur titres liés (`NI 31-103` art. 13.4 et 13.6) [9]. |
| `D7` Trésorerie et climat | Gestion consolidée du capital et divulgations climatiques désagrégées de portée 3 (*B-15*) [20]. | `Classe 1`, `Classe 2` | Présentation séparée obligatoire des émissions financées, assurées et sous gestion (Annexe 2-2 `b) ii`) [20]. |
| `D8` Opérations TI et cyber | Centre de sécurité unifié, émission d’identités non humaines, décontamination et coupe-circuit global ou par filiale (`CAP-035` à `CAP-042`). | `Classe 1` à `Classe 3` | Voûtes forensiques chiffrées sous clés propres à chaque entité juridique (`CAP-032`, `CAP-042`) [14] [22] [23]. |

## 18.4 Stade visé en 2035 par domaine et autonomie maximale par classe

À l’échelle du groupe prévaut la **règle du maillon réglementaire le plus strict** (`CAP-048`, `CAP-049`, `C27, § 43.1` [30]) : tout flux traversant deux filiales hérite du plafond d’autonomie de l’entité la plus contrainte. Les fonctions techniques défensives sans données clients inter-filiales (`D8` cybersécurité, `D6` inventaire technique des modèles et des tiers, `D7` consolidation prudentielle désagrégée) visent le **Stade 3 à 4** en 2035 C : tous ; SIG-101, tandis que tout parcours commercial ou opérationnel transversal (`D1`, `D2`, `D4`) demeure borné au **Stade 2** tant qu’un jeton cryptographique de consentement exprès conforme à la Loi 25 et hors prohibitions du `DORS/92-330` n’est pas validé C : tous ; SIG-108. Toute action de `Classe 6` visant une muraille inter-filiales ou un journal d’audit est bloquée hors modèle (`CAP-037`) [23] [25].

## 18.5 Exigences propres au groupe financier diversifié

Deux exigences propres à la structure conglomérale complètent le cloisonnement (`18.10`) et le consentement (`18.11`) et fondent `PEX-043` et `PEX-044` (statut `corpus_2026_absent`).

### Impartition intra-groupe et auditabilité par filiale

La section A3 de *B-10* qualifie expressément d'**arrangements avec des tiers** les services fournis par la société mère, les filiales et les sociétés affiliées, imposant ententes écrites, isolement logique des données (§ 2.3.2.1), droits d’audit du superviseur (Principe 8) et plans de sortie testés en crise (§ 2.3.5.1) [22], aux conditions du marché exigées entre apparentés (`Banques` art. 489; `Assurances` art. 521) [1] [3]. Au Québec, les articles 45 à 49 de la *Loi sur les assureurs* imputent à l’assureur les actes combinés des groupements contrôlés et habilitent l’AMF à inspecter tout affilié technologique non réglementé ou à interdire l’impartition [16].

> **P : PEX-043** **Encadrement contractuel d’impartition intra-groupe, auditabilité par filiale et plans de sortie du noyau mutualisé.** Toute entité interne de groupe opérant un registre, une passerelle d’outils, un plan d’inférence ou un centre de compétences agentiques pour le compte de filiales réglementées est assujettie envers chacune d’elles à une entente écrite aux conditions du marché, à un droit d’inspection direct des autorités de supervision et à un plan de continuité et de sortie testé par filiale (`CAP-031`, `CAP-047`, `CAP-050`, `CAP-051`; appuis : BSIF *B-10*, section A3, Principe 8 et § 2.3.5.1 [22]; *Loi sur les banques*, art. 489 [1]; *Loi sur les sociétés d’assurances*, art. 521 [3]; `L.Q. 2018, c. 23`, art. 45 à 49 [16]; `C27, § 27.5, § 36.5, § 39.1` [30]; `ADR-003`, `ADR-027`).

### Désagrégation réglementaire des livres, modèles et émissions de portée 3

Chaque loi constitutive exige la tenue séparée des livres au Canada (`Banques` art. 239; `Assurances` art. 262; `Fiducie` art. 244; `NI 31-103` art. 11.6) [1] [3] [4] [9], et l’Annexe 2-2 `b) ii` de *B-15* interdit dès l'**exercice 2028** D de fusionner en un seul agrégat les émissions financées bancaires, les émissions associées à l’assurance et celles des actifs sous gestion [20].

> **P : PEX-044** **Présentation désagrégée par métier réglementé des inventaires de modèles, des livres et des divulgations climatiques.** Les vues sémantiques et registres mutualisés d’un groupe financier conservent la séparation stricte par entité juridique des livres réglementaires localisés au Canada, des cotes de risque de modèles et des divulgations d’émissions de portée 3, en interdisant toute fusion en un agrégat unique des émissions financées bancaires, des émissions associées à l’assurance et des actifs sous gestion (`CAP-015`, `CAP-032`, `CAP-046`, `CAP-047`; appuis : BSIF *B-15*, Annexe 2-2 `b) ii` [20]; BSIF *E-23*, Principe 2.1 [21]; *Loi sur les banques*, art. 239 [1]; *Loi sur les sociétés d’assurances*, art. 262 [3]; *Loi sur les sociétés de fiducie et de prêt*, art. 244 [4]; `NI 31-103`, art. 11.6 [9]; `C27, § 12.2, § 37.1, § 38.3, § 39.1` [30]; `ADR-003`, `ADR-009`, `ADR-024`).

## 18.6 Interopérabilité entre organisations et standards de données

Un groupe diversifié fait coexister messages temps réel ISO 20022 (`head.001`, `pacs.008`, `pacs.002`) et norme technique désignée sous l’article 125 de la *LSAC* en banque [5] [6] [7], flux

quotidiens de frais de fonds (`NI 31-103` art. 14.1.2) en patrimoine [8] [9], dossiers cliniques en assurance de personnes [15] et échanges courtiers/PCAF en assurance de dommages [16] [20]. Plutôt qu’un schéma monolithique unique (`C27, § 12.5` [30]), l’architecture fédère des ontologies versionnées par domaine (`CAP-015`, `CAP-016`) et impose à tout appel inter-filiales de traverser la passerelle (`CAP-022`, `CAP-026`) munie d’un attribut immuable d’entité mandante (`CAP-036`).

## 18.7 Écarts propres au groupe et ajustements de la feuille de route

Trois écarts dominent fin 2027 : des entrepôts historiques rapprochant les clients sans étiquetage fin des restrictions du `DORS/92-330` ou de la Loi 25 [2] [14], l’hétérogénéité des plateformes infonuagiques et progicielles choisies par filiale (`CAP-013`), et l’absence de plans de sortie individualisés par filiale pour les services IA internes [22].

- **Palier 1 (2028-2029) :** Registre fédéré *E-23* partitionné par personne morale (**1er mai 2027** D) (`CAP-047`, `PEX-044`) [21]; mise en coupure du blocage banque-assurance `PEX-041` (`CAP-021`, `CAP-037`) [1] [2], des ententes intra-groupe *B-10* `PEX-043` (`CAP-051`) [22], des interfaces ouvertes à 99,5 % supervisées par la Banque du Canada (`CAP-026`) [5] [6], de l’interdiction des rétrofacturations en patrimoine au **1er octobre 2028** D [10] et des rapports *B-15* désagrégés pour l'**exercice 2028** D [20].
- **Palier 2 (2030-2032) :** Jeton cryptographique de consentement inter-filiales `PEX-042` (`CAP-036`) [14], migration post-quantique coordonnée des autorités de certification du groupe (`CAP-040`) — en priorisant l’assurance de personnes et les archives septennales de patrimoine [8] [9] [23] — et exercices annuels de sortie par filiale (`PEX-043`) C : tous ; SIG-009.
- **Palier 3 (2033-2035) :** Alignement coordonné des trois chartes fédérales sur la révision législative précédant l’échéance commune du **30 juin 2033** D [1] [3] [4], notamment sur le cloisonnement banque-assurance et les apparentés C : tous ; SIG-108.

## 18.8 Effet des scénarios A, B et C

- **Scénario A (Socle étendu) C : A ; SIG-003 .** La convergence des standards d’identité, d’échange de jetons (`CAP-036`) et d’observabilité (`CAP-042`) maximise les économies d’échelle du noyau partagé sans affaiblir aucune cloison statutaire entre filiales (`C27, § 43.3` [30]).
- **Scénario B (Archipel) C : B ; SIG-002 .** Chaque filiale subit l’attraction des assistants natifs de ses progiciels métiers. Le groupe active `CAP-013` : exécution locale près de la gravité des données de chaque filiale, mais médiation obligatoire par le plan de contrôle possédé pour la sécurité, le FinOps (`CAP-045`) et tout flux inter-domaines [22] [25].
- **Scénario C (Blocs) C : C ; SIG-107 .** Les groupes ayant des filiales étrangères (D-SIBs et IAIG) affrontent des exigences contradictoires de localisation et de sécurité nationale (`LSAC` art. 55–64 [5]; Regard sur le risque d’octobre 2026 [26]; Loi 25 art. 17 [14]), imposant la partition régionale des six substrats d’état (`CAP-032`) et un profil souverain à poids ouverts par bloc (`CAP-031`) C : C ; SIG-016.

## 18.9 Partage du noyau possédé

Un groupe financier diversifié peut et doit mutualiser les briques **dépourvues de renseignements personnels clients et de secrets commerciaux métiers** qui composent son plan de contrôle (`PRI-001`, `PRI-015`, `C27, § 23.2, § 27.2` [30]) :

1. **Autorité d’identités non humaines et d’agilité cryptographique (**`CAP-035`**,** `CAP-040`**)**, émettant des attestations éphémères partitionnées par espace de noms d’entité juridique et automatisant le cycle des certificats courts et post-quantiques sous *B-13* (§ 3.2.2 et § 3.2.7) [23] [25].
2. **Moteur déterministe de politiques, décontamination et coupe-circuit (**`CAP-037`**,** `CAP-038`**,** `CAP-039`**)**, raccordés au centre de sécurité du groupe pour prouver formellement les invariants et suspendre instantanément un agent défaillant [23] [24] [25].
3. **Plan d’inférence sans état, bacs à sable et pilotage FinOps (**`CAP-029`**,** `CAP-030`**,** `CAP-043`**,** `CAP-045`**)**, mutualisant la puissance de calcul et les harnais d’essais tout en isolant cryptographiquement les caches par filiale (`CAP-032`) [21] [22].
4. **Outillage logiciel du registre *E-23* et d’ingénierie sécurisée (**`CAP-047`**,** `CAP-050`**,** `CAP-052`**)**, chaque filiale conservant son pouvoir propre d’homologation et son plan de sortie (`PEX-043`) [16] [22].

## 18.10 Cloisonnement des données entre entités

Trois murailles légales interdisent toute base vectorielle, mémoire épisodique ou session d’orchestration fusionnant les données clients des entités du groupe (`CAP-017`, `CAP-021`, `C27, § 13.6, § 14.3` [30]).

1. **Muraille banque-assurance (**`Loi sur les banques` **art. 416 et** `DORS/92-330`**).** L’article 8 interdit à une banque de transmettre directement ou indirectement des renseignements sur ses clients au Canada à une société, un agent ou un courtier d’assurances, même affilié (hors engagements stricts de non-promotion approuvés par le surintendant), tandis que les articles 7.1 et 9 interdisent sur toute page Web ou application bancaire de promouvoir une assurance non autorisée (vie individuelle, automobile, habitation) ou d’aiguiller le client vers l’assureur [1] [2].
2. **Muraille des finalités par personne morale et des prohibitions sectorielles.** Sous la Loi 25 (art. 12–13) [14] et la *LPRPDE* [28], toute transmission entre deux filiales constitue une communication à un tiers, doublée de la purge pénale génétique en assurance (`PEX-021`) [12] [13] [15] et du secret des déclarations LBC/FAT [27].
3. **Muraille des conflits d’intérêts et d’indépendance en patrimoine et courtage.** La filiale en valeurs mobilières doit éviter ou résoudre au mieux des intérêts du client tout conflit sur émetteurs liés (`NI 31-103` art. 13.4 et 13.6; OCRI `3402`) [8] [9], et le cabinet de courtage IARD affilié demeure tenu d’offrir au moins trois soumissions hors groupe au Québec (art. 38 LDPSF) [16].

> **P : PEX-041** **Cloisonnement technique inter-entités et blocage du partage banque-assurance dans le socle de groupe.** Au sein d’un groupe financier diversifié mutualisant son infrastructure d’orchestration, chaque agent, index documentaire et appel d’outil porte un identifiant immuable d’entité juridique mandante et bloque par défaut toute lecture ou transmission de renseignements bancaires vers une société, un agent ou un courtier d’assurance

> ainsi que toute promotion d’assurance non autorisée sur canal bancaire (`CAP-001`, `CAP-017`, `CAP-021`, `CAP-037`; appuis : *Loi sur les banques*, art. 416 [1]; `DORS/92-330`, art. 7.1, 8 et 9 [2]; BSIF *B-10*, § 2.3.2.1 [22]; `L.Q. 2021, c. 25`, art. 12–13 [14]; `C27, § 13.6, § 14.3, § 32.1, § 38.3` [30]; `ADR-008`, `ADR-020`).

## 18.11 Consentement

Une clause générique de « partage au sein du groupe » noyée dans les conditions d’ouverture de compte est sans valeur pour autoriser une délégation d’agent. L’article 14 de la Loi 25 impose un consentement manifeste, libre, éclairé, demandé à **chacune des fins spécifiques** en termes simples et clairs et présenté **distinctement**, qui doit être **exprès** dès qu’un renseignement financier ou médical est sensible (art. 12–13), tandis que le mandat technique de l’article 18.3 exclut tout réemploi commercial par la filiale exécutante [14]. De même, l’article 627.08 de la *Loi sur les banques* exige un consentement exprès distinct par produit [1], et la *LSAC* impose un registre quinquennal de consentement exprès révocable [5] [6] sans lever les interdictions du `DORS/92-330` [2].

> **P : PEX-042** **Jeton vérifiable de consentement exprès granulaire avant toute délégation inter-filiales.** Aucune délégation d’agent franchissant la frontière de deux personnes morales distinctes d’un même groupe financier ne transporte de renseignements personnels à des fins commerciales ou de tarification sans un jeton cryptographique lié à un enregistrement valide de consentement manifeste, libre, éclairé, spécifique et présenté distinctement, exprès dès que le renseignement est sensible (`CAP-021`, `CAP-026`, `CAP-036`, `CAP-049`; appuis : `L.Q. 2021, c. 25`, art. 12 à 14 et 18.3 [14]; *LPRPDE*, Annexe 1 principe 4.3 [28]; *Loi sur les banques*, art. 627.08 [1]; *LSAC* et projet de règlement [5] [6]; `C27, § 29.5, § 30.2, § 38.3` [30]; `ADR-018`, `ADR-024`).

## 18.12 Synthèse comparative des sous-secteurs

La confrontation des quatre profils démontre pourquoi l’anti-objectif `A4` proscrit d’assimiler le secteur financier à une banque uniforme. La figure et le tableau croisé ci-dessous résument les convergences du socle et les divergences des plafonds par domaine (`D1` à `D8`) et classe (`Classe 1` à `Classe 6`).

> **[Figure]**
> - Stades visés en 2035 par sous-secteur et par domaine d’affaires (D1 à D8) Échelle C27 (§ 43.1, proposition non validée empiriquement) : le sommet n’est pas une cible universelle (DC-10)
> - Domaine (§ 6.5) Banque
> - (M-14)
> - Patrimoine
> - (M-15)
> - Assur. pers.
> - (M-16)
> - Assur. domm.
> - (M-17)
> - Groupe inter-fil.
> - (M-18)
> - D1 · Relation client
> - Accueil et distribution
> - Stade 3
> - Zéro promo assur.
> - Stade 3
> - Barrière OEO 3240
> - Stade 3
> - Récap. écrit art. 67
> - Stade 3–4
> - Courtage art. 38
> - Stade 2
> - Sauf jeton consent.
> - D2 · Conseil et vente
> - Convenance réglementée
> - Stade 2–3
> - Convenance 627.06
> - Stade 2–3 max
> - Pers. inscrite OCRI
> - Stade 2–3 max
> - Représentant LDPSF
> - Stade 2–3
> - Art. 27 & auto 71
> - Stade 2 max
> - Mur DORS/92-330
> - D3 · Souscription
> - Tarification & octroi
> - Stade 3
> - Crédit Cl. 5 / Cl. 4
> - Stade 3
> - Diligence KYP Cl. 2
> - Stade 2–3
> - Purge génétique
> - Stade 3 / 2–3
> - Part. / Entr. B-9
> - Isolé / filiale
> - Zéro score croisé
> - D4 · Contrats & opér.
> - Tenue et paiements
> - Stade 3
> - Lect. 4 / RTR 2–3
> - Stade 3
> - Interdit OEO 3241
> - Stade 3–4
> - Coll.; rachat Cl. 4
> - Stade 3–4
> - Avenants Cl. 2
> - Stade 2
> - Livres séparés CAN
> - D5 · Sinistres & plaintes
> - Indemnisation & recours
> - Stade 3
> - Délai légal 56 j
> - Stade 2–3
> - Dossiers 7 ans
> - Bimodal 3–4 / 2
> - Refus = humain
> - Bimodal 3–4 / 2
> - FNOL / expert cert.
> - Stade 2
> - Orientation seule
> - D6 · Conformité & LBC
> - Risques et surveillance
> - Stade 3–4
> - E-23 & secret LBC
> - Stade 3–4
> - Surveillance 3600
> - Stade 3
> - E-23 & LBC vie
> - Stade 3–4
> - Fraude & tiers B-10
> - Stade 3–4
> - Inventaire fédéré
> - D7 · Trésorerie & climat
> - Capital, ALM, réassur.
> - Stade 3–4
> - Scope 3 financé
> - Stade 3
> - Fin chargebacks
> - Stade 3
> - ALM long & B-15
> - Stade 3–4
> - Réassur. PML500
> - Stade 3
> - Désagrégé B-15
> - D8 · Opérations TI
> - Cyberrésilience & SOC
> - Stade 3–4
> - API ouverte 99,5 %
> - Stade 3–4
> - Archivage 7 ans
> - Stade 3
> - PQC voûtes 30–60 a
> - Stade 3–4
> - Élasticité E-21
> - Stade 3–4
> - Noyau NHI & SOC
> - Plafond légal / Stade 2 Stade 2–3 ou 3 gouverné Régime bimodal selon l’acte Stade 3–4 (fonctions maîtrisées)

*Fig. 5. – Stades visés en 2035 par sous-secteur et par domaine d’affaires*

| Dimension / Domaine | Banque (`M-14`) | Gestion de patrimoine (`M-15`) | Assurance de personnes (`M-16`) | Assurance de dommages (`M-17`) |
| --- | --- | --- | --- | --- |
| **Superviseurs clés** | BSIF, ACFC, **Banque du Canada** (*LSAC* & PSP), CANAFE; AMF (coopératives QC) [1] [5] [16] [27]. | ACVM (AMF, BCSC), OCRI, CANAFE; orientations *Avis 11-348* [8] [9] [11] [27]. | BSIF, AMF, CCRRA/OCRA, CANAFE (vie), CAI/CPVP et conciliation (voir M-16) [3] [14] [16] [17] [27]. | BSIF, AMF, CCRRA/OCRA, CAI/CPVP et conciliation (voir M-17) [3] [14] [16] [17] [19]. |
| **Verrou cardinal** | Virement RTR irrévocable `pacs.008` [7], **interdiction grattage d’écran** (art. 171 *LSAC*) [5], mur assurance (`DORS/92-330`) [2]. | **Non-délégabilité** (`OCRI 1103(2)`), convenance (`3402`), explicabilité (*Avis 11-348*) et compte OEO (`3241`) [8] [9] [11]. | **Prohibition criminelle génétique** (`2020 CSC 17`) [12] [13], consentement santé (`L.Q. 2023, c. 5`) [15] et patrimoine distinct des fonds (art. 76 et 237) [16]. | **Pointes catastrophiques** (*B-9*, *E-21*) [19] [24], 3 soumissions courtiers hors groupe (art. 38) et polices auto AMF (art. 71) [16]. |
| `D1` Relation client | **Stade 3** — Alertes obligatoires (art. 627.13), zéro promotion assurance non autorisée [1] [2] C : tous ; SIG-103. | **Stade 3** — Accueil KYC (`3202`), barrière anti-recommandation en OEO (`3240`) [8] C : tous ; SIG-105. | **Stade 3** — Orientation collective, récapitulatif écrit Internet (art. 67) [16] C : tous ; SIG-102. | **Stade 3–4** — Connectivité courtiers multi-assureurs (art. 38 LDPSF) [16] C : A, B ; SIG-110. |
| `D2` Conseil et vente | **Stade 2–3** — Convenance bancaire (art. 627.06) et consentement exprès (art. 627.08) [1] C : tous ; SIG-106. | **Stade 2–3 plafonné** — Personne physique inscrite responsable; pré-approbation recherche (`3602(3)`) [8] [9] C : tous ; SIG-105. | **Stade 2–3 plafonné** — Devoir légal du représentant certifié (art. 27 LDPSF) [16] C : tous ; SIG-102. | **Stade 2–3** — Conseil certifié (art. 27 LDPSF) et clauses auto immuables approuvées (art. 71) [16] C : tous ; SIG-102. |
| `D3` Souscription / KYP | **Stade 3** — Crédit simple en `Classe 5` (art. 12.1 Loi 25, *E-23*); complexe en `Classe 3`/`Classe 4` [14] [21] C : tous ; SIG-106. | **Stade 3** — Diligence continue KYP (`3301`) en `Classe 1`–`Classe 2`, approbation produit par le courtier [8] C : tous ; SIG-105. | **Stade 2–3** — Acceptation simple sous purge génétique (`PEX-021`); refus vie/invalidité en `Classe 4` humaine [12] [18] C : tous ; SIG-106. | **Stade 3** (particuliers) / **2–3** (entreprises) — Cumuls *B-9*/*B-15* et veille d’inassurabilité (§ 6.6 AICA) [18] [19] [20] C : tous ; SIG-109. |
| `D4` Contrats / opérations | **Stade 3** (lecture : **4**; RTR irrévocable : **2–3** avec point de contrôle en `Classe 4`) [5] [7] [25] C : tous ; SIG-104. | **Stade 3** en compte géré (**4** sur flux IFM); **interdiction d’ordres automatisés clients en OEO** (`3241(1) (ii)(a)`) [8] C : tous ; SIG-105. | **Stade 3–4** en collectif; `Classe 4` humaine sur bénéficiaires et rachats définitifs [16] C : A, B ; SIG-110. | **Stade 3–4** — Avenants réversibles (`Classe 2`) synchronisés avec les courtiers C : A, B ; SIG-110. |
| `D5` Plaintes / sinistres | **Stade 3** — Remboursement automatisable; délai 56 j; interdit d'« ombudsman » interne (art. 627.43) [1] C : tous ; SIG-106. | **Stade 2–3** — Instruction assistée et conservation sur 7 ans (`NI 31-103` art. 13.15–13.16) [9] C : tous ; SIG-105. | **Stade 3–4** (soins courants) / **Stade 2 strict** sur tout refus ou arrêt d’invalidité/vie (`PEX-023`) [14] [17] [18] C : tous ; SIG-106. | **Bimodal : Stade 3–4** (FNOL en pointe et bris simples) / **Stade 2 strict** avec examen par spécialiste humain ou expert en sinistre habilité sur tout refus (`PEX-031`) [14] [17] [18] C : tous ; SIG-106. |
| `D6`–`D8` Risques et TI | **Stade 3–4** — Disponibilité ouverte **99,5 %** [6], portée 3 financée **2028** D [20], plaintes **7 ans** / consentement **5 ans** [1] [6] C : tous ; SIG-103. | **Stade 3–4** — Conservation **7 ans** (`11.6`, Règle 3800) [8] [9], fin des *chargebacks* **1er oct. 2028** D [10], AUM `TBD` [20] C : tous ; SIG-105. | **Stade 3** — Priorité post-quantique sur voûtes médicales (`PEX-025`), portée 3 investissement **2028** D [20] [23] C : tous ; SIG-009. | **Stade 3–4** — Portée 3 assurée commercial/auto **2028** D [20], validation *B-9* `PML500` [19] et élasticité *E-21* [24] C : tous ; SIG-109. |

**SYNTHÈSE EXÉCUTIVE — Verdict global de la Partie IV sur la thèse de travail de l’ouvrage**

L’épreuve croisée des quatre sous-secteurs et du groupe diversifié sur trente-quatre textes primaires fédéraux, québécois et internationaux lus (`L+`) dans la Partie IV (dont vingt-neuf dans ce chapitre) **confirme la thèse de travail posée au chapitre M-1, tout en l’enrichissant d’une précision juridique essentielle**.

1. **Validation intégrale du noyau de la thèse :** Sur l’horizon 2027-2035, **100 % des échéances réglementaires datées portent sur la preuve, la gouvernance, la transparence ou l’interdiction d’abus** — entrée en vigueur d'*E-23* au 1er mai 2027 D [21], interdiction des rétrofacturations au 1er octobre 2028 D en patrimoine [10], divulgation désagrégée de portée 3 à l’exercice 2028 D sous *B-15* [20], disponibilité à 99,5 % et registre quinquennal ouvert [6], et temporisation des lois financières fédérales au 30 juin 2033 D [1] [3] [4]. Aucune règle adoptée n’impose de confier une décision à un agent autonome : le **plan de contrôle possédé** (`CAP-035` à `CAP-052`) demeure l’unique cible invariante commune.
2. **Nuance révélée par l’épreuve sectorielle :** Si aucun texte ne date une obligation *d’autonomisation*, le droit positif impose en revanche des **plafonds et prohibitions statutaires fermes contre certaines formes d’autonomie** — interdiction des ordres automatisés clients en compte OEO (`OCRI 3241(1)(ii)(a)`) et non-délégabilité de la convenance (`1103(2)`) [8]; interdiction du grattage d’écran bancaire (`LSAC` art. 171) [5]; prohibition criminelle des tests génétiques (`L.C. 2017, ch. 3`) [12] [13]; approbation préalable des polices automobiles (art. 71) et recours obligatoire à des représentants certifiés hors offre directe ou distributeur (art. 59 *Loi sur les assureurs*; art. 27 et 38 *LDPSF*, la codification consolidée `RLRQ, c. D-9.2` demeurant au statut `F`) [16]; droit de révision humaine sous l’article 12.1 de la Loi 25 [14]. L’autonomie est donc doublement conditionnelle : bornée en amont par le droit positif de chaque sous-secteur, et méritée en aval par la preuve opérationnelle (`CAP-048`).

## Grille de décision

| Décision d’architecture | Option par défaut retenue | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| **Périmètre de mutualisation technique au sein d’un groupe diversifié** | Mutualiser uniquement le plan de contrôle sans données clients (NHI `CAP-035`, PDP `CAP-037`, registre logiciel `CAP-047`, routage sans état `CAP-029`, cyber `CAP-038`–`039`), encadré par ententes *B-10* par filiale (`PEX-043`) [16] [22]. | Séparer physiquement l’infrastructure lorsqu’une filiale étrangère subit des restrictions de sécurité nationale ou de résidence incompatibles en scénario C (`CAP-032`, `SIG-002`) [5] [26]. | `[N]` |
| **Circulation de données clients ou d’indices entre banque et filiale d’assurance** | Bloquer par défaut dans l’orchestrateur et les index (`CAP-021`, `CAP-037`, `PEX-041`) toute transmission de données clients bancaires vers l’assurance et toute promotion non autorisée sur canal bancaire [1] [2]. | Uniquement pour les huit assurances expressément permises par `DORS/92-330` (crédit, hypothèque, voyage) ou sous engagement approuvé en vertu de l’article 8(2) [2]. | `[N]` |
| **Délégation d’agent entre deux filiales distinctes transportant des renseignements personnels** | Exiger à la passerelle inter-entités (`CAP-022`, `CAP-036`) un jeton cryptographique lié à un consentement manifeste, spécifique, distinct et exprès pour toute donnée sensible (`PEX-042`), hors prohibition `DORS/92-330` [1] [2] [14]. | Mandat purement technique (art. 18.3 Loi 25) par contrat écrit interdisant à la filiale exécutante tout réemploi ou conservation pour ses propres fins [14]. | `[N]` |
| **Registre des modèles (*E-23*) et divulgations climatiques (*B-15*) de groupe** | Utiliser un schéma commun (`CAP-015`, `CAP-047`) mais partitionner par personne morale les livres statutaires et présenter séparément les émissions financées, assurées et sous gestion (`PEX-044`) [1] [3] [9] [20] [21]. | Aucune fusion en un agrégat unique n’est permise par l’Annexe 2-2 `b) ii` de *B-15* [20]. | `[N]` |

## Limites

Conformément aux règles `EF-12`, `CA-17` et `CA-19`, la synthèse de groupe regroupe les réserves documentaires des chapitres M-14 à M-17 (`statut F`), sans qu’aucune obligation ni preuve de niveau normatif n’en dépende :

1. **Textes québécois bloqués (**`statut F`**) [31] [32] et compléments ouverts décloisonnés (**`L+`**) [34] [35].** Les cinq lignes directrices transversales de l’AMF (`T-01`, `T-02`, `T-13`, `T-14`, `T-15`), la copie française AMF du *Règlement 31-103* (`T-25`) et l’avis télématique de 2015 (`N-03`) [31], de même que les codifications sur LégisQuébec (`T-04`, `T-28`, `T-29`, `N-02`, `RLRQ, c. C-67.3`) [32], demeurent honnêtement classés `F` (`HTTP 403` sans contournement); l’analyse québécoise est complétée en `L+` par les lois sanctionnées [14] [15] [16], les publications des ACVM et du CCRRA/OCRA [8] [9] [10] [11] [17], le profil québécois décloisonné `CRE-IA-2026-01-QC` (`2026/documents/Note AMF IA.pdf`, 41 attentes et 12 `EXIG-AMF`, quatre lois habilitantes québécoises, `ANC-112` et `ANC-113`) [34] et la page officielle de la CAI sur la Loi 25 (`ANC-115`) [35] (`SIG-102`, `SIG-106`).
2. **Normes et rapports sous licence ou barrière (**`statut F`**) [33] et synchronisation** `DIV-02`**.** La spécification FDX v6.0 (`T-22`), la note KYC (`T-24`) et le rapport 2026 (`N-08`) de l’OCRI, le rapport *FR/02/2026* de l’OICV (`R-11`) ainsi que les schémas ACORD (`T-30`) et CSIO (`T-31`) demeurent non lus [33]; la traçabilité des propositions `PEX-041` à `PEX-044` envers `CRE-IA-2026-01` v1.2 est synchronisée dans l’Annexe D.
3. **Jalons ouverts (**`EF-15`**).** Restent non tranchés à la date de référence : la désignation de l’organisme de normalisation technique unique sous l’article 125 de la *LSAC* [5] [6] (`SIG-103`), l’échéance `TBD` des émissions liées aux actifs sous gestion dans *B-15* [20]
  (`SIG-109`) et l’issue de la révision fédérale précédant le **30 juin 2033** sur le cloisonnement banque-assurance [1] [2] [3] [4] (`SIG-108`).

## Sources

1. Parlement du Canada, *Loi sur les banques* (`L.C. 1991, ch. 46`), 2026-10-29 (dernière modification 2026-10-16), lu le 2026-11-16, lu par passages, statut L+, texte : T-16.txt.
2. Gouverneur en conseil, *Règlement sur le commerce de l’assurance (banques et sociétés de portefeuille bancaires)* (`DORS/92-330`), 2026-10-29, lu le 2026-11-16, lu en entier, statut L+, texte : T-17.txt.
3. Parlement du Canada, *Loi sur les sociétés d’assurances* (`L.C. 1991, ch. 47`), 2026-10-29, lu le 2026-11-16, lu par passages, statut L+, texte : CAN-01.txt.
4. Parlement du Canada, *Loi sur les sociétés de fiducie et de prêt* (`L.C. 1991, ch. 45`), 2026-10-29, lu le 2026-11-16, lu par passages, statut L+, texte : CAN-04.txt.
5. Parlement du Canada, *Loi sur les services bancaires axés sur les consommateurs* (`L.C. 2026, ch. 3, art. 224`), sanctionnée le 2026-03-26 (à jour au 2026-10-29), lu le 2026-11-16, lu en entier, statut L+, texte : T-19.txt.
6. Ministère des Finances du Canada, *Projet de Règlement sur les services bancaires axés sur les consommateurs*, 2026-06-27, lu le 2026-11-16, lu en entier, statut L+, texte : T-20.txt.
7. Paiements Canada, *Real-Time Rail ISO 20022 message specification companion document* (v1.4), 2025-05-30, lu le 2026-11-16, lu en entier, statut L+, texte : T-21.txt.
8. OCRI (CIRO), *Investment Dealer and Partially Consolidated Rules*, 2026-08-11, lu le 2026-11-16, lu par passages, statut L+, texte : T-23.txt.
9. ACVM (BCSC), *National Instrument 31-103 Registration Requirements, Exemptions and Ongoing Registrant Obligations* (consolidation au 2026-01-01, publ. 2026-01-30), lu le 2026-11-16, lu par passages, statut L+, texte : CAN-05.txt.
10. ACVM (FCAA), *CSA Notice of Amendments to NI 31-103 – Prohibition on the Use of Chargebacks* (publ. 2026-10-08, en vigueur le 2028-10-01), lu le 2026-11-16, lu en entier, statut L+, texte : CAN-08.txt.
11. ACVM (BCSC), *CSA Staff Notice and Consultation 11-348*, 2024-12-05, lu le 2026-11-16, lu en entier, statut L+, texte : T-26.txt.
12. Parlement du Canada, *Loi sur la non-discrimination génétique* (`L.C. 2017, ch. 3`), sanctionnée le 2017-05-04 (à jour au 2026-10-29), lu le 2026-11-16, lu en entier, statut L+, texte : N-01.txt.
13. Cour suprême du Canada, *Renvoi relatif à la Loi sur la non-discrimination génétique* (`2020 CSC 17`), 2020-07-10, lu le 2026-11-16, lu par passages, statut L+, texte : CAN-03.txt.
14. Parlement du Québec, *Loi modernisant des dispositions législatives en matière de protection des renseignements personnels* (`L.Q. 2021, c. 25`), 2021-09-22, lu le 2026-11-16, lu par passages, statut L+, texte : QC-01.txt.
15. Parlement du Québec, *Loi sur les renseignements de santé et de services sociaux* (`L.Q. 2023, c. 5`), 2023-04-04, lu le 2026-11-16, lu par passages, statut L+, texte : QC-02.txt.
16. Parlement du Québec, *Loi visant principalement à améliorer l’encadrement du secteur financier* (`L.Q. 2018, c. 23`), 2018-06-13, lu le 2026-11-16, lu par passages, statut L+, texte : QC-03.txt.
17. CCRRA et OCRA, *Directive — Conduite des activités d’assurance et traitement équitable des clients*, sans date de publication interne (réf. PBA 19, mis à jour en novembre 2017), lu le 2026-11-16, lu en entier, statut L+, texte : T-27.txt.
18. AICA (IAIS), *Application Paper on the supervision of artificial intelligence*, 2025-07-02, lu le 2026-11-16, lu en entier, statut L+, texte : CAN-02.txt.

19. BSIF, *Guideline B-9 – Earthquake Exposure Sound Practices*, 2013-02-28 (modifié le 2013-07-31), lu le 2026-11-16, lu en entier, statut L+, texte : N-04.txt.
20. BSIF, *Guideline B-15 – Climate Risk Management*, 2025-03-07 (mis à jour le 2026-01-08), lu le 2026-11-16, lu en entier, statut L+, texte : N-05.txt.
21. BSIF, *Guideline E-23 – Model Risk Management (2027)*, 2025-09-11, lu le 2026-11-16, lu en entier, statut L+, texte : T-05.txt.
22. BSIF, *Guideline B-10 – Third-Party Risk Management Guideline*, 2023-04-30, lu le 2026-11-16, lu en entier, statut L+, texte : T-06.txt.
23. BSIF, *Guideline B-13 – Technology and Cyber Risk Management*, 2022-07-31, lu le 2026-11-16, lu en entier, statut L+, texte : T-07.txt.
24. BSIF, *Guideline E-21 – Operational Risk Management and Resilience*, 2024-08-22, lu le 2026-11-16, lu en entier, statut L+, texte : T-08.txt.
25. BSIF, *Generative and Agentic Artificial Intelligence: Implications for Technology, Cyber Security, and Operational Resilience*, 2026-07-13, lu le 2026-11-16, lu en entier, statut L+, texte : T-09.txt.
26. BSIF, *Annual Risk Outlook – Semi-annual update – Fiscal Year 2026-2027*, 2026-10-08, lu le 2026-11-16, lu en entier, statut L+, texte : CAN-07.txt.
27. Parlement du Canada, *Loi sur le recyclage des produits de la criminalité et le financement des activités terroristes* (`L.C. 2000, ch. 17`), 2026-10-29, lu le 2026-11-16, lu par passages, statut L+, texte : T-10.txt.
28. Parlement du Canada, *Loi sur la protection des renseignements personnels et les documents électroniques* (`L.C. 2000, ch. 5`), 2026-10-29, lu le 2026-11-16, lu par passages, statut L+, texte : T-11.txt.
29. Secrétariat du Conseil du Trésor du Canada, *Guide sur la portée de la Directive sur la prise de décisions automatisée*, 2026-09-15, lu le 2026-11-16, lu en entier, statut L+, texte : CAN-09.txt.
30. Compendium 2027, *Interopérabilité et orchestration en entreprise agentique* (ch. 12 à 14, 22, 23, 27, 29, 30, 32, 36, 38, 39, 43, 50), consulté le 2026-11-16, lu par passages, statut C.
31. AMF, *Lignes directrices et textes non lus (*`T-01`*,* `T-02`*,* `T-13` *à* `T-15`*,* `T-25`*,* `N-03`*)*, repéré le 2026-11-16, non lu, statut F.
32. LégisQuébec, *Codifications* `T-04`*,* `T-28`*,* `T-29`*,* `N-02` *et* `RLRQ, c. C-67.3`, repéré le 2026-11-16, non lu, statut F.
33. FDX, OCRI, OICV, ACORD et CSIO, *Spécifications et rapports sous barrière ou licence (*`T-22`*,* `T-24`*,* `N-08`*,* `R-11`*,* `T-30`*,* `T-31`*)*, repéré le 2026-11-16, non lu, statut F.
34. Corpus Agentique (`2026/documents/Note AMF IA.pdf`), *Profil d’application québécois* `CRE-IA-2026-01-QC` *— 41 attentes AMF et 12* `EXIG-AMF`, 2026-11-11, lu le 2026-11-19, lu en entier, statut L+, texte : QC-AMF-NOTE-2026.txt.
35. CAI Québec, *Principaux changements aux lois sur la protection des renseignements personnels (Loi 25)*, 2026-01-01, lu le 2026-11-19, lu en entier, statut L+, texte : QC-CAI-LOI25.txt.
