# Audit indépendant de viabilité et de fiabilité des références — Compendium (`REV-02`)

**Auditeur :** `audit-references` (`REV-02`, mode audit uniquement — aucune modification du manuscrit ni des registres)
**Date d'audit :** `25 novembre 2026` (gel documentaire du Compendium : `2 décembre 2026`)
**Protocole vérifié :** `MLR-PRISMA-SCR-COMPENDIUM-2027-V1.0` (`AO-01` strict, `0,0 % METADATA_ONLY`, seuil `AACODS ≥ 9,0/12`)
**Régime de qualité :** Production (vérification exhaustive automatisée + sondage réseau réel `1` requête/URL sans contournement + contrôle factuel ciblé sur textes intégraux `corpus_l_plus/*.txt`)

---

## 1. Synthèse exécutive et indicateurs clés

**Verdict global : SOCLE PROBATOIRE INTÈGRE SUR LE FOND (`0` BLOQUANT), MAIS `6` ÉCARTS MAJEURS DE SYNCHRONISATION DES REGISTRES, DE DÉPENDANCE À UN AGRÉGATEUR TIERS ET DE REPRODUCTIBILITÉ RÉSEAU À CORRIGER.**

L'intégralité des `135` fichiers textes intégraux `L+` archivés dans `recherche/corpus_l_plus/` correspond au bit près aux empreintes `SHA-256` déclarées (`135/135` en LF pur, `0` fichier manquant, `0` orphelin, `0` doublon, `57/57` spécifications vérifiées dans `registre/specifications-lplus.json`). Aucune page d'erreur (`404`/`403`), aucun défi WAF/CAPTCHA/Cloudflare/Anubis, aucune bannière de témoins vide ni aucun fichier `METADATA_ONLY` ne s'est glissé dans `corpus_l_plus/`. Dans les `37` unités narratives (`00 - Liminaire` + `CH-01`..`CH-36`), **100 % des citations `[k]`** pointent vers une entrée valide de `sources/chXX-sources.md` (`0` citation pendante, `0` entrée non citée, `0` URL `statut F` glissée en preuve `L+`), et **0 lien mort (`404`/`410`/DNS/TLS)** n'a été relevé sur les `135` URLs `L+` sondées en direct.

Toutefois, l'audit relève **`12` constats (`0` BLOQUANT, `6` MAJEURS, `6` MINEURS)**, dominés par :
1. une désynchronisation complète du champ `"chapters"` dans `manifeste-sources-sha256.json` sur les `37` unités (`REF-001`) ;
2. des identifiants `SRC-NNN` obsolètes hérités d'une ancienne numérotation dans `registre/faits-empiriques.json` et `recherche/registre-statut-f.json`, assortis d'une erreur de recopie de TCAC (`30,38 %` au lieu de `42,38 %`) (`REF-002`) ;
3. une surdépendance citationnelle envers l'agrégateur tiers `SRC-071` (`AIBanks.ca`, AACODS plancher `9,0/12`, `53` citations dont `21` sans réserve en ligne) (`REF-003`) ;
4. `9` URLs `L+` bloquées ou filtrées lors d'un sondage direct automatisé (`HTTP 403` sur `SRC-102` et `6` dépôts SEC EDGAR sous UA générique ; défi Proof-of-Work `Anubis` sur `2` dépôts HAL `SRC-091` et `SRC-113`) (`REF-004`) ;
5. une citation arXiv non indexée (`arXiv:2505.02279` en `ch31:L92`) (`REF-005`) et un glissement d'attribution sur la borne haute `78 %` dans `FACT-SLM-AGENTIC` (`REF-006`).

### Tableau de bord chiffré

