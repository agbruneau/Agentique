# Annexe E — Bibliographie et niveaux de preuve

> Cette annexe complète les listes de sources des chapitres : elle dit comment les lire et rappelle les sources d'ancrage.

## E.1 Niveaux de preuve

Chaque chapitre se termine par ses sources numérotées et par une section « Limites de ce chapitre ». Les chapitres 1 à 47 en listent 775 au total (la partie X est décomptée à la section E.4); une source citée par plusieurs chapitres compte pour chacun.

Trois marques qualifient une affirmation.

| Marque | Sens | Usage |
|---|---|---|
| Primaire | Page de l'émetteur (spécification, texte officiel, article, documentation), lue pour le chapitre | Peut fonder une décision, dans les limites de la page |
| Secondaire | Compte rendu, analyse ou résumé d'un tiers | Signale un fait; à confirmer à la source avant d'agir |
| Non confirmé | Point qu'aucune page lue n'établit | Nommé dans les limites du chapitre; à ne pas reprendre |

La nature de la source compte aussi, de la plus solide à la plus fragile : texte normatif ou officiel; article évalué par les pairs; prépublication; documentation d'un éditeur sur son produit; billet d'éditeur, note d'analyste ou presse. Le chapitre 42 propose un classement voisin, en six niveaux, pour les études de cas.

Cinq réserves valent pour tout l'ouvrage.

- **Lecture par extraction.** La plupart des pages ont été lues et relues par un outil qui en condense le contenu. Un chiffre ou un niveau d'obligation se revérifie sur le texte intégral.
- **Résumés seulement.** Plusieurs articles ne sont connus que par leur résumé, ce que leur source signale.
- **Audit partiel.** L'audit n'a relu qu'une partie des sources; EUR-Lex, McKinsey, Gartner et ServiceNow sont restés inaccessibles. Les limites de chaque chapitre nomment les sources non revérifiées.
- **Documentation d'éditeur.** Elle décrit ce qu'un produit annonce. Aucun essai indépendant n'est cité pour les moteurs d'exécution durable, les passerelles ou l'interopérabilité entre plateformes (chapitres 18, 24 et 26).
- **Date de référence.** Les faits sont arrêtés au 11 novembre 2026 (13 novembre pour la partie X); les relectures de l'audit et les sources des chapitres 44 à 47 datent du 12; des compléments, signalés dans les sources et les limites de vingt chapitres, datent du 14. Brouillons et préversions ont pu changer depuis.

## E.2 Sources d'ancrage

Entre parenthèses : ceux des chapitres 1 à 47 qui citent cette adresse; d'autres en citent une autre version (HTML d'arXiv, PDF, brouillon).

**Protocoles et standards**

