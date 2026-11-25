# Journal d'ancrage atomique Wyvern G2 — Chapitre 14 (`ch14`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/05 - Partie V/Chapitre 14.md` (`3 628` mots de prose, plage `[3 377, 3 963]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch14-sources.md` (`[1]`–`[7]` en statut `L+`, `2` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b3-1`
- **Passe G2 initiale (supportés)** : 9
- **Rectifications appliquées lors de la passe G2 :** 22
- **Verdict final — supportés :** 32 / 32 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 14.md`

Toutes les formulations divergentes, sur-affirmées ou issues de spécifications hors corpus `L+` fermé relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 14.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/05%20-%20Partie%20V/Chapitre%2014.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant les `owned_concepts` (`choregraphie-event-mesh`, `pathologies-reactives-backpressure`, `pont-ia-physique-ros2-simplex`), l'ensemble des renvois `[1]`–`[7]` et le calibrage (`3 628` mots dans `[3 377, 3 963]`) :

1. **Enveloppe `CloudEvents v1.0.2`, extensions et `OPA`/`Rego` (`L9`, `L21`, `L23`, `Tableau 14.1`, `L109`, `L113`) :** séparation stricte entre les quatre attributs `REQUIRED` de `CloudEvents v1.0.2` (`id`, `source`, `specversion` `"1.0"`, `type`, `SRC-035.txt` `[1]`) et les ajouts imposés par `EXIG-EVT-02` (version dans `type`, `time`, `datacontenttype`, `dataschema`) ; qualification du plafond `64 Ko` (`64 KByte` garantis en relais par `[1]`) et des extensions ultérieures figées au catalogue (`Auth Context`, `Data Classification`, `Expiry Time`) ; rattachement de `default allow := false` à `[5]` (`SRC-087.txt`) et du seuil `100,0 %` (`45/45` tests) à `opa test --coverage` `[6]` (`SRC-088.txt`) vérifié en barrière `G0` (`aq/rapports-g0.json`).
2. **Traçabilité `OTel GenAI` et `traceparent` (`L9`, `L25`, `Tableau 14.1`) :** dissociation entre les conventions de spans `OpenTelemetry GenAI` (`create_agent`, `invoke_agent`, `execute_tool`, statut `Development` dans `SRC-037.txt` `[7]`, qui ne mentionne ni `traceparent` ni `span link`) et l'exigence architecturale `EXIG-EVT-04` (`Tome 2 § 6.7`) imposant l'injection `traceparent` `W3C` et les liens causaux entre producteur et abonnés parallèles.
3. **Courtiers d'écosystème, `Kafka 4.0–4.4.0` et déduplication (`L7`, `L19`, `L43`, `L47`, `Tableau 14.2`, `L62`, `L114`) :** remplacement de l'appellation inexacte `IBM MQ 9.4 PQC` par `IBM MQ 9.4 LTS` avec `TLS 1.3` post-quantique `ML-KEM` sur `AMQP 1.0` (`ISO/IEC 19464`) en tant qu'exemple d'écosystème indexé au cadre (`Tome 1`) ; rattachement d'`Apache Kafka` (`4.0` sans `ZooKeeper`, `4.2.0` files coopératives, `4.4.0` files de lettres mortes) au cas de référence indexé au `Tome 2 § 6.7` ; ancrage direct de la déduplication `(source, id)` sur `SRC-035.txt` `[1]` ; attribution de `MAST` au chapitre 13 et alignement de la terminologie `STPA` sur `SRC-058.txt` `[4]` et `ASI08`/`ASI10` sur `SRC-055.txt` `[2]`.
4. **Passerelle IA physique `ADR-028`, normes `statut F` et `TUF`/`Sigstore` (`L11`, `L66`–`L70`, `L85`–`L95`, `L105`, `L115`) :** qualification explicite de la passerelle `MCP ↔ ROS 2/DDS`, des cadences (`0,5–5 s`, `10–30 ms`, `≤ 5 ms`, `≤ 1 ms`), du registre `Cedar`, des distributions `Jazzy`/`Kilted`, de la transposition `Simplex` (principe de Sha sur `MCU Safety PLC`), des lots `OCI`/`TUF`/`Sigstore` (distinction entre rôles hors ligne `root`/`targets`/`snapshot` et rôle en ligne `timestamp`), de la sonde `30 s` et des bornes hors ligne (`24 h`, `72 h`) comme cibles et choix de conception `ADR-028` (`Tome 3 § 46.6–46.8, § 46.15–46.16`, hors corpus `L+` fermé) ; retrait de la mention d'alignement direct sur `IEC 61508`, `ISO 10218-1:2025` et `ISO 3691-4` au profit d'une formulation préparatoire précisant que ces normes payantes relèvent du `statut F` hors preuve `L+` (`AO-01`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C14-01` à `C14-31`)

