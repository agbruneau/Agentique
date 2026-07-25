# Relecture CA-01 à CA-14 — contrôle de sortie du jalon J-6

| Champ | Valeur |
|---|---|
| Objet | Relecture de la **grille des quatorze critères d'acceptation** du [PRD](../prd/PRD.md) **§11**, exigée par le critère de sortie du jalon **J-6** (PRD §12) : *« grille CA intégralement conforme **et constatée sur pièce** »* |
| Activité | Phase **P5**, à la suite de **P5.1** (revalidation temporelle) et de **P5.2** (rejeu des motifs de balayage) |
| Périmètre | Les **34 pièces** de [`monographie/`](../monographie/) — avant-propos, ch. 1 à 28, annexes A à E — plus les documents de `verification/` que les critères désignent nommément. Le registre de gel est lu comme document de contrôle, non comme pièce |
| Date d'exécution | **22 juillet 2026** |
| Domaine de mesure | Le **corps** de chaque pièce, découpé par la commande de [PRDPlan](../prd/PRDPlan.md) **§1.5** (`awk` du premier séparateur jusqu'à `## Notes`), hors en-tête et hors bloc `## Notes`, sauf mention contraire explicite. Toute mesure est prise **sur le domaine entier**, jamais sur un échantillon |
| Formulation exacte des critères | Relevée par **ouverture du PRD §11**, lignes 744 à 757, et non reformulée de mémoire |
| ⚠ Ce que ce rapport n'est pas | **Il ne délivre aucun certificat de conformité, ni pour l'ouvrage, ni pour aucune pièce, ni pour lui-même.** Il consigne, critère par critère, ce qui a été mesuré, où, et ce qui n'a pas pu l'être. **Un critère porté ci-dessous comme CONSTATÉ l'est au grain et sur le domaine déclarés à sa ligne**, pas au-delà |
| ⚠ Ce rapport ne clôt pas J-6 | Le jalon exige **trois termes** : un rapport de revalidation daté de moins de trente jours, la grille CA constatée sur pièce, et le **PDF régénéré et versionné avec sa source**. Le présent rapport est **le second des trois**. Le premier est déposé ([`revalidation-2026-07-22.md`](revalidation-2026-07-22.md)) ; **le troisième n'existe pas** — le volume n'a aucun pipeline de rendu (PRDPlan §7, P5.4) |

---

## 1. L'instrument, et ce qu'il vaut

**Trois familles de constatation ont été employées, et elles ne se valent pas.** Les distinguer est la condition pour que ce rapport soit rejouable plutôt que cru.

| Famille | Ce qu'elle établit | Ce qu'elle n'établit pas |
|---|---|---|
| **Relevé outillé** — expression régulière passée sur le domaine entier, cardinal recompté | Qu'une forme est présente ou absente, et combien de fois | Que ce que la forme désigne est correct. *Le balayage est un filet, pas un verdict* (PRD §A.6) |
| **Ouverture sur pièce** — occurrence lue en contexte | Ce que la phrase dit, à son siège | Rien au-delà de l'occurrence ouverte |
| **Confrontation à la source** — ouverture du document cité | Que la citation correspond à son original | Rien sur les citations non rouvertes |

**Deux propriétés ont été contrôlées avant tout relevé, et mesurées ici plutôt que reprises d'une passe amont**, parce qu'un motif qui les ignore rend zéro sans erreur apparente.

- **Appariement typographique** : les 34 corps portent **10 921 apostrophes droites (U+0027)** et **zéro apostrophe typographique (U+2019)**. Les motifs R-01, R-02, R-08 et R-14 portent une apostrophe droite ; ils portent donc bien sur ce texte. *Sur une prose à apostrophe courbe, les quatre rendraient zéro sans erreur apparente.*
- **Locale** : le balayage a été conduit sous `LC_ALL=C.UTF-8`. Contre-épreuve exécutée sur un échantillon d'essai portant « conformément à E-23 la ligne directrice AMF » : la branche `conform\w+.*(AMF|ligne directrice)` de R-07 rend **1** sous `LC_ALL=C.UTF-8` et **0** sous `LC_ALL=C` — sans la locale, le motif manque sa cible principale.

**Volumétrie re-mesurée à l'ouverture de la passe**, par la seule commande de PRDPlan §1.5, sur les 34 pièces et en une passe unique : **160 450 mots** pour **102 500** de cible. ⚠ **Cette valeur diffère de celle que publient les porteurs** (160 447) ; l'écart est de **trois mots**, il est arithmétiquement imputable, et son traitement est au §7.

---

## 2. Verdicts — les quatorze critères

**Trois verdicts sont employés, et un seul d'entre eux affirme quelque chose.** *CONSTATÉ* : le terme du critère a été relevé ou ouvert, au grain déclaré. *NON TENU* : le terme du critère n'est pas satisfait, et le constat est donné. *NON CONSTATABLE* : le terme n'est pas une propriété que cette passe puisse relever, et la raison est écrite.

| Critère | Verdict | Lieu du constat, et grain |
|---|---|---|
| **CA-01** Traçabilité | **CONSTATÉ** au volet relevable ; **NON CONSTATABLE** au volet « centralité » | §3.1 — 98 entrées `F-xx` et 33 `H-xx` distinctes mobilisées, aucun identifiant hors plage ; 209 mobilisations d'entrées **[C]**, 11 premières mobilisations sans marqueur de proximité, **ouvertes une à une** |
| **CA-02** Zéro proscrit | **CONSTATÉ** au volet outillé ; **NON CONSTATABLE** au volet « inspection humaine » | §4 — 15 motifs passés sur les 34 corps ; 4 motifs à faible cardinal ouverts **en totalité** ici (R-02, R-07, R-08, R-10) ; les 34 pièces portent un bilan de rejeu daté du 22 juillet 2026 |
| **CA-03** Attribution | **CONSTATÉ** | §3.3 — **8 pourcentages** au corps des 34 pièces, tous ouverts, tous attribués à leur source |
| **CA-04** Datation | **CONSTATÉ** | §3.4 — champ « Date de gel » lu dans les **34 en-têtes** : 34 valeurs, une seule date ; registre à 34 lignes ; [`revalidation-2026-07-22.md`](revalidation-2026-07-22.md) datée du jour |
| **CA-05** Fidélité des citations | **CONSTATÉ** sur deux revendications rouvertes à la source ; **NON CONSTATABLE** sur les vingt-deux autres | §3.5 — verbatim de non-compositionnalité confronté à `Monographie.md` §3.10.1, mot pour mot ; **4 revendications** reposent sur un fichier retiré du dépôt |
| **CA-06** Honnêteté des lacunes | **CONSTATÉ** | §3.6 — les **22** lacunes présentes, chacune **à la section que le TOC lui assigne** ; récapitulatif de 22 lignes au ch. 28 §28.5 |
| **CA-07** Marquage des inférences | **CONSTATÉ** sur les trois pièces à marquage d'ouverture ; **NON CONSTATABLE** sur l'exhaustivité | §3.7 — **162 occurrences** sur **34 pièces sur 34** ; ch. 8, ch. 26 et §27.4 ouverts et vérifiés à leur ouverture |
| **CA-08** Bilinguisme terminologique | **CONSTATÉ** sur la forme ; **NON CONSTATABLE** sur « à la première occurrence » | §3.8 — **218** termes anglais en italique entre parenthèses |
| **CA-09** Périmètre | **CONSTATÉ au périmètre que le critère prescrit** ; le **grain n'est pas tranché** | §3.9 — Parties VII et VIII : **5 pièces, 20 sections**, recomptées sur les fichiers ; grain ouvert sous **R-G-46**, réservé à l'auteur |
| **CA-10** Qualification des renvois | Branches (a) et (b) **CONSTATÉES** ; branche (c) **NON TENUE au grain de l'occurrence** | §3.10 — Vol. I : **133** renvois nommant leur fichier, **0** renvoi de section non qualifié, **1 ambiguïté de rédaction signalée** au ch. 12 ; questions du Vol. II : **33** mobilisations, **31** nommant leur chapitre ; garde-fous : **245 sur 382** nommant leur volume |
| **CA-11** Statut épistémique double | **CONSTATÉ** sur le relevé ; **NON CONSTATABLE** sur « tout énoncé prospectif » | §3.11 — **1 373** marques : 157 de tri prospectif, 1 216 de niveau ; **34 pièces sur 34** en portent |
| **CA-12** Traitement défensif | **NON TENU** sur son terme procédural ; volet substantiel **CONSTATÉ** | §5 — **aucun compte rendu déposé sous `verification/`** pour les cinq passes du 22 juillet 2026 ; **16 pièces sur 34** ne nomment aucun compte rendu CA-12 ; les **6 retraits** annoncés sont vérifiés appliqués |
| **CA-13** Traçabilité du blueprint | **CONSTATÉ** | §3.13 — [`relecture-CA-13-P4.md`](relecture-CA-13-P4.md) déposé ; 3 cas « ni tracé ni marqué », 3 corrigés, aucune trace fausse |
| **CA-14** Relecture adversariale | **CONSTATÉ** sur le statut ; **NON CONSTATABLE** sur la distinction rédacteur / relecteur | §3.14 — statut lu dans les **34 en-têtes** ; la distinction est **déclarée, non constatable sur les fichiers** — réserve 1 de **R-G-19**, non levée, que l'annexe A §A.8 porte elle-même |

**Décompte des verdicts, recompté ligne à ligne sur la table ci-dessus** : **douze** critères ne portent aucun verdict NON TENU — CA-01 à CA-09, CA-11, CA-13, CA-14 ; **deux** en portent un — **CA-10** sur sa troisième branche et **CA-12** sur son terme procédural. **Sept** critères portent en outre un volet **NON CONSTATABLE** : CA-01, CA-02, CA-05, CA-07, CA-08, CA-11, CA-14. **Un** critère porte une question de grain **non tranchée et réservée à l'auteur** : CA-09.

⚠ **Un verdict NON CONSTATABLE n'est pas un verdict favorable.** Il dit que la passe n'a pas l'instrument, non que le terme est tenu. *Compter les NON CONSTATABLE parmi les critères satisfaits reproduirait exactement le geste que CA-14 proscrit.*

---

## 3. Détail par critère

### 3.1 CA-01 — Traçabilité

**Énoncé (PRD §11)** : *« 100 % des affirmations factuelles centrales adossées à une entrée du socle (H-xx héritée ou F-xx propre) ou à une source primaire nouvelle de qualité équivalente. […] Une affirmation tracée vers une entrée [C] n'est pas centrale, ou n'est pas rédigée. »*

**Ce qui a été relevé sur le domaine entier.** Les 34 corps portent **1 939 occurrences** d'identifiants `F-xx` et **450** de `H-xx`. Les identifiants **distincts** sont **98** pour le socle propre et **33** pour le socle hérité — soit **l'intégralité** des deux socles déclarés au PRD §7.2, §7.3 et §7.8 à §7.11. **Aucun identifiant hors plage** n'est cité : zéro `F-` au-delà de 98, zéro `H-` au-delà de 33. *Aucune entrée n'est orpheline, et aucune n'est fantôme.*

**Le piège propre à ce critère a été traité au grain où il siège.** Les entrées **[C]** sont **dix-huit** — F-36 et H-17 à H-33, relevées par ouverture du PRD. Elles sont mobilisées **209 fois** dans les 34 corps, formant **109 couples (pièce, entrée)**. La convention du volume porte le niveau **à la première mobilisation dans la pièce** (convention R-G-21, déclarée notamment au ch. 8) : à ce grain, **98 premières mobilisations sur 109** portent le marqueur `[C]` dans une fenêtre de ±45 caractères.

**Les onze restantes ont été ouvertes une par une**, et aucune ne trace un fait central vers une entrée [C] :

- **sept** mobilisent **H-33**, qui n'est pas un fait mais **l'instrument du tri prospectif** — l'entrée est citée comme référence de méthode (« au sens du tri du Vol. I ») et non comme énoncé factuel ;
- **deux** siègent à l'annexe B et à l'annexe C, et elles **énoncent le critère lui-même** : « Trois entrées en [C] n'occupent aucune ligne de plein droit (CA-01) », « CA-01 refuse le fait central sur entrée [C] » ;
- **une** (ch. 18, H-17) déclare l'entrée **périmée** sur le point cité, par F-63 ;
- **une** (ch. 27, H-30) est un renvoi de terminologie au glossaire, non un énoncé.

⚠ **Ce qui n'est pas constatable, et il faut le dire au lieu de le contourner.** La **centralité** d'une affirmation n'est pas une propriété relevable : elle se juge. Cette passe établit qu'aucune des 209 mobilisations d'entrée [C] examinées ne porte visiblement un fait central ; elle **n'établit pas** que 100 % des affirmations factuelles centrales du volume soient adossées au socle, ce qui exigerait de lire les **148 en-têtes de niveau 2** que portent les 34 corps — cardinal recompté — et d'y trancher, un par un, ce qui est central. **Le volet outillé de CA-01 est constaté ; son volet de jugement ne l'est pas.**

⚠ **Deux entrées portent une dette de vote, et elles fondent un chapitre.** **F-92** et **F-96** n'ont pas subi le vote adversarial que PRD §A.4 réserve aux affirmations portant à elles seules la thèse d'un chapitre ; la parade est un marqueur ⚖ à chaque mobilisation au ch. 26. La dette est ouverte sous **R-G-44** et **n'est pas résorbée par la présente passe**.

### 3.2 CA-02 — Zéro proscrit

Traité au **§4**, qui porte le rejeu des motifs.

### 3.3 CA-03 — Attribution

**Énoncé** : *« Toutes les métriques auto-déclarées, projections et études commandées attribuées conformément à §8.2, à chaque occurrence, sans exception d'usage illustratif. »*

**Le corps des 34 pièces ne porte que huit pourcentages**, cardinal recompté sur le domaine entier. Les huit ont été **ouverts un par un** :

| Objet | Attribution constatée |
|---|---|
| Taux d'empoisonnement de mémoire — « ≥ 80 % » pour « < 0,1 % » (F-23), **deux occurrences** | « mesurés et **déclarés par** les auteurs », « dont les auteurs **déclarent** » — attribution portée à chaque occurrence |
| Brèches d'entreprise imputables aux identités machines — « environ 25 % » (H-21, **[C]**), **deux occurrences** | « **Gartner projetait, en 2024** », « **Gartner projetait, en millésime 2024** » — source et millésime portés à chaque occurrence |
| Écart de volumétrie du tronc — « +38,1 % », **quatre occurrences** | Mesure du volume lui-même, adossée à la commande de PRDPlan §1.5 |

**Le motif étendu de CA-03 relève 316 occurrences** sur les 34 corps, ventilées : `déclare` 184, `attache` 62, `selon` 42, `consigne` 16, pourcentage 8, `précise` 4. Ce sont des **verbes d'attribution**, non des métriques : leur présence est le signe que l'attribution est faite, non un point de faute.

⚠ **Borne du relevé** : le motif ne voit ni un effectif brut non attribué, ni un ordre de grandeur écrit en toutes lettres. Cette passe constate l'attribution des **valeurs chiffrées en pourcentage**, sur leur domaine entier ; elle ne balaie pas les grandeurs exprimées autrement.

### 3.4 CA-04 — Datation

**Énoncé** : *« Chaque pièce porte sa date de gel, consignée au registre. Les faits chauds (§8.3) sont revalidés avant publication, et le rapport de revalidation est daté de moins de trente jours au moment de publier. »*

**Trois termes, trois constats.**

1. **Date de gel en pièce** — le champ a été lu dans les **34 en-têtes**, un par un : **34 valeurs, aucune absente**, toutes au **21 juillet 2026**.
2. **Consignation au registre** — [`99-registre-gel.md`](../monographie/99-registre-gel.md) porte **34 lignes** renseignées en statut, date de gel, cible et volumétrie réelle. ⚠ **Trois de ses valeurs de volumétrie sont périmées** au regard du disque (voir §7) ; la date de gel et le statut, eux, concordent.
3. **Revalidation** — [`revalidation-2026-07-22.md`](revalidation-2026-07-22.md) porte les **sept lignes de PRD §8.3**, reprises à la source primaire, et est datée du **22 juillet 2026**. Elle déclare elle-même couvrir une publication **jusqu'au 21 août 2026**. ⚠ Le fichier est **présent dans l'arbre de travail et non encore versionné** au moment de cette passe.

⚠ **Un écart d'un jour subsiste entre le gel déclaré et les derniers correctifs**, pour les treize pièces dont les coupes ou les corrections datent du 22 juillet 2026. Il est **consigné plutôt que lissé** — aucune date n'a été réécrite —, et son arbitrage est ordonnancé en P5.1. La présente passe **ne le tranche pas** : la date de gel d'une pièce est un fait de gouvernance, et son déplacement modifierait 34 en-têtes et 34 lignes de registre.

### 3.5 CA-05 — Fidélité des citations

**Énoncé** : *« Toute citation présentée comme verbatim l'est. Une reprise dans la substance se déclare comme telle ; la revendication de verbatim est réservée aux reprises littérales, vérifiées contre le texte actuel de la source. »*

**Le corpus porte 24 revendications de verbatim** au corps de ses pièces, réparties sur 16 pièces, et **6 déclarations explicites de reprise dans la substance** (« rendu français », « reprise dans la substance », « non verbatim »).

**Le piège nommé par le cadrage a été rouvert à la source.** La formule de non-compositionnalité de la sûreté vit à quatre endroits du Vol. I sous trois formes ; **CA-05 impose de ne revendiquer le verbatim que sur un seul siège**. Constat :

- le ch. 12 et le ch. 22 déclarent expressément : « **Le verbatim n'est revendiqué que sur `Monographie.md` §3.10.1** », et nomment les trois autres sièges comme formes courte et condensée ;
- **la confrontation à la source a été faite** : `1 - InteroperabiliteAgentique/Monographie.md`, ligne 1868, section **§3.10.1** — présente au dépôt courant — porte **mot pour mot** « un agent sûr et un outil sûr, une fois composés, ne donnent pas un système sûr. La sûreté n'est pas une propriété compositionnelle », et, dans le même paragraphe, « la frontière de confiance n'est plus le périmètre d'un système mais *chaque arête* du graphe d'interaction ». **Les deux clauses citées le sont exactement.**

⚠ **Quatre revendications de verbatim reposent sur un fichier absent du dépôt.** Le commit `fd8f1be` a supprimé `Synthese Monographie.md` du Vol. I comme du Vol. II ; **quatre** revendications vivantes s'y adossent — l'invariant à quatre termes de **H-27** (`Synthese Monographie.md` §10.3, trois occurrences) et le front ouvert des deux sauts de **H-28** (§11.5, une occurrence).

**Contrôle conduit contre l'historique, et sa borne est déclarée.** Le contenu du fichier au commit `fd8f1be~1` a été ouvert : les deux verbatim y figurent **exactement**, et les huit sections citées par le volume (§4.2, §5.10, §6.12, §10.2, §10.3, §11.3, §11.5, §11.6) **existent toutes**. *Un renvoi exact vers un fichier absent demeure exact ; il cesse d'être opposable.* **CA-05 exige une vérification « contre le texte actuel de la source »** : pour ces quatre revendications, le texte actuel de la source n'est pas au dépôt, et la vérification s'est faite contre un blob git — **ce n'est pas une équivalence**. Le point est ouvert sous **R-G-52** et **n'est pas tranché ici** : il porte sur la charge éditoriale d'un autre volume.

⚠ **Les vingt autres revendications de verbatim n'ont pas été rouvertes à leur source par cette passe.**

### 3.6 CA-06 — Honnêteté des lacunes

**Énoncé** : *« Les vingt-deux lacunes de §10 apparaissent toutes, en encadré ou en question de recherche. Aucune silencieusement omise. Le gabarit employé correspond à l'état réel de l'instruction. »*

**Les vingt-deux ont été cherchées une par une, à la section que le TOC leur assigne**, et les vingt-deux y sont :

- **dix-sept** sont citées **par leur numéro** dans leur pièce porteuse, et le contrôle a vérifié la **section** : lacune 1 → ch. 5 §5.4 ; 2 → ch. 12 §12.4 ; 3 → ch. 21 §21.1 ; 4 → ch. 19 §19.1 ; 5 → ch. 7 §7.4 ; 6 → ch. 10 §10.3 ; 7 → ch. 26 §26.3 ; 8 → ch. 7 §7.2 **et** ch. 22 §22.1 ; 9 → ch. 25 §25.5 ; 10 → ch. 9 §9.1 ; 11 → avant-propos ; 12 → annexe A §A.9 ; 13 → ch. 16 §16.1 ; 14 → ch. 2 §2.2 ; 15 → ch. 26 §26.1 ; 21 → ch. 24 §24.4 ; 22 → ch. 27 §27.2. **Les dix-sept sièges correspondent à l'assignation du TOC.**
- **cinq** — les lacunes **16 à 20** — ne sont pas citées par leur numéro, et **elles sont présentes en substance à leur section assignée** : RGPD au ch. 20 (avertissement de portée, degré 3 déclaré) ; ISO/IEC SC 42 et CEN-CENELEC au ch. 21 §21.3, énoncés à la formule imposée du degré 3 ; OpenID Connect au ch. 2 §2.4, même formule ; cadre d'architecture européen au ch. 3 §3.2, « délibérément non converti en affirmation ».

**Le récapitulatif du ch. 28 §28.5 porte vingt-deux lignes numérotées de 1 à 22**, cardinal recompté sur la table. L'avant-propos annonce le même cardinal et **déclare le compter sur la liste**.

⚠ **Ce qui n'est pas constaté ici** : que le **gabarit** employé par chaque encadré corresponde à l'état réel de l'instruction. Ce contrôle exige de rouvrir, pour chacune des vingt-deux, le rapport de lot qui la porte — il n'a pas été conduit.

### 3.7 CA-07 — Marquage des inférences

**Énoncé** : *« Toute construction d'auteur porte le libellé "Lecture de l'auteur", suivi de ce que le socle établit et de ce qu'il n'établit pas. Les ch. 8, 26 et le §27.4 le portent à l'ouverture, étant des constructions d'auteur en totalité. »*

**162 occurrences** du libellé sur le domaine entier, réparties sur **34 pièces sur 34** — aucune pièce n'en est dépourvue. La clause négative « n'établit pas » ressort **160 fois**, et **33 pièces sur 34** en portent au moins une.

**Les trois marquages d'ouverture ont été ouverts et vérifiés :**

| Pièce | Position du marquage | Forme constatée |
|---|---|---|
| **ch. 8** | premier bloc cité de la pièce, en tête | « la pièce entière est une construction d'auteur, et le marquage se porte ici plutôt qu'au paragraphe » ; « Ce que le socle établit » et « Ce qu'il n'établit pas » présents, suivis de la formule du degré 3 |
| **ch. 26** | **première ligne du corps** | « marquage porté à l'ouverture de la pièce, et il régit le chapitre entier » ; les deux volets présents |
| **§27.4** | ligne suivant immédiatement le titre de section | « marquage porté à l'ouverture de la section, qui est une construction d'auteur en totalité » ; les deux volets présents |

⚠ **Un écart de forme est signalé, non corrigé.** L'**annexe C** porte une occurrence unique du libellé, et elle est la **seule des 34 pièces** à ne pas l'accompagner de la clause « n'établit pas » : la borne y est portée sous la forme « l'entrée, [A], **établissant seulement que**… ». La borne est écrite ; la forme prescrite ne l'est pas. *Le contrôle relève l'écart de forme et s'abstient de le juger sur le fond* — modifier une pièce excède le mandat de cette passe.

⚠ **Ce qui n'est pas constatable** : que **toute** construction d'auteur porte le marquage. Le relevé montre où le marquage est ; il ne montre pas où il manque. Établir l'exhaustivité exigerait de trancher, section par section, ce qui relève de l'inférence — c'est précisément le contrôle que **CA-13** a conduit sur la seule Partie IX, et qui y a trouvé **trois cas** « ni tracé ni marqué ».

### 3.8 CA-08 — Bilinguisme terminologique

**218 occurrences** de la forme prescrite — terme anglais entre parenthèses et en italique — sur le domaine entier. La forme est employée dans tout le corpus.

⚠ **Le terme « à la première occurrence » n'est pas constatable par relevé** : il exigerait, pour chaque terme technique du volume, d'établir où se situe sa première apparition et d'y vérifier la glose. Cette passe constate que **la convention est appliquée** ; elle n'établit pas qu'elle l'est **à chaque première occurrence**.

### 3.9 CA-09 — Périmètre

**Énoncé** : *« Le test d'appartenance (§5.1) est vérifié section par section en Parties VII et VIII. »*

**Le périmètre que le critère prescrit est couvert en totalité.** Les Parties VII et VIII comptent **cinq pièces** — ch. 22, 23, 24, 25, 26 — et **vingt sections de niveau 2**, cardinal **recompté sur les fichiers** (4 + 4 + 4 + 5 + 3 = 20). Le rapport [`relecture-CA-09-P4.md`](relecture-CA-09-P4.md), ouvert et lu, porte exactement ce périmètre : **20 sections examinées, 20 passent**, deux développements coupés au grain du §5.1 — 499 mots retirés, 271 écrits à leur place.

⚠ **Le grain du critère n'est pas tranché, et la présente passe ne le tranche pas.** CA-09 prescrit « section par section » ; le §5.1 qu'il met en œuvre énonce le test au grain du « développement ». Les deux coupes opérées vivaient dans des sections qui **passent** : *au grain prescrit, aucune n'aurait été trouvée.* **Modifier l'énoncé d'un critère d'acceptation relève de l'auteur sans exception** (PRDPlan §5.3) ; le point est ouvert sous **R-G-46**.

⚠ **La couverture des huit autres pièces de P4 par un test d'appartenance n'est pas exigée par CA-09**, dont l'énoncé se borne aux Parties VII et VIII. Le constat de la clôture de P4 — « 8 pièces sur 13 sans test d'appartenance » — vise une **ambition** de contrôle plus large que le critère, non un manquement au critère. *Les deux ne se confondent pas, et confondre l'un avec l'autre produirait un verdict faux dans les deux sens.*

### 3.10 CA-10 — Qualification des renvois

**Énoncé** : *« Tout renvoi au Vol. I nomme son fichier ; tout renvoi à une question du Vol. II nomme son chapitre ; tout renvoi à un garde-fou nomme son volume. »* **Trois branches, trois mesures distinctes.**

**(a) Renvoi au Vol. I — CONSTATÉ.** Les 34 corps portent **133 citations nommant un fichier du Vol. I** : `Monographie.md` 92, `Synthese Monographie.md` 37, `Chapitres/Annexe B - Architecture de Solutions.md` 4. **129 d'entre elles sont immédiatement suivies d'un renvoi de section** ; les quatre autres sont des mentions de fichier sans section. Le contrôle négatif — recherche d'un renvoi de section attribué au Vol. I **sans** nom de fichier dans son voisinage — **ne rend aucune occurrence**.

⚠ **Une ambiguïté de rédaction est signalée, et elle n'est pas un renvoi faux.** Le ch. 12 écrit : « la formule reste adossée au **Vol. I, au ch. 22 §22.3** ». Le §22.3 visé est celui du **présent volume** — « Ce que l'arête change : la non-compositionnalité de la sûreté », vérifié sur le fichier —, et **le Vol. I ne porte aucun §22.3**, vérifié sur `Monographie.md`. La juxtaposition rend la phrase lisible comme un renvoi au Vol. I. **Signalé, non corrigé** : la correction d'un renvoi relève de l'instance d'exécution, et elle se fera dans la pièce, non dans ce rapport.

**(b) Renvoi à une question du Vol. II — CONSTATÉ.** **33 mobilisations** des étiquettes Q1 à Q6 dans les 34 corps. **31 nomment leur chapitre** dans une fenêtre de 140 caractères — « Vol. II, ch. 21 §21.2 » pour l'essentiel, « du même chapitre » pour un renvoi anaphorique. **Les deux restantes sont des reprises internes à une énumération dont la tête porte la qualification** ; elles ont été ouvertes. Trois pièces au moins déclarent en outre l'homonymie explicitement : « le ch. 16 §16.3 du même volume porte un jeu **Q1 à Q5 entièrement distinct** ».

**(c) Renvoi à un garde-fou — NON TENU au grain de l'occurrence.** Les 34 corps portent **382 mobilisations** de garde-fous à deux chiffres (R-01 à R-14) et **15** à un chiffre (R-1 à R-8). **Les 15 mobilisations du Vol. II nomment toutes leur volume**, sans exception. Sur les 382 du présent volume, **245 nomment leur volume** dans une fenêtre de ±120 caractères ; **137 ne le nomment pas**. Ventilation par pièce :

| Situation | Pièces | Occurrences non qualifiées |
|---|---|---|
| **Qualification à 100 %** | **11 pièces** — ch. 1, 3, 6, 11, 14, 15, 16, 17, 18, 23, 26 | 0 |
| **Qualification partielle** | **23 pièces** | **137**, dont ch. 27 (19 sur 29), ch. 28 (18 sur 35), ch. 22 (13 sur 15), avant-propos (12 sur 14), annexe B (11 sur 12), annexe C (10 sur 16) |

**Cinq pièces posent la convention une fois pour toutes** — « les garde-fous cités ici portent la numérotation à deux chiffres du Vol. III, à ne pas confondre avec les R-1 à R-8 du Vol. II » : avant-propos, ch. 4, ch. 22, annexe B, annexe D.

⚠ **Le grain de cette branche n'est pas tranché, et il ne l'est pas ici.** CA-10 écrit « **tout** renvoi » ; au grain littéral de l'occurrence, la branche n'est pas tenue sur **23 pièces**. Au grain de la pièce — une déclaration de convention couvrant les occurrences de la pièce —, cinq pièces seulement la posent, et la branche n'est pas tenue davantage. **Trancher entre ces deux lectures modifie l'énoncé d'un critère d'acceptation : cela relève de l'auteur sans exception** (PRDPlan §5.3). Les deux options sont posées au §8.

**(d) Une quatrième branche existe hors de l'énoncé du critère.** Le `CLAUDE.md` du volume impose que tout renvoi à une section d'annexe nomme son **document** — le PRD et l'ouvrage portant des annexes homonymes aux objets différents. **Elle n'est pas au texte de CA-10**, et elle est mesurée ici à titre supplémentaire : **112 renvois** de la forme `§A.x`, `§B.x`, `§C.x` au corps des 34 pièces, dont **77 nomment leur document dans une fenêtre de 60 caractères**. Les **35** restants ont été ventilés puis ouverts : **32 sont des renvois d'une annexe à ses propres sections** — annexe A 5, annexe B 9, annexe C 18 —, **non ambigus par position** ; les **3 renvois inter-pièces** — avant-propos, ch. 17, ch. 19 — nomment tous leur document dans leur phrase, hors de la fenêtre de mesure : « l'annexe A §A.9 », « l'**Annexe B du PRD** […] en son §B.1 », « **PRD, Annexe C §C.2**, règle 1 ». **Aucun renvoi inter-pièces ne laisse l'homonymie ouverte.**

**Contrôle complémentaire, hors énoncé du critère** : les **86 cibles relatives distinctes** en `.md` que portent les 34 pièces ont été résolues sur le disque — **86 résolvent, 0 cassée**.

### 3.11 CA-11 — Statut épistémique double

**1 373 marques** relevées sur le domaine entier : **157 de tri prospectif** — PROGRAMMÉ 73, PROJETÉ 47, SPÉCULATIF 37 — et **1 216 de niveau** — [A] 356, [B] 603, [C] 257. **Les 34 pièces sur 34 portent des marques de niveau** ; aucune n'en est dépourvue.

⚠ **Deux limites du relevé, et elles ont été établies par les passes de balayage plutôt que supposées.** Le motif CA-11 est **aveugle au degré** — les mobilisations bornées par un degré d'absence lui échappent — et il ne voit pas un tri exprimé sans son mot-clé. Le relevé établit donc que **les deux instruments sont employés et distingués** ; il n'établit pas que **tout** énoncé prospectif porte son tri, ce qui exigerait d'identifier les énoncés prospectifs, opération de jugement et non de relevé.

### 3.12 CA-12 — Traitement défensif

Traité au **§5**.

### 3.13 CA-13 — Traçabilité du blueprint

**Énoncé** : *« Chaque composant, contrat et correspondance réglementaire de la Partie IX est tracé vers une entrée du socle ou marqué inférence d'auteur (Annexe B). »*

Le rapport [`relecture-CA-13-P4.md`](relecture-CA-13-P4.md) a été **ouvert et lu**. Il porte le périmètre exact du critère — les deux pièces de la Partie IX —, déclare avoir ouvert la **spécification PRD Annexe B §B.1 à §B.5 intégralement**, et rend : **trois cas « ni l'un ni l'autre », trois corrigés** ; **aucune trace fausse** — toutes les entrées citées portent ce que les pièces leur font porter.

Le ch. 27 porte **quatorze** occurrences du marquage « Lecture de l'auteur » et le ch. 28 **onze**, relevées sur leurs corps par la présente passe.

⚠ **Le rapport déclare lui-même ce qu'il n'a pas rejoué** : ni le contrôle de bornage, ni les motifs de §A.6, ni la relecture de conformité, ni CA-12. *Un contrôle de traçabilité n'atteste que la traçabilité.*

### 3.14 CA-14 — Relecture adversariale

**Énoncé** : *« Chaque pièce passe une relecture par un relecteur distinct de son rédacteur, chargée de réfuter et non de valider. Une attestation de conformité n'est jamais rédigée depuis le souvenir de l'avoir vérifiée : elle est portée par la constatation sur pièce. »*

**Le champ « Statut » a été lu dans les 34 en-têtes, un par un.** Les **34** portent « **Rédigé et relu adversarialement** », et **aucun gabarit ne subsiste**. **Vingt-six en-têtes** mentionnent en outre le rendement de leur relecture — réfutations reçues, fondées, appliquées —, et **vingt-trois** écrivent en toutes lettres « relecteur distinct ». *Ces deux cardinaux mesurent ce que les en-têtes déclarent, non ce qui a eu lieu.*

⚠ **La distinction rédacteur / relecteur n'est pas constatable sur disque, et ce rapport ne la présume pas.** Les fichiers ne portent aucune signature ; l'organisation des passes la déclare, rien ne l'établit. C'est la **réserve 1 de R-G-19**, **non levée**, et l'**annexe A §A.8** l'écrit elle-même : *« La distinction rédacteur / relecteur y est **déclarée, non constatable** sur les fichiers. »* Ce constat est repris ici depuis la pièce, après ouverture — non depuis le registre qui le déclare.

---

## 4. Le rejeu des motifs de balayage sur les trente-quatre pièces — CA-02

**Ce que le PRD §A.6 déclare de lui-même, et qui commande tout ce qui suit** : *« Les bilans §A.6 publiés dans les vingt et une pièces rédigées ont été mesurés à l'instrument défectueux. Leur rejeu est dû […] Jusque-là, aucun de ces bilans ne vaut attestation. »* Quatre motifs avaient été corrigés le 21 juillet 2026 sous R-G-40 — R-13 ancré, R-11 élargi, R-14 balayé avec `-i`, CA-03 étendu.

### 4.1 Que la correction des motifs était nécessaire, mesuré sur le corpus entier

**Le coût de l'instrument défectueux a été mesuré, et non repris d'une déclaration.** Chaque motif corrigé a été passé sur les 34 corps sous sa **forme antérieure** puis sous sa **forme corrigée** :

| Motif | Forme antérieure | Forme corrigée | Écart, et ce qu'il vaut |
|---|---|---|---|
| **R-14** | 1 137 | **1 313** | **+176 occurrences** que la sensibilité à la casse rendait invisibles. R-14 est le motif le plus sollicité du volume ; le sous-compte portait sur les négatifs **en tête de phrase**, c'est-à-dire sur les énoncés les plus chargés |
| **R-13** | 175 | **32** | **−143 faux positifs**, tous des identifiants de lot ou d'affirmation (`L01` à `L14`) qu'aucune échelle d'autonomie ne concerne. Le motif ancré rend L0 11, L3 9, L1 2, L2 1, `copilote` 9 |
| **CA-03** | 234 | **316** | **+82 attributions** formulées avec `précise`, `attache` ou `consigne` |
| **R-11** | 142 | **145** | **+3 occurrences** de la forme verbatim « NIST Internal Report (IR) 8547 », que CA-05 impose de citer telle quelle et que la branche abrégée ne voyait pas |

*Un instrument qui sous-compte de 176 occurrences le motif le plus sollicité d'un volume ne mesure pas ce volume.* **Le rejeu était dû ; il l'était sur le corpus entier, et non sur les vingt et une pièces du tronc.**

### 4.2 Relevé des quinze motifs sur les trente-quatre corps

Cardinal des motifs **recompté sur le bloc du PRD §A.6** : **quinze lignes** — R-01 à R-11, R-13, R-14, CA-03, CA-11. **R-12 n'a pas de motif**, et son absence est déclarée au PRD : il se contrôle par CA-12 seul.

| Motif | Occurrences, 34 corps | Ventilation ou constat |
|---|---|---|
| **R-01** | 43 | forme au singulier uniquement. ⚠ La forme plurielle « passeports d'agents » rend **0** : l'angle mort du motif, signalé par une passe antérieure, est **latent et non actif** |
| **R-02** | **5** | `garanti` 4, `prouve l'identité` 1 — **les cinq ouvertes** : quatre sont des mentions métalinguistiques du verbe proscrit ou une citation verbatim du Vol. I, la cinquième est « garantie de vérité » en énoncé négatif. **Aucun emploi affirmatif** |
| **R-03** | 55 | les trois termes de marché à leur siège de définition |
| **R-04** | 81 | branches `plan de contrôle`, `control plane`, `\bACP\b`, `AgentMesh` |
| **R-05** | 32 | `\bKYA\b` et `Know Your Agent` |
| **R-06** | 59 | dominée par `exigenc\w*` |
| **R-07** | **19** | branche `conforme à E-23` : **0**. Branche `B-13` : **12**, **toutes ouvertes** — formule du degré 3 ou clause renforcée. Branche `conformité.*E-23` : **9 captures pour trois formes distinctes**, toutes ouvertes, toutes de la forme « ne revendique aucune conformité **et aucune source ne documente le lien** avec E-23 ». **Aucune revendication affirmative de conformité.** ⚠ **Le piège de préfixe est armé et ne mord pas** : `B-13` n'est pas ancrée et capterait `B-131`, `B-134` — **0 occurrence** de `B-13` suivi d'un chiffre au corpus |
| **R-08** | **3** | **les trois ouvertes** : les trois sont des **refus** de l'affirmation d'absence générale, dont une écartée au vote adversarial. Aucune faute |
| **R-09** | 23 | `Community Group`, `\bCG\b`, `W3C.*normalis` |
| **R-10** | **12** | **les douze ouvertes** : les six noms d'auteurs du corpus d'appui retiré, cités **deux fois chacun**, à l'avant-propos et à l'annexe A — les deux sièges du récit de la décision P0.2. ⚠ **R-10 est sans objet à date et reste armé** ; ces douze occurrences ne le déclenchent pas au sens d'une faute, elles nomment ce qui **n'a pas** été déposé |
| **R-11** | 145 | `2035` 58, `2030` 41, `NIST IR 8547` 18, `post-quantique` 16, `IR 8547` 9, forme verbatim complète 3 |
| **R-13** | 32 | forme ancrée ; voir §4.1 |
| **R-14** | **1 313** (avec `-i`) | `aucun` 1 139, `le socle ne documente` 156, `n'existe pas` 18 |
| **CA-03** | 316 | voir §3.3 |
| **CA-11** | 1 373 | voir §3.11 |

**Aucun motif ne rend zéro sur le corpus** : les quinze ressortent, et leur somme est de **3 511 captures**. Les ventilations données ci-dessus se resomment à leur total, motif par motif — 32 pour R-13, 145 pour R-11, 1 313 pour R-14, 316 pour CA-03, 1 373 pour CA-11.

### 4.3 Ce que le rejeu établit, et ce qu'il n'établit pas

**Établi.** Les quinze motifs ont été passés sur le **domaine entier** — les 34 corps, jamais un échantillon —, avec `-i` sur R-14 sans exception et sous `LC_ALL=C.UTF-8`. **Les 34 pièces portent, dans leur bloc `## Notes`, un bilan de rejeu daté du 22 juillet 2026** : le contrôle a cherché la conjonction « rejeu » et « 22 juillet 2026 » dans chaque fichier, et **aucune pièce n'en est dépourvue**. Les quatre motifs à faible cardinal — R-02, R-07, R-08, R-10, soit **39 captures** (5 + 19 + 3 + 12) — ont été **ouvertes en totalité par la présente passe**, et aucune n'établit de faute.

**Non établi, et c'est la borne principale de ce rapport.** CA-02 exige que le contrôle outillé soit *« complété par une inspection humaine »*, au motif que *« la leçon du Vol. II est qu'une faute passe sous l'outil sans passer sous la règle »*. Le corpus porte **3 511 captures** des quinze motifs ; **la présente passe en a ouvert 39**, soit **1,1 %**. L'inspection occurrence par occurrence est **déclarée conduite par les neuf passes de balayage de P5.2**, chacune à son bloc de pièces — cette passe **ne la refait pas** et **ne la certifie pas**. *Une passe qui écrirait ici que l'inspection a eu lieu attesterait depuis un document amont ; c'est le geste que CA-14 proscrit.*

⚠ **Un balayage vert ne dit rien de R-12.** Aucun motif ne le couvre, et aucun décompte ne le supplée.

---

## 5. CA-12 — la couverture réelle après la passe du 22 juillet 2026

**Énoncé (PRD §11)** : *« Aucun élément de la Partie IV — ni d'aucune pièce de `verification/`, ni d'aucune entrée du socle §7.8 — ne permet de dériver une attaque. Contrôle par relecture dédiée, distincte de la relecture de conformité et confiée à un relecteur distinct du rédacteur (CA-14) ; **le compte rendu est déposé sous `verification/`** et **nommé dans la pièce qu'il couvre**. »*

### 5.1 Ce qui est déposé, constaté sur le répertoire

Le répertoire `verification/` portait **27 fichiers** au moment du relevé, **avant le dépôt du présent rapport**, qui le porte à 28. ⚠ *Le cardinal est borné à cet instant parce que la passe qui le publie le modifie ; une « re-mesure sur le répertoire courant » ne vaudrait pas au-delà de la phrase qui la porte.* **Deux de ces fichiers sont des comptes rendus CA-12** :

| Fichier | Périmètre déclaré à son en-tête, ouvert et lu | Résultat déclaré |
|---|---|---|
| [`relecture-CA-12-P3.md`](relecture-CA-12-P3.md) | **intégral** : `04-partie-IV/`, ch. 12 à 15, corps et Notes. **borné** : 4 sections hors Partie IV — ch. 1 §1.2, ch. 4 §4.3, ch. 10 §10.1, ch. 20 §20.2 | **1 retrait** (ch. 15 §15.3) ; 0 charge utile, 0 séquence, 0 preuve de concept ; 8 passages conservés avec motif |
| [`relecture-CA-12-lots.md`](relecture-CA-12-lots.md) | **13 rapports de lot** lus en entier — L-01, L-02, L-04 à L-07, L-09 à L-14 et L-14b | **2 retraits** (L-09 §E point 5, L-10 §E point 7) ; 0 charge utile, 0 séquence, 0 preuve de concept, 0 code offensif ; 6 passages conservés avec motif |

**Aucun autre compte rendu CA-12 n'est déposé.** Le constat est pris **sur le répertoire**, et non sur une déclaration de passe. *Les périmètres et les résultats de la table ci-dessus sont ceux que les deux fichiers déclarent à leur en-tête ; la présente passe les a lus, elle ne les a pas rejoués.*

### 5.2 Ce que la passe du 22 juillet 2026 a laissé sur disque

**Cinq passes de relecture CA-12 couvrant les 34 pièces sont déclarées par l'ordonnancement de la phase.** Cette passe n'en constate ni la tenue, ni la distinction du relecteur : elle constate **ce qui subsiste sur disque**. Les retraits annoncés ont été cherchés **un par un dans le corps de leur pièce** :

| Siège du retrait | Clause retirée | Constat au corps |
|---|---|---|
| ch. 7, `## Notes` | « la pièce ne traite pas de matière offensive » | **0 occurrence vivante** |
| ch. 8, `## Notes` | même clause | **0 occurrence vivante** |
| ch. 10, `## Notes` | « — il l'applique, » | **0 occurrence vivante** |
| ch. 14, `## Notes` | « elle est la seule de la Partie IV dont la matière est intégralement défensive » | **0 occurrence vivante** ; la formule subsiste **citée entre guillemets dans le journal de retrait**, ce qui est la pratique prescrite |
| ch. 15, corps §15.2 | « Conformément au traitement défensif exclusif du volume […] » | **0 occurrence vivante** au corps |
| ch. 25, `## Notes` | « ne portent ni séquence, ni charge utile, ni identifiant de vulnérabilité » | **0 occurrence vivante** |

**Balayage complémentaire sur `monographie/` entier** : la chaîne « matière offensive » ne subsiste qu'à **deux endroits**, ch. 17 et ch. 19, **tous deux dans un journal de retrait** daté et non dans une attestation vivante. Constat pris sur les deux fichiers, ligne par ligne.

**Les six retraits relèvent tous de la même famille** — l'attestation auto-délivrée —, et **les six sont effectivement appliqués**. ⚠ **Ce constat porte sur ce qui a été retiré, non sur ce qui aurait dû l'être** : établir qu'aucune charge utile ne subsiste exigerait de relire les 34 pièces sous la lentille de la dualité d'usage, ce que la présente passe n'a pas fait.

### 5.3 Ce que la couverture laisse — et c'est ici que le critère n'est pas tenu

**Trois manques, chacun constaté et non déduit.**

1. **Aucun compte rendu n'est déposé sous `verification/` pour les cinq passes du 22 juillet 2026.** CA-12 en fait un terme explicite. Les traces de ces passes vivent **uniquement dans les blocs `## Notes` des pièces**, sous forme de journaux de retrait. *Un journal dans la pièce contrôlée n'est pas un compte rendu déposé par un contrôleur distinct : c'est la pièce qui rend compte d'elle-même, et c'est la forme que CA-12 range parmi les non-contrôles.*
2. **Le second terme du critère — « nommé dans la pièce qu'il couvre » — est tenu par 18 pièces sur 34.** Relevé fichier par fichier : **18** pièces citent `relecture-CA-12-P3.md` — dont 2 citent en outre `relecture-CA-12-lots.md` — et **16 n'en nomment aucun** : avant-propos, ch. 3, ch. 6, ch. 7, ch. 11, ch. 16, ch. 21, ch. 22, ch. 23, ch. 24, ch. 26, ch. 27, ch. 28, annexe B, annexe C, annexe D. ⚠ **Dix de ces seize sont des pièces de P4** — avant-propos, ch. 22, 23, 24, 26, 27, 28, annexes B, C, D —, que la passe de P3 ne couvrait pas et pour lesquelles aucun compte rendu n'a été déposé depuis ; les **six autres** sont des pièces du tronc — ch. 3, 6, 7, 11, 16, 21. Décompte fait sur les deux ensembles, non déduit.
3. **Le périmètre étendu du critère demeure partiellement non couvert.** CA-12 vise, depuis l'extension du 21 juillet 2026, `verification/` **et** les entrées du socle §7.8. Les **13 rapports de lot** ont été lus par [`relecture-CA-12-lots.md`](relecture-CA-12-lots.md), qui déclare lui-même trois bornes : **sources primaires non rouvertes**, **aucun contrôle de migration rapport → pièce**, `monographie/` hors périmètre. Le **contrôle de migration** — vérifier qu'une matière retirée d'un rapport de lot n'a pas reparu dans une pièce — **n'a été conduit par aucune passe**, et aucun fichier de `verification/` ne le revendique. Constat pris sur le répertoire.

⚠ **Cinq rapports de lot portent des attestations auto-délivrées d'un autre critère** que R-12 — bornage, neutralité fournisseur —, **signalées et non corrigées** au titre de l'unicité de la lentille CA-12. Ouvert sous **R-G-49**, en tension déclarée avec **R-G-07** — *un rapport de lot ne se réécrit pas*, et deux l'ont pourtant été.

---

## 6. Ce que la présente passe a trouvé et n'a pas corrigé

**Aucune pièce, aucun document de gouvernance et aucun rapport antérieur n'a été modifié par cette passe.** Les points ci-dessous sont **signalés** ; leur correction relève des instances nommées à la dernière colonne.

| # | Constat | Siège | Instance |
|---|---|---|---|
| 1 | **CA-12 : aucun compte rendu déposé** pour les cinq passes du 22 juillet 2026, et **16 pièces sur 34** ne nomment aucun compte rendu | `verification/` ; 16 pièces | déposer les comptes rendus relève de l'**exécution** ; juger si un journal en pièce en tient lieu modifie la lecture d'un **critère** → **auteur** |
| 2 | **CA-10 branche (c) : 137 mobilisations de garde-fou sur 382 ne nomment pas leur volume** | **23 pièces** | **auteur** — le grain du critère (occurrence, ou pièce avec convention déclarée) |
| 3 | **Renvoi ambigu du ch. 12** : « adossée au Vol. I, au ch. 22 §22.3 », alors que le §22.3 visé est celui du **présent** volume et que le Vol. I n'en porte aucun | ch. 12, corps | **exécution** — renvoi |
| 4 | **CA-07 : l'annexe C porte son unique marquage sans la clause « n'établit pas »**, la borne y étant écrite sous une autre forme | annexe C, corps | **exécution** — forme ; **auteur** si la forme du marquage est tenue pour prescriptive |
| 5 | **Quatre revendications de verbatim reposent sur un fichier retiré du dépôt** ; exactes contre le blob `fd8f1be~1`, non opposables au dépôt courant | ch. 24, ch. 25, ch. 27 (H-27) ; ch. 10 (H-28) | **auteur** — R-G-52, charge éditoriale d'un autre volume |
| 6 | **Trois lignes du registre de gel et trois cardinaux publiés sont périmés** (voir §7) | registre, annexe A, avant-propos, rapports | **exécution** — P5.3 |
| 7 | **Écart d'un jour entre la date de gel déclarée (21 juillet) et les derniers correctifs (22 juillet)** sur treize pièces | 34 en-têtes, registre | **auteur** — la date de gel est un fait de gouvernance |

⚠ **Aucun de ces sept points n'est inscrit au registre des remontées par la présente passe.** Le registre porte **52 remontées**, R-G-01 à R-G-52 — **39 tranchées, 3 sans objet, 10 ouvertes** —, cardinal **recompté marqueur par marqueur** sur les en-têtes du fichier le 22 juillet 2026. **Leur inscription est due et n'a pas été faite ici** : écrire au registre excède le mandat de cette passe, et l'omettre serait laisser sept constats sans siège.

---

## 7. Décomptes constatés périmés — matière de P5.3

**La volumétrie a été re-mesurée en une passe unique, par la seule commande de PRDPlan §1.5, sur les 34 pièces.** Résultat : **160 450 mots**. Les porteurs publient **160 447**. **L'écart de trois mots est intégralement imputé, et l'imputation ferme le compte** :

| Pièce | Registre de gel | Mesure du 22 juillet 2026, fin de chaîne | Cause |
|---|---|---|---|
| ch. 12 | 4 314 | **4 316** | correctif de tri prospectif appliqué par la passe de balayage de la Partie IV ; **l'en-tête de la pièce porte déjà 4 316** |
| ch. 15 | 4 171 | **4 167** | retrait CA-12 au §15.2 ; **l'en-tête porte déjà 4 167** |
| ch. 28 | 10 991 | **10 996** | deux corrections d'attribution au §28.2 ; **l'en-tête porte déjà 10 996** |
| **Total** | **160 447** | **160 450** | **+2 − 4 + 5 = +3** |

**Les 34 en-têtes concordent avec la mesure**, champ par champ — **34 sur 34**, y compris le ch. 27, dont l'en-tête porte les deux valeurs **bornées à leur arbre** (10 648 au commit `fd8f1be`, 10 652 sur l'arbre de travail). **C'est le registre qui est en retard sur les pièces, non l'inverse.**

