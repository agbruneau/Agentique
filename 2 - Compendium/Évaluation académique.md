# Évaluation académique universitaire — *Compendium : Ingénierie des systèmes agentiques d'entreprise* (Volume IV)

**Titre de l'œuvre évaluée** : *Compendium — Ingénierie des systèmes agentiques d'entreprise : protocoles, identité, gouvernance et architecture de référence* (Volume IV du corpus *Agentique*, [`2 - Compendium/`](.))
**Date de l'évaluation** : 14 octobre 2026
**Évaluateur** : Comité d'audit académique et d'ingénierie logicielle (évaluation contradictoire outillée)
**Périmètre audité** : Dépôt `agbruneau/Agentique`, sous-arbre [`2 - Compendium/`](.), étiquette `corpus-v1.0`, commit `8b2cf08dcca6f0adf3dd7fb6c76664407b9ea2c9` (16 septembre 2026, clôture en l'état par décision `D-19`) — 50 chapitres en 5 livres (`333 416` mots de corps), 2 annexes (`annexe-bibliographie.md`, `annexe-references.md`), 8 pièces de gouvernance (`PRD/*.md`), 9 scripts de vérification et de décompte (`PRD/*.py`, `PRD/*.sh`), 8 scripts et gabarits de fabrication (`build/*`), programme de 118 figures vectorielles (`figures/*`), 50 rendus `.html` autonomes et l'ouvrage paginé [`Compendium.pdf`](Compendium.pdf) (`1 000` pages, `13 022 826` octets)
**Niveau de référence retenu** : **Doctorat / ouvrage de référence scientifique et professionnel** (conformément au [`Gabarit d'évaluation académique.md`](../Gabarit%20d'évaluation%20académique.md) v1.0, § 0.3)
**Couverture effective** : **100 % des 50 chapitres, des 2 annexes, des 8 pièces de gouvernance et des scripts lus intégralement (`[L]`)** ; **100 % des 14 commandes de la chaîne de vérification et de mutation exécutées (`[R]`)** ; **16 familles de sources primaires externes confrontées en direct au 14 octobre 2026 (`[S]`)**
**Document technique compagnon** : [`audit.md`](audit.md) (registre exhaustif des 41 constats d'audit `A-B1`..`A-B7`, `A-M1`..`A-M12`, `A-m1`..`A-m14`, `A-D1`..`A-D8`)

> **Marqueurs épistémiques employés dans la présente évaluation** :
> - **`[L]`** (*Lu intégralement*) : pièce lue de la première à la dernière ligne par l'évaluateur.
> - **`[E]`** (*Échantillonné*) : pièce inspectée par sondage ciblé (`0 %` dans le présent audit, l'intégralité du corpus ayant été lue en `[L]`).
> - **`[R]`** (*Rejoué / exécuté*) : script, test de mutation, décompte ou contrôle de fabrication exécuté directement par l'évaluateur avec capture du code de sortie.
> - **`[S]`** (*Source externe confrontée*) : affirmation vérifiée par confrontation directe à la source primaire externe (IETF Datatracker, W3C, NIST, Paiements Canada, BSIF, AMF, ACVM, dépôts MCP / A2A / OpenTelemetry, arXiv) à la date du **14 octobre 2026**.
> - **`[D]`** (*Déclaré par l'auteur, non vérifié indépendamment*) : élément relevant d'un processus externe au dépôt (ex. absence de relecture humaine tierce sur `CA-IV-11` et `CA-IV-12`).

---

## 1. Résumé exécutif et verdict académique

### 1.1 Synthèse en dix lignes

Le *Compendium* (Volume IV du corpus *Agentique*) est une somme architecturale, protocolaire et réglementaire de **333 416 mots de corps** répartis en **50 chapitres et 5 livres** (`[L]`, `[R]`), composée en **1 000 pages** ([`Compendium.pdf`](Compendium.pdf)) et accompagnée d'un programme original de **118 figures vectorielles SVG** (`[R]`). Son objet est de fusionner en une architecture de référence cohérente les trois premiers volumes du corpus — l'encyclopédie protocolaire du Volume I (`MCP`, `A2A`, `AP2`), la monographie par élimination du Volume II (orchestration `OO1`–`OO4`, réglementation financière canadienne, rails `Lynx`/`RTR`) et l'étude du Volume III (identité agentique, sécurité, post-quantique, `AgentOps`) — sous la **loi du maillon le plus faible des régimes de preuve (`[A]`, `[B]`, `[C]`)** (`[L]`). Ses contributions intellectuelles les plus remarquables résident dans ses grilles analytiques propres (les cinq questions d'identité du ch. 14, le passeport à quatre pièces du ch. 16, le test des frames déterministes du ch. 29, le renversement de la matrice protocoles × exigences canadiennes du ch. 42, les cinq points de contrôle `PC1`–`PC5` et la désambiguïsation des trois échelles d'autonomie du ch. 43) ainsi que dans son outillage d'auto-vérification par tests de mutation (`178` mutations sur 4 harnais) (`[L]`, `[R]`). En contrepartie, l'audit au **14 octobre 2026** met en évidence : (1) l'échec à l'exécution (`code 1`) de [`build/verifier-piece.py`](build/verifier-piece.py) sur 2 fichiers HTML et de [`PRD/decompte.sh --verifier`](PRD/decompte.sh) sans `LC_ALL=C` (`[R]`) ; (2) cinq contradictions internes majeures introduites au Livre II par la passe `D-11` du 30 juillet 2026 et deux divergences texte ↔ figures SVG au Livre V (`[L]`) ; (3) l'expiration au **2 octobre 2026** de la fenêtre de 30 jours de `CA-IV-04`, l'entrée effective dans le **`T4 2026`** du rail `RTR` le 1er octobre 2026 (avec une contradiction non purgée au ch. 36 l. 305), et une faille méthodologique de [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md) qui a interrogé des URL d'archives IETF immuables (`-00.txt`) et manqué l'adoption par le groupe de travail IETF WIMSE du brouillon `draft-klrc-aiagent-auth` devenu **`draft-ietf-wimse-aims-00`** le 15 septembre 2026 (`[S]`) ; et (4) le maintien en l'état, sous les décisions `D-16` et `D-19`, de chapitres rédigés sans socle primaire (ch. 41, 44, 47, 48) (`[L]`). Pris selon son statut déclaré d'*archive de recherche et d'architecture (`D-18`)*, l'ouvrage atteint la note globale pondérée de **`16,00 / 20` (`A-`, mention *Très Bien*)** et appelle des révisions ciblées de cohérence interne et de synchronisation calendaire ; toute levée ultérieure de `D-18` en vue d'une publication normative externe exigerait en revanche le franchissement préalable des portes `G-4`, `G-5`, `G-6` et `G-7`.

### 1.2 Tableau de notation pondéré

| Code | Dimension évaluée | Poids | Note / 20 | Score pondéré | Justification synthétique (avec marqueurs) |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **`D1`** | **Rigueur scientifique et exactitude factuelle** | **20 %** | **14,5 / 20** | **2,90** | Analyses protocolaires et réglementaires très sûres sur les chapitres adossés à `[A]` (`[L]`), mais pénalisées par 5 contradictions internes non purgées au Livre II (`A-B6`), 2 divergences texte ↔ SVG au Livre V (`A-B7`), 1 contradiction ch. 33/36 sur le 24 août 2026 (`A-B5`) et 2 contradictions corps/note aux ch. 37 et 39 (`A-M10`) (`[L]`). |
| **`D2`** | **Qualité, fraîcheur et traçabilité du sourçage primaire** | **15 %** | **14,0 / 20** | **2,10** | Socle consolidé remarquable (`159` entrées `S-nnn`, `1 154` réf. au Vol. I) (`[L]`), mais non-réadossement des chapitres aux `S-nnn` (`CA-IV-01`, `524` emplois nus `P3`), chapitres 41/44/47/48 sans socle primaire (`G-6`, `R-IV-102`), expiration de `CA-IV-04` au 2 oct. 2026 (`A-B3`) et faux négatifs IETF WIMSE causés par la vérification d'URL d'archives `-00.txt` (`A-B4`) (`[L]`, `[S]`). |
| **`D3`** | **Cohérence architecturale et consistance inter-modules** | **15 %** | **15,5 / 20** | **2,325** | Discipline exemplaire des **26 sièges de non-redondance** (`check-sieges.py` : `0` écart sur `S1`–`S5`, `115` mutations) et parité des 56 thèses (`[R]`), tempérées par l'absence de la couche d'exécution dans le Livre IV (`G-5`/`D-2`), 4 entrées désynchronisées dans `annexe-references.md` (`A-M6`) et le double `%` dans l'en-tête inférieur de 45 chapitres (`A-M1`) (`[L]`). |
| **`D4`** | **Originalité de la thèse et valeur ajoutée analytique** | **15 %** | **17,5 / 20** | **2,625** | Apports conceptuels originaux de premier plan : loi d'hérédité épistémique `[A]`/`[B]`/`[C]`, grille des 5 questions (ch. 14), passeport à 4 pièces (ch. 16), test à 3 conditions des frames déterministes (ch. 29), renversement protocoles × exigences canadiennes et 5 zones de compensation (ch. 42), 5 points de contrôle `PC1`–`PC5` et 3 échelles d'autonomie (ch. 43) (`[L]`). |
| **`D5`** | **Opérationnalisation, reproductibilité et outillage** | **15 %** | **17,0 / 20** | **2,55** | Ingénierie documentaire rare en sciences appliquées : 4 harnais de mutation (`178` mutations), générateur vectoriel autonome de 115 figures SVG (`dessine.py`), chaîne Typst de 1 000 pages (`[L]`, `[R]`). Pénalisée de 3 points par les 2 échecs `[R]` (`verifier-piece.py` code 1 sur 2 fichiers HTML `A-B1` ; `decompte.sh --verifier` code 1 sans `LC_ALL=C` `A-B2`) et le bogue `P3` (`A-M3`). |
| **`D6`** | **Qualité rédactionnelle, pédagogique et typographique** | **10 %** | **16,0 / 20** | **1,60** | Prose française d'une haute tenue analytique, composition Typst soignée (`Compendium.pdf`, `degagement +21.5 pt`) et 118 figures lisibles (`[L]`, `[R]`), mais alourdie dans les Livres III et IV par les périphrases d'anonymisation survivantes de la décision 15 (`A-m4`) et par la place disproportionnée du métadiscours de gouvernance dans les chapitres sans socle (`[L]`). |
| **`D7`** | **Lucidité épistémique, gouvernance des limites et réflexivité** | **10 %** | **19,0 / 20** | **1,90** | Niveau d'honnêteté intellectuelle exceptionnel : chaque inférence propre est marquée `Lecture de l'auteur` (`596` occ. au corps), chaque dette documentaire est enregistrée (`106` remontées `R-IV-*`), le chapitre 49 dresse la frontière du vérifiable et le chapitre 50 codifie la propre péremption de l'ouvrage (`[L]`, `[R]`). |
| **TOTAL** | **Moyenne générale pondérée** | **100 %** | **`16,00 / 20`** | **`16,00 / 20`** (`80,0 %`) | **Équivalence : `A-` — Mention *Très Bien* (statut d'archive `D-18` / `D-19`)** |

### 1.3 Verdict académique formel

- [ ] **Acceptation en l'état (Excellence)**
- [x] **Acceptation avec révisions mineures à modérées** *(au titre de son statut explicite d'archive de recherche et d'architecture non destinée à la publication externe sous les décisions `D-18` et `D-19`)*
- [ ] **Révisions majeures requises (Resoumission)** *(verdict qui s'appliquerait de plein droit si la décision `D-18` devait être levée en vue d'une publication éditoriale ou normative externe avant le franchissement des portes `G-4`, `G-5`, `G-6` et `G-7`)*
- [ ] **Rejet / Refonte structurelle complète**

**Motivation du verdict** : Évalué conformément à sa nature déclarée d'*archive de recherche et d'architecture (`corpus-v1.0`, décisions `D-18` et `D-19`)*, le *Compendium* constitue une réalisation scientifique et d'ingénierie documentaire de premier ordre (`16,00 / 20`), dont la réflexivité méthodologique (`D7 = 19,0 / 20`), l'originalité analytique (`D4 = 17,5 / 20`) et l'outillage de vérification par mutation (`D5 = 17,0 / 20`) dépassent largement les standards habituels des monographies d'architecture logicielle (`[L]`, `[R]`). Pour que cette archive soit pleinement intègre au **14 octobre 2026**, il est toutefois indispensable de corriger les **7 constats bloquants (`A-B1` à `A-B7`)** et les **12 constats majeurs (`A-M1` à `A-M12`)** identifiés par l'audit — corrections qui représentent environ **3 jours d'ingénierie ciblée** (Phases 1 à 3 de la feuille de route § 10). En revanche, l'ouvrage démontre lui-même avec une franchise exemplaire pourquoi il ne peut pas être publié tel quel comme traité normatif externe sans exécuter la Phase 4 (clôture des lots de matière neuve des ch. 41, 47 et 48, vérification d'ArchiMate 4 `doc C260` pour les ch. 44–45, instruction du lot `D-9` sur le biais d'automatisation et ré-adossement intégral aux `S-nnn`).

---

## 2. Protocole méthodologique et périmètre d'audit

### 2.1 Cartographie quantitative du corpus (`[L]`, `[R]`)

| Sous-ensemble / Module | Fichiers `.md` / `.py` / `.typ` | Lignes de source | Mots de corps (`decompte.sh`) | Cible (`TOC.md`) | Écart | Tableaux / Figures SVG | Statut de lecture |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Livre I — *Fondations protocolaires et d'intégration*** (`ch. 1`–`11` + `README.md`) | 12 `.md` | `9 294` | `73 255` | `76 500` | `−4,2 %` | 35 tab. / 28 fig. (`25+3`) | **100 % `[L]`** |
| **Livre II — *Identité, sécurité et confiance*** (`ch. 12`–`21` + `README.md`) | 11 `.md` | `7 666` | `69 390` | `57 100` | `+21,5 %` | 27 tab. / 22 fig. | **100 % `[L]`** |
| **Livre III — *Orchestration, gouvernance et conformité*** (`ch. 22`–`36` + `README.md`) | 16 `.md` | `11 937` | `103 200` | `110 000` | `−6,2 %` | 35 tab. / 35 fig. | **100 % `[L]`** |
| **Livre IV — *Architecture de référence et exploitation*** (`ch. 37`–`46` + `README.md`) | 11 `.md` | `7 205` | `60 723` | `70 500` | `−13,9 %` | 19 tab. / 24 fig. | **100 % `[L]`** |
| **Livre V — *Prospective, limites et péremption*** (`ch. 47`–`50` + `README.md`) | 5 `.md` | `2 797` | `26 848` | `30 400` | `−11,7 %` | 8 tab. / 10 fig. | **100 % `[L]`** |
| **Gouvernance (`PRD/`), Accueil (`README.md`, `JOURNAL.md`) & Annexes (`annexe-*.md`)** | 12 `.md` + 9 scripts | `6 742` (`.md`) + `2 518` (scripts) | Hors corps (`1 154` réf. Vol. I ; `159` `S-nnn`) | — | — | 2 annexes | **100 % `[L]` & `[R]`** |
| **Fabrication (`build/`) & Programme de figures (`figures/`)** | 8 (`build/`) + 8 (`figures/`) + 118 `.svg` + 50 `.html` + 1 `.pdf` | `1 412` (`build/`) + `4 190` (`figures/`) | `Compendium.pdf` : **1 000 pages** (`13 022 826` octets) | `1 000` p. | `0 %` | 118 fichiers `.svg` | **100 % `[L]` & `[R]`** |
| **TOTAL CORPUS (`2 - Compendium/`)** | **62 `.md`, 22 scripts/gabarits, 118 `.svg`, 50 `.html`, 1 `.pdf`** | **`53 761` lignes (`.md` + code)** | **`333 416` mots de corps** | **`344 500`** | **`−3,2 %`** | **124 tab. / 118 fig. SVG** | **100 % `[L]` & `[R]`** |

### 2.2 Régime de vérification appliqué (`[L]`, `[R]`, `[S]`, `[D]`)

1. **Lecture intégrale (`[L] = 100 %`, `[E] = 0 %`)** : Les 50 chapitres (`ch. 1` à `ch. 50`), les 6 fichiers `README.md`, `JOURNAL.md`, les 2 annexes (`annexe-bibliographie.md`, `annexe-references.md`), les 8 documents du dossier `PRD/` (`PRD.md`, `TOC.md`, `socle-consolide.md`, `registre-gel.md`, `gel-2026-07-27.md`, `gel-2026-07-28-volet-residuel.md`, `revalidation-2026-09-02.md`, `README.md`), les gabarits Typst/HTML (`build/*.template`) et les scripts Python/Bash (`PRD/*`, `build/*`, `figures/*`) ont été lus intégralement sans recourir à l'échantillonnage (`[L]`).
2. **Exécution directe de la chaîne d'outillage (`[R] = 14 commandes`)** : Toutes les commandes de vérification, de mutation, de décompte et de contrôle typographique ont été exécutées dans l'environnement du dépôt le 14 octobre 2026 (voir le journal complet en **Annexe A**).
3. **Confrontation externe aux sources primaires au 14 octobre 2026 (`[S]`)** : Les affirmations à haute sensibilité temporelle (brouillons IETF OAuth / WIMSE / AI Agent Auth, recommandations W3C DID 1.1 / VC 2.0 / RDF 1.2, standards NIST FIPS 203–205 et `NIST IR 8547`, échéances réglementaires canadiennes BSIF E-23, AMF LD IA, Loi 25, ACVM 11-348, Paiements Canada *By-law no 10* / RTR `T4 2026`, Cadre bancaire C-15, spécifications MCP, A2A, OpenTelemetry GenAI, OWASP Agentic Top 10 et préimpressions arXiv) ont été confrontées aux sources officielles en ligne le 14 octobre 2026 (voir **§ 6** et **Annexe B**).
4. **Périmètre déclaré non vérifiable par voie d'outillage (`[D]`)** : Seuls les processus humains externes au dépôt — tels que l'absence de relecture par un second expert en sécurité opérationnelle (`CA-IV-11`) ou par un architecte externe à la rédaction (`CA-IV-12`) — relèvent du marqueur `[D]`.

### 2.3 Biais et limites de l'évaluation

L'évaluation est conduite à la date précise du **14 octobre 2026**, soit quatre semaines après la clôture du dépôt (`16 septembre 2026`). Afin d'éviter tout biais d'anachronisme, le présent rapport distingue rigoureusement :
- d'une part, les **défauts intrinsèques à l'archive du 16 septembre 2026** (scripts en échec `A-B1`/`A-B2`, contradictions internes `A-B6` du 30 juillet 2026, divergences texte ↔ SVG `A-B7` du 15 septembre 2026, et faux négatifs méthodologiques du 2 septembre 2026 sur `draft-klrc-aiagent-auth` déjà en `-03` depuis juillet 2026 et devenu `draft-ietf-wimse-aims-00` le 15 septembre 2026 avant la clôture `D-19`) ;
- d'autre part, la **péremption calendaire survenue entre le 16 septembre et le 14 octobre 2026** (expiration de la fenêtre de 30 jours de `CA-IV-04` le 2 octobre 2026 et entrée dans le `T4 2026` du RTR le 1er octobre 2026).

---

## 3. Évaluation de la thèse directrice et de l'architecture d'ensemble

### 3.1 Formulation et soutenabilité de la thèse centrale (`[L]`)

Plutôt que d'énoncer une thèse unique monolithique, le *Compendium* articule une **méta-thèse architecturale et épistémique** distribuée en **56 thèses de chapitres et de mouvements** (50 chapitres dont 6 à deux mouvements : ch. 12, 20, 21, 22, 37, 45, 47, 49) collationnées dans [`PRD/TOC.md`](PRD/TOC.md) (v0.36) (`[L]`, `[R]`). Cette méta-thèse peut se formuler en deux propositions indissociables :

1. **Proposition substantielle (ingénierie et gouvernance des systèmes agentiques)** : *Les standards d'intégration et de sécurité hérités du Web et de l'entreprise (OAuth 2.0/2.1, OIDC, SPIFFE/SPIRE, SCIM, W3C DID/VC, OpenTelemetry, ISO 20022) ainsi que les nouveaux protocoles agentiques (`MCP` pour l'outillage vertical, `A2A` pour la délégation horizontale, `AP2` pour le mandat de paiement) laissent un vide structurel — identitaire, sémantique, transactionnel et prudentiel — dès qu'un agent probabiliste agit par délégation sur des systèmes à effet irréversible ; en contexte financier réglementé (BSIF E-23, AMF, Loi 25, ACVM 11-348), ce vide ne peut être comblé ni par les protocoles seuls ni par l'instrumentation post-hoc, mais exige une architecture de compensation à points de contrôle déterministes (`PC1`–`PC5`), des frames de traduction explicites et un passeport d'identité vérifiable.*
2. **Proposition méthodologique (loi du maillon le plus faible épistémique)** : *Lorsqu'une somme d'architecture fusionne des corpus de régimes probatoires hétérogènes — sources primaires vérifiées (`[A]`), sources secondaires concordantes (`[B]`) et reprises internes non ré-extraites (`[C]`) —, aucune synthèse ne peut prétendre à un degré de certitude supérieur au plus faible de ses composants, et toute inférence de l'architecte doit être isolée sous le marqueur explicite `Lecture de l'auteur`.*

Cette double thèse est **remarquablement soutenable, féconde et non triviale** (`[L]`). Elle prend à revers aussi bien l'enthousiasme techno-solutionniste des livres blancs d'éditeurs que les approches purement juridiques qui ignorent la mécanique protocolaire (JSON-RPC 2.0, jetons porteurs, files d'événements, sagas de compensation).

### 3.2 Architecture modulaire et progression logique (`[L]`, `[R]`)

La progression en **cinq livres** suit une chaîne causale rigoureuse :
- **Livre I (ch. 1–11)** : *Ce que les protocoles d'intégration et d'agentique (`MCP`, `A2A`, `AP2`, `AGNTCY`) font et où ils échouent.*
- **Livre II (ch. 12–21)** : *Qui agit, au nom de qui, sous quelle délégation, face à quelles attaques et sous quelle horloge cryptographique post-quantique.*
- **Livre III (ch. 22–36)** : *Comment orchestrer ces agents (`OO1`–`OO4`, `APM`) et les soumettre au maillage réglementaire et financier canadien (E-23, Loi 25, AMF, ACVM, C-15, Lynx/RTR).*
- **Livre IV (ch. 37–46)** : *Comment opérer le maillage en production (PEP/PDP, OTel GenAI, AgentOps/FinOps, fabrique) et composer l'architecture de référence en 6 couches, son métamodèle ArchiMate et sa feuille de route vers le 1er mai 2027.*
- **Livre V (ch. 47–50)** : *Ce qui manque encore au socle (artefact livré, sémantique d'effet et compensation), où s'arrête la connaissance vérifiable à l'horizon 2027–2032, et comment l'ouvrage gère sa propre péremption.*

L'articulation inter-modules est gouvernée par un mécanisme original de **26 sièges de non-redondance** ([`PRD/check-sieges.py`](PRD/check-sieges.py)) : chaque concept transversal (ex. les quatre états d'une tâche A2A au `ch. 7 § 7.5`, la grille des cinq questions au `ch. 14 § 14.1`, les options `OO1`–`OO4` au `ch. 22 § 22.1`, les six durcisseurs financiers au `ch. 31`) possède un unique **siège d'exposition** marqué par `<!-- SIÈGE : ... -->`, et tout autre chapitre qui mobilise ce concept est contraint par test automatique (`S1` à `S5`, éprouvés par `115` mutations) d'y renvoyer sans le ré-exposer (`[R]`). La seule réserve architecturale d'ensemble tient à la décision tardive `D-2` (porte `G-5`), qui a logé la **couche d'exécution (harnais d'agent)** en « cinquième horloge » au Livre V (`ch. 47 § 47.8.1`) après la rédaction du Livre IV, laissant l'architecture en 6 couches du chapitre 43 dépourvue de couche ou de point de contrôle dédié au harnais d'exécution (`[L]`).

### 3.3 Positionnement dans la littérature et l'état de l'art (`[L]`, `[S]`)

Dans le paysage scientifique et industriel d'octobre 2026, les travaux existants se divisent en trois silos : (1) les spécifications protocolaires et brouillons de groupes de travail (Anthropic/Linux Foundation pour `MCP`, Google/Linux Foundation pour `A2A` et `AP2`, IETF `WIMSE` et `OAuth`, W3C `DID`/`VC`), (2) les préimpressions académiques de sécurité et d'évaluation agentique (ex. *Promptware Kill Chain*, *MAST*, *EchoLeak*, *AgentBound*, taxonomie d'observabilité), et (3) les lignes directrices prudentielles et textes législatifs (BSIF E-23, AMF, Loi 25, AI Act européen, NIST AI RMF). Le *Compendium* occupe une position **sans équivalent direct en langue française ou anglaise** en opérant la jointure formelle, ligne à ligne et exigence par exigence, entre ces trois silos sur un vertical bancaire et assurantiel complet (`[L]`, `[S]`).

---

## 4. Évaluation analytique par sous-ensemble (`[L]`, `[R]`, `[S]`)

### 4.1 Fiche 1 — Livre I : *Fondations protocolaires et d'intégration* (Chapitres 1 à 11)

- **Identifiant et intitulé** : [`Livre I/`](Livre%20I/) — Chapitres [`01`](Livre%20I\01-interoperabilite-integration-entreprise.md) à [`11`](Livre%20I\11-modes-echec-risques-protocolaires.md) et [`Livre I/README.md`](Livre%20I/README.md).
- **Volume et statut de vérification** : `12` fichiers `.md`, `9 294` lignes, **`73 255` mots de corps** (cible `76 500`, écart `−4,2 %`), `35` tableaux, `28` figures SVG (`25` gravées + `3` antérieures au ch. 8) — **100 % `[L]`**, scripts **`[R]`**, sources normatives **`[S]`**.
- **Note du sous-ensemble** : **`16,8 / 20`**.
- **Thèse et rôle dans l'ensemble** : Établir la généalogie technique des systèmes agentiques depuis l'intégration d'entreprise classique (ESB/SOA, Web sémantique RDF 1.2 / SHACL 1.2 / SPARQL 1.2, HTTP/2–3, gRPC, OAuth 2.1, EDA/Kafka/AsyncAPI, ingénierie du contexte) jusqu'à l'anatomie comparée de `MCP` (`2025-11-25`) et d'`A2A` (`v0.3.0`), l'orchestration multi-agents, les protocoles émergents (`AGNTCY`, `AP2`, `ANP`, `ACP`, `LMOS`) et la chaîne d'attaque protocolaire (*Promptware Kill Chain*, *EchoLeak* `CVE-2025-32711`).
- **Analyse de la qualité scientifique et technique** :
  - *Forces* : Les chapitres 3, 6, 7, 8 et 11 constituent le noyau technique le plus solide du *Compendium* (`[L]`). L'analyse comparative sur **11 dimensions** entre `MCP` et `A2A` au [`chapitre 8`](Livre%20I\08-anatomie-mcp-a2a.md) (avec la mise en évidence des 6 zones grises où la formule *« MCP dans les agents, A2A entre les agents »* se brouille en production) et la décomposition au [`chapitre 11`](Livre%20I\11-modes-echec-risques-protocolaires.md) de la *Promptware Kill Chain* en 7 étapes face à `CVE-2025-32711` (*EchoLeak*, CVSS 9.3) sont d'une précision irréprochable.
  - *Faiblesses et anomalies* : (1) En raison de la décision de gouvernance de ne pas ré-extraire les 1 154 références du Volume I, une part importante des chapitres 1, 2, 4, 5 et 9 demeure sous le régime **`[C]`** (reprise interne du Vol. I) (`[L]`) ; (2) au [`ch. 8` (l. 15)](Livre%20I\08-anatomie-mcp-a2a.md), la thèse en exergue a été anonymisée (*« dans les agents, entre les agents — doctrine [...] déclarée par l'un des deux projets »*) alors que `§ 8.8` (l. 882) affirme la citer *« telle quelle »* depuis `TOC.md` (`A-M8`) ; (3) au [`ch. 3 § 3.2.1` (l. 101)](Livre%20I\03-securite-identite-gouvernance.md), le corps cite toujours `draft-ietf-oauth-v2-1-15` (expiré le 3 septembre 2026) sans nommer **`draft-ietf-oauth-v2-1-16`** publié le 2 septembre 2026 (`A-B4`, `[S]`).
- **Recommandations spécifiques** : Rétablir la thèse verbatim de `TOC.md` en tête du ch. 8 (`A-M8`) ; mettre à jour `draft-ietf-oauth-v2-1-16` au ch. 3 (`A-B4`) ; corriger l'en-tête inférieur des ch. 1–11 (`A-M1`) et la ligne `Garde-fous balayés` des ch. 8–11 (`A-M2`).

---

### 4.2 Fiche 2 — Livre II : *Identité, sécurité et confiance* (Chapitres 12 à 21)

- **Identifiant et intitulé** : [`Livre II/`](Livre%20II/) — Chapitres [`12`](Livre%20II\12-heritage-standards-etires.md) à [`21`](Livre%20II\21-horloge-post-quantique.md) et [`Livre II/README.md`](Livre%20II/README.md).
- **Volume et statut de vérification** : `11` fichiers `.md`, `7 666` lignes, **`69 390` mots de corps** (cible `57 100`, écart **`+21,5 %`**), `27` tableaux, `22` figures SVG — **100 % `[L]`**, scripts **`[R]`**, sources IETF / W3C / NIST **`[S]`**.
- **Note du sous-ensemble** : **`15,2 / 20`**.
- **Thèse et rôle dans l'ensemble** : Démontrer pourquoi les six standards d'identité hérités (OAuth 2.0 `RFC 6749`, OIDC, Token Exchange `RFC 8693`, RAR `RFC 9396`, SPIFFE/SPIRE, SCIM `RFC 7643/7644`) et le couple W3C `DID v1.1` / `VC 2.0` répondent à l'authentification et au transport mais laissent ouvertes les questions de **portée du mandat**, de **chaîne de responsabilité** et d'**arrêt d'urgence** (`ch. 14` à `17`), recenser les 9 chantiers de normalisation (`ch. 18`), cartographier la surface d'attaque agentique (`ch. 19`–`20`) et croiser le tout avec l'horloge de migration post-quantique `FIPS 203/204/205` et `ITSM.40.001` (`ch. 21`).
- **Analyse de la qualité scientifique et technique** :
  - *Forces* : La **grille des cinq questions** du [`chapitre 14`](Livre%20II\14-grille-cinq-questions.md) (*Qui est l'agent ? Au nom de qui ? Avec quelle portée ? Sous quelle responsabilité ? Comment l'arrêter ?*), le **passeport d'identité agentique à quatre pièces** du [`chapitre 16`](Livre%20II\16-passeport-agent.md) et l'analyse du **double silence cryptographique** (absence de profil PQC dans les protocoles agentiques et d'agilité algorithmique dans les jetons de délégation) au [`chapitre 21`](Livre%20II\21-horloge-post-quantique.md) sont des contributions analytiques remarquables (`[L]`).
  - *Faiblesses et anomalies* : Le Livre II souffre de **deux défauts bloquants** :
    1. **Les 5 contradictions internes de la passe `D-11` du 30 juillet 2026 (`A-B6`, `[L]`)** : greffe de `§ 13.0` sur W3C VC 2.0 / DID 1.1 contredite par `§ 13.1` (l. 172), `Synthèse` (l. 425) et `§ 13.6` (l. 492) ; collision de deux `Tableau 16.2` au ch. 16 (l. 147 et l. 382) ; ajout d'une **4e piste** (*atténuation par caveats* : Macaroons, Biscuit, GNAP `RFC 9635`) sous le titre `### 17.6.2 Trois pistes...` et conclusion *« aucune des trois »* (l. 562) ; ajout d'une **10e rangée** (`RFC 7662`) au `Tableau 20.1` commentée comme *« La onzième rangée »* (l. 328–337) ; extraction de la feuille de route canadienne `ITSM.40.001` en `§ 21.8` contredite par `§ 21.9` (l. 739) qui affirme que le socle est exclusivement fédéral américain.
    2. **Obsolescence IETF WIMSE au chapitre 18 et au chapitre 12 (`A-B4`, `[S]`)** : `draft-klrc-aiagent-auth-00` (`S-085`, `Tableau 18.1`), présenté au ch. 18 comme un brouillon individuel sans groupe de travail expirant le 27 septembre 2026, a en réalité atteint la révision `-03` le 6 juillet 2026, a été **adopté par le WG IETF WIMSE le 9 septembre 2026** et est devenu **`draft-ietf-wimse-aims-00`** le 15 septembre 2026 ; de plus, `draft-klrc-wimse-ai-agents-00` ([`ch. 12 § 12.5` l. 280](Livre%20II\12-heritage-standards-etires.md)) est **expiré depuis le 1er septembre 2026**.
- **Recommandations spécifiques** : Purger immédiatement les 5 contradictions internes des ch. 13, 16, 17, 20 et 21 (`A-B6`) ; mettre à jour le `Tableau 18.1` et le `§ 12.5` avec l'adoption WIMSE de `draft-ietf-wimse-aims-00` (`A-B4`) ; instruire le lot `D-9` au `§ 17.5` (`A-D2`).

---

### 4.3 Fiche 3 — Livre III : *Orchestration, gouvernance et conformité* (Chapitres 22 à 36)

- **Identifiant et intitulé** : [`Livre III/`](Livre%20III/) — Chapitres [`22`](Livre%20III\22-options-orchestration-paradigme-apm.md) à [`36`](Livre%20III\36-prospective-ap2-rails-canadiens.md) et [`Livre III/README.md`](Livre%20III/README.md).
- **Volume et statut de vérification** : `16` fichiers `.md`, `11 937` lignes, **`103 200` mots de corps** (cible `110 000`, écart `−6,2 %`), `35` tableaux, `35` figures SVG (`0` au ch. 28) — **100 % `[L]`**, scripts **`[R]`**, sources réglementaires canadiennes **`[S]`**.
- **Note du sous-ensemble** : **`16,0 / 20`**.
- **Thèse et rôle dans l'ensemble** : Confronter les quatre options d'orchestration (`OO1` chorégraphie, `OO2` orchestrateur central, `OO3` maillage pair-à-pair, `OO4` hybride hiérarchique), le paradigme `APM` et les six cadriciels du marché (`ch. 22`–`24`) au maillage réglementaire financier canadien et québécois : ligne directrice **E-23 du BSIF** (`ch. 25`), **article 12.1 de la Loi 25** et vide fédéral C-27 → C-36 (`ch. 26`), ligne directrice IA de l'**AMF** (`ch. 27`), **Avis 11-348 des ACVM** (`ch. 28`), pont architectural des **frames déterministes** (`ch. 29`), maillage international AI Act / DORA / NIST / ISO 42001 (`ch. 30`), **six durcisseurs financiers** (`ch. 31`), **Cadre bancaire axé sur le consommateur C-15** (`ch. 32`), rails **ISO 20022 / Lynx / RTR** (`ch. 33`), sous-domaines financiers (`ch. 34`), **dix études de cas canadiennes** (`ch. 35`) et prospective **AP2 sur les rails canadiens** (`ch. 36`).
- **Analyse de la qualité scientifique et technique** :
  - *Forces* : Le Livre III est le **cœur applicatif et réglementaire** de la somme (`31 %` du volume total). Le [`chapitre 29`](Livre%20III\29-pont-frames-deterministes.md) (traduction de l'article 12.1 de la Loi 25 en spécifications de *frames* déterministes avec le test de qualification à trois conditions cumulatives au `§ 29.4.1`), le [`chapitre 31`](Livre%20III\31-vertical-financier-durcisseurs.md) (qui pose 6 sièges structurants dont le patron d'irréversibilité et le principe des quatre-yeux) et le [`chapitre 33`](Livre%20III\33-iso-20022-lynx-rtr.md) (analyse du couplage entre messages `pacs.008`/`pain.001` d'ISO 20022, irrévocabilité de Lynx et fenêtre `T4 2026` du RTR) offrent une profondeur d'analyse sans équivalent dans la littérature professionnelle canadienne (`[L]`).
  - *Faiblesses et anomalies* :
    1. **Péremption calendaire au 14 octobre 2026 et contradiction interne ch. 33 vs ch. 36 (`A-B5`, `A-M7`, `[L]`, `[S]`)** : Nous sommes entrés depuis le 1er octobre 2026 dans le **`T4 2026`** du RTR ; le compte à rebours de 38 jours du `ch. 33 § 33.3` est échu, et le [`ch. 36 § 36.2.7` (l. 305)](Livre%20III\36-prospective-ap2-rails-canadiens.md) écrit encore au futur que le *By-law no 10* *« doit entrer en vigueur le 24 août 2026 »*. De même, les comptes à rebours vers le 1er mai 2027 aux [`ch. 25 § 25.1` (l. 90)](Livre%20III\25-e23-risque-modele.md) et [`ch. 26 § 26.3` (l. 159)](Livre%20III\26-vide-federal-c27-c36.md) sont figés à « neuf mois et quatre jours » alors qu'il reste **6 mois et 17 jours**, la date de publication de la LD IA de l'AMF (bloquée par HTTP 403 dans le texte) est établie au **7 avril 2026** (`[S]`), et le seuil d'obsolescence de 90 jours du [`ch. 35 § 35.10` (l. 852)](Livre%20III\35-etudes-de-cas-production-canadienne.md) est atteint le 14 octobre 2026.
    2. **Désynchronisation du chapitre 31 sur `S5` (`A-M9`, `[L]`, `[R]`)** : Le ch. 31 déclare encore en 4 endroits (`l. 66, 126, 568, 1041`) que `S5` est désactivé sur trois de ses sièges alors que `check-sieges.py` l'a réarmé le 2 septembre 2026.
    3. **Infraction à `D-9` (ch. 25 et 27), `Tableau 29.1` incomplet de 2 obligations de l'art. 12.1 (`R-IV-91`), et 4 préimpressions du `ch. 36 § 36.5` lues au seul résumé (`R-IV-99`)** (`[L]`).
- **Recommandations spécifiques** : Aligner `ch. 36 § 36.2.7` sur l'entrée en vigueur du 24 août 2026 et l'ouverture du `T4 2026` (`A-B5`) ; corriger les 4 mentions de `S5` au ch. 31 (`A-M9`) ; intégrer la date du **7 avril 2026** pour l'AMF (`S-023`) et compléter les 2 lignes manquantes du `Tableau 29.1` (`R-IV-91`).

---

### 4.4 Fiche 4 — Livre IV : *Architecture de référence et exploitation* (Chapitres 37 à 46)

- **Identifiant et intitulé** : [`Livre IV/`](Livre%20IV/) — Chapitres [`37`](Livre%20IV\37-maillage-agents-point-application.md) à [`46`](Livre%20IV\46-instrumentation-feuille-route.md) et [`Livre IV/README.md`](Livre%20IV/README.md).
- **Volume et statut de vérification** : `11` fichiers `.md`, `7 205` lignes, **`60 723` mots de corps** (cible `70 500`, écart `−13,9 %`), `19` tableaux, `24` figures SVG — **100 % `[L]`**, scripts **`[R]`**.
- **Note du sous-ensemble** : **`15,4 / 20`**.
- **Thèse et rôle dans l'ensemble** : Opérer le passage de l'analyse par silo à l'exploitation et à la composition architecturale : maillage d'agents et points d'application PEP/PDP (`ch. 37`), observabilité OpenTelemetry GenAI (`ch. 38`), cycle de vie opérationnel et 4 dérives (`ch. 39`), indicateurs AgentOps/FinOps (`ch. 40`), fabrique d'agents gouvernée (`ch. 41`), matrice de croisement protocoles × exigences canadiennes (`ch. 42`), architecture de référence en 6 couches (`ch. 43`), formalisation ArchiMate (`ch. 44`), blueprint instancié et cycle de vie bout-en-bout (`ch. 45`) et feuille de route d'instrumentation vers le 1er mai 2027 (`ch. 46`).
- **Analyse de la qualité scientifique et technique** :
  - *Forces* : Les chapitres **42, 43 et 46** représentent le sommet synthétique du *Compendium* (`[L]`). Le [`chapitre 42`](Livre%20IV\42-matrice-protocoles-exigences.md) démontre avec une rigueur chirurgicale le **renversement de la grille des cinq questions** entre les protocoles (qui répondent à Q1 et effleurent Q2–Q3 mais se taisent sur Q4–Q5) et les quatre instruments réglementaires canadiens (qui exigent Q3–Q5 mais se taisent sur les mécanismes protocolaires), d'où dérivent les **cinq zones de compensation** (`Tableau 42.2`) et les **cinq points de contrôle obligatoires `PC1`–`PC5`** du [`chapitre 43 (§ 43.3)`](Livre%20IV\43-architecture-reference-couches.md). De même, la désambiguïsation des **trois échelles d'autonomie homonymes** (`ch. 43 § 43.5`) et l'ordonnancement opératoire en trois mouvements vers le 1er mai 2027 (`ch. 46 § 46.2`) sont d'une grande valeur pratique.
  - *Faiblesses et anomalies* :
    1. **Trois chapitres grevés par des verrous de fond non levés (`ch. 41`, `ch. 44`, `ch. 45`) (`A-D3`, `A-D4`, `[L]`)** : Le [`chapitre 41`](Livre%20IV\41-fabrique-agents.md) (`−25,0 %`) a été rédigé hors portes sans aucune source au socle (`D-8`, 5 lots non ouverts) ; le [`chapitre 44`](Livre%20IV\44-formalisation-archimate.md) (`−25,8 %`) est à 100 % en `[C]` et son registre de 14 stéréotypes (`Tableau 44.1`) reste bloqué par la non-vérification du document normatif **ArchiMate 4 (`doc C260` du 27 avril 2026)** (`R-IV-101`), blocage qui se propage au `§ 45.14` du [`chapitre 45`](Livre%20IV\45-blueprint-instancie-cycle-de-vie.md) (`−38,7 %`).
    2. **Contradictions internes de re-datation aux chapitres 37 et 39 (`A-M10`, `[L]`)** : Le corps des `ch. 37 § 37.2.2` et `ch. 39 § 39.1 / § 39.3` conserve des affirmations démenties (« pré-version » pour `agentgateway`, « neuf dimensions » pour Langfuse) contredites par leurs propres notes adjacentes (`v1.4.0` stable, `4 dimensions`).
    3. **Anonymisation paradoxale au chapitre 45 (`A-m4`, `[L]`)** : Le `Tableau 45.2` tait les noms commerciaux des produits du portefeuille IBM qu'il instancie et le `§ 45.12` dé-nomme **Lynx** et **ISO 20022** contre la décision 18.
- **Recommandations spécifiques** : Exécuter le contrôle normatif sur ArchiMate 4 `doc C260` (`R-IV-101`) ; intégrer `v1.4.0` et `quatre dimensions` dans le corps des ch. 37 et 39 (`A-M10`) ; rétablir les noms des produits IBM, de CIBC, de Lynx et d'ISO 20022 au ch. 45 (`A-m4`) ; ajouter le paragraphe `T4.3` omis au ch. 40 `§ 40.7` (`A-m5`).

---

### 4.5 Fiche 5 — Livre V : *Prospective, limites et péremption* (Chapitres 47 à 50)

- **Identifiant et intitulé** : [`Livre V/`](Livre%20V/) — Chapitres [`47`](Livre%20V\47-artefact-livre-provenance-mise-en-service.md) à [`50`](Livre%20V\50-peremption-protocole-revalidation.md) et [`Livre V/README.md`](Livre%20V/README.md).
- **Volume et statut de vérification** : `5` fichiers `.md`, `2 797` lignes, **`26 848` mots de corps** (cible `30 400`, écart `−11,7 %`), `8` tableaux, `10` figures SVG — **100 % `[L]`**, scripts **`[R]`**, événements de péremption **`[S]`**.
- **Note du sous-ensemble** : **`15,8 / 20`** *(fort contraste entre les ch. 47–48 à `13,0 / 20` et les ch. 49–50 à `18,5 / 20`)*.
- **Thèse et rôle dans l'ensemble** : Instruire dans un premier mouvement (`ch. 47`–`48`) les deux angles morts matériels de la somme — la provenance de l'artefact livré (`SPDX 3.0`, `CycloneDX 1.7`, `SLSA v1.2`) et la sémantique d'effet (idempotence d'effet et compensation par sagas en régime probabiliste) — puis, dans un second mouvement (`ch. 49`–`50`), tracer la frontière de la connaissance vérifiable à l'horizon 2027–2032 (`PROGRAMMÉ` / `PROJETÉ` / `SPÉCULATIF`, registre des 33 lacunes des socles) et gouverner la péremption de l'ouvrage (`Tableau 50.1` des 14 événements, protocole de revalidation en 4 étapes, carte de fraîcheur des 50 chapitres).
- **Analyse de la qualité scientifique et technique** :
  - *Forces* : Les [`chapitres 49`](Livre%20V\49-horizon-frontiere-connaissance-verifiable.md) (`11 088` mots) et [`50`](Livre%20V\50-peremption-protocole-revalidation.md) (`5 920` mots) constituent un **modèle d'épistémologie appliquée à l'ingénierie** (`[L]`). Le verrou sémantique du `ch. 49 § 49.6` (pourquoi `JSON Schema`, `MCP` et `A2A` transportent des structures syntaxiques mais jamais d'ontologie formelle partageable ni de contrat d'effet) et l'architecture du `chapitre 50` (qui transforme le vieillissement documentaire en objet d'ingénierie testable) sont exemplaires.
  - *Faiblesses et anomalies* :
    1. **Deux divergences factuelles entre le texte et les figures SVG dans `figures/contenu5.py` (`A-B7`, `[L]`)** : [`Figure 49.0`](figures/f-49-00-cone-incertitude.svg) affiche **`ANNONCÉ`** au lieu de **`PROJETÉ`** (l. 81), et [`Figure 50.4`](figures/f-50-04-carte-fraicheur.svg) affiche **« onze événements »** au lieu de **« quatorze événements »** (l. 176).
    2. **Contradiction interne à la ligne 10 du `Tableau 50.1` (`A-M11`, `[L]`)** : la colonne 3 acte la revalidation du 2 septembre 2026 (`draft-sharif-01` au 27 février 2027) tandis que la colonne 4 parle encore des échéances des 27 septembre et 24 novembre 2026.
    3. **Inachèvement substantiel des chapitres 47 (`−37,1 %`) et 48 (`−39,9 %`) sous `D-3` / `G-6` (`A-M12`, `[L]`)** : rédigés sans socle primaire, ils exposent des contrats d'instruction au lieu d'analyses abouties.
- **Recommandations spécifiques** : Corriger les lignes 81 et 176 de [`figures/contenu5.py`](figures/contenu5.py) et régénérer les 2 SVG (`A-B7`) ; corriger la colonne 4 de la ligne 10 du `Tableau 50.1` et actualiser les 14 événements au 14 octobre 2026 (`A-M11`, `A-B3`, `A-B4`, `A-B5`).

---

### 4.6 Fiche 6 — Appareil probatoire, gouvernance (`PRD/`) et annexes (`annexe-*.md`)

- **Identifiant et intitulé** : [`PRD/`](PRD/) (`PRD.md` v0.20, `TOC.md` v0.36, `socle-consolide.md` v1.2, `registre-gel.md`, `gel-2026-07-27.md`, `gel-2026-07-28-volet-residuel.md`, `revalidation-2026-09-02.md`) et Annexes ([`annexe-bibliographie.md`](annexe-bibliographie.md), [`annexe-references.md`](annexe-references.md)).
- **Volume et statut de vérification** : `10` fichiers `.md`, `6 120` lignes — **100 % `[L]`**, scripts **`[R]`**.
- **Note du sous-ensemble** : **`16,5 / 20`**.
- **Analyse de la qualité scientifique et technique** :
  - *Forces* : La traçabilité des décisions (`D-1` à `D-19`), des portes (`G-1` à `G-7`), des 106 remontées (`R-IV-01` à `R-IV-112`) et du socle consolidé de 159 entrées (`S-001` à `S-159`) avec table de réconciliation des doublons inter-volumes est d'une rigueur archivistique rare (`[L]`).
  - *Faiblesses et anomalies* : (1) Cardinaux de mutations (`24/114/23/6` au lieu de `25/115/30/8`), version du TOC (`v0.32` au lieu de `v0.36`) et omission du ch. 31 (`§ 31.3.2`) dans [`PRD/PRD.md`](PRD/PRD.md) (`A-M5`) ; (2) désynchronisation de `S-001`, `S-027`, `S-032` et `S-131` dans [`annexe-references.md`](annexe-references.md) par rapport à `socle-consolide.md` v1.2 (`A-M6`) ; (3) [`annexe-bibliographie.md`](annexe-bibliographie.md) limitée aux 1 154 entrées du Volume I sans fusion des bibliographies des Volumes II et III (`A-D8`).

---

### 4.7 Fiche 7 — Chaîne de composition (`build/`), figures vectorielles (`figures/`) et harnais de vérification (`check-*.py`)

- **Identifiant et intitulé** : [`PRD/check-*.py`](PRD/), [`PRD/decompte.sh`](PRD/decompte.sh), [`PRD/reporter-volumetrie.py`](PRD/reporter-volumetrie.py), [`build/`](build/) et [`figures/`](figures/).
- **Volume et statut de vérification** : `22` scripts et gabarits (`8 120` lignes de code), `118` fichiers `.svg`, `50` fichiers `.html`, [`Compendium.pdf`](Compendium.pdf) (`1 000` pages) — **100 % `[L]` et `[R]`**.
- **Note du sous-ensemble** : **`16,8 / 20`**.
- **Analyse de la qualité scientifique et technique** :
  - *Forces* : Le principe du **contrôle du contrôleur par tests de mutation** (`25` mutations sur `check-toc.py`, `115` sur `check-sieges.py`, `30` sur `check-compendium.py`, `8` sur `verifier-piece.py`, soit **178 mutations** au total) et le générateur vectoriel autonome [`figures/dessine.py`](figures/dessine.py) (8 primitives géométriques sans dépendance externe gravant 115 figures en `< 2 s`) constituent un modèle d'ingénierie documentaire reproductible (`[L]`, `[R]`).
  - *Faiblesses et anomalies* : Échec `[R]` (`code 1`) de `verifier-piece.py` sur 2 fichiers HTML faute de `--columns=1000` dans `rendre-piece.py` (`A-B1`) ; échec `[R]` (`code 1`) de `bash PRD/decompte.sh --verifier` sans `LC_ALL=C` (`A-B2`) ; bogue du double pourcentage dans `reporter-volumetrie.py` (`A-M1`) ; bogue de sous-chaîne `"Vol. II" in "Vol. III"` dans `check-compendium.py` (`A-M3`) ; 6e recomposition PDF non journalisée et foliotage à `6,0 mm` du bord (`A-M4`).

---

## 5. Audit de l'appareil probatoire, méthodologique et empirique

### 5.1 Taxonomie et hygiène des sources (`[L]`, `[R]`)

Le socle probatoire du *Compendium* distingue trois régimes d'attestation (`[A]` primaire vérifiée, `[B]` secondaire concordante, `[C]` reprise interne non ré-extraite) complétés par le marqueur d'inférence **`Lecture de l'auteur`** (`596` occurrences dans le corps des 50 chapitres, `714` occurrences au total) (`[L]`). Dans [`PRD/socle-consolide.md`](PRD/socle-consolide.md) (v1.2), les **159 entrées uniques (`S-001` à `S-159`)** issues de la fusion des Volumes II et III se répartissent en **91 entrées en `[A]` (`57,2 %`)**, **17 entrées en `[B]` (`10,7 %`)** et **51 entrées en `[C]` (`32,1 %`)** (`[L]`). À ce socle s'ajoutent les **1 154 références uniques** du Volume I réunies dans [`annexe-bibliographie.md`](annexe-bibliographie.md) (`109` doublons fondus à partir de `1 263` lignes brutes) (`[R]`).

Toutefois, par suite de la décision `D-16` (2 septembre 2026) d'écarter le ré-adossement rétroactif des chapitres déjà rédigés, le rapport déclaratif de [`PRD/check-compendium.py`](PRD/check-compendium.py) (`[R]`) atteste deux dettes d'hygiène documentaire importantes :
- **Contrôle `P3`** : **524 emplois nus** d'identifiants `F-xx` ou `H-xx` (dépourvus du préfixe `Vol. II` ou `Vol. III`) subsistent à travers **26 pièces mixtes** (dont 73 au ch. 18, 49 au ch. 23, 47 au ch. 33, 37 au ch. 43, 35 au ch. 37 et 35 au ch. 39), créant un risque de collision de lecture entre les numérotations homonymes des Volumes II et III (`[R]`).
- **Contrôle `P4`** : **23 citations résiduelles** d'entrées exclues du socle consolidé (`F-92` et `F-96` du Vol. III, grevées d'une dette de vote adversarial, et `H-15`, issue de la prose du Vol. II) subsistent dans les chapitres 19, 20, 23, 38, 39, 40 et 43 (`[R]`).

### 5.2 Validité interne (`[L]`)

La validité interne de l'ouvrage est très élevée à l'échelle de l'architecture globale (parité des 56 thèses `P2`, intégrité des 26 sièges `S1`–`S5`, non-contradiction des arbitrages inter-volumes tranchés par `D-15`), mais elle est localement compromise par **huit contradictions internes textuelles ou graphiques** mises au jour par la lecture intégrale `[L]` :
1. Les **5 contradictions internes du Livre II (`A-B6.1` à `A-B6.5`)** laissées par les ajouts du 30 juillet 2026 (`D-11`) aux chapitres 13, 16, 17, 20 et 21.
2. La **contradiction entre le chapitre 33 (`§ 33.3`) et le chapitre 36 (`§ 36.2.7`, l. 305)** sur l'entrée en vigueur du *By-law no 10* le 24 août 2026 (`A-B5`).
3. Les **2 contradictions entre le corps et les notes de re-datation aux chapitres 37 (`§ 37.2.2`) et 39 (`§ 39.1` et `§ 39.3`)** sur `agentgateway v1.4.0` et les `4 dimensions` de Langfuse (`A-M10`).
4. Les **2 divergences entre le texte du Livre V et les figures SVG `Figure 49.0` (`ANNONCÉ` vs `PROJETÉ`) et `Figure 50.4` (`onze` vs `quatorze` événements)** (`A-B7`).

### 5.3 Validité externe et généralisabilité (`[L]`)

Le choix d'ancrer l'épreuve empirique et réglementaire dans le **secteur financier canadien et québécois** (BSIF E-23, AMF, Loi 25, ACVM 11-348, Paiements Canada Lynx/RTR, Cadre bancaire C-15, dix institutions financières canadiennes au ch. 35) constitue une **force méthodologique majeure** : loin de restreindre la portée de l'ouvrage à une monographie locale, ce vertical agit comme un *révélateur à haute contrainte* (irrévocabilité des règlements, obligation d'explication individuelle de l'art. 12.1, gouvernance du risque de modèle E-23). Les abstractions qui en sont tirées — la grille des cinq questions (ch. 14), le passeport à quatre pièces (ch. 16), le pont des frames déterministes (ch. 29), les cinq points de contrôle `PC1`–`PC5` (ch. 43) et l'analyse de l'idempotence d'effet (ch. 48) — sont immédiatement transposables à tout secteur critique (santé, énergie, administration publique, finance européenne sous AI Act / DORA) (`[L]`).

### 5.4 Reproductibilité et vérifiabilité automatique (`[R]`)

La reproductibilité outillée est l'un des points les plus admirables du *Compendium* : **11 des 14 commandes** de vérification et de mutation passent avec le code `0` (`[R]`). Les **3 échecs observés (`[R]`)** (`verifier-piece.py`, `verifier-piece-mutations.py` et `bash PRD/decompte.sh --verifier` sans `LC_ALL=C`) proviennent de deux causes purement mécaniques et immédiatement réparables (`--columns=1000` manquant dans `rendre-piece.py` et `LC_ALL=C` manquant à la ligne 70 de `decompte.sh`).

---

## 6. Confrontation à l'état de l'art et aux sources externes (`[S]`)

### 6.1 Exactitude des références normatives et techniques (`[S]`)

La confrontation directe des sources primaires au **14 octobre 2026** (`[S]`) confirme l'exactitude de la très grande majorité des références normatives du *Compendium* (RFC IETF `6749`, `7519`, `7643`, `7644`, `7662`, `8693`, `8705`, `9334`, `9396`, `9449`, `9635` ; recommandations W3C `VC Data Model 2.0` du 15 mai 2025 et `DID v1.1` du 19 mai 2026 ; standards post-quantiques NIST `FIPS 203`, `FIPS 204`, `FIPS 205` d'août 2024 et sélection de `HQC` en mars 2025 ; textes canadiens `L.C. 2026, ch. 6`, `DORS/2026-133`, BSIF `E-23`, Loi 25 art. 12.1, Avis ACVM `11-348` ; spécifications `MCP 2025-11-25` et `A2A v0.3.0`).

En revanche, la confrontation externe `[S]` met au jour **quatre écarts factuels ou méthodologiques significatifs** :
1. **Adoption par le groupe de travail IETF WIMSE de `draft-klrc-aiagent-auth` en `draft-ietf-wimse-aims-00` (`A-B4`, `[S]`)** : Contrairement à ce qu'affirment `S-085`, le [`chapitre 18 (§ 18.1, Tableau 18.1)`](Livre%20II\18-know-your-agent.md), le [`chapitre 50 (Tableau 50.1, Événement 10)`](Livre%20V\50-peremption-protocole-revalidation.md) et [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md), le brouillon `draft-klrc-aiagent-auth` n'est pas resté en révision `-00` (26 mars 2026) ni sans groupe de travail : il a publié les révisions `-01`, `-02` et **`-03` le 6 juillet 2026** (avant même le gel initial du 27 juillet 2026 !), a été **adopté par le groupe de travail IETF WIMSE le 9 septembre 2026**, et a été **remplacé le 15 septembre 2026 par `draft-ietf-wimse-aims-00`** (*AI Identity Management System*, auteurs Pioli, Lombardo, Rosomakho, Campbell, échéance 19 mars 2027) (`[S]`).
2. **Publication de `draft-ietf-oauth-v2-1-16` le 2 septembre 2026 (`A-B4`, `[S]`)** : Le [`chapitre 3 (§ 3.2.1, l. 101)`](Livre%20I\03-securite-identite-gouvernance.md) cite toujours `draft-ietf-oauth-v2-1-15` (expiré le 3 septembre 2026) en se bornant à indiquer en note qu'il a été renouvelé avant échéance, sans mentionner le numéro **`draft-ietf-oauth-v2-1-16`** publié le 2 septembre 2026 ni le jalon du groupe de travail OAuth (`Dec 2026 : Submit OAuth 2.1 to IESG for publication as Proposed Standard`) (`[S]`).
3. **Expiration de `draft-klrc-wimse-ai-agents-00` le 1er septembre 2026 (`A-B4`, `[S]`)** : Cité au présent dans le [`chapitre 12 (§ 12.5, l. 280)`](Livre%20II\12-heritage-standards-etires.md), ce brouillon a expiré le 1er septembre 2026 sans être relevé lors de la passe du 2 septembre 2026 (`[S]`).
4. **Date exacte de la *Ligne directrice sur l'utilisation de l'IA* de l'AMF (`S-023` / `S-113`, `[S]`)** : Laissée à « avril 2026 » dans les chapitres 27 et 42 en raison de quatre refus HTTP 403 lors du gel, la publication finale de la ligne directrice de l'AMF est datée du **7 avril 2026** (entrée en vigueur le **1er mai 2027**, en alignement exact avec E-23 du BSIF) (`[S]`).

### 6.2 Fraîcheur temporelle et péremption au 14 octobre 2026 (`[L]`, `[S]`)

Comme établi en détail dans [`audit.md` (§ 3)](audit.md), l'évaluation au **14 octobre 2026** constate :
- l'expiration depuis 12 jours (le **2 octobre 2026**) de la validité de 30 jours de `revalidation-2026-09-02.md` sous `CA-IV-04` (`A-B3`) ;
- l'entrée depuis 14 jours (le **1er octobre 2026**) dans la fenêtre cible du **`T4 2026`** du rail `RTR` (`S-027` / `F-29`), rendant caducs le compte à rebours de 38 jours du `ch. 33 § 33.3` et la consultation de 30 jours ouverte le 24 août 2026 (`A-B5`) ;
- l'atteinte exacte, au **14 octobre 2026**, du seuil d'obsolescence trimestriel (90 jours) déclaré par le `ch. 35 § 35.10` (l. 852) pour les dix études de cas canadiennes gelées les 16–17 juillet 2026 (`A-M7`) ;
- le raccourcissement du compte à rebours vers le **1er mai 2027** (BSIF E-23 et AMF LD IA) de `278 jours (9 mois et 4 jours)` à **`199 jours (6 mois et 17 jours)`** (`A-M7`).

### 6.3 Angles morts et littérature omise (`[L]`, `[S]`)

Trois angles morts bibliographiques et normatifs — lucidement déclarés par l'auteur sous forme de remontées ou de lots ouverts — demeurent non résorbés :
1. **Le document normatif ArchiMate 4 (`The Open Group, doc C260`, 27 avril 2026)** (`R-IV-101`, `ch. 44`–`45`) : non consulté en source primaire `[A]`, alors qu'il retire ~30 % des éléments d'ArchiMate 3.2 et conditionne la validité du registre des 14 stéréotypes (`Tableau 44.1`).
2. **La littérature primaire sur le biais d'automatisation et la supervision humaine en boucle** (`lot D-9`, `ch. 17 § 17.5`, `ch. 25`, `ch. 27`, `ch. 40 § 40.4`) : les travaux fondateurs (Parasuraman & Manzey 2010, Skitka et coll. 1999, Cummings 2004, et les études empiriques 2025–2026 sur l'approbation réflexe des actions d'agents) ne sont pas extraits au socle, empêchant les chapitres 25, 27 et 40 de fixer des seuils d'effectivité au contrôle humain.
3. **Les standards de chaîne d'approvisionnement logicielle (`SPDX 3.0`, profil `AI/Dataset`, `CycloneDX 1.7` ML-BOM, `SLSA v1.2`, `in-toto`, `Sigstore`) et la littérature sur les transactions compensables en contexte probabiliste (`SagaLLM`, `arXiv:2503.11951`)** (`lots L1–L3`, `ch. 47`–`48`) : laissés à l'état de contrats d'instruction ou de note non votée (`§ 47.0.1`).

---

## 7. Forces majeures et contributions distinctives

- **`F1` — Architecture épistémique à trois régimes (`[A]`, `[B]`, `[C]`) et isolement systématique des `Lecture de l'auteur`** :
  - *Constat* : L'ouvrage applique d'un bout à l'autre la loi du maillon le plus faible épistémique et isole chaque inférence, synthèse ou recommandation propre sous le marqueur explicite `Lecture de l'auteur` (`596` occurrences dans le corps, `714` au total) (`[L]`, `[R]`).
  - *Preuve précise* : [`PRD/PRD.md`](PRD/PRD.md) (§ 7.2–7.4), [`PRD/check-compendium.py`](PRD/check-compendium.py) (contrôles `P1`–`P10`) et les notes de statut finales des 50 chapitres (`[L]`, `[R]`).
  - *Portée* : Élimine radicalement le défaut majeur de la littérature actuelle sur l'IA agentique (la confusion entre ce qu'une spécification garantit réellement dans son schéma JSON/protocole et ce que la doctrine marketing d'un éditeur promet).
- **`F2` — Mécanisme des 26 sièges de non-redondance vérifié par tests de mutation (`check-sieges.py`)** :
  - *Constat* : Sur une somme de `333 416` mots, la cohérence inter-chapitres est garantie par 26 sièges formels contrôlés automatiquement par 5 règles (`S1` à `S5`) elles-mêmes validées contre `115` mutations (`[R]`).
  - *Preuve précise* : [`PRD/check-sieges.py`](PRD/check-sieges.py) et [`PRD/check-sieges-mutations.py`](PRD/check-sieges-mutations.py) (`code 0` à l'exécution `[R]`).
  - *Portée* : Empêche la dérive et la duplication des définitions à travers les 50 chapitres et constitue un patron d'ingénierie éditoriale réutilisable pour tout ouvrage collectif ou normatif de grande taille.
- **`F3` — Grille des cinq questions d'identité (ch. 14), passeport à quatre pièces (ch. 16) et renversement protocoles × réglementation canadienne (ch. 42)** :
  - *Constat* : Le croisement systématique entre les cinq questions d'identité/délégation (`Q1` à `Q5`), les protocoles (`MCP`, `A2A`, `OAuth 2.1`, `RFC 8693`, `SPIFFE`, `DID/VC`) et les quatre instruments canadiens (`BSIF E-23`, `AMF LD IA`, `Loi 25 art. 12.1`, `ACVM 11-348`) démontre formellement une complémentarité inversée (les protocoles couvrent `Q1`–`Q2` et ignorent `Q4`–`Q5`, tandis que le droit exige `Q3`–`Q5` sans prescrire `Q1`–`Q2`) (`[L]`).
  - *Preuve précise* : [`Livre II/14-grille-cinq-questions.md`](Livre%20II\14-grille-cinq-questions.md) (`Tableau 14.1` et `14.2`), [`Livre II/16-passeport-identite-agentique.md`](Livre%20II\16-passeport-agent.md) (`Tableau 16.1`) et [`Livre IV/42-matrice-protocoles-exigences.md`](Livre%20IV\42-matrice-protocoles-exigences.md) (`Tableau 42.1` et `Tableau 42.2`) (`[L]`).
  - *Portée* : Fournit aux architectes et aux régulateurs la justification théorique et pratique des **cinq zones de compensation** et des **cinq points de contrôle obligatoires (`PC1`–`PC5`)** du [`chapitre 43 (§ 43.3)`](Livre%20IV\43-architecture-reference-couches.md).
- **`F4` — Pont architectural des *frames* déterministes sous l'article 12.1 de la Loi 25 (ch. 29)** :
  - *Constat* : Le chapitre 29 traduit une obligation légale de transparence et d'explicabilité des décisions automatisées (art. 12.1 de la Loi 25 québécoise) en une structure de données déterministe enveloppant l'appel d'agent, assortie d'un **test de qualification à trois conditions cumulatives** (`§ 29.4.1`) permettant de déterminer quand une chaîne multi-agents tombe sous le coup de la loi (`[L]`).
  - *Preuve précise* : [`Livre III/29-pont-frames-deterministes.md`](Livre%20III\29-pont-frames-deterministes.md) (`Tableau 29.1` et siège du `§ 29.4.1`) (`[L]`).
  - *Portée* : Modèle exemplaire d'*ingénierie du droit par le code* (*compliance-by-design*), directement applicable dans les institutions financières québécoises et canadiennes.
- **`F5` — Programme déclaratif autonome des 118 figures vectorielles SVG (`figures/`) et composition Typst de 1 000 pages (`build/`)** :
  - *Constat* : Au lieu de dépendre d'outils externes fragiles, l'ouvrage grave ses 115 figures par un moteur Python pur de 8 primitives ([`figures/dessine.py`](figures/dessine.py)), vérifié à l'empreinte SHA-256 (`python figures/genere.py --verifier` → `0`), et compose un volume Typst de **1 000 pages exactes** sans débordement (`check-resume.py` → `+21.5 pt [OK]`) (`[L]`, `[R]`).
  - *Preuve précise* : [`figures/dessine.py`](figures/dessine.py), [`figures/genere.py`](figures/genere.py), [`build/compendium.template`](build/compendium.template) et [`Compendium.pdf`](Compendium.pdf) (`[L]`, `[R]`).
  - *Portée* : Garantit la pérennité graphique et la reproductibilité typographique du corpus.
- **`F6` — Codification réflexive de la frontière du vérifiable (ch. 49) et du protocole de péremption (ch. 50)** :
  - *Constat* : Rares sont les ouvrages d'informatique qui consacrent leurs deux derniers chapitres à recenser leurs propres lacunes héritées (`33` lacunes au `ch. 49 § 49.12`) et à définir les 14 événements précis qui rendront leurs chapitres caducs, avec la liste exacte des paragraphes à réécrire (`Tableau 50.1` et carte de fraîcheur du `ch. 50 § 50.4`) (`[L]`).
  - *Preuve précise* : [`Livre V/49-horizon-frontiere-connaissance-verifiable.md`](Livre%20V\49-horizon-frontiere-connaissance-verifiable.md) et [`Livre V/50-peremption-protocole-revalidation.md`](Livre%20V\50-peremption-protocole-revalidation.md) (`[L]`).
  - *Portée* : Rend l'audit et la maintenance scientifique de l'ouvrage rapides, prévisibles et traçables.

---

## 8. Faiblesses, angles morts et risques méthodologiques

- **`W1` [Bloquante] — Cinq contradictions internes majeures au Livre II (`A-B6`) et deux divergences texte ↔ SVG au Livre V (`A-B7`)** :
  - *Constat* : Les ajouts documentaires du 30 juillet 2026 (`D-11`) aux chapitres 13, 16, 17, 20 et 21 et la mise à jour du 2 septembre 2026 (`D-16`) au chapitre 50 n'ont pas été répercutés sur les paragraphes adjacents ni sur deux figures de `figures/contenu5.py` (`[L]`).
  - *Preuve précise* : `ch. 13` (`§ 13.0` vs `§ 13.1` l. 172, `Synthèse` l. 425, `§ 13.6` l. 492), `ch. 16` (deux `Tableau 16.2` l. 147 et l. 382), `ch. 17` (`§ 17.6.2` l. 483 et l. 562), `ch. 20` (`§ 20.4` l. 328–337), `ch. 21` (`§ 21.8` l. 637 vs `§ 21.9` l. 739), et `figures/contenu5.py` (l. 81 `ANNONCÉ` vs `PROJETÉ` ; l. 176 `onze` vs `quatorze` événements) (`[L]`).
  - *Impact* : Mine la validité interne de sept chapitres et désoriente le lecteur qui voit une section nier ce que la section précédente vient d'établir en `[A]`.
  - *Remédiation* : Exécuter les corrections chirurgicales prescrites sous `A-B6` et `A-B7` (voir § 10, `P1-3` et `P1-4`).
- **`W2` [Bloquante] — Faille méthodologique de `revalidation-2026-09-02.md` sur les brouillons IETF (`A-B4`) et expiration de `CA-IV-04` au 14 octobre 2026 (`A-B3`, `A-B5`)** :
  - *Constat* : En interrogeant le 2 septembre 2026 des URL d'archives immuables (`archive/id/draft-...-00.txt`), la passe de revalidation a conclu à tort que les brouillons IETF étaient inchangés, manquant le passage de `draft-klrc-aiagent-auth` en `-03` dès le 6 juillet 2026, son adoption par le WG IETF WIMSE le 9 septembre 2026 et son remplacement par **`draft-ietf-wimse-aims-00`** le 15 septembre 2026 (`[S]`). De plus, au 14 octobre 2026, la fenêtre de 30 jours de `CA-IV-04` est expirée depuis le 2 octobre (`A-B3`) et le `T4 2026` du RTR est ouvert depuis le 1er octobre avec une contradiction non purgée au `ch. 36 § 36.2.7` l. 305 (`A-B5`) (`[L]`, `[S]`).
  - *Preuve précise* : [`PRD/revalidation-2026-09-02.md`](PRD/revalidation-2026-09-02.md), [`ch. 18 Tableau 18.1`](Livre%20II\18-know-your-agent.md), [`ch. 36 § 36.2.7` l. 305](Livre%20III\36-prospective-ap2-rails-canadiens.md) et Datatracker IETF (`[S]`).
  - *Impact* : Fausse l'analyse institutionnelle du chapitre 18 (qui soutient que l'authentification d'agents n'est prise en charge par aucun groupe de travail IETF constitué, alors que WIMSE l'a officiellement adoptée) et laisse coexister au chapitre 36 un futur révolu (« doit entrer en vigueur le 24 août 2026 ») avec le passé composé du chapitre 33.
  - *Remédiation* : Remplacer dans le protocole du ch. 50 les URL `/archive/id/draft-...-00.txt` par les URL `https://datatracker.ietf.org/doc/draft-.../`, mettre à jour `S-084`, `S-085`, les ch. 3, 12, 13, 18, 33, 36 et 50, et enregistrer la passe du 14 octobre 2026 (`P1-5`, `P1-6`).
- **`W3` [Bloquante] — Deux échecs d'exécution (`code 1`) dans le harnais de vérification (`A-B1`, `A-B2`) et bogue `P3` dans `check-compendium.py` (`A-M3`)** :
  - *Constat* : `python build/verifier-piece.py` (et `verifier-piece-mutations.py`) échoue sur 2 fichiers `.html` (`ch. 14` l. 677 et `ch. 37` l. 740), `bash PRD/decompte.sh --verifier` échoue sans `LC_ALL=C` (`241 260` vs `233 257`), et `check-compendium.py` évalue `"Vol. II" in "Vol. III"` à `True` (`[R]`, `[L]`).
  - *Preuve précise* : Sorties d'exécution `[R]` (Annexe A) et [`PRD/check-compendium.py`](PRD/check-compendium.py#L166-L168).
  - *Impact* : Rompt la promesse d'un dépôt où 100 % des contrôles documentés dans `README.md` passent à zéro écart.
  - *Remédiation* : Passer `--columns=1000` à Pandoc dans `build/rendre-piece.py`, préfixer la ligne 70 de `PRD/decompte.sh` par `LC_ALL=C`, et corriger la regex de `"Vol. II"` dans `PRD/check-compendium.py` (`P1-1`, `P1-2`).
- **`W4` [Majeure] — Désynchronisation des `### En-tête de rédaction` dans 45 chapitres (`A-M1`), troncature des garde-fous dans 8 chapitres (`A-M2`) et désynchronisations documentaires (`A-M4` à `A-M11`)** :
  - *Constat* : L'outillage de mise à jour des en-têtes (`reporter-volumetrie.py` et `T4.3`) n'a mis à jour correctement que le bandeau supérieur de 5 lignes, laissant dans le pied des chapitres un pourcentage hybride (`mots_2_sept` + `%_28_juillet`) sur 40 chapitres ou l'ancien nombre de mots sur 5 chapitres (`ch. 10, 31, 35, 40, 42`), tandis que `PRD.md`, `JOURNAL.md`, `annexe-references.md` (4 entrées), `ch. 8` (thèse l. 15), `ch. 31` (`S5`), `ch. 37/39` (corps vs notes) et `Tableau 50.1` (l. 10 col. 4) présentent des désynchronisations locales (`[L]`).
  - *Preuve précise* : Voir [`audit.md` (§ 1.2, § 2.2, § 4 et § 5.2)](audit.md) (`[L]`).
  - *Impact* : Dégrade la précision métrologique de l'appareil critique.
  - *Remédiation* : Corriger `reporter-volumetrie.py` et resynchroniser l'ensemble des pièces listées (`P2-1` à `P2-6`).
- **`W5` [Majeure] — Quatre chapitres rédigés sans socle primaire (`ch. 41, 44, 47, 48`) et hypertrophie du métadiscours de gouvernance (`A-M12`, `A-D3`, `A-D4`)** :
  - *Constat* : Rédigés avant l'instruction de leurs lots (`D-8` au ch. 41, `R-IV-101`/`102` au ch. 44, `D-3` aux ch. 47–48), ces quatre chapitres présentent un fort déficit volumétrique (`−25,0 %`, `−25,8 %`, `−37,1 %`, `−39,9 %`) et consacrent une part importante de leur texte à commenter l'absence de leur propre socle documentaire (`[L]`).
  - *Preuve précise* : [`ch. 41`](Livre%20IV\41-fabrique-agents.md) (`4 503 / 6 000` mots), [`ch. 44`](Livre%20IV\44-formalisation-archimate.md) (`6 303 / 8 500` mots, 100 % en `[C]`), [`ch. 47`](Livre%20V\47-artefact-livre-provenance-mise-en-service.md) (`5 033 / 8 000` mots) et [`ch. 48`](Livre%20V\48-semantique-effet-idempotence-compensation.md) (`4 807 / 8 000` mots) (`[L]`).
  - *Impact* : Crée un déséquilibre de densité scientifique entre les livres amont (Livres I à III) et la fin de la somme (second mouvement du Livre IV et premier mouvement du Livre V).
  - *Remédiation* : En cas de levée de `D-18`, instruire prioritairement C260 ArchiMate 4 (`R-IV-101`), les 5 lots du ch. 41 et les lots `L1`–`L3` des ch. 47–48 (`P3-1`, `P3-2`).
- **`W6` [Majeure] — Non-réadossement des chapitres aux identifiants `S-001`..`S-159` (`CA-IV-01` / `A-D6`) et absence de la couche d'exécution dans le Livre IV (`G-5` / `A-D5`)** :
  - *Constat* : Le socle consolidé (`S-001` à `S-159`) existe dans `PRD/socle-consolide.md` et `annexe-references.md`, mais les chapitres des Livres I à IV continuent de citer les anciens identifiants `F-xx` et `H-xx` des Volumes II et III (avec `524` emplois nus sur 26 pièces mixtes et `23` citations de `F-92`/`F-96`/`H-15`), tandis que la couche d'exécution (`D-2`) est absente de l'architecture en 6 couches du chapitre 43 (`[L]`, `[R]`).
  - *Preuve précise* : Rapport déclaratif `P3` et `P4` de [`PRD/check-compendium.py`](PRD/check-compendium.py) (`[R]`) et [`PRD/PRD.md` (§ 8, G-5)](PRD/PRD.md) (`[L]`).
  - *Impact* : Rend la navigation du lecteur entre le corps des chapitres et l'`annexe-references.md` indirecte et laisse un angle mort architectural sur l'isolation du harnais d'exécution au chapitre 43.
  - *Remédiation* : Substituer ou doubler les `F-xx`/`H-xx` par leurs `S-nnn` dans les 50 chapitres et insérer un point de contrôle ou une sous-couche dédiée au harnais d'exécution au `ch. 43 § 43.1 / § 43.3` (`P3-3`, `P3-4`).
- **`W7` [Mineure] — Survivance de périphrases d'anonymisation de la décision 15 malgré la décision 18 (`A-m4`)** :
  - *Constat* : Bien que la décision 18 du 30 juillet 2026 ait révoqué la consigne d'évitement des noms propres de la décision 15 (28 juillet 2026), de nombreuses périphrases énigmatiques subsistent dans les Livres I, III et IV (notamment au `ch. 38 Tableau 38.2` et au `ch. 45 Tableau 45.2` où les produits du portefeuille IBM sont décrits sans être nommés, et au `ch. 45 § 45.12` où Lynx et ISO 20022 sont remplacés par *« le rail de grande valeur »* et *« la norme de messagerie financière »*) (`[L]`).
  - *Preuve précise* : [`ch. 38 Tableau 38.2` l. 392–393](Livre%20IV\38-observabilite-agentique.md), [`ch. 39 § 39.1` l. 105 & `§ 39.3` l. 262](Livre%20IV\39-cycle-de-vie-operationnel.md), [`ch. 43 § 43.6` l. 446–451](Livre%20IV\43-architecture-reference-couches.md), [`ch. 45 Tableau 45.2` l. 120–155 & `§ 45.12` l. 466](Livre%20IV\45-blueprint-instancie-cycle-de-vie.md) (`[L]`).
  - *Impact* : Nuit à la clarté didactique et contredit l'objectif d'instanciation concrète du chapitre 45.
  - *Remédiation* : Rétablir les dénominations explicites conformément à la décision 18 (`P2-7`).

---

## 9. Qualité rédactionnelle, pédagogique et typographique

1. **Registre de langue et précision terminologique (`[L]`)** : La langue française du *Compendium* est d'une tenue remarquable — soutenue, analytique, exempte de jargon anglophone non défini et dotée de traductions constantes (*mandat*, *jeton porteur*, *point d'application / point de décision*, *dérive de mandat*, *idempotence d'effet*, *coupe-circuit*). Les seules scories relevées sur `333 416` mots se limitent à quatre coquilles ponctuelles (`JSON-RPC 2.0..*` au ch. 3 l. 15 `A-m6`, `de de` au ch. 15 l. 201 `A-m7`, `La seconde garde-fou` au ch. 24 l. 458 `A-m8`, `d'une jalon` au ch. 46 l. 390 `A-m9`).
2. **Clarté didactique et progression (`[L]`)** : Chaque chapitre s'ouvre sur un bandeau de métadonnées standardisé, rappelle verbatim sa thèse directrice, structure son propos par paliers numérotés (`§ N.0` à `§ N.k`), se clôt par un encadré *« Synthèse : ce que le chapitre lègue à la somme »* (assurant le chaînage amont/aval) et isole son appareil critique dans une *Note de statut* finale. Cette séparation entre le corps architectural et la note de statut est excellente dans les Livres I et II, mais tend à s'estomper dans les chapitres du Livre IV et du Livre V rédigés sans socle (`ch. 41, 44, 45, 47, 48`), où les réserves méthodologiques envahissent le corps même de l'exposé.
3. **Qualité visuelle, figures SVG et mise en page Typst (`[L]`, `[R]`)** :
   - Les **118 figures vectorielles SVG** (`115` générées par `figures/dessine.py` sur une palette sobre anthracite/bleu-gris/ocre/brique et `3` antérieures au ch. 8) apportent une valeur synoptique décisive (notamment les planches ArchiMate du ch. 44, les chronogrammes protocolaires des ch. 6–8 et les cônes/cartes des ch. 49–50, sous réserve de la correction de `A-B7` dans `contenu5.py`). Seul le [`chapitre 28`](Livre%20III\28-valeurs-mobilieres-acvm-11-348.md) est dépourvu de figure (`A-m13`).
   - L'ouvrage paginé [`Compendium.pdf`](Compendium.pdf) (**1 000 pages**, format `6,5 × 9,25 po`, police *Libertinus Serif* `9,5 pt`, `PAS = 16.675pt`) est composé sans aucune veuve/orpheline non maîtrisée et tient son budget de 1 000 pages avec un dégagement de `+21,5 pt` en page 1000 (`[R]`). Seule la distance de **`6,0 mm`** entre les titres courants / folios et le bord physique de la feuille mérite d'être portée à `7,0 mm` (`header-ascent: 11mm`) pour respecter la marge d'impression usuelle de `6,35 mm` (`A-M4`).

---

## 10. Feuille de route de remédiation (plan d'action priorisé)

### Priorité 1 — Corrections bloquantes et immédiates (`A-B1` à `A-B7` — effort estimé : `1,5 jour`)

| ID action | Cible précise (fichier, lignes) | Action corrective concrète | Critère de validation (`[R]` / `[L]`) |
| :---: | :--- | :--- | :--- |
| **`P1-1`** (`A-B1`) | [`build/rendre-piece.py`](build/rendre-piece.py#L48), `ch. 14.html`, `ch. 37.html` | Ajouter `"--columns=1000"` à l'invocation de `pandoc` dans `build/rendre-piece.py` et régénérer les 50 `.html`. | `python build/verifier-piece.py` et `verifier-piece-mutations.py` retournent **`0`**. |
| **`P1-2`** (`A-B2`, `A-M3`) | [`PRD/decompte.sh`](PRD/decompte.sh#L70), [`PRD/check-compendium.py`](PRD/check-compendium.py#L166) | Préfixer `wc -w` par `LC_ALL=C` à la ligne 70 de `PRD/decompte.sh` ; remplacer `"Vol. II" in b` par `re.search(r"Vol\.\s+II(?!I)", b)` dans `check-compendium.py`. | `bash PRD/decompte.sh --verifier` (sans préfixe) et `check-compendium.py` retournent **`0`**. |
| **`P1-3`** (`A-B7`) | [`figures/contenu5.py`](figures/contenu5.py#L81) (l. 81 et l. 176) | Remplacer `"ANNONCÉ"` par `"PROJETÉ"` (l. 81, `Figure 49.0`) et `"onze événements"` par `"quatorze événements"` (l. 176, `Figure 50.4`), puis exécuter `python figures/genere.py`. | `python figures/genere.py --verifier` retourne **`0`** et les 2 SVG concordent avec les ch. 49 et 50. |
| **`P1-4`** (`A-B6`) | [`ch. 13`](Livre%20II\13-identite-decentralisee-vc-did.md), [`ch. 16`](Livre%20II\16-passeport-agent.md), [`ch. 17`](Livre%20II\17-chaine-mandat-deux-sauts.md), [`ch. 20`](Livre%20II\20-usurpation-revocation-boucle-defensive.md), [`ch. 21`](Livre%20II\21-horloge-post-quantique.md) | Purger les 5 contradictions internes `D-11` du Livre II : corriger `§ 13.1` l. 172, `Synthèse` l. 425 et `§ 13.6` l. 492 ; renuméroter le second `Tableau 16.2` en `Tableau 16.3` (l. 382) ; passer `§ 17.6.2` à « Quatre pistes » et corriger l. 562 ; remplacer « onzième / dix » par « dixième / neuf » en `§ 20.4` l. 328–337 ; aligner `§ 21.9` l. 739 sur `§ 21.8` (`ITSM.40.001`). | Lecture `[L]` sans contradiction interne et `check-compendium.py` → **`0`**. |
| **`P1-5`** (`A-B4`, `A-M11`) | [`PRD/socle-consolide.md`](PRD/socle-consolide.md), `ch. 3`, `ch. 12`, `ch. 13`, `ch. 18`, `ch. 50` | Remplacer les URL `/archive/id/draft-...-00.txt` par les URL `datatracker.ietf.org/doc/...` ; acter le passage de `draft-klrc-aiagent-auth` en `-03` puis son adoption WG WIMSE sous **`draft-ietf-wimse-aims-00`** (15 sept. 2026), la publication de **`draft-ietf-oauth-v2-1-16`** (2 sept. 2026), l'expiration de `draft-klrc-wimse-ai-agents-00` (1er sept. 2026) et `draft-ietf-wimse-workload-creds-01` ; harmoniser la ligne 10 col. 4 du `Tableau 50.1`. | Parité exacte avec le Datatracker IETF au 14 oct. 2026 (`[S]`). |
| **`P1-6`** (`A-B3`, `A-B5`) | [`ch. 33 § 33.3`](Livre%20III\33-iso-20022-lynx-rtr.md), [`ch. 36 § 36.2.7`](Livre%20III\36-prospective-ap2-rails-canadiens.md), [`ch. 50`](Livre%20V\50-peremption-protocole-revalidation.md) | Corriger le futur caduc du `ch. 36 § 36.2.7` l. 305 (*« est entré en vigueur le 24 août 2026 »*), acter l'entrée dans le **`T4 2026`** du RTR depuis le 1er oct. 2026 et enregistrer une passe de revalidation datée du 14 oct. 2026 pour restaurer `CA-IV-04`. | Aucune contradiction ch. 33 / ch. 36 et validité `CA-IV-04` restaurée pour 30 jours. |

### Priorité 2 — Consolidations méthodologiques et documentaires majeures (`A-M1` à `A-M10`, `A-m1` à `A-m14` — effort estimé : `1,5 jour`)

| ID action | Cible précise | Action corrective concrète | Critère de validation |
| :---: | :--- | :--- | :--- |
| **`P2-1`** (`A-M1`, `A-M2`) | [`PRD/reporter-volumetrie.py`](PRD/reporter-volumetrie.py), 50 chapitres | Étendre `reporter-volumetrie.py` pour synchroniser la ligne `Volumétrie :` de l'`### En-tête de rédaction` inférieur des 50 chapitres (éliminant les 40 doubles `%` et les 5 anciens décomptes) et rétablir les réserves `F-xx` / `§ 8.2` en tête des 8 chapitres tronqués (`ch. 8–11, 39, 42–44`). | `python PRD/reporter-volumetrie.py --verifier` étendu aux deux en-têtes retourne **`0`**. |
| **`P2-2`** (`A-M8`, `A-M9`, `A-M10`) | `ch. 8` (l. 15), `ch. 31` (l. 66, 126, 568, 1041), `ch. 37` (§ 37.2.2), `ch. 39` (§ 39.1, § 39.3) | Rétablir la thèse verbatim de `TOC.md` en tête du ch. 8 ; corriger les 4 mentions erronées de `S5` désactivé au ch. 31 ; intégrer `agentgateway v1.4.0` et les `4 dimensions` de Langfuse directement dans le corps des ch. 37 et 39. | `check-compendium.py` `P2` renforcé sur la thèse entière retourne **`0`**. |
| **`P2-3`** (`A-M5`, `A-M6`, `A-m2`) | [`PRD/PRD.md`](PRD/PRD.md), [`annexe-references.md`](annexe-references.md), `registre-gel.md`, `revalidation-2026-09-02.md` | Mettre à jour `PRD.md` (`TOC v0.36`, ajout du `ch. 31` en § 7.1, mutations `25/115/30/8` en § 9 et § 18.3) ; synchroniser `S-001`, `S-027`, `S-032` et `S-131` dans `annexe-references.md` ; passer `v0.35` à `v0.36`. | Parité exacte entre `socle-consolide.md` v1.2 et `annexe-references.md`. |
| **`P2-4`** (`A-M4`, `A-m1`) | [`build/compendium.template`](build/compendium.template), [`build/echantillon.template`](build/echantillon.template), [`JOURNAL.md`](JOURNAL.md) | Documenter la 6e recomposition du 15 sept. 2026 (`PAS = 16.675pt`) dans `JOURNAL.md` et `PRD.md` ; ramener `header-ascent`/`footer-descent` à `11mm` (`7,0 mm` du bord) ; aligner `echantillon.template`. | `Compendium.pdf` à 1 000 pages avec folios à `≥ 7,0 mm` du bord. |
| **`P2-5`** (`A-M7`) | `ch. 25, 26, 27, 30, 31, 34, 35, 42, 46` | Intégrer la date du **7 avril 2026** pour la LD IA de l'AMF (`S-023`/`S-113`), actualiser les comptes à rebours vers le 1er mai 2027 (`199 jours` au 14 oct. 2026) et passer au passé composé les dates franchies d'août–septembre 2026. | Cohérence calendaire complète au 14 octobre 2026. |
| **`P2-6`** (`A-m3` à `A-m13`) | `ch. 1, 3, 15, 24, 28, 31, 38, 39, 40, 41, 43, 44, 45, 46` | Purger les 4 coquilles (`ch. 3, 15, 24, 46`), ajouter le paragraphe `T4.3` au ch. 40 `§ 40.7` et l'encadré `D-16` au ch. 41 `§ 41.9`, retirer les 2 renvois à `avant-propos` (`ch. 1, 31`), rétablir les noms propres sous la décision 18 (`ch. 38, 39, 43, 45`) et graver 1 figure SVG au ch. 28. | 50 chapitres sur 50 illustrés et purgés des périphrases de la décision 15. |

### Priorité 3 — Chantiers de fond pour une éventuelle levée future de `D-18` (`A-D1` à `A-D8` — effort estimé : `10 à 15 jours`)

1. **`P3-1` (`A-D4` / `R-IV-101`)** : Acquérir et vérifier en source primaire `[A]` la spécification **ArchiMate 4 (`The Open Group, doc C260`, 27 avril 2026)** afin de lever la réserve bloquante sur le `Tableau 44.1` (`§ 44.1.9`) et sur l'instanciation du `§ 45.14`.
2. **`P3-2` (`A-D3` / `G-6` / `A-M12`)** : Instruire et voter contradictoirement les **5 lots du chapitre 41** (`D-8`) et les **lots `L1`, `L2`, `L3` des chapitres 47 et 48** (`D-3` : `SPDX 3.0`, `CycloneDX 1.7`, `SLSA v1.2`, idempotence d'effet et compensation par sagas probabilistes), puis porter les chapitres 41, 47 et 48 à leur cible volumétrique.
3. **`P3-3` (`A-D2` / `D-9`)** : Instruire le lot transversal sur le **biais d'automatisation et la supervision humaine** au `ch. 17 § 17.5` et en répercuter les seuils aux chapitres 25 (`E-23`), 27 (`AMF`) et 40 (`§ 40.4`).
4. **`P3-4` (`A-D1`, `A-D5`, `A-D6`)** : Clore les 6 remontées ouvertes du Volume III (`G-4`), intégrer la couche d'exécution (harnais, `D-2`) dans le Livre IV (`G-5`, `ch. 43`), et exécuter le ré-adossement mécanique des 50 chapitres aux identifiants `S-001`..`S-159` (`CA-IV-01`, ramenant les rapports `P3` et `P4` de `check-compendium.py` à `0`).

---

## 11. Questions de soutenance / comité de lecture

1. **`Q1` — Statut de la couche d'exécution (harnais d'agent) dans l'architecture de référence en 6 couches (`G-5` / `D-2`)** :
   - *Enjeu sous-jacent* : Pourquoi la décision `D-2` a-t-elle logé la couche d'exécution (isolation du bac à sable, interception des appels système et des outils locaux avant même le transport `MCP`) en « cinquième horloge » au Livre V (`ch. 47 § 47.8.1`) plutôt que comme une couche ou un point de contrôle (`PC0`) à part entière de l'architecture de référence du [`chapitre 43`](Livre%20IV\43-architecture-reference-couches.md) ?
   - *Éléments de réponse attendus* : Justification de la frontière entre le point d'application réseau (`PEP` maillage / passerelle `MCP` aux `PC2`–`PC3`) et le confinateur d'exécution local (bac à sable processus/noyau), et modalités d'intégration de cette couche dans la figure `43.1` et le `Tableau 43.1`.
2. **`Q2` — Adoption de `draft-klrc-aiagent-auth` par le groupe de travail IETF WIMSE (`draft-ietf-wimse-aims-00`) et thèse du chapitre 18 (`A-B4`)** :
   - *Enjeu sous-jacent* : Le [`chapitre 18`](Livre%20II\18-know-your-agent.md) fonde une partie de son diagnostic de fragmentation sur le fait que les brouillons d'identité d'agent (`draft-klrc-aiagent-auth-00`, `draft-drake-agent-identity-registry-03`) sont des initiatives individuelles sans groupe de travail IETF rattaché. Or le groupe de travail **IETF WIMSE** a officiellement adopté ce chantier le 9 septembre 2026 sous le nom **`draft-ietf-wimse-aims-00`** (*AI Identity Management System*) (`[S]`). En quoi cette adoption modifie-t-elle l'équilibre entre SPIFFE/WIMSE et OAuth/OIDC dans le passeport d'identité du chapitre 16 ?
   - *Éléments de réponse attendus* : Analyse de la convergence entre les *Workload Identity Credentials* (`S-084`) et `AIMS` au sein de WIMSE, et maintien de la thèse sur les pièces 3 et 4 du passeport (mandat et chaîne de responsabilité) qui demeurent hors du périmètre d'authentification de WIMSE.
3. **`Q3` — Opérabilité du test à trois conditions des *frames* déterministes (ch. 29 § 29.4.1) face à une chaîne multi-agents `OO4`** :
   - *Enjeu sous-jacent* : Sous l'article 12.1 de la Loi 25, lorsque la décision finale touchant un client bancaire est prise par un humain qui valide la recommandation d'un orchestrateur `OO4` mobilisant cinq sous-agents, où s'arrête la « décision fondée exclusivement sur un traitement automatisé » si l'humain est soumis au biais d'automatisation décrit au `ch. 17 § 17.5` (`lot D-9`) ?
   - *Éléments de réponse attendus* : Articulation juridique et technique entre l'interprétation stricte de « exclusivement » par la CAI, l'exigence de revue humaine effective d'E-23/AMF, et les métriques de *délai médian de révision* et de *taux de renversement* du `ch. 40 § 40.4`.
4. **`Q4` — Arbitrage entre ArchiMate 3.2 (outillé) et ArchiMate 4 `doc C260` (normatif mais non outillé) aux chapitres 44 et 45 (`R-IV-101`)** :
   - *Enjeu sous-jacent* : Dès lors qu'à l'automne 2026 la quasi-totalité des ateliers d'architecture d'entreprise des banques canadiennes (Bizzdesign, Sparx Enterprise Architect, Ardoq, Orbus) n'échangent qu'au format Open Group Exchange File d'**ArchiMate 3.2**, pourquoi avoir indexé la validité du registre des 14 stéréotypes (`Tableau 44.1`) sur la norme **ArchiMate 4 (C260)** plutôt que de stabiliser un profil normatif ArchiMate 3.2 assorti d'une table de migration vers 4.0 ?
   - *Éléments de réponse attendus* : Défense du choix de pérennité du métamodèle ou acceptation d'un double profil `3.2 (production 2026–2027)` / `4.0 (cible)` levant immédiatement le blocage du chapitre 45.
5. **`Q5` — Compétition entre le mandat cryptographique d'`AP2` (`S-090`) et les règles d'autorisation native du rail `RTR` de Paiements Canada (`T4 2026`, ch. 33 et 36)** :
   - *Enjeu sous-jacent* : Au moment où s'ouvre la fenêtre du `T4 2026` du RTR après l'entrée en vigueur du *By-law no 10* (`DORS/2026-133`), comment une institution financière canadienne peut-elle réconcilier l'irrévocabilité immédiate d'un règlement `pacs.008` sur le RTR avec un *Intent Mandate* / *Cart Mandate* `AP2` signé hors bande par un agent dont la révocation est asynchrone ?
   - *Éléments de réponse attendus* : Démonstration du rôle du point de contrôle `PC4` (sas pré-transactionnel déterministe et séquestre temporel avant soumission au rail) et de l'incompatibilité entre révocation probabiliste et règlement temps réel irrévocable.
6. **`Q6` — Sémantique d'effet, idempotence réseau vs idempotence métier et sagas de compensation en régime probabiliste (ch. 48)** :
   - *Enjeu sous-jacent* : Le [`chapitre 48`](Livre%20V\48-semantique-effet-idempotence-compensation.md) montre qu'une clé d'idempotence `JSON-RPC` ou `HTTP` empêche la ré-exécution d'un appel identique mais n'empêche jamais un agent qui reformule son raisonnement après une erreur d'émettre un *second appel syntaxiquement distinct produisant le même effet métier*. Quelle primitive architecturale concrète permet de détecter cette équivalence d'effet avant l'exécution de l'outil ?
   - *Éléments de réponse attendus* : Définition d'une empreinte d'effet métier (*business-intent idempotency key*) calculée par le `PEP` (`PC3`) sur le triplet `(sujet_métier, ressource_cible, opération_canonique)` indépendamment de l'identifiant de requête `MCP`/`A2A`.
7. **`Q7` — Gouvernance de l'appareil probatoire : coût et bénéfice du maintien des régimes `[C]` face à l'automatisation des passes de revalidation (ch. 50)** :
   - *Enjeu sous-jacent* : La présente évaluation a montré que la passe du 2 septembre 2026 a échoué à détecter le remplacement de `draft-klrc-aiagent-auth` par `draft-ietf-wimse-aims-00` parce qu'elle interrogeait des URL d'archives statiques (`-00.txt`) (`A-B4`). Comment faire évoluer l'outillage de `PRD/` pour que le protocole en 4 étapes du `ch. 50 § 50.3` soit lui-même vérifié mécaniquement contre les API de métadonnées (Datatracker API, Crossref, W3C TR API, Gazette du Canada) ?
   - *Éléments de réponse attendus* : Conception d'un script `PRD/check-fraicheur.py` interrogeant l'API JSON du Datatracker IETF (`https://datatracker.ietf.org/api/v1/doc/document/...`) pour vérifier les champs `rev`, `expires` et `replaced_by` des brouillons cités.

---

## 12. Liste de contrôle de conformité du rapport (auto-audit)

- [x] **Couverture** : Chaque livre, chapitre (50/50), annexe (2/2), document de gouvernance (8/8) et script (22/22) du périmètre figure dans la cartographie (§ 2.1) et possède son évaluation dans les fiches analytiques (§ 4.1 à § 4.7) ainsi que dans [`audit.md`](audit.md).
- [x] **Preuves** : Chaque constat positif (§ 7) ou négatif (§ 8) cite au moins un fichier, une section ou un numéro de ligne précis et porte son marqueur épistémique (`[L]`, `[R]`, `[S]`, `[D]`).
- [x] **Calculs** : La moyenne pondérée du tableau § 1.2 est mathématiquement exacte (`14,5 × 0,20 + 14,0 × 0,15 + 15,5 × 0,15 + 17,5 × 0,15 + 17,0 × 0,15 + 16,0 × 0,10 + 19,0 × 0,10 = 2,90 + 2,10 + 2,325 + 2,625 + 2,55 + 1,60 + 1,90 = 16,00 / 20`, somme des poids = `100 %`).
- [x] **Exécution** : Tous les scripts de vérification du projet ont été exécutés (`[R]`) et leurs sorties exactes sont consignées en Annexe A.
- [x] **Confrontation externe** : Les références critiques et sensibles au temps ont été vérifiées par rapport à l'état de l'art réel au **14 octobre 2026** (`[S]`) et consignées en § 6 et en Annexe B.
- [x] **Actionnabilité** : Chaque faiblesse identifiée au § 8 possède une contrepartie concrète dans la feuille de route de remédiation (§ 10).
- [x] **Indépendance critique** : Le ton demeure analytique, courtois, sans complaisance ni sévérité gratuite, et respecte scrupuleusement le niveau d'exigence doctoral fixé par le [`Gabarit d'évaluation académique.md`](../Gabarit%20d'évaluation%20académique.md) (v1.0).

---

## Annexe A — Journal des commandes de vérification exécutées (`[R]`)

Toutes les commandes ci-dessous ont été exécutées le **14 octobre 2026** depuis `c:\Users\agbru\Github\Agentique\2 - Compendium` sur le commit `8b2cf08dcca6f0adf3dd7fb6c76664407b9ea2c9` (`corpus-v1.0`) :

```text
$ python PRD/check-toc.py
OK — tous les contrôles passent (C1-C16). [exit 0]

$ python PRD/check-toc-mutations.py
OK — les 25 mutations sont toutes attrapées (M1-M16b). [exit 0]

$ python PRD/check-sieges.py
OK — les 26 sièges tiennent sur 50 pièces (S1-S5). [exit 0]

$ python PRD/check-sieges-mutations.py
OK — les 115 mutations sont toutes attrapées (M1-M12). [exit 0]

$ python PRD/check-compendium.py
OK — les 50 pièces tiennent (P1-P10), 5 rapport(s) déclaratif(s) :
  - P3 (emplois F-xx/H-xx nus en pièce mixte) : 524 emploi(s) sur 26 pièce(s)
  - P4 (entrées exclues ou hors socle consolidé) : 23 citation(s) (F-92, F-96, H-15)
  - P9 (inventaire R-IV-*) : 106 ouverture(s) de R-IV-01 à R-IV-112, 0 collision(s)
  - P5 (écarts de convention de soustraction) : 4 cardinal(aux) sur 3 pièce(s) (ch. 39, 40, 43)
  - P5 (écarts déclaratifs résiduels) : 4 cardinal(aux) sur 2 pièce(s) (ch. 48, 49) [exit 0]

$ python PRD/check-compendium-mutations.py
OK — les 30 mutations sont toutes attrapées. [exit 0]

$ python PRD/reporter-volumetrie.py --verifier
OK — 333 416 mots de corps, les trois sites concordent. [exit 0]

$ bash PRD/decompte.sh --registre
OK — les cinquante lignes du registre tiennent contre la mesure. [exit 0]

$ bash PRD/decompte.sh --verifier
ÉCART Vol. I wc -w brut : 241260 (attendu 233257)
ÉCHEC : 1 écart(s) sur les points d'ancrage. [exit 1 — Constat A-B2]

$ LC_ALL=C bash PRD/decompte.sh --verifier
OK — les quatre points d'ancrage sont tenus. [exit 0]

$ python build/verifier-piece.py
ÉCART Livre II/14-grille-cinq-questions.md :
  première différence à la ligne 677 :
    attendu : <table style="width:99%;">
    obtenu  : <table style="width:100%;">
ÉCART Livre IV/37-maillage-agents-point-application.md :
  première différence à la ligne 740 :
    attendu : <table style="width:99%;">
    obtenu  : <table style="width:100%;">
ÉCHEC — 2 divergence(s) sur 50 pièce(s). [exit 1 — Constat A-B1]

$ python build/verifier-piece-mutations.py
Temps 1 : 2 écart(s), sortie 1
ÉCHEC — le temps 1 doit passer avant de muter. [exit 1 — Constat A-B1]

$ python build/assemble-bibliographie.py --verifier
OK — 1154 entrées uniques, 109 doublons fondus. [exit 0]

$ python figures/genere.py --verifier
[figures] 118 figures du volume : 115 gravées sur 49 pièces, 3 antérieures au programme vérifiées à l'empreinte [exit 0]

$ python ../Python/check-renvois.py
OK — 238 .md, 2810 renvois relatifs (dont 439 à fragment), 0 mort(s), 1 toléré(s). [exit 0]

$ python ../Python/check-lisibilite.py
OK — les 18 pages d'accueil tiennent les seuils. [exit 0]

$ python "../3 - Veille/Python/check-resume.py" Compendium.pdf
Compendium.pdf : 1000 page(s) (budget 1000), derniere ligne a y=616.0/666.0 pt, degagement +21.5 pt [OK] [exit 0]
```

---

## Annexe B — Références externes mobilisées par l'évaluateur (`[S]`)

1. **IETF Datatracker — Groupe de travail WIMSE & AI Identity Management System (AIMS)** : `https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/` (révisions `-00` du 2026-03-26 à `-03` du 2026-07-06 ; adoption WIMSE le 2026-09-09) et `https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/` (`draft-ietf-wimse-aims-00` publié le **2026-09-15**, échéance 2027-03-19) — consultés le 14 octobre 2026 (`[S]`).
2. **IETF Datatracker — OAuth 2.1 Authorization Framework** : `https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/` (`draft-ietf-oauth-v2-1-16` publié le **2026-09-02**, 193 pages ; jalon WG OAuth : soumission IESG en décembre 2026) — consulté le 14 octobre 2026 (`[S]`).
3. **IETF Datatracker — WIMSE Workload Identity Credentials & AI Agents** : `https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-creds/` (`-00` / `-01`) et `https://datatracker.ietf.org/doc/draft-klrc-wimse-ai-agents/` (`-00` publié le 2026-02-28, **expiré le 2026-09-01**) — consultés le 14 octobre 2026 (`[S]`).
4. **IETF Datatracker — Agent Identity Registry & OpenID Agent Identity** : `https://datatracker.ietf.org/doc/draft-drake-agent-identity-registry/` (`-03` du 2026-05-23, échéance 2026-11-24) et `https://datatracker.ietf.org/doc/draft-sharif-openid-agent-identity/` (`-01` du 2026-08-26, échéance 2027-02-27) — consultés le 14 octobre 2026 (`[S]`).
5. **W3C Technical Reports — Verifiable Credentials 2.0, DID v1.1 & RDF 1.2 / SHACL 1.2 / SPARQL 1.2** : W3C Recommendation *Verifiable Credentials Data Model v2.0* (15 mai 2025), W3C Recommendation *Decentralized Identifiers (DIDs) v1.1* (19 mai 2026), et Candidate Recommendations W3C *RDF 1.2*, *SPARQL 1.2*, *SHACL 1.2* (2026) — vérifiés le 14 octobre 2026 (`[S]`).
6. **NIST Post-Quantum Cryptography** : `FIPS 203` (ML-KEM), `FIPS 204` (ML-DSA), `FIPS 205` (SLH-DSA) (13 août 2024), annonce de sélection de `HQC` (mars 2025) et `NIST IR 8547` (*Transition to Post-Quantum Cryptography Standards*, Initial Public Draft, novembre 2024) — vérifiés le 14 octobre 2026 (`[S]`).
7. **Bureau du surintendant des institutions financières (BSIF / OSFI) & Autorité des marchés financiers (AMF)** : BSIF, *Ligne directrice E-23 — Gestion du risque de modélisation à l'échelle de l'entreprise* (publiée le 11 septembre 2025, entrée en vigueur le **1er mai 2027**) ; AMF (Québec), *Ligne directrice sur l'utilisation de l'intelligence artificielle* (publiée le **7 avril 2026**, entrée en vigueur le **1er mai 2027**) — vérifiées le 14 octobre 2026 (`[S]`).
8. **Paiements Canada & Gazette du Canada** : *Règlement administratif no 10 sur le système de paiement en temps réel (RTR)* (`DORS/2026-133`, enregistré le 16 juin 2026, entré en vigueur le **24 août 2026**), consultation de 30 jours ouverte le 24 août 2026 (close en septembre 2026) et fenêtre cible d'essais/lancement du **`T4 2026`** (ouverte le 1er octobre 2026) ; *Loi sur les activités bancaires axées sur les consommateurs* (`L.C. 2026, ch. 6`, sanctionnée le 26 mars 2026) — vérifiés le 14 octobre 2026 (`[S]`).
9. **Spécifications protocolaires agentiques et observabilité** : Model Context Protocol (`MCP`, spécification stable `2025-11-25` et feuille de route SEPs du `2026-07-28`), Agent2Agent (`A2A v0.3.0`, Linux Foundation), Agent Payments Protocol (`AP2`, Linux Foundation, 28 avril 2026), OpenTelemetry *Semantic Conventions for Generative AI Systems* (`v1.37`–`v1.40`, statut `Development`), OWASP *Top 10 for Agentic Applications* (`décembre 2025 / 2026`) — vérifiés le 14 octobre 2026 (`[S]`).
10. **Littérature scientifique primaire** : Nassi et coll., *The Promptware Kill Chain* (`arXiv:2601.09625`) ; Cemri et coll., *Why Do Multi-Agent LLM Systems Fail?* (`MAST`, `arXiv:2503.13657`, ICLR 2025 / NeurIPS 2025 Datasets & Benchmarks) ; Krishnan, *Advancing Multi-Agent Systems Through Model Context Protocol* (`arXiv:2504.21030`) ; Habler et coll., *Building A Secure Agentic AI Application Leveraging A2A Protocol* (`arXiv:2504.16902`) ; Ehtesham et coll., *A Survey of Agent Interoperability Protocols: MCP, ACP, A2A, and ANP* (`arXiv:2505.02279`) — vérifiés le 14 octobre 2026 (`[S]`).

---

## Déclaration de l'évaluateur

Je soussigné, évaluateur académique et auditeur d'ingénierie logicielle, atteste que la présente évaluation universitaire du *Compendium* (Volume IV du corpus *Agentique*, étiquette `corpus-v1.0`, commit `8b2cf08dcca6f0adf3dd7fb6c76664407b9ea2c9`) a été conduite le **14 octobre 2026** en toute indépendance critique, sur la base de la lecture intégrale (`[L]`) de 100 % des 50 chapitres, des annexes, des pièces de gouvernance et des scripts, de l'exécution directe (`[R]`) de l'ensemble de la chaîne de vérification et de mutation, et de la confrontation aux sources primaires externes (`[S]`). Aucun fichier suivi du dépôt n'a été altéré au cours de l'audit.
