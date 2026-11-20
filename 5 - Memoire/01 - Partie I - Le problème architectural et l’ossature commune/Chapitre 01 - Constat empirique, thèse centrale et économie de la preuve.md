# Chapitre 1 — Constat empirique, thèse centrale et économie de la preuve

> **Ancrage corpus (état de référence : 17 novembre 2026) :** `[C26 ch. 1, 7, 35, 42, 43, 49, 50, Annexe B, Annexe N]` · `[CAD26 ch. 1, 2, 4 | PRIN-08, ch. 7 | EXIG-ORC-01, EXIG-ORC-02, ch. 8, 10 | EXIG-EVA-02, EXIG-EVA-03, EXIG-FIN-01, Annexe H]` · `[C27 § 0.2, § 0.5, ch. 1–4, 16, 17, 21, 34, 40, 42, 47, 48–50, Annexe E, Annexe F, Annexe G]` · `[PD28 M-1, M-2, M-6 à M-8 | PRI-001, PRI-002, CAP-007, CAP-043, CAP-045, SIG-001, SIG-013, SIG-017, ANC-045, ANC-046]`.

*Question directrice : Que sait-on réellement de la production agentique fin 2026, et comment bâtir une architecture durable sans céder aux effets d’annonce ni aux bancs d’essai saturés ?*

**Thèse du chapitre :** Fin 2026, aucune étude évaluée par les pairs ne documente les protocoles d’outils ou d’agents à grande échelle en production `[M]`. La majorité des déploiements exécutent au plus dix étapes sous supervision humaine `[M]`. De plus, les protocoles d’échange n’offrent aucun arrimage natif aux lois applicables `[N]`. Sur l’horizon 2026–2035, le contrôle déterministe et la capacité de preuve précèdent donc toute extension d’autonomie P : PRI-001 P : PRI-002 P : CAP-007 E : PRIN-08 E : EXIG-ORC-01 E : EXIG-ORC-02 .

## 1.1 Adoption mesurée fin 2026 et règle « soutien n’est pas production »

L’architecte d’entreprise (AE) et l’architecte de solutions (AS) séparent l’usage général de l’IA, le déploiement effectif d’agents et le discours fournisseur. Au deuxième trimestre de 2026, Statistique Canada mesure 19,2 % d’utilisateurs d’IA sur douze mois parmi les entreprises canadiennes. Ce taux atteint 27,8 % chez les organisations de 100 employés et plus, et 40,4 % en finance et assurances. À titre indicatif non directement comparable, Eurostat relève ~8 % dans les PME et 20,0 % dans l’Union européenne en 2025 (≥ 10 salariés ; `C27 ch. 4 § 4.1`, `ch. 50 § 50.4` ; `PD28 M-2 § 2.2`, `M-7 § 7.5`, `SIG-017`). Au troisième trimestre, les intentions atteignent 25,2 % (37,5 % dans les grandes entreprises). La Banque du Canada confirme toutefois la rareté des mises en production (`PD28 M-2 § 2.2`).

Aucun office statistique n’isole encore les agents fin 2026. Statistique Canada lancera TechStat dès 2027 A (`ANC-045`). La stratégie *« L’IA pour tous »* vise 60 % d’adoption IA d’ici 2034 A (`PD28 M-7 § 7.5`, `ANC-046`). Au Québec, le recensement de 432 initiatives d’IA dans les ministères et organismes des administrations publiques n’isole pas les agents. Il ne mesure aucun effet en service et ne s’extrapole pas aux institutions privées (`C27 ch. 42 § 42.1, § 42.5`).