| Indicateur | Valeur vérifiée | Cible / Référence | Statut |
| --- | ---: | ---: | --- |
| Sources `L+` archivées (`manifeste-sources-sha256.json`) | `135` | `135` | Conforme |
| Sources exclues en `statut F` (`registre-statut-f.json`) | `27` | `27` | Conforme |
| URLs distinctes dans `sources/ch00..ch36-sources.md` | `151` (`135` L+ + `16` F) | `151` | Conforme |
| URLs distinctes totales (`manifeste` + `sources` + `statut F`) | `162` (`135` L+ + `27` F) | — | Conforme (`0` chevauchement) |
| Empreintes `SHA-256` vérifiées (LF exact, octets et mots exacts) | `135 / 135` (`100 %`) | `135 / 135` | Conforme |
| Spécifications `specifications-lplus.json` alignées `SHA-256` | `57 / 57` (`100 %`) | `57 / 57` | Conforme |
| Sondage réseau `L+` (`135` URLs, `1` req./URL, timeout `10 s`) — `200 OK` direct | `118` (`87,4 %`) | — | Viable |
| Sondage réseau `L+` — Redirection `3xx -> 200 OK` | `8` (`5,9 %`) | — | À normaliser (`REF-009`) |
| Sondage réseau `L+` — Bloqué / `403` / WAF `Anubis` | `9` (`6,7 %`) | `0` idéal | Fragile (`REF-004`) |
| Sondage réseau `L+` — Lien mort (`404`/`410`) ou erreur DNS/TLS/timeout | `0` (`0,0 %`) | `0` | Conforme |
| Pages d'erreur / WAF / CAPTCHA / `METADATA_ONLY` déguisées en `L+` | `0 / 135` | `0` | Conforme |
| Fichiers `.txt` `L+` à anomalie qualitative ou structurelle (`<300` mots, HTML/MDX `>10 %`, vitrines commerciales) | `6 / 135` | `0` | À surveiller (`REF-007`, `REF-010`, `REF-011`) |
| Citations `[k]` pendantes ou entrées `sources/chXX` inutilisées (`37` unités) | `0` / `0` | `0` / `0` | Conforme |
| Anomalies de traçabilité citationnelle / registres (`manuscrit` + `registre` + `recherche`) | `6` | `0` | À corriger (`REF-001`, `REF-002`, `REF-005`, `REF-006`) |
| Constats totaux (`BLOQUANT` / `MAJEUR` / `MINEUR`) | `12` (`0` / `6` / `6`) | — | — |

---

## 2. Viabilité réseau réelle des URLs (`AO-01` strict)

**Méthode :** Extraction exhaustive des URLs distinctes de `manifeste-sources-sha256.json` (`135`), de `sources/ch00..ch36-sources.md` (`151` = les mêmes `135` URLs `L+` + `16` URLs listées dans les sections `## Exclusions en statut F`) et de `registre-statut-f.json` (`27`, sur-ensemble strict des `16` exclusions). Conformément à `AO-01` et aux règles anti-contournement, **strictement `1` requête HTTP `GET` légère** (lecture limitée aux en-têtes et aux premiers `8 Ko`, `User-Agent` standard, timeout `10 s`, aucun nouvel essai, regroupement séquentiel par hôte avec pause de `0,35 s`) a été émise pour chacune des **`135` URLs `L+` actives**. Les `27` URLs déjà classées `statut F` (WAF/403/401/404/500/CAPTCHA consignés les `22–23 novembre 2026`) n'ont pas été re-sondées.

### 2.1 Répartition globale des `135` URLs `L+` sondées

| Catégorie réseau | Nombre | Part | Détail |
| --- | ---: | ---: | --- |
| `200 OK` direct | `118` | `87,4 %` | Accessibles immédiatement sans redirection ni blocage |
| `3xx -> 200 OK` (redirection) | `8` | `5,9 %` | Même ressource cible ; `1` lien `http://` non chiffré (`SRC-066`), `1` chemin déplacé (`SRC-034`), `3` contrôles témoins Springer Nature (`SRC-073`, `SRC-109`, `SRC-112`) |
| `403 / 429 / WAF Anubis` (accès restreint) | `9` | `6,7 %` | `6` SEC EDGAR `HTTP 403` (politique Fair Access UA), `2` HAL `HTTP 200` avec défi PoW `Anubis`, `1` Grand View Research `HTTP 403` |
| `404 / 410` (lien mort) | `0` | `0,0 %` | Aucun lien mort détecté |
| `Timeout / DNS / TLS` (injoignable) | `0` | `0,0 %` | Aucune défaillance réseau ou TLS |
| **Total sondé (`L+`)** | **`135`** | **`100,0 %`** | **+ `27` URLs `statut F` hors preuve (non re-sondées, `0` fuite en `L+`)** |

### 2.2 Détail des `17` URLs `L+` non `200 OK` direct

