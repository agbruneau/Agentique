# Journal d'ancrage atomique Wyvern G2 — Chapitre 33 (`ch33`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/11 - Partie XI/Chapitre 33.md` (`3 699` mots de prose `verifie_manuscrit` / `3 906` mots `parser_plan`, plage `[3 377, 3 963]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch33-sources.md` (`[1]`–`[9]` en statut `L+`, `3` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` (incluant `SRC-040`, `SRC-055`, `SRC-063`, `SRC-064`, `SRC-066`, `SRC-068` archivés en `L+`) ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) ; spécification `Compendium/prd.md` (`CH-33`) et index heuristique interne `Corpus/Tome 1..7*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b5-4`
- **Passe G2 initiale (supportés) :** 15
- **Rectifications appliquées lors de la passe G2 :** 13
- **Verdict final — supportés :** 28 / 28 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 33.md`

Toutes les formulations divergentes, sur-attribuées ou insuffisamment sourcées relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 33.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/11%20-%20Partie%20XI/Chapitre%2033.md), en préservant les `owned_concepts` (`atrophie-competences-humaines`, `sanctuarisation-vivier-junior-reprise`, `approbation-reflexe-biais-automatisation`), les renvois `[1]`–`[9]` de `ch33-sources.md`, la cohérence des schémas `SCH-33-01..03`, le calibrage (`3 699` mots dans `[3 377, 3 963]`) et la barrière `G1` (`0` erreur) :

1. **Exclusions `statut F` et compensations `L+` (`L7`) :** correction de l'attribution des renvois compensatoires (`[3, 4]` pour le biais d'automatisation face à `pmc.ncbi.nlm.nih.gov` bloqué `g-recaptcha`, `SRC-063` `L.Q. 2021, c. 25` et `SRC-064` CAI `2026` en `L+` face à `legisquebec.gouv.qc.ca` `HTTP 403`, et retrait probatoire de `hbs.edu` `HTTP 403` selon `ch33-sources.md`).
2. **Paradoxe automatisation–augmentation, Stanford HAI et Banque du Canada (`L15`, `L17`, `L19`, `Tableau 33.1`) :**
   - Séparation explicite entre les constats de Chandra et Michel (`[7]`, `SRC-113.txt`) centrés sur le développement logiciel (Raisch & Krakowski, *deep practice*, atrophie des vétérans), la transposition du traité aux opérations réglementées et les concepts de **mémoire transactive** et de *bus factor* issus de Storey (`SRC-040`, Chapitre 03) ;
   - Alignement sur `SRC-008.txt` (`[1]`) : pic de `2022` (sans ajout de « fin `2022` » dans la prose du `§ 4.4`) et fenêtre `2024–2025` pour la baisse de `11 %` des inscriptions en informatique ;
   - Rectification factuelle sur `SRC-016.txt` (`[2]`) : la raison majoritaire de non-adoption citée par les entreprises canadiennes est le **manque de pertinence opérationnelle**, devant la pénurie de personnel qualifié ; précision des branches (`finance, assurances, immobilier et location`).
3. **Simulation `CAHAT` et étude de terrain sur la supervision (`L46`, `L48`) :**
   - Distinction dans `[3]` (`SRC-073.txt`) entre l'ablation de calibrage (`12,36 %` sans calibrage vs `0,81 %` avec *temperature scaling*) et la comparaison complète des protocoles (`0,8 %` pour l'hybride adaptatif vs `12,4 %` pour l'humain seul ou l'IA non calibrée), avec mention du seuil critique \(\psi \ge 0,75\) ;
   - Alignement sur `[4]` (`SRC-075.txt`) : quatre formes de supervision, suivi en direct guidé par des indices indirects (temps d'exécution ou nombre de tours anormalement longs), rattachement des quatre heuristiques à la revue *post hoc*, et qualification de l'estimation `~10 %` comme constat rapporté par un développeur interrogé à propos des traces de raisonnement.
4. **Droit québécois, droit européen et attentes prudentielles du BSIF (`L32`, `L34`, `L50`–`L54`, `L70`, `Tableau 33.2`) :**
   - Ancrage exact de la *Loi 25* (`L.Q. 2021, c. 25`, `SRC-063.txt`, `SRC-064.txt`) sur le texte sanctionné (`art. 12.1`, `90.1(5°)`, `90.12`, `91`), mention explicite de la clause `AO-05` pour l'analyse du risque de requalification et respect des règles `CA-03`/`CA-05` ;
   - Dissociation dans l'`EU AI Act` (`[8]`, `SRC-060.txt`) des articles `14(4)(b)`, `14(4)(d)–(e)` et `26(2)`, et ancrage de l'accessibilité `(UE) 2019/882` sur l'article `16(l)` (`[8]`) en précisant que son texte autonome reste hors corpus `L+` de ce chapitre ;
   - Rattachement des *manual fallbacks* et du rappel sur les sorties d'IA comme intrants d'analyse au bulletin technologique du BSIF du `13 juillet 2026` (`SRC-066.txt` en `L+`) conjointement à `E-23` (`1er mai 2027` `[9]`, `SRC-065.txt`) et `B-10` (`SRC-068.txt` en `L+`), tout en distinguant la périodicité normative interne d'`EXIG-HUM-04` (`POR-009`, `POR-014`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C33-01` à `C33-28`)

