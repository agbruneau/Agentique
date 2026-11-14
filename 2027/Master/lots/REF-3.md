# Compte rendu d'audit — Tranche 3 (Lot REF-3)

**Date de l'audit :** 14 novembre 2026  
**Périmètre :** `Master/manuscrit/chapitre-25-integration-patrimoine.md` à `chapitre-37-souverainete.md` (`13` fichiers)  
**Livrables produits :**
- `Master/recherche/audit-ref-3.json` (`712` entrées couvrant 100 % des sources, URL, appels `[n]` et renvois internes)
- `Master/lots/REF-3-renvoi.json` (`4` remplacements, catégorie `renvoi`)
- `Master/lots/REF-3-coherence.json` (`30` remplacements, catégorie `coherence`)
- `Master/lots/REF-3.md` (le présent rapport)

---

## 1. Statistiques de vérification

| Élément vérifié | Volume | Résultat |
|---|---:|---|
| Chapitres audités | 13 | 100 % couverts (`ch. 25` à `ch. 37`) |
| Entrées `## Sources` | 186 | Numérotation continue `1..N` dans chaque chapitre (`181` URL distinctes) |
| Appels `[n]` (hors code et hors volets) | 695 | `0` source non citée, `0` appel orphelin, `0` appel `[n]` dans les volets |
| URL dans les blocs de code des volets | 16 | `13` URL fictives `*.boreal.ca` conservées; `3` URI standards/espaces de noms vérifiées |
| Renvois internes (`chapitre`, `section`, `extrait`, `ADR`, `figures/*.svg`) | 497 | `497/497` cibles locales valides (`313` chapitres, `132` sections, `30` extraits, `12` SVG, `10` ADR) |
| Vérifications arXiv (API + HTML) | 23 | Titre, premier auteur et date conformes à 100 % |
| Vérifications PDF (`PyMuPDF`) | 9 | Tous lisibles (dont Capco `ch. 25 [2]`, `4` pages, revenu en HTTP 200) |
| Vérifications Crossref / DataCite | 2 | DOI `10.5281/zenodo.21279055` (`ch. 37 [10]`) et `10.1016/j.infsof.2026.108307` (`ch. 34 [9]`) |
| Sources HTTP 403 permanents | 10 | Vérifiées sans contournement par `search_web` / API Crossref (+ `1` URI en bloc de code) |
| Redirections automatisées EUR-Lex (`TodayOJ`) | 4 | Ch. 27 `[10]`, Ch. 35 `[2]`, Ch. 36 `[2]`, Ch. 37 `[2]` |

Validation mécanique :
- `python Master/compendium-master-lot.py Master/lots/REF-3-renvoi.json --essai` : **OK** (`4` remplacements à faire, `0` déjà en place, registre à `1315` entrées).
- `python Master/compendium-master-lot.py Master/lots/REF-3-coherence.json --essai` : **OK** (`30` remplacements à faire, `0` déjà en place, registre à `1341` entrées).

---

## 2. Anomalies trouvées et corrections préparées

### 2.1 Redirections canoniques (`Master/lots/REF-3-renvoi.json` — 4 remplacements)

Quatre sources pointaient vers des adresses redirigées de façon permanente :
1. **Ch. 26 `[16]`** : `https://theregister.com/2026/05/05/servicenow_clears_agents_for_landing/` mis à jour vers `https://www.theregister.com/software/2026/05/05/servicenow-adds-agent-kill-switches-to-ai-control-tower/5228579` (HTTP 200 direct).
2. **Ch. 29 `[14]`** : `https://developers.cloudflare.com/bots/concepts/bot/signed-agents/` mis à jour vers `https://developers.cloudflare.com/bots/concepts/bot/verified-bots/` (Cloudflare ayant fusionné les agents signés sous *Verified bots* le 1er juillet 2026). *Note hors tranche :* l'ancienne URL figure encore au chapitre 9 (`[14]`).
3. **Ch. 31 `[4]`** : `https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices.md` mis à jour vers `https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md`, déjà utilisée au chapitre 30 (`[2]`). *Note hors tranche :* l'ancien chemin figure encore au chapitre 24 (`[10]`).
4. **Ch. 35 `[6]`** : `https://www.nist.gov/caisi/ai-agent-standards-initiative` mis à jour vers `https://www.nist.gov/super-intelligence/si-agent-standards-initiative` avec actualisation de l'intitulé (*SI Agent Standards Initiative*, mise à jour NIST du 9 novembre 2026). *Note hors tranche :* l'ancienne URL figure encore aux chapitres 1, 3, 4, 11, 43, 49 et à l'annexe E.