| Source | Classement | Code / Défi | URL déclarée | URL finale / Observation | Impact |
| --- | --- | --- | --- | --- | --- |
| `SRC-023` | `3xx -> 200` | `302 -> 200` | `github.com/.../FOCUS_spec-v1_4.pdf` | `release-assets.githubusercontent.com/...` | Normal (CDN GitHub Releases) |
| `SRC-034` | `3xx -> 200` | `301 -> 200` | `docs.temporal.io/encyclopedia/temporal-sdks` | `docs.temporal.io/encyclopedia/architecture/temporal-sdks` | Chemin déplacé ; mettre à jour l'URL canonique (`REF-009`) |
| `SRC-066` | `3xx -> 200` | `301 -> 200` | `http://www.osfi-bsif.gc.ca/...` | `https://www.osfi-bsif.gc.ca/...` | Seule URL `http://` en clair du corpus ; passer en `https://` (`REF-009`) |
| `SRC-071` | `3xx -> 200` | `301 -> 200` | `https://www.aibanks.ca/` | `https://aibanks.ca/` | Redirection canonique apex |
| `SRC-073` | `3xx -> 200` | `302 -> 200` | `nature.com/articles/s41598-026-65730-y` | `...?error=cookies_not_supported&code=...` | Contrôle de témoin Springer Nature sans état (article servi en `200`) |
| `SRC-079` | `3xx -> 200` | `301 -> 200` | `gleif.org/organizational-identity/...` | `gleif.org/en/organizational-identity/...` | Redirection locale `/en/` |
| `SRC-109` | `3xx -> 200` | `302 -> 200` | `link.springer.com/article/10.1007/s10791-026-10509-y` | `...?error=cookies_not_supported&code=...` | Contrôle de témoin Springer Nature sans état (article servi en `200`) |
| `SRC-112` | `3xx -> 200` | `302 -> 200` | `link.springer.com/chapter/10.1007/978-3-030-05252-2_4` | `...?error=cookies_not_supported&code=...` | Contrôle de témoin Springer Nature sans état (chapitre servi en `200`) |
| `SRC-091` | `WAF Anubis` | `200` PoW | `inria.hal.science/hal-02526355v1/document` | Défi Proof-of-Work `Anubis` | `.txt` archivé authentique (`6 801` mots), mais re-téléchargement direct bloqué par `Anubis` (`AO-01`, `REF-004`) |
| `SRC-113` | `WAF Anubis` | `200` PoW | `hal.science/hal-05789314/document` | Défi Proof-of-Work `Anubis` | `.txt` archivé authentique (`8 640` mots), mais re-téléchargement direct bloqué par `Anubis` (`AO-01`, `REF-004`) |
| `SRC-102` | `HTTP 403` | `403` | `grandviewresearch.com/industry-analysis/enterprise-agentic-ai-market-report` | `HTTP 403 Forbidden` | Blocage anti-bot sur vitrine commerciale ; fragilité double (`REF-004`, `REF-007`) |
| `SRC-103` | `HTTP 403` | `403` | `sec.gov/Archives/edgar/data/1652044/.../googexhibit991q32026.htm` | `HTTP 403 Forbidden` | SEC EDGAR Fair Access Policy (exige un `User-Agent` déclaré organisation+courriel) ; `.txt` vérifié authentique (`REF-004`) |
| `SRC-104` | `HTTP 403` | `403` | `sec.gov/Archives/edgar/data/1018724/.../amzn-20260930xex991.htm` | `HTTP 403 Forbidden` | Idem SEC EDGAR Fair Access (`REF-004`) |
| `SRC-105` | `HTTP 403` | `403` | `sec.gov/Archives/edgar/data/1326801/.../meta-09302026xexhibit991.htm` | `HTTP 403 Forbidden` | Idem SEC EDGAR Fair Access (`REF-004`) |
| `SRC-106` | `HTTP 403` | `403` | `sec.gov/Archives/edgar/data/789019/.../msft-20260930.htm` | `HTTP 403 Forbidden` | Idem SEC EDGAR Fair Access (`REF-004`) |
| `SRC-107` | `HTTP 403` | `403` | `sec.gov/Archives/edgar/data/789019/.../msft-20260630.htm` | `HTTP 403 Forbidden` | Idem SEC EDGAR Fair Access (`REF-004`) |
| `SRC-108` | `HTTP 403` | `403` | `sec.gov/Archives/edgar/data/789019/.../msft-20251231.htm` | `HTTP 403 Forbidden` | Idem SEC EDGAR Fair Access (`REF-004`) |

**Cohérence inter-fichiers des URLs :** `0` divergence d'URL entre `manifeste-sources-sha256.json` et `sources/ch00..ch36-sources.md` (`L+`) ; `0` URL de `registre-statut-f.json` glissée dans `sources/` (section `L+`) ou `manuscrit/` comme preuve `L+`. Les `27` URLs `statut F` apparaissent uniquement dans `registre-statut-f.json`, dans les blocs explicites `## Exclusions en statut F` (`16` URLs) et dans la table d'exclusions d'`Annexe A` (`27` URLs).

---

## 3. Intégrité cryptographique et qualité réelle des `135` fichiers `.txt` `L+`

### 3.1 Intégrité cryptographique (`SHA-256`)

