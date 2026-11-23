# Annexe E — Bibliographie et niveaux de preuve

> Cette annexe complète les listes de sources des chapitres : elle dit comment les lire et rappelle les sources d’ancrage.

## E.1 Niveaux de preuve

Chaque chapitre se termine par ses sources numérotées et par une section « Limites de ce chapitre ». Les chapitres 1 à 47 en listent 795 au total (789 au 14 novembre 2026, plus 6 textes primaires ouverts L+ ajoutés au chapitre 38 le 19 novembre 2026) (la partie X est décomptée à la section E.4); une source citée par plusieurs chapitres compte pour chacun.

Trois marques qualifient une affirmation.

| Marque | Sens | Usage |
| --- | --- | --- |
| Primaire | Page de l’émetteur (spécification, texte officiel, article, documentation), lue pour le chapitre | Peut fonder une décision, dans les limites de la page |
| Secondaire | Compte rendu, analyse ou résumé d’un tiers | Signale un fait; à confirmer à la source avant d’agir |
| Non confirmé | Point qu’aucune page lue n’établit | Nommé dans les limites du chapitre; à ne pas reprendre |

La nature de la source compte aussi, de la plus solide à la plus fragile : texte normatif ou officiel; article évalué par les pairs; prépublication; documentation d’un éditeur sur son produit; billet d’éditeur, note d’analyste ou presse. Le chapitre 42 propose un classement voisin, en six niveaux, pour les études de cas.

Cinq réserves valent pour tout l’ouvrage.

- **Lecture par extraction.** La plupart des pages ont été lues et relues par un outil qui en condense le contenu. Un chiffre ou un niveau d’obligation se revérifie sur le texte intégral.
- **Résumés seulement (résorbé en section 48.12).** Dans l’état gelé au 14 novembre 2026, plusieurs articles n’étaient connus que par leur résumé (`103` notices résiduelles documentées). La refonte MLR PRISMA-ScR / Garousi du 19 novembre 2026 (`Borealis-Bench/mlr/protocole-mlr-prisma.json`, section 48.12) élimine cette dépendance sur le corpus scientifique consolidé (`160` études incluses sur texte intégral *Open Access* haché `SHA-256`, `33,75 %` arbitrées, `0,0 %` **sur résumé seul**), et formalise le plan initial des chapitres 1 à 47 dans `Borealis-Bench/mlr/plan-initial-2027.md`.

- **Audit partiel.** L’audit n’a relu qu’une partie des sources; EUR-Lex, McKinsey, Gartner et ServiceNow sont restés inaccessibles. Les limites de chaque chapitre nomment les sources non revérifiées.
- **Documentation d’éditeur.** Elle décrit ce qu’un produit annonce. Aucun essai indépendant n’est cité pour les moteurs d’exécution durable, les passerelles ou l’interopérabilité entre plateformes (chapitres 18, 24 et 26).
- **Date de référence.** Les faits sont arrêtés au 11 novembre 2026 (13 novembre pour la partie X); les relectures de l’audit et les sources des chapitres 44 à 47 datent du 12; des compléments, signalés dans les sources et les limites de vingt chapitres, datent du 14. Brouillons et préversions ont pu changer depuis.

## E.2 Sources d’ancrage

Entre parenthèses : ceux des chapitres 1 à 47 qui citent cette adresse; d’autres en citent une autre version (HTML d’arXiv, PDF, brouillon).

**Protocoles et standards**

- MCP — spécification `2026-07-28`, architecture (5) et feuille de route du 22 août 2026 (5, 13, 19, 27, 29, 30, 43)
- A2A — spécification (3, 6, 8, 19)
- Agentic AI Foundation — projets (1, 3–7, 11, 13, 24, 27, 43, 44)
- AG-UI — introduction et AGNTCY — documentation (7)
- AP2 — spécification v0.2 et x402 — introduction (10)
- Agent Skills — spécification (13, 27)
- NIST — SI Agent Standards Initiative (1, 3, 4, 11, 35, 43)

**Identité et sécurité**

- RFC 8693 — OAuth 2.0 Token Exchange (29, 30) et RFC 9449 — DPoP (29)
- IETF — draft-ietf-wimse-aims (3, 11, 29) et draft-ietf-oauth-identity-assertion-authz-grant (11, 29)
- OWASP — annonce du Top 10 for Agentic Applications (14, 31) et OWASP MCP Top 10 (30, 31)
- OpenTelemetry — conventions sémantiques GenAI, page déplacée vers le dépôt `semantic-conventions-genai` (33, 43)

