# Livre IV — Appliquer, exploiter, produire et composer : AgentMesh, AgentOps, fabrique d'agents et synthèse architecturale

Le quatrième des cinq Livres du [Vol. IV](../README.md) : dix chapitres — le maillage d'agents et l'exploitation (ch. 37-40), la
fabrique d'agents (ch. 41), la synthèse architecturale et le blueprint (ch. 42-46). Chaque pièce existe en `.md`, la source qui fait
foi et seule à porter l'appareil, et en `.html`, page autonome. Le cahier des charges de chaque chapitre est son entrée au
[`TOC.md`](../PRD/TOC.md), qui prime.

**Statut :** archive de travail, hors compte des livrables — le Vol. IV entier, par la décision [D-18](../PRD/PRD.md#d-18) du
15 septembre 2026. Les dix pièces sont rédigées et arbitrées hors portes, brouillon non publiable ; le ch. 41 est de la matière neuve,
sans volume source ni socle hérité.

| Ch. | Pièce | Capacité |
|---|---|---|
| 37 | [Le maillage d'agents : du *service mesh* au point d'application (PEP/PDP et *zero trust* agentique)](37-maillage-agents-point-application.md) · [html](37-maillage-agents-point-application.html) | appliquer |
| 38 | [L'observabilité agentique](38-observabilite-agentique.md) · [html](38-observabilite-agentique.html) | exploiter |
| 39 | [Le cycle de vie opérationnel : évaluation continue, dérive et incident](39-cycle-de-vie-operationnel.md) · [html](39-cycle-de-vie-operationnel.html) | exploiter |
| 40 | [Les indicateurs de l'AgentOps et le FinOps des agents](40-indicateurs-agentops-finops.md) · [html](40-indicateurs-agentops-finops.html) | exploiter |
| 41 | [La fabrique d'agents : produire, certifier et réémettre le parc](41-fabrique-agents.md) · [html](41-fabrique-agents.html) | produire |
| 42 | [La matrice protocoles × exigences réglementaires](42-matrice-protocoles-exigences.md) · [html](42-matrice-protocoles-exigences.html) | composer |
| 43 | [L'architecture de référence unifiée par couches](43-architecture-reference-couches.md) · [html](43-architecture-reference-couches.html) | composer |
| 44 | [La formalisation ArchiMate](44-formalisation-archimate.md) · [html](44-formalisation-archimate.html) | composer |
| 45 | [Le blueprint instancié et son cycle de vie : de Boréalis au portefeuille IBM, puis la naissance, la vie et la mort d'un agent d'entreprise](45-blueprint-instancie-cycle-de-vie.md) · [html](45-blueprint-instancie-cycle-de-vie.html) | composer |
| 46 | [Instrumentation et feuille de route vers le 1ᵉʳ mai 2027](46-instrumentation-feuille-route.md) · [html](46-instrumentation-feuille-route.html) | composer |

Volumétrie : 60 025 mots de corps, mesurés par [`decompte.sh`](../PRD/decompte.sh) et reportés ici par `reporter-volumetrie.py`, pour une
enveloppe de Livre de 69 000 au TOC, soit −13,0 %.

**Par où entrer :** le ch. 37, où le passeport d'agent devient opposable à chaque arête du maillage ; puis le ch. 43, l'architecture
de référence qui compose protocoles, identité, orchestration, maillage, exploitation et gouvernance.

**Refaire et vérifier :** depuis `2 - Compendium/`, `python build/rendre-piece.py "Livre IV/<pièce>.md"` régénère un `.html`, qui ne
s'édite jamais à la main, et `python build/verifier-piece.py` l'oppose à sa source ; les contrôles du volume sont à sa [page d'accueil](../README.md).

**Journal :** [la page de ce Livre au journal du volume](../JOURNAL.md#page-livre-iv) — clôture et arrêt, la collision de numérotation
des remontées et sa carte, volumétrie datée, sièges posés pour la somme, remontées soldées et passe de correction de juillet 2026.
