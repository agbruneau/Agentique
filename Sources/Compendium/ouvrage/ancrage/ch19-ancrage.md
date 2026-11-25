# Journal d'ancrage atomique Wyvern G2 — Chapitre 19 (`ch19`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/07 - Partie VII/Chapitre 19.md` (`4 491` mots de prose selon `parser_plan` / `verifie_manuscrit`, plage `[4 076, 4 784]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch19-sources.md` (`[1]`–`[7]` en statut `L+`, `1` exclusion `statut F` sur `genai.owasp.org`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json` et `Tomes/Tome 8 .../trousse/`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b3-6`
- **Passe G2 initiale (supportés)** : 9
- **Rectifications appliquées lors de la passe G2 :** 30
- **Verdict final — supportés :** 41 / 41 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 19.md`

Toutes les formulations demandant un resserrement documentaire à la passe initiale ont été directement rectifiées dans [Chapitre 19.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/07%20-%20Partie%20VII/Chapitre%2019.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant les vedettes propriétaires `blanchiment de frontière` et `injection indirecte de consignes`, les `owned_concepts`, l'ensemble des renvois `[1]`–`[7]` et le calibrage (`4 381` mots dans `[4 076, 4 784]`, barrière `G1 --unit ch19 --strict` passée à `0` erreur) :

1. **Séparation stricte entre corpus `L+` (`[1]`–`[7]`) et relevés internes du `Corpus` (`L7`, `L15`, `L17`, `L29`, `L33`, `L50`, `L56`, `L58`, `L92`–`L95`, Tableaux 19.1 et 19.2) :** requalification explicite, comme relevés internes hors archive `L+` de ce chapitre, de `CVE-2025-32711` (`Tome 1 § 11.1.3`), des boutons préremplis (« résumer avec l'IA », `Tome 3 § 14.5`), de l'expression *agent session smuggling* (`Tome 1 § 19.6`), de `AML.T0104` / `AML.T0053` / `AML.M0027` et `UNC6395` (`Tome 1 § 19.1`), de `F-52` (`Tome 1 § 39.2.1`), des `304` redirections / `212` comptes GitHub (`Tome 3 § 8.8`), des `102` fiches `NVD` (`Tome 3 § 49.7`), des `CVE-2025-6514` / `49596` / `54136`, de `MINJA` (`Tome 3 § 14.5`) et de `26,1 %` sur `31 132` compétences `Agent Skills` (`Tome 3 § 13.3`, analyse statique sans confirmation d'exploitation).
2. **Correction du rattachement statistique `OR = 2,96` (`L15`, `L54`, Tableau 19.1) :** rattachement exact du rapport de cotes `OR = 2,96` (IC `95 % [2,56 ; 3,42]` sur `6 699` serveurs multi-versions scannés) à la dérive sémantique silencieuse (`40,58 %`, IC `[39,57 ; 41,61]`) plutôt qu'aux redirections d'hôte (`4,16 %`), conformément à `SRC-057.txt` (`L21–22`, `L639–641`).
3. **Distinction entre étude `CaMeL` `L+` et évaluation `Borealis-Bench` (`L19`, `L45`) :** rattachement du résultat `77 %` contre `84 %` sur `AgentDojo` à `SRC-007.txt` (`arXiv:2503.18813v2`, propriété `ch20`), et qualification explicite de `Borealis-Bench` Campagne 2 (`95,83 %` de rappel, `115/120`, `0,00 %` FP, `5` manques sur `data_exfiltration_trifecta`) comme mesure expérimentale interne antérieure (`Tome 3 § 31.4`, hors `L+` et hors périmètre `G0`).
4. **Qualification des référentiels externes et des cibles architecturales (`L21`, `L39`, `L47`, `L66`–`L70`, `L88`, `L97`, `L103`, `L124`–`L130`) :** précision du statut bêta d'`OWASP MCP Top 10`, du statut de cadre d'auteur de `CSA MAESTRO`, de l'archétype à contrôleur unique de `STAMP`/`STPA` (`[7]`), de l'implémentation `G0` réelle (`taint_camel.py`, `camel_taint.rego`, `mcp_pinning.py`, `13/13` fichiers `owasp_src055` sous `OPA/Rego` et `metamorphic.py`) face aux cibles de conception `Tome 3` (`HMAC`, `Cedar`, `ASR_action = 0,0 %`), et alignement des portes `PRR S-08` et `PRR S-12` ainsi que des renvois amont/aval (`L9`, `L134`, `L136`).

---

## 2. Inventaire atomique et confrontation aux sources (`C19-01` à `C19-41`)

### Ouverture et Résumé exécutif (`L1–L21`)

- **C19-01 (`L1–L3`)** — *Affirmation :* Titre et question directrice cadrant la caractérisation des surfaces d'attaque non composables des Systèmes d'agentivité (injection indirecte, mutations silencieuses d'outils et de mémoire) et l'établissement de contrôles préventifs vérifiables avant production.
  - **Appui vérifié :** `specs/manifest.json` (`ch19`, `D07`, `SUB_D07_01`), `SRC-055.txt` (`[1]`), `SRC-057.txt` (`[4]`), `SRC-002.txt` (`[5]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C19-02 (`L5`)** — *Affirmation :* Contrairement à la séparation classique entre instructions et données, les agents `LLM` font converger consignes système, requêtes, courriels, pages Web, descriptions `MCP` et souvenirs dans un même flux de jetons.
  - **Appui vérifié :** `SRC-054.txt` (`[3]`, § 3.4 L2579–2583), `SRC-002.txt` (`[5]`, § 1–2 L50–97).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C19-03 (`L7`)** — *Affirmation :* Selon le modèle de la triade létale retenu par le cadre (`Tome 2 § 9.6`, `Tome 3 § 31.1`), l'assemblage de trois capacités auditables isolément (données internes, messagerie externe, envoi sortant) permet l'exfiltration zéro-clic (`ASI01`), tandis que `MCP` et les compétences subissent des altérations silencieuses après homologation.
  - **Appui vérifié :** `SRC-055.txt` (`[1]`, `ASI01` L363–365), `SRC-002.txt` (`[5]`, § 4.3), `SRC-057.txt` (`[4]`), `SRC-095.txt` (`[6]`), `Corpus/Tome 2` (`L4314–4351`), `Corpus/Tome 3` (`L16290–16296`).
  - **Passe initiale :** écart rectifié · **Action :** reformulée pour attribuer explicitement la notion de triade létale au cadre (`Tome 2`/`Tome 3`) et son illustration zéro-clic à `[1, 5]` · **Verdict : supporté**

