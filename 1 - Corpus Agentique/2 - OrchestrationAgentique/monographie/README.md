# L'autonomie encadrée

**Interopérabilité et orchestration agentique dans les services financiers canadiens — protocoles ouverts, cadre réglementaire et blueprint d'intégration d'entreprise (état des lieux 2024-2026)**

| Champ | Valeur |
|---|---|
| Version | millésime **`mono-v1.0`** — ⚠ millésime éditorial, l'**étiquette git n'a pas été posée** ([`CLAUDE.md`](../CLAUDE.md)) |
| Date de publication | 17 juillet 2026 |
| Dates de gel | 16 juillet 2026 (22 pièces) ; 17 juillet 2026 (7 pièces) — registre : [`99-registre-gel.md`](99-registre-gel.md) |
| Volumétrie | **92 059 mots** sur 29 pièces — mesure du 17 juillet 2026, après la passe corrective de l'[audit global](../doc/audit.md) (méthode et commande de référence : [PRDPlan §4.2](../doc/PRDPlan.md), dont le défaut connu y est documenté) |
| Socle factuel | **46 entrées** F-01 à F-48 ([PRD §7](../doc/PRD.md)) |
| Conformité | **CA-1 à CA-8 : 8/8** — ⚠ **partiellement démenti** par l'audit du 17 juillet 2026 (CA-1 et CA-7 portaient des écarts, depuis corrigés) : voir l'addendum de [`verification/relecture-CA.md`](../verification/relecture-CA.md) |
| Revalidation | 17 juillet 2026 ([`verification/revalidation-2026-07-17.md`](../verification/revalidation-2026-07-17.md)) |

**Commencer par l'[avant-propos](00-avant-propos.md).** Il expose la méthode, les niveaux de preuve, la convention de datation et les avertissements — sans lesquels les chapitres se lisent mal. Le **[chapitre 13](03-partie-III/ch-13-pont-frames.md)** est le pivot de l'ouvrage : c'est le chapitre à contester en premier.

---

## Ordre de lecture

| # | Pièce | Fichier |
|---|---|---|
| — | **Avant-propos et note méthodologique** | [`00-avant-propos.md`](00-avant-propos.md) |
| | **Partie I — Fondements : les protocoles d'interopérabilité agentique** | |
| 1 | Généalogie et gouvernance : des projets propriétaires aux standards ouverts | [`ch-01`](01-partie-I/ch-01-genealogie-gouvernance.md) |
| 2 | Anatomie technique : MCP et A2A v1.0, une complémentarité déclarée | [`ch-02`](01-partie-I/ch-02-anatomie-mcp-a2a.md) |
| 3 | La transaction agentique et la couche d'infrastructure : AP2 et AGNTCY | [`ch-03`](01-partie-I/ch-03-ap2-agntcy-acp.md) |
| 4 | Taxonomie des risques protocolaires | [`ch-04`](01-partie-I/ch-04-risques-protocolaires.md) |
| | **Partie II — L'orchestration multi-agents en entreprise** | |
| 5 | Les options d'orchestration : la taxonomie OO1–OO4 | [`ch-05`](02-partie-II/ch-05-options-orchestration.md) |
| 6 | L'autonomie encadrée : le paradigme APM | [`ch-06`](02-partie-II/ch-06-autonomie-encadree.md) |
| 7 | Réalisations : les frameworks d'orchestration d'entreprise | [`ch-07`](02-partie-II/ch-07-frameworks.md) |
| 8 | L'identité et les registres d'agents | [`ch-08`](02-partie-II/ch-08-identite-registres.md) |
| | **Partie III — Le cadre réglementaire canadien** | |
| 9 | E-23 : le risque de modèle à l'ère de l'IA | [`ch-09`](03-partie-III/ch-09-e23-risque-modele.md) |
| 10 | Le vide fédéral : de C-27 à C-36 | [`ch-10`](03-partie-III/ch-10-vide-federal-c36.md) |
| 11 | Québec : la ligne directrice IA de l'AMF et l'article 12.1 de la Loi 25 | [`ch-11`](03-partie-III/ch-11-quebec-amf-loi25.md) |
| 12 | Valeurs mobilières : l'avis ACVM 11-348 | [`ch-12`](03-partie-III/ch-12-acvm-11-348.md) |
| **13** | **Le pont : des contraintes réglementaires aux frames déterministes** *(pivot)* | [`ch-13`](03-partie-III/ch-13-pont-frames.md) |
| | **Partie IV — L'interopérabilité financière canadienne** | |
| 14 | Le cadre des services bancaires axés sur le consommateur | [`ch-14`](04-partie-IV/ch-14-cadre-bancaire.md) |
| 15 | ISO 20022 : Lynx accompli, RTR imminent | [`ch-15`](04-partie-IV/ch-15-iso20022-lynx-rtr.md) |
| 16 | Prospective : AP2 sur les rails canadiens ? | [`ch-16`](04-partie-IV/ch-16-ap2-rails.md) |
| | **Partie V — L'adoption par les institutions financières canadiennes** | |
| 17 | Études de cas : la production agentique canadienne (2025-2026) | [`ch-17`](05-partie-V/ch-17-etudes-de-cas.md) |
| | **Partie VI — Synthèse : l'architecture de référence** | |
| 18 | La matrice protocoles × exigences réglementaires | [`ch-18`](06-partie-VI/ch-18-matrice.md) |
| 19 | L'architecture de référence par couches | [`ch-19`](06-partie-VI/ch-19-architecture-reference.md) |
| 20 | Instrumentation et feuille de route vers le 1er mai 2027 | [`ch-20`](06-partie-VI/ch-20-instrumentation-feuille-route.md) |
| 21 | La frontière de la connaissance vérifiable | [`ch-21`](06-partie-VI/ch-21-frontiere.md) |
| | **Partie VII — Le blueprint : plateforme d'intégration d'entreprise (instanciation IBM)** | |
| 22 | Principes directeurs et vue en couches (C1–C8) | [`ch-22`](07-partie-VII/ch-22-principes-couches.md) |
| 23 | Correspondance réglementaire et flux illustratifs | [`ch-23`](07-partie-VII/ch-23-correspondance-flux.md) |
| 24 | Lacunes du blueprint et conditions de revalidation | [`ch-24`](07-partie-VII/ch-24-lacunes-revalidation.md) |
| | **Annexes** | |
| A | Méthodologie de constitution du socle | [`annexe-a`](90-annexes/annexe-a-methodologie.md) |
| B | Matrice détaillée protocoles × réglementation | [`annexe-b`](90-annexes/annexe-b-matrice.md) |
| C | Chronologie réglementaire et normative 2023-2027 | [`annexe-c`](90-annexes/annexe-c-chronologie.md) |
| D | Glossaire bilingue — **§D.1 et §D.7 font autorité** | [`annexe-d`](90-annexes/annexe-d-glossaire.md) |