**Deux cardinaux de bloc sont périmés du même mouvement**, re-mesurés ici :

- **tronc (ch. 1 à 21)** : **87 005** mots, et non 87 007 — l'écart reste **+38,1 %** ;
- **appareil et Parties VII à IX (13 pièces)** : **73 445** mots, et non 73 440 — l'écart reste **+85,9 %**.

⚠ **Les pourcentages ne bougent pas ; les cardinaux absolus, oui.** Les porteurs à réaligner ont été relevés fichier par fichier : `87 007` vit dans l'avant-propos, l'annexe A, le registre de gel, `relecture-P4.md`, `remontees-gouvernance.md` et le PRDPlan ; `73 440` et `160 447` vivent dans le registre, `relecture-P4.md` et `remontees-gouvernance.md`, et `160 447` en outre au PRDPlan. **Aucun n'est corrigé ici** — le réalignement des porteurs est l'objet de **P5.3**, et le faire pièce par pièce en dehors de cette activité reproduirait la désynchronisation qu'elle est chargée de résorber.

☑ **P5.3 exécutée — 22 juillet 2026, en fin de chaîne.** Le réalignement des porteurs a eu lieu. ⚠ **La mesure de 160 450 ci-dessus était une mesure d'ouverture de passe** : les retraits CA-12 de la passe P5.1 — ch. 1 (−4), ch. 25 (−3), avant-propos (−8), ch. 28 §28.3 (−8), soit **−23 mots** — lui sont postérieurs, et le ch. 28 est passé de 10 996 (ouverture) à **10 988** (après retrait CA-12, valeur portée à son en-tête). La re-mesure de fin de chaîne P5.3 sur les 34 pièces donne **160 427 mots** (tronc **87 001**, appareil **73 426**), et **les 34 en-têtes concordent avec elle, champ par champ**. Porteurs réalignés : registre de gel (colonne « Réel » et bilan), `CLAUDE.md` du volume, PRDPlan (en-tête), R-G-47 du registre des remontées, README du dépôt (section Vol. III) ; les rapports de phase [`relecture-P4.md`](relecture-P4.md) et le présent §7 conservent leurs mesures d'époque, datées. **160 450 est conservée ici comme mesure d'ouverture de P5** et ne vaut plus mesure courante.

