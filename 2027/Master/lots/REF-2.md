# Compte rendu d'audit — Lot REF-2 (Tranche 2, chapitres 12 à 24)

**Date d'audit :** 14 novembre 2026  
**Périmètre :** `Master/manuscrit/chapitre-12-couche-semantique-ontologies.md` à `chapitre-24-passerelles-integration.md` (13 fichiers)  
**Livrables produits :**
- `Master/recherche/audit-ref-2.json` (790 entrées de vérification)
- `Master/lots/REF-2-factuel.json` (21 remplacements factuels et bibliographiques, catégorie `factuel`)
- `Master/lots/REF-2-coherence.json` (36 remplacements de cohérence éditoriale post-`P2-F3`, catégorie `coherence`)
- `Master/lots/REF-2.md` (présent compte rendu)

---

## 1. Statistiques de vérification

| Catégorie auditée | Volume vérifié | Résultat |
|---|---|---|
| Entrées `## Sources` | 242 entrées (246 occurrences d'URL + 1 entrée sans URL) | 233 sans erreur factuelle (dont 31 harmonisées dans `REF-2-coherence` seul et 3 dans les deux lots); 9 entrées corrigées ou précisées dans `REF-2-factuel` (2 corrections factuelles dans le texte, 3 anomalies d'URL/barrière, 2 parutions à compléter, 2 précisions bibliographiques) |
| URL publiques uniques vérifiées (`## Sources` + blocs code) | 240 URL (236 sources + 4 schémas/namespaces en blocs de code) | 227 HTTP `200`, 8 HTTP `403`, 3 HTTP `404`, 2 `TimeoutError` (12 s) |
| URL dans les blocs de code (`{.volet}`) | 13 URL (4 publiques XML/JSON Schema + 9 fictives `boreal.ca`) | Intactes (invariants de volet préservés) |
| URL hors `## Sources` dans la prose | 0 | Aucune URL flottante en prose |
| Appariement des appels `[n]` | 13 chapitres | 100 % d'appariement `1..N` hors code; 0 appel dans `{.volet}` |
| Renvois internes | 517 renvois (`313` chapitres, `149` sections, `21` extraits, `18` figures, `15` ADR, `1` mention EU AI Act annexe I/III en ch. 22) | 0 renvoi interne cassé |
| Corrections préparées (`--essai` OK) | 57 remplacements sur 11 chapitres (impact maximal +1,72 % de mots sur ch. 20) | 0 débordement ni retour dans `Master/audit/corrections.json` |

---

## 2. Anomalies factuelles et bibliographiques relevées (`REF-2-factuel.json`, 21 remplacements)

1. **`chapitre-14-memoire.md` [26] — *Portable Agent Memory* (`arXiv 2605.11032`, 1 remplacement)**  
   La ligne 114 affirmait que le résumé « ne donne aucun résultat chiffré sur la fidélité du transfert [26] ». La lecture directe du PDF intégral (`HTTP 200`, 16 pages, section 5.2) révèle des mesures quantitatives : dans des essais pilotes sur 30 questions sondes (paire Claude vers GPT-4), la fidélité de réhydratation moyenne (`RHF`) décroît de `0,91` à plein budget (`8 192` jetons) à `0,71` à `25 %` du budget (`2 048` jetons), et l'approche obtient un gain moyen de `2,4` fois entre modèles par rapport à une base sans mémoire à `0,35`, sans validation externe en production. Le texte est corrigé en L114.

2. **`chapitre-14-memoire.md` [33] — Google Cloud Memory Bank (URL déplacée et descriptif inexact, 3 remplacements)**  
   L'URL `https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview` redirige (HTTP 200) vers la page générique `/gemini-enterprise-agent-platform/scale`. La fiche officielle Memory Bank se trouve désormais à `https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank` (HTTP 200, mise à jour du `2026-11-12 UTC`). Contrairement à ce qu'affirme la ligne 130, cette page documente l'extraction et la consolidation par modèle de langage, l'isolement par portée (`scope`), l'expiration automatique par durée de vie (`TTL`) ainsi que les risques d'injection de prompt et d'empoisonnement de la mémoire.

