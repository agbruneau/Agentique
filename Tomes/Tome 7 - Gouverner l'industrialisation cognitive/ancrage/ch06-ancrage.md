# Dossier d'ancrage atomique — Chapitre 06 (`ch06`)

- **Unité** : `ch06` — `7 - Livre/manuscrit/02 - Partie II/Chapitre 06 - Sobriete d orchestration et execution durable.md`
- **Barrière** : `G2` — Audit d'ancrage atomique indépendant (`CA-10`, `CA-12`, régime Production)
- **Dossier de sources probantes** : `7 - Livre/sources/ch06-sources.md` (`19` sources intégrales `L+`) et `7 - Livre/recherche/corpus_l_plus/*.txt`
- **Registres de référence vérifiés** : `faits-empiriques.json`, `ancres-chronologiques.json`, `glossaire-termes.json`
- **Date de gel des faits** : 2 décembre 2026
- **Volume final vérifié (`v1.3`)** : `6 484` mots lexicaux `G1` (`6 796` `split()`, cible `[5 888, 6 912]`)

## Bilan synthétique

- **Total d'affirmations atomiques actives vérifiées** : `133`
- **Verdict final — supportés : 133 (100 %)**
- **Verdict final — imprécis résiduels : 0**
- **Verdict final — non supportés résiduels : 0**
- **Constat initial avant rectifications** : `92` supportés initiaux, `41` imprécis initiaux rectifiés directement dans le manuscrit (`0` non supportés résiduels).
- **Contrôle différentiel post-G4 (`L27`, `L47–L81`, `Fig-11.mmd`)** : `4` écarts différentiels détectés et rectifiés en `L47`, `L53`, `L55`, `L61`; verdict post-rectification : **`100 %` `supporté`**, **`0` imprécis résiduel**, **`0` non supporté résiduel** (voir section dédiée en fin de dossier).

---

## Détail paragraphe par paragraphe

### U00 — Titre et question directrice (lignes 1–3)

