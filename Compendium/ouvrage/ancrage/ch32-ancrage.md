# Journal d'ancrage atomique Wyvern G2 — Chapitre 32 (`ch32`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/11 - Partie XI/Chapitre 32.md` (`4 499` mots de prose selon `verifie_manuscrit`, `4 734` selon `parser_plan`, plage `[4 251, 4 989]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch32-sources.md` (`[1]`–`[8]` en statut `L+`, `3` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` (`SRC-012`, `SRC-016`, `SRC-050`, `SRC-053`, `SRC-055`, `SRC-060`, `SRC-063`, `SRC-065`, `SRC-066`, `SRC-068`, `SRC-071`, `SRC-075`, `SRC-109`, `SRC-127`) ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b5-3`
- **Passe G2 initiale (supportés)** : 26
- **Rectifications appliquées lors de la passe G2 :** 7
- **Verdict final — supportés :** 33 / 33 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 32.md`

Toutes les formulations divergentes, sur-affirmées ou issues de spécifications hors corpus `L+` fermé relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 32.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/11%20-%20Partie%20XI/Chapitre%2032.md), en préservant les `owned_concepts` (`gouvernance-duale-ae-as`, `modele-operationnel-hub-and-spoke`, `dix-theses-t1-t10-tome-5`, `gouvernance-raci-modele-en-etoile`, `regime-derogations-et-transition-cohorte`, `registre-agents-cycle-de-vie-et-attestations`, `pieges-gouvernance`, `responsabilite-litiges-commerce-agentique`), l'ensemble des renvois `[1]`–`[8]` et le calibrage (`4 499` / `4 734` mots dans `[4 251, 4 989]`) :

1. **Socle `CRE-IA-2026-01 v1.2` vs `CRE-IA-2027 v2.0` (`L17`) :** dissociation explicite entre les `305` exigences du socle `CRE-IA-2026-01 v1.2` (`registre/matrice-exig-prr-c40.json`) et leur prolongement `CRE-IA-2027 v2.0` (`Tome 5 § 2`), et découpage conforme à `CA-05`.
2. **Qualification exacte de la *Loi 25* et de l'`EU AI Act` (`L26`, `L67`) :** rattachement des articles `3.1` à `3.3` (fonction `RPRP`, gouvernance et `ÉFVP`) et de l'article `17` (`ÉFVP` préalable à toute communication de renseignements personnels à l'extérieur du Québec, et non obligation de résidence absolue) à la *Loi sur la protection des renseignements personnels dans le secteur privé* modifiée par la *Loi 25* (`SRC-063.txt` `[5]`) ; rattachement de la compétence, de la formation et de l'autorité des approbateurs à l'article `26`, paragraphe `2`, de l'`EU AI Act` (`SRC-060.txt` `[4]`) pour les systèmes à haut risque ; retrait de la référence au *Data Act* européen (`(UE) 2023/2854`, absent du corpus probant `L+` fermé selon `AO-01` / `AO-02`) au profit d'un renvoi direct à `EXIG-APP-14`.
3. **Nomenclature `BSIF E-23` vs grille `R1–R4` (`Tableau 32.1`, `Tableau 32.2`) :** séparation entre l'exigence de cote de risque proportionnée inscrite dans la ligne directrice `E-23` (`SRC-065.txt` `[1]`) et la grille interne `R1–R4` du traité (`registre/concordance-taxonomies.json`), afin d'éviter d'attribuer ce sigle au texte réglementaire.
4. **Ancrage empirique du *shadow AI* (`L79`, `Tableau 32.2`) :** réancrage de l'écart `70 %` d'usage personnel hebdomadaire (vs `8 %` d'usage significatif en exploitation) sur les `314` répondants du *Pouls des leaders d'entreprise* de décembre `2025` (Banque du Canada, juin `2026`, `SRC-016.txt`), et des données liées aux clients transmises à des plateformes tierces sur les entretiens auprès de `17` développeurs expérimentés (Dhanorkar *et al.*, juin `2026`, `SRC-075.txt`) ; qualification des recommandations du bulletin technologique du BSIF de juillet `2026` (`SRC-066.txt` `[2]`) comme « saines pratiques recommandées » plutôt qu'une « violation frontale ».
5. **Matrice `EXIG-GOV-CYCLE` (`Tableau 32.3`) :** dissociation entre la réévaluation sur changement significatif (`EXIG-GOV-12`) et le blocage de promotion sur échec `EvalOps E1–E2` (`EXIG-EVA-01`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C32-01` à `C32-32`)

