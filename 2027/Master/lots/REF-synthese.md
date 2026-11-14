# Bilan de clôture — Validation et correction des références du Compendium 2027

## 1. Statistiques globales vérifiées (manuscrit final)

- **Manuscrit :** `59` fichiers Markdown dans `Master/manuscrit/` (`ouverture.md`, `chapitre-01` à `chapitre-50`, `annexe-A` à `annexe-H`), `31` volets « Mise en œuvre » dans `28` chapitres, `554` sections, `97` extraits, `31` fiches `ADR-001` à `ADR-031`, `67` figures SVG (`38` d'origine, `29` schémas d'exposé).
- **Sources numérotées (`## Sources`) :** `1 033` entrées (`789` dans les chapitres 1 à 47 et `244` dans la partie X, chapitres 48 à 50). Zéro entrée sans URL et zéro appel `[n]` dans les volets `{.volet}` ou dans `ouverture.md`.
- **URL recensées :** `1 101` occurrences d'URL publiques (`878` distinctes), dont `1 088` occurrences hors blocs de code (`866` distinctes) et `13` occurrences d'URI publiques dans les blocs de code (`12` distinctes), plus `48` occurrences d'URL fictives documentaires dans les extraits.
- **Audit consolidé (`Master/recherche/audit-references.json`) :** `5 607` entrées couvrant l'ensemble des `59` fichiers et toutes les URL publiques actuelles du manuscrit (`0` anomalie bloquante ouverte).
  - Provenance : `5 604` entrées consolidées depuis `audit-ref-1.json` (`1 510`), `audit-ref-2.json` (`790`), `audit-ref-3.json` (`712`), `audit-ref-4.json` (`1 427`) et `audit-ref-5.json` (`1 165`), auxquelles s'ajoutent `3` entrées `source` (DOI `10.3390/fi18060326` ajouté lors de l'audit dans `ch01`, `ch16` et `ch20`).
  - Par statut consolidé : `renvoi_valide` (`2 557`), `valide` (`2 416`), `corrige` (`263`), `acces_restreint` (`236`), `valide_redirection` (`64`), `illustratif` (`40`), `corrige_acces_restreint` (`30`), `mort_documente` (`1`).
- **Corrections appliquées (`Master/audit/corrections.json`) :** `268` remplacements issus des `16` lots (`12` lots `REF-1` à `REF-5` + `REF-cloture` à `REF-cloture-4`), portant le registre à `1 579` entrées.
- **PDF recomposé (`CompendiumMaster.pdf`) :** `1 100` pages, `16,3 Mo`, `412 671` mots estimés à l'assemblage (`428 919` mots extraits par `compendium-master-verifie.py`).

## 2. Récapitulatif par tranche et clôture

| Tranche / Lot | Périmètre | Entrées audit | Lots appliqués | Remplacements |
|:---|:---|---:|:---|---:|
| **Tranche 1** | Chapitres 1 à 11 (`1 510` + `1` ajout DOI `ch01`) | 1 511 | `REF-1-factuel` (20), `REF-1-harmonisation` (31) | 51 |
| **Tranche 2** | Chapitres 12 à 24 (`790` + `2` ajouts DOI `ch16`, `ch20`) | 792 | `REF-2-factuel` (21), `REF-2-coherence` (36) | 57 |
| **Tranche 3** | Chapitres 25 à 37 | 712 | `REF-3-renvoi` (4), `REF-3-coherence` (30) | 34 |
| **Tranche 4** | Chapitres 38 à 47 | 1 427 | `REF-4-renvoi` (10), `REF-4-factuel` (12), `REF-4-coherence` (39) | 61 |
| **Tranche 5** | Chapitres 48–50, `ouverture`, `annexes`, `Presentation.html` | 1 165 | `REF-5-renvoi` (2), `REF-5-factuel` (29), `REF-5-harmonisation` (12) | 43 |
| **Clôture** | Harmonisation inter-tranches, `annexe-E`, `ch16`, `ch17`, `ch21`, `ch22`, `ch24`, `ch38`, `ch39`, `ch47`, `ch50` | — | `REF-cloture` (10), `REF-cloture-2` (7), `REF-cloture-3` (3), `REF-cloture-4` (2) | 22 |
| **Total** | **59 fichiers + `Presentation.html`** | **5 607** | **16 lots** | **268** |

## 3. Principales corrections et harmonisations appliquées