---

## 8. Options posées, non tranchées

*Les points qui suivent relèvent de l'auteur au titre de PRDPlan §5.3 — critère d'acceptation, garde-fou, ou fait de gouvernance. Ils sont posés avec leurs options et leur coût ; aucun n'est arbitré.*

**A. Grain de CA-10, branche (c).** *Option 1 — qualification à chaque occurrence* : **137 corrections réparties sur 23 pièces**, aucune ambiguïté résiduelle, coût en verbosité concentré sur les pièces d'appareil et de composition — ch. 27, ch. 28, ch. 22, avant-propos, annexes B et C portent à elles seules **83 des 137**. *Option 2 — convention déclarée une fois par pièce* : **18 pièces à doter d'une clause de convention** — cinq la portent déjà —, les 137 occurrences demeurant inchangées, et **l'énoncé de CA-10 à amender**, puisqu'il écrit « tout renvoi ». *Option 3 — statu quo, l'écart étant documenté ici* : le critère demeure non tenu à sa lettre, et le rapport de sortie de J-6 le porte.

**B. Terme procédural de CA-12.** *Option 1 — déposer les cinq comptes rendus sous `verification/` et les nommer dans les 34 pièces* : le critère est tenu à sa lettre ; coût, cinq fichiers à écrire depuis les journaux existants et 34 en-têtes ou blocs Notes à compléter. ⚠ **Écrire un compte rendu depuis les journaux des pièces qu'il couvre reviendrait à faire attester le contrôle par le contrôlé** — c'est la faute que CA-12 nomme, et l'option n'est tenable que si les passes rendent leur propre relevé. *Option 2 — tenir les journaux en pièce pour l'équivalent d'un compte rendu déposé* : exige d'amender l'énoncé de CA-12, qui distingue expressément les deux. *Option 3 — rejouer les cinq passes en déposant leur compte rendu* : coût le plus élevé, et le seul qui produise un contrôle **et** sa trace conformes à l'énoncé.