Sur le terrain, l’étude `MAP` (*Measuring Agents in Production*, 20 cas et 306 réponses dont 86 systèmes déployés) montre des systèmes bornés. Ainsi, 68 % exécutent au plus dix étapes avant intervention humaine et 16 cas sur 20 (80 %) suivent des flux prédéfinis. Par ailleurs, 70 % emploient des modèles standards sans réentraînement et 74 % reposent sur l’évaluation humaine (`C27 ch. 4 § 4.2`, `ch. 42 § 42.1` ; `PD28 M-2 § 2.2`, `SIG-013`). Ni les 789 sources de `C27 ch. 1–47` ni la revue rapide du 13 novembre 2026 sur Consensus ne recensent d’étude arbitrée mesurant `MCP` ou `A2A` en production (`C27 ch. 42 § 42.6`, `ch. 48 § 48.1–48.3`). Cette revue couvre 10 requêtes et 123 notices, dont 83 retenues et lues sur résumé seulement (31 évaluées par les pairs, 52 prépublications). L’unique cas évalué par les pairs à grande échelle sur trafic réel (`Nubank`, `KDD 2026`) orchestre cinq agents ReAct simples sur graphes déterministes. Il progresse en libre-service mais reste inférieur aux experts

humains. Il exige aussi une réingénierie d’invites lors de la migration `GPT-4.1 → GPT-5` et n’utilise ni `MCP`, ni `A2A`, ni multiagent autonome (`C27 ch. 42 § 42.1–42.2`).

D’où la règle de `C26 ch. 7 § 7.6` et `ch. 35 § 35.0` : *« soutien » n’est pas « production »*. Les communiqués d’institutions canadiennes (`TD` `S-014, S-015`, `RBC` `S-016, S-017`, `Scotiabank` `S-018`, `Manuvie` `S-019`, `CIBC` `S-028`, `BMO` `S-045`, `Sun Life` `S-046`) documentent des intentions ou des volumes auto-déclarés. Il en va de même pour les rapports annuels 2025 (`Desjardins` `S-021`, `Intact` `S-029`) ou l’absence documentée (`Banque Nationale`, `C26 § 35.8.3, § 35.9`, `Annexe B`). Aucun de ces documents ne décrit une architecture d’exécution ni des métriques vérifiées de production.

## 1.2 Défaillances systémiques, loi de Lusser, bancs saturés et marché

Selon la loi de Lusser, sans validation déterministe intermédiaire, dix étapes consécutives fiables chacune à 94 % tombent à 𝑅= 0,9410 ≈53,9 % (`C27 § 0.2`, `ch. 17 § 17.8`, `ch. 21 § 21.1`). Sur 10 000 dépôts SEC, l’exactitude d’extraction plafonne à 0,758 par document (`C27 ch. 42 § 42.3`). La résolution autonome d’incidents TI plafonne entre 10 % et 25 % (`§ 42.4`). Selon Kim et coll., l’ajout d’agents varie de `-70 %` sur tâches séquentielles couplées à `+80,8 %` sur sous-tâches parallélisables (`C27 ch. 16 § 16.7`, `ch. 48 § 48.4`).

La taxonomie `MAST` (Cemri et al., 1 642 traces en `v3` sur sept cadriciels open source, 41 % à 86,7 % d’échecs) prouve que la défaillance est d’abord architecturale. Elle regroupe quatorze modes en trois familles (`C27 ch. 21 § 21.1–21.4` ; `CAD26 § 7.9` ; `PD28 M-6 § 6.2`). La spécification et la conception système comptent pour `44,2 %` en `v3` (`41,77 %` en `v2`). Le désalignement inter-agents pèse `32,4 %` en `v3` (`36,94 %` en `v2`), et la vérification/terminaison `23,5 %` (`21,30 %` en `v2`). L’audit de 168 bancs publics relève en outre des défauts critiques dans plus de 25 % des tâches (`C27 ch. 48 § 48.5`). Après saturation du seuil de 16 h, `METR` a gelé sa série le 8 septembre 2026. `METR Time Horizon v1.1 (Claude Mythos Preview)` atteint ~17,4 h à 50 % de réussite (IC : 8,5 à 55 h, génie logiciel/ML/cyber). Toutefois, cet horizon chute à ~3,1 h à 80 % de constance, soit un écart de 5 à 6 fois (`C27 ch. 49 § 49.2` ; `PD28 M-2 § 2.1.2`, `M-6 § 6.1–6.2`, `SIG-013`).