- **Corpus disque vs manifeste :** `135/135` fichiers présents dans `recherche/corpus_l_plus/`, `0` manquant, `0` orphelin, `0` fin de ligne `CRLF` (`100 %` LF pur).
- **Empreintes et volumétrie :** `135/135` correspondances exactes `SHA-256` (brut et LF), `135/135` correspondances exactes `byte_length`, `135/135` correspondances exactes `word_count`, `0` empreinte dupliquée.
- **Registre `specifications-lplus.json` :** `57/57` entrées pointent vers un `source_l_plus_id` existant avec `SHA-256` strictement identique au manifeste et au disque.
- **Fiches `sources/ch00..ch36-sources.md` :** `0` écart de `SHA-256`, d'octets, de mots, d'URL, de date ou de score `AACODS` par rapport au manifeste.

### 3.2 Authenticité et qualité textuelle des `135` `.txt`

Une inspection automatisée puis ciblée des `135` `.txt` confirme **zéro faux positif probatoire** :
- **0 page d'erreur / blocage / paywall / CAPTCHA / `METADATA_ONLY`** déguisée en `L+`. (La seule détection lexicale `403` en tête de document — `SRC-074` — correspond à l'exigence normative authentique de la spécification MCP Streamable HTTP : `servers MUST respond with HTTP 403 Forbidden`.)
- Les deux fichiers HAL bloqués par `Anubis` en direct (`SRC-091` et `SRC-113`) contiennent bien sur disque le texte intégral PDF extrait de HAL (`6 801` et `8 640` mots, en-têtes `HAL Id: hal-02526355` et `hal-05789314`).
- Les `6` dépôts SEC EDGAR (`SRC-103..108`) contiennent bien les états financiers et communiqués officiels complets (chiffres CapEx 9 mois 2026 vérifiés directement dans le texte : Alphabet `131 953 M$`, Amazon `175 670 M$`, Meta `83 055 M$`, Microsoft `39 367 M$` T1 FY27 et `49 27x M$` S1 FY26).

**`6` fichiers `.txt` présentent néanmoins des fragilités qualitatives ou structurelles documentées :**

| Source | Mots | Type d'anomalie | Constat détaillé | Constat lié |
| --- | ---: | --- | --- | --- |
| `SRC-069` | `295` | Seul fichier `< 300` mots | Communiqué officiel DG CNECT (Commission européenne, `21 oct. 2026`) sur `EN 18286:2026`. Authentique mais très bref ; sa force probante dépend de la Décision officielle `SRC-067` (`786` mots). | `REF-011` |
| `SRC-038` | `62 231` | Bruit HTML/MDX (`35,3 %`) | `7 579` balises HTML/JSX issues de la concaténation brute des fichiers `.mdx` de MCP `2025-11-25`. Contenu authentique et exploitable, mais bruit de balisage élevé. | `REF-010` |
| `SRC-089` | `3 715` | Bruit HTML (`11,5 %`) | `176` ancres `<a id=...>` et badges shields.io dans `gen-ai.md` (OTel `v1.41.0`, fichier autogénéré). | `REF-010` |
| `SRC-090` | `6 234` | Bruit HTML (`10,1 %`) | `205` ancres `<a id=...>` et badges shields.io dans `gen-ai.md` (`semantic-conventions-genai@244465e9`). | `REF-010` |
| `SRC-101` | `6 584` | Vitrine commerciale publique | Synthèse web ouverte d'un rapport payant (Mordor Intelligence, `AACODS 9,0/12`, méthodologie propriétaire non vérifiable). | `REF-007` |
| `SRC-102` | `2 917` | Vitrine commerciale + `403` live | Synthèse web ouverte d'un rapport payant (Grand View Research, `AACODS 9,0/12`, blocage `HTTP 403` en direct). | `REF-004`, `REF-007` |

