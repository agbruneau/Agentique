# Livre V — Livrer et clore : l'agent comme livrable logiciel, horizon et frontière

Le dernier des cinq Livres du [Vol. IV](../README.md) : quatre chapitres en deux mouvements — l'agent comme livrable logiciel (ch. 47-48),
l'horizon et la frontière de la connaissance vérifiable (ch. 49-50). Chaque pièce existe en `.md`, la source qui fait foi et seule à
porter l'appareil, et en `.html`, page autonome. Le cahier des charges de chaque chapitre est son entrée au [`TOC.md`](../PRD/TOC.md), qui prime.

**Statut :** archive de travail, hors compte des livrables — le Vol. IV entier, par la décision [D-18](../PRD/PRD.md#d-18) du
15 septembre 2026. Les quatre pièces sont rédigées et arbitrées hors portes, brouillon non publiable. Le premier mouvement est de la
matière neuve, sans volume source ni socle, et sa publication est bloquée par la décision d'auteur D-3 du [PRD](../PRD/PRD.md).

| Ch. | Pièce | Mouvement |
|---|---|---|
| 47 | [L'artefact livré : provenance des composants et mise en service](47-artefact-livre-provenance-mise-en-service.md) · [html](47-artefact-livre-provenance-mise-en-service.html) | livrer |
| 48 | [La sémantique d'effet : idempotence, compensation, réconciliation](48-semantique-effet-idempotence-compensation.md) · [html](48-semantique-effet-idempotence-compensation.html) | livrer |
| 49 | [L'horizon 2027-2032 et la frontière de la connaissance vérifiable](49-horizon-frontiere-connaissance-verifiable.md) · [html](49-horizon-frontiere-connaissance-verifiable.html) | horizon et frontière |
| 50 | [Péremption et protocole de revalidation](50-peremption-protocole-revalidation.md) · [html](50-peremption-protocole-revalidation.html) | horizon et frontière |

Volumétrie : 31 710 mots de corps, mesurés par [`decompte.sh`](../PRD/decompte.sh) et reportés ici par `reporter-volumetrie.py`, pour une
enveloppe de Livre de 34 000 au TOC, soit −6,7 %.

**Par où entrer :** le ch. 48, ce qui advient quand un virement réussit à moitié ; puis le ch. 49, qui réunit en un registre les lacunes
des trois volumes sources ; le ch. 50, dernier de la somme, dit ce qui la périme et comment la revalider.

**Refaire et vérifier :** depuis `2 - Compendium/`, `python build/rendre-piece.py "Livre V/<pièce>.md"` régénère un `.html`, qui ne
s'édite jamais à la main, et `python build/verifier-piece.py` l'oppose à sa source ; les contrôles du volume sont à sa [page d'accueil](../README.md).

**Journal :** [la page de ce Livre au journal du volume](../JOURNAL.md#page-livre-v) — clôture et arrêt, état des portes, volumétrie
datée et écart en défaut, sièges posés pour la somme, remontées soldées et passe de correction de juillet 2026.