### Section 33.0 — Titre, question directrice et cadrage méthodologique (`L1–L7`)

- **C33-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant la prévention de l'atrophie de la relève junior, la parade à l'approbation réflexe et le maintien du repli manuel.
  - **Appui vérifié :** `specs/manifest.json` (`ch33`, `D11`, `SUB_D11_03`), `Compendium/prd.md` (`CH-33`, `L6058–6060`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C33-02 (`L5`)** — *Affirmation :* L'automatisation cognitive absorbe les dossiers ordinaires, réduit le terrain d'apprentissage des analystes, expose les valideurs à entériner machinalement des synthèses persuasives et menace simultanément la reprise manuelle et la conformité en cas de supervision décorative.
  - **Appui vérifié :** `Compendium/prd.md` (`CH-33`, `L6064`), `Corpus/Tome 7` (`§ 11.2–11.4`, `L1629–1715`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C33-03 (`L7`)** — *Affirmation :* Analyse présentée sous la clause de non-avis juridique (`AO-05`) arrêtée au `2 décembre 2026` ; faits issus de sources `L+` (`AO-01`), avec consignation en `statut F` de `pmc.ncbi.nlm.nih.gov` (`CAPTCHA`, compensé par `[3, 4]`), `legisquebec.gouv.qc.ca` (`HTTP 403`, compensé par `L.Q. 2021, c. 25` `SRC-063` et CAI `2026` `SRC-064` au corpus `L+`) et `hbs.edu` (`HTTP 403`, exclu de la preuve) ; présentation du plan incluant le seuil interne de `70 %`.
  - **Appui vérifié :** `sources/ch33-sources.md` (`L3–5`, `L110–114`), `specs/protocole-mlr-compendium.json` (`AO-01`), `Compendium/prd.md` (`L6072`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié les compensations exactes (`[3, 4]` pour `pmc.ncbi.nlm.nih.gov`, `SRC-063`/`SRC-064` pour `legisquebec.gouv.qc.ca`, exclusion sans remplacement pour `hbs.edu`) au lieu de `[3, 4, 8, 9]` · **Verdict : supporté**

### Section 33.1.1 — Gains de productivité à court terme et contraction du vivier junior (`L11–L28`, Tableau 33.1)

- **C33-04 (`L13`)** — *Affirmation :* Dans un essai contrôlé randomisé publié dans *Science* auprès de `453` professionnels diplômés, Noy et Zhang mesurent une réduction de `40 %` du temps moyen de rédaction et une hausse de `18 %` de la qualité évaluée, en réduisant les écarts au profit des participants initialement moins performants.
  - **Appui vérifié :** `SRC-099.txt` (`[5]`, `L14–18`, `L80`, `L194–198`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C33-05 (`L13`)** — *Affirmation :* Dans trois expérimentations de terrain totalisant `4 867` développeurs logiciels, Cui, Demirer, Jaffe, Musolff, Peng et Salz observent une hausse globale de `26,08 %` des tâches complétées (plus marquée chez les profils à faible ancienneté), ainsi qu'une progression de `38,38 %` des compilations hebdomadaires (erreur type `12,55 %`) et de `13,55 %` des mises à jour de code (erreur type `10,0 %`, statistiquement non significative).
  - **Appui vérifié :** `SRC-100.txt` (`[6]`, `L13–16`, `L55–60`, `L124–125`, Table 3 `L660–710`, `L751–754`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C33-06 (`L15`)** — *Affirmation :* La revue de littérature de Chandra et Michel (reprenant le paradoxe automatisation–augmentation de Raisch et Krakowski `2021`) montre dans le développement logiciel qu'en déléguant aux agents les tâches courantes (code, tests, débogage), on risque de tarir la *deep practice* des débutants et d'exposer les développeurs chevronnés à l'atrophie par délégation excessive (`[7]`) ; transposée dans le traité aux opérations réglementées, cette dynamique nourrit la dette cognitive du Chapitre 03 (`Storey`), détruisant la mémoire transactive et abaissant le *bus factor*.
  - **Appui vérifié :** `SRC-113.txt` (`[7]`, `L50`, `L72–73`, `L479`, `L629–633`), `SRC-040.txt` (`L70`, `L131–134`), `Corpus/Tome 7` (`L1661`, `L1832`).
  - **Passe initiale :** écart rectifié · **Action :** isolé les constats logiciels de `[7]` de leur transposition aux métiers réglementés et rattaché la mémoire transactive et le *bus factor* à la dette cognitive du Chapitre 03 (`SRC-040`), tout en scindant la phrase (`CA-05`) · **Verdict : supporté**

- **C33-07 (`L17`)** — *Affirmation :* Selon l'*AI Index Report 2026* de Stanford HAI (`arXiv:2606.15708` `[1]`), aux États-Unis l'emploi des développeurs logiciels de `22` à `25` ans recule d'environ `20 %` depuis le sommet de `2022` jusqu'à `septembre 2025` selon le `§ 4.4` (formulé « depuis `2024` » dans la synthèse exécutive), tandis que les effectifs plus âgés croissent ; en neutralisant les effets propres aux types d'entreprises, les professions les plus exposées subissent un écart relatif d'environ `16 %`, parallèlement à une baisse de `11 %` des inscriptions en programmes universitaires de quatre ans en informatique entre `2024` et `2025` et à l'émergence du banc *Finance Agent*.
  - **Appui vérifié :** `SRC-008.txt` (`[1]`, `L397–399`, `L7256–7257`, `L16360–16372`, `L20280`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé « fin `2022` » par « sommet de `2022` » conforme à `L16363` et précisé la fenêtre `2024–2025` pour la baisse de `11 %` (`L20280`) · **Verdict : supporté**

- **C33-08 (`L19`)** — *Affirmation :* Selon le document analytique `2026-22` de la Banque du Canada (`2 juin 2026` `[2]`), à `12` mois `11 %` des firmes anticipent une diminution d'effectifs contre `8 %` une hausse, et à `3` ans `18 %` anticipent un frein ou une réduction d'embauche contre `9 %` une hausse ; chez `≥ 20` employés (`SML`), les anticipations de baisse passent de `10 %` en `2026` à `21 %` à `3` ans, avec solde négatif aux deux horizons en finance, assurances, immobilier et location ; les non-adoptants citent, après le manque de pertinence opérationnelle (raison majoritaire), la pénurie de personnel qualifié parmi les principaux freins.
  - **Appui vérifié :** `SRC-016.txt` (`[2]`, `L5`, `L97–98`, `L114–116`, `L179–180`, `L207–213`, `L314–330`, `L365–367`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé l'erreur sur le frein majoritaire (manque de pertinence opérationnelle avant la pénurie de personnel qualifié), aligné le libellé sectoriel et levé la collision `CA-03` · **Verdict : supporté**

- **C33-09 (`L21–L28`, Tableau 33.1)** — *Affirmation :* Le *Tableau 33.1* récapitule les ordres de grandeur vérifiés des études `[5]`, `[6]`, `[1]` et `[2]` ainsi que le lien vers le signal `SIG-017` (`2033–2035`).
  - **Appui vérifié :** `SRC-099.txt` `[5]`, `SRC-100.txt` `[6]`, `SRC-008.txt` `[1]`, `SRC-016.txt` `[2]`, `registre/matrice-exig-prr-c40.json` (`SIG-017`).
  - **Passe initiale :** écart rectifié · **Action :** aligné `pic 2022` et `2024–2025` dans la ligne Stanford HAI du Tableau 33.1 · **Verdict : supporté**

### Section 33.1.2 — Vulnérabilité prudentielle du repli manuel et accessibilité (`L30–L34`)

- **C33-10 (`L32`)** — *Affirmation :* L'article `15(4)` de l'`EU AI Act` impose aux systèmes à haut risque la résilience aux défaillances, au besoin par des plans de sauvegarde (`[8]`) ; au Canada, `BSIF E-23` (prévue le `1er mai 2027` `[9]`) exige des plans de contingence et d'urgence, et le bulletin technologique du BSIF de `juillet 2026` (`SRC-066` en `L+`) recommande d'éprouver des scénarios de panne et d'établir des replis manuels (*manual fallbacks*) en appui à `B-10` (`SRC-068` en `L+`) et `E-21`.
  - **Appui vérifié :** `SRC-060.txt` (`[8]`, `L3902–3908`), `SRC-065.txt` (`[9]`, `L31`, `L457`, `L475`), `SRC-066.txt` (`L3`, `L9`, `L113–117`, `L131`), `SRC-068.txt` (`L417–461`).
  - **Passe initiale :** écart rectifié · **Action :** précisé la date `1er mai 2027` de `[9]`, rattaché explicitement les *manual fallbacks* au bulletin `SRC-066` (`L+`) et à `B-10` (`SRC-068`, `L+`), et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C33-11 (`L34`)** — *Affirmation :* Un repli manuel non exercé perd son effectivité ; l'article `16(l)` de l'`EU AI Act` exige que les systèmes à haut risque soient conformes aux directives `(UE) 2016/2102` et `(UE) 2019/882` (`[8]`, leurs textes autonomes restant hors corpus `L+` du chapitre), ce qui fonde l'exigence architecturale du traité de préserver l'accessibilité sur les interfaces de secours destinées à la clientèle.
  - **Appui vérifié :** `SRC-060.txt` (`[8]`, `L3951–3952`), `Compendium/prd.md` (`L6076`, `L6116`), `Corpus/Tome 1` (`L12509`).
  - **Passe initiale :** écart rectifié · **Action :** ancré l'accessibilité sur `art. 16(l)` `[8]` en signalant l'absence du texte autonome de `(UE) 2019/882` dans la base `L+` du chapitre · **Verdict : supporté**

### Section 33.2.1 — Boucle d'érosion, approbation réflexe et risque juridique (`L36–L62`, Figures 103–104)

- **C33-12 (`L40–L44`, Figure 103 `SCH-33-01`)** — *Affirmation :* Sans réaménagement du poste de supervision, la boucle d'érosion cognitive s'enchaîne de `E1` à `E5` (`Z1`) et est interrompue par trois disjoncteurs organisationnels possédés `D1` à `D3` (`Z2`), illustrés par `SCH-33-01.svg`.
  - **Appui vérifié :** `specs/manifest.json` (`ch33`, `SCH-33-01`), `schemas/SCH-33-01.puml` (`L61–86`), `schemas/rendus/SCH-33-01.svg`, `Compendium/prd.md` (`L6126–6143`), `Corpus/Tome 7` (`§ 11.4`, `L1686`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C33-13 (`L46`)** — *Affirmation :* Au maillon `E3` opère l'approbation réflexe (`ASI09` dans *OWASP Top 10 for Agentic Applications* en `L+`) ; l'étude de simulation d'AL-Ali et coll. (*Nature Scientific Reports*, août `2026` `[3]`, soulignant le besoin de validation humaine réelle) montre un taux d'échec de `12,36 %` sans calibrage contre `0,81 %` avec *temperature scaling* en ablation, et de `0,8 %` en architecture hybride adaptative contre `12,4 %` pour l'humain seul ou l'IA non calibrée, désignant le biais cognitif humain sous pression (critique dès \(\psi \ge 0,75\)) comme facteur dominant.
  - **Appui vérifié :** `SRC-055.txt` (`L1190–1205`), `SRC-073.txt` (`[3]`, `L46`, `L190`, `L322–326`, `L346–357`, `L404`, `L416`).
  - **Passe initiale :** écart rectifié · **Action :** distingué exactement les chiffres d'ablation (`12,36 %`/`0,81 %`) de ceux du banc complet (`0,8 %`/`12,4 %`), précisé l'archivage `L+` d'`ASI09` et ajouté le seuil \(\psi \ge 0,75\) · **Verdict : supporté**

- **C33-14 (`L48`)** — *Affirmation :* L'étude de terrain de Dhanorkar, Passi et Vorvoreanu (`arXiv:2606.05391`, juin `2026` `[4]`) auprès de `17` développeurs expérimentés identifie `4` formes de supervision (contrôle *a priori*, co-planification, suivi en temps réel, revue *post hoc*), observe la rareté du suivi en direct (guidé par des indices indirects comme une durée d'exécution ou un nombre de tours anormalement longs), recense `4` heuristiques de revue *post hoc* (plan comme substitut, tests comme garantie, *eyeballing*, confiance en contexte non familier) et rapporte l'estimation d'un praticien selon lequel les traces de raisonnement sont erronées environ `10 %` du temps avec une forte assurance.
  - **Appui vérifié :** `SRC-075.txt` (`[4]`, `L9–15`, `L271–272`, `L387–411`, `L468–554`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la terminologie des quatre formes, rattaché les quatre heuristiques à la revue *post hoc*, précisé la 4e heuristique et qualifié `10 %` de constat rapporté par un praticien · **Verdict : supporté**

- **C33-15 (`L50–L52`)** — *Affirmation :* Au Québec, l'article `12.1` de la *Loi 25* (`L.Q. 2021, c. 25`, en vigueur depuis le `22 septembre 2023` selon `SRC-063`/`SRC-064` en `L+`) impose avis au plus tard lors de la décision, information sur demande des données personnelles mobilisées, des motifs, des facteurs déterminants et des paramètres, droit de rectification et occasion de présenter des observations à un employé habilité à réexaminer la décision ; selon l'analyse technique non-avis du traité (`AO-05`), une supervision mécanique expose au risque de requalification et aux sanctions administratives jusqu'à `10 M\$ CA` (`2 %`) de l'article `90.12` (via `90.1(5°)`) ainsi qu'aux amendes pénales de `15 000 \$ CA` à `25 M\$ CA` (`4 %`) édictées à l'article `91`.
  - **Appui vérifié :** `SRC-063.txt` (`L1542–1555`, `L2175–2177`, `L2283–2287`, `L2328–2332`), `SRC-064.txt` (`L15181`, `L15239–15241`), `registre/ancres-chronologiques.json` (`L30`, `L44`).
  - **Passe initiale :** écart rectifié · **Action :** aligné les éléments de l'article `12.1` et la distinction SAP (`90.1(5°)`/`90.12`) vs infractions pénales (`91`), explicité la clause `AO-05` sur le risque de requalification et scindé en deux paragraphes conformes à `CA-03` et `CA-05` · **Verdict : supporté**

- **C33-16 (`L54`)** — *Affirmation :* En Europe, l'`EU AI Act` impose à l'article `14(4)(b)` et `(d)–(e)` la conscience du biais d'automatisation et la faculté d'ignorer, inverser ou interrompre le système, et à l'article `26(2)` des contrôleurs disposant des compétences, de la formation, de l'autorité et du soutien nécessaires (`[8]`) ; au Canada, le bulletin technologique du BSIF de `juillet 2026` (`SRC-066` en `L+`, en cohérence avec `E-23` `[9]`) rappelle de traiter les sorties d'IA comme des intrants d'analyse et jamais comme des résultats définitifs.
  - **Appui vérifié :** `SRC-060.txt` (`[8]`, `L3866–3879`, `L4253–4255`), `SRC-066.txt` (`L45–47`), `SRC-065.txt` (`[9]`, `L153`, `L301–307`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié `art. 14(4)(b)`/`(d)–(e)` et `art. 26(2)` dans `[8]` et attribué la citation des sorties comme intrants au bulletin `SRC-066` conjointement à `[9]` · **Verdict : supporté**

- **C33-17 (`L56`)** — *Affirmation :* L'exigence normative interne `EXIG-HUM-02` impose le masquage de l'avis tant que les pièces primaires restent closes, un différentiel `I-JSON`, le visa hors bande `CIBA` (`EXIG-AUT-19`, validité `≤ 15 min`), un plafond de `≤ 33` dossiers complexes par quart (`360 min` effectives, `65 %` de vigilance), une durée minimale de `7 min` par examen et une médiane calculée sur au moins `3` approbateurs par cas d'usage (`EXIG-AUT-21`).
  - **Appui vérifié :** `Compendium/prd.md` (`L6073`), `Compendium/plan.md` (`L1579`), `Corpus/Tome 2` (`EXIG-AUT-19`, `EXIG-AUT-21` `L3743`), `registre/matrice-exig-prr-c40.json` (`A.5.3`, `CAP-002`).
  - **Passe initiale :** conforme · **Action :** précisés les paramètres numériques et `EXIG-AUT-21` (`post-G4`) · **Verdict : supporté**

- **C33-18 (`L58`)** — *Affirmation :* L'exigence normative interne `EXIG-HUM-03` impose l'injection continue et à l'aveugle de `3 %` à `5 %` de dossiers témoins canaris (`PRR G-11` / `G-12`), le suivi mensuel en `N3–N4` et une revue *a posteriori* sur `5 %` des dossiers en classe modérée (`1 %` en classe faible), le gel vers la validation synchrone (`POR-014`) sous le seuil interne retenu (aucune source normative ne fixant de plancher universel), leur renouvellement anonymisé et une charte non punitive agrégée par file.
  - **Appui vérifié :** `Compendium/prd.md` (`L6074`), `registre/matrice-exig-prr-c40.json` (`prr_75`: `G-11`, `G-12`, `POR-014`), `Corpus/Tome 2` (`EXIG-AUT-21`).
  - **Passe initiale :** conforme · **Action :** précisés `3 %–5 %`, la revue `5 %/1 %` et le basculement `POR-014` (`post-G4`) · **Verdict : supporté**

- **C33-19 (`L60–L62`, Figure 104 `SCH-33-02`)** — *Affirmation :* La *Figure 104* (`SCH-33-02.svg`) oppose le poste vulnérable à la validation réflexe (`Z1`, risque `Loi 25` / `EU AI Act`) et le poste différentiel durci (`Z2`, masquage préalable, pièces brutes, dossiers témoins et liaison `CIBA`).
  - **Appui vérifié :** `specs/manifest.json` (`ch33`, `SCH-33-02`), `schemas/SCH-33-02.svg`, `schemas/rendus/SCH-33-02.svg`, `Compendium/prd.md` (`L6144–6160`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 33.2.2 — Quotas formateurs, reconversion RH-IT et exercices sans agent (`L64–L88`, Figure 105, Tableau 33.2, Invariants)

- **C33-20 (`L66`)** — *Affirmation :* L'exigence normative interne `EXIG-HUM-01` active `INI-043` / `CAP-048` : au-delà de `70 %` d'automatisation, un quota plancher de dossiers instruits manuellement de bout en bout sans agent est sanctuarisé, combiné à `4` trimestres sans dérive ni dépassement de budget d'erreur pour préserver le certificat `POR-014`, avec *walkthroughs* juniors et jumeaux de rejeu.
  - **Appui vérifié :** `Compendium/prd.md` (`L6072`, `L6087`), `registre/matrice-exig-prr-c40.json` (`CAP-048`, `INI-043`, `POR-014`), `Corpus/Tome 4` (`L4733`), `Corpus/Tome 5` (`L995`).
  - **Passe initiale :** conforme · **Action :** ajoutée la condition des `4` trimestres sans dérive sous `POR-014` (`post-G4`) · **Verdict : supporté**

- **C33-21 (`L68`)** — *Affirmation :* L'exigence normative interne `EXIG-HUM-05` confie au tandem `RH–IT` *Hub-and-Spoke* un parcours certifiant de reconversion (`120 heures` dans les référentiels internes) sans suppression sèche d'emplois vers les rôles `HOTL`, curateurs sémantiques et `AgentOps`.
  - **Appui vérifié :** `Compendium/prd.md` (`L6076`), `Corpus/Tome 3` (`L21852`, `L21917`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C33-22 (`L70`)** — *Affirmation :* Pour opérationnaliser les attentes de plans de contingence, de repli manuel et de résilience posées par `BSIF E-23`, `B-10`, `E-21`, le bulletin de `juillet 2026` et `EU AI Act` art. `15(4)` (`[8, 9]`), l'exigence interne `EXIG-HUM-04` impose des *game days* au moins annuels (`≥ 1/an`, semestriels sur les fonctions critiques) sans agent (`L0`, `POR-009`, `POR-014`), prouvant une bascule technique en `< 60 s` (`POR-015` : rétrogradation vers la validation synchrone `N2` ou repli déterministe sans agent `L0`) et contrôlant débit dégradé, sortie de tiers et accessibilité (`Dir. 2019/882` via `art. 16(l)` `[8]`).
  - **Appui vérifié :** `SRC-060.txt` (`[8]`, `art. 15(4)`, `art. 16(l)`), `SRC-065.txt` (`[9]`, `Principe 3.6`), `SRC-066.txt` (`L117`), `SRC-068.txt` (`L417–461`), `Compendium/prd.md` (`L6075`), `registre/matrice-exig-prr-c40.json` (`POR-009`, `POR-014`, `POR-015`).
  - **Passe initiale :** écart rectifié · **Action :** ajoutée la preuve de bascule `< 60 s` (`POR-015`) et `≥ 1/an` (`post-G4`), et harmonisée l'articulation `N2` ou `L0` (lissage G5) · **Verdict : supporté**

- **C33-23 (`L72–L74`, Figure 105 `SCH-33-03`)** — *Affirmation :* La *Figure 105* (`SCH-33-03.png`) illustre la surveillance du seuil de `70,0 %`, le quota `INI-043`, la reconversion `RH-IT` (`Z1`) et la validation des exercices sans agent (`POR-009`/`POR-014`, débit dégradé, accessibilité, `Z2`).
  - **Appui vérifié :** `specs/manifest.json` (`ch33`, `SCH-33-03`), `schemas/SCH-33-03.mmd` (`L2–15`), `schemas/rendus/SCH-33-03.png`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C33-24 (`L76–L83`, Tableau 33.2)** — *Affirmation :* Le *Tableau 33.2* articule les quatre parades humaines (couloir rapide en lecture seule proportionné sous `E-23` `[9]`, responsable humain unique doté du pouvoir d'arrêt sous `art. 14(4)(e)`/`26(2)` `[8]` et `E-23` `[9]`, écran différentiel/`CIBA`/témoins, quotas `> 70 %` et *game days* `[7, 9]`) et leurs points de rupture.
  - **Appui vérifié :** `SRC-060.txt` `[8]`, `SRC-065.txt` `[9]`, `SRC-113.txt` `[7]`, `Corpus/Tome 7` (`Tableau 11.1`, `L1679–1682`).
  - **Passe initiale :** écart rectifié · **Action :** précisé la proportionnalité sous `E-23` `[9]` en ligne 1 et complété les références `art. 14(4)(e)`, `26(2)` `[8]` et `E-23` `[9]` en ligne 2 · **Verdict : supporté**

- **C33-25 (`L85–L88`)** — *Affirmation :* Encadré des trois invariants exécutables du Chapitre 33 : (1) masquage préalable, vue différentielle et signature `CIBA` (`EXIG-AUT-19`) avec cas témoins non punitifs ; (2) gel automatique d'autonomie sur chute du taux d'infirmation (`Loi 25` art. `12.1` / `EU AI Act` art. `14`) ; (3) quota formateur `INI-043` dès `70 %` et exercices `POR-009`/`POR-014` en mode accessible (`Dir. 2019/882`).
  - **Appui vérifié :** `Compendium/prd.md` (`L6072–6076`), `registre/matrice-exig-prr-c40.json` (`INI-043`, `POR-009`, `POR-014`, `EXIG-AUT-19`), `SRC-060.txt` `[8]`, `SRC-063.txt`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 33.3 — Synthèse opératoire, exigences et frontières d'architecture (`L90–L106`, Tableau 33.3)

- **C33-26 (`L92–L102`, Tableau 33.3)** — *Affirmation :* Le *Tableau 33.3* résume les cinq exigences `EXIG-HUM-01` à `EXIG-HUM-05` (intégrant `CAP-002`, `PRI-007`, `PRR-75`, `CAP-031`, `CAP-039` et `ADR-025`, dont `EXIG-HUM-04` : `Game days` de repli manuel `L0` `≥ 1/an` ou semestriel si critique et bascule `< 60 s` vers `N2` ou `L0` `POR-009`/`014`/`015`) et leurs preuves attendues (tableau de bord semestriel `RH-IT`, journaux d'interface et empreinte `h = SHA-256(JCS(...))`, rapports trimestriels agrégés non punitifs, comptes rendus de `game days` sous `B-10`/`E-21`, parcours `120 h` et tests d'accessibilité).
  - **Appui vérifié :** `Compendium/prd.md` (`L6072–6076`, `L6097–6100`), `aq/rapports-g0.json` (`rfc8785`: `20/20`, `test_authz_pqc_audit.py`: `23` tests incluant `ciba_approval.py`), `Corpus/Tome 3` (`L21852`), `registre/matrice-exig-prr-c40.json` (`CAP-002`, `CAP-031`, `CAP-039`, `ADR-025`, `PRI-007`, `PRR-75`, `POR-015`).
  - **Passe initiale :** conforme · **Action :** harmonisée l'entrée `EXIG-HUM-04` (`L0` / `N2`, lissage G5) ; révision `REV-04` : retrait des échappements `\$` dans les backticks (`L52`, `PRD-L4-010`) et intégration des identifiants `CAP-002`, `CAP-031`, `CAP-039`, `ADR-025`, `PRI-007` et `PRR-75` au `Tableau 33.3` (`PRD-L4-026`) · **Verdict : supporté**

- **C33-27 (`L104`)** — *Affirmation :* Partition conceptuelle `CA-21` (exclusion du droit individuel du travail et des négociations salariales ; interfaces aval `→` `ch03`, `ch31` avec arbitrage `INI-043` conditionnant l'ouverture du Palier 3 `2033–2035`, `ch32` et amont `←` `ch05`, `ch25`).
  - **Appui vérifié :** `specs/manifest.json` (`ch33` `owned_concepts`), `Compendium/prd.md` (`L6070`, `L6104–6110`), `verifie_manuscrit.py` (`CA-21`), `registre/concordance-taxonomies.json` (`DISC-02`).
  - **Passe initiale :** conforme · **Action :** harmonisé `ouverture du Palier 3` (retrait de `Stades 3 et 4` sous `DISC-02`, lissage G5) · **Verdict : supporté**

- **C33-28 (`L106`)** — *Affirmation :* Clôture sur les quatre livrables du domaine et transition vers la Partie XII (`CRE-IA-2026-01`, trousse logicielle et chaîne probatoire `Wyvern`, Chapitre 34).
  - **Appui vérifié :** `Compendium/prd.md` (`L6097–6100`), `specs/manifest.json` (`ch34`, Partie XII).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**