### Section 14.1 — Titre, question directrice et résumé (`L1–L11`)

- **C14-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant la chorégraphie événementielle `CloudEvents`/`AsyncAPI`, la prévention des tempêtes et messages poisons, et le découplage `LOTO`/`Simplex` vers l'IA physique.
  - **Appui vérifié :** `specs/manifest.json` (`ch14`, `D05`, `SUB_D05_02`), `registre/matrice-exig-prr-c40.json` (`CAP-011`, `CAP-012`, `ADR-028`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C14-02 (`L7`)** — *Affirmation :* La chorégraphie `Event Mesh` complète l'orchestration dirigée sans céder le contrôle transactionnel (`DEC-005`, `CAP-011`, `EXIG-EVT-01`), sur des courtiers d'écosystème indexés au cadre (`Apache Kafka`, `Solace PubSub+`, `NATS JetStream`, `IBM MQ 9.4 LTS` avec `TLS 1.3` `ML-KEM` sur `AMQP 1.0`).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`DEC-005`, `CAP-011`, `EXIG-EVT-01`), `Corpus/Tome 1` (`L10363`), `Corpus/Tome 3` (`L11053–11070`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé `IBM MQ 9.4 PQC` par `IBM MQ 9.4 LTS` avec `TLS 1.3` post-quantique `ML-KEM` et qualifié les courtiers d'exemples d'écosystème indexés · **Verdict : supporté**

- **C14-03 (`L9`)** — *Affirmation :* Conformité des événements à `CloudEvents v1.0.2` (plafond d'acheminement `64 Ko` `[1]` repris sous `EXIG-EVT-02`) et `AsyncAPI 3.x` (`EXIG-EVT-03`), zéro PII en attributs (`EXIG-EVT-05`), `traceparent` `W3C` et spans `OpenTelemetry GenAI` (`[7]`), `PEP` `OPA`/`Rego` (`default allow := false` et `100 %` exigé en `G0` `[5, 6]`), et compteur `xagenthopcount` plafonné à `xagentmaxhops = 4` (`EXIG-EVT-06`, `07`).
  - **Appui vérifié :** `SRC-035.txt` (`L510–514`), `SRC-087.txt` (`L2072–2113`), `SRC-088.txt` (`L625–699`), `SRC-037.txt` (`L43`, `L188`, `L668`), `aq/rapports-g0.json` (`L31–37`), `Corpus/Tome 2` (`L2415–2509`).
  - **Passe initiale :** écart rectifié · **Action :** distingué le plafond de relais `[1]` de la borne `EXIG-EVT-02`, généralisé `AsyncAPI 3.x`, rattaché `100 %` à `G0` et scindé en deux phrases conformes à `CA-05` · **Verdict : supporté**

- **C14-04 (`L11`)** — *Affirmation :* Sous `STAMP/STPA` `[4]`, `MAST` (`ch13`) et `OWASP ASI08`/`ASI10` `[2, 3]`, l'architecture couple `Transactional Outbox` + `CDC` à la déduplication `(source, id)` (`[1]`, `EXIG-EVT-08`), `DLQ` non bloquante, rétro-pression `TPM`, repli `FORCED_OPEN` vers `L0`, et passerelle cible `ADR-028` (`MCP ↔ ROS 2/DDS`, `0,5–5 s` vs `10–30 ms`, `LOTO`, `Simplex` `≤ 1 ms`, `TUF`/`Sigstore`).
  - **Appui vérifié :** `SRC-058.txt` (`[4]`), `SRC-055.txt` (`[2]`), `SRC-059.txt` (`[3]`), `SRC-035.txt` (`L251–254`), `registre/matrice-exig-prr-c40.json` (`ADR-028`), `Corpus/Tome 3` (`L24659–24725`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché `MAST` au chapitre 13, ancré `(source, id)` sur `[1]`, qualifié passerelle et arbitre de cibles `ADR-028` et scindé selon `CA-05` · **Verdict : supporté**

### Section 14.2.1 — Dorsale `Event Mesh`, pathologies réactives et régulateurs (`L15–L62`, Tableaux 14.1–14.2, Figures 1–2)

- **C14-05 (`L17`)** — *Affirmation :* Réserve du bus événementiel à trois besoins démontrés (`DEC-005`, `EXIG-EVT-01`, `CAP-011`) — découplage temporel, réactivité multi-domaines et rejeu ordonné — dans un patron hybride macro-orchestré entre domaines et chorégraphié localement.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`DEC-005`, `CAP-011`, `EXIG-EVT-01`), `Corpus/Tome 2` (`L2397–2407`), `Corpus/Tome 3` (`L11376–11385`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C14-06 (`L19`)** — *Affirmation :* Levée d'homonymie *Agent Mesh* (`Event Mesh` incluant `Kafka`, `Solace PubSub+`, `NATS JetStream` ou `IBM MQ 9.4 LTS` avec `TLS 1.3` post-quantique sur `AMQP 1.0` `ISO/IEC 19464` en exemples du cadre, maillage `MCP`/`A2A`, plan `PEP`) ; principe « le journal avant le cadre », propriétaire `EXIG-ORC-08` et coordinateur de saga à fenêtre de grâce (`ADR-013`).
  - **Appui vérifié :** `Corpus/Tome 1` (`L394`, `L10363`, `L12199`), `Corpus/Tome 3` (`L12418–12423`), `registre/matrice-exig-prr-c40.json` (`ADR-013`, `EXIG-ORC-08`).
  - **Passe initiale :** écart rectifié · **Action :** remplacé `IBM MQ 9.4 PQC` par `IBM MQ 9.4 LTS` avec `TLS 1.3` post-quantique et qualifié les courtiers d'exemples d'écosystème · **Verdict : supporté**

- **C14-07 (`L21`)** — *Affirmation :* `EXIG-EVT-02` impose `CloudEvents v1.0.2` `[1]` et prescrit sur `Kafka` le mode binaire défini par `[1]` (liaison par en-têtes `ce_*` selon le profil de protocole) ; aux 4 attributs `REQUIRED` de `[1]` (`id`, `source`, `specversion` `"1.0"`, `type`), il ajoute la version dans `type`, `time`, `datacontenttype` et `dataschema` ; taille bornée à `64 Ko` (`[1]`), pointeur `dataref` (`[1]`), et contrat `AsyncAPI 3.0.0`/`3.1.0` (`EXIG-EVT-03`, `CAP-012`).
  - **Appui vérifié :** `SRC-035.txt` (`L132–133`, `L158–160`, `L244–428`, `L510–525`), `Corpus/Tome 2` (`L2411–2429`), `registre/matrice-exig-prr-c40.json` (`CAP-012`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié les 4 attributs `REQUIRED` de `[1]` des ajouts obligatoires d'`EXIG-EVT-02` et précisé la garantie de relais `64 KByte` `[1]` ; en recollation `G3` (`seed=20270901`), rattaché la prescription sur `Kafka` et `ce_*` à `EXIG-EVT-02` hors cœur `SRC-035.txt` · **Verdict : supporté**

- **C14-08 (`L23`)** — *Affirmation :* Extensions de gouvernance du catalogue (`EXIG-EVT-04`, `05`, incluant des extensions documentées ultérieures à `1.0.2` figées au catalogue), interdiction des PII sur les attributs lus en clair (`[1]`), caractère informatif d'`Auth Context` (`authtype`, `authid`) et contrôle `PEP` au courtier sous `OPA`/`Rego` (`default allow := false` `[5]`, `opa test --coverage` à `100 %` exigé en `G0` `[6]`, `EXIG-EVT-07`).
  - **Appui vérifié :** `SRC-035.txt` (`L536–542`), `SRC-087.txt` (`L2072–2113`), `SRC-088.txt` (`L625–699`), `aq/rapports-g0.json` (`L31–37`), `Corpus/Tome 2` (`L2433`, `L2458–2510`).
  - **Passe initiale :** écart rectifié · **Action :** précisé le statut des extensions ultérieures figées au catalogue et rattaché le seuil `100 %` à la barrière `G0` · **Verdict : supporté**

- **C14-09 (`L25`)** — *Affirmation :* Autorisation fondée sur les ACL du catalogue et validation `dataschema`/`dataclassification` ; `EXIG-EVT-04` impose `traceparent` `W3C` et les liens causaux entre spans d'émission et de réception en corrélation avec les spans `OpenTelemetry GenAI` (`create_agent`, `invoke_agent`, `execute_tool`, statut `Development` `[7]`) ; délégation `RFC 8693` imputée dans `EXIG-ORC-04`.
  - **Appui vérifié :** `SRC-037.txt` (`L7`, `L43`, `L188`, `L668`), `Corpus/Tome 2` (`L2435`, `L2454`, `L2555`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché `traceparent` et les liens de spans à `EXIG-EVT-04` plutôt qu'à `SRC-037.txt` `[7]` qui ne définit que les spans `GenAI` · **Verdict : supporté**

- **C14-10 (`L27–L37`, Tableau 14.1)** — *Affirmation :* Le `Tableau 14.1` synthétise les attributs `CloudEvents v1.0.2` `[1]` + cadre et les extensions obligatoires `EXIG-EVT-02..09` (`traceparent`, `authtype`/`authid`, `dataclassification`, `xagentorigin`, `xagenthopcount`/`xagentmaxhops = 4`, `partitionkey`, `dataref`, `xcostcenter`).
  - **Appui vérifié :** `SRC-035.txt` (`[1]`), `SRC-037.txt` (`[7]`), `Corpus/Tome 2` (`Tableau 20`, `L2439–2448`).
  - **Passe initiale :** écart rectifié · **Action :** précisé `+ cadre` et `EXIG-EVT-04` avec `[7]` dans les deux premières lignes du Tableau 14.1 · **Verdict : supporté**

- **C14-11 (`L39–L41`, Figure 1)** — *Affirmation :* La Figure 1 (`SCH-14-01.svg`) illustre le patron hybride sur dorsale `Event Mesh` (`CloudEvents v1.0.2` / `AsyncAPI 3.0.0`), `Transactional Outbox` + `CDC` et fédération par gravité.
  - **Appui vérifié :** `specs/manifest.json` (`ch14`, `SCH-14-01`), `schemas/SCH-14-01.svg`, `schemas/rendus/SCH-14-01.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C14-12 (`L45`)** — *Affirmation :* Fédération inter-domaines par gravité (`CAP-013`, `DEC-007`, généralisant `ADR-015` sur le cloisonnement inter-entités) ; l'exemple de référence `Apache Kafka` (`Tome 2 § 6.7` : `4.0` sans `ZooKeeper`, `4.2.0` files coopératives, `4.4.0` `DLQ` associées ; livraison « au moins une fois » et `read_committed` interne) fonde les verrous solidaires d'`EXIG-EVT-08` : `Transactional Outbox` + `CDC`, déduplication sur `(source, id)` (`[1]`) et clé d'idempotence cible.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`CAP-013`, `DEC-007`, `ADR-015`, `EXIG-EVT-08`), `Corpus/Tome 2` (`Tableau 21`, `L2517–2537`), `SRC-035.txt` (`L251–254`).
  - **Passe initiale :** rectifié (`G2` + `REV-04`) · **Action :** intégré `DEC-007` et `ADR-015` (`PRD-L2-009`), uniformisé `Figure 46`–`Figure 48` et notations Unicode (`PRD-L2-022`) · **Verdict : supporté**

- **C14-13 (`L45`)** — *Affirmation :* `EXIG-EVT-09` impose une clé native égale à `partitionkey` pseudonyme sur partitions figées (sans files coopératives) ; `EXIG-EVT-10` impose `≥ 90` jours (classe modérée) et `≥ 1` an (classe élevée) de rétention avec effacement par destruction de clé, et rejeu isolé sur doublures sans reproduction garantie des décisions probabilistes.
  - **Appui vérifié :** `Corpus/Tome 2` (`L2539–2553`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C14-14 (`L47`)** — *Affirmation :* Sous `STAMP/STPA` `[4]` (action de contrôle inadéquate ou intempestive, modèle de processus désynchronisé, rétroaction manquante/erronée/retardée face à l'asymétrie de vitesse), `MAST` (`ch13`) et `OWASP ASI08`/`ASI10` `[2, 3]`, quatre pathologies menacent les bus réactifs : effet flipper et tempêtes (\(1 + k + k^2 + k^3\) sur 4 sauts, `ASI08` `[2]`), boucles d'écho (`ASI10` `[2]`), messages poisons (ex. `max.poll.interval.ms` sous `Kafka`) et saturation `TPM` / `HTTP 429`.
  - **Appui vérifié :** `SRC-058.txt` (`L398–431`, `L861–882`, `L1010–1016`), `SRC-055.txt` (`L1072–1122`, `L1305–1336`), `SRC-059.txt` (`L33–43`), `Corpus/Tome 2` (`L2468`), `Corpus/Tome 3` (`L2563–2597`).
  - **Passe initiale :** écart rectifié · **Action :** aligné le mécanisme `STPA` sur `SRC-058.txt` `[4]`, rattaché `MAST` au chapitre 13 et relié directement `ASI08`/`ASI10` à `[2]` · **Verdict : supporté**

- **C14-15 (`L49–L56`, Tableau 14.2)** — *Affirmation :* Le `Tableau 14.2` associe les quatre pathologies (`STPA`/`ASI08`/`ASI10`) aux régulateurs en ligne (`xagenthopcount`/`xagentmaxhops = 4`, plafond `traceparent`, `ce_ttl`/`expirytime`/`ce_correlationid`, validation `AsyncAPI`, rétro-pression) et aux replis (`DLQ` avant dépassement tel `max.poll.interval.ms`, `FORCED_OPEN` vers `L0`).
  - **Appui vérifié :** `SRC-058.txt` (`[4]`), `SRC-055.txt` (`[2]`), `Corpus/Tome 2` (`L2495–2501`), `Corpus/Tome 3` (`L2640–2647`).
  - **Passe initiale :** écart rectifié · **Action :** précisé `max.poll.interval.ms` comme exemple (`ex.`) en Tableau 14.2 · **Verdict : supporté**

- **C14-16 (`L60–L62`, Figure 47)** — *Affirmation :* La Figure 47 (`SCH-14-02.png`, corrigée en `REV-04` : `xagenthopcount ≥ 4`, `PRD-L2-004`) représente les quatre régulateurs déterministes et la bascule `FORCED_OPEN` vers `L0`.
  - **Appui vérifié :** `specs/manifest.json` (`ch14`, `SCH-14-02`), `schemas/SCH-14-02.mmd`, `schemas/rendus/SCH-14-02.png`.
  - **Passe initiale :** rectifié (`REV-04`) · **Action :** harmonisé `xagenthopcount ≥ 4` dans `SCH-14-02.mmd` · **Verdict : supporté**

- **C14-17 (`L62`)** — *Affirmation :* Règle `EXIG-EVT-06` (`xagenthopcount ≥ xagentmaxhops = 4`, plafond le plus bas prévalant, exception compensations `EXIG-ORC-28`, cohérence Figure 2), plafond par trace et fenêtre temporelle, `DLQ` à ACL héritées, rétro-pression `TPM` et disjoncteur interne à cinq états en mode `FORCED_OPEN` vers `L0`.
  - **Appui vérifié :** `Corpus/Tome 2` (`L2495–2501`), `Corpus/Tome 6` (`L3662–3691`), `schemas/SCH-14-02.mmd`.
  - **Passe initiale :** écart rectifié · **Action :** explicité le renvoi à la Figure 2 et le statut interne du disjoncteur à cinq états · **Verdict : supporté**

### Section 14.2.2 — Passerelle IA physique `MCP ↔ ROS 2/DDS`, `LOTO` et `Simplex` (`L64–L95`, Tableau 14.3, Figure 3)

- **C14-18 (`L66`)** — *Affirmation :* Dans l'architecture cible `ADR-028` (`Tome 3 § 46.15`, hors corpus `L+` fermé), l'incompatibilité d'horloge sépare les sagas `MCP`/`A2A` (`0,5–5 s` indicatifs) des boucles `ROS 2` (ciblant `Jazzy`/`Kilted`) / `DDS` (`10–30 ms` visés), avec interdiction pour tout agent ou LLM d'émettre des consignes continues (`cmd_vel`, couples, angles) sur `DDS` ou `Eclipse Zenoh`.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`ADR-028`, `DEC-008`), `Corpus/Tome 3` (`L24168`, `L24659–24663`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié l'architecture cible `ADR-028` (`Tome 3 § 46.15`, hors corpus `L+` fermé) et le caractère indicatif/visé des durées et distributions · **Verdict : supporté**

- **C14-19 (`L68`)** — *Affirmation :* `ADR-028` interpose une passerelle `MCP ↔ ROS 2/DDS` en `IDMZ` (modèle Purdue de référence `IEC 62443`) exposant des missions discrètes (`NavigateToNamedWaypoint`, `DockAtStation`), et impose `ROS_SECURITY_ENABLE` et `ROS_SECURITY_STRATEGY = Enforce` (enclave `X.509`, `AES-GCM`, `XML` signés) car la sécurité n'est pas activée par défaut dans la conception historique de `ROS 2` (`Tome 3 § 46.6`).
  - **Appui vérifié :** `Corpus/Tome 3` (`L24048–24060`, `L24666`), `registre/matrice-exig-prr-c40.json` (`ADR-028`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché le modèle Purdue et les paramètres `ROS 2`/`DDS-Security` à la prescription `ADR-028` (`Tome 3 § 46.6`) · **Verdict : supporté**

- **C14-20 (`L70`)** — *Affirmation :* Avant `ROS 2 Action` (`Goal → Feedback → Result`, profil cible `QoS RELIABLE`, `DEADLINE = 50 ms`), le garde-fou `ADR-028` (`Tome 3 § 46.15`) contrôle quatre préconditions : carte topologique homologuée, batterie minimale de retour, fraîcheur battement de cœur (cible indicative `≤ 5 ms`) et absence de verrou `LOTO` dans le registre de politiques (tel `Cedar` en exemple).
  - **Appui vérifié :** `Corpus/Tome 3` (`L24666`, `L24683–24709`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié les seuils `50 ms`/`≤ 5 ms` de cibles indicatives `ADR-028` et `Cedar` d'exemple du traité · **Verdict : supporté**

- **C14-21 (`L72–L79`, Tableau 14.3)** — *Affirmation :* Le `Tableau 14.3` synthétise les quatre couches de découplage cyber-physique (`IT` `0,5–5 s`, `IDMZ`/`LOTO` `20–50 ms`, `OT` `10–30 ms` non certifié `SIL`, arbitre matériel `Simplex` `PROFIsafe`/`FSoE` `≤ 1 ms` sous invariant `d_sécurité(t) ≤ d_LiDAR(t)`).
  - **Appui vérifié :** `Corpus/Tome 3` (`L24676–24681`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C14-22 (`L83–L85`, Figure 48)** — *Affirmation :* La Figure 48 (`SCH-14-03.svg`, corrigée en `REV-04` : « préparatoire à IEC 61508 et ISO 10218-1 », `PRD-L2-009`) illustre la séparation `IT`/`OT` par missions discrètes vérifiées `LOTO` et la coupure matérielle cible `Simplex` (`≤ 1 ms`).
  - **Appui vérifié :** `specs/manifest.json` (`ch14`, `SCH-14-03`), `schemas/SCH-14-03.puml`, `schemas/rendus/SCH-14-03.svg`.
  - **Passe initiale :** rectifié (`REV-04`) · **Action :** remplacé « conforme » par « préparatoire à » dans `SCH-14-03.puml` · **Verdict : supporté**

- **C14-23 (`L85–L89`)** — *Affirmation :* Le profil `ADR-028` (`Tome 3 § 46.7, § 46.15`) transpose l'architecture `Simplex` (principe de Sha, protection, ponctualité et tolérance aux fautes) en séparant `Nav2`/VLA d'un contrôleur de repli sur `MCU Safety PLC` à cycle cible `≤ 1 ms`, évaluant l'enveloppe cinématique \(d_{\text{sécurité}}(t) \le d_{\text{LiDAR}}(t)\).
  - **Appui vérifié :** `Corpus/Tome 3` (`L24064–24080`, `L24668–24674`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement la transposition et le cycle `≤ 1 ms` comme éléments cibles du profil `ADR-028` · **Verdict : supporté**

- **C14-24 (`L91`)** — *Affirmation :* L'arbitre cible bascule matériellement en `< 1 ms` vers l'arrêt sûr ; il vise un découplage préparatoire aux démarches sous `IEC 61508`, `ISO 10218-1:2025` et `ISO 3691-4` (normes payantes consignées en `statut F` hors corpus probant `L+` selon `AO-01`, sans vérification de leurs exigences logicielles), `Simplex` demeurant un patron `ADR-028` et non une voie de certification (`SIL 3` / `PL e` relevant d'une homologation instrumentée externe).
  - **Appui vérifié :** `Corpus/Tome 3` (`L24082–24086`, `L24169`, `L24674`), `sources/ch14-sources.md` (`L91`, exclusion `statut F` `iso.org`).
  - **Passe initiale :** écart rectifié · **Action :** retiré l'affirmation d'alignement normatif direct non vérifié sur ces normes payantes en `statut F` et qualifié la démarche préparatoire · **Verdict : supporté**

- **C14-25 (`L93`)** — *Affirmation :* Pour contrer les compromissions de chaîne logistique en périphérie déconnectée (`OWASP ASI04` `[2]`), le profil `ADR-028` (`Tome 3 § 46.8, § 46.16`) assemble poids, politiques `Cedar`, cartes et `Skills` en lots `OCI` signés via `TUF` (`root`, `targets`, `snapshot` hors ligne et `timestamp` en ligne contrant gel et retour arrière) et `Sigstore` (`cosign`) à double rôle, vérifiés contre `TPM 2.0` avec bascule `A/B` et sonde cible de `30` s.
  - **Appui vérifié :** `SRC-055.txt` (`L653–746`), `Corpus/Tome 3` (`L24092–24109`, `L24715–24724`).
  - **Passe initiale :** écart rectifié · **Action :** ancré `ASI04` sur `[2]`, distingué les rôles `TUF` hors ligne et en ligne (`timestamp`) et qualifié le dispositif de profil cible `ADR-028` · **Verdict : supporté**

- **C14-26 (`L95`)** — *Affirmation :* En rupture `WAN` prolongée, `ADR-028` atténue graduellement l'autonomie (`0–24 h` `L3` local avec `CRDT`, `24–72 h` cible indicative de gel des engagements externes puis rétrogradation `L1` à cosignature humaine), `72 h` demeurant une cible sans source externe à calculer par site et tester câble débranché.
  - **Appui vérifié :** `Corpus/Tome 3` (`L24163`, `L24711–24714`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié également la fenêtre `0–24 h` / `24–72 h` de cible indicative `ADR-028` · **Verdict : supporté**

### Section 14.3 — Schémas, livrables, interfaces, socle probatoire et invariants (`L97–L115`)

- **C14-27 (`L99`)** — *Affirmation :* Synthèse des trois figures (`SCH-14-01`, `SCH-14-02`, `SCH-14-03`) et de leur placement dans les sections `14.2.1` et `14.2.2`.
  - **Appui vérifié :** `specs/manifest.json` (`ch14`), `Chapitre 14.md` (`L39`, `L58`, `L81`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C14-28 (`L101–L105`)** — *Affirmation :* Quatre livrables obligatoires rattachés aux portes `PRR R-04` et `PRR R-05` (`DEC-007`, `ADR-015`, `PRD-L2-009`) : contrats `AsyncAPI 3.x` / `CloudEvents v1.0.2` `[1]` validés `OPA`/`JSON Schema` en `G0` `[5, 6]`, test de boucle `xagenthopcount ≥ 4` + `DLQ`, configuration `Outbox` + `CDC` et `traceparent` `W3C` inter-courtiers, et dossier industriel préparatoire `IEC 61508`/`ISO 10218-1` attestant `LOTO`, `DDS-Security Enforce` et coupure cible `Simplex` (`≤ 1 ms`).
  - **Appui vérifié :** `SRC-035.txt` `[1]`, `SRC-087.txt` `[5]`, `SRC-088.txt` `[6]`, `aq/rapports-g0.json`, `registre/matrice-exig-prr-c40.json` (`EXIG-EVT-01..10`, `DEC-007`, `ADR-015`, `PRR R-04`, `PRR R-05`, `ADR-028`).
  - **Passe initiale :** rectifié (`G2` + `REV-04`) · **Action :** intégré `DEC-007`, `ADR-015`, `PRR R-04` et `PRR R-05` ainsi que l'encadré `Clause non-avis` · **Verdict : supporté**

- **C14-29 (`L107`)** — *Affirmation :* Interfaces amont (`ch02`, `ch03`, `ch09`, `ch13`, `ch15`, `ch21`, `ch22`, `ch31`) et aval (`ch02`, `ch13`, `ch15`) respectant la partition bijective `CA-21`.
  - **Appui vérifié :** `specs/manifest.json` (`owned_concepts` et découpage `ch01`–`ch36`), `verifie_manuscrit.py` (`CA-21`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C14-30 (`L109`)** — *Affirmation :* Preuve documentaire arrêtée au `2 décembre 2026` sous `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` reposant sur `[1]`–`[7]` de `ch14-sources.md` et `aq/rapports-g0.json` (`overall_status = PASS`, couverture `OPA` `100,0 %` sur `45/45` tests), avec consignation en `statut F` (`AO-01`, `HTTP 403`) de `genai.owasp.org` (compensée par `[2, 3]`) et `iso.org`.
  - **Appui vérifié :** `sources/ch14-sources.md` (`L1–91`), `aq/rapports-g0.json` (`L11–37`).
  - **Passe initiale :** écart rectifié · **Action :** intégré les métriques exactes vérifiées dans `aq/rapports-g0.json` · **Verdict : supporté**

- **C14-31 (`L111–L115`)** — *Affirmation :* Trois invariants exécutables du Chapitre 14 : (1) enveloppe `CloudEvents` `≤ 64 Ko` `[1]` / `AsyncAPI 3.x` sans PII et `PEP` `OPA`/`Rego` (`default allow := false` `[5, 6]`) ; (2) coupure à `4` sauts + `Outbox`/`CDC` + déduplication `(source, id)` `[1]` + `DLQ` + `FORCED_OPEN` vers `L0` ; (3) passerelle discrète `MCP ↔ ROS 2/DDS` + `LOTO` + `DDS-Security Enforce` + `TUF`/`Sigstore` + arbitre cible `Simplex` visant `≤ 1 ms`.
  - **Appui vérifié :** `SRC-035.txt` `[1]`, `SRC-087.txt` `[5]`, `SRC-088.txt` `[6]`, `Corpus/Tome 2` (`EXIG-EVT-02..10`), `Corpus/Tome 3` (`ADR-028`).
  - **Passe initiale :** écart rectifié · **Action :** ajouté `[1, 5, 6]`, uniformisé `AsyncAPI 3.x` et qualifié `arbitre cible Simplex visant une coupure en ≤ 1 ms` · **Verdict : supporté**

- **C14-32 (`§ 14.2.1`, `§ 14.2.2`)** — *Affirmation :* La dorsale `Event Mesh` projette l'agentivité des systèmes dans le temps asynchrone où, selon `STAMP/STPA` `[4]`, les rétroactions engendrent tempêtes d'événements et dérives `ASI08`/`ASI10` `[2]` sans le plafond `xagentmaxhops = 4` ; la passerelle `MCP ↔ ROS 2/DDS` la prolonge dans l'espace physique sous verrou `LOTO` et arbitre cible `Simplex` visant `≤ 1 ms`.
  - **Appui vérifié :** `SRC-055.txt` (`[2]`), `SRC-058.txt` (`[4]`), `Tomes/Tome 2` (`EXIG-EVT-06`), `Tomes/Tome 3` (`ADR-028`).
  - **Passe initiale :** ajout ciblé · **Action :** raccordement terminologique ancré sur `[2, 4]` · **Verdict : supporté**
