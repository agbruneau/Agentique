# Lot REF-1 — Audit des références et liens de la tranche 1

**Périmètre :** `Master/manuscrit/ouverture.md` et `chapitre-01-entreprise-agentique.md` à `chapitre-11-gouvernance-standards.md` (12 fichiers).  
**Date de vérification :** 14 novembre 2026.  
**Statut :** lots validés par `--essai` uniquement (`REF-1-factuel.json` et `REF-1-harmonisation.json`), non appliqués.

## 1. Synthèse quantitative

L'inventaire complet enregistré dans [audit-ref-1.json](../recherche/audit-ref-1.json) totalise **1 510 entrées** couvrant 100 % des sources, URL publiques, URL illustratives, appels `[n]` et renvois internes de la tranche 1 :

- **Sources bibliographiques (`## Sources`) :** **205** entrées numérotées (`209` URL de sources et `1` source sans URL, `chapitre-07` `[22]`, remplacée par sa source primaire). Aucun `[n]` orphelin ni source non citée; **0** citation `[n]` dans les volets `{.volet}` et dans `ouverture.md`.
- **URL publiques distinctes :** **182** URL distinctes (`178` dans `## Sources` + `4` dans des blocs de code), toutes vérifiées par requête HTTP (`urllib.request`, `User-Agent Mozilla/5.0`, timeout 12 s) et recoupement de titre/métadonnées : **194** occurrences de sources en HTTP 200 (dont **1** faux 200/WAF sur `eur-lex.europa.eu`), **13** occurrences en HTTP 403 et **2** dépassements de délai (`mckinsey.com`).
- **URL fictives d'illustration :** **19** occurrences (`boreal.ca`, `127.0.0.1`, `acier-laurentides.ca`, dont `1` en prose de volet et `18` en blocs de code) vérifiées et conservées intactes.
- **API arXiv, HTML intégral et PDF :** **27** identifiants arXiv distincts contrôlés via l'API arXiv (`export.arxiv.org`), complétés par l'extraction HTML intégrale des versions citées (`2504.08148`, `2506.13538v5`, `2609.14119v1`, `2607.21824v1`, etc.) et `fitz` sur **2** PDF (`mgf-for-agentic-ai.pdf`, 53 p.; `SC00061G_FIPA_ACL.pdf`, 11 p.).
- **Renvois internes :** **505** renvois vérifiés (`258` `chapitre`, `105` `section`, `41` `chapitres`, `26` `Extrait`, `19` `figures/*.svg`, `18` `sections`, `14` `ADR-*`, `13` `Chapitre`, `5` `annexe`, `3` `Chapitres`, `3` `Partie`) — **0** cible manquante.

| Fichier | Sources (URL) | Code public | Fictives | Appels `[n]` | Renvois internes | `REF-1-factuel` | `REF-1-harmonisation` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `ouverture.md` | 0 (0) | 0 | 0 | 0 | 81 | 0 | 0 |
| `chapitre-01-entreprise-agentique.md` | 12 (13) | 0 | 4 | 58 | 61 | 4 | 4 |
| `chapitre-02-genealogie.md` | 12 (12) | 0 | 0 | 62 | 23 | 0 | 3 |
| `chapitre-03-dimensions-interoperabilite.md` | 16 (16) | 0 | 0 | 60 | 27 | 1 | 7 |
| `chapitre-04-etat-des-lieux.md` | 15 (15) | 0 | 0 | 45 | 35 | 1 | 3 |
| `chapitre-05-mcp.md` | 16 (16) | 0 | 2 | 76 | 50 | 0 | 0 |
| `chapitre-06-a2a.md` | 12 (12) | 2 | 11 | 66 | 50 | 1 | 0 |
| `chapitre-07-protocoles-peripheriques.md` | 22 (21) | 0 | 0 | 58 | 29 | 5 | 3 |
| `chapitre-08-decouverte-registres.md` | 27 (27) | 0 | 0 | 95 | 22 | 3 | 3 |
| `chapitre-09-web-agentique.md` | 19 (20) | 0 | 0 | 66 | 14 | 1 | 1 |
| `chapitre-10-commerce-agentique.md` | 20 (23) | 2 | 1 | 92 | 53 | 3 | 5 |
| `chapitre-11-gouvernance-standards.md` | 34 (34) | 0 | 1 | 94 | 60 | 1 | 2 |
| **Total** | **205 (209)** | **4** | **19** | **772** | **505** | **20** | **31** |

## 2. Anomalies relevées et corrections préparées

### 2.1 Cas particulier : `chapitre-07-protocoles-peripheriques.md` source `[22]`

