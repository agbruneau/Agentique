# Compte rendu d'audit — Tranche 5 (`REF-5`)

> **Régime :** Production | **Date des vérifications réseau :** 14 novembre 2026 | **Périmètre :** `chapitre-48` à `chapitre-50` (Partie X), `annexe-A` à `annexe-H`, et lecture seule de [`Presentation.html`](file:///c:/Github/Agentique/2027/Presentation.html) et [`index.html`](file:///c:/Github/Agentique/2027/index.html).

## 1. Statistiques de l'audit

Les 1 165 éléments vérifiés sont consignés dans [`Master/recherche/audit-ref-5.json`](file:///c:/Github/Agentique/2027/Master/recherche/audit-ref-5.json) :

| Type d'élément | Fichiers couverts | Total | Détail / issue |
|---|---|---|---|
| Entrées `## Sources` (= URL hors code, Partie X) | `chapitre-48` (101), `chapitre-49` (68), `chapitre-50` (75) | 244 | 244 URL uniques; numérotation `1..N` continue, 0 trou |
| URL hors code (annexes) | `annexe-E` (E.2 : 31, E.4 : 10); autres annexes : 0 | 41 | 269 URL distinctes sur l'ensemble des 285 occurrences |
| URL publiques dans des blocs de code | 11 fichiers de la tranche 5 | 0 | Aucune URL publique réelle en bloc de code |
| Appels `[n]` (corps + limites) | `chapitre-48` (130), `chapitre-49` (127), `chapitre-50` (157) | 414 | 100 % des sources citées; 0 appel orphelin |
| Renvois internes (`chapitre`, `section`, `annexe`, `ADR`, `fig-`, tables, glossaire) | 11 fichiers de la tranche 5 | 466 | 463 valides sans modification; 2 renvois incomplets corrigés (`annexe-E` L45, L60) et 1 renvoi d'incohérence corrigé (`chapitre-48` L509) |
| **Total enregistré** | **11 fichiers** | **1 165** | **43 corrections préparées (0 invalide non résolu)** |

## 2. Lots préparés et validés (`--essai` uniquement)

Trois lots commutatifs (ancres strictement disjointes) ont été générés sans être appliqués :

1. [`Master/lots/REF-5-factuel.json`](file:///c:/Github/Agentique/2027/Master/lots/REF-5-factuel.json) (`categorie: "factuel"`, **29 remplacements**) :
   - [`chapitre-48-revue-litterature.md`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-48-revue-litterature.md) (**19**) :
     * `[32]` : remplacement du lien Consensus redirigeant vers `/sign-up/` par l'adresse arXiv confirmée [`https://arxiv.org/abs/2603.07670`](https://arxiv.org/abs/2603.07670) (Pengfei Du, 8 mars 2026) et mise à jour cohérente de la ligne 49 en préservant l'historique du 13 novembre (`82/83`, aligné sur `fig-48-e1.svg`).
     * `[27]` : ajout de l'auteur vérifié **Sergey Emelyanov** depuis la page cible du DOI (`https://icaimt.com/2026/agentic-ai.html`, absent de Crossref).
     * `[87]`–`[96]` et `[98]`–`[101]` (**14 notices**) : compléments de dates de publication arXiv, numéros de version (`/html/...vN`), sous-titres complets et auteurs manquants (`[91]` *Xing et coll.*, `[95]` *She et Lin*, `[98]` *Goddard, Roudsari et Wyatt*, *JAMIA* vol. 19, no 1, 2012, p. 121-127, `[100]` *Computer Law & Security Review* 45, 2022 et arXiv 2021). `[97]` (Statistique Canada) était déjà complet.
     * `## Limites de ce chapitre` (**L506 et L509**) : alignement de la ligne 509 (issue de `#525` du registre, sans débord) et de la ligne 506 sur le profil recalculé en section 48.2 (l. 72 : `789`; l. 94 : `709` sources du 13 novembre classées par adresse + `80` ajouts classés à la main).
   - [`chapitre-49-veille-technologique.md`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-49-veille-technologique.md) (**6**) :
     * `[2]` et `[20]` : mise à jour des anciens chemins NIST (`cosais`, `caisi/ai-agent-standards-initiative`) vers les URL canoniques après renommage (`cosis`, `super-intelligence/si-agent-standards-initiative`) et précision des titres correspondants.
     * `[26]` : remplacement du permalien WordPress `?p=248010` par l'URL canonique SAP TechEd.
     * `[39]`, `[40]`, `[41]` : remplacement des URL de brouillons IETF (`draft-ietf-*`) par les URL canoniques des RFC publiées déjà nommées (`rfc10024/`, `rfc9964/`, `rfc10073/`).
   - [`chapitre-50-projection-etude-marche.md`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-50-projection-etude-marche.md) (**4**) :
     * `[29]` : `ai-inference-price-trends` → URL canonique `llm-inference-price-trends`.
     * `[32]` : `?p=122385` → URL canonique IDC FutureScape 2027.
     * `[66]` : ancien chemin TechTarget → URL canonique `/news/Dynatrace-acquires-Arize-for-AI-agent-development/846446/`.
     * `[72]` : `?p=298626` → URL canonique IT-Online.
2. [`Master/lots/REF-5-harmonisation.json`](file:///c:/Github/Agentique/2027/Master/lots/REF-5-harmonisation.json) (`categorie: "harmonisation"`, **12 remplacements**) :
   - [`chapitre-48-revue-litterature.md`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-48-revue-litterature.md) (**12**) : harmonisation de 9 notices à exactement deux auteurs écrites `et coll.` vers `X et Y` (`[4]` *Chang et Geng*, `[10]` *Ahmad et Hassan*, `[23]` *Oyewale et Soru*, `[28]` *Tanudjaja et Hutajulu*, `[52]` *Tran et Kiela*, `[55]` *Bertalanič et Fortuna*, `[70]` *Mandarapu et Kunkunuru*, `[71]` *Tuan et Sanyal*, `[82]` *Hacker et Holweg`), par alignement sur `[24]`, `[30]`, `[77]`, `[83]`, `[84]`, `[88]`, `[97]`; ajout de l'année sur `[84]` (`2026`), `[85]` (`2025`) et `[86]` (`2025`).
3. [`Master/lots/REF-5-renvoi.json`](file:///c:/Github/Agentique/2027/Master/lots/REF-5-renvoi.json) (`categorie: "renvoi"`, **2 remplacements**) :
   - [`annexe-E-bibliographie.md`](file:///c:/Github/Agentique/2027/Master/manuscrit/annexe-E-bibliographie.md) (**2**, § E.2) :
     * `L45` : ajout du chapitre `30` manquant pour `OWASP MCP Top 10` (`(31)` → `(30, 31)` — cité en source `[14]` de `chapitre-30-autorisation-delegation.md` l. 230).
     * `L60` : ajout du chapitre `35` manquant pour `IMDA v1.5` (`(1, 3, 22, 39)` → `(1, 3, 22, 35, 39)` — cité en source `[4]` de `chapitre-35-cadres-internationaux.md` l. 267).

Validation `--essai` exécutée sur chaque lot :
- `python Master/compendium-master-lot.py Master/lots/REF-5-factuel.json --essai` → `lot REF-5-factuel : 29 remplacements à faire, 0 déjà en place, registre à 1340 entrées (essai, rien d'écrit)` (code `0`).
- `python Master/compendium-master-lot.py Master/lots/REF-5-harmonisation.json --essai` → `lot REF-5-harmonisation : 12 remplacements à faire, 0 déjà en place, registre à 1323 entrées (essai, rien d'écrit)` (code `0`).
- `python Master/compendium-master-lot.py Master/lots/REF-5-renvoi.json --essai` → `lot REF-5-renvoi : 2 remplacements à faire, 0 déjà en place, registre à 1313 entrées (essai, rien d'écrit)` (code `0`).
- Simulation en mémoire des trois lots dans les 6 permutations d'application (`1 354` entrées finales) : aucun débordement ni retour dans `corrections.json`, et toutes les règles Partie X (`1..N` continu, 100 % cité, aucune ligne à double `$` LaTeX) passent.

## 3. Autres constats dans la tranche 5 (non modifiés dans les lots)

- **`chapitre-50 [58]` (`ciodive.com`, HTTP 403 Cloudflare) :** L'article `824530` (234 G$ US exposés) est confirmé via `search_web`, mais le slug canonique indexé est `agentic-ai-to-disrupt-234b-in-saas-spending-gartner/824530/` au lieu de `agentic-ai-disrupt-234-billion-saas-spending/824530/` dans le manuscrit. La protection Cloudflare 403 empêchant de vérifier la redirection HTTP, l'URL est laissée intacte et signalée ici.
- **`chapitre-50 [3]` (`Mordor Intelligence`) :** Le grattage texte sans JavaScript (38 000 caractères) confirme `9,9` et `2032`; `82,3` et `42,4` n'apparaissent pas dans l'extrait statique non rendu par navigateur.
- **`chapitre-50 [28]` et `[45]` (PDF complets) :** Les lectures partielles tronquées ne montraient pas tous les chiffres; le téléchargement complet et l'extraction intégrale par `pymupdf` confirment tous les nombres cités (`344,7 G$`, `127,5 %`, `170,9 G$`, Canada `4,28` / 5e rang pour Stanford HAI `[28]`; `1,65 G$`, `2,7 G$`, `500 M$` pour le Budget 2026 `[45]`).
- **`chapitre-49 [44]` (NVD) et `[5]` (`benchmark_results_1_1.yaml`) :** Requête directe sur l'API JSON de la NVD (`102` CVE de juillet à octobre 2026 : `16, 8, 56, 22`, `13` avec score >= 9,0, `2` avec score 10,0 `CVE-2026-59971` et `CVE-2026-77244`) et lecture YAML METR (`187.778`, `128.744 [104.428, 158.012]`) conformes au texte.
- **Annexes A à H :**
  - Tous les invariants structurels vérifiés (`annexe-A` sans ligne C supprimée ni nouveau sigle, `annexe-F` et `annexe-G` identiques octet pour octet entre `Master/manuscrit/` et `Master/fusion/reecrit/`, `annexe-H` à 1 section `## `, 0 puce `- ` et tableau inchangé).
  - [`annexe-E-bibliographie.md`](file:///c:/Github/Agentique/2027/Master/manuscrit/annexe-E-bibliographie.md) :
    * **E.1 et E.4 :** Les décomptes globaux du manuscrit (`789` sources dans les ch. 1–47 + `244` en partie X = `1 033`; ch. 48 : `101 = 31 + 52 + 3 + 15`; ch. 49 : `68 = 46 + 21 + 1`; ch. 50 : `75 = 51 + 24`) sont exacts. À noter toutefois dans les ch. 1–47 : `783` sources sur `789` suivent strictement le motif `k. [Titre](URL)`, les `6` autres (`ch 7 [22]`, `ch 10 [19]`, `ch 20 [19]`, `ch 23 [21]`, `ch 30 [5]`, `ch 46 [15]`) ayant une syntaxe atypique ou sans lien.
    * **E.2 :** Contrôle complet des 31 URL d'ancrage face aux chapitres 1 à 47 : outre les deux renvois complétés par `REF-5-renvoi.json` (`L45` chapitre `30` et `L60` chapitre `35`), toutes les listes de chapitres sont exactes. Les redirections `L39` (`caisi` → `si-agent-standards-initiative`), `L45` (`www-project-mcp-top-10/` → `projects/mcp-top-10`) et `L55` (`engineering/building-effective-agents` → `research/building-effective-agents`) restent volontairement alignées sur les chapitres 1–47.
    * **E.3 :** Le tableau `### Contrôles faits le 14 novembre 2026` est déjà présent dans le manuscrit (`P2-cloture`).
    * **E.4 (`L99`) :** Après application de `REF-5-factuel.json`, l'intégrateur peut optionnellement ajouter que l'identifiant arXiv de `[32]` et l'auteur de `[27]` ont été confirmés à l'audit du 14 novembre (la mention `82` restant exacte pour la requête automatique du 13 novembre).

## 4. Sources à accès restreint ou blocage technique (relevé du 14 novembre 2026)

Au 14 novembre 2026, **30** occurrences d'URL sur 285 (28 bloquées/redirigées sans API/moteur de recherche, plus 2 requêtes SEC EDGAR exigeant un `User-Agent` déclaré) ont présenté une restriction d'accès HTTP directe ; toutes ont été vérifiées par une voie de repli documentée (sans contournement de CAPTCHA) :

| Fichier / Source | Statut HTTP / erreur (14 nov. 2026) | Cause observée | Voie de vérification alternative (14 nov. 2026) |
|---|---|---|---|
| `chapitre-48` `[3]`, `[5]`, `[23]` & `annexe-E` L118 (`doi.org` → `ieeexplore.ieee.org`) | HTTP `202` | Défi JS anti-robot IEEE Xplore | API Crossref (titres, auteurs, années conformes) |
| `chapitre-48` `[4]`, `[6]`, `[8]`, `[14]`, `[20]` (`doi.org` → `dl.acm.org`) | HTTP `403` | Protection Cloudflare (`Just a moment...`) | API Crossref |
| `chapitre-48` `[18]`, `[31]` (`doi.org` → `mdpi.com`) | HTTP `403` | Protection anti-robot MDPI (`Access Denied`) | API Crossref |
| `chapitre-48` `[24]` (`doi.org` → `science.org`) | HTTP `403` | Protection Cloudflare (`Just a moment...`) | API Crossref |
| `chapitre-48` `[25]`, `[26]` (`doi.org` → `pubsonline.informs.org`) | HTTP `403` | Protection Cloudflare (`Just a moment...`) | API Crossref |
| `chapitre-48` `[9]` (`doi.org` → `linkinghub.elsevier.com`) | HTTP `200` (`Redirecting`) | Redirection JS côté client vers ScienceDirect | API Crossref |
| `chapitre-48` `[10]` (`doi:10.35444/ijana.2026.17605` → `www.ijana.in`) | Erreur TLS (`0`, `SSL: WRONG_VERSION_NUMBER`) | Certificat/TLS défaillant; HTTP redirige vers `safebrowse.io/warn.html` | API Crossref (*Ahmad & Hassan*, 2026, *IJANA*) |
| `chapitre-49` `[13]`, `[14]` (`w3.org`) | HTTP `403` | Protection Cloudflare (`Just a moment...`) | `search_web` (charte *Web & AI IG* et *AI Agent Protocol CG*) |
| `chapitre-50` `[7]`, `[10]`, `[12]`, `[15]` (`fortunebusinessinsights.com`) | HTTP `403` | Protection Cloudflare (`Just a moment...`) | `search_web` (identifiants `111574`, `109835`, `102042`, `114233`) |
| `chapitre-50` `[23]`, `[25]` (`sec.gov/Archives/edgar/...`) | HTTP `403` (UA générique) → HTTP `200` (UA SEC) | Politique d'identification SEC EDGAR | Requête HTTP `200` avec `User-Agent` conforme (chiffres T3 2026 vérifiés) |
| `chapitre-50` `[37]` (`bcg.com`) | HTTP `403` | Pare-feu Akamai (`Access Denied`) | `search_web` (*BCG Applied AI Index*, 30 sept. 2026) |
| `chapitre-50` `[53]` (`01net.it`) | HTTP `403` | Protection Cloudflare (`Just a moment...`) | `search_web` (reprise Omdia 22 sept. 2025 sur `informa.com`) |
| `chapitre-50` `[57]`, `[58]` (`ciodive.com`) | HTTP `403` | Protection Cloudflare | `search_web` (prévision Gartner `2 520 G$ US`; article `824530` / `234 G$ US`) |
| `chapitre-50` `[67]` (`newmarketpitch.com`) | HTTP `429` | Limitation de débit (`Too many requests`) | `search_web` (traceur M&A confirmé) |
| `annexe-E` L59 (`eur-lex.europa.eu/eli/reg/2026/1744/oj/eng`) | HTTP `200` → `/TodayOJ/index.html` | Redirection CloudFront générique hors session navigateur | `search_web` (Règlement UE `2026/1744`, JO 24 juil. 2026, entrée en vigueur 27 juil. 2026) |

*(Note : `chapitre-49` `[18]` et `[19]` sur `itu.int` ont expiré dans le lot initial, puis répondu HTTP `200` sur relance ciblée avec confirmation via `search_web` des cotes `F.748.93` et `Y.supp.NAC-roadmap`.)*

## 5. Vérification en lecture seule de `Presentation.html` et `index.html`

- **Liens locaux :** Tous les liens internes de [`index.html`](file:///c:/Github/Agentique/2027/index.html) (`Presentation.html`) et de [`Presentation.html`](file:///c:/Github/Agentique/2027/Presentation.html) (`CompendiumMaster.pdf`, `../2026/Presentation.html`) pointent vers des fichiers existants.
- **Compteurs :** `CompendiumMaster.pdf` compte exactement **1 097 pages** (`pymupdf`), ce qui correspond aux 5 mentions `1 097` de `Presentation.html`. Les autres compteurs (`50 chapitres`, `10 parties`, `31 volets`, `8 annexes A à H`, `31 ADR`, `75 points`, `1 033 sources = 789 + 244`, `83 résumés`, `15 travaux hors protocole`, `182` chiffres vérifiables au 14 nov. 2026) sont exacts face au manuscrit actuel.
- **Écarts relevés dans `Presentation.html` (à corriger par `@integrateur`) :**
  1. `L1406` (`CHAPTERS`, `ADR-031`) : le champ `invariant` renferme du LaTeX brut (`$\text{pass}^5 \ge 99\,\%$`, échappé `$\\text{pass}^5 \\ge 99\\,\\%$`) rendu littéralement par `esc(a.invariant)` sans moteur LaTeX, alors que `L1504` emploie la forme Unicode `pass⁵ ≥ 99 %`.
  2. `L1364` : le titre `Rigueur et limites déclarées : les quatre niveaux de preuve (annexe E)` attribue à l'annexe E les quatre marqueurs `[N]/[M]/[É]/[S]`, alors que ceux-ci sont définis dans [`Master/manuscrit/ouverture.md`](file:///c:/Github/Agentique/2027/Master/manuscrit/ouverture.md#L137) (section 0.4, l. 137) et absents d'`annexe-E-bibliographie.md`.
  3. `L1407` (`ANNEXES`) : cinq descriptions sur huit (`A`, `B`, `D`, `F`, `G`) sont tronquées en plein mot sans point de suspension (`(Age`, `que le protocole`, `(13 novembre`, `deux arbres de`, `cette revu`).
- **Action post-recomposition pour `@integrateur` :** Après application de `REF-5-factuel.json`, `REF-5-harmonisation.json` et `REF-5-renvoi.json` puis recomposition Typst du PDF, vérifier si le nombre de pages reste à `1 097`; le cas échéant, mettre à jour `Presentation.html` avec les écarts ci-dessus et relancer `node outils/verifier-presentation.mjs`.

## 6. Constats hors périmètre signalés pour suite

- [`chapitre-24` `[15]`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-24-passerelles-execution.md) (*MCP-Guard*, `arXiv 2508.10991v4`) omet également ses auteurs (`Xing et coll.`), comme `[91]` avant correction dans `REF-5-factuel.json`.
- [`chapitre-8` `[24]`, `[25]`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-08-evaluation-securite-mcp.md) et [`chapitre-20` `[20]`](file:///c:/Github/Agentique/2027/Master/manuscrit/chapitre-20-cadriciels-orchestration.md) citent des URL `/html/...v1` dont le titre a évolué entre `v1` et `v2`/`v4` sur `/abs/` (`2510.16558`, `2509.25292`, `2604.08906`).
