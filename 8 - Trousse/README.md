# `8 - Trousse/` — Dépôt compagnon exécutable du Volume 8

> **AVIS IMPORTANT (`non-avis` · `AO-05` / `DC-P12`) :**  
> Ce dépôt constitue une **référence figée et vérifiée à la date de gel (`2026-12-02`) — archive pédagogique non maintenue en production sans équipe d'exploitation dédiée**.  
> Toute exécution conforme (`G0 exit 0`) repose exclusivement sur des doublures hors modèle hermétiques et des vecteurs déterministes. Elle ne constitue **ni un avis juridique, ni un conseil réglementaire personnalisé, ni une certification d'audit ou actuarielle, ni une homologation `BSIF E-23`, `AMF`, `ISO/IEC 42001` ou `Loi 25` sur un *System of Record* (`SoR`) réel**.

---

## Vue d'ensemble

`8 - Trousse/` regroupe les contrats exécutables, politiques `OPA / Rego`, schémas `JSON Schema Draft 2020-12` (`strict: true`), vecteurs officiels tiers et suites `pytest` associés au manuel *Ingénierie exécutable de l'entreprise agentique* (André-Guy Bruneau, M.Sc IT, parution visée : janvier 2027).

- **Licence du code (`8 - Trousse/`) :** [`MIT`](LICENSE)
- **Licence du manuel et des figures (`8 - Manuel/`) :** `CC BY 4.0` (voir [`NOTICE`](NOTICE))
- **Moteur de politiques hors modèle :** `OPA` CLI `v1.22.4` (`Apache-2.0`, condensat vérifié dans [`tools-lock.json`](tools-lock.json))

### Structure cible

- `harness_proto/` — Harnais déterministe 80/20, canonisation `RFC 8785` (`JCS`), épinglage `MCP 2026-07-28`, validation `AgentCard A2A v1.0.1` et adaptateurs d'isolation post-gel (`SEP-2596` / `SEP-3398`, `A2A v1.1.0-rc`)
- `authz_pqc_audit/` — Délégation `OAuth 2.0 OBO` + `DPoP`, automate `SSF`/`CAEP`, approbations `CIBA` `I-JSON`/`JCS`, mesure exacte `HTTP 431` (`ML-DSA-65/87` vs *Transaction Tokens*), mappage `OTel v1.41.0` ↔ `semantic-conventions-genai`, `SLH-DSA FIPS 205`, chaîne `SCITT` et extension carbone `FOCUS v1.4`
- `policy_saga/` — Couche Python d'évaluation `OPA CLI` (`shell=False`), suivi de contamination `CaMeL`, validation des manifestes de confinement, arithmétique `Decimal` et orchestrateur Saga (`idem-v1`, `Outbox`, canal isolé `EXIG-ORC-28`)
- `evalops_prr/` — Doublures `mock MCP servers` (`pass^k`), bornes de Wilson (`EXIG-EVA-03`), tests métamorphiques sans oracle et validateurs `24 [BLOQUANT] PRR`, `2027-B001`, `5 SBB` et `C01–C40`
- `policies_opa/` — Paquets `.rego` (`default allow := false` obligatoire) et suites `*_test.rego` à couverture `100 %`
- `schemas/` — Schémas `JSON Schema Draft 2020-12` (`strict: true`, `"x-license": "MIT"`)
- `vectors/` — Suites de vecteurs tiers scellées hors ligne (`rfc8785`, `nist_acvp`, `a2a_tck`, `owasp_src055`)
- `tests/` — Harnais `pytest` découplé

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

### 2. Vérification de `opa.exe` et des politiques Rego

Sous **Windows (PowerShell)** :

```powershell
.\.tools\opa.exe version
.\.tools\opa.exe test policies_opa --coverage --format=json
```

Sous **Linux** (après téléchargement du binaire `opa_linux_amd64_static` vérifié contre `tools-lock.json`) :

```bash
./.tools/opa version
./.tools/opa test policies_opa --coverage --format=json
```

### 3. Exécution des tests `pytest` et de la barrière `G0`

Depuis la racine du dépôt (`Agentique/`) :

```powershell
& "8 - Trousse\.venv\Scripts\python.exe" -B -m pytest -p no:cacheprovider "8 - Trousse\tests" -q --tb=short
& "8 - Trousse\.venv\Scripts\python.exe" -B "8 - Manuel\outils\execute_g0.py"
```

Les licences de toutes les dépendances installées sont contrôlées mécaniquement via `importlib.metadata` contre [`spdx-allowlist.json`](spdx-allowlist.json).
