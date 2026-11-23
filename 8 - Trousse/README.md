# `8 - Trousse/` — Dépôt compagnon exécutable du Volume 8

> [Retour à l'index principal du dépôt](../README.md) · Manuel compagnon : [`8 - Manuel`](../8%20-%20Manuel/README.md) · Rapport `G0` : [`aq/rapports-g0.json`](../8%20-%20Manuel/aq/rapports-g0.json)

> **AVIS IMPORTANT (`non-avis` · `AO-05` / `DC-P12`) :**  
> Ce dépôt constitue une **référence figée et vérifiée à la date de gel (`2026-12-02`) — archive pédagogique non maintenue en production sans équipe d'exploitation dédiée**.  
> Toute exécution conforme (`G0 exit 0`) repose exclusivement sur des doublures hors modèle hermétiques et des vecteurs déterministes. Elle ne constitue **ni un avis juridique, ni un conseil réglementaire personnalisé, ni une certification d'audit ou actuarielle, ni une homologation `BSIF E-23`, `AMF`, `ISO/IEC 42001` ou `Loi 25` sur un *System of Record* (`SoR`) réel**.

---

## Vue d'ensemble

`8 - Trousse/` regroupe les contrats exécutables, politiques `OPA / Rego`, schémas `JSON Schema Draft 2020-12` (`strict: true`), vecteurs officiels tiers et suites `pytest` associés au manuel [*Ingénierie exécutable de l'entreprise agentique*](../8%20-%20Manuel/README.md) (André-Guy Bruneau, M.Sc IT — édition de référence : janvier 2027, gel des faits : `2 décembre 2026`).

- **Licence du code (`8 - Trousse/`) :** [`MIT`](LICENSE)
- **Licence du manuel et des figures (`8 - Manuel/`) :** `CC BY 4.0` (voir [`NOTICE`](NOTICE))
- **Moteur de politiques hors modèle :** `OPA` CLI `v1.22.4` (`Apache-2.0`, condensat vérifié dans [`tools-lock.json`](tools-lock.json))
- **Bilan `G0` vérifié (`aq/rapports-g0.json`) :** `PASS` (`exit_code: 0`) — `83/83` tests `pytest` réussis (`0` échec, `0` ignoré), `45/45` tests `OPA` réussis à `100,0 %` de couverture, `21` validations de schémas/registres, `4/4` suites de vecteurs tiers (`50/50` fichiers), `17` paquets verrouillés dans [`requirements.lock`](requirements.lock) et `50` fichiers / `18` paquets conformes `MIT` contre [`spdx-allowlist.json`](spdx-allowlist.json).

### Arborescence du dépôt

#### Modules applicatifs et bancs exécutables (`4` paquets Python)

- [`harness_proto/`](harness_proto/) (`5` fichiers : `__init__.py`, `jcs.py`, `pipeline.py`, `mcp_pinning.py`, `a2a_card.py`) — Harnais déterministe 80/20 en huit étapes, canonisation `RFC 8785` (`JCS`), épinglage `MCP 2026-07-28`, validation `AgentCard A2A v1.0.1` et adaptateurs d'isolation post-gel (`SEP-2596` / `SEP-3398`, `A2A v1.1.0-rc`)
- [`authz_pqc_audit/`](authz_pqc_audit/) (`8` fichiers : `__init__.py`, `obo_dpop.py`, `revocation_fsm.py`, `ciba_approval.py`, `pqc_http431.py`, `otel_pii_mapper.py`, `slh_dsa_fips205.py`, `audit_scitt_focus.py`) — Délégation `OAuth 2.0 OBO` + `DPoP`, automate `SSF`/`CAEP`, approbations `CIBA` `I-JSON`/`JCS`, mesure exacte `HTTP 431` (`ML-DSA-65/87` vs *Transaction Tokens*), mappage `OTel v1.41.0` ↔ `semantic-conventions-genai`, `SLH-DSA FIPS 205`, chaîne `SCITT` et extension carbone `FOCUS v1.4`
- [`policy_saga/`](policy_saga/) (`6` fichiers : `__init__.py`, `opa_runner.py`, `taint_camel.py`, `sandbox_manifest.py`, `decimal_money.py`, `saga_orchestrator.py`) — Couche Python d'évaluation `OPA CLI` (`shell=False`), suivi de contamination `CaMeL`, validation des manifestes de confinement, arithmétique `Decimal` et orchestrateur Saga (`idem-v1`, `Outbox`, canal isolé `EXIG-ORC-28`)
- [`evalops_prr/`](evalops_prr/) (`5` fichiers : `__init__.py`, `mock_mcp_harness.py`, `wilson_bounds.py`, `metamorphic.py`, `prr_validators.py`) — Doublures `mock MCP servers` (`pass^k`), bornes de Wilson (`EXIG-EVA-03`), tests métamorphiques sans oracle et validateurs `24 [BLOQUANT] PRR`, `2027-B001`, `5 SBB` et `C01–C40`

#### Politiques, schémas, vecteurs et tests

- [`policies_opa/`](policies_opa/) (`6` fichiers) — `3` paquets de politiques `.rego` avec `default allow := false` obligatoire (`camel_taint.rego`, `rule_of_two.rego`, `sandbox_confinement.rego`) et `3` suites de tests `*_test.rego` (`camel_taint_test.rego`, `rule_of_two_test.rego`, `sandbox_confinement_test.rego`) validant **`45` tests réussis** à **`100,0 %` de couverture**
- [`schemas/`](schemas/) (`13` schémas `JSON Schema Draft 2020-12`, `strict: true`, `"x-license": "MIT"`) — `a2a_agent_card.schema.json`, `adr_2027_b001.schema.json`, `approval_token_c6.schema.json`, `audit_record_c8.schema.json`, `delegated_token_claims.schema.json`, `evalops_wilson_report.schema.json`, `focus_carbon_record.schema.json`, `harness_extraction.schema.json`, `mcp_tool_catalog.schema.json`, `opa_authz_input.schema.json`, `prr_24_evidence.schema.json`, `saga_state.schema.json`, `sandbox_manifest.schema.json`
- [`vectors/`](vectors/) (`51` fichiers) — Manifeste [`vectors-manifest.json`](vectors/vectors-manifest.json) et `4` suites officielles hors ligne (`50` fichiers scellés `SHA-256`) : [`rfc8785/`](vectors/rfc8785/) (`20` fichiers), [`nist_acvp/`](vectors/nist_acvp/) (`12` fichiers), [`a2a_tck/`](vectors/a2a_tck/) (`5` fichiers) et [`owasp_src055/`](vectors/owasp_src055/) (`13` fichiers)
- [`tests/`](tests/) (`6` fichiers de tests `pytest` découplés, **`83` tests réussis**) — `test_harness_proto.py` (`14`), `test_authz_pqc_audit.py` (`23`), `test_policy_saga.py` (`18`), `test_saga_10_faults.py` (`11`), `test_evalops_prr.py` (`10`) et `test_third_party_vectors.py` (`7`)

#### Configuration, verrouillage et licences à la racine

- [`pyproject.toml`](pyproject.toml) — Paquet `agentique-trousse-vol8` (`1.0.0`, `requires-python >= 3.12`) et configuration `pytest`
- [`requirements.lock`](requirements.lock) — `17` paquets Python épinglés par condensats `SHA-256` (`pip install --require-hashes --no-deps`)
- [`tools-lock.json`](tools-lock.json) — Épinglage `SHA-256` multiplateforme de `OPA CLI v1.22.4` (`Apache-2.0`, Windows `.tools/opa.exe` et Linux `.tools/opa`)
- [`spdx-allowlist.json`](spdx-allowlist.json) — Liste blanche des `8` licences permissives compatibles `MIT`
- [`LICENSE`](LICENSE) — Texte officiel de la licence `MIT`
- [`NOTICE`](NOTICE) — Attributions, frontière `MIT` (`8 - Trousse/`, `8 - Manuel/outils/`) / `CC BY 4.0` (`8 - Manuel/`) et notice `OPA`
- [`.gitignore`](.gitignore) — Exclusions locales (`.venv/`, `.tools/`, `__pycache__/`, `.pytest_cache/`, `*.py[cod]`)

---

## Mode d'emploi portable (Windows et Linux)

### Prérequis

- **Python `>= 3.12`** (vérifié sous Python `3.14.10` Windows amd64)
- **OPA CLI `v1.22.4`** (`Apache-2.0`) : installé localement dans `.tools/opa.exe` sous Windows (ou téléchargeable selon les empreintes `SHA-256` de [`tools-lock.json`](tools-lock.json) sous Linux `.tools/opa`)

### 1. Création et restauration reproductible de `.venv`

Sous **Windows (PowerShell)** depuis `8 - Trousse/` :

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --require-hashes --no-deps -r requirements.lock
```

Sous **Linux / macOS (bash)** depuis `8 - Trousse/` :

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --require-hashes --no-deps -r requirements.lock
```

### 2. Vérification d'`OPA CLI` et des politiques Rego

Sous **Windows (PowerShell)** depuis `8 - Trousse/` :

```powershell
.\.tools\opa.exe version
.\.tools\opa.exe test policies_opa --coverage --format=json
```

Sous **Linux** depuis `8 - Trousse/` (après téléchargement du binaire `opa_linux_amd64_static` vérifié contre [`tools-lock.json`](tools-lock.json)) :

```bash
./.tools/opa version
./.tools/opa test policies_opa --coverage --format=json
```

### 3. Exécution des tests `pytest` et de la barrière `G0`

Depuis la racine du dépôt (`Agentique/`), sous **Windows (PowerShell)** :

```powershell
& "8 - Trousse\.venv\Scripts\python.exe" -B -m pytest -p no:cacheprovider "8 - Trousse\tests" -q --tb=short
& "8 - Trousse\.venv\Scripts\python.exe" -B "8 - Manuel\outils\execute_g0.py" --verify-sync-manifest
```

Sous **Linux / macOS (bash)** depuis la racine du dépôt :

```bash
"8 - Trousse/.venv/bin/python" -B -m pytest -p no:cacheprovider "8 - Trousse/tests" -q --tb=short
"8 - Trousse/.venv/bin/python" -B "8 - Manuel/outils/execute_g0.py" --verify-sync-manifest
```

Pour exécuter `execute_g0.py` en lecture seule sans réécrire l'horodatage de [`8 - Manuel/aq/rapports-g0.json`](../8%20-%20Manuel/aq/rapports-g0.json), ajouter `--output <chemin-temporaire.json>`. Les licences de toutes les dépendances installées sont contrôlées mécaniquement via `importlib.metadata` contre [`spdx-allowlist.json`](spdx-allowlist.json).