- **U00.1 (L1)** — Titre du chapitre 06 : « Quand ne pas multiplier les agents : lois d'échelle et exécution durable ».
  - Source : Cadrage rédactionnel conforme à l'intitulé de l'unité `ch06` dans `sources/ch06-sources.md` (ligne 1) et aux termes du `glossaire-termes.json` (`exécution durable`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **U00.2 (L3)** — Question directrice : conditions mesurables de supériorité de la coordination multi-agents et garanties de cohérence transactionnelle face aux pannes.
  - Source : Cadrage méthodologique de l'unité `ch06`, articulant les axes `RQ2` et `RQ3` (`sources/ch06-sources.md`, ligne 4).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P01 — Scénario illustratif, paragraphe 1 (ligne 5)

- **P01.1 (L5)** — Présentation explicitement balisée (« Scénario illustratif. Imaginons... ») d'une équipe déployant un comité de six agents en débat libre pour instruire des réclamations financières.
  - Source : Scénario illustratif explicite (aucune prétention empirique factuelle).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P01.2 (L5)** — Mécanisme narratif de relecture répétée de l'historique complet des pairs et de négociation de consensus à travers plusieurs rondes.
  - Source : Scénario illustratif cohérent avec les mécanismes de coût quadratique et de conformité mesurés dans `[10]` (`SRC-032.txt`, § 4, § K.2, lignes 3205–3211).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P02 — Scénario illustratif, paragraphe 2 (ligne 7)

- **P02.1 (L7)** — Illustration de l'explosion des jetons et de la latence, et de la sous-performance sur des tâches à règles séquentielles strictes face à un agent unique outillé.
  - Source : Scénario illustratif cohérent avec `[1]` (`SRC-003.txt`, § 4.2, `PlanCraft` `-39,1 %` à `-70,0 %`, lignes 674–677).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P02.2 (L7)** — Illustration des comportements observés : imitation mutuelle au sein d'une même famille de modèle, perte des contraintes du premier tour, boucles de reformulation et conclusion prématurée.
  - Source : Scénario illustratif cohérent avec `[6]` (`SRC-028.txt`, FM-1.3, FM-1.4, FM-3.1, lignes 60–96), `[10]` (`SRC-032.txt`, homogénéité, lignes 606–614) et `[15]` (`SRC-006.txt`, rétrécissement d'attention, lignes 1113–1133).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P03 — Scénario illustratif, paragraphe 3 (ligne 9)

- **P03.1 (L9)** — Illustration d'une panne réseau créant une écriture comptable en double après expiration du délai sans clé d'idempotence et d'un arrêt d'urgence bloquant la compensation.
  - Source : Scénario illustratif cohérent avec `[15]` (`SRC-006.txt`), `[16]` (`SRC-033.txt`), `[18]` (`SRC-035.txt`) et `[19]` (`SRC-036.txt`, § 1, lignes 251–258).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P03.2 (L9)** — Synthèse conceptuelle reliant le scénario au besoin d'aborder l'orchestration comme un problème de machines à états durables.
  - Source : Cadrage analytique introductif renvoyant aux sections 6.1–6.4 et à `glossaire-termes.json` (`exécution durable`).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P04 — Transition et annonce de plan (ligne 11)

- **P04.1 (L11)** — Rappel du fil conducteur depuis le chapitre 04 (possession du noyau de contrôle) et le chapitre 05 (alignement sémantique sur standards ouverts).
  - Source : Renvoi structurel interne cohérent avec `glossaire-termes.json` (`noyau de contrôle déterministe`, `ch04`; `couche sémantique métier`, `ch05`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P04.2 (L11)** — Annonce exacte de la structure en quatre sections (`6.1` à `6.4`).
  - Source : Structure vérifiée aux titres des sections `6.1` (L13), `6.2` (L45), `6.3` (L83) et `6.4` (L111).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P05 — Section 6.1, paragraphe 1 (ligne 15)

- **P05.1 (L15)** — Sur des problèmes fermés en un tour sans environnement externe (tels que la génération de courtes fonctions isolées sur des bancs statiques), le vote majoritaire sur plusieurs réponses indépendantes améliore la justesse lorsque les erreurs demeurent faiblement corrélées `[1, 10]`.
  - Source : `[1]` (`SRC-003.txt`, § 1, lignes 82–94, `HumanEval`) et `[10]` (`SRC-032.txt`, § 2, ligne 106; § H.1, lignes 2730–2739).
  - Constat initial : *imprécis* — le texte initial généralisait aux énoncés mathématiques autonomes et présentait le vote indépendant comme corrigeant efficacement les erreurs aléatoires sans mentionner la condition de faible corrélation, alors que `[10]` (lignes 2733–2739) montre sur `GSM-Hard` qu'en raison de la corrélation initiale $\rho(0) \approx 0{,}51$ et d'une faible précision solo (`10 %`), la cohérence interne (*self-consistency*) reste plate de $N=2$ à $N=30$. Rectifié en ciblant les fonctions isolées et la condition de faible corrélation des erreurs.
  - Verdict final : supporté.
- **P05.2 (L15)** — Définition des tâches agentiques : interactions soutenues sur plusieurs tours avec des outils externes, collecte itérative d'information sous observabilité partielle et adaptation de stratégie selon les retours du système `[1]`.
  - Source : `[1]` (`SRC-003.txt`, § 1, lignes 78–80 : *(i) sustained multi-step interactions with an external environment, (ii) iterative information gathering under partial observability, and (iii) adaptive strategy refinement based on environmental feedback*).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P05.3 (L15)** — Sur ces tâches agentiques, transmission d'états partiels divergents, taxe de coordination croissante avec la profondeur et propagation des erreurs en cascade `[1]`.
  - Source : `[1]` (`SRC-003.txt`, § 1, lignes 99–105).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P06 — Section 6.1, paragraphe 2 (ligne 17)

- **P06.1 (L17)** — Prépublication de Stanford de Dat Tran et Douwe Kiela montrant que les gains attribués aux `MAS` proviennent souvent d'une dépense cachée de jetons de raisonnement supplémentaires par rapport au `SAS` `[9]`.
  - Source : `[9]` (`SRC-031.txt`, lignes 1–11 : *Preprint. Under review... Stanford University... often confounded by increased test-time computation*).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P06.2 (L17)** — Application de la `DPI` sur la chaîne de Markov $Y \leftrightarrow C \leftrightarrow M$ avec $M = g(C)$, imposant $I(Y; C) \ge I(Y; M)$ et $P_e(C) \le P_e(M)$ `[9]`.
  - Source : `[9]` (`SRC-031.txt`, § 3, lignes 139–192).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P06.3 (L17)** — La compression du contexte global en messages inter-agents crée un goulot avec perte qui ne peut accroître l'information mutuelle tant que l'agent unique exploite sainement son contexte `[9]`.
  - Source : `[9]` (`SRC-031.txt`, § 3, lignes 14–15, 56–57, 148–150, 191–192).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P07 — Section 6.1, paragraphe 3 (ligne 19)

- **P07.1 (L19)** — Expériences contrôlées sur `FRAMES` et `MuSiQue` à quatre sauts avec `Qwen3-30B-A3B`, `DeepSeek-R1-Distill-Llama-70B`, `Gemini-2.5-Flash` et `Gemini-2.5-Pro`, à budget demandé apparié de `100` à `10 000` jetons de raisonnement `[9]`.
  - Source : `[9]` (`SRC-031.txt`, § 4.1, § 5, § G, lignes 229–231, 327–328, 358–683, 3023–3024).
  - Constat initial : *imprécis* — l'adjectif « strictement apparié » masquait que sur `Gemini 2.5`, l'appariement porte sur le *budget demandé* (`matched requested budget B`, ligne 3023) alors que la consommation effective rapportée diverge. Rectifié en « à budget demandé apparié ».
  - Verdict final : supporté.
- **P07.2 (L19)** — Dès `500` jetons (hors le palier de `100` jetons, trop court pour produire une trace utile), l'agent unique égale statistiquement ou surpasse cinq variantes multi-agents (séquentielle, parallèle par sous-tâches, parallèle par rôles, débat et ensemble) en consommant nettement moins de jetons effectifs `[9]`.
  - Source : `[9]` (`SRC-031.txt`, § 4.3, § 5.1, lignes 256–277, 331–337, Table 1 lignes 504–519, Table 8 lignes 2494–2535).
  - Constat initial : *imprécis* — la version initiale affirmait que l'agent unique égale ou surpasse « systématiquement » de `100` à `10 000` jetons, alors que `SRC-031.txt` (lignes 331–335) exclut explicitement le palier `100` jetons (où `Sequential` et `Debate` dépassent `SAS` en moyenne : `0,364`/`0,370` vs `0,290`, et `0,393` vs `0,308` sur `Gemini-2.5-Pro` `MuSiQue`) et énonce le résultat comme meilleur système ou *statistiquement indiscernable* du meilleur (recouvrement d'IC à `95 %`). Rectifié avec l'exception explicite des `100` jetons et la mention « égale statistiquement ou surpasse ».
  - Verdict final : supporté.
- **P07.3 (L19)** — Mise au jour d'artefacts de comptabilisation et de plafonnement des jetons visibles sur certaines interfaces (notamment `Gemini 2.5`), capables de masquer le calcul réellement consommé `[9]`.
  - Source : `[9]` (`SRC-031.txt`, § G, lignes 2458–2468, 3020–3028).
  - Constat initial : *imprécis* — le texte initial parlait de « facturation et le plafonnement », alors que `SRC-031.txt` n'aborde pas la facturation monétaire (`billing`/`price` absents) mais le décompte API des jetons de réflexion (`API-reported thoughts token count`) et le paramètre `thinkingBudget`. Remplacé « facturation » par « comptabilisation ».
  - Verdict final : supporté.
- **P07.4 (L19)** — Les architectures multi-agents redeviennent compétitives lorsque le contexte de l'agent unique se dégrade fortement sous bruit ou corruption, par exemple à `70 %` de masquage ou de substitution ($\alpha = 0{,}7$), où une chaîne séquentielle structurée filtre mieux les perturbations `[9]`.
  - Source : `[9]` (`SRC-031.txt`, § 5.3, lignes 894–925 : `Sequential` dépasse `SAS` à $\alpha = 0{,}7$ sous masquage et substitution).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P08 — Section 6.1, paragraphe 4 (lignes 21–23)

- **P08.1 (L23)** — Prépublication de Yubin Kim *et al.* (`arXiv:2512.08296`) testant `260` configurations contrôlées à invites, outils et budgets normalisés sur six bancs (`BrowseComp-Plus`, `Finance-Agent`, `PlanCraft`, `Workbench`, `SWE-bench Verified`, `Terminal-Bench`), trois familles (`OpenAI`, `Google`, `Anthropic`) et cinq topologies (`Single-Agent`, `Independent`, `Centralized`, `Decentralized`, `Hybrid`) `[1]`.
  - Source : `[1]` (`SRC-003.txt`, Résumé et § 4.1, lignes 10–13, 128–137, 556–625).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P08.2 (L23)** — Le modèle à effets mixtes explique `37,3 %` de la variance en validation croisée ($R^2 = 0{,}373$; `41,3 %` avec la métrique `ACI` ancrée dans la tâche) et choisit la meilleure architecture dans `87 %` des cas hors échantillon intra-domaine `[1]`.
  - Source : `[1]` (`SRC-003.txt`, lignes 13–21, 141–147, 885–895, 1041–1042, 1608 : *within-domain cross-validated evaluation* `87 %`, alors que la prédiction absolue *leave-one-dataset-out* reste limitée).
  - Constat initial : *imprécis* — l'expression initiale « variance inter-bancs » et « hors échantillon » sans précision laissait croire à une généralisation absolue sur bancs inédits (`LODO`), démentie par § 4.5 (lignes 1525–1531). Précisé en « variance en validation croisée » et « hors échantillon intra-domaine ».
  - Verdict final : supporté.
- **P08.3 (L23)** — Les écarts relatifs face à l'agent unique oscillent entre `+80,8 %` sur `Finance-Agent` (centralisée) et `-70,0 %` sur `PlanCraft` (indépendante), démontrant que l'alignement topologie-tâche prime sur le nombre d'agents `[1]`.
  - Source : `[1]` (`SRC-003.txt`, lignes 18–23, 668, 676).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P09 — Section 6.1, paragraphe 5 (ligne 25)

- **P09.1 (L25)** — Compromis outils-coordination ($\beta = -0{,}096$, $p = 0{,}002$) : jusqu'à `16` outils sur `Workbench`, faisant chuter la topologie hybride (`515 %` de surcoût en tours de coordination à budget apparié) à un succès de `0,21` sur `Workbench` `[1]`.
  - Source : `[1]` (`SRC-003.txt`, lignes 149–151, 649, 902, 947–952, Table 5 ligne 1207).
  - Constat initial : *imprécis* — le texte initial qualifiait `515 %` de « surcoût en jetons », alors que Table 5 définit `O% = (T_MAS - T_SAS)/T_SAS × 100 %` sur les **tours** (`44,3` vs `7,2` tours) dans des expériences appariées en jetons de raisonnement (`4 800` jetons/essai, ligne 1178). Rectifié en « surcoût en tours de coordination à budget apparié ».
  - Verdict final : supporté.
- **P09.2 (L25)** — Plafond de capacité ($\beta = -0{,}236$, $p = 0{,}004$) : au-delà d'environ `45 %` de réussite de base en agent unique, ajouter des agents engendre des rendements décroissants ou négatifs (`94 %` des `16` configurations modèle-banc sur `SWE-bench Verified` et `Terminal-Bench`) `[1]`.
  - Source : `[1]` (`SRC-003.txt`, lignes 15, 152–153, 1532, 1579).
  - Constat initial : *imprécis* — le manuscrit initial généralisait les `94 %` à l'ensemble des paires modèle-banc évaluées sur les six bancs, alors que les lignes 1532 et 1579 restreignent explicitement ce taux de `94 %` aux `16` configurations (`8` modèles × `2` bancs) sur `SWE-bench Verified` et `Terminal-Bench`. Périmètre rectifié.
  - Verdict final : supporté.
- **P09.3 (L25)** — Amplification différentielle des erreurs au niveau de la trace : `17,2×` en topologie indépendante sans vérification contre `4,4×` en coordination centralisée `[1]`.
  - Source : `[1]` (`SRC-003.txt`, lignes 154–157, Table 5 lignes 1226–1233, lignes 1445–1447).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P09.4 (L25)** — Les traces exposent notamment trois dégradations du raisonnement : contradictions logiques, dérive numérique dépassant `5 %` d'écart par rapport à la vérité terrain et omission du contexte antérieur `[1]`.
  - Source : `[1]` (`SRC-003.txt`, § 4.4 *Error Taxonomy*, lignes 1372–1379).
  - Constat initial : supporté (ajout de « notamment » pour refléter l'existence d'une 4e catégorie propre aux `MAS`, *Coordination Failure*).
  - Verdict final : supporté.

### P10 — Section 6.1, paragraphe 6 et équation (lignes 27–31)

- **P10.1 (L27)** — Prépublication de l'Institut Jožef Stefan (`arXiv:2606.02646`) où Blaž Bertalanič et Carolina Fortuna empruntent à Leslie Kish le concept de taille effective d'échantillon corrélé (*effet Ringelmann multi-agents*) `[10]`.
  - Source : `[10]` (`SRC-032.txt`, lignes 1–4, 36–37, 110, 120–124, 717).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P10.2 (L27)** — Modélisation de la corrélation moyenne entre paires d'agents par $\rho_N = c N^{-\beta}$ `[10]`.
  - Source : `[10]` (`SRC-032.txt`, Définition 1, ligne 142).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P10.3 (L29–L31)** — Courbe d'efficacité de Ringelmann $R(N) = \frac{N_{\text{eff}}(N)}{N} = \frac{1}{1 + c(N - 1)N^{-\beta}}$ `[10]`.
  - Source : `[10]` (`SRC-032.txt`, ligne 8, Éq. 2 ligne 147).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P11 — Section 6.1, paragraphe 7 (ligne 33)

- **P11.1 (L33)** — Classification en trois régimes asymptotiques selon $\beta$ : plafond strict à $1/c$ ($\beta = 0$), croissance sous-linéaire en $N^{\beta}/c$ ($0 < \beta < 1$) et linéaire ($\beta \ge 1$) `[10]`.
  - Source : `[10]` (`SRC-032.txt`, lignes 8–10, Proposition 1 lignes 166–184).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P11.2 (L33)** — Sur `44` cellules expérimentales couvrant `Qwen`, `Llama`, `Ministral` (`7` à `32` milliards de paramètres), un modèle à réflexion étendue (`Qwen3-8B`) et une vérification sur API (`Gemini 3.1 Flash-Lite`), ajustement à $R^2 \ge 0{,}97$ (médiane `0,999`) `[10]`.
  - Source : `[10]` (`SRC-032.txt`, lignes 14–18, 238–241, § 5.3 lignes 548–589).
  - Constat initial : *imprécis* — « des modèles à réflexion étendue » au pluriel alors que l'étude évalue un modèle ouvert à réflexion (`Qwen3-8B`) et un modèle API (`Gemini 3.1 Flash-Lite` en réflexion minimale). Modèles précisés.
  - Verdict final : supporté.
- **P11.3 (L33)** — Modèle de champ moyen montrant que le nombre de pairs observés $k$ et le nombre de rondes $\tau$ s'effondrent dans la dynamique en un seul produit $k\tau$ `[10]`.
  - Source : `[10]` (`SRC-032.txt`, Théorème 1, lignes 210–233, § 5.2 lignes 536–545).
  - Constat initial : supporté (précision ajoutée « dans la dynamique »).
  - Verdict final : supporté.

### P12 — Section 6.1, paragraphe 8 (ligne 35)

- **P12.1 (L35)** — À $N = 30$ agents nominaux en débat dense sur `Qwen2.5-7B`, $N_{\text{eff}}$ plafonne à `1,12` sur `MMLU-Hard`, `1,15` sur `GPQA` et `1,79` sur `GSM-Hard` `[10]`.
  - Source : `[10]` (`SRC-032.txt`, Table 17, lignes 3224–3249).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P12.2 (L35)** — Dépense en débat dense de `64 000` à `101 000` jetons d'invite par agent effectif, soit `10` à `46` fois plus que l'autocorrection sans échange entre pairs à $N = 30$ (`1 400` à `10 000` jetons/agent effectif), pour une précision statistiquement équivalente ($\pm 5$ points de pourcentage, test `TOST`) `[10]`.
  - Source : `[10]` (`SRC-032.txt`, § 5.4 lignes 600–603, § K.2 & Table 17 lignes 3205–3255).
  - Constat initial : *imprécis* — le manuscrit attribuait les `1 400` à `10 000` jetons à « l'autocorrection d'un agent unique », alors que Table 17 mesure cette dépense (`Prompt/Neff`) pour la condition *Self-correction* sur l'équipe de $N = 30$ agents sans communication entre pairs (avec comparaison d'équivalence `TOST` à $\pm 5$ pp). Rectifié.
  - Verdict final : supporté.
- **P12.3 (L35)** — Un groupe témoin exposé à du bruit aléatoire de même longueur reproduit presque la courbe d'autocorrection ($c = 0{,}33, \beta = 0{,}27$ contre $c = 0{,}34, \beta = 0{,}25$ sur `GSM-Hard`), démontrant que le gain vient de la réévaluation itérative et non du contenu des pairs `[10]`.
  - Source : `[10]` (`SRC-032.txt`, Table 1 lignes 358–364, § 5.4 lignes 593–597, § H.1 lignes 2723–2729).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P13 — Section 6.1, paragraphe 9 (ligne 37)

- **P13.1 (L37)** — Ni la topologie ni le nombre de rondes ne déplacent la limite en régime plafonné; seule la diversité architecturale (`Qwen + Llama + Ministral`) réduit $\rho(0)$ et abaisse $c$ de `0,85` à `0,54` sur `MMLU-Hard` et de `0,57` à `0,35` sur `GSM-Hard` `[10]`.
  - Source : `[10]` (`SRC-032.txt`, § 5.4 lignes 606–614).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P13.2 (L37)** — Un essai pilote sur $N \le 5$ suffit à calibrer $(c, \beta)$ et à extrapoler jusqu'à $N = 30$ avec `5` à `12 %` d'erreur relative moyenne sur les familles à poids ouverts `[10]`.
  - Source : `[10]` (`SRC-032.txt`, § 5.1 lignes 388–396, § 5.5 lignes 629–630 : `5,5 %` Qwen, `11,9 %` Llama, `5,8 %` Ministral).
  - Constat initial : *imprécis* — formulé initialement comme prédiction « du plafond à $N = 30$ » sans rappeler la plage d'extrapolation ($N \in \{7, 10, 15, 20, 30\}$) ni le périmètre des trois familles à poids ouverts. Rectifié.
  - Verdict final : supporté.

### P14 — Section 6.1, paragraphe 10 (ligne 39)

- **P14.1 (L39)** — Au gel du 2 décembre 2026, `[1]`, `[9]` et `[10]` demeurent des prépublications ouvertes (`arXiv`) et non des études longitudinales en production évaluées par les pairs.
  - Source : `sources/ch06-sources.md` (fiches `[1]`, `[9]`, `[10]`, toutes trois notées `Évalué par les pairs : Non`, dépôt `arXiv`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P14.2 (L39)** — Mise en garde épistémique interdisant d'ériger les coefficients numériques en constantes universelles malgré la convergence des mécanismes.
  - Source : Cadrage méthodologique prudentiel découlant du statut documenté en `P14.1`.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P15 — Section 6.1, paragraphe 11 (lignes 41–43)

- **P15.1 (L41)** — `HAL` (*Holistic Agent Leaderboard*, Kapoor *et al.*) orchestre `21 730` exécutions sur `9` modèles et `9` bancs pour environ `40 000 $ US` de calcul `[8]`.
  - Source : `[8]` (`SRC-030.txt`, Résumé et § 1, lignes 44–46, 95–96).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P15.2 (L41)** — Frontière de Pareto abrupte et clairsemée sur `HAL` : le modèle exécuté le plus onéreux (jusqu'à `15 $ US` / `75 $ US` par million de jetons pour `Claude Opus 4.1` sur huit bancs évalués, contre `0,10 $ US` / `0,40 $ US` pour un modèle frugal) ne figure sur la frontière que sur un seul banc `[8]`.
  - Source : `[8]` (`SRC-030.txt`, § 3, § 4.1, lignes 650–652, 773–778, 938–943 : `Claude Opus 4.1` non exécuté sur `Online Mind2Web` pour limite budgétaire, présent sur `1/8`, et le modèle exécuté le plus coûteux n'est sur la frontière que sur `1` des `9` bancs).
  - Constat initial : *imprécis* — omettait que `Claude Opus 4.1` n'a été évalué que sur `8` des `9` bancs. Périmètre précisé (« modèle exécuté le plus onéreux... sur huit bancs évalués »).
  - Verdict final : supporté.
- **P15.3 (L41)** — L'augmentation de l'effort de raisonnement échoue à améliorer la justesse dans `21` séries sur `36` `[8]`.
  - Source : `[8]` (`SRC-030.txt`, Figure 3 et § 4.1, lignes 745, 956–959).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P15.4 (L43)** — `METR` : l'horizon temporel des tâches logicielles réussies à `50 %` double environ tous les sept mois, mais la réussite chute sous `10 %` au-delà d'environ quatre heures humaines `[4]`.
  - Source : `[4]` (`SRC-025.txt`, lignes 46, 121, 131 : *around 7 months*, *succeed <10% of the time on tasks taking more than around 4 hours*).
  - Constat initial : *imprécis* — « au-delà de quatre heures humaines » omettait l'approximation explicite *around 4 hours* du texte source. Rectifié en « au-delà d'environ quatre heures humaines ».
  - Verdict final : supporté.
- **P15.5 (L43)** — Spécification ouverte `FOCUS v1.4` (FinOps Foundation) normalisant l'imputation des coûts infonuagiques `[2]`.
  - Source : `[2]` (`SRC-023.txt`, Abstract ligne 24, et `sources/ch06-sources.md` fiche `[2]`).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P16 — Section 6.2, paragraphe 1 (ligne 47)

- **P16.1 (L47)** — Loi multiplicative de Lusser formalisée dans le manuel du `NIST` : dix étapes autonomes indépendantes fiables à `94 %` n'aboutissent sans erreur que dans `53,9 %` des cas ($0{,}94^{10} \approx 53{,}86\ \%$) `[3]`, sous les deux hypothèses d'indépendance statistique des mécanismes de défaillance et d'échec de l'ensemble dès la première défaillance `[3]` (impliquant l'absence de boucle de vérification, de reprise ou de redondance).
  - Source : `[3]` (`SRC-024.txt`, § 8.1.8.1, lignes 15–16, 29–34, 53–59, 80–82) et `faits-empiriques.json` (`FACT-LUSSER-10-STEPS`).
  - Constat initial : supporté (précision post-G4 : attribution `[3]` ramenée avant le tiret explicatif pour ne pas prêter au manuel statistique du `NIST` les termes logiciels « boucle de vérification, de reprise ou de redondance »).
  - Verdict final : supporté.
- **P16.2 (L47)** — Renvoi à la partition `80/20` (chapitre 04) pour introduire la hiérarchie normative de sobriété en quatre paliers ordonnés.
  - Source : Renvoi interne cohérent avec `glossaire-termes.json` (`partition 80/20`, `ch04`) et synthèse méthodologique du chapitre.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P17 — Section 6.2, paragraphe 2 (ligne 49)

- **P17.1 (L49)** — Définition architecturale du palier 1 : règle fixe déterministe sans appel de modèle de langage.
  - Source : Construction normative du modèle de sobriété découlant de `P16.1`–`P16.2` et du chapitre 04 (`noyau de contrôle déterministe`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P17.2 (L49)** — Définition architecturale du palier 2 : flux déterministe à appels ponctuels typés où le contrôle de flux et la terminaison restent détenus par le code applicatif.
  - Source : Construction normative cohérente avec la partition `80/20` (`glossaire-termes.json`) et les flux structurés observés en `[5]`.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P18 — Section 6.2, paragraphe 3 (ligne 51)

- **P18.1 (L51)** — Palier 3 (agent unique outillé dans un harnais durci) : justifié pour collecte itérative ou choix dynamique d'outils, conservant le contexte en mémoire unifiée `[1, 9]`.
  - Source : `[1]` (`SRC-003.txt`, lignes 78–80, 95–98, 918–919) et `[9]` (`SRC-031.txt`, lignes 13–22) + `glossaire-termes.json` (`harnais d'agent`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P18.2 (L51)** — Palier 4 (topologie dirigée bornée) conditionné à trois critères : décomposabilité à faible couplage séquentiel `[1]`, saturation du contexte individuel `[9]` (ou séparation architecturale des privilèges imposant un cloisonnement des rôles), et validation centralisée contenant l'amplification d'erreur `[1]`.
  - Source : `[1]` (`SRC-003.txt`, lignes 154–157, 717–721), `[9]` (`SRC-031.txt`, § 3.1, § 5.3), et déduction architecturale pour le cloisonnement des privilèges.
  - Constat initial : *imprécis* — la citation `[9]` figurait après « ou la séparation des privilèges impose un cloisonnement des rôles [9] », alors que Tran et Kiela `[9]` ne traitent que de la saturation/dégradation du contexte, jamais de la séparation des privilèges. Citation `[9]` déplacée directement après « le contexte individuel sature `[9]` ».
  - Verdict final : supporté.
- **P18.3 (L51)** — Rejet en production de l'essaim en débat libre sans hiérarchie ni budget borné.
  - Source : Déduction architecturale immédiate de `[1, 6, 9, 10]`.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P19 — Section 6.2, paragraphe 4 (ligne 53)

- **P19.1 (L53)** — Étude de terrain `MAP` de Melissa Pan *et al.* : `20` équipes interrogées en profondeur, `306` répondants filtrés à `86` systèmes en production ou en phase pilote (enquête descriptive et observationnelle, et non essai contrôlé causal) `[5]`.
  - Source : `[5]` (`SRC-027.txt`, lignes 110–124, 305–315, 344–356).
  - Constat initial : *imprécis* — « en pilote avancé » ajoutait le qualificatif « avancé » absent de `SRC-027.txt` (*in production or pilot phases*, ligne 120). Rectifié en « en phase pilote » et statut descriptif explicité en G4.
  - Verdict final : supporté.
- **P19.2 (L53)** — `68 %` des systèmes déployés exécutent au plus `10` étapes avant toute intervention humaine et `16` études de cas sur `20` (`80 %`) reposent sur un flux structuré fixe plutôt que sur une planification autonome ouverte `[5]`.
  - Source : `[5]` (`SRC-027.txt`, lignes 25, 135, 639–641) et `faits-empiriques.json` (`FACT-MAP-STUDY`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P19.3 (L53)** — La majorité des équipes privilégie des modèles standards sans réentraînement des poids — moins fragiles lors des mises à jour des fournisseurs — (`14/20` = `70 %`) et des invites rédigées ou encadrées manuellement afin de préserver la maîtrise et l'interprétabilité (`79 %` dans le sondage, `19/20` dans les études de cas) `[5]`.
  - Source : `[5]` (`SRC-027.txt`, lignes 541–542, 579–584, 600–635).
  - Constat initial : *imprécis* — rectifié avant G4 puis synthétisé en G4; précision post-G4 rattachant l'absence de réentraînement à la robustesse aux mises à jour (`L581–583`) et les invites manuelles à la maîtrise et l'interprétabilité (`L624–625`).
  - Verdict final : supporté.

### P20 — Section 6.2, paragraphe 5 (lignes 55–59)

- **P20.1 (L59)** — Dans les `20` études de cas approfondies (`14` en production complète et `6` en phase pilote finale, majoritairement dans des organisations établies : `15/20`), `85 %` des équipes (`17` sur `20`) bâtissent leur propre boucle interne par appels `API` directs plutôt que d'adopter un cadriciel tiers `[5]`.
  - Source : `[5]` (`SRC-027.txt`, § 5.5 lignes 676–677, § B.2.1 ligne 1649, § C.2.1 lignes 2174, 2186).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P20.2 (L59)** — Dans l'échantillon élargi du sondage, la part des répondants utilisant un cadriciel atteint `61 %` parmi les systèmes déployés (soit `60,7 %`, `N=29`) et reste quasi identique à `60,5 %` (`N=43`) lorsque l'on inclut les systèmes non déployés, signe que les équipes arrêtent tôt le choix d'une pile avec ou sans cadriciel; dans les études de cas, le sur-mesure répond à l'intégration verticale à l'infrastructure propriétaire et aux pipelines personnalisés, à l'évitement de l'enflure des dépendances et aux politiques de sécurité d'entreprise — deux équipes ayant amorcé leur prototypage avec des cadriciels tels que `CrewAI` avant de migrer vers une solution interne en production pour alléger le surcoût de dépendances `[5]`.
  - Source : `[5]` (`SRC-027.txt`, § 5.5 lignes 679–691, § B.2.1 lignes 1591–1592, 1611, 1643–1660, § D.2 lignes 2481–2484, Figure 22b ligne 2527).
  - Constat initial : *imprécis* majeur — rectifié en G2 initial, puis retouché en G4 avec trois glissements corrigés au contrôle différentiel post-G4 (`pilotes précoces` contredit par `L312–313` et `L2482–2484`; `passées de CrewAI` exclusif au lieu de `tels que CrewAI`; confusion entre « systèmes patrimoniaux » / motifs généraux des études de cas et motif spécifique de réduction des dépendances des deux équipes migrées).
  - Verdict final : supporté.
- **P20.3 (L59)** — Calibrage frugal sur $N \le 5$ unités inspiré de l'« effet Ringelmann » (mesures de traction collective de Maximilien Ringelmann en 1913, transposé par Bertalanič et Fortuna en métaphore quantitative de perte marginale de coordination sans prêter aux modèles une psychologie de groupe), sous les hypothèses restrictives d'équicorrélation $\rho_N = c N^{-\beta}$ et d'étalonnage sur des tâches principalement fermées ou bornées en débat ou vote majoritaire `[10]`.
  - Source : `[10]` (`SRC-032.txt`, lignes 24–25, 35, 110, 125–126, 142, 241–246, 629, 718–719, 747–748, 1204–1205, § C.8 lignes 1386–1416, § K.1 ligne 3150).
  - Constat initial : supporté (« Maximilien Ringelmann » et `1913` expressément vérifiés aux lignes 124, 747–748 et 1204–1205 de `SRC-032.txt`).
  - Verdict final : supporté.

### P21 — Section 6.2, paragraphe 6 (ligne 61)

- **P21.1 (L61)** — La fiabilité technique constitue le principal goulot d'étranglement, poussant la majorité des organisations à s'appuyer sur l'évaluation humaine dans la boucle (`74,2 %`) et sur des essais comparatifs ou retours en conditions réelles plutôt que sur des jeux de test normalisés (`75 %` sans jeux de banc d'essai) `[5]`.
  - Source : `[5]` (`SRC-027.txt`, § 6.1–6.2, § 7, Figure 8, lignes 753–755, 809–823, 858).
  - Constat initial : *imprécis* — rectifié avant G4 puis reformulé en G4; précision post-G4 dissociant les autorisations en lecture seule (`6/20`) ou en bac à sable (`3/20`) de « la majorité des organisations » (ces mesures étant minoritaires, `L1944–1952`).
  - Verdict final : supporté.
- **P21.2 (L61)** — Confinement de plusieurs équipes interrogées par autorisations en lecture seule (`6/20`) ou environnement bac à sable / simulé (`3/20`) `[5]`.
  - Source : `[5]` (`SRC-027.txt`, § B.4.1 *Security practices*, lignes 1944–1952).
  - Constat initial : *imprécis* (portée corrigée au contrôle différentiel post-G4 pour ne pas attribuer ces pratiques à « la majorité des organisations »).
  - Verdict final : supporté.
- **P21.3 (L61)** — Ligne directrice `E-23` révisée du `BSIF` (entrée en vigueur le 1er mai 2027) : demande aux institutions financières fédérales de proportionner validation et suivi au risque inhérent tout au long du cycle de vie, avec d'autres mécanismes de contrôle pour les « approches boîte noire » ou les modèles autonomes `[13]`.
  - Source : `[13]` (`SRC-065.txt`, lignes 177, 258, 458, 532) et `ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`).
  - Constat initial : supporté (ajusté « institutions financières fédérales » et « ou les modèles autonomes » selon l'énoncé exact de la ligne 532).
  - Verdict final : supporté.
- **P21.4 (L61)** — Conventions sémantiques `OpenTelemetry` pour l'IA générative (au statut de développement), séparant `invoke_workflow` (contrôle applicatif) et `invoke_agent` (flux piloté par le modèle) `[11]`.
  - Source : `[11]` (`SRC-037.txt`, lignes 7, 175, 186–197).
  - Constat initial : *imprécis* — omettait que ces conventions ont le statut *Development* (`Status: Development`), pas encore *Stable*. Nuance ajoutée.
  - Verdict final : supporté.

### P22 — Section 6.2, Figure 11 et légende (lignes 63–67)

- **P22.1 (L63)** — Présentation de la figure 11 formalisant l'arbre décisionnel en cinq portes séquentielles.
  - Source : Cadrage rédactionnel décrivant le diagramme `Fig-11.png`.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P22.2 (L65–L67)** — Titre et légende de la figure 11 (« Arbre de sobriété opérationnelle avant toute décomposition multi-agents »).
  - Source : Légende descriptive interne du chapitre 06.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P23 — Section 6.2, paragraphe 8 (ligne 69)

- **P23.1 (L69)** — Renversement de la charge de preuve aux trois premières portes : règle fixe, flux déterministe à appels typés, agent unique outillé à budget égal `[1, 9]`.
  - Source : `[1]` (`SRC-003.txt`) et `[9]` (`SRC-031.txt`) synthétisés dans l'arbre décisionnel.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P23.2 (L69)** — Cinquième porte bloquant tout essaim en débat libre en rappelant les taux d'échec de `41 %` à `86,7 %` mesurés sur sept cadriciels multi-agents dans la taxonomie `MAST` `[6]`.
  - Source : `[6]` (`SRC-028.txt`, ligne 108, Figure 5) et `faits-empiriques.json` (`FACT-MAST-FAILURES`).
  - Constat initial : *imprécis* — rattachait les taux `41 %`–`86,7 %` sans précision contextuelle à la seule idée d'essaim en débat libre, alors qu'ils portent sur sept cadriciels `MAS` d'architectures variées. Précisé « mesurés sur sept cadriciels multi-agents ».
  - Verdict final : supporté.
- **P23.3 (L69)** — Chaque rejet motivé en comité d'architecture évite la sur-ingénierie et l'inflation de jetons avant déploiement pilote `[1, 10]`.
  - Source : Déduction managériale appuyée par les surcoûts mesurés dans `[1]` (`SRC-003.txt`) et `[10]` (`SRC-032.txt`).
  - Constat initial : supporté.
  - Verdict final : supporté.

### T01 — Section 6.2, Tableau 1 et légende (lignes 63–73)

- **T01.1 (L71, L73, L81)** — Annonce, en-têtes et légende du Tableau 1 comparant les cinq architectures d'orchestration.
  - Source : Cadrage synthétique de la section 6.2.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **T01.2 (L75)** — Ligne 1 (`Règle fixe déterministe`) : code applicatif pur, amplification nulle, calcul classique sans inférence, par défaut dès que les règles sont stables.
  - Source : Déduction architecturale directe de la section 6.2 (palier 1).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **T01.3 (L76)** — Ligne 2 (`Flux déterministe à appels typés`) : amplification faible et confinée aux contrôles de validation `[5]`, recommandé (budget égal `[1, 9]`; `80 %` des études de cas `MAP` `[5]`).
  - Source : `[1]` (`SRC-003.txt`), `[9]` (`SRC-031.txt`) et `[5]` (`SRC-027.txt`, § 5.4 `16/20` = `80 %` flux structurés, § 6.2 contrôles basés sur des règles).
  - Constat initial : *imprécis* — employait « schémas de validation » et « `80 %` des cas terrain observés » sans préciser qu'il s'agit des flux structurés des `20` études de cas. Rectifié en « contrôles de validation » et « `80 %` des cas structurés observés ».
  - Verdict final : supporté.
- **T01.4 (L77)** — Ligne 3 (`Agent unique outillé (SAS)`) : erreur croît avec les étapes non vérifiées `[3, 7]`, référence `1×` à budget de calcul égal `[1, 9]`, posture de base si dynamique requise `[1, 9]`.
  - Source : `[1]` (`SRC-003.txt`), `[3]` (`SRC-024.txt`), `[7]` (`SRC-029.txt`) et `[9]` (`SRC-031.txt`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **T01.5 (L78)** — Ligne 4 (`Topologie dirigée bornée`) : amplification contenue à `4,4×` si validation centrale `[1]`, coût contrôlé par pilote $N \le 5$ `[1, 10]`, sous preuve de décomposabilité ou contexte saturé `[1, 9]`.
  - Source : `[1]` (`SRC-003.txt`), `[9]` (`SRC-031.txt`) et `[10]` (`SRC-032.txt`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **T01.6 (L78)** — Ligne 5 (`Essaim libre en débat homogène`) : amplification de `7,8×` (pair-à-pair) à `17,2×` (isolé) `[1]`; `41 %`–`86,7 %` d'échecs `MAS` `[6]`; surcoût `10–46×` (`64K–101K` jetons/$N_{\text{eff}}$) `[10]`; à proscrire `[6, 10]`.
  - Source : `[1]` (`SRC-003.txt`, Table 5 lignes 1230–1231), `[6]` (`SRC-028.txt`), `[10]` (`SRC-032.txt`, Table 17).
  - Constat initial : *imprécis* — attribuait sans nuance `17,2×` à l'essaim en débat homogène, alors que dans Table 5 de `SRC-003.txt`, `17,2×` mesure la topologie `Independent` (isolée) et `7,8×` la topologie `Decentralized` (pair-à-pair). Distribué exactement entre `7,8×` (pair-à-pair) et `17,2×` (isolé).
  - Verdict final : supporté.

### P25 — Section 6.3, paragraphe 1 (ligne 85)

- **P25.1 (L85)** — Article évalué par les pairs publié à *NeurIPS 2025* (`arXiv:2503.13657`), par Mert Cemri, Melissa Pan et collègues, analysant `1 642` traces (`> 1 600`) dans `MAST-Data` `[6]`.
  - Source : `[6]` (`SRC-028.txt`, lignes 1–14, 57–58, 106, 495), `sources/ch06-sources.md` fiche `[6]`, `faits-empiriques.json` (`FACT-MAST-FAILURES`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P25.2 (L85)** — Sept cadriciels ouverts (`MetaGPT`, `ChatDev`, `HyperAgent`, `AppWorld`, `AG2`, `Magentic-One`, `OpenManus`) exécutés avec des modèles `GPT-4`, `Claude`, `Qwen2.5` et `CodeLlama` `[6]`.
  - Source : `[6]` (`SRC-028.txt`, Résumé ligne 34, Table 1 lignes 152–241, Table 3 lignes 1109–1155).
  - Constat initial : *imprécis* — omettait `Qwen2.5` et `CodeLlama` pourtant inclus dans `MAST-Data` (Table 1 et Résumé). Modèles complétés.
  - Verdict final : supporté.
- **P25.3 (L85)** — Taxonomie `MAST` validée par accord inter-annotateurs humains $\kappa = 0{,}88$, couvrant `7` cadriciels et `14` modes de défaillance `[6]`.
  - Source : `[6]` (`SRC-028.txt`, lignes 29–30, 127–128, 451).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P25.4 (L85)** — Taux d'échec mesurés sur leurs bancs respectifs de `41 %` (`AG2` sur `OlympiadBench`) à `86,7 %` (`AppWorld` sur `Test-C`), avec `60,0 %` (`MetaGPT`), `62,0 %` (`Magentic-One`), `66,7 %` (`ChatDev`) et `74,7 %` (`HyperAgent`) `[6]`.
  - Source : `[6]` (`SRC-028.txt`, Figure 5, lignes 1076–1103).
  - Constat initial : *imprécis* — omettait la précision méthodologique de la Figure 5 (« sur leurs bancs respectifs », car mesurés sur des bancs distincts). Précision ajoutée.
  - Verdict final : supporté.

### P26 — Section 6.3, paragraphe 2 et trois puces (lignes 87–93)

- **P26.1 (L87)** — Répartition globale sur les traces annotées : `44,2 %` défauts de conception/spécification, `32,3 %` désalignement inter-agents et `23,5 %` vérification/terminaison, démontrant que la majorité des échecs découle de la structure organisationnelle `[6]`.
  - Source : `[6]` (`SRC-028.txt`, Figure 1 lignes 93–95, Insight 1 ligne 526).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P26.2 (L91)** — Cinq modes de conception/spécification (`44,2 %`) : répétition d'étapes (`15,7 %`), méconnaissance des conditions d'arrêt (`12,4 %`), non-respect des exigences (`11,8 %`), perte d'historique (`2,8 %`), transgression des rôles (`1,5 %`) `[6]`.
  - Source : `[6]` (`SRC-028.txt`, Figure 1 lignes 66–92 et § 4 FC1 lignes 530–531).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P26.3 (L92)** — Six modes de désalignement (`32,3 %`) : discordance raisonnement-action (`13,2 %`), déraillement (`7,4 %`), hypothèses erronées sans clarification (`6,8 %`), réinitialisation (`2,2 %`), ignorance d'un pair (`1,9 %`), rétention d'information (`0,8 %`) `[6]`.
  - Source : `[6]` (`SRC-028.txt`, Figure 1 lignes 67–96 et § 4 FC2 lignes 548–551; note : Figure 1 indique `0.80%` et le texte ligne 550 indique `0.85%`, `0,8 %` assurant la somme exacte à `32,3 %`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P26.4 (L93)** — Trois modes de vérification/terminaison (`23,5 %`) : vérification erronée (`9,1 %`), absente/superficielle (`8,2 %`) et terminaison prématurée (`6,2 %`) `[6]`.
  - Source : `[6]` (`SRC-028.txt`, Figure 1 lignes 71–85 et § 4 FC3 lignes 573–581).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P27 — Section 6.3, paragraphe 3 (ligne 95)

- **P27.1 (L95)** — Les défauts de désalignement surviennent même en langage naturel dans un même cadriciel, montrant que la normalisation syntaxique (ch05) ne supplée pas à l'absence de modèle mental partagé `[6]`.
  - Source : `[6]` (`SRC-028.txt`, § 4 Insight 2 et texte lignes 558–567 : mentionnant explicitement `MCP` et `A2A`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P27.2 (L95)** — Interventions sur `ChatDev` (`ProgramDev-v0`) : réécriture d'invites fait passer de `25,0 %` à `34,4 %`, alors que la refonte topologique — transformant le `DAG` en graphe cyclique borné par un plafond strict d'itérations où seul le `CTO` confirme que les revues sont satisfaites — élève le score à `40,6 %` (`+15,6` pp) `[6]`.
  - Source : `[6]` (`SRC-028.txt`, § 4 ligne 587, § H.2 lignes 1818–1822, Table 5 lignes 1845–1855).
  - Constat initial : *imprécis* — le texte disait « transformant le flux acyclique en graphe borné où seul un superviseur hiérarchique valide la sortie », omettant que la nouvelle topologie décrite par `SRC-028.txt` est explicitement un **graphe cyclique** (*from a directed acyclic graph to a cyclic graph*) borné et que le rôle exact est l'agent **`CTO`**. Rectifié.
  - Verdict final : supporté.
- **P27.3 (L95)** — Traces de `HAL` : piégés dans des boucles répétitives face à des échecs d'outils, des agents usent de mauvaise carte de paiement ou cherchent les réponses sur un dépôt public comme `HuggingFace` ou sur `arXiv` `[8]`.
  - Source : `[8]` (`SRC-030.txt`, lignes 83, 1073, 1087–1088, 1096–1097, Table A6 & A8).
  - Constat initial : *imprécis* — qualifiait ces boucles de « non bornées » alors que `HAL` parle de *trapped in loops* / *repeated failures*, et restait flou sur le « dépôt public ». Rectifié en « piégés dans des boucles répétitives » et « `HuggingFace` (ou sur `arXiv`) ».
  - Verdict final : supporté.

### P28 — Section 6.3, paragraphe 4 et trois points numérotés (lignes 97–101)

- **P28.1 (L99)** — Item 1 (*echo loops* / *retry storms*) : combinaison de la répétition d'étapes (`15,7 %` `[6]`) et de la méconnaissance des conditions d'arrêt (`12,4 %` `[6]`) avec des bus asynchrones ou débats entre pairs.
  - Source : `[6]` (`SRC-028.txt`, Figure 1 lignes 80, 88) et analyse opérationnelle des systèmes réactifs.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P28.2 (L99)** — Dynamique de conformité : chaque ronde de communication contracte le désaccord résiduel selon l'exposant $k\tau$, rapprochant la corrélation mutuelle du consensus sans injecter d'évidence nouvelle `[10]`.
  - Source : `[10]` (`SRC-032.txt`, Théorème 1 Éq. 5, ligne 222 : $\rho_{\text{mf}}(\tau, k) \approx 1 - (1-\rho(0))(1-\alpha_1)^{k\tau}$).
  - Constat initial : *imprécis* — la formule antérieure (« augmente la corrélation mutuelle selon la puissance $k\tau$ ») pouvait laisser croire à une croissance algébrique en $(k\tau)^p$ au lieu de la contraction exponentielle du désaccord résiduel $(1-\alpha_1)^{k\tau}$. Formulé exactement.
  - Verdict final : supporté.
- **P28.3 (L100)** — Item 2 (*backpressure*) : saturation aval faute de files bornées, de sémaphores de concurrence — comme dans l'orchestrateur de `HAL` pour centaines de machines virtuelles `[8]` — et de rejet anticipé.
  - Source : `[8]` (`SRC-030.txt`, lignes 445–448, 1827–1834 : *hundreds of Azure VMs*, *semaphore library*).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P28.4 (L101)** — Item 3 (*unbounded hop depth*) : propagation géométrique du risque d'échec le long des chaînes non bornées `[3]`.
  - Source : `[3]` (`SRC-024.txt`, modèle multiplicatif en série).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P28.5 (L101)** — `τ-bench` (Yao *et al.*) : `gpt-4o` en appel de fonctions atteint `61,2 %` (`τ-retail`) et `35,2 %` (`τ-airline`) au premier essai; `pass^8 < 25 %`; `95,9 %` du coût côté agent provient des instructions et politiques en entrée `[7]`.
  - Source : `[7]` (`SRC-029.txt`, Table 2 lignes 395–397, lignes 488–494 : *For the agent, the input prompt / completion output take up 95.9% / 4.1% of the price*).
  - Constat initial : *imprécis* — présentait `95,9 %` comme part du coût total sans préciser qu'il s'agit du coût **côté agent** (hors simulation d'usager). Précisé « côté agent ».
  - Verdict final : supporté.
- **P28.6 (L101)** — Sur les `36` échecs analysés en `τ-retail`, `33,3 %` tiennent à la résolution partielle de demandes composées et `25 %` dans l'analyse des causes relèvent de décisions contraires aux règles métier (`22,2 %` dans la figure 5) `[7]`.
  - Source : `[7]` (`SRC-029.txt`, Figure 5 lignes 499–509 et § 5.2 lignes 537–544).
  - Constat initial : *imprécis* — attribuait `19 %` (tiré de la ligne 589 *19% of cases* sans précision de dénominateur) comme part des échecs de résolution partielle, alors que Figure 5 indique explicitement `33,3 %` (*Partially resolve*) des `36` échecs analysés en `τ-retail`, et `22,2 %` (*Wrong decision*, `25 %` en texte ligne 539). Rectifié sur les chiffres vérifiés de `τ-retail`.
  - Verdict final : supporté.

### P29 — Section 6.3, paragraphe 5 (ligne 103)

- **P29.1 (L103)** — Plafond dur de sauts et d'itérations (*max hop limit*, et *max iteration cutoff* `[6]`) hors portée du modèle, basculant de manière déterministe en échec explicite ou repli humain.
  - Source : `[6]` (`SRC-028.txt`, § H.2 ligne 1821 : *maximum iteration cutoff to prevent infinite loops*) et principe de contrôle du harnais.
  - Constat initial : *imprécis* — la parenthèse mettait `[6]` après les deux termes anglais, alors que `SRC-028.txt` ne mentionne que *maximum iteration cutoff*. Virgule ajoutée pour rattacher `[6]` uniquement à *max iteration cutoff*.
  - Verdict final : supporté.
- **P29.2 (L103)** — Contre-pression déterministe liant passerelles d'outils et files d'orchestration (budgets de jetons, quotas par fenêtre glissante, files bornées).
  - Source : Patron d'ingénierie réactive découlant directement des pathologies documentées en `P28.3` et du chapitre 04.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P29.3 (L103)** — Évaluation de terminaison et de vérification par assertions typées externes plutôt que par auto-évaluation de l'agent générateur `[6]`.
  - Source : `[6]` (`SRC-028.txt`, § 4 FC3 et § G.2, lignes 584–587, 1717–1724).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P30 — Section 6.3, paragraphe 6 (ligne 105)

- **P30.1 (L105)** — Étude publiée dans *Scientific Reports* en août 2026 : Maytha AL-Ali *et al.* utilisent un simulateur numérique de maintenance critique informé par la physique modélisant la pression opérationnelle sur un opérateur humain simulé `[14]`.
  - Source : `[14]` (`SRC-073.txt`, lignes 11, 46, 190 : *physics-informed predictive maintenance simulator*, *parametric behavioral proxy* de l'opérateur humain).
  - Constat initial : *imprécis* — écrivait « simulateur physique » et « opérateur humain » sans indiquer qu'il s'agit d'un simulateur *numérique informé par la physique* et d'un opérateur humain *modélisé/simulé*. Rectifié.
  - Verdict final : supporté.
- **P30.2 (L105)** — Une IA non calibrée subit un taux d'échec de `12,36 %` contre `0,81 %` après calibration par mise à l'échelle de température `[14]`.
  - Source : `[14]` (`SRC-073.txt`, § *Calibration Impact* ligne 346, § *Practical deployment guidelines* ligne 408).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P30.3 (L105)** — Lorsque la pression de production humaine $\psi \ge 0{,}75$, le taux de défaillance du système hybride remonte brutalement à `6,9 %` puis `12,4 %` (à $\psi = 1{,}0$) indépendamment du conservatisme algorithmique ($\lambda$) `[14]`.
  - Source : `[14]` (`SRC-073.txt`, § *Sensitivity Analysis* ligne 357, § *Practical deployment guidelines* ligne 408).
  - Constat initial : supporté (ajouté « à $\psi = 1{,}0$ » pour situer `12,4 %`).
  - Verdict final : supporté.

### P31 — Section 6.3, paragraphe 7 (lignes 107–109)

- **P31.1 (L109)** — Margaret-Anne Storey montre que le code et les flux générés rapidement par IA créent une **dette cognitive et d'intention** (*cognitive and intent debt*), érodant la « théorie du système » (Naur) et la trace des contraintes et justifications `[12]`.
  - Source : `[12]` (`SRC-040.txt`, lignes 14–23, 40–56, 155–183) et `glossaire-termes.json` (`dette cognitive et d'intention`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P31.2 (L109)** — Externalisation des invariants dans des machines à états explicites comme réponse architecturale à cette double exigence de sûreté et d'intelligibilité.
  - Source : Déduction architecturale reliant `P30`–`P31.1` à la section `6.4`.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P32 — Section 6.4, paragraphe 1 (ligne 113)

- **P32.1 (L113)** — Données `MAP` : `66 %` des agents déployés opèrent dans des tâches tolérant des latences de plusieurs minutes ou plus `[5]`.
  - Source : `[5]` (`SRC-027.txt`, § 1 ligne 129, § 4.4 ligne 442 : *66% allow response times of minutes or longer*).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P32.2 (L113)** — `τ-bench` montre qu'une seule écriture manquée ou partielle compromet l'état final de la base `[7]`.
  - Source : `[7]` (`SRC-029.txt`, § 3 ligne 246–247, § 5.2 lignes 543–544, 586–596).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P32.3 (L113)** — L'architecture de référence associe quatre mécanismes dans le noyau déterministe : exécution durable, idempotence canonique, sagas à point pivot et canal de compensation isolé.
  - Source : Cadrage architectural introduisant la section `6.4` et `glossaire-termes.json`.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P33 — Section 6.4, paragraphe 2 (ligne 115)

- **P33.1 (L115)** — Exécution durable par journal d'événements et rejeu déterministe (SDK `Temporal`), scindant définitions de workflow déterministes (transitions, minuteries, reprise) et activités externes non déterministes (base de données, API externe, et par extension architecturale appel `LLM`) `[17]`.
  - Source : `[17]` (`SRC-034.txt`, lignes 23, 132–135, 160, 176–185).
  - Constat initial : *imprécis* — présentait l'appel à un `LLM` comme un exemple littéral de la documentation `Temporal` (`SRC-034.txt` mentionne *querying a database or calling an external service*). Explicitement balisé comme extension architecturale.
  - Verdict final : supporté.
- **P33.2 (L115)** — Des travailleurs (*workers*) interrogent une `Task Queue` et envoient chaque commande émise et chaque résultat d'activité au service d'orchestration, qui les consigne dans un journal persistant (`Event History`) `[17]`.
  - Source : `[17]` (`SRC-034.txt`, lignes 151–154, 174–181, 217–221).
  - Constat initial : *imprécis* — qualifiait les workers de « sans état particulier » (*stateless* absent de `SRC-034.txt`) et affirmait qu'ils écrivent eux-mêmes vers l'`Event History`, alors que c'est le *Temporal Service* qui ajoute les événements à l'`Event History` à réception des commandes/résultats des workers. Rectifié.
  - Verdict final : supporté.
- **P33.3 (L115)** — Après redémarrage, expiration ou migration de machine, un travailleur rejoue le workflow depuis le journal sans réexécuter les effets déjà validés, tout en levant une erreur de non-déterminisme si le code diverge de l'historique `[17]`.
  - Source : `[17]` (`SRC-034.txt`, lignes 136, 181, 221, 227 : *a non-determinism error gets thrown*).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P33.4 (L115)** — Conventions `OpenTelemetry` : distinguent `invoke_workflow` des spans d'exécution d'outils (*Execute tool*) et normalisent `gen_ai.conversation.id` et `error.type` `[11]`, rejoignant les journaux structurés rejouables (« *tapes* ») évoqués dans les travaux sur la fiabilité multi-agents `[6]`.
  - Source : `[11]` (`SRC-037.txt`, lignes 18, 194, 234, 237, 621–624) et `[6]` (`SRC-028.txt`, § G.2 lignes 1748–1749 : *TapeAgents [80] use a structured, replayable log ("tape")*).
  - Constat initial : *imprécis* — citait littéralement `execute_tool` comme chaîne présente dans `SRC-037.txt`, alors que `SRC-037.txt` renvoie à `execute-tool.md` sous l'intitulé *Execute tool span*. Rectifié en « des spans d'exécution d'outils (*Execute tool*) ».
  - Verdict final : supporté.

### P34 — Section 6.4, paragraphe 3 (ligne 117)

- **P34.1 (L117)** — Selon la `RFC 9110`, `OPTIONS`, `HEAD`, `GET`, `PUT` et `DELETE` sont idempotentes par construction, contrairement à `POST` et `PATCH` : après un `timeout`, le client ignore si le serveur a appliqué l'écriture et réessayer risque de doubler l'opération `[19]`.
  - Source : `[19]` (`SRC-036.txt`, § 1, lignes 247–258).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P34.2 (L117)** — Le projet `HTTPAPI` de l'`IETF` (`Idempotency-Key`) associe à chaque mutation une clé unique — `UUID` ou clé composite imprévisible liée au locataire avec expiration documentée — et, au choix de la ressource, une empreinte de la charge utile (*idempotency fingerprint*) `[19]`.
  - Source : `[19]` (`SRC-036.txt`, § 2.2–2.4, § 5, lignes 297–325, 730–733).
  - Constat initial : *imprécis* — présentait l'empreinte comme obligatoire et « canonique », alors que le brouillon `IETF` (`SRC-036.txt` § 2.4, ligne 321) écrit *A resource MAY compute a fingerprint of the request payload* sans le qualificatif « canonique ». Rectifié en « au choix de la ressource, une empreinte de la charge utile ».
  - Verdict final : supporté.
- **P34.3 (L117)** — Quatre issues lors du réessai : exécuter et mettre en cache si clé neuve; restituer le résultat mémorisé si l'empreinte concorde; retourner `HTTP 409` (`SHOULD`) si la requête initiale est en cours; et rejeter (`HTTP 422` recommandé, échec obligatoire sur réessai non corrigé) si l'empreinte diverge `[19]`.
  - Source : `[19]` (`SRC-036.txt`, § 2.6–2.7, lignes 398–497).
  - Constat initial : *imprécis* — écrivait « rejeter impérativement par `HTTP 422` », alors que `HTTP 422` (comme `HTTP 409`) est normé en `SHOULD` (lignes 447, 470) et que l'obligation `MUST fail` (ligne 496) porte sur la reprise d'une requête en erreur non corrigée par le client. Modalités exactes rétablies.
  - Verdict final : supporté.

### P35 — Section 6.4, paragraphe 4 (ligne 119)

- **P35.1 (L119)** — Garcia-Molina et Salem (1987) démontrent qu'exiger des verrous exclusifs atomiques (de type `ACID`) sur des transactions de longue durée (`LLT`) provoque blocages, interblocages (*deadlocks*) et abandons sur panne `[15, 16]`.
  - Source : `[16]` (`SRC-033.txt`, § 1, lignes 143–226) et `[15]` (`SRC-006.txt`, § 2.1, lignes 163–168, reliant explicitement les sagas aux propriétés `ACID`).
  - Constat initial : *imprécis* — n'attribuait le sigle `ACID` qu'à `[16]` (`SRC-033.txt` ne contient pas le sigle `ACID`). Ajout de `[15]` à côté de `[16]`.
  - Verdict final : supporté.
- **P35.2 (L119)** — Découpage de la `LLT` en sous-transactions localement atomiques $T_1, \dots, T_n$ associées chacune à une transaction compensatoire $C_i$ annulant sémantiquement son effet métier si la suite échoue `[16]`.
  - Source : `[16]` (`SRC-033.txt`, Résumé et § 2, lignes 30–48).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P35.3 (L119)** — Coopération entre `SEC` et `TEC` via un journal dupliqué inscrivant commandes et paramètres de compensation avant exécution, permettant reprise arrière ($C_k \dots C_1$) ou reprise avant depuis des points de sauvegarde persistés `[16]`.
  - Source : `[16]` (`SRC-033.txt`, § 4 et § 6, lignes 1211–1529).
  - Constat initial : supporté.
  - Verdict final : supporté.

### P36 — Section 6.4, paragraphe 5 et trois puces (lignes 121–127)

- **P36.1 (L121)** — `SagaLLM` (Chang et Geng, `arXiv:2503.11951`) : les planificateurs `LLM` échouent pour quatre raisons : auto-validation peu fiable, rétrécissement d'attention faisant oublier des contraintes, absence de sémantique de repli et rupture de coordination `[15]`.
  - Source : `[15]` (`SRC-006.txt`, § 1–2, § 6, lignes 11–14, 130–133, 927–933, 1573–1576).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P36.2 (L121)** — Sur le banc `REALM`, des modèles isolés en replanification réactive violent des contraintes temporelles ou de sûreté pourtant explicitement énoncées dans l'invite initiale `[15]`.
  - Source : `[15]` (`SRC-006.txt`, § 5.1–5.3, lignes 957–966, 1113–1133, 1359–1422).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P36.3 (L123)** — `SagaLLM` couple passage de relais humain/automatisé, maintien de trois plans d'état externes ($S_A$, $S_O$, $S_D$) et validateurs indépendants maintenus dans un contexte borné (sous `1 000` jetons dans leurs études de cas) `[15]`, matérialisant les contraintes hors contexte volatil selon Storey `[12]`.
  - Source : `[15]` (`SRC-006.txt`, Table 2 lignes 346–389, Figure 2 lignes 550–601, § 5.2.3 ligne 1186 : *each maintaining a context of less than $1k$*) et `[12]` (`SRC-040.txt`, lignes 168–173).
  - Constat initial : *imprécis* — formulait « maintenus sous `1 000` jetons » comme invariant général de `SagaLLM`, alors que la limite `< 1k` est précisée pour les validateurs dans l'étude de cas `P9` (ligne 1186). Précisé « dans un contexte borné (sous `1 000` jetons dans leurs études de cas) ».
  - Verdict final : supporté.
- **P36.4 (L121–L127)** — Déduction architecturale explicite encadrant la saga autour du point pivot en trois zones : étapes pré-pivot compensables ($T_1, T_2$, inverse $C_1, C_2$ journalisés `[15, 16]`), garde et point pivot irréversible ($T_P$, vérification $S_D$ `[15]` et approbation ch07), et étapes post-pivot réessayables ($T_3$, reprise avant `[16]`, idempotence `[19]`, rejeu durable `[17]`).
  - Source : Déduction architecturale explicitement signalée (« Par déduction architecturale ») combinant `[15, 16, 17, 19]` et renvoyant au chapitre 07.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P37 — Section 6.4, paragraphe 6 (ligne 129)

- **P37.1 (L129)** — Déduction architecturale explicite : le coupe-circuit ne doit stopper que le flux direct vers $T_P$ et aiguiller les compensations sur un canal dédié afin d'éviter un état à moitié engagé.
  - Source : Déduction architecturale explicitement balisée (« Par déduction architecturale »).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P37.2 (L129)** — `CloudEvents v1.0.2` (`CNCF`) sépare attributs routables (`id`, `source`, `type`, `specversion`) et charge utile (`data`), permettant le routage sans désérialisation du contenu et la déduplication sur le couple unique `source` + `id` `[18]`.
  - Source : `[18]` (`SRC-035.txt`, lignes 158–160, 246–333 : *REQUIRED attributes*, inspection sans désérialiser `data`, unicité et déduplication sur `source` + `id`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P37.3 (L129)** — Des travailleurs déterministes isolés exécutent $C_2$ puis $C_1$ jusqu'à clôture du journal même si le fournisseur `LLM` ou le flux direct sont hors service `[16, 17, 18]`.
  - Source : Synthèse architecturale s'appuyant sur la clôture saga de `[16]`, les files et workers dédiés de `[17]` et l'enveloppe neutre `[18]`.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P38 — Section 6.4, Figure 12, légende et commentaire (lignes 131–137)

- **P38.1 (L131–L135)** — Annonce, inclusion et légende de la figure 12 (*Exécution durable et Saga à point pivot dotée d'un canal de compensation isolé*).
  - Source : Cadrage interne de la figure `Fig-12.svg`.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P38.2 (L137)** — Décision 1 : cantonner le composant probabiliste à la synthèse préparatoire en amont sans accès direct aux écritures ni à l'improvisation du repli `[15, 17]`.
  - Source : `[15]` (`SRC-006.txt`) et `[17]` (`SRC-034.txt`) appliqués au modèle de la figure 12.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P38.3 (L137)** — Décision 2 : journal à rejeu déterministe et clé d'idempotence verrouillant $T_1, T_2$ avant validation des invariants de $T_P$ `[15, 17, 19]`.
  - Source : `[15]` (`SRC-006.txt`), `[17]` (`SRC-034.txt`) et `[19]` (`SRC-036.txt`).
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P38.4 (L137)** — Décision 3 : toute anomalie pré-pivot déclenche le coupe-circuit sur le seul flux direct tout en laissant le canal isolé exécuter $C_2 \to C_1$ jusqu'à clôture `[16, 18]`.
  - Source : `[16]` (`SRC-033.txt`) et `[18]` (`SRC-035.txt`) selon l'architecture de la figure 12.
  - Constat initial : supporté.
  - Verdict final : supporté.

### T02 — Section 6.4, Tableau 2 et légende (lignes 125–134)

- **T02.1 (L139, L141, L148)** — Annonce, en-têtes et légende du Tableau 2 comparant les régimes de gestion d'état, d'idempotence et de compensation.
  - Source : Cadrage comparatif de la section `6.4`.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **T02.2 (L143)** — Ligne 1 (`Essai unique en mémoire vive`) : aucune persistance au redémarrage, échec sur coupure réseau, état orphelin et perte du contexte sur arrêt d'urgence.
  - Source : Propriétés élémentaires d'une exécution non persistée en mémoire vive.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **T02.3 (L144)** — Ligne 2 (`Réessai aveugle sans clé canonique`) : risque élevé de doubles écritures `[19]`; mutations partielles non annulées `[7]`.
  - Source : `[19]` (`SRC-036.txt`, § 1, doubles mutations sur réessais sans clé) et `[7]` (`SRC-029.txt`, § 5.2, écritures partielles de requêtes composées).
  - Constat initial : *imprécis* — citait `[7, 19]` sur les doubles écritures par réessai aveugle alors que `[7]` ne traite pas des réessais réseau sans clé, mais des mutations partielles non complétées. Citations réaffectées exactement.
  - Verdict final : supporté.
- **T02.4 (L145)** — Ligne 3 (`Verrou distribué strict (ACID)`) : journal couplé, blocage durant latences longues `[15, 16]`, forte contention `[16]`.
  - Source : `[15]` (`SRC-006.txt`, § 2.1) et `[16]` (`SRC-033.txt`, § 1).
  - Constat initial : *imprécis* — `ACID` n'était sourcé que sur `[16]` alors qu'il est explicite dans `[15]`. Citation `[15]` ajoutée.
  - Verdict final : supporté.
- **T02.5 (L146)** — Ligne 4 (`Exécution durable + Idempotence canonique + Saga isolée`) : journal à rejeu déterministe `[17]` et traces corrélées `[11]`; exécution unique effective dans la fenêtre de rétention sur clé et empreinte validée `[19]`; repli $C_2 \to C_1$ avant pivot et suite forcée après $T_P$ `[15, 16]`; coupe le flux direct tout en acheminant la compensation sur enveloppe isolée `[18]`.
  - Source : `[11]` (`SRC-037.txt`), `[15]` (`SRC-006.txt`), `[16]` (`SRC-033.txt`), `[17]` (`SRC-034.txt`), `[18]` (`SRC-035.txt`), `[19]` (`SRC-036.txt`).
  - Constat initial : *imprécis* — associait `[11]` (`OpenTelemetry`) au rejeu déterministe, parlait d'« exactement-une-fois effectif » sans mentionner la fenêtre d'expiration documentée dans `[19]` (§ 2.3), et attribuait directement le mécanisme de coupe-circuit à `[18]` (`CloudEvents` fournissant l'enveloppe routable isolée). Rectifié sur les trois colonnes.
  - Verdict final : supporté.

### P40 — Section 6.4, clôture réglementaire (ligne 150)

- **P40.1 (L150)** — Un système combinant rejeu sur journal immuable `[17]`, unicité prouvée des écritures `[19]` et compensation sous arrêt d'urgence `[15, 16, 18]` établit les contrôles de cycle de vie attendus avant l'entrée en vigueur de la ligne directrice `E-23` du `BSIF` le 1er mai 2027 `[13]`.
  - Source : `[13]` (`SRC-065.txt`, lignes 177, 484–486), `[15]`, `[16]`, `[17]`, `[18]`, `[19]`, et `ancres-chronologiques.json` (`2027-05-01-BSIF-E23-AMF`).
  - Constat initial : supporté.
  - Verdict final : supporté.

### E01 — Encadré : Trois arbitrages sans regret — Chapitre 06 (lignes 152–156)

- **E01.1 (L154)** — Arbitrage 1 : test de sobriété à budget égal avant tout projet multi-agents, pilote sur $N \le 5$ nœuds et préférence pour la diversité architecturale (synthèse des sections 6.1–6.2, appuyée par `[1, 9, 10]`).
  - Source : Synthèse prescriptive des résultats vérifiés aux paragraphes `P06`–`P21`.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **E01.2 (L155)** — Arbitrage 2 : plafonds durs de sauts/itérations, critères déterministes de terminaison, files avec contre-pression et validateurs indépendants (synthèse de la section 6.3, appuyée par `[1, 6, 8, 10, 15]`).
  - Source : Synthèse prescriptive des résultats vérifiés aux paragraphes `P25`–`P31`.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **E01.3 (L156)** — Arbitrage 3 : séparation orchestration rejouable / activités probabilistes, clés d'idempotence avec empreinte, garde avant point pivot et canal de compensation isolé (synthèse de la section 6.4, appuyée par `[15, 16, 17, 18, 19]`).
  - Source : Synthèse prescriptive des mécanismes vérifiés aux paragraphes `P32`–`P38`.
  - Constat initial : supporté.
  - Verdict final : supporté.

### P41 — Clôture de la Partie II et transition vers le chapitre 07 (ligne 158)

- **P41.1 (L158)** — Bilan de la Partie II (chapitres 04 à 06) : noyau de contrôle possédé, protocoles ouverts sur couche sémantique, parcimonie multi-agents et exécution transactionnelle durable.
  - Source : Synthèse structurelle de la Partie II cohérente avec `P04.1` et `glossaire-termes.json`.
  - Constat initial : supporté.
  - Verdict final : supporté.
- **P41.2 (L158)** — Ouverture de la Partie III (*La fabrique de confiance et l'économie de la preuve*) au chapitre 07 sur l'identité non humaine et la chaîne de mandat.
  - Source : Transition éditoriale cohérente avec `glossaire-termes.json` (`identité non humaine`, `délégation au nom de`, `chapitre_proprietaire: ch07`).
  - Constat initial : supporté.
  - Verdict final : supporté.

---

## Contrôle différentiel post-G4

- **Objet** : Audit `G2` différentiel post-retouche stylistique `G4` portant sur les lignes modifiées `L27` et `L47–L81` du chapitre 06 ainsi que sur l'alignement terminologique avec `7 - Livre/diagrammes/Fig-11.mmd`.
- **Corpus vérifié directement en texte intégral (`corpus_l_plus/*.txt`)** : `SRC-003.txt` (`[1]`), `SRC-024.txt` (`[3]`), `SRC-027.txt` (`[5]`), `SRC-028.txt` (`[6]`), `SRC-029.txt` (`[7]`), `SRC-031.txt` (`[9]`), `SRC-032.txt` (`[10]`), `SRC-037.txt` (`[11]`), `SRC-065.txt` (`[13]`).

### Constats différentiels et vérifications ciblées

1. **`L27` et `L55–L57` (`SRC-032.txt` `[10]`) — Ringelmann** :
   - **Vérifié supporté** : `Maximilien Ringelmann` et `1913` sont explicitement attestés dans `SRC-032.txt` (ligne 110 : `Ringelmann effect [Ringelmann, 1913]`; lignes 747–748 : `Maximilien Ringelmann. Recherches sur les moteurs animées: Travail de l’homme. Annales de l’Institut National Agronomique, 12:1–40, 1913`; lignes 1204–1205 : `Ringelmann’s [1913] rope-pulling data`). Maintien intégral de « Maximilien Ringelmann en 1913 ».
   - **Vérifié supporté** : équicorrélation $\rho_N = c N^{-\beta}$ (`SRC-032.txt`, lignes 125–126, 142), courbe $R(N)$ (ligne 147), pilote sur $N \le 5$ (lignes 24–25, 629, 3150) et étalonnage sur tâches principalement fermées ou bornées (lignes 241–246, § C.8 lignes 1386–1416).
2. **`L47` (`SRC-024.txt` `[3]`) — Loi de Lusser (`NIST`)** :
   - **Écart corrigé** : `SRC-024.txt` (lignes 15–16, 29–34, 80–82) formalise deux hypothèses (indépendance des mécanismes de défaillance et échec du système dès la première défaillance), sans employer les termes logiciels « boucle de vérification, de reprise ou de redondance ». Le renvoi `[3]` a été replacé avant le tiret explicatif introduisant cette conséquence architecturale.
3. **`L53` (`SRC-027.txt` `[5]`) — `MAP`** :
   - **Écart corrigé** : précisé que l'absence de réentraînement des poids (`14/20`) répond à la fragilité lors des mises à jour des fournisseurs (`SRC-027.txt`, lignes 579–584), tandis que les invites rédigées ou encadrées manuellement (`79 %`, `19/20`) visent la maîtrise et l'interprétabilité (lignes 624–625).
4. **`L59` (`SRC-027.txt` `[5]`) — `MAP` (`85 %`, `17/20`, `14`/`6`, `60,7 %`, `60,5 %`, `CrewAI`)** :
   - **Vérifiés supportés** : `85 %` (`17/20`), `14` en production complète / `6` en phase pilote finale (`L2186`), majorité d'organisations établies (`15/20`, `L2174`), `61 %` (`60,7 %`, `N=29`, `L679`, `L1592`, `L1611`) et `60,5 %` (`N=43`, `L2527`).
   - **Écarts corrigés** : (a) retiré l'affirmation selon laquelle la tension `85 %` vs `60,7 %` s'explique par des « pilotes précoces et usages exploratoires » dans le sondage — `60,7 %` porte déjà sur les systèmes déployés (`L312–313`: *not small pilots*), et la quasi-identité avec `60,5 %` indique selon `SRC-027.txt` (`L2482–2484`) que les équipes arrêtent tôt le choix d'une pile; (b) corrigé « deux équipes passées de `CrewAI` » en « deux équipes rapportant explicitement avoir amorcé leur prototypage avec des cadriciels tels que `CrewAI` » (`L680–681`: *e.g., CrewAI*, `L1651`: *like CrewAI*); (c) distingué les trois moteurs généraux des études de cas (intégration verticale à l'infrastructure propriétaire et aux pipelines personnalisés — plutôt que « systèmes patrimoniaux » —, enflure des dépendances, politiques de sécurité, `L683–691`, `L1653–1660`) du motif rapporté pour les deux migrations (alléger le surcoût de dépendances, `L1652`).
5. **`L61` (`SRC-027.txt` `[5]`, `SRC-065.txt` `[13]`, `SRC-037.txt` `[11]`)** :
   - **Écart corrigé** : dissocié « la majorité des organisations » (vrai pour l'évaluation humaine à `74,2 %` et l'absence de jeux de test normalisés à `75 %`) des autorisations en lecture seule (`6/20`) ou en bac à sable (`3/20`), qui concernent plusieurs équipes mais non la majorité (`SRC-027.txt`, lignes 1944–1952). `BSIF E-23` (`[13]`) et `OpenTelemetry` (`[11]`) vérifiés conformes.
6. **`L63–L81` et `Fig-11.mmd` — Alignement terminologique et données Tableau 1** :
   - **Vérifié conforme** : ni `Fig-11.mmd` ni `ch06` ne contiennent `échelon` ni aucun jargon matriciel (`Palier` avec majuscule ou `matrice`); la terminologie `palier` (en minuscule, 1er à 4e palier) est uniforme dans le chapitre et parfaitement cohérente avec les nœuds `Q1`–`Q5` / `R1`–`R6` de `Fig-11.mmd`.
   - **Vérifié supporté** : toutes les données de `L63–L81` (`41 %–86,7 %` `[6]`, `7,8×` / `17,2×` / `4,4×` `[1]`, `10–46×` et `64K–101K` `[10]`, `80 %` `MAP` `[5]`, `N <= 5` `[10]`) sont exactes contre leurs sources respectives.

### Certification différentielle post-G4

- **Taux de support post-rectification** : **`100 %` `supporté`**
- **Imprécis résiduels** : **`0`**
- **Non supportés résiduels** : **`0`**

---

## Contrôle différentiel post-lissage G5

- **Date et portée** : 2026-11-22 — Audit différentiel indépendant `auditeur-wyvern` (`git diff HEAD` depuis `fe6e945`) sur `ch06` (`36` éléments différentiels contrôlés : `24` lignes de retrait mécanique de rétro-apostrophes vérifiées exactes sur sigles/identifiants et `12` blocs substantiels couvrant `L5`, `L21–L23`, `L47`, `L57–L59`, `L61`, `L63–L65`, `L71`, `L97`, `L107–L109`, `L115`, `L117`, `L119`).
- **Primaires `L+` vérifiés** : `SRC-003.txt` (`[1]`), `SRC-024.txt` (`[3]`), `SRC-027.txt` (`[5]`), `SRC-028.txt` (`[6]`), `SRC-030.txt` (`[8]`), `SRC-031.txt` (`[9]`), `SRC-032.txt` (`[10]`), `SRC-033.txt` (`[16]`), `SRC-034.txt` (`[17]`), `SRC-036.txt` (`[19]`), `SRC-037.txt` (`[11]`), `SRC-040.txt` (`[12]`), `SRC-065.txt` (`[13]`), `SRC-073.txt` (`[14]`), `sources/ch06-sources.md`, `diagrammes/Fig-11.mmd` et renvoi au chapitre 11 (`L107–L109`).
- **Rectifications appliquées dans le manuscrit (`5`)** :
  1. `L47` (`NIST/SEMATECH` `SRC-024.txt` § 8.1.8.1) : replacé `[3]` avant la conséquence architecturale sur le harnais et rétabli les deux hypothèses effectives de Lusser (indépendance des défaillances et échec dès la première erreur) au lieu d'attribuer « harnais », « assertions déterministes » et « hypothèse d'absence de vérification » à `[3]`.
  2. `L59` (`MAP` `SRC-027.txt` L680–685) : rétabli « s'intégrer à l'infrastructure et aux pipelines propriétaires » et « avec des cadriciels tels que CrewAI » (*e.g., CrewAI*).
  3. `L71` (`Tran & Kiela` `SRC-031.txt` `[9]`, `Kim et al.` `[1]`, `Bertalanič & Fortuna` `[10]`, `Fig-11.mmd`) : rétabli l'attribution exacte du goulot d'information central à `[9]` et de la perte marginale de coordination à `[1, 10]` à la quatrième porte.
  4. `L107` (`AL-Ali et al.` `SRC-073.txt` L46, L190, L346, L357, L408) : rétabli « simulateur numérique de maintenance critique informé par la physique » et « opérateur humain simulé » afin de respecter le statut de proxy comportemental paramétrique documenté dans `[14]`.
  5. `L115` (`Temporal` `SRC-034.txt` L160, L176–182) : rétabli « ou, par extension architecturale, l'appel à un LLM » et corrigé le flux d'écriture vers l'*Event History* (« transmettent chaque commande et résultat d'activité au service d'orchestration, qui les consigne dans un journal persistant (*Event History*) [17] ») au lieu d'imputer l'écriture directe aux travailleurs.
- **Verdict différentiel final post-G5** : `36 / 36` items (`100 %` `supporté`), **`0` imprécis résiduel**, **`0` non supporté résiduel**, aucun tableau ajouté ni supprimé, aucune collision `CA-03` ni motif `CA-02`.

---

## Réindexation différentielle post-audit v1.3 (2 décembre 2026)

- **Périmètre `v1.3`** : `manuscrit/02 - Partie II/Chapitre 06 - Sobriete d orchestration et execution durable.md` (`164` lignes, `6 484` mots `G1` / `6 796` `split()`), `19` sources `L+`.
- **Mises à jour et réancrages vérifiés** :
  - `L21–L23`, `L35`, `L55–L59`, `L78–L79`, `L93–L97`, `L103–L107`, `L129–L133` : scission des phrases longues (`L35`, `L103`), aération des listes (`MAST`, pathologies, saga), uniformisation typographique `pass⁸` (`τ-bench` `< 25 %` `[7]` `SRC-029.txt`) et vérification contre `[2]` `SRC-023.txt`, `[4]` `SRC-025.txt` et `[11]` `SRC-037.txt`. `Verdict : supporté`.
  - `L117–L119`, `L139` (`Tableau 6.2`) : précision de la variante `SagaLLM` (`C1..Cn`) et réalignement des lignes. `Verdict : supporté`.
