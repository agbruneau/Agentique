# 1 - Collection — les trois monographies

Le triptyque du corpus : trois volumes conçus en progression — des protocoles à la réglementation, puis à l'organisation — qui
répondent ensemble à la question du [dépôt](../README.md). Chacun porte sa thèse, son socle factuel et ses dates de gel.

**Statut :** les trois sont livrables, le Vol. III sous réserve déclarée — fixé le 15 septembre 2026 par la décision
[D-18](../2%20-%20Compendium/PRD/PRD.md#d-18) ; dépôt rouvert le même jour par [D-17](../2%20-%20Compendium/PRD/PRD.md#d-17), re-clos le 16 septembre 2026 par [D-19](../2%20-%20Compendium/PRD/PRD.md#d-19). Aucun relecteur humain nommé.

| Vol. | Dossier | Thèse | Portée | Rendu |
|---|---|---|---|---|
| I | [`1 - InteroperabiliteAgentique/`](1%20-%20InteroperabiliteAgentique/) | l'autonomie graduée sous contrôle de finalité : l'agent prépare, l'humain ou le processus déterministe autorise | mondiale | 571 p. |
| II | [`2 - OrchestrationAgentique/`](2%20-%20OrchestrationAgentique/) | l'autonomie encadrée : sous exigence réglementaire, le cadre déterministe invoque les agents, jamais l'inverse | Canada, Québec | 390 p. |
| III | [`3 - EntrepriseAgentique/`](3%20-%20EntrepriseAgentique/) | la confiance ne se décrète pas, elle se fabrique : émettre une identité, l'appliquer, l'exploiter | organisation, identité non humaine | 428 p. |

**Par où entrer :** dans l'ordre I, II, III — le Vol. II présuppose le Vol. I, le Vol. III prolonge les deux sur leur verrou
commun, l'identité non humaine. Architecte : Vol. I, chapitre 1. Praticien canadien : Vol. II, chapitre 13, le pivot.
Responsable de l'identité : Vol. III, partie II, le passeport d'agent. Pour l'état du champ qui les recoupe, la
[veille technologique](../3%20-%20Veille/Veille%20Technologique.pdf).

[`0 - Références/`](0%20-%20R%C3%A9f%C3%A9rences/) porte le mémoire de maîtrise de l'auteur (1997), pièce déposée que nul document ne cite. Le Vol. IV,
qui réunit les trois en cinquante chapitres, est une archive de travail sous [`2 - Compendium/`](../2%20-%20Compendium/) : les trois volumes font foi.

**Refaire :** chaque volume se recompose de son dossier par `bash build/build-pdf.sh`, précédé aux Vol. II et III de
`python build/assemble.py`. Les trois chaînes sont des copies indépendantes : un correctif apporté à l'une ne se propage pas
aux autres. Le décompte commun des trois se vérifie depuis `2 - Compendium/` par `bash PRD/decompte.sh --verifier`.

**Journal :** [`JOURNAL.md`](JOURNAL.md) — la chronique des réouvertures du dépôt du 8 août au 5 septembre 2026, et la synthèse
consolidée des trois volumes telle qu'elle était écrite au 15 septembre 2026 : [vue d'ensemble](JOURNAL.md#vue-densemble),
[concepts transversaux](JOURNAL.md#concepts-transversaux), [recommandations](JOURNAL.md#recommandations-consolidées),
[volumétrie](JOURNAL.md#volumétrie-du-corpus).
