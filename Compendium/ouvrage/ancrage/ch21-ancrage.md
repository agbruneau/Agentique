# Journal d'ancrage atomique Wyvern G2 — Chapitre 21 (`ch21`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/07 - Partie VII/Chapitre 21.md` (`4 110` mots de prose, plage `[3 552, 4 168]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch21-sources.md` (`[1]`–`[6]` en statut `L+`, `1` exclusion `statut F` sur `genai.owasp.org`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-{055,058,062,087,088,095}.txt` ; registres `Compendium/ouvrage/registre/*.json` ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json` et trousse `Tomes/Tome 8 - Ingénierie exécutable et homologation vérifiable/trousse/`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b3-8`
- **Passe G2 initiale (supportés)** : 10
- **Rectifications appliquées lors de la passe G2** : 26
- **Verdict final — supportés** : 36 / 36 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 21.md`

Toutes les formulations méritant réancrage ou gain de précision lors de la passe initiale ont été reformulées et réancrées directement dans [Chapitre 21.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/07%20-%20Partie%20VII/Chapitre%2021.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant la vedette propriétaire du glossaire (`analyse de contrôle STPA`), les `owned_concepts`, l'ensemble des renvois `[1]`–`[6]` et le calibrage (`4 110` mots dans `[3 552, 4 168]`, `0` erreur `G1 --strict`) :

1. **Séparation entre contrat exécutable `G0`, exigences `EXIG-*` et repérages hors `L+` (`L5`, `L13`–`L15`, `L25`–`L31`, `L39`–`L44`, `L94`, `L100`, `L108`) :** distinction explicite entre le contrat déclaratif vérifié en `G0` (`schemas/sandbox_manifest.schema.json`, `policy_saga/sandbox_manifest.py`, `policies_opa/sandbox_confinement.rego` avec `network.mode == "none"`, blocage `IMDS` + `11` plages `IANA`, `env_secrets == []`, `read_only_root == true`, `allow_shell == false`, délais `30 s` / `1 200 s` / `3 600 s`, règle `default allow := false` `[3]` et `opa test --coverage` à `100,0 %` sur `45` tests `[4]` + `18` tests dans `test_policy_saga.py`), l'arithmétique `Decimal` portée séparément par `policy_saga/decimal_money.py`, la porte statique `AST` anti-`eval` (`EXIG-SEC-17`, alignée sur `OWASP ASI05` `[1]`), et les technologies issues du repérage antérieur des tomes (`OpenSandbox`, `SHADI`, `Firecracker`/`Kata` cible `< 15 ms`, `gVisor`, `WASI 0.2`, `MCP-UI`, notation `defaultEgress: DENY_ALL`) non archivées en `L+` dans le socle du chapitre.
2. **Portée exacte de `SRC-095.txt` (`[5]`), `TEE`/`HYOK` et `TEE.fail` (`L17`, `L46`–`L50`, `L101`, `L109`) :** précision que l'admission attestée démontrée par Metere `[5]` porte sur les serveurs d'outils `MCP` et que son application aux mesures `PCR` des enclaves CPU/GPU relève d'une analogie architecturale ; qualification explicite de `Intel TDX`, `AMD SEV-SNP`, `NVIDIA Confidential Computing`, de la cible `RTT ≤ 35 ms` (`AWS XKS`) et de l'attaque `DDR5` `TEE.fail` (`< 1 000 \$ US` sur la page des auteurs au repérage `Tome 3 § 46.2`) comme éléments de repérage antérieur hors socle `L+`, tout en retirant le renvoi hors portée `[5]` des `11` plages `IANA` (`L39`).
3. **Qualification des références `SOC`/`SOAR`, `Borealis-Bench`, `STPA` (`[2]`) et `DORA` (`[6]`) (`L19`, `L58`–`L62`, `L71`–`L78`, `L86`, `L94`, `L102`, `L110`) :** distinction entre `ASI08`/`ASI10` (`[1]`) et `LLM10` (`OWASP LLM 2025` hors socle `L+`) ; qualification de `GTG-1002`, `F-21`, `F-57`, `AISPM`/`AIDR`, `CoSAI AI IR 1.0`, `MITRE ATLAS` 2026 et `NIST CAISI`/`NCCoE` comme éléments issus du repérage antérieur (`Tome 1`, hors socle `L+`) ; qualification de `0,050 ms` (`p50 = 50,00 µs`, `max = 0,050 ms` sur `10` essais concurrents, `10/10` compensations) comme mesure locale du banc expérimental interne `Borealis-Bench` (`Tome 3 § 24.5`, évaluation artificielle hors production bancaire) ; ajout de la limite explicite de `SRC-058.txt` `[2]` (exploration centrée sur un archétype simple, systèmes multi-agents complexes hors portée) et ancrage nominatif sur les articles `10`, `11`, `12` et `19` de `DORA` `[6]`.

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C21-01` à `C21-36`)

### Section introductive — Titre, question directrice et cadrage (`L1–L9`)