**C. Écart d'un jour sur la date de gel.** *Option 1 — conserver le 21 juillet 2026 partout*, l'écart étant consigné : c'est l'état actuel, et il est déclaré. *Option 2 — porter au 22 juillet 2026 les treize pièces dont les correctifs datent du 22* : 13 en-têtes et 13 lignes de registre, et deux dates de gel coexistant dans l'ouvrage. *Option 3 — porter les 34 au 22 juillet 2026* : une seule date, mais elle **avance le gel de 21 pièces qui n'ont pas bougé**, ce qui est un fait inexact.

**D. Forme du marquage CA-07 à l'annexe C.** *Option 1 — rendre la forme prescrite* : la clause « ce qu'il n'établit pas » est ajoutée, la borne étant déjà écrite sous une autre tournure. *Option 2 — tenir la tournure « établissant seulement que » pour une forme admissible de la borne* : exige de le dire à CA-07, faute de quoi le prochain contrôle rendra le même écart.

---

## 9. Ce que ce rapport ne dit pas

*Une passe qui ne borne pas son périmètre laisse croire qu'elle l'a couvert.*

1. **Il n'atteste la conformité d'aucune pièce à aucun critère**, et il n'atteste pas la sienne. Il consigne des mesures, leur domaine et leur date.
2. **Les 34 pièces n'ont pas été lues intégralement par cette passe.** Ont été ouverts en contexte : les 39 captures des motifs R-02, R-07, R-08 et R-10 ; les 11 premières mobilisations d'entrée [C] sans marqueur de proximité ; les 8 pourcentages ; les 3 marquages d'ouverture de CA-07 ; les 22 sièges de lacune ; les 6 sièges de retrait CA-12 ; les 4 contextes de renvoi au Vol. I que le contrôle négatif a signalés ; les 2 mobilisations de question du Vol. II non qualifiées dans leur fenêtre ; les 3 renvois d'annexe inter-pièces ; les 3 formes distinctes de la branche `conformité.*E-23`. **Tout le reste du corpus a été mesuré, non lu.**
3. **L'inspection occurrence par occurrence exigée par CA-02 n'a pas été refaite.** Elle est déclarée par les neuf passes de balayage de P5.2, chacune à son bloc ; **cette passe ne l'a ni rejouée, ni contrôlée par sondage**. Sur **3 511 captures**, **39** ont été ouvertes ici.
4. **Aucune source primaire n'a été rouverte**, à deux exceptions nommées : `Monographie.md` §3.10.1 du Vol. I, ouvert au dépôt courant, et le contenu de `Synthese Monographie.md` au commit `fd8f1be~1`, ouvert par `git show`. Sur les **24 revendications de verbatim** du corpus, **2 ont été confrontées au texte vivant de la source**, **4 au contenu d'un blob git** — ce qui n'en est pas l'équivalent —, et **18 n'ont été confrontées à rien**.
5. **Les 15 rapports de lot n'ont pas été ouverts par cette passe**, hormis le relevé de leur cardinal sur le répertoire. Le socle n'a été ouvert qu'au PRD, pour relever les niveaux et les plages d'identifiants.
6. **CA-12 n'a pas été rejouée.** Cette passe constate ce que les cinq passes du 22 juillet 2026 ont laissé sur disque — retraits appliqués, comptes rendus absents — ; elle **ne relit aucune pièce sous la lentille de la dualité d'usage**. La question « un lecteur peut-il dériver une attaque de ce texte ? » n'a pas été posée ici.
7. **Le contrôle de migration rapport → pièce n'a pas été conduit**, ni par cette passe ni par aucune autre. Son absence est constatée sur le répertoire, non déduite.
8. **La centralité d'une affirmation, la première occurrence d'un terme anglais, la nature prospective d'un énoncé et l'exhaustivité du marquage d'inférence sont des jugements, non des relevés.** Les quatre volets de critère qui en dépendent — CA-01, CA-08, CA-11, CA-07 — sont portés NON CONSTATABLES à ce titre, et non tenus pour satisfaits.
9. **La distinction rédacteur / relecteur n'est pas constatable sur les fichiers** (R-G-19, réserve 1). Aucune conclusion n'en est tirée dans un sens ni dans l'autre.
10. **Aucun décompte publié ailleurs n'a été corrigé**, et aucune remontée n'a été inscrite au registre. Les sept constats du §6 et les quatre options du §8 attendent leur siège.
11. **J-6 n'est pas atteint, et ce rapport ne peut pas le rendre atteint.** Il est **un** des trois termes du jalon. Le deuxième — la revalidation de moins de trente jours — est déposé et non encore versionné. **Le troisième — le PDF régénéré et versionné avec sa source — n'existe pas** : le volume n'a aucun pipeline de rendu, et en créer un serait une troisième copie du pipeline du Vol. I (PRDPlan §7, activité P5.4).