- **URL et redirections corrigées :**
  - Mise à jour des URL canoniques Anthropic `/research/building-effective-agents` (`ch01`, `ch16`, `ch17`, `annexe-E`) et `/research/multi-agent-research-system` (`ch21 [6]`, aligné sur `ch40`), ainsi que NIST `SI Agent Standards Initiative` (`/super-intelligence/si-agent-standards-initiative` en `ch01` et `annexe-E`).
  - Actualisation de trois URL fédérales `www.canada.ca` après redirection permanente `301` (`ch22 [13]`, `ch38 [5]`, `[6]`, `[18]`, `ch39 [4]`, tout en conservant les réserves d'accès automatisé intermittent) et des deux adresses SEC EDGAR sans zéros initiaux dans le CIK (`ch50 [23]`, `[25]`).
  - Redirections canoniques mises à jour : Google Cloud Memory Bank (`ch14` `[33]`), The Register (`ch26` `[16]`), Cloudflare Verified bots (`ch29` `[14]`), MCP `security_best_practices.md` daté `2026-07-28` (`ch24` `[10]`, `ch31` `[4]`), Microsoft Learn / Entra Agent ID (`ch39` `[7]`, `[9]`), URL PDF officielle du Bulletin de l'AMF (`ch38` `[22]`), et arXiv `2603.07670` au lieu de Consensus (`ch48` `[32]`).
- **Exactitude factuelle et notices bibliographiques :**
  - Ajout et confirmation de DOI Crossref (`10.3390/fi18060326` dans `ch01`, `ch16`, `ch20`; `10.52202/085713-4082` dans `ch48`/`annexe-E`) et d'auteurs vérifiés sur source (`Xing et coll.` pour `arXiv 2508.10991v4` en `ch24 [15]`; `Emelyanov` en `ch48 [27]`; paires d'auteurs `X et Y` en `ch48`).
  - Harmonisation de `chapitre-47` (`L266`, `L1107` et `Master/fusion/reecrit/chapitre-47-volet-c.md`) et levée de contradictions entre bandeaux, `## Sources` et `## Limites` dans les tranches 1 à 4.
  - Synchronisation d'`annexe-E-bibliographie.md` : renvois `(30, 31)` OWASP et `(4, 22, 35)` IMDA en `E.2`, ajout du 4e contrôle en `E.3` (`878` URL publiques distinctes, `5 607` entrées dont `3` ajouts de DOI, `268` remplacements) et précision des confirmations `[32]`/`[27]` au 14 novembre 2026 en `E.4` tout en préservant le constat historique du 13 novembre (`82` / `83`).
- **`Presentation.html` :**
  - Actualisation du nombre de pages (`1 097` → `1 100` pages, 5 occurrences) après recomposition de `CompendiumMaster.pdf`.
  - Remplacement du LaTeX brut `$\text{pass}^5 \ge 99\,\%$` par `pass⁵ ≥ 99 %` (`ADR-031`, `L1406`).
  - Correction du renvoi des niveaux de preuve : `(annexe E)` → `(ouverture, section 0.4)` (`L1364`).
  - Détroncation des cinq descriptions d'`ANNEXES` (`A`, `B`, `D`, `F`, `G`) en `L1407` et suppression des astérisques Markdown bruts dans `B`.

## 4. Sources à accès restreint et lien mort documenté

- **Lien mort conservé comme documenté (`1`) :** `chapitre-23-architecture-reference.md` `[13]` (`gravitee.io/.../blueprinting-an-ai-agent-control-plane-...`), HTTP 404 confirmé le 14 novembre 2026 et déjà consigné explicitement dans la notice `[13]` et `## Limites`.
- **Sources à accès restreint documentées (`266` entrées d'audit : `236` `acces_restreint` + `30` `corrige_acces_restreint`) :** blocages anti-robot, paywalls, délais d'attente ou challenges WAF/Cloudflare sur des sites éditeurs et institutionnels (notamment `www.mckinsey.com`, `www.w3.org`, `doi.org` vers éditeurs IEEE/Elsevier/Springer/ACM, `www.canada.ca`, `www.fortunebusinessinsights.com`, `eur-lex.europa.eu` / `TodayOJ`, `www.preprints.org`, `genai.owasp.org`, `lautorite.qc.ca`, `www.donneesquebec.ca`, `www.gartner.com`).
  - Lors de l'exécution `--en-ligne` (`866` URL distinctes hors code) : `0` nouveau lien mort (`1` `mort_documente` reconnu sur `ch23 [13]`), `0` erreur HTTP 5xx non documentée, `0` redirection permanente non mise à jour (`16` redirections canoniques déjà documentées comme `valide_redirection`), `192/192` identifiants arXiv et `33/33` DOI confirmés sans dérive de métadonnées, `44` accès restreints/anti-bot/TLS éditeur documentés ou DOI vivants, et `1` avertissement de limite de débit HTTP `429` sur `www.codesys.com` (`chapitre-28` `[10]`, L176).

## 5. Outillage créé et résultats des vérifications

- **`Master/compendium-master-references.py` :** script pérenne (mode hors-ligne par défaut + mode `--en-ligne` avec `ThreadPoolExecutor`, timeout `12 s`, sémaphore par hôte, retry `429`/`503`, API `export.arxiv.org`, `doi.org/api/handles` et Crossref).
- **Exécutions finales vérifiées :**
  1. `python Master/compendium-master-verifie.py` → code de sortie `0` : `Tous les contrôles passent.` (`59` fichiers, `1 579` corrections, `1 100` pages, `428 919` mots, `16.3 Mo`).
  2. `python Master/compendium-master-references.py` → code de sortie `0` : `Tous les contrôles de références passent.` (`59` fichiers, `1 033` sources, `1 088` occurrences URL hors code, `554` sections, `97` extraits, `31` ADR, `5 607` entrées d'audit).
  3. `python Master/compendium-master-references.py --en-ligne` → code de sortie `0` : `Tous les contrôles de références passent.` (`866` URL distinctes hors code, `192` ID arXiv, `33` DOI, `0` nouveau lien mort, `0` redirection non documentée, `1` avertissement HTTP `429` sur `codesys.com`).
  4. `node outils/verifier-presentation.mjs` → code de sortie `0` : `Tout est conforme.` (`375x812`, `768x1024`, `1366x768`, `1920x1080` + repli système, contraste minimal `6.15:1`, `0` erreur JS).