**Recherche**

- Cemri et coll. — Why Do Multi-Agent LLM Systems Fail?, taxonomie MAST (3, 4, 12, 21)
- Pan et coll. — Measuring Agents in Production, étude MAP (1, 4, 17, 41, 43)
- Kim et coll. — Towards a Science of Scaling Agent Systems (16, 21)
- Kang et Diponegoro — Governance Gaps in Agent Interoperability Protocols (2, 7, 11, 43)
- Nubank — Building Customer Support AI Agents at 100M-User Scale (33, 42)
- Anthropic — Building effective agents (1, 16, 17)

**Cadres et droit**

- Règlement (UE) 2026/1744, Digital Omnibus sur l’IA (35)
- IMDA — Model AI Governance Framework for Agentic AI, version 1.5 (1, 3, 22, 35, 39)
- BSIF — ligne directrice E-23 (38, 39) et sa lettre d’accompagnement (38, 43)

- Canada — lancement de la stratégie « AI for All » (38)
- Québec, MCN — Guide sur l’utilisation responsable de l’IA agentique (22, 38, 39, 42)
- `2026/documents/Note AMF IA.pdf` — Profil québécois `CRE-IA-2026-01-QC` instruisant les 41 attentes de la Ligne directrice de l’AMF sur l’IA et les 12 exigences `EXIG-AMF-01` à `EXIG-AMF-12` (prise d’effet 1er mai 2027; PDF officiel AMF en statut F, HTTP 403 en téléchargement automatisé; SHA-256 `60f32f2017600fca9b52ac99a6e090dc3982313cd83f990a7af383f3b4ddfd7d`) (38, 39, 49)
- Textes primaires ouverts (`statut L+`, 19 novembre 2026) pour la purge juridique du chapitre 38 (§ 38.10) : LCCJTI sanctionnée, L.Q. 2001, c. 32, LUCE / UECA (CHLC/ULCC), Loi sur la concurrence, L.R.C. (1985), ch. C-34, Sherman Act, 15 U.S.C. § 1, TFUE, art. 101 et RFC 8785 (JCS) (38)

## E.3 Points à confirmer en priorité

Ces affirmations des chapitres 1 à 47 portent beaucoup et reposent sur une preuve mince : ce sont les premières à revérifier; celles de la partie X sont à la section E.4.

| Point | État de la preuve | Chapitres |
| --- | --- | --- |
| Texte de l’AI Act modifié par le règlement 2026/1744 | EUR-Lex illisible; lu par une prépublication ou une reproduction non officielle | 34, 35, 43 |
| Directive fédérale sur la prise de décisions automatisée | Page jamais lue (requête rejetée); champ d’application décrit d’après un guide | 22, 38 |
| Ligne directrice de l’AMF sur l’utilisation de l’IA | PDF officiel en statut F (erreur 403 Cloudflare en téléchargement automatisé); raccordée le 19 novembre 2026 à l’instruction interne `2026/documents/Note AMF IA.pdf` (`CRE-IA-2026-01-QC`, 41 attentes, `EXIG-AMF-01` à `EXIG-AMF-12`) en complément des deux analyses de cabinets | 38, 39, 49 |
| Sanctions du projet de loi C-36 | Document d’information; texte relu en partie | 38 |
| Chiffres des enquêtes McKinsey | Comptes rendus; pages de McKinsey non relues à la source | 1, 4, 39, 41 |
| Placement de ServiceNow au Magic Quadrant; ses offres en 2026 | Rapport non lu, reprises contradictoires; presse issue d’un breffage | 4, 26 |
| Usage de MCP et d’A2A en production | Communiqué qui ne nomme aucune organisation; aucun cas documenté | 6, 42 |

Le dernier point pèse sur la thèse de l’ouvrage : l’interopérabilité par protocoles ouverts est bien spécifiée et largement annoncée, mais sa pratique en production reste à documenter.

### Contrôles faits le 14 novembre 2026

Quatre contrôles ont suivi l’audit, faits par des lecteurs qui n’avaient pas écrit les passages contrôlés. Les trois premiers lisent les sources par un outil qui en rend des extraits, non le texte brut; le quatrième contrôle les adresses, identifiants et renvois directement sur les sources et les interfaces d’arXiv, Crossref et IETF Datatracker.