3. **`chapitre-16-topologies-patrons.md` [12] et `chapitre-20-cadriciels-orchestration.md` [15] — Relevé de Zhu et coll. (parution confirmée dans *Future Internet*, 4 remplacements)**  
   La prépublication `https://www.preprints.org/manuscript/202604.2147` retourne HTTP `403`. L'API Crossref (`HTTP 200`) confirme toutefois que l'article est paru sous le même titre dans *Future Internet*, vol. 18, n° 6, art. 326 (15 juin 2026), DOI `10.3390/fi18060326` (auteurs : Yiwen Zhu, Lihe Liu, Jiaqian Yu, Di Zhang), alors que les deux chapitres affirmaient qu'aucune parution n'avait été confirmée. La page MDPI (`https://www.mdpi.com/1999-5903/18/6/326`) retourne également HTTP `403` aux requêtes automatisées : les deux sources demeurent honnêtement marquées non lues.

4. **`chapitre-18-execution-durable-transactions.md` [15] — Architecture Nexus (Sandeep Nutakki, 4 remplacements)**  
   L'URL `https://consensus.app/papers/details/22a0c58efa5153b194fcbf5d89fbe04c/` ne retourne pas une erreur `403` mais une redirection `302` vers `/sign-up/` (`HTTP 200`). Une recherche via Crossref retrouve la publication originale en accès libre : Sandeep Nutakki, *Design and Implementation of Agentic AI Pipelines for Enterprise Decision-Making Architecture Patterns for Production Systems*, *IJIRMPS*, vol. 14, n° 2 (27 avril 2026), art. 233041, DOI `10.37082/ijirmps.v14.i2.233041`, PDF `https://www.ijirmps.org/papers/2026/2/233041.pdf` (`HTTP 200`, 10 pages), qui décrit bien l'architecture **Nexus**. Les mentions « erreur 403, original introuvable » sont corrigées tout en consignant que le corps du chapitre n'exploite pas cet article.

5. **`chapitre-20-cadriciels-orchestration.md` [14] — *MetaGPT* (`arXiv 2308.00352`, 1 remplacement)**  
   La ligne 149 indiquait « sans chiffre » à propos de MetaGPT. La lecture du PDF intégral (`HTTP 200`, 29 pages) confirme que l'article rapporte des taux `Pass@1` de `85,9 %` sur HumanEval et de `87,7 %` sur MBPP dans ses bancs d'essai de génération de code. Le texte est mis à jour en L149.

6. **`chapitre-20-cadriciels-orchestration.md` [20] — `arXiv 2604.08906v1` vs `v4` (1 remplacement)**  
   L'URL pointe sur la `v1` (10 avril 2026), dont le titre cité (*Dissecting Bug Triggers and Failure Modes...*) est exact. La `v4` (4 octobre 2026) a été renommée *Understanding Bugs in Modern Agentic Frameworks: A Study of Symptoms, Root Causes, and Triggering Conditions* tout en conservant le jeu de 409 bogues. Précision ajoutée en [20].

7. **`chapitre-22-humain-dans-la-boucle.md` [16] — Goddard et coll. (`JAMIA`, 3 remplacements)**  
   `PMC3240751` (`HTTP 200`) confirmé via Crossref DOI `10.1136/amiajnl-2011-000089` et NCBI `esummary` : auteurs Kate Goddard, Abdul Roudsari et Jeremy C. Wyatt; publication en ligne le 16 juin 2011, parution en numéro vol. 19, n° 1 (janvier-février 2012), pp. 121-127. La précision est apportée à la fois dans le corps du texte (L138 : « publié en ligne en 2011 (numéro de 2012) »), dans `## Sources` (L255) et dans `## Limites` (L265).