- **C19-04 (`L9`)** — *Affirmation :* Périmètre D07 au gel `2026-12-02` (`EXIG-SEC-01`..`05`, `18`..`22`, `24`, `EXIG-MCP-20`, `CAP-038`, `ADR-019`, avec appui sur `ADR-008`/`ADR-010` posés ← Ch. 10–11), renvois `→ Ch. 20–21`, clause `non-avis` `AO-05` et exclusion `statut F` de `genai.owasp.org` (`HTTP 403`) au profit de `[1, 2]`.
  - **Appui vérifié :** `sources/ch19-sources.md` (`L3–5`, `L88–90`), `recherche/registre-statut-f.json`, `registre/matrice-exig-prr-c40.json` (`CAP-038`), `SRC-055.txt` (`[1]`, L13–18), `SRC-059.txt` (`[2]`), `Corpus/Tome 3` (`L7137`, `L7792`, `L17039`).
  - **Passe initiale :** écart rectifié · **Action :** précisé que `ADR-008` et `ADR-010` relèvent de l'appui posé en amont (`← Ch. 10–11`) · **Verdict : supporté**

- **C19-05 (`L13`)** — *Affirmation :* Trois surfaces couplées (`ASI01`, `ASI04`, `ASI06`) et mécanisme de **blanchiment de frontière** lorsqu'un agent amont transmet en prose non qualifiée une donnée contaminée à un agent aval.
  - **Appui vérifié :** `registre/glossaire-termes.json` (`L303–309`, vedette propriétaire `blanchiment de frontière`), `SRC-055.txt` (`[1]`, `ASI01`, `ASI04`, `ASI06`, `ASI07`), `SRC-057.txt` (`[4]`), `SRC-002.txt` (`[5]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C19-06 (`L15`)** — *Affirmation :* `EchoLeak` (`[1]`, `CVE-2025-32711` au relevé interne `Tome 1 § 11.1.3`) illustre l'exfiltration par **injection indirecte de consignes** ; Kraishan (`[4]`) mesure sur `21 643` serveurs `MCP` et `72 606` versions (`8 900` multi-versions) `51,09 %` de changements, `40,58 %` de dérive sémantique silencieuse (`OR = 2,96` de faille grave sur `6 699` scannés) et `4,16 %` de redirections d'hôte.
  - **Appui vérifié :** `SRC-055.txt` (`[1]`, L363–365, L2118–2134), `SRC-054.txt` (`[3]`, § 3.4.3 L2677–2680), `SRC-057.txt` (`[4]`, L13–22, L553–559, L639–641), `registre/glossaire-termes.json` (`L359–365`), `Corpus/Tome 1` (`L3033`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié `CVE-2025-32711` (`Tome 1`) de `[1, 3]` et rattaché `OR = 2,96` exactement à la dérive silencieuse `40,58 %` sur `6 699` scannés plutôt qu'à `4,16 %` · **Verdict : supporté**

- **C19-07 (`L17`)** — *Affirmation :* Un relevé interne du `Tome 3 (§ 13.3)` hors `L+` (analyse statique sans confirmation d'exploitation) signale `26,1 %` de motifs vulnérables parmi `31 132` compétences `Agent Skills` (environ doublé avec scripts), et `EXIG-SEC-05` (`Tome 2 § 9.6`) proscrit les filtres probabilistes comme contrôle unique face aux attaquants adaptatifs `[3, 5]`.
  - **Appui vérifié :** `Corpus/Tome 3` (`L6620`), `Corpus/Tome 2` (`L4373–4379`), `SRC-054.txt` (`[3]`, § 4.1.2 L2797–2798), `SRC-002.txt` (`[5]`, § 2 L120–125).
  - **Passe initiale :** écart rectifié · **Action :** réancrée l'origine interne `Tome 3 § 13.3` (hors `L+`, analyse statique sans exploitation confirmée) du chiffre `26,1 %` et rattachée `EXIG-SEC-05` au `Tome 2 § 9.6` · **Verdict : supporté**

- **C19-08 (`L19`)** — *Affirmation :* Marquage `UNTRUSTED_EXTERNAL` (`EXIG-SEC-03`, `taint_camel.py` en `G0`), sas `SLM`/`CaMeL` (`CAP-038`), `77 %` sur `AgentDojo` contre `84 %` sans défense (`SRC-007` au `→ Ch. 20`) et `95,83 %` de rappel sur `Borealis-Bench` Campagne 2 (mesure interne antérieure `Tome 3 § 31.4`, hors `L+` et hors `G0`).
  - **Appui vérifié :** `taint_camel.py` (`L14`), `SRC-007.txt` (`L13–14`), `registre/faits-empiriques.json` (`FACT-CAMEL-AGENTDOJO`), `Corpus/Tome 3` (`L16412`), `Corpus/Tome 8` (`L1763`).
  - **Passe initiale :** écart rectifié · **Action :** séparée la référence `L+` `CaMeL` (`SRC-007`) de la mesure antérieure `Borealis-Bench` (`Tome 3 § 31.4` hors `G0`) · **Verdict : supporté**

- **C19-09 (`L21`)** — *Affirmation :* Face aux lacunes `MCP` `[4, 6]`, scellement `SHA-256 JCS` à `tools/list` et pré-appel (`EXIG-MCP-20`, `EXIG-SEC-18`, `mcp_pinning.py` en `G0`), classement `Q-A`..`Q-D` sur matrice `ASI01`–`ASI10` `[1, 2]` × `NIST AI 100-2` `[3]` × `MCP Top 10` (bêta) × `CSA MAESTRO` (`EXIG-SEC-01`, `ADR-019`), et protection `ASI06` (`OPA` en `G0`, cible `HMAC`/`Cedar` `Tome 3`) sous `Red Team` `FR`/`EN` (`EXIG-SEC-24`, `ADR-019` `ASR_action = 0,0 %`).
  - **Appui vérifié :** `SRC-057.txt` (`[4]`), `SRC-095.txt` (`[6]`), `SRC-055.txt` (`[1]`), `SRC-059.txt` (`[2]`), `SRC-054.txt` (`[3]`), `aq/rapports-g0.json`, `Corpus/Tome 2` (`Tableau 37`, `L4606–4680`), `Corpus/Tome 3` (`L16657`, `L17039–17065`).
  - **Passe initiale :** écart rectifié · **Action :** distinguées les preuves `L+` `[1]`–`[6]` des spécifications normatives du traité (`EXIG-*`, `Q-A..Q-D`, `MAESTRO`, `Cedar`/`HMAC`) et de l'épreuve `G0` (`mcp_pinning.py`, `OPA`) · **Verdict : supporté**

### Section 19.2.1 — Injection indirecte, non-compositionnalité et chaîne logistique (`L27–L84`, Figures 1–2, Tableau 19.1)

- **C19-10 (`L27`)** — *Affirmation :* Distinction entre injection directe (utilisateur malveillant) et **injection indirecte de consignes** (usager légitime, directives adverses dans un document, courriel ou retour d'outil faute de séparation matérielle entre ordre et donnée dans le mécanisme d'attention).
  - **Appui vérifié :** `SRC-055.txt` (`[1]`, `ASI01` L326–339), `SRC-054.txt` (`[3]`, § 3.4 L2579–2593), `SRC-002.txt` (`[5]`, § 2 L86–97), `registre/glossaire-termes.json` (`L359–365`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C19-11 (`L29`)** — *Affirmation :* `NIST AI 100-2e2025` classe l'injection indirecte sous `NISTAML.015` `[3]`, `OWASP` sous `ASI01` `[1, 2]`, illustrée par les boutons bureautiques préremplis (`Tome 3 § 14.5`, hors `L+`, `50` invites / `31` entreprises), les scénarios messagerie `[5]` et `EchoLeak` (`[1]`, `CVE-2025-32711` au `Tome 1 § 11.1.3`).
  - **Appui vérifié :** `SRC-054.txt` (`[3]`, L326, L2577), `SRC-055.txt` (`[1]`, L363–365), `SRC-002.txt` (`[5]`, § 4.3), `Corpus/Tome 3` (`L7323`), `Corpus/Tome 1` (`L3033`).
  - **Passe initiale :** écart rectifié · **Action :** ajoutée la référence exacte `NISTAML.015` (`[3]`) et rattachés les boutons préremplis au `Tome 3 § 14.5` hors `L+` · **Verdict : supporté**

- **C19-12 (`L31`)** — *Affirmation :* Non-compositionnalité de la sûreté : des modules validés unitairement recréent une faille critique dès qu'une session réunit exposition non fiable (`A`), données sensibles (`B`) et canal sortant ou mutateur (`C`) (`Tome 2 § 9.6`, `Tome 3 § 31.1`) `[1, 5]`.
  - **Appui vérifié :** `SRC-055.txt` (`[1]`, L237–242, L472–479), `SRC-002.txt` (`[5]`, § 3 L149–155), `Corpus/Tome 2` (`L4314–4363`), `Corpus/Tome 3` (`L16290–16296`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C19-13 (`L33`)** — *Affirmation :* Propagation multi-agents et chaînage `MCP`, incluant le mécanisme illustré dans la note de veille *agent session smuggling* (`Tome 1 § 19.6`, hors `L+`), les contournements en chaîne `[1, 5]`, et le périmètre conjoint outils/invites/mémoire `[1, 3]`.
  - **Appui vérifié :** `SRC-055.txt` (`[1]`, `ASI07` L987–993), `SRC-002.txt` (`[5]`, § 3), `SRC-054.txt` (`[3]`, § 3.5), `Corpus/Tome 1` (`L4618`).
  - **Passe initiale :** écart rectifié · **Action :** qualifiée l'origine `Tome 1 § 19.6` hors `L+` de l'expression *agent session smuggling* et reformulé l'effet en chaîne selon `[1, 5]` · **Verdict : supporté**

- **C19-14 (`L35–L37`, Figure 1)** — *Affirmation :* Le schéma `SCH-19-01.svg` et sa légende illustrent la reconstitution de la triade létale à partir de trois capacités bénignes et le désamorçage par pré-lecteur `SLM` et suivi `CaMeL`.
  - **Appui vérifié :** `specs/manifest.json` (`ch19`, `SCH-19-01`), `schemas/SCH-19-01.svg`, `schemas/rendus/SCH-19-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C19-15 (`L39`)** — *Affirmation :* Les parades probabilistes (*Spotlighting* `[3]`, injonctions système `[3]`, classifieurs tels *Prompt Shields* cités au `Tome 2 § 9.6`) cèdent face aux formulations obliques, à l'encodage `Base64` (`[3]`), à l'équivalence détection / classification robuste (`[3]`) et aux attaques adaptatives `[3, 5]`, d'où `EXIG-SEC-05` (`Tome 2 § 9.6`).
  - **Appui vérifié :** `SRC-054.txt` (`[3]`, L2655–2656, L2701–2704, L2797–2798), `SRC-002.txt` (`[5]`, L120–125), `Corpus/Tome 2` (`L4371–4379`).
  - **Passe initiale :** écart rectifié · **Action :** attribués *Spotlighting*, `Base64` et l'équivalence théorique exactement à `[3]`, et *Prompt Shields* / `EXIG-SEC-05` au `Tome 2 § 9.6` · **Verdict : supporté**

- **C19-16 (`L41–L43`)** — *Affirmation :* Taxonomie des six patrons architecturaux de Beurer-Kellner et coll. `[5]` (*action-selector*, *plan-then-execute*, *map-reduce LLM*, *dual-LLM*, *code-then-execute*, *context-minimization*) plaçant la défense dans le graphe de contrôle hors du modèle.
  - **Appui vérifié :** `SRC-002.txt` (`[5]`, § 3.1 L160–384).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C19-17 (`L45`)** — *Affirmation :* Sas `SLM` sans outil sous `JSON Schema` fermé (`CAP-038`, `EXIG-SEC-03`) alimentant `CaMeL` (`→ Ch. 20`) ; `77 %` vs `84 %` sur `AgentDojo` (`SRC-007`), et mesure interne complémentaire `Borealis-Bench` Campagne 2 (`Tome 3 § 31.4` hors `L+`/`G0` : `95,83 %` de rappel, `115/120`, `0,00 %` FP, `5` manques sur `data_exfiltration_trifecta`).
  - **Appui vérifié :** `SRC-007.txt` (`L13–14`), `registre/faits-empiriques.json` (`FACT-CAMEL-AGENTDOJO`), `Corpus/Tome 3` (`L16412`), `Corpus/Tome 8` (`L1763`).
  - **Passe initiale :** écart rectifié · **Action :** précisée la provenance `SRC-007` (`ch20`) et la qualification interne hors `G0` de `Borealis-Bench` avec le détail exact des `5` échecs sur `15` · **Verdict : supporté**

- **C19-18 (`L47`)** — *Affirmation :* Surface chaîne logistique des outils (`ASI04` `[1]`, `MCP03`/`MCP04` en statut bêta selon `Tome 2`/`Tome 3 § 31.3`) ; `MCP` normalise `JSON-RPC` mais pas la confiance cryptographique `[6]`, ne versionne pas les définitions d'outils `[4]` et présente le défaut interne `F-52` (huit champs `Tool` en `MCP 2025-11-25`, `Tome 1 § 39.2.1`, `← Ch. 07`).
  - **Appui vérifié :** `SRC-055.txt` (`[1]`, L653–700), `SRC-095.txt` (`[6]`, § 2.2 L153–169), `SRC-057.txt` (`[4]`, L144–146), `Corpus/Tome 1` (`L4710`, `L9237`), `Corpus/Tome 2` (`L4253`), `Corpus/Tome 3` (`L16329–16336`).
  - **Passe initiale :** écart rectifié · **Action :** séparés `ASI04` `[1]` et les faits `[4, 6]` des repères `MCP03/04` (`Tome 2/3`) et `F-52` (`Tome 1`) · **Verdict : supporté**

- **C19-19 (`L49–L52`)** — *Affirmation :* Trois classes d'attaques : empoisonnement d'outil (`[1, 4]`, `AML.T0104` au relevé interne `Tome 1 § 19.1` hors `L+`), ombrage d'outil (`[4, 6]`), et mutation silencieuse *rug-pull* (`[4, 6]`).
  - **Appui vérifié :** `SRC-055.txt` (`[1]`, L460–466, L679–681), `SRC-057.txt` (`[4]`, L98–100, L228–230), `SRC-095.txt` (`[6]`, L235–242), `Corpus/Tome 1` (`L4505`).
  - **Passe initiale :** écart rectifié · **Action :** qualifiée l'origine `Tome 1 § 19.1` hors `L+` de l'identifiant `AML.T0104` · **Verdict : supporté**

- **C19-20 (`L54`)** — *Affirmation :* Recensement Kraishan `[4]` (`21 643` serveurs, `72 606` versions, `14 353` codes sources de `13 051` dépôts, `8 900` multi-versions) : `51,09 %` (`4 547`, IC `[50,05 ; 52,13]`) modifiés, `40,58 %` (IC `[39,57 ; 41,61]`) en dérive silencieuse associée à `OR = 2,96` (IC `[2,56 ; 3,42]`) sur `6 699` multi-versions scannés, et `4,16 %` (`370`) de redirections d'hôte.
  - **Appui vérifié :** `SRC-057.txt` (`[4]`, L13–22, L196–197, L553–559, L639–641).
  - **Passe initiale :** écart rectifié · **Action :** rattaché exactement `OR = 2,96` aux `6 699` multi-versions scannés et à la dérive silencieuse `40,58 %` · **Verdict : supporté**

- **C19-21 (`L56`)** — *Affirmation :* Li et Gao (cités dans `[4]`) recensent `833` serveurs vulnérables sur `67 057` entrées ; les relevés internes du `Corpus` (hors `L+`) complètent par `304` redirections et `212` comptes GitHub réenregistrables (`Tome 3 § 8.8`), `102` fiches `NVD` (`Tome 3 § 49.7`, `← Ch. 07`) et `CVE-2025-6514`, `CVE-2025-49596` (`Tome 1 § 11.1.3`) et `CVE-2025-54136` (`Tome 3 § 31.9`).
  - **Appui vérifié :** `SRC-057.txt` (`[4]`, L104–105), `Corpus/Tome 3` (`L3996`, `L16623`, `L26949`), `Corpus/Tome 1` (`L3037`).
  - **Passe initiale :** écart rectifié · **Action :** dissociée la citation présente dans `[4]` (`67 057` / `833`) des relevés internes `Tome 1` et `Tome 3` hors `L+` · **Verdict : supporté**

- **C19-22 (`L58`)** — *Affirmation :* Sur les paquets `Agent Skills` (`SKILL.md`), le relevé interne `Tome 3 § 13.3` (hors `L+`, analyse statique sans confirmation d'exploitation) rapporte `26,1 %` de motifs vulnérables sur `31 132` compétences (environ doublé avec scripts) ; sous `ASI04` `[1]`, le chargement non vérifié reste prohibé.
  - **Appui vérifié :** `Corpus/Tome 3` (`L6620`), `SRC-055.txt` (`[1]`, `ASI04` L729–731).
  - **Passe initiale :** écart rectifié · **Action :** retirée l'attribution `[1, 4]` du chiffre `26,1 %` et qualifiée sa provenance `Tome 3 § 13.3` hors `L+` · **Verdict : supporté**

- **C19-23 (`L60–L62`, Figure 2)** — *Affirmation :* Le schéma `SCH-19-02.svg` et sa légende opposent les registres publics mutables (`40,58 %` dérives `MCP` `[4]` et `26,1 %` `Skills` selon `Tome 3`, sous `F-52`) au verrou `SHA-256 JCS` en passerelle `PEP`.
  - **Appui vérifié :** `specs/manifest.json` (`ch19`, `SCH-19-02`), `schemas/SCH-19-02.puml`, `schemas/rendus/SCH-19-02.svg`.
  - **Passe initiale :** écart rectifié · **Action :** précisée en légende la provenance `Tome 3` du `26,1 %` · **Verdict : supporté**

- **C19-24 (`L64–L70`)** — *Affirmation :* Cinq obligations bloquantes (`EXIG-MCP-20`, `EXIG-SEC-18..22`, `EXIG-MCP-21`, `Tome 2 § 6.5` et `§ 9.8`) : scellement `SHA-256 JCS` (complété par la veille `SEP-2640` `Tome 3 § 5.2`), révocation sur `list_changed` ou redirection `[4]`, espaces de noms et blocage `sampling`/`elicitation`, registre interne et `AIBOM` `CycloneDX`/`SPDX` `[1]` (`→ Ch. 22`), et admission attestée (`/.well-known/mcp-attestation`, `[6]`) avec plan de contingence tiers (`Tome 2 § 9.8`).
  - **Appui vérifié :** `SRC-057.txt` (`[4]`), `SRC-055.txt` (`[1]`, `ASI04` L727–731, Appendix B), `SRC-095.txt` (`[6]`, § 8–10, Appendix C L1015–1028), `Corpus/Tome 2` (`L4606–4654`), `Corpus/Tome 3` (`L2090`).
  - **Passe initiale :** écart rectifié · **Action :** distinguées les primitives attestées de `[6]` (URI, liste blanche, `Ed25519`) des exigences `Tome 2` et de `SEP-2640` (`Tome 3`) · **Verdict : supporté**

- **C19-25 (`L72`)** — *Affirmation :* Dans Metere (`arXiv:2605.24248` `[6]`), l'hôte vérifie hors bande une assertion signée `Ed25519` contre une racine de confiance verrouillée, n'admet que la liste blanche fermée locale et journalise chaque décision dans un journal chaîné, en composition avec le suivi de dérive aval (§ 9 `[6]`).
  - **Appui vérifié :** `SRC-095.txt` (`[6]`, § 5 L350–449, § 5.5 L458–481, § 9 L822–866).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C19-26 (`L74`)** — *Affirmation :* Troisième surface en état persistant (`ASI06` `[1]`) : `AgentPoison` (`[1]` réf. 4, `Tome 3 § 14.5`), `MINJA` (`Tome 3 § 14.5` hors `L+`) et attaques `RAG` `PoisonedRAG`/`Phantom` `[3]` insèrent des déclencheurs dormants biaisant les requêtes futures, imposant le cloisonnement `CoALA` et le filtrage `ACL` (`← Ch. 11`).
  - **Appui vérifié :** `SRC-055.txt` (`[1]`, `ASI06` L855–949), `SRC-054.txt` (`[3]`, L2646–2651), `Corpus/Tome 3` (`L7315–7317`).
  - **Passe initiale :** écart rectifié · **Action :** attribuées exactement `AgentPoison` à `[1]`/`Tome 3`, `MINJA` au `Tome 3` hors `L+`, et `PoisonedRAG`/`Phantom` à `[3]` · **Verdict : supporté**

- **C19-27 (`L76`)** — *Affirmation :* Effet cumulatif sur chaînes à horizon long : lorsqu'une dégradation ou un fragment `ASI06` franchit les contrôles initiaux, la boucle de rétroaction s'érode progressivement et amplifie l'écart de trajectoire (`← Ch. 13`) `[1, 7]`.
  - **Appui vérifié :** `SRC-055.txt` (`[1]`, `ASI06`/`ASI08`), `SRC-058.txt` (`[7]`, § 7 L1030–1049).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C19-28 (`L78–L84`, Tableau 19.1)** — *Affirmation :* Le Tableau 19.1 synthétise les trois surfaces (`ASI01`, `ASI04`, `ASI06`), leurs vecteurs, prévalences mesurées (`L+` et relevés qualifiés) et verrous préventifs.
  - **Appui vérifié :** cohérence avec `C19-05`..`C19-27` et `SRC-055/054/057/002/095`.
  - **Passe initiale :** écart rectifié · **Action :** alignés les renvois et mentions `Tome 1`/`Tome 3` et `OPA`/`Cedar` dans les trois lignes du tableau · **Verdict : supporté**

### Section 19.2.2 — Taxonomies, matrice `ASI`, `STPA` et suivi de contamination (`L88–L130`, Figure 3, Tableau 19.2)

- **C19-29 (`L88`)** — *Affirmation :* Double axe de modélisation (`EXIG-SEC-01`, `EXIG-SEC-02`) : classement causal sur le **mandataire confus** (Norm Hardy 1988, cité dans `[4, 6]`) et matrice croisant `OWASP ASI01`–`ASI10` `[1, 2]` et `NIST AI 100-2e2025` `[3]` avec `MCP Top 10` (bêta), `MITRE ATLAS` et `CSA MAESTRO` (`Tome 2 Tableau 37`, `Tome 3 § 31.3, 31.8`).
  - **Appui vérifié :** `SRC-055.txt` (`[1]`), `SRC-059.txt` (`[2]`), `SRC-054.txt` (`[3]`), `SRC-057.txt` (`[4]`, L911), `SRC-095.txt` (`[6]`, L1109), `Corpus/Tome 2` (`L4247–4293`), `Corpus/Tome 3` (`L16327–16515`).
  - **Passe initiale :** écart rectifié · **Action :** attribuée la citation de Hardy à `[4, 6]` et séparés les référentiels du `Tome 2`/`Tome 3` du socle `[1, 2, 3]` · **Verdict : supporté**

- **C19-30 (`L90–L95`)** — *Affirmation :* Rattachement aux maillons `Q-A`..`Q-D` (`← Ch. 16`, `Tome 1 § 19.4`) : `Q-A` (`UNC6395` relevé `Tome 1 § 19.1, F-21` hors `L+` avec sa réserve d'auteur), `Q-B` (`AML.T0104` `Tome 1`, `F-52`, `40,58 %` `[4]`, `AgentPoison` `[1]`), `Q-C` (*token passthrough* `[4]`, `ASI03` `[1, 2]`, `OBO` `← Ch. 17`), et `Q-D` (`ASI09` `[1, 2]`, `AML.T0053`/`AML.M0027` relevé `Tome 1 § 19.1` hors `L+`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L4505–4509`, `L4555–4565`), `SRC-057.txt` (`[4]`, L231–233, L554–555), `SRC-055.txt` (`[1]`), `SRC-059.txt` (`[2]`).
  - **Passe initiale :** écart rectifié · **Action :** qualifiés les identifiants `UNC6395`, `AML.T0104` et `AML.T0053`/`M0027` comme issus du relevé interne `Tome 1 § 19.1` hors `L+` · **Verdict : supporté**

- **C19-31 (`L97–L101`)** — *Affirmation :* Articulation avec `STAMP`/`STPA` (`arXiv:2512.17600v2`, fév. 2026 `[7]`) sur les *unsafe control actions* et l'érosion des boucles (archétype à contrôleur unique dont l'extension multi-agents reste ouverte `[7]`), **blanchiment de frontière** `[1, 5, 7]`, et insuffisance des contrôles nominaux face aux attaques adaptatives multi-étapes `[3]`.
  - **Appui vérifié :** `SRC-058.txt` (`[7]`, L63–69, L412–431, L538–540, L1030–1049), `SRC-054.txt` (`[3]`, § 3.5, § 4.1.2), `SRC-055.txt` (`[1]`), `SRC-002.txt` (`[5]`), `registre/glossaire-termes.json` (`L303–309`).
  - **Passe initiale :** écart rectifié · **Action :** explicitée la borne d'archétype unique de `[7]` et la formulation exacte tirée de `[3]` · **Verdict : supporté**

- **C19-32 (`L103`)** — *Affirmation :* Matrice normative unique sur les quatre déplacements agentiques (`Tome 3 § 31.1`) croisant `ASI01`–`ASI10` `[1, 2]`, `MCP Top 10` (bêta) et `CSA MAESTRO` (`Tome 2 Tableau 37`, `Tome 3 § 31.8`), raccordée aux signaux `OTel`/`SIEM` et contrôles déterministes (`ADR-019`, `PRR S`, `→ Ch. 34`).
  - **Appui vérifié :** `Corpus/Tome 3` (`L16279–16284`, `L16496–16520`, `L17039–17065`), `Corpus/Tome 2` (`L4247–4293`), `SRC-055.txt` (`[1]`), `SRC-059.txt` (`[2]`).
  - **Passe initiale :** écart rectifié · **Action :** explicitée l'origine `Tome 2`/`Tome 3` des quatre déplacements et de `MAESTRO`/`MCP Top 10` · **Verdict : supporté**

- **C19-33 (`L105–L118`, Tableau 19.2)** — *Affirmation :* Le Tableau 19.2 relie les dix catégories `ASI01`–`ASI10` `[1, 2]` aux maillons `Q-A`..`Q-D`, aux couches `MAESTRO`, aux correspondances `MCP` (bêta) / `ATLAS` / `NIST` `[3]` et aux contrôles déterministes (`POR-003 < 10 s` vs `15 min` `Tome 2`).
  - **Appui vérifié :** `SRC-055.txt` (`[1]`), `SRC-059.txt` (`[2]`), `SRC-054.txt` (`[3]`), `SRC-057.txt` (`[4]`), `SRC-095.txt` (`[6]`), `SRC-058.txt` (`[7]`), `registre/matrice-exig-prr-c40.json` (`POR-003`, `L300`).
  - **Passe initiale :** écart rectifié · **Action :** alignées les citations du tableau sur les sources `L+` vs relevés `Tome 1/3` et mentionné l'écart `POR-003 < 10 s` / `15 min` `Tome 2` · **Verdict : supporté**

- **C19-34 (`L120–L122`, Figure 3)** — *Affirmation :* Le schéma `SCH-19-03.png` et sa légende unifient maillons `Q-A`..`Q-D`, matrice `ASI01–10`/`MAESTRO`, sceau de teinte `UNTRUSTED_EXTERNAL` contre `ASI06` et harnais `Red Team` `CI/CD`.
  - **Appui vérifié :** `specs/manifest.json` (`ch19`, `SCH-19-03`), `schemas/SCH-19-03.mmd`, `schemas/rendus/SCH-19-03.png`.
  - **Passe initiale :** écart rectifié · **Action :** légende harmonisée avec la distinction `G0` / cible `Tome 3` · **Verdict : supporté**

- **C19-35 (`L122`)** — *Affirmation :* Étiquetage `UNTRUSTED_EXTERNAL` hors du modèle distinguant le socle scellé `G0` (`policy_saga/taint_camel.py` avec `SessionTaintTracker` isolé par `tenant_id`, `record_tool_output` et `delegate_taint_envelope`, et `policies_opa/camel_taint.rego` sous `default allow := false` et `control_flow_source == "TRUSTED_PLAN"`, sans `HMAC` ni `Cedar` en `G0`) de la cible `Tome 3` hors `G0` (`§ 31.9`, `§ 31.11`, `§ 32.7` : sceau `HMAC` à la passerelle `PEP` `agentgateway` vérifié avant clause `Cedar` `forbid`) rejetant toute écriture sensible ou mémoire vers quarantaine (`← Ch. 11`) `[1, 5]`.
  - **Appui vérifié :** `taint_camel.py` (`L10–60`), `policies_opa/camel_taint.rego`, `Corpus/Tome 3` (`L16657`, `L17063`), `SRC-055.txt` (`[1]`), `SRC-002.txt` (`[5]`).
  - **Passe initiale :** écart rectifié · **Action :** distingués explicitement l'artefact `G0` exécutable (`SessionTaintTracker` / `OPA/Rego`) et la cible hors `G0` `HMAC`/`Cedar` du `Tome 3` (`post-G4`) · **Verdict : supporté**

- **C19-36 (`L126–L130`)** — *Affirmation :* Harnais `Red Team` `CI/CD` (`EXIG-SEC-24` `Tome 2 § 9.9`, `ADR-019` `Tome 3 § 31.13`, `PRR S-08` et `S-12`) mesurant `ASR_plan` et `ASR_action = 0,0 %` sur suites bilingues `FR`/`EN` ; en `G0` (`aq/rapports-g0.json`), `owasp_src055` (`13/13` fichiers à `100,0 %` via `test_owasp_src055_asi01_asi10_full_coverage`) valide la couverture `ASI01`–`ASI10` et l'invariance `FR`/`EN` sous `OPA/Rego` et `metamorphic.py` `[1, 3]`.
  - **Appui vérifié :** `aq/rapports-g0.json` (`L70–75`), `tests/test_third_party_vectors.py` (`L359–506`), `registre/matrice-exig-prr-c40.json` (`PRR S-08`, `PRR S-12`), `Corpus/Tome 2` (`L4676–4680`), `Corpus/Tome 3` (`L17065`), `SRC-055.txt` (`[1]`), `SRC-054.txt` (`[3]`).
  - **Passe initiale :** écart rectifié · **Action :** distinguées l'épreuve `G0` (`13/13` `owasp_src055`, `OPA` et `metamorphic.py`) et la cible `ASR_action = 0,0 %` (`ADR-019`), et corrigé le rattachement aux deux portes `PRR S-08` et `S-12` · **Verdict : supporté**

### Section 19.3 — Synthèse architecturale, livrables et portes de contrôle (`L134–L151`, Tableau 19.3, Trois invariants)

- **C19-37 (`L134–L136`)** — *Affirmation :* Articulation amont (`ch02`, `ch07`–`ch13`, `ch16`–`ch17`) et aval (`ch20`–`ch23`, `ch26`, `ch34`, `ch36`), et absence de bloc `CA-G0-SYNC` vérifiée (`owasp_src055` `13` fichiers et `mcp_pinning.py` `G0-EX-CH01-03` couverts en `G0` avec `ch07` et `ch20`).
  - **Appui vérifié :** `specs/manifest.json` (`ch19`), `aq/rapports-g0.json` (`L70–97`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé le sens des flèches amont/aval (`← Ch. 02`, `← Ch. 10`, `← Ch. 13`, `→ Ch. 22`, `→ Ch. 26`) · **Verdict : supporté**

- **C19-38 (`L138–L145`, Tableau 19.3)** — *Affirmation :* Le Tableau 19.3 récapitule les quatre livrables d'ingénierie (matrice `ASI01–10 × MCP01–10 × MAESTRO × Q-A..Q-D`, registre signé `MCP`/`Skills`, pipeline `SLM` + suivi de teinte, harnais `Red Team` `FR`/`EN`), leurs exigences (`EXIG-SEC-01..05`, `18..22`, `24`, `EXIG-MCP-20`, `CAP-038`, `ADR-008/010/019`, `PRR S-06/08/12`) et leurs critères `G0`–`G1`.
  - **Appui vérifié :** `matrice-exig-prr-c40.json`, `aq/rapports-g0.json`, `SRC-055/059/054/057/002/095`.
  - **Passe initiale :** écart rectifié · **Action :** harmonisés `owasp_src055 (13/13)`, l'admission attestée `[6]`, `OPA`/`Cedar` et `PRR S-08`/`S-12` · **Verdict : supporté**

- **C19-39 (`L147–L151`, Trois invariants)** — *Affirmation :* Les trois invariants exécutables du Chapitre 19 synthétisent : (1) la proscription du filtre probabiliste unique et le sas `SLM` typé (`EXIG-SEC-03/05`, `CAP-038`), (2) le scellement `SHA-256 JCS` continu des outils `MCP` et `Agent Skills` (`EXIG-MCP-20`, `EXIG-SEC-18..22`), et (3) la teinte anti-`ASI06` (`OPA`/`Cedar`, cible `HMAC`) et la porte `Red Team` `ASR_action = 0,0 %` (`EXIG-SEC-24`, `ADR-019`, `PRR S-08/S-12`).
  - **Appui vérifié :** cohérence complète de `§ 19.1`–`§ 19.3`, des sources `L+` `[1]`–`[7]` et de la barrière `G0`.
  - **Passe initiale :** écart rectifié · **Action :** intégrées dans les invariants 2 et 3 les réserves `Tome 3 § 13.3` et la dualité `OPA`/`Cedar` + `PRR S-08/S-12` · **Verdict : supporté**

- **C19-40 (`REV-04`, `PRD-L3-001/002/003`, `PRD-L4-002`)** — *Affirmation :* Ajout des repères secondaires PRD (`PRIN-07`, `F-25` détournement de refus multi-agents `Tome 3 § 31.1`, `OWASP API1–API3` `Tome 2`, `AIUC-1` `Tome 2`/`Tome 3`), uniformisation des légendes en `Figure 61`..`Figure 63`, et alignement des schémas `SCH-19-01.svg` (`EXIG-SEC-03` / `EXIG-SEC-05` + ordre `A`/`B`/`C`) et `SCH-19-03.mmd` (`FR/EN`, `EXIG-SEC-24`, distinction `OPA` `G0` vs cible `HMAC`/`Cedar`).
  - **Appui vérifié :** `Compendium/prd.md` (`L3612–3641`), `Corpus/Tome 2` (`§ 9.6`), `Corpus/Tome 3` (`§ 31.1`, `§ 31.8`), `schemas/SCH-19-01.svg`, `schemas/SCH-19-03.mmd`.
  - **Passe REV-04 :** intégré et vérifié · **Verdict : supporté**

- **C19-41 (`L31`, `L99`)** — *Affirmation :* La non-compositionnalité de la triade létale éclaire l'agentivité des systèmes comme propriété émergente de l'assemblage (outils, mémoire, délégations) activant *Excessive Agency* (`ASI01`–`ASI03` `[1, 5]`) ; Barrett et coll. (`[7]`, `SRC-058` `L953–966`) identifient l'agentivité (*agency*), la conscience de situation et les buts instrumentaux comme facteurs systémiques de perte de contrôle lorsque des données externes détournent les outils légitimes du mandataire confus (`ASI01`–`ASI03` `[1, 5, 7]`).
  - **Appui vérifié :** `SRC-055.txt` `[1]` (`ASI01`–`ASI03`, `Excessive Agency` `L237`, `L430`, `L485`, `L551`), `SRC-002.txt` `[5]` (`§ 3`), `SRC-058.txt` `[7]` (`L953–966`), `Chapitre 19.md` (`L31`, `L99`).
  - **Ajout concept agentivité des systèmes :** intégré et vérifié · **Verdict : supporté**