---

## Avertissements

Ils sont développés dans l'[avant-propos](00-avant-propos.md) ; en voici la substance.

- **Aucun avis juridique, aucun conseil d'investissement.** L'ouvrage rapporte des textes et en propose des lectures d'architecture. Ces lectures engagent l'auteur, jamais le régulateur.
- **Aucune recommandation de fournisseur.** La Partie VII instancie un blueprint sur le portefeuille d'IBM : c'est un **cas documenté par sources primaires**, retenu parce que sa documentation publique permettait de tracer chaque composant. Ce n'est pas un verdict comparatif.
- **L'ouvrage se périme par morceaux.** Chaque pièce porte sa date de gel. Une révision majeure de la spécification MCP est confirmée pour le **28 juillet 2026** — douze jours après le gel des chapitres 1, 2 et 7, qui décrivent donc en connaissance de cause un état déjà daté. Les conditions de péremption et le protocole de revalidation sont au [chapitre 24](07-partie-VII/ch-24-lacunes-revalidation.md).
- **Onze lacunes ouvertes** sont exposées plutôt que comblées ([chapitre 21](06-partie-VI/ch-21-frontiere.md)). La plus coûteuse : le contenu de la ligne directrice sur l'IA de l'AMF n'est pas au socle, et l'ouvrage n'en dérive aucune contrainte.

## Comment cet ouvrage a été vérifié

Chaque affirmation factuelle centrale renvoie à une entrée du socle (F-xx), et chaque entrée porte son niveau de preuve : **[A]** vote adversarial 3-0, **[B]** source primaire lue et extraite sans vote, **[C]** repérage à confirmer. **[A] > [B] > [C]** — le niveau ne mesure pas la qualité de la source, mais **ce que l'affirmation a subi**.

Les 29 pièces ont chacune passé la boucle qualité de [PRDPlan §4.2](../doc/PRDPlan.md), dont une **relecture adversariale par un relecteur distinct du rédacteur**. La grille [CA-1..CA-8](../verification/relecture-CA.md) consigne les contrôles exécutés — et les écarts qu'ils ont trouvés, corrigés plutôt qu'absorbés.

Un résultat de cette vérification mérite d'être donné au lecteur, parce qu'il dit ce que vaut le reste : **tous les défauts lourds trouvés à la publication l'ont été par des relecteurs adversariaux, aucun par l'auto-contrôle de leur rédacteur.**

## Gouvernance

[`doc/PRD.md`](../doc/PRD.md) (autorité de contenu — socle, garde-fous, critères) · [`doc/PRDPlan.md`](../doc/PRDPlan.md) (exécution) · [`doc/TOC.md`](../doc/TOC.md) (découpage, thèses, volumétrie) · [`CLAUDE.md`](../CLAUDE.md) (conventions). En cas de conflit, **le PRD prime**.

Ce fichier est l'**index de lecture** des 29 pièces, et rien d'autre : la gouvernance, le pipeline de rendu et la procédure de reprise sont au [`README.md`](../README.md) et au [`CLAUDE.md`](../CLAUDE.md) du volume ; la place du volume dans le corpus est au [README du dépôt](../../../README.md).
