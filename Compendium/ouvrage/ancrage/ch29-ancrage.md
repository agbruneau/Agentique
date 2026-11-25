# Journal d'ancrage atomique Wyvern G2 — Chapitre 29 (`ch29`)

- **Unité auditée :** `Compendium/ouvrage/manuscrit/10 - Partie X/Chapitre 29.md` (`4 645` mots `verifie_manuscrit` / `4 878` mots `parser_plan`, plage `[4 251, 4 989]`)
- **Base documentaire fermée :** `Compendium/ouvrage/sources/ch29-sources.md` (`[1]`–`[8]` en statut `L+`, `2` exclusions `statut F`) ; textes intégraux `Compendium/ouvrage/recherche/corpus_l_plus/SRC-*.txt` ; registres `Compendium/ouvrage/registre/*.json` ; protocole `Compendium/ouvrage/specs/protocole-mlr-compendium.json` (`MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0`) ; barrière `G0` (`Compendium/ouvrage/aq/rapports-g0.json`) et code de la trousse `Tomes/Tome 8 .../trousse/` ; index heuristique interne `Corpus/Tome 1..8*.md` (`AO-02`)
- **Date de référence et de gel :** `2026-12-02` (`2 décembre 2026`)
- **Auditeur indépendant (`AO-07`) :** `wyvern-b4-8`
- **Passe G2 initiale (supportés)** : 13
- **Rectifications appliquées lors de la passe G2 :** 23
- **Verdict final — supportés :** 36 / 36 (100,0 %)

---

## 1. Synthèse des rectifications appliquées dans `Chapitre 29.md`

