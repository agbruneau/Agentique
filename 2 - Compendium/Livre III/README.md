# Livre III — Encadrer : orchestration en entreprise, cadre réglementaire canadien et terrain financier

Le troisième des cinq Livres du [Vol. IV](../README.md) : quinze chapitres en trois mouvements — l'autonomie encadrée (ch. 22-24), le
cadre réglementaire canadien (ch. 25-30), le terrain financier canadien (ch. 31-36). Chaque pièce existe en `.md`, la source qui fait
foi et seule à porter l'appareil, et en `.html`, page autonome. Le cahier des charges de chaque chapitre est son entrée au
[`TOC.md`](../PRD/TOC.md), qui prime.

**Statut :** archive de travail, hors compte des livrables — le Vol. IV entier, par la décision [D-18](../PRD/PRD.md#d-18) du
15 septembre 2026. Les quinze pièces sont rédigées et arbitrées hors portes, brouillon non publiable.

| Ch. | Pièce | Mouvement |
|---|---|---|
| 22 | [Options d'orchestration et paradigme APM : la taxonomie OO1-OO4 et l'autonomie encadrée](22-options-orchestration-paradigme-apm.md) · [html](22-options-orchestration-paradigme-apm.html) | autonomie encadrée |
| 23 | [Les frameworks d'orchestration d'entreprise](23-frameworks-orchestration-entreprise.md) · [html](23-frameworks-orchestration-entreprise.html) | autonomie encadrée |
| 24 | [Le passage à l'échelle de l'entreprise](24-passage-echelle-entreprise.md) · [html](24-passage-echelle-entreprise.html) | autonomie encadrée |
| 25 | [E-23 : le risque de modèle à l'ère de l'IA](25-e23-risque-modele.md) · [html](25-e23-risque-modele.html) | cadre réglementaire |
| 26 | [Le vide fédéral : de C-27 à C-36](26-vide-federal-c27-c36.md) · [html](26-vide-federal-c27-c36.html) | cadre réglementaire |
| 27 | [Québec : la ligne directrice IA de l'AMF et l'article 12.1 de la Loi 25](27-quebec-amf-article-12-1.md) · [html](27-quebec-amf-article-12-1.html) | cadre réglementaire |
| 28 | [Valeurs mobilières : l'avis ACVM 11-348](28-valeurs-mobilieres-acvm-11-348.md) · [html](28-valeurs-mobilieres-acvm-11-348.html) | cadre réglementaire |
| 29 | [Le pont : des contraintes réglementaires aux frames déterministes](29-pont-frames-deterministes.md) · [html](29-pont-frames-deterministes.html) | cadre réglementaire |
| 30 | [Le maillage réglementaire international et la normalisation institutionnelle](30-maillage-reglementaire-normalisation.md) · [html](30-maillage-reglementaire-normalisation.html) | cadre réglementaire |
| 31 | [Le vertical financier : pourquoi l'agentique y est durcie](31-vertical-financier-durcisseurs.md) · [html](31-vertical-financier-durcisseurs.html) | terrain canadien |
| 32 | [Le cadre des services bancaires axés sur le consommateur](32-cadre-bancaire-consommateur.md) · [html](32-cadre-bancaire-consommateur.html) | terrain canadien |
| 33 | [ISO 20022 : Lynx accompli, RTR visé](33-iso-20022-lynx-rtr.md) · [html](33-iso-20022-lynx-rtr.html) | terrain canadien |
| 34 | [Les sous-domaines financiers : banque, assurance, patrimoine](34-sous-domaines-financiers.md) · [html](34-sous-domaines-financiers.html) | terrain canadien |
| 35 | [Études de cas : la production agentique canadienne (2025-2026)](35-etudes-de-cas-production-canadienne.md) · [html](35-etudes-de-cas-production-canadienne.html) | terrain canadien |
| 36 | [Prospective : AP2 sur les rails canadiens ?](36-prospective-ap2-rails-canadiens.md) · [html](36-prospective-ap2-rails-canadiens.html) | terrain canadien |

Volumétrie : 100 354 mots de corps, mesurés par [`decompte.sh`](../PRD/decompte.sh) et reportés ici par `reporter-volumetrie.py`, pour
une enveloppe de Livre de 90 000 au TOC, soit +11,5 %.

**Par où entrer :** le ch. 22, qui place toute architecture agentique sur le continuum OO1-OO4 ; puis le ch. 29, le pont, pivot du
plan « encadrer », qui traduit les exigences canadiennes en frames déterministes d'architecture.

**Refaire et vérifier :** depuis `2 - Compendium/`, `python build/rendre-piece.py "Livre III/<pièce>.md"` régénère un `.html`, qui ne
s'édite jamais à la main, et `python build/verifier-piece.py` l'oppose à sa source ; les contrôles du volume sont à sa [page d'accueil](../README.md).

**Journal :** [la page de ce Livre au journal du volume](../JOURNAL.md#page-livre-iii) — clôture et arrêt, passe de correction du
28 juillet 2026, volumétrie datée, sièges posés pour la somme, remontées soldées le 27 juillet.