**Conservation intentionnelle :**
- `https://owasp.org/www-project-mcp-top-10/` (`ch. 30 [14]` et `ch. 31 [3]`) reste inchangée pour respecter la décision `#183` (`tranche 06-8`) de `Master/audit/corrections.json`.
- `https://arxiv.org/html/2606.08867v1` (`ch. 33 [12]`) est conservée en `v1` (HTTP 200, KDD 2026), en cohérence avec le chapitre 42 et l'annexe E, même si une `v2` existe sur arXiv.

### 2.2 Incohérences résiduelles et mises à jour factuelles (`Master/lots/REF-3-coherence.json` — 30 remplacements)

1. **Alignement post-`P2-F3` (`ch. 30`, `ch. 31`, `ch. 32`, `ch. 33`, `ch. 34`) :**
   Le lot `P2-F3` (`#779`–`#783`, `#820`–`#826`, `#836`) avait consigné en tête de `## Limites` la relecture au-delà du résumé des articles arXiv et de `ch. 31 [13]` le 14 novembre 2026, mais avait laissé subsister des mentions contraires :
   - **Ch. 30 (`[13]`) :** correction de `État de référence` (`[13] en résumé seulement`) et de la notice `## Sources` l. 229.
   - **Ch. 31 (`[6]`–`[10]`, `[13]`) :** correction de `État de référence` (`les articles par leur résumé seulement`), de quatre passages du corps de texte (`Leur résumé assimile`, `Le résumé ne publie pas de taux` sur AgentDojo `[7]` alors que l'article publie des tableaux de taux, `Le résumé ne donne aucun chiffre` sur Prompt Infection `[9]` et `Selon le résumé` sur `[10]`), des notices `## Sources` (`[6]`–`[10]` et `[13]`), ainsi que des puces l. 300 (`Les cinq articles sont cités d'après leur résumé ... faute de lecture du texte`) et l. 304 (`faute de source lue qui en donne` sur la prévalence et les taux de succès d'attaque, contradictoire avec `#822` et avec les taux publiés par `[7]` et `[9]`, tout en maintenant le constat sur les appuis de `31.7`).
   - **Ch. 32 (`[9]`–`[11]`) :** correction des notices `## Sources` l. 225–227 et de l'ancienne puce l. 239 (`Pour [9], [10] et [11], seuls les résumés ont été lus.`), en conservant la réserve sur l'absence de revue par les pairs.
   - **Ch. 33 (`[13]`, `[14]`, `[16]`) :** mise à jour de `État de référence`, de l'intertitre de `[16]` (`Résumé seulement`), des notices `[13]`–`[14]`, de l'ancienne puce l. 318 et des mentions résiduelles « connue par son résumé » aux lignes 181, 197, 220 et 276.
   - **Ch. 34 (`[3]`) :** correction de `État de référence` et de la notice `## Sources` `[3]`.
2. **Statuts actualisés le 14 novembre 2026 (`ch. 25 [2]`, `ch. 34 [9]`) :**
   - **Ch. 25 l. 207 :** la note du 12 novembre indiquait `[2] n'a pu être relu (page en maintenance, PDF hors délai)`. Le PDF Capco (`4` pages, `© 2025`) répond HTTP 200 le 14 novembre 2026 et confirme le modèle mixte (*blended*) et les quatre questions.
   - **Ch. 34 l. 285 :** remplacement de « une nouvelle recherche, le 14 novembre 2026, ne l'a pas retrouvé » concernant Xia et coll. (`[9]`) par le constat exact : blocage HTTP 403 anti-robot sur SSRN, et confirmation bibliographique sur l'API Crossref via le DOI `10.1016/j.infsof.2026.108307` (*Information and Software Technology*, vol. 200, article 108307, 2026; texte intégral non libre).
3. **Mention explicite des accès restreints dans `## Sources` / `## Limites` :** ajout des constats datés du 14 novembre 2026 dans les chapitres 25, 29, 31, 32, 34, 36 et 37 (voir section 3).

---

## 3. Sources à accès restreint ou non résolvables (audit du 14 novembre 2026)

Aucun contournement anti-robot ou CAPTCHA n'a été tenté. Toutes les entrées ci-dessous ont été vérifiées par recherche web (`search_web`) ou par API officielle :

| Chapitre | Source | URL | Statut observé (14 nov. 2026) | Vérification substitutive & suivi |
|---|---|---|---|---|
| Ch. 25 | `[5]` IBM CICS MCP | `https://www.ibm.com/docs/en/cics-ts/6.x?topic=ai-how-it-works-cics-mcp-server` | HTTP 403 (IBM Notice) | `search_web` : transaction `CWMC`, CMCI JVM server `EYUCMCIJ`, *toolboxes* CICS TS 6.3+; consigné dans `REF-3-coherence` |
| Ch. 25 | `[6]` IBM CICS Agents | `https://www.ibm.com/docs/en/cics-ts/6.x?topic=ai-how-it-works-cics-agents` | HTTP 403 (IBM Notice) | `search_web` : agents *Topology*, *Problem Determination*, lecture seule sur watsonx Assistant for Z; consigné dans `REF-3-coherence` |
| Ch. 26 | `[18]` Gartner | `https://www.gartner.com/doc/8557473` | HTTP 403 (Cloudflare -> `/en/documents/8557473`) | Déjà marqué `— accès refusé.` dans le manuscrit |
| Ch. 27 | `[10]` EUR-Lex Data Act | `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202302854` | HTTP 200 -> `TodayOJ/index.html` (filtrage automatisé) | Déjà signalé dans `## Limites` l. 199 |
| Ch. 29 | `[10]` W3C DID v1.0 | `https://www.w3.org/TR/did-1.0/` | HTTP 403 (Cloudflare) | `search_web` : recommandation W3C du 19 juillet 2022 confirmée; consigné dans `REF-3-coherence` |
| Ch. 29 | `[12]` CSA Agentic Identity | `https://labs.cloudsecurityalliance.org/research/csa-slack-20260916-225950-csa-styled/` | HTTP 403 (défi JS CSA) | `search_web` : note du 16 septembre 2026 confirmée; consigné dans `REF-3-coherence` |
| Ch. 29 | `[15]` W3C DID v1.1 | `https://www.w3.org/TR/did-1.1/` | HTTP 403 (Cloudflare) | `search_web` : *Candidate Recommendation Snapshot* du 5 mars 2026 confirmé; consigné dans `REF-3-coherence` |
| Ch. 30 | Bloc code l. 374 | `https://www.w3.org/ns/credentials/v2` | HTTP 403 (Cloudflare) | URI canonique JSON-LD W3C VC v2.0 dans un bloc de code du volet (conservée intacte) |
| Ch. 30 | Bloc code l. 375 | `https://schemas.agntcy.org/credentials/agent-mandate/v1` | Non résolu (espace de noms) | URI d'espace de noms JSON-LD AGNTCY dans un bloc de code du volet (conservée intacte) |
| Ch. 31 | `[13]` OWASP Q3 2026 | `https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026/` | HTTP 200 initial, puis HTTP 403 WAF intermittent | `search_web` : titre exact et date du 8 octobre 2026 confirmés; consigné dans `REF-3-coherence` |
| Ch. 32 | `[7]` W3C Agent Conformance | `https://www.w3.org/community/agent-conformance/` | HTTP 403 (Cloudflare) | `search_web` : charte et livrables (lancement 30 août 2026) confirmés; consigné dans `REF-3-coherence` |
| Ch. 32 | Bloc code l. 549 | `https://schemas.openid.net/secevent/caep/` | Non résolu (espace de noms) | URI canonique d'événement OpenID Shared Signals / CAEP dans le volet (conservée intacte) |
| Ch. 34 | `[9]` Xia et coll. (SSRN) | `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5534588` | HTTP 403 (Cloudflare) | API Crossref `10.1016/j.infsof.2026.108307` + `search_web` : titre, 6 auteurs et *IST* vol. 200 confirmés; consigné dans `REF-3-coherence` |
| Ch. 35 | `[2]` EUR-Lex 2026/1744 | `https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` | HTTP 200 -> `TodayOJ/index.html` (filtrage automatisé) | Déjà signalé dans `## Limites` l. 290; corroboré via AI Act Explorer `[3]` |
| Ch. 36 | `[2]` EUR-Lex 2024/2853 | `https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=OJ:L_202402853` | HTTP 200 -> `TodayOJ/index.html` (filtrage automatisé) | Déjà signalé dans `## Limites` l. 221 |
| Ch. 36 | `[6]` CSA Liability Note | `https://labs.cloudsecurityalliance.org/research/csa-research-note-agentic-ai-liability-legal-risk-20260703-c/` | HTTP 403 (défi JS CSA) | `search_web` : *AI Liability Inflection: Enterprise Accountability in the Agentic Era* (été 2026); consigné dans `REF-3-coherence` |
| Ch. 36 | `[14]` *Moffatt* (CanLII) | `https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html` | HTTP 403 (DataDome) | Déjà marqué `— accès refusé.` à la l. 214; rappelé dans `REF-3-coherence` |
| Ch. 37 | `[2]` EUR-Lex Data Act | `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202302854` | HTTP 200 -> `TodayOJ/index.html` (filtrage automatisé) | Précision explicite ajoutée dans `## Limites` par `REF-3-coherence` |