| Contrôle | Périmètre | Résultat |
| --- | --- | --- |
| Recollationnement des chiffres | 200 phrases d’exposé tirées au hasard parmi les 295 qui portent une quantité et un appel de source | 182 vérifiables : 178 confirmées, 4 en erreur, soit 2,2 %; 18 non vérifiables, la source étant inaccessible ou le chiffre introuvable |
| Lecture au-delà du résumé | 134 sources des chapitres 1 à 47 connues par leur seul résumé et citées dans le texte | 124 relues : 64 confirmées, 54 exactes mais à nuancer, 6 en erreur; 10 non relues |
| Second audit des compléments | Les 193 entrées ajoutées au registre le 14 novembre | 95 constats : aucun bloquant, 19 majeurs, 76 mineurs; 86 corrigés |
| Contrôle intégral des références et liens | 59 fichiers du manuscrit : 1 033 sources (789 ch. 1–47, 244 partie X), 1 101 occurrences d’URL publiques (878 distinctes, dont 13 occurrences / 12 URI en blocs de code), appels [n] et renvois internes (5 607 entrées consignées pour les tranches 1 à 5, dont 3 ajouts de DOI) | 0 source sans URL, 0 appel ou renvoi interne cassé; 268 remplacements appliqués au registre (lots REF-1 à REF-5 et REF-cloture à REF-cloture-4); accès restreints (403, 429, défis anti-robot, délais) vérifiés par API ou recherche et datés dans les sources et limites |

Les quatre erreurs de relevé tiennent à la portée du chiffre plus qu’au chiffre : un exemple donné pour une règle, une population plus étroite que celle annoncée, une attribution à la mauvaise page, une source révisée depuis la lecture. Le deuxième contrôle pèse davantage : près d’une fois sur deux, le texte complet ajoute au résumé une réserve qui change la portée du résultat, le plus souvent la taille réelle de l’échantillon, le périmètre de l’essai ou le lien des auteurs avec le produit mesuré. Les corrections sont inscrites au registre, et les limites des chapitres disent quelles sources ont été relues. Les sources de la partie X, lues par leur résumé selon la méthode déclarée au chapitre 48, n’ont pas été relues ainsi.

## E.4 Sources de la partie X

La partie X a été écrite le 13 novembre 2026, après la clôture des chapitres 1 à 47. Ses trois chapitres listent 275 sources (251 au 14 novembre 2026, plus 24 DOI arbitrés sur texte intégral OA ajoutés au chapitre 48 lors de la refonte MLR W3.2 du 19 novembre 2026), qui s’ajoutent aux 795 de la section E.1 sans y être comptées.

| Chapitre | Sources | Nature | Lecture |
| --- | --- | --- | --- |
| 48 — Revue de littérature | 125 | 55 publications évaluées par les pairs (31 historiques + 24 DOI OA ajoutés en section 48.12 sur 54 incluses dans la MLR W3.2), 52 prépublications historiques, 3 reprises, 15 hors protocole (14 nov.); corpus MLR consolidé : 453 notices (67,11 % pairs) → 160 textes intégraux OA (33,75 % pairs, 0,0 % résumés) | Résumés seulement pour les 83 notices du protocole, dont titre, auteurs et lieu de publication sont confirmés auprès d’arXiv ou de Crossref pour 82 le 13 novembre (la 83e, [32], est confirmée sur arXiv et l’auteur de [27] sur la page du DOI le 14 novembre); des quinze travaux hors protocole, six n’étaient connus que par leur résumé; la refonte MLR PRISMA-ScR du 19 novembre 2026 (section 48.12) repose exclusivement sur 160 textes intégraux OA hachés `SHA-256` (`0,0 %` sur résumé seul, κ = 0,7935, `Borealis-Bench/mlr/manifeste-oa-sha256.json`), dont 24 DOI arbitrés clés `[102]`–`[125]` |
| 49 — Veille technologique | 75 | 46 pages d’émetteur, 21 notices d’arXiv, 1 page tierce, 7 reprises des ch. 4, 8, 26, 37 et 38 | Extraction par outil; sept sources relues à l’audit |
| 50 — Projection 2027-2030 et étude de marché | 75 | 51 pages d’émetteur, 24 pages tierces qui rapportent un émetteur non chargé | Extraction par outil; cinq sources relues à l’audit |

Trois réserves s’ajoutent à celles de la section E.1.

