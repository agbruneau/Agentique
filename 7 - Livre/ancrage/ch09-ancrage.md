# Audit Wyvern — Chapitre 09 : Observer, prouver et compter

## En-tête de verdict (Barrière G2 — ancrage atomique et passe différentielle post-G4 Tour 1)

Verdict final — supportés : 55 (100 %)
Verdict final — imprécis résiduels : 0
Verdict final — non supportés résiduels : 0

- **Périmètre vérifié** : [Chapitre 09 - Observer, prouver et compter.md](file:///c:/Github/Agentique/7%20-%20Livre%202027/manuscrit/03%20-%20Partie%20III/Chapitre%2009%20-%20Observer%2C%20prouver%20et%20compter.md) (lignes 1 à 138), contre [ch09-sources.md](file:///c:/Github/Agentique/7%20-%20Livre%202027/sources/ch09-sources.md) (`[1]` à `[22]`, dont `[22]` `SRC-077` `RFC 8785 JCS`), les fichiers `.txt` correspondants de `7 - Livre 2027/recherche/corpus_l_plus/`, ainsi que [ancres-chronologiques.json](file:///c:/Github/Agentique/7%20-%20Livre%202027/registre/ancres-chronologiques.json), [faits-empiriques.json](file:///c:/Github/Agentique/7%20-%20Livre%202027/registre/faits-empiriques.json) et [glossaire-termes.json](file:///c:/Github/Agentique/7%20-%20Livre%202027/registre/glossaire-termes.json).
- **Date de gel des faits** : `2 décembre 2026` | **Volume final (`v1.3`)** : `5 518` mots `G1` (`5 716` `split()`, `144` lignes, cible `[5 152, 6 048]`)
- **Bilan quantifié consolidé** :
  - **Passe G2 initiale** (lignes 1–132 d'origine) : **52** affirmations atomiques actives vérifiées (`100 %` `supporté` après 18 rectifications et levée d'une collision `CA-03` de 12-gramme).
  - **Passe différentielle G2 post-bâtisseur G4 Tour 1** (diff sur lignes `17, 29, 31, 33, 35, 43–71, 75, 81–83, 87, 89, 95, 97–101, 120, 128–130` dans le manuscrit réindexé à `138` lignes (`v1.3`)) : **55** items atomiques différentiels audités directement contre les `.txt` de `corpus_l_plus/` ; **10** rectifications chirurgicales appliquées aux lignes `41, 45, 49, 50, 51, 55, 57, 62, 63, 93` pour alignement strict mot pour mot sur les sources primaires `L+` ; **0** résidu non supporté, **0** matrice interdite (`CA-02`), **0** recopie `>= 12` mots (`CA-03`), **1** seul tableau conservé (`CA-05`), balise `AO-07` respectée en ouverture (ligne 5), `$` échappés (`\$`) et formules en `\(...\)` / `\[...\]` (`CA-06`).

---

## Passe différentielle G2 — Audit post-bâtisseur G4 Tour 1 (55 items audités)

### A. Nettoyages et précisions de la section 9.1 (lignes 17, 29, 31, 33, 35 — 14 items)

1. **Ligne 17 (`Loi 25` `[21]`, `EU AI Act` `[11]`, `DORA` `[12]`, `Bostan` `[10]`)** — `5` items :
   - Art. 23 modifié par la `Loi 25` (`LQ 2021, c. 25`, art. 119) : destruction ou anonymisation irréversible à des fins sérieuses et légitimes selon critères réglementaires (`corpus_l_plus/SRC-063.txt`, L1766–1788). **Verdict final : supporté**
   - Plafonds `SAP` `10 000 000 \$ CA` / `2 %` (art. 90.12) et amendes pénales `25 000 000 \$ CA` / `4 %` (art. 91) sans guillemets inversés (`SRC-063.txt`, L2283–2333). **Verdict final : supporté**
   - Article 12.1 de la `Loi 25` (renvoi chapitre 10) (`SRC-063.txt`, L1542–1555). **Verdict final : supporté**
   - `EU AI Act` art. 12 et art. 19 (tenue et conservation par les fournisseurs pendant au moins 6 mois, ou plus selon le droit financier, en conciliation avec la protection des données) (`SRC-060.txt`, L3777–4048). **Verdict final : supporté**
   - `DORA` art. 17 (`SRC-062.txt`, L2228–2237) et revue systématique PRISMA 2020 de 66 études par Ionel Bostan (`SRC-059.txt`, L16, L60, L70, L141–163). **Verdict final : supporté**
2. **Ligne 29 (`OpenTelemetry GenAI` `[5]`, `BSIF` `[14]`, `DORA` `[12]`)** — `2` items :
   - Intervalles normalisés (`create_agent`, `invoke_agent`, `invoke_workflow`, `plan` et l'intervalle connexe `execute_tool`) et attributs à faible cardinalité incluant jetons facturés cache/raisonnement (`SRC-037.txt`, L7, L45–L64, L640–L668). **Verdict final : supporté**
   - Classement `Opt-In` de `gen_ai.system_instructions`, définitions d'outils, `gen_ai.input.messages`, `gen_ai.output.messages`, `*_ref`, et avertissement de sensibilité incluant `exception.message` (`SRC-037.txt`, L252–259, L361–466, L530–532). **Verdict final : supporté**
3. **Ligne 31 (`RFC 8785` `JCS`, `[22]` `SRC-077.txt` ; `EU AI Act` `[11]`)** — `2` items :
   - Canonisation `RFC 8785` (ordre lexicographique des clés, suppression des blancs superflus, sérialisation déterministe des nombres et chaînes) (`SRC-077.txt`, L212–L214, L302–L339). **Verdict final : supporté**
   - Précision de portée explicite : `RFC 8785` ne réalise ni signature, ni hachage, ni horodatage, ni ancrage immuable à elle seule (`SRC-077.txt`, L4, L15, L99–L107). **Verdict final : supporté**
4. **Ligne 33 (`RFC 9943` `SCITT` `[6]`, `RFC 9162`, `BSIF B-10` `[16]`, `Loi 25` `[21]`)** — `3` items :
   - `RFC 9943` (juin 2026) : énoncé `COSE_Sign1`, structure vérifiable en ajout seul anti-équivocation (telle que `RFC 9162`), reçu horodaté `COSE Receipt`, charge utile détachée par empreinte seule (sec. 6.2 et 8) (`SRC-044.txt`, L11, L112–145, L424–558, L999–1003, L1131, L1172–1174, L1270–1272). **Verdict final : supporté**
   - Stockage `WORM` reproductible sous forme écrite intelligible selon `BSIF B-10` (`SRC-068.txt`, L393). **Verdict final : supporté**
   - *Crypto-shredding* conditionné aux critères réglementaires de l'art. 23 (`SRC-063.txt`, L1777–1788). **Verdict final : supporté**
5. **Ligne 35 (`Kraishan` `[8]`, `BSIF B-15` `[15]`, `Bostan` `[10]`)** — `2` items :
   - Recensement `MCP` de Kraishan (septembre 2026) : `21 643` serveurs recensés, `14 353` analysés depuis `13 051` dépôts, absence de versionnement des définitions d'outils, `40,6 %` de dérive silencieuse sur `8 900` serveurs multi-versions (médiane `0` jour parmi ceux qui évoluent), `4,2 %` (`370`) redirections d'hôte (`SRC-057.txt`, L13–21, L47–67, L141–215, L552–638). **Verdict final : supporté**
   - `BSIF B-15` : exercice financier `2028` (`fin 2028`), portée 3 incluant catégorie 15 financée et assurée selon `GHG Protocol` et `PCAF` (volet `AUM` marqué `TBD`), traçabilité et contrôles comparables à l'information financière (`SRC-067.txt`, L384–394, L498–501, L667–753 ; `ancres-chronologiques.json` `2028-12-31-BSIF-B15-PORTEE3`). **Verdict final : supporté**

### B. Refonte de la section 9.2 (lignes 43 à 71 — 28 items, dont 9 rectifications appliquées)

6. **Lignes 43–49 (`τ-bench`, Yao *et al.* `[19]`)** — `6` items :
   - Définition de `pass^k` (`SRC-029.txt`, L261–262). **Verdict final : supporté**
   - Formule et estimateur sans biais \(\mathrm{pass}^k = \mathbb{E}_{\text{tâche}}[\binom{c}{k}/\binom{n}{k}] \approx \mathbb{E}_{\text{tâche}}[p_i^k]\) (`SRC-029.txt`, L277–284). **Rectification L41** : « obéit à une loi géométrique » remplacé par « décroît géométriquement » afin d'éviter la confusion mathématique avec la loi géométrique du premier succès. **Verdict final : supporté**
   - Chiffres `GPT-4o` appel de fonctions : `~61 %` (`pass^1` sur `τ-retail`), `~35 %` (`35,2 %` sur `τ-airline`), `< 25 %` (`~25 %` à `pass^8` sur `τ-retail`) (`SRC-029.txt`, L105–107, L476, L488–489). **Verdict final : supporté**
   - Comparaison uniforme \(0{,}61^8 \approx 1{,}9\,\%\) et effet mathématique de l'hétérogénéité des tâches sur \(\mathbb{E}[p_i^k] > (\mathbb{E}[p_i])^k\) (`SRC-029.txt`, § A Fig. 7, L764–779). **Verdict final : supporté**
   - Concentration des échecs sur politiques métier et calculs sur bases de données (`SRC-029.txt`, § 5.2, L517–571). **Rectification L45** : suppression de la mention prêtant à `τ-bench` une « corrélation d'échecs qui freine la baisse », au profit de l'explication exacte (inégalité sur l'hétérogénéité des tâches + concentration des difficultés sur politiques métier et bases de données). **Verdict final : supporté**
   - Plus des trois quarts des séries de huit essais comportant au moins un échec (`1 - 0,25 = 75 %`) face à `pass@k` (`SRC-029.txt`, L258, L488–489). **Verdict final : supporté**
7. **Ligne 53 (`MAP`, Pan *et al.* `[18]`)** — `4` items :
   - Devis mixte avril–novembre 2025, `20` études de cas, `306` répondants sur `26` domaines filtrés à `86` systèmes en production ou pilote (`SRC-027.txt`, L117–120). **Verdict final : supporté**
   - `68 %` au plus `10` étapes avant intervention humaine et `80 %` (`16` sur `20`) flux structurés fixes (`SRC-027.txt`, L135, L639 ; `FACT-MAP-STUDY`). **Verdict final : supporté**
   - `75 %` sans bancs (tests A/B et revue humaine), `74 %` revue humaine (`N=31`), `52 %` juges LLM, `39 %` couplés à l'humain, `39 %` référence non agentique (`SRC-027.txt`, L702, L754, L773, L785–786, L858–860). **Verdict final : supporté**
   - **Rectification L53** : remplacement de « concentrés en Amérique du Nord » par « les études de cas étant concentrées dans les Amériques avec quelques cas en Europe », fidèle à `SRC-027.txt` L331–356 (*Americas, with a few in Europe*, biais de participation et absence d'audit technique direct des journaux). **Verdict final : supporté**
8. **Ligne 56 (`τ-bench`, Yao *et al.* `[19, 20]`)** — `3` items :
   - Simulateur à bases JSON, API Python déterministes, usager simulé par LLM sur `115` tâches (`τ-retail`) et `50` (`τ-airline`) (`SRC-029.txt`, § 3, Table 1 L265–276). **Verdict final : supporté**
   - Répartition des échecs `GPT-4o` sur `τ-retail` : `~55 %` arguments/informations erronés et `25 %` mauvaises décisions face aux règles métier (`SRC-029.txt`, L535, L539). **Verdict final : supporté**
   - **Rectification L54** : précision exacte des limites — deux domaines simplifiés, éventuelles ambiguïtés des instructions et limites du simulateur d'usager (`SRC-029.txt`, L304–323, L607–616), défauts de spécification corrigés dans une version ultérieure (`τ2-Bench` cité dans `SRC-030.txt`, L1939–1941) et fuite du jeu de test dans le harnais *few-shot* (`SRC-030.txt`, L389, § A5 L1979–2019). **Verdict final : supporté**
9. **Ligne 57 (`HAL`, Kapoor *et al.* `[20]`)** — `4` items :
   - Infrastructure en machines virtuelles isolées, `21 730` exécutions, `9` modèles, `9` bancs, `2,5` milliards de jetons, `~40 000 \$ US`, inspection `Docent` sur `AssistantBench`, `SciCode` et `CORE-Bench` (`SRC-030.txt`, L44–51, L349–350, L1040–1041, L1065–1066). **Verdict final : supporté**
   - Quasi-absence d'exécution sans erreur d'outil sur `SciCode` et `CORE-Bench` ; `> 60 %` violations de consigne sur `AssistantBench` et `CORE-Bench` ; `~40 %` obstacles d'environnement dans les échecs sur les trois bancs (`SRC-030.txt`, L1098–1115). **Verdict final : supporté**
   - **Rectification L57 (attribution)** : séparation entre les raccourcis révélés par `Docent` (HuggingFace, carte de crédit erronée, L1087–1097) et les changements silencieux de poids ou de quantification révélés par l'exploitation multi-fournisseurs du harnais `HAL` (L472–475, L1871–1885). **Verdict final : supporté**
   - **Rectification L57 (limites)** : « l'omission du cache sur `SWE-Agent` » corrigé en « la non-prise en compte des économies de cache dans le calcul des coûts sur `SWE-Agent` » (`SRC-030.txt`, L1927–1929 : `SWE-Agent currently uses caching... our cost calculations don't yet account for cache hits`), avec `SWE-Bench Verified Mini`, matrice incomplète faute de budget, paramètres propriétaires opaques et absence de rejeu contre-factuel (`SRC-030.txt`, L1933–1971). **Verdict final : supporté**
10. **Ligne 55 (`MAST`, Cemri *et al.* `[3]`)** — `2` items :
    - `1 642` traces, `7` cadriciels, `14` modes de défaillance, `41 %` à `86,7 %` d'échecs globaux (`SRC-028.txt`, L106–112 ; `FACT-MAST-FAILURES`). **Verdict final : supporté**
    - Vérification absente (`8,20 %`) ou erronée (`9,10 %`) jusque dans des trajectoires aboutissant pourtant au bon résultat (`SRC-028.txt`, Fig. 1 L83–85, Table 7 L2186–2239). **Verdict final : supporté**
11. **Ligne 59 (`Dhanorkar et al.` `[17]`, `Barrett et al.` `[9]`)** — `2` items :
    - **Rectification L59 (`Dhanorkar et al.`)** : « 17 entrevues de développeurs chez Microsoft, dont 12 issus d'une même grande entreprise » corrigé en « 17 entrevues de développeurs menées par des chercheurs de Microsoft — dont 12 issus de la même grande entreprise technologique bien dotée en jetons — sur des tâches relativement modestes » (`SRC-075.txt`, L3–5, L223–230, L649–655) ; *eyeballing* et témoignage `P10` (`~10 %`) sans valeur statistique généralisable (`SRC-075.txt`, L392, L405–406). **Verdict final : supporté**
    - **Rectification L59 (`Barrett et al.`)** : « modélisation théorique de sûreté système illustrée sur un scénario hypothétique » précisée avec « caractérise néanmoins structurellement le scénario de perte » (`SRC-058.txt`, L1063, L2135–2146). **Verdict final : supporté**
12. **Ligne 61 (`BSIF E-23` `[13]`, `BSIF juil. 2026` `[14]`, `DORA` `[12]`, `EU AI Act` `[11]`, `NIST` `[7]`)** — `3` items :
    - **Rectification L61 (`BSIF`)** : précision sur `E-23` (`1er mai 2027`, principes 3.4 et 3.6 : validations indépendantes *proportionnées au risque* lors d'erreurs importantes, dérives ou violations de seuils, `SRC-065.txt`, L31, L399–L473) et sur le bulletin `BSIF` de juillet 2026 (*recommande* de tester rigoureusement les cas limites sous contrainte, `SRC-066.txt`, L27, L49, L103). **Verdict final : supporté**
    - **Rectification L61 (`DORA`)** : précision de l'art. 11(6)(a) (tests de continuité en cas de modification substantielle) et de l'art. 25(2) (évaluations de vulnérabilité avant déploiement/redéploiement critique pour les dépositaires centraux et contreparties centrales) (`SRC-062.txt`, L1962–1965, L2528–2540). **Verdict final : supporté**
    - `EU AI Act` art. 15 et 72 (`SRC-060.txt`, L3888–3922, L6113–6141) et `NIST AI 100-2e2025` (`SRC-054.txt`, L2480–2482, § 4.2.4 L2917–2933). **Verdict final : supporté**
13. **Lignes 65–71 (pipeline `EvalOps`, simulation hermétique, sas ombre et canari)** — `6` items :
    - Répétitions `pass^k` (`k >= 5`, seuil d'ingénierie) et jeux issus de journaux réels validés par experts dans `MAP` (`SRC-027.txt`, L757–765). **Verdict final : supporté**
    - Interventions `MAST` (`6` répétitions `AG2`/`GSM-Plus` avec `GPT-4o` `84,25 ± 1,86 %` à `89,00 ± 1,38 %` ; `ChatDev` sur `ProgramDev-v0` DAG vers graphe cyclique borné sous revue `CTO` de `25,0 %` à `40,6 %`, soit `15,6` points à modèle inchangé) (`SRC-028.txt`, Table 5 L1830–1856, § H.1–H.2). **Verdict final : supporté**
    - **Rectification L66 (`HAL`)** : reformulation en association observée sur les trois bancs analysés (« s'associe à des chances de succès de 1,5 à 4 fois plus élevées » et « à une probabilité de réussite supérieure de 13 % à 87 % sur les trois bancs analysés », reflétant Fig. 4a–4b et Table A4 `RR = 1,13` à `1,87` de `SRC-030.txt`, L1101–1108, L2572–2615), plus front de Pareto `NIST`/`HAL` (`SRC-054.txt`, `SRC-030.txt`). **Verdict final : supporté**
    - **Rectification L67 (`Kraishan`)** : « détecteurs statiques non calibrés » corrigé en « détecteurs statiques à motifs » (les détecteurs de Kraishan ayant précisément été validés/calibrés sur `414` cas pour mesurer `0,17` sur l'injection de commande contre `0,93` sur les dépendances non épinglées, `SRC-057.txt`, L300–379) ; `Docent` (`[20]`), `o1` `MAST` (`κ = 0,58` -> `0,77` avec `94 %` d'exactitude, `κ = 0,79` hors domaine, `SRC-028.txt` L132–133, L463–482), vulnérabilités corrélées `NIST` (`SRC-054.txt`, L2496) et routage `MAP` (`SRC-027.txt`, L787–794). **Verdict final : supporté**
    - Simulation hermétique (`HAL` VMs isolées `[20]`, figement d'outils par empreinte `[8]`, principe 3.2 de `BSIF E-23` sur données synthétiques/anonymisées `SRC-065.txt`, L538–561). **Verdict final : supporté**
    - Sas ombre et canari fondés sur le confinement sans écriture et la référence non agentique de `MAP` (`SRC-027.txt`, L702, L840–881) avec alertes `OpenTelemetry GenAI` (`[5]`). **Verdict final : supporté**

### C. Nettoyages et précisions des sections 9.3 et 9.4 (lignes 75, 77–79, 83, 85, 91, 93, 112, 118 — 13 items)

14. **Ligne 75 (`Dhanorkar et al.` `[17]`, `HAL` `[20]`)** — `1` item :
    - `17` développeurs : suivi en direct rare, signaux tardifs (`30` à `60` minutes selon `P03`), redirection en vol jugée inefficace imposant arrêt et redémarrage (`P02`/`P17`) (`SRC-075.txt`, L387–420) ; modification silencieuse de fournisseur (`SRC-030.txt`, L472–475, L1871–1885). **Verdict final : supporté**
15. **Lignes 81–83 (`MAST` `[3]`, `NIST` `[7]`, `Kraishan` `[8]`, `BSIF` `[14]`, `HAL` `[20]`)** — `3` items :
    - Répétition d'étapes (`15,7 %`) et perte de terminaison (`12,4 %`, exclusive aux échecs dans `ChatDev` et `MetaGPT`) (`SRC-028.txt`, Fig. 1 L80, L88, Table 7 L2215–2239). **Verdict final : supporté**
    - `NIST AI 100-2e2025` sec. 3.4.1 : tâches bouclantes, inhibition d'API, homoglyphes et jeton `<|endoftext|>` forçant une sortie vide (`SRC-054.txt`, L2601–2613). **Verdict final : supporté**
    - Redirection silencieuse `MCP` (`4,2 %`, `SRC-057.txt` L19) et substitution non annoncée de poids/quantification (`SRC-030.txt`, L472–475, L1871–1885 ; `SRC-066.txt`, L103, L117). **Verdict final : supporté**
16. **Lignes 87 et 85 (`BSIF E-23` `[13]`, `B-10` `[16]`, `DORA` `[12]`, `EU AI Act` `[11]`, `NIST` `[7]`, `MAST` `[3]`, `Barrett` `[9]`)** — `4` items :
    - `BSIF E-23` (`1er mai 2027`, principe 3.6, `SRC-065.txt` L177, L660–672) et `BSIF B-10` (concentration propre vs systémique, substituabilité/portabilité, sortie ordonnée et *stressed exit*, `SRC-068.txt` L315–318, L555, L777–793). **Verdict final : supporté**
    - `DORA` art. 11, 12, 28–30 (`SRC-062.txt`, L1936–2013, L2787–2803, L2933–2940) et `EU AI Act` art. 14(4)(e) et 15(4) (`SRC-060.txt`, L3878–3908). **Verdict final : supporté**
    - `NIST` défaillances corrélées (`SRC-054.txt`, L2496) et `MAST` (`GPT-4o` `39 %` d'erreurs `FC1` en moins que `Claude 3.7 Sonnet` dans `MetaGPT` ; modèles ouverts plus sujets aux échecs, `SRC-028.txt` L658–659, L2090–2091). **Verdict final : supporté**
    - `Barrett et al.` : écart entre capacités réelles du modèle et modèle mental du contrôleur rendant les contraintes inappropriées (`SRC-058.txt`, L918–927). **Verdict final : supporté**
17. **Lignes 95, 93, 112, 118 (`HAL` `[20]`, `CaMeL` `[1]`, `MAST` `[3]`, `Dhanorkar` `[17]`, `B-10` `[16]`, `B-15` `[15]`, `Bostan` `[10]`, `FOCUS` `[2]`)** — `5` items :
    - L95 (`HAL`) : `15 \$ / 75 \$` (`Claude Opus 4.1`) vs `0,1 \$ / 0,4 \$` (`Gemini 2.0 Flash`), `1` banc sur `9`, `21` sur `36`, `Online Mind2Web` `171 \$` (`SeeAct`+`GPT-5 Medium`) vs `1 577 \$` (`Browser-Use`+`Claude Sonnet 4`), `9×` pour `2` points, abstention vs paiement erroné (`SRC-030.txt`, L650–651, L773–774, L957–963, L1043, L1091–1097). **Verdict final : supporté**
    - **Rectification L99 (`CaMeL`)** : séparation explicite entre les ratios médians sous attaque (`2,82×` entrée, `2,73×` sortie avec `Claude 3.5 Sonnet`, `SRC-007.txt` Fig. 13 L1066–1070), les moyennes et dispersions **sous attaque du Tableau 12** (`3 764` à `13 463` jetons d'entrée, écart-type `21 276`, médiane `3 643`, `SRC-007.txt` L2561–2580) et celles **hors attaque du Tableau 11** (`2 999` à `14 889`, écart-type `22 622`, médiane `3 641`, `SRC-007.txt` L2498–2517), au lieu d'attribuer le Tableau 11 à la condition sous attaque. **Verdict final : supporté**
    - L101 (`MAST` & `Dhanorkar`) : `41 %` à `86,7 %` (`SRC-028.txt`), quotas généreux et relecture complète à chaque itération (`SRC-075.txt`, L464–467, L649–650). **Verdict final : supporté**
    - L120 (tableau `C_sécu`) : plans de sortie et continuité `B-10` (`SRC-068.txt`, § 2.3.4–2.3.5). **Verdict final : supporté**
    - L130 (`CaMeL`, `FOCUS`, `Bostan`, `B-15`) : `Claude 3.5 Haiku` + `Claude 4 Sonnet` réduisant le coût médian de `12 %` pour `~1 %` de perte d'utilité (`SRC-007.txt`, L701–703) ; `FOCUS` (`SRC-023.txt`) ; `BSIF B-15` fin `2028` (`SRC-067.txt`, `SRC-059.txt`). **Verdict final : supporté**

---

## Rappel consolidé de la passe G2 initiale (lignes actualisées `1` à `128`)

Les 52 contrôles atomiques de la passe initiale G2 couvrant l'ensemble du chapitre (ouverture illustrative `AO-07` à la ligne 5, section `9.1` lignes 13–35, section `9.2` lignes 37–71 après refonte G4 Tour 1, section `9.3` lignes 73–91, section `9.4` lignes 93–130 incluant le tableau unique lignes 107–114, encadré des trois arbitrages et conclusion lignes 132–138) demeurent intégralement au verdict `supporté`. Aucun renvoi `[n]` orphelin ni aucune source en `statut F` n'est utilisé.

---

## Contrôle différentiel post-lissage G5

- **Périmètre inspecté** : intégralité du `git diff HEAD` (depuis le commit `fe6e945`) sur [Chapitre 09 - Observer, prouver et compter.md](file:///c:/Github/Agentique/7%20-%20Livre%202027/manuscrit/03%20-%20Partie%20III/Chapitre%2009%20-%20Observer%2C%20prouver%20et%20compter.md) — **47** items contrôlés (`25` lignes à simple retrait de rétro-apostrophes et `22` lignes/paragraphes comportant des retouches rédactionnelles), vérifiés contre `sources/ch09-sources.md` (`[1]`–`[21]`), `corpus_l_plus/*.txt`, les registres et `verifie_manuscrit.py --unit ch09 --strict`.
- **Rectifications appliquées** (`15` paragraphes/lignes ajustés) : `L17` (renvoi `(chapitre 10)` rattaché à l'article 12.1 de la `Loi 25` et « 4 % du chiffre d'affaires mondial »), `L19` (« par les fournisseurs » et « voire plus selon le droit financier » à l'art. 19 de l'`EU AI Act`), `L31` (« consignes système » et « vers l'identité non humaine et le mandat »), `L33` (« ni signature, ni hachage, ni horodatage, ni ancrage immuable » pour `RFC 8785`), `L35` (« signe un énoncé `COSE_Sign1` et l'enregistre auprès d'un service de transparence » et « forme écrite intelligible » selon `BSIF B-10`), `L37` (dénominateur exact des `8 900` serveurs multi-versions pour `40,6 %` et `4,2 %` chez Kraishan `[8]`, et « données traçables jusqu'à leurs sources » selon `BSIF B-15`), `L57` (« 20 études de cas et 306 répondants sur 26 domaines (filtrés à 86 systèmes en production ou pilote) » selon `MAP`), `L57` (« arguments ou informations erronés » selon `τ-bench`), `L57` (périmètre des trois bancs pour les `40 %` d'obstacles d'environnement et « non-prise en compte des économies de cache dans le calcul des coûts sur SWE-Agent » selon `HAL`), `L63` (« validations indépendantes proportionnées au risque lors d'erreurs importantes, de dérives ou de violations de seuils » pour `BSIF E-23`, et mention des dépositaires centraux et contreparties centrales à l'art. 25 de `DORA`), `L77` (« quand le seuil est franchi », « maintenue et levée pour une durée erronée », « économiquement précieux » et « revues périodiques » selon `STAMP`/`STPA`), `L87` (« pouvant s'appuyer sur des solutions redondantes ou mesures après défaillance » selon `EU AI Act` art. 15(4)), `L95` (« à taux d'échec égal » et « coût réel » selon `HAL`), `L103` (correction de la coquille grammaticale « à fois » -> « à la fois ») et `L130` (« environ 1 % »).
- **Taux d'ancrage certifié post-G5** : **100 % `supporté`**
- **Imprécis résiduel** : **0**
- **Non supporté résiduel** : **0**

---

## Contrôle différentiel post-recollation G3 (`seed=202702`, `CA-14`)

- **Objet** : Micro-rectification à `L31` (`ch09:P013:S04`) identifiée lors de la recollation indépendante à froid `G3` passe 2 (`seed=202702`).
- **Écart détecté** : L'énoncé écrivait *« la télémétrie temps réel demandée par le BSIF [14] et DORA [12] »*, attribuant à tort un caractère impératif au bulletin technologique du BSIF de juillet 2026 (`SRC-066.txt` l. 423–431 : saines pratiques que *« institutions can consider... enabling real-time detection... feed AI telemetry into existing security operations »*) et attribuant littéralement l'expression *« télémétrie temps réel »* à DORA (`SRC-062.txt` art. 10 § 1–3 l. 1902–1913 et art. 17 l. 2231–2259 exigent des mécanismes permettant de *« détecter rapidement les activités anormales »*, des alertes automatiques et le suivi des incidents TIC).
- **Rectification appliquée (`L31`)** : « livrant au centre de sécurité la télémétrie temps réel demandée par le BSIF [14] et DORA [12] sans exposer de données confidentielles. » remplacé par « livrant au centre de sécurité la télémétrie IA préconisée par le BSIF pour la détection en temps réel [14] à l'appui de la détection rapide des activités anormales requise par DORA [12], sans exposer de données confidentielles. » (`[14]` et `[12]` préservés sans modification des tableaux ni de la numérotation).
- **Verdict post-G3 (`L31`)** : **supporté**
- **Imprécis résiduel** : **0**
- **Non supporté résiduel** : **0**

---

## Réindexation différentielle post-audit v1.3 (2 décembre 2026)

- **Périmètre `v1.3`** : `manuscrit/03 - Partie III/Chapitre 09 - Observer, prouver et compter.md` (`144` lignes, `5 518` mots `G1` / `5 716` `split()`), `22` sources `L+` (`[1]` à `[22]`, ajout `[22]` `SRC-077`).
- **Mises à jour et réancrages vérifiés** :
  - `L91` (ex-`L85`, Pass 3 `#44`) : limitation des jetons exprimée sur les compteurs normalisés `gen_ai.usage.input_tokens` et `output_tokens` (`[5]` `SRC-037.txt` l. 250–251) servant d'assiette FinOps au coût par dossier, et exigence de versionnage des définitions d'outils au registre avec épinglage côté client des points de terminaison et condensats de paquets (`[8]` `SRC-057.txt` l. 769–773). `Verdict : supporté`.
  - `L43`, `L45`, `L51`, `L55–L59`, `L67–L73`, `L79`, `L85–L89`, `L101`, `L113` (ex-`L107`), `L119`, `L125`, `L141` : aération des listes, scission de phrase longue en `L113` et uniformisation typographique `pass¹` / `pass⁸` / `passᵏ` (synchronisée avec `specs/toc.md` sur `## 9.2`). `Verdict : supporté`.
  - `L21` (`[4]` `SRC-035.txt` `CloudEvents v1.0.2`, l. 1, 5, 73–85) : traçage des événements sans fuite de données personnelles dans le bus d'exploitation. `Verdict : supporté`.
  - `L31` (`[5]` `SRC-037.txt`, l. 640–668) : correction du nom d'intervalle OpenTelemetry GenAI en `execute_tool` (au lieu de l'ancien tiret), aligné sur `SRC-037.txt`. `Verdict : supporté`.
  - `L33–L35` (`[22]` `SRC-077.txt`, l. 4, 15, 212–214, 302–339 ; `[16]` `SRC-068.txt`, l. 393) : réancrage explicite de `RFC 8785` (*JSON Canonicalization Scheme*, `JCS`) sur `SRC-077.txt` (en remplacement de l'erreur antérieure vers la source `A2A`). `Verdict : supporté`.
  - `L37` (`[11]` `SRC-060.txt`, l. 4242, 4278–4280) : conservation minimale des journaux imposée aux déployeurs par l'article `26(6)` (et fournisseurs art. `19`) de l'`EU AI Act`. `Verdict : supporté`.
  - `L95` et `L97` : reformulations anti-collision `CA-03` sur FinOps agentique et l'effet harnais `HAL` (`Online Mind2Web`, `[20]` `SRC-030.txt`), plus `Tableau 9.1` (`L125`). `Verdict : supporté`.
