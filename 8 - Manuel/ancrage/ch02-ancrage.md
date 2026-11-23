# Audit d'ancrage atomique Wyvern — Chapitre 02 (`ch02`)

- **Unité auditée** : `manuscrit/01 - Partie I/Chapitre 02 - Identite non humaine, PQC et double couloir.md`
- **Dossier fermé de sources** : `sources/ch02-sources.md` (`26` sources `L+` numérotées `[1]` à `[26]` : `SRC-046`, `SRC-047`, `SRC-048`, `SRC-041`, `SRC-009`, `SRC-043`, `SRC-042`, `SRC-045`, `SRC-004`, `SRC-019`, `SRC-020`, `SRC-017`, `SRC-050`, `SRC-012`, `SRC-076`, `SRC-013`, `SRC-089`, `SRC-090`, `SRC-037`, `SRC-044`, `SRC-018`, `SRC-023`, `SRC-010`, `SRC-053`, `SRC-063`, `SRC-077`)
- **Sources `L+` complémentaires du manifeste (`manifeste-sources-sha256.json`) et `statut F` (`registre-statut-f.json`)** : `SRC-051` (`NIST IR 8547`), `SRC-052` (`G7 Cyber Expert Group`), `SRC-078` (`MCP 2026-07-28 Authorization Security Considerations`) ; `P-39.1` consigné en `statut F` (`HTTP 403`) compensé par `SRC-063` (`LQ 2021, c. 25`)
- **Preuves `G0` et registres vérifiés** : `aq/rapports-g0.json`, `8 - Trousse/authz_pqc_audit/` (`7` modules), `8 - Trousse/schemas/` (`4` schémas `ch02`), `8 - Trousse/tests/` (`test_authz_pqc_audit.py`, `test_third_party_vectors.py`), `registre/ancres-chronologiques.json`, `registre/faits-empiriques.json`, `registre/glossaire-termes.json`, `registre/matrice-exig-prr-c40.json`
- **Date de gel des faits** : 2 décembre 2026 (`2026-12-02`)
- **Volume final vérifié (`G1`)** : `8 898` mots lexicaux `CA-03` (`9 847` `split()`, cible `[7 820, 9 180]`)
- **Barrière** : `G2` (`CA-10`, `CA-12`, protocole d'ancrage atomique Wyvern `specs/contrat-aq.md` § 2.2)

## Bilan quantifié de l'audit

- **Total d'affirmations atomiques segmentées** : 86 (`C01` à `C86`)
- **Constat initial — supportés** : 52
- **Constat initial — imprécis rectifiés** : 34 (`C03`, `C04`, `C11`, `C19`, `C22`, `C23`, `C24`, `C29`, `C31`, `C32`, `C33`, `C34`, `C35`, `C36`, `C37`, `C42`, `C43`, `C44`, `C52`, `C53`, `C55`, `C56`, `C57`, `C58`, `C59`, `C64`, `C65`, `C71`, `C73`, `C79`, `C81`, `C83`, `C84`, `C85`)
- **Constat initial — non supportés supprimés ou réancrés** : 0
- **Verdict final — supportés : 86 (100 %)**
- **Imprécis résiduels (final) : 0**
- **Non supportés résiduels (final) : 0**

---

## Détail paragraphe par paragraphe et affirmation par affirmation

### Titre et question directrice (`L001`, `L003`)

- **C01 (`L001`, `L003`)** — Le titre et la question directrice posent le périmètre du Chapitre 02 (identité non humaine, délégation bornée à deux sauts, choc post-quantique `ML-DSA` sous le plafond HTTP 431, double couloir `OTel` / `JCS` / `SCITT` / `SLH-DSA` / `FOCUS`), en cohérence exacte avec `specs/manifest.json`, `specs/toc.md` et les six vedettes de `registre/glossaire-termes.json` (`Identité non humaine`, `Passage de jeton`, `Jeton de transaction`, `Preuve d'action C.6`, `Double couloir probatoire`, `Coût par résultat conforme`).
  - Constat initial : supporté.
  - Verdict final : supporté

### Ouverture — Scénario illustratif (`L005`, `L007`, `L009`)

- **C02 (`L005`)** — Modélisation pédagogique explicite (`*Scénario illustratif.* Imaginons...`) d'un flux d'approvisionnement entre un agent orchestrateur et un agent spécialiste soumis à validation humaine.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C03 (`L005`)** — Définition du *passage de jeton* (*Token Passthrough*) proscrit par la spécification `MCP 2026-07-28` (Chapitre 1, `SRC-078.txt` l. 22–23, 124) et l'exigence `EXIG-MCP-11` (`Cadre de Référence`, Vol. 2) faute de liaison d'audience conforme à `RFC 8707` `[5]` (`SRC-009.txt` l. 99, 194–197).
  - Constat initial : imprécis (rattachait directement `[5]` (`RFC 8707`) à `(proscrit par EXIG-MCP-11)`, alors que `SRC-009.txt` ne contient ni l'expression *Token Passthrough* ni `EXIG-MCP-11` ; rectifié en séparant explicitement l'interdiction `MCP 2026-07-28` / `EXIG-MCP-11` et la liaison d'audience `RFC 8707 [5]`).
  - Verdict final : supporté
- **C04 (`L007`)** — Horizon post-quantique `2030–2035` : conjugaison de la cible non contraignante du groupe d'experts cyber du `G7` (`G7 CEG`, secteur financier : `2030–2032` pour les systèmes critiques et `2035` au total ; `SRC-052.txt` l. 187–217, *non-authoritative target*) et du calendrier `NIST IR 8547` prévoyant la dépréciation des schémas vulnérables au quantique après `2030` puis leur interdiction (*disallowed*) après `2035` au profit de schémas comme `FIPS 204` `[13]` et `FIPS 205` `[21]` (`SRC-051.txt` l. 289–291, 688–689, 778–779).
  - Constat initial : imprécis (qualifiait la transition de « programmée à l'horizon `2030–2035` », estompant la nature *non-authoritative* des cibles du `G7 CEG` dans le secteur financier et la distinction dépréciation `2030` / interdiction `2035` du `NIST` ; rectifié dans le texte).
  - Verdict final : supporté
- **C05 (`L007`)** — Amplification des tailles de signature post-quantiques : une signature `Ed25519` (`RFC 8032`, *IRTF Informational* `[15]`) mesure `64` octets (`SRC-076.txt` l. 1110), contre `3 309` octets pour `ML-DSA-65` et `4 627` octets pour `ML-DSA-87` (`NIST FIPS 204` `[13]`, `SRC-050.txt` l. 1314–1321 ; `RFC 9964` `[14]`, `SRC-012.txt` l. 199–201), soit un facteur de `52` à `72` fois avant encodage Base64url, provoquant le dépassement du plafond courant de `8 192` octets en HTTP 431 dès les premiers sauts d'une chaîne empilée.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C06 (`L009`)** — Rupture de traçabilité analogue à la `lacune 21` (Vol. 1 `1 - Compendium 2026.md` l. 10962 : corrélation trace ↔ effet), exposition de numéros d'assurance sociale (`NAS`) et courriels en télémétrie, et résolution exécutable dans `authz_pqc_audit/` vérifiée en `G0` sur doublures synthétiques hermétiques sans essai sur `SoR` réel ni portée d'avis juridique (`non-avis`).
  - Constat initial : supporté.
  - Verdict final : supporté

### Section 2.1 — Identité non humaine sans secret statique et rotation accélérée (`L013`–`L023`)

- **C07 (`L013`)** — Rappel exact du Chapitre 1 (harnais déterministe à huit étapes, épinglage `MCP` et `A2A`) et justification de la preuve d'identité, de délégation, de clé éphémère et de consentement hors bande aux frontières multi-agents.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C08 (`L017`)** — Exposition des secrets statiques partagés (variables d'environnement, certificats longs) en cas de fuite de journaux ou de conteneurs vs fondation dynamique d'une identité non humaine (`NHI`) par attestation de plateforme (`SRC-046.txt` l. 74–78 ; `SRC-047.txt` § 3.3 l. 279–294, § 5.1.4 l. 979–994).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C09 (`L017`)** — Modèle `SPIFFE` `[1]` : identifiant URI `spiffe://domaine-confiance/identifiant-charge`, document vérifiable `SVID` à courte durée de vie délivré par la `Workload API` avec *trust bundle*, et recommandation de privilégier `X.509-SVID` face au rejeu des jetons au porteur `JWT-SVID` sauf interposition d'un mandataire inverse de couche 7 (`SRC-046.txt` l. 35–86).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C10 (`L019`)** — Qualification exacte au 2 décembre 2026 de `draft-ietf-wimse-workload-identity-practices-08` (30 octobre 2026, *Internet-Draft* à vocation informative, `[2]`) : obtention fédérée sans secret statique, typage explicite des jetons, isolation des réseaux de métadonnées et limitation d'audience (`SRC-047.txt` l. 1–12, § 3.2, § 5.7).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C11 (`L019`)** — Qualification exacte de `draft-ietf-wimse-aims-01` (2 novembre 2026, *Internet-Draft* *work in progress*, *Intended status: Informational* comme `-08`, `[3]`) : décomposition d'une mission en accès limités via délégation OAuth 2.0 et protection par jetons de transaction (`SRC-048.txt` l. 1–13, § 10.1–10.2, § 10.5–10.6).
  - Constat initial : imprécis (omettait *Intended status: Informational* sur les deux brouillons WIMSE `-08` / `-01` et paraphrasait § 10.1 sans citer la décomposition en accès limités ni la délégation OAuth 2.0 ; rectifié dans le texte).
  - Verdict final : supporté
- **C12 (`L021`)** — Architecture `RATS` (`RFC 9334` `[23]`) : catégorie `Informational` (et non `Standards Track`), vocabulaire de rôles (*Attester*, *Verifier*, *Relying Party*, *Endorser*) et caractère agnostique quant au format d'encodage sur le fil (`SRC-010.txt` l. 5, § 7 l. 83–87, § 9 l. 1402–1408).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C13 (`L021`)** — Renvoi sans redondance d'audit de l'inventaire logiciel `AIBOM` (`CycloneDX 1.7` et `SPDX 3.0`) vers le `Tableau 47.3` (Vol. 1 `1 - Compendium 2026.md` l. 10763–10784) et le Chapitre 1.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C14 (`L023`)** — Calendrier `CA/B Forum` des *Baseline Requirements* TLS (`v2.3.1`, intégrant `Ballot SC-081v3` / `SC081`, `[24]`) : durée maximale de validité des certificats serveurs TLS publics ramenée à **`100` jours** le **`15 mars 2027`** puis à **`47` jours** le **`15 mars 2029`**, avec réutilisation des données de validation réduite à **`10` jours** au `15 mars 2029` (`SRC-053.txt` l. 151, 199–205).
  - Constat initial : supporté.
  - Verdict final : supporté

### Section 2.1 — Délégation OBO bornée à deux sauts, rejet *passthrough* et preuve DPoP (`L027`–`L075`)

- **C15 (`L027`)** — Matérialisation du contrat `C.5` par `authz_pqc_audit/obo_dpop.py` sous contrainte du schéma `schemas/delegated_token_claims.schema.json`, comblant l'absence sur disque du dépôt historique `Borealis-Bench/` (`G0`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C16 (`L029`)** — Structure stricte de `schemas/delegated_token_claims.schema.json` : `additionalProperties: false` et onze propriétés obligatoires à la racine (`iss`, `sub`, `aud`, `client_id`, `scope`, `authorization_details`, `act`, `cnf`, `iat`, `exp`, `jti`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C17 (`L029`)** — Fermeture structurelle de la profondeur de délégation par l'union `oneOf` entre `ActLeaf` (`^spiffe://.+`) et `ActHop2` (au plus un sous-objet `ActLeaf`), ainsi que contrainte `cnf` sur `jkt` ou `x5t#S256` (`minLength: 16`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C18 (`L031`)** — `RFC 8693` (*Standards Track*, `[4]`) : séparation entre le mandant d'origine (`sub`) et les intermédiaires techniques enregistrés dans l'objet imbriqué `act` (*actor*, `SRC-041.txt` l. 5, § 4.1 l. 674–723).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C19 (`L031`)** — `RFC 8707` (*Standards Track*, `[5]`) et `EXIG-MCP-11` : le paramètre `resource` lie chaque jeton à son audience `aud` (`SRC-009.txt` l. 54, 194–197), de sorte qu'un relais vers un autre service rompt cette liaison `[5]` et caractérise un *passage de jeton* interdit par `EXIG-MCP-11` (`MCP 2026-07-28`, `SRC-078.txt`, Chapitre 1) sous le code `TOKEN_PASSTHROUGH_AUD_MISMATCH`.
  - Constat initial : imprécis (plaçait `[5]` après `TOKEN_PASSTHROUGH_AUD_MISMATCH` comme si `RFC 8707` énonçait `EXIG-MCP-11` et ce code ; rectifié pour attribuer exactement la liaison d'audience à `[5]`, l'interdiction *passthrough* à `MCP` / `EXIG-MCP-11` et le code d'erreur à `8 - Trousse/`).
  - Verdict final : supporté
- **C20 (`L033`)** — `RFC 9449` `DPoP` (*Standards Track*, `[6]`) : liaison cryptographique du jeton d'accès via l'empreinte de clé publique dans `cnf` (`jkt`) et présentation par requête d'un en-tête `dpop+jwt` contenant `htm`, `htu`, `ath` (SHA-256 Base64url du jeton) et `jti` à usage unique (`SRC-043.txt` l. 5, 397–466, 701–707).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C21 (`L035`, `L037`–`L069`)** — `extract_act_chain` itératif à garde anti-boucle de `64` maillons (`obo_dpop.py` l. 71–81) et bloc synchronisé `G0-EX-CH02-01` (`validate_obo_delegation`, l. 85–114, condensat `sha256` vérifié dans `aq/rapports-g0.json`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C22 (`L071`)** — Implémentation des portes `S-01`, `S-03`, `SBB-SECRETS-VAULT` et du volet OBO de `C27` (`matrice-exig-prr-c40.json` où `C27` pointe d'abord sur `pqc_http431`), rejet `MISSING_NHI_ACTOR`, séparation entre la garde logicielle `isinstance(exp, bool)` dans `obo_dpop.py` contre `True == 1` en Python et les assertions effectivement couvertes par `test_authz_pqc_audit.py` (`TOKEN_EXPIRED`, `EXP_EXTENSION_FORBIDDEN`).
  - Constat initial : imprécis (prêtait à `test_authz_pqc_audit.py` un vecteur de test sur un booléen dans `exp` alors que `8 - Trousse/tests/` n'en contient aucun et que `isinstance(exp, bool)` relève d'une garde d'implémentation de `obo_dpop.py`, tout en omettant que `C27` vise prioritairement `pqc_http431` ; rectifié).
  - Verdict final : supporté
- **C23 (`L073`)** — `_check_dpop_binding` : contrôle des champs `cnf` (`jkt` ou `x5t#S256`) confrontés au champ interne `jwk_thumbprint` ou `x5t#S256` de `dpop_proof`, vérification de `typ`, `htm`, `htu`, `ath`, et enregistrement différé du `jti` dans `used_dpop_jtis` après réussite complète (`DPOP_JTI_REPLAY`, `obo_dpop.py` l. 24–68).
  - Constat initial : imprécis (mentionnait `jwk_thumbprint` ou `x5t#S256` sans distinguer le membre `cnf.jkt` de `RFC 9449` du champ Python interne `dpop_proof["jwk_thumbprint"]` ; rectifié).
  - Verdict final : supporté
- **C24 (`L075`)** — Plafond `max_hops = 2`, comparaison stricte `aud` (`RFC 8707` `[5]`) contre l'escalade horizontale, et obligation structurelle d'`authorization_details` (`RFC 9396` `[7]`, `SRC-042.txt`) vérifiée sur `C.5` par `delegated_token_claims.schema.json` en amont du contrôle métier dans `ciba_approval.py` et les politiques `OPA` du Chapitre 3.
  - Constat initial : imprécis (laissait entendre que `obo_dpop.py` vérifiait lui-même les bornes métier d'`authorization_details` selon `C.5`, alors que seul le schéma JSON `C.5` en impose la structure et que la vérification sémantique s'effectue en `C.6` et `OPA` ; rectifié).
  - Verdict final : supporté

### Section 2.1 — Automate de révocation continue SSF/CAEP et brouillon individuel (`L079`–`L083`)

- **C25 (`L079`)** — `RevocationStateMachine` (`ACTIVE`, `SUSPENDED`, `REVOKED`) et `CaepRevocationEvent` répondant à `S-14` et `C26`, adossés aux normes finales de l'OpenID Foundation publiées le `29 août 2025` : `SSF 1.0` `[10]` (`SET`, `SRC-019.txt` l. 5–14, 42–76) et `CAEP 1.0` `[11]` (`SRC-020.txt` l. 5–18).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C26 (`L081`)** — Limites de `RFC 7009` face à la révocation par agent et en cascade adressées par `draft-chen-oauth-agent-revocation-01` (30 octobre 2026, `[12]`, `POST /agent/revoke`, paramètres `agent_id`, `reason`, `cascade_depth`, `revoke_all_tokens` ; `SRC-017.txt`), explicitement marqué dans `revocation_fsm.py` par `spec_source = "IETF_INDIVIDUAL_DRAFT_AGENT_REVOCATION_01"` contre `"SSF_CAEP_FINAL"` en tant qu'*Internet-Draft individuel* non adopté par un groupe de travail IETF au `2 décembre 2026`.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C27 (`L083`)** — Irréversibilité de `REVOKED` face à `REINSTATE`, inscription dans `_revoked_jtis`, refus fermé sur `subject_spiffe` ou `jti` vide dans `assert_active` (`test_soc_killswitch_caep_revocation_terminal`) et orthogonalité vis-à-vis d'un canal de compensation distinct (`EXIG-ORC-28`).
  - Constat initial : supporté.
  - Verdict final : supporté

### Section 2.1 — Approbation hors bande CIBA, I-JSON, `C.6` et Tableau 2.1 (`L087`–`L121`)

- **C28 (`L087`)** — Approbation hors bande (*backchannel*) par `OpenID Connect CIBA Core 1.0` `[8]` (`auth_req_id`, `SBB-SIGNED-HUMAN-APPROVAL`, `SRC-045.txt` l. 1, 22, 374, 518) combinée au tableau `authorization_details` de `RFC 9396` `[7]` (`SRC-042.txt` l. 164–178).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C29 (`L089`)** — Contrat `C.6` (`approval_token_c6.schema.json`, `R-07`, `S-15`, `C24`, `EXIG-SEC-25`), séparation entre les règles `RFC 7493` `I-JSON` (*Standards Track*, `[9]`, `SRC-004.txt` § 2.1–2.2 sur surrogates UTF-8 isolés et plage entière `±(2^53 - 1)`) et le durcissement `C.6` dans `validate_ijson_strict` rejetant tout `float` (`NaN`, `Infinity`) via `IJsonError`, puis canonisation `RFC 8785` `JCS` (`utf-16-be`, `[26]`) et SHA-256.
  - Constat initial : imprécis (confondait l'interdiction `C.6` de tout `float` avec les exigences générales de `RFC 7493`, qui accepte les flottants double précision ; rectifié pour distinguer les deux niveaux).
  - Verdict final : supporté
- **C30 (`L091`–`L107`)** — Bloc synchronisé `G0-EX-CH02-02` (`compute_action_hash_h`, `ciba_approval.py` l. 106–117, empreinte `sha256` vérifiée dans `aq/rapports-g0.json`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C31 (`L109`)** — Clé `"definition_digest"` liant `outil`, `version`, `agent_id`, `task_id` et `arguments` à la définition épinglée `C.2`, et vecteur `C.6` vérifié par `test_ciba_c6_action_hash_exact_match` (`1 248 000` cents CAD = `40 × 24 960 + 12 × 20 800`, empreinte exacte `h = 92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81`).
  - Constat initial : imprécis (employait l'amorce prohibée « Il convient de souligner » signalée dans `specs/manifest.json` ; rectifié en formulation neutre).
  - Verdict final : supporté
- **C32 (`L111`)** — Schéma `schemas/approval_token_c6.schema.json` (`additionalProperties: false`) : `typ == "approbation+jwt"`, `alg` parmi `ES256`, `EdDSA`, `ML-DSA-65`, `ML-DSA-87`, `approbateur_role` dans `["tiers", "superviseur", "comite"]`, `action_sha256` sur `64` hexadécimaux minuscules et `grandeur_seuil` entière positive ou nulle (`valeur >= 0`, `unite`, `portee`).
  - Constat initial : imprécis (qualifiait `grandeur_seuil.valeur` d'« entière positive » alors que le schéma stipule `"minimum": 0` ; rectifié en « entière positive ou nulle (`valeur >= 0`) »).
  - Verdict final : supporté
- **C33 (`L113`)** — Contrôles de `verify_ciba_approval_tokens` et couverture exacte des tests : `test_reject_self_approval_by_principal_sub` valide le rejet d'auto-approbation (`sub == principal_sub`, `S-15`), `test_ciba_approval_token_valid_and_single_use` valide le rejet de `at+jwt`, du doublon d'approbateur, de la discordance d'`action_sha256` et de `task_id`, de l'expiration et du rejeu de `jti`, tandis que `_validate_single_ciba_token` rejette aussi la discordance d'`agent_id` (`ciba_approval.py` l. 77).
  - Constat initial : imprécis (attribuait l'ensemble des six classes dont l'auto-approbation et `agent_id` à la seule fonction `test_ciba_approval_token_valid_and_single_use` ; rectifié pour refléter la répartition exacte entre les deux tests et le code).
  - Verdict final : supporté
- **C34 (`L115–L117`, Tableau 2.1 ligne 1)** — Synthèse exacte de `obo_dpop.py` (`C.5`) : `RFC 8693 [4]`, `RFC 8707 [5]`, `RFC 9449 [6]` (*Standards Track*), `SPIFFE [1]`, `WIMSE -08/-01 [2, 3]` (*Internet-Drafts* *Informational*), invariants et séparation explicite entre vecteurs négatifs testés en `pytest` (`> 2` sauts, discordance `aud` / `resource` hors `RFC 8707` + `EXIG-MCP-11`, `EXP_EXTENSION_FORBIDDEN`, `TOKEN_EXPIRED`, rejeu / substitution `dpop+jwt`) et garde de code (`isinstance(exp, bool)` dans `obo_dpop.py`).
  - Constat initial : imprécis (regroupait sous « Vecteurs négatifs démontrés en `G0` » le cas `booléen dans exp`, absent de `test_authz_pqc_audit.py` ; en-tête et ligne rectifiés).
  - Verdict final : supporté
- **C35 (`L118`, Tableau 2.1 ligne 2)** — Synthèse exacte de `revocation_fsm.py` : `OpenID SSF 1.0 [10]`, `CAEP 1.0 [11]` (*Standards Track* / *Final*), `draft-chen-oauth-agent-revocation-01 [12]` (*Internet-Draft individuel*), automate `ACTIVE <-> SUSPENDED -> REVOKED`, marquage `spec_source` et distinction entre rejets prouvés en `pytest` (`REINSTATE` après `REVOKED`, contrôle de `jti` révoqué, `S-14`/`C26`) et gardes d'implémentation (`assert_active` sur `subject_spiffe` / `jti` vides et `SUSPEND` après `REVOKED`).
  - Constat initial : imprécis (annonçait « Rétrogradation après `REVOKED` ; appel sans `jti` » parmi les vecteurs démontrés par `pytest` alors que seuls `REINSTATE` et l'interrogation de `jti` révoqué sont exécutés dans `test_soc_killswitch_caep_revocation_terminal`, le reste relevant des gardes de `revocation_fsm.py` ; rectifié).
  - Verdict final : supporté
- **C36 (`L119`, Tableau 2.1 ligne 3)** — Synthèse exacte de `ciba_approval.py` (`C.6`) et statuts normatifs exacts : `OIDC CIBA 1.0 [8]` (*Final*), `RFC 9396 [7]` et `RFC 7493 [9]` (*Standards Track*), et **`RFC 8785 JCS [26]` (*Independent Submission* / *Informational*, `SRC-077.txt` l. 3, 5, 32–33, 152)**, avec empreinte `h = 92be4083...e81`, `typ == "approbation+jwt"`, quorum distinct et rejets `I-JSON`/`C.6`.
  - Constat initial : imprécis (regroupait `RFC 8785` sous `*Standards Track*` en contradiction directe avec l'en-tête et le statut de `SRC-077.txt` ; corrigé).
  - Verdict final : supporté

### Section 2.2 — Banc HTTP 431 : chaînes `O(sauts)` vs *Transaction Tokens* `-11` `O(1)` (`L125`–`L215`)

- **C37 (`L125`)** — Choc dimensionnel PQC lors de la préparation à la fenêtre `2030–2035` : cible non contraignante du `G7` (`SRC-052.txt`) et calendrier de dépréciation après `2030` puis d'interdiction après `2035` selon `NIST IR 8547` (`SRC-051.txt`), avec appui sur `FIPS 204` `[13]` et `FIPS 205` `[21]`.
  - Constat initial : imprécis (mentionnait sans qualification `(G7 / NIST IR 8547)` ; rectifié pour distinguer le statut non contraignant du `G7` et les deux seuils `2030`/`2035` de `NIST IR 8547`).
  - Verdict final : supporté
- **C38 (`L129`)** — Taille exacte d'une signature elliptique `Ed25519` (`RFC 8032` `[15]`) fixée à **`64` octets** (`SRC-076.txt` l. 1110).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C39 (`L131`)** — Paramètres exacts `NIST FIPS 204` (`[13]`, `SRC-050.txt` l. 1314–1321 ; `SRC-012.txt` l. 199–201) : `ML-DSA-65` (`3 309` octets de signature, `1 952` octets de clé publique, `4 032` octets de clé privée étendue ; `4 412` octets en Base64url, soit `~52×` `Ed25519`) et `ML-DSA-87` (`4 627` octets de signature, `2 592` octets de clé publique, `4 896` octets de clé privée étendue ; `6 170` octets en Base64url, soit `~72×` `Ed25519`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C40 (`L135`)** — Norme ratifiée `RFC 9964` (*Standards Track*, mai 2026, `[14]`) : profil `ML-DSA` pour `JOSE` et `COSE`, type de clé `AKP` (`kty = 7` en COSE) et représentation obligatoire de la clé privée `priv` par sa graine de `32` octets (`SRC-012.txt` l. 5, 135–169, 398–405).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C41 (`L136`)** — Statut exact de `draft-ietf-oauth-transaction-tokens-11` (`30 juillet 2026`, expiration `31 janvier 2027`, `[16]`) : *Internet-Draft* du groupe de travail OAuth non encore ratifié en RFC au `2 décembre 2026`, définissant les `Txn-Tokens` émis par un `TTS` et portés dans l'en-tête HTTP `Txn-Token` (`SRC-013.txt` l. 1–7, 1005–1010, 1429).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C42 (`L138`)** — Passage de `O(sauts)` à `O(1)` via `txn` et `tctx` : `[16]` définit `tctx` comme un objet JSON de contexte transactionnel immuable (`SRC-013.txt` l. 559, 607–620) et ne spécifie que le format JWT (`typ: "txntoken+jwt"`, l. 511, `0` occurrence CBOR/COSE), tandis que `pqc_http431.py` (l. 82–90, 120–145) modélise `TRANSACTION_TOKEN_JWT` sous `"typ": "txn+jwt"` avec une durée de vie de `300` s et un condensat `jcs_sha256_hex` dans `tctx`, et transpose ce motif `O(1)` en `COSE_Sign1` ML-DSA (`RFC 9964` `[14]`) pour `TRANSACTION_TOKEN_CBOR` ; garde-fous de `[16]` (`SRC-013.txt` § 13.12).
  - Constat initial : imprécis (attribuait à `[16]` la notion de condensat cryptographique dans `tctx` et ne séparait pas la spécification purement JWT de `-11` de la transposition `COSE_Sign1` opérée par `pqc_http431.py` ; rectifié).
  - Verdict final : supporté
- **C43 (`L142`)** — Implémentation `pqc_http431.py` en Python pur reposant sur `dilithium-py` (licence `MIT`) et `cbor2` (licence `MIT`), confrontée hors ligne aux vecteurs officiels `NIST FIPS 204 ACVP` (`ML-DSA-keyGen-FIPS204`, `ML-DSA-sigGen-FIPS204`, `ML-DSA-sigVer-FIPS204` dans `8 - Trousse/vectors/nist_acvp/`).
  - Constat initial : imprécis (mentionnait à tort `MIT OR Apache-2.0` pour `dilithium-py`, contredit par `dilithium_py-1.5.1.dist-info/METADATA` et `LICENSE` indiquant uniquement `MIT` ; rectifié).
  - Verdict final : supporté
- **C44 (`L144`)** — Équité algorithmique entre les six `PqcProfile` tous signés en `ML-DSA-65` ou `ML-DSA-87` (`RFC 9964`), encodage Base64url de `pub` dans `JWT_EMBEDDED_JWK`, séparation des `4` profils `O(sauts)` (`~` en JOSE ou liste CBOR) et `2` profils `O(1)` (`tctx` sur `64` hex constants), et modélisation dans `JWT_X5C_CHAIN` de l'encodage Base64 (`base64.b64encode`) d'un gabarit DER minimal (clé publique, signature ML-DSA et `4` octets de gabarit dans `pqc_http431.py` l. 127–130).
  - Constat initial : imprécis (décrivait `x5c` comme un certificat DER signé complet puis comme « l'empreinte Base64 » au lieu de l'encodage Base64 d'un gabarit DER minimal ; rectifié).
  - Verdict final : supporté
- **C45 (`L146`)** — Contrainte matérielle du seuil de `8 192` octets (`8` Kio) pour les en-têtes HTTP sur répartiteurs de charge/mandataires inverses et caractère structurel du blocage `O(sauts)`.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C46 (`L148`–`L181`)** — Critère `C27` et bloc synchronisé `G0-EX-CH02-03` (`build_signed_delegation_frame`, `evaluate_http_431`, `pqc_http431.py` l. 149–177, condensat vérifié dans `rapports-g0.json`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C47 (`L183`)** — Encodage `_b64u` des profils CBOR avant ajout du préfixe HTTP (`Authorization: Bearer ` = `22` octets, `Txn-Token: ` = `11` octets) et reproductibilité déterministe par `_SEED` et signature déterministe `dilithium-py` (`pqc_http431.py` l. 35, 61–63, 145, 170–173).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C48 (`L187`–`L196`, Tableau 2.2 lignes `ML-DSA-65`)** — Mesures exactes en octets vérifiées en `G0` sous `ML-DSA-65` (`3 309` o sig, `1 952` o pk) de `1` à `5` sauts : `JWT_EMBEDDED_JWK` (`8 298`..`41 993`, `431`), `JWT_X5C_CHAIN` (`14 139`..`71 198`, `431`), `JWT_KID_REF` (`4 793 (200)` | `9 624`..`24 468 (431)`), `CBOR_COSE_CWT` (`4 692 (200)` | `9 413`..`23 880 (431)`), `TRANSACTION_TOKEN_JWT` (`4 778 (200)` × `5`), `TRANSACTION_TOKEN_CBOR` (`4 757 (200)` × `5`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C49 (`L197`–`L204`, Tableau 2.2 lignes `ML-DSA-87`)** — Mesures exactes en octets vérifiées en `G0` sous `ML-DSA-87` (`4 627` o sig, `2 592` o pk) de `1` à `5` sauts : `JWT_EMBEDDED_JWK` (`11 193`..`56 468`, `431`), `JWT_X5C_CHAIN` (`19 380`..`97 403`, `431`), `JWT_KID_REF` (`6 551 (200)` | `13 140`..`33 258 (431)`), `CBOR_COSE_CWT` (`6 449 (200)` | `12 928`..`32 666 (431)`), `TRANSACTION_TOKEN_JWT` (`6 536 (200)` × `5`), `TRANSACTION_TOKEN_CBOR` (`6 514 (200)` × `5`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C50 (`L206`)** — Analyse du 1er constat sur le Tableau 2.2 : rupture dès le saut `1` de `JWT_EMBEDDED_JWK` et `JWT_X5C_CHAIN` dans les deux jeux `ML-DSA-65` et `ML-DSA-87` (toutes valeurs concordantes bit pour bit).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C51 (`L208`)** — Analyse du 2e constat : illusion à `1` saut puis échec HTTP 431 dès `2` sauts pour `JWT_KID_REF` et `CBOR_COSE_CWT` jusqu'à `24 468` / `23 880` o (`ML-DSA-65`) et `33 258` / `32 666` o (`ML-DSA-87`) au saut `5`.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C52 (`L210`)** — Analyse du 3e constat : invariance `O(1)` (`max - min == 0`, gain CBOR de `21` o sous `ML-DSA-65` et `22` o sous `ML-DSA-87`) vérifiée par `test_pqc_http431_vs_transaction_token_o1`, préparant l'échéancier `2030–2035` (`NIST IR 8547` : dépréciation après `2030`, interdiction après `2035`).
  - Constat initial : imprécis (mentionnait uniquement « convergence cryptographique attendue vers `2030–2035` (`NIST IR 8547`) » ; rectifié avec le calendrier exact de `SRC-051.txt`).
  - Verdict final : supporté
- **C53 (`L212`–`L215`, Figure 3)** — Concordance exacte de `diagrammes/rendus/Fig-03.svg` (`Fig-03.puml`) avec la séparation des composants déterministes `G0` (encadrés ardoise) et des deux agents probabilistes (encadrés ambre), la passerelle vérificatrice et le seuil `8 192` o sous `ML-DSA-65`/`87`, avec qualification explicite du profil CBOR-COSE comme transposition `RFC 9964` (`[14]`) du *Transaction Token* `O(1)`.
  - Constat initial : imprécis (désignait le flux interne CBOR-COSE comme « le *Transaction Token* CBOR-COSE » sans rappeler son statut de transposition `RFC 9964` distincte de `-11` JWT ; rectifié).
  - Verdict final : supporté

### Section 2.3 — Mappage OTel `v1.41.0` ↔ `semantic-conventions-genai`, caviardage PII et `Loi 25` (`L219`–`L289`)

- **C54 (`L219`)** — Double défi d'observabilité en aval : exposition de PII par journalisation brute des invites et absence de jointure vérifiable au mandat ou à l'approbation.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C55 (`L223`)** — Retrait des attributs `gen_ai.*` du dépôt central `open-telemetry/semantic-conventions` après l'étiquette `v1.41.0` du `28 avril 2026` `[17]` (laissant `v1.44+` sans référence `gen_ai.*`, comme documenté au *Cadre de Référence* Vol. 2 l. 8357, 8768) vers le dépôt dédié `open-telemetry/semantic-conventions-genai` `[18, 19]`.
  - Constat initial : imprécis (citait `v1.44+` sans renvoyer au *Cadre de Référence* qui établit la dernière étiquette `v1.44.0` ; rectifié).
  - Verdict final : supporté
- **C56 (`L227`)** — Décompte exact et statut des attributs dans les deux `gen-ai.md` : `SRC-089.txt` (`v1.41.0`, commit `e018fe6f`, `[17]`) recense `60` entrées `gen_ai.*` dont **`50` actifs en statut `Development` (incluant déjà les quatre attributs `gen_ai.agent.*`) et `10` en statut `Deprecated`** (`5` GenAI + `5` OpenAI, **`0` `Stable`**), contre **`85` attributs tous en statut `Development`** (`0` `Stable`, `0` `Deprecated`) dans `SRC-090.txt` (`@244465e9`, `31 octobre 2026`, `[18]`, ajouts couvrant notamment `gen_ai.main_agent.*`, `gen_ai.skill.*`, `gen_ai.memory.*`, les modalités multimodales, les références `*_ref` et `gen_ai.transfer.*`).
  - Constat initial : imprécis (qualifiait `v1.41.0` de « registre stable `v1.41.0` » puis attribuait à tort aux ajouts `@244465e9` les attributs `gen_ai.agent.*` déjà présents en `v1.41.0` ; rectifié avec le décompte exact `50 Development` + `10 Deprecated` et les ajouts réels `@244465e9`).
  - Verdict final : supporté
- **C57 (`L228`)** — Évolution exacte entre `v1.41.0` `[17]`, `semantic-conventions-genai@244465e9` `[18]`, `OTEL_V141_TO_GENAI_DEV_MAP` et `[19]` : renommages actifs `cache_creation` → `cache_write` et `token.type` → `token.modality` ; disparition des trois clés déjà `Deprecated` en `v1.41.0` (`gen_ai.system`, `gen_ai.usage.prompt_tokens`, `gen_ai.usage.completion_tokens`, `SRC-089.txt` l. 290–292) au profit de `provider.name`, `input_tokens`, `output_tokens` ; provenance de la règle métrique `gen_ai.client.token.usage` → `gen_ai.client.inference.usage.*` depuis le *Cadre de Référence* (Vol. 2 l. 4853, source `gen-ai-metrics.md` non archivée en `L+`) concrétisée comme clé d'adaptateur `gen_ai.client.inference.usage.input_tokens` dans `otel_pii_mapper.py` (contrat `G0`) ; et spans `create_agent`, `invoke_agent`, `execute_tool` dans les conventions GenAI du `5 novembre 2026` `[19]` (`gen-ai-agent-spans` et `execute-tool`, en `Development`, `SRC-037.txt`).
  - Constat initial : imprécis (présentait `gen_ai.client.token.usage` → `gen_ai.client.inference.usage.input_tokens` comme issu directement des tableaux `gen-ai.md` et ne distinguait pas la non-archivation `L+` de `gen-ai-metrics.md`, les attributs déjà `Deprecated` en `v1.41.0` ni les deux documents `[19]` ; rectifié).
  - Verdict final : supporté
- **C58 (`L230`)** — Encapsulation des `6` correspondances dans `OTEL_V141_TO_GENAI_DEV_MAP` (`OtelGenAiMapper`, `map_span_attributes`, `otel_pii_mapper.py` l. 123–144) et admission dans `DEFAULT_ALLOWED_ATTRS` de `mcp.method.name` ainsi que `gen_ai.client.inference.usage.input_tokens` en plus des attributs GenAI non sensibles.
  - Constat initial : imprécis (omettait de citer `gen_ai.client.inference.usage.input_tokens` aux côtés de `mcp.method.name` dans la liste d'admission complémentaire de `DEFAULT_ALLOWED_ATTRS` ; rectifié).
  - Verdict final : supporté
- **C59 (`L232`)** — Basculement `"genai_dev"` / `"v1.41.0"` restaurant sans perte les **six clés mappées** dans `OTEL_V141_TO_GENAI_DEV_MAP` (sans convertir d'autres attributs propres à `genai_dev`) et rejet silencieux des clés absentes de `DEFAULT_ALLOWED_ATTRS` pour préserver la cardinalité SRE (`otel_pii_mapper.py` l. 200–231).
  - Constat initial : imprécis (sur-affirmait que `target_dialect="v1.41.0"` « rétablit sans perte le nommage d'origine » en général au lieu de le restreindre aux six clés de correspondance ; rectifié).
  - Verdict final : supporté
- **C60 (`L234`)** — Fonction des `4` clés de `REQUIRED_MANDATE_JOIN_ATTRS` : `ca.entreprise.task_id`, `ca.entreprise.autonomy_level` (échelle `L0–L4` du Liminaire `DISC-01`), `ca.entreprise.approval.jti` (lien vers `C.6` sans exposer le nom d'approbateur) et `ca.entreprise.cost_center`.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C61 (`L238`)** — Résolution de la `lacune 21` (`C30`) dans `map_span_attributes` : exception `ValueError` bloquante sur clé de jointure absente/vide ou sur préfixe `enterprise.`/`otel.` (`EXIG-OBS-06`, `otel_pii_mapper.py` l. 208–215).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C62 (`L240`)** — Minimisation `EXIG-OBS-07` à deux couches : liste fermée `DEFAULT_ALLOWED_ATTRS`, purge des `9` attributs bruts (`FORBIDDEN_RAW_CONTENT_ATTRS`, `otel_pii_mapper.py` l. 100–112) et exclusion de toute clé contenant `approver` ou `approbateur` (`l. 175, 219`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C63 (`L242`)** — Appui exclusif sur `LQ 2021, c. 25` (`SRC-063`, sanctionnée le `22 septembre 2021`) sous discipline `DC-01` et clause `non-avis` (`AO-05`), la version consolidée `P-39.1` sur LégisQuébec étant en `statut F` (`HTTP 403`, `registre-statut-f.json`, `AO-01`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C64 (`L244`)** — Entrée en vigueur le **`22 septembre 2023`** (`LQ 2021, c. 25`, art. `110` et art. `175`) de l'article `12.1` encadrant toute décision fondée exclusivement sur un traitement automatisé (avis au plus tard lors de la décision, communication sur demande des renseignements utilisés, motifs, principaux paramètres déterminants et droit de rectification, formulation d'observations auprès d'un membre du personnel habilité à réviser la décision ; `SRC-063.txt` l. 1542–1555, 2489).
  - Constat initial : imprécis (précisé sur l'échéance de notification, l'article `175` et le droit de rectification de `SRC-063.txt`, tout en reformulant sans collision `CA-03` avec les volumes antérieurs ; rectifié).
  - Verdict final : supporté
- **C65 (`L246`)** — Plafonds répressifs (`LQ 2021, c. 25`, art. `159` et `160` édictant les art. `90.12` et `91`, `SRC-063.txt` l. 2283–2287, 2327–2333) : hors personne physique, sanctions administratives pécuniaires plafonnées au plus élevé de `10 millions CAD` (`10 M CAD`) et `2 %` du chiffre d'affaires mondial de l'exercice financier précédent, et amendes pénales jusqu'au plus élevé de `25 millions CAD` (`25 M CAD`) et `4 %` de ce chiffre d'affaires mondial.
  - Constat initial : imprécis (utilisait « revenus mondiaux » au lieu de « chiffre d'affaires mondial de l'exercice financier précédent » et omettait la référence explicite à l'article `91` ; rectifié).
  - Verdict final : supporté
- **C66 (`L250`)** — Caviardage déterministe `redact_pii_bilingual` (`EXIG-OBS-09`, `O-02`) : `7` motifs ordonnés (`BEARER_JWT`, `IBAN`, `PAYMENT_CARD`, `EMAIL`, `RAMQ`, `PHONE`, `NAS_SIN`) remplacés par `[CATEGORIE:hex12]` via HMAC-SHA256 tronqué à `12` hexadécimaux (`otel_pii_mapper.py` l. 146–171, 244–254).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C67 (`L252`–`L287`)** — Bloc synchronisé `G0-EX-CH02-04` (`map_span_attributes` et `redact_pii_bilingual`, `otel_pii_mapper.py` l. 235–265, empreinte `sha256` vérifiée dans `aq/rapports-g0.json`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C68 (`L289`)** — Ordre de `_PII_PATTERNS` (`PHONE` avant `NAS_SIN`), protection `HMAC-SHA256` contre les tables arc-en-ciel avec corrélation intra-session (`test_pii_redaction_bilingual_and_drop_raw_content`) et limite assumée sur les noms propres libres justifiant `EXIG-OBS-07`.
  - Constat initial : supporté.
  - Verdict final : supporté

### Section 2.4 — Chaîne `JCS` + `SCITT`, `SLH-DSA` et calculateur `CPO` / `FOCUS v1.4` (`L293`–`L345`)

- **C69 (`L293`)** — Couloir 2 répondant à `EXIG-OBS-12`, `G-15`, `O-09`, `SBB-IMMUTABLE-AUDIT-LEDGER`, `C20`, `C38`, `C39` et intégrant `CAP-046` (`matrice-exig-prr-c40.json`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C70 (`L297`)** — `AuditChainLedger` (`audit_scitt_focus.py`, contrat `C.8`, `schemas/audit_record_c8.schema.json`) : nature `"intention"` / `"issue"`, `sequence >= 1`, `flux` et racine de genèse `"sha256:" + "0"*64` pour `precedent_sha256`.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C71 (`L299`)** — Structure exacte d'`enregistrement` dans `audit_record_c8.schema.json` : `12` propriétés obligatoires à la racine (`flux`, `horodatage`, `nature`, `sequence`, `intention_sequence`, `precedent_sha256`, les `5` éléments d'`EXIG-OBS-12` — `mandant` incluant `type`, `agent` incluant `id`/`identite`/`invite_systeme`/`version`, `action` incluant `definition_version` et `issue`, `modele`, `autorite` incluant `classe_risque`/`controle` — ainsi que le bloc `correlation`).
  - Constat initial : imprécis (indiquait `version` au lieu de `definition_version` dans `action`, puis classait à tort `correlation` parmi les `5` éléments d'`EXIG-OBS-12` en laissant `modele` en dehors ; rectifié selon `2 - Cadre de Référence.md` l. 4921 et `audit_record_c8.schema.json`).
  - Verdict final : supporté
- **C72 (`L301`)** — Canonisation `RFC 8785` (`[26]`, `harness_proto/jcs.py`), validation des `20` fichiers de `vectors/rfc8785/` (`Annexe B` IEEE-754 avec rejet `NaN`/`Infinity`, tri UTF-16 astral, `6` paires `cyberphone/json-canonicalization`) et détection d'altération `broken_sequence` (`1` puis `2`) dans `test_audit_chain_tamper_detection`.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C73 (`L305`)** — Architecture `SCITT` `RFC 9943` `[20]` (*Standards Track*, juin 2026) : journal en ajout seul muni d'une structure de données vérifiable (`VDS`) sans imposer de `VDS` unique et délivrant des reçus cryptographiques d'inclusion `COSE` (`RFC 9942`, `SRC-044.txt` l. 5–11, 108–116, `0` occurrence de *Merkle*).
  - Constat initial : imprécis (attribuait directement à `RFC 9943` `[20]` un « arbre de Merkle » alors que `SRC-044.txt` spécifie un `VDS` abstrait sans imposer Merkle et que l'instanciation par arbre binaire de Merkle relève de `audit_scitt_focus.py` ; rectifié).
  - Verdict final : supporté
- **C74 (`L307`)** — Implémentation Merkle `SCITT` dans `audit_scitt_focus.py` : préfixes de domaine `0x00` (feuilles) et `0x01` (nœuds internes), vérification `O(log N)` et cas `pytest` (`ValueError` sur liste vide, preuve vide sur `total = 1`, `5` feuilles non puissance de deux, rejet de feuille substituée ou fausse racine ; `test_scitt_merkle_inclusion_and_slh_dsa_seal`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C75 (`L309`)** — `SLH-DSA` `NIST FIPS 205` `[21]` (`13 août 2024`) : schéma sans état reposant exclusivement sur les propriétés de sécurité des fonctions de hachage (`SRC-018.txt` l. 12, 44).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C76 (`L311`)** — Structure `FORS` / hyperarbre `XMSS` / `WOTS+` et paramètres exacts `FIPS 205` (`SRC-018.txt` l. 2481–2501) : `SLH-DSA-SHA2-128s` (`h = 63, d = 7, h' = 9, a = 12, k = 14`, signature `7 856` octets, clé publique `32` octets) retenu par `seal_merkle_root` contre `SLH-DSA-SHA2-128f` (`h = 66, d = 22, h' = 3, a = 6, k = 33`, signature `17 088` octets).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C77 (`L313`)** — Interdiction `SPDX` du paquet copyleft *slh-dsa* (`LGPL-3.0-or-later`) en `G0` (`execute_g0.py`, `spdx-allowlist.json`), implémentation `MIT` autonome `slh_dsa_fips205.py` sur `hashlib` et `hmac`, et vérification bit à bit sur les vecteurs `NIST ACVP` (`SLH-DSA-keyGen/sigGen/sigVer-FIPS205`), validant `G-15` et `C38`.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C78 (`L317`–`L321`)** — Définition du **Coût par résultat conforme** (`CPO`) par le rapport entre la somme des `EffectiveCost` engagés et `compliant_outcomes >= 1`.
  - Constat initial : supporté.
  - Verdict final : supporté
- **C79 (`L323`)** — `compute_cpo_and_focus` et spécification `FOCUS v1.4` (`4 juin 2026`, `[22]`, `manifeste-sources-sha256.json`), validation sous `focus_carbon_record.schema.json` (`10` colonnes normalisées de `FOCUS v1.4` + colonne héritée `ProviderName` conservée au schéma bien que remplacée dans `FOCUS` depuis `v1.3` par `ServiceProviderName`/`HostProviderName` selon `SRC-023.txt` l. 5237 + extensions obligatoires de trousse `x_carbon_gco2e` et `x_energy_kwh`, mécanisme `x_` de `FOCUS`, capacité `CAP-046`, porte `O-09`, critère `C39`).
  - Constat initial : imprécis (présentait `11` colonnes comme toutes normalisées dans `FOCUS v1.4`, alors que `ProviderName` a été retirée de `FOCUS` en `v1.3` et n'est conservée que comme champ hérité dans `focus_carbon_record.schema.json` ; rectifié).
  - Verdict final : supporté
- **C80 (`L325`)** — Calcul `Decimal` exact via `_to_decimal` (`float`/`bool` -> `TypeError`, négatif/non fini -> `ValueError`), agrégat `FocusCpoSummary` et résultats `pytest` vérifiés (`0,10 + 0,20 = 0,30` CAD et `CPO = 0,15` CAD sur `2` résultats conformes ; `compliant_outcomes = 0` -> `ValueError` ; `test_focus_cpo_and_budget_ceiling_decimal` et `test_focus_carbon_cap046_fields`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C81 (`L327`–`L333`, Tableau 2.3)** — Synthèse comparative des deux couloirs : statut `OTel v1.41.0` (`60` entrées `gen_ai.*` : `50 Development`, `10 Deprecated`, `cache_creation`) `[17]` ↔ `@244465e9` (`85` attr. `Development`, `cache_write`) `[18]`, `gen-ai-agent-spans` et `execute-tool` `[19]`, `LQ 2021, c. 25` (`12.1`) `[25]`, `RFC 8785` (*Independent Submission*) `[26]`, `RFC 9943` `[20]` (`VDS` SCITT instancié en arbre Merkle), `FIPS 205` `[21]`, `5` éléments `EXIG-OBS-12` (`mandant`, `agent`, `action`, `modele`, `autorite`) + `correlation`, et `FOCUS v1.4` (`10` col. + `ProviderName` héritée) `[22]`.
  - Constat initial : imprécis (écrivait `60 attr.` sans détailler `50 Development, 10 Deprecated`, omettait `execute-tool` et `Independent Submission` sur `RFC 8785`, classait `correlation` parmi les `5` blocs d'`EXIG-OBS-12` au lieu de `modele`, et n'explicitait ni le `VDS` SCITT ni la colonne héritée `ProviderName` ; rectifié).
  - Verdict final : supporté
- **C82 (`L335`–`L338`, Figure 4)** — Concordance de `diagrammes/rendus/Fig-04.png` (`Fig-04.mmd`) avec la séparation au harnais entre inférence probabiliste et les deux couloirs convergents sur `CPO` / `FOCUS v1.4` (`CAP-046`).
  - Constat initial : supporté.
  - Verdict final : supporté
- **C83 (`L340`–`L341`, Encadré invariant 1)** — Synthèse vérifiable de l'invariant 1 : rejet *passthrough* (`TOKEN_PASSTHROUGH_AUD_MISMATCH`, `EXIG-MCP-11` / `RFC 8707`), `OBO` `<= 2` sauts + `DPoP`, automate irréversible `SSF`/`CAEP`, et `CIBA` (`approbation+jwt`, règle `C.6` sans `float` sur `I-JSON`, `definition_digest`, `h = 92be4083...`).
  - Constat initial : imprécis (n'explicitait ni l'association `EXIG-MCP-11` / `RFC 8707` ni le renforcement `C.6` sans `float` sur `I-JSON` ; rectifié).
  - Verdict final : supporté
- **C84 (`L342`, Encadré invariant 2)** — Synthèse vérifiable de l'invariant 2 : `ML-DSA-65` (`3 309` o) et `ML-DSA-87` (`4 627` o) (`RFC 9964` / `FIPS 204`), seuil `8 192` o, invariance `O(1)` des *Transaction Tokens* (modélisés en JWT sur `draft-ietf-oauth-transaction-tokens-11` et transposés en CBOR-COSE selon `RFC 9964` : `4 757` / `4 778` o vs `6 514` / `6 536` o).
  - Constat initial : imprécis (regroupait CBOR-COSE directement sous `-11` sans rappeler la transposition `RFC 9964` ; rectifié).
  - Verdict final : supporté
- **C85 (`L343`, Encadré invariant 3)** — Synthèse vérifiable de l'invariant 3 : mappage `otel_pii_mapper.py` entre `OTel v1.41.0` (`60` entrées `gen_ai.*` : `50 Development` et `10 Deprecated`) et `semantic-conventions-genai` (`85` attributs `Development`, `cache_write`), `4` clés `lacune 21`, purge des `9` champs bruts, caviardage `FR/EN` HMAC-SHA256, chaîne `C.8`, preuves Merkle d'un `VDS` `SCITT` (`RFC 9943`), `SLH-DSA` (`FIPS 205`, implémentation `MIT` ACVP) et `CPO` / `FOCUS v1.4` (`Decimal`).
  - Constat initial : imprécis (désignait `v1.41.0` par « `60` attributs » sans en rappeler la répartition `50 Development` / `10 Deprecated` et omettait le rôle du `VDS` `SCITT` avant l'arbre de Merkle ; rectifié).
  - Verdict final : supporté
- **C86 (`L345`)** — Transition exacte vers la Partie II / Chapitre 3 (`Chapitre 03 - Politiques OPA hors modele et Sagas.md` : `OPA / Rego` fermé par défaut `default allow := false`, `Règle de deux`, propagation `CaMeL`, manifestes de confinement, garde `Decimal` et orchestrateur Saga à `10` fautes dans `test_saga_10_faults.py`).
  - Constat initial : supporté.
  - Verdict final : supporté

---

## Traçabilité complète du dossier fermé de sources (`26/26`) et des preuves `G0`

| Citation | Identifiant | Document primaire vérifié (`corpus_l_plus/`) | Statut normatif / date | Emploi vérifié |
|---|---|---|---|---|
| `[1]` | `SRC-046` | SPIFFE Concepts (`Workload Identity`, `SVID`, `Workload API`) | Spécification ouverte CNCF (`2026`) | Supporté |
| `[2]` | `SRC-047` | `draft-ietf-wimse-workload-identity-practices-08` | *Internet-Draft* IETF WG (`2026-10-30`) | Supporté |
| `[3]` | `SRC-048` | `draft-ietf-wimse-aims-01` | *Internet-Draft* IETF WG (`2026-11-02`) | Supporté |
| `[4]` | `SRC-041` | `RFC 8693` (*OAuth 2.0 Token Exchange*) | IETF *Standards Track* (`2020-01`) | Supporté |
| `[5]` | `SRC-009` | `RFC 8707` (*Resource Indicators for OAuth 2.0*) | IETF *Standards Track* (`2020-02`) | Supporté |
| `[6]` | `SRC-043` | `RFC 9449` (*OAuth 2.0 DPoP*) | IETF *Standards Track* (`2023-09`) | Supporté |
| `[7]` | `SRC-042` | `RFC 9396` (*OAuth 2.0 RAR*) | IETF *Standards Track* (`2023-05`) | Supporté |
| `[8]` | `SRC-045` | *OpenID Connect CIBA Flow — Core 1.0* | OpenID *Final* (`2021-09-01`) | Supporté |
| `[9]` | `SRC-004` | `RFC 7493` (*The I-JSON Message Format*) | IETF *Standards Track* (`2015-03`) | Supporté |
| `[10]` | `SRC-019` | *OpenID Shared Signals Framework (SSF) 1.0* | OpenID *Final* (`2025-08-29`) | Supporté |
| `[11]` | `SRC-020` | *OpenID Continuous Access Evaluation Profile (CAEP) 1.0* | OpenID *Final* (`2025-08-29`) | Supporté |
| `[12]` | `SRC-017` | `draft-chen-oauth-agent-revocation-01` | *Internet-Draft* individuel (`2026-10-30`) | Supporté |
| `[13]` | `SRC-050` | `NIST FIPS 204` (*ML-DSA*) | Norme NIST (`2024-08-13`) | Supporté |
| `[14]` | `SRC-012` | `RFC 9964` (*ML-DSA for JOSE and COSE*) | IETF *Standards Track* (`2026-05`) | Supporté |
| `[15]` | `SRC-076` | `RFC 8032` (*EdDSA / Ed25519*) | IRTF *Informational* (`2017-01`) | Supporté |
| `[16]` | `SRC-013` | `draft-ietf-oauth-transaction-tokens-11` | *Internet-Draft* OAuth WG (`2026-07-30`, exp. `2027-01-31`) | Supporté |
| `[17]` | `SRC-089` | `open-telemetry/semantic-conventions@v1.41.0` (`gen-ai.md`) | Tag `e018fe6f` (`2026-04-28`) ; `50` *Dev*, `10` *Dep* | Supporté |
| `[18]` | `SRC-090` | `open-telemetry/semantic-conventions-genai@244465e9` (`gen-ai.md`) | Commit `244465e9` (`2026-10-31`) ; `85` *Dev* | Supporté |
| `[19]` | `SRC-037` | OTel GenAI `agent-spans`, `execute-tool` & `registry.yaml` | *Development* (`2026-11-05`) | Supporté |
| `[20]` | `SRC-044` | `RFC 9943` (*SCITT Architecture*) | IETF *Standards Track* (`2026-06`) | Supporté |
| `[21]` | `SRC-018` | `NIST FIPS 205` (*SLH-DSA*) | Norme NIST (`2024-08-13`) | Supporté |
| `[22]` | `SRC-023` | `FOCUS v1.4` (*FinOps Open Cost & Usage Spec*) | Release `v1.4` (`2026-06-04`) | Supporté |
| `[23]` | `SRC-010` | `RFC 9334` (*RATS Architecture*) | IETF *Informational* (`2023-01`) | Supporté |
| `[24]` | `SRC-053` | *CA/B Forum TLS Baseline Requirements v2.3.1* (`SC-081v3`) | Spécification CA/BF (`2026-10-04`) | Supporté |
| `[25]` | `SRC-063` | `LQ 2021, c. 25` (*Loi 25*, art. `12.1`, `90.12`, `91`) | Loi modificatrice Québec (`2021-09-22` ; v. `2023-09-22`) | Supporté |
| `[26]` | `SRC-077` | `RFC 8785` (*JSON Canonicalization Scheme*) | *Independent Submission* / *Informational* (`2020-06`) | Supporté |

### Vérification directe des preuves `G0` exécutées en session d'audit

- **`pytest` complet (`8 - Trousse/.venv/Scripts/python.exe -B -m pytest "8 - Trousse/tests" -v`)** : `83 passed in 18.79s` (`0 failed`, `0 skipped` sur `test_authz_pqc_audit.py`, `test_evalops_prr.py`, `test_harness_proto.py`, `test_policy_saga.py`, `test_saga_10_faults.py`, `test_third_party_vectors.py`).
- **Tests OPA complets (`8 - Trousse/.tools/opa.exe test "8 - Trousse/policies_opa" -v` et `--coverage`)** : `PASS: 45/45` et `covered_lines = 585`, `not_covered_lines = 0`, `coverage = 100`.
- **Contrôles numériques et schémas `G0` en séance** : exécution directe de `pqc_http431.evaluate_http_431` (concordance bit à bit du Tableau 2.2), `ciba_approval.compute_action_hash_h` (`92be40835a73023d117ebb4965da82dfa05e2e6d647d0919d53461289bbc6e81`), métadonnées `dilithium-py 1.5.1` (`MIT`) et `cbor2 6.3.0` (`MIT`), `aq/rapports-g0.json` (`overall_status = PASS`, `exit_code = 0`, `spdx_check.passed = true`, `SHA-256` exacts pour `G0-EX-CH02-01` à `G0-EX-CH02-04`).
- **Re-vérification `G1` finale post-rectification (`C:\Python314\python.exe -B "8 - Manuel/outils/verifie_manuscrit.py" --unit ch02 --strict`)** : `exit 0` (`OK : Barriere deterministe G1 passee avec 0 erreur.`, `8 898` mots lexicaux `CA-03` / `9 847` `split()`).