Les estimations de marché exigent le même tri (`C27 ch. 50 § 50.1–50.5` ; `PD28 M-7 § 7.1`). En 2025, un écart de 1 à 58 (1,5 à 88 G$ US) confond six périmètres emboîtés. Le recalibrage sur treize séries non indépendantes donne 8 à 17 G$ US en 2027 et 25 à 55 G$ US en 2030 (`C27 § 50.2`). Les agents pèsent 1,1 % des dépenses mondiales en IA et 21 % des organisations ont une gouvernance dédiée (`C27 § 50.4`). Au Canada, 30,0 % des grandes entreprises citent cybersécurité et confidentialité comme premier frein (`PD28 M-2 § 2.2`). Enfin, Gartner projette (communiqué du 26 mai 2026 sans méthode publiée) l’abandon ou la rétrogradation de 40 % des projets autonomes d’ici fin 2027 A (`CAD26 § 2.1, § 8.1` ; `C27 § 4.3`).

## 1.3 Thèse centrale, fractures du corpus et économie de la preuve

Ce mémoire condense (~21:1 en v1.2) un corpus fermé de 2 541 pages (complété par `Note AMF IA`, 49 p., 141 chapitres, 27 annexes). Il résorbe cinq fractures : volume et redondances, lacune `DIV-02`, prolifération des couches et échelles, asymétrie probatoire et coupure AE / AS.

| Volume | Mesure et gel | Statut | Apports majeurs | Limites héritées |
| --- | --- | --- | --- | --- |
| `C26` | 673 p., 50 ch., Ann. B, I, N (27 juill., reval. 29 oct., 1er nov. 2026) | Analytique | `LCIM` `[S]`, `Q-A..Q-E` `[S]`, 2e saut, `OO1–OO4` `[S]`, `0/15` `[S]`, `Z1–Z5` & `PC1–PC5` `[S]`, effets `ch. 48` | Constructions d’auteur à 0 entrée au socle (`ch. 41, 43, 47, 48` `[S]`) |
| `CAD26` | 351 p. (+ `Note AMF IA` 49 p.), 15 ch., Ann. A–H (28 oct. / 19 nov. 2026) | Normatif (`305 EXIG-*` v1.2) | `12 PRIN`, 6 couches `§ 5.2`, `ABB`/`SBB`, `CoALA`, 8 patrons, `N0–N4`, `JCS`/`CIBA`, `CaMeL`, `EXIG-AMF-01..12` | Textes HTTPS AMF bloqués (`statut F`) compensés par `Note AMF IA` ; horizon 2030 |
| `C27` | 1 117 p., 50 ch., Ann. A–H (14 / 19 nov. 2026) | Mixte (`59,6 %` / `34,9 %` [`34,87 %`]) | `1 033` sources, `COMP-3`, `OPC UA`, durable/Saga, double couloir `RP`, `CPO`, `31 ADR`, `75` PRR (`24` bloquants) | 31 volets à `0` source ; `255/473` lignes `[S]` (`53,9 %`) ; cas fictif *Groupe Boréal* exclu ; `16 ADR` généralisées |
| `PD28` | 400 p., `M-1..26`, Ann. A–H (16 / 19 nov. 2026) | Cible AE et `DAPP` | `67` ancres (`98` textes `L+`), `15 PRI`, `52 CAP` (`42` inv., `10` cond.), `12 DEC`, `24 PEX`, `43 INI`, `15 POR`, `27 SIG` | Lacune `DIV-02` close par concordances typées (`DC-P07`) ; zéro patron d’implémentation AS |