8. **`chapitre-23-architecture-reference.md` [21] — Nabin Debnath, sans URL d'origine (4 remplacements)**  
   Article retrouvé via Crossref DOI `10.29322/IJSRP.15.12.2025.p16803` et PDF en accès libre `https://www.ijsrp.org/research-paper-1225/ijsrp-p16803.pdf` (`HTTP 200`, 6 pages) : *The Enterprise Agentic Mesh: Architectural Convergence of Semantic Control Planes and Autonomous Multi-Agent Governance*, *International Journal of Scientific and Research Publications* (*IJSRP*), vol. 15, n° 12 (décembre 2025), pp. 4-11. La lecture du PDF confirme qu'il s'agit d'une proposition conceptuelle sans implantation ni mesure de déploiement. La source passe du statut secondaire sans lien à la notice complète avec PDF vérifié, tout en conservant la réserve sur l'évaluation par les pairs d'*IJSRP*.

---

## 3. Contradictions de mode de lecture post-`P2-F3` (`REF-2-coherence.json`, 36 remplacements)

Dans le registre existant (`Master/audit/corrections.json`), le lot `P2-F3` (`#808` à `#819`) a ajouté en tête des sections `## Limites de ce chapitre` une mention indiquant que certaines sources d'abord connues par leur résumé ont été relues au-delà du résumé par extraits le 14 novembre 2026. Cependant, les mentions antérieures « résumé seulement », « d'après le résumé » ou « ne sont connus ici que par leur résumé » étaient restées inchangées dans l'État de référence, `## Sources`, la prose ou la suite des `## Limites`.