*(Artefacts d'extraction mineurs également notés sans altération du sens dans `SRC-024` — balises `<i>`, `<img SRC=...>` et repères `Add marginal notes below` — ainsi que `SRC-070` — en-tête `MAIN CONT DIV START`.)*

---

## 4. Évaluation de la fiabilité, de l'autorité (`AACODS`) et de la chronologie

### 4.1 Profil d'autorité du corpus `L+` (`135` sources)

- **Distribution des catégories :** `33` prépublications (`preprint`, `24,4 %`), `26` spécifications ouvertes (`standard_spec`, `19,3 %`), `22` normes IETF (`standard_rfc`, `16,3 %`), `7` lois/règlements (`legislation`), `6` dépôts réglementaires SEC (`regulatory_filing`), `5` brouillons IETF (`standard_draft`), `5` normes NIST/FIPS (`standard_gov`), `4` rapports officiels (`official_report`), `4` articles de revue (`journal_article`), `4` lignes directrices prudentielles (`regulatory_guideline`), `3` articles de conférence (`conference_paper`), `3` rapports d'industrie (`industry_report`), `2` statistiques officielles StatCan (`official_statistics`), `2` manuels de référence NIST (`standard_reference`), `2` référentiels OWASP (`industry_standard`), `2` documents de travail NBER (`working_paper`), et `5` catégories unitaires (`report`, `technical_spec`, `third_party_aggregator`, `regulatory_notice`, `book_chapter`).
- **Chronologie vs gel du `2 décembre 2026` :** **0 source postérieure au `2026-12-02`** (ni même postérieure au `2026-11-25`). Les dates d'entrée en vigueur futures (`2027`–`2035`) sont encadrées en horizon prospectif ou programmé.
- **Distribution `AACODS` :** toutes les sources respectent le seuil minimal `≥ 9,0/12` (`9,0` : 3 ; `9,5` : 3 ; `10,0` : 4 ; `10,5` : 26 ; `11,0` : 29 ; `11,5` : 50 ; `12,0` : 20).
- **Incohérence de métadonnées `peer_reviewed` (`REF-008`) :** Le booléen `peer_reviewed` (`24` `true`, `111` `false`) est appliqué de façon hétérogène dans des catégories identiques : `11` RFC sont marquées `true` (`SRC-004`, `005`, `009`, `010`, `012`...) et `11` autres RFC `false` (`SRC-125..129`...) ; `1` texte législatif `true` (`SRC-067`) contre `6` `false` (`SRC-060..063`, `070`...) ; `1` norme FIPS `true` (`SRC-018`) contre `4` `false` (`SRC-049..051`, `054`) ; `1` manuel NIST `true` (`SRC-022`) contre `1` `false` (`SRC-024`).

### 4.2 Sources à autorité fragile (`AACODS < 10,0/12` — `6` sources)

| Source | Score | Catégorie | Citations manuscrit | Appréciation de fiabilité |
| --- | ---: | --- | ---: | --- |
| `SRC-071` | `9,0` | `third_party_aggregator` (`AIBanks.ca`) | **`53`** (`7` chapitres) | **Risque majeur (`REF-003`)** : site indépendant (« Mitey, data editor ») devenu la 7e source la plus citée du Compendium. Si le traité signale souvent le `statut F` de l'AMF (`lautorite.qc.ca`), `21` occurrences citent `SRC-071` sans réserve en ligne et `ch25` (`L84`, `L98`) l'emploie même pour le projet de règlement fédéral LSAC du `27 juin 2026` au lieu de la Gazette du Canada. |
| `SRC-101` | `9,0` | `industry_report` (Mordor Intelligence) | `5` (`ch03`) | Vitrine commerciale publique à méthodologie propriétaire fermée (`REF-007`). Usage circonscrit et assorti d'une mise en garde explicite en `ch03`. |
| `SRC-102` | `9,0` | `industry_report` (Grand View Research) | `2` (`ch03`) | Vitrine commerciale publique à méthodologie fermée et désormais `HTTP 403` en direct (`REF-004`, `REF-007`). |
| `SRC-011` | `9,5` | `industry_report` (Deloitte TMT 2026) | `14` | Source secondaire de cabinet réputé, utilisée proprement avec mention explicite du `statut F` du communiqué primaire Gartner (`> 40 %`). |
| `SRC-017` | `9,5` | `standard_draft` (IETF indiv. `-01`) | `3` (`ch17`) | Brouillon individuel China Mobile expirant le `3 mai 2027` ; qualifié avec rigueur `(-01 non adopté)` en `ch17:L156`. |
| `SRC-095` | `9,5` | `preprint` (Metere, Enclawed LLC) | `15` (`ch19`, `ch21`) | Prépublication mono-auteur non évaluée par les pairs ; transparence acceptable mais autorité limitée pour `15` citations. |

---

## 5. Traçabilité citationnelle et vérification factuelle (`37` unités + registres)

### 5.1 Maillage `[k]` <-> `sources/chXX-sources.md`

- **Exhaustivité parfaite dans les chapitres :** `0` citation `[k]` hors plage ou pendante sur les `37` unités narratives ; `0` entrée `### [k] SRC-NNN` non citée ; `135/135` sources `L+` effectivement citées dans au moins un chapitre.
- **Cloisonnement `statut F` dans le manuscrit :** Le balayage systématique des mentions de sources exclues (`AMF`, `ISO/IEC 42001`, `OCRI/CIRO`, `Gartner`, `Coase`, `IDC`, `Polaris`, `Leveson/STPA`) confirme que le manuscrit qualifie explicitement leur statut hors preuve (`statut F`, compensé par `SRC-011`, `SRC-058`, `SRC-067`, `SRC-097`, etc.), à la réserve près de la sur-citation sans nuance en ligne de `SRC-071` (`REF-003`).
- **Exception de base fermée (`REF-005`) :** `Chapitre 31` (`L92`, ainsi que `ancrage/ch31-ancrage.md`) cite `Ehtesham et coll. (arXiv:2505.02279)` directement dans le texte sans aucune entrée correspondante dans `ch31-sources.md`, `manifeste-sources-sha256.json`, `corpus_l_plus/` ni `registre-statut-f.json`.
- **Désynchronisation du champ `"chapters"` (`REF-001`) :** Dans `manifeste-sources-sha256.json`, le champ `"chapters"` ne couvre que `00-liminaire`, `ch00`..`ch05`, `ch07` et `ch09`..`ch12`, divergeant de `sources/ch00..ch36-sources.md` sur la totalité des `37` chapitres (`ch06`, `ch08`, `ch13`..`ch36` absents).

### 5.2 Vérification factuelle ciblée (chiffres, dates, versions, identifiants)

Les vérifications croisées directes entre le manuscrit, `registre/faits-empiriques.json`, `registre/ancres-chronologiques.json` (`86` ancres sans écart `SRC`) et les fichiers `.txt` de `corpus_l_plus/` confirment l'exactitude de la très grande majorité des faits empiriques majeurs :
- **Vérifiés exacts sur `.txt` :** `SRC-027` MAP (`68 % ≤ 10 étapes`, `80 %` = `16/20` flux fixe) ; `SRC-028` MAST (`1 642` traces, `7` cadriciels, `14` modes, `41 %` à `86,7 %`) ; `SRC-057` Kraishan (`21 643` serveurs, `72 606` versions, `8 900` multi-versions, `51,09 %`, `40,58 %`, `4,16 %`, `OR = 2,96`) ; `SRC-007`/`SRC-056` CaMeL (`77 %` vs `84 %` ; ASR `12,9 %` -> `0,2 %` -> `0,0 %`) ; `SRC-050`/`SRC-012` ML-DSA (`3 309` et `4 627` octets) ; `SRC-008` Stanford HAI (recul près de `20 %` chez les `22–25` ans) ; `SRC-014`/`SRC-015` StatCan (`19,2 %` global, `40,4 %` finance/assurances) ; `SRC-061` `(UE) 2026/1744` (`2 août 2027` / `2 août 2028`) ; `SRC-065` BSIF E-23 (`1 mai 2027`) ; `SRC-067`/`SRC-069` `EN 18286:2026` / `(UE) 2026/2274` ; `SRC-074` MCP `2026-07-28` (retrait du flux GET et des sessions protocolaires, en-têtes `MCP-Protocol-Version`, `Mcp-Method`, `Mcp-Name`) ; `SRC-044` `RFC 9943` SCITT (mentionne bien `[RFC9942]` pour les reçus COSE, confirmant `ch22:L141`) ; `SRC-090` OTel GenAI (`85` attributs `Development` exacts incluant `cache_write`).
- **Écarts factuels ou de référencement détectés :**
  1. **`registre/faits-empiriques.json` — `FACT-HYPERSCALER-CAPEX-2026` (`REF-002`) :** le champ `"source"` cite encore `SRC-017`..`SRC-022` (qui sont en réalité OAuth Revocation, FIPS 205, SPIFFE, SPIRE, JSON Schema et NIST 7.2.4.1) alors que `"source_l_plus_id"` indique correctement `SRC-103`..`SRC-108` ; de plus, `"owner_chapter"` pointe sur `ch02` au lieu de `ch03`.
  2. **`registre/faits-empiriques.json` — `FACT-MARKET-ENVELOPE-2027-2030` (`REF-002`) :** `"source"` cite `SRC-012` (RFC 9964) et `SRC-013` (RFC 9562) au lieu de `SRC-101` et `SRC-102` ; `"owner_chapter"` pointe sur `ch02` au lieu de `ch03` ; `"commentaire_annexe"` contient la coquille `40,61 (interpolé à 30,38 % CAGR pour Mordor)` alors que `SRC-101` et `ch03:L25` donnent `42,38 %` (`14,06 × 1,4238^3 = 40,58 G$ US`).
  3. **`recherche/registre-statut-f.json` (`REF-002`) :** les notes de compensation renvoient à `SRC-010` (RFC 9334) au lieu de `SRC-100` (Cui et al.) et à `SRC-004` (RFC 7493) au lieu de `SRC-097` (Shahidi et al., NBER w34468).
  4. **`registre/faits-empiriques.json` — `FACT-SLM-AGENTIC` et `Annexe C:L200` (`REF-006`) :** attribuent `70 % à 78 % en routage frugal` à `SRC-123` (Belcak et al.), alors que `SRC-123` estime `40 %` (Open Operator), `60 %` (MetaGPT) et `70 %` (Cradle) ; la borne `78 %` est une cible interne `[S]` (correctement distinguée en `ch03:L139` et `ch09:L130`).
  5. **`SRC-024` titre catalogué (`REF-012`) :** intitulé `Section 8.1.8.1 Series Model (Lusser Reliability Law)` alors que la section NIST s'intitule `8.1.8.1. Competing risk model` sans jamais citer « Lusser » (`ch02:L23` est exact, seul le titre catalogué extrapole). Nuance mineure également sur `SRC-089` (`60` attributs = `50` `Development` + `10` `Deprecated`).

---

## 6. Table complète des constats (`REF-001` à `REF-012`)

| ID | Sévérité | Unité | Synthèse du constat | Action corrective recommandée |
| --- | --- | --- | --- | --- |
| `REF-001` | **MAJEUR** | `global` | Le champ `"chapters"` de `recherche/manifeste-sources-sha256.json` est désynchronisé sur les `37` unités (ancien découpage `00-liminaire`/`ch01`..`ch12`, omettant `ch06`, `ch08`, `ch13`..`ch36`). | Régénérer le champ `"chapters"` de `manifeste-sources-sha256.json` de manière déterministe à partir des `37` fichiers `sources/ch00..ch36-sources.md` (normalisation `ch00`..`ch36`). |
| `REF-002` | **MAJEUR** | `global` | Identifiants `SRC-NNN` obsolètes et erronés dans `registre/faits-empiriques.json` (`SRC-017..022` -> `SRC-103..108` ; `SRC-012..013` -> `SRC-101..102` ; `owner_chapter: ch02` -> `ch03` ; coquille `30,38 %`/`40,61` -> `42,38 %`/`40,58`) et dans `recherche/registre-statut-f.json` (`SRC-010` -> `SRC-100` pour Cui et al. ; `SRC-004` -> `SRC-097` pour Shahidi et al.). | Corriger les identifiants `SRC-NNN`, les chapitres propriétaires et la formule TCAC (`42,38 %` -> `40,58 G$ US`) dans `registre/faits-empiriques.json` et `recherche/registre-statut-f.json`, puis ajouter un test de cohérence CI vérifiant tout motif `SRC-\d{3}` dans les registres JSON. |
| `REF-003` | **MAJEUR** | `global` | Surdépendance à l'agrégateur tiers `SRC-071` (`AIBanks.ca`, AACODS plancher `9,0/12`, éditeur individuel « Mitey ») : `53` citations dans `7` chapitres (`ch16`, `ch17`, `ch25`, `ch28`, `ch32`, `ch34`, `ch36`), dont `21` sans réserve en ligne, et utilisation en `ch25:L84,L98` pour le projet de règlement fédéral LSAC du `27 juin 2026`. | Sourcer directement le projet de règlement LSAC (`27 juin 2026`) sur la *Gazette du Canada, Partie I* en `L+`, restreindre `SRC-071` exclusivement à la corroboration sous réserve de l'échéance AMF (`1er mai 2027`) et expliciter la réserve `(source secondaire AIBanks.ca, portail AMF en statut F)` sur les occurrences restantes. |
| `REF-004` | **MAJEUR** | `global` | `9` URLs `L+` inaccessibles lors du sondage réseau automatisé `1` req./URL : `SRC-102` (`HTTP 403`), `SRC-091` et `SRC-113` (défi PoW `Anubis` sur HAL, explicitement interdit par `AO-01`), et `SRC-103..108` (`HTTP 403` SEC EDGAR sous UA générique). | Consigner l'en-tête SEC Fair Access Policy dans l'outillage de vérification (`SRC-103..108`), vérifier l'existence d'URLs API ouvertes HAL ou de miroirs sans `Anubis` pour `SRC-091`/`SRC-113` (sinon documenter l'archivage gelé antérieur à `Anubis`), et réévaluer le maintien en `L+` de `SRC-102` (bloqué `403` + vitrine commerciale). |
| `REF-005` | **MAJEUR** | `ch31` | Citation externe non indexée `Ehtesham et coll. (arXiv:2505.02279)` dans `Chapitre 31` (`L92`) et `ancrage/ch31-ancrage.md`, absente de `ch31-sources.md`, de `manifeste-sources-sha256.json` et de `corpus_l_plus/`. | Soit archiver `arXiv:2505.02279` en `L+` (texte intégral + `SHA-256` + entrée `ch31-sources.md`), soit retirer la référence précise si elle n'est pas nécessaire à la démonstration du tri `PROGRAMMÉ`/`PROJETÉ`/`SPÉCULATIF`. |
| `REF-006` | **MAJEUR** | `ch03` | Glissement d'attribution sur `FACT-SLM-AGENTIC` (`registre/faits-empiriques.json` et `Annexe C:L200`) : la cible `70 % à 78 %` est attribuée à `SRC-123` (Belcak et al.), qui ne rapporte que `40 %`–`70 %` (`40 %` Open Operator, `60 %` MetaGPT, `70 %` Cradle). | Aligner `FACT-SLM-AGENTIC` et `Annexe C:L200` sur la distinction déjà respectée en `ch03:L139` et `ch09:L130` : « `40 %` à `70 %` mesurés dans Belcak et al. (`SRC-123`), étendus en cible interne `[S]` `70 %–78 %` ». |
| `REF-007` | **MINEUR** | `ch03` | Inclusion en `L+` des vitrines publiques commerciales `SRC-101` (Mordor Intelligence) et `SRC-102` (Grand View Research), notées au plancher `AACODS 9,0/12`, à méthodologie propriétaire non vérifiable. | Maintenir la mise en garde critique de `ch03` et envisager le déclassement de `SRC-102` (désormais `HTTP 403`) en `statut F` lors de la prochaine révision, ou la conservation uniquement comme illustration de dispersion commerciale hors preuve décisionnelle. |
| `REF-008` | **MINEUR** | `global` | Typage incohérent du champ `peer_reviewed` dans `manifeste-sources-sha256.json` au sein de catégories identiques (`standard_rfc` 11/11, `legislation` 1/6, `standard_gov` 1/4, `official_report` 1/3, `standard_reference` 1/1, `standard_spec` 1/25). | Définir une règle uniforme de codage de `peer_reviewed` par catégorie (réservé aux articles de revue/conférence évalués par les pairs, ou distingué par un champ `review_regime` : `academic_peer_review` / `standards_consensus` / `statutory` / `preprint` / `grey`). |
| `REF-009` | **MINEUR** | `global` | `SRC-066` emploie une URL `http://` non chiffrée (`osfi-bsif.gc.ca`), `SRC-034` pointe vers un chemin Temporal déplacé (`.../encyclopedia/temporal-sdks` -> `.../architecture/temporal-sdks`), et `6` autres URLs subissent des redirections `3xx` (dont `3` contrôles témoins Springer Nature). | Normaliser `SRC-066` en `https://`, mettre à jour l'URL canonique de `SRC-034` (`architecture/temporal-sdks`) et de `SRC-079` (`/en/`) dans `manifeste-sources-sha256.json` et les fichiers `sources/chXX-sources.md` correspondants. |
| `REF-010` | **MINEUR** | `global` | Bruit de balisage HTML/MDX supérieur à `10 %` dans `SRC-038` (`35,3 %`, `7 579` balises), `SRC-089` (`11,5 %`) et `SRC-090` (`10,1 %`), plus artefacts HTML résiduels mineurs dans `SRC-024` et `SRC-070`. | Documenter dans le manifeste le format natif source (`mdx`/`md_autogen`/`html_extract`) afin d'éviter toute confusion avec un mauvais grattage, ou nettoyer lors d'une future refonte avec recalcul des empreintes `SHA-256`. |
| `REF-011` | **MINEUR** | `ch26` | `SRC-069` (`295` mots) est l'unique fichier `L+` sous le seuil de `300` mots (communiqué court DG CNECT sur `EN 18286:2026`). | Mentionner explicitement son caractère de communiqué institutionnel complémentaire à la Décision d'exécution `(UE) 2026/2274` (`SRC-067`, `786` mots) qui porte l'autorité juridique. |
| `REF-012` | **MINEUR** | `ch02` | Titre catalogué imprécis pour `SRC-024` (`Section 8.1.8.1 Series Model (Lusser Reliability Law)` alors que le texte NIST s'intitule `8.1.8.1. Competing risk model` sans mention de « Lusser ») ; préciser aussi que `SRC-089` compte `60` attributs au total (`50` `Development` + `10` `Deprecated`) et surveiller l'expiration de `SRC-017` (`3 mai 2027`). | Rectifier le titre catalogué de `SRC-024` en `Section 8.1.8.1 Competing Risk Model (loi multiplicative équivalente à Lusser)` et préciser la ventilation `50 Development + 10 Deprecated` pour `SRC-089` dans `FACT-OTEL-GENAI-ATTRS`. |