- **Transition revue de cadrage → MLR PRISMA-ScR ouverte.** Les sections 48.1 à 48.10 gardent la trace datée de la revue de cadrage du 13 novembre (base *Consensus*, 83 résumés); la section 48.12 (19 novembre 2026, lot `W3.2`) y substitue une MLR PRISMA-ScR / Garousi reproductible (`Borealis-Bench/mlr/protocole-mlr-prisma.json`, `Borealis-Bench/mlr/plan-initial-2027.md`, 9 API ouvertes dont 5 productives et 3 en statut F sans contournement `A4`, 160 textes intégraux OA hachés `SHA-256`, 0,0 % de résumé seul), exécutée en régime `100 %` IA sans comité de lecture humain.
- **Des émetteurs lus de seconde main.** Les sites de Gartner, de McKinsey, de MarketsandMarkets et de l’ISO ont refusé l’accès : leurs chiffres viennent de reprises, nommées dans les sources.
- **Des calculs propres à l’ouvrage.** L’enveloppe des estimations de marché, la somme des dépenses d’investissement et les conversions d’unités du chapitre 49 ne figurent dans aucune source; le texte les signale.

**Sources d’ancrage de la partie X**

- METR — horizons temporels des tâches et son fichier de données (49)
- IETF — groupes de travail agentproto et dawn (49)
- NIST — IR 8547, version finale (49)
- Commission européenne — calendrier de mise en œuvre de l’AI Act (49)
- Statistique Canada — utilisation de l’IA par les entreprises, deuxième trimestre de 2026 (50)
- Stanford HAI — AI Index Report 2026, chapitre 4 (50)
- Cemri et coll. — Why Do Multi-Agent LLM Systems Fail?, NeurIPS 2025 (48)
- Debenedetti et coll. — Defeating Prompt Injections by Design, IEEE SaTML 2026 (48)
- Peters-Gill et coll. — Can CaMeLs Talk?, prépublication (49)
- Yue et coll. — Building MCP-native hierarchical AI scientist ecosystems, Frontiers in AI 2026 (48, texte intégral OA `MLR-0034`)
- Tajik et coll. — Disagreement as Data: Reasoning Trace Analytics in Multi-Agent Systems, ACM L@S 2026 (48, texte intégral OA `MLR-0044`)

- Bamouh et coll. — Towards Orchestrating LLM-based Multi-Agent Systems with SysML v2, ER 2026 (Springer) (48, texte intégral OA `MLR-0091`)
- Dang et coll. — LLM4Schema.org : Generating Schema.org Markups with Large Language Models, Semantic Web 2025 (48, texte intégral OA `MLR-0121`)
- He et coll. — Tracing MCP Security Vulnerabilities, IEEE SPW 2026 (48, texte intégral OA `MLR-0093`)
- Clusmann et coll. — Prompt injection attacks on vision language models in oncology, Nature Communications 2025 (48, texte intégral OA `MLR-0129`)
- Lioliou et coll. — Governance under Algorithmic Opacity: How Financial Firms Construct Accountability and Control around AI in Risk Disclosures, Information Systems Frontiers 2026 (48, texte intégral OA `MLR-0059`)
- Espie et coll. — A Differentiated Approach for Post-Quantum DNSSEC, ACM ASIA CCS 2026 (48, texte intégral OA `MLR-0001`)
- del Pino et Niot — Finally! A Compact Lattice-Based Threshold Signature, PKC 2025 (Springer) (48, texte intégral OA `MLR-0113`)
- Karcz et coll. — Exploring hardware implementation feasibility of post-quantum cryptography (ML-KEM, ML-DSA, SLH-DSA), PLOS One 2026 (48, texte intégral OA `MLR-0056`)

**Points de la partie X à confirmer en priorité**

| Point | État de la preuve | Chapitres |
| --- | --- | --- |
| Chiffres des documents payants de Gartner sur l’IA agentique intégrée | Un seul blogue tiers; documents non accessibles | 50 |
| Calendrier de l’AI Act après le règlement modificatif | Pages d’information de la Commission; Journal officiel non lu | 49, 50 |
| Scores affichés par ARC Prize à l’automne 2026 | Page qui ne distingue pas les résultats vérifiés; annonce officielle prévue le 4 décembre 2026 | 49 |
| Agents sortis de leur confinement en juillet 2026 | Recension de l’OWASP; divulgations d’origine non ouvertes | 49 |
| Garanties d’isolation qui ne se composent pas entre agents | Une prépublication, non répliquée | 49 |
| Norme chinoise obligatoire sur les agents | Média d’État citant un registre non ouvert | 49 |
| Indépendance des estimations de marché | Hypothèse de l’ouvrage, tirée d’une seule note de méthode | 50 |