> **[Figure]**
> - Cartographie du corpus (2 541 p. + Note AMF IA) et fermeture DIV-02 Soudure vérifiée au 19 nov. 2026 des quatre volumes vers le mémoire AE / AS v2.0
> - C26 · Compendium 2026 (673 p.)
> - 50 ch. · Ann. B, I, N (1er nov. 2026)
> - • LCIM [S], Q-A..Q-E [S], 2e saut
> - • OO1–OO4 [S], PQC, ch. 48 [S]
> - • Matrice 0/15 & Z1–Z5 [S]
> - CAD26 · CRE-IA v1.2 (351 p. + AMF 49 p.)
> - 15 ch. · Ann. A–H + Note AMF IA
> - • 12 PRIN · 6 vraies couches § 5.2
> - • 305 EXIG-* (255+34+16, +12 AMF)
> - • 10 interdictions GOV-17 (46 ND)
> - C27 · Compendium 2027 (1 117 p.)
> - 50 ch. · Ann. A–H (1 033 sources)
> - • 31 ADR · 75 PRR (24 bloquants)
> - • COMP-3, Saga, CoALA, Double PII
> - • FinOps CPO & cas fictif exclu
> - PD28 · Plan directeur 28–35 (400 p.)
> - 26 ch. (M-1..M-26) · 98 textes L+
> - • 67 ancres · 15 PRI · 12 DEC
> - • 52 CAP (42 inv. + 10 cond.)
> - • 24 PEX · 43 INI · 15 POR · 27 SIG
> - Socle consolidé : 2 541 p. + Note AMF (49 p.) · 141 ch. · 27 annexes
> - 1. Fermeture DIV-02 (DC-P07)
> - • 52 CAP ↔ 305 EXIG-* v1.2
> - • 24 PEX (13 spéc. + 11 lacunes)
> - • 5 couches + 3 volets ↔ 6 CAD26
> - • Liens typés : directe / ext. / lacune
> - 2. Économie de la preuve
> - • [N] Droit L+ · [M] Études revues
> - • [É] Specs tech. · [S] Construits
> - • [D] adopté · [A] annoncé · [C]
> - • Cas fictif exclu · statut F borné
> - Mémoire AE / AS v2.0 — 115–125 p. (Ch. 1–12 & Annexes A–F)
> - Architecte d’entreprise (AE)
> - • 52 CAP, noyau possédé, 5 profils
> - • 15 POR, 27 SIG, 3 lignes & APP
> - Architecte de solutions (AS)
> - • PEP 9 contrôles, CoALA, Saga OO3
> - • JCS/CIBA, SPIFFE/PQC, double PII

*Fig. 1. – Cartographie des 2 541 pages du corpus (+ Note AMF IA), hiérarchie de la preuve et fermeture structurelle de la lacune DIV-02.*

Sur l’horizon 2026–2035, les protocoles ouverts (`MCP`, `A2A`) règlent l’échange syntaxique (`Q-A` : *qui parle* `[S]`). À l’inverse, le droit exige l’imputabilité et la preuve d’instance (`Q-E` : *qui en répond* `[S]`). Or `C26 ch. 42` constate `0/15` lien natif `[S]` entre protocoles et exigences financières selon trois vides (`§ 42.3.1`). Le *vide de socle* initial sur l’AMF a été documenté le 31 octobre 2026 en `Annexe N.3`, sans lien protocolaire. Le *vide de texte* porte sur la norme bancaire ouverte (*Loi sur les services bancaires axés sur les consommateurs*, `LSAC`). Enfin, le *vide de protocole* subsiste face à `BSIF E-23`, à l’article 12.1 de la Loi 25 et à `ACVM 11-348`.

Quatre régimes de preuve gouvernent le mémoire. Le niveau `[N]` couvre les textes `L+` lus (`98` en `PD28 Annexe H`) et le socle `CAD26` v1.2 de `305 EXIG-*` (`255 DOIT`, `34 NE DOIT PAS`, `16 DEVRAIT`, intégrant les `12 EXIG-AMF`). Le niveau `[M]` désigne les mesures évaluées par les pairs, `[É]` les spécifications techniques ou prépublications, et `[S]` les constructions d’auteur co-appuyées (`C26` et les 31 volets de `C27`). Le cas fictif *Groupe Boréal Inc.* (`C27 § 0.5`) est exclu comme sans valeur probante. Toute cible sans source primaire (`< 10 s` `[S]`, `< 15 min` `[S]`, `≤ 15` outils `[S]`, `72 h` `[S]`, `≥ 85 %` `[S]`, `30 j` `[S]`, `pass^5 ≥ 99 %` `[S]`) porte obligatoirement `[S]`.

