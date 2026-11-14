# Compte rendu d'audit — Tranche 4 (`REF-4`)

> **Régime :** Production | **Date des vérifications réseau :** 14 novembre 2026 | **Périmètre :** [`chapitre-38-canada-quebec.md`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-38-canada-quebec.md) à [`chapitre-47-ingenierie-agentique-interne-distillation.md`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-47-ingenierie-agentique-interne-distillation.md) (10 fichiers).

## 1. Statistiques de l'audit

Les **1 427** éléments audités sont consignés dans [`Master/recherche/audit-ref-4.json`](file:///c:/Github/Agentique/2027/Master/recherche/audit-ref-4.json) :

| Type d'élément | Répartition | Total | Détail / issue |
|---|---|---|---|
| Notices `## Sources` | 10 chapitres (157 enregistrements, car `ch45 [15]` porte 2 URL et `ch46 [15]` n'a aucune URL) | 156 notices (156 URL) | Numérotation continue `1..N`, 0 trou, 0 source non citée |
| URL hors `## Sources` et hors code | 10 chapitres | 0 | Aucune URL en clair dans l'exposé ni dans `## Limites` |
| URL publiques réelles en blocs de code (`{.volet}`) | `chapitre-45` (`odrl.jsonld`, `tractusx`) | 2 | Conservées intactes (voir section 3) |
| URL fictives / locales illustratives (`{.volet}`) | `ch38` (1), `ch44` (4), `ch45` (1), `ch46` (1) | 7 | 6 `*.boreal.ca` + 1 `.svc.cluster.local:9443` conservées |
| Appels `[n]` | Exposé : 530; `## Limites` : 159; `{.volet}` : 0 | 689 | 689/689 rattachés; 0 appel orphelin; 0 appel en volet |
| Renvois internes (`Chapitre`, `section`, `Extrait`, `ADR-`, `Annexe`, `fig-`, tableaux) | Exposé : 263; `{.volet}` : 280; `## Limites` : 22; `## Sources` : 7 | 572 | 572/572 cibles vérifiées existantes (`Extrait 34.1` inclus) |
| **Total enregistré** | **10 chapitres (165 occurrences d'URL, 154 URL uniques)** | **1 427** | **100 % couvert** |

## 2. Anomalies relevées et lots préparés (`--essai` uniquement)

Trois lots disjoints et séquentiellement compatibles (**61 remplacements** au total, **non appliqués**) ont été validés par `Master/compendium-master-lot.py` :

1. [`Master/lots/REF-4-renvoi.json`](file:///c:/Github/Agentique/2027/Master/lots/REF-4-renvoi.json) (`categorie: "renvoi"`, **10 remplacements**) :
   - [`chapitre-38`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-38-canada-quebec.md) `[22]` : correction du lien brisé de l'AMF (`/files/pdf/.../vol23no13_5.pdf`) vers l'adresse officielle de la section 5.2.2 du *Bulletin de l'AMF* du 2 avril 2026 (`https://lautorite.qc.ca/fileadmin/lautorite/bulletin/2026/vol23no13/vol23no13_5-2.pdf`, décision n° `2026-PDG-0016`, confirmée par `search_web`; le serveur maintient HTTP 403 Cloudflare).
   - [`chapitre-39`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-39-gouvernance-interne.md) `[7]` et `[9]`, [`chapitre-40`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-40-finops-agentique.md) `[6]` et `[11]`, [`chapitre-43`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-43-maturite-prospective.md) `[2]`, [`chapitre-44`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-44-plan-donnees-inference-routage.md) `[3]`, [`chapitre-47`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-47-ingenierie-agentique-interne-distillation.md) `[2]` (**7 redirections permanentes HTTP 301/308**) : mise à jour vers les URL canoniques (`microsoft-agent-365/admin/agent-registry-overview`, `entra/agent-id/agent-owners-sponsors-managers`, `anthropic.com/research/...`, `www.linuxfoundation.org/...`, `nist.gov/super-intelligence/si-agent-standards-initiative` avec renommage *SI Agent Standards Initiative*, `agentgateway.dev/docs/standalone/latest/documentation/llm/`, `github.com/scip-code/scip`). Les redirections temporaires `302` (`docs.vllm.ai/en/latest/features/lora.html`, `gleif.org/en/vlei/...`) sont conservées.
   - [`chapitre-45`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-45-reseaux-b2b-federes.md) `[15]` : mise à jour de l'intitulé `draft-hood-agtp-lei-00` → `draft-hood-agtp-lei-01` (30 octobre 2026, version active sur Datatracker) et mention de la date interne (septembre 2026) du document de travail GLEIF.
   - [`chapitre-46`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-46-inference-confidentielle-resilience-ia-physique.md) `[15]` : ajout du DOI canonique vérifié via Crossref (`https://doi.org/10.1109/ms.2001.936213`, HTTP 200, *IEEE Software*, vol. 18, n° 4, p. 20-28, juillet-août 2001 — l'identifiant `10.1109/52.936214` retournant HTTP 404).

2. [`Master/lots/REF-4-factuel.json`](file:///c:/Github/Agentique/2027/Master/lots/REF-4-factuel.json) (`categorie: "factuel"`, **12 remplacements**) :
   - [`chapitre-38`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-38-canada-quebec.md) (**8**) : correction du statut de `[16]` Blakes (HTTP 200 lu en texte intégral, daté du 17 juillet 2026), de `[17]` Directive fédérale (HTTP 200 avec en-têtes navigateur : modification du 24 juin 2025, §§ 1.2.1-1.2.2 au 24 juin 2026, niveaux I–IV aux annexes B et C), de la consultation de `P-39.1` sur LégisQuébec (HTTP 200 avec en-têtes navigateur, à jour au 15 octobre 2026, art. 12.1 inchangé depuis 2021) et de la limite sur `[22]` AMF.
   - [`chapitre-46`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-46-inference-confidentielle-resilience-ia-physique.md) (**1**) : alignement de l'État de référence pour `[15]` (DOI Crossref vérifié).
   - [`chapitre-47`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-47-ingenierie-agentique-interne-distillation.md) (**3**) : ajout de la version courante **Project Nessie `0.110.0`** affichée dans la navigation du site (corrigeant l'affirmation contraire en `## Limites`) et correction de l'erreur sur `max_loras` (paramètre bien nommé à deux reprises sur la page de documentation vLLM).

3. [`Master/lots/REF-4-coherence.json`](file:///c:/Github/Agentique/2027/Master/lots/REF-4-coherence.json) (`categorie: "coherence"`, **39 remplacements**) :
   - Harmonisation des **28** notices et mentions résiduelles « résumé seulement » sur les sources relues par extraits le 14 novembre 2026 (`#826`–`#832`, chapitres `40`, `41`, `42`, `43`, `44`, `45`, `47`).
   - Consignation datée du **14 novembre 2026** des accès restreints dans `## Limites` (chapitres `38`, `39`, `41`, `42`, `45`, `46`).

Validation `--essai` exécutée sur chaque lot (0 débord sur `Master/audit/corrections.json`, 0 collision séquentielle) :
- `python Master/compendium-master-lot.py Master/lots/REF-4-renvoi.json --essai` → `lot REF-4-renvoi : 10 remplacements à faire, 0 déjà en place, registre à 1321 entrées (essai, rien d'écrit)` (code `0`).
- `python Master/compendium-master-lot.py Master/lots/REF-4-factuel.json --essai` → `lot REF-4-factuel : 12 remplacements à faire, 0 déjà en place, registre à 1323 entrées (essai, rien d'écrit)` (code `0`).
- `python Master/compendium-master-lot.py Master/lots/REF-4-coherence.json --essai` → `lot REF-4-coherence : 39 remplacements à faire, 0 déjà en place, registre à 1350 entrées (essai, rien d'écrit)` (code `0`).

## 3. Invariants des volets et points à coordonner avec `Master/fusion/reecrit/`

- Aucun appel `[n]` ni aucune liste de sources dans les volets `{.volet}` ; les **7** URL illustratives (`6` `*.boreal.ca`, `1` `warranty-agent.bca.svc.cluster.local:9443`), les figures `*.svg` et les formules sont laissées intactes.
- **Cas Tractus-X (`chapitre-45` L367 / `Master/fusion/reecrit/chapitre-45-volet-a.md`) :** dans le bloc de code JSON-LD du volet de [`chapitre-45`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-45-reseaux-b2b-federes.md), l'URI `https://w3id.org/tractusx/v2.0/context.jsonld` redirige vers la page d'accueil `https://eclipse-tractusx.github.io/` sans servir de contexte JSON-LD. Elle est **conservée intacte** dans les lots `REF-4` afin de préserver la conformité stricte de `fus.controle` avec [`Master/fusion/reecrit/chapitre-45-volet-a.md`](file:///c:/Github/Agentique/2027/Master/fusion/reecrit/chapitre-45-volet-a.md).
- **Cas Carlini / canaris (`chapitre-47` L1107 / [`Master/fusion/reecrit/chapitre-47-volet-c.md`](file:///c:/Github/Agentique/2027/Master/fusion/reecrit/chapitre-47-volet-c.md) L183) :** dans le volet de [`chapitre-47`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-47-ingenierie-agentique-interne-distillation.md) (L1107, miroir exact de `chapitre-47-volet-c.md` L183), la phrase « *le résumé lu de l’article de Carlini ne décrit ni les canaris ni la métrique d’exposition...* » contredit L266 mise à jour par `REF-4-coherence.json` (relecture par extraits du 14 novembre 2026, `#832`). Afin de ne pas rompre l'invariant `fus.controle` (`compendium-master-verifie.py`) ni modifier `Master/fusion/`, L1107 est **conservée intacte** dans `REF-4`, L266 signale cette conservation dans le texte, et la divergence est consignée ici pour `@integrateur` en vue d'une éventuelle mise à jour synchronisée de `chapitre-47-volet-c.md` L183 et de `chapitre-47` L1107.

## 4. Sources à accès restreint ou filtrage automatisé (relevé du 14 novembre 2026)

| Chapitre(s) / Source | Hôte / URL | Statut observé le 14 novembre 2026 | Recoupement et suite donnée |
|---|---|---|---|
| `ch38 [2],[5],[6],[18]`, `ch39 [4]`, `ch45 [13]` | `www.canada.ca` (6 occurrences, 5 URL) | `TimeoutError` (12 s) | Relecture antérieure + `search_web`; fiche `BT22-298/2026F-PDF` HTTP 200 sur `publications.gc.ca`; daté dans `REF-4-coherence`. |
| `ch38 [17]` | `www.tbs-sct.canada.ca/pol/doc-fra.aspx?id=32592` | WAF (`Request Rejected`) sur UA simple; **HTTP 200** avec en-têtes navigateur | Lecture directe confirmant `2025-06-24`, §§ 1.2.1-1.2.2 et annexes B-C; corrigé dans `REF-4-factuel`. |
| `ch38` (art. 12.1) | `www.legisquebec.gouv.qc.ca/fr/document/lc/P-39.1` | HTTP 403 sur UA simple; **HTTP 200** avec en-têtes navigateur | Recueil à jour au 15 octobre 2026 confirmant l'art. 12.1 inchangé depuis 2021; corrigé dans `REF-4-factuel`. |
| `ch38 [22]` | `lautorite.qc.ca` (`vol23no13_5.pdf` → `vol23no13_5-2.pdf`) | HTTP 403 Cloudflare (`Just a moment...`) | URL officielle confirmée par `search_web` (`2026-PDG-0016`, 2 avril 2026); corrigée dans `REF-4-renvoi` et `REF-4-factuel`. |
| `ch39 [1]`, `ch41 [1]–[4]` | `www.mckinsey.com` (5 URL) | `TimeoutError` (12 s) | Accès restreint daté au 14 novembre 2026 dans `REF-4-coherence`. |
| `ch42 [9]` | `www.donneesquebec.ca` (portrait IA) | HTTP 202 (défi JS navigateur) | Daté au 14 novembre 2026 dans `REF-4-coherence`. |
| `ch42 [12]` | `www.servicenow.com/.../orlando-marquez-gene-cain2025.html` | `TimeoutError` (12 s) | Notice CAIN 2025 confirmée par `search_web`; daté dans `REF-4-coherence`. |
| `ch45 [1]` et `{.volet}` | `www.w3.org/TR/odrl-model/`, `www.w3.org/ns/odrl.jsonld` | HTTP 403 Cloudflare (`Just a moment...`) | Spécification ODRL 2.2 confirmée par `search_web`; datée dans `REF-4-coherence`; URI en volet conservée. |
| `ch46 [1]` | `www.intel.com/.../trust-domain-extensions/overview.html` | HTTP 403 Akamai (`Access Denied`) | Confirmé par `search_web`; daté au 14 novembre 2026 dans `REF-4-coherence`. |
| `ch46 [12]` | `www.iso.org/standard/73933.html` (`ISO 10218-1:2025`) | HTTP 403 Cloudflare intermittent (200 sur 1/3 essais) | Édition et date confirmées; daté au 14 novembre 2026 dans `REF-4-coherence`. |