### En-tête, problématique et hygiène probatoire (`L1`–`L7`)

- **C32-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant le contrat dual `AE ↔ AS`, le modèle en étoile à responsable unique `A`, le cycle de vie, les sept pièges internes et les zones d'ombre juridiques du commerce agentique.
  - **Appui vérifié :** `specs/manifest.json` (`ch32`, `D11`, `SUB_D11_02`), `registre/matrice-exig-prr-c40.json` (`CAP-047`–`CAP-052`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-02 (`L5`)** — *Affirmation :* Un programme de **Systèmes d'agentivité** s'érode par désalignement interne (uniformité d'homologation entre assistant consultatif et automate financier, contournement par outils non déclarés, saturation de la `2e` ligne et dilution entre filiales).
  - **Appui vérifié :** `Corpus/Tome 7` (`§ 11.1`, `L1609–1623`), `SRC-065.txt` (`[1]`, proportionnalité `C.2`–`C.3`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-03 (`L7`)** — *Affirmation :* Clause de non-avis (`AO-05`) arrêtée au `2 décembre 2026`, règle probatoire `AO-01` (`SHA-256`) et consignation en `Statut F` sans contournement d'`iso.org` (`HTTP 403` `ISO/IEC 42001`), `lautorite.qc.ca` (`HTTP 403` Cloudflare, avec date attendue AMF corroborée sous réserve via `AIBanks.ca` `[6]`) et `genai.owasp.org` (compensé par `CC BY-SA 4.0` dans `GenAI-Security-Corpus` `[7]`).
  - **Appui vérifié :** `recherche/registre-statut-f.json` (`L40–49`, `L62–71`, `L216–225`), `sources/ch32-sources.md` (`L99–103`), `SRC-071.txt` (`L271–275`), `SRC-055.txt` (`L1–18`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section `32.1.1` — Dix thèses `T1–T10`, six décisions conjointes et modèle `Hub-and-Spoke` (`L11`–`L22`)

- **C32-04 (`L13`)** — *Affirmation :* Une gouvernance exclusivement informatique échoue faute de légitimité d'affaires et de maîtrise budgétaire, tandis qu'une décentralisation intégrale fragmente les ontologies et contredit les attentes prudentielles d'inventaire unifié `[1, 2]` ; contrat croisé `AE ↔ AS` adossé à `10` thèses (`T1`–`T10`) et `6` décisions conjointes cosignées.
  - **Appui vérifié :** `SRC-065.txt` (`[1]`, `L209–231` inventaire d'entreprise), `SRC-066.txt` (`[2]`, `L13–28`, `L115`), `Corpus/Tome 3` (`ADR-025`, `L21923–21932`), `Corpus/Tome 5` (`§§ 1–3`, `L86–117`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-05 (`L15`–`L17`)** — *Affirmation :* Thèses `T1`–`T4` : `T1` (sobriété face à la loi de Lusser et la falaise de capacité), `T2` (`52` capacités et `305` exigences `CRE-IA-2026-01 v1.2` prolongées par `CRE-IA-2027 v2.0`, sans `SQL` direct `ADR-001`), `T3` (protocoles épinglés `MCP`, `A2A`, `CloudEvents` derrière `PEP`), `T4` (sémantique, `CoALA`, `EBCDIC`/`COMP-3`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`exig_cre_ia_v1_2` : `305`, `cap_52` : `52`), `Corpus/Tome 5` (`§ 2`, `L97–100`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié explicitement les `305` exigences `CRE-IA-2026-01 v1.2` de leur prolongement `CRE-IA-2027 v2.0` et ajusté le découpage `CA-05` · **Verdict : supporté**

- **C32-06 (`L18`)** — *Affirmation :* Thèses `T5`–`T10` : `T5` (`OO3`/`OO4` et sagas à canal dédié), `T6` (domaines, classes et autonomie sous `JCS`/`CIBA`), `T7` (`SPIFFE`, `RFC 8693`, `DPoP`, `CaMeL`, préparation `TLS` `47 jours` et `PQC`), `T8` (double couloir, `EvalOps E1–E3`, `CPO`), `T9` (preuve unique `Loi 25` `[5]`, `BSIF E-23` `[1]`, `EU AI Act` `[4]` sur `24` propositions sectorielles), `T10` (`3` lignes, usine séparée, clauses tiers, homologation unifiée).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`pex_24` : `24`), `SRC-063.txt` `[5]`, `SRC-065.txt` `[1]`, `SRC-060.txt` `[4]`, `Corpus/Tome 5` (`§ 2`, `L101–106`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-07 (`L20`)** — *Affirmation :* L'`AE` gouverne `52` capacités (`CAP-001`–`CAP-052`), `3` lignes, plafonds par domaine et classe, grille d'acquisition réversible et `15` portes `POR` sur `27` signaux `SIG` ; l'`AS` conçoit `SBB`, `PEP`, contexte compilé, `CoALA`, sagas, jetons, `CaMeL`, `PQC`, `OTel`/`JCS` et bancs `E1–E3` ; `6` décisions conjointes (`1` sobriété/topologie à `6` exploitation/`CPO`/`POR`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`cap_52` = `52`, `dapp_por_15` = `15`, `dapp_sig_27` = `27`), `Corpus/Tome 5` (`§ 1` & `§ 3`, `L92–93`, `L110–117`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-08 (`L22`)** — *Affirmation :* Modèle opérationnel en étoile (*Hub-and-Spoke*) à `3` lignes (`EXIG-ARC-19`, `EXIG-GOV-05`, `EXIG-GOV-06`, `ADR-025`) : moyeu central fournissant passerelles, bus, registre, catalogue, gabarits conformes par construction, `EvalOps`, `CPO` et coupe-circuit ; interdiction d'exploiter passerelle/registre/catalogue parallèle sans dérogation écrite (`EXIG-GOV-05`) ; rayons propriétaires des serveurs `MCP` de domaine et tandem `RH–IT`.
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 11.3`, `EXIG-GOV-05`, `EXIG-GOV-06`, `L5321–5380`), `Corpus/Tome 3` (`L21917`, `ADR-025`), `registre/matrice-exig-prr-c40.json` (`EXIG-ARC-19`, `CAP-050`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section `32.1.2` — Douze rôles, matrice `RACI` à `A` unique et séparation `Oracle` / `Bâtisseur` (`L24`–`L45`, Tableau 32.1, Figure 100)

- **C32-09 (`L26`)** — *Affirmation :* Douze rôles (`EXIG-GOV-01` à `06`, `PRIN-10`) : parrain métier, responsable technique, évaluation indépendante, plateforme, `FinOps`, `AE`, sécurité, risques/conformité (`2e` ligne), `RPRP` (art. `3.1`–`3.3` de la loi sur le secteur privé modifiée par la *Loi 25* `[5]`), comité d'architecture et des risques agentiques (`EXIG-GOV-02`), approbateurs humains (compétence, formation et autorité calquées sur l'art. `26(2)` de l'`EU AI Act` `[4]` pour le haut risque) et équipe de garde.
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 43`, `L5237–5254`), `SRC-063.txt` (`art. 103` insérant `3.1`–`3.3` dans `RLRQ, c. P-39.1`), `SRC-060.txt` (`art. 26(2)`).
  - **Passe initiale :** écart rectifié · **Action :** précisé l'insertion des articles `3.1`–`3.3` dans la loi sur le secteur privé modifiée par la *Loi 25* `[5]` et le périmètre haut risque de l'article `26(2)` `[4]`, avec scission en deux phrases conformes à `CA-05` · **Verdict : supporté**

- **C32-10 (`L28`)** — *Affirmation :* `EXIG-GOV-RACI` : rattachement de chaque agent et serveur `MCP` à une personne physique nommée comme parrain dans le `SIRH` avec suppléant et rétrogradation automatique d'autonomie sous `72 heures` sur vacance sans relève (`EXIG-GOV-01`, `ADR-025`) ; interdiction de cumul préparation/approbation (`EXIG-GOV-03`) et unique rôle `A` par activité (`EXIG-GOV-04`).
  - **Appui vérifié :** `Corpus/Tome 2` (`EXIG-GOV-01`, `EXIG-GOV-03`, `EXIG-GOV-04`, `L5256–5319`), `Corpus/Tome 3` (`ADR-025`, `L21931`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-11 (`L30`–`L37`, Tableau 32.1)** — *Affirmation :* Répartition `RACI` à `A` unique sur `3` lignes : `1re` ligne (parrain `SIRH` & RT sous `72 h`, plateforme/`CoE` avec blocage hors registre `EXIG-GOV-08`, `10` et usine séparée), `2e` ligne (classement `E-23`, palier, homologation, réattestation `6`/`12` mois, dérogations, arrêt anticipé ; validation `E-23` proportionnée à la cote de risque `[1]` et grille interne `R1–R4`, récusation `EXIG-GOV-02`, veto suspensif), `3e` ligne (audit indépendant, lecture seule et exercices de sortie `B-10` `[3]`).
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 44`, `Tableau 45`), `SRC-065.txt` (`[1]`, `C.2`–`C.3` cote de risque), `SRC-068.txt` (`[3]`, `§ 2.3.3` & `§ 2.3.5`), `registre/concordance-taxonomies.json` (`DISC-02`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié dans le `Tableau 32.1` la cote de risque proportionnée de `BSIF E-23` `[1]` et la nomenclature interne `(grille interne R1–R4)` · **Verdict : supporté**

- **C32-12 (`L39`)** — *Affirmation :* Usine logicielle interne (`EXIG-GOV-USINE`, `ADR-029`–`031`, en cohérence avec la séparation dev/prod prudentielle) : séparation matérielle des dépôts/droits entre agent `Oracle` (`AST`/`SCIP`) et agent `Bâtisseur`, porte d'analyse statique et revue humaine, cibles d'ingénierie synthétiques sans appui empirique statistique (`score de mutation ≥ 85 %` et `Shadow Mirroring` de `30 jours` à zéro écart décimal).
  - **Appui vérifié :** `Corpus/Tome 3` (`ADR-029`, `L25368–25388`), `Corpus/Tome 5` (`L1491–1493`, `L1542`), `SRC-065.txt` (`Principe 3.4` validation indépendante du développement), `SRC-066.txt` (`L63–75` validation et gestion des changements).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-13 (`L41`)** — *Affirmation :* Garde-fous d'usine : `DataOps` sous contrats `ODCS v3` et patron `Write-Audit-Publish` (`WAP`) avec quarantaine immédiate ; `SRE` en lecture seule sur journaux assainis, procédures pré-signées et zéro `shell` libre en production (`ADR-030`) ; distillation `LLM → SLM` sous sas de purge des `RP` validé par jetons témoins et cible de conception synthétique sans appui empirique `pass^5 ≥ 99 %`.
  - **Appui vérifié :** `Corpus/Tome 3` (`ADR-030` `L25727–25745`, `ADR-031` `L26026–26034`), `Corpus/Tome 5` (`L1494–1496`, `L1542`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-14 (`L43`–`L45`, Figure 100)** — *Affirmation :* La *Figure 100* (`SCH-32-01.svg`) illustre le moyeu central mutualisé (`EXIG-ARC-19`) et l'usine `Oracle ↔ Bâtisseur` (`Z1`), le contrat `AE ↔ AS` autour des `10` thèses et `6` décisions (`Z2`), et les rayons métiers avec parrain `SIRH` et `3` lignes de défense (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch32`, `SCH-32-01`), `schemas/SCH-32-01.puml` (`L61–86`), `schemas/rendus/SCH-32-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section `32.2.1` — Registre à sept états, six jalons, dérogations et cohorte transitoire (`L49`–`L71`, Figure 101)

- **C32-15 (`L51`)** — *Affirmation :* `EXIG-GOV-CYCLE` et registre unifié (`EXIG-GOV-07`–`14`) répondant à l'attente d'inventaire de `BSIF E-23` applicable le `1er mai 2027` `[1]` et à la surveillance des tiers `B-10` `[3]`, recensant `100 %` des agents (internes, `SaaS`, partenaires) et `100 %` des serveurs `MCP`.
  - **Appui vérifié :** `SRC-065.txt` (`L31` `Le 1 mai 2027`, `L209–231`), `SRC-068.txt` (`L199`), `Corpus/Tome 2` (`EXIG-GOV-07`, `L5384–5412`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-16 (`L53`)** — *Affirmation :* Sept états officiels (`proposé`, `en conception`, `en construction`, `pilote`, `production`, `suspendu`, `retiré`), six jalons ordonnés (`EXIG-GOV-11`) avec démarrage au niveau inférieur en pilote `N3`/`N4`, et verrou `EXIG-GOV-08` refusant tout justificatif prod hors `pilote`/`production` (pilote sur données réelles traité comme mise en production ; exception exclusive des compensations sur canal dédié).
  - **Appui vérifié :** `Corpus/Tome 2` (`L5392`, `EXIG-GOV-08` `L5414–5420`, `EXIG-GOV-11` `L5487–5502`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-17 (`L55`)** — *Affirmation :* `EXIG-GOV-12` énumère `11` déclencheurs (`15` cas) de réévaluation avant mise en service ; blocage promotion/bascule si `EvalOps E1` et `E2` échouent (`EXIG-EVA-01`) ; `EXIG-GOV-10` impose un rapprochement au moins mensuel (passerelles, IdP, `SaaS`, facturation) avec quarantaine (`suspendu`), révocation `OAuth` et arrêt propre (`EXIG-ARC-02`).
  - **Appui vérifié :** `Corpus/Tome 2` (`EXIG-EVA-01`, `EXIG-GOV-10` `L5430–5436`, `EXIG-GOV-12` `L5504–5510`), `Corpus/Tome 5` (`L1480`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-18 (`L57`)** — *Affirmation :* `EXIG-GOV-ATTEST` (`EXIG-GOV-09`, `13`, `14`) : réattestation `12` mois (`6` mois classe élevée), alerte `30` jours avant échéance, suspension administrative trimestrielle des orphelins (ou rôle `A` vacant `> 30` jours) ; retrait (`retiré`) sous préavis minimal `60` jours (sauf retrait anticipé d'urgence pour sécurité décidé par le comité), révocation, retrait catalogue, archivage/purge et preuve de révocation validée par la sécurité.
  - **Appui vérifié :** `Corpus/Tome 2` (`EXIG-GOV-09` `L5422–5428`, `EXIG-GOV-13` `L5516–5522`, `EXIG-GOV-14` `L5524–5530`, `Tableau 44` `L5302`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-19 (`L59`)** — *Affirmation :* `EXIG-GOV-DEROG` (`EXIG-GOV-15`–`17`) : demande écrite justifiée avec risque résiduel, mesures compensatoires et plan daté ; instruite par l'`AE` avec avis sécurité, conformité et `RPRP` ; tranchée par le comité pour `≤ 6` mois renouvelable `1` seule fois (`≤ 90` jours par délégation `AE` en classe faible, sans cumul avec l'instruction) ; alerte `30` jours et suspension automatique à l'échéance.
  - **Appui vérifié :** `Corpus/Tome 2` (`EXIG-GOV-15` `L5546–5552`, `EXIG-GOV-16` `L5554–5560`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-20 (`L61`–`L63`)** — *Affirmation :* Liste fermée de `10` interdictions absolues non dérogeables (`EXIG-GOV-17`) : `NX`, `P3` sans approbation hors bande, usurpation d'identité, relais de jeton reçu, absence de fiche complète/parrain (hors fiche minimale existant inventorié), dépassement plafond de classe, autonomie `> N2` sous règle d'or, violation Règle de deux sans retrait d'exfiltration, absence de journal d'audit, manquement légal ou réglementaire.
  - **Appui vérifié :** `Corpus/Tome 2` (`EXIG-GOV-17`, `L5562–5568`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-21 (`L65`)** — *Affirmation :* Régime transitoire de cohorte (`existant inventorié`, `EXIG-GOV-16`) : fiche minimale et parrain sous `5` jours ouvrables sous peine de désactivation, contournement transitoire de passerelle limité à `P0`/`P1` (lecture seule).
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 11.6 Régime transitoire`, `L5570`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-22 (`L67`)** — *Affirmation :* Catalogue des protocoles (`EXIG-GOV-18`–`20`) : `6` critères `Adopter`, révision trimestrielle ou extraordinaire sous `15` jours ouvrables, veille désignée incluant la gouvernance systémique des chaînes d'approvisionnement en IA générative `[8]` ; grille éliminatoire et `10` clauses `EXIG-APP-07`–`16` (`MCP`/`A2A`, non-entraînement, localisation et `ÉFVP` préalable hors Québec selon l'article `17` de la loi sur le secteur privé modifiée par la *Loi 25* `[5]`, audit `BSIF B-10` `[3]`, sortie assistée sans pénalité avec destruction attestée selon `EXIG-APP-14` et arrêt d'urgence direct).
  - **Appui vérifié :** `Corpus/Tome 2` (`EXIG-GOV-18`–`20` `L5580–5609`, `EXIG-APP-07`–`16` `L6375–6454`), `SRC-109.txt` (`[8]`, `L14–22`), `SRC-063.txt` (`[5]`, art. `111` remplaçant l'art. `17` de `RLRQ, c. P-39.1`), `SRC-068.txt` (`[3]`, `§ 2.3.3` & `§ 2.3.5`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé « résidence `Loi 25` `[5]` art. `17` » par la règle exacte de localisation et d'`ÉFVP` préalable hors Québec, et retiré la mention du *Data Act* européen (absent du corpus `L+` fermé selon `AO-01` / `AO-02`) au profit d'`EXIG-APP-14` · **Verdict : supporté**

- **C32-23 (`L69`–`L71`, Figure 101)** — *Affirmation :* La *Figure 101* (`SCH-32-02.png`) illustre la progression sur le registre à `7` états et `6` jalons bloquée par `EvalOps E1–E2` (`Z1`), le filet mensuel anti-fantômes (`Z2`) et le sas des dérogations `≤ 6` mois face aux `10` lignes rouges d'`EXIG-GOV-17` (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch32`, `SCH-32-02`), `schemas/SCH-32-02.mmd` (`L1–23`), `schemas/rendus/SCH-32-02.png`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section `32.2.2` — Sept pièges endogènes et angle mort des litiges `AP2` (`L73`–`L108`, Tableau 32.2, Figure 102)

- **C32-24 (`L75`, `L77`)** — *Affirmation :* Sept modes d'échec endogènes (`M-26` / `T7 ch. 11`, `EXIG-GOV-PIEGES`) ; piège `1` (sur-ingénierie initiale) contredisant les principes `2.2` et `2.3` de proportionnalité de la ligne directrice `E-23` du BSIF `[1]`.
  - **Appui vérifié :** `Corpus/Tome 7` (`§ 11.1`, `Tableau 11.2`, `L1609–1613`, `L1694–1706`), `SRC-065.txt` (`[1]`, Principes `2.2` et `2.3`, `L233–283`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-25 (`L79`)** — *Affirmation :* Piège `2` (*shadow AI*) : sur `314` répondants du *Pouls des leaders d'entreprise* de décembre `2025` (Banque du Canada, juin `2026`), `70 %` utilisent personnellement l'IA chaque semaine au travail contre `8 %` d'usage significatif en exploitation ; des entretiens auprès de `17` développeurs expérimentés (Dhanorkar *et al.*, juin `2026`) montrent une incertitude sur le devenir de données liées aux clients transmises à des plateformes tierces, à l'encontre des saines pratiques recommandées au bulletin technologique du BSIF de juillet `2026` `[2]` ; parade par couloir rapide en lecture seule (`R1` / `L0–L1` via `Golden Paths`) et blocage hors passerelle `PEP`.
  - **Appui vérifié :** `SRC-016.txt` (`L39`, `L90`, `L94` `70% of respondents`, `L158–159` `8% of businesses surveyed reporting significant use`), `SRC-075.txt` (`17 experienced developers`, `customer-related data ... transmitted to third-party platforms`), `SRC-066.txt` (`[2]`, `L43` `prohibit sensitive data use in public or unapproved AI tools`, `L131` `sound practices`), `registre/concordance-taxonomies.json` (`DISC-02`).
  - **Passe initiale :** écart rectifié · **Action :** réancré exactement sur `SRC-016.txt` (`314` répondants, usage significatif en exploitation) et `SRC-075.txt` (`17` développeurs, données liées aux clients), qualifié `[2]` de « saines pratiques recommandées », scindé la phrase selon `CA-05` et aligné `Classe 1` → `R1` / `L0–L1` sous `DISC-02` (lissage G5) · **Verdict : supporté**

- **C32-26 (`L81`)** — *Affirmation :* Piège `3` (engorgement de la `2e` ligne avant le `1er mai 2027` pour `BSIF E-23` `[1]`, coïncidant avec l'échéance attendue de l'AMF rapportée sous réserve par `AIBanks.ca` `[6]`) ; piège `4` (dilution intra-groupe entre filiales, nécessitant par `B-10` `[3]` un propriétaire métier nominatif par entité juridique, inventaire `E-23` désagrégé et consentement inter-filiales).
  - **Appui vérifié :** `SRC-065.txt` (`[1]`, `L31`), `SRC-071.txt` (`[6]`, `L271–275`), `SRC-068.txt` (`[3]`, `L117`, `L315` `business functions/units and legal entities`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-27 (`L83`)** — *Affirmation :* Piège `5` (veille décorative et confiance excessive envers les évaluations des vendeurs `[2]`, arbitrage budgétaire `≤ 30` jours sur `27` signaux `SIG` audité annuellement par la `3e` ligne) ; piège `6` (choc tarifaire `FinOps`, pilotage `CPO` et bascule bimodèle annuelle `CAP-031`, `POR-016`) ; piège `7` (collision cryptographique `TLS` `100` puis `47` jours vs signatures `ML-DSA` en erreur `HTTP 431`, `ACME` et référence `kid` `JWKS` en `POR-007`).
  - **Appui vérifié :** `SRC-066.txt` (`[2]`, `L13` `over-reliance on vendor-provided assessments`), `registre/matrice-exig-prr-c40.json` (`CAP-031`, `POR-007`, `POR-016`, `dapp_sig_27`), `SRC-053.txt` (`100`/`47 days`), `SRC-012.txt` & `SRC-050.txt` (`ML-DSA`, `HTTP 431`), `SRC-127.txt` (`ACME`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-28 (`L85`–`L95`, Tableau 32.2)** — *Affirmation :* Le *Tableau 32.2* synthétise les `7` pièges endogènes (`M-26` / `T7 ch. 11`), symptômes (`70 %` personnel hebdomadaire vs `8 %` en exploitation), conséquences (contournement `ÉFVP` `Loi 25` `[5]` et écart aux pratiques `BSIF` `[2]`) et disjoncteurs (couloir `R1` (`L0–L1`), blocage `PEP`, scan mensuel `EXIG-GOV-10`, tri proportionnel par cote `E-23` `[1]` et grille interne `R1–R4`, titulaire `SIRH` par entité + `B-10` `[3]`, arbitrage `SIG ≤ 30 j`, revue valeur `2` mois `EXIG-FIN-10` + `CAP-031`, `ACME` + `kid` `JWKS` en `POR-007`).
  - **Appui vérifié :** `SRC-016.txt`, `SRC-063.txt` `[5]`, `SRC-065.txt` `[1]`, `SRC-066.txt` `[2]`, `SRC-068.txt` `[3]`, `SRC-071.txt` `[6]`, `Corpus/Tome 2` (`EXIG-FIN-10` `L5203` deux mois de suite), `Corpus/Tome 7` (`Tableau 11.2`), `registre/concordance-taxonomies.json` (`DISC-02`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la ligne `2` (`70 %` vs `8 %` en exploitation, écart aux pratiques `[2]`), la ligne `3` (tri par cote `E-23` `[1]` distinct de la grille interne `R1–R4`) et nettoyé `Classe 1` → `R1` (`L0–L1`) (lissage G5) · **Verdict : supporté**

- **C32-29 (`L97`–`L103`, Figure 102)** — *Affirmation :* Limite juridique des litiges `AP2` sans présence humaine (`Tome 1 § 10.4`) : un mandat signé prouve l'émission d'un consentement cryptographique, mais ni son caractère éclairé ni l'intégrité du raisonnement face à `OWASP ASI01`–`ASI10` `[7]` ; ni `AP2` ni l'`EU AI Act` `[4]` n'instituent de mécanisme propre de contestation automatisée, laissant `3` impasses ouvertes au degré `3` d'absence de documentation au `2 décembre 2026` (commerçant de référence, impayé contesté sans présence humaine, admissibilité probatoire de la non-répudiation machine multi-sauts) ; `SCH-32-03.svg` (*Figure 102*).
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 10.4`, `L2834–2862`), `SRC-055.txt` (`[7]`, `ASI01`–`ASI10`), `SRC-060.txt` (`[4]`), `schemas/rendus/SCH-32-03.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C32-30 (`L105`–`L108`)** — *Affirmation :* Encadré des trois invariants exécutables du Chapitre 32 : (1) unique `A` nominatif `SIRH` (`≤ 72 h`), zéro auto-homologation (`EXIG-GOV-03`, `04`), scission `Oracle`/`Bâtisseur` sans `shell` `SRE` ; (2) registre à `7` états bloquant tout jeton hors `pilote`/`production` (`EXIG-GOV-08`), scan mensuel (`10`), réattestation `6`/`12` mois (`13`), plafond `6` mois et `10` interdits `EXIG-GOV-17` ; (3) couloir rapide `R1` (`L0–L1`), arbitrage `SIG ≤ 30 j` et bornage contractuel `AP2` au degré `3`.
  - **Appui vérifié :** `Corpus/Tome 2` (`EXIG-GOV-03`, `04`, `08`, `10`, `13`, `15`–`17`), `Corpus/Tome 3` (`ADR-025`, `ADR-029`, `ADR-030`), `Corpus/Tome 1` (`§ 10.4`), `registre/concordance-taxonomies.json` (`DISC-02`).
  - **Passe initiale :** conforme · **Action :** aligné `Classe 1` → `R1` (`L0–L1`) sous `DISC-02` (lissage G5) · **Verdict : supporté**

### Section `32.3` — Synthèse opératoire, exigences `EXIG-GOV` et frontières d'architecture (`L110`–`L137`, Tableau 32.3)

- **C32-31 (`L112`–`L123`, Tableau 32.3)** — *Affirmation :* Six exigences directrices (`EXIG-GOV-RACI`, `CYCLE`, `ATTEST`, `DEROG`, `PIEGES` avec couloir rapide `R1` (`L0–L1`), `USINE`) en cohérence avec `EXIG-GOV-01`–`20` et `EXIG-APP-07`–`17`, récapitulant prescriptions normatives et artefacts probatoires (dont la distinction entre réévaluation `EXIG-GOV-12` et blocage `E1–E2` `EXIG-EVA-01`).
  - **Appui vérifié :** `Corpus/Tome 2` (`§§ 11.1–11.7`, `§ 13.3`, `EXIG-EVA-01`), `SRC-065.txt` `[1]`, `SRC-068.txt` `[3]`, `registre/concordance-taxonomies.json` (`DISC-02`).
  - **Passe initiale :** écart rectifié · **Action :** clarifié dans `EXIG-GOV-CYCLE` la séparation entre `réévaluation (12)` et `blocage E1–E2 (EXIG-EVA-01)`, et aligné `Classe 1` → `R1` (`L0–L1`) (lissage G5) · **Verdict : supporté**

- **C32-32 (`L129`–`L137`)** — *Affirmation :* Frontières de non-redite (`→` / `←`) avec les chapitres `04`, `06`, `09`, `13`, `23`, `24`, `25`, `26`, `30`, `31`, `33` et `34` ; cinq livrables concrets (incluant la procédure de couloir rapide `R1` (`L0–L1`)) et transition vers le Chapitre 33 (`→ Chapitre 33`).
  - **Appui vérifié :** `specs/manifest.json` (`ch04`, `ch06`, `ch09`, `ch13`, `ch23`, `ch24`, `ch25`, `ch26`, `ch30`, `ch31`, `ch32`, `ch33`, `ch34`), `verifie_manuscrit.py` (`CA-21`), `registre/concordance-taxonomies.json` (`DISC-02`).
  - **Passe initiale :** conforme · **Action :** aligné `Classe 1` → `R1` (`L0–L1`) et renvoi `(→ Chapitre 33)` (lissage G5) · **Verdict : supporté**

- **C32-33 (`L112`–`L116`, § 32.3 — ajout post-G4)** — *Affirmation :* Grille interne à quatre échelons (`R1` à `R4` : `R1 Minimal` `L0–L1` lecture interne sans `SoR` ni `RP` revue annuelle, `R2 Modéré` `L1–L2` revue ciblée `2LoD` semestrielle, `R3 Élevé` `L2–L3` contrôle indépendant `2LoD`/homologation/`ÉFVP`/audit `3LoD`, `R4 Critique` `L3–L4` comité exécutif/`RPRP`/bascule `L0`/retrait éprouvé), explicitement distincte des cotes propres à `BSIF E-23` `[1]`.
  - **Appui vérifié :** `Corpus/Tome 6` (`§ 12` `L3775–3778`), `registre/concordance-taxonomies.json` (`DISC-02`), `SRC-065.txt` (`[1]`).
  - **Passe initiale :** ajout post-G4 · **Action :** vérification différentielle `G2` · **Verdict : supporté**