`REF-2-coherence.json` harmonise ces mentions sur les 11 chapitres concernés (36 remplacements; le chapitre 21 était déjà aligné) :
- `chapitre-12` (5) : L39, L250 et L252 (suppression de « D'après le résumé » / « Le résumé rapporte » pour `[10]`, tout en conservant L254 sur les 600 exécutions simulées lues au ch. 21), `[10][11]`, L366 (`#808`)
- `chapitre-13` (3) : `[3]`, `[12]`, `[14]` (`#809`)
- `chapitre-14` (3) : L5, en-tête `## Sources` L239 (`sources [1] à [28]` hors de la parenthèse `articles d'arXiv`), L287 (`#810`)
- `chapitre-15` (1) : intertitre L238 (`[6]` à `[8]`, `#811`)
- `chapitre-16` (4) : L5, L135, L137, `[8][9][10]` (`#812`)
- `chapitre-18` (2) : `[13]`, intertitre L296 (`« Sources non lues ou non exploitées dans la rédaction : »`, `#813`)
- `chapitre-19` (2) : `[12]`, L242 (`#814`)
- `chapitre-20` (7) : L5 (deux segments), L212, `[14]`, `[21]`, L297, L298 (`#815`)
- `chapitre-22` (3) : L144, `[17]`, L265 (`#817`)
- `chapitre-23` (3) : L107 (précision sur `arXiv 2501.10114` `[20]` : retrait de « Le résumé de l'article » et indication que « maillage » n'est pas employé au sens d'une architecture d'agents dans l'article complet, où les trois occurrences de `mesh` désignent uniquement `Dharmesh`), `[20]`, L342 (`#818`)
- `chapitre-24` (3) : L5, `[16]`, L288 (`#819`)

---

## 4. Redirections et liens documentés sans anomalie

- **Redirections documentaires validées (`29` entrées `valide_apres_redirection`)** : Anthropic `/engineering/...` -> `/research/...`, LangGraph `/memory` -> `/concepts/memory`, CrewAI -> `/v1.15.41/`, Restate, Confluence `FLIP-531`, Databricks, UiPath, MCP `security_best_practices.md` : contenu cible vérifié conforme (`HTTP 200`).
- **Redirection LangGraph `durable-execution` -> `persistence`** (`ch18 [5]` et `ch20 [3]`) : déjà explicitement signalée dans les chapitres (`« l'adresse sert la page sur la persistance »`).
- **Lien mort documenté** (`ch23 [13]`, Gravitee `HTTP 404`) : déjà consigné `« page introuvable au 13 novembre 2026 (erreur 404) »` dans le manuscrit (`#315`).
- **Namespaces et méta-schéma en blocs de code** (`ch16` OMG BPMN `404`, Camunda Zeebe `404`, W3C `XMLSchema-instance` `403`; `ch17` JSON Schema `2020-12` `200`) : identifiants standard conformes en bloc de code.

---

## 5. Sources à accès restreint ou non joignables (état du 14 novembre 2026)

| Chapitre / Source | URL | Statut observé (14 nov. 2026) | Méthode de recoupement et traitement |
|---|---|---|---|
| Ch. 12 [7] Snowflake OSI | `https://www.snowflake.com/en/blog/open-semantic-interchanges-specs-finalized/` | HTTP `403` (Cloudflare) | Confirmée par `search_web` (billet du 27 janv. 2026); déjà recoupée avec [12]/[13]. |
| Ch. 14 [18][19][20][32] OWASP GenAI | `https://genai.owasp.org/...` (4 URL) | HTTP `403` (Cloudflare) | Confirmées par `search_web` (9 déc. 2025, 13 mai 2026 ASI06, Q3 2026); `[32]` déjà marquée PDF non lu. |
| Ch. 16 [11] Zenodo `19774440` | `https://zenodo.org/records/19774440` | HTTP `200` (défi JS anti-robot) | Métadonnées vérifiées via API REST Zenodo (`HTTP 200` : Yiwen Zhu, Frank Toffoletto). |
| Ch. 16 [12] et Ch. 20 [15] Preprints.org / MDPI | `https://www.preprints.org/manuscript/202604.2147` | HTTP `403` (Preprints & MDPI) | Parution vérifiée via Crossref API (`DOI 10.3390/fi18060326`, *Future Internet*, 15 juin 2026); `REF-2-factuel`. |
| Ch. 19 [14] SD Times | `https://sdtimes.com/how-to-build-a-multi-agent-orchestrator-using-flink-and-kafka/` | HTTP `403` | Article de S. Falconer (fév. 2025) confirmé par `search_web`; signalé comme billet fournisseur. |
| Ch. 19 [15] ACM FSE (DOI cité dans le texte) | `https://doi.org/10.1145/3803437.3805231` | HTTP `403` sur `dl.acm.org` (billet Alibaba Cloud `200`) | Vérifiée par Crossref API (`HTTP 200` : Li Zhou et coll., ACM FSE 2026); déjà marquée « article d'origine non lu ». |
| Ch. 22 [13] SCT Canada (portée DAIA) | `https://www.canada.ca/.../guide-scope-directive-automated-decision-making.html` | `TimeoutError` (12 s) | Existence du guide fédéral confirmée par `search_web`; non-chargement déjà consigné en L263. |
| Ch. 23 [12] McKinsey QuantumBlack | `https://www.mckinsey.com/.../seizing-the-agentic-ai-advantage` | `TimeoutError` (12 s) | Rapport de juin 2025 confirmé par `search_web`; déjà marqué « page non chargée » en L316 et L342. |

---

## 6. Validation `--essai`

```text
python Master/compendium-master-lot.py Master/lots/REF-2-factuel.json --essai
-> lot REF-2-factuel : 21 remplacements à faire, 0 déjà en place, registre à 1332 entrées (essai, rien d'écrit)

python Master/compendium-master-lot.py Master/lots/REF-2-coherence.json --essai
-> lot REF-2-coherence : 36 remplacements à faire, 0 déjà en place, registre à 1347 entrées (essai, rien d'écrit)
```