La source `[22]` pointait vers une source secondaire sans URL (« Plan initial du compendium, version 3 ») pour étayer l'absence de normalisation formelle sur ANP. La vérification directe sur IETF Datatracker établit qu'aucun groupe de travail de l'IETF n'a adopté ANP : on y recense uniquement le brouillon individuel expiré [`draft-zyyhl-agent-networks-framework-01`](https://datatracker.ietf.org/doc/draft-zyyhl-agent-networks-framework/) (*Framework for AI Agent Networks*, révision du 20 octobre 2025 avec coauteur de la communauté ANP Open Source, expiré le 23 avril 2026, `Stream: (None)`) et quatre soumissions individuelles `draft-song-anp-*-00` (`adp`, `aip`, `aitp`, `ans`), également expirées le 26 septembre 2026 sans portée normative. `REF-1-factuel` remplace `[22]` par cette source primaire (en trois ancrages respectant la borne `#321` de `corrections.json`) et ajuste l'énoncé à la ligne 67 ainsi que le bandeau de référence.

### 2.2 Constats factuels vérifiés sur API et texte intégral

- **Zhu et coll. (`chapitre-01` `[11]` et `## Limites`) :** l'API Crossref (`10.3390/fi18060326`) confirme la parution dans *Future Internet*, vol. 18, n° 6, art. 326 (15 juin 2026; auteurs Zhu, Liu, Yu et Zhang), alors que `preprints.org` et `mdpi.com` retournent HTTP 403 aux requêtes automatisées. `REF-1-factuel` met à jour `[11]` (hors borne `#316`/`#317`) et corrige `## Limites` (`chapitre-01`).
- **Kandogan et coll. (`chapitre-01` `[3]`, `arXiv 2504.08148`) :** la version `html/2504.08148` omet la référence d'atelier, mais la fiche `abs/2504.08148` affiche explicitement *First Workshop on Data-AI Systems (DAIS), ICDE 2025* (`ICDEW 2025`). `REF-1-factuel` corrige la limite en conséquence.
- **Kraishan (`chapitre-08` `[23]`, `arXiv 2609.14119v1`) :** la section 4.2 du texte HTML indique explicitement `n = 8 900` serveurs à plusieurs versions (`51,09 %` modifiés, `40,58 %` avec au moins une dérive sémantique silencieuse, `4,16 %` ayant redirigé leur hôte distant), levant l'ambiguïté sur le dénominateur des `40,6 %` du résumé.
- **Hasan et coll. (`chapitre-08` `[26]`, `arXiv 2506.13538v5`) :** l'en-tête HTML de `html/2506.13538v5` affiche explicitement `Journal: TOSEM`, absent de `abs/2506.13538`. `REF-1-factuel` consigne cette mention littérale en `## Limites` tout en maintenant la cohérence avec `[27]` relu par extraits (`P2-F3`).
- **Louck (`chapitre-10` `[15]`, `arXiv 2607.21824v1`) :** la table des matières HTML nomme les trois cibles totalisant les 33 vulnérabilités structurelles : **CoralOS** (11), **Fetch.ai uAgents** (8) et **AP2 v0.2.0** (14).

### 2.3 URL déplacées (`REF-1-factuel`) et redirections bénignes

- **10 occurrences d'URL déplacées mises à jour** (7 URL distinctes) :
  - `anthropic.com/engineering/building-effective-agents` -> `https://www.anthropic.com/research/building-effective-agents` (`ch01` `[1]`)
  - `nist.gov/caisi/ai-agent-standards-initiative` -> `https://www.nist.gov/super-intelligence/si-agent-standards-initiative` (`ch01` `[9]`, `ch03` `[11]`, `ch04` `[5]`, `ch11` `[20]`; page `SI Agent Standards Initiative | NIST`, mise à jour le 9 novembre 2026)
  - `lfaidata.foundation/?p=7689` -> `https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/` (`ch06` `[10]`)
  - `learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry` -> `https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview` (`ch08` `[19]`)
  - `developers.cloudflare.com/bots/concepts/bot/signed-agents/` -> `https://developers.cloudflare.com/bots/concepts/bot/verified-bots/` (`ch09` `[14]`, intitulé mis à jour « Verified bots » intégrant les anciens agents signés depuis le 1er juillet 2026)
  - `developer.visa.com/capabilities/trusted-agent-protocol/overview` -> `https://developer.visa.com/docs/trusted-agent-protocol` (`ch10` `[8]`)
  - `inriver.com/resources/b2b-agentic-commerce-retail-protocols/` -> `https://www.inriver.com/resources/blog/b2b-agentic-commerce-retail-protocols/` (`ch10` `[17]`)
- **8 redirections canoniques mineures conservées** (barre oblique finale, sous-domaine `www.`, suppression de `.html` ou paramètre `?bc=OTH`) : documentées dans `audit-ref-1.json` comme `valide_redirection`.
- **URL publiques en blocs de code (4 occurrences conservées) :** `w3.org/ns/did/v1` (HTTP 403 W3C) et `w3id.org/security/suites/jws-2020/v1` (HTTP 200 -> `w3c.github.io/vc-jws-2020/contexts/v1/`) dans `ch06` (`L670`); `w3.org/ns/credentials/v2` (HTTP 403 W3C) et `schemas.agentpayments.org/ap2/v1` (`SSL TLSV1_UNRECOGNIZED_NAME`, URI de contexte JSON-LD illustratif du vocabulaire initial 2025 dans l'Extrait 10.2) dans `ch10` (`L526`).
- **Versions arXiv antérieures citées volontairement :** `2503.13657v2` (`ch03` `[8]`, `ch04` `[2]`), `2510.16558v1` (`ch08` `[24]`) et `2509.25292v1` (`ch08` `[25]`) pointent exactement vers les versions citées et restent en HTTP 200.

### 2.4 Harmonisation post-`P2-F3` (`REF-1-harmonisation`)

Dans 9 chapitres (`ch01`, `ch02`, `ch03`, `ch04`, `ch07`, `ch08`, `ch09`, `ch10`, `ch11`), le lot `P2-F3` avait ajouté en tête de `## Limites de ce chapitre` que les prépublications « d'abord connues par leur seul résumé, ont été relues au-delà du résumé le 14 novembre 2026 », mais avait laissé subsister les anciennes mentions « résumé seulement » / « seul le résumé a été lu » / « d'après son résumé » / « selon son résumé » dans les bandeaux de référence, `## Sources`, le corps (`ch02` L168, `ch03` L88 et L145, `ch08` L205, `ch10` L202) et d'autres puces de `## Limites`. `REF-1-harmonisation` (31 remplacements) met ces formulations en cohérence sans dépasser aucune borne de `corrections.json`.

## 3. Sources à accès restreint (constat du 14 novembre 2026)

| Source / Chapitre | URL testée | Constat HTTP (14 novembre 2026) | Vérification de repli & traitement |
|---|---|---|---|
| `ch01` `[11]` Zhu et coll. | `https://www.preprints.org/manuscript/202604.2147` et `https://www.mdpi.com/1999-5903/18/6/326` | HTTP 403 (`Forbidden`) | Crossref API (`DOI 10.3390/fi18060326`) + `search_web`; `REF-1-factuel` |
| `ch01` `[12]` McKinsey | `https://www.mckinsey.com/capabilities/people-and-organization/...` | Timeout 12 s | `search_web`; daté au 14 novembre 2026 (`REF-1-harmonisation`) |
| `ch02` `[9]` W3C RDF 1.1 | `https://www.w3.org/TR/rdf11-primer/` | HTTP 403 (`Forbidden`) | `search_web`; accès documenté (`REF-1-harmonisation`) |
| `ch03` `[1]` EUR-Lex EIF | `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52017DC0134` | Redirection anti-robot vers `/TodayOJ/index.html` | `search_web` (`COM(2017) 134` annexe 2); accès documenté (`REF-1-harmonisation`) |
| `ch03` `[12]`, `ch07` `[8]`, `ch09` `[17]`, `ch11` `[9]`–`[12]` W3C CG | `w3.org/community/agentprotocol/`, `groups/cg/agentprotocol`, `community/atp/`, `groups/cg/agent-identity/`, `community/agent-conformance/` | HTTP 403 (`Forbidden`) | `search_web`; accès documenté au 14 novembre 2026 (`REF-1-harmonisation`) |
| `ch04` `[11]` McKinsey | `https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai` | Timeout 12 s | Reprises de presse + `search_web`; daté en `Sources` et `Limites` (`REF-1-harmonisation`) |
| `ch04` `[12]` Gartner | `https://www.gartner.com/en/newsroom/press-releases/2025-06-25-...` | HTTP 403 (`Forbidden`) | Reprises + `search_web`; daté en `Limites` (`REF-1-harmonisation`) |
| `ch10` `[18]` Mastercard | `mastercard-agent-pay.html` et `stories/2026/verifiable-intent.html` | HTTP 403 (`Forbidden`) | Résumé de recherche + `fidoalliance.org` (`[20]`); daté (`REF-1-harmonisation`) |
| `ch06` / `ch10` blocs de code | `w3.org/ns/did/v1`, `w3.org/ns/credentials/v2` | HTTP 403 (`Forbidden`) | Identifiants de contexte JSON-LD standards; blocs de code intacts |

## 4. Validation `--essai`

```text
python Master/compendium-master-lot.py Master/lots/REF-1-factuel.json --essai
-> lot REF-1-factuel : 20 remplacements à faire, 0 déjà en place, registre à 1331 entrées (essai, rien d'écrit)

python Master/compendium-master-lot.py Master/lots/REF-1-harmonisation.json --essai
-> lot REF-1-harmonisation : 31 remplacements à faire, 0 déjà en place, registre à 1342 entrées (essai, rien d'écrit)
```

Une simulation en mémoire appliquant les deux lots dans les deux ordres confirme l'absence de conflit mutuel, l'intégrité des blocs de code, des figures SVG et des volets `{.volet}`, ainsi que le respect de toutes les bornes du registre `corrections.json`.
