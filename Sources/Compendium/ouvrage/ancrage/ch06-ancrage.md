# Journal d'ancrage atomique Wyvern — Chapitre 06 (`Chapitre 06.md`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/02 - Partie II/Chapitre 06.md` (`ch06`)
- **Agent auditeur :** `wyvern-b2-1` (auditeur atomique Wyvern neuf, barrière `G2` selon `AO-07`)
- **Base fermée autorisée :** `Compendium/ouvrage/sources/ch06-sources.md` (`[1]`–`[8]`), textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt`, registres `Compendium/ouvrage/registre/*.json`, exclusions `Compendium/ouvrage/recherche/registre-statut-f.json`, spécifications `Compendium/ouvrage/specs/{manifest.json,protocole-mlr-compendium.json}`, rapport `Compendium/ouvrage/aq/rapports-g0.json`, schéma `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/schemas/adr_2027_b001.schema.json` et renvois internes vérifiés dans `Corpus/Tome 1..8*.md`
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Passe G2 initiale (supportés)** : 33 affirmations atomiques validées sans retouche sur `51` auditées (`18` rectifiées directement dans `Chapitre 06.md`)
- **Actions appliquées dans `Chapitre 06.md` :** correction du renversement sur `EXIG-GOV-16` (`90` jours au plus par délégation à l'architecture d'entreprise pour un agent de *classe faible* plutôt que pour des écarts critiques), remplacement des sept libellés anglais absents du corpus par les sept états officiels du registre (`proposé`, `en conception`, `en construction`, `pilote`, `production`, `suspendu`, `retiré` selon `CAD26 § 11.2` et `CH-32`, cible `< 10` s), précision de l'échelonnement des `42` capacités invariantes sans regret (`29` en `Palier 1` et `13` en `Palier 2` d'après `Tome 4 Annexe B`), séparation explicite entre les `9` clauses de négociation du Tome 3 et les `10` clauses contractuelles minimales `EXIG-APP-07` à `EXIG-APP-16` (avec retrait de la mention non fondée de « rang 4 » au profit de l'avis écrit de sous-traitance de `BSIF B-10`), réancrage doctrinal du *Data Act* `(UE) 2023/2854` sur `ANC-003` / `Tome 3 § 27.5`, alignement du paragraphe `2027-B001` sur le schéma réel `schemas/adr_2027_b001.schema.json` (`L0`–`L4`, `minimum_eval_gate`) et les huit critères EA `C01`–`C08` (`Tome 6 Annexe B.2`), correction de la matrice `LCIM` sur cinq paliers (`Tome 1 Tableau 7.1`, incluant le palier *dynamique*), ajout des critères intermédiaires d'arbitrage `CAD26 § 4.3`, qualification du banc synthétique `Borealis-Bench` et de la portée exacte des exclusions `statut F` de `ch06-sources.md` face aux guides `TOGAF 10 ADM`.
- **Verdict final — supportés** : 53 / 53 (100,0 %)

---

## 1. Synthèse de la vérification par section

| Section (`Chapitre 06.md`) | Affirmations auditées | Initialement conformes | Écarts rectifiés ou réancrés | Actives finales (`100,0 %`) |
| --- | :---: | :---: | :---: | :---: |
| En-tête, `6.1` et Trois invariants (`L1–L17`) | 7 | 5 | 2 (`C06-04`, `C06-07`) | 7 |
| `6.2.1` Fermeture `DIV-02`, noyau `42 CAP` et `12 DEC` (`L21–L107`) | 23 | 12 | 11 (`C06-10`, `C06-11`, `C06-14`..`C06-16`, `C06-20`..`C06-23`, `C06-27`, `C06-28`) | 23 |
| `6.2.2` Six couches, arbitrage, outils et `S_ready` (`L109–L164`) | 17 | 14 | 3 (`C06-33`, `C06-37`, `C06-42`) | 17 |
| `6.3` Exigences, interfaces et livrables (`L166–L187`) | 4 | 2 | 2 (`C06-48`, `C06-49`) | 4 |
| **Total** | **51** | **33** | **18** | **51** |

---

## 2. Journal détaillé des affirmations atomiques (`C06-01` à `C06-51`)

### 2.0 En-tête, section `6.1` et encadré des trois invariants (`L1–L17`)

- **C06-01 (`L1`, `L3`) :** Titre et question directrice posant l'unification des découpages en un noyau de contrôle déterministe possédé (`42` capacités invariantes et `12` décisions neutres), l'arbitrage normatif, le diagnostic patrimonial et la réversibilité contractuelle.
  - Preuve vérifiée : `specs/manifest.json` (`ch06`), `prd.md` (`CH-06`), `plan.md` (`CH-06`).
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-02 (`L7`) :** L'obsolescence rapide des trousses `SDK` (souvent remaniées en moins de douze mois) et la captivité des suites infonuagiques fermées sur le plan de contrôle justifient la sanctuarisation du **noyau de contrôle déterministe** dans le domaine `D02` / `SUB_D02_03`.
  - Preuve vérifiée : `specs/manifest.json`, `registre/glossaire-termes.json` (`noyau de contrôle déterministe`), `Corpus/Tome 3 § 27.1`, `Corpus/Tome 4 § 11.2`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-03 (`L9`) :** L'architecture clôt la divergence `DIV-02` en soudant `C1`–`C5` et `Plans A`–`C` aux six vraies couches de `CAD26 § 5.2–5.3`, réconcilie les quatre plans SI et les quatre plans du noyau possédé sous `DISC-03` et assure la compatibilité `ArchiMate 3.2` / `4.0` (`C260`) sous `DISC-04`.
  - Preuve vérifiée : `registre/concordance-taxonomies.json` (`div_02`, `DISC-03`, `DISC-04`), `Corpus/Tome 5 § 2.4`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-04 (`L11`) :** Délimitation de `42` capacités invariantes sans regret face à `10` conditionnelles sur `SIG-*`, conversion des `31 ADR` en `12 DEC`, hiérarchie `PRIN-01..12` et `PRI-001..015`, diagnostic `S_ready` et dix clauses contractuelles de sortie vérifiables.
  - Preuve vérifiée : `Corpus/Tome 4 § 11.2–11.3, § 13.2–13.3`, `Corpus/Tome 2 § 4.1, § 13.3` (`EXIG-APP-07..16`).
  - Passe initiale : écart rectifié · Action : reformulée `neuf clauses de sortie` en `dix clauses contractuelles de sortie` pour concorder avec `EXIG-APP-07` à `EXIG-APP-16` · Verdict : supporté
- **C06-05 (`L15`) :** Premier invariant exécutable (`42 CAP`, `EXIG-ARC-01`, `EXIG-ARC-19`, `EXIG-GOV-07..08`) : l'effectivité du noyau possédé exige cumulativement un chemin réseau `PEP` obligé, un registre central à sept états distinct du catalogue de découverte et une preuve immuable hors modèle.
  - Preuve vérifiée : `Corpus/Tome 2 L1315–L1325, L5406`, `Corpus/Tome 4 L2777–L2789`, `prd.md L1288`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-06 (`L16`) :** Deuxième invariant exécutable (`EXIG-ARC-20`, `PRI-003`) : tout `ABB` pointe vers un `SBB` révisé trimestriellement, les conflits cèdent devant `CAD26 § 4.3` et les `16 ADR` couplées à des éditeurs sont remplacées par `DEC-001` à `DEC-012` au gabarit `2027-B001`.
  - Preuve vérifiée : `Corpus/Tome 2 L995–L996, L1327–L1331`, `Corpus/Tome 4 L3027–L3083`, `Tome 8/trousse/schemas/adr_2027_b001.schema.json`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-07 (`L17`) :** Troisième invariant exécutable (`BSIF B-10` `[4]`, `c_sec ≥ 60`) : nul système patrimonial n'accède à l'écriture `L2+` si `S_ready < 50` ou `c_sec < 60`, et les actifs portables sous `Git` sont protégés par les dix clauses contractuelles minimales (`EXIG-APP-07` à `EXIG-APP-16`) éprouvées annuellement.
  - Preuve vérifiée : `SRC-068.txt` (`BSIF B-10 § 2.3.5`), `Corpus/Tome 3 L22583–L22587`, `Corpus/Tome 2 L6375–L6452`.
  - Passe initiale : écart rectifié · Action : reformulée la mention de neuf clauses en `dix clauses contractuelles minimales (EXIG-APP-07 à EXIG-APP-16)` · Verdict : supporté

### 2.1 Section `6.2.1` — Fermeture `DIV-02`, noyau possédé (`42 CAP`), clauses de sortie et `12 DEC` (`L21–L107`)

- **C06-08 (`L23`) :** La fermeture de `DIV-02` corrige trois erreurs d'alignement (`C5 modeles` en Couche 3 `CAD26`, absence de Couche 3 « Connaissance » dont `C3` agrège les Couches 2, 3 et 5, et `SoR` en Couche 6 sous `C4 acces`) ; la prose renvoie les quatre rectifications éditoriales associées de `CAD26 v1.2` à la concordance générale (`→ Chapitre 36`).
  - Preuve vérifiée : `registre/concordance-taxonomies.json L9–L19`, `Corpus/Tome 5 § 2.4`.
  - Passe initiale : conforme · Action : reformulation post-G5 renvoyant le détail des 4 coquilles `CAD26 v1.2` vers `→ Chapitre 36` · Verdict : supporté
- **C06-09 (`L25–L36`, Tableau 6.1) :** Table de concordance fermant `DIV-02` entre les cinq couches `C1`–`C5` + trois volets `Plans A`–`C`, `CAD26 § 5.2–5.3` et les `52` capacités `CAP-001` à `CAP-052`.
  - Preuve vérifiée : `registre/concordance-taxonomies.json L37–L101`, `Corpus/Tome 4 L5249–L5307`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-10 (`L38`) :** `100,0 %` des composants soumis en `ARB` démontrent leur raccordement `ABB → SBB` sur standards ouverts (`EXIG-ARC-20`, `EXIG-GOV-18`), avec révision trimestrielle et plafonnement de toute dérogation à six mois au plus (ou `90` jours au plus par délégation à l'architecture d'entreprise pour un agent de classe faible sous `EXIG-GOV-16`).
  - Preuve vérifiée : `Corpus/Tome 2 L1009, L1327–L1331`, `Corpus/Tome 5 L395`.
  - Passe initiale : écart rectifié · Action : corrigé `90 jours pour les écarts critiques` en `90 jours au plus par délégation à l'architecture d'entreprise pour un agent de classe faible` conformément à `EXIG-GOV-16` · Verdict : supporté
- **C06-11 (`L40`) :** `DISC-04` assure la compatibilité bidirectionnelle `ArchiMate 3.2` / `4.0` (`C260`, `27 avril 2026`), rappelle que les manuels propriétaires `TOGAF 10 ADM` demeurent hors évidence probante ouverte (`statut F` doctrinal, zéro artefact commercial exigé en `G0`), et impose par `Specialization` / `W172` de typer `«Cognitive Actor»` en `Application Component` et jamais en `Business Actor`.
  - Preuve vérifiée : `registre/concordance-taxonomies.json L255–L271`, `Corpus/Tome 1 L10062`, `Corpus/Tome 6 L594, L609`, `Corpus/Tome 5 L372`.
  - Passe initiale : écart rectifié · Action : reformulé le classement de `TOGAF 10 ADM` comme hors évidence probante ouverte (`statut F` doctrinal) afin de le distinguer des blocages HTTP consignés dans `registre-statut-f.json` · Verdict : supporté
- **C06-12 (`L42`) :** Les sept patrons de modélisation (`Tome 1 § 44.1.2–44.1.8`) relient `«Cognitive Actor»`, `«Guardrail Policy»` et `«Human-on-the-Loop»` à la couche applicative, interdisent tout `Flow` contournant l'approbateur humain et exigent zéro `«regulatory-requirement»` orpheline le long de `Driver → Assessment → Requirement → Exécution`.
  - Preuve vérifiée : `Corpus/Tome 1 L10134–L10168`, `Corpus/Tome 5 L372`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-13 (`L44–L46`, Figure 1) :** Schéma `SCH-06-01.svg` présentant la fermeture `DIV-02`, le modèle à cinq couches et trois volets, `ArchiMate 4.0` et `PC1–PC5`.
  - Preuve vérifiée : `specs/manifest.json`, `schemas/SCH-06-01.svg`, `schemas/rendus/SCH-06-01.svg`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-14 (`L48–L52`) :** Sanctuarisation du **noyau de contrôle déterministe** — en cohérence avec les garde-fous techniques (*AI harnessing*) du bulletin technologique BSIF `[5]` — reposant sur trois conditions non dérogeables (`EXIG-ARC-01`, `EXIG-GOV-07`, `EXIG-GOV-08`, `EXIG-OBS-11`, `EXIG-OBS-12`) : chemin réseau `PEP` obligé, registre central à sept états distinct du catalogue, preuve immuable hors modèle.
  - Preuve vérifiée : `SRC-066.txt L27, L65, L175`, `registre/glossaire-termes.json L255–L260`, `Corpus/Tome 2 L1315, L5406, L4956`.
  - Passe initiale : écart rectifié · Action : ancré explicitement le concept de *harnessing* / noyau de contrôle sur `SRC-066` (`[5]`) · Verdict : supporté
- **C06-15 (`L54`) :** Distinction entre catalogue de découverte et registre d'autorité à sept états (`proposé`, `en conception`, `en construction`, `pilote`, `production`, `suspendu`, `retiré` selon `CAD26 § 11.2` et `CH-32`), conditionnant l'accès réseau et l'émission de jetons, avec blocage rapide (`cible < 10` s) sur bascule à `suspendu` ou `retiré`.
  - Preuve vérifiée : `Corpus/Tome 2 L5392`, `Chapitre 32.md L52`, `registre/matrice-exig-prr-c40.json` (`CAP-039`, `CAP-047`).
  - Passe initiale : écart rectifié · Action : remplacé les sept états anglais absents du corpus (`PROPOSED`, `VALIDATED`, etc.) par les sept états normatifs de `CAD26 § 11.2` et précisé la cible `< 10` s · Verdict : supporté
- **C06-16 (`L56`) :** Sous `DISC-03`, convergence des quatre plans SI (`Tome 6 C03`), des quatre plans possédés (`Tome 7`), de `Plans A`–`C` et des quatre modules du `Tome 8` (`PRI-015`, `DEC-007`), avec sanctuarisation des `42` capacités invariantes sans regret sur `A`, `B`, `C` (`29` en `P1` et `13` en `P2`, soit `17` de plan de contrôle pur et `25` points de coupure).
  - Preuve vérifiée : `registre/concordance-taxonomies.json L231–L253`, `Corpus/Tome 4 L2777–L2787, L5249–L5307` (`29` `P1` et `13` `P2` vérifiées).
  - Passe initiale : écart rectifié · Action : réancré l'échelonnement `29` en `P1` / `13` en `P2` (au lieu d'un financement unique dès `P1`) et scindé la phrase pour respecter `CA-05` · Verdict : supporté
- **C06-17 (`L58`) :** Les `10` capacités conditionnelles (`CAP-004`, `006`, `013`, `014`, `025`, `027`, `028`, `033`, `034`, `041`) reçoivent uniquement une interface légère préparatoire et s'activent sur signal `SIG-*` (`A`, `B`, `C`), tandis que cinq capacités (`CAP-025`, `028`, `033`, `046`, `052`) comblent les lacunes de 2026.
  - Preuve vérifiée : `registre/concordance-taxonomies.json L24–L30`, `Corpus/Tome 4 L2797–L2825`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-18 (`L60`) :** Gravité des données (`≥ 85 %` d'exécution locale près des données métiers), confinement des agents `SaaS` mono-silo sous `EXIG-ARC-21` et rapatriement de l'orchestration inter-silos dans le moteur durable avec étiquette immuable d'entité juridique (`EXIG-CON-06`).
  - Preuve vérifiée : `Corpus/Tome 3 L14145`, `Corpus/Tome 2 L1335`, `Corpus/Tome 5 L379, L386`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-19 (`L62`) :** Découplage des quatre plans SI et des quatre plans du noyau possédé (`DISC-03`) empêchant une plateforme commerciale de cumuler exécution métier et détention des journaux, clés et règles.
  - Preuve vérifiée : `registre/concordance-taxonomies.json L231–L253`, `Corpus/Tome 3 L14046–L14047`, `Corpus/Tome 7 L634–L695`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-20 (`L64`) :** Gouvernance financière distinguant le socle incompressible sans regret (`29` capacités fondatrices au `Palier 1`, dont `NHI`, `PEP` et double couloir, puis `13` compléments au `Palier 2`) du coût marginal nul des interfaces d'attente des `10` capacités conditionnelles.
  - Preuve vérifiée : `Corpus/Tome 4 L2797–L2801, L5249–L5307`, `Corpus/Tome 5 L121–L126`.
  - Passe initiale : écart rectifié · Action : précisé la ventilation budgétaire `29` fondatrices en `P1` et `13` compléments en `P2` · Verdict : supporté
- **C06-21 (`L66`) :** Distinction formelle **interchangeabilité** (`MCP`, `A2A`, `Open Responses`) / **transférabilité** et classement des sept classes d'actifs : cinq sous `Git` interne (`AGENTS.md` pour agents de programmation, `SKILL.md` rattachées à l'`AAIF` le `22 octobre 2026`, gabarits d'invites, `JSON Schema` `[7]`, suites `EvalOps`) contre deux captives par défaut (mémoire reconstruite des sources, configuration d'éditeur).
  - Preuve vérifiée : `Corpus/Tome 3 L14013–L14035`, `Corpus/Tome 2 L8214`, `SRC-021.txt` (`[7]`).
  - Passe initiale : écart rectifié · Action : précisé le périmètre d'`AGENTS.md` (agents de programmation) et la date exacte `22 octobre 2026` du rattachement `AAIF` · Verdict : supporté
- **C06-22 (`L68`) :** Convergence entre `BSIF B-10` `[4]` (inventaire des sous-traitants, continuité, plans de sortie ordonnée et sous contrainte) et les repères du Chapitre VI du Règlement `(UE) 2023/2854` (*Data Act*, consigne doctrinale `ANC-003` du `Tome 3 § 27.5` sans texte intégral `L+` propre dans `ch06-sources.md`, `12 septembre 2025`, transition de `30` jours civils à `7` mois, interdiction des frais au `12 janvier 2027`, sous clause `non-avis`).
  - Preuve vérifiée : `SRC-068.txt` (`A3`, `2.2.4`, `2.3.5`), `registre/ancres-chronologiques.json` (`ANC-003`), `Corpus/Tome 3 L14057`.
  - Passe initiale : écart rectifié · Action : réancré explicitement le *Data Act* sur la consigne doctrinale `ANC-003` / `Tome 3 § 27.5` et la clause `non-avis` en l'absence de texte intégral `L+` autonome dans `ch06-sources.md` · Verdict : supporté
- **C06-23 (`L70`) :** Articulation des neuf clauses de négociation du Tome 3 (`Figure 2`) et de leur consolidation en **dix clauses contractuelles minimales** (`EXIG-APP-07` à `EXIG-APP-16`, `CH-27`) : exportabilité, assistance, suppression des frais, avis écrit préalable en cas de recours ou de substitution de sous-traitant (`BSIF B-10` `[4]`), journaux, clés, effacement, ségrégation et essai annuel de bascule (`POR-016`).
  - Preuve vérifiée : `Corpus/Tome 3 L14067–L14076`, `Corpus/Tome 2 L6375–L6452`, `SRC-068.txt L339`, `Chapitre 27.md L51–L74`, `registre/matrice-exig-prr-c40.json` (`POR-016`).
  - Passe initiale : écart rectifié · Action : distingué les `9` clauses de négociation des `10` clauses `EXIG-APP-07`–`EXIG-APP-16` et remplacé la mention sans appui de `rang 4` par l'avis écrit de recours ou substitution de sous-traitant (`BSIF B-10`) · Verdict : supporté
- **C06-24 (`L72–L74`, Figure 2) :** Schéma `SCH-06-02.svg` illustrant la possession du noyau (`42` capacités invariantes par rapport à `10` sur signal), la gravité des données et les neuf clauses de sortie.
  - Preuve vérifiée : `specs/manifest.json`, `schemas/SCH-06-02.svg`, `schemas/rendus/SCH-06-02.svg`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-25 (`L76–L80`) :** Ventilation `8 / 7 / 16` des `31 ADR` (`ADR-001` à `ADR-031`) : `8` maintenues (`001`, `002`, `003`, `008`, `011`, `017`, `025`, `029`), `7` sous veille `SIG-*` (`004`, `005`, `018`, `021`, `024`, `027`, `031`), `16` remplacées par `DEC-001` à `DEC-012`.
  - Preuve vérifiée : `Corpus/Tome 4 L3027–L3066`, `Corpus/Tome 5 L1858–L1893`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-26 (`L82–L97`, Tableau 6.2) :** Conversion exacte des `16 ADR` en `12 DEC` (`DEC-001` à `DEC-012`) avec objet fonctionnel neutre et rattachement exact aux capacités `CAP`.
  - Preuve vérifiée : `Corpus/Tome 4 L3067–L3083`, `Corpus/Tome 5 L1894–L1909`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-27 (`L99`) :** Matérialisation en intégration continue par `2027-B001` (`schemas/adr_2027_b001.schema.json`, extrait `G0-EX-CH04-03` inspecté au `CH-34`), validant `L0`–`L4` (aligné sur `N0`–`N4`), l'empreinte réglementaire (`BSIF E-23`, `Loi 25`, `EU AI Act`), le plafond `CPO`, le critère minimal d'évaluation (illustré par `pass^5` en YAML) et le coupe-circuit `SOC`, en appui à `PRR-75` et aux huit critères `EA` `C01` à `C08`.
  - Preuve vérifiée : `Tome 8/trousse/schemas/adr_2027_b001.schema.json`, `aq/rapports-g0.json L170–L175`, `Corpus/Tome 3 L28418–L28451`, `Corpus/Tome 6 L5011–L5018`.
  - Passe initiale : écart rectifié · Action : rectifié le champ `autonomy_ceiling` (`L0`–`L4` dans le schéma JSON), la portée de `minimum_eval_gate`, le contenu exact des huit critères `EA` `C01`–`C08` (en retirant résilience/confinement qui relèvent des critères suivants) et scindé la phrase pour `CA-05` · Verdict : supporté
- **C06-28 (`L101`) :** Consignation des réserves d'alignement issues de la révision du corpus (dont la neutralisation des seize `ADR` couplées), mentions obligatoires (juridiction, date de révision, `SIG-*`, preuves de tests) et blocage automatique en intégration continue en cas d'omission ou non-conformité (`CPO`, coupe-circuit `SOC` ou propriétaire métier nominatif).
  - Preuve vérifiée : `Corpus/Tome 3 L28303–L28340, L28450`, `Corpus/Tome 4 L3027–L3064`, `prd.md L1312`.
  - Passe initiale : écart rectifié · Action : reformulé la référence aux réserves d'alignement et au déclencheur réel du blocage CI/CD (`Tome 3 § F.4`), tout en levant la collision `12-grammes` (`CA-03`) · Verdict : supporté
- **C06-29 (`L103`) :** L'articulation `8 / 7 / 12` évite à la fois de figer un cadriciel éphémère et de laisser chaque équipe réinventer résilience, identité et journalisation, préservant la substituabilité des fournisseurs d'inférence.
  - Preuve vérifiée : `Corpus/Tome 4 § 13.2–13.3`, `Corpus/Tome 5 Annexe B.2–B.3`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-30 (`L105–L107`, Figure 3) :** Schéma `SCH-06-03.png` illustrant la pyramide d'arbitrage (`12 PRIN` / `15 PRI`) et la conversion des `31 ADR` de 2027 en `12 DEC`.
  - Preuve vérifiée : `specs/manifest.json`, `schemas/SCH-06-03.mmd`, `schemas/rendus/SCH-06-03.png`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté

### 2.2 Section `6.2.2` — Six couches, principes d'arbitrage, ergonomie d'outils et `S_ready` (`L109–L165`)

- **C06-31 (`L111`) :** Vue du Tome 3 à six couches horizontales et deux piliers transversaux (*Zero-Trust / NHI* et *AgentOps / FinOps*), situation par rapport à `Lu et coll.`, `Megagon`, `SALLMA`, `CSA` et `Futurum`, et inscription de la non-substituabilité `PRI-003` entre outil vertical (`MCP`) et pair horizontal (`A2A`).
  - Preuve vérifiée : `Corpus/Tome 3 L595, L11899, L12334, L12377`, `Corpus/Tome 4 L5318`, `prd.md L1329`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-32 (`L113`) :** Synthèse du Tome 1 (`Tableau 43.1`) fusionnant les vues à quatre et trois couches en six strates unifiées, levant la collision terminologique entre fabrique d'identités et fabrique d'agents, et positionnant cinq points de contrôle opposables `PC1`–`PC5`.
  - Preuve vérifiée : `Corpus/Tome 1 L9857–L9950`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-33 (`L115`) :** Affectation de `PC1` (`Loi 25` art. `12.1`), `PC2` (`Z1`), `PC3` (`Z2`), `PC4` (`Z3`, `ACVM 11-348` et `BSIF E-23` `[6]`), `PC5` (`Z5`), couche d'abstraction `Z4`, et matrice `LCIM` retenue sur cinq paliers en pile agentique (`Tome 1, Tableau 7.1` : technique, syntaxique, sémantique, pragmatique et dynamique).
  - Preuve vérifiée : `Corpus/Tome 1 L1757–L1766, L9934–L9944`, `Corpus/Tome 5 L1728`, `SRC-065.txt`.
  - Passe initiale : écart rectifié · Action : corrigé `quatre paliers` vers les `cinq paliers` retenus au `Tableau 7.1` du Tome 1 (ajout du palier `dynamique`) · Verdict : supporté
- **C06-34 (`L117`) :** Langage commun entre architectes, juristes et exploitation grâce à l'ancrage de chaque point de contrôle à une frontière logicielle précise (`Z1` à `Z5`) sans passeport d'agent propriétaire.
  - Preuve vérifiée : `Corpus/Tome 1 L9946–L9948`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-35 (`L119`) :** Alignement `PRIN-01..12`, `PRI-001..015` et `10` décisions `CAD26`, vérification trimestrielle `ABB → SBB` (`EXIG-ARC-20`, `EXIG-GOV-18`), refus des promesses verbales d'éditeur et réouverture en comité lors du basculement d'un signal `SIG-*`.
  - Preuve vérifiée : `Corpus/Tome 5 L1838–L1857`, `Corpus/Tome 2 L1327–L1331`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-36 (`L121–L128`) :** Organisation des douze principes directeurs `PRIN-01` à `PRIN-12` (`CAD26` ch. 4) en six paires complémentaires, incluant `PRIN-03` (moindre privilège et moindre agence repris en `OWASP` `[8]`).
  - Preuve vérifiée : `Corpus/Tome 2 L837–L964`, `SRC-055.txt L238, L382, L489`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-37 (`L130`) :** Ordre de préséance strict (`CAD26 § 4.3`) : droit applicable > dix interdits `EXIG-GOV-17` > `DOIT` sur `DEVRAIT` > source unique désignée sur renvoi > disposition spéciale sur disposition générale > bloc de protection (`PRIN-03..07, 10, 12`) > bloc architectural (`PRIN-01, 02, 08, 09, 11`), sous dérogation bornée (`EXIG-GOV-16`).
  - Preuve vérifiée : `Corpus/Tome 2 L995–L1009`, `Corpus/Tome 5 L370`.
  - Passe initiale : écart rectifié · Action : complété l'ordre de préséance avec les deux règles intermédiaires (`source unique` et `disposition spéciale`) de `CAD26 § 4.3` · Verdict : supporté
- **C06-38 (`L132`) :** Déclinaison prospective (`2028–2035`) en quinze principes falsifiables `PRI-001` à `PRI-015` répartis en quatre familles et reliés terme à terme aux `10` décisions structurantes `CAD26`.
  - Preuve vérifiée : `Corpus/Tome 4 L1604–L1643, L5312–L5331`, `Corpus/Tome 5 L1838–L1857`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-39 (`L134`) :** Appuis empiriques de l'ergonomie d'outils : *Toolformer* (`arXiv:2302.04761` `[1]`, balisage syntaxique borné `<API>`), *Gorilla* (`arXiv:2305.15334` `[2]`, ancrage documentaire réduisant les hallucinations d'appels) et *ToolLLM* (`arXiv:2307.16789` `[3]`, arbre de décision `DFSDT` et recherche sémantique sur `16 000+` API réelles).
  - Preuve vérifiée : `SRC-116.txt L180–L189`, `SRC-117.txt L16–L22, L92`, `SRC-119.txt L3, L143, L231`, `ch06-sources.md` `[1]`–`[3]`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-40 (`L136`) :** Conception d'outil comme contrat cognitif atomique (non miroir `REST`), signature sous `JSON Schema` strict `[7]`, descriptions univoques, idempotence, budgets d'appels et messages d'erreur structurés et actionnables.
  - Preuve vérifiée : `SRC-021.txt` (`[7]`), `Corpus/Tome 1 L1200–L1229, L1252`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-41 (`L138–L144`) :** Cinq critères permanents d'évaluation de l'ouvrage : neutralité de gouvernance, déterminisme des frontières, tolérance aux pannes, coût marginal en latence et en jetons, coût de sortie.
  - Preuve vérifiée : `Corpus/Tome 3 L298–L308`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-42 (`L146`) :** Budgets `QoS` par classe de tâche (plafond coût/requête, plancher `pass^k`, cible latence `p99`) mesurés en intégration continue via le banc synthétique reproductible `Borealis-Bench`, les bancs `OpenEnv` et `AgentArcEval` et la trousse ouverte `TCK A2A` (`CH-23`).
  - Preuve vérifiée : `prd.md L1337, L1373`, `Corpus/Tome 8 L1763`, `registre/specifications-lplus.json` (`SPEC-A2A-TCK-ALPHA3`).
  - Passe initiale : écart rectifié · Action : qualifié `Borealis-Bench` comme banc synthétique reproductible et `TCK A2A` comme trousse ouverte afin de ne pas confondre un banc interne avec une norme tierce · Verdict : supporté
- **C06-43 (`L148`) :** Grille de maturité `N1`–`N5` (`N3` conforme à `BSIF E-23` `[6]` et à l'`EU AI Act`), six dimensions d'évaluation et quatre portes bloquantes `G1`–`G4` proscrivant tout saut direct `N1 → N4`.
  - Preuve vérifiée : `Corpus/Tome 3 L22447–L22516`, `SRC-065.txt`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-44 (`L150`) :** Preuves cumulatives des quatre portes : `G1` (inventaire, zéro secret partagé), `G2` (façade déterministe, idempotence, `pass^5 ≥ 0,95`), `G3` (résilience durable, double couloir, étalonnage) et `G4` (attestations cryptographiques `B2B`).
  - Preuve vérifiée : `Corpus/Tome 3 L22507–L22516, L22655`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-45 (`L152–L158`) :** Formule de préparation patrimoniale `S_ready` (`0,25 c_1 + 0,25 c_sec + 0,20 c_3 + 0,15 c_4 + 0,15 c_5`) × `I(c_sec ≥ 60)`, confinement en lecture seule `L1` si `S_ready < 50` ou `c_sec < 60`, et protection des verrous `SAP ENQUEUE` et sous-systèmes `IBM i QINTER` par façade `MCP` (`ACID` + *bulkhead*).
  - Preuve vérifiée : `Corpus/Tome 3 L22575–L22587`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-46 (`L160`) :** Exemple chiffré `(40, 70, 65, 55, 60)` produisant `S_ready = 57,75` (écriture bornée `[50, 75]` sous quotas et *full jitter*, qualification `N3`/`N4` dès `≥ 75`) et quatre verdicts de triage (`DECOMMISSION`, `QUARANTINE_L1`, `REMEDIATE`, `PROMOTE`).
  - Preuve vérifiée : `Corpus/Tome 3 L22587–L22659`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-47 (`L162–L164`, Figure 4) :** Schéma `SCH-06-04.svg` illustrant la maturité `N1–N5`, `S_ready` (`c_sec ≥ 60`), l'ergonomie d'outils et les budgets `QoS`.
  - Preuve vérifiée : `specs/manifest.json`, `schemas/SCH-06-04.svg`, `schemas/rendus/SCH-06-04.svg`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté

### 2.3 Section `6.3` — Exigences vérifiables, interfaces systémiques et livrables d'acceptation (`L166–L187`)

- **C06-48 (`L168`) :** Six exigences (`EXIG-D02-03.1` à `EXIG-D02-03.6`) encadrées par `AO-05` (`non-avis`) au gel du `2 décembre 2026`, appui exclusif sur les huit sources `L+` (`[1]`–`[8]`), exclusion en `statut F` (`AO-01`) de `iso.org/standard/81230.html` et `genai.owasp.org` (compensée par `SRC-055` `[8]`), et maintien des guides `TOGAF 10 ADM` hors évidence ouverte `L+` sous `DISC-04`.
  - Preuve vérifiée : `sources/ch06-sources.md L5–L102`, `recherche/registre-statut-f.json`, `registre/concordance-taxonomies.json L269`, `SRC-055.txt`.
  - Passe initiale : écart rectifié · Action : dissocié explicitement les deux exclusions formelles `statut F` de `ch06-sources.md` du statut hors évidence ouverte `TOGAF 10 ADM` sous `DISC-04` · Verdict : supporté
- **C06-49 (`L170–L179`, Tableau 6.3) :** Synthèse des six exigences `EXIG-D02-03.1` à `EXIG-D02-03.6`, critères déterministes, ancrages et portée.
  - Preuve vérifiée : `prd.md L1288–L1293`, `Corpus/Tome 2`, `Corpus/Tome 3`, `Corpus/Tome 4`, `SRC-116`, `SRC-117`, `SRC-119`, `SRC-068`.
  - Passe initiale : écart rectifié · Action : précisé `classe faible` sur `EXIG-D02-03.2` et `10 clauses EXIG-APP-07..16 (9 de négociation T3)` sur `EXIG-D02-03.6` · Verdict : supporté
- **C06-50 (`L181–L183`) :** Interfaces transversales vers `CH-05`, `CH-09`, `CH-10`, `CH-23`, `CH-25`, `CH-26`, `CH-29`, `CH-30`, `CH-31`, `CH-32`, `CH-34` (`305 EXIG-*` et `75 PRR`) et `CH-36` (`DIV-02`, `DISC-03`, `DISC-04`), ainsi que la gestion des tiers `BSIF B-10` `[4]`.
  - Preuve vérifiée : `prd.md L1361–L1384`, `plan.md L745`, `SRC-068.txt`, `registre/matrice-exig-prr-c40.json`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté
- **C06-51 (`L185–L187`) :** Cinq livrables auditables aux portes `G1` à `G5` : matrice trimestrielle `DIV-02` / `ABB → SBB`, vues `ArchiMate 4.0` (`3.2` compatibles) sans exigence réglementaire orpheline, portefeuille financé `42` / `10` `CAP`, registre YAML `31 ADR` / `12 DEC` aligné sur `2027-B001`, manifestes *Brownfield Readiness* (`S_ready` avec `c_sec ≥ 60`) et procès-verbal annuel d'essai de sortie `BSIF B-10` `[4]`.
  - Preuve vérifiée : `plan.md L761`, `prd.md L1353–L1360`, `SRC-068.txt`.
  - Passe initiale : conforme · Action : aucune · Verdict : supporté

---

## 3. Contrôle final post-rectifications (`verifie_manuscrit.py --unit ch06 --strict`)

- **Mots vérifiés (`Chapitre 06.md`) :** `5 279` mots de prose (plage autorisée `[4 950, 5 810]`, cible `5 380`, conforme `CA-01`).
- **Base fermée citée (`CA-09`, `CA-10`, `CA-11`) :** `8 / 8` sources (`[1]`–`[8]`) citées, `0` référence orpheline, `2` exclusions `statut F` formelles consignées dans `ch06-sources.md` (`iso.org/standard/81230.html`, `genai.owasp.org` compensée par `SRC-055` `[8]`) et guides propriétaires `TOGAF 10 ADM` maintenus hors évidence ouverte sous `DISC-04`.
- **Synchronisation et hygiène (`CA-02..CA-08`, `CA-22`) :** `0` symbole dollar non échappé, `0` collision `12-grammes`, `3` tableaux (`Tableau 6.1` à `Tableau 6.3`), `4` figures (`SCH-06-01` à `SCH-06-04`), vedette propriétaire du glossaire présente (`noyau de contrôle déterministe`), encodage UTF-8 sans BOM et fins de ligne `LF` strictes.
- **Verdict final — supportés :** 51 / 51 (100,0 %)

---

## Mise à jour post-révision PRD (`REV-04`)

- **C06-REV-01 (`L7`, `L17`, `L46`, `L70–L74`, `L107`, `L115`, `L152`, `L158`, `L164`, `L168`, `SCH-06-01.svg`, `SCH-06-02.puml`, `PRD-L1-003`, `008`, `011`, `015`, `016`, `021`)** — Retrait bloquant des backticks autour des `6` formules LaTeX inline (`S_ready < 50`, `c_sec < 60`, `\tau_{\min} = 60`, `\mathbb{I}(c_{\text{sec}} \ge 60)`), numérotation continue `Figure 20`–`Figure 23` (y compris renvoi `L70` vers `Figure 21`), phrase de pont sur l'emboîtement `LCIM` (`4`/`5`/`7` paliers), harmonisation `9` clauses de négociation Tome 3 consolidées en `10` clauses `EXIG-APP-07..16` (prose, légende `Figure 21` et `SCH-06-02.puml`), retrait des fuites (`SUB_D02_03`, `SRC-055`), retrait des backticks littéraux dans `SCH-06-01.svg` et remplacement de `vs` dans `SCH-06-02.puml`.
  - *Preuve primaire :* `Compendium/prd.md` (`L1333`, `L1345`), `specs/manifest.json`, `schemas/SCH-06-01.svg`, `schemas/SCH-06-02.puml`.
  - Verdict : supporté
- **C06-REV-02 (`L42`, `L132`, `§ 6.2.1`, `§ 6.2.2`)** — Traduction en modélisation `ArchiMate 4.0` du caractère composite de **l'agentivité des systèmes** (*system agency*, acteur cognitif subordonné en `Application Component`, jamais `Business Actor`) et ancrage de la souveraineté institutionnelle dans les `42` capacités invariantes (`PRIN-01` à `PRIN-12`), où le pouvoir d'agir relève du système gouverné et borné par contrat.
  - *Preuve primaire :* `SRC-066.txt` (`[5]`, `L27`, `L69–L73`, `L175`), `SRC-055.txt` (`[8]`, `L237–L242`), `registre/matrice-exig-prr-c40.json` (`42` capacités invariantes).
  - Verdict : supporté
- **Contrôle `REV-05` :** `5 380` mots (`verifie_manuscrit.py`) dans `[4 950, 5 810]`, `verifie_manuscrit.py --unit ch06 --strict` = `exit 0`. **Verdict final : `53 / 53` (`100,0 %` supporté).**