## 1.4 Sobriété agentique, hypothèses H1–H6 et parcours adaptatifs DAPP

L’AE et l’AS appliquent l’arbre de sobriété (`C26 § 43.2.3`, statut « C » hors socle, `[S]` ; `C27 Annexe F.3` `[S]`) P : PRI-001 P : PRI-002 E : PRIN-08 E : EXIG-ORC-01 E : EXIG-ORC-02 . Ils privilégient d’abord la règle déterministe (`N0`), puis le flux déterministe à étapes cognitives bornées. Ils n’ouvrent l’agent unique outillé (patron 8) qu’en cas d’entrées non structurées. Enfin, le multiagent homologué (`≤ 2` sauts) exige un gain mesuré (`pass^k`) et un avantage en coût complet par résultat conforme (`CPO`) face au repère non agentique P : CAP-043 P : CAP-045 E : EXIG-EVA-02 E : EXIG-FIN-01 .

Les hypothèses `H1–H6` (`C27 § 4.5` réévaluées en `PD28 M-2 § 2.2`) confortent ce cadre avant `BSIF E-23` au 1er mai 2027 D . Les hypothèses `H1` (grandes entreprises), `H2` (agents bornés supervisés) et `H3` (primauté de l’architecture) sont confirmées. Il en va de même pour `H4` (`MCP`/`A2A` acquis sur le fil ; `WIMSE`, `DAWN` et `OpenTelemetry` en chantier). Par ailleurs, `H5` (plans de contrôle multiples) se renforce et `H6` (tri valeur/risque) est en cours.

Au-delà de 2030, la méthode `DAPP` (Haasnoot et al., `PD28 M-1 § 1.4`, `M-8`) gouverne l’incertitude jusqu’en 2035 sans probabilité chiffrée. Elle mobilise `27` signaux (`SIG-001..017`, `SIG-101..110`) et `15` portes (`POR-001..009`, `POR-011..016`) sur trois scénarios C : A, B, C ; SIG-001, SIG-013 . Le **Scénario A (*Socle étendu*)** mise sur une convergence ouverte. Le **Scénario B (*Archipel*)** décrit des silos propriétaires fermés sur le contrôle. Le **Scénario C (*Blocs*)** suppose une fragmentation exigeant la souveraineté stricte des substrats et des clés jusqu’en 2035 C : C ; SIG-002, SIG-016 .

Contrat opérationnel croisé — Architecte d’entreprise (AE) | Architecte de solutions (AS)

Décisions AE

1. Imposer la sobriété (« le contrôle précède l’autonomie ») P : PRI-001 P : PRI-002 E : PRIN-08 E : EXIG-ORC-01 et refuser tout financement agentique là où `N0` suffit.
2. Exiger `[N]/[M]/[É]/[S]` dans chaque dossier : écarter les prévisions de marché au profit du seul `CPO` P : CAP-045 E : EXIG-FIN-01 .
3. Piloter selon `DAPP` sur `A`, `B` et `C` sans probabilité, en finançant d’abord les 42 capacités invariantes sans regret.

Spécifications AS

