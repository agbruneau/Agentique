# 5 - Recension — l'état de l'art en services financiers

Un document, son abrégé en cinq planches, et le graveur de leurs figures.
[*État de l'art en services financiers*](%C3%89tat%20de%20l%27art%20%E2%80%94%20services%20financiers.md) dresse l'état de l'interopérabilité et
de l'orchestration agentiques pour une coopérative financière canadienne régie — caisses, fédération, filiales d'assurance et de
courtage —, faits arrêtés au 20 août 2026, chaque affirmation confrontée à sa source primaire ou déclarée inatteignable. Thèse : le
débat porte sur la pile protocolaire ; dans une coopérative régie, la pile n'est pas ce qui décide.
[*Cinq schémas*](Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.md) reprend ses cinq figures et les explique.

**Statut :** livrable, planche comprise (Vol. VIII) — fixé le 15 septembre 2026 par la décision [D-18](../2%20-%20Compendium/PRD/PRD.md#d-18) ;
dépôt rouvert le même jour par [D-17](../2%20-%20Compendium/PRD/PRD.md#d-17). Ni relecteur distinct du rédacteur, ni ronde adverse.

| Pièce | Rendus | Contenu |
|---|---|---|
| État de l'art | [PDF](%C3%89tat%20de%20l%27art%20%E2%80%94%20services%20financiers.pdf), 186 p. | 15 sections numérotées, 312 notices pour 311 documents, 11 tableaux, 5 figures, 14 questions ouvertes |
| Cinq schémas | [PDF](Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.pdf), 7 p. · [HTML](Cinq%20sch%C3%A9mas%20%E2%80%94%20%C3%A9tat%20de%20l%27art%20en%20services%20financiers.html) autonome | les cinq figures commentées ; aucun régime de preuve propre, celui du document long |

**Par où entrer :** la planche, cinq minutes ; puis le sommaire exécutif du document long. Deux faits négatifs y conditionnent la
lecture : le domaine du régulateur québécois a refusé la consultation automatisée, et deux lignes directrices n'ont cédé qu'à un service
tiers d'extraction ; aucune source consultée n'établit de lien documenté entre un protocole d'agents et une exigence sectorielle canadienne.

**Refaire :** depuis ce dossier, `bash build/build-pdf.sh` recompose les deux PDF, `etat` ou `planche` pour un seul, et mesure leur page
de titre ; `bash build/build-pdf.sh html` refait le `.html` de la planche avec [`build/recension.css`](build/recension.css) ;
`python figures/dessine.py` regrave les cinq figures, qui ne se retouchent pas à la main.

**Vérifier :** le seul contrôle qui s'applique ici est `check-resume.py`, de [`3 - Veille/Python/`](../3%20-%20Veille/Python/), sur la page de
titre des deux rendus ; il sort 0, et « LIMITE » sur la planche, que la moindre reprise ferait déborder ([`APPAREIL.md`](../APPAREIL.md)).
Rien n'oppose la bibliographie au corps, ni la pagination à une cible.

**Journal :** [`JOURNAL.md`](JOURNAL.md) — le dossier détruit le 19 août 2026 et celui qui porte son nom depuis le 20, les corrections des
notices, les recompositions, les relevés datés du contrôle de page de titre et les réserves.