- [MCP — spécification `2026-07-28`, architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md) (5) et [feuille de route du 22 août 2026](https://modelcontextprotocol.io/development/roadmap.md) (5, 13, 19, 27, 29, 30, 43)
- [A2A — spécification](https://a2a-protocol.org/latest/specification/) (3, 6, 8, 19)
- [Agentic AI Foundation — projets](https://aaif.io/projects) (1, 3–7, 11, 13, 24, 27, 43, 44)
- [AG-UI — introduction](https://docs.ag-ui.com/introduction) et [AGNTCY — documentation](https://docs.agntcy.org/) (7)
- [AP2 — spécification v0.2](https://ap2-protocol.org/ap2/specification/) et [x402 — introduction](https://docs.x402.org/introduction) (10)
- [Agent Skills — spécification](https://agentskills.io/specification) (13, 27)
- [NIST — AI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative) (1, 3, 4, 11, 35, 43)

**Identité et sécurité**

- [RFC 8693 — OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693.html) (29, 30) et [RFC 9449 — DPoP](https://www.rfc-editor.org/rfc/rfc9449.html) (29)
- [IETF — draft-ietf-wimse-aims](https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/) (3, 11, 29) et [draft-ietf-oauth-identity-assertion-authz-grant](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/) (11, 29)
- [OWASP — annonce du Top 10 for Agentic Applications](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) (14, 31) et [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (31)
- [OpenTelemetry — conventions sémantiques GenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/), page déplacée vers le [dépôt `semantic-conventions-genai`](https://github.com/open-telemetry/semantic-conventions-genai) (33, 43)

**Recherche**

- [Cemri et coll. — Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/html/2503.13657v2), taxonomie MAST (3, 4, 12, 21)
- [Pan et coll. — Measuring Agents in Production](https://arxiv.org/abs/2512.04123), étude MAP (1, 4, 17, 41, 43)
- [Kim et coll. — Towards a Science of Scaling Agent Systems](https://arxiv.org/html/2512.08296v3) (16, 21)
- [Kang et Diponegoro — Governance Gaps in Agent Interoperability Protocols](https://arxiv.org/abs/2606.31498) (2, 7, 11, 43)
- [Nubank — Building Customer Support AI Agents at 100M-User Scale](https://arxiv.org/html/2606.08867v1) (33, 42)
- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (1, 16, 17)

**Cadres et droit**

- [Règlement (UE) 2026/1744, Digital Omnibus sur l'IA](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) (35)
- [IMDA — Model AI Governance Framework for Agentic AI, version 1.5](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) (1, 3, 22, 39)
- [BSIF — ligne directrice E-23](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027) (38, 39) et sa [lettre d'accompagnement](https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027-letter) (38, 43)
- [Canada — lancement de la stratégie « AI for All »](https://www.pm.gc.ca/en/news/news-releases/2026/06/04/prime-minister-carney-launches-ai-all-canadas-new-national-artificial) (38)
- [Québec, MCN — Guide sur l'utilisation responsable de l'IA agentique](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/cybersecurite_numerique/Intelligence_artificielle/GU_IA_Agentique.pdf) (22, 38, 39, 42)

## E.3 Points à confirmer en priorité

Ces affirmations des chapitres 1 à 47 portent beaucoup et reposent sur une preuve mince : ce sont les premières à revérifier; celles de la partie X sont à la section E.4.

| Point | État de la preuve | Chapitres |
|---|---|---|
| Texte de l'AI Act modifié par le règlement 2026/1744 | EUR-Lex illisible; lu par une prépublication ou une reproduction non officielle | 34, 35, 43 |
| Directive fédérale sur la prise de décisions automatisée | Page jamais lue (requête rejetée); champ d'application décrit d'après un guide | 22, 38 |
| Ligne directrice de l'AMF sur l'utilisation de l'IA | Texte jamais lu (erreur 403); deux analyses de cabinets | 38, 39, 49 |
| Sanctions du projet de loi C-36 | Document d'information; texte relu en partie | 38 |
| Chiffres des enquêtes McKinsey | Comptes rendus; pages de McKinsey non relues à la source | 1, 4, 39, 41 |
| Placement de ServiceNow au Magic Quadrant; ses offres en 2026 | Rapport non lu, reprises contradictoires; presse issue d'un breffage | 4, 26 |
| Usage de MCP et d'A2A en production | Communiqué qui ne nomme aucune organisation; aucun cas documenté | 6, 42 |

Le dernier point pèse sur la thèse de l'ouvrage : l'interopérabilité par protocoles ouverts est bien spécifiée et largement annoncée, mais sa pratique en production reste à documenter.

## E.4 Sources de la partie X

La partie X a été écrite le 13 novembre 2026, après la clôture des chapitres 1 à 47. Ses trois chapitres listent 244 sources, qui s'ajoutent aux 775 de la section E.1 sans y être comptées.

| Chapitre | Sources | Nature | Lecture |
|---|---|---|---|
| 48 — Revue de littérature | 101 | 31 publications en revue ou en conférence, 52 prépublications ou documents de travail, 3 sources reprises de l'ouvrage, 15 travaux relevés hors protocole le 14 novembre 2026 | Résumés seulement pour les 83 notices du protocole, dont titre, auteurs et lieu de publication sont confirmés auprès d'arXiv ou de Crossref pour 82; des quinze travaux hors protocole, six ne sont connus que par leur résumé |
| 49 — Veille technologique | 68 | 46 pages d'émetteur, 21 notices d'arXiv, 1 page tierce | Extraction par outil; sept sources relues à l'audit |
| 50 — Projection 2027-2030 et étude de marché | 75 | 51 pages d'émetteur, 24 pages tierces qui rapportent un émetteur non chargé | Extraction par outil; cinq sources relues à l'audit |

Trois réserves s'ajoutent à celles de la section E.1.

- **Une revue de cadrage, non une revue systématique.** Le chapitre 48 repose sur dix requêtes dans une seule base, et sur des résumés.
- **Des émetteurs lus de seconde main.** Les sites de Gartner, de McKinsey, de MarketsandMarkets et de l'ISO ont refusé l'accès : leurs chiffres viennent de reprises, nommées dans les sources.
- **Des calculs propres à l'ouvrage.** L'enveloppe des estimations de marché, la somme des dépenses d'investissement et les conversions d'unités du chapitre 49 ne figurent dans aucune source; le texte les signale.

**Sources d'ancrage de la partie X**

- [METR — horizons temporels des tâches](https://metr.org/time-horizons/) et son [fichier de données](https://metr.org/assets/benchmark_results_1_1.yaml) (49)
- IETF — groupes de travail [agentproto](https://datatracker.ietf.org/group/agentproto/about/) et [dawn](https://datatracker.ietf.org/group/dawn/about/) (49)
- [NIST — IR 8547, version finale](https://csrc.nist.gov/pubs/ir/8547/final) (49)
- [Commission européenne — calendrier de mise en œuvre de l'AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) (49)
- [Statistique Canada — utilisation de l'IA par les entreprises, deuxième trimestre de 2026](https://www150.statcan.gc.ca/n1/pub/11-621-m/11-621-m2026010-fra.htm) (50)
- [Stanford HAI — AI Index Report 2026, chapitre 4](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf) (50)
- [Cemri et coll. — Why Do Multi-Agent LLM Systems Fail?, NeurIPS 2025](https://doi.org/10.52202/085713-4082) (48)
- [Debenedetti et coll. — Defeating Prompt Injections by Design, IEEE SaTML 2026](https://doi.org/10.1109/satml68715.2026.00040) (48)
- [Peters-Gill et coll. — Can CaMeLs Talk?, prépublication](https://arxiv.org/abs/2610.05640) (49)

**Points de la partie X à confirmer en priorité**

| Point | État de la preuve | Chapitres |
|---|---|---|
| Chiffres des documents payants de Gartner sur l'IA agentique intégrée | Un seul blogue tiers; documents non accessibles | 50 |
| Calendrier de l'AI Act après le règlement modificatif | Pages d'information de la Commission; Journal officiel non lu | 49, 50 |
| Scores affichés par ARC Prize à l'automne 2026 | Page qui ne distingue pas les résultats vérifiés; annonce officielle prévue le 4 décembre 2026 | 49 |
| Agents sortis de leur confinement en juillet 2026 | Recension de l'OWASP; divulgations d'origine non ouvertes | 49 |
| Garanties d'isolation qui ne se composent pas entre agents | Une prépublication, non répliquée | 49 |
| Norme chinoise obligatoire sur les agents | Média d'État citant un registre non ouvert | 49 |
| Indépendance des estimations de marché | Hypothèse de l'ouvrage, tirée d'une seule note de méthode | 50 |