1. Appliquer l’arbre (`C27 Annexe F.3` `[S]`) E : EXIG-ORC-01 E : EXIG-ORC-02 : code/*Decision Model and Notation* (`DMN`, `N0`) → flux déterministe → agent unique → multiagent sur gain `pass^k` P : CAP-043 .
2. Contrer Lusser (0,9410 ≈53,9 %) et les 14 modes `MAST` par schémas JSON, invariants hors modèle et points de contrôle persistés P : CAP-007 .
3. Qualifier chaque agent sur un banc interne versionné de `≥ 50` scénarios incluant cas limites et injections E : EXIG-EVA-02 (`≥ 100` `[S]` dans `C27 PRR O-04`).

## 1.5 Grille de décision

| Décision | Option par défaut | Quand s’en écarter | Preuve |
| --- | --- | --- | --- |
| Agent autonome vs flux programmé | Automatisation déterministe ou flux codé à étapes bornées (`N0` / patron 1) | Entrées non structurées rendant le codage exhaustif impraticable, sous enveloppe déterministe E : EXIG-ORC-01 | `[M]` `MAP` (`68 %` `≤ 10` étapes, `16/20` flux fixes) ; `CAD26` `PRIN-08` |
| Agent unique outillé vs multiagent | Agent unique doté d’outils d’intention métier et de contexte compilé (patron 8) | Gain net mesuré sur banc interne ou séparation stricte de domaines de sécurité E : EXIG-ORC-02 | `[M]` `MAST` (`1 642` traces) ; `C27` § 16.7 (`-70 %` à `+80,8 %`), § 48.4 |
| Qualification avant mise en production | Simulation isolée (`≥ 3` essais E : EXIG-EVA-03 ) mesurant la constance `pass^k` (`0,95` à `0,99` `[S]` selon criticité, `C27 ADR-022` / `PRR F-15`) | Tâche consultative sans écriture (`Classe 1` / `N1`), soumise aux tests d’ancrage documentaire | `[M]` `[S]` `C27` § 48.5 (`> 25 %` bancs viciés), § 49.2 (`METR`) ; `CAD26` `EXIG-EVA-03` |
| Justification économique d’un projet | Coût complet par résultat conforme non rouvert (`CPO`) comparé à la base non agentique E : EXIG-FIN-01 | Jamais en production ; les prévisions macroéconomiques ne fondent aucun dossier d’affaires | `[É]` `C27` § 40.5, § 50.2 (`13` séries non indépendantes) ; `PD28` `CAP-045` |
| Appui d’une prescription architecturale | Exigence normative (`CAD26`), texte primaire `L+` ou mesure évaluée par les pairs | Patron issu d’un volet `C27` ou d’un cadre `C26`, uniquement étiqueté `[S]` et co-appuyé | `[S]` `PD28` M-1 § 1.3 ; `C26` Annexe B ; `C27` Annexe E.1 |
| Planification pluriannuelle (2027–2035) | Parcours adaptatifs `DAPP` sans probabilité (`A`, `B`, `C`) gouvernés par signaux `SIG-*` | Échéances adoptées à date ferme D , exécutées par rétroplanning calendaire strict | `[M]` Haasnoot et al. (`DAPP`, `PD28` M-1 § 1.4, M-8 § 8.1) |

## 1.6 Limites et renvois

Les PDF primaires de l’AMF bloqués en HTTPS (`T-01`, `T-02`, `T-13..15`), les codifications LégisQuébec et les lots non déposés `P1-B2` à `P1-B4` et `P3-L2` restent au `statut F`. Ils ne fondent aucune obligation `[N]` nouvelle. Toutefois, `2026/documents/Note AMF IA.pdf` (`CRE-IA-2026-01-QC`, 41 attentes et `12 EXIG-AMF`, recoupée avec `C26 Annexe N.3`) est intégrée au socle `CAD26` v1.2 (`305 EXIG-*`). En outre, `C27` et `PD28` n’ont pas subi de relecture humaine intégrale. Les dissonances internes des volets — telle `ADR-009` adoptant `Apache Ossie` `0.1.1` en incubation sans moteur (`C27` p. 250 face à l’Extrait 12.1 p. 240 en `"1.0.0"`) — sont neutralisées (Annexe B). Renvois : `C26 ch. 1, 7, 35, 42, 43, 49, 50, Ann. B, N` ; `CAD26 ch. 1, 2, 4, 7, 8, 10, Ann. H` ; `C27 § 0.2, 0.5, ch. 1–4, 16, 17, 21, 34, 40, 42, 47, 48–50, Ann. E, F, G` ; `PD28 M-1, M-2, M-6 à M-8` ; Annexes A à F.