Toutes les formulations divergentes, sur-affirmées ou insuffisamment attribuées relevées lors de la passe initiale ont été réancrées ou reformulées directement dans [Chapitre 29.md](file:///c:/Github/Agentique/Compendium/ouvrage/manuscrit/10%20-%20Partie%20X/Chapitre%2029.md), sans altérer les invariants `CA-01`..`CA-22`, en préservant les `owned_concepts` (`blueprints-reference-multisectoriels`, `blueprint-1-assistant-sor`, `blueprint-2-enclave-rag-acl`, `blueprint-3-maillage-b2b`, `fil-rouge-groupe-boreal-bel`, `federation-multi-plateformes-gravite`, `reprise-sinistre-cognitif-continuite`, `reseaux-b2b-federes-p3`), l'ensemble des renvois `[1]`–`[8]` et le calibrage (`4 645` / `4 878` mots dans `[4 251, 4 989]`) :

1. **Socle `C1–C8`, `565` exigences et neutralité fournisseur (`L7`, `L13`, `L15`, `L74`, `L78`) :** clarification du statut des `565` exigences de contrôle en tant qu'illustration d'un cadre d'éditeur en couche `C8` (`IBM Cloud Framework for Financial Services`, distinct de `BSIF B-13`, `Tome 1 § 45.1–45.4`) ; attribution systématique du nom de l'éditeur (`IBM`) devant les briques d'illustration, ajout des statuts datés (`ContextForge` annoncé sans disponibilité générale établie, `IBM MQ 9.4 LTS` à cryptographie `TLS 1.3` `ML-KEM` auto-déclarée et non vérifiée, `IBM Instana` en préversion publique, `IBM Sovereign Core` en disponibilité générale du `5 mai 2026`).
2. **Trousse du Tome 8, `5 SBB`, `prr_validators.py` et rapport `G0` (`L17`–`L26`, `Tableau 29.1`, `L83`, `L135`, `L143`) :** correction du chemin réel de `policy_saga/opa_runner.py` (au lieu de `policies_opa/opa_runner.py`) agissant avec `policies_opa/rule_of_two.rego` ; séparation stricte entre `validate_blueprints_and_c40` (`REQUIRED_BLUEPRINT_IDS`, `REQUIRED_5_SBB_SLOTS`, `C01–C40`) et les validateurs utilisant les schémas JSON `Draft 2020-12` (`prr_24_evidence.schema.json`, `adr_2027_b001.schema.json`, `sandbox_manifest.schema.json`) ; distinction entre les `45/45` tests `OPA` (`100,0 %` sur les trois politiques `.rego`, `aq/rapports-g0.json`) et l'ancrage Rego `default allow := false` (`[7]`, `SRC-087.txt`).
3. **Détails protocolaires `MCP`, `Firecracker` et critères `bp3` (`L42`, `L52`, `L60`–`L62`, `Tableau 29.2`) :** séparation entre les exigences de `SRC-072.txt` `[4]` (schémas, annotations non fiables, en-têtes `Mcp-Method`/`Mcp-Name`) et le mode *Stateless Streamable HTTP* imposé en `G0` (`DISC-05`) ; qualification des seuils `Firecracker` (`≤ 125 ms`, `< 5 MiB`, `> 95 %` CPU) comme spécifications rapportées au cadre (`Tome 6 § 14.3.4`, hors corpus `L+` fermé de ce chapitre) ; réindexation des critères de `bp3` selon `Tome 6 Tableau B.2` et la matrice SSOT (`C13` `A2A`, `C14` `AGNTCY`/`SLIM`, `C20` `CloudEvents`/`AsyncAPI`, `C27` `OBO`) avec ajout des renvois `[2]` (`SSRF`, `CancelTask`).
4. **Reprise `Cognitive DR` (`ADR-027`), `BSIF E-23` et sas `B2B` `POR-013` (`L101`, `L105`, `L110`, `L114`, `L118`, `L123`) :** qualification de `RTO < 15` minutes, du seuil `pass^5_DR ≥ 0,94 · pass^5_nominal` et du plancher `0,90` comme cibles de conception internes `ADR-027` sans source externe (`Tome 3 § 46.11–46.13`) ; retrait de l'attribution textuelle à `BSIF E-23` `[5]` du délai de `15` minutes et de l'exercice annuel de débranchement, en les reliant comme instrumentation cible des attentes de résilience et de gestion des tiers (`E-23` `[5]` / `B-10`) ; précision des domaines `D2` (conseil, vente et convenance) et `D6` (conformité, LBC et gestion des risques), et ajout de `CAP-014` avec `EXIG-INT-22`/`ADR-026` sur le rapprochement tripartite.
5. **`Borealis-Bench` et exclusion probante `DC-P11`/`DC-P12` (`L7`, `L83`, `L135`–`L143`) :** rectification du décompte de `Borealis-Bench` consigné au Corpus (`Tome 3`, hors dépôt local : `108/108` blocs syntaxiquement valides, dont `90` exécutés en CI incluant `9` modules Python à assertions comportementales et l'Extrait `47.7`, et `18` schémas conceptuels), couplé aux preuves locales exécutées en `G0` dans la trousse du Tome 8 (`aq/rapports-g0.json`), et précision de l'intitulé `Data Act` pour le règlement européen sur les données (`L137`).

---

## 2. Inventaire atomique et confrontation aux sources `L+` (`C29-01` à `C29-36`)

### Section 29.0 — Titre, question directrice et résumé (`L1–L7`)

- **C29-01 (`L1`, `L3`)** — *Affirmation :* Titre et question directrice encadrant l'assemblage du noyau de contrôle possédé en trois blueprints normalisés validables mécaniquement sur `C01–C40` et `5 SBB`, la fédération multi-SaaS, la reprise `Cognitive DR` et la séparation entre le fil rouge `Groupe Boréal` et `Borealis-Bench`.
  - **Appui vérifié :** `specs/manifest.json` (`ch29`, `D10`, `SUB_D10_02`), `registre/matrice-exig-prr-c40.json` (`c01_c40_blueprints`, `cinq_sbb`, `ADR-015`, `ADR-027`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-02 (`L5`)** — *Affirmation :* Concrétisation de l'architecture de référence en trois blueprints sectoriels instanciables : `bp1_assistant_interne` (assistant transactionnel sur `SoR`), `bp2_rag_entreprise_acl` (enclave souveraine à recherche augmentée filtrée par habilitations) et `bp3_orchestration_multi_agents_b2b` (maillage multi-agents fédéré).
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`c01_c40_blueprints`), `Tomes/Tome 8 .../trousse/evalops_prr/prr_validators.py` (`REQUIRED_BLUEPRINT_IDS`, `L47–L51`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-03 (`L7`)** — *Affirmation :* Plan en trois volets : modèles en huit couches `C1–C8` (illustré par un portefeuille complet à `565` exigences en `C8`) et validation `G0` sur les `5 SBB` du `Tableau 12` et `C01–C40` ; fédération `SaaS` (`ADR-015`), `Cognitive DR` cible `15` min (`ADR-027`) et verrous `B2B` Palier 3 (`POR-013`) ; fil rouge `Groupe Boréal Inc.` (`BEL`, `BCA`, `BSN`) sous exclusion `DC-P11`/`DC-P12` substituant `Borealis-Bench` (`108` blocs CI consignés au Corpus) et les preuves exécutables du Tome 8.
  - **Appui vérifié :** `Corpus/Tome 1` (`L10368`), `Corpus/Tome 3` (`L320`, `L14574`, `L24480`), `registre/matrice-exig-prr-c40.json` (`cinq_sbb`, `POR-013`), `aq/rapports-g0.json`.
  - **Passe initiale :** écart rectifié · **Action :** qualifié l'illustration à `565` exigences en `C8`, qualifié `15` min de cible, rattaché `108` blocs `Borealis-Bench` au Corpus et ajouté les preuves du Tome 8 · **Verdict : supporté**

### Section 29.1.1 — Socle `C1–C8`, six principes et correspondance `G0` (`L11–L31`, Tableau 29.1)

- **C29-04 (`L13`)** — *Affirmation :* Assemblage sur huit strates (`C1–C8`) ancré dans sept repères réglementaires canadiens et québécois (`BSIF E-23` `[5]`, `BSIF B-13`, profil `AMF IA`, `Loi 25` art. `12.1` `[6]`, `ACVM 11-348`, cadre bancaire ouvert, rails de paiement canadiens) et six principes directeurs (`Tableau 45.1` du Tome 1) : `OO3`/`OO4`, passerelle de politiques, republication des contrats, résidence canadienne illustrée en `C8` par un cadre d'éditeur à `565` exigences, traçabilité hors agents et gouvernance continue des modèles.
  - **Appui vérifié :** `SRC-065.txt` (`[5]`), `SRC-063.txt` (`L1542`, `[6]`), `Corpus/Tome 1` (`Tableau 45.1`, `L10338–L10348` ; `Tableau 45.3`, `L10400–L10408`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché le cadre à `565` exigences au statut d'illustration d'éditeur en `C8` et scindé la phrase pour respecter `CA-05` · **Verdict : supporté**

- **C29-05 (`L15`)** — *Affirmation :* Sous règle de neutralité fournisseur (`Tome 1 § 45.3`), référence datée aux composants IBM sur `C1–C8` avec leur statut (`IBM API Connect` `v10.0.8` GA, `IBM ContextForge` annoncé sans GA établie, `IBM App Connect Enterprise` `v13.0`, `IBM MQ 9.4 LTS` avec `TLS 1.3` `ML-KEM` auto-déclaré et non vérifié, `IBM Data Fabric`, `IBM watsonx Orchestrate`/`IBM Granite 4.0`, `IBM watsonx.governance` GA, `IBM Instana` en préversion publique, `IBM Sovereign Core` GA du `5 mai 2026`), absence de revendication `E-23`/`B-13`, non-équivalence des `565` exigences avec `B-13` et rôle limité d'opérateur des rails de paiement canadiens.
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 45.2` `Tableau 45.2`, `L10355–L10369` ; `§ 45.3`, `L10382–L10388` ; `§ 45.4` `Tableau 45.3`, `L10394–L10408` ; `§ 45.9`, `L10478`).
  - **Passe initiale :** écart rectifié · **Action :** nommé `IBM` devant chaque composant, ajouté les statuts datés et la mention auto-déclarée/non vérifiée de `MQ 9.4 LTS`, explicité que `565` exigences ≠ `B-13`, et scindé la phrase selon `CA-05` · **Verdict : supporté**

- **C29-06 (`L17`)** — *Affirmation :* Matérialisation des `5 SBB` laissés sans exemple au `Tableau 12` : trois dans le `Plan A` (`secrets_vault` via `authz_pqc_audit/obo_dpop.py` sans secret statique ; `guardrails_engine` via `policy_saga/opa_runner.py` + `policies_opa/rule_of_two.rego` ; `signed_human_approval_service` via `authz_pqc_audit/ciba_approval.py`) et deux dans le `Plan B` (`immutable_audit_ledger` via `authz_pqc_audit/audit_scitt_focus.py` ; `finops_budget_quota_controller` via `policy_saga/decimal_money.py` + `audit_scitt_focus.py`).
  - **Appui vérifié :** `Corpus/Tome 2` (`Tableau 12`, `L1360–L1361`), `registre/matrice-exig-prr-c40.json` (`cinq_sbb`), arborescence réelle `Tomes/Tome 8 .../trousse/policy_saga/opa_runner.py` et `policies_opa/rule_of_two.rego`.
  - **Passe initiale :** écart rectifié · **Action :** corrigé le chemin réel `policy_saga/opa_runner.py` (en notant l'emploi de `policies_opa/rule_of_two.rego`) et scindé le paragraphe selon `CA-05` · **Verdict : supporté**

- **C29-07 (`L19`)** — *Affirmation :* Dans `evalops_prr/prr_validators.py`, `validate_blueprints_and_c40` vérifie via `REQUIRED_BLUEPRINT_IDS` et `REQUIRED_5_SBB_SLOTS` le renseignement des `5 SBB` et la couverture `C01–C40` ; les validateurs voisins s'appuient sur les schémas JSON `Draft 2020-12` (`prr_24_evidence.schema.json`, `adr_2027_b001.schema.json`, et `sandbox_manifest.schema.json` dans `policy_saga/sandbox_manifest.py`) ; `aq/rapports-g0.json` atteste au `2 décembre 2026` `83/83` `pytest`, `50/50` vecteurs tiers et `45/45` tests `OPA` à `100,0 %` sur les trois politiques `Rego` en mode fermé (`default allow := false` `[7]`).
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/evalops_prr/prr_validators.py` (`L39–L167`), `aq/rapports-g0.json` (`L11–L75`), `SRC-087.txt` (`L2079`, `L2103`, `L3302`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié `validate_blueprints_and_c40` des validateurs sur schémas JSON `Draft 2020-12`, corrigé `45/45 règles OPA` en `45/45 tests OPA`, et rattaché `[7]` à `default allow := false` et les métriques à `aq/rapports-g0.json` · **Verdict : supporté**

- **C29-08 (`L21`)** — *Affirmation :* Le contrôle de cohérence interne (`Tome 1 § 45.15`) exige la continuité du cycle de vie complet (naissance, vie `RFC 8693`/OTel/rotation/PQC, révocation propagée sans délai pour préserver l'imputabilité de l'archive).
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 45.8–45.10`, `L10452–L10494`, et `§ 45.15`, `L10560–L10566`).
  - **Passe initiale :** écart rectifié · **Action :** explicité le renvoi `Tome 1 § 45.15` devant `§ 45.15` · **Verdict : supporté**

- **C29-09 (`L23–L31`, Tableau 29.1)** — *Affirmation :* Le `Tableau 29.1` résume les `5 SBB` du `Tableau 12`, leur plan (`Plan A`/`Plan B`), leurs modules (`obo_dpop.py`, `policy_saga/opa_runner.py` + `policies_opa/rule_of_two.rego`, `ciba_approval.py`, `audit_scitt_focus.py`, `decimal_money.py`) et les propriétés vérifiées en `G0` (`default allow := false` `[7]`).
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/` (modules vérifiés sur disque), `SRC-087.txt` (`[7]`), `aq/rapports-g0.json`, `registre/matrice-exig-prr-c40.json` (`cinq_sbb`).
  - **Passe initiale :** écart rectifié · **Action :** corrigé le chemin `policy_saga/opa_runner.py + policies_opa/rule_of_two.rego` dans la ligne `guardrails_engine` · **Verdict : supporté**

### Section 29.1.2 — Blueprint 1 (`bp1_assistant_interne`, `L33–L44`)

- **C29-10 (`L33–L40`)** — *Affirmation :* `bp1_assistant_interne` couvre les processus internes réglementés orientés `SoR` sous *Loi 25* art. `12.1` `[6]` et `BSIF E-23` `[5]`, correspond à `Tome 6 § 14.1` (`Fig. 53`), et sépare quatre plans (`SoE`, `SoA` `Temporal` `80/20` `JSON Schema`, Données/Outils `MCP`/`agentgateway`/`OPA` `[7]`/`OBO` `RFC 8693`/`CQRS`/`CDC`, Confiance/Audit `SPIFFE/SPIRE`/`OTel GenAI`/`WORM`).
  - **Appui vérifié :** `SRC-063.txt` (`[6]`), `SRC-065.txt` (`[5]`), `SRC-087.txt` (`[7]`), `Corpus/Tome 6` (`§ 14.1`, `Fig. 53`, `Tableau 14.1`, `L4340–L4415`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-11 (`L42`)** — *Affirmation :* Zéro `SQL` direct vers `SoR` ; respect de `MCP` `28 juillet 2026` — validation des schémas entrée/sortie et caractère non fiable des annotations `[4]`, avec en-têtes `Mcp-Method`/`Mcp-Name` et mode *Stateless Streamable HTTP* imposés en `G0` (`← Chapitre 07`, `DISC-05`) ; `Temporal` attente durable, *Worker Versioning* (`Pinned`), compensations en ordre inverse via canal isolé et cibles d'architecture `3-AZ` (`RPO = 0`) / multi-régions (`Tome 6 § 14.1.3`).
  - **Appui vérifié :** `SRC-072.txt` (`L62–L89`, `L302–L306`, `L368`, `[4]`), `registre/concordance-taxonomies.json` (`DISC-05`), `registre/specifications-lplus.json` (`SPEC-MCP-2026-07-28-HTTP`), `Corpus/Tome 6` (`§ 14.1.3`, `L4398–L4402`).
  - **Passe initiale :** écart rectifié · **Action :** dissocié les éléments couverts par `[4]` (`SRC-072`) du mode *Stateless Streamable HTTP* (`DISC-05`) et rattaché `3-AZ`/`RPO = 0` aux cibles du `Tome 6 § 14.1.3` ; en recollation `G3` (`seed=20270901`), regroupé `Mcp-Method`/`Mcp-Name` avec la porte `G0` (`← ch07`, `DISC-05`) hors `SRC-072.txt` · **Verdict : supporté**

- **C29-12 (`L44`)** — *Affirmation :* Gabarit orienté `OPEX` prévisible (capacité réservée + débordement, réduction des jetons `80/20`) et consommation de la plateforme interne comme service par les équipes alignées sur le flux.
  - **Appui vérifié :** `Corpus/Tome 6` (`§ 14.4.3`, `L4622–L4624`, `Tableau 14.4`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

### Section 29.1.3 — Blueprint 2 (`bp2_rag_entreprise_acl`, `L46–L54`)

- **C29-13 (`L46–L48`)** — *Affirmation :* `bp2_rag_entreprise_acl` répond aux charges haute confidentialité sous régime `Silo` de la *Loi 25* `[6]` (*Zero Egress*) et établit la concordance bijective `T6 Fig. 55 ↔ bp2` (Tome 6 `§ 14.3` « Blueprint 3 » vs Tome 8 `bp2_rag_entreprise_acl`, rappelée au Chapitre 36).
  - **Appui vérifié :** `SRC-063.txt` (`[6]`), `Corpus/Tome 6` (`§ 14.3`, `Fig. 55`, `L4510–L4562`), `Corpus/Tome 8` (`L1452`), `registre/matrice-exig-prr-c40.json` (`c01_c40_blueprints`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-14 (`L50`)** — *Affirmation :* Neutralisation de `OWASP ASI05` et `ASI06` `[8]` et hébergement mutualisé : `AI Gateway` locale (`Endpoint Picker`, `llm-d`/`vLLM`, `NVIDIA NIM`) en enclaves `AMD SEV-SNP`/`Intel TDX` et `GPU TEE` sous attestation distante, suivie du pipeline `RAG` (`OpenFGA` `ListObjects` `C15`, `Qdrant` `is_tenant`/`Silo` `C16`, `PostgreSQL RLS` en refus par défaut).
  - **Appui vérifié :** `SRC-055.txt` (`L102–L114`, `L266–L316`, `[8]`), `Corpus/Tome 6` (`§ 14.3.2–14.3.3`, `L4564–L4578`, `Tableau B.2` `C15`/`C16`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-15 (`L52–L54`)** — *Affirmation :* Confinement d'exécution analytique en `microVM` éphémères (`Firecracker` ou `Kata Containers` sous `agent-sandbox` avec bassins pré-chauffés, *Zero Egress*) visant les seuils `Firecracker` rapportés au cadre (`Tome 6 § 14.3.4`, hors corpus `L+` fermé de ce chapitre : `≤ 125 ms`, `< 5 MiB`, `> 95 %` CPU natif) ; substitution vers `CAPEX` GPU/RAM et veille chaude active-passive des données.
  - **Appui vérifié :** `Corpus/Tome 6` (`§ 14.3.4`, `L4580–L4587` ; `§ 14.4.2`, `L4618` ; `§ 14.4.3`, `L4622`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié les seuils `125 ms`, `5 MiB` et `95 %` de seuils `Firecracker` rapportés au cadre (`Tome 6 § 14.3.4`, hors corpus `L+` fermé de ce chapitre) et scindé le paragraphe selon `CA-05` · **Verdict : supporté**

### Section 29.1.4 — Blueprint 3 (`bp3_orchestration_multi_agents_b2b`, `L56–L83`, Tableau 29.2, Figure 91)

- **C29-16 (`L56–L58`)** — *Affirmation :* `bp3_orchestration_multi_agents_b2b` gouverne les chaînes transversales et `B2B`, opère la permutation `T6 Fig. 54 ↔ bp3` (`Tome 6 § 14.2` vs `Tome 8`) et garantit l'opacité inter-domaines (aucun `MCP` ni mémoire interne exposés).
  - **Appui vérifié :** `Corpus/Tome 6` (`§ 14.2`, `Fig. 54`, `L4417–L4478`), `Corpus/Tome 8` (`L1452`), `registre/matrice-exig-prr-c40.json` (`c01_c40_blueprints`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-17 (`L60`)** — *Affirmation :* Strate macro-réglementaire fédérée : `Process Manager` durable, `A2A v1.0.1` (`C13` `[2]`), `AGNTCY` (`OASF`, `ADS`, `SLIM`/`MLS` sortant uniquement, `C14`), `OAuth 2.0 OBO` à deux sauts (`C27`), fiches répliquées à provenance signée.
  - **Appui vérifié :** `SRC-083.txt` (`[2]`), `Corpus/Tome 6` (`§ 14.2.2`, `L4480–L4486` ; `Tableau B.2` `C13`/`C14`/`C27`, `L5023–L5037`), `registre/specifications-lplus.json` (`SPEC-RFC-9420`).
  - **Passe initiale :** écart rectifié · **Action :** réaligné les identifiants de critères sur `C13` (`A2A`), `C14` (`AGNTCY`/`SLIM`) et `C27` (`OBO` deux sauts) · **Verdict : supporté**

- **C29-18 (`L62–L64`)** — *Affirmation :* Strate intra-domaine `Event Mesh` (`Solace DMR`, `Kafka Cluster Linking`, `CloudEvents`, `AsyncAPI 3.0` `C20`, `ce_ttl`, `DLQ`, arbitrage réplication sync/async) ; validation anti-`SSRF` `[2]`, filtrage injections indirectes `[8]` et `CancelTask` `[2]` ; `a2a-tck` `1.0.0.alpha3` marquant `CARD-SIGN-001`..`004` `NOT_AUTOMATABLE` sans vecteurs `a2a-jcs-v01` `[3]` ; synthèse comparative sur socle commun (`SPIFFE`, `OpenTelemetry`, `OPA` `[7]`).
  - **Appui vérifié :** `SRC-083.txt` (`L270`, `L1168`, `L2370`, `[2]`), `SRC-086.txt` (`L133–L184`, `[3]`), `SRC-055.txt` (`L348–L355`, `[8]`), `SRC-087.txt` (`[7]`), `sources/ch29-sources.md` (`L40`), `Corpus/Tome 6` (`§ 14.2.3`, `L4489–L4498` ; `§ 14.4.3`, `L4657`).
  - **Passe initiale :** écart rectifié · **Action :** déplacé `C20` vers `CloudEvents`/`AsyncAPI 3.0` et ajouté les renvois `[2]` sur `SSRF` et `CancelTask` · **Verdict : supporté**

- **C29-19 (`L66–L72`, Tableau 29.2)** — *Affirmation :* Le `Tableau 29.2` met en regard `bp1_assistant_interne` (`§ 14.1` · `T6 Fig. 53`), `bp2_rag_entreprise_acl` (`§ 14.3` · `T6 Fig. 55`) et `bp3_orchestration_multi_agents_b2b` (`§ 14.2` · `T6 Fig. 54`), leurs critères clés, piles protocolaires (`[2, 3, 4]`) et garants de sécurité et de résilience.
  - **Appui vérifié :** `Corpus/Tome 6` (`Tableaux 14.1–14.3`, `L4406–L4596`), `SRC-072.txt` `[4]`, `SRC-083.txt` `[2]`, `SRC-086.txt` `[3]`.
  - **Passe initiale :** écart rectifié · **Action :** qualifié les seuils `Firecracker` de cibles et aligné les critères `C13`, `C14`, `C20`, `C27` et les renvois `[2]` dans le `Tableau 29.2` · **Verdict : supporté**

- **C29-20 (`L74–L78`, Figure 91)** — *Affirmation :* `Figure 91` (`SCH-29-01.svg`) comparant `bp1` (`Z1`), `bp2` (`Z2`) et `bp3` (`Z3`) assemblés sur `C1–C8` (socle d'illustration à `565` contrôles), les `5 SBB` du `Tableau 12` et la validation mécanique `C01–C40` en `G0`.
  - **Appui vérifié :** `specs/manifest.json` (`ch29`, `SCH-29-01`), `schemas/SCH-29-01.puml` (`L61–L83`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `(socle d'illustration à 565 contrôles)` en `L74` et `L78` pour refléter la portée de `C8` · **Verdict : supporté**

- **C29-21 (`L80–L83`)** — *Affirmation :* Trois invariants exécutables du Chapitre 29 : (1) validation mécanique des `5 SBB`, `C01–C40` et permutation `T6 Fig. 54 ↔ bp3` / `T6 Fig. 55 ↔ bp2` dans `evalops_prr/prr_validators.py` ; (2) gravité locale `≥ 85 %` `SaaS`, `Cognitive DR` cible `RTO < 15` min / `RPO = 0` / resserrement `HOTL` `15–25 %`, sas `B2B` `P3` (`vLEI`, `ODRL 2.2`, Diplomate/Évaluateur, rapprochement tripartite) ; (3) exclusion `DC-P11`/`DC-P12`/`C27`/`CA-10` du Groupe Boréal au profit des `108` blocs `Borealis-Bench` consignés au Corpus (`90` exécutés en CI dont `9` modules Python à assertions comportementales) et de la trousse du Tome 8.
  - **Appui vérifié :** `Tomes/Tome 8 .../trousse/evalops_prr/prr_validators.py`, `Corpus/Tome 3` (`L320`, `L14233`, `L24392`, `L24480`), `registre/matrice-exig-prr-c40.json` (`POR-013`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié `RTO < 15` minutes de cible (`visant`) et précisé la provenance Corpus (`90` exécutés dont `9` modules Python) et l'appui sur la trousse du Tome 8 · **Verdict : supporté**

### Section 29.2.1 — Fédération des cinq suites `SaaS` par gravité des données (`ADR-015`, `L87–L101`, Figure 92)

- **C29-22 (`L87–L89`)** — *Affirmation :* Coexistence des cinq écosystèmes `SaaS` (`Salesforce Agentforce`, `ServiceNow`, `SAP Joule`/`S/4HANA`, `Microsoft Copilot Studio`, `Workday`) exposant au maillage quadratique et aux fuites d'invariants (dont dossiers salariaux `Workday` sous *Loi 25* `[6]`).
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 27.6`, `L14147–L14221` ; `§ 27.10`, `L14556`), `SRC-063.txt` (`[6]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-23 (`L91–L95`)** — *Affirmation :* Fédération gouvernée par gravité des données (`ADR-015`) selon trois règles déterministes : localité intra-domaine (`≥ 85 %` d'appels locaux), enrichissement en lecture seule via `agentgateway` + `MCP`, et élévation au plan de contrôle neutre (`Temporal` et `agentgateway`) dès mutation sur `≥ 2` silos, saga compensatoire ou exigence prudentielle (`BSIF E-23` `[5]`).
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 27.7`, `L14223–L14247` ; `§ 27.11`, `L14574–L14582`), `SRC-065.txt` (`[5]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-24 (`L97`)** — *Affirmation :* Propagation d'identité `OAuth 2.0 OBO` (`RFC 8693`) depuis `Microsoft Entra ID` vers `Salesforce` et `SAP CIS` sans compte technique partagé, et vecteur de trace cryptographiquement signé détectant et coupant toute réentrance circulaire de webhooks.
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 27.8`, `L14316–L14424`, Extraits `27.2` et `27.3`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-25 (`L99–L101`, Figure 92)** — *Affirmation :* `Figure 92` (`SCH-29-02.png`) et légende articulant `ADR-015` (`Z1`, `≥ 85 %` local), `Cognitive DR` `ADR-027` (`Z2`, visant `RTO < 15` min) et `POR-013` (`Z3`).
  - **Appui vérifié :** `specs/manifest.json` (`ch29`, `SCH-29-02`), `schemas/SCH-29-02.mmd` (`L1–L17`).
  - **Passe initiale :** écart rectifié · **Action :** précisé `visant un RTO < 15 minutes` dans la légende `L101` · **Verdict : supporté**

### Section 29.2.2 — Reprise après sinistre cognitif (`Cognitive DR`, `ADR-027`, `L103–L114`)

- **C29-26 (`L103–L105`)** — *Affirmation :* `ADR-027` (`Cognitive DR`, liée aux contrôles de reprise `F-07` et `R-11` du cadre, `Tome 3 § 46.11–46.13`) institue la continuité cognitive testée par exercice de bascule trimestriel (ou au moins annuel), autour d'une cible de conception sans source externe de `RTO < 15` minutes et `RPO = 0`.
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 46.11`, `L24383–L24399` ; `§ 46.13`, `L24478–L24499`), `registre/matrice-exig-prr-c40.json` (`prr_75` `F-07`, `R-11`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié explicitement `RTO < 15` min de cible de conception sans source externe (`Tome 3 § 46.11–46.13`) et aligné la cadence d'exercice (`trimestriel` ou au moins `annuel`) · **Verdict : supporté**

- **C29-27 (`L107–L112`)** — *Affirmation :* Quatre mécanismes du profil `ADR-027` : (1) enveloppe `Open Responses` écartant les blocs de délibération chiffrés au profit du journal canonique ; (2) double profil nominal / secours (`vLLM` ou `SGLang`, décodage contraint `MCP`), homologation CI/CD `pass^5_DR ≥ 0,94 · pass^5_nominal`, zone intermédiaire `[0,90 ; 0,94 · pass^5_nominal[` recalée en nominal mais admise en bascule d'urgence (`cognitive_dr_switch.py`) sous plafonds `HOTL` resserrés (`−15 %` à `−25 %`, multiplicateur `0,80`), et déviation sous `0,90` vers file humaine (`SAFE_HOLD_L2_HUMAN_QUEUE`, `Tome 3 § 46.11`) ; (3) embeddings ouverts + `BM25` (`100 %` interrogeables) et préchargement `NVMe` sous cible de `180` s ; (4) abaissement des plafonds `HOTL` de `15` à `25 %` (`RPO = 0`).
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 46.10`, `L24381` ; `§ 46.11`, `L24389–L24447`, `cognitive_dr_switch.py`).
  - **Passe initiale :** écart rectifié · **Action :** rattaché explicitement le seuil `0,94` et le plancher illustratif `0,90` aux règles internes `ADR-027` (`Tome 3 § 46.11`), et explicité au lissage G5 la zone `[0,90 ; 0,94 · pass^5_nominal[` et `SAFE_HOLD_L2_HUMAN_QUEUE` (`0,80`) · **Verdict : supporté**

- **C29-28 (`L114–L116`)** — *Affirmation :* Formule opérationnelle du `RTO ≤ 15` min (`Tome 3 § 46.11`) en trois jalons séquentiels : (1) détection (`cognitive_dr_switch.py` : taux d'erreur `≥ 0,08`, `p95_ttft_ms ≥ 12 000` ou `≥ 25` erreurs `429`/`5xx`), quiescence `Temporal` (`RPO = 0`) et purge `Open Responses` (`T + 30 s` en gabarit Fig. 58) ; (2) basculement passerelle en parallèle du préchargement `NVMe` (`≤ 180 s`, `T + 3 min`) ; (3) validation *Canary* distinguant la zone `[0,90 ; 0,94 · pass^5_nominal[` (reprise dégradée sous `HOTL` resserré à `0,80`) du plancher `< 0,90` (file humaine, `T + 12 min`). Ce budget cible (`ADR-027`) vise à instrumenter la résilience et la maîtrise des dépendances externes attendues par `BSIF E-23` `[5]` (avec `BSIF B-10`), sans que ce délai ni cette cadence ne figurent textuellement dans `E-23` `[5]`.
  - **Appui vérifié :** `Corpus/Tome 3` (`§ 46.11` `L24383–24470`, `cognitive_dr_switch.py`), `SRC-065.txt` (`[5]`, absence vérifiée de `15` min et d'exercice annuel de débranchement), `Corpus/Tome 1` (`L10609`), `SRC-068.txt` (`BSIF B-10`).
  - **Passe initiale :** écart rectifié · **Action :** retiré la formulation attribuant à `BSIF E-23` `[5]` l'exigence textuelle d'exercices annuels de débranchement sous `15` minutes, intégré les trois jalons chiffrés (`post-G4`) et aligné la distinction `[0,90 ; 0,94 · pass^5_nominal[` vs `< 0,90` (lissage G5) · **Verdict : supporté**

### Section 29.2.3 — Ouverture conditionnelle aux réseaux `B2B` fédérés au Palier 3 (`POR-013`, `L116–L123`)

- **C29-29 (`L116–L118`)** — *Affirmation :* Proscription de l'automatisation inter-organisations entièrement fédérée en conseil, vente et convenance (`D2`, incluant la gestion de patrimoine) et en conformité, LBC et gestion des risques (`D6`) ; ouverture différée au Palier 3 (`2033–2035`) sous `POR-013`, signaux `SIG-007` et `SIG-110`, arbitrage `DEC-012` et initiatives `INI-046` à `INI-048`.
  - **Appui vérifié :** `registre/matrice-exig-prr-c40.json` (`POR-013`, `SIG-007`, `SIG-110`, `INI-046`..`048`), `registre/concordance-taxonomies.json` (`DISC-02`, `L132`), `Corpus/Tome 4` (`L2957`, `L2961`, `L4566`, `L4626`).
  - **Passe initiale :** écart rectifié · **Action :** précisé les libellés complets des domaines `D2` et `D6` conformément au `Tome 4`, et retiré `de stade 4` au lissage G5 (`DISC-02`) · **Verdict : supporté**

- **C29-30 (`L120–L123`)** — *Affirmation :* Quatre verrous cumulatifs `B2B` : (1) `GLEIF vLEI` et `OOR` (`CAP-041`, `ISO 17442-3`, `KERI`/`ACDC` `[1]`, sous-page gouvernance `HTTP 404` consignée en `statut F` `AO-01` compensée par `[1]`) ; (2) connecteurs `Dataspace` et `ODRL 2.2` (`CAP-027`) ; (3) scission `Diplomate` externe ↔ `Évaluateur` interne (`CAP-014`) ; (4) rapprochement tripartite hors modèle (`EXIG-INT-22`, `ADR-026`, `CAP-014` et `CAP-026`, rails `AP2`/`x402`).
  - **Appui vérifié :** `SRC-079.txt` (`L5`, `L97–L125`, `[1]`), `sources/ch29-sources.md` (`L101`), `registre/matrice-exig-prr-c40.json` (`CAP-014`, `CAP-026`, `CAP-027`, `CAP-041`, `POR-013`), `Corpus/Tome 3` (`§ 45.12`, `L23909–L23914`).
  - **Passe initiale :** écart rectifié · **Action :** qualifié l'exclusion `statut F` (`AO-01`) sur la sous-page `HTTP 404` et ajouté `CAP-014` avec `EXIG-INT-22`/`ADR-026` sur le rapprochement tripartite · **Verdict : supporté**

### Section 29.3 — Fil rouge `Groupe Boréal`, exclusion `DC-P11`/`DC-P12` et `Borealis-Bench` (`L125–L153`, Tableau 29.3, Figure 93)

- **C29-31 (`L125–L127`)** — *Affirmation :* Scénario transversal fictif **Groupe Boréal Inc.** (`BEL` fabrication/distribution, `BCA` financement/assurance sous `BSIF E-23` `[5]` et *Loi 25* `[6]`, `BSN` télématique industrielle), rationalisation de `47` initiatives dont `19` fantômes sous `L0–L3` et `ADR-003`/`014`/`027`/`029`, avec périmètre démontré borné à `BCA` et au contrôle logiciel déterministe (`BEL` et `BSN` étant des extrapolations illustratives).
  - **Appui vérifié :** `Corpus/Tome 3` (`L320–L339`, `L1051`), `SRC-065.txt` (`[5]`), `SRC-063.txt` (`[6]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-32 (`L129–L133`)** — *Affirmation :* Quatre flux `Boréalis` : Flux 1 (`BCA` décision de crédit `OO3`–`OO4`, point d'arrêt technique distinct de la révision qualifiée art. `12.1` *Loi 25* `[6]`), Flux 2 (`Lynx` « l'agent observe, le rail exécute »), Flux 3 (cadre bancaire ouvert sans norme technique désignée), Flux 4 (`HL7 FHIR` souscription vie et règlement de sinistres).
  - **Appui vérifié :** `Corpus/Tome 1` (`§ 45.11–45.14`, `L10498–L10559`), `SRC-063.txt` (`L1542`, `[6]`).
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**

- **C29-33 (`L135`)** — *Affirmation :* Exclusion probante absolue (`DC-P11`, `DC-P12`, `C27`, `CA-10`) des chiffres narratifs fictifs (`6,8 G$ CAD`, `14 500` employés, `11` min `14` s) au profit des campagnes reproductibles `FEDS` : `108/108` blocs syntaxiquement valides de `Borealis-Bench` consignés au Corpus (`Tome 3`, hors dépôt local : `90` exécutés en CI dont `9` modules Python à assertions comportementales et l'Extrait `47.7`, et `18` schémas conceptuels), appuyés localement sur les `83/83` `pytest`, `50/50` vecteurs tiers et `45/45` tests `OPA` (`100,0 %`, `default allow := false` `[7]`) de `aq/rapports-g0.json`.
  - **Appui vérifié :** `Corpus/Tome 3` (`L320`), `Corpus/Tome 8` (`L1763`), `aq/rapports-g0.json` (`L31–L75`), `SRC-087.txt` (`[7]`).
  - **Passe initiale :** écart rectifié · **Action :** rectifié la proportion exacte des `90` blocs en CI (`9` modules Python à assertions comportementales), précisé la provenance Corpus de `Borealis-Bench` (hors dépôt local) et rattaché `default allow := false` à `[7]` et les métriques `G0` à `aq/rapports-g0.json` · **Verdict : supporté**

- **C29-34 (`L137`)** — *Affirmation :* Portabilité contractuelle des actifs ouverts et clauses de sortie réglementaires (`BSIF B-10` et règlement européen sur les données `Data Act`), avec contrat de tests automatisés requis avant promotion en production.
  - **Appui vérifié :** `SRC-068.txt` (`BSIF B-10`, plans de sortie), `registre/ancres-chronologiques.json` (`ANC-003`, Règlement (UE) 2023/2854 `Data Act`, art. `29 § 1`).
  - **Passe initiale :** écart rectifié · **Action :** nommé explicitement `Data Act` pour lever toute ambiguïté sur le règlement européen sur les données · **Verdict : supporté**

- **C29-35 (`L139–L145`, Tableau 29.3)** — *Affirmation :* Le `Tableau 29.3` synthétise la frontière `DC-P11`/`DC-P12` entre le rôle pédagogique du Groupe Boréal (`6,8 G$ CAD`, `14 500` employés, `41 000 $ CAD` d'incident, `47`/`19`, `11` min `14` s) et les substituts vérifiables (`BCA`/contrôle logiciel, `108` blocs `Borealis-Bench` consignés au Corpus dont `90` exécutés en CI / `9` modules Python et `18` schémas, campagnes `FEDS` et `G0` Tome 8 à `83/83` `pytest`, `50/50` vecteurs tiers, `45/45` tests `OPA` à `100,0 %` sur `default allow := false` `[7]`).
  - **Appui vérifié :** `Corpus/Tome 3` (`L320`, `L324`, `L333`, `L335`, `L24471`), `aq/rapports-g0.json`, `SRC-087.txt` (`[7]`).
  - **Passe initiale :** écart rectifié · **Action :** aligné la colonne `Substitut probant` sur le décompte exact (`9` modules Python, `18` schémas, `50/50` vecteurs tiers, `45/45` tests `OPA`, `default allow := false` `[7]`) · **Verdict : supporté**

- **C29-36 (`L147–L153`, Figure 93)** — *Affirmation :* `Figure 93` (`SCH-29-03.svg`) illustrant la séparation entre le fil rouge `Groupe Boréal Inc.` (`Z1`), le filtre d'exclusion `DC-P11`/`DC-P12`/`C27` (`Z2`) et les `108` blocs CI de `Borealis-Bench` (`Z3`), suivie de la transition vers le Chapitre 30 (`IAP`, `GitOps` cognitif et anti-patrons).
  - **Appui vérifié :** `specs/manifest.json` (`ch29`, `SCH-29-03`, `ch30`), `schemas/SCH-29-03.svg`.
  - **Passe initiale :** conforme · **Action :** aucune · **Verdict : supporté**
