# Livre I — Coopérer : fondements de l'interopérabilité et couche protocolaire agentique

Le premier des cinq Livres du [Vol. IV](../README.md) : onze chapitres en deux mouvements, les fondements (ch. 1-6) puis la couche
protocolaire agentique (ch. 7-11). Chaque pièce existe en `.md`, la source qui fait foi et seule à porter l'appareil, et en `.html`,
page autonome qui se lit hors ligne. Le cahier des charges de chaque chapitre est son entrée au [`TOC.md`](../PRD/TOC.md), qui prime.

**Statut :** archive de travail, hors compte des livrables — le Vol. IV entier, par la décision [D-18](../PRD/PRD.md#d-18) du
15 septembre 2026. Les onze pièces sont rédigées et arbitrées hors portes, brouillon non publiable ; aucun énoncé n'y est central au
sens de CA-IV-01.

| Ch. | Pièce | Mouvement |
|---|---|---|
| 1 | [L'interopérabilité comme problème d'intégration d'entreprise](01-interoperabilite-integration-entreprise.md) · [html](01-interoperabilite-integration-entreprise.html) | fondements |
| 2 | [Données, sémantique et ontologies](02-donnees-semantique-ontologies.md) · [html](02-donnees-semantique-ontologies.html) | fondements |
| 3 | [Sécurité, identité et gouvernance de l'interopérabilité](03-securite-identite-gouvernance.md) · [html](03-securite-identite-gouvernance.html) | fondements |
| 4 | [L'ingénierie des systèmes agentiques : anatomie, raisonnement, outils](04-ingenierie-systemes-agentiques.md) · [html](04-ingenierie-systemes-agentiques.html) | fondements |
| 5 | [Ancrage informationnel : mémoire, contexte, RAG agentique](05-ancrage-informationnel.md) · [html](05-ancrage-informationnel.html) | fondements |
| 6 | [Systèmes multi-agents, évaluation et sûreté](06-multi-agents-evaluation-surete.md) · [html](06-multi-agents-evaluation-surete.html) | fondements |
| 7 | [Généalogie et gouvernance : des projets propriétaires aux standards ouverts](07-genealogie-gouvernance.md) · [html](07-genealogie-gouvernance.html) | couche protocolaire |
| 8 | [Anatomie : MCP (agent-outil) et A2A (agent-agent)](08-anatomie-mcp-a2a.md) · [html](08-anatomie-mcp-a2a.html) | couche protocolaire |
| 9 | [Découverte, registres, portabilité et pile protocolaire](09-decouverte-registres-pile.md) · [html](09-decouverte-registres-pile.html) | couche protocolaire |
| 10 | [Transaction et infrastructure : AP2 et AGNTCY](10-transaction-infrastructure.md) · [html](10-transaction-infrastructure.html) | couche protocolaire |
| 11 | [Modes d'échec et taxonomie des risques protocolaires](11-modes-echec-risques-protocolaires.md) · [html](11-modes-echec-risques-protocolaires.html) | couche protocolaire |

Volumétrie : 72 584 mots de corps, mesurés par [`decompte.sh`](../PRD/decompte.sh) et reportés ici par `reporter-volumetrie.py`, pour une
enveloppe de Livre de 65 000 au TOC, soit +11,7 %.

**Par où entrer :** le ch. 1, puis le ch. 3, charnière de l'héritage IAM auquel les Livres II et IV renvoient sans le reconstruire ;
le ch. 7 porte au § 7.5, pour toute la somme, l'encadré de désambiguïsation du garde-fou R-8.

**Refaire et vérifier :** depuis `2 - Compendium/`, `python build/rendre-piece.py "Livre I/<pièce>.md"` régénère un `.html`, qui ne
s'édite jamais à la main, et `python build/verifier-piece.py` l'oppose à sa source ; les contrôles du volume sont à sa
[page d'accueil](../README.md).

**Journal :** [la page de ce Livre au journal du volume](../JOURNAL.md#page-livre-i) — clôture et arrêt, remontées soldées le
27 juillet 2026, passe de correction du 28, volumétrie datée, périmètre couvert et procédure d'ajout d'une pièce.
