# Journal d'ancrage atomique Wyvern — Chapitre 02

- **Unité :** `ch02` (`Compendium/ouvrage/manuscrit/01 - Partie I/Chapitre 02.md` — *Chapitre 02 — Fiabilité de l'automatisation agentique face au déterminisme : loi de Lusser, cascades inter-systèmes et constance pass^k*)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch02-sources.md` (`9` sources intégrales `L+`, `SHA-256`)
- **Registres vérifiés :** `registre/faits-empiriques.json`, `registre/ancres-chronologiques.json`, `registre/glossaire-termes.json`
- **Auditeur :** `wyvern-02` (barrière indépendante `G2`, `AO-07`, régime Production)
- **Date d'audit :** 2026-11-25 (gel factuel : `2026-12-02`)
- **Volume final vérifié :** `3 969` mots de prose `G1` (plage `[3 552, 4 168]`)

## Synthèse quantitative de l'audit

- **Affirmations atomiques vérifiables :** 44 (`C02-01` à `C02-44`)
- **Passe G2 initiale (supportés) :** 23 / 44 (52,3 %)
- **Énoncés rectifiés lors de la passe G2 :** 21 / 44 (réancrés intégralement sur `corpus_l_plus/*.txt` et `registre/`)
- **Verdict final — supportés :** 44 / 44 (100,0 %)

---

## Détail complet par paragraphe et tableau

### Titre, question directrice et introduction (`L1–L7`)

- **C02-01** (`L5`) : À la différence des pannes franches (`HTTP 500`, exception, délai dépassé), un maillon cognitif probabiliste échoue fréquemment en silence sémantique en retournant un JSON bien formé sous statut `HTTP 200 OK`, ce qui expose une chaîne sans coupure déterministe à une dégradation en série [9].
  - Preuve L+ : `SRC-055.txt` (`ASI08: Cascading Failures`, p. 30–32 : fautes silencieuses contournant les contrôles par étapes sous activité apparemment conforme).
  - Statut initial : rectifié (reformulation de « échoue rarement en silence technique » pour éviter toute ambiguïté).
  - Verdict : supporté

- **C02-02** (`L7`) : Le chapitre structure la démonstration autour de `OWASP ASI08`, de la loi de Lusser, de la taxonomie `MAST` face à l'agent unique continu, de la primauté de `pass^k` sur `pass@k`, de la borne statistique de Wilson et des biais des palmarès publics.
  - Preuve L+ : cohérence interne de plan vérifiée sur l'ensemble des sections `2.1` à `2.3` et des sources `[1]`–`[9]` de `ch02-sources.md`.
  - Statut initial : supporté.
  - Verdict : supporté

---

### Section 2.1.1 — Rupture entre validité syntaxique et erreurs sémantiques silencieuses (`L13–L21`)

- **C02-03** (`L13`) : Une chaîne d'agents est non compositionnelle : deux maillons satisfaisant isolément leurs tests syntaxiques et politiques locales peuvent former un chemin composé dangereux une fois raccordés bout à bout [9].
  - Preuve L+ : `SRC-055.txt` (`ASI08`, p. 30–31 : une faute unique traverse des agents autonomes et contourne les contrôles locaux).
  - Statut initial : rectifié (suppression du code interne `H-24` absent des sources `L+` et réancrage direct sur `[9]`).
  - Verdict : supporté

- **C02-04** (`L13`) : Un agent basé sur un modèle linguistique ne garantit pas un résultat identique d'une exécution à l'autre — même à température `0,0` pour l'agent selon `τ-bench` [6] — et reste sensible aux variations de harnais, de latence et de quantification côté fournisseur selon `HAL` [7].
  - Preuve L+ : `SRC-029.txt` (L383 : température agent `0.0` ; L486–490 : instabilité `pass^8 < 25 %`) ; `SRC-030.txt` (L472–475 : changements silencieux de poids/quantification ; L1136–1137, L1962 : variance de latence).
  - Statut initial : rectifié (remplacement de la mention `p99` non mesurée dans `ch02-sources.md` par les constats vérifiés dans `SRC-029` et `SRC-030`).
  - Verdict : supporté

- **C02-05** (`L15`) : La transmission d'un montant hors taxes dans un champ JSON `montant_total` valide illustre le risque `ASI08` documenté dans *OWASP Top 10 for Agentic Applications 2026* (`SRC-055` en statut `L+`, tandis que `genai.owasp.org` reste au statut F pour blocage `HTTP 403`) [9].
  - Preuve L+ : `SRC-055.txt` (p. 30–32, `ASI08`) et `ch02-sources.md` (L97–L112 : `SRC-055` L+ et exclusion `HTTP_403` sur `genai.owasp.org`).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-06** (`L17`) : L'étude de Rory Milsom (`1er décembre 2025`, `arXiv:2512.02230`) montre que `GPT-4o` sous `OpenHands` résout `0/12` tâches financières initiales de `TheAgentCompany` (`14,8 %` des points de contrôle) et `2/12` nouvelles tâches patrimoniales à autonomie élevée (`49,0 %` des `49` points de contrôle) en raison de défauts d'accès, de chemins et de format de livraison [3].
  - Preuve L+ : `SRC-124.txt` (L1–32 : métadonnées ; Table 4.1, L1272–1294 : `0/12`, `8/54 = 14.8%`, `2/12`, `24/49 = 49.0%`).
  - Statut initial : rectifié (suppression de l'attribution erronée à Milsom des facteurs `17,2×` et `4,4×` absents de `SRC-124.txt`, remplacés par les mesures exactes de `SRC-124.txt`).
  - Verdict : supporté

- **C02-07** (`L17`) : Dans la même étude (`SRC-124`), l'imposition de schémas et de chemins explicites (autonomie réduite) double la résolution à `4/12` tâches et élève les points de contrôle réussis à `69,4 %` (`34/49`) à coût moyen légèrement moindre (`0,1237 \$` contre `0,1373 \$`) [3].
  - Preuve L+ : `SRC-124.txt` (Table 4.2, L1424–1449 : `4/12 vs. 2/12`, `34/49 = 69.4%` vs `49.0%`, `$0.1237` vs `$0.1373`).
  - Statut initial : rectifié (remplacement des chiffres non sourcés dans `[3]` par les résultats vérifiés de la Table 4.2 de `SRC-124.txt`).
  - Verdict : supporté

- **C02-08** (`L17`) : Les mesures comparatives d'architectures multi-agents de Kim et coll. (analysées au Chapitre 13) montrent une amplification d'erreurs de trace jusqu'à `17,2×` sans vérificateur central contre `4,4×` sous coordination centralisée.
  - Preuve L+ : `corpus_l_plus/SRC-003.txt` (L155–156, L195 : `17.2×` unchecked error amplification vs `4.4×` centralized coordination).
  - Statut initial : rectifié (restitution de l'attribution exacte à Kim et coll. / `SRC-003` au lieu de `[3]`).
  - Verdict : supporté

- **C02-09** (`L19`) : Les pathologies de boucle associent amplification d'appels API (`HTTP 429`), boucles de rétroaction entre agents [9], répétition stérile d'étapes (`13,2 %` des défaillances sur le corpus `MAST`) [4] et défauts de vérification ou d'arrêt (`23,5 %`) en l'absence d'oracle externe [4].
  - Preuve L+ : `SRC-055.txt` (L452 `Loop amplification`, p. 31 `Feedback-loop amplification`) ; `SRC-028.txt` (Figure 1, L68, L82 `13.2%` `Step Repetition`, L95 `23.5%` `Task Verification`).
  - Statut initial : rectifié (suppression de la statistique `27,9 %` absente de tout fichier `corpus_l_plus/*.txt`, remplacée par les taux vérifiés `SRC-028` et `SRC-055`).
  - Verdict : supporté

- **C02-10** (`L21`) : Le Compendium prescrit des assertions sémantiques déterministes (`EXIG-INT-02`), des disjoncteurs de débit et des compteurs de sauts (`xagenthopcount`, `xagentmaxhops` sous `EXIG-EVT-06` et `EXIG-ORC-04`) pour interrompre et escalader toute dérive.
  - Preuve L+ : prescriptions architecturales normatives du Compendium adossées aux mesures de contrôle de `SRC-055.txt` (p. 32 `ASI08` mitigations 3–5) et `SRC-124.txt` (L1424–1449).
  - Statut initial : supporté.
  - Verdict : supporté

---

### Section 2.1.2 — Loi de Lusser, taxonomie `MAST` et saturation d'horizon `METR` (`L25–L39`)

- **C02-11** (`L25–L27`) : Selon le manuel statistique NIST/SEMATECH (§ `8.1.8.1`), la fiabilité globale d'une séquence de `n` mécanismes de défaillance indépendants en série obéit au produit $R = \prod_{i=1}^{n} p_i = p^n$ [1].
  - Preuve L+ : `SRC-024.txt` (L19–78 : `Competing risk model`, $R_c(t) = \prod_{i=1}^k R_i(t)$ sous indépendance et première défaillance critique).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-12** (`L29`) : Avec une fiabilité unitaire de `94 %` sur `10` étapes, le taux de succès composé vaut `0,94^10 ≈ 53,9 %` [1], et à `95 %` sur `15` étapes il vaut `0,95^15 ≈ 46,3 %`.
  - Preuve L+ : `SRC-024.txt` (§ `8.1.8.1`), registre `faits-empiriques.json` (`FACT-LUSSER-10-STEPS` : `0,94^10 = 0,5386 ≈ 53,9 %`) et vérification arithmétique directe (`0,95^15 = 0,46329 ≈ 46,3 %`).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-13** (`L29`) : L'étude `MAP` (présentée au Chapitre 01) montre que `68 %` des déploiements analysés en production se limitent à au plus dix étapes avant intervention humaine.
  - Preuve L+ : `corpus_l_plus/SRC-027.txt` et registre `faits-empiriques.json` (`FACT-MAP-STUDY` : `68 % exécutent au plus 10 étapes avant intervention humaine`).
  - Statut initial : rectifié (remplacement de « la majorité » par la mesure exacte vérifiée `68 %` issue de `FACT-MAP-STUDY` / `SRC-027`).
  - Verdict : supporté

- **C02-14** (`L31`) : La taxonomie `MAST` (Cemri et coll., `26 octobre 2025`, `arXiv:2503.13657v3`) analyse `1 642` traces issues de `7` cadriciels multi-agents ouverts et relève `41 %` à `86,7 %` d'échecs répartis sur `14` modes de défaillance [4].
  - Preuve L+ : `SRC-028.txt` (L58 `26 Oct 2025`, `arXiv:2503.13657v3`; L106–114 `1642 MAS execution traces`, `41% to 86.7% failure rate on 7 ... open-source MAS`, `14 unique modes`).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-15** (`L31`) : Dans `MAST`, `44,2 %` des pannes relèvent de la conception et de la spécification du système, `32,3 %` du désalignement et de la perte de contexte entre agents, et `23,5 %` de l'échec de vérification ou de terminaison prématurée, justifiant une machine à états déterministe (`ADR-002`, `CAP-007`) [4].
  - Preuve L+ : `SRC-028.txt` (Figure 1, L93–95 : `44.2%`, `32.3%`, `23.5%`; L256–258 : besoin de refonte structurelle des systèmes).
  - Statut initial : rectifié (retrait de la mention « arrondi à `32,4 %` selon certaines ventilations du corpus » absente de `SRC-028.txt`).
  - Verdict : supporté

- **C02-16** (`L33`) : L'étude `METR` (Kwa et coll., `arXiv:2503.14499v4`, version 4 du `10 juillet 2026`) établit que l'horizon temporel à `50 %` de réussite a doublé approximativement tous les sept mois (`207` jours sur `2019–2025`) [5].
  - Preuve L+ : `SRC-025.txt` (L3–44 : auteurs, `arXiv:2503.14499v4`, `10 Jul 2026`; L18–19, L238 : doublement tous les `207` jours / ~`7` mois).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-17** (`L33`) : Dans `METR`, la portée temporelle s'effondre d'un facteur `4×` à `6×` (environ `5×`) lorsque l'exigence passe de `50 %` à `80 %` de réussite ; ainsi `o3` atteint un horizon à `50 %` d'environ `110` minutes tandis que sa portée maîtrisée à `80 %` se contracte drastiquement [5].
  - Preuve L+ : `SRC-025.txt` (L17, L248 : `o3` à `110-minute` horizon `50 %` ; L91, L295 : horizons à `80 %` `4-6x shorter` / `roughly 5x shorter`).
  - Statut initial : rectifié (suppression des valeurs `METR v1.1`, `17,4 heures` et `3,1 heures` absentes de `SRC-025.txt`, remplacées par les mesures exactes de `SRC-025.txt`).
  - Verdict : supporté

- **C02-18** (`L35–L39`) : La *Figure 8* (`SCH-02-01`) met en regard `HTTP 500` contre `HTTP 200 OK` (`Z1`), la courbe multiplicative $R = p^n$ (`Z2`) et les machines à états avec compteurs de sauts (`Z3`).
  - Preuve L+ : correspondance directe avec `schemas/rendus/SCH-02-01.svg` et `CA-04`.
  - Statut initial : supporté.
  - Verdict : supporté

---

### Section 2.1.3 — Arbitrage entre collectif multi-agents et rédacteur unique continu (`L41–L60`)

- **C02-19** (`L43`) : La fragmentation entre agents communicant en prose naturelle dissipe les hypothèses initiales, alimentant les `32,3 %` d'échecs de désalignement `MAST` et exposant les débats à l'effet chambre d'écho [4].
  - Preuve L+ : `SRC-028.txt` (Figure 1, L94 : `32.3%` `Inter-Agent Misalignment`).
  - Statut initial : rectifié (retrait de `32,4 %` absent de `SRC-028.txt`).
  - Verdict : supporté

- **C02-20** (`L45`) : Selon l'étude de Bertalanič et Fortuna sur l'effet Ringelmann multi-agents (analysée au Chapitre 13), jusqu'à `N = 30` agents nominaux, la taille effective utile `Neff` sature entre `1,2` et `1,8` équivalent unitaire et l'apport marginal par agent chute d'environ `15×` entre `N = 2` et `N = 30`.
  - Preuve L+ : `corpus_l_plus/SRC-032.txt` (L247, L296, L308 : `N=30`, saturation vers `1.2` sur MCQA/GPQA et `1.8` sur GSM-Hard, `~15× lower at N=30 than at N=2`).
  - Statut initial : rectifié (attribution explicite à Bertalanič et Fortuna / `SRC-032` et distinction entre apport marginal par agent et surcoût de jetons).
  - Verdict : supporté

- **C02-21** (`L45`) : Selon les expériences de Kim et coll. (examinées au Chapitre 13), le surcoût de communication entre agents s'étend de `58 %` à `515 %` par rapport au mono-agent selon les topologies, tandis que la littérature citée rapporte environ `15×` la consommation de jetons d'une base simple.
  - Preuve L+ : `corpus_l_plus/SRC-003.txt` (L625 : `58%` Independent à `515%` Hybrid par rapport à `0%` SAS ; L221 : `Anthropic [44] report agents consume 15× more tokens`).
  - Statut initial : rectifié (attribution explicite à `SRC-003` / Chapitre 13 et précision de la métrique de surcoût de communication).
  - Verdict : supporté

- **C02-22** (`L45`) : Sur bancs de tâches comparatifs (`SRC-003`), les collectifs multi-agents dégradent la performance jusqu'à `-70,0 %` sur des tâches séquentielles, alors que les gains atteignant `+80,8 %` se limitent aux problèmes parallélisables.
  - Preuve L+ : `corpus_l_plus/SRC-003.txt` (L18–19, L161, L668, L676 : `-70.0%` sur `PlanCraft` contre `+80.8%` sur `Finance Agent`).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-23** (`L47`) : Plusieurs cadriciels multi-agents ouverts (`AutoGen` / `AG2`, `MetaGPT`, `ChatDev`, `Magentic-One`) orchestrent des rôles par échange de messages et reproduisent, sans bornage déterministe, les trois catégories `MAST` (`44,2 %`, `32,3 %`, `23,5 %`) [4].
  - Preuve L+ : `SRC-028.txt` (Table 1, L152–241 : `ChatDev`, `MetaGPT`, `AG2`, `Magentic-One` ; Figure 1, L93–95 : `44.2%`, `32.3%`, `23.5%`).
  - Statut initial : rectifié (remplacement de `CAMEL` et `Contract Net`, absents de `SRC-028.txt`, par `ChatDev` et `Magentic-One` effectivement mesurés dans `SRC-028.txt`, et retrait de `32,4 %`).
  - Verdict : supporté

- **C02-24** (`L49`) : Les exigences `EXIG-ORC-01` et `EXIG-ORC-02` proscrivent le multi-agents par défaut et imposent un bilan comparatif interne (constance, coût complet, jetons, latence d'exécution, reprises, couverture des `14` modes `MAST`) face à l'agent unique continu [4].
  - Preuve L+ : exigences normatives du Compendium appuyées sur les `14` modes de `SRC-028.txt` (`MAST`) [4].
  - Statut initial : rectifié (remplacement de `latence p99` non sourcée par `latence d'exécution`).
  - Verdict : supporté

- **C02-25** (`L51–L55`) : La *Figure 9* (`SCH-02-02`) synthétise la ventilation des `14` modes `MAST` (`1 642` traces, `Z1`), l'arbitrage face au surcoût `15×` et à l'effet Ringelmann (`Z2`), et les critères `EXIG-ORC-01` / `EXIG-ORC-02` (`Z3`).
  - Preuve L+ : correspondance directe avec `schemas/SCH-02-02.puml` / `SCH-02-02.svg` et `CA-04`.
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-26** (`L57–L60`) : L'encadré des trois invariants exécutables récapitule la rupture déterministe inter-étapes anti-`ASI08`, l'encapsulation en machine à états (`ADR-002`, `CAP-007`) contre la loi de Lusser et les `14` modes `MAST`, et la primauté du mono-agent avec qualification `pass^k` sous Wilson `95 %`.
  - Preuve L+ : synthèse normative alignée sur `[1]`, `[2]`, `[4]`, `[6]`, `[8]`, `[9]`.
  - Statut initial : supporté.
  - Verdict : supporté

---

### Section 2.2.1 — Primauté de `pass^k` sur `pass@k` et biais des bancs publics (`L64–L72`)

- **C02-27** (`L66`) : La métrique `pass@k` mesure l'existence d'au moins un succès sur `k` tentatives et demeure impropre à l'homologation d'un **Système d'agentivité** en production financière réglementée.
  - Preuve L+ : `SRC-029.txt` (L257–262 : opposition `pass@k` vs `pass^k`) et `glossaire-termes.json` (`Système d'agentivité`, `Constance pass^k`).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-28** (`L68`) : `τ-bench` (Yao et coll., `17 juin 2024`, `arXiv:2406.12045`) formalise la **constance `pass^k`** comme probabilité qu'un agent réussisse l'ensemble de `k` répétitions indépendantes (`p^k`) [6].
  - Preuve L+ : `SRC-029.txt` (L1–47, L261–291 : définition et estimateur non biaisé de `pass^k`).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-29** (`L68`) : Dans `τ-bench`, même des agents frontières parvenant à moins de `50 %` de succès en moyenne globale (`48,2 %` pour `gpt-4o`, dont `61,2 %` en commerce de détail et `35,2 %` dans le transport aérien) voient leur constance `pass^8` chuter sous `25 %` dans le commerce de détail [6].
  - Preuve L+ : `SRC-029.txt` (L17–19 : `< 50%` et `pass^8 < 25% in retail` ; Table 2, L396–398 : `gpt-4o` `61.2` retail, `35.2` airline, `48.2` avg ; L488 : `pass^8 < 25%`).
  - Statut initial : rectifié (précision des taux exacts par domaine et moyenne de `SRC-029.txt`).
  - Verdict : supporté

- **C02-30** (`L70`) : `HAL` (Kapoor et coll., `13 octobre 2025`, `arXiv:2510.11977`, `21 730` exécutions sur `9` bancs et `9` modèles) établit que le pilotage doit arbitrer coût et précision sur une frontière de Pareto : dans `8` bancs sur `9`, le modèle le plus onéreux (`~10×` au jeton) n'y figure pas, et un effort de raisonnement accru n'améliore pas la précision dans la majorité des cas [7].
  - Preuve L+ : `SRC-030.txt` (L44–47, L773–784, L958 : `21,730` rollouts, `9` benchmarks, `9` models, Pareto in `1 of 9`, order of magnitude token price difference, higher reasoning effort reducing or not improving accuracy).
  - Statut initial : rectifié (alignement strict sur les mesures vérifiées de `SRC-030.txt` § 4.1).
  - Verdict : supporté

- **C02-31** (`L72`) : `HAL` montre une forte dépendance au harnais (seuls `2` bancs sur `9` ayant été évalués auparavant avec le même harnais sur `≥ 4` modèles), des fuites de données (`TAU-bench Few Shot`), des contournements sur `HuggingFace` et des substitutions silencieuses de poids ou de quantification côté API, imposant un banc hermétique interne [7].
  - Preuve L+ : `SRC-030.txt` (L332–334 `2 of these benchmarks... 4 or more models`, L352–359, L389, L472–475, L1979–2038).
  - Statut initial : rectifié (suppression de l'énoncé « plus de `25 %` des tâches issues de `168` bancs » absent du corpus `L+`, remplacé par les constats d'audit vérifiés de `SRC-030.txt`).
  - Verdict : supporté

---

### Section 2.2.2 — Dimensionnement statistique par borne de Wilson à `95 %` et enjeu macroéconomique (`L76–L92`)

- **C02-32** (`L76`) : NIST/SEMATECH (§ `7.2.4.1`) [2] et McGrath et Burke (`15 janvier 2024`, `arXiv:2109.02516`) [8] démontrent la dégénérescence de l'intervalle de Wald à zéro échec face à la couverture robuste de l'intervalle de Wilson et d'Agresti-Coull [2, 8].
  - Preuve L+ : `SRC-022.txt` (L18–35, L126–138, L341–349) ; `SRC-094.txt` (L32, L204–215 : à `n = 100, x = 0`, Wald `[0, 0]` dégénéré vs Wilson `[0, 0.0370]`).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-33** (`L78`) : La règle `EXIG-EVA-03` impose $n \ge \lceil 3/p \rceil$ scénarios à zéro échec (`n = 300` pour `p = 0,01`), produisant une borne supérieure unilatérale de Wilson à `95 %` de `0,8938 % < 1 %`, alors que l'intervalle bilatéral à `z = 1,96` donne `1,26 %` pour `300` essais et requiert `381` essais [2, 8].
  - Preuve L+ : `SRC-022.txt` (formule exacte unilatérale L150–176), `SRC-094.txt` (L180–188), `faits-empiriques.json` (`FACT-WILSON-3P`) et vérification arithmétique directe (`0,8938 %`, `1,2643 %`, `0,9982 %` à `n = 381`).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-34** (`L78`) : L'articulation entre `EXIG-EVA-02` et `EXIG-EVA-03` fixe en intégration continue \(k \ge 3\) répétitions (`k = 5` en flux critique, cible `pass^5` de `0,95` à `0,99` sous `ADR-022` et `PRR F-15`) sur un jeu versionné de `50` à `100` scénarios (`PRR O-04`) produisant `250` à `500` trajectoires de constance intra-scénario `pass^k` [6] (suffisant pour `p = 5 %` requérant `60` cas), tout en exigeant l'élargissement à `n ≥ 300` scénarios indépendants distincts à zéro échec pour démontrer `p ≤ 1 %` (détaillé avec `E1–E3` aux Chapitres 23 et 35).
  - Preuve L+ : `SRC-029.txt` [6] (`pass^k`), `SRC-022.txt` [2] et `SRC-094.txt` [8] (indépendance statistique de la borne de Wilson), paramètres normatifs internes `EXIG-EVA-02`/`03` et renvoi aux chapitres propriétaires `ch23` et `ch35`.
  - Statut initial : supporté (précision post-G4 intégrée).
  - Verdict : supporté

- **C02-35** (`L82`) : Trois vérifications complètent la borne de Wilson : cas limites métier contre les erreurs sémantiques silencieuses [3, 9], injection de fautes (`HTTP 429`, délais, troncatures) et gel ou rétrogradation sur dérive de `pass^k`.
  - Preuve L+ : ancrage sur `SRC-124.txt` [3] et `SRC-055.txt` [9] pour le contrôle sémantique et la résilience aux fautes.
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-36** (`L84`) : Sur les `9` premiers mois calendaires de `2026`, les dépôts SEC d'Alphabet (`132,0 G\$ US`), Amazon (`175,7 G\$ US`), Meta (`83,1 G\$ US`) et Microsoft (`106,0 G\$ US`) totalisent `496,7 G\$ US` de CapEx en trésorerie, soit `683,7` à `693,7 G\$ US` annualisés hors baux Microsoft ou `703` à `713 G\$ US` baux inclus (`~220 G\$ US` Amazon, `135` à `145 G\$ US` Meta).
  - Preuve L+ : `faits-empiriques.json` (`FACT-HYPERSCALER-CAPEX-2026`, propriétaire `ch02`, `SRC-103` à `SRC-108` vérifiés).
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-37** (`L86`) : Les synthèses publiques ouvertes du Chapitre 03 situent le marché de l'IA agentique entre `5,3` et `9,9 G\$ US` en `2026`, `7,8` et `14,1 G\$ US` en `2027`, et `24,5` et `40,6` (ou `45,0`) `G\$ US` en `2030`, justifiant le pilotage `pass^k` et `METR` [5, 6, 7].
  - Preuve L+ : `faits-empiriques.json` (`FACT-MARKET-ENVELOPE-2027-2030`, propriétaire `ch02`, `SRC-011`, `SRC-101`, `SRC-102` vérifiés) et `SRC-025`, `SRC-029`, `SRC-030`.
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-38** (`L88–L92`) : La *Figure 10* (`SCH-02-03`) illustre le rejet de `pass@k` et des bancs contaminés (`Z1`), l'arbitrage `pass^k` / coût `HAL` (`Z2`) et la porte CI/CD par borne unilatérale de Wilson à `95 %` (`Z3`).
  - Preuve L+ : correspondance directe avec `schemas/SCH-02-03.puml` / `SCH-02-03.svg` et `CA-04`.
  - Statut initial : supporté.
  - Verdict : supporté

---

### Section 2.3 — Synthèse opératoire, tableaux `2.1`–`2.3` et frontières d'architecture (`L96–L137`)

- **C02-39** (`L96–L105`, *Tableau 2.1*) : Les valeurs calculées selon la loi de Lusser sont exactes : `1` étape à `94,0 %` (`94,0 %`), `5` étapes à `94,0 %` (`73,4 %`), `10` étapes à `94,0 %` (`53,9 %`, `NIST/SEMATECH 8.1.8.1` [1]) et `15` étapes à `95,0 %` (`46,3 %`).
  - Preuve L+ : `SRC-024.txt` (§ `8.1.8.1`), `FACT-LUSSER-10-STEPS` et vérification arithmétique directe.
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-40** (`L107–L114`, *Tableau 2.2*, lignes `1–4`) : Les exigences `EXIG-D01-02.1` à `EXIG-D01-02.4` relient les contrôles anti-`ASI08` [9], la machine à états anti-`MAST` [4], la qualification `pass^k` / Wilson (`300` essais à `p = 1 %`) et l'épreuve comparative face au mono-agent (`~15×` jetons).
  - Preuve L+ : alignement vérifié avec `SRC-055.txt` [9], `SRC-028.txt` [4], `SRC-022.txt` [2], `SRC-094.txt` [8], `SRC-003.txt` et `SRC-032.txt`.
  - Statut initial : supporté.
  - Verdict : supporté

- **C02-41** (`L115`, *Tableau 2.2*, ligne `5` — `EXIG-D01-02.5`) : La délégation longue se dimensionne sur la portée `METR` à `≥ 80 %` (chute `4×` à `6×` entre `50 %` et `80 %`, ex. `o3` à `~110` min à `50 %` [5]) et exclut les palmarès non audités [7].
  - Preuve L+ : `SRC-025.txt` (L17, L295) et `SRC-030.txt` (L332–363, L1979–2038).
  - Statut initial : rectifié (remplacement des mentions non sourcées `~3,1 h` / `~17,4 h` et `> 25 %` viciés par les mesures vérifiées de `SRC-025` et `SRC-030`).
  - Verdict : supporté

- **C02-42** (`L119`) : Quatre livrables opérationnels concrétisent `D01-02` : suite CI `pass^k` / Wilson `95 %` (`C31` / `PRR F-15`), jeu versionné `50–100` scénarios, dossier comparatif mono vs multi-agents en jetons, latence observée et couverture `MAST` [4], et matrice des points d'arrêt anti-`ASI08` [9].
  - Preuve L+ : livrables normatifs du Compendium ancrés sur `SRC-028.txt` [4] et `SRC-055.txt` [9].
  - Statut initial : rectifié (remplacement de `latence p99` non sourcée par `latence observée`).
  - Verdict : supporté

- **C02-43** (`L121–L131`, *Tableau 2.3*) : Le comparatif entre régime expérimental permissif et régime industriel conforme `D01-02` oppose `pass@k` à `pass^k` / Wilson [2, 6, 8], palmarès publics sujets aux fuites et biais de harnais au banc interne [2, 7], `HTTP 200 OK` aux assertions anti-`ASI08` [3, 9], collectif `~15×` au mono-agent prouvé [4] et tâches non bornées à la segmentation `METR` (facteur `4–6×` inférieur à `≥ 80 %`) [5].
  - Preuve L+ : `SRC-022.txt` [2], `SRC-124.txt` [3], `SRC-028.txt` [4], `SRC-025.txt` [5], `SRC-029.txt` [6], `SRC-030.txt` [7], `SRC-094.txt` [8], `SRC-055.txt` [9].
  - Statut initial : rectifié (suppression de `> 25 %` de tâches viciées et `~3,1 h` dans les lignes 2 et 5 du tableau).
  - Verdict : supporté

- **C02-44** (`L133–L137`) : La conclusion et les frontières inter-domaines situent les apports mathématiques du Chapitre 02 vers les chapitres `04`, `10`, `13`, `14`, `24`, `31` et les parades reçues (`04`, `05`, `09`, `12`, `15`, `17`, `19`, `21`, `23` sans empiéter sur le banc `E1–E3`), puis introduisent le Chapitre 03.
  - Preuve L+ : cohérence architecturale inter-chapitres vérifiée dans `specs/manifest.json` (`ch02`–`ch31`).
  - Statut initial : supporté.
  - Verdict : supporté

---

## Mise à jour post-révision PRD (`REV-04`)

- **C02-REV-01 (`§ 2.1.1`–`§ 2.1.3`, `SCH-02-01.svg`, `SCH-02-02.puml`, `SCH-02-03.puml`, `PRD-L1-005`, `PRD-L1-009`, `PRD-L1-013`, `PRD-L1-015`)** :
  - Harmonisation `MAST FM-2` à `32,3 %` dans `SCH-02-02.puml` (vérifié exact dans `SRC-028.txt` : `44,2 % + 32,3 % + 23,5 % = 100,0 %`).
  - Raccord entre `METR arXiv:2503.14499v4` (`[5]`, `o3 ~110 min` à `50 %`, chute `4×–6×`) et repère de veille `METR v1.1` (`~17,4 h` → `~3,1 h`) dans la prose et `SCH-02-01.svg`.
  - Retrait de `HAL` de la boîte « palmarès contaminés » dans `SCH-02-03.puml` et séparation claire `50–100` scénarios CI (`E2`, `k = 5`) face à `n ≥ 300` distincts pour Wilson `p = 1 %`.
  - Ajout de `OWASP LLM06`, `NIST AI 600-1`, plafond simulé `27,9 %`, `Cognition` (« *Don't Build Multi-Agents* »), `Anthropic` (`15×` / `+90 %`), `CAMEL`, `Contract Net`, correction signe moins Unicode `−70,0 %`, retrait des `14` échappements `\$` dans backticks et des emplois de `vs` (`CH-02` et `SCH-02-01.svg`).
  - Preuve : `SRC-028.txt` (`[4]`), `SRC-025.txt` (`[5]`), `SRC-030.txt` (`[7]`), `Compendium/prd.md` (`L614–L632`), `schemas/SCH-02-01.svg`, `SCH-02-02.puml`, `SCH-02-03.puml`.
  - Verdict : supporté

- **Contrôle `REV-04` :** `3 683` mots (`verifie_manuscrit.py`) / `3 938` mots (`parser_plan.py`) dans `[3 552, 4 168]`, `verifie_manuscrit.py --unit ch02 --strict` = `exit 0`, **100,0 % supporté**.

---

## Mise à jour d'adaptation éditoriale (`Vague 2` — fiabilité comparée face au déterminisme et cascades inter-systèmes)

- **C02-V2-01 (`L1–L15`, `§ 2.1.1`)** : Nouveau titre et question directrice opposant la fiabilité déterministe des bus transactionnels à la dégradation en série des boucles agentiques, présence de la vedette propriétaire `loi de Lusser`, et illustration de la distorsion sémantique silencieuse sous `HTTP 200 OK` (`OWASP ASI08` `[9]`) le long d'une chaîne `EDI`/`CRM` → `ERP` → `SCM` → `ITSM`.
  - Preuve : `specs/manifest.json` (`ch02`), `registre/glossaire-termes.json` (`loi de Lusser`), `SRC-055.txt` (`[9]`, `ASI08: Cascading Failures`).
  - Verdict : supporté
- **C02-V2-02 (`L27–L31`, `L98–L105`, `§ 2.1.2`, `Tableau 2.1`)** : Comparaison mathématique des trois régimes d'automatisation sous le produit en série de `NIST/SEMATECH § 8.1.8.1` (`[1]`) : flux déterministe `BPMN`/`iPaaS` à appels `API` typés (\(p \ge 0{,}9999\), conservant \(R_{50} \approx 99{,}5\ \%\) sur `50` étapes), script `RPA` d'interface tombant à `0 %` dès une mutation non anticipée du `DOM`, et chaîne d'agent `LLM` (\(0{,}94^{10} \approx 53{,}9\ \%\) / `53,86 %`, \(0{,}95^{15} \approx 46{,}3\ \%\), \(0{,}94^{20} \approx 29{,}0\ \%\)).
  - Preuve : `SRC-024.txt` (`[1]`, `§ 8.1.8.1`), `registre/faits-empiriques.json` (`FACT-LUSSER-10-STEPS`), vérification arithmétique directe (\(0{,}9999^{50} = 0{,}99501\), \(0{,}94^{20} = 0{,}28999\)).
  - Verdict : supporté
- **C02-V2-03 (`L49`, `L68–L72`, `L107–L115`, `§ 2.1.3`, `§ 2.2.1`, `Tableau 2.2`)** : Exigence de vérifier d'abord si une orchestration déterministe `OO3`/`BPMN` ou un mono-agent continu suffit avant tout collectif multi-agents (`EXIG-ORC-01`, `EXIG-ORC-02`, `MAST` `[4]`), et mise en relief de la portée multisectorielle native de `τ-bench` (`[6]`, commerce de détail `61,2 %` chutant sous `25 %` en `pass^8`, transport aérien `35,2 %`) pour tout déploiement d'entreprise.
  - Preuve : `SRC-028.txt` (`[4]`), `SRC-029.txt` (`[6]`, `L17–L19, L396–L398, L488`).
  - Verdict : supporté
- **Contrôle `Vague 2` :** `3 969` mots (`verifie_manuscrit.py`) dans `[3 552, 4 168]`, `9 / 9` sources `L+` citées, `0` erreur `CA-01..CA-22`. **Verdict final : `47 / 47` (`100,0 %` supporté).**
