# Volume II — Orchestration agentique

**Lire :** [`Monographie.pdf`](Monographie.pdf) (387 p.) — ou pièce par pièce, depuis l'[index de lecture](monographie/README.md).

Monographie sur l'interopérabilité et l'orchestration agentiques dans les services financiers canadiens : protocoles ouverts (MCP,
A2A, AP2, AGNTCY), cadre réglementaire canadien (E-23, AMF, ACVM, Loi 25) et blueprint d'intégration d'entreprise, état des lieux
2024-2026. Thèse : l'autonomie encadrée — sous exigence réglementaire stricte, le cadre déterministe invoque les agents, jamais
l'inverse. Son résultat le plus citable est négatif : trois protocoles croisés avec cinq corpus de textes canadiens, quinze
croisements, aucun lien documenté par source primaire. Il présuppose le [Vol. I](../1%20-%20InteroperabiliteAgentique/).

**Statut :** livrable — fixé le 15 septembre 2026 par la décision [D-18](../../2%20-%20Compendium/PRD/PRD.md#d-18) ; dépôt rouvert le
même jour par [D-17](../../2%20-%20Compendium/PRD/PRD.md#d-17). Aucun relecteur humain nommé.

| Champ | Valeur |
|---|---|
| Pièces | 29 sous [`monographie/`](monographie/) : avant-propos, 24 chapitres en sept parties, annexes A à D |
| Gel | 16 juillet 2026 pour 22 pièces, 17 juillet pour 7 — [registre des gels](monographie/99-registre-gel.md) |
| Socle factuel | 46 entrées, F-01 à F-48, au [PRD](prd/PRD.md) §7 |
| Niveaux de preuve | [H] lu et non réfuté par un relecteur humain nommé, que nulle entrée ne porte ; [A-i] réfutation tentée par trois instances de modèle ; [B] source primaire extraite ; [C] repérage |
| Millésime | `mono-v1.0`, du 17 juillet 2026 ; l'étiquette git du même nom marque l'arbre du 8 août |

**Par où entrer :** l'[avant-propos](monographie/00-avant-propos.md), puis le [chapitre 13](monographie/03-partie-III/ch-13-pont-frames.md), pivot
de l'ouvrage et premier à contester. La gouvernance, par ordre d'autorité : [`PRD.md`](prd/PRD.md), [`PRDPlan.md`](prd/PRDPlan.md),
[`TOC.md`](prd/TOC.md) ; les revalidations et la grille CA-1 à CA-8 sous [`verification/`](verification/).

**Refaire :** depuis ce dossier, `python build/assemble.py` réunit les 29 pièces en `Monographie.md`, puis
`bash build/build-pdf.sh Monographie.md` recompose le PDF. L'intégration continue rejoue l'assemblage et exige un `Monographie.md`
identique à l'octet.

**Journal :** [`JOURNAL.md`](JOURNAL.md) — renommage du volume, pose de l'étiquette `mono-v1.0`, renvois repointés, correctifs de
l'assembleur, clôture et réouverture, et l'index de lecture tel qu'il était écrit au 15 septembre 2026.
