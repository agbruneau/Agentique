# Journal d'ancrage atomique Wyvern G2 — Chapitre 18 (`ch18`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/06 - Partie VI/Chapitre 18.md` (`3 786` mots de prose, plage `[3 552, 4 168]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch18-sources.md` (`[1]`–`[11]` en statut `L+`, `1` exclusion `statut F` sur `iso.org`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` (`SRC-012`, `SRC-018`, `SRC-044`, `SRC-049`, `SRC-050`, `SRC-051`, `SRC-052`, `SRC-053`, `SRC-076`, `SRC-127`, `SRC-130`, `SRC-005`) ; registres `Compendium/ouvrage/registre/*.json` ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`, `authz_pqc_audit/pqc_http431.py`, `authz_pqc_audit/slh_dsa_fips205.py`, `tests/test_{authz_pqc_audit,third_party_vectors}.py`) ; repérage interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b3-5`
- **Passe G2 initiale (supportés)** : 20
- **Rectifications appliquées lors de la passe G2** : 13
- **Verdict final — supportés** : 34 / 34 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 18.md`

Toutes les formulations divergentes ou issues de documents non archivés en `L+` relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 18.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/06%20-%20Partie%20VI/Chapitre%2018.md), sans modifier le bloc scellé `CA-G0-SYNC` (`G0-EX-CH02-03`, lignes `70–101`), en préservant les invariants `CA-01`..`CA-22`, le fait `FACT-PQC-SIGNATURE-SIZE` (`ML-DSA-65 : 3 309 o`, `ML-DSA-87 : 4 627 o`), les sept ancres chronologiques rattachées à `ch18`, la vedette propriétaire `Crypto-agilité post-quantique`, les `owned_concepts`, l'ensemble des renvois `[1]`–`[11]` et le calibrage dans `[3 552, 4 168]` :

1. **Mandats américains `EO 14412` / `OMB M-26-15` et repères canadiens (`L46`, `L47`, `L48`) :** retrait de la mention `7,1 G$ US` (absente de `OMB M-26-15` et non archivée en `L+`, relevant d'un rapport antérieur de juillet 2024 cité hors socle au `Tome 1 § 21.7`) au profit des échéances exactes documentées dans `SRC-051.txt` (`TLS 1.3` au `2 janvier 2030`, établissement de clés au `31 décembre 2030`, signatures au `31 décembre 2031`) ; qualification explicite d'`ITSM.40.001` et du bulletin BSIF de mars 2026 comme repérage historique `Tome 1 § 21.8` hors base `L+` ; rattachement des quatre dates canadiennes et québécoises (`22 septembre 2023`, `1er octobre 2028`, `fin 2028`, `30 juin 2033`) aux ancres `L+` du registre chronologique plutôt qu'à `[5]`.
2. **Théorème de Mosca, fenêtre `2026–2029`, constat `0/5` et transport hybride (`L13`, `L50`, `L52`, `L56`, `L58`, `L131`) :** alignement des notations (\(X + Y > Z\)) sur `SRC-051.txt`, attribution explicite de la fenêtre `2026–2029` et du constat `0/5` aux constructions et inventaires du `Tome 1` (`§ 21.5`, `§ 21.9`), reformulation des durées de conservation à partir de `7` ans (`EXIG-SEC-28`), et distinction claire entre `MLS` (`RFC 9420` `[11]`), `ML-KEM-768` (`FIPS 203` `[1]`) et le profil hybride transitoire `X25519MLKEM768` (`NIST IR 8547` `[4]`).
3. **Défis `ACME` (`L29`), banc `pqc_http431.py` (`L68`, `L103`) et trajectoire `DAPP` `P1–P3` (`Tableau 18.3`) :** précision des défis spécifiés dans `RFC 8555` (`http-01`, `dns-01`, avec `TLS-ALPN-01` en complément), retrait de l'allégation d'exécution de `Borealis-Bench` (absent du disque selon `Tome 8`) et de la grandeur `165 Ko` (absente de `pqc_http431.py` et de `SRC-012.txt`), et harmonisation du `Tableau 18.3` sur `DAPP-T5-04..06` (`P1` `2028–2029` incluant `TLS ≤ 47 j` après rampe `2026–2027`, `P2` `2030–2032`, `P3` `2033–2035`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C18-01` à `C18-33`)

