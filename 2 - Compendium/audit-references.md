# Annexe — Inventaire et validation des références

*Rapport de mesure daté du 29 juillet 2026, ajouté au rendu après le chapitre 50 sur instruction
d'auteur. Hors plan : il n'est aucune des neuf annexes A à I que le `TOC.md` prévoit, et il ne
prend pas leur place.*

## Régime de ce rapport

| Champ | Valeur |
|---|---|
| **Nature** | **Rapport de mesure, sans autorité.** Ni source, ni socle, ni décision — même régime que [`audit.md`](audit.md). Ses constats sont des **remontées en attente d'arbitrage** ; aucun n'est arbitré, et il n'alloue aucun identifiant de remontée (PRD §13). ⚠ **Être relié n'est pas faire autorité** : sa présence dans le rendu paginé ne lui en confère aucune, et **il ne se cite pas à l'appui d'un énoncé**. |
| **Domaine** | Le corpus du commit **`d81b63c`** (29 juillet 2026) : les **50 pièces** `.md` des cinq Livres, l'Annexe B ([`PRD/socle-consolide.md`](PRD/socle-consolide.md) v1.2), le [`TOC.md`](PRD/TOC.md) v0.31, le [`PRD.md`](PRD/PRD.md) v0.15 et [`compendium.pdf`](compendium.pdf). **Domaine entier, aucun échantillon.** |
| **Méthode** | Tous les cardinaux sont **mesurés sur les fichiers**, jamais recopiés d'un document amont. La délimitation du corps d'une pièce est celle de [`PRD/decompte.sh`](PRD/decompte.sh) (`corps_compendium` : du premier `---` à la ligne « Note de statut »), reprise telle quelle pour distinguer ce que le corps cite de ce que l'en-tête déclare. Les décomptes du §8 de l'Annexe B ont été **re-calculés indépendamment** et concordent (§ 1.3). |
| **Ce qu'il ne fait pas** | Il **ne valide aucune source primaire** — aucun document externe n'a été ouvert ; il **ne conduit aucun vote adversarial** ; il **ne relit pas** — CA-IV-11 et CA-IV-13 exigent une seconde personne, et ce rapport est produit par un agent. |

## 1. Combien de références — l'inventaire

### 1.1 Le compendium ne porte aucune bibliographie, et c'est le premier fait

**Zéro entrée bibliographique, zéro URL, aucune référence numérotée.** Mesuré sur l'ensemble des
`.md` du dossier :

| Grandeur mesurée | Domaine | Résultat |
|---|---|---|
| Entrées de bibliographie | 50 pièces + annexes | **0** — aucune annexe du plan n'est rédigée |
| URL (`http://`, `https://`) | tous les `.md` du volume | **0** |
| DOI | tous les `.md` du volume | **10** (3 en chapitre, 7 au `TOC.md`) |
| Identifiants arXiv | tous les `.md` du volume | mentions dispersées, **aucune entrée normalisée** |

L'**Annexe I — Bibliographie générale consolidée** est **planifiée, non écrite** : le `TOC.md` lui
assigne une enveloppe de 40 000 mots et déclare son **plancher mesuré à 1 270 entrées et
37 104 mots pour le seul Vol. I**, avant fusion des corpus des Vol. II et III. C'est le seul
cardinal bibliographique que le volume possède aujourd'hui, et il désigne un livrable **à produire**.

⚠ **Conséquence pour le rendu paginé.** `build/assemble.py` n'assemble que les fichiers
`Livre */[0-9]*.md` — les cinquante chapitres — et, depuis le 29 juillet 2026, le présent rapport.
Le PDF ne contient **ni bibliographie, ni Annexe B, ni table de correspondance** : un lecteur du
rendu **ne peut résoudre aucun renvoi de socle**, ni `S-nnn`, ni `F-xx`. *L'appareil de référence du
volume existe, mais il n'est pas dans le livrable qu'on lit.*

### 1.2 L'appareil de référence qui existe : 159 entrées

Le compendium n'a pas de bibliographie ; il a une **table des faits** — le socle consolidé de
l'Annexe B, qui est ce contre quoi les chapitres adossent leurs énoncés.