- **C21-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant le confinement physique du code généré et tiers (`SHADI`/microVM/`WASI`), la souveraineté matérielle `TEE`/`HYOK` et l'interruption rapide d'un agent déviant sans rompre l'intégrité des sagas en cours.
  - **Appui vérifié :** `Compendium/ouvrage/specs/manifest.json` (`ch21`, `D07`, `SUB_D07_03`, `owned_concepts`), `Compendium/ouvrage/registre/mindmap-complet.json`.
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C21-02 (`L5`)** — *Affirmation :* Un conteneur à noyau partagé (`runc`, proscrit par `EXIG-ARC-10`) expose une surface d'appels système où évasion de bac à sable, lecture de jeton ou requête vers `IMDS` (bloqué par `EXIG-SEC-13`) exposent l'hôte et les comptes adjacents (`OWASP ASI05` `[1]`), appelant confinement physique, confidentialité et bouclage `SOC`/`SOAR`.
  - **Appui vérifié :** `SRC-055.txt` (`L766–775` sur l'évasion de bac à sable et la compromission hôte/conteneur sous `ASI05`), `Corpus/Tome 2` (`EXIG-ARC-10` `L1206`, `EXIG-SEC-13` `L4536–4542`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement `runc` à `EXIG-ARC-10`, `IMDS` à `EXIG-SEC-13` et aligné la menace sur la formulation vérifiée de `SRC-055.txt` (`évasion de bac à sable`) · **Verdict : supporté**

- **C21-03 (`L7`)** — *Affirmation :* La défense physique concilie isolement et réaction rapide face à l'emballement ou aux attaques autonomes (`OWASP ASI08`, `ASI10` `[1]`) avec la préservation de la souveraineté, des traces forensiques et du canal de compensation isolé `Saga`.
  - **Appui vérifié :** `SRC-055.txt` (`L1072–1101` `ASI08: Cascading Failures`, `L1342–1370` `ASI10: Rogue Agents` et recommandation de `kill-switches`, quarantaine et journaux forensiques).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C21-04 (`L9`)** — *Affirmation :* Le chapitre clôt la Partie VII au `2 décembre 2026` sur la base fermée `[1]`–`[6]`, sous clause `non-avis` (`AO-05`) et exclusion `statut F` de `genai.owasp.org`, sans réécrire `rule_of_two.rego`/`camel_taint.rego` (`ch20`) ni le journal `Outbox` (`ch15`), et sans bloc de code clôturé.
  - **Appui vérifié :** `sources/ch21-sources.md` (`L1–79`), `recherche/registre-statut-f.json`, `SRC-055.txt` (`L13–15` clause non-avis juridique), `verifie_manuscrit.py` (`CA-21`, `CA-G0-SYNC`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

### Section 21.1 — Résumé exécutif (`L11–L19`)

- **C21-05 (`L13`)** — *Affirmation :* Exigence générale d'exécution en bac à sable éphémère à noyau isolé (`[1]`), concrétisée selon les choix techniques internes du traité (`ADR-020`) par microVM `Firecracker`/`Kata` (cible `< 15 ms` sur `/dev/kvm`), `gVisor` ou `WASI 0.2` sous `OpenSandbox` ou `SHADI` (`EXIG-ARC-10`, `EXIG-SEC-08..17`, `CAP-030`, `PRR S-11`), sans `runc` nu ni montage de socket Docker.
  - **Appui vérifié :** `SRC-055.txt` (`L503–504`, `L732–733`), `matrice-exig-prr-c40.json` (`CAP-030`), `Corpus/Tome 2` (`EXIG-ARC-10`, `EXIG-SEC-08..17`), `Corpus/Tome 3` (`L17328–17333`), `Corpus/Tome 6` (`L155`).
  - **Passe initiale :** écart rectifié · **Action :** en `G2`, qualifié `MCP-UI`, `OpenSandbox`, `SHADI`, `Firecracker`/`Kata`, `gVisor` et `WASI 0.2` hors socle `L+` et retiré `[3]` ; en recollation `G3` (`seed 20270902`), déplacé `[1]` sur l'exigence générale de bac à sable isolé de la phrase précédente et qualifié la pile technique de choix interne du traité (`ADR-020`) · **Verdict : supporté**

- **C21-06 (`L15`)** — *Affirmation :* En barrière `G0`, `sandbox_manifest.py` et `sandbox_confinement.rego` vérifient `network.mode == "none"` (noté `defaultEgress: DENY_ALL` sous `OpenSandbox`), le blocage d'`IMDS` (`169.254.169.254`) et des `11` plages `IANA`, `env_secrets == []`, `read_only_root == true`, `allow_shell == false` et les plafonds `30 s` / `1 200 s` / `3 600 s` sous `default allow := false` et `opa test --coverage` à `100,0 %` `[3, 4]`, complétés par `decimal_money.py` (`Decimal`) et la porte `EXIG-SEC-17` anti-`eval` (`ASI05` `[1]`).
  - **Appui vérifié :** `Tomes/Tome 8/.../policy_saga/sandbox_manifest.py` (`L12–147`), `policies_opa/sandbox_confinement.rego` (`L6–57`), `policy_saga/decimal_money.py`, `tests/test_policy_saga.py` (`L317–439`), `aq/rapports-g0.json` (`L31–37`), `SRC-087.txt` (`[3]`), `SRC-088.txt` (`[4]`), `SRC-055.txt` (`L787`, `L813` `[1]`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé la confusion entre `defaultEgress: DENY_ALL` et `network.mode == "none"`, dissocié `decimal_money.py` et `EXIG-SEC-17` anti-`eval` (`[1]`) du module `sandbox_manifest.py` et scindé en paragraphe conforme à `CA-05` · **Verdict : supporté**

- **C21-07 (`L17`)** — *Affirmation :* Pour les grappes partagées, la confidentialité matérielle combine enclaves `TEE` CPU/GPU (`Intel TDX`, `AMD SEV-SNP`, `NVIDIA Confidential Computing`) et séquestre `HYOK` (cible `RTT ≤ 35 ms` hors `L+`) pour le déchiquetage cryptographique (`CAP-033`, `PRI-011`, `DEC-006`), tout en excluant les secrets ultimes face au risque `DDR5` `TEE.fail` (`< 1 000 \$ US` hors `L+`) avec continuité bimodèle trimestrielle à poids ouverts (`CAP-031`, `POR-006`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`CAP-031`, `CAP-033`, `POR-006`), `Corpus/Tome 3` (`L23948–23991`), `Corpus/Tome 5` (`L1352`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement `RTT ≤ 35 ms` et `TEE.fail` (`< 1 000 \$ US`) comme éléments issus du repérage antérieur hors socle `L+` · **Verdict : supporté**

- **C21-08 (`L19`)** — *Affirmation :* Face à `GTG-1002` (hors `L+`), `ASI08`/`ASI10` (`[1]`) et `LLM10` (`2025` hors `L+`), la boucle `SOC`/`SOAR` (`AISPM`/`AIDR` et `CoSAI AI IR 1.0` hors `L+`) déploie un coupe-circuit à `4` paliers et `5` états (`EXIG-IAM-20`, `EXIG-SEC-23..26`, `CAP-039`, `PRR S-14`) `[2, 6]` visant `< 10 s` au `PEP` (`POR-003` ; `0,050 ms` max local `Borealis-Bench` C1), éviction `SSF`/`CAEP` `≤ 15 min` (`CAD26`), repli `N2`/`L0` `< 60 s` (`POR-015`) et préservation du canal `Saga` (`EXIG-ORC-28`) et des traces (`DORA` art. `10`–`11` `[6]`).
  - **Appui vérifié :** `SRC-055.txt` (`ASI08`, `ASI10`), `SRC-058.txt` (`STPA`), `SRC-062.txt` (`L1899–1965` art. `10`–`11`), `matrice-exig-prr-c40.json` (`CAP-039`, `POR-003`, `POR-015`), `Corpus/Tome 3` (`L12865`), `Corpus/Tome 1` (`L4797`, `L5888`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `GTG-1002`, `LLM10`, `AISPM`/`AIDR`, `CoSAI AI IR 1.0` comme hors socle `L+`, précisé le statut interne de `Borealis-Bench` (`0,050 ms` max) et ancré `DORA` sur les art. `10`–`11` · **Verdict : supporté**

### Section 21.2.1 — Confinement matériel et enclaves `TEE`/`HYOK` (`L23–L54`, Figure 1 et Figure 2)

- **C21-09 (`L25`)** — *Affirmation :* `OWASP ASI05` (`[1]`) vise l'exécution de logique contrôlée par l'attaquant menant à l'évasion de bac à sable ou à la compromission de l'hôte/conteneur ; dans un conteneur `runc`, le partage du noyau hôte expose le nœud, motivant la proscription sans dérogation de `runc` nu et du montage de sockets par `EXIG-ARC-10` (`CAP-030`, `PRR S-11`).
  - **Appui vérifié :** `SRC-055.txt` (`L762–779`), `Corpus/Tome 2` (`EXIG-ARC-10` `L1206`), `matrice-exig-prr-c40.json` (`CAP-030`, `S-11`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la description d'`ASI05` sur le texte exact de `SRC-055.txt` et explicité `EXIG-ARC-10` · **Verdict : supporté**

- **C21-10 (`L27–L31`)** — *Affirmation :* Sous `OpenSandbox` (`AAIF`, `ADR-020`) et `SHADI` (`AGNTCY`) issus du repérage antérieur hors `L+`, l'arbitrage gradue trois moteurs (`EXIG-SEC-08` à `11`, `Tome 2 § 9.7`, `Tome 3 § 32.6`) : `Firecracker`/`Kata` sur `/dev/kvm` (~`50 000` lignes Rust, `< 5` Mio 2020, `~25–45` Mo actif, `< 125 ms` froid, `< 15 ms` *WarmPool*, défaut réglementé pour Python/Bash/`Agent Skills`/`CUA`) ; `gVisor` (`runsc`, `~35–60` Mo, `200–500 ms`, `~97 %` Linux, repli sans `/dev/kvm` et bacs GPU sous analyse `EXIG-SEC-10` car `nvproxy` relaye les `ioctl` sans valider les tampons `DMA` vs `IOMMU`) ; et `WASI 0.2` (`wasm32-wasip2`, `1–5` Mo, `0,2–2 ms`, parseurs et transformations pures).
  - **Appui vérifié :** `Corpus/Tome 2` (`§ 9.7` `L4426–4508`, `L8023` `50 000` lignes Rust), `Corpus/Tome 3` (`§ 32.6` `L17323–17342`).
  - **Passe initiale :** écart rectifié · **Action :** intégrées les métriques comparatives `Firecracker`/`gVisor`/`WASI 0.2` et la limite GPU `nvproxy`/`DMA` (`post-G4`) · **Verdict : supporté**

- **C21-11 (`L31`)** — *Affirmation :* L'usage de `/dev/kvm` exige des nœuds métal nu ou virtualisation imbriquée (renvoi `ch09`), basculant vers `gVisor` ou `WASI 0.2` en l'absence de `KVM` sans relâcher les invariants vérifiés en `G0` par `schemas/sandbox_manifest.schema.json`, `sandbox_manifest.py` et `sandbox_confinement.rego` (`EXIG-SEC-08..17`, `default allow := false`, `opa test --coverage` `100,0 %` `[3, 4]`).
  - **Appui vérifié :** `Corpus/Tome 8` (`L986–992`), `sandbox_manifest.schema.json`, `sandbox_manifest.py`, `sandbox_confinement.rego`, `aq/rapports-g0.json` (`L31–37`), `SRC-087.txt` `[3]`, `SRC-088.txt` `[4]`.
  - **Passe initiale :** écart rectifié · **Action :** précisé la validation déclarative sans `/dev/kvm` en barrière `G0` et le lien exact à `[3, 4]` · **Verdict : supporté**

- **C21-12 (`L33–L35`)** — *Affirmation :* La Figure 1 (`SCH-21-01.svg`) illustre l'échelle proscrivant `runc` au profit de `WASI 0.2`, `gVisor` et `Firecracker` (`< 15 ms`), articulée sur les quatre verrous cumulatifs `OpenSandbox` / `SHADI`.
  - **Appui vérifié :** `specs/manifest.json` (`ch21`, `SCH-21-01`), `Compendium/ouvrage/schemas/SCH-21-01.svg` (`L1–87`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C21-13 (`L39`)** — *Affirmation :* Verrou 1 (`EXIG-SEC-12`–`13`, recommandations `OWASP` `[1]`) : en `G0`, `network.mode == "none"` et `allowlist == []` (`defaultEgress: DENY_ALL` sous `OpenSandbox`, ou liste nominative sans `*` sous `default allow := false` `[3]`) ; `sandbox_manifest.py` bloque `169.254.169.254`, `metadata.google.internal`, `localhost`, `ip6-localhost`, les `11` plages spéciales `IANA` (`6` IPv4 et `5` IPv6), `0.0.0.0/8` et `::/128`, tandis que `sandbox_confinement.rego` double ce contrôle sur `imds_blocked`, `special_iana_blocked`, `*` et les préfixes courants contre `SSRF` `[1, 3]`.
  - **Appui vérifié :** `sandbox_manifest.py` (`L12–82`, `L126–147`), `sandbox_confinement.rego` (`L6–19`, `L36–57`), `test_policy_saga.py` (`L325–383`), `SRC-055.txt` (`L503–504`, `L2315`), `SRC-087.txt` (`[3]`).
  - **Passe initiale :** écart rectifié · **Action :** rectifié la correspondance exacte entre `sandbox_manifest.py`, `sandbox_confinement.rego` et `OpenSandbox`, retiré le renvoi hors portée `[5]` et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C21-14 (`L42`)** — *Affirmation :* Verrou 2 (`EXIG-SEC-14`) : zéro secret en environnement (`env_secrets == []`) ou sur racine en lecture seule (`read_only_root == true`, vérifiés en `G0`) ni en mémoire invitée ; sans interface réseau routable, la microVM échange uniquement via `virtio-vsock` avec le mandataire hôte (*Credential Vault Proxy* / `agentgateway`), lequel coupe immédiatement les routes `vsock` sur révocation `OpenID SSF 1.0`/`CAEP 1.0` ou bascule `FORCED_OPEN`.
  - **Appui vérifié :** `sandbox_manifest.schema.json` (`L28–31`), `sandbox_confinement.rego` (`L13–15`), `test_policy_saga.py` (`L385–416`), `Corpus/Tome 2` (`EXIG-SEC-14` `L4548–4553`), `Corpus/Tome 3` (`§ 32.6` `L17328`).
  - **Passe initiale :** écart rectifié · **Action :** ajoutée la fermeture des routes `virtio-vsock` sur `SSF/CAEP` ou `FORCED_OPEN` (`post-G4`) · **Verdict : supporté**

- **C21-15 (`L41`)** — *Affirmation :* Verrou 3 (`EXIG-SEC-15`, `EXIG-SEC-10`) : délais par défaut du cadre normatif fixés à `30 s` par appel d'outil, `1 200 s` (`20 min`) par boucle et `3 600 s` (`60 min`) de vie totale, vérifiés par `sandbox_manifest.py` et `sandbox_confinement.rego` `[3, 4]`, complétés par l'isolation `IOMMU` sur `GPU`.
  - **Appui vérifié :** `sandbox_manifest.schema.json` (`L33–42`), `sandbox_confinement.rego` (`L21–34`), `test_policy_saga.py` (`L396–410`), `Corpus/Tome 2` (`EXIG-SEC-10` `L4508`, `EXIG-SEC-15` `L4560–4565`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié les durées comme valeurs par défaut du cadre normatif (`EXIG-SEC-15`) vérifiées en `G0` `[3, 4]`, rattaché `IOMMU` à `EXIG-SEC-10` et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C21-16 (`L42`)** — *Affirmation :* Verrou 4 (`EXIG-SEC-17`) : porte `AST` rejetant `eval`/`exec` en cohérence avec `OWASP ASI05` `[1]`, interdiction du shell libre en `G0` (`allow_shell == false` `[3, 4]`) et arithmétique décimale exacte via `policy_saga/decimal_money.py` (`Decimal`, rejetant `float` et `bool` par `TypeError`).
  - **Appui vérifié :** `SRC-055.txt` (`L787`, `L813`), `Corpus/Tome 2` (`EXIG-SEC-17` `L4582–4587`), `sandbox_confinement.rego` (`L16`), `decimal_money.py`, `test_policy_saga.py` (`L418–439`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié la porte statique `AST` (`EXIG-SEC-17`), le contrôle `G0` `allow_shell == false` et `decimal_money.py`, et scindé la phrase (`CA-05`) · **Verdict : supporté**

- **C21-17 (`L44`)** — *Affirmation :* L'isolation s'étend à l'interface `MCP-UI` (renvoi `ch08`, patron issu du repérage antérieur hors `L+`) via un cadre `iframe` sans `allow-same-origin` et une politique `CSP` `connect-src 'none'`, prolongeant le confinement contre `OWASP ASI05` `[1]`.
  - **Appui vérifié :** `Corpus/Tome 1` (`L12342`), `SRC-055.txt` (`ASI05`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `MCP-UI` comme patron issu du repérage antérieur hors socle `L+` prolongeant les principes de confinement d'`ASI05` `[1]` · **Verdict : supporté**

- **C21-18 (`L46`)** — *Affirmation :* La souveraineté d'inférence sur grappes partagées (`PRI-011`, `DEC-006`, `CAP-033`, renvoi `ch12`) combine enclaves `TEE` (`Intel TDX`, `AMD SEV-SNP`, `NVIDIA Confidential Computing`) et gestion de clés `HYOK` (issus du repérage `Tome 3 § 46.2–46.3`, hors socle `L+`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`CAP-033`, `PRI-011`, `DEC-006`), `Corpus/Tome 3` (`L23948–23991`).
  - **Passe initiale :** écart rectifié · **Action :** retiré le renvoi hors portée `[5]` de cette phrase générale et rattaché `TEE`/`HYOK` au repérage `Tome 3 § 46.2–46.3` hors `L+` · **Verdict : supporté**

- **C21-19 (`L48`)** — *Affirmation :* Le routeur géofencé vérifie l'attestation matérielle (`PCR`) — transposant par analogie architecturale l'admission attestée `MCP` démontrée par Metere `[5]` — avant de libérer la clé depuis un `HSM` hors nuage (cible indicative `RTT ≤ 35 ms` reprise d'`AWS XKS` hors `L+`), conférant un pouvoir de déchiquetage cryptographique instantané.
  - **Appui vérifié :** `SRC-095.txt` (`L110–127`, `L749–865` sur l'admission attestée `MCP` préalable), `Corpus/Tome 3` (`L23976–23985` `AWS XKS` `35 ms` et révocation irrécupérable).
  - **Passe initiale :** écart rectifié · **Action :** explicité que le mécanisme `PCR` transpose par analogie le principe de `[5]` (portant sur les serveurs `MCP`) et que `RTT ≤ 35 ms` provient du repérage `AWS XKS` hors `L+` · **Verdict : supporté**

- **C21-20 (`L50`)** — *Affirmation :* L'attaque `TEE.fail` décrite sur la page de ses auteurs au repérage antérieur (`Tome 3 § 46.2`, hors `L+`) sur bus `DDR5` (`< 1 000 \$ US`) interdit une confiance absolue dans les enclaves partagées ; l'option `CAP-033` reste conditionnelle sous veille (`SIG-016`) sans secrets ultimes, et les architectures de classe élevée exercent chaque trimestre la bascule bimodèle à poids ouverts (`CAP-031`, `POR-006`).
  - **Appui vérifié :** `Corpus/Tome 3` (`L23970`), `Corpus/Tome 5` (`L1352`), `matrice-exig-prr-c40.json` (`CAP-031`, `CAP-033`, `POR-006`, `SIG-016`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `TEE.fail` (`< 1 000 \$ US`) comme source de repérage hors `L+` décrite d'après ses auteurs · **Verdict : supporté**

- **C21-21 (`L52–L54`)** — *Affirmation :* La Figure 2 (`SCH-21-02.svg`) représente le séquestre `HYOK` (`RTT ≤ 35 ms`), les enclaves attestées (`TDX`, `SEV-SNP`, `NVIDIA CC`), la limite physique `DDR5` `TEE.fail` et la bascule trimestrielle vers une grappe souveraine à poids ouverts.
  - **Appui vérifié :** `specs/manifest.json` (`ch21`, `SCH-21-02`), `Compendium/ouvrage/schemas/SCH-21-02.puml` (`L1–89`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

### Section 21.2.2 — Défense `SOC`/`SOAR`, `STPA` et coupe-circuit (`L56–L88`, Tableau 21.1, Figure 3)

- **C21-22 (`L58`)** — *Affirmation :* L'organisation doit contrer les cascades d'erreurs et agents déviants (`OWASP ASI08`, `ASI10` `[1]`, ainsi que `LLM10` de l'édition 2025 hors `L+`) et les intrusions rapides documentées au repérage antérieur (`Tome 1`, hors `L+` : campagne `MCP` `GTG-1002` et incidents `OAuth` `F-21`).
  - **Appui vérifié :** `SRC-055.txt` (`L1072–1101`, `L1342–1370`), `Corpus/Tome 1` (`L3330–3341`, `L4797`, `L11757`), `Corpus/Tome 2` (`L4251`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié `ASI08`/`ASI10` (`[1]`) de `LLM10` (`2025`) et qualifié `GTG-1002` et `F-21` comme issus du repérage antérieur (`Tome 1`, hors `L+`) · **Verdict : supporté**

- **C21-23 (`L60`)** — *Affirmation :* L'instrumentation défensive réunit `AISPM`/`AIDR` et des cadres issus du repérage antérieur hors `L+` (`CoSAI AI IR 1.0`, `MITRE ATLAS` 2026, projet conceptuel `NIST CAISI`/`NCCoE`) ; chaque agent du `SOC` doit posséder une `NHI` parrainée par `SPIFFE` et `OPA`/`Cedar` (renvoi `ch16`) au lieu d'un compte humain `PIM`/`TAP` (lacune `F-57` relevée au `Tome 1`, hors `L+`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L4383`, `L4841`, `L4873`, `L5888`, `L9275`), `Corpus/Tome 5` (`L1051`, `L1183`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `AISPM`, `AIDR`, `CoSAI AI IR 1.0`, `MITRE ATLAS`, `NIST CAISI`/`NCCoE` et `F-57` comme issus du repérage antérieur hors socle `L+` · **Verdict : supporté**

- **C21-24 (`L62`)** — *Affirmation :* La conception des seuils s'appuie sur l'**analyse de contrôle STPA** (`STAMP`/`STPA` `[2]`, dont l'exploration porte sur un archétype simple en exploitation et place les systèmes multi-agents complexes hors de portée directe) en modélisant les boucles de rétroaction dégradées, ce qui répond aux articles `10` et `11` de `DORA` (`[6]`) sur la détection rapide des anomalies, les seuils multi-niveaux, l'endiguement sans retard et la continuité des fonctions critiques.
  - **Appui vérifié :** `SRC-058.txt` (`L23–69`, `L408–415`, `L539`, `L780–790`), `SRC-062.txt` (`L1899–1965` art. `10`–`11`), `glossaire-termes.json` (`L383–389`, vedette propriétaire `analyse de contrôle STPA`).
  - **Passe initiale :** écart rectifié · **Action :** explicité la limite de portée de `SRC-058.txt` `[2]` sur les multi-agents complexes et rattaché nommément les obligations `DORA` aux articles `10` et `11` de `SRC-062.txt` `[6]` · **Verdict : supporté**

- **C21-25 (`L64–L69`)** — *Affirmation :* `EXIG-IAM-20`, `EXIG-SEC-26` et `CAP-039` (`PRR S-14`, `ADR-011`, `ADR-013`) instaurent un coupe-circuit à cinq états (`CLOSED`, `HALF_OPEN`, `OPEN`, `DEGRADED`, `FORCED_OPEN`) et quatre paliers (tâche/saga, connecteur `MCP`, `ClusterSPIFFEID`, domaine/région).
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`CAP-039`, `S-14`), `Corpus/Tome 2` (`EXIG-IAM-20` `L3265`, `EXIG-SEC-26` `L371`), `Corpus/Tome 3` (`L15869`), `Corpus/Tome 5` (`L824`, `L1101`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C21-26 (`L71`)** — *Affirmation :* Le premier horizon cible la coupure locale `PEP` en `< 10 s` (`POR-003` ; `p50 = 50,00 µs`, `max = 0,050 ms` sur `10` essais concurrents en Campagne `1` du banc expérimental interne `Borealis-Bench`, bail cible `TTL ≤ 5 s`, en évaluation artificielle hors production bancaire), le second l'enveloppe globale `≤ 15 min` (`CAD26`) par `OpenID SSF/CAEP` (renvoi `ch17`) et `SPIFFE`, complété par le repli `POR-015` `< 60 s` vers `N2` ou `L0`.
  - **Appui vérifié :** `Corpus/Tome 3` (`L12863–12878`), `Corpus/Tome 5` (`L522`, `L824`, `L1101`), `matrice-exig-prr-c40.json` (`POR-003`, `POR-015`).
  - **Passe initiale :** écart rectifié · **Action :** précisé le statut expérimental interne de `Borealis-Bench` (`p50 = 50,00 µs`, `max = 0,050 ms`, évaluation artificielle hors production) et la qualification d'`agentgateway` comme exemple du repérage antérieur · **Verdict : supporté**

- **C21-27 (`L73–L80`, Tableau 21.1)** — *Affirmation :* Le Tableau 21.1 synthétise les quatre mécanismes (`PEP POR-003`, `SOAR SSF`/`CAEP` + `SPIRE`, `POR-015`, Sanctuaire `Saga` `EXIG-ORC-17`/`28` avec `10/10` compensations préservées en C1 `Borealis-Bench`), leurs déclencheurs et leurs effets.
  - **Appui vérifié :** `Corpus/Tome 3` (`L12865`), `matrice-exig-prr-c40.json` (`CAP-039`, `POR-003`, `POR-015`), `Corpus/Tome 2` (`EXIG-ORC-17`, `EXIG-ORC-28`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `GTG-1002` hors `L+`, précisé `0,050 ms max local` et ajouté la mesure vérifiée `10/10 en C1` sur le sanctuaire `Saga` · **Verdict : supporté**

- **C21-28 (`L82–L84`)** — *Affirmation :* La Figure 3 (`SCH-21-03.svg`) modélise la boucle `AISPM`/`AIDR` → `FORCED_OPEN` (`< 10 s` / `0,050 ms` local) → `SSF`/`CAEP` (`≤ 15 min`) → repli `N2`/`L0` (`< 60 s`) tout en maintenant ouvert le canal `Saga` `EXIG-ORC-28`.
  - **Appui vérifié :** `specs/manifest.json` (`ch21`, `SCH-21-03`), `Compendium/ouvrage/schemas/SCH-21-03.puml` (`L1–86`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C21-29 (`L86`)** — *Affirmation :* L'arrêt d'urgence de la voie avant ne doit jamais interrompre le canal de compensation isolé `Saga` (`EXIG-ORC-17`, `EXIG-ORC-28`, renvoi `ch15`) ; en gelant la progression avant `Temporal` sans détruire microVMs ni journaux, les compensations idempotentes s'achèvent et les preuves subsistent pour l'examen post-incident et la notification `DORA` (art. `11`–`12` et `19`, renvoi `ch26` `[6]`).
  - **Appui vérifié :** `SRC-062.txt` (`L1923–1943`, `L2057–2063` art. `11`–`12` et `19`), `Corpus/Tome 2` (`EXIG-ORC-17`, `EXIG-ORC-28`), `Corpus/Tome 5` (`L824`).
  - **Passe initiale :** écart rectifié · **Action :** ancré explicitement la conservation des traces et la notification sur les articles `11`, `12` et `19` de `DORA` (`SRC-062.txt` `[6]`) · **Verdict : supporté**

- **C21-30 (`L88`)** — *Affirmation :* `EXIG-SEC-23` impose des exercices trimestriels chronométrés validant `< 10 s` (`POR-003`), `< 60 s` (`POR-015`) et la bascule bimodèle (`POR-006`), complétés par un exercice annuel `Red Team`.
  - **Appui vérifié :** `Corpus/Tome 2` (`EXIG-SEC-23` `L4664`), `Corpus/Tome 5` (`L824`), `matrice-exig-prr-c40.json` (`CAP-031`, `CAP-039`, `POR-003`, `POR-006`, `POR-015`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

### Section 21.3 — Synthèse architecturale, livrables et invariants (`L90–L110`, Tableau 21.2)

- **C21-31 (`L92`)** — *Affirmation :* En amont, le chapitre consomme les artefacts de compilation et `Agent Skills` (`ch04`), les rendus `A2UI`/`MCP-UI` (`ch08`), `ClusterSPIFFEID` (`ch16`), l'automate `SSF 1.0`/`CAEP 1.0` (`ch17`), le canal `Saga` (`ch15`), `ASI05`/`ASI08`/`ASI10` (`ch19`) et la traduction `STPA` (`ch20`), dans le respect de `CA-21`.
  - **Appui vérifié :** `specs/manifest.json` (`owned_concepts` et découpage `ch01`–`ch36`), `verifie_manuscrit.py` (`CA-21`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C21-32 (`L94`)** — *Affirmation :* En aval, le dispositif protège les six substrats (`ch12`), isole `Event Mesh` et `MAST` (`ch13`, `ch14`), nourrit `EvalOps` `E2` (`ch23`), `FinOps` (`ch24`), les boucles SaaS (`ch29`), les incidents `DORA` art. `10`–`11` (`[6]`) / `Loi 25` (`ch26`) et `PRR` `S-11`/`S-14` (`ch34`, `ch36`) ; en `G0` (`rapports-g0.json`), `test_policy_saga.py` passe `18` tests `pytest` et `opa_check` atteint `100,0 %` sur `45` tests `OPA` via `opa test --coverage` `[3, 4]`.
  - **Appui vérifié :** `aq/rapports-g0.json` (`L31–46`), `SRC-062.txt` (`L1899–1965`), `SRC-087.txt` `[3]`, `SRC-088.txt` `[4]`.
  - **Passe initiale :** écart rectifié · **Action :** précisé les effectifs exacts de `rapports-g0.json` (`18` tests `pytest`, `45` tests `OPA` à `100,0 %`), ajouté `[3, 4]` et précisé `DORA` art. `10`–`11` `[6]` · **Verdict : supporté**

- **C21-33 (`L96`)** — *Affirmation :* La convergence des trois lignes de défense (`ch19`, `ch20`, `ch21`) confère une maîtrise vérifiable du rayon d'impact en intégration continue et en exploitation trimestrielle sans reposer sur une fiabilité morale du modèle.
  - **Appui vérifié :** `Chapitre 21.md` (`§ 21.1`–`§ 21.3`), `specs/manifest.json` (`D07`).
  - **Passe initiale :** Conforme · **Action :** aucune · **Verdict : supporté**

- **C21-34 (`L98–L104`, Tableau 21.2)** — *Affirmation :* Le Tableau 21.2 récapitule les trois livrables d'ingénierie du chapitre (`OpenSandbox`/`SHADI` & `CSP` `MCP-UI`, matrice `TEE`/`HYOK` & continuité bimodèle, guides `SOAR` & coupe-circuit à `4` paliers), leurs exigences (`C18`, `C29`, `PRR S-11`, `S-14`) et leurs critères `G0`–`G1` (`[1]`–`[6]`).
  - **Appui vérifié :** `sandbox_manifest.py`, `sandbox_confinement.rego`, `decimal_money.py`, `aq/rapports-g0.json`, `matrice-exig-prr-c40.json`, `SRC-055.txt` `[1]`, `SRC-058.txt` `[2]`, `SRC-087.txt` `[3]`, `SRC-088.txt` `[4]`, `SRC-095.txt` `[5]`, `SRC-062.txt` `[6]`.
  - **Passe initiale :** écart rectifié · **Action :** aligné le tableau sur les désignations `G0` (`mode: "none"`, `allow_shell == false`, `decimal_money.py`, `AST` `EXIG-SEC-17` `[1]`), la transposition de `[5]`, le statut hors `L+` de `RTT ≤ 35 ms`/`TEE.fail` et le banc interne `Borealis-Bench` · **Verdict : supporté**

- **C21-35 (`L108`)** — *Affirmation :* Invariant exécutable 1 (`EXIG-ARC-10`, `EXIG-SEC-08..17`, `CAP-030`) : exécution en microVM `Firecracker`/`Kata` (cible `< 15 ms`), `gVisor` ou `WASI 0.2` sans `runc` nu, sous `network.mode == "none"` (`DENY_ALL` `OpenSandbox`), blocage `IMDS` et `11` plages `IANA`, `env_secrets == []`, plafonds `30 s` / `1 200 s` / `3 600 s`, porte anti-`eval` (`EXIG-SEC-17`, `ASI05`) et arithmétique `Decimal`.
  - **Appui vérifié :** `sandbox_manifest.py`, `sandbox_confinement.rego`, `decimal_money.py`, `SRC-055.txt` (`ASI05`), `Corpus/Tome 2` (`EXIG-ARC-10`, `EXIG-SEC-08..17`).
  - **Passe initiale :** écart rectifié · **Action :** harmonisé sur `network.mode == "none"` (`DENY_ALL` `OpenSandbox`), cible `< 15 ms` et `EXIG-SEC-17`/`ASI05` · **Verdict : supporté**

- **C21-36 (`L109–L110`)** — *Affirmation :* Invariants exécutables 2 et 3 (`CAP-031/033`, `POR-006`, `EXIG-IAM-20`, `EXIG-ORC-28`, `POR-003`, `POR-015`) : clés `HYOK` exclusivement client (cible `RTT ≤ 35 ms` hors `L+`), secrets ultimes hors matériel vulnérable à `TEE.fail` (repérage hors `L+`), bascule trimestrielle à poids ouverts ; coupe-circuit à `5` états basculant sous cible `< 10 s` (`≤ 15 min` `SSF`/`CAEP`), repli `< 60 s` vers `N2`/`L0` et préservation du canal `Saga` et des traces forensiques.
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`CAP-031`, `CAP-033`, `CAP-039`, `POR-003`, `POR-006`, `POR-015`), `Corpus/Tome 2` (`EXIG-IAM-20`, `EXIG-ORC-28`), `Corpus/Tome 3` (`L23970`, `L23985`).
  - **Passe initiale :** écart rectifié · **Action :** explicité le statut de cible interne (`< 10 s`, `RTT ≤ 35 ms`) et le statut de repérage hors `L+` de `TEE.fail` · **Verdict : supporté**

- **C21-37 (`REV-04`, `PRD-L3-007/008`, `PRD-L4-002`)** — *Affirmation :* Restauration substantielle du 4e verrou obligatoire `EXIG-SEC-16` (journal d'exécution immuable tenu hors bac à sable en ajout seul `EXIG-OBS-13`, distinct des traces et de l'audit, `Tome 2 § 9.7` L4568–4576, `OWASP ASI05`/`ASI10` `[1]`) en prose, `Tableau 21.2`, Invariant 1 et 4e boîte de `SCH-21-01.svg` ; précision `IMDSv2` (`hop limit = 1`, `EXIG-SEC-13`), correction du renvoi `Loi 25 (→ Chapitres 25 et 26)`, nettoyage `\$` dans backticks, devise `$ US` / légende de `SCH-21-02.puml`, et numérotation `Figure 67`..`Figure 69`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L4568–4587`), `Compendium/prd.md` (`L3964`), `SRC-055.txt` (`ASI05`, `ASI10`), `schemas/SCH-21-01.svg`, `schemas/SCH-21-02.puml`.
  - **Passe REV-04 :** intégré et vérifié · **Verdict : supporté**