### Ouverture et Section 18.1 — Résumé exécutif (`L1–L15`)

- **C18-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice posant l'automatisation PKI à `47` jours et la transition post-quantique `ML-DSA`/`SLH-DSA` sans saturation `HTTP 431` ni perte probante des archives et mandats à long terme.
  - **Appui vérifié :** `specs/manifest.json` (`ch18`, `D06`, `SUB_D06_03`), structure `§ 18.1`–`§ 18.3`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-02 (`L5`)** — *Affirmation :* Appui sur les identités non humaines (`← ch16`) et les chaînes `OBO`/`CIBA` (`← ch17`), avec convergence entre la réduction `TLS` jusqu'à `47` jours `[6, 10]` et la publication des normes PQC et de `NIST IR 8547` (`octobre 2026`) fixant l'échéance classique à `2030–2035` `[1, 2, 3, 4]`.
  - **Appui vérifié :** `SRC-053.txt` (`L205`), `SRC-127.txt`, `SRC-049.txt`, `SRC-050.txt`, `SRC-018.txt`, `SRC-051.txt` (`L28`, `L57`, `L801–802`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-03 (`L7`)** — *Affirmation :* Traduction en exigences `EXIG-SEC-27`, `EXIG-SEC-28`, `PRI-012`, `POR-001`, `POR-007`, `POR-011` au gel du `2 décembre 2026`, démonstration du dépassement `HTTP 431` sur `pqc_http431.py` dès `2` sauts avec parade `kid`/`JWKS` et `Transaction Tokens CBOR-COSE O(1)` `[7, 8]`, et clause `non-avis` (`AO-05`).
  - **Appui vérifié :** `matrice-exig-prr-c40.json` (`C27`), `Corpus/Tome 2` (`L4708–4722`), `pqc_http431.py`, `SRC-012.txt` (`[7]`), `SRC-044.txt` (`[8]`), `ch18-sources.md` (`L4–5`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-04 (`L11`)** — *Affirmation :* `Ballot SC-081v3` (*CA/Browser Forum*, `4 octobre 2026`) réduit la validité `TLS` publique à `100` jours au `15 mars 2027` puis `47` jours au `15 mars 2029` (réutilisation de validation à `10` jours) `[6]`, imposant `ACME` (`RFC 8555` `[10]`) et `SPIFFE`/`Envoy SDS` dès `POR-001`.
  - **Appui vérifié :** `SRC-053.txt` (`L199–205`), `ch18-sources.md` (`[6]` `2026-10-04`), `SRC-127.txt` (`[10]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-05 (`L13`)** — *Affirmation :* Théorème de Mosca (\(X + Y > Z\)) `[4]`, fenêtre d'action inverse `2026–2029` construite par le cadre pour les artefacts à conservation longue (`≥ 7` ans sous `EXIG-SEC-28`), `CBOM`, trois conditions de **crypto-agilité post-quantique**, et séparation stricte des calendriers (`NIST IR 8547`, `G7`, `EO 14412`/`OMB M-26-15`, repères canadiens, échéances d'oct. 2028, fin 2028 et juin 2033) `[4, 5]`.
  - **Appui vérifié :** `SRC-051.txt` (`L465–471`, `L206–209`), `SRC-052.txt` (`[5]`), `glossaire-termes.json` (`L351–357`), `ancres-chronologiques.json`.
  - **Passe initiale :** écart rectifié · **Action :** aligné les notations (\(X + Y > Z\)), reformulé `7` ans sous `EXIG-SEC-28` et qualifié la fenêtre `2026–2029` comme construction du cadre · **Verdict : supporté**

- **C18-06 (`L15`)** — *Affirmation :* Tailles de signature `ML-DSA-65` (`3 309` octets) et `ML-DSA-87` (`4 627` octets) `[2, 7]`, soit `50` à `72` fois `Ed25519` (`64` octets `[9]`), franchissant `8 192` octets (`HTTP 431`) sans `CBOR-COSE O(1)`, `kid`/`JWKS`, `X25519MLKEM768` (`MLS`, `RFC 9420`) et `SCITT` (`RFC 9943`) + `SLH-DSA` (`FIPS 205`) `[1, 3, 7, 8, 11]`.
  - **Appui vérifié :** `SRC-050.txt` (`L1317`, `L1321`), `SRC-012.txt` (`L199–201`), `SRC-076.txt` (`L1110`), `faits-empiriques.json` (`FACT-PQC-SIGNATURE-SIZE`), `SRC-049.txt`, `SRC-018.txt`, `SRC-044.txt`, `SRC-130.txt`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 18.2.1 — Certificats `TLS` `100 j / 47 j` et `ACME` (`L19–L35`, Figure 1)

- **C18-07 (`L21`)** — *Affirmation :* Multiplication des terminaisons `TLS` (`PEP`, `MCP`, `A2A`, `STS`, `CIBA`, `IDMZ`), plafond historique `398` jours puis `200` jours jusqu'en `2026`, et réduction en deux marches par `Ballot SC-081v3` (`EXIG-SEC-27`, `PRI-012`) `[6]`.
  - **Appui vérifié :** `SRC-053.txt` (`L192`, `L2185`), `Corpus/Tome 2` (`EXIG-SEC-27`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-08 (`L23`)** — *Affirmation :* Au `15 mars 2027`, validité maximale `TLS` publique et réutilisation de validation de domaine/IP ramenées à `100` jours ; au `15 mars 2029`, validité maximale ramenée à `47` jours et réutilisation de validation réduite à `10` jours `[6]`.
  - **Appui vérifié :** `SRC-053.txt` (`L199–200`, `L204–205`), `ancres-chronologiques.json` (`2027-03-15-TLS-100J`, `2029-03-15-TLS-47J`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-09 (`L25`, `L27`)** — *Affirmation :* Sous un plafond de `47` jours (renouvellement opérationnel tous les `25` à `30` jours, fréquence `~8×` par rapport au cycle annuel), les billets manuels provoquent une **collision cryptographique** menaçant `Temporal` et `OPA`/`Cedar`, et la fenêtre de validation de `10` jours exclut les preuves manuelles trimestrielles `[6, 10]`.
  - **Appui vérifié :** `SRC-053.txt` (`L204–205`), `SRC-127.txt` (`[10]`), arithmétique vérifiée (`398 / 47 ≈ 8,5`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-10 (`L29`, `L31`)** — *Affirmation :* `EXIG-SEC-27`, `EXIG-IAM-15`, `INI-002` et `POR-001` imposent `100,0 %` d'automatisation via `ACME` (`RFC 8555`, mars 2019, défis `http-01` et `dns-01`, complétés le cas échéant par `TLS-ALPN-01` `[10]`), inventaire exhaustif, `SPIFFE`/`Envoy SDS` (`1 h`, `← ch16`) et blocage `POR-007` sous test `≤ 47` jours sans coupure `[6, 10]`.
  - **Appui vérifié :** `SRC-127.txt` (`L483`, `L1459`, `L2598`), `SRC-053.txt` (`L205`), `Corpus/Tome 2` (`EXIG-SEC-27`, `EXIG-IAM-15`).
  - **Passe initiale :** écart rectifié · **Action :** distingué les défis normalisés par `RFC 8555` (`http-01`, `dns-01`) du complément `TLS-ALPN-01` · **Verdict : supporté**

- **C18-11 (`L33`–`L35`, Figure 1)** — *Affirmation :* Figure 1 (`SCH-18-01.png`) retraçant `200 j → 100 j (15 mars 2027) → 47 j (15 mars 2029)`, le piège de collision et l'automatisation `ACME`/`Envoy SDS` dès `P1`.
  - **Appui vérifié :** `specs/manifest.json` (`SCH-18-01`), `schemas/SCH-18-01.mmd`, `schemas/rendus/SCH-18-01.png`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 18.2.2 — Transition post-quantique, crypto-agilité et choc `HTTP 431` (`L37–L122`, Tableau 18.1, Figures 2–3)

- **C18-12 (`L39`)** — *Affirmation :* Menace de l'algorithme de Shor sur `RSA`, `ECDSA` et `Ed25519`, et publication le `13 août 2024` des normes NIST `FIPS 203` (`ML-KEM`), `FIPS 204` (`ML-DSA`) et `FIPS 205` (`SLH-DSA`) `[1, 2, 3]`.
  - **Appui vérifié :** `SRC-049.txt` (`L12`, `L47`), `SRC-050.txt` (`L12`, `L43`), `SRC-018.txt` (`L12`, `L44`), `SRC-051.txt` (`L287–292`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-13 (`L41`)** — *Affirmation :* Publication finale de `NIST IR 8547` le `21 octobre 2026` programmant la dépréciation des algorithmes asymétriques classiques après `2030` et leur interdiction après `2035` `[4]`, et feuille de route financière du `G7 Cyber Expert Group` (`14 janvier 2026`) sur `2030–2035` `[5]`.
  - **Appui vérifié :** `SRC-051.txt` (`L57`, `L801–802`, `L880–881`, `L901–903`), `SRC-052.txt` (`L6`, `L189–198`), `ancres-chronologiques.json` (`2030-2035-G7-PQC-FINANCE`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-14 (`L43`, `L45`)** — *Affirmation :* Séparation de quatre familles de repères sans fusion ; référentiels techniques `NIST IR 8547` (`> 2030` / `> 2035`) `[4]` et coordination financière `G7` (`2030–2035`, priorité critique `2030–2032`) `[5]`.
  - **Appui vérifié :** `SRC-051.txt` (`L901–903`), `SRC-052.txt` (`L196–198`, note 9).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-15 (`L46`)** — *Affirmation :* Mandats gouvernementaux américains `EO 14412` (`22 juin 2026`) et `OMB M-26-15` (`24 juin 2026`) imposant aux agences fédérales américaines `TLS 1.3` au `2 janvier 2030`, l'établissement de clés PQC au `31 décembre 2030` et les signatures numériques au `31 décembre 2031`, sans lier les institutions financières canadiennes `[4]`.
  - **Appui vérifié :** `SRC-051.txt` (`L206–209`, `L908–910`, `L1160`, `L1190–1194`, `L1285`).
  - **Passe initiale :** écart rectifié · **Action :** retiré le coût `7,1 G$ US` (issu d'un rapport OMB de juillet 2024 hors `L+`) et inscrit les échéances exactes de `SRC-051.txt` · **Verdict : supporté**

- **C18-16 (`L47`)** — *Affirmation :* Orientations canadiennes `ITSM.40.001` (`23 juin 2025`, `fin 2031` / `fin 2035` pour le gouvernement fédéral canadien) et bulletin technologique BSIF de mars 2026 relevés au repérage historique `Tome 1 § 21.8` (hors base `L+`), sans obligation légale directe sur les institutions financières privées (`→ ch25`).
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 21.8`, `L5094–5107`, `Tableau 21.4`), contrôle négatif `corpus_l_plus/` (`0` occurrence).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement comme repérage historique `Tome 1 § 21.8` hors base fermée `L+` · **Verdict : supporté**

- **C18-17 (`L48`)** — *Affirmation :* Ancres réglementaires `L+` canadiennes et québécoises croisant la conservation longue : Loi 25 art. 12.1 (`22 septembre 2023`), Norme canadienne `31-103` (`1er octobre 2028`), `BSIF B-15` portée 3 (`fin 2028`) et Loi sur les banques art. 21 (`30 juin 2033`).
  - **Appui vérifié :** `registre/ancres-chronologiques.json` (`2026-LOI25-ART12-1`, `2028-10-01-GESTION-PATRIMOINE-RETROFACTURATION`, `2028-12-31-BSIF-B15-PORTEE3`, `2033-06-30-LOIS-FINANCIERES-CANADA`), `SRC-063`, `SRC-064`, `SRC-111`, `SRC-110`, `SRC-070`.
  - **Passe initiale :** écart rectifié · **Action :** retiré le renvoi `[5]` inadéquat et rattaché ces dates aux ancres `L+` du registre chronologique · **Verdict : supporté**

- **C18-18 (`L50`)** — *Affirmation :* Extension architecturale de « récolter maintenant, déchiffrer plus tard » `[4, 5]` vers « récolter maintenant, falsifier plus tard » pour les signatures et mandats à conservation de `7` ans à plusieurs décennies à l'horizon `2030–2035`, aggravée par l'absence d'expiration native sur l'`AgentCard` (`← ch16`).
  - **Appui vérifié :** `SRC-051.txt` (`L200–205`, `L278–288`), `SRC-052.txt` (`L193–195`), `Corpus/Tome 1` (`§ 21.2`, `L4961–4969`).
  - **Passe initiale :** écart rectifié · **Action :** borné la fenêtre de risque sur `2030–2035`, remplacé `7 à 40 ans` par `7 ans ou plusieurs décennies` et distingué la projection architecturale des sources `[4, 5]` · **Verdict : supporté**

- **C18-19 (`L52`, `L54`)** — *Affirmation :* Théorème de Mosca (\(X + Y > Z\)) `[4]`, fenêtre d'action inverse `2026–2029` construite depuis `2030` (`Tome 1 § 21.9`), inventaire `CBOM` dès `2026–2027` `[4, 5]` à quatre dimensions et priorisation des actifs dépassant `2030`.
  - **Appui vérifié :** `SRC-051.txt` (`L213–215`, `L465–471`), `SRC-052.txt` (`L110–120`), `Corpus/Tome 1` (`§ 21.9`, `L5125`).
  - **Passe initiale :** écart rectifié · **Action :** aligné les notations (\(X + Y > Z\)) sur `SRC-051.txt` et explicité l'origine `Tome 1 § 21.9` de la fenêtre `2026–2029` · **Verdict : supporté**

- **C18-20 (`L56`)** — *Affirmation :* Définition de la **crypto-agilité post-quantique** (`EXIG-SEC-27`, `EXIG-SEC-28`) en trois conditions (paramètre `alg` nommé `[2, 7]`, schémas versionnés Draft 2020-12 Annexe C `[7]`, procédure de retrait testée) et constat `0/5` issu de l'inventaire `Tome 1 § 21.5` face au risque de rétrogradation `[4, 5]`.
  - **Appui vérifié :** `glossaire-termes.json` (`L351–357`), `SRC-050.txt` (`[2]`), `SRC-012.txt` (`[7]`), `Corpus/Tome 1` (`§ 21.5 Tableau 21.3`, `L5019–5040`), `SRC-051.txt`, `SRC-052.txt`.
  - **Passe initiale :** écart rectifié · **Action :** attribué explicitement `0/5` à l'inventaire comparatif `Tome 1 § 21.5` plutôt qu'aux sources `[4, 5]` · **Verdict : supporté**

- **C18-21 (`L58`)** — *Affirmation :* Quatre patrons de transition `[2, 7, 8]` et déploiement sur le plan transport (`EXIG-SEC-28`) de `TLS 1.3` et `MLS` (`RFC 9420`, juill. 2023 `[11]`) sur `SLIM`/`AGNTCY` avec le profil hybride `X25519MLKEM768` combinant `X25519` et `ML-KEM-768` (`FIPS 203` `[1]`) selon l'approche transitoire de `NIST IR 8547` `[4]`.
  - **Appui vérifié :** `SRC-049.txt` (`[1]`), `SRC-130.txt` (`[11]`), `SRC-051.txt` (`L939–941`, `L1161–1162` `[4]`), `SRC-050.txt`, `SRC-012.txt`, `SRC-044.txt`.
  - **Passe initiale :** écart rectifié · **Action :** dissocié `RFC 9420` (`[11]`) de la spécification de `X25519MLKEM768` et ancré l'hybridation sur `FIPS 203` (`[1]`) et `NIST IR 8547` (`[4]`) · **Verdict : supporté**

- **C18-22 (`L60`)** — *Affirmation :* Ancrage des journaux `C.8`, cartes `AgentCard` et jetons `CIBA` (`> 5` ans) dans un arbre de Merkle `SCITT` (`RFC 9943`, juin 2026 `[8]`) et rescellement `≤ 5` ans en `SLH-DSA` (`FIPS 205`, `SHA2-128s` à `7 856` octets, `SHA2-128f` à `17 088` octets, clé publique `32` octets `[3]`) ; implémentation Python pur sous licence `MIT` dans `slh_dsa_fips205.py` (vecteurs `NIST FIPS 205 ACVP`, sans paquet `LGPL-3.0-or-later`) et sélection exclusive de `SLH-DSA-SHA2-128s` par `seal_merkle_root` dans `audit_scitt_focus.py` (`→ ch22`).
  - **Appui vérifié :** `SRC-044.txt` (`[8]`), `SRC-018.txt` (`[3]`), `slh_dsa_fips205.py` (`L2`, `L33–40`), `audit_scitt_focus.py`, `aq/rapports-g0.json` (`nist_acvp` `12/12`, `spdx_check` `MIT`), `Corpus/Tome 2` (`EXIG-SEC-28`).
  - **Passe initiale :** conforme · **Action :** précisées les tailles exactes `7 856`/`17 088`/`32` octets et le rôle de `slh_dsa_fips205.py`/`audit_scitt_focus.py` (`post-G4`) · **Verdict : supporté**

- **C18-23 (`L62`–`L64`, Figure 2)** — *Affirmation :* Figure 2 (`SCH-18-02.svg`) distinguant les calendriers `2024–2035`, la fenêtre de Mosca `2026–2029`, les trois conditions de crypto-agilité et le rescellement `SCITT + SLH-DSA`.
  - **Appui vérifié :** `specs/manifest.json` (`SCH-18-02`), `schemas/SCH-18-02.svg`, `schemas/rendus/SCH-18-02.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-24 (`L66`)** — *Affirmation :* Comparaison exacte des tailles : `Ed25519` (`RFC 8032` `[9]`, `64` o) et `ES256` (`64` o) contre `ML-DSA-44` (`2 420` o), `ML-DSA-65` (`3 309` o, ~`52×`, clé publique `1 952` o) et `ML-DSA-87` (`4 627` o, ~`72×`, clé publique `2 592` o) `[2, 7]`.
  - **Appui vérifié :** `SRC-076.txt` (`L1110`), `SRC-005.txt` (`L2223`), `SRC-050.txt` (`L1312–1321`), `SRC-012.txt` (`L197–202`), `faits-empiriques.json` (`FACT-PQC-SIGNATURE-SIZE`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-25 (`L68`–`L101`, `G0-EX-CH02-03`)** — *Affirmation :* Plafond HTTP courant de `8 192` octets (`8` Kio) en \(O(\text{sauts})\) `[7]` et extrait scellé `CA-G0-SYNC` `G0-EX-CH02-03` (`pqc_http431.py`, lignes `149–177`, `sha256="c5c72e27..."`) vérifié à la barrière `G0` pour pallier l'absence sur disque de `Borealis-Bench` `[2, 7]`.
  - **Appui vérifié :** `aq/rapports-g0.json` (`L120–126`), `pqc_http431.py` (`L149–177`), `Corpus/Tome 8` (`L1763`, `L2130`), `SRC-012.txt` (`[7]`).
  - **Passe initiale :** écart rectifié · **Action :** retiré l'allégation d'exécution en Campagne 4 de `Borealis-Bench` (dépôt absent du disque) et rattaché la vérification à la barrière `G0` · **Verdict : supporté**

- **C18-26 (`L103`–`L114`, Tableau 18.1)** — *Affirmation :* Mesures déterministes d'`evaluate_http_431` sur `1`, `2` et `5` sauts : `JWT_EMBEDDED_JWK` (`8 298`/`11 193` à `41 993`/`56 468` o), `JWT_X5C_CHAIN` (`14 139`/`19 380` à `71 198`/`97 403` o), `JWT_KID_REF` (`4 793`/`6 551` → `9 624`/`13 140` → `24 468`/`33 258` o), `CBOR_COSE_CWT` (`4 692`/`6 449` → `9 413`/`12 928` → `23 880`/`32 666` o), `TRANSACTION_TOKEN_JWT` (`4 778`/`6 536` o constants) et `TRANSACTION_TOKEN_CBOR` (`4 757`/`6 514` o constants) `[2, 7]`.
  - **Appui vérifié :** exécution directe de `pqc_http431.evaluate_http_431` (`.venv`), `test_authz_pqc_audit.py::test_pqc_http431_vs_transaction_token_o1`, `SRC-012.txt` (`[7]`), `SRC-050.txt` (`[2]`).
  - **Passe initiale :** écart rectifié · **Action :** retiré la mention `près de 165 Ko` absente de `pqc_http431.py` et de `SRC-012.txt`, et conservé les seules mesures vérifiées · **Verdict : supporté**

- **C18-27 (`L116`)** — *Affirmation :* Parade en trois mesures (`EXIG-SEC-27`, `POR-007`) : bannissement des clés embarquées au profit de `kid`/`JWKS`, tampons passerelle `≥ 32` Ko dès `P1`, et bascule intra-domaine vers des `Transaction Tokens` (`← ch17`, `transaction-tokens-11` hors base fermée de ce chapitre) encodés en `CBOR-COSE` `ML-DSA` selon `RFC 9964` `[7]` et `FIPS 204` `[2]`, mesurés en \(O(1)\) par `pqc_http431.py` (`G0`) à `4 757` o (`ML-DSA-65`) et `6 514` o (`ML-DSA-87`).
  - **Appui vérifié :** `SRC-012.txt` (`[7]`), `SRC-050.txt` (`[2]`), `pqc_http431.py` (`aq/rapports-g0.json`), `Corpus/Tome 2` (`EXIG-SEC-27`).
  - **Passe initiale :** conforme · **Action :** en recollation `G3` (`seed=20270901`), dissocié `transaction-tokens-11` (absent de `ch18-sources.md`) de `[7]` et rattaché `4 757` / `6 514` octets aux mesures `G0` de `pqc_http431.py` sur `[2, 7]` · **Verdict : supporté**

- **C18-28 (`L118`–`L122`, Figure 3 & `AO-01`)** — *Affirmation :* Figure 3 (`SCH-18-03.png`) illustrant le choc `HTTP 431` et sa neutralisation `O(1)`, et exclusion `AO-01` de la norme ISO payante (`HTTP 403` sur `iso.org`) au profit des normes ouvertes NIST, IETF, *CA/B Forum* et vecteurs `G0` `[1, 2, 3, 4, 6, 7]`.
  - **Appui vérifié :** `specs/manifest.json` (`SCH-18-03`), `schemas/SCH-18-03.mmd`, `schemas/rendus/SCH-18-03.png`, `recherche/registre-statut-f.json` (`L216–224`), `ch18-sources.md` (`L132–134`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 18.3 — Synthèse architecturale, livrables et portes (`L124–L153`, Tableaux 18.2–18.3, Encadré)

- **C18-29 (`L126`)** — *Affirmation :* Liens transversaux amont (`← ch08, ch31, ch35, ch36`) et aval (`→ ch09, ch16, ch17, ch22, ch25, ch31`, dont `SIG-009`..`SIG-012`) respectant l'exclusivité conceptuelle `CA-21`.
  - **Appui vérifié :** `specs/manifest.json` (`ch18.owned_concepts`), `Corpus/Tome 4` (`SIG-009`..`SIG-012`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-30 (`L128`–`L135`, Tableau 18.2)** — *Affirmation :* Quatre livrables et critères exécutables (`G0`–`G1`) : `ACME`/`Envoy SDS` `TLS ≤ 47 j` (`15 mars 2029`, validation `≤ 10 j` `[6, 10]`) ; `CBOM` et `3` conditions (`0/5` au `Tome 1 § 21.5`, fenêtre `2026–2029` `[4, 5]`) ; `pqc_http431.py` `O(1)` (`4 757` o / `6 514` o à `HTTP 200` `[2, 7]`) ; `SCITT` (`RFC 9943`) + `slh_dsa_fips205.py` + vecteurs `NIST ACVP` + `X25519MLKEM768` `[1, 3, 8, 11]`.
  - **Appui vérifié :** `SRC-049.txt`, `SRC-050.txt`, `SRC-018.txt`, `SRC-051.txt`, `SRC-052.txt`, `SRC-053.txt`, `SRC-012.txt`, `SRC-044.txt`, `SRC-127.txt`, `SRC-130.txt`, `aq/rapports-g0.json` (`L58–63`), `test_third_party_vectors.py` (`L208–292`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement `0/5` au `Tome 1 § 21.5` dans la ligne `CBOM` · **Verdict : supporté**

- **C18-31 (`L137`–`L145`, Tableau 18.3)** — *Affirmation :* Trajectoire échelonnée `P1`–`P3` : `P1` (`2028–2029` après rampe `2026–2027`, `INI-002`, `POR-001`, `ACME` `100 %` `100 j` puis `≤ 47 j`, tampons `≥ 32` Ko, `CBOM`, `X25519MLKEM768`) `[6, 10, 11]` ; `P2` (`2030–2032`, `INI-019`, `POR-007`, `ML-DSA`, `CBOR-COSE O(1)` + `kid`/`JWKS`, `SCITT + SLH-DSA ≤ 5` ans) `[3, 5, 7, 8]` ; `P3` (`2033–2035`, `INI-041`, `POR-011`, retrait classique `> 2035`) `[3, 4]`.
  - **Appui vérifié :** `ancres-chronologiques.json` (`DAPP-T5-04`, `DAPP-T5-05`, `DAPP-T5-06`), `Chapitre 31.md` (`L44–52`), `SRC-018.txt`, `SRC-051.txt`, `SRC-052.txt`, `SRC-053.txt`, `SRC-012.txt`, `SRC-044.txt`, `SRC-127.txt`, `SRC-130.txt`.
  - **Passe initiale :** écart rectifié · **Action :** réaligné les horizons et jalons de `P1` (`2028–2029`, incluant `TLS ≤ 47 j`) et `P2` (`2030–2032`) sur `DAPP-T5-04..06` et le `Chapitre 31` · **Verdict : supporté**

- **C18-32 (`L147`)** — *Affirmation :* Clôture de `D06` (identité machine parrainée jusqu'à pérennité post-quantique) et enchaînement vers la défense hors modèle et `OPA`/`Rego` (`→ Chapitre 19`).
  - **Appui vérifié :** `specs/manifest.json` (`D06`, `D07`, `ch19`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C18-33 (`L151`–`L155`, Trois invariants)** — *Affirmation :* Encadré final des trois invariants exécutables : automatisation `ACME`/`SPIFFE` `100,0 %` (`15 mars 2027` et `15 mars 2029`, `≤ 47` j, `≤ 10` j) ; maîtrise `HTTP 431` sous `ML-DSA-65` (`3 309` o) / `ML-DSA-87` (`4 627` o) via `kid`/`JWKS`, `CBOR-COSE O(1)` (`4 757`–`6 514` o pour l'en-tête seul) et tampons passerelle `≥ 32` Ko dès `P1` face au cumul `Authorization`/`Txn-Token` + preuve `DPoP` (`> 8 192` o hors `mTLS` dès le premier saut) ; crypto-agilité en `3` conditions, `X25519MLKEM768` et rescellement `SCITT` (`RFC 9943`) + `SLH-DSA` (`FIPS 205`) `≤ 5` ans.
  - **Appui vérifié :** `SRC-053.txt`, `SRC-127.txt`, `SRC-050.txt`, `SRC-012.txt`, `SRC-044.txt`, `SRC-018.txt`, `SRC-051.txt`, `pqc_http431.py`, `Corpus/Tome 2` (`EXIG-SEC-27`, `EXIG-SEC-28`, `EXIG-IAM-14`).
  - **Passe initiale :** conforme · **Action :** précisé le cumul `Authorization`/`Txn-Token` + `DPoP` dépassant `8 192` octets hors `mTLS` (`post-G4`) · **Verdict : supporté**

- **C18-34 (Révision `REV-04` : `PRD-L2-002`, `010`, `018`, `019`, `021`–`023`, `PRD-L4-002`)** — *Affirmation :* Résolution du bloquant `PRD-L2-002` dans `SCH-18-03.mmd` (`9,6–38,8 Ko` à 2 sauts et `24,5–97,4 Ko` max `97 403 o` à 5 sauts alignés sur `pqc_http431.py` / Tableau 18.1), uniformisation `Figure 58`..`Figure 60`, francisation `automation` → `automatisation` (`SCH-18-01.mmd`), qualification `Tome 1 Tab. 21.3` (`SCH-18-02.svg`), accord `sa neutralisation`, réconciliation explicite de la date `NIST IR 8547 Final` (`21 octobre 2026` faisant foi selon `SRC-051` face au repère antérieur du `27 octobre 2026`), intégration de `ANC-023/030/040/043`, `DEC-012`, `SIG-010/011`, `SP 800-131A Rev. 3` (`SRC-051`), `Public Law 117-260` et veille `Europol/QSFF` (repérage du traité), encadré `Clause non-avis (AO-05)` et conversion Unicode de toutes les expressions LaTeX, bloc `CA-G0-SYNC` `G0-EX-CH02-03` intact.
  - **Appui vérifié :** `SRC-051.txt` (`[4]`), `manifeste-sources-sha256.json` (`SRC-051` `2026-10-21`), `pqc_http431.py`, `schemas/SCH-18-01.mmd`, `schemas/SCH-18-02.svg`, `schemas/SCH-18-03.mmd`, `Compendium/prd.md`.
  - **Passe initiale :** ajout `REV-04` · **Action :** vérification différentielle `REV-04` · **Verdict : supporté**