**Total mesuré : 159 entrées, `S-001` à `S-159`, série continue, sans trou ni doublon** (vérifié
ligne à ligne sur les tables des §3.1 à §3.3 de l'Annexe B).

| Volume d'origine | Plage | Entrées mesurées |
|---|---|---|
| Vol. II, *L'autonomie encadrée* | `S-001` → `S-046` | **46** |
| Vol. III, *L'entreprise agentique* (socle propre) | `S-047` → `S-142` | **96** |
| Vol. I, *Interopérabilité agentique* (par les `H-17…H-33`) | `S-143` → `S-159` | **17** |
| **Total** | `S-001` → `S-159` | **159** |

**Identité de clôture recalculée indépendamment et vérifiée** : 46 identifiants `F-xx` du Vol. II
(hors les trois lignes de signalement `F-12`, `F-13`, `F-14`) + 98 `F-xx` du Vol. III + 33 `H-xx`
du Vol. III = **177 identifiants sources** = 159 entrées + 13 fondues + 5 exclues. ✔

**Cinq entrées sources sont exclues**, chacune avec son motif : `F-92` et `F-96` du Vol. III (dette
de vote adversarial non résorbée), `H-13`, `H-15` et `H-16` du Vol. III (hors socle factuel — un
garde-fou et deux thèses attribuées). S'y ajoutent, sans avoir jamais été des entrées, les **huit
affirmations réfutées** `R-1` à `R-8` du Vol. II, proscrites dans l'ouvrage.

### 1.3 Contrôle de concordance avec les décomptes publiés

Chaque cardinal de l'Annexe B a été re-calculé sur ses tables plutôt que lu à son §8. **Aucun écart.**

| Grandeur | §8 de l'Annexe B | Re-mesure indépendante |
|---|---|---|
| Entrées | 159 | **159** ✔ |
| `[A]` / `[A/B]` / `[B]` / `[B/C]` / `[C]` | 56 / 1 / 79 / 2 / 21 | **56 / 1 / 79 / 2 / 21** ✔ |
| Niveau hérité d'une phrase de portée | 29 | **29** ✔ |
| Entrées fondues (deux identifiants sources) | 13 | **13** ✔ |
| Sensibilité temporelle / sans objet | 123 / 36 | **123 / 36** ✔ |
| Re-datation : inchangée / dont partielles / changée / non établie | 91 / 28 / 10 / 22 | **91 / 28 / 10 / 22** ✔ |

⚠ **Une ambiguïté de notation est relevée, et elle n'est pas de forme.** Les **36 entrées sans
sensibilité temporelle** portent en colonne de re-datation le marqueur **`☐ due`**, que le §8.7 lit
comme « sans objet ». Les deux lectures sont incompatibles : un lecteur qui dépouille la colonne
seule compte **58 re-datations en souffrance** (36 + 22) là où le décompte publié en compte 22.
*Le même glyphe sert à deux états contraires — « rien à faire » et « non établi ».*

### 1.4 Un troisième cardinal, indicatif seulement

Les cinquante pièces nomment en clair des documents normatifs sans les référencer : un relevé par
motif (RFC, NIST SP/IR/AI, ISO, ISO/IEC, ECMA, SLSA, CycloneDX, SPDX) fait apparaître
**38 identifiants distincts** — dont 14 RFC et 15 normes ISO ou ISO/IEC. ⚠ **Ce chiffre est
indicatif et non opposable** : le relevé est fondé sur des motifs, il ne dédoublonne pas les
millésimes (`ISO/IEC 25010` et `ISO/IEC 25010:2023` y comptent deux fois) et il ne couvre pas les
sources citées en prose sans identifiant normalisé. *Il mesure une littératie normative, pas un
appareil bibliographique.*

## 2. La grille de validation — critères et cotations

Cinq critères, tous **dérivés de données portées par le corpus**, aucun estimé.

| Critère | Ce qu'il mesure | Source de la mesure |
|---|---|---|
| **Fiabilité** | ce que l'affirmation a **subi** | niveau `[A]`/`[B]`/`[C]` et marqueurs de l'Annexe B |
| **Viabilité** | l'état de la source **à sa re-datation** du 28 juillet 2026 | colonne de re-datation |
| **Pertinence** | l'usage **effectif** de l'entrée par les cinquante pièces | occurrences mesurées, corps contre en-tête |
| **Traçabilité** | la résolution d'un renvoi vers l'entrée | résolution des `S-nnn` et des `F-xx`/`H-xx` |
| **Opposabilité** | l'aptitude à porter un fait **central** (CA-IV-01) | niveau et régime déclaré |

### 2.1 Fiabilité — ce que le niveau atteste, et ce qu'il n'atteste pas

| Cote | Signification | Entrées | Part |
|---|---|---|---|
| **A** | `[A]` à marquage individuel — vote adversarial 3-0 chez la source | 36 | 22,6 % |
| **A⁻** | `[A]` **hérité d'une phrase de portée générale** | 20 | 12,6 % |
| **B** | `[B]` à marquage individuel — source primaire ouverte et citée | 63 | 39,6 % |
| **B⁻ (portée)** | `[B]` hérité de la phrase de portée du §7.8 du Vol. II | 9 | 5,7 % |
| **B⁻ (composition)** | `[B]` obtenu par **rétrogradation** d'une entrée composite | 7 | 4,4 % |
| **C** | repérage — source identifiée, contenu non extrait | 21 | 13,2 % |
| **mixtes** | `[A/B]` (1) et `[B/C]` (2) | 3 | 1,9 % |

⚠ **Trois réserves bornent la lecture de ce tableau, et aucune n'est de style.**

1. **Aucun vote adversarial n'a été conduit par le compendium.** Les 56 entrées `[A]` tiennent leur
   niveau de leur volume source ; le volume qui les consolide **n'a re-soumis aucune affirmation à
   une épreuve**. Le niveau est **conservé, jamais re-subi**.
2. **Vingt-neuf entrées sur 159 — dont vingt des quarante-six du Vol. II — tiennent leur niveau
   d'une phrase qui parlait d'autres entrées en même temps.** L'Annexe B matérialise l'héritage par
   un marqueur mais **ne résout pas la dépendance**. Le fait est documenté d'un précédent : cette
   même construction a déjà fourni au ch. 18 du Vol. II sa couverture pour écrire « niveau [A] » sur
   un contenu `[B]`.
3. **Le socle est de second rang.** Les trois extractions dont l'Annexe B procède portent sur les
   **PRD des volumes**, non sur les documents que ces PRD citent (réserve 9). *Aucun énoncé n'a été
   confronté à sa source primaire par la passe qui a constitué le socle* — la re-datation du
   28 juillet a constaté **l'état d'un document à une date**, non la véracité de l'énoncé.

### 2.2 Viabilité — l'état des sources au 28 juillet 2026

| Cote | État | Entrées | Part |
|---|---|---|---|
| **V0** | sans sensibilité temporelle — re-datation sans objet | 36 | 22,6 % |
| **V1** | ☑ inchangée, intégralement ré-établie | 63 | 39,6 % |
| **V2** | ☑ inchangée **partiellement** — une composante seulement constatée | 28 | 17,6 % |
| **V3** | ☑ **changée** — la source a bougé depuis la rédaction de l'entrée | 10 | 6,3 % |
| **V4** | ☐ **non établie** — la re-datation n'a pas pu aboutir | 22 | 13,8 % |

⚠ **« Inchangée » n'est pas « confirmée », et l'écart est chiffré** : sur les 123 entrées à
sensibilité temporelle, **63 seulement sont intégralement ré-établies**. Les 28 partielles portent
une composante constatée et une composante non re-vérifiée.

⚠ **Trente-deux entrées sont d'une actualité problématique** : les 10 dont la source a changé et les
22 dont l'état n'a pu être établi. **`S-001` en fait partie** — la révision MCP `2025-11-25` que
l'entrée donne pour courante a été remplacée le 28 juillet 2026 par `2026-07-28`, soit **le
lendemain du gel** ; et c'est l'entrée la plus citée du corpus, avec 81 occurrences.

⚠ **Trente-cinq entrées portent un statut de source non stabilisé** — préversion, *preview*,
*release candidate*, *Development*, projet, consultation en cours, non adopté. ⚠ **Dix-neuf entrées
ont un terme postérieur au gel** : `S-009`, `S-016`, `S-019`, `S-021`, `S-023`, `S-027`, `S-032`,
`S-075`, `S-088`, `S-106`, `S-109`, `S-112`, `S-114`, `S-126`, `S-131`, `S-132`, `S-143`, `S-144`,
`S-147` — l'échéance commune E-23 / AMF du 1ᵉʳ mai 2027 en concentre plusieurs.

### 2.3 Pertinence — l'usage réel par les cinquante pièces

Mesuré sur les cinquante pièces, en séparant le **corps** — ce que le rendu publie — de l'**en-tête**
et de la note de statut, que la coupe retire.

| Cote | Usage | Entrées | Part |
|---|---|---|---|
| **P1** | citée dans le **corps** d'au moins une pièce | 44 | 27,7 % |
| **P2** | citée **seulement** en en-tête (« Socle mobilisé ») ou en note | 47 | 29,6 % |
| **P3** | **jamais citée** sous son identifiant consolidé | 68 | 42,8 % |

⚠ **Ce tableau se lit avec sa cause, sinon il induit en erreur.** Les cinquante chapitres ont été
rédigés le **27 juillet 2026** ; le socle consolidé a été constitué le **28**. Les pièces citent
donc massivement les identifiants **sources** — `F-xx`, `H-xx` — et non la série `S-nnn` que le
volume a créée pour les remplacer. **Quarante et une pièces sur cinquante citent au moins un
identifiant source**, pour **1 853 occurrences de `F-xx` et 363 de `H-xx`**.

**Atteignabilité réelle des 159 entrées, sous trois conventions de résolution :**

| Convention | Entrées atteintes | Non atteintes |
|---|---|---|
| **A — stricte** : seul le renvoi `S-nnn` littéral compte | **91** | 68 |
| **B — moyenne** : `S-nnn`, plus tout `F-xx`/`H-xx` dont le volume est nommé à ±1 ligne | **154** | **5** |
| **C — large** : toute résolution possible d'un `F-xx`, ambiguïté ignorée | **159** | 0 |

**Les cinq entrées hors d'atteinte en convention B** — `S-063`, `S-068`, `S-070`, `S-100`, `S-108` —
**ne le sont pas faute de matière**. Vérification faite sur pièce : le ch. 21 traite bien FIPS 203 et
FIPS 204 et cite `F-62` — l'origine de `S-108` — **six fois, sans jamais nommer le volume**. *La
matière est présente ; c'est le pointeur qui est ambigu.*

⚠ **Une pièce sur cinquante ne mobilise aucune entrée de socle sous son identifiant consolidé** : le
**ch. 35**, les études de cas de production canadienne. Son en-tête nomme pourtant douze entrées du
Vol. II (`F-17`…`F-48`) et signale qu'elles résolvent au socle consolidé — **sans écrire les `S-nnn`
correspondants**. *Sur un chapitre d'études de cas, la correspondance non écrite est précisément
celle qu'un lecteur voudrait suivre.*

### 2.4 Traçabilité — le défaut le plus étendu du volume

⚠ **Sept cent vingt-quatre renvois `F-01`…`F-48` sont écrits sans que le volume soit nommé, dans des
pièces qui consomment les deux volumes.** C'est exactement l'indécidabilité que l'Annexe B nomme à
son §1 — *« un `F-xx` nu est indécidable »* — et qui a motivé la création de la série `S-`.

Le décompte se lit ainsi : sur **1 853 renvois `F-xx`** relevés dans les cinquante pièces, **601
portent un numéro supérieur à `F-48`** et sont donc décidables par la plage seule, le Vol. II
s'arrêtant à `F-48` ; **1 252 tombent dans la plage partagée `F-01`…`F-48`**, dont **724 sans mention
de volume à ±1 ligne**. ⚠ **Le contexte de la pièce ne les sauve pas** : **les quarante et une pièces
qui citent un `F-xx` nomment toutes les deux volumes**, de sorte qu'aucune ne fournit de
désambiguïsation implicite au niveau du fichier.

Pièces les plus exposées : ch. 45 (106 renvois nus), ch. 16 (78), ch. 12 (76), ch. 15 (74), ch. 14 et
ch. 43 (70 chacun).

⚠ **Réserve de méthode, à porter avec le chiffre** : la fenêtre de mesure est de deux lignes. Un
titre de section ou un paragraphe antérieur peut nommer le volume au-delà. **724 est donc une borne
supérieure au grain de la ligne**, non un décompte de fautes établies. *Il faudrait une lecture pièce
par pièce pour le convertir en cardinal opposable.*

### 2.5 Opposabilité — ce qui ne peut pas porter un fait central

**Vingt-trois entrées sur 159 ne peuvent porter aucun fait central** au sens de CA-IV-01 : les **21**
en `[C]` et les **2** `[B/C mixte]` dont le volet `[C]` n'est pas élevé. Elles se citent en
corroboration, jamais en appui.

⚠ **Neuf d'entre elles sont citées dans le corps d'une pièce** — `S-082`, `S-102`, `S-143`, `S-144`,
`S-149`, `S-152`, `S-153`, `S-154`, `S-157`. **Vérification menée sur les neuf, non sur un
échantillon** : chacune est citée **avec sa réserve écrite sur place** — niveau `[C]` déclaré,
re-datation « non établie » nommée, ou source retirée du dépôt signalée. **Aucune n'est employée en
appui d'un énoncé central.** *La discipline tient là où elle était le plus exposée.*

⚠ **Un fait de régime prime les cinq critères** : le volume est **arrêté sous dérogation** (D-10,
PRD v0.15 §14), et **CA-IV-11 comme CA-IV-13 sont dérogés, non satisfaits** — *il n'existe aucun
relecteur distinct du rédacteur*. La validation présente est **elle-même une mesure d'agent, non une
relecture par un tiers** : elle ne comble pas cette lacune et ne peut pas la combler.

## 3. Verdict par entrée — synthèse

Trois verdicts, appliqués mécaniquement aux 159 entrées à partir des critères ci-dessus.

| Verdict | Règle | Entrées | Part |
|---|---|---|---|
| **R1 — recevable en appui** | niveau `[A]` ou `[B]` à marquage individuel **et** viabilité V0 ou V1 | **76** | 47,8 % |
| **R2 — recevable sous réserve écrite** | niveau hérité d'une portée, rétrogradé par composition, mixte `[A/B]`, **ou** viabilité V2 | **38** | 23,9 % |
| **R3 — non recevable en appui central** | niveau `[C]` ou `[B/C]`, **ou** viabilité V3 (source changée), **ou** V4 (non établie) | **45** | 28,3 % |

**Ventilation des 45 R3 par motif**, avec recouvrement : 23 par le niveau, 10 par une source changée,
22 par une re-datation non établie ; **dix cumulent deux motifs**.

**Deux croisements méritent l'attention.**

- ⚠ **Vingt-trois entrées R3 sont citées dans le corps d'une pièce** — `S-001`, `S-023`, `S-024`,
  `S-025`, `S-042`, `S-043`, `S-082`, `S-096`, `S-102`, `S-104`, `S-114`, `S-116`, `S-124`, `S-129`,
  `S-135`, `S-142`, `S-143`, `S-144`, `S-149`, `S-152`, `S-153`, `S-154`, `S-157`. Les neuf du § 2.5
  ont été vérifiées et portent leur réserve ; **les quatorze restantes, R3 par viabilité et non par
  niveau, n'ont pas été vérifiées une à une** — *le contrôle reste dû, et il n'est pas revendiqué
  ici.*
- **Quarante-six entrées R1 ne sont jamais citées** sous leur identifiant consolidé. Ce sont les
  meilleures entrées du socle, et le texte ne les atteint que par leur identifiant source. *Le
  déficit n'est pas de qualité, il est de raccordement.*

## 4. Grille des 159 entrées

**Lecture des colonnes.** *Prov.* : volume et identifiant source ; deux identifiants signalent
une entrée fondue. *Niv.* : niveau de l'Annexe B — **⚠p** = niveau hérité d'une phrase de portée,
**⚠c** = rétrogradé par la règle de composition. *Viab.* : **V0** sans objet · **V1** inchangée ·
**V2** inchangée partiellement · **V3** changée · **V4** non établie. *Usage* : « corps » = citée
dans le corps publié · « en-tête » = déclarée mais non citée · « — » = jamais citée sous son
identifiant consolidé. *Cote* : R1 / R2 / R3 (§ 3). *Objet* : libellé de tête de l'énoncé, abrégé.

⚠ **Une ligne de cette grille ne remplace pas son entrée** : l'énoncé complet, sa provenance
détaillée, son degré d'absence et sa re-datation motivée vivent à l'Annexe B — *un abrégé oriente,
il n'atteste pas.*

### Vol. II, *L'autonomie encadrée* — `S-001` à `S-046`

| S | Prov. | Niv. | Viab. | Usage | Cote | Objet |
|---|---|---|---|---|---|---|
| S-001 | II F-01 + III H-09 | A ⚠p | V3 | corps | R3 | MCP |
| S-002 | II F-02 + III H-01 | A ⚠p | V1 | corps | R2 | A2A |
| S-003 | II F-03 | A ⚠p | V2 | corps | R2 | Intégrations infonuagiques d'A2A |
| S-004 | II F-04 | A ⚠p | V2 | corps | R2 | AP2 |
| S-005 | II F-05 + III H-10 | A ⚠p | V2 | en-tête | R2 | AGNTCY |
| S-006 | II F-06 | A ⚠p | V1 | en-tête | R2 | Feuille de route académique |
| S-007 | II F-07 + III H-02 | A ⚠p | V1 | — | R2 | Microsoft Entra Agent ID |
| S-008 | II F-08 + III H-03 | A ⚠p | V1 | en-tête | R2 | Spécification CSA « Agent Registry » |
| S-009 | II F-09 + III H-04 | A/B | V2 | corps | R2 | BSIF, ligne directrice E-23 « Gestion du risque de modélisation (2… |
| S-010 | II F-10 | A ⚠p | V2 | corps | R2 | Rapport conjoint BSIF-ACFC |
| S-011 | II F-11 | A ⚠p | V2 | corps | R2 | Cadre des services bancaires axés sur le consommateur |
| S-012 | II F-15 | A ⚠p | V2 | en-tête | R2 | Microsoft Agent Framework |
| S-013 | II F-16 | A ⚠p | V2 | corps | R2 | Complémentarité MCP/A2A |
| S-014 | II F-17 | A ⚠p | V1 | — | R2 | TD / Layer 6 |
| S-015 | II F-18 | A ⚠p | V2 | — | R2 | TD, gouvernance |
| S-016 | II F-19 | A ⚠p | V4 | — | R3 | RBC, structure et cible |
| S-017 | II F-20 | A ⚠p | V2 | — | R2 | RBC, gouvernance |
| S-018 | II F-21 | A ⚠p | V4 | — | R3 | Scotiabank / AIDox |
| S-019 | II F-22 | A ⚠p | V2 | — | R2 | Manuvie |
| S-020 | II F-23 | A ⚠p | V2 | corps | R2 | Accréditation au cadre bancaire |
| S-021 | II F-23b | A | V4 | — | R3 | Desjardins |
| S-022 | II F-24 | B | V1 | corps | R1 | Post-C-27 |
| S-023 | II F-25 + III H-05 | A ⚠p | V4 | corps | R3 | AMF (Québec), ligne directrice IA |
| S-024 | II F-26 + III H-07 | B | V4 | corps | R3 | ACVM, avis 11-348 |
| S-025 | II F-27 + III H-06 | B | V4 | corps | R3 | Loi 25 (Québec), art. 12.1 |
| S-026 | II F-28 | A | V1 | corps | R1 | Lynx / ISO 20022 |
| S-027 | II F-29 | A | V1 | corps | R1 | Real-Time Rail (RTR) |
| S-028 | II F-30 | B | V1 | — | R1 | CIBC |
| S-029 | II F-31 | B | V4 | — | R3 | Intact |
| S-030 | II F-32 | B | V1 | en-tête | R1 | LangGraph Platform |
| S-031 | II F-33 | B | V3 | en-tête | R3 | Confluent / orchestration événementielle |
| S-032 | II F-34 | A | V2 | corps | R2 | Règlement sur les services bancaires axés sur le consommateur (pré… |
| S-033 | II F-35 + III H-08 | A | V1 | corps | R1 | Standard technique du cadre bancaire : AUCUN désigné officiellemen… |
| S-034 | II F-36 + III H-11 | B | V2 | en-tête | R2 | Manifeste de recherche APM (Agentic Business Process Management) |
| S-035 | II F-37 + III H-12 | B | V1 | en-tête | R1 | Cadre de classification OO1-OO4 et preuves empiriques de l'encadre… |
| S-036 | II F-38 | B ⚠p | V2 | en-tête | R2 | Acquisition webMethods/StreamSets et offre hybride |
| S-037 | II F-39 | B ⚠p | V2 | en-tête | R2 | Cloud Pak for Integration, MQ, App Connect |
| S-038 | II F-40 | B ⚠p | V4 | — | R3 | API Connect 12.1, AI Gateway, famille DataPower |
| S-039 | II F-41 | B ⚠p | V1 | en-tête | R2 | Pivot événementiel : dépréciation d'Event Automation et acquisitio… |
| S-040 | II F-42 | B ⚠p | V2 | en-tête | R2 | watsonx Orchestrate : plan de contrôle agentique |
| S-041 | II F-43 | B ⚠p | V1 | en-tête | R2 | IBM et la généalogie ACP → A2A |
| S-042 | II F-44 + III H-14 | B ⚠p | V4 | corps | R3 | watsonx.governance et observabilité des agents |
| S-043 | II F-45 | B ⚠p | V4 | corps | R3 | Ancrage canadien d'IBM |
| S-044 | II F-46 | B ⚠p | V4 | en-tête | R3 | Architecture de référence agentique d'IBM |
| S-045 | II F-47 | B/C | V2 | — | R3 | BMO |
| S-046 | II F-48 | B/C | V2 | en-tête | R3 | Sun Life / consortium « Agentic Control Plane » |

### Vol. III, *L'entreprise agentique* — `S-047` à `S-142`

| S | Prov. | Niv. | Viab. | Usage | Cote | Objet |
|---|---|---|---|---|---|---|
| S-047 | III F-01 | A | V0 | — | R1 | Format et chaîne de signature |
| S-048 | III F-02 | A | V0 | — | R1 | La charge utile n'est pas transportée |
| S-049 | III F-03 | A | V0 | — | R1 | L'en-tête protégé ne porte aucune validité temporelle |
| S-050 | III F-04 | A | V0 | — | R1 | La signature est facultative, sa vérification seulement recommandé… |
| S-051 | III F-05 | A | V0 | — | R1 | La carte ne porte ni validité ni statut |
| S-052 | III F-06 | A | V0 | — | R1 | Aucun moyen d'établir le statut d'une clé |
| S-053 | III F-07 | A | V0 | — | R1 | L'interdiction sans le moyen de s'y conformer |
| S-054 | III F-08 | A | V0 | — | R1 | Le SECURITY.md du dépôt ne porte aucune disposition de gouvernance… |
| S-055 | III F-09 | B | V0 | — | R1 | L'ancrage est renvoyé hors du protocole |
| S-056 | III F-10 | B | V0 | — | R1 | La rotation est outillée, le retrait ne l'est pas |
| S-057 | III F-11 | B | V0 | — | R1 | Gouvernance de projet sans responsabilité de clés |
| S-058 | III F-12 | B | V1 | corps | R1 | Versions et écart de version non arbitré |
| S-059 | III F-13 | A | V2 | — | R2 | ATLAS, empoisonnement d'outil à la publication |
| S-060 | III F-14 | A | V0 | — | R1 | ATLAS, l'écart d'autorité de la délégation |
| S-061 | III F-15 | A | V0 | — | R1 | ATLAS, plafond de privilège du mandataire |
| S-062 | III F-16 | A | V1 | — | R1 | Le référentiel OWASP et son statut |
| S-063 | III F-17 | A | V0 | — | R1 | Les dix entrées ASI01 à ASI10 |
| S-064 | III F-18 | A | V0 | — | R1 | Un seul intitulé sur dix porte « Identity », aucun ne porte « Dele… |
| S-065 | III F-19 | A | V0 | — | R1 | ASI03, l'identité comme inadéquation architecturale |
| S-066 | III F-20 | A | V1 | — | R1 | L'identité érigée en plan de contrôle |
| S-067 | III F-21 | A | V1 | — | R1 | Incident public daté d'identité non humaine |
| S-068 | III F-22 | A | V0 | — | R1 | La spécification A2A ne nomme aucune menace d'identité classique |
| S-069 | III F-23 | A | V1 | en-tête | R1 | Empoisonnement de mémoire, publication revue par les pairs |
| S-070 | III F-24 | A | V0 | — | R1 | La confusion de délégué est nommée dans la littérature |
| S-071 | III F-25 | A | V0 | — | R1 | Le détournement réussit sur des agents individuellement sains |
| S-072 | III F-26 | B | V2 | en-tête | R2 | Quatre identifiants de vulnérabilité, vote incomplet |
| S-073 | III F-27 | B ⚠c | V0 | — | R2 | L'hypothèse humaine d'OAuth est dans le flux, pas dans les définit… |
| S-074 | III F-28 | B | V0 | — | R1 | La §4 de SCIM Core Schema ne définit aucun type de ressource pour… |
| S-075 | III F-29 | A | V1 | en-tête | R1 | Les jetons de transaction sont pré-normatifs, et datés |
| S-076 | III F-30 | B | V1 | — | R1 | Community Groups, ce qu'ils produisent et ce qu'ils ne produisent… |
| S-077 | III F-31 | C | V3 | — | R3 | Le fossé d'adoption financière n'est pas comblé |
| S-078 | III F-32 | B | V1 | — | R1 | Un précédent institutionnel existe hors du champ agentique |
| S-079 | III F-33 | B | V1 | — | R1 | La GA d'Entra Agent ID est datée d'avril 2026 |
| S-080 | III F-34 | A | V1 | en-tête | R1 | La GA du produit ne vaut pas GA de ses capacités |
| S-081 | III F-35 | A | V0 | — | R1 | Réserve explicite d'absence de couverture entre les deux plans d'i… |
| S-082 | III F-36 | C ⚠c | V3 | corps | R3 | Les pairs infonuagiques, datés et triés |
| S-083 | III F-37 | B | V0 | — | R1 | « Blueprint » est défini, et c'est un objet d'annuaire |
| S-084 | III F-38 | A | V1 | — | R1 | La spécification CSA est un brouillon de labs, et son en-tête le d… |
| S-085 | III F-39 | B | V1 | — | R1 | Le relevé ne soutient pas la mise à jour du 20 mai 2026 annoncée p… |
| S-086 | III F-40 | B | V0 | — | R1 | toolAccessList et permissionBoundaries sont des champs obligatoire… |
| S-087 | III F-41 | B ⚠c | V1 | — | R2 | Le brouillon IETF dont la spécification CSA se réclame est expiré… |
| S-088 | III F-42 | B | V1 | — | R1 | La consolidation IETF a eu lieu, et elle a été renvoyée |
| S-089 | III F-43 | B ⚠c | V1 | — | R2 | A2A normalise la découverte et décline le registre |
| S-090 | III F-44 | A | V1 | corps | R1 | Le transfert d'AP2 est annoncé par une source primaire, et qualifi… |
| S-091 | III F-45 | B | V1 | corps | R1 | Trois mois après, le transfert n'est pas matérialisé |
| S-092 | III F-46 | B | V2 | — | R2 | Les mandats AP2 sont spécifiés et versionnés |
| S-093 | III F-47 | A | V0 | — | R1 | RFC 8693 exprime la délégation et décline la sécurité du jeton |
| S-094 | III F-48 | A | V0 | en-tête | R1 | L'instance qui a compilé le livre blanc décline explicitement la n… |
| S-095 | III F-49 | B | V1 | — | R1 | « Know Your Agent » désigne au moins deux objets distincts |
| S-096 | III F-50 | B | V3 | corps | R3 | Aucune des propositions n'est ratifiée ni adoptée |
| S-097 | III F-51 | B | V0 | en-tête | R1 | Ce que les précédents de fédération portent d'institutionnel |
| S-098 | III F-52 | B ⚠c | V1 | corps | R2 | Deux pages de la spécification MCP ne portent, sous les termes che… |
| S-099 | III F-53 | B ⚠c | V0 | — | R2 | Même le précédent PKI ne garantit pas ce qu'on lui prête |
| S-100 | III F-54 | B | V1 | — | R1 | Le précédent se rétracte |
| S-101 | III F-55 | C | V2 | en-tête | R3 | Les registres agentiques prescrivent des états sans délai de propa… |
| S-102 | III F-56 | C ⚠c | V1 | corps | R3 | Les référentiels sont datés et versionnés |
| S-103 | III F-57 | A | V1 | — | R1 | La défense agentique pose elle-même le problème d'identité du volu… |
| S-104 | III F-58 | B | V4 | corps | R3 | Trois offres de sécurité relevées chez trois éditeurs, à trois dat… |
| S-105 | III F-59 | B | V1 | en-tête | R1 | NIST IR 8547 demeure un Initial Public Draft |
| S-106 | III F-60 | B | V1 | en-tête | R1 | Les jalons, leur libellé exact, et le sens du 2035 |
| S-107 | III F-61 | B ⚠c | V1 | — | R2 | Une obligation fédérale datée s'ancre sur un projet |
| S-108 | III F-62 | B | V1 | — | R1 | L'écart de statut est net, et il est le cœur de l'horloge |
| S-109 | III F-63 | B | V1 | corps | R1 | Le rapport européen n'énonce aucune échéance calendaire |
| S-110 | III F-64 | B | V2 | en-tête | R2 | Les douze énoncés numérotés d'E-23 sont au should |
| S-111 | III F-65 | B ⚠c | V0 | en-tête | R2 | Ce qu'E-23 énonce que l'institution devrait (« should ») faire |
| S-112 | III F-66 | B | V1 | en-tête | R1 | La « période de transition » n'est pas dans la ligne directrice |
| S-113 | III F-67 | B | V4 | en-tête | R3 | La divergence de date de l'AMF n'est tranchée par aucune source pr… |
| S-114 | III F-68 | B | V4 | corps | R3 | Ce que l'AMF attend, et sur quelle définition |
| S-115 | III F-69 | A | V1 | corps | R1 | La question reste ouverte, et le texte officiel l'écrit au futur |
| S-116 | III F-70 | B | V3 | corps | R3 | Le tri annonce / GA / production, appliqué offre par offre |
| S-117 | III F-71 | B | V0 | — | R1 | L'autorisation par arête existe, spécifiée |
| S-118 | III F-72 | B | V0 | — | R1 | « Agent mesh » désigne deux objets distincts chez deux fournisseur… |
| S-119 | III F-73 | B | V1 | — | R1 | Le socle zero trust est ancien et le volet agentique est un projet |
| S-120 | III F-74 | B | V1 | en-tête | R1 | Le déplacement est daté, et c'est une rupture déclarée |
| S-121 | III F-75 | B | V1 | — | R1 | Le dépôt dédié ne porte, à cette date, aucun numéro de version qui… |
| S-122 | III F-76 | B | V0 | — | R1 | L'échelle de maturité des groupes de conventions sémantiques compt… |
| S-123 | III F-77 | B | V1 | en-tête | R1 | Le statut relevé des documents agentiques est le premier échelon |
| S-124 | III F-78 | B | V3 | corps | R3 | Une conformité annoncée peut pointer un millésime périmé |
| S-125 | III F-79 | B | V1 | en-tête | R1 | Le modèle de données des accréditations vérifiables v2.0 est une R… |
| S-126 | III F-80 | B | V1 | en-tête | R1 | La v2.1 est un brouillon de travail, et le document le dit de lui-… |
| S-127 | III F-81 | B | V2 | — | R2 | DID Core v1.0 est une Recommandation, et sa page signale des errat… |
| S-128 | III F-82 | A | V1 | en-tête | R1 | DID v1.1 n'a pas dépassé le Candidate Recommendation Snapshot, et… |
| S-129 | III F-83 | B | V3 | corps | R3 | Un Community Group du W3C, sa mission et son décompte affiché — av… |
| S-130 | III F-84 | B | V0 | — | R1 | Le mode d'octroi par justificatifs de client existe, et c'est le p… |
| S-131 | III F-85 | B | V1 | en-tête | R1 | Les sept Internet-Drafts du groupe WIMSE, datés, et aucun publié e… |
| S-132 | III F-86 | B | V1 | — | R1 | Ce que WIMSE énonce des intermédiaires d'IA, et à quel titre |
| S-133 | III F-87 | B | V0 | — | R1 | SPIFFE-ID |
| S-134 | III F-88 | B | V1 | corps | R1 | La maturité CNCF de SPIFFE et de SPIRE, et la divergence d'un jour… |
| S-135 | III F-89 | B | V4 | corps | R3 | L'article 12.1 de la Loi 25 : trois informations sur demande, plus… |
| S-136 | III F-90 | B | V1 | en-tête | R1 | Douze métriques définies, toutes des histogrammes, toutes au premi… |
| S-137 | III F-91 | B | V1 | en-tête | R1 | Quatre des douze portent sur l'agent ou le flux de travail, huit n… |
| S-138 | III F-93 | B | V2 | en-tête | R2 | Aucune dimension d'identité, de mandat, de conversation ni de révo… |
| S-139 | III F-94 | B | V1 | en-tête | R1 | Les dimensions qui permettraient d'agréger un parc sont facultativ… |
| S-140 | III F-95 | B | V2 | corps | R2 | Quatre métriques MCP de plus, toutes des histogrammes, et le volet… |
| S-141 | III F-97 | B | V1 | en-tête | R1 | Onze évaluateurs d'agents chez un éditeur, dont cinq en préversion… |
| S-142 | III F-98 | B | V3 | corps | R3 | Trois sources ouvertes, trois grains d'indicateur, aucun identifia… |

### Vol. I, *Interopérabilité agentique* — `S-143` à `S-159`

| S | Prov. | Niv. | Viab. | Usage | Cote | Objet |
|---|---|---|---|---|---|---|
| S-143 | III H-17 | C | V2 | corps | R3 | L'horloge post-quantique |
| S-144 | III H-18 | C | V3 | corps | R3 | Les jalons de normalisation 2027-2028 |
| S-145 | III H-19 | C | V1 | en-tête | R3 | KYA et la trust fabric |
| S-146 | III H-20 | C | V1 | en-tête | R3 | Les Community Groups agentiques du W3C |
| S-147 | III H-21 | C | V4 | en-tête | R3 | Le SOC agentique |
| S-148 | III H-22 | C | V1 | en-tête | R3 | Les référentiels de sécurité agentique en mouvement |
| S-149 | III H-23 | C | V1 | corps | R3 | La science de l'évaluation |
| S-150 | III H-24 | C | V0 | en-tête | R3 | La non-compositionnalité de la sûreté |
| S-151 | III H-25 | C | V1 | en-tête | R3 | Le rug-pull et l'intégrité continue |
| S-152 | III H-26 | C | V1 | corps | R3 | Injection et empoisonnement |
| S-153 | III H-27 | C | V4 | corps | R3 | L'invariant à quatre termes |
| S-154 | III H-28 | C | V4 | corps | R3 | La délégation au-delà de deux sauts |
| S-155 | III H-29 | C | V4 | — | R3 | Le verrou d'origine |
| S-156 | III H-30 | C | V4 | en-tête | R3 | Le plan de contrôle obligatoire |
| S-157 | III H-31 | C | V4 | corps | R3 | L'autonomie graduée |
| S-158 | III H-32 | C | V4 | — | R3 | Le cas fil rouge |
| S-159 | III H-33 | C | V0 | en-tête | R3 | Le tri prospectif, siège de la discipline |
